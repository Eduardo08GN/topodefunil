#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
banho16_short.py — randomizador + gerador + linter do AGENTE **BANHO 16**.

⭐⭐ O QUE ELE E': o primeiro agente do parque que acontece num BANHEIRO, e o
primeiro **sem pessoa em quadro por padrao**. A camera e' POV: o que existe do
narrador sao as MAOS. A prova nao e' um corpo nem um prop falico — e' a receita
sendo feita, com um INSTRUMENTO DE MEDIDA parado ao lado, nunca tocado.

FONTE: pagina "Be yourself" (Facebook). SETE reels lidos a 1 fps + transcricao
em 2026-08-12, mais a grade de 21 miniaturas. Numeros:

    211k views / 2.5k coment  · script IDADE longo  · placa de papelao
    112k / 2.3k               · script AVISO        · post-it   (c/l 2,39)
    101k / 646                · script rodeio       · o unico com PESSOA
     62k / 249                · script struggling
     50k / 374 · 50k / 281 · 49k / 396              · script IDADE

⛔⛔ O QUE A LEITURA PROVOU, e que este motor executa:

  1. A COPY E' TEMPLATE, NAO IMPROVISO. Quatro scripts em sete videos, e os
     tres mais recentes voltaram todos para o mesmo (IDADE). O que varia entre
     dois videos do mesmo script e' UM NUMERO: a idade.
  2. O CENARIO E' O EIXO. Sete videos, sete arranjos: cesta de canto,
     prateleira de arame, nicho embutido, borda de banheira, banquinho de
     madeira, pia. O que sobrevive aos sete e' AGUA CORRENDO + os props + a
     medida.
  3. O ROTULO `growth hack` SEPARA OS DOIS GRUPOS. Media de views COM ele:
     108,5k; SEM ele: 67k. Mediana de comentarios: 2.300 contra 374. Sao sete
     pontos, entao e' indicio e nao prova — mas custa nada e por isso e'
     OBRIGATORIO aqui.
  4. NENHUM INGREDIENTE E' NOMEADO NA FALA. A fonte nunca diz gelatina, vapor
     rub nem mel: os tres existem so' na imagem. E' o nosso CT5 cumprido por
     quem nunca leu o nosso contrato — evidencia de que a regra e' do mercado.
  5. OS VIDEOS DA FONTE SAO GERADOS POR IA. O texto dos rotulos vem
     embaralhado (`APPLE CIDER GLIAST`, `CHARFTINS`). E' o que reconcilia a
     marca com o P12: a forma e a cor sao reconheciveis, o texto nao e'
     legivel. Nao se pede a marca ao gerador — ela vem sozinha.

⛔ AS DECISOES DO OPERADOR (2026-08-12), que valem por cima da doutrina geral:

  D1 marca PODE aparecer ....................... excecao declarada ao P12
  D2 keyword continua `GELATIN` ................ NAO copiar o `recipe` da fonte
  D3 medida PODE, sem nomear o orgao ........... o trocadilho fica no ar
  D4 pessoa em quadro NAO e' obrigatoria ....... toggle, e nasce DESLIGADO
  D5 pedir follow PODE ......................... excecao declarada ao CT8
  D6 bebida E pomada, intercalando ............. eixo 50/50
  D7 apelidos: SO' `Johnson` e `manhood` ....... derruba o CT4b
  D8 registro LEVE e limpo ..................... *"sem copys muito fortes e
     agressivas para evitar restricoes, mas interessantes o suficiente para
     viralizar"*

⚠️ D6 quebra a congruencia com a VSL de proposito, e a ordem foi literal:
*"nao importa a congruencia com a VSL, e' apenas para despertar o desejo de
comentar e ir assistir a VSL"*. Registrado aqui para ninguem "corrigir" isso
depois lendo so' o CLAUDE.md.

⛔ O CT2 NASCE DESLIGADO, como no ALFA 16: ele exige que o take 1 enuncie a
falha, e este angulo nao abre em falha nenhuma — abre num AVISO ou numa
IDADE. Nao e' esquecimento, e' o desenho.

O ARCO — 2 takes de 8s, destino AdBatch Vertical 2:

    take 1  O AVISO / A IDADE   o banheiro, os props na superficie, a medida
                                parada, o rotulo `growth hack`; as maos entram
    take 2  O MECANISMO + CTA   a gelatina cai no recipiente, a colher de mel,
                                a espuma sobe · o gelatin trick + o CTA

Uso:
    python funil-organico/banho16_short.py --pagina joe --n 1
    python funil-organico/banho16_short.py --autoteste
"""

import argparse
import io
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

TITULO = "AGENTE BANHO 16"
SLUG = "banho-16"
SUBTITULO = ("2 takes de 8s = 16 segundos · o banheiro · as maos preparam a "
             "receita e a medida fica parada ao lado, intocada")

LEDGER = os.path.join(AQUI, ".banho-16-ledger.json")

CENAS_UI = ["1 · O AVISO / A IDADE", "2 · O MECANISMO + CTA"]

# ⛔ TETO por cena, e PISO que e' ARITMETICA: a soma dos minimos dos beats.
# Piso calibrado no chute vira alarme que sempre dispara, e alarme que sempre
# dispara ensina o operador a ignorar o linter inteiro.
TETO_FALA = {1: 25, 2: 25}
# ⚠️ PISO RECALIBRADO EM 13/08, quando as nove copies do operador
# substituiram os pools: o piso antigo (16/21) vinha de takes de TRES
# beats e disparava em ~40% dos sorteios de producao correta. Piso que
# sempre dispara ensina a ignorar o linter inteiro.
# ⭐ Estes dois numeros sao o MINIMO REAL medido nos pools novos.
PISO_FALA = {1: 11, 2: 19}

# ⛔ A etnia vem da PAGINA, nunca do sorteio: e' a congruencia inviolavel do
# funil. Aqui ela chega ao quadro pelas MAOS, que sao a unica parte do narrador
# que existe em imagem.
ETNIA = {
    "roy": "white American", "dean": "white American",
    "earl": "white American",
    "jason": "Black American", "philippe": "Black American",
    "joe": "white American", "ray": "white American", "matt": "white American",
    "marcus": "Black American", "chuck": "Black American",
}

PELE_TRAVAVEL = False

# ⭐⭐ O UNICO MODO DESTE MOTOR — e ele NASCE DESLIGADO. Ordem do operador:
# *"no agente python pode criar botoes para travar pessoa em quadro ou nao, e
# no sorteio gerar somente sem pessoas no quadro pois foi o padrao que mais se
# repetiu e deu certo na pagina"*.
# ⚠️ MEDIDO na fonte: 1 video em 7 tem pessoa. O padrao e' a ausencia.
MODO_PESSOA = True
MODOS_DEFAULT = ()

# ⛔⛔ D7 — SO' DOIS APELIDOS, e o `sc.APELIDOS_16` compartilhado NAO e' usado
# aqui. Ordem do operador: *"deve utilizar as palavras somente jonhson e
# manhood caso necessario, e nao pecker, wiener e outras"*. O compartilhado tem
# `pecker` e `wiener`, que sao justamente os dois que este agente nao pode
# dizer — importa-lo seria herdar o oposto da ordem.
NUCLEO = ("Johnson", "manhood")


# ===========================================================================
# O BANHEIRO — o eixo que mais varia na fonte (7 de 7 diferentes)
# ===========================================================================
# ⛔ AGUA CORRENDO em todos, sem excecao: e' o que faz `shower hack` ser lido
# no mudo. Sem agua e' uma bancada de cozinha qualquer, e o angulo evapora.
# ⚠️ `luz` e `audio` acompanham o banheiro porque um chuveiro de teto num box
# escuro e uma banheira de pe-de-galinha num banheiro claro nao soam igual.
# ⛔⛔ CADA BANHEIRO DECLARA AS SUPERFICIES QUE EXISTEM NELE (`sups`). Achado
# LENDO o bloco: o sorteio livre entregou "uma banheira de pe-de-galinha" com
# os props "na bancada da pia" — duas peles do mesmo banheiro num quadro so'.
# O Veo resolve contradicao de cenario inventando um terceiro ambiente, e ai'
# o take 2 nao casa com o take 1.
BANHEIROS = [
    {"id": "box_bege", "sups": ("cesta_canto", "prateleira_arame"),
     "cen": "a small tiled shower stall with large beige square tiles and a "
            "chrome fixed shower head running",
     "agua": "the shower running steadily behind everything",
     "luz": "Flat overhead bathroom light, damp air.",
     "audio": "a shower running on tile"},
    {"id": "box_branco", "sups": ("cesta_canto", "prateleira_arame"),
     "cen": "a white-tiled shower stall with a curved chrome arm and a wide "
            "rain head running",
     "agua": "the rain head falling in a broad soft sheet",
     "luz": "Cool daylight from a frosted window.",
     "audio": "a rain shower head, water on tile"},
    {"id": "nicho_madeira", "sups": ("nicho", "prateleira_arame"),
     "cen": "a shower wall of light reclaimed wood planks with a wide "
            "recessed niche and a rain head running above it",
     "agua": "the water falling past the mouth of the niche",
     "luz": "Bright even daylight, wet wood.",
     "audio": "a rain shower, water on wood"},
    {"id": "banheira_branca", "sups": ("borda_banheira", "tampo_madeira", "banquinho"),
     "cen": "a white bathtub filling, the chrome spout running hard into pale "
            "green water",
     "agua": "the tub spout pouring into the filling water",
     "luz": "Soft daylight, steam on the tiles.",
     "audio": "a bathtub filling, water hitting water"},
    {"id": "banheira_pes", "sups": ("borda_banheira", "banquinho", "tampo_madeira"),
     "cen": "an old clawfoot tub filling in a bright bathroom with white "
            "beadboard walls",
     "agua": "the tap running into the rising water",
     "luz": "Bright morning light through a small window.",
     "audio": "a tap running into a deep tub"},
    {"id": "pia_espelho", "sups": ("bancada_pia",),
     "cen": "a bathroom vanity with a chrome faucet, a wide mirror behind it "
            "and a shower curtain reflected in the glass",
     "agua": "the faucet running thin into the basin",
     "luz": "Warm bathroom light, soft shadows.",
     "audio": "a faucet running into a sink"},
    {"id": "banheira_azulejo", "sups": ("borda_banheira", "tampo_madeira", "banquinho"),
     "cen": "a tub alcove with small square wall tiles and a chrome spout "
            "running",
     "agua": "the spout running steadily into the tub",
     "luz": "Even daylight, pale tiles.",
     "audio": "a tub filling, water on enamel"},
    # ⭐⭐ DEZESSETE BANHEIROS NOVOS (2026-08-13). Ordem do operador: *"aumente
    # o pool de opcoes substancialmente, tambem dos ambientes"*. Oito arranjos
    # no eixo que a fonte trocou em 7 de 7 videos e' o mesmo banheiro voltando
    # a cada oito lotes — e ele e' justamente o eixo que mais varia la'.
    # ⛔⛔ O PREFIXO DO `id` E' CONTRATO, nao estilo: o `--cenario` (e o cadeado
    # do painel) filtram por `id.split("_")[0]` contra FAMILIAS_BANHEIRO. Id que
    # nao comece por `box`, `banheira` ou `pia` cai fora do filtro em silencio —
    # e' o que ja' acontece com o `nicho_madeira`, que veio da primeira versao e
    # nunca e' alcancado com a familia travada. Divida declarada, nao propagada.
    # ⛔ AGUA CORRENDO em todos os dezessete, como nos oito antigos: sem ela o
    # quadro e' uma bancada qualquer e o angulo evapora no mudo.
    # ⛔ E cada um so' declara `sups` que existem de verdade em SUPERFICIES — a
    # BA8 cobra isso por video e o autoteste cobra o pool inteiro.
    {"id": "box_vidro", "sups": ("cesta_canto", "prateleira_vidro", "nicho"),
     "cen": "a glass-walled shower stall in pale grey tile with a chrome rain "
            "head running from the ceiling",
     "agua": "the rain head falling straight down behind the glass",
     "luz": "Cool even light through the clear panel.",
     "audio": "a rain shower on tile"},
    {"id": "box_metro", "sups": ("prateleira_arame", "cesta_pendurada", "nicho"),
     "cen": "a shower stall lined to the ceiling in white subway tile with a "
            "chrome fixed head running",
     "agua": "the shower running steadily onto the tile",
     "luz": "Flat overhead light on glossy tile.",
     "audio": "a shower running on tile"},
    {"id": "box_teca", "sups": ("banco_teca", "nicho", "cesta_canto"),
     "cen": "a wide shower in warm sand-coloured tile with a teak bench along "
            "the back wall and a rain head running",
     "agua": "the rain head falling in a broad soft sheet",
     "luz": "Warm diffused light, damp air.",
     "audio": "a rain shower head, water on tile"},
    {"id": "box_marmore", "sups": ("nicho", "prateleira_vidro"),
     "cen": "a marble-lined shower in veined grey slabs with a polished nickel "
            "rain head running",
     "agua": "the water falling straight down against the marble",
     "luz": "Bright light bouncing off the polished stone.",
     "audio": "a rain shower on stone"},
    {"id": "box_verde", "sups": ("cesta_canto", "cesta_pendurada"),
     "cen": "a narrow shower stall in small mint green tile with a chrome "
            "fixed head running",
     "agua": "the shower running steadily behind everything",
     "luz": "Soft daylight through a high frosted pane.",
     "audio": "a shower running on tile"},
    {"id": "box_bronze", "sups": ("nicho", "prateleira_arame"),
     "cen": "a shower in large tumbled stone tile with an oil-rubbed bronze "
            "head running",
     "agua": "the water falling past the mouth of the niche",
     "luz": "Warm low light, wet stone.",
     "audio": "a heavy shower on stone"},
    {"id": "box_concreto", "sups": ("nicho", "banco_teca"),
     "cen": "a shower with smooth poured concrete walls and a square rain head "
            "running from the ceiling",
     "agua": "the water falling straight down in front of the wall",
     "luz": "Dim, high contrast, wet concrete.",
     "audio": "a heavy rain shower on stone"},
    {"id": "box_azul",
     "sups": ("cesta_canto", "cesta_pendurada", "prateleira_arame"),
     "cen": "a small shower stall in pale blue square tile with a chrome "
            "handset clipped high on its rail, running",
     "agua": "the handset running steadily on its rail",
     "luz": "Even daylight, pale tiles.",
     "audio": "a shower running on tile"},
    {"id": "banheira_teca",
     "sups": ("tampo_madeira", "borda_banheira", "parapeito"),
     "cen": "a deep white tub filling under a small window, the chrome spout "
            "running hard into clear water",
     "agua": "the spout pouring hard into the filling water",
     "luz": "Soft daylight, steam on the glass.",
     "audio": "a bathtub filling, water hitting water"},
    {"id": "banheira_rosa",
     "sups": ("borda_banheira", "banquinho", "bancada_pia"),
     "cen": "a bathroom in pale pink fifties tile with a white tub filling and "
            "a shower curtain pushed back",
     "agua": "the tap running into the pale water",
     "luz": "Soft warm light, steam on the tiles.",
     "audio": "a bathtub filling, water hitting water"},
    {"id": "banheira_embutida",
     "sups": ("degrau_banheira", "borda_banheira", "parapeito"),
     "cen": "a sunken tub set into a wide tiled step, filling from a low "
            "chrome spout",
     "agua": "the low spout running into the rising water",
     "luz": "Warm even light, steam over the step.",
     "audio": "a deep tub filling, water hitting water"},
    {"id": "banheira_janela",
     "sups": ("parapeito", "borda_banheira", "tampo_madeira"),
     "cen": "a white tub filling beneath a wide window with the blind half "
            "down, the tap running",
     "agua": "the tap running into the rising water",
     "luz": "Bright daylight through the half-closed blind.",
     "audio": "a tap running into a deep tub"},
    {"id": "banheira_ferro", "sups": ("borda_banheira", "banquinho"),
     "cen": "a heavy cast iron tub filling in a plain bathroom with white "
            "panelled walls",
     "agua": "the tap pouring hard into the filling tub",
     "luz": "Warm clean light, steam on the fresh paint.",
     "audio": "a bathtub filling, water hitting water"},
    {"id": "banheira_cortina",
     "sups": ("borda_banheira", "prateleira_arame", "banquinho"),
     "cen": "a tub alcove with the shower curtain pushed back on its rail and "
            "the chrome spout running",
     "agua": "the spout running steadily into the tub",
     "luz": "Even daylight, pale tiles.",
     "audio": "a tub filling, water on enamel"},
    {"id": "pia_dupla", "sups": ("bancada_pia", "prateleira_vidro"),
     "cen": "a wide double vanity in pale stone with two chrome faucets, the "
            "near one running into its basin",
     "agua": "the near faucet running thin into the basin",
     "luz": "Bright even light over the mirrors.",
     "audio": "a faucet running into a sink"},
    {"id": "pia_coluna", "sups": ("borda_pia", "armario_espelho"),
     "cen": "a white pedestal sink against a panelled wall, the chrome faucet "
            "running into the deep porcelain bowl",
     "agua": "the faucet running steadily into the bowl",
     "luz": "Warm bathroom light, soft shadows.",
     "audio": "a faucet running into a sink"},
    {"id": "pia_armario",
     "sups": ("armario_espelho", "bancada_pia", "prateleira_vidro"),
     "cen": "a bathroom basin under a mirrored cabinet standing open, the "
            "faucet running and a shower curtain behind",
     "agua": "the faucet running thin into the basin",
     "luz": "Cool even light off the mirror doors.",
     "audio": "a faucet running into a sink"},
]
FAMILIAS_BANHEIRO = ["box", "banheira", "pia"]


# ===========================================================================
# A SUPERFICIE — onde os props ficam. Sete videos, seis arranjos diferentes.
# ===========================================================================
# ⛔ Ela e' a BANCADA deste angulo, e e' o que amarra a receita ao banho. A
# fonte nunca usa uma mesa: e' sempre alguma coisa que so' existe num banheiro.
SUPERFICIES = [
    {"id": "cesta_canto", "sup": "a chrome corner shower caddy at chest height",
     "curto": "cesta de canto"},
    {"id": "prateleira_arame",
     "sup": "a wire shelf bolted to the tiled wall", "curto": "prateleira de arame"},
    {"id": "nicho", "sup": "the flat stone floor of the recessed niche",
     "curto": "nicho embutido"},
    {"id": "borda_banheira", "sup": "the wide enamel rim of the tub",
     "curto": "borda da banheira"},
    {"id": "banquinho", "sup": "a small wooden stool standing beside the tub",
     "curto": "banquinho de madeira"},
    {"id": "bancada_pia", "sup": "the white counter beside the basin",
     "curto": "bancada da pia"},
    {"id": "tampo_madeira", "sup": "a teak bath board laid across the tub",
     "curto": "tabua de banheira"},
    # ⭐⭐ SETE SUPERFICIES NOVAS (2026-08-13). Ordem do operador: *"aumente o
    # pool de opcoes substancialmente, tambem dos ambientes"*. As sete antigas
    # cobriam os sete videos da fonte e nada alem deles — banheiro americano tem
    # parapeito, banco de teca, armario de espelho e cesta pendurada, e nenhum
    # dos quatro existia aqui.
    # ⛔ Cada uma continua sendo COISA QUE SO' EXISTE NUM BANHEIRO: e' isso que
    # amarra a receita ao banho. Mesa, bancada de cozinha e aparador ficam de
    # fora por construcao — a fonte nunca usa nenhum dos tres.
    # ⚠️ A frase que consome o pool e' `On %s sit ...`, entao toda entrada tem
    # de ser sintagma nominal que aceite `On` na frente.
    {"id": "borda_pia", "sup": "the wide porcelain lip of the pedestal sink",
     "curto": "borda da pia de coluna"},
    {"id": "prateleira_vidro",
     "sup": "a glass shelf mounted on the wall under the mirror",
     "curto": "prateleira de vidro"},
    {"id": "armario_espelho",
     "sup": "the open shelf of the mirrored cabinet above the basin",
     "curto": "armario de espelho aberto"},
    {"id": "banco_teca",
     "sup": "a slatted teak bench standing inside the shower",
     "curto": "banco de teca"},
    {"id": "cesta_pendurada",
     "sup": "a plastic caddy hanging from the shower arm",
     "curto": "cesta pendurada no chuveiro"},
    {"id": "degrau_banheira",
     "sup": "the wide tiled step running around the sunken tub",
     "curto": "degrau da banheira"},
    {"id": "parapeito", "sup": "the tiled window ledge above the tub",
     "curto": "parapeito da janela"},
]


# ===========================================================================
# ⭐⭐ A MEDIDA — a promessa virada objeto
# ===========================================================================
# ⛔⛔ ELA E' A PECA CENTRAL DO ANGULO, e a regra e' uma so': **fica em quadro
# do primeiro ao ultimo segundo e NINGUEM ENCOSTA NELA**. Presente em 6 dos 7
# videos lidos.
# ⭐ E e' ela que deixa a promessa de tamanho existir sem o classificador ter
# uma palavra para pegar: a fala diz `bigger`, nunca diz onde. Quem fecha o
# sentido e' a regua, e regua nao e' palavra.
# ⚠️ O OBJETO varia (regua clara, escura, fita metrica); o que NAO varia e' a
# presenca e a intocabilidade.
MEDIDAS = [
    # ⛔⛔ OBJETO PURO, SEM POSICAO. As entradas traziam a propria pose
    # (`standing upright against the wall`, `lying flat along the edge`) e a
    # frase que as costura acrescentava outra: saia "A ruler standing upright
    # against the wall LEANS UPRIGHT AGAINST THE WALL at the left end". Duas
    # ordens de pose para o mesmo objeto e' ordem ambigua — o gerador escolhe
    # uma, e foi assim que a regua saiu FLUTUANDO e a placa saiu TAMPADA nos
    # oito renders que o operador narrou em video.
    # ⭐ Mesma licao que o TRIO 16 pagou com `held upright, held upright`.
    {"id": "regua_clara", "nome": "ruler",
     "img": "a pale wooden ruler, its numbers large and facing the camera",
     "curto": "regua clara"},
    {"id": "regua_escura", "nome": "ruler",
     "img": "a dark varnished wooden ruler marked in both inches and "
            "centimetres",
     "curto": "regua escura"},
    {"id": "regua_amarela", "nome": "ruler",
     "img": "a yellow-varnished school ruler with black markings",
     "curto": "regua amarela"},
    {"id": "fita_metrica", "nome": "tape measure",
     "img": "a soft tailor's tape measure, unrolled and straight",
     "curto": "fita metrica"},
    {"id": "regua_metal", "nome": "steel rule",
     "img": "a thin steel rule with etched markings",
     "curto": "regua de metal"},
    {"id": "regua_dobravel", "nome": "folding rule",
     "img": "a wooden folding carpenter's rule, opened out straight",
     "curto": "regua dobravel"},
]


# ===========================================================================
# ⭐ O ROTULO `growth hack` — o unico elemento que separou os dois grupos
# ===========================================================================
# ⚠️ MEDIDO nos 7: media de views COM rotulo 108,5k, SEM rotulo 67k; mediana de
# comentarios 2.300 contra 374. Sete pontos e' indicio, nao prova — mas o
# rotulo custa nada e os DOIS melhores videos o tem. Por isso aqui ele e'
# OBRIGATORIO, e o que se sorteia e' o SUPORTE, nunca a ausencia.
# ⛔ E' o unico texto permitido em quadro. A `CAUDA` proibe todo o resto.
ROTULOS = [
    # ⛔ OBJETO PURO tambem aqui, pela mesma razao. E o texto e' sempre GROWTH
    # HACK em letra de mao — foi a unica variavel que separou os dois grupos da
    # fonte (108,5k views de media com ele, 67k sem).
    {"id": "papelao",
     "img": "a torn piece of cardboard with GROWTH HACK written on it by hand "
            "in thick black marker",
     "curto": "placa de papelao"},
    {"id": "postit",
     "img": "a large yellow sticky note with GROWTH HACK written on it in blue "
            "pen",
     "curto": "post-it amarelo"},
    {"id": "papel_fita",
     "img": "a sheet of paper with GROWTH HACK written across it in thick "
            "black marker",
     "curto": "papel escrito a mao"},
    {"id": "tabua",
     "img": "a small wooden board with GROWTH HACK burned into it",
     "curto": "tabuinha de madeira"},
]


# ===========================================================================
# ⭐ A RECEITA — bebida OU pomada, 50/50 (D6)
# ===========================================================================
# ⛔ Ordem do operador: *"vamos manter bebida e pomada, fazer intercalar"*. Sao
# dois produtos diferentes e ele sabe: a bebida e' o que a VSL vende, a pomada
# e' o que a fonte faz em 6 dos 7. A congruencia foi dispensada por escrito.
# ⚠️ O que muda e' o RECIPIENTE e o gesto final; o resto do quadro e' o mesmo.
RECEITAS = [
    {"id": "bebida", "vaso_nome": "glass",
     "vaso": "a tall clear glass filled with amber liquid",
     "vaso_curto": "copo de liquido ambar",
     "final": "the powder sinks through the amber liquid in slow white "
              "ribbons",
     "curto": "bebida"},
    {"id": "pomada", "vaso_nome": "jar",
     # ⛔⛔ VICKS VAPORUB, PELO NOME E NO POTE DELE. Decisao final do operador
     # em 2026-08-12, depois de tres mensagens no mesmo dia:
     #   1. *"deixe claro o pote de vick vaporub, o nome real da marca"*
     #   2. vendo o render: *"pode deixar o Mentolaited, mas o frasco dele
     #      esta' errado, esta' no frasco do vick"*
     #   3. *"na verdade, utilize o vick vaporub mesmo, vamos ficar com o
     #      original que funcionou"*
     # ⭐ O passo 2 apontava um defeito real de COERENCIA — nome generico
     # (`Mentholated Chest Rub`) estampado no pote azul cobalto inconfundivel
     # da Vicks. Havia duas saidas coerentes: generico em pote generico, ou
     # marca em pote de marca. Ele escolheu a segunda, que e' tambem a da
     # FONTE: os 7 reels usam o pote da Vicks de verdade.
     # ⚠️ E nao ha' risco de texto legivel errado: a leitura otica mostrou que
     # os reels da fonte sao gerados por IA e o rotulo sai embaralhado sozinho
     # (`APPLE CIDER GLIAST`, `CHARFTINS`). Pedir a marca acerta FORMA e COR; o
     # texto o gerador embaralha por conta. Excecao P12 declarada (D1).
     "vaso": "an open jar of Vicks VapoRub, the classic cobalt blue tub with "
             "its turquoise lid off and lying beside it, the white cream "
             "smooth and untouched inside",
     "vaso_curto": "pote azul de pomada",
     "final": "the cream turns into a fine white foam",
     "curto": "pomada"},
]

# ⛔ O SEGUNDO INGREDIENTE, sempre visivel e nunca dito. A caixa de gelatina
# aparece nos 7 videos.
# ⛔ A MARCA PELO NOME, nos dois. Ordem do operador: *"quero que deixe claro o
# pote de vick vaporub na cena, o nome real da marca"*, e a mesma decisao D1
# vale para a gelatina, que aparece como Knox nos 7 reels da fonte.
# ⭐ E nao ha' risco de texto legivel errado: a leitura otica mostrou que os
# reels da fonte sao gerados por IA e o rotulo sai embaralhado sozinho
# (`APPLE CIDER GLIAST`, `CHARFTINS`). Pedir a marca acerta a FORMA e a COR; o
# texto o gerador embaralha por conta.
GELATINA = ("a box of Knox unflavoured gelatin, its flap torn open and a small "
            "paper sachet of white powder resting against it")

# ⭐ O terceiro: a colher de mel. E' o gesto que fecha o preparo em 6 dos 7.
COLHER = "a metal spoon holding a pool of thick amber honey"


# ===========================================================================
# AS MAOS — o narrador inteiro, quando o MODO PESSOA esta' desligado
# ===========================================================================
# ⛔⛔ E' AQUI QUE A IDADE E A ETNIA EXISTEM. A fala diz "tenho 72 anos" e nao
# ha' rosto para confirmar. Mao generica derruba a fala inteira.
# ⚠️ MEDIDO na fonte: o video campeao tem uma mao visivelmente MAIS JOVEM que a
# idade falada, e mesmo assim foi o melhor. Entao isto e' cuidado, nao lei — e
# esta' escrito aqui para ninguem transformar em trava sem medir.
# ⛔⛔ AS ENTRADAS SAO NEUTRAS DE TOM — o tom vem do `TOM_PELE`, que vem da
# ETNIA DA PAGINA. A primeira versao trazia `pale scarred skin` dentro do pool
# e NENHUMA mencao de etnia no bloco IMAGE (so' a REF a tinha): numa pagina de
# homem negro o primeiro lote saiu com mao clara, e o operador reprovou
# — *"perceba que nao ficou muito negra, quero uma cor mais forte"*.
# ⚠️ Etnia que so' existe na REF nao chega ao quadro: o IMAGE e' o que o
# gerador le' para compor, e o que nao esta' escrito nele nao acontece.
#
#
# ⛔⛔ POOL SANEADO E AMPLIADO (2026-08-13). Duas ordens do operador no mesmo
# dia: *"nao quero mao feia parecendo nao-saudavel"* e *"aumente o pool de
# opcoes substancialmente"*. O V2 ja' tinha sido saneado; este arquivo tinha
# ficado para tras e ainda carregava o pool original inteiro.
# ⚠️ O QUE ESTAVA ERRADO, e era SEIS DE SEIS: `heavily sun-spotted`,
# `weathered`, `thin skin`, `dark age spots`, `loose skin over the tendons`,
# `bony`, `pale scarred`. Todas descreviam DANO. Num angulo POV em que a mao e'
# a UNICA parte do narrador em quadro, mao castigada nao e' detalhe — e' o
# ROSTO do video.
# ⭐ Mesma doutrina do PLACA 16 (*"esses caras tao parecendo mendigo"*),
# aplicada onde ela pesa mais: DISTINTIVO, NUNCA DETERIORADO. A mao continua
# sendo de um homem de 60 e poucos — o que sai e' a avaria, nao a idade: pele
# cuidada, unhas curtas e limpas, veias discretas em vez de saltadas.
# ⛔ E NENHUMA PALAVRA DE APROVACAO (`beautiful`, `elegant`): elogio no prompt
# puxa para mao de banco de imagem, e mao de modelo de 25 num homem de 63 e' a
# incoerencia que o espectador pega antes de qualquer outra.
# ⛔ E NENHUMA COR DE PELE: a etnia entra pela PAGINA, na frase que costura o
# REF. Duas vozes decidindo a mesma coisa e' o defeito FT14 do FIGHT 16.
# ⚠️ A FORMA E' CONTRATO: `<adjetivo> hands with <detalhe> and <detalhe>`. As
# tres frases que consomem o pool sao `A pair of %s enters...`, `The same %s
# hold...` e o REF — entrada que nao comeca por adjetivo quebra as tres.
#
# ⭐⭐ 2026-08-13 — O POOL VIROU DICIONARIO, E O MOTIVO E' O DROPDOWN.
# Ordem do operador: *"implemente esse mecanismo e menu drop down para todos os
# demais agentes 16"*. O mecanismo e o `DROPDOWNS_UI` (ver la' embaixo), e ele
# monta o menu lendo `e.get(campo)` de cada entrada — o que exige DICIONARIO.
# ⛔ Lista de STRING nao serve: `"clean broad hands...".get` estoura
# AttributeError DENTRO do callback do tkinter, ou seja, o painel morre calado.
# Foi medido antes de converter, nao suposto.
# ⚠️ O `desc` e' a string ANTIGA, caractere por caractere — o que vai para o
# prompt nao mudou uma virgula (equivalencia conferida em 300 videos, hash dos
# blocos identico antes e depois). O que nasceu foram `id` (chave do sorteio) e
# `rotulo` (o texto do menu).
# ⛔⛔ AQUI NAO HA' IDADE NO ROTULO, e nao e' esquecimento: a idade deste angulo
# e' do eixo `idade`, sorteada a' parte, e a MESMA mao serve 18 idades. Prefixar
# uma idade no rotulo seria o painel prometendo o que a entrada nao decide.
# Entao o rotulo comeca pelo TRACO — porte da mao — que e' o que o operador
# reconhece de relance.
MAOS = [
    {"id": "largas_limpas",
     "rotulo": "maos largas + unhas curtas + pele lisa",
     "desc": "clean broad hands with short trimmed nails and smooth skin"},
    {"id": "sardas_leves",
     "rotulo": "firmes + sardas leves + unhas cuidadas",
     "desc": "steady hands with light freckling and neatly kept nails"},
    {"id": "veias_discretas",
     "rotulo": "grandes + veias discretas + unha quadrada",
     "desc": "large well-kept hands with faint veins and clean square nails"},
    {"id": "alianca_ouro",
     "rotulo": "solidas + alianca de ouro lisa",
     "desc": "solid hands with a plain gold wedding band and smooth even skin"},
    {"id": "bronzeado_dorso",
     "rotulo": "largas + dorso levemente bronzeado",
     "desc": "wide clean hands with short nails and a light tan across the "
             "backs"},
    {"id": "pele_limpa",
     "rotulo": "firmes + pele limpa + unhas aparadas",
     "desc": "firm hands with clear skin and neatly trimmed nails"},
    {"id": "nos_largos",
     "rotulo": "quadradas + nos largos e chatos",
     "desc": "square hands with wide flat knuckles and short clean nails"},
    {"id": "anel_prata",
     "rotulo": "dedos longos + anel de prata",
     "desc": "long-fingered hands with smooth skin and a smooth silver band on "
             "the ring finger"},
    {"id": "pelos_no_dorso",
     "rotulo": "largas + pelos no dorso + unha reta",
     "desc": "broad hands with a light dusting of hair across the backs and "
             "blunt clean nails"},
    {"id": "punho_grosso",
     "rotulo": "compactas + punho grosso",
     "desc": "compact hands with thick wrists and short square nails"},
    {"id": "sardas_nos_nos",
     "rotulo": "lisas + sardas sobre os nos dos dedos",
     "desc": "smooth hands with a scatter of small freckles over the knuckles "
             "and clipped nails"},
    {"id": "relogio_aco",
     "rotulo": "largas + relogio de aco no pulso",
     "desc": "steady wide hands with a plain steel watch on the left wrist and "
             "short nails"},
    {"id": "anel_brasao",
     "rotulo": "lisas + anel de brasao dourado",
     "desc": "smooth firm hands with a narrow gold signet ring and neatly "
             "filed nails"},
    {"id": "veias_suaves",
     "rotulo": "grandes + veias suaves + unha redonda",
     "desc": "big clean hands with softly raised veins and short rounded "
             "nails"},
    {"id": "enxutas_retas",
     "rotulo": "enxutas + pele lisa + unha reta curta",
     "desc": "lean hands with smooth skin and short straight nails"},
    {"id": "ponta_quadrada",
     "rotulo": "robustas + pontas dos dedos quadradas",
     "desc": "sturdy hands with square fingertips and short nails cut straight "
             "across"},
    {"id": "marca_de_anel",
     "rotulo": "enxutas + marca clara de anel",
     "desc": "trim hands with a faint pale band where a ring usually sits and "
             "short clean nails"},
    {"id": "bronzeado_verao",
     "rotulo": "cuidadas + bronzeado uniforme de verao",
     "desc": "well-kept hands with an even summer tan and clean rounded nails"},
    {"id": "nos_lisos",
     "rotulo": "largas + nos lisos e amplos",
     "desc": "wide steady hands with smooth broad knuckles and short clean "
             "nails"},
    {"id": "alianca_larga",
     "rotulo": "palma quadrada + alianca larga",
     "desc": "square-palmed hands with a wide plain wedding band and short "
             "polished nails"},
    {"id": "meia_lua",
     "rotulo": "grandes + unhas em meia-lua",
     "desc": "large smooth hands with neat half-moon nails and steady fingers"},
    {"id": "bracelete_couro",
     "rotulo": "largas + bracelete de couro fino",
     "desc": "broad hands with a thin leather band on the wrist and short "
             "clean nails"},
]

# ⭐⭐ O TOM, e ele e' EXPLICITO. Ordem do operador depois do primeiro lote:
# *"quero uma cor mais forte"*. `Black American` sozinho o gerador entrega em
# tom medio; o que trava o tom e' a descricao do TOM, nao o gentilico.
TOM_PELE = {
    "Black American": "very deep dark brown skin, rich and unmistakably dark",
    "white American": "fair weathered skin",
}

# ⭐ O HOMEM — so' existe com o MODO PESSOA ligado. Espelhado do unico video da
# fonte que tem gente (101k views): ele de costas/perfil diante do espelho,
# passando o creme na PROPRIA NUCA.
# ⛔ Na nuca, e nao na regiao que a copy promete. E' desvio de moderacao
# deliberado da fonte: mostra o gesto sem mostrar o alvo.
HOMENS = [
    {"id": "grisalho_curto", "idade": 58,
     "cabeca": "short grey hair and three days of grey stubble",
     "marca": "deep laugh lines at the corners of both eyes"},
    {"id": "grisalho_ondulado", "idade": 61,
     "cabeca": "wavy salt-and-pepper hair pushed back",
     "marca": "a cleft chin and an even complexion"},
    {"id": "careca_barba", "idade": 64,
     "cabeca": "a close-shaved scalp and a short white beard",
     "marca": "a birthmark below the left ear"},
    # ⚠️ DOIS COM OCULOS, e nao por gosto: o `medir_personagens --gate` acusou
    # `HOMENS oculos` ZERADO neste motor. Eixo zerado num pool de gente e' o
    # mesmo homem repetido — e aqui o rosto so' existe no BLOCO 0 (REF) e no
    # take 1 do MODO PESSOA, entao a pouca variacao que ha' precisa contar.
    {"id": "bigode", "idade": 66,
     "cabeca": "close-cropped grey hair and a thick grey moustache",
     "marca": "wire-rimmed glasses and a dimple that shows in one cheek"},
    {"id": "prateado", "idade": 69,
     "cabeca": "full silver hair combed back and a trimmed silver beard",
     "marca": "wide-set eyes and laugh lines"},
    {"id": "raspado", "idade": 62,
     "cabeca": "a shaved head and heavy grey stubble",
     "marca": "thick black-framed glasses and a small mole on the right "
              "cheekbone"},
    # ⭐⭐ DEZOITO HOMENS NOVOS (2026-08-13). Ordem do operador: *"melhore a
    # aparencia e shape desses homens"* e *"aumente o pool de opcoes
    # substancialmente"*.
    # ⭐ O `shape` ENTROU PELO CAMPO `marca`, e nao por chave nova: o motor monta
    # `%(cabeca)s, %(marca)s, wearing %(traje)s` e nao existe slot de porte. Cada
    # entrada nova carrega PORTE + PELE SAUDAVEL + ANCORA no mesmo campo, que
    # sao tres dos seis eixos que o `medir_personagens --gate` conta — os seis
    # antigos acionavam porte e pele em 2 de 6.
    # ⛔ DISTINTIVO, NUNCA DETERIORADO: nada de cicatriz, dente lascado, pele
    # castigada ou olhar fundo. As ancoras sao covinha, queixo partido, pinta,
    # mecha prateada, sarda, argola/tarraxa — sinal permanente e saudavel.
    # ⛔ E NENHUMA PALAVRA DE APROVACAO (`handsome`, `chiseled`, `strong jaw`):
    # elogio no prompt puxa o rosto para a media do banco de imagem, que e' o
    # mesmo mecanismo pelo qual `not a celebrity` invoca a celebridade.
    # ⛔ NENHUMA COR DE PELE aqui: a etnia vem do dict ETNIA, pela pagina, e ja'
    # entra na frase montada. Duas vozes no mesmo sintagma o Veo resolve
    # inventando.
    # ⚠️ OCULOS em 7 das 24 entradas (29%): eixo zerado e' o mesmo homem
    # repetido, e eixo cheio demais e' um pool de bibliotecarios.
    {"id": "barba_cheia", "idade": 63,
     "cabeca": "thick grey hair combed to one side and a full trimmed beard",
     "marca": "a broad-shouldered build, smooth-skinned, and a cleft chin"},
    {"id": "topete_prata", "idade": 65,
     "cabeca": "silver hair swept up off the forehead, clean-shaven",
     "marca": "a compact build and a beauty mark high on the left cheek"},
    {"id": "careca_bigode", "idade": 67,
     "cabeca": "a bald crown with close-cropped grey at the sides and a neat "
               "grey moustache",
     "marca": "a solid build, lightly tanned, and a small mole beside the "
              "nose"},
    {"id": "crespo_curto", "idade": 59,
     "cabeca": "short tight curls kept close and a neat goatee",
     "marca": "a trim build, laugh lines at both eyes, and a gold stud in one "
              "ear"},
    {"id": "oculos_leitura", "idade": 70,
     "cabeca": "full white hair parted low and a short white beard",
     "marca": "half-moon reading glasses, a lean build, and a cleft chin"},
    {"id": "rabo_grisalho", "idade": 62,
     "cabeca": "grey hair pulled back into a short ponytail, clean-shaven",
     "marca": "a broad build, freckled across the nose, and a silver streak "
              "above one temple"},
    {"id": "escovinha", "idade": 57,
     "cabeca": "a grey buzz cut and heavy stubble",
     "marca": "a stocky build, smooth-skinned, and a dimple in the chin"},
    {"id": "entradas_altas", "idade": 68,
     "cabeca": "a high hairline with thick grey hair behind it and a trimmed "
               "white moustache",
     "marca": "a tall narrow build and a patch of white above one temple"},
    {"id": "bigode_chevron", "idade": 66,
     "cabeca": "close-cropped silver hair and a full chevron moustache",
     "marca": "wire-frame glasses, a husky build, and laugh lines at both "
              "eyes"},
    {"id": "barba_curta", "idade": 60,
     "cabeca": "dark hair going grey at the temples and a short cropped beard",
     "marca": "a broad-shouldered build, smooth-skinned, and a small mole at "
              "the jawline"},
    {"id": "locs_grisalhos", "idade": 64,
     "cabeca": "short grey locs tied back and a neat chin-strap beard",
     "marca": "a lean build, laugh lines at both eyes, and a gold hoop in the "
              "left ear"},
    {"id": "oculos_pretos", "idade": 71,
     "cabeca": "fine white hair combed back, clean-shaven",
     "marca": "thick black-framed glasses, a slight build, and a birthmark on "
              "the right temple"},
    {"id": "cabelo_ondulado", "idade": 63,
     "cabeca": "wavy grey hair kept a little long and light stubble",
     "marca": "a rangy build, lightly tanned, and a cleft chin"},
    {"id": "careca_total", "idade": 61,
     "cabeca": "a fully shaved head and a short white goatee",
     "marca": "a barrel-chested build and a beauty mark below one eye"},
    {"id": "oculos_aro", "idade": 69,
     "cabeca": "silver hair in a side part and a trimmed silver beard",
     "marca": "rimless glasses, a compact build, and a dimple in one cheek"},
    {"id": "viuvo_pico", "idade": 58,
     "cabeca": "a widow's peak in thick salt-and-pepper hair, clean-shaven",
     "marca": "broad shoulders, smooth-skinned, and a small mole above the "
              "lip"},
    {"id": "grisalho_alto", "idade": 72,
     "cabeca": "thick grey hair pushed straight back and a close-trimmed "
               "beard",
     "marca": "a tall solid build, laugh lines at both eyes, and a silver "
              "streak in the beard"},
    {"id": "oculos_dourados", "idade": 65,
     "cabeca": "short silver hair and a neat white moustache",
     "marca": "gold wire-rimmed glasses, a trim build, and a cleft chin"},
]

TRAJES = [
    "a faded blue cotton t-shirt",
    "a plain grey t-shirt, damp at the collar",
    "a white undershirt",
    "a navy t-shirt with the sleeves pushed up",
]


# ===========================================================================
# A COPY — duas familias de abertura, um fecho
# ===========================================================================
# ⛔⛔ A ORDEM DAS BATIDAS E' A DA FONTE, e ela nao e' arbitraria: o aviso (ou a
# idade) prende, a consequencia (ou a promessa) da' o motivo de ficar, e o
# take 2 inteiro e' mecanismo -> CTA -> follow.
#
# ⭐ FAMILIA IDADE — 4 dos 7 videos, incluindo o campeao de 211k.
# ⚠️ A idade e' `%(idade)d`: e' o UNICO campo que a fonte troca entre dois
# videos do mesmo script. Deixa-la literal no pool seria congelar o unico eixo
# que eles mexem.
IDADES_HACK = [
    "I am %(idade)d, and this is my shower hack.",
    "I am %(idade)d, and this is my morning trick.",
    "At %(idade)d, this is the shower hack I use.",
    "I am %(idade)d, and this is my bathroom trick.",
    "I am %(idade)d, and this is the trick I use.",
    "At %(idade)d, this is my shower routine.",
    "I am %(idade)d, and this one stays in my shower.",
    "I am %(idade)d, and this is my nightly trick.",
    "At %(idade)d, this is the habit I kept.",
    "I am %(idade)d, and this is my bath trick.",
]

QUANDOS = [
    "I use it every night before bed.",
    "I do this every single night.",
    "Every night, right before bed.",
    "I have done it nightly for months.",
    "I use it before bed, every night.",
    "It takes me two minutes a night.",
    "I do it while the water runs.",
    "Every night, in the shower.",
    "I have not skipped a night since.",
    "I do it before I dry off.",
]

PROMESSAS = [
    "It made me bigger, and I last longer.",
    "Now I am bigger and I last all night.",
    "It changed my size and my stamina.",
    "Bigger, and I do not go soft.",
    "I gained size, and I last much longer.",
    "It gave me size and staying power.",
    "Bigger than I was at forty.",
    "It gave me back my size and my nights.",
    "I am bigger now, and I last.",
    "More size, and I do not quit early.",
]

# ⭐ FAMILIA AVISO — 1 dos 7, mas a MELHOR taxa de comentario (2,39 contra
# 1,67 do campeao). E' a familia do nosso GOOD 16: a leitura otica encontrou
# `If you are single, do not try this` e `ladies won't keep up with you`, que
# ja' vivem nos pools `AVISOS` e `AGUENTAM` de la'.
AVISOS_SOLTEIRO = [
    "If you are single, skip this one.",
    "Single men, this is not for you.",
    "If you are single, do not try this.",
    "No wife at home? Skip this one.",
    "Single men, stop the video here.",
    "If you are single, this is not for you.",
    "Single men, you can skip this.",
    "If nobody is waiting at home, skip this.",
    "If you are single, leave this one.",
    "Single men, this one is not yours.",
]

AVISOS_CASADO = [
    "If you are married, go easy.",
    "Married men, take it slow.",
    "If you have a wife, go easy.",
    "Married men, do not overdo it.",
    "If you are married, use it carefully.",
    "Married men, you were warned.",
    "If you have a wife, be careful.",
    "Married men, start slow.",
    "If you are married, thank me later.",
    "Married men, one spoon is plenty.",
]

ELAS = [
    "She will not keep up with you afterwards.",
    "Your wife will not keep up.",
    "She is going to ask for a night off.",
    "She will not be getting much sleep.",
    "Your wife will notice the same night.",
    "She will not keep up for long.",
    "Your wife will be asking for mercy.",
    "She will need a night off after this.",
    "Your wife is going to notice.",
    "She will not be sleeping tonight.",
]

# ===========================================================================
# TAKE 2 — o mecanismo, o CTA e o follow
# ===========================================================================
# ⛔⛔ CT3: toda entrada carrega o literal `gelatin trick`, um VERBO DE EFEITO e
# um ALVO de `sc.ALVOS_16` na MESMA sentenca. `gelatin trick` sozinho e' nome
# sem razao, e o espectador nao sabe do que se trata.
# ⛔⛔ CT7: o orgao NUNCA divide sentenca com verbo de ereccao. A fonte diz
# `make your buddy big and as hard as a rock` — orgao e `hard` juntos, a frase
# mais restringivel do lote inteiro. Aqui o efeito fica no verbo (clears,
# opens, feeds) e a rigidez nao e' dita: o ouvido junta, o classificador nao.
# ⭐ E' isso que cumpre a ordem D8 (*"mais leve e limpo, sem copys muito fortes
# e agressivas para evitar restricoes"*) sem perder o alvo.
MECANISMOS = [
    "The gelatin trick clears the blood path to your {o}.",
    "The gelatin trick opens the flow to your {o}.",
    "The gelatin trick sends blood back to your {o}.",
    "The gelatin trick feeds blood back to your {o}.",
    "The gelatin trick restores the flow to your {o}.",
    "The gelatin trick fills your {o} with blood again.",
    "The gelatin trick carries blood back to your {o}.",
    "The gelatin trick opens the blood flow to your {o}.",
    "The gelatin trick feeds the flow back to your {o}.",
    "The gelatin trick restores blood to your {o}.",
]

# ⛔ CT6: o CTA diz ONDE a receita chega. ⛔ E a VIRGULA depois de `gelatin` e'
# intocavel — a automacao de DM casa palavra EXATA, e ela e' a mesma nas 12
# paginas. Trocar a keyword aqui quebraria todas de uma vez (D2).
CTAS = [
    "Comment recipe, and the recipe goes to your messages.",
    "Comment recipe, and the recipe lands in your messages.",
    "Comment recipe, and the recipe is in your messages.",
    "Comment recipe, and I'll send it to your inbox.",
    "Comment recipe, and it goes straight to your inbox.",
    "Comment recipe, and the recipe arrives in your messages.",
    "Comment recipe, and I'll send it to your messages.",
    "Comment recipe, and the full recipe hits your inbox.",
    "Comment recipe, and it lands in your inbox tonight.",
    "Comment recipe, and the recipe reaches your messages.",
]

# ⭐ D5 — o follow foi LIBERADO pelo operador, e o CT8 cai aqui.
# ⛔ Mas ele NAO pode ser condicao: `Follow me or it won't send` e' mentira — a
# DM sai igual, fato confirmado por ele em 2026-08-10, e foi por isso que o CT8
# nasceu. Estas dez entradas sao PEDIDO, nunca porteiro.
FOLLOWS = [
    "Follow me so it reaches you.",
    "Follow me so I can send it.",
    "Follow me so it gets to you.",
    "Follow me and I will send it.",
    "Follow me so it can find you.",
    "Follow me so I can reach you.",
    "Follow me and it comes to you.",
    "Follow me so it arrives tonight.",
    "Follow me so I can deliver it.",
    "Follow me and it will reach you.",
]

IDADE_MIN, IDADE_MAX = 62, 74


# ===========================================================================
# CAUDA E CLAUSULAS DE QUADRO
# ===========================================================================
# ⛔ O rotulo `growth hack` E' o unico texto permitido. Sem esta clausula o
# gerador enche o azulejo de placas e o quadro vira anuncio.
# ⭐⭐ O ENQUADRAMENTO, e ele e' a correcao mais importante do lote de video de
# 2026-08-12. O operador abriu um reel da fonte ao lado do nosso render e disse:
# *"olha a diferenca da camera, do posicionamento da camera para a mao. NAO
# PRECISA TER ESPACO, nao precisa fazer sentido. A mao pode estar sendo filmada
# de perto mesmo. Olha a qualidade da placa ali, da agua caindo ao fundo, dos
# produtos aqui perto. E' isso que eu quero."*
# ⛔ `Vertical medium shot` era a origem do defeito que ele nomeou tres vezes:
# *"essa mao ta' vindo de muito longe"*, *"nao precisa estar tao longe da
# camera"*, *"essas duas ficaram muito de lado"*. Plano medio pede espaco, e
# espaco afasta a mao e a joga para a lateral.
# ⚠️ E vale a observacao dele sobre a fonte: o enquadramento NAO precisa ser
# espacialmente plausivel. A mao pode estar impossivelmente perto — e' assim
# que os 7 reels sao.
# ⚠️ SEM A TAG: quem a poe e' o `sc.selar_tags`. A primeira versao a trazia
# embutida e o bloco saiu com `IMAGE 01/02: IMAGE 01/02:` — o AdBatch parseia
# pelo cabecalho, e cabecalho duplicado e' bloco que entra no slot errado.
ENQUADRAMENTO = ("Vertical close shot, camera right up at the shelf, shot "
                 "straight on. The objects fill the frame and the hands come "
                 "in close to the lens.")

CAUDA = ("Shot on an iPhone, natural grain, slightly wet lens. "
         "No subtitles, no captions, no watermark.")

# ⛔ A MEDIDA NUNCA E' TOCADA — em nenhum dos dois takes, por nenhuma mao.
# ⛔⛔ E A TRAVA CITA O OBJETO QUE ESTA' EM CENA. A primeira versao dizia
# `the ruler` fixo, e o sorteio entrega FITA METRICA em 1 de 6 videos: o prompt
# mandava nao tocar num objeto que nao existia no quadro. Contradicao assim o
# Veo resolve INVENTANDO a regua — e ai' sao dois instrumentos de medida na
# cena. Achado LENDO o bloco, nao por lente.
NAO_TOCA = ("Nothing lifts, moves or touches the %s, and nothing is added to "
            "the surface or taken away from it.")


# ===========================================================================
# HELPERS
# ===========================================================================

def _palavras(t):
    return len(re.findall(r"[A-Za-z0-9'%()\-]+", t or ""))


def _mn(pool):
    """O menor beat do pool, ja' resolvido o `%(idade)d`."""
    return min(_palavras(_amostra(x)) for x in pool)


def _amostra(x):
    return x % {"idade": 70} if "%(idade)" in x else x


def _cabe(pool, reserva, cena, o=None):
    """As entradas que ainda cabem no teto depois de reservar os outros beats.

    ⛔ Sem isto uma entrada longa vira LETRA MORTA: nunca e' sorteada e o
    autoteste a conta como viva. E' a lente [ALCANCE], paga no GOOD 16.
    """
    def _mede(x):
        t = _amostra(x)
        return _palavras(t.format(o=o) if o and "{o}" in t else t)
    ok = [x for x in pool if _mede(x) + reserva <= TETO_FALA[cena]]
    return ok or list(pool)


def _fresco(pool, usados, rng, chave="id"):
    """Sorteia evitando o que saiu nos ultimos lotes. Pool grande com sorteio
    sem memoria repete igual — licao do PEE 16."""
    livres = [x for x in pool if x[chave] not in usados]
    return rng.choice(livres or pool)


def _fresco_txt(pool, usados, rng):
    livres = [x for x in pool if x not in usados]
    return rng.choice(livres or list(pool))


def _por_id(pool, valor, chave="id"):
    for x in pool:
        if x[chave] == valor:
            return x
    return pool[0]


def _cap(s):
    return s[0].upper() + s[1:] if s else s


# ===========================================================================
# LEDGER
# ===========================================================================

def _carregar_ledger():
    if not os.path.isfile(LEDGER):
        return {}
    try:
        with io.open(LEDGER, encoding="utf-8") as f:
            return json.load(f)
    except (ValueError, IOError):
        return {}


def _gravar_ledger(ledger, spec=None):
    if spec is not None:
        for eixo, chave in (("banheiro", "id"), ("superficie", "id"),
                            ("medida", "id"), ("rotulo", "id"),
                            ("receita", "id"), ("homem", "id")):
            v = spec.get(eixo)
            if isinstance(v, dict):
                ledger.setdefault(eixo, []).append(v[chave])
                ledger[eixo] = ledger[eixo][-24:]
        ledger.setdefault("idade", []).append(spec["idade"])
        ledger["idade"] = ledger["idade"][-8:]
    try:
        with io.open(LEDGER, "w", encoding="utf-8") as f:
            f.write(json.dumps(ledger, ensure_ascii=False, indent=1))
    except IOError:
        pass


# ===========================================================================
# ⭐⭐ AS NOVE COPIES DO OPERADOR — 2026-08-13
# ===========================================================================
# Comprimidas por ele a partir dos QUATRO roteiros da pagina fonte, medidos e
# transcritos: A (`shower hack` + idade), B (o comprimido), C (a falha na
# cara) e D (o rodeio). O roteiro E ja' cabia em 16s e e' o que o GOOD 16 usa.
#
# ⛔⛔ A IDADE E' SLOT NAS DUAS PONTAS. Onde o hook diz a idade e onde o fecho
# do rodeio diz a idade, os dois leem `spec["idade"]` — entao nunca ha' dois
# numeros diferentes no mesmo video. E' a alternativa ao guarda que eu ia
# escrever: em vez de PROIBIR 5 pares, o defeito deixa de ser possivel.
# ⭐ E isso e' o que a fonte faz: tres dos sete reels sao 99% identicos e a
# UNICA diferenca entre eles e' o numero da idade (67 / 72 / 66).
#
# ⛔ A KEYWORD E' `recipe` POR ORDEM DELE (13/08), contra a ordem de 02/08 que
# travava `gelatin` em todos os agentes. Uma constante, uma palavra para voltar.
CTA_BANHO = "Comment recipe,"

HOOKS_ED = [
    "I am %(idade)d and this is the shower hack I use every night to look "
    "bigger and last longer.",
    "I am %(idade)d. Why do men still have small baseball bats and go soft "
    "every single night?",
    "I am %(idade)d and I fixed my small bat with one habit in the shower.",
    "I am %(idade)d. One shower habit fixed my small bat for good.",
    "I am %(idade)d, and a shower habit did what no pill ever did.",
    "Struggling to stay hard, or with your small size? That is not about "
    "getting older.",
    "Struggling to stay hard? That is not about age at all.",
    "Over fifty and not doing this trick? You are already falling like a lame "
    "horse in the middle of a rodeo.",
    "Why accept a shrinking bat and going soft? I am %(idade)d and I use zero "
    "blue pills.",
]

FECHOS_ED = [
    "It clears the toxic buildup in your arteries so blood flows again. No "
    "pharmacy. %s and I will send the step-by-step." % CTA_BANHO,
    "This shower hack clears the toxic buildup blocking your blood, and you "
    "gain inches down there. %s and I will send it." % CTA_BANHO,
    "It unclogs the toxic buildup stopping your blood flow. Clear pipes, "
    "maximum size. %s and I will send the step-by-step." % CTA_BANHO,
    "Once the pipes are clear you get maximum size and rock solid endurance. "
    "%s and I will send the step-by-step." % CTA_BANHO,
    "It simply unclogs the toxic buildup stopping your blood flow. No side "
    "effects. %s and I will send it to you." % CTA_BANHO,
    "This shower trick flushes out the toxins clogging your blood vessels. "
    "%s and I will send the full step-by-step." % CTA_BANHO,
    "This shower trick flushes the toxins clogging your vessels, and you gain "
    "inches down there. %s and I will send it." % CTA_BANHO,
    # ⚠️ CONCATENACAO, nao `%`: esta entrada tem `%(idade)d` E o literal do
    # CTA. Formatar na definicao tentaria preencher os dois de uma vez e
    # estoura (`format requires a mapping`) — o `%(idade)d` so' pode ser
    # resolvido em tempo de sorteio.
    "I am %(idade)d and I use zero blue pills. " + CTA_BANHO
    + " and I will send you the step-by-step video.",
    "This shower hack forces blood down there for rock hard results. %s and I "
    "will send the full step-by-step." % CTA_BANHO,
]



# ===========================================================================
# SORTEIO
# ===========================================================================

def _falas(spec, rng, quais=(0, 1)):
    """As duas falas.

    ⛔⛔ CT4 — UM APELIDO POR VIDEO. Aqui ele so' aparece no take 2 (o take 1
    nunca nomeia o orgao em nenhuma das duas familias), entao nao ha' o que
    repetir — mas o campo continua UNICO no spec para o painel nao mentir.
    ⛔ ORDEM DE ESCOLHA: escolhe primeiro quem tem MENOS substituto. No take 2
    e' o MECANISMO, que carrega o literal do funil, o verbo e o alvo na mesma
    sentenca. O beat mais intercambiavel escolhe por ULTIMO e absorve a sobra.
    """
    o = spec["apelido"]
    f = dict(enumerate(spec.get("falas", ["", ""])))

    if 0 in quais:
        f[0] = rng.choice(HOOKS_ED) % {"idade": spec["idade"]}
    if 1 in quais:
        f[1] = rng.choice(FECHOS_ED) % {"idade": spec["idade"]}

    return f


def sortear(pagina, rng, led, travas=None):
    travas = travas or {}
    hist = led if isinstance(led, dict) else {}
    etnia = ETNIA.get(pagina, "white American")

    fam = travas.get("familia_banheiro")
    pool_b = ([b for b in BANHEIROS if b["id"].split("_")[0] == fam]
              if fam and fam != "livre" else BANHEIROS)
    banheiro = (_por_id(BANHEIROS, travas["banheiro"]) if travas.get("banheiro")
                else _fresco(pool_b or BANHEIROS, hist.get("banheiro", [])[-4:], rng))

    # ⛔ So' as superficies que existem NESTE banheiro. O cadeado da tela
    # continua vencendo: superficie travada no painel e' escolha explicita do
    # operador, e ele ve' o resultado antes de gerar.
    _sups = [x for x in SUPERFICIES if x["id"] in banheiro["sups"]]
    superficie = (_por_id(SUPERFICIES, travas["superficie"])
                  if travas.get("superficie")
                  else _fresco(_sups or SUPERFICIES,
                               hist.get("superficie", [])[-2:], rng))
    medida = (_por_id(MEDIDAS, travas["medida"]) if travas.get("medida")
              else _fresco(MEDIDAS, hist.get("medida", [])[-3:], rng))
    rotulo = (_por_id(ROTULOS, travas["rotulo"]) if travas.get("rotulo")
              else _fresco(ROTULOS, hist.get("rotulo", [])[-2:], rng))
    receita = (_por_id(RECEITAS, travas["receita"]) if travas.get("receita")
               else _fresco(RECEITAS, hist.get("receita", [])[-1:], rng))

    # ⭐ MODO PESSOA — nasce DESLIGADO (D4). O cadeado da tela vence o modo,
    # como em todos os motores: homem travado no painel e' mais especifico.
    pessoa = bool(travas.get("pessoa")) and MODO_PESSOA
    homem = (_por_id(HOMENS, travas["homem"]) if travas.get("homem")
             else _fresco(HOMENS, hist.get("homem", [])[-3:], rng))

    # ⛔ A idade da FALA e a idade do HOMEM em quadro sao a MESMA quando ele
    # aparece. Duas idades diferentes no mesmo video e' a contradicao que o Veo
    # resolve inventando um terceiro rosto.
    if pessoa:
        idade = homem["idade"]
    else:
        livres = [i for i in range(IDADE_MIN, IDADE_MAX + 1)
                  if i not in hist.get("idade", [])[-6:]]
        idade = rng.choice(livres or list(range(IDADE_MIN, IDADE_MAX + 1)))

    spec = {
        "pagina": pagina, "etnia": etnia,
        "banheiro": banheiro, "superficie": superficie, "medida": medida,
        "rotulo": rotulo, "receita": receita,
        "pessoa": pessoa, "homem": homem,
        "traje": rng.choice(TRAJES),
        # ⭐ O DROPDOWN `AS MAOS` entra POR AQUI. ⚠️ O `rng.choice` fica no
        # ramo `else` de proposito: sem trava a chamada acontece no MESMO ponto
        # da sequencia de sorteio de sempre, entao nenhum video existente muda.
        "maos": (_por_id(MAOS, travas["maos"]) if travas.get("maos")
                 else rng.choice(MAOS)),
        "idade": idade,
        "abertura": (travas.get("abertura")
                     or rng.choice(["idade", "idade", "idade", "aviso"])),
        # ⛔ D7 — os dois unicos apelidos deste agente.
        "apelido": rng.choice(list(NUCLEO)),
    }
    spec["falas"] = [v for _, v in sorted(_falas(spec, rng).items())]
    return spec


def nova_fala(spec, i, rng):
    """⛐ O BANCO DE COPY POR CENA — e' esta funcao que a UI chama.

    ⚠️ Ela NAO existia neste motor, e o botao `trocar` da tela estava MORTO
    desde que o agente nasceu: a UI procura `nova_fala(spec, i, rng)` e o que
    havia aqui era um `trocar_fala(spec, rng, i)` — outro nome, outra ordem de
    argumentos — que ninguem nunca chamou. 41 dos 44 motores do parque tinham
    a funcao certa; os tres do BANHO nao, porque o primeiro nasceu sem ela e os
    outros dois nasceram por copia dele.
    ⭐ Forma sem funcao ao contrario: a funcao existia e o nome e' que estava
    errado, entao nem o import quebrava. So' o operador clicando descobre.
    """
    pool = HOOKS_ED if i == 0 else FECHOS_ED
    return rng.choice(pool) % {"idade": spec["idade"]}


def trocar_fala(spec, rng, i):
    return _falas(spec, rng, quais=(i,))[i]


# ===========================================================================
# MONTAGEM
# ===========================================================================

def montar(spec):
    b, r = spec["banheiro"], spec["receita"]
    sup, med, rot = spec["superficie"], spec["medida"], spec["rotulo"]
    h = spec["homem"]
    # ⛔⛔⛔ O LOTE COMENTADO EM VIDEO (2026-08-12). O operador gravou a tela
    # narrando as OITO imagens, uma a uma, e o veredito dele fecha assim:
    # *"voce tem todo o contexto de como deve ser o visual, eu ja' te dei o
    # padrao desses videos, eu te dei sete videos, e' so' analisar eles e fazer
    # uma cena SIMPLES aqui, nao precisa de muita coisa, e' uma cena simples"*.
    #
    # ⛔ Ele estava certo: o bloco tinha chegado a 329 PALAVRAS para uma cena
    # de seis objetos. Cada correcao minha virava mais uma clausula, e clausula
    # concorrente e' o que faz o gerador escolher mal.
    #
    # ⭐⭐ E O CONSERTO NAO E' SO' ENCURTAR, E' ATRIBUIR POSICAO. Todos os
    # defeitos que ele nomeou sao de objeto SEM LUGAR definido:
    #     "a placa esta' sendo tampada"          -> sem lugar
    #     "regua flutuando"                      -> sem apoio
    #     "a regua tampando o potinho da gelatina"-> sem lugar
    #     "o saquinho da gelatina la' no fundo"  -> sem lugar
    #     "os itens muito espalhados"            -> sem agrupamento
    #     "a mao vindo pela lateral"             -> direcao fraca
    # Objeto sem posicao o gerador empilha. Cada peca ganha uma: os tres potes
    # AGRUPADOS no meio, a medida encostada a' ESQUERDA, a placa a' DIREITA, as
    # maos entrando POR CIMA.
    # ⚠️ Saiu o `Nearest to the camera and in sharp focus` (foi ele que fez a
    # regua flutuar na frente) e saiu o `clear space around every object` (foi
    # ele que espalhou os itens).
    # ⛔ `unhurried` SAIU em 2026-08-20 — mesma ordem do operador e mesma
    # razao do `banho16_3t`: pedir voz sem pressa e' pedir menos palavra
    # dentro do mesmo take. `calm` e `matter-of-fact` ficam: eles descrevem
    # o REGISTRO, nao a VELOCIDADE.
    voz = ("Voice: one calm American man in his %ds, plain "
           "matter-of-fact delivery, slightly gravelly, speaking straight to "
           "camera at the ordinary pace of everyday American speech, never stretching or slowing the words to fill the take. "
           "The same voice in both takes." % ((spec["idade"] // 10) * 10))

    # ⛔ A GEOMETRIA DA AGUA, dita e nao proibida.
    # ⛔ AO FUNDO, e nao "afastada". O conserto anterior empurrou o jato para
    # a parede lateral e em varios renders a agua sumiu do quadro — e o
    # operador, mostrando a fonte, apontou justamente *"a agua caindo ao
    # fundo"* como parte do que ele quer ver. Ela fica ATRAS, visivel, e nao
    # encosta na prateleira.
    agua = ("The shower runs in the background behind the shelf, the falling "
            "water clearly visible the whole time, and none of it reaches the "
            "shelf or anything on it.")

    cena = ("%s, brightly and evenly lit. %s On %s, grouped close together in "
            "the middle, stand %s, %s and %s. %s leans upright against the "
            "wall at the left end of the shelf, whole and fully visible, "
            "covering nothing. %s stands flat against the wall at the right "
            "end, large and completely unobstructed."
            % (_cap(b["cen"]), agua, sup["sup"], r["vaso"], GELATINA, COLHER,
               _cap(med["img"]), _cap(rot["img"])))

    # ⚠️ SEM ARTIGO: o IMAGE 02 diz "the same %s" e o artigo embutido gerava
    # "come the same THE hands of a 62-year-old...". Artigo e' da frase, nao do
    # dado — mesma classe do `held upright, held upright` do TRIO.
    maos = ("hands of a %d-year-old %s man, %s, %s"
            % (spec["idade"], spec["etnia"],
               TOM_PELE.get(spec["etnia"], "weathered skin"),
               spec["maos"]["desc"]))

    if spec["pessoa"]:
        quem1 = ("A %d-year-old %s man stands with his back half to the "
                 "camera, %s, %s, wearing %s, holding the spoon of honey over "
                 "the %s."
                 % (h["idade"], spec["etnia"], h["cabeca"], h["marca"],
                    spec["traje"], r["vaso_nome"]))
    else:
        quem1 = ("Coming in close to the lens from the bottom of the frame, "
                 "large in the picture, are the %s: one hand holds the %s "
                 "steady, "
                 "the other tips the spoon of honey over it."
                 % (maos, r["vaso_nome"]))

    b1 = ("%s %s %s %s %s"
          % (ENQUADRAMENTO, cena, quem1, _cap(b["luz"]), CAUDA))

    t1 = ("TAKE 01/02: Animate the provided image exactly. Handheld iPhone "
          "shot, very slight natural sway, no cuts, and the camera does not "
          "move. The spoon tips and a slow thread of honey runs down into the %s, "
          "and that is the only thing that happens. The gelatin box and its "
          "sachet stay closed and untouched on the shelf. %s %s\n"
          'Dialogue: "%s"\n%s\nAudio: %s. No music.'
          % (r["vaso_nome"], NAO_TOCA % med["nome"], agua,
             sonorizar(spec["falas"][0]), voz, b["audio"]))

    # ⛔ O MESMO texto de cena, palavra por palavra — foi ele que segurou a
    # continuidade quando o take 2 ia parar noutro comodo. So' muda o que muda:
    # o mel ja' esta' dentro e a mao agora segura o sache.
    b2 = ("%s Same place, same tiles, same light. %s The pool of honey is already inside the %s "
          "and the spoon lies empty beside it. Coming in close to the lens "
          "from the bottom of "
          "the frame, large in the picture, come the same %s, holding the torn "
          "paper sachet over the "
          "%s, tipped, a fine stream of white powder falling in. %s %s"
          % (ENQUADRAMENTO, cena, r["vaso_nome"], maos, r["vaso_nome"], _cap(b["luz"]),
             CAUDA))

    # ⭐ E UMA ACAO SO' NO TAKE 2: o po cai e a mistura reage. ⛔ A reacao e'
    # CONTIDA: o primeiro lote devolveu uma escultura de espuma de trinta
    # centimetros saindo do pote, porque eu escrevi `swells over the rim`.
    t2 = ("TAKE 02/02: Animate the provided image exactly. Handheld iPhone "
          "shot, very slight natural sway, no cuts. The powder keeps falling "
          "from the sachet into the %s at the same steady rate, and %s. The foam "
          "stays inside the %s and never rises more than a finger above the "
          "rim. Nothing else enters the frame. %s %s\n"
          'Dialogue: "%s"\n%s\nAudio: %s. No music.'
          % (r["vaso_nome"], r["final"], r["vaso_nome"],
             NAO_TOCA % med["nome"], agua,
             sonorizar(spec["falas"][1]), voz, b["audio"]))

    # ⭐⭐ BLOCO 0 (REF) — E ELE E' AS MAOS.
    # ⛔ A falta dele quebrou o painel compartilhado (`KeyError 'BLOCO 0
    # (REF)'`), e a quebra apontou uma lacuna REAL: este angulo nao tinha
    # ancora nenhuma entre os dois takes. Todos os outros motores amarram a
    # continuidade num ROSTO; aqui nao ha' rosto — entao a ancora sao as MAOS,
    # que e' o unico corpo em quadro.
    # ⚠️ E foi o primeiro lote que provou o tamanho do problema: sem ancora
    # forte, o take 2 saiu noutro comodo.
    if spec["pessoa"]:
        ref = ("REF 01: Photo of a real person, a %d-year-old %s man, chest "
               "up, facing the camera directly, calm steady expression. %s, "
               "%s. Hands out of frame, no objects. Plain neutral gray "
               "background, soft even frontal light. Slight sensor grain, soft "
               "focus, raw iPhone front camera aesthetic. No subtitles, no "
               "captions, no burned-in text, no watermark."
               % (h["idade"], spec["etnia"], _cap(h["cabeca"]), h["marca"]))
    else:
        ref = ("REF 01: Photo of both hands of a %d-year-old %s man with %s, "
               "palms down on a plain surface, filled frame, nothing held. %s. "
               "Plain "
               "neutral gray background, soft even frontal light. Slight "
               "sensor grain, soft focus, raw iPhone photo. No subtitles, no "
               "captions, no burned-in text, no watermark."
               % (spec["idade"], spec["etnia"],
                  TOM_PELE.get(spec["etnia"], "weathered skin"),
                  _cap(spec["maos"]["desc"])))

    blocos = sc.selar_takes(sc.selar_tags({
        "BLOCO 0 (REF)": ref,
        "IMAGE 01/02": b1, "TAKE 01/02": t1,
        "IMAGE 02/02": b2, "TAKE 02/02": t2,
    }))
    # ⚠️ A TENSAO ENTRE `No on-screen text` E A PLACA — declarada, nao
    # consertada. A trava compartilhada e' cobrada pelo literal exato pela
    # `sc.lint_sem_texto` (trocar a frase reprovou 800 de 800), e o PLACA 16
    # roda em producao com esta mesma combinacao sem perder o cartao: o TAKE
    # anima uma IMAGE que JA' contem a placa. O primeiro lote do BANHO
    # confirmou — a placa `GROWTH HACK` apareceu nos QUATRO renders.
    return blocos


# ===========================================================================
# LENTES
# ===========================================================================

def _ba1_medida(spec, blocos, ach):
    """⭐⭐ BA1 — A MEDIDA EM QUADRO NOS DOIS TAKES, E INTOCADA.

    ⛔ E' a peca central do angulo: e' ela que faz a promessa de tamanho
    existir sem o classificador ter uma palavra para pegar. Se sumir do take 2,
    a fala promete `bigger` e o quadro nao tem onde aterrissar.
    """
    # ⚠️ Comparacao SEM CAIXA: o bloco recebe a string com a primeira letra
    # levantada pelo `_cap`, e a lente que compara com a forma do POOL em vez
    # da forma do PROMPT acusa 400 de 400 videos CERTOS — foi exatamente o que
    # ela fez no primeiro autoteste deste motor.
    alvo = spec["medida"]["img"].lower()
    for nome in ("IMAGE 01/02", "IMAGE 02/02"):
        if alvo not in blocos.get(nome, "").lower():
            ach.append(("ERRO", "BA1: %s sem o instrumento de medida — e' o "
                                "unico lugar onde o `bigger` aterrissa" % nome))
    for nome in ("TAKE 01/02", "TAKE 02/02"):
        if "or touches the" not in blocos.get(nome, ""):
            ach.append(("ERRO", "BA1: %s sem a trava de nao tocar a medida — "
                                "mao na regua vira demonstracao, e demonstracao "
                                "de tamanho e' recusa certa" % nome))


def _ba2_rotulo(spec, blocos, ach):
    """⭐ BA2 — O ROTULO `growth hack` NOS DOIS TAKES.

    ⚠️ MEDIDO nos 7 videos: com rotulo, media de 108,5k views e mediana de
    2.300 comentarios; sem rotulo, 67k e 374. Sete pontos e' indicio, nao
    prova — mas custa nada e os dois melhores o tem.
    """
    for nome in ("IMAGE 01/02", "IMAGE 02/02"):
        if "growth hack" not in blocos.get(nome, "").lower():
            ach.append(("ERRO", "BA2: %s sem o rotulo `GROWTH HACK`" % nome))


def _ba3_sem_pessoa(spec, blocos, ach):
    """⛔⛔ BA3 — COM O MODO PESSOA DESLIGADO, NINGUEM EM QUADRO.

    Ordem do operador: o sorteio gera *"somente sem pessoas no quadro, pois foi
    o padrao que mais se repetiu e deu certo na pagina"* (1 video em 7 tem
    gente). Sem esta lente, uma frase solta com `man` faria o Veo inventar um
    corpo, e o angulo inteiro depende da ausencia dele.
    """
    if spec.get("pessoa"):
        if "man stands" not in blocos.get("IMAGE 01/02", ""):
            ach.append(("ERRO", "BA3: MODO PESSOA ligado e o take 1 nao tem "
                                "homem em quadro"))
        return
    for nome in ("IMAGE 01/02", "IMAGE 02/02", "TAKE 01/02", "TAKE 02/02"):
        t = blocos.get(nome, "")
        # ⚠️ A LENTE ACUSAVA A PROPRIA CORRECAO. Desde que as maos passaram a
        # dizer de QUEM sao (`the hands of a 71-year-old Black American man`),
        # o literal ` man,` aparece em todo bloco — e isso NAO e' pessoa em
        # quadro, e' posse. A lente agora procura CORPO: alguem de pe', um
        # rosto, um torso. Lente que reprova o certo ensina a ignorar a lente.
        t_limpo = re.sub(r"hands of an? [^,]+ (?:man|woman)", "HANDS", t)
        for pista in ("man stands", "man is standing", " his face", " her face",
                      " woman ", "his back", "torso"):
            if pista in t_limpo:
                ach.append(("ERRO", "BA3: %s tem CORPO em quadro (%r) com o "
                                    "MODO PESSOA desligado"
                            % (nome, pista.strip())))
                break


def _ba4_idade(spec, blocos, ach):
    """⛔ BA4 — UMA IDADE SO' NO VIDEO.

    Com o MODO PESSOA ligado, a idade falada tem de ser a do homem em quadro.
    Duas idades diferentes no mesmo video e' a contradicao que o Veo resolve
    inventando um terceiro rosto — licao paga no VAZAMENTO.
    """
    if not spec.get("pessoa"):
        return
    if spec["idade"] != spec["homem"]["idade"]:
        ach.append(("ERRO", "BA4: a fala diz %d e o homem em quadro tem %d"
                    % (spec["idade"], spec["homem"]["idade"])))
    if spec["abertura"] == "idade" and \
            "%d-year-old" % spec["idade"] not in blocos.get("IMAGE 01/02", ""):
        ach.append(("ERRO", "BA4: a fala anuncia %d e a IMAGE nao renderiza "
                            "essa idade" % spec["idade"]))


def _ba5_apelido(spec, blocos, ach):
    """⛔⛔ BA5 — SO' `Johnson` E `manhood`, E UM POR VIDEO.

    Ordem do operador (D7). O `sc.APELIDOS_16` compartilhado traz `pecker` e
    `wiener`, que sao exatamente os dois proibidos aqui: herdar o pool
    compartilhado seria herdar o oposto da ordem.
    """
    f2 = spec["falas"][1]
    if spec["apelido"] not in NUCLEO:
        ach.append(("ERRO", "BA5: apelido %r fora de %s"
                    % (spec["apelido"], list(NUCLEO))))
    for proibido in ("pecker", "wiener", "cock", "dick", "penis"):
        if re.search(r"\b%s\b" % proibido, " ".join(spec["falas"]), re.I):
            ach.append(("ERRO", "BA5: a fala usa %r — so' `Johnson` e "
                                "`manhood` sao permitidos" % proibido))
    outros = [t for t in NUCLEO if t != spec["apelido"] and t.lower() in f2.lower()]
    if outros:
        ach.append(("ERRO", "BA5: dois apelidos no mesmo video (%s e %s)"
                    % (spec["apelido"], outros[0])))


def _ba6_leve(spec, blocos, ach):
    """⛔⛔ BA6 — O REGISTRO LEVE, que e' a razao de ser deste agente.

    Ordem do operador (D8): *"sem copys muito fortes e agressivas para evitar
    restricoes, mas interessantes o suficiente para viralizar"*.

    ⚠️ A fonte diz `make your buddy big and as hard as a rock` — orgao e verbo
    de ereccao na MESMA sentenca. E' a frase mais restringivel do lote inteiro,
    e e' exatamente o que o CT7 proibe. Copiar a fonte aqui seria copiar o
    defeito dela.
    """
    for i, fala in enumerate(spec["falas"], 1):
        for sent in re.split(r"(?<=[.!?])\s+", fala):
            tem_org = any(t.lower() in sent.lower() for t in NUCLEO)
            if tem_org and sc.ERECAO_16.search(sent):
                ach.append(("ERRO", "BA6/CT7: cena %d junta o orgao e verbo de "
                                    "ereccao na mesma sentenca: %r"
                            % (i, sent.strip())))
    # ⚠️ `rock hard` SAIU DA LISTA EM 13/08: ele esta na copy que o
    # OPERADOR escreveu (*"um resultado duro que nem pedra"*), comprimida
    # por ele a partir do roteiro D da fonte. A BA6 nasceu da ordem D8
    # dele (registro leve); a copy de hoje e mais recente e tambem e dele.
    # ⛔ A primeira metade desta lente (orgao + verbo de ereccao na mesma
    # sentenca) continua intacta, e continua sendo ERRO.
    duro = re.compile(r"\b(brutal|savage|slam|pound)\b", re.I)
    for i, fala in enumerate(spec["falas"], 1):
        m = duro.search(fala)
        if m:
            ach.append(("AVISO", "BA6: cena %d usa %r — o registro deste agente "
                                 "e' leve por ordem do operador"
                        % (i, m.group(0))))


def _ba7_follow(spec, blocos, ach):
    """⭐ BA7 — O FOLLOW E' PEDIDO, NUNCA PORTEIRO.

    O CT8 caiu por ordem do operador (D5), mas a razao pela qual ele nasceu
    continua verdadeira: *"a mensagem e' enviada independente de seguirem ou
    nao"*. Dizer `follow or it won't send` e' mentir para o espectador sobre
    uma automacao que envia de qualquer jeito.
    """
    f2 = spec["falas"][1]
    if re.search(r"follow[^.]*\b(or|otherwise|unless)\b", f2, re.I):
        ach.append(("ERRO", "BA7: o follow virou CONDICAO — a DM sai igual, e "
                            "prometer o contrario e' mentira"))


# ⛔⛔ TRES TRAVAS DO CONTRATO DE 16s DESLIGADAS NESTE MOTOR, cada uma com o
# motivo escrito e a ordem do operador citada. Regra que nasce desligada sem
# razao escrita e' regra que alguem religa amanha sem saber o que quebra.
# ---------------------------------------------------------------------------
# CT1 — "nada depois da sentenca do CTA; o follow vai ANTES". ⚠️ MEDIDO na
#   fonte: os SETE videos terminam no follow, depois do CTA. O operador
#   aprovou a ordem mecanismo -> CTA -> follow lendo a copy. O risco que o CT1
#   protege (diluir a instrucao) nao aparece nos numeros da pagina modelada.
# CT4b — "os apelidos sorteaveis sao pecker/wiener/Johnson". Ordem literal
#   dele: *"deve utilizar as palavras somente jonhson e manhood caso
#   necessario, e nao pecker, wiener e outras"*. O `manhood` nao esta' no pool
#   compartilhado, e os dois proibidos estao — manter ligado seria cobrar o
#   oposto da ordem.
# CT8 — "nenhum pedido de follow na fala". Liberado por ele: *"pedir follow nao
#   ha' problema tambem"*. ⚠️ O que NAO caiu foi a razao: a DM sai igual, entao
#   o follow e' PEDIDO e nunca CONDICAO — quem cobra isso agora e' a BA7.
# CT2 — "o take 1 enuncia a FALHA dele, com dano concreto". Este angulo NAO
#   abre em falha: abre num AVISO (`if you are single, skip this`) ou numa
#   IDADE (`I am 72, and this is my shower hack`). E' o mesmo desenho do
#   ALFA 16, e o cabecalho deste arquivo ja' o declarava — mas o codigo nao
#   fazia, e a lente acusava 337 de 400 videos CERTOS. Forma sem funcao ao
#   contrario: a doutrina escrita e o comportamento em desacordo.
_CT_DESLIGADOS = ("CT1:", "CT2:", "CT4b:", "CT8:")


def _ba8_coerencia(spec, blocos, ach):
    """⛔⛔ BA8 — A SUPERFICIE EXISTE NAQUELE BANHEIRO.

    Achado lendo o bloco, nao por lente: "an old clawfoot tub filling" com os
    props "on the white counter beside the basin". Sao dois ambientes no mesmo
    quadro, e o Veo resolve contradicao de cenario inventando um terceiro — o
    que quebra a continuidade entre os dois takes, que e' a unica coisa que
    este agente precisa manter.
    """
    if spec["superficie"]["id"] not in spec["banheiro"]["sups"]:
        ach.append(("ERRO", "BA8: superficie %r nao existe no banheiro %r"
                    % (spec["superficie"]["id"], spec["banheiro"]["id"])))


def lint(spec, blocos):
    ach = []
    falas = spec["falas"]
    sc.lint_tags(blocos, ach)
    sc.lint_sem_texto(blocos, ach)
    # ⛔⛔ A negacao anti-celebridade nunca volta ao texto montado
    # (2026-08-14, ordem do operador). Este motor nao passa pelo
    # `sc.lint_curto`, entao a lente entra aqui explicitamente — regra sem
    # guarda volta no proximo agente nascido por copia, e foi exatamente
    # assim que a clausula chegou aos 30 motores.
    sc.lint_anticeleb(blocos, ach)
    sc.lint_isca_cta(falas[1], ach, "a cena 2 (CTA)")
    # ⛔ literal LOCAL: a keyword deste agente e' `recipe`
    #    (ordem do operador 13/08), nao o `gelatin` do repo.
    if CTA_BANHO not in (falas[1] or ""):
        ach.append(("ERRO", "a cena 2 sem o literal %r"
                    % CTA_BANHO))
    sc.lint_take_vs_image(blocos, ach)
    sc.lint_painel_honesto(sys.modules[__name__], spec, blocos, ach)
    # ⛔ `isca_absurda=False`: este angulo nao tem substancia absurda nenhuma.
    _ct = []
    sc.lint_copy16(sys.modules[__name__], spec, _ct, isca_absurda=False)
    ach.extend(x for x in _ct if not x[1].startswith(_CT_DESLIGADOS))
    for f in (_ba1_medida, _ba2_rotulo, _ba3_sem_pessoa, _ba4_idade,
              _ba5_apelido, _ba6_leve, _ba7_follow, _ba8_coerencia):
        f(spec, blocos, ach)

    for i, fala in enumerate(falas, 1):
        n = _palavras(fala)
        if n > TETO_FALA[i]:
            ach.append(("ERRO", "cena %d com %d palavras (teto %d) — fala "
                                "cortada mata o CTA" % (i, n, TETO_FALA[i])))
        elif n < PISO_FALA[i]:
            ach.append(("AVISO", "cena %d com %d palavras (piso %d)"
                        % (i, n, PISO_FALA[i])))
    return ach


# ===========================================================================
# PAINEL
# ===========================================================================

# ⭐⭐ A PALAVRA DO CTA E' CAMPO NO PAINEL (2026-08-15). Ordem do operador:
# *"todos os agentes16 meus devem levar um ui ux input pertinente para alterar
# a palavra chave X do cta"*.
# ⛔ `KEYWORD_NATIVA` e' a palavra que os POOLS deste motor ja' trazem escrita —
# a ancora da substituicao, nao uma preferencia. Assumir `gelatin` para todos
# reescreveria em silencio a excecao dos tres BANHO, que usam `recipe` por
# ordem de 2026-08-13.
# ⛔ A troca vale so' para a KEYWORD (`Comment <x>,`). O MECANISMO
# (`gelatin trick`) e o rotulo da caixa em quadro NAO mudam: e' o que a VSL
# vende, e a congruencia e' inviolavel.
KEYWORD_UI = True
KEYWORD_NATIVA = "recipe"

EIXOS_UI = [
    ("banheiro", "O BANHEIRO", "BANHEIROS", "id"),
    ("superficie", "A SUPERFICIE", "SUPERFICIES", "curto"),
    ("medida", "A MEDIDA", "MEDIDAS", "curto"),
    ("rotulo", "O ROTULO", "ROTULOS", "curto"),
    ("receita", "A RECEITA", "RECEITAS", "curto"),
]
EIXOS_TRAVAVEIS = ["banheiro", "superficie", "medida", "rotulo", "receita",
                   "maos"]
TRAVAS_UI = [("familia_banheiro", "cenario",
              ["livre"] + FAMILIAS_BANHEIRO)]

# ⭐⭐ O DROPDOWN `AS MAOS` — e' ELE que da' FUNCAO ao campo `rotulo` do pool.
# ⛔ Sem esta linha os 22 rotulos seriam comentario caro: escritos, medidos,
# travados, e nenhum olho humano os veria. Forma sem funcao e' o defeito que
# este repo mais paga (licoes-de-construcao §41).
# ⛔⛔ E ELE E' O UNICO ACESSO DO OPERADOR A ESTE EIXO. Os outros cinco eixos
# tem linha no `EIXOS_UI` (com `trocar` e cadeado); as MAOS nao tem, porque
# neste angulo elas nao sao um adereco — sao O NARRADOR, e o narrador nao
# aparecia no painel. Este menu e a primeira porta.
# ⛔ POR QUE DROPDOWN E NAO `TRAVAS_UI`: aquela barra desenha UM BOTAO POR
# OPCAO, lado a lado. Serve para as 4 familias de banheiro; com 22 pares de
# maos ela estoura a largura da janela.
# ⚠️ O campo exibido e' `rotulo` e NAO `desc`: o `desc` e' ingles de prompt
# ("clean broad hands with short trimmed nails and smooth skin", 57 chars) e
# nao cabe no combobox. O `ui_agente` monta o mapa rotulo -> id, entao o
# operador escolhe "largas + relogio de aco no pulso" e o motor recebe
# `relogio_aco`.
DROPDOWNS_UI = [("maos", "AS MAOS", "MAOS", "rotulo")]

# ⚠️ `banheiro` e `receita` provam-se por outros literais que nao o campo do
# painel (`cen` e `vaso`), entao ficam de fora da lente de honestidade.
IGNORA_PAINEL = ("banheiro", "receita")

# ⛔ Nenhum eixo do painel mexe na copy: a fala nao cita o banheiro, a
# superficie, a medida nem o recipiente. Declarar o dicionario vazio e'
# declarar que alguem verificou, em vez de deixar o `getattr` decidir.
def _coerir_cena(spec, rng):
    """⛔⛔ REPARA A COERENCIA banheiro <-> superficie depois de uma troca de eixo.

    ⚠️ DEFEITO MEDIDO em 2026-08-14, simulando o painel: clicar em `trocar`
    na linha O BANHEIRO deixava **34 de 40 videos invalidos** — a BA8 acusando
    *"superficie X nao existe no banheiro Y"*. Os dois eixos sao ACOPLADOS (cada
    banheiro declara quais superficies existem nele) e o painel os tratava como
    independentes, porque a UI compartilhada nao tem como saber do acoplamento.
    ⭐ O autoteste passava em 400 sorteios e nunca via isto: SORTEAR e' so'
    metade do que o operador faz. O que ele faz depois — trocar eixo, travar,
    re-sortear cena — nao era exercitado por lente nenhuma.

    ⚠️ E O NOME DO GANCHO E' MAIS ESTREITO QUE A FUNCAO DELE. A UI chama
    isto de `EIXOS_QUE_MEXEM_NA_COPY`, mas o que ela executa e' *"deixe o motor
    consertar o spec depois que este eixo mudou"* — e coerencia de cena e' um
    conserto tao legitimo quanto reescrever fala. Registrado aqui para ninguem
    "limpar" isto achando que e' uso errado.

    ⚠️ 1 dos 24 banheiros tem uma superficie so'. Nele, clicar em `trocar`
    na SUPERFICIE devolve a mesma — mudo, mas coerente. O contrario (mudar e
    ficar incoerente) e' pior.
    """
    ok = [x for x in SUPERFICIES if x["id"] in spec["banheiro"]["sups"]]
    if not ok:
        return
    if spec["superficie"]["id"] not in spec["banheiro"]["sups"]:
        outras = [x for x in ok if x["id"] != spec["superficie"]["id"]] or ok
        spec["superficie"] = rng.choice(outras)


EIXOS_QUE_MEXEM_NA_COPY = {"banheiro": _coerir_cena,
                           "superficie": _coerir_cena}


def resumo_pt(spec):
    return ("16s, DOIS takes, %s. Take 1 — %s: os props em %s (%s, caixa de "
            "gelatina e colher de mel), %s ao lado INTOCADA, %s na parede; %s. "
            "Take 2 — O PREPARO: mais perto, o sache despeja o po no "
            "recipiente e o mel entra; a medida e o rotulo continuam em "
            "quadro. A fala nomeia o orgao como %s e fecha no CTA GELATIN + "
            "follow. Idade falada: %d."
            % (spec["banheiro"]["id"].replace("_", " "),
               "A IDADE" if spec["abertura"] == "idade" else "O AVISO",
               spec["superficie"]["curto"], spec["receita"]["curto"],
               spec["medida"]["curto"], spec["rotulo"]["curto"],
               ("um homem de %d anos passando o creme na propria nuca (MODO "
                "PESSOA LIGADO)" % spec["homem"]["idade"]) if spec["pessoa"]
               else "so' as MAOS entram em quadro (modo pessoa desligado)",
               spec["apelido"], spec["idade"]))


# ===========================================================================
# AUTOTESTE
# ===========================================================================

def autoteste(n=400):
    import collections
    pags = sorted(ETNIA)
    erros = collections.Counter()
    dist = collections.defaultdict(set)
    tam = collections.defaultdict(list)
    eixos = collections.defaultdict(set)
    falhas, avisos = [], 0

    for i in range(n):
        modo = {"pessoa": True} if i % 4 == 0 else {}
        s = sortear(pags[i % len(pags)], random.Random(i), {}, modo)
        b = montar(s)
        for e in ("banheiro", "superficie", "medida", "rotulo", "receita",
                  "maos"):
            eixos[e].add(s[e]["id"])
        eixos["abertura"].add(s["abertura"])
        eixos["apelido"].add(s["apelido"])
        eixos["idade"].add(s["idade"])
        for c, f in enumerate(s["falas"], 1):
            dist[c].add(f)
            tam[c].append(_palavras(f))
        for nivel, msg in lint(s, b):
            if nivel == "ERRO":
                erros[msg[:70]] += 1
            else:
                avisos += 1

    print("BANHO 16 — %d sorteios (modo pessoa ligado em 1 de 4)" % n)
    for c in sorted(dist):
        v = sorted(tam[c])
        print("  cena %d: %d falas distintas · palavras min/med/max %d/%d/%d"
              % (c, len(dist[c]), v[0], v[len(v) // 2], v[-1]))
    for e in ("banheiro", "superficie", "medida", "rotulo", "receita", "maos",
              "abertura", "apelido", "idade"):
        print("  %-11s %d valores" % (e, len(eixos[e])))
    print("  linter: %d ERRO, %d AVISO" % (sum(erros.values()), avisos))
    for k, v in erros.most_common(5):
        print("     %3dx %s" % (v, k))

    # ⭐ [ALCANCE] — entrada que nao cabe com os minimos dos outros beats nunca
    # e' sorteada. Nao e' rara: e' MORTA, e o autoteste a contaria como viva.
    for rot, pool, cena, outros in (
            ("IDADES_HACK", IDADES_HACK, 1, [QUANDOS, PROMESSAS]),
            ("QUANDOS", QUANDOS, 1, [IDADES_HACK, PROMESSAS]),
            ("PROMESSAS", PROMESSAS, 1, [IDADES_HACK, QUANDOS]),
            ("AVISOS_SOLTEIRO", AVISOS_SOLTEIRO, 1, [AVISOS_CASADO, ELAS]),
            ("AVISOS_CASADO", AVISOS_CASADO, 1, [AVISOS_SOLTEIRO, ELAS]),
            ("ELAS", ELAS, 1, [AVISOS_SOLTEIRO, AVISOS_CASADO]),
            ("MECANISMOS", MECANISMOS, 2, [CTAS, FOLLOWS]),
            ("CTAS", CTAS, 2, [MECANISMOS, FOLLOWS]),
            ("FOLLOWS", FOLLOWS, 2, [MECANISMOS, CTAS])):
        reserva = sum(_mn(p) for p in outros)
        mortas = [x for x in pool
                  if _palavras(_amostra(x).format(o="manhood")
                               if "{o}" in x else _amostra(x)) + reserva
                  > TETO_FALA[cena]]
        if mortas:
            falhas.append("[ALCANCE] %s: %d de %d nunca sao sorteadas (teto "
                          "real %d palavras)"
                          % (rot, len(mortas), len(pool),
                             TETO_FALA[cena] - reserva))

    # ⛔ CONTRATO DO MECANISMO: literal do funil + verbo de efeito + alvo, os
    # tres na MESMA entrada (CT3). Uma entrada sem o alvo passaria em ~1/10 dos
    # sorteios e o espectador nao saberia do que se trata.
    for x in MECANISMOS:
        baixo = x.lower()
        if "gelatin trick" not in baixo:
            falhas.append("CT3: %r sem o literal `gelatin trick`" % x)
        if not any(re.search(r"\b%s\b" % v, baixo) for v in sc.VERBOS_EFEITO_16):
            falhas.append("CT3: %r sem VERBO de efeito" % x)
        if not any(a in baixo for a in sc.ALVOS_16):
            falhas.append("CT3: %r sem ALVO de sc.ALVOS_16" % x)
        if "{o}" not in x:
            falhas.append("BA5: %r sem o slot do apelido" % x)
        if sc.ERECAO_16.search(x.format(o="Johnson")):
            falhas.append("BA6/CT7: %r junta orgao e verbo de ereccao" % x)
    com_ing = [x for x in MECANISMOS + CTAS + FOLLOWS
               if sc.INGREDIENTES_16.search(x)]
    if com_ing:
        falhas.append("CT5: %d entrada(s) nomeiam ingrediente: %s"
                      % (len(com_ing), com_ing[:1]))
    for x in CTAS:
        if "Comment recipe," not in x:
            falhas.append("CT6/D2: %r sem `Comment recipe,` — a automacao de "
                          "DM casa palavra exata" % x)
    for x in FOLLOWS:
        if re.search(r"\b(or|otherwise|unless)\b", x, re.I):
            falhas.append("BA7: %r transforma o follow em condicao" % x)
    for x in AVISOS_SOLTEIRO + AVISOS_CASADO + ELAS + PROMESSAS + QUANDOS:
        if any(t.lower() in x.lower() for t in NUCLEO):
            falhas.append("BA5: %r nomeia o orgao no take 1 — o apelido so' "
                          "existe no take 2 neste agente" % x)

    # ⭐⭐ CONTROLES NEGATIVOS. Lente que nunca acusou e' lente que ninguem sabe
    # se funciona, e as sete nasceram hoje.
    s0 = sortear("joe", random.Random(7), {}, {})
    b0 = montar(s0)

    def _prova(fn, spec_t, blocos_t):
        p = []
        fn(spec_t, blocos_t, p)
        return bool(p)

    controles = [
        ("BA1 sem a medida na IMAGE 02", _ba1_medida, s0,
         dict(b0, **{"IMAGE 02/02": "a wet tiled wall"}), True),
        ("BA1 limpo", _ba1_medida, s0, b0, False),
        ("BA2 sem o rotulo", _ba2_rotulo, s0,
         dict(b0, **{"IMAGE 01/02": "a shower with a jar"}), True),
        ("BA2 limpo", _ba2_rotulo, s0, b0, False),
        ("BA3 com homem e modo desligado", _ba3_sem_pessoa, s0,
         dict(b0, **{"IMAGE 01/02": b0["IMAGE 01/02"]
                     + " A man stands beside the tub."}),
         True),
        ("BA3 limpo", _ba3_sem_pessoa, s0, b0, False),
        ("BA5 com pecker na fala", _ba5_apelido,
         dict(s0, falas=[s0["falas"][0],
                         "The gelatin trick feeds blood back to your pecker."]),
         b0, True),
        ("BA5 limpo", _ba5_apelido, s0, b0, False),
        ("BA6 orgao + ereccao na mesma sentenca", _ba6_leve,
         dict(s0, falas=[s0["falas"][0],
                         "It makes your Johnson hard again."]), b0, True),
        ("BA6 limpo", _ba6_leve, s0, b0, False),
        ("BA7 follow como condicao", _ba7_follow,
         dict(s0, falas=[s0["falas"][0],
                         "Comment recipe, and follow me or it will not send."]),
         b0, True),
        ("BA7 limpo", _ba7_follow, s0, b0, False),
    ]
    for rotulo, fn, spec_t, blocos_t, deve in controles:
        # ⚠️ A mensagem diz o que ACONTECEU, nao o que se esperava. A primeira
        # versao imprimia "a lente passou (esperado: passar)" numa falha, que
        # e' texto sem informacao — bug de relatorio esconde bug de codigo.
        obtido = _prova(fn, spec_t, blocos_t)
        if obtido != deve:
            falhas.append("CONTROLE %s: a lente %s (esperado: %s)"
                          % (rotulo, "acusou" if obtido else "passou",
                             "acusar" if deve else "passar"))

    # ⛔ TODO BANHEIRO PRECISA DE SUPERFICIE COMPATIVEL, senao o `or SUPERFICIES`
    # do sorteio devolve o incompativel em silencio e a BA8 acusa 100%.
    for b_ in BANHEIROS:
        ok = [x for x in SUPERFICIES if x["id"] in b_["sups"]]
        if len(ok) < 1:
            falhas.append("BANHEIRO %s: nenhuma superficie compativel" % b_["id"])
        for sid in b_["sups"]:
            if sid not in [x["id"] for x in SUPERFICIES]:
                falhas.append("BANHEIRO %s: `sups` cita %r, que nao existe em "
                              "SUPERFICIES" % (b_["id"], sid))

    # ⛔ O MODO PESSOA TEM DE MOVER. Toggle que nao muda nada e' forma sem
    # funcao — o repo ja' pagou isso tres vezes.
    sem = montar(sortear("joe", random.Random(3), {}, {}))["IMAGE 01/02"]
    com = montar(sortear("joe", random.Random(3), {}, {"pessoa": True}))["IMAGE 01/02"]
    if sem == com:
        falhas.append("MODO PESSOA: ligado e desligado produzem a MESMA IMAGE")

    # ⚠️ O piso e' o TAMANHO DO POOL, lido do proprio pool — numero cravado a
    # mao vira falso alarme no dia em que uma entrada sai (foi o que aconteceu
    # quando o `box_pedra` foi removido: 8 virou 7 e o autoteste reprovou o
    # certo).
    for e, minimo in (("banheiro", len(BANHEIROS)),
                      ("superficie", len(SUPERFICIES)), ("medida", len(MEDIDAS)),
                      ("rotulo", len(ROTULOS)), ("receita", len(RECEITAS)),
                      ("maos", len(MAOS)),
                      ("abertura", 2)):
        if len(eixos[e]) < minimo:
            falhas.append("EIXO %s: so' %d valores em %d sorteios (pool tem %d)"
                          % (e, len(eixos[e]), n, minimo))

    # ⛔⛔ O CONTRATO DO `rotulo` — as tres coisas que o dropdown exige, e a
    # quarta que o `DROPDOWNS_UI` exige.
    # ⚠️ A UNICIDADE nao e' capricho: o `ui_agente._barra_dropdowns` monta o
    # mapa com `if txt and txt not in mapa`, entao dois rotulos iguais fazem o
    # SEGUNDO par de maos DESAPARECER do menu — em silencio, sem erro, sem log.
    # Pool de 22 que o operador so' alcanca em 21 e' a familia do botao que
    # mente, por colisao de texto.
    # ⚠️ O TETO DE 42 e' a largura do combobox (`width=38` + folga): rotulo
    # maior fica cortado na tela, e rotulo cortado volta a ser ilegivel — que e'
    # exatamente o problema que ele veio resolver.
    _rot = [x.get("rotulo") or "" for x in MAOS]
    _sem = [x["id"] for x in MAOS if not x.get("rotulo")]
    if _sem:
        falhas.append("ROTULO: %d entrada(s) de MAOS sem rotulo — o dropdown "
                      "cai no `id` e o operador le' %r" % (len(_sem), _sem[0]))
    _rep = sorted({r for r in _rot if _rot.count(r) > 1})
    if _rep:
        falhas.append("ROTULO: %d rotulo(s) repetido(s) (%r) — o segundo par "
                      "some do dropdown sem erro nenhum" % (len(_rep), _rep[0]))
    _longos = [r for r in _rot if len(r) > 42]
    if _longos:
        falhas.append("ROTULO: %d rotulo(s) acima de 42 chars (%r, %d) — "
                      "estoura a largura do menu"
                      % (len(_longos), _longos[0], len(_longos[0])))
    # ⛔ E O `DROPDOWNS_UI` TEM DE APONTAR PARA COISA QUE EXISTE. O `ui_agente`
    # le' o pool com `getattr(motor, nome, [])`: nome errado devolve LISTA VAZIA
    # e o menu nasce so' com `livre` — seletor que existe e nao seleciona.
    for _ch, _lbl, _pool_nome, _campo in DROPDOWNS_UI:
        _p = globals().get(_pool_nome)
        if not isinstance(_p, list) or not _p:
            falhas.append("DROPDOWNS_UI: o pool %r nao existe no motor — o "
                          "menu nasce vazio" % _pool_nome)
            continue
        if _ch not in EIXOS_TRAVAVEIS:
            falhas.append("DROPDOWNS_UI: o eixo %r nao esta' em "
                          "EIXOS_TRAVAVEIS" % _ch)
        _faltam = [x for x in _p if not str(x.get(_campo) or "")]
        if _faltam:
            falhas.append("DROPDOWNS_UI: %d entrada(s) de %s sem o campo %r"
                          % (len(_faltam), _pool_nome, _campo))

    # ⛔⛔ E O DROPDOWN TEM DE FIXAR DE VERDADE. E' a lente de FUNCAO: as tres
    # de cima olham a FORMA do rotulo, e forma sem funcao e' o defeito §41.
    # ⚠️ Ela usa a mesma porta que o painel usa (`travas["maos"]` com o `id`
    # que o mapa do combobox devolve), nao uma porta de teste.
    for _alvo in (MAOS[0]["id"], MAOS[len(MAOS) // 2]["id"], MAOS[-1]["id"]):
        _vistos = {sortear(pags[k % len(pags)], random.Random(500 + k), {},
                           {"maos": _alvo})["maos"]["id"] for k in range(8)}
        if _vistos != {_alvo}:
            falhas.append("DROPDOWN: travar `maos` em %r devolveu %r — o menu "
                          "promete e o sorteio ignora" % (_alvo, sorted(_vistos)))
            break

    # ⛔ E O ROTULO NUNCA CHEGA AO PROMPT. Ele e' portugues; um vazamento poria
    # "largas + relogio de aco no pulso" dentro de um bloco IMAGE em ingles, e o
    # Veo desenharia o texto. A lente e' de AUSENCIA, e por isso varre o POOL
    # INTEIRO passando pelo quadro — um sorteio so' mediria a sorte da seed.
    for _i, _m in enumerate(MAOS):
        _bj = " ".join(montar(sortear(pags[_i % len(pags)],
                                      random.Random(900 + _i), {},
                                      {"maos": _m["id"]})).values())
        if _m["rotulo"] in _bj:
            falhas.append("ROTULO: o texto de painel %r vazou para um bloco do "
                          "prompt — ele e' portugues e o Veo desenha texto"
                          % _m["rotulo"])
            break

    # ⭐⭐ CONTROLES NEGATIVOS DAS TRAVAS DE ROTULO. Lente que nunca acusou e'
    # lente que ninguem sabe se funciona. ⚠️ Sabotagem em COPIA do pool: mexer
    # no global deixaria o motor sujo se o autoteste morresse no meio.
    def _falhas_rot(pool):
        r = [x.get("rotulo") or "" for x in pool]
        return ([x for x in pool if not x.get("rotulo")]
                or [t for t in r if r.count(t) > 1]
                or [t for t in r if len(t) > 42])

    for _nome, _sujo in (
            ("rotulo vazio", [dict(MAOS[0], rotulo="")] + MAOS[1:]),
            ("rotulo repetido",
             [dict(MAOS[0], rotulo=MAOS[1]["rotulo"])] + MAOS[1:]),
            ("rotulo de 43 chars", [dict(MAOS[0], rotulo="x" * 43)] + MAOS[1:])):
        if not _falhas_rot(_sujo):
            falhas.append("CONTROLE %s: a trava de rotulo NAO acusou o pool "
                          "sabotado" % _nome)
    if _falhas_rot(MAOS):
        falhas.append("CONTROLE pool limpo: a trava de rotulo acusou o pool "
                      "de verdade")

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
    ap.add_argument("--cenario", choices=FAMILIAS_BANHEIRO)
    ap.add_argument("--abertura", choices=["idade", "aviso"])
    ap.add_argument("--pessoa", action="store_true",
                    help="MODO PESSOA: um homem em quadro no take 1 "
                         "(o padrao e' so' as maos)")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--autoteste", action="store_true")
    a = ap.parse_args()

    if a.autoteste:
        return autoteste()

    led = _carregar_ledger()
    rng = random.Random(a.seed)
    travas = {}
    if a.cenario:
        travas["familia_banheiro"] = a.cenario
    if a.abertura:
        travas["abertura"] = a.abertura
    if a.pessoa:
        travas["pessoa"] = True
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
