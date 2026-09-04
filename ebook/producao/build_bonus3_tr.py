# -*- coding: utf-8 -*-
"""BÔNUS 3 — 50 HÁBITOS E EXERCÍCIOS. TRADUZIDO.
Uso: python build_bonus3_tr.py <de|fr>
"""
import os
import sys
import time
import http.server
import socketserver
import threading
import importlib
import html as _html
import subprocess

import motor_receitas as motor

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

PORTA = 8132
AQUI = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(AQUI, "fotos")

TEXTOS = {
"de": {
 "arquivo": "Schritt 9 - Bonus 3 - 50 Gewohnheiten und Uebungen.pdf",
 "titulo": "Bonus 3 — 50 Gewohnheiten und Übungen",
 "badge": "Bonus 3", "h1": "50 Gewohnheiten und Übungen",
 "pill_ex": "Übungen", "pill_hab": "Gewohnheiten",
 "lbl_plano": "Steigerung:", "lbl_dica": "Tipp:",
 "foto_ph": "quadratischer Platz<br>reserviert",
 "lead": """Die Ernährung macht den größten Teil der Arbeit, aber es ist die
    Bewegung, die <b>das Verbrennen beschleunigt</b>, den Körper formt und das Ergebnis
    halten lässt. Hier findest du <b>30 Übungen</b>, die wirklich beim Abnehmen helfen —
    auf der Straße, auf dem Laufband, im Fitnessstudio oder zu Hause, jede mit einem
    <b>Plan zum Steigern</b> — und <b>20 Gewohnheiten</b>, die zusammen den Unterschied
    machen.""",
 "how": """<b>So nutzt du das:</b> Wähle eine <b>Ausdauerübung</b> (Gehen, Rad, Schwimmen…)
    und mach sie <b>3- bis 5-mal pro Woche</b>, dem Steigerungsplan folgend. Nimm
    <b>2 Tage Krafttraining</b> dazu (im Studio oder zu Hause), um den Stoffwechsel
    anzuregen. Übernimm die Gewohnheiten nach und nach — es ist die Summe aus allem,
    die wirklich schlanker macht.""",
},
"fr": {
 "arquivo": "Etape 9 - Bonus 3 - 50 habitudes et exercices.pdf",
 "titulo": "Bonus 3 — 50 habitudes et exercices",
 "badge": "Bonus 3", "h1": "50 habitudes et exercices",
 "pill_ex": "Exercices", "pill_hab": "Habitudes",
 "lbl_plano": "Progression :", "lbl_dica": "Astuce :",
 "foto_ph": "emplacement carré<br>réservé",
 "lead": """L'alimentation fait la plus grande partie du travail, mais c'est
    l'exercice qui <b>accélère le brûlage</b>, dessine le corps et fait durer le
    résultat. Tu trouveras ici <b>30 exercices</b> qui font vraiment maigrir —
    dans la rue, sur le tapis, en salle ou à la maison, chacun avec un
    <b>plan de progression</b> — et <b>20 habitudes</b> qui, additionnées, font
    la différence.""",
 "how": """<b>Comment l'utiliser :</b> choisis un exercice de <b>cardio</b> (marche,
    vélo, natation…) et fais-le <b>3 à 5 fois par semaine</b>, en suivant la
    progression. Ajoute <b>2 jours de renforcement</b> (musculation ou séance à la
    maison) pour accélérer le métabolisme. Adopte les habitudes petit à petit — c'est
    la somme de tout qui affine vraiment.""",
},
}

EXTRA_CSS = """
.b3cover{page-break-after:always;padding-top:24px}
.veg-badge{display:inline-block;background:var(--green);color:#fff;font-size:16px;font-weight:900;
letter-spacing:.14em;text-transform:uppercase;padding:9px 20px;border-radius:999px}
.b3cover h1{font-size:52px;font-weight:900;letter-spacing:-.03em;margin:18px 0 18px;line-height:1.04;color:var(--green)}
.b3cover .veg-rule{width:70px;height:5px;background:var(--gold);border-radius:3px;margin:0 0 20px}
.b3cover .lead{font-size:16px;color:var(--soft);line-height:1.6;max-width:97%}
.b3cover .how{margin-top:20px;font-size:15px;line-height:1.65}
.b3cover .how b{color:var(--green)}
.exsec{margin-top:6px;page-break-before:always}
.exsec-head{margin-bottom:6px;break-after:avoid;page-break-after:avoid}
.exsec-pill{display:inline-block;background:var(--green);color:#fff;font-size:13px;font-weight:800;
text-transform:uppercase;letter-spacing:.09em;padding:8px 18px;border-radius:999px}
.exsec-head h2{font-size:24px;font-weight:900;letter-spacing:-.01em;margin:10px 0 4px;line-height:1.15}
.exsec-head .tintro{font-size:14.5px;color:var(--soft);line-height:1.5;max-width:97%}
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


def _img_html(T, num, cls):
    n3 = "%03d" % num
    for ext in (".jpg", ".jpeg", ".png", ".webp"):
        if os.path.isfile(os.path.join(IMG, n3 + ext)):
            return '<div class="%s"><img src="fotos/%s" alt=""></div>' % (cls, n3 + ext)
    return ('<div class="%s"><b>FOTO %s</b><small>%s</small></div>'
            % (cls, n3, T["foto_ph"]))


def cover_html(T):
    return """
<div class="b3cover">
  <span class="veg-badge">%s</span>
  <h1>%s</h1>
  <div class="veg-rule"></div>
  <p class="lead">%s</p>
  <div class="how">%s</div>
</div>
""" % (_html.escape(T["badge"]), _html.escape(T["h1"]), T["lead"], T["how"])


def exsec_html(T, t, contador):
    cards = ""
    for e in t["itens"]:
        contador[0] += 1
        cards += ("""<div class="excard">
  %s
  <div>
    <div class="exhead"><div class="exnum">%d</div><h3>%s</h3></div>
    <div class="meta">%s<span class="g">%s</span></div>
    <div class="plano"><span class="lbl">%s</span> %s</div>
    <div class="dica"><span class="lbl">%s</span> %s</div>
  </div>
</div>""" % (_img_html(T, e["img"], "excard-img"), contador[0], _html.escape(e["nome"]),
            _html.escape(e["onde"]), _html.escape(e["gasto"]),
            _html.escape(T["lbl_plano"]), _html.escape(e["plano"]),
            _html.escape(T["lbl_dica"]), _html.escape(e["dica"])))
    return ("""<div class="exsec">
  <div class="exsec-head"><span class="exsec-pill">%s</span><h2>%s</h2>
    <p class="tintro">%s</p></div>
  %s
</div>""" % (_html.escape(T["pill_ex"]), _html.escape(t["tema"]),
            _html.escape(t["intro"]), cards))


def hsec_html(T, t, contador):
    itens = ""
    for h in t["itens"]:
        contador[0] += 1
        itens += ('<div class="habitem"><div class="hn">%d</div>'
                  '<p><b>%s.</b> %s</p></div>'
                  % (contador[0], _html.escape(h["titulo"]), _html.escape(h["desc"])))
    return ("""<div class="hsec">
  <div class="hsec-head">%s
    <div><span class="hsec-pill">%s</span><h2>%s</h2>
      <p class="tintro">%s</p></div>
  </div>
  %s
</div>""" % (_img_html(T, t["img"], "hsec-img"), _html.escape(T["pill_hab"]),
            _html.escape(t["tema"]), _html.escape(t["intro"]), itens))


def build(lang):
    T = TEXTOS[lang]
    eh = importlib.import_module("exercicios_habitos_%s" % lang)
    importlib.reload(eh)
    contador = [0]
    corpo = cover_html(T)
    for t in eh.TEMAS:
        corpo += (exsec_html(T, t, contador) if t["tipo"] == "exercicio"
                  else hsec_html(T, t, contador))

    doc = ("""<!DOCTYPE html><html lang="%s"><head><meta charset="utf-8">
<title>%s</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700;800;900&display=swap" rel="stylesheet">
<style>%s%s
%s</style></head><body>%s</body></html>"""
           % (motor.I18N[lang]["html_lang"], _html.escape(T["titulo"]),
              motor.ESTILO, motor.I18N[lang]["css"], EXTRA_CSS, corpo))

    html_path = os.path.join(AQUI, "_tmp_bonus3_%s.html" % lang)
    saida = os.path.join(AQUI, "Entregavel em %s" % lang.upper())
    os.makedirs(saida, exist_ok=True)
    pdf_path = os.path.join(saida, T["arquivo"])
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
                    "http://127.0.0.1:%d/_tmp_bonus3_%s.html" % (PORTA, lang)],
                   capture_output=True)
    ok = os.path.exists(pdf_path)
    print("Total de itens numerados:", contador[0])
    print("PDF:", pdf_path, "OK" if ok else "FALHOU",
          "(%.1f MB)" % (os.path.getsize(pdf_path) / 1e6) if ok else "")
    if ok and os.path.exists(html_path):
        os.remove(html_path)
    return ok


if __name__ == "__main__":
    sys.exit(0 if build(sys.argv[1] if len(sys.argv) > 1 else "de") else 1)
