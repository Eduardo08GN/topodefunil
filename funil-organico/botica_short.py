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
import sys

import short_comum as sc
from nucleo_sonoro import sonorizar

AQUI = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(AQUI, ".botica-short-ledger.json")

TITULO = "AGENTE BOTICA SHORT"
SLUG = "botica-short"
SUBTITULO = ("a botica de casa contra a farmacia · o preparo e' a prova · "
             "gerador offline de prompts Veo")

# ⭐ QUEM NARRA — o sexo de quem fala com a lente (2026-08-06).
# Ordem do operador: *"uma marcacao dentro dos agentes python, de todos, pra
# saber se aquele agente gera roteiros com personagem homens e mulheres como
# narrador/apresentador ou se so' gera com um dos dois"*.
# ⛔ MEDIDO, nao lido: 120 sorteios por agente, olhando o BLOCO 0 do prompt.
# Declarar de cabeca aqui seria a mesma FORMA-sem-FUNCAO que ja' custou o
# botao de pele morto em tres motores.
# ⚠️ Com DOIS sexos a UI desenha a trava homem/mulher; com um so', nao desenha
# botao nenhum — botao que nao trava nada e' pior que botao nenhum.
SEXOS = ("mulher",)

ETNIA = {
    # ⭐ As 5 paginas do lote de 2026-08-05. Split 3 brancos / 2 negros —
    # a razao (volume absoluto x prevalencia) esta' escrita no
    # `bridge-pages-deploy.md`.
    "roy": "white American", "dean": "white American",
    "earl": "white American",
    "jason": "Black American", "philippe": "Black American",
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
# ⛔⛔ UM CANUDO, E O COPO VARIA — ordem do Ed, repetida. Ele ja tinha pedido
# ("dois canudos? quero so um") e eu nao apliquei AQUI: isto era uma CONSTANTE,
# nao um pool, entao saia identico em 100% dos videos, sempre com os dois
# canudos. Constante nao varia por definicao — foi o proprio formato que fez o
# pedido dele nao chegar neste agente.
#
# ⚠️ O QUE NAO PODE MUDAR entre as variacoes, porque e' o que faz a cena
# funcionar: o liquido e' OPACO e CLARO (a gelatina tem de parecer bebida, nao
# agua), o copo esta' CHEIO ATE A BORDA, e ele e' o objeto que a mao empurra
# para a lente no frame em que a boca diz `gelatin`. O que varia e' o vasilhame
# e o canudo — nunca a leitura.
COPOS = [
    "a tall clear glass filled to the top with a thick pale drink, a single "
    "paper straw standing in it",
    "a straight-sided mason jar filled to the top with a thick pale drink, one "
    "striped paper straw standing in it",
    "a heavy tumbler filled to the top with a thick pale drink, one short paper "
    "straw standing in it",
    "a ribbed drinking glass filled to the top with a thick pale drink, a single "
    "paper straw standing in it",
    "a stemless glass filled to the top with a thick pale drink, one paper straw "
    "leaning against the rim",
    "a tall narrow glass filled to the top with a thick pale drink, a single "
    "wide paper straw standing in it",
    "a squat wide-mouthed glass filled to the top with a thick pale drink, one "
    "paper straw standing in it",
    "a clear glass mug filled to the top with a thick pale drink, a single paper "
    "straw standing in it",
    "a footed glass filled to the top with a thick pale drink, one paper straw "
    "standing in it",
    "a plain drinking glass filled to the top with a thick pale drink, a single "
    "paper straw resting in it",
]

# ⚠️ mantido como nome so' para o que ainda referencia a constante fora do
# sorteio; o valor real do video vem de `spec["copo"]`.
BO_COPO = COPOS[0]

# ⭐⭐ BO6 — O HOMEM MUDO. Ordem do operador: *"no take final, alem do ref
# falando, havera um homem sempre atras, com cara de espanto e surpresa e
# olhando para o objeto na mao do ref"*.
# ⛔ Ele olha para O COPO, nunca para a lente, e NUNCA fala. E' a mesma mecanica
# da plateia congelada do ESCANDALO: ele encena o espanto NO LUGAR do espectador.
# ⚠️ `Only she speaks` e' obrigatorio no TAKE — sem isso o segundo corpo dubla a
# fala dela, que e' a falha que derrubou a cena do casal do VAZAMENTO.
# ⭐⭐ A FEICAO DELE E' POOL desde 2026-08-05 — ordem do operador: *"A feicao de
# reacao do cara no take 3 tem que variar tb na pool, se sorrindo, cara de
# surpresa, etc"*. Antes era UMA string travada (olhos arregalados, boca
# aberta), e por isso os tres prints que ele mandou tinham o mesmo homem com a
# mesma cara.
# ⛔ O QUE NAO VARIA, porque e' a mecanica do angulo e o linter trava: ele olha
# o COPO e nunca a lente, e NUNCA fala. A reacao muda de SABOR (espanto, riso,
# incredulidade, orgulho), nunca de direcao nem de mudez.
# ⚠️ Cada entrada e' (clausula da IMAGE, clausula do TAKE) e as duas tem de
# descrever a MESMA coisa: o take anima a image, nao inventa outro gesto — e
# contradicao entre os dois e' pior que omissao, porque o Veo resolve mexendo
# no que estava certo.
REACOES_HOMEM = [
    # ⛔⛔ A CARA DE SURPRESA SAIU (2026-08-07, ordem do operador). O pool
    # anterior tinha 12 entradas e SETE delas eram boca aberta ou olho
    # arregalado — "his eyes are wide... his mouth open in plain astonishment",
    # "his eyes have gone round", "his jaw has gone slack". Renderizado, aquilo
    # nao le' como reacao humana: le' como emoji de espanto colado num homem,
    # e e' uma das assinaturas mais reconheciveis de video feito por IA.
    # ⭐ O que fica: uma pessoa NORMAL olhando para o copo. A reacao continua
    # variando de sabor — atencao, aprovacao contida, interesse, um aceno — e
    # continua muda e virada para o copo, nunca para a lente.
    # ⚠️ Cada entrada e' (clausula da IMAGE, clausula do TAKE) e as duas tem de
    # descrever a MESMA coisa: o take anima a image, nao inventa outro gesto.
    ("his face is relaxed and he is looking down at it steadily",
     "keeps looking down at it, his face relaxed and still"),
    ("he is watching it with a small closed-mouth smile",
     "holds that small closed-mouth smile without moving"),
    ("his brows are relaxed and his lips are pressed lightly together",
     "keeps his lips lightly pressed and does not move"),
    ("he is looking at it with his head very slightly tilted",
     "keeps his head slightly tilted and does not move"),
    ("he is nodding once, slowly, his mouth closed",
     "finishes the slow nod and then stays still"),
    ("his eyes are steady on it and one corner of his mouth is lifted",
     "holds that one-sided look without moving"),
    ("he is looking down at it with a calm, unhurried expression",
     "keeps that calm expression and does not move"),
    ("his chin is lowered slightly and he is looking at it from under his brows",
     "keeps his chin lowered and does not move"),
    ("he is looking at it plainly, his face giving nothing away",
     "keeps that plain expression without moving"),
    ("his mouth is closed and he is looking at it the way a man reads a label",
     "keeps reading it with his mouth closed, not moving"),
    ("he is looking at it and breathing out slowly through his nose",
     "finishes the slow breath and stays looking at it"),
    ("his expression is settled and he is looking at it without blinking much",
     "keeps that settled expression and does not move"),
]

BO_HOMEM = (
    "Standing behind her and slightly to frame-left, close enough to be in the "
    "same focus, is a %d-year-old %s man, %s, wearing %s. %s, and he is "
    "looking directly at the glass in her hand — never at the camera."
)
BO_HOMEM_TAKE = (
    "The man behind her %s, eyes fixed on the glass the whole time, and never "
    "speaks. Only she speaks, straight into the lens."
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
    {"id": "amish", "eua": True, "selo": "V", "familia": "amish",
     "etnias": ["white American"],
     "coz": "a rustic timber farmhouse kitchen with open shelves of unlabelled "
            "glass jars of dried herbs from floor to ceiling, a hand pump by "
            "the basin and a wide plank table",
     "coz_c": "timber herb kitchen",
     "sup_a": "a heavy scrubbed pine table", "sup": "table",
     # ⭐ CINCO trajes, com SILHUETA diferente — nao cinco cores do mesmo.
     "trajes": [
         ("%s long-sleeved high-collared dress under a black bib apron, with a white cap tied under the chin",
          "black bib apron"),
         ("%s plain caped dress with a white organdy apron over it",
          "organdy apron"),
         ("%s long-sleeved dress with a dark shawl pinned across the shoulders",
          "pinned shawl"),
         ("%s wide-skirted work dress with the sleeves buttoned at the wrist",
          "work dress"),
         ("%s plain dress under a full-length dark pinafore",
          "dark pinafore"),
     ],
     "cores": ["deep plum", "dark brown", "slate blue", "forest green", "charcoal", "wine"],
     "luz": "Soft daylight coming in from a window at frame-right.",
     "luz_c": "soft window daylight",
     "audio": "quiet room tone, a wood floor creaking"},

    {"id": "americana_comum", "eua": True, "selo": "N", "familia": "americana",
     "etnias": ["white American"],
     "coz": "an ordinary American suburban kitchen, honey-oak cabinets and a "
            "row of unlabelled glass spice jars on a shelf above the sink, a "
            "kettle on the hob and a window looking onto the yard",
     "coz_c": "oak suburban kitchen",
     "sup_a": "a speckled granite countertop", "sup": "countertop",
     # ⭐ CINCO trajes, com SILHUETA diferente — nao cinco cores do mesmo.
     "trajes": [
         ("%s knit sweater with the sleeves pushed back",
          "knit sweater"),
         ("%s checked flannel shirt tucked in at the waist",
          "checked flannel"),
         ("%s sleeveless denim shirt over a plain tee",
          "denim shirt"),
         ("%s ribbed turtleneck under a heavy canvas apron",
          "canvas apron"),
         ("%s short-sleeved henley with a dish towel over one shoulder",
          "henley"),
     ],
     "cores": ["dusty rose", "navy", "sage", "mustard", "burgundy", "cream"],
     "luz": "Warm overhead kitchen light with weak daylight behind it.",
     "luz_c": "warm overhead light",
     "audio": "a fridge humming, quiet room tone"},

    {"id": "apalache", "eua": True, "selo": "N", "familia": "apalache",
     "etnias": ["white American"],
     "coz": "a mountain-lodge kitchen with finished pine panelling, bundles of "
            "dried plants hanging from a rail and rows of unlabelled jars "
            "behind glass cabinet doors, a black enamel range in the corner",
     "coz_c": "pine lodge kitchen",
     "sup_a": "a thick oiled butcher-block counter", "sup": "counter",
     # ⭐ CINCO trajes, com SILHUETA diferente — nao cinco cores do mesmo.
     "trajes": [
         ("%s quilted flannel shirt with the sleeves rolled",
          "quilted flannel shirt"),
         ("%s corduroy shirt-jacket over a plain work tee",
          "corduroy shirt-jacket"),
         ("%s wool vest over a long-sleeved plaid shirt",
          "wool vest"),
         ("%s heavy knit cardigan with wooden buttons",
          "knit cardigan"),
         ("%s denim dungarees over a long-sleeved shirt",
          "denim dungarees"),
     ],
     "cores": ["dark red", "forest green", "brown", "slate blue", "mustard", "charcoal"],
     "luz": "Low grey mountain daylight through a small window at frame-left.",
     "luz_c": "low grey daylight",
     "audio": "wind at the window, a stove ticking"},

    {"id": "sulista", "eua": True, "selo": "N", "familia": "sulista",
     "etnias": ["Black American"],
     "coz": "a Southern kitchen with pale yellow beadboard walls, a screen door "
            "open onto a green yard, unlabelled mason jars of dried leaves and "
            "roots along an open shelf and a cast-iron skillet on the hob",
     "coz_c": "yellow beadboard kitchen",
     "sup_a": "a pale blue painted wooden counter", "sup": "counter",
     # ⭐ CINCO trajes, com SILHUETA diferente — nao cinco cores do mesmo.
     "trajes": [
         ("%s short-sleeved button-down shirt",
          "button-down shirt"),
         ("%s floral house dress with a half apron tied at the waist",
          "half apron"),
         ("%s sleeveless linen shift with a headwrap in the same cloth",
          "matching headwrap"),
         ("%s wide-collared blouse tucked into a long skirt",
          "wide-collared blouse"),
         ("%s cotton shirt with the sleeves rolled and a printed apron",
          "printed apron"),
     ],
     "cores": ["sky blue", "deep coral", "emerald", "plum", "marigold", "cream"],
     "luz": "Bright soft daylight through the open screen door.",
     "luz_c": "bright daylight through the door",
     "audio": "cicadas outside, a screen door creaking"},

    {"id": "mexicana", "eua": False, "selo": "N", "familia": "mexicana",
     "etnias": ["Mexican American"],
     "coz": "a Mexican American kitchen with hand-painted blue and yellow tiles "
            "across the backsplash, clay pots and unlabelled jars of dried "
            "herbs stacked on an open shelf and a flat steel comal on the hob",
     "coz_c": "talavera-tiled kitchen",
     "sup_a": "a terracotta-tiled counter", "sup": "counter",
     # ⭐ CINCO trajes, com SILHUETA diferente — nao cinco cores do mesmo.
     "trajes": [
         ("%s embroidered cotton blouse",
          "embroidered blouse"),
         ("%s square-necked huipil with woven trim at the hem",
          "huipil"),
         ("%s ruffled off-shoulder blouse with a woven belt",
          "ruffled blouse"),
         ("%s plain blouse under a striped woven apron",
          "striped apron"),
         ("%s long-sleeved blouse with a rebozo folded over one shoulder",
          "rebozo"),
     ],
     "cores": ["deep red", "marigold", "turquoise", "magenta", "cobalt", "cream"],
     "luz": "Warm afternoon sun coming in low from frame-left.",
     "luz_c": "warm low afternoon sun",
     "audio": "a radio playing faintly in another room"},

    {"id": "caribenha", "eua": False, "selo": "N", "familia": "caribenha",
     "etnias": ["Caribbean American"],
     "coz": "a Caribbean kitchen with mint-green walls and louvred windows "
            "standing open onto broad green leaves, unlabelled jars of bark and "
            "dried flowers on a fitted shelf and matched enamel bowls by the sink",
     "coz_c": "mint-green island kitchen",
     "sup_a": "a pale speckled stone counter", "sup": "counter",
     # ⭐ CINCO trajes, com SILHUETA diferente — nao cinco cores do mesmo.
     "trajes": [
         ("%s loose linen blouse worn open at the collar",
          "loose linen blouse"),
         ("%s madras-check wrap top knotted at the waist",
          "wrap top"),
         ("%s sleeveless cotton shift with a tall bright headwrap",
          "bright headwrap"),
         ("%s short-sleeved blouse with a full printed skirt",
          "printed skirt"),
         ("%s off-shoulder blouse with wide ruffled sleeves",
          "ruffled sleeves"),
     ],
     "cores": ["sea blue", "coral", "lime green", "hot pink", "pale yellow", "white"],
     "luz": "Hard bright island daylight coming through the louvres.",
     "luz_c": "hard bright daylight",
     "audio": "birds outside, a ceiling fan turning"},

    {"id": "leste_asia", "eua": False, "selo": "N", "familia": "asiatica",
     "etnias": ["East Asian American"],
     "coz": "a compact East Asian kitchen with a wall of small wooden drawers "
            "and unlabelled glass jars of dried roots and bark, a clay pot on "
            "the hob and a bamboo steamer stacked on a shelf",
     "coz_c": "wooden-drawer kitchen",
     "sup_a": "a pale grey stone counter", "sup": "counter",
     # ⭐ CINCO trajes, com SILHUETA diferente — nao cinco cores do mesmo.
     "trajes": [
         ("%s round-collared cotton jacket",
          "cotton jacket"),
         ("%s side-fastening mandarin-collar tunic",
          "mandarin tunic"),
         ("%s wide-sleeved linen wrap top tied at the side",
          "linen wrap top"),
         ("%s quilted vest over a long-sleeved shirt",
          "quilted vest"),
         ("%s plain shirt under a dark half apron with deep pockets",
          "half apron"),
     ],
     "cores": ["indigo", "charcoal", "moss green", "deep teal", "rust", "oat"],
     "luz": "Even cool daylight from a window behind the camera.",
     "luz_c": "even cool daylight",
     "audio": "a clay pot simmering, quiet room tone"},

    {"id": "sul_asia", "eua": False, "selo": "N", "familia": "sul_asiatica",
     "etnias": ["South Asian American"],
     "coz": "a South Asian kitchen with polished stone surfaces, a row of round "
            "steel tins and unlabelled jars of coloured powders along an open "
            "shelf, a heavy pestle and a steel tumbler beside the sink",
     "coz_c": "polished stone kitchen",
     "sup_a": "a dark polished granite counter", "sup": "counter",
     # ⭐ CINCO trajes, com SILHUETA diferente — nao cinco cores do mesmo.
     "trajes": [
         ("%s long-sleeved kurta",
          "kurta"),
         ("%s cotton sari with the pallu tucked in at the waist",
          "cotton sari"),
         ("%s salwar kameez with a light dupatta over one shoulder",
          "salwar kameez"),
         ("%s short-sleeved kurti over straight trousers",
          "kurti"),
         ("%s printed blouse with a wrapped cotton shawl",
          "cotton shawl"),
     ],
     "cores": ["deep maroon", "marigold", "emerald", "saffron", "royal blue", "off-white"],
     "luz": "Warm even daylight from a window at frame-right.",
     "luz_c": "warm even daylight",
     "audio": "a pressure cooker hissing softly, quiet room tone"},

    {"id": "africa_oeste", "eua": False, "selo": "N", "familia": "africana",
     "etnias": ["West African"],
     "coz": "a well-kept West African kitchen with glazed tiled walls, rows of "
            "unlabelled jars and calabashes of dried bark and seed in a fitted "
            "cabinet, a carved mortar on the side and a door open onto a swept "
            "green courtyard",
     "coz_c": "tiled West African kitchen",
     "sup_a": "a polished dark granite counter", "sup": "counter",
     # ⭐ CINCO trajes, com SILHUETA diferente — nao cinco cores do mesmo.
     "trajes": [
         ("%s short-sleeved embroidered cotton tunic",
          "embroidered tunic"),
         ("%s wax-print wrapper tied at the waist with a matching top",
          "wax-print wrapper"),
         ("%s wide-sleeved boubou with gold thread at the neck",
          "boubou"),
         ("%s fitted print dress with a tall matching headwrap",
          "tall headwrap"),
         ("%s plain blouse under a wax-print apron",
          "wax-print apron"),
     ],
     "cores": ["indigo", "deep green", "ochre", "bright orange", "royal blue", "white"],
     "luz": "Strong flat daylight coming through the open doorway.",
     "luz_c": "strong flat daylight",
     "audio": "voices far off outside, quiet room tone"},

    {"id": "africa_leste", "eua": False, "selo": "N", "familia": "africana",
     "etnias": ["East African"],
     "coz": "a tidy East African kitchen with pale tiled walls and a wide "
            "shuttered window, woven baskets and unlabelled jars of dried "
            "leaves ranged along a fitted shelf, a stainless kettle on the hob",
     "coz_c": "pale tiled kitchen",
     "sup_a": "a solid hardwood worktop", "sup": "worktop",
     # ⭐ CINCO trajes, com SILHUETA diferente — nao cinco cores do mesmo.
     "trajes": [
         ("%s open-collared cotton shirt",
          "cotton shirt"),
         ("%s printed kanga wrapped over one shoulder",
          "kanga"),
         ("%s long tunic dress with fine embroidery at the neckline",
          "tunic dress"),
         ("%s sleeveless linen top with a folded headscarf",
          "folded headscarf"),
         ("%s buttoned blouse with a wrapped patterned skirt",
          "patterned skirt"),
     ],
     "cores": ["deep purple", "terracotta", "bright green", "sky blue", "cobalt", "white"],
     "luz": "Soft daylight through the shutters at frame-left.",
     "luz_c": "soft shuttered daylight",
     "audio": "a kettle ticking, quiet room tone"},

    {"id": "mediterranea", "eua": False, "selo": "N", "familia": "mediterranea",
     "etnias": ["Mediterranean"],
     "coz": "a whitewashed Mediterranean kitchen with a low arched window, "
            "bunches of dried herbs hanging on a hook, unlabelled jars of seed "
            "and leaf on an open shelf and a large tin of oil by the door",
     "coz_c": "whitewashed arched kitchen",
     "sup_a": "a thick pale marble counter", "sup": "counter",
     # ⭐ CINCO trajes, com SILHUETA diferente — nao cinco cores do mesmo.
     "trajes": [
         ("%s linen blouse with the sleeves rolled",
          "linen blouse"),
         ("%s sleeveless cotton dress with a canvas apron over it",
          "canvas apron"),
         ("%s buttoned shirt-dress belted at the waist",
          "shirt-dress"),
         ("%s crocheted cardigan over a plain vest top",
          "crocheted cardigan"),
         ("%s wide-necked blouse with a scarf knotted at the throat",
          "knotted scarf"),
     ],
     "cores": ["olive", "terracotta", "deep navy", "mustard", "pale blue", "white"],
     "luz": "Hard bright Mediterranean sun through the arched window.",
     "luz_c": "hard bright sun",
     "audio": "gulls far off, quiet room tone"},

    {"id": "andina", "eua": False, "selo": "N", "familia": "andina",
     "etnias": ["Andean South American"],
     "coz": "an Andean kitchen with smooth painted walls and a tiled splashback, "
            "fine woven cloth folded on a bench, labelled sacks and jars of "
            "dried root and grain squared along a built shelf and a glazed "
            "tiled stove in the corner",
     "coz_c": "tiled andean kitchen",
     "sup_a": "a thick oiled hardwood work table", "sup": "table",
     # ⭐ CINCO trajes, com SILHUETA diferente — nao cinco cores do mesmo.
     "trajes": [
         ("%s woven wool cardigan over a plain blouse",
          "wool cardigan"),
         ("%s embroidered wool skirt with a fitted jacket",
          "embroidered skirt"),
         ("%s striped manta folded over the shoulders",
          "striped manta"),
         ("%s knitted vest over a long-sleeved blouse",
          "knitted vest"),
         ("%s pleated pollera with a plain buttoned top",
          "pollera"),
     ],
     "cores": ["deep red", "burnt orange", "indigo", "emerald", "magenta", "cream"],
     "luz": "Cool high-altitude daylight from a small window at frame-right.",
     "luz_c": "cool high daylight",
     "audio": "wind outside, quiet room tone"},

    # ======================================================================
    # + 2026-08-05 — DOZE ARQUETIPOS NORTE-AMERICANOS.
    # ⛔ Ordem do operador: *"preciso que popule com varias pools de varios
    # arqueticos de africa north americans no agente e north americans white
    # people"*.
    # ⚠️ E o gargalo era pior do que parecia: `Black American` tinha UM UNICO
    # mundo (`sulista`) contra tres do `white American` — e METADE das paginas
    # do funil e' Black American. Cinco paginas sorteavam sempre a mesma
    # cozinha. Agora sao 7 e 9.
    # ⭐ Cada arquetipo e' uma REGIAO com cultura material propria, nao um
    # rotulo: Lowcountry, Delta, Grandes Lagos, Creole, Atlanta e Harlem; e
    # Meio-Oeste, Nova Inglaterra, Texas, Noroeste, italo e polonesa.
    # ======================================================================
    {"id": "gullah", "selo": "N", "familia": "gullah",
     "etnias": ["Black American"],
     "eua": True,
     "coz": "a Lowcountry kitchen with wide beadboard walls painted haint blue, a tall sash window onto live oaks and hanging moss, rows of unlabelled jars of dried root and bark in a fitted shelf and a cast-iron pot on the hob",
     "coz_c": "haint-blue Lowcountry kitchen",
     "sup_a": "a scrubbed heart-pine counter", "sup": "counter",
     "trajes": [
         ("%s wide-sleeved cotton blouse with a wrapped head tie",
          "wrapped head tie"),
         ("%s indigo-dyed shift dress with a woven sweetgrass belt",
          "indigo shift"),
         ("%s fitted short-sleeved blouse over a long tie-dyed skirt",
          "tie-dyed skirt"),
         ("%s linen tunic with a strip-woven cloth over one shoulder",
          "strip-woven cloth"),
         ("%s buttoned cotton dress with a full-length work apron",
          "work apron"),
     ],
     "cores": ["indigo", "haint blue", "deep coral", "ochre", "emerald", "white"],
     "luz": "Soft green-filtered daylight through the tall sash window.",
     "luz_c": "green-filtered daylight",
     "audio": "cicadas and marsh birds outside"},
    {"id": "delta", "selo": "N", "familia": "delta",
     "etnias": ["Black American"],
     "eua": True,
     "coz": "a Delta farmhouse kitchen with white-painted plank walls, a wide window onto flat cotton fields, unlabelled jars of dried leaf and root ranged on a built shelf and a heavy cream enamel range",
     "coz_c": "white plank Delta kitchen",
     "sup_a": "a thick oiled oak counter", "sup": "counter",
     "trajes": [
         ("%s printed cotton house dress with a bib apron",
          "bib apron"),
         ("%s fitted gingham blouse tucked into a wide skirt",
          "gingham blouse"),
         ("%s sleeveless denim shift over a plain tee",
          "denim shift"),
         ("%s wrapped cotton dress with a knotted head scarf",
          "knotted head scarf"),
         ("%s buttoned work shirt with the sleeves rolled to the elbow",
          "rolled work shirt"),
     ],
     "cores": ["deep red", "cobalt", "marigold", "forest green", "plum", "white"],
     "luz": "Flat bright daylight off the fields through the wide window.",
     "luz_c": "flat field daylight",
     "audio": "a tractor far off, wind in the screen"},
    {"id": "grandes_lagos", "selo": "N", "familia": "grandes_lagos",
     "etnias": ["Black American"],
     "eua": True,
     "coz": "a well-kept city apartment kitchen with glazed white tile to the ceiling, tall sash windows onto the brick building opposite, unlabelled glass jars of dried herb behind a glass-front cabinet and a heavy enamel stove",
     "coz_c": "white-tiled city kitchen",
     "sup_a": "a polished speckled granite counter", "sup": "counter",
     "trajes": [
         ("%s ribbed knit sweater with the sleeves pushed up",
          "ribbed knit sweater"),
         ("%s silk headwrap tied high over a fitted blouse",
          "silk headwrap"),
         ("%s wrap dress belted at the waist",
          "wrap dress"),
         ("%s tailored blouse under a fitted waistcoat",
          "fitted waistcoat"),
         ("%s long-sleeved top with a beaded necklace at the throat",
          "beaded necklace"),
     ],
     "cores": ["burgundy", "royal blue", "mustard", "emerald", "charcoal", "cream"],
     "luz": "Cool north light through the tall sash windows.",
     "luz_c": "cool north light",
     "audio": "city traffic far below, a radiator ticking"},
    {"id": "creole", "selo": "N", "familia": "creole",
     "etnias": ["Black American"],
     "eua": True,
     "coz": "a New Orleans Creole kitchen with tall shuttered French doors onto a courtyard, plaster walls in soft ochre, unlabelled apothecary jars of dried root along a carved shelf and a copper pot on the hob",
     "coz_c": "ochre Creole kitchen",
     "sup_a": "a veined marble counter", "sup": "counter",
     "trajes": [
         ("%s ruffled cotton blouse with a fitted bodice",
          "ruffled blouse"),
         ("%s madras head tie knotted high above a fitted dress",
          "madras head tie"),
         ("%s embroidered linen dress with a lace collar",
          "lace collar"),
         ("%s short-sleeved blouse under a long striped apron",
          "striped apron"),
         ("%s draped shawl over a high-necked fitted dress",
          "draped shawl"),
     ],
     "cores": ["deep purple", "gold", "wine", "sea green", "coral", "cream"],
     "luz": "Warm dappled light through the shuttered French doors.",
     "luz_c": "dappled courtyard light",
     "audio": "a courtyard fountain, distant brass"},
    {"id": "atlanta", "selo": "N", "familia": "atlanta",
     "etnias": ["Black American"],
     "eua": True,
     "coz": "a bright modern suburban kitchen with white shaker cabinets and a subway-tiled splashback, a wide window onto a kept back garden, labelled glass jars of dried herb on floating shelves and a stainless range",
     "coz_c": "white shaker kitchen",
     "sup_a": "a honed black granite island", "sup": "island",
     "trajes": [
         ("%s fitted knit top with the sleeves pushed back",
          "fitted knit top"),
         ("%s satin headwrap tied over a sleeveless shell top",
          "satin headwrap"),
         ("%s buttoned linen shirt worn open over a vest top",
          "open linen shirt"),
         ("%s jersey wrap top knotted at the side",
          "jersey wrap top"),
         ("%s cotton dress under a cropped denim jacket",
          "cropped denim jacket"),
     ],
     "cores": ["dusty rose", "olive", "burnt orange", "teal", "ivory", "wine"],
     "luz": "Bright even daylight through the wide garden window.",
     "luz_c": "bright garden daylight",
     "audio": "birds in the garden, a fridge humming"},
    {"id": "harlem", "selo": "N", "familia": "harlem",
     "etnias": ["Black American"],
     "eua": True,
     "coz": "a brownstone kitchen with tall bay windows onto a tree-lined street, dark stained cabinets with glass doors, unlabelled jars of dried root on an open shelf and a heavy cast-iron pot on the range",
     "coz_c": "brownstone kitchen",
     "sup_a": "a thick oiled butcher-block counter", "sup": "counter",
     "trajes": [
         ("%s long cardigan over a fitted shell top",
          "long cardigan"),
         ("%s printed headwrap tied at the front over a roll-neck",
          "printed headwrap"),
         ("%s buttoned shirt-dress with a wide belt",
          "wide belt"),
         ("%s wide-legged jumpsuit with the sleeves rolled",
          "wide-legged jumpsuit"),
         ("%s knitted vest over a long-sleeved blouse",
          "knitted vest"),
     ],
     "cores": ["mustard", "rust", "deep teal", "burgundy", "camel", "ivory"],
     "luz": "Soft filtered light through the tall bay windows.",
     "luz_c": "filtered bay-window light",
     "audio": "street noise below, a stoop conversation"},
    {"id": "meio_oeste", "selo": "N", "familia": "meio_oeste",
     "etnias": ["white American"],
     "eua": True,
     "coz": "a Midwest farmhouse kitchen with painted wainscot and a wide window onto flat corn fields, glass-front cabinets of home preserves, unlabelled jars of dried herb on a built shelf and a big cream enamel range",
     "coz_c": "farmhouse kitchen",
     "sup_a": "a thick maple butcher-block counter", "sup": "counter",
     "trajes": [
         ("%s fitted gingham shirt tucked into a denim skirt",
          "gingham shirt"),
         ("%s knitted cardigan over a plain blouse",
          "knitted cardigan"),
         ("%s bib apron over a long-sleeved tee",
          "bib apron"),
         ("%s corduroy pinafore over a roll-neck",
          "corduroy pinafore"),
         ("%s short-sleeved shirt with a dish towel tucked at the waist",
          "tucked dish towel"),
     ],
     "cores": ["barn red", "denim blue", "sage", "mustard", "hunter green", "cream"],
     "luz": "Wide flat daylight off the fields.",
     "luz_c": "flat prairie daylight",
     "audio": "wind over the fields, a screen door"},
    {"id": "nova_inglaterra", "selo": "N", "familia": "nova_inglaterra",
     "etnias": ["white American"],
     "eua": True,
     "coz": "a New England coastal kitchen with white-painted panelling and a window onto grey water and rigging, glass-front cabinets of preserves, unlabelled jars of dried herb along a plate rail and a cream enamel range",
     "coz_c": "white-panelled coastal kitchen",
     "sup_a": "a honed slate counter", "sup": "counter",
     "trajes": [
         ("%s cable-knit fisherman jumper",
          "cable-knit jumper"),
         ("%s fitted striped Breton top with the sleeves pushed up",
          "Breton top"),
         ("%s quilted waistcoat over a checked shirt",
          "quilted waistcoat"),
         ("%s oilskin apron buttoned over a roll-neck",
          "oilskin apron"),
         ("%s linen shirt-dress belted at the waist",
          "linen shirt-dress"),
     ],
     "cores": ["navy", "seafoam", "brick red", "forest green", "slate grey", "oatmeal"],
     "luz": "Cool overcast light off the water.",
     "luz_c": "cool overcast sea light",
     "audio": "gulls and rigging outside"},
    {"id": "texas", "selo": "N", "familia": "texas",
     "etnias": ["white American"],
     "eua": True,
     "coz": "a Texas ranch kitchen with hand-glazed talavera tiles behind a wide range, exposed cedar beams, unlabelled jars of dried herb in a tall pine dresser and a window onto open scrub",
     "coz_c": "cedar-beamed ranch kitchen",
     "sup_a": "a thick mesquite-wood counter", "sup": "counter",
     "trajes": [
         ("%s fitted pearl-snap western shirt with the sleeves rolled",
          "pearl-snap shirt"),
         ("%s denim shirt-dress with a tooled leather belt",
          "tooled leather belt"),
         ("%s suede waistcoat over a fitted blouse",
          "suede waistcoat"),
         ("%s checked shirt knotted at the waist",
          "knotted checked shirt"),
         ("%s cotton blouse with a bandana tied at the throat",
          "bandana"),
     ],
     "cores": ["turquoise", "rust", "denim blue", "burnt orange", "deep red", "bone"],
     "luz": "Hard bright sun through the scrub-side window.",
     "luz_c": "hard ranch sunlight",
     "audio": "wind over dry scrub, a distant gate"},
    {"id": "noroeste", "selo": "N", "familia": "noroeste",
     "etnias": ["white American"],
     "eua": True,
     "coz": "a Pacific Northwest kitchen with wide fir boards and open shelving, tall windows onto dark evergreens and rain, labelled glass jars of dried herb in a run of fitted shelves and a matte black range",
     "coz_c": "fir-panelled kitchen",
     "sup_a": "a live-edge walnut counter", "sup": "counter",
     "trajes": [
         ("%s heavy flannel shirt worn open over a fitted tee",
          "open flannel"),
         ("%s waffle-knit roll-neck with the sleeves pushed up",
          "waffle roll-neck"),
         ("%s canvas work apron over a long-sleeved shirt",
          "canvas apron"),
         ("%s chunky wool cardigan with deep pockets",
          "chunky cardigan"),
         ("%s denim dungarees over a striped long-sleeve",
          "denim dungarees"),
     ],
     "cores": ["moss green", "rust", "slate blue", "mustard", "charcoal", "oatmeal"],
     "luz": "Soft grey rain light through the tall windows.",
     "luz_c": "grey rain light",
     "audio": "rain on the glass, wind in the firs"},
    {"id": "italo_americana", "selo": "N", "familia": "italo_americana",
     "etnias": ["white American"],
     "eua": True,
     "coz": "an Italian-American kitchen with a tiled splashback in green and cream, a crowded dresser of matched crockery, unlabelled jars of dried herb on an open shelf and a big pot on a six-burner range",
     "coz_c": "green-tiled kitchen",
     "sup_a": "a thick marble pastry counter", "sup": "counter",
     "trajes": [
         ("%s fitted wrap-front blouse with three-quarter sleeves",
          "wrap-front blouse"),
         ("%s floral housecoat buttoned to the throat",
          "floral housecoat"),
         ("%s knitted twinset with a fine gold chain",
          "knitted twinset"),
         ("%s plain blouse under a full pinny",
          "full pinny"),
         ("%s belted shirt-dress with the sleeves rolled",
          "belted shirt-dress"),
     ],
     "cores": ["deep red", "olive", "navy", "gold", "aubergine", "cream"],
     "luz": "Warm kitchen light with sun through a side window.",
     "luz_c": "warm side-window light",
     "audio": "a radio in another room, a pot lid"},
    {"id": "polonesa", "selo": "N", "familia": "polonesa",
     "etnias": ["white American"],
     "eua": True,
     "coz": "a Polish-American kitchen with cream-painted cabinets and a hand-painted folk border along the wall, a tall dresser of matched china, unlabelled jars of dried herb and a heavy enamel range",
     "coz_c": "folk-bordered kitchen",
     "sup_a": "a scrubbed birch counter", "sup": "counter",
     "trajes": [
         ("%s embroidered folk blouse with full sleeves",
          "embroidered folk blouse"),
         ("%s printed headscarf tied under the chin over a fitted dress",
          "printed headscarf"),
         ("%s wool waistcoat over a white blouse",
          "wool waistcoat"),
         ("%s buttoned housedress with a half apron",
          "half apron"),
         ("%s knitted jumper with the sleeves pushed back",
          "knitted jumper"),
     ],
     "cores": ["deep red", "cobalt", "forest green", "amber", "burgundy", "white"],
     "luz": "Clean cool daylight through a lace-edged window.",
     "luz_c": "cool lace-filtered daylight",
     "audio": "a clock ticking, a kettle settling"},

    # ⭐⭐ + 2026-08-13 — SEIS BOTICAS NOVAS, de 24 para 30. Ordem do operador:
    # *"aumente o pool de opcoes substancialmente, tambem dos ambientes"*.
    # ⛔ CADA UMA E' AMBIENTE INTEIRO, no mesmo nivel das vinte e quatro de cima:
    # cozinha COM A TRADICAO DE ERVAS dentro (que e' a autoridade do angulo),
    # superficie, cinco trajes de silhueta diferente, seis cores, luz e audio.
    # Fundo novo com o resto herdado nao e' mundo, e' papel de parede.
    # ⛔ ZERO texto legivel, como as outras: os potes entram `unlabelled`, porque
    # a CAUDA promete "No on-screen text" e etiqueta escrita e' texto em cena.
    # ⚠️ A COBERTURA DE ETNIA SOBE nas duas que as paginas usam — `white
    # American` vai de 10 para 12 e `Black American` de 7 para 9. Nenhuma pele
    # fica com menos cenario do que tinha, que e' o que derrubaria a trava.
    # ⭐ Duas sao de fora dos EUA (`eua: False`), como as oito herdadas: o selo
    # governa a clausula de apelo, e um pool 100% americano o deixaria morto.
    {"id": "ozark", "selo": "N", "familia": "ozark",
     "eua": True,
     "etnias": ["white American"],
     "coz": "an Ozark hill kitchen with bare board walls, bunches of dried "
            "roots strung along a beam and unlabelled jars crowding a plank "
            "shelf, a hand pump at the stone sink and a squat wood range",
     "coz_c": "board-walled hill kitchen",
     "sup_a": "a scrubbed plank worktable", "sup": "table",
     # ⭐ CINCO trajes, com SILHUETA diferente — nao cinco cores do mesmo.
     "trajes": [
         ("%s long-sleeved calico dress with a bib apron over it",
          "calico bib apron"),
         ("%s quilted vest over a plain work blouse",
          "quilted vest"),
         ("%s buttoned shirtdress with the sleeves rolled to the elbow",
          "rolled shirtdress"),
         ("%s knitted shawl pinned over a long skirt and blouse",
          "pinned shawl"),
         ("%s denim pinafore over a checked shirt",
          "denim pinafore"),
     ],
     "cores": ["dark red", "butter yellow", "slate blue", "moss green", "brown", "cream"],
     "luz": "Low daylight through a small deep-set window at frame-left.",
     "luz_c": "low deep-set daylight",
     "audio": "a wood range ticking, wind in the trees"},

    {"id": "memphis", "selo": "N", "familia": "memphis",
     "eua": True,
     "etnias": ["Black American"],
     "coz": "a Memphis shotgun-house kitchen with cream tongue-and-groove "
            "walls, a window fan turning in the frame, unlabelled jars of "
            "dried leaves and roots along a chrome-edged shelf and cast-iron "
            "on the range",
     "coz_c": "cream shotgun-house kitchen",
     "sup_a": "a chrome-edged formica counter", "sup": "counter",
     # ⭐ CINCO trajes, com SILHUETA diferente — nao cinco cores do mesmo.
     "trajes": [
         ("%s wrapped house dress tied at the waist",
          "wrapped house dress"),
         ("%s sleeveless shift with a headwrap in the same cloth",
          "matching headwrap"),
         ("%s short-sleeved blouse tucked into a long full skirt",
          "tucked blouse"),
         ("%s printed duster coat worn open over a plain dress",
          "printed duster"),
         ("%s cotton shirt with the sleeves rolled and a half apron",
          "rolled cotton shirt"),
     ],
     "cores": ["gold", "deep coral", "teal", "plum", "ivory", "wine"],
     "luz": "Warm low sun cutting through the window fan.",
     "luz_c": "warm fan-cut sun",
     "audio": "a window fan turning, a radio through a wall"},

    {"id": "escandinava", "selo": "N", "familia": "escandinava",
     "eua": True,
     "etnias": ["white American"],
     "coz": "a Scandinavian-American farm kitchen in the Upper Midwest, pale "
            "birch cabinets with painted trim, unlabelled jars of dried herb "
            "in a glass-front dresser and a cream enamel range under a window "
            "of bare branches",
     "coz_c": "pale birch farm kitchen",
     "sup_a": "a scrubbed birch counter", "sup": "counter",
     # ⭐ CINCO trajes, com SILHUETA diferente — nao cinco cores do mesmo.
     "trajes": [
         ("%s knitted cardigan with wooden buttons over a plain dress",
          "knitted cardigan"),
         ("%s pinafore apron over a long-sleeved blouse",
          "pinafore apron"),
         ("%s wool waistcoat over a high-necked shirt",
          "wool waistcoat"),
         ("%s buttoned work dress with the sleeves turned back",
          "buttoned work dress"),
         ("%s folded headscarf tied behind over a knitted jumper",
          "folded headscarf"),
     ],
     "cores": ["ivory", "cornflower blue", "dusty rose", "moss green", "charcoal", "mustard"],
     "luz": "Flat bright light bouncing off the snow outside.",
     "luz_c": "flat snow-bright light",
     "audio": "a furnace kicking in, a clock ticking"},

    {"id": "tidewater", "selo": "N", "familia": "tidewater",
     "eua": True,
     "etnias": ["Black American"],
     "coz": "a Tidewater Virginia kitchen with whitewashed brick, a wide hearth "
            "kept swept, unlabelled jars of bark and dried root along a deep "
            "sill and a long-handled pot hanging by the fire",
     "coz_c": "whitewashed hearth kitchen",
     "sup_a": "a broad scrubbed oak table", "sup": "table",
     # ⭐ CINCO trajes, com SILHUETA diferente — nao cinco cores do mesmo.
     "trajes": [
         ("%s long wrapper dress tied at the hip",
          "wrapper dress"),
         ("%s wide-collared blouse over a long gathered skirt",
          "wide-collared blouse"),
         ("%s sleeveless linen shift with a tied head cloth",
          "tied head cloth"),
         ("%s buttoned bodice with a full apron over the skirt",
          "full apron"),
         ("%s knotted kerchief at the neck over a plain work dress",
          "knotted kerchief"),
     ],
     "cores": ["indigo", "ochre", "cream", "deep green", "brick red", "black"],
     "luz": "Soft daylight off the whitewash from a window at frame-right.",
     "luz_c": "soft whitewash daylight",
     "audio": "a fire settling, gulls far off"},

    {"id": "filipina", "selo": "N", "familia": "filipina",
     "eua": False,
     "etnias": ["Filipino American"],
     "coz": "a Filipino American kitchen with a covered outdoor prep area just "
            "beyond the door, bamboo shelving of unlabelled jars, bundles of "
            "dried leaves hanging from a hook and a clay pot on a gas ring",
     "coz_c": "bamboo-shelved kitchen",
     "sup_a": "a scrubbed hardwood counter", "sup": "counter",
     # ⭐ CINCO trajes, com SILHUETA diferente — nao cinco cores do mesmo.
     "trajes": [
         ("%s light embroidered blouse with sheer sleeves",
          "embroidered blouse"),
         ("%s wrapped cotton skirt with a fitted top",
          "wrapped skirt"),
         ("%s short-sleeved shift dress with a woven belt",
          "woven belt"),
         ("%s sleeveless linen top over a long printed skirt",
          "printed skirt"),
         ("%s buttoned camisa worn loose over cotton trousers",
          "loose camisa"),
     ],
     "cores": ["pale yellow", "sea green", "coral", "white", "indigo", "amber"],
     "luz": "Bright humid daylight through the open door.",
     "luz_c": "bright humid daylight",
     "audio": "rain on a metal roof, a rooster far off"},

    {"id": "levantina", "selo": "N", "familia": "levantina",
     "eua": False,
     "etnias": ["Middle Eastern American"],
     "coz": "a Levantine kitchen with a tiled splashback in blue and white, "
            "unlabelled glass jars of dried flowers and seed heads along an "
            "open shelf, a brass tray of small cups and a copper pot on a low "
            "flame",
     "coz_c": "blue-tiled Levantine kitchen",
     "sup_a": "a pale stone counter", "sup": "counter",
     # ⭐ CINCO trajes, com SILHUETA diferente — nao cinco cores do mesmo.
     "trajes": [
         ("%s long embroidered tunic over straight trousers",
          "embroidered tunic"),
         ("%s wrapped headscarf worn loose over a buttoned dress",
          "wrapped headscarf"),
         ("%s wide-sleeved robe belted at the waist",
          "belted robe"),
         ("%s fitted blouse under a long open sleeveless coat",
          "sleeveless coat"),
         ("%s printed shawl draped over a plain long dress",
          "draped shawl"),
     ],
     "cores": ["deep teal", "saffron", "burgundy", "cream", "olive", "midnight blue"],
     "luz": "Warm side light off the tile from a high window.",
     "luz_c": "warm tile-side light",
     "audio": "a copper pot simmering, a street far below"},
]

FAMILIAS_MUNDO = list(dict.fromkeys(m["familia"] for m in MUNDOS))

# ---------------------------------------------------------------------------
# ⭐⭐ O TOGGLE DE PELE — ORDEM DO ED, 2026-08-06
# ---------------------------------------------------------------------------
# Ele setou `pele clara` e recebeu ora REF clara, ora escura. O motivo: neste
# agente a etnia NAO vem da pagina, vem do MUNDO sorteado
# (`rng.choice(mundo["etnias"])`) — e o seletor de pele da UI, para motor que
# nao declara `PELE_TRAVAVEL`, so' TROCA DE PAGINA. Trocar a pagina aqui nao
# muda nada. O toggle estava inerte, e a palavra `pele` nao aparecia uma vez
# neste arquivo fora de um comentario.
#
# ⛔ A TRAVA ENTRA ANTES DO SORTEIO DA FAMILIA, nao depois na etnia. Filtrar so'
# a etnia deixaria o cenario, o traje, a luz e o audio do mundo errado — uma
# mulher branca numa cozinha do Caribe com jarros de casca de arvore. O eixo do
# BOTICA arrasta o mundo inteiro, entao a trava tem de agir no mundo.
#
# ⚠️ ONDE EU DECIDI, PARA VOCE PODER MOVER EM UMA LINHA: quatro etnias sao
# genuinamente limitrofes num toggle binario. Coloquei `Mexican American`,
# `Andean South American`, `Mediterranean` e `East Asian American` em CLARA, e
# `South Asian American` em ESCURA. Se discordar de alguma, e' mudar de lista.
PELE_TRAVAVEL = True


# ⛔⛔ A CLASSIFICACAO E' LISTA EXPLICITA, NUNCA "tudo que nao e' branco".
# Correcao de campo do operador em 2026-08-05, com print: no CLEAN V2 ele
# travou `escura` e recebeu um REF Asian American. **Para ele, escura = NEGRO.**
# ⚠️ Asiatico, latino, mediterraneo, andino e mestico nao sao nem clara nem
# escura — so' saem com a pele LIVRE.
# ⛔ MESMA LISTA DOS OUTROS MOTORES (cha, dupla, placa, trio). Eu tinha escrito
# uma tabela propria classificando Mexican/Mediterranean/Andean como clara e
# South Asian como escura — exatamente o erro que ele ja' havia corrigido, e
# classificacao divergente entre agentes e' o fragmento espelhado que a P9
# proibe. Copiado de `cha_short.py`, sem uma virgula de diferenca.
PELE_ETNIAS = {
    "escura": ("Black American",),
    "clara": ("white American",),
}


def _pele_de(etnia):
    """A pele da etnia pela lista explicita — ou None (neutra, so' no livre)."""
    for pele, ets in PELE_ETNIAS.items():
        if etnia in ets:
            return pele
    return None


def mundos_da_pele(pele):
    """Os mundos que COMPORTAM a pele pedida.

    ⛔ Cede em vez de derrubar: se a trava nao deixar mundo nenhum de pe,
    devolve a lista inteira. Botao que zera o sorteio e' botao que quebra o
    app, nao que muda a REF — licoes-de-construcao.
    """
    if pele not in ("clara", "escura"):
        return MUNDOS
    filtrados = [m for m in MUNDOS if any(_pele_de(e) == pele for e in m["etnias"])]
    return filtrados or MUNDOS


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
    {"id": "aveia", "nome": "oats",
     "img": "a small bowl of rolled oats"},
    {"id": "leite", "nome": "warm milk",
     "img": "a small jug of milk"},
    {"id": "beterraba", "nome": "beet powder",
     "img": "a shallow dish of deep red powder"},
    {"id": "caiena", "nome": "cayenne",
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
    {"idade": 29, "corpo": "slim with an hourglass figure and a narrow waist",
     "cabeca": "copper-red hair pinned back off her face",
     "marca": "a heavy dusting of freckles across her nose and clear skin"},
    {"idade": 34, "corpo": "toned and curvy, with a clearly defined waist",
     "cabeca": "long dark hair in a low twist",
     "marca": "high round cheekbones and lightly tanned even skin"},
    {"idade": 26, "corpo": "long-legged and slender, with a graceful neck and full shoulders",
     "cabeca": "honey-blonde hair braided over one shoulder",
     "marca": "pale green eyes, a light spray of freckles and a beauty mark above her lip"},
    {"idade": 31, "corpo": "shapely and strong, with toned arms and a small waist",
     "cabeca": "tight natural curls gathered high",
     "marca": "glowing deep brown skin and a wide bright smile"},
    {"idade": 37, "corpo": "slim-hipped and elegant, with a long line from neck to shoulder",
     "cabeca": "straight black hair parted in the middle",
     "marca": "full lips, a deep dimple in her left cheek and warm tanned skin"},
    {"idade": 28, "corpo": "athletic and curvy, with swimmer's shoulders and a narrow waist",
     "cabeca": "long braids gathered at the nape",
     "marca": "a small silver hoop in her left nostril and clear skin"},
    {"idade": 33, "corpo": "softly curved and full-figured, with a defined waist",
     "cabeca": "chestnut hair in a loose knot with strands escaping",
     "marca": "a dusting of freckles and a small crescent birthmark at her right temple"},
    {"idade": 25, "corpo": "trim and shapely, standing very straight",
     "cabeca": "dark hair in a high smooth bun",
     "marca": "eyes of two different colours, one green and one brown"},
    {"idade": 36, "corpo": "tall and statuesque, with a long waist",
     "cabeca": "auburn hair coiled and pinned at the back",
     "marca": "a bright silver streak at one temple and smooth clear skin"},
    {"idade": 30, "corpo": "petite and curvy, with a small frame and a defined waist",
     "cabeca": "black hair in a thick plait down her back",
     "marca": "smoothly tanned skin and a dark beauty spot high on her left cheekbone"},
    {"idade": 27, "corpo": "lean and toned, with a flat stomach and long arms",
     "cabeca": "wavy caramel hair tucked behind her ears",
     "marca": "a deep dimple in one cheek that shows when she smiles"},
    {"idade": 38, "corpo": "full-figured and confident, with rounded shoulders and a narrow waist",
     "cabeca": "silver-free dark hair wound into a bun",
     "marca": "arched brows over wide dark eyes and clear skin"},
    # + 2026-08-05 — o operador leu tres lotes e reclamou da repeticao de
    # pessoas e roupa. Estas dez variam CORPO e FORMATO DE CABECA, nao so' cor.
    {"idade": 32, "corpo": "slim and supple, with a dancer's line",
     "cabeca": "loose dark curls falling past her shoulders",
     "marca": "a small dark mole just above her lip and clear skin"},
    {"idade": 24, "corpo": "compact and shapely, with strong shoulders and a small waist",
     "cabeca": "jet-black hair in a blunt chin-length bob",
     "marca": "wide-set almond eyes and a dimple in her chin"},
    {"idade": 35, "corpo": "tall and slim with an hourglass line",
     "cabeca": "tight coils cropped close to the head",
     "marca": "sharply cut cheekbones and a small gold stud in one nostril"},
    {"idade": 29, "corpo": "curvy and athletic, with a long neck and a defined waist",
     "cabeca": "dark hair with a deep side part falling in heavy waves",
     "marca": "a beauty spot at the outer corner of her right eye"},
    {"idade": 27, "corpo": "slender and fine-boned, with elegant posture",
     "cabeca": "ash-brown hair twisted into a loose topknot",
     "marca": "pale grey eyes and a beauty mark just above her left brow"},
    {"idade": 33, "corpo": "toned and full-figured, with a small waist and straight back",
     "cabeca": "thick black hair coiled into two low buns",
     "marca": "full arched brows and a small beauty mark on her jawline"},
    {"idade": 26, "corpo": "long-limbed and shapely, with a narrow waist",
     "cabeca": "waist-length straight black hair left loose",
     "marca": "a dimple that shows in one cheek only"},
    {"idade": 31, "corpo": "trim and athletic, with a flat stomach and square shoulders",
     "cabeca": "copper braids wrapped into a crown around her head",
     "marca": "a scatter of dark freckles across both cheeks"},
    {"idade": 37, "corpo": "softly curvy, with a full figure and a defined waist",
     "cabeca": "glossy black hair in a low ponytail",
     "marca": "a small raised birthmark on her right temple"},
    {"idade": 28, "corpo": "slim and long-waisted, with a very straight back",
     "cabeca": "sandy hair in a thick fishtail braid",
     "marca": "a slight overbite that shows when she talks"},

    # ⭐⭐ + 2026-08-13 — CATORZE ENTRADAS NOVAS, de 22 para 36. Ordem do
    # operador: *"aumente o pool de opcoes substancialmente, tambem dos
    # ambientes"*.
    # ⛔ Cada uma varia CORPO, CABECA e MARCA juntos, como as vinte e duas de
    # cima: duas mulheres de cabelo diferente e mesmo porte leem como a mesma
    # pessoa, e foi essa a licao que criou o `medir_personagens.py`.
    # ⛔ Zero adjetivo de etnia — quem injeta e' a montagem, a partir do MUNDO.
    # ⛔ Zero oculos, zero grisalho, zero pele castigada (LEI DO REF).
    #
    # ⛔⛔ E CINCO ENTRADAS ANTIGAS FORAM REESCRITAS NO MESMO DIA. O que saiu,
    # medido: `fine pale scar through one eyebrow`, `gap between her front
    # teeth`, `faint pale scar on her chin`, `thin scar along her jawline` e
    # `faint round mark between her brows` — este ultimo porque `mark between
    # the brows` e' o que o gerador resolve como VINCO, nao como pinta.
    # ⚠️ NADA foi apagado sem substituicao: cada uma ganhou ancora SAUDAVEL no
    # lugar (`silver streak`, `dimple`, `beauty mark`), senao o eixo `ancora`
    # cai junto com a cicatriz — erro ja' cometido no PLACA 16 em 12/08.
    {"idade": 26, "corpo": "tall and athletic, with a long waist and narrow hips",
     "cabeca": "cinnamon-red hair in a thick side braid",
     "marca": "a light spray of freckles over her cheekbones and amber eyes"},
    {"idade": 24, "corpo": "shapely and lithe, with a very small waist",
     "cabeca": "espresso-dark hair in a high twisted knot",
     "marca": "a deep dimple in her right cheek and long dark lashes"},
    {"idade": 29, "corpo": "long-legged and toned, with square shoulders and a flat stomach",
     "cabeca": "wheat-blonde hair swept into a low side wave",
     "marca": "a small gold hoop in one ear and lightly tanned even skin"},
    {"idade": 25, "corpo": "petite and curvy, with full shoulders and a defined waist",
     "cabeca": "fine cornrows finished in a low gathered bun",
     "marca": "a beauty mark at the outer corner of her left eye"},
    {"idade": 32, "corpo": "statuesque and strong, with a narrow waist and long arms",
     "cabeca": "burnt-copper hair falling in heavy waves to the ribs",
     "marca": "wide green eyes and a dense scatter of freckles"},
    {"idade": 28, "corpo": "slim and supple, with a very long neck",
     "cabeca": "blue-black hair in a blunt chin-length cut with a deep fringe",
     "marca": "a silver streak at her right temple and dark almond eyes"},
    {"idade": 35, "corpo": "curvy and full-figured, with rounded shoulders and a small waist",
     "cabeca": "honey-brown hair coiled into a low chignon",
     "marca": "warm hazel eyes and a beauty mark below her right cheekbone"},
    {"idade": 27, "corpo": "trim and dancer-like, with a very straight back",
     "cabeca": "platinum hair in a sleek high ponytail",
     "marca": "ice-grey eyes and a small stud in one nostril"},
    {"idade": 31, "corpo": "athletic and shapely, with broad shoulders and a flat stomach",
     "cabeca": "dark coils cut into a rounded crop",
     "marca": "sculpted cheekbones and a gold hoop in one ear"},
    {"idade": 24, "corpo": "slender and fine-boned, with a small waist and long legs",
     "cabeca": "ginger hair in two loose braids",
     "marca": "heavy freckling across the nose and pale green eyes"},
    {"idade": 33, "corpo": "tall and long-limbed, with a defined waist",
     "cabeca": "chestnut hair wound into a high crown braid",
     "marca": "a beauty mark high on her left temple and full lips"},
    {"idade": 26, "corpo": "compact and toned, with strong shoulders and a narrow waist",
     "cabeca": "jet-black hair in a sharp centre part falling past the collarbone",
     "marca": "wide dark eyes and a dimple in her chin"},
    {"idade": 30, "corpo": "softly curvy, with a small frame and a very defined waist",
     "cabeca": "caramel hair in a loose fishtail braid over one shoulder",
     "marca": "a scatter of freckles across both cheeks and grey-green eyes"},
    {"idade": 38, "corpo": "full-figured and upright, with a long waist and full shoulders",
     "cabeca": "deep auburn hair pinned into a soft roll",
     "marca": "a small crescent beauty mark beside her right eye"},
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
# ⛔⛔ POOL SANEADO E AMPLIADO EM 2026-08-13. Ordem do operador: *"melhore a
# aparencia e shape desses homens"* / *"aumente o pool de opcoes
# substancialmente, tambem dos ambientes"*.
#
# ⚠️ E' A MESMA ORDEM QUE JA' TINHA SIDO DADA NO PLACA 16 EM 12/08, com o lote na
# mao — *"esses caras tao parecendo mendigo"*. La' o pool foi reescrito e AQUI
# nao: este arquivo continuava com as 22 originais, e catorze delas carregavam
# marcador de DANO. Medido, entrada por entrada:
#     `weathered` / `sun-weathered` / `deeply lined` / `deep tan line`
#     `ruddy` · `gaunt` (2x) · `hollow cheeks`
#     `scar` (2x) · `chipped front tooth` · `gap between his front teeth`
#     `raised mole` · `large mole` · `bulbous nose` · `squint` · `deep-set eyes`
# Pele castigada, cicatriz, dente faltando e verruga nao sao "marca distintiva":
# sao DANO. Num homem de 60, dano renderiza exatamente como ele descreveu.
#
# ⭐ A REGRA E' A DO REPO: **DISTINTIVO, NUNCA DETERIORADO**. A ancora e' uma
# feicao MEMORAVEL num rosto SAUDAVEL — `cleft`, `dimple`, `beauty mark`,
# `silver streak`, `hoop`, `stud`, `patch of white`. Nenhuma delas e' avaria, e
# todas continuam contando no eixo `ancora` do `medir_personagens.py`.
# ⛔ E A PELE NAO PODE FICAR VAZIA NO LUGAR: tirar `weathered` sem por
# `smooth-skinned`/`tanned`/`freckled`/`laugh lines` ZERA o eixo `pele` — foi
# exatamente o erro cometido na primeira versao do pool do PLACA 16.
#
# ⛔⛔ NENHUMA PALAVRA DE APROVACAO: sairam `strong square jaw` e `strong cleft
# chin`, e nada de `handsome`, `chiseled`, `rugged` entrou no lugar. Elogio no
# prompt puxa o rosto para a media do banco de imagem — o mesmo mecanismo pelo
# qual `not a celebrity` invoca a celebridade.
# ⚠️ A ETNIA NAO ENTRA AQUI: vem do MUNDO (`spec["etnia"]`), igual a' dela.
# ⚠️ AS IDADES E AS PESSOAS NAO MUDARAM nas 22 herdadas — mexeu-se so' no que
# era avaria. Quem trocar o numero aqui esta' mexendo noutra decisao.
HOMENS = [
    {"id": "grisalho_barbudo", "idade": 58,
     "marca": "a heavy-set build, thick silver hair and a short grey beard, "
              "smooth-skinned, with a silver streak through one eyebrow",
     "roupa": "a plain navy work shirt"},
    {"id": "careca_bigode", "idade": 63,
     "marca": "a stocky build, a bald crown with white hair at the sides and a "
              "thick moustache, lightly tanned, with a beauty mark high on one "
              "cheek",
     "roupa": "a heather-grey pocket tee"},
    {"id": "cabelo_farto", "idade": 46,
     "marca": "a tall lean frame, a full head of dark hair going grey at the "
              "temples, clean-shaven, with a deep cleft in his chin",
     "roupa": "an olive canvas shirt with the sleeves rolled"},
    {"id": "sardas_ruivo", "idade": 41,
     "marca": "a wiry build, coppery hair and heavy freckling across the nose, "
              "with a small gold hoop in one ear",
     "roupa": "a faded red flannel shirt"},
    {"id": "fade_grisalho", "idade": 55,
     "marca": "a broad-shouldered build, a close grey fade and a neat chinstrap "
              "beard, smooth-skinned, with a small gold stud in one ear",
     "roupa": "a slate-blue polo shirt"},
    {"id": "locs_oculos", "idade": 49,
     "marca": "a solid build, salt-and-pepper locs gathered back, wire-rimmed "
              "glasses and a beauty mark beside his right eye",
     "roupa": "a charcoal henley with the sleeves pushed up"},
    {"id": "corte_militar", "idade": 52,
     "marca": "a thickset build, an iron-grey brush cut, lightly tanned, with "
              "heavy level brows and a cleft in his chin, wearing plain "
              "steel-framed glasses",
     "roupa": "a mustard snap-button shirt"},
    {"id": "cavanhaque", "idade": 60,
     "marca": "a barrel-chested build, a shaved head and a neat white goatee, "
              "with a white streak in one eyebrow",
     "roupa": "a cream short-sleeve camp shirt"},
    {"id": "onda_longa", "idade": 44,
     "marca": "a slim build, wavy dark hair grown a little long at the collar, "
              "clean-shaven, with a deep dimple in his left cheek",
     "roupa": "a forest-green work shirt"},
    {"id": "sobrancelha_oculos", "idade": 66,
     "marca": "a slender upright build, white hair combed back, heavy "
              "black-framed glasses, smooth-skinned, with a beauty mark at his "
              "left temple",
     "roupa": "a blue-and-white checked shirt"},
    {"id": "queixo_fendido", "idade": 47,
     "marca": "a compact build, sandy hair going grey at the sides, tanned, "
              "with a deep cleft chin",
     "roupa": "a rust-red pocket tee"},
    {"id": "afro_curto", "idade": 54,
     "marca": "a burly build, a short grey afro and a broad open face, with a "
              "small birthmark high on one cheek",
     "roupa": "a sand-coloured linen shirt"},
    # + 2026-08-05, mesma ordem do operador. Porte, cabeca e pelo facial variam
    # juntos: dois homens de cabelo diferente e mesmo porte leem como o mesmo.
    {"id": "bigode_farto", "idade": 57,
     "marca": "a lean upright frame, dark hair combed to one side and a thick "
              "moustache, with deep laugh lines around the eyes",
     "roupa": "a striped short-sleeve shirt"},
    {"id": "calvo_barba", "idade": 51,
     "marca": "a heavy build, a shaved head and a full salt-and-pepper beard, "
              "smooth-skinned, with a broad flat nose",
     "roupa": "a denim work shirt"},
    {"id": "branco_liso", "idade": 62,
     "marca": "a narrow build, straight white hair falling over the forehead, "
              "smooth-skinned, with a cleft chin",
     "roupa": "a pale blue oxford shirt"},
    {"id": "locs_curtas", "idade": 45,
     "marca": "a stocky athletic build, short twisted locs and a trimmed "
              "goatee, with a patch of white above one temple",
     "roupa": "a burgundy polo shirt"},
    {"id": "sobrancelha_farta", "idade": 59,
     "marca": "a solid build, thinning grey hair and very heavy level "
              "eyebrows, freckled across the nose, with a beauty mark near his "
              "jaw",
     "roupa": "a khaki utility shirt"},
    {"id": "queimado_sol", "idade": 48,
     "marca": "a rangy build, sun-bleached brown hair, lightly tanned, with "
              "laugh lines at the eyes and a dimple in one cheek",
     "roupa": "a faded teal work shirt"},
    {"id": "cavanhaque_branco", "idade": 65,
     "marca": "a spare frame, close-cropped white hair and a white goatee, "
              "smooth-skinned, with prominent ears",
     "roupa": "a grey chambray shirt"},
    {"id": "cacheado_grisalho", "idade": 43,
     "marca": "a broad build, dense curly hair going grey at the temples, "
              "clean-shaven and smooth-skinned, with a deep dimple in one "
              "cheek",
     "roupa": "a black crew-neck tee"},
    {"id": "bochechudo", "idade": 56,
     "marca": "a round-faced heavy build, dark hair receding at the temples "
              "and full cheeks, with a dimpled chin",
     "roupa": "a plaid flannel shirt"},
    {"id": "magro_alto", "idade": 50,
     "marca": "a very tall lean frame, iron-grey hair cropped short and a long "
              "straight nose, lightly tanned, with a cleft chin",
     "roupa": "a white undershirt beneath an open work shirt"},

    # ⭐⭐ + 2026-08-13 — SEIS ENTRADAS NOVAS, de 22 para 28, mesma ordem do
    # operador (*"aumente o pool de opcoes substancialmente"*).
    # ⛔ Todas 50+, no padrao que o PLACA 16 fixou em 12/08: nenhum marcador de
    # dano, nenhuma palavra de aprovacao, nenhuma cor de pele.
    # ⚠️ QUATRO DELAS TRAZEM OCULOS de proposito. O eixo media 2 em 22 (9,1%),
    # que e' rotacao morta num medidor que cobra 25-30%; com estas seis mais os
    # oculos que voltaram ao `corte_militar` ele fecha em 7 de 28.
    # ⭐ Cada uma varia PORTE, CABECA e MARCA juntas — duas entradas de cabelo
    # diferente e mesmo corpo leem como o mesmo homem.
    {"id": "prata_penteado_oculos", "idade": 61,
     "marca": "a broad solid build, a full head of silver hair combed straight "
              "back, clean-shaven and smooth-skinned, wearing thin gold "
              "wire-rimmed glasses, with a shallow cleft chin",
     "roupa": "a slate-blue linen shirt"},
    {"id": "barba_branca_cheia", "idade": 64,
     "marca": "a tall broad-shouldered build, thick white hair and a full beard "
              "kept neatly shaped, with laugh lines at the eyes and a dimple "
              "beside his mouth",
     "roupa": "a charcoal cardigan over a plain white tee"},
    {"id": "twists_prata_oculos", "idade": 57,
     "marca": "a lean upright build, short silver twists kept close and a "
              "close-trimmed beard, smooth-skinned, with a beauty mark below "
              "one eye, wearing slim half-rim glasses",
     "roupa": "a stone-grey henley with the sleeves pushed up"},
    {"id": "bigode_chevron", "idade": 59,
     "marca": "a compact sturdy build, steel-grey hair parted low and a full "
              "chevron moustache kept trimmed, freckled across the cheeks, "
              "with a cleft in his chin",
     "roupa": "a warm grey flannel shirt"},
    {"id": "careca_oculos_pesados", "idade": 66,
     "marca": "a heavy square build, a cleanly shaved crown and no beard at "
              "all, lightly tanned, wearing heavy dark-rimmed glasses, with a "
              "beauty mark high on one cheekbone",
     "roupa": "a dark olive crewneck sweater"},
    {"id": "mecha_branca_lateral", "idade": 53,
     "marca": "a tall trim build, dark hair silvering at the sides with a "
              "patch of white above one temple, clean-shaven and "
              "smooth-skinned, wearing rimless reading glasses",
     "roupa": "a pressed light blue shirt"},
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
# ⛔⛔ REESTRUTURADO EM 2026-08-05 — A CENA 1 VIROU TRES BEATS COMPOSTOS.
# O operador comparou o que o agente gerou com o que ele queria:
#
#   gerado: "The chemist kept selling us refills while my husband's weiner
#            stayed dead, until mucuna, the famous velvet bean of the tropics
#            and a gelatin trick."
#   ele:    "My husband's weiner stayed dead, things changed when i discovered
#            mucuna, the famous velvet bean of the tropics and a secret gelatin
#            trick."
#
# ⭐ TRES DIFERENCAS, e nenhuma e' de comprimento:
#   1. O PROBLEMA ABRE. O vilao ocupava a abertura e empurrava o problema para
#      o meio — e a abertura pertence ao que esta' em jogo.
#   2. `until {r}` NAO TEM VERBO. "until mucuna, the famous velvet bean" promete
#      uma virada e entrega um substantivo: a frase fica truncada. A virada
#      precisa de verbo — "Things changed when I discovered".
#   3. `secret` entra como ADJETIVO do mecanismo (`a secret gelatin trick`).
#      ⚠️ De proposito DIFERENTE da cena 2, que usa `and a secret: the gelatin
#      trick` — a mesma construcao duas vezes em 24 segundos vira bordao.
#
# ⛔ O VILAO SAIU DO ESCOPO DA CENA 1, por ordem expressa dele. Consequencia
# registrada: a farmacia so' existia nessas iscas, entao ela sai do video
# inteiro. A lente BO3 foi aposentada junto — regra que cobra o que o operador
# mandou tirar e' regra que reprova a producao.
#
# ⛔⛔ E O INGLES DO EXEMPLO DELE NAO FOI COPIADO — ordem dele: *"tomar cuidado
# com o efeito maritaca seu: minha coesao de escrita do ingles no exemplo ta'
# errada, ajustar isso"*. A frase dele e' comma splice com `i` minusculo
# ("stayed dead, things changed when i discovered"). Aqui o problema fecha em
# PONTO, a virada abre em maiuscula, e o aposto do raro leva virgula dos DOIS
# lados, como manda a gramatica. O que se copia do exemplo e' a FORMA (§26).
#
# ⭐ POOL COMPOSTA, nao lista chapada: 16 problemas x 12 viradas x 6 fechos =
# 1152 aberturas distintas antes de multiplicar pelos 9 raros. O operador pediu
# "um pool rico com variacoes do sentido", e variacao de sentido se consegue
# combinando beats, nao repetindo a mesma frase com sinonimos.
# ⛔⛔ ENCURTADAS DE 7-11 PARA 4-6 PALAVRAS EM 2026-08-05 — segunda evidencia
# de corte no mesmo dia. O operador mandou o render:
#   "My husband stopped reaching for me, and his John-son was why. Things
#    changed when I discovered fenugreek, ... and a secret gelatin trick."
# ...e a fala CORTOU em `secret`. A linha tinha 28 palavras — exatamente o
# teto que eu tinha acabado de definir como seguro.
#
# ⭐ A ARITMETICA QUE EU NAO TINHA FEITO: o raro mais longo custa 10 palavras
# (o aposto e' obrigatorio, BO8), a virada mais curta 5 e o fecho mais curto
# 5. Sao 20 palavras COMPROMETIDAS antes de a abertura dizer qualquer coisa.
# Abertura de 11 palavras nao cabia em teto nenhum que respeitasse o relogio.
# ⛔ Ordem dele: *"usar formas de escrever sentencas mais curtas que fala do
# John-son do marido nao funcionar"*. Todas dizem QUEM (`my husband`) e O QUE
# (`{o}`) em 4-6 palavras, que e' o minimo que a BO9 aceita — e a variacao
# mora no VERBO da falha, nao em adornos.
PROBLEMAS = [
    "My husband's {o} was dead",
    "My husband's {o} had quit",
    "My husband's {o} stopped working",
    "My husband's {o} never worked",
    "My husband's {o} gave up",
    "My husband's {o} was finished",
    "My husband's {o} went dead",
    "My husband's {o} was long gone",
    "My husband's {o} stayed down",
    "My husband's {o} had shut down",
    "My husband's {o} slept for years",
    "My husband's {o} quit on him",
    "My husband's {o} had gone silent",
    "My husband's {o} stopped for good",
    "My husband's {o} was done",
    "My man's {o} was dead",
    "My man's {o} had quit",
    "Nothing woke my husband's {o}",
    "For years my husband's {o} failed",
    "My husband's {o} embarrassed him",
    # + 2026-08-05 — todas em 4-6 palavras, com QUEM e O QUE, variando o verbo da falha
    "My husband's {o} was asleep",
    "My husband's {o} had failed",
    "My husband's {o} would not answer",
    "My husband's {o} had gone cold",
    "My husband's {o} was over",
    "My husband's {o} had checked out",
    "My husband's {o} stayed asleep",
    "My husband's {o} had no life left",
    "My husband's {o} let him down",
    "My husband's {o} was beaten",
    "My man's {o} stopped answering",
    "My husband's {o} had retired early",
]

VIRADAS = [
    "Things changed when I discovered",
    "That changed the day I found",
    "That turned around once I found",
    "Everything shifted when I came across",
    "That ended the week I found",
    # ⛔ era "It came back after I started using" e o `medir_deiticos` acusou:
    # pronome nu como sujeito de estado do corpo e' a familia (B), a mesma
    # que o operador reprovou no RECEITA. Pool novo reintroduz vicio velho.
    "He changed the week I found",
    "What turned it around was",
    "A neighbour told me about",
    "It all changed once my sister sent me",
    "That was over the day I read about",
    "Everything changed after I got",
    "The turn came when I finally found",
    # + 2026-08-05 — viradas com VERBO — nunca `until {ingrediente}`, que fica truncado
    "That changed the month I found",
    "Everything turned around after I found",
    "It changed for good when I found",
    "That stopped the day I tried",
    "What finally worked was",
    "It all changed when a friend gave me",
    "That was over once I started using",
    "The change came the week I found",
    "It turned around when I switched to",
    "What did it for him was",
    "That ended after I brought home",
    "Everything was different once I had",
]

# ⚠️ O fecho vem depois do aposto do raro, entao a virgula ANTES dele mora na
# montagem (`%s, %s`), nunca aqui — senao o aposto fica sem fechar.
FECHOS = [
    "and a secret gelatin trick",
    "plus a secret gelatin trick",
    "and one secret gelatin trick",
    "and a secret gelatin trick on top",
    "and a gelatin trick nobody sells",
    "and the secret gelatin trick with it",
    "and a gelatin trick I keep to myself",
    "and one gelatin trick nobody talks about",
    "and a secret gelatin trick my grandmother used",
    # ⛔ Era "and a quiet gelatin trick" — Ed, 2026-08-06: *"que adjetivo sem
    # sentido e nonsense e esse?"*. Truque silencioso nao significa nada e ainda
    # dilui o nome do mecanismo. O literal e' intocavel; o que varia tem de
    # dizer algo de ACESSO ou ORIGEM, como o resto do pool ja fazia.
    # ⚠️ O `_adjetivo_do_mecanismo` em short_comum agora reprova isso nos 18.
    "and a gelatin trick nobody wrote down",
    "and one gelatin trick from home",
    "plus the gelatin trick that made it work",
    "and a gelatin trick nobody mentions",
    "and one gelatin trick that never left the house",
    "and the gelatin trick that finished it",
    "and a gelatin trick kept in the family",
    "plus one gelatin trick of my own",
    "and a gelatin trick no shop carries",
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
# ⛔⛔ POOL APOSENTADO EM 2026-08-05 — NAO E' MAIS SORTEADO POR NINGUEM.
# O operador mandou tirar este beat da cena 1 porque ele era o que estourava o
# teto e cortava a fala. As dez entradas ficam AQUI, e nao apagadas, por dois
# motivos: e' copy curada que pode voltar se a cena 1 ganhar folego, e apagar
# copy aprovada sem registro e' como o repertorio some sem ninguem notar.
# ⚠️ O vilao continua no video — ele desceu para dentro das ISCAS, em seis das
# vinte e duas entradas. A lente BO3 passou a cobrar isso no POOL, e nao no
# sorteio, porque o proprio exemplo que o operador escreveu nao tem vilao.
VILOES_APOSENTADO = [
    "The pharmacy industry sells you pills and keeps the kitchen mix off the label.",
    "No drug company makes a cent off a kitchen shelf.",
    "The chemists keep the two-dollar mix off the shelf; they cannot bill you for it.",
    "The chemists would rather sell you the box behind the counter.",
    "Doctors do not hand the cheap recipe out, and not because it fails.",
    "The drug companies advertise the pill and never the mix that hardens him.",
    "The pill companies need you buying the little blue box instead.",
    "My grandmother knew this recipe. Then the drug industry put a price on it.",
    "The pharmacy sells you a monthly refill and hides the mix that costs pennies.",
    "Every pharmacy ad sells the expensive pill and buries the cheap recipe.",
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
# ⛔⛔ O VASO SAIU DA FALA EM 2026-08-05. Toda entrada terminava em `into
# the {v}` e o operador reescreveu o take sem isso.
# ⚠️ A razao e' economia pura: o vaso ESTA' NO QUADRO — a mao dela esta'
# fechada nele, o audio traz o som dele, e a IMAGE o descreve. Dizer em voz
# alta o que a imagem ja' mostra gasta 3 a 4 palavras num take de 8s e nao
# acrescenta nada que o espectador nao esteja vendo.
# ⭐ `{v}` continua no dict do metodo e no prompt de IMAGE. So' saiu da FALA.
# ⛔⛔ A GELATINA SAIU DA LISTA DE INGREDIENTES EM 2026-08-05, e a mudanca e'
# do operador: *"Fresh ginger and epimedium and a secret: the gelatin trick"*.
# ⭐ E' melhor do que estava, por dois motivos que valem registrar:
#   1. ECONOMIA — a receita falada listava `gelatin` e depois a ancora dizia
#      `gelatin trick`. A palavra aparecia duas vezes num take de 8s.
#   2. CURIOSIDADE — listar a gelatina COMO INGREDIENTE e depois chamar o
#      conjunto de `gelatin trick` entrega o mecanismo. Deixando-a fora da
#      lista, o que o espectador VE e' uma receita incompleta e o que falta
#      tem nome. E' a lacuna que o comentario compra — a mesma funcao da
#      opcao `c` de 2026-08-04, agora em 6 palavras em vez de 7 e sem uma
#      sentenca propria.
# ⚠️ `gelatin` continua sendo dito (dentro de `gelatin trick`) e a gelatina
# continua NO QUADRO e no prompt de IMAGE. So' saiu da ENUMERACAO falada.
# ⛔⛔ A GELATINA SAIU DA LISTA DE INGREDIENTES EM 2026-08-05, ordem do
# operador: *"Fresh ginger and epimedium and a secret: the gelatin trick"*.
# ⭐ E' melhor do que estava, por dois motivos:
#   1. ECONOMIA — a receita listava `gelatin` e a ancora repetia `gelatin
#      trick`. A palavra saia duas vezes num take de 8s.
#   2. CURIOSIDADE — listar a gelatina e depois chamar o conjunto de `gelatin
#      trick` ENTREGA o mecanismo. Fora da lista, o espectador ve uma receita
#      incompleta e o que falta tem nome. E' a lacuna que o comentario compra.
# ⚠️ `gelatin` continua sendo dito (dentro de `gelatin trick`) e a gelatina
# continua no QUADRO e no prompt de IMAGE. So' saiu da enumeracao falada.
#
# ⛔⛔ E NENHUMA ENTRADA COMECA COM ADJETIVO — licao paga no primeiro render.
# A primeira versao tinha `Fresh {c} and {r}` e o sorteio devolveu
# **`Fresh fresh ginger and maca root`**, porque `fresh ginger` JA' e' o nome
# do ingrediente no pool COMUNS. Template que qualifica um slot preenchido
# por outro pool duplica quando os dois carregam a mesma palavra — e nenhum
# linter pega isso, porque a frase e' gramatical. Achado LENDO a saida (§19).
# ⛔⛔ QUATRO COPIAS DE `{c} and {r}` FORAM REMOVIDAS — 2026-08-08. A entrada
# aparecia CINCO vezes: com isso ela tinha cinco vezes a chance das outras e
# ocupava quatro slots que deviam ser repertorio novo.
# ⚠️ Duplicata nao quebra nada, e por isso e' cara: o autoteste ja' a
# reportava (`pool RECEITAS tem entrada REPETIDA`) e o motor seguia gerando.
# O sintoma so' aparece no LOTE, como 'esses videos parecem iguais'.
RECEITAS = [
    "{c} and {r}",
    "{c} with {r}",
    "{c}, {r}",
    "a little {c} and {r}",
    "just {c} and {r}",
    "{c}, plus {r}",
    "some {c} and {r}",
    # + 2026-08-05 — so' os ingredientes VISIVEIS — a gelatina fica de fora, e' o segredo
    "{c} and {r} together",
    "{c}, then {r}",
    # ⛔ NAO ACRESCENTAR RECEITA QUE SE AUTO-FECHA. Aqui esteve `{c} and {r},
    # nothing more` e o render saiu **"Turmeric and sarsaparilla, NOTHING MORE
    # AND one thing I keep back: the gelatin trick"** — a receita declarava a
    # lista encerrada e a clausula do segredo emendava mesmo assim.
    # ⚠️ A receita e' uma lista ABERTA por construcao: a ancora SEMPRE cola
    # `and <segredo>: the gelatin trick` no fim dela. Nenhum linter pega isso,
    # porque as duas metades sao gramaticais — so' a leitura do render pega.
    "two things: {c} and {r}",
    "{c} first, then {r}",
    "{c} mixed with {r}",
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
# ⛔⛔ REESCRITO EM 2026-08-05 — A CLAUSULA DE RETENCAO SAIU.
# Ordem do operador lendo o TAKE 02: *"retirar 'There's one step I'm not
# showing here.' esse bullet copy falada nao e' relevante o suficiente pra
# ocupar espaco precioso de tempo"*. Eram 7 palavras num take de 8s.
#
# ⚠️ ISTO REVERTE A OPCAO `c` QUE ELE MESMO ESCOLHEU EM 2026-08-04, e a
# consequencia esta' registrada aqui de proposito: sem o passo retido, a
# cena 2 passa a EQUIPARAR a receita visivel ao mecanismo — que e' o que
# ele tinha alertado (*"pode matar a curiosidade"*). Ele viu os renders e
# decidiu que as 7 palavras custam mais do que a lacuna compra. A lente
# BO15 continua barrando a forma pior (equiparar E emendar o beneficio na
# MESMA sentenca), que e' o caso que entrega tudo de uma vez.
# ⛔⛔ REESCRITO 2026-08-05 — A ANCORA DEIXOU DE SER SENTENCA E VIROU CLAUSULA.
# Forma do operador: *"Fresh ginger and epimedium AND A SECRET: the gelatin
# trick"*. Antes eram duas sentencas (`... into the mortar. That's the gelatin
# trick.`); agora e' uma so'.
# ⭐ E isto RECUPERA a curiosidade que a versao anterior tinha matado. Em
# 2026-08-04 ele mandou tirar `There's one step I'm not showing here` por
# custar 7 palavras, e o que sobrou (`That's the gelatin trick`) EQUIPARAVA a
# receita ao mecanismo — o risco que ele mesmo tinha apontado. `and a secret:`
# custa 3 palavras e faz o mesmo trabalho da retencao: a receita visivel esta'
# incompleta, e o que falta tem nome.
ANCORAS = [
    "%s and a secret: the gelatin trick.",
    "%s and one secret: the gelatin trick.",
    "%s plus a secret — the gelatin trick.",
    "%s and the one secret: the gelatin trick.",
    "%s and one thing I keep back: the gelatin trick.",
    "%s and a secret nobody sells: the gelatin trick.",
    "%s and my grandmother's secret: the gelatin trick.",
    "%s and one more thing: the gelatin trick.",
    # + 2026-08-05 — clausula, nunca sentenca propria — e o mecanismo e' NOMEADO, nao entregue
    "%s and one thing more: the gelatin trick.",
    "%s and the part I hold back: the gelatin trick.",
    "%s and what nobody sells: the gelatin trick.",
    "%s and a step I keep: the gelatin trick.",
    "%s and my own secret: the gelatin trick.",
    "%s and one last thing: the gelatin trick.",
    "%s and the missing piece: the gelatin trick.",
    "%s and a trick from home: the gelatin trick.",
    "%s and something I do not show: the gelatin trick.",
    "%s and the step nobody prints: the gelatin trick.",
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
    # + 2026-08-05 — as seis abaixo sao as CURTAS, no registro que o operador
    # escreveu a mao ("Your wife will be surprised with your John-son"). Com o
    # vaso fora da receita, a cena 2 tem folga para respirar em vez de correr.
    "Your wife will be surprised with your {o}.",
    "Your wife will not believe your {o}.",
    "She will notice your {o} first.",
    "Your wife will talk about your {o}.",
    "She will feel your {o} before she asks.",
    "Your wife will want your {o} again.",
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
    # + 2026-08-05 — toda promessa nomeia o ORGAO e traz ELA — reacao dela e' prova, auto-relato e' alegacao
    "Your wife will feel your {o} that same night.",
    "She will reach for your {o} first.",
    "Your wife will not let your {o} rest.",
    "She stops pretending, and your {o} is why.",
    "Your wife will ask what happened to your {o}.",
    "She will notice your {o} before the coffee.",
    "Your {o} answers, and she stops asking.",
    "She will hold on to your {o} again.",
    "Your wife wakes to your {o}, not to the alarm.",
    "She will want your {o} in the morning.",
    "Your {o} shows up, and your wife notices.",
    "She stops sleeping turned away, and your {o} is why.",
    "Your wife will be the one reaching, and your {o} is why.",
    "She looks at your {o} the way she used to.",
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
    # + 2026-08-05 — o USO nomeia o orgao — sem ele o espectador nao sabe para que serve
    "Drink it before bed and your {o} feels it by morning.",
    "One glass at night, and your {o} is what wakes.",
    "Take it every morning and your {o} does the rest.",
    "Drink it warm and your {o} answers within the week.",
    "A glass a day, and your {o} stops letting him down.",
    "Drink this daily and your {o} comes back on its own.",
    "One glass before bed, and your {o} does not go quiet.",
    "Drink it every morning and your {o} holds all night.",
    "Take a glass at night and your {o} shows up for her.",
    "One glass, every single day, and your {o} does the talking.",
    "Drink it first thing and your {o} follows within days.",
    "A glass each night, and your {o} stops going missing.",
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
    # + 2026-08-05 — sintagma NOMINAL curto: e' o que o CTA promete no DM.
    # ⚠️ Tres das minhas primeiras entradas aqui (`the exact recipe`, `the
    # complete recipe`, `the recipe and the doses`) JA' EXISTIAM nas linhas
    # acima, e a duplicata passou despercebida porque o bloco antigo tem varias
    # entradas por linha. Duplicata dobra em silencio a chance da linha e ocupa
    # um slot que devia ser repertorio novo — agora ha' trava no autoteste.
    "the full measurements",
    "the written recipe",
    "the exact steps",
    "every step of it",
    "the recipe in full",
    "the missing step",
    "the whole method",
    "the recipe and the timing",
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
    # + 2026-08-05 — o gate e' o beat que cede espaco quando o teto aperta
    "Follow me first, or your comment will not reach me.",
    "You have to follow me, or I will not find you.",
    "Follow me before you comment, or I cannot send it.",
    "Follow first, otherwise I have no way to answer.",
    "I can only reply if you are following me.",
    "Follow me, or your comment gets lost in the pile.",
    "Follow me first, or the message will not go through.",
    "You must be following me for me to reply.",
    "Follow me, otherwise I cannot get back to you.",
    "Follow first, or I have no way to send it.",
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
# ⛔⛔ A CENA 1 CAIU DE 32 PARA 28 EM 2026-08-05, e a evidencia e' um render.
# O operador mandou o TAKE 01 com a fala CORTADA — e ela tinha exatamente 32
# palavras, o teto. Ou seja: 32 (4,0 palavras/s, o TOPO da faixa 3,4-4,0 da
# doutrina) e' agressivo demais na pratica desta narradora. O exemplo que ele
# reescreveu a mao tem 25 palavras (3,1 p/s).
# ⚠️ 28 = 3,5 p/s, a metade conservadora da faixa. O piso cai junto porque a
# cena perdeu um beat inteiro (o vilao).
# ⚠️ cena 2: teto 32 -> 28 e piso 22 -> 15 em 2026-08-05. A receita perdeu o
# vaso e o operador quer a cena CURTA — o exemplo que ele escreveu a mao tem
# 16 palavras. Piso 22 acusaria silencio numa fala que ele mesmo pediu.
# ⛔⛔ CENA 1: 28 -> 25 EM 2026-08-05. SEGUNDA evidencia de corte no mesmo dia.
# Primeiro 32 cortou; baixei para 28 e 28 CORTOU TAMBEM. O numero nao sai de
# calculo, sai de render (licoes §28).
# ⚠️ 25 palavras = 3,1 p/s, que e' a taxa dos exemplos que o operador escreve
# a mao. E 25 e' exatamente o pior caso viavel da cena 1: abertura 5 + virada
# 5 + raro 10 + fecho 5.
# ⛔ A CENA 3 CONTINUA EM 31 E ISSO E' RISCO CONHECIDO — ver o relatorio ao
# operador. Baixa-la exige encurtar o CTA, que e' alcada dele.
# ⛔⛔ TETO 25 — ordem permanente do operador, 2026-08-05: *"sempre meca. Nao
# pode haver cortes de fala."* O numero vem de render, nao de conta: 32
# cortou, 28 cortou. Os exemplos que ele escreve a mao vivem em 16-25
# palavras (2,0-3,1 palavras/s).
# ⚠️ cena 2 cortava em 12,8%. A cadeia ja' reserva ancora e promessa antes da receita.
# ⛔ NAO baixar o [3] junto: medido, ele vai de max 31 para 36 pelo `or pool`.
# ⭐⭐ MODO REF BELA — contrato compartilhado (short_comum), 2026-08-05.
# Ordem do operador: *"toggle de trava pra modo ref mulher bela em todos os ui
# ux pertinentes dos agentes shorts, que, quando ativados, gera refs mulheres
# com essas caracteristicas"* — super model, corpao, pouca roupa.
# ⛔ O pool e o helper moram no `short_comum`: um pool por motor divergiria em
# uma semana, e classificacao divergente e' o fragmento espelhado que a P9 proibe.
MODO_BELA = True
MODO_FORTE = True

TETO_FALA = {1: 25, 2: 25, 3: 25}
PISO_FALA = {1: 18, 2: 15, 3: 23}


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
                   "metodo", "comum", "raro", "cor", "traje", "copo"]


def etnias_do_mundo(spec):
    """O pool de ETNIA depende do MUNDO em cena — trocar para uma etnia que
    aquele mundo nao comporta e' exatamente a incongruencia que os MUNDOS
    existem para impedir."""
    return list(spec["mundo"]["etnias"])


etnias_do_mundo.recebe_spec = True


def trajes_do_mundo(spec):
    """O pool de TRAJE depende do MUNDO — kurta em cozinha amish e' a mesma
    incongruencia que a etnia errada. A UI lista os nomes curtos."""
    return [x[1] for x in spec["mundo"]["trajes"]]


trajes_do_mundo.recebe_spec = True

EIXOS_UI = [
    ("mundo", "A BOTICA", "MUNDOS", "id"),
    ("etnia", "ETNIA", "etnias_do_mundo", None),
    ("ref", "A BOTICARIA", "REFS", "cabeca"),
    ("traje", "O TRAJE", "trajes_do_mundo", None),
    ("homem", "O ESPANTADO", "HOMENS", "marca"),
    ("prop", "O PROP", "PROPS", "nome"),
    ("substancia", "A ISCA", "SUBSTANCIAS", "nome"),
    ("metodo", "O PREPARO", "METODOS", "id"),
    ("comum", "O COMUM", "COMUNS", "nome"),
    ("raro", "O RARO", "RAROS", "nome"),
    ("copo", "O COPO", "COPOS", None),
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


def _fresco_traje(pool, usados, rng):
    """Como `_fresco`, mas o pool de trajes e' de TUPLAS `(template, curto)` e
    nao de dicts — `_fresco` chama `.get()` e quebra. A chave de frescor e' o
    nome curto.
    ⚠️ `or pool` aqui e' correto e nao e' o estouro silencioso do teto: quando
    todos ja' sairam, repetir e' a unica saida possivel.
    """
    livres = [x for x in pool if x[1] not in usados] or pool
    return rng.choice(livres)


def _por_traje(mundo, curto):
    """Acha o traje do mundo pelo nome curto (a trava da UI guarda o curto).

    ⚠️ Devolve o primeiro do mundo quando o curto nao pertence a ele — o
    operador pode ter travado um traje e depois trocado de mundo, e travar
    `kurta` num mundo amish nao pode derrubar o sorteio.
    """
    for x in mundo["trajes"]:
        if x[1] == curto:
            return x
    return mundo["trajes"][0]


# ⭐⭐ O APELO DA REF — ordem do operador, 2026-08-05: *"As mulheres tem que ter
# mais sex appeal tb, quando for dos EUA"*.
# ⛔ E havia uma CONTRADICAO LITERAL no BLOCO 0: ele mandava *"an ordinary
# everyday relatable person with a plain unremarkable face, NOT A MODEL"*. Pedir
# apelo com essa frase no prompt e' dar duas ordens opostas ao gerador, e ele
# resolve pela ultima. A frase saiu dos mundos dos EUA e ficou nos outros.
# ⚠️ O QUE FICA NOS DOIS CASOS: `not a celebrity, not resembling any famous
# person`. Essa nao e' estetica — e' a trava de identidade que impede o gerador
# de devolver o rosto de alguem real.
# ⚠️ E a estetica UGC continua: iPhone cru, grao, luz frontal. O apelo entra na
# PESSOA, nao na producao — modelo em estudio nao converte neste funil.
# ⚠️ REFORCADO EM 2026-08-05: *"pelo amor de Deus, DE mais sex appeal pra
# essas mulheres, estao muito feias e sem shape"*. A primeira versao falava
# so' de rosto e cabelo — e o BLOCO 0 e' `chest up`, entao rosto sozinho nao
# resolve FIGURA. Agora a clausula nomeia o corpo, e o campo `corpo` das 22
# REFS foi reescrito junto: ele dizia `slim and upright`, `lean and
# long-limbed` — descricao atletica e neutra, que o gerador le como magra e
# sem forma.
# ⛔ Continua tasteful de proposito: `figure`, `shapely`, `toned`. Termo
# explicito nao converte melhor e ainda arrisca recusa do gerador, que custa
# lote (ver RUNBOOK-bisseccao-moderacao).
APELO_EUA = [
    "A strikingly attractive everyday woman, well groomed, with clear even skin, softly styled hair and a noticeably good figure, not a celebrity, not resembling any famous person.",
    "A very good-looking everyday woman with glowing skin, light natural make-up and a shapely figure, not a celebrity, not resembling any famous person.",
    "An unusually pretty everyday woman with fine features, healthy glossy hair and a trim shapely body, not a celebrity, not resembling any famous person.",
    "A head-turning everyday woman, carefully groomed, with bright eyes, full lips and a striking figure, not a celebrity, not resembling any famous person.",
    "A notably beautiful everyday woman with high cheekbones, smooth clear skin and a curvy figure, not a celebrity, not resembling any famous person.",
    "A very attractive everyday woman with a toned shapely figure, shining hair and even skin, not a celebrity, not resembling any famous person.",
]

APELO_PADRAO = (
    "An ordinary everyday relatable person with a plain unremarkable face, not "
    "a celebrity, not a model, not an actor, not resembling any famous person.")


def _apelo(spec):
    """A clausula de apresentacao da REF: apelo nos mundos dos EUA, o registro
    relatable nos demais. ⚠️ `.get` e nao `[...]`: mundo sem o selo cai no
    padrao em vez de derrubar o sorteio."""
    if not spec["mundo"].get("eua"):
        return APELO_PADRAO
    return spec["apelo"]


def _traje(spec):
    """A roupa SORTEADA do mundo, com o artigo certo.

    ⛔ O artigo NAO mora no template: cores como `off-white`, `indigo` e `olive`
    sairiam `a off-white` — bug pago no CLEAN v2 e achado LENDO o render.
    ⚠️ Ate' 2026-08-05 isto lia `spec["mundo"]["traje"]`, UM traje por mundo, e
    o operador mandou tres prints de tres mundos diferentes com a mesma blusa
    bege. Agora o traje e' um eixo proprio, sorteado entre cinco silhuetas.
    """
    cor = spec["cor"]
    return "%s %s" % (_artigo(cor), spec["traje"][0] % cor)


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
        # ⛔⛔ A CENA 1 E' UMA ISCA SO', DESDE 2026-08-05. Ordem do operador
        # lendo o TAKE 01 renderizado com a fala cortada: *"Retire 'Every
        # pharmacy ad sells the expensive pill and buries the cheap recipe' e
        # use bullets curtos"*.
        # ⚠️ O beat do vilao custava 9 a 14 palavras num take que ja' apertava,
        # e era ele que empurrava a cena para o teto. O vilao NAO sumiu: ele
        # desceu para dentro da isca, em seis das vinte e duas entradas.
        # ⭐ TRES BEATS, sorteados em CADEIA e do mais longo para o mais curto:
        # o FECHO carrega o literal `gelatin trick` (intocavel), a VIRADA e o
        # problema cedem em volta. ⛔ Fallback e' a entrada mais CURTA, nunca
        # `or pool`.
        r_fal = raro_falado(spec["raro"])

        def _c1(pb, vr, fc):
            return "%s. %s %s, %s." % (pb.format(o=o1), vr, r_fal, fc)

        cv = min(VIRADAS, key=_palavras)
        cf = min(FECHOS, key=_palavras)
        pb = rng.choice(_cabem(PROBLEMAS, lambda x: _c1(x, cv, cf),
                               TETO_FALA[1]))
        vr = rng.choice(_cabem(VIRADAS, lambda x: _c1(pb, x, cf),
                               TETO_FALA[1]))
        fc = rng.choice(_cabem(FECHOS, lambda x: _c1(pb, vr, x),
                               TETO_FALA[1]))
        f[0] = _c1(pb, vr, fc)

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
            lambda a: _cap((a % rec).format(o=o2)) + " " + curto_p.format(o=o2),
            TETO_FALA[2]))
        # ⛔ `_cap` porque a receita ABRE a sentenca. Ate' 2026-08-05 ela comecava
        # com o literal `Gelatin,` e a maiuscula vinha de graca; com a gelatina
        # fora da lista, o primeiro token passou a ser `{c}` em minuscula e o
        # render saiu **`baking soda, fenugreek and one secret...`**. Achado LENDO
        # a saida, nao pelo linter — frase em minuscula e' gramaticalmente valida.
        meio = _cap((anc % rec).format(o=o2))
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

        # ⛔ 2026-08-05 — `_cabem` termina em `or pool`, e com teto 25 ele
        # devolvia o pool INTEIRO: a cena 3 subiu de max 31 para 36. Aqui o
        # fallback e' a entrada mais CURTA, e a ISCA tambem cede — ela e' o
        # unico slot com folga (`the whole recipe` vs `the recipe and the
        # measurements`), e o `Comment gelatin,` e' intocavel.
        def _ok(pool, monta):
            v = [x for x in pool if _palavras(monta(x)) <= TETO_FALA[3]]
            return v or [min(pool, key=lambda x: _palavras(monta(x)))]

        isca_e = min(ISCAS_ENTREGA, key=_palavras) if _palavras(
            _c3(min(USOS, key=_palavras), curto_g)) > TETO_FALA[3] else isca_e
        uso = rng.choice(_ok(USOS, lambda u: _c3(u, curto_g)))
        gate = rng.choice(_ok(GATES, lambda g: _c3(uso, g)))
        f[2] = _c3(uso, gate)

    return f


def sortear(pagina, rng, led, travas=None):
    """Monta a spec. `travas` fixa eixos (pre-selecao do painel e cadeado)."""
    travas = travas or {}
    usados = led.get(pagina, {})

    fam_trava = travas.get("familia_mundo")
    # ⭐ a pele filtra o UNIVERSO de mundos antes de qualquer sorteio (ver a
    # tabela PELE_DE_ETNIA no topo). Sem trava, `_disponiveis` e' MUNDOS.
    _pele = travas.get("pele")
    _disponiveis = mundos_da_pele(_pele)
    _familias = list(dict.fromkeys(m["familia"] for m in _disponiveis))
    if travas.get("mundo"):
        mundo = _por_id(MUNDOS, travas["mundo"])
    else:
        if fam_trava and fam_trava != "livre":
            fam = fam_trava
        else:
            fam = _fresco([{"id": x} for x in _familias],
                          usados.get("familia_mundo", []), rng, "id")["id"]
        # ⚠️ o `or` cede: familia travada na UI que nao tem mundo daquela pele
        # (ex.: nicho=caribenha + pele=clara) mantem a FAMILIA, porque ela foi
        # escolhida a mao e escolha explicita ganha de toggle.
        mundo = rng.choice(
            [m for m in _disponiveis if m["familia"] == fam]
            or [m for m in MUNDOS if m["familia"] == fam]
        )

    # ⛔ a etnia tambem cede a pele: um mundo pode listar mais de uma, e sem
    # este filtro o sorteio poderia devolver a que contradiz a trava.
    _ets = [e for e in mundo["etnias"] if _pele_de(e) == _pele]         if _pele in ("clara", "escura") else []
    et = travas.get("etnia") or rng.choice(_ets or mundo["etnias"])
    cor = travas.get("cor") or rng.choice(mundo["cores"])
    # ⭐ O TRAJE E' EIXO PROPRIO desde 2026-08-05, com pool por mundo. Cada
    # entrada e' (template_com_%s_de_cor, nome_curto) — o curto tem de vir do
    # traje SORTEADO, senao a ancora descreve uma roupa que nao esta' em cena.
    reacao = _fresco_traje(REACOES_HOMEM, usados.get("reacao", []), rng)
    # ⭐ O COPO virou eixo: sorteado, travavel e visivel no painel.
    copo = travas.get("copo") or _fresco([{"id": c} for c in COPOS],
                                         usados.get("copo", []), rng, "id")["id"]
    apelo = rng.choice(APELO_EUA)
    # ⛔ NO MODO BELA A ROUPA TAMBEM MUDA. O operador nomeou TRES coisas —
    # *"super models com corpao e pouca roupa"* — e trocar so' o rosto e o corpo
    # deixaria a REF de biquini de tricô amish. Aqui o traje vem do MUNDO, entao
    # o modo o substitui pelo pool proprio do `short_comum`.
    traje = (_por_traje(mundo, travas["traje"]) if travas.get("traje")
             else sc.traje_bela(rng) if travas.get("bela")
             else _fresco_traje(mundo["trajes"], usados.get("traje", []), rng))
    ref = (_por_id(REFS, travas["ref"], "cabeca") if travas.get("ref")
           else sc.ref_bela(REFS[0], rng) if travas.get("bela")
           else rng.choice(REFS))
    homem = (_por_id(HOMENS, travas["homem"]) if travas.get("homem")
             else sc.ref_forte(HOMENS[0], rng) if travas.get("forte")
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
    # ⛔ 2026-08-10 — SO' OS TRES APELIDOS SAO SORTEAVEIS (ordem do
    # operador, parque inteiro). `soldier` e `tool` seguem no NUCLEO porque
    # as LENTES os usam para DETECTAR o orgao; o que muda e' que nao saem
    # mais na fala. Ver `short_comum.orgaos_sorteaveis`.
    orgaos = sc.orgaos_sorteaveis(rng, 2)

    # ⭐ A FLAG VIAJA NO SPEC. O `montar()` nao recebe `travas`, e sem

    # isto a clausula do rosto e o `resumo_pt` ficavam na versao comum

    # enquanto o corpo e a roupa ja' eram os do modo — a contradicao

    # exata que o CL26 documenta.

    spec = {"pagina": pagina, "bela": bool(travas.get("bela")),
            "forte": bool(travas.get("forte")), "mundo": mundo, "etnia": et, "cor": cor,
            "copo": copo,
            "traje": traje, "reacao": reacao, "apelo": apelo,
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
                        _sem_artigo(r["marca"]), spec["traje"][1])


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
        "copo": spec.get("copo", BO_COPO), "anti": (sc.ANTICELEB_BELA if spec.get("bela") else ANTICELEB), "cauda": CAUDA, "band": band,
    }
    v["nao_toca"] = BO_NAO_TOCA % m["sup"]

    b = {}
    b["BLOCO 0 (REF)"] = (
        "REF 01: Photo of a real person, a %(idade)d-year-old %(etnia)s woman, "
        "chest up, facing the camera directly, neutral steady expression with "
        "her mouth closed. %(pessoa_curta)s %(apelo)s Hands out of frame, "
        "no objects. Plain neutral gray background, soft even frontal light. "
        "Slight sensor grain, soft focus, raw iPhone front camera aesthetic. "
        "No subtitles, no captions, no burned-in text, no watermark."
        % dict(v, apelo=_apelo(spec), pessoa_curta="%s. %s. Wearing %s."
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
        # ⛔⛔ `_cap` NA REACAO. As entradas de REACOES_HOMEM comecam em
        # MINUSCULA de proposito (encaixam no meio de frase noutros
        # motores) e a `BO_HOMEM` poe um PONTO antes delas — o bloco saia
        # com "wearing a burgundy polo shirt. his chin is lowered".
        # ⚠️ MEDIDO em 2026-08-08: 300 de 300 blocos. Frase em minuscula
        # e gramaticalmente valida — nenhum guard de placeholder, token
        # banido ou teto a pega. So LENDO.
                                    hom["roupa"], _cap(spec["reacao"][0]))))

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
        BO_HOMEM_TAKE % spec["reacao"][1],
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
# ⛔⛔ `epimedium\s+\w+` REPROVAVA A COPY DO PROPRIO OPERADOR — corrigido
# 2026-08-05. O padrao existia para pegar o binomio `Epimedium spp.`, mas casava
# `epimedium` seguido de QUALQUER palavra: a frase que ele escreveu a mao
# ("Fresh ginger and epimedium and a secret") era acusada de nome cientifico.
# ⚠️ `epimedium` E' o nome POPULAR no nosso pool — esta' no campo `nome`, e BO8
# exige que ele apareca na cena 2. A lente estava proibindo o que outra lente
# obrigava, e so' nao explodia antes porque a receita antiga punha uma virgula
# depois dele. Mudar a ordem das palavras acordou o conflito.
# ⭐ Agora so' o que e' de fato binomio: o epiteto tem de ser `spp.` ou um nome
# de especie, nunca uma palavra funcional do ingles.
CIENTIFICO = re.compile(
    r"\b(lepidium|eurycoma|tribulus terrestris|epimedium\s+(?:spp\.?|"
    r"grandiflorum|sagittatum|brevicornum|koreanum)|trigonella|"
    r"ptychopetalum|ginkgo biloba|mucuna pruriens|smilax\s+(?:spp\.?|\w+ata))"
    r"\b", re.I)


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
    alvos = [(2, ["gelatin"] + [o.lower() for o in sc.APELIDOS_16]),
             (3, [o.lower() for o in sc.APELIDOS_16])]
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

    # --- BO3: APOSENTADA EM 2026-08-05 -------------------------------------
    # ⛔ Ordem do operador: *"tirar o vilao do escopo do take 1"*. A lente cobrava
    # que uma parcela das iscas nomeasse a farmacia; sem vilao na cena 1 ela
    # reprovaria 100% da producao. Regra que cobra o que o operador mandou tirar
    # nao e' defesa, e' sabotagem.
    # ⚠️ CONSEQUENCIA REGISTRADA, porque ela e' real e ele decidiu com ela na
    # mesa: a farmacia so' existia nessas iscas — zero mencoes em ANCORAS,
    # PROMESSAS, RECEITAS, USOS, GATES e ISCAS_ENTREGA. Ela sai do video inteiro.
    # O angulo continua sendo a botica de casa, so' que sem o adversario dito em
    # voz alta: ele fica implicito no `nobody sells` dos fechos e na propria
    # existencia da receita caseira.

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
    # ⚠️ Mede o copo SORTEADO, nao a constante. Quando o copo virou eixo
    # (2026-08-06), este linter continuou procurando `BO_COPO` — que agora e' so'
    # a primeira entrada do pool — e acusou 1064 de 1200 sorteios. O linter caiu
    # junto com a mudanca porque descrevia o copo como ele NAO e' mais escrito;
    # foi o mesmo erro que quebrou a ancora do TROCA algumas horas antes.
    copo = spec.get("copo", BO_COPO)
    for nome in ("IMAGE 01/03", "IMAGE 02/03"):
        if copo in blocos[nome]:
            ach.append(("ERRO", "BO5: o copo pronto fora da cena 3 (%s) — "
                                "entrega o payoff antes da promessa" % nome))
    if copo not in i3:
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

    # ⛔⛔ TAKE CONTRA IMAGE — 2026-08-05. Este motor tem `lint()` proprio e NAO
    # passa pelo `lint_curto`, entao a lente compartilhada nao chegava aqui.
    # ⚠️ Foi assim que a primeira varredura deu "limpo" para sete motores: eles
    # nunca rodaram a lente. "Limpo" sem cobertura e' o pior resultado possivel,
    # porque parece verde. Medir a lente e' medir TAMBEM se ela e' chamada.
    # ⛔ PAINEL HONESTO — 2026-08-05. Nenhum eixo desenhado no painel pode
    # deixar de chegar ao video.
    sc.lint_painel_honesto(sys.modules[__name__], spec, blocos, ach)

    # ⛔ HIERARQUIA DO MECANISMO — diretriz do operador, 2026-08-06 (§31).
    # So dispara quando a cena 2 mostra preparo em quadro.
    sc.lint_hierarquia_mecanismo(spec, blocos, ach)

    sc.lint_take_vs_image(blocos, ach)

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
               "comum": len(COMUNS), "raro": len(RAROS), "homem": len(HOMENS),
               "copo": len(COPOS)}

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
                       ("HOMENS", HOMENS), ("PROBLEMAS", PROBLEMAS),
                       ("VIRADAS", VIRADAS), ("FECHOS", FECHOS),
                       ("USOS", USOS),
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
    # ⛔⛔ NENHUM POOL COM ENTRADA REPETIDA — trava criada em 2026-08-05.
    # Ao ampliar os pools eu acrescentei tres iscas que JA' EXISTIAM. Duplicata
    # nao quebra nada: ela dobra em silencio a chance daquela linha e ocupa um
    # slot que deveria ser repertorio novo. O sintoma so' apareceu porque a
    # cobertura media 15 de 18 sem conseguir apontar as faltantes.
    # ⚠️ Compara pelo TEXTO da entrada, nao pelo objeto — pools de tupla e de
    # dict entram por `str`.
    for _n, _p in (("PROBLEMAS", PROBLEMAS), ("VIRADAS", VIRADAS),
                   ("FECHOS", FECHOS), ("RECEITAS", RECEITAS),
                   ("ANCORAS", ANCORAS), ("PROMESSAS", PROMESSAS),
                   ("USOS", USOS), ("ISCAS_ENTREGA", ISCAS_ENTREGA),
                   ("GATES", GATES), ("REFS", REFS), ("HOMENS", HOMENS),
                   ("REACOES_HOMEM", REACOES_HOMEM), ("MUNDOS", MUNDOS)):
        _txt = [str(_x) for _x in _p]
        _rep = sorted({_x for _x in _txt if _txt.count(_x) > 1})
        for _x in _rep:
            falhas.append("pool %s tem entrada REPETIDA: %s" % (_n, _x[:70]))

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

    # ⚠️ O controle de BO3 saiu junto com a lente em 2026-08-05. Ele montava um
    # repertorio sem vilao e esperava reprovacao — hoje esse e' o repertorio
    # CERTO. Controle de regra aposentada que fica para tras vira ruido, e ruido
    # ensina o operador a ignorar o autoteste.

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
    # ⛔⛔ A SONDA ESTAVA CEGA, e o proprio autoteste a reportava assim todo
    # dia: ela injetava a CONSTANTE `BO_COPO` na cena 1, e a lente procura o
    # copo SORTEADO (`spec["copo"]`, eixo desde 2026-08-06). Quando os dois
    # saem diferentes — que e' o caso na maioria dos sorteios — a sabotagem
    # nunca chega na regra, e a regra do copo nao protegia nada.
    # ⚠️ Mesma classe da sonda do CO7 no COLO: sonda que nao altera O QUE A
    # LENTE OLHA passa sempre, e passar sempre e' o mesmo que nao existir.
    b5 = dict(b)
    b5["IMAGE 01/03"] += " " + s.get("copo", BO_COPO)
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
