# -*- coding: utf-8 -*-
"""ESTEIRA · ETAPA 1 — a leitura LOCAL de um video-fonte. ZERO TOKEN.

    python esteira/ler.py "C:\\caminho\\video.mp4"

⛔⛔ POR QUE ESTA ESTEIRA EXISTE, e por que ela NAO substitui os agentes.
Os motores (`<angulo>_short.py`) existem para gerar LOTES variados de um angulo
ja' validado: pool, ledger, lente, autoteste. Isso e' caro de construir — os 7
videos de 16/08 custaram ~1,9 milhao de tokens, quase tudo em MOTOR, nao em
leitura. Esta esteira faz outra coisa: **um video parecido com um video**. Ela
nao escala lote; escala repertorio. As duas convivem.

⭐⭐ A ARQUITETURA E' DESENHADA EM VOLTA DO CUSTO, e o desenho e' este:
    ETAPA 1 (este arquivo) .... 100% local, zero token
    ETAPA 2 (o chat) .......... UMA folha de contato + a transcricao ja' alinhada
    ETAPA 3 (`gerar.py`) ...... 100% local, zero token

O que so' a VISAO resolve fica na etapa 2, e ela recebe **uma imagem**, nao cem
quadros: ~2k tokens de folha + ~0,5k de transcricao + ~1,5k de JSON de volta.
⛔ E o prompt final NAO e' escrito pelo modelo. Se fosse, cada video custaria
4-5x mais e traria de volta os defeitos que este repo ja' pagou: aparelho na
mao do personagem, `not a celebrity`, bloco estourando 4.000 caracteres, fala
cortada. **O modelo descreve o que ve'; o gerador de prompt e' CODIGO** — e
contrato em codigo nao regride.

O QUE ESTA ETAPA FAZ, tudo deterministico:
 1. duracao e formato (ffprobe)
 2. ⭐ DETECCAO DE CORTE — e' ela que descobre QUANTOS takes o video tem e ONDE
    eles cortam, sem ninguem olhar. E' o dado mais caro de obter a olho e o
    mais barato de obter por codigo.
 3. quadros nos cortes e no meio de cada take -> FOLHA DE CONTATO com o tempo
    queimado em cada quadro
 4. transcricao com `faster-whisper` (local, offline)
 5. ⭐ ALINHAMENTO fala <-> take, por intersecao de tempo. E' o que transforma
    "a transcricao do video" em "o que se fala em CADA cena" — e e' de graca.
 6. escreve o `PEDIDO.md`, ja' pronto para colar no chat
"""
import argparse
import io
import json
import os
import re
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
SAIDA = os.path.join(AQUI, "saida")
FONTE_TTF = "C\\:/Windows/Fonts/arialbd.ttf"


def _slug(caminho):
    n = os.path.splitext(os.path.basename(caminho))[0].lower()
    n = re.sub(r"[^a-z0-9]+", "-", n).strip("-")
    return n[:60] or "video"


def duracao(p):
    o = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                        "format=duration", "-of", "default=nw=1:nk=1", p],
                       capture_output=True, text=True)
    try:
        return float(o.stdout.strip())
    except ValueError:
        raise SystemExit("ffprobe nao leu a duracao de %s" % p)


LIMIAR = 0.12


def cortes(p, limiar=LIMIAR):
    """Os segundos em que a cena MUDA.

    ⭐ E' o achado central da etapa 1. O `select='gt(scene,N)'` do ffmpeg
    devolve a diferenca entre quadros vizinhos; acima do limiar e' corte.

    ⛔⛔ O 0,12 E' MEDIDO, NAO ESCOLHIDO. Gabarito: os 14 cortes que a leitura
    otica quadro a quadro de 2026-08-16 achou nos 7 videos-fonte, com
    timestamp. Rodando o detector contra eles:

        limiar   cortes reais achados   falsos positivos
        0.40           5 de 14                 0
        0.30           8 de 14                 0     <- o meu chute inicial
        0.20          12 de 14                 0
        0.12          14 de 14                 2     <- padrao
        0.08          14 de 14                 3
        0.05          14 de 14                30

    ⚠️ Com 0,30 o detector perdia SEIS cortes reais — e perder corte e' pior
    que inventar um: o take vira dois planos colados num prompt so', e a
    imagem gerada nao consegue ser os dois. Falso positivo o operador ve' na
    folha e ignora; corte perdido some.
    ⛔ Abaixo de 0,08 desmorona: em 0,05 sao 30 falsos, quase todos movimento
    de camera lida como cena nova.
    """
    o = subprocess.run(
        ["ffmpeg", "-hide_banner", "-i", p, "-filter_complex",
         "select='gt(scene,%s)',metadata=print:file=-" % limiar,
         "-an", "-f", "null", "-"], capture_output=True, text=True)
    ts = [float(m) for m in re.findall(r"pts_time:([0-9.]+)", o.stdout)]
    return sorted(set(round(t, 2) for t in ts if t > 0.4))


def takes(dur, cs, minimo=1.2):
    """Os cortes viram INTERVALOS. Corte colado no vizinho e' descartado.

    ⛔ Um corte a menos de 1,2s do anterior quase nunca e' cena nova: e' flash,
    zoom brusco ou legenda entrando. Deixar entrar inflaria a contagem de takes
    e o `gerar.py` pediria uma imagem para cada piscada.
    """
    bordas = [0.0]
    for c in cs:
        if c - bordas[-1] >= minimo:
            bordas.append(c)
    bordas.append(dur)
    return [(bordas[i], bordas[i + 1]) for i in range(len(bordas) - 1)
            if bordas[i + 1] - bordas[i] >= minimo]


def folha(p, tks, dest, por_take=4):
    """A folha de contato: quadros AMARRADOS aos takes, nao espalhados no tempo.

    ⛔ Uma folha de N quadros igualmente espacados desperdica quadro em cena
    longa e perde cena curta. Aqui cada take ganha o mesmo numero de quadros,
    entao a leitura da etapa 2 ve' TODAS as cenas — que e' o que ela precisa
    descrever.
    """
    tempos = []
    for (a, b) in tks:
        dur = b - a
        for k in range(por_take):
            tempos.append(a + dur * (k + 0.5) / por_take)
    tmp = os.path.join(dest, "_q")
    os.makedirs(tmp, exist_ok=True)
    for i, t in enumerate(tempos, 1):
        subprocess.run(
            ["ffmpeg", "-y", "-v", "error", "-ss", "%.3f" % t, "-i", p,
             "-frames:v", "1", "-vf",
             "scale=340:-1,drawtext=fontfile='%s':text='%.1fs':x=6:y=6:"
             "fontsize=22:fontcolor=yellow:box=1:boxcolor=black@0.65:"
             "boxborderw=4" % (FONTE_TTF, t),
             "-q:v", "3", os.path.join(tmp, "q%03d.jpg" % i)],
            capture_output=True)
    cols = 4
    alvo = os.path.join(dest, "folha.jpg")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i",
                    os.path.join(tmp, "q%03d.jpg"), "-filter_complex",
                    "tile=%dx%d:margin=4:padding=4"
                    % (cols, (len(tempos) + cols - 1) // cols),
                    "-frames:v", "1", "-q:v", "3", alvo], capture_output=True)
    for f in os.listdir(tmp):
        os.remove(os.path.join(tmp, f))
    os.rmdir(tmp)
    return alvo, tempos


def transcrever(p):
    from faster_whisper import WhisperModel
    m = WhisperModel("small.en", device="cpu", compute_type="int8")
    segs, _ = m.transcribe(p, language="en", beam_size=5, vad_filter=True)
    return [{"t0": round(s.start, 2), "t1": round(s.end, 2),
             "txt": s.text.strip()} for s in segs]


def alinhar(tks, segs):
    """Cada fala entra no take com que ela mais se sobrepoe.

    ⭐ E' a linha mais barata desta esteira e uma das mais uteis: transforma
    "a transcricao do video" em "o que se fala em CADA cena", que e' o formato
    que o `gerar.py` precisa para pendurar a fala no TAKE certo.
    """
    fala = [[] for _ in tks]
    for s in segs:
        melhor, area = None, 0.0
        for i, (a, b) in enumerate(tks):
            ov = min(b, s["t1"]) - max(a, s["t0"])
            if ov > area:
                melhor, area = i, ov
        if melhor is not None:
            fala[melhor].append(s["txt"])
    return [" ".join(f).strip() for f in fala]


PEDIDO = u"""# PEDIDO DE LEITURA — {slug}

> Cole este arquivo INTEIRO no chat, junto com a imagem `folha.jpg` desta
> mesma pasta. Salve a resposta como `mapa.json`, aqui do lado.

Voce vai ler UMA folha de contato de um video e devolver **so' JSON**, sem
texto antes nem depois.

O video tem **{n} take(s)**, ja' detectados por corte de cena:

{tabela}

A folha tem {q} quadros, {por} por take, na ordem dos takes. O tempo de cada
quadro esta' queimado em amarelo no canto.

## O QUE DEVOLVER

Um objeto com a chave `takes`, uma entrada por take, NA ORDEM:

```json
{{"takes": [
  {{"ambiente": "", "superficie": "", "props": [""], "gesto": "",
   "pessoa": "", "traje": "", "camera": "", "luz": "", "audio": "",
   "texto_em_quadro": ""}}
]}}
```

## REGRAS DURAS

- Tudo **EM INGLES** e pronto para entrar num prompt de imagem: frase
  descritiva, concreta, com material e cor. Nada de julgamento
  ("beautiful kitchen"), nada de marca, nada de nome de pessoa famosa.
- ⛔ NUNCA escreva `phone`, `iPhone`, `camera`, `filming`, `selfie` ou
  `tripod` no campo `camera`. Descreva o **angulo** e a **altura**. Escrever o
  aparelho faz o gerador DESENHAR o aparelho.
- ⛔ NUNCA escreva negacao do tipo `not a celebrity` ou `no phone in frame`:
  negacao INJETA o token. Descreva o que EXISTE.
- `props` e uma lista, um item por objeto, com cor, material e **posicao no
  quadro**.
- `pessoa`: o que aparece do corpo (so' maos? torso? rosto?), idade aparente,
  etnia, marcas distintivas. Se nao houver ninguem, escreva `none`.
- `texto_em_quadro`: a legenda queimada nessa cena, como aparece. Se nao
  houver, string vazia.
- Se um take estiver ambiguo na folha, descreva o que da' para ver e diga o
  que ficou incerto dentro do proprio campo. **Nao invente.**

## A FALA DE CADA TAKE, ja' alinhada por tempo

{falas}
"""


def main():
    ap = argparse.ArgumentParser(description="Etapa 1 da esteira — leitura local")
    ap.add_argument("video")
    ap.add_argument("--limiar", type=float, default=LIMIAR)
    ap.add_argument("--por-take", type=int, default=4)
    ap.add_argument("--sem-fala", action="store_true",
                    help="pula a transcricao (video mudo ou so' visual)")
    a = ap.parse_args()

    if not os.path.exists(a.video):
        raise SystemExit("nao achei o arquivo: %s" % a.video)

    slug = _slug(a.video)
    dest = os.path.join(SAIDA, slug)
    os.makedirs(dest, exist_ok=True)

    dur = duracao(a.video)
    cs = cortes(a.video, a.limiar)
    tks = takes(dur, cs)
    print("%s · %.1fs · %d corte(s) -> %d take(s)"
          % (slug, dur, len(cs), len(tks)))
    for i, (x, y) in enumerate(tks, 1):
        print("   take %d: %5.1fs -> %5.1fs  (%.1fs)" % (i, x, y, y - x))

    f, tempos = folha(a.video, tks, dest, a.por_take)
    print("folha: %s (%d quadros)" % (f, len(tempos)))

    segs = [] if a.sem_fala else transcrever(a.video)
    falas = alinhar(tks, segs) if segs else ["" for _ in tks]

    dossie = {"slug": slug, "arquivo": os.path.abspath(a.video),
              "duracao": round(dur, 2), "cortes": cs,
              "takes": [{"i": i + 1, "t0": round(x, 2), "t1": round(y, 2),
                         "fala": falas[i]} for i, (x, y) in enumerate(tks)],
              "transcricao": segs}
    io.open(os.path.join(dest, "dossie.json"), "w", encoding="utf-8").write(
        json.dumps(dossie, indent=1, ensure_ascii=False))

    tabela = "\n".join(
        "| take %d | %.1fs a %.1fs | %.1fs |" % (i + 1, x, y, y - x)
        for i, (x, y) in enumerate(tks))
    tabela = "| take | de/ate | duracao |\n|---|---|---|\n" + tabela
    blocos = "\n".join(
        "**take %d** (%.1fs a %.1fs): %s"
        % (i + 1, tks[i][0], tks[i][1], falas[i] or "_(sem fala)_")
        for i in range(len(tks)))

    io.open(os.path.join(dest, "PEDIDO.md"), "w", encoding="utf-8").write(
        PEDIDO.format(slug=slug, n=len(tks), tabela=tabela,
                      q=len(tempos), por=a.por_take, falas=blocos))

    print("\npronto em %s" % dest)
    print("  1. abra PEDIDO.md, cole no chat junto com folha.jpg")
    print("  2. salve a resposta como mapa.json nesta pasta")
    print("  3. python esteira/gerar.py %s" % slug)
    return 0


if __name__ == "__main__":
    sys.exit(main())
