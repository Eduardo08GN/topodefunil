# -*- coding: utf-8 -*-
"""Gera o HTML + PDF de uma categoria do ebook TRADUZIDO.
Uso: python build_ebook_tr.py <de|fr> <cafe|almoco|jantar|sobremesa|suco>

⛔ UM builder para TODOS os idiomas. Copiar `build_ebook_de.py` para
`build_ebook_fr.py` criaria dois arquivos que divergem no primeiro conserto —
o mesmo motivo que fez a lente virar `lint_traducao.py`. Idioma novo entra em
`TEXTOS` + `PDF_NAME`, nunca em arquivo novo.
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

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

# (modulo base, tipo do motor, numero da primeira receita)
CATS = {
    "cafe":      ("receitas_cafe",      "cafe",      1),
    "almoco":    ("receitas_almoco",    "almoco",    31),
    "jantar":    ("receitas_jantar",    "jantar",    66),
    "sobremesa": ("receitas_sobremesa", "sobremesa", 101),
    "suco":      ("receitas_suco",      "suco",      121),
}

# titulo que aparece DENTRO do PDF (com acento certo)
TITULOS = {
    "de": {"cafe": "Fitness-Frühstück", "almoco": "Fitness-Mittagessen",
           "jantar": "Fitness-Abendessen", "sobremesa": "Fitness-Desserts",
           "suco": "Smoothies und Detox-Säfte"},
    "fr": {"cafe": "Petits-déjeuners minceur", "almoco": "Déjeuners minceur",
           "jantar": "Dîners minceur", "sobremesa": "Desserts minceur",
           "suco": "Smoothies et jus détox"},
}

# ⛔ nome de ARQUIVO sem acento, sem trema e sem ß: acento em nome de arquivo
# ja' quebrou download em plataforma. O titulo DENTRO do PDF leva os acentos.
PDF_NAME = {
    "de": {"cafe": "Schritt 2 - Fruehstueck.pdf",
           "almoco": "Schritt 3 - Mittagessen.pdf",
           "jantar": "Schritt 4 - Abendessen.pdf",
           "sobremesa": "Schritt 5 - Desserts.pdf",
           "suco": "Schritt 6 - Smoothies, Saefte und Detox-Tees.pdf"},
    "fr": {"cafe": "Etape 2 - Petits-dejeuners.pdf",
           "almoco": "Etape 3 - Dejeuners.pdf",
           "jantar": "Etape 4 - Diners.pdf",
           "sobremesa": "Etape 5 - Desserts.pdf",
           "suco": "Etape 6 - Smoothies, jus et thes detox.pdf"},
}

# rotulo da bebida, que muda por receita dentro da categoria `suco`.
# (palavra procurada no nome minusculo -> rotulo) + o rotulo padrao no fim.
TAG_BEBIDA = {
    "de": ([("tee", "Detox-Tee"), ("aufguss", "Detox-Tee"),
            ("wasser", "Detox-Wasser"), ("smoothie", "Smoothie")], "Detox-Saft"),
    "fr": ([("thé", "Thé détox"), ("tisane", "Thé détox"), ("infusion", "Thé détox"),
            ("eau", "Eau détox"), ("smoothie", "Smoothie")], "Jus détox"),
}

PORTA = 8132
AQUI = os.path.dirname(os.path.abspath(__file__))


def pasta_saida(lang):
    return os.path.join(AQUI, "..", "Entregavel em %s" % lang.upper())


def _tag_bebida(nome, lang):
    regras, padrao = TAG_BEBIDA[lang]
    n = nome.lower()
    for palavra, rotulo in regras:
        if palavra in n:
            return rotulo
    return padrao


def _servidor():
    os.chdir(AQUI)
    h = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("127.0.0.1", PORTA), h) as srv:
        srv.serve_forever()


def build(lang, cat):
    base, tipo, num0 = CATS[cat]
    mod = importlib.import_module("%s_%s" % (base, lang))
    importlib.reload(mod)
    img = os.path.join(AQUI, "fotos")
    if cat == "suco":
        for r in mod.RECEITAS:
            r.setdefault("tag", _tag_bebida(r["nome"], lang))
    html = motor.montar_html(mod.RECEITAS, tipo, TITULOS[lang][cat],
                             num0=num0, img_dir=img, lang=lang)

    html_path = os.path.join(AQUI, "_tmp_%s_%s.html" % (cat, lang))
    saida = pasta_saida(lang)
    os.makedirs(saida, exist_ok=True)
    pdf_path = os.path.join(saida, PDF_NAME[lang][cat])
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("HTML:", html_path, "(%d receitas)" % len(mod.RECEITAS))

    threading.Thread(target=_servidor, daemon=True).start()
    time.sleep(1.2)

    url = "http://127.0.0.1:%d/_tmp_%s_%s.html" % (PORTA, cat, lang)
    subprocess.run([motor.CHROME, "--headless=new", "--disable-gpu",
                    "--no-pdf-header-footer", "--virtual-time-budget=20000",
                    "--print-to-pdf=" + pdf_path, url], capture_output=True)
    ok = os.path.exists(pdf_path)
    print("PDF:", pdf_path, "OK" if ok else "FALHOU",
          "(%.1f MB)" % (os.path.getsize(pdf_path) / 1e6) if ok else "")
    if ok and os.path.exists(html_path):
        os.remove(html_path)
        print("HTML intermediario apagado")
    return ok


if __name__ == "__main__":
    lang = sys.argv[1] if len(sys.argv) > 1 else "de"
    cat = sys.argv[2] if len(sys.argv) > 2 else "cafe"
    sys.exit(0 if build(lang, cat) else 1)
