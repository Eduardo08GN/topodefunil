"""Motor de edicao: junta os takes -> tira silencio -> transcreve -> queima
legenda CapCut. Roda 100% offline (FFmpeg + auto-editor + faster-whisper).

Modelo de pasta:
  - Se a pasta de ENTRADA tem subpastas, cada subpasta = 1 video (seus arquivos
    de video, em ordem de nome, sao os takes).
  - Se a pasta de ENTRADA tem arquivos de video soltos, eles sao os takes de UM
    unico video.
O resultado vai pra pasta de SAIDA como <nome>.mp4.
"""

import os
import re
import sys
import json
import shutil
import zipfile
import tempfile
import subprocess

from captions import transcrever, gerar_ass, aqui_texto_para

FFMPEG = shutil.which("ffmpeg") or "ffmpeg"
FFPROBE = shutil.which("ffprobe") or "ffprobe"
VIDEO_EXT = (".mp4", ".mov", ".mkv", ".webm", ".m4v", ".avi")

# ⭐ ZOOM DE ENQUADRAMENTO — 2026-08-10, ordem do operador: *"quero que voce
# programe para ele ajustar o zoom dos videos para 104%, atualmente o tamanho
# natural chega como 100%"*, e *"e' o zoom no video INTEIRO"*.
# 1.04 = 4% de aproximacao, em TODOS os frames. O quadro e' ampliado e recortado
# no CENTRO de volta ao tamanho original, entao a resolucao de saida NAO muda —
# o AdBatch e o Facebook continuam recebendo o mesmo 9:16 de sempre.
# ⚠️ Um numero so', aqui. E' o unico lugar a mexer se ele pedir outro valor, e
# vale para o app e para a esteira, que chamam o mesmo `processar_video`.
ZOOM = 1.04


def _auto_editor():
    """Prefere o auto-editor do proprio ambiente (venv) e so depois o do PATH.
    Sem isso, rodando pelo venv o subprocess acharia a versao global (ou nada)."""
    base = os.path.dirname(os.path.abspath(sys.executable))
    for pasta in (base, os.path.join(base, "Scripts"), os.path.join(base, "bin")):
        for nome in ("auto-editor.exe", "auto-editor"):
            caminho = os.path.join(pasta, nome)
            if os.path.isfile(caminho):
                return caminho
    return shutil.which("auto-editor") or "auto-editor"


AUTO_EDITOR = _auto_editor()


# sem essa flag, cada ffmpeg/ffprobe/auto-editor abre um console preto quando o
# app roda via pythonw (sem console proprio)
SEM_JANELA = subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0


def _run(cmd, cwd=None):
    p = subprocess.run(cmd, capture_output=True, text=True, cwd=cwd,
                       encoding="utf-8", errors="replace",
                       creationflags=SEM_JANELA)
    if p.returncode != 0:
        raise RuntimeError(
            f"comando falhou ({cmd[0]}):\n{(p.stderr or p.stdout)[-1800:]}"
        )
    return p


def _natural(nome):
    # ordena take2 antes de take10
    return [int(x) if x.isdigit() else x.lower() for x in re.split(r"(\d+)", nome)]


def dims(path):
    p = _run([FFPROBE, "-v", "error", "-select_streams", "v:0",
              "-show_entries", "stream=width,height", "-of", "json", path])
    st = json.loads(p.stdout)["streams"][0]
    return int(st["width"]), int(st["height"])


def coletar_takes(pasta):
    arqs = [a for a in os.listdir(pasta)
            if a.lower().endswith(VIDEO_EXT) and os.path.isfile(os.path.join(pasta, a))]
    arqs.sort(key=_natural)
    return [os.path.join(pasta, a) for a in arqs]


def contar_zips(pasta):
    return [a for a in sorted(os.listdir(pasta), key=_natural)
            if a.lower().endswith(".zip") and os.path.isfile(os.path.join(pasta, a))]


def extrair_zips(entrada, log=print):
    """Extrai os .zip soltos na pasta de entrada (o pacote que o Flow baixa).
    Cada zip vira uma subpasta com o nome do arquivo = 1 video.
    So extrai video, achatando a estrutura interna (o basename tambem elimina
    qualquer path traversal do zip). Retorna as pastas criadas."""
    criadas = []
    for z in contar_zips(entrada):
        zpath = os.path.join(entrada, z)
        destino = os.path.join(entrada, os.path.splitext(z)[0])
        if os.path.isdir(destino) and coletar_takes(destino):
            log(f"  zip ja extraido, reaproveitando: {z}")
            criadas.append(destino)
            continue
        os.makedirs(destino, exist_ok=True)
        log(f"  extraindo {z}...")
        with zipfile.ZipFile(zpath) as zf:
            for membro in zf.infolist():
                if membro.is_dir():
                    continue
                nome = os.path.basename(membro.filename)
                if not nome or not nome.lower().endswith(VIDEO_EXT):
                    continue
                with zf.open(membro) as src, open(os.path.join(destino, nome), "wb") as dst:
                    shutil.copyfileobj(src, dst)
        n = len(coletar_takes(destino))
        if not n:
            log(f"  AVISO: {z} nao tinha video dentro, ignorando")
            shutil.rmtree(destino, ignore_errors=True)
            continue
        log(f"  {n} take(s) -> {os.path.basename(destino)}/")
        criadas.append(destino)
    return criadas


def duracao(path):
    p = _run([FFPROBE, "-v", "error", "-show_entries", "format=duration",
              "-of", "json", path])
    try:
        return float(json.loads(p.stdout)["format"]["duration"])
    except (KeyError, ValueError, TypeError):
        return 0.0


def concat(takes, out, cortes=None):
    """Junta na ordem, re-encodando uniforme (aguenta params diferentes do Veo).

    cortes: {caminho_do_take: [inicio, fim]} em segundos. fim None ou 0 = ate o
    final. O corte entra como filtro trim (preciso no frame) em vez de -ss, que
    com seek rapido erraria o ponto."""
    cortes = cortes or {}
    if len(takes) == 1 and not cortes.get(takes[0]):
        shutil.copy(takes[0], out)
        return out

    inputs = []
    for t in takes:
        inputs += ["-i", t]

    partes, rotulos = [], ""
    for i, t in enumerate(takes):
        corte = cortes.get(t)
        if corte:
            ini = max(0.0, float(corte[0] or 0))
            fim = float(corte[1]) if len(corte) > 1 and corte[1] else None
            tv = f"trim=start={ini:.3f}" + (f":end={fim:.3f}" if fim else "")
            ta = f"atrim=start={ini:.3f}" + (f":end={fim:.3f}" if fim else "")
            partes.append(f"[{i}:v:0]{tv},setpts=PTS-STARTPTS[v{i}]")
            partes.append(f"[{i}:a:0]{ta},asetpts=PTS-STARTPTS[a{i}]")
        else:
            partes.append(f"[{i}:v:0]null[v{i}]")
            partes.append(f"[{i}:a:0]anull[a{i}]")
        rotulos += f"[v{i}][a{i}]"

    fc = ";".join(partes) + f";{rotulos}concat=n={len(takes)}:v=1:a=1[v][a]"
    _run([FFMPEG, "-y", *inputs, "-filter_complex", fc, "-map", "[v]", "-map", "[a]",
          "-c:v", "libx264", "-preset", "veryfast", "-crf", "18",
          "-c:a", "aac", "-b:a", "192k", "-r", "30", out])
    return out


def desilenciar(inp, out, margem="0.2s"):
    """Corta silencio com folga ASSIMETRICA: a margem informada vale para a
    entrada da fala; na saida usamos margem + 0.35s. Fim de palavra (vogal
    fraca, consoante final) cai abaixo do threshold e o corte simetrico come
    a ultima silaba ("bio" vira "bi"). O threshold tambem desce de 4% para
    2.5% para o rabo da fala contar como som, nao como silencio."""
    try:
        m = float(str(margem).rstrip("s"))
    except ValueError:
        m = 0.2
    _run([AUTO_EDITOR, inp, "-o", out, "--no-open",
          "--edit", "audio:threshold=0.025",
          "--margin", f"{m}s,{m + 0.35:.2f}s"])
    return out


def aplicar_velocidade(inp, out, fator):
    """Muda a velocidade do video inteiro (video+audio). fator 1.03 = 3% mais
    rapido, 0.95 = 5% mais lento. atempo preserva o pitch da voz, entao a
    variacao fica inaudivel. Roda ANTES da transcricao para a legenda karaoke
    nascer ja sincronizada com o audio no ritmo final."""
    if fator is None or abs(fator - 1.0) < 0.001:
        shutil.copy(inp, out)
        return out
    _run([FFMPEG, "-y", "-i", inp,
          "-filter_complex",
          f"[0:v:0]setpts=PTS/{fator:.4f}[v];[0:a:0]atempo={fator:.4f}[a]",
          "-map", "[v]", "-map", "[a]",
          "-c:v", "libx264", "-preset", "veryfast", "-crf", "18",
          "-c:a", "aac", "-b:a", "192k", out])
    return out


def aplicar_zoom(inp, out, zoom):
    """Aproxima o quadro em `zoom` e recorta no centro de volta ao tamanho
    original. Vale para o video INTEIRO, do primeiro ao ultimo frame.
    1.04 = 4% mais perto; 1.0 nao faz nada.

    ⛔ RODA ANTES DE QUEIMAR A LEGENDA, e isso e' o ponto inteiro. Se o zoom
    viesse depois, ele ampliaria e cortaria o TEXTO junto — o pin do CTA fica a
    10% do topo, exatamente na faixa que um recorte de 4% come primeiro. Aqui a
    legenda e' desenhada sobre o quadro JA' aproximado, no tamanho certo e
    inteira dentro da tela.

    ⚠️ A saida tem a MESMA resolucao da entrada. Nao e' detalhe: o `gerar_ass`
    dimensiona fonte e margem a partir de `dims()`, e mudar a resolucao aqui
    mudaria o tamanho da legenda de tabela.
    ⚠️ Largura e altura intermediarias sao arredondadas para PAR — libx264 com
    yuv420p rejeita dimensao impar, e 1.04 sobre um lado impar cai nisso na
    primeira vez que alguem trocar o valor.
    ⚠️ O audio e' COPIADO (`-c:a copy`): zoom nao encosta no som, e reencodar
    aqui so' somaria perda a mais numa cadeia que ja' reencoda tres vezes.
    """
    if zoom is None or abs(zoom - 1.0) < 0.001:
        shutil.copy(inp, out)
        return out
    w, h = dims(inp)
    w2 = int(round(w * zoom / 2)) * 2
    h2 = int(round(h * zoom / 2)) * 2
    # ⚠️ o recorte usa o tamanho ORIGINAL, nao uma divisao por `zoom`: dividir
    # de volta reintroduz o erro do arredondamento e devolve 1079 no lugar de
    # 1080 de vez em quando.
    _run([FFMPEG, "-y", "-i", inp,
          "-vf", f"scale={w2}:{h2},crop={w}:{h}",
          "-c:v", "libx264", "-preset", "veryfast", "-crf", "18",
          "-c:a", "copy", out])
    return out


def queimar_legenda(inp, ass_path, out):
    # roda com cwd = pasta do .ass e passa o nome relativo, pra fugir do inferno
    # de escape de path do filtro ass no Windows (dois-pontos do drive).
    work = os.path.dirname(ass_path)
    ass_nome = os.path.basename(ass_path)
    _run([FFMPEG, "-y", "-i", os.path.abspath(inp),
          "-vf", f"ass={ass_nome}",
          "-c:v", "libx264", "-preset", "veryfast", "-crf", "18",
          "-c:a", "copy", os.path.abspath(out)], cwd=work)
    return out


def _inicio_take2(durs, dur_final, log=print):
    """Em que segundo do video PRONTO comeca o segundo take.

    ⛔ Nao da' para usar a duracao do take 1 direto. Entre juntar e legendar, o
    video passa por DOIS encolhimentos: o auto-editor tira os silencios e o
    fator de velocidade reescala tudo. Um take 1 de 8s pode virar 5,4s no
    arquivo final — e o pin entraria com quase 3s de atraso, ja' dentro da
    fala do CTA, que e' exatamente o que este modo existe para evitar.

    ⚠️ A conta e' PROPORCIONAL: os dois encolhimentos agem sobre o video
    inteiro, entao a fracao que o take 1 ocupa se preserva bem. Nao e' exata
    (silencio nao esta' distribuido por igual), e por isso o `captions.py`
    ainda ENCAIXA o alvo na primeira palavra dali em diante — a aproximacao
    escolhe a regiao, a palavra escolhe o frame.

    Com um take so', devolve None: nao existe segundo take para marcar.
    """
    if len(durs) < 2:
        return None
    duracoes = list(durs)
    if not all(duracoes) or not dur_final:
        return None
    alvo = (duracoes[0] / sum(duracoes)) * dur_final
    log("  CTA fixo: take 2 comeca em ~%.1fs de %.1fs (take 1 tinha %.1fs)"
        % (alvo, dur_final, duracoes[0]))
    return alvo


def _janela_do_take(durs, dur_final, n, log=print):
    """(inicio, fim) do take `n` no video PRONTO, em segundos.

    ⛔ MESMA CONTA PROPORCIONAL do `_fim_de_takes`, e pela mesma razao: o
    auto-editor tira silencio e o fator de velocidade reescala tudo depois
    da juncao. Somar as duracoes cruas devolve um par de segundos que
    nao existe mais no arquivo final.

    ⚠️ `n` fora da faixa devolve (None, None) = o VIDEO INTEIRO. E' o que
    faz "pedi o take 5 num video de 3" degradar para algo util em vez de
    sumir com a legenda.
    """
    if not n or not dur_final or not durs:
        return None, None
    ds = list(durs)
    if not all(ds) or n > len(ds):
        return None, None
    tot = float(sum(ds))
    ini = (sum(ds[:n - 1]) / tot) * dur_final
    fim = (sum(ds[:n]) / tot) * dur_final
    log("  legenda fixa: take %d vai de %.1fs a %.1fs" % (n, ini, fim))
    return ini, fim


def _fim_de_takes(durs, dur_final, n, log=print):
    """Em que segundo do video PRONTO termina o take `n`.

    ⛔ MESMA CONTA PROPORCIONAL do `_inicio_ultimo_take`, e pela mesma
    razao: o auto-editor tira silencio e o fator de velocidade reescala
    tudo depois da juncao, entao somar as duracoes cruas dos takes da' um
    segundo que nao existe mais no arquivo final. A FRACAO, sim, sobrevive.

    ⚠️ Devolve None quando `n` cobre todos os takes — ai' o efeito vale o
    video inteiro e quem manda e' a duracao final, sem conta nenhuma.
    """
    if not n or not dur_final or not durs:
        return None
    duracoes = list(durs)
    if not all(duracoes) or n >= len(duracoes):
        return None
    alvo = (sum(duracoes[:n]) / float(sum(duracoes))) * dur_final
    log("  circulado: acaba em ~%.1fs de %.1fs (%d de %d takes)"
        % (alvo, dur_final, n, len(duracoes)))
    return alvo


def _inicio_ultimo_take(durs, dur_final, log=print):
    """Em que segundo do video PRONTO comeca o ULTIMO take.

    ⭐ 2026-08-26 — o pin do CTA passou a mirar o ultimo take em vez do
    segundo. Ordem do operador: *"fixe a palavra Comment Yes no topo do
    video no ultimo take de todo video"*.

    ⛔ Mesma conta PROPORCIONAL do `_inicio_take2`, e pela mesma razao: o
    auto-editor tira silencio e o fator de velocidade reescala tudo, entao
    somar as duracoes cruas dos takes anteriores da' um numero que nao
    existe mais no arquivo final. A fracao, sim, se preserva.

    ⚠️ E e' so' um FALLBACK: quando o audio tem `comment <palavra>`, quem
    manda no tempo e' a fala, nao esta conta (ver `captions.gerar_ass`).

    Com um take so', devolve None.
    """
    if len(durs) < 2:
        return None
    duracoes = list(durs)
    if not all(duracoes) or not dur_final:
        return None
    alvo = (sum(duracoes[:-1]) / sum(duracoes)) * dur_final
    log("  CTA fixo: ultimo take comeca em ~%.1fs de %.1fs (%d takes)"
        % (alvo, dur_final, len(duracoes)))
    return alvo


# ===========================================================================
# ⭐⭐ A LEGENDA DAY — QUEIMADA AQUI, NAO PEDIDA AO GERADOR (2026-08-21)
# ===========================================================================
# Ordem do operador, depois de filmar oito geracoes: *"remova completamente
# esse dia 1 e dia 50 e poucos do prompt [...] e coloque pro editor conseguir
# fazer essa legenda queimada, deixar ela fixa dia 1 no take 1 e fixa o dia
# que tem que ser no take 2 [...] porque ele tem dificuldade em fixar essa
# legenda. E' mais facil fazer ela sair a partir do editor"*.
# ⛔ MEDIDO por ele: em 8 de 8 takes a legenda DESAPARECIA no meio, e dois
# lotes de imagem vieram com TARJA PRETA atras do texto. O ffmpeg desenha o
# mesmo pixel em todo frame — o gerador nao tem como fazer isso.
# ⭐ E' um botao GERAL, nao do AMISH: *"vai ser utilizado pra mais agentes
# tambem, entao precisa ter um botao ali de fixar ou nao"*.
FONTE_DIA = r"C:\Windows\Fonts\ariblk.ttf"      # Arial Black

# os cinco estilos que a pagina-fonte usa, lidos dos 18 reels
ESTILOS_DIA = {
    "vermelho": dict(cor="red", borda="white", larg=6, caixa=None),
    "amarelo":  dict(cor="yellow", borda="black", larg=5, caixa=None),
    "branco":   dict(cor="white", borda="black", larg=6, caixa=None),
    "rosa":     dict(cor="white", borda="black", larg=3, caixa="#E8117F"),
    "roxo":     dict(cor="white", borda="#7B2FBE", larg=6, caixa=None),
}


def _esc_ff(p):
    """Caminho de fonte para dentro de um filtro do ffmpeg no Windows."""
    return p.replace("\\", "/").replace(":", "\\:")


def queimar_dia(inp, texto, out, estilo="vermelho"):
    """Queima `texto` (ex.: "DAY 1") FIXO, do primeiro ao ultimo frame.

    ⛔ A altura e' 8% do topo e o tamanho 11% da altura — a mesma faixa que a
    fonte usa. Fica ACIMA do recorte de 4% do `aplicar_zoom`? Nao: o zoom
    roda DEPOIS e comeria a borda. Por isso o texto e' centralizado e nasce
    a 8%, nunca colado no topo.
    ⚠️ `borderw` desenha contorno, nao tarja. A tarja (`box`) so' entra no
    estilo `rosa`, que e' o unico da fonte que a tem — a tarja PRETA que
    apareceu nos lotes dele era invencao do gerador, e e' o que este
    caminho elimina.
    """
    e = ESTILOS_DIA.get(estilo) or ESTILOS_DIA["vermelho"]
    w, h = dims(inp)
    fs = max(28, int(h * 0.11))
    partes = ["fontfile='%s'" % _esc_ff(FONTE_DIA),
              "text='%s'" % texto.replace("'", ""),
              "fontcolor=%s" % e["cor"],
              "fontsize=%d" % fs,
              "bordercolor=%s" % e["borda"],
              "borderw=%d" % e["larg"],
              "x=(w-text_w)/2", "y=h*0.08"]
    if e["caixa"]:
        partes += ["box=1", "boxcolor=%s" % e["caixa"], "boxborderw=%d" % (fs // 6)]
    _run([FFMPEG, "-y", "-i", os.path.abspath(inp),
          "-vf", "drawtext=" + ":".join(partes),
          "-c:v", "libx264", "-preset", "veryfast", "-crf", "18",
          "-c:a", "copy", os.path.abspath(out)])
    return out


def volume_medio(path):
    """RMS medio em dB. Devolve -99 quando nao ha' audio nenhum."""
    p = _run([FFMPEG, "-i", path, "-af", "volumedetect", "-f", "null", "-"])
    for l in (p.stderr or "").splitlines():
        if "mean_volume:" in l:
            try:
                return float(l.split("mean_volume:")[1].split("dB")[0])
            except (IndexError, ValueError):
                pass
    return -99.0


# ⛔⛔ O LIMIAR DE MUDEZ — MEDIDO, NAO ESTIMADO (2026-08-21)
# ===========================================================================
# Nasceu -55 dB, que e' silencio DIGITAL. Ao rodar o primeiro lote real de 4
# takes do AMISH o valor foi desmentido: o Veo NAO entrega silencio digital
# nem quando o prompt manda: ele entrega ruido de sala. Medido nos 6 takes
# gerados por ele em 21/08 (mean_volume):
#
#   takes que o prompt pediu MUDOS  ->  -41.6 · -40.3 · -37.2 · -31.2 dB
#   takes COM FALA                  ->  -19.1 · -18.3 dB
#
# ⚠️ Com -55 dB nenhum dos quatro era reconhecido: os dois takes de card
# passavam pelo auto-editor, NAO recebiam a legenda DAY, NAO eram cortados a
# 3s e a musica era pulada com um log que dizia *"video de 1 take so'"*. As
# duas funcoes construidas ontem a pedido dele nao rodavam uma vez sequer, e
# nada no log denunciava. E' o mesmo modo de falha do §41: forma pronta,
# funcao morta.
# ⭐ -26 dB fica no meio dos 12 dB de folga entre os dois grupos (5 dB de
# margem para o take mudo mais barulhento, 7 para a fala mais baixa).
# ⛔ E o operador nao depende deste numero: o seletor `takes mudos` do rodape
# DECLARA quantos sao, e declaracao ganha de medicao sempre que existe.
LIMIAR_MUDO = -26.0


def e_mudo(path, limiar=LIMIAR_MUDO):
    """⛔⛔ O take e' MUDO? Pergunta que o editor precisa fazer desde 21/08.

    O AMISH 16S gera os takes 1-2 sem fala por ordem (a musica entra aqui).
    E o `auto-editor` corta o que estiver abaixo do threshold de audio — num
    take sem fala isso significa cortar O TAKE INTEIRO.
    ⚠️ Sem esta pergunta, o primeiro lote do AMISH sairia com dois takes
    faltando e nada no log dizendo por que.
    """
    return volume_medio(path) <= limiar


def mudez_dos_takes(takes, declarado=None, log=print):
    """Quais takes seguem pelo caminho MUDO (sem auto-editor, com legenda DAY,
    cobertos pela musica). Devolve uma lista de bool do tamanho de `takes`.

    `declarado`: quantos takes do INICIO sao mudos, dito pelo operador no
    rodape. None = detectar pelo volume. 0 = nenhum (desliga o caminho).

    ⭐ A DECLARACAO GANHA DA MEDICAO. O operador sabe que o AMISH tem dois
    cards mudos na frente; o medidor so' sabe que dois arquivos estao baixos.
    Quando os dois discordam, quem erra e' o medidor — e o log diz que
    discordaram, para o limiar poder ser corrigido com evidencia.
    """
    if declarado is not None:
        n = max(0, min(int(declarado), len(takes)))
        decl = [i < n for i in range(len(takes))]
        auto = [e_mudo(t) for t in takes]
        if auto != decl:
            log("  mudez: declarada %d (o medidor teria dito %d) — vale a "
                "declaracao" % (n, sum(auto)))
        return decl
    return [e_mudo(t) for t in takes]


def zerar_audio(inp, out):
    """Zera o audio do take, preservando a faixa (o `concat` mapeia `[i:a:0]`
    e um take sem stream de audio quebraria o filtro inteiro).

    ⛔ POR QUE ZERAR: o take mudo e' aquele cujo som e' SUBSTITUIDO pela
    musica — foi essa a ordem (*"takes 1 e 2 completamente mudos, sem nenhum
    tipo de som ou barulho, pois sera' colocada musica neles"*). O gerador
    nao cumpre: o take 2 do lote de 21/08 chegou com um pico de -3,7 dB
    (uma batida de colher) que, por baixo da musica, sai como estalo.
    ⚠️ O video e' COPIADO — zerar som nao encosta em quadro nenhum.
    """
    _run([FFMPEG, "-y", "-i", os.path.abspath(inp), "-af", "volume=0",
          "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", os.path.abspath(out)])
    return out


def _fim_takes_mudos(durs, mudos, dur_final):
    """Em que segundo do video PRONTO termina o ultimo take MUDO.

    ⭐ 2026-08-21: deixou de ser "todos menos o ultimo" (palpite) e passou a
    usar a DETECCAO de audio real (`e_mudo`) — a musica cobre exatamente os
    takes que nasceram mudos, seja qual for a quantidade deles.
    ⚠️ Continua proporcional porque a velocidade e o zoom reescalam o video
    inteiro DEPOIS; mas a base agora e' a duracao ja' tratada, nao a bruta.
    """
    if not any(mudos) or not dur_final or not sum(durs):
        return None
    # ultimo indice mudo (contiguo do inicio e' o caso normal, mas nao exigimos)
    ult = max(i for i, m in enumerate(mudos) if m)
    return (sum(durs[:ult + 1]) / sum(durs)) * dur_final


def mixar_musica(inp, musica, fim, out):
    """Mistura a musica por cima do audio de 0 ate `fim` segundos, com fade-out
    de 0,5s para nao estalar no corte.

    ⛔ Roda DEPOIS da legenda queimada e o video e' COPIADO (`-c:v copy`):
    musica nao encosta em quadro nenhum, e reencodar aqui so' somaria perda
    numa cadeia que ja' reencoda tres vezes.
    ⭐ Se a musica for mais curta que o trecho, ela simplesmente acaba (o
    atrim nao estica); se for mais longa, o atrim corta no `fim` exato — que
    e' o "cortada automaticamente caso os takes fiquem mais curtos" da ordem.
    ⚠️ `normalize=0` no amix: sem ele o filtro derruba o volume dos dois lados
    pela metade e a fala do take final sai baixa.
    """
    fade_ini = max(0.0, fim - 0.5)
    fc = (f"[1:a]atrim=0:{fim:.3f},asetpts=PTS-STARTPTS,"
          f"afade=t=out:st={fade_ini:.3f}:d=0.5[m];"
          f"[0:a][m]amix=inputs=2:duration=first:"
          f"dropout_transition=0:normalize=0[a]")
    _run([FFMPEG, "-y", "-i", os.path.abspath(inp), "-i", os.path.abspath(musica),
          "-filter_complex", fc, "-map", "0:v", "-map", "[a]",
          "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", os.path.abspath(out)])
    return out


def preparar_takes(takes, work, margem, dias=None, log=print):
    """⭐⭐ TRATA CADA TAKE ANTES DE JUNTAR — mudanca de 2026-08-21.

    ⛔ POR QUE O DESILENCIAR MUDOU DE LUGAR: ate' aqui ele rodava no video
    JUNTADO. Com o AMISH 16S os takes 1-2 passaram a nascer em SILENCIO
    TOTAL por ordem do operador (a musica entra depois) — e o `auto-editor`
    corta tudo que esta' abaixo do threshold de audio. Num take 100% mudo
    isso e' cortar O TAKE INTEIRO: o video sairia so' com o CTA, e nada no
    log diria por que.
    ⭐ Rodando por take, o mudo e' PRESERVADO e so' quem tem fala passa pelo
    corte. Efeito colateral bom: as duracoes finais ficam CONHECIDAS aqui, e
    o pin do CTA e o fim da musica deixam de ser estimativa proporcional.

    Devolve [(caminho_tratado, era_mudo)] na ordem.
    """
    dias = dias or {}
    ligado = bool(dias.get("ligado"))
    estilo = dias.get("estilo", "vermelho")
    corte = float(dias.get("corte") or 0)
    # ⭐⭐ CHAVINHA POR TAKE — 2026-08-26, ordem do operador: *"quando ela
    # estiver desligada o take em questao nao seja cortado, pois atualmente se eu
    # configuro a ferramenta para cortar em 4s, 3,5 ou 3s ela corta todos os
    # takes, e as vezes tem algum que eu nao quero cortar"*.
    # ⛔ `sem_corte` e' um conjunto de INDICES 0-based na lista JA COMPACTADA de
    # takes (slot vazio no painel nao gera indice). Vem no `_semcorte.json` dentro
    # do zip, e nao de uma config global: a fila pode ter varios jobs esperando, e
    # um flag global seria aplicado ao job errado.
    # ⭐ DESLIGADA = o take passa INTEIRO: sem corte duro E sem `desilenciar`.
    # E' a leitura literal de *"nao seja cortado"* — e a util: o corte duro so'
    # pega take MUDO, entao numa cena com fala a chavinha nao faria nada e ele
    # veria o take encurtar mesmo com ela desligada.
    # ⚠️ O que a chavinha NAO desliga: `zerar_audio` e a legenda DAY. Zerar o
    # audio nao encurta nada — e' o que a musica cobre.
    sem_corte = {int(i) for i in (dias.get("sem_corte") or ())}
    mudez = mudez_dos_takes(takes, dias.get("mudos"), log)
    saida, i_mudo = [], 0
    for i, tk in enumerate(takes):
        mudo = mudez[i]
        intocado = i in sem_corte
        cur = tk
        if mudo:
            i_mudo += 1
            # ⛔ O TAKE MUDO NAO PASSA PELO auto-editor — ver acima.
            if intocado:
                log("  take %d: chavinha DESLIGADA — mudo, preservado inteiro (%.1fs)"
                    % (i + 1, duracao(cur)))
            elif corte and duracao(cur) > corte + 0.05:
                # ⚠️ o Veo nao gera abaixo de 4s (medido pelo operador); o
                # take de 3s que o agente pede nasce do corte AQUI.
                novo_c = os.path.join(work, "t%02d_corte.mp4" % i)
                _run([FFMPEG, "-y", "-i", cur, "-t", "%.3f" % corte,
                      "-c:v", "libx264", "-preset", "veryfast", "-crf", "18",
                      "-c:a", "aac", "-b:a", "192k", novo_c])
                log("  take %d: mudo, cortado a %.1fs" % (i + 1, corte))
                cur = novo_c
            else:
                log("  take %d: mudo, preservado inteiro" % (i + 1))
            # o som do take mudo e' o que a musica substitui — ver `zerar_audio`
            novo_z = os.path.join(work, "t%02d_zero.mp4" % i)
            zerar_audio(cur, novo_z)
            cur = novo_z
            if ligado:
                texto = "DAY 1" if i_mudo == 1 else "DAY %s" % dias.get("dia2", 51)
                novo_d = os.path.join(work, "t%02d_dia.mp4" % i)
                queimar_dia(cur, texto, novo_d, estilo)
                log("  take %d: legenda %s queimada (estilo %s)"
                    % (i + 1, texto, estilo))
                cur = novo_d
        elif intocado:
            log("  take %d: chavinha DESLIGADA — fala preservada inteira, sem "
                "dessilenciar (%.1fs)" % (i + 1, duracao(cur)))
        else:
            novo_s = os.path.join(work, "t%02d_sil.mp4" % i)
            desilenciar(cur, novo_s, margem)
            log("  take %d: fala, silencio cortado (%.1fs -> %.1fs)"
                % (i + 1, duracao(cur), duracao(novo_s)))
            cur = novo_s
        saida.append((cur, mudo))
    return saida


def transcrever_takes(prontos, durs, model, lang, fator=None, log=print):
    """Transcreve TAKE A TAKE e reposiciona cada palavra no tempo do video
    final. Devolve a mesma lista de {text, start, end} que o `transcrever`.

    ⛔⛔ POR QUE NAO SE TRANSCREVE O VIDEO JUNTADO. Foi assim ate' 25/08, e o
    operador filmou o resultado: um video de SEIS takes saiu com legenda so' no
    take 1. Medido no lote dele, com o mesmo modelo e as mesmas opcoes:

        take a take .......... 52 palavras, cobrindo os 6 takes
        video juntado ........  8 palavras, parando em 2,16s

    ⛔ O audio do juntado esta' INTEIRO — 21,08s de stream, som entre -17 e
    -21 dB em todas as janelas. Nao e' o `concat`, nao e' o container (o WAV
    extraido da o mesmo resultado) e nao e' o `condition_on_previous_text`.
    E' o `vad_filter`: no arquivo juntado ele decide que a fala acabou depois
    da primeira frase e o decoder encerra. Com `vad_filter=False` a mesma
    chamada devolve 44 palavras em vez de 8 — mas ainda perde o ultimo take,
    porque o take MUDO no meio (3s de silencio real) faz o decoder parar de
    novo.
    ⭐ Take a take o problema nao existe: cada arquivo e' uma peca curta com
    fala continua, que e' o caso em que o whisper e' confiavel. E o take mudo
    nem chega a ser transcrito — e' pulado, nao "transcrito e descartado".

    ⚠️ O DESLOCAMENTO E' EXATO, nao estimado: `durs` sao as duracoes dos
    takes JA' tratados (pos auto-editor, pos corte do mudo), que e' a mesma
    lista que o `_inicio_take2` e o `_fim_takes_mudos` usam. O unico ajuste e'
    a VELOCIDADE, que entra depois do concat: `setpts=PTS/fator` divide o
    tempo, entao a palavra tambem.
    """
    from captions import transcrever as _t
    palavras, base = [], 0.0
    f = fator if (fator and abs(fator - 1.0) >= 0.001) else 1.0
    for i, ((caminho, mudo), d) in enumerate(zip(prontos, durs), 1):
        if mudo:
            log("  take %d: mudo, sem transcrever" % i)
        else:
            n0 = len(palavras)
            for w in _t(caminho, model, lang):
                palavras.append({"text": w["text"],
                                 "start": (base + w["start"]) / f,
                                 "end": (base + w["end"]) / f})
            log("  take %d: %d palavra(s)" % (i, len(palavras) - n0))
        base += d
    return palavras


def processar_video(takes, out_final, model="base", lang="en",
                    margem="0.2s", fator=None, keywords=None, musica=None,
                    dias=None, log=print):
    if not takes:
        raise RuntimeError("nenhum take encontrado")
    work = tempfile.mkdtemp(prefix="owedit_")
    try:
        juntado = os.path.join(work, "01_juntado.mp4")
        cortado = os.path.join(work, "02_cortado.mp4")
        ritmado = os.path.join(work, "03_ritmado.mp4")
        aproximado = os.path.join(work, "04_zoom.mp4")
        assf = os.path.join(work, "05_legenda.ass")

        log(f"  preparando {len(takes)} take(s)...")
        prontos = preparar_takes(takes, work, margem, dias, log)
        tratados = [p for p, _m in prontos]
        # as duracoes ja' tratadas: o pin e a musica deixam de ser estimativa
        durs = [duracao(p) for p in tratados]
        mudos = [m for _p, m in prontos]
        log("  juntando...")
        concat(tratados, juntado)
        shutil.copy(juntado, cortado)
        if fator is not None and abs(fator - 1.0) >= 0.001:
            log(f"  variando velocidade: {fator:.3f}x...")
            aplicar_velocidade(cortado, ritmado, fator)
            base = ritmado
        else:
            base = cortado
        # ⭐ o zoom entra AQUI: depois da velocidade (que mexe no tempo) e ANTES
        # da transcricao e da legenda (que mexem na imagem). Assim o pin do CTA
        # nasce sobre o quadro final e nao corre risco de recorte.
        if abs(ZOOM - 1.0) >= 0.001:
            log(f"  aproximando o quadro: {ZOOM:.0%}...")
            aplicar_zoom(base, aproximado, ZOOM)
            base = aproximado
        w, h = dims(base)
        log(f"  transcrevendo (whisper {model})... {w}x{h}")
        # ⛔⛔ TAKE A TAKE, nao no juntado — ver `transcrever_takes`. No
        # juntado o whisper parava na primeira frase e o video de 6 takes saia
        # com legenda so' no take 1 (medido: 8 palavras contra 52).
        palavras = transcrever_takes(prontos, durs, model, lang, fator, log)
        log(f"  {len(palavras)} palavras -> legenda")
        dur_final = duracao(base)
        # ⭐ CTA FIXO NO TOPO (religado em 2026-08-26): `cta` traz
        # {"ligado": bool, "palavra": str}. Desligado = so' o karaoke da fala,
        # que e' como o editor rodou de 13/08 ate' aqui.
        _cta = (dias or {}).get("cta") or {}
        _lig = bool(_cta.get("ligado"))
        _pal = (_cta.get("palavra") or "").strip()
        if _lig:
            log("  CTA fixo LIGADO: palavra %r" % (_pal.upper() or "auto"))
        _leg = (dias or {}).get("legenda") or {}
        _leg_lig = _leg.get("ligada", True)
        _leg_pos = float(_leg.get("pos", 0.60))
        if not _leg_lig:
            log("  legenda karaoke DESLIGADA — sai so' o pin do CTA")
        else:
            log("  legenda karaoke a %.0f%% da altura" % (_leg_pos * 100))
        _cta_pos = float(_cta.get("pos", 0.47))
        if _lig:
            log("  CTA fixo a %.0f%% da altura" % (_cta_pos * 100))
        # ⭐⭐ O CIRCULADO + "HERE" (2026-08-28). Vale para o video
        # INTEIRO, nao por take — ordem do operador: *"a chave deve
        # ativar em todos os takes"*.
        _aq = (dias or {}).get("aqui") or {}
        _aq_lig = bool(_aq.get("ligado"))
        _aq_x = float(_aq.get("x", 0.806))
        _aq_y = float(_aq.get("y", 0.682))
        _aq_n = _aq.get("takes")
        _aq_fim = None
        if _aq_lig:
            log("  circulado %r em %.0f%% x %.0f%% da tela"
                % (aqui_texto_para(lang), _aq_x * 100, _aq_y * 100))
            _aq_fim = _fim_de_takes(durs, dur_final, _aq_n, log)
            if _aq_n and _aq_fim is None:
                log("  circulado: %d take(s) cobre o video inteiro" % _aq_n)
        _fx = (dias or {}).get("fixo") or {}
        _fx_txt = (_fx.get("texto") or "").strip()
        _fx_ini = _fx_fim = None
        if _fx_txt:
            _fx_ini, _fx_fim = _janela_do_take(
                durs, dur_final, _fx.get("take"), log)
            log("  legenda fixa: %r em %.0f%% x %.0f%% (%s)"
                % (_fx_txt[:40], float(_fx.get("x", 0.5)) * 100,
                   float(_fx.get("y", 0.15)) * 100,
                   "take %s" % _fx.get("take") if _fx_ini is not None
                   else "video inteiro"))
        gerar_ass(palavras, w, h, assf, keywords=keywords,
                  duracao_video=dur_final,
                  pin_cta=_lig, cta_palavra=_pal,
                  pos_legenda=_leg_pos, so_pin=not _leg_lig,
                  pos_cta=_cta_pos,
                  aqui_ligado=_aq_lig, aqui_x=_aq_x, aqui_y=_aq_y,
                  aqui_fim=_aq_fim, aqui_texto=aqui_texto_para(lang),
                  fixo_texto=_fx_txt, fixo_x=float(_fx.get("x", 0.50)),
                  fixo_y=float(_fx.get("y", 0.15)),
                  fixo_ini=_fx_ini, fixo_fim=_fx_fim,
                  fixo_cor=_fx.get("cor") or "#000000",
                  fixo_fundo=_fx.get("fundo") or "#F0D000",
                  pin_em=_inicio_ultimo_take(durs, dur_final, log))
        log("  queimando legenda...")
        os.makedirs(os.path.dirname(os.path.abspath(out_final)), exist_ok=True)
        queimar_legenda(base, assf, out_final)
        # ⭐ MUSICA nos takes mudos (2026-08-21, pedido para o AMISH 16S):
        # entra por cima do audio do inicio ate o fim do penultimo take,
        # cortada no tamanho exato do trecho ja' editado.
        if musica and os.path.isfile(musica):
            fim = _fim_takes_mudos(durs, mudos, dur_final)
            if fim and fim > 0.6:
                log(f"  musica: {os.path.basename(musica)} ate {fim:.1f}s "
                    f"(cobre {sum(mudos)} take mudo(s))...")
                com_musica = os.path.join(work, "06_musica.mp4")
                mixar_musica(out_final, musica, fim, com_musica)
                shutil.move(com_musica, out_final)
            else:
                # ⚠️ a mensagem antiga dizia *"video de 1 take so'"* e mentia:
                # o lote real tinha 4 takes e nenhum reconhecido como mudo.
                # Log que da' o diagnostico errado custa mais que log nenhum.
                log("  musica: nenhum take mudo reconhecido — nada a cobrir, "
                    "pulando (seletor `takes mudos` no rodape resolve)")
        log(f"  OK -> {out_final}")
        return out_final
    finally:
        shutil.rmtree(work, ignore_errors=True)


def _tem_video_solto(pasta):
    return any(a.lower().endswith(VIDEO_EXT) for a in os.listdir(pasta)
              if os.path.isfile(os.path.join(pasta, a)))


def processar_pasta(entrada, saida, model="base", lang="en", margem="0.2s",
                    musica=None, dias=None, log=print):
    """Processa a pasta de entrada (subpastas=1 video cada, ou arquivos soltos=1 video).
    Retorna lista de arquivos gerados."""
    os.makedirs(saida, exist_ok=True)
    gerados = []

    # o Flow entrega o lote como .zip; extrai antes de decidir o modo de pasta
    extraidas = extrair_zips(entrada, log)

    subpastas = [d for d in sorted(os.listdir(entrada), key=_natural)
                 if os.path.isdir(os.path.join(entrada, d))]

    # se veio de zip, o modo e sempre "1 video por subpasta", mesmo que haja
    # video solto na entrada (evita misturar lote antigo com o recem-extraido)
    if not extraidas and _tem_video_solto(entrada):
        # arquivos soltos = 1 video
        nome = os.path.basename(os.path.normpath(entrada)) or "video"
        out = os.path.join(saida, f"{nome}_final.mp4")
        log(f"[1 video] {nome}")
        gerados.append(processar_video(coletar_takes(entrada), out, model, lang, margem, musica=musica, dias=dias, log=log))
    elif subpastas:
        for i, d in enumerate(subpastas, 1):
            takes = coletar_takes(os.path.join(entrada, d))
            if not takes:
                log(f"[{i}/{len(subpastas)}] {d}: sem takes, pulando")
                continue
            out = os.path.join(saida, f"{d}_final.mp4")
            log(f"[{i}/{len(subpastas)}] {d}")
            gerados.append(processar_video(takes, out, model, lang, margem, musica=musica, dias=dias, log=log))
    else:
        raise RuntimeError("pasta de entrada nao tem videos nem subpastas com videos")
    return gerados


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(description="Editor CapCut offline (junta+desilencia+legenda)")
    ap.add_argument("--input", "-i", required=True, help="pasta de entrada (takes do Veo)")
    ap.add_argument("--output", "-o", required=True, help="pasta de saida")
    ap.add_argument("--model", default="base",
                    help="porte do whisper: base, small ou medium (o sufixo "
                         ".en e' colocado sozinho quando --lang=en)")
    ap.add_argument("--lang", default="en", choices=["en", "de", "fr"])
    ap.add_argument("--margin", default="0.2s", help="margem de silencio a manter (ex: 0.2s)")
    a = ap.parse_args()
    feitos = processar_pasta(a.input, a.output, a.model, a.lang, a.margin)
    print(f"\nPronto. {len(feitos)} video(s) gerado(s):")
    for f in feitos:
        print("  -", f)
