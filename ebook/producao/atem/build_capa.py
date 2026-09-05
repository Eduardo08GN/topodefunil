# -*- coding: utf-8 -*-
"""CAPAS DO PRODUTO — compostas em HTML e rasterizadas pelo Chrome.

⛔ O TEXTO DA CAPA NAO SAI DO GERADOR DE IMAGEM. Nano Banana escreve texto
razoavel em ingles e erra trema em alemao — e uma capa com `Atemanker` sem o
trema certo ou com uma letra a mais e' um produto que parece falsificado. A
FOTO vem do gerador; a PALAVRA vem do motor, onde ela e' uma string que eu
controlo caractere a caractere.

Gera:
  capa-atem-800x1000.jpg   arte do livro para a landing
  capa-atem-600x600.jpg    imagem do produto na Hotmart (quadrada)

    python build_capa.py
"""

import os
import subprocess

import motor_atem as M

AQUI = os.path.dirname(os.path.abspath(__file__))

TITULO = "DER<br>ATEMANKER"
SUB = "Die 2-Minuten-Methode<br>gegen innere Unruhe"
RODAPE = "Ohne Eis. Ohne Ausrüstung. Zu Hause."
FOTO = "fotos/persona.jpg"

# ⭐ A linha do rodape e' a lente `GE5` do funil impressa na capa: a imagem do
# criativo e' gelo, a oferta e' respiracao. Quem chega do video le' `ohne Eis`
# antes de qualquer outra coisa e a promessa fecha em vez de trocar de assunto.

_CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{width:%(W)dpx;height:%(H)dpx;overflow:hidden;position:relative;
font-family:"DM Sans",system-ui,sans-serif;background:#0f2b1e}
.bg{position:absolute;inset:0;width:100%%;height:100%%;object-fit:cover}
.scrim{position:absolute;inset:0;background:
linear-gradient(180deg, rgba(8,32,22,.80) 0%%, rgba(8,32,22,.34) 34%%,
rgba(8,32,22,.30) 56%%, rgba(8,32,22,.86) 100%%)}
.wrap{position:absolute;inset:0;display:flex;flex-direction:column;
justify-content:space-between;padding:%(P)dpx %(P)dpx %(PB)dpx}
.eyebrow{display:inline-block;align-self:flex-start;background:#D9A441;color:#2b1e04;
font-size:%(EY)dpx;font-weight:900;letter-spacing:.16em;padding:%(EYP)dpx %(EYPX)dpx;
border-radius:999px}
h1{color:#fff;font-size:%(T)dpx;font-weight:900;line-height:.95;letter-spacing:-.035em;
text-shadow:0 3px 26px rgba(0,0,0,.5);margin-top:%(TM)dpx}
.rule{width:%(RW)dpx;height:%(RH)dpx;background:#D9A441;border-radius:4px;margin:%(RM)dpx 0}
.sub{color:#EAF3EC;font-size:%(S)dpx;font-weight:600;line-height:1.32;
text-shadow:0 2px 16px rgba(0,0,0,.55)}
.foot{color:#fff;font-size:%(F)dpx;font-weight:800;letter-spacing:.02em;
text-shadow:0 2px 16px rgba(0,0,0,.6)}
.dot{color:#D9A441}
"""

_HTML = """<!doctype html><html lang="de"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<style>%(css)s</style></head><body>
<img class="bg" src="%(foto)s">
<div class="scrim"></div>
<div class="wrap">
  <div>
    <span class="eyebrow">7 DATEIEN &middot; SOFORT-DOWNLOAD</span>
    <h1>%(titulo)s</h1>
    <div class="rule"></div>
    <p class="sub">%(sub)s</p>
  </div>
  <p class="foot">%(rodape)s</p>
</div></body></html>"""


def _render(nome, W, H, dim):
    css = _CSS % dim
    html = _HTML % {"css": css, "foto": FOTO, "titulo": TITULO,
                    "sub": SUB, "rodape": RODAPE}
    tmp = os.path.join(AQUI, "_tmp_capa.html")
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(html)
    png = os.path.join(AQUI, nome + ".png")
    subprocess.run([M.CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                    "--force-device-scale-factor=2",
                    "--virtual-time-budget=15000",
                    "--window-size=%d,%d" % (W, H),
                    "--screenshot=" + png,
                    "file:///" + tmp.replace("\\", "/")], capture_output=True)
    if not os.path.exists(png):
        print("FALHOU:", nome)
        return None
    from PIL import Image
    im = Image.open(png).convert("RGB").resize((W, H), Image.LANCZOS)
    jpg = os.path.join(AQUI, nome + ".jpg")
    im.save(jpg, quality=92)
    os.remove(png)
    os.remove(tmp)
    print("CAPA: %-26s %dx%d  %.0f KB" % (nome, W, H, os.path.getsize(jpg) / 1024))
    return jpg


def main():
    _render("capa-atem-800x1000", 800, 1000, dict(
        W=800, H=1000, P=54, PB=48, EY=15, EYP=10, EYPX=20,
        T=82, TM=26, RW=86, RH=7, RM=26, S=27, F=21))
    _render("capa-atem-600x600", 600, 600, dict(
        W=600, H=600, P=40, PB=34, EY=12, EYP=8, EYPX=16,
        T=62, TM=18, RW=64, RH=6, RM=18, S=20, F=16))


if __name__ == "__main__":
    main()
