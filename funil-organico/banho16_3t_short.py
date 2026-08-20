#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
banho16_3t_short.py — randomizador + gerador + linter do **BANHO 16 3TAKES**.

⭐⭐ O QUE ELE E': o mesmo banheiro POV do `banho16`, em TRES takes de ~5s em
vez de dois de 8s. ⛔ **Nao substitui o `banho16` nem o `banho16_v2`** — os tres
convivem, como o CLEAN v1/v2. O que muda nao e' o angulo, e' o RELOGIO, e o
relogio arrasta tudo o mais: teto de 14 palavras por cena em vez de 25, tres
imagens em vez de duas, destino AdBatch **Vertical 3** em vez de Vertical 2.

⛔ A ORDEM QUE O CRIOU (operador, 2026-08-14): *"Resolvi criar a partir de
agora videos mais dinamicos, com 3 takes de 5 segundos"*. E o teto de palavras
e' MEDIDO POR ELE em campo, nao teorizado por mim: *"Eu posso gerar cada take
com o limite de 6 segundos de duracao, entao faca cada cena ter no maximo 14
palavras em ingles, para que cada take tenha em torno de 4-5 segundos"*.

FONTE: os MESMOS sete reels da pagina "Be yourself" que deram o `banho16`, mas
lidos de novo em 2026-08-14 com as SETE COPIES INTEIRAS na mao (original +
a variacao que o operador rodou), o que a leitura otica de 12/08 nao tinha.

⛔⛔ O QUE A LEITURA NOVA PROVOU — e ela desmentiu a hipotese de trabalho:

  1. ⚠️ A HIPOTESE ERA *"as combinacoes saem parecidas demais"*. MEDIDO, ela
     nao se sustenta: os 9 hooks do `banho16` tem 12% de sobreposicao de
     vocabulario e 4 aberturas distintas em 9; os 7 hooks da fonte tem **14%**
     e 5 em 7. As copies da fonte sao TAO repetitivas quanto as nossas — e
     duas delas (videos 3 e 4) sao **identicas palavra por palavra**.
     Se o problema fosse variedade de copy, a fonte nao seria a solucao.
  2. ⭐⭐ O QUE SEPARA E' A **FORMA** DO HOOK, nao a variedade. Taxa de
     comentario por mil views, nos sete originais:
         exclusao (`If you are single, do not try this`) ....... 20,5
         idade + hack ................................. 11,8 · 7,5 · 5,6
         confissao (`fixed my small bat`) ..................... 8,1
         acusacao/metafora (o rodeio) ......................... 6,4
         pergunta (`Struggling to stay hard?`) ................ 4,0
  3. ⭐⭐ O CAMPEAO E' O UNICO SEM MECANISMO. O video de 20,5 nao explica
     NADA: avisa, promete, e pede. Os outros seis entregam a explicacao
     inteira de graca (*"remove o acumulo toxico no seu sangue"*) — e depois
     pedem comentario pelo que sobrou. E' o nosso CT5 (*a receita e' a moeda*)
     confirmado por quem nunca leu o nosso contrato.
  4. ⚠️ MAS n=7 E O CAMPEAO E' UNICO EM TRES COISAS AO MESMO TEMPO: hook de
     exclusao, sem mecanismo, e o mais curto. **Nao da' para separar as tres
     com sete pontos.** Por isso `sem_mecanismo` nasce EIXO SORTEAVEL 50/50
     neste motor, e nao decisao: em 30 videos o campo separa o que a fonte
     nao separa. Variavel confundida vira eixo, nunca palpite.
  5. ⭐ A ordem do beat mudou de lugar. Em 2 takes o CTA divide cena com o
     mecanismo; em 3 ele tem cena PROPRIA — e cena propria de CTA e' o que
     permite o `follow` existir sem comer palavra do mecanismo.

⛔ AS DECISOES DO OPERADOR PARA ESTE MOTOR (2026-08-14):

  E1 keyword e' `RECIPE` ....................... a fonte inteira pede Recipe
  E2 as 12 copies sao APROVADAS UMA A UMA ...... nao ha' geracao de fala nova
  E3 apelidos: `bat` e `pipe` LIBERADOS ........ decidido pela pratica, ao
     aprovar as familias 4 e 7 — a regra `so' Johnson/manhood` do `banho16`
     NAO vale aqui, e isso e' escolha, nao esquecimento
  E4 o `follow` e' o beat COMPRESSIVEL ......... *"a parte de seguir nao e'
     tao importante quanto o CTA, deve ser feita de modo que nao atrapalhe a
     quantidade de palavras"*. Quando a cena 3 encosta no teto, cai o follow,
     nunca a keyword.
  E5 pessoas: homem americano NEGRO ............ quando aparece (modo pessoa)
  E6 a agua NUNCA cai nos ingredientes ......... ordem literal dele
  E7 borbulha SEM transbordar .................. ordem literal dele, e ela
     nasceu de um erro real: o lote do video 5 devolveu espuma escorrendo
     pela lateral do pote

⛔⛔ E1 REVERTE O D2 do `banho16` (*keyword continua GELATIN*). A ordem nova e'
mais recente e nomeia este motor. Se voltar para GELATIN, e' trocar
`CTA_BANHO` aqui e o PT em `dados_banho_3t.py`.

⛔ O `Segue primeiro` SAIU da familia 6.2, e a razao e' de FATO, nao de gosto:
*"a mensagem e' enviada independente de seguirem ou nao"* (operador,
2026-08-10). Follow como condicao promete um portao que a automacao de DM nao
tem. A lente `B3-7` cobra isso.

O ARCO — 3 takes de 6s (18s no total), destino AdBatch Vertical 3:

    take 1  O HOOK        o banheiro, os props parados na superficie, a medida
                          intocada, o rotulo `growth hack`; a mao ALCANCA
    take 2  O PREPARO     o sache rasga e o po cai no recipiente; o dedo mexe
    take 3  A REACAO+CTA  a colher de ambar entra e a mistura ERUPCIONA em
                          espuma — contida abaixo da borda · o CTA

Uso:
    python funil-organico/banho16_3t_short.py --pagina joe --n 1
    python funil-organico/banho16_3t_short.py --autoteste
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

TITULO = "AGENTE BANHO 16 3TAKES"
SLUG = "banho-16-3t"
SUBTITULO = ("3 takes de 6s = 18 segundos · o banheiro · as maos preparam a "
             "receita, a medida fica intocada e a mistura reage no fim")

LEDGER = os.path.join(AQUI, ".banho-16-3t-ledger.json")

CENAS_UI = ["1 · O HOOK", "2 · O PREPARO", "3 · A REACAO + CTA"]

# ⛔⛔ OS NOMES DOS BLOCOS SAO CONSTANTES, e isso e' conserto de um defeito
# real: as lentes herdadas do `banho16` varriam a tupla literal
# `("IMAGE 01/02", "IMAGE 02/02")`. Depois da cirurgia temporal os blocos
# passaram a se chamar `01/03`, e as lentes acusaram 7 ERROS em um video
# CERTO — procurando blocos que nao existem mais e ignorando os tres que
# existem. Lente que varre nome literal apodrece na primeira mudanca de
# formato; lente que varre a constante acompanha.
IMAGENS = ("IMAGE 01/03", "IMAGE 02/03", "IMAGE 03/03")
TAKES = ("TAKE 01/03", "TAKE 02/03", "TAKE 03/03")

# ⛔⛔ O TETO E' DO OPERADOR, MEDIDO EM CAMPO — nao e' estimativa minha.
# *"Eu posso gerar cada take com o limite de 6 segundos de duracao, entao faca
# cada cena ter no maximo 14 palavras em ingles, para que cada take tenha em
# torno de 4-5 segundos de duracao"* (2026-08-14).
# ⚠️ E' MUITO mais duro que o do `banho16` (25 por take, medido em render de
# 8s). Cena que estoura 14 aqui nao "fica apertada": ela CORTA, e o que corta
# no fim de um take de 5s e' justamente o CTA.
# ⭐⭐ 2026-08-20 — O TETO PASSOU A SER DERIVADO, NAO DECLARADO.
# Medido em 30 segmentos de video GERADO no nosso formato contra 469
# segmentos de 60 reels reais da fonte: a voz gerada fala 2,62 palavras
# por segundo e a voz real fala 3,49 — 33% mais devagar. Em 6 segundos
# eles cabem 21 palavras e nos cabemos 15.
# ⛔ Por isso o teto e' `SEGUNDOS_TAKE x TAXA_MEDIA`, e nao um numero
# escrito na mao: quando o relogio mudar, o teto muda junto. O 14 antigo
# nao estava errado — estava sem origem, e numero sem origem nao
# sobrevive a proxima cirurgia temporal.
SEGUNDOS_TAKE = 8.0   # ⭐ MEDIDO, nao pedido: o player marca 00:08:00.
                      # O `durationSeconds: 10` da AdBatch e' aspiracional.
TAXA_MEDIA = 3.1      # ritmo de fala NORMAL — a calibracao dos outros 19.
# ⛔⛔ OS 2,62 p/s QUE EU MEDI EM 20/08 NAO ERAM O GERADOR: eram o
# `slow deliberate cadence` deste arquivo, retirado no mesmo dia. Medir o
# efeito do proprio pedido e chamar de limite do meio foi erro meu.
TAXA_LENTA = 2.62     # lapide: e' o que sai QUANDO se pede lentidao.
TETO = round(SEGUNDOS_TAKE * TAXA_MEDIA)        # 25
TETO_FALA = {1: TETO, 2: TETO, 3: TETO}


def segundos_de(fala, taxa=TAXA_MEDIA):
    """Quanto tempo esta fala ocupa, na taxa pedida.

    ⚠️ Existe porque o `medir_teto_fala` conta PALAVRA contra o teto
    declarado, nunca palavra contra o RELOGIO — entao um motor podia
    passar no gate e cortar a fala no render. Aqui o tempo e' medido e
    impresso, e a aposta de encher o take fica visivel.
    """
    return len([p for p in str(fala).split() if p]) / float(taxa)
# ⭐ PISO = o MINIMO REAL medido nos pools deste motor, nunca chutado. Piso
# calibrado no chute vira alarme que sempre dispara, e alarme que sempre
# dispara ensina o operador a ignorar o linter inteiro. Recalibrar sempre que
# as FAMILIAS mudarem (o autoteste cobra isso).
PISO_FALA = {1: 11, 2: 10, 3: 10}

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

# ⛔⛔ E3 — O VOCABULARIO DA FONTE, LIBERADO AQUI. Estes dois entraram porque
# o operador aprovou copy que os usa: `bat` nas duas entradas da familia 4
# (*"meu bastao era pequeno e mole"*) e `pipe` na 7.2, que ele mesmo editou
# para dizer *"a circulacao do seu cano"*. Aprovar a copy E' decidir o
# vocabulario — nao ha' decisao separada a pedir.
# ⚠️ Isto NAO vale para o `banho16` V1/V2: la' a ordem D7 (*"somente jonhson
# e manhood"*) continua de pe'. Duas regras, dois motores, cada uma escrita
# onde vale.
APELIDOS_FONTE = ("bat", "pipe")


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
# ⛔⛔ O CAMPO `meio` E' NOVO NESTE MOTOR, e ele conserta um defeito que so'
# existe em TRES takes. No `banho16` o po que cai E' a reacao — o `final` da
# `pomada` diz *"o creme vira uma espuma branca fina"*, e isso fecha o video.
# Com tres takes a reacao mudou de casa: ela e' o TAKE 3, quando o ambar entra.
# ⚠️ Se o take 2 ja' espumasse, o take 3 seria a segunda espuma do mesmo pote —
# o espectador le' isso como corte errado, e o gerador, lendo os dois blocos,
# resolve a contradicao inventando um terceiro estado. `meio` e' o que o po faz
# SEM reagir; `final` continua sendo a reacao, e agora so' o take 3 o usa.
RECEITAS = [
    {"id": "bebida", "vaso_nome": "glass",
     "vaso": "a tall clear glass filled with amber liquid",
     "vaso_curto": "copo de liquido ambar",
     "meio": "the powder sinks through the amber liquid in slow white "
             "ribbons and settles at the bottom, with no reaction yet",
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
     "meio": "the white powder lands on the smooth cream and builds a small "
             "mound on top of it, with no reaction yet",
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
# ⛔⛔ SEM `shot straight on` E SEM `Vertical close shot` — os dois SAIRAM, e
# nao por tamanho: eles CONTRADIZEM a `ORIENTACAO` logo abaixo, que pede a
# camera *"aimed slightly downward at about thirty degrees"*. Reto e trinta
# graus nao podem ser verdade no mesmo bloco, e contradicao nao e' ignorada
# pelo gerador — ele escolhe uma, e a que ele escolhe nao e' a nossa. Foi
# lendo o primeiro lote em voz alta que isso apareceu; nenhum linter pegaria.
# ⚠️ `Vertical` tambem saiu daqui porque a ORIENTACAO ja' abre com
# `Vertical 9:16 portrait orientation` — dizer duas vezes nao reforca, dilui.
ENQUADRAMENTO = ("The camera is right up at the shelf, the objects filling "
                 "the frame and the hands coming in large and close to the "
                 "lens.")

CAUDA = ("Shot on an iPhone, natural grain, slightly wet lens. "
         "No subtitles, no captions, no watermark.")

# ⛔⛔ A ORIENTACAO EM GRAUS — e ela e' LICAO PAGA POR OUTRO, nao teoria minha.
# O operador tentou `looking straight down at a perfectly level angle` para
# consertar um enquadramento torto e o gerador devolveu **vista aerea, imagem
# rotacionada**. O que funcionou foi descrever a PESSOA segurando o telefone,
# com o angulo em GRAUS, e so' depois negar as orientacoes erradas.
# ⭐ A ordem importa: a descricao positiva primeiro, a negacao por ultimo. A
# negacao sozinha injeta o token (mesma licao do `not a celebrity`); a negacao
# DEPOIS de uma geometria explicita so' fecha a porta que ja' estava estreita.
# ⚠️ `shot straight on` sozinho nao segura isto — foi o que o `banho16` usa, e
# e' o unico eixo em que a fonte do operador ficou objetivamente melhor.
ORIENTACAO = ("Vertical 9:16 portrait orientation, the camera held upright in "
              "vertical position like a person standing at the shelf filming "
              "with their phone in portrait mode, aimed slightly downward at "
              "about thirty degrees. The phone is held upright, not sideways, "
              "not rotated, not landscape, not overhead, not bird's eye.")

# ⛔ A TRAVA ANTI-ARTEFATO. POV de maos e' onde o gerador mais inventa membro:
# uma terceira mao entrando pela lateral, seis dedos, um antebraco que nao
# pertence a ninguem. A fonte carrega esta clausula em TODOS os blocos, imagem
# e take, e e' barata.
DEZ_DEDOS = ("Exactly ten fingers total visible, no extra hands, no extra "
             "limbs, only two arms in frame.")

# ⭐ A ANCORA DE MAO — a parte CONSTANTE da descricao, que o pool `MAOS` nao
# carrega. Sem rosto, a mao e' a unica continuidade entre tres quadros gerados
# separadamente, e "maos largas com unhas curtas" nao identifica ninguem.
# ⚠️ Idade e etnia vivem AQUI, e por isso o slot da idade e o mesmo da fala.
# ⚠️ SEM A CLAUSULA DE UNHA: todas as 22 entradas do pool `MAOS` ja' terminam
# em unha, e a primeira versao devolvia *"short clean trimmed nails, natural
# age spots [...], with short trimmed nails and smooth skin"*. Duplicacao lida
# em voz alta, que nenhum linter pegaria.
ANCORA_MAO = ("thick veins standing out across the back of the hand and up "
              "the wrist, large visible knuckles, natural age spots scattered "
              "near the wrist")

# ⭐ O BANHEIRO HABITADO. Os banheiros do `banho16` estao VAZIOS, e banheiro
# vazio le' como render de catalogo. A fonte enche o fundo de vida barata, e e'
# isso que faz o quadro passar por celular.
# ⛔ Sempre ATRAS ou NA BEIRA, nunca perto dos props: detalhe encostado no
# grupo central e' o que o gerador empilha em cima da placa.
HABITADOS = [
    "a used disposable razor and a crumpled hand towel lie at the far end, "
    "well away from the products",
    "a ceramic holder with two toothbrushes and a tube of toothpaste sits at "
    "the far end, well away from the products",
    "a worn bar of soap and a small bottle of mouthwash sit at the far end, "
    "well away from the products",
    "a half-used shampoo bottle and a folded washcloth sit at the far end, "
    "well away from the products",
    "a comb and a small deodorant stick lie at the far end, well away from "
    "the products",
    "a folded hand towel hangs from a ring on the wall behind, and a worn bath "
    "mat shows at the bottom edge",
]

# ⭐ A DERIVA DE CAMERA, uma por take. No `banho16` ela e' uma frase so' nos
# dois takes, e camera identica em cortes seguidos e' o que denuncia geracao.
# A fonte varia a imperfeicao em cada take, sempre pequena.
DERIVAS = [
    "The camera has a constant subtle handheld sway with a tiny drift to the "
    "right.",
    "The camera drifts slightly forward with a subtle wobble.",
    "The camera has a faint wobble and a tiny involuntary zoom-in that settles "
    "back.",
    "The camera sways gently left to right and settles.",
]

# ⭐⭐ A REACAO — o payoff visual, e a maior diferenca medida entre o nosso
# take final e o da fonte. O `banho16` diz *"o po afunda em fitas brancas
# lentas"*; a fonte diz que a mistura ERUPCIONA. Mesmo prop, mesmo plano: o
# que muda e' o VERBO.
# ⛔⛔ E ela e' CONTIDA, por ordem literal do operador (*"faca borbulhar mas
# nao ao ponto de derramar para fora"*). A ordem nasceu de um erro real: o
# lote do video 5 devolveu espuma escorrendo pela lateral do pote.
# ⚠️ A contencao e' dita TRES vezes de formas diferentes de proposito — foi o
# que a fonte precisou fazer para o gerador parar de transbordar.
REACAO = ("the liquid hits the mixture and it immediately erupts into a "
          "vigorous fizzing and bubbling reaction, thick white foam expanding "
          "fast with visible bubbles forming and popping, rising toward the "
          "rim but staying contained inside, not overflowing, not spilling "
          "over the edge, bubbling hard but always below the rim")

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


def _maos_partes(txt):
    """Parte uma entrada de `MAOS` em (adjetivo, detalhe).

    ⛔ As 22 entradas seguem UM molde: `<adjetivos> hands with <detalhes>`.
    Partir aqui e' o que permite a mesma entrada virar *"as maos X de um homem
    de 69 anos, com Y"* ou *"a mao direita de um homem de 69 anos, uma mao X
    com Y"* sem repetir o substantivo.
    ⚠️ Se alguem acrescentar uma entrada fora do molde, o fallback devolve o
    texto inteiro como detalhe — degrada, nao quebra. A lente `B3-9` cobra o
    molde no pool inteiro, para o fallback nunca virar o caso normal.
    """
    txt = txt["desc"] if isinstance(txt, dict) else txt
    if " hands with " in txt:
        a, d = txt.split(" hands with ", 1)
        return a.strip(), d.strip()
    return "steady", txt


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
# ⭐⭐ AS DOZE COPIES DO OPERADOR — 2026-08-14
# ===========================================================================
# ⛔⛔ APROVADAS UMA A UMA, em duas rodadas, com ele lendo cada linha. Isto NAO
# e' um pool que eu escrevi e ele carimbou: seis das doze ele reescreveu ou
# editou na mao, e duas (`6.2` e `7.2`) chegaram ja' corrigidas por ele.
# NADA aqui se altera sem ordem — e' copy, e copy e' alcada dele.
#
# ⭐ A ARQUITETURA E' POR **FAMILIA**, nao por beat solto, e isso e' o conserto
# do defeito que ele apontou (*"a variacao [...] e' sempre muito parecida uma
# com a outra"*). O `banho16` sorteia hook e fecho INDEPENDENTES de dois pools
# — 81 combinacoes nominais que o espectador le' como umas quatro, porque 5 dos
# 9 hooks abriam com as MESMAS tres palavras (medido: 55% dos sorteios).
# Aqui a familia e' atomica: as tres cenas vem juntas, escritas para casar.
# ⚠️ Menos combinacoes nominais (12 contra 81) e MAIS diferenca percebida.
# Combinacao nominal nunca foi a metrica; distancia percebida e'.
#
# ⛔ A IDADE E' SLOT (`%(idade)d`). E' o unico campo que a fonte troca entre
# dois videos do mesmo script (67 / 72 / 66 nos tres reels quase identicos), e
# ela e' lida uma vez por video — entao nunca ha' dois numeros diferentes no
# mesmo video. O defeito deixa de ser possivel em vez de ser proibido.
#
# ⭐⭐ O CAMPO `mec` E' O EIXO DA HIPOTESE. `False` = a copy NAO explica o
# mecanismo, so' avisa e promete. E' a forma do reel de 20,5 comentarios por
# mil views — 2,5x o segundo colocado da fonte, e o UNICO dos sete sem
# explicacao. ⚠️ Com n=7 e tres diferencas simultaneas eu NAO consigo provar
# que a causa e' essa; por isso `mec` e' pre-selecionavel no painel, para o
# lote responder o que a fonte nao responde.
CTA_LITERAL = "Comment Recipe"

FAMILIAS = [
    # -- FAMILIA 2 — solteiro vs casado. SEM MECANISMO. ---------------------
    # ⭐ A forma de melhor comentario da fonte inteira. Ela nao explica nada:
    # avisa quem nao deve fazer, promete a consequencia, e pede.
    {"id": "excl_a", "curto": "solteiro/casado · nao encosta", "mec": False,
     "cenas": [
"If you are single, do not touch this. If you have a wife, go "
         "real easy, because she is the one who will need mercy.",
"These two items, mixed right in the shower, and she will not "
         "be able to keep up with you. That is all I will say.",
"No pharmacy and no prescription. %s and follow me, and the "
         "complete step by step goes straight to your messages." % CTA_LITERAL,
     ]},
    {"id": "excl_b", "curto": "solteiro/casado · passa direto", "mec": False,
     "cenas": [
"If you are single, keep scrolling. If you are married, I am "
         "sorry in advance, because my wife stopped asking me what "
         "changed.",
"Mixed right, these two will have her asking you to slow down "
         "and rest. I am not going to explain more than that here.",
"It costs almost nothing to try. %s and follow me, and the full "
         "step by step goes straight to your messages." % CTA_LITERAL,
     ]},

    # -- FAMILIA 3 — a acusacao na cara ------------------------------------
    {"id": "acus_gelatina", "curto": "mole igual gelatina", "mec": True,
     "cenas": [
"I was going soft at %(idade)d and I blamed my age for years. "
         "This bizarre bath method is what actually fixed it for me.",
"This recipe forces the blood flow back down there. Rock hard "
         "again, no blue pills, no pharmacy, and no doctor asking "
         "questions.",
"%s and follow me right now, and the complete step by step goes "
         "straight to your messages in a couple of minutes." % CTA_LITERAL,
     ]},
    {"id": "acus_cavalo", "curto": "cavalo manco no rodeio", "mec": True,
     "cenas": [
"I was falling like a lame horse every single night and she "
         "noticed. This strange thing I do in the shower turned it "
         "around.",
"This shower habit unclogs the pipes for good. Maximum size, "
         "rock solid endurance, and it happens while you are already "
         "washing.",
"%s and follow me, and I will send the whole step by step "
         "straight to your messages, no charge and no catch." % CTA_LITERAL,
     ]},

    # -- FAMILIA 4 — o bastao e os canos -----------------------------------
    {"id": "bat_trinca", "curto": "o bastao pequeno e mole", "mec": True,
     "cenas": [
"I am %(idade)d and my bat was small and soft. My wife was done "
         "pretending. This bizarre shower habit is what saved my "
         "marriage.",
"It unclogged the toxic buildup that was killing my blood flow. "
         "Maximum size now, and the whole thing took less than two "
         "weeks.",
"No pharmacy needed at all. %s and follow me, and the complete "
         "step by step arrives right in your messages." % CTA_LITERAL,
     ]},
    {"id": "bat_canos", "curto": "o bastao · canos limpos", "mec": True,
     "cenas": [
"My bat was soft every night and I stopped reaching for her at "
         "all. Two things off this shelf gave me my nights back.",
"Once the pipes are finally clear you get maximum size and rock "
         "solid endurance, every single time, without one pill.",
"No pills and no pharmacy. %s and follow me, and the full step "
         "by step lands right in your messages." % CTA_LITERAL,
     ]},

    # -- FAMILIA 5 — a noite toda, no presente -----------------------------
    # ⭐ A prova e' ele AGORA, nao um antes/depois. E' o unico registro do lote
    # que nao confessa falha nenhuma.
    {"id": "noite_hack", "curto": "ainda duro a noite toda", "mec": True,
     "cenas": [
"I am %(idade)d and I still last all night. Nobody believes me "
         "until I tell them what I keep on my shower shelf.",
"It flushes out the toxic buildup choking your blood flow. No "
         "more going soft, no more apologizing, and no more pharmacy.",
"No pharmacy at all. %s and follow me, and the full step by "
         "step goes straight to your messages." % CTA_LITERAL,
     ]},
    {"id": "noite_prateleira", "curto": "a noite toda · duas coisas",
     "mec": True,
     "cenas": [
"I was going soft and my marriage was going with it. Two things "
         "off this bathroom shelf are the reason I last all night now.",
"They flush out the toxic buildup that is choking your blood "
         "flow down there, and you do it while you are already in the "
         "shower.",
"%s and follow me so I can send you the full step by step, "
         "straight to your messages, in a couple of minutes." % CTA_LITERAL,
     ]},

    # -- FAMILIA 6 — nega a causa falsa antes de vender a verdadeira -------
    {"id": "idade_causa", "curto": "nao e' idade · tem causa", "mec": True,
     "cenas": [
"I was going soft and everyone told me it was just my age. It "
         "was never my age. This bizarre bath method proved that.",
"This shower hack flushes out the toxic buildup and forces the "
         "blood back down there. Age was never the real problem here.",
"%s and follow me right now, and every single step goes "
         "straight to your messages, free, in a couple of minutes." % CTA_LITERAL,
     ]},
    # ⚠️ EDITADA POR ELE. E o `Segue primeiro` que ele escreveu SAIU, por fato:
    # *"a mensagem e' enviada independente de seguirem ou nao"* (10/08). Follow
    # como condicao promete um portao que a automacao nao tem. Ele autorizou
    # (*"tanto faz, a parte de seguir nao e' tao importante"*).
    {"id": "idade_nunca", "curto": "nunca foi por idade", "mec": True,
     "cenas": [
"I never went soft because of my age, and I can prove it. This "
         "strange shower routine is the thing my wife thanks now.",
"This shower trick forces the blood back down there. Hard as a "
         "rock again, and nobody around you has to know why.",
"%s and follow me as well, and the full step by step arrives "
         "right in your messages, at no cost." % CTA_LITERAL,
     ]},

    # -- FAMILIA 7 — as pilulas abandonadas --------------------------------
    # ⭐ A prova e' o que ele DEIXOU de tomar. Vem do original de 101k
    # (*"I am 65 and I ditched the blue pills"*), que na fonte era so' um beat
    # perdido no meio — aqui ele vira o hook.
    {"id": "pilula_fora", "curto": "joguei fora os azuis", "mec": True,
     "cenas": [
"I threw out the blue pills eight months ago and I never went "
         "back. This bizarre bath method does what they used to do.",
"This mixture clears out what is choking your blood flow. No "
         "prescription, no pharmacy, no monthly bill, and no side "
         "effects.",
"%s and follow me right now, and the step by step goes straight "
         "to your messages, free of charge." % CTA_LITERAL,
     ]},
    # ⚠️ EDITADA POR ELE — e e' aqui que entra `pipe`, que junto com `bat` da
    # familia 4 decide o E3: o vocabulario do orgao neste motor e' o da FONTE,
    # nao o `so' Johnson/manhood` do `banho16`.
    {"id": "pilula_troca", "curto": "troquei os azuis pelos itens", "mec": True,
     "cenas": [
"I swapped the blue pills for two things off this shelf. My "
         "wife noticed before I said a single word to her about it.",
"They clear the toxic buildup choking the blood in your pipe. "
         "No side effects, no doctor visit, and no monthly bill.",
"%s and follow me so I can send you the whole step by step, "
         "straight to your messages, tonight." % CTA_LITERAL,
     ]},
]



# ===========================================================================
# SORTEIO
# ===========================================================================

def _falas(spec, rng, quais=(0, 1, 2)):
    """As TRES falas — e elas vem da MESMA familia, sempre.

    ⛔⛔ AQUI NAO HA' SORTEIO POR BEAT, e essa e' a diferenca arquitetural
    inteira em relacao ao `banho16`. La' o hook vem de um pool e o fecho de
    outro, independentes; aqui a familia e' ATOMICA. Trocar a cena 2 de um
    video sem trocar a 1 produziria um par que ninguem aprovou — e as doze
    foram aprovadas COMO CONJUNTO, uma a uma.
    ⭐ Por isso `trocar_fala` neste motor troca a FAMILIA inteira: e' a unica
    troca que preserva o que o operador carimbou.
    """
    fam = spec["familia"]
    d = {"idade": spec["idade"]}
    f = dict(enumerate(spec.get("falas", ["", "", ""])))
    for i in quais:
        f[i] = fam["cenas"][i] % d
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

    # ⭐⭐ A FAMILIA DE COPY — o eixo mais visivel do motor, e por isso o que
    # mais precisa de memoria. Sem ledger, doze familias devolvem a mesma duas
    # vezes seguidas em ~8% dos pares, e e' exatamente disso que o operador
    # reclamou no `banho16` (*"sempre muito parecida uma com a outra"*).
    # ⛔ O FILTRO `mec` VEM ANTES da frescura: pre-selecao do painel e' escolha
    # explicita e vence a memoria.
    quer = travas.get("mecanismo")
    pool_f = FAMILIAS
    if quer == "sem":
        pool_f = [x for x in FAMILIAS if not x["mec"]]
    elif quer == "com":
        pool_f = [x for x in FAMILIAS if x["mec"]]
    familia = (_por_id(FAMILIAS, travas["familia"]) if travas.get("familia")
               else _fresco(pool_f or FAMILIAS, hist.get("familia", [])[-5:],
                            rng))

    spec = {
        "pagina": pagina, "etnia": etnia,
        "banheiro": banheiro, "superficie": superficie, "medida": medida,
        "rotulo": rotulo, "receita": receita,
        "pessoa": pessoa, "homem": homem,
        "traje": rng.choice(TRAJES),
        # ⛔ A MAO ENTROU NO LEDGER (2026-08-14, integrando o Eduardo). Ela
        # era o unico eixo deste motor sorteado com `rng.choice` CRU, sem
        # memoria nenhuma — e sem rosto, a mao E' a identidade do narrador.
        # ⚠️ O repo ja' pagou exatamente isto no `pee16`: *pool grande com
        # sorteio sem memoria repete igual*, e nenhuma ampliacao de pool
        # conserta, porque o problema nunca foi o tamanho.
        "maos": (_por_id(MAOS, travas["maos"]) if travas.get("maos")
                 else _fresco(MAOS, hist.get("maos", [])[-6:], rng)),
        "habitado": _fresco_txt(HABITADOS, hist.get("habitado", [])[-2:], rng),
        # ⛔ TRES DERIVAS DISTINTAS no mesmo video. `rng.sample` garante que os
        # tres takes nunca repitam o mesmo movimento de camera — repetir seria
        # pior que nao ter, porque camera identica em corte seguido e' o que
        # denuncia geracao.
        "derivas": rng.sample(DERIVAS, 3),
        "idade": idade,
        "familia": familia,
        # ⚠️ CAMPO MORTO, mantido so' para o painel compartilhado nao quebrar:
        # as doze copies do operador ja' trazem o vocabulario do orgao escrito
        # (`bat`, `pipe`) ou nao trazem nenhum. Sortear apelido aqui seria
        # inventar palavra dentro de copy aprovada.
        "apelido": familia["id"],
    }
    spec["falas"] = [v for _, v in sorted(_falas(spec, rng).items())]
    return spec


def nova_fala(spec, i, rng):
    """⛐⛐ AQUI O BOTAO TROCA A FAMILIA INTEIRA, e devolve a cena `i`.

    ⚠️ Ela NAO existia, e o botao `trocar` estava MORTO: a UI procura
    `nova_fala(spec, i, rng)` e o que havia era `trocar_fala(spec, rng, i)` —
    outro nome, outra ordem. Defeito herdado por copia do `banho16`.

    ⛔ E NAO DA' PARA TROCAR UMA CENA SOZINHA neste motor, por desenho: as
    doze familias foram aprovadas pelo operador COMO CONJUNTO, uma a uma, e
    cada uma tem exatamente uma linha por cena. Trocar so' a cena 2 significaria
    colar o mecanismo de uma familia no hook de outra — um par que ninguem
    aprovou, e que a lente BA9 reprova na hora.
    ⭐ Por isso a funcao re-sorteia a FAMILIA e a UI redesenha as tres caixas.
    """
    atual = spec["familia"]["id"]
    nova = _fresco([x for x in FAMILIAS if x["id"] != atual], [], rng)
    spec["familia"] = nova
    spec["apelido"] = nova["id"]
    spec["falas"] = [v for _, v in sorted(_falas(spec, rng).items())]
    return spec["falas"][i]


def trocar_fala(spec, rng, i):
    """⛔ Troca a FAMILIA inteira, nunca uma cena solta — ver `_falas`."""
    nova = _fresco([x for x in FAMILIAS if x["id"] != spec["familia"]["id"]],
                   [], rng)
    spec["familia"] = nova
    spec["apelido"] = nova["id"]
    spec["falas"] = [v for _, v in sorted(_falas(spec, rng).items())]
    return spec["falas"][i]


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
    # ⛔⛔ A VOZ E' UM BLOCO TRAVADO E REPETIDO PALAVRA POR PALAVRA nos tres
    # takes. Ordem do operador: *"Ajuste o prompt para a voz do narrador sair
    # igual nos 3 takes"*. Com dois takes dava para relaxar; com TRES quadros
    # gerados separadamente, qualquer variacao de descricao devolve tres
    # homens diferentes lendo o mesmo texto.
    # ⭐ A idade entra na voz (nao so' a decada) porque e' o que amarra a voz
    # as' MAOS — os dois leem o mesmo `spec["idade"]`.
    # ⛔⛔ `slow deliberate cadence` SAIU em 2026-08-20, por ordem do
    # operador: *"fala lenta = menos espaco de tempo pra copy = jogando
    # tempo de copy falada que vale ouro fora no lixo"*.
    # ⚠️ Medido: a voz dos nossos renders sai a 2,62 palavras/segundo
    # contra 3,49 dos reels reais da fonte. A diferenca NAO era limite do
    # gerador — era esta linha pedindo lentidao. Num take de 8s isso e'
    # a diferenca entre 21 e 15 palavras faladas.
    # ⛔ E a clausula que entra e' POSITIVA primeiro (ritmo normal) e so'
    # depois nega o arrastar. E' copia da constante `RITMO` do
    # `clean_v1_16s`, que e' string ja' validada em campo.
    # ⛔⛔ `Exactly the same voice in all three takes` NAO FAZ NADA
    # sozinho, e o operador viu isso em campo em 2026-08-20: *"toda hora
    # num take aleatorio e um timbre diferente"*. Cada take e uma chamada
    # de video SEPARADA — o modelo ve UM take por vez e nao tem o anterior.
    # Pedir "a mesma voz dos outros tres" e ANAFORA, o mesmo defeito de
    # dizer `the same counter as before` no ambiente: nao ha "before".
    # ⭐ O que faz tres geracoes independentes convergirem e a DESCRICAO
    # ser especifica o bastante para caber uma voz so — mesma logica do
    # BLOCO 0 para o rosto. Saem dois adjetivos vagos e entram CINCO eixos
    # reproduziveis: altura, corpo, textura, sotaque e volume.
    voz = ("Voice: one %d-year-old %s man with a plain everyday American "
           "accent, pitched low in the chest, dry and slightly gravelly, "
           "close to the microphone at ordinary conversational volume, "
           "never raised and never whispered, speaking straight to camera "
           "at the ordinary pace of everyday American speech, never "
           "stretching or slowing the words to fill the take. The pitch, "
           "the texture, the accent and the speed are identical in all "
           "three takes." % (spec["idade"], spec["etnia"]))

    # ⛔ A GEOMETRIA DA AGUA, dita e nao proibida.
    # ⛔ AO FUNDO, e nao "afastada". O conserto anterior empurrou o jato para
    # a parede lateral e em varios renders a agua sumiu do quadro — e o
    # operador, mostrando a fonte, apontou justamente *"a agua caindo ao
    # fundo"* como parte do que ele quer ver. Ela fica ATRAS, visivel, e nao
    # encosta na prateleira.
    agua = ("The shower runs in the background behind the shelf, the falling "
            "water clearly visible the whole time, and none of it reaches the "
            "shelf or anything on it.")
    # ⭐ FORMA CURTA PARA AS IMAGENS. Numa foto parada `the falling water
    # clearly visible the whole time` nao quer dizer nada — `the whole time`
    # e' duracao, e foto nao tem duracao. A clausula longa fica onde ela
    # governa movimento (os TAKEs) e sai de onde e' so' peso.
    # ⛔ O que NAO sai de lugar nenhum e' a segunda metade: *"a agua do
    # chuveiro ou torneira nunca deve cair dentro dos ingredientes"* e' ordem
    # literal do operador (E6).
    agua_img = ("The shower runs in the background behind the shelf, and none "
                "of the water reaches the shelf or anything on it.")

    cena = ("%s, brightly and evenly lit. %s On %s, grouped close together in "
            "the middle, stand %s, %s and %s. %s leans upright against the "
            "wall at the left end of the shelf, whole and fully visible, "
            "covering nothing. %s stands flat against the wall at the right "
            "end, large and completely unobstructed. Further back, %s."
            % (_cap(b["cen"]), agua_img, sup["sup"], r["vaso"], GELATINA, COLHER,
               _cap(med["img"]), _cap(rot["img"]), spec["habitado"]))

    # ⚠️ SEM ARTIGO: o IMAGE 02 diz "the same %s" e o artigo embutido gerava
    # "come the same THE hands of a 62-year-old...". Artigo e' da frase, nao do
    # dado — mesma classe do `held upright, held upright` do TRIO.
    # ⭐ A MAO E' A ANCORA, e por isso ela carrega SEMPRE as mesmas camadas:
    # idade + etnia + tom de pele + a arquitetura fixa (`ANCORA_MAO`) + a
    # variacao do pool. Sem rosto, tres quadros gerados separadamente so'
    # viram a mesma pessoa se a mao for descrita identica nos tres.
    # ⚠️ DUAS FORMAS, e nao uma. A primeira versao usava a mesma string nos
    # dois lugares e a IMAGE 01 saiu com *"is the right hand of the hands of a
    # 69-year-old man"*. Quando UMA mao entra em quadro a frase e' outra —
    # artigo e numero sao da frase, nao do dado (mesma classe do `held
    # upright, held upright` do TRIO).
    adj, det = _maos_partes(spec["maos"]["desc"])
    pele = TOM_PELE.get(spec["etnia"], "weathered skin")
    maos = ("the %s hands of a %d-year-old %s man, %s, with %s, %s"
            % (adj, spec["idade"], spec["etnia"], pele, det, ANCORA_MAO))
    mao_uma = ("the right hand of a %d-year-old %s man, %s, a %s hand with "
               "%s, %s"
               % (spec["idade"], spec["etnia"], pele, adj, det, ANCORA_MAO))

    if spec["pessoa"]:
        quem1 = ("A %d-year-old %s man stands with his back half to the "
                 "camera, %s, %s, wearing %s, one hand reaching toward the %s."
                 % (h["idade"], spec["etnia"], h["cabeca"], h["marca"],
                    spec["traje"], r["vaso_nome"]))
    else:
        quem1 = ("Coming in close to the lens from the bottom of the frame, "
                 "large in the picture, is %s, reaching toward the %s, "
                 "fingers open and about to touch it."
                 % (mao_uma, r["vaso_nome"]))

    # -- IMAGE 01 — os props parados e a mao ALCANCANDO ---------------------
    # ⛔ Em 2 takes o hook ja' abria no despejo. Com 3, o hook ganhou um quadro
    # so' para o ARRANJO — e' o unico momento em que a placa e a medida sao
    # lidas sem nada acontecendo em cima delas.
    b1 = ("%s %s %s %s %s %s %s"
          % (ORIENTACAO, ENQUADRAMENTO, cena, quem1, DEZ_DEDOS,
             _cap(b["luz"]), CAUDA))

    t1 = ("TAKE 01/03: Animate the provided image exactly. Handheld iPhone "
          "shot, very slight natural sway, no cuts. As the line begins the "
          "hand closes the last inches and taps the %s twice with the index "
          "finger. Halfway through the line it sweeps slowly across the three "
          "products, palm down. As the line ends it settles on the shelf. "
          "Nothing is picked up, nothing is opened, nothing is poured. "
          "%s %s %s %s\n"
          'Dialogue: "%s"\n%s\nAudio: %s. No music.'
          % (r["vaso_nome"], NAO_TOCA % med["nome"], agua, DEZ_DEDOS,
             spec["derivas"][0], sonorizar(spec["falas"][0]), voz, b["audio"]))

    # -- IMAGE 02 e 03 — MAIS PERTO ----------------------------------------
    # ⛔⛔ A CENA INTEIRA **NAO** SE REPETE NAS TRES. O `banho16` repete, e com
    # dois blocos isso custava 300 palavras; com tres o primeiro lote saiu com
    # IMAGEs de 402, 422 e 446 palavras — contra o veredito do proprio operador
    # sobre este angulo: *"e' so' fazer uma cena SIMPLES aqui, nao precisa de
    # muita coisa"* (ele reprovou um bloco de 329).
    # ⭐ E a fonte resolve isso do jeito certo: os quadros 2 e 3 dela sao
    # *"tighter framing centered on the products"*. Enquadramento mais fechado
    # e' motivo NARRATIVO para o inventario nao reaparecer — o que precisa
    # sobreviver ao corte e' so' o que a continuidade exige: a superficie, o
    # recipiente, a medida e o rotulo.
    # ⚠️ AQUI A MEDIDA E O ROTULO ENTRAM PELO NOME CURTO, nao pela descricao
    # inteira. A IMAGE 01 ja' estabeleceu os dois; repetir `a soft tailor's
    # tape measure, unrolled and straight` nos tres quadros custa ~30 palavras
    # por bloco e nao acrescenta nada — o que a continuidade exige e' que eles
    # CONTINUEM EM QUADRO e no mesmo canto, e e' isso que a frase diz.
    perto = ("Same place, same shelf, same light, tighter framing on the "
             "products: %s, with the %s still leaning at the left end and the "
             "hand-written GROWTH HACK sign still flat against the wall at "
             "the right end, both whole and unobstructed. %s"
             % (sup["sup"], med["nome"], agua_img))

    b2 = ("%s %s %s Coming in close to the lens from the bottom of the frame, "
          "large in the picture, come the same %s: the left hand holds the %s "
          "steady from below while the right hand tips the torn paper sachet "
          "over it, a fine stream of white powder falling in. %s %s %s"
          % (ORIENTACAO, ENQUADRAMENTO, perto, maos, r["vaso_nome"],
             DEZ_DEDOS, _cap(b["luz"]), CAUDA))

    # ⭐ TRES GESTOS CRONOMETRADOS por take, e nao um. E' a diferenca de
    # construcao mais visivel entre a fonte e o nosso `banho16`: la' cada take
    # amarra 2-3 gestos a pontos da fala, aqui havia UMA acao por take.
    # ⚠️ A fonte amarra CITANDO a fala (*On "these two bathroom items" his hand
    # sweeps..."*). Aqui nao da': o AdBatch le' a fala pela linha `Dialogue:`,
    # e repetir as palavras no corpo do bloco pede ao gerador que as fale duas
    # vezes. A amarra e' por POSICAO na fala — mesma funcao, sem conflito de
    # contrato.
    t2 = ("TAKE 02/03: Animate the provided image exactly. Handheld iPhone "
          "shot, very slight natural sway, no cuts. As the line begins the "
          "powder keeps falling from the sachet into the %s at the same steady "
          "rate, and %s. Halfway through the line the empty sachet is set down "
          "on the shelf. As the line ends the right index finger dips in and "
          "stirs the mixture in slow circles. The %s stays where it is and "
          "nothing else enters the frame. %s %s %s %s\n"
          'Dialogue: "%s"\n%s\nAudio: %s, and a soft wet sound as the finger '
          "stirs. No music."
          % (r["vaso_nome"], r["meio"], med["nome"],
             NAO_TOCA % med["nome"], agua, DEZ_DEDOS, spec["derivas"][1],
             sonorizar(spec["falas"][1]), voz, b["audio"]))

    # -- IMAGE 03 — A REACAO -----------------------------------------------
    # ⭐⭐ O quadro que o formato de 2 takes nao tinha espaco para ter. A colher
    # de ambar parada NO AR sobre o recipiente, o primeiro fio comecando a
    # cair: e' a imagem que o take 3 anima ate' a erupcao.
    b3 = ("%s %s %s The white powder is already stirred into the %s. Coming in "
          "close to the lens from the bottom of the frame, large in the "
          "picture, come the same %s: the left hand holds the %s steady from "
          "below while the right hand holds the metal spoon full of thick "
          "amber honey just above the opening, tipped, the first thread "
          "beginning to fall, and the surface below already showing the first "
          "small bubbles. %s %s %s"
          % (ORIENTACAO, ENQUADRAMENTO, perto, r["vaso_nome"], maos,
             r["vaso_nome"], DEZ_DEDOS, _cap(b["luz"]), CAUDA))

    t3 = ("TAKE 03/03: Animate the provided image exactly. Handheld iPhone "
          "shot, very slight natural sway, no cuts. As the line begins the "
          "spoon tips fully and the amber honey pours down into the %s, and %s. "
          "Halfway through the line the spoon is pulled back and rests against "
          "the rim. As the line ends the foam is still working inside and the "
          "hand settles beside the %s. Nothing else enters the frame. %s %s %s "
          "%s\n"
          'Dialogue: "%s"\n%s\nAudio: %s, and a loud fizzing and crackling '
          "from inside the %s. No music."
          % (r["vaso_nome"], REACAO, r["vaso_nome"], NAO_TOCA % med["nome"],
             agua, DEZ_DEDOS, spec["derivas"][2], sonorizar(spec["falas"][2]),
             voz, b["audio"], r["vaso_nome"]))

    # ⭐⭐ BLOCO 0 (REF) — E ELE E' AS MAOS.
    # ⛔ A falta dele quebrou o painel compartilhado (`KeyError 'BLOCO 0
    # (REF)'`), e a quebra apontou uma lacuna REAL: este angulo nao tinha
    # ancora nenhuma entre os dois takes. Todos os outros motores amarram a
    # continuidade num ROSTO; aqui nao ha' rosto — entao a ancora sao as MAOS,
    # que e' o unico corpo em quadro.
    # ⚠️ E foi o primeiro lote que provou o tamanho do problema: sem ancora
    # forte, o take 2 saiu noutro comodo.
    # ⛔⛔ ESTE MOTOR NAO TEM `BLOCO 0 (REF)`, e e' o unico dos 44 assim.
    # Ordem do operador (2026-08-14), testando o app: *"A imagem do bloco 0
    # desse agente e' completamente irrelevante, posso anexar direto a imagem 1
    # como referencia"*.
    #
    # ⭐ E ele esta' certo pela ESTRUTURA do angulo, nao so' por conveniencia.
    # O BLOCO 0 existe para dar uma ancora de continuidade quando os quadros
    # sao gerados separadamente — nos outros motores e' um ROSTO, que nao
    # aparece em nenhuma cena e por isso precisa de foto propria. Aqui a ancora
    # e' a MAO, e a mao ja' esta' na IMAGE 01, na mesma luz e no mesmo
    # banheiro. Uma foto de maos sobre fundo cinza e' uma referencia PIOR que a
    # propria cena: menos informacao, e nenhuma continuidade de iluminacao.
    #
    # ⚠️ O `banho16` V1/V2 CONTINUAM com o BLOCO 0 — a ordem nomeia *"desse
    # agente"*, e eles tem dois takes, nao tres.
    # ⚠️ E o cabecalho do `banho16` registra que tirar o BLOCO 0 ja' quebrou o
    # painel compartilhado uma vez (`KeyError 'BLOCO 0 (REF)'`). Conferido
    # antes de tirar: a UI hoje procura com `next(..., None)` e avisa em vez de
    # estourar, e a lente que EXIGE o cabecalho REF vive no `sc.lint_curto`,
    # que este motor nao chama. Medido, nao suposto.
    blocos = sc.selar_takes(sc.selar_tags({
        IMAGENS[0]: b1, TAKES[0]: t1,
        IMAGENS[1]: b2, TAKES[1]: t2,
        IMAGENS[2]: b3, TAKES[2]: t3,
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
    # ⛔⛔ E A LENTE COBRA A FUNCAO, NAO O LITERAL. A primeira versao procurava
    # a descricao INTEIRA do pool (`a soft tailor's tape measure, unrolled and
    # straight`) nas tres imagens — e quando as IMAGEs 02 e 03 passaram a citar
    # o instrumento pelo nome curto (que e' o certo: mais perto, ja'
    # estabelecido), ela reprovou 800 blocos CORRETOS. Lente colada na FORMA da
    # string acusa a si mesma na primeira reescrita; o que ela tem de garantir
    # e' que o instrumento CONTINUE EM QUADRO.
    # ⚠️ A IMAGE 01 e' a unica que ainda precisa da descricao inteira — e' ela
    # que estabelece o objeto.
    if spec["medida"]["img"].lower() not in blocos.get(IMAGENS[0], "").lower():
        ach.append(("ERRO", "BA1: %s sem a descricao do instrumento de medida "
                            "— e' a IMAGE que estabelece o objeto"
                    % IMAGENS[0]))
    for nome in IMAGENS[1:]:
        if spec["medida"]["nome"].lower() not in blocos.get(nome, "").lower():
            ach.append(("ERRO", "BA1: %s sem o instrumento de medida — e' o "
                                "unico lugar onde o `bigger` aterrissa" % nome))
    for nome in TAKES:
        if "or touches the" not in blocos.get(nome, ""):
            ach.append(("ERRO", "BA1: %s sem a trava de nao tocar a medida — "
                                "mao na regua vira demonstracao, e demonstracao "
                                "de tamanho e' recusa certa" % nome))


def _ba9_familia(spec, blocos, ach):
    """⛔⛔ BA9 — A COPY APROVADA CHEGA AO TAKE PALAVRA POR PALAVRA.

    ⭐ E' a lente mais importante deste motor, e ela existe por causa da
    natureza do material: as doze copies foram aprovadas UMA A UMA pelo
    operador, em duas rodadas, com ele reescrevendo seis delas na mao. Copy
    assim nao pode ser reformatada, comprimida nem "melhorada" no caminho ate'
    o bloco — se chegar diferente, o que ele carimbou nao e' o que vai ao ar.
    ⛔ Ela tambem e' a substituta honesta da lente de painel para o eixo
    `familia`: em vez de perguntar se o ROTULO em portugues aparece no prompt
    (nunca aparece), pergunta se o EFEITO da familia aparece — que e' a
    pergunta que a lente de painel queria fazer desde o comeco.
    ⚠️ Compara depois do `sonorizar`, que e' o unico transformador legitimo no
    caminho; qualquer outra diferenca e' perda.
    """
    for i, (take, fala) in enumerate(zip(TAKES, spec["falas"]), 1):
        alvo = 'Dialogue: "%s"' % sonorizar(fala)
        if alvo not in blocos.get(take, ""):
            ach.append(("ERRO", "BA9: a cena %d da familia %r nao chegou "
                                "intacta ao %s — copy aprovada nao se "
                                "reescreve no caminho"
                        % (i, spec["familia"]["id"], take)))
    # ⛔ E as tres tem de vir da MESMA familia. Sortear beat a beat foi o
    # defeito de arquitetura do `banho16` que este motor existe para nao ter.
    esperado = [c % {"idade": spec["idade"]} for c in spec["familia"]["cenas"]]
    if list(spec["falas"]) != esperado:
        ach.append(("ERRO", "BA9: as tres falas nao sao as tres cenas da "
                            "familia %r — beat solto de familia trocada e' "
                            "par que ninguem aprovou" % spec["familia"]["id"]))


def _ba2_rotulo(spec, blocos, ach):
    """⭐ BA2 — O ROTULO `growth hack` NOS DOIS TAKES.

    ⚠️ MEDIDO nos 7 videos: com rotulo, media de 108,5k views e mediana de
    2.300 comentarios; sem rotulo, 67k e 374. Sete pontos e' indicio, nao
    prova — mas custa nada e os dois melhores o tem.
    """
    for nome in IMAGENS:
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
        if "man stands" not in blocos.get(IMAGENS[0], ""):
            ach.append(("ERRO", "BA3: MODO PESSOA ligado e o take 1 nao tem "
                                "homem em quadro"))
        return
    for nome in IMAGENS + TAKES:
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
    # ⭐ A COBRANCA AGORA E' SOBRE A FALA REAL, nao sobre um campo `abertura`
    # que este motor nao tem mais: as doze familias sao aprovadas inteiras, e
    # sete delas dizem a idade no hook. Perguntar ao TEXTO se ele anuncia um
    # numero e' mais honesto do que perguntar a um rotulo de sorteio — e vale
    # tambem para a copy que entrar amanha.
    fala1 = spec["falas"][0]
    anuncia = re.search(r"\bI am %d\b|\bI'm %d\b" % (spec["idade"],
                                                     spec["idade"]), fala1)
    if anuncia and "%d-year-old" % spec["idade"] not in blocos.get(IMAGENS[0],
                                                                  ""):
        ach.append(("ERRO", "BA4: a fala anuncia %d e a IMAGE 01 nao renderiza "
                            "essa idade" % spec["idade"]))
    if not spec.get("pessoa"):
        return
    if spec["idade"] != spec["homem"]["idade"]:
        ach.append(("ERRO", "BA4: a fala diz %d e o homem em quadro tem %d"
                    % (spec["idade"], spec["homem"]["idade"])))


def _ba5_apelido(spec, blocos, ach):
    """⛔⛔ BA5 — O VOCABULARIO DO ORGAO E' O DA FONTE, E UM SO' POR VIDEO.

    ⚠️ ESTA LENTE MUDOU DE REGRA em relacao ao `banho16`, e a mudanca e' do
    OPERADOR, nao minha. La' vale o D7 (*"somente jonhson e manhood"*). Aqui
    ele aprovou, uma a uma, copies que dizem `bat` (familia 4, duas entradas)
    e `pipe` (familia 7.2, que ele mesmo editou para incluir *"a circulacao do
    seu cano"*). Aprovar a copy E' decidir o vocabulario — e' a decisao E3.
    ⛔ O que NAO mudou e' o resto: os termos clinicos e os vulgares continuam
    fora, e continua valendo UM apelido por video (CT4). O que a fonte usa e
    o operador carimbou entra; o que nenhum dos dois usou, nao.
    """
    permitidos = NUCLEO + APELIDOS_FONTE
    texto = " ".join(spec["falas"])
    for proibido in ("pecker", "wiener", "cock", "dick", "penis", "schlong"):
        if re.search(r"\b%s\b" % proibido, texto, re.I):
            ach.append(("ERRO", "BA5: a fala usa %r — fora do vocabulario "
                                "aprovado %s" % (proibido, list(permitidos))))
    # ⛔ CT4 — UM apelido por video. Com copy aprovada em FAMILIA isto nunca
    # deveria disparar; a lente fica porque copy nova entra por aqui, e o dia
    # em que entrar uma familia que mistura `bat` e `pipe` o corte de 5s nao
    # da' ao ouvinte tempo de remapear.
    usados = sorted({t for t in permitidos
                     if re.search(r"\b%s\b" % t, texto, re.I)})
    if len(usados) > 1:
        ach.append(("ERRO", "BA5/CT4: dois apelidos no mesmo video (%s)"
                    % ", ".join(usados)))


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
    # ⛔ CENA 3, nao mais cena 2 — o CTA mudou de casa com o terceiro take.
    # ⭐ E a lente ganhou a forma SEQUENCIAL (`follow first`, `follow before`):
    # foi assim que o portao voltou a aparecer em 14/08, na familia 6.2 que o
    # operador escreveu (*"Segue primeiro"*). Condicao nao precisa de `or` para
    # ser condicao — basta dizer que uma coisa vem antes da outra.
    f3 = spec["falas"][2]
    if re.search(r"follow[^.]*\b(or|otherwise|unless)\b", f3, re.I):
        ach.append(("ERRO", "BA7: o follow virou CONDICAO — a DM sai igual, e "
                            "prometer o contrario e' mentira"))
    if re.search(r"\bfollow\b[^.]*\b(first|before)\b", f3, re.I):
        ach.append(("ERRO", "BA7: o follow virou PRE-REQUISITO ('follow "
                            "first') — a DM sai igual, seguindo ou nao"))


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
    # ⛔ O CTA MUDOU DE CENA: com dois takes ele dividia a cena 2 com o
    # mecanismo; com tres ele tem a cena 3 inteira. Toda lente de CTA leu
    # `falas[1]` ate' aqui — deixar como estava faria as lentes olharem o
    # PREPARO e aprovarem um video sem CTA nenhum.
    sc.lint_isca_cta(falas[2], ach, "a cena 3 (CTA)")
    # ⛔ literal LOCAL: a keyword deste agente e' `Recipe` (ordem do operador
    #    14/08), nao o `gelatin` do repo.
    if CTA_LITERAL not in (falas[2] or ""):
        ach.append(("ERRO", "a cena 3 sem o literal %r" % CTA_LITERAL))
    sc.lint_take_vs_image(blocos, ach)
    sc.lint_painel_honesto(sys.modules[__name__], spec, blocos, ach)
    # ⛔ `isca_absurda=False`: este angulo nao tem substancia absurda nenhuma.
    _ct = []
    sc.lint_copy16(sys.modules[__name__], spec, _ct, isca_absurda=False)
    ach.extend(x for x in _ct if not x[1].startswith(_CT_DESLIGADOS))
    for f in (_ba1_medida, _ba2_rotulo, _ba3_sem_pessoa, _ba4_idade,
              _ba5_apelido, _ba6_leve, _ba7_follow, _ba8_coerencia,
              _ba9_familia):
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

# ⭐ A FAMILIA DE COPY E' O PRIMEIRO EIXO DO PAINEL, e nao um detalhe no fim
# da lista: e' o unico eixo que muda o que o video DIZ. Os outros mudam onde
# ele acontece.
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
    ("familia", "A COPY", "FAMILIAS", "curto"),
    ("banheiro", "O BANHEIRO", "BANHEIROS", "id"),
    ("superficie", "A SUPERFICIE", "SUPERFICIES", "curto"),
    ("medida", "A MEDIDA", "MEDIDAS", "curto"),
    ("rotulo", "O ROTULO", "ROTULOS", "curto"),
    ("receita", "A RECEITA", "RECEITAS", "curto"),
]
EIXOS_TRAVAVEIS = ["familia", "banheiro", "superficie", "medida", "rotulo",
                   "receita"]
# ⭐⭐ A PRE-SELECAO `mecanismo` E' O EXPERIMENTO, e por isso ela esta' na
# tela e nao escondida no codigo: e' com ela que o operador roda 15 videos de
# cada lado e o campo responde o que a fonte, com sete pontos e tres
# diferencas simultaneas, nao respondeu.
# ⭐⭐ O SELETOR FIXO DE REF, sexto contrato da UI, que o Eduardo criou em
# 2026-08-14 e levou aos 22 motores 16s. ⛔ Este motor nasceu de uma copia
# ANTERIOR a essa mudanca e ficaria de fora em silencio — botao ausente num
# agente e' o defeito que o operador descobre tarde, achando que o agente e'
# que nao suporta.
# ⚠️ Aqui o REF **e' a mao**: nao ha' rosto neste angulo, entao o eixo
# `maos` e' o unico que fixa quem narra.
DROPDOWNS_UI = [("maos", "AS MAOS", "MAOS", "rotulo")]

TRAVAS_UI = [("familia_banheiro", "cenario", ["livre"] + FAMILIAS_BANHEIRO),
             ("mecanismo", "explica?", ["livre", "com", "sem"])]

# ⚠️ `banheiro` e `receita` provam-se por outros literais que nao o campo do
# painel (`cen` e `vaso`), entao ficam de fora da lente de honestidade.
# ⚠️ `familia` ENTRA AQUI, MAS NAO FICA SEM GUARDA. A lente compartilhada
# procura o texto do painel dentro de um bloco, e o rotulo da familia e' em
# PORTUGUES (`solteiro/casado · nao encosta`) — nunca vai aparecer num prompt
# em ingles, entao ela acusaria 400 de 400 videos certos. ⛔ Desligar sem
# substituir seria o padrao que este repo mais paga: o eixo com a memoria
# apagada. Quem cobra a familia agora e' a BA9, e ela cobra MAIS: as tres
# falas, verbatim, nas tres linhas `Dialogue:`.
IGNORA_PAINEL = ("banheiro", "receita", "familia")

# ⛔ Nenhum eixo do painel mexe na copy: a fala nao cita o banheiro, a
# superficie, a medida nem o recipiente. Declarar o dicionario vazio e'
# declarar que alguem verificou, em vez de deixar o `getattr` decidir.
def _refazer_falas(spec, rng):
    """⛔⛔ O eixo `A COPY` mexe na FALA, e a UI precisa ser avisada disso.

    ⚠️ DEFEITO REAL, filmado pelo operador em 2026-08-14: ele clicava em
    `trocar` na linha **A COPY** e o painel trocava o ROTULO da familia sem
    trocar as tres falas. O resultado era um video que dizia ser da familia
    `pilula_troca` com a copy da `noite_hack` — e a lente BA9 acusava, na
    barra de baixo, a cada clique.
    ⭐ A BA9 fez o trabalho dela: o defeito apareceu como ERRO na tela em vez
    de sair no lote. Mas lente que acusa a cada clique legitimo treina o
    operador a ignorar a barra — o conserto e' aqui, nao na lente.

    ⛔ A CAUSA E' DE HERANCA: este motor nasceu por copia do `banho16`, onde
    `EIXOS_QUE_MEXEM_NA_COPY` e' `{}` com razao — la' NENHUM eixo do painel
    toca a copy (banheiro, superficie, medida, rotulo e receita sao todos de
    CENA). Aqui eu acrescentei um eixo que E' a copy e trouxe o dicionario
    vazio junto. Copiar um motor copia tambem as declaracoes que deixaram de
    valer.
    """
    spec["apelido"] = spec["familia"]["id"]
    spec["falas"] = [v for _, v in sorted(_falas(spec, rng).items())]


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


EIXOS_QUE_MEXEM_NA_COPY = {"familia": _refazer_falas,
                           "banheiro": _coerir_cena,
                           "superficie": _coerir_cena}


def resumo_pt(spec):
    return ("16s, TRES takes de ~5s, %s. Take 1 — O HOOK: os props em %s (%s, "
            "caixa de gelatina e colher de mel), %s ao lado INTOCADA, %s na "
            "parede; %s — a mao so' ALCANCA e toca o recipiente, nada abre. "
            "Take 2 — O PREPARO: o sache rasga e o po cai no recipiente, o "
            "dedo mexe. Take 3 — A REACAO: o mel entra e a mistura ERUPCIONA "
            "em espuma, contida abaixo da borda; fecha no CTA RECIPE. "
            "Copy: familia %s (%s). Idade falada: %d."
            % (spec["banheiro"]["id"].replace("_", " "),
               spec["superficie"]["curto"], spec["receita"]["curto"],
               spec["medida"]["curto"], spec["rotulo"]["curto"],
               ("um homem de %d anos de costas no espelho (MODO PESSOA "
                "LIGADO)" % spec["homem"]["idade"]) if spec["pessoa"]
               else "so' as MAOS entram em quadro (modo pessoa desligado)",
               spec["familia"]["curto"],
               "COM mecanismo" if spec["familia"]["mec"] else "SEM mecanismo",
               spec["idade"]))


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
        eixos["familia"].add(s["familia"]["id"])
        eixos["mecanismo"].add(s["familia"]["mec"])
        eixos["habitado"].add(s["habitado"])
        eixos["maos"].add(s["maos"]["id"])
        eixos["idade"].add(s["idade"])
        for c, f in enumerate(s["falas"], 1):
            dist[c].add(f)
            tam[c].append(_palavras(f))
        for nivel, msg in lint(s, b):
            if nivel == "ERRO":
                erros[msg[:70]] += 1
            else:
                avisos += 1

    print("BANHO 16 3TAKES — %d sorteios (modo pessoa ligado em 1 de 4)" % n)
    for c in sorted(dist):
        v = sorted(tam[c])
        # ⭐ O TEMPO, NAO SO' A PALAVRA. O `medir_teto_fala` do repo conta
        # palavra contra o teto declarado e nunca palavra contra o
        # RELOGIO — entao um motor passa no gate e corta a fala no
        # render. Aqui os dois tempos saem impressos: na voz MEDIANA
        # (2,62 p/s) e na voz LENTA (1,97 p/s, o decimo mais lento dos
        # renders medidos). ⚠️ A coluna da voz lenta ESTOURA os 6s de
        # proposito: e' o preco declarado de encher o take, ordem do
        # operador em 2026-08-20. Fica medido, nao implicito.
        pior = v[-1]
        print("  cena %d: %d falas distintas · palavras min/med/max "
              "%d/%d/%d (teto %d) · no pior caso %.1fs na voz media e "
              "%.1fs na lenta (take de %.0fs)"
              % (c, len(dist[c]), v[0], v[len(v) // 2], v[-1],
                 TETO_FALA[c], pior / TAXA_MEDIA, pior / TAXA_LENTA,
                 SEGUNDOS_TAKE))
    for e in ("banheiro", "superficie", "medida", "rotulo", "receita",
              "familia", "mecanismo", "habitado", "maos", "idade"):
        print("  %-11s %d valores" % (e, len(eixos[e])))
    print("  linter: %d ERRO, %d AVISO" % (sum(erros.values()), avisos))
    for k, v in erros.most_common(5):
        print("     %3dx %s" % (v, k))

    # =======================================================================
    # ⛔⛔ O CONTRATO DAS DOZE FAMILIAS
    # =======================================================================
    # ⚠️ ESTE BLOCO SUBSTITUI o contrato de beats do `banho16` (CT3 no pool de
    # mecanismos, [ALCANCE] cruzando minimos entre pools). Aquele contrato so'
    # faz sentido onde a fala e' MONTADA de pedacos independentes; aqui ela e'
    # aprovada inteira, e o que precisa ser cobrado e' outra coisa: que a copy
    # que o operador carimbou continue chegando ao video **como ele escreveu**.
    idades_prova = (IDADE_MIN, (IDADE_MIN + IDADE_MAX) // 2, IDADE_MAX)
    ids = [f["id"] for f in FAMILIAS]
    if len(set(ids)) != len(ids):
        falhas.append("FAMILIAS: id repetido — o ledger e a trava do painel "
                      "casam por id")
    for fam in FAMILIAS:
        if len(fam["cenas"]) != 3:
            falhas.append("FAMILIA %s: %d cenas, e este motor tem 3"
                          % (fam["id"], len(fam["cenas"])))
            continue
        # ⛔ O TETO VALE PARA TODA IDADE POSSIVEL. Uma cena de 14 palavras com
        # `%(idade)d` continua com 14 — mas se alguem trocar o slot por um
        # numero por extenso, a contagem muda com a idade sorteada e o estouro
        # aparece em 1 video em 40. Provar nos tres extremos custa nada.
        for idade in idades_prova:
            for i, c in enumerate(fam["cenas"], 1):
                n_ = _palavras(c % {"idade": idade})
                if n_ > TETO_FALA[i]:
                    falhas.append("[TETO] familia %s cena %d: %d palavras com "
                                  "idade %d (teto %d) — em 5s isto CORTA"
                                  % (fam["id"], i, n_, idade, TETO_FALA[i]))
                if n_ < PISO_FALA[i]:
                    falhas.append("[PISO] familia %s cena %d: %d palavras "
                                  "(piso %d) — recalibre o piso ou a copy"
                                  % (fam["id"], i, n_, PISO_FALA[i]))
        c3 = fam["cenas"][2]
        # ⛔ CT6 — a keyword literal, na cena 3, em TODAS. A automacao de DM
        # casa palavra exata: keyword parafraseada nao dispara mensagem nenhuma.
        if CTA_LITERAL not in c3:
            falhas.append("[CT6] familia %s: a cena 3 nao traz %r"
                          % (fam["id"], CTA_LITERAL))
        # ⛔ BA7 — o follow nunca e' condicao nem pre-requisito.
        if re.search(r"\bfollow\b[^.]*\b(or|otherwise|unless|first|before)\b",
                     c3, re.I):
            falhas.append("[BA7] familia %s: o follow virou portao — a DM sai "
                          "igual, seguindo ou nao" % fam["id"])
        # ⛔ CT5 — nenhum ingrediente nomeado. E' a moeda: se o video conta a
        # receita, nao sobra motivo para comentar. A fonte cumpre isto em 7/7.
        for i, c in enumerate(fam["cenas"], 1):
            if sc.INGREDIENTES_16.search(c):
                falhas.append("[CT5] familia %s cena %d nomeia ingrediente: %r"
                              % (fam["id"], i, c))
        # ⛔ CT7 — verbo de ereccao colado no orgao na MESMA sentenca.
        for i, c in enumerate(fam["cenas"], 1):
            for sent in re.split(r"(?<=[.!?])\s+", c):
                if (any(re.search(r"\b%s\b" % t, sent, re.I)
                        for t in NUCLEO + APELIDOS_FONTE)
                        and sc.ERECAO_16.search(sent)):
                    falhas.append("[CT7] familia %s cena %d: orgao e verbo de "
                                  "ereccao na mesma sentenca: %r"
                                  % (fam["id"], i, sent.strip()))
        # ⛔ CT4 — UM apelido por video, e so' do vocabulario aprovado.
        usados = {t for t in NUCLEO + APELIDOS_FONTE
                  if re.search(r"\b%s\b" % t, " ".join(fam["cenas"]), re.I)}
        if len(usados) > 1:
            falhas.append("[CT4] familia %s mistura %s — em 5s o corte zera a "
                          "memoria e o ouvinte tem de remapear"
                          % (fam["id"], sorted(usados)))

    # ⭐ O EIXO DA HIPOTESE PRECISA TER OS DOIS LADOS POVOADOS. Se um dia
    # todas as familias virarem `mec=True`, a pre-selecao `sem mecanismo`
    # devolve pool vazio e o `or FAMILIAS` do sorteio cede em SILENCIO — o
    # painel prometeria um lote que nunca sai. Mesma classe do `praia` que
    # devolvia 0/120 no GOOD 16.
    for quer, quantas in (("com", len([x for x in FAMILIAS if x["mec"]])),
                          ("sem", len([x for x in FAMILIAS if not x["mec"]]))):
        if quantas < 1:
            falhas.append("[EIXO mec] nenhuma familia com mec=%r — a "
                          "pre-selecao do painel cederia em silencio" % quer)

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
         dict(b0, **{IMAGENS[1]: "a wet tiled wall"}), True),
        ("BA1 limpo", _ba1_medida, s0, b0, False),
        ("BA2 sem o rotulo", _ba2_rotulo, s0,
         dict(b0, **{IMAGENS[0]: "a shower with a jar"}), True),
        ("BA2 limpo", _ba2_rotulo, s0, b0, False),
        ("BA3 com homem e modo desligado", _ba3_sem_pessoa, s0,
         dict(b0, **{IMAGENS[0]: b0[IMAGENS[0]]
                     + " A man stands beside the tub."}),
         True),
        ("BA3 limpo", _ba3_sem_pessoa, s0, b0, False),
        ("BA5 com pecker na fala", _ba5_apelido,
         dict(s0, falas=[s0["falas"][0],
                         "The trick feeds blood back to your pecker.",
                         s0["falas"][2]]),
         b0, True),
        # ⭐ CONTROLE DO E3: `bat` e `pipe` sao o vocabulario NOVO deste motor.
        # Se alguem reaplicar aqui o D7 do `banho16` (*so' Johnson/manhood*),
        # este controle acusa — e' o unico jeito de a decisao do operador nao
        # ser "consertada" por engano seis meses depois.
        ("BA5 com `bat` (liberado por E3)", _ba5_apelido,
         dict(s0, falas=["I am 70 and my bat was small and soft.",
                         s0["falas"][1], s0["falas"][2]]), b0, False),
        ("BA5 misturando bat e pipe", _ba5_apelido,
         dict(s0, falas=["My bat was small.", "It clears your pipe.",
                         s0["falas"][2]]), b0, True),
        ("BA5 limpo", _ba5_apelido, s0, b0, False),
        ("BA6 orgao + ereccao na mesma sentenca", _ba6_leve,
         dict(s0, falas=[s0["falas"][0],
                         "It makes your Johnson hard again.",
                         s0["falas"][2]]), b0, True),
        ("BA6 limpo", _ba6_leve, s0, b0, False),
        ("BA7 follow como condicao", _ba7_follow,
         dict(s0, falas=[s0["falas"][0], s0["falas"][1],
                         "Comment Recipe and follow me or it will not send."]),
         b0, True),
        # ⭐⭐ CONTROLE DO DEFEITO HISTORICO REAL: o `Segue primeiro` que o
        # operador escreveu na familia 6.2 em 14/08. Nao e' um defeito
        # inventado para a lente ter o que pegar — e' o que chegou aqui.
        ("BA7 follow como pre-requisito (`follow first`)", _ba7_follow,
         dict(s0, falas=[s0["falas"][0], s0["falas"][1],
                         "Comment Recipe to get the step by step. Follow me "
                         "first."]), b0, True),
        ("BA7 limpo", _ba7_follow, s0, b0, False),
        # ⭐⭐ CONTROLES DA BA9 — o defeito plantado e' o que ela existe para
        # impedir: copy aprovada chegando alterada, e beat de outra familia.
        ("BA9 com a fala reescrita no caminho", _ba9_familia, s0,
         dict(b0, **{TAKES[0]: b0[TAKES[0]].replace(
             'Dialogue: "%s"' % sonorizar(s0["falas"][0]),
             'Dialogue: "I am old and this is my little shower trick."')}),
         True),
        ("BA9 com beat de outra familia", _ba9_familia,
         dict(s0, falas=[FAMILIAS[0]["cenas"][0], s0["falas"][1],
                         s0["falas"][2]]), b0, True),
        ("BA9 limpo", _ba9_familia, s0, b0, False),
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
    sem = montar(sortear("joe", random.Random(3), {}, {}))[IMAGENS[0]]
    com = montar(sortear("joe", random.Random(3), {}, {"pessoa": True}))[IMAGENS[0]]
    if sem == com:
        falhas.append("MODO PESSOA: ligado e desligado produzem a MESMA IMAGE")

    # ⚠️ O piso e' o TAMANHO DO POOL, lido do proprio pool — numero cravado a
    # mao vira falso alarme no dia em que uma entrada sai (foi o que aconteceu
    # quando o `box_pedra` foi removido: 8 virou 7 e o autoteste reprovou o
    # certo).
    for e, minimo in (("banheiro", len(BANHEIROS)),
                      ("superficie", len(SUPERFICIES)), ("medida", len(MEDIDAS)),
                      ("rotulo", len(ROTULOS)), ("receita", len(RECEITAS)),
                      ("familia", len(FAMILIAS)), ("mecanismo", 2),
                      ("habitado", len(HABITADOS)), ("maos", len(MAOS)),
                      ("derivas", 0)):
        if minimo and len(eixos[e]) < minimo:
            falhas.append("EIXO %s: so' %d valores em %d sorteios (pool tem %d)"
                          % (e, len(eixos[e]), n, minimo))

    # ⛔ AS TRES DERIVAS DE CAMERA SAO DISTINTAS NO MESMO VIDEO. `rng.sample`
    # garante isso hoje; a lente existe para o dia em que alguem trocar por
    # tres `rng.choice` e a camera repetir movimento em cortes seguidos — que
    # e' justamente o que denuncia geracao.
    for i in range(60):
        d = sortear(pags[i % len(pags)], random.Random(1000 + i), {}, {})["derivas"]
        if len(set(d)) != 3:
            falhas.append("DERIVAS: o video %d repete movimento de camera "
                          "entre takes" % i)
            break

    # ⭐⭐ O PAINEL SIMULADO — cada eixo trocado como a UI troca, e o linter
    # cobrado depois. ⚠️ Este bloco nasce de um defeito FILMADO: o operador
    # clicava em `trocar` na linha A COPY e a BA9 acusava a cada clique, porque
    # o eixo trocava o rotulo da familia sem refazer as tres falas. O autoteste
    # media 400 sorteios e passava — ele nunca tocava no painel.
    # ⛔ Sortear e' so' METADE do que o operador faz. O que ele faz depois —
    # trocar eixo, trocar cena, travar — nao era medido por lente nenhuma.
    for chave in [e[0] for e in EIXOS_UI]:
        pool_nome = dict((e[0], e[2]) for e in EIXOS_UI)[chave]
        for k in range(12):
            sp = sortear(pags[k % len(pags)], random.Random(500 + k), {}, {})
            opcoes = [x for x in globals()[pool_nome] if x != sp[chave]]
            if not opcoes:
                continue
            sp[chave] = random.Random(k).choice(opcoes)
            # ⭐ exatamente o que o `ui_agente.trocar_eixo` faz em seguida
            reescreve = EIXOS_QUE_MEXEM_NA_COPY.get(chave)
            if reescreve:
                reescreve(sp, random.Random(k))
            ruins = [m for n, m in lint(sp, montar(sp)) if n == "ERRO"]
            if ruins:
                falhas.append("[PAINEL] trocar o eixo %r deixa o video invalido: "
                              "%s" % (chave, ruins[0][:80]))
                break

    # ⭐ E o botao `trocar` de CENA, que a UI chama por `nova_fala`.
    if not callable(globals().get("nova_fala")):
        falhas.append("[PAINEL] sem `nova_fala`: o botao `trocar` de cena fica "
                      "MORTO e a tela diz que o agente nao tem banco de copy")
    else:
        for k in range(12):
            sp = sortear(pags[k % len(pags)], random.Random(700 + k), {}, {})
            antes = list(sp["falas"])
            r = random.Random(k)
            cand = nova_fala(sp, k % 3, r)
            sp["falas"][k % 3] = cand
            ruins = [m for n, m in lint(sp, montar(sp)) if n == "ERRO"]
            if ruins:
                falhas.append("[PAINEL] `nova_fala` na cena %d deixa o video "
                              "invalido: %s" % (k % 3 + 1, ruins[0][:80]))
                break
            if sp["falas"] == antes:
                falhas.append("[PAINEL] `nova_fala` devolveu a MESMA copy — "
                              "botao que nao muda nada e' botao quebrado")
                break

    # ⛔ O MOLDE DO POOL DE MAOS (`<adj> hands with <detalhe>`) — o
    # `_maos_partes` degrada em silencio se alguem acrescentar uma entrada
    # fora do molde, e o degradado ("steady" para todo mundo) apagaria o unico
    # eixo de variacao da mao. Silencio e' o que a lente existe para quebrar.
    fora = [x for x in MAOS if " hands with " not in x["desc"]]
    if fora:
        falhas.append("MAOS: %d entrada(s) fora do molde `<adj> hands with "
                      "<detalhe>`: %r" % (len(fora), fora[0]))
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
    # ⛔ `--abertura` MORREU com os pools de beat: as doze familias sao
    # aprovadas inteiras e a abertura vem dentro delas. O que o substitui e'
    # `--familia` (uma das doze) e `--mecanismo` (o eixo da hipotese).
    ap.add_argument("--familia", choices=[f["id"] for f in FAMILIAS])
    ap.add_argument("--mecanismo", choices=["com", "sem"],
                    help="`sem` = as familias que NAO explicam o mecanismo — "
                         "a forma do reel de melhor comentario da fonte")
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
    if a.familia:
        travas["familia"] = a.familia
    if a.mecanismo:
        travas["mecanismo"] = a.mecanismo
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
