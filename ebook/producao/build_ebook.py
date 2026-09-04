# -*- coding: utf-8 -*-
"""Gera o HTML + PDF de uma categoria do ebook.
Uso: python build_ebook.py <cafe|almoco|jantar|sobremesa|suco>
Cada categoria tem seu módulo receitas_<cat>.py, seu num inicial e título.
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
    "cafe":   ("receitas_cafe",   "cafe",   1,  "Cafés da Manhã Fit"),
    "almoco": ("receitas_almoco", "almoco", 31, "Almoços Fit"),
    "jantar": ("receitas_jantar", "jantar", 66, "Jantares Fit"),
    "sobremesa": ("receitas_sobremesa", "sobremesa", 101, "Sobremesas Fit"),
    "suco":   ("receitas_suco",   "suco",   121, "Vitaminas e Sucos Detox"),
}
# nome CLARO do PDF entregue no Hotmart (arquivos separados, categorias no plural)
PDF_NAME = {
    "cafe": "Passo 2 - Cafés da Manhã.pdf",
    "almoco": "Passo 3 - Almoços.pdf",
    "jantar": "Passo 4 - Jantares.pdf",
    "sobremesa": "Passo 5 - Sobremesas.pdf",
    "suco": "Passo 6 - Vitaminas, Sucos e Chás Detox.pdf",
}
PORTA = 8132
AQUI = os.path.dirname(os.path.abspath(__file__))


def _tag_suco(nome):
    n = nome.lower()
    if "chá" in n or "infus" in n:
        return "Chá detox"
    if "água" in n:
        return "Água detox"
    if "vitamina" in n or "smoothie" in n:
        return "Vitamina"
    return "Suco detox"


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
        # sucos/vitaminas/chás usam o MESMO template grande e legível das outras
        # categorias (1 por página). Só o rótulo varia por receita, e chás/águas
        # (livre:True) trocam a tabela pela faixa "bebida livre".
        for r in mod.RECEITAS:
            r.setdefault("tag", _tag_suco(r["nome"]))
    html = motor.montar_html(mod.RECEITAS, tipo, titulo, num0=num0, img_dir=img)
    html_path = os.path.join(AQUI, cat + ".html")  # temporário (apagado ao fim)
    pdf_path = os.path.join(AQUI, PDF_NAME[cat])    # nome claro para o Hotmart
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("HTML:", html_path, "(%d receitas)" % len(mod.RECEITAS))

    t = threading.Thread(target=_servidor, daemon=True)
    t.start()
    time.sleep(1.2)

    url = "http://127.0.0.1:%d/%s.html" % (PORTA, cat)
    subprocess.run([motor.CHROME, "--headless=new", "--disable-gpu",
                    "--no-pdf-header-footer",
                    "--virtual-time-budget=20000",
                    "--print-to-pdf=" + pdf_path, url],
                   capture_output=True)
    ok = os.path.exists(pdf_path)
    print("PDF:", pdf_path, "OK" if ok else "FALHOU",
          "(%.1f MB)" % (os.path.getsize(pdf_path) / 1e6) if ok else "")
    # o HTML e' so' intermediario: o PDF ja sai com as imagens embutidas.
    # apaga o .html apos gerar, para a pasta guardar so' os PDFs.
    if ok and os.path.exists(html_path):
        os.remove(html_path)
        print("HTML intermediario apagado (pasta guarda so' o PDF)")
    return ok


if __name__ == "__main__":
    cat = sys.argv[1] if len(sys.argv) > 1 else "almoco"
    build(cat)
