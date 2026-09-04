# -*- coding: utf-8 -*-
"""BOOK FRONT — "Start Here" (Step 1). English (US market).
Welcome, how the material works, honest notes, YouTube tip, note/print,
calories/portions note and the 30-DAY MEAL PLAN.
Generates: "Step 1 - Start Here.pdf" into ../Entregavel em ENG.
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
import receitas_cafe_en as R_cafe
import receitas_almoco_en as R_almoco
import receitas_jantar_en as R_jantar
import receitas_sobremesa_en as R_sobremesa
import receitas_suco_en as R_suco

PORTA = 8137
AQUI = os.path.dirname(os.path.abspath(__file__))
SAIDA = os.path.join(AQUI, "..", "Entregavel em ENG")


def _nome(mod, i):
    return mod.RECEITAS[i]["nome"]


EXTRA_CSS = """
.cover{page-break-after:always;padding-top:30px}
.badge{display:inline-block;background:var(--green);color:#fff;font-size:16px;font-weight:900;
letter-spacing:.14em;text-transform:uppercase;padding:9px 20px;border-radius:999px}
.cover h1{font-size:62px;font-weight:900;letter-spacing:-.03em;margin:18px 0 18px;line-height:1.0;color:var(--green)}
.cover .rule{width:70px;height:5px;background:var(--gold);border-radius:3px;margin:0 0 22px}
.cover .lead{font-size:18.5px;color:var(--soft);line-height:1.7;max-width:97%}
.sec{page-break-before:always;padding-top:6px}
.sec h2{font-size:32px;font-weight:900;letter-spacing:-.01em;color:var(--green);margin-bottom:8px;line-height:1.1}
.sec .sub{font-size:17px;color:var(--soft);line-height:1.6;margin-bottom:18px;max-width:97%}
.sec p{font-size:17.5px;line-height:1.7;margin-bottom:13px}
.sec p b{color:var(--ink)}
.stepbox{display:grid;grid-template-columns:44px 1fr;gap:12px;padding:13px 0;border-bottom:1px solid var(--line);break-inside:avoid;align-items:start}
.stepbox .sn{width:36px;height:36px;background:var(--green);color:#fff;border-radius:50%;
display:flex;align-items:center;justify-content:center;font-size:16px;font-weight:800}
.stepbox p{font-size:17px;line-height:1.55;margin:0}
.stepbox p b{color:var(--ink);font-weight:800}
.warn{background:var(--gold-tint);border-left:4px solid var(--gold);border-radius:0 12px 12px 0;
padding:18px 22px;margin-bottom:16px;break-inside:avoid}
.warn b{color:#8a6a1a;font-size:14px;text-transform:uppercase;letter-spacing:.05em;display:block;margin-bottom:6px}
.warn p{font-size:17px;line-height:1.6;margin:0}
.tipbox{background:var(--green-tint);border-radius:14px;padding:20px 24px;margin-bottom:16px;break-inside:avoid}
.tipbox h3{font-size:16.5px;color:var(--green);text-transform:uppercase;letter-spacing:.05em;margin-bottom:9px}
.tipbox p{font-size:17px;line-height:1.6;margin:0}
.plan-note{font-size:16px;color:var(--soft);line-height:1.6;margin-bottom:20px}
.dcard{padding:15px 0 13px;border-top:1.5px solid var(--line);break-inside:avoid;page-break-inside:avoid}
.dcard h3{font-size:21px;font-weight:900;color:var(--green);margin-bottom:11px}
.drow{display:grid;grid-template-columns:160px 1fr;gap:10px;padding:5px 0;align-items:baseline}
.drow .lbl{color:var(--soft);font-weight:800;font-size:13.5px;text-transform:uppercase;letter-spacing:.04em}
.drow .val{font-size:16.5px;line-height:1.45;color:var(--ink)}
.drow .val .n{color:var(--green);font-weight:800;margin-right:6px}
"""


def cover():
    return """
<div class="cover">
  <span class="badge">Start Here</span>
  <h1>Welcome!</h1>
  <div class="rule"></div>
  <p class="lead">It is great to have you here. You have just taken the first step to
    lose weight by eating well, without going hungry and without crazy diets. This
    material is a <b>complete protocol</b>: 150 fit recipes, a 30-day plan and three
    bonuses of exercises and habits. Before you start cooking, read these first pages
    carefully — they will save you time and prevent frustration. Let's do this
    together!</p>
</div>
"""


def como_funciona():
    passos = [
     ("Start Here", "This file. The instructions, the notes and the 30-day plan."),
     ("Breakfasts", "30 recipes to start the day with energy and fullness."),
     ("Lunches", "35 complete, light dishes for the middle of the day."),
     ("Dinners", "35 lighter options for the evening."),
     ("Desserts", "20 fit, sugar-free treats to beat the craving with no guilt."),
     ("Smoothies, Juices and Detox Teas", "30 drinks to hydrate, debloat and boost you."),
     ("Bonus 1 — Vegetarian Diet", "20 meat-free options, evenly split."),
     ("Bonus 2 — Belly-Slimming Pilates at Home", "12 core exercises, no equipment."),
     ("Bonus 3 — 50 Habits and Exercises", "The exercises and habits that speed up results."),
    ]
    linhas = ""
    for i, (t, d) in enumerate(passos, 1):
        linhas += ('<div class="stepbox"><div class="sn">%d</div>'
                   '<p><b>Step %d — %s.</b> %s</p></div>' % (i, i, _html.escape(t), _html.escape(d)))
    return """<div class="sec">
  <h2>How this material works</h2>
  <p class="sub">To keep things organized, the material comes in separate files, numbered
    as <b>steps</b>. Follow the order — each step is a part of your day.</p>
  %s
  <p style="margin-top:16px">Inside each file, the recipes have a <b>number</b>
    (for example, <b>Recipe 003</b>). It is by that number that the 30-day plan, further
    on, tells you what to eat each day.</p>
</div>""" % linhas


def avisos():
    itens = [
     ("The diet works no miracles", "There is no magic formula. What there is, is consistency. Following the menu during the week and going overboard on sweets and fried food on the weekend cancels out all the effort. Results come to those who keep the habit most of the time."),
     ("Results take a few months", "You will not change overnight — and that is a good thing, because what comes fast also leaves fast. Give your body a few months of consistency and the change will be solid and lasting."),
     ("Exercise is part of it", "Food is the biggest part, but the body truly transforms when you also move. Bonuses 2 and 3 bring exercises for all levels, at home and outside. Use them."),
     ("No false promises", "We do not promise you will lose 20 pounds in a week, because that would be a lie. We deliver a complete, honest protocol that, followed with consistency, can bring real and lasting results."),
    ]
    blocos = ""
    for t, d in itens:
        blocos += ('<div class="warn"><b>%s</b><p>%s</p></div>'
                   % (_html.escape(t), _html.escape(d)))
    return """<div class="sec">
  <h2>The truth, honestly</h2>
  <p class="sub">Before any recipe, four truths no one usually tells you —
    and that make all the difference to your success.</p>
  %s
</div>""" % blocos


def dicas():
    return """<div class="sec">
  <h2>Tips to get the most out of it</h2>
  <p class="sub">Small tricks that make your journey easier.</p>

  <div class="tipbox">
    <h3>Not sure about a recipe? Use YouTube</h3>
    <p>If you do not know how to do a step, just search YouTube for the
      <b>recipe name + "how to make"</b> and videos will show you the step by step.
      It is a big help, especially at the start.</p>
  </div>

  <div class="tipbox">
    <h3>Note down and print what you will use</h3>
    <p>Mark the recipes you liked most and make <b>notes</b> of what to buy and prepare
      for the week. If you prefer, <b>print</b> the pages of the foods, habits and
      exercises you are interested in and keep them in sight, in the kitchen or on the
      fridge. What is within reach gets done.</p>
  </div>

  <div class="tipbox">
    <h3>About the calories and portions</h3>
    <p>The calories in each recipe are <b>approximate values</b>, calculated from
      standard nutrition tables — a guide, not an exact lab measurement. Each recipe has
      an <b>adjustment table by sex and weight</b>: find your row and follow those
      amounts. Vegetables, greens, coffee and unsweetened tea are free — enjoy them
      freely, no need to count.</p>
  </div>
</div>"""


def _row(lbl, num, mod, idx):
    return ('<div class="drow"><span class="lbl">%s</span>'
            '<span class="val"><span class="n">%03d</span>%s</span></div>'
            % (lbl, num, _html.escape(_nome(mod, idx))))


def plano_30():
    dias = ""
    for dia in range(1, 31):
        s = ((dia - 1) % 20) + 1   # dessert 101..120, repeats after 20
        dias += ("""<div class="dcard"><h3>Day %d</h3>
  %s%s%s%s%s</div>""" % (
            dia,
            _row("Breakfast", dia, R_cafe, dia - 1),
            _row("Lunch", 30 + dia, R_almoco, dia - 1),
            _row("Dinner", 65 + dia, R_jantar, dia - 1),
            _row("Dessert", 100 + s, R_sobremesa, s - 1),
            _row("Drink", 120 + dia, R_suco, dia - 1)))
    return """<div class="sec">
  <h2>30-Day Meal Plan</h2>
  <p class="sub">A whole month laid out for you — just follow it. Each day has a
    different breakfast, lunch, dinner, dessert and drink, with no repeated dishes
    across the month.</p>
  <p class="plan-note">The number before each recipe shows where to find it in the
    category file (for example, <b>Recipe 031</b> is in the <b>Lunches</b> file). The
    desserts, being 20, restart from day 21. Feel free to swap any dish for another in
    the same category you prefer.</p>
  %s
</div>""" % dias


def build():
    for m in (R_cafe, R_almoco, R_jantar, R_sobremesa, R_suco):
        importlib.reload(m)
    corpo = cover() + como_funciona() + avisos() + dicas() + plano_30()
    doc = ("""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<title>Start Here</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700;800;900&display=swap" rel="stylesheet">
<style>%s
%s</style></head><body>%s</body></html>""" % (motor.ESTILO, EXTRA_CSS, corpo))

    html_path = os.path.join(AQUI, "_tmp_frente_en.html")
    os.makedirs(SAIDA, exist_ok=True)
    pdf_path = os.path.join(SAIDA, "Step 1 - Start Here.pdf")
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
                    "http://127.0.0.1:%d/%s" % (PORTA, "_tmp_frente_en.html")],
                   capture_output=True)
    ok = os.path.exists(pdf_path)
    print("PDF:", pdf_path, "OK" if ok else "FAILED",
          "(%.1f MB)" % (os.path.getsize(pdf_path) / 1e6) if ok else "")
    if ok and os.path.exists(html_path):
        os.remove(html_path)
    return ok


if __name__ == "__main__":
    build()
