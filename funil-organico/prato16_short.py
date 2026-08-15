#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE PRATO 16 — o prato erguido e o copo estendido · 2 takes de 8s = 16s.

⭐⭐ O QUINTO MOTOR DO PARQUE COM NARRADOR HOMEM (os outros: GOOD 16, BED 16,
FIGHT 16, ALFA 16) e o PRIMEIRO em que a prova nao e' um corpo, um prop falico
nem uma esposa: e' A RECEITA ACONTECENDO. O prato de cubos, a bancada com as
caixas, a jarra, o copo. O espectador nao ve' um resultado — ve' o PREPARO, e o
resultado ele ouve.

Destilado da LEITURA OTICA A 1 FPS do reel 1709350110183701 (Charles Monroe,
2026-08-12): 24,17 segundos, take unico, camera fixa, sem corte.
KPI da fonte: 868 reacoes · 1.6K COMENTARIOS · 35 shares — mais comentario que
reacao, o mesmo padrao do CHA, que e' o melhor CTA de comentario do repertorio.

O QUE OS 24 FRAMES MOSTRAM (e o que virou o que):

    t=00-04  ele SOZINHO, prato de cubos AZUIS na mao esquerda na altura do
             peito, colher com UM cubo erguida ao lado do rosto, boca
             escancarada e olhos arregalados. Na bancada em primeiro plano: a
             caixa de gelatina, a caixa laranja de bicarbonato e o limao.
             fala: a descoberta + o casamento + OS TRES INGREDIENTES
             --> vira o TAKE 1 inteiro
    t=05-11  o preparo: agua na jarra, o bicarbonato inclinado, o limao
             espremido com as duas maos, e o liquido servido no copo
    t=12-19  ele ergue as caixas para a lente e depois ESTENDE O COPO, braco
             esticado, copo grande em primeiro plano e ele menor atras
             fala: `I'm rock hard, just like when I was 18.` + a facilidade
             --> viram o TAKE 2, fundidos
    t=19-22  o CTA, copo no peito
    t=22-23  ele BEBE  --> ⛔ CORTADO por ordem do operador (ver decisao 6)

⛔⛔ AS SEIS DECISOES DO OPERADOR (2026-08-12), perguntadas uma a uma com a
    leitura otica na mao. Nenhuma delas e' minha:
 1. O CORTE: take 1 = o prato erguido (hook estatico) · take 2 = o PREPARO +
    CTA. E' a arquitetura do GOOD 16 (um quadro parado, um quadro preparando).
 2. ⛔⛔ O CT5 E' FURADO NESTE ANGULO, DECLARADO: a fala NOMEIA os tres
    ingredientes, como a fonte. Ver o cabecalho de `RECEITAS` para o preco.
 3. A ESPOSA ENTRA — e a fonte e' SOLO, entao ela nao tem lugar herdado.
 4. ELA SO' APARECE NO TAKE 2, colada nele. A chegada dela E' o payoff.
    ⚠️ Isto contraria a regra de continuidade que o GOOD 16 aprendeu (objeto
    que aparece so' depois do corte le' como dois videos colados) — e o
    operador decidiu assim mesmo, sabendo. O motor compensa do outro lado: a
    ancora de continuidade DELE vem em cinco pecas, e a bancada, as caixas e a
    cor sao as MESMAS nos dois quadros. Quem atravessa o corte e' o CENARIO.
 5. A COR DA GELATINA E' EIXO SORTEAVEL (a fonte e' azul).
 6. O GOLE NAO ENTRA: fecha no COPO ESTENDIDO. *"Deixa o ultimo frame na prova
    em vez de na boca dele"* — e evita a mao subindo em cima da sentenca do CTA.
 7. Os dois toggles: MODO FORTE (com `maduros=True`) e MODO BELA.

⛔ REGRAS QUE NASCEM COM O AGENTE
  · o CTA e' `gelatin`, nunca `recipe` (a fonte pede `recipe`; a automacao de DM
    casa palavra EXATA e o funil inteiro roda em gelatin)
  · ⛔⛔ PR-ORGAO — a fala NUNCA nomeia o orgao. A fonte diz `I'm rock hard` em
    PRIMEIRA PESSOA, com o sujeito sendo ELE, e essa e' a formula que passa no
    gerador: verbo de ereccao COLADO no orgao e' lido como tumescencia e reprova
    (licao paga no COLO 16, ~95% de recusa). Aqui o verbo existe e o orgao nao —
    e' o CT7 satisfeito pela construcao, nao por sorte.
  · a mulher e' MUDA, e so' existe no segundo quadro
  · o prato NUNCA volta no take 2, e o copo NUNCA aparece no take 1

⚠️ RESSALVA DE FIDELIDADE, DECLARADA: o Whisper devolveu `Horse gelatin` em
   DUAS passadas independentes do audio (a completa e uma so' do trecho
   3,0-9,5s). A caixa em quadro e' `Royal Blue Gelatin`, entao quase certamente
   e' mis-hear. NADA neste motor depende dessa palavra — os pools de `RECEITAS`
   nomeiam a gelatina sem adjetivo.

    python funil-organico/prato16_short.py --pagina joe --n 1
    python funil-organico/prato16_short.py --pagina joe --n 1 --bela
    python funil-organico/prato16_short.py --autoteste
    python funil-organico/prato16_short_app.py
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

# ⛔ Os apelidos do orgao. Este agente NAO os usa na fala (ver PR-ORGAO no
# cabecalho) — a lista existe para a lente conseguir PROIBI-LOS.
NUCLEO = ["Johnson", "pecker", "wiener", "soldier", "tool"]

LEDGER = os.path.join(AQUI, ".prato-16-ledger.json")

TITULO = "AGENTE PRATO 16"
SLUG = "prato-16"
SUBTITULO = ("2 takes de 8s = 16 segundos · a cozinha de fora · ele ergue o "
             "prato de cubos e depois estende o copo; ela e' muda")

CENAS_UI = ["1 · O PRATO", "2 · O PREPARO + CTA"]

# ⛔⛔ DUAS CENAS no teto FISICO de 25 palavras (8s a ~3,1 p/s). O teto vem de
# RENDER, nao de teoria: 32 cortou, 28 cortou, 25 nao.
TETO_FALA = {1: 25, 2: 25}
# ⛔ O piso e' ARITMETICA: a soma dos MINIMOS dos beats de cada cena.
# ⚠️ cena 1 = menor DESCOBERTA (10) + menor RECEITA (6) = 16.
# ⚠️ E o piso NAO se rebaixa para caber numa entrada curta: quando a
# ampliacao de pool de 2026-08-12 trouxe combinacoes de 14 palavras, o conserto
# foi ALONGAR as tres entradas curtas, nao baixar o piso. 14 palavras em 8
# segundos deixam ~3,5s de silencio no fim do take, e piso rebaixado para
# calar o alarme e' o alarme que ensina a ignorar o linter.
# ⚠️ cena 2 = menor PROVA (7) + menor FACILIDADE (4) + menor CTA (9) = 20.
PISO_FALA = {1: 16, 2: 20}

# ⛔ Congruencia inviolavel: a etnia do REF casa com a etnia do avatar da
# pagina. ⭐ Neste angulo o REF que fala e' o HOMEM — entao a pagina governa
# ELE, e a mulher fica solta (mesma politica do GOOD 16).
ETNIA = {
    "roy": "white American", "dean": "white American",
    "earl": "white American",
    "jason": "Black American", "philippe": "Black American",
    "joe": "white American", "ray": "white American", "matt": "white American",
    "marcus": "Black American", "chuck": "Black American",
}

# ⭐ QUEM NARRA — quinto motor do parque com narrador HOMEM.
# ⚠️ Com UM sexo so' a UI nao desenha botao nenhum, que e' o certo.
SEXOS = ("homem",)

# ⭐⭐ OS DOIS TOGGLES, pelo CONTRATO COMPARTILHADO (`sc.ref_bela` /
# `sc.ref_forte`) — nunca implementacao propria. Ordem do operador, 2026-08-12:
# *"quero toggle de modo forte e modo bela"*.
#
#   BELA  move IDADE + PORTE + TRAJE DELA. ⛔ E ela SO' EXISTE NO TAKE 2 neste
#         angulo, entao o modo move metade do video — o que e' correto e esta'
#         medido no autoteste, nao suposto.
#         ⛔ A ETNIA DELA SOBREVIVE AO MODO (licao do GOOD 16): o `ref_bela`
#         devolveria a etnia do MOLDE, e sem reimpor a sorteada o modo travaria
#         a mulher inteira em `white American` sem ninguem ver.
#   FORTE move IDADE + CABECA + MARCA + CORPO DELE, e NASCE LIGADO.
MODO_BELA = True
MODO_FORTE = True
MODOS_DEFAULT = ("forte",)

# ⛔ A etnia sai da PAGINA (nao do mundo).
PELE_TRAVAVEL = False

# ⭐⭐ A FAIXA DO MODO FORTE — E ELA E' A RAZAO PELA QUAL O `maduros` EXISTE.
# Ordem do operador de 2026-08-12: *"modo forte deve abarcar refs homens mais
# velhos tb"*. O pool compartilhado `sc.REFS_FORTES` vai de 26 a 38 anos e nao
# serve a este angulo: a fonte e' um senhor de uns 68, e o narrador do pool
# proprio vai de 58 a 70.
#
# ⛔⛔ O PISO SUBIU DE 48 PARA 61 no mesmo dia, e a ordem e' MAIS RECENTE e mais
# especifica que a primeira: *"sempre que travar a referencia de forte mantenha
# o homem acima de 60 anos no prompt"*. Ela chegou depois deste motor nascer
# (veio pelo GOOD 16, commit `7ec3f38`), e o `sempre` e' o que a torna
# aplicavel aqui — nao e' regra do GOOD, e' regra do toggle.
# ⚠️ Com 48, o botao aceso ainda entregava um homem de 48 num angulo cujo
# narrador desligado tem 58-70. O toggle prometia trocar o CORPO e continuava
# podendo rejuvenescer dez anos.
# ⚠️ E o `or _pool` do helper NAO dispara aqui: o `sc.REFS_FORTES_MADUROS` tem
# DEZ entradas de 61 a 72 (ampliado de 12 para 18 pelo outro autor no mesmo
# dia), entao a faixa casa de verdade. Pedir 61 num pool que vai ate' 38 seria
# o helper cedendo em silencio — que e' o modo de falha que a lente do
# autoteste cobre.
FORTE_IDADE_MIN = 61


# ===========================================================================
# ⭐⭐ MUNDOS — 15 COZINHAS DE FORA, UMA POR REGIAO DOS EUA
# ===========================================================================
# ⛔ A fonte e' uma COZINHA EXTERNA: pergolado de madeira, vasos de barro com
# plantas, churrasqueira de inox e bancada de granito preto. Nao e' cozinha de
# dentro, e essa e' a diferenca visual que separa este angulo do BOTICA (potes
# de ervas) e do RECEITA (bancada fechada).
# ⛔ Arquetipos POR REGIAO com `etnias`, como no FALTA 16 / BED 16 / GOOD 16: a
# etnia da pagina FILTRA os mundos. Um homem branco num quintal de brownstone do
# Harlem quebra a leitura tanto quanto trocar o rosto.
#
# ⭐ Cada entrada arrasta CENARIO + BANCADA + LUZ + AUDIO + TRAJE DELA — nunca
# so' o fundo. E' `variar etnia = arrastar o mundo inteiro`.
# ⭐⭐ A `bancada` E' EIXO DE CENA, NAO ENFEITE: e' a superficie onde as caixas
# e o limao ficam nos DOIS quadros, e e' ela que faz o cenario atravessar o
# corte. Como a esposa SO' aparece no take 2 (decisao 4 do operador), a
# continuidade deste angulo se apoia no cenario e nele — nao no elenco.
# ⚠️ E ela e' SLOT, nunca a palavra `counter`: ha' mundo com ilha de tijolo, com
# tabua de madeira e com granito. Cravar o literal e' o erro que o autoteste do
# PLACA 16 pegou em 43 de 600 seeds.
#
# ⭐⭐ E cada entrada carrega o TRAJE DELA EM DOIS REGISTROS — `dela` (modo BELA
# desligado) e `dela_bela` (ligado), da MESMA regiao. Nunca roupa generica de
# outro mundo, que e' o modo de falha "REF de biquini de trico amish".
MUNDOS = [
    {"id": "apalache", "familia": "apalache", "regiao": "Apalaches",
     "cen": "an outdoor kitchen on a cedar deck behind an Appalachian "
            "farmhouse, tall pines crowding the yard behind it",
     "bancada": "the dark stone counter top",
     "luz": "late afternoon sun coming in low and warm through the pines",
     "audio": "cicadas, wind in the pines, a screen door somewhere",
     "dela": "a plain denim shirt with the sleeves rolled",
     "dela_bela": "a fitted white sleeveless blouse",
     "etnias": ["white American"]},

    {"id": "sulista", "familia": "sulista", "regiao": "Sul profundo",
     "cen": "a covered outdoor kitchen off the back of a Southern house, a "
            "plank fence and a magnolia over the far corner",
     "bancada": "the polished granite counter top",
     "luz": "warm late afternoon light coming flat across the yard",
     "audio": "cicadas, a screen door, a lawn mower two yards over",
     "dela": "a loose coral blouse",
     "dela_bela": "a fitted coral wrap top",
     "etnias": ["Black American"]},

    {"id": "texas", "familia": "texas", "regiao": "Texas",
     "cen": "an outdoor kitchen under a timber pergola behind a Texas ranch "
            "house, a plank fence and dry St. Augustine grass beyond it",
     "bancada": "the wide stone counter slab",
     "luz": "hard late sun with short shadows across the yard",
     "audio": "a window unit humming, far traffic, wind in dry grass",
     "dela": "a chambray shirt buttoned to the collar",
     "dela_bela": "a fitted white halter top",
     "etnias": ["white American"]},

    {"id": "meio_oeste", "familia": "meio_oeste", "regiao": "Meio-Oeste",
     "cen": "an outdoor kitchen built into the back deck of a Midwestern "
            "split-level, a chain-link fence and a maple behind it",
     "bancada": "the grey composite counter top",
     "luz": "cool overcast evening light, soft and even",
     "audio": "wind in the maple, a dog two yards over, a distant highway",
     "dela": "a plain navy cardigan over a tee",
     "dela_bela": "a fitted navy sleeveless top",
     "etnias": ["white American"]},

    {"id": "nova_inglaterra", "familia": "nova_inglaterra",
     "regiao": "Nova Inglaterra",
     "cen": "an outdoor kitchen on a stone patio beside a New England "
            "colonial, hydrangeas along a low stone wall",
     "bancada": "the pale soapstone counter top",
     "luz": "cool north light, soft and even",
     "audio": "gulls, wind through the hydrangeas, a distant boat horn",
     "dela": "a light grey knit sweater",
     "dela_bela": "a fitted white linen tank",
     "etnias": ["white American"]},

    {"id": "harlem", "familia": "harlem", "regiao": "Harlem",
     "cen": "an outdoor kitchen set up on the tar roof of a Harlem brownstone, "
            "water tanks and rooftops running off behind",
     "bancada": "the stainless counter top of the roof cart",
     "luz": "warm late city light coming in low across the roofs",
     "audio": "faint traffic below, a radio somewhere, pigeons",
     "dela": "a loose black tee",
     "dela_bela": "a fitted black wrap top",
     "etnias": ["Black American"]},

    {"id": "atlanta", "familia": "atlanta", "regiao": "Atlanta",
     "cen": "an outdoor kitchen on the back patio of an Atlanta house, tall "
            "pines past the fence",
     "bancada": "the dark granite island top",
     "luz": "bright filtered daylight coming through the pines",
     "audio": "birds in the pines, a quiet yard, a far lawn mower",
     "dela": "a soft gold blouse",
     "dela_bela": "a fitted gold halter top",
     "etnias": ["Black American"]},

    {"id": "delta", "familia": "delta", "regiao": "Delta do Mississippi",
     "cen": "an outdoor kitchen under a metal awning behind a Mississippi "
            "Delta house, flat fields past a wire fence",
     "bancada": "the worn butcher-block counter",
     "luz": "flat wide daylight with the fields bright behind",
     "audio": "crickets, a truck on gravel, wind across the fields",
     "dela": "a faded floral house dress",
     "dela_bela": "a fitted red sundress",
     "etnias": ["Black American"]},

    {"id": "gullah", "familia": "gullah", "regiao": "Costa Gullah",
     "cen": "an outdoor kitchen on a screened coastal porch in the Gullah low "
            "country, live oaks and hanging moss past the rail",
     "bancada": "the painted wooden counter top",
     "luz": "soft coastal light filtered through the oaks",
     "audio": "marsh birds, wind in the moss, water somewhere close",
     "dela": "a loose indigo blouse",
     "dela_bela": "a fitted indigo halter dress",
     "etnias": ["Black American"]},

    {"id": "noroeste", "familia": "noroeste", "regiao": "Noroeste do Pacifico",
     "cen": "an outdoor kitchen on a cedar deck in the Pacific Northwest, wet "
            "firs crowding the yard behind it",
     "bancada": "the wet cedar counter boards",
     "luz": "cool overcast light, everything soft and damp",
     "audio": "rain dripping off the firs, a crow, a far chainsaw",
     "dela": "a green flannel shirt",
     "dela_bela": "a fitted olive tank top",
     "etnias": ["white American"]},

    {"id": "grandes_lagos", "familia": "grandes_lagos",
     "regiao": "Grandes Lagos",
     "cen": "an outdoor kitchen on a lakeside deck in the Great Lakes, birches "
            "and open water past the rail",
     "bancada": "the pale quartz counter top",
     "luz": "clear cool light coming off the water",
     "audio": "water against a dock, gulls, wind in the birches",
     "dela": "a striped cotton shirt",
     "dela_bela": "a fitted white bandeau top",
     "etnias": ["white American"]},

    {"id": "creole", "familia": "creole", "regiao": "Creole da Luisiana",
     "cen": "an outdoor kitchen in a Creole courtyard in Louisiana, brick "
            "walls, ferns and a wrought-iron gate behind",
     "bancada": "the brick counter with a tiled top",
     "luz": "warm filtered light bouncing off the brick",
     "audio": "a fountain, cicadas, a brass band far off",
     "dela": "a loose cream blouse",
     "dela_bela": "a fitted cream off-shoulder top",
     "etnias": ["Black American"]},

    {"id": "italo_americana", "familia": "italo_americana",
     "regiao": "italo-americana",
     "cen": "an outdoor kitchen under a grape arbour behind an Italian "
            "American house, tomato stakes along the fence",
     "bancada": "the tiled counter top",
     "luz": "warm afternoon light coming through the vine leaves",
     "audio": "cicadas, a radio in the house, plates somewhere inside",
     "dela": "a plain black blouse",
     "dela_bela": "a fitted black wrap dress",
     "etnias": ["white American"]},

    {"id": "florida", "familia": "florida", "regiao": "Florida",
     "cen": "an outdoor kitchen on a screened lanai in Florida, palms and a "
            "canal past the screen",
     "bancada": "the white quartz counter top",
     "luz": "bright even light coming through the screen",
     "audio": "a screen door, water in the canal, a small plane overhead",
     "dela": "a loose turquoise blouse",
     "dela_bela": "a fitted turquoise halter top",
     "etnias": ["white American"]},

    {"id": "americana", "familia": "americana", "regiao": "suburbio americano",
     "cen": "an outdoor kitchen on a concrete patio behind a suburban American "
            "house, a wooden fence and a basketball hoop past it",
     "bancada": "the grey concrete counter slab",
     "luz": "plain bright afternoon light across the patio",
     "audio": "a lawn mower, kids far off, a car door",
     "dela": "a plain grey tee",
     "dela_bela": "a fitted white cropped tank",
     "etnias": ["white American"]},

    # =======================================================================
    # + 2026-08-13 — AS NOVE QUE LEVAM O EIXO DE 15 A 24
    # =======================================================================
    # ⛔ Ordem do operador: *"aumente o pool de opcoes substancialmente, tambem
    # dos ambientes"*. Com 15 mundos e o filtro de etnia, a pagina BRANCA via 9
    # quintais e a NEGRA via 6 — e com memoria de 5 no ledger a pagina negra
    # repetia o quintal a cada seis videos. Pool pequeno com sorteio com memoria
    # ainda repete: a memoria adia, ela nao evita.
    #
    # ⭐⭐ E NENHUMA DELAS INVENTA FAMILIA NOVA, de proposito. O homem e'
    # filtrado pela `familia` do mundo, e o autoteste exige DOIS arquetipos por
    # familia — familia nova sem dois homens novos e' um eixo que o painel
    # mostra e que devolve sempre o mesmo rosto. Entao cada quintal novo e' uma
    # SEGUNDA VARIANTE de uma regiao que ja' existe: o mesmo homem cabe nos
    # dois, e quem varia e' o quintal.
    # ⚠️ Cobertura conferida por etnia: branca vai de 9 para 14 quintais, negra
    # de 6 para 10. Nenhuma etnia perdeu opcao.
    # ⛔ Contrato igual ao das quinze de cima, campo por campo — `bancada` e'
    # SLOT (nunca a palavra `counter` cravada no TAKE), e o traje dela vem nos
    # DOIS registros, `dela` e `dela_bela`, da MESMA regiao.
    # ⚠️ MOTOR IRMAO: as nove entradas abaixo sao IDENTICAS as do `mel16_short`,
    # caractere por caractere. Os dois nasceram por copia literal e testam UMA
    # variavel (o hook); quintal diferente entre eles seria uma segunda variavel
    # entrando de fininho, e o campo nao saberia a que atribuir a diferenca.

    {"id": "hill_country", "familia": "texas", "regiao": "Texas Hill Country",
     "cen": "an outdoor kitchen on a caliche patio behind a Hill Country stone "
            "house, live oaks and a windmill past the fence",
     "bancada": "the honed limestone counter top",
     "luz": "warm low sun coming in under the oaks",
     "audio": "cicadas, a windmill turning, cattle far off",
     "dela": "a plain khaki shirt with the sleeves rolled",
     "dela_bela": "a fitted white knotted shirt",
     "etnias": ["white American"]},

    {"id": "fazenda_milho", "familia": "meio_oeste",
     "regiao": "Meio-Oeste (fazenda)",
     "cen": "an outdoor kitchen beside a pole barn on an Iowa farmyard, corn "
            "standing tall past the gravel drive",
     "bancada": "the galvanised steel work counter",
     "luz": "flat bright daylight with the corn glowing behind",
     "audio": "a grain dryer humming, swallows, gravel underfoot",
     "dela": "a loose chambray work shirt",
     "dela_bela": "a fitted denim sleeveless top",
     "etnias": ["white American"]},

    {"id": "cascatas_rio", "familia": "noroeste",
     "regiao": "Cascades (cabana de rio)",
     "cen": "an outdoor kitchen under a cedar shelter beside a river cabin in "
            "the Cascades, wet ferns and moss on the rocks behind",
     "bancada": "the split cedar counter slab",
     "luz": "cool green light filtered through wet firs",
     "audio": "the river running, a woodpecker, water off the eaves",
     "dela": "a grey waffle-knit henley",
     "dela_bela": "a fitted forest green tank top",
     "etnias": ["white American"]},

    {"id": "michigan_varanda", "familia": "grandes_lagos",
     "regiao": "Grandes Lagos (chale)",
     "cen": "an outdoor kitchen on the screened porch of a Michigan lake "
            "cottage, cordwood stacked to the rail and birches beyond",
     "bancada": "the varnished pine counter top",
     "luz": "warm evening light coming in sideways through the screens",
     "audio": "moths on the screen, water on the shore, a far outboard",
     "dela": "a plain cream sweatshirt",
     "dela_bela": "a fitted cream ribbed tank",
     "etnias": ["white American"]},

    {"id": "golfo_bangalo", "familia": "florida", "regiao": "Costa do Golfo",
     "cen": "an outdoor kitchen on a paver patio beside a Gulf Coast bungalow, "
            "sea grapes and a boat trailer past the drive",
     "bancada": "the terrazzo counter slab",
     "luz": "hot white midday light bouncing off the pavers",
     "audio": "gulls, a trailer chain, wind off the water",
     "dela": "a loose pale yellow blouse",
     "dela_bela": "a fitted yellow halter top",
     "etnias": ["white American"]},

    {"id": "carolina_carport", "familia": "sulista", "regiao": "Carolinas",
     "cen": "an outdoor kitchen under a carport behind a South Carolina brick "
            "ranch house, crepe myrtle and a chain-link gate past it",
     "bancada": "the poured concrete counter top",
     "luz": "bright flat afternoon light under the carport roof",
     "audio": "cicadas, a car door two houses down, a screen door",
     "dela": "a loose lilac blouse",
     "dela_bela": "a fitted lilac wrap top",
     "etnias": ["Black American"]},

    {"id": "bed_stuy_jardim", "familia": "harlem",
     "regiao": "Brooklyn (quintal de brownstone)",
     "cen": "an outdoor kitchen in the fenced back garden of a Bed-Stuy "
            "brownstone, brick walls and a fire escape above",
     "bancada": "the butcher-block top of the garden cart",
     "luz": "warm late light coming over the brick wall",
     "audio": "kids down the block, a siren far off, pigeons",
     "dela": "a loose olive tee",
     "dela_bela": "a fitted olive halter top",
     "etnias": ["Black American"]},

    {"id": "pecan_delta", "familia": "delta",
     "regiao": "Delta (quintal da pecaneira)",
     "cen": "an outdoor kitchen set up under a big pecan tree in a Delta back "
            "yard, an oil-drum smoker and flat fields past the fence",
     "bancada": "the plank counter of the smoker table",
     "luz": "dappled light coming down through the pecan leaves",
     "audio": "cicadas, the smoker ticking, a dog barking far off",
     "dela": "a faded blue house dress",
     "dela_bela": "a fitted navy sundress",
     "etnias": ["Black American"]},

    {"id": "bayou_alpendre", "familia": "creole",
     "regiao": "Bayou da Luisiana",
     "cen": "an outdoor kitchen under a tin lean-to on a bayou porch, cypress "
            "knees and still brown water past the rail",
     "bancada": "the painted plank counter top",
     "luz": "warm heavy light coming low off the water",
     "audio": "frogs, a boat motor far off, insects close by",
     "dela": "a loose peach blouse",
     "dela_bela": "a fitted peach off-shoulder top",
     "etnias": ["Black American"]},
]

FAMILIAS_MUNDO = sorted({m["familia"] for m in MUNDOS})


def mundos_da_etnia(etnia):
    """Os mundos que comportam a etnia da pagina.

    ⚠️ CEDE para a lista inteira se nenhum casar: pagina nova sem mundo
    compativel nao pode derrubar o sorteio — quem reclama e' a lente PR6.
    """
    return [m for m in MUNDOS if etnia in m["etnias"]] or list(MUNDOS)


# ===========================================================================
# ⭐⭐ A COR — O EIXO QUE A FONTE NAO TEM
# ===========================================================================
# ⛔ Decisao 5 do operador: *"eixo de cor sorteavel"*. A fonte e' AZUL BERRANTE
# (cubos, liquido e caixa), e o azul contra a polo vermelha e o granito preto e'
# metade do impacto do frame — mas um lote inteiro de azul e' um video repetido
# quinze vezes.
#
# ⛔⛔ A COR E' UMA SO' E ATRAVESSA TUDO: os cubos do prato, o liquido do copo e
# a caixa de gelatina. Sortear a cor por OBJETO entregaria cubo verde virando
# bebida roxa, que e' o defeito de continuidade que o espectador perdoa menos —
# ele acabou de ver o cubo entrar na jarra. A lente PR4 cobra as tres.
# ⚠️ `sabor` NAO entra na fala: nomear o sabor e' ingrediente nomeado por outro
# caminho, e a fala ja' gasta a excecao do CT5 com os TRES que o operador
# escolheu.
CORES = [
    {"id": "azul", "curto": "azul", "cubo": "bright blue",
     "liquido": "bright blue", "caixa": "a blue and white gelatin carton"},
    {"id": "vermelho", "curto": "vermelho", "cubo": "deep red",
     "liquido": "deep red", "caixa": "a red and white gelatin carton"},
    {"id": "verde", "curto": "verde", "cubo": "bright green",
     "liquido": "bright green", "caixa": "a green and white gelatin carton"},
    {"id": "roxo", "curto": "roxo", "cubo": "deep purple",
     "liquido": "deep purple", "caixa": "a purple and white gelatin carton"},
    {"id": "ambar", "curto": "ambar", "cubo": "golden amber",
     "liquido": "golden amber", "caixa": "an amber and white gelatin carton"},
    {"id": "laranja", "curto": "laranja", "cubo": "bright orange",
     "liquido": "bright orange", "caixa": "an orange and white gelatin carton"},
]


# ===========================================================================
# OS PROPS FIXOS DA BANCADA
# ===========================================================================
# ⛔⛔ A CAIXA DE BICARBONATO E' INVARIANTE DESTE ANGULO, nao eixo 50/50 como no
# GOOD 16: aqui a fala NOMEIA o bicarbonato (a excecao do CT5), e prop nomeado
# na boca que nao esta' no quadro e' a contradicao que o espectador ouve.
# ⚠️ Descrita por FORMA e COR, nunca pelo rotulo legivel: `label sharp and
# readable` reprovou 200/200 no ESCANDALO 16 (lente ES13). O que a caixa precisa
# entregar e' a leitura instantanea de "bicarbonato de cozinha".
CAIXA_BICARBONATO = ("an orange and yellow cardboard box of baking soda")

# ⛔ O limao INTEIRO em quadro, cortado ao meio e aberto — e' o terceiro
# ingrediente da fala, e ele tem de estar la'.
# ⚠️ E a FALA nao diz `half a lemon`, mesmo a fonte dizendo: a doutrina do repo
# e' que a fala nao paga o que o quadro ja' mostra (sem medida, vasilhame nem
# fracao na copy falada). O QUADRO mostra a metade; a boca diz `a lemon`.
LIMAO = "a lemon cut in half with both halves face up"

PRATOS = [
    {"id": "ceramica_creme", "curto": "ceramica creme",
     "img": "a wide cream ceramic platter"},
    {"id": "esmalte_azul", "curto": "esmalte azul",
     "img": "a wide blue-glazed ceramic platter"},
    {"id": "louca_branca", "curto": "louca branca",
     "img": "a wide white ironstone platter"},
    {"id": "gres_pontilhado", "curto": "gres pontilhado",
     "img": "a wide speckled grey stoneware platter"},
    {"id": "vidro_grosso", "curto": "vidro grosso",
     "img": "a wide heavy clear glass platter"},
    {"id": "esmaltado_borda", "curto": "esmaltado de borda",
     "img": "a wide enamelled metal platter with a dark rim"},
]

# ⛔ O recipiente do PREPARO — o que a fonte usa e' o copo de um liquidificador,
# com a base de laminas em baixo. ⚠️ Ele NAO e' ligado em cena: motor girando e'
# ruido que come a fala de 8 segundos, e a fonte tambem nao liga.
# ⛔⛔ TODA ENTRADA CARREGA O SUBSTANTIVO `jug`, e isso NAO e' pobreza de
# vocabulario: o TAKE 02 se refere ao objeto como `the jug`, e o
# `sc.lint_take_vs_image` reprova — corretamente — quando o TAKE cita um objeto
# que a IMAGE do mesmo bloco nao tem. Com `pitcher` no pool, 197 de 400 videos
# mandavam animar uma jarra que o quadro nao continha. Medido na primeira
# execucao do autoteste, antes de qualquer render.
# ⚠️ A variacao continua existindo no QUALIFICADOR (liquidificador, bico,
# alca), que e' onde ela sempre esteve — o substantivo e' so' o ponteiro.
JARRAS = [
    {"id": "liquidificador", "curto": "jarra de liquidificador",
     "img": "a glass blender jug with its blade base"},
    {"id": "jarra_vidro", "curto": "jarra de vidro",
     "img": "a heavy clear glass jug"},
    {"id": "jarra_bico", "curto": "jarra de bico",
     "img": "a tall clear glass jug with a pouring lip"},
    {"id": "jarra_alca", "curto": "jarra de alca",
     "img": "a thick clear glass jug with a moulded handle"},
]


# ===========================================================================
# ⭐⭐ QUEM FALA — UM ARQUETIPO NORTE-AMERICANO POR REGIAO
# ===========================================================================
# ⛔⛔ POOL REESCRITO EM 2026-08-12, no mesmo dia em que nasceu. Ordem do
# operador, lendo o painel: *"troque a pool do agente prato16 para arquetipos
# tipicos de norte americanos por diferentes regioes dentro dos EUA"*.
#
# ⚠️ O QUE ESTAVA ERRADO: o pool anterior tinha dez senhores CORRETOS e
# GENERICOS — prata penteado, careca de cavanhaque, barba branca. Nenhum deles
# era de LUGAR NENHUM. O motor ja' arrastava o mundo inteiro por regiao
# (cenario, bancada, luz, audio, traje dela) e punha no meio dele um homem que
# poderia estar em qualquer um dos quinze. O eixo mais visivel do quadro — o
# rosto que fala — era o unico que nao sabia onde estava.
#
# ⭐ AGORA CADA ENTRADA DECLARA `familias`, e o homem e' filtrado pelo mundo JA'
# SORTEADO. E' a mesma mecanica de `mundos_da_etnia`, um degrau adiante: a
# regiao arrasta o quintal E quem esta' nele.
# ⚠️ Toda familia tem PELO MENOS DUAS opcoes — uma so' seria eixo morto: o
# painel mostraria `trocar` e devolveria sempre o mesmo homem, que e' o botao
# que mente. O autoteste cobra isso familia por familia.
#
# ⛔ NENHUMA ENTRADA DIZ COR DE PELE. A etnia vem da PAGINA e ja' entra na
# frase (`a 66-year-old white American man`); descrever pele aqui criaria duas
# vozes no mesmo sintagma — o defeito FT14 que trocou a mulher entre os takes do
# FIGHT 16. O arquetipo e' CABELO, PELO FACIAL e ANCORA, nunca tom.
# ⛔ DISTINTIVO, NUNCA DETERIORADO (doutrina do PLACA 16): zero cicatriz, nariz
# quebrado, dente lascado ou `weathered`. Num homem de 68, dano renderiza como
# mendigo — o operador ja' reprovou um pool inteiro por isso.
# ⛔ E ZERO PALAVRA DE APROVACAO (`handsome`, `strong jaw`): elogio no prompt
# puxa o rosto para a media do banco de imagem, o mesmo mecanismo pelo qual
# `not a celebrity` invoca a celebridade.
# ⚠️ Os oculos entram em 6 das 21: a fonte usa, e um pool sem eles perde o
# marcador etario mais barato que existe.
HOMENS = [
    # --- APALACHES / NOROESTE: o homem de montanha, barba de verdade -------
    {"id": "montanhes_barba", "idade": 67, "familias": ["apalache", "noroeste"],
     "rotulo": "67y · grisalho curto + barba cheia",
     "cabeca": "grey hair cut short under the ears and a full grey beard "
               "grown out",
     "marca": "heavy level brows and deep laugh lines"},
    {"id": "apalache_careca", "idade": 63, "familias": ["apalache", "noroeste"],
     "rotulo": "63y · careca + barba sal-e-pimenta",
     "cabeca": "a bald crown with the sides clipped close and a thick "
               "salt-and-pepper beard",
     "marca": "a shallow cleft in his chin"},
    {"id": "noroeste_longo", "idade": 61, "familias": ["noroeste", "apalache"],
     "rotulo": "61y · grisalho longo + oculos na testa",
     "cabeca": "grey hair worn a little long over the ears and a short "
               "trimmed beard",
     "marca": "rimless glasses pushed up on his head"},

    # --- SUL PROFUNDO / DELTA: o cavalheiro de bigode ----------------------
    {"id": "sulista_bigode", "idade": 65, "familias": ["sulista", "delta"],
     "rotulo": "65y · prata penteado + bigode branco",
     "cabeca": "silver hair combed back and a thick white moustache",
     "marca": "a beauty mark high on one cheekbone"},
    {"id": "delta_careca", "idade": 69, "familias": ["delta", "sulista"],
     "rotulo": "69y · careca + bigode branco + oculos",
     "cabeca": "a cleanly shaved head and a neat white moustache",
     "marca": "gold half-moon glasses and a dimple beside his mouth"},
    {"id": "sulista_branco", "idade": 62, "familias": ["sulista", "gullah"],
     "rotulo": "62y · branco curto + barba aparada",
     "cabeca": "short white hair in a clean taper and a close white beard",
     "marca": "a silver streak running through one eyebrow"},

    # --- TEXAS: o bigode largo, o cabelo curto -----------------------------
    {"id": "texano_bigode", "idade": 64, "familias": ["texas", "americana"],
     "rotulo": "64y · grisalho raspado + bigode largo",
     "cabeca": "close-cropped grey hair and a wide grey moustache that covers "
               "his top lip",
     "marca": "deep laugh lines and heavy brows"},
    {"id": "texano_prata", "idade": 66, "familias": ["texas", "americana"],
     "rotulo": "66y · prata farto + barbeado + fenda",
     "cabeca": "thick silver hair cut short at the sides, clean-shaven",
     "marca": "a deep cleft in his chin"},

    # --- MEIO-OESTE / GRANDES LAGOS: o pai de familia, sem firula ----------
    {"id": "meio_oeste_oculos", "idade": 61,
     "rotulo": "61y · grisalho curto + oculos finos",
     "familias": ["meio_oeste", "grandes_lagos", "americana"],
     "cabeca": "short grey hair in a clean taper, clean-shaven",
     "marca": "thin wire-rimmed glasses and a dimple in one cheek"},
    {"id": "lagos_escovinha", "idade": 59,
     "rotulo": "59y · escovinha prata + barbeado",
     "familias": ["grandes_lagos", "meio_oeste"],
     "cabeca": "a silver brush cut kept very short, clean-shaven",
     "marca": "a straight narrow nose and laugh lines at the eyes"},
    # ⚠️ 2026-08-13: `white hair THINNING at the crown` saiu (*"melhore a
    # aparencia e shape desses homens"*). Rarefacao nao e' ancora — e' avaria, e
    # a ancora deste homem sempre foram os oculos pesados. O cabelo so' precisa
    # ser branco e curto.
    {"id": "meio_oeste_barba", "idade": 68,
     "rotulo": "68y · branco curto + barba + oculos",
     "familias": ["meio_oeste", "grandes_lagos"],
     "cabeca": "a full head of white hair cut short and a short white beard",
     "marca": "heavy dark-rimmed glasses"},

    # --- NOVA INGLATERRA / ITALO-AMERICANA: o cabelo farto penteado --------
    {"id": "yankee_branco", "idade": 70,
     "rotulo": "70y · branco farto + oculos meia-lua",
     "familias": ["nova_inglaterra", "italo_americana"],
     "cabeca": "thick white hair cut neatly above the collar, clean-shaven",
     "marca": "gold half-moon glasses and a shallow cleft chin"},
    {"id": "italo_prata", "idade": 65,
     "rotulo": "65y · prata para tras + sobrancelha forte",
     "familias": ["italo_americana", "nova_inglaterra"],
     "cabeca": "thick silver hair swept straight back, clean-shaven",
     "marca": "heavy dark level brows and a beauty mark near his jaw"},
    {"id": "yankee_cavanhaque", "idade": 62,
     "rotulo": "62y · grisalho com risca + cavanhaque",
     "familias": ["nova_inglaterra", "italo_americana", "grandes_lagos"],
     "cabeca": "short grey hair with a sharp side part and a trimmed grey "
               "goatee",
     "marca": "a dimple that shows on one side"},

    # --- HARLEM / ATLANTA / CREOLE / GULLAH -------------------------------
    {"id": "harlem_careca", "idade": 63, "familias": ["harlem", "atlanta"],
     "rotulo": "63y · careca + cavanhaque + argola",
     "cabeca": "a cleanly shaved head and a short white goatee",
     "marca": "a plain gold hoop in one ear"},
    {"id": "atlanta_fade", "idade": 60,
     "rotulo": "60y · fade grisalho + barba rente",
     "familias": ["atlanta", "harlem", "creole"],
     "cabeca": "a short grey fade with a clean line at the temples and a "
               "close-trimmed grey beard",
     "marca": "a dimple in one cheek"},
    {"id": "gullah_barba", "idade": 69, "familias": ["gullah", "delta"],
     "rotulo": "69y · branco natural + barba cheia",
     "cabeca": "short white natural hair and a full white beard kept neatly "
               "shaped",
     "marca": "deep laugh lines at the corners of his mouth"},
    {"id": "creole_risca", "idade": 64,
     "rotulo": "64y · sal-e-pimenta + bigode + oculos",
     "familias": ["creole", "gullah", "harlem"],
     "cabeca": "salt-and-pepper hair with a clean side part and a thin "
               "moustache",
     "marca": "thin wire-rimmed glasses and a straight narrow nose"},
    {"id": "harlem_prata", "idade": 66, "familias": ["harlem", "creole"],
     "rotulo": "66y · prata rente + bigode prateado",
     "cabeca": "short silver hair kept close to the crown and a trimmed "
               "silver moustache",
     "marca": "a beauty mark high on one cheekbone"},

    # --- FLORIDA: o aposentado, e e' o retrato da fonte --------------------
    {"id": "florida_morsa", "idade": 68, "familias": ["florida", "americana"],
     "rotulo": "68y · careca + bigode de morsa + oculos",
     "cabeca": "a bald crown with the sides clipped short and a full white "
               "walrus moustache",
     "marca": "thin wire-rimmed glasses and deep laugh lines"},
    # ⚠️ 2026-08-13: `combed FORWARD` saiu pela mesma ordem. E' literalmente o
    # REF que o operador reprovou vendo o render no ALFA 16 (*"retire esse ref
    # feio"*): cabelo penteado para a frente le' como quem esconde entrada.
    {"id": "florida_branco", "idade": 66, "familias": ["florida", "sulista"],
     "rotulo": "66y · branco com risca + barbeado",
     "cabeca": "short white hair in a neat side part, clean-shaven",
     "marca": "a small pale birthmark near one temple"},

    # --- SUBURBIO AMERICANO -----------------------------------------------
    {"id": "suburbano_taper", "idade": 58, "familias": ["americana", "texas"],
     "rotulo": "58y · grisalho classico + covinha",
     "cabeca": "grey hair in a clean classic taper, clean-shaven",
     "marca": "a dimple beside his mouth"},
]

FAMILIAS_HOMEM = sorted({f for h in HOMENS for f in h["familias"]})


def homens_da_familia(familia):
    """Os arquetipos que pertencem a' regiao sorteada.

    ⚠️ CEDE para a lista inteira se nenhum casar: familia nova sem homem
    declarado nao pode derrubar o sorteio — quem reclama e' o autoteste, que
    cobra DUAS opcoes por familia.
    """
    return [h for h in HOMENS if familia in h["familias"]] or list(HOMENS)


MOLDE_H = dict(HOMENS[0], corpo="")

# ⛔ O corpo dele com o MODO FORTE DESLIGADO. ⚠️ Ele esta' VESTIDO neste angulo
# (polo, como a fonte) — entao o corpo e' PORTE, nao musculatura exposta: pedir
# veia no antebraco de um homem de polo e' pedir o que o quadro nao mostra.
CORPOS_H = [
    "a solid build with square shoulders",
    "a heavy build, broad through the chest",
    "a lean upright frame with long arms",
    "a compact build with a deep chest",
    "a tall build with sloping shoulders",
    "a stocky build with thick forearms",
    # + 2026-08-13 — ordem do operador: *"melhore a aparencia e shape desses
    # homens"* / *"aumente o pool de opcoes substancialmente"*. Seis entradas
    # repetiam o porte a cada seis videos.
    # ⚠️ E o registro NAO muda: aqui ele esta' de POLO, entao o corpo continua
    # sendo PORTE e nunca musculatura exposta — pedir veia no antebraco de um
    # homem de manga e' pedir o que o quadro nao mostra. (No motor irmao
    # `mel16`, de regata, o mesmo eixo e' descrito com braco justamente porque
    # la' o braco aparece.)
    "an upright build with a straight back",
    "a broad build with a full chest",
    "a trim build with narrow shoulders",
    "a thickset build with a short neck",
    "a long-limbed build with a lean torso",
    "an average build carrying a little weight in the middle",
    "a square build with even shoulders",
    "a slight build with a narrow chest",
]

# ⛔ A polo e' o uniforme do angulo (a fonte usa vermelha), e a COR e' sorteada
# a' parte: polo da mesma cor da gelatina em todo video seria um lote monocromo.
# ⚠️ Nenhuma cor daqui repete o `cubo` de `CORES` no mesmo video — a lente PR4b
# cobra, porque homem de polo azul segurando cubo azul apaga o prop.
POLOS = ["a red polo shirt", "a navy polo shirt", "a white polo shirt",
         "a charcoal polo shirt", "a forest green polo shirt",
         "a burgundy polo shirt", "a light grey polo shirt",
         "a tan polo shirt"]


# ===========================================================================
# A ESPOSA — E ELA SO' EXISTE NO TAKE 2
# ===========================================================================
# ⛔ Decisao 4 do operador. A fonte e' SOLO; ela e' acrescimo nosso, e entra
# COLADA no lado dele olhando o copo, muda.
# ⛔ A FAIXA E' DE ESPOSA REAL DE UM SENHOR (46-58), nao a REF do pool bela —
# e' a mecanica do BED 16: *"desligado entrega a esposa realista do print,
# ligado traz a REF do pool bela"*. Uma de 27 ao lado de um de 68 le' como
# outra coisa, e nao e' o que o angulo vende.
# ⛔ NENHUMA ENTRADA DIZ COR DE PELE (licao FT14 do FIGHT 16): a etnia declarada
# e' a UNICA autoridade sobre a cor, e pele escrita aqui brigaria com ela.
MULHERES = [
    {"id": "prata_curto", "etnia": "white American", "idade": 54,
     "porte": "of medium build",
     "cabeca": "silver hair cut short and layered",
     "marca": "laugh lines at the eyes"},
    {"id": "loira_ombro", "etnia": "white American", "idade": 49,
     "porte": "slim and narrow-shouldered",
     "cabeca": "blonde hair cut blunt at the shoulders",
     "marca": "a small beauty spot above her lip"},
    {"id": "castanho_preso", "etnia": "white American", "idade": 57,
     "porte": "of full build",
     "cabeca": "brown hair going grey, pinned back",
     "marca": "reading glasses on a chain"},
    {"id": "trancas_gris", "etnia": "Black American", "idade": 55,
     "porte": "tall and straight-backed",
     "cabeca": "greying braids gathered at the nape",
     "marca": "small gold hoops in both ears"},
    {"id": "afro_curto", "etnia": "Black American", "idade": 51,
     "porte": "of medium build with square shoulders",
     "cabeca": "a short natural afro with grey coming in at the temples",
     "marca": "a beauty spot on one cheek"},
    {"id": "coque_branco", "etnia": "Black American", "idade": 58,
     "porte": "small and lightly built",
     "cabeca": "white hair gathered in a low bun",
     "marca": "deep laugh lines and a wide smile"},
    {"id": "latina_ondulado", "etnia": "Latina American", "idade": 50,
     "porte": "of medium build",
     "cabeca": "dark wavy hair worn to the shoulders with grey at the roots",
     "marca": "a small mole beside one eye"},
    {"id": "asiatica_liso", "etnia": "Asian American", "idade": 46,
     "porte": "slim with rounded shoulders",
     "cabeca": "straight black hair cut to the jaw",
     "marca": "fine laugh lines and a smooth complexion"},

    # -----------------------------------------------------------------------
    # + 2026-08-13 — AS QUATORZE QUE LEVAM A ESPOSA DE 8 A 22
    # -----------------------------------------------------------------------
    # ⛔ Ordem do operador: *"aumente o pool de opcoes substancialmente"*. Com
    # OITO entradas e memoria de 4 no ledger, um lote de 10 videos trazia a
    # mesma esposa duas ou tres vezes — e ela e' metade do quadro 2, que e' o
    # quadro do CTA.
    # ⛔ MESMO CONTRATO das oito acima: faixa de ESPOSA REAL de um senhor
    # (46-58), ZERO cor de pele (a etnia declarada e' a unica autoridade, licao
    # FT14 do FIGHT 16) e ancora SAUDAVEL — nada de cicatriz, dente falhado,
    # pele castigada. Marca e' o que se LEMBRA entre dois quadros gerados
    # separadamente, nao o que se lamenta.
    # ⚠️ OCULOS EM 6 DAS 22 (27%): eram 1 em 8. E' o marcador etario mais barato
    # que existe e o unico eixo que estava praticamente parado neste pool.
    # ⭐ E as quatro etnias giram: 8 brancas, 8 negras, 3 latinas, 3 asiaticas —
    # ela e' o eixo SOLTO deste angulo (quem a pagina governa e' o HOMEM, que e'
    # quem fala), entao aqui a variacao e' de graca.
    # ⚠️ MOTOR IRMAO: identicas as do `mel16_short`, caractere por caractere.
    # ⚠️ CADA `marca` CARREGA UMA ANCORA QUE O MEDIDOR RECONHECE (pinta, sinal
    # de nascenca, covinha, brinco, mecha, fenda) e METADE carrega tambem um
    # marcador de PELE SAUDAVEL (sarda, laugh lines, smooth-skinned). Nao e'
    # enfeite: `medir_personagens.py` mede os seis eixos, e a primeira versao
    # destas quatorze usava `beauty SPOT` — que le' igual e que o medidor nao
    # conhece. Pool grande com eixo parado e' pool grande de um personagem so'.
    {"id": "ruiva_curta", "etnia": "white American", "idade": 52,
     "porte": "of slim build",
     "cabeca": "copper-red hair cut short and swept back",
     "marca": "freckles across her nose and a beauty mark on one temple"},
    {"id": "loira_coque", "etnia": "white American", "idade": 56,
     "porte": "tall and broad-shouldered",
     "cabeca": "ash-blonde hair gathered into a loose bun",
     "marca": "tortoiseshell glasses pushed up on her head and a small mole "
              "on her jaw"},
    {"id": "castanho_ondulado", "etnia": "white American", "idade": 47,
     "porte": "of medium build with a narrow waist",
     "cabeca": "chestnut hair worn wavy to the shoulders",
     "marca": "laugh lines at her eyes and a dimple in one cheek"},
    {"id": "grisalha_lisa", "etnia": "white American", "idade": 58,
     "porte": "small and lightly built",
     "cabeca": "steel-grey hair cut blunt at the chin",
     "marca": "thin gold-rimmed glasses and a shallow cleft in her chin"},
    {"id": "morena_franja", "etnia": "white American", "idade": 48,
     "porte": "of full build",
     "cabeca": "dark brown hair with a soft fringe to the eyebrows",
     "marca": "a beauty mark above her left eyebrow"},
    {"id": "locs_gris", "etnia": "Black American", "idade": 53,
     "porte": "of medium build with a long neck",
     "cabeca": "shoulder-length locs with grey through them, gathered to one "
               "side",
     "marca": "gold studs in both ears, smooth-skinned"},
    {"id": "twist_curto", "etnia": "Black American", "idade": 49,
     "porte": "slim and long-limbed",
     "cabeca": "hair in short defined twists with grey at the temples",
     "marca": "a beauty mark high on one cheekbone"},
    {"id": "bob_preto", "etnia": "Black American", "idade": 57,
     "porte": "of full build",
     "cabeca": "black hair pressed straight into a chin-length bob with grey "
               "at the part",
     "marca": "dark-rimmed reading glasses and a small mole beside her mouth"},
    {"id": "coque_alto_gris", "etnia": "Black American", "idade": 55,
     "porte": "tall and full-figured",
     "cabeca": "silver-grey hair pulled up into a high bun",
     "marca": "small pearl studs in both ears and fine laugh lines"},
    {"id": "cacheada_prata", "etnia": "Black American", "idade": 51,
     "porte": "of solid build",
     "cabeca": "grey natural curls worn full around her face",
     "marca": "a wide mouth with a deep cupid's bow and a mole on one "
              "cheekbone"},
    {"id": "latina_coque", "etnia": "Latina American", "idade": 53,
     "porte": "of full build",
     "cabeca": "dark hair with grey at the temples gathered into a low knot",
     "marca": "thin wire-rimmed glasses and a mole beside one eyebrow"},
    {"id": "latina_curto", "etnia": "Latina American", "idade": 48,
     "porte": "of trim build",
     "cabeca": "dark hair cut short and layered with silver coming in",
     "marca": "freckles high on both cheekbones and a small gold stud in one "
              "nostril"},
    {"id": "asiatica_coque", "etnia": "Asian American", "idade": 56,
     "porte": "small and finely built",
     "cabeca": "black hair going grey, pinned up in a neat twist",
     "marca": "smooth-skinned, with a beauty mark at the corner of one eye"},
    {"id": "asiatica_gris", "etnia": "Asian American", "idade": 50,
     "porte": "of medium build and upright",
     "cabeca": "salt-and-pepper hair cut to a soft shoulder length",
     "marca": "square glasses in a pale tortoiseshell frame and a dimple "
              "beside her mouth"},
]


# ===========================================================================
# ⭐⭐ A COPY — o arco medido no reel, quase palavra por palavra
# ===========================================================================
# ---------------------------------------------------------------------------
# cena 1 = A DESCOBERTA + OS TRES INGREDIENTES
# ---------------------------------------------------------------------------
# ⚠️ CT2 do CONTRATO-COPY-16S: este take NAO enuncia falha — ele e' TESTEMUNHO
# DE DESCOBERTA, que e' outro molde. E' a mesma excecao do GOOD 16 (aviso de
# excesso) e do ALFA 16 (aviso brincalhao), e a regra que sobra e' a de sempre:
# quem nao enuncia falha TEM DE SABER que nao enuncia. Por isso o CT2 e'
# filtrado no `lint` deste motor e declarado no `medir_copy16`.
DESCOBERTAS = [
    "Honestly, this was the best discovery I ever made for my marriage.",
    "This is the best thing I ever found for my marriage.",
    "Honestly, nothing I ever tried did more for my marriage.",
    "This one discovery changed my marriage more than anything else.",
    "Best thing that ever happened to my marriage, and I am serious.",
    "Honestly, my marriage changed the week I found this out.",
    "I found this late in life and my marriage has never been better.",
    "Nothing in thirty years did for my marriage what this did.",
    "This is the one thing that gave my marriage back to me.",
    "Honestly, my wife noticed before I said a single word.",
    "My marriage turned around on the day I learned this.",
    "This is the best thing I ever put in a glass.",
    # + 2026-08-12, no mesmo dia em que o pool nasceu: 12 x 8 dava 96
    # combinacoes e o autoteste mediu 95 falas distintas em 400 sorteios — num
    # lote de 50 videos a cena 1 se repetiria a cada dez. ⛔ O molde e' que
    # varia, nao so' a palavra: o operador ja' apontou isso no GOOD 16 (*"variar
    # a PALAVRA dentro do mesmo molde nao varia o video"*), e as entradas
    # abaixo abrem em sujeitos diferentes — a esposa, os anos, o vizinho, a
    # cozinha — em vez de todas em `Honestly, this`.
    "My wife asked what I was doing different. This is it.",
    "Sixty years old, and I found this out by accident.",
    "A neighbour told me about this and it changed everything.",
    "Everything I needed was already there in my own kitchen.",
    "Two weeks of this and my wife stopped asking questions.",
    "I wish somebody had told me this thirty years ago.",
    "My doctor never mentioned this to me. A friend did.",
    "The best thing in my marriage came out of my own kitchen.",
]

# ---------------------------------------------------------------------------
# ⛔⛔ RECEITAS — AQUI O CT5 E' FURADO, POR ORDEM DIRETA DO OPERADOR
# ---------------------------------------------------------------------------
# Decisao 2 de 2026-08-12, perguntada com as tres opcoes na mesa e escolhida
# com o preco escrito na frente: *"furar o CT5 neste angulo, declarado"*.
#
# ⛔ O QUE O CT5 DIZ, e continua valendo nos outros dezoito motores: *"nenhum
# ingrediente nomeado na fala — a receita e' a UNICA moeda que o comentario
# compra, e entregue uma vez ela esta' gasta para os outros 49 videos da
# pagina"*.
# ⭐ O QUE PESOU DO OUTRO LADO: a fonte nomeia os tres na cara e fez 1.6K
# COMENTARIOS — mais comentario que reacao. A hipotese que este angulo testa e'
# que a receita DITA nao esvazia o pedido: ela o torna CRIVEL, e o que o
# comentario compra deixa de ser a lista e passa a ser o COMO (proporcao,
# preparo, quando tomar) — que continua so' na DM.
# ⚠️ E' HIPOTESE, NAO FATO, e o campo decide. Se o comentario cair neste angulo
# contra os outros, a causa candidata numero um esta' escrita aqui.
#
# ⛔ SEM MEDIDA, SEM VASILHAME, SEM FRACAO: a fonte diz `half a lemon` e nos
# dizemos `a lemon`. A fala nao paga o que o quadro ja' mostra — o QUADRO tem o
# limao cortado ao meio, e gastar palavra do orcamento de 25 para dizer o que a
# imagem entrega de graca e' o erro que o repo ja' catalogou.
# ⚠️ 5 a 8 palavras, e o teto e' ARITMETICA: com a menor DESCOBERTA (9) uma
# entrada de 17 caberia — mas o piso importa mais aqui, e a lista fica curta de
# proposito. Este beat e' uma ENUMERACAO; enumeracao longa vira lista de
# compras e mata o ritmo do hook.
RECEITAS = [
    "Gelatin, a lemon, and baking soda.",
    "Just gelatin, a lemon, and baking soda.",
    "Gelatin, lemon, baking soda. That is all.",
    "Only gelatin, a lemon, and baking soda.",
    "Gelatin, a lemon and baking soda, nothing else.",
    "Three things: gelatin, a lemon, baking soda.",
    "Gelatin, a lemon, baking soda. Nothing from a pharmacy.",
    "Gelatin, a lemon, and baking soda. That is the whole list.",
    "Gelatin, a lemon, and baking soda. Nothing you have to buy.",
    "Gelatin, a lemon, baking soda. All from my own kitchen.",
    "Gelatin, a lemon and baking soda. No pharmacy in it.",
    "It is gelatin, a lemon, and baking soda.",
    "Gelatin, a lemon, baking soda. Three things.",
    "Nothing but gelatin, a lemon, and baking soda.",
]

# ---------------------------------------------------------------------------
# ⭐⭐ cena 2 = A PROVA + A FACILIDADE + O CTA
# ---------------------------------------------------------------------------
# ⛔⛔ A PROVA E' EM PRIMEIRA PESSOA, E ISSO E' A DEFESA DO ANGULO. A fonte diz
# `I'm rock hard, just like when I was 18` — o sujeito e' ELE, nao o orgao. A
# licao paga no COLO 16 (~95% de recusa) foi sobre o PAR `verbo de ereccao
# COLADO no orgao`; sem o orgao na sentenca o mesmo verbo passa, e o FIGHT 16 e
# o ALFA 16 ja' provaram o inverso em campo no mesmo dia.
# ⛔ Entao NENHUMA entrada nomeia o orgao — nao por pudor, por engenharia: o
# apelido aqui traria de volta exatamente o par que reprova. A lente PR-ORGAO
# cobra isso na fala inteira, nos dois takes.
# ⚠️ E o `18` da fonte fica: a idade concreta e' o que faz a frase ser um
# testemunho e nao um slogan.
PROVAS = [
    "I am rock hard, just like when I was eighteen.",
    "I get rock hard again, the way I did at eighteen.",
    "At my age I am harder than I was at forty.",
    "I am hard like a teenager again, at my age.",
    "Rock hard again, just like when I was a young man.",
    "I am back to how I was at twenty five.",
    "Every night I am hard the way I was decades ago.",
    "I am harder now than I was in my forties.",
    "It brought me back to eighteen, and my wife agrees.",
    "I am rock hard again after all these years.",
]

# ⚠️ O beat mais dispensavel dos tres e o unico sem promessa nem comando — por
# isso e' ele que absorve a sobra do orcamento.
# ⛔ E ele NAO repete ingrediente: a enumeracao ja' aconteceu no take 1, e
# repetir gastaria a excecao do CT5 duas vezes pelo mesmo preco.
FACILIDADES = [
    "Simple ingredients, quick prep.",
    "Cheap, simple, and fast.",
    "No pills, no prescriptions.",
    "No pharmacy, no doctor.",
    "Simple stuff, no complicated routine.",
    "Quick to make, costs almost nothing.",
    "No routine, no waiting around.",
    "Costs pocket change, takes a minute.",
]

# ⛔⛔ A fonte pede `recipe`. NAO COPIAMOS o comando: a automacao de DM casa
# palavra EXATA e o funil inteiro roda em `gelatin`. O literal vem de
# `sc.CTA_LITERAL`, nunca redigitado — e a VIRGULA depois de `gelatin` e'
# intocavel (a legenda nasce do Whisper em cima do audio, e sem a micro-pausa o
# Veo emenda e narra `gelatine`).
# ⭐⭐ TODA ENTRADA DIZ ONDE A RECEITA CHEGA (CT6) — e a fonte ja' dizia
# (`to get it in your inbox`), o que e' raro no repertorio garimpado.
# ⛔ CT1: nada vem depois desta sentenca.
CTAS = [
    "%s and the recipe goes to your messages." % sc.CTA_LITERAL,
    "%s and the recipe lands in your inbox." % sc.CTA_LITERAL,
    "%s and I'll send the recipe by message." % sc.CTA_LITERAL,
    "%s and the whole recipe hits your inbox." % sc.CTA_LITERAL,
    "%s and I'll send the recipe in private." % sc.CTA_LITERAL,
    "%s and your inbox gets the recipe tonight." % sc.CTA_LITERAL,
    "%s and only your messages get the recipe." % sc.CTA_LITERAL,
    "%s and the recipe comes straight to your messages." % sc.CTA_LITERAL,
]


# ===========================================================================
# HELPERS
# ===========================================================================

def _palavras(s):
    return len(re.findall(r"[A-Za-z']+", s or ""))


def _cap(s):
    return s[0].upper() + s[1:] if s else s


def _carregar_ledger():
    try:
        with open(LEDGER, "r", encoding="utf-8") as f:
            return json.load(f)
    except (IOError, ValueError):
        return {}


EIXOS_LEDGER = ("mundo", "homem", "mulher", "cor", "prato")


def _anotar(ledger, spec):
    hist = ledger.setdefault(spec["pagina"], {})
    for eixo in EIXOS_LEDGER:
        val = spec.get(eixo)
        if isinstance(val, dict):
            hist.setdefault(eixo, []).append(val.get("id"))


def _gravar_ledger(ledger, spec=None):
    if spec is not None:
        _anotar(ledger, spec)
    try:
        with open(LEDGER, "w", encoding="utf-8") as f:
            json.dump(ledger, f, ensure_ascii=False, indent=1)
    except IOError:
        pass


def _fresco(pool, usados, rng):
    """Uma entrada evitando as ultimas usadas — e CEDE quando nada sobra.

    ⛔ Pool grande com sorteio SEM memoria repete igual: e' a licao do PEE 16,
    onde duas ampliacoes de pool nao resolveram a repeticao porque o sorteio era
    `rng.choice` cru.
    """
    livres = [x for x in pool if x.get("id") not in usados]
    return rng.choice(livres or pool)


def _por_id(pool, valor, chave="id"):
    """A entrada do pool, aceitando ID (string) OU a ENTRADA JA' RESOLVIDA.

    ⛔⛔ OS DOIS FORMATOS SAO OBRIGATORIOS, e o segundo e' o que o PAINEL manda
    (o cadeado devolve `self.spec[chave]`, o dicionario inteiro). A versao
    ingenua (`x["id"] == valor`) nunca casa com um dicionario, devolve `None` e
    o `resumo_pt` estoura DENTRO do callback do tkinter — bug que quebrou os
    quatro cadeados do GOOD 16 e que so' apareceu porque o app foi EXERCITADO em
    vez de apenas aberto.
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
    minimo em todos o ULTIMO beat fica preso; com a mediana em todos o PRIMEIRO
    fica preso.
    """
    f = dict(enumerate(spec.get("falas", ["", ""])))

    if 0 in quais:
        de = rng.choice(_cabe(DESCOBERTAS, _mn(RECEITAS), 1))
        re_ = rng.choice(_cabe(RECEITAS, _palavras(de), 1))
        f[0] = "%s %s" % (de, re_)

    if 1 in quais:
        # ⛔ O CTA escolhe PRIMEIRO: ele carrega o literal `Comment gelatin,` e
        # o endereco da entrega, e nao se encurta. A FACILIDADE e' o beat mais
        # intercambiavel e vai por ULTIMO, absorvendo a sobra.
        ct = rng.choice(_cabe(CTAS, _mn(PROVAS) + _mn(FACILIDADES), 2))
        pr = rng.choice(_cabe(PROVAS,
                              _palavras(ct)
                              + _rsv([_palavras(x) for x in FACILIDADES]), 2))
        fa = rng.choice(_cabe(FACILIDADES, _palavras(ct) + _palavras(pr), 2))
        f[1] = "%s %s %s" % (pr, fa, ct)

    return f


def sortear(pagina, rng, ledger, travas=None):
    travas = travas or {}
    hist = (ledger or {}).get(pagina, {})
    etnia = ETNIA.get(pagina, "white American")

    # ⛔ O MUNDO E' FILTRADO PELA ETNIA DA PAGINA.
    pool_m = mundos_da_etnia(etnia)
    if travas.get("familia_mundo"):
        fam = [m for m in pool_m if m["familia"] == travas["familia_mundo"]]
        pool_m = fam or pool_m
    mundo = (_por_id(MUNDOS, travas["mundo"]) if travas.get("mundo")
             else _fresco(pool_m, hist.get("mundo", [])[-5:], rng))

    # ⭐⭐ O HOMEM E' FILTRADO PELA REGIAO JA' SORTEADA (2026-08-12): o mundo
    # escolhe primeiro, e o arquetipo sai de quem pertence aquela familia.
    homem = (_por_id(HOMENS, travas["homem"]) if travas.get("homem")
             else _fresco(homens_da_familia(mundo["familia"]),
                          hist.get("homem", [])[-3:], rng))
    mulher = (_por_id(MULHERES, travas["mulher"]) if travas.get("mulher")
              else _fresco(MULHERES, hist.get("mulher", [])[-4:], rng))

    # ⭐⭐ MODO FORTE — e AQUI ELE DIVERGE DO CONTRATO COMPARTILHADO, DE
    # PROPOSITO E COM O MOTIVO ESCRITO.
    # ⛔⛔ O `sc.ref_forte` devolve uma PESSOA INTEIRA (cabeca, marca, idade,
    # corpo). Nos outros motores isso e' o certo. Aqui seria a destruicao do
    # eixo que o operador acabou de pedir: o toggle NASCE LIGADO, entao o
    # arquetipo regional so' apareceria com o botao desligado — o pool novo
    # seria invisivel no estado padrao do app. Forma sem funcao, e silenciosa.
    # ⭐ Entao o modo pega do helper SO' O QUE ELE VEIO MOVER: a IDADE e o
    # CORPO. O ROSTO E O CABELO CONTINUAM SENDO OS DA REGIAO.
    # ⚠️ E isso e' fiel a' ordem original do operador sobre o toggle
    # (*"n quis manter os tiozao forte?"*): ele nunca pediu para TROCAR o homem,
    # pediu para o homem ficar FORTE.
    # ⛔⛔ A GUARDA AQUI OLHA O FORMATO DE `travas["homem"]`, E ISSO NAO E'
    # DETALHE — E' A CORRECAO DE UM ERRO MEU DE 2026-08-13.
    #
    # A guarda antiga era `and not travas.get("homem")`: qualquer homem travado
    # matava o FORTE. Eu a removi inteira, com a justificativa de que ela ficara
    # obsoleta — o FORTE hoje troca so' o CORPO, mantendo o rosto da regiao,
    # entao homem escolhido e corpo forte deixaram de ser incompativeis. Isso e'
    # verdade para o DROPDOWN, e so' para ele.
    #
    # ⚠️ O que eu nao verifiquei: `travas["homem"]` tem DOIS formatos (esta' no
    # docstring do `_por_id`, logo acima). O dropdown manda um ID (string) fresco
    # do pool — reaplicar o FORTE nele e' idempotente. O CADEADO manda o
    # DICIONARIO JA' RESOLVIDO do sorteio anterior, que JA' passou por aqui. Sem
    # guarda nenhuma o FORTE se reaplica sobre si mesmo a cada SORTEAR, e as
    # duas consequencias foram medidas:
    #   (a) `sc.ref_forte` re-sorteia IDADE e CORPO toda vez — o cadeado, cujo
    #       contrato e' congelar o que esta' na tela, parou de congelar
    #       (idades 67, 70, 72, 68, 68, 72 em seis cliques seguidos);
    #   (b) o `id` acumula o sufixo sem limite —
    #       `texano_prata_forte_forte_forte_forte...` — e e' ESSA string que o
    #       `_anotar` grava no ledger, onde ela nunca mais casa com o pool.
    #
    # ⭐ A licao vale mais que o conserto: eu medi o caminho novo (o menu),
    # declarei a guarda obsoleta, e nao medi o OUTRO chamador da mesma chave.
    # Verificar a funcao num caminho nao autoriza conclusao sobre o outro.
    forte = bool(travas.get("forte")) and not isinstance(travas.get("homem"), dict)
    if forte:
        _f = sc.ref_forte(MOLDE_H, rng, idade_min=FORTE_IDADE_MIN,
                          maduros=True)
        homem = dict(homem, idade=_f["idade"], corpo=_f["corpo"],
                     id="%s_forte" % homem["id"])

    # ⭐⭐ MODO BELA — o espelho, do outro lado.
    # ⛔ E A ETNIA DELA SOBREVIVE AO MODO (licao do GOOD 16).
    bela = bool(travas.get("bela")) and not travas.get("mulher")
    if bela:
        _et_dela = mulher["etnia"]
        mulher = sc.ref_bela(MULHERES[0], rng)
        mulher["etnia"] = _et_dela

    cor = (_por_id(CORES, travas["cor"]) if travas.get("cor")
           else _fresco(CORES, hist.get("cor", [])[-3:], rng))
    prato = (_por_id(PRATOS, travas["prato"]) if travas.get("prato")
             else _fresco(PRATOS, hist.get("prato", [])[-3:], rng))
    jarra = (_por_id(JARRAS, travas["jarra"]) if travas.get("jarra")
             else rng.choice(JARRAS))

    # ⛔ A POLO NUNCA REPETE A COR DA GELATINA (lente PR4b): homem de polo azul
    # segurando cubo azul apaga o prop, e o prop e' o video.
    polos = [p for p in POLOS if cor["cubo"].split()[-1] not in p] or POLOS

    spec = {
        "pagina": pagina, "etnia": etnia, "bela": bela, "forte": forte,
        "mundo": mundo, "homem": homem, "mulher": mulher,
        "cor": cor, "prato": prato, "jarra": jarra,
        "polo": rng.choice(polos),
        # ⭐ Com o MODO FORTE ligado o corpo vem DO HELPER, junto do rosto e da
        # idade: sortear um corpo do pool velho por cima do homem forte seria
        # colar um tronco de um rosto noutro.
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

# ⛔ ANTICELEB — nunca INVENTAR declaracao de conformidade. ⚠️ Esta frase existe
# porque o BLOCO 0 do repo inteiro a carrega e o gerador a espera; o que se
# proibe e' escrever uma nova.
# ⭐ Com o MODO FORTE ligado ela vira `sc.ANTICELEB_FORTE`: dizer "powerfully
# built" no corpo e "plain unremarkable face" no rosto na mesma frase e' a
# contradicao que o CLEAN ja' pagou.
# ⛔ A negacao anti-celebridade saiu daqui em 2026-08-14, por ordem do operador
# (*"tire not a celebrity do prompt"*): declaracao INJETA o token que ela nega.
# A metade positiva ficou. Ver CLAUDE.md §"CONTRA A CELEBRIDADE, SILENCIO".
ANTICELEB = ("An ordinary everyday relatable person with a plain unremarkable "
             "face.")


def _traje_dela(spec):
    """A roupa dela, ja' resolvida pelo MODO BELA.

    ⛔ Um lugar so'. Espalhar `if spec["bela"]` pelo bloco e' o fragmento
    espelhado que diverge na primeira manutencao.
    """
    m = spec["mundo"]
    return m["dela_bela"] if spec.get("bela") else m["dela"]


def _bancada(spec):
    """Os tres props da receita na bancada, na MESMA ordem nos dois quadros.

    ⛔ Um lugar so', e a ordem e' parte da continuidade: caixa de gelatina,
    caixa de bicarbonato, limao. Trocar a ordem entre os quadros faz o gerador
    reposicionar tudo, e o espectador le' outra bancada.
    """
    return "%s, %s and %s" % (spec["cor"]["caixa"], CAIXA_BICARBONATO, LIMAO)


def montar(spec):
    m, h, w = spec["mundo"], spec["homem"], spec["mulher"]
    c = spec["cor"]
    et = spec["etnia"]
    b = {}

    # --- BLOCO 0 — a REF e' o HOMEM (ele e' quem fala) ---------------------
    b["BLOCO 0 (REF)"] = (
        "REF 01: Photo of a real person, a %d-year-old %s man, chest up, "
        "facing the camera directly, calm steady expression. %s, %s, %s, "
        "wearing %s and a gold wedding band. %s Hands out of frame, no "
        "objects. Plain neutral gray background, soft even frontal light. "
        "Slight sensor grain, soft focus, raw iPhone front camera aesthetic. "
        "No subtitles, no captions, no burned-in text, no watermark."
        % (h["idade"], et, _cap(h["cabeca"]), h["marca"], spec["corpo_h"],
           spec["polo"],
           sc.ANTICELEB_FORTE if spec.get("forte") else ANTICELEB))

    # --- IMAGE 01 — O PRATO ERGUIDO ---------------------------------------
    # ⛔ ELE ESTA' SOZINHO AQUI (decisao 4). A esposa nao existe neste quadro, e
    # a frase `He is the only person in the frame` e' obrigatoria: sem ela o Veo
    # povoa cozinha de fora com figurante, que e' o comportamento default dele
    # em cenario de quintal.
    # ⛔ O COPO NAO ENTRA (lente PR1): mostrar o payoff no hook entrega o fim
    # antes da promessa. O que existe aqui e' o PRATO e a COLHER.
    # ⚠️ A boca aberta e' a cara da fonte, e ela e' descrita como ESPANTO, nunca
    # como grito: `mouth open` sozinho rendeu bocarra deformada no repertorio.
    b["IMAGE 01/02"] = (
        "IMAGE 01/02: Medium shot at %s. Standing behind %s and filmed from "
        "the waist up is a %d-year-old %s man, %s, %s, %s, wearing %s and a "
        "gold wedding band, talking straight to camera with his eyes wide and "
        "his mouth open mid-word in delight. In his left hand, held up at "
        "chest height, is %s piled with cut cubes of %s gelatin, and his right "
        "hand holds a metal spoon up beside his face with a single %s cube "
        "resting on it. Along the near edge of %s, in front of him, sit %s. He "
        "is the only person in the frame. %s. %s"
        % (m["cen"], m["bancada"], h["idade"], et, h["cabeca"], h["marca"],
           spec["corpo_h"], spec["polo"], spec["prato"]["img"], c["cubo"],
           c["cubo"], m["bancada"], _bancada(spec), _cap(m["luz"]), CAUDA))

    # --- IMAGE 02 — O PREPARO + O COPO ESTENDIDO --------------------------
    # ⛔⛔ A ANCORA DE CONTINUIDADE VEM EM CINCO PECAS: idade, etnia, cabeca,
    # marca e a frase `It is the same man`. Sem isso o Veo desenha OUTRA pessoa
    # — no VAZAMENTO o corpo-prova voltou como um senhor de oculos e bigode, e
    # como o TAKE diz `Only he speaks`, o ESTRANHO falava a fala do REF.
    # ⭐ E aqui a ancora carrega peso DOBRADO: a esposa aparece do nada neste
    # quadro (decisao 4 do operador), entao quem prova que e' o mesmo video e'
    # ele mais a bancada, a mesma cor e os mesmos tres props.
    # ⛔ O PRATO NAO VOLTA (lente PR1): o prato e' o hook, o copo e' o payoff.
    b["IMAGE 02/02"] = (
        "IMAGE 02/02: Medium shot at %s. Standing behind %s is the same "
        "%d-year-old %s man from the first scene, %s, %s, %s, wearing %s and a "
        "gold wedding band, his arm stretched out towards the lens. It is the "
        "same man, not a different person. In his outstretched hand, large and "
        "close in the front of the picture, is a clear glass tumbler filled to "
        "the top with %s liquid. His other hand rests on the handle of %s "
        "standing on %s, half full of the same %s liquid. Along the near edge "
        "sit %s. Pressed against his side with her shoulder against his arm is "
        "a %d-year-old %s woman, %s, %s, %s, wearing %s; she is looking at the "
        "glass and says nothing. They are the only two people in the frame. "
        "%s. %s"
        % (m["cen"], m["bancada"], h["idade"], et, h["cabeca"], h["marca"],
           spec["corpo_h"], spec["polo"], c["liquido"], spec["jarra"]["img"],
           m["bancada"], c["liquido"], _bancada(spec),
           w["idade"], w["etnia"], w["cabeca"], w["marca"], w["porte"],
           _traje_dela(spec), _cap(m["luz"]), CAUDA))

    # --- OS TAKES ----------------------------------------------------------
    # ⛔ `Only he speaks` e `she never speaks` sao OBRIGATORIOS (lente PR2):
    # omitir nao basta, o Veo poe as duas bocas a mexer se ninguem proibir.
    b["TAKE 01/02"] = (
        "TAKE 01/02: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway, no cuts, and the camera does not move. He "
        # ⛔⛔ A SUPERFICIE E' SLOT, NUNCA O LITERAL `counter`. A primeira versao
        # deste bloco dizia `nothing on the counter is touched` — e ha' mundo
        # cuja bancada e' `the dark granite ISLAND TOP` e mundo cuja bancada e'
        # `the wet cedar counter BOARDS`. E' o mesmo defeito que o autoteste do
        # PLACA 16 pegou em 43 de 600 seeds, cometido de novo aqui e pego no
        # primeiro render lido a olho, nao por lente.
        "talks straight into the lens the whole time and both hands stay "
        "exactly where they are, the platter held up and the spoon beside his "
        "face. The cube on the spoon does not fall and nothing on %s is "
        "touched, moved or lifted. He stays the only person in the frame "
        "and nothing else changes.\n"
        "Dialogue: \"%s\"\nAudio: %s. No music."
        % (m["bancada"], sonorizar(spec["falas"][0]), m["audio"]))

    # ⛔⛔ E O GOLE NAO ENTRA — decisao 6 do operador, escrita como PROIBICAO no
    # bloco e cobrada pela lente PR7. Sem a frase o Veo termina o gesto: mao
    # esticada segurando um copo cheio, num plano de 8 segundos, resolve
    # sozinha em beber — e a mao subindo passa por cima da sentenca do CTA.
    b["TAKE 02/02"] = (
        "TAKE 02/02: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway, no cuts, and the camera does not move. He "
        "talks straight into the lens the whole time and it is the same man as "
        "in the first scene. He holds the glass out towards the lens for the "
        "whole shot and never brings it to his mouth, never drinks from it and "
        "never sets it down. His other hand stays on the jug. She stays "
        "pressed against his side looking at the glass, and she never speaks. "
        "Only he speaks. Nothing else in the frame changes.\n"
        "Dialogue: \"%s\"\nAudio: %s. No music."
        % (sonorizar(spec["falas"][1]), m["audio"]))

    return sc.selar_takes(b)


# ===========================================================================
# LINTER — as regras PR
# ===========================================================================

def _pr1_prato_e_copo(spec, blocos, achados):
    """⭐⭐ PR1 — O PRATO E' DO HOOK, O COPO E' DO PAYOFF.

    ⛔ Os dois defeitos sao opostos e igualmente caros: copo na cena 1 entrega
    o fim antes da promessa; prato na cena 2 diz que nada aconteceu entre os
    quadros. E' a unica mudanca de estado que este angulo tem — a fonte inteira
    e' um take so', e o que faz o corte existir e' o prato virar copo.
    """
    i1, i2 = blocos["IMAGE 01/02"], blocos["IMAGE 02/02"]
    if "tumbler" in i1 or "glass tumbler" in i1:
        achados.append(("ERRO", "PR1: o copo aparece na cena 1 — e' o payoff, e "
                                "mostrado antes da promessa ele nao paga nada"))
    if spec["prato"]["img"] in i2 or "platter" in i2:
        achados.append(("ERRO", "PR1: o prato volta na cena 2 — o prato e' o "
                                "hook e o copo e' o payoff; os dois no mesmo "
                                "video dizem que nada mudou no corte"))
    if spec["prato"]["img"] not in i1:
        achados.append(("ERRO", "PR1: a cena 1 nao tem o prato sorteado (%r)"
                        % spec["prato"]["curto"]))
    if "tumbler" not in i2:
        achados.append(("ERRO", "PR1: a cena 2 nao tem o copo — e' o objeto "
                                "que fecha o video"))


def _pr2_ela_so_no_take2(spec, blocos, achados):
    """PR2 — ela NAO existe no quadro 1, existe no 2, e e' MUDA nos dois.

    ⛔ Decisao 4 do operador. A lente cobra os DOIS lados: mulher vazando para o
    hook mata a solidao que faz o testemunho funcionar, e mulher ausente do
    payoff apaga a decisao inteira.
    """
    i1, i2 = blocos["IMAGE 01/02"], blocos["IMAGE 02/02"]
    if "woman" in i1:
        achados.append(("ERRO", "PR2: ha' uma mulher na cena 1 — o hook e' "
                                "SOLO, e a chegada dela no quadro 2 e' o "
                                "payoff"))
    if "He is the only person in the frame" not in i1:
        achados.append(("ERRO", "PR2: a cena 1 nao declara que ele esta' "
                                "sozinho — cozinha de quintal sem a clausula "
                                "vem com figurante de brinde"))
    if "woman" not in i2:
        achados.append(("ERRO", "PR2: a cena 2 nao tem a esposa"))
    # ⛔ `Only he speaks` SO' FAZ SENTIDO NO TAKE 02, e a primeira versao desta
    # lente o cobrava nos dois — 400 de 400 sorteios reprovados por uma lente
    # que pedia a proibicao de uma segunda boca num quadro com uma pessoa so'.
    # ⭐ O que o TAKE 01 precisa e' do oposto: a declaracao de que ele esta'
    # SOZINHO, que e' o que impede o gerador de povoar o quintal.
    if "the only person in the frame" not in blocos["TAKE 01/02"]:
        achados.append(("ERRO", "PR2: o TAKE 01 nao declara que ele segue "
                                "sozinho — a IMAGE dizer nao basta, o TAKE e' "
                                "quem governa o que se mexe"))
    if "Only he speaks" not in blocos["TAKE 02/02"]:
        achados.append(("ERRO", "PR2: o TAKE 02 sem `Only he speaks`"))
    if "she never speaks" not in blocos["TAKE 02/02"]:
        achados.append(("ERRO", "PR2: o TAKE 02 nao diz que ela e' muda — a "
                                "mudez dela e' invariante do angulo"))


def _pr3_continuidade(spec, blocos, achados):
    """PR3 — as CINCO pecas da ancora do mesmo homem."""
    h, i2 = spec["homem"], blocos["IMAGE 02/02"]
    if "It is the same man, not a different person." not in i2:
        achados.append(("ERRO", "PR3: a cena 2 nao declara que e' o mesmo "
                                "homem — sem a frase o Veo desenha outro, e o "
                                "TAKE manda o estranho falar a fala do REF"))
    for campo in ("cabeca", "marca"):
        if h[campo] not in i2:
            achados.append(("ERRO", "PR3: a cena 2 sem o %s dele (%r)"
                            % (campo, h[campo][:34])))
    if "%d-year-old %s man" % (h["idade"], spec["etnia"]) not in i2:
        achados.append(("ERRO", "PR3: a cena 2 sem a idade/etnia dele"))


def _pr4_cor_unica(spec, blocos, achados):
    """⭐⭐ PR4 — UMA COR SO', NOS TRES OBJETOS E NOS DOIS QUADROS.

    ⛔ O cubo do prato, o liquido do copo e a caixa da bancada sao a MESMA cor.
    O espectador acabou de ver o cubo entrar; cubo verde virando bebida roxa e'
    a incoerencia que ele perdoa menos num video de 16 segundos.
    """
    c = spec["cor"]
    if c["cubo"] not in blocos["IMAGE 01/02"]:
        achados.append(("ERRO", "PR4: a cor sorteada (%s) nao chega aos cubos "
                                "da cena 1" % c["curto"]))
    if c["liquido"] not in blocos["IMAGE 02/02"]:
        achados.append(("ERRO", "PR4: a cor sorteada (%s) nao chega ao liquido "
                                "da cena 2" % c["curto"]))
    for k in ("IMAGE 01/02", "IMAGE 02/02"):
        if c["caixa"] not in blocos[k]:
            achados.append(("ERRO", "PR4: %s sem a caixa de gelatina na cor "
                                    "sorteada" % k))
    # ⛔ PR4b — a polo nunca repete a cor da gelatina.
    if c["cubo"].split()[-1] in spec["polo"]:
        achados.append(("ERRO", "PR4b: a polo (%r) e a gelatina (%s) sao da "
                                "mesma cor — o prop desaparece contra o peito "
                                "dele" % (spec["polo"], c["curto"])))


def _pr5_orcamento(spec, blocos, achados):
    for i, fala in enumerate(spec["falas"], 1):
        n = _palavras(fala)
        if n > TETO_FALA[i]:
            achados.append(("ERRO", "PR5: cena %d com %d palavras (teto %d) — "
                                    "a fala e' cortada no render"
                            % (i, n, TETO_FALA[i])))
        if n < PISO_FALA[i]:
            achados.append(("AVISO", "PR5: cena %d com %d palavras (piso %d) — "
                                     "sobra ar morto no take"
                            % (i, n, PISO_FALA[i])))


def _pr6_etnia(spec, blocos, achados):
    """PR6 — a congruencia governa O HOMEM, que e' quem fala, e o MUNDO."""
    et = spec["etnia"]
    for k in ("BLOCO 0 (REF)", "IMAGE 01/02", "IMAGE 02/02"):
        if et not in blocos[k]:
            achados.append(("ERRO", "PR6: %s sem a etnia da pagina (%r)"
                            % (k, et)))
    if et not in spec["mundo"]["etnias"]:
        achados.append(("ERRO", "PR6: o mundo %r nao comporta a etnia da "
                                "pagina (%r) — o arquetipo regional arrasta o "
                                "quintal inteiro, nao so' o fundo"
                        % (spec["mundo"]["id"], et)))


def _pr7_sem_gole(spec, blocos, achados):
    """⛔⛔ PR7 — O GOLE NAO ENTRA. Decisao 6 do operador.

    ⚠️ A proibicao e' POSITIVA no bloco (`never brings it to his mouth`) e a
    lente cobra a frase, nao a ausencia de `drink`: mao esticada segurando copo
    cheio, num plano de 8 segundos, resolve sozinha em beber se ninguem
    proibir — e a mao subindo passa por cima da sentenca do CTA.
    """
    t2 = blocos["TAKE 02/02"]
    if "never brings it to his mouth" not in t2:
        achados.append(("ERRO", "PR7: o TAKE 02 nao proibe o gole — o operador "
                                "cortou o gole da fonte, e sem a clausula o "
                                "gerador o traz de volta"))
    if "holds the glass out towards the lens" not in t2:
        achados.append(("ERRO", "PR7: o TAKE 02 nao manda estender o copo — e' "
                                "o ultimo frame escolhido pelo operador"))


def _pr_orgao(spec, blocos, achados):
    """⭐⭐ PR-ORGAO — a fala NUNCA nomeia o orgao, e o motivo e' engenharia.

    A copy deste angulo carrega verbo de ereccao em PRIMEIRA PESSOA (`I am rock
    hard`), que e' a formula da fonte e passa no gerador. Nomear o orgao na
    mesma fala reconstruiria o par `verbo + orgao` que o COLO 16 pagou com ~95%
    de recusa — e aqui bastaria UMA entrada de pool para reintroduzi-lo.
    """
    for i, fala in enumerate(spec["falas"], 1):
        achou = sorted({t for t in NUCLEO if t.lower() in fala.lower()})
        if achou:
            achados.append((
                "ERRO",
                "PR-ORGAO: o take %d nomeia o orgao (%s) — esta copy carrega "
                "verbo de ereccao em primeira pessoa, e o par verbo+orgao e' "
                "o que reprova no gerador (COLO 16, ~95%%)" % (i, achou)))


def _pr8_receita_na_fala(spec, blocos, achados):
    """⛔⛔ PR8 — OS TRES INGREDIENTES ESTAO NA FALA DO TAKE 1.

    ⚠️ Esta lente cobra o CONTRARIO do CT5, e de proposito: o operador furou o
    CT5 neste angulo por decisao declarada (2026-08-12). Sem a lente, uma
    entrada de pool escrita amanha sem os tres passaria — e o ANGULO teria
    perdido calado a coisa que o operador escolheu contra a doutrina.
    ⭐ Lente que cobra uma EXCECAO e' o que impede a excecao de virar erosao.
    """
    f1 = spec["falas"][0].lower()
    faltam = [n for n in ("gelatin", "lemon", "baking soda") if n not in f1]
    if faltam:
        achados.append(("ERRO", "PR8: a fala do take 1 nao nomeia %s — o CT5 "
                                "foi furado neste angulo POR DECISAO, e a "
                                "receita dita e' o que o operador escolheu"
                        % faltam))
    # ⛔ E o quadro paga o que a boca diz: os tres tem de estar na bancada.
    for k in ("IMAGE 01/02", "IMAGE 02/02"):
        if CAIXA_BICARBONATO not in blocos[k] or LIMAO not in blocos[k]:
            achados.append(("ERRO", "PR8: %s sem os props da receita na "
                                    "bancada — a fala os nomeia, e prop "
                                    "nomeado fora do quadro e' contradicao" % k))


def _pr9_modos(spec, blocos, achados):
    """⭐⭐ PR9 — OS DOIS TOGGLES TEM DE CHEGAR AO QUADRO, NOS DOIS ESTADOS.

    ⛔ E' a lente contra a FORMA-SEM-FUNCAO: botao aceso, sorteio igual.
    ⚠️ O que ela cobra DELA so' existe na IMAGE 02 — a esposa nao entra no
    quadro 1 neste angulo, e uma lente que a procurasse nos dois reprovaria a
    producao certa em 100% dos sorteios.
    """
    w, h = spec["mulher"], spec["homem"]
    i2 = blocos["IMAGE 02/02"]
    if "%d-year-old %s woman" % (w["idade"], w["etnia"]) not in i2:
        achados.append(("ERRO", "PR9: a cena 2 sem a idade/etnia sorteadas "
                                "dela (%d, %r) — a idade e' a primeira coisa "
                                "que o modo BELA move" % (w["idade"],
                                                          w["etnia"])))
    for campo in ("porte", "cabeca", "marca"):
        if w[campo] not in i2:
            achados.append(("ERRO", "PR9: a cena 2 sem o %s dela (%r)"
                            % (campo, w[campo][:34])))
    if _traje_dela(spec) not in i2:
        achados.append(("ERRO", "PR9: a cena 2 sem o traje do estado atual do "
                                "modo BELA (%r)" % _traje_dela(spec)))
    for k in ("IMAGE 01/02", "IMAGE 02/02"):
        for campo in ("cabeca", "marca"):
            if h[campo] not in blocos[k]:
                achados.append(("ERRO", "PR9: %s sem o %s dele (%r) — e' o que "
                                        "o modo FORTE move"
                                % (k, campo, h[campo][:34])))
        if spec["corpo_h"] not in blocos[k]:
            achados.append(("ERRO", "PR9: %s sem o corpo dele" % k))
    if spec.get("forte") and spec["corpo_h"] != spec["homem"].get("corpo"):
        achados.append(("ERRO", "PR9: modo FORTE ligado e o corpo em quadro "
                                "nao e' o do homem forte sorteado"))


def _pr11_bancada(spec, blocos, achados):
    """⛔⛔ PR11 — A SUPERFICIE E' SLOT EM TODO BLOCO QUE A CITA.

    ⚠️ Esta lente nasce de um erro MEU, cometido nesta mesma construcao e pego
    lendo um render a olho, nao por medicao: o TAKE 01 dizia `nothing on the
    counter is touched` com o literal cravado. Ha' mundo cuja bancada e' `the
    dark granite ISLAND TOP` e mundo cuja bancada e' `the wet cedar counter
    BOARDS` — nos dois, `the counter` aponta para um objeto que o quadro nao
    nomeia, e o gerador escolhe qual superficie obedecer.
    ⭐ E' o MESMO defeito que o autoteste do PLACA 16 pegou em 43 de 600 seeds
    em 2026-08-12. Repetir um erro catalogado no mesmo dia e' o argumento para
    a lente existir aqui em vez de virar so' um comentario.
    """
    b = spec["mundo"]["bancada"]
    for k in ("IMAGE 01/02", "IMAGE 02/02", "TAKE 01/02"):
        if b not in blocos[k]:
            achados.append(("ERRO", "PR11: %s nao usa a bancada do mundo "
                                    "sorteado (%r) — superficie cravada aponta "
                                    "para o que o quadro nao tem" % (k, b)))


def _pr10_contrato16(spec, blocos, achados):
    """As travas do CONTRATO DE COPY 16s, cobradas de dentro do motor.

    ⛔⛔ DUAS SAO FILTRADAS, E AS DUAS SAO DECISAO DECLARADA DO OPERADOR
    (2026-08-12). Deixar qualquer uma entrar seria centenas de alarmes por
    autoteste em cima de uma copy que o operador escolheu — e alarme que sempre
    dispara ensina a ignorar o linter inteiro, que e' o defeito mais caro que
    uma lente pode ter.

      CT2  este take 1 nao enuncia FALHA: e' TESTEMUNHO DE DESCOBERTA. Mesma
           familia da excecao do GOOD 16 e do ALFA 16.
      CT5  a fala NOMEIA os tres ingredientes. E' a decisao 2, e o motor cobra
           o contrario dela na `PR8`.

    ⚠️ O `medir_copy16`, que mede DE FORA, continua CONTANDO as duas — e a
    decisao aparece rotulada no rodape pelo mecanismo `DESLIGADAS`. O numero
    nunca some; o que muda e' que ele para de ser chamado de defeito.
    """
    brutos = []
    sc.lint_copy16(sys.modules[__name__], spec, brutos, isca_absurda=False)
    achados.extend([(n, msg) for n, msg in brutos
                    if not msg.startswith(("CT2:", "CT5:"))])


def lint(spec, blocos):
    """⚠️ Lint PROPRIO, nao `sc.lint_curto`: aquele e' da maquinaria de colapso
    5->3 e pede `base` e `mapa`, que este motor nao tem — ele nao deriva de
    motor longo nenhum."""
    ach = []
    falas = spec["falas"]
    sc.lint_tags(blocos, ach)
    sc.lint_sem_texto(blocos, ach)
    sc.lint_isca_cta(falas[1], ach, "a cena 2 (CTA)")
    sc.lint_cta_literal(falas[1], ach, "a cena 2 (CTA)")
    sc.lint_take_vs_image(blocos, ach)
    # ⛔⛔ A negacao anti-celebridade nunca volta ao texto montado
    # (2026-08-14, ordem do operador). Este motor tem `lint()` PROPRIO e
    # nao passa pelo `sc.lint_curto`, entao a lente entra aqui
    # explicitamente — regra sem guarda volta no proximo agente nascido
    # por copia, e foi exatamente assim que a clausula chegou aos 30
    # motores.
    sc.lint_anticeleb(blocos, ach)
    sc.lint_painel_honesto(sys.modules[__name__], spec, blocos, ach)
    for f in (_pr1_prato_e_copo, _pr2_ela_so_no_take2, _pr3_continuidade,
              _pr4_cor_unica, _pr5_orcamento, _pr6_etnia, _pr7_sem_gole,
              _pr_orgao, _pr8_receita_na_fala, _pr9_modos, _pr11_bancada,
              _pr10_contrato16):
        f(spec, blocos, ach)
    return ach


# ===========================================================================
# PAINEL
# ===========================================================================

EIXOS_UI = [
    ("mundo", "A REGIAO", "MUNDOS", "regiao"),
    ("homem", "QUEM FALA", "HOMENS", "id"),
    ("mulher", "A ESPOSA", "MULHERES", "id"),
    ("cor", "A COR", "CORES", "curto"),
    ("prato", "O PRATO", "PRATOS", "curto"),
    ("jarra", "A JARRA", "JARRAS", "curto"),
]

EIXOS_TRAVAVEIS = ["mundo", "homem", "mulher", "cor", "prato", "jarra"]

TRAVAS_UI = [("familia_mundo", "regiao", ["livre"] + FAMILIAS_MUNDO)]

# ⭐⭐ O DROPDOWN DE QUEM FALA — e' ELE que da' FUNCAO ao campo `rotulo`.
# ⛔ Sem esta linha os 22 rotulos seriam comentario caro: escritos, medidos e
# travados, e nenhum olho humano os veria. Forma sem funcao e' o defeito que
# este repo mais paga (licoes-de-construcao §41), e label que nao aparece na
# tela e' a versao mais barata dele.
# ⛔ POR QUE DROPDOWN E NAO `TRAVAS_UI`: a barra de travas desenha UM BOTAO POR
# OPCAO, lado a lado. Serve para as familias de regiao; com 22 homens ela
# estoura a largura da janela. Contrato aditivo do `ui_agente` (2026-08-13).
# ⚠️ O ROTULO DA TELA E' O MESMO DO `EIXOS_UI` ("QUEM FALA") de proposito: sao o
# mesmo eixo, e dois nomes para o mesmo eixo fazem o operador procurar um
# controle que nao existe.
# ⚠️ E o campo exibido e' `rotulo`, NAO `id`: o `ui_agente` monta o mapa
# texto -> id, entao ele escolhe "68y · careca + bigode de morsa + oculos" e o
# motor recebe `florida_morsa`. Um menu de ids obrigaria a abrir o codigo para
# saber o que se escolheu. ⚠️ O `EIXOS_UI` acima continua com `id` porque la' o
# `_texto_eixo` ja' prefixa a idade (`"%dy · %s"`) — trocar para `rotulo`
# imprimiria "67y · 67y · grisalho curto...". Dois lugares, dois campos.
# ⛔ O DROPDOWN GANHA DA FAMILIA DO MUNDO. O `homens_da_familia` so' e'
# consultado quando `travas["homem"]` esta' vazio; escolher aqui e' escolha
# EXPLICITA, e escolha explicita vence filtro automatico — o mesmo precedente do
# `or` que faz a familia travada ceder no `sortear`.
DROPDOWNS_UI = [("homem", "QUEM FALA", "HOMENS", "rotulo")]

# ⚠️ `mundo` entra na lista de ignorados do `lint_painel_honesto` porque o valor
# do eixo e' um id interno; os outros chegam ao quadro pelo `img`/`cabeca`/
# `marca` deles, e a lente cobra isso a cada sorteio.
IGNORA_PAINEL = ("mundo",)

# ⛔ Nenhum eixo do painel mexe na copy: a fala nao cita o quintal, a cor, o
# prato, a jarra nem as pessoas. Declarar o dicionario vazio e' declarar que
# alguem verificou, em vez de deixar o `getattr` decidir por omissao.
EIXOS_QUE_MEXEM_NA_COPY = {}


def resumo_pt(spec):
    """⚠️ Texto de PAINEL, nao copy falada — mas e' o unico lugar onde o
    operador le' o video ANTES de gastar credito gerando."""
    m = spec["mundo"]
    # ⚠️ A polo entra entre PARENTESES, como a agua do BED 16: string inglesa
    # crua emendada na frase portuguesa ("homem de a tan polo shirt") faz o
    # operador parar de ler o resumo — e o resumo e' o unico lugar onde ele ve'
    # o video antes de gastar credito.
    return ("16s, DOIS takes, regiao: %s. Take 1 — O PRATO: homem %s de %d "
            "anos (%s), SOZINHO atras da bancada da cozinha de fora, "
            "segurando o prato de %s cheio de cubos de gelatina %s e a colher "
            "com UM cubo ao lado do rosto, olhos arregalados; na bancada a "
            "caixa de gelatina, o bicarbonato e o limao. A fala diz a "
            "descoberta e NOMEIA os tres ingredientes. Take 2 — O PREPARO: o "
            "MESMO homem, o copo de liquido %s ESTENDIDO na lente, a mao na "
            "%s; a esposa %s de %d anos aparece colada nele, MUDA, olhando o "
            "copo. Fecha no CTA, e ele NAO bebe. Modo FORTE %s, modo BELA %s."
            % (m["regiao"], spec["etnia"], spec["homem"]["idade"],
               spec["polo"], spec["prato"]["curto"], spec["cor"]["curto"],
               spec["cor"]["curto"], spec["jarra"]["curto"],
               spec["mulher"]["etnia"], spec["mulher"]["idade"],
               "LIGADO" if spec.get("forte") else "desligado",
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
    cores = collections.Counter()
    falhas, avisos = [], 0
    # ⭐⭐ OS QUATRO ESTADOS DOS DOIS MODOS, MEDIDOS JUNTOS. Medir so' o default
    # e' medir um quarto do agente: cada toggle troca um elenco inteiro, e um
    # KeyError do lado ligado morreria CALADO dentro do callback do tkinter.
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
        cores[s["cor"]["id"]] += 1
        for c, f in enumerate(s["falas"], 1):
            dist[c].add(f)
            tam[c].append(_palavras(f))
        for nivel, msg in lint(s, montar(s)):
            if nivel == "ERRO":
                erros[msg[:70]] += 1
            else:
                avisos += 1

    print("PRATO 16 — %d sorteios (os QUATRO estados de bela x forte)" % n)
    for c in sorted(dist):
        v = sorted(tam[c])
        print("  cena %d: %d falas distintas · palavras min/med/max %d/%d/%d"
              % (c, len(dist[c]), v[0], v[len(v) // 2], v[-1]))
    print("  mundos: %d de %d · cores: %d de %d"
          % (len(mundos), len(MUNDOS), len(cores), len(CORES)))
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
    # ⛔⛔ E O FORTE TEM DE FICAR ACIMA DE 60. Ordem do operador de 2026-08-12,
    # a segunda e mais especifica: *"sempre que travar a referencia de forte
    # mantenha o homem acima de 60 anos no prompt"*.
    # ⚠️ A lente existe porque o `sc.ref_forte` CEDE em silencio quando nada
    # cabe na faixa (`or _pool`): pedir 61 num pool que nao os tenha devolveria
    # um rapaz sem erro nenhum. Sem alguem cobrando a faixa DEPOIS do sorteio, o
    # defeito volta calado — e essa razao vale qualquer que seja o numero.
    _fortes = estados[(False, True)]["idade_dele"] | estados[(True, True)]["idade_dele"]
    if min(_fortes) <= 60:
        falhas.append("MODO FORTE: homem de %d anos com o botao aceso — o piso "
                      "de %d cedeu (o helper devolve o pool inteiro quando nada "
                      "cabe na faixa)" % (min(_fortes), FORTE_IDADE_MIN))

    # ⛔ CONTROLE DE MUNDO E DE COR.
    for et in sorted(set(ETNIA.values())):
        if not [m for m in MUNDOS if et in m["etnias"]]:
            falhas.append("MUNDO: nenhum mundo comporta a etnia %r" % et)
    # ⛔⛔ CADA REGIAO PRECISA DE DUAS OPCOES DE HOMEM. Uma so' e' eixo morto: o
    # painel mostraria `trocar` em QUEM FALA e devolveria sempre o mesmo rosto
    # naquela regiao, que e' o botao que mente — o defeito que este repo ja'
    # pagou tres vezes.
    for _m in MUNDOS:
        _op = homens_da_familia(_m["familia"])
        if len(_op) < 2:
            falhas.append("HOMENS: a familia %r tem %d arquetipo(s) — o botao "
                          "`trocar` de QUEM FALA nao muda nada la'"
                          % (_m["familia"], len(_op)))
    # ⛔⛔ E O ARQUETIPO REGIONAL TEM DE SOBREVIVER AO MODO FORTE. O toggle
    # NASCE LIGADO: se ele trocasse a pessoa inteira, o pool que o operador
    # pediu em 2026-08-12 seria invisivel no estado padrao do app.
    _cabecas = {h["cabeca"] for h in HOMENS}
    for i in range(80):
        _s = sortear(pags[i % len(pags)], random.Random(1000 + i), {},
                     {"forte": True})
        if _s["homem"]["cabeca"] not in _cabecas:
            falhas.append("MODO FORTE: o rosto deixou de ser o do arquetipo "
                          "regional (%r) — o toggle voltou a trocar a PESSOA "
                          "em vez do CORPO" % _s["homem"]["cabeca"][:40])
            break
    for m in MUNDOS:
        if m["dela_bela"] == m["dela"]:
            falhas.append("MUNDO %s: o traje bela e' igual ao normal — o "
                          "toggle nao move nada nesta regiao" % m["id"])
    if len(mundos) < len(MUNDOS):
        falhas.append("MUNDOS: so' %d de %d aparecem em %d sorteios"
                      % (len(mundos), len(MUNDOS), n))
    if len(cores) < len(CORES):
        falhas.append("CORES: so' %d de %d aparecem em %d sorteios"
                      % (len(cores), len(CORES), n))

    # ⭐ [ALCANCE] — entrada que nao cabe com os minimos dos outros beats nunca
    # e' sorteada. Nao e' rara: e' MORTA, e o autoteste a contava como viva.
    for rot, pool, cena, outros in (
            ("DESCOBERTAS", DESCOBERTAS, 1, [RECEITAS]),
            ("RECEITAS", RECEITAS, 1, [DESCOBERTAS]),
            ("PROVAS", PROVAS, 2, [FACILIDADES, CTAS]),
            ("FACILIDADES", FACILIDADES, 2, [PROVAS, CTAS]),
            ("CTAS", CTAS, 2, [PROVAS, FACILIDADES])):
        reserva = sum(_mn(p) for p in outros)
        mortas = [x for x in pool
                  if _palavras(x) + reserva > TETO_FALA[cena]]
        if mortas:
            falhas.append("[ALCANCE] %s: %d de %d nunca sao sorteadas (teto "
                          "real %d palavras): %s"
                          % (rot, len(mortas), len(pool),
                             TETO_FALA[cena] - reserva, mortas[:1]))

    # ⛔⛔ CONTROLE DA EXCECAO DO CT5 — a decisao 2 do operador, cobrada no POOL.
    # Sem isto, uma entrada nova sem os tres ingredientes passaria e o angulo
    # perderia calado a coisa que ele escolheu contra a doutrina.
    for x in RECEITAS:
        faltam = [t for t in ("gelatin", "lemon", "baking soda")
                  if t not in x.lower()]
        if faltam:
            falhas.append("PR8: a entrada %r de RECEITAS nao nomeia %s"
                          % (x, faltam))
    # ⛔ E NENHUM POOL DA CENA 2 REPETE INGREDIENTE: a excecao se gasta uma vez.
    repete = [x for x in PROVAS + FACILIDADES + CTAS
              if any(t in x.lower() for t in ("lemon", "baking soda"))]
    if repete:
        falhas.append("CT5: a cena 2 repete ingrediente (%r) — a excecao do "
                      "take 1 nao se estende ao CTA" % repete[0])

    # ⛔⛔ CONTROLE DO PR-ORGAO — nenhum pool nomeia o orgao, e o motivo e'
    # que esta copy carrega verbo de ereccao em primeira pessoa.
    com_orgao = [x for x in DESCOBERTAS + RECEITAS + PROVAS + FACILIDADES + CTAS
                 if any(t.lower() in x.lower() for t in NUCLEO)]
    if com_orgao:
        falhas.append("PR-ORGAO: %d entrada(s) de pool nomeiam o orgao: %s"
                      % (len(com_orgao), com_orgao[:1]))

    # ⛔ CONTROLE POSITIVO DAS LENTES — lente que nunca acusa e' forma sem
    # funcao, e "sem achado" nela significaria "ninguem olhou".
    s0 = sortear("joe", random.Random(7), {}, {})
    b0 = montar(s0)
    controles = []
    b1 = dict(b0)
    b1["IMAGE 01/02"] += " a clear glass tumbler filled to the top"
    if not any("PR1" in m for _, m in lint(s0, b1)):
        controles.append("[PR1] nao acusa o copo adiantado na cena 1")
    b2 = dict(b0)
    b2["IMAGE 01/02"] += " Beside him is a 30-year-old woman."
    if not any("PR2" in m for _, m in lint(s0, b2)):
        controles.append("[PR2] nao acusa mulher na cena 1")
    b3 = dict(b0)
    b3["IMAGE 02/02"] = b3["IMAGE 02/02"].replace(
        "It is the same man, not a different person. ", "")
    if not any("PR3" in m for _, m in lint(s0, b3)):
        controles.append("[PR3] nao acusa a ancora de continuidade ausente")
    b7 = dict(b0)
    b7["TAKE 02/02"] = b7["TAKE 02/02"].replace(
        "never brings it to his mouth, ", "")
    if not any("PR7" in m for _, m in lint(s0, b7)):
        controles.append("[PR7] nao acusa o gole liberado")
    s8 = dict(s0, falas=list(s0["falas"]))
    s8["falas"][0] = "This was the best discovery I ever made for my marriage."
    if not any("PR8" in m for _, m in lint(s8, b0)):
        controles.append("[PR8] nao acusa a fala sem os tres ingredientes")
    s9 = dict(s0, falas=list(s0["falas"]))
    s9["falas"][1] = s9["falas"][1].replace("I am", "My pecker is", 1)
    if not any("PR-ORGAO" in m for _, m in lint(s9, b0)):
        controles.append("[PR-ORGAO] nao acusa o orgao na fala")
    b11 = dict(b0)
    b11["TAKE 01/02"] = b11["TAKE 01/02"].replace(
        s0["mundo"]["bancada"], "the counter")
    if not any("PR11" in m for _, m in lint(s0, b11)):
        controles.append("[PR11] nao acusa a superficie cravada no TAKE")
    if controles:
        print("\n>> O AUTOTESTE ESTA' CEGO:")
        for c in controles:
            print("   " + c)
        falhas.extend(controles)


    # ⛔⛔ O CONTRATO DO `rotulo` — as quatro coisas que o dropdown do painel
    # exige, cobradas do DADO e nao da intencao de quem escreveu o pool.
    # ⚠️ A UNICIDADE nao e' capricho: o `ui_agente._barra_dropdowns` monta o
    # mapa com `if txt and txt not in mapa`, entao dois rotulos iguais fazem a
    # SEGUNDA entrada sumir do menu — em silencio, sem erro, sem log. Pool que o
    # operador so' consegue alcancar pela metade e' a familia do botao que
    # mente, so' que por colisao de texto.
    # ⚠️ O TETO DE 42 e' a largura do combobox (`width=38` + folga): rotulo
    # maior fica cortado na tela, e rotulo cortado volta a ser ilegivel — que e'
    # exatamente o problema que ele veio resolver.
    # ⛔ E O `id` E' COBRADO DA ENTRADA porque a linha `mapa[txt] = e.get("id")`
    # do `ui_agente` e' o que vira TRAVA. Entrada sem `id` mapeia para None, o
    # `if alvo:` do `travas()` descarta a escolha e o menu vira ENFEITE: o
    # operador escolhe uma pessoa e o sorteio devolve outra, sem uma linha de
    # erro. Foi o estado real deste pool ate' 2026-08-13.
    for _ch, _rt, _pn, _cp in DROPDOWNS_UI:
        _pool = globals().get(_pn)
        if not isinstance(_pool, list) or not _pool:
            falhas.append("DROPDOWNS_UI: o pool %r nao existe ou esta' vazio — "
                          "o `ui_agente` le' com getattr e desenha um menu "
                          "VAZIO, sem erro nenhum" % _pn)
            continue
        if _ch not in EIXOS_TRAVAVEIS:
            falhas.append("DROPDOWNS_UI: o eixo %r nao esta' em "
                          "EIXOS_TRAVAVEIS — o menu oferece uma escolha que o "
                          "sorteio nao aceita" % _ch)
        if _rt not in [e[1] for e in EIXOS_UI if e[0] == _ch]:
            falhas.append("DROPDOWNS_UI: o eixo %r se chama %r no menu e outra "
                          "coisa (ou nada) no EIXOS_UI — dois nomes para o "
                          "mesmo eixo confundem quem opera" % (_ch, _rt))
        _txt = [str(e.get(_cp) or "") for e in _pool]
        _sem = [i for i, t in enumerate(_txt) if not t]
        if _sem:
            falhas.append("ROTULO: %d entrada(s) de %s sem %r — o dropdown cai "
                          "no `id` e o operador le' codigo em vez de gente "
                          "(1a: indice %d)" % (len(_sem), _pn, _cp, _sem[0]))
        _rep = sorted({t for t in _txt if t and _txt.count(t) > 1})
        if _rep:
            falhas.append("ROTULO: %d rotulo(s) repetido(s) em %s (%r) — a "
                          "segunda entrada some do dropdown sem erro nenhum"
                          % (len(_rep), _pn, _rep[0]))
        _longos = [t for t in _txt if len(t) > 42]
        if _longos:
            falhas.append("ROTULO: %d rotulo(s) de %s acima de 42 chars (%r, "
                          "%d) — estoura a largura do menu"
                          % (len(_longos), _pn, _longos[0], len(_longos[0])))
        _sem_id = [i for i, e in enumerate(_pool) if not e.get("id")]
        if _sem_id:
            falhas.append("DROPDOWNS_UI: %d entrada(s) de %s sem `id` — o "
                          "`ui_agente` mapeia rotulo -> `e.get(\'id\')`, e "
                          "None faz o `travas()` DESCARTAR a escolha: o menu "
                          "vira enfeite" % (len(_sem_id), _pn))
        # ⛔ E O ROTULO NUNCA CHEGA AO PROMPT. Ele e' portugues; um vazamento
        # poria um texto de painel dentro de um bloco IMAGE em ingles, e o Veo
        # DESENHA texto. A lente e' de AUSENCIA, e olha os blocos montados, nao
        # a intencao do `montar`.
        # ⚠️ E ela varre 40 SORTEIOS FORCANDO a entrada, nao um sorteio solto:
        # lente de vazamento que olha um bloco so' mede a sorte da seed.
        for _i in range(40):
            _e = _pool[_i % len(_pool)]
            _sr = sortear(pags[_i % len(pags)], random.Random(31000 + _i), {},
                          {_ch: _e.get("id")})
            _bj = " ".join(montar(_sr).values())
            _vaza = [t for t in _txt if t and t in _bj]
            if _vaza:
                falhas.append("ROTULO: o texto de painel %r vazou para um "
                              "bloco do prompt — ele e' portugues e o Veo "
                              "desenha texto" % _vaza[0])
                break
        # ⛔⛔ E A ESCOLHA TEM DE FIXAR DE VERDADE. Esta e' a lente de FUNCAO, e
        # e' a que faltou no MODO FORTE do GOOD 16 (licoes §41): la' o botao
        # tinha idade certa, lente propria e controle negativo, e mesmo assim
        # nao entregava. Aqui ela refaz o que o painel faz — manda o `id` como
        # trava — e cobra que as 12 specs seguintes tragam a MESMA entrada.
        _alvo = _pool[len(_pool) // 2]
        _ids = {sortear(pags[_i % len(pags)], random.Random(41000 + _i), {},
                        {_ch: _alvo.get("id")})[_ch].get("id")
                for _i in range(12)}
        if len(_ids) != 1:
            falhas.append("DROPDOWNS_UI: escolher %r no menu de %s NAO fixa o "
                          "eixo — 12 sorteios devolveram %d pessoas diferentes"
                          % (_alvo.get(_cp), _pn, len(_ids)))

    if sum(erros.values()):
        falhas.append("%d ERRO de linter" % sum(erros.values()))
    if falhas:
        print("\nSELF-TEST REPROVADO (%d falha(s)):" % len(falhas))
        for f in falhas:
            print("   " + f)
        return 1
    print("\nAUTOTESTE OK — e os controles reprovam quando devem.")
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
    # de comando entregar o MESMO video que o app entrega.
    ap.add_argument("--bela", action="store_true",
                    help="MODO BELA ligado (o padrao e' a esposa realista)")
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
