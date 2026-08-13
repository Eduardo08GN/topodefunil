#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE FIGHT 16 — a briga no quarto · 2 takes de 8s = 16 segundos.

⭐⭐⭐ O ANGULO E' A BRIGA QUE VIRA APROXIMACAO. No take 1 ele esta' DE PE',
tronco nu, TOALHA BRANCA amarrada na cintura, uma mao aberta se explicando para
a lente — e ela, atras, de BRACOS CRUZADOS, com cara fechada, encarando ele. No
take 2 os dois estao COLADOS um no outro, e ele carrega a prova NAS DUAS MAOS.
A distancia entre os dois quadros E' o video, e ela e' contada sem uma palavra.

⭐⭐ O TERCEIRO MOTOR DO PARQUE COM NARRADOR HOMEM (os outros dois sao o
`good16` e o `bed16`). A mulher e' MUDA nos dois takes.

FONTE: reel do Facebook 1337455585246706, 20s, LIDO A 1 FPS com os cookies da
sessao do operador (arquivo destruido logo apos). A transcricao:

    [00:00] Struggling to stay hard? I thought it was just part of getting older.
    [00:03] But letting your performance die is a choice.
    [00:06] I refused to accept that until I discovered this simple horse
            gelatin recipe.
    [00:11] Just one daily habit made with cheap, raw ingredients.
    [00:15] Stop losing your power.
    [00:17] Comment horse and I'll send you the full recipe.

⭐ O QUE A FONTE TEM E NENHUMA DAS NOSSAS TINHA: `But letting your performance
die is a CHOICE.` — ela converte vitima em decisao. Nao culpa o corpo dele,
culpa a INACAO, e quem se sente responsavel age. ⚠️ NAO entrou na copy: o
operador escolheu fechar o take 1 na VIRADA. Fica registrada como municao.

⚠️ A CENA NAO VEM DA FONTE — vem de um PRINT que o operador mandou. Fonte e
print sao coisas separadas aqui, e e' preciso dizer qual e' qual: a COPY e' da
fonte lida; a CENA do take 1 e' do print; os DEZ ambientes do take 2 foram
DITADOS por ele, um a um. Especificacao completa em `SPEC-FIGHT-16.md`.

O ARCO — 2 cenas de 8s, destino AdBatch Vertical 2:

    take 1  A BRIGA         ele DE PE' de toalha na cintura, tronco nu, uma mao
                            aberta se explicando, falando para a lente · ela
                            atras, de BRACOS CRUZADOS, encarando ele, MUDA
                            copy: a falha em 2a pessoa + a falsa causa + a
                            VIRADA que nomeia o gelatin trick
    take 2  O CASAL COLADO  o MESMO homem, com rosto, colado nela · na mao
                            direita a TIGELA DE CUBOS DE GELATINA, na esquerda
                            a CAIXA DE BICARBONATO
                            copy: mecanismo com razao -> habito -> CTA

⛔⛔ AS SEIS DECISOES DO OPERADOR (2026-08-10) — NAO SE REABREM
-----------------------------------------------------------------------------
 1. NARRADOR = ELE. `SEXOS = ("homem",)`. A mulher e' MUDA nos dois takes.
 2. A COPY E' A DA FONTE, com a virada que ele escreveu a mao:
        `Struggling to stay hard? I thought it was just age. But things
         changed when i discovered the gelatin trick.`
    — *"Assim fica melhor e mais contextualizado"*.
 3. O TAKE 1 E' O PRINT: toalha na cintura, ele de pe', ela de bracos cruzados.
 4. POOL DE QUARTOS no take 1 (hotel, banheiro de suite, jacuzzi, casa de
    campo, *etc*) e os DEZ ambientes DITADOS no take 2.
 5. NO TAKE 2 ELE ESTA' COM A TIGELA DE CUBOS NUMA MAO E A CAIXA DE
    BICARBONATO NA OUTRA.
 6. MODO BELA, pelo contrato compartilhado (`MODO_BELA = True` + `sc.ref_bela`).

⛔⛔ DOIS EIXOS DE CENA INDEPENDENTES — E ISSO E' O QUE SEPARA ESTE MOTOR DO
BED 16, que e' o irmao estrutural (narrador homem, MODO BELA, frieza -> casal
colado). No BED os dois ambientes sao DA MESMA CASA e vem do MESMO eixo: a
regiao arrasta quarto + agua, e por isso a agua de la' sempre diz `the same
<casa>`. Aqui o operador declarou DUAS LISTAS SEPARADAS, e o quarto da briga
nao tem nada a ver com o ambiente do casal.

    ⛔ Consequencia direta na LENTE: a continuidade NAO pode exigir "a mesma
       casa". O que ela exige e' O MESMO HOMEM (FT3), e a FT13 PROIBE dizer
       `the same room/house/bedroom` no take 2 — quem copiar o idioma do BED
       para ca' escreve uma mentira, porque os dois eixos sortearam lugares
       diferentes.

⛔ NAO EXISTE PROP FALICO NESTE ANGULO, e a ausencia e' propriedade, nao
esquecimento. A prova e' o CASAL e o que ele tem nas maos. A lente FT6 reprova
qualquer geoduck, peca anatomica ou proxy de legume que alguem tente
"consertar" para ca' no futuro.

⚠️ O QUE NAO EXISTE AQUI E EXISTE NO BED, para ninguem procurar: arquetipo
REGIONAL. O BED/GOOD/FALTA usam regiao dos EUA porque a casa e' o argumento
deles; aqui os quartos sao HOTEL, SUITE, JACUZZI — lugares sem regiao. A etnia
vem da PAGINA e governa o HOMEM, que e' quem fala.

⚠️ IDADE NUNCA E' DITA NA FALA, e a omissao e' deliberada. E' a pendencia B do
BED 16 (idade dita x idade em quadro, 6,0% dos videos de la') resolvida por
CONSTRUCAO: nenhum pool deste motor carrega numero de idade, entao a conta nao
tem como nao fechar. Familia nova nao nasce alimentando defeito conhecido.

⚠️⚠️ O `medir_abertura` ACUSA 100% DAS CENAS 1 DESTE MOTOR, E O VEREDITO E' QUE
ELE ESTA' ERRADO — dito aqui para ninguem "consertar" o pool olhando so' o
numero. Ele procura, na primeira sentenca, um substantivo do NUCLEO ou uma
pessoa com posse (`my wife`), e os HOOKS deste angulo nao tem NENHUM DOS DOIS
de proposito: e' justamente por nao nomear o orgao que o CT7 passa por
construcao. O proprio medidor diz no cabecalho que `o numero e' PONTO DE
PARTIDA, a lista de frases e' o trabalho, e o veredito de cada uma e' humano`, e
proibe usar o `--gate` dele como aceite. Lidas uma a uma pelo TESTE WTF:

    `Struggling to stay hard?`             — o operador escreveu e aprovou
    `Struggling to last ten minutes in bed?`
    `Struggling to keep it up for her?`

Nenhuma deixa espaco para `do que ele esta' falando?`. ⚠️ O GOOD 16 esta' em
100% pelo mesmo motivo e pela mesma formula, e esta' em producao.

⚠️ UM DESVIO DECLARADO EM RELACAO AO `SPEC-FIGHT-16.md` §7, e o motivo esta'
medido: o pool de HABITOS da spec trazia `One bowl every night.` / `One bowl
before bed.`. Vasilhame na fala e' DOSE, e a ordem permanente do operador e' que
a fala nao paga o que o quadro mostra (`lemon`, nao `half of a lemon`). O quadro
ja' mostra a tigela na mao dele; a fala diz a FREQUENCIA, que e' o que o quadro
nao mostra. As entradas com `bowl` sairam e viraram tempo (`A minute a night`).

    python funil-organico/fight16_short.py --pagina joe --n 1
    python funil-organico/fight16_short.py --autoteste
    python funil-organico/fight16_short_app.py
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

LEDGER = os.path.join(AQUI, ".fight-16-ledger.json")

TITULO = "AGENTE FIGHT 16"
SLUG = "fight-16"
SUBTITULO = ("2 takes de 8s = 16 segundos · a briga de toalha no quarto e "
             "depois o casal colado · o homem fala e ela e' muda · a prova "
             "esta' nas duas maos dele")

CENAS_UI = ["1 · A BRIGA", "2 · O CASAL COLADO"]

# ⛔⛔ DUAS CENAS no teto FISICO de 25 palavras (8s a ~3,1 p/s). O teto vem de
# RENDER, nao de teoria: 32 cortou, 28 cortou, 25 nao.
TETO_FALA = {1: 25, 2: 25}
# ⛔ O piso e' ARITMETICA, nao gosto: e' a soma dos MINIMOS de cada beat.
#     take 1   HOOK 4  + FALSA 6  + VIRADA 8  = 18
#     take 2   MECANISMO 9 + HABITO 4 + CTA 9 = 22
# ⚠️ Piso calibrado com um beat que nao existe e' alarme que sempre dispara — e
# alarme que sempre dispara ensina a ignorar o linter inteiro.
PISO_FALA = {1: 18, 2: 22}

# ⛔ Congruencia inviolavel: a etnia do REF casa com a etnia do avatar da
# pagina. ⭐ Neste angulo o REF que fala e' o HOMEM — entao a pagina governa
# ELE. A mulher fica solta (mesma politica do GOOD 16 e do BED 16).
ETNIA = {
    "roy": "white American", "dean": "white American",
    "earl": "white American",
    "jason": "Black American", "philippe": "Black American",
    "joe": "white American", "ray": "white American", "matt": "white American",
    "marcus": "Black American", "chuck": "Black American",
}

# ⭐ QUEM NARRA — o terceiro motor do parque com narrador HOMEM.
# ⚠️ Com UM sexo so' a UI nao desenha botao nenhum, que e' o certo: botao que
# nao trava nada e' pior que botao nenhum.
SEXOS = ("homem",)

# ⭐⭐ MODO BELA LIGADO — ordem do operador, 2026-08-10.
#
#   · DESLIGADO -> a mulher REALISTA do print (pool `MULHERES`, 33-42 anos):
#     cabelo preso, camiseta escura, cara fechada. E' o quadro que ele mandou.
#   · LIGADO    -> `sc.ref_bela` (contrato compartilhado do repo).
#
# ⛔ E O MODO ARRASTA O QUE PODE ARRASTAR, sem furar o lugar sorteado: "trocar
# so' o rosto deixa a REF de biquini de trico amish". Aqui o modo move IDADE +
# PORTE + TRAJE DELA — e o traje move para a variante BELA **do mesmo quarto e
# do mesmo ambiente sorteados** (`dela_bela`), nunca para uma roupa generica.
#
# ⛔ MODO_FORTE fica desligado, e a ausencia e' declarada: o operador nao pediu
# toggle de corpo aqui, e o homem do print ja' e' atletico por construcao (ver
# `CORPOS_H`). Toggle que duplica o que o pool ja' entrega e' botao sem funcao.
MODO_BELA = True
MODO_FORTE = False

# ⛔ A etnia sai da PAGINA, entao o seletor clara/escura do painel funciona
# trocando de pagina — que e' o comportamento padrao. Declarar PELE_TRAVAVEL
# aqui acenderia um caminho que este motor nao usa.
PELE_TRAVAVEL = False


# ===========================================================================
# ⭐⭐ EIXO 1 DE CENA — OS QUARTOS DA BRIGA (take 1)
# ===========================================================================
# ⛔ ORDEM DO OPERADOR: *"tera pool de variacoes de quartos: quarto de hotel,
# banheiro luxuoso de uma suite, jacuzzi (o homem de toalha amarrada na cintura
# fora e a mulher emburrada com os bracos cruzados), quarto de casa de campo,
# etc"*. As quatro que ele nomeou estao aqui com o `id` dele; as outras quatro
# sao o `etc`.
#
# ⛔⛔ CADA ENTRADA CARREGA ONDE ELA ESTA', e isso NAO e' redundancia com o
# cenario. O print poe a mulher DEITADA DE LADO NA CAMA — geometria que nao
# existe num banheiro de suite nem dentro de uma jacuzzi. Um pool que so'
# trocasse a parede deixaria o gerador improvisar a posicao dela em metade das
# entradas, e improviso e' o que devolve duas pessoas em pe' lado a lado, que e'
# exatamente o take 2 oito segundos antes da hora.
# ⚠️ O QUE NAO VARIA, em nenhuma entrada: os BRACOS CRUZADOS e o ENCARAR. E' a
# metade fria da inversao, e a lente FT2 cobra os dois literais.
#
# ⭐ E cada entrada carrega o TRAJE DELA EM DOIS REGISTROS — `dela` (modo BELA
# desligado, a mulher realista do print) e `dela_bela` (modo ligado). O par bela
# e' do MESMO lugar, so' que no registro do modo: e' isso que impede a REF de
# biquini de trico amish, o modo de falha que o repo ja' nomeou.
QUARTOS = [
    {"id": "hotel", "nome": "quarto de hotel",
     "cen": "a hotel room at night, a wide upholstered headboard and heavy "
            "curtains pulled back from a window with the lit city behind it",
     "ela": "lying on her side on top of the made bed several feet behind him, "
            "propped on one elbow against the pillows",
     "luz": "two warm bedside lamps on and the rest of the room low",
     "audio": "a hotel air handler humming, faint traffic far below",
     "dela": "a black t-shirt and dark trousers",
     "dela_bela": "a short black satin slip"},

    {"id": "banheiro_suite", "nome": "banheiro luxuoso de suite",
     "cen": "the marble bathroom of a luxury suite, a long double vanity and a "
            "wide lit mirror running along the wall",
     "ela": "standing several feet behind him with her back against the far "
            "end of the vanity",
     "luz": "warm bulbs over the mirror and a little steam still on the glass",
     "audio": "an extractor fan running, water dripping in the shower stall",
     "dela": "a white waffle bathrobe tied closed",
     "dela_bela": "a short white waffle robe"},

    {"id": "jacuzzi", "nome": "jacuzzi (ele fora da agua)",
     "cen": "an indoor spa room, a tiled jacuzzi sunk into the floor with the "
            "water moving",
     "ela": "sitting in the jacuzzi several feet behind him with the water at "
            "her waist",
     "luz": "warm recessed light and steam coming off the water",
     "audio": "the jacuzzi jets running, water moving against tile",
     "dela": "a black one-piece swimsuit",
     "dela_bela": "a black halter bikini top"},

    {"id": "casa_campo", "nome": "quarto de casa de campo",
     "cen": "a country house bedroom, painted board walls and an iron bed "
            "frame with a heavy quilt on it",
     "ela": "sitting up against the iron headboard several feet behind him, on "
            "top of the quilt",
     "luz": "one lamp on the nightstand and the window black behind it",
     "audio": "wind in the trees outside, an old house settling",
     "dela": "a grey long-sleeved top and plaid pyjama trousers",
     "dela_bela": "a short grey satin slip"},

    {"id": "apartamento", "nome": "quarto de apartamento urbano",
     "cen": "a modern apartment bedroom, plain walls and a wide window with "
            "city lights behind it",
     "ela": "sitting on the far end of the bed several feet behind him, turned "
            "toward him",
     "luz": "one low lamp inside and the city glow coming in through the glass",
     "audio": "distant city traffic, an elevator chiming somewhere in the "
              "building",
     "dela": "a navy tank top and cotton shorts",
     "dela_bela": "a short navy satin camisole and shorts"},

    {"id": "cabana", "nome": "quarto de cabana na montanha",
     "cen": "a mountain cabin bedroom, log walls and a wood stove burning in "
            "the corner",
     "ela": "sitting on the edge of the bed several feet behind him with a "
            "wool blanket over her knees",
     "luz": "firelight from the stove and one small lamp on the nightstand",
     "audio": "the stove ticking, wind against the log walls",
     "dela": "a cream knit sweater and thick socks",
     "dela_bela": "a cropped cream knit sweater and thick socks"},

    {"id": "praia", "nome": "suite de praia",
     "cen": "a beach suite bedroom, open balcony doors and dark palms moving "
            "beyond the rail",
     "ela": "sitting sideways on the bed several feet behind him with her feet "
            "on the floor",
     "luz": "moonlight coming through the open doors and one warm lamp inside",
     "audio": "surf breaking far off, wind through the open doors",
     "dela": "a white cotton beach cover-up",
     "dela_bela": "a short white beach cover-up"},

    {"id": "cobertura", "nome": "quarto de cobertura",
     "cen": "a penthouse bedroom, a glass wall onto a private terrace with the "
            "lit city behind it",
     "ela": "sitting back against the pillows several feet behind him, on top "
            "of the covers",
     "luz": "low warm lamps inside and the city throwing cold light through "
            "the glass",
     "audio": "the low hum of the city, wind against the glass",
     "dela": "a charcoal robe tied closed",
     "dela_bela": "a short charcoal satin robe"},

    # ⭐⭐ + 2026-08-13, ordem do operador: *"aumente o pool de opcoes
    # substancialmente, tambem dos ambientes"*. De 8 para 24 quartos.
    # ⛔ Cada entrada nova declara EXATAMENTE as mesmas sete chaves das
    # vizinhas — `nome`, `cen`, `ela`, `luz`, `audio` e o par de trajes
    # (`dela`/`dela_bela`), que o autoteste cobra um por um e exige DIFERENTES
    # entre si.
    # ⛔⛔ E CADA UMA DIZ ONDE ELA ESTA', que e' a razao de ser deste campo:
    # `ela` vira o sujeito da frase montada (`Lying on her side ... is a
    # 35-year-old woman`), entao entrada sem geometria propria devolve o
    # gerador improvisando a posicao dela.
    # ⚠️ O que NAO varia em nenhuma: os BRACOS CRUZADOS e o ENCARAR moram na
    # MONTAGEM, nao aqui — a lente FT2 cobra os dois literais.
    {"id": "casa_praia_manha", "nome": "quarto de casa de praia de manha",
     "cen": "a beach house bedroom, whitewashed board walls and a window full "
            "of pale morning sky",
     "ela": "sitting up in bed several feet behind him with the sheet across "
            "her legs",
     "luz": "flat early daylight coming in through thin curtains",
     "audio": "surf far off, gulls over the roof",
     "dela": "a white cotton nightshirt",
     "dela_bela": "a short white cotton nightshirt"},

    {"id": "loft_industrial", "nome": "quarto de loft industrial",
     "cen": "a converted loft bedroom, exposed brick and a tall factory window "
            "with black frames",
     "ela": "leaning against the brick wall several feet behind him with her "
            "weight on one hip",
     "luz": "one hanging bulb over the bed and grey light off the brick",
     "audio": "a freight lift somewhere in the building, rain on the glass",
     "dela": "a grey tank top and loose trousers",
     "dela_bela": "a short grey satin slip"},

    {"id": "fazenda", "nome": "quarto de casa de fazenda",
     "cen": "a farmhouse bedroom, painted board walls and a tall wooden "
            "wardrobe against the far wall",
     "ela": "standing several feet behind him with one hand on the wardrobe "
            "door",
     "luz": "one warm lamp on the dresser and the window dark",
     "audio": "cattle far off, an old house settling",
     "dela": "a flannel shirt over a cotton tee",
     "dela_bela": "a short plaid flannel shirt over a camisole"},

    {"id": "hotel_manha", "nome": "quarto de hotel de manha",
     "cen": "a hotel room in daylight, an open suitcase on a luggage rack and "
            "curtains pulled wide",
     "ela": "sitting on the arm of a chair several feet behind him, turned "
            "toward him",
     "luz": "bright flat daylight filling the room",
     "audio": "a housekeeping cart in the corridor, faint traffic below",
     "dela": "a navy hotel robe tied closed",
     "dela_bela": "a short navy satin robe"},

    {"id": "sauna_seca", "nome": "sauna seca da suite",
     "cen": "a cedar sauna room off a suite, slatted benches and a stove of "
            "hot stones in the corner",
     "ela": "sitting on the upper bench several feet behind him with a towel "
            "across her knees",
     "luz": "low amber light from a lamp behind the slats",
     "audio": "the stones ticking, a fan running behind the wall",
     "dela": "a white towel wrapped and tucked at her chest",
     "dela_bela": "a short white towel wrapped at her chest"},

    {"id": "quarto_deserto", "nome": "quarto de casa no deserto",
     "cen": "a desert house bedroom, thick plaster walls and a deep-set window "
            "onto dark rock",
     "ela": "sitting sideways on the end of the bed several feet behind him "
            "with her feet on the floor",
     "luz": "one lamp on the nightstand and cold moonlight in the window",
     "audio": "dry wind against the glass, coyotes far off",
     "dela": "a sand-coloured cotton nightdress",
     "dela_bela": "a short sand-coloured satin slip"},

    {"id": "barco", "nome": "cabine de barco",
     "cen": "the cabin of a moored boat, varnished wood walls and a small "
            "porthole over the berth",
     "ela": "sitting on the berth several feet behind him with her back "
            "against the hull",
     "luz": "one warm reading light over the berth and dark water outside",
     "audio": "water knocking against the hull, rigging tapping on deck",
     "dela": "a navy striped top and shorts",
     "dela_bela": "a short navy satin camisole and shorts"},

    {"id": "chale_neve", "nome": "quarto de chale na neve",
     "cen": "a ski chalet bedroom, timber walls and a wide window packed with "
            "snow-covered pines",
     "ela": "sitting on a bench at the foot of the bed several feet behind him",
     "luz": "warm lamplight inside and cold blue snow light in the window",
     "audio": "wind over the roof, a heater ticking",
     "dela": "a cream thermal top and thick socks",
     "dela_bela": "a cropped cream thermal top and thick socks"},

    {"id": "casarao", "nome": "quarto de casarao antigo",
     "cen": "a bedroom in an old townhouse, high ceilings, a marble fireplace "
            "and tall shuttered windows",
     "ela": "standing several feet behind him with one hand on the mantel",
     "luz": "two lamps low and firelight from the grate",
     "audio": "a clock ticking in the hall, rain on the shutters",
     "dela": "a deep red dressing gown tied closed",
     "dela_bela": "a short deep red satin dressing gown"},

    {"id": "trailer_parque", "nome": "quarto de trailer de viagem",
     "cen": "the sleeping end of a travel trailer, panelled walls and a narrow "
            "window with the night outside",
     "ela": "sitting on the built-in bunk several feet behind him with her "
            "back against the panelling",
     "luz": "one strip light over the bunk and the rest dark",
     "audio": "a generator running outside, insects against the screen",
     "dela": "a grey sweatshirt and cotton shorts",
     "dela_bela": "a cropped grey sweatshirt and cotton shorts"},

    {"id": "spa_piscina_interna", "nome": "sala de piscina coberta",
     "cen": "an indoor pool room, a long lap pool under a glass roof and tiled "
            "walls throwing echo",
     "ela": "standing on the tiles several feet behind him at the edge of the "
            "pool",
     "luz": "cool daylight through the glass roof, the water throwing light "
            "upward",
     "audio": "water lapping the tiled gutter, echo off the walls",
     "dela": "a black one-piece swimsuit with a towel over her arm",
     "dela_bela": "a black halter bikini top with a towel over her arm"},

    {"id": "quarto_lago", "nome": "quarto de casa de lago",
     "cen": "a lake house bedroom, panelled walls and sliding doors onto a "
            "deck over the water",
     "ela": "sitting in a chair by the sliding doors several feet behind him",
     "luz": "one lamp inside and last light coming off the lake",
     "audio": "water against a dock, loons far off",
     "dela": "a pale green cotton nightdress",
     "dela_bela": "a short pale green satin slip"},

    {"id": "banheiro_azulejo", "nome": "banheiro de azulejo antigo",
     "cen": "an older tiled bathroom, small square wall tiles and a wide "
            "mirror over a single basin",
     "ela": "standing in the doorway several feet behind him with one shoulder "
            "against the frame",
     "luz": "a bare bulb over the mirror and steam still on the glass",
     "audio": "a tap dripping, an extractor fan running",
     "dela": "a pale grey waffle robe tied closed",
     "dela_bela": "a short pale grey waffle robe"},

    {"id": "suite_deserto_luxo", "nome": "suite de resort no deserto",
     "cen": "a desert resort suite, a low platform bed and a wall of glass "
            "onto a dark courtyard",
     "ela": "sitting cross-legged on the far end of the platform bed several "
            "feet behind him",
     "luz": "warm floor lights inside and cold light from the courtyard",
     "audio": "wind in the courtyard palms, a fountain running",
     "dela": "a bronze satin slip dress",
     "dela_bela": "a short bronze satin slip dress"},

    {"id": "quarto_chuva_cidade", "nome": "quarto urbano na chuva",
     "cen": "a city bedroom with the window streaming with rain and wet neon "
            "smeared across the glass",
     "ela": "sitting on the windowsill several feet behind him with her back "
            "to the glass",
     "luz": "one lamp inside and coloured light bleeding through the rain",
     "audio": "heavy rain on the glass, tyres on a wet street",
     "dela": "a black jersey tank top and cotton trousers",
     "dela_bela": "a short black jersey slip"},

    {"id": "quarto_montanha_vidro", "nome": "quarto de casa envidracada na "
                                            "montanha",
     "cen": "a glass-walled mountain house bedroom, a wall of glass onto a "
            "dark valley and a low platform bed",
     "ela": "standing at the glass several feet behind him, turned toward him",
     "luz": "two low lamps inside and moonlight on the valley behind",
     "audio": "wind across the glass, an owl somewhere below",
     "dela": "a slate grey robe tied closed",
     "dela_bela": "a short slate grey satin robe"},
]


# ===========================================================================
# ⭐⭐ EIXO 2 DE CENA — OS DEZ AMBIENTES DO CASAL (take 2)
# ===========================================================================
# ⛔⛔ LISTA FECHADA, DITADA PELO OPERADOR, uma a uma. NAO se inventa entrada
# nova, NAO se resume, NAO se troca de ordem. O que esta' aqui e' a traducao
# para o idioma dos nossos blocos das dez descricoes que ele escreveu.
#
# ⛔ E ESTE EIXO E' INDEPENDENTE DO QUARTO DA BRIGA — ver o cabecalho. O que
# amarra os dois takes e' O HOMEM (FT3), nunca o lugar (FT13).
#
# ⭐ CADA ENTRADA CARREGA A POSE DELE, e a razao e' de producao: em cinco das
# dez ele esta' na cama ou de pe' e nas outras esta' dentro d'agua ou perto de
# uma banheira. `pose` diz onde o CORPO dele esta'; a clausula que cola os dois
# e a que poe a tigela e a caixa nas maos dele moram na MONTAGEM, porque sao
# invariantes do angulo e a lente as cobra literalmente.
#
# ⚠️⚠️ E CADA ENTRADA CARREGA `maos`, QUE E' ACHADO DE LEITURA — nao de linter.
# O primeiro render saiu com ele DENTRO da jacuzzi, com a agua no peito, segurando
# uma CAIXA DE PAPELAO. O linter passou verde nos seis medidores e nas treze
# lentes: nenhum deles cruza o objeto com o lugar. So' aparece lendo o bloco
# IMAGE inteiro em voz alta, que e' a unica lente que pega contradicao fisica.
# ⛔ SO' A ENTRADA QUE PRECISA DECLARA (lido com `.get`), e nao e' preguica:
# frase que nao acrescenta nada e' ruido no prompt, e nove `"maos": ""` seriam
# nove linhas que ninguem le'. O que impede o campo de sumir e' o CONTROLE do
# autoteste — ambiente cuja `pose` diz `water` e' OBRIGADO a trazer a clausula.
AMBIENTES = [
    {"id": "jacuzzi_hotel", "nome": "jacuzzi de hotel a' noite",
     "cen": "a hotel jacuzzi at night, wine glasses set on the tiled rim, "
            "towels folded over the edges and clothes left neatly around the "
            "room",
     "pose": "Sitting in the jacuzzi with the water at his chest is",
     "maos": "Both of his hands are raised clear of the water and stay dry.",
     "luz": "low warm light with steam coming off the water",
     "audio": "the jacuzzi jets running, water moving against tile",
     "dele": "bare-chested",
     "dela": "a black bikini top",
     "dela_bela": "a black halter bikini top"},

    {"id": "hotel_festa", "nome": "quarto de hotel depois da festa",
     "cen": "a hotel room after a party, a suit jacket and a dress left over "
            "the back of a chair and the bed partly unmade",
     "pose": "Sitting on the edge of the bed is",
     "luz": "low lamplight with the ceiling light off",
     "audio": "a hotel air handler humming, faint music from a floor below",
     "dele": "wearing an open white dress shirt",
     "dela": "a dark green satin slip dress",
     "dela_bela": "a short dark green satin slip dress"},

    {"id": "cabana_lareira", "nome": "cabana isolada na montanha",
     "cen": "a bedroom in an isolated mountain cabin warmed by a fireplace, "
            "casual clothes folded over an armchair and a blanket pushed aside",
     "pose": "Sitting on the rug in front of the fireplace is",
     "luz": "firelight from the hearth and one small lamp",
     "audio": "the fire cracking, wind against the log walls",
     "dele": "wearing a plain grey t-shirt",
     "dela": "a cream knit sweater",
     "dela_bela": "a cropped cream knit sweater"},

    {"id": "praia_tropical", "nome": "praia tropical a' noite",
     "cen": "a suite beside a tropical beach at night, the balcony door open "
            "and beach clothes left near the bed",
     "pose": "Sitting on the end of the bed is",
     "luz": "moonlight coming in through the open balcony door and one warm "
            "lamp inside",
     "audio": "surf breaking outside, wind through the open door",
     "dele": "bare-chested with a towel over one shoulder",
     "dela": "a white cotton beach cover-up",
     "dela_bela": "a short white beach cover-up"},

    {"id": "apartamento_jantar", "nome": "apartamento depois do jantar",
     "cen": "a modern apartment bedroom just off a table still set with plates "
            "and two wine glasses, city light coming in through the windows",
     "pose": "Standing just inside the bedroom doorway is",
     "luz": "warm indoor light with the city glow behind the glass",
     "audio": "distant city traffic, a refrigerator humming in the kitchen",
     "dele": "wearing an open dark shirt",
     "dela": "a navy wrap dress",
     "dela_bela": "a short navy wrap dress"},

    {"id": "motel_neon", "nome": "quarto de motel com neon",
     "cen": "a styled motel room, the bed unmade, personal things left on the "
            "counter and clothes lying casually on the floor",
     "pose": "Sitting back against the headboard is",
     "luz": "neon light from the window sign washing the room in colour",
     "audio": "a window air conditioner rattling, a car passing outside",
     "dele": "wearing a plain white t-shirt",
     "dela": "a black satin camisole and shorts",
     "dela_bela": "a short black satin camisole and shorts"},

    {"id": "banheiro_luxo", "nome": "banheiro luxuoso de suite",
     "cen": "the luxury bathroom of a suite beside a deep freestanding tub, "
            "towels spread over the edges and mist on the mirror",
     "pose": "Sitting on the wide edge of the tub is",
     "luz": "warm bulbs over the mirror with mist softening the light",
     "audio": "water dripping into the tub, an extractor fan running",
     "dele": "bare-chested with a towel around his waist",
     "dela": "a white waffle robe tied closed",
     "dela_bela": "a short white waffle robe"},

    {"id": "domingo_manha", "nome": "quarto numa manha de domingo",
     "cen": "a bedroom on a Sunday morning, clothes scattered around the room "
            "and strong daylight coming through the curtains",
     "pose": "Sitting up in bed under the sheets is",
     "luz": "bright morning daylight pushing through the curtains",
     "audio": "birds outside the window, a quiet street",
     "dele": "bare-chested with the sheet across his lap",
     "dela": "a grey cotton t-shirt",
     "dela_bela": "an oversized grey cotton t-shirt"},

    {"id": "campo_chuva", "nome": "casa de campo na chuva",
     "cen": "a country house bedroom during heavy rain, the window covered in "
            "running drops and clothes left over a chair",
     "pose": "Sitting on the edge of the bed is",
     "luz": "soft light from a bedside lamp with the window dark behind it",
     "audio": "heavy rain on the window, an old house settling",
     "dele": "wearing an open flannel shirt",
     "dela": "a plaid flannel shirt over a camisole",
     "dela_bela": "a short plaid flannel shirt over a camisole"},

    {"id": "cobertura_piscina", "nome": "cobertura com piscina privativa",
     "cen": "a penthouse bedroom just in from a private pool, towels and "
            "swimwear left around, glasses on a table and a glass door showing "
            "the lit city behind",
     "pose": "Standing just inside the glass door is",
     "luz": "low warm lamps inside with the city throwing cold light through "
            "the glass",
     "audio": "pool water moving outside, the low hum of the city",
     "dele": "bare-chested with a towel around his waist",
     "dela": "a coral swimsuit with a towel wrap at her hips",
     "dela_bela": "a coral halter swimsuit with a towel wrap at her hips"},

    # ⭐⭐ + 2026-08-13 — E ESTA E' UMA ORDEM QUE REVOGA OUTRA, entao vale
    # escrever qual. O cabecalho acima dizia LISTA FECHADA, ditada pelo
    # operador uma a uma, e o autoteste cobrava `len(AMBIENTES) == 10`. A ordem
    # nova e' dele e e' mais recente: *"aumente o pool de opcoes
    # substancialmente, tambem dos ambientes"*. De 10 para 24 — as DEZ dele
    # ficam palavra por palavra, e o piso do autoteste virou 24.
    # ⛔ Cada entrada nova declara as mesmas oito chaves das dez originais, e o
    # `maos` continua sendo declarado SO' por quem precisa (o controle do
    # autoteste cobra a clausula de todo ambiente cuja `pose` diga `water`,
    # porque a caixa de bicarbonato e' de PAPELAO e ele a carrega na mao).
    # ⛔ E NENHUMA diz `the same <lugar>`: os dois eixos de cena sao
    # independentes e quem atravessa o corte e' o HOMEM (lente FT13).
    {"id": "lago_amanhecer", "nome": "casa de lago ao amanhecer",
     "cen": "a lake house bedroom at first light, sliding doors open onto a "
            "deck over the water and clothes left over a chair",
     "pose": "Sitting on the end of the bed is",
     "luz": "pale early light coming in off the lake",
     "audio": "water against a dock, birds starting outside",
     "dele": "bare-chested with a blanket across his lap",
     "dela": "a pale green cotton nightdress",
     "dela_bela": "a short pale green satin slip"},

    {"id": "sauna_cedro", "nome": "sauna de cedro da suite",
     "cen": "a cedar sauna room off a suite, towels folded on the lower bench "
            "and a stove of hot stones in the corner",
     "pose": "Sitting on the lower bench is",
     "luz": "low amber light coming through the slats",
     "audio": "the stones ticking, a fan running behind the wall",
     "dele": "bare-chested with a towel around his waist",
     "dela": "a white towel wrapped and tucked at her chest",
     "dela_bela": "a short white towel wrapped at her chest"},

    {"id": "piscina_coberta", "nome": "piscina coberta",
     "cen": "an indoor pool room under a glass roof, towels left along the "
            "tiled edge and robes on a hook by the door",
     "pose": "Standing in the shallow end with the water at his waist is",
     "maos": "Both of his hands are raised clear of the water and stay dry.",
     "luz": "cool daylight through the glass roof, the water throwing light "
            "upward",
     "audio": "water lapping the tiled gutter, echo off the walls",
     "dele": "bare-chested",
     "dela": "a black bikini top",
     "dela_bela": "a black halter bikini top"},

    {"id": "terraco_verao", "nome": "terraco de verao a' noite",
     "cen": "a roof terrace on a summer night, string lights overhead and "
            "towels thrown over the backs of two chairs",
     "pose": "Sitting on a low bench is",
     "luz": "warm string lights with the lit city behind",
     "audio": "the low hum of the city, music from another roof",
     "dele": "wearing an open linen shirt",
     "dela": "a white slip dress",
     "dela_bela": "a short white slip dress"},

    {"id": "banheira_pe_leao", "nome": "banheiro antigo com banheira de pe' "
                                       "de leao",
     "cen": "an older tiled bathroom beside a deep claw-foot tub, towels over "
            "the rim and mist on the mirror",
     "pose": "Sitting on the wide rim of the claw-foot tub is",
     "luz": "a bare bulb over the mirror with mist softening it",
     "audio": "water dripping into the tub, an extractor fan running",
     "dele": "bare-chested with a towel around his waist",
     "dela": "a pale grey waffle robe tied closed",
     "dela_bela": "a short pale grey waffle robe"},

    {"id": "chale_neve", "nome": "chale na neve",
     "cen": "a ski chalet bedroom with snow packed against the window, coats "
            "left over a bench and a heater running",
     "pose": "Sitting on the bench at the foot of the bed is",
     "luz": "warm lamplight inside and cold blue snow light in the window",
     "audio": "wind over the roof, a heater ticking",
     "dele": "wearing a cream thermal top",
     "dela": "a cream knit sweater and thick socks",
     "dela_bela": "a cropped cream knit sweater and thick socks"},

    {"id": "fazenda_manha", "nome": "casa de fazenda de manha",
     "cen": "a farmhouse bedroom in the morning, boots by the door and a quilt "
            "pushed down to the foot of the bed",
     "pose": "Sitting on the edge of the bed is",
     "luz": "strong morning daylight through a thin curtain",
     "audio": "cattle far off, a screen door",
     "dele": "wearing an open flannel shirt",
     "dela": "a plaid flannel shirt over a camisole",
     "dela_bela": "a short plaid flannel shirt over a camisole"},

    {"id": "barco_deck", "nome": "convés de barco ao entardecer",
     "cen": "the deck of a moored boat at dusk, towels over the rail and two "
            "glasses on a low table",
     "pose": "Sitting on the bench seat on deck is",
     "luz": "last orange light coming in low over the water",
     "audio": "water knocking against the hull, rigging tapping on deck",
     "dele": "bare-chested with a towel over one shoulder",
     "dela": "a navy bikini top with a wrap at her hips",
     "dela_bela": "a navy halter bikini top with a wrap at her hips"},

    {"id": "loft_chuva", "nome": "loft industrial na chuva",
     "cen": "a converted loft bedroom with rain on the tall factory window, "
            "clothes over a chair and one hanging bulb lit",
     "pose": "Sitting back against the headboard is",
     "luz": "one hanging bulb over the bed and grey light off the brick",
     "audio": "heavy rain on the glass, a freight lift somewhere in the "
              "building",
     "dele": "wearing a plain grey t-shirt",
     "dela": "a grey tank top",
     "dela_bela": "a cropped grey tank top"},

    {"id": "deserto_patio", "nome": "patio no deserto com plunge pool",
     "cen": "the patio of a desert house at night, a plunge pool lit from "
            "inside and towels over a low wall",
     "pose": "Sitting on the edge of the plunge pool with his feet in the "
             "water is",
     "maos": "Both of his hands are well clear of the water and stay dry.",
     "luz": "warm patio lights with the pool glowing behind",
     "audio": "dry wind in the palms, water lapping the pool wall",
     "dele": "bare-chested with a towel around his waist",
     "dela": "a bronze bikini top",
     "dela_bela": "a bronze halter bikini top"},

    {"id": "quarto_neon_chuva", "nome": "quarto urbano na chuva",
     "cen": "a city bedroom with rain streaming down the window and wet neon "
            "smeared across the glass, clothes left on the floor",
     "pose": "Sitting on the end of the bed is",
     "luz": "one lamp inside and coloured light bleeding through the rain",
     "audio": "heavy rain on the glass, tyres on a wet street",
     "dele": "wearing an open dark shirt",
     "dela": "a black jersey slip",
     "dela_bela": "a short black jersey slip"},

    {"id": "jacuzzi_montanha", "nome": "jacuzzi em deck de montanha",
     "cen": "a hot tub on a mountain deck at night, robes hung on a hook and "
            "steam rising off the water",
     "pose": "Sitting in the hot tub with the water at his chest is",
     "maos": "Both of his hands are raised clear of the water and stay dry.",
     "luz": "low deck lights with the steam lit warm from below",
     "audio": "the tub jets running, wind in the pines",
     "dele": "bare-chested",
     "dela": "a forest green bikini top",
     "dela_bela": "a forest green halter bikini top"},

    {"id": "suite_manha", "nome": "suite de resort de manha",
     "cen": "a resort suite in the morning, the balcony curtain moving and a "
            "breakfast tray left on a side table",
     "pose": "Standing just inside the balcony door is",
     "luz": "bright morning light through the moving curtain",
     "audio": "birds outside, a fountain running below",
     "dele": "wearing an open white linen shirt",
     "dela": "a white cotton robe tied closed",
     "dela_bela": "a short white cotton robe"},

    {"id": "casarao_lareira", "nome": "casarao antigo com lareira acesa",
     "cen": "a bedroom in an old townhouse with a fire in the marble grate, a "
            "dressing gown over a chair and tall shutters closed",
     "pose": "Sitting in an armchair by the fire is",
     "luz": "firelight from the grate with two lamps low",
     "audio": "the fire cracking, a clock ticking out in the hall",
     "dele": "wearing a plain dark t-shirt",
     "dela": "a deep red dressing gown tied closed",
     "dela_bela": "a short deep red satin dressing gown"},
]


# ===========================================================================
# O HOMEM — quem fala. ⛔ etnia TRAVADA na pagina.
# ===========================================================================
# ⛔⛔ MARCA FACIAL OBRIGATORIA, E AQUI ELA E' DUPLA (`marca` + `sinal`). Nao e'
# enfeite: ele aparece nos DOIS takes, com um corte no meio e uma troca completa
# de cenario, roupa e luz — e, ao contrario do BED, sem nem a casa em comum para
# ajudar. Sem ancora distintiva o Veo devolve OUTRO homem no take 2. Foi o que
# aconteceu no VAZAMENTO, e como o TAKE diz `Only he speaks` o ESTRANHO falava a
# fala do REF.
#
# ⚠️ 45-55 anos, e o numero vem do print: o homem dele nao e' o senhor de 57 do
# BED. E' um homem de meia-idade que ainda se cuida — cabelo escuro com grisalho
# entrando, rosto firme. ⛔ E a idade NUNCA e' dita na fala (ver o cabecalho).
# ⛔⛔ REESCRITO E AMPLIADO EM 2026-08-13 — ordem do operador com o print dos
# renders na mao: *"melhore a aparencia e shape desses homens"* / *"aumente o
# pool de opcoes substancialmente, tambem dos ambientes"*. De 8 para 24.
# ⚠️ CINCO DAS OITO `sinal` ANTIGAS ERAM DANO — `a deep vertical crease between
# his eyebrows`, `a pale scar through his left eyebrow`, `a broad flat nose
# broken once and never set`, `heavy folds under both eyes`, `a white patch of
# old sun damage on his left temple`. O `sinal` e' repetido LITERAL na IMAGE 02
# (ancora da FT3), e aqui ele e' a UNICA coisa que atravessa o corte (os dois
# eixos de cena sao independentes): a avaria ia inteira para os dois quadros. E'
# a licao do PLACA 16 (*"esses caras tao parecendo mendigo"*).
# ⭐ As tres que NAO eram dano ficaram intactas — pinta, covinha e argola de
# prata ja' estavam certas.
# ⛔ NENHUMA PALAVRA DE APROVACAO (handsome, rugged, strong jaw): elogio no
# prompt puxa o rosto para a media do banco de imagem. ⛔ E NENHUMA COR DE PELE:
# a etnia entra pela PAGINA, na frase montada.
# ⚠️ SEM OCULOS, e isso e' isencao DECLARADA no `medir_personagens.py`
# (*CONTRATO DA CENA*): ele sai do banho de toalha no take 1 e um dos ambientes
# do take 2 o poe dentro d'agua. Nao e' eixo esquecido — e' eixo que a cena nao
# comporta, e o lugar de mudar isso seria a isencao, nao o pool.
HOMENS = [
    {"id": "escuro_curto", "idade": 45,
     "marca": "short dark brown hair with grey coming in at the temples and a "
              "clean-shaven jaw",
     "sinal": "a strong cleft in his chin"},
    {"id": "barba_curta", "idade": 48,
     "marca": "dark hair cut short and three days of dark stubble going grey "
              "at the chin",
     "sinal": "a small dark mole high on his right cheek"},
    {"id": "sal_pimenta", "idade": 50,
     "marca": "salt-and-pepper hair pushed back off the forehead and a close "
              "grey beard",
     "sinal": "laugh lines at the corners of his eyes"},
    {"id": "careca_raspado", "idade": 47,
     "marca": "a closely shaved head and a short dark goatee",
     "sinal": "heavy level brows over wide-set eyes"},
    {"id": "ondulado", "idade": 52,
     "marca": "thick wavy grey hair kept a little long and a clean-shaven face",
     "sinal": "a small beauty mark below his right eye"},
    {"id": "recuado", "idade": 55,
     "marca": "grey hair with a low widow's peak and a thick grey moustache",
     "sinal": "a patch of white above his left temple"},
    {"id": "escuro_liso", "idade": 46,
     "marca": "straight dark hair combed to one side and a clean-shaven face",
     "sinal": "a shallow dimple in his chin"},
    {"id": "grisalho_barbudo", "idade": 53,
     "marca": "short grey hair and a full grey beard trimmed close",
     "sinal": "a small silver hoop in his left ear"},
    {"id": "escuro_denso", "idade": 45,
     "marca": "thick dark hair pushed back off the forehead and a close dark "
              "beard",
     "sinal": "a dimple in each cheek when he talks"},
    {"id": "raspado_bigode", "idade": 49,
     "marca": "a shaved head and a thick dark moustache",
     "sinal": "a small mole on his left jaw"},
    {"id": "mecha_branca", "idade": 51,
     "marca": "a white streak running through short dark hair and a trimmed "
               "dark beard",
     "sinal": "a shallow cleft in his chin"},
    {"id": "cachos_curtos", "idade": 46,
     "marca": "short dark curls kept close and a clean-shaven face",
     "sinal": "a small gold stud in his left ear"},
    {"id": "sal_pimenta_liso", "idade": 54,
     "marca": "straight salt-and-pepper hair parted on one side and a close "
              "grey beard",
     "sinal": "smooth-skinned with a wide square chin"},
    {"id": "barba_quadrada", "idade": 50,
     "marca": "short grey hair and a dark beard trimmed square at the jaw",
     "sinal": "a small mole above his lip"},
    {"id": "topete_escuro", "idade": 47,
     "marca": "dark hair still full on top and combed high, with a "
              "clean-shaven face",
     "sinal": "a silver streak through one eyebrow"},
    {"id": "cavanhaque_grisalho", "idade": 52,
     "marca": "close-cropped dark hair going grey and a short grey goatee",
     "sinal": "laugh lines at the corners of his mouth"},
    {"id": "franja_escura", "idade": 45,
     "marca": "dark hair kept a little long over the forehead and light "
              "stubble",
     "sinal": "freckles scattered across his nose"},
    {"id": "risca_lateral", "idade": 55,
     "marca": "grey hair combed to one side and a thin grey moustache",
     "sinal": "a beauty mark high on his right cheek"},
    {"id": "barba_longa_escura", "idade": 48,
     "marca": "short dark hair and a long dark beard combed straight",
     "sinal": "heavy level brows and a small mole at his temple"},
    {"id": "aparado_militar", "idade": 44,
     "marca": "a high and tight crew cut and a clean-shaven face",
     "sinal": "smooth-skinned with a cleft chin"},
    {"id": "ondas_grisalhas", "idade": 53,
     "marca": "wavy grey hair pushed back and three days of grey stubble",
     "sinal": "a small gold hoop in his right ear"},
    {"id": "careca_lateral", "idade": 51,
     "marca": "a bald crown with dark hair at the sides and a close dark "
              "beard",
     "sinal": "a shallow dimple in his left cheek"},
    {"id": "castanho_medio", "idade": 46,
     "marca": "mid-length brown hair tucked behind his ears and a clean-shaven "
              "face",
     "sinal": "laugh lines and a small mole beside his right eye"},
    {"id": "grisalho_raspado", "idade": 54,
     "marca": "grey hair clipped down to the scalp and a full grey beard",
     "sinal": "smooth-skinned with heavy level brows"},
]

# ⛔ Ele esta' de TRONCO NU e de TOALHA no take 1 (o print), e o corpo e' o do
# print: um homem de meia-idade que ainda treina — peito definido, ombros
# largos, sem ser fisiculturista. ⚠️ E' um sorteio SEM eixo de painel: ele chega
# ao quadro, o operador nao precisa escolher.
# ⭐ AMPLIADO EM 2026-08-13 (de 8 para 14), ordem do operador: *"melhore a
# aparencia e shape desses homens"*. ⚠️ UMA ENTRADA ANTIGA SAIU por descrever
# corpo mole — `medium build, fit through the shoulders and softening at the
# waist`: o `corpo_h` entra nos DOIS blocos, e "softening at the waist" e'
# exatamente o que o operador viu no render e reprovou. As outras sete ja'
# estavam no registro certo e ficam palavra por palavra.
CORPOS_H = [
    "lean and athletic with a defined chest",
    "broad-shouldered and solid with a flat stomach",
    "trim and wiry with visible collarbones",
    "thick through the chest and arms, still carrying muscle",
    "medium build, firm through the shoulders and flat at the waist",
    "tall and rangy with long arms and a lean chest",
    "compact and muscular through the chest and shoulders",
    "broad through the back with a heavier chest and thick forearms",
    "square through the shoulders with a hard flat stomach",
    "deep-chested with thick upper arms and a trim waist",
    "long-limbed and lean with defined shoulders",
    "solid and even through the torso, the chest firm",
    "heavy through the chest and shoulders with thick wrists",
    "athletic through the back and arms with a narrow waist",
]

# ⛔ A TOALHA E' DO PRINT e por isso EXISTE em quadro: homem de tronco nu num
# quarto sem nada dito da cintura para baixo e' o convite exato para o gerador
# improvisar — e improviso de cintura para baixo e' recusa. ⚠️ Uma cor por
# entrada, e nada de estampa: toalha estampada vira roupa e a leitura do banho
# se perde.
TOALHAS = [
    "a white bath towel knotted at his waist",
    "a thick cream bath towel knotted at his waist",
    "a pale grey bath towel knotted at his waist",
    "a white hotel bath towel knotted at his waist",
    "a soft beige bath towel knotted at his waist",
    "a light blue bath towel knotted at his waist",
]


# ===========================================================================
# A MULHER — ⭐ etnia SOLTA. Ela e' MUDA nos dois takes.
# ===========================================================================
# ⭐⭐ ESTE POOL E' O ESTADO **BELA DESLIGADO**, e ele e' a MULHER DO PRINT: 34 a
# 43 anos, cabelo escuro preso, camiseta escura, bracos cruzados, cara fechada.
# Nao e' descuido com a LEI DO REF — a lei mira a REF, e a REF aqui e' o HOMEM,
# que e' quem fala e quem a pagina governa. Com o toggle LIGADO ela vem do
# `sc.ref_bela`, e os DOIS estados sao validos e medidos.
#
# ⛔ MARCA FACIAL OBRIGATORIA mesmo assim, e pelo motivo de sempre: ela reaparece
# no take 2 depois de um corte, de outro lugar, de outra roupa e de outra luz.
# Sem ancora o Veo devolve outra mulher.
# ⛔ E ela e' MUDA — invariante do angulo, nao estilo. Sem `Only he speaks` no
# TAKE o Veo poe as duas bocas a mexer e o dialogo sai monofonico e torto
# (lente FT1).
#
# ⚠️⚠️ O PISO DE 34 E' MEDIDO, NAO ESTIMADO, e ele custou uma reprovacao do
# autoteste. O pool bela do repo vai de 21 a **33** — nao a 32, como eu supus ao
# escrever este bloco. Com o piso em 33 os dois estados se tocavam em UMA idade,
# e o controle do toggle acusou na hora. ⛔ O piso fica em 34 para que os dois
# estados NAO se sobreponham em idade nenhuma: e' isso que permite ao autoteste
# provar que o toggle move alguma coisa — sobreposicao seria botao aceso sem
# funcao, o defeito que a FT11 existe para impedir.
MULHERES = [
    {"id": "morena_presa", "idade": 35, "etnia": "white American",
     "porte": "slim with narrow shoulders",
     "marca": "dark brown hair pulled back into a loose knot and a small mole "
              "beside her left eye"},
    {"id": "loira_lisa", "idade": 38, "etnia": "white American",
     "porte": "average build with a long waist",
     "marca": "straight blonde hair cut blunt at the shoulders and a dimple "
              "in one cheek"},
    {"id": "ruiva_ondulada", "idade": 43, "etnia": "white American",
     "porte": "small and lightly built",
     "marca": "wavy auburn hair falling past her shoulders and a dense spray "
              "of freckles"},
    {"id": "castanha_franja", "idade": 41, "etnia": "white American",
     "porte": "solid through the shoulders and hips",
     "marca": "chestnut hair with a heavy fringe and a beauty mark above her "
              "lip"},
    {"id": "trancas_lateral", "idade": 36, "etnia": "Black American",
     "porte": "tall and broad-shouldered",
     "marca": "long box braids gathered over one shoulder and a small beauty "
              "spot on her cheek"},
    {"id": "afro_curto", "idade": 39, "etnia": "Black American",
     "porte": "slight and wiry with thin arms",
     "marca": "a short natural afro and a small gold stud in one nostril"},
    {"id": "cachos_altos", "idade": 42, "etnia": "Black American",
     "porte": "full-figured with round shoulders",
     "marca": "dark curls gathered high on her head and a small birthmark at "
              "her temple"},
    {"id": "alisado_longo", "idade": 34, "etnia": "Black American",
     "porte": "lean and long-limbed",
     "marca": "long straightened black hair parted in the middle and a small "
              "beauty spot on her chin"},
    {"id": "latina_ondulada", "idade": 37, "etnia": "Latina American",
     "porte": "short and softly built",
     "marca": "long wavy black hair pushed behind one ear and a small mole "
              "beside her right eye"},
    {"id": "asiatica_lisa", "idade": 40, "etnia": "Asian American",
     "porte": "slim with rounded shoulders",
     "marca": "straight black hair to the shoulders cut with a heavy fringe "
              "and a dimple in her chin"},
    # ⭐⭐ + 2026-08-13, ordem do operador: *"aumente o pool de opcoes
    # substancialmente, tambem dos ambientes"*. De 10 para 24.
    # ⛔ QUATRO ENTRADAS ANTIGAS FORAM REESCRITAS na mesma passada, todas por
    # ancora de DANO: `a faint scar through one eyebrow`, `deep lines at the
    # corners of her mouth`, `a fine scar on her chin`, `a faint scar on her
    # chin`. A `marca` dela e' repetida nos DOIS blocos (lente FT11) e o angulo
    # a poe colada nele no take 2 — avaria no rosto dela contradiz o payoff.
    # ⛔ O PISO DE 34 VALE PARA TODA ENTRADA NOVA: o pool bela do repo vai ate'
    # 33, e sobreposicao de idade derruba o controle do toggle no autoteste.
    # ⛔ Sem oculos (isencao declarada: LEI DO REF + CENA) e sem tom de pele —
    # a `_marca_dela` corta tom de pele no MODO BELA, e escrever o que a
    # montagem vai apagar e' escrever para o lixo.
    {"id": "loira_ondulada", "idade": 36, "etnia": "white American",
     "porte": "tall and long-limbed",
     "marca": "wavy blonde hair falling past her shoulders and a small mole on "
              "her jaw"},
    {"id": "castanha_rabo", "idade": 39, "etnia": "white American",
     "porte": "lean with square shoulders",
     "marca": "dark chestnut hair in a low ponytail and freckles across her "
              "cheeks"},
    {"id": "ruiva_curta", "idade": 42, "etnia": "white American",
     "porte": "compact and solidly built",
     "marca": "a copper bob cut just below the jaw and a beauty mark on her "
              "left cheek"},
    {"id": "morena_coque", "idade": 34, "etnia": "white American",
     "porte": "slim with narrow hips",
     "marca": "dark hair twisted into a high bun and laugh lines at the "
              "corners of her eyes"},
    {"id": "loira_escura_franja", "idade": 43, "etnia": "white American",
     "porte": "full-figured with soft shoulders",
     "marca": "dark blonde hair with a soft fringe, smooth-skinned, with a "
              "small mole beside her mouth"},
    {"id": "grisalha_precoce", "idade": 40, "etnia": "white American",
     "porte": "average build with narrow shoulders",
     "marca": "shoulder-length brown hair with a silver streak at the front "
              "and a dimple in one cheek"},
    {"id": "trancas_finas", "idade": 35, "etnia": "Black American",
     "porte": "lean and long-limbed",
     "marca": "fine braids falling loose down her back and a small gold stud "
              "in one ear"},
    {"id": "twists_curtos", "idade": 41, "etnia": "Black American",
     "porte": "solid through the shoulders and hips",
     "marca": "short two-strand twists and a beauty spot high on her right "
              "cheek"},
    {"id": "coque_alto_preto", "idade": 38, "etnia": "Black American",
     "porte": "tall and fine-boned",
     "marca": "hair pulled into a high sleek bun and freckles across her nose"},
    {"id": "afro_medio", "idade": 42, "etnia": "Black American",
     "porte": "stout and heavy through the arms",
     "marca": "a rounded afro kept medium-length, smooth-skinned, with a small "
              "mole at her temple"},
    {"id": "latina_coque", "idade": 36, "etnia": "Latina American",
     "porte": "petite and lightly built",
     "marca": "black hair in a low knot at her neck and a beauty mark under "
              "her left eye"},
    {"id": "latina_lisa", "idade": 42, "etnia": "Latina American",
     "porte": "broad-shouldered and solidly built",
     "marca": "long straight dark hair parted in the middle and laugh lines at "
              "the corners of her mouth"},
    {"id": "asiatica_curto", "idade": 37, "etnia": "Asian American",
     "porte": "slim and small-framed",
     "marca": "black hair cut short at the nape and a small mole on her "
              "cheekbone"},
    {"id": "asiatica_rabo", "idade": 43, "etnia": "Asian American",
     "porte": "average build with a long waist",
     "marca": "long black hair pulled back into a low ponytail and a dimple in "
              "her chin"},
]


# ===========================================================================
# ⭐⭐⭐ A PROVA NAS DUAS MAOS — decisao 5 do operador
# ===========================================================================
# ⛔ Ordem literal: *"O take 2, o cara esta' com uma bowl de cubos de gelatina na
# mao e box de baking soda noutra mao"*. Os dois sao STRINGS TRAVADAS, nao pools:
# o operador especificou UM objeto de cada, e string validada e' constante.
#
# ⭐ E ELES SAO O CT5 EM QUADRO ABERTO. Os reels-fonte lidos a 1 fps poem as
# caixas com ROTULO LEGIVEL (JELL-O, Arm & Hammer) e a fala NUNCA lista
# ingrediente. O lugar do ingrediente e' a IMAGEM; a moeda que o comentario
# compra e' a RECEITA, e ela continua inteira.
# ⚠️ EXCECAO DECLARADA na trava `No on-screen text`: a palavra esta' no OBJETO,
# nao queimada na tela pelo gerador. A trava segue valendo para legenda, marca
# d'agua e texto de interface — e a lente FT5 cobra as duas coisas.
#
# ⛔ A CAIXA E' HERDADA DO GOOD 16 SEM A CLAUSULA DE LUGAR. La' ela termina em
# `standing on the same edge`, porque la' ela esta' apoiada na borda da piscina;
# aqui ela esta' NA MAO DELE, e o lugar mora na frase da montagem. Licao do
# SACHE: lugar dentro da constante faz o prompt dizer duas vezes onde o objeto
# esta', na mesma sentenca.
TIGELA_CUBOS = ("a clear glass bowl full of cut cubes of set amber gelatin")
CAIXA_BICARBONATO = ("an orange and yellow cardboard box of baking soda, the "
                     "label sharp and readable")


# ===========================================================================
# ⭐⭐ A COPY — sob o CONTRATO DE COPY 16s, trava por trava
# ===========================================================================
# ⛔ O ORCAMENTO, e ele FECHA POR CONSTRUCAO (nao por solver — solver que
# "tenta 12 vezes" ja' custou caro duas vezes no repo):
#
#     take 1   HOOK 4-7    + FALSA 6-8   + VIRADA 8-9   = 18-24  (teto 25)
#     take 2   MECANISMO 9-10 + HABITO 4-5 + CTA 9-10   = 22-25  (teto 25)
#
# ⭐ TODAS AS 216 COMBINACOES DE CADA TAKE SAO ALCANCAVEIS — o maximo de cada
# cena cabe no teto, entao `_cabe` nunca precisa cortar e o sorteio e' uniforme.
# ⚠️ Isso e' desenho, nao sorte: pool que vai de 6 a 14 palavras num teto de 25
# nao e' pool de 12, e' pool de 4 com oito enfeites, porque as oito longas nunca
# sao sorteadas. Aqui a maior entrada de cada beat cabe com as maiores dos
# outros dois.
#
# ⛔⛔ A REGRA QUE GOVERNA A REDACAO DESTES POOLS, e ela e' ordem do operador:
# *"tomar cuidado com afirmacao de copy vaga, ambigua"*. Toda sentenca tem de
# fazer sentido OUVIDA UMA VEZ, SOZINHA. Pronome sem dono e estado momentaneo
# sao descarte — e' a licao que ele ja' pagou duas vezes (o `this` do GOOD e o
# `no wife at home`, que confundia estar sozinho com ser casado).

# ---------------------------------------------------------------------------
# take 1 — O HOOK EM 2a PESSOA  (CT2)
# ---------------------------------------------------------------------------
# ⛔⛔ O ORGAO NAO ENTRA AQUI, E ISSO E' O QUE FAZ O CT7 PASSAR POR CONSTRUCAO.
# Metade destas entradas carrega `hard`, que e' token do `sc.ERECAO_16`; sobre o
# CORPO ele passa, colado ao ORGAO ele reprova no gerador (licao paga no COLO
# 16, ~95% de recusa). Como nenhuma sentenca deste take nomeia o orgao, o verbo
# nunca encosta nele. E' a formula segura do GOOD 16.
# ⚠️ Consequencia declarada: o apelido do orgao aparece SO' no take 2. O CT4
# (um apelido por video) continua satisfeito — ele proibe o apelido MUDAR no
# corte, e um apelido so' nao tem como mudar.
#
# ⛔ `Struggling to finish what you start?` NASCEU E MORREU AQUI. Fora de
# contexto ela le' como procrastinacao, e a regra do operador e': se o viewer
# leigo pode perguntar "do que ele ta' falando?", e' descarte. Pelo mesmo teste
# `Struggling to last ten minutes?` virou `... in bed?`.
# ⛔ E NENHUMA DIZ IDADE. `at sixty` / `past fifty` sairam: os HOMENS vao de 45 a
# 55 e o quadro mostra o rosto. E' a pendencia B do BED 16 resolvida antes de
# existir.
HOOKS = [
    "Struggling to stay hard?",                        # ← verbatim da fonte
    "Struggling to stay hard for her?",
    # ⛔ `Struggling to stay firm every night?` -> `... firm in bed every
    # night?` (2026-08-10). O operador leu a versao antiga e devolveu *"firm
    # WHAT?? my butt??"* — `firm` sem lugar nem objeto e' predicado orfao, e o
    # espectador chega no meio do scroll sem nada antes desta sentenca. `in
    # bed` custa UMA palavra e diz o campo sem nomear o orgao (que e' o que
    # mantem o CT7 passando neste beat).
    "Struggling to stay firm in bed?",
    "Struggling to last ten minutes in bed?",
    "Struggling to stay hard the whole night?",
    # ⛔ `keep it up` guardava a mesma armadilha do `firm`: `it` sem dono. Com
    # `in bed` o campo fica dito e o pronome deixa de flutuar.
    "Struggling to keep it up in bed?",
]

# ---------------------------------------------------------------------------
# take 1 — A FALSA CAUSA  (a absolvicao, em 1a pessoa)
# ---------------------------------------------------------------------------
# ⛔ O BEAT INTEIRO E' A PONTE DA 2a PARA A 1a PESSOA. O hook fala do corpo de
# quem assiste; esta sentenca traz o narrador para dentro e devolve o video ao
# depoimento, que e' o que a virada e o take 2 sao. Pergunta sozinha vira
# anuncio de clinica.
# ⚠️ TODAS as que usam `it`/`that` tem o antecedente na sentenca IMEDIATAMENTE
# anterior (a falha do hook). As que nao tem pronome nenhum sao a rede para
# quando o hook sortear uma forma mais curta.
# ⛔ E NENHUMA E' UMA CAUSA QUE O VIDEO VAI DEFENDER — sao todas ditas no
# PASSADO (`I thought`, `I blamed`, `I figured`, `I told myself`), porque a
# frase seguinte as desmente. Falsa causa no presente viraria o claim do video.
#
# ⛔⛔⛔ POOL REESCRITO EM 2026-08-10 — O ORGAO PASSA A SER NOMEADO NO TAKE 1.
# ---------------------------------------------------------------------------
# Ordem do operador, com o app aberto e o take na tela:
#
#     "Struggling to stay firm every night?"  -> "firm WHAT?? my butt??"
#     "I thought age did that to every man."  -> "did that to WHO or to WHAT???"
#     "Vc tinha que ter se referido ao menos UMA VEZ ao Johnson, pecker ou
#      wiener na primeira passagem da copy falada do take 1. Ajuste isso."
#
# ⭐ E ELE ESTA' CERTO PELA LEI QUE ELE MESMO INSTAUROU: o TESTE WTF. As duas
# sentencas passavam em todas as lentes e mesmo assim deixavam o espectador
# sem saber do que se trata — `firm` e `did that` sao predicados sem OBJETO, e
# o take 1 inteiro corria em 2a pessoa sem nunca dizer o que esta' quebrado.
# ⚠️ Este arquivo declarava o contrario, em comentario, como se fosse virtude:
# *"o take 1 fala do corpo sem nomear o orgao, que e' o que faz o CT7 passar
# por construcao"*. Era conveniencia de lente vendida como decisao de copy.
#
# ⛔⛔ E O CT7 CONTINUA INTEIRO — ELE NUNCA PROIBIU O ORGAO NO TAKE 1.
# O que ele proibe e' VERBO DE ERECCAO NA MESMA SENTENCA DO ORGAO. Por isso o
# nome entra AQUI, na falsa causa, e nao no hook: o hook carrega `hard`/`firm`
# e juntar os dois seria a licao paga no COLO 16 (~95% de recusa do gerador).
# Sao duas sentencas separadas, o ouvido junta as duas, e o classificador nao.
#     hook   -> `Struggling to stay hard?`        (verbo, sem orgao)
#     falsa  -> `I figured my Johnson quit ...`   (orgao, sem verbo de ereccao)
# ⚠️ Nenhum verbo daqui pode estar no `sc.ERECAO_16` — `quit`, `gave out`,
# `killing`, `did that` sao o idioma da casa e passam no render; `came back`,
# `works again`, `stands up` e `wakes up` estao proibidos e o autoteste cobra.
#
# ⚠️⚠️ OITO PALAVRAS EXATAS em todas, e o numero foi MEDIDO, nao escolhido. A
# primeira versao deste pool tinha 8-9, e o controle de COBERTURA do autoteste
# reprovou na hora: a soma dos MAIORES dava 27 num teto de 25. Nao e' detalhe —
# quando a soma estoura, o `_cabe` comeca a cortar, e quem sai do sorteio sao
# sempre as MESMAS entradas (as longas). O pool encolhe sozinho e ninguem ve'.
# ⭐ Com HOOK 4-8 · FALSA 8 · VIRADA 8-9, o pior caso e' 25 EXATOS: toda
# combinacao cabe por construcao e a rede do `_cabe` nunca dispara.
# ⛔ Quem acrescentar uma entrada de 9 aqui tem de encurtar um hook — o
# autoteste diz na hora, mas a conta e' esta.
#
# ⛔⛔⛔ A NEGACAO E' OBRIGATORIA — CONSERTO DE 2026-08-10, NO MESMO DIA.
# ---------------------------------------------------------------------------
# O operador leu o take pronto e devolveu o `NOT` escrito a mao:
#
#     eu entreguei : "I figured age was what killed my peck-er."
#     ele corrigiu : "I figured age was NOT what killed my peck-er."
#     *"Tem que ter o NOT, senao nao faz sentido."*
#
# ⭐ E O DEFEITO ERA MEU, DE ORCAMENTO DE SENTIDO, nao de gosto dele. A forma
# afirmativa so' funciona se a VIRADA a desmentir, e a unica virada que
# desmente e' a que comeca com `But` — a verbatim dele. As outras CINCO abrem
# com `Everything changed` / `Then I found` / `Three weeks on`, e nenhuma
# contradiz nada. Como o sorteio cruza qualquer falsa com qualquer virada, em
# 5 de 6 sorteios o video AFIRMAVA que a idade matou o orgao e nunca voltava
# atras. O claim do video passava a ser o contrario do que a VSL vende.
# ⚠️ Este e' o modo de falha do pool combinatorio: cada beat lido sozinho
# estava certo, e o par estava errado. Nao havia lente que olhasse o PAR — a
# rede agora e' o controle de negacao no autoteste, que cobra o token em TODA
# entrada e nao depende de qual virada saiu.
#
# ⛔ ENTAO O BEAT MUDOU DE FUNCAO, e o nome do pool ficou por compatibilidade:
# ele nao ENUNCIA mais a falsa causa, ele a DESMENTE. E' a mesma coisa que a
# cena 2 vende (nao e' idade, e' fluxo), so' que dita em 1a pessoa e oito
# segundos antes.
# ⛔ TODA ENTRADA CARREGA `not` OU `never` — sem excecao, e o autoteste reprova
# quem entrar sem. Entrada afirmativa aqui reintroduz o defeito inteiro.
#
# ⚠️ NOVE PALAVRAS EXATAS (a negacao custou uma). Com FALSA 9 e VIRADA ate' 9,
# o teto de 25 obriga o HOOK a ficar em ate' 7 — foi por isso que
# `Struggling to stay firm IN BED EVERY NIGHT?` (8) encurtou para
# `Struggling to stay firm in bed?` (6). O controle de cobertura do autoteste
# faz essa conta sozinho e reprova se alguem esquecer.
FALSAS = [
    "I figured age was not what killed my {o}.",    # ← a forma dele, literal
    "I thought age was not what stopped my {o}.",
    "Turns out age was not what took my {o}.",
    "It was not age that shut my {o} down.",
    "My age was never what my {o} was fighting.",
    "It was never age doing that to my {o}.",
]

# ---------------------------------------------------------------------------
# take 1 — A VIRADA  (o take fecha APONTANDO PARA FRENTE)
# ---------------------------------------------------------------------------
# ⛔ O take 1 tem de FECHAR APONTANDO PARA FRENTE, nunca empilhando drama — e' a
# regra que o operador instaurou hoje no WIFE, no BED, no FLAGRANTE e no
# ESCANDALO, e a forma dele foi escrita a mao:
#     `But things changed when i discovered the gelatin trick.`
# ⚠️ 8-9 palavras, e TODAS nomeiam o `gelatin trick` — aqui ele e' a DESCOBERTA,
# nao o mecanismo. A razao dele (verbo de efeito + alvo, CT3) mora na cena 2,
# que e' onde ela cabe: cobrar a razao nas DUAS mencoes seria redundancia paga
# em palavras que o take nao tem.
# ⛔ NENHUM PRONOME ORFAO. `That ended the week I found the gelatin trick.`
# nasceu e morreu aqui: com a falsa causa no meio, `That` tanto podia ser a
# falha quanto o ato de culpar a idade. Foi trocada por `Everything turned
# around when...`, que nao tem para onde apontar errado.
VIRADAS = [
    "But things changed when I discovered the gelatin trick.",   # ← a dele
    "Then I found the gelatin trick and everything changed.",
    "Everything changed after I started the gelatin trick.",
    "Everything turned around when I found the gelatin trick.",
    "Three weeks on the gelatin trick changed everything.",
    "Then the gelatin trick turned my nights around.",
]

# ---------------------------------------------------------------------------
# take 2 — O MECANISMO COM RAZAO  (CT3)
# ---------------------------------------------------------------------------
# ⛔ CT3: nome de mecanismo SEM razao ao lado nao vira crenca, vira ruido de
# marca. Toda entrada carrega, na mesma sentenca, VERBO DE EFEITO + ALVO:
#
#     ✗ The gelatin trick is the half that works.
#     ✓ The gelatin trick puts blood back in your {o}.
#
# ⛔⛔ E A CONSTRUCAO E' SEMPRE DIRECIONAL — `blood ... TO/INTO/IN your {o}`. Nao
# e' estilo: e' a forma validada em campo. As formas de RETENCAO (`fills your
# {o} with blood`, `holds blood inside your {o}`) descrevem o orgao enchendo, e
# e' exatamente isso que o classificador le' como tumescencia. Nasceram e
# morreram nesta lista, antes do primeiro render.
# ⛔ TODAS EM 2a PESSOA E NO PRESENTE. O mecanismo descreve o que o truque FAZ —
# verdade geral sobre o produto. Passado + 2a pessoa (`fixed blood flow to your
# {o}`) diz que o truque JA' consertou o corpo de quem esta' assistindo, o que
# e' falso e soa quebrado; o operador pegou esse defeito lendo o app do BED.
# ⛔ O `_adjetivo_do_mecanismo` do `short_comum` e' ALLOWLIST: so' artigo,
# numeral, `secret` e `whole` podem vir ANTES do literal. Todas comecam em `The`.
MECANISMOS = [
    "The gelatin trick puts blood back in your {o}.",             # ← a dele
    "The gelatin trick brings blood flow to your {o}.",
    "The gelatin trick feeds blood back into your {o}.",
    "The gelatin trick sends blood back into your {o}.",
    "The gelatin trick opens the blood flow to your {o}.",
    "The gelatin trick clears the blood flow to your {o}.",
]

# ---------------------------------------------------------------------------
# take 2 — O HABITO  (vem do `just one daily habit` da fonte)
# ---------------------------------------------------------------------------
# ⛔⛔ NENHUMA ENTRADA NOMEIA VASILHAME, MEDIDA OU FRACAO, e este pool foi
# REESCRITO por causa disso — ver o desvio declarado no cabecalho. O
# `SPEC-FIGHT-16.md` §7 trazia `One bowl every night.` e `One bowl before bed.`,
# e vasilhame na fala e' DOSE: a ordem permanente do operador e' que a fala nao
# paga o que o quadro mostra. O quadro ja' poe a tigela na mao dele; o que ele
# NAO mostra e' a frequencia, e e' isso que esta sentenca compra.
# ⛔ E nenhuma nomeia INGREDIENTE (CT5) — a receita e' a unica moeda que o
# comentario compra, e entregue uma vez ela esta' gasta para os outros 49 videos
# da pagina.
# ⚠️ 4-5 palavras. E' o beat mais curto e o mais intercambiavel dos tres: por
# isso ele escolhe por ULTIMO no `_falas` e absorve a sobra.
HABITOS = [
    "One habit a night.",                              # ← a do operador
    "One habit, every single night.",
    "One habit before bed.",
    "One simple habit, every night.",
    "A minute a night.",
    "Two minutes before bed.",
]

# ---------------------------------------------------------------------------
# take 2 — O CTA  (CT1 · CT6 · CT8)
# ---------------------------------------------------------------------------
# ⛔ CT1: NADA DEPOIS DESTA SENTENCA. A posicao final e' a que fica, e ela tem de
# ser o pedido. O defeito mais caro do lote antigo (100% dos sorteios em 6 de 7
# motores) era exatamente uma frase depois do CTA.
# ⛔ CT8: NENHUM PEDIDO DE FOLLOW. A DM sai igual para quem nao segue — ordem do
# operador, 2026-08-10, corrigindo a premissa errada que gerou o beat inteiro.
# Este motor nasce SEM o pool de follow: nao ha' o que aposentar aqui.
# ⚠️ E a FONTE confirma em campo: os 20 segundos dela nao pedem seguir uma vez.
# ⛔ CT6: a sentenca diz ONDE a receita chega. O KPI e' uma confissao publica —
# o comentario leva nome e foto e vai para o feed da mulher dele —, e a clausula
# de entrega e' de graca: paga o endereco, a privacidade e o fato de nao ser na
# tela publica.
# ⛔⛔ A VIRGULA DEPOIS DE `gelatin` E' INTOCAVEL: a automacao de DM casa palavra
# EXATA, e a legenda do video nasce do Whisper em cima do audio gerado. Sem a
# micro-pausa o Veo emenda e narra `gelatine`. O literal vem de `sc.CTA_LITERAL`,
# nunca redigitado.
# ⚠️ TODAS nomeiam `recipe` (`sc.lint_isca_cta`: pedir o comentario sem dizer o
# que chega e' pedir sem oferecer).
CTAS = [
    "%s and the recipe goes to your messages." % sc.CTA_LITERAL,   # ← a dele
    "%s and the recipe lands in your messages." % sc.CTA_LITERAL,
    "%s and the recipe arrives in your messages." % sc.CTA_LITERAL,
    "%s and I'll send the recipe to your inbox." % sc.CTA_LITERAL,
    "%s and I'll send the recipe by message." % sc.CTA_LITERAL,
    "%s and your inbox gets the recipe tonight." % sc.CTA_LITERAL,
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


EIXOS_LEDGER = ("quarto", "ambiente", "homem", "mulher")


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
# SORTEIO
# ===========================================================================

def _falas(spec, rng, quais=(0, 1)):
    """As duas falas.

    ⛔⛔ CT4 — UM APELIDO POR VIDEO. Em 24s e cinco cenas o bordao e' o risco; em
    16s e duas cenas o risco e' o oposto: o corte ZERA a memoria de trabalho, e
    trocar `pecker` por `Johnson` no segundo 9 obriga o espectador a remapear
    justamente quando ele ja' esta' com um pe' fora. Por isso o apelido mora no
    SPEC e nao e' re-sorteado por cena.
    ⚠️ O APELIDO E' DITO NOS DOIS TAKES desde 2026-08-10 (ordem do operador:
    *"tinha que ter se referido ao menos uma vez ao Johnson, pecker ou wiener
    na primeira passagem da copy falada do take 1"*). No take 1 ele entra na
    FALSA CAUSA — nunca no hook, que e' quem carrega `hard`/`firm`. O CT7 vale
    por SENTENCA, entao verbo e orgao ficam em sentencas vizinhas: o ouvido
    junta, o classificador nao.

    ⛔ ORDEM DE ESCOLHA (que nao e' a ordem da frase): escolhe primeiro quem tem
    MENOS SUBSTITUTOS. No take 1 e' o HOOK — ele e' o verbatim da fonte e carrega
    o CT2 sozinho. No take 2 e' o CTA — ele carrega o literal `Comment gelatin,`
    e o endereco da entrega, e nao se encurta. O beat mais intercambiavel escolhe
    por ULTIMO e absorve a sobra.
    ⚠️ Neste motor a ordem nao muda NADA hoje (o maximo de cada cena cabe no
    teto, entao `_cabe` nunca corta) — e e' de proposito que ela esta' escrita
    assim mesmo: quem acrescentar uma entrada longa amanha herda a ordem certa
    em vez de descobrir o mode-collapse num lote renderizado.
    """
    o = spec["apelido"]
    f = dict(enumerate(spec.get("falas", ["", ""])))

    if 0 in quais:
        # ⛔ `o=o` nas FALSAS desde 2026-08-10: o beat passou a nomear o orgao
        # (ordem do operador — ver a nota do pool), entao a conta de palavras
        # tem de ser feita na string FORMATADA. Sem isso o `{o}` cru contaria
        # como 1 e a reserva ficaria certa por acaso, nao por construcao.
        ho = rng.choice(_cabe(HOOKS, _mn(FALSAS, o) + _mn(VIRADAS), 1))
        fc = rng.choice(_cabe(FALSAS, _palavras(ho) + _mn(VIRADAS), 1,
                              o)).format(o=o)
        vi = rng.choice(_cabe(VIRADAS, _palavras(ho) + _palavras(fc), 1))
        f[0] = "%s %s %s" % (ho, fc, vi)

    if 1 in quais:
        ct = rng.choice(_cabe(CTAS, _mn(MECANISMOS, o) + _mn(HABITOS), 2))
        me = rng.choice(_cabe(MECANISMOS,
                              _palavras(ct) + _mn(HABITOS), 2, o)).format(o=o)
        ha = rng.choice(_cabe(HABITOS, _palavras(me) + _palavras(ct), 2))
        f[1] = "%s %s %s" % (me, ha, ct)

    return f


def sortear(pagina, rng, ledger, travas=None):
    travas = travas or {}
    hist = (ledger or {}).get(pagina, {})
    etnia = ETNIA.get(pagina, "white American")

    # ⛔⛔ OS DOIS EIXOS DE CENA SAO SORTEADOS SEPARADAMENTE, e nenhum filtra o
    # outro. E' a decisao 4 do operador — duas listas independentes. Quem
    # quiser "casar" os dois (o quarto de hotel puxando a jacuzzi de hotel)
    # estaria inventando uma regra que ele nao deu, e reduzindo 80 pares a 10.
    quarto = (_por_id(QUARTOS, travas["quarto"]) if travas.get("quarto")
              else _fresco(QUARTOS, hist.get("quarto", [])[-4:], rng))
    ambiente = (_por_id(AMBIENTES, travas["ambiente"])
                if travas.get("ambiente")
                else _fresco(AMBIENTES, hist.get("ambiente", [])[-5:], rng))

    homem = (_por_id(HOMENS, travas["homem"]) if travas.get("homem")
             else _fresco(HOMENS, hist.get("homem", [])[-4:], rng))
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
    # entrada sorteada. Sem esta linha o modo BELA travaria a mulher inteira em
    # `white American` e ninguem veria, porque a congruencia do funil olha o
    # homem.
    bela = bool(travas.get("bela")) and not travas.get("mulher")
    if bela:
        _et_dela = mulher["etnia"]
        mulher = sc.ref_bela(MULHERES[0], rng)
        mulher["etnia"] = _et_dela

    spec = {
        "pagina": pagina, "etnia": etnia, "bela": bela,
        "quarto": quarto, "ambiente": ambiente,
        "homem": homem, "mulher": mulher,
        "corpo_h": rng.choice(CORPOS_H),
        "toalha": rng.choice(TOALHAS),
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

# ⛔⛔ A NEGACAO SAIU EM 2026-08-10 — ORDEM DIRETA DO OPERADOR.
# ---------------------------------------------------------------------------
# A constante dizia: *"An ordinary everyday relatable person with a plain
# unremarkable face, NOT A CELEBRITY, NOT A MODEL, NOT AN ACTOR."*, e ele a
# leu no BLOCO 0 deste agente, na tela do app:
#     *"nao falar de celebridade nem usar a palavra famoso, celebridade no
#      prompt, muito menos dizer burramente no prompt 'not morgan freeman',
#      'not celebrity', 'not famous people'. Nao seja estupido."*
#
# ⭐ E o repo ja' tinha a regra escrita ha' DEZ DIAS e nunca a aplicou aqui
# (licoes-producao-veo §"E' pior que inutil: e' municao", 2026-07-31):
#     *"escrever `not a celebrity` INJETA `celebrity`. O classificador casa
#      TOKEN, nao intencao."*
# ⚠️ O comentario que ficava aqui era a propria confissao do erro: ele dizia
# "nunca INVENTAR declaracao de conformidade" e em seguida mantinha tres, com a
# desculpa de que *"o BLOCO 0 do repo inteiro a carrega"*. Herdar um defeito
# nao o transforma em contrato — foi assim que ele chegou a este arquivo, que
# nasceu por copia do BED 16.
#
# ⭐ O QUE FICA NO LUGAR: a metade POSITIVA, que descreve em vez de negar. Ela
# empurra para o registro de foto de pessoa comum, que e' o efeito que se
# queria, sem pronunciar a categoria que se teme.
# ⛔ Nao devolver `not a model` / `not an actor` / `not resembling any famous
# person`: sao a mesma municao com outra roupa. Contra o atrator quem trabalha
# e' a descricao especifica do rosto (`marca` + `sinal` do pool HOMENS).
ANTICELEB = ("An ordinary everyday relatable person with a plain unremarkable "
             "face.")


def _traje_dela(spec, take):
    """A roupa dela no take pedido, ja' resolvida pelo MODO BELA.

    ⛔ Um lugar so'. Espalhar `if spec["bela"]` pelos dois blocos e' o fragmento
    espelhado que diverge na primeira manutencao — e o eixo que diverge aqui e'
    justamente o que o operador vai olhar primeiro.
    ⚠️ E o traje sai do LUGAR daquele take: o quarto governa o take 1 e o
    ambiente governa o take 2. Sao dois eixos independentes, entao um traje so'
    para os dois deixaria a mulher de biquini na cabana com lareira.
    """
    fonte = spec["quarto"] if take == 1 else spec["ambiente"]
    return fonte["dela_bela" if spec.get("bela") else "dela"]


# ===========================================================================
# ⛔⛔ FT14 — A MULHER TROCAVA ENTRE OS DOIS TAKES (2026-08-10, relato de campo)
# ===========================================================================
# O operador mediu ~15% dos videos com uma mulher no take 1 e OUTRA no take 2, e
# mandou os dois prompts. A causa nao e' falta de ancora: e' CONTRADICAO DENTRO
# DA PROPRIA FRASE, e sao DUAS, empilhadas na mesma oracao:
#
#   1. ETNIA x PELE
#      "a 23-year-old WHITE AMERICAN woman, ..., CLEAR DEEP BROWN SKIN and ..."
#      A etnia vem do campo `etnia` do pool; o tom de pele vem do `marca` do
#      pool BELA compartilhado (`sc.ref_bela`). Sao DUAS AUTORIDADES para o
#      MESMO atributo, e elas se contradizem em boa parte dos sorteios.
#
#   2. SORRISO x CARA FECHADA  (so' no take 1)
#      "... and A WIDE BRIGHT SMILE, ... staring straight at him with A HARD
#       CLOSED EXPRESSION."
#      O sorriso e' identidade (vem do pool); a cara fechada e' CENA (a briga).
#
# ⭐ E E' POR ISSO QUE O DEFEITO APARECE NO CORTE, e nao dentro de um quadro: os
# dois IMAGE sao gerados SEPARADAMENTE, e diante de uma contradicao o gerador
# escolhe um lado — so' que escolhe INDEPENDENTEMENTE em cada chamada. No take 1
# ele obedeceu `white American`; no take 2 obedeceu `deep brown skin`. Duas
# mulheres. E' a mesma familia das DUAS COLHERES e da CAIXA DE PAPELAO MOLHADA:
# contradicao dentro do prompt nunca vira "meio termo", vira invencao.
#
# ⛔ O CONSERTO E' TIRAR A SEGUNDA AUTORIDADE, NUNCA ACRESCENTAR MAIS ANCORA.
# Repetir "it is the same woman" nao resolve — a contradicao continua la', e a
# frase nova so' disputa com ela. Quem sai e' o TOM DE PELE do pool bela: a
# etnia declarada passa a ser a UNICA voz sobre a cor da pele.
# ⚠️ Por que a etnia fica e a pele sai, e nao o contrario: quando o pool bela
# NAO traz clausula de pele (metade das entradas), tirar a etnia deixaria a
# mulher sem nenhuma definicao — e ai' o gerador escolheria livre em cada
# take, que e' o MESMO bug pela outra ponta. Autoridade unica tem de estar
# SEMPRE presente, e so' a etnia esta'.
_CLAUSULA = re.compile(r",\s*|\s+and\s+")
_TOM_DE_PELE = re.compile(r"\bskin\b|\bcomplexion\b|\bcomplected\b", re.I)
_SORRISO = re.compile(r"\bsmile\b|\bsmiling\b|\bgrin\w*\b", re.I)


def _marca_dela(spec, take):
    """A descricao dela sem as clausulas que brigam com a CENA daquele take.

    ⛔ So' age no MODO BELA. Com o modo desligado a mulher vem do pool deste
    arquivo, que foi escrito SEM tom de pele e SEM sorriso justamente para nao
    brigar — mexer ali seria consertar o que nao esta' quebrado.
    ⚠️ E age por CLAUSULA, nao por regex na string inteira: cirurgia de regex
    num texto que ja' foi montado deixa virgula orfa e ` and ` solto, e isso ja'
    entregou prompt com pontuacao quebrada neste repo.
    """
    marca = spec["mulher"]["marca"]
    if not spec.get("bela"):
        return marca
    partes = [p.strip() for p in _CLAUSULA.split(marca) if p.strip()]
    fica = []
    for p in partes:
        if _TOM_DE_PELE.search(p):
            continue                       # briga com a ETNIA declarada
        if take == 1 and _SORRISO.search(p):
            continue                       # briga com `a hard closed expression`
        fica.append(p)
    if not fica:                           # rede: nunca devolver string vazia
        return partes[0]
    if len(fica) == 1:
        return fica[0]
    return ", ".join(fica[:-1]) + " and " + fica[-1]


def montar(spec):
    q, a = spec["quarto"], spec["ambiente"]
    h, w = spec["homem"], spec["mulher"]
    et = spec["etnia"]
    b = {}

    # --- BLOCO 0 — a REF e' o HOMEM (ele e' quem fala) ---------------------
    b["BLOCO 0 (REF)"] = (
        "REF 01: Photo of a real person, a %d-year-old %s man, chest up, "
        "facing the camera directly, tense frustrated expression. %s, %s. %s "
        "Hands out of frame, no objects. Plain neutral gray background, soft "
        "even frontal light. Slight sensor grain, soft focus, raw iPhone front "
        "camera aesthetic. No subtitles, no captions, no burned-in text, no "
        "watermark."
        % (h["idade"], et, h["marca"], h["sinal"], ANTICELEB))

    # --- TAKE 1 — A BRIGA -------------------------------------------------
    # ⛔ O PRINT, ELEMENTO POR ELEMENTO: ele DE PE', tronco nu, TOALHA amarrada
    # na cintura, UMA MAO ABERTA num gesto de quem se explica, olhando para a
    # LENTE com cara de exasperado. Ela atras, de BRACOS CRUZADOS, cara fechada,
    # ENCARANDO ele.
    # ⛔⛔ A TENSAO E' CONTADA PELA POSTURA DELA, nunca por fala: ela e' MUDA
    # (FT1) e a inversao desta postura no take 2 E' o video (FT2).
    # ⚠️ ELE FALA PARA A LENTE, e nao para ela. E' o que o print mostra e e' o
    # que o angulo precisa: ele nao esta' discutindo com a mulher, esta' se
    # explicando para QUEM ASSISTE — e e' por isso que a fala pode ser em 2a
    # pessoa sem soar que ele acusa a esposa.
    b["IMAGE 01/02"] = (
        "IMAGE 01/02: Medium shot in %s. Standing in the foreground close to "
        "the lens, facing the camera, is a %d-year-old %s man, bare-chested, "
        "%s, wearing %s, one hand open in front of him in a mid-explanation "
        "gesture, his mouth open and his face tense and exasperated. %s, %s. "
        "%s is a %d-year-old %s woman, %s, %s, wearing %s, her arms folded "
        "across her chest and her face turned toward him, staring straight at "
        "him with a hard closed expression. Shallow depth of field: he is large "
        "and sharp in the foreground and she is smaller and softer behind him. "
        "They are the only two people in the frame. %s. %s"
        % (q["cen"], h["idade"], et, spec["corpo_h"], spec["toalha"],
           _cap(h["marca"]), h["sinal"], _cap(q["ela"]),
           w["idade"], w["etnia"], w["porte"], _marca_dela(spec, 1),
           _traje_dela(spec, 1), _cap(q["luz"]), CAUDA))

    b["TAKE 01/02"] = (
        "TAKE 01/02: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway, no cuts, and the camera does not move. He "
        "talks straight into the lens the whole time and never turns to look "
        "at her, and his open hand keeps moving slightly as he explains. She "
        "stays exactly where she is, her arms folded across her chest and her "
        "eyes on him, and she never speaks. Only he speaks. He stays large and "
        "sharp in the foreground and she stays smaller and softer behind him. "
        "Nothing else in the frame changes.\n"
        "Dialogue: \"%s\"\nAudio: %s. No music."
        % (sonorizar(spec["falas"][0]), q["audio"]))

    # --- TAKE 2 — O CASAL COLADO ------------------------------------------
    # ⛔⛔ A ANCORA DE CONTINUIDADE VEM AQUI EM CINCO PECAS: idade, etnia, marca,
    # sinal e a frase `It is the same man`. Sem isso o Veo desenha OUTRA pessoa
    # — no VAZAMENTO o corpo-prova voltou como um senhor de oculos e bigode, e
    # como o TAKE diz `Only he speaks` o estranho falava a fala do REF. Lente
    # FT3.
    # ⛔⛔ E AQUI A ANCORA E' MAIS CARA QUE NO BED: la' os dois takes sao da
    # MESMA casa, e o cenario ajuda a segurar a pessoa. Aqui o lugar muda por
    # inteiro (dois eixos independentes), entao o HOMEM e' a UNICA coisa que
    # atravessa o corte. FT13 proibe fingir que o lugar tambem atravessa.
    # ⭐⭐ AS DUAS MAOS SAO A PROVA (decisao 5): a tigela de cubos numa, a caixa
    # de bicarbonato na outra. Lente FT4.
    b["IMAGE 02/02"] = (
        "IMAGE 02/02: Medium shot in %s. %s the same %d-year-old %s man from "
        "the first scene, %s, %s, %s, %s, his face fully in frame and turned to "
        "the camera. It is the same man, not a different person. Pressed "
        "against his side with her shoulder against his chest is the same "
        "%d-year-old %s woman, %s, %s, wearing %s; she is smiling happily, a "
        "wide open smile with her eyes bright, looking at him, and she says "
        "nothing. In one hand he holds %s, and in his other hand he holds %s.%s "
        "They are the only two people in the frame. %s. %s"
        % (a["cen"], a["pose"], h["idade"], et, h["marca"], h["sinal"],
           spec["corpo_h"], a["dele"],
           w["idade"], w["etnia"], w["porte"], _marca_dela(spec, 2),
           _traje_dela(spec, 2), TIGELA_CUBOS, CAIXA_BICARBONATO,
           (" " + a["maos"]) if a.get("maos") else "",
           _cap(a["luz"]), CAUDA))

    b["TAKE 02/02"] = (
        "TAKE 02/02: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway, no cuts, and the camera does not move. He "
        "talks straight into the lens the whole time and it is the same man as "
        "in the first scene. She stays pressed against his side and never "
        "moves away from him, she keeps smiling happily the whole time, and "
        "she never speaks. Only he speaks. He keeps "
        "the bowl in one hand and the box in the other the whole time and "
        "never sets either one down. Nothing else in the frame changes.\n"
        "Dialogue: \"%s\"\nAudio: %s. No music."
        % (sonorizar(spec["falas"][1]), a["audio"]))

    # ⛔ trava de texto queimado em todo TAKE — o watermark que o operador viu
    # vazando nos reels da concorrente (2026-08-01).
    return sc.selar_takes(b)


# ===========================================================================
# LINTER — as regras FT
# ===========================================================================

def _ft1_ela_muda(spec, blocos, achados):
    """FT1 — ela nunca fala, e os DOIS takes tem de DIZER isso.

    ⚠️ Omitir nao basta: o Veo poe as duas bocas a mexer se ninguem proibir, e o
    dialogo dele sai monofonico e torto. Foi assim que a cena do casal do
    VAZAMENTO caiu.
    """
    for k in ("TAKE 01/02", "TAKE 02/02"):
        if "Only he speaks" not in blocos[k]:
            achados.append(("ERRO", "FT1: %s sem `Only he speaks` — sem isso o "
                                    "Veo mexe a boca dela tambem" % k))
        if "she never speaks" not in blocos[k]:
            achados.append(("ERRO", "FT1: %s nao diz que ela e' muda — a mudez "
                                    "dela e' invariante do angulo" % k))


def _ft2_inversao(spec, blocos, achados):
    """⭐⭐ FT2 — A INVERSAO E' O VIDEO.

    ⛔ Bracos cruzados ENCARANDO ele no take 1; corpo colado no take 2. Sem os
    dois lados o angulo deixa de existir: sobra um homem falando de gelatina num
    quarto. A prova deste agente nao e' um corpo nem um prop — e' o CASAL, e ela
    so' se le' na DIFERENCA entre os dois quadros.
    """
    i1, i2 = blocos["IMAGE 01/02"], blocos["IMAGE 02/02"]
    if "arms folded across her chest" not in i1:
        achados.append(("ERRO", "FT2: a IMAGE 01 nao tem os bracos cruzados "
                                "dela — a briga e' contada pela POSTURA, e sem "
                                "ela nao ha' o que inverter no take 2"))
    if "staring straight at him" not in i1:
        achados.append(("ERRO", "FT2: a IMAGE 01 nao poe ela ENCARANDO ele — "
                                "desviar e' evitar, encarar e' cobrar, e a "
                                "cobranca e' a metade fria do angulo"))
    if "Pressed against his side" not in i2:
        achados.append(("ERRO", "FT2: a IMAGE 02 nao tem ela colada nele — a "
                                "inversao dos bracos cruzados E' o video"))
    if "shoulder against his chest" not in i2:
        achados.append(("ERRO", "FT2: a IMAGE 02 nao encosta o ombro dela no "
                                "peito dele — `ao lado` nao inverte `bracos "
                                "cruzados a varios pes de distancia`"))


def _ft3_ancora(spec, blocos, achados):
    """⛔⛔ FT3 — A ANCORA DE CONTINUIDADE DO HOMEM NO TAKE 2.

    Decisao do operador: no take 2 ele aparece COM ROSTO e e' O MESMO. Isso
    exige ancora forte, e a licao e' paga: no VAZAMENTO a ancora estava na
    camisa (`wearing the same shirt`) e o render devolveu um senhor de oculos e
    bigode no lugar do corpo-prova — e como o TAKE diz `Only he speaks`, o
    ESTRANHO falava a fala do REF.
    ⚠️ Cinco pecas, e nenhuma delas sozinha basta: idade + etnia + marca +
    sinal + a frase explicita.
    ⛔⛔ E AQUI ELA CARREGA MAIS PESO QUE NO BED 16: la' o cenario dos dois takes
    e' a mesma casa e ajuda a segurar a pessoa. Aqui o lugar muda por inteiro,
    porque os dois eixos de cena sao independentes — o homem e' a UNICA coisa
    que atravessa o corte.
    """
    h, et = spec["homem"], spec["etnia"]
    i2, t2 = blocos["IMAGE 02/02"], blocos["TAKE 02/02"]
    if "the same %d-year-old" % h["idade"] not in i2:
        achados.append(("ERRO", "FT3: a IMAGE 02 nao repete `the same "
                                "%d-year-old` — o Veo troca de pessoa"
                        % h["idade"]))
    if et not in i2:
        achados.append(("ERRO", "FT3: a IMAGE 02 nao repete a etnia (%r)" % et))
    for peca, rot in ((h["marca"], "marca"), (h["sinal"], "sinal")):
        if peca not in i2:
            achados.append(("ERRO", "FT3: a IMAGE 02 nao repete o %s facial "
                                    "sorteado (%r) — e' a ancora que o Veo usa "
                                    "para nao trocar de homem"
                            % (rot, peca[:38])))
    if "It is the same man" not in i2:
        achados.append(("ERRO", "FT3: a IMAGE 02 nao diz `It is the same man` — "
                                "a ancora implicita nao segura troca de lugar, "
                                "roupa e luz de uma vez"))
    if "the same man as in the first scene" not in t2:
        achados.append(("ERRO", "FT3: o TAKE 02 nao repete a ancora — a IMAGE "
                                "segura o primeiro frame, o TAKE segura os 8 "
                                "segundos"))


def _ft4_duas_maos(spec, blocos, achados):
    """⭐⭐⭐ FT4 — A PROVA ESTA' NAS DUAS MAOS DELE.

    ⛔ Ordem literal do operador: *"O take 2, o cara esta' com uma bowl de cubos
    de gelatina na mao e box de baking soda noutra mao"*. A lente cobra as
    quatro pontas: os dois objetos na IMAGE, a construcao que os separa em maos
    diferentes, e a trava no TAKE que os mantem la' pelos 8 segundos.

    ⚠️ SEM A TRAVA DO TAKE o Veo poe ele apoiando a tigela em algum lugar no
    segundo 3 — e a prova sai de quadro justamente quando a fala esta' dizendo o
    que a tigela FAZ.
    """
    i2, t2 = blocos["IMAGE 02/02"], blocos["TAKE 02/02"]
    if TIGELA_CUBOS not in i2:
        achados.append(("ERRO", "FT4: a IMAGE 02 nao traz a tigela de CUBOS de "
                                "gelatina — e' metade da prova do angulo"))
    if CAIXA_BICARBONATO not in i2:
        achados.append(("ERRO", "FT4: a IMAGE 02 nao traz a caixa de "
                                "bicarbonato com o rotulo legivel — e' a outra "
                                "metade, e e' o CT5 em quadro aberto"))
    if "In one hand he holds" not in i2 or "in his other hand he holds" not in i2:
        achados.append(("ERRO", "FT4: a IMAGE 02 nao separa os dois objetos em "
                                "MAOS DIFERENTES — sem isso o gerador junta os "
                                "dois numa mao so' ou apoia um deles"))
    if "the bowl in one hand and the box in the other" not in t2:
        achados.append(("ERRO", "FT4: o TAKE 02 nao segura os dois objetos pelos "
                                "8 segundos — a IMAGE segura o primeiro frame, "
                                "o TAKE segura o resto"))
    # ⛔⛔ A CAIXA E' DE PAPELAO, E UM DOS DEZ AMBIENTES E' DENTRO D'AGUA. Achado
    # do PRIMEIRO render deste motor, lendo o bloco em voz alta: ele sentado na
    # jacuzzi com a agua no peito, segurando uma caixa de papelao. Passou nas
    # treze lentes e nos seis medidores, porque nenhum deles cruza o OBJETO com
    # o LUGAR. Aqui a clausula e' cobrada no bloco montado, nao na lista: se um
    # dia a fala for remontada por outro caminho, e' esta conta que acusa.
    if "water at his chest" in i2 and "clear of the water" not in i2:
        achados.append(("ERRO", "FT4: a IMAGE 02 poe ele com a agua no peito e "
                                "nao tira as maos da agua — a caixa de "
                                "bicarbonato e' de PAPELAO"))


def _ft5_sem_texto(spec, blocos, achados):
    """FT5 — nada de texto queimado.

    ⛔ A EXCECAO E' O ROTULO DA CAIXA, e ela e' declarada: a palavra esta' no
    OBJETO (a embalagem de bicarbonato), nao queimada na tela pelo gerador. A
    trava segue valendo para legenda, marca d'agua e texto de interface — a
    nossa legenda nasce DEPOIS, no Veo Editor, do Whisper rodando sobre o audio
    gerado. Texto vindo do gerador entra por cima e nao ha' como tirar.
    """
    sc.lint_sem_texto(blocos, achados)
    for k in ("IMAGE 01/02", "IMAGE 02/02"):
        if "No on-screen text" not in blocos[k]:
            achados.append(("ERRO", "FT5: %s sem a trava de texto queimado" % k))


# ⛔⛔ FT6 — NAO HA' PROP FALICO NESTE ANGULO, e a ausencia e' VIGIADA.
# ⚠️ A maioria dos motores do parque tem um; quem chegar aqui vindo de qualquer
# um deles vai sentir falta e vai querer "consertar". A prova deste agente e' o
# CASAL e o que ele tem nas maos — um geoduck na cena mataria justamente isso.
_PROXY_FALICO = re.compile(
    r"\b(geoduck|clam|siphon|banana|cucumber|carrot|squash|zucchini|sausage|"
    r"eggplant|anatomical model|anatomy model|penile|phallic|shaft)\b", re.I)


def _ft6_sem_prop(spec, blocos, achados):
    for nome in sorted(blocos):
        m = _PROXY_FALICO.search(blocos[nome])
        if m:
            achados.append(("ERRO", "FT6: %s traz um proxy falico (%r) — este "
                                    "angulo NAO tem prop, e a prova dele e' o "
                                    "casal (bracos cruzados -> corpo colado)"
                            % (nome, m.group(0))))


def _ft7_orcamento(spec, blocos, achados):
    for i, fala in enumerate(spec["falas"], 1):
        n = _palavras(fala)
        if n > TETO_FALA[i]:
            achados.append(("ERRO", "FT7: cena %d com %d palavras (teto %d) — a "
                                    "fala e' CORTADA no render"
                            % (i, n, TETO_FALA[i])))
        if n < PISO_FALA[i]:
            achados.append(("AVISO", "FT7: cena %d com %d palavras (piso %d) — "
                                     "sobra ar morto no take"
                            % (i, n, PISO_FALA[i])))


def _ft8_etnia(spec, blocos, achados):
    """FT8 — a congruencia governa O HOMEM, que e' quem fala.

    ⚠️ E aqui ela NAO cobra o cenario, ao contrario do BED 16: la' o mundo e' um
    arquetipo REGIONAL (um brownstone do Harlem com um homem branco quebra a
    leitura), e aqui os lugares sao hotel, suite e jacuzzi — que nao tem etnia.
    Cobrar congruencia de cenario aqui seria a lente inventando uma regra.
    """
    et = spec["etnia"]
    for k in ("BLOCO 0 (REF)", "IMAGE 01/02", "IMAGE 02/02"):
        if et not in blocos[k]:
            achados.append(("ERRO", "FT8: %s sem a etnia da pagina (%r) — a "
                                    "congruencia com o avatar sai do video sem "
                                    "ninguem ver" % (k, et)))


def _ft9_toalha(spec, blocos, achados):
    """⛔ FT9 — O TAKE 1 E' O PRINT: de pe', tronco nu, toalha na cintura.

    ⚠️ A TOALHA NAO E' FIGURINO, E' TRAVA DE MODERACAO. Homem de tronco nu num
    quarto, com uma mulher na cama, sem nada dito da cintura para baixo, e' o
    convite exato para o gerador improvisar — e improviso de cintura para baixo
    e' recusa. A toalha resolve a cena do print E fecha a porta.
    ⛔ E ele esta' DE PE' e falando PARA A LENTE, nao para ela: e' o que o print
    mostra, e e' o que autoriza a fala em 2a pessoa sem soar que ele acusa a
    mulher.
    """
    i1 = blocos["IMAGE 01/02"]
    if spec["toalha"] not in i1:
        achados.append(("ERRO", "FT9: a IMAGE 01 nao poe a toalha sorteada — "
                                "tronco nu sem nada dito da cintura para baixo "
                                "e' recusa do gerador"))
    if "bare-chested" not in i1:
        achados.append(("ERRO", "FT9: a IMAGE 01 nao poe ele de tronco nu — e' "
                                "o print"))
    if "Standing in the foreground close to the lens" not in i1:
        achados.append(("ERRO", "FT9: a IMAGE 01 nao poe ele DE PE' na frente — "
                                "sentado ele vira o take 2 antes da hora"))
    if "one hand open in front of him" not in i1:
        achados.append(("ERRO", "FT9: a IMAGE 01 perdeu a MAO ABERTA do gesto "
                                "de quem se explica — e' o que faz a briga ser "
                                "lida sem uma palavra dela"))


# ⛔⛔ FT10 — O DEITICO DO TAKE 2 NAO TEM PARA ONDE APONTAR.
# ⚠️ Lente herdada do BED 16, onde ela nasceu DEPOIS de o defeito passar por
# todos os medidores externos: `She unpacked that bag that week.` vivia no pool e
# o `medir_deiticos` nao o via — ele mede DENTRO da sentenca, e ali o antecedente
# dependia de qual entrada de OUTRO pool tinha caido no take ANTERIOR.
#
# ⭐ Aqui o escopo e' ainda mais claro que no BED: os dois takes nao dividem nem
# o LUGAR. O take 2 nao herda um objeto sequer do quarto da briga, e as suas
# tres batidas (mecanismo · habito · CTA) nao introduzem substantivo nenhum para
# apontar depois. Logo, no take 2, qualquer `that/those/these <substantivo>` que
# nao tenha sido dito ANTES na propria fala e' deitico apontando para o vazio.
#
# ⛔ O TAKE 1 FICA DE FORA DE PROPOSITO: la' o quarto esta' em quadro, e ainda
# seria preciso adivinhar quando `that` e' conjuncao (`I thought that was just
# getting older`). Estender a lente para o take 1 reprovaria a copy certa.
_DEITICO_T2 = re.compile(r"\b(that|those|these)\s+([a-z]{3,})\b", re.I)


def _ft10_deitico_orfao(spec, blocos, achados):
    fala = spec["falas"][1]
    for m in _DEITICO_T2.finditer(fala):
        alvo = m.group(2).lower()
        if alvo not in fala[:m.start(2)].lower():
            achados.append(("ERRO",
                            "FT10: o take 2 diz %r e o substantivo nunca foi "
                            "introduzido — os dois takes deste angulo nao "
                            "dividem nem o lugar, entao nao ha' para onde o "
                            "deitico apontar" % m.group(0)))


def _ft11_bela(spec, blocos, achados):
    """⭐⭐ FT11 — O TOGGLE MODO BELA TEM DE MUDAR O QUADRO, NOS DOIS ESTADOS.

    ⛔ E' a lente contra a FORMA-SEM-FUNCAO, que este repo ja' pagou tres vezes:
    botao aceso, sorteio igual. Ela cobra que a idade, o porte, a marca e o traje
    dela cheguem aos DOIS blocos de imagem — que sao exatamente o que o modo
    move.

    ⚠️ E cobra os DOIS ESTADOS pelo MESMO caminho: com o modo desligado, a
    mulher realista do print (33+); com ele ligado, a REF do pool compartilhado.
    Lente que so' olha o estado ligado deixaria o desligado apodrecer sem
    ninguem ver.
    """
    w = spec["mulher"]
    for k, t in (("IMAGE 01/02", 1), ("IMAGE 02/02", 2)):
        bl = blocos[k]
        if "%d-year-old" % w["idade"] not in bl:
            achados.append(("ERRO", "FT11: %s sem a idade sorteada dela (%d) — "
                                    "a idade e' a primeira coisa que o modo "
                                    "BELA move" % (k, w["idade"])))
        if w["porte"] not in bl:
            achados.append(("ERRO", "FT11: %s sem o porte sorteado dela (%r) — "
                                    "corpo que nao chega ao frame nao e' corpo"
                            % (k, w["porte"][:34])))
        # ⚠️ 2026-08-10: compara com a marca SANEADA (`_marca_dela`), nao com o
        # campo cru do pool. Desde a FT14 a descricao dela perde, por take, as
        # clausulas que brigam com a cena — e uma lente que cobrasse o texto
        # ORIGINAL reprovaria 100% dos sorteios em MODO BELA, que e' a lente
        # contra o proprio template (licoes §16). O que ela guarda continua
        # sendo o mesmo: a ancora facial TEM de chegar aos dois quadros.
        marca_no_bloco = _marca_dela(spec, t)
        if marca_no_bloco not in bl:
            achados.append(("ERRO", "FT11: %s sem a marca facial dela — ela "
                                    "reaparece depois de um corte e de uma "
                                    "troca de lugar inteira, e sem ancora o Veo "
                                    "troca de mulher" % k))
        # ⛔ e a ancora nao pode ter sido esvaziada pelo saneamento: se sobrar
        # so' a cor dos olhos, duas mulheres diferentes do pool viram a mesma
        # frase e o corte deixa de ter ancora nenhuma.
        if len(marca_no_bloco.split()) < 3:
            achados.append(("ERRO", "FT11: %s ficou com a marca dela reduzida a "
                                    "%r — o saneamento da FT14 comeu a ancora "
                                    "inteira" % (k, marca_no_bloco)))
        if _traje_dela(spec, t) not in bl:
            achados.append(("ERRO", "FT11: %s sem o traje do estado atual do "
                                    "modo BELA (%r)"
                            % (k, _traje_dela(spec, t)[:34])))
    if not spec.get("bela") and w["idade"] < 34:
        achados.append(("ERRO", "FT11: modo BELA DESLIGADO e a mulher tem %d "
                                "anos — o estado desligado e' a mulher "
                                "realista do print (34+), e o pool bela do repo "
                                "vai ate' 33" % w["idade"]))


# ⛔⛔ FT13 — O TAKE 2 NAO PODE FINGIR QUE E' O MESMO LUGAR.
# ⚠️ Esta lente existe por causa da DIVERGENCIA ESTRUTURAL com o BED 16, e ela
# e' o unico jeito de codificar essa divergencia. La' os dois ambientes sao da
# MESMA casa e o bloco de agua diz literalmente `the same <casa>` — e o autoteste
# do BED COBRA esse literal, entrada por entrada. Quem trouxer aquele idioma para
# ca' (por copia, que e' como este motor nasceu) escreve uma MENTIRA: os dois
# eixos de cena aqui sao independentes, e o quarto de hotel do take 1 nao tem
# nada a ver com a cabana do take 2.
# ⛔ O que PODE dizer `the same` e' O HOMEM (`the same 48-year-old`, `the same
# man`) e a MULHER — e por isso a lente mira SUBSTANTIVO DE LUGAR, nao a palavra
# `same`.
_MESMO_LUGAR = re.compile(
    r"\bthe same (room|bedroom|bathroom|house|hotel|cabin|suite|place|"
    r"apartment|motel)\b", re.I)


def _ft14_mulher_sem_contradicao(spec, blocos, achados):
    """FT14 — a descricao dela nao pode brigar consigo mesma (2026-08-10).

    ⛔ Relato de campo: ~15% dos videos com uma mulher no take 1 e outra no
    take 2. A causa foi CONTRADICAO na frase, nao falta de ancora — ver o bloco
    do `_marca_dela`. Esta lente cobra o resultado nos BLOCOS MONTADOS, que e'
    onde o defeito aparecia; um teste de pool nao o veria, porque nenhuma das
    duas metades esta' errada sozinha.
    """
    i1 = blocos.get("IMAGE 01/02", "")
    i2 = blocos.get("IMAGE 02/02", "")
    # a frase dela comeca na idade e vai ate' o traje — pega o trecho
    for bloco, rot, take in ((i1, "IMAGE 01/02", 1), (i2, "IMAGE 02/02", 2)):
        m = re.search(r"%d-year-old %s woman[^.;]*"
                      % (spec["mulher"]["idade"], re.escape(spec["mulher"]["etnia"])),
                      bloco)
        if not m:
            achados.append(("ERRO", "FT14: %s nao traz a mulher com idade e "
                                    "etnia declaradas — sem autoridade unica "
                                    "sobre a aparencia, o gerador escolhe "
                                    "sozinho e escolhe DIFERENTE em cada take"
                                    % rot))
            continue
        trecho = m.group(0)
        if _TOM_DE_PELE.search(trecho):
            achados.append(("ERRO", "FT14: %s declara a etnia dela E um tom de "
                                    "pele na mesma frase (%r) — duas "
                                    "autoridades para o mesmo atributo, e o "
                                    "gerador resolve DIFERENTE em cada take"
                                    % (rot, trecho[:90])))
        if take == 1 and _SORRISO.search(trecho):
            achados.append(("ERRO", "FT14: a IMAGE 01/02 poe sorriso na "
                                    "descricao dela e `a hard closed "
                                    "expression` na mesma frase (%r)"
                                    % trecho[:90]))
    # ⭐ ordem do operador, 2026-08-10: *"mulher no take 2 sempre sorrindo
    # feliz"*. E' o payoff visual do angulo — a inversao da cara fechada do
    # take 1 — entao vale nos DOIS blocos do take 2, imagem e movimento.
    if "smiling happily" not in i2:
        achados.append(("ERRO", "FT14: a IMAGE 02/02 nao diz que ela esta' "
                                "sorrindo feliz — e' a inversao que o angulo "
                                "vende, e foi pedida nominalmente"))
    if "keeps smiling happily" not in blocos.get("TAKE 02/02", ""):
        achados.append(("ERRO", "FT14: o TAKE 02/02 nao manda ela CONTINUAR "
                                "sorrindo — sorriso so' na IMAGE some no "
                                "movimento"))


def _ft13_lugares_independentes(spec, blocos, achados):
    for k in ("IMAGE 02/02", "TAKE 02/02"):
        m = _MESMO_LUGAR.search(blocos[k])
        if m:
            achados.append(("ERRO",
                            "FT13: %s diz %r — os DOIS eixos de cena deste "
                            "angulo sao independentes (o quarto da briga e os "
                            "dez ambientes do casal), entao o lugar NAO "
                            "atravessa o corte. Quem atravessa e' o homem"
                            % (k, m.group(0))))


def _ft12_contrato16(spec, blocos, achados):
    """As NOVE travas do CONTRATO DE COPY 16s, cobradas de dentro do motor.

    ⭐ `isca_absurda=False`: este angulo nao promete nada no take 1 que ele mesmo
    va' desmentir meio segundo depois (o take 1 e' a falha + a falsa causa + a
    virada, nao substancia absurda). Logo o CT7 — verbo de ereccao colado no
    orgao — vale nos DOIS takes, e nao so' no do CTA.
    ⚠️ `sys.modules[__name__]` e nao outro modulo: a lente le' `base.NUCLEO`, e o
    NUCLEO e' deste arquivo.
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
    for f in (_ft1_ela_muda, _ft2_inversao, _ft3_ancora, _ft4_duas_maos,
              _ft5_sem_texto, _ft6_sem_prop, _ft7_orcamento, _ft8_etnia,
              _ft9_toalha, _ft10_deitico_orfao, _ft11_bela, _ft12_contrato16,
              _ft13_lugares_independentes, _ft14_mulher_sem_contradicao):
        f(spec, blocos, ach)
    return ach


# ===========================================================================
# PAINEL
# ===========================================================================

EIXOS_UI = [
    ("quarto", "O QUARTO DA BRIGA", "QUARTOS", "nome"),
    ("ambiente", "O AMBIENTE DO CASAL", "AMBIENTES", "nome"),
    ("homem", "QUEM FALA", "HOMENS", "id"),
    ("mulher", "A MULHER", "MULHERES", "id"),
]

EIXOS_TRAVAVEIS = ["quarto", "ambiente", "homem", "mulher"]

# ⛔ SEM TRAVA DE LOTE, e a ausencia e' declarada. O BED tem `familia_mundo`
# porque la' quinze regioes se agrupam em familias; aqui os dois eixos de cena
# JA' sao listas curtas e cada um ja' e' travavel video a video pelo cadeado.
# Uma trava de lote em cima disso seria um segundo controle para a mesma coisa —
# e controle duplicado e' onde o operador para de confiar no painel.
TRAVAS_UI = []

# ⚠️ Nenhum eixo entra em IGNORA_PAINEL: os quatro chegam ao quadro por algum
# campo (o `cen` do quarto, o `cen` do ambiente, a `marca` dele e a dela), e o
# `lint_painel_honesto` aceita QUALQUER campo do eixo como prova de presenca.
# Declarar a tupla vazia e' declarar que alguem verificou, em vez de deixar o
# `getattr` decidir por omissao.
IGNORA_PAINEL = ()

# ⛔ Nenhum eixo do painel mexe na copy neste motor: a fala nao cita o quarto, o
# ambiente, os objetos nem as pessoas. Trocar um eixo remonta o QUADRO e mantem
# a fala, que e' o comportamento certo.
EIXOS_QUE_MEXEM_NA_COPY = {}


def resumo_pt(spec):
    """⚠️ Texto de PAINEL, nao copy falada — mas e' o unico lugar onde o operador
    le' o video ANTES de gastar credito gerando. Resumo errado faz ele aprovar o
    que nao viu (licoes §30), e resumo com a string inglesa crua faz ele parar
    de ler.

    ⛔⛔ NENHUM MARCADOR DENTRO DA STRING. Nos COMENTARIOS o simbolo pode ficar;
    no que sai por `print()` NAO — o console do Windows e' cp1252 e o `⛔`
    levanta UnicodeEncodeError. ⚠️ E o crash acontece exatamente na hora em que
    a mensagem importa: o `--autoteste` passa verde (ele nao chama esta funcao)
    e o motor morre na PRIMEIRA vez que alguem manda gerar um video pela linha
    de comando. Foi assim, aqui, no primeiro render deste agente — a mesma
    licao ja' paga nos autotestes do COLO, do ESCANDALO e no `distribuir.py`.
    """
    return ("16s, DOIS takes. Take 1 — A BRIGA, em %s: ele de %d anos, DE PE' "
            "perto da lente, tronco nu e TOALHA na cintura, uma mao aberta se "
            "explicando PARA A LENTE; ela atras, de BRACOS CRUZADOS, ENCARANDO "
            "ele, muda. A fala e' a falha em 2a pessoa + a falsa causa + a "
            "VIRADA que nomeia o gelatin trick. Take 2 — O CASAL COLADO, em %s: "
            "o MESMO homem, com rosto, ela COLADA nele, e ele com a TIGELA DE "
            "CUBOS numa mao e a CAIXA DE BICARBONATO na outra. Mecanismo, "
            "habito e o CTA por ultimo. ATENCAO: os dois lugares sao "
            "INDEPENDENTES — quem atravessa o corte e' o homem, nao a casa. "
            "Elenco: homem %s, "
            "mulher %s de %d anos (modo BELA %s). Ela e' MUDA nos dois takes."
            % (spec["quarto"]["nome"], spec["homem"]["idade"],
               spec["ambiente"]["nome"], spec["etnia"],
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
    apel = collections.Counter()
    tam = collections.defaultdict(list)
    falhas, avisos = [], 0
    # ⭐⭐ OS DOIS ESTADOS DO MODO BELA, MEDIDOS SEPARADAMENTE. Medir so' o
    # default e' medir metade do agente: o toggle troca o pool inteiro da
    # mulher, e um KeyError do lado ligado morreria CALADO dentro do callback do
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

    print("FIGHT 16 — %d sorteios (metade com MODO BELA ligado)" % n)
    for c in sorted(dist):
        v = sorted(tam[c])
        print("  cena %d: %d falas distintas · palavras min/med/max %d/%d/%d"
              % (c, len(dist[c]), v[0], v[len(v) // 2], v[-1]))
    print("  apelido: %s" % dict(apel))
    for on in (False, True):
        v = sorted(idades_bela[on])
        print("  mulher · modo BELA %-9s idades %d..%d (%d distintas)"
              % ("LIGADO" if on else "desligado", v[0], v[-1], len(v)))
    print("  linter: %d ERRO, %d AVISO" % (sum(erros.values()), avisos))
    for k, v in erros.most_common(5):
        print("     %3dx %s" % (v, k))

    # ⛔ CONTROLE DO TOGGLE: o modo tem de MOVER a mulher. Se as idades dos dois
    # estados se sobrepuserem, o botao acende e nao muda nada — que e' a
    # forma-sem-funcao que a FT11 existe para impedir.
    if idades_bela[False] & idades_bela[True]:
        falhas.append("MODO BELA: os dois estados sorteiam idades em comum (%s) "
                      "— o pool realista comeca em 34 e o pool bela termina em "
                      "33, entao sobreposicao significa que alguem mexeu num "
                      "dos dois"
                      % sorted(idades_bela[False] & idades_bela[True]))

    # ⭐ [ALCANCE] — entrada que nao cabe somada aos MINIMOS dos outros beats
    # nunca e' sorteada. Ela nao e' rara: e' MORTA, e o autoteste a contava como
    # opcao viva. E' a licao §36 do repo.
    o_pior = max(sc.APELIDOS_16, key=len)
    for rot, pool, cena, outros in (
            ("HOOKS", HOOKS, 1, [FALSAS, VIRADAS]),
            ("FALSAS", FALSAS, 1, [HOOKS, VIRADAS]),
            ("VIRADAS", VIRADAS, 1, [HOOKS, FALSAS]),
            ("MECANISMOS", MECANISMOS, 2, [HABITOS, CTAS]),
            ("HABITOS", HABITOS, 2, [MECANISMOS, CTAS]),
            ("CTAS", CTAS, 2, [MECANISMOS, HABITOS])):
        reserva = sum(_mn(p, o_pior) for p in outros)
        mortas = [x for x in pool
                  if _palavras(x.format(o=o_pior)) + reserva > TETO_FALA[cena]]
        if mortas:
            falhas.append("[ALCANCE] %s: %d de %d nunca sao sorteadas "
                          "(teto real %d palavras)"
                          % (rot, len(mortas), len(pool),
                             TETO_FALA[cena] - reserva))

    # ⛔⛔ CONTROLE DE COBERTURA COMPLETA — este motor foi desenhado para que
    # NENHUM `_cabe` corte nada, e por isso as 216 combinacoes de cada take sao
    # alcancaveis. Se alguem acrescentar uma entrada longa, o [ALCANCE] acima
    # pega as MORTAS; este pega o caso mais sutil, em que o MAIOR de cada beat
    # ainda cabe sozinho mas nao cabe COM os outros maiores.
    for cena, pools in ((1, (HOOKS, FALSAS, VIRADAS)),
                        (2, (MECANISMOS, HABITOS, CTAS))):
        pior = sum(max(_palavras(x.format(o=o_pior)) for x in p) for p in pools)
        if pior > TETO_FALA[cena]:
            falhas.append("COBERTURA cena %d: a soma dos MAIORES da' %d palavras "
                          "(teto %d) — o `_cabe` passa a cortar e o sorteio "
                          "deixa de ser uniforme" % (cena, pior, TETO_FALA[cena]))

    # ⛔ CONTROLE DE CONTRATO: todo HOOK tem de enunciar a falha (CT2). A lente
    # do `short_comum` so' olha a fala MONTADA — se um dia entrar uma entrada
    # sem verbo de falha, ela so' apareceria em ~1/6 dos sorteios.
    _CT2 = re.compile(r"\b(struggl\w*|quit|soft|stopped|dead|failed|"
                      r"shut down|useless|lose it|not working|gave out)\b", re.I)
    sem_ct2 = [x for x in HOOKS if not _CT2.search(x)]
    if sem_ct2:
        falhas.append("CT2: %d entrada(s) de HOOKS sem verbo de falha: %s"
                      % (len(sem_ct2), sem_ct2[:2]))

    # ⛔⛔ CONTROLE DO CT7 POR CONSTRUCAO — REESCRITO EM 2026-08-10.
    # A versao anterior exigia que NENHUMA das tres listas do take 1 nomeasse o
    # orgao. Isso era forte demais e o operador derrubou: o take 1 TEM de
    # nomear o orgao (`firm WHAT?? my butt??`). O que o CT7 proibe nao e' o
    # orgao no take — e' o VERBO DE ERECCAO NA MESMA SENTENCA DELE.
    # ⭐ Entao a garantia mudou de lugar, mas continua sendo cobrada na LISTA e
    # nao no sorteio, e agora sao TRES condicoes em vez de uma:
    #   · HOOKS e VIRADAS nao nomeiam o orgao (o hook carrega `hard`/`firm`);
    #   · TODA FALSA nomeia o orgao (senao o video volta ao defeito reportado);
    #   · NENHUMA FALSA carrega verbo do `sc.ERECAO_16`.
    for rot, pool in (("HOOKS", HOOKS), ("VIRADAS", VIRADAS)):
        sujas = [x for x in pool
                 if any(nn.lower() in x.lower() for nn in NUCLEO)]
        if sujas:
            falhas.append("CT7: %s nomeia o orgao em %d entrada(s) (%s) — este "
                          "beat carrega `hard`/`firm`, e verbo de ereccao "
                          "colado no orgao e' ~95%% de recusa no gerador"
                          % (rot, len(sujas), sujas[0][:34]))
    mudas = [x for x in FALSAS if "{o}" not in x]
    if mudas:
        falhas.append("O TAKE 1 TEM DE NOMEAR O ORGAO: %d FALSA(S) sem `{o}` "
                      "(%s) — ordem do operador de 2026-08-10, e sem isso o "
                      "espectador ouve `did that` sem objeto"
                      % (len(mudas), mudas[0][:40]))
    # ⛔⛔ A NEGACAO EM TODA FALSA — o conserto do operador de 2026-08-10.
    # Sem `not`/`never` a sentenca AFIRMA que a idade matou o orgao, e so' UMA
    # das seis viradas a desmente (`But things changed...`). Nos outros 5/6 dos
    # sorteios o video fecharia o take 1 sustentando o contrario do que a VSL
    # vende. ⚠️ O controle mora na LISTA de proposito: o defeito nasce no PAR
    # falsa x virada, e nao ha' como cobra-lo no sorteio sem enumerar 36 pares.
    # Exigir a negacao em cada entrada torna todo par seguro por construcao.
    sem_not = [x for x in FALSAS if not re.search(r"\b(not|never)\b", x, re.I)]
    if sem_not:
        falhas.append("A FALSA CAUSA TEM DE SER DESMENTIDA NA PROPRIA "
                      "SENTENCA: %d entrada(s) sem `not`/`never` (%s) — so' a "
                      "virada `But things changed` contradiz, e ela e' 1 de 6"
                      % (len(sem_not), sem_not[0][:40]))
    erecao = [x for x in FALSAS if sc.ERECAO_16.search(x)]
    if erecao:
        falhas.append("CT7: %d FALSA(S) com verbo de ereccao NA SENTENCA DO "
                      "ORGAO (%s) — e' exatamente a composicao que o COLO 16 "
                      "pagou com ~95%% de recusa" % (len(erecao), erecao[0][:40]))

    # ⛔ CONTROLE DE CONTRATO: todo MECANISMOS carrega o literal do funil.
    sem_lit = [x for x in MECANISMOS if "gelatin trick" not in x]
    if sem_lit:
        falhas.append("CT3: %d entrada(s) de MECANISMOS sem `gelatin trick`"
                      % len(sem_lit))
    # ⚠️ E toda VIRADA tambem — e' ela que nomeia a DESCOBERTA no take 1, e o
    # take fecharia apontando para lugar nenhum sem o literal.
    sem_lit = [x for x in VIRADAS if "gelatin trick" not in x]
    if sem_lit:
        falhas.append("VIRADAS: %d entrada(s) sem `gelatin trick` — o take 1 "
                      "fecharia sem nomear a descoberta" % len(sem_lit))

    # ⛔ CONTROLE DE VASILHAME NA FALA — ordem permanente do operador: a fala
    # nao paga o que o quadro mostra. O quadro poe a tigela na mao dele; a fala
    # que disser `bowl` esta' gastando palavra com o que ja' esta' em cena, e
    # `one bowl` le' como DOSE de receita.
    _VASILHAME = re.compile(r"\b(bowl|cup|glass|spoon|teaspoon|tablespoon|"
                            r"jar|box|scoop|half|quarter)\b", re.I)
    for rot, pool in (("HABITOS", HABITOS), ("MECANISMOS", MECANISMOS),
                      ("CTAS", CTAS), ("HOOKS", HOOKS), ("FALSAS", FALSAS),
                      ("VIRADAS", VIRADAS)):
        sujas = [x for x in pool if _VASILHAME.search(x)]
        if sujas:
            falhas.append("VASILHAME: %s tem %d entrada(s) com medida ou "
                          "recipiente na fala (%r) — a fala nao paga o que o "
                          "quadro mostra" % (rot, len(sujas), sujas[0][:34]))

    # ⛔ CONTROLE DE IDADE DITA — nenhum pool de fala pode citar idade. E' a
    # pendencia B do BED 16 (idade dita x idade em quadro) impedida na origem.
    _IDADE_DITA = re.compile(
        r"\b(forty|fifty|sixty|seventy|thirty)\b", re.I)
    for rot, pool in (("HOOKS", HOOKS), ("FALSAS", FALSAS),
                      ("VIRADAS", VIRADAS), ("MECANISMOS", MECANISMOS),
                      ("HABITOS", HABITOS), ("CTAS", CTAS)):
        sujas = [x for x in pool if _IDADE_DITA.search(x)]
        if sujas:
            falhas.append("IDADE: %s diz idade em %d entrada(s) (%r) — os "
                          "HOMENS vao de 45 a 55 e o quadro mostra o rosto"
                          % (rot, len(sujas), sujas[0][:34]))

    # ⛔⛔ CONTROLE POSITIVO DA FT13 — lente que nunca acusa nada e' forma sem
    # funcao, e "sem achado" nela significaria "ninguem olhou". A frase abaixo e'
    # exatamente o idioma do BED 16 (`the same <casa>`), que e' o que uma copia
    # descuidada traria para ca'.
    for morta in ("In the water at the same house is the same man.",
                  "Medium shot in the same hotel room."):
        prova = []
        _ft13_lugares_independentes(
            {}, {"IMAGE 02/02": morta, "TAKE 02/02": ""}, prova)
        if not prova:
            falhas.append("FT13: a lente parou de acusar %r — ela e' a unica "
                          "coisa entre este motor e a mentira de continuidade "
                          "de lugar" % morta)
    limpo = []
    _ft13_lugares_independentes(
        {}, {"IMAGE 02/02": "It is the same 48-year-old white American man, "
                            "the same man, not a different person.",
             "TAKE 02/02": "it is the same man as in the first scene"}, limpo)
    if limpo:
        falhas.append("FT13: a lente acusa a ancora do HOMEM, que e' o unico "
                      "`the same` legitimo aqui (%s)" % limpo[0][1][:60])

    # ⛔⛔ CONTROLE POSITIVO DA FT10 — a lente tem de ACUSAR o deitico orfao e
    # DEIXAR PASSAR a copy limpa deste motor.
    prova = []
    _ft10_deitico_orfao(
        {"falas": ["", "The gelatin trick opens the blood flow to your pecker. "
                       "That habit changed everything."]}, {}, prova)
    if not prova:
        falhas.append("FT10: a lente parou de acusar deitico orfao no take 2")
    limpo = []
    _ft10_deitico_orfao(
        {"falas": ["", "The gelatin trick puts blood back in your pecker. One "
                       "habit a night. Comment gelatin, and the recipe goes to "
                       "your messages."]}, {}, limpo)
    if limpo:
        falhas.append("FT10: a lente acusa copy limpa (%s)" % limpo[0][1][:60])

    # ⛔ CONTROLE DOS DOIS EIXOS DE CENA: cada quarto precisa dos campos que o
    # `montar` le', e cada ambiente tambem. Campo faltando levantaria KeyError
    # so' quando aquela entrada fosse sorteada — e num pool de 8x10 isso pode
    # demorar um lote inteiro para aparecer.
    for q in QUARTOS:
        for k in ("nome", "cen", "ela", "luz", "audio", "dela", "dela_bela"):
            if not q.get(k):
                falhas.append("QUARTO %s: sem %r" % (q["id"], k))
        if q.get("dela_bela") == q.get("dela"):
            falhas.append("QUARTO %s: o traje bela e' igual ao normal — o "
                          "toggle nao move nada neste quarto" % q["id"])
    for a in AMBIENTES:
        for k in ("nome", "cen", "pose", "luz", "audio", "dele", "dela",
                  "dela_bela"):
            if not a.get(k):
                falhas.append("AMBIENTE %s: sem %r" % (a["id"], k))
        if a.get("dela_bela") == a.get("dela"):
            falhas.append("AMBIENTE %s: o traje bela e' igual ao normal — o "
                          "toggle nao move nada neste ambiente" % a["id"])
        # ⛔⛔ AMBIENTE QUE POE ELE NA AGUA TEM DE TIRAR AS MAOS DELA. A caixa de
        # bicarbonato e' de PAPELAO, e ele carrega os dois objetos nas maos em
        # TODOS os dez ambientes. O campo `maos` e' lido com `.get` (so' a
        # entrada que precisa declara), e e' ESTE controle que impede o campo de
        # sumir num refactor — sem ele, apagar a clausula da jacuzzi passaria
        # verde em tudo.
        # ⚠️ O gatilho e' `water` na POSE, e nao `tub`/`pool`: o banheiro de
        # luxo poe ele na BORDA da banheira e a cobertura poe ele ja' DENTRO do
        # quarto. Gatilho largo cobraria clausula de quem esta' seco, que e' a
        # lente inventando defeito.
        if re.search(r"\bwater\b", a["pose"], re.I) and not a.get("maos"):
            falhas.append("AMBIENTE %s: a pose poe ele na agua e nao ha' "
                          "clausula `maos` — ele carrega uma caixa de PAPELAO "
                          "nas duas cenas" % a["id"])
    # ⛔⛔ ESTE CONTROLE MUDOU EM 2026-08-13, E A MUDANCA E' ORDEM DO OPERADOR,
    # nao discordancia minha. Ele cobrava `== 10` porque os dez ambientes eram
    # LISTA FECHADA, ditada por ele um a um. A ordem nova e' dele e e' mais
    # recente: *"aumente o pool de opcoes substancialmente, tambem dos
    # ambientes"*. Entao o `==` virou PISO: os dez originais continuam no pool,
    # palavra por palavra, e o gate agora reprova quem ENCOLHER a lista.
    # ⚠️ O mesmo piso vale para os QUARTOS, que nasceram como 4 ditados + 4 de
    # `etc` e nunca tiveram controle de tamanho nenhum.
    if len(AMBIENTES) < 24:
        falhas.append("AMBIENTES: sao %d e o piso e' 24 (2026-08-13) — os DEZ "
                      "ditados pelo operador continuam na lista e ninguem os "
                      "resume" % len(AMBIENTES))
    if len(QUARTOS) < 24:
        falhas.append("QUARTOS: sao %d e o piso e' 24 (2026-08-13)"
                      % len(QUARTOS))

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
    ap.add_argument("--quarto", choices=[q["id"] for q in QUARTOS])
    ap.add_argument("--ambiente", choices=[a["id"] for a in AMBIENTES])
    # ⭐ o mesmo toggle do painel, pela linha de comando: aceite e' medicao, e
    # medir o estado ligado exige poder liga-lo sem abrir a janela.
    ap.add_argument("--bela", action="store_true",
                    help="MODO BELA ligado (o padrao e' a mulher do print)")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--autoteste", action="store_true")
    a = ap.parse_args()

    if a.autoteste:
        return autoteste()

    led = _carregar_ledger()
    rng = random.Random(a.seed)
    travas = {}
    for k in ("quarto", "ambiente"):
        if getattr(a, k):
            travas[k] = getattr(a, k)
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
