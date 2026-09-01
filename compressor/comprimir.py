# -*- coding: utf-8 -*-
"""COMPRIMIR - encolhe video e imagem sem perda visivel, via ffmpeg.

Uso:
    python comprimir.py <arquivo-ou-pasta>
    python comprimir.py "C:\\Users\\lucas\\Desktop\\videos"
    python comprimir.py video.mp4 --crf 23
    python comprimir.py pasta --x265          (HEVC: menor ainda, mais lento)
    python comprimir.py foto.png --para-jpg   (PNG-foto vira JPG)

O que ele faz e por que:
  VIDEO  -> reencoda com CRF (qualidade constante). CRF nao mira um tamanho:
            mira uma QUALIDADE e deixa o tamanho cair sozinho. E' o certo para
            "sem perder qualidade" — bitrate fixo faz o contrario, joga bits
            fora onde nao precisa e falta onde precisa.
  IMAGEM -> JPG reencoda com qualidade alta; PNG tenta o melhor sem perder
            (PNG e' sem perdas, entao encolhe pouco — use --para-jpg em FOTO).

⛔ NUNCA sobrescreve o original. A saida vai para uma subpasta `comprimidos/`
   ao lado do arquivo. Se o "comprimido" sair MAIOR que o original (ja' estava
   otimizado), o original e' copiado no lugar e o resultado e' avisado.
"""
import argparse
import os
import shutil
import subprocess
import sys

# ⛔ sob pythonw (app sem console) sys.stdout e' None: reconfigure
# estouraria na importacao e o app "nao abriria". Guardado.
if sys.stdout is not None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

VIDEO_EXT = {".mp4", ".mov", ".mkv", ".webm", ".avi", ".m4v"}
IMAGEM_EXT = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tiff"}


# --------------------------------------------------------------------------
# ⛔ SEM JANELA PRETA. Sob pythonw o app nao tem console, entao cada ffmpeg/
# ffprobe abria um cmd preto proprio (um por chamada). CREATE_NO_WINDOW no
# Windows faz o processo-filho nascer sem console. Fora do Windows a flag nao
# existe e vale 0.
_SEM_JANELA = getattr(subprocess, "CREATE_NO_WINDOW", 0)


def _run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True,
                          creationflags=_SEM_JANELA)


def _tamanho(p):
    return os.path.getsize(p)


def _mb(n):
    return n / (1024.0 * 1024.0)


def _pct(antes, depois):
    if antes <= 0:
        return 0.0
    return (1 - depois / float(antes)) * 100.0


def _tem_audio(caminho):
    r = _run(["ffprobe", "-v", "error", "-select_streams", "a",
              "-show_entries", "stream=codec_type", "-of", "csv=p=0", caminho])
    return "audio" in r.stdout


def _tem_alpha(caminho):
    """PNG com transparencia NAO pode virar JPG (JPG nao tem alpha)."""
    r = _run(["ffprobe", "-v", "error", "-select_streams", "v:0",
              "-show_entries", "stream=pix_fmt", "-of", "csv=p=0", caminho])
    pf = r.stdout.strip().lower()
    return "a" in pf and ("rgba" in pf or "ya" in pf or "argb" in pf or pf.endswith("a"))


# --------------------------------------------------------------------------
def comprimir_video(entrada, saida, crf, x265, preset):
    codec = "libx265" if x265 else "libx264"
    # ⛔ o x265 marca a stream com a tag hvc1, senao o QuickTime/alguns players
    # nao reconhecem. Sem isso o arquivo abre preto no Mac.
    tag = ["-tag:v", "hvc1"] if x265 else []
    cmd = ["ffmpeg", "-v", "error", "-y", "-i", entrada,
           "-c:v", codec, "-crf", str(crf), "-preset", preset,
           "-pix_fmt", "yuv420p"] + tag
    if _tem_audio(entrada):
        # AAC 128k e' transparente para narracao; nao ha' ganho em copiar um
        # audio que ja' costuma vir pesado dos geradores.
        cmd += ["-c:a", "aac", "-b:a", "128k"]
    else:
        cmd += ["-an"]
    # +faststart poe o indice no comeco: o video comeca a tocar antes de baixar
    # inteiro (importa no upload para FB/AdBatch).
    cmd += ["-movflags", "+faststart", saida]
    return _run(cmd)


def comprimir_imagem(entrada, saida, jpeg_q, para_jpg):
    ext = os.path.splitext(entrada)[1].lower()
    alvo_ext = os.path.splitext(saida)[1].lower()

    if alvo_ext in (".jpg", ".jpeg"):
        # qscale 2 (quase sem perda) a 5 (bem leve). 3 e' o ponto em que o olho
        # nao ve' diferenca e o arquivo ja' cai muito.
        cmd = ["ffmpeg", "-v", "error", "-y", "-i", entrada,
               "-qscale:v", str(jpeg_q), saida]
    elif alvo_ext == ".png":
        # PNG e' SEM PERDAS: da' para reempacotar melhor, mas nao ha' milagre.
        # compression_level 100 no libpng via ffmpeg pede o maximo.
        cmd = ["ffmpeg", "-v", "error", "-y", "-i", entrada,
               "-compression_level", "100", saida]
    elif alvo_ext == ".webp":
        cmd = ["ffmpeg", "-v", "error", "-y", "-i", entrada,
               "-quality", "88", saida]
    else:
        cmd = ["ffmpeg", "-v", "error", "-y", "-i", entrada, saida]
    return _run(cmd)


# --------------------------------------------------------------------------
def _saida_para(entrada, para_jpg):
    pasta = os.path.join(os.path.dirname(os.path.abspath(entrada)), "comprimidos")
    os.makedirs(pasta, exist_ok=True)
    nome, ext = os.path.splitext(os.path.basename(entrada))
    e = ext.lower()
    if e in IMAGEM_EXT:
        if para_jpg and e not in (".jpg", ".jpeg") and not _tem_alpha(entrada):
            ext = ".jpg"
        # PNG com alpha fica PNG mesmo com --para-jpg (JPG perderia a transparencia)
    return os.path.join(pasta, nome + ext)


def processar(entrada, args):
    e = os.path.splitext(entrada)[1].lower()
    if e not in VIDEO_EXT and e not in IMAGEM_EXT:
        return None
    saida = _saida_para(entrada, args.para_jpg)
    antes = _tamanho(entrada)

    if e in VIDEO_EXT:
        r = comprimir_video(entrada, saida, args.crf, args.x265, args.preset)
        tipo = "video"
    else:
        r = comprimir_imagem(entrada, saida, args.jpeg_q, args.para_jpg)
        tipo = "imagem"

    if r.returncode != 0 or not os.path.exists(saida):
        print("  >>> ERRO em %s: %s" % (os.path.basename(entrada),
                                        (r.stderr or "").strip()[:120]))
        return None

    depois = _tamanho(saida)
    # ⛔ se ficou MAIOR (ja' estava otimizado), fica com o original
    if depois >= antes:
        shutil.copy2(entrada, saida)
        print("  = %-40s ja' estava otimo (%.1f MB) — copiado sem mexer"
              % (os.path.basename(entrada)[:40], _mb(antes)))
        return (antes, antes)

    print("  %s %-38s %7.1f MB -> %6.1f MB  (-%.0f%%)"
          % ("V" if tipo == "video" else "I",
             os.path.basename(entrada)[:38], _mb(antes), _mb(depois),
             _pct(antes, depois)))
    return (antes, depois)


# --------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description="Comprime video e imagem sem perda visivel")
    ap.add_argument("caminho", help="arquivo ou pasta")
    ap.add_argument("--crf", type=int, default=23,
                    help="qualidade do video: 18 (quase perfeito, maior) a 28 "
                         "(bem menor). Padrao 23 = sem diferenca visivel.")
    ap.add_argument("--x265", action="store_true",
                    help="usa HEVC (H.265): ~30-40%% menor que o padrao, porem "
                         "mais lento para gerar")
    ap.add_argument("--preset", default="medium",
                    choices=["ultrafast", "fast", "medium", "slow", "veryslow"],
                    help="mais lento = menor arquivo. Padrao medium.")
    ap.add_argument("--jpeg-q", type=int, default=3,
                    help="qualidade JPG: 2 (quase perfeito) a 6 (leve). Padrao 3.")
    ap.add_argument("--para-jpg", action="store_true",
                    help="converte imagem (PNG sem transparencia) para JPG")
    args = ap.parse_args()

    if not os.path.exists(args.caminho):
        print(">>> nao encontrei: %s" % args.caminho); sys.exit(1)

    alvos = []
    if os.path.isdir(args.caminho):
        for nome in sorted(os.listdir(args.caminho)):
            p = os.path.join(args.caminho, nome)
            if os.path.isfile(p) and os.path.splitext(nome)[1].lower() in (VIDEO_EXT | IMAGEM_EXT):
                alvos.append(p)
    else:
        alvos = [args.caminho]

    if not alvos:
        print(">>> nenhum video ou imagem em %s" % args.caminho); sys.exit(1)

    print("=" * 66)
    print("codec video: %s CRF %d preset %s | JPG q%d%s"
          % ("H.265" if args.x265 else "H.264", args.crf, args.preset,
             args.jpeg_q, " | PNG->JPG" if args.para_jpg else ""))
    print("saida: subpasta 'comprimidos' ao lado dos arquivos")
    print("=" * 66)

    tot_antes = tot_depois = 0
    feitos = 0
    for p in alvos:
        r = processar(p, args)
        if r:
            tot_antes += r[0]; tot_depois += r[1]; feitos += 1

    print("=" * 66)
    if feitos:
        print("%d arquivo(s): %.1f MB -> %.1f MB  |  economia total %.0f%% (%.1f MB)"
              % (feitos, _mb(tot_antes), _mb(tot_depois),
                 _pct(tot_antes, tot_depois), _mb(tot_antes - tot_depois)))
    else:
        print("nada processado")


if __name__ == "__main__":
    main()
