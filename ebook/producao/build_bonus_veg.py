# -*- coding: utf-8 -*-
"""Monta o BÔNUS 1 — DIETA VEGETARIANA num PDF:
  1) página de abertura (explicação + proteína vegetariana + como usar)
  2) lista das 12 receitas VEGETARIANAS que já existem no livro (café/sobremesa/sucos)
  3) as 8 receitas NOVAS (4 almoços + 4 jantares), template grande das outras.
Uso: python build_bonus_veg.py
"""
import os
import time
import http.server
import socketserver
import threading
import importlib

import motor_receitas as motor
import receitas_bonus_veg as veg

PORTA = 8132
AQUI = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(AQUI, "fotos")

# 12 receitas do próprio livro que já são vegetarianas (nome, número)
REUSO = {
    "Café da manhã": [("Panqueca de Banana e Aveia", 1),
                      ("Iogurte Grego com Frutas Vermelhas e Aveia", 3),
                      ("Mingau de Aveia com Banana e Pasta de Amendoim", 7),
                      ("Omelete de Cogumelos e Espinafre", 15)],
    "Sobremesa": [("Mousse de Chocolate com Abacate", 102),
                  ("Sorvete Cremoso de Banana", 106),
                  ("Gelatina de Frutas Caseira", 110),
                  ("Cheesecake Fit de Frutas Vermelhas", 116)],
    "Vitaminas e sucos": [("Suco Verde Detox", 121),
                          ("Vitamina de Banana com Aveia e Canela", 131),
                          ("Vitamina de Frutas Vermelhas", 133),
                          ("Vitamina de Abacate", 135)],
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
        linhas = "".join('<tr><td class="n">Receita %03d</td><td>%s</td></tr>' % (num, nome)
                         for nome, num in itens)
        blocos += ('<div class="reuse-cat"><h3>%s</h3><table>%s</table></div>'
                   % (cat, linhas))
    return blocos


def intro_html():
    return """
<div class="veg-cover">
  <span class="veg-badge">Bônus 1</span>
  <h1>Dieta Vegetariana</h1>
  <div class="veg-rule"></div>
  <p class="veg-lead">Cortar a carne não significa abrir mão de proteína, de sabor
    nem de saciedade. Uma dieta vegetariana bem montada é leve, barata e cheia de
    fibra — e pode acelerar o emagrecimento, desde que você garanta uma boa fonte
    de proteína em cada refeição. Aqui você tem <b>20 opções</b>, divididas
    igualmente entre café da manhã, almoço, jantar, sobremesa e sucos.</p>

  <div class="veg-box">
    <h2>De onde vem a proteína</h2>
    <ul>
      <li><b>Ovos</b> — proteína completa e muito saciante.</li>
      <li><b>Laticínios</b> — iogurte natural, queijo branco, ricota, cottage.</li>
      <li><b>Leguminosas</b> — feijão, lentilha, grão-de-bico e ervilha.</li>
      <li><b>Tofu</b> — feito de soja, cheio de proteína e com pouca gordura.</li>
      <li><b>Oleaginosas</b> — castanhas, nozes e pasta de amendoim (com moderação).</li>
    </ul>
    <div class="compl">Uma dica de ouro: junte uma <b>leguminosa</b> com um
      <b>cereal</b> na mesma refeição (arroz com feijão, grão-de-bico com arroz)
      e você forma uma proteína tão completa quanto a da carne.</div>
  </div>

  <div class="veg-how">
    <b>Como usar:</b> monte o seu dia escolhendo 1 café da manhã, 1 almoço,
    1 jantar, 1 sobremesa e 1 suco desta lista. As opções de café, sobremesa e
    suco já estão prontas no seu livro — é só procurar pelo número da receita.
    Os almoços e jantares vegetarianos são as <b>4 + 4 receitas novas</b> que
    vêm logo a seguir.
  </div>

  <div class="reuse">
    <h2>Do próprio livro</h2>
    <p class="sub">Estas receitas que você já tem são naturalmente vegetarianas —
      use-as à vontade dentro da dieta.</p>
    %s
  </div>
</div>

<div class="veg-recipes-head">
  <div class="kicker">Bônus 1 · Dieta Vegetariana</div>
  <h2>Almoços e jantares vegetarianos</h2>
  <p>As receitas a seguir são novas e feitas sem carne nem peixe — a proteína vem
    das leguminosas, do tofu, dos ovos e dos queijos. Cada uma traz a tabela de
    ajuste por perfil, igual às receitas do livro.</p>
</div>
""" % _reuse_html()


def build():
    importlib.reload(veg)
    corpo = intro_html()
    for i, r in enumerate(veg.ALMOCOS):
        corpo += motor.render_receita(r, "almoco", 151 + i, IMG)
    for i, r in enumerate(veg.JANTARES):
        corpo += motor.render_receita(r, "jantar", 155 + i, IMG)

    html = ("""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">
<title>Bônus 1 — Dieta Vegetariana</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700;800;900&display=swap" rel="stylesheet">
<style>%s
%s</style></head><body>%s</body></html>""" % (motor.ESTILO, INTRO_CSS, corpo))

    html_path = os.path.join(AQUI, "_tmp_bonus1.html")
    pdf_path = os.path.join(AQUI, "Passo 7 - Bônus 1 - Dieta Vegetariana.pdf")
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
                    "http://127.0.0.1:%d/%s" % (PORTA, "_tmp_bonus1.html")],
                   capture_output=True)
    ok = os.path.exists(pdf_path)
    print("PDF:", pdf_path, "OK" if ok else "FALHOU",
          "(%.1f MB)" % (os.path.getsize(pdf_path) / 1e6) if ok else "")
    if ok and os.path.exists(html_path):
        os.remove(html_path)
    return ok


if __name__ == "__main__":
    build()
