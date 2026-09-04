# -*- coding: utf-8 -*-
"""Builds BONUS 2 — BELLY-SLIMMING PILATES AT HOME (English) into a PDF:
  1) opening (what it is, why it helps, honest note, how to use, weekly plan)
  2) the 12 exercises (photos 159-170), big card in the book's look.
Usage: python build_bonus_pilates_en.py
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
import exercicios_pilates_en as pil

PORTA = 8135
AQUI = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(AQUI, "fotos")
SAIDA = os.path.join(AQUI, "..", "Entregavel em ENG")

EXTRA_CSS = """
.veg-cover{page-break-after:always;padding-top:24px}
.veg-badge{display:inline-block;background:var(--green);color:#fff;font-size:16px;font-weight:900;
letter-spacing:.14em;text-transform:uppercase;padding:9px 20px;border-radius:999px}
.veg-cover h1{font-size:56px;font-weight:900;letter-spacing:-.03em;margin:18px 0 18px;line-height:1.02;color:var(--green)}
.veg-cover .veg-rule{width:70px;height:5px;background:var(--gold);border-radius:3px;margin:0 0 20px}
.veg-lead{font-size:16px;color:var(--soft);line-height:1.6;max-width:96%}
.veg-box{margin-top:22px;background:var(--green-tint);border-radius:16px;padding:20px 24px;break-inside:avoid}
.veg-box h2{font-size:15px;color:var(--green);text-transform:uppercase;letter-spacing:.06em;margin-bottom:10px}
.veg-box ul{list-style:none;margin:0}
.veg-box li{font-size:15px;padding:5px 0 5px 20px;position:relative;line-height:1.5}
.veg-box li::before{content:"";position:absolute;left:0;top:11px;width:7px;height:7px;border-radius:50%;background:var(--green)}
.honest{margin-top:20px;background:var(--gold-tint);border-left:4px solid var(--gold);border-radius:0 12px 12px 0;
padding:16px 20px;break-inside:avoid}
.honest .hlabel{color:#8a6a1a;font-size:12.5px;font-weight:800;text-transform:uppercase;letter-spacing:.06em;display:block;margin-bottom:6px}
.honest p{font-size:14.5px;line-height:1.6;color:var(--ink)}
.honest p b{color:#8a6a1a;font-weight:800}
.veg-how{margin-top:22px;font-size:15px;line-height:1.65}
.veg-how b{color:var(--green)}
.plan{margin-top:22px;background:var(--cream);border-radius:14px;padding:18px 22px;break-inside:avoid}
.plan h2{font-size:15px;color:var(--green);text-transform:uppercase;letter-spacing:.06em;margin-bottom:10px}
.plan p{font-size:15px;line-height:1.65}
.plan .seq{margin-top:10px;font-size:14.5px;color:var(--soft);line-height:1.6}
.ex-head{page-break-before:always;padding-top:6px}
.ex-head .kicker{font-size:13px;font-weight:800;letter-spacing:.16em;text-transform:uppercase;color:var(--gold)}
.ex-head h2{font-size:30px;font-weight:900;letter-spacing:-.01em;margin:6px 0 8px;line-height:1.1}
.ex-head p{font-size:15px;color:var(--soft);line-height:1.6;max-width:96%}
.ex-list{margin-top:22px}
.ex-list table{width:100%;border-collapse:collapse}
.ex-list td{padding:9px 4px;font-size:15px;border-bottom:1px solid var(--line);line-height:1.4}
.ex-list td.n{width:42px;color:var(--green);font-weight:800}
.ex-list td.s{text-align:right;color:var(--soft);font-size:13px;white-space:nowrap;width:170px}
.foco{margin-top:2px;font-size:15px;color:var(--ink);line-height:1.5}
.resp{margin-top:22px;background:var(--green-tint);border-left:4px solid var(--green);
border-radius:0 10px 10px 0;padding:14px 18px;break-inside:avoid}
.resp b{color:var(--green);font-size:12.5px;text-transform:uppercase;letter-spacing:.06em;display:block;margin-bottom:5px}
.resp p{font-size:15px;line-height:1.55}
"""


def _ex_list_html(exs):
    linhas = ""
    for i, e in enumerate(exs):
        linhas += ('<tr><td class="n">%d</td><td>%s</td><td class="s">%s</td></tr>'
                   % (i + 1, _html.escape(e["nome"]), _html.escape(e["series"])))
    return '<div class="ex-list"><table>%s</table></div>' % linhas


def intro_html(exs):
    return ("""
<div class="veg-cover">
  <span class="veg-badge">Bonus 2</span>
  <h1>Belly-Slimming Pilates at Home</h1>
  <div class="veg-rule"></div>
  <p class="veg-lead">Pilates is a workout of slow, controlled movements that mainly
    strengthens the <b>center of the body</b> — the belly and back area. With no
    equipment, no impact and without leaving home, it is perfect to go with the diet
    and speed up results. All you need is a mat or a towel on the floor.</p>

  <div class="veg-box">
    <h2>Why it helps flatten the belly</h2>
    <ul>
      <li>It strengthens the <b>deep abdominal muscle</b>, which works like a natural corset and holds the belly in.</li>
      <li>It improves <b>posture</b> — and standing taller already makes the belly look visibly flatter.</li>
      <li>It defines the <b>waist</b> by working the side muscles.</li>
      <li>It is <b>low impact</b>: gentle on the joints, ideal for all ages.</li>
    </ul>
  </div>

  <div class="honest">
    <span class="hlabel">An important truth</span>
    <p>No exercise burns fat only on the belly — that does not exist. Fat leaves the
      whole body, and what drives that loss is your <b>diet</b>. Pilates strengthens,
      defines and improves posture; together with the book's recipes, it is the
      combination that truly slims the belly. Consistency is everything.</p>
  </div>

  <div class="veg-how">
    <b>How to use it:</b> do it <b>3 to 4 times a week</b>, 15 to 20 minutes. Wear
    comfortable clothes, train on an empty stomach or at least 1 hour after eating,
    and <b>always breathe</b> (never hold your breath). Start with the easier
    variations noted in each exercise and progress over time. If you feel sharp pain,
    stop.
  </div>
</div>

<div class="ex-head">
  <div class="kicker">Bonus 2 · Belly-Slimming Pilates</div>
  <h2>The 12 exercises</h2>
  <p>Do them in order, respecting your breathing and your limit. Each exercise has the
    focus, the number of reps, the step by step and an easier variation when there is one.</p>

  <div class="plan">
    <h2>Weekly plan</h2>
    <p>Choose 3 to 4 days (for example <b>Monday, Wednesday and Friday</b>) and do the
      full sequence of the 12 exercises in the order they appear.</p>
    <div class="seq">The order is already thought out: it starts with the <b>warm-up</b>
      (1 and 2), goes through the <b>belly</b> exercises (3 to 10), strengthens the
      <b>back</b> (11) and ends with the <b>stretch</b> (12). Never skip the warm-up
      or the stretch.</div>
  </div>
  %s
</div>
""" % _ex_list_html(exs))


def render_exercicio(e, num):
    n3 = "%03d" % num
    foto = ('<b>PHOTO %s</b><small>square space reserved<br>'
            '(generate from the prompt and name it "%s")</small>' % (n3, n3))
    if os.path.isdir(IMG):
        for ext in (".jpg", ".jpeg", ".png", ".webp"):
            if os.path.isfile(os.path.join(IMG, n3 + ext)):
                foto = '<img src="fotos/%s" alt="">' % (n3 + ext)
                break
    passos = "".join("<li>%s</li>" % _html.escape(x) for x in e["passos"])
    return """<div class="recipe">
  <div class="top"><span class="tag">Pilates</span><span class="num">Bonus · Pilates</span></div>
  <h1>%s</h1>
  <p class="hook">%s</p>
  <div class="grid">
    <div class="photo">%s</div>
    <div>
      <div class="stats">
        <div class="stat"><div class="v">%s</div><div class="l">Level</div></div>
        <div class="stat"><div class="v">%s</div><div class="l">Sets</div></div>
        <div class="stat"><div class="v">%s</div><div class="l">Time</div></div>
      </div>
      <h2>Focus</h2>
      <p class="foco">%s</p>
    </div>
  </div>
  <div class="steps"><h2>How to do it</h2><ol>%s</ol></div>
  <div class="resp"><b>Breathing</b><p>%s</p></div>
  <div class="tip"><b>Tip</b><p>%s</p></div>
</div>""" % (_html.escape(e["nome"]), _html.escape(e["hook"]), foto,
            _html.escape(e["nivel"]), _html.escape(e["series"]), _html.escape(e["tempo"]),
            _html.escape(e["foco"]), passos, _html.escape(e["respiracao"]),
            _html.escape(e["dica"]))


def build():
    importlib.reload(pil)
    corpo = intro_html(pil.EXERCICIOS)
    for i, e in enumerate(pil.EXERCICIOS):
        corpo += render_exercicio(e, 159 + i)

    doc = ("""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<title>Bonus 2 — Belly-Slimming Pilates at Home</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700;800;900&display=swap" rel="stylesheet">
<style>%s
%s</style></head><body>%s</body></html>""" % (motor.ESTILO, EXTRA_CSS, corpo))

    html_path = os.path.join(AQUI, "_tmp_bonus2_en.html")
    os.makedirs(SAIDA, exist_ok=True)
    pdf_path = os.path.join(SAIDA, "Step 8 - Bonus 2 - Belly-Slimming Pilates at Home.pdf")
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
                    "http://127.0.0.1:%d/%s" % (PORTA, "_tmp_bonus2_en.html")],
                   capture_output=True)
    ok = os.path.exists(pdf_path)
    print("PDF:", pdf_path, "OK" if ok else "FAILED",
          "(%.1f MB)" % (os.path.getsize(pdf_path) / 1e6) if ok else "")
    if ok and os.path.exists(html_path):
        os.remove(html_path)
    return ok


if __name__ == "__main__":
    build()
