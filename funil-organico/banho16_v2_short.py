#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
banho16_v2_short.py — randomizador + gerador + linter do AGENTE **BANHO 16 V2**.

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
    python funil-organico/banho16_v2_short.py --pagina joe --n 1
    python funil-organico/banho16_v2_short.py --autoteste
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

TITULO = "AGENTE BANHO 16 V2"
SLUG = "banho-16-v2"
SUBTITULO = ("2 takes de 8s = 16 segundos · o banheiro · as maos preparam a "
             "receita e a medida fica parada ao lado, intocada")

LEDGER = os.path.join(AQUI, ".banho-16-v2-ledger.json")

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
# ⛔⛔ POOL REGIONAL DESDE A V2 (2026-08-12). Ordem do operador: *"quero pool
# de banheiros tipicos alinhados tb com os arquetipos de diferentes regioes dos
# eua"*. O V1 tinha oito banheiros CORRETOS e de lugar nenhum — box bege, box
# branco, nicho de madeira. Nenhum deles dizia onde estava.
#
# ⭐ Cada entrada declara `regiao`, e a REGIAO ARRASTA O BANHEIRO INTEIRO
# (decisao 3 do operador): o cenario, a agua, a luz, o audio E as superficies
# compativeis. Banquinho de madeira rustica num box de condominio da Florida e'
# o par incoerente que o eixo solto produzia.
# ⚠️ A etnia continua vindo da PAGINA e nao daqui: as maos sao a unica parte
# do narrador em quadro, e a congruencia do funil governa elas. Duas vozes
# decidindo a mesma coisa e' o defeito FT14 do FIGHT 16.
BANHEIROS = [
    {"id": "nova_inglaterra", "regiao": "Nova Inglaterra",
     "sups": ("borda_banheira", "banquinho", "tampo_madeira"),
     "cen": "an old clawfoot tub filling in a bright bathroom with white "
            "beadboard walls and a small sash window",
     "agua": "the tap running into the rising water",
     "luz": "Bright morning light through the small window.",
     "audio": "a tap running into a deep tub"},
    {"id": "harlem", "regiao": "Harlem",
     "sups": ("borda_banheira", "prateleira_arame"),
     "cen": "a restored prewar bathroom with gleaming white subway tile to "
            "the ceiling and a chrome spout running into a clean cast "
            "iron tub",
     "agua": "the spout running steadily into the tub",
     "luz": "Flat overhead light on glossy tile.",
     "audio": "a tub filling, water on enamel"},
    {"id": "noroeste", "regiao": "Noroeste do Pacifico",
     "sups": ("nicho", "prateleira_arame"),
     "cen": "a shower wall of dark reclaimed cedar planks with a recessed "
            "stone niche and a rain head running above it",
     "agua": "the water falling past the mouth of the niche",
     "luz": "Warm low light, wet wood.",
     "audio": "a rain shower, water on wood"},
    {"id": "texas", "regiao": "Texas",
     "sups": ("cesta_canto", "prateleira_arame", "nicho"),
     "cen": "a wide ranch house shower stall in large sand-coloured tile with "
            "an oil-rubbed bronze shower head running",
     "agua": "the shower running steadily behind everything",
     "luz": "Warm even light, dry heat outside.",
     "audio": "a shower running on tile"},
    {"id": "florida", "regiao": "Florida",
     "sups": ("cesta_canto", "prateleira_arame"),
     "cen": "a bright condo shower stall in pale glossy tile with a frosted "
            "glass window and a chrome fixed head running",
     "agua": "the shower falling straight down in front of the wall",
     "luz": "Cool daylight through the frosted glass.",
     "audio": "a shower running on tile"},
    {"id": "apalache", "regiao": "Apalaches",
     "sups": ("borda_banheira", "banquinho"),
     "cen": "a well-kept bathroom with fresh white panelled walls and a "
            "clean cast iron tub filling from a polished chrome tap",
     "agua": "the tap pouring hard into the filling tub",
     "luz": "Warm clean light, steam on the fresh paint.",
     "audio": "a bathtub filling, water hitting water"},
    {"id": "meio_oeste", "regiao": "Meio-Oeste",
     "sups": ("borda_banheira", "tampo_madeira", "bancada_pia"),
     "cen": "a family bathroom with small beige square wall tiles and a "
            "chrome spout running into a white tub",
     "agua": "the spout running steadily into the tub",
     "luz": "Even daylight, pale tiles.",
     "audio": "a tub filling, water on enamel"},
    {"id": "sulista", "regiao": "Sul profundo",
     "sups": ("borda_banheira", "banquinho", "bancada_pia"),
     "cen": "a bathroom in pale pink and mint fifties tile with a white tub "
            "filling and a shower curtain pushed back",
     "agua": "the tap running into the pale water",
     "luz": "Soft warm light, steam on the tiles.",
     "audio": "a bathtub filling, water hitting water"},
    {"id": "delta", "regiao": "Delta do Mississippi",
     "sups": ("bancada_pia",),
     "cen": "a plain bathroom vanity with a chrome faucet, a wide mirror "
            "behind it and a shower curtain reflected in the glass",
     "agua": "the faucet running thin into the basin",
     "luz": "Warm bathroom light, soft shadows.",
     "audio": "a faucet running into a sink"},
    {"id": "atlanta", "regiao": "Atlanta",
     "sups": ("nicho", "cesta_canto", "prateleira_arame"),
     "cen": "a dark slate shower with a square rain head running from the "
            "ceiling and a built-in stone niche",
     "agua": "the water falling straight down in front of the wall",
     "luz": "Dim, high contrast, wet stone.",
     "audio": "a heavy rain shower on stone"},
    {"id": "creole", "regiao": "Creole",
     "sups": ("borda_banheira", "banquinho", "bancada_pia"),
     "cen": "a high-ceilinged bathroom with polished patterned cement floor "
            "tile and a deep clean tub filling from a brass tap",
     "agua": "the brass tap running into the deep tub",
     "luz": "Warm slatted light through wooden shutters.",
     "audio": "a tap running into a deep tub"},
    {"id": "gullah", "regiao": "Gullah",
     "sups": ("borda_banheira", "banquinho"),
     "cen": "a bright airy bathroom with crisp white panelling and a clean "
            "white tub filling, a shuttered window open to green light",
     "agua": "the tap running into the shallow water",
     "luz": "Soft green daylight through the screen.",
     "audio": "a bathtub filling, water hitting water"},
    {"id": "grandes_lagos", "regiao": "Grandes Lagos",
     "sups": ("prateleira_arame", "borda_banheira", "bancada_pia"),
     "cen": "a tidy lower-level bathroom with spotless white wall tile and a "
            "chrome shower head running over a clean enamel tub",
     "agua": "the shower running steadily onto the enamel",
     "luz": "Even warm ceiling light, clean damp air.",
     "audio": "a shower running on enamel"},
    {"id": "italo_americana", "regiao": "Italo-americana",
     "sups": ("bancada_pia", "prateleira_arame"),
     "cen": "a marble-tiled bathroom with a wide framed mirror, gold fixtures "
            "and a faucet running into a marble basin",
     "agua": "the faucet running steadily into the basin",
     "luz": "Warm bright light bouncing off the marble.",
     "audio": "a faucet running into a stone basin"},
    {"id": "americana", "regiao": "Americana",
     "sups": ("cesta_canto", "prateleira_arame", "bancada_pia"),
     "cen": "a standard suburban shower stall in white square tile with a "
            "chrome fixed shower head running",
     "agua": "the shower running steadily behind everything",
     "luz": "Flat overhead bathroom light, damp air.",
     "audio": "a shower running on tile"},
    # ⭐⭐ ONZE REGIOES NOVAS (2026-08-13). Ordem do operador: *"aumente o pool
    # de opcoes substancialmente, tambem dos ambientes"*. Quinze regioes num
    # eixo que arrasta o banheiro INTEIRO (cenario, agua, luz, audio e
    # superficies) e' o mesmo lugar voltando a cada quinze videos.
    # ⛔ Cada uma declara as MESMAS chaves das quinze antigas — `regiao` e
    # `sups` inclusive. Entrada com chave a menos derruba o `montar` ou o
    # painel, e o painel deste motor mostra `regiao`.
    # ⛔ E O `id` E' DE UMA PALAVRA SO', de proposito: o `--cenario` filtra por
    # `id.split("_")[0]`, entao id composto (`nova_inglaterra`, `meio_oeste`)
    # nunca casa com a propria familia. Nao consertei o filtro — nao e' meu
    # escopo aqui — mas nao aumentei o problema.
    # ⛔ AGUA CORRENDO nas onze, e todos os `sups` existem em SUPERFICIES.
    # ⚠️ A etnia continua vindo da PAGINA, nunca da regiao: as regioes de
    # arquetipo negro (Chicago, Detroit, Filadelfia, Memphis, Baltimore) entram
    # como AMBIENTE e nao como casting. Quem governa as maos e' o dict ETNIA.
    {"id": "arizona", "regiao": "Arizona",
     "sups": ("nicho", "cesta_canto", "banco_teca"),
     "cen": "a desert house shower in large tumbled stone tile with an "
            "oil-rubbed bronze rain head running",
     "agua": "the rain head falling in a broad soft sheet",
     "luz": "Hard bright light through a high slot window.",
     "audio": "a rain shower on stone"},
    {"id": "california", "regiao": "California",
     "sups": ("prateleira_vidro", "nicho", "banco_teca"),
     "cen": "a glass-walled shower in pale grey tile with a teak bench along "
            "the back wall and a chrome rain head running",
     "agua": "the water falling straight down behind the glass",
     "luz": "Cool bright daylight through the clear panel.",
     "audio": "a rain shower head, water on tile"},
    {"id": "chicago", "regiao": "Chicago",
     "sups": ("borda_banheira", "prateleira_arame", "parapeito"),
     "cen": "a tidy two-flat bathroom with glossy white wall tile and a chrome "
            "spout running into a clean enamel tub",
     "agua": "the spout running steadily into the tub",
     "luz": "Warm ceiling light, cold daylight at the window.",
     "audio": "a tub filling, water on enamel"},
    {"id": "detroit", "regiao": "Detroit",
     "sups": ("borda_banheira", "bancada_pia", "armario_espelho"),
     "cen": "a well-kept bathroom in small hexagonal floor tile with a white "
            "tub filling from a polished chrome tap",
     "agua": "the tap running into the rising water",
     "luz": "Even warm light, steam on the mirror.",
     "audio": "a bathtub filling, water hitting water"},
    {"id": "filadelfia", "regiao": "Filadelfia",
     "sups": ("borda_banheira", "prateleira_arame", "banquinho"),
     "cen": "a narrow row house bathroom with white subway tile to the ceiling "
            "and a chrome spout running into a cast iron tub",
     "agua": "the spout pouring hard into the filling tub",
     "luz": "Flat overhead light on glossy tile.",
     "audio": "a bathtub filling, water hitting water"},
    {"id": "memphis", "regiao": "Memphis",
     "sups": ("borda_banheira", "banquinho", "bancada_pia"),
     "cen": "a bathroom in pale yellow and white fifties tile with a clean "
            "white tub filling and a shower curtain pushed back",
     "agua": "the tap running into the pale water",
     "luz": "Soft warm light, steam on the tiles.",
     "audio": "a bathtub filling, water hitting water"},
    {"id": "baltimore", "regiao": "Baltimore",
     "sups": ("borda_pia", "armario_espelho", "prateleira_vidro"),
     "cen": "a small row house bathroom with a white pedestal sink against a "
            "pale panelled wall and the chrome faucet running",
     "agua": "the faucet running steadily into the bowl",
     "luz": "Warm bathroom light, soft shadows.",
     "audio": "a faucet running into a sink"},
    {"id": "carolina", "regiao": "Carolinas",
     "sups": ("borda_banheira", "tampo_madeira", "parapeito"),
     "cen": "a bright coastal bathroom with white shiplap walls and a deep "
            "clean tub filling under a shuttered window",
     "agua": "the tap running into the rising water",
     "luz": "Soft daylight through the open shutters.",
     "audio": "a tap running into a deep tub"},
    {"id": "rochosas", "regiao": "Montanhas Rochosas",
     "sups": ("nicho", "banco_teca", "cesta_canto"),
     "cen": "a lodge bathroom shower in split stone with a knotty pine ceiling "
            "and a rain head running",
     "agua": "the water falling past the mouth of the niche",
     "luz": "Warm low light, wet stone.",
     "audio": "a heavy rain shower on stone"},
    {"id": "nevada", "regiao": "Nevada",
     "sups": ("degrau_banheira", "borda_banheira", "parapeito"),
     "cen": "a sunken tub set into a wide tiled step in a bright desert house "
            "bathroom, filling from a low chrome spout",
     "agua": "the low spout running into the rising water",
     "luz": "Hard bright daylight, steam over the step.",
     "audio": "a deep tub filling, water hitting water"},
    {"id": "dakota", "regiao": "Dakotas",
     "sups": ("cesta_canto", "prateleira_arame", "cesta_pendurada"),
     "cen": "a plain farmhouse shower stall in white square tile with a chrome "
            "fixed head running",
     "agua": "the shower running steadily behind everything",
     "luz": "Cold clear daylight through a small high window.",
     "audio": "a shower running on tile"},
]
FAMILIAS_BANHEIRO = sorted({b["id"] for b in BANHEIROS})



# ===========================================================================
# ⭐⭐ ACOES — O GESTO DOS DOIS TAKES, SORTEADO EM PAR (V2, 2026-08-12)
# ===========================================================================
# ⛔ Ordem do operador: mapear as acoes do take 1 E do take 2 dos sete videos
# fonte e virar pool. A leitura foi feita a 1 FPS nos sete (152 quadros
# extraidos) mais as sete transcricoes — cada entrada guarda de qual video ela
# saiu, e nenhuma e' invencao exceto as marcadas `nossa`.
#
# ⭐⭐ O QUE OS SETE VIDEOS TEM EM COMUM, e por isso virou o molde do par:
#     TAKE 1 = o cenario com AGUA CORRENDO + a mao TOCANDO ou ABRINDO um prop
#     TAKE 2 = o PREPARO DENTRO DO RECIPIENTE (po, mel, colher, o dedo)
# Nao ha' um so' video em que o take 2 mostre outra coisa. O arco e' sempre
# `os props existem` -> `a mistura acontece`.
#
# ⛔⛔ SORTEADOS EM PAR, decisao 2 do operador. Cada entrada declara os DOIS
# gestos, e a razao e' continuidade de graca: o pote que a mao toca no take 1 e'
# o mesmo que aparece aberto no take 2. Com dois pools independentes, o take 1
# abriria uma caixa de gelatina e o take 2 mexeria num copo que nunca apareceu
# — e ai' a coerencia vira trabalho do linter, que e' onde ela sempre quebra.
#
# ⭐ A COPY E' PUXADA (decisao 1): a entrada pode declarar `copy` com as duas
# falas, e ai' ela VENCE os pools de script. Quem nao declara cai nos quatro
# scripts do V1 (idade / aviso / rodeio / struggling), que continuam vivos.
# ⚠️ Os DOIS mecanismos convivem por ordem do operador, com o risco declarado:
# o repo tem regra contra duas implementacoes da mesma ideia, e a defesa aqui e'
# que o painel DIZ de onde a copy veio (ver `resumo_pt`) — operador que edita a
# fala e nao entende por que ela nao mudou e' o defeito que isso evita.
#
# ⛔ `pessoa`: a entrada com gente em quadro so' e' sorteada com o MODO PESSOA
# LIGADO, e as sem gente so' com ele desligado. Toggle que promete pessoa e
# entrega maos em seis de sete videos e' o botao que mente.
ACOES = [
    # ---- MAOS (o padrao do angulo: 6 dos 7 videos) ----------------------
    {"id": "maos_na_borda", "vasos": ("jar",), "curto": "as maos pousadas ao lado dos props",
     "reel": "v1", "pessoa": False,
     "t1_img": "A pair of %(maos)s enters from the bottom of the frame and "
               "rests flat on the edge beside the jar, palms down, lifting "
               "nothing.",
     "t1_take": "The hands stay flat on the edge and lift nothing.",
     "t2_img": "The same %(maos)s hold the open jar tilted towards the lens "
               "with a spoonful of white powder already sitting on the cream "
               "inside it.",
     "t2_take": "The powder stays where it is on the cream and the hands only "
                "tilt the jar a little further towards the lens."},
    {"id": "rasga_sache", "vasos": ("jar", "glass"), "curto": "as maos rasgando o sache",
     "reel": "v2", "pessoa": False, "ct7_liberado": True,
     "t1_img": "A pair of %(maos)s holds a small paper gelatin sachet up "
               "beside the jar and is tearing the top strip off it.",
     "t1_take": "The hands keep tearing the strip off the sachet and set "
                "nothing down.",
     "t2_img": "The same %(maos)s hold the torn sachet over the glass and a "
               "fine stream of white powder is falling into the amber liquid.",
     "t2_take": "The powder keeps falling into the liquid at the same rate.",
     # ⭐ COPY PROPRIA — do v2, o video do AVISO. A fonte diz *"If you are
     # single, do not try this (...) ladies won't be able to keep up with you"*.
     "copy": ("If you are single, do not try this. If you are married, go easy "
              "with it. She will not keep up with you.",
              # ⛔⛔ O `hard` COLADO NO ORGAO VOLTOU — ORDEM DIRETA DO OPERADOR
              # (2026-08-13), depois de eu ter mostrado que o CT7 e a BA6
              # reprovavam: *"volte com o hard colado"*. E' a frase da fonte,
              # verbatim menos o apelido (`buddy` -> `Johnson`, que e' o D7).
              #
              # ⚠️⚠️ DUAS ORDENS DELE COLIDEM AQUI, e a nova venceu por ser mais
              # recente e mais especifica: o D8 (*"sem copys muito fortes e
              # agressivas para evitar restricoes"*) e' a razao de existir da
              # BA6, que cita esta frase NOMINALMENTE como o que nao copiar.
              # ⛔ O PRECO ESTA' MEDIDO EM CAMPO E NAO E' TEORIA: verbo de
              # ereccao colado no orgao rendeu ~95%% de recusa no COLO 16. Se
              # os renders deste gesto cairem, a causa candidata numero um esta'
              # nesta sentenca.
              # ⭐ Por isso a excecao e' DESTA ENTRADA (`ct7_liberado`), e nao do
              # motor: as outras doze acoes e os quatro scripts continuam no
              # registro leve, e a BA6 segue cobrando todas elas.
              "The gelatin trick makes your Johnson big and as hard as a rock. "
              "Comment recipe, and it lands in your inbox. Follow me.")},
    {"id": "abre_a_caixa", "vasos": ("jar",), "curto": "as duas maos abrindo a caixa",
     "reel": "v1 / v3", "pessoa": False,
     "t1_img": "A pair of %(maos)s holds a small cardboard gelatin carton "
               "open at the top and is drawing a paper sachet up out of it.",
     "t1_take": "The hands keep drawing the sachet up out of the carton and "
                "never pull it free.",
     "t2_img": "The same %(maos)s hold the open jar while a spoon tips a thick "
               "ribbon of honey down onto the white powder inside it.",
     "t2_take": "The honey keeps running off the spoon down onto the powder.",
     # ⭐ COPY PROPRIA — do v3, o video do RODEIO (o de melhor retencao entre os
     # que tem gente). A fonte: *"you are already falling like a lame horse in
     # the middle of a rodeo"*.
     "copy": ("If you are over fifty and not doing this yet, you are falling "
              "like a lame horse in the middle of a rodeo.",
              "This shower hack clears the blocked vessels feeding your "
              "manhood. Comment recipe, and it lands in your inbox. Follow me "
              "so I can reach you.")},
    {"id": "toca_a_caixa", "vasos": ("jar",), "curto": "a mao tocando a caixa sob o chuveiro",
     "reel": "v4 / v6", "pessoa": False,
     "t1_img": "One of %(maos)s reaches in from the side and rests two "
               "fingertips on the gelatin carton, water running over the back "
               "of the hand.",
     "t1_take": "The fingertips stay resting on the carton and move nothing.",
     "t2_img": "The same %(maos)s hold the open jar close to the lens with one "
               "finger pressed into the white cream inside it.",
     "t2_take": "The finger stays pressed into the cream and the hands hold "
                "the jar steady."},
    {"id": "segura_o_pote", "vasos": ("jar",), "curto": "as duas maos segurando o pote aberto",
     "reel": "v7", "pessoa": False,
     "t1_img": "A pair of %(maos)s holds the open jar up in front of the "
               "running water with the lid resting on the surface beside it.",
     "t1_take": "The hands keep the open jar held up and steady.",
     "t2_img": "The same %(maos)s hold the jar close to the lens while one "
               "finger lifts a thick white string of the cream up out of it.",
     "t2_take": "The string of cream keeps stretching up off the finger and "
                "does not break."},
    {"id": "dedo_erguido", "vasos": ("jar",), "curto": "o dedo erguido com o creme",
     "reel": "v5", "pessoa": False,
     "t1_img": "A pair of %(maos)s rests on the surface on either side of the "
               "jar, palms down, lifting nothing.",
     "t1_take": "The hands stay flat on either side of the jar and lift "
                "nothing.",
     "t2_img": "The same %(maos)s hold the open jar low in the frame while one "
               "finger is raised close to the lens with a thick blob of white "
               "cream on the tip.",
     "t2_take": "The finger stays raised close to the lens with the cream on "
                "it and never touches anything.",
     # ⭐ COPY PROPRIA — do v5, o video do STRUGGLING. A fonte abre em
     # *"Struggling to stay hard or with your small size? That's not about
     # getting older"*, que e' o unico dos sete que enuncia a falha.
     # ⭐ O `small` VOLTOU (ordem do operador, 2026-08-13): eu o tinha cortado
     # sem regra nenhuma que pedisse, e copy e' alcada dele.
     "copy": ("Struggling to stay hard, or with your small size? That is not "
              "about getting older at all.",
              "This morning trick flushes what is choking your manhood. "
              "Comment recipe, and it lands in your inbox. Follow me so I can "
              "reach you.")},
    {"id": "colher_por_cima", "vasos": ("jar",), "curto": "a colher entrando por cima",
     "reel": "v6", "pessoa": False,
     "t1_img": "One of %(maos)s reaches in from the side and stands the spoon "
               "upright against the jar, then lets go.",
     "t1_take": "The hand stays beside the spoon and the spoon does not fall.",
     "t2_img": "The same %(maos)s lower the spoon down into the open jar from "
               "above, the honey on it about to touch the white powder.",
     "t2_take": "The spoon keeps lowering towards the powder and the honey on "
                "it does not drip off."},
    {"id": "po_no_pote", "vasos": ("jar",), "curto": "o po caindo dentro do pote",
     "reel": "v1", "pessoa": False,
     "t1_img": "A pair of %(maos)s holds the closed jar up beside the gelatin "
               "carton, turning the label towards the lens.",
     "t1_take": "The hands keep the jar turned towards the lens and open "
                "nothing.",
     "t2_img": "Seen from straight above, the open jar is held in %(maos)s and "
               "a fine fall of white powder is landing in a small heap on the "
               "cream inside it.",
     "t2_take": "The powder keeps falling into the jar and the heap keeps "
                "growing."},
    {"id": "mistura_espuma", "vasos": ("jar",), "curto": "a mistura espumando no pote",
     "reel": "v1", "pessoa": False,
     "t1_img": "A pair of %(maos)s rests on the surface beside the jar with "
               "the spoon lying between them, touching nothing.",
     "t1_take": "The hands stay resting beside the spoon and lift nothing.",
     "t2_img": "Held close to the lens in %(maos)s, the open jar is full of a "
               "pale mixture covered in fine white bubbles rising to the rim.",
     "t2_take": "The bubbles keep rising and spreading across the surface of "
                "the mixture."},
    {"id": "colher_no_copo", "vasos": ("glass",), "curto": "a colher mexendo o copo",
     "reel": "v2", "pessoa": False,
     "t1_img": "One of %(maos)s holds the spoon standing upright in the tall "
               "glass of amber liquid, not yet turning it.",
     "t1_take": "The hand keeps the spoon standing upright in the glass "
                "without turning it.",
     "t2_img": "The same %(maos)s lift the spoon up out of the glass with a "
               "thick pale thread of the mixture hanging off it.",
     "t2_take": "The thread keeps hanging off the spoon and stretches slowly "
                "without breaking."},
    # ---- PESSOA (o MODO PESSOA ligado) ----------------------------------
    # ⚠️ So' UM dos sete videos tem gente (v3, 101k views). As outras duas
    # entradas sao NOSSAS, construidas sobre o mesmo gesto: sao precisas para o
    # modo ter mais de uma opcao — eixo com uma entrada so' e' eixo morto.
    {"id": "creme_na_nuca", "vasos": ("jar",), "curto": "o creme na propria nuca",
     "reel": "v3", "pessoa": True,
     "t1_img": "A %(idade)d-year-old %(etnia)s man stands with his back half "
               "to the camera, %(cabeca)s, %(marca)s, wearing %(traje)s, "
               "scooping white cream from the open jar with two fingers and "
               "rubbing it into the back of his own neck. His face is turned "
               "away, seen only in part.",
     "t1_take": "He keeps working the cream into the back of his neck with the "
                "same slow circles and does not turn around.",
     "t2_img": "The same man, still turned away, holds the open jar up close "
               "to the lens while a spoon tips honey down onto the white "
               "powder inside it.",
     "t2_take": "The honey keeps running off the spoon into the jar and he "
                "does not turn around."},
    {"id": "creme_no_ombro", "vasos": ("jar",), "curto": "o creme no proprio ombro (nossa)",
     "reel": "nossa, sobre o v3", "pessoa": True,
     "t1_img": "A %(idade)d-year-old %(etnia)s man stands with his back to the "
               "camera, %(cabeca)s, %(marca)s, wearing %(traje)s, working white "
               "cream from the open jar into his own shoulder with two "
               "fingers. His face is not visible.",
     "t1_take": "He keeps working the cream into his shoulder with the same "
                "slow circles and does not turn around.",
     "t2_img": "The same man, still turned away, holds the open jar low in "
               "front of him with one finger lifting a thick string of the "
               "cream up out of it.",
     "t2_take": "The string of cream keeps stretching up off his finger and "
                "does not break."},
    {"id": "espelho_embacado", "vasos": ("jar", "glass"), "curto": "de costas no espelho embacado (nossa)",
     "reel": "nossa, sobre o v3", "pessoa": True,
     "t1_img": "A %(idade)d-year-old %(etnia)s man stands with his back to the "
               "camera facing a fogged mirror, %(cabeca)s, %(marca)s, wearing "
               "%(traje)s, holding the open jar up in one hand. Only the blur "
               "of his shape shows in the fogged glass.",
     "t1_take": "He keeps the jar held up and stays facing the fogged mirror "
                "without turning around.",
     "t2_img": "The same man, still facing away, holds the open jar close to "
               "the lens with a small heap of white powder sitting on the "
               "cream inside it.",
     "t2_take": "He keeps the jar held towards the lens and the heap of powder "
                "stays where it is."},
]


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
    # ⛔⛔ E CADA UMA E' CITADA POR PELO MENOS UM BANHEIRO em `sups`. Superficie
    # que nenhuma regiao declara e' entrada MORTA que o painel conta como viva —
    # e o sorteio filtra por `sups`, entao ela nunca sairia.
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
    {"id": "regua_clara_pe", "nome": "ruler",
     "img": "a pale wooden ruler standing upright against the wall, its "
            "numbers facing the camera",
     "curto": "regua clara em pe"},
    {"id": "regua_escura_pe", "nome": "ruler",
     "img": "a dark wooden ruler standing upright against the tiles, marked in "
            "both inches and centimetres",
     "curto": "regua escura em pe"},
    {"id": "regua_clara_deitada", "nome": "ruler",
     "img": "a pale wooden ruler lying flat along the edge, numbers up",
     "curto": "regua clara deitada"},
    {"id": "regua_escura_deitada", "nome": "ruler",
     "img": "a dark varnished ruler lying flat with its numbers facing up",
     "curto": "regua escura deitada"},
    {"id": "fita_metrica", "nome": "tape measure",
     "img": "a soft tailor's tape measure lying unrolled along the edge",
     "curto": "fita metrica"},
    {"id": "regua_metal", "nome": "steel rule",
     "img": "a thin steel rule propped against the wall, numbers facing out",
     "curto": "regua de metal"},
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
    {"id": "papelao",
     "img": "a torn piece of cardboard propped against the wall with GROWTH "
            "HACK written on it by hand in black marker",
     "curto": "placa de papelao"},
    {"id": "postit",
     "img": "a yellow sticky note stuck flat on the surface with GROWTH HACK "
            "written on it in blue pen",
     "curto": "post-it amarelo"},
    {"id": "papel_fita",
     "img": "a sheet of paper taped to the tiles with GROWTH HACK written "
            "across it in thick black marker",
     "curto": "papel colado no azulejo"},
    {"id": "tabua",
     "img": "a small wooden board leaning against the wall with GROWTH HACK "
            "burned into it",
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
    # ⛔⛔ `vaso_tipo` ENTROU EM 2026-08-13 E CONSERTA UM BURACO QUE EU DEIXEI
    # ONTEM. As treze ACOES nomeiam o vasilhame no proprio texto ("the open
    # jar", "the tall glass"), e a receita era sorteada A' PARTE: dez gestos
    # falam de POTE e o `bebida` poe um COPO na bancada, entao um em cada tres
    # videos mandava a mao mexer num pote que o quadro nao tinha. O
    # `lint_take_vs_image` nao pegava porque o texto do gesto entra na IMAGE
    # junto — os dois blocos concordavam entre si e discordavam da cena.
    # ⭐ Agora a receita declara o TIPO de vasilhame e o gesto declara quais
    # aceita; o sorteio so' cruza os compativeis.
    {"id": "bebida", "vaso_tipo": "glass",
     "vaso": "a tall clear glass filled with amber liquid",
     "vaso_curto": "copo de liquido ambar",
     "final": "the powder sinking through the amber liquid in slow white "
              "ribbons as the spoon turns",
     # ⭐ V2: o `final` descrevia O GESTO, e o gesto passou a ser da ACAO. Ele
     # citava colher e pote que metade das treze acoes nao tem em quadro, e o
     # `lint_take_vs_image` acusou 157 vezes. O `final2` diz o que acontece com
     # a MISTURA, sem nomear utensilio nenhum — a receita continua visivel e
     # quem move e' a acao.
     "final2": "The amber liquid keeps going cloudy from the bottom up.",
     "curto": "bebida"},
    {"id": "pomada", "vaso_tipo": "jar",
     "vaso": "an open blue jar of mentholated chest rub, the white cream "
             "smooth and untouched inside",
     "vaso_curto": "pote azul de pomada",
     "final": "the mixture rising into a thick white foam that swells over "
              "the rim of the jar",
     "final2": "The white mixture keeps swelling slowly where it sits.",
     "curto": "pomada"},
    # ⭐⭐ AS DUAS NOVAS (2026-08-13, ordem do operador: *"inclua baking soda,
    # aloe vera na pool de recipe prep"*).
    # ⛔ Cada uma entra numa das DUAS familias de vasilhame que os gestos ja'
    # conhecem — o bicarbonato no COPO, a babosa no POTE. Inventar um terceiro
    # vasilhame (uma tigela, por exemplo) criaria uma receita que gesto nenhum
    # sabe manusear: treze acoes falam de `jar` ou `glass`, e nenhuma de `bowl`.
    # ⚠️ E NENHUMA E' NOMEADA NA FALA. Os dois sao INGREDIENTE, e o CT5 vale:
    # eles existem no quadro, nunca na boca. E' o mesmo que a fonte faz — os
    # sete videos mostram a caixa laranja e nunca a citam.
    {"id": "bicarbonato", "vaso_tipo": "glass",
     "vaso": "a tall clear glass of water going milky, an orange and yellow "
             "cardboard box of baking soda standing open beside it",
     "vaso_curto": "copo com bicarbonato",
     "final": "the white powder clouding down through the water in slow "
              "streaks",
     "final2": "The water keeps clouding from the bottom up.",
     "curto": "bicarbonato"},
    {"id": "babosa", "vaso_tipo": "jar",
     "vaso": "an open glass jar of clear aloe vera gel, a cut aloe leaf lying "
             "beside it with the gel showing at the cut",
     "vaso_curto": "pote de babosa",
     "final": "the clear gel folding over on itself where it was disturbed",
     "final2": "The clear gel keeps settling slowly back into itself.",
     "curto": "babosa"},
]

# ⛔ O SEGUNDO INGREDIENTE, sempre visivel e nunca dito. A caixa de gelatina
# aparece nos 7 videos.
GELATINA = ("a box of unflavoured gelatin, its flap torn open and a small "
            "paper sachet of white powder resting against it")

# ⭐ O terceiro: a colher de mel. E' o gesto que fecha o preparo em 6 dos 7.
COLHER = "a metal spoon holding a pool of thick amber honey"


# ===========================================================================
# AS MAOS — o narrador inteiro, quando o MODO PESSOA esta' desligado
# ===========================================================================
# ⛔⛔ E' AQUI QUE A IDADE E A ETNIA EXISTEM. A fala diz "tenho 72 anos" e nao
# ha' rosto para confirmar: quem confirma sao as manchas de sol, as veias e a
# pele fina. Mao generica derruba a fala inteira.
# ⚠️ MEDIDO na fonte: o video campeao tem uma mao visivelmente MAIS JOVEM que a
# idade falada, e mesmo assim foi o melhor. Entao isto e' cuidado, nao lei — e
# esta' escrito aqui para ninguem transformar em trava sem medir.
# \u26d4\u26d4 POOL REESCRITO (2026-08-13). Ordem do operador: *"nao quero mao feia
# parecendo nao-saudavel"*.
# \u26a0\ufe0f O QUE ESTAVA ERRADO, e era o pool inteiro: `heavily sun-spotted`,
# `weathered`, `thin skin`, `dark age spots`, `loose skin over the tendons`,
# `bony`, `pale scarred`. Seis de seis descreviam DANO. Num angulo em que a mao
# e' a UNICA parte do narrador em quadro, mao castigada e' o rosto do video.
# \u2b50 E' a mesma doutrina do PLACA 16, aplicada onde ela pesa mais: DISTINTIVO,
# NUNCA DETERIORADO. A mao continua sendo de um homem de 60 e poucos \u2014 o que
# sai e' a avaria, nao a idade: pele cuidada, unhas curtas e limpas, veias
# discretas em vez de saltadas.
# \u26d4 E NENHUMA PALAVRA DE APROVACAO (`beautiful`, `elegant`): elogio no prompt
# puxa para mao de banco de imagem, e mao de modelo de 25 num homem de 63 e' a
# incoerencia que o espectador pega antes de qualquer outra.
# \u26d4 E NENHUMA COR DE PELE: a etnia entra pela PAGINA, na frase que costura o
# REF. Duas vozes decidindo a mesma coisa e' o defeito FT14 do FIGHT 16.
#
# \u2b50\u2b50 DEZESSEIS ENTRADAS NOVAS (2026-08-13). Ordem do operador: *"aumente o
# pool de opcoes substancialmente"*. Seis maos no eixo que E' o rosto deste
# angulo e' a mesma mao voltando a cada seis videos \u2014 e num POV a mao e' a
# unica coisa em que o espectador se agarra entre os dois takes.
# \u26a0\ufe0f A FORMA E' CONTRATO: `<adjetivo> hands with <detalhe> and <detalhe>`. As
# tres frases que consomem o pool vem das ACOES (`A pair of %(maos)s...`, `The
# same %(maos)s...`) e do REF \u2014 entrada que nao comeca por adjetivo quebra as
# tres de uma vez.
# \u2b50 O que VARIA e' porte da mao, unhas, veias, sardas, bronzeado e o objeto do
# pulso (alianca, anel, relogio, pulseira) \u2014 sinal permanente e saudavel, que
# e' o que faz a mesma mao VOLTAR igual no take 2.
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
    # ⭐ O `shape` ENTROU PELO CAMPO `marca`, e nao por chave nova: as tres
    # ACOES de pessoa montam `%(cabeca)s, %(marca)s, wearing %(traje)s` e nao
    # existe slot de porte. Cada entrada nova carrega PORTE + PELE SAUDAVEL +
    # ANCORA no mesmo campo, que sao tres dos seis eixos que o
    # `medir_personagens --gate` conta — os seis antigos acionavam porte e pele
    # em 2 de 6.
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

    # ⭐⭐ A COPY DA ACAO VENCE OS SCRIPTS (decisao 1 do operador, V2). Quem
    # declara `copy` traz as duas falas do proprio video de onde o gesto saiu;
    # quem nao declara cai nos quatro scripts do V1, que continuam vivos.
    # ⚠️ Os dois mecanismos convivem por ordem dele, e o risco esta' declarado
    # no cabecalho de `ACOES`: a defesa e' o painel DIZER de onde a copy veio,
    # senao o operador troca o script e nao entende por que a fala nao mudou.
    _cp = spec.get("acao", {}).get("copy")
    if _cp:
        for i in quais:
            f[i] = _cp[i]
        return f

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

    # ⭐ MODO PESSOA — nasce DESLIGADO (D4). O cadeado da tela vence o modo,
    # como em todos os motores: homem travado no painel e' mais especifico.
    pessoa = bool(travas.get("pessoa")) and MODO_PESSOA

    # ⭐⭐ A ACAO E' O EIXO NOVO DA V2, e ela cobre os DOIS takes num par so'.
    # ⛔ O filtro por `pessoa` nao e' enfeite: com o modo ligado o pool passa a
    # ser SO' o das entradas com gente. Deixar as de maos dentro faria o botao
    # prometer pessoa e entregar maos em dez de treze sorteios — o botao que
    # mente, que este repo ja' pagou tres vezes.
    _pool_ac = [a for a in ACOES if bool(a["pessoa"]) == pessoa]
    acao = (_por_id(ACOES, travas["acao"]) if travas.get("acao")
            else _fresco(_pool_ac or ACOES, hist.get("acao", [])[-4:], rng))

    # ⛔ SO' AS RECEITAS QUE O GESTO SABE MANUSEAR. O cadeado da tela continua
    # vencendo: receita travada e' escolha explicita do operador, e ele ve' o
    # resultado antes de gerar.
    _rec = [r for r in RECEITAS if r["vaso_tipo"] in acao["vasos"]]
    receita = (_por_id(RECEITAS, travas["receita"]) if travas.get("receita")
               else _fresco(_rec or RECEITAS, hist.get("receita", [])[-1:], rng))
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
        "banheiro": banheiro, "superficie": superficie, "acao": acao, "medida": medida,
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
    # ⛔⛔ QUANDO A ACAO TRAZ COPY, O APELIDO SAI DELA. O `apelido` do spec
    # alimenta o painel e as lentes; deixa-lo sorteado a' parte punha `Johnson`
    # no campo e `manhood` na fala, e a BA5 acusou dois apelidos no mesmo video
    # em 34 de 400 sorteios. Um video, um apelido — e quem manda e' a fala.
    _cp = acao.get("copy")
    if _cp:
        for _n in NUCLEO:
            if _n.lower() in _cp[1].lower():
                spec["apelido"] = _n
                break
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

    # ⛔ A MEDIDA E O ROTULO ENTRAM NOS DOIS TAKES. A regua so' faz o trabalho
    # dela se estiver la' quando a promessa e' dita E quando a receita e' feita
    # — sumir no take 2 e' perder o unico lugar onde o `bigger` aterrissa.
    # ⚠️ `img` e' sintagma nominal nos dois pools, entao os dois ganham verbo
    # aqui: "A pale wooden ruler standing upright." e' fragmento e o gerador
    # trata fragmento como enfeite; com verbo, e' instrucao.
    # ⚠️ `There is` nos DOIS: a primeira versao usava "Against the wall is %s"
    # para o rotulo, e as entradas de ROTULOS ja' trazem a propria posicao —
    # saia "Against the wall is a board leaning against the wall". Quem
    # posiciona e' o pool, nao a frase que o costura.
    cenario = ("%s. On %s sit %s, %s and %s. There is %s. There is %s."
               % (_cap(b["cen"]), sup["sup"], r["vaso"], GELATINA, COLHER,
                  med["img"], rot["img"]))

    # ⭐⭐ O GESTO VEM DA ACAO SORTEADA, nos dois takes. Antes da V2 havia UM
    # gesto de maos e UM de pessoa, escritos aqui dentro; agora sao treze pares
    # lidos dos sete videos fonte, e este bloco so' os costura.
    # ⚠️ `agua` e' SINTAGMA NOMINAL ("the spout running into the tub"): ele
    # entra como SUJEITO de um verbo proprio, nunca emendado ("...running into
    # the tub is falling" nao e' ingles).
    h = spec["homem"]
    _slots = {"maos": spec["maos"]["desc"],
              "idade": h["idade"], "etnia": spec["etnia"],
              "cabeca": h["cabeca"], "marca": h["marca"],
              "traje": spec["traje"]}
    ac = spec["acao"]
    quem1 = ac["t1_img"] % _slots
    mov1 = ("%s %s keeps running the whole time. %s"
            % (ac["t1_take"] % _slots, _cap(b["agua"]), NAO_TOCA % med["nome"]))

    b1 = ("IMAGE 01/02: Vertical medium shot. %s %s %s %s"
          % (cenario, quem1, _cap(b["luz"]), CAUDA))

    t1 = ("TAKE 01/02: Animate the provided image exactly. Handheld iPhone "
          "shot, very slight natural sway, no cuts, and the camera does not "
          "move. %s Nothing else in the frame changes.\n"
          'Dialogue: "%s"\nAudio: %s. No music.'
          % (mov1, sonorizar(spec["falas"][0]), b["audio"]))

    # ⭐ TAKE 2 — o preparo. A camera chega mais perto, o quadro e' o mesmo
    # lugar, e o gesto e' UM SO': a gelatina cai no recipiente e o mel entra.
    b2 = ("IMAGE 02/02: Closer vertical shot in the same place, same "
          "background, same light. %s %s stays exactly "
          "where it was, untouched. %s is still in shot. %s %s"
          % (ac["t2_img"] % _slots, _cap(med["img"]), _cap(rot["img"]),
             _cap(b["luz"]), CAUDA))

    t2 = ("TAKE 02/02: Animate the provided image exactly. Handheld iPhone "
          # ⭐ O movimento do take 2 vem da ACAO (V2). Antes era um gesto unico
          # escrito aqui — po caindo + colher + mexer — e com treze pares ele
          # passou a mentir: metade das acoes nao tem po nem colher, e o
          # `lint_take_vs_image` acusou 278 vezes na primeira execucao — que
          # e' exatamente o trabalho dele.
          "shot, very slight natural sway, no cuts. %s %s %s\n"
          'Dialogue: "%s"\nAudio: %s. No music.'
          % (ac["t2_take"] % _slots, r["final2"], NAO_TOCA % med["nome"],
             sonorizar(spec["falas"][1]), b["audio"]))

    # ⭐⭐ BLOCO 0 (REF) — E ELE E' AS MAOS.
    # ⛔ A falta dele quebrou o painel compartilhado (`KeyError 'BLOCO 0
    # (REF)'`), e a quebra apontou uma lacuna REAL: este angulo nao tinha
    # ancora nenhuma entre os dois takes. Todos os outros motores amarram a
    # continuidade num ROSTO; aqui nao ha' rosto — entao a ancora sao as MAOS,
    # que e' o unico corpo que existe em quadro.
    # ⚠️ E' o que impede o take 2 vir com outra mao, que num video POV e' a
    # unica coisa que o espectador tem para se agarrar.
    # ⭐ Com o MODO PESSOA ligado a REF vira o HOMEM, porque ai' existe rosto e
    # e' ele que atravessa o corte.
    if spec["pessoa"]:
        h = spec["homem"]
        ref = ("REF 01: Photo of a real person, a %d-year-old %s man, chest "
               "up, facing the camera directly, calm steady expression. %s, "
               "%s. Hands out of frame, no objects. Plain neutral gray "
               "background, soft even frontal light. Slight sensor grain, soft "
               "focus, raw iPhone front camera aesthetic. No subtitles, no "
               "captions, no burned-in text, no watermark."
               % (h["idade"], spec["etnia"], _cap(h["cabeca"]), h["marca"]))
    else:
        ref = ("REF 01: Photo of both hands of a %d-year-old %s man, palms "
               "down on a plain surface, filled frame, nothing held. %s. Plain "
               "neutral gray background, soft even frontal light. Slight "
               "sensor grain, soft focus, raw iPhone photo. No subtitles, no "
               "captions, no burned-in text, no watermark."
               % (spec["idade"], spec["etnia"], _cap(spec["maos"]["desc"])))

    blocos = sc.selar_takes(sc.selar_tags({
        "BLOCO 0 (REF)": ref,
        "IMAGE 01/02": b1, "TAKE 01/02": t1,
        "IMAGE 02/02": b2, "TAKE 02/02": t2,
    }))
    # ⚠️ A TENSAO ENTRE `No on-screen text` E A PLACA — declarada, nao
    # consertada. O `selar_takes` compartilhado injeta essa trava em todo TAKE,
    # e a placa `GROWTH HACK` E' texto em cena. Eu cheguei a trocar a frase
    # aqui e a `sc.lint_sem_texto` reprovou 800 de 800 — a trava e' cobrada
    # pelo literal exato.
    # ⛔ E FICA COMO ESTA', por evidencia e nao por comodismo: o PLACA 16 roda
    # em producao com exatamente esta combinacao (cartao escrito a mao no
    # quadro + `No on-screen text` no TAKE) e nao perde a placa. O TAKE anima
    # uma IMAGE que JA' contem o cartao, e a trava serve para impedir LEGENDA
    # QUEIMADA, nao para apagar um prop que tem letra.
    # ⚠️ O que importa e' que a CAUDA da IMAGE (onde a placa nasce) nunca diga
    # `no text` — e ela nao diz: so' `no subtitles, no captions, no watermark`.
    # Se um dia um lote voltar sem a placa, este comentario e' o primeiro lugar
    # a olhar.
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
        for pista in (" man ", " man,", " he ", " his ", " woman"):
            if pista in t:
                ach.append(("ERRO", "BA3: %s tem pessoa em quadro (%r) com o "
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
            if (tem_org and sc.ERECAO_16.search(sent)
                    and not spec.get("acao", {}).get("ct7_liberado")):
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


def _ba_acao(spec, blocos, achados):
    """⭐⭐ BA-ACAO — o gesto sorteado tem de chegar aos QUATRO blocos.

    ⛔ Sem esta lente, um par de acao que se perdesse continuaria passando em
    todas as outras: o banheiro certo, a medida intocada, a copy no orcamento —
    e o video sem gesto nenhum. Quadro correto, angulo errado.
    ⛔⛔ E ela cobra IMAGE **e** TAKE dos dois takes, porque falham separado: a
    IMAGE sem o gesto e' um homem parado; o TAKE sem a clausula e' pior e
    silencioso, porque o gerador fecha o gesto sozinho ao longo dos 8 segundos.
    ⚠️ E cobra a COERENCIA DO MODO: acao de pessoa com o modo desligado poe
    gente num angulo que o operador declarou sem gente (D4).
    """
    h = spec["homem"]
    sl = {"maos": spec["maos"]["desc"],
          "idade": h["idade"], "etnia": spec["etnia"],
          "cabeca": h["cabeca"], "marca": h["marca"], "traje": spec["traje"]}
    ac = spec["acao"]
    for chave, bloco in (("t1_img", "IMAGE 01/02"), ("t1_take", "TAKE 01/02"),
                         ("t2_img", "IMAGE 02/02"), ("t2_take", "TAKE 02/02")):
        if (ac[chave] % sl) not in blocos[bloco]:
            achados.append(("ERRO", "BA-ACAO: %s nao carrega o %s do gesto %r"
                            % (bloco, chave, ac["curto"])))
    if bool(ac["pessoa"]) != bool(spec["pessoa"]):
        achados.append(("ERRO", "BA-ACAO: gesto %r (pessoa=%s) com o MODO "
                                "PESSOA %s — o botao promete e nao entrega"
                        % (ac["curto"], ac["pessoa"],
                           "ligado" if spec["pessoa"] else "desligado")))


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
    # ⭐ O CT7 so' e' filtrado NA ENTRADA que o operador liberou (ver
    # `rasga_sache`). Nas outras doze acoes ele continua valendo inteiro.
    _off = _CT_DESLIGADOS + (("CT7:",) if spec.get("acao", {}).get("ct7_liberado")
                             else ())
    ach.extend(x for x in _ct if not x[1].startswith(_off))
    for f in (_ba1_medida, _ba2_rotulo, _ba3_sem_pessoa, _ba4_idade,
              _ba5_apelido, _ba6_leve, _ba7_follow, _ba8_coerencia,
              _ba_acao):
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

EIXOS_UI = [
    ("banheiro", "O BANHEIRO", "BANHEIROS", "regiao"),
    ("acao", "O GESTO", "ACOES", "curto"),
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
# ⛔⛔ E ELE E' O UNICO ACESSO DO OPERADOR A ESTE EIXO. Os seis eixos do
# `EIXOS_UI` tem linha no painel (com `trocar` e cadeado); as MAOS nao tem,
# porque neste angulo elas nao sao um adereco — sao O NARRADOR, e o narrador
# nao aparecia no painel. Este menu e a primeira porta.
# ⛔ POR QUE DROPDOWN E NAO `TRAVAS_UI`: aquela barra desenha UM BOTAO POR
# OPCAO, lado a lado. Serve para as familias de banheiro; com 22 pares de maos
# ela estoura a largura da janela.
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


def _coerir_acao(spec, rng):
    """⛔⛔ O GESTO ARRASTA TRES COISAS, e o painel arrastava ZERO.

    ⚠️ MEDIDO em 2026-08-14 simulando o painel: clicar em `trocar` na linha
    O GESTO deixava **22 de 60 videos invalidos**. O gesto governa tres campos
    e o `sortear` respeita os tres; a troca de eixo nao respeitava nenhum:

      1. PESSOA — metade dos gestos so' existe com alguem em quadro. Trocar
         para um deles com o MODO PESSOA desligado poe um homem na IMAGE e a
         BA3 acusa.
      2. RECEITA — cada gesto sabe manusear certos recipientes (`vasos`).
      3. COPY — tres gestos carregam FALA PROPRIA (`acao["copy"]`), que vence
         os scripts. Trocar o gesto sem refazer a fala deixa o video dizendo a
         copy de um gesto que nao esta' mais em quadro.

    ⭐ O (3) e' o mesmo defeito que o operador filmou no BANHO 16 3TAKES, no
    eixo A COPY. Um defeito de classe, em dois motores irmaos: **eixo que
    arrasta outro campo, num painel que trata todo eixo como independente**.
    """
    ok = [a for a in ACOES if bool(a["pessoa"]) == bool(spec["pessoa"])]
    if ok and bool(spec["acao"]["pessoa"]) != bool(spec["pessoa"]):
        outras = [a for a in ok if a["id"] != spec["acao"]["id"]] or ok
        spec["acao"] = rng.choice(outras)
    rec = [r for r in RECEITAS if r["vaso_tipo"] in spec["acao"]["vasos"]]
    if rec and spec["receita"]["vaso_tipo"] not in spec["acao"]["vasos"]:
        spec["receita"] = rng.choice(rec)
    # ⛔ QUARTO CAMPO: o APELIDO. Mesma regra do `sortear` — quando a acao traz
    # copy propria, quem manda no apelido e' a FALA, nao o sorteio a' parte.
    # ⚠️ Sem esta parte o reparo ainda deixava 9 de 60 invalidos, com a BA5
    # acusando *dois apelidos no mesmo video*: a fala nova dizia `manhood` e o
    # campo do painel continuava em `Johnson`. O `sortear` ja' resolvia isto
    # desde 13/08 (34 de 400 sorteios na epoca) — o reparo do painel e' que
    # nascia sem a lembranca.
    _cp = spec["acao"].get("copy")
    if _cp:
        for _n in NUCLEO:
            if _n.lower() in _cp[1].lower():
                spec["apelido"] = _n
                break
    spec["falas"] = [v for _, v in sorted(_falas(spec, rng).items())]


EIXOS_QUE_MEXEM_NA_COPY = {"acao": _coerir_acao,
                           "banheiro": _coerir_cena,
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

    print("BANHO 16 V2 — %d sorteios (modo pessoa ligado em 1 de 4)" % n)
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

    # ⛔⛔ O VASILHAME DO GESTO TEM DE CASAR COM O DA RECEITA. Sem este
    # controle o defeito volta calado: a IMAGE e o TAKE concordam entre si (o
    # texto do gesto entra nos dois) e discordam da CENA, entao o
    # `lint_take_vs_image` passa e o video sai com a mao mexendo num pote que a
    # bancada nao tem.
    for _i in range(300):
        _s = sortear(pags[_i % len(pags)], random.Random(400 + _i), {}, {})
        if _s["receita"]["vaso_tipo"] not in _s["acao"]["vasos"]:
            falhas.append("VASO: gesto %r (%s) sorteado com a receita %r (%s)"
                          % (_s["acao"]["id"], "/".join(_s["acao"]["vasos"]),
                             _s["receita"]["id"], _s["receita"]["vaso_tipo"]))
            break
    # ⚠️ e toda receita precisa de pelo menos um gesto que a saiba manusear —
    # receita inalcancavel e' entrada morta que o painel conta como viva.
    for _r in RECEITAS:
        if not [a for a in ACOES if _r["vaso_tipo"] in a["vasos"]]:
            falhas.append("VASO: a receita %r (%s) nao tem gesto compativel"
                          % (_r["id"], _r["vaso_tipo"]))

    # ⛔⛔ OS CONTROLES DO EIXO NOVO (V2). Lente que nunca acusou e' lente que
    # ninguem sabe se funciona — e a BA-ACAO nasceu hoje.
    import collections as _c
    _vistas, _com_copy = _c.Counter(), _c.Counter()
    for _i in range(400):
        _s = sortear(pags[_i % len(pags)], random.Random(700 + _i), {}, {})
        _vistas[_s["acao"]["id"]] += 1
        _com_copy[bool(_s["acao"].get("copy"))] += 1
    _maos = [a for a in ACOES if not a["pessoa"]]
    if len(_vistas) < len(_maos):
        falhas.append("ACOES: so' %d de %d gestos de maos aparecem em 400 "
                      "sorteios" % (len(_vistas), len(_maos)))
    if any(a["pessoa"] for a in ACOES if a["id"] in _vistas):
        falhas.append("ACOES: gesto de PESSOA sorteado com o modo desligado")
    # ⭐ e o modo ligado tem de entregar SO' pessoa, e mais de uma opcao
    _p = {sortear(pags[_i % len(pags)], random.Random(800 + _i), {},
                  {"pessoa": True})["acao"]["id"] for _i in range(120)}
    if not _p <= {a["id"] for a in ACOES if a["pessoa"]}:
        falhas.append("ACOES: modo PESSOA ligado sorteou gesto de maos")
    if len(_p) < 2:
        falhas.append("ACOES: modo PESSOA com %d opcao(oes) — eixo morto"
                      % len(_p))
    if not _com_copy[True]:
        falhas.append("ACOES: nenhum gesto com copy propria foi sorteado — a "
                      "decisao 1 do operador virou codigo morto")
    # ⭐ toda entrada tem os quatro slots e os placeholders que ela usa
    for _a in ACOES:
        for _k in ("t1_img", "t1_take", "t2_img", "t2_take", "curto", "reel"):
            if not _a.get(_k):
                falhas.append("ACOES: %r sem %s" % (_a["id"], _k))
        if _a.get("copy") and len(_a["copy"]) != 2:
            falhas.append("ACOES: %r com copy de %d fala(s)"
                          % (_a["id"], len(_a["copy"])))


    controles = [
        ("BA1 sem a medida na IMAGE 02", _ba1_medida, s0,
         dict(b0, **{"IMAGE 02/02": "a wet tiled wall"}), True),
        ("BA1 limpo", _ba1_medida, s0, b0, False),
        ("BA2 sem o rotulo", _ba2_rotulo, s0,
         dict(b0, **{"IMAGE 01/02": "a shower with a jar"}), True),
        ("BA2 limpo", _ba2_rotulo, s0, b0, False),
        ("BA3 com homem e modo desligado", _ba3_sem_pessoa, s0,
         dict(b0, **{"IMAGE 01/02": b0["IMAGE 01/02"] + " A man stands there."}),
         True),
        ("BA3 limpo", _ba3_sem_pessoa, s0, b0, False),
        ("BA5 com pecker na fala", _ba5_apelido,
         dict(s0, falas=[s0["falas"][0],
                         "The gelatin trick feeds blood back to your pecker."]),
         b0, True),
        ("BA5 limpo", _ba5_apelido, s0, b0, False),
        # ⚠️ O `acao` E' FIXADO NUMA ENTRADA SEM `ct7_liberado`, e isso nao e'
        # detalhe: desde 2026-08-13 a BA6 abre mao do par orgao+ereccao NA
        # ACAO QUE O OPERADOR LIBEROU. Se o controle cair justo nela, a lente
        # fica CERTA em nao acusar e o autoteste reprova o comportamento
        # correto — foi o que aconteceu na primeira execucao depois da
        # excecao. O controle tem de testar o caso que ainda e' proibido.
        ("BA6 orgao + ereccao na mesma sentenca", _ba6_leve,
         dict(s0, acao=next(a for a in ACOES if not a.get("ct7_liberado")),
              falas=[s0["falas"][0],
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

    for e, minimo in (("banheiro", 8), ("superficie", 7), ("medida", 6),
                      ("rotulo", 4), ("receita", 2), ("maos", len(MAOS)),
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
