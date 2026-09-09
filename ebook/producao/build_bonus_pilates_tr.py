# -*- coding: utf-8 -*-
"""BÔNUS 2 — PILATES. TRADUZIDO.
Uso: python build_bonus_pilates_tr.py <de|fr>
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
 "arquivo": "Schritt 8 - Bonus 2 - Pilates fuer einen flachen Bauch.pdf",
 "titulo": "Bonus 2 — Pilates für einen flachen Bauch zu Hause",
 "badge": "Bonus 2", "h1": "Pilates für einen flachen Bauch zu Hause",
 "tag": "Pilates", "num": "Bonus · Pilates",
 "st_nivel": "Niveau", "st_series": "Sätze", "st_tempo": "Zeit",
 "h_foco": "Schwerpunkt", "h_passos": "So geht's",
 "h_resp": "Atmung", "h_dica": "Tipp",
 "lead": """Pilates ist eine Gymnastik aus langsamen, kontrollierten Bewegungen,
    die vor allem die <b>Körpermitte</b> kräftigt — den Bereich von Bauch und Rücken.
    Ohne Geräte, ohne Belastung und ohne aus dem Haus zu gehen, ist es perfekt als
    Begleitung zur Ernährung und beschleunigt die Ergebnisse. Du brauchst nur eine Matte
    oder ein Handtuch auf dem Boden.""",
 "box_h2": "Warum das hilft, den Bauch flacher zu bekommen",
 "box_itens": ["Es kräftigt den <b>tiefen Bauchmuskel</b>, der wie ein natürliches Korsett wirkt und den Bauch nach innen hält.",
               "Es verbessert die <b>Haltung</b> — und aufrechter zu stehen lässt den Bauch schon sichtbar flacher wirken.",
               "Es formt die <b>Taille</b>, indem es die seitlichen Muskeln trainiert.",
               "Es ist <b>gelenkschonend</b>: sanft zu den Gelenken, ideal für jedes Alter."],
 "honest_label": "Eine wichtige Wahrheit",
 "honest": """Keine Übung verbrennt Fett nur am Bauch — das gibt es nicht. Das Fett geht am
      ganzen Körper zurück, und was diesen Verlust steuert, ist die <b>Ernährung</b>.
      Pilates kräftigt, formt und verbessert die Haltung; zusammen mit den Rezepten
      aus dem Buch ist es die Kombination, die den Bauch wirklich schmaler macht.
      Beständigkeit ist alles.""",
 "how": """<b>So nutzt du das:</b> Mach es <b>3- bis 4-mal pro Woche</b>, 15 bis 20 Minuten
    lang. Zieh bequeme Kleidung an, trainiere auf nüchternen Magen oder mindestens
    1 Stunde nach dem Essen, und <b>atme immer weiter</b> (halte nie die Luft an).
    Fang mit den leichteren Varianten an, die bei jeder Übung angegeben sind, und
    steigere dich mit der Zeit. Wenn du einen stechenden Schmerz spürst, hör auf.""",
 "kicker": "Bonus 2 · Pilates für einen flachen Bauch",
 "head_h2": "Die 12 Übungen",
 "head_p": """Mach sie der Reihe nach, achte auf die Atmung und auf deine eigene Grenze. Jede
    Übung bringt den Schwerpunkt, die Zahl der Wiederholungen, die Schritt-für-Schritt-
    Anleitung und, wo es sie gibt, eine leichtere Variante mit.""",
 "plan_h2": "Wochenplan",
 "plan_p": """Wähle 3 bis 4 Tage (zum Beispiel <b>Montag, Mittwoch und Freitag</b>) und mach die
      vollständige Abfolge der 12 Übungen in der Reihenfolge, in der sie erscheinen.""",
 "plan_seq": """Die Reihenfolge ist mit Absicht so: Sie beginnt mit dem <b>Aufwärmen</b>
      (1 und 2), geht durch die <b>Bauchübungen</b> (3 bis 10), kräftigt den <b>Rücken</b>
      (11) und endet mit der <b>Dehnung</b> (12). Lass niemals das Aufwärmen oder die
      Dehnung aus.""",
 "foto_ph": ('<b>FOTO %s</b><small>quadratischer Platz reserviert<br>'
             '(mit dem Prompt erzeugen und "%s" nennen)</small>'),
},
"fr": {
 "arquivo": "Etape 8 - Bonus 2 - Pilates ventre plat.pdf",
 "titulo": "Bonus 2 — Pilates ventre plat à la maison",
 "badge": "Bonus 2", "h1": "Pilates ventre plat à la maison",
 "tag": "Pilates", "num": "Bonus · Pilates",
 "st_nivel": "Niveau", "st_series": "Séries", "st_tempo": "Temps",
 "h_foco": "Objectif", "h_passos": "Comment faire",
 "h_resp": "Respiration", "h_dica": "Astuce",
 "lead": """Le Pilates est une gymnastique aux mouvements lents et contrôlés qui
    renforce surtout le <b>centre du corps</b> — la zone du ventre et du dos.
    Sans matériel, sans impact et sans sortir de chez toi, il est parfait pour
    accompagner l'alimentation et accélérer les résultats. Tu n'as besoin que d'un
    tapis ou d'une serviette posée au sol.""",
 "box_h2": "Pourquoi ça aide à affiner le ventre",
 "box_itens": ["Il renforce le <b>muscle profond du ventre</b>, qui agit comme une gaine naturelle et maintient le ventre rentré.",
               "Il améliore la <b>posture</b> — et se tenir plus droit rend déjà le ventre visiblement plus plat.",
               "Il dessine la <b>taille</b> en travaillant les muscles latéraux.",
               "Il est <b>doux pour les articulations</b> : idéal à tout âge."],
 "honest_label": "Une vérité importante",
 "honest": """Aucun exercice ne brûle la graisse uniquement au ventre — cela n'existe pas.
      La graisse part de tout le corps, et ce qui commande cette perte, c'est
      l'<b>alimentation</b>. Le Pilates renforce, dessine et améliore la posture ;
      avec les recettes du livre, c'est la combinaison qui affine vraiment le ventre.
      La régularité fait tout.""",
 "how": """<b>Comment l'utiliser :</b> fais-le <b>3 à 4 fois par semaine</b>, 15 à
    20 minutes. Mets des vêtements confortables, entraîne-toi à jeun ou au moins
    1 heure après avoir mangé, et <b>respire toujours</b> (ne bloque jamais ta
    respiration). Commence par les variantes les plus faciles indiquées à chaque
    exercice et progresse avec le temps. Si tu ressens une douleur vive, arrête.""",
 "kicker": "Bonus 2 · Pilates ventre plat",
 "head_h2": "Les 12 exercices",
 "head_p": """Fais-les dans l'ordre, en respectant la respiration et ta propre limite.
    Chaque exercice indique l'objectif, le nombre de répétitions, le pas à pas et,
    quand elle existe, une variante plus facile.""",
 "plan_h2": "Le plan de la semaine",
 "plan_p": """Choisis 3 à 4 jours (par exemple <b>lundi, mercredi et vendredi</b>) et fais
      la séquence complète des 12 exercices dans l'ordre où ils apparaissent.""",
 "plan_seq": """L'ordre est pensé : il commence par l'<b>échauffement</b> (1 et 2),
      passe par les exercices de <b>ventre</b> (3 à 10), renforce le <b>dos</b> (11)
      et se termine par l'<b>étirement</b> (12). Ne saute jamais l'échauffement ni
      l'étirement.""",
 "foto_ph": ('<b>PHOTO %s</b><small>emplacement carré réservé<br>'
             '(à générer avec le prompt et à nommer "%s")</small>'),
},
"en": {
 "arquivo": "Step 8 - Bonus 2 - Flat Belly Pilates at Home.pdf",
 "titulo": "Bonus 2 — Flat Belly Pilates at Home",
 "badge": "Bonus 2", "h1": "Flat Belly Pilates at Home",
 "tag": "Pilates", "num": "Bonus · Pilates",
 "st_nivel": "Level", "st_series": "Sets", "st_tempo": "Time",
 "h_foco": "Focus", "h_passos": "How to do it",
 "h_resp": "Breathing", "h_dica": "Tip",
 "lead": """Pilates is a form of exercise with slow, controlled movements that
    mainly strengthens the <b>center of your body</b> — the belly and back area.
    With no equipment, no impact and without leaving home, it is perfect to go
    with your eating plan and speed up your results. All you need is a mat or a
    towel on the floor.""",
 "box_h2": "Why this helps to slim your belly",
 "box_itens": ["It strengthens the <b>deep belly muscle</b>, which works like a natural corset and holds your belly in.",
               "It improves your <b>posture</b> — and standing taller already makes your belly look visibly flatter.",
               "It shapes your <b>waist</b> by working the side muscles.",
               "It is <b>gentle on your joints</b>: ideal at any age."],
 "honest_label": "An important truth",
 "honest": """No exercise burns fat only on your belly — that does not exist.
      Fat comes off your whole body, and what drives that loss is your
      <b>food</b>. Pilates strengthens, shapes and improves your posture;
      together with the recipes in this book, it is the combination that really
      slims your belly. Consistency is everything.""",
 "how": """<b>How to use this:</b> do it <b>3 to 4 times a week</b>, for 15 to
    20 minutes. Wear comfortable clothes, train on an empty stomach or at least
    1 hour after eating, and <b>keep breathing</b> (never hold your breath).
    Start with the easier variations given for each exercise and build up over
    time. If you feel a sharp pain, stop.""",
 "kicker": "Bonus 2 · Flat Belly Pilates",
 "head_h2": "The 12 exercises",
 "head_p": """Do them in order, respecting the breathing and your own limit.
    Each exercise gives the focus, the number of reps, the step by step and,
    when there is one, an easier variation.""",
 "plan_h2": "The weekly plan",
 "plan_p": """Pick 3 to 4 days (for example <b>Monday, Wednesday and Friday</b>) and do
      the full sequence of the 12 exercises in the order they appear.""",
 "plan_seq": """The order is deliberate: it starts with the <b>warm-up</b> (1 and 2),
      goes through the <b>belly</b> exercises (3 to 10), strengthens the <b>back</b> (11)
      and finishes with the <b>stretch</b> (12). Never skip the warm-up or
      the stretch.""",
 "foto_ph": ('<b>PHOTO %s</b><small>square space reserved<br>'
             '(generate with the prompt and name it "%s")</small>'),
},
"es": {
 # ⛔ Nome de arquivo SEM acento (glossario §3).
 "arquivo": "Paso 8 - Bono 2 - Pilates para Abdomen Plano.pdf",
 "titulo": "Bono 2 — Pilates para Abdomen Plano en Casa",
 "badge": "Bono 2", "h1": "Pilates para Abdomen Plano en Casa",
 "tag": "Pilates", "num": "Bono · Pilates",
 "st_nivel": "Nivel", "st_series": "Series", "st_tempo": "Tiempo",
 "h_foco": "Enfoque", "h_passos": "Cómo hacerlo",
 "h_resp": "Respiración", "h_dica": "Consejo",
 "lead": """El Pilates es una forma de ejercicio con movimientos lentos y controlados que
    fortalece principalmente el <b>centro del cuerpo</b> — la zona de la panza y la espalda.
    Sin equipo, sin impacto y sin salir de casa, es perfecto para acompañar
    tu plan de alimentación y acelerar tus resultados. Lo único que necesitas es un tapete o una
    toalla en el piso.""",
 "box_h2": "Por qué esto ayuda a adelgazar la panza",
 "box_itens": ["Fortalece el <b>músculo profundo de la panza</b>, que funciona como una faja natural y mete el abdomen.",
               "Mejora tu <b>postura</b> — y estar más erguida ya hace que la panza se vea visiblemente más plana.",
               "Da forma a tu <b>cintura</b> trabajando los músculos laterales.",
               "Es <b>suave con tus articulaciones</b>: ideal a cualquier edad."],
 "honest_label": "Una verdad importante",
 "honest": """Ningún ejercicio quema grasa solo de la panza — eso no existe.
      La grasa se va de todo el cuerpo, y lo que impulsa esa pérdida es tu
      <b>alimentación</b>. El Pilates fortalece, da forma y mejora tu postura;
      junto con las recetas de este libro, es la combinación que de verdad
      adelgaza la panza. La constancia lo es todo.""",
 "how": """<b>Cómo usar esto:</b> hazlo <b>3 o 4 veces por semana</b>, de 15 a
    20 minutos. Usa ropa cómoda, entrena en ayunas o por lo menos
    1 hora después de comer, y <b>sigue respirando</b> (nunca detengas la respiración).
    Empieza con las variaciones más fáciles que se dan en cada ejercicio y ve subiendo con
    el tiempo. Si sientes un dolor agudo, detente.""",
 "kicker": "Bono 2 · Pilates para Abdomen Plano",
 "head_h2": "Los 12 ejercicios",
 "head_p": """Hazlos en orden, respetando la respiración y tu propio límite.
    Cada ejercicio indica el enfoque, el número de repeticiones, el paso a paso y,
    cuando la hay, una variación más fácil.""",
 "plan_h2": "El plan semanal",
 "plan_p": """Elige 3 o 4 días (por ejemplo <b>lunes, miércoles y viernes</b>) y haz
      la secuencia completa de los 12 ejercicios en el orden en que aparecen.""",
 "plan_seq": """El orden es deliberado: empieza con el <b>calentamiento</b> (1 y 2),
      pasa por los ejercicios de <b>panza</b> (3 al 10), fortalece la <b>espalda</b> (11)
      y termina con el <b>estiramiento</b> (12). Nunca te saltes el calentamiento ni
      el estiramiento.""",
 "foto_ph": ('<b>FOTO %s</b><small>espacio cuadrado reservado<br>'
             '(generar con el prompt y nombrarla "%s")</small>'),
},
"it": {
 # ⛔ Nome de arquivo SEM acento (glossario §3).
 "arquivo": "Passo 8 - Bonus 2 - Pilates per la Pancia Piatta.pdf",
 "titulo": "Bonus 2 — Pilates per la Pancia Piatta a Casa",
 "badge": "Bonus 2", "h1": "Pilates per la Pancia Piatta a Casa",
 "tag": "Pilates", "num": "Bonus · Pilates",
 "st_nivel": "Livello", "st_series": "Serie", "st_tempo": "Tempo",
 "h_foco": "Obiettivo", "h_passos": "Come si fa",
 "h_resp": "Respirazione", "h_dica": "Consiglio",
 "lead": """Il Pilates è una forma di esercizio con movimenti lenti e controllati che
    rafforza soprattutto il <b>centro del corpo</b> — la zona della pancia e della schiena.
    Senza attrezzi, senza impatto e senza uscire di casa, è perfetto per accompagnare
    il tuo piano alimentare e accelerare i risultati. L'unica cosa che ti serve è un tappetino o un
    asciugamano per terra.""",
 "box_h2": "Perché questo aiuta a sgonfiare la pancia",
 "box_itens": ["Rafforza il <b>muscolo profondo della pancia</b>, che funziona come una guaina naturale e tira dentro l'addome.",
               "Migliora la tua <b>postura</b> — e stare più dritta fa già sembrare la pancia visibilmente più piatta.",
               "Dà forma alla tua <b>vita</b> lavorando i muscoli laterali.",
               "È <b>delicato con le articolazioni</b>: ideale a qualsiasi età."],
 "honest_label": "Una verità importante",
 "honest": """Nessun esercizio brucia il grasso solo della pancia — non esiste.
      Il grasso se ne va da tutto il corpo, e ciò che spinge quella perdita è la tua
      <b>alimentazione</b>. Il Pilates rafforza, dà forma e migliora la postura;
      insieme alle ricette di questo libro, è la combinazione che davvero
      sgonfia la pancia. La costanza è tutto.""",
 "how": """<b>Come usare questo bonus:</b> fallo <b>3 o 4 volte a settimana</b>, da 15 a
    20 minuti. Metti abiti comodi, allenati a digiuno o almeno
    1 ora dopo aver mangiato, e <b>continua a respirare</b> (non trattenere mai il respiro).
    Inizia con le varianti più facili indicate in ogni esercizio e aumenta con
    il tempo. Se senti un dolore acuto, fermati.""",
 "kicker": "Bonus 2 · Pilates per la Pancia Piatta",
 "head_h2": "I 12 esercizi",
 "head_p": """Falli in ordine, rispettando la respirazione e il tuo limite.
    Ogni esercizio indica l'obiettivo, il numero di ripetizioni, il passo passo e,
    quando c'è, una variante più facile.""",
 "plan_h2": "Il piano settimanale",
 "plan_p": """Scegli 3 o 4 giorni (per esempio <b>lunedì, mercoledì e venerdì</b>) e fai
      la sequenza completa dei 12 esercizi nell'ordine in cui compaiono.""",
 "plan_seq": """L'ordine è voluto: inizia con il <b>riscaldamento</b> (1 e 2),
      passa per gli esercizi di <b>pancia</b> (dal 3 al 10), rafforza la <b>schiena</b> (11)
      e chiudi con l'<b>allungamento</b> (12). Non saltare mai il riscaldamento né
      l'allungamento.""",
 "foto_ph": ('<b>FOTO %s</b><small>spazio quadrato riservato<br>'
             '(generare con il prompt e chiamarla "%s")</small>'),
},
}

EXTRA_CSS = """
.veg-cover{page-break-after:always;padding-top:24px}
.veg-badge{display:inline-block;background:var(--green);color:#fff;font-size:16px;font-weight:900;
letter-spacing:.14em;text-transform:uppercase;padding:9px 20px;border-radius:999px}
.veg-cover h1{font-size:50px;font-weight:900;letter-spacing:-.03em;margin:18px 0 18px;line-height:1.05;color:var(--green)}
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
.ex-list td.s{text-align:right;color:var(--soft);font-size:13px;white-space:nowrap;width:200px}
.foco{margin-top:2px;font-size:15px;color:var(--ink);line-height:1.5}
.resp{margin-top:22px;background:var(--green-tint);border-left:4px solid var(--green);
border-radius:0 10px 10px 0;padding:14px 18px;break-inside:avoid}
.resp b{color:var(--green);font-size:12.5px;text-transform:uppercase;letter-spacing:.06em;display:block;margin-bottom:5px}
.resp p{font-size:15px;line-height:1.55}
"""


def _ex_list_html(exs):
    linhas = "".join('<tr><td class="n">%d</td><td>%s</td><td class="s">%s</td></tr>'
                     % (i + 1, _html.escape(e["nome"]), _html.escape(e["series"]))
                     for i, e in enumerate(exs))
    return '<div class="ex-list"><table>%s</table></div>' % linhas


def intro_html(T, exs):
    itens = "".join("<li>%s</li>" % x for x in T["box_itens"])
    return """
<div class="veg-cover">
  <span class="veg-badge">%s</span>
  <h1>%s</h1>
  <div class="veg-rule"></div>
  <p class="veg-lead">%s</p>

  <div class="veg-box"><h2>%s</h2><ul>%s</ul></div>

  <div class="honest">
    <span class="hlabel">%s</span>
    <p>%s</p>
  </div>

  <div class="veg-how">%s</div>
</div>

<div class="ex-head">
  <div class="kicker">%s</div>
  <h2>%s</h2>
  <p>%s</p>

  <div class="plan">
    <h2>%s</h2>
    <p>%s</p>
    <div class="seq">%s</div>
  </div>
  %s
</div>
""" % (_html.escape(T["badge"]), _html.escape(T["h1"]), T["lead"],
       _html.escape(T["box_h2"]), itens,
       _html.escape(T["honest_label"]), T["honest"], T["how"],
       _html.escape(T["kicker"]), _html.escape(T["head_h2"]), T["head_p"],
       _html.escape(T["plan_h2"]), T["plan_p"], T["plan_seq"],
       _ex_list_html(exs))


def render_exercicio(T, e, num):
    n3 = "%03d" % num
    foto = T["foto_ph"] % (n3, n3)
    if os.path.isdir(IMG):
        for ext in (".jpg", ".jpeg", ".png", ".webp"):
            if os.path.isfile(os.path.join(IMG, n3 + ext)):
                foto = '<img src="fotos/%s" alt="">' % (n3 + ext)
                break
    passos = "".join("<li>%s</li>" % _html.escape(x) for x in e["passos"])
    return """<div class="recipe">
  <div class="top"><span class="tag">%s</span><span class="num">%s</span></div>
  <h1>%s</h1>
  <p class="hook">%s</p>
  <div class="grid">
    <div class="photo">%s</div>
    <div>
      <div class="stats">
        <div class="stat"><div class="v">%s</div><div class="l">%s</div></div>
        <div class="stat"><div class="v">%s</div><div class="l">%s</div></div>
        <div class="stat"><div class="v">%s</div><div class="l">%s</div></div>
      </div>
      <h2>%s</h2>
      <p class="foco">%s</p>
    </div>
  </div>
  <div class="steps"><h2>%s</h2><ol>%s</ol></div>
  <div class="resp"><b>%s</b><p>%s</p></div>
  <div class="tip"><b>%s</b><p>%s</p></div>
</div>""" % (_html.escape(T["tag"]), _html.escape(T["num"]),
            _html.escape(e["nome"]), _html.escape(e["hook"]), foto,
            _html.escape(e["nivel"]), _html.escape(T["st_nivel"]),
            _html.escape(e["series"]), _html.escape(T["st_series"]),
            _html.escape(e["tempo"]), _html.escape(T["st_tempo"]),
            _html.escape(T["h_foco"]), _html.escape(e["foco"]),
            _html.escape(T["h_passos"]), passos,
            _html.escape(T["h_resp"]), _html.escape(e["respiracao"]),
            _html.escape(T["h_dica"]), _html.escape(e["dica"]))


def build(lang):
    T = TEXTOS[lang]
    pil = importlib.import_module("exercicios_pilates_%s" % lang)
    importlib.reload(pil)
    corpo = intro_html(T, pil.EXERCICIOS)
    for i, e in enumerate(pil.EXERCICIOS):
        corpo += render_exercicio(T, e, 159 + i)

    doc = ("""<!DOCTYPE html><html lang="%s"><head><meta charset="utf-8">
<title>%s</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700;800;900&display=swap" rel="stylesheet">
<style>%s%s
%s</style></head><body>%s</body></html>"""
           % (motor.I18N[lang]["html_lang"], _html.escape(T["titulo"]),
              motor.ESTILO, motor.I18N[lang]["css"], EXTRA_CSS, corpo))

    html_path = os.path.join(AQUI, "_tmp_bonus2_%s.html" % lang)
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
                    "http://127.0.0.1:%d/_tmp_bonus2_%s.html" % (PORTA, lang)],
                   capture_output=True)
    ok = os.path.exists(pdf_path)
    print("PDF:", pdf_path, "OK" if ok else "FALHOU",
          "(%.1f MB)" % (os.path.getsize(pdf_path) / 1e6) if ok else "")
    if ok and os.path.exists(html_path):
        os.remove(html_path)
    return ok


if __name__ == "__main__":
    sys.exit(0 if build(sys.argv[1] if len(sys.argv) > 1 else "de") else 1)
