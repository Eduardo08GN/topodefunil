#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE WIFE 16 — o casamento na beira do fim · 2 takes de 8s = 16 segundos.

⭐⭐ O SEGUNDO ANGULO DO PARQUE EM QUE O HOMEM FALA E A MULHER E' MUDA (o outro
e' o GOOD 16). Aqui a inversao nao e' so' de quem narra: e' de QUAL PROVA o
video mostra. Nos outros vinte a prova e' um corpo, um prop ou um copo. Neste
angulo **a prova e' o casamento** — bracos cruzados no take 1, corpo colado no
take 2. A inversao E' o video.

FONTE: reel do Facebook 1244976845366022.
⚠️⚠️ LEITURA OTICA PENDENTE. O video NAO pode ser baixado (login exigido). O que
esta' aqui vem de **UM FRAME** que o operador mandou (take 1, elemento por
elemento) e da especificacao escrita dele. Consequencia declarada, para ninguem
tratar como verbatim de fonte:

    ⛔ OS POOLS DE FALA SAO CONSTRUCAO NOSSA sob o CONTRATO DE COPY 16s, nao
       transcricao. Eles serao REFINADOS quando o mp4 chegar — e ate' la' o
       criterio deles e' o contrato (`CONTRATO-COPY-16S.md`), nao a fonte.

O ARCO — 2 cenas de 8s, destino AdBatch Vertical 2:

    take 1  A CAMA FRIA     ele em primeiro plano na beirada da cama, tronco
                            nu, ombros caidos · ela atras, deitada, camisola,
                            BRACOS CRUZADOS, olhando para o outro lado
                            copy: a falha DELE + o custo conjugal
    take 2  A VIRADA        o MESMO homem, com rosto, dentro d'agua (piscina,
                            jacuzzi, banheira) · ela COLADA nele · os dois com
                            um copo, bebendo
                            copy: mecanismo com razao -> prova -> CTA

⛔⛔ AS QUATRO DECISOES DO OPERADOR (2026-08-10) — NAO SE REABREM
-----------------------------------------------------------------------------
 1. NARRADOR = ELE. `SEXOS = ("homem",)`. A mulher e' MUDA nos dois takes.
 2. A BEBIDA E' O PROPRIO GELATIN TRICK. O copo nao e' cenario: e' a prova
    visual do que a copy vende. Por isso o pool `COPOS` nao e' de bebidas — e'
    de COMO O PREPARO APARECE em quadro.
 3. A REGIAO ARRASTA TUDO. Um eixo so' (`mundo`) move etnia + quarto + agua +
    luz + audio + traje dela. Mecanica do FALTA 16 (`MUNDOS` com `etnias`)
    fundida com a do GOOD 16 (mundo aquatico com `agua`, `luz`, `audio`).
 4. NO TAKE 2 O HOMEM APARECE COM ROSTO, e e' O MESMO do take 1.

⛔⛔ A DECISAO 4 EXIGE ANCORA DE CONTINUIDADE FORTE, e isso e' licao paga: no
VAZAMENTO o corpo-prova voltou na cena seguinte como um senhor de oculos e
bigode — e como o TAKE dizia `Only he speaks`, o ESTRANHO falava a fala do REF.
Aqui o bloco 2 repete idade + etnia + a marca facial sorteada + o sinal
sorteado + `It is the same man`. Lente WF3 cobra os cinco.

⛔ NAO EXISTE PROP FALICO NESTE ANGULO, e nao se inventa um. A prova e' o
casamento. A lente WF6 reprova qualquer geoduck, peca anatomica ou proxy de
legume que alguem tente "consertar" para ca' no futuro.

⛔ O frame da fonte tem legenda QUEIMADA ("ABOUT TO LEAVE"). Nos nao queimamos
texto: a legenda nasce depois, no Veo Editor, a partir do Whisper. A trava
`No on-screen text, no watermark` vale em todo bloco (WF5).

⚠️ PENDENCIA REGISTRADA — A GEOMETRIA DA FALA NO TAKE 1. O frame mostra o homem
DE PERFIL e de olhar baixo; mas ele e' o NARRADOR (decisao 1) e precisa falar na
lente. O motor resolve com o TRONCO virado para longe dela e o ROSTO virado
para a camera — a postura derrotada do frame fica de pe' e a fala tem para onde
sair. **Isto e' cena, e cena e' alcada do operador**: esta' aqui declarado para
ser confirmado, nao para passar despercebido.

    python funil-organico/wife16_short.py --pagina joe --n 1
    python funil-organico/wife16_short.py --autoteste
    python funil-organico/wife16_short_app.py
"""

import argparse
import json
import os
import random
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
if AQUI not in sys.path:
    sys.path.insert(0, AQUI)

import short_comum as sc                                        # noqa: E402
from nucleo_sonoro import sonorizar                             # noqa: E402

# ⛔ Os apelidos do orgao. O motor SORTEIA de `sc.APELIDOS_16` (CT4b: pecker,
# wiener, Johnson); esta lista e' maior de proposito porque e' com ela que as
# LENTES detectam o orgao numa fala — `soldier` e `tool` continuam aqui so'
# para serem DETECTADOS, nunca para serem sorteados.
NUCLEO = ["Johnson", "pecker", "wiener", "soldier", "tool"]

LEDGER = os.path.join(AQUI, ".wife-16-ledger.json")

TITULO = "AGENTE WIFE 16"
SLUG = "wife-16"
SUBTITULO = ("2 takes de 8s = 16 segundos · a cama fria e a virada na agua · "
             "o homem fala e ela e' muda · a prova e' o casamento")

CENAS_UI = ["1 · A CAMA FRIA", "2 · A VIRADA NA AGUA"]

# ⛔⛔ DUAS CENAS no teto FISICO de 25 palavras (8s a ~3,1 p/s). O teto vem de
# RENDER, nao de teoria: 32 cortou, 28 cortou, 25 nao.
TETO_FALA = {1: 25, 2: 25}
# ⛔ O piso e' ARITMETICA, nao gosto: e' a soma dos MINIMOS de cada beat menos
# uma folga. Piso calibrado com um beat que nao existe e' alarme que sempre
# dispara — e alarme que sempre dispara ensina a ignorar o linter inteiro.
PISO_FALA = {1: 20, 2: 22}

# ⛔ Congruencia inviolavel: a etnia do REF casa com a etnia do avatar da
# pagina. ⭐ Neste angulo o REF que fala e' o HOMEM — entao a pagina governa
# ELE. A mulher fica solta (mesma politica do GOOD 16).
ETNIA = {
    "roy": "white American", "dean": "white American",
    "earl": "white American",
    "jason": "Black American", "philippe": "Black American",
    "joe": "white American", "ray": "white American", "matt": "white American",
    "marcus": "Black American", "chuck": "Black American",
}

# ⭐ QUEM NARRA — o segundo motor do parque com narrador HOMEM.
# ⚠️ Com UM sexo so' a UI nao desenha botao nenhum, que e' o certo: botao que
# nao trava nada e' pior que botao nenhum.
SEXOS = ("homem",)

# ⛔ SEM MODO BELA aqui, e a ausencia e' DECLARADA. A mulher deste angulo ja'
# nasce sob a LEI DO REF (25-38, bonita, marca facial, zero oculos/grisalho) em
# TODAS as entradas do pool — um toggle "ref bela" nao mudaria um pixel, e
# toggle que nao muda nada e' a forma-sem-funcao que o repo ja' pagou tres
# vezes. O mesmo vale para o MODO_FORTE: ele nao existe porque o corpo dele nao
# e' o argumento aqui (o argumento e' ela voltando).
MODO_BELA = False
# ⭐ O TERCEIRO modo do repo, e o primeiro que mexe na CENA e nao na pessoa.
# O `ui_agente` desenha o botao sem o prefixo `ref` e NAO o desliga quando o
# operador trava a REF na tela — ver `MODOS_NAO_REF` la' (a tupla se chamava
# `MODOS_DE_CENA` ate' 2026-08-12, quando entrou nela um modo de COPY).
MODO_RECEITA = True
MODO_FORTE = False

# ⛔ A etnia sai da PAGINA (nao do mundo), entao o seletor clara/escura do
# painel funciona trocando de pagina — que e' o comportamento padrao. Declarar
# PELE_TRAVAVEL aqui acenderia um caminho que este motor nao usa.
PELE_TRAVAVEL = False


# ===========================================================================
# ⭐⭐ MUNDOS — 15 ARQUETIPOS POR REGIAO DOS EUA
# ===========================================================================
# ⛔ ORDEM DO OPERADOR: pool de arquetipos por regiao dos EUA, como no FALTA 16.
# O funil e' US e o espectador tem de reconhecer o quarto como o da casa dele.
#
# ⭐⭐ CADA ENTRADA CARREGA OS DOIS AMBIENTES DA MESMA CASA — o quarto (take 1)
# E a agua (take 2). Isso nao e' capricho de redacao: o video corta de um para o
# outro em 8 segundos, e se os dois nao forem a MESMA casa o espectador le' dois
# videos colados. E' por isso que a agua sempre diz `the same <casa>`.
#
# ⚠️ "Variar etnia e' arrastar o mundo inteiro": cada entrada leva quarto, agua,
# luz, audio, camisola, traje de banho E etnia juntos. Trocar so' o rosto deixa
# a casa errada.
#
# ⛔ E cada mundo declara `etnias`, que e' a mecanica do FALTA 16: a etnia da
# PAGINA filtra quais mundos podem ser sorteados. Sem isso a congruencia
# quebrava pelo cenario, nao pelo rosto.
MUNDOS = [
    {"id": "apalache", "familia": "apalache", "regiao": "Apalaches",
     "q_cen": "a bedroom in an Appalachian farmhouse, painted board walls and "
              "a heavy quilt pushed down to the foot of the bed",
     "q_luz": "one warm lamp on the far nightstand, the rest of the room dark",
     "q_audio": "wind in the trees outside, an old house settling",
     "a_cen": "the back porch of the same Appalachian farmhouse, tall pines "
              "crowding the edge of the yard",
     "a_agua": "a round cedar hot tub set into the porch boards, the water "
               "moving",
     "a_luz": "late afternoon sun coming in low and warm through the pines",
     "a_audio": "cicadas, water moving in the tub, a chainsaw far off",
     "dela_q": "a black satin nightgown",
     "dela_a": "a white bikini top",
     "etnias": ["white American"]},

    {"id": "sulista", "familia": "sulista", "regiao": "Sul profundo",
     "q_cen": "a bedroom in a Southern house, pale yellow beadboard walls and "
              "a ceiling fan turning slowly overhead",
     "q_luz": "one warm bedside lamp, the corners of the room in shadow",
     "q_audio": "crickets outside, a ceiling fan turning",
     "a_cen": "the back yard of the same Southern house, a plank fence and a "
              "magnolia over the far corner",
     "a_agua": "a round above-ground pool with a wooden deck built around it",
     "a_luz": "warm late afternoon light coming flat across the yard",
     "a_audio": "cicadas, water lapping the pool wall, a screen door",
     "dela_q": "a deep red satin nightgown",
     "dela_a": "a coral bikini top",
     "etnias": ["Black American"]},

    {"id": "texas", "familia": "texas", "regiao": "Texas",
     "q_cen": "a bedroom in a Texas ranch house, plaster walls and a heavy "
              "wooden headboard",
     "q_luz": "a single lamp on one nightstand, the rest of the room low and "
              "dark",
     "q_audio": "dry wind against the window, a window unit humming",
     "a_cen": "the back yard of the same Texas ranch house, a plank fence and "
              "dry St. Augustine grass",
     "a_agua": "a rectangular concrete pool with a tiled lip",
     "a_luz": "hard late sun, short shadows across the water",
     "a_audio": "a window unit humming, water lapping the tile, far traffic",
     "dela_q": "a black satin slip",
     "dela_a": "a black bikini top",
     "etnias": ["white American"]},

    {"id": "meio_oeste", "familia": "meio_oeste", "regiao": "Meio-Oeste",
     "q_cen": "a bedroom in a Midwestern split-level, papered walls and a wall "
              "clock over the dresser",
     "q_luz": "one bedside lamp on and the ceiling light off",
     "q_audio": "a furnace kicking on, a quiet street outside",
     "a_cen": "the back deck of the same Midwestern house, a chain-link fence "
              "and a maple behind it",
     "a_agua": "a square hot tub on the deck boards, steam coming off the "
               "surface",
     "a_luz": "cool overcast evening light with the steam catching it",
     "a_audio": "the tub jets, wind in the maple, a dog two yards over",
     "dela_q": "a navy satin nightgown",
     "dela_a": "a navy bikini top",
     "etnias": ["white American"]},

    {"id": "nova_inglaterra", "familia": "nova_inglaterra",
     "regiao": "Nova Inglaterra",
     "q_cen": "a bedroom in a New England colonial, white panelled walls and "
              "small paned windows",
     "q_luz": "a single lamp beside the bed, the rest of the room dark",
     "q_audio": "a radiator ticking, gulls far off",
     "a_cen": "the side yard of the same New England house, hydrangeas along a "
              "low stone wall",
     "a_agua": "a cedar hot tub on a stone patio, the water steaming",
     "a_luz": "cool north light, soft and even off the water",
     "a_audio": "steam and jets, gulls, wind through the hydrangeas",
     "dela_q": "a cream satin nightgown",
     "dela_a": "a white halter bikini top",
     "etnias": ["white American"]},

    {"id": "harlem", "familia": "harlem", "regiao": "Harlem",
     "q_cen": "a bedroom in a Harlem brownstone, pressed tin ceiling and one "
              "tall narrow window",
     "q_luz": "one lamp on the nightstand, city light leaking past the blind",
     "q_audio": "faint traffic below, a radio two floors down",
     "a_cen": "the tiled bathroom of the same brownstone, a tall narrow window "
              "above the tub",
     "a_agua": "a deep claw-foot bathtub filled to the rim",
     "a_luz": "warm city light coming in high through the window",
     "a_audio": "water moving in the tub, faint traffic, a radiator",
     "dela_q": "a black satin nightgown",
     "dela_a": "a black bikini top",
     "etnias": ["Black American"]},

    {"id": "atlanta", "familia": "atlanta", "regiao": "Atlanta",
     "q_cen": "a bedroom in an Atlanta house, dark wood furniture and heavy "
              "curtains half drawn",
     "q_luz": "one lamp on the far side of the bed, everything else in shadow",
     "q_audio": "an air handler running, a quiet street",
     "a_cen": "the back patio of the same Atlanta house, tall pines past the "
              "fence",
     "a_agua": "a kidney-shaped pool with a raised spa spilling into it",
     "a_luz": "bright filtered daylight, the water throwing light upward",
     "a_audio": "the spa spillover, birds in the pines, a quiet yard",
     "dela_q": "a deep purple satin nightgown",
     "dela_a": "a gold bikini top",
     "etnias": ["Black American"]},

    {"id": "delta", "familia": "delta", "regiao": "Delta do Mississippi",
     "q_cen": "a bedroom in a Mississippi Delta house, chipped plaster walls "
              "and a bare bulb hanging dark over the bed",
     "q_luz": "a small lamp on a chair beside the bed, warm and low",
     "q_audio": "crickets, a slow ceiling fan",
     "a_cen": "the back yard of the same Delta house, flat fields past a wire "
              "fence",
     "a_agua": "a round above-ground pool with a metal ladder on one side",
     "a_luz": "flat evening light coming across the fields",
     "a_audio": "crickets, water against the pool wall, a truck far off",
     "dela_q": "a pale blue satin nightgown",
     "dela_a": "a turquoise bikini top",
     "etnias": ["Black American"]},

    {"id": "gullah", "familia": "gullah", "regiao": "Lowcountry",
     "q_cen": "a bedroom in a Lowcountry house, blue-washed boards and a "
              "window onto marsh grass",
     "q_luz": "one lamp by the bed and the window black behind it",
     "q_audio": "waves far off, wind through a screen",
     "a_cen": "the back deck of the same Lowcountry house, marsh grass and "
              "open water past the rail",
     "a_agua": "a wooden hot tub sunk into the deck, the water moving",
     "a_luz": "soft coastal light coming off the water",
     "a_audio": "water moving in the tub, marsh birds, wind",
     "dela_q": "a white satin nightgown",
     "dela_a": "a white bikini top",
     "etnias": ["Black American"]},

    {"id": "noroeste", "familia": "noroeste", "regiao": "Noroeste do Pacifico",
     "q_cen": "a bedroom in a Pacific Northwest house, cedar walls and a "
              "window onto wet firs",
     "q_luz": "one bedside lamp, rain black on the glass behind it",
     "q_audio": "rain on the window, a quiet house",
     "a_cen": "the back deck of the same Northwest house, wet firs crowding "
              "the rail",
     "a_agua": "a cedar hot tub on the deck, steam rising off it",
     # ⛔ NADA DE LUZ COLORIDA: o operador viu um lote e disse *"tire esse ar de
     # blade runner 2049, esta em tom esverdeado villeneuve"*. Foi neste mundo,
     # no FALTA 16, e o defeito era do motor pedindo verde — nao do gerador.
     "a_luz": "cool grey daylight coming through the trees",
     "a_audio": "steam and jets, rain in the firs, water dripping",
     "dela_q": "a charcoal satin nightgown",
     "dela_a": "a dark green bikini top",
     "etnias": ["white American"]},

    {"id": "grandes_lagos", "familia": "grandes_lagos",
     "regiao": "Grandes Lagos",
     "q_cen": "a bedroom in a Great Lakes cabin, knotty pine panelling and a "
              "wool blanket shoved aside",
     "q_luz": "one lamp on the nightstand, the window pale with snow light",
     "q_audio": "wind against the glass, a quiet house",
     "a_cen": "the screened porch of the same Great Lakes cabin, birch and "
              "snow past the screens",
     "a_agua": "a square hot tub on the porch boards, heavy steam off the "
               "surface",
     "a_luz": "pale winter light off the snow, the steam catching it",
     "a_audio": "the tub jets, wind in the birches, a loon far off",
     "dela_q": "a burgundy satin nightgown",
     "dela_a": "a red bikini top",
     "etnias": ["white American"]},

    {"id": "creole", "familia": "creole", "regiao": "Nova Orleans",
     "q_cen": "a bedroom in a New Orleans shotgun house, tall shuttered "
              "windows and a slow ceiling fan",
     "q_luz": "one lamp on the nightstand, the shutters closed and dark",
     "q_audio": "a streetcar far off, cicadas",
     # ⚠️ `banana leaves` seria o cenario certo para um patio de Nova Orleans —
     # e foi o que estava aqui. A lente WF6 acusou 21 de 400, e ela esta'
     # CERTA: a palavra `banana` e' o proxy falico de tres motores do parque, e
     # deixar a excecao aberta e' abrir a porta pelo cenario. Trocada a planta,
     # nao a lente.
     "a_cen": "the brick courtyard of the same New Orleans house, broad "
              "tropical leaves hanging over the far wall",
     "a_agua": "a small tiled plunge pool set into the brick",
     "a_luz": "heavy humid light coming over the courtyard wall",
     "a_audio": "water moving, cicadas, a streetcar far off",
     "dela_q": "a black satin nightgown",
     "dela_a": "an emerald bikini top",
     "etnias": ["Black American"]},

    {"id": "italo_americana", "familia": "italo_americana",
     "regiao": "italo-americana",
     "q_cen": "a bedroom in an Italian-American house, papered walls and a "
              "framed photograph over the headboard",
     "q_luz": "a single lamp beside the bed, warm and yellow",
     "q_audio": "a clock ticking, a quiet street",
     "a_cen": "the back yard of the same house, a tomato bed along the fence "
              "and a grape arbour over the path",
     "a_agua": "a round above-ground pool with a wooden deck at one end",
     "a_luz": "warm evening light coming in under the arbour",
     "a_audio": "water against the pool wall, a radio inside, cicadas",
     "dela_q": "an ivory satin nightgown",
     "dela_a": "a black halter bikini top",
     "etnias": ["white American"]},

    {"id": "florida", "familia": "florida", "regiao": "Florida",
     "q_cen": "a bedroom in a Florida house, tile floor and a rattan headboard "
              "with the blinds drawn",
     "q_luz": "one lamp on the nightstand, the blinds dark behind it",
     "q_audio": "an air conditioner cycling, frogs outside",
     "a_cen": "the screened lanai of the same Florida house, palms standing "
              "behind the screen",
     "a_agua": "a rectangular pool with water spilling over the near edge",
     "a_luz": "bright overcast, soft even light off the water",
     "a_audio": "water spilling over the edge, a mockingbird, a pool pump",
     "dela_q": "a coral satin nightgown",
     "dela_a": "a turquoise bikini top",
     "etnias": ["white American", "Black American"]},

    {"id": "americana", "familia": "americana", "regiao": "suburbio americano",
     "q_cen": "a bedroom in a plain suburban house, beige walls and a laundry "
              "basket left by the door",
     "q_luz": "one bedside lamp on and the ceiling light off",
     "q_audio": "a refrigerator humming somewhere, a quiet street",
     "a_cen": "the back yard of the same suburban house, a wooden fence and a "
              "swing set still standing",
     "a_agua": "a round above-ground pool with a blue liner",
     "a_luz": "flat late afternoon light across the yard",
     "a_audio": "water against the pool wall, a lawnmower two streets over",
     "dela_q": "a black satin nightgown",
     "dela_a": "a white bikini top",
     "etnias": ["white American", "Black American"]},

    # ⭐⭐ + 2026-08-13, ordem do operador: *"aumente o pool de opcoes
    # substancialmente, tambem dos ambientes"*. De 15 para 24 regioes.
    # ⛔ Cada entrada nova declara EXATAMENTE as mesmas treze chaves das
    # vizinhas — quarto + luz + audio do take 1, casa + agua + luz + audio do
    # take 2, os dois trajes dela e as `etnias`. Cenario aqui e' AMBIENTE
    # INTEIRO, nao fundo.
    # ⛔ E o `a_cen` continua dizendo `the same <casa>` (controle do autoteste):
    # sem isso o corte le' como dois videos colados.
    # ⭐ COBERTURA DE ETNIA AUMENTADA: 9 -> 15 mundos que comportam `white
    # American` e 8 -> 13 que comportam `Black American`.
    # ⚠️ Sao as MESMAS nove regioes do `bed16_short.py`, sem os dois trajes do
    # MODO BELA, que este motor nao tem. Motores irmaos andam juntos.
    {"id": "socal", "familia": "socal", "regiao": "Sul da California",
     "q_cen": "a bedroom in a Southern California stucco house, white walls "
              "and a wide window behind a slatted blind",
     "q_luz": "one lamp on the far nightstand, the rest of the room dark",
     "q_audio": "a pool pump running outside, a quiet street",
     "a_cen": "the back yard of the same Southern California house, a low "
              "block wall and a lemon tree in the corner",
     "a_agua": "a rectangular plaster pool with a stone coping, the water "
               "still",
     "a_luz": "warm low sun coming in over the block wall",
     "a_audio": "the pool pump, a mockingbird, a car door two houses down",
     "dela_q": "a pale pink satin nightgown",
     "dela_a": "a white bikini top",
     "etnias": ["white American"]},

    {"id": "arizona", "familia": "arizona", "regiao": "Arizona",
     "q_cen": "a bedroom in an Arizona adobe house, thick plaster walls and a "
              "deep-set window",
     "q_luz": "a single lamp on the nightstand, the corners of the room dark",
     "q_audio": "an evaporative cooler humming, dry wind outside",
     "a_cen": "the back patio of the same Arizona adobe house, saguaro and "
              "gravel past a low wall",
     "a_agua": "a small rectangular plunge pool set into the patio, the water "
               "still",
     "a_luz": "late desert sun coming in low and orange",
     "a_audio": "the cooler humming, water lapping the pool wall, cicadas",
     "dela_q": "a sand-coloured satin nightgown",
     "dela_a": "a terracotta bikini top",
     "etnias": ["white American"]},

    {"id": "carolinas", "familia": "carolinas", "regiao": "Carolinas",
     "q_cen": "a bedroom in a Carolina brick ranch house, panelled walls and a "
              "chest of drawers under the window",
     "q_luz": "one bedside lamp on and the ceiling light off",
     "q_audio": "crickets outside, a window unit cycling",
     "a_cen": "the back yard of the same Carolina brick house, pines and a "
              "wire fence at the far edge",
     "a_agua": "a round above-ground pool with a wooden step ladder",
     "a_luz": "warm evening light coming flat across the grass",
     "a_audio": "crickets, water against the pool wall, a screen door",
     "dela_q": "a deep purple satin nightgown",
     "dela_a": "a purple bikini top",
     "etnias": ["Black American"]},

    {"id": "detroit", "familia": "detroit", "regiao": "Detroit",
     "q_cen": "a bedroom in a Detroit brick house, painted plaster walls and a "
              "tall radiator under the window",
     "q_luz": "one lamp beside the bed, street light leaking past the blind",
     "q_audio": "a radiator ticking, a bus braking two streets over",
     "a_cen": "the back yard of the same Detroit brick house, a chain-link "
              "fence and a garage out at the alley",
     "a_agua": "a square hot tub on a concrete pad, steam coming off the "
               "surface",
     "a_luz": "cool evening light with the steam catching it",
     "a_audio": "the tub jets, a dog down the alley, far traffic",
     "dela_q": "a black satin nightgown",
     "dela_a": "a red bikini top",
     "etnias": ["Black American"]},

    {"id": "rochosas", "familia": "rochosas", "regiao": "Montanhas Rochosas",
     "q_cen": "a bedroom in a Rocky Mountain log house, log walls and a wool "
              "blanket folded at the foot of the bed",
     "q_luz": "one lamp on the nightstand and the window black behind it",
     "q_audio": "wind against the log walls, a stove ticking",
     "a_cen": "the back deck of the same Rocky Mountain log house, pines and a "
              "ridge line behind",
     "a_agua": "a round cedar hot tub set into the deck, steam rising off the "
               "water",
     "a_luz": "cold blue evening light with the steam lit warm from below",
     "a_audio": "the tub jets, wind in the pines, an elk far off",
     "dela_q": "a forest green satin nightgown",
     "dela_a": "a forest green bikini top",
     "etnias": ["white American"]},

    {"id": "golfo", "familia": "golfo", "regiao": "Costa do Golfo",
     "q_cen": "a bedroom in a Gulf Coast raised house, beadboard walls and "
              "shutters half closed",
     "q_luz": "one lamp on the far nightstand, the rest of the room low",
     "q_audio": "a ceiling fan turning, frogs outside",
     "a_cen": "the screened porch of the same Gulf Coast house, marsh grass "
              "past the rail",
     "a_agua": "a round hot tub set into the porch boards, the water moving",
     "a_luz": "warm late light coming in through the screen",
     "a_audio": "frogs, water moving in the tub, a boat motor far off",
     "dela_q": "a seafoam satin nightgown",
     "dela_a": "a seafoam bikini top",
     "etnias": ["white American", "Black American"]},

    {"id": "chicago", "familia": "chicago", "regiao": "South Side de Chicago",
     "q_cen": "a bedroom in a Chicago bungalow, papered walls and a wooden "
              "dresser with a mirror",
     "q_luz": "one bedside lamp on, the hallway dark behind the door",
     "q_audio": "a radiator knocking, an elevated train far off",
     "a_cen": "the back yard of the same Chicago bungalow, a wooden fence and "
              "a garage out at the alley",
     "a_agua": "a round above-ground pool with a metal rail around the top",
     "a_luz": "flat late summer light across the yard",
     "a_audio": "water against the pool wall, an elevated train, kids two "
                "yards over",
     "dela_q": "a burgundy satin nightgown",
     "dela_a": "a burgundy bikini top",
     "etnias": ["Black American"]},

    {"id": "jersey", "familia": "jersey", "regiao": "Jersey Shore",
     "q_cen": "a bedroom in a Jersey Shore cottage, white board walls and a "
              "window facing the street",
     "q_luz": "one lamp on the nightstand and the ceiling light off",
     "q_audio": "gulls outside, a car on gravel",
     "a_cen": "the back deck of the same Jersey Shore cottage, a slat fence "
              "and beach grass behind it",
     "a_agua": "a round above-ground pool with a wooden deck built to the rim",
     "a_luz": "cool late afternoon light coming off the water",
     "a_audio": "gulls, water lapping the pool wall, a screen door",
     "dela_q": "a pale blue satin nightgown",
     "dela_a": "a pale blue bikini top",
     "etnias": ["white American"]},

    {"id": "piemonte", "familia": "piemonte", "regiao": "Piemonte da Virginia",
     "q_cen": "a bedroom in a Virginia Piedmont farmhouse, papered walls and a "
              "quilt folded over a chair",
     "q_luz": "a single lamp beside the bed, the rest of the room dark",
     "q_audio": "crickets outside, an old house settling",
     "a_cen": "the side yard of the same Virginia farmhouse, a split-rail "
              "fence and low hills behind",
     "a_agua": "a square cedar hot tub on a gravel pad, the water moving",
     "a_luz": "soft evening light coming across the fields",
     "a_audio": "crickets, water moving in the tub, a truck on the county road",
     "dela_q": "a dusty rose satin nightgown",
     "dela_a": "a rose bikini top",
     "etnias": ["white American", "Black American"]},
]

FAMILIAS_MUNDO = list(dict.fromkeys(m["familia"] for m in MUNDOS))


def mundos_da_etnia(etnia):
    """Os mundos que COMPORTAM a etnia da pagina.

    ⛔ Cede em vez de derrubar: sem mundo compativel devolve a lista inteira.
    Filtro que zera o sorteio e' filtro que quebra o app.
    """
    v = [m for m in MUNDOS if etnia in m["etnias"]]
    return v or MUNDOS


# ===========================================================================
# O HOMEM — quem fala. ⛔ etnia TRAVADA na pagina.
# ===========================================================================
# ⛔⛔ MARCA FACIAL OBRIGATORIA, E AQUI ELA E' DUPLA (`marca` + `sinal`). Nao e'
# enfeite: ele aparece nos DOIS takes, com um corte no meio e uma troca completa
# de cenario, roupa e luz. Sem ancora distintiva o Veo devolve OUTRO homem no
# take 2 — foi o que aconteceu no VAZAMENTO, e como o TAKE diz `Only he speaks`
# o estranho falava a fala do REF.
# ⚠️ 55-62 anos, conforme o frame da fonte. Cabelo e barba grisalhos.
#
# ⛔⛔ REESCRITO INTEIRO EM 2026-08-13 — ordem do operador com o print dos
# renders na mao: *"melhore a aparencia e shape desses homens"* / *"aumente o
# pool de opcoes substancialmente, tambem dos ambientes"*. De 15 para 24.
# ⚠️ O conserto NAO e' de tamanho, e' de CONTEUDO: o pool antigo carregava DANO
# no `sinal` — `a pale scar through his left eyebrow`, `a broad flat nose broken
# once and never set` (duas vezes), `heavy folds under both eyes`, `a white
# patch of old sun damage`, `a deep vertical crease between his eyebrows`, `a
# weathered squint`, `a chipped front tooth that shows when he talks`, `a pale
# old scar along his jaw`. O `sinal` e' repetido LITERAL na IMAGE 02 (ancora de
# continuidade), entao cada video levava a mesma avaria duas vezes. E' a licao
# do PLACA 16 (*"esses caras tao parecendo mendigo"*): ancora DISTINTIVA, nunca
# DETERIORADA.
# ⭐ E' o MESMO pool do `bed16_short.py`, entrada por entrada — os dois motores
# nasceram por copia literal e divergir aqui e' criar duas verdades sobre o
# mesmo homem.
# ⛔ NENHUMA PALAVRA DE APROVACAO (handsome, rugged, strong jaw): elogio no
# prompt puxa o rosto para a media do banco de imagem, mesmo mecanismo do `not
# a celebrity`. ⛔ E NENHUMA COR DE PELE — a etnia entra pela PAGINA.
# ⭐ OCULOS EM 6 DAS 24 (25%) — o eixo estava ZERADO no `medir_personagens
# --gate` (reprovacao).
HOMENS = [
    {"id": "grisalho_curto", "idade": 57,
     "rotulo": "57y · grisalho rente + barba cheia",
     "marca": "close-cropped grey hair and a full grey beard going white at "
              "the chin",
     "sinal": "a strong cleft in his chin"},
    {"id": "careca_cavanhaque", "idade": 59,
     "rotulo": "59y · careca + cavanhaque grisalho",
     "marca": "a clean-shaven scalp and a short grey goatee",
     "sinal": "a small dark mole high on his right cheek"},
    {"id": "sal_pimenta", "idade": 55,
     "rotulo": "55y · sal-e-pimenta + barba por fazer",
     "marca": "short salt-and-pepper hair and three days of grey stubble",
     "sinal": "laugh lines at the corners of his eyes"},
    {"id": "barba_cheia", "idade": 60,
     "rotulo": "60y · entrada em bico + barba branca",
     "marca": "grey hair with a low widow's peak and a full white beard",
     "sinal": "heavy level brows over wide-set eyes"},
    {"id": "bigode_grisalho", "idade": 58,
     "rotulo": "58y · grisalho rente + bigode grosso",
     "marca": "close-cropped grey hair and a thick grey moustache",
     "sinal": "a shallow dimple in his left cheek and light freckling across "
              "his nose"},
    {"id": "ondulado", "idade": 56,
     "rotulo": "56y · grisalho ondulado + barba rente",
     "marca": "short wavy grey hair and a close grey beard",
     "sinal": "a patch of white above his left temple"},
    {"id": "oculos_fio", "idade": 61,
     "rotulo": "61y · prata para tras + oculos de fio",
     "marca": "thick silver hair swept straight back, a clean-shaven face and "
              "thin wire-rimmed glasses",
     "sinal": "a small mole beside his right eye"},
    {"id": "barba_quadrada", "idade": 62,
     "rotulo": "62y · branco rente + barba quadrada",
     "marca": "close-cropped white hair and a full white beard trimmed square "
              "at the jaw",
     "sinal": "smooth-skinned with a cleft chin"},
    {"id": "topete_prata", "idade": 55,
     "rotulo": "55y · topete prata + oculos de aco",
     "marca": "silver hair still full on top and combed high, a clean-shaven "
              "face and thin steel-rimmed glasses",
     "sinal": "a beauty mark below his right eye"},
    {"id": "raspado_cavanhaque", "idade": 58,
     "rotulo": "58y · raspado + cavanhaque branco",
     "marca": "a shaved head and a short white goatee",
     "sinal": "heavy level brows and a wide square chin"},
    {"id": "oculos_retangular", "idade": 59,
     "rotulo": "59y · risca lateral + oculos retangular",
     "marca": "short grey hair parted on one side, a trimmed grey beard and "
              "dark rectangular glasses",
     "sinal": "a shallow cleft in his chin"},
    {"id": "cachos_grisalhos", "idade": 56,
     "rotulo": "56y · cachos grisalhos + tarraxa dourada",
     "marca": "loose grey curls kept short and a close-trimmed grey beard",
     "sinal": "a small gold stud in his left ear"},
    {"id": "bigode_chevron", "idade": 60,
     "rotulo": "60y · lateral rente + bigode chevron",
     "marca": "grey hair clipped short at the sides and a thick chevron "
              "moustache",
     "sinal": "laugh lines at the corners of his mouth"},
    {"id": "entradas_barba", "idade": 57,
     "rotulo": "57y · entradas altas + barba cheia",
     "marca": "a high hairline with thick grey hair behind it and a full grey "
              "beard",
     "sinal": "a small mole on his left jaw"},
    {"id": "oculos_grossos", "idade": 62,
     "rotulo": "62y · branco curto + oculos de aro grosso",
     "marca": "short white hair, a clean-shaven face and heavy black-framed "
              "glasses",
     "sinal": "a silver streak through one eyebrow"},
    {"id": "lateral_prateada", "idade": 55,
     "rotulo": "55y · laterais prateadas + covinhas",
     "marca": "dark hair going silver at the sides, cut short, and a close "
              "dark beard",
     "sinal": "a dimple in each cheek when he talks"},
    {"id": "barba_curta_branca", "idade": 61,
     "rotulo": "61y · branco muito curto + barba branca",
     "marca": "white hair kept very short and a short white beard",
     "sinal": "smooth-skinned with a broad square chin"},
    {"id": "onda_para_tras", "idade": 58,
     "rotulo": "58y · onda sal-e-pimenta + barbeado",
     "marca": "wavy salt-and-pepper hair pushed back off the forehead and a "
              "clean-shaven face",
     "sinal": "smooth-skinned with a small beauty mark on his left cheekbone"},
    {"id": "oculos_aro_fino", "idade": 56,
     "rotulo": "56y · grisalho escuro + oculos sem aro",
     "marca": "short dark grey hair, a close grey beard and rimless glasses",
     "sinal": "a cleft chin under heavy level brows"},
    {"id": "crista_branca", "idade": 59,
     "rotulo": "59y · mecha branca + barba escura",
     "marca": "a white streak running through short dark hair and a trimmed "
              "dark beard",
     "sinal": "a small mole above his lip"},
    {"id": "careca_bigode", "idade": 60,
     "rotulo": "60y · careca com laterais + bigode grosso",
     "marca": "a bald crown with grey at the sides and a thick grey moustache",
     "sinal": "a small gold hoop in his left ear"},
    {"id": "barba_longa_grisalha", "idade": 62,
     "rotulo": "62y · grisalho atras + barba longa",
     "marca": "grey hair combed back short and a long grey beard combed "
              "straight",
     "sinal": "freckles scattered across his nose"},
    {"id": "oculos_claro", "idade": 57,
     "rotulo": "57y · grisalho rente + oculos incolor",
     "marca": "close-cropped grey hair, a short grey beard and clear-framed "
              "glasses",
     "sinal": "a shallow dimple in his chin"},
    {"id": "franja_grisalha", "idade": 58,
     "rotulo": "58y · franja grisalha + barbeado",
     "marca": "straight grey hair kept a little long over the forehead and a "
              "clean-shaven face",
     "sinal": "laugh lines and a small mole at the corner of his jaw"},
]

# ⛔ Ele esta' de TRONCO NU no take 1 (frame da fonte) e com a agua no peito no
# take 2.
#
# ⛔⛔ REESCRITO INTEIRO EM 2026-08-13, ordem do operador com o print na mao:
# *"melhore a aparencia e shape desses homens"*. Das 12 entradas antigas, DEZ
# descreviam corpo mole ou curvado (`soft middle`, `gone soft at the waist`,
# `lean and stooped, the shoulder blades showing`, `a low round belly`,
# `softened with age`, `the chest gone slack`, `the belly resting on his lap`,
# `narrow-shouldered with a soft chest and thin arms`...) — e o `corpo_h` entra
# nos DOIS blocos, entao o render trazia o mesmo homem fora de forma duas vezes.
# ⚠️ A metade certa da justificativa antiga FICA e esta' escrita no alvo: ⛔ NAO
# e' fisiculturista. Este angulo nao tem MODO FORTE, e musculo de academia num
# homem de 58 na cama quebra a leitura de marido comum que voltou a funcionar. O
# alvo e' **em forma para a idade**: solido, ombro largo, peito firme, cintura
# controlada. De 12 para 14, e identico ao do `bed16_short.py` (motores irmaos).
CORPOS_H = [
    "solid through the chest and shoulders with the waist still trim",
    "broad-shouldered with a firm flat chest and a straight back",
    "squarely built and thick through the upper arms, the middle flat",
    "wide and level through the shoulders with a firm chest",
    "heavy in the shoulders and arms with a flat stomach",
    "thick through the neck and shoulders, the chest full and the waistline "
    "clean",
    "a broad chest and a straight upright back, the stomach flat",
    "deep through the chest with heavy forearms and a trim waist",
    "big-framed and even, the shoulders square and the middle firm",
    "compact and solid, the chest firm and the arms thick",
    "long-backed and wide at the shoulders with a flat stomach",
    "a full chest over round shoulders, the waist held in",
    "sturdy through the ribs and shoulders, the arms still full",
    "heavy through the chest with a flat stomach and thick wrists",
]


# ===========================================================================
# A MULHER — ⭐ etnia SOLTA. Ela e' MUDA nos dois takes.
# ===========================================================================
# ⛔ A LEI DO REF vale para ela em todas as entradas: 25-38 anos, sempre bonita,
# marca facial obrigatoria, zero oculos, zero grisalho, zero pele castigada.
# ⛔ E ela e' MUDA — invariante do angulo, nao estilo. Sem `Only he speaks` no
# TAKE o Veo poe as duas bocas a mexer e o dialogo sai monofonico e torto
# (lente WF1).
MULHERES = [
    {"id": "loira_longa", "idade": 31, "etnia": "white American",
     "marca": "long blonde hair loose over one shoulder and a small beauty "
              "spot above her lip"},
    {"id": "ruiva_ondulada", "idade": 29, "etnia": "white American",
     "marca": "auburn waves pushed back off her face and a dense spray of "
              "freckles"},
    {"id": "morena_lisa", "idade": 34, "etnia": "white American",
     "marca": "dark brown hair, straight and heavy, and a dimple in one "
              "cheek"},
    {"id": "bob_castanho", "idade": 26, "etnia": "white American",
     "marca": "a glossy chestnut bob and a dimple in one cheek"},
    {"id": "trancas_lateral", "idade": 30, "etnia": "Black American",
     "marca": "long box braids gathered over one shoulder and high cheekbones"},
    {"id": "afro_curto", "idade": 27, "etnia": "Black American",
     "marca": "a short rounded afro and a small gold stud in one nostril"},
    {"id": "trancas_longas", "idade": 36, "etnia": "Black American",
     "marca": "waist-length braids and a beauty spot high on her cheek"},
    {"id": "cachos_altos", "idade": 33, "etnia": "Black American",
     "marca": "dark curls gathered high on her head and a small birthmark at "
              "her temple"},
    {"id": "latina_ondulada", "idade": 32, "etnia": "Latina American",
     "marca": "long wavy black hair and a small mole beside her right eye"},
    {"id": "asiatica_lisa", "idade": 28, "etnia": "Asian American",
     "marca": "straight black hair to the shoulders, smooth-skinned, with a "
              "small beauty mark on her chin"},
    # + 2026-08-10: de 10 para 18. ⛔ LEI DO REF — 25-38, sempre bonita, marca
    # facial obrigatoria, zero oculos/grisalho/pele castigada. ⭐ A etnia dela e'
    # SOLTA (quem casa com a pagina e' ELE, que e' quem fala), e por isso o pool
    # cobre pele clara, negra, latina e asiatica.
    {"id": "castanha_curta", "idade": 33, "etnia": "white American",
     "marca": "chin-length dark brown hair tucked behind one ear and a small mole on her jaw"},
    {"id": "afro_baixo", "idade": 30, "etnia": "Black American",
     "marca": "a short natural afro and a beauty spot high on her right cheek"},
    {"id": "coque_baixo", "idade": 35, "etnia": "Latina American",
     "marca": "black hair in a low bun and a thin gold chain at her throat"},
    {"id": "liso_longo_preto", "idade": 28, "etnia": "Asian American",
     "marca": "long straight black hair and a small dark mole beside her mouth"},
    {"id": "loira_curta", "idade": 36, "etnia": "white American",
     "marca": "a blonde bob cut just below the jaw and pale freckles across her nose"},
    {"id": "trancas_coque", "idade": 32, "etnia": "Black American",
     "marca": "braids gathered into a high bun and a silver streak at the "
              "front of her hairline"},
    {"id": "ondulado_castanho", "idade": 34, "etnia": "Latina American",
     "marca": "loose brown waves past her shoulders and a beauty spot under her left eye"},
    {"id": "rabo_alto", "idade": 27, "etnia": "white American",
     "marca": "dark hair pulled into a high ponytail and a small silver hoop in one ear"},
    # ⭐⭐ + 2026-08-13, ordem do operador: *"aumente o pool de opcoes
    # substancialmente, tambem dos ambientes"*. De 18 para 24.
    # ⛔ E as TRES entradas que carregavam `scar` foram REESCRITAS na mesma
    # passada (`a small scar through one eyebrow` x2, `a faint scar on her
    # chin`): a `marca` dela e' repetida no take 2 como ancora, e ancora de
    # DANO num pool que a LEI DO REF manda ser bonito e' contradicao dentro da
    # mesma frase. Ancora saudavel cumpre a mesma funcao — covinha, sinal de
    # beleza, mecha, sardas — e volta igual depois do corte.
    # ⛔ SEM OCULOS, e isso e' isencao declarada no `medir_personagens.py`
    # (LEI DO REF, pool em registro de beleza) — nao e' buraco esquecido.
    # ⭐ A etnia continua SOLTA: quem casa com a pagina e' ELE, que e' quem
    # fala. As quatro familias do pool antigo seguem cobertas.
    {"id": "cachos_soltos", "idade": 29, "etnia": "white American",
     "marca": "loose chestnut curls past her shoulders and freckles across "
              "her nose"},
    {"id": "trancas_finas", "idade": 31, "etnia": "Black American",
     "marca": "fine braids falling loose down her back and a small mole above "
              "her lip"},
    {"id": "coque_frouxo", "idade": 26, "etnia": "white American",
     "marca": "honey blonde hair twisted into a loose knot and a dimple in "
              "her chin"},
    {"id": "liso_repartido", "idade": 33, "etnia": "Asian American",
     "marca": "long black hair parted in the middle, smooth-skinned, with a "
              "small mole on her cheekbone"},
    {"id": "franja_cortina", "idade": 30, "etnia": "Latina American",
     "marca": "dark brown hair with a curtain fringe and a beauty mark beside "
              "her left eye"},
    {"id": "twists_altos", "idade": 35, "etnia": "Black American",
     "marca": "two-strand twists gathered high and a fine gold hoop in one "
              "ear"},
]


# ===========================================================================
# ⭐⭐ O COPO — E ELE E' O PROPRIO GELATIN TRICK
# ===========================================================================
# ⛔ DECISAO 2 DO OPERADOR: a bebida do take 2 e' o mecanismo que a copy vende.
# Por isso este pool NAO e' de bebidas — e' de COMO O PREPARO APARECE em quadro.
# O que muda e' o vasilhame; o conteudo e' sempre o mesmo preparo pálido.
#
# ⛔⛔ E ELE NAO TEM ROTULO, NEM NOME DE INGREDIENTE. Duas razoes distintas:
#   · CT5 — a receita e' a UNICA moeda que o comentario compra. Entregar um
#     ingrediente (na fala OU escrito no quadro) a gasta para os outros 49
#     videos da mesma pagina.
#   · o GOOD 16 mostra um sache com GELATIN legivel porque a FONTE dele mostra.
#     A fonte deste angulo nao mostra rotulo nenhum — copiar o sache de la'
#     seria importar a excecao de outro agente sem a evidencia que a justifica.
#
# ⚠️ CADA ENTRADA TEM SILHUETA PROPRIA. Licao do BOTICA: metade de um pool era
# de vidro e o gerador colapsou quatro entradas numa prensa francesa, que e' a
# forma que ele conhece melhor. Aqui nao ha' dois corpos iguais.
# ---------------------------------------------------------------------------
# ⭐⭐ MODO RECEITA — a tigela na borda (2026-08-10)
# ---------------------------------------------------------------------------
# ⛔ Encomenda do operador: *"quero um toggle na interface que, quando ativada,
# o take 2 gera a cena da piscina porem com um adendo: o casal (ainda dentro do
# corpo dagua) esta com uma bowl de cubos de gelatina e uma caixa de baking
# soda na BORDA da piscina, e o homem fazendo stirring com uma colher na bowl."*
#
# ⭐ POR QUE ISSO IMPORTA, e e' a mesma queixa que reformou o ESCANDALO 16 hoje:
# desligado, o take 2 mostra um casal na agua com dois copos — e nada em quadro
# diz RECEITA. O CTA pede `gelatin` e a prova visual e' uma bebida palida que
# poderia ser qualquer coisa. Ligado, a tigela de CUBOS e a caixa dizem
# "isto e' feito em casa" sem uma palavra.
#
# ⛔⛔ A CAIXA E' DE PAPELAO E ELES ESTAO DENTRO D'AGUA — e' por isso que ela
# fica na BORDA, seca, e nao na mao. O operador ja' resolveu isso ao escrever o
# pedido; o que o codigo acrescenta e' a TRAVA: a lente WF10 reprova se a caixa
# ou a tigela forem descritas dentro da agua. E' a licao paga no FIGHT 16, onde
# o primeiro render pos ele com a agua no peito segurando uma caixa de papelao.
#
# ⛔ E O COPO DELE SAI. Decisao do operador: *"so' a mulher com copo quando o
# toggle estiver ativado; ela segura o drink e o corpo dela continua rente ao
# dele"*. E' troca, nao soma — as duas maos dele passam a ter UMA agenda
# (segurar a tigela e mexer), e mandar ele segurar copo E colher e' a
# contradicao das DUAS COLHERES, que o gerador resolve desenhando a terceira
# mao. ⚠️ A lente WF4, que exigia o copo nos DOIS, passou a exigir isso SO' no
# modo desligado.
WF_RECEITA_IMAGE = (
    "On the ledge beside them, out of the water and dry, sit a clear glass "
    "bowl full of cut cubes of set amber gelatin, an orange and yellow "
    "cardboard box of baking soda with the label sharp and readable, and a "
    "spoon standing in the bowl. He has both hands on the bowl at the ledge, "
    "one steadying its rim and the other turning the spoon in it, and his arms "
    "are clear of the water."
)

WF_RECEITA_TAKE = (
    "His hands keep turning the spoon in the bowl in slow circles the whole "
    "time, and that is the only movement in his hands. The bowl, the box and "
    "the spoon stay on the ledge and are never lifted into the water. She "
    "simply holds her own drink the whole time and never drinks from it or "
    "lifts it to her mouth."
)

COPOS = [
    {"id": "copo_alto_gelo", "nome": "copo alto com gelo",
     "curto": "copo alto",
     "img": "a tall glass filled with ice and a pale drink, beaded with "
            "condensation"},
    {"id": "caneca_vidro", "nome": "caneca de vidro",
     "curto": "caneca de vidro",
     "img": "a clear glass mug of a pale drink with a long steel spoon left "
            "standing in it"},
    {"id": "copo_baixo", "nome": "copo baixo de vidro grosso",
     "curto": "copo baixo",
     "img": "a short heavy tumbler of thick glass with a pale drink in it"},
    {"id": "copo_estriado", "nome": "copo de vidro estriado",
     "curto": "copo estriado",
     "img": "a ribbed glass tumbler of a pale drink with one large cube of ice"},
    {"id": "pote_vidro", "nome": "pote de vidro com tampa",
     "curto": "pote de vidro",
     "img": "a wide-mouth glass jar of a pale drink with its screw lid sitting "
            "beside it"},
    {"id": "caneca_esmalte", "nome": "caneca de esmalte",
     "curto": "caneca de esmalte",
     "img": "a white enamel mug with a chipped blue rim and a pale drink in it"},
    {"id": "copo_acrilico", "nome": "copo alto de acrilico",
     "curto": "copo de acrilico",
     "img": "a tall clear acrylic tumbler of a pale drink with a wide straw "
            "in it"},
    {"id": "taca_grossa", "nome": "taca de vidro grosso",
     "curto": "taca grossa",
     "img": "a thick stemmed glass with a pale drink standing in it"},
]


# ===========================================================================
# ⭐⭐ A COPY — sob o CONTRATO DE COPY 16s, trava por trava
# ===========================================================================
# ⛔ O ORCAMENTO, e ele FECHA POR CONSTRUCAO (nao por solver — solver que
# "tenta 12 vezes" ja' custou caro duas vezes no repo):
#
#     take 1   FALHA 11-12  +  CUSTO 11             = 22-23   (teto 25)
#     take 2   MECANISMO 8-9 + PROVA 6 + CTA 9      = 23-24   (teto 25)
#
# ⚠️ ENTRADAS DO MESMO POOL COM TAMANHOS PARECIDOS, de proposito. Pool que vai
# de 6 a 14 palavras num teto de 25 nao e' pool de 12: e' pool de 4 com oito
# enfeites, porque as oito longas nunca sao sorteadas.
#
# ⛔ ORDEM DE ESCOLHA (que nao e' a ordem da frase): escolhe primeiro quem tem
# MENOS SUBSTITUTOS. No take 2 e' o CTA — ele carrega o literal `Comment
# gelatin,` e o endereco da entrega, e nao se encurta. O beat mais
# intercambiavel escolhe por ULTIMO e absorve a sobra.

# ---------------------------------------------------------------------------
# take 1 — A FALHA DELE  (CT2)
# ---------------------------------------------------------------------------
# ⛔ CT2: uma sentenca dizendo o que o corpo dele faz de errado, com DANO
# CONCRETO e, de preferencia, um NUMERO. A melhor linha do lote inteiro do
# parque e' `He'd lose it ten minutes in.` — cinco palavras, um numero, um dano.
# Sem auto-reconhecimento nao ha' comentario: ele nao comenta porque a copy e'
# boa, comenta porque SE VIU.
#
# ⛔⛔ CT7 VALE AQUI. Este angulo NAO tem isca absurda (nao ha' promessa falsa a
# ser desmentida meio segundo depois, como no TROCA/EXTERIOR/COLO), entao verbo
# de ereccao colado no orgao e' proibido nos DOIS takes. Foi por isso que
# `never came back up` saiu deste pool antes de ele existir: `came back` na
# mesma sentenca do orgao le' como tumescencia e reprova no gerador (~95% de
# recusa medidos no COLO 16).
#
# ⭐ E A FALHA DESTE ANGULO TEM DOIS LADOS: o corpo (aqui) e o casamento
# (o pool seguinte). Os dois cabem no take 1, e e' isso que o separa dos outros
# vinte — nos outros o take 1 so' tem o corpo.
# ⛔⛔ A FALHA E' CURTA E A APOSTA CABE EM QUATRO PALAVRAS — reescrita
# 2026-08-10 por ordem do operador, e e' a SEGUNDA vez que ele faz esta mesma
# correcao no mesmo dia (a primeira foi no FLAGRANTE 16):
#   *"uma unica frase curta dizendo 'my pecker went soft e eu estava com medo de
#    perde-la' ja' esta' suficiente. Tu ta' gastando fala com detalhes
#    secundarios desnecessarios no drama com a mulher. No que voce poderia
#    colocar uma frase com funcao de descoberta de reviravolta positiva."*
# ⚠️ O que saiu: `I never explained`, `Nine months without her hand on me`,
# `Twenty six years married, and she was already packing a bag`. Sao 11 palavras
# de drama de segunda ordem ocupando o lugar da DESCOBERTA — e o take 1 fechava
# no fundo do poco, sem nenhuma razao para o espectador continuar.
# ⭐ Agora cada entrada carrega A FALHA + A APOSTA em 11-12 palavras, e o slot
# seguinte (VIRADAS) fecha o take apontando para frente.
FALHAS = [
    "My {o} gave out on our anniversary. I was losing her.",
    "My {o} quit on me at fifty five. She was almost gone.",
    "My {o} went soft every single night. I was losing my wife.",
    "My {o} stopped working two years ago. My marriage was going.",
    "My {o} gave out halfway, three nights running. She was leaving.",
    "My {o} was dead by our anniversary. I could feel her going.",
    "My {o} quit on me before sixty. I was watching her go.",
    "My {o} went soft ten minutes in. We were nearly done.",
    "My {o} did nothing for eight months. Her bags were packed.",
    "My {o} shut down after fifty. I was afraid of losing her.",
    "My {o} quit halfway, twice a week. She stopped looking at me.",
    "My {o} hadn't worked in a year. I was losing my marriage.",
    "My {o} failed me again last Saturday. She was done asking.",
    "My {o} was finished by fifty eight. I was losing her.",
]

# ---------------------------------------------------------------------------
# take 1 — O CUSTO CONJUGAL  (o que este angulo tem e nenhum outro tem)
# ---------------------------------------------------------------------------
# ⛔ 11 palavras EXATAS em todas — e' o beat de comprimento fixo que fecha o
# orcamento do take 1.
# ⛔ SEM O ORGAO AQUI, de proposito: o apelido ja' foi dito na FALHA, e repetir
# duas vezes dentro de 8 segundos e' bordao. A repeticao que o CT4 exige e'
# ENTRE OS DOIS TAKES, nao dentro de um.
# ⚠️ E sem verbo de ereccao em lugar nenhum: `is back`, `comes back`, `came
# back` sao tokens do CT7, e uma frase sobre o CASAMENTO voltando com esses
# verbos ficaria a um passo de ser lida como frase sobre o orgao.
# ⭐⭐ A VIRADA — o beat que substituiu o CUSTO (2026-08-10).
# O take 1 tem de FECHAR APONTANDO PARA FRENTE, nunca empilhando drama. E' a
# forma que o operador escreveu a mao:
#     "My pecker gave out on our anniversary. I was losing her.
#      Everything started to change when I discovered the gelatin trick."
# ⚠️ 9-10 palavras, e TODAS nomeiam o `gelatin trick` — aqui ele e' a DESCOBERTA,
# nao o mecanismo. A razao dele (verbo de efeito + alvo, CT3) mora na cena 2,
# que e' onde ela cabe: cobrar a razao nas DUAS mencoes seria redundancia paga
# em palavras que o take nao tem.
VIRADAS = [
    "Everything started to change when I discovered the gelatin trick.",
    "Everything changed the week I found the gelatin trick.",
    "Then a buddy told me about the gelatin trick.",
    "All of that turned around with the gelatin trick.",
    "Everything turned when I finally tried the gelatin trick.",
    "It all changed after I started the gelatin trick.",
    "Then I found the gelatin trick, and everything shifted.",
    "Everything changed the night I made the gelatin trick.",
    "That all ended when I discovered the gelatin trick.",
    "One month on the gelatin trick and everything changed.",
    "Everything got better the day I found the gelatin trick.",
    "My brother handed me the gelatin trick, and everything changed.",
]

# ---------------------------------------------------------------------------
# take 2 — O MECANISMO COM RAZAO  (CT3)
# ---------------------------------------------------------------------------
# ⛔ CT3: nome de mecanismo SEM razao ao lado nao vira crenca, vira ruido de
# marca. Toda entrada carrega, na mesma sentenca, VERBO DE EFEITO + ALVO:
#
#     ✗ The gelatin trick is the half that works.
#     ✓ The gelatin trick opens blood flow to your {o}.
#
# ⛔⛔ E A CONSTRUCAO E' SEMPRE DIRECIONAL — `blood flow TO/INTO/THROUGH your
# {o}`. Nao e' estilo: e' a forma validada em campo (a mesma do FLAGRANTE 16,
# `blood flow to your {o} got choked off`). As formas de RETENCAO — `fills your
# {o} with blood`, `holds blood inside your {o}` — descrevem o orgao enchendo, e
# e' exatamente isso que o classificador le' como tumescencia. Nasceram e
# morreram nesta lista, antes do primeiro render.
#
# ⛔ O `_adjetivo_do_mecanismo` do `short_comum` e' ALLOWLIST: so' artigo,
# numeral, `secret` e `whole` podem vir ANTES do literal. Todas comecam em
# `The`.
#
# ⛔⛔ TODAS EM 2a PESSOA, e a excecao foi MEDIDA e derrubada. O motor nasceu
# com duas entradas em 1a pessoa (`blood flow to my {o}`), com o argumento de
# que a fala inteira e' depoimento dele. Medido em 400 sorteios: 11% dos
# videos saiam com o mecanismo em 1a pessoa — e como a cena 1 deste angulo E'
# toda em 1a pessoa por construcao, nesses 11% o video INTEIRO nunca falava do
# corpo de quem assiste. A sentenca do mecanismo e' o UNICO lugar em que o
# espectador entra; ali o depoimento nao e' variedade, e' a transferencia
# perdida. O depoimento continua vivo onde ele custa nada: na cena 1 e na
# PROVA (`she quit sleeping on that side`).
# ⚠️⚠️ TEMPO VERBAL: o MECANISMO E' PRESENTE SIMPLES, sempre. Ele descreve
# o que o truque FAZ — verdade geral sobre o produto — e o alvo e' o corpo
# DELE, que ainda nao foi consertado. Duas entradas nasceram no PASSADO
# (`fixed`/`gave blood flow to your {o}`) e o operador pegou lendo o app:
# elas eram DEPOIMENTO em 1a pessoa (`to MY {o}`), e quando eu virei o
# possessivo para `your` esqueci de virar o verbo. Passado + 2a pessoa diz
# que o truque ja' consertou o corpo de quem esta' assistindo, o que e'
# falso e soa quebrado.
# ⛔ O depoimento continua vivo onde ele e' verdade: na cena 1 (a falha e a
# virada) e na PROVA (`she quit sleeping on that side`), que sao passado
# com sujeito na 1a/3a pessoa.
MECANISMOS = [
    # 9 palavras
    "The gelatin trick opens blood flow to your {o}.",
    "The gelatin trick restores blood flow to your {o}.",
    "The gelatin trick clears blood flow into your {o}.",
    "The gelatin trick feeds blood flow to your {o}.",
    "The gelatin trick moves blood flow through your {o}.",
    "The gelatin trick unblocks blood flow to your {o}.",
    "The gelatin trick pushes blood flow into your {o}.",
    "The gelatin trick carries blood flow into your {o}.",
    "The gelatin trick starts blood flow to your {o}.",
    "The gelatin trick brings blood flow to your {o}.",
    "The gelatin trick fixes blood flow to your {o}.",
    "The gelatin trick sends blood flow to your {o}.",
    # 8 palavras — a folga que tira o take 2 de cima do teto
    "The gelatin trick moves blood into your {o}.",
    "The gelatin trick pushes blood into your {o}.",
    "The gelatin trick carries blood into your {o}.",
    "The gelatin trick brings blood to your {o}.",
]

# ---------------------------------------------------------------------------
# take 2 — A PROVA, QUE E' ELA
# ---------------------------------------------------------------------------
# ⛔⛔ ESTE E' O BEAT DO ANGULO. Nos outros motores a prova e' um corpo, um prop
# ou um copo; aqui e' a MULHER, e a fala so' precisa NOMEAR o que o quadro ja'
# mostra — ela colada nele. E' a inversao exata do take 1 (bracos cruzados,
# virada para o outro lado), e o video inteiro e' essa inversao.
# ⛔ 6 palavras EXATAS. Beat de comprimento fixo, e o mais intercambiavel dos
# tres — por isso ele escolhe por ULTIMO no `_falas` e absorve a sobra.
# ⚠️ Nenhuma menciona o orgao: o CT4 ja' esta' pago pelo MECANISMO, e o CT7
# proibe justamente a frase que juntaria o orgao a um verbo de retomada.
#
# ⛔⛔ DUAS ENTRADAS MORRERAM NA CONFERENCIA (2026-08-10) POR DEMONSTRATIVO SEM
# REFERENTE, e ficam nomeadas aqui para ninguem "melhorar" de volta:
#
#     ✗ "She unpacked that bag that week."   ← em 31 de 36 sorteios NAO havia
#       mala nenhuma no take 1 (so' 2 das 12 entradas de VIRADAS citam bag ou
#       suitcase). E `that week` nunca tem semana.
#     ✗ "She quit sleeping on that side."    ← em 27 de 35 sorteios nao havia
#       lado nenhum. E pior que o outro: o take 2 se passa DENTRO D'AGUA, entao
#       nao ha' cama em quadro para o deitico apontar.
#
# ⛔ A regra e' a do repo: *o deitico so' aponta se houver para onde apontar* —
# e num video de 16s com corte no meio, o take 2 nao herda o cenario do take 1.
# ⚠️ O `medir_deiticos` NAO pega isto: ele mede dentro da sentenca. Um
# demonstrativo cujo antecedente depende de qual entrada de OUTRO pool caiu no
# take anterior so' aparece lendo a fala montada, em voz alta.
# ⚠️ As substitutas mantem as 6 PALAVRAS EXATAS (o beat de comprimento fixo que
# fecha o orcamento do take 2) e ficam no mesmo grupo semantico das mortas —
# a que falava de mala virou a de ir embora, a que falava de lado da cama virou
# a de iniciativa dela.
PROVAS = [
    "Now she never sleeps turned away.",
    "She has not slept facing away.",
    "Now she is the one reaching.",
    "She quit talking about moving out.",
    "Now she climbs in with me.",
    "She stopped sleeping in another room.",
    "Now she reaches over before dawn.",
    "She has never mentioned leaving again.",
    "She holds on the whole evening.",
    "Now she stays pressed against me.",
    "Now she pulls me to bed.",
    "Now she is the one asking.",
]

# ---------------------------------------------------------------------------
# take 2 — O CTA  (CT1 · CT6 · CT8)
# ---------------------------------------------------------------------------
# ⛔ CT1: NADA DEPOIS DESTA SENTENCA. A posicao final e' a que fica, e ela tem
# de ser o pedido. O defeito mais caro do lote antigo (100% dos sorteios em 6 de
# 7 motores) era exatamente uma frase depois do CTA.
# ⛔ CT8: NENHUM PEDIDO DE FOLLOW. A DM sai igual para quem nao segue — ordem do
# operador, 2026-08-10, corrigindo a premissa errada que gerou o beat inteiro.
# Este motor nasce SEM o pool de follow: nao ha' o que aposentar aqui.
# ⛔ CT6: a sentenca diz ONDE a receita chega. O KPI e' uma confissao publica —
# o comentario leva nome e foto e vai para o feed da esposa dele —, e a clausula
# de entrega e' de graca: mesmas 9 palavras, e paga o endereco, a privacidade e
# o fato de nao ser na tela publica.
# ⛔⛔ A VIRGULA DEPOIS DE `gelatin` E' INTOCAVEL: a automacao de DM casa palavra
# EXATA, e a legenda do video nasce do Whisper em cima do audio gerado. Sem a
# micro-pausa o Veo emenda e narra `gelatine`. O literal vem de
# `sc.CTA_LITERAL`, nunca redigitado.
# ⚠️ 9 palavras EXATAS em todas, e todas nomeiam `recipe` (`sc.lint_isca_cta`:
# pedir o comentario sem dizer o que chega e' pedir sem oferecer).
CTAS = [
    "%s and the recipe goes to your messages." % sc.CTA_LITERAL,
    "%s and the recipe lands in your messages." % sc.CTA_LITERAL,
    "%s and the recipe hits your inbox tonight." % sc.CTA_LITERAL,
    "%s and I'll send the recipe by message." % sc.CTA_LITERAL,
    "%s and the recipe arrives in your messages." % sc.CTA_LITERAL,
    "%s and the recipe arrives in your messages." % sc.CTA_LITERAL,
    "%s and I'll send the recipe in private." % sc.CTA_LITERAL,
    "%s and the recipe comes to your inbox." % sc.CTA_LITERAL,
    "%s and your inbox gets the recipe tonight." % sc.CTA_LITERAL,
    "%s and the whole recipe reaches your messages." % sc.CTA_LITERAL,
]


# ===========================================================================
# HELPERS
# ===========================================================================

def _palavras(s):
    return len(re.findall(r"[A-Za-z']+", s or ""))


def _cap(s):
    return s[0].upper() + s[1:] if s else s


def _carregar_ledger():
    if os.path.exists(LEDGER):
        with open(LEDGER, encoding="utf-8-sig") as f:
            try:
                return json.load(f)
            except ValueError:
                return {}
    return {}


EIXOS_LEDGER = ("mundo", "homem", "mulher", "copo")


def _anotar(ledger, spec):
    p = ledger.setdefault(spec["pagina"], {})
    for eixo in EIXOS_LEDGER:
        if spec.get(eixo):
            p.setdefault(eixo, []).append(spec[eixo]["id"])
            p[eixo] = p[eixo][-12:]
    return ledger


def _gravar_ledger(ledger, spec=None):
    """⛔ DOIS argumentos, sempre: o `ui_agente` chama
    `_gravar_ledger(_carregar_ledger(), self.spec)`, e motor que aceita UM
    levanta TypeError dentro do callback do tkinter — que morre CALADO. O toast
    diz "registrado" e nada e' escrito. Oito dos dezoito agentes nasceram com
    esse defeito; este nao.
    """
    if spec is not None:
        _anotar(ledger, spec)
    try:
        with open(LEDGER, "w", encoding="utf-8") as f:
            json.dump(ledger, f, indent=2, ensure_ascii=False)
    except OSError:
        pass


def _fresco(pool, usados, rng):
    livres = [x for x in pool if x["id"] not in usados]
    return rng.choice(livres or pool)


def _por_id(pool, valor):
    """A entrada do pool, aceitando ID (string) OU a ENTRADA JA' RESOLVIDA.

    ⛔⛔ OS DOIS FORMATOS SAO OBRIGATORIOS, e o segundo e' o que o PAINEL manda:
    o dropdown devolve um id, mas o CADEADO devolve `self.spec[chave]`, o
    dicionario inteiro. A versao ingenua (`x["id"] == valor`) nunca casa com um
    dicionario, devolvia `None`, e o `resumo_pt` estourava
    `TypeError: 'NoneType' object is not subscriptable` DENTRO do callback do
    tkinter — onde a excecao morre calada. No `.exe` (pythonw, sem console) o
    efeito era o SORTEAR simplesmente nao fazer nada.
    ⚠️ Atingia TODOS os eixos travaveis deste motor, e e' o mesmo defeito que o
    `_por_id` do `prato16` ja' documentava desde que quebrou os quatro cadeados
    do GOOD 16. Corrigido em 2026-08-13, achado por uma revisao adversarial que
    EXERCITOU o painel em vez de so' abri-lo.
    ⚠️ O fallback e' `pool[0]`, nunca `None`: id que sumiu do pool (ledger
    velho, menu de outra versao) tem de cair no caminho normal, nao estourar.
    """
    if isinstance(valor, str):
        return next((x for x in pool if x.get("id") == valor), pool[0])
    return valor


def _cabe(pool, reserva, cena, o=None):
    """As entradas que cabem depois de reservar `reserva` palavras.

    ⚠️ O fallback NAO devolve o pool inteiro — isso e' estouro silencioso, e foi
    assim que a cena 2 do TROCA passou de 25 para 27 palavras sem ninguem ver.
    Devolve a entrada mais CURTA, e quem reclama depois e' o linter.
    ⛔ Mede a string FORMATADA, nunca o template: o `{o}` vale 1 palavra, mas se
    um dia entrar placeholder longo aqui a conta tem de continuar certa.
    """
    def _n(x):
        return _palavras(x.format(o=o) if o is not None else x)
    v = [x for x in pool if _n(x) + reserva <= TETO_FALA[cena]]
    return v or [min(pool, key=_n)]


def _mn(pool, o=None):
    return min(_palavras(x.format(o=o) if o is not None else x) for x in pool)


# ===========================================================================
# SORTEIO
# ===========================================================================

def _falas(spec, rng, quais=(0, 1)):
    """As duas falas.

    ⛔⛔ CT4 — UM APELIDO POR VIDEO, repetido nos DOIS takes. Em 24s e cinco
    cenas o bordao e' o risco; em 16s e duas cenas o risco e' o oposto: o corte
    ZERA a memoria de trabalho, e trocar `pecker` por `Johnson` no segundo 9
    obriga o espectador a remapear justamente quando ele ja' esta' com um pe'
    fora. Por isso o apelido mora no SPEC, e nao e' re-sorteado por cena.
    ⚠️ Quando o operador re-sorteia UMA cena pelo painel, o apelido do spec
    continua o mesmo — que e' exatamente o que o CT4 exige.
    """
    o = spec["apelido"]
    f = dict(enumerate(spec.get("falas", ["", ""])))

    if 0 in quais:
        # a FALHA carrega o orgao e o numero — menos substitutos, escolhe antes.
        fa = rng.choice(_cabe(FALHAS, _mn(VIRADAS), 1, o)).format(o=o)
        cu = rng.choice(_cabe(VIRADAS, _palavras(fa), 1))
        f[0] = "%s %s" % (fa, cu)

    if 1 in quais:
        # o CTA carrega o literal e o endereco de entrega: nao se encurta, e por
        # isso escolhe PRIMEIRO. A PROVA e' o beat intercambiavel e vai por
        # ultimo, absorvendo a sobra.
        ct = rng.choice(_cabe(CTAS, _mn(MECANISMOS, o) + _mn(PROVAS), 2))
        me = rng.choice(_cabe(MECANISMOS,
                              _palavras(ct) + _mn(PROVAS), 2, o)).format(o=o)
        pr = rng.choice(_cabe(PROVAS, _palavras(me) + _palavras(ct), 2))
        f[1] = "%s %s %s" % (me, pr, ct)

    return f


def sortear(pagina, rng, ledger, travas=None):
    travas = travas or {}
    hist = (ledger or {}).get(pagina, {})
    etnia = ETNIA.get(pagina, "white American")

    # ⛔ O MUNDO E' FILTRADO PELA ETNIA DA PAGINA (mecanica do FALTA 16). A
    # congruencia do funil nao e' so' do rosto: um homem branco num quarto de
    # brownstone do Harlem quebra a leitura tanto quanto trocar a etnia.
    pool_m = mundos_da_etnia(etnia)
    if travas.get("familia_mundo"):
        fam = [m for m in pool_m if m["familia"] == travas["familia_mundo"]]
        pool_m = fam or pool_m
    mundo = (_por_id(MUNDOS, travas["mundo"]) if travas.get("mundo")
             else _fresco(pool_m, hist.get("mundo", [])[-5:], rng))

    homem = (_por_id(HOMENS, travas["homem"]) if travas.get("homem")
             else _fresco(HOMENS, hist.get("homem", [])[-3:], rng))
    # ⭐ a mulher tem etnia SOLTA — ela nao e' o REF de congruencia, ele e'.
    mulher = (_por_id(MULHERES, travas["mulher"]) if travas.get("mulher")
              else _fresco(MULHERES, hist.get("mulher", [])[-4:], rng))
    copo = (_por_id(COPOS, travas["copo"]) if travas.get("copo")
            else _fresco(COPOS, hist.get("copo", [])[-4:], rng))

    spec = {
        "pagina": pagina, "etnia": etnia,
        "mundo": mundo, "homem": homem, "mulher": mulher, "copo": copo,
        # ⭐ MODO RECEITA (2026-08-10): vem do toggle do painel via
        # `travas["receita"]`. Nao troca pessoa nenhuma — troca o que esta'
        # nas maos deles no take 2 e poe a receita na borda da agua.
        # ⚠️ Guardado no SPEC e nao lido do `travas` na montagem: o painel
        # re-sorteia a fala sem re-sortear a cena, e a montagem precisa saber
        # o estado mesmo quando o `travas` nao passa por ali.
        "receita": bool((travas or {}).get("receita")),
        "corpo_h": rng.choice(CORPOS_H),
        # ⛔ CT4b — o apelido sai de `sc.APELIDOS_16` e de mais lugar nenhum.
        # `soldier` soa filme de guerra para ouvido americano e `tool` e'
        # ambiguo em giria dos EUA; os dois seguem no NUCLEO so' para as lentes
        # DETECTAREM o orgao.
        "apelido": rng.choice(list(sc.APELIDOS_16)),
    }
    spec["falas"] = [v for _, v in sorted(_falas(spec, rng).items())]
    return spec


def nova_fala(spec, i, rng):
    return _falas(spec, rng, quais=(i,))[i]


# ===========================================================================
# MONTAGEM
# ===========================================================================

CAUDA = ("Shot on iPhone, natural grain. No on-screen text, no subtitles, no "
         "captions, no watermark.")

# ⛔ ANTICELEB — nunca INVENTAR declaracao de conformidade ("fully clothed",
# "not underage" sao municao: nomeiam a categoria que o classificador policia).
# ⚠️ Esta frase existe porque o BLOCO 0 do repo inteiro a carrega e o gerador a
# espera; o que se proibe e' escrever uma nova.
ANTICELEB = ("An ordinary everyday relatable person with a plain unremarkable "
             "face, not a celebrity, not a model, not an actor.")


def _maos_da_agua(spec):
    """O que esta' nas maos deles no take 2 — DEPENDE DO MODO RECEITA.

    Desligado: o quadro de sempre, os DOIS com copo. A bebida E' o gelatin
    trick (decisao 2 do operador) e a prova e' o casal segurando.
    Ligado: a receita vem para a borda, ELE MEXE, e so' ELA fica com o copo —
    ordem do operador. Nao e' soma: as duas maos dele passam a ter UMA
    agenda, e mandar segurar copo E colher e' a contradicao das duas colheres.
    """
    if spec.get("receita"):
        # ⚠️ `In her own hand she is holding X`, e nao `She is holding X in
        # her own hand`: varias entradas de COPOS terminam em `with a pale
        # drink IN IT`, e a segunda forma saia com `in it in her own hand`.
        # Achado LENDO o bloco montado.
        return ("In her own hand she is holding %s. %s"
                % (spec["copo"]["img"], WF_RECEITA_IMAGE))
    return ("Each of them is holding %s, one in his hand and one in hers."
            % spec["copo"]["img"])


def _maos_da_agua_take(spec):
    if spec.get("receita"):
        return WF_RECEITA_TAKE
    return ("Each of them simply holds their own drink the whole time and "
            "neither one drinks from it or lifts it to their mouth, and "
            "neither hands theirs to the other.")


def montar(spec):
    m, h, w = spec["mundo"], spec["homem"], spec["mulher"]
    et = spec["etnia"]
    b = {}

    # --- BLOCO 0 — a REF e' o HOMEM (ele e' quem fala) ---------------------
    b["BLOCO 0 (REF)"] = (
        "REF 01: Photo of a real person, a %d-year-old %s man, chest up, "
        "facing the camera directly, tired steady expression. %s, %s, wearing "
        "a plain gold wedding band. %s Hands out of frame, no objects. Plain "
        "neutral gray background, soft even frontal light. Slight sensor "
        "grain, soft focus, raw iPhone front camera aesthetic. No subtitles, "
        "no captions, no burned-in text, no watermark."
        % (h["idade"], et, h["marca"], h["sinal"], ANTICELEB))

    # --- TAKE 1 — A CAMA FRIA ---------------------------------------------
    # ⛔ A FRIEZA E' CONTADA PELA POSTURA DELA, nunca por fala: bracos cruzados,
    # rosto virado para o outro lado. Ela e' MUDA (WF1) e a inversao desta
    # postura no take 2 E' o video (WF2).
    # ⚠️ O tronco dele fica virado para longe dela e o rosto virado para a
    # lente: a postura derrotada do frame de origem fica de pe' e a fala tem
    # para onde sair. Ver a PENDENCIA no cabecalho.
    b["IMAGE 01/02"] = (
        "IMAGE 01/02: Medium shot in %s. In the foreground, sitting on the "
        "edge of the bed with his body turned away from her and his face "
        "turned to the camera, is a %d-year-old %s man, bare-chested, %s, his "
        "shoulders down and his head low. %s, %s. Behind him, lying back "
        "across the bed on top of the covers, is a %d-year-old %s woman, %s, "
        "wearing %s, her arms folded across her chest and her face turned away "
        "from him toward the far wall. The bedclothes are white and rumpled. "
        "They are the only two people in the frame. %s. %s"
        % (m["q_cen"], h["idade"], et, spec["corpo_h"], _cap(h["marca"]),
           h["sinal"], w["idade"], w["etnia"], w["marca"], m["dela_q"],
           _cap(m["q_luz"]), CAUDA))

    b["TAKE 01/02"] = (
        "TAKE 01/02: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway, no cuts, and the camera does not move. He "
        "talks straight into the lens the whole time and never turns to look "
        "at her. She stays exactly where she is, her arms folded across her "
        "chest and her face turned away, and she never speaks. Only he speaks. "
        "Nothing else in the frame changes.\n"
        "Dialogue: \"%s\"\nAudio: %s. No music."
        % (sonorizar(spec["falas"][0]), m["q_audio"]))

    # --- TAKE 2 — A VIRADA NA AGUA ----------------------------------------
    # ⛔⛔ A ANCORA DE CONTINUIDADE VEM AQUI EM CINCO PECAS: idade, etnia,
    # marca, sinal e a frase `It is the same man`. Sem isso o Veo desenha OUTRA
    # pessoa — no VAZAMENTO o corpo-prova voltou como um senhor de oculos e
    # bigode, e como o TAKE diz `Only he speaks` o estranho falava a fala do
    # REF. Lente WF3.
    b["IMAGE 02/02"] = (
        "IMAGE 02/02: Medium shot at %s. In the water is the same "
        "%d-year-old %s man from the first scene, %s, %s, %s, sitting in %s "
        "with the water at his chest, his face fully in frame and turned to "
        "the camera. It is the same man, not a different person. Pressed "
        "against his side with her shoulder against his chest is the same "
        "%d-year-old %s woman, %s, wearing %s; she looks at him and says "
        "nothing. %s They are the only two people in the "
        "frame. %s. %s"
        % (m["a_cen"], h["idade"], et, h["marca"], h["sinal"], spec["corpo_h"],
           m["a_agua"], w["idade"], w["etnia"], w["marca"], m["dela_a"],
           _maos_da_agua(spec), _cap(m["a_luz"]), CAUDA))

    b["TAKE 02/02"] = (
        "TAKE 02/02: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway, no cuts, and the camera does not move. He "
        "talks straight into the lens the whole time and it is the same man as "
        "in the first scene. She stays pressed against his side and never "
        "moves away from him, and she never speaks. Only he speaks. %s The "
        "water keeps moving the way "
        "water moves and nothing else in the frame changes.\n"
        "Dialogue: \"%s\"\nAudio: %s. No music."
        % (_maos_da_agua_take(spec), sonorizar(spec["falas"][1]),
           m["a_audio"]))

    # ⛔ trava de texto queimado em todo TAKE — o watermark que o operador viu
    # vazando nos reels da concorrente (2026-08-01).
    return sc.selar_takes(b)


# ===========================================================================
# LINTER — as regras WF
# ===========================================================================

def _wf1_ela_muda(spec, blocos, achados):
    """WF1 — ela nunca fala, e os DOIS takes tem de DIZER isso.

    ⚠️ Omitir nao basta: o Veo poe as duas bocas a mexer se ninguem proibir, e o
    dialogo dele sai monofonico e torto. Foi assim que a cena do casal do
    VAZAMENTO caiu.
    """
    for k in ("TAKE 01/02", "TAKE 02/02"):
        if "Only he speaks" not in blocos[k]:
            achados.append(("ERRO", "WF1: %s sem `Only he speaks` — sem isso o "
                                    "Veo mexe a boca dela tambem" % k))
        if "she never speaks" not in blocos[k]:
            achados.append(("ERRO", "WF1: %s nao diz que ela e' muda — a "
                                    "mudez dela e' invariante do angulo" % k))


def _wf2_inversao(spec, blocos, achados):
    """⭐⭐ WF2 — A INVERSAO E' O VIDEO.

    ⛔ Bracos cruzados e rosto virado no take 1; corpo colado no take 2. Sem os
    dois lados o angulo deixa de existir: sobra um homem falando de gelatina
    numa piscina, que e' o GOOD 16. A prova deste agente nao e' um corpo nem um
    prop — e' o casamento, e ela so' se le' na DIFERENCA entre os dois quadros.
    """
    i1, i2 = blocos["IMAGE 01/02"], blocos["IMAGE 02/02"]
    if "arms folded across her chest" not in i1:
        achados.append(("ERRO", "WF2: a IMAGE 01 nao tem os bracos cruzados "
                                "dela — a frieza e' contada pela POSTURA, e "
                                "sem ela nao ha' o que inverter no take 2"))
    if "turned away from him" not in i1:
        achados.append(("ERRO", "WF2: a IMAGE 01 nao vira o rosto dela para o "
                                "outro lado — metade do lado frio do angulo"))
    if "Pressed against his side" not in i2:
        achados.append(("ERRO", "WF2: a IMAGE 02 nao tem ela colada nele — a "
                                "inversao dos bracos cruzados E' o video"))
    if "shoulder against his chest" not in i2:
        achados.append(("ERRO", "WF2: a IMAGE 02 nao encosta o ombro dela no "
                                "peito dele — `ao lado` nao inverte `virada "
                                "para o outro lado`"))


def _wf3_ancora(spec, blocos, achados):
    """⛔⛔ WF3 — A ANCORA DE CONTINUIDADE DO HOMEM NO TAKE 2.

    Decisao 4 do operador: no take 2 ele aparece COM ROSTO e e' O MESMO. Isso
    exige ancora forte, e a licao e' paga: no VAZAMENTO a ancora estava na
    camisa (`wearing the same shirt`) e o render devolveu um senhor de oculos e
    bigode no lugar do corpo-prova — e como o TAKE diz `Only he speaks`, o
    ESTRANHO falava a fala do REF.
    ⚠️ Cinco pecas, e nenhuma delas sozinha basta: idade + etnia + marca +
    sinal + a frase explicita.
    """
    h, et = spec["homem"], spec["etnia"]
    i2, t2 = blocos["IMAGE 02/02"], blocos["TAKE 02/02"]
    if "the same %d-year-old" % h["idade"] not in i2:
        achados.append(("ERRO", "WF3: a IMAGE 02 nao repete `the same "
                                "%d-year-old` — o Veo troca de pessoa"
                        % h["idade"]))
    if et not in i2:
        achados.append(("ERRO", "WF3: a IMAGE 02 nao repete a etnia (%r)" % et))
    for peca, rot in ((h["marca"], "marca"), (h["sinal"], "sinal")):
        if peca not in i2:
            achados.append(("ERRO", "WF3: a IMAGE 02 nao repete o %s facial "
                                    "sorteado (%r) — e' a ancora que o Veo "
                                    "usa para nao trocar de homem"
                            % (rot, peca[:38])))
    if "It is the same man" not in i2:
        achados.append(("ERRO", "WF3: a IMAGE 02 nao diz `It is the same man` "
                                "— a ancora implicita nao segura troca de "
                                "cenario, roupa e luz de uma vez"))
    if "the same man as in the first scene" not in t2:
        achados.append(("ERRO", "WF3: o TAKE 02 nao repete a ancora — a IMAGE "
                                "segura o primeiro frame, o TAKE segura os 8 "
                                "segundos"))


def _wf4_copo(spec, blocos, achados):
    """WF4 — o copo do trick nas maos dos DOIS, e os dois bebendo.

    ⛔ Decisao 2 do operador: a bebida E' o gelatin trick. Ela e' a prova visual
    do que a fala vende — se so' um dos dois segura, o video mostra o remedio
    DELE em vez do ritual DO CASAL, que e' o payoff deste angulo.
    """
    i2, t2 = blocos["IMAGE 02/02"], blocos["TAKE 02/02"]
    # ⛔⛔ 2026-08-10 — ESTA METADE PASSOU A VALER SO' COM O MODO RECEITA
    # DESLIGADO. Ordem do operador ao encomendar o toggle: *"so' a mulher com
    # copo quando o toggle estiver ativado"*. Com o modo ligado as duas maos
    # DELE estao na tigela, e cobrar o copo dele aqui seria a lente exigindo
    # TRES MAOS — o mesmo defeito que a bancada do ESCANDALO 16 produziu hoje.
    # ⚠️ E a regra que ela guarda continua inteira nos dois estados: o copo
    # (a bebida E' o gelatin trick) NUNCA some do quadro; o que muda e' de
    # quantas maos ele sai.
    if not spec.get("receita") and "Each of them is holding" not in i2:
        achados.append(("ERRO", "WF4: a IMAGE 02 nao poe o copo nas maos dos "
                                "DOIS — a bebida e' o gelatin trick e a prova "
                                "e' o casal bebendo"))
    # ⛔ 2026-08-10 — ORDEM DO OPERADOR: *"o REF so' tem que parar de falar
    # enquanto bebe, deixe-os apenas segurando as bebidas, nao precisa deles
    # tomarem no take"*. Beber e falar ao mesmo tempo e' fisicamente
    # incompativel, e o gerador resolve o conflito do pior jeito possivel: ou
    # corta a fala no gole, ou anima uma boca que fala com o copo na frente.
    # A prova visual e' o copo NA MAO DOS DOIS, nao o gole.
    # ⚠️ A lente NAO morreu — trocou de pergunta: antes cobrava o gole,
    # agora cobra que ele NAO aconteca.
    if "and both are drinking" in i2:
        achados.append(("ERRO", "WF4: a IMAGE 02 poe os dois BEBENDO — beber e falar ao mesmo tempo nao cabe em 8 segundos; eles apenas SEGURAM"))
    if spec["copo"]["img"] not in i2:
        achados.append(("ERRO", "WF4: o copo sorteado (%r) nao chega a' IMAGE "
                                "02 — eixo de painel que nao muda o video"
                        % spec["copo"]["id"]))
    # ⛔ A REGRA E' "O GOLE E' PROIBIDO EXPLICITAMENTE", e a REDACAO segue quantas
    # pessoas seguram copo. Com o MODO RECEITA desligado sao dois (`neither
    # one`); ligado, so' ELA (`never drinks from it`). Cobrar o literal de dois
    # no estado de um seria a lente exigindo uma frase que mente — e ela
    # reprovou 200 de 200 assim antes desta correcao.
    if not any(x in t2 for x in ("neither one drinks from it",
                                 "never drinks from it")):
        achados.append(("ERRO", "WF4: o TAKE 02 nao proibe o gole — sem a "
                                "proibicao explicita o gerador poe o copo na "
                                "boca no meio da fala"))


def _wf5_sem_texto(spec, blocos, achados):
    """WF5 — nada de texto queimado, e aqui ha' um motivo A MAIS.

    ⛔ O frame da FONTE tem legenda queimada (`ABOUT TO LEAVE`). Quem for
    "fiel a' fonte" sem ler isto vai pedir a legenda ao gerador — e a nossa
    legenda nasce DEPOIS, no Veo Editor, do Whisper rodando sobre o audio.
    Texto vindo do gerador entra por cima e nao ha' como tirar.
    """
    sc.lint_sem_texto(blocos, achados)
    for k in ("IMAGE 01/02", "IMAGE 02/02"):
        if "No on-screen text" not in blocos[k]:
            achados.append(("ERRO", "WF5: %s sem a trava de texto — a fonte "
                                    "tem legenda queimada e nos nao "
                                    "queimamos" % k))


# ⛔⛔ WF6 — NAO HA' PROP FALICO NESTE ANGULO, e a ausencia e' VIGIADA.
# ⚠️ Dezenove dos vinte e dois motores do parque tem um; quem chegar aqui vindo
# de qualquer um deles vai sentir falta e vai querer "consertar". A prova deste
# agente e' o CASAMENTO — bracos cruzados que viram corpo colado — e um geoduck
# na cena mataria justamente isso.
_PROXY_FALICO = re.compile(
    r"\b(geoduck|clam|siphon|banana|cucumber|carrot|squash|zucchini|sausage|"
    r"eggplant|anatomical model|anatomy model|penile|phallic|shaft)\b", re.I)


def _wf6_sem_prop(spec, blocos, achados):
    for nome in sorted(blocos):
        m = _PROXY_FALICO.search(blocos[nome])
        if m:
            achados.append(("ERRO", "WF6: %s traz um proxy falico (%r) — este "
                                    "angulo NAO tem prop, e a prova dele e' o "
                                    "casamento (bracos cruzados -> corpo "
                                    "colado)" % (nome, m.group(0))))


# ⛔⛔ WF10 — O DEITICO DO TAKE 2 NAO TEM PARA ONDE APONTAR.
# ⚠️ Lente escrita DEPOIS de o defeito passar por todos os medidores externos:
# `She unpacked that bag that week.` e `She quit sleeping on that side.` viviam
# no pool das PROVAS e o `medir_deiticos` nao os via — ele mede DENTRO da
# sentenca, e aqui o antecedente dependia de qual entrada de OUTRO pool tinha
# caido no take ANTERIOR. Em 31 de 36 e 27 de 35 sorteios nao havia mala nem
# lado nenhum.
#
# ⭐ A lente e' de escopo EXATO, e o escopo e' o argumento: o take 2 se passa
# DENTRO D'AGUA, oito segundos depois de um corte. Ele nao herda um objeto
# sequer do quarto, e as suas tres batidas (mecanismo · prova · CTA) nao
# introduzem substantivo nenhum para apontar depois. Logo, no take 2, qualquer
# `that/those/these <substantivo>` que nao tenha sido dito ANTES na propria fala
# e' um deitico apontando para o vazio.
#
# ⛔ O TAKE 1 FICA DE FORA DE PROPOSITO, e a exclusao nao e' preguica: la' o
# quarto esta' em quadro, e `She stayed on her side of that bed` aponta para uma
# cama que o espectador esta' vendo. Estender a lente para o take 1 reprovaria a
# copy certa (modo de falha §16), e ainda precisaria adivinhar quando `that` e'
# conjuncao (`I let that run for months`).
_DEITICO_T2 = re.compile(r"\b(that|those|these)\s+([a-z]{3,})\b", re.I)


def _wf10_deitico_orfao(spec, blocos, achados):
    fala = spec["falas"][1]
    for m in _DEITICO_T2.finditer(fala):
        alvo = m.group(2).lower()
        if alvo not in fala[:m.start(2)].lower():
            achados.append(("ERRO",
                            "WF10: o take 2 diz %r e o substantivo nunca foi "
                            "introduzido — o take 2 e' DENTRO D'AGUA, oito "
                            "segundos e um corte depois do quarto, e nao herda "
                            "objeto nenhum para o deitico apontar"
                            % m.group(0)))


def _wf7_orcamento(spec, blocos, achados):
    for i, fala in enumerate(spec["falas"], 1):
        n = _palavras(fala)
        if n > TETO_FALA[i]:
            achados.append(("ERRO", "WF7: cena %d com %d palavras (teto %d) — "
                                    "a fala e' CORTADA no render"
                            % (i, n, TETO_FALA[i])))
        if n < PISO_FALA[i]:
            achados.append(("AVISO", "WF7: cena %d com %d palavras (piso %d) — "
                                     "sobra ar morto no take"
                            % (i, n, PISO_FALA[i])))


def _wf8_etnia(spec, blocos, achados):
    """WF8 — a congruencia governa O HOMEM, que e' quem fala.

    ⭐ E cobra tambem o MUNDO: a etnia da pagina tem de caber no arquetipo
    regional sorteado. Congruencia que so' olha o rosto deixa o homem branco
    num brownstone do Harlem, e a leitura quebra do mesmo jeito.
    """
    et = spec["etnia"]
    for k in ("BLOCO 0 (REF)", "IMAGE 01/02", "IMAGE 02/02"):
        if et not in blocos[k]:
            achados.append(("ERRO", "WF8: %s sem a etnia da pagina (%r) — a "
                                    "congruencia com o avatar sai do video sem "
                                    "ninguem ver" % (k, et)))
    if et not in spec["mundo"]["etnias"]:
        achados.append(("ERRO", "WF8: o mundo %r nao comporta a etnia da "
                                "pagina (%r) — o arquetipo regional arrasta a "
                                "casa inteira, nao so' o fundo"
                        % (spec["mundo"]["id"], et)))


def _wf9_contrato16(spec, blocos, achados):
    """As NOVE travas do CONTRATO DE COPY 16s, cobradas de dentro do motor.

    ⭐ `isca_absurda=False`: este angulo nao promete nada no take 1 que ele
    mesmo va' desmentir meio segundo depois (o take 1 e' a falha + o custo
    conjugal, nao substancia absurda). Logo o CT7 — verbo de ereccao colado no
    orgao — vale nos DOIS takes, e nao so' no do CTA.
    ⚠️ `sys.modules[__name__]` e nao outro modulo: a lente le' `base.NUCLEO`, e
    o NUCLEO e' deste arquivo.
    """
    sc.lint_copy16(sys.modules[__name__], spec, achados, isca_absurda=False)


def _wf11_modo_receita(spec, blocos, achados):
    """WF11 — o MODO RECEITA muda o quadro, e a caixa NUNCA molha.

    ⛔ A lente cobra os DOIS estados, que e' o unico jeito de um toggle nao
    virar forma sem funcao. Este repo ja' pagou o botao aceso com sorteio igual
    tres vezes.

    ⛔⛔ E o controle central e' o PAPELAO NA AGUA. Eles estao sentados com a
    agua no peito; a caixa de bicarbonato e' de PAPELAO e a tigela tem cubos que
    boiariam. Por isso as duas ficam na BORDA, secas, e os bracos dele saem da
    agua. E' a licao paga no FIGHT 16, onde o primeiro render pos o homem com a
    agua no peito segurando uma caixa de papelao — e nenhuma lente pegou,
    porque nenhuma cruzava OBJETO com LUGAR.
    """
    i2, t2 = blocos["IMAGE 02/02"], blocos["TAKE 02/02"]
    if not spec.get("receita"):
        # ⛔ desligado, a receita NAO pode vazar para o quadro
        for pedaco, rot in (("cubes of set amber gelatin", "a tigela"),
                            ("box of baking soda", "a caixa"),
                            ("turning the spoon", "ele mexendo")):
            if pedaco in i2:
                achados.append(("ERRO", "WF11: %s aparece com o MODO RECEITA "
                                        "DESLIGADO — o toggle nao esta' "
                                        "mudando nada" % rot))
        return
    for pedaco, rot in (("cubes of set amber gelatin", "a tigela de cubos"),
                        ("box of baking soda", "a caixa de bicarbonato"),
                        ("turning the spoon in it", "ele MEXENDO"),
                        ("out of the water and dry", "a borda SECA"),
                        ("arms are clear of the water", "os bracos fora d'agua")):
        if pedaco not in i2:
            achados.append(("ERRO", "WF11: a IMAGE 02 sem %s — o modo esta' "
                                    "ligado e o quadro nao mostra a receita"
                            % rot))
    if WF_RECEITA_TAKE not in t2:
        achados.append(("ERRO", "WF11: o TAKE 02 sem a coreografia da colher e "
                                "a trava da borda — objeto que pode ser "
                                "levantado entra na agua no movimento"))
    # ⛔ ele nao pode segurar copo E colher: sao duas agendas para duas maos, e
    # o gerador resolve desenhando a terceira.
    if "Each of them is holding" in i2:
        achados.append(("ERRO", "WF11: o modo esta' ligado e a IMAGE 02 ainda "
                                "poe copo nas maos dos DOIS — ele esta' "
                                "mexendo a tigela com as duas"))
    # ⛔ e ELA continua com o copo: a bebida E' o gelatin trick e nao pode sumir
    if spec["copo"]["img"] not in i2:
        achados.append(("ERRO", "WF11: o copo sorteado sumiu do quadro — com o "
                                "modo ligado ele fica NA MAO DELA"))


def lint(spec, blocos):
    """⚠️ Lint PROPRIO, nao `sc.lint_curto`. Aquele e' da maquinaria de colapso
    5->3 e pede `base` e `mapa`, que este motor nao tem: ele nao deriva de motor
    longo nenhum — nasceu direto em dois takes."""
    ach = []
    falas = spec["falas"]
    sc.lint_tags(blocos, ach)
    sc.lint_take_vs_image(blocos, ach)
    sc.lint_isca_cta(falas[-1], ach, "a cena 2 (CTA)")
    sc.lint_cta_literal(falas[-1], ach, "a cena 2 (CTA)")
    sc.lint_painel_honesto(sys.modules[__name__], spec, blocos, ach)
    for f in (_wf1_ela_muda, _wf2_inversao, _wf3_ancora, _wf4_copo,
              _wf5_sem_texto, _wf6_sem_prop, _wf7_orcamento, _wf8_etnia,
              _wf9_contrato16, _wf10_deitico_orfao,
              _wf11_modo_receita):
        f(spec, blocos, ach)
    return ach


# ===========================================================================
# PAINEL
# ===========================================================================

EIXOS_UI = [
    ("mundo", "A REGIAO", "MUNDOS", "regiao"),
    ("homem", "QUEM FALA", "HOMENS", "id"),
    ("mulher", "A ESPOSA", "MULHERES", "id"),
    ("copo", "O COPO DO TRICK", "COPOS", "curto"),
]

EIXOS_TRAVAVEIS = ["mundo", "homem", "mulher", "copo"]

TRAVAS_UI = [("familia_mundo", "regiao", ["livre"] + FAMILIAS_MUNDO)]

# ⭐⭐ O DROPDOWN DE QUEM FALA — e' ELE que da' FUNCAO ao campo `rotulo`.
# Ordem do operador (2026-08-13): *"implemente esse mecanismo e menu drop down
# para todos os demais agentes 16"*, tendo o MEL 16 como modelo.
# ⛔ Sem esta linha o `rotulo` seria comentario caro: 24 textos escritos,
# medidos e travados, e nenhum olho humano os veria. Forma sem funcao e' o
# defeito que este repo mais paga (licoes-de-construcao §41).
# ⛔ POR QUE DROPDOWN E NAO `TRAVAS_UI`: a barra de travas desenha UM BOTAO POR
# OPCAO, lado a lado. Serve para as regioes; com 24 REFs ela estoura a largura
# da janela e vira uma parede de botoes ilegivel.
# ⚠️ O campo exibido e' `rotulo`, NAO `id`: o `ui_agente` monta o mapa
# texto -> id, entao o operador escolhe "60y · careca com laterais + bigode
# grosso" e o motor recebe `careca_bigode`. Menu de ids obriga a abrir o
# codigo para saber o que se escolheu.
# ⚠️ E o `EIXOS_UI` acima continua com `id` de proposito: la' o `_texto_eixo`
# ja' prefixa a idade, e trocar para `rotulo` imprimiria "57y · 57y · grisalho".
# ⛔ ESTE MOTOR E' O IRMAO DO `bed16_short.py` (o BED nasceu como copia deste) e
# os dois pools de HOMENS sao identicos — os rotulos foram escritos iguais nos
# dois DE PROPOSITO: o mesmo rosto tem de ler igual nos dois paineis. Divergir
# aqui e' inventar diferenca onde o pool nao tem nenhuma.
DROPDOWNS_UI = [("homem", "QUEM FALA", "HOMENS", "rotulo")]

# ⚠️ `mundo` ja' entra na lista de ignorados do `lint_painel_honesto` (o valor
# do eixo e' um id interno). Os outros tres chegam ao quadro pelo `marca`,
# pelo `marca` dela e pelo `img` do copo — e a lente cobra isso a cada sorteio.
IGNORA_PAINEL = ("mundo",)

# ⛔ Nenhum eixo do painel mexe na copy neste motor: a fala nao cita o quarto, a
# agua, o copo nem as pessoas. Trocar um eixo remonta o QUADRO e mantem a fala,
# que e' o comportamento certo — e declarar o dicionario vazio e' declarar que
# alguem verificou, em vez de deixar o `getattr` decidir por omissao.
EIXOS_QUE_MEXEM_NA_COPY = {}


def resumo_pt(spec):
    """⚠️ Texto de PAINEL, nao copy falada — mas e' o unico lugar onde o
    operador le' o video ANTES de gastar credito gerando. Resumo errado faz ele
    aprovar o que nao viu (licoes §30), e resumo com a string inglesa crua
    ("ela atras de a black satin nightgown") faz ele parar de ler.
    """
    return ("16s, DOIS takes, região: %s. Take 1 — A CAMA FRIA: ele de %d "
            "anos, tronco nu na beirada da cama; ela atrás, deitada de "
            "camisola, com os BRAÇOS CRUZADOS e virada para o outro lado. A "
            "fala é a falha dele + o custo do casamento. Take 2 — A VIRADA: o "
            "MESMO homem, com rosto, dentro d'água (%s); ela COLADA nele, os "
            "dois com %s (que É o gelatin trick) e bebendo. Mecanismo, a prova "
            "(ela) e o CTA por último. Elenco: homem %s, esposa %s. Ela é MUDA "
            "nos dois takes."
            % (spec["mundo"]["regiao"], spec["homem"]["idade"],
               spec["mundo"]["a_agua"], spec["copo"]["nome"],
               spec["etnia"], spec["mulher"]["etnia"]))


# ===========================================================================
# AUTOTESTE
# ===========================================================================

def autoteste(n=400):
    import collections
    pags = sorted(ETNIA)
    erros = collections.Counter()
    dist = collections.defaultdict(set)
    apel = collections.Counter()
    tam = collections.defaultdict(list)
    falhas, avisos = [], 0

    for i in range(n):
        s = sortear(pags[i % len(pags)], random.Random(i), {})
        apel[s["apelido"]] += 1
        for c, f in enumerate(s["falas"], 1):
            dist[c].add(f)
            tam[c].append(_palavras(f))
        for nivel, msg in lint(s, montar(s)):
            if nivel == "ERRO":
                erros[msg[:70]] += 1
            else:
                avisos += 1

    print("WIFE 16 — %d sorteios" % n)
    for c in sorted(dist):
        v = sorted(tam[c])
        print("  cena %d: %d falas distintas · palavras min/med/max %d/%d/%d"
              % (c, len(dist[c]), v[0], v[len(v) // 2], v[-1]))
    print("  apelido: %s" % dict(apel))
    print("  linter: %d ERRO, %d AVISO" % (sum(erros.values()), avisos))
    for k, v in erros.most_common(5):
        print("     %3dx %s" % (v, k))

    # ⭐ [ALCANCE] — entrada que nao cabe somada aos MINIMOS dos outros beats
    # nunca e' sorteada. Ela nao e' rara: e' MORTA, e o autoteste a contava como
    # opcao viva. E' a licao §36 do repo.
    o_pior = max(sc.APELIDOS_16, key=len)
    for rot, pool, cena, outros in (
            ("FALHAS", FALHAS, 1, [VIRADAS]),
            ("VIRADAS", VIRADAS, 1, [FALHAS]),
            ("MECANISMOS", MECANISMOS, 2, [PROVAS, CTAS]),
            ("PROVAS", PROVAS, 2, [MECANISMOS, CTAS]),
            ("CTAS", CTAS, 2, [MECANISMOS, PROVAS])):
        reserva = sum(_mn(p, o_pior) for p in outros)
        mortas = [x for x in pool
                  if _palavras(x.format(o=o_pior)) + reserva > TETO_FALA[cena]]
        if mortas:
            falhas.append("[ALCANCE] %s: %d de %d nunca sao sorteadas "
                          "(teto real %d palavras)"
                          % (rot, len(mortas), len(pool),
                             TETO_FALA[cena] - reserva))

    # ⛔ CONTROLE DE CONTRATO: todo FALHAS tem de enunciar a falha (CT2). A
    # lente do `short_comum` so' olha a fala MONTADA — se um dia entrar uma
    # entrada sem verbo de falha, ela so' apareceria em ~1/14 dos sorteios.
    # ⚠️ 2026-08-13 — TRES VERBOS DE FALHA FALTAVAM NA LENTE, nao no pool. O
    # autoteste vinha REPROVADO acusando `My {o} did nothing for eight months`,
    # `My {o} hadn't worked in a year` e `My {o} was finished by fifty eight`,
    # que enunciam a falha tao bem quanto `quit`. ⛔ O conserto e' na REGEX e
    # nunca na copy: copy e' alcada do operador, e gate que acusa copy certa
    # ensina a ignorar o gate. Mesmo conserto no `bed16_short.py`.
    _CT2 = re.compile(r"\b(quit|soft|stopped|dead|failed|shut down|useless|"
                      r"lose it|not working|gave out|did nothing|"
                      r"hadn't worked|was finished)\b", re.I)
    sem_ct2 = [x for x in FALHAS if not _CT2.search(x)]
    if sem_ct2:
        falhas.append("CT2: %d entrada(s) de FALHAS sem verbo de falha: %s"
                      % (len(sem_ct2), sem_ct2[:2]))

    # ⛔⛔ CONTROLE POSITIVO DA WF10 — lente que nunca acusa nada e' forma sem
    # funcao, e "sem achado" nela significaria "ninguem olhou". As duas frases
    # abaixo sao as que MORRERAM na conferencia de 2026-08-10; se a lente parar
    # de pega-las, ela quebrou.
    for morta in ("She unpacked that bag that week.",
                  "She quit sleeping on that side."):
        prova = []
        _wf10_deitico_orfao({"falas": ["", "The gelatin trick opens blood flow "
                                           "to your pecker. %s" % morta]},
                            {}, prova)
        if not prova:
            falhas.append("WF10: a lente parou de acusar %r — ela era a unica "
                          "coisa entre este pool e o deitico orfao" % morta)
    limpo = []
    _wf10_deitico_orfao({"falas": ["", "The gelatin trick opens blood flow to "
                                       "your pecker. Now she pulls me to bed. "
                                       "Comment gelatin, and the recipe goes "
                                       "to your messages."]}, {}, limpo)
    if limpo:
        falhas.append("WF10: a lente acusa copy limpa (%s)" % limpo[0][1][:60])

    # ⛔ CONTROLE DE CONTRATO: todo MECANISMOS carrega o literal do funil.
    sem_lit = [x for x in MECANISMOS if "gelatin trick" not in x]
    if sem_lit:
        falhas.append("CT3: %d entrada(s) de MECANISMOS sem `gelatin trick`"
                      % len(sem_lit))

    # ⛔ CONTROLE DE MUNDO: cada etnia da tabela precisa de mundo compativel, e
    # cada mundo precisa dos dois ambientes da MESMA casa.
    for et in sorted(set(ETNIA.values())):
        if not [m for m in MUNDOS if et in m["etnias"]]:
            falhas.append("MUNDO: nenhum mundo comporta a etnia %r" % et)
    for m in MUNDOS:
        if "the same" not in m["a_cen"]:
            falhas.append("MUNDO %s: a agua nao diz `the same <casa>` — o "
                          "corte le' como dois videos colados" % m["id"])

    # ⛔⛔ O CONTRATO DO `rotulo` — o que o dropdown QUEM FALA exige do pool.
    # ⚠️ A UNICIDADE nao e' capricho: o `ui_agente._barra_dropdowns` monta o
    # mapa texto -> id com `if txt and txt not in mapa`, entao dois rotulos
    # iguais fazem o SEGUNDO homem DESAPARECER do menu — em silencio, sem erro
    # e sem log. Pool de 24 que o operador so' alcanca em 23 e' a mesma familia
    # do botao que mente, so' que por colisao de texto.
    # ⚠️ O TETO DE 42 e' a largura do combobox (`width=38` mais folga): rotulo
    # maior sai cortado na tela, e rotulo cortado volta a ser ilegivel — que e'
    # exatamente o problema que ele veio resolver.
    _rt_sem = [h["id"] for h in HOMENS if not h.get("rotulo")]
    if _rt_sem:
        falhas.append("ROTULO: %d entrada(s) de HOMENS sem rotulo — o dropdown "
                      "cai no `id` e o operador le' %r"
                      % (len(_rt_sem), _rt_sem[0]))
    _rt = [h.get("rotulo") or "" for h in HOMENS]
    _rt_rep = sorted({r for r in _rt if _rt.count(r) > 1})
    if _rt_rep:
        falhas.append("ROTULO: %d rotulo(s) repetido(s) (%r) — o segundo homem "
                      "some do dropdown sem erro nenhum"
                      % (len(_rt_rep), _rt_rep[0]))
    _rt_longo = [r for r in _rt if len(r) > 42]
    if _rt_longo:
        falhas.append("ROTULO: %d rotulo(s) acima de 42 chars (%r, %d) — "
                      "estoura a largura do menu"
                      % (len(_rt_longo), _rt_longo[0], len(_rt_longo[0])))

    # ⛔ E O CONTRATO DO PAINEL TEM DE APONTAR PARA COISA QUE EXISTE. O
    # `_barra_dropdowns` le' o pool com `getattr(motor, pool_nome, [])`: nome
    # errado devolve LISTA VAZIA e desenha um menu com `livre` e mais nada — o
    # seletor "funcionando" sem uma opcao dentro. Campo errado cai no
    # `e.get("id")` e devolve justamente o menu de ids que o rotulo veio abolir.
    # ⭐ E a ultima checagem e' de FUNCAO, nao de forma: escolher no menu tem de
    # SAIR no spec. Forma verificada e funcao nao verificada e' o defeito §41.
    for _dd_ch, _dd_tela, _dd_pool, _dd_campo in DROPDOWNS_UI:
        _dd_p = globals().get(_dd_pool)
        if not isinstance(_dd_p, list) or not _dd_p:
            falhas.append("DROPDOWNS_UI: o pool %r nao existe ou esta' vazio — "
                          "o menu %r sai so' com `livre`"
                          % (_dd_pool, _dd_tela))
            continue
        _dd_falta = [e.get("id") for e in _dd_p if not e.get(_dd_campo)]
        if _dd_falta:
            falhas.append("DROPDOWNS_UI: %d entrada(s) de %s sem o campo %r — "
                          "o menu cai no `id`"
                          % (len(_dd_falta), _dd_pool, _dd_campo))
        if _dd_ch not in EIXOS_TRAVAVEIS:
            falhas.append("DROPDOWNS_UI: o eixo %r nao esta' em EIXOS_TRAVAVEIS "
                          "— escolher no menu nao travaria nada" % _dd_ch)
        for _dd_e in _dd_p[:2] + _dd_p[-2:]:
            _dd_s = sortear(sorted(ETNIA)[0], random.Random(4242), {},
                            {_dd_ch: _dd_e["id"]})
            if _dd_s[_dd_ch]["id"] != _dd_e["id"]:
                falhas.append("DROPDOWNS_UI: escolher %r no menu %r devolveu "
                              "%r — o seletor nao fixa"
                              % (_dd_e["id"], _dd_tela, _dd_s[_dd_ch]["id"]))
                break

    if sum(erros.values()):
        falhas.append("%d ERRO de linter" % sum(erros.values()))
    if falhas:
        print("\nSELF-TEST REPROVADO (%d falha(s)):" % len(falhas))
        for f in falhas:
            print("   " + f)
        return 1
    print("\nAUTOTESTE OK.")
    return 0


def main():
    ap = argparse.ArgumentParser(description=TITULO)
    ap.add_argument("--pagina", choices=sorted(ETNIA), default="joe")
    ap.add_argument("--n", type=int, default=1)
    ap.add_argument("--seed", type=int)
    ap.add_argument("--regiao", choices=FAMILIAS_MUNDO)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--autoteste", action="store_true")
    a = ap.parse_args()

    if a.autoteste:
        return autoteste()

    led = _carregar_ledger()
    rng = random.Random(a.seed)
    travas = {"familia_mundo": a.regiao} if a.regiao else {}
    for _ in range(a.n):
        s = sortear(a.pagina, rng, led, travas)
        b = montar(s)
        print("=" * 70)
        print(resumo_pt(s))
        print("=" * 70)
        for k in sorted(b):
            print("\n%s\n" % b[k])
        for nivel, msg in lint(s, b):
            print("[%s] %s" % (nivel, msg))
        if not a.dry_run:
            _gravar_ledger(led, s)
    return 0


if __name__ == "__main__":
    sys.exit(main())
