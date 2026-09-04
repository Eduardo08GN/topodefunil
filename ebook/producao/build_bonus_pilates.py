# -*- coding: utf-8 -*-
"""Monta o BÔNUS 2 — PILATES SECA BARRIGA EM CASA num PDF:
  1) abertura (o que é, por que ajuda, aviso honesto, como usar, plano da semana)
  2) os 12 exercícios (fotos 159-170), card grande no visual do livro.
Uso: python build_bonus_pilates.py
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
import exercicios_pilates as pil

PORTA = 8132
AQUI = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(AQUI, "fotos")

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
  <span class="veg-badge">Bônus 2</span>
  <h1>Pilates Seca Barriga em Casa</h1>
  <div class="veg-rule"></div>
  <p class="veg-lead">O Pilates é uma ginástica de movimentos lentos e controlados que
    fortalece principalmente o <b>centro do corpo</b> — a região da barriga e das costas.
    Sem aparelhos, sem impacto e sem sair de casa, ele é perfeito para acompanhar a dieta
    e acelerar os resultados. Você só precisa de um tapete ou uma toalha no chão.</p>

  <div class="veg-box">
    <h2>Por que ajuda a secar a barriga</h2>
    <ul>
      <li>Fortalece o <b>músculo profundo do abdômen</b>, que funciona como uma cinta natural e segura a barriga para dentro.</li>
      <li>Melhora a <b>postura</b> — e ficar mais ereto já deixa a barriga visivelmente mais reta.</li>
      <li>Define a <b>cintura</b> ao trabalhar os músculos laterais.</li>
      <li>É de <b>baixo impacto</b>: pega leve nas articulações, ideal para todas as idades.</li>
    </ul>
  </div>

  <div class="honest">
    <span class="hlabel">Uma verdade importante</span>
    <p>Nenhum exercício queima gordura só na barriga — isso não existe. A gordura sai
      do corpo inteiro, e quem comanda essa perda é a <b>alimentação</b>. O Pilates
      fortalece, define e melhora a postura; junto com as receitas do livro, é a
      combinação que faz a barriga afinar de verdade. Consistência é tudo.</p>
  </div>

  <div class="veg-how">
    <b>Como usar:</b> faça de <b>3 a 4 vezes por semana</b>, de 15 a 20 minutos.
    Use roupa confortável, treine de estômago vazio ou pelo menos 1 hora depois de comer,
    e <b>respire sempre</b> (nunca prenda o ar). Comece pelas variações mais fáceis
    indicadas em cada exercício e evolua com o tempo. Se sentir dor aguda, pare.
  </div>
</div>

<div class="ex-head">
  <div class="kicker">Bônus 2 · Pilates Seca Barriga</div>
  <h2>Os 12 exercícios</h2>
  <p>Faça na ordem, respeitando a respiração e o seu limite. Cada exercício traz o foco,
    o número de repetições, o passo a passo e uma variação mais fácil quando existe.</p>

  <div class="plan">
    <h2>Plano da semana</h2>
    <p>Escolha 3 a 4 dias (por exemplo <b>segunda, quarta e sexta</b>) e faça a sequência
      completa dos 12 exercícios na ordem em que aparecem.</p>
    <div class="seq">A ordem já está pensada: começa pelo <b>aquecimento</b> (1 e 2),
      passa pelos exercícios de <b>abdômen</b> (3 a 10), fortalece as <b>costas</b> (11)
      e termina no <b>alongamento</b> (12). Nunca pule o aquecimento nem o alongamento.</div>
  </div>
  %s
</div>
""" % _ex_list_html(exs))


def render_exercicio(e, num):
    n3 = "%03d" % num
    foto = ('<b>FOTO %s</b><small>espaço quadrado reservado<br>'
            '(gerar pelo prompt e nomear "%s")</small>' % (n3, n3))
    if os.path.isdir(IMG):
        for ext in (".jpg", ".jpeg", ".png", ".webp"):
            if os.path.isfile(os.path.join(IMG, n3 + ext)):
                foto = '<img src="fotos/%s" alt="">' % (n3 + ext)
                break
    passos = "".join("<li>%s</li>" % _html.escape(x) for x in e["passos"])
    return """<div class="recipe">
  <div class="top"><span class="tag">Pilates</span><span class="num">Bônus · Pilates</span></div>
  <h1>%s</h1>
  <p class="hook">%s</p>
  <div class="grid">
    <div class="photo">%s</div>
    <div>
      <div class="stats">
        <div class="stat"><div class="v">%s</div><div class="l">Nível</div></div>
        <div class="stat"><div class="v">%s</div><div class="l">Séries</div></div>
        <div class="stat"><div class="v">%s</div><div class="l">Tempo</div></div>
      </div>
      <h2>Foco</h2>
      <p class="foco">%s</p>
    </div>
  </div>
  <div class="steps"><h2>Como fazer</h2><ol>%s</ol></div>
  <div class="resp"><b>Respiração</b><p>%s</p></div>
  <div class="tip"><b>Dica</b><p>%s</p></div>
</div>""" % (_html.escape(e["nome"]), _html.escape(e["hook"]), foto,
            _html.escape(e["nivel"]), _html.escape(e["series"]), _html.escape(e["tempo"]),
            _html.escape(e["foco"]), passos, _html.escape(e["respiracao"]),
            _html.escape(e["dica"]))


def build():
    importlib.reload(pil)
    corpo = intro_html(pil.EXERCICIOS)
    for i, e in enumerate(pil.EXERCICIOS):
        corpo += render_exercicio(e, 159 + i)

    doc = ("""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">
<title>Bônus 2 — Pilates Seca Barriga em Casa</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700;800;900&display=swap" rel="stylesheet">
<style>%s
%s</style></head><body>%s</body></html>""" % (motor.ESTILO, EXTRA_CSS, corpo))

    html_path = os.path.join(AQUI, "_tmp_bonus2.html")
    pdf_path = os.path.join(AQUI, "Passo 8 - Bônus 2 - Pilates Seca Barriga em Casa.pdf")
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
                    "http://127.0.0.1:%d/%s" % (PORTA, "_tmp_bonus2.html")],
                   capture_output=True)
    ok = os.path.exists(pdf_path)
    print("PDF:", pdf_path, "OK" if ok else "FALHOU",
          "(%.1f MB)" % (os.path.getsize(pdf_path) / 1e6) if ok else "")
    if ok and os.path.exists(html_path):
        os.remove(html_path)
    return ok


if __name__ == "__main__":
    build()
