#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""AGENTE AMISH 16S — a vovo Amish, o antes/depois com DAY em quadro, e o CTA YES.

⭐⭐ FONTE: pagina "Martha.Knows" (Old Nanny Pure Wisdom, 39k seguidores),
78 reels enumerados em 2026-08-21 e os **18 com 50k+ views lidos quadro a
quadro** (legenda karaoke queimada = a copy, palavra por palavra). Nicho:
EMAGRECIMENTO — nao ED. E' o primeiro motor do parque fora do nicho.

O FORMATO, ordem do operador (2026-08-21):
  take 1 — 3s — DAY 1  (o sujeito obeso recebe a colherada)
  take 2 — 3s — DAY 47-57 sorteado (o MESMO sujeito, magro, mesma roupa larga)
  take 3 — 8s — a apresentacao selfie + CTA
⚠️ Os takes saem do gerador com ~8s; os takes 1-2 sao CORTADOS a 3s na edicao.
Por isso a acao deles mora nos TRES PRIMEIROS segundos ("within the first
second...") — o que acontece depois do corte e' custo, nao cena.

⛔⛔ O TETO DE FALA E' CALCULADO, nao chutado. A regra do operador: 14 palavras
em 6s (2,33 p/s) e 24 em 8s (3,0 p/s). Para 3s, pela taxa mais dura:
14/6 x 3 = **7 palavras** (o palpite dele era 6; a conta da' 7). ⭐ Mas os
takes 1-2 nascem **MUDOS por fidelidade**: nos 18 reels lidos, ninguem fala
sobre o antes/depois — a fala inteira mora no selfie. O teto de 7 fica
registrado para o dia em que alguem quiser fala ali.
⚠️ TAKE 3: teto nominal 24 (24/8s). A COPY 1 tem **34 palavras** — verbatim da
fonte (8 dos 18 videos, campea com 331k views) e a ordem foi *"o resto deve
permanecer igual"*. A 3,1 p/s medidos da voz gerada, 34 palavras pedem ~11s:
risco DECLARADO de a cauda cortar. O que corta e' o pedido de share/follow —
o `comment YES` vem no meio e sobrevive. Encurtar e' alcada do operador.

⛔⛔ O DAY E' ESCRITO PELO VEO, NAO NA EDICAO — ordem literal: *"e' o proprio
veo que deve escrever essa legenda no mesmo padrao dos videos originais"*.
Consequencia unica no parque: a trava `SEM_TEXTO_TAKE` do contrato
compartilhado **NAO entra nos takes 1-2** (ela mataria a unica coisa que o
take existe para mostrar) e entra normalmente no take 3, onde texto nenhum e'
bem-vindo. A lente AM4 cobra os dois lados dessa excecao.

⛔ KEYWORD NATIVA = "YES", e isso CONFLITA de proposito com a lista
`BANIDAS_KEYWORD` do short_comum ("yes" quebra a automacao de DM do funil ED).
Este motor e' de OUTRO funil: a pagina nova nasce com a automacao cadastrada
em YES, como a fonte (18 de 18 pedem YES/DRINK/BOOK — e o operador travou:
*"O cta sempre deve ser comentar YES"*). A banida vale para TROCAR no painel;
a nativa deste motor e' decisao dele, registrada aqui.

⛔⛔ SEM BLOCO 0 (REF), desde 2026-08-21 — ordem: *"a referencia deve ser
baseada direto na imagem 1 [...] gere a imagem 2 e 3 a partir da imagem 1 que
irei anexar como base. Dessa forma eu economizo tempo."* A IMAGE 01 e' a unica
descricao completa; as IMAGEs 02/03 sao instrucoes de EDICAO sobre ela, e a
lente AM8 cobra as ancoras (`Using the provided image`, `Change ONLY`...).

⭐ AS 4 COPIES SAO AS VALIDADAS NA FONTE, renumeradas por uso e views:
  1 — resultados (8/18 usos · 331k+184k+110k+109k+88k+61k+56k+54k)
  2 — colher + receita (2/18 · 88k+76k)
  3 — Johnny secreto (1/18 · 70k)
  4 — colher + comprar (1/18 · 67k)
⛔ A unica variacao permitida: nome do personagem e ele/ela conforme o sexo
do sujeito. O resto e' constante e a lente AM2 cobra verbatim.

    python funil-organico/amish16_short.py --pagina clara --n 3
    python funil-organico/amish16_short.py --autoteste
    python funil-organico/amish16_short.py --stats
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

TITULO = "AGENTE AMISH 16S"
SLUG = "amish-16s"
SUBTITULO = ("4 takes (4s + 4s + 8s + 6s) · o antes/depois · a vovo Amish e "
             "mais oito narradores · CTA YES · a legenda DAY sai no editor")

LEDGER = os.path.join(AQUI, ".amish-16s-ledger.json")

CENAS_UI = ["1 · DAY 1 (mudo)", "2 · o depois (mudo)",
            "3 · CTA parte 1", "4 · CTA parte 2"]

# ⛔⛔ QUATRO TAKES, TRES IMAGENS — o TAKE 04 anima a MESMA IMAGE 03 (a
# selfie). Ordem do operador (2026-08-21, gravacao de 21 min): *"caso nao
# seja possivel falar tudo dentro de 8 segundos, ai' voce ira' ajustar o
# agente para que gere 4 takes ao inves de 3"*.
# ⭐ E ele nao foi possivel — MEDIDO por ele em campo, nao estimado: das 4
# geracoes do TAKE 3 com a COPY 1 (34 palavras), TRES cortaram na MESMA
# palavra (`video`, a 28a) e so' uma falou inteira. 28 palavras em 8s.
IMAGENS = ("IMAGE 01/03", "IMAGE 02/03", "IMAGE 03/03")
TAKES = ("TAKE 01/04", "TAKE 02/04", "TAKE 03/04", "TAKE 04/04")

# ⛔ O RELOGIO, medido por ele no proprio Veo: *"o Veo so' da' o limite
# minimo aqui, o mais curto e' quatro"* — os takes 1-2 nascem com 4s e sao
# cortados a ~3s na edicao. E *"todos os videos precisam ter no maximo 20
# segundos"*: 3 + 3 + 8 + 6 = 20 no arquivo final.
SEGUNDOS_TAKE = {1: 4, 2: 4, 3: 8, 4: 6}
TAXA = 3.0                        # palavras/s — a regra dele (24 em 8s)
# ⛔ takes 1-2 sao MUDOS (a musica entra no editor), entao teto 0.
TETO_FALA = {1: 0, 2: 0,
             3: int(SEGUNDOS_TAKE[3] * TAXA),      # 24
             4: int(SEGUNDOS_TAKE[4] * TAXA)}      # 18

# ⛔ As paginas aqui sao o CONTRATO DE UI (botao de pele), nao paginas reais
# do Facebook: o motor nasce antes da pagina. `clara`/`escura` definem o
# DEFAULT de pele de narrador e sujeito; as travas do painel vencem.
ETNIA = {"clara": "white American", "escura": "Black American"}
PELES = {"branca": "white American", "negra": "Black American"}

# ⛔⛔ O CTA E' SEMPRE YES — ordem do operador (2026-08-21): *"o cta desse
# agente deve ser sempre a palavra yes"*. O campo de keyword da UI NAO
# aparece (KEYWORD_UI=False) e nao ha' substituicao em lugar nenhum: a
# palavra vive escrita dentro das quatro copies verbatim e a AM2 cobra o
# literal `comment YES`.
# ⚠️ A automacao de DM da pagina nova tem de nascer cadastrada em YES.
KEYWORD_UI = False
KEYWORD_NATIVA = "YES"

# ⭐ [LOCAL LUCAS] o seletor pele/pagina do topo NAO aparece neste motor —
# as paginas aqui sao sinteticas (contrato de UI) e a pele ja' tem DUAS
# travas proprias no painel (narrador e sujeito). Dois controles para a
# mesma trava e' a copia espelhada que diverge na semana seguinte.
SEM_SELETOR_PAGINA = True

DIA_MIN, DIA_MAX = 47, 57
# ⛔⛔ 380-420 kg DESDE 21/08 — e' a faixa do prompt que ele carimbou como
# *"absurdamente perfeito"*, que sai em **880 lb** (≈ 399 kg). Isso SUPERA a
# ordem de mais cedo no mesmo dia (*"aumente esse numero de peso para 240-280
# kg"*), e a superacao e' o proprio teste de campo dele: registrar o prompt
# aprovado mantendo a faixa antiga entregaria 570 lb, ou seja, outra coisa.
# ⚠️ A faixa e' larga de proposito — 838 a 926 lb — para o eixo continuar
# sorteando; 880 e' o centro, nao um valor fixo.
PESO_MIN, PESO_MAX = 380, 420      # kg — no prompt vai em lb

# ⛔ Contrato do `lint_copy16`/`medir_copy16`: NUCLEO e' o pool de apelidos do
# orgao. Este motor e' de EMAGRECIMENTO — nao ha' orgao, nao ha' apelido.
# Lista vazia e' declaracao, nao esquecimento.
NUCLEO = []


# ===========================================================================
# NARRADORES — os nove que o operador ditou, um a um
# ===========================================================================
# ⛔ Cada rosto tem ARQUITETURA (formato, nariz, marca) — rosto generico
# deriva para a media do treino, e a media tem nome. Doutrina de 2026-08-10;
# zero negacao de celebridade em lugar nenhum.
# ⚠️ `pele_fixa`: indigenas e curandeiros africanos tem identidade que a trava
# de pele NAO pode trocar. A trava e' IGNORADA COM AVISO — botao que cede em
# silencio e' o defeito que o GO21 ja' pagou; aqui ele avisa.
NARRADORES = [
    {"id": "vovo_amish", "rotulo": "vovo Amish (a ancora)", "sexo": "f",
     "pele_fixa": None,
     "voz": "a warm, cracked elderly woman's voice",
     "desc": ("an elderly Amish %(pele)s woman in her late seventies, a long "
              "deeply lined face with high cheekbones, a narrow straight nose "
              "and pale gray eyes, small pearl-drop earrings, wearing a plain "
              "%(cor)s dress with a white lace-trimmed bonnet and a white bow "
              "tied at her collar")},
    {"id": "moca_verao", "rotulo": "moca americana de 25", "sexo": "f",
     "pele_fixa": None,
     "voz": "a bright, friendly young woman's voice",
     "desc": ("a 25-year-old %(pele)s American woman, strikingly beautiful, "
              "an oval face with high cheekbones, large bright eyes and a "
              "small straight nose, long shiny hair loose over her shoulders, "
              "tall with a fit healthy figure, wearing modest denim shorts "
              "and a loose short-sleeve summer blouse")},
    {"id": "vovo_amish_h", "rotulo": "vovo Amish homem (75)", "sexo": "m",
     "pele_fixa": None,
     "voz": "a deep, unhurried elderly man's voice",
     "desc": ("a 75-year-old Amish %(pele)s man with a long white beard and "
              "no mustache, a square weathered face with deep-set eyes under "
              "heavy white brows, wearing a straw hat, a plain collarless "
              "white shirt and dark suspenders")},
    {"id": "doutora", "rotulo": "doutora de 40", "sexo": "f",
     "pele_fixa": None,
     "voz": "a clear, confident woman's voice",
     "desc": ("a 40-year-old %(pele)s woman physician, her hair tied back, a "
              "calm oval face with fine smile lines and a small mole on her "
              "left cheek, wearing a white doctor's coat over teal scrubs "
              "with a stethoscope around her neck")},
    {"id": "doutor", "rotulo": "doutor de 40", "sexo": "m",
     "pele_fixa": None,
     "voz": "a calm, reassuring man's voice",
     "desc": ("a 40-year-old %(pele)s man physician with short neat hair "
              "graying at the temples, a squared jaw, rimless glasses, "
              "wearing a white doctor's coat over a shirt and tie with a "
              "stethoscope around his neck")},
    {"id": "india_anciana", "rotulo": "india anciana de 80", "sexo": "f",
     "pele_fixa": "Native American",
     "voz": "a low, steady elderly woman's voice",
     "desc": ("an 80-year-old Native American elder woman with long silver "
              "braids, a broad deeply lined face with high flat cheekbones "
              "and dark hooded eyes, wearing traditional beaded regalia with "
              "a woven shawl over her shoulders")},
    {"id": "indio_anciao", "rotulo": "indio anciao de 80", "sexo": "m",
     "pele_fixa": "Native American",
     "voz": "a deep, gravelly elderly man's voice",
     "desc": ("an 80-year-old Native American elder man with long silver "
              "hair, a broad lined face with a strong straight nose and "
              "hooded eyes, wearing traditional regalia with beadwork and a "
              "bone-bead breastplate")},
    {"id": "curandeira_africana", "rotulo": "curandeira africana de 80",
     "sexo": "f", "pele_fixa": "Black African",
     "voz": "a warm, resonant elderly woman's voice",
     "desc": ("an 80-year-old African healer woman, a round deeply lined "
              "face with wide-set eyes, her white hair wrapped in a printed "
              "headwrap, wearing traditional printed robes with layered "
              "beaded necklaces")},
    {"id": "curandeiro_africano", "rotulo": "curandeiro africano de 80",
     "sexo": "m", "pele_fixa": "Black African",
     "voz": "a deep, warm elderly man's voice",
     "desc": ("an 80-year-old African healer man with a short white beard, a "
              "lean deeply lined face with a broad nose, wearing traditional "
              "healer robes with cowrie-shell necklaces")},
]

# ⭐ A ANCORA VARIA SO' NA COR DO VESTIDO — ordem: *"mude somente as cores da
# roupa dela"*. O roxo e' o original; o vinho apareceu na propria fonte.
CORES_VESTIDO = ["deep purple", "dark burgundy red", "navy blue",
                 "forest green", "chocolate brown", "slate blue"]


# ===========================================================================
# SUJEITOS — quem passa pelo antes/depois (looks lidos dos 18 reels)
# ===========================================================================
# ⛔ O look NAO diz pele nem sexo: pele vem da trava/pagina, sexo da trava.
# Cada entrada e' cabelo+roupa+idade — o que sobrevive ao emagrecimento e
# ancora a continuidade entre os dois quadros gerados separadamente.
SUJEITOS_H = [
    {"id": "grisalho_macacao", "rotulo": "grisalho de macacao", "idade": 62,
     "rosto": "a broad square face with a heavy jaw, deep-set blue eyes under bushy brows, a wide flat nose and a ruddy complexion",
     "visual": "shoulder-length gray hair and a thick gray mustache",
     "roupa": "a thin red plaid short-sleeve shirt"},
    {"id": "cabeludo_oculos", "rotulo": "cabeludo de oculos laranja",
     "idade": 55,
     "rosto": "a long oval face with a high forehead, close-set brown eyes, a narrow hooked nose and a pale complexion",
     "visual": "long dark curly hair, a dark mustache and orange-tinted "
               "glasses",
     "roupa": "a thin white short-sleeve shirt"},
    {"id": "calvo_oculos", "rotulo": "calvo de oculos", "idade": 60,
     "rosto": "a round face with full cheeks, small hazel eyes, a short blunt nose and a cleft chin",
     "visual": "a balding head with neat side hair and rectangular glasses",
     "roupa": "a thin plain white short-sleeve button shirt"},
    {"id": "careca", "rotulo": "careca", "idade": 52,
     "rosto": "a wide moon face with a low brow, small dark eyes, a bulbous nose and a florid complexion",
     "visual": "a completely bald head and a clean-shaven round face",
     "roupa": "a thin white short-sleeve shirt with a gray stripe"},
    {"id": "ruivo_estampada", "rotulo": "ruivo de camisa estampada",
     "idade": 50,
     "rosto": "a square freckled face with a strong chin, pale green eyes, a broad straight nose and reddened cheeks",
     "visual": "curly red hair and a bushy red mustache",
     "roupa": "a thin loud pink-and-blue patterned short-sleeve shirt"},
    {"id": "franjinha", "rotulo": "franjinha de polo", "idade": 58,
     "rosto": "a narrow face with a pointed chin, gray-blue eyes, a thin straight nose and a sallow complexion",
     "visual": "thin combed-back brown hair and small round glasses",
     "roupa": "a thin plain white polo shirt"},
    {"id": "coroa_social", "rotulo": "coroa de camisa social", "idade": 65,
     "rosto": "a heavy rectangular face with jowls, brown eyes under drooping lids, a wide nose and a weathered complexion",
     "visual": "short gray hair and bushy gray eyebrows",
     "roupa": "a thin light blue short-sleeve button shirt"},
    {"id": "barbudo", "rotulo": "barbudo de flanela", "idade": 48,
     "rosto": "a broad face with high cheekbones, dark brown eyes, a straight nose and sun-reddened skin",
     "visual": "a full brown beard and shaggy brown hair",
     "roupa": "a thin green-and-black checked short-sleeve shirt"},
]
SUJEITOS_M = [
    {"id": "ruiva_regata", "rotulo": "ruiva de regata azul", "idade": 38,
     "rosto": "a round freckled face with soft cheeks, green eyes, a small upturned nose and fair skin",
     "visual": "long curly red hair",
     "roupa": "a light blue tank top and jeans"},
    {"id": "ruiva_amarelo", "rotulo": "ruiva de top amarelo", "idade": 35,
     "rosto": "an oval face with a rounded chin, hazel eyes, a straight narrow nose and freckled fair skin",
     "visual": "long curly red hair",
     "roupa": "a yellow tank top and jeans"},
    {"id": "loira_rabo", "rotulo": "loira de rabo baixo", "idade": 42,
     "rosto": "a square face with a firm jaw, pale blue eyes, a small straight nose and light skin",
     "visual": "blond hair in a low ponytail",
     "roupa": "a white blouse and dark pants"},
    {"id": "morena_solta", "rotulo": "morena de cabelo solto", "idade": 40,
     "rosto": "a long face with a narrow chin, dark brown eyes, a slim straight nose and olive skin",
     "visual": "long straight dark hair",
     "roupa": "a lavender t-shirt and jeans"},
    {"id": "cacheada_curta", "rotulo": "cacheada curta", "idade": 45,
     "rosto": "a round face with full cheeks, dark eyes, a short broad nose and warm skin",
     "visual": "short tight curls",
     "roupa": "a thin chambray short-sleeve shirt"},
    {"id": "grisalha_floral", "rotulo": "grisalha de blusa floral",
     "idade": 58,
     "rosto": "a heart-shaped face with a pointed chin, gray-green eyes, a fine straight nose and pale skin",
     "visual": "shoulder-length gray-streaked hair",
     "roupa": "a floral print blouse"},
    {"id": "ruiva_gola", "rotulo": "ruiva de gola alta", "idade": 36,
     "rosto": "an oval face with high cheekbones, amber eyes, a small nose and freckled skin",
     "visual": "curly auburn hair",
     "roupa": "a high-collar white button blouse and dark pants"},
    {"id": "coque_verde", "rotulo": "coque de blusa verde", "idade": 44,
     "rosto": "a broad face with a soft jaw, brown eyes, a rounded nose and light olive skin",
     "visual": "dark hair in a loose bun",
     "roupa": "a green summer top and jeans"},
]


def sujeitos_do_sexo(spec):
    """Pool de QUEM MUDA conforme o sexo travado/sorteado — contrato da UI."""
    return SUJEITOS_H if spec.get("sexo_sujeito") == "homem" else SUJEITOS_M


sujeitos_do_sexo.recebe_spec = True

# ⚠️ Pool combinado so' para inventario (--stats e paineis que listam tudo).
SUJEITOS = SUJEITOS_H + SUJEITOS_M


# ===========================================================================
# CENARIOS — 12 rotacoes do mundo-fonte (fazenda Amish, bandeira, cavalos)
# ===========================================================================
# ⛔ Ordem: *"os cenarios devem sempre mudar, mas ser parecidos com o original
# que funcionou, sempre rotacionando e inovando"*. Todos sao o MESMO mundo —
# fazenda Amish de verao — trocando o fundo. A bandeira americana e' quase
# constante na fonte e fica em 10 dos 12.
#
# ⛔⛔ NADA ATRAVESSA O QUADRO — 2026-08-21, gravacao de tela do operador.
# ===========================================================================
# Ele filmou os quatro takes de um mesmo video e mostrou a carroca de feno
# passando atras do casal no take 1 — e passando DE NOVO no take 2, que
# acontece 47 dias depois, e outra vez nos takes 3 e 4, sendo o take 4 a
# continuacao direta do 3, com a MESMA imagem de base:
#   *"a carroca fica dando looping. Isso esta' errado, isso e' confuso. A
#   carroca ja' deveria ter passado."*
# ⛔ A causa nao e' o cenario: e' o campo `vida`, que entra nos QUATRO takes
# e e' literalmente a ordem de mover a coisa. Um `vida` de travessia vira
# quatro travessias, uma por take, e o espectador le' loop.
# ⭐ A regra que ele ditou: *"deve ser objetos estaticos que nao mudam. No
# maximo, pequenos animais ali no chao, como galinhas pastando [...] ou entao
# pessoas se mexendo, mas num cenario muito ao fundo mesmo, la' onde estao
# essas arvores, que mal da' para ver, como agricultores trabalhando"*.
# ⛔ Logo: `vida` so' pode ser movimento NO LUGAR (balancar, fumegar,
# ciscar, girar no eixo) ou figura minuscula na linha das arvores. Verbo de
# travessia — `past`, `along the lane`, `rolls`, `plods`, `hauling`,
# `pulled by` — esta' banido, e quem cobra e' a lente `AM11`.
# ⚠️ Quatro entradas foram reescritas por isso: `carroca_feno` (virou os
# fardos), `construcao_celeiro` (a obra parada), `colheita_milho` (saiu a
# carroca de mula) e `pomar_florido` (saiu o cavaleiro).
CENARIOS = [
    {"id": "celeiro_bandeira", "rotulo": "celeiro vermelho + bandeira",
     "desc": ("in front of a weathered red barn with a large American flag "
              "hung on its wall, a black Amish buggy parked with its shafts "
              "resting on the ground and two draft horses standing still at "
              "a hitching rail"),
     "vida": "the horses shift their weight and swish their tails",
     "curto": "the red barn with the American flag"},
    {"id": "fardos_feno", "rotulo": "fardos de feno empilhados",
     "desc": ("beside a tall stack of square hay bales in a freshly mown "
              "field, a red barn and an American flag on a pole in the "
              "distance"),
     "vida": "loose straw stirs on top of the bales in the breeze",
     "curto": "the stack of hay bales"},
    {"id": "celeiro_novo", "rotulo": "celeiro novo, obra parada",
     "desc": ("in a quiet farmyard beside the bare wooden frame of a "
              "half-built barn, stacks of fresh lumber and two sawhorses "
              "resting on the ground, an American flag on a post"),
     "vida": "sawdust drifts in the sunlight above the lumber stacks",
     "curto": "the half-built barn frame"},
    {"id": "varal_caldeiroes", "rotulo": "varal + caldeiroes fumegando",
     "desc": ("in a muddy work yard with laundry lines and big black "
              "cauldrons steaming over open fires, a gray barn and an "
              "American flag behind"),
     "vida": "steam keeps rising off the cauldrons",
     "curto": "the steaming cauldrons"},
    {"id": "curral", "rotulo": "curral de vacas e ovelhas",
     "desc": ("by a wooden fence with dairy cows and sheep crowding the "
              "barnyard behind, chickens pecking near the fence posts, a "
              "small American flag on the barn"),
     "vida": "the chickens peck at the ground near the fence posts",
     "curto": "the crowded barnyard"},
    {"id": "milharal", "rotulo": "milharal na colheita",
     "desc": ("at the edge of a tall cornfield at harvest time, wooden "
              "crates of picked corn stacked on the ground beside them, an "
              "American flag on a pole"),
     "vida": "the tall corn sways in the breeze",
     "curto": "the edge of the cornfield"},
    {"id": "pomar_florido", "rotulo": "pomar florido",
     "desc": ("in a blooming spring orchard with pink flowering trees, a "
              "white farmhouse and a red barn far in the distance"),
     "vida": "loose petals drift down through the still air",
     "curto": "the blooming orchard"},
    {"id": "celeiro_cinza", "rotulo": "celeiro cinza + foice",
     "desc": ("against a weathered gray barn wall with an American flag "
              "nailed to it and a long-handled scythe leaning beside, open "
              "green pasture behind"),
     "vida": "tall grass sways in the open pasture",
     "curto": "the gray barn wall with the flag"},
    {"id": "pasto_moinho", "rotulo": "pasto + moinho de vento",
     "desc": ("in an open summer pasture with grazing cows and a tall metal "
              "windmill turning slowly in the distance, a dirt lane and a "
              "fence line running through the field"),
     "vida": "the windmill blades turn slowly in the distance",
     "curto": "the pasture with the windmill"},
    {"id": "despensa_ervas", "rotulo": "despensa de ervas",
     "desc": ("inside a rustic herb pantry, wooden shelves packed with "
              "glass jars of dried herbs and roots behind, warm window "
              "light from the side"),
     "vida": "dust motes drift in the warm window light",
     "curto": "the herb pantry shelves"},
    {"id": "lago_gansos", "rotulo": "lago com gansos",
     "desc": ("by a farm pond with white geese on the bank, a covered "
              "wooden bridge and a red barn beyond, an American flag on the "
              "bridge post"),
     "vida": "the geese preen and dip their beaks at the water's edge",
     "curto": "the farm pond"},
    {"id": "horta_abobora", "rotulo": "horta + carroca de abobora",
     "desc": ("beside a fenced vegetable garden with a wooden cart of "
              "pumpkins parked at the fence, a farmhouse porch with an "
              "American flag, and the tiny far-off figure of an Amish woman "
              "hoeing a row up at the tree line"),
     # ⭐ a unica pessoa que ainda se mexe no fundo do parque, e minuscula:
     # e' a excecao que ele autorizou — *"pessoas se mexendo, mas [...] la'
     # onde estao essas arvores, que mal da' para ver"*.
     "vida": "the tiny distant figure keeps hoeing at the tree line",
     "curto": "the pumpkin cart by the garden"},
]


# ===========================================================================
# O DAY — escrito pelo Veo, no estilo da fonte
# ===========================================================================
# ⭐ Um estilo por video, IGUAL nos dois takes (comportamento da fonte: o
# estilo nunca muda dentro do mesmo reel — mudar leria como outro video).
ESTILOS_DAY = [
    {"id": "vermelho", "rotulo": "vermelho com contorno branco",
     "desc": "thick bold red block letters with a white outline"},
    {"id": "amarelo", "rotulo": "amarelo com contorno preto",
     "desc": "bold bright yellow block letters with a thin black outline"},
    {"id": "branco", "rotulo": "branco com contorno preto",
     "desc": "bold white block letters with a heavy black outline"},
    {"id": "chip_rosa", "rotulo": "branco em etiqueta rosa",
     "desc": "bold white block letters on a small hot-pink rectangular tag"},
    {"id": "roxo", "rotulo": "branco com brilho roxo",
     "desc": "bold white block letters with a purple outline glow"},
]

# ⛔⛔ O DAY SAIU DO PROMPT EM 2026-08-21 — ordem do operador depois de
# filmar quatro geracoes de cada take: *"remova completamente esse dia 1 e
# dia 50 e poucos do prompt [...] e coloque pro editor conseguir fazer essa
# legenda queimada [...] porque ele tem dificuldade em fixar essa legenda"*.
# ⭐ MEDIDO por ele: em 8 de 8 geracoes de take a legenda DESAPARECIA no
# meio, e em 2 lotes de imagem veio uma TARJA PRETA atras do texto. Nenhuma
# das duas coisas o prompt consegue impedir de forma confiavel.
# ⚠️ Agora TODO quadro nasce LIMPO e a legenda e' queimada pelo Veo Editor,
# fixa e identica do primeiro ao ultimo frame. O `dia2` continua sorteado no
# spec — ele vai para o resumo em PT, para o operador saber o que pedir ao
# editor —, mas nao entra em prompt nenhum.
# ⭐⭐ PROMPT NEGATIVO — pedido literal do operador (2026-08-21): *"coloque
# tambem no mesmo prompt um prompt negativo, o que a imagem NAO deve ter"*.
# ⛔ Nasce de defeito medido, nao de precaucao: ele gerou quatro imagens
# seguidas SEM bigode e SEM o cabelo pedido, com a base anexada.
# ⚠️ E' negacao de DEFEITO (careca, barbeado, texto), nunca de pessoa: dizer
# `not a celebrity` injeta o token, e a ordem de 10/08 baniu isso no parque
# inteiro. Negar `bald` nao tem esse efeito — `bald` nao e' identidade.
NEGATIVO_IMG = ("Do NOT include: a bald or shaved head; a clean-shaven face "
                "when facial hair is described; hair or facial hair of a "
                "different colour or length than described; a different face "
                "from the one described; glasses that were not described; "
                "any text, caption, number or watermark; a black bar or "
                "coloured box behind anything; extra hands, arms or fingers.")

NEGATIVO_MAGRO = ("Do NOT include: a different person; a different face; a "
                  "changed hairstyle or facial hair; any remaining belly, "
                  "double chin or thick thighs; oversized clothes hanging "
                  "loose on the body; any text, caption, number or "
                  "watermark; extra hands, arms or fingers.")

_SEM_TEXTO_IMG = ("There is no text, no caption, no lettering, no numbers "
                  "and no watermark anywhere in this image.")
_SEM_TEXTO_TK = ("No text, no caption, no lettering, no numbers and no "
                 "watermark appear at any moment.")


# ===========================================================================
# AS 4 COPIES — verbatim da fonte, renumeradas por uso e views
# ===========================================================================
# ⛔ ALCADA: copy e' do operador. As quatro chegaram prontas na ordem de
# 2026-08-21; a unica variacao permitida e' nome/pronome do sujeito.
# ⚠️ O literal YES e' substituido pela keyword do painel quando o operador
# trocar (substituicao verificada, molde `tirar_bandeira`) — nunca redigitado.
# ⛔⛔ CADA COPY VEM PARTIDA EM DUAS — a divisao e' o unico jeito de a fala
# caber no relogio, e o corte foi escolhido no PONTO NATURAL de respiro de
# cada uma (fim de sentenca), nunca no meio de uma oracao. A soma das duas
# partes e' a copy validada, palavra por palavra: nada foi reescrito.
# ⚠️ Parte 1 vai no TAKE 03 (8s, teto 24) e parte 2 no TAKE 04 (6s, teto 18).
COPIES = [
    {"id": "c1", "rotulo": "1 · resultados (a campea — 8/18, 331k)",
     "usos": 8, "views_max": 331000,
     "pt1": ("Se voce quer saber o que eu dei pra %(pt_obj)s conseguir esses "
             "resultados, comente YES e eu te mando."),
     "pt2": ("Mas me siga e compartilhe este video para que minha mensagem "
             "chegue ate voce."),
     "en1": ("If you wanna know what I gave %(obj)s to get those results, "
             "comment YES and I will send it to you."),
     "en2": ("But follow me and share this video so that my message "
             "reaches you.")},
    {"id": "c2", "rotulo": "2 · colher + receita (2/18, 88k)",
     "usos": 2, "views_max": 88000,
     "pt1": "Uma colher de sopa toda manha antes do cafe. So isso.",
     "pt2": "Comente YES que eu te mando a receita dessa bebida Amish.",
     "en1": "One tablespoon every morning before breakfast. That's it.",
     "en2": ("Comment YES and I will send you this Amish drink recipe.")},
    {"id": "c3", "rotulo": "3 · o segredo do Johnny (1/18, 70k)",
     "usos": 1, "views_max": 70000,
     "pt1": ("Quer saber a bebida secreta que eu acabei de dar pro "
             "%(pt_nome)s pra %(pt_obj)s emagrecer?"),
     "pt2": "E' so' comentar YES que eu te mando.",
     "en1": ("Wanna know the secret drink I just gave %(nome)s to help "
             "%(obj)s lose weight?"),
     "en2": "Just comment YES and I will send it to you."},
    {"id": "c4", "rotulo": "4 · colher + comprar (1/18, 67k)",
     "usos": 1, "views_max": 67000,
     "pt1": "Beba uma colher de sopa toda manha antes do cafe. So isso.",
     "pt2": ("Para comprar, comente YES que eu mando direto pra voce na sua "
             "caixa de entrada."),
     "en1": "Drink one tablespoon every morning before breakfast. That's it.",
     "en2": ("To buy it, comment YES and I will send it straight to your "
             "inbox.")},
]

# ⭐ Copy 3 nomeia o personagem — Johnny e' o da fonte; os outros sao nomes
# rurais US da mesma familia sonora. Nome segue o SEXO do sujeito.
NOMES = {"homem": ["Johnny", "Billy", "Tommy", "Eddie", "Walter", "Harold"],
         "mulher": ["Sally", "Betty", "Peggy", "Mary", "Dorothy", "Hazel"]}


# ===========================================================================
# geometria travada (as tres cenas da fonte, em constantes)
# ===========================================================================
ORIENTACAO = ("Vertical 9:16 portrait orientation, photorealistic smartphone "
              "footage in bright summer daylight, handheld realism.")

_GARRAFA = "a dark amber glass bottle"


def _palavras(t):
    return len(re.findall(r"[A-Za-z0-9'%()\-]+", t or ""))


def _por_id(pool, ident):
    for x in pool:
        if x["id"] == ident:
            return x
    return pool[0]


def _fresco(pool, usados, rng, chave="id"):
    """Sorteia evitando os ids recentes — pool grande sem memoria repete."""
    livres = [x for x in pool if x[chave] not in usados]
    return rng.choice(livres or pool)


# ===========================================================================
# LEDGER
# ===========================================================================
def _carregar_ledger():
    if not os.path.isfile(LEDGER):
        return {}
    try:
        with io.open(LEDGER, encoding="utf-8") as f:
            return json.load(f)
    except Exception:                                    # noqa: BLE001
        return {}


def _gravar_ledger(led, spec):
    for k, v in [("narrador", spec["narrador"]["id"]),
                 ("cenario", spec["cenario"]["id"]),
                 ("sujeito", spec["sujeito"]["id"]),
                 ("copy", spec["copy"]["id"]),
                 ("estilo", spec["estilo"]["id"]),
                 ("cor", spec["cor_vestido"]),
                 ("peso", spec["peso_kg"]),
                 ("dia2", spec["dia2"]),
                 ("sexo", spec["sexo_sujeito"])]:
        led.setdefault(k, []).append(v)
        led[k] = led[k][-40:]
    try:
        with io.open(LEDGER, "w", encoding="utf-8") as f:
            json.dump(led, f, ensure_ascii=False, indent=0)
    except Exception:                                    # noqa: BLE001
        pass


# ===========================================================================
# SORTEIO
# ===========================================================================
def _modulo():
    return sys.modules[__name__]


def _kw():
    """⛔ SEMPRE YES, por ordem (2026-08-21) — nao le' painel nem processo."""
    return "YES"


def _falas(spec):
    c = spec["copy"]
    obj = "him" if spec["sexo_sujeito"] == "homem" else "her"
    pt_obj = "ele" if spec["sexo_sujeito"] == "homem" else "ela"
    val = {"obj": obj, "nome": spec["nome"]}
    val_pt = {"pt_obj": pt_obj, "pt_nome": spec["nome"]}
    # ⛔ SEM substituicao de keyword: o YES e' cravado por ordem (2026-08-21)
    p1 = c["en1"] % val if "%" in c["en1"] else c["en1"]
    p2 = c["en2"] % val if "%" in c["en2"] else c["en2"]
    spec["fala_pt"] = ((c["pt1"] % val_pt if "%" in c["pt1"] else c["pt1"])
                       + " " + (c["pt2"] % val_pt if "%" in c["pt2"]
                                else c["pt2"]))
    # ⛔ takes 1-2 MUDOS por fidelidade a fonte e por ordem (a musica entra
    # no editor); a fala mora inteira nos takes 3 e 4.
    return ["", "", p1, p2]


def sortear(pagina, rng, led, travas=None):
    travas = travas or {}
    hist = led if isinstance(led, dict) else {}
    pele_pag = ETNIA.get(pagina, "white American")
    avisos = []

    nar = (_por_id(NARRADORES, travas["narrador"]) if travas.get("narrador")
           else _fresco(NARRADORES, hist.get("narrador", [])[-4:], rng))

    # pele do narrador: trava > identidade fixa > pagina
    pele_nar = PELES.get(travas.get("pele_narrador", ""), pele_pag)
    if nar["pele_fixa"]:
        if travas.get("pele_narrador"):
            avisos.append("a trava de pele do narrador foi IGNORADA: %r tem "
                          "identidade fixa (%s)"
                          % (nar["id"], nar["pele_fixa"]))
        pele_nar = nar["pele_fixa"]

    sexo = travas.get("sexo_sujeito") or rng.choice(["homem", "mulher"])
    pele_suj = PELES.get(travas.get("pele_sujeito", ""), pele_pag)

    pool_s = SUJEITOS_H if sexo == "homem" else SUJEITOS_M
    suj = (_por_id(pool_s, travas["sujeito"]) if travas.get("sujeito")
           else _fresco(pool_s, hist.get("sujeito", [])[-5:], rng))

    cen = (_por_id(CENARIOS, travas["cenario"]) if travas.get("cenario")
           else _fresco(CENARIOS, hist.get("cenario", [])[-5:], rng))
    estilo = (_por_id(ESTILOS_DAY, travas["estilo_day"])
              if travas.get("estilo_day")
              else _fresco(ESTILOS_DAY, hist.get("estilo", [])[-2:], rng))
    cor = travas.get("cor_vestido") or rng.choice(
        [c for c in CORES_VESTIDO
         if c not in hist.get("cor", [])[-2:]] or CORES_VESTIDO)

    quer = str(travas.get("copy") or "").strip()
    if quer and quer != "livre":
        copy = COPIES[max(0, min(3, int(quer) - 1))]
    else:
        copy = _fresco(COPIES, hist.get("copy", [])[-2:], rng)

    # ⭐⭐ O PESO DO SUJEITO — ordem do operador (2026-08-21, com dois lotes
    # de imagem na mao): *"a pessoa sentada nao estava com o peso que eu
    # desejo. Sempre deve gerar a pessoa com 200-240 kg em sorteio."*
    # ⛔ `obese` + `enormous belly` rendeu gente so' acima do peso — adjetivo
    # nao pesa. O prompt passa a dizer o NUMERO, e em LIBRAS, que e' a
    # unidade que a fonte queima na tela (`DAY 1 : 350 pounds`) e a que o
    # gerador associa a corpos americanos.
    pesos_livres = [k for k in range(PESO_MIN, PESO_MAX + 1)
                    if k not in hist.get("peso", [])[-6:]]
    peso_kg = rng.choice(pesos_livres or list(range(PESO_MIN, PESO_MAX + 1)))

    # ⛔ DAY 1 fixo; DAY do take 2 sorteado em 47-57 (ordem), com memoria
    dias_livres = [d for d in range(DIA_MIN, DIA_MAX + 1)
                   if d not in hist.get("dia2", [])[-4:]]
    dia2 = rng.choice(dias_livres or list(range(DIA_MIN, DIA_MAX + 1)))

    spec = {
        "pagina": pagina,
        "narrador": nar, "pele_narrador": pele_nar, "cor_vestido": cor,
        "sexo_sujeito": sexo, "pele_sujeito": pele_suj, "sujeito": suj,
        "cenario": cen, "estilo": estilo, "copy": copy,
        "nome": rng.choice(NOMES[sexo]),
        "peso_kg": peso_kg, "peso_lb": int(round(peso_kg * 2.20462 / 10) * 10),
        "dia2": dia2, "avisos": avisos,
    }
    spec["falas"] = _falas(spec)
    return spec


def _refazer_falas(spec, rng):
    spec["falas"] = _falas(spec)


EIXOS_QUE_MEXEM_NA_COPY = {"copy": _refazer_falas}


def nova_fala(spec, i, rng):
    """O botao `trocar` da cena 3 re-sorteia a COPY inteira (sao atomicas)."""
    atual = spec["copy"]["id"]
    spec["copy"] = _fresco([c for c in COPIES if c["id"] != atual], [], rng)
    spec["falas"] = _falas(spec)
    return spec["falas"][i]


# ===========================================================================
# MONTAGEM
# ===========================================================================
def _nar_desc(spec):
    d = spec["narrador"]["desc"] % {"pele": spec["pele_narrador"],
                                    "cor": spec["cor_vestido"]}
    return d


def _suj_desc(spec, magro=False):
    s = spec["sujeito"]
    sexo_en = "man" if spec["sexo_sujeito"] == "homem" else "woman"
    # ⚠️ SEM ARTIGO no "the same X": a roupa do pool ja' traz `a `/`an `.
    roupa = re.sub(r"^(a|an)\s+", "", s["roupa"])
    if magro:
        # ⛔⛔ NAO E' UM HOMEM NOVO — E' O MESMO, DEPOIS. Diagnostico do
        # operador em 21/08, e ele estava certo: *"nao e' pra pedir pra
        # transformar completamente o homem sentado SUBSTITUINDO por um homem
        # americano branco de 62 anos [...] porque aqui ele entende que e' pra
        # criar um novo homem. Se trata do MESMO homem"*. O verbo `replace` e
        # a redescricao da pessoa liberavam o gerador a inventar outro rosto —
        # foi o que ele filmou: base com bigode, saida sem bigode.
        # ⭐ Agora a frase e' de CONTINUIDADE, e o unico redescrito e' o CORPO.
        # ⛔⛔ A ROUPA E' A MESMA, EM OUTRO TAMANHO — correcao dele no mesmo
        # dia: *"e' importante manter a consistencia visual da roupa sim [...]
        # porem deve sair de uma roupa XXXG para uma roupa P de acordo com o
        # novo tamanho do corpo, e nao usar a roupa antiga extremamente larga
        # e desproporcional"*. E' o que a fonte faz: nos dois frames do reel
        # de 110k a camisa xadrez e o macacao sao os MESMOS, servindo.
        # ⚠️ A PERNA tem clausula propria porque foi o defeito que ele
        # apontou com o dedo: *"a perna dele nao mudou nada, o grosso dessa
        # perna pra essa daqui esta exatamente igual"*.
        lb = 154 if spec["sexo_sujeito"] == "homem" else 121
        ele = "he" if sexo_en == "man" else "she"
        dele = "his" if sexo_en == "man" else "her"
        return ("the very same %s from the base image, months later, after "
                "losing a huge amount of weight. %s now weighs exactly %d "
                "pounds and is lean and athletic: a completely flat stomach "
                "with no belly at all, a narrow waist, THIN LEGS — the "
                "thighs and calves are now slim, less than half the width "
                "they were in the base image — slim arms with no hanging "
                "flesh, slim hands with slender fingers, one sharp jawline "
                "with no double chin and lean hollow cheeks. %s face is "
                "IDENTICAL to the base image: the same features, the same "
                "%s, the same skin tone, the same age — only the body "
                "changed. %s wears the same %s as in the base image, but now "
                "in a small size that fits the slim body properly, neat and "
                "well-fitted, never the huge loose clothes from before"
                % (sexo_en, ele.capitalize(), lb, dele.capitalize(),
                   s["visual"], ele.capitalize(), roupa))

    # ⭐⭐ A FORMULA SUMO — calibrada em SETE rodadas de teste com o operador.
    # ⛔ A IDENTIDADE VEM ANTES DO CORPO desde 21/08: ele filmou quatro
    # geracoes seguidas SEM bigode e SEM o cabelo pedido, e diagnosticou
    # *"talvez seja muito detalhe aqui"* — o cabelo e o bigode moravam no FIM
    # de uma descricao longa de gordura e perdiam peso. Agora abrem a frase.
    # ⛔ PESO EXATO, sem `around`: *"nao quero que tenha a aproximacao [...]
    # o peso exato no prompt, isso facilita ele ter precisao"*.
    _dele = "his" if sexo_en == "man" else "her"
    # ⭐⭐ A BARRIGA EM DOBRO — carimbada em campo em 21/08: *"esse prompt
    # ficou absurdamente perfeito, registre ele na memoria imediatamente"*.
    # ⛔ A alavanca nova, e a que explica o salto, e' a ANCORA DE QUADRO. Ate'
    # aqui o prompt media a barriga contra o CORPO dele (*passa dos
    # joelhos*), e isso um homem so' grande ja' satisfaz. Medir contra o
    # QUADRO — metade inferior, de borda a borda — nao tem meio-termo,
    # porque e' o mesmo espaco em que o gerador compoe a imagem.
    # ⭐ E a OCLUSAO junto (esconde colo, joelhos e a cadeira): esconder
    # objeto de tamanho conhecido forca volume como adjetivo nenhum forca.
    # ⚠️ As sete rodadas anteriores morreram tentando adjetivo mais forte,
    # camera mais longe e geometria relativa ao proprio corpo. Nenhuma das
    # tres esta' aqui — se alguem for encurtar este bloco um dia, corte a
    # oclusao, nunca a ancora de quadro.
    return ("A %d-year-old %s %s with %s, and %s. This hair and facial hair "
            "must appear exactly as described.%s %s body is that of the very "
            "largest super-heavyweight sumo wrestler in the world, weighing "
            "exactly %d pounds, "
            "sitting upright in a relaxed, normal posture on a small wooden "
            "chair: one gigantic soft round ball of a belly starts at the "
            "chest and hangs all the way down past the knees until it rests "
            "on the ground, and it is by far the largest thing in the "
            "picture — it fills the entire lower half of the frame from the "
            "left edge to the right edge, far wider than %s shoulders and "
            "wider than the whole chair, completely hiding %s lap, %s knees "
            "and almost all of the chair behind it, pointed toward the lens "
            "as the closest "
            "object in the frame; %s %s is stretched drum-tight over the "
            "entire ball and covers all of it, "
            "the hem hanging low below the waistband so the whole belly "
            "stays inside the shirt; upper arms thicker than thighs hanging "
            "with loose soft flesh folding over the elbows, forearms round "
            "and swollen, puffy hands with thick soft fingers, the neck "
            "buried in deep rolls of soft flesh with a triple chin spilling "
            "onto the chest, heavy sagging jowls and round puffed cheeks"
            % (s["idade"], spec["pele_sujeito"], sexo_en, s["visual"],
               s["rosto"], "",
               "His" if sexo_en == "man" else "Her", spec["peso_lb"],
               _dele, _dele, _dele, _dele, roupa))


def montar(spec):
    cen = spec["cenario"]
    nar = _nar_desc(spec)
    nar_ela = "she" if spec["narrador"]["sexo"] == "f" else "he"
    nar_dela = "her" if spec["narrador"]["sexo"] == "f" else "his"
    suj_en = "man" if spec["sexo_sujeito"] == "homem" else "woman"
    suj_ele = "he" if spec["sexo_sujeito"] == "homem" else "she"
    suj_dele = "his" if spec["sexo_sujeito"] == "homem" else "her"

    # ⛔⛔ AS MAOS DO SENTADO — conserto do defeito mais visivel da gravacao
    # de 21/08: *"do nada aparece uma colher na mao dele"*, em 8 de 8
    # geracoes dos takes 1 e 2. O gerador inventa o objeto porque a cena tem
    # UMA colher e DUAS pessoas, e nada diz de quem ela e'.
    # ⛔ NA IMAGEM: maos vazias, parado. E' descricao de ESTADO.
    # ⚠️ JOELHOS, NAO COXAS — 2026-08-21. O take 2 comecou a ser recusado
    # pela politica e a hipotese do operador foi a coxa: *"acredito que e'
    # referente a citacao de mao na coxa ou algo do tipo"*. A palavra dele e'
    # `joelhos` (*"apenas deixar as maos sobre os joelhos imoveis"*), e a
    # troca custa nada: o gesto e' o mesmo e o token sai.
    # ⛔ Nao e' diagnostico fechado — o take 1 carrega a MESMA clausula de
    # coxa e passou. Ver a nota no `t2` sobre o que mais mudou junto.
    MAOS_SENTADO = ("Both of the seated %s's hands rest empty on %s own "
                    "knees — %s holds nothing, and there is no spoon, cup "
                    "or object of any kind in %s hands. The only spoon in "
                    "the scene is the one held by the narrator."
                    % (suj_en, suj_dele, suj_ele, suj_dele))
    # ⛔⛔ NO TAKE: e' o MOVIMENTO que precisa ser proibido, nao o estado.
    # Defeito filmado pelo operador em 21/08 e conferido quadro a quadro por
    # mim: nos tres primeiros frames as maos estao nas coxas, e no quarto ele
    # JA' ergueu o braco com uma colher amarela — dai em diante come sozinho
    # e a colher da narradora some. A clausula de imagem nao pegava isso: ela
    # descreve um ESTADO, e o gerador leu *"a colher vai a' boca dele"* como
    # *"ele leva a colher a' boca"*. Quem responde a isso e' um verbo negado.
    # ⛔⛔⛔ A NEGACAO ERA O DEFEITO — 2026-08-21, o conserto mais caro do dia.
    # =======================================================================
    # A versao anterior tinha DEZ clausulas negando a colher na mao dele, e a
    # colher continuou nascendo. O operador filmou de novo e eu conferi o
    # frame: aos 0,75s a colher MATERIALIZA na mao PARADA, no colo, com o
    # braco ainda embaixo — a trava de movimento estava sendo OBEDECIDA e o
    # bug acontecia assim mesmo. Logo o alvo estava errado: nao era o
    # movimento, era o OBJETO.
    # ⛔ Medido no prompt reprovado: `spoon` aparecia OITO vezes, e TRES
    # clausulas colavam `colher` em `mao do homem sentado` — todas em
    # negacao. A atencao cruzada encoda o sintagma, nao o `never`. E' o
    # `not a celebrity` aplicado a um objeto: descrever o quadro proibido
    # sete vezes e' pinta'-lo sete vezes.
    # ⭐⭐ O conserto e' POSITIVO e foi escolhido POR TESTE DE CAMPO, nao por
    # gosto: mandei tres variacoes e o operador rodou as seis (21/08).
    #   take 1 -> variacao B: enumerar o UNICO movimento que ele tem;
    #   take 2 -> variacao C: B + as maos com TAREFA + a trava de CONTAGEM.
    # ⛔ A lista `Do NOT show:` inteira SAIU dos dois. Ela era a maior fonte
    # de injecao — e quem cobra que ela nao volte e' a `AM10`.
    #
    # ⭐ VARIACAO B — o take 1. Nada e' negado: diz-se o que ele FAZ, e a
    # enumeracao fecha o resto por exclusao.
    MOVIMENTO_T1 = ("The seated %s's only movement in the entire shot is %s "
                    "mouth opening to receive the spoonful, closing, and %s "
                    "eyes widening; everything else about %s is frozen "
                    "exactly as in the photograph — %s arms, %s hands and %s "
                    "shoulders hold the identical position from the first "
                    "frame to the last. The narrator is the only person in "
                    "the frame whose arms move."
                    % (suj_en, suj_dele, suj_dele, suj_ele, suj_dele,
                       suj_dele, suj_dele))
    # ⭐ VARIACAO C — o take 2. As maos GANHAM TAREFA (agarrar as rotulas):
    # mao ocupada e' incompativel com mao segurando colher, e a frase nao
    # precisa dizer `colher` para isso. Fecha com a trava de CONTAGEM, que
    # e' a unica mencao a colher que sobra do lado dele — e ela e'
    # afirmativa: existe UMA, e ela esta' com o narrador.
    MOVIMENTO_T2 = ("The seated %s keeps both hands closed around %s own "
                    "kneecaps, fingers curled over the front of each knee, "
                    "gripping them steadily, and %s arms stay locked in that "
                    "exact position from the first frame to the last. %s "
                    "only movement in the entire shot is %s mouth opening to "
                    "receive the spoonful, closing, and %s eyes widening. "
                    "The narrator is the only person in the frame who moves: "
                    "%s arm reaches in from the side and does all of the "
                    "feeding, and %s is the only hand that ever comes near "
                    "%s face. Exactly one spoon exists in this scene from "
                    "beginning to end, and it stays in the narrator's "
                    "fingers the whole time."
                    % (suj_en, suj_dele, suj_dele, suj_dele.capitalize(),
                       suj_dele, suj_dele, nar_dela,
                       "hers" if spec["narrador"]["sexo"] == "f" else "his",
                       suj_dele))
    # ⛔⛔ A GARRAFA NA MAO — *"ela soltou a garrafa [...] do nada a garrafa
    # vai aparecer de novo, esse bug visual nao pode acontecer"*.
    _GARRAFA_DEF = _GARRAFA.replace("a dark", "the dark", 1)
    # ⛔ SUJEITO EXPLICITO, nunca pronome. A versao anterior abria com
    # `He keeps...` logo depois de duas frases sobre o homem SENTADO — e o
    # `He` mais proximo e' ele, nao o narrador. Pronome ambiguo num prompt
    # nao e' estilo: e' o gerador escolhendo por conta, que e' a familia de
    # defeito que esta cena ja' pagou com a colher fantasma.
    GARRAFA_TRAVADA = ("The narrator keeps %s gripped in the same hand for "
                       "the entire shot: it never leaves the narrator's "
                       "hand, never disappears and never reappears, and it "
                       "stays visible in frame from the first frame to the "
                       "last." % _GARRAFA_DEF)
    # ⚠️ Nos takes 1-2 o narrador tem DUAS maos ocupadas — uma alimenta, a
    # outra segura a garrafa — e a frase precisa dizer QUAL, senao o gerador
    # e' quem escolhe. Nos takes 3-4 nao existe mao que alimenta, e dizer
    # `the other hand` la' inventaria uma segunda tarefa que a cena nao tem.
    GARRAFA_ALIMENTA = GARRAFA_TRAVADA.replace(
        "in the same hand", "in %s other hand" % nar_dela, 1)
    # ⛔ MAO FANTASMA — *"com uma mao que nao existe, mao fantasma"*.
    DUAS_MAOS = ("Exactly two hands are visible in the whole frame and both "
                 "belong to the narrator; no extra hand, arm or finger "
                 "appears at any moment.")

    # ⛔⛔ O FUNDO PARADO — 2026-08-21, a carroca em looping.
    # =======================================================================
    # O `vida` do cenario entra nos QUATRO takes. Enquanto ele era um verbo
    # de travessia, o mesmo objeto atravessava o quadro quatro vezes: no
    # take 1, de novo no take 2 (47 dias depois) e mais duas no 3 e no 4,
    # que saem da MESMA imagem. *"A carroca ja' deveria ter passado."*
    # ⭐ A trava e' POSITIVA e nao nomeia nenhum veiculo: dizer *"no wagon
    # crossing"* injetaria a carroca no prompt — a licao do `not a
    # celebrity`, paga em 30 motores. Aqui o `vida` sorteado e' declarado o
    # UNICO movimento permitido, e tudo o mais fica onde esta'. O que nao e'
    # nomeado nao e' desenhado.
    def _fundo_parado(vida):
        # ⚠️ E a clausula nao lista substantivos (`wagon`, `cart`, `buggy`)
        # nem para mandar parar: o que se escreve, o gerador desenha.
        # ⚠️ E sem pronome: a versao anterior dizia *"anywhere behind THEM"*,
        # e nos takes 3 e 4 so' a narradora esta' em quadro — `them` sem
        # referente e' a mesma familia de defeito da garrafa (`He keeps...`
        # lido como o homem sentado).
        return ("The background holds perfectly still: the only movement "
                "anywhere in the background is this, and nothing else moves "
                "at all — %s. Everything else in the background stays "
                "exactly where it is from the first frame to the last, and "
                "nothing travels across the frame." % vida.rstrip("."))

    # ⛔⛔ SEM BLOCO 0 (REF) — ordem de 21/08: a IMAGE 01 e' a unica descricao
    # completa e as IMAGEs 02/03 sao instrucoes de EDICAO sobre ela.
    # ⭐ O SUJEITO ABRE O PROMPT — foi parte do que destravou a massa nas
    # sete rodadas de teste; o cenario desceu para o fim.
    _suj = _suj_desc(spec)
    _suj = _suj[0].upper() + _suj[1:]
    b1 = ("%s %s. The small wooden chair has completely vanished under the "
          "seated %s. Standing at the side, small next to the seated %s, "
          "%s holds %s in one hand and lifts a spoonful of dark syrup "
          "toward the seated %s's wide-open mouth with the other. %s They "
          "are %s %s"
          % (ORIENTACAO, _suj, suj_en, suj_en, nar, _GARRAFA, suj_en,
             MAOS_SENTADO, cen["desc"] + ".", _SEM_TEXTO_IMG + " "
             + NEGATIVO_IMG))

    # ⭐ VARIACAO B, escolhida em campo pelo operador (21/08): *"a variacao B
    # foi a que melhor funcionou no take 1"*. Ver o bloco do `MOVIMENTO_T1`.
    # ⚠️ `the narrator's HAND slides` — a mao e' nomeada como sujeito da
    # acao. Faz parte da variacao testada; nao trocar por `the narrator`.
    t1 = ("Animate the provided image exactly as it is. Within the first "
          "second the narrator's hand slides the spoonful into the seated "
          "%s's mouth; %s swallows, %s eyes going wide at the taste, and the "
          "narrator nods once, pleased. %s %s %s %s Camera: static "
          "handheld with a barely visible sway. Audio: completely silent — "
          "no sound at all, no ambience, no music, no wind, no voice."
          % (suj_en, suj_ele, suj_dele, MOVIMENTO_T1, GARRAFA_ALIMENTA,
             _fundo_parado(cen["vida"]), _SEM_TEXTO_TK))

    b2 = ("Using the provided image as the exact base. This is the SAME "
          "SCENE and the SAME TWO PEOPLE from the base image, photographed "
          "again months later — not a new photo and not new people. Keep "
          "the place, the framing, the light, the narrator and the wooden "
          "chair exactly as they are; the narrator is in the same spot, in "
          "the same clothes, holding the same dark amber glass bottle and "
          "lifting another spoonful of dark syrup. The only thing that "
          "changed is the seated %s's BODY: seated on the chair is %s. %s "
          "%s %s"
          % (suj_en, _suj_desc(spec, magro=True), MAOS_SENTADO,
             _SEM_TEXTO_IMG, NEGATIVO_MAGRO))

    # ⛔⛔ O JOINHA CAIU — 2026-08-21, recusa de politica no take 2.
    # =======================================================================
    # Ordem do operador, com a recusa na mao: *"o homem nunca deve fazer
    # sinal de joinha ou positivo, apenas deixar as maos sobre os joelhos
    # imoveis"*.
    # ⚠️ TRES COISAS MUDARAM DE UMA VEZ, e isso e' declarado de proposito
    # porque o RUNBOOK-bisseccao-moderacao manda isolar UMA variavel:
    #   1. o joinha saiu           — ordem direta, nao e' teste;
    #   2. `thighs` -> `knees`     — hipotese DELE, e a palavra que ele usou;
    #   3. `lips`   -> `mouth`     — hipotese MINHA.
    # ⛔ A (2) sozinha explica mal a recusa: o take 1 carrega a MESMA
    # clausula de coxa e passa. O que o take 2 tinha de exclusivo era
    # `lips` + `thumbs-up` + `grinning` + uma mao subindo — e o take 1, que
    # passa, diz `mouth`. Por isso a (3) entrou junto.
    # ⚠️ Se voltar a ser recusado, o proximo suspeito nao e' mais a mao: e'
    # a colherada na boca de um adulto por outro adulto, que e' a unica
    # coisa que sobra em comum entre os dois takes.
    # ⭐ VARIACAO C, escolhida em campo pelo operador (21/08): *"a variacao C
    # foi a que melhor funcionou no take 2"*. Ver o bloco do `MOVIMENTO_T2`.
    # ⚠️ E' a variacao MAIS PESADA das tres, e ela ganhou justamente no take
    # que tambem apanhava da moderacao — as maos com tarefa fecham as duas
    # frentes de uma vez: mao ocupada nao segura colher e nao fica pousada
    # sobre a propria perna.
    t2 = ("Animate the provided image exactly as it is. Within the first "
          "second the narrator's hand brings the spoonful to the seated "
          "%s's mouth and %s swallows, %s eyes going wide at the taste, "
          "while the narrator smiles, pleased. %s %s %s %s Camera: "
          "static handheld with a barely visible sway. Audio: completely "
          "silent — no sound at all, no ambience, no music, no wind, no "
          "voice."
          % (suj_en, suj_ele, suj_dele, MOVIMENTO_T2,
             GARRAFA_ALIMENTA, _fundo_parado(cen["vida"]),
             _SEM_TEXTO_TK))

    b3 = ("Using the provided image as the base. Keep the same narrator — "
          "the same face, the same clothes, the same light — and the same "
          "location, but reframe as a selfie: the narrator now fills the "
          "lower half of the frame, face close to the lens, looking "
          "straight into it, %s visible behind %s. %s holds %s raised in "
          "front of %s chest, the label clearly visible, the bottle fully "
          "inside the frame. The seated person from the base image is no "
          "longer in frame. %s"
          % (cen["curto"], nar_dela, nar_ela.capitalize(), _GARRAFA,
             nar_dela, _SEM_TEXTO_IMG + " " + NEGATIVO_IMG))

    _voz = spec["narrador"]["voz"]
    t3 = ("Animate the provided image exactly as it is. The narrator speaks "
          "straight into the lens at a brisk, natural conversational pace, "
          "with small head movements, warm and direct like a video call. "
          "%s %s %s %s Camera: selfie held at arm's length, slight handheld "
          "sway. Audio: only the narrator's voice — %s — with no music and "
          "no background sound.\n"
          'Dialogue: "%s"'
          % (GARRAFA_TRAVADA, DUAS_MAOS, _fundo_parado(cen["vida"]),
             _SEM_TEXTO_TK, _voz, sonorizar(spec["falas"][2])))

    # ⭐⭐ TAKE 04 — anima a MESMA IMAGE 03, continuando a fala do take 3.
    # ⛔ O gesto de erguer a garrafa mudou de casa: ele era o fecho do take 3
    # e agora fecha o take 4, que e' o ultimo frame do video.
    # ⚠️ O OPERADOR CONTOU AS IMAGENS E ACHOU QUE FALTAVA UMA (21/08):
    # *"so' esta' gerando 3 imagens [...] imagino que e' pra gerar o take do
    # CTA parte 1 e parte 2 tudo com a imagem 3"*. Era, sim — mas o bloco
    # nao dizia, e contrato que so' existe na minha cabeca e' contrato que o
    # operador descobre errando. Agora ele diz na primeira linha.
    t4 = ("(Use the SAME IMAGE 03/03 as the base for this take — there is no "
          "separate image 04.) Animate the provided image exactly as it is. "
          "This is the direct "
          "continuation of the previous shot: the same narrator, same "
          "selfie framing, same light, still speaking straight into the "
          "lens at a brisk, natural conversational pace. In the final two "
          "seconds %s raises the bottle closer to the lens until it fills "
          "part of the frame. %s %s %s %s Camera: selfie held at arm's "
          "length, slight handheld sway. Audio: only the narrator's voice "
          "— %s — with no music and no background sound.\n"
          'Dialogue: "%s"'
          % (nar_ela, GARRAFA_TRAVADA, DUAS_MAOS,
             _fundo_parado(cen["vida"]), _SEM_TEXTO_TK, _voz,
             sonorizar(spec["falas"][3])))

    blocos = {
        IMAGENS[0]: b1, TAKES[0]: t1,
        IMAGENS[1]: b2, TAKES[1]: t2,
        IMAGENS[2]: b3, TAKES[2]: t3,
        TAKES[3]: t4,
    }
    blocos = sc.selar_tags(blocos)
    # ⛔ SEM `sc.selar_takes` — de proposito, e e' o unico motor do parque
    # assim. A clausula propria `_SEM_TEXTO_TK` ja' esta' em TODOS os quatro
    # takes e cobre mais que a compartilhada (numeros e lettering, que sao
    # justamente o que o DAY deixou de ser). Somar as duas poria duas travas
    # dizendo a mesma coisa em palavras diferentes: dilui o prompt e as duas
    # envelhecem separadas.
    return blocos


# ===========================================================================
# LENTES
# ===========================================================================
def _am1_limpo(spec, blocos, ach):
    """⭐⭐ AM1 — NENHUM texto em quadro nenhum. O DAY e' do EDITOR.

    ⛔ Ordem de 2026-08-21, depois de o operador filmar oito geracoes: a
    legenda DESAPARECIA no meio do take em 8 de 8, e dois lotes de imagem
    vieram com TARJA PRETA atras do texto. *"Remova completamente esse dia 1
    e dia 50 e poucos do prompt [...] coloque pro editor conseguir fazer essa
    legenda queimada"*. Prompt nao consegue fixar texto; o ffmpeg consegue.
    ⚠️ A lente inverteu de sinal: antes EXIGIA o caption, agora o PROIBE."""
    for nome in list(IMAGENS) + list(TAKES):
        txt = blocos.get(nome, "")
        if '"DAY' in txt or "caption reading" in txt:
            ach.append(("ERRO", "AM1: %s pede legenda ao gerador — o DAY sai "
                                "no editor desde 21/08" % nome))
    for nome in IMAGENS:
        if "no text, no caption" not in blocos.get(nome, "").lower():
            ach.append(("ERRO", "AM1: %s sem a trava de quadro limpo — sem "
                                "ela vem texto inventado e tarja preta"
                        % nome))
    for nome in TAKES:
        if "no text, no caption" not in blocos.get(nome, "").lower():
            ach.append(("ERRO", "AM1: %s sem a trava de quadro limpo" % nome))
    if not (DIA_MIN <= spec["dia2"] <= DIA_MAX):
        ach.append(("ERRO", "AM1: dia2=%r fora de %d-%d — o numero vai para o "
                            "editor, mas continua sendo sorteado aqui"
                    % (spec["dia2"], DIA_MIN, DIA_MAX)))


def _am2_copy(spec, blocos, ach):
    """⛔⛔ AM2 — as DUAS partes da copy chegam VERBATIM, uma por take.

    ⭐ E a soma delas tem de ser a copy validada inteira: partir a fala em
    dois takes nao pode virar desculpa para reescrever meia frase."""
    for i, take in ((2, TAKES[2]), (3, TAKES[3])):
        alvo = 'Dialogue: "%s"' % sonorizar(spec["falas"][i])
        if alvo not in blocos.get(take, ""):
            ach.append(("ERRO", "AM2: a parte %d da copy %r nao chegou "
                                "intacta ao %s — copy validada nao se "
                                "reescreve no caminho"
                        % (i - 1, spec["copy"]["id"], take)))
    if spec["falas"][0] or spec["falas"][1]:
        ach.append(("ERRO", "AM2: fala nos takes 1-2 — eles sao MUDOS"))
    inteira = (spec["falas"][2] + " " + spec["falas"][3]).strip()
    kw = _kw()
    if len(re.findall(r"\bcomment %s\b" % re.escape(kw), inteira,
                      re.IGNORECASE)) != 1:
        ach.append(("ERRO", "AM2: a copy inteira nao tem exatamente um "
                            "`comment %s`" % kw))
    # ⛔ o teto e' POR TAKE, e o relogio de cada um e' diferente
    for i, n in ((2, 3), (3, 4)):
        p = _palavras(spec["falas"][i])
        if p > TETO_FALA[n]:
            ach.append(("ERRO", "AM2: a parte %d tem %d palavras e o TAKE 0%d "
                                "e' de %ds (teto %d) — foi assim que a COPY 1 "
                                "cortou em 3 de 4 geracoes"
                        % (i - 1, p, n, SEGUNDOS_TAKE[n], TETO_FALA[n])))


def _am4_mudez(spec, blocos, ach):
    """⛔ AM4 — os dois lados da excecao de texto deste motor."""
    for nome in (TAKES[0], TAKES[1]):
        t = blocos.get(nome, "")
        if "Dialogue:" in t:
            ach.append(("ERRO", "AM4: %s com Dialogue — os takes 1-2 sao "
                                "mudos" % nome))
        if sc.SEM_TEXTO_TAKE in t:
            ach.append(("ERRO", "AM4: %s com a trava de sem-texto — ela "
                                "mataria o DAY que o Veo tem de escrever"
                        % nome))
        if "completely silent — no sound at all" not in t:
            ach.append(("ERRO", "AM4: %s sem a clausula de SILENCIO TOTAL — "
                                "ordem de 21/08: a musica entra no editor, o "
                                "take nasce mudo" % nome))
    # ⚠️ A trava de texto dos takes de FALA e' a propria (`_SEM_TEXTO_TK`),
    # cobrada pela AM1 em todos os quatro. A compartilhada saiu para nao
    # haver duas dizendo o mesmo.
    for nome in (TAKES[2], TAKES[3]):
        if "Dialogue:" not in blocos.get(nome, ""):
            ach.append(("ERRO", "AM4: %s sem linha Dialogue — os takes 3 e 4 "
                                "sao os que falam" % nome))


def _am5_pronome(spec, blocos, ach):
    """⛔ AM5 — pronome e nome seguem o SEXO do sujeito (a unica variacao)."""
    fala = spec["falas"][2]
    cid = spec["copy"]["id"]
    if cid in ("c1", "c3"):
        errado = r"\bher\b" if spec["sexo_sujeito"] == "homem" else \
                 r"\b(him|his)\b"
        if re.search(errado, fala):
            ach.append(("ERRO", "AM5: pronome do sexo errado na copy %s "
                                "(sujeito=%s)" % (cid, spec["sexo_sujeito"])))
    if cid == "c3" and spec["nome"] not in NOMES[spec["sexo_sujeito"]]:
        ach.append(("ERRO", "AM5: nome %r fora do pool do sexo %s"
                    % (spec["nome"], spec["sexo_sujeito"])))


def _am6_garrafa(spec, blocos, ach):
    """⭐ AM6 — a garrafa ambar atravessa os tres takes (e' a assinatura)."""
    for nome in IMAGENS + TAKES:
        if "amber" not in blocos.get(nome, "").lower():
            ach.append(("ERRO", "AM6: %s sem a garrafa ambar" % nome))


def _am9_peso(spec, blocos, ach):
    """⭐⭐ AM9 — a FORMULA SUMO chega inteira a IMAGE 01.

    Calibrada em sete rodadas de geracao real com o operador (21/08). As
    ancoras cobradas sao as que MOVERAM o corpo nos testes; perder qualquer
    uma e' voltar ao fazendeiro rechonchudo que ele reprovou seis vezes."""
    b1 = blocos.get(IMAGENS[0], "")
    for alvo, motivo in [
            ("the very largest super-heavyweight sumo wrestler in the world",
             "o token de silhueta, no grau que ele carimbou em 21/08"),
            # ⭐⭐ AS DUAS ANCORAS DA BARRIGA EM DOBRO (21/08). A de QUADRO e'
            # a que explica o salto: medir contra a moldura em vez de contra
            # o proprio corpo. Sem lente, ela e' a primeira coisa que um
            # refactor de encurtamento apaga.
            ("fills the entire lower half of the frame",
             "a ancora de QUADRO — sete rodadas mediram contra o corpo dele "
             "e nenhuma funcionou"),
            ("until it rests on the ground",
             "ate' onde a barriga desce; `past the knees` um homem so' "
             "grande ja' satisfaz"),
            ("completely hiding",
             "a OCLUSAO: esconder objeto de tamanho conhecido forca volume"),
            ("exactly %d pounds" % spec["peso_lb"],
             "peso EXATO — `around` foi vetado em 21/08 (*\"nao quero a "
             "aproximacao\"*)"),
            ("must appear exactly as described",
             "a identidade abre a frase; no fim de uma lista de gordura ela "
             "perdia peso e saiam 4 geracoes sem bigode"),
            # ⛔⛔ REVERTIDO EM 21/08: era `small strip of bare belly`, e o
            # operador viu o resultado e mandou o oposto — *"para a imagem 1
            # a barriga nunca estar para fora da camisa"*. A faixa de pele
            # que a versao anterior PEDIA saiu; a camisa cobre a bola
            # inteira. A lente vira ao contrario junto: cobra a cobertura e
            # proibe a faixa nua, senao a ordem antiga volta num refactor.
            ("the whole belly stays inside the shirt",
             "a camisa cobre a barriga INTEIRA (ordem de 21/08, revertendo "
             "a faixa de pele que a versao anterior pedia)"),
            ("sitting upright in a relaxed, normal posture",
             "sem a pose de quem passa mal (ordem final)"),
            ("closest object in the frame",
             "a barriga apontada para a lente e' o truque de perspectiva")]:
        if alvo not in b1:
            ach.append(("ERRO", "AM9: IMAGE 01 sem %r — %s" % (alvo, motivo)))
    # ⛔ e a faixa de pele nao pode VOLTAR: e' a ordem de 21/08 ao contrario
    if re.search(r"bare belly|belly shows|strip of bare", b1, re.I):
        ach.append(("ERRO", "AM9: IMAGE 01 pedindo pele nua na barriga — o "
                            "operador mandou a camisa cobrir tudo em 21/08"))
    # ⛔ a palavra explicita e' o token de politica — nunca em bloco nenhum
    for nome, txt in blocos.items():
        if re.search(r"\bobese\b|\bobesity\b|\bfat\b", txt, re.I):
            ach.append(("ERRO", "AM9: %s com palavra explicita de condicao "
                                "— o numero informa, a palavra viola" % nome))
    if not (PESO_MIN <= spec["peso_kg"] <= PESO_MAX):
        ach.append(("ERRO", "AM9: peso %r fora de %d-%d kg"
                    % (spec["peso_kg"], PESO_MIN, PESO_MAX)))


def _am10_bugs(spec, blocos, ach):
    """⭐⭐ AM10 — as tres travas de BUG filmadas pelo operador em 21/08.

    Cada uma nasceu de um defeito visto em geracao real, nao de suposicao:
      · a COLHER FANTASMA na mao do sentado — 8 de 8 takes;
      · a GARRAFA que a narradora SOLTA e que reaparece do nada;
      · a MAO FANTASMA no take do CTA.
    ⛔ Clausula sem lente e' forma sem funcao: some no proximo refactor e
    ninguem percebe ate' o lote sair errado."""
    for nome in (IMAGENS[0], IMAGENS[1]):
        if "hands rest empty" not in blocos.get(nome, ""):
            ach.append(("ERRO", "AM10: %s sem a trava de ESTADO das maos "
                                "— maos vazias na imagem parada" % nome))
    # ⛔⛔⛔ NOS TAKEs A LENTE VIROU AO CONTRARIO — 2026-08-21.
    # Ela cobrava TRES literais de negacao (`never takes, holds, reaches
    # for or touches the spoon`, `The ONLY hand that moves toward`, `Do NOT
    # show:`) — e a medicao do frame provou que essas tres eram a CAUSA, nao
    # o conserto: com as dez negacoes no lugar, a colher continuava nascendo
    # na mao parada aos 0,75s. O que passou em campo foram as variacoes
    # POSITIVAS (B no take 1, C no take 2), e e' isso que a lente cobra
    # agora — mais a proibicao de a lista `Do NOT show:` voltar.
    # ⛔ A memoria do defeito NAO cai: os literais antigos viram o CONTROLE,
    # nao o alvo. Quem os replantar e' acusado.
    ancoras = {TAKES[0]: ["only movement in the entire shot",
                          "frozen exactly as in the photograph",
                          "the only person in the frame"],
               TAKES[1]: ["closed around", "kneecaps",
                          "only movement in the entire shot",
                          "the only person in the frame",
                          "Exactly one spoon exists"]}
    for nome, lits in ancoras.items():
        txt = blocos.get(nome, "")
        for lit in lits:
            if lit not in txt:
                ach.append(("ERRO", "AM10: %s sem %r — e' a variacao que "
                                    "passou em campo em 21/08 (B no take 1, "
                                    "C no take 2)" % (nome, lit)))
    for nome in (TAKES[0], TAKES[1]):
        txt = blocos.get(nome, "")
        if "Do NOT show:" in txt:
            ach.append(("ERRO", "AM10: %s com a lista `Do NOT show:` de "
                                "volta — ela era a maior fonte de injecao "
                                "da colher na mao dele" % nome))
        # ⛔ e nenhuma clausula pode colar COLHER em MAO DELE, nem negando
        for m in re.finditer(r"[^.;:]+", txt):
            fr = m.group(0)
            if re.search(r"spoon", fr, re.I) and \
               re.search(r"\b(?:his|her) hand|seated %s's hand"
                         % ("man" if spec.get("sexo_sujeito") == "homem"
                            else "woman"), fr, re.I) and \
               "narrator" not in fr:
                ach.append(("ERRO", "AM10: %s cola `spoon` na mao do sentado "
                                    "(%r) — foi assim que ela nasceu la'"
                            % (nome, fr.strip()[:60])))
    for nome in (TAKES[0], TAKES[1], TAKES[2], TAKES[3]):
        if "never leaves" not in blocos.get(nome, ""):
            ach.append(("ERRO", "AM10: %s sem a trava da GARRAFA — ela some "
                                "da mao e volta do nada" % nome))
    for nome in (TAKES[2], TAKES[3]):
        if "Exactly two hands" not in blocos.get(nome, ""):
            ach.append(("ERRO", "AM10: %s sem a trava das DUAS MAOS — mao "
                                "fantasma no take do CTA" % nome))


# ⚠️⚠️ DUAS PALAVRAS SOZINHAS NAO SERVEM, e as duas foram achadas MEDINDO O
# PROMPT GERADO — nenhuma aparecia na pool:
#   · `past`   — a IMAGE 01 diz que a barriga *"hangs past the knees"*, que
#                e' posicao; acusou 200 de 200 videos CERTOS;
#   · `riding` — a mesma imagem diz *"the hem riding up"*, que e' a camisa
#                subindo, pedido dele; acusou os mesmos 200.
# ⛔ Lente colada no literal cru acusa a si mesma (§16). Aqui os dois so'
# contam em construcao de MOVIMENTO — `creaks slowly past`, `riding along`
# — e o substantivo `rider`, que era o defeito real do pomar, fica.
# ⚠️ E `across the` exclui `frame`: e' a propria trava que diz *"nothing
# travels across the frame"*.
_RX_TRAVESSIA = re.compile(
    r"\b(?:(?:creaks?|rolls?|rumbles?|trundles?|rattles?|clatters?|moves?|"
    r"drives?|walks?|goes|passes|plods?|rides?|riding)\s+(?:\w+\s+)?"
    r"(?:past|along|across|by)|"
    r"passing|crossing|crosses|plods|plodding|"
    r"hauling|hauls|pulled by|pulling|driving|rider|"
    r"approaching|approaches|travels|traveling|travelling|"
    r"along the|across the (?:field|yard|lane|road|track|pasture|barnyard)|"
    r"down the (?:lane|track|road|path))\b", re.I)


def _am11_fundo(spec, blocos, ach):
    """⛔⛔ AM11 — NADA ATRAVESSA O QUADRO (2026-08-21).

    O operador filmou os quatro takes de um video e mostrou a carroca de
    feno passando atras do casal no take 1, passando OUTRA VEZ no take 2 —
    que acontece 47 dias depois — e mais duas no 3 e no 4, que nascem da
    mesma imagem: *"a carroca fica dando looping [...] ela ja' deveria ter
    passado"*.

    ⭐ A lente tem DUAS metades, e a primeira e' a que importa:
      1. audita a POOL INTEIRA, nao so' o cenario sorteado. Cenario ruim
         que hoje nao caiu no sorteio cai amanha, e o defeito volta pela
         porta dos fundos. Mesmo precedente da `GO21` do GOOD 16.
      2. exige a trava de fundo parado nos QUATRO takes, que e' onde o
         `vida` entra e onde o movimento e' de fato pedido.
    """
    for c in CENARIOS:
        for campo in ("desc", "vida", "curto"):
            m = _RX_TRAVESSIA.search(c.get(campo, ""))
            if m:
                ach.append(("ERRO", "AM11: cenario %r tem %r no campo %s — "
                                    "verbo de travessia vira objeto cruzando "
                                    "o quadro nos quatro takes, e o operador "
                                    "filmou esse loop"
                            % (c["id"], m.group(0), campo)))
    for nome in (TAKES[0], TAKES[1], TAKES[2], TAKES[3]):
        if "The background holds perfectly still" not in blocos.get(nome, ""):
            ach.append(("ERRO", "AM11: %s sem a trava de FUNDO PARADO — o "
                                "`vida` entra cru e o fundo volta a se mexer"
                        % nome))


def _am7_pele(spec, blocos, ach):
    """⛔ AM7 — a pele sorteada/travada aparece ESCRITA nos blocos.

    ⚠️ A primeira versao cobrava o LITERAL `Black African` num narrador cuja
    identidade ja' esta' escrita como `African healer` — 89 acusacoes em 400
    videos CERTOS no primeiro autoteste. Lente colada na forma acusa a si
    mesma; o que ela tem de garantir e' que a IDENTIDADE chegue ao quadro:
    nos fixos, o token da identidade; nos livres, a pele sorteada."""
    fixa = spec["narrador"]["pele_fixa"]
    alvo = ("Native American" if fixa == "Native American"
            else "African" if fixa else spec["pele_narrador"])
    if alvo not in blocos.get(IMAGENS[0], ""):
        ach.append(("ERRO", "AM7: a identidade do narrador (%s) nao chegou a "
                            "IMAGE 01" % alvo))
    if spec["pele_sujeito"] not in blocos.get(IMAGENS[0], ""):
        ach.append(("ERRO", "AM7: pele do sujeito (%s) nao chegou a IMAGE 01"
                    % spec["pele_sujeito"]))


def _am8_mesmo(spec, blocos, ach):
    """⭐⭐ AM8 — as IMAGEs 2-3 DERIVAM da IMAGE 01 anexada (ordem 21/08).

    ⛔ Sem a ancora `Using the provided image` o prompt vira descricao solta
    e o gerador inventa outra cena — o tempo que a ordem existe para poupar
    volta em dobro como incoerencia entre quadros."""
    b2 = blocos.get(IMAGENS[1], "")
    # ⛔ ancoras do MAGRO ABSOLUTO (21/08): TRANSFORM (verbo forte), a
    # barriga CHATA com numero, a identidade do rosto restatada e a roupa
    # larga. "Change ONLY" + "slimmer" relativo rendeu gordo em 3 de 4.
    # ⛔ ANCORAS REESCRITAS EM 21/08 — o operador diagnosticou que `TRANSFORM
    # [...] replace the enormous body` fazia o gerador criar uma PESSOA NOVA.
    # As ancoras de hoje sao de CONTINUIDADE, e cada uma responde a um
    # defeito que ele apontou com o dedo na gravacao.
    for lit, motivo in (
            ("Using the provided image", "a base anexada e' a referencia"),
            ("SAME TWO PEOPLE", "e' a mesma gente, nao um retrato novo"),
            ("the very same", "continuidade, nunca substituicao"),
            ("face is IDENTICAL", "*\"mantem o rosto exatamente igual\"*"),
            ("THIN LEGS", "*\"a perna dele nao mudou nada\"*"),
            ("flat stomach", "barriga CHATA, nao 'menor'"),
            ("in a small size that fits",
             "mesma roupa, tamanho P — nao a XXXG folgada")):
        if lit not in b2:
            ach.append(("ERRO", "AM8: IMAGE 02 sem %r — %s" % (lit, motivo)))
    b3 = blocos.get(IMAGENS[2], "")
    for lit in ("Using the provided image", "reframe as a selfie",
                "no longer in frame"):
        if lit not in b3:
            ach.append(("ERRO", "AM8: IMAGE 03 sem %r — a selfie deriva da "
                                "mesma base" % lit))


def lint(spec, blocos):
    ach = []
    for aviso in spec.get("avisos", []):
        ach.append(("AVISO", aviso))
    sc.lint_tags(blocos, ach)
    _am1_limpo(spec, blocos, ach)
    _am2_copy(spec, blocos, ach)
    _am4_mudez(spec, blocos, ach)
    _am5_pronome(spec, blocos, ach)
    _am6_garrafa(spec, blocos, ach)
    _am7_pele(spec, blocos, ach)
    _am9_peso(spec, blocos, ach)
    _am10_bugs(spec, blocos, ach)
    _am11_fundo(spec, blocos, ach)
    _am8_mesmo(spec, blocos, ach)
    sc.lint_anticeleb(blocos, ach)
    # ⛔ O TETO ANTIGO MORREU COM A EXCECAO QUE ELE CARREGAVA: ate' 21/08 a
    # COPY 1 era excecao declarada (34 palavras num take de 8s) e o campo
    # media' o take 3 inteiro. A divisao em QUATRO takes tornou a excecao
    # desnecessaria — cada parte cabe no proprio relogio, e quem cobra isso
    # agora e' a AM2, por take, com o `SEGUNDOS_TAKE` de cada um.
    return ach


# ===========================================================================
# RESUMO
# ===========================================================================
def resumo_pt(spec):
    c = spec["copy"]
    return ("20s, 4 takes (4s+4s+8s+6s no Veo · takes 1-2 cortados a ~3s na "
            "edicao). NARRA: %s, pele %s%s. MUDA: %s de %d anos (%s, pele "
            "%s) — antes ~%d kg, depois LEAN/FIT ~70 kg. CENARIO: %s. "
            "** LEGENDA: os quadros saem LIMPOS — no editor, queime DAY 1 no "
            "take 1 e DAY %d no take 2, estilo %s. ** TAKES 1-2 MUDOS (a "
            "musica entra no editor). COPY %s — PT: %s"
            % (spec["narrador"]["rotulo"], spec["pele_narrador"],
               (" · vestido %s" % spec["cor_vestido"])
               if spec["narrador"]["id"] == "vovo_amish" else "",
               "homem" if spec["sexo_sujeito"] == "homem" else "mulher",
               spec["sujeito"]["idade"], spec["sujeito"]["rotulo"],
               spec["pele_sujeito"], spec["peso_kg"],
               spec["cenario"]["rotulo"], spec["dia2"],
               spec["estilo"]["rotulo"], c["rotulo"],
               spec.get("fala_pt", "")))


# ===========================================================================
# CONTRATO DA UI COMPARTILHADA
# ===========================================================================
EIXOS_UI = [
    ("copy", "A COPY", "COPIES", "rotulo"),
    ("cenario", "O CENARIO", "CENARIOS", "rotulo"),
    ("sujeito", "QUEM MUDA", "sujeitos_do_sexo", "rotulo"),
    ("estilo", "A LEGENDA DAY", "ESTILOS_DAY", "rotulo"),
]
EIXOS_TRAVAVEIS = ["copy", "cenario", "sujeito", "estilo"]
DROPDOWNS_UI = [("narrador", "QUEM NARRA", "NARRADORES", "rotulo")]
TRAVAS_UI = [
    ("copy", "copy", ["livre", "1", "2", "3", "4"]),
    ("sexo_sujeito", "quem muda", ["livre", "homem", "mulher"]),
    ("pele_narrador", "pele narrador", ["livre", "branca", "negra"]),
    ("pele_sujeito", "pele sujeito", ["livre", "branca", "negra"]),
]
IGNORA_PAINEL = ("copy", "sujeito", "estilo")


# ===========================================================================
# AUTOTESTE — aceite e' MEDICAO, nunca relato
# ===========================================================================
def autoteste(n=400):
    print("%s — autoteste, %d sorteios" % (TITULO, n))
    erros = 0
    vistos = {"narrador": set(), "copy": set(), "cenario": set(),
              "sujeito": set(), "estilo": set(), "dia2": set(),
              "sexo": set()}
    for i in range(n):
        rng = random.Random(i)
        s = sortear(["clara", "escura"][i % 2], rng, {})
        b = montar(s)
        for nivel, msg in lint(s, b):
            if nivel == "ERRO":
                erros += 1
                if erros <= 5:
                    print("  [ERRO] seed %d: %s" % (i, msg))
        for k, v in [("narrador", s["narrador"]["id"]),
                     ("copy", s["copy"]["id"]),
                     ("cenario", s["cenario"]["id"]),
                     ("sujeito", s["sujeito"]["id"]),
                     ("estilo", s["estilo"]["id"]),
                     ("dia2", s["dia2"]), ("sexo", s["sexo_sujeito"])]:
            vistos[k].add(v)
    print("  ERRO em %d sorteios ... %d" % (n, erros))
    alvo = {"narrador": len(NARRADORES), "copy": len(COPIES),
            "cenario": len(CENARIOS), "sujeito": len(SUJEITOS),
            "estilo": len(ESTILOS_DAY),
            "dia2": DIA_MAX - DIA_MIN + 1, "sexo": 2}
    falha_alcance = 0
    for k, a in alvo.items():
        ok = len(vistos[k]) == a
        falha_alcance += 0 if ok else 1
        print("  alcance %-9s %2d/%2d %s"
              % (k, len(vistos[k]), a, "ok" if ok else "<-- INALCANCAVEL"))

    # --- travas honradas ---------------------------------------------------
    rng = random.Random(99)
    falha_trava = 0
    for nid in [x["id"] for x in NARRADORES]:
        s = sortear("clara", rng, {}, {"narrador": nid})
        if s["narrador"]["id"] != nid:
            falha_trava += 1
    for i in "1234":
        s = sortear("clara", rng, {}, {"copy": i})
        if s["copy"]["id"] != "c%s" % i:
            falha_trava += 1
    for sx in ("homem", "mulher"):
        s = sortear("clara", rng, {}, {"sexo_sujeito": sx})
        if s["sexo_sujeito"] != sx or \
           s["sujeito"] not in (SUJEITOS_H if sx == "homem" else SUJEITOS_M):
            falha_trava += 1
    s = sortear("clara", rng, {}, {"pele_narrador": "negra",
                                   "narrador": "vovo_amish"})
    if s["pele_narrador"] != "Black American":
        falha_trava += 1
    s = sortear("clara", rng, {}, {"pele_narrador": "negra",
                                   "narrador": "india_anciana"})
    if s["pele_narrador"] != "Native American" or not s["avisos"]:
        falha_trava += 1
    s = sortear("escura", rng, {}, {"pele_sujeito": "branca"})
    if s["pele_sujeito"] != "white American":
        falha_trava += 1
    print("  travas honradas ......... %s"
          % ("ok" if not falha_trava else "%d FALHA(S)" % falha_trava))

    # --- controles NEGATIVOS: plantar o defeito e exigir a acusacao --------
    rng = random.Random(7)
    s = sortear("clara", rng, {})
    b = montar(s)
    cegas = 0

    def _acusa(blocos, trecho, spec=None):
        return any(trecho in m for nv, m in lint(spec or s, blocos)
                   if nv == "ERRO")

    # ⛔ o DAY nao pode VOLTAR ao prompt em silencio (ordem de 21/08)
    p = dict(b)
    p[IMAGENS[0]] += ' A large caption reading "DAY 1" on top.'
    cegas += 0 if _acusa(p, "AM1") else 1
    p = dict(b)
    p[IMAGENS[0]] = p[IMAGENS[0]].replace(_SEM_TEXTO_IMG, "")
    cegas += 0 if _acusa(p, "AM1") else 1
    # ⛔ as tres travas de bug filmadas
    p = dict(b)
    p[IMAGENS[0]] = p[IMAGENS[0]].replace("hands rest empty", "hands rest")
    cegas += 0 if _acusa(p, "AM10") else 1
    # ⛔⛔ OS CONTROLES VIRARAM JUNTO COM A LENTE (21/08): o que se planta
    # agora e' o retorno da NEGACAO, que era a causa medida no frame.
    p = dict(b)
    p[TAKES[0]] = p[TAKES[0]].replace("only movement in the entire shot",
                                      "movement in the shot")
    cegas += 0 if _acusa(p, "AM10") else 1
    p = dict(b)
    p[TAKES[1]] = p[TAKES[1]].replace("Exactly one spoon exists",
                                      "There is one spoon")
    cegas += 0 if _acusa(p, "AM10") else 1
    p = dict(b)
    p[TAKES[1]] = p[TAKES[1]].replace("kneecaps", "knees")
    cegas += 0 if _acusa(p, "AM10") else 1
    # a lista de negacao nao pode VOLTAR a nenhum dos dois
    for _k in (TAKES[0], TAKES[1]):
        p = dict(b)
        p[_k] += (" Do NOT show: the seated man holding a spoon; a spoon "
                  "appearing in the seated man's hand.")
        cegas += 0 if _acusa(p, "AM10") else 1
    # nem uma clausula solta colando colher na mao dele
    p = dict(b)
    p[TAKES[0]] += " No spoon ever appears in his hands at any moment."
    cegas += 0 if _acusa(p, "AM10") else 1
    # ⛔⛔ ESTE CONTROLE JA' FOI INVERTIDO DUAS VEZES EM UM DIA, e o registro
    # das duas fica porque cada volta custou um lote:
    #   1a — exigia que `raising a hand or an arm` NAO estivesse no take 2,
    #        porque o take 2 pedia um joinha e o negativo o contradizia;
    #   2a — com o joinha fora, passou a exigir que ESTIVESSE nos dois;
    #   3a (agora) — exige que NAO esteja em nenhum, porque o frame provou
    #        que a familia inteira de negacao era a causa da colher.
    # ⚠️ A licao sobrevivente e' a terceira e ela e' mais geral que as duas:
    # negar o objeto na mao e' pinta'-lo la'. O que funciona e' ocupar a mao.
    cegas += 0 if not any("raising a hand or an arm" in v
                          for v in b.values()) else 1
    # ⛔ e o joinha nao pode VOLTAR em silencio a nenhum bloco
    cegas += 0 if not any("thumbs-up" in v for v in b.values()) else 1
    # ⛔⛔ AS ANCORAS DA BARRIGA EM DOBRO (prompt carimbado em 21/08)
    for _lit, _fraco in (
            ("fills the entire lower half of the frame", "is very large"),
            ("until it rests on the ground", "past the knees"),
            ("the very largest super-heavyweight sumo wrestler in the world",
             "a super-heavyweight sumo wrestler"),
            ("completely hiding", "partly hiding")):
        p = dict(b)
        p[IMAGENS[0]] = p[IMAGENS[0]].replace(_lit, _fraco)
        cegas += 0 if _acusa(p, "AM9") else 1
    # ⛔ e o peso nao pode cair de volta para a faixa antiga
    _s = dict(s)
    _s["peso_kg"] = 260
    cegas += 0 if _acusa(b, "AM9", _s) else 1
    # ⛔ a faixa de barriga nua nao pode voltar (ordem de 21/08)
    p = dict(b)
    p[IMAGENS[0]] = p[IMAGENS[0]].replace(
        "the whole belly stays inside the shirt",
        "only a small strip of bare belly shows above the waistband")
    cegas += 0 if _acusa(p, "AM9") else 1
    # ⛔ maos nos JOELHOS, nunca nas coxas (recusa de politica de 21/08)
    # ⚠️ A palavra `thigh` SOZINHA nao serve — quarta vez hoje que colo um
    # controle num literal cru e ele acusa o certo. Ela e' legitima em duas
    # descricoes de corpo que o operador aprovou em sete rodadas de teste:
    # `upper arms as thick as thighs` (o obeso) e `the thighs and calves are
    # now slim` (o magro). O que saiu foi a MAO na coxa, e e' so' isso que
    # este controle pode cobrar.
    cegas += 0 if not any(re.search(r"(?:on|over) (?:his|her|the) thigh", v)
                          for v in b.values()) else 1
    # ⛔ e a garrafa e' do NARRADOR, dito com todas as letras
    cegas += 0 if all("The narrator keeps" in b[k] for k in TAKES) else 1
    p = dict(b)
    p[TAKES[2]] = p[TAKES[2]].replace("never leaves", "sometimes leaves")
    cegas += 0 if _acusa(p, "AM10") else 1
    p = dict(b)
    p[TAKES[3]] = p[TAKES[3]].replace("Exactly two hands", "Some hands")
    cegas += 0 if _acusa(p, "AM10") else 1
    p = dict(b)
    p[TAKES[2]] = p[TAKES[2]].replace("comment", "type")
    cegas += 0 if _acusa(p, "AM2") else 1
    # ⛔⛔ A CARROCA EM LOOPING — o defeito que ele filmou em 21/08. Planto o
    # `vida` antigo de volta na pool e exijo que a AM11 acuse; depois tiro a
    # trava de fundo parado de cada take, um por um.
    _guardado = CENARIOS[1]["vida"]
    CENARIOS[1]["vida"] = "the loaded hay wagon creaks slowly past behind them"
    cegas += 0 if _acusa(b, "AM11") else 1
    CENARIOS[1]["vida"] = _guardado
    _guardado = CENARIOS[5]["desc"]
    CENARIOS[5]["desc"] = "a mule cart passing on the dirt lane"
    cegas += 0 if _acusa(b, "AM11") else 1
    CENARIOS[5]["desc"] = _guardado
    # ⚠️ e a pool limpa NAO pode acusar: lente que grita no estado certo
    # ensina o operador a ignorar a lente
    cegas += 0 if not _acusa(b, "AM11") else 1
    for _k in TAKES:
        p = dict(b)
        p[_k] = p[_k].replace("The background holds perfectly still",
                              "The background is alive")
        cegas += 0 if _acusa(p, "AM11") else 1
    p = dict(b)
    p[IMAGENS[0]] += " Ordinary face, not a celebrity."
    cegas += 0 if _acusa(p, "anticeleb") else 1
    p = dict(b)
    p[TAKES[0]] += '\nDialogue: "hello there"'
    cegas += 0 if _acusa(p, "AM4") else 1
    p = dict(b)
    p[TAKES[0]] += " " + sc.SEM_TEXTO_TAKE
    cegas += 0 if _acusa(p, "AM4") else 1
    p = dict(b)
    p[TAKES[3]] = p[TAKES[3]].replace("Dialogue:", "Fala:")
    cegas += 0 if _acusa(p, "AM4") else 1
    s2 = dict(s, sexo_sujeito=("mulher" if s["sexo_sujeito"] == "homem"
                               else "homem"))
    if s["copy"]["id"] in ("c1", "c3"):
        cegas += 0 if _acusa(b, "AM5", spec=s2) else 1
    p = dict(b)
    p[IMAGENS[1]] = p[IMAGENS[1]].replace("the very same", "a new")
    cegas += 0 if _acusa(p, "AM8") else 1
    p = dict(b)
    p[IMAGENS[1]] = p[IMAGENS[1]].replace("flat stomach", "smaller belly")
    cegas += 0 if _acusa(p, "AM8") else 1
    p = dict(b)
    p[IMAGENS[1]] = p[IMAGENS[1]].replace("THIN LEGS", "slimmer legs")
    cegas += 0 if _acusa(p, "AM8") else 1
    p = dict(b)
    p[IMAGENS[1]] = p[IMAGENS[1]].replace("in a small size that fits",
                                          "still loose")
    cegas += 0 if _acusa(p, "AM8") else 1
    p = dict(b)
    p[IMAGENS[2]] = p[IMAGENS[2]].replace("Using the provided image",
                                          "A fresh new scene")
    cegas += 0 if _acusa(p, "AM8") else 1
    # ⛔ o REF nao pode voltar em silencio — a ordem foi tira'-lo
    cegas += 0 if "BLOCO 0 (REF)" not in b else 1
    # ⛔ o prompt negativo e' pedido explicito de 21/08
    for _i in (0, 1, 2):
        cegas += 0 if "Do NOT include" in b[IMAGENS[_i]] else 1
    p = dict(b)
    p[IMAGENS[0]] = p[IMAGENS[0]].replace(
        "exactly %d pounds" % s["peso_lb"], "quite heavy")
    cegas += 0 if _acusa(p, "AM9") else 1
    p = dict(b)
    p[IMAGENS[0]] = p[IMAGENS[0]].replace(
        "super-heavyweight sumo wrestler", "large man")
    cegas += 0 if _acusa(p, "AM9") else 1
    p = dict(b)
    p[IMAGENS[0]] = p[IMAGENS[0]].replace(
        "sitting upright in a relaxed, normal posture", "leaning far back")
    cegas += 0 if _acusa(p, "AM9") else 1
    p = dict(b)
    p[IMAGENS[0]] += " He is an obese man."
    cegas += 0 if _acusa(p, "AM9") else 1
    print("  controles negativos ..... %s"
          % ("todos acusam" if not cegas else "%d CEGO(S)" % cegas))

    ok = not erros and not falha_alcance and not falha_trava and not cegas
    print("\n%s" % ("AUTOTESTE OK" if ok else "AUTOTESTE REPROVADO"))
    return 0 if ok else 1


def stats(n=400):
    print("%s — %d narradores · %d sujeitos (%dH/%dM) · %d cenarios · "
          "%d estilos DAY · %d copies · dias %d-%d"
          % (TITULO, len(NARRADORES), len(SUJEITOS), len(SUJEITOS_H),
             len(SUJEITOS_M), len(CENARIOS), len(ESTILOS_DAY), len(COPIES),
             DIA_MIN, DIA_MAX))
    for c in COPIES:
        print("  %-40s %2d palavras%s"
              % (c["rotulo"],
                 _palavras(c["en"] % {"obj": "him", "nome": "Johnny"}),
                 "  <-- excecao declarada (34, fonte 331k)"
                 if c["id"] == "c1" else ""))
    return autoteste(n)


# ===========================================================================
def main():
    ap = argparse.ArgumentParser(description=TITULO)
    ap.add_argument("--pagina", choices=sorted(ETNIA), default="clara")
    ap.add_argument("--n", type=int, default=1)
    ap.add_argument("--seed", type=int)
    ap.add_argument("--narrador", choices=[x["id"] for x in NARRADORES])
    ap.add_argument("--copy", choices=["1", "2", "3", "4"])
    ap.add_argument("--sexo", choices=["homem", "mulher"])
    ap.add_argument("--pele-narrador", choices=sorted(PELES))
    ap.add_argument("--pele-sujeito", choices=sorted(PELES))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--autoteste", action="store_true")
    ap.add_argument("--stats", action="store_true")
    a = ap.parse_args()

    if a.autoteste:
        return autoteste()
    if a.stats:
        return stats()

    led = _carregar_ledger()
    rng = random.Random(a.seed)
    travas = {}
    if a.narrador:
        travas["narrador"] = a.narrador
    if a.copy:
        travas["copy"] = a.copy
    if a.sexo:
        travas["sexo_sujeito"] = a.sexo
    if a.pele_narrador:
        travas["pele_narrador"] = a.pele_narrador
    if a.pele_sujeito:
        travas["pele_sujeito"] = a.pele_sujeito

    for _ in range(a.n):
        s = sortear(a.pagina, rng, led, travas)
        b = montar(s)
        print("=" * 70)
        print(resumo_pt(s))
        print("=" * 70)
        for k in [x for par in zip(IMAGENS, TAKES) for x in par]:
            print("\n%s\n" % b[k])
        for nivel, msg in lint(s, b):
            print("[%s] %s" % (nivel, msg))
        if not a.dry_run:
            _gravar_ledger(led, s)
    return 0


if __name__ == "__main__":
    sys.exit(main())
