#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE GOOD 16 — o casal na agua · 2 takes de 8s = 16 segundos.

⭐⭐ O PRIMEIRO ANGULO EM QUE O HOMEM FALA E A MULHER E' MUDA (o outro e' o BED
16). Os outros vinte tem narradora. Aqui a inversao e' o ativo: quem promete e'
o corpo que ja' entregou, e a prova social esta' encostada nele, sem dizer
palavra.

Doutrina completa em `../AGENTE_ED_GOOD_V1.md`, destilada da leitura otica a
1 fps de CINCO reels (2026-08-09): `agenteGOOD.mp4`, `agenteGOOD2.mp4`,
`prep1.mp4`, `prep2.mp4`, `prep3.mp4`.

O ARCO — 2 cenas de 8s, destino AdBatch Vertical 2:

    take 1  O AVISO      ele sentado na agua, a agua no peito, ela colada no
                         ombro dele · a TIGELA ja' esta' na borda, intocada
                         copy: o aviso + a esposa + ela nao aguenta
    take 2  O PREPARO    ele de pe' na mesma agua, a agua na cintura, inclinado
                         sobre a borda, MEXENDO a tigela com a colher e
                         SORRINDO · o SACHE amassado com `GELATIN` legivel logo
                         ao lado da tigela · ela colada no lado dele, olhando
                         para a tigela tambem
                         copy: a MISTURA nomeada + o preco + o CTA

⛔⛔ AS SETE MUDANCAS DE 2026-08-10 (ordem do operador) — o que este arquivo era
    ontem e por que deixou de ser:
 1. SAIU O ENQUADRAMENTO `so as maos`. Ver o tumulo em `⛔ O QUE MORREU AQUI`.
 2. Os 8 mundos aquaticos viraram QUINZE ARQUETIPOS POR REGIAO DOS EUA, cada um
    declarando `etnias` — a etnia da pagina FILTRA os mundos (mecanica do FALTA
    16 / BED 16). ⛔ Aquatico sempre: *"sempre voltado pra piscina, jacuzzi,
    nicho de verao"*.
 3. O take 2 deixou de ser `ele ergue o sache` e passou a ser O PREPARO DA
    RECEITA, elemento por elemento do print que o operador mandou.
 4. A copy do take 2 passou a ser TAXATIVA SOBRE A MISTURA: ela NOMEIA o que
    esta' na tigela (`the gelatin trick in this bowl`) e o que aquilo faz.
    ⛔ Isso NAO fura o CT5 — o que se proibe e' listar INGREDIENTE; a mistura
    nomeada e' a keyword do funil, que tem de ser dita.
 5. MODO BELA, pelo contrato compartilhado (`sc.ref_bela`).
 6. MODO FORTE, pelo contrato compartilhado (`sc.ref_forte`), e o toggle NASCE
    LIGADO (`MODOS_DEFAULT`). O `MODO_MUSCULOSO` proprio foi APOSENTADO.
 7. O take 1 nao mudou de cena. O UNICO ajuste foi de CONTINUIDADE, e e' o
    minimo possivel: a TIGELA passa a existir na borda ja' no take 1, intocada.
    Sem isso o take 2 introduziria tigela, colher e sache de uma vez, e o
    espectador leria dois videos colados. ⭐ De quebra o `this` dos AVISOS ganha
    referente EM QUADRO — ver a PENDENCIA de copy no fim deste cabecalho.

⛔ REGRAS QUE NASCEM COM O AGENTE
  · o CTA e' `gelatin`, nunca `recipe` (a fonte pede recipe; a automacao de DM
    casa palavra EXATA e o funil inteiro roda em gelatin)
  · ⛔⛔ GO1 — a fala e' sobre o CORPO (`harder and stronger`), NUNCA sobre o
    orgao: verbo de ereccao colado ao orgao e' lido como tumescencia e reprova
    (licao paga em campo no COLO 16, ~95% de recusa, 2026-08-09). E' por isso
    que este angulo passa onde os outros apanham, e por isso `{o}` nao existe
    nesta copy.

⛔ O QUE MORREU AQUI (2026-08-10) — e' divida do repo regra que some sem dizer
   por que:
  · ENQUADRAMENTOS / `so as maos` — o macro na bancada do banheiro, sem rosto e
    sem mulher. Ordem do operador. Com um enquadramento so', o EIXO INTEIRO
    deixa de existir: saiu o toggle da UI, saiu o ramo de montagem, saiu a
    lente GO3 (que cobrava `no face is in the frame`) e sairam os quatro pools
    que so' serviam a ele — POSTITS, BANCADAS, CLUTTER e o `bancada` do ledger.
    ⚠️ Pool orfao nao fica de enfeite: o [ALCANCE] o contaria como opcao viva.
  · FOLLOWS — o pedido de follow na fala. ⛔ CT8 do CONTRATO-COPY-16S: *"a
    mensagem e' enviada independente de seguirem ou nao"*. O beat inteiro sai e
    as palavras vao para o mecanismo. Era ele, colado depois do CTA, que fazia
    este motor violar o CT1 em 100% dos sorteios.
  · MODO_MUSCULOSO — flag propria que a UI nunca leu (o painel so' conhece
    `MODO_BELA` e `MODO_FORTE`). Substituida pelo MODO FORTE compartilhado:
    duas implementacoes do mesmo conceito e' a divida que o repo ja' pagou.

⚠️ PENDENCIA DE CENA, DECLARADA (alcada do operador): o print poe ele
   *"olhando para baixo, para a tigela"*, mas ele e' o NARRADOR e precisa falar
   na lente. O motor resolve como o BED 16 resolveu: TRONCO inclinado sobre a
   borda, MAOS na tigela e na colher, ROSTO virado para a camera, sorrindo. A
   postura do print fica de pe' e a fala tem para onde sair.

⚠️ PENDENCIA DE COPY, DECLARADA E NAO CORRIGIDA (copy e' alcada do operador):
   uma das seis entradas de AVISOS termina em `stay away from this.` — deitico
   terminal em construcao de contraste, que o `medir_deiticos` acusa em ~50 de
   1750 sentencas. Medido ANTES e DEPOIS desta passada: o numero nao mudou,
   porque a copy do take 1 nao foi tocada. ⭐ O que mudou foi o quadro: a tigela
   agora esta' em cena desde o primeiro frame, entao o `this` passou a ter para
   onde apontar. Conserto sugerido, se ele quiser: `If you are single, skip this
   bowl.` (7 palavras contra 8 — nao custa orcamento).

    python funil-organico/good16_short.py --pagina joe --n 1
    python funil-organico/good16_short.py --autoteste
    python funil-organico/good16_short_app.py
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

# ⛔ Os apelidos do orgao. Este agente NAO os usa na fala (ver GO1) — a lista
# existe para a lente conseguir PROIBI-LOS.
NUCLEO = ["Johnson", "pecker", "wiener", "soldier", "tool"]

LEDGER = os.path.join(AQUI, ".good-16-ledger.json")

TITULO = "AGENTE GOOD 16"
SLUG = "good-16"
SUBTITULO = ("2 takes de 8s = 16 segundos · o casal na agua · ele prepara a "
             "receita na borda e fala; ela e' muda")

CENAS_UI = ["1 · O AVISO", "2 · O PREPARO + CTA"]

# ⛔⛔ DUAS CENAS no teto FISICO de 25 palavras (8s a ~3,1 p/s). O teto vem de
# RENDER, nao de teoria: 32 cortou, 28 cortou, 25 nao.
TETO_FALA = {1: 25, 2: 25}
# ⛔ O piso e' ARITMETICA: a soma dos MINIMOS dos beats de cada cena. Piso
# calibrado com um beat que nao existe mais e' alarme que sempre dispara — e
# alarme que sempre dispara ensina a ignorar o linter inteiro (foi o que o
# CONTRATO-COPY-16S mediu no TROCA 16 depois de remover o follow).
# ⚠️ cena 2 = menor MISTURA (11) + menor PRECO (3) + menor CTA (9) = 23.
PISO_FALA = {1: 16, 2: 23}

# ⛔ Congruencia inviolavel: a etnia do REF casa com a etnia do avatar da
# pagina. ⭐ Neste angulo o REF que fala e' o HOMEM — entao a pagina governa
# ELE, e a mulher fica solta (ordem do operador, 2026-08-09).
ETNIA = {
    "roy": "white American", "dean": "white American",
    "earl": "white American",
    "jason": "Black American", "philippe": "Black American",
    "joe": "white American", "ray": "white American", "matt": "white American",
    "marcus": "Black American", "chuck": "Black American",
}

# ⭐ QUEM NARRA — um dos dois agentes do parque com narrador HOMEM.
# ⚠️ Com UM sexo so' a UI nao desenha botao nenhum, que e' o certo: botao que
# nao trava nada e' pior que botao nenhum.
SEXOS = ("homem",)

# ⭐⭐ OS DOIS MODOS, pelo CONTRATO COMPARTILHADO — `sc.ref_bela` e
# `sc.ref_forte`, nunca implementacao propria (duas implementacoes da mesma
# ideia divergem na primeira manutencao; e' a P9).
#
#   BELA  move IDADE + PORTE + TRAJE DELA, e o traje vem da variante `dela_bela`
#         da MESMA regiao ja' sorteada — nunca roupa generica de outro mundo,
#         que e' o modo de falha "REF de biquini de trico amish".
#         ⛔ A ETNIA DELA SOBREVIVE AO MODO: o `ref_bela` devolveria a etnia do
#         MOLDE (`MULHERES[0]`), e sem reimpor a sorteada o modo travaria a
#         mulher inteira em `white American` sem ninguem ver — a congruencia do
#         funil olha o HOMEM.
#   FORTE move IDADE + CABECA + MARCA + CORPO DELE. ⭐ E o toggle NASCE LIGADO
#         (`MODOS_DEFAULT`), ordem do operador de 2026-08-10.
#
# ⛔ APOSENTADO: `MODO_MUSCULOSO = True`, que vivia aqui. Era o mesmo conceito
# do MODO FORTE, com um nome que a UI nao conhece — o painel monta os toggles
# lendo `MODO_BELA` / `MODO_FORTE` (`ui_agente`, `self.modos`), entao a flag
# antiga era codigo escrito e inalcancavel: o operador nunca conseguiria
# liga-la. O corpo musculoso que ela prometia continua existindo sem toggle
# nenhum, no pool `CORPOS_H` (bracos grossos, veias no antebraco) — o que o
# MODO FORTE acrescenta e' o homem INTEIRO no registro forte.
MODO_BELA = True
MODO_FORTE = True

# ⭐⭐ 5o CONTRATO ADITIVO DA UI (2026-08-10): quais modos nascem LIGADOS no
# painel. Ordem do operador: *"toggle marcado como default"* para o FORTE.
# ⛔ Ate' hoje o `ui_agente` nascia com TODOS os modos desligados
# (`self.modo_on = {m: False ...}`). A UI agora le' `MODOS_DEFAULT` com
# `getattr(motor, "MODOS_DEFAULT", ())` — motor que nao declara nada continua
# nascendo desligado, e por isso nenhum dos outros 30+ motores muda de
# comportamento (provado, nao prometido: ver o relatorio de nao-regressao).
MODOS_DEFAULT = ("forte",)

# ⛔ A etnia sai da PAGINA (nao do mundo), entao o seletor clara/escura do painel
# funciona trocando de pagina — que e' o comportamento padrao. Declarar
# PELE_TRAVAVEL aqui acenderia um caminho que este motor nao usa.
PELE_TRAVAVEL = False

# ⭐ A FAIXA DO MODO FORTE. O pool compartilhado vai de 26 a 38 anos; aqui o
# piso e' 32 porque a fala e' de homem CASADO falando com homem casado (`if you
# have a wife`). Um de 26 continuaria crivel como corpo, nao como quem diz a
# frase. ⚠️ O `sc.ref_forte` CEDE se nada couber — botao que zera o sorteio e'
# botao que quebra o app.
FORTE_IDADE_MIN = 32


# ===========================================================================
# ⭐⭐ MUNDOS — 15 ARQUETIPOS AQUATICOS POR REGIAO DOS EUA
# ===========================================================================
# ⛔ Ordem do operador, 2026-08-09: *"sempre voltado pra piscina, jacuzzi, por
# favor, nicho de verao"*. Nao ha' mundo seco neste agente — e nao ha' banheira
# de banheiro: banheira nao e' nicho de verao.
# ⛔ Ordem do operador, 2026-08-10: pool de arquetipos POR REGIAO DOS EUA, com
# `etnias`, como no FALTA 16 e no BED 16. O funil e' US e o espectador tem de
# reconhecer o quintal como o da rua dele.
#
# ⭐ Cada entrada arrasta CENARIO + AGUA + BORDA + LUZ + AUDIO + TRAJE DELA,
# nunca so' o fundo — e' a mecanica de `variar etnia = arrastar o mundo`, aqui
# aplicada tambem ao corpo dele: e' a agua que autoriza o tronco nu.
#
# ⭐⭐ A `borda` E' EIXO DE CENA, NAO ENFEITE: e' onde a tigela fica apoiada nos
# DOIS takes e onde o sache cai no take 2. Sem ela cada mundo teria de repetir
# "the edge", e o gerador poria a tigela boiando.
#
# ⭐⭐ E cada entrada carrega o TRAJE DELA EM DOIS REGISTROS — `dela` (modo BELA
# desligado) e `dela_bela` (ligado). O par bela e' da MESMA regiao, so' que no
# registro do modo. ⛔ E ele para ANTES do extremo: a cena ja' e' dentro d'agua e
# o top da regiao ja' e' roupa de banho; o que o modo move e' o CORTE, nao a
# cobertura.
MUNDOS = [
    {"id": "apalache", "familia": "apalache", "regiao": "Apalaches",
     "cen": "a cedar-plank porch behind an Appalachian farmhouse, tall pines "
            "crowding the edge of the yard",
     "agua": "a round cedar hot tub set into the porch boards",
     "borda": "the wet cedar rim of the tub",
     "luz": "late afternoon sun coming in low and warm through the pines",
     "audio": "cicadas, water moving in the tub, a chainsaw far off",
     "dela": "a white bikini top", "dela_bela": "a white halter bikini top",
     "etnias": ["white American"]},

    {"id": "sulista", "familia": "sulista", "regiao": "Sul profundo",
     "cen": "the back yard of a Southern house, a plank fence and a magnolia "
            "over the far corner",
     "agua": "a round above-ground pool with a wooden deck built around it",
     "borda": "the wet deck boards at the pool wall",
     "luz": "warm late afternoon light coming flat across the yard",
     "audio": "cicadas, water lapping the pool wall, a screen door",
     "dela": "a coral bikini top", "dela_bela": "a coral halter bikini top",
     "etnias": ["Black American"]},

    {"id": "texas", "familia": "texas", "regiao": "Texas",
     "cen": "the back yard of a Texas ranch house, a plank fence and dry "
            "St. Augustine grass",
     "agua": "a rectangular concrete pool with a tiled lip",
     "borda": "the wet tiled lip of the pool",
     "luz": "hard late sun, short shadows across the water",
     "audio": "a window unit humming, water lapping the tile, far traffic",
     "dela": "a black bikini top", "dela_bela": "a black halter bikini top",
     "etnias": ["white American"]},

    {"id": "meio_oeste", "familia": "meio_oeste", "regiao": "Meio-Oeste",
     "cen": "the back deck of a Midwestern split-level, a chain-link fence and "
            "a maple behind it",
     "agua": "a square hot tub set into the deck boards with steam coming "
             "off the surface",
     "borda": "the wet deck boards at the edge of the tub",
     "luz": "cool overcast evening light with the steam catching it",
     "audio": "the tub jets, wind in the maple, a dog two yards over",
     "dela": "a navy bikini top", "dela_bela": "a navy halter bikini top",
     "etnias": ["white American"]},

    {"id": "nova_inglaterra", "familia": "nova_inglaterra",
     "regiao": "Nova Inglaterra",
     "cen": "the side yard of a New England colonial, hydrangeas along a low "
            "stone wall",
     "agua": "a cedar hot tub on a stone patio",
     "borda": "the wet stone coping beside the tub",
     "luz": "cool north light, soft and even off the water",
     "audio": "steam and jets, gulls, wind through the hydrangeas",
     "dela": "a white halter bikini top",
     "dela_bela": "a white twist-front bikini top",
     "etnias": ["white American"]},

    {"id": "harlem", "familia": "harlem", "regiao": "Harlem",
     # ⚠️ O BED 16 poe uma banheira de pe' de leao aqui, e la' faz sentido: o
     # take 2 dele e' dentro de casa. Aqui NAO — banheira nao e' nicho de verao,
     # e a ordem do operador e' piscina/jacuzzi. O telhado com piscina inflavel
     # e' o verao do brownstone.
     "cen": "the tar roof of a Harlem brownstone, water tanks and rooftops "
            "running off behind",
     "agua": "a round inflatable pool set up on the roof decking",
     "borda": "the wet plywood decking at the pool wall",
     "luz": "warm late city light coming in low across the roofs",
     "audio": "faint traffic below, water against the pool wall, a radio "
              "somewhere",
     "dela": "a black bikini top", "dela_bela": "a black twist-front bikini top",
     "etnias": ["Black American"]},

    {"id": "atlanta", "familia": "atlanta", "regiao": "Atlanta",
     "cen": "the back patio of an Atlanta house, tall pines past the fence",
     "agua": "a kidney-shaped pool with a raised spa spilling into it",
     "borda": "the wet stone coping of the pool",
     "luz": "bright filtered daylight, the water throwing light upward",
     "audio": "the spa spillover, birds in the pines, a quiet yard",
     "dela": "a gold bikini top", "dela_bela": "a gold halter bikini top",
     "etnias": ["Black American"]},

    {"id": "delta", "familia": "delta", "regiao": "Delta do Mississippi",
     "cen": "the back yard of a Mississippi Delta house, flat fields past a "
            "wire fence",
     "agua": "a round above-ground pool with a metal ladder on one side",
     "borda": "the wet metal rail of the pool wall",
     "luz": "flat evening light coming across the fields",
     "audio": "crickets, water against the pool wall, a truck far off",
     "dela": "a turquoise bikini top",
     "dela_bela": "a turquoise halter bikini top",
     "etnias": ["Black American"]},

    {"id": "gullah", "familia": "gullah", "regiao": "Lowcountry",
     "cen": "the back deck of a Lowcountry house, marsh grass and open water "
            "past the rail",
     "agua": "a wooden hot tub sunk into the deck",
     "borda": "the wet deck boards at the rim of the tub",
     "luz": "soft coastal light coming off the water",
     "audio": "water moving in the tub, marsh birds, wind",
     "dela": "a white bikini top",
     "dela_bela": "a white twist-front bikini top",
     "etnias": ["Black American"]},

    {"id": "noroeste", "familia": "noroeste", "regiao": "Noroeste do Pacifico",
     "cen": "the back deck of a Pacific Northwest house, wet firs crowding the "
            "rail",
     "agua": "a cedar hot tub on the deck with steam rising off it",
     "borda": "the wet cedar rim of the tub",
     # ⛔ NADA DE LUZ COLORIDA: o operador viu um lote e disse *"tire esse ar de
     # blade runner 2049, esta em tom esverdeado villeneuve"*. Foi neste mundo,
     # no FALTA 16, e o defeito era do motor PEDINDO verde — nao do gerador.
     "luz": "cool grey daylight coming through the trees",
     "audio": "steam and jets, rain in the firs, water dripping",
     "dela": "a dark green bikini top",
     "dela_bela": "a dark green halter bikini top",
     "etnias": ["white American"]},

    {"id": "grandes_lagos", "familia": "grandes_lagos",
     "regiao": "Grandes Lagos",
     "cen": "the end of a Great Lakes dock, birch along the shore behind",
     "agua": "a square hot tub set on the dock boards with heavy steam off "
             "the surface",
     "borda": "the wet dock boards at the edge of the tub",
     "luz": "pale afternoon light off the lake, the steam catching it",
     "audio": "the tub jets, water against the dock posts, a loon far off",
     "dela": "a red bikini top", "dela_bela": "a red halter bikini top",
     "etnias": ["white American"]},

    {"id": "creole", "familia": "creole", "regiao": "Nova Orleans",
     # ⚠️ `banana leaves` seria o cenario certo para um patio de Nova Orleans, e
     # esta' proibido: `banana` e' o proxy falico de tres motores do parque, e
     # deixar a palavra entrar pelo CENARIO e' abrir a porta pelos fundos.
     "cen": "the brick courtyard of a New Orleans house, broad tropical leaves "
            "hanging over the far wall",
     "agua": "a small tiled plunge pool set into the brick",
     "borda": "the wet tiled edge of the plunge pool",
     "luz": "heavy humid light coming over the courtyard wall",
     "audio": "water moving, cicadas, a streetcar far off",
     "dela": "an emerald bikini top",
     "dela_bela": "an emerald halter bikini top",
     "etnias": ["Black American"]},

    {"id": "italo_americana", "familia": "italo_americana",
     "regiao": "italo-americana",
     "cen": "the back yard of an Italian-American house, a tomato bed along "
            "the fence and a grape arbour over the path",
     "agua": "a round above-ground pool with a wooden deck at one end",
     "borda": "the wet wooden rail at the pool wall",
     "luz": "warm evening light coming in under the arbour",
     "audio": "water against the pool wall, a radio inside, cicadas",
     "dela": "a black halter bikini top",
     "dela_bela": "a black twist-front bikini top",
     "etnias": ["white American"]},

    {"id": "florida", "familia": "florida", "regiao": "Florida",
     "cen": "the screened lanai of a Florida house, palms standing behind the "
            "screen",
     "agua": "a rectangular pool with water spilling over the near edge",
     "borda": "the wet tiled edge of the pool",
     "luz": "bright overcast, soft even light off the water",
     "audio": "water spilling over the edge, a mockingbird, a pool pump",
     "dela": "a lime bikini top", "dela_bela": "a lime halter bikini top",
     "etnias": ["white American", "Black American"]},

    {"id": "americana", "familia": "americana", "regiao": "suburbio americano",
     "cen": "the back yard of a plain suburban house, a wooden fence and a "
            "swing set still standing",
     "agua": "a round above-ground pool with a blue liner",
     "borda": "the wet flat rail on top of the pool wall",
     "luz": "flat late afternoon light across the yard",
     "audio": "water against the pool wall, a lawnmower two streets over",
     "dela": "a pale blue bikini top",
     "dela_bela": "a pale blue halter bikini top",
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
# ⛔⛔ O CORPO E' O ARGUMENTO. Sem os bracos e as veias a fala vira promessa
# vazia — invariante medida 2/2 na fonte. E a ALIANCA importa: a fala e' *"se
# voce tem esposa"*.
# ⛔ CABECA e MARCA SEPARADAS (era um campo so'). Sao os dois campos que o
# `sc.ref_forte` sabe preencher, e sem a separacao o MODO FORTE entregaria um
# homem sem cabelo descrito — o helper devolve `cabeca` e `marca` em campos
# distintos, e campo que o molde nao pede ele nao devolve.
# ⛔ MARCA FACIAL OBRIGATORIA: ele aparece nos DOIS takes, com um corte no meio e
# uma mudanca de postura inteira. Sem ancora distintiva o Veo devolve OUTRO
# homem no take 2 — licao paga no VAZAMENTO.
HOMENS = [
    {"id": "grisalho_curto", "idade": 58,
     "cabeca": "close-cropped grey hair and a full grey beard",
     "marca": "a deep vertical crease between his eyebrows"},
    {"id": "careca_cavanhaque", "idade": 58,
     "cabeca": "a clean-shaven scalp and a short grey goatee",
     "marca": "a small dark mole high on his right cheek"},
    {"id": "grisalho_tempos", "idade": 58,
     "cabeca": "short salt-and-pepper hair and a trimmed grey beard",
     "marca": "a pale scar through his left eyebrow"},
    {"id": "barba_cheia", "idade": 58,
     "cabeca": "grey hair receding at the temples and a full white beard",
     "marca": "heavy folds under both eyes"},
    {"id": "bigode_grisalho", "idade": 58,
     "cabeca": "close-cropped grey hair and a thick grey moustache",
     "marca": "a broad flat nose broken once and never set"},
    {"id": "grisalho_ondulado", "idade": 58,
     "cabeca": "short wavy grey hair and a close grey beard",
     "marca": "a white patch of old sun damage on his left temple"},
]

# ⭐ O MOLDE do `sc.ref_forte`: ele so' devolve os campos que o molde PEDE.
# ⛔ Derivado do pool, nunca redigitado — molde escrito a mao e' a primeira
# coisa que diverge quando alguem acrescenta um campo em HOMENS.
MOLDE_H = dict(HOMENS[0], corpo="")

CORPOS_H = [
    "heavy through the shoulders, thick arms with the veins standing out on "
    "the forearms",
    "broad-chested and thick-armed, the veins showing along both forearms",
    "solid through the chest and shoulders, forearms corded and veined",
    "wide-shouldered with heavy upper arms and visible forearm veins",
    "thick through the neck and shoulders, heavy veined forearms",
    "densely built through the chest, the veins standing up on his arms",
]

# ===========================================================================
# A MULHER — ⭐ etnia SOLTA (ordem do operador). Ela e' MUDA.
# ===========================================================================
# ⛔ A LEI DO REF vale para ela: 25-35, sempre bonita, zero oculos, zero
# grisalho, zero pele castigada.
# ⛔ E ela e' MUDA. Invariante 2/2 na fonte, nao estilo.
# ⛔ IDADE e PORTE sao campos porque sao DUAS DAS TRES COISAS QUE O MODO BELA
# MOVE (a terceira e' o traje, que mora no mundo). Sem eles o toggle acenderia e
# a mulher em quadro seria a mesma — a forma-sem-funcao que este repo ja' pagou
# tres vezes.
MULHERES = [
    {"id": "loira_longa", "etnia": "white American", "idade": 29,
     "porte": "tall with a narrow waist",
     "cabeca": "long blonde hair, wet at the ends",
     "marca": "a small beauty spot above her lip"},
    {"id": "ruiva_ondulada", "etnia": "white American", "idade": 27,
     "porte": "slim and long-limbed",
     "cabeca": "wavy auburn hair pushed back wet",
     "marca": "a dense spray of freckles"},
    {"id": "morena_lisa", "etnia": "white American", "idade": 31,
     "porte": "athletic with square shoulders",
     "cabeca": "dark brown hair slicked back wet",
     "marca": "a small scar through one eyebrow"},
    {"id": "tranca_lateral", "etnia": "Black American", "idade": 28,
     "porte": "tall and softly curved",
     "cabeca": "long box braids gathered over one shoulder",
     "marca": "high cheekbones and a small mole on her cheek"},
    {"id": "cacheada_curta", "etnia": "Black American", "idade": 26,
     "porte": "strong-shouldered and lean",
     "cabeca": "a short wet curly afro",
     "marca": "a small gold nose stud"},
    {"id": "tranca_longa", "etnia": "Black American", "idade": 30,
     "porte": "curved with a small waist",
     "cabeca": "waist-length braids wet to the ends",
     "marca": "a beauty spot on her cheek"},
    {"id": "latina_ondulada", "etnia": "Latina American", "idade": 27,
     "porte": "petite with a narrow frame",
     "cabeca": "long wavy black hair wet at the ends",
     "marca": "a small mole by her eye"},
    {"id": "asiatica_lisa", "etnia": "Asian American", "idade": 32,
     "porte": "slim with rounded shoulders",
     "cabeca": "straight black hair slicked back wet",
     "marca": "a faint scar on her chin"},
]


# ===========================================================================
# ⭐⭐⭐ A TIGELA, A COLHER E O SACHE — o take 2 e' O PREPARO
# ===========================================================================
# ⛔ Leitura do print que o operador mandou (2026-08-10), elemento por elemento:
# tigela de ceramica apoiada na borda molhada, mistura amarelo-ambar dentro,
# colher de metal na mao dele, e o sache AMASSADO caido logo ao lado, com o
# rotulo legivel.
#
# ⭐ A TIGELA E' A MESMA NOS DOIS TAKES. No take 1 ela ja' esta' na borda,
# intocada; no take 2 ele esta' mexendo. E' a UNICA mudanca de estado do plano —
# a mesma funcao que o sache subindo tinha na versao antiga.
# ⚠️ CADA ENTRADA TEM SILHUETA E ACABAMENTO PROPRIOS. Licao do BOTICA: metade de
# um pool era de vidro e o gerador colapsou quatro entradas numa prensa
# francesa, a forma que ele conhece melhor. ⛔ E todas sao de CERAMICA/BARRO,
# porque e' o que o print mostra — variar o material seria inventar cena.
TIGELAS = [
    {"id": "creme_lisa", "curto": "ceramica creme",
     "img": "a heavy cream ceramic bowl of glossy amber gelatin mixture with a "
            "metal spoon standing in it"},
    {"id": "azul_esmalte", "curto": "ceramica azul",
     "img": "a deep blue-glazed ceramic bowl of glossy amber gelatin mixture "
            "with a metal spoon standing in it"},
    {"id": "barro_terracota", "curto": "terracota",
     "img": "a squat terracotta bowl of glossy amber gelatin mixture with a "
            "metal spoon standing in it"},
    {"id": "gres_pontilhado", "curto": "gres pontilhado",
     "img": "a speckled grey stoneware bowl of glossy amber gelatin mixture "
            "with a metal spoon standing in it"},
    {"id": "branca_alta", "curto": "louca branca",
     "img": "a tall white ironstone bowl of glossy amber gelatin mixture with "
            "a metal spoon standing in it"},
    {"id": "areia_larga", "curto": "barro areia",
     "img": "a wide sand-coloured earthenware bowl of glossy amber gelatin "
            "mixture with a metal spoon standing in it"},
]

# ⛔⛔ O ROTULO E' STRING TRAVADA E HERDADA — nao se redigita. Ordem do operador:
# *"seja fiel ao video original: aparecendo gelatin legivel e escrito"*, e o
# mercado e' os EUA, entao a palavra sai em INGLES.
# ⚠️ EXCECAO DECLARADA na trava `No on-screen text`: a palavra esta' no OBJETO,
# nao queimada na tela pelo gerador. A trava segue valendo para legenda, marca
# d'agua e texto de interface — e a lente GO4 cobra as duas coisas.
SACHE_ROTULO = ("a small foil sachet with the word GELATIN printed across the "
                "front in plain black letters")

# ⭐ O ESTADO NOVO DO SACHE (2026-08-10): ele saiu da MAO dele e passou a estar
# AMASSADO E VAZIO na borda, ao lado da tigela. E' o que o print mostra, e conta
# a mesma coisa sem ocupar a mao que agora segura a colher.
# ⛔ O LUGAR MORA NA FRASE DA MONTAGEM, NAO AQUI. A primeira versao punha
# `lying on the edge right beside the bowl` DENTRO da constante e a IMAGE 02 ja'
# abria com a mesma clausula — o prompt saia dizendo duas vezes onde o sache
# esta', na mesma sentenca. Achado LENDO o bloco renderizado, que e' a unica
# lente que pega redundancia (o linter cobra presenca, nao ritmo).
SACHE = ("%s, empty and crumpled, with the lettering face up and readable"
         % SACHE_ROTULO)


# ===========================================================================
# ⭐⭐ A COPY — o arco medido nos CINCO reels, quase palavra por palavra
# ===========================================================================
# ⛔⛔ A FALA E' SOBRE O CORPO, NUNCA SOBRE O ORGAO. A fonte diz `your body
# harder and stronger` — e essa e' a razao pela qual este angulo e' mais seguro
# que os outros na moderacao. Verbo que descreve o orgao voltando a funcionar e'
# lido como tumescencia; o COLO 16 pagou ~95% de recusa por isso em 2026-08-09.
# ⛔ Nao introduzir `{o}` nesta copy. Nao e' esquecimento, e' a defesa.

# ---------------------------------------------------------------------------
# cena 1 = AVISO + A ESPOSA + ELA NAO AGUENTA   ⛔ NAO FOI TOCADA EM 2026-08-10
# ---------------------------------------------------------------------------
# ⚠️ CT2 do CONTRATO-COPY-16S: este take nao enuncia FALHA — ele e' AVISO DE
# EXCESSO, que e' o oposto. O proprio contrato declara a excecao nominalmente
# (*"ha' angulos cuja cena 1 e' aviso de excesso, nao falha (o GOOD 16)"*), e a
# regra que sobra e' esta: quem nao enuncia falha TEM DE SABER que nao enuncia.
# ⛔ Por isso o CT2 e' filtrado no `lint` deste motor, e SO' o CT2 — ver
# `_go11_contrato16`.
AVISOS = [
    "If you are single, stay away from this.",
    "If you are single, do not try this.",
    "If you are single, this is not for you.",
    "If you are single, do not touch this.",
    "If you are single, skip this one.",
    "Single men, this is not for you.",
]

ESPOSAS = [
    "And if you have a wife, be very careful.",
    "If you are married, be very careful with this.",
    "If you are married, use it carefully.",
    "If you are married, thank me later.",
    "If you have a wife, go easy with it.",
    "Married men, use this with caution.",
]

# ⛔ E' o beat que faz o video existir: a promessa vem da MULHER nao dar conta,
# nao de uma afirmacao sobre o corpo do espectador.
AGUENTAM = [
    "She will not handle you.",
    "She will not be able to keep up.",
    "She will not keep up with you.",
    "Your wife will not keep up.",
    "She is not going to keep up.",
]

# ---------------------------------------------------------------------------
# ⭐⭐ cena 2 = A MISTURA + O PRECO + O CTA
# ---------------------------------------------------------------------------
# ⛔⛔ ORDEM DO OPERADOR, 2026-08-10: *"copy tem que ser taxativa se referindo a
# MISTURA da receita"*. Ate' ontem a fala falava do CORPO e nunca dizia de ONDE
# vinha o efeito — o quadro mostrava um sache erguido e a fala dizia `This
# leaves your body harder`, com um `This` sem dono. Agora a sentenca NOMEIA o
# que esta' na tigela e o que aquilo faz.
#
# ⛔ SEM PRONOME SEM DONO. `This`, `that` e `it` sozinhos apontando para a
# tigela sairam: toda entrada carrega o designador explicito (`the gelatin trick
# in this bowl`, `one bowl of the gelatin trick`).
#
# ⛔⛔ E ISSO NAO FURA O CT5 — a diferenca e' medivel e esta' medida no
# autoteste: o que se proibe e' listar INGREDIENTE (`pomegranate`, `collagen`,
# `honey`...), porque a receita e' a UNICA moeda que o comentario compra e
# entregue uma vez ela esta' gasta para os outros 49 videos da pagina. O que
# estas entradas nomeiam e' a MISTURA — e o nome dela e' a KEYWORD do funil, que
# tem de ser dita. `INGREDIENTES_16` do `short_comum` nao conhece `gelatin`
# justamente por isso.
#
# ⛔ CT3: toda entrada carrega o literal `gelatin trick` COM verbo de efeito e
# alvo na MESMA sentenca (`makes ... your body`). Nome de mecanismo sem razao ao
# lado nao vira crenca, vira ruido de marca.
# ⛔ GO1: nenhuma nomeia o orgao. O alvo e' o CORPO — e' o que faz este angulo
# passar no gerador.
# ⚠️ 11 a 12 palavras, e o teto de 12 e' ARITMETICA, nao gosto: com o menor CTA
# (9) e o menor PRECO (3) uma entrada de 13 caberia so' na melhor combinacao e
# nunca seria sorteada nas outras. Entrada que quase nunca cabe nao e' rara: e'
# morta, e o [ALCANCE] a contaria como opcao viva (licao §36).
MISTURAS = [
    "The gelatin trick in this bowl makes your body harder and stronger.",
    "The gelatin trick in this bowl makes your body stronger every night.",
    "The gelatin trick in this bowl puts blood back in your body.",
    "The gelatin trick in this bowl brings your body back to strength.",
    "The gelatin trick I mix in this bowl makes your body harder.",
    "One bowl of the gelatin trick a night makes your body harder.",
    "One bowl of the gelatin trick a night keeps your body strong.",
    "One bowl of the gelatin trick nightly makes your body stronger.",
]

# ⚠️ O beat mais dispensavel dos tres, e o unico que nao carrega promessa nem
# comando — por isso e' ele que absorve a sobra do orcamento.
# ⛔ SAIU `And it costs almost nothing.`: `it` sem dono e' exatamente o que a
# ordem de 2026-08-10 proibe, e a entrada custava 5 palavras para dizer o que as
# outras dizem em 3.
PRECOS = [
    "Costs almost nothing.",
    "Costs next to nothing.",
    "Costs pocket change.",
    "The price is nothing.",
]

# ⛔⛔ A fonte pede `recipe`. NAO COPIAMOS o comando: a automacao de DM casa
# palavra EXATA e o funil inteiro roda em `gelatin`. O literal vem de
# `sc.CTA_LITERAL`, nunca redigitado — e a VIRGULA depois de `gelatin` e'
# intocavel (a legenda nasce do Whisper em cima do audio, e sem a micro-pausa o
# Veo emenda e narra `gelatine`).
# ⭐⭐ TODA ENTRADA DIZ ONDE A RECEITA CHEGA (CT6). O KPI e' uma confissao
# publica — o comentario leva nome e foto e vai para o feed da esposa dele —, e
# a clausula de entrega e' de graca: mesmas 9 palavras, e paga o endereco, a
# privacidade e o fato de nao ser na tela publica.
# ⛔ CT1: nada vem depois desta sentenca. Ela e' a ultima coisa no ouvido.
CTAS = [
    "%s and the recipe goes to your messages." % sc.CTA_LITERAL,
    "%s and the recipe lands in your messages." % sc.CTA_LITERAL,
    "%s and the recipe hits your inbox tonight." % sc.CTA_LITERAL,
    "%s and I'll send the recipe by message." % sc.CTA_LITERAL,
    "%s and the recipe comes to your inbox." % sc.CTA_LITERAL,
    "%s and I'll send the recipe in private." % sc.CTA_LITERAL,
    "%s and only your messages get the recipe." % sc.CTA_LITERAL,
    "%s and your inbox gets the recipe tonight." % sc.CTA_LITERAL,
    "%s and the whole recipe goes to your messages." % sc.CTA_LITERAL,
    "%s and I'll send the whole recipe by message." % sc.CTA_LITERAL,
]

# ⛔⛔ AQUI MORAVA O POOL `FOLLOWS` (6 entradas). Ele saiu inteiro pelo CT8 do
# CONTRATO-COPY-16S — ordem do operador, 2026-08-10: *"eu tb nao acho que deva
# ter que ter follow me no cta, a mensagem e' enviada independente de seguirem
# ou nao"*. Nao e' gosto: a premissa de que a automacao de DM so' alcancava
# seguidor era FALSA, e quem opera a automacao corrigiu.
# ⭐ E era ele, colado DEPOIS do CTA, que fazia este motor violar o CT1 em 100%
# dos sorteios — o defeito mais caro do lote antigo. As 3-6 palavras liberadas
# foram para a MISTURA, que passou de 8-10 para 11-12.
# ⚠️ Se o follow voltar, volta ANTES do CTA e por decisao do operador.


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


EIXOS_LEDGER = ("mundo", "homem", "mulher", "tigela")


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
    levanta TypeError dentro do callback do tkinter — que morre CALADO."""
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


def _por_id(pool, valor, chave="id"):
    """A entrada do pool, aceitando ID (string) OU a ENTRADA JA' RESOLVIDA.

    ⛔⛔ OS DOIS FORMATOS SAO OBRIGATORIOS, e o segundo e' o que o PAINEL manda.
    O `ui_agente.travas()` diz na propria docstring: *"o cadeado devolve o VALOR
    QUE ESTA' NA TELA (`self.spec[chave]`), nao um id"* — ou seja, o DICIONARIO
    inteiro. A versao ingenua (`x["id"] == valor`) nunca casa com um dicionario,
    devolvia `None`, e o `resumo_pt` estourava
    `TypeError: 'NoneType' object is not subscriptable` DENTRO do callback do
    tkinter: bastava o operador clicar TRAVAR num dos quatro eixos e SORTEAR.
    ⚠️ Medido nos QUATRO cadeados deste painel (mundo, homem, mulher, tigela) —
    os quatro quebravam. Bug LATENTE, anterior a' passada de 2026-08-10: a
    linha vem intacta do HEAD, e so' apareceu porque o app foi EXERCITADO em vez
    de apenas aberto. O `falta16_short` — o motor de quem este copiou os MUNDOS
    — ja' trazia esta forma; o `bed16_short` ainda tem a ingenua.
    ⚠️ E o fallback CEDE (`pool[0]`) em vez de devolver `None`: id desconhecido
    vindo de um ledger velho nao pode derrubar o sorteio.
    """
    if isinstance(valor, str):
        return next((x for x in pool if x.get(chave) == valor), pool[0])
    return valor


def _cabe(pool, reserva, cena):
    """As entradas que cabem depois de reservar `reserva` palavras.

    ⚠️ O fallback nao devolve o pool inteiro — isso e' estouro silencioso.
    Devolve a entrada mais CURTA, e quem reclama e' o linter.
    """
    v = [x for x in pool if _palavras(x) + reserva <= TETO_FALA[cena]]
    return v or [min(pool, key=_palavras)]


def _rsv(vals):
    v = sorted(vals)
    return v[len(v) // 2]


def _mn(pool):
    return min(_palavras(x) for x in pool)


# ===========================================================================
# SORTEIO
# ===========================================================================

def _falas(spec, rng, quais=(0, 1)):
    """As duas falas.

    ⛔⛔ QUEM ESCOLHE PRIMEIRO RESERVA O MINIMO; QUEM ESCOLHE NO MEIO RESERVA A
    MEDIANA. Regra medida no ESCANDALO 16, dos dois defeitos opostos: com o
    minimo em todos o ULTIMO beat fica preso; com a mediana em todos o
    PRIMEIRO fica preso.
    """
    f = dict(enumerate(spec.get("falas", ["", ""])))

    if 0 in quais:
        av = rng.choice(_cabe(AVISOS, _mn(ESPOSAS) + _mn(AGUENTAM), 1))
        es = rng.choice(_cabe(ESPOSAS,
                              _palavras(av)
                              + _rsv([_palavras(x) for x in AGUENTAM]), 1))
        ag = rng.choice(_cabe(AGUENTAM, _palavras(av) + _palavras(es), 1))
        f[0] = "%s %s %s" % (av, es, ag)

    if 1 in quais:
        # ⛔ O CTA escolhe PRIMEIRO: ele carrega o literal `Comment gelatin,` e o
        # endereco da entrega, e nao se encurta. O PRECO e' o beat mais
        # intercambiavel e vai por ULTIMO, absorvendo a sobra.
        ct = rng.choice(_cabe(CTAS, _mn(MISTURAS) + _mn(PRECOS), 2))
        mi = rng.choice(_cabe(MISTURAS,
                              _palavras(ct)
                              + _rsv([_palavras(x) for x in PRECOS]), 2))
        pr = rng.choice(_cabe(PRECOS, _palavras(ct) + _palavras(mi), 2))
        f[1] = "%s %s %s" % (mi, pr, ct)

    return f


def sortear(pagina, rng, ledger, travas=None):
    travas = travas or {}
    hist = (ledger or {}).get(pagina, {})
    etnia = ETNIA.get(pagina, "white American")

    # ⛔ O MUNDO E' FILTRADO PELA ETNIA DA PAGINA (mecanica do FALTA 16 / BED
    # 16). A congruencia do funil nao e' so' do rosto: um homem branco num
    # telhado de brownstone do Harlem quebra a leitura tanto quanto trocar o
    # rosto — e' a doutrina `variar etnia e' arrastar o mundo inteiro`.
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

    # ⭐⭐ MODO FORTE — contrato compartilhado (`sc.ref_forte`), nao
    # implementacao propria. O helper devolve o homem no FORMATO DESTE pool
    # (`id`, `idade`, `cabeca`, `marca`, `corpo`), entao o `montar()` nao ganha
    # um `if`.
    # ⛔ O CADEADO DA TELA VENCE O MODO: homem travado no painel e' mais
    # especifico que "um forte qualquer" — mesma precedencia que o `ui_agente`
    # ja' aplica com `ref`, e que aqui precisa ser respeitada na mao porque o
    # eixo se chama `homem`.
    forte = bool(travas.get("forte")) and not travas.get("homem")
    if forte:
        homem = sc.ref_forte(MOLDE_H, rng, idade_min=FORTE_IDADE_MIN)

    # ⭐⭐ MODO BELA — o espelho exato, do outro lado.
    # ⛔ E A ETNIA DELA SOBREVIVE AO MODO: o `ref_bela` mantem o campo que nao
    # conhece, e o campo que ele mantem e' o do MOLDE (`MULHERES[0]`), nao o da
    # entrada sorteada. Sem esta linha o modo travaria a mulher inteira em
    # `white American` e ninguem veria, porque a congruencia do funil olha o
    # HOMEM.
    bela = bool(travas.get("bela")) and not travas.get("mulher")
    if bela:
        _et_dela = mulher["etnia"]
        mulher = sc.ref_bela(MULHERES[0], rng)
        mulher["etnia"] = _et_dela

    tigela = (_por_id(TIGELAS, travas["tigela"]) if travas.get("tigela")
              else _fresco(TIGELAS, hist.get("tigela", [])[-3:], rng))

    spec = {
        "pagina": pagina, "etnia": etnia, "bela": bela, "forte": forte,
        "mundo": mundo, "homem": homem, "mulher": mulher, "tigela": tigela,
        # ⭐ Com o MODO FORTE ligado o corpo vem DO HELPER, junto do rosto e da
        # idade: sortear um corpo do pool velho por cima do homem forte seria
        # colar um tronco de 58 anos num rosto de 34.
        "corpo_h": homem.get("corpo") or rng.choice(CORPOS_H),
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

# ⛔ ANTICELEB — nunca INVENTAR declaracao de conformidade ("not a celebrity" e'
# municao). ⚠️ Esta frase existe porque o BLOCO 0 do repo inteiro a carrega e o
# gerador a espera; o que se proibe e' escrever uma nova.
# ⭐ Com o MODO FORTE ligado ela vira `sc.ANTICELEB_FORTE`: dizer "powerfully
# built" no corpo e "plain unremarkable face" no rosto na mesma frase e' a
# contradicao que o CLEAN ja' pagou — o gerador recebe as duas e resolve contra
# nos.
ANTICELEB = ("An ordinary everyday relatable person with a plain unremarkable "
             "face, not a celebrity, not a model, not an actor.")


def _traje_dela(spec):
    """A roupa dela, ja' resolvida pelo MODO BELA.

    ⛔ Um lugar so'. Espalhar `if spec["bela"]` pelos dois blocos e' o fragmento
    espelhado que diverge na primeira manutencao.
    """
    m = spec["mundo"]
    return m["dela_bela"] if spec.get("bela") else m["dela"]


def montar(spec):
    m, h, w = spec["mundo"], spec["homem"], spec["mulher"]
    et = spec["etnia"]
    b = {}

    # --- BLOCO 0 — a REF e' o HOMEM (ele e' quem fala) ---------------------
    # ⛔ Neste angulo a congruencia de etnia governa ELE, nao ela.
    b["BLOCO 0 (REF)"] = (
        "REF 01: Photo of a real person, a %d-year-old %s man, chest up, "
        "facing the camera directly, calm steady expression. %s, %s, %s, "
        "wearing a gold wedding band. %s Hands out of frame, no objects. Plain "
        "neutral gray background, soft even frontal light. Slight sensor "
        "grain, soft focus, raw iPhone front camera aesthetic. No subtitles, "
        "no captions, no burned-in text, no watermark."
        % (h["idade"], et, _cap(h["cabeca"]), h["marca"], spec["corpo_h"],
           sc.ANTICELEB_FORTE if spec.get("forte") else ANTICELEB))

    # --- IMAGE 01 — O AVISO -----------------------------------------------
    # ⭐ A TIGELA JA' ESTA' EM CENA, INTOCADA. E' o unico ajuste que o take 1
    # sofreu em 2026-08-10, e ele e' de CONTINUIDADE: sem a tigela aqui, o take
    # 2 introduziria tigela, colher e sache de uma vez e o corte leria como dois
    # videos colados.
    # ⛔ O SACHE NAO ENTRA AQUI (lente GO4): ele e' a mudanca de estado do plano.
    # ⚠️ `submerged to his chest` e' FORMA, nao cena — a agua continua no peito
    # dele. E' licao paga no BED 16: `with the water at his chest` encadeia dois
    # `with` no mesmo substantivo nos mundos cujo `agua` ja' tem um (`a pool
    # WITH a tiled lip WITH the water at his chest`), e `, the water at his
    # chest` repete `the water` nos que descrevem a agua se movendo. Esta
    # redacao nao usa nem `with` nem `water`, e por isso e' a unica que le'
    # limpo nos QUINZE — conferido um por um.
    b["IMAGE 01/02"] = (
        "IMAGE 01/02: Medium shot at %s. Sitting in %s, submerged to his "
        "chest, shoulders and arms out of the water, is a %d-year-old %s man, "
        "bare-chested, %s, %s, %s, a gold wedding band on his hand, talking "
        "straight to camera. His hands are empty and rest on the edge in front "
        "of him, and on %s, in front of him and untouched, sits %s. Beside "
        "him, leaning in against his shoulder with the water at her chest, is "
        "a %d-year-old %s woman, %s, %s, %s, wearing %s; she looks at the lens "
        "and says nothing. They are the only two people in the frame. %s. %s"
        % (m["cen"], m["agua"], h["idade"], et, h["cabeca"], h["marca"],
           spec["corpo_h"], m["borda"], spec["tigela"]["img"],
           w["idade"], w["etnia"], w["cabeca"], w["marca"], w["porte"],
           _traje_dela(spec), _cap(m["luz"]), CAUDA))

    # --- IMAGE 02 — O PREPARO ---------------------------------------------
    # ⛔⛔ A ANCORA DE CONTINUIDADE VEM EM CINCO PECAS: idade, etnia, cabeca,
    # marca e a frase `It is the same man`. Sem isso o Veo desenha OUTRA pessoa
    # — no VAZAMENTO o corpo-prova voltou como um senhor de oculos e bigode, e
    # como o TAKE diz `Only he speaks`, o ESTRANHO falava a fala do REF.
    # ⚠️ A postura vem do print: de pe', agua na cintura, inclinado sobre a
    # borda, MEXENDO e SORRINDO. O rosto virado para a lente e' a resolucao da
    # PENDENCIA declarada no cabecalho — ele e' o narrador e precisa falar.
    b["IMAGE 02/02"] = (
        "IMAGE 02/02: Medium shot at %s. Standing in %s, submerged to his "
        "waist and leaning forward over %s, is the same %d-year-old %s man "
        "from the first scene, bare-chested, %s, %s, %s, a gold wedding band "
        "on his hand, his face turned to the camera and smiling. It is the "
        "same man, not a different person. On the edge in front of him sits "
        "%s, and he is stirring it with the spoon. Right beside the bowl, on "
        "the same edge, lies %s. Pressed against his side with her shoulder "
        "against his arm is a %d-year-old %s woman, %s, %s, %s, wearing %s; "
        "she is looking down at the bowl and says nothing. They are the only "
        "two people in the frame. %s. %s"
        % (m["cen"], m["agua"], m["borda"], h["idade"], et, h["cabeca"],
           h["marca"], spec["corpo_h"], spec["tigela"]["img"], SACHE,
           w["idade"], w["etnia"], w["cabeca"], w["marca"], w["porte"],
           _traje_dela(spec), _cap(m["luz"]), CAUDA))

    # --- OS TAKES ----------------------------------------------------------
    # ⛔ `Only he speaks` e `she never speaks` sao OBRIGATORIOS (lente GO2):
    # omitir nao basta, o Veo poe as duas bocas a mexer se ninguem proibir e o
    # dialogo sai monofonico e torto.
    b["TAKE 01/02"] = (
        "TAKE 01/02: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway, no cuts, and the camera does not move. He "
        "talks straight into the lens the whole time and his hands stay where "
        "they are. The bowl on the edge is not touched, moved or lifted. She "
        "stays exactly where she is, leaning against his shoulder, and she "
        "never speaks. Only he speaks. The water keeps moving the way water "
        "moves and nothing else in the frame changes.\n"
        "Dialogue: \"%s\"\nAudio: %s. No music."
        % (sonorizar(spec["falas"][0]), m["audio"]))

    b["TAKE 02/02"] = (
        "TAKE 02/02: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway, no cuts, and the camera does not move. He "
        "talks straight into the lens the whole time and it is the same man as "
        "in the first scene. He keeps stirring the bowl with the spoon for the "
        "whole shot, the bowl stays exactly where it is on the edge, and the "
        "lettering on the sachet beside it stays sharp and readable. She stays "
        "pressed against his side looking down at the bowl, and she never "
        "speaks. Only he speaks. The water keeps moving the way water moves "
        "and nothing else in the frame changes.\n"
        "Dialogue: \"%s\"\nAudio: %s. No music."
        % (sonorizar(spec["falas"][1]), m["audio"]))

    return sc.selar_takes(b)


# ===========================================================================
# LINTER — as regras GO
# ===========================================================================
# ⛔ APOSENTADA: a lente `GO3` (`no face is in the frame` + nenhuma mulher no
# enquadramento `so as maos`). O enquadramento inteiro saiu por ordem do
# operador em 2026-08-10 — lente que cobra cena que nao existe reprova a
# producao certa (modo de falha §16). O numero nao foi reciclado: GO3 fica
# vago de proposito, para quem procurar por ele no historico achar este aviso.


def _go1_corpo_nao_orgao(spec, blocos, achados):
    """⭐⭐ GO1 — A FALA E' SOBRE O CORPO, NUNCA SOBRE O ORGAO.

    ⛔ E' a defesa central deste angulo. O COLO 16 mediu ~95% de recusa no Veo
    em 2026-08-09 porque a fala nomeava o orgao junto de um verbo de ereccao —
    o classificador le' isso como tumescencia. A fonte deste angulo fala de
    `your body harder and stronger`, e e' por isso que ela passa.
    ⚠️ A lente existe para impedir que alguem "melhore" a copy no futuro
    trazendo o orgao para ca.
    """
    corpo = " ".join(spec["falas"]).lower()
    for n in NUCLEO:
        if n.lower() in corpo:
            achados.append((
                "ERRO",
                "GO1: a fala nomeia o orgao (%r) — este angulo fala do CORPO "
                "(`harder and stronger`), e e' isso que o faz passar na "
                "moderacao onde os outros reprovam" % n))


def _go2_ela_muda(spec, blocos, achados):
    """GO2 — ela nunca fala, e os DOIS takes tem de DIZER isso."""
    for k in ("TAKE 01/02", "TAKE 02/02"):
        if "Only he speaks" not in blocos[k]:
            achados.append(("ERRO", "GO2: %s sem `Only he speaks` — sem isso "
                                    "o Veo mexe a boca dela tambem" % k))
        if "she never speaks" not in blocos[k]:
            achados.append(("ERRO", "GO2: %s nao diz que ela e' muda — a mudez "
                                    "dela e' invariante do angulo" % k))


def _go4_sache(spec, blocos, achados):
    """GO4 — o sache com GELATIN legivel aparece na cena 2, nunca na 1.

    ⛔ Ele e' a mudanca de estado do plano: no take 1 a tigela esta' intocada na
    borda; no take 2 ele ja' foi usado, amassado, e esta' caido AO LADO dela. Se
    aparecer na cena 1, o video perde a batida que a fonte tem.
    ⭐ E a lente cobra o LUGAR, nao so' a presenca: sache erguido na mao era a
    cena antiga, e a mao agora segura a colher.
    """
    if "GELATIN" in blocos["IMAGE 01/02"]:
        achados.append(("ERRO", "GO4: o sache ja' aparece na cena 1 — ele e' a "
                                "unica mudanca de estado do plano e entra na 2"))
    i2 = blocos["IMAGE 02/02"]
    if "GELATIN" not in i2:
        achados.append(("ERRO", "GO4: a cena 2 nao tem o sache com GELATIN "
                                "legivel — ordem do operador, fiel a' fonte"))
    # ⚠️ `lower()`: a clausula abre a sentenca na montagem (`Right beside the
    # bowl, ...`), e lente que casa caixa alta e' lente que reprova a producao
    # certa no dia em que alguem reordena a frase.
    if "beside the bowl" not in i2.lower():
        achados.append(("ERRO", "GO4: o sache da cena 2 nao esta' AO LADO DA "
                                "TIGELA — e' o que o print mostra, e a mao dele "
                                "agora segura a colher"))
    if "crumpled" not in i2:
        achados.append(("ERRO", "GO4: o sache da cena 2 nao esta' amassado — "
                                "sache intacto nao conta que a mistura ja' foi "
                                "feita"))


def _go5_orcamento(spec, blocos, achados):
    for i, fala in enumerate(spec["falas"], 1):
        n = _palavras(fala)
        if n > TETO_FALA[i]:
            achados.append(("ERRO", "GO5: cena %d com %d palavras (teto %d) — "
                                    "a fala e' cortada no render"
                            % (i, n, TETO_FALA[i])))
        if n < PISO_FALA[i]:
            achados.append(("AVISO", "GO5: cena %d com %d palavras (piso %d) — "
                                     "sobra ar morto no take"
                            % (i, n, PISO_FALA[i])))


def _go6_etnia(spec, blocos, achados):
    """GO6 — a congruencia governa O HOMEM, que e' quem fala.

    ⭐ E cobra tambem o MUNDO: a etnia da pagina tem de caber no arquetipo
    regional sorteado. Congruencia que so' olha o rosto deixa o homem branco num
    telhado do Harlem, e a leitura quebra do mesmo jeito.
    """
    et = spec["etnia"]
    for k in ("BLOCO 0 (REF)", "IMAGE 01/02", "IMAGE 02/02"):
        if et not in blocos[k]:
            achados.append(("ERRO", "GO6: %s sem a etnia da pagina (%r) — a "
                                    "congruencia com o avatar sai do video "
                                    "sem ninguem ver" % (k, et)))
    if et not in spec["mundo"]["etnias"]:
        achados.append(("ERRO", "GO6: o mundo %r nao comporta a etnia da "
                                "pagina (%r) — o arquetipo regional arrasta o "
                                "quintal inteiro, nao so' o fundo"
                        % (spec["mundo"]["id"], et)))


def _go7_ancora(spec, blocos, achados):
    """⛔⛔ GO7 — A ANCORA DE CONTINUIDADE DO HOMEM NO TAKE 2.

    Ate' 2026-08-10 os dois takes eram o MESMO quadro e a ancora era de graca.
    Agora ele muda de postura (sentado -> de pe', inclinado sobre a borda), e
    mudanca de postura com corte no meio e' exatamente onde o Veo troca de
    pessoa. Licao paga no VAZAMENTO: o corpo-prova voltou como um senhor de
    oculos e bigode, e como o TAKE diz `Only he speaks`, o ESTRANHO falava a
    fala do REF.
    ⚠️ Cinco pecas, e nenhuma sozinha basta.
    """
    h = spec["homem"]
    i2, t2 = blocos["IMAGE 02/02"], blocos["TAKE 02/02"]
    if "the same %d-year-old" % h["idade"] not in i2:
        achados.append(("ERRO", "GO7: a IMAGE 02 nao repete `the same "
                                "%d-year-old` — o Veo troca de pessoa"
                        % h["idade"]))
    for peca, rot in ((h["cabeca"], "cabeca"), (h["marca"], "marca")):
        if peca not in i2:
            achados.append(("ERRO", "GO7: a IMAGE 02 nao repete o %s sorteado "
                                    "(%r) — e' a ancora que o Veo usa para nao "
                                    "trocar de homem" % (rot, peca[:38])))
    if "It is the same man" not in i2:
        achados.append(("ERRO", "GO7: a IMAGE 02 nao diz `It is the same man` "
                                "— a ancora implicita nao segura mudanca de "
                                "postura com corte no meio"))
    if "the same man as in the first scene" not in t2:
        achados.append(("ERRO", "GO7: o TAKE 02 nao repete a ancora — a IMAGE "
                                "segura o primeiro frame, o TAKE segura os 8 "
                                "segundos"))


def _go8_tigela(spec, blocos, achados):
    """⭐⭐ GO8 — A TIGELA E' O FIO, E A COLHER E' O QUE FAZ DELA UM PREPARO.

    ⛔ Ordem do operador (print de 2026-08-10): tigela de ceramica apoiada na
    borda molhada, mistura ambar dentro, colher de metal, e ele MEXENDO. A lente
    cobra as quatro pontas: a tigela sorteada nos DOIS blocos, a borda como
    apoio, o `untouched` do take 1 e o `stirring` do take 2.
    ⚠️ Sem o `untouched` no take 1 o gerador comeca a mexer oito segundos antes
    da hora, e a unica mudanca de estado do plano desaparece.
    """
    tg, m = spec["tigela"], spec["mundo"]
    i1, i2 = blocos["IMAGE 01/02"], blocos["IMAGE 02/02"]
    t1, t2 = blocos["TAKE 01/02"], blocos["TAKE 02/02"]
    for k, bl in (("IMAGE 01/02", i1), ("IMAGE 02/02", i2)):
        if tg["img"] not in bl:
            achados.append(("ERRO", "GO8: a tigela sorteada (%r) nao chega a' "
                                    "%s — eixo de painel que nao muda o video"
                            % (tg["id"], k)))
        if m["borda"] not in bl:
            achados.append(("ERRO", "GO8: %s nao apoia nada em %r — sem a borda "
                                    "sorteada o gerador poe a tigela boiando"
                            % (k, m["borda"][:34])))
    if "untouched" not in i1 or "is not touched, moved or lifted" not in t1:
        achados.append(("ERRO", "GO8: a cena 1 nao trava a tigela como "
                                "INTOCADA — o preparo e' a mudanca de estado, e "
                                "sem a trava ele comeca cedo demais"))
    if "he is stirring it with the spoon" not in i2:
        achados.append(("ERRO", "GO8: a IMAGE 02 nao poe ele MEXENDO com a "
                                "colher — e' o que o print mostra e e' o que a "
                                "fala do take 2 nomeia"))
    if "keeps stirring the bowl with the spoon" not in t2:
        achados.append(("ERRO", "GO8: o TAKE 02 nao segura o gesto pelos 8 "
                                "segundos — a IMAGE segura o primeiro frame"))


# ⭐⭐ GO9 — OS DESIGNADORES DA MISTURA. Ordem do operador, 2026-08-10: *"copy
# tem que ser taxativa se referindo a MISTURA da receita"*.
# ⛔ A lente e' de FUNCAO, nao de forma: nao basta a fala ter mudado, ela tem de
# NOMEAR o que esta' na tigela. Sao as duas formas que os pools usam.
_MISTURA_NOMEADA = re.compile(
    r"\b(the gelatin trick in this bowl|the gelatin trick I mix in this bowl|"
    r"one bowl of the gelatin trick)\b", re.I)
# ⛔ E o outro lado da mesma ordem: pronome sem dono. `This leaves your body
# harder` era a copy de ontem — o `This` apontava para um sache que o
# espectador via meio segundo antes, e num video de 16s com corte no meio isso
# nao resolve. A lente cobra SUJEITO NU no comeco da sentenca, que e' onde o
# defeito morava.
_PRONOME_NU = re.compile(r"(?:^|(?<=[.!?])\s+)(this|that|it)\s+(?!bowl\b|"
                         r"mix\b|trick\b)[a-z]", re.I)


def _go9_mistura(spec, blocos, achados):
    fala = spec["falas"][1]
    if not _MISTURA_NOMEADA.search(fala):
        achados.append(("ERRO", "GO9: o take 2 nao NOMEIA a mistura — a ordem "
                                "do operador e' copy taxativa sobre o que esta' "
                                "na tigela, e sem o designador a fala volta a "
                                "vender um efeito sem causa"))
    m = _PRONOME_NU.search(fala)
    if m:
        achados.append(("ERRO", "GO9: o take 2 abre uma sentenca com pronome "
                                "sem dono (%r) — o corte zera a memoria de "
                                "trabalho e o deitico aponta para o vazio"
                        % m.group(0).strip()))
    # ⛔ CT5 do contrato, cobrado tambem aqui e de dentro: a diferenca entre
    # NOMEAR A MISTURA e ENTREGAR A RECEITA e' o funil inteiro.
    ing = sc.INGREDIENTES_16.search(fala)
    if ing:
        achados.append(("ERRO", "GO9: o take 2 nomeia o ingrediente %r — a "
                                "mistura se nomeia, a receita nao se entrega"
                        % ing.group(0)))


def _go10_modos(spec, blocos, achados):
    """⭐⭐ GO10 — OS DOIS TOGGLES TEM DE MUDAR O QUADRO, NOS QUATRO ESTADOS.

    ⛔ E' a lente contra a FORMA-SEM-FUNCAO, que este repo ja' pagou tres vezes:
    botao aceso, sorteio igual. Ela cobra que o que cada modo MOVE chegue aos
    blocos — dela: idade, porte, cabeca, marca e traje; dele: idade, cabeca,
    marca e corpo.
    ⚠️ E cobra os DOIS ESTADOS pelo MESMO caminho. Lente que so' olha o estado
    ligado deixa o desligado apodrecer sem ninguem ver.
    """
    w, h = spec["mulher"], spec["homem"]
    for k in ("IMAGE 01/02", "IMAGE 02/02"):
        bl = blocos[k]
        if "%d-year-old %s woman" % (w["idade"], w["etnia"]) not in bl:
            achados.append(("ERRO", "GO10: %s sem a idade/etnia sorteadas dela "
                                    "(%d, %r) — a idade e' a primeira coisa que "
                                    "o modo BELA move"
                            % (k, w["idade"], w["etnia"])))
        for campo in ("porte", "cabeca", "marca"):
            if w[campo] not in bl:
                achados.append(("ERRO", "GO10: %s sem o %s dela (%r) — o que "
                                        "nao chega ao frame nao existe"
                                % (k, campo, w[campo][:34])))
        if _traje_dela(spec) not in bl:
            achados.append(("ERRO", "GO10: %s sem o traje do estado atual do "
                                    "modo BELA (%r)"
                            % (k, _traje_dela(spec))))
        for campo in ("cabeca", "marca"):
            if h[campo] not in bl:
                achados.append(("ERRO", "GO10: %s sem o %s dele (%r) — e' o que "
                                        "o modo FORTE move" % (k, campo,
                                                               h[campo][:34])))
        if spec["corpo_h"] not in bl:
            achados.append(("ERRO", "GO10: %s sem o corpo dele — o corpo E' o "
                                    "argumento deste angulo" % k))
    if spec.get("forte") and spec["corpo_h"] not in (spec["homem"].get("corpo"),):
        achados.append(("ERRO", "GO10: modo FORTE ligado e o corpo em quadro "
                                "nao e' o do homem forte sorteado — tronco de "
                                "58 anos colado num rosto de 34"))


def _go11_contrato16(spec, blocos, achados):
    """As NOVE travas do CONTRATO DE COPY 16s, cobradas de dentro do motor.

    ⭐ `isca_absurda=False`: este angulo nao promete no take 1 nada que ele
    mesmo va' desmentir meio segundo depois. Logo o CT7 vale nos DOIS takes —
    o que aqui nao custa nada, porque a fala nunca nomeia o orgao (GO1).

    ⛔⛔ O CT2 E' FILTRADO, E SO' ELE. O contrato declara a excecao com o nome
    deste agente: *"ha' angulos cuja cena 1 e' aviso de excesso, nao falha (o
    GOOD 16). Quem nao enuncia falha tem de saber que nao enuncia."* Deixar o
    AVISO entrar seria 400 alarmes por autoteste em cima de uma copy que o
    contrato aprova — e alarme que sempre dispara ensina a ignorar o linter
    inteiro, que e' o defeito mais caro que uma lente pode ter.
    ⚠️ O `medir_copy16`, que mede DE FORA, continua contando o CT2 em 100%
    neste motor. E' o comportamento certo: a excecao e' deste motor, nao do
    contrato.
    """
    brutos = []
    sc.lint_copy16(sys.modules[__name__], spec, brutos, isca_absurda=False)
    achados.extend([(n, msg) for n, msg in brutos
                    if not msg.startswith("CT2:")])


def lint(spec, blocos):
    """⚠️ Lint PROPRIO, nao `sc.lint_curto`. Aquele e' da maquinaria de
    colapso 5->3 e pede `base` e `mapa`, que este motor nao tem: ele nao
    deriva de motor longo nenhum."""
    ach = []
    falas = spec["falas"]
    sc.lint_tags(blocos, ach)
    sc.lint_sem_texto(blocos, ach)
    sc.lint_isca_cta(falas[1], ach, "a cena 2 (CTA)")
    sc.lint_cta_literal(falas[1], ach, "a cena 2 (CTA)")
    sc.lint_take_vs_image(blocos, ach)
    sc.lint_painel_honesto(sys.modules[__name__], spec, blocos, ach)
    for f in (_go1_corpo_nao_orgao, _go2_ela_muda, _go4_sache, _go5_orcamento,
              _go6_etnia, _go7_ancora, _go8_tigela, _go9_mistura,
              _go10_modos, _go11_contrato16):
        f(spec, blocos, ach)
    return ach


# ===========================================================================
# PAINEL
# ===========================================================================

EIXOS_UI = [
    ("mundo", "A REGIAO", "MUNDOS", "regiao"),
    ("homem", "QUEM FALA", "HOMENS", "id"),
    ("mulher", "A MULHER", "MULHERES", "id"),
    ("tigela", "A TIGELA", "TIGELAS", "curto"),
]

EIXOS_TRAVAVEIS = ["mundo", "homem", "mulher", "tigela"]

TRAVAS_UI = [("familia_mundo", "regiao", ["livre"] + FAMILIAS_MUNDO)]

# ⚠️ `mundo` entra na lista de ignorados do `lint_painel_honesto` porque o valor
# do eixo e' um id interno; os outros tres chegam ao quadro pelo `cabeca`/
# `marca` deles e pelo `img` da tigela — e a lente cobra isso a cada sorteio.
IGNORA_PAINEL = ("mundo",)

# ⛔ Nenhum eixo do painel mexe na copy: a fala nao cita o quintal, a agua, o
# material da tigela nem as pessoas. Trocar um eixo remonta o QUADRO e mantem a
# fala — declarar o dicionario vazio e' declarar que alguem verificou, em vez de
# deixar o `getattr` decidir por omissao.
EIXOS_QUE_MEXEM_NA_COPY = {}


def resumo_pt(spec):
    """⚠️ Texto de PAINEL, nao copy falada — mas e' o unico lugar onde o
    operador le' o video ANTES de gastar credito gerando. Resumo errado faz ele
    aprovar o que nao viu (licoes §30), e resumo com a string inglesa crua
    emendada na frase ("sentado em a small tiled plunge pool") faz ele parar de
    ler: por isso a agua entra entre PARENTESES, como no BED 16.
    """
    return ("16s, DOIS takes, regiao: %s. Take 1 — O AVISO: homem %s de %d "
            "anos, tronco nu, sentado na agua ate' o peito (%s), falando na "
            "lente; a tigela de %s ja' esta' na borda, INTOCADA; ela colada no "
            "ombro dele, muda. Take 2 — O PREPARO: o MESMO homem de pe', agua "
            "na cintura, inclinado sobre a borda, MEXENDO a tigela com a "
            "colher e sorrindo; o sache GELATIN amassado ao lado dela; ela "
            "colada nele, olhando a tigela. A fala NOMEIA a mistura, diz o "
            "preco e fecha no CTA. Elenco: homem %s de %d anos (modo FORTE "
            "%s), mulher %s de %d anos (modo BELA %s). Ela e' MUDA nos dois "
            "takes."
            % (spec["mundo"]["regiao"], spec["etnia"], spec["homem"]["idade"],
               spec["mundo"]["agua"], spec["tigela"]["curto"],
               spec["etnia"], spec["homem"]["idade"],
               "LIGADO" if spec.get("forte") else "desligado",
               spec["mulher"]["etnia"], spec["mulher"]["idade"],
               "LIGADO" if spec.get("bela") else "desligado"))


# ===========================================================================
# AUTOTESTE
# ===========================================================================

def autoteste(n=400):
    import collections
    pags = sorted(ETNIA)
    erros = collections.Counter()
    dist = collections.defaultdict(set)
    tam = collections.defaultdict(list)
    mundos = collections.Counter()
    falhas, avisos = [], 0
    # ⭐⭐ OS QUATRO ESTADOS DOS DOIS MODOS, MEDIDOS JUNTOS. Medir so' o default
    # e' medir um quarto do agente: cada toggle troca um elenco inteiro, e um
    # KeyError do lado ligado morreria CALADO dentro do callback do tkinter —
    # que e' exatamente como seis botoes `trocar` ficaram quebrados em
    # 2026-07-31 sem ninguem ver.
    estados = collections.defaultdict(lambda: collections.defaultdict(set))

    for i in range(n):
        modo = {}
        if i % 2:
            modo["bela"] = True
        if (i // 2) % 2:
            modo["forte"] = True
        s = sortear(pags[i % len(pags)], random.Random(i), {}, modo)
        chave = (bool(s["bela"]), bool(s["forte"]))
        estados[chave]["idade_dela"].add(s["mulher"]["idade"])
        estados[chave]["idade_dele"].add(s["homem"]["idade"])
        estados[chave]["traje"].add(_traje_dela(s))
        mundos[s["mundo"]["id"]] += 1
        for c, f in enumerate(s["falas"], 1):
            dist[c].add(f)
            tam[c].append(_palavras(f))
        for nivel, msg in lint(s, montar(s)):
            if nivel == "ERRO":
                erros[msg[:70]] += 1
            else:
                avisos += 1

    print("GOOD 16 — %d sorteios (os QUATRO estados de bela x forte)" % n)
    for c in sorted(dist):
        v = sorted(tam[c])
        print("  cena %d: %d falas distintas · palavras min/med/max %d/%d/%d"
              % (c, len(dist[c]), v[0], v[len(v) // 2], v[-1]))
    print("  mundos: %d de %d sorteados" % (len(mundos), len(MUNDOS)))
    for on in sorted(estados):
        e = estados[on]
        print("  bela %-3s forte %-3s · ela %d..%d · ele %d..%d · %d trajes"
              % ("ON" if on[0] else "off", "ON" if on[1] else "off",
                 min(e["idade_dela"]), max(e["idade_dela"]),
                 min(e["idade_dele"]), max(e["idade_dele"]),
                 len(e["traje"])))
    print("  linter: %d ERRO, %d AVISO" % (sum(erros.values()), avisos))
    for k, v in erros.most_common(5):
        print("     %3dx %s" % (v, k))

    # ⛔ CONTROLE DOS TOGGLES: modo que nao MOVE nada e' forma sem funcao.
    if estados[(False, False)]["idade_dele"] == estados[(False, True)]["idade_dele"]:
        falhas.append("MODO FORTE: os dois estados sorteiam as MESMAS idades "
                      "para o homem — toggle que nao muda nada")
    if estados[(False, False)]["traje"] == estados[(True, False)]["traje"]:
        falhas.append("MODO BELA: os dois estados sorteiam os MESMOS trajes — "
                      "toggle que nao muda nada")

    # ⛔ CONTROLE DE MUNDO: cada etnia da tabela precisa de mundo compativel, e
    # cada mundo precisa do par de traje do modo BELA.
    for et in sorted(set(ETNIA.values())):
        if not [m for m in MUNDOS if et in m["etnias"]]:
            falhas.append("MUNDO: nenhum mundo comporta a etnia %r" % et)
    for m in MUNDOS:
        if m["dela_bela"] == m["dela"]:
            falhas.append("MUNDO %s: o traje bela e' igual ao normal — o "
                          "toggle nao move nada nesta regiao" % m["id"])
    if len(mundos) < len(MUNDOS):
        falhas.append("MUNDOS: so' %d de %d aparecem em %d sorteios"
                      % (len(mundos), len(MUNDOS), n))

    # ⭐ [ALCANCE] — entrada que nao cabe com os minimos dos outros beats nunca
    # e' sorteada. Nao e' rara: e' MORTA, e o autoteste a contava como viva.
    for rot, pool, cena, outros in (
            ("AVISOS", AVISOS, 1, [ESPOSAS, AGUENTAM]),
            ("ESPOSAS", ESPOSAS, 1, [AVISOS, AGUENTAM]),
            ("AGUENTAM", AGUENTAM, 1, [AVISOS, ESPOSAS]),
            ("MISTURAS", MISTURAS, 2, [PRECOS, CTAS]),
            ("PRECOS", PRECOS, 2, [MISTURAS, CTAS]),
            ("CTAS", CTAS, 2, [MISTURAS, PRECOS])):
        reserva = sum(_mn(p) for p in outros)
        mortas = [x for x in pool
                  if _palavras(x) + reserva > TETO_FALA[cena]]
        if mortas:
            falhas.append("[ALCANCE] %s: %d de %d nunca sao sorteadas "
                          "(teto real %d palavras)"
                          % (rot, len(mortas), len(pool),
                             TETO_FALA[cena] - reserva))

    # ⛔ CONTROLE DE CONTRATO: toda MISTURA carrega o literal do funil E um
    # designador da mistura. Se um dia entrar uma entrada sem, ela so'
    # apareceria em ~1/8 dos sorteios.
    sem_lit = [x for x in MISTURAS if "gelatin trick" not in x]
    if sem_lit:
        falhas.append("CT3: %d entrada(s) de MISTURAS sem `gelatin trick`: %s"
                      % (len(sem_lit), sem_lit[:1]))
    sem_des = [x for x in MISTURAS if not _MISTURA_NOMEADA.search(x)]
    if sem_des:
        falhas.append("GO9: %d entrada(s) de MISTURAS sem designador da "
                      "mistura: %s" % (len(sem_des), sem_des[:1]))
    com_ing = [x for x in MISTURAS + PRECOS + CTAS
               if sc.INGREDIENTES_16.search(x)]
    if com_ing:
        falhas.append("CT5: %d entrada(s) da cena 2 nomeiam ingrediente: %s"
                      % (len(com_ing), com_ing[:1]))

    # ⛔⛔ CONTROLE POSITIVO DA GO9 — lente que nunca acusa e' forma sem funcao,
    # e "sem achado" nela significaria "ninguem olhou". A frase abaixo e' a copy
    # que este motor tinha ATE' 2026-08-10; se a lente parar de pega-la, ela
    # quebrou.
    morta = ("This leaves your body harder and stronger than in years. "
             "Costs almost nothing. Comment gelatin, and the recipe goes to "
             "your messages.")
    prova = []
    _go9_mistura({"falas": ["", morta]}, {}, prova)
    if len(prova) < 2:
        falhas.append("GO9: a lente parou de acusar a copy antiga (%d de 2 "
                      "achados) — ela era a unica coisa entre este pool e o "
                      "pronome sem dono" % len(prova))
    limpo = []
    _go9_mistura({"falas": ["", MISTURAS[0] + " " + PRECOS[0] + " "
                            + CTAS[0]]}, {}, limpo)
    if limpo:
        falhas.append("GO9: a lente acusa copy limpa (%s)" % limpo[0][1][:60])

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
    # ⭐ Os mesmos toggles do painel, pela linha de comando: aceite e' MEDICAO,
    # e medir um estado exige poder liga-lo sem abrir a janela.
    # ⛔ O FORTE nasce LIGADO tambem aqui (`--sem-forte` desliga), para a linha
    # de comando entregar o MESMO video que o app entrega. CLI e painel com
    # defaults diferentes e' a divergencia que faz o operador aprovar o que nao
    # viu.
    ap.add_argument("--bela", action="store_true",
                    help="MODO BELA ligado (o padrao e' o pool proprio)")
    ap.add_argument("--sem-forte", action="store_true",
                    help="desliga o MODO FORTE, que vem LIGADO por padrao")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--autoteste", action="store_true")
    a = ap.parse_args()

    if a.autoteste:
        return autoteste()

    led = _carregar_ledger()
    rng = random.Random(a.seed)
    travas = {"familia_mundo": a.regiao} if a.regiao else {}
    if a.bela:
        travas["bela"] = True
    if not a.sem_forte:
        travas["forte"] = True
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
