"""Esteira de producao do Veo Editor: vigia a pasta Downloads (e 01_entrada),
captura o .zip que as ferramentas do Flow baixam, edita sozinha e organiza o
resultado em pastas de fila/prontos/arquivo/erros. Desenhada para dezenas de
videos por dia sem intervencao manual.

Pastas (criadas ao lado do app):
  01_entrada/          zips arrastados manualmente (qualquer *.zip)
  02_processando/      zip + takes extraidos do video em edicao
  03_prontos/AAAA-MM-DD/vNNN_final.mp4
  04_zips_arquivados/  zip original preservado (limpeza automatica > 14 dias)
  05_erros/            zip que falhou + .log do erro (com retry pelo painel)
  historico.csv        registro de tudo que passou pela esteira
"""

import os
import re
import csv
import json
import time
import queue
import random
import shutil
import zipfile
import traceback
import threading
from datetime import datetime, date, timedelta

from pipeline import processar_video, coletar_takes, duracao, VIDEO_EXT, _natural

BASE = os.environ.get("VEO_EDITOR_BASE") or os.path.dirname(os.path.abspath(__file__))
D_ENTRADA = os.path.join(BASE, "01_entrada")
D_PROC = os.path.join(BASE, "02_processando")
D_PRONTOS = os.path.join(BASE, "03_prontos")
D_ARQUIVO = os.path.join(BASE, "04_zips_arquivados")
D_ERROS = os.path.join(BASE, "05_erros")
HISTORICO = os.path.join(BASE, "historico.csv")
CONFIG = os.path.join(BASE, "config.json")

# so zips das nossas ferramentas sao capturados na pasta vigiada; na 01_entrada
# qualquer zip vale (caminho manual)
# ⚠️ INVERTIDO EM 2026-08-01: a v2.0 virou o destino padrao do Downloads
# (qualquer .zip que cair la' vai pra ela), e este aqui ficou com um territorio
# NOMEADO e pequeno — so' a AdBatch Vertical 5 e a Vertical 4. Antes era o
# contrario: aqui era "^adbatch.*" com a v2.0 recortada por um "(?!...)".
#
# A fronteira segue sendo a mesma coisa e pela mesma razao: as duas esteiras
# fazem poll na MESMA pasta Downloads, e quem pegasse o zip da outra entregaria
# o video com a velocidade errada, sem erro nenhum na tela.
#
# ⭐ A VERTICAL 3 ENTROU AQUI EM 2026-08-03 (ordem do operador). Ela e' o destino
# dos 12 agentes SHORT, e estava caindo na v2.0 — ou seja, TODO video SHORT
# saia acelerado 1.35x quando o operador queria 1x. Nao havia erro na tela: o
# lote era editado, so' que na esteira errada.
# ⚠️ O nome real que a ferramenta gera e' `adbatch_vertical_output.zip`, nao o
# `adbatch_vertical_3.zip` que o RUNBOOK documenta. Os dois casam aqui, porque
# quem manda e' o arquivo que chega, nao o que a doutrina previa.
#
# ⚠️⚠️ FRAGMENTO ESPELHADO — a copia literal deste _NOSSOS mora na v2.0
# (VEO-EDITOR-2.0/esteira.py), la' dentro de um "(?!...)". O que casa AQUI tem
# de estar excluido LA'. Mexeu num, mexe no outro no mesmo commit, senao as
# duas esteiras brigam pelo mesmo zip.
#
# Nomes vem da familia documentada em RUNBOOK-adbatch-vertical.md §A FAMILIA:
# V5 -> adbatch_vertical_5.zip · V4 -> adbatch_lote.zip
# V3 -> adbatch_vertical_3.zip / adbatch_vertical_output.zip
_V5_V4 = r"adbatch[_ -]?(?:vertical[_ -]?(?:[345]|output)|lote)"
PADRAO_DOWNLOADS = re.compile(_V5_V4 + r".*\.zip$", re.I)
DIAS_ARQUIVO = 14
VEL_MIN, VEL_MAX = 0.95, 1.03  # -5% a +3%, sorteado por video

# watch_dir vazio = usa o Downloads do Windows; keywords = palavras-gatilho do
# CTA destacadas na legenda (cor propria + fonte maior)
CFG = {"model": "base.en", "margem": "0.2s", "watch_dir": "",
       # ⭐ YES entrou em 2026-08-21 com o AMISH 16S, cuja keyword de
       # automacao e' `YES` por ordem dele (*"o cta desse agente deve ser
       # sempre a palavra yes"*). Sem ela o CTA saia sem destaque nenhum —
       # medido no v001 de hoje, o unico video do lote em que a palavra que
       # o espectador precisa digitar era a UNICA sem cor.
       # ⚠️ Preco declarado: um `yes` conversacional na fala de outro agente
       # tambem sai colorido. Tirar e' apagar uma palavra desta linha.
       "keywords": "HONEY,GELATIN,VICK,VICKS,RECIPE,YES",
       # ⭐ MUSICA nos takes mudos (2026-08-21, pedido para o AMISH 16S).
       # `musica` = nome do arquivo dentro de MUSICAS_DIR ("" = sem musica).
       # `musica_travada` = "1" mantem a escolha entre sessoes; vazio = a
       # escolha vale so' ate' fechar o app (os takes 1-2 do AMISH sao mudos,
       # entao ele trava uma vez e esquece).
       "musica": "", "musica_travada": "",
       # ⭐⭐ LEGENDA DE DIA nos takes MUDOS (2026-08-21). Ordem: *"precisa
       # ter um botao ali de fixar ou nao as legendas de dia no take 1 e
       # take 2"*, e ela e' GERAL — *"vai ser utilizado pra mais agentes
       # tambem"*. `dia_ligado` = "1" liga; `dia_num` = "" sorteia entre
       # DIA_MIN e DIA_MAX, ou um numero fixo; `dia_corte` = segundos a que
       # o take mudo e' cortado ("" = nao corta).
       "dia_ligado": "", "dia_num": "", "dia_estilo": "vermelho",
       "dia_corte": "3",
       # ⭐⭐ QUANTOS TAKES DO INICIO SAO MUDOS — 2026-08-21, junto com o
       # quarto slot. "auto" mede pelo volume (LIMIAR_MUDO); um numero
       # DECLARA, e declaracao ganha de medicao. O AMISH 16S e' "2".
       # ⛔ Existe porque o medidor ja' errou: com o limiar antigo os quatro
       # takes reais do lote passaram por falados e as duas funcoes novas
       # (legenda DAY e musica) nao rodaram uma vez.
       "mudos": "auto"}

# a faixa que o AMISH 16S sorteia — o operador pediu poder travar dentro dela
DIA_MIN, DIA_MAX = 45, 57

# a pasta que o operador pediu: dentro da "Agentes Python" da area de trabalho
MUSICAS_DIR = os.path.join(os.path.expanduser("~"), "Desktop",
                           "Agentes Python", "Musicas")
AUDIO_EXT = (".mp3", ".wav", ".m4a", ".aac", ".ogg", ".flac")


def listar_musicas():
    """Nomes dos audios em MUSICAS_DIR, ordenados. Pasta ausente = lista vazia."""
    try:
        return sorted(a for a in os.listdir(MUSICAS_DIR)
                      if a.lower().endswith(AUDIO_EXT))
    except OSError:
        return []


def dias_atual():
    """O contrato que o `pipeline.processar_video` espera. SEMPRE um dict.

    ⛔ O sorteio do dia acontece AQUI, uma vez por video — nao no pipeline.
    Assim o numero fica no log e no historico, e dois videos do mesmo lote
    nao saem com o mesmo dia so' porque o processo nao reiniciou.

    ⚠️ Deixou de devolver None com a legenda desligada (2026-08-21): o
    `mudos` e o `corte` valem mesmo sem legenda nenhuma — quem decide se o
    take passa pelo auto-editor e ate' onde a musica vai e' a MUDEZ, nao a
    legenda. Amarrar as duas coisas fazia desligar a legenda apagar a
    musica junto, em silencio.
    """
    fixo = (CFG.get("dia_num") or "").strip()
    if fixo.isdigit():
        n = max(DIA_MIN, min(DIA_MAX, int(fixo)))
    else:
        n = random.randint(DIA_MIN, DIA_MAX)
    corte = (CFG.get("dia_corte") or "").strip()
    md = (CFG.get("mudos") or "auto").strip()
    return {"ligado": CFG.get("dia_ligado") == "1", "dia2": n,
            "estilo": CFG.get("dia_estilo") or "vermelho",
            "corte": float(corte) if corte else 0,
            "mudos": int(md) if md.isdigit() else None}


def musica_atual():
    """Caminho completo da musica escolhida, ou None se nao houver/sumiu."""
    nome = (CFG.get("musica") or "").strip()
    if not nome:
        return None
    p = os.path.join(MUSICAS_DIR, nome)
    return p if os.path.isfile(p) else None

_lock = threading.RLock()
_fila = queue.Queue()
_iniciada = False

ESTADO = {
    "chegando": [],    # [nome do zip visto, esperando o tamanho estabilizar]
    "pendentes": [],   # [nome do zip aguardando]
    "atual": None,     # {"zip", "etapa", "log": [...]}
    "prontos": [],     # [{"arquivo","data","zip","duracao","fator","hora"}]
    "erros": [],       # [{"zip","erro","hora"}]
    "watch": [],       # pastas vigiadas (informativo pro painel)
}


def pasta_downloads():
    """Downloads verdadeiro do Windows (nao um palpite em ~/Downloads)."""
    if os.name == "nt":
        try:
            import winreg
            with winreg.OpenKey(
                winreg.HKEY_CURRENT_USER,
                r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders",
            ) as k:
                val, _ = winreg.QueryValueEx(k, "{374DE290-123F-4565-9164-39C4925E467B}")
            p = os.path.expandvars(val)
            if os.path.isdir(p):
                return p
        except OSError:
            pass
    return os.path.join(os.path.expanduser("~"), "Downloads")


def _carregar_cfg():
    # ⛔ `utf-8-sig`, nao `utf-8` (2026-08-21): qualquer editor do Windows —
    # o PowerShell inclusive — grava JSON com BOM, e com `utf-8` o
    # `json.load` levanta ValueError na primeira coluna. O `except` abaixo
    # engole, e o app volta com TODOS os ajustes no padrao sem uma linha de
    # log. Foi assim que a escolha de DAY 47/amarelo sumiu num teste de hoje.
    try:
        with open(CONFIG, encoding="utf-8-sig") as f:
            dados = json.load(f)
        for k in CFG:
            if isinstance(dados.get(k), str):
                CFG[k] = dados[k]
    except (OSError, ValueError):
        pass
    # ⛔ musica NAO travada morre com a sessao: se o config diz que nao esta'
    # travada, a escolha gravada e' resto da sessao anterior e sai daqui.
    if CFG.get("musica_travada") != "1":
        CFG["musica"] = ""


def salvar_cfg():
    try:
        with open(CONFIG, "w", encoding="utf-8") as f:
            json.dump(CFG, f, ensure_ascii=False, indent=2)
    except OSError:
        pass


def pasta_vigiada():
    """Pasta onde os zips sao capturados. Prioridade:
    env (testes) > escolhida pelo usuario (config.json) > Downloads real."""
    env = os.environ.get("VEO_EDITOR_DOWNLOADS")
    if env:
        return env
    if CFG["watch_dir"] and os.path.isdir(CFG["watch_dir"]):
        return CFG["watch_dir"]
    return pasta_downloads()


def _modo_downloads(vigiada):
    """True quando a pasta vigiada e o Downloads real: ai vale o filtro
    adbatch*.zip (senao a esteira engoliria qualquer download). Numa pasta
    dedicada escolhida pelo usuario, QUALQUER .zip e capturado."""
    try:
        return os.path.normcase(os.path.abspath(vigiada)) == \
            os.path.normcase(os.path.abspath(pasta_downloads()))
    except OSError:
        return True


def _captura(nome, modo_downloads):
    if not nome.lower().endswith(".zip"):
        return False
    return PADRAO_DOWNLOADS.match(nome) is not None if modo_downloads else True


def definir_pasta_vigiada(p):
    """Troca a pasta vigiada em tempo real (o watcher le a cada ciclo)."""
    if not p or not os.path.isdir(p):
        return False
    CFG["watch_dir"] = os.path.normpath(p)
    salvar_cfg()
    return True


def _preparar_pastas():
    for d in (D_ENTRADA, D_PROC, D_PRONTOS, D_ARQUIVO, D_ERROS):
        os.makedirs(d, exist_ok=True)


def _nome_unico(pasta, nome):
    """a.zip -> a.zip, a (2).zip, a (3).zip... ate nao colidir."""
    destino = os.path.join(pasta, nome)
    if not os.path.exists(destino):
        return destino
    raiz, ext = os.path.splitext(nome)
    n = 2
    while True:
        destino = os.path.join(pasta, f"{raiz} ({n}){ext}")
        if not os.path.exists(destino):
            return destino
        n += 1


def _registrar(arquivo, data_str, zip_origem, dur, fator, status):
    novo = not os.path.exists(HISTORICO)
    with open(HISTORICO, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if novo:
            w.writerow(["datahora", "arquivo", "data", "zip_origem",
                        "duracao_s", "fator", "status"])
        w.writerow([datetime.now().isoformat(timespec="seconds"), arquivo,
                    data_str, zip_origem, f"{dur:.1f}", f"{fator:.4f}", status])


def _carregar_prontos_de_hoje():
    """Repovoa o painel apos reiniciar o app no meio do dia."""
    if not os.path.exists(HISTORICO):
        return
    hoje = date.today().isoformat()
    try:
        with open(HISTORICO, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                if row.get("data") == hoje and row.get("status") == "ok":
                    ESTADO["prontos"].append({
                        "arquivo": row["arquivo"], "data": row["data"],
                        "zip": row["zip_origem"],
                        "duracao": float(row["duracao_s"] or 0),
                        "fator": float(row["fator"] or 1),
                        "hora": row["datahora"][11:16],
                    })
    except (OSError, ValueError, KeyError):
        pass


def _limpar_arquivo_antigo():
    limite = time.time() - DIAS_ARQUIVO * 86400
    try:
        for a in os.listdir(D_ARQUIVO):
            p = os.path.join(D_ARQUIVO, a)
            if os.path.isfile(p) and os.path.getmtime(p) < limite:
                os.remove(p)
    except OSError:
        pass


def _proximo_nome(pasta_dia):
    """v001_final.mp4, v002_final.mp4... sequencial dentro da pasta do dia."""
    os.makedirs(pasta_dia, exist_ok=True)
    maior = 0
    for a in os.listdir(pasta_dia):
        m = re.match(r"^v(\d+)_final\.mp4$", a, re.I)
        if m:
            maior = max(maior, int(m.group(1)))
    return f"v{maior + 1:03d}_final.mp4"


def _extrair_zip(zpath, destino):
    """Extrai so os videos, achatando a estrutura interna do zip."""
    os.makedirs(destino, exist_ok=True)
    with zipfile.ZipFile(zpath) as zf:
        for membro in zf.infolist():
            if membro.is_dir():
                continue
            nome = os.path.basename(membro.filename)
            if not nome or not nome.lower().endswith(VIDEO_EXT):
                continue
            with zf.open(membro) as src, open(os.path.join(destino, nome), "wb") as dst:
                shutil.copyfileobj(src, dst)


def _enfileirar(origem_path):
    """Move o zip para 02_processando e poe na fila."""
    destino = _nome_unico(D_PROC, os.path.basename(origem_path))
    shutil.move(origem_path, destino)
    nome = os.path.basename(destino)
    with _lock:
        ESTADO["pendentes"].append(nome)
    _fila.put(nome)
    return nome


def _reenfileirar_orfaos():
    """Zips parados em 02_processando de uma execucao que morreu no meio.

    A fila e' em memoria: se o app fecha (ou e' morto) durante o processamento,
    o zip ja' saiu do Downloads e ninguem mais olha para ele — some da esteira
    sem virar video nem erro. Um ficou 5 horas estranhado assim em producao
    (adbatch_vertical_5.zip, 2026-07-30).
    """
    try:
        for a in sorted(os.listdir(D_PROC)):
            if not a.lower().endswith(".zip"):
                continue
            with _lock:
                if a in ESTADO["pendentes"]:
                    continue
                ESTADO["pendentes"].append(a)
            _fila.put(a)
    except OSError:
        pass


# ---------------- watcher ----------------

def _watcher():
    """Poll a cada 2.5s. Um zip so e capturado quando o tamanho ficou estavel
    entre duas leituras (download concluido) e nao ha .crdownload do navegador."""
    tamanhos = {}
    while True:
        try:
            vendo = []          # o que ainda esta' estabilizando NESTE ciclo
            candidatos = []
            vigiada = pasta_vigiada()  # relido a cada ciclo: troca vale na hora
            modo_dl = _modo_downloads(vigiada)
            for a in os.listdir(vigiada):
                if _captura(a, modo_dl):
                    candidatos.append(os.path.join(vigiada, a))
            for a in os.listdir(D_ENTRADA):
                if a.lower().endswith(".zip"):
                    candidatos.append(os.path.join(D_ENTRADA, a))

            for p in candidatos:
                if not os.path.isfile(p):
                    continue
                if os.path.exists(p + ".crdownload") or os.path.exists(p + ".part"):
                    continue
                try:
                    tam = os.path.getsize(p)
                except OSError:
                    continue
                if tamanhos.get(p) == tam and tam > 0:
                    tamanhos.pop(p, None)
                    try:
                        _enfileirar(p)
                    except OSError:
                        pass  # arquivo em uso; tenta no proximo ciclo
                else:
                    tamanhos[p] = tam
                    vendo.append(os.path.basename(p))

            # ⭐ publica o que esta' sendo observado: e' o que acende o mascote
            # antes mesmo do arquivo entrar na fila (ordem do operador).
            with _lock:
                ESTADO["chegando"] = vendo
            # esquece caminhos que sumiram
            for p in list(tamanhos):
                if not os.path.exists(p):
                    tamanhos.pop(p, None)
        except OSError:
            pass
        time.sleep(2.5)


# ---------------- worker ----------------

def _log_atual(msg):
    with _lock:
        if ESTADO["atual"] is not None:
            ESTADO["atual"]["log"].append(str(msg))
            # a "etapa" e a ultima linha de log resumida
            ESTADO["atual"]["etapa"] = str(msg).strip()


def _processar_zip(nome):
    zpath = os.path.join(D_PROC, nome)
    extra = os.path.join(D_PROC, os.path.splitext(nome)[0] + "_takes")
    with _lock:
        if nome in ESTADO["pendentes"]:
            ESTADO["pendentes"].remove(nome)
        ESTADO["atual"] = {"zip": nome, "etapa": "extraindo...", "log": []}
    try:
        _log_atual(f"extraindo {nome}...")
        _extrair_zip(zpath, extra)
        takes = coletar_takes(extra)
        if not takes:
            raise RuntimeError("o zip nao tinha nenhum video dentro")
        _log_atual(f"{len(takes)} take(s) em ordem: "
                   + ", ".join(os.path.basename(t) for t in takes))

        fator = round(random.uniform(VEL_MIN, VEL_MAX), 4)
        data_str = date.today().isoformat()
        pasta_dia = os.path.join(D_PRONTOS, data_str)
        arquivo = _proximo_nome(pasta_dia)
        out = os.path.join(pasta_dia, arquivo)

        kws = [k for k in CFG["keywords"].split(",") if k.strip()]
        mus = musica_atual()
        if CFG.get("musica") and not mus:
            _log_atual("aviso: musica %r sumiu da pasta — seguindo sem"
                       % CFG["musica"])
        dias = dias_atual()
        if dias.get("ligado"):
            _log_atual("legenda de dia LIGADA: DAY 1 / DAY %d (estilo %s)"
                       % (dias["dia2"], dias["estilo"]))
        if dias.get("mudos") is not None:
            _log_atual("takes mudos declarados: %d" % dias["mudos"])
        processar_video(takes, out, model=CFG["model"], margem=CFG["margem"],
                        fator=fator, keywords=kws, musica=mus, dias=dias,
                        log=_log_atual)

        dur = duracao(out)
        shutil.move(zpath, _nome_unico(D_ARQUIVO, nome))
        _registrar(arquivo, data_str, nome, dur, fator, "ok")
        with _lock:
            ESTADO["prontos"].append({
                "arquivo": arquivo, "data": data_str, "zip": nome,
                "duracao": dur, "fator": fator,
                "hora": datetime.now().strftime("%H:%M"),
            })
    except Exception as e:  # noqa: BLE001
        erro = str(e)
        try:
            destino_err = _nome_unico(D_ERROS, nome)
            if os.path.exists(zpath):
                shutil.move(zpath, destino_err)
            with open(destino_err + ".log", "w", encoding="utf-8") as f:
                f.write(traceback.format_exc())
            nome = os.path.basename(destino_err)
        except OSError:
            pass
        _registrar("", date.today().isoformat(), nome, 0.0, 1.0, "erro")
        with _lock:
            ESTADO["erros"].append({
                "zip": nome, "erro": erro[:300],
                "hora": datetime.now().strftime("%H:%M"),
            })
    finally:
        shutil.rmtree(extra, ignore_errors=True)
        with _lock:
            ESTADO["atual"] = None


def _worker():
    while True:
        nome = _fila.get()
        try:
            _processar_zip(nome)
        finally:
            _fila.task_done()


# ---------------- API usada pelo app ----------------

def enfileirar_manual(caminhos):
    """⭐ MODO MANUAL (2026-08-03): o operador escolhe os takes na mao.

    Recebe os caminhos JA' NA ORDEM (take 1, 2, 3, 4...) e devolve o nome do
    job. Quantos slots o painel oferece e' decisao dele (`app.N_MANUAL`);
    aqui a quantidade e' livre.

    ⚠️ NAO existe um segundo caminho de edicao aqui. Esta funcao so' MONTA UM
    ZIP em 01_entrada e deixa o watcher/worker que ja' rodam fazerem o resto.
    E' de proposito: legenda, dessilenciamento, velocidade, pin do CTA e
    registro de "prontos hoje" saem identicos ao fluxo automatico porque sao
    literalmente o mesmo codigo. Um segundo pipeline seria a mesma armadilha
    do fragmento espelhado — nasce igual e envelhece diferente.

    ⚠️ Os arquivos entram renomeados `01_`, `02_`, `03_` porque `coletar_takes`
    ordena por `_natural`: sem o prefixo, `cena10.mp4` viria antes de
    `cena2.mp4` e o video sairia fora de ordem sem erro nenhum.
    """
    caminhos = [c for c in caminhos if c]
    if not caminhos:
        raise ValueError("nenhum take selecionado")
    for c in caminhos:
        if not os.path.isfile(c):
            raise ValueError("arquivo nao encontrado: %s" % os.path.basename(c))
        if not c.lower().endswith(VIDEO_EXT):
            raise ValueError("nao e' video: %s" % os.path.basename(c))

    _preparar_pastas()
    nome = "manual_%s.zip" % datetime.now().strftime("%Y%m%d_%H%M%S")
    destino = _nome_unico(D_ENTRADA, nome)
    # monta num temporario e so' depois move para 01_entrada: o watcher faz
    # poll por tamanho estavel, e um zip crescendo na pasta vigiada ja' foi
    # capturado pela metade em producao.
    tmp = destino + ".parcial"
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_STORED) as z:
        for i, c in enumerate(caminhos, 1):
            z.write(c, "%02d_%s" % (i, os.path.basename(c)))
    os.replace(tmp, destino)
    return os.path.basename(destino)


def iniciar():
    """Sobe watcher + worker (idempotente). Chamar no boot do app."""
    global _iniciada
    with _lock:
        if _iniciada:
            return
        _iniciada = True
    _preparar_pastas()
    _reenfileirar_orfaos()
    _carregar_cfg()
    _carregar_prontos_de_hoje()
    _limpar_arquivo_antigo()
    threading.Thread(target=_watcher, daemon=True).start()
    threading.Thread(target=_worker, daemon=True).start()


def status():
    with _lock:
        hoje = date.today().isoformat()
        atual = None
        if ESTADO["atual"] is not None:
            atual = {"zip": ESTADO["atual"]["zip"],
                     "etapa": ESTADO["atual"]["etapa"],
                     "log": list(ESTADO["atual"]["log"])}
        vigiada = pasta_vigiada()
        modo_dl = _modo_downloads(vigiada)
        padrao = "adbatch*.zip" if modo_dl else "*.zip"
        ignorados = 0
        if modo_dl:
            # zips no Downloads fora do padrao: avisa em vez de ignorar mudo
            try:
                ignorados = sum(1 for a in os.listdir(vigiada)
                                if a.lower().endswith(".zip")
                                and not PADRAO_DOWNLOADS.match(a))
            except OSError:
                pass
        return {
            "watch": [f"{vigiada} ({padrao})", D_ENTRADA + r" (*.zip)"],
            "ignorados": ignorados,
            "chegando": list(ESTADO["chegando"]),
            "pendentes": list(ESTADO["pendentes"]),
            "atual": atual,
            "prontos": [p for p in ESTADO["prontos"] if p["data"] == hoje],
            "erros": list(ESTADO["erros"]),
            "pasta_prontos": D_PRONTOS,
            "cfg": dict(CFG),
        }


def tentar_de_novo(nome):
    """Retry de um zip que caiu em 05_erros."""
    p = os.path.join(D_ERROS, nome)
    if not os.path.isfile(p):
        return False
    for sufixo in (".log",):
        try:
            os.remove(p + sufixo)
        except OSError:
            pass
    with _lock:
        ESTADO["erros"] = [e for e in ESTADO["erros"] if e["zip"] != nome]
    _enfileirar(p)
    return True


def caminho_video(data_str, arquivo):
    """Resolve com validacao o caminho de um video pronto (pro player)."""
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", data_str):
        return None
    if not re.match(r"^v\d+_final\.mp4$", arquivo, re.I):
        return None
    p = os.path.join(D_PRONTOS, data_str, arquivo)
    return p if os.path.isfile(p) else None
