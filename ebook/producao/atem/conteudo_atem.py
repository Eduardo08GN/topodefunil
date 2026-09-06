# -*- coding: utf-8 -*-
"""CONTEUDO — DER ATEMANKER (alemao). DADOS, nao apresentacao.

⛔ Este arquivo so' DESCREVE. Quem renderiza e' o `motor_atem`, e quem monta os
PDFs e' o `build_atem`. Mesma separacao do motor de receitas.

⛔⛔ TRES TRAVAS ATRAVESSAM TODO O TEXTO, e nenhuma e' estilo:
  1. SEM HIPERVENTILACAO. Nenhum exercicio pede respirar fundo muitas vezes
     seguidas nem segurar o ar vazio. O mecanismo e' expiracao mais longa.
  2. AGUA NUNCA. Nada de respiracao dentro de banheira, piscina ou lago —
     `GE4` do `gelo16_short.py`. O bonus do frio e' de pia e chuveiro.
  3. SEM DIAGNOSTICO E SEM CURA (HWG alemao). A moldura e' `Nervensystem im
     Daueralarm` -> `Regulation in Minuten`. Quem esta' em crise aguda e'
     mandado ao medico por escrito, como a propria pagina do concorrente faz.

⭐ O nome do mecanismo e' `Der Atemanker`, escolha do operador entre tres
propostas. Ele puxa a keyword `ATEM` que ja' esta' cadastrada na automacao de
DM do funil (ver `gelo16_short.py`), e por isso o produto e o comentario do
video falam a mesma palavra.
"""

MARCA = "Der Atemanker"
SUB_MARCA = "Zwei Minuten, die deinem Körper sagen, dass die Gefahr vorbei ist."

# ===========================================================================
# TEXTOS QUE SE REPETEM — constante, nunca redigitada (regra do playbook)
# ===========================================================================

SICHERHEIT_KURZ = (
    "Setz dich hin oder leg dich hin. Nie im Stehen, nie am Steuer, nie im "
    "oder am Wasser. Wenn dir schwindelig wird, hörst du auf und atmest "
    "ganz normal weiter."
)

# ⛔ DUAS VERSOES DA MESMA TRAVA, e a diferenca e' de TAMANHO, nao de forca.
# A longa e' didatica e mora onde ha' espaco para ler: a pagina de seguranca do
# Schritt 1 e as regras do Bonus 1. A curta e' a que vai no rodape de cada card
# de exercicio — o paragrafo inteiro empurrava a caixa vermelha sozinha para a
# pagina seguinte (4 orfas medidas), e ordem curta em card se le', paragrafo
# nao. Nenhum card fica sem a trava.
WASSER_TRAVA = (
    "Niemals im Wasser. Keine Badewanne, kein Pool, kein See — auch nicht "
    "im flachen Wasser und auch nicht mit jemandem daneben. Atemübungen und "
    "Wasser gehören nicht zusammen, und dieser Satz steht in jeder Datei, "
    "weil er der wichtigste im ganzen Paket ist."
)

WASSER_KURZ = "Nie im oder am Wasser — keine Wanne, kein Pool, kein See."

# ===========================================================================
# SCHRITT 1 — FANG HIER AN
# ===========================================================================

S1 = {
    "badge": "Schritt 1",
    "titel": "Fang hier an",
    "lead": ("Zehn Minuten Lesen, und du weißt, was du in den nächsten "
             "drei Wochen tust — und warum es funktioniert. Danach brauchst "
             "du nie wieder mehr als zwei Minuten am Stück."),
    "foto": "persona",

    "willkommen_titel": "Schön, dass du da bist",
    "willkommen_sub": ("Bevor du irgendetwas übst, ein paar Sätze darüber, "
                       "was du gekauft hast und was nicht."),
    "willkommen": [
        "Du hast kein Kursvideo gekauft, das du nie zu Ende schaust. Du hast eine "
        "<b>Handvoll Dateien</b> gekauft, die du ausdrucken, auf dem Handy lesen und "
        "neben das Bett legen kannst.",
        "Der ganze Inhalt dreht sich um <b>eine einzige Sache</b>: länger auszuatmen, "
        "als du einatmest. Das klingt zu klein, um etwas zu ändern. Es ist trotzdem "
        "das, was deinem Körper am schnellsten sagt, dass er runterfahren darf.",
        "Alles andere in diesem Paket — die Haltung, der Plan, der Abend, das "
        "kalte Wasser — hängt an diesem einen Satz.",
        "<b>Und es dauert wirklich zwei Minuten.</b> Nicht zwanzig. Zwei. Wer keine "
        "zwanzig Minuten hat, ist genau die Person, für die das hier gebaut wurde.",
    ],

    "paket_titel": "Was in diesem Paket steckt",
    "paket_sub": "Sieben Dateien, in genau dieser Reihenfolge nummeriert.",
    "paket": [
        ("Schritt 1", "Fang hier an", "Die Datei, die du gerade liest. Wie dein "
         "Körper Alarm macht, warum das Ausatmen ihn abstellt, und die "
         "Sicherheitsregeln."),
        ("Schritt 2", "Der Atemanker", "Die Grundübung. Haltung, Hand auf den "
         "Rippen, der Rhythmus 4–6 — und fünf Varianten für Schreibtisch, "
         "Weg zur Arbeit und Warteschlange."),
        ("Schritt 3", "Der Notfall-Anker", "Was du machst, wenn es dich gerade "
         "erwischt. Neunzig Sekunden, im Sitzen, ohne dass jemand etwas merkt."),
        ("Schritt 4", "Dein 21-Tage-Plan", "Tag für Tag, mit einer Aufgabe pro "
         "Tag. Das ist der Teil, der aus einer Übung eine Gewohnheit macht."),
        ("Schritt 5", "Die Abendroutine", "Für den Kopf, der abends lauter wird "
         "als tagsüber, und für die Nächte, in denen du um drei wach liegst."),
        ("Bonus 1", "Kälte ohne Eis", "Der kleine Verstärker: kaltes Wasser am "
         "Handgelenk, am Gesicht, am Ende der Dusche. Freiwillig, und nie "
         "zusammen mit den Atemübungen."),
        ("Bonus 2", "Dein Ruhe-Tagebuch", "Vorlagen zum Ausdrucken. Nach drei "
         "Wochen siehst du schwarz auf weiß, was sich verändert hat — und "
         "was dich zuverlässig hochfahren lässt."),
    ],

    "alarm_titel": "Warum dein Körper Alarm macht, obwohl nichts passiert",
    "alarm_sub": ("Der kurze, ehrliche Teil Biologie. Danach kommt nur noch Üben."),
    "alarm": [
        "In deinem Körper läuft ein Teil des Nervensystems, um den du dich nie "
        "kümmern musst. Er regelt den Herzschlag, die Verdauung, die Weite deiner "
        "Blutgefäße. Du entscheidest das nicht — es passiert einfach.",
        "Dieser Teil hat zwei Betriebsarten. Die eine macht dich bereit zu "
        "handeln: Herz schneller, Muskeln angespannt, Atem hoch und flach in der "
        "Brust. Die andere macht das Gegenteil: Puls runter, Verdauung an, Atem "
        "tief und langsam in den Bauch.",
        "Bei vielen Menschen bleibt der erste Modus <b>an</b>, auch wenn gar keine "
        "Gefahr da ist. Kein Tier, kein Feuer, kein Angriff — nur eine E-Mail, "
        "eine Rechnung, ein Gedanke um 23 Uhr. Der Körper macht trotzdem das "
        "volle Programm.",
        "<b>Und hier ist der Punkt, an dem du eingreifen kannst.</b> Von all den "
        "Dingen, die dieses System steuert, gibt es genau eines, das du auch "
        "bewusst übernehmen kannst: <b>den Atem</b>. Du kannst deinen Puls nicht "
        "direkt befehlen. Deine Verdauung auch nicht. Deinen Atem schon.",
        "Der Atem ist die Tür. Deshalb geht es in diesem ganzen Paket nur um ihn.",
    ],

    "ausatmen_titel": "Warum ausgerechnet das Ausatmen",
    "ausatmen_sub": ("Die eine Idee, auf der alles andere steht."),
    "ausatmen": [
        "Wenn du <b>einatmest</b>, wird dein Herzschlag ein Stück schneller. Wenn du "
        "<b>ausatmest</b>, wird er langsamer. Das ist kein Gefühl, das kann man messen, "
        "und es passiert bei jedem Menschen bei jedem Atemzug.",
        "Daraus folgt etwas sehr Einfaches: <b>Je mehr Zeit du mit Ausatmen "
        "verbringst, desto mehr Zeit verbringt dein Herz im langsameren Modus.</b>",
        "Genau das machen wir. Wir atmen nicht tiefer, nicht schneller, nicht mehr. "
        "Wir verschieben nur das Verhältnis: <b>kurz rein, lang raus.</b>",
        "In der Grundübung sind das vier Sekunden ein und sechs Sekunden aus. "
        "Zehn Sekunden pro Atemzug, sechs Atemzüge in der Minute. Die meisten "
        "Menschen atmen in Ruhe zwölf bis sechzehn Mal pro Minute — du gehst "
        "also auf etwa die Hälfte runter.",
    ],
    "ausatmen_merk": ("Alles, was du dir merken musst, ist dieser eine Satz: "
                      "<b>Das Ausatmen ist länger als das Einatmen.</b> Wenn du den "
                      "Rest des Pakets vergisst und nur den behältst, hast du "
                      "schon das meiste."),

    "ehrlich_titel": "Ehrliche Hinweise",
    "ehrlich_sub": ("Was dieses Paket kann — und was es ausdrücklich nicht kann."),
    "ehrlich": [
        ("Das ist keine Behandlung.", "Der Atemanker ist eine Übung, keine "
         "Therapie und kein Medikament. Er ersetzt weder Ärztin noch "
         "Psychotherapie, und er stellt keine Diagnose."),
        ("Setz nichts ab.", "Wenn du Medikamente nimmst, nimmst du sie weiter. "
         "Über Veränderungen entscheidet die Person, die sie dir "
         "verschrieben hat — nicht ein PDF."),
        ("Einmal reicht nicht.", "Beim ersten Mal passiert oft: nichts. Das ist "
         "normal. Der Effekt kommt aus der Wiederholung, nicht aus dem "
         "einzelnen Versuch. Deshalb gibt es den 21-Tage-Plan."),
        ("Es wird nicht alles still.", "Wir versprechen dir keinen leeren Kopf "
         "und kein Leben ohne Anspannung. Das Ziel ist kleiner und ehrlicher: "
         "schneller wieder runterkommen als vorher."),
        ("Du spürst es zuerst im Körper.", "Die meisten merken zuerst warme "
         "Hände, lockere Schultern oder ein tieferes Gähnen — nicht "
         "einen ruhigeren Kopf. Der Kopf kommt danach."),
    ],

    "sicher_titel": "Sicherheit — bitte einmal ganz lesen",
    "sicher_sub": ("Eine Seite. Sie ist wichtiger als jede Übung im Paket."),
    "sicher_regeln": [
        "<b>Immer im Sitzen oder Liegen.</b> Nie im Stehen üben. Wenn dir "
        "schwindelig wird, sitzt du schon.",
        "<b>Nie am Steuer.</b> Nicht im fahrenden Auto, nicht auf dem Rad, nicht "
        "auf einer Leiter, nicht an einer Maschine.",
        "<b>Nie im oder am Wasser.</b> Keine Badewanne, kein Pool, kein See. Auch "
        "nicht flach, auch nicht mit jemandem daneben.",
        "<b>Hör auf, wenn es kippt.</b> Schwindel, Kribbeln in Händen oder "
        "Lippen, Herzrasen, ein Druck auf der Brust: Du beendest die Übung und "
        "atmest ganz normal weiter. Das ist kein Scheitern, das ist Aufpassen.",
        "<b>Zwing nichts.</b> Wenn sechs Sekunden Ausatmen sich eng anfühlen, "
        "nimmst du fünf. Oder vier. Eine Übung, die dich anstrengt, macht "
        "das Gegenteil von dem, wofür sie da ist.",
    ],
    "sicher_arzt": (
        "<b>Sprich vorher mit deiner Ärztin oder deinem Arzt</b>, wenn du "
        "schwanger bist, eine Herz- oder Lungenerkrankung hast, unter Epilepsie "
        "leidest, sehr niedrigen Blutdruck hast, oder wenn du wegen einer "
        "psychischen Erkrankung in Behandlung bist."
    ),
    "sicher_krise": (
        "<b>Wenn es dir gerade akut sehr schlecht geht</b> — wenn du in einer "
        "seelischen Krise steckst oder Gedanken hast, dir etwas anzutun — dann "
        "ist dieses Paket nicht der richtige nächste Schritt. Hol dir "
        "Unterstützung bei einem Menschen. In Deutschland ist die "
        "Telefonseelsorge rund um die Uhr kostenlos erreichbar: "
        "<b>0800 111 0 111</b> und <b>0800 111 0 222</b>. In Österreich: "
        "<b>142</b>. In der Schweiz: <b>143</b>."
    ),

    "los_titel": "So gehst du jetzt vor",
    "los_sub": "Vier Sätze, dann bist du hier fertig.",
    "los": [
        "Lies als Nächstes <b>Schritt 2</b> und mach die Grundübung einmal mit. "
        "Das dauert keine fünf Minuten.",
        "Sieh dir <b>Schritt 3</b> heute noch an, auch wenn du ihn gerade nicht "
        "brauchst. Man liest keine Anleitung, während es brennt.",
        "Starte morgen früh mit <b>Schritt 4</b>, Tag 1. Nicht heute Abend noch "
        "schnell — morgen, mit Tag 1.",
        "<b>Schritt 5</b> und die beiden Bonus-Dateien kommen dazu, wenn der Plan "
        "sie dir sagt. Du musst sie nicht vorher lesen.",
    ],
    "los_drucken": (
        "<b>Ein Tipp, der wirklich etwas ändert:</b> Druck dir aus Schritt 3 die "
        "Seite mit dem Notfall-Anker aus und leg sie irgendwohin, wo du sie ohne "
        "Suchen findest — Nachttisch, Handtasche, Schreibtischschublade. Im "
        "Moment selbst tippt niemand einen Dateinamen."
    ),
}

# ===========================================================================
# SCHRITT 2 — DER ATEMANKER (a grande licao)
# ===========================================================================

S2 = {
    "badge": "Schritt 2",
    "titel": "Der Atemanker",
    "lead": ("Die Grundübung, und fünf Varianten für den Alltag. Wenn du "
             "nur eine Datei aus diesem Paket behalten dürftest, wäre es "
             "diese."),
    "foto": "rippen",

    "drei_titel": "Die drei Anker",
    "drei_sub": ("Ein Anker hält ein Schiff an einer Stelle, während um es "
                 "herum alles in Bewegung bleibt. Genau das machen diese drei."),
    "drei": [
        ("Der Körperanker", "Wie du sitzt. Ein Körper, der zusammengesackt "
         "ist, bekommt die Luft gar nicht nach unten. Deshalb fangen wir bei der "
         "Haltung an und nicht beim Atem."),
        ("Der Atemanker", "Der Rhythmus: vier Sekunden ein, sechs Sekunden aus. "
         "Das ist das Herzstück, und der Rest des Pakets sind Varianten davon."),
        ("Der Blickanker", "Wohin die Aufmerksamkeit geht, während du atmest. "
         "Ohne diesen dritten Anker zählst du mit und denkst gleichzeitig über "
         "morgen nach — und dann wirkt es nur halb."),
    ],

    "uebungen": [
        {
            "tag": "Grundlage",
            "nome": "Die Haltung",
            "hook": ("Bevor du einen einzigen Atemzug änderst: So sitzt du, damit "
                     "die Luft überhaupt nach unten kann."),
            "foto": "haltung",
            "stats": [("1 Min", "Dauer"), ("Stuhl", "Ort"), ("Täglich", "Wie oft")],
            "ritmo": None,
            "schritte": [
                "Setz dich auf die <b>vordere Hälfte</b> eines Stuhls. Nicht angelehnt, "
                "aber auch nicht steif — du sollst bequem sitzen, nicht stramm stehen.",
                "Beide <b>Füße flach auf den Boden</b>, ungefähr hüftbreit "
                "auseinander. Wenn deine Füße nicht ankommen, stell ein Buch drunter.",
                "<b>Becken leicht nach vorn kippen</b>, so dass du auf den Sitzbeinhöckern "
                "sitzt und nicht auf dem Steißbein. Der untere Rücken bekommt dadurch "
                "seine natürliche Kurve zurück.",
                "<b>Schultern einmal hochziehen, kurz halten, fallen lassen.</b> Zweimal. "
                "Wo sie danach landen, ist die richtige Stelle.",
                "<b>Kinn minimal Richtung Brust</b>, als würdest du eine Walnuss unter "
                "dem Kinn halten. Der Nacken wird dadurch lang.",
                "<b>Hände locker auf die Oberschenkel.</b> Fertig. So sitzt du bei "
                "jeder Übung in diesem Paket.",
            ],
            "worauf": ("Wenn du richtig sitzt, geht dein Bauch beim Einatmen von "
                       "allein ein Stück nach vorn — ohne dass du irgendetwas "
                       "drückst. Passiert das nicht, sackst du wahrscheinlich noch "
                       "im unteren Rücken zusammen."),
            "sicher": None,
        },
        {
            "tag": "Grundlage",
            "nome": "Die Hand auf den Rippen",
            "hook": ("Die meisten Menschen atmen oben in der Brust. Diese Übung "
                     "zeigt dir in zwei Minuten, ob du dazugehörst."),
            "foto": "rippen",
            "stats": [("2 Min", "Dauer"), ("Sitzen", "Haltung"), ("Einmal", "Zum Testen")],
            "ritmo": None,
            "schritte": [
                "Setz dich wie in der Übung davor.",
                "Leg eine <b>Hand flach auf die unteren Rippen</b>, seitlich, da wo der "
                "Brustkorb schmaler wird. Die andere Hand auf den Bauch.",
                "Atme <b>ganz normal</b> weiter. Nicht tiefer, nicht bewusster. Nur "
                "normal, und beobachte fünf oder sechs Atemzüge lang.",
                "<b>Welche Hand bewegt sich mehr?</b> Wenn es die obere ist, atmest du "
                "in die Brust — das machen die meisten, und es ist genau die Atmung, "
                "die dein Körper im Alarmzustand benutzt.",
                "Jetzt lenkst du die Luft <b>nach unten</b>: Stell dir vor, du atmest in "
                "deine Hand an den Rippen hinein und schiebst sie leicht nach außen.",
                "Fünf Atemzüge so. Die Schultern bleiben unten — wenn sie "
                "hochgehen, atmest du wieder oben.",
            ],
            "worauf": ("Richtig ist es, wenn sich die Rippen <b>seitlich</b> weiten, wie "
                       "ein Blasebalg, und die Schultern still bleiben. Das ist die "
                       "Atmung, die du in allen weiteren Übungen benutzt."),
            "sicher": None,
        },
        {
            "tag": "Die Hauptübung",
            "nome": "Der Atemanker 4–6",
            "hook": ("Das ist er. Zwei Minuten, zwölf Atemzüge, und du brauchst "
                     "nichts außer einem Stuhl."),
            "foto": "anker",
            "stats": [("2 Min", "Dauer"), ("12", "Atemzüge"), ("6 / Min", "Frequenz")],
            "ritmo": (4, 6, 0, 3),
            "schritte": [
                "Sitz wie in Übung 1. Eine Hand darf an den Rippen liegen, das hilft "
                "am Anfang.",
                "<b>Atme durch die Nase ein und zähle innerlich bis vier.</b> Nicht "
                "maximal voll — etwa drei Viertel. Voll gepumpt ist unangenehm und "
                "macht das Gegenteil.",
                "<b>Atme durch die Nase wieder aus und zähle bis sechs.</b> Lass die "
                "Luft eher raus, als dass du sie rausdrückst. Am Ende ist noch Luft "
                "drin, und das soll auch so sein.",
                "<b>Keine Pause.</b> Wenn die sechs vorbei sind, beginnt der nächste "
                "Einatemzug direkt. Kein Anhalten, weder voll noch leer.",
                "<b>Der Blickanker:</b> Such dir <b>eine</b> Sache, bei der du bleibst — "
                "die Zahlen, das Gefühl der Luft an den Nasenlöchern, oder die Hand "
                "an den Rippen. Eine, nicht drei.",
                "<b>Zwölf Atemzüge.</b> Das sind zwei Minuten. Dann hörst du "
                "auf und atmest normal weiter — auch wenn es gerade schön ist.",
            ],
            "worauf": ("Warme Hände. Ein tiefes Gähnen. Schultern, die "
                       "plötzlich tiefer hängen als vorher. Ein Schlucken. Das "
                       "sind die Zeichen, dass der ruhige Modus angesprungen ist — "
                       "und sie kommen fast immer vor dem Gefühl, ruhig zu sein."),
            "sicher": SICHERHEIT_KURZ + " " + WASSER_KURZ,
        },
        {
            "tag": "Variante",
            "nome": "Wenn sechs zu lang sind",
            "hook": ("Für alle, bei denen sich das lange Ausatmen erst mal eng "
                     "anfühlt. Das ist häufig und kein schlechtes Zeichen."),
            "foto": "nase",
            "stats": [("2 Min", "Dauer"), ("3→4", "Start"), ("1 Woche", "Aufbau")],
            "ritmo": (3, 4, 0, 3),
            "schritte": [
                "Fang mit <b>drei ein, vier aus</b> an. Das Verhältnis stimmt schon — "
                "raus ist länger als rein — und darauf kommt es an.",
                "Bleib zwei, drei Tage dabei, bis es sich mühelos anfühlt.",
                "Dann geh auf <b>drei ein, fünf aus</b>. Wieder ein paar Tage.",
                "Dann <b>vier ein, sechs aus</b>. Das ist die Zielform.",
                "Wenn ein Tag mal schlechter läuft, gehst du einen Schritt "
                "zurück. Das ist erlaubt und passiert jedem.",
            ],
            "worauf": ("Der Aufbau ist kein Trostpreis. Ein Rhythmus, den du drei "
                       "Wochen lang hältst, wirkt mehr als einer, der beeindruckend "
                       "aussieht und den du nach vier Tagen aufgibst."),
            "sicher": ("Zwing die Zahl nie. Wenn du am Ende des Ausatmens nach Luft "
                       "schnappen musst, ist das Intervall zu lang — nimm eine "
                       "Sekunde weniger."),
        },
        {
            "tag": "Alltag",
            "nome": "Der Anker am Schreibtisch",
            "hook": ("Die Version, die niemand im Raum bemerkt. Kein Augenschließen, "
                     "keine Handbewegung, kein Geräusch."),
            "foto": "schreibtisch",
            "stats": [("90 Sek", "Dauer"), ("Unsichtbar", "Für andere"), ("2–3x", "Am Tag")],
            "ritmo": (4, 6, 0, 3),
            "schritte": [
                "<b>Augen bleiben offen</b> und auf dem Bildschirm oder auf einem Punkt "
                "am Tisch. Niemand sieht etwas.",
                "<b>Beide Füße flach auf den Boden</b> und ganz leicht in den Boden "
                "drücken. Das ist dein Körperanker im Sitzen — unauffällig und "
                "wirksam.",
                "Nimm die <b>Hände von der Tastatur</b> und leg sie auf die "
                "Oberschenkel. Das allein senkt die Schultern.",
                "Neun Atemzüge im Rhythmus <b>4–6</b>, durch die Nase, ohne Ton.",
                "<b>Der Blickanker sind hier die Füße</b>, nicht die Zahlen — "
                "spür den Boden unter den Sohlen, während du zählst.",
            ],
            "worauf": ("Der beste Zeitpunkt ist <b>vor</b> dem schwierigen Termin, nicht "
                       "danach. Zwei Minuten vorher kosten dich nichts und "
                       "verändern, mit welcher Stimme du reingehst."),
            "sicher": None,
        },
        {
            "tag": "Alltag",
            "nome": "Der Anker im Gehen",
            "hook": ("Für Menschen, die im Sitzen unruhig werden. Der Körper "
                     "bewegt sich, der Rhythmus bleibt."),
            "foto": "gehen",
            "stats": [("5 Min", "Dauer"), ("Draußen", "Ort"), ("Schritte", "Der Takt")],
            "ritmo": (4, 6, 0, 3),
            "schritte": [
                "Geh in einem <b>ruhigen, gleichmäßigen Tempo</b>. Kein Sport, kein "
                "Ziel, keine Uhr.",
                "Statt Sekunden zählst du <b>Schritte</b>: vier Schritte lang einatmen, "
                "sechs Schritte lang ausatmen.",
                "Wenn das nicht aufgeht, geh langsamer. <b>Der Atem gibt den Takt vor, "
                "nicht die Beine.</b>",
                "Durch die Nase, auch im Gehen. Wenn das nicht klappt, bist du zu "
                "schnell unterwegs.",
                "Fünf Minuten reichen. Danach gehst du normal weiter.",
            ],
            "worauf": ("Diese Variante ist die beste für unruhige Tage. Wenn Sitzen "
                       "sich anfühlt wie Stillhalten unter Strom, ist Gehen kein "
                       "Rückschritt, sondern der passendere Weg."),
            "sicher": ("Nur dort, wo du auf nichts achten musst. Nicht an einer "
                       "Straße, nicht mit Kopfhörern im Verkehr, und nicht am "
                       "Wasser — kein Ufer, kein Steg, kein Beckenrand."),
        },
    ],

    "fehler_titel": "Die fünf häufigsten Fehler",
    "fehler_sub": ("Wenn die Übung sich unangenehm anfühlt, steht der Grund "
                   "fast immer in dieser Liste."),
    "fehler": [
        ("Zu voll einatmen.", "Der häufigste Fehler von allen. „Tief atmen“ "
         "heißt nicht „viel atmen“. Etwa drei Viertel voll reicht — "
         "randvoll erzeugt genau den Druck auf der Brust, den du loswerden willst."),
        ("Die Luft anhalten.", "Weder oben noch unten. Sobald das Einatmen fertig "
         "ist, beginnt das Ausatmen, und umgekehrt. Anhalten macht viele Menschen "
         "unruhiger, nicht ruhiger."),
        ("Durch den Mund atmen.", "Die Nase wärmt und bremst die Luft. Durch den "
         "Mund geht zu viel zu schnell rein. Ausnahme ist der Notfall-Anker in "
         "Schritt 3, und dort steht auch, warum."),
        ("Mit den Schultern atmen.", "Wenn deine Schultern bei jedem Einatmen "
         "hochwandern, atmest du oben in der Brust. Geh zurück zur Hand auf den "
         "Rippen, bis die Bewegung wieder unten passiert."),
        ("Es zu lange machen.", "Zwölf Atemzüge, dann Schluss. Zwanzig Minuten "
         "am Stück sind nicht besser — sie sind nur das, was du nächste "
         "Woche nicht mehr machst."),
    ],

    "faq": [
        ("Ich muss dauernd gähnen. Mache ich etwas falsch?",
         "Im Gegenteil. Gähnen, Seufzen und Schlucken tauchen genau dann auf, "
         "wenn der Körper vom Alarm- in den Ruhemodus wechselt. Lass es zu."),
        ("Ich verliere ständig die Zählung.",
         "Das ist normal und kein Problem. Wenn du merkst, dass du weg warst, "
         "fängst du beim nächsten Einatmen wieder bei eins an. Das Bemerken "
         "ist der Übungsteil, nicht das Durchhalten."),
        ("Muss ich die Augen schließen?",
         "Nein. Manche Menschen werden mit geschlossenen Augen unruhiger, weil die "
         "Gedanken dann lauter sind. Ein weicher Blick auf einen festen Punkt "
         "funktioniert genauso gut."),
        ("Wann am Tag ist es am besten?",
         "Morgens, weil du dann noch nicht ausdiskutieren kannst, ob du Lust hast. "
         "Der Plan in Schritt 4 hängt es deshalb an etwas, das du sowieso jeden "
         "Morgen tust."),
        ("Kann ich es öfter als zweimal machen?",
         "Ja, so oft du magst — solange es kurz bleibt. Sechs Mal zwei Minuten "
         "über den Tag verteilt ist besser als einmal zwölf Minuten."),
    ],
}


# ===========================================================================
# ⭐ ROTULOS FIXOS DA INTERFACE — o que nao e' conteudo, e' cromo.
# ⛔ Eles moram AQUI, no modulo de dados do idioma, e nao no motor nem no
# builder. Foi o que permitiu o frances reusar `motor_atem` e `build_atem`
# inteiros: uma ferramenta por funcao, dados por idioma.
# ===========================================================================

ROT = {
    "merk": "Woran du merkst, dass es wirkt",
    "stop": "Sicherheit",
    "faq": "Häufige Fragen",
    "tag": "TAG",
    "anker": "ANKER",
    "s1_satz": "Der eine Satz",
    "s1_arzt": "Vorher fragen",
    "s1_krise": "Akute Krise",
    "s1_druck": "Ausdrucken",
    "s3_real": "Realistisch bleiben",
    "s3_notruf": "Wann es kein Fall für eine Atemübung ist",
    "s4_warum": "Warum 21 Tage",
    "s6_wer": "Wer diesen Bonus auslässt",
    "s7_skala": "Zur Skala",
    "s7_ende": "Zum Schluss",
    "dias": ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"],
    "woche": "Woche",
    # ⛔ Rotulo de GRAFICO tambem e' idioma. Ficaram cravados em alemao
    # dentro do motor e vazaram inteiros para o PDF frances — texto que
    # ninguem le em revisao porque esta desenhado, nao escrito.
    "svg": {"ein": "EIN", "aus": "AUS", "ein_longo": "EINATMEN",
            "aus_longo": "AUSATMEN", "cheio": "VOLL", "vazio": "LEER",
            "legenda": "Das Ausatmen ist l&#228;nger. Genau das ist der ganze Trick."},
}

ARQUIVOS = [
    "Schritt 1 - Fang hier an.pdf",
    "Schritt 2 - Der Atemanker.pdf",
    "Schritt 3 - Der Notfall-Anker.pdf",
    "Schritt 4 - Dein 21-Tage-Plan.pdf",
    "Schritt 5 - Die Abendroutine.pdf",
    "Schritt 6 - Bonus 1 - Kaelte ohne Eis.pdf",
    "Schritt 7 - Bonus 2 - Dein Ruhe-Tagebuch.pdf",
]

TITULOS_DOC = [
    "Fang hier an — Der Atemanker", "Der Atemanker", "Der Notfall-Anker",
    "Dein 21-Tage-Plan", "Die Abendroutine", "Kälte ohne Eis",
    "Dein Ruhe-Tagebuch",
]
