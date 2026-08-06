#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
receita_short.py — randomizador + gerador + linter do AGENTE **RECEITA** (SHORT).

⭐ FONTE: reel facebook.com/reel/1683536299390859 (19,8s). Baixado pela rota 2b do
`RUNBOOK-watch-videos.md` (aba logada + relay local), transcrito com Whisper e
lido frame a frame em 2026-08-04. Este motor nao inventa copy: ele TRADUZ a da
fonte para o nosso mecanismo (gelatin trick / Comment gelatin).

⭐ O QUE E' O ANGULO, em uma frase: um homem confessa em PRIMEIRA PESSOA que
estava perdendo a mulher, e a prova que ele oferece nao e' um corpo — e' a
RECEITA SENDO FEITA na bancada dele, sem rosto em quadro ate' o payoff.

⛔ E' o unico agente do repertorio sem prop falico e sem corpo-prova nas duas
primeiras cenas. O que segura o scroll e' a mao e a tigela.

O ARCO — 3 cenas de 8s, destino AdBatch Vertical 3:

    cena 1  A PERDA        o po' caindo na tigela + a confissao   (o hook)
    cena 2  A RECEITA      a bancada aberta + a virada + a reacao (o mecanismo)
    cena 3  O PAYOFF       ele e ela num lugar masculino + a taca (o CTA)

⭐⭐ O TOGGLE DA CENA 1 — ordem do operador, 2026-08-04. A cena 1 tem DOIS
enquadramentos e o painel alterna entre eles:

    corte      macro de cima, so' as maos e a tigela, zero rosto (a fonte)
    terceira   plano medio, ele em quadro preparando a receita, falando na lente

⚠️ O toggle governa **so' a cena 1**, que foi o escopo pedido. A cena 2 fica
sempre no plano aberto da bancada sem rosto (fiel a' fonte), entao no modo
`terceira` o rosto aparece na 1, some na 2 e volta na 3. Esta' declarado de
proposito: se o operador quiser que a cena 2 acompanhe o toggle, e' uma decisao
dele, nao minha (regra de alcada — copy e cena sao do operador).

⛔⛔ O CAVALO VIVO NAO EXISTE NESTE AGENTE. A fonte fecha com um cavalo preto
colado no rosto do homem; o operador cortou o animal em 2026-08-04 e mandou
repor a entropia que ele trazia com um POOL DE LUGARES masculinos, garagem como
carro-chefe. O cavalo sobrevive so' como SILHUETA IMPRESSA na caixa de gelatina
(papelao, zero risco de render) — e o linter cobra que ele nao saia de la'.

⛔ DESPEJO CRU — ordem do operador, 2026-08-04. Nada cresce, nada faz morph em
cena nenhuma. Quem cresce e' o RESSURREICAO. Aqui o bit visual e' o po' caindo.

⚠️ ETNIA ARRASTA O MUNDO INTEIRO. Nao ha' eixo `etnia` solto: ela sai de dentro
do MUNDO, junto com a cozinha, a bancada, o traje, a luz e a ambiencia. Mesma
forma do `MUNDOS` do COLO e do CLEAN v2, e mesma ordem do operador.

Uso:
    python funil-organico/receita_short.py --pagina joe --n 1
    python funil-organico/receita_short.py --pagina ray --n 3 --seed 42 --dry-run
    python funil-organico/receita_short.py --autoteste
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
LEDGER = os.path.join(AQUI, ".receita-short-ledger.json")

TITULO = "AGENTE RECEITA SHORT"
SLUG = "receita-short"
SUBTITULO = ("a receita e' a prova, em 3 cenas · corte de maos ou terceira "
             "pessoa · gerador offline de prompts Veo")

# O dict que a `ui_agente.paginas_por_pele` le' para agrupar as paginas no
# seletor `pele clara/escura`. ⚠️ Ele NAO governa a etnia do video neste motor
# (ver MUNDOS) — mas sem ele o painel quebra, e a classificacao e' por
# SUBSTRING (`"white" in ...`), entao o formato tem de ser string.
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

# ⭐⭐ RE1 — A CAIXA. E' o prop-mestre do angulo e o unico claim do video: a
# silhueta de cavalo impressa promete potencia sem que ninguem diga uma palavra
# de alegacao. Lida na fonte em t=00:00 (caixa kraft/salmao, cavalo preto de
# perfil, texto ilegivel no video).
# ⛔ `no readable words` NAO e' enfeite: a CAUDA promete "No on-screen text", e
# rotulo com letra em foco e' texto em cena. A silhueta passa; a palavra, nao.
# ⛔ O cavalo so' existe AQUI. Cavalo vivo em quadro foi cortado pelo operador.
RE_CAIXA = ("a kraft cardboard box of gelatin with a black horse silhouette "
            "printed on the front and no readable words anywhere on it")

# ⭐⭐ RE2 — O CORTE DE MAOS (modo `corte`). E' a cena 1 da fonte inteira.
# ⚠️ A CAMERA E' A ANCORA DE ALTURA, nunca um movel: licao do COLO (H4), onde
# ancorar altura num movel em quadro fez o movel virar assunto.
# ⚠️ AS MAOS SAO A UNICA IDENTIDADE DELE nesta cena — nao ha' rosto, nao ha'
# tronco. Por isso a ancora distintiva TEM de morar na mao, e o linter cobra.
RE_CORTE = (
    "Filmed from directly above and close in, looking straight down at %(sup_a)s, "
    "so that the bowl sits in the middle of the frame and the %(sup)s runs out to "
    "both edges. In the centre is a wide clear glass bowl of water. Two hands "
    "come in from the top of the frame holding %(caixa)s, tipped mouth-down a "
    "hand's width above the bowl, and %(po)s is falling from it in a steady "
    "stream into the water. His hands are the only part of him in the frame — "
    "%(etnia)s, %(maos)s, and %(marca_mao)s. His head and his body stay out of "
    "shot for the whole frame."
)

# ⭐⭐ RE3 — A TERCEIRA PESSOA (modo `terceira`). O outro lado do toggle.
# ⚠️ Mesma acao, mesma tigela, mesma caixa — muda o ENQUADRAMENTO e so' ele. Foi
# o que o operador pediu: alternar o take, nao trocar a cena.
RE_TERCEIRA = (
    "Medium shot in %(coz)s, filmed straight on at chest height and framed from "
    "the waist up. Standing behind %(sup_a)s, centred in the frame, is "
    "%(pessoa)s. On the %(sup)s in front of him is a wide clear glass bowl of "
    "water. He holds %(caixa)s in both hands, tipped mouth-down a hand's width "
    "above the bowl, and %(po)s is falling from it in a steady stream into the "
    "water. He looks straight into the lens with his mouth open mid-word as he "
    "speaks, his front teeth even and complete."
)

# ⭐⭐ RE4 — A BANCADA ABERTA (cena 2). Lida na fonte de t=00:06 a t=00:17.
# ⛔ A MAO ESQUERDA CHAPADA NA FRENTE DO QUADRO e' o achado da leitura otica e
# nao pode cair: e' ela que da' presenca fisica ao homem num plano em que ele
# nao tem rosto. Sem ela a cena 2 vira um b-roll de receita.
# ⛔ A pegada da mao direita e' o anti-F12b (punho inteiro em volta + antebraco):
# o Veo solta objeto que a mao "segura" sem estar descrito.
RE_BANCADA = (
    "Medium shot in %(coz)s, filmed straight on at the height of the %(sup)s, "
    "framed so that %(sup_a)s runs across the bottom third of the picture. "
    "Standing in the "
    "centre is the same wide clear glass bowl, now filled to halfway with "
    "%(gel)s. At frame-left on the %(sup)s stands %(caixa)s. At frame-right "
    "stands %(pote)s with a metal spoon lying on the %(sup)s beside it. His left "
    "hand rests flat and open on the %(sup)s in the very front of the frame, "
    "close to the camera and large in shot, %(etnia)s, %(maos)s, and "
    "%(marca_mao)s. His right hand is closed around %(pote_curto)s, the whole "
    "hand visibly wrapped around it, his forearm resting steady on the %(sup)s, "
    "tipping it over the bowl. His head and his body stay out of shot."
)

# ⛔ RE5 — nada se mexe na bancada alem do que ele esta' fazendo. Sem isto o Veo
# comeca a mexer em tudo o que esta' em quadro e a continuidade morre.
RE_NAO_TOCA = ("Nothing else on the %s is touched, moved, opened or lifted, and "
               "nothing is added to it or taken away.")

# ⭐ RE6 — A TACA DO PAYOFF. Lida na fonte em t=00:18: taca larga de coupe cheia
# de cubos de gelatina rosa, estendida para a lente.
# ⛔ Ela so' existe na CENA 3. Mostrar antes entrega o payoff antes da promessa.
RE_TACA = ("a wide-bowled glass coupe heaped with firm vivid purple gelatin cubes, "
           "glossy and set")

# ⛔ RE7 — A ANCORA DE CONTINUIDADE do modo `terceira`. Rosto E idade, nunca so'
# roupa: no VAZAMENTO a ancora estava na camisa e o render devolveu outra pessoa.
# ⚠️ So' e' exigida quando o rosto JA' APARECEU. No modo `corte` a cena 3 e' a
# primeira vez que existe rosto, e cobrar ancora ali seria cobrar continuidade de
# um rosto que ninguem viu — regra larga demais (licoes §16).
# ⚠️ Comeca em minuscula: entra no meio da frase e o `_cap` a levanta quando abre.
RE_ANCORA = ("the same %d-year-old %s man from the first scene, same %s, same "
             "%s, same %s")

ANTICELEB = ("Ordinary relatable face, not a celebrity, not a model, not an "
             "actor, not resembling any famous person.")
CAUDA = "Shot on iPhone, natural grain. No on-screen text, no watermark."


# ---------------------------------------------------------------------------
# ⭐⭐ MUNDOS — O NICHO VISUAL INTEIRO NUM EIXO SO'
# ---------------------------------------------------------------------------
# ⛔ NAO EXISTE EIXO `etnia` SOLTO NESTE MOTOR. Ordem do operador (a mesma do
# COLO, 2026-08-03, reafirmada aqui em 2026-08-04): *"variar etnia e' arrastar o
# mundo inteiro — cenario, traje, luz, audio — nunca trocar so' o rosto"*.
#
# ⚠️ A TENSAO COM A REGRA 3.2 ESTA' DECLARADA, NAO ESCONDIDA: o WORKFLOW manda a
# etnia do REF casar com a etnia do avatar da pagina. Este motor segue o
# precedente do COLO, que o operador abriu de proposito — a etnia sai do MUNDO.
# Quem quiser o comportamento antigo trava o mundo no painel.
#
# Cada MUNDO carrega, congruentes entre si:
#     etnias   as etnias que aquele mundo comporta
#     coz      a cozinha (o set das cenas 1 e 2)
#     coz_c    a mesma, curta, para a ancora
#     sup_a    a superficie da bancada, COM artigo
#     sup      a mesma, uma palavra
#     traje    a roupa (%s = cor) — ⛔ SEM artigo: `_traje()` calcula `a`/`an`
#     curto    a roupa em duas palavras, para a ancora de continuidade
#     cores    as cores que aquela roupa aceita
#     luz      a luz, frase inteira
#     luz_c    a mesma, curta
#     audio    a ambiencia
#     fam_lug  as familias de LUGAR que aquele mundo comporta ("*" = todas)
#
# ⭐ O SORTEIO E' POR FAMILIA, DEPOIS POR MUNDO DENTRO DELA. Sem esse passo a
# familia com mais sets domina o lote — medido no CLEAN v2 e no COLO.
# ⛔ ZERO texto legivel em qualquer set: a CAUDA promete "No on-screen text".
# ⚠️ O selo `V` fica so' no mundo da fonte; os outros sao `N` (extrapolacao
# nossa, sem render — quem valida em campo e' o operador).
MUNDOS = [
    # ---- a fonte: farmhouse americana --------------------------------------
    {"id": "fazenda_americana", "selo": "V", "familia": "americana",
     "etnias": ["white American"],
     "coz": "a bright white American farmhouse kitchen, white shaker cabinets "
            "and a white subway-tile backsplash, a deep white apron sink under "
            "a window with bare winter branches outside",
     "coz_c": "white farmhouse kitchen",
     "sup_a": "a dark walnut butcher-block counter", "sup": "counter",
     "traje": "%s flannel shirt with the sleeves pushed back",
     "curto": "flannel shirt",
     "cores": ["faded blue", "dark green", "rust red", "charcoal"],
     "luz": "Cold flat daylight coming in from the window at frame-left, no "
            "lamps on.",
     "luz_c": "cold window daylight",
     "audio": "quiet kitchen room tone", "fam_lug": "*"},

    {"id": "cozinha_suburbana", "selo": "N", "familia": "americana",
     "etnias": ["white American"],
     "coz": "a plain American suburban kitchen, honey-oak cabinets and a "
            "speckled beige backsplash, a wall calendar of photographs by the "
            "doorway and a chrome kettle on the hob",
     "coz_c": "oak suburban kitchen",
     "sup_a": "a worn beige laminate countertop", "sup": "countertop",
     "traje": "%s zip-up fleece over a plain t-shirt",
     "curto": "zip-up fleece",
     "cores": ["navy", "grey", "olive", "maroon"],
     "luz": "Warm overhead kitchen light with weak daylight behind it.",
     "luz_c": "warm overhead kitchen light",
     "audio": "a fridge humming, quiet room tone", "fam_lug": "*"},

    # ---- apalache -----------------------------------------------------------
    {"id": "cozinha_montanha", "selo": "N", "familia": "apalache",
     "etnias": ["white American"],
     # ⚠️ `bare pine board walls` + `tinned goods` + `scarred plank` liam como
     # cabana de subsistencia. O rustico fica; a carencia sai.
     "coz": "a well-built Appalachian lodge kitchen, finished pine panelling "
            "and glass-front cabinets of preserves, matched cast-iron hanging "
            "on a rail and a black enamel range in the corner",
     "coz_c": "pine lodge kitchen",
     "sup_a": "a thick oiled butcher-block counter", "sup": "counter",
     "traje": "%s quilted flannel work shirt",
     "curto": "quilted work shirt",
     "cores": ["dark red", "forest green", "brown", "slate blue"],
     "luz": "Low grey mountain daylight through a small window at frame-right.",
     "luz_c": "low grey mountain daylight",
     "audio": "wind at the window, a stove ticking",
     "fam_lug": ["garagem", "rural", "agua"]},

    # ---- sulista ------------------------------------------------------------
    {"id": "cozinha_sul", "selo": "N", "familia": "sulista",
     "etnias": ["Black American"],
     "coz": "a Southern American kitchen with pale yellow beadboard walls, a "
            "screen door standing open onto a green yard, glass jars of dried "
            "beans on an open shelf and a well-used cast-iron skillet on the hob",
     "coz_c": "yellow beadboard kitchen",
     "sup_a": "a pale blue painted wooden counter", "sup": "counter",
     "traje": "%s short-sleeved button-down shirt",
     "curto": "button-down shirt",
     "cores": ["cream", "sky blue", "khaki", "soft grey"],
     "luz": "Bright soft daylight coming through the open screen door.",
     "luz_c": "bright daylight through the screen door",
     "audio": "cicadas outside, a screen door creaking", "fam_lug": "*"},

    # ---- mexicana -----------------------------------------------------------
    {"id": "cozinha_mexicana", "selo": "N", "familia": "mexicana",
     "etnias": ["Mexican American"],
     "coz": "a Mexican American family kitchen, hand-painted blue and yellow "
            "talavera tiles across the backsplash, clay pots stacked on an open "
            "shelf and a flat steel comal resting on the hob",
     "coz_c": "talavera-tiled kitchen",
     "sup_a": "a terracotta-tiled counter", "sup": "counter",
     "traje": "%s open camp-collar shirt over a white vest",
     "curto": "camp-collar shirt",
     "cores": ["cream", "pale blue", "tan", "deep red"],
     "luz": "Warm afternoon sun coming in low from frame-left.",
     "luz_c": "warm low afternoon sun",
     "audio": "a radio playing faintly in another room",
     "fam_lug": ["garagem", "quintal", "rural"]},

    # ---- caribenha ----------------------------------------------------------
    {"id": "cozinha_caribe", "selo": "N", "familia": "caribenha",
     "etnias": ["Caribbean American"],
     "coz": "a Caribbean kitchen with mint-green painted walls and louvred "
            "jalousie windows standing open, broad green leaves visible "
            "outside, chipped enamel bowls stacked by the sink",
     "coz_c": "mint-green island kitchen",
     "sup_a": "a pale speckled stone counter", "sup": "counter",
     "traje": "%s loose linen shirt worn open at the collar",
     "curto": "loose linen shirt",
     "cores": ["white", "pale yellow", "sea blue", "sand"],
     "luz": "Hard bright island daylight coming through the louvres.",
     "luz_c": "hard bright island daylight",
     "audio": "birds outside, a ceiling fan turning",
     "fam_lug": ["quintal", "agua", "garagem"]},

    # ---- asiatica -----------------------------------------------------------
    {"id": "cozinha_leste_asia", "selo": "N", "familia": "asiatica",
     "etnias": ["East Asian American"],
     "coz": "a compact East Asian American kitchen, stainless steel splashback "
            "and a magnetic bar of knives, a bamboo steamer stacked on a shelf "
            "and a rice cooker beside the hob",
     "coz_c": "stainless-steel kitchen",
     "sup_a": "a pale grey stone counter", "sup": "counter",
     "traje": "%s half-zip knit pullover",
     "curto": "half-zip pullover",
     "cores": ["charcoal", "oat", "navy", "moss green"],
     "luz": "Even cool daylight from a window behind the camera.",
     "luz_c": "even cool daylight",
     "audio": "a rice cooker ticking, quiet room tone", "fam_lug": "*"},

    # ---- sul-asiatica -------------------------------------------------------
    {"id": "cozinha_sul_asia", "selo": "N", "familia": "sul_asiatica",
     "etnias": ["South Asian American"],
     "coz": "a South Asian American kitchen with polished stone surfaces, a row "
            "of round steel storage tins along an open shelf, a heavy pressure "
            "cooker on the hob and a steel tumbler beside the sink",
     "coz_c": "polished stone kitchen",
     "sup_a": "a dark polished granite counter", "sup": "counter",
     "traje": "%s long-sleeved kurta shirt",
     "curto": "kurta shirt",
     "cores": ["off-white", "pale blue", "sand", "deep maroon"],
     "luz": "Warm even daylight from a window at frame-right.",
     "luz_c": "warm even daylight",
     "audio": "a pressure cooker hissing softly, quiet room tone",
     "fam_lug": ["garagem", "quintal", "rural"]},

    # ---- africana -----------------------------------------------------------
    {"id": "cozinha_africa_oeste", "selo": "N", "familia": "africana",
     "etnias": ["West African"],
     # ⚠️ REGISTRO SOCIOECONOMICO SUBIDO, 2026-08-04, ordem do operador lendo o
     # render: *"nao quero ambiente tao humilde assim, nao passa muito
     # credibilidade"*. Concreto pintado, bacias esmaltadas empilhadas e porta
     # dando na terra batida liam como POBREZA — e quem vende receita caseira
     # precisa parecer que a casa dele funciona.
     # ⛔ A ETNIA NAO MUDOU, mudou a CLASSE. O que identifica o mundo continua
     # sendo o pilao, o traje e a luz; o que saiu foi o sinal de carencia.
     "coz": "a well-kept West African kitchen with glazed tiled walls, fitted "
            "wood cabinets with glass fronts, a carved wooden mortar and pestle "
            "on the side and a door open onto a swept green courtyard",
     "coz_c": "tiled West African kitchen",
     "sup_a": "a polished dark granite counter", "sup": "counter",
     "traje": "%s short-sleeved embroidered cotton tunic",
     "curto": "embroidered tunic",
     "cores": ["white", "indigo", "sand", "deep green"],
     "luz": "Strong flat daylight coming through the open doorway.",
     "luz_c": "strong flat daylight",
     "audio": "voices far off outside, quiet room tone",
     "fam_lug": ["quintal", "rural", "garagem"]},

    {"id": "cozinha_africa_leste", "selo": "N", "familia": "africana",
     "etnias": ["East African"],
     # ⚠️ idem: `dented aluminium kettle`, `hanging from a nail` e `plain
     # scrubbed counter` liam como falta de dinheiro, nao como tradicao.
     # ⛔ E nada de `herbs growing in pots` aqui — a primeira versao desta linha
     # usava `growing` e disparou a RE17 (vocabulario de crescimento fora da
     # cena do bit visual) em 192 de 1500 sorteios.
     "coz": "a tidy East African kitchen with pale tiled walls and a wide "
            "shuttered window, a stainless kettle on the hob, woven baskets in "
            "a neat row on a shelf and potted herbs along the sill",
     "coz_c": "pale tiled kitchen",
     "sup_a": "a solid hardwood worktop", "sup": "worktop",
     "traje": "%s open-collared cotton shirt",
     "curto": "cotton shirt",
     "cores": ["white", "pale grey", "tan", "sky blue"],
     "luz": "Soft daylight through the shutters at frame-left.",
     "luz_c": "soft shuttered daylight",
     "audio": "a kettle ticking, quiet room tone",
     "fam_lug": ["quintal", "rural", "agua"]},

    # ---- mediterranea -------------------------------------------------------
    {"id": "cozinha_grega", "selo": "N", "familia": "mediterranea",
     "etnias": ["Mediterranean"],
     "coz": "a whitewashed Mediterranean kitchen with a wide arched window, "
            "hand-glazed tiles behind the hob, matched terracotta on an open "
            "shelf and a string of dried herbs on a hook",
     "coz_c": "whitewashed arched kitchen",
     "sup_a": "a thick pale marble counter", "sup": "counter",
     "traje": "%s open cotton shirt with the sleeves rolled",
     "curto": "rolled-sleeve shirt",
     "cores": ["white", "pale blue", "sand", "olive"],
     "luz": "Hard bright Mediterranean sun through the arched window.",
     "luz_c": "hard bright sun",
     "audio": "gulls far off, quiet room tone",
     "fam_lug": ["agua", "quintal", "rural"]},

    {"id": "cozinha_italiana", "selo": "N", "familia": "mediterranea",
     "etnias": ["Southern European"],
     "coz": "a southern Italian kitchen with pale green tiled walls to shoulder "
            "height, a heavy hanging copper pan rack, a glass jar of dried pasta "
            "on the side and shuttered doors standing half open",
     "coz_c": "green-tiled kitchen",
     "sup_a": "a worn grey stone counter", "sup": "counter",
     "traje": "%s knitted polo shirt",
     "curto": "knitted polo",
     "cores": ["cream", "navy", "olive", "brick red"],
     "luz": "Warm daylight through the half-open shutters at frame-right.",
     "luz_c": "warm shuttered daylight",
     "audio": "a clock ticking, quiet room tone", "fam_lug": "*"},
]

FAMILIAS_MUNDO = list(dict.fromkeys(m["familia"] for m in MUNDOS))


# ---------------------------------------------------------------------------
# ⭐⭐ LUGARES — O PAYOFF MASCULINO DA CENA 3
# ---------------------------------------------------------------------------
# ⛔ ESTE POOL EXISTE PORQUE O CAVALO SAIU. Ordem do operador, 2026-08-04:
# *"Nao precisa do cavalo, em substituicao ao cavalo no take pode caprichar num
# pool de lugares (garagem bem mainly, outros ambientes tipicamente bem
# masculinos) para mantermos a entropia que o cavalo trazia pra cena"*.
#
# ⚠️ POR QUE `garagem` E' UMA FAMILIA E NAO UMA ENTRADA PESADA: o checklist do
# repo cobra que nenhum eixo passe de ~17% de concentracao, e uma unica entrada
# "garagem" com peso alto violaria isso. Cinco garagens DISTINTAS resolvem os
# dois lados: cada entrada fica dentro do teto por entrada, e a familia
# `garagem` domina o lote como o operador pediu (5 de 16 = 31% do pool).
#
# ⚠️ CONGRUENCIA COM O MUNDO: cada MUNDO declara `fam_lug` — que familias de
# lugar aquele nicho comporta. Uma cozinha de cabana apalache nao paga um pier
# de marina urbana. `"*"` significa que o mundo comporta todas.
#
# ⛔ ZERO texto legivel em qualquer lugar (placa, letreiro, marca no carro): a
# CAUDA promete "No on-screen text", e oficina e' onde mais aparece letreiro.
LUGARES = [
    # ---- garagem — o carro-chefe -------------------------------------------
    {"id": "garagem_carro", "selo": "N", "fam": "garagem",
     "set": "an open home garage with a car up on axle stands and its bonnet "
            "propped open behind them, a coiled hose on the wall and an oil "
            "stain on the concrete floor",
     "luz": "Flat daylight coming in through the open garage door behind the "
            "camera.",
     "audio": "a distant lawnmower, quiet garage echo"},
    {"id": "garagem_bancada", "selo": "N", "fam": "garagem",
     "set": "a home garage workbench corner, a heavy steel vice bolted to the "
            "bench behind them and a pegboard of hand tools hung in outlines on "
            "the wall",
     "luz": "A bare shop light overhead with daylight leaking in from the side.",
     "audio": "a shop light buzzing faintly, quiet garage echo"},
    {"id": "garagem_moto", "selo": "N", "fam": "garagem",
     "set": "a home garage with a motorcycle on its stand behind them, a red "
            "rolling tool chest against the wall and a folded tarpaulin in the "
            "corner",
     "luz": "Warm low sun reaching in through the open garage door at "
            "frame-left.",
     "audio": "quiet garage echo, a bird outside"},
    {"id": "garagem_porta_aberta", "selo": "N", "fam": "garagem",
     "set": "the mouth of an open home garage, the driveway and a strip of "
            "green lawn visible behind them, a wheelbarrow tipped against the "
            "wall",
     "luz": "Bright open daylight from the driveway behind them.",
     "audio": "wind and distant traffic"},
    {"id": "garagem_lenha", "selo": "N", "fam": "garagem",
     "set": "a garage with the side door open onto a neatly stacked woodpile, a "
            "splitting axe on its rack and a chest freezer humming against the "
            "back wall",
     "luz": "Cool daylight through the open side door at frame-right.",
     "audio": "a freezer humming, wind outside"},

    # ---- oficina / galpao ---------------------------------------------------
    {"id": "marcenaria", "selo": "N", "fam": "oficina",
     "set": "a small woodworking shop, a bench with clamps along its edge "
            "behind them and curls of shaving on the floor",
     "luz": "Dusty daylight from a high window at frame-left.",
     "audio": "quiet workshop room tone"},
    {"id": "galpao_ferramentas", "selo": "N", "fam": "oficina",
     "set": "a finished garden workshop, tools hung in order on a slatted wall "
            "and a bank of labelled parts drawers beside them",
     "luz": "Flat grey daylight through the open shed door.",
     "audio": "wind against metal, quiet room tone"},

    # ---- quintal ------------------------------------------------------------
    {"id": "churrasqueira", "selo": "N", "fam": "quintal",
     "set": "a back yard beside a fired-up charcoal grill with smoke rising off "
            "it, a wooden fence and a green lawn behind them",
     "luz": "Warm late-afternoon sun from frame-right.",
     "audio": "coals ticking, birds in the yard"},
    {"id": "alpendre", "selo": "N", "fam": "quintal",
     "set": "a covered cedar porch with two solid armchairs behind them and a "
            "kept lawn falling away past the rail",
     "luz": "Soft shaded daylight under the porch roof.",
     "audio": "wind in the trees, a wind chime"},
    {"id": "quintal_horta", "selo": "N", "fam": "quintal",
     "set": "the edge of a back-yard vegetable patch, staked tomato plants and "
            "a leaning garden fork behind them",
     "luz": "Bright open sun overhead.",
     "audio": "birds and insects in the garden"},

    # ---- caminhonete / estrada ---------------------------------------------
    {"id": "caçamba", "selo": "N", "fam": "veiculo",
     "set": "the dropped tailgate of a pickup truck parked on gravel, the open "
            "bed and a coil of rope behind them",
     "luz": "Low golden sun coming in from behind the truck.",
     "audio": "gravel underfoot, wind"},
    {"id": "capo_caminhonete", "selo": "N", "fam": "veiculo",
     "set": "the front of a clean pickup on a gravel drive, the bonnet standing "
            "open behind them and open country beyond",
     "luz": "Hard open daylight with the sun high.",
     "audio": "wind across open ground"},

    # ---- agua ---------------------------------------------------------------
    {"id": "pier_pesca", "selo": "N", "fam": "agua",
     "set": "the end of a wooden fishing pier, two rods propped in holders "
            "behind them and flat water running to the horizon",
     "luz": "Low sun coming off the water behind them.",
     "audio": "water lapping at the piles, gulls"},
    {"id": "doca_barco", "selo": "N", "fam": "agua",
     "set": "a small boat dock with a moored open boat behind them and coiled "
            "line on the boards",
     "luz": "Bright daylight bouncing off the water.",
     "audio": "water slapping the hull, rigging tapping"},

    # ---- rural --------------------------------------------------------------
    {"id": "curral_celeiro", "selo": "N", "fam": "rural",
     "set": "the open doorway of a well-kept timber barn, a swept concrete "
            "floor and stacked feed sacks squared against the wall behind them",
     "luz": "Strong daylight from the barn doorway behind the camera.",
     "audio": "wind through the barn, quiet room tone"},
    {"id": "cerca_campo", "selo": "N", "fam": "rural",
     "set": "a post-and-wire fence line at the edge of an open field, long dry "
            "grass and a treeline behind them",
     "luz": "Warm low sun across the field.",
     "audio": "wind in dry grass, birds"},
]

FAMILIAS_LUGAR = list(dict.fromkeys(l["fam"] for l in LUGARES))


# ---------------------------------------------------------------------------
# ⭐ REFS — O HOMEM QUE CONFESSA
# ---------------------------------------------------------------------------
# ⛔ ELE E' A VOZ DO VIDEO INTEIRO e o rosto de uma cena so'. Por isso o pool
# cobre DOIS conjuntos de eixos que os outros agentes tratam separado:
#   · o ROSTO ..... para o modo `terceira` e para a cena 3 (payoff)
#   · a MAO ....... a UNICA identidade dele no modo `corte` e na cena 2 inteira
#
# ⚠️ IDADE 57-69, seguindo a fonte (homem grisalho de 60 e poucos). ⛔ A lei do
# REF (mulher sempre bonita, 20-35) e' da MULHER e nao se aplica aqui: o homem e'
# o dono do problema, e problema de ED com 30 anos nao e' o avatar da VSL.
#
# ⚠️ EIXOS FISICOS COBERTOS, como o `medir_personagens.py --gate` cobra:
#   cabelo ✓  pelo facial ✓  oculos ✓  porte ✓  pele ✓  ancora facial ✓
# Entrada nova difere das outras em ≥ 3 eixos. ⛔ Contar entradas nao basta:
# doze homens descritos so' pelo cabelo sao o mesmo homem doze vezes (licoes §15).
#
# ⛔ ZERO adjetivo de etnia dentro das entradas: quem injeta e' a montagem, a
# partir do MUNDO. Mesmo contrato do COLO, do NECROSE e do EXTERIOR.
REFS = [
    {"idade": 62, "porte": "heavy through the shoulders and thick in the neck",
     "cabeca": "a full head of silver-grey hair combed back",
     "pelo": "several days of white stubble",
     "oculos": "",
     "pele": "weathered skin, deeply lined across the forehead",
     "marca": "a broad flattened nose that has been broken once",
     "maos": "broad and squared, with short blunt nails and raised veins",
     "marca_mao": "a plain worn gold wedding band on his left ring finger"},

    {"idade": 58, "porte": "lean and wiry, with a flat stomach",
     "cabeca": "close-cropped grey hair thinning at the crown",
     "pelo": "clean-shaven",
     "oculos": "thin wire-framed glasses",
     "pele": "pale skin with a scatter of sun spots on the temples",
     "marca": "a deep vertical crease between his eyebrows",
     "maos": "long and bony, the knuckles enlarged",
     "marca_mao": "a faded blue-green tattoo of an anchor on his left forearm"},

    {"idade": 66, "porte": "broad and barrel-chested, with a heavy middle",
     "cabeca": "bald on top with grey hair kept short at the sides",
     "pelo": "a thick white moustache",
     "oculos": "",
     "pele": "ruddy sun-darkened skin across the cheeks",
     "marca": "a pale crescent scar on his left cheekbone",
     "maos": "big and weathered, the skin cracked at the joints",
     "marca_mao": "a heavy steel watch worn loose on his left wrist"},

    {"idade": 60, "porte": "tall and rangy, with narrow hips",
     "cabeca": "wavy salt-and-pepper hair worn a little long at the collar",
     "pelo": "a short greying beard kept close",
     "oculos": "",
     "pele": "olive skin, weathered at the neck",
     "marca": "a gold-flecked hazel eye and a heavy brow",
     "maos": "wide palms with thick fingers and cracked nails",
     "marca_mao": "a thick silver signet ring on his left little finger"},

    {"idade": 69, "porte": "stooped and thin, with sloped shoulders",
     "cabeca": "fine white hair, sparse and combed flat",
     "pelo": "clean-shaven",
     "oculos": "heavy black-framed reading glasses pushed up on his head",
     "pele": "thin papery skin with prominent veins at the temple",
     "marca": "a large dark mole beside his right nostril",
     "maos": "thin, the tendons standing out on the backs",
     "marca_mao": "a leather-strapped watch sitting square on his left wrist"},

    {"idade": 57, "porte": "solid and square, built like a former lineman",
     "cabeca": "dark hair going grey at the temples, cut short",
     "pelo": "a neat chinstrap beard",
     "oculos": "",
     "pele": "smooth dark skin with a shine across the cheekbones",
     "marca": "a deep dimple in his left cheek when he smiles",
     "maos": "thick-fingered, the palms pale and calloused",
     "marca_mao": "a wide plain steel band on his left ring finger"},

    {"idade": 64, "porte": "compact and stocky, with a short thick neck",
     "cabeca": "grey hair shaved down to stubble all over",
     "pelo": "a full grey beard, trimmed square at the jaw",
     "oculos": "",
     "pele": "dark skin with a raised keloid line at the jaw",
     "marca": "a wide gap between his two front teeth",
     "maos": "square and heavy, with darkened knuckles",
     "marca_mao": "a knotted leather cord tied around his left wrist"},

    {"idade": 61, "porte": "slight and narrow-framed",
     "cabeca": "straight black hair going grey, parted at the side",
     "pelo": "a thin moustache",
     "oculos": "rimless glasses",
     "pele": "smooth skin with deep lines at the corners of the eyes",
     "marca": "a small dark birthmark high on his right cheek",
     "maos": "small and neat, the nails cut short and square",
     "marca_mao": "a thin gold band worn on his left ring finger"},

    {"idade": 67, "porte": "big-bellied and slow-moving, with heavy forearms",
     "cabeca": "a receding hairline with grey hair worn long behind the ears",
     "pelo": "a heavy grey walrus moustache",
     "oculos": "",
     "pele": "florid skin with broken capillaries across the nose",
     "marca": "a drooping left eyelid",
     "maos": "meaty and red, the fingers swollen at the joints",
     "marca_mao": "a thumbnail ridged and darkened from an old injury"},

    {"idade": 59, "porte": "trim and upright, still carrying muscle",
     "cabeca": "thick grey hair swept back off a high forehead",
     "pelo": "clean-shaven",
     "oculos": "",
     "pele": "tanned skin with a pale band across the forehead",
     "marca": "very pale blue eyes under dark brows",
     "maos": "hard and dry, the backs freckled",
     "marca_mao": "a thin white scar running across the back of his left hand"},

    {"idade": 65, "porte": "round-shouldered and soft through the middle",
     "cabeca": "curly grey hair kept short and dense",
     "pelo": "a short white goatee",
     "oculos": "square tortoiseshell glasses",
     "pele": "brown skin, dry and ashy across the knuckles and cheeks",
     "marca": "a heavy fold beneath each eye",
     "maos": "wide and soft, with pale creased palms",
     "marca_mao": "a beaded bracelet worn loose on his left wrist"},

    {"idade": 63, "porte": "tall and heavy-boned, with a long back",
     "cabeca": "iron-grey hair in a flat brush cut",
     "pelo": "a two-day shadow of grey stubble",
     "oculos": "",
     "pele": "coarse skin, pitted across the cheeks",
     "marca": "a notch cut through his right eyebrow",
     "maos": "enormous, with thick wrists and blunt fingertips",
     "marca_mao": "a white band of untanned skin where a ring used to be"},
]


# ---------------------------------------------------------------------------
# ⭐ MULHERES — a parceira do payoff
# ---------------------------------------------------------------------------
# ⛔⛔ LEI DO REF — ELA E' SEMPRE MUITO BONITA. Ordem permanente do operador.
# ⛔ Zero oculos, zero grisalho, zero pele castigada. A ancora facial e' SINAL DE
# BELEZA (marca de nascenca, covinha, sarda, olho de cor incomum), nunca
# deterioracao (licoes-producao-veo §REF).
# ⚠️ FAIXA 30-35, o topo da lei. E' escolha declarada: a fonte poe uma loira de
# ~25 ao lado de um homem de 60+, e diferenca de idade grande e' geometria que o
# classificador olha com lupa sem nada a ganhar em conversao. 30-35 continua
# dentro da lei e e' a menor distancia disponivel.
# ⚠️ A IDADE DELA E' DECLARADA NO PROMPT em toda mencao (licao V12 do VAZAMENTO).
# ⛔ Zero adjetivo de etnia: quem injeta e' a montagem, a partir do MUNDO.
# ⚠️ O eixo PELE esta' em 12/12 e sempre como SINAL DE BELEZA — `smooth`,
# `clear`, `glowing`, `sun-kissed`. E' o mesmo eixo que o `medir_personagens.py`
# cobra nos pools masculinos, so' que aqui ele nao pode virar `weathered`,
# `lined` ou `sun-damaged`: no homem a pele castigada le' como credibilidade, na
# mulher le' como o oposto do que ela vende.
MULHERES = [
    {"idade": 34, "corpo": "slim and toned",
     "cabeca": "long wavy honey-blonde hair falling past her shoulders",
     "marca": "clear even skin and a small dark beauty mark just above her lip"},
    {"idade": 31, "corpo": "lean and athletic, with defined shoulders",
     "cabeca": "long dark hair pulled back into a high ponytail",
     "marca": "striking pale green eyes and a light spray of freckles across "
              "fair clear skin"},
    {"idade": 35, "corpo": "slim, with a long neck and fine collarbones",
     "cabeca": "shoulder-length glossy auburn hair tucked behind one ear",
     "marca": "smooth luminous skin and a small gap between her front teeth "
              "that shows when she smiles"},
    {"idade": 32, "corpo": "compact and athletic, with toned arms",
     "cabeca": "tight natural curls kept short and close",
     "marca": "glowing deep brown skin over high sharp cheekbones"},
    {"idade": 33, "corpo": "slender and long-limbed",
     "cabeca": "straight black hair cut in a blunt glossy bob",
     "marca": "poreless golden skin, full lips and a deep dimple in her left "
              "cheek"},
    {"idade": 30, "corpo": "toned and broad-shouldered, like a swimmer",
     "cabeca": "long braids gathered over one shoulder",
     "marca": "rich even skin, a small silver hoop in her left nostril and a "
              "wide bright smile"},
    {"idade": 34, "corpo": "slim-hipped and wiry",
     "cabeca": "thick copper-red hair falling loose past her shoulders",
     "marca": "pale clear skin under a dense spray of freckles, and pale blue "
              "eyes"},
    {"idade": 31, "corpo": "petite and tightly muscled",
     "cabeca": "dark hair in a high messy bun with loose strands at the temples",
     "marca": "warm olive skin and a beauty mark at the left corner of her "
              "mouth"},
    {"idade": 35, "corpo": "tall and lean, with square shoulders",
     "cabeca": "long dark hair with a sharp widow's peak",
     "marca": "smooth fair skin and eyes of two different colours, one green "
              "and one brown"},
    {"idade": 33, "corpo": "athletic, with a narrow waist",
     "cabeca": "chin-length wavy caramel hair pushed back off her forehead",
     "marca": "sun-kissed skin and a small heart-shaped birthmark below her "
              "right ear"},
    {"idade": 30, "corpo": "slim and long-limbed",
     "cabeca": "very long straight dark hair parted in the middle",
     "marca": "clear glowing skin, arched brows and a small beauty mark high "
              "on her left cheek"},
    {"idade": 32, "corpo": "trim and athletic, with a defined waist",
     "cabeca": "thick dark hair in a low glossy ponytail",
     "marca": "smooth clear skin and a fine pale scar through her right "
              "eyebrow"},
]


# ---------------------------------------------------------------------------
# ⭐ O PO' E O GEL — os dois estados da tigela
# ---------------------------------------------------------------------------
# ⚠️ Lidos na fonte: o po' que cai da caixa e' ROSA, e na cena 2 a tigela ja'
# esta' com liquido VERMELHO. O par anda junto para o video nao trocar de cor
# entre os blocos de 8s.
PO_E_GEL = [
    {"id": "rosa", "selo": "V",
     "po": "a stream of fine pink powder",
     "gel": "clear deep-red liquid"},
    {"id": "ambar", "selo": "N",
     "po": "a stream of fine amber powder",
     "gel": "clear golden-amber liquid"},
    {"id": "roxo", "selo": "N",
     "po": "a stream of fine violet powder",
     "gel": "clear dark-purple liquid"},
    {"id": "verde", "selo": "N",
     "po": "a stream of fine pale-green powder",
     "gel": "clear light-green liquid"},
    {"id": "laranja", "selo": "N",
     "po": "a stream of fine orange powder",
     "gel": "clear bright-orange liquid"},
    {"id": "carmim", "selo": "N",
     "po": "a stream of fine deep-red powder",
     "gel": "clear crimson liquid"},
    {"id": "bordo", "selo": "N",
     "po": "a stream of fine dark-red powder",
     "gel": "clear dark-wine liquid"},
]


# ---------------------------------------------------------------------------
# ⭐ ACOMPANHAMENTOS — o segundo pote da bancada (cena 2)
# ---------------------------------------------------------------------------
# ⚠️ A fonte mostra bicarbonato e vinagre de maca. ⛔ ZERO MARCA LEGIVEL: a
# excecao nominal da marca real e' do EXTERIOR e so' dele (P12), e a fonte usa
# uma caixa de bicarbonato de marca real que nos nao podemos copiar.
# ⚠️ `nome` e' o que a boca DIZ na receita; `pote` e' o que a camera VE.
ACOMPANHAMENTOS = [
    {"id": "bicarbonato", "selo": "V", "nome": "baking soda",
     "pote": "a squat orange cardboard tub of baking soda with no readable "
             "words on it",
     "curto": "the orange tub"},
    {"id": "vinagre", "selo": "V", "nome": "apple cider vinegar",
     "pote": "a tall glass bottle of cloudy amber vinegar with no label",
     "curto": "the glass bottle"},
    {"id": "mel", "selo": "N", "nome": "raw honey",
     "pote": "a wide unlabelled glass jar of thick amber honey",
     "curto": "the honey jar"},
    {"id": "gengibre", "selo": "N", "nome": "ground ginger",
     "pote": "a small unlabelled tin of pale yellow ground ginger",
     "curto": "the small tin"},
    {"id": "canela", "selo": "N", "nome": "ground cinnamon",
     "pote": "a short unlabelled glass jar of red-brown ground cinnamon",
     "curto": "the glass jar"},
    {"id": "curcuma", "selo": "N", "nome": "turmeric",
     "pote": "a squat unlabelled jar of deep yellow turmeric powder",
     "curto": "the yellow jar"},
    {"id": "beterraba", "selo": "N", "nome": "beet powder",
     "pote": "an unlabelled paper pouch of dark red beet powder, rolled open "
             "at the top",
     "curto": "the paper pouch"},
    {"id": "limao", "selo": "N", "nome": "lemon juice",
     "pote": "a small unlabelled glass bottle of pale lemon juice",
     "curto": "the small bottle"},
    {"id": "caiena", "selo": "N", "nome": "cayenne",
     "pote": "a tiny unlabelled shaker of bright red cayenne",
     "curto": "the red shaker"},
    {"id": "magnesio", "selo": "N", "nome": "magnesium powder",
     "pote": "a plain white cardboard tub of fine white powder with no "
             "readable words on it",
     "curto": "the white tub"},
]


# ---------------------------------------------------------------------------
# COPY — cena 1: A PERDA + A REJEICAO
# ---------------------------------------------------------------------------
# ⭐ ESTRUTURA COPIADA DA FONTE, bullet por bullet:
#     "I was losing my wife because I couldn't perform anymore. ||
#      She had completely lost interest in me."
#
# ⛔ AS DUAS METADES ANDAM JUNTAS: a perda e' o que da' o tamanho do problema, a
# rejeicao e' o que faz o espectador se ver. Uma sem a outra e' meia confissao.
#
# ⛔ REGRA DE CONCRETUDE (licoes §17 e §20): a perda NOMEIA o que quebrou, e a
# rejeicao e' um FATO OBSERVAVEL, nunca um estado de espirito. `She pulled away`
# nao e' rejeicao, e' resumo. `She started sleeping in the guest room` e'.
PERDAS = [
    "I was losing my wife because my {o} quit showing up",
    "I nearly lost my marriage because my {o} stopped working",
    "My wife was halfway out the door because my {o} had given up",
    "I was watching my marriage end because my {o} wouldn't stand up",
    "I was losing my wife because my {o} had gone dead on me",
    "Thirty-one years of marriage nearly ended because my {o} quit",
    "I was losing the woman I married because my {o} stopped answering",
    "My wife was done with me because my {o} hadn't worked in two years",
    "I almost lost my wife because my {o} embarrassed me every single time",
    "I was losing my wife because my {o} let me down every night",
]

# ⛔ FATO OBSERVAVEL, sempre. Cada linha e' uma coisa que uma camera veria.
REJEICOES = [
    "She started sleeping in the guest room.",
    "She stopped reaching over at night.",
    "She quit touching me altogether.",
    "She started going to bed an hour before me.",
    "She turned her back to me every single night.",
    "She stopped kissing me goodnight.",
    "She quit looking at me when I got out of the shower.",
    "She moved her pillow to the far side of the bed.",
    "She stopped waiting up for me.",
    "She started locking the bathroom door.",
]

# ---------------------------------------------------------------------------
# ⭐⭐ VILOES — O TERCEIRO BEAT DA CENA 1
# ---------------------------------------------------------------------------
# ⛔ ORDEM DO OPERADOR, 2026-08-04: *"poderia ter incluido bullet de angulo de
# grande vilao: 'doctors don't want you to know this' no agente receita short"*.
#
# ⚠️ E ELE ESTA' APONTANDO PARA A VAGA QUE EU MESMO TINHA MEDIDO E DEIXADO
# ABERTA. Eu reportei que a cena 1 rodava a 2,43 palavras/s contra uma
# capacidade de 3,4-4,0 — oito palavras sobrando — e parei ali, porque inventar
# bullet e' alcada dele. Ele respondeu com o bullet. E' assim que a folga se
# fecha: eu MEÇO e reporto, ele DECIDE o que entra.
#
# ⭐ O QUE O VILAO FAZ, e e' por isso que ele e' o terceiro beat e nao o
# primeiro: a PERDA da o tamanho do problema, a REJEICAO faz o espectador se
# ver, e o VILAO tira a culpa dele e a poe em alguem. Sem esse beat, o homem que
# assiste conclui que o problema e' ele. Com ele, o problema e' que esconderam a
# resposta — e ai' existe motivo para ficar mais oito segundos.
#
# ⛔ REGRA DE FUNCAO, cobrada pelo linter (RE20): TODA entrada NOMEIA QUEM
# esconde ou QUEM lucra. `Nobody told me this` sem dono e' queixa; `no one makes
# a dime when a man fixes this in his own kitchen` e' vilao. A diferenca e' a
# mesma do §20: sujeito sem objeto nao diz nada.
#
# ⚠️ A LINHA DO OPERADOR ENTRA UMA VEZ, NAO QUATORZE. O resto varia o vilao
# (medico, industria, propaganda, a desculpa da idade, a geracao anterior) e o
# registro (1a pessoa contando o que viveu, 2a falando com o espectador).
# ⛔⛔ ESTE COMENTARIO ESTAVA ERRADO E CUSTOU DOIS RENDERS REPROVADOS.
# Dizia: *"Zero `{o}` obrigatorio aqui: a PERDA ja' nomeia o orgao, e repetir o
# substantivo duas vezes em 8 segundos vira bordao."* A premissa era falsa. O
# problema nunca foi repetir o SUBSTANTIVO — foi terminar a frase sem DESTINO.
# ⚠️ E a saida existia desde sempre: o motor sorteia DUAS grafias por video, e
# foi o proprio operador quem mostrou usando as duas no mesmo take. A perda leva
# `o1`, o vilao leva `o2`. Bordao e' a mesma palavra duas vezes; isto nao e'.
# ⛔⛔ REESCRITO INTEIRO EM 2026-08-04 — O POOL TODO CARREGAVA O VICIO.
# O operador leu dois renders seguidos e reprovou os dois:
#   1. "...points you at the expensive pill and away from this."
#      -> *"Drifting identificado 'away from this.' From what???"*
#   2. "The drug companies own the pill. Nobody owns what my grandfather knew."
#      -> e ele mostrou como deveria ser: *"Nobody owns what my grandfather knew
#         to trully save my john-son and my marriage"*
#
# ⚠️ E ao reler as 14 entradas com o teste WTF eu vi que NAO ERAM DUAS LINHAS
# RUINS: era o pool inteiro. Toda entrada terminava num substantivo abstrato sem
# destino — `what costs two dollars` · `nothing that worked` · `the cheap fix` ·
# `the cheap answer` · `asking questions` · `a man stays broken`. Cada uma delas
# responde SIM a "wtf are they talking about?", e todas passavam pela RE20,
# porque RE20 so' cobrava o AGENTE no comeco e nao olhava o fim da frase.
#
# ⭐⭐ O MOLDE COMPLETO, ditado por ele em dois exemplos:
#       [QUEM] + [o que ele te VENDE] + [o que ele te ESCONDE] + [PARA QUE SERVE]
# A quarta parte e' a que faltava em 12 das 14. Sem ela o espectador ouve uma
# briga com a farmacia e nao sabe o que ganha se ela perder.
#
# ⭐ O ORGAO APARECE DUAS VEZES NA CENA 1, EM GRAFIAS DIFERENTES — e foi ele
# quem mostrou: `my weiner embarrassed me` ... `to save my john-son`. Por isso
# o vilao recebe `o2`, nao `o1`. Repetir a MESMA palavra em 8 segundos vira
# bordao; trocar a grafia nao.
VILOES = [
    "The pharmacy industry sells you pills and buries the two-dollar fix that "
    "got my {o} working.",
    "My doctor had a prescription pad and nothing on it that ever got my {o} up.",
    "Drug companies sell refills. Nothing on that shelf ever kept my {o} up for "
    "my wife.",
    "The pharmacy sold me eleven years of excuses and never one thing that "
    "fixed my {o}.",
    # ⭐ literal do operador, a correcao da recusa 1
    "Every television ad points you at the expensive pill, the secret is in "
    "this natural trick.",
    "No doctor gets paid for the two-dollar mix that puts a man's {o} back to "
    "work.",
    "The clinic had a code to bill and nothing to tell my father about his {o}.",
    "The pharmacy industry sells you a monthly plan and hides the cheap mix "
    "that hardens your {o}.",
    "Add up what the pharmacy took from me. None of it ever woke my {o} up.",
    # ⭐ literal do operador, a correcao da recusa 2 — a mais longa do pool (20
    # palavras), e e' ela que fixa o teto da cena 1 em 33.
    "The drug companies own the pill. Nobody owns what my grandfather knew to "
    "truly save my {o} and my marriage.",
    "The clinic was paid to prescribe, never to tell me what actually gets my "
    "{o} hard.",
    # ⚠️ Era "...need you believing it is age and nothing else." e o
    # `medir_contexto_copy --gate` reprovou, com razao: nomeia a CAUSA (`age`)
    # sem dizer o que ela quebra — a frase orfa da §17.
    "The pill companies need you buying refills instead of asking what really "
    "fixes your {o}.",
    "Every pharmacy in this town sells the refill and not the recipe that "
    "saved my marriage.",
    "The drug industry profits every month a man's {o} stays down and his wife "
    "stays angry.",
]

# ⛔ RE20 — QUEM esconde, ou QUEM lucra. Um dos dois, nomeado.
# ⚠️ A lista sai das entradas do pool, mas a lente roda sobre a fala MONTADA
# (§19): frase quebrada entre literais adjacentes nao aparece no grep do fonte.
# ⛔⛔ PRONOME NAO E' AGENTE NOMEADO — corrigido em 2026-08-04.
# O operador leu "They will sell you a monthly plan before they sell you the
# truth" e perguntou: *"who will sell what and with what purpose?"*.
# A primeira versao desta lente aceitava `they`, `them`, `nobody` e `somebody`
# como agente — ou seja, ELA CARREGAVA O VICIO QUE EXISTIA PARA PEGAR. `They`
# nao diz quem; `the pharmacy industry` diz.
#
# ⭐ O modelo que o operador ditou tem TRES partes:
#       [QUEM] + [o que ele te VENDE] + [o que ele te ESCONDE]
#       "the pharmacy industry will sell you pills and not let you know the
#        truth that works"
VILAO_AGENTE = re.compile(
    r"\b(pharmac(?:y|ies|eutical|y industry)|drug compan(?:y|ies)|"
    r"drug industry|pill compan(?:y|ies)|doctors?|clinic|chemists?|"
    r"television ad)\b", re.I)


# ---------------------------------------------------------------------------
# COPY — cena 2: A VIRADA + O RESULTADO + A REACAO
# ---------------------------------------------------------------------------
# ⭐ A FONTE:
#     "Everything changed when I started using horse gelatin. ||
#      It grew three times bigger and stayed hard for hours."
# ⛔ `horse gelatin` vira `gelatin trick` — congruencia inviolavel com a VSL.

VIRADAS = [
    "Everything changed the week I started the gelatin trick",
    "Everything turned around when I started the gelatin trick",
    "It all changed the day my brother showed me the gelatin trick",
    "Everything changed when a guy at work gave me the gelatin trick",
    "Everything changed the morning I first did the gelatin trick",
    "It all turned around when my doctor's nurse told me the gelatin trick",
    "Everything changed once I started the gelatin trick every morning",
    "Everything changed the week my cousin sent me the gelatin trick",
]

# ⛔ O NUMERO ABSURDO E' DA FONTE E FICA. Ordem do operador, 2026-08-04: o numero
# e' o choque e a reacao e' a prova — os dois, nessa ordem.
# ⛔⛔ AS 8 ENTRADAS COMECAVAM COM O PRONOME NU `It` — a §22 outra vez.
# O operador leu o TAKE 02 renderizado e corrigiu a mao:
#     gerado:  "It came back full and stayed hard for the better part of an hour"
#     devido:  "My tool came back full and stayed hard for the better part..."
# ⚠️ `It` depois de uma frase que fala de `the gelatin trick` resolve para O
# TRUQUE, nao para o orgao — o espectador ouve "o truque voltou inteiro". O
# pronome nao economiza nada: custa a unica coisa que a frase tinha para vender.
# ⭐ Grafia propria (`o3`), diferente da reacao (`o4`), como no exemplo dele.
RESULTADOS = [
    "My {o} came back three times harder and stayed up for hours",
    "My {o} came back twice the size and held all night",
    "My {o} stood up three times harder than it did at thirty",
    "My {o} came back so hard it woke me up at four in the morning",
    "My {o} came back harder than my wedding night and stayed that way",
    "My {o} went from nothing to three times harder in eleven days",
    "My {o} came back full and stayed hard for the better part of an hour",
    "My {o} came back harder than it has been in twenty years",
]

# ---------------------------------------------------------------------------
# ⭐⭐ REACOES — O BULLET QUE MIGROU DO POST-IT
# ---------------------------------------------------------------------------
# ⛔⛔ ESTE POOL E' A LICAO §20 EM FORMA DE CODIGO.
#
# A fonte cola um post-it manuscrito na tigela com `HARDER THAN EVER`. O operador
# mandou o papel sair do quadro (2026-08-04) e a copy dele migrar para a fala,
# ocupando a folga de tempo da cena 2. Ao propor o pool eu escrevi `SHE NOTICED`
# — e ele parou tudo:
#
#     "She noticed. (telespectador: 'Ela notou o QUE? WTF???')
#      o certo seria: she noticed his John-son harder than ever"
#
# ⛔ POR ISSO TODA ENTRADA DESTE POOL CARREGA `{o}` — obrigatoriamente, e o
# linter (RE12) trava nisso dos dois lados. Reacao de terceiro e' o slot que
# carrega a PROVA SOCIAL: vago ali, o video perde a prova em silencio, porque
# `She noticed.` passa em qualquer linter de forma.
#
# ⚠️ ESCOPO DA REGRA, e ele foi ESTREITADO DE PROPOSITO (licoes §16). A versao
# larga — "toda sentenca com verbo de percepcao precisa do orgao" — reprovaria
# `She stopped reaching over at night` (que e' concreta e esta' certa) e ate' a
# copy que o proprio operador aprovou no RESSURREICAO (`Her hand lands on it and
# she freezes`, cujo objeto e' um pronome). A regra que este motor codifica e' a
# do SLOT: a sentenca de reacao da cena 2 nomeia o orgao. Precisa, sem falso
# positivo, e com controle positivo e negativo no autoteste.
REACOES = [
    "She noticed my {o} harder than ever",
    "She felt my {o} against her and stopped talking",
    "She grabbed my {o} and asked what I had done",
    "She woke up against my {o} and laughed out loud",
    "She reached over, found my {o} like that, and froze",
    "She looked down at my {o} and her mouth fell open",
    "She put her hand on my {o} and said it felt like before",
    "She felt my {o} through the sheet and rolled straight over",
    "She caught my {o} standing there and started smiling",
    "She held my {o} and told me she wanted the old me back",
]


# ---------------------------------------------------------------------------
# COPY — cena 3: O CTA
# ---------------------------------------------------------------------------
# ⭐ A FONTE: "Want the full explanation? || Comment yes and I'll send you the
# video right now." ⛔ `yes` e' PROIBIDO no repo (quebra a automacao DM) e vira o
# literal `Comment gelatin,` + a isca do que chega.
ESCALADAS = [
    "If you want the exact recipe I used",
    "If you want the whole thing written out",
    "If you want the measurements the way I do them",
    "If you want the version that got my {o} back",
    "If you want the full routine and not just the trick",
    "If you want what I actually put in that bowl",
    "If you want the part I can't say out loud here",
    "If you want the same thing that fixed my {o}",
    "If you want it step by step",
    "If you want the whole recipe",
]

# ⚠️ `recipe` domina de proposito: ordem do operador — *"sempre comente gelatin
# pra receber algo {isca} (geralmente sera recipe mesmo)"*.
ISCAS_ENTREGA = [
    "the whole recipe", "the full recipe", "the complete recipe",
    "the exact recipe", "the recipe and the measurements",
    "the recipe and the doses", "the exact measurements",
    "the recipe", "the full routine", "the whole thing written out",
]

GATES = [
    "But you have to follow me, or I can't reach you.",
    "Follow me first, or I can't reply to you.",
    "Make sure you're following, or I can't message you back.",
    "Follow me before you comment, or it never reaches me.",
    "Hit follow first, or my message can't get to you.",
    "Follow me, or I won't be able to find your comment.",
    "Follow me first, or I can't reply.",
    "Follow me, or I can't message you.",
    "Don't forget to follow, or the app won't let me answer.",
]

# ⛔ As palavras do orgao. Rotacionam DENTRO do video (nunca a mesma duas vezes).
NUCLEO = ["Johnson", "pecker", "wiener", "soldier", "tool"]

# ⚠️ MEDIDOS CONTRA A CAPACIDADE REAL de 8s de narracao (~3,4-4,0 p/s), nao
# escolhidos no olho. A fonte roda 16 / 18 / 14 palavras por take, muito abaixo
# da capacidade — foi essa folga que o operador mandou ocupar com a REACAO.
# ⚠️ A cena 2 e' a mais densa: virada + resultado + reacao, tres bullets em 8s.
# ⚠️ O TETO DA CENA 1 SUBIU DE 28 PARA 31 EM 2026-08-04, e o motivo esta' medido:
# com dois beats ela rodava a 2,43 p/s (media 19,4 palavras) contra uma
# capacidade real de 3,4-4,0 — oito palavras de silencio por video. O terceiro
# beat (o VILAO, ordem do operador) ocupa exatamente essa folga. ⛔ Teto folgado
# nao e' seguranca: e' frase morta esperando para nascer (licoes §5).
# ⛔⛔ TETO = 32, E ELE E' FISICO: 8 segundos a 3,4-4,0 palavras/s comportam
# 27-32 palavras (licoes-de-construcao §5). Acima disso a fala NAO e' apertada —
# e' CORTADA, porque o take acaba antes dela.
#
# ⚠️ EU JA' SUBI ESTE TETO PARA 33 UMA VEZ, EM 2026-08-04, E ESTAVA ERRADO.
# O operador tinha reescrito um take a mao para me mostrar o molde do vilao, e
# esse take tinha 33 palavras. Eu tratei o COMPRIMENTO do exemplo dele como
# especificacao e subi o teto para acomoda-lo. Ele corrigiu:
#     *"eu nao testei o meu exemplo contra o teto. Pare de ser literal com meus
#      exemplos, eles sao apenas referencia, nao absolutismo."*
# ⭐ O que o exemplo dele especifica e' a FORMA (as quatro partes do molde), nao
# a metrica. Metrica se mede; forma se copia.
# ⚠️ E a linha longa dele CONTINUA GERANDO com teto 32, porque a rejeicao e'
# opcional e as perdas curtas abrem espaco: 10 (perda) + 20 (vilao) = 30.
# ⛔⛔ TETO 25 — ordem permanente do operador, 2026-08-05: *"sempre meca. Nao
# pode haver cortes de fala."* O numero vem de RENDER, nao de conta: 32
# cortou e 28 cortou. Os exemplos que ele escreve a mao vivem em 16-25
# palavras (2,0-3,1 p/s). Ver licoes-de-construcao §28.
# ⭐⭐ MODOS DE REF — contrato compartilhado (short_comum), 2026-08-05.
# Ordem do operador: toggles de `ref bela` (super model, corpo
# escultural, pouca roupa, olhos fora do comum) e `ref forte` (homem
# musculoso e atraente). ⛔ Desligados, o prompt volta IDENTICO ao de
# antes do recurso — provado caractere por caractere em 200 seeds.
MODO_BELA = True

TETO_FALA = {1: 32, 2: 32, 3: 25}
PISO_FALA = {1: 24, 2: 24, 3: 22}


# ---------------------------------------------------------------------------
# TRAVAS E EIXOS DO PAINEL
# ---------------------------------------------------------------------------
# ⭐⭐ O TOGGLE PEDIDO PELO OPERADOR mora aqui: pre-selecao de tres estados no
# topo do painel. `livre` sorteia; os outros dois fixam o enquadramento da cena 1.
ENQ_CORTE = "corte de maos"
ENQ_TERCEIRA = "terceira pessoa"
ENQUADRAMENTOS = [ENQ_CORTE, ENQ_TERCEIRA]

TRAVAS_UI = [
    ("enquadramento", "CENA 1", ["livre"] + ENQUADRAMENTOS),
    ("familia_mundo", "nicho", ["livre"] + FAMILIAS_MUNDO),
]

EIXOS_TRAVAVEIS = ["mundo", "etnia", "ref", "mulher", "lugar", "cor",
                   "acompanhamento", "gel"]


def etnias_do_mundo(spec):
    """O pool de ETNIA depende do MUNDO em cena — trocar para uma etnia que
    aquele mundo nao comporta e' exatamente a incongruencia que os MUNDOS
    existem para impedir."""
    return list(spec["mundo"]["etnias"])


etnias_do_mundo.recebe_spec = True


def lugares_do_mundo(spec):
    """Os LUGARES que o mundo em cena comporta (`fam_lug`).

    ⚠️ Devolve os DICTS, nao os ids. O painel atribui o item escolhido direto em
    `spec["lugar"]`, e `spec["lugar"]` e' dict em todo o motor — devolver string
    aqui fazia o botao `trocar` gravar uma string e o `resumo_pt` estourar
    `TypeError: string indices must be integers`. Achado no smoke test, nao no
    autoteste: o autoteste sorteia, o painel TROCA.
    ⛔ O contraste e' com `etnias_do_mundo`, que devolve string com razao — la' o
    `spec["etnia"]` E' string. O campo exibido de cada eixo mora no EIXOS_UI.
    """
    return list(_lugares_possiveis(spec["mundo"]))


lugares_do_mundo.recebe_spec = True

EIXOS_UI = [
    ("mundo", "COZINHA", "MUNDOS", "id"),
    ("etnia", "ETNIA", "etnias_do_mundo", None),
    ("ref", "QUEM CONFESSA", "REFS", "cabeca"),
    ("lugar", "O LUGAR (cena 3)", "lugares_do_mundo", "id"),
    ("mulher", "A PARCEIRA", "MULHERES", "cabeca"),
    ("acompanhamento", "O 2o INGREDIENTE", "ACOMPANHAMENTOS", "nome"),
    ("gel", "COR DO PO'", "PO_E_GEL", "id"),
]

CENAS_UI = ["1 · a perda", "2 · a receita", "3 · o CTA"]


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
        return next((x for x in pool if x[chave] == valor), pool[0])
    return valor


def _artigo(s):
    return "an" if s[:1].lower() in "aeiou" else "a"


def _traje(spec):
    """A roupa do mundo com o artigo certo. ⛔ O artigo NAO mora no template:
    cores como `off-white`, `indigo` e `olive` sairiam `a off-white` — bug pago
    no CLEAN v2, e achado LENDO o render, nao pelo linter."""
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
    """As entradas do pool que cabem no teto daquela cena.

    ⛔ DESCARTA-SE A LINHA QUE NAO CABE, NUNCA SE ENCURTA A LINHA (CL15): as
    linhas foram aprovadas uma a uma, e reescrever menor para caber e' trocar
    copy validada por copy nova sem validacao.
    ⚠️ `or pool` porque lista vazia nao pode existir: antes de reprovar o
    sorteio, o teto cede e o LINTER reclama — e' ele quem tem de aparecer, nao
    um IndexError.
    """
    return [x for x in pool if _palavras(monta(x)) <= teto] or pool


def _com_o(pool):
    """As entradas que nomeiam o orgao."""
    return [x for x in pool if "{o}" in x]


_ORNAMENTO = re.compile(
    r"^(if you want|the|whole|full|complete|exact|same|my|it|and|of)\b\s*", re.I)


def _miolo(frase):
    """O nucleo semantico de uma promessa, sem os ornamentos que a abrem.

    ⛔ Existe para a RE19: `If you want the whole recipe` e `the whole recipe`
    sao a MESMA promessa com casacos diferentes, e comparar as strings cruas
    nunca as veria como iguais.
    """
    s = frase.lower().rstrip(".").strip()
    anterior = None
    while s != anterior:
        anterior = s
        s = _ORNAMENTO.sub("", s).strip()
    return s


def _lugares_possiveis(mundo):
    """Os LUGARES congruentes com aquele mundo."""
    fam = mundo["fam_lug"]
    if fam == "*":
        return list(LUGARES)
    return [l for l in LUGARES if l["fam"] in fam] or list(LUGARES)


def _falas(spec, rng, quais=(0, 1, 2)):
    """Monta as falas pedidas a partir dos pools ja' sorteados no spec.

    ⚠️ Uma funcao so' para as tres cenas, e nao tres blocos espalhados: o botao
    `trocar` da UI re-sorteia UMA fala, e duas copias desta conta e' a garantia
    de que uma delas envelhece mentindo (licao paga no CLEAN v2).

    ⭐ A COTA DO ORGAO E' GARANTIDA AQUI, NO SORTEIO, nao so' cobrada no linter.
    A cena 2 sempre nomeia o orgao (todas as REACOES trazem `{o}`, RE12) e a
    cena 1 tambem (todas as PERDAS trazem). Linter que reprova o proprio motor e'
    aviso, nao defesa.
    """
    # ⭐ QUATRO GRAFIAS, UMA POR SLOT QUE NOMEIA O ORGAO — e foi o operador quem
    # ditou a arquitetura, corrigindo dois takes a mao:
    #   take 1: "my weiner embarrassed me"   ...  "to save my john-son"
    #   take 2: "My tool came back full"     ...  "She noticed my soljer harder"
    # ⛔ Ate' 2026-08-04 o motor sorteava DUAS grafias e o comentario dizia que
    # bastava, "porque repetir o substantivo vira bordao". Isso empurrou metade
    # dos slots para o PRONOME (`It came back full`, `away from this`), que e'
    # justamente o vicio cronico (§20/§22). A saida nunca foi calar o orgao: era
    # ter grafia sobrando. `NUCLEO` tem 5.
    o1, o2, o3, o4 = spec["orgaos"]
    f = dict(spec.get("falas_map", {}))

    if 0 in quais:
        # ⭐ TRES BEATS, e a ordem e' lei do angulo: perda (o tamanho) ->
        # rejeicao (o espectador se ve) -> vilao (a culpa sai dele). Foi o
        # operador quem mandou o terceiro entrar, na folga que eu tinha medido.
        # ⛔⛔ O VILAO SORTEIA PRIMEIRO, E A REJEICAO E' OPCIONAL. Ordem invertida
        # em 2026-08-04, e a razao e' medida, nao estetica.
        # ⚠️ Ate' aqui o vilao era o ULTIMO e pegava a SOBRA do teto: perda e
        # rejeicao reservavam apenas a entrada mais CURTA do pool seguinte,
        # enchiam as palavras e o filtro derrubava todo vilao longo. Com o pool
        # reescrito (destino nomeado, 15-20 palavras) isso mataria o pool
        # inteiro. Medido na versao anterior: a linha de 16 palavras que o
        # operador ditou saia 6 vezes em 2000 (0,3%) contra 427 da mais curta.
        # Pool cuja entrada nova nasce morta nao e' pool, e' decoracao.
        # ⭐ E foi o proprio operador quem mostrou o trade: no exemplo que ele
        # escreveu a mao, a REJEICAO NAO ESTA' LA'. Ele preferiu um vilao
        # completo a tres beats truncados. Entao a rejeicao entra quando cabe e
        # sai quando nao cabe — nunca o contrario.
        # ⛔ `o2` no vilao: as duas grafias no mesmo take, como no exemplo dele.
        curto_p = min(PERDAS, key=_palavras).format(o=o1)
        vil = rng.choice(_cabem(
            VILOES, lambda v: curto_p + ". " + v.format(o=o2),
            TETO_FALA[1])).format(o=o2)
        perda = rng.choice(_cabem(
            PERDAS, lambda p: p.format(o=o1) + ". " + vil,
            TETO_FALA[1])).format(o=o1)
        # ⚠️ `_cabe_ainda` e nao `_cabem`: aqui a lista VAZIA e' resposta
        # legitima (nao ha' rejeicao que caiba), e `_cabem` tem `or pool` — ele
        # devolveria o pool inteiro e estouraria o teto em silencio.
        cabem_r = [r for r in REJEICOES
                   if _palavras("%s. %s %s" % (perda, r, vil)) <= TETO_FALA[1]]
        rej = rng.choice(cabem_r) if cabem_r else ""
        # ⚠️ `%s. %s %s` com `rej` vazio deixaria dois espacos no meio da fala.
        f[0] = ("%s. %s %s" % (perda, rej, vil) if rej
                else "%s. %s" % (perda, vil))

    if 1 in quais:
        # ⭐ TRES BULLETS EM 8s. A ordem e' lei do angulo e foi o operador quem a
        # fixou: virada (nomeia o mecanismo) -> resultado (o numero) -> reacao
        # (a prova social, sempre com o orgao). Nada aqui e' opcional.
        curto_v = min(VIRADAS, key=_palavras)
        curto_x = min(REACOES, key=_palavras)

        # ⛔ `res` TAMBEM leva `.format` agora: ate' 2026-08-04 as 8 entradas
        # comecavam com o pronome nu `It`, e o operador leu o render — *"It came
        # back full... deveria ser My tool came back full"*. Grafias distintas
        # no resultado (o3) e na reacao (o4), como no exemplo dele.
        def _c2(vir, res, rea):
            return "%s. %s. %s." % (vir, res.format(o=o3), rea.format(o=o4))

        res = rng.choice(_cabem(RESULTADOS,
                                lambda r: _c2(curto_v, r, curto_x),
                                TETO_FALA[2]))
        vir = rng.choice(_cabem(VIRADAS,
                                lambda v: _c2(v, res, curto_x), TETO_FALA[2]))
        rea = rng.choice(_cabem(REACOES,
                                lambda x: _c2(vir, res, x), TETO_FALA[2]))
        f[1] = _c2(vir, res, rea)

    if 2 in quais:
        # ⛔ RE19 — A ESCALADA E A ISCA NAO PODEM SER A MESMA COISA.
        # Achado LENDO a saida renderizada, nao pelo linter (§19): o sorteio
        # solto devolvia `If you want the whole recipe - Comment gelatin, and
        # I'll send you the whole recipe.` — a promessa dita duas vezes com as
        # mesmas palavras, num take que ja' e' o mais denso dos tres.
        # ⚠️ Resolvido no SORTEIO, nao so' cobrado no linter: linter que reprova
        # o proprio motor e' aviso, nao defesa.
        curto_g = min(GATES, key=_palavras)
        esc = rng.choice(_cabem(
            ESCALADAS,
            lambda e: "%s — %s and I'll send you %s. %s"
            % (e.format(o=o1), sc.CTA_LITERAL, max(ISCAS_ENTREGA, key=_palavras),
               curto_g),
            TETO_FALA[3]))
        miolo = _miolo(esc)
        livres = [i for i in ISCAS_ENTREGA if _miolo(i) != miolo] or ISCAS_ENTREGA
        isca = rng.choice(livres)

        def _c3(rot, gate):
            return "%s — %s and I'll send you %s. %s" % (
                rot.format(o=o1), sc.CTA_LITERAL, isca, gate)

        gate = rng.choice(_cabem(GATES, lambda g: _c3(esc, g), TETO_FALA[3]))
        f[2] = _c3(esc, gate)

    return f


def sortear(pagina, rng, led, travas=None):
    """Monta a spec. `travas` fixa eixos (pre-selecao do painel e cadeado)."""
    travas = travas or {}
    usados = led.get(pagina, {})

    # ⭐ O MUNDO VEM PRIMEIRO: ele decide cozinha, bancada, traje, luz, ambiencia,
    # as etnias que aquele lugar comporta E quais LUGARES o payoff aceita.
    # Sorteio por FAMILIA e so' depois por mundo dentro dela.
    fam_trava = travas.get("familia_mundo")
    if travas.get("mundo"):
        mundo = _por_id(MUNDOS, travas["mundo"])
    else:
        if fam_trava and fam_trava != "livre":
            fam = fam_trava
        else:
            fam = _fresco([{"id": f} for f in FAMILIAS_MUNDO],
                          usados.get("familia_mundo", []), rng, "id")["id"]
        mundo = rng.choice([m for m in MUNDOS if m["familia"] == fam])

    # ⭐⭐ O TOGGLE. `livre` (ou ausente) sorteia; qualquer outro valor fixa.
    enq = travas.get("enquadramento")
    if enq in (None, "", "livre"):
        enq = rng.choice(ENQUADRAMENTOS)

    et = travas.get("etnia") or rng.choice(mundo["etnias"])
    cor = travas.get("cor") or rng.choice(mundo["cores"])
    ref = _por_id(REFS, travas["ref"], "cabeca") if travas.get("ref") \
        else rng.choice(REFS)
    # ⭐ MODO BELA — contrato do short_comum, 2026-08-05.
    mulher = (_por_id(MULHERES, travas["mulher"], "cabeca")
              if travas.get("mulher")
              else sc.ref_bela(MULHERES[0], rng) if travas.get("bela")
              else rng.choice(MULHERES))

    poss = _lugares_possiveis(mundo)
    lugar = (_por_id(poss, travas["lugar"]) if travas.get("lugar")
             else _fresco(poss, usados.get("lugar", []), rng, "id"))
    acomp = (_por_id(ACOMPANHAMENTOS, travas["acompanhamento"])
             if travas.get("acompanhamento")
             else _fresco(ACOMPANHAMENTOS, usados.get("acompanhamento", []),
                          rng, "id"))
    gel = (_por_id(PO_E_GEL, travas["gel"]) if travas.get("gel")
           else _fresco(PO_E_GEL, usados.get("gel", []), rng, "id"))

    # ⛔ QUATRO orgaos DIFERENTES no mesmo video, um por slot que o nomeia:
    # perda (c1) · vilao (c1) · resultado (c2) · reacao (c2). A cena 3 reusa o
    # primeiro, 24 segundos depois.
    # ⚠️ Eram DOIS ate' 2026-08-04, e a escassez era a desculpa que empurrava
    # slot para pronome. `NUCLEO` tem 5 grafias — nunca faltou.
    orgaos = rng.sample(NUCLEO, 4)

    spec = {"pagina": pagina, "mundo": mundo, "etnia": et, "cor": cor,
            "enquadramento": enq, "ref": ref, "mulher": mulher, "lugar": lugar,
            "acompanhamento": acomp, "gel": gel, "orgaos": orgaos}
    spec["falas"] = [v for _, v in sorted(_falas(spec, rng).items())]
    return spec


def _pessoa(spec):
    """O homem inteiro — so' usado onde o rosto entra em quadro."""
    r = spec["ref"]
    oc = (", " + r["oculos"]) if r["oculos"] else ""
    return ("a %d-year-old %s man, %s, %s, %s%s, %s, wearing %s"
            % (r["idade"], spec["etnia"], r["porte"], r["cabeca"], r["pelo"],
               oc, r["marca"], _traje(spec)))


def _ancora(spec):
    """⛔ RE7 — a ancora de continuidade. Rosto E idade, nunca so' roupa."""
    r = spec["ref"]
    return RE_ANCORA % (r["idade"], spec["etnia"],
                        _sem_artigo(r["cabeca"]),
                        _sem_artigo(r["marca"]),
                        spec["mundo"]["curto"])


def _mulher(spec):
    w = spec["mulher"]
    return ("a %d-year-old %s woman, %s, %s, %s"
            % (w["idade"], spec["etnia"], w["corpo"], w["cabeca"], w["marca"]))


def montar(spec):
    """Os 7 blocos. Formatacao NOMEADA de ponta a ponta — sao 15+ campos por
    bloco, e um deslocamento de indice posicional troca pronome por cor sem
    estourar erro nenhum (bug que so' aparece no video pronto)."""
    m, ref, lug = spec["mundo"], spec["ref"], spec["lugar"]
    ac, gel = spec["acompanhamento"], spec["gel"]

    v = {
        "coz": m["coz"], "coz_c": m["coz_c"],
        "sup_a": m["sup_a"], "sup": m["sup"],
        "luz": m["luz"], "luz_c": m["luz_c"],
        "etnia": spec["etnia"], "idade": ref["idade"],
        "pessoa": _pessoa(spec), "ancora": _ancora(spec),
        "Ancora": _cap(_ancora(spec)),
        "mulher": _mulher(spec),
        "maos": ref["maos"], "marca_mao": ref["marca_mao"],
        "caixa": RE_CAIXA, "taca": RE_TACA,
        "po": gel["po"], "gel": gel["gel"],
        "pote": ac["pote"], "pote_curto": ac["curto"],
        "lugar": lug["set"], "luz_lugar": lug["luz"],
        "anti": ANTICELEB, "cauda": CAUDA,
    }
    v["nao_toca"] = RE_NAO_TOCA % m["sup"]

    b = {}
    # ⛔ O BLOCO 0 e' o REF do AdBatch: rosto de referencia para a Consistencia
    # Visual. Ele existe nos DOIS modos, porque o rosto aparece na cena 3 em
    # qualquer caso — e sem ele o payoff sai com um homem que ninguem escolheu.
    oc = (" " + _cap(ref["oculos"]) + ".") if ref["oculos"] else ""
    b["BLOCO 0 (REF)"] = (
        "REF 01: Photo of a real person, a %(idade)d-year-old %(etnia)s man, "
        "chest up, facing the camera directly, neutral steady expression with "
        "his mouth closed. %(pessoa_curta)s An ordinary everyday relatable "
        "person with a plain unremarkable face, not a celebrity, not a model, "
        "not an actor, not resembling any famous person. Hands out of frame, "
        "no objects. Plain neutral gray background, soft even frontal light. "
        "Slight sensor grain, soft focus, raw iPhone front camera aesthetic. "
        "No subtitles, no captions, no burned-in text, no watermark."
        % dict(v, pessoa_curta="%s. %s.%s %s. Wearing %s."
               % (_cap(ref["cabeca"]), _cap(ref["pelo"]), oc,
                  _cap(ref["marca"]), _traje(spec))))

    # --- CENA 1 — A PERDA (o hook) ------------------------------------------
    # ⛔ O po' JA' ESTA' caindo no frame 0: nao ha' frame de "antes". Mesma
    # economia do EXTERIOR e do TROCA — 8 segundos nao pagam uma preparacao.
    # ⭐⭐ AQUI MORA O TOGGLE, e ele troca o ENQUADRAMENTO, nunca a acao.
    if spec["enquadramento"] == ENQ_CORTE:
        b["IMAGE 01/03"] = (
            "Overhead close shot in %(coz)s. %(corte)s %(anti)s %(luz)s "
            "%(cauda)s" % dict(v, corte=RE_CORTE % v))
    else:
        b["IMAGE 01/03"] = (
            "%(terceira)s He is the only person in the frame. %(anti)s "
            "%(luz)s %(cauda)s" % dict(v, terceira=RE_TERCEIRA % v))

    # --- CENA 2 — A RECEITA (o mecanismo) -----------------------------------
    # ⚠️ SEM ROSTO NOS DOIS MODOS — e' a cena 2 da fonte, e a mao esquerda
    # chapada em primeiro plano e' o que da' presenca fisica a um homem que nao
    # tem rosto em quadro.
    b["IMAGE 02/03"] = (
        "%(bancada)s %(anti)s %(luz)s %(cauda)s"
        % dict(v, bancada=RE_BANCADA % v))

    # --- CENA 3 — O PAYOFF E O CTA ------------------------------------------
    # ⭐ O objeto da keyword esta' NA MAO no frame em que a boca diz `gelatin,`.
    # ⛔ RE6 — a taca de cubos so' existe aqui. Mostra-la antes entrega o payoff
    # antes da promessa.
    # ⚠️ A ancora de continuidade so' entra no modo `terceira`: no modo `corte`
    # este e' o PRIMEIRO rosto do video, e cobrar continuidade de um rosto que
    # ninguem viu e' regra larga demais (licoes §16).
    # ⚠️ MINUSCULA de proposito: a ancora entra no MEIO da frase (`...to the
    # camera, is the same 62-year-old man...`). A primeira versao usava a forma
    # capitalizada e saia `is The same 62-year-old` — o mesmo defeito que o COLO
    # ja' pagou lendo o render, e aqui ele derrubava tambem o linter RE7, que
    # compara em caixa baixa. Um bug, duas caras.
    quem = "%(ancora)s" if spec["enquadramento"] == ENQ_TERCEIRA else "%(pessoa)s"
    b["IMAGE 03/03"] = (
        ("Medium shot in %(lugar)s, filmed straight on at chest height and "
         "framed from the waist up. Standing centred in the frame, turned to "
         "the camera, is " + quem + ", smiling with his mouth open mid-word as "
         "he speaks, his front teeth even and complete. Beside him at "
         "frame-right, her shoulder against his, stands %(mulher)s, laughing "
         "and looking at him. In his right hand, held up at chest height and "
         "turned so the cubes face the lens, is %(taca)s. They are the only two "
         "people in the frame. %(anti)s %(luz_lugar)s %(cauda)s") % v)

    # ⛔⛔ O TAKE ANIMA A IMAGE — ELE NAO INVENTA OUTRO GESTO.
    # ⚠️ Contradicao entre IMAGE e TAKE e' pior que omissao: a omissao o gerador
    # preenche com o frame; a contradicao ele resolve mexendo no que estava
    # certo (licao lida no render do COLO).
    # ⛔ DESPEJO CRU (ordem do operador): o po' cai e nada mais acontece. Nada
    # cresce, nada vira gel na tela, nada faz morph.
    if spec["enquadramento"] == ENQ_CORTE:
        mov1 = ("His two hands keep the box tipped at exactly the same height "
                "and the same angle over the bowl, and the powder keeps falling "
                "in the same steady stream into the water. Nothing else enters "
                "the frame and his head and body never come into shot.")
        fala1 = ("The voice is the same man whose hands are in the frame, "
                 "speaking over the shot; no face appears.")
    else:
        mov1 = ("He keeps the box tipped at the same height and the same angle "
                "over the bowl in both hands, and the powder keeps falling in "
                "the same steady stream into the water. His eyes stay on the "
                "lens the whole time.")
        fala1 = "He is the only person in the shot, and only he speaks."

    mov = [
        mov1,
        ("His left hand stays flat and still on the %(sup)s in the front of the "
         "frame the whole time. His right hand keeps its grip on "
         "%(pote_curto)s, his forearm resting steady on the %(sup)s, and tips "
         "it a little further over the bowl. %(nao_toca)s" % v),
        ("He holds the coupe of gelatin cubes steady at chest height the whole "
         "time and never sets it down. She stays where she is, her shoulder "
         "against his, and laughs without speaking." % v),
    ]
    elenco = [
        fala1,
        "The voice is the same man whose hands are in the frame, speaking "
        "over the shot; no face appears.",
        "Only the man speaks, straight into the lens; she stays silent.",
    ]
    audio = ["%s, dry powder falling into water. No music." % m["audio"],
             "%s, a spoon against glass. No music." % m["audio"],
             "%s. No music." % lug["audio"]]

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


def lint(spec, blocos):
    ach = []
    falas = spec["falas"]
    m = spec["mundo"]
    corte = spec["enquadramento"] == ENQ_CORTE

    sc.lint_tags(blocos, ach)
    sc.lint_sem_texto(blocos, ach)
    sc.lint_isca_cta(falas[2], ach, "a cena 3 (CTA)")
    sc.lint_cta_literal(falas[2], ach, "a cena 3 (CTA)")

    if not blocos.get("BLOCO 0 (REF)", "").lstrip().upper().startswith("REF"):
        ach.append(("ERRO", "BLOCO 0 sem o cabecalho REF — o AdBatch descarta a "
                            "referencia em silencio"))

    # --- RE21: nenhum placeholder cru sobrevive ate' o prompt ---------------
    # ⛔ Guarda geral, e ela nasceu de um caso real: um `.format()` esquecido no
    # sorteio do vilao mandou `a man's {o} stays broken` para o Dialogue:. O
    # teto de palavras NAO pega — `_palavras` normaliza `{o}` para uma palavra —
    # e nenhuma outra regra olhava para chaves. Custa uma varredura e cobre
    # todos os slots de uma vez, inclusive os que ainda vao existir.
    for i, f in enumerate(falas, 1):
        cru = re.findall(r"\{\w+\}", f)
        if cru:
            ach.append(("ERRO", "RE21: a fala da cena %d tem placeholder cru %s "
                                "— faltou o .format() no sorteio, e isso chega "
                                "literal no Dialogue:" % (i, cru)))
    for nome, txt in blocos.items():
        cru = re.findall(r"\{\w+\}", txt)
        if cru:
            ach.append(("ERRO", "RE21: %s tem placeholder cru %s" % (nome, cru)))

    # --- RE11: tetos e pisos -------------------------------------------------
    for i, f in enumerate(falas, 1):
        n = _palavras(f)
        if n > TETO_FALA[i]:
            ach.append(("ERRO", "RE11: cena %d com %d palavras (teto %d) — a "
                                "narracao passa de 7s" % (i, n, TETO_FALA[i])))
        if n < PISO_FALA[i]:
            ach.append(("AVISO", "RE11: cena %d com %d palavras (piso %d) — "
                                 "sobra silencio nos 8s" % (i, n, PISO_FALA[i])))

    # --- RE12: ⭐⭐ A REACAO NOMEIA O ORGAO (licoes §20) ---------------------
    # ⛔ A regra que fez este agente existir. A ultima sentenca da cena 2 e' a
    # reacao dela, e sem o orgao nela o espectador ouve `She noticed.` e pergunta
    # "notou o QUE?". A prova social morre em silencio, porque a sentenca e'
    # gramaticalmente perfeita e passa em qualquer linter de forma.
    # ⚠️ Escopo deliberadamente ESTREITO: a ULTIMA sentenca da CENA 2, que e' o
    # slot da reacao. Cobrar todo verbo de percepcao do video reprovaria as
    # REJEICOES, que estao certas (licoes §16, "regra larga demais").
    sents2 = _sentencas(falas[1])
    if sents2:
        rea = sents2[-1]
        if not any(o.lower() in rea.lower() for o in NUCLEO):
            ach.append(("ERRO", "RE12: a reacao da cena 2 nao nomeia o orgao — "
                                "%r deixa o espectador perguntando 'notou o "
                                "que?' e a prova social morre em silencio "
                                "(licoes-de-construcao §20)" % rea))
    for linha in REACOES:
        if "{o}" not in linha:
            ach.append(("ERRO", "RE12: entrada do pool REACOES sem `{o}` — %r "
                                "(toda reacao nomeia o orgao)" % linha))

    # --- RE19: a escalada e a isca nao sao a mesma promessa -----------------
    # ⛔ Achado LENDO a saida montada, nao pelo linter (§19). Guarda contra o
    # proximo refactor reintroduzir o sorteio solto.
    cta = falas[2]
    if " — " in cta and "I'll send you " in cta:
        esc = cta.split(" — ", 1)[0]
        isca = cta.split("I'll send you ", 1)[1].split(".", 1)[0]
        if _miolo(esc) == _miolo(isca):
            ach.append(("ERRO", "RE19: a escalada e a isca do CTA sao a mesma "
                                "promessa (%r) — a cena 3 diz a mesma coisa "
                                "duas vezes no take mais denso dos tres"
                        % _miolo(isca)))

    # --- RE13: o mecanismo ---------------------------------------------------
    corpo = " ".join(falas).lower()
    if "gelatin trick" not in corpo:
        ach.append(("ERRO", "RE13: literal `gelatin trick` ausente — sem ele o "
                            "criativo deixa de ser congruente com a VSL"))
    if "gelatin trick" not in falas[1].lower():
        ach.append(("ERRO", "RE13: o `gelatin trick` tem de estar na CENA 2, "
                            "que e' a cena do mecanismo"))

    # --- RE14: a confissao e' em PRIMEIRA PESSOA ----------------------------
    # ⚠️ E' o angulo inteiro. Narradora contando de um terceiro ja' e' o TROCA e
    # o ESCANDALO; aqui quem fala e' o dono do problema.
    if not re.search(r"\b(I|my|me)\b", falas[0]):
        ach.append(("ERRO", "RE14: a cena 1 nao fala em primeira pessoa — a "
                            "confissao do proprio homem e' o angulo"))

    # --- RE15: os beats OBRIGATORIOS da cena 1 -------------------------------
    # ⚠️ Regra de FUNCAO: a perda da' o tamanho do problema, a rejeicao faz o
    # espectador se ver, e o vilao tira a culpa dele. O mais caro de perder e' o
    # terceiro: sem vilao, o homem que assiste conclui que o problema e' ele.
    # ⛔⛔ ERA `< 3` E REPROVAVA A COPY DO PROPRIO OPERADOR (2026-08-04).
    # Quando ele reescreveu o take 1 a mao, a REJEICAO nao estava la': ele
    # preferiu um vilao completo — com o destino nomeado — a tres beats
    # truncados. Regra que reprova a copy certa e' regra mal escrita (§2, §16).
    # ⭐ Obrigatorios: perda (RE22) e vilao (RE20). A rejeicao entra se couber.
    sents1 = _sentencas(falas[0])
    if len(sents1) < 2:
        ach.append(("ERRO", "RE15: a cena 1 tem %d sentenca(s) — ela precisa no "
                            "minimo da perda e do vilao" % len(sents1)))


    # --- RE22: ⭐ a PERDA nomeia QUEM ---------------------------------------
    # ⛔ Ordem do operador, 2026-08-04, lendo o app: `I almost lost her` ->
    # *"lost who? His mom? His sister? Wtf are he talking about?"*. Pronome nao
    # e' referente. A perda diz `my wife` / `my marriage`, com todas as letras.
    # ⚠️⛔ ESTAS LINHAS JA' NASCERAM QUEBRADAS UMA VEZ: escritas por heredoc, o
    # `` do padrao virou um BYTE DE BACKSPACE (0x08) DENTRO da string raw, e o
    # regex passou a exigir um caractere invisivel — reprovava 100% do pool com
    # uma mensagem perfeitamente plausivel. E' a §2 outra vez: linter que
    # reprova tudo, a suspeita e' DELE. Regex se escreve no arquivo, nunca por
    # script com escape.
    quem = r"\b(my wife|my marriage|the woman I married|marriage)\b"
    if sents1 and not re.search(quem, sents1[0], re.I):
        ach.append(("ERRO", "RE22: a perda da cena 1 nao nomeia QUEM se perde — "
                            "%r deixa o espectador perguntando 'perdeu quem?'"
                    % sents1[0]))
    for linha in PERDAS:
        if not re.search(quem, linha, re.I):
            ach.append(("ERRO", "RE22: entrada do pool PERDAS sem dizer quem se "
                                "perde — %r" % linha))

    # --- RE20: ⭐ o vilao NOMEIA quem esconde ou quem lucra ------------------
    # ⛔ Ordem do operador (2026-08-04) e regra de FUNCAO. `Nobody told me this`
    # sem dono e' queixa; `no doctor gets paid for the answer that worked` e'
    # vilao. E' a §20 outra vez, so' que no slot da culpa: sujeito sem dono nao
    # diz nada, e o espectador volta a achar que o problema e' ele.
    # ⚠️⚠️ A UNIDADE E' O BEAT INTEIRO, NAO A ULTIMA SENTENCA — e a primeira
    # versao desta lente errou exatamente isso. Ela olhava so' `sents1[-1]` e
    # reprovou 100% dos sorteios que caiam em `Add up what they took from me.
    # None of it was meant to work.`, cujo agente (`they`) mora na PRIMEIRA
    # sentenca do beat. Regra que reprova a copy certa e' regra mal escrita
    # (licoes §2 e §16). O beat do vilao e' tudo depois da perda e da rejeicao.
    # ⛔⛔ `sents1[1:]`, NAO `sents1[2:]` — corrigido em 2026-08-04.
    # A versao anterior assumia que o vilao comecava sempre na terceira
    # sentenca, porque a rejeicao era obrigatoria. Agora ela e' opcional, e com
    # ela fora `sents1[2:]` pulava a PRIMEIRA sentenca do vilao — justamente a
    # que carrega o agente (`The drug companies own the pill.`) — e reprovava a
    # copy correta. O beat do vilao e' tudo o que vem depois da perda.
    beat = " ".join(sents1[1:])
    if beat and not VILAO_AGENTE.search(beat):
        ach.append(("ERRO", "RE20: o vilao da cena 1 nao nomeia quem esconde nem "
                            "quem lucra — %r e' queixa, nao vilao, e sem dono a "
                            "culpa volta para o espectador" % beat))
    for linha in VILOES:
        if not VILAO_AGENTE.search(linha):
            ach.append(("ERRO", "RE20: entrada do pool VILOES sem agente "
                                "nomeado — %r" % linha))

    # --- RE24: ⭐ DEITICO TERMINAL — `this` no fim nao aponta para nada -------
    # ⛔ Ordem do operador, 2026-08-04, lendo o render do TAKE 01:
    #     "Every television ad points you at the expensive pill and away from
    #      this."  ->  *"Drifting identificado 'away from this.' From what???"*
    #
    # ⚠️ E' a familia do §20 num disfarce novo. La' o vicio era SUJEITO sem
    # objeto (`She noticed.`); aqui e' OBJETO sem substantivo — a frase termina
    # apontando o dedo para o vazio. E o take 1 e' o pior lugar possivel para
    # isso, porque o mecanismo ainda nao foi nomeado: deitico resolve para tras,
    # nunca para frente.
    #
    # ⭐ A lente NAO pode ser "proibido terminar em deitico", senao reprova o CTA
    # (`Comment gelatin and I'll send it`), onde o referente esta' na propria
    # frase — regra que reprova a copy certa e' regra mal escrita (§2, §16).
    # A regra e': termina em deitico nu E a sentenca nao nomeia nada nosso.
    for n, fala in enumerate(falas, 1):
        for s in _sentencas(fala):
            if not re.search(r"\b(this|that|it|these|those|them)\s*[.!?]*\s*$",
                             s, re.I):
                continue
            if re.search(r"\b(gelatin|recipe|trick|mix|mixture|ingredients?|"
                         r"jar|glass|kitchen|counter|bowl)\b", s, re.I):
                continue
            ach.append(("ERRO", "RE24: a cena %d termina num deitico nu — %r "
                                "aponta para um referente que a frase nao "
                                "nomeia ('from WHAT?')" % (n, s)))

    # --- RE25: ⭐ o vilao diz PARA QUE serve o que ele esconde ----------------
    # ⛔ Ordem do operador, 2026-08-04, corrigindo o render a mao:
    #     gerado:  "Nobody owns what my grandfather knew."
    #     devido:  "Nobody owns what my grandfather knew to trully save my
    #               john-son and my marriage"
    # ⚠️ RE20 ja' cobrava o AGENTE e passou nas duas — porque olhava so' o
    # COMECO da frase. O vicio tinha se mudado para o fim: substantivo abstrato
    # sem destino (`the cheap fix`, `the answer`, `what my grandfather knew`).
    # Sem a quarta parte o espectador ouve uma briga com a farmacia e nao sabe o
    # que ele ganha se a farmacia perder.
    for linha in VILOES:
        if not re.search(r"\{o\}|\bmarriage\b|\bmy wife\b|\bhis wife\b|"
                         r"\bnatural trick\b|\brecipe\b", linha, re.I):
            ach.append(("ERRO", "RE25: entrada do pool VILOES sem DESTINO — %r "
                                "nomeia quem esconde mas nao diz para que serve "
                                "o que foi escondido" % linha))

    # --- RE26: ⭐ o resultado nomeia o orgao, nunca um pronome ----------------
    # ⛔ Ordem do operador, 2026-08-04, corrigindo o TAKE 02 a mao:
    #     gerado:  "It came back full and stayed hard..."
    #     devido:  "My tool came back full and stayed hard..."
    # ⚠️ `It` vem logo depois de uma frase que fala de `the gelatin trick`, e um
    # pronome resolve para o substantivo mais proximo — o espectador ouve que O
    # TRUQUE voltou inteiro. E' a §22 num slot novo.
    for linha in RESULTADOS:
        if "{o}" not in linha:
            ach.append(("ERRO", "RE26: entrada do pool RESULTADOS sem `{o}` — "
                                "%r deixa o resultado num pronome" % linha))

    # --- RE4: cota do orgao --------------------------------------------------
    cota = [i for i, f in enumerate(falas, 1)
            if any(o.lower() in f.lower() for o in NUCLEO)]
    if len(cota) < 2:
        ach.append(("ERRO", "RE4: cota do orgao %d/3 (minimo 2) — cenas sem "
                            "substantivo do nucleo: %s"
                    % (len(cota), [i for i in (1, 2, 3) if i not in cota])))
    if len(set(spec["orgaos"])) < 4:
        ach.append(("ERRO", "RE4: o video nao tem quatro grafias distintas do "
                            "orgao — %s" % (spec["orgaos"],)))

    i1, i2, i3 = (blocos["IMAGE 01/03"], blocos["IMAGE 02/03"],
                  blocos["IMAGE 03/03"])
    t1 = blocos["TAKE 01/03"]

    # --- RE2/RE3: ⭐⭐ O TOGGLE cumpre o que promete -------------------------
    # ⛔ Regra de FUNCAO, e ela e' a razao do toggle existir: o modo `corte` NAO
    # pode ter rosto e o modo `terceira` TEM de ter. Sem isto o painel oferece
    # uma escolha que nao muda o prompt — que e' exatamente o slot que passa no
    # linter e nao cumpre a funcao (licoes §4).
    if corte:
        if "out of shot" not in i1:
            ach.append(("ERRO", "RE2: modo `corte` sem o recorte — a cabeca e o "
                                "corpo dele tem de ficar fora de quadro"))
        if "hands are the only part of him" not in i1:
            ach.append(("ERRO", "RE2: modo `corte` sem a declaracao de que so' "
                                "as maos aparecem — o Veo poe o tronco"))
        for tok in ("looks straight into the lens", "his mouth open mid-word"):
            if tok in i1:
                ach.append(("ERRO", "RE2: modo `corte` com %r no IMAGE 01/03 — "
                                    "nao ha' rosto nesta cena" % tok))
        if "only he speaks" in t1:
            ach.append(("ERRO", "RE2: modo `corte` com lip-sync no TAKE 01/03 — "
                                "sem rosto a fala e' voz sobre a cena"))
        if spec["ref"]["marca_mao"] not in i1:
            ach.append(("ERRO", "RE2: o homem entrou sem ancora distintiva na "
                                "mao — no modo `corte` a mao e' a unica "
                                "identidade que ele tem"))
    else:
        if "mouth open mid-word" not in i1:
            ach.append(("ERRO", "RE3: modo `terceira` sem o rosto falando — o "
                                "toggle nao mudou nada no prompt"))
        if "%d-year-old %s man" % (spec["ref"]["idade"], spec["etnia"]) not in i1:
            ach.append(("ERRO", "RE3: modo `terceira` sem a pessoa declarada no "
                                "IMAGE 01/03"))
        # RE7 — a ancora de continuidade so' se cobra quando o rosto ja' apareceu
        if "the same %d-year-old" % spec["ref"]["idade"] not in i3:
            ach.append(("ERRO", "RE7: modo `terceira` sem a ancora `the same "
                                "N-year-old` na cena 3 — o rosto apareceu na "
                                "cena 1 e o Veo troca de pessoa entre blocos"))

    # --- RE16: a cena 2 nunca tem rosto, nos dois modos ---------------------
    if "out of shot" not in i2:
        ach.append(("ERRO", "RE16: IMAGE 02/03 sem manter a cabeca e o corpo "
                            "fora de quadro — a cena 2 e' a bancada, sem rosto"))
    if "left hand rests flat" not in i2:
        ach.append(("ERRO", "RE16: IMAGE 02/03 sem a mao esquerda chapada em "
                            "primeiro plano — e' ela que da' presenca fisica a "
                            "um homem sem rosto, e sem ela a cena vira b-roll"))

    # --- RE1: a caixa, e o cavalo que so' existe nela -----------------------
    for nome in ("IMAGE 01/03", "IMAGE 02/03"):
        if RE_CAIXA not in blocos[nome]:
            ach.append(("ERRO", "RE1: %s sem a caixa de gelatina — ela e' o "
                                "prop-mestre e o unico claim do video" % nome))
    # ⛔ O cavalo VIVO foi cortado pelo operador. Ele so' pode existir como
    # silhueta impressa, e a unica string que a carrega e' a RE_CAIXA.
    for nome, txt in blocos.items():
        if nome.startswith("BLOCO"):
            continue
        fora = txt.replace(RE_CAIXA, "")
        if re.search(r"\bhorses?\b", fora, re.I):
            ach.append(("ERRO", "RE1: %s tem cavalo fora da caixa — o animal "
                                "vivo foi cortado (ordem do operador "
                                "2026-08-04) e so' a silhueta impressa fica"
                        % nome))

    # --- RE6: a taca de cubos so' na cena 3 ---------------------------------
    for nome in ("IMAGE 01/03", "IMAGE 02/03"):
        if "gelatin cubes" in blocos[nome]:
            ach.append(("ERRO", "RE6: taca de cubos fora da cena 3 (%s) — "
                                "entrega o payoff antes da promessa" % nome))
    if "gelatin cubes" not in i3:
        ach.append(("ERRO", "RE6: a cena 3 tem de mostrar a taca de cubos na "
                            "mao — e' o objeto da keyword"))

    # --- RE17: DESPEJO CRU — nada cresce em cena nenhuma --------------------
    # ⚠️ Ordem do operador, 2026-08-04. Este agente NAO tem morph: o bit visual
    # e' o po' caindo. A excecao e' vazia de proposito.
    sc.lint_nada_cresce(blocos, ach, rotulo="RE17")

    # --- P12: zero marca legivel (a excecao do EXTERIOR e' so' dele) --------
    for nome, txt in blocos.items():
        if nome.startswith("BLOCO"):
            continue
        for marca in ("arm & hammer", "great value", "kroger", "brand name",
                      "printed label", "logo"):
            if marca in txt.lower():
                ach.append(("ERRO", "P12: %s traz marca/rotulo legivel (%r) — a "
                                    "excecao da marca real e' nominal do "
                                    "EXTERIOR" % (nome, marca)))

    # --- congruencia do lugar com o mundo -----------------------------------
    if spec["lugar"] not in _lugares_possiveis(m):
        ach.append(("ERRO", "RE18: o lugar %r nao e' congruente com o mundo %r "
                            "— cada mundo declara as familias que comporta"
                    % (spec["lugar"]["id"], m["id"])))

    # --- a superficie do mundo e' a unica em cena ---------------------------
    junto = " ".join(t for k, t in blocos.items() if not k.startswith("BLOCO"))
    if m["sup"] != "counter" and re.search(r"\bcounter\b", junto):
        ach.append(("ERRO", "`counter` sobrou num mundo de %s (%s) — literal "
                            "esquecido no refactor" % (m["sup"], m["id"])))
    if re.search(r"\ba [aeiou]", junto):
        ach.append(("ERRO", "artigo errado: %r"
                    % re.search(r"\ba [aeiou]\w+", junto).group()))

    # ⛔⛔ TAKE CONTRA IMAGE — 2026-08-05. Este motor tem `lint()` proprio e NAO
    # passa pelo `lint_curto`, entao a lente compartilhada nao chegava aqui.
    # ⚠️ Foi assim que a primeira varredura deu "limpo" para sete motores: eles
    # nunca rodaram a lente. "Limpo" sem cobertura e' o pior resultado possivel,
    # porque parece verde. Medir a lente e' medir TAMBEM se ela e' chamada.
    # ⛔ PAINEL HONESTO — 2026-08-05. Nenhum eixo desenhado no painel pode
    # deixar de chegar ao video.
    sc.lint_painel_honesto(sys.modules[__name__], spec, blocos, ach)

    sc.lint_take_vs_image(blocos, ach)

    return ach


# ---------------------------------------------------------------------------
# UI
# ---------------------------------------------------------------------------

def resumo_pt(spec):
    m = spec["mundo"]
    enq = ("corte macro só nas mãos" if spec["enquadramento"] == ENQ_CORTE
           else "plano médio, ele em quadro")
    return ("Homem %s de %d anos, em %s (%s). Cena 1 (%s): despeja a caixa de "
            "gelatina na tigela. Cena 2: a bancada com %s, sem rosto. Cena 3 "
            "em %s, com a parceira de %d anos e a taça de cubos."
            % (spec["etnia"], spec["ref"]["idade"],
               m["id"].replace("_", " "), m["familia"], enq,
               spec["acompanhamento"]["nome"],
               spec["lugar"]["id"].replace("_", " "), spec["mulher"]["idade"]))


def nova_fala(spec, i, rng):
    """Re-sorteia a copy de UMA cena, ja' formatada com os slots deste video."""
    spec["falas_map"] = {j: f for j, f in enumerate(spec["falas"])}
    return _falas(spec, rng, quais=(i,))[i]


def _apos_mundo(spec, rng):
    """Trocou o MUNDO: etnia, cor e LUGAR tem de vir do mundo novo, senao o
    botao `trocar` deixa em cena a incongruencia que os MUNDOS existem para
    impedir."""
    if spec["etnia"] not in spec["mundo"]["etnias"]:
        spec["etnia"] = rng.choice(spec["mundo"]["etnias"])
    if spec["cor"] not in spec["mundo"]["cores"]:
        spec["cor"] = rng.choice(spec["mundo"]["cores"])
    poss = _lugares_possiveis(spec["mundo"])
    if spec["lugar"] not in poss:
        spec["lugar"] = rng.choice(poss)


EIXOS_QUE_MEXEM_NA_COPY = {
    "mundo": _apos_mundo,
}

TETO_LEDGER = {"familia_mundo": len(FAMILIAS_MUNDO), "lugar": len(LUGARES),
               "acompanhamento": len(ACOMPANHAMENTOS), "gel": len(PO_E_GEL)}

MIN_OPCOES = 7          # piso por eixo visual


# ---------------------------------------------------------------------------
# AUTOTESTE
# ---------------------------------------------------------------------------

def autoteste(n=600):
    """As invariantes do agente, MEDIDAS, com controles positivos.

    ⚠️ Existe porque a licao e' sempre a mesma: verificar a FORMA e declarar
    pronto sem verificar a FUNCAO. Pool bonito nao prova nada; o que prova e' o
    motor rodando 600 vezes e um sabotador confirmando que cada checagem SABE
    reprovar. `0 ERRO` num lote grande e' SUSPEITA, nao aprovacao.
    """
    falhas = []
    vistos = collections.defaultdict(set)
    fam = collections.Counter()
    fam_lug = collections.Counter()
    enq = collections.Counter()
    larguras = {1: [], 2: [], 3: []}

    for seed in range(n):
        spec = sortear("joe", random.Random(seed), {}, {})
        blocos = montar(spec)
        for tipo, msg in lint(spec, blocos):
            if tipo == "ERRO":
                falhas.append("seed %d (%s/%s): %s"
                              % (seed, spec["mundo"]["id"],
                                 spec["enquadramento"], msg))
        vistos["mundo"].add(spec["mundo"]["id"])
        vistos["etnia"].add(spec["etnia"])
        vistos["lugar"].add(spec["lugar"]["id"])
        vistos["ref"].add(spec["ref"]["marca"])
        vistos["mulher"].add(spec["mulher"]["marca"])
        vistos["acompanhamento"].add(spec["acompanhamento"]["id"])
        vistos["gel"].add(spec["gel"]["id"])
        fam[spec["mundo"]["familia"]] += 1
        fam_lug[spec["lugar"]["fam"]] += 1
        enq[spec["enquadramento"]] += 1
        for i, f in enumerate(spec["falas"], 1):
            larguras[i].append(_palavras(f))
        if spec["etnia"] not in spec["mundo"]["etnias"]:
            falhas.append("seed %d: etnia fora do mundo" % seed)

        # ⛔ §19 — a frase se confere no PROMPT MONTADO, nunca no fonte: o Python
        # quebra string longa em literais adjacentes e o grep nunca ve a frase
        # inteira. Aqui a checagem roda no texto renderizado, com os espacos
        # normalizados.
        for chave, txt in blocos.items():
            if re.search(r"\s\s", txt) or "  " in txt:
                falhas.append("seed %d: %s com espaco duplo (concatenacao)"
                              % (seed, chave))
                break

    # cobertura
    for eixo, pool in (("mundo", MUNDOS), ("lugar", LUGARES),
                       ("acompanhamento", ACOMPANHAMENTOS), ("gel", PO_E_GEL)):
        if len(vistos[eixo]) != len(pool):
            falhas.append("%s: %d de %d nunca sorteados"
                          % (eixo, len(pool) - len(vistos[eixo]), len(pool)))
    for nome, pool in (("MUNDOS", MUNDOS), ("LUGARES", LUGARES),
                       ("REFS", REFS), ("MULHERES", MULHERES),
                       ("ACOMPANHAMENTOS", ACOMPANHAMENTOS),
                       ("PO_E_GEL", PO_E_GEL),
                       ("PERDAS", PERDAS), ("REJEICOES", REJEICOES),
                       ("VILOES", VILOES),
                       ("VIRADAS", VIRADAS), ("RESULTADOS", RESULTADOS),
                       ("REACOES", REACOES), ("ESCALADAS", ESCALADAS)):
        if len(pool) < MIN_OPCOES:
            falhas.append("eixo %s com %d opcoes (minimo %d)"
                          % (nome, len(pool), MIN_OPCOES))
    # nenhuma familia de mundo domina
    for f, q in fam.items():
        if q > n * 0.25:
            falhas.append("familia de mundo %s levou %.1f%% do lote (teto 25%%)"
                          % (f, 100.0 * q / n))
    # ⚠️ o toggle tem de sair equilibrado quando ninguem trava
    for e, q in enq.items():
        if not 0.35 <= q / float(n) <= 0.65:
            falhas.append("enquadramento %s em %.1f%% do lote (faixa 35-65%%)"
                          % (e, 100.0 * q / n))
    # ⚠️ nenhuma ENTRADA de lugar passa de 17% — a familia `garagem` domina, que
    # e' o que o operador pediu, mas nenhuma garagem sozinha vira bordao
    conc = collections.Counter()
    for seed in range(n):
        conc[sortear("joe", random.Random(seed), {}, {})["lugar"]["id"]] += 1
    for lid, q in conc.items():
        if q > n * 0.17:
            falhas.append("lugar %s levou %.1f%% do lote (teto 17%%)"
                          % (lid, 100.0 * q / n))

    # ---- CONTROLES POSITIVOS E NEGATIVOS -----------------------------------
    # ⚠️ Toda lente nova nasce com os dois, e eles rodam ANTES de qualquer numero
    # ser olhado. O caso que o operador reprovou entra como controle.
    ctrl = []

    # ⭐⭐ [RE12] O CONTROLE QUE O OPERADOR ESCREVEU: `She noticed.` tem de
    # reprovar, e `she noticed his Johnson harder than ever` tem de passar.
    s = sortear("joe", random.Random(1), {}, {})
    b = montar(s)
    # ⛔⛔ `\s*` NO PADRAO, E ELE FALTAVA — o controle ficou CEGO em 2026-08-04 e
    # so' apareceu porque o autoteste roda os controles antes dos numeros.
    # `[^.]+\.$` trocava a ultima sentenca SEM o espaco que a separava, gerando
    # `...twenty years.She noticed.`; `_sentencas` divide em `. ` e devolvia as
    # duas GRUDADAS como uma so'. A sentenca grudada carregava o orgao do
    # RESULTADO, entao RE12 passava — o controle media uma string que o motor
    # nunca produz. So' comecou a falhar quando o resultado passou a nomear o
    # orgao; antes disso ele acertava por acidente.
    # ⚠️ Controle que so' funciona por coincidencia da copy vizinha nao e'
    # controle. E' a §16 aplicada ao proprio medidor.
    _ult = r"\s*[^.]+\.$"
    s_neg = dict(s, falas=list(s["falas"]))
    s_neg["falas"][1] = re.sub(_ult, " She noticed.", s_neg["falas"][1])
    if not any("RE12" in msg for _, msg in lint(s_neg, b)):
        ctrl.append("[RE12] NAO acusa `She noticed.` — o caso que o operador "
                    "reprovou passa pelo medidor (licoes §16)")
    s_pos = dict(s, falas=list(s["falas"]))
    s_pos["falas"][1] = re.sub(_ult,
                               " She noticed his Johnson harder than ever.",
                               s_pos["falas"][1])
    if any("RE12" in msg for _, msg in lint(s_pos, b)):
        ctrl.append("[RE12] acusa a forma CERTA — regra larga demais")

    # ⭐ [RE19] O DEFEITO QUE EU LI NA SAIDA vira controle — se o medidor nao
    # reprovar exatamente a frase que me fez escrever a regra, ele mede outra
    # coisa (licoes §16).
    s_r19 = dict(s, falas=list(s["falas"]))
    s_r19["falas"][2] = ("If you want the whole recipe — %s and I'll send you "
                         "the whole recipe. Follow me first, or I can't reply."
                         % sc.CTA_LITERAL)
    if not any("RE19" in msg for _, msg in lint(s_r19, b)):
        ctrl.append("[RE19] NAO acusa escalada e isca identicas — o caso que eu "
                    "li na saida passa pelo medidor")
    s_r19b = dict(s, falas=list(s["falas"]))
    s_r19b["falas"][2] = ("If you want the whole recipe — %s and I'll send you "
                          "the exact measurements. Follow me first, or I can't "
                          "reply." % sc.CTA_LITERAL)
    if any("RE19" in msg for _, msg in lint(s_r19b, b)):
        ctrl.append("[RE19] acusa promessas DIFERENTES — regra larga demais")

    # ⭐ [RE21] o placeholder cru — o caso que eu li na saida vira controle
    s21 = dict(s, falas=list(s["falas"]))
    s21["falas"][0] = s21["falas"][0] + " Somebody profits while his {o} sits."
    if not any("RE21" in msg for _, msg in lint(s21, b)):
        ctrl.append("[RE21] NAO acusa placeholder cru na fala — `{o}` chegaria "
                    "literal no Dialogue:")

    # [RE13] gelatin trick fora da cena 2
    s4 = dict(s, falas=list(s["falas"]))
    s4["falas"][1] = s4["falas"][1].replace("gelatin trick", "morning routine")
    if not any("RE13" in msg for _, msg in lint(s4, b)):
        ctrl.append("[RE13] nao acusa a cena 2 sem o `gelatin trick`")

    # [RE15] cena 1 reduzida a um beat so'
    s5 = dict(s, falas=list(s["falas"]))
    s5["falas"][0] = _sentencas(s5["falas"][0])[0]
    if not any("RE15" in msg for _, msg in lint(s5, b)):
        ctrl.append("[RE15] nao acusa a cena 1 com um unico beat")

    # ⭐ [RE20] vilao sem dono — o controle e' a diferenca entre queixa e vilao
    # ⚠️ Montado a partir da PERDA sozinha, nao de `[:2]`: com a rejeicao
    # opcional, `sents1[1]` tanto pode ser a rejeicao quanto a primeira sentenca
    # do vilao (que tem agente), e o controle virava sorteio.
    s20 = dict(s, falas=list(s["falas"]))
    s20["falas"][0] = (_sentencas(s["falas"][0])[0]
                       + " It was never going to work.")
    if not any("RE20" in msg for _, msg in lint(s20, b)):
        ctrl.append("[RE20] NAO acusa vilao sem dono — `It was never going to "
                    "work.` e' queixa e passou pelo medidor")

    # ⭐ [RE24] deitico terminal — a frase que o operador reprovou, literal
    s24 = dict(s, falas=list(s["falas"]))
    s24["falas"][0] = (_sentencas(s["falas"][0])[0] + " Every television ad "
                       "points you at the expensive pill and away from this.")
    if not any("RE24" in msg for _, msg in lint(s24, b)):
        ctrl.append("[RE24] NAO acusa `away from this.` — o deitico nu passou")
    # ⚠️ controle positivo: o CTA termina em `it` com o referente na frase e
    # NAO pode ser acusado.
    if any("RE24" in msg for _, msg in lint(s, b)):
        ctrl.append("[RE24] acusa a copy limpa — regra larga demais")

    # ⭐ [RE25/RE26] os dois pools, na forma que o operador reprovou
    if any("{o}" not in x for x in RESULTADOS):
        ctrl.append("[RE26] ha' entrada de RESULTADOS sem `{o}` — o pronome nu "
                    "voltou")
    if not re.search(r"\{o\}|marriage|natural trick|recipe",
                     "|".join(VILOES), re.I):
        ctrl.append("[RE25] o pool VILOES perdeu o destino")
    s20b = dict(s, falas=list(s["falas"]))
    s20b["falas"][0] = " ".join(_sentencas(s["falas"][0])[:2]
                                + ["Doctors don't want you knowing this one."])
    if any("RE20" in msg for _, msg in lint(s20b, b)):
        ctrl.append("[RE20] acusa a linha que o OPERADOR ditou — regra larga "
                    "demais")

    # ⭐ [RE2/RE3] O TOGGLE — os dois modos, cada um com o seu sabotador
    s_c = sortear("joe", random.Random(2), {}, {"enquadramento": ENQ_CORTE})
    b_c = montar(s_c)
    if s_c["enquadramento"] != ENQ_CORTE:
        ctrl.append("[toggle] a trava `corte` nao foi respeitada no sorteio")
    bc = dict(b_c)
    bc["IMAGE 01/03"] = bc["IMAGE 01/03"].replace(
        "hands are the only part of him", "whole body is")
    if not any("RE2" in msg for _, msg in lint(s_c, bc)):
        ctrl.append("[RE2] nao acusa o modo `corte` mostrando o corpo")
    if [m2 for t, m2 in lint(s_c, b_c) if t == "ERRO"]:
        ctrl.append("o modo `corte` limpo esta' sendo reprovado")

    s_t = sortear("joe", random.Random(2), {}, {"enquadramento": ENQ_TERCEIRA})
    b_t = montar(s_t)
    if s_t["enquadramento"] != ENQ_TERCEIRA:
        ctrl.append("[toggle] a trava `terceira` nao foi respeitada no sorteio")
    bt = dict(b_t)
    bt["IMAGE 01/03"] = bt["IMAGE 01/03"].replace("mouth open mid-word", "mouth shut")
    if not any("RE3" in msg for _, msg in lint(s_t, bt)):
        ctrl.append("[RE3] nao acusa o modo `terceira` sem o rosto falando")
    bt2 = dict(b_t)
    bt2["IMAGE 03/03"] = bt2["IMAGE 03/03"].replace(
        "the same %d-year-old" % s_t["ref"]["idade"], "a")
    if not any("RE7" in msg for _, msg in lint(s_t, bt2)):
        ctrl.append("[RE7] nao acusa a cena 3 sem a ancora de continuidade")
    if [m2 for t, m2 in lint(s_t, b_t) if t == "ERRO"]:
        ctrl.append("o modo `terceira` limpo esta' sendo reprovado")

    # ⛔ E O TOGGLE PRECISA MUDAR O PROMPT — controle contra o slot que existe e
    # nao faz nada (licoes §4). Mesma seed, modos diferentes, IMAGE 01 igual =
    # o painel oferece uma escolha decorativa.
    if b_c["IMAGE 01/03"] == b_t["IMAGE 01/03"]:
        ctrl.append("[toggle] os dois modos geram o MESMO IMAGE 01/03 — o "
                    "toggle nao cumpre a funcao pela qual existe")

    # [RE1] o cavalo vivo
    b1 = dict(b)
    b1["IMAGE 03/03"] += " A black horse stands behind them."
    if not any("RE1" in msg for _, msg in lint(s, b1)):
        ctrl.append("[RE1] nao acusa cavalo vivo fora da caixa")

    # [RE6] taca adiantada
    b6 = dict(b)
    b6["IMAGE 01/03"] += " " + RE_TACA
    if not any("RE6" in msg for _, msg in lint(s, b6)):
        ctrl.append("[RE6] nao acusa a taca de cubos fora da cena 3")

    # [RE16] a mao chapada
    b7 = dict(b)
    b7["IMAGE 02/03"] = b7["IMAGE 02/03"].replace("left hand rests flat",
                                                  "left hand is somewhere")
    if not any("RE16" in msg for _, msg in lint(s, b7)):
        ctrl.append("[RE16] nao acusa a cena 2 sem a mao chapada em primeiro plano")

    # e o lote limpo NAO pode ser acusado
    if [m2 for t, m2 in lint(s, b) if t == "ERRO"]:
        ctrl.append("o lote limpo esta' sendo reprovado — regra que reprova "
                    "tudo nunca foi testada")

    print("MUNDOS %d em %d familias | LUGARES %d em %d familias | REFS %d | "
          "MULHERES %d" % (len(MUNDOS), len(FAMILIAS_MUNDO), len(LUGARES),
                           len(FAMILIAS_LUGAR), len(REFS), len(MULHERES)))
    print("%d videos | mundos %d/%d | etnias %d | lugares %d/%d | refs %d"
          % (n, len(vistos["mundo"]), len(MUNDOS), len(vistos["etnia"]),
             len(vistos["lugar"]), len(LUGARES), len(vistos["ref"])))
    print("familia de mundo mais frequente: %s com %.1f%%"
          % (fam.most_common(1)[0][0], 100.0 * fam.most_common(1)[0][1] / n))
    print("familia de lugar mais frequente: %s com %.1f%% (garagem e' para "
          "dominar — ordem do operador)"
          % (fam_lug.most_common(1)[0][0],
             100.0 * fam_lug.most_common(1)[0][1] / n))
    print("toggle: %s"
          % " | ".join("%s %.1f%%" % (k, 100.0 * q / n) for k, q in enq.items()))
    for i in (1, 2, 3):
        L = larguras[i]
        print("  cena %d: %d-%d palavras (media %.1f) | piso %d teto %d | "
              "%.2f p/s" % (i, min(L), max(L), sum(L) / float(len(L)),
                            PISO_FALA[i], TETO_FALA[i],
                            sum(L) / float(len(L)) / 8))
    print("  video: media %.1f palavras"
          % (sum(sum(larguras[i]) for i in (1, 2, 3)) / float(n)))

    if ctrl:
        # ⚠️ Marcador ASCII de proposito: o console do Windows e' cp1252 e o
        # `⛔` levanta UnicodeEncodeError — e esta linha so' e' impressa QUANDO
        # HA' FALHA, ou seja, o crash aconteceria na hora em que o relatorio
        # importa.
        print("\n>> O AUTOTESTE ESTA' CEGO:")
        for c in ctrl:
            print("   %s" % c)
    if falhas:
        print("\n>> %d FALHA(S):" % len(falhas))
        for f in falhas[:20]:
            print("   %s" % f)
    if not falhas and not ctrl:
        print("\nAUTOTESTE OK — e os controles positivos reprovam quando devem.")
    return 1 if (falhas or ctrl) else 0


def main():
    ap = argparse.ArgumentParser(description="Randomizador do agente RECEITA SHORT")
    ap.add_argument("--pagina", choices=sorted(ETNIA))
    ap.add_argument("--n", type=int, default=1)
    ap.add_argument("--seed", type=int)
    ap.add_argument("--nicho", choices=FAMILIAS_MUNDO)
    ap.add_argument("--cena1", choices=ENQUADRAMENTOS,
                    help="fixa o enquadramento da cena 1 (default: sorteia)")
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
    travas = {}
    if a.nicho:
        travas["familia_mundo"] = a.nicho
    if a.cena1:
        travas["enquadramento"] = a.cena1

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
                              ("lugar", spec["lugar"]["id"]),
                              ("acompanhamento", spec["acompanhamento"]["id"]),
                              ("gel", spec["gel"]["id"])):
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
