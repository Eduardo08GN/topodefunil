# -*- coding: utf-8 -*-
"""COPY DAS LANDINGS — alemao e frances, num dicionario so'.

⛔ Um builder (`build_landing.py`), dados por idioma — a mesma doutrina do
`build_atem`. A copy morava dentro do builder enquanto so' existia o alemao;
quando o frances chegou, ela saiu de la' em vez de nascer um
`build_landing_fr.py`.

⭐ TRATAMENTO POR IDIOMA, e por motivos diferentes:
  · alemao `du`  — o pool do `gelo16` inteiro fala `du`; pagina que responde
    com `Sie` troca de pessoa no meio do funil.
  · frances `vous` — e' a voz que o repo ja' usa em frances (o `index-fr.html`
    do landing-150 tem 47 `vous` e zero `tu`).

⛔ O QUE NAO ENTRA EM NENHUM DOS DOIS: escassez falsa (`ultimos 5 exemplares`
num PDF) e depoimento/contagem de avaliacao inventados. No lugar, o bloco
`NAO promete`, que e' honesto e converte.
"""

TEXTOS = {

# ===========================================================================
# ALEMAO
# ===========================================================================
"de": {
 "lang": "de",
 "titulo_doc": "Der Atemanker — die 2-Minuten-Methode gegen innere Unruhe",
 "meta": ("Zwei Minuten, die deinem Körper sagen, dass die Gefahr vorbei ist. "
          "Sieben Dateien, ein 21-Tage-Plan, zwei Boni. Ohne Eis, ohne "
          "Ausrüstung, zu Hause."),
 "marca_mark": "ATEM",
 "marca": "Der Atemanker",
 "btn_topo": "Jetzt sichern",
 "capa": "capa-atem-800x1000.jpg",
 "capa_alt": "Der Atemanker — die 2-Minuten-Methode gegen innere Unruhe",
 "preco_de": "39", "desconto": "74%",
 "moeda_sinal": "€", "preco": "10", "centavos": ",00",
 "preco_texto": "10 €",

 "hero_eyebrow": "7 Dateien · 2 Gratis-Boni · Sofort-Download",
 "hero_h1": ("Du kannst dich nicht ruhig <i>denken</i>.<br>"
             "Aber du kannst dich ruhig <i>atmen</i>."),
 "hero_lede": ("Die 2-Minuten-Methode, die deinem Körper das Signal gibt, aus "
               "dem Daueralarm auszusteigen. Im Sitzen, zu Hause, im Warmen — "
               "<b>ohne Eis, ohne Ausrüstung und ohne dass jemand im Raum etwas "
               "mitbekommt.</b>"),
 "hero_badges": [("ic-book", "7", "Dateien"), ("ic-gift", "2", "Gratis-Boni"),
                 ("ic-bolt", "2", "Minuten pro Übung"),
                 ("ic-calendar", "21", "-Tage-Plan")],

 "pb_statt": "Statt", "pb_sparen": "sparen",
 "pb_once": "Einmalzahlung. Für immer deins. Kein Abo.",
 "pb_btn": "Sofort-Zugang holen",
 "pb_pay": ["Sicherer Hotmart-Checkout", "Per E-Mail zugesendet", "7 Tage Garantie"],

 "prob_eyebrow": "Warum bisher nichts geholfen hat",
 "prob_h2": "Du hast alles versucht, was im Kopf ansetzt.",
 "prob_itens": [
   "<b>Tabletten beruhigen den Kopf.</b> An den Teil, der deinen Puls hochfährt "
   "und deine Brust eng macht, kommen sie nicht heran.",
   "<b>Reden hilft dem Kopf.</b> Deinem Körper hat nie jemand beigebracht, wie "
   "er wieder runterkommt, wenn nichts mehr passiert.",
   "<b>Apps zählen dir Sekunden vor.</b> Sie erklären dir nie, warum die eine "
   "Zahl größer sein muss als die andere — und genau daran hängt alles.",
   "<b>Und der Klassiker: „Entspann dich einfach.“</b> Als hätte irgendjemand "
   "das nicht schon versucht.",
 ],
 "prob_punch": ("<b>Das Problem sitzt nicht im Kopf. Es sitzt im Körper</b> — und "
                "der hört keine Argumente. Er hört auf ein einziges Signal, und "
                "dieses Signal ist dein Ausatmen."),

 "feat_eyebrow": "Die Methode",
 "feat_h2": "Eine Sache, die du änderst — und zwar die richtige",
 "feat_lede": ("Nicht tiefer atmen. Nicht mehr atmen. Nur länger ausatmen als "
               "einatmen."),
 "feat_cards": [
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
 ],

 "rail_eyebrow": "Alles, was drin ist",
 "rail_h2": "Sieben Dateien, in der Reihenfolge, in der du sie brauchst",
 "rail_lede": ("Nummeriert von Schritt 1 bis Bonus 2 — du musst nie überlegen, "
               "was als Nächstes dran ist."),
 "rail_hint": "zum Weitersehen wischen",
 "rail_itens": [
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
 ],

 "cont_h2": "Das bekommst du",
 "cont_ticks": [
   "<b>Die Grundübung</b> in ihren fünf Varianten — Stuhl, Schreibtisch, "
   "Gehen, Liegen und die Version für alle, denen sechs Sekunden zu lang sind",
   "<b>Der Notfall-Anker:</b> neunzig Sekunden für den Akutmoment, plus eine "
   "Übung für nachts um drei",
   "<b>Ein 21-Tage-Plan</b> mit einer einzigen Aufgabe pro Tag",
   "<b>Eine komplette Abendroutine</b> für den Kopf, der abends lauter wird",
   "<b>Bonus 1:</b> Kälte ohne Eis — drei Stufen am Waschbecken",
   "<b>Bonus 2:</b> das Ruhe-Tagebuch zum Ausdrucken",
   "Alle Übungen mit <b>Foto und Atem-Diagramm</b>, damit du siehst, was du tust",
   "Zum Ausdrucken oder zum Lesen auf Handy, Tablet und Rechner",
   "Lebenslanger Zugang, einmal bezahlt",
 ],

 "bonus_eyebrow": "Kostenlos dabei",
 "bonus_h2": "Zwei Boni, die du sonst einzeln kaufen müsstest",
 "bonus_tag": "Bonus", "bonus_gratis": "heute gratis",
 "bonus_soma": "Zusammen <b>33 €</b> wert. Heute im Paket enthalten.",
 "bonus_itens": [
   ("1", "ic-shield", "Kälte ohne Eis",
    "Drei Stufen am Waschbecken und in der Dusche, jede unter dreißig "
    "Sekunden. Mit den Regeln, die dabei nicht verhandelbar sind.", "19"),
   ("2", "ic-calendar", "Dein Ruhe-Tagebuch",
    "Wochenblätter, ein Auslöser-Blatt und drei Abendfragen. Zum Ausdrucken, "
    "damit du nach 21 Tagen etwas in der Hand hast statt eines Gefühls.", "14"),
 ],

 "pass_eyebrow": "So läuft es ab",
 "pass_h2": "Von hier bis zur ersten Übung sind es Minuten",
 "pass_itens": [
   ("Du sicherst dir das Paket", "Über den sicheren Hotmart-Checkout. "
    "Einmalzahlung, kein Abo, keine Verlängerung."),
   ("Es landet in deinem Postfach", "In wenigen Minuten, als sieben "
    "PDF-Dateien zum Herunterladen. Auf Handy, Tablet, Rechner oder ausgedruckt."),
   ("Du fängst heute an", "Nicht nächsten Montag. Schritt 2 lesen, einmal "
    "mitmachen, fertig. Das sind fünf Minuten, einmalig."),
 ],

 "off_eyebrow": "Das Angebot",
 "off_h2": "Weniger als ein Kaffee und ein Stück Kuchen",
 "off_lede": "Eine Zahlung. Sofortige Lieferung. Für immer deins.",
 "off_h3": "Das kommt in dein Postfach",
 "off_ticks": [
   "<b>Der Atemanker</b> — das komplette Paket, sieben Dateien",
   "Die Grundübung mit fünf Alltags-Varianten",
   "Der Notfall-Anker für den Akutmoment",
   "Der 21-Tage-Plan mit Häkchen-Tabelle",
   "Die Abendroutine für ruhigere Nächte",
   "<b>Bonus 1:</b> Kälte ohne Eis",
   "<b>Bonus 2:</b> Dein Ruhe-Tagebuch zum Ausdrucken",
   "Sofort als Download, für immer deins",
 ],
 "off_once": "Eine Zahlung. Kein Abo. Keine Verlängerung.",
 "off_btn": "Ja, ich will den Atemanker",
 "off_note": ("Sicherer Hotmart-Checkout. Lieferung per E-Mail in wenigen "
              "Minuten."),

 "gar_dias": "7", "gar_dias_lab": "Tage",
 "gar_h2": "Probier es eine Woche lang aus. Auf unsere Kosten.",
 "gar_p1": ("Kauf es, lade es herunter und üb sieben Tage lang. Wenn es dir "
            "nichts bringt, schreibst du uns und bekommst dein Geld zurück — "
            "ohne Formular, ohne Begründung, ohne Rückfragen. Die Dateien "
            "liegen längst auf deinem Gerät, und dort bleiben sie auch."),
 "gar_p2": "Das Einzige, was du hier riskieren kannst, sind zwei Minuten.",

 "nicht_eyebrow": "Fair bleiben",
 "nicht_h2": "Was dieses Paket <i>nicht</i> verspricht",
 "nicht_lede": ("Wer ständig unruhig ist, wurde schon genug versprochen. "
                "Deshalb hier zuerst das, was wir nicht behaupten."),
 "nicht_itens": [
   ("Es macht deinen Kopf nicht leer.", "Das verspricht dir hier niemand. Das "
    "Ziel ist kleiner und ehrlicher: schneller wieder runterkommen als vorher."),
   ("Es ist keine Behandlung.", "Der Atemanker ist eine Übung. Er ersetzt "
    "weder Ärztin noch Psychotherapie, stellt keine Diagnose und ist kein "
    "Medikament. Wenn du Medikamente nimmst, nimmst du sie weiter."),
   ("Einmal reicht nicht.", "Beim ersten Mal passiert bei vielen Menschen "
    "schlicht nichts. Der Effekt kommt aus der Wiederholung — deshalb liegt "
    "dem Paket ein 21-Tage-Plan bei und keine Wunderübung."),
   ("Es ist nicht für jeden der richtige Moment.", "Wenn du gerade in einer "
    "akuten seelischen Krise steckst, ist das hier nicht dein nächster "
    "Schritt. Dann hol dir bitte Unterstützung bei einem Menschen."),
 ],

 "faq_eyebrow": "Fragen", "faq_h2": "Bevor du dich entscheidest",
 "faq_itens": [
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
 ],

 "cta_h2": "Zwei Minuten. Heute noch.",
 "cta_lede": ("Du brauchst keinen freien Nachmittag und nichts Kaltes. Nur "
              "einen Stuhl."),
 "cta_btn": "Den Atemanker sichern — 10 €",

 "rodape_fine": ("Dieses Paket dient der allgemeinen Information und ersetzt "
                 "keine ärztliche oder psychotherapeutische Beratung. Es "
                 "stellt keine Diagnose und ist kein Medikament. Bei "
                 "Schwangerschaft, Herz- oder Lungenerkrankungen, Epilepsie "
                 "oder sehr niedrigem Blutdruck sprich bitte vorher mit deiner "
                 "Ärztin oder deinem Arzt. Atemübungen niemals im oder am "
                 "Wasser und niemals am Steuer. Ergebnisse sind von Person zu "
                 "Person unterschiedlich."),
 "rodape_direitos": "© 2026. Alle Rechte vorbehalten.",
},

# ===========================================================================
# FRANCES
# ===========================================================================
"fr": {
 "lang": "fr",
 "titulo_doc": "L'Ancre du Souffle — la méthode en 2 minutes contre l'agitation intérieure",
 "meta": ("Deux minutes pour dire à votre corps que le danger est passé. Sept "
          "fichiers, un plan de 21 jours, deux bonus. Sans glace, sans "
          "matériel, chez vous."),
 "marca_mark": "ANCRE",
 "marca": "L'Ancre du Souffle",
 "btn_topo": "Je le veux",
 "capa": "capa-ancre-800x1000.jpg",
 "capa_alt": "L'Ancre du Souffle — la méthode en 2 minutes contre l'agitation intérieure",
 "preco_de": "39", "desconto": "74 %",
 "moeda_sinal": "€", "preco": "10", "centavos": ",00",
 "preco_texto": "10 €",

 "hero_eyebrow": "7 fichiers · 2 bonus offerts · Téléchargement immédiat",
 "hero_h1": ("On ne peut pas se <i>penser</i> calme.<br>"
             "Mais on peut se <i>respirer</i> calme."),
 "hero_lede": ("La méthode en 2 minutes qui donne à votre corps le signal de "
               "sortir de l'alarme permanente. Assise, chez vous, au chaud — "
               "<b>sans glace, sans matériel et sans que personne dans la pièce "
               "ne s'en rende compte.</b>"),
 "hero_badges": [("ic-book", "7", "fichiers"), ("ic-gift", "2", "bonus offerts"),
                 ("ic-bolt", "2", "minutes par exercice"),
                 ("ic-calendar", "21", "jours de plan")],

 "pb_statt": "Au lieu de", "pb_sparen": "d'économie",
 "pb_once": "Paiement unique. À vous pour toujours. Sans abonnement.",
 "pb_btn": "Accéder immédiatement",
 "pb_pay": ["Paiement sécurisé Hotmart", "Envoyé par e-mail", "Garantie 7 jours"],

 "prob_eyebrow": "Pourquoi rien n'a marché jusqu'ici",
 "prob_h2": "Vous avez essayé tout ce qui s'adresse à la tête.",
 "prob_itens": [
   "<b>Les cachets calment la tête.</b> Ils n'atteignent pas la partie qui fait "
   "monter votre pouls et serre votre poitrine.",
   "<b>Parler aide la tête.</b> Personne n'a jamais appris à votre corps "
   "comment redescendre quand il ne se passe plus rien.",
   "<b>Les applications vous comptent les secondes.</b> Elles ne vous "
   "expliquent jamais pourquoi un chiffre doit être plus grand que l'autre — "
   "et c'est pourtant là que tout se joue.",
   "<b>Et le classique : « détends-toi, c'est tout ».</b> Comme si personne "
   "n'avait déjà essayé.",
 ],
 "prob_punch": ("<b>Le problème n'est pas dans la tête. Il est dans le corps</b> "
                "— et le corps n'entend pas les arguments. Il entend un seul "
                "signal, et ce signal est votre expiration."),

 "feat_eyebrow": "La méthode",
 "feat_h2": "Une seule chose à changer — et c'est la bonne",
 "feat_lede": ("Ne pas respirer plus profondément. Ne pas respirer davantage. "
               "Seulement expirer plus longtemps qu'on inspire."),
 "feat_cards": [
   ("ic-pulse", "L'expiration est l'interrupteur",
    "À l'inspiration, votre cœur accélère ; à l'expiration, il ralentit. "
    "Allongez l'expiration et vous allongez exactement la partie où votre "
    "corps redescend. Le principe ne va pas plus loin que ça."),
   ("ic-bolt", "Deux minutes, pas vingt",
    "Douze respirations. C'est un exercice. Celle qui n'a pas vingt minutes "
    "par jour est précisément la personne pour qui ceci a été construit — et "
    "pas celle à qui on trouve une excuse."),
   ("ic-leaf", "Ni glace, ni studio, ni rendez-vous",
    "Il vous faut une chaise. Pas de tapis, pas d'application, pas "
    "d'abonnement, pas de matériel et rien de froid. Cela marche chez vous, "
    "au chaud, assise."),
 ],

 "rail_eyebrow": "Tout ce qu'il y a dedans",
 "rail_h2": "Sept fichiers, dans l'ordre où vous en avez besoin",
 "rail_lede": ("Numérotés de l'Étape 1 au Bonus 2 — vous n'avez jamais à vous "
               "demander ce qui vient ensuite."),
 "rail_hint": "faites glisser pour voir la suite",
 "rail_itens": [
   ("anker", "Étape 2 — L'Ancre du Souffle",
    "L'exercice de base : quatre secondes à l'inspiration, six à l'expiration. "
    "Avec la posture, la main sur les côtes et cinq variantes pour le bureau, "
    "le trajet et la file d'attente."),
   ("lippen", "Étape 3 — L'Ancre d'urgence",
    "Quatre-vingt-dix secondes pour le moment où ça vous tombe dessus. Assise, "
    "sans matériel, sans que personne dans la pièce ne s'en aperçoive."),
   ("plan21", "Étape 4 — Votre plan de 21 jours",
    "Une tâche par jour, jamais plus de cinq minutes. La partie qui transforme "
    "un exercice en habitude — avec le tableau de croix à imprimer."),
   ("abend", "Étape 5 — La routine du soir",
    "Pour la tête qui devient plus bruyante le soir que la journée, et pour "
    "les nuits où vous êtes réveillée à trois heures à faire des calculs."),
   ("handgelenk", "Bonus 1 — Le froid sans glace",
    "Le petit amplificateur au lavabo : de l'eau froide sur le poignet, sur le "
    "visage, les vingt dernières secondes de la douche. Facultatif."),
   ("tagebuch", "Bonus 2 — Votre carnet de calme",
    "Des fiches à imprimer. Au bout de trois semaines, vous voyez noir sur "
    "blanc ce qui a changé — et ce qui vous fait monter à chaque fois."),
   ("haltung", "Étape 1 — Commencez ici",
    "Pourquoi votre corps sonne l'alarme alors qu'il ne se passe rien, "
    "pourquoi c'est l'expiration qui la coupe, et les règles de sécurité."),
 ],

 "cont_h2": "Voici ce que vous recevez",
 "cont_ticks": [
   "<b>L'exercice de base</b> dans ses cinq variantes — chaise, bureau, marche, "
   "position allongée et la version pour celles à qui six secondes font trop",
   "<b>L'Ancre d'urgence :</b> quatre-vingt-dix secondes pour le moment aigu, "
   "plus un exercice pour trois heures du matin",
   "<b>Un plan de 21 jours</b> avec une seule tâche par jour",
   "<b>Une routine du soir complète</b> pour la tête qui devient plus bruyante",
   "<b>Bonus 1 :</b> le froid sans glace — trois niveaux au lavabo",
   "<b>Bonus 2 :</b> le carnet de calme à imprimer",
   "Tous les exercices avec <b>photo et schéma respiratoire</b>, pour voir ce "
   "que vous faites",
   "À imprimer ou à lire sur téléphone, tablette et ordinateur",
   "Accès à vie, payé une seule fois",
 ],

 "bonus_eyebrow": "Offerts avec le lot",
 "bonus_h2": "Deux bonus que vous devriez acheter séparément",
 "bonus_tag": "Bonus", "bonus_gratis": "offert aujourd'hui",
 "bonus_soma": "<b>33 €</b> de valeur au total. Inclus aujourd'hui dans le lot.",
 "bonus_itens": [
   ("1", "ic-shield", "Le froid sans glace",
    "Trois niveaux au lavabo et sous la douche, chacun sous les trente "
    "secondes. Avec les règles qui, elles, ne se négocient pas.", "19"),
   ("2", "ic-calendar", "Votre carnet de calme",
    "Des feuilles de semaine, une feuille de déclencheurs et trois questions "
    "du soir. À imprimer, pour avoir au bout de 21 jours autre chose qu'une "
    "impression.", "14"),
 ],

 "pass_eyebrow": "Comment ça se passe",
 "pass_h2": "D'ici au premier exercice, il y a quelques minutes",
 "pass_itens": [
   ("Vous prenez le lot", "Via le paiement sécurisé Hotmart. Paiement unique, "
    "sans abonnement, sans reconduction."),
   ("Il arrive dans votre boîte mail", "En quelques minutes, sous forme de "
    "sept fichiers PDF à télécharger. Sur téléphone, tablette, ordinateur ou "
    "imprimés."),
   ("Vous commencez aujourd'hui", "Pas lundi prochain. Lire l'Étape 2, faire "
    "une fois, terminé. Cela prend cinq minutes, une seule fois."),
 ],

 "off_eyebrow": "L'offre",
 "off_h2": "Moins qu'un café et une part de gâteau",
 "off_lede": "Un paiement. Livraison immédiate. À vous pour toujours.",
 "off_h3": "Voici ce qui arrive dans votre boîte mail",
 "off_ticks": [
   "<b>L'Ancre du Souffle</b> — le lot complet, sept fichiers",
   "L'exercice de base avec cinq variantes du quotidien",
   "L'Ancre d'urgence pour le moment aigu",
   "Le plan de 21 jours avec le tableau de croix",
   "La routine du soir pour des nuits plus calmes",
   "<b>Bonus 1 :</b> le froid sans glace",
   "<b>Bonus 2 :</b> votre carnet de calme à imprimer",
   "Téléchargement immédiat, à vous pour toujours",
 ],
 "off_once": "Un paiement. Sans abonnement. Sans reconduction.",
 "off_btn": "Oui, je veux L'Ancre du Souffle",
 "off_note": ("Paiement sécurisé Hotmart. Livraison par e-mail en quelques "
              "minutes."),

 "gar_dias": "7", "gar_dias_lab": "jours",
 "gar_h2": "Essayez tout pendant une semaine. À nos frais.",
 "gar_p1": ("Achetez-le, téléchargez-le et pratiquez sept jours. Si cela ne "
            "vous apporte rien, vous nous écrivez et vous êtes remboursée — "
            "sans formulaire, sans justification, sans question. Les fichiers "
            "sont déjà sur votre appareil, et ils y restent."),
 "gar_p2": "La seule chose que vous risquez ici, c'est deux minutes.",

 "nicht_eyebrow": "Rester honnête",
 "nicht_h2": "Ce que ce lot ne promet <i>pas</i>",
 "nicht_lede": ("Quand on est constamment agitée, on nous a déjà assez promis. "
                "Voici donc d'abord ce que nous n'affirmons pas."),
 "nicht_itens": [
   ("Cela ne vide pas votre tête.", "Personne ne vous le promet ici. "
    "L'objectif est plus petit et plus honnête : redescendre plus vite qu'avant."),
   ("Ce n'est pas un traitement.", "L'Ancre du Souffle est un exercice. Elle "
    "ne remplace ni médecin ni psychothérapie, ne pose aucun diagnostic et "
    "n'est pas un médicament. Si vous prenez un traitement, vous continuez."),
   ("Une fois ne suffit pas.", "La première fois, il ne se passe souvent rien "
    "du tout. L'effet vient de la répétition — c'est pour cela que le lot "
    "contient un plan de 21 jours et pas un exercice miracle."),
   ("Ce n'est pas le bon moment pour tout le monde.", "Si vous traversez en ce "
    "moment une crise psychique aiguë, ce n'est pas votre prochaine étape. "
    "Cherchez alors de l'aide auprès d'un être humain."),
 ],

 "faq_eyebrow": "Questions", "faq_h2": "Avant de vous décider",
 "faq_itens": [
   ("C'est la même chose que les bains de glace ?",
    "Non. Chez nous, le froid est un bonus facultatif au lavabo, et vous "
    "pouvez le supprimer entièrement sans rien perdre. La méthode elle-même se "
    "pratique au chaud, assise et habillée."),
   ("Dois-je inspirer profondément ou bloquer ma respiration ?",
    "Non, et c'est important : dans ce lot, on n'hyperventile nulle part et on "
    "ne bloque jamais la respiration poumons vides. Respirer vite et "
    "profondément en continu produit exactement les sensations dont vous "
    "voulez vous débarrasser."),
   ("De combien de temps ai-je vraiment besoin ?",
    "Deux minutes par exercice. À partir de la semaine 2, le plan en prévoit "
    "deux par jour — cela fait quatre minutes. Sur la durée, il n'en faut pas "
    "plus."),
   ("Je n'ai jamais réussi ce truc du comptage.",
    "C'est pour cela que l'Étape 2 consacre un exercice entier à ce que vous "
    "faites quand six secondes vous paraissent trop longues, et propose une "
    "variante où vous ne comptez pas les secondes mais les pas."),
   ("Sous quel format cela arrive-t-il ?",
    "Sept fichiers PDF, numérotés de l'Étape 1 au Bonus 2, réunis dans un "
    "fichier ZIP. Pas d'espace de cours, pas de vidéo, rien qui expire."),
   ("Est-ce indiqué pendant la grossesse ?",
    "Pendant la grossesse, parlez-en d'abord à votre médecin — c'est aussi "
    "écrit dans l'Étape 1. Il en va de même en cas de maladie cardiaque ou "
    "pulmonaire, d'épilepsie et de tension très basse."),
   ("Et si cela ne m'apporte rien ?",
    "Vous écrivez dans les 7 jours et vous êtes remboursée. Sans formulaire et "
    "sans justification."),
 ],

 "cta_h2": "Deux minutes. Dès aujourd'hui.",
 "cta_lede": ("Vous n'avez besoin ni d'un après-midi libre ni de quoi que ce "
              "soit de froid. Juste d'une chaise."),
 "cta_btn": "Prendre L'Ancre du Souffle — 10 €",

 "rodape_fine": ("Ce lot est fourni à titre d'information générale et ne "
                 "remplace pas un avis médical ou psychothérapeutique. Il ne "
                 "pose aucun diagnostic et n'est pas un médicament. En cas de "
                 "grossesse, de maladie cardiaque ou pulmonaire, d'épilepsie "
                 "ou de tension très basse, parlez-en d'abord à votre médecin. "
                 "Ne pratiquez jamais d'exercices de respiration dans l'eau ou "
                 "au bord de l'eau, ni au volant. Les résultats varient d'une "
                 "personne à l'autre."),
 "rodape_direitos": "© 2026. Tous droits réservés.",
},
}
