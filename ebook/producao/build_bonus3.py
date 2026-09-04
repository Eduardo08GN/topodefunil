# -*- coding: utf-8 -*-
"""Monta o BÔNUS 3 — 50 HÁBITOS E EXERCÍCIOS.
30 EXERCÍCIOS como CARDS INDIVIDUAIS com FOTO (171-200), agrupados por tema;
20 HÁBITOS em 3 seções com foto de tema (201-203). Numeração contínua 1..50.
Uso: python build_bonus3.py
"""
import os
import time
import http.server
import socketserver
import threading
import importlib
import html as _html
import subprocess

import motor_receitas as motor
import exercicios_habitos as eh

PORTA = 8132
AQUI = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(AQUI, "fotos")

EXTRA_CSS = """
.b3cover{page-break-after:always;padding-top:24px}
.veg-badge{display:inline-block;background:var(--green);color:#fff;font-size:16px;font-weight:900;
letter-spacing:.14em;text-transform:uppercase;padding:9px 20px;border-radius:999px}
.b3cover h1{font-size:56px;font-weight:900;letter-spacing:-.03em;margin:18px 0 18px;line-height:1.0;color:var(--green)}
.b3cover .veg-rule{width:70px;height:5px;background:var(--gold);border-radius:3px;margin:0 0 20px}
.b3cover .lead{font-size:16px;color:var(--soft);line-height:1.6;max-width:97%}
.b3cover .how{margin-top:20px;font-size:15px;line-height:1.65}
.b3cover .how b{color:var(--green)}
/* cabeçalho de tema de exercício */
.exsec{margin-top:6px;page-break-before:always}
.exsec-head{margin-bottom:6px;break-after:avoid;page-break-after:avoid}
.exsec-pill{display:inline-block;background:var(--green);color:#fff;font-size:13px;font-weight:800;
text-transform:uppercase;letter-spacing:.09em;padding:8px 18px;border-radius:999px}
.exsec-head h2{font-size:24px;font-weight:900;letter-spacing:-.01em;margin:10px 0 4px;line-height:1.15}
.exsec-head .tintro{font-size:14.5px;color:var(--soft);line-height:1.5;max-width:97%}
/* card de exercício com foto */
.excard{display:grid;grid-template-columns:215px 1fr;gap:24px;padding:18px 0;border-top:1px solid var(--line);
break-inside:avoid;page-break-inside:avoid;align-items:start}
.excard-img{width:215px;height:215px;border-radius:14px;background:var(--cream);border:2px dashed #cfc8ba;
display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;color:#9a927f;padding:10px}
.excard-img b{font-size:13px;color:var(--green);font-weight:800}
.excard-img small{font-size:10.5px;margin-top:5px;line-height:1.4}
.excard-img img{width:100%;height:100%;object-fit:cover;border-radius:12px}
.exhead{display:flex;align-items:center;gap:10px;margin-bottom:7px}
.exnum{flex:none;width:30px;height:30px;background:var(--green);color:#fff;border-radius:50%;
display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:800}
.excard h3{font-size:19px;font-weight:800;color:var(--ink);line-height:1.15}
.excard .meta{font-size:13px;color:var(--soft);margin-bottom:9px}
.excard .meta .g{display:inline-block;background:var(--gold-tint);color:#8a6a1a;font-weight:800;
padding:2px 11px;border-radius:999px;margin-left:6px}
.excard .plano{font-size:14px;line-height:1.6;margin-bottom:7px}
.excard .dica{font-size:13.5px;line-height:1.55;color:var(--soft)}
.excard .lbl{color:var(--green);font-weight:800}
/* seção de hábitos com foto de tema */
.hsec{page-break-before:always;padding-top:6px}
.hsec-head{display:grid;grid-template-columns:215px 1fr;gap:24px;align-items:center;margin-bottom:12px}
.hsec-img{width:215px;height:215px;border-radius:14px;background:var(--cream);border:2px dashed #cfc8ba;
display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;color:#9a927f;padding:10px}
.hsec-img b{font-size:13px;color:var(--green);font-weight:800}
.hsec-img small{font-size:10.5px;margin-top:5px}
.hsec-img img{width:100%;height:100%;object-fit:cover;border-radius:12px}
.hsec-pill{display:inline-block;background:var(--green);color:#fff;font-size:12.5px;font-weight:800;
text-transform:uppercase;letter-spacing:.08em;padding:6px 15px;border-radius:999px}
.hsec-head h2{font-size:24px;font-weight:900;margin:10px 0 6px;line-height:1.15}
.hsec-head .tintro{font-size:14.5px;color:var(--soft);line-height:1.5}
.habitem{display:grid;grid-template-columns:34px 1fr;gap:8px;padding:11px 0;border-top:1px solid var(--line);
break-inside:avoid;page-break-inside:avoid;align-items:start}
.hn{font-size:15px;font-weight:900;color:var(--green);line-height:1.5}
.habitem p{font-size:14.5px;line-height:1.55}
.habitem p b{color:var(--ink);font-weight:800}
"""


def _img_html(num, cls):
    n3 = "%03d" % num
    for ext in (".jpg", ".jpeg", ".png", ".webp"):
        if os.path.isfile(os.path.join(IMG, n3 + ext)):
            return '<div class="%s"><img src="fotos/%s" alt=""></div>' % (cls, n3 + ext)
    return ('<div class="%s"><b>FOTO %s</b><small>espaço quadrado<br>reservado</small></div>'
            % (cls, n3))


def cover_html():
    return """
<div class="b3cover">
  <span class="veg-badge">Bônus 3</span>
  <h1>50 Hábitos e Exercícios</h1>
  <div class="veg-rule"></div>
  <p class="lead">A dieta faz a maior parte do trabalho, mas é o exercício que
    <b>acelera a queima</b>, define o corpo e faz o resultado durar. Aqui estão
    <b>30 exercícios</b> que realmente emagrecem — na rua, na esteira, na academia ou
    em casa, cada um com um <b>plano de evolução</b> — e <b>20 hábitos</b> que, somados,
    fazem a diferença.</p>
  <div class="how">
    <b>Como usar:</b> escolha um exercício de <b>cardio</b> (caminhada, bike, natação…)
    e faça de <b>3 a 5 vezes por semana</b>, seguindo a progressão. Junte <b>2 dias de
    força</b> (musculação ou treino em casa) para acelerar o metabolismo. Adote os
    hábitos aos poucos — é a soma de tudo que seca de verdade.
  </div>
</div>
"""


def exsec_html(t, contador):
    cards = ""
    for e in t["itens"]:
        contador[0] += 1
        cards += ("""<div class="excard">
  %s
  <div>
    <div class="exhead"><div class="exnum">%d</div><h3>%s</h3></div>
    <div class="meta">%s<span class="g">%s</span></div>
    <div class="plano"><span class="lbl">Progressão:</span> %s</div>
    <div class="dica"><span class="lbl">Dica:</span> %s</div>
  </div>
</div>""" % (_img_html(e["img"], "excard-img"), contador[0], _html.escape(e["nome"]),
            _html.escape(e["onde"]), _html.escape(e["gasto"]),
            _html.escape(e["plano"]), _html.escape(e["dica"])))
    return ("""<div class="exsec">
  <div class="exsec-head"><span class="exsec-pill">Exercícios</span><h2>%s</h2>
    <p class="tintro">%s</p></div>
  %s
</div>""" % (_html.escape(t["tema"]), _html.escape(t["intro"]), cards))


def hsec_html(t, contador):
    itens = ""
    for h in t["itens"]:
        contador[0] += 1
        itens += ('<div class="habitem"><div class="hn">%d</div>'
                  '<p><b>%s.</b> %s</p></div>'
                  % (contador[0], _html.escape(h["titulo"]), _html.escape(h["desc"])))
    return ("""<div class="hsec">
  <div class="hsec-head">%s
    <div><span class="hsec-pill">Hábitos</span><h2>%s</h2>
      <p class="tintro">%s</p></div>
  </div>
  %s
</div>""" % (_img_html(t["img"], "hsec-img"), _html.escape(t["tema"]),
            _html.escape(t["intro"]), itens))


def build():
    importlib.reload(eh)
    contador = [0]
    corpo = cover_html()
    for t in eh.TEMAS:
        if t["tipo"] == "exercicio":
            corpo += exsec_html(t, contador)
        else:
            corpo += hsec_html(t, contador)

    doc = ("""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">
<title>Bônus 3 — 50 Hábitos e Exercícios</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700;800;900&display=swap" rel="stylesheet">
<style>%s
%s</style></head><body>%s</body></html>""" % (motor.ESTILO, EXTRA_CSS, corpo))

    html_path = os.path.join(AQUI, "_tmp_bonus3.html")
    pdf_path = os.path.join(AQUI, "Passo 9 - Bônus 3 - 50 Hábitos e Exercícios.pdf")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(doc)

    def _srv():
        os.chdir(AQUI)
        with socketserver.TCPServer(("127.0.0.1", PORTA),
                                    http.server.SimpleHTTPRequestHandler) as s:
            s.serve_forever()
    threading.Thread(target=_srv, daemon=True).start()
    time.sleep(1.2)

    subprocess.run([motor.CHROME, "--headless=new", "--disable-gpu",
                    "--no-pdf-header-footer", "--virtual-time-budget=20000",
                    "--print-to-pdf=" + pdf_path,
                    "http://127.0.0.1:%d/%s" % (PORTA, "_tmp_bonus3.html")],
                   capture_output=True)
    ok = os.path.exists(pdf_path)
    print("Total de itens numerados:", contador[0])
    print("PDF:", pdf_path, "OK" if ok else "FALHOU",
          "(%.1f MB)" % (os.path.getsize(pdf_path) / 1e6) if ok else "")
    if ok and os.path.exists(html_path):
        os.remove(html_path)
    return ok


if __name__ == "__main__":
    build()
