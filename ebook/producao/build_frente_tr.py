# -*- coding: utf-8 -*-
"""FRENTE DO LIVRO — "Fang hier an" / "Commence ici" (passo 1). TRADUZIDO.
Uso: python build_frente_tr.py <de|fr>

⛔ UM builder para todos os idiomas: a prosa mora em `TEXTOS`, a estrutura
HTML é uma só. Idioma novo entra como chave, nunca como arquivo novo.
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

# ── prosa por idioma ────────────────────────────────────────────────────
TEXTOS = {
"de": {
 "arquivo": "Schritt 1 - Fang hier an.pdf",
 "titulo": "Fang hier an",
 "badge": "Fang hier an",
 "cover_h1": "Willkommen!",
 "cover_lead": """Schön, dass du hier bist. Du hast gerade den ersten Schritt gemacht,
    um abzunehmen, indem du gut isst — ohne zu hungern und ohne verrückte Diäten. Dieses
    Material ist ein <b>vollständiges Programm</b>: 150 Fitness-Rezepte, ein Plan für
    30 Tage und drei Boni mit Übungen und Gewohnheiten. Bevor du zu kochen beginnst,
    lies diese ersten Seiten in Ruhe — sie sparen dir Zeit und ersparen dir Frust.
    Auf geht's, gemeinsam!""",
 "passo": "Schritt",
 "como_h2": "So funktioniert dieses Material",
 "como_sub": """Damit alles übersichtlich bleibt, kommt das Material in getrennten Dateien,
    nummeriert als <b>Schritte</b>. Halte dich an die Reihenfolge — jeder Schritt ist ein
    Teil deines Tages.""",
 "como_pe": """In jeder Datei haben die Rezepte eine <b>Nummer</b>
    (zum Beispiel <b>Rezept 003</b>). Über diese Nummer gibt dir der 30-Tage-Plan weiter
    hinten an, was du an welchem Tag isst.""",
 "passos": [
  ("Fang hier an", "Diese Datei. Die Anleitung, die Hinweise und der 30-Tage-Plan."),
  ("Frühstück", "30 Rezepte, um mit Energie und Sättigung in den Tag zu starten."),
  ("Mittagessen", "35 vollständige und leichte Gerichte für die Tagesmitte."),
  ("Abendessen", "35 leichtere Möglichkeiten für den Abend."),
  ("Desserts", "20 Fitness-Süßspeisen ohne Zucker, die die Lust ohne schlechtes Gewissen stillen."),
  ("Smoothies, Säfte und Detox-Tees", "30 Getränke, die versorgen, entwässern und anregen."),
  ("Bonus 1 — Vegetarische Ernährung", "20 gut verteilte Möglichkeiten ohne Fleisch."),
  ("Bonus 2 — Pilates für einen flachen Bauch", "12 Bauchübungen, ganz ohne Geräte."),
  ("Bonus 3 — 50 Gewohnheiten und Übungen", "Die Übungen und Gewohnheiten, die das Ergebnis beschleunigen."),
 ],
 "avisos_h2": "Die Wahrheit, ehrlich gesagt",
 "avisos_sub": """Vor allen Rezepten vier Wahrheiten, die dir sonst niemand sagt —
    und die für deinen Erfolg den ganzen Unterschied machen.""",
 "avisos": [
  ("Die Ernährung wirkt keine Wunder", "Es gibt keine Zauberformel. Was es gibt, ist Beständigkeit. Unter der Woche dem Plan zu folgen und am Wochenende bei Süßem und Frittiertem zu übertreiben macht die ganze Mühe zunichte. Das Ergebnis kommt bei allen, die die Gewohnheit die meiste Zeit halten."),
  ("Das Ergebnis braucht einige Monate", "Du wirst dich nicht über Nacht verändern — und das ist gut so, denn was schnell kommt, geht auch schnell wieder. Gib deinem Körper einige Monate Beständigkeit, und die Veränderung wird stabil und dauerhaft sein."),
  ("Bewegung gehört dazu", "Die Ernährung ist der größte Teil, aber der Körper verändert sich wirklich, wenn du dich auch bewegst. Bonus 2 und 3 bringen Übungen für jedes Niveau, drinnen und draußen. Nutze sie."),
  ("Keine falschen Versprechen", "Wir versprechen dir nicht, dass du in einer Woche 10 Kilo verlierst, denn das wäre gelogen. Wir liefern dir ein vollständiges und ehrliches Programm, das mit Beständigkeit befolgt echte und dauerhafte Ergebnisse bringen kann."),
 ],
 "dicas_h2": "Tipps, um mehr herauszuholen",
 "dicas_sub": "Kleine Kniffe, die dir den Weg leichter machen.",
 "dicas": [
  ("Unsicher bei einem Rezept? Nutze YouTube",
   """Wenn du nicht weißt, wie ein Schritt geht, such einfach auf YouTube nach dem
      <b>Namen des Rezepts + „Zubereitung“</b> — dann erscheinen Videos, die es
      Schritt für Schritt zeigen. Das hilft enorm, vor allem am Anfang."""),
  ("Schreib dir auf und druck aus, was du nutzt",
   """Markiere die Rezepte, die dir am besten gefallen haben, und mach dir
      <b>Notizen</b> darüber, was du in der Woche einkaufst und zubereitest. Wenn du
      magst, <b>druck</b> die Seiten mit den Gerichten, den Gewohnheiten und den Übungen
      aus, die dich interessieren, und häng sie sichtbar auf, in der Küche oder an den
      Kühlschrank. Was in Reichweite liegt, setzen wir auch um."""),
  ("Über die Kalorien und die Portionen",
   """Die Kalorien jedes Rezepts sind <b>ungefähre Werte</b>, berechnet nach
      Standard-Nährwerttabellen — sie sind ein Anhaltspunkt, keine genaue Labormessung.
      Jedes Rezept bringt eine <b>Tabelle zum Anpassen nach Geschlecht und Gewicht</b>
      mit: Suche deine Zeile und halte dich an diese Mengen. Gemüse, Blattsalat, Kaffee
      und Tee ohne Zucker sind frei, so viel du magst — das musst du nicht mitzählen."""),
 ],
 "plano_h2": "Ernährungsplan für 30 Tage",
 "plano_sub": """Ein ganzer Monat, für dich zusammengestellt — du musst ihm nur folgen.
    Jeder Tag bringt ein anderes Frühstück, ein Mittagessen, ein Abendessen, ein Dessert
    und ein Getränk, ohne dass sich die Gerichte im Lauf des Monats wiederholen.""",
 "plano_note": """Die Nummer vor jedem Rezept sagt dir, wo du es in der Datei der
    jeweiligen Kategorie findest (zum Beispiel steht <b>Rezept 031</b> in der Datei
    <b>Mittagessen</b>). Die Desserts beginnen ab Tag 21 von vorn, weil es nur 20 sind.
    Du kannst jedes Gericht jederzeit gegen ein anderes aus derselben Kategorie
    tauschen, das dir besser gefällt.""",
 "dia": "Tag",
 "rotulos": ("Frühstück", "Mittagessen", "Abendessen", "Dessert", "Getränk"),
},
"fr": {
 "arquivo": "Etape 1 - Commence ici.pdf",
 "titulo": "Commence ici",
 "badge": "Commence ici",
 "cover_h1": "Bienvenue !",
 "cover_lead": """Quel plaisir de t'avoir ici. Tu viens de faire le premier pas
    pour maigrir en mangeant bien — sans avoir faim et sans régimes farfelus. Ce
    matériel est un <b>programme complet</b> : 150 recettes minceur, un plan de
    30 jours et trois bonus d'exercices et d'habitudes. Avant de te mettre à cuisiner,
    lis ces premières pages tranquillement — elles vont t'épargner du temps et de la
    frustration. On y va, ensemble !""",
 "passo": "Étape",
 "como_h2": "Comment fonctionne ce matériel",
 "como_sub": """Pour que tout reste bien rangé, le matériel arrive en fichiers séparés,
    numérotés comme des <b>étapes</b>. Suis l'ordre — chaque étape est une partie de
    ta journée.""",
 "como_pe": """Dans chaque fichier, les recettes ont un <b>numéro</b>
    (par exemple <b>Recette 003</b>). C'est par ce numéro que le plan de 30 jours, plus
    loin, t'indique quoi manger chaque jour.""",
 "passos": [
  ("Commence ici", "Ce fichier. Les consignes, les avertissements et le plan de 30 jours."),
  ("Petits-déjeuners", "30 recettes pour commencer la journée avec de l'énergie et de la satiété."),
  ("Déjeuners", "35 plats complets et légers pour le milieu de la journée."),
  ("Dîners", "35 options plus légères pour le soir."),
  ("Desserts", "20 douceurs minceur sans sucre qui calment l'envie sans culpabilité."),
  ("Smoothies, jus et thés détox", "30 boissons pour s'hydrater, dégonfler et stimuler."),
  ("Bonus 1 — Alimentation végétarienne", "20 options sans viande, bien réparties."),
  ("Bonus 2 — Pilates ventre plat", "12 exercices pour le ventre, sans aucun matériel."),
  ("Bonus 3 — 50 habitudes et exercices", "Les exercices et les habitudes qui accélèrent le résultat."),
 ],
 "avisos_h2": "La vérité, en toute honnêteté",
 "avisos_sub": """Avant toute recette, quatre vérités que personne ne te dit d'ordinaire —
    et qui font toute la différence pour ta réussite.""",
 "avisos": [
  ("L'alimentation ne fait pas de miracle", "Il n'existe pas de formule magique. Ce qui existe, c'est la régularité. Suivre le menu en semaine et abuser des sucreries et des fritures le week-end annule tous les efforts. Le résultat vient à ceux qui tiennent l'habitude la plupart du temps."),
  ("Le résultat prend quelques mois", "Tu ne vas pas changer du jour au lendemain — et heureusement, car ce qui vient vite repart vite aussi. Donne à ton corps quelques mois de régularité et le changement sera solide et durable."),
  ("L'exercice fait partie du jeu", "L'alimentation représente la plus grande part, mais le corps se transforme vraiment quand tu bouges aussi. Les Bonus 2 et 3 proposent des exercices pour tous les niveaux, à la maison et dehors. Sers-t'en."),
  ("Aucune promesse mensongère", "Nous ne te promettons pas de perdre 10 kilos en une semaine, parce que ce serait un mensonge. Nous te livrons un programme complet et honnête qui, suivi avec régularité, peut apporter des résultats réels et durables."),
 ],
 "dicas_h2": "Des conseils pour en tirer le meilleur",
 "dicas_sub": "De petites astuces qui rendent ton parcours plus facile.",
 "dicas": [
  ("Un doute sur une recette ? Utilise YouTube",
   """Si tu ne sais pas comment faire une étape, cherche simplement sur YouTube le
      <b>nom de la recette + « préparation »</b> et des vidéos apparaîtront pour te
      montrer pas à pas. C'est une aide précieuse, surtout au début."""),
  ("Note et imprime ce que tu utilises",
   """Repère les recettes qui t'ont le plus plu et prends des <b>notes</b> de ce que
      tu vas acheter et préparer dans la semaine. Si tu préfères, <b>imprime</b> les
      pages des plats, des habitudes et des exercices qui t'intéressent et laisse-les
      bien en vue, dans la cuisine ou sur le réfrigérateur. Ce qui est à portée de main,
      on le fait."""),
  ("À propos des calories et des portions",
   """Les calories de chaque recette sont des <b>valeurs approximatives</b>, calculées
      d'après des tables nutritionnelles standard — elles servent de repère, pas de
      mesure exacte de laboratoire. Chaque recette apporte un <b>tableau d'ajustement
      selon le sexe et le poids</b> : trouve ta ligne et suis ces quantités. Les légumes,
      la salade, le café et le thé sans sucre sont libres, à volonté — tu n'as pas
      besoin de les compter."""),
 ],
 "plano_h2": "Plan alimentaire de 30 jours",
 "plano_sub": """Un mois entier monté pour toi — tu n'as qu'à le suivre. Chaque jour
    apporte un petit-déjeuner, un déjeuner, un dîner, un dessert et une boisson
    différents, sans répéter les plats au fil du mois.""",
 "plano_note": """Le numéro devant chaque recette indique où la trouver dans le fichier
    de sa catégorie (par exemple, la <b>Recette 031</b> se trouve dans le fichier
    <b>Déjeuners</b>). Les desserts, n'étant que 20, recommencent à partir du jour 21.
    Sens-toi libre de remplacer n'importe quel plat par un autre de la même catégorie
    que tu préfères.""",
 "dia": "Jour",
 "rotulos": ("Petit-déjeuner", "Déjeuner", "Dîner", "Dessert", "Boisson"),
},
}

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
.drow{display:grid;grid-template-columns:170px 1fr;gap:10px;padding:5px 0;align-items:baseline}
.drow .lbl{color:var(--soft);font-weight:800;font-size:13.5px;text-transform:uppercase;letter-spacing:.04em}
.drow .val{font-size:16.5px;line-height:1.45;color:var(--ink)}
.drow .val .n{color:var(--green);font-weight:800;margin-right:6px}
"""


def _mods(lang):
    nomes = ["receitas_cafe", "receitas_almoco", "receitas_jantar",
             "receitas_sobremesa", "receitas_suco"]
    ms = [importlib.import_module("%s_%s" % (n, lang)) for n in nomes]
    for m in ms:
        importlib.reload(m)
    return ms


def cover(T):
    return """
<div class="cover">
  <span class="badge">%s</span>
  <h1>%s</h1>
  <div class="rule"></div>
  <p class="lead">%s</p>
</div>
""" % (_html.escape(T["badge"]), _html.escape(T["cover_h1"]), T["cover_lead"])


def como_funciona(T):
    linhas = ""
    for i, (t, d) in enumerate(T["passos"], 1):
        linhas += ('<div class="stepbox"><div class="sn">%d</div>'
                   '<p><b>%s %d — %s.</b> %s</p></div>'
                   % (i, _html.escape(T["passo"]), i, _html.escape(t), _html.escape(d)))
    return """<div class="sec">
  <h2>%s</h2>
  <p class="sub">%s</p>
  %s
  <p style="margin-top:16px">%s</p>
</div>""" % (_html.escape(T["como_h2"]), T["como_sub"], linhas, T["como_pe"])


def avisos(T):
    blocos = "".join('<div class="warn"><b>%s</b><p>%s</p></div>'
                     % (_html.escape(t), _html.escape(d)) for t, d in T["avisos"])
    return """<div class="sec">
  <h2>%s</h2>
  <p class="sub">%s</p>
  %s
</div>""" % (_html.escape(T["avisos_h2"]), T["avisos_sub"], blocos)


def dicas(T):
    caixas = "".join('<div class="tipbox"><h3>%s</h3><p>%s</p></div>'
                     % (_html.escape(t), d) for t, d in T["dicas"])
    return """<div class="sec">
  <h2>%s</h2>
  <p class="sub">%s</p>
  %s
</div>""" % (_html.escape(T["dicas_h2"]), _html.escape(T["dicas_sub"]), caixas)


def _row(lbl, num, mod, idx):
    return ('<div class="drow"><span class="lbl">%s</span>'
            '<span class="val"><span class="n">%03d</span>%s</span></div>'
            % (_html.escape(lbl), num, _html.escape(mod.RECEITAS[idx]["nome"])))


def plano_30(T, mods):
    R_cafe, R_almoco, R_jantar, R_sobremesa, R_suco = mods
    L = T["rotulos"]
    dias = ""
    for dia in range(1, 31):
        s = ((dia - 1) % 20) + 1   # sobremesa 101..120, repete apos 20
        dias += ("""<div class="dcard"><h3>%s %d</h3>
  %s%s%s%s%s</div>""" % (
            _html.escape(T["dia"]), dia,
            _row(L[0], dia, R_cafe, dia - 1),
            _row(L[1], 30 + dia, R_almoco, dia - 1),
            _row(L[2], 65 + dia, R_jantar, dia - 1),
            _row(L[3], 100 + s, R_sobremesa, s - 1),
            _row(L[4], 120 + dia, R_suco, dia - 1)))
    return """<div class="sec">
  <h2>%s</h2>
  <p class="sub">%s</p>
  <p class="plan-note">%s</p>
  %s
</div>""" % (_html.escape(T["plano_h2"]), T["plano_sub"], T["plano_note"], dias)


def build(lang):
    T = TEXTOS[lang]
    mods = _mods(lang)
    corpo = cover(T) + como_funciona(T) + avisos(T) + dicas(T) + plano_30(T, mods)
    doc = ("""<!DOCTYPE html><html lang="%s"><head><meta charset="utf-8">
<title>%s</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700;800;900&display=swap" rel="stylesheet">
<style>%s%s
%s</style></head><body>%s</body></html>"""
           % (motor.I18N[lang]["html_lang"], _html.escape(T["titulo"]),
              motor.ESTILO, motor.I18N[lang]["css"], EXTRA_CSS, corpo))

    html_path = os.path.join(AQUI, "_tmp_frente_%s.html" % lang)
    saida = os.path.join(AQUI, "..", "Entregavel em %s" % lang.upper())
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
                    "http://127.0.0.1:%d/_tmp_frente_%s.html" % (PORTA, lang)],
                   capture_output=True)
    ok = os.path.exists(pdf_path)
    print("PDF:", pdf_path, "OK" if ok else "FALHOU",
          "(%.1f MB)" % (os.path.getsize(pdf_path) / 1e6) if ok else "")
    if ok and os.path.exists(html_path):
        os.remove(html_path)
    return ok


if __name__ == "__main__":
    sys.exit(0 if build(sys.argv[1] if len(sys.argv) > 1 else "de") else 1)
