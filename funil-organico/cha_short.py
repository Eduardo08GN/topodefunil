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
LEDGER = os.path.join(AQUI, ".cha-short-ledger.json")

TITULO = "AGENTE CHA SHORT"
SLUG = "cha-short"
SUBTITULO = ("a caneca estendida na lente · da varanda para a cozinha · o corpo\n"
             "e' a retencao · 3 cenas de 8s")

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


# ⭐⭐ PELE TRAVAVEL — contrato aditivo criado no CLEAN V2 em 2026-08-05, e este
# motor tem exatamente o mesmo defeito que o criou: o seletor clara/escura do
# painel troca a PAGINA, e este motor IGNORA `ETNIA[pagina]` de proposito (a
# etnia sai de dentro do MUNDO, doutrina "etnia arrasta o mundo inteiro"). O
# operador clicava, o botao acendia, e o sorteio seguia aleatorio — pior que nao
# ter botao, porque PARECIA travado.
# ⚠️ Lido pela ui_agente com `getattr`: motor sem a flag nao muda de comportamento.
PELE_TRAVAVEL = True


# ⛔⛔ A CLASSIFICACAO E' LISTA EXPLICITA, NUNCA "tudo que nao e' branco".
# Correcao de campo do operador em 2026-08-05, com print: no CLEAN V2 ele travou
# `escura` e recebeu um REF Asian American. **Para ele, escura = NEGRO.**
# ⚠️ Asiatico, latino, mediterraneo, nativo e mestico nao sao nem clara nem
# escura — so' saem com a pele LIVRE. A regra binaria do `paginas_por_pele`
# (clara = tem `white`, escura = o resto) e' o que produzia o defeito, e eu a
# tinha herdado meia hora antes achando que estava sendo congruente.
# ⛔ Mesma lista dos outros motores: classificacoes divergentes entre agentes
# seriam o fragmento espelhado que a P9 proibe.
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
# ⭐⭐ BO1 — A CANECA ESTENDIDA NA LENTE, na VARANDA. Lido frame a frame em
# 0:00-0:07: ela SENTADA numa cadeira de varanda, o braco esticado para a
# camera com a caneca de vidro, que fica GRANDE em primeiro plano enquanto ela
# aparece menor atras. E' um enquadramento de escala, nao de gosto: a caneca
# perto da lente e' o objeto; o corpo dela atras e' a retencao.
# ⛔ SENTADA, nao em pe' — sentada as pernas ficam em quadro, e a ordem do
# operador sobre este angulo e' explicita quanto a isso.
BO_CANECA = (
    "Filmed straight on at chest height. Sitting in a metal porch chair, leaning "
    "slightly towards the camera, is %s. Her right arm is stretched out towards "
    "the lens holding %s, close enough that it fills the lower middle of the "
    "frame while she sits smaller behind it. Her knees are together and angled "
    "to frame-left, her bare legs in shot. She is looking straight into the lens "
    "with her mouth open mid-word as she speaks, her front teeth even and "
    "complete."
)

# ⛔ BO2 — no TAKE da cena 1 a caneca NAO se move e ela NAO bebe. Se ela leva a
# caneca a' boca, o objeto sai do quadro justamente no segundo em que a fala o
# promete. Diz-se pela POSICAO, nunca por `motionless` — ordem impossivel para
# um objeto na mao, e o Veo resolve SOLTANDO o objeto (F12b).
BO_CANECA_ESTAVEL = (
    "Her right arm stays extended at exactly the same distance from the lens and "
    "the mug stays the same size in frame, the liquid inside barely moving. She "
    "never drinks from it and never lowers it."
)

# ⭐ A CANECA. Lida na fonte: vidro transparente com alca, cha verde-claro,
# preenchida quase ate' a borda. ⛔ NUNCA opaca — o que vende aqui e' ver o
# liquido, e caneca opaca vira xicara de cafe.
BO_MUG = ("a clear glass mug with a handle, filled almost to the brim with pale "
          "green tea")

# ⭐⭐ BO3 — A PANELA NO FOGAREIRO. Lido em 0:08-0:24: fogareiro eletrico BRANCO
# portatil sobre a bancada de madeira, panela de inox com agua, prato de limoes
# cortados a' esquerda, gengibre inteiro e cabeca de alho a' direita.
# ⛔ Os limoes JA' ESTAO BOIANDO na panela: nao ha' frame de "antes". Oito
# segundos nao pagam preparacao — mesma economia do EXTERIOR e do TROCA.
BO_PANELA = (
    "Medium shot in %(coz)s, filmed straight on at the height of the %(sup)s, "
    "framed so that %(sup_a)s runs across the bottom third of the picture. "
    "Standing behind it, centred in the frame, is %(ancora)s. On the %(sup)s in "
    "front of her sits a small white electric hotplate with a stainless steel "
    "pan on it, cut lemon halves already floating in the water inside. To one "
    "side is a plate of cut lemons, to the other %(comum_img)s and %(raro_img)s. "
    "She holds one of them up in her right hand at chest height, turned so the "
    "lens sees it. Her expression is bright and certain, her mouth open mid-word "
    "as she speaks. She is the only person in the frame."
)

# ⛔ BO4 — ela nunca toca no resto da bancada. Sem isto o Veo comeca a mexer em
# tudo o que esta' em quadro e a continuidade entre os blocos de 8s morre.
BO_NAO_TOCA = ("Nothing else on the %s is touched, moved, opened or lifted, and "
               "nothing is added to it or taken away.")

BO_ANCORA = ("the same %d-year-old %s woman from the first scene, same %s, same "
             "%s, same %s")

# ⭐⭐ A CLAUSULA ANTI-CELEBRIDADE, NO REGISTRO DE MULHER. Ordem do operador,
# 2026-08-05, lendo o prompt gerado: a REF deste angulo **e' top model**.
# ⛔ `Ordinary relatable face, not a model` brigava DE FRENTE com o pool: o
# gerador recebia "tall and long-legged, strikingly beautiful" no corpo e "cara
# comum, nao e' modelo" no rosto NA MESMA FRASE, e resolvia a contradicao contra
# nos — rosto sem graca em cima de um corpo encomendado bonito.
# ⚠️ E' o mesmo conserto que o CLEAN ja' tinha feito (CL26): a protecao de
# IDENTIDADE (nao-celebridade) fica; so' sai o "comum" e o "nao e' modelo".
# ⛔ A negacao anti-celebridade saiu daqui em 2026-08-14, por ordem do operador
# (*"tire not a celebrity do prompt"*): declaracao INJETA o token que ela nega.
# A metade positiva ficou. Ver CLAUDE.md §"CONTRA A CELEBRIDADE, SILENCIO".
ANTICELEB = ("A strikingly beautiful face.")
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
    {"id": "carolina", "eua": True, "selo": "N", "familia": "sul_atlantico",
     "etnias": ['Black American', 'white American'],
     "var": 'the front porch of a red-brick house with white siding, potted ferns and geraniums along the steps and a brick floor',
     "var_c": 'red-brick front porch',
     "coz": 'a bright home kitchen with cream walls, hanging plants in macrame slings, a big window onto green leaves',
     "coz_c": 'cream kitchen with hanging plants',
     "sup_a": 'a butcher-block counter',
     "sup": 'counter',
     "trajes": [
         ('%s ribbed knit halter top with a deep cowl neckline that falls to the waist, worn with a short leopard-print skirt',
          'knit cowl halter'),
         ('%s cropped knit tank with a plunging V and a short denim skirt',
          'plunging knit tank'),
         ('%s wrapped halter tied at the neck with a very short A-line skirt',
          'tied halter'),
         ('%s low-cut bodysuit under an open shirt, with cut-off shorts',
          'low-cut bodysuit'),
     ],
     "cores": ['cream', 'sand beige', 'white', 'soft gold', 'dusty rose', 'black'],
     "luz_e": 'Bright overcast daylight under the porch roof.',
     "luz_e_c": 'bright porch daylight',
     "luz": 'Broad daylight from the window at frame-right.',
     "luz_c": 'broad window daylight',
     "audio": 'cicadas outside, a wind chime, quiet room tone'},

    {"id": "brooklyn", "eua": True, "selo": "N", "familia": "nordeste",
     "etnias": ['Black American', 'Hispanic American'],
     "var": 'the stoop of a Brooklyn brownstone, wrought-iron rail, planters on the steps and parked cars along the kerb behind',
     "var_c": 'brownstone stoop',
     "coz": 'a narrow apartment kitchen with white subway tile, a fire escape framed in the window, plants crowded on the sill',
     "coz_c": 'subway-tile apartment kitchen',
     "sup_a": 'a small tiled counter',
     "sup": 'counter',
     "trajes": [
         ('%s tight ribbed crop top with a deep scoop neck and low-slung track shorts',
          'ribbed crop top'),
         ('%s satin cami with thin straps and a very short pleated skirt',
          'satin cami'),
         ('%s halter bodysuit with a plunging front, worn with bike shorts',
          'halter bodysuit'),
         ('%s open-knit tank over a bralette, with a short wrap skirt',
          'open-knit tank'),
     ],
     "cores": ['black', 'white', 'scarlet', 'cobalt', 'silver', 'burgundy'],
     "luz_e": 'Hard afternoon sun bouncing off the street.',
     "luz_e_c": 'hard street sun',
     "luz": 'Cool daylight through the fire-escape window.',
     "luz_c": 'cool window daylight',
     "audio": 'distant traffic, a car door, quiet room tone'},

    {"id": "louisiana", "eua": True, "selo": "N", "familia": "golfo",
     "etnias": ['Black American', 'white American'],
     "var": 'the gallery of a Louisiana shotgun house, turned wooden posts and gingerbread trim, ferns hanging in baskets and a painted board floor',
     "var_c": 'shotgun-house gallery',
     "coz": 'a warm Creole kitchen with beadboard walls, a cast-iron skillet hanging by the stove, jars of dried peppers on a shelf',
     "coz_c": 'beadboard Creole kitchen',
     "sup_a": 'a scrubbed pine worktop',
     "sup": 'worktop',
     "trajes": [
         ('%s off-shoulder crop blouse tied under the bust with a short flared skirt',
          'tied crop blouse'),
         ('%s deep-V sundress cut short above the knee',
          'deep-V sundress'),
         ('%s halter top with a knotted front and very short shorts',
          'knotted halter'),
         ('%s lace-trimmed cami with a short skirt and bare legs',
          'lace-trimmed cami'),
     ],
     "cores": ['emerald', 'white', 'hot pink', 'gold', 'cobalt', 'black'],
     "luz_e": 'Humid golden light filtering through the gallery posts.',
     "luz_e_c": 'humid golden light',
     "luz": 'Warm afternoon light through a shuttered window.',
     "luz_c": 'warm shuttered light',
     "audio": 'crickets, a screen door on a spring, quiet room tone'},

    {"id": "texas", "eua": True, "selo": "N", "familia": "texas",
     "etnias": ['white American', 'Hispanic American'],
     "var": 'the covered porch of a Texas ranch house, cedar posts and a metal roof, a Texas flag on the rail, boots by the door and dry pasture beyond',
     "var_c": 'cedar ranch porch',
     "coz": 'a ranch kitchen with knotty-pine cabinets, a cast-iron pan on the hob, a rack of dried chillies by the window',
     "coz_c": 'knotty-pine ranch kitchen',
     "sup_a": 'a wide pine countertop',
     "sup": 'countertop',
     "trajes": [
         ('%s cropped western shirt knotted high with the top buttons open, worn with very short denim cut-offs',
          'knotted western shirt'),
         ('%s low-cut tank tucked into a short denim skirt',
          'low-cut tank'),
         ('%s bandana halter tied at the back with cut-off shorts',
          'bandana halter'),
         ('%s sleeveless denim shirt worn open over a bralette, with short shorts',
          'open denim shirt'),
     ],
     "cores": ['denim blue', 'white', 'scarlet', 'turquoise', 'black', 'cream'],
     "luz_e": 'Flat bright sun under the porch roof.',
     "luz_e_c": 'flat porch sun',
     "luz": 'Strong daylight from a window over the sink.',
     "luz_c": 'strong sink-window light',
     "audio": 'wind over open ground, a distant truck, quiet room tone'},

    {"id": "miami", "eua": True, "selo": "N", "familia": "florida",
     "etnias": ['Hispanic American', 'Black American'],
     "var": 'the terrace of a pastel Miami bungalow, jalousie windows behind, palms and bird-of-paradise in glazed pots and a terrazzo floor',
     "var_c": 'pastel Miami terrace',
     "coz": 'a bright Florida kitchen with white cabinets and mint tile, a cafetera on the hob, potted herbs on the sill',
     "coz_c": 'mint-tile Florida kitchen',
     "sup_a": 'a white tiled counter',
     "sup": 'counter',
     "trajes": [
         ('%s tiny halter top tied at the neck with a very short wrap skirt',
          'tied halter top'),
         ('%s deep-V bodysuit worn with high-cut shorts',
          'deep-V bodysuit'),
         ('%s crochet bralette top under a mesh cover-up, with a mini skirt',
          'crochet bralette top'),
         ('%s strappy cami with a plunging front and a short skirt',
          'strappy cami'),
     ],
     "cores": ['hot pink', 'turquoise', 'white', 'lime green', 'gold', 'black'],
     "luz_e": 'Hot tropical daylight bouncing off pale walls.',
     "luz_e_c": 'hot tropical daylight',
     "luz": 'Bright flat daylight through a jalousie window.',
     "luz_c": 'bright jalousie light',
     "audio": 'palm fronds, a scooter passing, quiet room tone'},

    {"id": "california", "eua": True, "selo": "N", "familia": "oeste",
     "etnias": ['white American', 'Hispanic American'],
     "var": 'the front deck of a California bungalow, redwood boards and a low rail, succulents in terracotta and dry hills in the distance',
     "var_c": 'redwood bungalow deck',
     "coz": 'an airy kitchen with open shelving, a wide window onto a lemon tree, mason jars of grains in a row',
     "coz_c": 'open-shelf airy kitchen',
     "sup_a": 'a pale wood counter',
     "sup": 'counter',
     "trajes": [
         ('%s ribbed tank with a deep neckline and short linen shorts',
          'ribbed tank'),
         ('%s halter jumpsuit cut short at the thigh with an open back',
          'halter jumpsuit'),
         ('%s cropped cardigan buttoned once over bare skin, with a mini skirt',
          'single-button cardigan'),
         ('%s low-cut slip dress cut above the knee',
          'low-cut slip dress'),
     ],
     "cores": ['white', 'black', 'dusty rose', 'denim blue', 'cream', 'olive'],
     "luz_e": 'Clean west-coast daylight, slightly hazy.',
     "luz_e_c": 'hazy west-coast daylight',
     "luz": 'Even daylight from a large window.',
     "luz_c": 'even window daylight',
     "audio": 'a distant lawn sprinkler, birds, quiet room tone'},

    {"id": "detroit", "eua": True, "selo": "N", "familia": "meio_oeste",
     "etnias": ['Black American', 'white American'],
     "var": 'the porch of a Detroit two-storey with aluminium siding, a swing seat on chains and bare winter branches over the walk',
     "var_c": 'sided two-storey porch',
     "coz": 'a lived-in kitchen with laminate counters, a chalkboard on the fridge, plants along the sill',
     "coz_c": 'laminate family kitchen',
     "sup_a": 'a laminate countertop',
     "sup": 'countertop',
     "trajes": [
         ('%s fitted scoop-neck top cut short at the midriff, with a short skirt',
          'scoop-neck crop'),
         ('%s zip-front bodysuit worn half unzipped with bike shorts',
          'half-zipped bodysuit'),
         ('%s spaghetti-strap cami with a low front and a mini skirt',
          'spaghetti-strap cami'),
         ('%s cropped hoodie unzipped over a bralette, with short shorts',
          'unzipped cropped hoodie'),
     ],
     "cores": ['black', 'burgundy', 'royal blue', 'silver', 'white', 'scarlet'],
     "luz_e": 'Cold flat daylight off the siding.',
     "luz_e_c": 'cold flat daylight',
     "luz": 'Grey daylight through a kitchen window.',
     "luz_c": 'grey window light',
     "audio": 'a car passing on wet road, quiet room tone'},

    {"id": "atlanta", "eua": True, "selo": "N", "familia": "sul_atlantico",
     "etnias": ['Black American'],
     "var": 'the porch of an Atlanta craftsman, tapered columns on brick piers, boston ferns in hanging baskets and a swing at frame-left',
     "var_c": 'craftsman porch',
     "coz": 'a warm kitchen with navy cabinets and brass handles, a window onto a green yard, herbs in jars and a row of small clay pots on the sill',
     "coz_c": 'navy-and-brass kitchen',
     "sup_a": 'a marble-look counter',
     "sup": 'counter',
     "trajes": [
         ('%s ribbed halter dress cut very short with a deep neckline',
          'ribbed halter dress'),
         ('%s corset-style top with a short flared skirt',
          'corset-style top'),
         ('%s one-shoulder crop top with a mini skirt',
          'one-shoulder crop'),
         ('%s low-cut knit bodysuit with a short wrap skirt',
          'low-cut bodysuit'),
     ],
     "cores": ['dusty rose', 'white', 'black', 'teal', 'gold', 'wine'],
     "luz_e": 'Soft southern daylight in the porch shade.',
     "luz_e_c": 'soft porch shade',
     "luz": 'Warm daylight from a window at frame-left.',
     "luz_c": 'warm window daylight',
     "audio": 'birdsong, a screen door, quiet room tone'},

    {"id": "arizona", "eua": True, "selo": "N", "familia": "sudoeste",
     "etnias": ['Hispanic American', 'white American'],
     "var": 'the shaded ramada of a stucco house, exposed beams overhead, barrel cactus in pots and pale desert light beyond',
     "var_c": 'stucco ramada',
     "coz": 'a stucco kitchen with a tiled backsplash, a string of dried chillies by the door, clay pots on a shelf',
     "coz_c": 'tiled stucco kitchen',
     "sup_a": 'a tiled worktop',
     "sup": 'worktop',
     "trajes": [
         ('%s off-shoulder crop top with very short shorts',
          'off-shoulder crop'),
         ('%s low-cut tank knotted at the waist with a short skirt',
          'knotted tank'),
         ('%s halter top with a plunging front and cut-off denim shorts',
          'plunging halter'),
         ('%s short slip dress with thin straps and a deep neckline',
          'short slip dress'),
     ],
     "cores": ['turquoise', 'white', 'black', 'scarlet', 'denim blue', 'cream'],
     "luz_e": 'Bright desert light softened under the ramada.',
     "luz_e_c": 'shaded desert light',
     "luz": 'Hard daylight through a deep-set window.',
     "luz_c": 'hard deep-set window light',
     "audio": 'dry wind, a distant dog, quiet room tone'},

    {"id": "apalache", "eua": True, "selo": "N", "familia": "apalaches",
     "etnias": ['white American'],
     "var": 'the plank porch of a mountain house, split firewood stacked to the rail, a rocking chair and forested ridges behind',
     "var_c": 'mountain plank porch',
     "coz": 'a mountain kitchen with painted board walls, a wood stove in the corner, bundles of dried herbs hanging from a beam',
     "coz_c": 'board-walled mountain kitchen',
     "sup_a": 'a worn plank table',
     "sup": 'table',
     "trajes": [
         ('%s cropped flannel shirt knotted under the bust and unbuttoned at the top, with short denim cut-offs',
          'knotted flannel'),
         ('%s low-cut tank with very short shorts',
          'low-cut tank'),
         ('%s ribbed camisole with a short skirt and bare legs',
          'ribbed camisole'),
         ('%s open flannel over a bralette with cut-off shorts',
          'open flannel'),
     ],
     "cores": ['dark red', 'denim blue', 'forest green', 'white', 'black', 'cream'],
     "luz_e": 'Cool mountain daylight, thin and clear.',
     "luz_e_c": 'cool mountain daylight',
     "luz": 'Low daylight through a small window.',
     "luz_c": 'low small-window light',
     "audio": 'wind in trees, a distant crow, quiet room tone'},

    {"id": "jersey", "eua": True, "selo": "N", "familia": "nordeste",
     "etnias": ['white American', 'Hispanic American'],
     "var": 'the front step of a Jersey row house, vinyl siding and an awning, a plastic chair and a hedge trimmed square by the walk',
     "var_c": 'row-house front step',
     "coz": 'a tidy kitchen with white cabinets, a wall clock, a bowl of fruit on the counter',
     "coz_c": 'tidy white kitchen',
     "sup_a": 'a laminate counter',
     "sup": 'counter',
     "trajes": [
         ('%s tight low-cut top with a very short skirt',
          'tight low-cut top'),
         ('%s halter crop top with high-waisted shorts',
          'halter crop top'),
         ('%s bodysuit with a plunging neckline and a mini skirt',
          'plunging bodysuit'),
         ('%s satin cami worn under an open jacket with short shorts',
          'satin cami'),
     ],
     "cores": ['black', 'hot pink', 'white', 'navy', 'silver', 'scarlet'],
     "luz_e": 'Flat suburban daylight under the awning.',
     "luz_e_c": 'flat awning daylight',
     "luz": 'Even ceiling light with daylight from the window.',
     "luz_c": 'even kitchen light',
     "audio": 'a lawnmower two houses down, quiet room tone'},

    {"id": "nashville", "eua": True, "selo": "N", "familia": "tennessee",
     "etnias": ['white American', 'Black American'],
     "var": 'the porch of a Nashville cottage with shiplap and a metal roof, string lights along the beam and hydrangeas by the steps',
     "var_c": 'shiplap cottage porch',
     "coz": 'a kitchen with shiplap walls and a farmhouse sink under a window onto a green yard, mason jars in a row',
     "coz_c": 'shiplap farmhouse kitchen',
     "sup_a": 'a butcher-block counter',
     "sup": 'counter',
     "trajes": [
         ('%s cropped tank with a deep scoop neck and a short denim skirt',
          'deep-scoop tank'),
         ('%s knotted gingham shirt open at the top with cut-off shorts',
          'knotted gingham shirt'),
         ('%s halter sundress cut short above the knee',
          'halter sundress'),
         ('%s low-cut bodysuit with a short flared skirt',
          'low-cut bodysuit'),
     ],
     "cores": ['denim blue', 'white', 'scarlet', 'black', 'cream', 'emerald'],
     "luz_e": 'Soft golden light along the porch.',
     "luz_e_c": 'soft golden porch light',
     "luz": 'Bright daylight over the farmhouse sink.',
     "luz_c": 'bright sink daylight',
     "audio": 'cicadas, a screen door, quiet room tone'},

    {"id": "chicago", "eua": True, "selo": "N", "familia": "meio_oeste",
     "etnias": ['Black American', 'white American'],
     "var": 'the back porch of a Chicago three-flat, painted wooden stairs zigzagging above, tomato plants in buckets and an alley beyond the fence',
     "var_c": 'three-flat back porch',
     "coz": 'a compact kitchen with painted cabinets, a radiator under the window, jars on an open shelf',
     "coz_c": 'painted compact kitchen',
     "sup_a": 'a narrow counter',
     "sup": 'counter',
     "trajes": [
         ('%s ribbed tank with a low front tucked into a short skirt',
          'low-front tank'),
         ('%s wrap top tied at the waist with very short shorts',
          'wrap top'),
         ('%s cropped knit with a deep V and a mini skirt',
          'deep-V knit'),
         ('%s slip top with thin straps and short shorts',
          'slip top'),
     ],
     "cores": ['burgundy', 'royal blue', 'black', 'white', 'camel', 'scarlet'],
     "luz_e": 'Clear midday light between the buildings.',
     "luz_e_c": 'clear midday light',
     "luz": 'Cool daylight through a tall sash window.',
     "luz_c": 'cool sash-window light',
     "audio": 'an elevated train far off, quiet room tone'},

    {"id": "nova_inglaterra", "eua": True, "selo": "N", "familia": "nova_inglaterra",
     "etnias": ['white American'],
     "var": 'the porch of a New England clapboard house, white rail and blue shutters, hydrangeas in bloom and a picket fence at the walk',
     "var_c": 'clapboard porch',
     "coz": 'a coastal kitchen with white beadboard, a window onto grey sky, a rack of enamel mugs and a jar of wooden spoons on the sill',
     "coz_c": 'white beadboard kitchen',
     "sup_a": 'a scrubbed wood counter',
     "sup": 'counter',
     "trajes": [
         ('%s striped crop top with a wide neckline and short shorts',
          'striped crop top'),
         ('%s low-cut linen tank with a short skirt',
          'linen tank'),
         ('%s halter top tied at the neck with cut-off shorts',
          'tied halter'),
         ('%s short wrap dress with a deep neckline',
          'short wrap dress'),
     ],
     "cores": ['navy', 'white', 'seafoam', 'brick red', 'black', 'coral'],
     "luz_e": 'Soft coastal daylight, slightly grey.',
     "luz_e_c": 'soft coastal daylight',
     "luz": 'Cool even light from a north window.',
     "luz_c": 'cool north light',
     "audio": 'gulls far off, wind in a hedge, quiet room tone'},

    {"id": "vegas", "eua": True, "selo": "N", "familia": "nevada",
     "etnias": ['Hispanic American', 'white American', 'Black American'],
     "var": 'the front patio of a desert stucco house, gravel landscaping with two palms and low mountains on the horizon',
     "var_c": 'desert stucco patio',
     "coz": 'a modern kitchen with grey cabinets and a mirrored splashback, recessed lights, a glass jug on the island',
     "coz_c": 'grey modern kitchen',
     "sup_a": 'a quartz island',
     "sup": 'island',
     "trajes": [
         ('%s sequined crop top with a very short skirt',
          'sequined crop top'),
         ('%s deep-plunge bodysuit with high-cut shorts',
          'deep-plunge bodysuit'),
         ('%s halter mini dress with an open back',
          'halter mini dress'),
         ('%s satin bralette top under an open blazer, with a mini skirt',
          'satin bralette top'),
     ],
     "cores": ['black', 'gold', 'hot pink', 'silver', 'scarlet', 'white'],
     "luz_e": 'Harsh dry sunlight, deep shadow under the eave.',
     "luz_e_c": 'harsh dry sunlight',
     "luz": 'Even recessed lighting with daylight from the door.',
     "luz_c": 'even recessed light',
     "audio": 'air conditioning humming, quiet room tone'},

    {"id": "pacifico", "eua": True, "selo": "N", "familia": "noroeste",
     "etnias": ['white American', 'Asian American'],
     "var": 'the covered porch of a Pacific Northwest house, cedar shingles damp with rain, moss on the rail and tall firs behind',
     "var_c": 'cedar-shingle porch',
     "coz": 'a warm kitchen with dark green cabinets, a kettle steaming, herbs drying on a string across the window',
     "coz_c": 'dark-green cabinet kitchen',
     "sup_a": 'a wide fir counter',
     "sup": 'counter',
     "trajes": [
         ('%s ribbed thermal top pulled low off one shoulder with short shorts',
          'off-shoulder thermal'),
         ('%s low-cut knit tank with a short skirt',
          'low-cut knit tank'),
         ('%s cropped zip fleece worn half open over a bralette, with a mini skirt',
          'half-open fleece'),
         ('%s slip dress cut short with thin straps',
          'short slip dress'),
     ],
     "cores": ['forest green', 'cream', 'black', 'rust red', 'white', 'charcoal'],
     "luz_e": 'Flat wet daylight, everything slightly damp.',
     "luz_e_c": 'flat wet daylight',
     "luz": 'Soft grey daylight through a rain-flecked window.',
     "luz_c": 'soft rain-flecked light',
     "audio": 'light rain on a roof, quiet room tone'},

    # ⭐⭐ + 2026-08-13 — OITO CASAS NOVAS, ordem do operador: *"aumente o pool
    # de opcoes substancialmente, tambem dos ambientes"*. 16 -> 24, e as
    # familias vao de 13 para 21.
    # ⛔ CADA ENTRADA DECLARA AS DEZOITO CHAVES DAS DEZESSEIS DE CIMA — `eua`,
    # `selo`, `familia`, `etnias`, `var`, `var_c`, `coz`, `coz_c`, `sup_a`,
    # `sup`, `trajes` (quatro), `cores` (seis), `luz_e`, `luz_e_c`, `luz`,
    # `luz_c`, `audio`. Chave faltando aqui nao e' pool menor: e' KeyError na
    # mao do operador, porque a montagem le' todas.
    # ⛔⛔ E CADA UMA E' A CASA INTEIRA, nao um fundo: varanda E cozinha da MESMA
    # casa, as duas luzes, as duas versoes curtas e a ambiencia. E' o unico
    # angulo do parque com corte de ambiente dentro do video, e por isso varanda
    # e cozinha sao UM eixo so'.
    # ⭐ COBERTURA DE ETNIA — nenhuma encolheu, todas cresceram: `white
    # American` 13 -> 20 casas, `Black American` 9 -> 13, `Hispanic American`
    # 7 -> 10 e `Asian American`, que era a mais magra do pool com UMA casa so'
    # (o pacifico), passa a ter TRES (havai e baia). Etnia com uma casa so' e'
    # etnia que sempre sai no mesmo cenario.
    # ⚠️ Zero etnia NOVA de proposito: o motor classifica pele por lista
    # explicita (`PELE_ETNIAS`), e string nova entraria como neutra — visivel
    # so' com a pele livre, invisivel nas duas travas do painel.
    # ⭐ O TRAJE CONTINUA SENDO A BULLET DE RETENCAO (ordem do operador):
    # decote, saia curta, pernas em quadro. As 32 pecas novas seguem o registro
    # das 64 de cima, e nenhuma repete o nome curto de outra.
    {"id": "kansas", "eua": True, "selo": "N", "familia": "planicies",
     "etnias": ['white American', 'Black American'],
     "var": 'the front porch of a plains farmhouse, a white-painted rail and a windbreak of cottonwoods behind, flat wheat country to the horizon',
     "var_c": 'plains farmhouse porch',
     "coz": 'a farm kitchen with painted cabinets and a deep enamel sink under a window onto open fields, jars of preserves on a shelf',
     "coz_c": 'painted farm kitchen',
     "sup_a": 'a wide oak worktop',
     "sup": 'worktop',
     "trajes": [
         ('%s cropped chambray shirt knotted under the bust with very short denim cut-offs',
          'knotted chambray shirt'),
         ('%s deep-scoop bodysuit tucked into a short flared skirt',
          'deep-scoop bodysuit'),
         ('%s thin-strap sundress cut well above the knee',
          'thin-strap sundress'),
         ('%s low-cut ribbed tank with high-waisted short shorts',
          'high-waisted tank'),
     ],
     "cores": ['wheat gold', 'white', 'denim blue', 'brick red', 'black', 'cream'],
     "luz_e": 'Wide flat prairie daylight under the porch roof.',
     "luz_e_c": 'flat prairie daylight',
     "luz": 'Even daylight through a tall farm window.',
     "luz_c": 'even farm-window light',
     "audio": 'wind across open wheat, a grain truck far off, quiet room tone'},

    {"id": "baltimore", "eua": True, "selo": "N", "familia": "meio_atlantico",
     "etnias": ['Black American', 'white American'],
     "var": 'the marble front steps of a Baltimore row house, painted brick and a screen door behind, a run of identical stoops down the block',
     "var_c": 'marble row-house steps',
     "coz": 'a narrow row-house kitchen with white cabinets and a checkerboard floor, a window onto a small back yard, a spice rack by the stove',
     "coz_c": 'checkerboard row-house kitchen',
     "sup_a": 'a laminate galley counter',
     "sup": 'counter',
     "trajes": [
         ('%s fitted rib tank with a very low front, worn with a short wrap skirt',
          'low-front rib tank'),
         ('%s halter top knotted at the back with high-cut denim shorts',
          'back-knot halter'),
         ('%s cropped bomber worn open over a bralette, with a mini skirt',
          'open cropped bomber'),
         ('%s plunging jersey mini dress with thin straps',
          'plunging jersey mini'),
     ],
     "cores": ['black', 'white', 'plum', 'gold', 'royal blue', 'scarlet'],
     "luz_e": 'Bright flat daylight bouncing off the brick.',
     "luz_e_c": 'flat brick daylight',
     "luz": 'Warm daylight through a small back window.',
     "luz_c": 'warm back-window light',
     "audio": 'a bus braking two blocks away, quiet room tone'},

    {"id": "havai", "eua": True, "selo": "N", "familia": "havai",
     "etnias": ['Asian American', 'white American'],
     "var": 'the lanai of a plantation-style island house, wide eaves and screened panels behind, plumeria and ti plants crowding the rail',
     "var_c": 'plantation lanai',
     "coz": 'an airy island kitchen with louvred cabinets, a wide window onto broad green leaves, glass jars in a row on the sill',
     "coz_c": 'louvred island kitchen',
     "sup_a": 'a koa wood counter',
     "sup": 'counter',
     "trajes": [
         ('%s tied halter bikini top under an open shirt, with a very short sarong skirt',
          'tied halter top'),
         ('%s cropped tube top with a short wrap skirt',
          'cropped tube top'),
         ('%s deep-V romper cut short at the thigh',
          'deep-V romper'),
         ('%s single-shoulder knit top with high-cut shorts',
          'single-shoulder knit'),
     ],
     "cores": ['white', 'hibiscus red', 'turquoise', 'sun yellow', 'black', 'cream'],
     "luz_e": 'Soft trade-wind daylight under the deep eaves.',
     "luz_e_c": 'soft lanai daylight',
     "luz": 'Bright even daylight through a louvred window.',
     "luz_c": 'bright louvred light',
     "audio": 'wind in broad leaves, a rooster far off, quiet room tone'},

    {"id": "baia", "eua": True, "selo": "N", "familia": "baia",
     "etnias": ['Asian American', 'Hispanic American'],
     "var": 'the front steps of a San Francisco Victorian, bay windows and painted trim above, a grey street falling away behind',
     "var_c": 'painted Victorian steps',
     "coz": 'a narrow flat kitchen with glass-front cabinets, a window onto a light well, herbs in tins along the sill',
     "coz_c": 'glass-front flat kitchen',
     "sup_a": 'a soapstone counter',
     "sup": 'counter',
     "trajes": [
         ('%s ribbed knit crop with a wide boat neck pulled off one shoulder, with a mini skirt',
          'boat-neck crop'),
         ('%s slip camisole under a cropped blazer, with short shorts',
          'slip camisole'),
         ('%s low-back halter dress cut short above the knee',
          'low-back halter dress'),
         ('%s zip-front knit top worn half open with a short pleated skirt',
          'half-open knit top'),
     ],
     "cores": ['charcoal', 'white', 'emerald', 'dusty rose', 'burgundy', 'pale grey'],
     "luz_e": 'Cool even light through coastal fog.',
     "luz_e_c": 'cool fog light',
     "luz": 'Soft grey daylight from the light well.',
     "luz_c": 'soft light-well daylight',
     "audio": 'a cable car bell far off, quiet room tone'},

    {"id": "colorado", "eua": True, "selo": "N", "familia": "montanhas",
     "etnias": ['white American', 'Hispanic American'],
     "var": 'the timber porch of a Colorado mountain house, log posts and a split-rail fence, snow-tipped peaks beyond the pines',
     "var_c": 'timber mountain porch',
     "coz": 'a lodge kitchen with pine cabinets and a stone chimney breast, a window onto tall firs, enamel mugs hanging on hooks',
     "coz_c": 'pine lodge kitchen',
     "sup_a": 'a thick slab counter',
     "sup": 'counter',
     "trajes": [
         ('%s cropped puffer vest worn open over a low-cut tank, with short shorts',
          'open puffer vest'),
         ('%s ribbed long-sleeve crop with a deep V and a mini skirt',
          'deep-V long-sleeve crop'),
         ('%s wool wrap top tied at the waist with very short cut-offs',
          'wool wrap top'),
         ('%s thermal henley unbuttoned low, tucked into a short skirt',
          'unbuttoned henley'),
     ],
     "cores": ['forest green', 'cream', 'rust red', 'denim blue', 'black', 'white'],
     "luz_e": 'Thin bright mountain daylight in the porch shade.',
     "luz_e_c": 'thin mountain daylight',
     "luz": 'Clear high-altitude daylight from a tall window.',
     "luz_c": 'clear high window light',
     "audio": 'wind in pines, a raven far off, quiet room tone'},

    {"id": "novo_mexico", "eua": True, "selo": "N", "familia": "novo_mexico",
     "etnias": ['Hispanic American', 'white American'],
     "var": 'the portal of an adobe house, carved wooden corbels overhead, strings of dried red chiles on the posts and mesa country beyond',
     "var_c": 'adobe portal',
     "coz": 'an adobe kitchen with a rounded corner fireplace, hand-painted tiles behind the stove and clay bowls stacked on open shelves',
     "coz_c": 'adobe corner-fireplace kitchen',
     "sup_a": 'a thick plastered ledge',
     "sup": 'ledge',
     "trajes": [
         ('%s embroidered off-shoulder blouse pulled low, with a very short skirt',
          'embroidered off-shoulder blouse'),
         ('%s crossover crop top with high-waisted denim shorts',
          'crossover crop top'),
         ('%s tiered mini dress with a deep square neckline',
          'square-neck mini dress'),
         ('%s knit shawl worn open over a bralette, with short shorts',
          'open knit shawl'),
     ],
     "cores": ['turquoise', 'terracotta', 'white', 'black', 'silver', 'scarlet'],
     "luz_e": 'Warm light bounced off the adobe wall.',
     "luz_e_c": 'warm adobe light',
     "luz": 'Soft light from a deep window recess.',
     "luz_c": 'soft recessed daylight',
     "audio": 'dry wind, a magpie somewhere, quiet room tone'},

    {"id": "alabama", "eua": True, "selo": "N", "familia": "sul_profundo",
     "etnias": ['Black American', 'white American'],
     "var": 'the swept front porch of an Alabama farmhouse, a porch swing on chains and pots of caladiums on the boards, open fields beyond the fence',
     "var_c": 'swept farmhouse porch',
     "coz": 'a country kitchen with yellow-painted cabinets, a screen door onto the yard and a row of mason jars along the window',
     "coz_c": 'yellow country kitchen',
     "sup_a": 'a scrubbed oak table',
     "sup": 'table',
     "trajes": [
         ('%s gingham crop top tied in front with very short shorts',
          'gingham crop top'),
         ('%s smocked bandeau dress cut short at the thigh',
          'smocked bandeau dress'),
         ('%s sleeveless button-down opened to the waist over a bralette, with a mini skirt',
          'opened button-down'),
         ('%s eyelet cami with a low neckline and a short flared skirt',
          'eyelet cami'),
     ],
     "cores": ['sunflower yellow', 'white', 'red', 'denim blue', 'black', 'sage green'],
     "luz_e": 'Hot southern daylight softened by the porch roof.',
     "luz_e_c": 'soft southern porch light',
     "luz": 'Bright daylight through the screen door.',
     "luz_c": 'bright screen-door light',
     "audio": 'cicadas in the field, a dog on a chain far off, quiet room tone'},

    {"id": "minnesota", "eua": True, "selo": "N", "familia": "lagos",
     "etnias": ['white American', 'Black American'],
     "var": 'the screened porch of a northern lake cabin, birch trunks and a wooden dock behind, flat water past the trees',
     "var_c": 'screened lake porch',
     "coz": 'a cabin kitchen with knotty-pine walls and a red enamel stove, a window onto the water and tin canisters on a shelf',
     "coz_c": 'red-stove cabin kitchen',
     "sup_a": 'a birch plank counter',
     "sup": 'counter',
     "trajes": [
         ('%s cropped fleece pullover worn off one shoulder with very short shorts',
          'off-shoulder fleece'),
         ('%s lace-edge bralette top under an open flannel, with a mini skirt',
          'lace-edge bralette top'),
         ('%s scoop-back knit dress cut short above the knee',
          'scoop-back knit dress'),
         ('%s cropped waffle top with a deep neckline and short cut-offs',
          'cropped waffle top'),
     ],
     "cores": ['pine green', 'white', 'red', 'slate blue', 'cream', 'black'],
     "luz_e": 'Clean northern daylight bouncing off the lake.',
     "luz_e_c": 'clean lake daylight',
     "luz": 'Bright even light from a window over the water.',
     "luz_c": 'bright lake-window light',
     "audio": 'a loon far off, water at the dock, quiet room tone'},

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
# ⭐⭐ CENA 1, BEAT 1 — A DESPEDIDA. Forma da fonte, literal em 0:00:
# *"Say goodbye to a soft Johnson and poor blood flow."*
# ⛔ A construcao e' DESPEDIDA + PAR (estado do orgao, o que o causa). O segundo
# termo NAO e' enfeite: sem ele a frase promete o fim de um sintoma e nao diz de
# que ele vem, e o espectador nao tem o que ligar a' receita que vem depois.
DESPEDIDAS = [
    "Say goodbye to a soft {o} and poor blood flow",
    "Say goodbye to a soft {o} and the blood that stopped reaching it",
    "Say goodbye to a tired {o} and weak circulation",
    "Wave goodbye to a soft {o} and the blood flow that quit",
    "Say goodbye to a quiet {o} and the circulation behind it",
    "Say goodbye to a soft {o} and the poor flow under it",
    "Kiss goodbye a soft {o} and slow blood flow",
    "Say goodbye to a sleepy {o} and the blood that never gets there",
    "Say goodbye to a limp {o} and the circulation that failed it",
    "Say goodbye to a soft {o} and the blood flow you lost",
    "Say goodbye to a cold {o} and the flow that dried up",
    "Say goodbye to a weak {o} and the blood that goes everywhere else",
    "Say goodbye to a soft {o} and mornings with nothing there",
    "Say goodbye to a dead {o} and the circulation that killed it",
    "Say goodbye to a soft {o} and the pressure you stopped feeling",
    "Say goodbye to a slow {o} and the blood flow that gave out",
]

# ⭐ CENA 1, BEAT 2 — A CANECA. Fonte, 0:03: *"One single cup can help support
# healthy circulation where it matters most."*
# ⛔ `where it matters most` e' a ofuscacao que o funil exige — ofusca-se a
# PALAVRA, nunca o SENTIDO. A caneca esta' estendida na lente enquanto ela diz
# isso: a imagem entrega o referente que a frase nao nomeia.
CANECAS = [
    "One single cup can help support healthy circulation where it matters most",
    "One cup a day supports the circulation where you want it most",
    "A single cup helps the blood get where it matters most",
    "One cup like this supports healthy flow right where you need it",
    "This one cup can bring the circulation back where it counts",
    "One single cup a day, and the blood goes where it matters",
    "A cup of this helps push healthy flow where it matters most",
    "One cup every day supports the circulation down there",
    # ⛔ Aqui esteve "This single cup helps the blood reach where it stopped
    # reaching" — reprovada pelo `medir_contexto_copy` (familia A) e com razao:
    # o `it` volta para "the blood", e a frase diz que o sangue chega onde o
    # sangue parou de chegar. Circulo fechado, referente nenhum. O conserto poe
    # ELE como referente: e' o corpo dele que parou de sentir.
    "This single cup gets the blood back down there where you stopped feeling it",
    "One cup can support healthy circulation exactly where you want it",
    "A single cup a day sends the flow where it belongs",
    "One cup of this supports the blood flow where it counts most",
]

# ⭐⭐ CENA 2 — A RECEITA. Fonte, 0:06: *"Cut three lemons, add a piece of fresh
# ginger, and one clove of garlic."*
# ⭐ O RARO entra aqui, com o APOSTO — ordem do operador: *"no take 2 de prep
# receita pode incluir o pool com aqueles ingredientes fodas"*. O aposto e' lei
# do repo (`maca root, that Andean root from Peru`), nunca o nome cientifico.
# ⭐⭐ CENA 2 — A RECEITA. Fonte, 0:06: *"Cut three lemons, add a piece of fresh
# ginger, and one clove of garlic."*
# ⭐ O RARO entra aqui, com o APOSTO — ordem do operador: *"no take 2 de prep
# receita pode incluir o pool com aqueles ingredientes fodas"*. O aposto e' lei
# do repo (`maca root, that Andean root from Peru`), nunca o nome cientifico.
#
# ⛔⛔ AS CURTAS EXISTEM PARA O SEGREDO CABER. Em 2026-08-06 o operador leu o
# TAKE e apontou que o `gelatin trick` estava coadjuvante; o conserto foi dar 6-9
# palavras ao SEGREDO, e elas saem daqui. Por isso metade das entradas larga o
# alho ou comprime as medidas — o proprio operador escreveu o exemplo dele sem o
# alho. ⚠️ O quadro mostra os limoes, o gengibre E o alho na bancada, entao a
# fala pode omitir um deles sem contradizer a imagem; o que ela NAO pode omitir
# e' o segredo, que so' existe na fala.
RECEITAS = [
    "Three lemons, fresh ginger, and {r}",
    "Cut three lemons, add ginger, and {r}",
    "Three cut lemons, ginger, garlic, and {r}",
    "Cut three lemons, ginger and garlic, then {r}",
    "Three lemons, a piece of ginger, and {r}",
    "Cut three lemons in, add ginger, and {r}",
    "Three lemons cut open, fresh ginger, and {r}",
    "Cut three lemons, drop in ginger and {r}",
    "Three lemons, ginger, one clove of garlic, and {r}",
    "Cut three lemons open, add ginger and {r}",
]

# ⭐ CENA 2, FECHO — a fervura. Fonte, 0:11: *"Then let it boil for 10 minutes."*
FERVURAS = [
    "Let it boil ten minutes",
    "Boil it ten minutes",
    "Then let it boil for ten minutes",
    "Let that boil ten minutes",
    "Boil the lot for ten minutes",
    "Then boil it ten minutes",
    "Let it come to a boil for ten minutes",
    "Boil it down for ten minutes",
]

# ⭐⭐ O SEGREDO GUARDADO — carrega o literal `gelatin trick`, intocavel.
# ⛔ E' aqui que a congruencia com a VSL mora: o mecanismo que o criativo promete
# tem de ser o que a pagina vende. A fonte guarda "the extra ingredient I like to
# add" para o DM; nos guardamos o mesmo lugar, com o nosso mecanismo no lugar.
# ⭐⭐ O SEGREDO E' A REVELACAO, NAO O ULTIMO ITEM DA LISTA.
# Ordem do operador, 2026-08-06, lendo o TAKE 02 renderizado: o `gelatin trick`
# saia como *"...garlic, and ginkgo, ... and one gelatin trick"* — item N de uma
# enumeracao, com o mesmo peso do alho. A forma que ele pediu poe uma PAUSA e um
# ROTULO antes do nome: *"and... the secret: THE GELATIN TRICK."*
#
# ⛔ TODA ENTRADA TEM AS TRES PARTES, nesta ordem:
#   1. a CONJUNCAO que separa da lista (`and`, `plus`, `then`);
#   2. o ROTULO que anuncia hierarquia (`the secret`, `the one thing`, `the
#      part nobody sells`) seguido de DOIS PONTOS;
#   3. o LITERAL `the gelatin trick`, intocavel.
# Sem o rotulo, o trick volta a ser alho. E' o rotulo que faz o espectador
# entender que o que vem depois nao e' ingrediente — e' o mecanismo.
#
# ⚠️ CUSTAM 6-9 PALAVRAS, contra as 4 da versao anterior. O espaco sai da
# RECEITA, e sai de la' de proposito: o quadro da cena 2 JA' MOSTRA os limoes, o
# gengibre e o alho. O que o quadro nao mostra — e por isso a fala tem de
# carregar — e' o segredo.
SEGREDOS = [
    "and the secret: the gelatin trick",
    "plus the secret: the gelatin trick",
    "and then the secret: the gelatin trick",
    "and the one thing nobody sells: the gelatin trick",
    "plus the part I hold back: the gelatin trick",
    "and the real secret: the gelatin trick",
    "and the one step nobody posts: the gelatin trick",
    "plus my grandmother's secret: the gelatin trick",
    "and the last thing: the gelatin trick",
    "and the piece nobody tells you: the gelatin trick",
    "plus the one I never post: the gelatin trick",
    "and here is the secret: the gelatin trick",
    "and the part that does it: the gelatin trick",
    "plus the quiet one: the gelatin trick",
]

# ⭐⭐ CENA 3 — O USO. Fonte, 0:13: *"Drink one cup every single morning and wake
# up feeling like a man again."*
# ⛔ O USO NOMEIA O ORGAO. Sem ele a frase promete "se sentir bem" e o espectador
# nao sabe do que se trata — e' o gate do `medir_contexto_copy`.
USOS = [
    # ⛔⛔ AS OITO CURTAS (7-9 palavras) EXISTEM POR MEDICAO. Com o pool so' de
    # entradas longas, a cena 3 saia com **5 falas distintas em 600 videos**: o
    # piso da cena (uso 10 + `Comment gelatin,` 2 + `and I'll send you` 4 + isca
    # 2 + gate 7) dava exatamente 25 contra um teto de 25, entao so' o combo
    # minimo cabia e o sorteio nao tinha o que sortear. Cena encostada no teto
    # nao tem repertorio — e' mode-collapse por construcao, justamente o que o
    # randomizador existe para impedir.
    # ⚠️ Curta NAO quer dizer vaga: cada uma continua nomeando o ORGAO e dizendo
    # O QUE ACONTECE com ele. Encurtar cortando a funcao seria trocar um defeito
    # medido por um defeito pior.
    "One cup a day and your {o} answers.",
    "A cup each morning and your {o} wakes.",
    "Drink it daily and your {o} comes back.",
    "One cup a morning and your {o} holds.",
    "Drink it warm and your {o} feels it.",
    "A cup a day and your {o} stands again.",
    "One cup and your {o} stops going quiet.",
    "Drink it each morning and your {o} follows.",
    "Drink one cup every single morning and your {o} wakes up with you.",
    "One cup every morning, and your {o} is what you notice first.",
    "Drink a cup each morning and wake up with your {o} already up.",
    "One cup every single morning and your {o} answers again.",
    "Drink it every morning and your {o} comes back to what it was.",
    "A cup each morning, and your {o} stops letting you down.",
    "Drink one cup daily and your {o} holds like it used to.",
    "One cup in the morning and your {o} is awake before you are.",
    "Drink it warm each morning and your {o} feels it by the week.",
    "One cup a day, and your {o} shows up for her again.",
    "Drink a cup every morning and your {o} does the rest.",
    "One single cup a day and your {o} stops going quiet.",
    "Drink it first thing and your {o} gets the blood it lost.",
    "A cup every morning, and your {o} is the first thing she notices.",
    "Drink one cup daily and your {o} stands like it did at twenty.",
    "One cup each morning and your {o} never leaves you waiting.",
]

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
# ⭐⭐ REFS ESTILO TOP MODEL — ordem do operador para ESTE agente: *"a ref
# mulher tem que ser extremamente linda e com um corpo muito atrativo"*. E'
# o mesmo pool do DUPLA/PLACA: 30 entradas, CINCO ruivas de tons diferentes
# (auburn, copper, ginger, dark red, mahogany) — ruiva nao e' uma cor so'.
# ⛔ Cada uma varia CORPO, CABECA e MARCA juntos. Duas mulheres de cabelo
# diferente e mesmo porte leem como a mesma pessoa (medir_personagens).
REFS = [
    {"idade": 24, "corpo": 'tall and long-legged with a very small waist',
     "cabeca": 'deep auburn hair falling in loose waves past her shoulders',
     "marca": 'a light spray of freckles across her nose and green eyes'},
    {"idade": 27, "corpo": 'slim with an hourglass figure and long legs',
     "cabeca": 'copper-red hair in a high glossy ponytail',
     "marca": 'pale green eyes and a small beauty mark above her lip'},
    {"idade": 23, "corpo": 'willowy and fine-boned with a flat stomach',
     "cabeca": 'bright ginger hair cut in long layers',
     "marca": 'heavy freckling across her cheeks and hazel eyes'},
    {"idade": 29, "corpo": 'curvy with a narrow waist and full shoulders',
     "cabeca": 'dark red hair swept over one shoulder',
     "marca": 'a small gold hoop in her left nostril and clear skin'},
    {"idade": 26, "corpo": 'tall and statuesque with a long waist',
     "cabeca": 'strawberry-blonde hair in a loose braid',
     "marca": 'wide-set blue eyes and a deep dimple in her right cheek'},
    {"idade": 25, "corpo": "slim and toned with a dancer's line",
     "cabeca": 'jet-black hair in a sleek centre part',
     "marca": 'sharp cheekbones and a small mole on her jaw'},
    {"idade": 28, "corpo": 'long-legged and slender with square shoulders',
     "cabeca": 'platinum blonde hair in a blunt shoulder-length cut',
     "marca": 'ice-blue eyes and a dimple in one cheek'},
    {"idade": 24, "corpo": 'curvy and athletic with a small waist',
     "cabeca": 'tight dark curls gathered high on her head',
     "marca": 'a wide bright smile and a small beauty mark on her left temple'},
    {"idade": 30, "corpo": 'tall and slim with an hourglass line',
     "cabeca": 'chestnut hair in long beachy waves',
     "marca": "a pronounced Cupid's bow and warm brown eyes"},
    {"idade": 22, "corpo": 'petite and curvy with a defined waist',
     "cabeca": 'honey-blonde hair in a high messy bun',
     "marca": 'a scatter of freckles and full lips'},
    {"idade": 27, "corpo": 'lean and toned with a flat stomach and long arms',
     "cabeca": 'long jet-black hair worn straight to the waist',
     "marca": 'almond eyes and a small stud in one nostril'},
    {"idade": 26, "corpo": 'shapely with toned arms and a narrow waist',
     "cabeca": 'caramel balayage falling past her shoulders',
     "marca": 'a beauty mark at the corner of her right eye'},
    {"idade": 23, "corpo": 'slim-hipped and elegant with a long neck',
     "cabeca": 'sandy blonde hair in a fishtail braid',
     "marca": 'a slight overbite that shows when she smiles'},
    {"idade": 31, "corpo": 'curvy and strong with a small waist',
     "cabeca": 'long box braids gathered over one shoulder',
     "marca": 'high round cheekbones and a gold nose ring'},
    {"idade": 25, "corpo": "tall and lean with swimmer's shoulders",
     "cabeca": 'auburn hair in a low glossy ponytail',
     "marca": 'dark freckles across both cheeks and grey eyes'},
    {"idade": 28, "corpo": 'softly curvy with a full figure and a narrow waist',
     "cabeca": 'dark brown hair in heavy waves with a deep side part',
     "marca": 'a small raised birthmark on her temple'},
    {"idade": 24, "corpo": 'slim and supple with a very straight back',
     "cabeca": 'copper hair cropped into a long bob',
     "marca": 'heavy freckling over her nose and bright green eyes'},
    {"idade": 29, "corpo": 'long-limbed and shapely with a defined waist',
     "cabeca": 'black hair in a high sleek ponytail',
     "marca": 'a sharply defined jawline and full brows'},
    {"idade": 26, "corpo": 'trim and athletic with a flat stomach',
     "cabeca": 'golden blonde hair in loose waves',
     "marca": 'a small dimple in one cheek only'},
    {"idade": 22, "corpo": 'tall and willowy with narrow hips',
     "cabeca": 'dark auburn hair in a half-up twist',
     "marca": 'wide hazel eyes and a light dusting of freckles'},
    {"idade": 30, "corpo": 'curvy with a small waist and long legs',
     "cabeca": 'tight coils cropped close to the head',
     "marca": 'sculpted cheekbones and a small gold stud'},
    {"idade": 27, "corpo": 'slim with a long waist and square shoulders',
     "cabeca": 'ash-brown hair in a sleek low bun',
     "marca": 'grey-green eyes and a small beauty mark above her left brow'},
    {"idade": 25, "corpo": 'shapely and toned with a narrow waist',
     "cabeca": 'ginger hair in loose curls past her shoulders',
     "marca": 'heavy freckling and a small chin dimple'},
    {"idade": 28, "corpo": 'tall and slim with a graceful neck',
     "cabeca": 'long dark hair in a high crown braid',
     "marca": 'a beauty mark high on her left cheek'},
    {"idade": 23, "corpo": 'petite and shapely with a defined waist',
     "cabeca": 'bleached blonde hair in a blunt chin-length bob',
     "marca": 'wide dark eyes and a shallow cleft in her chin'},
    {"idade": 31, "corpo": 'athletic and curvy with strong shoulders',
     "cabeca": 'long waves in a rich mahogany red',
     "marca": 'clear skin and a small hoop in her right nostril'},
    {"idade": 24, "corpo": 'long-legged and lean with a flat stomach',
     "cabeca": 'dark brown hair in a slicked-back ponytail',
     "marca": 'sharp brows and a small mole under one eye'},
    {"idade": 26, "corpo": 'curvy and confident with a very narrow waist',
     "cabeca": 'honey-red hair falling in soft waves',
     "marca": 'a dense spray of freckles across her nose'},
    {"idade": 29, "corpo": 'slim and elegant with long arms',
     "cabeca": 'black hair in a smooth shoulder-length cut',
     "marca": 'a thin white streak at her temple and dark eyes'},
    {"idade": 25, "corpo": 'tall with a small waist and full shoulders',
     "cabeca": 'strawberry-blonde hair in a high loose bun',
     "marca": 'green eyes and a small beauty spot on her cheekbone'},
    # ⭐⭐ + 2026-08-13 — OITO BOTICARIAS NOVAS, ordem do operador: *"melhore a
    # aparencia e shape desses homens"* / *"aumente o pool de opcoes
    # substancialmente"*. 30 -> 38.
    # ⛔ SETE ENTRADAS ACIMA FORAM REESCRITAS NO MESMO DIA e o motivo fica
    # escrito: quatro traziam CICATRIZ (`a faint scar through one eyebrow`, `a
    # thin scar along her jawline`, `a faint scar on her chin`), uma trazia
    # DENTE (`a gap between her front teeth` — a mesma armadilha que o CLEAN
    # pagou com foto de campo no CL25), uma trazia VINCO (`a faint mark between
    # her brows`, que o gerador desenha como ruga de testa franzida) e DUAS
    # traziam COR DE PELE (`glowing deep brown skin`, `pale skin`). As duas
    # ultimas violavam a regra do proprio bloco tres linhas acima — a etnia sai
    # do MUNDO e e' injetada pela montagem; dizer a cor aqui poe duas vozes no
    # mesmo sintagma e o gerador resolve inventando um rosto mestico.
    # ⛔ Nas oito novas: zero oculos, zero grisalho, zero cor de pele, zero
    # palavra de deterioracao e zero negacao de conformidade. A ancora e' sempre
    # SINAL DE BELEZA e sempre permanente (covinha, sarda, malar, argola,
    # beleza-marca, arco do labio, fenda no queixo) — sem ela o Veo troca de
    # rosto entre a varanda e a cozinha, que sao dois blocos gerados separados.
    # ⚠️ CORPO, CABECA e MARCA giram JUNTOS nas oito: duas mulheres de cabelo
    # diferente e mesmo porte leem como a mesma pessoa (medir_personagens).
    {"idade": 24, "corpo": 'tall and full-figured with a very small waist',
     "cabeca": 'jet-black hair worn to the waist with blunt bangs',
     "marca": 'a deep dimple in her left cheek only'},
    {"idade": 28, "corpo": 'lean and long-necked with narrow shoulders and long legs',
     "cabeca": 'warm brown hair gathered into a high top knot',
     "marca": 'wide-set amber eyes and full arched brows'},
    {"idade": 23, "corpo": 'hourglass-shaped with a full bust and a cinched waist',
     "cabeca": 'cherry-red hair in a long shag with curtain bangs',
     "marca": 'a small gold hoop high in her right ear'},
    {"idade": 27, "corpo": 'slender and high-waisted with long straight legs',
     "cabeca": 'icy blonde hair in a single braid down her back',
     "marca": "a pronounced Cupid's bow and a wide even smile"},
    {"idade": 30, "corpo": 'curvy through the hip with a flat stomach and a small waist',
     "cabeca": 'long senegalese twists gathered high on her head',
     "marca": 'a beauty mark at the centre of her right cheek'},
    {"idade": 26, "corpo": 'tall and broad-shouldered with a long lean line',
     "cabeca": 'bronde balayage swept over in a deep side part',
     "marca": 'grey-blue eyes ringed darker at the edge'},
    {"idade": 22, "corpo": 'petite and hourglass with a very narrow waist',
     "cabeca": 'black hair in a wet-look chin-length bob',
     "marca": 'a small silver stud in her left ear and a wide smile'},
    {"idade": 29, "corpo": 'strong and graceful with a long straight back and full shoulders',
     "cabeca": 'espresso-brown hair in a long low ponytail with a middle part',
     "marca": "a widow's peak at her hairline and a heart-shaped face"},
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


# ⚠️ O fecho vem depois do aposto do raro, entao a virgula ANTES dele mora na
# montagem (`%s, %s`), nunca aqui — senao o aposto fica sem fechar.

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
    # ⛔ AS CURTAS (4-6 palavras) sao o beat que CEDE quando o teto aperta — o
    # `Comment gelatin,` e o USO sao lei do repo e nao encolhem. ⚠️ Nenhuma
    # abandona a RAZAO: `follow me` sozinho e' ordem sem motivo, e motivo e' o
    # que faz alguem clicar.
    "Follow me, or I cannot find you.",
    "Follow first, or I cannot answer.",
    "Follow me, or it never reaches me.",
    "Follow first, or I cannot send it.",
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

# ⛔ SO' OS EIXOS QUE ESTE MOTOR SORTEIA. `homem`, `prop`, `substancia` e
# `metodo` estavam aqui por heranca do BOTICA — o cadeado apareceria na UI e nao
# travaria nada, porque nao ha' o que travar. Botao que mente e' pior que botao
# ausente: o operador confia nele.
EIXOS_TRAVAVEIS = ["mundo", "etnia", "ref", "comum", "raro", "cor", "traje"]


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
    ("mundo", "A CASA (varanda + cozinha)", "MUNDOS", "id"),
    ("etnia", "ETNIA", "etnias_do_mundo", None),
    ("ref", "A REF", "REFS", "cabeca"),
    # ⭐ O TRAJE E' O EIXO MAIS IMPORTANTE DESTE AGENTE — e' a bullet de
    # retencao do hook, por ordem do operador. Logo abaixo da REF de proposito.
    ("traje", "O TRAJE (a retencao)", "trajes_do_mundo", None),
    ("comum", "O COMUM", "COMUNS", "nome"),
    ("raro", "O RARO", "RAROS", "nome"),
]

CENAS_UI = ["1 · varanda: a caneca na lente", "2 · cozinha: a receita",
            "3 · a caneca + CTA"]


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
    operador pode ter travado um traje e depois trocado de mundo, e travar um
    traje de Miami num mundo dos Apalaches nao pode derrubar o sorteio.

    ⛔⛔ ACEITA TUPLA. A `ui_agente.travas()` devolve o VALOR QUE ESTA' NA TELA,
    e o valor na tela e' a TUPLA `(template, curto)` — nao o curto. Com esta
    funcao aceitando so' string, o cadeado do traje APARECIA e nao segurava:
    a comparacao `x[1] == ('...', 'knit cowl halter')` nunca dava verdade e o
    fallback devolvia o primeiro traje do mundo, calado.
    ⚠️ Botao que mente e' pior que botao ausente — o operador confia nele. Foi
    por isso que o cadeado passou a ser MEDIDO (30 sorteios por eixo) e nao
    declarado; medindo, este apareceu na hora. Declarando, teria ido para o
    .exe.
    """
    if isinstance(curto, (tuple, list)):
        # ⭐⭐ TRAVA EXPLICITA VENCE O MUNDO — e isto diverge do BOTICA de
        # proposito. La' o traje e' ETNICO (vestido amish, sari, huipil) e
        # arrastar um para outro mundo produz incongruencia visivel. Aqui os 64
        # trajes sao ROUPA AMERICANA DE RUA, e um cami de renda funciona tanto
        # numa varanda da Louisiana quanto numa cozinha de Detroit.
        # ⚠️ O operador trava o traje quando um lote sai bom — e' o eixo de
        # retencao deste angulo. Devolver outro traje porque o MUNDO mudou seria
        # desobedecer a trava calado, que e' o defeito que esta funcao ja' teve.
        return tuple(curto)
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
# ⛔ A negacao anti-celebridade saiu daqui em 2026-08-14, por ordem do operador
# (*"tire not a celebrity do prompt"*): declaracao INJETA o token que ela nega.
# A metade positiva ficou. Ver CLAUDE.md §"CONTRA A CELEBRIDADE, SILENCIO".
APELO_EUA = [
    "A strikingly attractive everyday woman, well groomed, with clear even skin, softly styled hair and a noticeably good figure.",
    "A very good-looking everyday woman with glowing skin, light natural make-up and a shapely figure.",
    "An unusually pretty everyday woman with fine features, healthy glossy hair and a trim shapely body.",
    "A head-turning everyday woman, carefully groomed, with bright eyes, full lips and a striking figure.",
    "A notably beautiful everyday woman with high cheekbones, smooth clear skin and a curvy figure.",
    "A very attractive everyday woman with a toned shapely figure, shining hair and even skin.",
]

# ⛔ HOJE E' CODIGO MORTO: os 16 mundos deste motor sao todos `eua: True`,
# entao `_apelo` nunca cai aqui (medido). Fica porque um mundo novo sem o
# selo o religa — e no registro ANTIGO ele entregaria `plain unremarkable
# face` num agente cuja REF o operador encomendou top model. Codigo morto
# com a regra errada dentro e' bomba com pino: alguem acrescenta um mundo e
# o vicio volta calado, sem lint, sem autoteste, sem aviso.
# ⛔ A negacao anti-celebridade saiu daqui em 2026-08-14, por ordem do operador
# (*"tire not a celebrity do prompt"*): declaracao INJETA o token que ela nega.
# A metade positiva ficou. Ver CLAUDE.md §"CONTRA A CELEBRIDADE, SILENCIO".
APELO_PADRAO = (
    "A strikingly beautiful everyday woman.")


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
    1 sempre o nomeia (todas as DESPEDIDAS trazem `{o}`) e a cena 3 tambem (todos
    os USOS trazem). Linter que reprova o proprio motor e' aviso, nao defesa.

    ⛔ Todo `_cabem` aqui cai na entrada mais CURTA quando nada serve — NUNCA em
    `or pool`, que devolve o pool inteiro e faz a cena estourar em silencio.
    Foi assim que o COLO e o BOTICA subiram de 31 para 36 palavras.
    """
    o1, o2 = spec["orgaos"]
    f = dict(spec.get("falas_map", {}))

    def _ok(pool, monta, teto):
        v = [x for x in pool if _palavras(monta(x)) <= teto]
        return v or [min(pool, key=lambda x: _palavras(monta(x)))]

    if 0 in quais:
        # ⭐ DOIS BEATS, a forma exata da fonte em 0:00-0:06:
        #   "Say goodbye to a soft Johnson and poor blood flow."
        #   "One single cup can help support healthy circulation where it
        #    matters most."
        # ⛔ A caneca esta' ESTENDIDA NA LENTE enquanto ela diz o segundo beat —
        # e' a imagem que entrega o referente que `where it matters most` cala.
        # Sem a caneca em quadro a frase vira drifting.
        def _c1(dp, cn):
            return "%s. %s." % (dp.format(o=o1), cn)

        cc = min(CANECAS, key=_palavras)
        dp = rng.choice(_ok(DESPEDIDAS, lambda x: _c1(x, cc), TETO_FALA[1]))
        cn = rng.choice(_ok(CANECAS, lambda x: _c1(dp, x), TETO_FALA[1]))
        f[0] = _c1(dp, cn)

    if 1 in quais:
        # ⭐ A RECEITA + A FERVURA + O SEGREDO. Fonte, 0:06-0:13.
        # ⭐ O RARO entra com o APOSTO (`maca root, that Andean root from Peru`)
        # — ordem do repo, e nunca o nome cientifico.
        r_fal = raro_falado(spec["raro"])

        def _c2(rec, fer, seg):
            return "%s. %s, %s." % (rec.format(r=r_fal), fer, seg)

        cf = min(FERVURAS, key=_palavras)
        cs = min(SEGREDOS, key=_palavras)
        rec = rng.choice(_ok(RECEITAS, lambda x: _c2(x, cf, cs), TETO_FALA[2]))
        fer = rng.choice(_ok(FERVURAS, lambda x: _c2(rec, x, cs), TETO_FALA[2]))
        seg = rng.choice(_ok(SEGREDOS, lambda x: _c2(rec, fer, x), TETO_FALA[2]))
        f[1] = _c2(rec, fer, seg)

    if 2 in quais:
        # ⭐⭐ O CTA. Fonte, 0:18: *"Comment hard and I'll send you the extra
        # ingredient I like to add to this drink."* Nosso literal e' `gelatin` —
        # `hard` quebraria a automacao de DM, como `BOOK` e `YES`.
        # ⚠️ 2.4K comentarios contra 1.4K reacoes na fonte: e' este beat que faz
        # este angulo valer o lugar dele no repertorio.
        # ⛔ `o2`, NAO `o1`. O sorteio tira DOIS orgaos diferentes justamente
        # para o substantivo nao virar bordao em 24 segundos — e este motor
        # gastava `o1` na cena 1 e de novo na cena 3, deixando `o2` morto em
        # 600 de 600 videos. A cena 2 e' a receita e nao nomeia orgao, entao o
        # par certo e' cena 1 = o1, cena 3 = o2.
        def _c3(uso, isca, gate):
            return "%s %s and I'll send you %s. %s" % (
                uso.format(o=o2), sc.CTA_LITERAL, isca, gate)

        ci = min(ISCAS_ENTREGA, key=_palavras)
        cg = min(GATES, key=_palavras)
        uso = rng.choice(_ok(USOS, lambda u: _c3(u, ci, cg), TETO_FALA[3]))
        isca = rng.choice(_ok(ISCAS_ENTREGA, lambda x: _c3(uso, x, cg),
                              TETO_FALA[3]))
        gate = rng.choice(_ok(GATES, lambda g: _c3(uso, isca, g), TETO_FALA[3]))
        f[2] = _c3(uso, isca, gate)

    return f


def sortear(pagina, rng, led, travas=None):
    """Monta a spec. `travas` fixa eixos (pre-selecao do painel e cadeado)."""
    travas = travas or {}
    usados = led.get(pagina, {})

    # ⭐ TRAVA DE PELE — a pele chega em travas["pele"] ("clara"/"escura") e o
    # sorteio REMONTA O VIDEO EM VOLTA DELA: o mundo so' sai entre os que
    # COMPORTAM aquela pele, e a etnia sorteia dentro do mundo ja' filtrado.
    # ⛔ A ETNIA NUNCA SAI DE FORA DO MUNDO — e' a invariante do autoteste, e e'
    # ela que faz "etnia arrasta o mundo inteiro" ser verdade em vez de slogan.
    # Por isso quem se move e' o MUNDO, nunca a etnia.
    # ⚠️ Mundo travado incompativel CEDE e e' re-sorteado, de preferencia na
    # mesma familia: antes de derrubar o sorteio, o eixo derivado cede.
    pele = travas.get("pele")

    def _comporta(m):
        return not pele or any(_pele_de(e) == pele for e in m["etnias"])

    def _etnias_ok(m):
        """As etnias do mundo que servem a' pele pedida. ⛔ Sem este filtro o
        mundo passava (tem UMA etnia da pele) e a etnia sorteava entre TODAS as
        dele — foi assim que `escura` devolveu Asian American."""
        return [e for e in m["etnias"] if not pele or _pele_de(e) == pele]

    fam_trava = travas.get("familia_mundo")
    if travas.get("mundo"):
        mundo = _por_id(MUNDOS, travas["mundo"])
        if not _comporta(mundo):
            mundo = rng.choice(
                [m for m in MUNDOS if m["familia"] == mundo["familia"]
                 and _comporta(m)]
                or [m for m in MUNDOS if _comporta(m)]
                or [mundo])
    else:
        if fam_trava and fam_trava != "livre":
            fam = fam_trava
        else:
            fam = _fresco([{"id": x} for x in FAMILIAS_MUNDO],
                          usados.get("familia_mundo", []), rng, "id")["id"]
        cand = [m for m in MUNDOS if m["familia"] == fam and _comporta(m)]
        # ⛔ Familia sem mundo daquela pele: a FAMILIA cede, a pele nao.
        # ⛔⛔ E SE NEM O FALLBACK TIVER MUNDO, A PELE CEDE — nao o sorteio.
        # Achado sabotando `_pele_de` para provar que a sonda acusa: o
        # `rng.choice([])` levantava IndexError e derrubava o app do operador.
        # Perder a trava e' ruim; quebrar o app na mao dele e' pior, e um pool
        # de mundos editado amanha pode zerar uma das peles sem ninguem notar.
        mundo = rng.choice(cand
                           or [m for m in MUNDOS if _comporta(m)]
                           or MUNDOS)

    et = travas.get("etnia") or rng.choice(_etnias_ok(mundo)
                                           or mundo["etnias"])
    cor = travas.get("cor") or rng.choice(mundo["cores"])
    # ⭐ O TRAJE E' EIXO PROPRIO desde 2026-08-05, com pool por mundo. Cada
    # entrada e' (template_com_%s_de_cor, nome_curto) — o curto tem de vir do
    # traje SORTEADO, senao a ancora descreve uma roupa que nao esta' em cena.
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
    # ⛔ SEM homem, SEM prop falico, SEM substancia absurda, SEM utensilio: a
    # fonte nao tem nenhum dos quatro. Estavam aqui por heranca do BOTICA, e
    # eixo herdado que nao entra em cena e' pool morto — a armadilha do §29.
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

    spec = {"pagina": pagina, "bela": bool(travas.get("bela")), "mundo": mundo, "etnia": et, "cor": cor,
            "traje": traje, "apelo": apelo, "ref": ref,
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
BANDEIRA_VAR = " A US flag hangs from a pole by the porch rail behind her."
BANDEIRA = " A US flag hangs on the wall behind her."


def montar(spec):
    """Os 7 blocos. Formatacao NOMEADA de ponta a ponta — sao 15+ campos por
    bloco, e um deslocamento de indice posicional troca pronome por cor sem
    estourar erro nenhum (bug que so' aparece no video pronto)."""
    m, ref = spec["mundo"], spec["ref"]
    com, raro = spec["comum"], spec["raro"]
    band = BANDEIRA if spec.get("bandeira") else ""

    v = {
        "var": m["var"], "var_c": m["var_c"],
        "coz": m["coz"], "coz_c": m["coz_c"],
        "sup_a": m["sup_a"], "sup": m["sup"],
        "luz": m["luz"], "luz_c": m["luz_c"],
        "luz_e": m["luz_e"], "luz_e_c": m["luz_e_c"],
        "etnia": spec["etnia"], "idade": ref["idade"],
        "pessoa": _pessoa(spec), "ancora": _ancora(spec),
        "Ancora": _cap(_ancora(spec)),
        "comum_img": com["img"], "raro_img": raro["img"],
        "mug": BO_MUG, "anti": (sc.ANTICELEB_BELA if spec.get("bela") else ANTICELEB), "cauda": CAUDA, "band": band,
        "band_v": (BANDEIRA_VAR if spec.get("bandeira") else ""),
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

    # --- CENA 1 — A VARANDA + A CANECA NA LENTE -----------------------------
    b["IMAGE 01/03"] = (
        "Medium shot on %(var)s.%(band_v)s %(caneca)s She is the only person in "
        "the frame. %(anti)s %(luz_e)s %(cauda)s"
        % dict(v, caneca=BO_CANECA % (_pessoa(spec), BO_MUG)))

    # --- CENA 2 — A COZINHA + A PANELA (o mecanismo) ------------------------
    # ⛔ MUDA DE AMBIENTE, mas NAO de casa nem de roupa: a fonte corta da varanda
    # para a cozinha da mesma casa, com a mesma mulher e o mesmo traje.
    b["IMAGE 02/03"] = (
        "%(panela)s %(anti)s %(luz)s %(cauda)s"
        % dict(v, panela=BO_PANELA % v))

    # --- CENA 3 — A CANECA PRONTA + O CTA -----------------------------------
    # ⭐ O objeto da keyword esta' NA MAO no frame em que a boca diz `gelatin,`.
    b["IMAGE 03/03"] = (
        "Closer medium shot in the same kitchen, same background, same "
        "%(luz_c)s, filmed straight on and framed from the waist up. %(Ancora)s, "
        "standing centred in the frame, holding %(mug)s up at chest height, "
        "turned towards the lens. She looks directly into the camera, warm and "
        "certain, her mouth open mid-word as she speaks, her front teeth even "
        "and complete. She is the only person in the frame. %(anti)s %(cauda)s"
        % v)

    # ⛔⛔ O TAKE ANIMA A IMAGE — ELE NAO INVENTA OUTRO GESTO. Contradicao entre
    # IMAGE e TAKE e' pior que omissao: a omissao o gerador preenche com o frame;
    # a contradicao ele resolve mexendo no que estava certo.
    mov = [
        BO_CANECA_ESTAVEL + " She stays seated and never stands up.",
        ("She keeps the ingredient held up in her right hand at chest height "
         "the whole time and never puts it down. Her left hand stays flat on "
         "the %(sup)s beside the hotplate. %(nao_toca)s" % v),
        ("She holds the mug steady at chest height the whole time, never drinks "
         "from it and never sets it down."),
    ]
    audio = ["%s. No music." % m["audio"],
             "%s, water simmering in a pan. No music." % m["audio"],
             "%s. No music." % m["audio"]]

    for i in range(3):
        b["TAKE %02d/03" % (i + 1)] = (
            "Animate the provided image exactly. Handheld iPhone shot, very "
            "slight natural sway, no cuts. %s She is the only person in the "
            'shot.\nDialogue: "%s"\nAudio: %s'
            % (mov[i], sonorizar(spec["falas"][i]), audio[i]))

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
    # ⛔⛔ A negacao anti-celebridade nunca volta ao texto montado
    # (2026-08-14, ordem do operador). Este motor nao passa pelo
    # `sc.lint_curto`, entao a lente entra aqui explicitamente — regra sem
    # guarda volta no proximo agente nascido por copia, e foi exatamente
    # assim que a clausula chegou aos 30 motores.
    sc.lint_anticeleb(blocos, ach)
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
    # ⛔⛔ REESCRITO PARA O CHA, 2026-08-05. A versao herdada do BOTICA exigia
    # duas coisas que este angulo nao tem, e reprovava 100% da producao:
    #   (a) `gelatin` ou o orgao na ABERTURA da cena 2 — aqui a cena 2 abre na
    #       receita, e o `gelatin trick` fecha a cena (e' o segredo retido, a
    #       forma da fonte). Cobrar na abertura entregaria o mecanismo cedo.
    #   (b) `my husband` na cena 1 — no BOTICA a narradora conta do marido;
    #       aqui ela fala DIRETO COM O HOMEM QUE ASSISTE, no imperativo (*"Say
    #       goodbye to a soft Johnson"*). Nao ha' marido para nomear.
    # ⭐ O PRINCIPIO (§21, o teste WTF) SOBREVIVE INTEIRO: o espectador nunca
    # pode perguntar "do que ela esta' falando?". So' muda o que cumpre a funcao
    # em cada cena — e e' por isso que a lente e' reescrita e nao apagada.
    sents1 = _sentencas(falas[0])
    if sents1:
        a1 = sents1[0].lower()
        if not any(o.lower() in a1 for o in NUCLEO):
            ach.append(("ERRO", "BO9: a abertura da cena 1 nao nomeia o ORGAO — "
                                "%r deixa o espectador sem saber do que se "
                                "trata no segundo em que ele decide se fica"
                        % sents1[0]))
        # ⭐ A DOR E' DELE, E A FRASE TEM DE DIZER ISSO. No imperativo o
        # destinatario e' quem assiste; sem imperativo nem 2a pessoa, a frase
        # fica sem dono e vira slogan.
        if not (re.match(r"(say|wave|kiss) goodbye", a1)
                or re.search(r"\byour\b", a1)):
            ach.append(("ERRO", "BO9: a abertura da cena 1 nao fala COM ele — "
                                "sem imperativo nem `your`, o problema nao tem "
                                "dono e a frase vira slogan (%r)" % sents1[0]))
    # ⭐ A cena 2 abre na RECEITA: tem de nomear ingrediente concreto, nunca uma
    # abstracao ("mix the ingredients"). E' o que a imagem esta' mostrando.
    sents2 = _sentencas(falas[1])
    if sents2 and not any(x in sents2[0].lower()
                          for x in ("lemon", "ginger", "garlic")):
        ach.append(("ERRO", "BO9: a abertura da cena 2 nao nomeia ingrediente "
                            "concreto — %r nao casa com a panela em quadro"
                    % sents2[0]))
    # ⭐ A cena 3 abre no USO e nomeia o orgao: e' o beat que diz PARA QUE SERVE.
    sents3 = _sentencas(falas[2])
    if sents3 and not any(o.lower() in sents3[0].lower() for o in NUCLEO):
        ach.append(("ERRO", "BO9: a abertura da cena 3 nao nomeia o orgao — "
                            "%r promete um habito sem dizer para que (%s)"
                    % (sents3[0], "licoes §21")))

    # --- BO8: ⭐ O RARO E O APOSTO, e o aposto mora na CENA 2 --------------
    # ⛔ REESCRITO PARA O CHA. No BOTICA o raro abria a cena 1 como segredo; aqui
    # a cena 1 e' a DESPEDIDA + a caneca na lente, e a fonte nao nomeia nenhum
    # ingrediente ate' 0:06. O raro e o aposto vivem os dois na cena 2.
    raro = spec["raro"]
    if raro["nome"].lower() not in (spec["falas"][1] or "").lower():
        ach.append(("ERRO", "BO8: a cena 2 nao nomeia o ingrediente raro (%s) — "
                            "e' ele que separa esta receita de um cha comum"
                    % raro["nome"]))
    elif raro["aposto"].lower() not in (spec["falas"][1] or "").lower():
        ach.append(("ERRO", "BO8: `%s` entrou SEM o aposto na cena 2 — nome solto "
                            "nao diz ao espectador o que ele esta' ouvindo"
                    % raro["nome"]))
    for r in RAROS:
        if _palavras(r["aposto"]) > 9:
            ach.append(("ERRO", "BO8: aposto de %r com %d palavras (regra de "
                                "repo: nome popular + aposto curto)"
                        % (r["nome"], _palavras(r["aposto"]))))

    # --- BO15: ⭐ a PROMESSA nomeia o orgao, e o mecanismo nao e' ENTREGUE ---
    # ⛔ Ordem do operador, 2026-08-04, duas partes:
    #   1. *"tome cuidado ao dizer que X E' o gelatin trick: pode matar a
    #      curiosidade"* -> a cena 2 declara um passo RETIDO, nunca equipara a
    #      receita visivel ao mecanismo.
    #   2. *"«you'll be a new person» apenas seria vago pq pode ser nova pessoa
    #      por qualquer circunstancia"* -> promessa sem orgao e' promessa de
    #      nada.
    # ⛔ REESCRITO: este angulo nao tem pool de PROMESSAS — a cena 2 fecha no
    # SEGREDO RETIDO, que e' a forma da fonte (*"the extra ingredient I like to
    # add"*). A regra que sobrevive e' a de nao entregar o mecanismo: dizer que
    # a receita visivel E' o gelatin trick mata a curiosidade que move o DM.
    for linha in SEGREDOS:
        if "gelatin trick" not in linha:
            ach.append(("ERRO", "BO15: segredo sem o literal `gelatin trick` — "
                                "%r quebra a congruencia com a VSL" % linha))
    if re.search(r"(?:is|are)\s+the\s+gelatin\s+trick", spec["falas"][1] or "",
                 re.I):
        ach.append(("ERRO", "BO15: a cena 2 equipara a receita visivel ao "
                            "mecanismo — entregue o nome, retenha o passo"))

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

    # --- BO1: ⭐⭐ A CANECA ESTENDIDA NA LENTE, o eixo deste agente ---------
    # ⛔ REESCRITO. A lente herdada exigia `fills the left half of the frame` e
    # o `prop` sorteado — as duas do BOTICA, onde a cena 1 e' um prop falico com
    # substancia caindo em cima. Aqui a cena 1 e' a caneca no braco esticado, e
    # exigir a clausula do outro angulo reprovaria 100% da producao.
    if "stretched out towards" not in i1 or BO_MUG not in i1:
        ach.append(("ERRO", "BO1: IMAGE 01/03 sem a CANECA ESTENDIDA na lente — "
                            "e' o unico objeto deste angulo e o que o segundo "
                            "beat da fala aponta sem nomear"))
    # ⭐ SENTADA, com as pernas em quadro. Ordem do operador sobre este agente:
    # o corpo e' a bullet de retencao, e em pe' as pernas saem do enquadramento.
    if "Sitting in a metal porch chair" not in i1 or "bare legs in shot" not in i1:
        ach.append(("ERRO", "BO1: IMAGE 01/03 sem a pose SENTADA com as pernas "
                            "em quadro — e' a retencao do hook deste angulo"))

    # --- BO5: ⭐ OS DOIS AMBIENTES — varanda na 1, cozinha na 2 e 3 ---------
    # ⚠️ E' o unico agente do repertorio com corte de ambiente dentro do video.
    # Se a cena 1 nascer na cozinha, o corte some e o video vira um BOTICA.
    m = spec["mundo"]
    if m["var"] not in i1:
        ach.append(("ERRO", "BO5: a cena 1 nao esta' na VARANDA — o corte "
                            "varanda->cozinha e' a estrutura da fonte"))
    for nome in ("IMAGE 02/03", "IMAGE 03/03"):
        if m["var"] in blocos[nome]:
            ach.append(("ERRO", "BO5: %s ainda na varanda — as cenas 2 e 3 sao "
                                "na cozinha da MESMA casa" % nome))
    if m["coz"] not in blocos["IMAGE 02/03"]:
        ach.append(("ERRO", "BO5: a cena 2 nao esta' na cozinha do mundo "
                            "sorteado"))
    # ⭐ A CANECA fecha o video na mao dela: e' o objeto da keyword, e tem de
    # estar em quadro no frame em que a boca diz `gelatin,`.
    if BO_MUG not in i3:
        ach.append(("ERRO", "BO5: a cena 3 sem a caneca na mao — o CTA nomeia "
                            "o mecanismo e a mao tem de mostrar o objeto"))
    # ⛔ Ela NUNCA bebe. Levar a caneca a' boca tira o objeto do quadro no
    # segundo em que a fala o promete.
    for nome in ("TAKE 01/03", "TAKE 03/03"):
        if "never drinks from it" not in blocos[nome]:
            ach.append(("ERRO", "BO5: %s sem a trava de NAO BEBER — a caneca "
                                "sai do quadro justamente no beat que a promete"
                        % nome))

    # --- BO6: ⭐ PESSOA UNICA nas tres cenas --------------------------------
    # ⛔ REESCRITO: a lente herdada cobrava um HOMEM MUDO na cena 3. A fonte nao
    # tem homem nenhum — em 28 segundos ela e' a unica pessoa em quadro. Um
    # segundo corpo aqui divide a atencao que o traje foi posto para prender.
    for nome in ("IMAGE 01/03", "IMAGE 02/03", "IMAGE 03/03"):
        if "only person in the frame" not in blocos[nome]:
            ach.append(("ERRO", "BO6: %s sem a trava de PESSOA UNICA — e' ela "
                                "sozinha nos 28 segundos da fonte" % nome))

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
    """⛔ Este angulo NAO tem prop falico — o objeto e' a caneca. Mantido porque
    o `randomizador-prisma` chama esta funcao em todos os motores."""
    return "glass mug of tea"


# ---------------------------------------------------------------------------
# UI
# ---------------------------------------------------------------------------

def resumo_pt(spec):
    m = spec["mundo"]
    return ("Mulher %s de %d anos, de %s, em %s (%s). Cena 1: sentada na "
            "varanda, o braco esticado com a caneca de cha na lente, pernas em "
            "quadro. Cena 2: na cozinha da mesma casa, a panela no fogareiro "
            "com %s e %s. Cena 3: a caneca na mao e o CTA. Ela sozinha nas "
            "tres.%s"
            % (spec["etnia"], spec["ref"]["idade"], spec["traje"][1],
               m["id"].replace("_", " "), m["familia"],
               spec["comum"]["nome"], spec["raro"]["nome"],
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
    """Trocou o COMUM ou o RARO: o RARO esta' na fala da cena 2.

    ⛔ Aqui havia um guard de `spec["metodo"]` herdado do BOTICA — e este motor
    NAO TEM metodo. Trocar COMUM ou RARO no painel estourava KeyError dentro do
    callback do tkinter, que sob `pythonw` nao tem stderr: o botao simplesmente
    nao fazia nada, e a IMAGE ficava com um ingrediente e a boca com outro.
    ⚠️ Achado por auditoria, nao por lint — nenhuma lente executa o painel.
    """
    spec["falas"][1] = nova_fala(spec, 1, rng)


EIXOS_QUE_MEXEM_NA_COPY = {
    "mundo": _apos_mundo,
    "comum": _apos_cena2,
    "raro": _apos_cena2,
}

TETO_LEDGER = {"familia_mundo": len(FAMILIAS_MUNDO), "comum": len(COMUNS),
               "raro": len(RAROS), "traje": 4}

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
        for eixo, chave in (("mundo", "id"), ("comum", "id"), ("raro", "id")):
            vistos[eixo].add(spec[eixo][chave])
        vistos["etnia"].add(spec["etnia"])
        vistos["ref"].add(spec["ref"]["marca"])
        vistos["traje"].add(spec["traje"][1])
        fam[spec["mundo"]["familia"]] += 1
        band[bool(spec["bandeira"])] += 1
        for i, f in enumerate(spec["falas"], 1):
            larguras[i].append(_palavras(f))
        if spec["etnia"] not in spec["mundo"]["etnias"]:
            falhas.append("seed %d: etnia fora do mundo" % seed)

    for eixo, pool in (("mundo", MUNDOS), ("comum", COMUNS), ("raro", RAROS)):
        if len(vistos[eixo]) != len(pool):
            falhas.append("%s: %d de %d nunca sorteados"
                          % (eixo, len(pool) - len(vistos[eixo]), len(pool)))
    for nome, pool in (("MUNDOS", MUNDOS), ("RAROS", RAROS),
                       ("COMUNS", COMUNS), ("REFS", REFS),
                       ("DESPEDIDAS", DESPEDIDAS), ("CANECAS", CANECAS),
                       ("RECEITAS", RECEITAS), ("FERVURAS", FERVURAS),
                       ("SEGREDOS", SEGREDOS), ("USOS", USOS),
                       ("ISCAS_ENTREGA", ISCAS_ENTREGA), ("GATES", GATES)):
        if len(pool) < MIN_OPCOES:
            falhas.append("eixo %s com %d opcoes (minimo %d)"
                          % (nome, len(pool), MIN_OPCOES))
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
    for _n, _p in (("DESPEDIDAS", DESPEDIDAS), ("CANECAS", CANECAS),
                   ("RECEITAS", RECEITAS), ("FERVURAS", FERVURAS),
                   ("SEGREDOS", SEGREDOS), ("USOS", USOS),
                   ("ISCAS_ENTREGA", ISCAS_ENTREGA), ("GATES", GATES),
                   ("REFS", REFS), ("MUNDOS", MUNDOS)):
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
    # ⚠️ A SONDA ACOMPANHOU A REGRA. Ela mexia em `falas[0]` porque no BOTICA o
    # raro abria a cena 1; aqui ele mora na cena 2, e a sonda ficou vigiando uma
    # frase que nunca teve raro nenhum — passava sempre, sem proteger nada.
    s8 = dict(s, falas=list(s["falas"]))
    s8["falas"][1] = s8["falas"][1].replace(
        raro_falado(s["raro"]), s["raro"]["nome"])
    if not any("BO8" in msg for _, msg in lint(s8, b)):
        ctrl.append("[BO8] NAO acusa o ingrediente raro sem o aposto na cena 2")
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

    # ⭐⭐ [BO1] A CANECA FORA DA LENTE — o controle deste agente.
    # ⛔ As tres sondas que estavam aqui (homem mudo, homem olhando a lente,
    # copo adiantado) vigiavam regras que este angulo desligou. Sonda de regra
    # morta e' decoracao: ela passa sempre e nao protege nada.
    b1 = dict(b)
    b1["IMAGE 01/03"] = b1["IMAGE 01/03"].replace("stretched out towards",
                                                  "resting on")
    if not any("BO1" in msg for _, msg in lint(s, b1)):
        ctrl.append("[BO1] NAO acusa a caneca fora da lente — o eixo do agente")

    # [BO1] a pose sentada com as pernas em quadro (a retencao do hook)
    b1b = dict(b)
    b1b["IMAGE 01/03"] = b1b["IMAGE 01/03"].replace("bare legs in shot",
                                                    "hands in shot")
    if not any("BO1" in msg for _, msg in lint(s, b1b)):
        ctrl.append("[BO1] NAO acusa a perda das pernas em quadro")

    # [BO5] o corte de ambiente: cena 1 na cozinha em vez da varanda
    b5 = dict(b)
    b5["IMAGE 01/03"] = b5["IMAGE 01/03"].replace(s["mundo"]["var"],
                                                  s["mundo"]["coz"])
    if not any("BO5" in msg for _, msg in lint(s, b5)):
        ctrl.append("[BO5] NAO acusa a cena 1 fora da varanda")

    # [BO5] ela bebendo — o objeto sai do quadro no beat que o promete
    b5b = dict(b)
    b5b["TAKE 03/03"] = b5b["TAKE 03/03"].replace("never drinks from it",
                                                  "raises it to her lips")
    if not any("BO5" in msg for _, msg in lint(s, b5b)):
        ctrl.append("[BO5] NAO acusa a caneca indo a' boca")

    # [BO6] um segundo corpo em cena
    b6 = dict(b)
    b6["IMAGE 03/03"] = b6["IMAGE 03/03"].replace(
        "She is the only person in the frame.", "A man stands behind her.")
    if not any("BO6" in msg for _, msg in lint(s, b6)):
        ctrl.append("[BO6] NAO acusa um segundo corpo em cena")

    # [BO4] gelatin trick fora da cena 2
    s4 = dict(s, falas=list(s["falas"]))
    s4["falas"][1] = s4["falas"][1].replace("gelatin trick", "morning routine")
    if not any("BO4" in msg for _, msg in lint(s4, b)):
        ctrl.append("[BO4] nao acusa a cena 2 sem o `gelatin trick`")

    # ⭐⭐ [PELE] A TRAVA DE PELE, MEDIDA — nao declarada. Contrato criado em
    # 2026-08-05 porque o seletor clara/escura era um botao MORTO neste motor
    # (etnia livre, vinda do mundo). Um contrato novo sem sonda e' a mesma
    # armadilha do §29: ninguem percebe quando ele para de valer.
    # ⛔ Duas invariantes, as duas cobradas em 120 sorteios por pele:
    #   1. a pele sorteada e' a pedida;
    #   2. a etnia continua vindo de DENTRO do mundo — se ela passar a sair
    #      solta para satisfazer a trava, "etnia arrasta o mundo" virou slogan.
    for _pele in ("clara", "escura"):
        # ⛔ A COBERTURA E' CHECADA ANTES DOS 120 SORTEIOS. Ao contrario, a
        # sonda gastava 120 sorteios contra uma trava impossivel e so' depois
        # reportava — e no caminho podia derrubar o proprio autoteste.
        if not [m for m in MUNDOS
                if any(_pele_de(e) == _pele for e in m["etnias"])]:
            ctrl.append("[PELE] nenhum mundo comporta %r — a trava nao tem o "
                        "que sortear e a pele vai ceder calada" % _pele)
            continue
        _fora, _solta = 0, 0
        _vistas = set()
        for _k in range(120):
            _s = sortear("joe", random.Random(_k), {}, {"pele": _pele})
            _vistas.add(_s["etnia"])
            if _pele_de(_s["etnia"]) != _pele:
                _fora += 1
            if _s["etnia"] not in _s["mundo"]["etnias"]:
                _solta += 1
        if _fora:
            ctrl.append("[PELE] trava %r furou em %d de 120 sorteios"
                        % (_pele, _fora))
        if _solta:
            ctrl.append("[PELE] a etnia saiu de FORA do mundo em %d de 120 — a "
                        "trava esta' sendo satisfeita quebrando a invariante"
                        % _solta)
        # ⛔⛔ A TERCEIRA INVARIANTE, e ela e' correcao DE CAMPO do operador
        # (2026-08-05, com print): `escura` significa NEGRO. Asiatico, latino e
        # mestico nao sao nem clara nem escura — so' saem com a pele LIVRE.
        # ⚠️ Checar so' `_pele_de(etnia) == pele` NAO pega isto: com a regra
        # binaria antiga (`clara = tem white, escura = o resto`) o Asian
        # American passava como "escura" e a sonda dizia OK. A sonda tem de
        # olhar as etnias QUE SAIRAM contra a lista explicita.
        _fora_lista = _vistas - set(PELE_ETNIAS[_pele])
        if _fora_lista:
            ctrl.append("[PELE] a trava %r devolveu etnia fora da lista: %s — "
                        "escura significa NEGRO, e neutras so' saem no livre"
                        % (_pele, ", ".join(sorted(_fora_lista))))

    # o lote limpo NAO pode ser acusado
    if [x for t, x in lint(s, b) if t == "ERRO"]:
        ctrl.append("o lote limpo esta' sendo reprovado — regra que reprova "
                    "tudo nunca foi testada")

    print("MUNDOS %d em %d familias | RAROS %d | COMUNS %d | REFS %d | "
          "DESPEDIDAS %d | CANECAS %d | USOS %d"
          % (len(MUNDOS), len(FAMILIAS_MUNDO), len(RAROS), len(COMUNS),
             len(REFS), len(DESPEDIDAS), len(CANECAS), len(USOS)))
    print("%d videos | mundos %d/%d | etnias %d | raros %d/%d"
          % (n, len(vistos["mundo"]), len(MUNDOS), len(vistos["etnia"]),
             len(vistos["raro"]), len(RAROS)))
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
            # ⭐ O TRAJE entra no ledger: neste agente ele e' a retencao, e
            # repetir a roupa em videos seguidos da mesma pagina e' o que o
            # operador ve primeiro no lote.
            for eixo, val in (("familia_mundo", spec["mundo"]["familia"]),
                              ("comum", spec["comum"]["id"]),
                              ("raro", spec["raro"]["id"]),
                              ("traje", spec["traje"][1])):
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
