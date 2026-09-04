# -*- coding: utf-8 -*-
"""BÔNUS 1 — DIETA VEGETARIANA. TRADUZIDO.
Uso: python build_bonus_veg_tr.py <de|fr>

⭐ A lista de receitas reaproveitadas (`REUSO`) guarda só os NÚMEROS e busca o
nome no próprio módulo de dados do idioma. Nome copiado é nome que diverge no
dia em que a receita for renomeada, e dentro de um PDF isso passa despercebido.
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

# (modulo base, numero da PRIMEIRA receita daquele modulo, numeros reaproveitados)
REUSO = [("receitas_cafe", 1, [1, 3, 7, 15]),
         ("receitas_sobremesa", 101, [102, 106, 110, 116]),
         ("receitas_suco", 121, [121, 131, 133, 135])]

TEXTOS = {
"de": {
 "arquivo": "Schritt 7 - Bonus 1 - Vegetarische Ernaehrung.pdf",
 "titulo": "Bonus 1 — Vegetarische Ernährung",
 "badge": "Bonus 1", "h1": "Vegetarische Ernährung",
 "rezept": "Rezept",
 "cats": ["Frühstück", "Desserts", "Smoothies und Säfte"],
 "lead": """Auf Fleisch zu verzichten heißt nicht, auf Eiweiß, Geschmack
    oder Sättigung zu verzichten. Eine gut zusammengestellte vegetarische Ernährung
    ist leicht, günstig und reich an Ballaststoffen — und sie kann das Abnehmen
    beschleunigen, solange du bei jeder Mahlzeit für eine gute Eiweißquelle sorgst.
    Hier hast du <b>20 Möglichkeiten</b>, gleichmäßig verteilt auf Frühstück,
    Mittagessen, Abendessen, Dessert und Getränke.""",
 "box_h2": "Woher das Eiweiß kommt",
 "box_itens": ["<b>Eier</b> — vollwertiges Eiweiß, das sehr satt macht.",
               "<b>Milchprodukte</b> — Naturjoghurt, heller Käse, Ricotta, Hüttenkäse.",
               "<b>Hülsenfrüchte</b> — Bohnen, Linsen, Kichererbsen und Erbsen.",
               "<b>Tofu</b> — aus Sojabohnen, voller Eiweiß und mit wenig Fett.",
               "<b>Nüsse und Kerne</b> — Nüsse, Walnüsse und Erdnussmus (in Maßen)."],
 "box_compl": """Ein goldener Tipp: Kombiniere eine <b>Hülsenfrucht</b> mit
      einem <b>Getreide</b> in derselben Mahlzeit (Reis mit Bohnen, Kichererbsen
      mit Reis) und du erhältst ein Eiweiß, das so vollständig ist wie das aus
      Fleisch.""",
 "how": """<b>So nutzt du das:</b> Stell dir deinen Tag zusammen, indem du aus dieser
    Liste 1 Frühstück, 1 Mittagessen, 1 Abendessen, 1 Dessert und 1 Getränk
    wählst. Die Möglichkeiten für Frühstück, Dessert und Getränk stehen schon in
    deinem Buch — such einfach nach der Nummer des Rezepts. Die vegetarischen
    Mittag- und Abendessen sind die <b>4 + 4 neuen Rezepte</b>, die gleich
    danach kommen.""",
 "reuse_h2": "Aus dem Buch selbst",
 "reuse_sub": """Diese Rezepte, die du schon hast, sind von Natur aus vegetarisch —
      nutze sie, so viel du magst, innerhalb dieser Ernährung.""",
 "kicker": "Bonus 1 · Vegetarische Ernährung",
 "head_h2": "Vegetarische Mittag- und Abendessen",
 "head_p": """Die folgenden Rezepte sind neu und kommen ohne Fleisch und ohne Fisch aus — das
    Eiweiß stammt aus Hülsenfrüchten, Tofu, Eiern und Käse. Jedes bringt die Tabelle
    zum Anpassen nach Profil mit, genau wie die Rezepte im Buch.""",
},
"fr": {
 "arquivo": "Etape 7 - Bonus 1 - Alimentation vegetarienne.pdf",
 "titulo": "Bonus 1 — Alimentation végétarienne",
 "badge": "Bonus 1", "h1": "Alimentation végétarienne",
 "rezept": "Recette",
 "cats": ["Petits-déjeuners", "Desserts", "Smoothies et jus"],
 "lead": """Supprimer la viande ne veut pas dire renoncer aux protéines, au goût
    ni à la satiété. Une alimentation végétarienne bien construite est légère,
    économique et pleine de fibres — et elle peut accélérer l'amincissement, à
    condition d'assurer une bonne source de protéines à chaque repas.
    Tu as ici <b>20 options</b>, réparties également entre petit-déjeuner,
    déjeuner, dîner, dessert et boissons.""",
 "box_h2": "D'où viennent les protéines",
 "box_itens": ["<b>Les œufs</b> — une protéine complète et très rassasiante.",
               "<b>Les produits laitiers</b> — yaourt nature, fromage blanc, ricotta.",
               "<b>Les légumineuses</b> — haricots, lentilles, pois chiches et petits pois.",
               "<b>Le tofu</b> — fait de soja, plein de protéines et avec peu de graisses.",
               "<b>Les fruits à coque</b> — noix, amandes et beurre de cacahuète (avec modération)."],
 "box_compl": """Un conseil en or : associe une <b>légumineuse</b> à une
      <b>céréale</b> dans le même repas (riz avec haricots, pois chiches avec riz)
      et tu obtiens une protéine aussi complète que celle de la viande.""",
 "how": """<b>Comment l'utiliser :</b> monte ta journée en choisissant dans cette
    liste 1 petit-déjeuner, 1 déjeuner, 1 dîner, 1 dessert et 1 boisson. Les
    options de petit-déjeuner, de dessert et de boisson sont déjà dans ton livre —
    il suffit de chercher le numéro de la recette. Les déjeuners et dîners
    végétariens sont les <b>4 + 4 nouvelles recettes</b> qui viennent juste
    après.""",
 "reuse_h2": "Tirées du livre lui-même",
 "reuse_sub": """Ces recettes que tu as déjà sont naturellement végétariennes —
      utilise-les à volonté dans cette alimentation.""",
 "kicker": "Bonus 1 · Alimentation végétarienne",
 "head_h2": "Déjeuners et dîners végétariens",
 "head_p": """Les recettes qui suivent sont nouvelles et faites sans viande ni poisson — les
    protéines viennent des légumineuses, du tofu, des œufs et des fromages. Chacune
    apporte le tableau d'ajustement par profil, comme les recettes du livre.""",
},
"en": {
 "arquivo": "Step 7 - Bonus 1 - Vegetarian Diet.pdf",
 "titulo": "Bonus 1 — Vegetarian Diet",
 "badge": "Bonus 1", "h1": "Vegetarian Diet",
 "rezept": "Recipe",
 "cats": ["Breakfasts", "Desserts", "Smoothies and juices"],
 "lead": """Cutting out meat does not mean giving up protein, flavor
    or feeling full. A well-built vegetarian diet is light, cheap and full of
    fiber — and it can speed up your weight loss, as long as you make sure you
    have a good protein source at every meal.
    Here you have <b>20 options</b>, spread evenly between breakfast,
    lunch, dinner, dessert and drinks.""",
 "box_h2": "Where the protein comes from",
 "box_itens": ["<b>Eggs</b> — a complete protein that is very filling.",
               "<b>Dairy</b> — plain yogurt, white cheese, ricotta, cottage cheese.",
               "<b>Legumes</b> — beans, lentils, chickpeas and peas.",
               "<b>Tofu</b> — made from soy, full of protein and low in fat.",
               "<b>Nuts and seeds</b> — walnuts, almonds and peanut butter (in moderation)."],
 "box_compl": """A golden tip: pair a <b>legume</b> with a
      <b>grain</b> in the same meal (rice with beans, chickpeas with rice)
      and you get a protein as complete as the one from meat.""",
 "how": """<b>How to use this:</b> build your day by picking from this
    list 1 breakfast, 1 lunch, 1 dinner, 1 dessert and 1 drink. The
    breakfast, dessert and drink options are already in your book —
    just look for the recipe number. The vegetarian lunches and dinners
    are the <b>4 + 4 new recipes</b> that come right
    after.""",
 "reuse_h2": "From the book itself",
 "reuse_sub": """These recipes you already have are naturally vegetarian —
      use them as much as you want within this diet.""",
 "kicker": "Bonus 1 · Vegetarian Diet",
 "head_h2": "Vegetarian lunches and dinners",
 "head_p": """The recipes that follow are new and made with no meat and no fish — the
    protein comes from legumes, tofu, eggs and cheese. Each one
    brings the adjustment table by profile, like the recipes in the book.""",
},
}

INTRO_CSS = """
.veg-cover{page-break-after:always;padding-top:24px}
.kicker{font-size:13px;font-weight:800;letter-spacing:.18em;text-transform:uppercase;color:var(--gold)}
.veg-badge{display:inline-block;background:var(--green);color:#fff;font-size:16px;font-weight:900;
letter-spacing:.14em;text-transform:uppercase;padding:9px 20px;border-radius:999px}
.veg-cover h1{font-size:56px;font-weight:900;letter-spacing:-.03em;margin:18px 0 20px;line-height:1.04;color:var(--green)}
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
.reuse-cat td.n{width:130px;color:var(--green);font-weight:800;white-space:nowrap}
.veg-recipes-head{page-break-before:always;padding-top:6px}
.veg-recipes-head .kicker{color:var(--gold)}
.veg-recipes-head h2{font-size:30px;font-weight:900;letter-spacing:-.01em;margin:6px 0 8px;line-height:1.1}
.veg-recipes-head p{font-size:15px;color:var(--soft);line-height:1.6;max-width:96%;margin-bottom:6px}
"""


def _reuse_html(lang, T):
    blocos = ""
    for (base, primeiro, nums), cat in zip(REUSO, T["cats"]):
        mod = importlib.import_module("%s_%s" % (base, lang))
        importlib.reload(mod)
        linhas = "".join(
            '<tr><td class="n">%s %03d</td><td>%s</td></tr>'
            % (_html.escape(T["rezept"]), n,
               _html.escape(mod.RECEITAS[n - primeiro]["nome"])) for n in nums)
        blocos += ('<div class="reuse-cat"><h3>%s</h3><table>%s</table></div>'
                   % (_html.escape(cat), linhas))
    return blocos


def intro_html(lang, T):
    itens = "".join("<li>%s</li>" % x for x in T["box_itens"])
    return """
<div class="veg-cover">
  <span class="veg-badge">%s</span>
  <h1>%s</h1>
  <div class="veg-rule"></div>
  <p class="veg-lead">%s</p>

  <div class="veg-box">
    <h2>%s</h2>
    <ul>%s</ul>
    <div class="compl">%s</div>
  </div>

  <div class="veg-how">%s</div>

  <div class="reuse">
    <h2>%s</h2>
    <p class="sub">%s</p>
    %s
  </div>
</div>

<div class="veg-recipes-head">
  <div class="kicker">%s</div>
  <h2>%s</h2>
  <p>%s</p>
</div>
""" % (_html.escape(T["badge"]), _html.escape(T["h1"]), T["lead"],
       _html.escape(T["box_h2"]), itens, T["box_compl"], T["how"],
       _html.escape(T["reuse_h2"]), T["reuse_sub"], _reuse_html(lang, T),
       _html.escape(T["kicker"]), _html.escape(T["head_h2"]), T["head_p"])


def build(lang):
    T = TEXTOS[lang]
    veg = importlib.import_module("receitas_bonus_veg_%s" % lang)
    importlib.reload(veg)
    corpo = intro_html(lang, T)
    for i, r in enumerate(veg.ALMOCOS):
        corpo += motor.render_receita(r, "almoco", 151 + i, IMG, lang=lang)
    for i, r in enumerate(veg.JANTARES):
        corpo += motor.render_receita(r, "jantar", 155 + i, IMG, lang=lang)

    html = ("""<!DOCTYPE html><html lang="%s"><head><meta charset="utf-8">
<title>%s</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700;800;900&display=swap" rel="stylesheet">
<style>%s%s
%s</style></head><body>%s</body></html>"""
            % (motor.I18N[lang]["html_lang"], _html.escape(T["titulo"]),
               motor.ESTILO, motor.I18N[lang]["css"], INTRO_CSS, corpo))

    html_path = os.path.join(AQUI, "_tmp_bonus1_%s.html" % lang)
    saida = os.path.join(AQUI, "..", "Entregavel em %s" % lang.upper())
    os.makedirs(saida, exist_ok=True)
    pdf_path = os.path.join(saida, T["arquivo"])
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)

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
                    "http://127.0.0.1:%d/_tmp_bonus1_%s.html" % (PORTA, lang)],
                   capture_output=True)
    ok = os.path.exists(pdf_path)
    print("PDF:", pdf_path, "OK" if ok else "FALHOU",
          "(%.1f MB)" % (os.path.getsize(pdf_path) / 1e6) if ok else "")
    if ok and os.path.exists(html_path):
        os.remove(html_path)
    return ok


if __name__ == "__main__":
    sys.exit(0 if build(sys.argv[1] if len(sys.argv) > 1 else "de") else 1)
