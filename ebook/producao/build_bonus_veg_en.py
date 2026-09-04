# -*- coding: utf-8 -*-
"""Builds BONUS 1 — VEGETARIAN DIET (English) into a PDF:
  1) opening page (intro + vegetarian protein + how to use)
  2) list of the 12 VEGETARIAN recipes already in the book (breakfast/dessert/drinks)
  3) the 8 NEW recipes (4 lunches + 4 dinners), big template like the others.
Usage: python build_bonus_veg_en.py
"""
import os
import time
import http.server
import socketserver
import threading
import importlib

import motor_receitas as motor
import receitas_bonus_veg_en as veg

PORTA = 8134
AQUI = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(AQUI, "fotos")
SAIDA = os.path.join(AQUI, "..", "Entregavel em ENG")

# 12 recipes from the book itself that are already vegetarian (English name, number)
REUSO = {
    "Breakfast": [("Banana Oat Pancakes", 1),
                  ("Greek Yogurt with Berries and Oats", 3),
                  ("Oatmeal Porridge with Banana and Peanut Butter", 7),
                  ("Mushroom and Spinach Omelette", 15)],
    "Dessert": [("Chocolate Avocado Mousse", 102),
                ("Creamy Banana Nice Cream", 106),
                ("Homemade Fruit Jelly", 110),
                ("No-Bake Fit Berry Cheesecake", 116)],
    "Smoothies and juices": [("Detox Green Juice", 121),
                             ("Banana Oat Smoothie with Cinnamon", 131),
                             ("Mixed Berry Smoothie", 133),
                             ("Avocado Smoothie", 135)],
}

INTRO_CSS = """
.veg-cover{page-break-after:always;padding-top:24px}
.kicker{font-size:13px;font-weight:800;letter-spacing:.18em;text-transform:uppercase;color:var(--gold)}
.veg-badge{display:inline-block;background:var(--green);color:#fff;font-size:16px;font-weight:900;
letter-spacing:.14em;text-transform:uppercase;padding:9px 20px;border-radius:999px}
.veg-cover h1{font-size:66px;font-weight:900;letter-spacing:-.03em;margin:18px 0 20px;line-height:1.0;color:var(--green)}
.veg-cover .veg-rule{width:70px;height:5px;background:var(--gold);border-radius:3px;margin:0 0 20px}
.veg-lead{font-size:16px;color:var(--soft);line-height:1.6;max-width:96%}
.veg-box{margin-top:22px;background:var(--green-tint);border-radius:16px;padding:20px 24px}
.veg-box h2{font-size:15px;color:var(--green);text-transform:uppercase;letter-spacing:.06em;margin-bottom:10px}
.veg-box ul{list-style:none;margin:0}
.veg-box li{font-size:15px;padding:5px 0 5px 20px;position:relative;line-height:1.5}
.veg-box li::before{content:"";position:absolute;left:0;top:11px;width:7px;height:7px;border-radius:50%;background:var(--green)}
.veg-box .compl{margin-top:12px;font-size:14.5px;color:var(--soft);line-height:1.6}
.veg-how{margin-top:22px;font-size:15px;line-height:1.65}
.veg-how b{color:var(--green)}
.reuse{margin-top:24px}
.reuse > h2{font-size:20px;font-weight:900;margin-bottom:6px}
.reuse .sub{font-size:14.5px;color:var(--soft);margin-bottom:16px;line-height:1.55}
.reuse-cat{margin-top:20px;break-inside:avoid;page-break-inside:avoid}
.reuse-cat h3{display:inline-block;background:var(--green);color:#fff;font-size:13px;font-weight:800;
text-transform:uppercase;letter-spacing:.09em;padding:8px 18px;border-radius:999px;margin-bottom:10px}
.reuse-cat table{width:100%;border-collapse:collapse}
.reuse-cat td{padding:8px 4px;font-size:15px;border-bottom:1px solid var(--line);line-height:1.4}
.reuse-cat td.n{width:120px;color:var(--green);font-weight:800;white-space:nowrap}
.veg-recipes-head{page-break-before:always;padding-top:6px}
.veg-recipes-head .kicker{color:var(--gold)}
.veg-recipes-head h2{font-size:30px;font-weight:900;letter-spacing:-.01em;margin:6px 0 8px;line-height:1.1}
.veg-recipes-head p{font-size:15px;color:var(--soft);line-height:1.6;max-width:96%;margin-bottom:6px}
"""


def _reuse_html():
    blocos = ""
    for cat, itens in REUSO.items():
        linhas = "".join('<tr><td class="n">Recipe %03d</td><td>%s</td></tr>' % (num, nome)
                         for nome, num in itens)
        blocos += ('<div class="reuse-cat"><h3>%s</h3><table>%s</table></div>'
                   % (cat, linhas))
    return blocos


def intro_html():
    return """
<div class="veg-cover">
  <span class="veg-badge">Bonus 1</span>
  <h1>Vegetarian Diet</h1>
  <div class="veg-rule"></div>
  <p class="veg-lead">Cutting out meat does not mean giving up protein, flavor or
    fullness. A well-built vegetarian diet is light, cheap and full of fiber — and
    it can speed up weight loss, as long as you make sure to have a good protein
    source at every meal. Here you have <b>20 options</b>, split evenly between
    breakfast, lunch, dinner, dessert and drinks.</p>

  <div class="veg-box">
    <h2>Where the protein comes from</h2>
    <ul>
      <li><b>Eggs</b> — a complete, very filling protein.</li>
      <li><b>Dairy</b> — plain yogurt, white cheese, ricotta, cottage cheese.</li>
      <li><b>Legumes</b> — beans, lentils, chickpeas and peas.</li>
      <li><b>Tofu</b> — made from soy, full of protein and low in fat.</li>
      <li><b>Nuts and seeds</b> — nuts, walnuts and peanut butter (in moderation).</li>
    </ul>
    <div class="compl">A golden tip: pair a <b>legume</b> with a <b>grain</b> in the
      same meal (rice with beans, chickpeas with rice) and you form a protein as
      complete as the one from meat.</div>
  </div>

  <div class="veg-how">
    <b>How to use it:</b> build your day by choosing 1 breakfast, 1 lunch, 1 dinner,
    1 dessert and 1 drink from this list. The breakfast, dessert and drink options
    are already in your book — just look them up by the recipe number. The
    vegetarian lunches and dinners are the <b>4 + 4 new recipes</b> that come
    next.
  </div>

  <div class="reuse">
    <h2>From the book itself</h2>
    <p class="sub">These recipes you already have are naturally vegetarian — use
      them freely within the diet.</p>
    %s
  </div>
</div>

<div class="veg-recipes-head">
  <div class="kicker">Bonus 1 · Vegetarian Diet</div>
  <h2>Vegetarian lunches and dinners</h2>
  <p>The recipes that follow are new and made with no meat or fish — the protein
    comes from legumes, tofu, eggs and cheese. Each one has the adjustment table by
    profile, just like the book's recipes.</p>
</div>
""" % _reuse_html()


def build():
    importlib.reload(veg)
    corpo = intro_html()
    for i, r in enumerate(veg.ALMOCOS):
        corpo += motor.render_receita(r, "almoco", 151 + i, IMG, lang="en")
    for i, r in enumerate(veg.JANTARES):
        corpo += motor.render_receita(r, "jantar", 155 + i, IMG, lang="en")

    html = ("""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<title>Bonus 1 — Vegetarian Diet</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700;800;900&display=swap" rel="stylesheet">
<style>%s
%s</style></head><body>%s</body></html>""" % (motor.ESTILO, INTRO_CSS, corpo))

    html_path = os.path.join(AQUI, "_tmp_bonus1_en.html")
    os.makedirs(SAIDA, exist_ok=True)
    pdf_path = os.path.join(SAIDA, "Step 7 - Bonus 1 - Vegetarian Diet.pdf")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)

    def _srv():
        os.chdir(AQUI)
        with socketserver.TCPServer(("127.0.0.1", PORTA),
                                    http.server.SimpleHTTPRequestHandler) as s:
            s.serve_forever()
    threading.Thread(target=_srv, daemon=True).start()
    time.sleep(1.2)

    import subprocess
    subprocess.run([motor.CHROME, "--headless=new", "--disable-gpu",
                    "--no-pdf-header-footer", "--virtual-time-budget=20000",
                    "--print-to-pdf=" + pdf_path,
                    "http://127.0.0.1:%d/%s" % (PORTA, "_tmp_bonus1_en.html")],
                   capture_output=True)
    ok = os.path.exists(pdf_path)
    print("PDF:", pdf_path, "OK" if ok else "FAILED",
          "(%.1f MB)" % (os.path.getsize(pdf_path) / 1e6) if ok else "")
    if ok and os.path.exists(html_path):
        os.remove(html_path)
    return ok


if __name__ == "__main__":
    build()
