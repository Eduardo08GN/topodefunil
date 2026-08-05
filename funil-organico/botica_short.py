#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
botica_short.py — randomizador + gerador + linter do AGENTE **BOTICA** (SHORT).

⭐ FONTE: True Health, reel facebook.com/reel/3973945436069257 (52,2s).
**1K reacoes / 1K comentarios / 53 shares** — e comentario e' o KPI do nosso
funil, entao a razao 1:1 com reacao e' o numero que importa aqui.
Baixado pela rota 2b do RUNBOOK-watch-videos, transcrito com Whisper e lido
frame a frame em 2026-08-04.

⭐ O QUE E' O ANGULO, em uma frase: uma mulher de traje tradicional, numa cozinha
forrada de potes de ervas secas, prepara uma receita caseira na frente da camera
— e o vilao e' a FARMACIA. A botica de casa contra a botica da esquina.

⛔ O QUE NENHUM DOS 13 AGENTES ANTERIORES TEM: a prova e' a **receita sendo
PREPARADA em cena**, com utensilio em movimento. Os outros mostram bancada
parada ou despejo; aqui a mao trabalha.

O ARCO — 3 cenas de 8s, destino AdBatch Vertical 3:

    cena 1  A ISCA      o prop gigante na lente + o despejo + O VILAO
    cena 2  O PREPARO   o metodo em acao + o ingrediente raro + gelatin trick
    cena 3  O COPO      o copo na lente + o HOMEM MUDO atras + o CTA

⚠️ A FALA DA FONTE, integral, que este motor TRADUZ (nunca inventa):
    "Did you know that if you add saffron to banana, this happens?
     Pharmacies don't want you to know this.
     In a mixer, add one chopped banana, a pinch of saffron, then add a
     tablespoon of honey, and squeeze half a lime. You can buy some of these
     products at Walmart or Costco. In the end, add a glass of water and blend
     well. Drink this every morning to increase blood flow and circulation to
     your wiener naturally. Want to learn another natural trick that could help
     your wiener grow up to 5 inches faster in a week? Comment wiener below and
     I'll personally send it to you. But don't forget to follow me. Otherwise,
     I can't find you."

⚠️ O Whisper ouviu `winner`: e' **wiener**, que ja' e' palavra do nosso NUCLEO.

⛔⛔ AS SEIS ORDENS DO OPERADOR NESTE AGENTE (2026-08-04), todas verificadas por
linter, nao por comentario:

  1. O METODO DE PREPARO NAO E' FIXO. *"nao fixe liquidificador = vai engessar o
     repertorio visual do take e tornar os videos muito parecidos entre si"*.
     O liquidificador da fonte e' UMA entrada de METODOS, nao a cena.
  2. O PROP sai do pool **ja' validado prompt a prompt no COLO** — banana,
     banana-da-terra, berinjela, cenoura, pastinaca. Pepino e abobrinha foram
     recusados pelo gerador e nao entram.
  3. ETNIA ARRASTA O MUNDO, e o pool inclui o americano tipico.
  4. UM ingrediente raro por video, sorteado entre os nove.
  5. O homem da cena 3 e' MUDO.
  6. ⛔ ZERO claim numerico de centimetro. A fonte promete "5 inches faster in a
     week"; nos ficamos com a promessa sem a medida.

⭐⭐ E ESTE AGENTE NASCE COM A §21 APLICADA: a PRIMEIRA sentenca de cada cena
nomeia o referente. Nao ha' uma abertura orfa neste motor, por construcao e por
linter (BO9). E' o primeiro que nasce assim.

Uso:
    python funil-organico/botica_short.py --pagina joe --n 1
    python funil-organico/botica_short.py --pagina ray --n 3 --seed 42 --dry-run
    python funil-organico/botica_short.py --autoteste
"""

import argparse
import collections
import json
import os
import random
import re

import short_comum as sc
from nucleo_sonoro import sonorizar

AQUI = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(AQUI, ".botica-short-ledger.json")

TITULO = "AGENTE BOTICA SHORT"
SLUG = "botica-short"
SUBTITULO = ("a botica de casa contra a farmacia · o preparo e' a prova · "
             "gerador offline de prompts Veo")

ETNIA = {
    "joe": "white American", "ray": "white American", "matt": "white American",
    "marcus": "Black American", "chuck": "Black American",
    "hank": "white American", "wade": "white American",
    "isaiah": "Black American", "curtis": "Black American",
    "otis": "Black American",
}


# ---------------------------------------------------------------------------
# STRINGS TRAVADAS — leitura otica da fonte. NAO REESCREVER.
# ---------------------------------------------------------------------------

# ⭐⭐ BO1 — A ISCA NA LENTE. E' o hook inteiro em uma frase, lido no frame 0:00:
# o prop descascado ocupa METADE do quadro porque esta' empurrado para a lente,
# perto da camera, e o corpo dela fica pequeno atras. A tacinha da substancia
# vem na outra mao, mais alta, e despeja por cima aos 0:05.
# ⛔ A escala vem do ENQUADRAMENTO (mao esticada para a lente), nunca de dizer
# que o objeto e' gigante: `absurdly oversized` esta' no selo de risco do
# banco-hooks e ja' custou recusa.
BO_ISCA = (
    "Filmed straight on at chest height. Her left hand is stretched out towards "
    "the camera holding %s, close enough to the lens that it fills the left half "
    "of the frame while she stands smaller behind it. Her right hand is raised "
    "higher at frame-right holding %s, tipped over so that %s is falling onto "
    "the top of it in a thin scatter. She is looking straight into the lens with "
    "her mouth open mid-word as she speaks, her front teeth even and complete."
)

# ⛔ BO2 — no TAKE da cena 1 o prop NAO muda de estado. Este agente nao tem
# crescimento: quem cresce e' o RESSURREICAO. O bit visual aqui e' o DESPEJO.
# ⚠️ Nunca `completely motionless` num objeto que a mao segura — ordem impossivel,
# e o Veo resolve SOLTANDO o objeto (F12b). Diz-se pela POSICAO.
BO_ISCA_ESTAVEL = (
    "Her left hand keeps it in exactly the same place, at the same distance from "
    "the lens, same size, same shape, same colour. Her right hand keeps the dish "
    "at the same height and the same tilt. Only the falling scatter moves."
)

# ⭐⭐ BO3 — O PREPARO. ⛔ ORDEM DO OPERADOR: o utensilio NAO E' FIXO. A fonte usa
# liquidificador; travar isso faria os videos deste agente parecerem o mesmo
# video. O metodo entra pelo pool METODOS e o verbo acompanha.
BO_PREPARO = (
    "Medium shot in %(coz)s, filmed straight on at the height of the %(sup)s, "
    "framed so that %(sup_a)s runs across the bottom third of the picture. "
    "Standing behind it, centred in the frame, is %(ancora)s. On the %(sup)s in "
    "front of her stands %(vaso)s, and beside it %(comum_img)s and %(raro_img)s. "
    "Her right hand is closed around %(vaso_curto)s, the whole hand visibly "
    "wrapped around it, her forearm resting steady on the %(sup)s as she %(acao)s. "
    "Her left hand rests flat on the %(sup)s beside it. She looks directly into "
    "the lens with her mouth open mid-word as she speaks, her expression serious "
    "and certain. She is the only person in the frame."
)

# ⛔ BO4 — ela nunca toca no resto da bancada. Sem isto o Veo comeca a mexer em
# tudo o que esta' em quadro e a continuidade entre os blocos de 8s morre.
BO_NAO_TOCA = ("Nothing else on the %s is touched, moved, opened or lifted, and "
               "nothing is added to it or taken away.")

# ⭐ BO5 — O COPO DO PAYOFF, lido em 0:30: ela empurra o copo para a lente com a
# mao, o liquido opaco e cremoso, dois canudos dentro.
# ⛔ Ele so' existe na CENA 3, e e' o objeto da keyword — esta' na mao no frame em
# que a boca diz `gelatin,`. Mostra-lo antes entrega o payoff antes da promessa.
BO_COPO = ("a tall clear glass filled to the top with a thick pale drink, two "
           "paper straws standing in it")

# ⭐⭐ BO6 — O HOMEM MUDO. Ordem do operador: *"no take final, alem do ref
# falando, havera um homem sempre atras, com cara de espanto e surpresa e
# olhando para o objeto na mao do ref"*.
# ⛔ Ele olha para O COPO, nunca para a lente, e NUNCA fala. E' a mesma mecanica
# da plateia congelada do ESCANDALO: ele encena o espanto NO LUGAR do espectador.
# ⚠️ `Only she speaks` e' obrigatorio no TAKE — sem isso o segundo corpo dubla a
# fala dela, que e' a falha que derrubou a cena do casal do VAZAMENTO.
BO_HOMEM = (
    "Standing behind her and slightly to frame-left, close enough to be in the "
    "same focus, is a %d-year-old %s man, %s, wearing %s. His eyes are wide and "
    "his eyebrows are raised, his mouth open in plain astonishment, and he is "
    "looking directly at the glass in her hand — never at the camera."
)
BO_HOMEM_TAKE = (
    "The man behind her holds his astonished expression without moving, eyes "
    "fixed on the glass the whole time, and never speaks. Only she speaks, "
    "straight into the lens."
)

# ⛔ BO7 — A ANCORA DE CONTINUIDADE. Rosto E idade, nunca so' roupa: no VAZAMENTO
# a ancora estava na camisa e o render devolveu um senhor de oculos e bigode no
# lugar do corpo-prova.
# ⚠️ Comeca em minuscula: entra no meio da frase e o `_cap` a levanta quando abre.
BO_ANCORA = ("the same %d-year-old %s woman from the first scene, same %s, same "
             "%s, same %s")

ANTICELEB = ("Ordinary relatable face, not a celebrity, not a model, not an "
             "actor, not resembling any famous person.")
CAUDA = "Shot on iPhone, natural grain. No on-screen text, no watermark."


# ---------------------------------------------------------------------------
# ⭐⭐ MUNDOS — A BOTICA, E A ETNIA SAI DE DENTRO DELA
# ---------------------------------------------------------------------------
# ⛔ NAO EXISTE EIXO `etnia` SOLTO. Ordem do operador: *"variar etnia e' arrastar
# o mundo inteiro — cenario, traje, luz, audio"*. Aqui o mundo carrega tambem a
# TRADICAO DE ERVAS, que e' a autoridade do angulo.
# ⚠️ O operador mandou incluir o americano tipico no pool ("mundo entre varios,
# inclui tb o tipico cidadao norte americano").
# ⛔ ZERO texto legivel em qualquer set: a CAUDA promete "No on-screen text", e
# pote de erva com etiqueta escrita e' texto em cena. Os potes entram como
# `unlabelled glass jars`.
# ⚠️ O selo `V` fica so' no mundo da fonte (o amish); os outros sao `N`.
MUNDOS = [
    {"id": "amish", "selo": "V", "familia": "amish",
     "etnias": ["white American"],
     "coz": "a rustic timber farmhouse kitchen with open shelves of unlabelled "
            "glass jars of dried herbs from floor to ceiling, a hand pump by "
            "the basin and a wide plank table",
     "coz_c": "timber herb kitchen",
     "sup_a": "a heavy scrubbed pine table", "sup": "table",
     "traje": "%s long-sleeved high-collared dress under a black bib apron, "
              "with a white cap tied under the chin",
     "curto": "black bib apron",
     "cores": ["deep plum", "dark brown", "slate blue", "forest green"],
     "luz": "Soft daylight coming in from a window at frame-right.",
     "luz_c": "soft window daylight",
     "audio": "quiet room tone, a wood floor creaking"},

    {"id": "americana_comum", "selo": "N", "familia": "americana",
     "etnias": ["white American"],
     "coz": "an ordinary American suburban kitchen, honey-oak cabinets and a "
            "row of unlabelled glass spice jars on a shelf above the sink, a "
            "kettle on the hob and a window looking onto the yard",
     "coz_c": "oak suburban kitchen",
     "sup_a": "a speckled granite countertop", "sup": "countertop",
     "traje": "%s knit sweater with the sleeves pushed back",
     "curto": "knit sweater",
     "cores": ["cream", "dusty rose", "navy", "sage"],
     "luz": "Warm overhead kitchen light with weak daylight behind it.",
     "luz_c": "warm overhead light",
     "audio": "a fridge humming, quiet room tone"},

    {"id": "apalache", "selo": "N", "familia": "apalache",
     "etnias": ["white American"],
     "coz": "a mountain-lodge kitchen with finished pine panelling, bundles of "
            "dried plants hanging from a rail and rows of unlabelled jars "
            "behind glass cabinet doors, a black enamel range in the corner",
     "coz_c": "pine lodge kitchen",
     "sup_a": "a thick oiled butcher-block counter", "sup": "counter",
     "traje": "%s quilted flannel shirt with the sleeves rolled",
     "curto": "quilted flannel shirt",
     "cores": ["dark red", "forest green", "brown", "slate blue"],
     "luz": "Low grey mountain daylight through a small window at frame-left.",
     "luz_c": "low grey daylight",
     "audio": "wind at the window, a stove ticking"},

    {"id": "sulista", "selo": "N", "familia": "sulista",
     "etnias": ["Black American"],
     "coz": "a Southern kitchen with pale yellow beadboard walls, a screen door "
            "open onto a green yard, unlabelled mason jars of dried leaves and "
            "roots along an open shelf and a cast-iron skillet on the hob",
     "coz_c": "yellow beadboard kitchen",
     "sup_a": "a pale blue painted wooden counter", "sup": "counter",
     "traje": "%s short-sleeved button-down shirt",
     "curto": "button-down shirt",
     "cores": ["cream", "sky blue", "khaki", "soft grey"],
     "luz": "Bright soft daylight through the open screen door.",
     "luz_c": "bright daylight through the door",
     "audio": "cicadas outside, a screen door creaking"},

    {"id": "mexicana", "selo": "N", "familia": "mexicana",
     "etnias": ["Mexican American"],
     "coz": "a Mexican American kitchen with hand-painted blue and yellow tiles "
            "across the backsplash, clay pots and unlabelled jars of dried "
            "herbs stacked on an open shelf and a flat steel comal on the hob",
     "coz_c": "talavera-tiled kitchen",
     "sup_a": "a terracotta-tiled counter", "sup": "counter",
     "traje": "%s embroidered cotton blouse",
     "curto": "embroidered blouse",
     "cores": ["cream", "pale blue", "tan", "deep red"],
     "luz": "Warm afternoon sun coming in low from frame-left.",
     "luz_c": "warm low afternoon sun",
     "audio": "a radio playing faintly in another room"},

    {"id": "caribenha", "selo": "N", "familia": "caribenha",
     "etnias": ["Caribbean American"],
     "coz": "a Caribbean kitchen with mint-green walls and louvred windows "
            "standing open onto broad green leaves, unlabelled jars of bark and "
            "dried flowers on a fitted shelf and matched enamel bowls by the sink",
     "coz_c": "mint-green island kitchen",
     "sup_a": "a pale speckled stone counter", "sup": "counter",
     "traje": "%s loose linen blouse worn open at the collar",
     "curto": "loose linen blouse",
     "cores": ["white", "pale yellow", "sea blue", "sand"],
     "luz": "Hard bright island daylight coming through the louvres.",
     "luz_c": "hard bright daylight",
     "audio": "birds outside, a ceiling fan turning"},

    {"id": "leste_asia", "selo": "N", "familia": "asiatica",
     "etnias": ["East Asian American"],
     "coz": "a compact East Asian kitchen with a wall of small wooden drawers "
            "and unlabelled glass jars of dried roots and bark, a clay pot on "
            "the hob and a bamboo steamer stacked on a shelf",
     "coz_c": "wooden-drawer kitchen",
     "sup_a": "a pale grey stone counter", "sup": "counter",
     "traje": "%s round-collared cotton jacket",
     "curto": "cotton jacket",
     "cores": ["indigo", "oat", "charcoal", "moss green"],
     "luz": "Even cool daylight from a window behind the camera.",
     "luz_c": "even cool daylight",
     "audio": "a clay pot simmering, quiet room tone"},

    {"id": "sul_asia", "selo": "N", "familia": "sul_asiatica",
     "etnias": ["South Asian American"],
     "coz": "a South Asian kitchen with polished stone surfaces, a row of round "
            "steel tins and unlabelled jars of coloured powders along an open "
            "shelf, a heavy pestle and a steel tumbler beside the sink",
     "coz_c": "polished stone kitchen",
     "sup_a": "a dark polished granite counter", "sup": "counter",
     "traje": "%s long-sleeved kurta",
     "curto": "kurta",
     "cores": ["off-white", "pale blue", "sand", "deep maroon"],
     "luz": "Warm even daylight from a window at frame-right.",
     "luz_c": "warm even daylight",
     "audio": "a pressure cooker hissing softly, quiet room tone"},

    {"id": "africa_oeste", "selo": "N", "familia": "africana",
     "etnias": ["West African"],
     "coz": "a well-kept West African kitchen with glazed tiled walls, rows of "
            "unlabelled jars and calabashes of dried bark and seed in a fitted "
            "cabinet, a carved mortar on the side and a door open onto a swept "
            "green courtyard",
     "coz_c": "tiled West African kitchen",
     "sup_a": "a polished dark granite counter", "sup": "counter",
     "traje": "%s short-sleeved embroidered cotton tunic",
     "curto": "embroidered tunic",
     "cores": ["white", "indigo", "sand", "deep green"],
     "luz": "Strong flat daylight coming through the open doorway.",
     "luz_c": "strong flat daylight",
     "audio": "voices far off outside, quiet room tone"},

    {"id": "africa_leste", "selo": "N", "familia": "africana",
     "etnias": ["East African"],
     "coz": "a tidy East African kitchen with pale tiled walls and a wide "
            "shuttered window, woven baskets and unlabelled jars of dried "
            "leaves ranged along a fitted shelf, a stainless kettle on the hob",
     "coz_c": "pale tiled kitchen",
     "sup_a": "a solid hardwood worktop", "sup": "worktop",
     "traje": "%s open-collared cotton shirt",
     "curto": "cotton shirt",
     "cores": ["white", "pale grey", "tan", "sky blue"],
     "luz": "Soft daylight through the shutters at frame-left.",
     "luz_c": "soft shuttered daylight",
     "audio": "a kettle ticking, quiet room tone"},

    {"id": "mediterranea", "selo": "N", "familia": "mediterranea",
     "etnias": ["Mediterranean"],
     "coz": "a whitewashed Mediterranean kitchen with a low arched window, "
            "bunches of dried herbs hanging on a hook, unlabelled jars of seed "
            "and leaf on an open shelf and a large tin of oil by the door",
     "coz_c": "whitewashed arched kitchen",
     "sup_a": "a thick pale marble counter", "sup": "counter",
     "traje": "%s linen blouse with the sleeves rolled",
     "curto": "linen blouse",
     "cores": ["white", "pale blue", "sand", "olive"],
     "luz": "Hard bright Mediterranean sun through the arched window.",
     "luz_c": "hard bright sun",
     "audio": "gulls far off, quiet room tone"},

    {"id": "andina", "selo": "N", "familia": "andina",
     "etnias": ["Andean South American"],
     "coz": "an Andean kitchen with smooth painted walls and a tiled splashback, "
            "fine woven cloth folded on a bench, labelled sacks and jars of "
            "dried root and grain squared along a built shelf and a glazed "
            "tiled stove in the corner",
     "coz_c": "tiled andean kitchen",
     "sup_a": "a thick oiled hardwood work table", "sup": "table",
     "traje": "%s woven wool cardigan over a plain blouse",
     "curto": "wool cardigan",
     "cores": ["deep red", "burnt orange", "cream", "indigo"],
     "luz": "Cool high-altitude daylight from a small window at frame-right.",
     "luz_c": "cool high daylight",
     "audio": "wind outside, quiet room tone"},
]

FAMILIAS_MUNDO = list(dict.fromkeys(m["familia"] for m in MUNDOS))


# ---------------------------------------------------------------------------
# ⭐ METODOS — O PREPARO, E ELE NAO E' FIXO
# ---------------------------------------------------------------------------
# ⛔⛔ ORDEM DO OPERADOR, 2026-08-04: *"nao fixe liquidificador = vai engessar o
# repertorio visual do take e tornar os videos muito parecidos entre si e
# repetitivos"*.
# A fonte usa liquidificador; aqui ele e' UMA entrada de doze. O `acao` e' o
# verbo que o TAKE anima, e ele acompanha o utensilio — sem isso o bloco manda
# "she blends" com um pilao na mao.
# ⚠️ `vaso_curto` existe para a pegada anti-F12b: punho inteiro em volta do
# recipiente. O Veo solta objeto que a mao "segura" sem estar descrito.
METODOS = [
    {"id": "liquidificador", "selo": "V",
     "vaso": "a glass blender jug on its base",
     "curto": "the blender jug",
     "acao": "tips the last of it in and sets the lid on",
     "fala": "Blend it"},
    {"id": "pilao", "selo": "N",
     "vaso": "a heavy stone mortar with the pestle standing in it",
     "curto": "the stone mortar",
     "acao": "works the pestle round in slow circles",
     "fala": "Grind it down"},
    {"id": "jarra_colher", "selo": "N",
     "vaso": "a tall glass jug with a long wooden spoon in it",
     "curto": "the glass jug",
     "acao": "turns the long spoon through it twice",
     "fala": "Stir it through"},
    {"id": "tigela_fouet", "selo": "N",
     "vaso": "a wide ceramic bowl with a wire whisk resting in it",
     "curto": "the ceramic bowl",
     "acao": "beats it with the whisk in short strokes",
     "fala": "Whisk it together"},
    {"id": "garrafa", "selo": "N",
     "vaso": "a capped glass bottle half full",
     "curto": "the glass bottle",
     "acao": "caps it and shakes it twice",
     "fala": "Shake it hard"},
    {"id": "bule_infusor", "selo": "N",
     "vaso": "a clear glass teapot with a metal infuser basket sitting in the top",
     "curto": "the glass teapot",
     "acao": "presses the infuser basket down into it",
     "fala": "Steep it"},
    {"id": "moedor", "selo": "N",
     "vaso": "a hand-crank grinder clamped to the edge of the surface",
     "curto": "the grinder",
     "acao": "turns the crank steadily",
     "fala": "Grind it fine"},
    {"id": "coador_pano", "selo": "N",
     "vaso": "a wide jar with a square of cloth tied over its mouth",
     "curto": "the cloth-covered jar",
     "acao": "presses the mixture through the cloth with the back of a spoon",
     "fala": "Strain it"},
    {"id": "panela_esmalte", "selo": "N",
     "vaso": "a small enamel pan on a low flame",
     "curto": "the enamel pan",
     "acao": "folds it through with a wooden spoon",
     "fala": "Warm it through"},
    {"id": "almofariz_madeira", "selo": "N",
     "vaso": "a deep wooden mortar with a long pestle",
     "curto": "the wooden mortar",
     "acao": "pounds it down with the long pestle",
     "fala": "Pound it"},
    {"id": "prensa_frances", "selo": "N",
     "vaso": "a glass press pot with the plunger raised",
     "curto": "the press pot",
     "acao": "pushes the plunger slowly down through it",
     "fala": "Press it down"},
    {"id": "peneira_tigela", "selo": "N",
     "vaso": "a fine metal sieve resting over a glass bowl",
     "curto": "the metal sieve",
     "acao": "taps the sieve so it falls through into the bowl",
     "fala": "Sift it in"},
]


# ---------------------------------------------------------------------------
# ⭐⭐ RAROS — OS INGREDIENTES QUE O OPERADOR MANDOU ENTRAR
# ---------------------------------------------------------------------------
# ⛔ ORDEM DO OPERADOR, 2026-08-04, com a diretiva de incorporacao inteira:
#
#     [NOME POPULAR] + [APOSTO CONTEXTUAL DISTINTIVO E SUCINTO]
#
# O aposto existe para que quem NUNCA ouviu falar do ingrediente entenda na hora
# O QUE E', DE ONDE VEM ou POR QUE E' RECONHECIVEL.
#
# ⛔ O QUE O APOSTO NAO PODE SER: descricao visual generica da planta. *"aquela
# raiz redondinha"*, *"aquelas sementes amarelas"* nao identificam nada — varias
# plantas compartilham isso. O aposto e' ORIGEM, TRADICAO, NOME POPULAR
# ALTERNATIVO ou caracteristica botanica realmente distintiva.
#
# ⛔ ZERO NOME CIENTIFICO NA FALA. O binomio vive no campo `interno`, que existe
# so' para producao e NUNCA entra no prompt. Falar `Lepidium meyenii` quebra o
# tom UGC na hora.
#
# ⛔ NAO INVENTAR: origem, propriedade, povo, regiao, historia ou beneficio. Se a
# caracteristica nao for defensavel, a formulacao fica mais neutra. Cada aposto
# abaixo e' factualmente sustentavel.
#
# ⚠️ REGRA DE ECONOMIA: 3 a 10 palavras. E de NATURALIDADE: as construcoes VARIAM
# — `that root...`, `a traditional herb...`, `the famous...`, `the leaf off
# that...`, `known for generations...`. Nao pode parecer doze copias da mesma
# formula gramatical, que e' o que o operador pediu explicitamente.
RAROS = [
    {"id": "maca", "nome": "maca root", "interno": "Lepidium meyenii",
     "aposto": "that Andean root from Peru",
     "img": "a small dish of pale yellow maca powder"},
    {"id": "tongkat", "nome": "tongkat ali", "interno": "Eurycoma longifolia",
     "aposto": "a root from the forests of Southeast Asia",
     "img": "a small dish of coarse light-brown root shavings"},
    {"id": "tribulus", "nome": "tribulus", "interno": "Tribulus terrestris",
     "aposto": "that spiny fruit that grows along the ground",
     "img": "a small dish of dried spiny seed pods"},
    {"id": "epimedium", "nome": "epimedium", "interno": "Epimedium spp.",
     "aposto": "the herb they call horny goat weed",
     "img": "a small dish of dried heart-shaped leaves"},
    {"id": "fenogrego", "nome": "fenugreek", "interno": "Trigonella foenum-graecum",
     "aposto": "the golden seed of the Mediterranean",
     "img": "a small dish of hard golden-brown seeds"},
    {"id": "muirapuama", "nome": "muira puama", "interno": "Ptychopetalum olacoides",
     "aposto": "an Amazon root known for generations",
     "img": "a small dish of chipped pale bark and root"},
    {"id": "ginkgo", "nome": "ginkgo", "interno": "Ginkgo biloba",
     "aposto": "the leaf off that ancient Chinese tree",
     "img": "a small dish of dried fan-shaped leaves"},
    {"id": "mucuna", "nome": "mucuna", "interno": "Mucuna pruriens",
     "aposto": "the famous velvet bean of the tropics",
     "img": "a small dish of dark glossy beans"},
    {"id": "salsaparrilha", "nome": "sarsaparilla", "interno": "Smilax spp.",
     "aposto": "a vine root native to the Americas",
     "img": "a small dish of dried twisted root pieces"},
]

# ⛔ O APOSTO E' OBRIGATORIO E O LINTER COBRA (BO8). Sem ele o ingrediente e' um
# nome aleatorio jogado no roteiro, e o espectador pensa "esse cara comecou a dar
# uma aula de botanica" — que e' o oposto do objetivo.


# ---------------------------------------------------------------------------
# ⭐ COMUNS — o que ja' esta' na cozinha das pessoas
# ---------------------------------------------------------------------------
# ⚠️ CASADOS E COMPLEMENTARES aos raros, nunca excludentes (ordem do operador).
# A receita e' sempre `comum + gelatina + raro`.
COMUNS = [
    {"id": "mel", "nome": "raw honey",
     "img": "an open jar of thick amber honey with a wooden dipper"},
    {"id": "limao", "nome": "half a lemon",
     "img": "a lemon cut in half on a small board"},
    {"id": "bicarbonato", "nome": "baking soda",
     "img": "an unlabelled squat orange tub of white powder"},
    {"id": "canela", "nome": "ground cinnamon",
     "img": "a short unlabelled jar of red-brown powder"},
    {"id": "gengibre", "nome": "fresh ginger",
     "img": "a knob of fresh ginger root grated into a dish"},
    {"id": "curcuma", "nome": "turmeric",
     "img": "an unlabelled jar of deep yellow powder"},
    {"id": "aveia", "nome": "a spoon of oats",
     "img": "a small bowl of rolled oats"},
    {"id": "leite", "nome": "warm milk",
     "img": "a small jug of milk"},
    {"id": "beterraba", "nome": "beet powder",
     "img": "a shallow dish of deep red powder"},
    {"id": "caiena", "nome": "a pinch of cayenne",
     "img": "a tiny unlabelled shaker of bright red powder"},
]


# ---------------------------------------------------------------------------
# ⭐ SUBSTANCIAS — o que ela despeja sobre o prop na cena 1
# ---------------------------------------------------------------------------
# ⚠️ A fonte despeja acafrao em fios vermelhos sobre a banana branca, e o
# CONTRASTE de cor e' metade do bit visual. Todas as entradas caem em fio, po' ou
# grao visivel — liquido transparente nao se ve' cair no scroll.
SUBSTANCIAS = [
    {"id": "acafrao", "selo": "V", "nome": "saffron",
     "dish": "a small glass dish of deep red saffron threads",
     "queda": "a scatter of fine red threads"},
    {"id": "paprica", "selo": "N", "nome": "smoked paprika",
     "dish": "a small glass dish of dark red powder",
     "queda": "a fall of fine dark red powder"},
    {"id": "hibisco", "selo": "N", "nome": "dried hibiscus",
     "dish": "a small glass dish of dried crimson petals",
     "queda": "a scatter of dried crimson petals"},
    {"id": "cravo", "selo": "N", "nome": "whole cloves",
     "dish": "a small glass dish of dark brown cloves",
     "queda": "a scatter of small dark cloves"},
    {"id": "erva_mate", "selo": "N", "nome": "crushed green tea",
     "dish": "a small glass dish of coarse green leaf",
     "queda": "a fall of coarse green leaf"},
    {"id": "semente_abobora", "selo": "N", "nome": "pumpkin seed",
     "dish": "a small glass dish of flat green seeds",
     "queda": "a scatter of flat green seeds"},
    {"id": "canela_pau", "selo": "N", "nome": "crushed cinnamon",
     "dish": "a small glass dish of coarse red-brown bark",
     "queda": "a fall of coarse red-brown bark"},
    {"id": "rosa_mosqueta", "selo": "N", "nome": "crushed rosehip",
     "dish": "a small glass dish of coarse orange-red pieces",
     "queda": "a scatter of coarse orange-red pieces"},
]


# ---------------------------------------------------------------------------
# ⭐ PROPS — reuso do pool VALIDADO PROMPT A PROMPT no COLO (2026-08-03)
# ---------------------------------------------------------------------------
# ⛔ ORDEM DO OPERADOR: *"use o pool"*. Sao CINCO e isso e' de proposito.
#   PASSA  quem quebra a leitura de cilindro — casca dobrada (banana,
#          banana-da-terra), afunilamento conico (cenoura, pastinaca) ou cabo
#          no topo (berinjela)
#   CAI    cilindro de DIAMETRO CONSTANTE terminando em PONTA ROMBA — pepino
#          (2 recusas), abobrinha (1), daikon (1)
# ⛔ Nao completar o pool com entradas nao testadas para "bater o piso": foi
# exatamente esse o erro que o COLO documenta. Pool e' o que passou.
PROPS = [
    {"id": "banana_da_terra", "selo": "V", "nome": "plantain",
     "img": "a large green plantain, peeled halfway with the thick peel folded "
            "back around its base"},
    {"id": "banana", "selo": "V", "nome": "banana",
     "img": "a ripe yellow banana, peeled halfway down with the peel folded "
            "back in strips around its base"},
    {"id": "berinjela", "selo": "V", "nome": "eggplant",
     "img": "a long slim purple eggplant with its green cap still on, the lower "
            "end squared off flat"},
    {"id": "cenoura", "selo": "V", "nome": "carrot",
     "img": "a thick orange carrot with the greens cut off and the wide end "
            "squared flat"},
    {"id": "pastinaca", "selo": "V", "nome": "parsnip",
     "img": "a large pale parsnip, the thick end trimmed flat"},
]


# ---------------------------------------------------------------------------
# ⭐ REFS — a boticaria
# ---------------------------------------------------------------------------
# ⛔⛔ LEI DO REF — ela e' sempre bonita. Ordem permanente do operador, ja' dada
# em tres agentes (CLEAN, COLO, RESSURREICAO) e reafirmada no ESCANDALO em
# 2026-08-04: *"mulheres sempre super fit e lindas"*.
# ⚠️ DECISAO DECLARADA: a fonte e' uma mulher de ~40 de oculos, e a autoridade
# dela vem de PARECER curandeira. Eu escolhi a lei do operador sobre a fonte — a
# tradicao entra pelo TRAJE do mundo, nao pelo desgaste do rosto. E' uma linha
# para inverter se ele discordar.
# ⛔ Zero oculos, zero grisalho, zero pele castigada. A ancora facial e' SINAL DE
# BELEZA, nunca deterioracao.
# ⛔ Zero adjetivo de etnia nas entradas: quem injeta e' a montagem, a partir do
# MUNDO. Mesmo contrato do COLO, NECROSE e EXTERIOR.
REFS = [
    {"idade": 29, "corpo": "slim and upright, with fine collarbones",
     "cabeca": "copper-red hair pinned back off her face",
     "marca": "a heavy dusting of freckles across her nose and clear skin"},
    {"idade": 34, "corpo": "trim and athletic, with a straight back",
     "cabeca": "long dark hair in a low twist",
     "marca": "high round cheekbones and lightly tanned even skin"},
    {"idade": 26, "corpo": "lean and long-limbed",
     "cabeca": "honey-blonde hair braided over one shoulder",
     "marca": "pale green eyes, a light spray of freckles and a beauty mark above her lip"},
    {"idade": 31, "corpo": "compact and strong, with toned forearms",
     "cabeca": "tight natural curls gathered high",
     "marca": "glowing deep brown skin and a wide bright smile"},
    {"idade": 37, "corpo": "slender, with square shoulders",
     "cabeca": "straight black hair parted in the middle",
     "marca": "full lips, a deep dimple in her left cheek and warm tanned skin"},
    {"idade": 28, "corpo": "toned and broad-shouldered, like a swimmer",
     "cabeca": "long braids gathered at the nape",
     "marca": "a small silver hoop in her left nostril and clear skin"},
    {"idade": 33, "corpo": "slim-hipped and wiry",
     "cabeca": "chestnut hair in a loose knot with strands escaping",
     "marca": "a dusting of freckles and a small crescent birthmark at her right temple"},
    {"idade": 25, "corpo": "petite and tightly muscled",
     "cabeca": "dark hair in a high smooth bun",
     "marca": "eyes of two different colours, one green and one brown"},
    {"idade": 36, "corpo": "tall and lean, with a long neck",
     "cabeca": "auburn hair coiled and pinned at the back",
     "marca": "a fine pale scar through one eyebrow and smooth clear skin"},
    {"idade": 30, "corpo": "firm and athletic, with a narrow waist",
     "cabeca": "black hair in a thick plait down her back",
     "marca": "smoothly tanned skin and a dark beauty spot high on her left cheekbone"},
    {"idade": 27, "corpo": "slim and toned, with a flat stomach",
     "cabeca": "wavy caramel hair tucked behind her ears",
     "marca": "a gap between her front teeth that shows when she smiles"},
    {"idade": 38, "corpo": "strong-shouldered and upright",
     "cabeca": "silver-free dark hair wound into a bun",
     "marca": "arched brows over wide dark eyes and clear skin"},
]


# ---------------------------------------------------------------------------
# ⭐⭐ HOMENS — o espantado MUDO da cena 3
# ---------------------------------------------------------------------------
# ⛔ Ordem do operador: *"no take final, alem do ref falando, havera um homem
# sempre atras, com cara de espanto e surpresa e olhando para o objeto na mao do
# ref"*. E, perguntado se ele fala: *"Mudo"*.
# ⚠️ A etnia dele vem do MUNDO, igual a' dela — congruencia de casal no mesmo
# quadro (mesma regra do COLO).
# ⚠️ Ele existe para encenar o espanto NO LUGAR do espectador, que e' a mecanica
# da plateia congelada do ESCANDALO. Por isso ele olha o COPO, nunca a lente.
HOMENS = [
    {"id": "grisalho_barbudo", "idade": 58,
     "marca": "a heavy-set build, thick silver hair and a short grey beard, "
              "weathered skin and a pale scar through one eyebrow",
     "roupa": "a plain navy work shirt"},
    {"id": "careca_bigode", "idade": 63,
     "marca": "a stocky build, a bald crown with white hair at the sides and a "
              "thick moustache, ruddy skin and a large mole on his cheek",
     "roupa": "a heather-grey pocket tee"},
    {"id": "cabelo_farto", "idade": 46,
     "marca": "a tall lean frame, a full head of dark hair going grey at the "
              "temples, clean-shaven, with a deep cleft in his chin",
     "roupa": "an olive canvas shirt with the sleeves rolled"},
    {"id": "sardas_ruivo", "idade": 41,
     "marca": "a wiry build, coppery hair and heavy freckling across the nose, "
              "with a gap between his front teeth",
     "roupa": "a faded red flannel shirt"},
    {"id": "fade_grisalho", "idade": 55,
     "marca": "a broad-shouldered build, a close grey fade and a neat chinstrap "
              "beard, smooth skin and a small gold stud in one ear",
     "roupa": "a slate-blue polo shirt"},
    {"id": "locs_oculos", "idade": 49,
     "marca": "a solid build, salt-and-pepper locs gathered back, wire-rimmed "
              "glasses and a raised mole beside his right eye",
     "roupa": "a charcoal henley with the sleeves pushed up"},
    {"id": "corte_militar", "idade": 52,
     "marca": "a thickset build, an iron-grey brush cut, sun-weathered skin and "
              "a broad nose broken once",
     "roupa": "a mustard snap-button shirt"},
    {"id": "cavanhaque", "idade": 60,
     "marca": "a barrel-chested build, a shaved head and a neat white goatee, "
              "with a white streak in one eyebrow",
     "roupa": "a cream short-sleeve camp shirt"},
    {"id": "onda_longa", "idade": 44,
     "marca": "a slim build, wavy dark hair worn a little long at the collar, "
              "clean-shaven, with a deep dimple in his left cheek",
     "roupa": "a forest-green work shirt"},
    {"id": "sobrancelha_oculos", "idade": 66,
     "marca": "a gaunt frame, white hair combed back, heavy black-framed "
              "glasses and deeply lined skin",
     "roupa": "a blue-and-white checked shirt"},
    {"id": "queixo_fendido", "idade": 47,
     "marca": "a compact build, sandy hair going grey at the sides, tanned skin "
              "and a strong cleft chin",
     "roupa": "a rust-red pocket tee"},
    {"id": "afro_curto", "idade": 54,
     "marca": "a burly build, a short grey afro and a broad open face, with a "
              "small birthmark high on one cheek",
     "roupa": "a sand-coloured linen shirt"},
]


# ---------------------------------------------------------------------------
# COPY — cena 1: A ISCA + O VILAO
# ---------------------------------------------------------------------------
# ⭐ ESTRUTURA DA FONTE, literal:
#     "Did you know that if you add saffron to banana, this happens?
#      Pharmacies don't want you to know this."
#
# ⛔⛔ §21 APLICADA DESDE O NASCIMENTO: a PRIMEIRA sentenca NOMEIA os dois objetos
# em cena (a substancia e o prop). Nenhuma abertura deste motor deixa o
# espectador perguntando "do que ela esta' falando?". Cobrado pela BO9.
# ⛔⛔⛔ REESCRITO EM 2026-08-04 — A CENA 1 PARA DE FALAR DO VEGETAL.
#
# O operador leu o TAKE 01 renderizado:
#
#     "Nobody told you what crushed cinnamon does to an eggplant, did they?"
#     -> "Erro grave: fala APENAS do vegetal. Deveria dizer: «My husband's
#         John-son was dead for years till I discovered this golden seed of the
#         Mediterranean secret ingredient»"
#
# ⛔ O DEFEITO: o espectador via uma mulher despejando canela numa berinjela e
# ouvia falar sobre UMA BERINJELA. Nao havia homem, nao havia orgao, nao havia
# problema — ele concluia que o video era de culinaria e rolava. O prop e' um
# PROXY do orgao, e sem a copy fazendo a ligacao ele nao e' metafora, e' legume.
#
# ⚠️⚠️ E O QUE ISSO EXPOS SOBRE A MINHA LENTE: eu tinha construido a BO9 para
# exigir que a abertura "nomeasse o referente", e DEFINI referente como o prop e
# a substancia — ou seja, *o que aparece no quadro*. A lente rodou verde e a copy
# estava errada. Medi "a abertura nomeia o que APARECE?" quando a regra e' "a
# abertura nomeia o que esta' EM JOGO?". O que esta' no quadro sao adereços; o
# que esta' em jogo e' o orgao do marido dela. (licoes §22)
#
# ⭐ AS CINCO PARTES, todas obrigatorias, na ordem que o operador ditou:
#     1. QUEM ................ `my husband` / `my man` — pessoalidade
#     2. O ORGAO ............. `{o}`
#     3. O PROBLEMA COM DURACAO  `was dead for years`
#     4. A VIRADA ............ `till I found`
#     5. O RARO COM O APOSTO . enquadrado como SEGREDO, nao como revelacao
#
# ⚠️ O RARO APARECE NAS DUAS CENAS, e o operador autorizou: *"no take um refere-se
# com aposto mecanismo unico secreto (hook-bullet de curiosidade / exclusividade
# / misterio) e NAO revelacao"*. Por isso o APOSTO e' pago AQUI, na cena 1, onde
# ele e' curiosidade; a cena 2 nomeia o raro sem repeti-lo — repetir custaria ~8
# palavras num video de 24 segundos.
#
# ⛔ O PROP GIGANTE CONTINUA NO QUADRO (ordem do operador), agora como metafora
# MUDA: a imagem carrega o proxy, a fala carrega o que esta' em jogo.
ISCAS = [
    "My husband's {o} was dead for years, until I found this secret: {r}.",
    "My husband's {o} had quit on us both, and then I came across {r}.",
    "My man's {o} stopped working at sixty, and what fixed it was {r}.",
    "For three years my husband's {o} gave up on him, until I found {r}.",
    "My husband's {o} had not worked in years, and nobody sells what did it: {r}.",
    "My husband's {o} was gone, and the one thing that brought it back was {r}.",
    "Nobody told me my husband's {o} could come back. This is what did it: {r}.",
    "My husband's {o} quit on him years ago, until I got hold of {r}.",
    "My husband's {o} had been dead a long time, and the secret was {r}.",
    "The doctors had my husband's {o} written off. What nobody sells is {r}.",
]

# ⛔ O VILAO — na fonte e' `Pharmacies don't want you to know this.` O operador
# mandou este beat entrar tambem no RECEITA no mesmo dia; aqui ele e' da fonte.
# ⛔ REGRA DE FUNCAO: toda entrada NOMEIA QUEM esconde ou QUEM lucra. Queixa sem
# dono devolve a culpa para o espectador.
# ⛔⛔ O MODELO DO VILAO TEM TRES PARTES — ordem do operador, 2026-08-04, depois
# de ler "They will sell you a monthly plan before they sell you the truth":
#     *"who will sell what and with what purpose? No lugar deveria ter: the
#      pharmacy industry will sell you pills and not let you know the truth
#      that works"*
#
#     [QUEM] + [o que ele te VENDE] + [o que ele te ESCONDE]
#
# ⛔ PRONOME NAO E' QUEM. `They`, `nobody`, `somebody` nao nomeiam ninguem, e a
# primeira versao deste pool (e da lente que o cobra) aceitava os tres.
VILOES = [
    "The pharmacy industry sells you pills and keeps this off the label.",
    "No drug company makes a cent off a kitchen shelf.",
    "The chemists keep this off the shelf because they cannot bill you for it.",
    "The chemists would rather sell you the box behind the counter.",
    "Doctors do not hand this out, and it is not because it fails.",
    "The drug companies advertise the pill and never this.",
    "The pill companies need you buying the little blue box instead.",
    "My grandmother knew this. Then the drug industry put a price on it.",
    "The pharmacy sells you a monthly refill and hides what costs pennies.",
    "Every pharmacy ad sells the expensive answer and buries the cheap one.",
]


# ---------------------------------------------------------------------------
# COPY — cena 2: O PREPARO (o mecanismo)
# ---------------------------------------------------------------------------
# ⛔⛔ CONGRUENCIA INVIOLAVEL: o mecanismo do criativo e' o que a VSL vende, e a
# nossa vende GELATIN nas paginas. A fonte manda banana + acafrao + mel + limao;
# nos mantemos a FORMA (caseiro, tres ingredientes, um utensilio) e ancoramos no
# `gelatin trick`. O que varia e' o acompanhamento, nunca a ancora.
# ⛔ O literal `gelatin trick` e' obrigatorio nesta cena e o linter trava nele.
#
# ⭐ O SLOT `{r}` E' O INGREDIENTE RARO **COM O APOSTO COLADO** — a montagem
# injeta `nome, aposto`, nunca o nome sozinho (BO8).
# ⚠️ ENCURTADAS EM 2026-08-04 por ARITMETICA, nao por gosto. A cena 2 passou a
# carregar TRES beats — receita + o passo retido + a promessa — e o modelo do
# passo retido e' mais longo que o antigo. Com as receitas anteriores a conta
# dava 42 palavras contra teto de 32. Quem entra por ultimo nao paga a conta
# sozinho: as tres partes encolhem juntas.
RECEITAS = [
    "Into the {v}: gelatin, {c}, and {r}",
    "Gelatin, {c} and {r}, into the {v}",
    "In the {v}: gelatin first, then {c}, then {r}",
    "A spoon of gelatin, {c} and {r}, into the {v}",
    "Gelatin goes in the {v} with {c} and {r}",
    "Gelatin, {c}, {r} — all of it into the {v}",
]

# ⛔ A ANCORA. Toda entrada traz o literal `gelatin trick` E nomeia o orgao — as
# duas coisas que o colapso de 52 segundos para 24 ameacava levar embora.
# ⛔⛔ REESCRITO EM 2026-08-04 — O PASSO RETIDO, NAO A REVELACAO.
#
# Ordem do operador, lendo o TAKE 02 renderizado
# ("Into the metal sieve: gelatin, oats, and tongkat ali. That is the gelatin
#  trick, and your weiner feels it first."):
#
#     *"Tome cuidado ao dizer que X E' o gelatin trick: pode matar a
#      curiosidade."*
#
# ⛔ E ele esta' certo pela mecanica do funil: se a cena 2 mostra a receita
# INTEIRA e ainda bate o martelo dizendo que aquilo E' o mecanismo, o espectador
# ja' tem tudo — e nao ha' motivo para comentar. O CTA vende o que a cena 2
# entregou de graca.
#
# ⭐ A FORMA ESCOLHIDA PELO OPERADOR (opcao `c`): FALTA UM PASSO.
#     "There's one step I'm not showing here. That's the gelatin trick."
# A receita fica visivel e verdadeira; o que falta e' um passo, e o passo tem
# nome. A lacuna e' o que o comentario compra.
# ⚠️ O literal `gelatin trick` continua obrigatorio (congruencia com a VSL) — ele
# e' NOMEADO, so' nao e' ENTREGUE. Nomear nao gasta; entregar gasta.
ANCORAS = [
    "%s. There's one step I'm not showing here. That's the gelatin trick.",
    "%s. One step stays off camera, and that's the gelatin trick.",
    "%s. I left one step out on purpose. That's the gelatin trick.",
    "%s. What I'm not showing you is the gelatin trick.",
    "%s. There's a step missing here, and it's the gelatin trick.",
    "%s. The part I skipped is the gelatin trick.",
    "%s. One thing isn't in that bowl. That's the gelatin trick.",
    "%s. There's a step after this one. That's the gelatin trick.",
]

# ---------------------------------------------------------------------------
# ⭐⭐ PROMESSAS — o terceiro beat da cena 2, no lugar do bullet de loja
# ---------------------------------------------------------------------------
# ⛔ ORDEM DO OPERADOR, 2026-08-04: *"usar bullet de store, loja nao tem funcao
# pratica: melhor seria bullet de promessa"*. O `ONDE` (`You can buy all of it
# at Walmart`) era fiel a' fonte e nao movia ninguem — saiu do pool inteiro.
#
# ⛔⛔ E A RESSALVA DELE E' A REGRA DESTE POOL: *"«you'll be a new person» apenas
# seria vago pq pode ser nova pessoa por qualquer circunstancia — o que seria
# copy drifting"*. Novo POR QUE? Toda entrada nomeia o ORGAO, ou nomeia o que a
# mulher percebe NELE. Promessa sem referente e' a §20 outra vez.
#
# ⚠️ FALA COM O HOMEM, em 2a pessoa. A narradora e' a esposa e ate' aqui ela
# contava do marido dela; neste beat ela vira para a lente e fala com QUEM
# ASSISTE — que e' homem. `Seu marido sera' outro` conversaria com a esposa
# dele, nao com ele.
# ⚠️ VARIACAO ALTA por ordem explicita: *"capriche nas variacoes de pool
# semantica aqui, nao quero videos repetitivos mesmo sorteando"*. Sao 16, em
# quatro familias semanticas — o corpo dele, a reacao dela, a rotina que volta,
# e o homem que ele era.
# ⛔⛔ TODA ENTRADA CARREGA `{o}` — e o linter cobra dos dois lados (BO15).
# A primeira versao tinha cinco sem: `Mornings go back to what they were`
# (que manhas?), `You get back the version of yourself she fell for` (versao em
# que sentido?), `She stops pretending to be asleep` (de que ela desistiu?).
# Sao exatamente a promessa vaga que o operador descreveu — nova pessoa POR
# QUALQUER CIRCUNSTANCIA. A regra e' simples e verificavel: promessa sem orgao
# nao entra.
# ⭐⭐ O CRITERIO DE CURADORIA, e ele vale para QUALQUER pool deste repo.
# Ordem do operador, 2026-08-04: *"«your wife will notice before you do» >>
# «you'll be a new person». Copys que fazem STACK de varios angulos de apelos
# persuasivos sempre vencem na curadoria de candidatos"*. E, na mensagem
# seguinte, o par que ele nomeia: **PROMESSA + DESEJO OCULTO**.
#
# A linha entrega um RESULTADO e, na mesma respiracao, toca o que o espectador
# quer e nao diz em voz alta. `you'll be a new person` so' promete — e promete
# vago, porque novo pode ser por qualquer circunstancia.
#
# ⛔ AUDITADAS UMA A UMA E QUATRO FORAM TROCADAS por entregarem so' a promessa:
#   `Your {o} remembers what it used to do.`        so' resultado
#   `Your {o} answers the first time again.`        so' resultado
#   `Your {o} makes mornings what they used to be.` so' resultado
#   `You'll stop planning your night around...`     so' alivio, sem ela
#
# ⚠️ E EMPILHAR NAO AFROUXA O REFERENTE: toda entrada continua com `{o}`. A forma
# que ganha e' `your wife will notice your {o} before you do` — os dois angulos
# **e** o objeto. Sem o objeto, e' "notara' o que?" (§20).
#
# O desejo oculto deste funil: ela querer de novo · ela tomar a iniciativa · ele
# parar de ser motivo de pena · nao precisar explicar nada.
PROMESSAS = [
    # ela nota — o desejo de ser visto
    "Your wife notices your {o} before you do.",
    "Your wife talks about your {o} before you do.",
    "She'll ask what changed, and your {o} already told her.",
    "Your {o} is up before you are, and she knows it.",
    # ela toma a iniciativa — o desejo de ser querido
    "Your wife reaches over again, and your {o} is why.",
    "Your {o} wakes her up before the alarm does.",
    "Your {o} shows up, and she stops pretending to sleep.",
    "She stops setting the alarm, and your {o} is the reason.",
    # ele volta a ser homem aos olhos dela — o desejo de dignidade
    "You'll be a new man, and your {o} tells her first.",
    "You get the old you back, and she notices your {o} first.",
    "She looks at you like before, and your {o} earned it.",
    "You'll be the man she married, {o} and all.",
    # a vergonha acaba — o desejo de nao precisar explicar
    "You'll stop apologising, and she'll stop pretending your {o} was fine.",
    "Your {o} gets you in trouble, and she is not complaining.",
    "You stop dreading the bedroom, and your {o} is why she smiles.",
    "You'll feel it in your {o} inside a week, and so will she.",
]



# ---------------------------------------------------------------------------
# COPY — cena 3: O COPO + O CTA
# ---------------------------------------------------------------------------
# ⭐ A FONTE: "Drink this every morning to increase blood flow and circulation to
# your wiener naturally. Want to learn another natural trick that could help your
# wiener grow up to 5 inches faster in a week? Comment wiener below and I'll
# personally send it to you. But don't forget to follow me. Otherwise I can't
# find you."
#
# ⛔⛔ O CENTIMETRO SAI. Ordem do operador: *"so' a promessa sem centimetro"*.
# A fonte promete `5 inches faster in a week`; nos ficamos com a promessa. O
# linter varre qualquer medida (BO10).
USOS = [
    "Drink this every morning and it goes straight to your {o}.",
    "One glass every morning, and your {o} is what feels it.",
    "Drink it first thing and your {o} gets the blood it stopped getting.",
    "Every morning on an empty stomach, and your {o} notices before you do.",
    "Drink this daily and your {o} comes back to what it was.",
    "One glass a day, and your {o} stops letting you down.",
    "Take it every morning and your {o} answers again inside a week.",
    "Drink it warm before bed and your {o} is up before you are.",
]

# ⛔⛔ A ESCALADA SAIU DA CENA 3 — decisao MEDIDA, nao estetica.
# Com uso + escalada + keyword + isca + gate a cena batia em 42 palavras contra
# um teto de 31, ou seja 5,3 palavras por segundo: um terco acima do que cabe em
# 8 segundos de narracao. Quatro funcoes nao cabem; tres cabem.
# ⚠️ E a que saiu foi a ESCALADA porque ela e' a unica REDUNDANTE: ela promete
# "tem mais" e a ISCA ja' diz o que chega. Keyword, isca e gate sao lei do repo
# e nao encolhem. Fica registrado para ninguem "reintroduzir a escalada" sem
# saber o que vai sair no lugar.
ISCAS_ENTREGA = [
    "the whole recipe", "the full recipe", "the complete recipe",
    "the exact recipe", "the recipe and the measurements",
    "the recipe and the doses", "the exact measurements",
    "the recipe", "the full routine", "the whole thing written out",
]

GATES = [
    "But you have to follow me, or I cannot reach you.",
    "Follow me first, or I cannot reply to you.",
    "Make sure you are following, or I cannot message you back.",
    "Follow me before you comment, or it never reaches me.",
    "Hit follow first, or my message cannot get to you.",
    "Follow me, or I will not be able to find your comment.",
    "Follow me first, or I cannot reply.",
    "Do not forget to follow, or the app will not let me answer.",
]

# ⛔ As palavras do orgao. Rotacionam DENTRO do video (nunca a mesma duas vezes).
NUCLEO = ["Johnson", "pecker", "wiener", "soldier", "tool"]

# ⚠️ MEDIDOS CONTRA A CAPACIDADE REAL de 8s de narracao (~3,4-4,0 p/s = 27-32
# palavras). ⛔ Teto folgado nao e' seguranca: e' frase morta esperando nascer
# (licoes §5). A cena 2 e' a mais densa por construcao — receita + aposto +
# gelatin trick + orgao.
# ⚠️ RECALIBRADOS EM 2026-08-04, quando o APOSTO mudou de cena. A cena 1 passou a
# carregar quem + orgao + problema + descoberta + o raro com aposto, e a cena 2
# ficou so' com a receita. Medido depois da mudanca: cena 1 subiu para 28-38 e a
# cena 2 caiu para 21-30. Teto e piso seguem o que os pools REALMENTE produzem —
# teto que nenhuma combinacao alcanca e' decorativo, e piso que ninguem atinge
# vira AVISO permanente que se aprende a ignorar (licoes §5).
TETO_FALA = {1: 32, 2: 32, 3: 31}
PISO_FALA = {1: 26, 2: 22, 3: 23}


# ---------------------------------------------------------------------------
# TRAVAS E EIXOS DO PAINEL
# ---------------------------------------------------------------------------
# ⚠️ ⛔ NAO declarar "livre" aqui: a barra do `ui_agente` ja' o prepende. Motor que
# declara ganha o botao DUPLICADO — defeito achado lendo o print do .exe em
# 2026-08-04 e corrigido na UI, mas nao ha' motivo para recria-lo no dado.
TRAVAS_UI = [
    ("familia_mundo", "nicho", FAMILIAS_MUNDO),
]

EIXOS_TRAVAVEIS = ["mundo", "etnia", "ref", "homem", "prop", "substancia",
                   "metodo", "comum", "raro", "cor"]


def etnias_do_mundo(spec):
    """O pool de ETNIA depende do MUNDO em cena — trocar para uma etnia que
    aquele mundo nao comporta e' exatamente a incongruencia que os MUNDOS
    existem para impedir."""
    return list(spec["mundo"]["etnias"])


etnias_do_mundo.recebe_spec = True

EIXOS_UI = [
    ("mundo", "A BOTICA", "MUNDOS", "id"),
    ("etnia", "ETNIA", "etnias_do_mundo", None),
    ("ref", "A BOTICARIA", "REFS", "cabeca"),
    ("homem", "O ESPANTADO", "HOMENS", "marca"),
    ("prop", "O PROP", "PROPS", "nome"),
    ("substancia", "A ISCA", "SUBSTANCIAS", "nome"),
    ("metodo", "O PREPARO", "METODOS", "id"),
    ("comum", "O COMUM", "COMUNS", "nome"),
    ("raro", "O RARO", "RAROS", "nome"),
]

CENAS_UI = ["1 · a isca + o vilao", "2 · o preparo", "3 · o copo + CTA"]


# ---------------------------------------------------------------------------
# MAQUINARIA
# ---------------------------------------------------------------------------

def _palavras(s):
    return len(re.sub(r"\{\w+\}", "x", s or "").split())


def _carregar_ledger():
    try:
        with open(LEDGER, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


def _gravar_ledger(led):
    try:
        with open(LEDGER, "w", encoding="utf-8") as f:
            json.dump(led, f, ensure_ascii=False, indent=1)
    except OSError:
        pass


def _fresco(pool, usados, rng, chave):
    livres = [x for x in pool if str(x.get(chave, x)) not in usados] or pool
    return rng.choice(livres)


def _por_id(pool, valor, chave="id"):
    if isinstance(valor, str):
        return next((x for x in pool if x.get(chave) == valor), pool[0])
    return valor


def _artigo(s):
    return "an" if s[:1].lower() in "aeiou" else "a"


def _traje(spec):
    """A roupa do mundo com o artigo certo. ⛔ O artigo NAO mora no template:
    cores como `off-white`, `indigo` e `olive` sairiam `a off-white` — bug pago
    no CLEAN v2 e achado LENDO o render, nao pelo linter."""
    cor = spec["cor"]
    return "%s %s" % (_artigo(cor), spec["mundo"]["traje"] % cor)


def _sem_artigo(s):
    for art in ("a ", "an ", "the "):
        if s.startswith(art):
            return s[len(art):]
    return s


def _cap(s):
    return s[0].upper() + s[1:] if s else s


def _cabem(pool, monta, teto):
    """As entradas que cabem no teto. ⛔ DESCARTA-SE A LINHA, NUNCA SE ENCURTA
    (CL15): as linhas foram aprovadas uma a uma, e reescrever menor para caber e'
    trocar copy validada por copy nova sem validacao."""
    return [x for x in pool if _palavras(monta(x)) <= teto] or pool


def _na_faixa(pool, monta, piso, teto):
    """As entradas que caem DENTRO da faixa — piso E teto, nao so' o teto.

    ⛔ O `_cabem` sozinho so' impede a fala de ESTOURAR. Medido neste motor:
    26,7% das cenas 1 saiam ABAIXO do piso, a mais curta com 14 palavras em 8
    segundos — 1,75 palavra por segundo, ou seja metade do take em silencio.
    Teto sem piso troca "fala atropelada" por "ar morto", que e' o mesmo defeito
    do outro lado (licoes §5).
    ⚠️ Degrada em dois passos em vez de estourar: tenta a faixa inteira, depois
    so' o teto, e por fim o pool cru — assim quem aparece e' o LINTER, nunca um
    IndexError.
    """
    dentro = [x for x in pool if piso <= _palavras(monta(x)) <= teto]
    return dentro or _cabem(pool, monta, teto)


def _com_o(pool):
    return [x for x in pool if "{o}" in x]


def raro_falado(raro):
    """⭐ BO8 — o ingrediente raro NUNCA sai sozinho na fala.

    `[NOME POPULAR] + [APOSTO]`, que e' a diretiva inteira do operador em uma
    funcao. ⛔ O `interno` (o binomio cientifico) existe so' para producao e nao
    pode chegar ao prompt: `Lepidium meyenii` na boca quebra o tom UGC na hora.
    """
    return "%s, %s" % (raro["nome"], raro["aposto"])


def _falas(spec, rng, quais=(0, 1, 2)):
    """Monta as falas pedidas a partir dos pools ja' sorteados no spec.

    ⚠️ Uma funcao so' para as tres cenas: o botao `trocar` da UI re-sorteia UMA
    fala, e duas copias desta conta garantem que uma delas envelhece mentindo.

    ⭐ A COTA DO ORGAO E' GARANTIDA NO SORTEIO, nao so' cobrada no linter: a cena
    2 sempre o nomeia (todas as ANCORAS trazem `{o}`) e a cena 3 tambem (todos os
    USOS trazem). Linter que reprova o proprio motor e' aviso, nao defesa.
    """
    o1, o2 = spec["orgaos"]
    f = dict(spec.get("falas_map", {}))

    if 0 in quais:
        # ⭐ O APOSTO E' PAGO AQUI, na cena 1, onde ele e' HOOK DE CURIOSIDADE.
        # ⛔ O prop e a substancia SAIRAM da fala (2026-08-04): a cena 1 falava
        # do vegetal e o espectador achava que era culinaria. Eles continuam no
        # QUADRO como metafora muda — a imagem carrega o proxy, a fala carrega o
        # que esta' em jogo, que e' o orgao do marido dela.
        iscas_slots = dict(o=o1, r=raro_falado(spec["raro"]))
        curto_v = min(VILOES, key=_palavras)
        isca = rng.choice(_cabem(
            ISCAS,
            lambda i: i.format(**iscas_slots) + " " + curto_v,
            TETO_FALA[1])).format(**iscas_slots)
        vil = rng.choice(_na_faixa(VILOES, lambda v: isca + " " + v,
                                   PISO_FALA[1], TETO_FALA[1]))
        f[0] = "%s %s" % (isca, vil)

    if 1 in quais:
        met, com, raro = spec["metodo"], spec["comum"], spec["raro"]
        # ⚠️ SEM o aposto aqui: ele ja' foi pago na cena 1. Repetir os 5-9
        # palavras do aposto num video de 24 segundos e' pagar duas vezes pela
        # mesma informacao — e a cena 2 e' a mais densa das tres.
        rec_slots = dict(v=met["vaso_fala"], c=com["nome"], r=raro["nome"])
        # ⚠️ O ESPACO DA PROMESSA E' RESERVADO NA CONTA DESDE O PRIMEIRO SORTEIO.
        # Sem isso a receita e a ancora sao escolhidas contra o teto cheio, a
        # promessa entra por cima e a cena estoura — foi o que aconteceu quando
        # o terceiro beat entrou: 34 a 40 palavras contra teto de 32. Quem
        # escolhe primeiro tem de saber o que ainda vem depois.
        curto_a = min(ANCORAS, key=lambda a: _palavras(a % ""))
        curto_p = min(PROMESSAS, key=_palavras)
        rec = rng.choice(_cabem(
            RECEITAS,
            lambda x: (curto_a % x.format(**rec_slots)).format(o=o2)
            + " " + curto_p.format(o=o2),
            TETO_FALA[2])).format(**rec_slots)
        anc = rng.choice(_cabem(
            ANCORAS,
            lambda a: (a % rec).format(o=o2) + " " + curto_p.format(o=o2),
            TETO_FALA[2]))
        meio = (anc % rec).format(o=o2)
        # ⭐ A PROMESSA fecha a cena 2, no lugar do bullet de loja. Ela fala com
        # o HOMEM que assiste, em 2a pessoa, e nomeia o orgao ou o que ela nota
        # nele — promessa sem referente e' "novo por que?".
        prom = rng.choice(_na_faixa(
            PROMESSAS, lambda x: meio + " " + x.format(o=o2),
            PISO_FALA[2], TETO_FALA[2]))
        f[1] = "%s %s" % (meio, prom.format(o=o2))

    if 2 in quais:
        isca_e = rng.choice(ISCAS_ENTREGA)
        curto_g = min(GATES, key=_palavras)

        def _c3(uso, gate):
            return "%s %s and I'll send you %s. %s" % (
                uso.format(o=o1), sc.CTA_LITERAL, isca_e, gate)

        uso = rng.choice(_cabem(USOS, lambda u: _c3(u, curto_g), TETO_FALA[3]))
        gate = rng.choice(_cabem(GATES, lambda g: _c3(uso, g), TETO_FALA[3]))
        f[2] = _c3(uso, gate)

    return f


def sortear(pagina, rng, led, travas=None):
    """Monta a spec. `travas` fixa eixos (pre-selecao do painel e cadeado)."""
    travas = travas or {}
    usados = led.get(pagina, {})

    fam_trava = travas.get("familia_mundo")
    if travas.get("mundo"):
        mundo = _por_id(MUNDOS, travas["mundo"])
    else:
        if fam_trava and fam_trava != "livre":
            fam = fam_trava
        else:
            fam = _fresco([{"id": x} for x in FAMILIAS_MUNDO],
                          usados.get("familia_mundo", []), rng, "id")["id"]
        mundo = rng.choice([m for m in MUNDOS if m["familia"] == fam])

    et = travas.get("etnia") or rng.choice(mundo["etnias"])
    cor = travas.get("cor") or rng.choice(mundo["cores"])
    ref = (_por_id(REFS, travas["ref"], "cabeca") if travas.get("ref")
           else rng.choice(REFS))
    homem = (_por_id(HOMENS, travas["homem"]) if travas.get("homem")
             else _fresco(HOMENS, usados.get("homem", []), rng, "id"))
    prop = (_por_id(PROPS, travas["prop"]) if travas.get("prop")
            else _fresco(PROPS, usados.get("prop", []), rng, "id"))
    sub = (_por_id(SUBSTANCIAS, travas["substancia"])
           if travas.get("substancia")
           else _fresco(SUBSTANCIAS, usados.get("substancia", []), rng, "id"))
    met = (_por_id(METODOS, travas["metodo"]) if travas.get("metodo")
           else _fresco(METODOS, usados.get("metodo", []), rng, "id"))
    com = (_por_id(COMUNS, travas["comum"]) if travas.get("comum")
           else _fresco(COMUNS, usados.get("comum", []), rng, "id"))
    # ⭐ UM raro por video, sorteado entre os nove (ordem do operador)
    raro = (_por_id(RAROS, travas["raro"]) if travas.get("raro")
            else _fresco(RAROS, usados.get("raro", []), rng, "id"))

    # ⛔ Dois orgaos DIFERENTES no mesmo video: repetir o substantivo em 24
    # segundos vira bordao.
    orgaos = rng.sample(NUCLEO, 2)

    spec = {"pagina": pagina, "mundo": mundo, "etnia": et, "cor": cor,
            "ref": ref, "homem": homem, "prop": prop, "substancia": sub,
            "metodo": dict(met, vaso_fala=_sem_artigo(met["curto"])),
            "comum": com, "raro": raro, "orgaos": orgaos,
            # ⭐ 50/50, ordem do operador 2026-08-04
            "bandeira": rng.random() < 0.5}
    spec["falas"] = [v for _, v in sorted(_falas(spec, rng).items())]
    return spec


def _pessoa(spec):
    r = spec["ref"]
    return ("a %d-year-old %s woman, %s, %s, %s, wearing %s"
            % (r["idade"], spec["etnia"], r["corpo"], r["cabeca"], r["marca"],
               _traje(spec)))


def _ancora(spec):
    """⛔ BO7 — rosto E idade, nunca so' roupa."""
    r = spec["ref"]
    return BO_ANCORA % (r["idade"], spec["etnia"], _sem_artigo(r["cabeca"]),
                        _sem_artigo(r["marca"]), spec["mundo"]["curto"])


# ⭐ A BANDEIRA, 50/50 — ordem do operador. Ela nao mora nas strings de cenario
# deste motor (aprendemos no ESCANDALO que isso a torna obrigatoria por
# construcao): entra como clausula propria, e some inteira quando o sorteio diz.
BANDEIRA = " A US flag hangs on the wall behind her."


def montar(spec):
    """Os 7 blocos. Formatacao NOMEADA de ponta a ponta — sao 15+ campos por
    bloco, e um deslocamento de indice posicional troca pronome por cor sem
    estourar erro nenhum (bug que so' aparece no video pronto)."""
    m, ref, met = spec["mundo"], spec["ref"], spec["metodo"]
    com, raro, hom = spec["comum"], spec["raro"], spec["homem"]
    prop, sub = spec["prop"], spec["substancia"]
    band = BANDEIRA if spec.get("bandeira") else ""

    v = {
        "coz": m["coz"], "coz_c": m["coz_c"],
        "sup_a": m["sup_a"], "sup": m["sup"],
        "luz": m["luz"], "luz_c": m["luz_c"],
        "etnia": spec["etnia"], "idade": ref["idade"],
        "pessoa": _pessoa(spec), "ancora": _ancora(spec),
        "Ancora": _cap(_ancora(spec)),
        "vaso": met["vaso"], "vaso_curto": met["curto"], "acao": met["acao"],
        "comum_img": com["img"], "raro_img": raro["img"],
        "copo": BO_COPO, "anti": ANTICELEB, "cauda": CAUDA, "band": band,
    }
    v["nao_toca"] = BO_NAO_TOCA % m["sup"]

    b = {}
    b["BLOCO 0 (REF)"] = (
        "REF 01: Photo of a real person, a %(idade)d-year-old %(etnia)s woman, "
        "chest up, facing the camera directly, neutral steady expression with "
        "her mouth closed. %(pessoa_curta)s An ordinary everyday relatable "
        "person with a plain unremarkable face, not a celebrity, not a model, "
        "not an actor, not resembling any famous person. Hands out of frame, "
        "no objects. Plain neutral gray background, soft even frontal light. "
        "Slight sensor grain, soft focus, raw iPhone front camera aesthetic. "
        "No subtitles, no captions, no burned-in text, no watermark."
        % dict(v, pessoa_curta="%s. %s. Wearing %s."
               % (_cap(ref["cabeca"]), _cap(ref["marca"]), _traje(spec))))

    # --- CENA 1 — A ISCA NA LENTE + O VILAO ---------------------------------
    # ⛔ O despejo JA' ESTA' acontecendo no frame 0: nao ha' frame de "antes".
    # Mesma economia do EXTERIOR e do TROCA — 8 segundos nao pagam preparacao.
    b["IMAGE 01/03"] = (
        "Medium shot in %(coz)s.%(band)s %(isca)s She is the only person in the "
        "frame. %(anti)s %(luz)s %(cauda)s"
        % dict(v, isca=BO_ISCA % (prop["img"], sub["dish"], sub["queda"])))

    # --- CENA 2 — O PREPARO (o mecanismo) -----------------------------------
    # ⚠️ O utensilio VARIA (ordem do operador) e o verbo do TAKE acompanha.
    b["IMAGE 02/03"] = (
        "%(preparo)s %(anti)s %(luz)s %(cauda)s"
        % dict(v, preparo=BO_PREPARO % v))

    # --- CENA 3 — O COPO + O HOMEM MUDO + O CTA -----------------------------
    # ⭐ O objeto da keyword esta' NA MAO no frame em que a boca diz `gelatin,`.
    # ⛔ BO5 — o copo so' existe aqui. BO6 — o homem e' mudo e olha o copo.
    b["IMAGE 03/03"] = (
        "Closer medium shot in the same place, same background, same %(luz_c)s, "
        "filmed straight on and framed from the waist up. %(Ancora)s, standing "
        "centred in the frame, holding %(copo)s up at chest height, turned "
        "towards the lens. She looks directly into the camera, calm and "
        "certain, her mouth open mid-word as she speaks, her front teeth even "
        "and complete. %(homem)s %(anti)s %(cauda)s"
        % dict(v, homem=BO_HOMEM % (hom["idade"], spec["etnia"], hom["marca"],
                                    hom["roupa"])))

    # ⛔⛔ O TAKE ANIMA A IMAGE — ELE NAO INVENTA OUTRO GESTO. Contradicao entre
    # IMAGE e TAKE e' pior que omissao: a omissao o gerador preenche com o frame;
    # a contradicao ele resolve mexendo no que estava certo.
    mov = [
        BO_ISCA_ESTAVEL + " She never lowers either hand and never sets "
        "anything down.",
        ("She keeps her right hand closed around %(vaso_curto)s, her forearm "
         "resting steady on the %(sup)s, and %(acao)s. Her left hand stays flat "
         "on the %(sup)s beside it. %(nao_toca)s" % v),
        ("She holds the glass steady at chest height the whole time and never "
         "sets it down."),
    ]
    elenco = [
        "She is the only person in the shot.",
        "She is the only person in the shot.",
        BO_HOMEM_TAKE,
    ]
    audio = ["%s. No music." % m["audio"],
             # ⚠️ SEM `the` aqui: o campo `curto` dos METODOS JA' traz o artigo
             # (`the metal sieve`). A versao anterior saia "the sound of the the
             # metal sieve" — achado LENDO o TAKE renderizado, nao no fonte, e
             # invisivel em qualquer linter de conteudo.
             "%s, the sound of %s. No music." % (m["audio"], met["curto"]),
             "%s. No music." % m["audio"]]

    for i in range(3):
        b["TAKE %02d/03" % (i + 1)] = (
            "Animate the provided image exactly. Handheld iPhone shot, very "
            "slight natural sway, no cuts. %s %s\n"
            'Dialogue: "%s"\nAudio: %s'
            % (mov[i], elenco[i], sonorizar(spec["falas"][i]), audio[i]))

    return sc.selar_takes(sc.selar_tags(b))


# ---------------------------------------------------------------------------
# LINTER
# ---------------------------------------------------------------------------

def _sentencas(fala):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", fala or "") if s.strip()]


# ⛔ BO10 — ZERO MEDIDA DE CRESCIMENTO. A fonte promete "5 inches faster in a
# week"; ordem do operador: *"so' a promessa sem centimetro"*.
MEDIDA = re.compile(r"\b\d+\s*(inch|inches|cm|centimet\w*)\b"
                    r"|\b(an|one|two|three|four|five)\s+(inch|inches)\b", re.I)

# ⛔ BO11 — nome cientifico NUNCA na fala.
CIENTIFICO = re.compile(
    r"\b(lepidium|eurycoma|tribulus terrestris|epimedium\s+\w+|trigonella|"
    r"ptychopetalum|ginkgo biloba|mucuna pruriens|smilax)\b", re.I)


def lint(spec, blocos):
    ach = []
    falas = spec["falas"]
    m = spec["mundo"]

    sc.lint_tags(blocos, ach)
    sc.lint_sem_texto(blocos, ach)
    sc.lint_isca_cta(falas[2], ach, "a cena 3 (CTA)")
    sc.lint_cta_literal(falas[2], ach, "a cena 3 (CTA)")
    sc.lint_bandeira(spec, blocos, ach, rotulo="BO12")

    if not blocos.get("BLOCO 0 (REF)", "").lstrip().upper().startswith("REF"):
        ach.append(("ERRO", "BLOCO 0 sem o cabecalho REF — o AdBatch descarta a "
                            "referencia em silencio"))

    # --- tetos e pisos ------------------------------------------------------
    for i, f in enumerate(falas, 1):
        n = _palavras(f)
        if n > TETO_FALA[i]:
            ach.append(("ERRO", "BO13: cena %d com %d palavras (teto %d) — a "
                                "narracao passa de 7s" % (i, n, TETO_FALA[i])))
        if n < PISO_FALA[i]:
            ach.append(("AVISO", "BO13: cena %d com %d palavras (piso %d) — "
                                 "sobra silencio nos 8s" % (i, n, PISO_FALA[i])))

    # --- BO9: ⭐⭐ A ABERTURA DE CADA CENA TEM REFERENTE (licoes §21) ---------
    # ⛔ Este agente NASCE com a regra aplicada, e e' o primeiro. A primeira
    # sentenca e' a que o espectador ouve antes de qualquer outra, sozinha, no
    # scroll — e era a unica que nenhuma lente minha olhava.
    # ⛔⛔ A DEFINICAO DE `referente` MUDOU EM 2026-08-04, E ESSE FOI O DEFEITO.
    # A versao anterior aceitava, na cena 1, o PROP e a SUBSTANCIA — ou seja, o
    # que aparece no quadro. A lente rodava verde e a copy falava do vegetal.
    # O que esta' em quadro sao adereços; o que esta' EM JOGO e' o orgao do
    # marido dela. A cena 1 agora exige ORGAO **e** o homem.
    alvos = [(2, ["gelatin"] + [o.lower() for o in NUCLEO]),
             (3, [o.lower() for o in NUCLEO])]
    for i, termos in alvos:
        sents = _sentencas(falas[i - 1])
        if not sents:
            continue
        baixo = sents[0].lower()
        if not any(t.lower() in baixo for t in termos):
            ach.append(("ERRO", "BO9: a abertura da cena %d nao nomeia o "
                                "referente — %r deixa o espectador perguntando "
                                "'do que ela esta' falando?' no segundo em que "
                                "ele decide se fica (licoes §21)"
                        % (i, sents[0])))
    sents1 = _sentencas(falas[0])
    if sents1:
        a1 = sents1[0].lower()
        if not any(o.lower() in a1 for o in NUCLEO):
            ach.append(("ERRO", "BO9: a abertura da cena 1 nao nomeia o ORGAO — "
                                "%r fala do adereço e nao do que esta' em jogo, "
                                "e o espectador acha que e' culinaria"
                        % sents1[0]))
        if not re.search(r"\b(my husband|my man)\b", a1):
            ach.append(("ERRO", "BO9: a abertura da cena 1 nao diz DE QUEM e' o "
                                "problema — sem `my husband` nao ha' pessoa, e "
                                "sem pessoa nao ha' historia (%r)" % sents1[0]))

    # --- BO8: ⭐⭐ O RARO E O APOSTO, e o aposto mora na CENA 1 --------------
    # ⚠️ Ordem do operador: o raro aparece nas DUAS cenas — na 1 como "mecanismo
    # unico secreto" (curiosidade), na 2 como receita. O APOSTO e' pago na 1;
    # repeti-lo na 2 custaria 5-9 palavras no take mais denso dos tres.
    raro = spec["raro"]
    if raro["nome"] not in falas[0]:
        ach.append(("ERRO", "BO8: a cena 1 nao nomeia o ingrediente raro (%s) — "
                            "e' ele o segredo que segura o espectador"
                    % raro["nome"]))
    elif raro["aposto"] not in falas[0]:
        ach.append(("ERRO", "BO8: `%s` entrou SEM o aposto na cena 1 — nome solto "
                            "e' um termo aleatorio jogado no roteiro, e o "
                            "espectador nao faz ideia do que e'" % raro["nome"]))
    if raro["nome"] not in falas[1]:
        ach.append(("ERRO", "BO8: a cena 2 nao nomeia o ingrediente raro (%s) na "
                            "receita" % raro["nome"]))
    for r in RAROS:
        if not 3 <= len(r["aposto"].split()) <= 12:
            ach.append(("ERRO", "BO8: aposto de %r com %d palavras (regra de "
                                "economia: 3-10, teto duro 12)"
                        % (r["nome"], len(r["aposto"].split()))))

    # --- BO15: ⭐ a PROMESSA nomeia o orgao, e o mecanismo nao e' ENTREGUE ---
    # ⛔ Ordem do operador, 2026-08-04, duas partes:
    #   1. *"tome cuidado ao dizer que X E' o gelatin trick: pode matar a
    #      curiosidade"* -> a cena 2 declara um passo RETIDO, nunca equipara a
    #      receita visivel ao mecanismo.
    #   2. *"«you'll be a new person» apenas seria vago pq pode ser nova pessoa
    #      por qualquer circunstancia"* -> promessa sem orgao e' promessa de
    #      nada.
    # ⭐⭐ O STACK E' COBRADO, NAO CONFIADO. Criterio de curadoria do operador:
    # a linha vence quando empilha PROMESSA + DESEJO OCULTO, e o desejo oculto
    # deste funil mora na REACAO DELA. A involuntariedade e' a alavanca de
    # credibilidade: `my {o} is harder` e' alegacao, `she noticed before I did`
    # e' evidencia — por isso toda promessa tem de ter ELA em cena, nao so' o
    # resultado.
    for linha in PROMESSAS:
        if "{o}" not in linha:
            ach.append(("ERRO", "BO15: promessa sem `{o}` — %r e' 'novo por "
                                "que?'" % linha))
        if not re.search(r"\b(she|her|wife)\b", linha, re.I):
            ach.append(("ERRO", "BO15: promessa sem o DESEJO OCULTO — %r entrega "
                                "so' o resultado. Sem a reacao dela e' alegacao "
                                "do proprio homem, e alegacao nao prova nada"
                        % linha))
    ultima = _sentencas(falas[1])[-1] if _sentencas(falas[1]) else ""
    if not any(o.lower() in ultima.lower() for o in NUCLEO):
        ach.append(("ERRO", "BO15: a promessa que fecha a cena 2 nao nomeia o "
                            "orgao — %r promete mudanca sem dizer em que"
                    % ultima))
    # ⛔ E o mecanismo NAO pode ser entregue como equivalente da receita: se a
    # cena 2 diz "that is the gelatin trick" logo depois de listar tudo, o
    # espectador ja' tem o produto e nao tem por que comentar.
    if re.search(r"(that|this) is the gelatin trick[^.]*\band\b", falas[1], re.I):
        ach.append(("ERRO", "BO15: a cena 2 equipara a receita visivel ao "
                            "mecanismo e emenda o beneficio — isso entrega o "
                            "produto de graca e mata a curiosidade que o CTA "
                            "existe para cobrar"))

    # --- BO11: zero nome cientifico na fala ---------------------------------
    corpo = " ".join(falas)
    hit = CIENTIFICO.search(corpo)
    if hit:
        ach.append(("ERRO", "BO11: nome cientifico na fala (%r) — o binomio vive "
                            "no campo `interno`, nunca na boca do personagem"
                    % hit.group(0)))

    # --- BO10: zero medida de crescimento -----------------------------------
    hit = MEDIDA.search(corpo)
    if hit:
        ach.append(("ERRO", "BO10: medida de crescimento na fala (%r) — ordem do "
                            "operador: so' a promessa, sem centimetro"
                    % hit.group(0)))

    # --- BO3: o vilao na cena 1, e ele nomeia QUEM ---------------------------
    sents1 = _sentencas(falas[0])
    if len(sents1) < 2:
        ach.append(("ERRO", "BO3: a cena 1 tem uma sentenca so' — a isca tem de "
                            "vir seguida do vilao"))
    else:
        vil = " ".join(sents1[1:])
        # ⛔ PRONOME NAO E' AGENTE. A primeira versao desta lente aceitava
        # `nobody`, `somebody`, `they` e `them` — e o operador reprovou
        # exatamente uma frase com `they`. A lente carregava o vicio que
        # existia para pegar.
        if not re.search(r"\b(pharmac\w+|chemist\w*|drug compan\w+|"
                         r"drug industry|pill compan\w+|doctors?|clinic)\b",
                         vil, re.I):
            ach.append(("ERRO", "BO3: o vilao da cena 1 nao nomeia quem esconde "
                                "nem quem lucra — %r e' queixa, nao vilao" % vil))

    # --- BO4: o mecanismo ----------------------------------------------------
    if "gelatin trick" not in " ".join(falas).lower():
        ach.append(("ERRO", "BO4: literal `gelatin trick` ausente — sem ele o "
                            "criativo deixa de ser congruente com a VSL"))
    if "gelatin trick" not in falas[1].lower():
        ach.append(("ERRO", "BO4: o `gelatin trick` tem de estar na CENA 2, que "
                            "e' a cena do mecanismo"))

    # --- cota do orgao -------------------------------------------------------
    cota = [i for i, f in enumerate(falas, 1)
            if any(o.lower() in f.lower() for o in NUCLEO)]
    if len(cota) < 2:
        ach.append(("ERRO", "BO14: cota do orgao %d/3 (minimo 2) — cenas sem "
                            "substantivo do nucleo: %s"
                    % (len(cota), [i for i in (1, 2, 3) if i not in cota])))
    if len(set(spec["orgaos"])) < 2:
        ach.append(("ERRO", "BO14: o mesmo orgao repetido no mesmo video"))

    i1, i3 = blocos["IMAGE 01/03"], blocos["IMAGE 03/03"]

    # --- BO1: a isca na lente ------------------------------------------------
    if "fills the left half of the frame" not in i1:
        ach.append(("ERRO", "BO1: IMAGE 01/03 sem a escala por ENQUADRAMENTO — "
                            "sem ela o prop vira um objeto qualquer na mao"))
    if spec["prop"]["img"] not in i1:
        ach.append(("ERRO", "BO1: IMAGE 01/03 sem o prop sorteado"))

    # --- BO5: o copo so' na cena 3 -------------------------------------------
    for nome in ("IMAGE 01/03", "IMAGE 02/03"):
        if BO_COPO in blocos[nome]:
            ach.append(("ERRO", "BO5: o copo pronto fora da cena 3 (%s) — "
                                "entrega o payoff antes da promessa" % nome))
    if BO_COPO not in i3:
        ach.append(("ERRO", "BO5: a cena 3 tem de mostrar o copo na mao — e' o "
                            "objeto da keyword"))

    # --- BO6: ⭐ o homem e' MUDO e olha o COPO -------------------------------
    if "never at the camera" not in i3:
        ach.append(("ERRO", "BO6: o homem da cena 3 nao esta' travado olhando o "
                            "copo — se ele olha a lente, disputa o quadro com "
                            "ela em vez de encenar o espanto"))
    if "never speaks" not in blocos["TAKE 03/03"]:
        ach.append(("ERRO", "BO6: TAKE 03/03 sem a trava de mudez — sem ela o "
                            "segundo corpo dubla a fala dela (falha que derrubou "
                            "a cena do casal do VAZAMENTO)"))
    for nome in ("IMAGE 01/03", "IMAGE 02/03"):
        if "only person" not in blocos[nome]:
            ach.append(("ERRO", "BO6: %s sem a trava de pessoa unica — o homem "
                                "so' existe na cena 3" % nome))
    if "only person" in i3:
        ach.append(("ERRO", "BO6: a cena 3 declara pessoa UNICA e tem DUAS — "
                            "ordem contraditoria: o Veo resolve apagando o "
                            "homem, que e' o espanto do espectador"))

    # --- BO7: a ancora de continuidade nas cenas 2 e 3 ----------------------
    for nome in ("IMAGE 02/03", "IMAGE 03/03"):
        if ("the same %d-year-old" % spec["ref"]["idade"]
                not in blocos[nome].lower()):
            ach.append(("ERRO", "BO7: %s sem a ancora `the same N-year-old` — e' "
                                "onde o Veo troca de pessoa entre blocos" % nome))

    # --- BO2: nada cresce ----------------------------------------------------
    sc.lint_nada_cresce(blocos, ach, rotulo="BO2")

    # --- P12: zero marca legivel NA IMAGEM ----------------------------------
    # ⚠️ As marcas DITAS (Walmart/Costco) sao permitidas por ordem do operador —
    # a varredura e' so' sobre a direcao de cena, nunca sobre a fala.
    for nome, txt in blocos.items():
        if nome.startswith("BLOCO"):
            continue
        direcao = txt.split("\nDialogue:")[0]
        for marca in ("walmart", "costco", "arm & hammer", "printed label",
                      "logo", "brand name"):
            if marca in direcao.lower():
                ach.append(("ERRO", "P12: %s traz marca/rotulo legivel na IMAGEM "
                                    "(%r) — na fala e' permitido, em cena nao"
                            % (nome, marca)))

    # --- a superficie do mundo e' a unica em cena ---------------------------
    # ⚠️ SO' A DIRECAO DE CENA. A fala nunca entra na varredura de token: um
    # VILAO diz "the box behind the counter", que e' ingles correto e nao tem
    # nada a ver com a superficie do mundo. Copiei esta regra do COLO e perdi o
    # escopo — a lente acusou 70 de 600 sorteios que estavam certos (§16).
    junto = " ".join(t.split(chr(10) + "Dialogue:")[0]
                     for k, t in blocos.items() if not k.startswith("BLOCO"))
    if m["sup"] != "counter" and re.search(r"\bcounter\b", junto):
        ach.append(("ERRO", "`counter` sobrou num mundo de %s (%s) — literal "
                            "esquecido no refactor" % (m["sup"], m["id"])))
    if re.search(r"\ba [aeiou]", junto):
        ach.append(("ERRO", "artigo errado: %r"
                    % re.search(r"\ba [aeiou]\w+", junto).group()))
    if re.findall(r"\{\w+\}", junto):
        ach.append(("ERRO", "placeholder cru no prompt: %s"
                    % re.findall(r"\{\w+\}", junto)[:3]))

    return ach


def prop_n(spec):
    return spec["prop"]["nome"]


# ---------------------------------------------------------------------------
# UI
# ---------------------------------------------------------------------------

def resumo_pt(spec):
    m = spec["mundo"]
    return ("Mulher %s de %d anos, em %s (%s). Cena 1: despeja %s sobre %s "
            "esticado na lente + o vilao. Cena 2: %s com %s e %s. Cena 3: o "
            "copo na mao, com um homem de %d anos mudo e espantado atras.%s"
            % (spec["etnia"], spec["ref"]["idade"], m["id"].replace("_", " "),
               m["familia"], spec["substancia"]["nome"], spec["prop"]["nome"],
               spec["metodo"]["id"].replace("_", " "), spec["comum"]["nome"],
               spec["raro"]["nome"], spec["homem"]["idade"],
               " Com bandeira." if spec.get("bandeira") else " Sem bandeira."))


def nova_fala(spec, i, rng):
    spec["falas_map"] = {j: f for j, f in enumerate(spec["falas"])}
    return _falas(spec, rng, quais=(i,))[i]


def _apos_mundo(spec, rng):
    """Trocou o MUNDO: etnia e cor tem de vir do mundo novo, senao o botao
    `trocar` deixa em cena a incongruencia que os MUNDOS existem para impedir."""
    if spec["etnia"] not in spec["mundo"]["etnias"]:
        spec["etnia"] = rng.choice(spec["mundo"]["etnias"])
    if spec["cor"] not in spec["mundo"]["cores"]:
        spec["cor"] = rng.choice(spec["mundo"]["cores"])


def _apos_cena1(spec, rng):
    """Trocou o PROP ou a SUBSTANCIA: a cena 1 os NOMEIA (BO9), entao a fala tem
    de ser remontada — senao a boca fala de um objeto que nao esta' em cena."""
    spec["falas"][0] = nova_fala(spec, 0, rng)


def _apos_cena2(spec, rng):
    """Trocou o METODO, o COMUM ou o RARO: os tres estao NA FALA da cena 2."""
    if "vaso_fala" not in spec["metodo"]:
        spec["metodo"] = dict(spec["metodo"],
                              vaso_fala=_sem_artigo(spec["metodo"]["curto"]))
    spec["falas"][1] = nova_fala(spec, 1, rng)


EIXOS_QUE_MEXEM_NA_COPY = {
    "mundo": _apos_mundo,
    "prop": _apos_cena1,
    "substancia": _apos_cena1,
    "metodo": _apos_cena2,
    "comum": _apos_cena2,
    "raro": _apos_cena2,
}

TETO_LEDGER = {"familia_mundo": len(FAMILIAS_MUNDO), "prop": len(PROPS),
               "substancia": len(SUBSTANCIAS), "metodo": len(METODOS),
               "comum": len(COMUNS), "raro": len(RAROS), "homem": len(HOMENS)}

MIN_OPCOES = 8


# ---------------------------------------------------------------------------
# AUTOTESTE
# ---------------------------------------------------------------------------

def autoteste(n=600):
    """As invariantes do agente, MEDIDAS, com controles positivos e negativos.

    ⚠️ `0 ERRO` num lote grande e' SUSPEITA, nao aprovacao: pode ser motor limpo
    ou regra morta. Por isso cada trava tem um sabotador, e o sabotador tem de
    CHEGAR onde a regra olha (licoes §16).
    """
    falhas = []
    vistos = collections.defaultdict(set)
    fam = collections.Counter()
    band = collections.Counter()
    larguras = {1: [], 2: [], 3: []}

    for seed in range(n):
        spec = sortear("joe", random.Random(seed), {}, {})
        blocos = montar(spec)
        for tipo, msg in lint(spec, blocos):
            if tipo == "ERRO":
                falhas.append("seed %d (%s): %s" % (seed, spec["mundo"]["id"], msg))
        for eixo, chave in (("mundo", "id"), ("prop", "id"), ("substancia", "id"),
                            ("metodo", "id"), ("comum", "id"), ("raro", "id"),
                            ("homem", "id")):
            vistos[eixo].add(spec[eixo][chave])
        vistos["etnia"].add(spec["etnia"])
        vistos["ref"].add(spec["ref"]["marca"])
        fam[spec["mundo"]["familia"]] += 1
        band[bool(spec["bandeira"])] += 1
        for i, f in enumerate(spec["falas"], 1):
            larguras[i].append(_palavras(f))
        if spec["etnia"] not in spec["mundo"]["etnias"]:
            falhas.append("seed %d: etnia fora do mundo" % seed)

    for eixo, pool in (("mundo", MUNDOS), ("prop", PROPS),
                       ("substancia", SUBSTANCIAS), ("metodo", METODOS),
                       ("comum", COMUNS), ("raro", RAROS), ("homem", HOMENS)):
        if len(vistos[eixo]) != len(pool):
            falhas.append("%s: %d de %d nunca sorteados"
                          % (eixo, len(pool) - len(vistos[eixo]), len(pool)))
    for nome, pool in (("MUNDOS", MUNDOS), ("METODOS", METODOS),
                       ("RAROS", RAROS), ("COMUNS", COMUNS),
                       ("SUBSTANCIAS", SUBSTANCIAS), ("REFS", REFS),
                       ("HOMENS", HOMENS), ("ISCAS", ISCAS),
                       ("VILOES", VILOES), ("USOS", USOS),
                       ("ISCAS_ENTREGA", ISCAS_ENTREGA)):
        # ⚠️ PROPS tem piso PROPRIO de 5 e ele e' EMPIRICO: o pool e' o conjunto
        # dos props que PASSARAM no gerador em teste manual (COLO, 2026-08-03).
        if len(pool) < MIN_OPCOES:
            falhas.append("eixo %s com %d opcoes (minimo %d)"
                          % (nome, len(pool), MIN_OPCOES))
    if len(PROPS) < 5:
        falhas.append("PROPS abaixo do piso empirico de 5")
    for f, q in fam.items():
        if q > n * 0.25:
            falhas.append("familia %s levou %.1f%% do lote (teto 25%%)"
                          % (f, 100.0 * q / n))
    for k, q in band.items():
        if not 0.35 <= q / float(n) <= 0.65:
            falhas.append("bandeira %s em %.1f%% do lote (faixa 35-65%%)"
                          % (k, 100.0 * q / n))

    # ---- CONTROLES ---------------------------------------------------------
    ctrl = []
    s = sortear("joe", random.Random(1), {}, {})
    b = montar(s)

    # ⭐ [BO8] o raro sem o aposto — a diretiva inteira do operador em um controle
    # ⚠️ O controle apontava para a cena 2 e ficou CEGO quando o aposto mudou
    # para a cena 1 — controle que nao acompanha a regra deixa de ser controle.
    s8 = dict(s, falas=list(s["falas"]))
    s8["falas"][0] = s8["falas"][0].replace(
        raro_falado(s["raro"]), s["raro"]["nome"])
    if not any("BO8" in msg for _, msg in lint(s8, b)):
        ctrl.append("[BO8] NAO acusa o ingrediente raro sem o aposto na cena 1")
    if any("BO8" in msg for _, msg in lint(s, b)):
        ctrl.append("[BO8] acusa a forma CERTA (nome + aposto)")

    # ⭐ [BO9] o caso que o operador reprovou: a cena 1 falando do vegetal
    s9b = dict(s, falas=list(s["falas"]))
    s9b["falas"][0] = ("Nobody told you what crushed cinnamon does to an "
                       "eggplant, did they? " + _sentencas(s["falas"][0])[-1])
    if not any("BO9" in msg for _, msg in lint(s9b, b)):
        ctrl.append("[BO9] NAO acusa a cena 1 falando so' do vegetal — o caso "
                    "que o operador reprovou passa pelo medidor")

    # ⭐ [BO9] a abertura orfa — a licao §21 como controle
    s9 = dict(s, falas=list(s["falas"]))
    s9["falas"][0] = "Did you know that this happens? " + _sentencas(s["falas"][0])[-1]
    if not any("BO9" in msg for _, msg in lint(s9, b)):
        ctrl.append("[BO9] NAO acusa abertura sem referente (licoes §21)")

    # [BO11] nome cientifico
    s11 = dict(s, falas=list(s["falas"]))
    s11["falas"][1] = s11["falas"][1] + " Lepidium meyenii, to be exact."
    if not any("BO11" in msg for _, msg in lint(s11, b)):
        ctrl.append("[BO11] nao acusa nome cientifico na fala")

    # [BO10] o centimetro que o operador cortou
    s10 = dict(s, falas=list(s["falas"]))
    s10["falas"][2] = s10["falas"][2] + " Up to 5 inches in a week."
    if not any("BO10" in msg for _, msg in lint(s10, b)):
        ctrl.append("[BO10] nao acusa medida de crescimento")

    # [BO3] vilao sem dono
    s3 = dict(s, falas=list(s["falas"]))
    s3["falas"][0] = _sentencas(s["falas"][0])[0] + " It never worked anyway."
    if not any("BO3" in msg for _, msg in lint(s3, b)):
        ctrl.append("[BO3] nao acusa vilao sem dono")

    # [BO6] o homem falando / olhando a lente
    b6 = dict(b)
    b6["TAKE 03/03"] = b6["TAKE 03/03"].replace("never speaks", "also speaks")
    if not any("BO6" in msg for _, msg in lint(s, b6)):
        ctrl.append("[BO6] nao acusa o homem sem a trava de mudez")
    b6b = dict(b)
    b6b["IMAGE 03/03"] = b6b["IMAGE 03/03"].replace("never at the camera",
                                                    "and at the camera")
    if not any("BO6" in msg for _, msg in lint(s, b6b)):
        ctrl.append("[BO6] nao acusa o homem olhando a lente")

    # [BO5] copo adiantado
    b5 = dict(b)
    b5["IMAGE 01/03"] += " " + BO_COPO
    if not any("BO5" in msg for _, msg in lint(s, b5)):
        ctrl.append("[BO5] nao acusa o copo fora da cena 3")

    # [BO4] gelatin trick fora da cena 2
    s4 = dict(s, falas=list(s["falas"]))
    s4["falas"][1] = s4["falas"][1].replace("gelatin trick", "morning routine")
    if not any("BO4" in msg for _, msg in lint(s4, b)):
        ctrl.append("[BO4] nao acusa a cena 2 sem o `gelatin trick`")

    # o lote limpo NAO pode ser acusado
    if [x for t, x in lint(s, b) if t == "ERRO"]:
        ctrl.append("o lote limpo esta' sendo reprovado — regra que reprova "
                    "tudo nunca foi testada")

    print("MUNDOS %d em %d familias | METODOS %d | RAROS %d | COMUNS %d | "
          "SUBSTANCIAS %d | REFS %d | HOMENS %d"
          % (len(MUNDOS), len(FAMILIAS_MUNDO), len(METODOS), len(RAROS),
             len(COMUNS), len(SUBSTANCIAS), len(REFS), len(HOMENS)))
    print("%d videos | mundos %d/%d | etnias %d | metodos %d/%d | raros %d/%d"
          % (n, len(vistos["mundo"]), len(MUNDOS), len(vistos["etnia"]),
             len(vistos["metodo"]), len(METODOS), len(vistos["raro"]),
             len(RAROS)))
    print("familia mais frequente: %s com %.1f%% | bandeira COM %.1f%%"
          % (fam.most_common(1)[0][0], 100.0 * fam.most_common(1)[0][1] / n,
             100.0 * band[True] / n))
    for i in (1, 2, 3):
        L = larguras[i]
        print("  cena %d: %d-%d palavras (media %.1f) | piso %d teto %d | %.2f p/s"
              % (i, min(L), max(L), sum(L) / float(len(L)), PISO_FALA[i],
                 TETO_FALA[i], sum(L) / float(len(L)) / 8))

    if ctrl:
        # ⛔ ASCII de proposito: o console do Windows e' cp1252.
        print("\n>> O AUTOTESTE ESTA' CEGO:")
        for c in ctrl:
            print("   %s" % c)
    if falhas:
        print("\n>> %d FALHA(S):" % len(falhas))
        for f in falhas[:20]:
            print("   %s" % f)
    if not falhas and not ctrl:
        print("\nAUTOTESTE OK — e os controles reprovam quando devem.")
    return 1 if (falhas or ctrl) else 0


def main():
    ap = argparse.ArgumentParser(description="Randomizador do agente BOTICA SHORT")
    ap.add_argument("--pagina", choices=sorted(ETNIA))
    ap.add_argument("--n", type=int, default=1)
    ap.add_argument("--seed", type=int)
    ap.add_argument("--nicho", choices=FAMILIAS_MUNDO)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--autoteste", action="store_true")
    a = ap.parse_args()
    if a.autoteste:
        return autoteste()
    if not a.pagina:
        ap.error("--pagina obrigatorio")

    seed = a.seed if a.seed is not None else random.randrange(10 ** 6)
    rng = random.Random(seed)
    led = _carregar_ledger()
    travas = {"familia_mundo": a.nicho} if a.nicho else {}

    for _ in range(a.n):
        spec = sortear(a.pagina, rng, led, travas)
        blocos = montar(spec)
        print("=" * 72)
        print("SPEC — pagina %s | seed %s" % (a.pagina, seed))
        print(resumo_pt(spec))
        print("=" * 72)
        for nome, txt in blocos.items():
            print(txt if nome.startswith("BLOCO")
                  else "\n%s\n%s" % ("-" * 72, txt))
        ach = lint(spec, blocos)
        print("\n" + "=" * 72)
        if ach:
            for tipo, msg in ach:
                print("[%s] %s" % (tipo, msg))
            print("%d achado(s)." % len(ach))
        else:
            print("LINTER: OK — nenhuma violacao mecanica.")
        if not a.dry_run:
            u = led.setdefault(a.pagina, {})
            for eixo, val in (("familia_mundo", spec["mundo"]["familia"]),
                              ("prop", spec["prop"]["id"]),
                              ("substancia", spec["substancia"]["id"]),
                              ("metodo", spec["metodo"]["id"]),
                              ("comum", spec["comum"]["id"]),
                              ("raro", spec["raro"]["id"]),
                              ("homem", spec["homem"]["id"])):
                u.setdefault(eixo, [])
                if val not in u[eixo]:
                    u[eixo].append(val)
                if len(u[eixo]) >= TETO_LEDGER[eixo]:
                    u[eixo] = [val]
    if not a.dry_run:
        _gravar_ledger(led)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
