# -*- coding: utf-8 -*-
"""LANDING — DER ATEMANKER (alemao). Monta o `index.html` autossuficiente.

⛔ O CSS E OS ICONES NAO SAO COPIADOS A MAO. Eles saem do `landing-150`, que e'
onde o sistema de design mora. Copiar 19 KB de CSS para ca' criaria uma segunda
fonte da verdade que diverge no primeiro ajuste — a mesma razao pela qual o
`motor_atem` importa os tokens do `motor_receitas` em vez de redeclara-los.
O ARQUIVO GERADO continua autossuficiente (CSS e SVG inline), como o playbook
da landing exige; quem le' o HTML nao precisa deste script.

    python build_landing.py

⭐⭐ TRATAMENTO: `du`, NAO `Sie`. A landing do 150 usa `Sie`, e aqui isso seria
um erro de congruencia: o trafego chega do `gelo16`, cujo pool inteiro fala
`du` (`Dafür brauchst du kein Eis`, `Kommentiere ATEM`). Quem clica ouviu `du`
no video; a pagina que responde com `Sie` troca de pessoa no meio do funil.

⛔ O QUE EU NAO COPIEI DA LANDING DE REFERENCIA, E POR QUE:
  · `NUR NOCH 5 EXEMPLARE VERFÜGBAR` — escassez falsa. O produto e' um PDF;
    nao existe "ultimo exemplar". A propria §5 do PLAYBOOK-LANDING manda copy
    honesta, e na Alemanha (UWG) escassez inventada e' publicidade enganosa.
  · `Mehr als 4.782 positive Bewertungen` + o bloco de depoimentos — este
    produto nasceu hoje e nao tem um unico comprador. Inventar avaliacao e'
    fabricar prova. No lugar entrou `Was dieses Paket nicht verspricht`, que
    e' honesto E converte, porque quem esta' ansiosa ja' foi prometida demais.

⏳ PENDENCIA DO OPERADOR: pagina alema comercial precisa de IMPRESSUM e
DATENSCHUTZERKLÄRUNG (TMG/DSGVO). Eu nao tenho os dados da empresa do Ed, entao
o rodape traz os links preparados e vazios. Preencher antes de escalar trafego.
"""

import io
import os
import re
import shutil

AQUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(AQUI)
REF = os.path.join(REPO, "landing-150", "index-de.html")
FOTOS = os.path.join(REPO, "ebook", "producao", "atem")

# ⏳ Trocado pelo link real assim que o produto existir na Hotmart. Ate' la' o
# botao aponta para a propria oferta, nunca para um `#` morto — link morto na
# landing foi defeito medido nas tres paginas do ebook 150.
CHECKOUT = "#offer"

PRECO_DE = "39"
DESCONTO = "74%"


def _ref_css_e_icones():
    s = io.open(REF, encoding="utf-8").read()
    css = re.search(r"<style>(.*?)</style>", s, re.S).group(1)
    defs = re.search(r"(<svg[^>]*>\s*<defs>.*?</defs>\s*</svg>)", s, re.S).group(1)
    return css, defs


# ===========================================================================
# CONTEUDO — alemao, tratamento `du`
# ===========================================================================

DATEIEN = [
    ("anker", "Schritt 2 — Der Atemanker",
     "Die Grundübung: vier Sekunden ein, sechs Sekunden aus. Dazu die Haltung, "
     "die Hand auf den Rippen und fünf Varianten für Schreibtisch, Weg und "
     "Warteschlange."),
    ("lippen", "Schritt 3 — Der Notfall-Anker",
     "Neunzig Sekunden für den Moment, in dem es dich gerade erwischt. Im "
     "Sitzen, ohne Hilfsmittel, ohne dass jemand im Raum etwas mitbekommt."),
    ("plan21", "Schritt 4 — Dein 21-Tage-Plan",
     "Eine Aufgabe pro Tag, nie länger als fünf Minuten. Der Teil, der aus "
     "einer Übung eine Gewohnheit macht — mit Häkchen-Tabelle zum Ausdrucken."),
    ("abend", "Schritt 5 — Die Abendroutine",
     "Für den Kopf, der abends lauter wird als tagsüber, und für die Nächte, "
     "in denen du um drei wach liegst und rechnest."),
    ("handgelenk", "Bonus 1 — Kälte ohne Eis",
     "Der kleine Verstärker am Waschbecken: kaltes Wasser aufs Handgelenk, "
     "aufs Gesicht, die letzten zwanzig Sekunden der Dusche. Freiwillig."),
    ("tagebuch", "Bonus 2 — Dein Ruhe-Tagebuch",
     "Vorlagen zum Ausdrucken. Nach drei Wochen siehst du schwarz auf weiß, "
     "was sich verändert hat — und was dich zuverlässig hochfahren lässt."),
    ("haltung", "Schritt 1 — Fang hier an",
     "Warum dein Körper Alarm schlägt, obwohl nichts passiert, warum "
     "ausgerechnet das Ausatmen ihn abstellt, und die Sicherheitsregeln."),
]

CARDS = [
    ("ic-pulse", "Das Ausatmen ist der Schalter",
     "Beim Einatmen wird dein Herzschlag schneller, beim Ausatmen langsamer. "
     "Verlängere das Ausatmen, und du verlängerst genau den Teil, in dem dein "
     "Körper herunterfährt. Mehr ist das Prinzip nicht."),
    ("ic-bolt", "Zwei Minuten, nicht zwanzig",
     "Zwölf Atemzüge. Das ist eine Übung. Wer keine zwanzig Minuten am Tag "
     "übrig hat, ist genau die Person, für die das hier gebaut wurde — und "
     "nicht die, die dafür entschuldigt wird."),
    ("ic-leaf", "Kein Eis, kein Studio, keine Termine",
     "Du brauchst einen Stuhl. Keine Matte, keine App, kein Abo, keine "
     "Ausrüstung und nichts Kaltes. Es funktioniert bei dir zu Hause, im "
     "Warmen, im Sitzen."),
]

PROBLEM = [
    "<b>Tabletten beruhigen den Kopf.</b> An den Teil, der deinen Puls hochfährt "
    "und deine Brust eng macht, kommen sie nicht heran.",
    "<b>Reden hilft dem Kopf.</b> Deinem Körper hat nie jemand beigebracht, wie er "
    "wieder runterkommt, wenn nichts mehr passiert.",
    "<b>Apps zählen dir Sekunden vor.</b> Sie erklären dir nie, warum die eine "
    "Zahl größer sein muss als die andere — und genau daran hängt alles.",
    "<b>Und der Klassiker: „Entspann dich einfach.“</b> Als hätte irgendjemand "
    "das nicht schon versucht.",
]

BONI = [
    ("1", "ic-shield", "Kälte ohne Eis",
     "Drei Stufen am Waschbecken und in der Dusche, jede unter dreißig "
     "Sekunden. Mit den Regeln, die dabei nicht verhandelbar sind.", "19"),
    ("2", "ic-calendar", "Dein Ruhe-Tagebuch",
     "Wochenblätter, ein Auslöser-Blatt und drei Abendfragen. Zum Ausdrucken, "
     "damit du nach 21 Tagen etwas in der Hand hast statt eines Gefühls.", "14"),
]

SCHRITTE = [
    ("Du sicherst dir das Paket", "Über den sicheren Hotmart-Checkout. "
     "Einmalzahlung, kein Abo, keine Verlängerung."),
    ("Es landet in deinem Postfach", "In wenigen Minuten, als sieben PDF-Dateien "
     "zum Herunterladen. Auf Handy, Tablet, Rechner oder ausgedruckt."),
    ("Du fängst heute an", "Nicht nächsten Montag. Schritt 2 lesen, einmal "
     "mitmachen, fertig. Das sind fünf Minuten, einmalig."),
]

NICHT = [
    ("Es macht deinen Kopf nicht leer.", "Das verspricht dir hier niemand. Das "
     "Ziel ist kleiner und ehrlicher: schneller wieder runterkommen als vorher."),
    ("Es ist keine Behandlung.", "Der Atemanker ist eine Übung. Er ersetzt weder "
     "Ärztin noch Psychotherapie, stellt keine Diagnose und ist kein Medikament. "
     "Wenn du Medikamente nimmst, nimmst du sie weiter."),
    ("Einmal reicht nicht.", "Beim ersten Mal passiert bei vielen Menschen "
     "schlicht nichts. Der Effekt kommt aus der Wiederholung — deshalb liegt "
     "dem Paket ein 21-Tage-Plan bei und keine Wunderübung."),
    ("Es ist nicht für jeden der richtige Moment.", "Wenn du gerade in einer "
     "akuten seelischen Krise steckst, ist das hier nicht dein nächster Schritt. "
     "Dann hol dir bitte Unterstützung bei einem Menschen."),
]

FRAGEN = [
    ("Ist das dasselbe wie diese Eisbad-Sachen?",
     "Nein. Das Kalte ist bei uns ein freiwilliger Bonus am Waschbecken, und du "
     "kannst ihn komplett weglassen, ohne dass dir etwas fehlt. Die Methode "
     "selbst findet im Warmen statt, im Sitzen, angezogen."),
    ("Muss ich tief einatmen oder die Luft anhalten?",
     "Nein, und das ist wichtig: In diesem Paket wird nirgends hyperventiliert "
     "und nirgends die Luft mit leeren Lungen angehalten. Schnelles, tiefes "
     "Dauer-Atmen erzeugt genau die Symptome, die du loswerden willst."),
    ("Wie viel Zeit brauche ich wirklich?",
     "Zwei Minuten pro Übung. Der Plan sieht ab Woche 2 zweimal am Tag vor — "
     "das sind vier Minuten. Mehr wird es dauerhaft nicht."),
    ("Ich habe das mit dem Zählen noch nie hinbekommen.",
     "Deshalb steht in Schritt 2 eine ganze Übung nur dafür, was du machst, "
     "wenn dir sechs Sekunden zu lang sind, und eine Variante, bei der du gar "
     "nicht zählst, sondern Schritte gehst."),
    ("In welchem Format kommt das?",
     "Sieben PDF-Dateien, nummeriert von Schritt 1 bis Bonus 2, zusammen in "
     "einer ZIP-Datei. Kein Kurs-Login, kein Video, nichts, was abläuft."),
    ("Ist das etwas für Kinder oder in der Schwangerschaft?",
     "In der Schwangerschaft sprich bitte vorher mit deiner Ärztin oder deinem "
     "Arzt — das steht auch in Schritt 1. Dasselbe gilt bei Herz- oder "
     "Lungenerkrankungen, Epilepsie und sehr niedrigem Blutdruck."),
    ("Und wenn es mir nichts bringt?",
     "Dann schreibst du innerhalb von 7 Tagen und bekommst dein Geld zurück. "
     "Ohne Formular und ohne Begründung."),
]


def corpo():
    b = []
    A = b.append

    A('<header class="topbar"><div class="wrap topbar-in">'
      '<div class="brand"><span class="brand-mark">ATEM</span> Der Atemanker</div>'
      '<a href="#offer" class="btn btn-sm">Jetzt sichern</a></div></header>')

    # ---- HERO -------------------------------------------------------------
    A('<section class="hero"><div class="wrap hero-grid"><div class="hero-copy">'
      '<span class="eyebrow">7 Dateien · 2 Gratis-Boni · Sofort-Download</span>'
      '<h1>Du kannst dich nicht ruhig <i>denken</i>.<br>Aber du kannst dich ruhig '
      '<i>atmen</i>.</h1>'
      '<p class="lede">Die 2-Minuten-Methode, die deinem Körper das Signal gibt, '
      'aus dem Daueralarm auszusteigen. Im Sitzen, zu Hause, im Warmen — '
      '<b>ohne Eis, ohne Ausrüstung und ohne dass jemand im Raum etwas '
      'mitbekommt.</b></p>'
      '<div class="badges">'
      '<span class="badge"><svg class="i"><use href="#ic-book"/></svg><b>7</b> Dateien</span>'
      '<span class="badge"><svg class="i"><use href="#ic-gift"/></svg><b>2</b> Gratis-Boni</span>'
      '<span class="badge"><svg class="i"><use href="#ic-bolt"/></svg><b>2</b> Minuten pro Übung</span>'
      '<span class="badge"><svg class="i"><use href="#ic-calendar"/></svg><b>21</b>-Tage-Plan</span>'
      '</div></div>'
      '<div class="hero-art"><img class="book" src="capa-atem-800x1000.jpg" '
      'alt="Der Atemanker — die 2-Minuten-Methode gegen innere Unruhe"></div>'
      '<div class="hero-price">' + pricebox("#offer", "Sofort-Zugang holen") +
      '</div></div></section>')

    # ---- PROBLEMA ---------------------------------------------------------
    A('<section class="sec problem"><div class="wrap">'
      '<div class="center kicker"><span class="eyebrow">Warum bisher nichts geholfen hat</span>'
      '<h2>Du hast alles versucht, was im Kopf ansetzt.</h2></div>'
      '<ul class="was" style="margin-top:30px">%s</ul>'
      '<p class="lede" style="margin-top:26px"><b>Das Problem sitzt nicht im Kopf. '
      'Es sitzt im Körper</b> — und der hört keine Argumente. Er hört auf ein '
      'einziges Signal, und dieses Signal ist dein Ausatmen.</p>'
      '</div></section>'
      % "".join("<li>%s</li>" % p for p in PROBLEM))

    # ---- FEATURES ---------------------------------------------------------
    A('<section class="sec"><div class="wrap">'
      '<div class="center kicker"><span class="eyebrow">Die Methode</span>'
      '<h2>Eine Sache, die du änderst — und zwar die richtige</h2>'
      '<p class="lede">Nicht tiefer atmen. Nicht mehr atmen. Nur länger ausatmen '
      'als einatmen.</p></div>'
      '<div class="grid grid-3" style="margin-top:34px">%s</div>'
      '</div></section>'
      % "".join('<div class="card"><div class="ico"><svg class="i"><use href="#%s"/>'
                '</svg></div><b>%s</b><p>%s</p></div>' % c for c in CARDS))

    # ---- O QUE VEM (rail) -------------------------------------------------
    A('<section class="sec sec-white"><div class="wrap">'
      '<div class="center kicker"><span class="eyebrow">Alles, was drin ist</span>'
      '<h2>Sieben Dateien, in der Reihenfolge, in der du sie brauchst</h2>'
      '<p class="lede">Nummeriert von Schritt 1 bis Bonus 2 — du musst nie '
      'überlegen, was als Nächstes dran ist.</p></div>'
      '<div class="rail" style="margin-top:32px">%s</div>'
      '<p class="rail-hint"><svg class="i"><use href="#ic-swipe"/></svg>'
      'zum Weitersehen wischen</p></div></section>'
      % "".join('<div class="rcard"><img src="%s.jpg" alt="%s">'
                '<p><b>%s</b><br>%s</p></div>' % (f, t, t, d)
                for f, t, d in DATEIEN))

    # ---- CONTEUDO ---------------------------------------------------------
    A('<section class="sec"><div class="wrap"><div class="contentcard">'
      '<div class="head"><div class="ico"><svg class="i"><use href="#ic-book"/></svg></div>'
      '<h2 style="font-size:clamp(21px,3.2vw,28px)">Das bekommst du</h2></div>'
      '<ul class="ticks">'
      '<li><b>Die Grundübung</b> in ihren fünf Varianten — Stuhl, Schreibtisch, '
      'Gehen, Liegen und die Version für alle, denen sechs Sekunden zu lang sind</li>'
      '<li><b>Der Notfall-Anker:</b> neunzig Sekunden für den Akutmoment, plus '
      'eine Übung für nachts um drei</li>'
      '<li><b>Ein 21-Tage-Plan</b> mit einer einzigen Aufgabe pro Tag</li>'
      '<li><b>Eine komplette Abendroutine</b> für den Kopf, der abends lauter wird</li>'
      '<li><b>Bonus 1:</b> Kälte ohne Eis — drei Stufen am Waschbecken</li>'
      '<li><b>Bonus 2:</b> das Ruhe-Tagebuch zum Ausdrucken</li>'
      '<li>Alle Übungen mit <b>Foto und Atem-Diagramm</b>, damit du siehst, was du tust</li>'
      '<li>Zum Ausdrucken oder zum Lesen auf Handy, Tablet und Rechner</li>'
      '<li>Lebenslanger Zugang, einmal bezahlt</li>'
      '</ul></div></div></section>')

    # ---- BONUS ------------------------------------------------------------
    A('<section class="sec sec-white"><div class="wrap">'
      '<div class="center kicker"><span class="eyebrow">Kostenlos dabei</span>'
      '<h2>Zwei Boni, die du sonst einzeln kaufen müsstest</h2></div>'
      '<div class="grid grid-2" style="margin-top:34px">%s</div>'
      '<p class="center lede" style="margin-top:24px">Zusammen <b>33 €</b> wert. '
      'Heute im Paket enthalten.</p></div></section>'
      % "".join('<div class="card bonus"><span class="bonus-tag">Bonus %s</span>'
                '<div class="ico"><svg class="i"><use href="#%s"/></svg></div>'
                '<b>%s</b><p>%s</p><div class="val"><s>%s €</s> heute gratis</div>'
                '</div>' % bn for bn in BONI))

    # ---- COMO FUNCIONA ----------------------------------------------------
    A('<section class="sec"><div class="wrap">'
      '<div class="center kicker"><span class="eyebrow">So läuft es ab</span>'
      '<h2>Von hier bis zur ersten Übung sind es Minuten</h2></div>'
      '<div class="grid grid-3" style="margin-top:34px">%s</div>'
      '</div></section>'
      % "".join('<div class="step"><div class="n">%d</div><b>%s</b><p>%s</p></div>'
                % (i + 1, t, d) for i, (t, d) in enumerate(SCHRITTE)))

    # ---- OFERTA -----------------------------------------------------------
    A('<section class="sec sec-green" id="offer"><div class="wrap">'
      '<div class="center kicker" style="margin-bottom:32px">'
      '<span class="eyebrow">Das Angebot</span>'
      '<h2>Weniger als ein Kaffee und ein Stück Kuchen</h2>'
      '<p class="lede">Eine Zahlung. Sofortige Lieferung. Für immer deins.</p></div>'
      '<div class="offer"><h3>Das kommt in dein Postfach</h3>'
      '<ul class="ticks">'
      '<li><b>Der Atemanker</b> — das komplette Paket, sieben Dateien</li>'
      '<li>Die Grundübung mit fünf Alltags-Varianten</li>'
      '<li>Der Notfall-Anker für den Akutmoment</li>'
      '<li>Der 21-Tage-Plan mit Häkchen-Tabelle</li>'
      '<li>Die Abendroutine für ruhigere Nächte</li>'
      '<li><b>Bonus 1:</b> Kälte ohne Eis</li>'
      '<li><b>Bonus 2:</b> Dein Ruhe-Tagebuch zum Ausdrucken</li>'
      '<li>Sofort als Download, für immer deins</li></ul>'
      '<div class="rule"></div>' + precorow() +
      '<p class="once">Eine Zahlung. Kein Abo. Keine Verlängerung.</p>'
      '<a href="%s" class="btn btn-gold" style="margin-top:12px">Ja, ich will den '
      'Atemanker <svg class="i"><use href="#ic-arrow"/></svg></a>'
      '<p class="btn-note">Sicherer Hotmart-Checkout. Lieferung per E-Mail in '
      'wenigen Minuten.</p></div></div></section>' % CHECKOUT)

    # ---- GARANTIA ---------------------------------------------------------
    A('<section class="sec"><div class="wrap"><div class="guarantee">'
      '<div class="seal"><div><b>7</b><span>Tage</span></div></div><div>'
      '<h2 style="font-size:clamp(22px,3.4vw,30px)">Probier es eine Woche lang '
      'aus. Auf unsere Kosten.</h2>'
      '<p style="color:var(--ink-soft);margin-top:12px">Kauf es, lade es herunter '
      'und üb sieben Tage lang. Wenn es dir nichts bringt, schreibst du uns und '
      'bekommst dein Geld zurück — ohne Formular, ohne Begründung, ohne '
      'Rückfragen. Die Dateien liegen längst auf deinem Gerät, und dort bleiben '
      'sie auch.</p>'
      '<p style="color:var(--ink-soft);margin-top:12px;font-weight:700">Das '
      'Einzige, was du hier riskieren kannst, sind zwei Minuten.</p>'
      '</div></div></div></section>')

    # ---- HONESTIDADE (no lugar de depoimento inventado) -------------------
    A('<section class="sec sec-white"><div class="wrap">'
      '<div class="center kicker"><span class="eyebrow">Fair bleiben</span>'
      '<h2>Was dieses Paket <i>nicht</i> verspricht</h2>'
      '<p class="lede">Wer ständig unruhig ist, wurde schon genug versprochen. '
      'Deshalb hier zuerst das, was wir nicht behaupten.</p></div>'
      '<div class="grid grid-2" style="margin-top:34px">%s</div>'
      '</div></section>'
      % "".join('<div class="card"><b>%s</b><p>%s</p></div>' % n for n in NICHT))

    # ---- FAQ --------------------------------------------------------------
    A('<section class="sec"><div class="wrap">'
      '<div class="center kicker" style="margin-bottom:32px">'
      '<span class="eyebrow">Fragen</span><h2>Bevor du dich entscheidest</h2></div>'
      '%s</div></section>'
      % "".join('<details class="faq"><summary>%s</summary><p>%s</p></details>'
                % (q, a) for q, a in FRAGEN))

    # ---- CTA FINAL --------------------------------------------------------
    A('<section class="sec-tight sec-green center"><div class="wrap">'
      '<h2>Zwei Minuten. Heute noch.</h2>'
      '<p class="lede" style="margin:12px auto 0;max-width:560px">Du brauchst '
      'keinen freien Nachmittag und nichts Kaltes. Nur einen Stuhl.</p>'
      '<a href="%s" class="btn btn-gold" style="margin-top:22px;max-width:420px">'
      'Den Atemanker sichern — 10 € <svg class="i"><use href="#ic-arrow"/></svg></a>'
      '</div></section>' % CHECKOUT)

    # ---- RODAPE -----------------------------------------------------------
    A('<footer><div class="wrap">'
      '<div class="brand"><span class="brand-mark">ATEM</span> Der Atemanker</div>'
      '<p>© 2026. Alle Rechte vorbehalten.</p>'
      '<p class="fine" style="margin-top:16px">Dieses Paket dient der allgemeinen '
      'Information und ersetzt keine ärztliche oder psychotherapeutische '
      'Beratung. Es stellt keine Diagnose und ist kein Medikament. Bei '
      'Schwangerschaft, Herz- oder Lungenerkrankungen, Epilepsie oder sehr '
      'niedrigem Blutdruck sprich bitte vorher mit deiner Ärztin oder deinem '
      'Arzt. Atemübungen niemals im oder am Wasser und niemals am Steuer. '
      'Ergebnisse sind von Person zu Person unterschiedlich.</p>'
      '</div></footer>')

    return "\n".join(b)


def precorow():
    return ('<div class="pricehead"><span>Statt <s>%s €</s></span>'
            '<span class="save">%s sparen</span></div>'
            '<div class="price-row"><span class="now"><span class="cur">€</span>10'
            '<span class="cents">,00</span></span></div>' % (PRECO_DE, DESCONTO))


def pricebox(href, label):
    return ('<div class="pricebox">' + precorow() +
            '<p class="once">Einmalzahlung. Für immer deins. Kein Abo.</p>'
            '<a href="%s" class="btn">%s <svg class="i"><use href="#ic-arrow"/>'
            '</svg></a><div class="pay">'
            '<span><svg class="i"><use href="#ic-lock"/></svg>Sicherer Hotmart-Checkout</span>'
            '<span><svg class="i"><use href="#ic-mail"/></svg>Per E-Mail zugesendet</span>'
            '<span><svg class="i"><use href="#ic-return"/></svg>7 Tage Garantie</span>'
            '</div></div>' % (href, label))


EXTRA = """
/* ⛔ O CSS de referencia so' clareia `.lede` e `.eyebrow` dentro de
   `.sec-green` — dentro de `.problem` (fundo --ink, quase preto) eles ficam
   com a cor clara padrao --ink-soft, que e' cinza ESCURO. Medido aqui:
   rgb(84,82,78) sobre rgb(26,26,26), ou seja, texto invisivel. A landing de
   referencia nunca pos um `.lede` dentro do bloco escuro e por isso nunca
   pagou por isso; esta pos. */
.problem .lede{color:rgba(255,255,255,.88)}
.problem .eyebrow{color:#fff;background:rgba(255,255,255,.16)}
.problem .lede b{color:#fff}

h1 i{font-style:normal;color:var(--green);font-weight:900}
.sec-green h2 i,.problem h2 i{font-style:normal;color:var(--gold)}
.sec-white h2 i{font-style:normal;color:var(--green)}
.was{list-style:none;margin:0;padding:0;display:grid;gap:13px;max-width:760px}
.was li{position:relative;padding-left:30px;font-size:16.5px;line-height:1.6;
color:rgba(255,255,255,.9)}
.was li::before{content:"";position:absolute;left:0;top:9px;width:11px;height:11px;
border-radius:3px;background:var(--gold)}
.rcard p b{color:var(--ink);font-weight:800}
details.faq{border-top:1px solid var(--line);padding:16px 0}
details.faq summary{font-size:17.5px;font-weight:800;color:var(--ink);cursor:pointer;
list-style:none;position:relative;padding-right:28px}
details.faq summary::-webkit-details-marker{display:none}
details.faq summary::after{content:"+";position:absolute;right:4px;top:-2px;
font-size:24px;color:var(--green);font-weight:700}
details.faq[open] summary::after{content:"–"}
details.faq p{margin-top:10px;color:var(--ink-soft);font-size:16.5px;line-height:1.65}
.card b{display:block;font-size:18px;line-height:1.3}
"""


def main():
    css, defs = _ref_css_e_icones()
    doc = ("""<!doctype html><html lang="de"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Der Atemanker — die 2-Minuten-Methode gegen innere Unruhe</title>
<meta name="description" content="Zwei Minuten, die deinem Körper sagen, dass die Gefahr vorbei ist. Sieben Dateien, ein 21-Tage-Plan, zwei Boni. Ohne Eis, ohne Ausrüstung, zu Hause.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<style>%s
%s</style></head><body>
%s
%s
</body></html>""" % (css, EXTRA, defs, corpo()))

    saida = os.path.join(AQUI, "index.html")
    io.open(saida, "w", encoding="utf-8").write(doc)
    print("LANDING: %s  (%.0f KB)" % (saida, os.path.getsize(saida) / 1024))

    # imagens que a pagina referencia
    precisa = ["capa-atem-800x1000.jpg"] + ["%s.jpg" % f for f, _, _ in DATEIEN]
    # ⛔ As fotos do ebook tem 1024px e ~650 KB cada. Numa landing isso e' 4,6 MB
    # de imagem para cards que aparecem com 3:4 e algumas centenas de pixels —
    # peso que o comprador paga em segundos de espera e o anuncio paga em
    # abandono. Elas entram redimensionadas; a capa fica como esta'.
    from PIL import Image
    for n in precisa:
        capa = n.startswith("capa")
        orig = os.path.join(FOTOS, n) if capa else os.path.join(FOTOS, "fotos", n)
        dst = os.path.join(AQUI, n)
        if not os.path.exists(orig):
            print("  !! FALTA:", orig)
            continue
        if capa:
            shutil.copy2(orig, dst)
        else:
            im = Image.open(orig).convert("RGB")
            im.thumbnail((620, 620), Image.LANCZOS)
            im.save(dst, quality=82, optimize=True)
    faltam = [n for n in precisa if not os.path.exists(os.path.join(AQUI, n))]
    print("  imagens: %d/%d presentes%s"
          % (len(precisa) - len(faltam), len(precisa),
             "  FALTAM: " + " ".join(faltam) if faltam else ""))
    return saida


if __name__ == "__main__":
    main()
