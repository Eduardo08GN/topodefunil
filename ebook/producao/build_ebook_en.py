# -*- coding: utf-8 -*-
"""Generates the HTML + PDF of one ENGLISH category of the ebook.
Usage: python build_ebook_en.py <cafe|almoco|jantar|sobremesa|suco>
Mirrors build_ebook.py but renders with lang='en', reads receitas_<cat>_en.py,
reuses the shared fotos/ folder, and writes "Step N - Name.pdf" into
"../Entregavel em ENG". PT stays untouched.
"""
import sys
import os
import subprocess
import time
import http.server
import socketserver
import threading
import importlib

import motor_receitas as motor

CFG = {
    "cafe":   ("receitas_cafe_en",   "cafe",   1,  "Fit Breakfasts"),
    "almoco": ("receitas_almoco_en", "almoco", 31, "Fit Lunches"),
    "jantar": ("receitas_jantar_en", "jantar", 66, "Fit Dinners"),
    "sobremesa": ("receitas_sobremesa_en", "sobremesa", 101, "Fit Desserts"),
    "suco":   ("receitas_suco_en",   "suco",   121, "Smoothies and Detox Drinks"),
}
# clear PDF name delivered on Hotmart (separate files, plural categories)
PDF_NAME = {
    "cafe": "Step 2 - Breakfasts.pdf",
    "almoco": "Step 3 - Lunches.pdf",
    "jantar": "Step 4 - Dinners.pdf",
    "sobremesa": "Step 5 - Desserts.pdf",
    "suco": "Step 6 - Smoothies, Juices and Detox Teas.pdf",
}
PORTA = 8133
AQUI = os.path.dirname(os.path.abspath(__file__))
SAIDA = os.path.join(AQUI, "..", "Entregavel em ENG")


def _tag_suco(nome):
    n = nome.lower()
    if "tea" in n or "infus" in n:
        return "Detox tea"
    if "water" in n:
        return "Detox water"
    if "smoothie" in n or "shake" in n:
        return "Smoothie"
    return "Detox juice"


def _servidor():
    os.chdir(AQUI)
    h = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("127.0.0.1", PORTA), h) as srv:
        srv.serve_forever()


def build(cat):
    mod_nome, tipo, num0, titulo = CFG[cat]
    mod = importlib.import_module(mod_nome)
    importlib.reload(mod)
    img = os.path.join(AQUI, "fotos")
    if cat == "suco":
        for r in mod.RECEITAS:
            r.setdefault("tag", _tag_suco(r["nome"]))
    html = motor.montar_html(mod.RECEITAS, tipo, titulo, num0=num0, img_dir=img, lang="en")
    html_path = os.path.join(AQUI, cat + "_en.html")   # temporary (deleted at end)
    os.makedirs(SAIDA, exist_ok=True)
    pdf_path = os.path.join(SAIDA, PDF_NAME[cat])
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("HTML:", html_path, "(%d recipes)" % len(mod.RECEITAS))

    t = threading.Thread(target=_servidor, daemon=True)
    t.start()
    time.sleep(1.2)

    url = "http://127.0.0.1:%d/%s_en.html" % (PORTA, cat)
    subprocess.run([motor.CHROME, "--headless=new", "--disable-gpu",
                    "--no-pdf-header-footer",
                    "--virtual-time-budget=20000",
                    "--print-to-pdf=" + pdf_path, url],
                   capture_output=True)
    ok = os.path.exists(pdf_path)
    print("PDF:", pdf_path, "OK" if ok else "FAILED",
          "(%.1f MB)" % (os.path.getsize(pdf_path) / 1e6) if ok else "")
    if ok and os.path.exists(html_path):
        os.remove(html_path)
        print("intermediate HTML deleted (folder keeps only the PDF)")
    return ok


if __name__ == "__main__":
    cat = sys.argv[1] if len(sys.argv) > 1 else "cafe"
    build(cat)
