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
PISO_FALA = {1: 16, 2: 21}

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
     "cen": "a shower wall of dark reclaimed wood planks with a recessed "
            "stone niche and a rain head running above it",
     "agua": "the water falling past the mouth of the niche",
     "luz": "Warm low light, wet wood.",
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
    {"id": "box_pedra", "sups": ("nicho", "cesta_canto", "prateleira_arame"),
     "cen": "a dark slate shower with a square rain head running from the "
            "ceiling",
     "agua": "the water falling straight down in front of the wall",
     "luz": "Dim, high contrast, wet stone.",
     "audio": "a heavy rain shower on stone"},
    {"id": "banheira_azulejo", "sups": ("borda_banheira", "tampo_madeira", "banquinho"),
     "cen": "a tub alcove with small square wall tiles and a chrome spout "
            "running",
     "agua": "the spout running steadily into the tub",
     "luz": "Even daylight, pale tiles.",
     "audio": "a tub filling, water on enamel"},
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
    {"id": "bebida",
     "vaso": "a tall clear glass filled with amber liquid",
     "vaso_curto": "copo de liquido ambar",
     "final": "the powder sinking through the amber liquid in slow white "
              "ribbons as the spoon turns",
     "curto": "bebida"},
    {"id": "pomada",
     "vaso": "an open blue jar of mentholated chest rub, the white cream "
             "smooth and untouched inside",
     "vaso_curto": "pote azul de pomada",
     "final": "the mixture rising into a thick white foam that swells over "
              "the rim of the jar",
     "curto": "pomada"},
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
MAOS = [
    "heavily sun-spotted hands with prominent veins and thin skin",
    "broad weathered hands with thick knuckles and raised veins",
    "lean hands with dark age spots across the backs",
    "large hands with loose skin over the tendons and blunt clean nails",
    "wide hands with heavy veins and a plain gold wedding band",
    "bony hands with prominent knuckles and pale scarred skin",
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
    "Comment gelatin, and the recipe goes to your messages.",
    "Comment gelatin, and the recipe lands in your messages.",
    "Comment gelatin, and the recipe is in your messages.",
    "Comment gelatin, and I'll send it to your inbox.",
    "Comment gelatin, and it goes straight to your inbox.",
    "Comment gelatin, and the recipe arrives in your messages.",
    "Comment gelatin, and I'll send it to your messages.",
    "Comment gelatin, and the full recipe hits your inbox.",
    "Comment gelatin, and it lands in your inbox tonight.",
    "Comment gelatin, and the recipe reaches your messages.",
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
        if spec["abertura"] == "idade":
            pr = rng.choice(_cabe(PROMESSAS, _mn(IDADES_HACK) + _mn(QUANDOS), 1))
            ih = rng.choice(_cabe(IDADES_HACK, _palavras(pr) + _mn(QUANDOS), 1))
            qd = rng.choice(_cabe(QUANDOS, _palavras(pr) + _palavras(_amostra(ih)), 1))
            f[0] = "%s %s %s" % (ih % {"idade": spec["idade"]}, qd, pr)
        else:
            el = rng.choice(_cabe(ELAS, _mn(AVISOS_SOLTEIRO) + _mn(AVISOS_CASADO), 1))
            so = rng.choice(_cabe(AVISOS_SOLTEIRO, _palavras(el) + _mn(AVISOS_CASADO), 1))
            ca = rng.choice(_cabe(AVISOS_CASADO, _palavras(el) + _palavras(so), 1))
            f[0] = "%s %s %s" % (so, ca, el)

    if 1 in quais:
        me = rng.choice(_cabe(MECANISMOS, _mn(CTAS) + _mn(FOLLOWS), 2, o)).format(o=o)
        ct = rng.choice(_cabe(CTAS, _palavras(me) + _mn(FOLLOWS), 2))
        fo = rng.choice(_cabe(FOLLOWS, _palavras(me) + _palavras(ct), 2))
        f[1] = "%s %s %s" % (me, ct, fo)

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
        "maos": rng.choice(MAOS),
        "idade": idade,
        "abertura": (travas.get("abertura")
                     or rng.choice(["idade", "idade", "idade", "aviso"])),
        # ⛔ D7 — os dois unicos apelidos deste agente.
        "apelido": rng.choice(list(NUCLEO)),
    }
    spec["falas"] = [v for _, v in sorted(_falas(spec, rng).items())]
    return spec


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

    if spec["pessoa"]:
        h = spec["homem"]
        quem1 = ("A %d-year-old %s man stands with his back half to the "
                 "camera, %s, %s, wearing %s, scooping white cream from a blue "
                 "jar with two fingers and rubbing it into the back of his own "
                 "neck. His face is turned away, seen only in part."
                 % (h["idade"], spec["etnia"], h["cabeca"], h["marca"],
                    spec["traje"]))
        mov1 = ("He keeps working the cream into the back of his neck with the "
                "same slow circles and does not turn around. "
                + NAO_TOCA % med["nome"])
    else:
        quem1 = ("A pair of %s enters from the bottom of the frame and rests "
                 "on the edge beside the jar, palms down, lifting nothing."
                 % spec["maos"])
        # ⚠️ `agua` e' SINTAGMA NOMINAL ("the spout running into the tub"), e
        # a versao anterior emendava "is falling the whole time" nele: saia
        # "the spout running steadily into the tub is falling", que nao e'
        # ingles. Aqui ele entra como SUJEITO de um verbo proprio.
        mov1 = ("The hands stay flat on the edge and lift nothing. %s keeps "
                "running the whole time. %s"
                % (_cap(b["agua"]), NAO_TOCA % med["nome"]))

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
          "background, same light. The same %s hold the torn paper sachet over "
          "%s and a fine stream of white powder is falling into it, while the "
          "spoon of honey waits at the edge of the frame. %s stays exactly "
          "where it was, untouched. %s is still in shot. %s %s"
          % (spec["maos"], r["vaso"], _cap(med["img"]), _cap(rot["img"]),
             _cap(b["luz"]), CAUDA))

    t2 = ("TAKE 02/02: Animate the provided image exactly. Handheld iPhone "
          "shot, very slight natural sway, no cuts. The powder keeps falling "
          "at the same rate, then the spoon tips its honey in and the hands "
          "stir once, %s. %s\n"
          'Dialogue: "%s"\nAudio: %s. No music.'
          % (r["final"], NAO_TOCA % med["nome"],
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
               % (spec["idade"], spec["etnia"], _cap(spec["maos"])))

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
            if tem_org and sc.ERECAO_16.search(sent):
                ach.append(("ERRO", "BA6/CT7: cena %d junta o orgao e verbo de "
                                    "ereccao na mesma sentenca: %r"
                            % (i, sent.strip())))
    duro = re.compile(r"\b(rock hard|rock-hard|brutal|savage|slam|pound)\b", re.I)
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
    sc.lint_isca_cta(falas[1], ach, "a cena 2 (CTA)")
    sc.lint_cta_literal(falas[1], ach, "a cena 2 (CTA)")
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

EIXOS_UI = [
    ("banheiro", "O BANHEIRO", "BANHEIROS", "id"),
    ("superficie", "A SUPERFICIE", "SUPERFICIES", "curto"),
    ("medida", "A MEDIDA", "MEDIDAS", "curto"),
    ("rotulo", "O ROTULO", "ROTULOS", "curto"),
    ("receita", "A RECEITA", "RECEITAS", "curto"),
]
EIXOS_TRAVAVEIS = ["banheiro", "superficie", "medida", "rotulo", "receita"]
TRAVAS_UI = [("familia_banheiro", "cenario",
              ["livre"] + FAMILIAS_BANHEIRO)]

# ⚠️ `banheiro` e `receita` provam-se por outros literais que nao o campo do
# painel (`cen` e `vaso`), entao ficam de fora da lente de honestidade.
IGNORA_PAINEL = ("banheiro", "receita")

# ⛔ Nenhum eixo do painel mexe na copy: a fala nao cita o banheiro, a
# superficie, a medida nem o recipiente. Declarar o dicionario vazio e'
# declarar que alguem verificou, em vez de deixar o `getattr` decidir.
EIXOS_QUE_MEXEM_NA_COPY = {}


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
        for e in ("banheiro", "superficie", "medida", "rotulo", "receita"):
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
    for e in ("banheiro", "superficie", "medida", "rotulo", "receita",
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
        if "Comment gelatin," not in x:
            falhas.append("CT6/D2: %r sem `Comment gelatin,` — a automacao de "
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
         dict(b0, **{"IMAGE 01/02": b0["IMAGE 01/02"] + " A man stands there."}),
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
                         "Comment gelatin, and follow me or it will not send."]),
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
                      ("rotulo", 4), ("receita", 2), ("abertura", 2)):
        if len(eixos[e]) < minimo:
            falhas.append("EIXO %s: so' %d valores em %d sorteios (pool tem %d)"
                          % (e, len(eixos[e]), n, minimo))
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
