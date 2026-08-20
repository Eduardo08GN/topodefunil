#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""raro16_short.py — randomizador + gerador + linter do **RARO 16**.

    python funil-organico/raro16_short.py --autoteste
    python funil-organico/raro16_short.py --pagina joe

===============================================================================
 ⭐⭐ O QUE ELE E' — e ele e' UMA ROTA NOVA, nao um angulo a mais
===============================================================================
Um video que so' mostra **o preparo em cima da mesa**. Sem rosto, sem corpo, sem
prop falico, sem substancia absurda. A camera filma os COMPONENTES e as MAOS.
O que carrega o video e' o INGREDIENTE RARO — nomeado, com aposto, apoiado num
povo que o consumia — e o METODO em que se prepara.

⛔⛔ ESTE MOTOR NAO USA GELATINA, E ISSO E' ORDEM EXPRESSA DO OPERADOR
(2026-08-20): *"nao iremos trabalhar com gelatina mais nesse agente, inclusive
o cta sera comment recipe"*.
⚠️ CONSEQUENCIA DECLARADA, para ninguem "consertar" depois: os outros 31
motores fecham em `gelatin` porque a VSL vende gelatina. Este fecha em
`recipe`, entao ele **nao casa com a VSL atual** — e' uma rota propria, com
oferta propria, e nao um irmao dos outros. Quem publicar isto apontando para a
VSL de gelatina quebra a congruencia de proposito.

===============================================================================
 A COPY, no arco que o operador ditou
===============================================================================
    *"Tired of going soft? this bizarre method from tribos andinas that pharma
    don't want you to know... (deixar a entender que tal povo era viril por
    conta daquele consumo) nomeia rapidamente o prep recipe nomeando o
    ingrediente raro + coadjuvante e parte para o cta comment recipe"*

  TAKE 1 = a FALHA + o POVO + a farmacia que nao quer que voce saiba
  TAKE 2 = a RECEITA (raro + aposto + preparo) + `Comment recipe`

⭐ O TEOR SEMANTICO E' VINCULADO, e nao decorativo: o povo do take 1 SAI do
raro sorteado. Sortear tribo por fora produziria "as tribos andinas" num video
de acafrao persa — que e' o drifting que o operador reprova no teste WTF.

⛔⛔ E A TRIBO TEM ACURACIA HISTORICA PERTINENTE, por ordem dele. Cada povo
abaixo casa com a origem real da planta: maca/Andes, catuaba/Tupi,
ginseng/Coreia, ashwagandha/India, muira puama/Amazonia, epimedium/montanhas
da China, acafrao/Persia. ⚠️ A VIRILIDADE e' IMPLICADA pela vizinhanca da
frase (o hook fala da falha, o povo "bebia isso por geracoes"), nunca afirmada
como fato historico — que seria alegacao que nao se sustenta.

===============================================================================
 OS EIXOS
===============================================================================
  AMBIENTES  14 · a mesa e o entorno, com superficie + luz + audio juntos
  CAMERAS    12 · o angulo, generoso por ordem dele (*"pra nao ficar monotono"*)
  ACOES      10 · a manipulacao: despeja, mexe, coa, ergue
  RAROS      14 · o mesmo pool canonico dos outros motores, + a tribo
  PREPAROS   16 · o METODO, que e' o que aparece em quadro
  MAOS       10 · a ancora de continuidade, ja' que nao ha' rosto

⛔⛔ O CRITERIO DO PAR E' QUIMICA DE EXTRACAO, NAO SABOR — e isso corrige um
erro meu. A primeira versao deste motor modelava o par por gosto (chutei que
acafrao nao vai em citrico). A tabela que o operador levantou mostra o
criterio de verdade:
  · hidrossoluvel  -> decoccao   (tongkat, tribulus, sarsaparilla, ginseng)
  · lipossoluvel   -> LEITE      (ashwagandha, muira puama)
  · mucilagem      -> molho FRIO (fenugreek, o classico `methi water`)
  · folha          -> infusao    (ginkgo, que entra por ultimo)
  · L-DOPA         -> torra      (mucuna, o `Nescafe` de mucuna)
Errar o metodo nao e' mau gosto: e' preparar de um jeito que NAO EXTRAI
nada. A lente `RA6` cobra isso, e os metodos ERRADOS vivem no pool de
proposito, para o controle negativo do autoteste ter o que plantar.
⚠️ DIVIDA: a regra do acafrao veio cortada no print (*"nunca na panela — ver
a regra abaixo"*). Adotei o conservador e quimicamente correto: bloom em
leite MORNO, nunca fervido — a crocina sai na agua e o safranal e' volatil.
Se a regra dele disser outra coisa, e' uma linha.
"""
import argparse
import collections
import json
import os
import random
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import short_comum as sc  # noqa: E402

APP = TITULO = "AGENTE RARO 16"
SUBTITULO = ("2 takes de 8s · so' o preparo na mesa, sem ninguem em quadro · "
             "o raro + o metodo certo de extrair, e a tribo que o tomava")
SLUG = "raro-16"
SEXOS = ("homem",)
CENAS_UI = ["1 · A FALHA + A TRIBO", "2 · A RECEITA + CTA"]
LEDGER = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      ".raro-16-ledger.json")

# ⛔ `recipe`, nao `gelatin`. Ordem do operador, e e' o que separa esta rota.
KEYWORD_UI = True
KEYWORD_NATIVA = "recipe"

TETO_FALA = {1: 25, 2: 25}
PISO_FALA = {1: 12, 2: 12}

# ⛔ Sem apelido de orgao: este angulo nao mostra corpo e nao nomeia orgao. A
# falha entra pelo VERBO (`going soft`), que e' o que o CT2 cobra.
NUCLEO = ()

BANIDOS_CTA = {"book": "quebra a automacao de DM",
               "yes": "quebra a automacao de DM",
               "gelatin": "esta rota nao usa gelatina"}
BANIDOS_IMAGE = {}
BANIDOS_TAKE = {}
BANIDOS_BLOCO = {}

ETNIA = {"joe": "white American", "marcus": "Black American",
         "ray": "white American", "chuck": "white American",
         "matt": "white American"}

IDADES = (54, 58, 61, 63, 66, 68, 71)


# ===========================================================================
# ⭐⭐ OS RAROS — o pool canonico do parque, com a TRIBO acrescentada
# ===========================================================================
# ⛔ `nome` e `aposto` sao COPIA LITERAL do pool que ja' roda no BOTICA, no
# CHA, no DUPLA, no PLACA e no TRIO. String validada se copia, nunca se
# redigita — e assim uma correcao de aposto vale para o parque inteiro.
#
# ⭐ O campo `tribo` e' novo e e' o que este motor acrescenta. Ele NAO afirma
# que o povo era viril: ele diz que o povo TOMAVA aquilo por geracoes, e a
# virilidade vem da vizinhanca com o hook, que fala da falha. A diferenca
# importa — a primeira formulacao e' alegacao historica, a segunda e'
# associacao, e e' a associacao que o operador pediu.
#
# ⚠️ `interno` nunca entra no prompt nem na fala: existe so' para producao.
RAROS = [
    {"id": "maca", "nome": "maca root", "interno": "Lepidium meyenii",
     "aposto": "that Andean root from Peru",
     "tribo": "the Andean men",
     "certo": ['leite_quente'],
     "falso": ['agua_fria'],
     "inteiro": "two whole dried maca roots, pale and knobbed",
     "img": "a small dish of pale yellow maca powder"},
    {"id": "tongkat", "nome": "tongkat ali", "interno": "Eurycoma longifolia",
     "aposto": "a root from the forests of Southeast Asia",
     "tribo": "the forest villages of Borneo",
     "certo": ['decoccao_longa'],
     "falso": ['agua_fria', 'batida_crua'],
     "inteiro": "a few long pieces of whole tongkat ali root",
     "img": "a small dish of coarse light-brown root shavings"},
    {"id": "tribulus", "nome": "tribulus", "interno": "Tribulus terrestris",
     "aposto": "that spiny fruit that grows along the ground",
     "tribo": "old India",
     "certo": ['decoccao'],
     "falso": ['infusao'],
     "inteiro": "a small heap of whole dried tribulus pods",
     "img": "a small dish of dried spiny seed pods"},
    {"id": "epimedium", "nome": "epimedium", "interno": "Epimedium spp.",
     "aposto": "the herb they call horny goat weed",
     "tribo": "China's mountain herders",
     "certo": ['decoccao_curta', 'vinho'],
     "falso": ['fervura_longa'],
     "inteiro": "a loose bundle of whole dried epimedium leaves",
     "img": "a small dish of dried heart-shaped leaves"},
    {"id": "horny_goat", "nome": "horny goat weed", "interno": "Epimedium spp.",
     "aposto": "the herb goat farmers stumbled onto",
     "tribo": "China's mountain herders",
     "certo": ['decoccao_curta', 'vinho'],
     "falso": ['fervura_longa'],
     "inteiro": "a loose bundle of whole dried horny goat weed leaves",
     "img": "a small dish of dried heart-shaped leaves"},
    {"id": "fenogrego", "nome": "fenugreek",
     "interno": "Trigonella foenum-graecum",
     "aposto": "the golden seed of the Mediterranean",
     "tribo": "the old Mediterranean",
     "certo": ['molho_frio', 'torra_moagem'],
     "falso": [],
     "inteiro": "a handful of whole golden fenugreek seeds",
     "img": "a small dish of hard golden-brown seeds"},
    {"id": "muirapuama", "nome": "muira puama",
     "interno": "Ptychopetalum olacoides",
     "aposto": "an Amazon root known for generations",
     "tribo": "the Amazon river men",
     "certo": ['leite_integral', 'decoccao_longa'],
     "falso": ['infusao', 'agua_fria'],
     "inteiro": "two long strips of whole muira puama bark",
     "img": "a small dish of chipped pale bark and root"},
    {"id": "ginkgo", "nome": "ginkgo", "interno": "Ginkgo biloba",
     "aposto": "the leaf off that ancient Chinese tree",
     "tribo": "China's temple keepers",
     "certo": ['infusao'],
     "falso": ['decoccao_longa'],
     "inteiro": "a spread of whole dried ginkgo leaves",
     "img": "a small dish of dried fan-shaped leaves"},
    {"id": "mucuna", "nome": "mucuna", "interno": "Mucuna pruriens",
     "aposto": "the famous velvet bean of the tropics",
     "tribo": "the villages of old India",
     "certo": ['torra_moagem'],
     "falso": ['agua_fria'],
     "inteiro": "a handful of whole dark mucuna beans",
     "img": "a small dish of dark glossy beans"},
    {"id": "salsaparrilha", "nome": "sarsaparilla", "interno": "Smilax spp.",
     "aposto": "a vine root native to the Americas",
     "tribo": "the native Americas",
     "certo": ['decoccao'],
     "falso": ['infusao'],
     "inteiro": "a bundle of whole twisted sarsaparilla root",
     "img": "a small dish of dried twisted root pieces"},
    {"id": "ginseng", "nome": "panax ginseng", "interno": "Panax ginseng",
     "aposto": "the famous Korean root",
     "tribo": "Korea's mountain villages",
     "certo": ['decoccao_longa', 'sopa'],
     "falso": ['infusao'],
     "inteiro": "one whole pale ginseng root with its long legs",
     "img": "a small dish of pale twisted ginseng root"},
    {"id": "acafrao", "nome": "saffron", "interno": "Crocus sativus",
     "aposto": "the rare red spice from the crocus flower",
     "tribo": "the Persian spice roads",
     "certo": ['bloom_morno'],
     "falso": ['fervura_longa', 'gordura_pura'],
     "inteiro": "a pinch of whole dark red saffron threads",
     "img": "a small dish of deep red saffron threads"},
    {"id": "catuaba", "nome": "catuaba",
     "interno": "Trichilia catigua (geralmente)",
     "aposto": "the bark traditionally used in Brazil",
     "tribo": "the Tupi of Brazil",
     "certo": ['decoccao_curta', 'vinho'],
     "falso": ['agua_fria'],
     "inteiro": "several curled strips of whole catuaba bark",
     "img": "a small dish of reddish bark shavings"},
    {"id": "ashwagandha", "nome": "ashwagandha", "interno": "Withania somnifera",
     "aposto": "that ancient root used in Indian medicine",
     "tribo": "old India",
     "certo": ['leite_fervido'],
     "falso": ['fervura_longa'],
     "inteiro": "two whole beige ashwagandha roots",
     "img": "a small dish of beige ashwagandha root and light brown powder"},
]


# ===========================================================================
# ⭐ OS VEICULOS — como a pessoa REALMENTE toma aquele po'
# ===========================================================================
# ⛔ Nao e' pool de bebida bonita: cada entrada e' um jeito que existe de tomar
# po' de raiz na cozinha. `fam` e' o que a lente `RA6` usa para barrar o par
# impossivel — po' amargo de raiz nao vai em suco citrico, e fio de acafrao
# nao vira shake de proteina.
PREPAROS = [
    {"id": "decoccao_longa", "curto": "decoccao longa (20-30 min)",
     "fala": "simmered thirty minutes",
     "img": "a small steel pot on a trivet with dark liquid still moving in it",
     "t2": "the pot is off the heat and the liquid has gone still"},
    {"id": "decoccao", "curto": "decoccao",
     "fala": "simmered into a decoction",
     "img": "a small enamel pot of dark liquid beside a strainer",
     "t2": "the liquid has been poured off through the strainer"},
    {"id": "decoccao_curta", "curto": "decoccao curta (10-15 min)",
     "fala": "simmered fifteen minutes",
     "img": "a small covered pot with a little steam escaping at the lid",
     "t2": "the lid is off and the steam has thinned"},
    {"id": "infusao", "curto": "infusao (folha por ultimo)",
     "fala": "steeped like tea, leaf last",
     "img": "a clear glass cup of pale amber infusion with leaves suspended",
     "t2": "the leaves have sunk and the cup has cleared"},
    {"id": "molho_frio", "curto": "molho frio de 8-10h",
     "fala": "soaked overnight in cold water",
     "img": "a lidded glass jar of cold water with the seeds swollen at the "
            "bottom and a soft gel around them",
     "t2": "the jar is open and the gel has drawn into long threads"},
    {"id": "leite_fervido", "curto": "fervido no leite",
     "fala": "simmered in whole milk",
     "img": "a small milk pan of warm milk gone pale tan, a thin skin forming",
     "t2": "the pan is off the heat and the skin has set on top"},
    {"id": "leite_quente", "curto": "leite quente / batida cremosa",
     "fala": "whisked into hot milk",
     "img": "a tall glass of hot milk gone creamy and pale, a whisk resting in it",
     "t2": "the whisk is out and the foam is settling"},
    {"id": "leite_integral", "curto": "leite integral (gordura)",
     "fala": "stirred into whole milk",
     "img": "a short glass of whole milk with the powder folded through it",
     "t2": "the powder has gone in and the surface is smooth"},
    {"id": "torra_moagem", "curto": "molho, torra e moagem",
     "fala": "soaked, roasted and ground",
     "img": "a shallow pan of dark roasted beans beside a hand grinder with "
            "fresh grounds under it",
     "t2": "the grinder is open and the grounds are heaped in the tray"},
    {"id": "bloom_morno", "curto": "bloom em liquido morno",
     "fala": "bloomed in warm milk",
     "img": "a small bowl of warm milk turning deep gold around the threads",
     "t2": "the colour has spread through the whole bowl"},
    {"id": "vinho", "curto": "maceracao em vinho",
     "fala": "macerated in wine",
     "img": "a corked glass bottle of dark wine with the pieces suspended in it",
     "t2": "the bottle is corked again and the pieces have settled low"},
    {"id": "sopa", "curto": "raiz na sopa",
     "fala": "cooked into a broth",
     "img": "a wide clay bowl of pale broth with the whole root standing in it",
     "t2": "a spoon rests in the bowl and the broth has stopped moving"},
    {"id": "agua_fria", "curto": "agua fria pura",
     "fala": "in a glass of cold water",
     "img": "a tall glass of plain cold water",
     "t2": "the water is still and clear"},
    {"id": "batida_crua", "curto": "batida crua",
     "fala": "blended raw",
     "img": "a blender jug with raw pieces and water in it",
     "t2": "the jug is set down and the pieces have not broken up"},
    {"id": "fervura_longa", "curto": "fervura longa",
     "fala": "boiled hard for a long time",
     "img": "a pot at a hard rolling boil, steam thick above it",
     "t2": "the pot is off the heat and the boil has collapsed"},
    {"id": "gordura_pura", "curto": "gordura pura",
     "fala": "in warm oil",
     "img": "a small dish of warm oil with the threads sitting in it",
     "t2": "the oil has gone faintly coloured"},
]

# ⛔⛔ OS METODOS ERRADOS EXISTEM NO POOL DE PROPOSITO, e NUNCA sao sorteados
# como preparo do video. Eles moram aqui para a lente `RA6` ter contra o que
# comparar e para o `--autoteste` conseguir PLANTAR o defeito e provar que ela
# acusa. Pool sem o errado dentro e' lente sem controle negativo.
ERRADOS = {"agua_fria", "batida_crua", "fervura_longa", "gordura_pura"}


# ===========================================================================
# ⭐ OS AMBIENTES — generosos por ordem do operador (*"pra nao ficar monotono"*)
# ===========================================================================
# ⛔ Cada entrada carrega superficie + fundo + luz + audio JUNTOS. Separar em
# quatro eixos daria mais combinacao e menos nexo — e' a licao do VICK 16, onde
# cem elementos distintos viraram cem elementos soltos.
AMBIENTES = [
    {"id": "tabua_rustica", "curto": "tabua de madeira rustica",
     "amb": "a home kitchen with a wide rustic acacia wood table filling the "
            "frame, small white flowers and dried red chillies arranged along "
            "the far edge",
     "sup": "the warm honey-brown wood, grain running left to right",
     "luz": "soft daylight from a window out of frame on the left, warm and even",
     "audio": "a quiet kitchen, a spoon touching glass"},
    {"id": "bancada_marmore", "curto": "bancada de marmore branco",
     "amb": "a bright kitchen with a white marble counter, grey veining "
            "running across, a folded linen cloth at the back edge",
     "sup": "the cold polished marble",
     "luz": "clean daylight from the right, soft shadows, neutral white balance",
     "audio": "a quiet room, a glass set down on stone"},
    {"id": "mesa_pinho", "curto": "mesa de pinho clara",
     "amb": "a plain kitchen with a pale pine table, a woven straw mat under "
            "the pieces and a clay jug at the back",
     "sup": "the light pine boards with visible knots",
     "luz": "warm afternoon light coming in low from the left",
     "audio": "a quiet house, birds faint outside"},
    {"id": "granito_escuro", "curto": "granito escuro",
     "amb": "a modern kitchen with a dark speckled granite counter, a black "
            "tiled backsplash behind and a cutting board at the far left",
     "sup": "the dark granite, faint speckles catching the light",
     "luz": "cool overhead light with a soft pool on the counter",
     "audio": "a quiet kitchen, a low fridge hum"},
    {"id": "azulejo_portugues", "curto": "bancada com azulejo",
     "amb": "a warm kitchen with a tiled counter, blue and white patterned "
            "tiles on the wall behind and a hanging bunch of dried herbs",
     "sup": "the glazed tile top with grout lines crossing it",
     "luz": "warm side light, the tiles catching a soft sheen",
     "audio": "a quiet kitchen, a distant kettle"},
    {"id": "varanda_manha", "curto": "varanda de manha",
     "amb": "an outdoor porch table of weathered grey wood, green leaves and "
            "a low wooden railing behind, morning garden beyond",
     "sup": "the sun-bleached grey planks",
     "luz": "early morning sun coming in low and warm from the right",
     "audio": "outdoor morning air, birds and a light breeze"},
    {"id": "mesa_ferro", "curto": "mesa de ferro no jardim",
     "amb": "a small round garden table with a black iron top, potted green "
            "plants close behind and gravel out of focus beyond",
     "sup": "the matte black iron, a few water spots on it",
     "luz": "bright overcast daylight, soft and shadowless",
     "audio": "a garden, leaves moving and far traffic"},
    {"id": "balcao_madeira", "curto": "balcao de bar de casa",
     "amb": "a home bar counter of dark stained wood, shelved bottles blurred "
            "in the background and a folded bar towel to the side",
     "sup": "the dark polished wood with a worn edge",
     "luz": "warm low light from a lamp above and to the left",
     "audio": "a quiet room, glass on wood"},
    {"id": "cozinha_campo", "curto": "cozinha de sitio",
     "amb": "a rural kitchen with a thick worn butcher block table, an enamel "
            "pot and a woven basket of roots at the back",
     "sup": "the scarred butcher block, cut marks across it",
     "luz": "daylight from a small high window, warm and directional",
     "audio": "a quiet country kitchen, a wooden chair creak"},
    {"id": "aco_inox", "curto": "bancada de inox",
     "amb": "a clean kitchen with a brushed stainless steel counter, a plain "
            "white wall behind and a steel rail with hanging utensils",
     "sup": "the brushed steel, faint lines running lengthwise",
     "luz": "even cool daylight, low contrast",
     "audio": "a quiet kitchen, metal touching metal"},
    {"id": "mesa_vidro", "curto": "mesa de vidro",
     "amb": "a bright room with a clear glass table top, a pale rug visible "
            "through it and a green plant behind",
     "sup": "the clear glass, the pieces reflected faintly in it",
     "luz": "bright diffuse daylight from a large window",
     "audio": "a quiet room, glass on glass"},
    {"id": "tabua_escura", "curto": "tabua de nogueira",
     "amb": "a kitchen with a dark walnut board across the frame, a linen "
            "runner along the back and a small brass scale behind",
     "sup": "the deep brown walnut with an oiled sheen",
     "luz": "warm directional light from the upper left, soft falloff",
     "audio": "a quiet kitchen, a wooden spoon set down"},
    {"id": "peitoril", "curto": "peitoril de janela",
     "amb": "a wide window sill of painted white wood, the garden out of "
            "focus through the glass behind",
     "sup": "the painted white sill, small chips in the paint",
     "luz": "backlit daylight through the window, the pieces rimmed with light",
     "audio": "a quiet room, faint outdoor air"},
    {"id": "mesa_ceramica", "curto": "mesa de ceramica",
     "amb": "a small kitchen table topped with hand-painted ceramic tiles, a "
            "clay bowl of whole roots at the back edge",
     "sup": "the glazed ceramic, one tile slightly off-level",
     "luz": "warm lamp light from directly above",
     "audio": "a quiet kitchen, ceramic touching ceramic"},
]


# ===========================================================================
# ⭐ AS CAMERAS — o angulo, e SO' o angulo
# ===========================================================================
# ⛔⛔ NENHUMA DELAS NOMEIA APARELHO. Escrever `phone`, `camera` ou `filming`
# num prompt de imagem nao instrui enquadramento: instrui CONTEUDO, e o gerador
# DESENHA o aparelho. O repo pagou um lote inteiro por isso no VICK 16.
# ⛔ E nao se escreve `no phone in frame`: negacao INJETA o token.
CAMERAS = [
    {"id": "prumo", "curto": "a prumo",
     "txt": "Straight overhead at ninety degrees, looking directly down at the "
            "surface, everything flat in frame"},
    {"id": "quase_prumo", "curto": "quase a prumo",
     "txt": "Steep overhead at about seventy degrees, tipped just enough that "
            "the pieces keep their height"},
    {"id": "tres_quartos", "curto": "tres quartos",
     "txt": "Angled at about forty-five degrees above the surface, close in, "
            "the pieces reading in depth"},
    {"id": "rasante", "curto": "rasante",
     "txt": "Low and level with the surface, almost at table height, the "
            "pieces standing against the background"},
    {"id": "macro", "curto": "macro no ingrediente",
     "txt": "Very close macro on the ingredient, shallow depth of field, the "
            "background falling soft"},
    {"id": "lateral", "curto": "lateral",
     "txt": "From the side at surface height, the pieces in profile across the "
            "frame"},
    {"id": "ombro", "curto": "por cima do ombro",
     "txt": "From just behind and above the hands, looking down the forearms "
            "onto the surface"},
    {"id": "diagonal", "curto": "diagonal",
     "txt": "From an upper corner at about sixty degrees, the surface running "
            "diagonally through the frame"},
    {"id": "frontal_alto", "curto": "frontal alto",
     "txt": "Straight on from the front, a little above the pieces, the "
            "background clean behind them"},
    {"id": "contra_luz", "curto": "contra a luz",
     "txt": "From the side with the light behind the pieces, their edges rimmed "
            "and the surface darker in front"},
    {"id": "deriva", "curto": "com deriva lenta",
     "txt": "Just above the surface with a slow steady drift to the right, the "
            "pieces staying centred"},
    {"id": "aproxima", "curto": "aproximacao lenta",
     "txt": "Starting wide on the whole surface and creeping in slowly toward "
            "the ingredient"},
]


# ===========================================================================
# ⭐ AS ACOES — a manipulacao da receita
# ===========================================================================
ACOES = [
    {"id": "despeja_po", "curto": "despeja o po",
     "t1": "one hand tips the small dish and a thin column of powder falls "
           "into it",
     "t2": "the powder has settled and the surface has gone still"},
    {"id": "mexe_colher", "curto": "mexe com a colher",
     "t1": "one hand turns a long spoon slowly through it",
     "t2": "the spoon rests against the rim and the swirl is slowing"},
    {"id": "esmaga_raiz", "curto": "esmaga a raiz",
     "t1": "both hands press a small pestle down onto the whole root in a "
           "shallow stone bowl",
     "t2": "the root is broken into coarse pieces and the pestle lies beside it"},
    {"id": "peneira", "curto": "peneira o po",
     "t1": "one hand taps a small sieve and fine powder falls through onto the "
           "surface",
     "t2": "a low even cone of powder sits under the sieve"},
    {"id": "ergue_copo", "curto": "ergue o copo",
     "t1": "one hand lifts it a few inches off the surface and holds it there",
     "t2": "it is back down and the hand has let go"},
    {"id": "serve_de_jarra", "curto": "serve da jarra",
     "t1": "one hand tips a small jug and a steady stream pours into it",
     "t2": "the jug is upright again and it is full to two thirds"},
    {"id": "pinca_fios", "curto": "pinca os fios",
     "t1": "two fingers lift a pinch of the ingredient and hold it just above "
           "glass",
     "t2": "the pinch has been dropped in and the fingers are open and empty"},
    {"id": "empurra_bowl", "curto": "empurra a tigela",
     "t1": "one hand slides the small dish of powder across the surface toward "
           "it",
     "t2": "the dish sits beside it and the hand rests flat"},
    {"id": "cobre_e_espera", "curto": "tampa e espera",
     "t1": "one hand lays a small saucer over the top of it",
     "t2": "the saucer is lifted away and a little steam comes off"},
    {"id": "alinha_pecas", "curto": "alinha as pecas",
     "t1": "both hands set the whole ingredient and the dish of powder side by "
           "side in front of it",
     "t2": "the pieces are lined up and both hands have withdrawn to the edge"},
]


# ===========================================================================
# ⭐ AS MAOS — a unica ancora, ja' que nao ha' rosto
# ===========================================================================
# ⛔ Entrada nova difere em pelo menos TRES eixos, nunca so' na cor. Contar
# entradas nao e' contar variacao — e' a §15 das licoes.
MAOS = [
    {"id": "veias_altas", "curto": "veias altas, nos quadrados",
     "txt": "high ropey veins across the backs, thick square knuckles, short "
            "trimmed nails"},
    {"id": "cicatriz_polegar", "curto": "cicatriz no polegar",
     "txt": "a pale old scar across the base of the thumb, narrow knuckles, "
            "flat ridged nails"},
    {"id": "manchas_sol", "curto": "manchas solares",
     "txt": "dark sun spots scattered over the backs, heavy tendons, nails cut "
            "square and short"},
    {"id": "calo_palma", "curto": "calo na palma",
     "txt": "a hard yellow callus along the palm edge, broad flat knuckles, "
            "one chipped nail"},
    {"id": "juntas_inchadas", "curto": "juntas inchadas",
     "txt": "swollen arthritic knuckles on both middle fingers, raised veins "
            "branching over the metacarpals, wide flat nails"},
    {"id": "mindinho_torto", "curto": "mindinho torto",
     "txt": "a crooked little finger set from an old break, bony knuckles, "
            "nails worn short"},
    {"id": "gretas_secas", "curto": "gretas secas",
     "txt": "cracked dry creases across the joints, deep tendon cords, thick "
            "pale nails"},
    {"id": "queimadura", "curto": "queimadura antiga",
     "txt": "a shiny burn mark on the back of one hand, knobbed knuckles, "
            "short blunt nails"},
    {"id": "pelo_antebraco", "curto": "pelo grisalho no antebraco",
     "txt": "coarse grey hair over the forearms, flat wide knuckles, nails "
            "filed round"},
    {"id": "tinta_unha", "curto": "tinta sob a unha",
     "txt": "a dark stain under one thumbnail, heavy raised veins, blunt "
            "square nails"},
]


# ===========================================================================
# A COPY — o arco que o operador ditou
# ===========================================================================
# ⛔ O CTA e' `Comment recipe`, e a constante existe para o campo de keyword do
# painel poder reescrever a palavra sem recompilar nada.
CTA_LITERAL = "Comment recipe"

# ⭐ A FALHA. Ela e' o que o CT2 cobra e e' o que faz o espectador se
# reconhecer. ⛔ Sem apelido de orgao: este angulo nao mostra corpo nenhum, e
# nomear o orgao sobre uma mesa de cozinha e' o drifting invertido.
# ⭐⭐ A FALHA — SEIS FORMAS, nao uma forma com N sinonimos.
# ⛔ O campo `forma` existe para o autoteste MEDIR diversidade de forma, e nao
# so' contar entradas. Contar entradas foi exatamente como este pool nasceu
# errado: oito falas, uma forma.
# ⚠️ A `pergunta` fica no pool com peso igual, mesmo tendo medido pior na
# fonte (4,0 contra 20,5 da exclusao): o lote existe para o campo responder, e
# tirar a forma pior antes de medir seria decidir no lugar do campo.
FALHAS = [
    # -- PERGUNTA (mediu 4,0 na fonte) -----------------------------------
    {"id": "pg1", "forma": "pergunta",
     "txt": "Tired of going soft when it matters?"},
    {"id": "pg2", "forma": "pergunta",
     "txt": "Went soft again last night?"},
    {"id": "pg3", "forma": "pergunta",
     "txt": "Going soft halfway through, every time?"},
    {"id": "pg4", "forma": "pergunta",
     "txt": "How many nights has it gone soft on you?"},
    # -- EXCLUSAO (mediu 20,5 — a melhor da fonte) -----------------------
    {"id": "ex1", "forma": "exclusao",
     "txt": "If you are single, do not go looking for this one."},
    {"id": "ex2", "forma": "exclusao",
     "txt": "If you never go soft, this is not for you."},
    {"id": "ex3", "forma": "exclusao",
     "txt": "Married men only, and even then, go easy."},
    {"id": "ex4", "forma": "exclusao",
     "txt": "Under forty? Close this. You do not need it yet."},
    # -- CONFISSAO (8,1) -------------------------------------------------
    {"id": "cf1", "forma": "confissao",
     "txt": "I went soft for two straight years and said nothing."},
    {"id": "cf2", "forma": "confissao",
     "txt": "I stopped reaching for her because I knew how it would end."},
    {"id": "cf3", "forma": "confissao",
     "txt": "I blamed my age for going soft. I was wrong."},
    {"id": "cf4", "forma": "confissao",
     "txt": "I faked being tired for years so she would not see me go soft."},
    # -- IDADE (11,8 / 7,5 / 5,6) ----------------------------------------
    {"id": "id1", "forma": "idade",
     "txt": "At sixty-three I stopped going soft, and not with pills."},
    {"id": "id2", "forma": "idade",
     "txt": "Sixty-eight, and my wife stopped asking what is wrong."},
    {"id": "id3", "forma": "idade",
     "txt": "Fifty-nine was the year it started. Sixty was the year it stopped."},
    # -- ACUSACAO --------------------------------------------------------
    {"id": "ac1", "forma": "acusacao",
     "txt": "Over fifty and still doing nothing about going soft?"},
    {"id": "ac2", "forma": "acusacao",
     "txt": "You went soft again and you are still blaming the week you had."},
    {"id": "ac3", "forma": "acusacao",
     "txt": "Every man your age goes soft and nobody says it out loud."},
    # -- CONSTATACAO / AVISO ---------------------------------------------
    {"id": "cn1", "forma": "constatacao",
     "txt": "Going soft is not what age does to you. It is what you drink."},
    {"id": "cn2", "forma": "constatacao",
     "txt": "There is a reason your grandfather never went soft."},
    {"id": "cn3", "forma": "constatacao",
     "txt": "Men go soft in this country and nowhere else does it this fast."},
    {"id": "cn4", "forma": "constatacao",
     "txt": "Watch this before you go soft on her again."},
]

# ⭐ O QUALIFICADOR VIRA POOL. Era a palavra `bizarre` CRAVADA na frase, entao
# os quatorze raros, os dezesseis preparos e os quatorze ambientes produziam
# videos que diziam todos a mesma palavra no mesmo lugar.
ADJETIVOS = [
    "bizarre", "strange", "backwards", "old", "forgotten", "ugly",
    "unglamorous", "crude", "stubborn", "cheap", "quiet", "unlikely",
    "primitive", "odd",
]

# ⭐ A PONTE ate' a tribo. `%s` e' o adjetivo, `%s` e' a tribo.
PONTES = [
    # ⛔ AS CURTAS EXISTEM PARA AS FORMAS LONGAS DE HOOK CABEREM. Medido: com
    # so' as pontes de 10 palavras, `pergunta` ficava em 98% dos videos porque
    # era a unica forma curta o bastante — as outras cinco estavam no pool e
    # mortas. Ponte curta nao e' economia de estilo, e' o que mantem o eixo
    # vivo.
    {"id": "b0", "txt": "A %s trick from %s."},
    {"id": "b0b", "txt": "%s did this. %s as it sounds.", "inv": True},
    {"id": "b0c", "txt": "%s knew it. %s, but it works.", "inv": True},
    {"id": "b1", "txt": "This %s method comes from %s."},
    # ⚠️ `X is where` quebrava concordancia com tribo PLURAL (`the villages of
    # old India IS where`). Com o ponto no meio, a tribo vira sujeito de uma
    # frase propria e o verbo some.
    {"id": "b2", "txt": "%s. That is where this %s trick comes from.",
     "inv": True},
    {"id": "b3", "txt": "It is a %s habit borrowed from %s."},
    {"id": "b4", "txt": "%s did this for centuries, %s as it looks.",
     "inv": True},
    {"id": "b5", "txt": "This %s routine is older than your country: %s."},
    # ⚠️ `in %s` pedia um LUGAR e recebia um POVO (`Nothing primitive about it
    # in China's temple keepers`). `where it comes from:` aceita os dois.
    {"id": "b6", "txt": "Nothing %s about it where it comes from: %s."},
]

# ⭐⭐ O TERCEIRO BEAT tem DUAS FUNCOES, e essa era a que faltava. O operador:
# *"por que vc nao alternou «the pharmacy will never bring this one up» por
# «your wife won't be able to keep up»?"*
#  · VILAO        — quem perde com voce saber (a farmacia, o balcao, o medico)
#  · CONSEQUENCIA — o que acontece com voce depois (ela nao acompanha)
# ⛔ Sao promessas OPOSTAS: o vilao explica por que voce nunca ouviu falar; a
# consequencia vende o depois. Um pool so' de vilao entrega metade do arco.
FECHOS = [
    # -- VILAO -----------------------------------------------------------
    {"id": "v0", "fam": "vilao", "txt": "No pharmacy sells it."},
    {"id": "v0b", "fam": "vilao", "txt": "There is no pill version."},
    {"id": "v1", "fam": "vilao",
     "txt": "The pharmacy will never bring this one up."},
    {"id": "v2", "fam": "vilao",
     "txt": "No pharmacy makes a cent when you do this."},
    {"id": "v3", "fam": "vilao",
     "txt": "This is the one they leave off the shelf."},
    {"id": "v4", "fam": "vilao",
     "txt": "The drug counter would rather you never heard it."},
    {"id": "v5", "fam": "vilao",
     "txt": "Nobody selling pills wants this getting around."},
    {"id": "v6", "fam": "vilao",
     "txt": "Your doctor has ten minutes and none of them for this."},
    {"id": "v7", "fam": "vilao",
     "txt": "There is no patent on it, so nobody advertises it."},
    {"id": "v8", "fam": "vilao",
     "txt": "It costs almost nothing, which is exactly the problem."},
    # -- CONSEQUENCIA ----------------------------------------------------
    {"id": "q0", "fam": "consequencia", "txt": "She will notice."},
    {"id": "q0b", "fam": "consequencia", "txt": "Go easy on her."},
    {"id": "q1", "fam": "consequencia",
     "txt": "Your wife will not be able to keep up."},
    {"id": "q2", "fam": "consequencia",
     "txt": "She is going to ask you what changed."},
    {"id": "q3", "fam": "consequencia",
     "txt": "Do not start this on a weeknight."},
    {"id": "q4", "fam": "consequencia",
     "txt": "She will notice before you say a word."},
    {"id": "q5", "fam": "consequencia",
     "txt": "You will stop planning your nights around it."},
    {"id": "q6", "fam": "consequencia",
     "txt": "She will be the one asking to slow down."},
    {"id": "q7", "fam": "consequencia",
     "txt": "You will be the one turning the lamp off last."},
    {"id": "q8", "fam": "consequencia",
     "txt": "Nobody has to know why you sleep so well now."},
]

# ⭐ A PROVA do take 2, antes do CTA. Sem numero, sem prazo e sem promessa de
# cura: o que sobra e' o custo, a facilidade e a ausencia de receita medica.
# ⛔ Ela e' OPCIONAL por orcamento — ver o comentario em `_falas`.
PROVAS = [
    {"id": "r1", "txt": "Every morning, nothing else."},
    {"id": "r2", "txt": "One glass a day is the whole thing."},
    {"id": "r3", "txt": "Two minutes, and it costs almost nothing."},
    {"id": "r4", "txt": "You already have most of it at home."},
    {"id": "r5", "txt": "No prescription, no pharmacy, no bill."},
    {"id": "r6", "txt": "Cheaper than a coffee."},
    {"id": "r7", "txt": "Nobody has to know you are doing it."},
    {"id": "r8", "txt": "It keeps a week in the fridge."},
    {"id": "r9", "txt": "Takes longer to read than to make."},
    {"id": "r10", "txt": "One pot, one spoon, that is it."},
]

CTAS = [
    # ⛔ A VIRGULA DEPOIS DA KEYWORD nao e' estilo: sem a micro-pausa o Veo
    # emenda a palavra na frase e narra `gelatine`. O `lint_cta_literal` cobra
    # o literal COM ela, e o `medir_copy16` conta isso como CT1.
    # ⛔ E nenhum deles pede FOLLOW: o CT8 caiu por FATO — a DM sai igual, o
    # portao nunca existiu, e follow na fala so' gasta palavra do teto.
    {"id": "c0", "txt": "%s, and it goes to your messages."},
    {"id": "c0b", "txt": "%s, and I send it to your messages."},
    # ⚠️ `the recipe` sairia com a keyword `recipe` e a palavra apareceria duas
    # vezes na mesma frase.
    {"id": "c0c", "txt": "%s, and the whole thing goes to your messages."},
    {"id": "c1", "txt": "%s, and the full step by step goes to your messages."},
    {"id": "c2", "txt": "%s, and I send the exact measures to your messages."},
    {"id": "c3", "txt": "%s, and the measures land in your messages."},
    {"id": "c4", "txt": "%s, and I will send it over to your messages."},
    {"id": "c5", "txt": "%s, and check your messages."},
]

EIXOS_LEDGER = ("ambiente", "camera", "acao", "raro", "preparo", "maos",
                "falha", "farmacia", "prova", "cta")


def _chave(x):
    return x["id"] if isinstance(x, dict) else str(x)


def _carregar_ledger():
    if not os.path.exists(LEDGER):
        return {}
    try:
        with open(LEDGER, encoding="utf-8") as f:
            return json.load(f)
    except Exception:  # noqa: BLE001
        return {}


def _anotar(ledger, spec):
    d = ledger.setdefault(spec["pagina"], {})
    for eixo in EIXOS_LEDGER:
        if eixo in spec and spec[eixo]:
            d.setdefault(eixo, []).append(_chave(spec[eixo]))
            d[eixo] = d[eixo][-40:]


def _gravar_ledger(ledger, spec=None):
    if spec:
        _anotar(ledger, spec)
    try:
        with open(LEDGER, "w", encoding="utf-8") as f:
            json.dump(ledger, f, indent=1)
    except Exception:  # noqa: BLE001
        pass


def _fresco(pool, usados, rng):
    livres = [x for x in pool if _chave(x) not in usados]
    return rng.choice(livres or pool)


def _por_id(pool, valor, chave="id"):
    if isinstance(valor, dict):
        return valor
    for x in pool:
        if x.get(chave) == valor:
            return x
    return None


def _palavras(s):
    return len(re.findall(r"[A-Za-z']+", s or ""))


def _frases(t):
    """Maiuscula no inicio e depois de cada ponto."""
    return re.sub(r"(^|[.!?] )([a-z])",
                  lambda m: m.group(1) + m.group(2).upper(), t)


def _cap(s):
    return s[0].upper() + s[1:] if s else s


def preparos_para(raro):
    """Os metodos que EXTRAEM aquele raro.

    ⛔ Lista de INCLUSAO, e nao de exclusao: o campo `certo` de cada raro sai
    da tabela de quimica do operador, entao um raro so' e' preparado do jeito
    que funciona. ⚠️ Isso reduz combinacao de proposito — vinte metodos vezes
    quatorze raros dariam 224 pares, e a maioria seria preparo que nao extrai
    nada. Combinacao que nao existe no mundo nao e' variedade, e' ruido.
    """
    return [p for p in PREPAROS if p["id"] in raro["certo"]] or PREPAROS


def _falas(spec, rng, quais=(0, 1)):
    """As duas falas, cada uma um PAR sorteado entre as combinacoes VIAVEIS.

    ⛔ Nunca em cascata (escolher o primeiro beat e depois procurar um que
    caiba): isso colapsa a variancia — medido no VICK 16, onde o take 2 saiu
    com UMA fala em 400 videos.
    """
    f = dict(enumerate(spec.get("falas", ["", ""])))
    raro = spec["raro"]
    if 0 in quais:
        # ⭐ A TRIBO SAI DO RARO SORTEADO, nunca de um pool proprio: sortear
        # povo por fora poria "as tribos andinas" num video de acafrao persa.
        # ⭐⭐ E o ADJETIVO e a PONTE tambem sao sorteados — antes a frase era
        # `This bizarre method comes from X`, cravada, e os quatorze raros
        # diziam todos a mesma palavra no mesmo lugar.
        adj = rng.choice(ADJETIVOS)
        # ⛔ A CAPITALIZACAO E' APLICADA DEPOIS DE MONTAR, e nao escrita nas
        # entradas: nas pontes `inv` quem abre a frase e' a TRIBO (minuscula
        # no pool) e quem abre a segunda e' o ADJETIVO. Medido na leitura do
        # texto montado: `did this. cheap as it sounds.` e `the villages of
        # old India is where...`. Uma regra so' resolve os dois, e continua
        # valendo para molde novo que alguem escreva depois.
        pontes = [(b, _frases(b["txt"] % ((raro["tribo"], adj) if b.get("inv")
                                          else (adj, raro["tribo"]))))
                  for b in PONTES]
        # ⛔ O trio inteiro e' sorteado entre os viaveis, nunca em cascata: o
        # VICK 16 escolheu o primeiro beat e depois procurou um que coubesse, e
        # o take 2 saiu com UMA fala em 400 videos.
        trios = [(x, b, t, fe) for x in FALHAS for (b, t) in pontes
                 for fe in FECHOS
                 if _palavras(x["txt"]) + _palavras(t)
                 + _palavras(fe["txt"]) <= TETO_FALA[1]]
        # ⛔⛔ SORTEIA-SE A FORMA, DEPOIS O TRIO — e isso e' conserto de um
        # vies que so' a medicao mostrou. Sorteando o trio direto, `pergunta`
        # ficava com 48% dos videos com apenas 4 das 22 entradas: as perguntas
        # sao as falas mais CURTAS, entao cabem com mais combinacoes de ponte
        # e fecho, e o comprimento vira PESO sem ninguem ter pedido.
        # ⭐ A licao generaliza: num sorteio filtrado por orcamento, entrada
        # curta e' entrada favorecida. Se o eixo que importa e' a FORMA, e' a
        # forma que tem de ser sorteada — nunca o resultado.
        por_forma = {}
        for t3 in trios:
            por_forma.setdefault(t3[0]["forma"], []).append(t3)
        x, b, t, fe = rng.choice(por_forma[rng.choice(sorted(por_forma))])
        spec["falha"], spec["ponte"], spec["fecho"] = x, b, fe
        spec["adjetivo"], spec["tribo_txt"] = adj, t
        f[0] = "%s %s %s" % (x["txt"], t, fe["txt"])
    if 1 in quais:
        v = spec["preparo"]
        # ⭐ A receita nomeia as TRES coisas: o raro, o aposto e o METODO.
        # Sem o metodo o espectador nao sabe o que fazer com o po', e o video
        # vira uma lista de nomes — o defeito que o CT3 cobra.
        receita = "%s, %s, %s." % (_cap(raro["nome"]), raro["aposto"],
                                   v["fala"])
        # ⛔⛔ A PROVA E' OPCIONAL, E ISSO E' ORCAMENTO MEDIDO, nao preguica.
        # A receita sozinha ja' custa 12 a 15 palavras porque carrega nome +
        # aposto + metodo; com o CTA de 9 a 11 sobram 0 a 4. Forcar a prova
        # estouraria os 25 em quase todo par — e o que corta no fim de um take
        # de 8s e' justamente o CTA.
        # ⭐ Entao ela entra QUANDO CABE, e o pool vazio compete de igual: o
        # sorteio escolhe entre os pares viaveis, nunca em cascata.
        opc = PROVAS + [{"id": "sem", "txt": ""}]
        pares = [(r, c) for r in opc for c in CTAS
                 if _palavras(receita) + _palavras(r["txt"])
                 + _palavras(c["txt"] % _cta()) <= TETO_FALA[2]]
        r, c = rng.choice(pares)
        spec["prova"], spec["cta"], spec["receita_txt"] = r, c, receita
        f[1] = " ".join(x for x in (receita, r["txt"], c["txt"] % _cta()) if x)
    return f


def _cta():
    """`Comment recipe`, com a palavra vinda do painel quando ele a troca."""
    kw = sc.keyword_do_motor(sys.modules[__name__])
    return "Comment %s" % kw


def sortear(pagina, rng, ledger, travas=None):
    travas = travas or {}
    hist = (ledger or {}).get(pagina, {})
    raro = (_por_id(RAROS, travas["raro"]) if travas.get("raro")
            else _fresco(RAROS, hist.get("raro", [])[-5:], rng))
    prep = (_por_id(PREPAROS, travas["preparo"]) if travas.get("preparo")
            else _fresco(preparos_para(raro),
                         hist.get("preparo", [])[-2:], rng))
    # ⚠️ Se o painel travou um METODO que nao extrai aquele raro, quem cede e'
    # o RARO — nunca o metodo, porque o metodo e' o que o operador acabou de
    # escolher na tela. Botao que promete e entrega outra coisa e' pior que
    # botao ausente.
    if prep["id"] not in raro["certo"]:
        livres = [r for r in RAROS if prep["id"] in r["certo"]]
        raro = rng.choice(livres) if livres else raro
        if prep["id"] not in raro["certo"]:
            prep = rng.choice(preparos_para(raro))
    spec = {
        "pagina": pagina,
        "etnia": ETNIA.get(pagina, "white American"),
        "idade": rng.choice(IDADES),
        "raro": raro,
        "preparo": prep,
        "ambiente": (_por_id(AMBIENTES, travas["ambiente"])
                     if travas.get("ambiente")
                     else _fresco(AMBIENTES, hist.get("ambiente", [])[-5:], rng)),
        "camera": (_por_id(CAMERAS, travas["camera"]) if travas.get("camera")
                   else _fresco(CAMERAS, hist.get("camera", [])[-4:], rng)),
        "acao": (_por_id(ACOES, travas["acao"]) if travas.get("acao")
                 else _fresco(ACOES, hist.get("acao", [])[-4:], rng)),
        "maos": (_por_id(MAOS, travas["maos"]) if travas.get("maos")
                 else _fresco(MAOS, hist.get("maos", [])[-4:], rng)),
    }
    spec["falas"] = [v for _, v in sorted(_falas(spec, rng).items())]
    return spec


def nova_fala(spec, i, rng):
    return _falas(spec, rng, quais=(i,))[i]


# ===========================================================================
# MONTAGEM
# ===========================================================================
def _maos_txt(spec):
    return ("the hands and forearms of a %d-year-old %s man, %s"
            % (spec["idade"], spec["etnia"], spec["maos"]["txt"]))


CAUDA = ("Everyday amateur snapshot look, slight natural sway, soft sensor "
         "grain. No on-screen text, no subtitles, no captions, no watermark.")


def montar(spec):
    amb, cam, ac = spec["ambiente"], spec["camera"], spec["acao"]
    raro, veic = spec["raro"], spec["preparo"]
    maos = _maos_txt(spec)
    b = {}

    # ⛔ O BLOCO 0 E' UMA FOTO DAS MAOS, nao de uma pessoa. Sem rosto em quadro
    # elas sao a UNICA ancora de continuidade entre os dois quadros, que sao
    # gerados separadamente — mesmo precedente do `banho16` e do `horse16`.
    b["BLOCO 0 (REF)"] = (
        "REF 01: Photo of a real person's hands: both hands and forearms of a "
        "%d-year-old %s man, %s, resting palm-down and side by side on a plain "
        "neutral grey surface. The frame holds the hands and forearms and stops "
        "at the elbows. Soft even frontal light. Slight sensor grain, raw "
        "amateur photo look. No subtitles, no captions, no burned-in text, no "
        "watermark." % (spec["idade"], spec["etnia"], spec["maos"]["txt"]))

    # ⛔ A ORDEM E' A MESMA NOS DOIS BLOCOS — ambiente, superficie, o raro
    # inteiro, a tigela de po, o veiculo, as maos, o gesto, a camera, a luz,
    # a cauda. Bloco que muda de ordem entre os quadros da' ao gerador uma
    # segunda leitura da mesma cena, e ele desenha a segunda.
    # ⛔⛔ OS DOIS PONTOS DEPOIS DA SUPERFICIE NAO SAO ESTILO. Varias
    # entradas de `sup` terminam numa oracao subordinada (`the clear glass,
    # the pieces reflected faintly in it`), e um VERBO depois delas produz
    # `On the clear glass, the pieces reflected faintly in it lie the whole
    # fenugreek` — gramatica quebrada no meio do quadro. O `:` encerra a
    # frase da superficie e a lista comeca limpa, seja qual for a entrada.
    # ⚠️ O linter nao pega isto: os dois blocos tem os mesmos substantivos e
    # o mesmo tamanho. So' aparece LENDO o texto montado.
    b["IMAGE 01/02"] = (
        "IMAGE 01/02: %s. On %s: %s, and right beside it %s. "
        "Next to them stands %s. In frame are %s, and %s. %s. %s. %s"
        % (_cap(amb["amb"]), amb["sup"], raro["inteiro"], raro["img"],
           veic["img"], maos, ac["t1"], cam["txt"], _cap(amb["luz"]),
           CAUDA))

    b["IMAGE 02/02"] = (
        "IMAGE 02/02: %s, the same place in the same framing. On %s: %s, and "
        "right beside it %s. Next to them stands %s, and %s. In frame are the "
        "same hands and forearms from the first scene, %s, not different "
        "hands. %s. %s. %s. %s"
        % (_cap(amb["amb"]), amb["sup"], raro["inteiro"], raro["img"],
           veic["img"], veic["t2"], spec["maos"]["txt"], _cap(ac["t2"]),
           cam["txt"], _cap(amb["luz"]), CAUDA))

    b["TAKE 01/02"] = (
        "TAKE 01/02: Animate the provided image exactly. %s, and there are no "
        "cuts. The movement happens once, slowly, and stops. Nothing else in "
        "the frame moves and nobody enters the shot. Audio: %s. One calm "
        "American man speaks over the shot at the ordinary pace of everyday "
        "speech, never stretching or slowing the words to fill the take; he is "
        "never seen.\nDialogue: \"%s\""
        % (cam["txt"], amb["audio"], spec["falas"][0]))

    b["TAKE 02/02"] = (
        "TAKE 02/02: Animate the provided image exactly. %s, and there are no "
        "cuts. The movement finishes and settles; nothing else in the frame "
        "changes and nobody enters the shot. Audio: %s. The same calm American "
        "voice from the first take, same pitch, same texture, same pace; he is "
        "never seen.\nDialogue: \"%s\""
        % (cam["txt"], amb["audio"], spec["falas"][1]))

    return sc.selar_takes(sc.selar_tags(b))


# ===========================================================================
# AS LENTES
# ===========================================================================
_RX_APARELHO = re.compile(
    r"\b(phone|iphone|smartphone|camera|camcorder|lens|filming|filmed|"
    r"recording|selfie|tripod|gimbal)\b", re.I)
_RX_PESSOA = re.compile(
    r"\b(his face|her face|smiling|chest|torso|shoulders|shirt|wearing a|"
    r"looks at the lens|man stands|woman stands)\b", re.I)
_RX_GELATINA = re.compile(r"\bgelatin[ea]?\b", re.I)


def _sem_dialogo(txt):
    return re.sub(r'Dialogue:.*', '', txt, flags=re.S)


def _ra1_sem_aparelho(spec, blocos, ach):
    """⛔ Aparelho escrito num prompt vira aparelho DESENHADO no quadro.

    O repo pagou um lote inteiro por isso: o `vick16` dizia `with the phone in
    his free hand` e o gerador desenhou o telefone.
    ⚠️ Vale nos quatro blocos, e fora do `Dialogue:` — a fala e' do operador.
    """
    for k, v in blocos.items():
        m = _RX_APARELHO.search(_sem_dialogo(v))
        if m:
            ach.append(("ERRO", "RA1: %s nomeia %r — aparelho escrito vira "
                                "aparelho desenhado" % (k, m.group(0))))


def _ra2_ninguem_em_quadro(spec, blocos, ach):
    """⛔⛔ A ASSINATURA DESTE ANGULO E' A AUSENCIA.

    Ordem do operador: *"nao aparece ninguem"*. So' maos e antebracos. Rosto,
    torso ou roupa em quadro descaracterizam o motor inteiro — e o gerador
    ADORA acrescentar uma pessoa se o texto abrir espaco.
    """
    for k in ("IMAGE 01/02", "IMAGE 02/02"):
        m = _RX_PESSOA.search(blocos[k])
        if m:
            ach.append(("ERRO", "RA2: %s poe gente em quadro (%r) — este "
                                "angulo e' so' maos" % (k, m.group(0))))


def _ra3_sem_gelatina(spec, blocos, ach):
    """⛔ Esta rota NAO usa gelatina, por ordem expressa (2026-08-20).

    A lente existe porque o parque inteiro fala em gelatina e a proxima copy
    colada de outro motor traria a palavra junto sem ninguem notar.
    """
    for k, v in blocos.items():
        if _RX_GELATINA.search(v):
            ach.append(("ERRO", "RA3: %s fala em gelatina — esta rota fecha em "
                                "`recipe` e nao usa gelatina" % k))


def _ra4_raro_nos_dois(spec, blocos, ach):
    """O raro e a tigela de po ficam nos DOIS quadros, iguais.

    ⛔ Se o ingrediente saisse do segundo quadro, o video prometeria uma coisa
    e mostraria outra no payoff — e o inventario fechado e' o que impede o
    gerador de trocar a mesa no meio.
    """
    r = spec["raro"]
    for k in ("IMAGE 01/02", "IMAGE 02/02"):
        if r["inteiro"] not in blocos[k]:
            ach.append(("ERRO", "RA4: %s sem o %s inteiro em quadro"
                        % (k, r["nome"])))
        if r["img"] not in blocos[k]:
            ach.append(("ERRO", "RA4: %s sem a tigela de po do %s"
                        % (k, r["nome"])))


def _ra5_copy_amarrada(spec, blocos, ach):
    """⭐⭐ O TEOR SEMANTICO VINCULADO, em codigo.

    A tribo do take 1 tem de ser a do raro que o take 2 nomeia. Sem esta lente
    o motor poderia dizer `the Andean men` e servir acafrao persa — que e' o
    drifting que o operador reprova no teste WTF.
    """
    # ⚠️ minusculas dos dois lados: as pontes `inv` CAPITALIZAM a tribo
    # (ela abre a frase), e a comparacao crua reprovava 104 videos certos.
    if spec["raro"]["tribo"].lower() not in spec["falas"][0].lower():
        ach.append(("ERRO", "RA5: a tribo da fala 1 nao e' a do raro sorteado"))
    # ⚠️ minusculas dos dois lados: a fala CAPITALIZA a primeira palavra
    # (`Maca root, ...`) e a comparacao crua reprovava 400 de 400 videos
    # certos.
    if spec["raro"]["nome"].lower() not in spec["falas"][1].lower():
        ach.append(("ERRO", "RA5: a fala 2 nao nomeia o raro"))
    if spec["raro"]["aposto"].lower() not in spec["falas"][1].lower():
        ach.append(("ERRO", "RA5: a fala 2 perdeu o APOSTO — sem ele o "
                            "ingrediente e' um nome jogado no roteiro"))
    if spec["preparo"]["fala"].lower() not in spec["falas"][1].lower():
        ach.append(("ERRO", "RA5: a fala 2 nao diz COMO se prepara"))


def _ra6_par_possivel(spec, blocos, ach):
    """⛔⛔ O METODO TEM DE EXTRAIR AQUELE RARO.

    Nao e' questao de gosto: `ashwagandha` em agua fervida por muito tempo
    degrada a withaferina A, que e' termolabil; `fenugreek` fervido perde a
    mucilagem que so' sai em agua fria; `ginkgo` em decoccao longa cozinha a
    folha. O video mostraria alguem preparando errado — e o espectador que
    conhece a planta perde a confianca na hora.
    """
    p, r = spec["preparo"], spec["raro"]
    if p["id"] in r.get("falso", ()):
        ach.append(("ERRO", "RA6: %s em %s e' o metodo que a tabela marca "
                            "como ERRADO — nao extrai"
                    % (r["nome"], p["curto"])))
    elif p["id"] not in r["certo"]:
        ach.append(("ERRO", "RA6: %s nao se prepara em %s"
                    % (r["nome"], p["curto"])))


def _ra7_orcamento(spec, blocos, ach):
    for i, fala in enumerate(spec["falas"], 1):
        n = _palavras(fala)
        if n > TETO_FALA[i]:
            ach.append(("ERRO", "RA7: cena %d com %d palavras (teto %d) — a "
                                "fala CORTA" % (i, n, TETO_FALA[i])))
        if n < PISO_FALA[i]:
            ach.append(("AVISO", "RA7: cena %d com so' %d palavras" % (i, n)))


def _ra8_fala_no_take(spec, blocos, ach):
    for i, k in enumerate(("TAKE 01/02", "TAKE 02/02")):
        if ('Dialogue: "%s"' % spec["falas"][i]) not in blocos[k]:
            ach.append(("ERRO", "RA8: a fala %d nao chega verbatim ao %s"
                        % (i + 1, k)))


def _ct16(spec, blocos, ach):
    """⛔ CT5 DESLIGADO, e a excecao e' a razao de existir do motor: o video E'
    a receita nomeada. Sem o ingrediente na fala nao ha' curiosidade nem
    autoridade — sobra "um po' qualquer".
    ⛔ CT4/CT4b tambem: este angulo NAO nomeia orgao nenhum (nao ha' corpo em
    quadro), entao a cota de apelido nao se aplica.
    """
    fora = []
    sc.lint_copy16(sys.modules[__name__], spec, fora)
    ach.extend(x for x in fora
               if not x[1].startswith(("CT5:", "CT4:", "CT4b:")))


def _anticeleb(spec, blocos, ach):
    sc.lint_anticeleb(blocos, ach)


def _painel(spec, blocos, ach):
    sc.lint_painel_honesto(sys.modules[__name__], spec, blocos, ach)


def lint(spec, blocos):
    return sc.lint_curto(
        sys.modules[__name__], spec, blocos, (1, 2), TETO_FALA,
        literais=("recipe",), cota_min=0,
        extras=(_ct16, _anticeleb, _painel, _ra1_sem_aparelho,
                _ra2_ninguem_em_quadro, _ra3_sem_gelatina, _ra4_raro_nos_dois,
                _ra5_copy_amarrada, _ra6_par_possivel, _ra7_orcamento,
                _ra8_fala_no_take))


# ===========================================================================
# RESUMO E PAINEL
# ===========================================================================
def resumo_pt(spec):
    return ("16s, DOIS takes, SO' A MESA — ninguem em quadro, so' as maos. "
            "Ambiente: %s. Camera: %s. Acao: %s. RARO: %s (%s), com a tigela "
            "de po ao lado, preparado em %s. TAKE 1 — a falha + a tribo (%s) + a "
            "farmacia. TAKE 2 — a receita nomeada + CTA. Maos: %s. Homem de "
            "%d anos (so' as maos e a voz). Fecha em `%s`. ⛔ SEM gelatina."
            % (spec["ambiente"]["curto"], spec["camera"]["curto"],
               spec["acao"]["curto"], spec["raro"]["nome"],
               spec["raro"]["aposto"], spec["preparo"]["curto"],
               spec["raro"]["tribo"], spec["maos"]["curto"], spec["idade"],
               sc.keyword_do_motor(sys.modules[__name__])))


EIXOS_UI = [
    ("raro", "O INGREDIENTE RARO", "RAROS", "nome"),
    ("preparo", "COMO SE PREPARA", "PREPAROS", "curto"),
    ("ambiente", "O AMBIENTE", "AMBIENTES", "curto"),
    ("camera", "O ANGULO", "CAMERAS", "curto"),
    ("acao", "A MANIPULACAO", "ACOES", "curto"),
    ("maos", "AS MAOS", "MAOS", "curto"),
]
EIXOS_TRAVAVEIS = ["raro", "preparo", "ambiente", "camera", "acao", "maos"]
DROPDOWNS_UI = [("raro", "O RARO", "RAROS", "nome"),
                ("ambiente", "O AMBIENTE", "AMBIENTES", "curto")]
IGNORA_PAINEL = ()


# ===========================================================================
# AUTOTESTE
# ===========================================================================
def _autoteste(n=400, seed=20260820):
    rng = random.Random(seed)
    led, erros = {}, collections.Counter()
    cont = {e: collections.Counter() for e in
            ("raro", "preparo", "ambiente", "camera", "acao", "maos")}
    falas = {1: set(), 2: set()}
    pal = {1: [], 2: []}
    pares, specs = set(), []
    for _ in range(n):
        sp = sortear("joe", rng, led)
        _anotar(led, sp)
        bl = montar(sp)
        for nivel, txt in lint(sp, bl):
            if nivel == "ERRO":
                erros[txt.split(":")[0]] += 1
        for e in cont:
            cont[e][sp[e]["id"]] += 1
        pares.add((sp["raro"]["id"], sp["preparo"]["id"]))
        specs.append(sp)
        for i in (1, 2):
            falas[i].add(sp["falas"][i - 1])
            pal[i].append(_palavras(sp["falas"][i - 1]))

    print("%s — %d sorteios (seed %d)" % (APP, n, seed))
    for e, pool in (("raro", RAROS), ("preparo", PREPAROS),
                    ("ambiente", AMBIENTES), ("camera", CAMERAS),
                    ("acao", ACOES), ("maos", MAOS)):
        c = cont[e]
        print("  %-9s %2d de %2d alcancados · menos sorteado %dx"
              % (e, len(c), len(pool), min(c.values())))
    # ⛔ O par raro x veiculo e' o unico eixo com trava; conferir que ela NAO
    # esta' matando combinacao demais.
    possiveis = sum(len(preparos_para(r)) for r in RAROS)
    print("  pares raro x metodo vistos: %d de %d que EXTRAEM"
          % (len(pares), possiveis))
    # ⭐⭐ A MEDICAO QUE TERIA PEGO O DEFEITO ORIGINAL. O pool nasceu com oito
    # falhas e as OITO eram pergunta — contar entradas dizia "8 opcoes", e o
    # operador viu na tela que era uma frase repintada. Contar FORMA e' o que
    # mede variacao percebida.
    # ⚠️ E a distribuicao importa mais que a existencia: uma forma em 60% dos
    # videos e' quase o pool antigo com enfeite.
    formas = collections.Counter(sp["falha"]["forma"] for sp in specs)
    print("  FORMA do hook (o que o espectador percebe, nao o numero de "
          "entradas):")
    for k, v in formas.most_common():
        print("     %-12s %3d  %2d%%" % (k, v, 100 * v // len(specs)))
    dom = formas.most_common(1)[0]
    if 100 * dom[1] // len(specs) > 45:
        print("     ⛔ `%s` domina %d%% — pool de forma unica com enfeite"
              % (dom[0], 100 * dom[1] // len(specs)))
    fam = collections.Counter(sp["fecho"]["fam"] for sp in specs)
    print("  FECHO: %s" % " · ".join("%s %d%%" % (k, 100 * v // len(specs))
                                     for k, v in fam.most_common()))
    print("  adjetivos usados: %d de %d"
          % (len(set(sp["adjetivo"] for sp in specs)), len(ADJETIVOS)))
    print("  pontes usadas: %d de %d"
          % (len(set(sp["ponte"]["id"] for sp in specs)), len(PONTES)))
    for i in (1, 2):
        print("  cena %d: %3d falas distintas · palavras %d/%d/%d (teto %d)"
              % (i, len(falas[i]), min(pal[i]), sum(pal[i]) // len(pal[i]),
                 max(pal[i]), TETO_FALA[i]))

    # ⛔ CONTROLES NEGATIVOS: cada lente prova que ACUSA o defeito plantado.
    print("  controles negativos:")
    sp = sortear("joe", random.Random(1), {})
    bl = montar(sp)
    provas = [
        ("aparelho", "IMAGE 01/02", lambda t: t + " Shot with a phone."),
        ("gente em quadro", "IMAGE 01/02", lambda t: t + " A man stands behind."),
        ("gelatina", "IMAGE 02/02", lambda t: t + " A box of gelatin sits by."),
    ]
    falhou = 0
    for rot, k, sabota in provas:
        b2 = dict(bl)
        b2[k] = sabota(b2[k])
        pego = any(n == "ERRO" for n, _ in lint(sp, b2))
        print("     %-18s %s" % (rot, "acusou" if pego else "⛔ PASSOU"))
        falhou += 0 if pego else 1
    # o par proibido
    sp2 = dict(sp)
    sp2["raro"] = _por_id(RAROS, "ashwagandha")
    sp2["preparo"] = _por_id(PREPAROS, "fervura_longa")
    pego = any(t.startswith("RA6") for n, t in lint(sp2, montar(sp2))
               if n == "ERRO")
    print("     %-18s %s" % ("metodo que nao extrai",
                             "acusou" if pego else "⛔ PASSOU"))
    falhou += 0 if pego else 1

    print("  linter: %d ERRO" % sum(erros.values()))
    for k, v in erros.most_common(8):
        print("     %4dx %s" % (v, k))
    return sum(erros.values()) + falhou


def main():
    ap = argparse.ArgumentParser(description=APP)
    ap.add_argument("--pagina", default="joe")
    ap.add_argument("--seed", type=int)
    ap.add_argument("--autoteste", action="store_true")
    ap.add_argument("--n", type=int, default=400)
    a = ap.parse_args()
    if a.autoteste:
        raise SystemExit(1 if _autoteste(a.n) else 0)
    rng = random.Random(a.seed)
    sp = sortear(a.pagina, rng, _carregar_ledger())
    bl = montar(sp)
    print(resumo_pt(sp), "\n")
    for k in ("BLOCO 0 (REF)", "IMAGE 01/02", "IMAGE 02/02",
              "TAKE 01/02", "TAKE 02/02"):
        print("=" * 70)
        print(bl[k], "\n")
    for nivel, txt in lint(sp, bl):
        print("[%s] %s" % (nivel, txt))


if __name__ == "__main__":
    main()
