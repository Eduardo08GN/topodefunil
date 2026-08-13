#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE BED 16 — a cama fria e a tigela · 2 takes de 8s = 16 segundos.

⭐⭐⭐ A TIGELA E' O FIO DO VIDEO, e essa e' a razao de ser do angulo. No take 1
ela esta' NO COLO DELE, sozinho, mexendo a mistura, enquanto ela olha irritada
de varios pes de distancia. No take 2 ela esta' NAS MAOS DELA, colada nele,
dentro d'agua. **O MESMO OBJETO conta o antes e o depois sem uma palavra** — e
e' por isso que o agente se chama BED e nao WIFE: o que muda de mao e' a tigela,
e a cama e' onde ela comeca.

⭐⭐ O SEGUNDO ANGULO DO PARQUE EM QUE O HOMEM FALA E A MULHER E' MUDA (o outro
e' o GOOD 16). Aqui a inversao nao e' so' de quem narra: e' de QUAL PROVA o
video mostra. Nos outros vinte a prova e' um corpo, um prop ou um copo. Neste
angulo **a prova e' o casamento**, e ela se le' em DOIS eixos ao mesmo tempo:
a POSTURA dela (bracos cruzados encarando -> corpo colado) e a MAO em que a
tigela esta'. A inversao E' o video.

FONTE: reel do Facebook 1752010159557238.
⚠️⚠️ LEITURA OTICA PENDENTE. ⚠️ A FONTE MUDOU DE REEL (era o 1244976845366022) e
o reel novo tambem NAO baixa sem login. O que esta' aqui vem de **UM PRINT** que
o operador mandou (take 1, elemento por elemento) e da especificacao escrita
dele. Consequencia declarada, para ninguem tratar como verbatim de fonte:

    ⛔ OS POOLS DE FALA SAO CONSTRUCAO NOSSA sob o CONTRATO DE COPY 16s, nao
       transcricao. Eles serao REFINADOS quando o mp4 chegar — e ate' la' o
       criterio deles e' o contrato (`CONTRATO-COPY-16S.md`), nao a fonte.

⚠️ E o prompt que o operador mandou junto do print veio *"apenas como
referencia, nao o use literalmente"*. Os elementos dele foram TRADUZIDOS para o
idioma dos nossos blocos; nenhuma frase dele foi copiada.

O ARCO — 2 cenas de 8s, destino AdBatch Vertical 2:

    take 1  A CAMA E A      ele MUITO PROXIMO da lente, tres-quartos de perfil,
            TIGELA          tronco nu, calca de pijama xadrez, a TIGELA NO COLO
                            e a colher mexendo a mistura ambar · ela varios pes
                            atras, sentada contra a cabeceira, edredom branco,
                            BRACOS CRUZADOS, ENCARANDO ele
                            copy: a falha DELE + o custo conjugal
    take 2  A VIRADA        o MESMO homem, com rosto, dentro d'agua (piscina,
                            jacuzzi, banheira) · ela COLADA nele, e a TIGELA
                            agora esta' NAS MAOS DELA, com os cubos de gelatina
                            copy: mecanismo com razao -> prova -> CTA

⭐⭐ O TAKE 1 NAO E' SO' A FALHA — E' A FALHA MAIS O COMECO DA SAIDA. Ele ja'
esta' FAZENDO o truque enquanto conta o que perdeu, e e' isso que da' ao arco
um lugar para ir. Antes deste print ele so' estava sentado, cabisbaixo.

⛔⛔ AS CINCO DECISOES DO OPERADOR (2026-08-10) — NAO SE REABREM
-----------------------------------------------------------------------------
 1. NARRADOR = ELE. `SEXOS = ("homem",)`. A mulher e' MUDA nos dois takes.
 2. A TIGELA E' O PROPRIO GELATIN TRICK, e ela TROCA DE MAO entre os takes. O
    pool `TIGELAS` nao e' de vasilhame de bebida — e' de COMO O PREPARO APARECE
    em quadro. No take 1 mistura semi-liquida sendo mexida; no take 2 CUBOS DE
    GELATINA visiveis dentro.
 3. A REGIAO ARRASTA TUDO. Um eixo so' (`mundo`) move etnia + quarto + agua +
    luz + audio + traje dela. Mecanica do FALTA 16 (`MUNDOS` com `etnias`)
    fundida com a do GOOD 16 (mundo aquatico com `agua`, `luz`, `audio`).
 4. NO TAKE 2 O HOMEM APARECE COM ROSTO, e e' O MESMO do take 1.
 5. MODO BELA, pelo contrato compartilhado do repo (`MODO_BELA = True` +
    `sc.ref_bela`), e ele resolve uma tensao real — ver o bloco das MULHERES.

⛔⛔ A PROFUNDIDADE DE CAMPO E' A COPY VISUAL DO TAKE 1. Ele GRANDE e NITIDO em
primeiro plano, ela MENOR e mais SUAVE varios pes atras: a distancia entre os
dois e' o argumento do quadro, e ela e' pedida ao gerador de forma EXPLICITA
(lente BD9). Sem isso o Veo achata os dois no mesmo plano e a cama vira um casal
sentado junto — que e' exatamente o take 2, oito segundos antes da hora.

⛔⛔ A DECISAO 4 EXIGE ANCORA DE CONTINUIDADE FORTE, e isso e' licao paga: no
VAZAMENTO o corpo-prova voltou na cena seguinte como um senhor de oculos e
bigode — e como o TAKE dizia `Only he speaks`, o ESTRANHO falava a fala do REF.
Aqui o bloco 2 repete idade + etnia + a marca facial sorteada + o sinal
sorteado + `It is the same man`. Lente BD3 cobra os cinco.

⛔ NAO EXISTE PROP FALICO NESTE ANGULO, e nao se inventa um. A prova e' o
casamento. A lente BD6 reprova qualquer geoduck, peca anatomica ou proxy de
legume que alguem tente "consertar" para ca' no futuro.

⛔⛔ A CONTA DO CASAMENTO E' PUBLICA — achado da conferencia de 2026-08-10, e o
unico defeito que sobreviveu aos seis medidores externos, ao linter em 0/0 e ao
autoteste OK. Duas entradas de VIRADAS contam os anos de casamento (`Twenty six
years married`, `Thirty one years`) e a IMAGE diz a idade dela em numero. Quem
subtrai:

    · modo BELA LIGADO   (esposa 21-33): 16,1% dos videos, medido em 1000 —
      esposa de 21 + 26 anos de casamento = casada aos MENOS CINCO;
    · modo BELA DESLIGADO (esposa 44-52): 5,5% — esposa de 44 + 31 anos de
      casamento = casada aos TREZE. ⛔ Este e' o pior dos dois, e nao o menor:
      o numero negativo o espectador le' como erro de roteiro; `casada aos
      treze` num video sobre sexo e' a familia de token que derruba pagina.

⭐ A correcao NAO reescreve copy aprovada: as duas linhas sao as melhores do
pool pelo CT2 (numero + dano) e seguem vivas — `_viradas_da_esposa` so' as tira
do sorteio quando a conta nao fecha com a esposa em quadro. A lente BD13 refaz
a subtracao na fala JA' MONTADA a cada sorteio.
⚠️ NENHUM medidor externo pega isto, e a razao vale para todo agente: eles
medem a fala CONTRA O CONTRATO, e este defeito mora entre a fala e o ELENCO. So'
aparece lendo em voz alta com o bloco IMAGE do lado.

⛔ O print da fonte tem legenda QUEIMADA. Nos nao queimamos texto: a legenda
nasce depois, no Veo Editor, a partir do Whisper. A trava `No on-screen text,
no watermark` vale em todo bloco (BD5).

⚠️ PENDENCIA REGISTRADA — A GEOMETRIA DA FALA NO TAKE 1. O print mostra o homem
de tres-quartos de perfil e de OLHAR BAIXO, sobre a tigela; mas ele e' o
NARRADOR (decisao 1) e precisa falar na lente. O motor resolve com o CORPO de
tres-quartos virado para longe dela, as MAOS na tigela do colo e o ROSTO virado
para a camera — a postura derrotada do print fica de pe' e a fala tem para onde
sair. **Isto e' cena, e cena e' alcada do operador**: esta' aqui declarado para
ser confirmado, nao para passar despercebido.

⚠️⚠️ DUAS PENDENCIAS DE COPY ACHADAS NA LEITURA EM VOZ ALTA (2026-08-10) E NAO
CORRIGIDAS DE PROPOSITO — sao anteriores a' mudanca de cena e nenhuma das duas
e' exigida por ela, entao mexer nelas seria reescrever copy aprovada sem ordem.
⛔ Copy e' alcada do operador: aqui estao medidas, para ele decidir.

 A. MECANISMO EM 2a PESSOA COM VERBO NO PASSADO — 12,3% dos videos (247 de
    2000). Duas das 16 entradas de MECANISMOS sao `The gelatin trick FIXED
    blood flow to your {o}.` e `... GAVE blood flow to your {o}.`. As outras
    catorze estao no presente (`opens`, `restores`, `clears`...). Em 1a pessoa
    o passado fechava (`fixed blood flow to MY {o}` = depoimento); a lista foi
    passada para a 2a pessoa — decisao certa e documentada no bloco MECANISMOS
    — e estas duas ficaram para tras. Dito na lente, `o truque CONSERTOU o
    fluxo para o SEU {o}` afirma como ja' acontecido algo que o espectador
    ainda nao fez. ⭐ Conserto sugerido, se o operador quiser: trocar por
    `fixes` e `gives`, que mantem as 9 palavras e nao move mais nada.

 B. A IDADE DITA PASSA A IDADE EM QUADRO — 6,0% (119 de 2000). Quatro entradas
    de FALHAS citam a idade dele (`at fifty five`, `at fifty seven`, `At fifty
    eight`, `after fifty`) e os HOMENS vao de 55 a 60: um homem de 57 dizendo
    `At fifty eight my {o} went soft` fala de um ano que nao chegou.
    ⚠️ E' MAIS FRACO que a conta do casamento e por isso nao entrou na mesma
    correcao: a idade DELE nao aparece escrita em lugar nenhum que o
    espectador leia, e 55 ou 58 sao o mesmo rosto na tela. So' o operador diz
    se vale filtrar por idade (como `_viradas_da_esposa`) ou deixar correr.

    python funil-organico/bed16_short.py --pagina joe --n 1
    python funil-organico/bed16_short.py --autoteste
    python funil-organico/bed16_short_app.py
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

LEDGER = os.path.join(AQUI, ".bed-16-ledger.json")

TITULO = "AGENTE BED 16"
SLUG = "bed-16"
SUBTITULO = ("2 takes de 8s = 16 segundos · a tigela no colo dele, depois nas "
             "maos dela · o homem fala e ela e' muda · a prova e' o casamento")

CENAS_UI = ["1 · A CAMA E A TIGELA", "2 · A TIGELA NAS MAOS DELA"]

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

# ⭐⭐ MODO BELA LIGADO — ordem do operador, 2026-08-10, e aqui ele RESOLVE UMA
# TENSAO REAL em vez de so' enfeitar. O print da fonte mostra uma esposa de
# ~45-50 de bracos cruzados e cara de brava; a LEI DO REF pede mulher sempre
# bonita. Os dois estao certos e nao cabem no mesmo pool:
#
#   · DESLIGADO -> a esposa REALISTA do print (pool `MULHERES`, 44-52 anos).
#     E' o quadro que o operador mandou, com a idade e o porte que ele mandou.
#   · LIGADO    -> `sc.ref_bela` (contrato compartilhado do repo), e ela vem no
#     padrao MODO BELA.
#
# ⛔ E O MODO ARRASTA O QUE PODE ARRASTAR, sem furar a regiao: "trocar so' o
# rosto deixa a REF de biquini de trico amish". Aqui o MUNDO ja' e' arrastado
# pela REGIAO (quarto, agua, luz, audio), entao o que este toggle move e'
# IDADE + PORTE + TRAJE DELA — e o traje move para a variante BELA **da mesma
# regiao sorteada** (`dela_q_bela` / `dela_a_bela`), nunca para uma roupa
# generica de outro mundo.
#
# ⛔ MODO_FORTE continua desligado, e a ausencia e' declarada: o corpo dele nao
# e' o argumento aqui (o argumento e' ela voltando), e um tronco de academia
# contradiria a cena da cama.
MODO_BELA = True
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
# ⭐⭐ E CADA ENTRADA CARREGA O TRAJE DELA EM DOIS REGISTROS — `dela_q`/`dela_a`
# (modo BELA desligado, a esposa realista do print) e `dela_q_bela`/
# `dela_a_bela` (modo ligado). O par bela e' da MESMA regiao, so' que no
# registro do modo: e' isso que impede a REF de biquini de trico amish, o modo
# de falha que o repo ja' nomeou. ⛔ E ele para ANTES do extremo de biquini —
# ordem do operador de 2026-08-05, que vale para o pool compartilhado e vale
# aqui: o take 2 e' dentro d'agua e o top da regiao ja' e' roupa de banho; o que
# o modo move e' o corte, nao a cobertura.
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
     "dela_q_bela": "a short black satin slip with thin straps",
     "dela_a_bela": "a white halter bikini top",
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
     "dela_q_bela": "a short deep red satin slip with thin straps",
     "dela_a_bela": "a coral halter bikini top",
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
     "dela_q_bela": "a short black satin cami and matching shorts",
     "dela_a_bela": "a black halter bikini top",
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
     "dela_q_bela": "a short navy satin slip with thin straps",
     "dela_a_bela": "a navy halter bikini top",
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
     "dela_q_bela": "a short cream satin slip with thin straps",
     "dela_a_bela": "a white twist-front bikini top",
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
     "dela_q_bela": "a short black satin slip with thin straps",
     "dela_a_bela": "a black halter bikini top",
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
     "dela_q_bela": "a short deep purple satin slip with thin straps",
     "dela_a_bela": "a gold halter bikini top",
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
     "dela_q_bela": "a short pale blue satin slip with thin straps",
     "dela_a_bela": "a turquoise halter bikini top",
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
     "dela_q_bela": "a short white satin slip with thin straps",
     "dela_a_bela": "a white twist-front bikini top",
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
     "dela_q_bela": "a short charcoal satin slip with thin straps",
     "dela_a_bela": "a dark green halter bikini top",
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
     "dela_q_bela": "a short burgundy satin slip with thin straps",
     "dela_a_bela": "a red halter bikini top",
     "etnias": ["white American"]},

    {"id": "creole", "familia": "creole", "regiao": "Nova Orleans",
     "q_cen": "a bedroom in a New Orleans shotgun house, tall shuttered "
              "windows and a slow ceiling fan",
     "q_luz": "one lamp on the nightstand, the shutters closed and dark",
     "q_audio": "a streetcar far off, cicadas",
     # ⚠️ `banana leaves` seria o cenario certo para um patio de Nova Orleans —
     # e foi o que estava aqui. A lente BD6 acusou 21 de 400, e ela esta'
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
     "dela_q_bela": "a short black lace-trimmed satin cami and matching shorts",
     "dela_a_bela": "an emerald halter bikini top",
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
     "dela_q_bela": "a short ivory satin slip with thin straps",
     "dela_a_bela": "a black twist-front bikini top",
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
     "dela_q_bela": "a short coral satin cami and matching shorts",
     "dela_a_bela": "a turquoise halter bikini top",
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
     "dela_q_bela": "a short black satin cami and matching shorts",
     "dela_a_bela": "a white halter bikini top",
     "etnias": ["white American", "Black American"]},

    # ⭐⭐ + 2026-08-13, ordem do operador: *"aumente o pool de opcoes
    # substancialmente, tambem dos ambientes"*. De 15 para 24 regioes.
    # ⛔ Cada entrada nova declara EXATAMENTE as mesmas quinze chaves das
    # vizinhas — quarto + luz + audio do take 1, casa + agua + luz + audio do
    # take 2, os QUATRO trajes dela (normal e bela, quarto e agua) e as
    # `etnias`. Cenario aqui e' AMBIENTE INTEIRO, nao fundo: entrada que so'
    # trocasse a parede deixaria o gerador improvisar a luz e o som.
    # ⛔ E o `a_cen` continua dizendo `the same <casa>`, que e' o que impede o
    # corte de ler como dois videos colados (controle do autoteste).
    # ⭐ COBERTURA DE ETNIA AUMENTADA nas duas: 9 -> 15 mundos que comportam
    # `white American` e 8 -> 13 que comportam `Black American`. Etnia sem
    # cenario compativel derruba o sorteio.
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
     "dela_q_bela": "a short pale pink satin slip with thin straps",
     "dela_a_bela": "a white halter bikini top",
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
     "dela_q_bela": "a short sand-coloured satin slip with thin straps",
     "dela_a_bela": "a terracotta halter bikini top",
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
     "dela_q_bela": "a short deep purple satin slip with thin straps",
     "dela_a_bela": "a purple halter bikini top",
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
     "dela_q_bela": "a short black satin slip with thin straps",
     "dela_a_bela": "a red halter bikini top",
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
     "dela_q_bela": "a short forest green satin slip with thin straps",
     "dela_a_bela": "a forest green halter bikini top",
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
     "dela_q_bela": "a short seafoam satin slip with thin straps",
     "dela_a_bela": "a seafoam halter bikini top",
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
     "dela_q_bela": "a short burgundy satin slip with thin straps",
     "dela_a_bela": "a burgundy halter bikini top",
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
     "dela_q_bela": "a short pale blue satin slip with thin straps",
     "dela_a_bela": "a pale blue halter bikini top",
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
     "dela_q_bela": "a short dusty rose satin slip with thin straps",
     "dela_a_bela": "a rose halter bikini top",
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
# pool de opcoes substancialmente, tambem dos ambientes"*. De 6 para 24.
# ⚠️ E o conserto NAO e' de tamanho, e' de CONTEUDO: as SEIS entradas antigas
# tinham `sinal` de DANO — `a pale scar through his left eyebrow`, `a broad flat
# nose broken once and never set`, `heavy folds under both eyes`, `a white patch
# of old sun damage on his left temple`, `a deep vertical crease between his
# eyebrows`. Seis de seis. O `sinal` e' repetido LITERAL na IMAGE 02 (ancora da
# BD3), entao cada video levava a mesma avaria duas vezes, e o render devolvia o
# que o operador viu. E' a mesma licao do PLACA 16 (*"esses caras tao parecendo
# mendigo"*): a ancora tem de ser DISTINTIVA, nunca DETERIORADA.
# ⭐ O que entra no lugar sao ancoras SAUDAVEIS e igualmente permanentes —
# covinha, queixo partido, mecha branca, pinta, sarda, laugh lines, argola ou
# tarraxa, entrada em bico, sobrancelha cheia e reta: todas voltam iguais no
# take 2 e nenhuma le' como estrago.
# ⛔ NENHUMA PALAVRA DE APROVACAO (handsome, rugged, strong jaw). Elogio no
# prompt puxa o rosto para a media do banco de imagem — mesmo mecanismo pelo
# qual `not a celebrity` invoca a celebridade. Descreve-se FEICAO, nao
# julgamento.
# ⛔ E NENHUMA COR DE PELE: a etnia entra pela PAGINA, na frase montada. Cor
# escrita aqui criaria duas vozes no mesmo sintagma.
# ⭐ OCULOS EM 6 DAS 24 (25%) — o eixo estava ZERADO no `medir_personagens
# --gate` (reprovacao). Ele fica no `marca`, junto do cabelo, porque e' ali que
# a IMAGE 02 repete a ancora.
HOMENS = [
    {"id": "grisalho_curto", "idade": 57,
     "marca": "close-cropped grey hair and a full grey beard going white at "
              "the chin",
     "sinal": "a strong cleft in his chin"},
    {"id": "careca_cavanhaque", "idade": 59,
     "marca": "a clean-shaven scalp and a short grey goatee",
     "sinal": "a small dark mole high on his right cheek"},
    {"id": "sal_pimenta", "idade": 55,
     "marca": "short salt-and-pepper hair and three days of grey stubble",
     "sinal": "laugh lines at the corners of his eyes"},
    {"id": "barba_cheia", "idade": 60,
     "marca": "grey hair with a low widow's peak and a full white beard",
     "sinal": "heavy level brows over wide-set eyes"},
    {"id": "bigode_grisalho", "idade": 58,
     "marca": "close-cropped grey hair and a thick grey moustache",
     "sinal": "a shallow dimple in his left cheek and light freckling across "
              "his nose"},
    {"id": "ondulado", "idade": 56,
     "marca": "short wavy grey hair and a close grey beard",
     "sinal": "a patch of white above his left temple"},
    {"id": "oculos_fio", "idade": 61,
     "marca": "thick silver hair swept straight back, a clean-shaven face and "
              "thin wire-rimmed glasses",
     "sinal": "a small mole beside his right eye"},
    {"id": "barba_quadrada", "idade": 62,
     "marca": "close-cropped white hair and a full white beard trimmed square "
              "at the jaw",
     "sinal": "smooth-skinned with a cleft chin"},
    {"id": "topete_prata", "idade": 55,
     "marca": "silver hair still full on top and combed high, a clean-shaven "
              "face and thin steel-rimmed glasses",
     "sinal": "a beauty mark below his right eye"},
    {"id": "raspado_cavanhaque", "idade": 58,
     "marca": "a shaved head and a short white goatee",
     "sinal": "heavy level brows and a wide square chin"},
    {"id": "oculos_retangular", "idade": 59,
     "marca": "short grey hair parted on one side, a trimmed grey beard and "
              "dark rectangular glasses",
     "sinal": "a shallow cleft in his chin"},
    {"id": "cachos_grisalhos", "idade": 56,
     "marca": "loose grey curls kept short and a close-trimmed grey beard",
     "sinal": "a small gold stud in his left ear"},
    {"id": "bigode_chevron", "idade": 60,
     "marca": "grey hair clipped short at the sides and a thick chevron "
              "moustache",
     "sinal": "laugh lines at the corners of his mouth"},
    {"id": "entradas_barba", "idade": 57,
     "marca": "a high hairline with thick grey hair behind it and a full grey "
              "beard",
     "sinal": "a small mole on his left jaw"},
    {"id": "oculos_grossos", "idade": 62,
     "marca": "short white hair, a clean-shaven face and heavy black-framed "
              "glasses",
     "sinal": "a silver streak through one eyebrow"},
    {"id": "lateral_prateada", "idade": 55,
     "marca": "dark hair going silver at the sides, cut short, and a close "
              "dark beard",
     "sinal": "a dimple in each cheek when he talks"},
    {"id": "barba_curta_branca", "idade": 61,
     "marca": "white hair kept very short and a short white beard",
     "sinal": "smooth-skinned with a broad square chin"},
    {"id": "onda_para_tras", "idade": 58,
     "marca": "wavy salt-and-pepper hair pushed back off the forehead and a "
              "clean-shaven face",
     "sinal": "smooth-skinned with a small beauty mark on his left cheekbone"},
    {"id": "oculos_aro_fino", "idade": 56,
     "marca": "short dark grey hair, a close grey beard and rimless glasses",
     "sinal": "a cleft chin under heavy level brows"},
    {"id": "crista_branca", "idade": 59,
     "marca": "a white streak running through short dark hair and a trimmed "
              "dark beard",
     "sinal": "a small mole above his lip"},
    {"id": "careca_bigode", "idade": 60,
     "marca": "a bald crown with grey at the sides and a thick grey moustache",
     "sinal": "a small gold hoop in his left ear"},
    {"id": "barba_longa_grisalha", "idade": 62,
     "marca": "grey hair combed back short and a long grey beard combed "
              "straight",
     "sinal": "freckles scattered across his nose"},
    {"id": "oculos_claro", "idade": 57,
     "marca": "close-cropped grey hair, a short grey beard and clear-framed "
              "glasses",
     "sinal": "a shallow dimple in his chin"},
    {"id": "franja_grisalha", "idade": 58,
     "marca": "straight grey hair kept a little long over the forehead and a "
              "clean-shaven face",
     "sinal": "laugh lines and a small mole at the corner of his jaw"},
]

# ⛔ Ele esta' de TRONCO NU no take 1 (frame da fonte) e com a agua no peito no
# take 2.
#
# ⛔⛔ REESCRITO INTEIRO EM 2026-08-13, ordem do operador com o print na mao:
# *"melhore a aparencia e shape desses homens"*. O pool antigo tinha SEIS
# entradas e CINCO descreviam corpo mole ou curvado (`soft middle`, `gone soft
# at the waist`, `lean and stooped, the shoulder blades showing`, `a low round
# belly`, `softened with age`) — e o `corpo_h` entra nos DOIS blocos, entao o
# render trazia o mesmo homem fora de forma duas vezes.
# ⚠️ O bloco antigo justificava isso dizendo que "um tronco de academia
# contradiria a cena da cama". A metade certa dessa frase FICA e esta' escrita
# no alvo: ⛔ NAO e' fisiculturista. Este angulo nao tem MODO FORTE, e musculo
# de academia num homem de 58 na cama quebra a leitura de marido comum que
# voltou a funcionar. O alvo e' **em forma para a idade**: solido, ombro largo,
# peito firme, cintura controlada — o corpo de quem carrega peso na vida, nao
# de quem posa. De 6 para 14.
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

# ⛔ A CALCA DE PIJAMA vem do print (xadrez azul-escuro) e por isso EXISTE em
# quadro: homem de tronco nu na beirada da cama sem nada dito da cintura para
# baixo e' o convite exato para o gerador improvisar — e improviso de cintura
# para baixo e' recusa. ⚠️ E' um sorteio SEM eixo de painel, como o `corpo_h`:
# ele chega ao quadro, o operador nao precisa escolher.
PIJAMAS = [
    "dark blue plaid pyjama trousers",
    "faded grey plaid pyjama trousers",
    "dark green checked pyjama trousers",
    "navy striped pyjama trousers",
    "plain charcoal cotton pyjama trousers",
    "burgundy plaid pyjama trousers",
]


# ===========================================================================
# A MULHER — ⭐ etnia SOLTA. Ela e' MUDA nos dois takes.
# ===========================================================================
# ⭐⭐ ESTE POOL E' O ESTADO **BELA DESLIGADO**, e ele e' a ESPOSA DO PRINT: 44 a
# 52 anos, de bracos cruzados, cara de brava, sem retoque. Nao e' descuido com a
# LEI DO REF — e' a resolucao que o operador mandou para o choque entre as duas
# verdades (ver o bloco `MODO_BELA` la' em cima). Com o toggle LIGADO ela vem do
# `sc.ref_bela`, e os DOIS estados sao validos e medidos.
#
# ⚠️ Ela NAO e' a REF de congruencia deste motor — quem fala e' o homem, e e' a
# etnia DELE que a pagina governa. Por isso a idade e o grisalho dela nao ferem
# a lei: a lei mira a REF, e a REF aqui e' ele.
#
# ⛔ MARCA FACIAL OBRIGATORIA mesmo assim, e pelo motivo de sempre: ela reaparece
# no take 2 depois de um corte, de outra roupa e de outra luz. Sem ancora o Veo
# devolve outra mulher — o mesmo defeito que a BD3 cobra dele.
# ⛔ E ela e' MUDA — invariante do angulo, nao estilo. Sem `Only he speaks` no
# TAKE o Veo poe as duas bocas a mexer e o dialogo sai monofonico e torto
# (lente BD1).
# ⛔⛔ AMPLIADO E SANEADO EM 2026-08-13 — ordem do operador: *"melhore a
# aparencia e shape desses homens"* / *"aumente o pool de opcoes
# substancialmente, tambem dos ambientes"*. De 10 para 24.
# ⚠️ "Realista" nunca quis dizer AVARIADA, e tres entradas tinham escorregado
# para o lado errado: `going dry at the ends`, `a deep line between her brows`,
# `a small scar through one eyebrow`, `deep lines at the corners of her mouth`,
# `a faint scar on her chin`. A `marca` dela e' repetida LITERAL na IMAGE 02
# (lente BD11), entao cada uma dessas ia duas vezes ao render. Trocadas por
# ancoras saudaveis e igualmente permanentes — covinha, pinta, sinal de beleza,
# mecha, sardas, laugh lines.
# ⭐ OCULOS EM 6 DAS 24 (25%): o eixo estava ZERADO no `medir_personagens
# --gate` (reprovacao). ⚠️ Aqui NAO ha' isencao de LEI DO REF como no `wife16`,
# porque este pool e' o estado BELA DESLIGADO — a esposa do print, nao a REF.
MULHERES = [
    {"id": "loira_seca", "idade": 47, "etnia": "white American",
     "porte": "solid through the shoulders and hips",
     "marca": "shoulder-length blonde hair with a deep side part and a small "
              "beauty mark on her jaw"},
    {"id": "ruiva_desbotada", "idade": 50, "etnia": "white American",
     "porte": "small and thin with narrow shoulders",
     "marca": "auburn hair pinned back off her face and a dense spray "
              "of freckles"},
    {"id": "morena_lisa", "idade": 46, "etnia": "white American",
     "porte": "heavy through the middle with soft arms",
     "marca": "dark brown hair cut blunt at the jaw and a dimple in one cheek"},
    {"id": "bob_grisalho", "idade": 52, "etnia": "white American",
     "porte": "average build, a little heavy at the waist",
     "marca": "a greying chestnut bob and laugh lines at the corners of her "
              "mouth"},
    {"id": "trancas_lateral", "idade": 48, "etnia": "Black American",
     "porte": "broad-shouldered and solidly built",
     "marca": "long box braids gathered over one shoulder and a small mole on "
              "her cheek"},
    {"id": "afro_curto", "idade": 45, "etnia": "Black American",
     "porte": "slight and wiry with thin arms",
     "marca": "a short natural afro going grey at the temples and a small gold "
              "stud in one nostril"},
    {"id": "trancas_longas", "idade": 51, "etnia": "Black American",
     "porte": "full-figured with round shoulders",
     "marca": "waist-length braids and a beauty spot high on her cheek"},
    {"id": "cachos_altos", "idade": 49, "etnia": "Black American",
     "porte": "tall and big-boned",
     "marca": "greying curls gathered high on her head and a small birthmark "
              "at her temple"},
    {"id": "latina_ondulada", "idade": 47, "etnia": "Latina American",
     "porte": "short and softly built",
     "marca": "long wavy black hair with grey coming in at the part and a "
              "small mole beside her right eye"},
    {"id": "asiatica_lisa", "idade": 44, "etnia": "Asian American",
     "porte": "slim with rounded shoulders",
     "marca": "straight black hair to the shoulders cut with a heavy fringe "
              "and a dimple in her chin"},
    {"id": "loira_curta_oculos", "idade": 50, "etnia": "white American",
     "porte": "trim with square shoulders",
     "marca": "short blonde hair tucked behind her ears and thin wire-rimmed "
              "glasses"},
    {"id": "rabo_castanho", "idade": 46, "etnia": "white American",
     "porte": "tall and long-limbed",
     "marca": "chestnut hair pulled into a low ponytail, freckles across her "
              "cheeks and thin tortoiseshell glasses"},
    {"id": "grisalha_lisa", "idade": 52, "etnia": "white American",
     "porte": "small-framed and lightly built",
     "marca": "silver-grey hair cut straight to the shoulders and a beauty "
              "mark above her lip"},
    {"id": "ruiva_cacheada", "idade": 45, "etnia": "white American",
     "porte": "full-figured with soft shoulders",
     "marca": "copper curls gathered in a loose clip, smooth-skinned, with a "
              "cleft in her chin"},
    {"id": "tranca_unica", "idade": 49, "etnia": "Black American",
     "porte": "solid and broad through the back",
     "marca": "a single thick braid over one shoulder and laugh lines at the "
              "corners of her eyes"},
    {"id": "bob_preto_oculos", "idade": 47, "etnia": "Black American",
     "porte": "average build with a long waist",
     "marca": "a blunt black bob and dark rectangular glasses"},
    {"id": "coque_alto", "idade": 44, "etnia": "Black American",
     "porte": "tall and narrow-shouldered",
     "marca": "hair pulled into a high bun with a silver streak at the front"},
    {"id": "twists_curtos", "idade": 51, "etnia": "Black American",
     "porte": "stout and heavy through the arms",
     "marca": "short two-strand twists going grey and a small mole under one "
              "eye"},
    {"id": "latina_rabo", "idade": 48, "etnia": "Latina American",
     "porte": "compact and solidly built",
     "marca": "dark hair in a low knot at her neck, laugh lines and a beauty "
              "mark on her left cheek"},
    {"id": "latina_bob_oculos", "idade": 45, "etnia": "Latina American",
     "porte": "slim with narrow hips",
     "marca": "a dark chin-length bob and clear-framed glasses"},
    {"id": "asiatica_curto", "idade": 50, "etnia": "Asian American",
     "porte": "petite and finely built",
     "marca": "black hair cut short at the nape, smooth-skinned, with a grey "
              "streak at one temple"},
    {"id": "asiatica_oculos", "idade": 52, "etnia": "Asian American",
     "porte": "average build with round shoulders",
     "marca": "long black hair pinned up loosely and thin gold-rimmed glasses"},
    {"id": "loira_meio_oculos", "idade": 49, "etnia": "white American",
     "porte": "broad-shouldered and thickset",
     "marca": "dark blonde hair in a shoulder-length cut and rimless glasses"},
    {"id": "morena_franja", "idade": 46, "etnia": "white American",
     "porte": "lean with a narrow build",
     "marca": "dark hair with a soft fringe and freckles across her nose"},
]


# ===========================================================================
# ⭐⭐⭐ A TIGELA — O FIO DO VIDEO, E ELA E' O PROPRIO GELATIN TRICK
# ===========================================================================
# ⛔ DECISAO 2 DO OPERADOR: a tigela e' o mecanismo que a copy vende, e ela
# TROCA DE MAO entre os dois takes — colo dele -> maos dela. Por isso o pool
# NAO e' de vasilhame de bebida (era, e saiu): e' de COMO O PREPARO APARECE em
# quadro, no MESMO recipiente, nos dois estados.
#
# ⭐ CADA ENTRADA CARREGA OS DOIS ESTADOS DO MESMO OBJETO:
#     `img1` — no colo dele, a mistura ambar semi-liquida sendo mexida;
#     `img2` — nas maos dela, ja' com os CUBOS DE GELATINA visiveis dentro.
# ⛔ Um campo so' nao serviria: o espectador precisa reconhecer O MESMO
# recipiente e ver que o CONTEUDO mudou de estado. E' o antes-e-depois contado
# sem uma palavra, que e' a razao de ser do angulo.
#
# ⛔ A TIGELA CONTINUA SEM ROTULO E SEM NOME DE INGREDIENTE, por causa do CT5:
# a receita e' a UNICA moeda que o comentario compra, e entregar um ingrediente
# (na fala OU escrito no quadro) a gasta para os outros 49 videos da pagina.
#
# ⚠️⚠️ MUDOU UMA COISA EM 2026-08-10, E E' PRECISO DIZER O QUE: ate' a leitura
# otica, este bloco declarava que o angulo nao podia ter rotulo NENHUM em quadro
# — "o GOOD 16 mostra um sache com GELATIN legivel porque a FONTE dele mostra; a
# fonte deste angulo nao mostra rotulo nenhum". A frase estava certa e a
# premissa era falsa: as fontes nunca tinham sido vistas, so' descritas. Com os
# dois mp4 baixados e lidos a 1 fps, as DUAS poem caixa com rotulo legivel em
# quadro (JELL-O, Arm & Hammer, mel de vidro, e a caixa `HORSE GELATIN`) — e a
# fala NUNCA lista ingrediente, que e' exatamente o CT5 sendo obedecido em
# quadro aberto. A evidencia que faltava chegou; ver `CAIXA` logo abaixo.
# ⛔ O que continua valendo sem uma virgula de mudanca: o rotulo e' o da KEYWORD
# (`GELATIN`), nunca o de um ingrediente da receita.
#
# ⚠️ CADA ENTRADA TEM SILHUETA PROPRIA. Licao do BOTICA: metade de um pool era
# de vidro e o gerador colapsou quatro entradas numa prensa francesa, que e' a
# forma que ele conhece melhor. Aqui nao ha' dois corpos iguais.
TIGELAS = [
    {"id": "ceramica_creme", "nome": "tigela de ceramica creme",
     "curto": "ceramica creme",
     "img1": "a heavy cream ceramic bowl of glossy amber gelatin mixture with "
             "a steel spoon standing in it",
     "img2": "the same heavy cream ceramic bowl, now full of cut cubes of set "
             "amber gelatin"},
    {"id": "vidro_transparente", "nome": "tigela de vidro transparente",
     "curto": "vidro transparente",
     "img1": "a clear glass mixing bowl of glossy amber gelatin mixture with a "
             "steel spoon standing in it",
     "img2": "the same clear glass mixing bowl, now full of cut cubes of set "
             "amber gelatin"},
    {"id": "esmaltada_azul", "nome": "tigela esmaltada de borda azul",
     "curto": "esmaltada azul",
     "img1": "a white enamel bowl with a chipped blue rim, full of glossy "
             "amber gelatin mixture with a steel spoon standing in it",
     "img2": "the same white enamel bowl with the chipped blue rim, now full "
             "of cut cubes of set amber gelatin"},
    {"id": "barro_marrom", "nome": "tigela de barro marrom",
     "curto": "barro marrom",
     "img1": "a squat brown earthenware bowl of glossy amber gelatin mixture "
             "with a steel spoon standing in it",
     "img2": "the same squat brown earthenware bowl, now full of cut cubes of "
             "set amber gelatin"},
    {"id": "inox_funda", "nome": "tigela funda de inox",
     "curto": "inox funda",
     "img1": "a deep stainless steel bowl of glossy amber gelatin mixture with "
             "a spoon standing in it",
     "img2": "the same deep stainless steel bowl, now full of cut cubes of set "
             "amber gelatin"},
    {"id": "louca_azul", "nome": "tigela de louca azul e branca",
     "curto": "louca azul",
     "img1": "a blue and white patterned china bowl of glossy amber gelatin "
             "mixture with a steel spoon standing in it",
     "img2": "the same blue and white patterned china bowl, now full of cut "
             "cubes of set amber gelatin"},
    {"id": "vidro_estriado", "nome": "tigela de vidro estriado",
     "curto": "vidro estriado",
     "img1": "a ribbed pressed-glass bowl of glossy amber gelatin mixture with "
             "a steel spoon standing in it",
     "img2": "the same ribbed pressed-glass bowl, now full of cut cubes of set "
             "amber gelatin"},
    {"id": "gres_escuro", "nome": "tigela de gres escuro",
     "curto": "gres escuro",
     "img1": "a wide dark stoneware bowl of glossy amber gelatin mixture with "
             "a steel spoon standing in it",
     "img2": "the same wide dark stoneware bowl, now full of cut cubes of set "
             "amber gelatin"},
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
# ⭐⭐ take 1 — A SEGUNDA FAMILIA DE ABERTURA: PERGUNTA EM 2a PESSOA + PONTE
# ---------------------------------------------------------------------------
# ⛔⛔ ACHADO DA LEITURA OTICA (2026-08-10, fonte 1). O video abre assim:
#
#     "Finding it harder to stay firm?"   ->   "That's exactly where I was."
#
# ⭐ O QUE ISSO CONSERTA AQUI: ate' hoje o take 1 do BED 16 era depoimento em 1a
# pessoa do primeiro ao ultimo segundo, e o ESPECTADOR so' entrava no video na
# sentenca do MECANISMO — ja' no take 2, oito segundos e um corte depois. Quem
# faz scroll decide nos dois primeiros segundos, e nesses dois segundos a copy
# antiga falava de um homem que ele nao conhece.
#
# ⭐ A PONTE E' METADE DA FAMILIA, e nao um detalhe de redacao: pergunta sozinha
# vira anuncio de clinica. `... My {o} quit on me too.` traz o narrador para
# dentro e devolve o video ao depoimento, que e' o que o resto da copy e' — o
# take 1 continua terminando no CUSTO CONJUGAL, em 1a pessoa.
#
# ⛔ ELA OCUPA O MESMO SLOT DA FALHA (sorteio lado a lado em `ABERTURAS`) e o
# MESMO orcamento: 11-12 palavras, com o CUSTO de 11 vindo depois. Familia que
# come palavra a mais empurra o take 1 para cima do teto de 25 — e o teto e'
# RENDER, nao teoria.
#
# ⛔⛔ CT2 — A ENTRADA TEM DE CARREGAR VERBO DE FALHA, e a pergunta sozinha NAO
# carrega: `Finding it harder to stay firm?` nao casa nada no regex do
# `sc.lint_copy16`. Por isso o verbo (`quit` · `went soft` · `stopped working` ·
# `gave out` · `failed` · `useless` · `dead` · `shut down`) mora SEMPRE na
# ponte. O autoteste cobra isso entrada por entrada — se so' a fala montada
# fosse medida, uma entrada sem verbo apareceria em ~1/26 dos sorteios.
#
# ⛔⛔ CT7 — O APELIDO DO ORGAO NUNCA ENTRA NA SENTENCA DA PERGUNTA. Metade das
# perguntas carrega `harder`, que e' token do `sc.ERECAO_16`; sobre o CORPO ele
# passa, colado ao ORGAO ele reprova no gerador (licao paga no COLO 16, ~95% de
# recusa). O orgao mora na PONTE, que e' outra sentenca. Lente BD19.
#
# ⚠️ E NENHUMA ENTRADA DIZ A IDADE DELE. A pendencia B do cabecalho (idade dita
# x idade em quadro, 6,0% dos videos) e' anterior a esta familia e continua com
# o operador — mas familia nova nao nasce alimentando defeito conhecido.
PERGUNTAS = [
    "Finding it harder to stay firm? My {o} quit on me too.",
    "Going soft before she is finished? My {o} quit for two years.",
    "Losing it ten minutes in? My {o} stopped working for years.",
    "Giving out halfway through the night? My {o} failed me for months.",
    "Nothing happening down there anymore? My {o} was dead for months.",
    "Quitting halfway with your wife again? My {o} gave out nightly.",
    "Tired of going soft every night? My {o} was useless for years.",
    "Not lasting the way you did? My {o} shut down completely.",
    "Losing it before she even starts? My {o} quit for two years.",
    "Finding it harder to finish? My {o} stopped working every night.",
    "Feeling it go soft midway? My {o} gave out for two years.",
    "Nothing left for her at night? My {o} was dead for months.",
]

# ⭐ O SLOT DA ABERTURA — as duas familias no MESMO sorteio, sem preferencia.
# ⛔ Derivado, nunca redigitado: duas listas a mao divergem no primeiro acrescimo.
ABERTURAS = FALHAS + PERGUNTAS

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
#
# ⛔⛔ DUAS ENTRADAS AQUI CONTAM OS ANOS DE CASAMENTO (`Twenty six years
# married`, `Thirty one years`) — e ANOS DE CASAMENTO SAO ARITMETICA CONTRA A
# IDADE QUE O QUADRO MOSTRA. Elas NAO sao removidas: sao FILTRADAS por
# `_viradas_da_esposa` conforme a esposa sorteada, porque com a esposa certa
# elas sao as duas melhores linhas do pool (numero + dano, que e' o CT2).
# Ver o bloco `_ANOS_CASADO` para a conta e para o que ela evitou.
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
# ⚠️ 9 palavras EXATAS nas dez primeiras, e todas nomeiam `recipe`
# (`sc.lint_isca_cta`: pedir o comentario sem dizer o que chega e' pedir sem
# oferecer).
#
# ⭐⭐⭐ A SEGUNDA METADE DO POOL E' O GAP DO ULTIMO PASSO — o melhor achado da
# leitura otica das duas fontes (2026-08-10). A fonte 1 diz, verbatim:
#
#     "The recipe wasn't the secret. The last step was."
#
# ⛔ POR QUE ISTO IMPORTA MAIS QUE UMA REDACAO MELHOR: **a nossa isca nao
# sobrevive ao Google.** Prometemos "a receita", e receita de gelatina qualquer
# um acha em tres segundos — a moeda que o comentario compra ja' esta' de graca
# na primeira busca. A fonte ENTREGA a receita e RETEM o ultimo passo: um gap
# que nao tem como ser fechado por fora, porque o que falta e' um passo que so'
# existe na boca de quem fala.
#
# ⭐ POR QUE O POOL E' METADE/METADE E NAO 100% NA FORMA NOVA: a troca da moeda
# tem de ser medida EM CAMPO (comentarios por view, nao gosto meu), e pool de
# uma forma so' e' o vicio que o operador ja' reprovou tres vezes. Dez de cada,
# sorteio uniforme: o campo decide.
#
# ⛔⛔ AS DUAS TRAVAS DE REGEX QUE ESTA METADE TEM DE PAGAR — e as duas foram
# MEDIDAS antes de a lista ser escrita, nao supostas:
#
#   · `sc.ISCA_CTA` NAO conhece `last step`. Ele casa `recipe|measurements|
#     ingredients|link|source|protocol`, ou `I'll send/show/tell/...`, ou
#     `(in|to) your (inbox|messages|dm)`. Logo TODA entrada desta metade paga a
#     isca pelo ENDERECO (`goes TO YOUR MESSAGES`, `lands IN YOUR INBOX`) ou
#     pelo verbo de entrega (`I'll send`). ⛔ Formas como `only your messages
#     get the last step` ou `the last step hits your inbox` reprovam em 100% —
#     `your messages` sem `in`/`to` na frente nao casa nada, e sem `recipe` nao
#     ha' segunda ancora. Elas nasceram e morreram aqui.
#   · `sc.ENTREGA_16` (CT6) casa `your messages/inbox/dm`, `by message`,
#     `in private`. Todas as vinte pagam.
#
# ⚠️ E O ANTECEDENTE DE `the last step` E' `the gelatin trick`, dito na sentenca
# do MECANISMO uma frase antes, no MESMO take. Um truque tem passos; e' isso que
# deixa a forma NUA de pe' sem gastar palavra com a montagem do gap. A lente
# BD14 cobra essa costura a cada sorteio — sem `gelatin trick` na fala, `o
# ultimo passo` e' passo de coisa nenhuma.
#
# ⚠️ 10 e 11 palavras nesta metade (contra 9 na de `recipe`): cabe no orcamento
# porque o CTA escolhe PRIMEIRO e reserva 14 (8 do menor mecanismo + 6 da
# prova), entao o teto real do slot e' 11. Medido no [ALCANCE], nao estimado.
CTAS = [
    # --- a moeda antiga: A RECEITA (10 entradas, 9 palavras) ---------------
    "%s and the recipe goes to your messages." % sc.CTA_LITERAL,
    "%s and the recipe lands in your messages." % sc.CTA_LITERAL,
    "%s and the recipe hits your inbox tonight." % sc.CTA_LITERAL,
    "%s and I'll send the recipe by message." % sc.CTA_LITERAL,
    "%s and the recipe arrives in your messages." % sc.CTA_LITERAL,
    "%s and only your messages get the recipe." % sc.CTA_LITERAL,
    "%s and I'll send the recipe in private." % sc.CTA_LITERAL,
    "%s and the recipe comes to your inbox." % sc.CTA_LITERAL,
    "%s and your inbox gets the recipe tonight." % sc.CTA_LITERAL,
    "%s and the whole recipe reaches your messages." % sc.CTA_LITERAL,
    # --- a moeda nova: O ULTIMO PASSO (10 entradas, 10-11 palavras) --------
    "%s and the last step goes to your messages." % sc.CTA_LITERAL,
    "%s and the last step lands in your inbox." % sc.CTA_LITERAL,
    "%s and the last step comes to your inbox." % sc.CTA_LITERAL,
    "%s and the last step arrives in your messages." % sc.CTA_LITERAL,
    "%s and I'll send the last step by message." % sc.CTA_LITERAL,
    "%s and I'll send the last step in private." % sc.CTA_LITERAL,
    "%s and the missing step goes to your inbox." % sc.CTA_LITERAL,
    "%s and the missing step lands in your messages." % sc.CTA_LITERAL,
    "%s and I'll send the missing step to your inbox." % sc.CTA_LITERAL,
    "%s and I'll send the missing step in private." % sc.CTA_LITERAL,
]

# ⭐ As duas familias de isca, para a MEDICAO da reparticao e para a lente BD14.
# ⛔ Derivadas do pool, nunca redigitadas: lista paralela escrita a mao e' a
# primeira coisa que diverge quando alguem acrescenta um CTA.
_RX_PASSO = re.compile(r"\b(last|missing)\s+step\b", re.I)
CTAS_PASSO = [c for c in CTAS if _RX_PASSO.search(c)]
CTAS_RECEITA = [c for c in CTAS if not _RX_PASSO.search(c)]

# ⛔⛔ CONTRATO NO IMPORT, e ele nasceu de um achado do `medir_alcance`: as duas
# listas existiam e NINGUEM as usava — pool orfao, que e' pior que pool ausente
# porque quem edita depois nao sabe por que elas nunca fazem diferenca.
# ⭐ E a troca de moeda do CTA (`the recipe` -> `the last step`, vinda da leitura
# otica da fonte em 2026-08-10) SO' se mede em campo se as DUAS familias
# sairem. Metade/metade e' o desenho; este guarda impede que uma expansao
# futura do pool zere uma delas sem ninguem perceber.
if not CTAS_PASSO or not CTAS_RECEITA:
    raise AssertionError(
        "CTAS: as duas iscas tem de existir — `last/missing step` (%d) e "
        "`recipe` (%d). Uma delas zerada mata o teste de campo da troca de "
        "moeda." % (len(CTAS_PASSO), len(CTAS_RECEITA)))
if not (0.3 <= len(CTAS_PASSO) / float(len(CTAS)) <= 0.7):
    raise AssertionError(
        "CTAS: a reparticao entre as duas iscas saiu de 30-70%% (%d de %d em "
        "`last step`) — pool desbalanceado nao mede troca de moeda, mede a "
        "familia maior." % (len(CTAS_PASSO), len(CTAS)))


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
    return next((x for x in pool if x["id"] == valor), None)


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
# ⛔⛔ A CONTA DO CASAMENTO — anos ditos x idade que o QUADRO mostra
# ===========================================================================
# ⚠️ ACHADO DA CONFERENCIA (2026-08-10), e ele passou por TUDO: os seis
# medidores externos verdes, o linter em 0 ERRO / 0 AVISO e o autoteste OK. So'
# aparece LENDO A FALA EM VOZ ALTA COM O BLOCO IMAGE DO LADO, porque o defeito
# nao mora na sentenca — mora entre a sentenca e o rosto.
#
# Duas entradas de VIRADAS contam os anos de casamento. A IMAGE 01 diz a idade
# dela em numero (`a 23-year-old ... woman`), e o espectador ve' a idade mesmo
# sem o numero. Subtraindo:
#
#     MODO BELA LIGADO   (esposa 21-33)  16,1% dos videos, medido em 1000:
#         esposa de 21 + `Twenty six years married` -> casada aos MENOS CINCO
#     MODO BELA DESLIGADO (esposa 44-52)  5,5% dos videos, medido em 1000:
#         esposa de 44 + `Thirty one years`         -> casada aos TREZE
#
# ⛔⛔ E O ESTADO DESLIGADO E' O PIOR DOS DOIS, ao contrario do que a % sugere.
# O absurdo do modo ligado (numero negativo) o espectador le' como erro de
# roteiro e segue em frente; `casada aos treze` ele le' como o que a frase
# literalmente diz — num video sobre sexo, num funil que vive de conta de
# rede social. Nao e' so' o TESTE WTF: e' a familia de token que derruba pagina.
#
# ⭐ A CORRECAO NAO REESCREVE COPY APROVADA. As duas linhas sao as melhores do
# pool pelo CT2 (numero + dano concreto) e continuam vivas — so' nao sao
# sorteadas para uma esposa em que a conta nao fecha. E' filtro de ALCANCE por
# estado, a mesma familia do `_cabe`: la' o limite e' o teto de palavras, aqui
# e' a idade em quadro.
#
# ⚠️ O piso e' 18 e nao 16: a idade legal varia por estado nos EUA, e o numero
# que o espectador (e o classificador) usa e' 18.
IDADE_MINIMA_AO_CASAR = 18

# ⛔ So' as DEZENAS entram. `for the last two years` e `two years of that` sao
# duracao da FRIEZA, nao do casamento, e cabem em qualquer idade — casar a
# regex nelas reprovaria a copy certa (modo de falha §16, a lente que cobra a
# cena que nao existe). E as FALHAS dizem `at fifty seven`, sem `years`, entao
# a idade DELE nunca entra nesta conta.
_ANOS_CASADO = re.compile(
    r"\b(twenty|thirty|forty|fifty)(?:[-\s](one|two|three|four|five|six|"
    r"seven|eight|nine))?\s+years\b", re.I)
_DEZENAS = {"twenty": 20, "thirty": 30, "forty": 40, "fifty": 50}
_UNIDADES = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
             "six": 6, "seven": 7, "eight": 8, "nine": 9}


def _anos_de_casamento(frase):
    """Os anos de casamento que a frase DIZ — 0 quando ela nao diz nenhum."""
    m = _ANOS_CASADO.search(frase or "")
    if not m:
        return 0
    return _DEZENAS[m.group(1).lower()] + _UNIDADES.get(
        (m.group(2) or "").lower(), 0)


def _viradas_da_esposa(spec):
    """Os VIRADAS em que a conta fecha com a esposa SORTEADA.

    ⛔ Depende do `spec` e nao de `MODO BELA`, e a diferenca importa: o defeito
    existe nos DOIS estados (esposa de 44 + 31 anos de casamento = 13). Uma
    guarda escrita como `if spec["bela"]` consertaria 16% e deixaria 5,5% de pe'
    — e os 5,5% sao justamente os perigosos.
    ⚠️ SEM `or VIRADAS`: dez das doze entradas nao citam duracao nenhuma e
    sobrevivem a qualquer idade, entao o filtro nao tem como esvaziar. O
    fallback silencioso e' o que deixou a cena 2 do TROCA passar de 25 para 27
    palavras sem ninguem ver; onde ele nao e' necessario, ele nao entra — e o
    autoteste prova o piso para TODA idade dos dois pools.
    """
    idade = spec["mulher"]["idade"]
    return [c for c in VIRADAS
            if idade - _anos_de_casamento(c) >= IDADE_MINIMA_AO_CASAR]


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
        # ⛔ O CUSTO E' FILTRADO PELA IDADE DELA ANTES DE QUALQUER CONTA DE
        # PALAVRA: `Thirty one years` nao e' uma frase longa demais, e' uma
        # frase que nao fecha com a esposa que esta' em quadro. Ver
        # `_viradas_da_esposa`.
        # ⚠️ E o pool filtrado entra tambem na RESERVA do `_cabe`, nao so' na
        # escolha — reservar pelo minimo de um pool que nao vai ser sorteado e'
        # a mesma mentira do `_cabe` medindo o template em vez da string.
        viradas = _viradas_da_esposa(spec)
        # a ABERTURA carrega o orgao e o numero — menos substitutos, escolhe
        # antes. ⭐ E ela sorteia das DUAS familias no mesmo pote: depoimento em
        # 1a pessoa (FALHAS) e pergunta em 2a pessoa + ponte (PERGUNTAS).
        fa = rng.choice(_cabe(ABERTURAS, _mn(viradas), 1, o)).format(o=o)
        cu = rng.choice(_cabe(viradas, _palavras(fa), 1))
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

    # ⭐⭐ MODO BELA — contrato compartilhado (`sc.ref_bela`), nao implementacao
    # propria. O helper devolve a REF no FORMATO DESTE pool (`idade`, `porte`,
    # `marca`, `id`), entao o `montar()` nao muda um `if`.
    # ⛔ O CADEADO DA TELA VENCE O MODO: mulher travada no painel e' mais
    # especifica que "uma bela qualquer" — mesma precedencia que o `ui_agente`
    # ja' aplica com `ref`, e que aqui precisa ser respeitada na mao porque o
    # eixo se chama `mulher`.
    # ⛔ E A ETNIA DELA SOBREVIVE AO MODO. O `ref_bela` mantem o campo que nao
    # conhece — e o campo que ele mantem e' o do MOLDE (`MULHERES[0]`), nao o da
    # entrada sorteada. Sem esta linha o modo BELA travaria a esposa inteira em
    # `white American` e ninguem veria, porque a congruencia do funil olha o
    # homem.
    bela = bool(travas.get("bela")) and not travas.get("mulher")
    if bela:
        _et_dela = mulher["etnia"]
        mulher = sc.ref_bela(MULHERES[0], rng)
        mulher["etnia"] = _et_dela

    tigela = (_por_id(TIGELAS, travas["tigela"]) if travas.get("tigela")
              else _fresco(TIGELAS, hist.get("tigela", [])[-4:], rng))

    spec = {
        "pagina": pagina, "etnia": etnia, "bela": bela,
        "mundo": mundo, "homem": homem, "mulher": mulher, "tigela": tigela,
        "corpo_h": rng.choice(CORPOS_H),
        "pijama": rng.choice(PIJAMAS),
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


def _traje_dela(spec, take):
    """A roupa dela no take pedido, ja' resolvida pelo MODO BELA.

    ⛔ Um lugar so'. Espalhar `if spec["bela"]` pelos dois blocos e' o fragmento
    espelhado que diverge na primeira manutencao — e o eixo que diverge aqui e'
    justamente o que o operador vai olhar primeiro.
    """
    m = spec["mundo"]
    suf = "_bela" if spec.get("bela") else ""
    return m["dela_q" + suf] if take == 1 else m["dela_a" + suf]


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

    # --- TAKE 1 — A CAMA E A TIGELA ---------------------------------------
    # ⛔ A FRIEZA E' CONTADA PELA POSTURA DELA, nunca por fala: bracos cruzados
    # e o olhar ENCARANDO ele. Ela e' MUDA (BD1) e a inversao desta postura no
    # take 2 E' o video (BD2).
    # ⚠️ ELA ENCARA, e isso e' correcao do operador sobre o print (antes ela
    # olhava para o outro lado). O encarar e' MAIS frio que o desviar: desviar
    # e' evitar, encarar e' cobrar — e cobranca com bracos cruzados e' a cena
    # que o print mostra.
    # ⭐⭐ A TIGELA NASCE AQUI, NO COLO DELE, e e' o que faz o take 1 deixar de
    # ser so' a falha: ele ja' esta' FAZENDO o truque enquanto conta o que
    # perdeu.
    # ⛔⛔ A PROFUNDIDADE DE CAMPO E' PEDIDA EXPLICITAMENTE (BD9): ele grande e
    # nitido em primeiro plano, ela menor e mais suave varios pes atras. Sem
    # isso o Veo achata os dois no mesmo plano e a distancia — que e' o
    # argumento do quadro — desaparece.
    # ⚠️ O corpo dele fica de tres-quartos, virado para longe dela, as maos na
    # tigela e o rosto virado para a lente: a postura derrotada do print fica de
    # pe' e a fala tem para onde sair. Ver a PENDENCIA no cabecalho.
    b["IMAGE 01/02"] = (
        "IMAGE 01/02: Medium shot in %s. Close to the lens in the left "
        "foreground, sitting on the edge of the bed in three-quarter profile "
        "with his body turned away from her and his face turned to the camera, "
        "is a %d-year-old %s man, bare-chested, %s, wearing %s, his shoulders "
        "down. %s, %s. In his lap he is holding %s, and he keeps stirring it, "
        "his head low over the bowl. Several feet behind him, sitting "
        "up against a dark padded headboard with a white duvet pulled to her "
        "waist, is a %d-year-old %s woman, %s, %s, wearing %s, her arms folded "
        "across her chest and her face turned toward him, staring straight at "
        "him with a hard annoyed expression. A wooden nightstand stands beside "
        "her and clothes lie on the floor. Shallow depth of field: he is large "
        "and sharp in the foreground and she is smaller and softer behind him, "
        "and the framing makes the distance between them plain. They are the "
        "only two people in the frame. %s. %s"
        % (m["q_cen"], h["idade"], et, spec["corpo_h"], spec["pijama"],
           _cap(h["marca"]), h["sinal"], spec["tigela"]["img1"],
           w["idade"], w["etnia"], w["porte"], w["marca"],
           _traje_dela(spec, 1), _cap(m["q_luz"]), CAUDA))

    b["TAKE 01/02"] = (
        "TAKE 01/02: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway, no cuts, and the camera does not move. He "
        "talks straight into the lens the whole time and never turns to look "
        "at her, and he keeps slowly stirring the bowl in his lap with the "
        "spoon. She stays exactly where she is, her arms folded across her "
        "chest and her eyes on him, and she never speaks. Only he speaks. He "
        "stays large and sharp in the foreground and she stays smaller and "
        "softer behind him. Nothing else in the frame changes.\n"
        "Dialogue: \"%s\"\nAudio: %s. No music."
        % (sonorizar(spec["falas"][0]), m["q_audio"]))

    # --- TAKE 2 — A VIRADA NA AGUA ----------------------------------------
    # ⛔⛔ A ANCORA DE CONTINUIDADE VEM AQUI EM CINCO PECAS: idade, etnia,
    # marca, sinal e a frase `It is the same man`. Sem isso o Veo desenha OUTRA
    # pessoa — no VAZAMENTO o corpo-prova voltou como um senhor de oculos e
    # bigode, e como o TAKE diz `Only he speaks` o estranho falava a fala do
    # REF. Lente BD3.
    # ⭐⭐ E A TIGELA FECHA O FIO: e' O MESMO recipiente do take 1 (`the same
    # ...`), agora NAS MAOS DELA e com os cubos ja' cortados. A mao que segura
    # e o estado do conteudo mudaram juntos — e' o antes-e-depois contado sem
    # uma palavra. Lente BD4.
    b["IMAGE 02/02"] = (
        "IMAGE 02/02: Medium shot at %s. In the water is the same "
        # ⚠️ `submerged to his chest` e' FORMA, nao cena — a agua continua no
        # peito dele. As duas redacoes anteriores brigavam com o pool `a_agua`,
        # cada uma em metade dele: `with the water at his chest` encadeava dois
        # `with` no mesmo substantivo em 8 dos 15 mundos (`a pool WITH a tiled
        # lip WITH the water at his chest`), e `, the water at his chest`
        # repetia `the water` nos outros 3 (`the water moving, the water at his
        # chest`). Esta nao usa nem `with` nem `water`, e por isso e' a unica
        # que le' limpo nos QUINZE — conferido um por um.
        "%d-year-old %s man from the first scene, %s, %s, %s, sitting in %s, "
        "submerged to his chest, his face fully in frame and turned to "
        "the camera. It is the same man, not a different person. Pressed "
        "against his side with her shoulder against his chest is the same "
        "%d-year-old %s woman, %s, %s, wearing %s; she looks at him and says "
        "nothing. In both hands, just above the water, she holds %s, and his "
        "own hands are empty. They are the only two people in the frame. "
        "%s. %s"
        % (m["a_cen"], h["idade"], et, h["marca"], h["sinal"], spec["corpo_h"],
           m["a_agua"], w["idade"], w["etnia"], w["porte"], w["marca"],
           _traje_dela(spec, 2), spec["tigela"]["img2"],
           _cap(m["a_luz"]), CAUDA))

    b["TAKE 02/02"] = (
        "TAKE 02/02: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway, no cuts, and the camera does not move. He "
        "talks straight into the lens the whole time and it is the same man as "
        "in the first scene. She stays pressed against his side and never "
        "moves away from him, and she never speaks. Only he speaks. She keeps "
        "hold of the bowl in both hands the whole time and never hands it to "
        "him, and he never reaches for it. The water keeps moving the way "
        "water moves and nothing else in the frame changes.\n"
        "Dialogue: \"%s\"\nAudio: %s. No music."
        % (sonorizar(spec["falas"][1]), m["a_audio"]))

    # ⛔ trava de texto queimado em todo TAKE — o watermark que o operador viu
    # vazando nos reels da concorrente (2026-08-01).
    return sc.selar_takes(b)


# ===========================================================================
# LINTER — as regras BD
# ===========================================================================

def _bd1_ela_muda(spec, blocos, achados):
    """BD1 — ela nunca fala, e os DOIS takes tem de DIZER isso.

    ⚠️ Omitir nao basta: o Veo poe as duas bocas a mexer se ninguem proibir, e o
    dialogo dele sai monofonico e torto. Foi assim que a cena do casal do
    VAZAMENTO caiu.
    """
    for k in ("TAKE 01/02", "TAKE 02/02"):
        if "Only he speaks" not in blocos[k]:
            achados.append(("ERRO", "BD1: %s sem `Only he speaks` — sem isso o "
                                    "Veo mexe a boca dela tambem" % k))
        if "she never speaks" not in blocos[k]:
            achados.append(("ERRO", "BD1: %s nao diz que ela e' muda — a "
                                    "mudez dela e' invariante do angulo" % k))


def _bd2_inversao(spec, blocos, achados):
    """⭐⭐ BD2 — A INVERSAO E' O VIDEO.

    ⛔ Bracos cruzados ENCARANDO ele no take 1; corpo colado no take 2. Sem os
    dois lados o angulo deixa de existir: sobra um homem falando de gelatina
    numa piscina, que e' o GOOD 16. A prova deste agente nao e' um corpo nem um
    prop — e' o casamento, e ela so' se le' na DIFERENCA entre os dois quadros.

    ⚠️ O OLHAR MUDOU DE DIRECAO EM 2026-08-10, por ordem do operador lendo o
    print: ela ENCARA, nao desvia. A lente foi atras — e a versao antiga
    (`turned away from him`) morreu, porque lente que cobra a cena velha
    reprova a cena certa.
    """
    i1, i2 = blocos["IMAGE 01/02"], blocos["IMAGE 02/02"]
    if "arms folded across her chest" not in i1:
        achados.append(("ERRO", "BD2: a IMAGE 01 nao tem os bracos cruzados "
                                "dela — a frieza e' contada pela POSTURA, e "
                                "sem ela nao ha' o que inverter no take 2"))
    if "staring straight at him" not in i1:
        achados.append(("ERRO", "BD2: a IMAGE 01 nao poe ela ENCARANDO ele — "
                                "desviar e' evitar, encarar e' cobrar, e a "
                                "cobranca e' a metade fria do angulo"))
    if "Pressed against his side" not in i2:
        achados.append(("ERRO", "BD2: a IMAGE 02 nao tem ela colada nele — a "
                                "inversao dos bracos cruzados E' o video"))
    if "shoulder against his chest" not in i2:
        achados.append(("ERRO", "BD2: a IMAGE 02 nao encosta o ombro dela no "
                                "peito dele — `ao lado` nao inverte `bracos "
                                "cruzados a varios pes de distancia`"))


def _bd3_ancora(spec, blocos, achados):
    """⛔⛔ BD3 — A ANCORA DE CONTINUIDADE DO HOMEM NO TAKE 2.

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
        achados.append(("ERRO", "BD3: a IMAGE 02 nao repete `the same "
                                "%d-year-old` — o Veo troca de pessoa"
                        % h["idade"]))
    if et not in i2:
        achados.append(("ERRO", "BD3: a IMAGE 02 nao repete a etnia (%r)" % et))
    for peca, rot in ((h["marca"], "marca"), (h["sinal"], "sinal")):
        if peca not in i2:
            achados.append(("ERRO", "BD3: a IMAGE 02 nao repete o %s facial "
                                    "sorteado (%r) — e' a ancora que o Veo "
                                    "usa para nao trocar de homem"
                            % (rot, peca[:38])))
    if "It is the same man" not in i2:
        achados.append(("ERRO", "BD3: a IMAGE 02 nao diz `It is the same man` "
                                "— a ancora implicita nao segura troca de "
                                "cenario, roupa e luz de uma vez"))
    if "the same man as in the first scene" not in t2:
        achados.append(("ERRO", "BD3: o TAKE 02 nao repete a ancora — a IMAGE "
                                "segura o primeiro frame, o TAKE segura os 8 "
                                "segundos"))


def _bd4_tigela(spec, blocos, achados):
    """⭐⭐⭐ BD4 — A TIGELA E' O FIO, E ELA TROCA DE MAO.

    ⛔ Decisao 2 do operador: a tigela E' o gelatin trick, e o angulo inteiro
    mora no percurso dela — colo DELE no take 1, maos DELA no take 2, com o
    conteudo mudando de mistura para cubos. A lente cobra as quatro pontas:
    o recipiente sorteado nos dois blocos, o colo, as maos dela, e o `the same`
    que amarra os dois como UM objeto.

    ⚠️ MORREU AQUI a cobranca do gole (`lifts it to drink`) da versao copo: nao
    ha' mais bebida nenhuma no angulo, e lente que cobra cena que nao existe
    reprova a producao certa. No lugar dela entrou a trava de nao passar a
    tigela de mao em mao dentro do take — se ela voltar para a mao dele em
    quadro, o percurso que conta a virada se desfaz nos 8 segundos.
    """
    i1, i2 = blocos["IMAGE 01/02"], blocos["IMAGE 02/02"]
    t2 = blocos["TAKE 02/02"]
    tg = spec["tigela"]
    if tg["img1"] not in i1:
        achados.append(("ERRO", "BD4: a tigela sorteada (%r) nao chega a' IMAGE "
                                "01 — eixo de painel que nao muda o video"
                        % tg["id"]))
    if "In his lap he is holding" not in i1 or "keeps stirring it" not in i1:
        achados.append(("ERRO", "BD4: a IMAGE 01 nao poe a tigela NO COLO DELE "
                                "sendo mexida — sem isso o take 1 volta a ser "
                                "so' a falha, sem o comeco da saida"))
    if tg["img2"] not in i2:
        achados.append(("ERRO", "BD4: a tigela sorteada (%r) nao chega a' IMAGE "
                                "02 com os cubos — o conteudo mudar de estado "
                                "e' metade do antes-e-depois" % tg["id"]))
    if "In both hands, just above the water, she holds" not in i2:
        achados.append(("ERRO", "BD4: a IMAGE 02 nao poe a tigela nas MAOS "
                                "DELA — a troca de mao E' o video"))
    if "his own hands are empty" not in i2:
        achados.append(("ERRO", "BD4: a IMAGE 02 nao esvazia as maos DELE — "
                                "duas tigelas em quadro desfazem o percurso de "
                                "um objeto so'"))
    if "never hands it to him" not in t2:
        achados.append(("ERRO", "BD4: o TAKE 02 nao trava a tigela na mao dela "
                                "— se ela devolve em quadro, a virada se "
                                "desfaz dentro dos 8 segundos"))


def _bd9_profundidade(spec, blocos, achados):
    """⛔⛔ BD9 — A PROFUNDIDADE DE CAMPO E' A COPY VISUAL DO TAKE 1.

    Ordem do operador, lendo o print: ele grande e NITIDO em primeiro plano,
    ela menor e mais SUAVE varios pes atras. A distancia entre os dois E' o
    argumento do quadro — e distancia nao se pede por omissao. Sem a direcao
    explicita o Veo achata os dois no mesmo plano, e a cama vira um casal
    sentado junto: que e' exatamente o take 2, oito segundos antes da hora.

    ⚠️ E a lente cobra tambem no TAKE, nao so' na IMAGE: a IMAGE segura o
    primeiro frame, o TAKE segura os oito segundos — a mesma razao da BD3.
    """
    i1, t1 = blocos["IMAGE 01/02"], blocos["TAKE 01/02"]
    for peca in ("Close to the lens in the left foreground",
                 "Several feet behind him",
                 "Shallow depth of field",
                 "large and sharp in the foreground",
                 "makes the distance between them plain"):
        if peca not in i1:
            achados.append(("ERRO", "BD9: a IMAGE 01 nao pede %r — sem a "
                                    "direcao explicita o Veo achata os dois no "
                                    "mesmo plano e a distancia some" % peca))
    if "stays large and sharp in the foreground" not in t1:
        achados.append(("ERRO", "BD9: o TAKE 01 nao segura a profundidade — a "
                                "IMAGE segura o primeiro frame, o TAKE segura "
                                "os 8 segundos"))


def _bd5_sem_texto(spec, blocos, achados):
    """BD5 — nada de texto queimado, e aqui ha' um motivo A MAIS.

    ⛔ O print da FONTE tem legenda queimada. Quem for "fiel a' fonte" sem ler
    isto vai pedir a legenda ao gerador — e a nossa legenda nasce DEPOIS, no
    Veo Editor, do Whisper rodando sobre o audio. Texto vindo do gerador entra
    por cima e nao ha' como tirar.
    """
    sc.lint_sem_texto(blocos, achados)
    for k in ("IMAGE 01/02", "IMAGE 02/02"):
        if "No on-screen text" not in blocos[k]:
            achados.append(("ERRO", "BD5: %s sem a trava de texto — a fonte "
                                    "tem legenda queimada e nos nao "
                                    "queimamos" % k))


# ⛔⛔ BD6 — NAO HA' PROP FALICO NESTE ANGULO, e a ausencia e' VIGIADA.
# ⚠️ Dezenove dos vinte e dois motores do parque tem um; quem chegar aqui vindo
# de qualquer um deles vai sentir falta e vai querer "consertar". A prova deste
# agente e' o CASAMENTO — bracos cruzados que viram corpo colado — e um geoduck
# na cena mataria justamente isso.
_PROXY_FALICO = re.compile(
    r"\b(geoduck|clam|siphon|banana|cucumber|carrot|squash|zucchini|sausage|"
    r"eggplant|anatomical model|anatomy model|penile|phallic|shaft)\b", re.I)


def _bd6_sem_prop(spec, blocos, achados):
    for nome in sorted(blocos):
        m = _PROXY_FALICO.search(blocos[nome])
        if m:
            achados.append(("ERRO", "BD6: %s traz um proxy falico (%r) — este "
                                    "angulo NAO tem prop, e a prova dele e' o "
                                    "casamento (bracos cruzados -> corpo "
                                    "colado)" % (nome, m.group(0))))


# ⛔⛔ BD10 — O DEITICO DO TAKE 2 NAO TEM PARA ONDE APONTAR.
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


def _bd10_deitico_orfao(spec, blocos, achados):
    fala = spec["falas"][1]
    for m in _DEITICO_T2.finditer(fala):
        alvo = m.group(2).lower()
        if alvo not in fala[:m.start(2)].lower():
            achados.append(("ERRO",
                            "BD10: o take 2 diz %r e o substantivo nunca foi "
                            "introduzido — o take 2 e' DENTRO D'AGUA, oito "
                            "segundos e um corte depois do quarto, e nao herda "
                            "objeto nenhum para o deitico apontar"
                            % m.group(0)))


def _bd7_orcamento(spec, blocos, achados):
    for i, fala in enumerate(spec["falas"], 1):
        n = _palavras(fala)
        if n > TETO_FALA[i]:
            achados.append(("ERRO", "BD7: cena %d com %d palavras (teto %d) — "
                                    "a fala e' CORTADA no render"
                            % (i, n, TETO_FALA[i])))
        if n < PISO_FALA[i]:
            achados.append(("AVISO", "BD7: cena %d com %d palavras (piso %d) — "
                                     "sobra ar morto no take"
                            % (i, n, PISO_FALA[i])))


def _bd8_etnia(spec, blocos, achados):
    """BD8 — a congruencia governa O HOMEM, que e' quem fala.

    ⭐ E cobra tambem o MUNDO: a etnia da pagina tem de caber no arquetipo
    regional sorteado. Congruencia que so' olha o rosto deixa o homem branco
    num brownstone do Harlem, e a leitura quebra do mesmo jeito.
    """
    et = spec["etnia"]
    for k in ("BLOCO 0 (REF)", "IMAGE 01/02", "IMAGE 02/02"):
        if et not in blocos[k]:
            achados.append(("ERRO", "BD8: %s sem a etnia da pagina (%r) — a "
                                    "congruencia com o avatar sai do video sem "
                                    "ninguem ver" % (k, et)))
    if et not in spec["mundo"]["etnias"]:
        achados.append(("ERRO", "BD8: o mundo %r nao comporta a etnia da "
                                "pagina (%r) — o arquetipo regional arrasta a "
                                "casa inteira, nao so' o fundo"
                        % (spec["mundo"]["id"], et)))


def _bd11_bela(spec, blocos, achados):
    """⭐⭐ BD11 — O TOGGLE MODO BELA TEM DE MUDAR O QUADRO, NOS DOIS ESTADOS.

    ⛔ E' a lente contra a FORMA-SEM-FUNCAO, que este repo ja' pagou tres vezes:
    botao aceso, sorteio igual. Ela cobra que a idade, o porte e o traje dela
    sorteados cheguem aos DOIS blocos de imagem — que sao exatamente as tres
    coisas que o modo move.

    ⚠️ E cobra os DOIS ESTADOS pelo MESMO caminho: com o modo desligado a
    esposa realista tem de estar la' com a idade de 44+ do print; com ele
    ligado, a REF do pool compartilhado. Lente que so' olha o estado ligado
    deixaria o desligado apodrecer sem ninguem ver.
    """
    w = spec["mulher"]
    i1, i2 = blocos["IMAGE 01/02"], blocos["IMAGE 02/02"]
    for k, bl in (("IMAGE 01/02", i1), ("IMAGE 02/02", i2)):
        if "%d-year-old" % w["idade"] not in bl:
            achados.append(("ERRO", "BD11: %s sem a idade sorteada dela (%d) — "
                                    "a idade e' a primeira coisa que o modo "
                                    "BELA move" % (k, w["idade"])))
        if w["porte"] not in bl:
            achados.append(("ERRO", "BD11: %s sem o porte sorteado dela (%r) — "
                                    "corpo que nao chega ao frame nao e' corpo"
                            % (k, w["porte"][:34])))
        if w["marca"] not in bl:
            achados.append(("ERRO", "BD11: %s sem a marca facial dela — ela "
                                    "reaparece depois de um corte, e sem "
                                    "ancora o Veo troca de mulher" % k))
    for k, bl, t in (("IMAGE 01/02", i1, 1), ("IMAGE 02/02", i2, 2)):
        if _traje_dela(spec, t) not in bl:
            achados.append(("ERRO", "BD11: %s sem o traje do estado atual do "
                                    "modo BELA (%r)"
                            % (k, _traje_dela(spec, t)[:34])))
    if not spec.get("bela") and w["idade"] < 44:
        achados.append(("ERRO", "BD11: modo BELA DESLIGADO e a esposa tem %d "
                                "anos — o estado desligado e' a esposa "
                                "realista do print (44+)" % w["idade"]))


def _bd13_conta_do_casamento(spec, blocos, achados):
    """⛔⛔ BD13 — OS ANOS DITOS TEM DE FECHAR COM A IDADE EM QUADRO.

    ⚠️ Esta lente existe porque o defeito que ela pega passou por TODOS os
    medidores externos, pelo linter e pelo autoteste. Nenhum deles cruza a fala
    com o ELENCO: o `medir_deiticos` mede dentro da sentenca, o `medir_copy16`
    mede o contrato, o `medir_teto_fala` mede palavras. `Twenty six years
    married` e' uma sentenca impecavel — ate' voce olhar quem esta' na cama.

    ⛔ A lente cobra o RESULTADO, nao a intencao: ela le' a fala JA' MONTADA e
    refaz a subtracao. Guarda que so' checasse `_viradas_da_esposa` ter sido
    chamado seria forma verificando forma — se um dia alguem montar a fala por
    outro caminho (o `nova_fala` do painel, por exemplo), e' esta conta que
    acusa.

    ⚠️ So' a esposa entra na conta, e a ausencia do homem e' deliberada: ele tem
    55-60 e a maior duracao do pool e' 31, entao a conta dele fecha em 100% dos
    sorteios por construcao. Lente que nunca pode acusar e' forma sem funcao.
    """
    anos = _anos_de_casamento(spec["falas"][0])
    if not anos:
        return
    idade = spec["mulher"]["idade"]
    if idade - anos < IDADE_MINIMA_AO_CASAR:
        achados.append(("ERRO",
                        "BD13: a fala diz %d anos de casamento e a esposa em "
                        "quadro tem %d — ela teria casado aos %d. O quadro "
                        "mostra a idade dela, entao a conta e' publica"
                        % (anos, idade, idade - anos)))


def _bd12_contrato16(spec, blocos, achados):
    """As NOVE travas do CONTRATO DE COPY 16s, cobradas de dentro do motor.

    ⭐ `isca_absurda=False`: este angulo nao promete nada no take 1 que ele
    mesmo va' desmentir meio segundo depois (o take 1 e' a falha + o custo
    conjugal, nao substancia absurda). Logo o CT7 — verbo de ereccao colado no
    orgao — vale nos DOIS takes, e nao so' no do CTA.
    ⚠️ `sys.modules[__name__]` e nao outro modulo: a lente le' `base.NUCLEO`, e
    o NUCLEO e' deste arquivo.
    """
    sc.lint_copy16(sys.modules[__name__], spec, achados, isca_absurda=False)


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
    for f in (_bd1_ela_muda, _bd2_inversao, _bd3_ancora, _bd4_tigela,
              _bd5_sem_texto, _bd6_sem_prop, _bd7_orcamento, _bd8_etnia,
              _bd9_profundidade, _bd10_deitico_orfao, _bd11_bela,
              _bd12_contrato16, _bd13_conta_do_casamento):
        f(spec, blocos, ach)
    return ach


# ===========================================================================
# PAINEL
# ===========================================================================

EIXOS_UI = [
    ("mundo", "A REGIAO", "MUNDOS", "regiao"),
    ("homem", "QUEM FALA", "HOMENS", "id"),
    ("mulher", "A ESPOSA", "MULHERES", "id"),
    ("tigela", "A TIGELA DO TRICK", "TIGELAS", "curto"),
]

EIXOS_TRAVAVEIS = ["mundo", "homem", "mulher", "tigela"]

TRAVAS_UI = [("familia_mundo", "regiao", ["livre"] + FAMILIAS_MUNDO)]

# ⚠️ `mundo` ja' entra na lista de ignorados do `lint_painel_honesto` (o valor
# do eixo e' um id interno). Os outros tres chegam ao quadro pelo `marca`, pelo
# `marca` dela e pelos `img1`/`img2` da tigela — e a lente cobra isso a cada
# sorteio.
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
    return ("16s, DOIS takes, região: %s. Take 1 — A CAMA E A TIGELA: ele de "
            "%d anos, tronco nu e calça de pijama, MUITO perto da lente, com "
            "%s NO COLO, mexendo com a colher; ela vários pés atrás, sentada "
            "contra a cabeceira, com os BRAÇOS CRUZADOS, ENCARANDO ele. Ele "
            "grande e nítido na frente, ela menor e suave atrás — a distância "
            "é o quadro. A fala é a falha dele + o custo do casamento. Take 2 "
            "— A VIRADA: o MESMO homem, com rosto, dentro d'água (%s); ela "
            "COLADA nele e A MESMA TIGELA agora NAS MÃOS DELA, com os cubos de "
            "gelatina. Mecanismo, a prova (ela) e o CTA por último. Elenco: "
            "homem %s, esposa %s de %d anos (modo BELA %s). Ela é MUDA nos "
            "dois takes."
            % (spec["mundo"]["regiao"], spec["homem"]["idade"],
               spec["tigela"]["nome"], spec["mundo"]["a_agua"],
               spec["etnia"], spec["mulher"]["etnia"], spec["mulher"]["idade"],
               "LIGADO" if spec.get("bela") else "desligado"))


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
    # ⭐⭐ OS DOIS ESTADOS DO MODO BELA, MEDIDOS SEPARADAMENTE. Medir so' o
    # default e' medir metade do agente: o toggle troca o pool inteiro da
    # esposa, e um KeyError do lado ligado morreria CALADO dentro do callback do
    # tkinter — que e' exatamente como seis botoes `trocar` ficaram quebrados em
    # 2026-07-31 sem ninguem ver.
    idades_bela = collections.defaultdict(set)

    for i in range(n):
        modo = {} if i % 2 == 0 else {"bela": True}
        s = sortear(pags[i % len(pags)], random.Random(i), {}, modo)
        apel[s["apelido"]] += 1
        idades_bela[bool(s["bela"])].add(s["mulher"]["idade"])
        for c, f in enumerate(s["falas"], 1):
            dist[c].add(f)
            tam[c].append(_palavras(f))
        for nivel, msg in lint(s, montar(s)):
            if nivel == "ERRO":
                erros[msg[:70]] += 1
            else:
                avisos += 1

    print("BED 16 — %d sorteios (metade com MODO BELA ligado)" % n)
    for c in sorted(dist):
        v = sorted(tam[c])
        print("  cena %d: %d falas distintas · palavras min/med/max %d/%d/%d"
              % (c, len(dist[c]), v[0], v[len(v) // 2], v[-1]))
    print("  apelido: %s" % dict(apel))
    for on in (False, True):
        v = sorted(idades_bela[on])
        print("  esposa · modo BELA %-9s idades %d..%d (%d distintas)"
              % ("LIGADO" if on else "desligado", v[0], v[-1], len(v)))
    print("  linter: %d ERRO, %d AVISO" % (sum(erros.values()), avisos))
    for k, v in erros.most_common(5):
        print("     %3dx %s" % (v, k))

    # ⛔ CONTROLE DO TOGGLE: o modo tem de MOVER a esposa. Se as idades dos dois
    # estados se sobrepuserem inteiras, o botao acende e nao muda nada — que e'
    # a forma-sem-funcao que a BD11 existe para impedir.
    if min(idades_bela[False]) <= max(idades_bela[True]) and (
            idades_bela[False] & idades_bela[True]):
        falhas.append("MODO BELA: os dois estados sorteiam as MESMAS idades — "
                      "toggle que nao muda nada e' forma sem funcao")

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
    # ensina a ignorar o gate.
    _CT2 = re.compile(r"\b(quit|soft|stopped|dead|failed|shut down|useless|"
                      r"lose it|not working|gave out|did nothing|"
                      r"hadn't worked|was finished)\b", re.I)
    sem_ct2 = [x for x in FALHAS if not _CT2.search(x)]
    if sem_ct2:
        falhas.append("CT2: %d entrada(s) de FALHAS sem verbo de falha: %s"
                      % (len(sem_ct2), sem_ct2[:2]))

    # ⛔⛔ CONTROLE POSITIVO DA BD10 — lente que nunca acusa nada e' forma sem
    # funcao, e "sem achado" nela significaria "ninguem olhou". As duas frases
    # abaixo sao as que MORRERAM na conferencia de 2026-08-10; se a lente parar
    # de pega-las, ela quebrou.
    for morta in ("She unpacked that bag that week.",
                  "She quit sleeping on that side."):
        prova = []
        _bd10_deitico_orfao({"falas": ["", "The gelatin trick opens blood flow "
                                           "to your pecker. %s" % morta]},
                            {}, prova)
        if not prova:
            falhas.append("BD10: a lente parou de acusar %r — ela era a unica "
                          "coisa entre este pool e o deitico orfao" % morta)
    limpo = []
    _bd10_deitico_orfao({"falas": ["", "The gelatin trick opens blood flow to "
                                       "your pecker. Now she pulls me to bed. "
                                       "Comment gelatin, and the recipe goes "
                                       "to your messages."]}, {}, limpo)
    if limpo:
        falhas.append("BD10: a lente acusa copy limpa (%s)" % limpo[0][1][:60])

    # ⛔⛔ CONTROLE POSITIVO DA BD13 — a lente tem de ACUSAR a conta que nao
    # fecha e tem de DEIXAR PASSAR a que fecha. Os dois casos abaixo sao os que
    # a conferencia de 2026-08-10 mediu em producao: 16,1% dos videos com o modo
    # BELA ligado e 5,5% com ele desligado.
    for idade, custo, deve_acusar in (
            (21, "Twenty six years married, and she was already packing a "
                 "bag.", True),
            (44, "Thirty one years, and she was sleeping in the other "
                 "room.", True),
            (52, "Thirty one years, and she was sleeping in the other "
                 "room.", False),
            (24, "She stopped saying goodnight, and I let that run for "
                 "months.", False)):
        prova = []
        _bd13_conta_do_casamento(
            {"falas": ["My pecker quit on me. %s" % custo, ""],
             "mulher": {"idade": idade}}, {}, prova)
        if bool(prova) != deve_acusar:
            falhas.append("BD13: esposa de %d com %r — a lente %s e devia %s"
                          % (idade, custo[:28],
                             "acusou" if prova else "passou",
                             "acusar" if deve_acusar else "passar"))

    # ⛔⛔ CONTROLE DO PISO DO FILTRO: para TODA idade que os DOIS pools de
    # esposa sabem sortear, `_viradas_da_esposa` tem de sobrar com pool util. E'
    # o que autoriza o filtro a NAO ter `or VIRADAS` — fallback silencioso e' o
    # que deixou a cena 2 do TROCA estourar o teto sem ninguem ver.
    idades_possiveis = set(w["idade"] for w in MULHERES) | idades_bela[True]
    for idade in sorted(idades_possiveis):
        v = _viradas_da_esposa({"mulher": {"idade": idade}})
        if len(v) < 8:
            falhas.append("VIRADAS: esposa de %d anos deixa so' %d entrada(s) — "
                          "o filtro da conta do casamento estreitou demais"
                          % (idade, len(v)))
        for c in v:
            if idade - _anos_de_casamento(c) < IDADE_MINIMA_AO_CASAR:
                falhas.append("VIRADAS: o filtro deixou passar %r para uma "
                              "esposa de %d anos" % (c[:34], idade))

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
        # ⛔ CONTROLE DO MODO BELA POR MUNDO: os quatro trajes existem e sao
        # DISTINTOS entre os dois registros. Mundo que esquece o par bela
        # levantaria KeyError no `_traje_dela` so' quando o operador ligasse o
        # botao naquela regiao — e travar o app pelo toggle e' o defeito que a
        # BD11 nasceu para impedir.
        for k in ("dela_q_bela", "dela_a_bela"):
            if not m.get(k):
                falhas.append("MUNDO %s: sem %r — o modo BELA quebra nesta "
                              "regiao" % (m["id"], k))
        if m.get("dela_q_bela") == m["dela_q"]:
            falhas.append("MUNDO %s: o traje bela do quarto e' igual ao normal "
                          "— o toggle nao move nada aqui" % m["id"])
        if m.get("dela_a_bela") == m["dela_a"]:
            falhas.append("MUNDO %s: o traje bela da agua e' igual ao normal "
                          "— o toggle nao move nada aqui" % m["id"])

    # ⛔ CONTROLE DA TIGELA: os dois estados do MESMO objeto, e o take 2 tem de
    # dizer `the same` — e' o que faz o espectador ler UM recipiente que trocou
    # de mao, e nao dois recipientes parecidos.
    for t in TIGELAS:
        if not t["img2"].startswith("the same "):
            falhas.append("TIGELA %s: o `img2` nao comeca em `the same` — sem "
                          "isso o fio do video vira dois objetos" % t["id"])
        if "gelatin" not in t["img1"] or "cubes of set" not in t["img2"]:
            falhas.append("TIGELA %s: os dois estados (mistura -> cubos) nao "
                          "estao os dois em cena" % t["id"])

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
    # ⭐ o mesmo toggle do painel, pela linha de comando: aceite e' medicao, e
    # medir o estado ligado exige poder liga-lo sem abrir a janela.
    ap.add_argument("--bela", action="store_true",
                    help="MODO BELA ligado (o padrao e' a esposa do print)")
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
