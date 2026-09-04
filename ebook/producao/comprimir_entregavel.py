# -*- coding: utf-8 -*-
"""Comprime os PDFs de um entregavel RECOMPRIMINDO AS FOTOS DENTRO DELES.

⛔ Nao regera o PDF: abre o que ja' existe e troca cada imagem embutida por uma
versao menor. Assim o layout, a paginacao e o texto ficam BYTE a byte iguais —
o unico que muda e' o pixel da foto. Regerar o PT (que ja' vende) para encolher
foto seria arriscar o produto por um motivo que nao exige risco.

Uso:  python comprimir_entregavel.py <PT|EN|DE|FR|todos> [--lado 640] [--q 80] [--dry-run]
"""
import io
import os
import sys
import glob

import pikepdf
from PIL import Image

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

AQUI = os.path.dirname(os.path.abspath(__file__))
IDIOMAS = ("PT", "EN", "DE", "FR")


def _recomprime(im_obj, lado, q):
    """Devolve (bytes_jpeg, largura, altura) ou None se nao vale a pena."""
    try:
        pil = pikepdf.PdfImage(im_obj).as_pil_image()
    except Exception:
        return None
    if pil.mode not in ("RGB", "L"):
        pil = pil.convert("RGB")
    w, h = pil.size
    if max(w, h) > lado:
        nw = lado if w >= h else max(1, round(w * lado / h))
        nh = lado if h > w else max(1, round(h * lado / w))
        pil = pil.resize((nw, nh), Image.LANCZOS)
    buf = io.BytesIO()
    pil.save(buf, format="JPEG", quality=q, optimize=True, progressive=True)
    return buf.getvalue(), pil.size[0], pil.size[1], pil.mode


def comprime_pdf(caminho, lado, q, dry=False):
    antes = os.path.getsize(caminho)
    pdf = pikepdf.open(caminho, allow_overwriting_input=True)
    trocadas = 0
    vistas = set()
    for pagina in pdf.pages:
        for nome, im in list(pagina.images.items()):
            chave = im.objgen
            if chave in vistas:
                continue
            vistas.add(chave)
            r = _recomprime(im, lado, q)
            if not r:
                continue
            dados, nw, nh, modo = r
            if len(dados) >= int(im.stream_dict.get("/Length", 10 ** 9)):
                continue                      # ja' esta menor: nao mexe
            im.write(dados, filter=pikepdf.Name("/DCTDecode"))
            im.Width, im.Height = nw, nh
            im.ColorSpace = pikepdf.Name("/DeviceRGB" if modo == "RGB" else "/DeviceGray")
            im.BitsPerComponent = 8
            for k in ("/SMask", "/Decode", "/DecodeParms"):
                if k in im:
                    del im[k]
            trocadas += 1
    if not dry:
        pdf.save(caminho, linearize=True)
    pdf.close()
    depois = os.path.getsize(caminho) if not dry else antes
    return antes, depois, trocadas


def main():
    args = [a for a in sys.argv[1:]]
    dry = "--dry-run" in args
    lado = 640
    q = 80
    if "--lado" in args:
        lado = int(args[args.index("--lado") + 1])
    if "--q" in args:
        q = int(args[args.index("--q") + 1])
    alvo = next((a.upper() for a in args if a.upper() in IDIOMAS or a.lower() == "todos"), None)
    if not alvo:
        print(__doc__)
        return 2
    langs = list(IDIOMAS) if alvo == "TODOS" else [alvo]

    ta = td = 0
    for lang in langs:
        d = os.path.join(AQUI, "..", "Entregavel em %s" % lang)
        fs = sorted(glob.glob(os.path.join(d, "*.pdf")))
        if not fs:
            print("[ERRO] sem PDFs em %s" % d)
            return 1
        print("=" * 18, lang, "=" * 18)
        la = ld = 0
        for f in fs:
            a, dp, n = comprime_pdf(f, lado, q, dry)
            la += a
            ld += dp
            print("  %-50s %6.1f -> %5.1f MB  (%d imgs)"
                  % (os.path.basename(f)[:50], a / 1e6, dp / 1e6, n))
        print("  %-50s %6.1f -> %5.1f MB   (-%.0f%%)"
              % ("TOTAL", la / 1e6, ld / 1e6, 100 * (1 - ld / la) if la else 0))
        print()
        ta += la
        td += ld
    if len(langs) > 1:
        print("GERAL: %.1f -> %.1f MB  (-%.0f%%)" % (ta / 1e6, td / 1e6, 100 * (1 - td / ta)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
