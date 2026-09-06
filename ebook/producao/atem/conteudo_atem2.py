# -*- coding: utf-8 -*-
"""CONTEUDO — DER ATEMANKER, parte 2: Schritte 3 a 7.

Continuacao de `conteudo_atem.py`. Separado em dois arquivos por TAMANHO, nao
por assunto — as mesmas tres travas do cabecalho de la' valem aqui inteiras.
"""

from conteudo_atem import SICHERHEIT_KURZ, WASSER_KURZ

# ===========================================================================
# SCHRITT 3 — DER NOTFALL-ANKER
# ===========================================================================

S3 = {
    "badge": "Schritt 3",
    "titel": "Der Notfall-Anker",
    "lead": ("Für den Moment, in dem es dich erwischt. Neunzig Sekunden, im "
             "Sitzen, ohne dass jemand im Raum etwas mitbekommt. Lies das "
             "heute — nicht erst, wenn du es brauchst."),
    "foto": "akut",

    "was_titel": "Was in diesem Moment gerade passiert",
    "was_sub": ("Zu wissen, was der Körper tut, nimmt der Sache schon einen "
                "Teil ihrer Größe."),
    "was": [
        "Dein Körper hat entschieden, dass etwas gefährlich ist, und schaltet auf "
        "Handeln. Das Herz wird schneller, damit die Muskeln Blut bekommen. Der "
        "Atem geht hoch in die Brust und wird schnell. Die Hände werden kalt, weil "
        "das Blut aus der Peripherie in die Mitte gezogen wird.",
        "Das ist alles <b>sinnvoll</b> — nur eben gerade nicht nötig. Der Körper "
        "macht ein Programm für eine Gefahr, die nicht da ist.",
        "Und jetzt kommt der Teil, der im Moment selbst schwer zu glauben ist: "
        "<b>Der schnelle Atem hält das Programm am Laufen.</b> Wenn du schnell und "
        "flach in die Brust atmest, meldet dein Körper zurück: „Wir sind noch "
        "mitten drin.“ Es ist eine Schleife.",
        "Der Notfall-Anker unterbricht genau diese Schleife an der einzigen "
        "Stelle, an die du herankommst — <b>am Ausatmen</b>.",
    ],
    "was_merk": ("Erwarte nicht, dass es von hundert auf null geht. Das Ziel "
                 "ist von <b>neun auf sechs</b>. Von sechs kommst du allein "
                 "weiter, von neun nicht."),

    "uebungen": [
        {
            "tag": "Akut",
            "nome": "Die Lippenbremse",
            "hook": ("Die erste Übung im Akutmoment, weil sie die einzige ist, die "
                     "auch dann funktioniert, wenn du nicht klar denken kannst."),
            "foto": "lippen",
            "stats": [("90 Sek", "Dauer"), ("6", "Atemzüge"), ("Sofort", "Einsatz")],
            "ritmo": (4, 8, 0, 2),
            "schritte": [
                "<b>Setz dich hin.</b> Egal wo — Stuhl, Bettkante, Treppenstufe, "
                "Toilettendeckel. Hauptsache sitzen.",
                "<b>Ein durch die Nase, zähl bis vier.</b> Nicht tief. Ganz normal viel.",
                "<b>Spitz die Lippen</b>, als würdest du durch einen Strohhalm pusten "
                "oder eine Kerze fast ausblasen wollen — ohne sie zu treffen.",
                "<b>Atme durch diesen schmalen Spalt aus und zähl bis acht.</b> Der "
                "Widerstand an den Lippen macht das lange Ausatmen leicht; ohne ihn "
                "ist es im Akutmoment fast unmöglich.",
                "<b>Sechs Atemzüge.</b> Das sind ungefähr neunzig Sekunden.",
                "Danach gehst du auf die normale Nasenatmung <b>4–6</b> über, "
                "solange es sich gut anfühlt.",
            ],
            "worauf": ("Der erste Hinweis ist fast nie „ich bin ruhig“. Es ist "
                       "ein tiefer, unwillkürlicher Seufzer, oder dass dir "
                       "auffällt, wie fest deine Kiefer zusammengepresst waren."),
            "sicher": SICHERHEIT_KURZ + " " + WASSER_KURZ,
        },
        {
            "tag": "Akut",
            "nome": "Der Bodenanker 5–4–3",
            "hook": ("Wenn der Kopf in einer Schleife hängt und Zählen allein nicht "
                     "reicht: Der Anker geht dann über die Sinne."),
            "foto": "boden",
            "stats": [("2 Min", "Dauer"), ("Augen offen", "Immer"), ("Überall", "Ort")],
            "ritmo": None,
            "schritte": [
                "Sitz hin und atme <b>einmal</b> lang aus, bevor du anfängst.",
                "<b>Fünf Dinge, die du siehst.</b> Nenn sie innerlich beim Namen — "
                "„Türrahmen“, „Tasse“, „Kabel“. Nach jedem Ding einmal lang ausatmen.",
                "<b>Vier Dinge, die du hörst.</b> Auch die leisen: der Kühlschrank, "
                "ein Auto, dein eigener Atem.",
                "<b>Drei Dinge, die du spürst.</b> Die Füße im Schuh. Der Stoff am "
                "Arm. Die Sitzfläche unter dir.",
                "Dann sechs Atemzüge <b>4–6</b>, und du bist fertig.",
            ],
            "worauf": ("Diese Übung holt die Aufmerksamkeit aus dem Kopf in den "
                       "Raum. Sie ist besonders gut, wenn das Zählen selbst zum "
                       "Stressfaktor geworden ist („mache ich es richtig?“)."),
            "sicher": None,
        },
        {
            "tag": "Nachts",
            "nome": "Der Anker um drei Uhr",
            "hook": ("Für das Aufwachen mitten in der Nacht, wenn der Kopf sofort "
                     "auf Betriebstemperatur ist."),
            "foto": "nacht",
            "stats": [("Liegend", "Haltung"), ("Kein Licht", "Regel"), ("4–8", "Rhythmus")],
            "ritmo": (4, 8, 0, 2),
            "schritte": [
                "<b>Bleib liegen und mach kein Licht an.</b> Kein Handy — der Blick "
                "aufs Display beendet die Nacht endgültig.",
                "Dreh dich auf die <b>rechte Seite</b> oder auf den Rücken, was "
                "bequemer ist, und leg eine Hand auf den Bauch.",
                "<b>Vier ein durch die Nase, acht aus durch die Nase.</b> Das lange "
                "Ausatmen geht im Liegen leichter als im Sitzen.",
                "<b>Zähl die Ausatmungen rückwärts</b>, von zehn auf eins. Wenn du "
                "bei eins ankommst und noch wach bist, fängst du wieder bei zehn an.",
                "Es ist ausdrücklich <b>egal</b>, ob du wieder einschläfst. Sobald "
                "Einschlafen das Ziel wird, wird es zur Prüfung — und Prüfungen "
                "halten wach.",
            ],
            "worauf": ("Ruhig daliegen und atmen erholt deinen Körper deutlich mehr "
                       "als wach daliegen und rechnen, wie viele Stunden noch "
                       "bleiben. Das ist kein Trost, das ist der eigentliche Zweck."),
            "sicher": None,
        },
    ],

    "wenn_titel": "Wenn es nicht sofort wirkt",
    "wenn_sub": "Drei Sätze, die dir dann helfen.",
    "wenn": [
        "<b>Erwarte keinen Schalter.</b> Es ist ein Regler. Von neun auf sechs ist "
        "der ganze Job — und von sechs kommst du allein weiter.",
        "<b>Zwing die Zahlen nicht.</b> Wenn acht Sekunden Ausatmen im Moment nicht "
        "gehen, nimm sechs. Das Verhältnis zählt, nicht der Wert.",
        "<b>Der Notfall-Anker wird durch Übung besser.</b> Wer ihn drei Wochen lang "
        "in Ruhe geübt hat, greift im Ernstfall auf etwas Bekanntes zurück. Wer "
        "ihn zum ersten Mal mitten im Sturm probiert, hat es schwerer. Genau "
        "deswegen gibt es Schritt 4.",
    ],

    "plan_titel": "Dein Notfallplan zum Ausdrucken",
    "plan_sub": ("Füll das einmal in Ruhe aus und leg es dorthin, wo du es "
                 "ohne Suchen findest."),
    "plan_zeilen": [
        ("Ich merke es zuerst daran, dass …", "z. B. enge Brust, kalte Hände, Kloß im Hals"),
        ("Dann setze ich mich hin — hier:", "z. B. Küchenstuhl, Bettkante, Auto im Stand"),
        ("Ich mache:", "Lippenbremse 4–8, sechs Atemzüge"),
        ("Danach:", "Nasenatmung 4–6, so lange es guttut"),
        ("Wenn es nicht besser wird, rufe ich an:", "Name und Nummer eines Menschen"),
    ],
    "plan_hinweis": (
        "<b>Bitte einmal ernst nehmen:</b> Starke Brustschmerzen, Atemnot, "
        "Ohnmacht oder ein Zustand, der ganz anders ist als sonst, gehören nicht "
        "in eine Atemübung, sondern zum Notruf <b>112</b>. Eine Übung ersetzt "
        "keine ärztliche Abklärung."
    ),
}

# ===========================================================================
# SCHRITT 4 — DER 21-TAGE-PLAN
# ===========================================================================

S4 = {
    "badge": "Schritt 4",
    "titel": "Dein 21-Tage-Plan",
    "lead": ("Eine Aufgabe pro Tag, nie länger als fünf Minuten. Das ist der "
             "Teil, der aus einer Übung eine Gewohnheit macht — und der "
             "einzige Grund, warum es in drei Wochen anders ist als heute."),
    "foto": "plan21",

    "wie_titel": "Wie dieser Plan funktioniert",
    "wie_sub": "Vier Regeln, und alle vier sind bewusst niedrig gehängt.",
    "wie": [
        "<b>Eine Aufgabe pro Tag.</b> Nicht drei. Wenn du mehr machen willst, "
        "machst du mehr — aber die Aufgabe ist immer nur eine.",
        "<b>Häng sie an etwas, das du sowieso tust.</b> Nach dem Zähneputzen. "
        "Nachdem der Kaffee durchgelaufen ist. Beim Hinsetzen ins Auto, bevor du "
        "startest. Eine Gewohnheit braucht einen festen Nachbarn, keinen Wecker.",
        "<b>Ein verpasster Tag ist kein Abbruch.</b> Du machst am nächsten Tag da "
        "weiter, wo du warst. Zwei verpasste Tage sind auch kein Abbruch. Der "
        "Plan hat keine Frist.",
        "<b>Hak ab.</b> Jeden Tag ein Häkchen in der Tabelle am Ende dieser Datei "
        "oder im Ruhe-Tagebuch. Das klingt albern und ist trotzdem der Grund, "
        "warum Leute in Woche drei noch dabei sind.",
    ],
    "wie_merk": ("Warum 21 Tage? Nicht weil eine Gewohnheit nach genau 21 Tagen "
                 "fertig ist — das ist ein Mythos, und wir verkaufen ihn dir "
                 "nicht. Drei Wochen sind einfach lang genug, dass du den "
                 "Unterschied selbst bemerkst, und kurz genug, dass man sie "
                 "durchhält."),

    "wochen": [
        {
            "rot": "Woche 1",
            "titel": "Das Fundament",
            "text": ("In dieser Woche geht es nur darum, den Rhythmus in den "
                     "Körper zu bekommen — noch nicht darum, ihn zu benutzen, "
                     "wenn es schwierig wird."),
            "tage": [
                (1, "Die Haltung", "Lies Schritt 2 und mach nur die Übung „Die "
                    "Haltung“. Zwei Minuten. Heute noch kein Rhythmus."),
                (2, "Die Hand auf den Rippen", "Finde heraus, ob du oben oder unten "
                    "atmest. Fünf Atemzüge mit der Hand an den Rippen."),
                (3, "Zum ersten Mal 4–6", "Zwölf Atemzüge im Rhythmus 4–6. Wenn "
                    "sechs zu lang sind, nimm 3–4. Beides ist richtig."),
                (4, "Nochmal 4–6", "Dasselbe wie gestern, gleiche Uhrzeit, gleicher "
                    "Ort. Die Wiederholung ist heute die eigentliche Aufgabe."),
                (5, "Der Blickanker", "Heute wählst du bewusst <b>eine</b> Sache, bei "
                    "der du bleibst: die Zahlen, die Luft an der Nase, oder die "
                    "Hand. Nur eine."),
                (6, "Zwei Minuten ohne Zählen", "Mach die Übung, aber zähl nicht "
                    "mit. Nur „lang raus“. Danach: Hast du den Rhythmus gehalten?"),
                (7, "Rückblick", "Die Übung wie immer, und danach eine Minute: Was "
                    "war diese Woche anders? Schreib einen Satz ins Ruhe-Tagebuch."),
            ],
        },
        {
            "rot": "Woche 2",
            "titel": "Zweimal am Tag",
            "text": ("Jetzt kommt der zweite Termin dazu, und zum ersten Mal "
                     "übst du den Notfall-Anker — in Ruhe, absichtlich, "
                     "solange nichts los ist."),
            "tage": [
                (8, "Morgens und abends", "Zweimal zwei Minuten. Der Abendtermin "
                    "kommt an etwas dran, das du sowieso machst."),
                (9, "Die Lippenbremse üben", "Lies Schritt 3 und mach die "
                    "Lippenbremse einmal in aller Ruhe. Genau jetzt, wo du sie "
                    "nicht brauchst, lernst du sie."),
                (10, "Der Anker am Schreibtisch", "Bau die unsichtbare Variante "
                     "einmal in deinen Arbeitstag ein — vor einem Termin, nicht "
                     "danach."),
                (11, "Vor dem schwierigen Moment", "Such dir heute eine Situation, "
                     "von der du weißt, dass sie dich anspannt, und atme zwei "
                     "Minuten <b>vorher</b>."),
                (12, "Der Anker im Gehen", "Fünf Minuten gehen, vier Schritte ein, "
                     "sechs Schritte aus. Auch wenn du ein Sitztyp bist: einmal "
                     "probieren."),
                (13, "Länger ausatmen", "Heute 4–7 statt 4–6, wenn es mühelos "
                     "geht. Wenn nicht, bleibst du bei 4–6. Kein Punktabzug."),
                (14, "Rückblick", "Zweimal zwei Minuten, und danach: In welcher "
                     "Situation hättest du den Anker diese Woche gut gebrauchen "
                     "können, hast ihn aber vergessen?"),
            ],
        },
        {
            "rot": "Woche 3",
            "titel": "Im echten Leben",
            "text": ("Die Übung verlässt den geschützten Termin. Diese Woche "
                     "benutzt du sie da, wo sie eigentlich hingehört."),
            "tage": [
                (15, "Der Abendanker", "Lies Schritt 5 und mach die Abendroutine "
                     "heute zum ersten Mal, im Bett, im Liegen."),
                (16, "Ohne Vorbereitung", "Mach die Übung heute irgendwann "
                     "spontan, wenn dir auffällt, dass du angespannt bist. Egal wo."),
                (17, "Kaltes Wasser", "Lies Bonus 1 und mach nur die "
                     "Handgelenks-Übung. Zwanzig Sekunden, mehr nicht."),
                (18, "Der Bodenanker", "Übe heute 5–4–3 aus Schritt 3 einmal in "
                     "Ruhe durch, damit du ihn im Ernstfall kennst."),
                (19, "Zweimal, plus einmal spontan", "Die beiden festen Termine, "
                     "und einmal, wenn der Tag es verlangt."),
                (20, "Dein eigener Rhythmus", "Finde heraus, welche Variante dir "
                     "am meisten bringt, und mach heute nur die."),
                (21, "Die Bilanz", "Übung wie immer. Danach nimmst du dir das "
                     "Ruhe-Tagebuch und liest die drei Wochen am Stück durch. "
                     "Das ist der wichtigste Moment im ganzen Plan."),
            ],
        },
    ],

    "danach_titel": "Und nach Tag 21?",
    "danach_sub": "Der ehrliche Teil.",
    "danach": [
        "Es hört nicht auf. Der Atemanker ist keine Kur, die man abschließt — er "
        "ist eher wie Zähneputzen: klein, unspektakulär, und man merkt ihn vor "
        "allem, wenn er wegfällt.",
        "<b>Was in den meisten Fällen bleibt:</b> zweimal zwei Minuten am Tag, "
        "morgens und abends, plus der Notfall-Anker, wenn er gebraucht wird. Das "
        "sind vier Minuten. Mehr braucht es dauerhaft nicht.",
        "<b>Wenn du merkst, dass es wegrutscht</b> — und das passiert bei fast "
        "jedem irgendwann — fängst du einfach wieder bei Tag 1 an. Die zweite "
        "Runde geht deutlich schneller als die erste.",
    ],

    "tabela_col": "Geübt",
    "tabelle_titel": "Deine Häkchen-Tabelle",
    "tabelle_sub": ("Druck diese Seite aus. Ein Kreuz pro Tag, und mehr "
                    "nicht — Notizen kommen ins Ruhe-Tagebuch."),
}

# ===========================================================================
# SCHRITT 5 — DIE ABENDROUTINE
# ===========================================================================

S5 = {
    "badge": "Schritt 5",
    "titel": "Die Abendroutine",
    "lead": ("Für den Kopf, der abends lauter wird als tagsüber. Zwanzig "
             "Minuten vor dem Licht-aus, und eine Übung für die Nächte, in "
             "denen du um drei wach wirst."),
    "foto": "abend",

    "warum_titel": "Warum der Kopf abends lauter wird",
    "warum_sub": "Es liegt nicht daran, dass du zu viel nachdenkst.",
    "warum": [
        "Tagsüber ist dein Kopf beschäftigt. Es gibt Aufgaben, Menschen, "
        "Geräusche, Bildschirme. Alles davon frisst Aufmerksamkeit, und "
        "Aufmerksamkeit ist begrenzt.",
        "Abends fällt das alles weg. Zum ersten Mal seit dem Aufstehen ist "
        "<b>Platz</b> — und was du dann hörst, war den ganzen Tag schon da. Es war "
        "nur übertönt.",
        "Deshalb funktioniert der Rat „denk einfach nicht dran“ so zuverlässig "
        "nicht. Du kannst dir nicht befehlen, etwas nicht zu denken.",
        "Was du kannst: <b>dem Körper ein Signal geben, das stärker ist als der "
        "Gedanke.</b> Ein langes Ausatmen ist so ein Signal. Ein warmer Raum, "
        "gedämpftes Licht und ein liegender Körper sind drei weitere.",
    ],

    "uebungen": [
        {
            "tag": "Abend",
            "nome": "Der Abendanker 4–8",
            "hook": ("Dieselbe Übung wie tagsüber, nur mit doppelt so langem "
                     "Ausatmen — im Liegen geht das plötzlich leicht."),
            "foto": "liegen",
            "stats": [("3 Min", "Dauer"), ("10", "Atemzüge"), ("Im Bett", "Ort")],
            "ritmo": (4, 8, 0, 2),
            "schritte": [
                "<b>Leg dich auf den Rücken</b>, Beine lang, Arme neben dem Körper. "
                "Wenn der untere Rücken zwickt, leg ein Kissen unter die Knie.",
                "Eine <b>Hand auf den Bauch</b>. Im Liegen spürst du die Bewegung "
                "deutlicher als im Sitzen.",
                "<b>Vier ein durch die Nase.</b> Nicht tief — normal viel.",
                "<b>Acht aus durch die Nase.</b> Lass die Luft aus dir "
                "herausfließen, ohne zu drücken. Wenn acht zu viel sind, nimm sechs.",
                "<b>Zehn Atemzüge.</b> Danach hörst du auf zu zählen und lässt den "
                "Atem machen, was er will.",
            ],
            "worauf": ("Die Bauchdecke wird weich. Oft merkst du erst jetzt, dass "
                       "du sie den ganzen Tag angespannt hattest."),
            "sicher": SICHERHEIT_KURZ + " " + WASSER_KURZ,
        },
        {
            "tag": "Abend",
            "nome": "Der Körperscan von unten nach oben",
            "hook": ("Für die Abende, an denen der Atem allein den Kopf nicht "
                     "einholt. Zehn Minuten, und du bist selten am Ende wach."),
            "foto": "scan",
            "stats": [("10 Min", "Dauer"), ("Liegend", "Haltung"), ("Von unten", "Richtung")],
            "ritmo": None,
            "schritte": [
                "Leg dich hin und atme <b>fünf Atemzüge</b> im Rhythmus 4–8, damit "
                "der Körper weiß, was jetzt kommt.",
                "Dann wanderst du mit der Aufmerksamkeit <b>von den Füßen aufwärts</b>. "
                "Erst der linke Fuß, dann der rechte. Unterschenkel. Knie. "
                "Oberschenkel. Becken.",
                "An jeder Stelle bleibst du <b>zwei Atemzüge</b> und stellst eine "
                "einzige Frage: <b>Ist hier etwas fest?</b> Wenn ja, lass es beim "
                "Ausatmen ein Stück los.",
                "Weiter: Bauch, unterer Rücken, Brustkorb, Hände, Arme, Schultern.",
                "<b>Die vier Stellen, an denen fast jeder etwas findet:</b> Kiefer, "
                "Zunge, Stirn zwischen den Augenbrauen, Schultern. Nimm dir für "
                "diese vier extra Zeit.",
                "Am Ende der Kopf. Dann liegst du einfach da und lässt es sein.",
            ],
            "worauf": ("Der Kiefer ist bei den meisten Menschen die Überraschung. "
                       "Wenn du die Zähne auseinandernimmst und die Zunge vom "
                       "Gaumen löst, geht oft ein Teil der Anspannung im Nacken "
                       "gleich mit."),
            "sicher": None,
        },
        {
            "tag": "Einschlafen",
            "nome": "Rückwärts von hundert",
            "hook": ("Wenn Gedanken kreisen, hilft nicht Leere — es hilft eine "
                     "Aufgabe, die langweilig genug ist."),
            "foto": "einschlafen",
            "stats": [("Offen", "Dauer"), ("Liegend", "Haltung"), ("Jede Nacht", "Wenn nötig")],
            "ritmo": None,
            "schritte": [
                "Atme im Rhythmus <b>4–8</b>, ohne die Sekunden zu zählen.",
                "Bei <b>jedem Ausatmen</b> zählst du innerlich eine Zahl rückwärts, "
                "beginnend bei hundert. Ausatmen — hundert. Ausatmen — "
                "neunundneunzig.",
                "Wenn du dich verzählst oder die Zahl verlierst, ist das <b>gut</b>: "
                "Es heißt, dass dein Kopf gerade abschaltet. Fang bei einer "
                "beliebigen runden Zahl wieder an.",
                "Wenn du bei achtzig ankommst und hellwach bist, hörst du auf, "
                "stehst kurz auf, trinkst einen Schluck Wasser und legst dich "
                "wieder hin. Stundenlang wach im Bett zu liegen bringt nichts.",
            ],
            "worauf": ("Der Trick ist die <b>Langeweile</b>. Die Aufgabe muss "
                       "gerade so viel Aufmerksamkeit binden, dass für die "
                       "Sorgenschleife nichts übrig bleibt — und gleichzeitig zu "
                       "öde sein, um dich wachzuhalten."),
            "sicher": None,
        },
    ],

    "stunde_titel": "Die letzte Stunde vor dem Schlafen",
    "stunde_sub": ("Fünf Dinge, die mehr bringen als jede Übung — und drei "
                   "davon kosten nichts."),
    "stunde": [
        ("Licht runter, eine Stunde vorher.", "Nicht die Deckenlampe, sondern "
         "eine kleine Lampe. Dein Körper liest Helligkeit als Uhrzeit."),
        ("Bildschirm aus dem Bett.", "Nicht wegen des blauen Lichts allein — "
         "vor allem, weil das, was auf dem Bildschirm passiert, dich wach hält. "
         "Nachrichten um 23 Uhr sind eine Entscheidung gegen den Schlaf."),
        ("Kühl schlafen.", "Um die 18 Grad. Der Körper muss zum Einschlafen "
         "seine Kerntemperatur senken, und in einem warmen Zimmer geht das "
         "schwerer."),
        ("Der Zettel neben dem Bett.", "Wenn dir etwas einfällt, schreib es "
         "auf, statt es zu behalten. Ein aufgeschriebener Gedanke hört auf, "
         "sich zu wiederholen."),
        ("Gleiche Aufstehzeit, auch am Wochenende.", "Die Aufstehzeit steuert "
         "den Rhythmus stärker als die Zubettgehzeit. Zwei Stunden Ausschlafen "
         "am Sonntag kosten dich den Sonntagabend."),
    ],

    "faq": [
        ("Ich schlafe bei der Übung ein. Ist das schlecht?",
         "Nein, das ist abends genau das Ziel. Wenn du tagsüber einschläfst, "
         "machst du die Übung im Sitzen statt im Liegen."),
        ("Hilft das bei einer Schlafstörung?",
         "Diese Datei ist eine Abendroutine, keine Behandlung. Wenn du seit "
         "Wochen kaum schläfst, gehört das ärztlich abgeklärt — dafür gibt es "
         "wirksame Verfahren, und ein PDF ist keines davon."),
        ("Wie lange dauert es, bis ich einen Unterschied merke?",
         "Beim Einschlafen merken viele Menschen etwas in der ersten Woche. "
         "Beim Durchschlafen dauert es meist länger, weil da mehr mitspielt "
         "als der Atem."),
    ],
}

# ===========================================================================
# SCHRITT 6 — BONUS 1: KAELTE OHNE EIS
# ===========================================================================

S6 = {
    "badge": "Bonus 1",
    "titel": "Kälte ohne Eis",
    "lead": ("Der kleine Verstärker — kaltes Wasser am Handgelenk, am "
             "Gesicht, am Ende der Dusche. Freiwillig, in dreißig Sekunden, "
             "und niemals zusammen mit den Atemübungen."),
    "foto": "handgelenk",
    "dourado": True,

    "warum_titel": "Warum Kälte — und warum sie nicht das Wichtigste ist",
    "warum_sub": ("Diese Datei ist ein Bonus, und das ist wörtlich gemeint."),
    "warum": [
        "Kaltes Wasser im Gesicht und an den Handgelenken löst eine sehr alte, "
        "sehr schnelle Reaktion aus: der Puls geht runter, die Aufmerksamkeit "
        "springt vom Gedanken in den Körper. Das passiert innerhalb von Sekunden "
        "und ohne dass du etwas dafür können musst.",
        "Genau das macht Kälte zu einem guten <b>Türöffner</b> an Tagen, an denen "
        "du zu aufgedreht bist, um dich hinzusetzen und zu zählen. Erst das kalte "
        "Wasser, dann der Atemanker — in dieser Reihenfolge.",
        "<b>Und jetzt der ehrliche Teil:</b> Die Kälte ist nicht der Grund, warum "
        "das Ganze funktioniert. Der Atem ist es. Wenn du dich zwischen beidem "
        "entscheiden müsstest, nimmst du den Atem, jeden Tag.",
        "Du brauchst <b>kein Eis</b>, keine Tonne, keine Wanne und keinen Kurs. "
        "Ein Wasserhahn reicht.",
    ],

    "regeln_titel": "Die Regeln — bitte vor der ersten Übung lesen",
    "regeln_sub": ("Diese Seite ist der Grund, warum dieser Bonus so klein "
                   "gehalten ist."),
    "regeln": [
        "<b>Niemals Atemübung und Kälte gleichzeitig.</b> Erst das eine, dann das "
        "andere, mit ein paar Minuten dazwischen. Nie kombiniert.",
        "<b>Niemals die Luft anhalten, während du im kalten Wasser bist.</b> Weder "
        "kurz noch lang, weder unter der Dusche noch am Waschbecken.",
        "<b>Niemals in eine Wanne, einen Pool, einen See oder einen Fluss.</b> Auch "
        "nicht flach. Auch nicht mit jemandem daneben. Wer nach Atemübungen ins "
        "kalte Wasser steigt, kann ohne Vorwarnung das Bewusstsein verlieren — "
        "und das passiert auch Menschen, die gut schwimmen.",
        "<b>Nicht länger als dreißig Sekunden.</b> Mehr bringt nichts und "
        "verwandelt eine kleine Übung in einen Wettkampf.",
        "<b>Kein Schockstart.</b> Nicht mit dem Kopf oder der Brust anfangen — "
        "immer mit den Händen.",
    ],
    "regeln_wer": (
        "<b>Lass diesen Bonus ganz weg</b>, wenn du eine Herzerkrankung oder "
        "Bluthochdruck hast, schwanger bist, unter Raynaud oder einer "
        "Kälteallergie leidest, oder wenn du dir bei irgendetwas davon unsicher "
        "bist. Dieser Bonus ist der einzige Teil des Pakets, den du komplett "
        "auslassen kannst, ohne dass dir etwas fehlt."
    ),

    "uebungen": [
        {
            "tag": "Stufe 1",
            "nome": "Kaltes Wasser auf die Handgelenke",
            "hook": ("Die kleinste Dosis, die es gibt, und der richtige Anfang "
                     "für alle."),
            "foto": "handgelenk",
            "stats": [("20 Sek", "Dauer"), ("Waschbecken", "Ort"), ("Kalt", "Nicht eiskalt")],
            "ritmo": None,
            "schritte": [
                "Dreh den Hahn auf <b>kalt</b>. Kein Eis, keine Eiswürfel — "
                "Leitungswasser reicht vollkommen.",
                "Halt das <b>linke Handgelenk</b> unter den Strahl, die Innenseite "
                "nach oben, zehn Sekunden lang.",
                "Dann das <b>rechte</b>, auch zehn Sekunden.",
                "<b>Atme dabei normal weiter.</b> Kein Anhalten, kein Hecheln, kein "
                "Zählen. Wenn dir das Luftanhalten von allein passiert, ist das "
                "Wasser zu kalt für dich.",
                "Abtrocknen. Fertig. Danach kannst du dich hinsetzen und zwei "
                "Minuten den Atemanker machen — jetzt geht er leichter.",
            ],
            "worauf": ("Ein kurzes, scharfes Einatmen beim ersten Kontakt ist "
                       "normal. Danach sollte sich der Atem innerhalb von zwei, "
                       "drei Atemzügen von allein beruhigen. Tut er das nicht, "
                       "brich ab."),
            "sicher": ("Nur am Waschbecken. Nicht über einer Wanne, nicht in der "
                       "Wanne, und nie mit angehaltenem Atem."),
        },
        {
            "tag": "Stufe 2",
            "nome": "Das kalte Tuch aufs Gesicht",
            "hook": ("Die stärkste Variante am Waschbecken — und die, die "
                     "im hochgefahrenen Moment am schnellsten wirkt."),
            "foto": "gesichtstuch",
            "stats": [("20 Sek", "Dauer"), ("Sitzend", "Haltung"), ("Waschlappen", "Werkzeug")],
            "ritmo": None,
            "schritte": [
                "Mach einen <b>Waschlappen unter kaltem Wasser nass</b> und drück ihn "
                "leicht aus. <b>Setz dich hin</b>, bevor du weitermachst.",
                "Leg das Tuch auf <b>Stirn, Augen und Wangenknochen</b>. Das ist die "
                "Zone, die zählt — nicht Mund und nicht Hals.",
                "<b>Atme dabei ganz normal weiter</b> und halt die Luft auf keinen "
                "Fall an. Zwanzig Sekunden, mehr nicht.",
                "Tuch weg, Gesicht abtrocknen, einen Moment sitzen bleiben.",
                "Danach der Atemanker <b>4–6</b>, zwölf Atemzüge.",
            ],
            "worauf": ("Viele merken, dass der Kopf für ein paar Sekunden „leer“ "
                       "wird. Genau dieses Fenster nutzt du für die Atemübung — "
                       "deshalb kommt sie direkt danach."),
            "sicher": ("Im Sitzen, nie über ein volles Waschbecken gebeugt, und "
                       "nie mit angehaltenem Atem. Bei Herzerkrankungen ganz "
                       "auslassen."),
        },
        {
            "tag": "Stufe 3",
            "nome": "Die letzten zwanzig Sekunden der Dusche",
            "hook": ("Für alle, die die ersten beiden Stufen eine Woche lang "
                     "problemlos gemacht haben."),
            "foto": "dusche",
            "stats": [("20 Sek", "Dauer"), ("Am Ende", "Wann"), ("Füße zuerst", "Reihenfolge")],
            "ritmo": None,
            "schritte": [
                "Dusch ganz normal warm. Das hier passiert <b>am Ende</b>, nicht am "
                "Anfang.",
                "Dreh auf kalt und fang bei den <b>Füßen</b> an. Dann Unterschenkel, "
                "dann Hände und Unterarme.",
                "Dann <b>Rücken und Nacken</b>. Der Kopf ist optional und kein Ziel.",
                "<b>Atme laut und ruhig weiter</b> — ein hörbares, langes Ausatmen "
                "hilft hier mehr als alles andere. Kein Anhalten.",
                "Zwanzig Sekunden. Rausgehen, gut abtrocknen, warm anziehen.",
            ],
            "worauf": ("Wenn du danach zitterst, war es zu lang oder zu kalt. Ziel "
                       "ist wach und warm durchblutet, nicht durchgefroren."),
            "sicher": ("Steh sicher, halt dich fest, wenn die Wanne rutschig ist. "
                       "Nicht bei Kreislaufproblemen. Wer beim Aufstehen "
                       "regelmäßig schwarz sieht, lässt Stufe 3 weg."),
        },
    ],

    "woche_titel": "Eine Woche Aufbau",
    "woche_sub": ("Wenn du den Bonus machst, dann so — und nicht schneller."),
    "woche_tage": [
        (1, "Handgelenke, 10 Sekunden", "Nur die Hände, nur kurz."),
        (2, "Handgelenke, 20 Sekunden", "Gleiche Übung, ein bisschen länger."),
        (3, "Handgelenke plus Gesicht mit den Händen", "Kaltes Wasser zweimal "
            "ins Gesicht spritzen, im Stehen am Becken."),
        (4, "Das kalte Tuch, 10 Sekunden", "Zum ersten Mal im Sitzen."),
        (5, "Das kalte Tuch, 20 Sekunden", "Danach direkt der Atemanker."),
        (6, "Pause", "Absichtlich. Ein Tag ohne Kälte gehört dazu."),
        (7, "Deine Wahl", "Die Stufe, die sich am besten angefühlt hat. Stufe 3 "
            "erst in der Woche darauf."),
    ],
}

# ===========================================================================
# SCHRITT 7 — BONUS 2: DAS RUHE-TAGEBUCH
# ===========================================================================

S7 = {
    "badge": "Bonus 2",
    "titel": "Dein Ruhe-Tagebuch",
    "lead": ("Vorlagen zum Ausdrucken. Nach drei Wochen siehst du schwarz "
             "auf weiß, was sich verändert hat — und was dich zuverlässig "
             "hochfahren lässt."),
    "foto": "tagebuch",
    "dourado": True,

    "warum_titel": "Warum aufschreiben",
    "warum_sub": "Zwei Gründe, und der zweite ist der wichtigere.",
    "warum": [
        "<b>Erstens: Erinnerung lügt.</b> Wenn du heute einen schlechten Tag hast, "
        "sagt dir dein Kopf mit voller Überzeugung, dass es „immer“ so ist und "
        "„nie“ besser wird. Ein Blatt Papier mit vierzehn Häkchen und drei "
        "notierten guten Abenden widerspricht dem.",
        "<b>Zweitens: Muster sieht man nur von außen.</b> Fast jeder hat zwei oder "
        "drei Auslöser, die zuverlässig funktionieren — eine bestimmte Uhrzeit, "
        "eine bestimmte Person, ein bestimmter Ort, zu wenig Schlaf, zu viel "
        "Kaffee, ein leerer Magen. Solange das im Kopf bleibt, ist es Nebel. "
        "Sobald es fünfmal auf demselben Blatt steht, ist es Information.",
        "Und mit Information kannst du etwas anfangen: den Termin verlegen, "
        "vorher atmen, den vierten Kaffee weglassen.",
    ],

    "wie_titel": "Wie du es benutzt",
    "wie_sub": "Zwei Minuten am Abend. Mehr ist nicht vorgesehen.",
    "wie": [
        "<b>Druck die Vorlagen aus</b> — drei Wochenblätter und ein "
        "Auslöser-Blatt. Ein Blatt pro Woche reicht.",
        "<b>Abends, direkt nach dem Abendanker</b>, machst du dein Häkchen und "
        "füllst die drei kurzen Spalten aus. Wenn du länger als zwei Minuten "
        "brauchst, schreibst du zu viel.",
        "<b>Zahlen statt Worte, wo es geht.</b> „Anspannung heute: 6“ ist "
        "vergleichbar. „War irgendwie anstrengend“ ist es nicht.",
        "<b>Der Auslöser kommt nur dann aufs zweite Blatt</b>, wenn wirklich etwas "
        "war. An ruhigen Tagen bleibt es leer, und das ist ein gutes Zeichen, "
        "kein Versäumnis.",
        "<b>Am Ende von Woche 3</b> legst du die drei Blätter nebeneinander und "
        "liest sie am Stück. Das ist Tag 21 im Plan, und es ist der Moment, für "
        "den das ganze Tagebuch existiert.",
    ],
    "wie_merk": ("Eine Skala von 0 bis 10 klingt beliebig, und das ist sie auch. "
                 "Sie muss nur <b>für dich</b> gleich bleiben — dann misst sie "
                 "Veränderung, und mehr soll sie nicht."),

    "wochen_titel": "Wochenblatt",
    "wochen_sub": ("Eine Zeile pro Tag. Anspannung von 0 bis 10, wobei 0 "
                   "vollkommen ruhig ist und 10 der schlimmste Zustand, den "
                   "du kennst."),
    "wochen_spalten": ["Tag", "Geübt", "Anspannung 0–10", "Geschlafen (Std.)",
                       "Ein Satz zum Tag"],

    "ausloeser_titel": "Das Auslöser-Blatt",
    "ausloeser_sub": ("Nur ausfüllen, wenn wirklich etwas war. Leere Zeilen "
                      "sind hier gute Nachrichten."),
    "ausloeser_spalten": ["Wann", "Wo / bei wem", "Wie stark 0–10",
                          "Was ich gemacht habe", "Hat es geholfen?"],

    "abend_titel": "Die drei Abendfragen",
    "abend_sub": ("Wenn dir das Wochenblatt zu trocken ist, nimm stattdessen "
                  "diese drei Fragen. Drei Zeilen, handschriftlich."),
    "abend_fragen": [
        ("Wann war ich heute am angespanntesten?",
         "Uhrzeit und Situation reichen. Keine Erklärung, keine Bewertung."),
        ("Was hat heute geholfen — und sei es für zwei Minuten?",
         "Auch Kleinigkeiten zählen: ein Fenster auf, ein Spaziergang, ein "
         "Anruf, der Atemanker vor dem Termin."),
        ("Was nehme ich mir für morgen vor — genau eine Sache?",
         "Eine. Die kleinste, die dir einfällt. Große Vorsätze am Abend werden "
         "am Morgen zurückgenommen."),
    ],

    "ende_titel": "Was du nach 21 Tagen siehst",
    "ende_sub": "Vier Dinge, die fast alle Menschen in ihren Blättern finden.",
    "ende": [
        "<b>Dass es schwankt.</b> Kein Verlauf geht sauber nach unten. Es gibt "
        "gute Wochen mit einem schlechten Tag darin, und das ist der "
        "Normalfall — nicht das Scheitern.",
        "<b>Dass die Spitzen kürzer werden, bevor sie seltener werden.</b> Meistens "
        "verändert sich zuerst, wie lange ein Zustand anhält, und erst später, "
        "wie oft er kommt.",
        "<b>Dass Schlaf fast alles erklärt.</b> Wenn du deine Anspannungswerte "
        "neben die Schlafstunden legst, sehen viele Menschen ihren stärksten "
        "Zusammenhang — deutlicher als jeden anderen Auslöser.",
        "<b>Dass du an mehr Tagen geübt hast, als du gedacht hättest.</b> Der Kopf "
        "erinnert sich an die Lücken. Das Blatt erinnert sich an die Häkchen.",
    ],
    "ende_schluss": (
        "Wenn du nach drei Wochen aufhören willst, hör auf. Wenn du weitermachen "
        "willst, brauchst du dafür nichts Neues — zweimal zwei Minuten am Tag "
        "und dieses Blatt einmal pro Woche reichen dauerhaft. "
        "<b>Und wenn deine Werte über Wochen oben bleiben, obwohl du übst, ist "
        "das kein Grund, dich mehr anzustrengen — es ist der Moment, in dem "
        "jemand vom Fach draufschauen sollte.</b>"
    ),
}
