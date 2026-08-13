#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE FLAGRANTE SHORT — 3 cenas de 8 segundos.

⭐ 2026-08-03 — MOTOR AUTOSSUFICIENTE. Nao importa mais nenhum modulo
`*_lucas`: as strings travadas, os pools, as tabelas de token banido e o arco
de cinco cenas foram copiados para ca', caractere por caractere. Este arquivo
passou a ser a FONTE DA VERDADE do angulo FLAGRANTE.

    base 1 · RUINA      ->  SHORT 1 · O FLAGRANTE
    base 4 · REDENCAO   ->  SHORT 2 · O TRUQUE + A VIRADA   (funde 2 e 4)
    base 5 · CTA        ->  SHORT 3 · CTA

⛔ O QUE O COLAPSO AMEACAVA
No FLAGRANTE o literal `gelatin trick` morava nas DESCOBERTAS — **a cena 2**,
que nao sobrevive. Junto com ele ia embora o MUP (`blood flow`), que vive na
mesma frase daquele pool. Os dois entram na copy fundida, e o linter trava.

⚠️ O QUE SE PERDE, e e' consciente: o **F16** (a placa D1 em corte sagital na
cena 2) nao tem onde morar num video de tres cenas. A explicacao anatomica cede
lugar a oracao de `blood flow` dentro da cena 2. Quem quiser o D1 usa a versao
longa.
"""

import collections
import os
import random
import re
import sys
import types

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import short_comum as sc                                        # noqa: E402

from nucleo_sonoro import sonorizar                             # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(AQUI, ".flagrante-short-ledger.json")

TITULO = "AGENTE FLAGRANTE SHORT"
SUBTITULO = "humilhação pública, em 3 cenas · gerador offline de prompts Veo"
SLUG = "flagrante-short"


# ===========================================================================
# ⭐ MOTOR LONGO INLINEADO — 2026-08-03
# ===========================================================================
# Ate' hoje este arquivo fazia `import flagrante_lucas as base` e herdava de la'
# ETNIA, NUCLEO, EIXOS_UI, BRAGGING, QUEM_CONTOU, PT_OCASIAO, _palavras e o
# proprio arco de 5 cenas (sortear/montar/nova_fala). Os arquivos `*_lucas` sao
# de terceiro e saem do repo de trabalho — enquanto a importacao existisse, a
# fonte da verdade do FLAGRANTE morava num arquivo que nao e' nosso.
#
# Tudo o que vinha de la' esta' copiado abaixo, LITERAL: mesma ordem, mesma
# pontuacao, e os comentarios de regra vieram junto, porque eles sao a memoria
# de por que cada string existe. ⛔ Nada foi reescrito nem reindentado — com o
# mesmo seed, o video que sai e' bit a bit o mesmo de antes da separacao.
#
# ⚠️ TRES nomes tiveram de mudar, e so' eles, porque colidiam com a API deste
# arquivo (o SHORT tem os seus proprios `sortear`, `montar` e `nova_fala`, de 3
# cenas). O arco de CINCO cenas passou a se chamar:
#       sortear    ->  _sortear_longo
#       montar     ->  _montar_longo
#       nova_fala  ->  _nova_fala_longo
# Sao eles que rodam ANTES do colapso 5->3. Confundir os dois pares troca o
# video inteiro.
#
# ⛔ O `TETO_FALA` do arco longo ({1: 22, 2: 30, 3: 22, 4: 32, 5: 24}) NAO veio:
# nem este arquivo nem o `short_comum` o liam. O teto que vale aqui e' o de 3
# cenas, medido, que continua na secao do SHORT. Copiar o outro criaria uma
# segunda verdade sem ninguem para le-la.
#
# ⚠️ A parte propria do SHORT (MAPA, FUNDIDAS, linter, resumo) comeca depois
# deste bloco, em `O SHORT`.

# ---------------------------------------------------------------------------
# STRINGS TRAVADAS — copia literal da doutrina. NAO REESCREVER, NAO COMPRIMIR.
# Cada token esta' aqui porque a combinacao passou na moderacao e renderizou
# certo. Comprimir o D1 uma vez ja' entregou esqueleto 3D no lugar da placa.
# ---------------------------------------------------------------------------

D1_IMAGE = (
    "In his left hand he holds up toward the camera a hand-sized medical "
    "teaching model of the male pelvis in median sagittal section — a "
    "flat-backed slab of molded plastic, painted in pink, salmon and pale "
    "blue, the interior structures exposed in lengthwise profile the way a "
    "urology office display shows them, the whole model turned so its cut "
    "face is squared to the lens. His right index finger points at the model."
)

D1_TAKE = (
    "He holds the plastic anatomy model steady in his left hand and taps its "
    "cut face twice with his right index finger as he explains. The model "
    "stays squared to the camera and does not turn or tilt."
)

IMOBILIDADE = (
    "same position, same angle, same shape — completely motionless for the "
    "entire shot."
)

NEGACAO_AVE = (
    " No bird, no goose, no duck, no swan, no snake, no feathers, no beak, no "
    "eyes, no head, nothing alive."
)

ANTICELEB = "Ordinary relatable face, not a celebrity."
CAUDA = "iPhone shot, natural grain, no text, no watermark."

# Agencia — a correcao validada em 2026-07-30. O proxy fica na mao da PROPRIA
# vitima e o narrador so' aponta, sem contato. Proxy na mao de terceiro no
# corpo dela barrou 4x seguidas (2 paginas, 2 props, 2 geometrias).
AGENCIA_IMAGE = (
    "In his own fist on his lap he holds {prop_murcho}. Beside him {ref_desc} "
    "points his finger down at it without touching him, talking to camera."
)
AGENCIA_TAKE = (
    "The {ref_curto}-haired man speaks calmly to camera, his pointing finger "
    "stays close but never touches the seated man. The seated man keeps his "
    "head down, blinks slowly, never speaks, his fist stays on his own lap."
)

# ⭐ QUEM NARRA — o sexo de quem fala com a lente (2026-08-06).
# Ordem do operador: *"uma marcacao dentro dos agentes python, de todos, pra
# saber se aquele agente gera roteiros com personagem homens e mulheres como
# narrador/apresentador ou se so' gera com um dos dois"*.
# ⛔ MEDIDO, nao lido: 120 sorteios por agente, olhando o BLOCO 0 do prompt.
# Declarar de cabeca aqui seria a mesma FORMA-sem-FUNCAO que ja' custou o
# botao de pele morto em tres motores.
# ⚠️ Com DOIS sexos a UI desenha a trava homem/mulher; com um so', nao desenha
# botao nenhum — botao que nao trava nada e' pior que botao nenhum.
SEXOS = ("homem",)

ETNIA = {
    # ⭐ As 5 paginas do lote de 2026-08-05. Split 3 brancos / 2 negros —
    # a razao (volume absoluto x prevalencia) esta' escrita no
    # `bridge-pages-deploy.md`.
    "roy": "white American", "dean": "white American",
    "earl": "white American",
    "jason": "Black American", "philippe": "Black American",
    "joe": "white American",
    "ray": "white American",
    "matt": "white American",
    "marcus": "Black American",
    "chuck": "Black American",
}

# ---------------------------------------------------------------------------
# POOLS SORTEAVEIS
# ---------------------------------------------------------------------------

# F7 — ocasiao nova vira registro. Marcadas com selo:
#   V = validada em render · N = nova, ainda sem numero
OCASIOES = [
    {
        "id": "casamento", "selo": "V",
        "cenario": "a wedding reception",
        "detalhe": "round table with plates and glasses, string lights overhead",
        "assento": "at the table", "posicao_mulher": "Across the table",
        "plateia": "guests", "plateia_evento": "that wedding",
        "eco": "same reception hall",
        "luz_hook": "Warm string-light glow.",
        "audio": "reception chatter, laughter, glasses clinking.",
    },
    {
        "id": "confraternizacao", "selo": "V",
        "cenario": "a company year-end holiday party in a break room",
        "detalhe": "paper garlands and a folding table with plastic cups",
        "assento": "on a folding chair", "posicao_mulher": "Across the room",
        "plateia": "coworkers", "plateia_evento": "that Christmas party",
        "eco": "the next company party",
        "luz_hook": "Warm string-light glow mixed with overhead fluorescent.",
        "audio": "party chatter, laughter, a plastic cup set down.",
    },
    {
        "id": "pescaria_firma", "selo": "N",
        "cenario": "a company fishing trip on a lake dock",
        "detalhe": "coolers and folding chairs on the wooden dock",
        "assento": "on a folding chair on the dock",
        "posicao_mulher": "Standing on the dock",
        "plateia": "coworkers", "plateia_evento": "that boat",
        "eco": "same dock, same crew",
        "luz_hook": "Bright overcast daylight.",
        "audio": "water lapping the dock, laughter, a cooler lid closing.",
    },
    {
        "id": "reuniao_firma", "selo": "N",
        "cenario": "a company end-of-year meeting in a conference room",
        "detalhe": "long table with laptops and coffee cups",
        "assento": "at the table", "posicao_mulher": "Across the table",
        "plateia": "colleagues", "plateia_evento": "that company meeting",
        "eco": "same conference room",
        "luz_hook": "Flat office fluorescent light.",
        "audio": "office chatter, laughter, a laptop closing.",
    },
    {
        "id": "churrasco", "selo": "V",
        "cenario": "a family cookout in a backyard",
        "detalhe": "picnic table with paper plates, a grill smoking behind them",
        "assento": "at the picnic table", "posicao_mulher": "Across the table",
        "plateia": "relatives", "plateia_evento": "that cookout",
        "eco": "same backyard, same crowd",
        "luz_hook": "Late afternoon sunlight.",
        "audio": "cookout chatter, laughter, a grill hissing.",
    },
    {
        "id": "jantar_amigos", "selo": "N",
        "cenario": "a friends' dinner party in a dining room",
        "detalhe": "long table with dinner plates and wine glasses",
        "assento": "at the near end of the table",
        "posicao_mulher": "Across the table",
        "plateia": "dinner guests", "plateia_evento": "that dinner table",
        "eco": "same dinner table",
        "luz_hook": "Warm dining room lamp light.",
        "audio": "dinner chatter, laughter, cutlery on plates.",
    },
    {
        "id": "aniversario", "selo": "V",
        "cenario": "a fortieth anniversary party in a rented hall",
        "detalhe": "a long table with a sheet cake and folding chairs",
        "assento": "at the table", "posicao_mulher": "Across the table",
        "plateia": "family members", "plateia_evento": "that anniversary party",
        "eco": "same hall, same song",
        "luz_hook": "Warm overhead hall light.",
        "audio": "party chatter, laughter, a chair scraping.",
    },
    {
        "id": "clube_golfe", "selo": "N",
        "cenario": "a clubhouse lunch after a golf round",
        "detalhe": "a corner table with iced tea glasses and golf gloves",
        "assento": "at the corner table", "posicao_mulher": "Across the table",
        "plateia": "club members", "plateia_evento": "that clubhouse",
        "eco": "same clubhouse table",
        "luz_hook": "Bright window daylight.",
        "audio": "clubhouse chatter, laughter, ice in a glass.",
    },
    # + 2026-08-01: o operador mediu vicio no lote — o mesmo punhado de
    # eventos voltando. Pool dobrado, todas selo N (ainda sem numero).
    {
        "id": "igreja_social", "selo": "N",
        "cenario": "a church fellowship hall after service",
        "detalhe": "folding tables with coffee urns and paper cups",
        "assento": "on a folding chair", "posicao_mulher": "Across the table",
        "plateia": "churchgoers", "plateia_evento": "that church hall",
        "eco": "same fellowship hall",
        "luz_hook": "Flat overhead hall light.",
        "audio": "hall chatter, laughter, a coffee urn hissing.",
    },
    {
        "id": "clube_veteranos", "selo": "N",
        "cenario": "a veterans club hall on a Friday night",
        "detalhe": "small round tables with beer glasses, a bar counter behind them",
        "assento": "at a round table", "posicao_mulher": "Across the room",
        "plateia": "old servicemen", "plateia_evento": "that veterans hall",
        "eco": "same veterans hall, same table",
        "luz_hook": "Dim amber bar light.",
        "audio": "bar chatter, laughter, a glass set down on wood.",
    },
    {
        "id": "boliche", "selo": "N",
        "cenario": "a bowling alley on league night",
        "detalhe": "a scoring table with rented shoes and a ball rack behind it",
        "assento": "on the bench at the scoring table",
        "posicao_mulher": "Standing by the ball rack",
        "plateia": "league bowlers", "plateia_evento": "that bowling league",
        "eco": "same lane, same league night",
        "luz_hook": "Cool overhead alley light.",
        "audio": "pins falling, laughter, a ball rolling on wood.",
    },
    {
        "id": "lanchonete", "selo": "N",
        "cenario": "a roadside diner at Sunday breakfast",
        "detalhe": "a corner booth with coffee mugs and a napkin holder",
        "assento": "in the booth", "posicao_mulher": "Across the booth",
        "plateia": "diner regulars", "plateia_evento": "that diner booth",
        "eco": "same booth, same waitress",
        "luz_hook": "Hard morning light through the window blinds.",
        "audio": "diner chatter, laughter, mugs set on a counter.",
    },
    {
        "id": "reencontro", "selo": "N",
        "cenario": "a forty-year class reunion in a rented gym",
        "detalhe": "folding tables with punch bowls and paper streamers",
        "assento": "at a folding table", "posicao_mulher": "Across the table",
        "plateia": "old classmates", "plateia_evento": "that class reunion",
        "eco": "same gym, same crowd",
        "luz_hook": "Cool overhead gym light.",
        "audio": "reunion chatter, laughter, a punch ladle clinking.",
    },
    {
        "id": "feira_condado", "selo": "N",
        "cenario": "a county fair food tent",
        "detalhe": "long picnic tables under canvas, paper trays of food",
        "assento": "at a picnic table",
        "posicao_mulher": "Across the picnic table",
        "plateia": "fairgoers", "plateia_evento": "that county fair",
        "eco": "same fair, same tent",
        "luz_hook": "Bright daylight under canvas shade.",
        "audio": "fairground chatter, laughter, a distant loudspeaker.",
    },
]

# Ancora de escala obrigatoria nos dois estados (F12 / F15).
# murcho: "no longer than his thumb" · ereto: "as long as her forearm"
PROPS = [
    {"id": "geoduck", "marisco": True,
     "murcho": ("a small geoduck clam by its pale ridged shell, its siphon no "
                "longer than his thumb, shriveled and wrinkled, completely "
                "soft, folded over on itself"),
     "ereto": ("a geoduck clam upright by its shell at shoulder height, its "
               "siphon held stiff and straight, as long as her forearm and as "
               "thick as her wrist")},
    {"id": "banana", "marisco": False,
     "murcho": ("a small banana, no longer than his thumb, shriveled and "
                "wrinkled, skin dull and spotted, completely soft, folded "
                "over on itself"),
     "ereto": ("a banana upright at shoulder height, held stiff and straight, "
               "as long as her forearm and as thick as her wrist")},
    {"id": "okra", "marisco": False,
     "murcho": ("a small wilted okra pod, no longer than his thumb, shriveled "
                "and completely soft, drooping over his fingers"),
     "ereto": ("an okra pod upright at shoulder height, held stiff and "
               "straight, as long as her forearm")},
    {"id": "pepino", "marisco": False,
     "murcho": ("a small shrivelled cucumber, no longer than his thumb, "
                "wrinkled and completely soft, folded over on itself"),
     "ereto": ("a cucumber upright at shoulder height, held stiff and "
               "straight, as long as her forearm and as thick as her wrist")},
    {"id": "aspargo", "marisco": False,
     "murcho": ("a small wilted asparagus stalk, no longer than his thumb, "
                "limp and drooping over his fingers"),
     "ereto": ("an asparagus stalk upright at shoulder height, held stiff and "
               "straight, as long as her forearm")},
    {"id": "daikon", "marisco": False,
     "murcho": ("a small shrivelled daikon radish, no longer than his thumb, "
                "wrinkled and completely soft, drooping over his fingers"),
     "ereto": ("a daikon radish upright at shoulder height, held stiff and "
               "straight, as long as her forearm and as thick as her wrist")},
    {"id": "linguica", "marisco": False,
     "murcho": ("a small pale sausage, no longer than his thumb, shriveled "
                "and completely soft, folded over on itself"),
     "ereto": ("a thick sausage upright at shoulder height, held stiff and "
               "straight, as long as her forearm")},
    # + 2026-08-01: o operador mediu vicio — sempre o mesmo prop na mao do
    # lote. Dois novos, com as duas ancoras de escala obrigatorias (F12/F15).
    {"id": "cenoura", "marisco": False,
     "murcho": ("a small limp carrot, no longer than his thumb, shriveled and "
                "wrinkled, completely soft, drooping over his fingers"),
     "ereto": ("a carrot upright at shoulder height, held stiff and straight, "
               "as long as her forearm")},
    {"id": "alho_poro", "marisco": False,
     "murcho": ("a small wilted leek, no longer than his thumb, shriveled and "
                "completely soft, folded over on itself"),
     "ereto": ("a leek stalk upright at shoulder height, held stiff and "
               "straight, as long as her forearm and as thick as her wrist")},
]

# Set das cenas 2/3/5. Escopo do D1 (P15): bancada ou interno — todos servem.
AMBIENTES = [
    {"id": "cozinha", "set": "a plain kitchen, cabinets and a window behind him",
     "bancada": "counter", "curto": "kitchen", "luz": "warm lamp light."},
    {"id": "cozinha_aberta",
     "set": "an open-plan kitchen with an island, a living room out of focus behind him",
     "bancada": "island", "curto": "kitchen", "luz": "warm even light from a window frame-left."},
    {"id": "churrasqueira",
     "set": "an outdoor grill station in a backyard, a wooden fence behind him",
     "bancada": "grill counter", "curto": "grill station", "luz": "late afternoon sunlight from frame-left."},
    {"id": "varanda",
     "set": "a covered back porch, a screen door and potted plants behind him",
     "bancada": "porch table", "curto": "back porch", "luz": "soft shaded daylight."},
    {"id": "garagem",
     "set": "a clean home garage workshop, pegboard tools on the wall behind him",
     "bancada": "workbench", "curto": "garage workshop", "luz": "cool overhead shop light."},
    {"id": "copa",
     "set": "a small breakfast nook, a window with half-closed blinds behind him",
     "bancada": "table", "curto": "breakfast nook", "luz": "warm morning light from frame-right."},
    # + 2026-08-01: o operador mediu vicio — o mesmo set de video em video.
    # Seis ambientes novos, todos com bancada e internos (escopo do D1, P15).
    {"id": "lavanderia", "set": "a home laundry room, a washer and dryer behind him",
     "bancada": "folding counter", "curto": "laundry room", "luz": "cool even light from a small window."},
    {"id": "porao_bar",
     "set": "a finished basement with a small home bar, shelves behind him",
     "bancada": "bar counter", "curto": "basement bar", "luz": "warm low light from a hanging lamp."},
    {"id": "sala_jantar",
     "set": "a dining room, a wooden sideboard and a plain wall behind him",
     "bancada": "sideboard", "curto": "dining room", "luz": "warm ceiling light."},
    {"id": "escritorio", "set": "a small home office, a bookshelf behind him",
     "bancada": "desk", "curto": "home office", "luz": "soft warm light from frame-left."},
    {"id": "galpao",
     "set": "a backyard tool shed, hand tools hanging on the wall behind him",
     "bancada": "shed bench", "curto": "tool shed", "luz": "hard daylight from frame-right."},
    {"id": "estufa",
     "set": "a backyard greenhouse, potted plants on shelves behind him",
     "bancada": "potting bench", "curto": "greenhouse", "luz": "bright diffused daylight."},
    # ⭐⭐ + 2026-08-13 — DOZE AMBIENTES NOVOS, ordem do operador: *"aumente o
    # pool de opcoes substancialmente, tambem dos ambientes"*. 12 -> 24.
    # ⛔ Cada entrada declara EXATAMENTE as mesmas quatro chaves das doze de
    # cima, e nenhuma e' opcional: o `curto` volta na cena 5 como "in the same
    # %s", a `bancada` volta no insert das maos e a `luz` entra duas vezes (uma
    # capitalizada, outra no meio da frase) — por isso toda `luz` nova comeca em
    # minuscula e termina em ponto, como as antigas.
    # ⚠️ Nenhuma repete superficie E luz de outra ao mesmo tempo: doze cozinhas
    # com nome diferente sao uma cozinha so', e era exatamente o vicio que o
    # operador mediu em 2026-08-01 no bloco acima.
    # ⛔ Escopo do D1 (P15) mantido nas doze: superficie de apoio em quadro e
    # fundo que nao compete com o rosto.
    # ⚠️ IDENTICO ao flagrante16_short.py — os dois nasceram por copia literal e
    # andam juntos; pool que diverge deixa de ter fonte da verdade.
    {"id": "despensa",
     "set": "a walk-in pantry, deep shelves of jars and tins behind him",
     "bancada": "pantry shelf", "curto": "pantry", "luz": "cool strip light from above."},
    {"id": "alpendre",
     "set": "the front porch of a house, a white rail and a rocking chair behind him",
     "bancada": "porch rail table", "curto": "front porch", "luz": "clear morning sun from frame-left."},
    {"id": "sala_estar",
     "set": "a living room, a sofa and framed family pictures on the wall behind him",
     "bancada": "console table", "curto": "living room", "luz": "warm lamp light from frame-right."},
    {"id": "deck",
     "set": "a raised backyard deck, a wooden rail and mown lawn behind him",
     "bancada": "deck bar", "curto": "backyard deck", "luz": "low golden light from frame-right."},
    {"id": "cozinha_fazenda",
     "set": "a farmhouse kitchen, open shelves and cast-iron pans hanging behind him",
     "bancada": "butcher block", "curto": "farmhouse kitchen", "luz": "broad daylight from a wide window behind the camera."},
    {"id": "marcenaria",
     "set": "a woodworking shop, clamps on a rack and stacked lumber behind him",
     "bancada": "assembly table", "curto": "wood shop", "luz": "flat light from a high skylight."},
    {"id": "pergola",
     "set": "a paved patio under a wooden pergola, a climbing vine overhead behind him",
     "bancada": "patio table", "curto": "patio", "luz": "dappled midday light through the slats."},
    {"id": "den",
     "set": "a wood-panelled den, framed photographs and a mantel behind him",
     "bancada": "sideboard cabinet", "curto": "den", "luz": "low warm light from a table lamp."},
    {"id": "cozinha_apartamento",
     "set": "a narrow galley kitchen in an apartment, tiled splashback and a fridge behind him",
     "bancada": "narrow counter", "curto": "galley kitchen", "luz": "flat even light from a single window."},
    {"id": "entrada",
     "set": "an entry hall, coat hooks and a tall mirror on the wall behind him",
     "bancada": "hall console", "curto": "entry hall", "luz": "soft daylight coming in through the open door."},
    {"id": "cabana",
     "set": "the main room of a lake cabin, log walls and a window onto open water behind him",
     "bancada": "plank table", "curto": "lake cabin", "luz": "clear light reflected up off the water."},
    {"id": "solarium",
     "set": "a glassed-in sunroom, wicker chairs and a garden beyond the panes behind him",
     "bancada": "wicker table", "curto": "sunroom", "luz": "bright diffused light through the glass."},
]

# F4b — contraste estrutural: o REF SEMPRE tem cabeleira farta, e' barbeado e
# nao usa oculos; a vitima e' SEMPRE careca, de bigode e de oculos. Assim os
# 3 eixos visiveis a' distancia nascem garantidos, sem depender de frase extra.
REFS = [
    {"idade": 66, "marca": "full silver hair and a notched left ear",
     "cabelo": "silver", "roupa": "Plain navy crew-neck tee shirt.",
     "roupa_curta": "navy tee shirt"},
    {"idade": 68, "marca": "thick white hair and a deep cleft in his chin",
     "cabelo": "white", "roupa": "Plain charcoal crew-neck tee shirt.",
     "roupa_curta": "charcoal tee shirt"},
    # ⛔ REESCRITA 2026-08-13 (era `a clean pale scar through his left eyebrow`):
    # ordem do operador *"melhore a aparencia e shape desses homens"*. Cicatriz
    # esta' do lado ⛔ da tabela — o gerador a le' como desgaste e devolve o
    # mendigo que ele reprovou no PLACA 16. A ancora vira uma mecha, que e'
    # igualmente permanente e igualmente distintiva, sem custo de aparencia.
    {"idade": 64, "marca": "full gray hair and a single silver streak running through his left eyebrow",
     "cabelo": "gray", "roupa": "Plain olive crew-neck tee shirt.",
     "roupa_curta": "olive tee shirt"},
    {"idade": 70, "marca": "thick silver hair and a prominent dark mole on his left cheekbone",
     "cabelo": "silver", "roupa": "Plain black crew-neck tee shirt.",
     "roupa_curta": "black tee shirt"},
    {"idade": 65, "marca": "full salt-and-pepper hair and a gold crown on one front tooth",
     "cabelo": "salt-and-pepper",
     "roupa": "Plain slate blue crew-neck tee shirt.",
     "roupa_curta": "slate blue tee shirt"},
    {"idade": 67, "marca": "thick gray hair swept back and a small notch in his right ear",
     "cabelo": "gray", "roupa": "Plain burgundy crew-neck tee shirt.",
     "roupa_curta": "burgundy tee shirt"},
    # + 2026-08-01: o operador viu o mesmo rosto de narrador voltando no lote.
    # Tres REFs novos, mesmo contraste estrutural do F4b (cabeleira, sem oculos).
    {"idade": 63, "marca": "a sharp widow's peak in thick white hair and a deep dimple in his left cheek",
     "cabelo": "white", "roupa": "Plain forest green crew-neck tee shirt.",
     "roupa_curta": "forest green tee shirt"},
    {"idade": 71, "marca": "iron gray hair cut in a flat-top and a cluster of dark freckles across his nose",
     "cabelo": "iron gray", "roupa": "Plain teal crew-neck tee shirt.",
     "roupa_curta": "teal tee shirt"},
    {"idade": 61, "marca": "full black hair streaked bright white at the front and a small gold hoop in his left ear",
     "cabelo": "black", "roupa": "Plain cream crew-neck tee shirt.",
     "roupa_curta": "cream tee shirt"},
    # + 2026-08-02: mesma medicao que gerou o bloco das VITIMAS logo abaixo, so'
    # que do lado do narrador — o operador viu SEMPRE O MESMO ROSTO. As nove
    # acima dizem cabelo + ancora e mais nada, entao o gerador recebia quase a
    # mesma frase e devolvia quase a mesma cara. As tres novas abrem o eixo
    # ZERADO deste pool: PORTE (compleicao), que nenhuma das nove menciona.
    #   · 74 — ombros largos e quadrados, cabelo aco repartido baixo.
    #   · 58 — armacao baixa e compacta, cabelo em cachos fechados.
    #   · 62 — armacao quadrada e possante, topete alto.
    #   · cabeleira farta, barbeado e sem oculos continua TRAVADO nas tres
    #     (F4b: sao os 3 eixos que separam o narrador da vitima a' distancia).
    #   · a ancora e' sempre do lado ✅ da tabela de licoes-producao-veo §REF —
    #     DISTINTIVO, NUNCA DETERIORADO (cicatriz limpa, mecha branca).
    #   · nenhuma repete ancora das VITIMAS deste arquivo, pelo mesmo motivo
    #     escrito la' embaixo: ancora repetida remenda o morphing que o F4b
    #     evita, e os dois aparecem lado a lado no mesmo IMAGE.
    #   · zero mencao a etnia: o motor injeta ETNIA[pagina] antes da marca.
    # ⛔ AS DUAS DE BAIXO FORAM REESCRITAS EM 2026-08-13, mesma ordem do
    # operador (*"melhore a aparencia e shape desses homens"*): traziam
    # `a raised white scar across the bridge of his nose` e `a small silver scar
    # splitting his upper lip`. O comentario de 2026-08-02 logo acima ja' dizia
    # "cicatriz limpa" como se fosse do lado ✅ — nao e'. Cicatriz no rosto puxa
    # o banco de imagem para o homem castigado; o PORTE (que era o ponto do
    # bloco) fica intacto nas duas, so' a ancora troca.
    {"idade": 74, "marca": "unusually broad square shoulders, thick steel gray hair parted low on one side and a small gold stud in his right earlobe",
     "cabelo": "steel gray", "roupa": "Plain mustard yellow crew-neck tee shirt.",
     "roupa_curta": "mustard yellow tee shirt"},
    {"idade": 58, "marca": "a short compact frame, a full head of tight coppery-brown curls and a beauty mark at the outer corner of his right eye",
     "cabelo": "curly", "roupa": "Plain sky blue crew-neck tee shirt.",
     "roupa_curta": "sky blue tee shirt"},
    {"idade": 62, "marca": "a square powerfully built frame, thick dark hair combed up into a high pompadour and one eyebrow gone completely white",
     "cabelo": "dark", "roupa": "Plain stone gray crew-neck tee shirt.",
     "roupa_curta": "stone gray tee shirt"},
    # + 2026-08-04: ampliacao por ordem do operador — *"aumente o pool de
    # personagens... faca isso para pelo menos outros 5 agentes shorts"*.
    # ⛔ Cada entrada difere das outras em >= 3 eixos fisicos (licoes §15):
    # contar entradas nao basta, o que conta e' quantos eixos elas acionam.
    {"idade": 58,
     "marca": "thick chestnut hair with a bright white streak at the left temple",
     "cabelo": "chestnut",
     "roupa": "Plain charcoal crew-neck tee shirt.",
     "roupa_curta": "charcoal tee shirt"},
    {"idade": 63,
     "marca": "a full head of wavy steel-grey hair and a cleft chin",
     "cabelo": "steel-grey",
     "roupa": "Plain olive crew-neck tee shirt.",
     "roupa_curta": "olive tee shirt"},
    {"idade": 55,
     "marca": "dense dark hair swept back and very pale blue eyes",
     "cabelo": "dark",
     "roupa": "Plain rust-red crew-neck tee shirt.",
     "roupa_curta": "rust-red tee shirt"},
    # ⛔ REESCRITA 2026-08-13 (era `a broad flattened nose`): "achatado" e' a
    # mesma imagem que `broken nose`, que esta' na lista proibida — o gerador
    # nao le' a diferenca entre descrever e depreciar. A arquitetura facial fica
    # (o nariz continua sendo o eixo), so' o adjetivo de dano sai.
    {"idade": 61,
     "marca": "a thick grey afro worn low and a broad straight nose with a wide bridge",
     "cabelo": "grey",
     "roupa": "Plain slate-blue crew-neck tee shirt.",
     "roupa_curta": "slate-blue tee shirt"},
    {"idade": 68,
     "marca": "a full head of white hair combed sideways and a long thin face",
     "cabelo": "white",
     "roupa": "Plain sand crew-neck tee shirt.",
     "roupa_curta": "sand tee shirt"},
    {"idade": 59,
     "marca": "salt-and-pepper locs gathered back and deep-set dark eyes",
     "cabelo": "salt-and-pepper",
     "roupa": "Plain forest-green crew-neck tee shirt.",
     "roupa_curta": "forest-green tee shirt"},
    # ⭐⭐ + 2026-08-13 — OITO NARRADORES NOVOS, ordem do operador: *"melhore a
    # aparencia e shape desses homens"* / *"aumente o pool de opcoes
    # substancialmente"*. 18 -> 26.
    # ⛔ ZERO palavra de aprovacao (`handsome`, `rugged`, `chiseled`, `strong
    # jaw`, `piercing eyes`): elogio no prompt puxa o rosto para a media do
    # banco de imagem, que e' o mesmo mecanismo pelo qual dizer "not a
    # celebrity" invoca a celebridade. O que entra e' FEICAO, nunca julgamento.
    # ⛔ ZERO ancora deteriorada — nada de cicatriz, dente lascado, pele
    # castigada, olho fundo ou vinco entre as sobrancelhas. As ancoras saudaveis
    # daqui: sobrancelha cheia e reta, linhas de riso, mecha branca na tempora,
    # sarda no malar, covinha de um lado so', beleza-marca abaixo da orelha,
    # olhos claros bem separados, malar alto.
    # ⛔ ZERO cor de pele e zero etnia: quem injeta e' `ETNIA[pagina]` antes da
    # marca. O que entra e' TEXTURA (`smooth even skin`, `lightly tanned`,
    # `light freckles`), que e' saudavel e nao briga com a etnia da pagina.
    # ⚠️ EIXO `OCULOS` FICA EM 0% AQUI DE PROPOSITO, e a excecao e' o F4b: o
    # narrador e' cabeleira + barbeado + SEM oculos, a vitima e' careca + bigode
    # + COM oculos. Sao os tres eixos que sobrevivem ao plano medio e separam os
    # dois no mesmo quadro. Quem carrega os oculos neste motor e' a VITIMA
    # (100%) e a MULHER (~27%) — nao o narrador.
    # ⚠️ Cada entrada aciona PORTE + CABELO + ANCORA (e cinco delas, PELE):
    # contar entradas nao basta, o que conta e' quantos eixos elas mexem.
    # ⚠️ IDENTICO ao flagrante16_short.py — motores irmaos andam juntos.
    {"idade": 66,
     "marca": "a tall broad-chested frame, a thick sandy-blond mane pushed straight back and heavy level brows",
     "cabelo": "sandy-blond",
     "roupa": "Plain indigo crew-neck tee shirt.",
     "roupa_curta": "indigo tee shirt"},
    {"idade": 57,
     "marca": "a lean upright build, thick dark hair with a patch of white above his left temple and smooth even skin",
     "cabelo": "dark",
     "roupa": "Plain brick red crew-neck tee shirt.",
     "roupa_curta": "brick red tee shirt"},
    {"idade": 69,
     "marca": "a heavy barrel-chested build, a full head of loose white waves and laugh lines that frame a wide easy smile",
     "cabelo": "white",
     "roupa": "Plain moss green crew-neck tee shirt.",
     "roupa_curta": "moss green tee shirt"},
    {"idade": 60,
     "marca": "a broad-shouldered athletic frame, close-cropped silver hair over a low straight hairline and light freckles across both cheekbones",
     "cabelo": "silver",
     "roupa": "Plain denim blue crew-neck tee shirt.",
     "roupa_curta": "denim blue tee shirt"},
    {"idade": 72,
     "marca": "a long-limbed rangy build, thick ash-gray hair combed to the right and a dimple in his right cheek only",
     "cabelo": "ash-gray",
     "roupa": "Plain plum crew-neck tee shirt.",
     "roupa_curta": "plum tee shirt"},
    {"idade": 56,
     "marca": "a solid square-set build, dense light-brown hair with a deep side part, wide-set green eyes and lightly tanned even skin",
     "cabelo": "light-brown",
     "roupa": "Plain ochre crew-neck tee shirt.",
     "roupa_curta": "ochre tee shirt"},
    {"idade": 64,
     "marca": "a trim upright frame, thick iron-grey hair in a short brush cut and a small dark beauty spot just below his left ear",
     "cabelo": "iron-grey",
     "roupa": "Plain terracotta crew-neck tee shirt.",
     "roupa_curta": "terracotta tee shirt"},
    {"idade": 70,
     "marca": "a deep-chested build heavy through the shoulders, thick snow-white hair long enough to touch the collar, high wide cheekbones and amber-brown eyes",
     "cabelo": "snow-white",
     "roupa": "Plain steel blue crew-neck tee shirt.",
     "roupa_curta": "steel blue tee shirt"},
]

VITIMAS = [
    {"idade": 63, "marca": "bald man with a thick gray mustache and black-framed glasses, smooth-skinned"},
    {"idade": 62, "marca": "bald man with a red mustache and wire-rimmed glasses"},
    {"idade": 65, "marca": "bald man with a white mustache and thick square glasses, lightly tanned"},
    {"idade": 64, "marca": "bald man with a gray fringe above his ears, a bushy mustache and glasses"},
    {"idade": 61, "marca": "bald man with a short gray mustache and round wire glasses, freckled across the nose"},
    # + 2026-08-01: o operador viu o mesmo rosto de vitima voltando no lote.
    # Cinco novas, todas carecas de bigode e oculos (F4b).
    {"idade": 66, "marca": "bald man with a horseshoe mustache and heavy tortoiseshell glasses"},
    {"idade": 59, "marca": "bald man with a thin pencil mustache and gold aviator glasses, laugh lines at the eyes"},
    {"idade": 67, "marca": "bald man with a bushy salt-and-pepper mustache and half-rim glasses"},
    {"idade": 68, "marca": "bald man with a drooping gray walrus mustache and rimless glasses, smooth-skinned"},
    {"idade": 70, "marca": "bald man with a white handlebar mustache and small oval glasses"},
    # + 2026-08-02: o operador mediu o pool inteiro e viu a MESMA vitima
    # voltando — as 10 acima variam bigode e oculos e mais nada, entao o
    # gerador recebia quase a mesma frase e devolvia quase o mesmo rosto.
    # As seis novas trazem os dois eixos zerados aqui: PORTE (compleicao) e
    # PELE (textura de idade), mais uma ANCORA FACIAL permanente (P6) que faz
    # o rosto voltar igual nas cenas 1 e 4.
    #   · careca + bigode + oculos continua TRAVADO nas seis (F4b: sao os 3
    #     eixos que sobrevivem ao plano medio e separam a vitima do narrador).
    #   · a ancora e' sempre do lado ✅ da tabela de licoes-producao-veo
    #     §REF — DISTINTIVO, NUNCA DETERIORADO (mecha branca, cicatriz limpa,
    #     sinal de nascenca, pinta). ⛔ dente lascado, palpebra caida e nariz
    #     quebrado ficaram de fora: viram mendigo e matam a credibilidade.
    #   · nenhuma repete ancora dos REFS deste arquivo — orelha entalhada,
    #     covinha/fenda no queixo, cicatriz na sobrancelha, pinta na maca do
    #     rosto, coroa de ouro, sardas no nariz, argola na orelha. Ancora
    #     repetida entre narrador e vitima remenda o morphing que o F4b evita.
    #   · zero mencao a etnia/cor: o motor injeta ETNIA[pagina] antes da marca.
    {"idade": 58, "marca": "bald man, heavy-set and round-faced, with a chevron mustache streaked white on the left side and thick-lensed glasses, lightly tanned"},
    # ⛔⛔ AS TRES DE BAIXO FORAM REESCRITAS EM 2026-08-13. Ordem do operador:
    # *"melhore a aparencia e shape desses homens"* — e a vitima e' homem em
    # quadro tambem, no MESMO IMAGE que o narrador. Elas traziam `thin and
    # deeply lined`, `tall and bony`, `a clean scar across his scalp`, `stocky
    # and sun-weathered` e `a clean scar along his right jawline`: cinco itens
    # do lado ⛔ da tabela, e juntos entregam o mendigo que o operador reprovou
    # no PLACA 16. ⭐ O que a cena precisa da vitima e' HUMILHACAO (cabeca
    # baixa, ombros caidos, boca fechada), e isso ja' esta' no TAKE — nao no
    # rosto. Vitima castigada nao aumenta a dor: derruba a credibilidade do
    # video inteiro, porque o espectador nao se ve' nela.
    # ⚠️ O F4b fica intacto nas tres (careca + bigode + oculos) e o PORTE, que
    # era o ponto do bloco de 2026-08-02, tambem — so' o dano sai.
    {"idade": 72, "marca": "bald man, lean and long-faced, with a dark mole beside his mouth, a sparse white mustache and half-moon glasses"},
    {"idade": 60, "marca": "bald man, short and barrel-chested, with a coin-sized dark birthmark on his crown, a bristly steel-gray mustache and boxy clear-framed glasses, freckled across the nose"},
    {"idade": 69, "marca": "bald man, tall and narrow-shouldered, with a wide flat brow, a close-cropped charcoal mustache and narrow rectangular glasses on a beaded cord"},
    {"idade": 57, "marca": "bald man, stocky and thick-necked, with a squared-off chin and a wide mouth, a wide brush mustache and heavy black-framed bifocal glasses, laugh lines at the eyes"},
    {"idade": 71, "marca": "bald man, broad-shouldered and heavy through the middle, with a dark birthmark at his left temple, a full silver mustache and clip-on shades over his glasses"},
]

MULHERES = [
    {"idade": 58, "hook": "woman with chin-length wavy hair",
     "payoff": "with chin-length wavy hair, in a red dress"},
    {"idade": 59, "hook": "woman with long straight hair and pearl earrings",
     "payoff": "with long straight hair, in a navy wrap dress"},
    {"idade": 57, "hook": "woman with short curly hair and a beauty mark on her jaw",
     "payoff": "with short curly hair, in an emerald dress"},
    {"idade": 60, "hook": "woman with shoulder-length hair pinned back",
     "payoff": "with shoulder-length hair, in a burgundy dress"},
    {"idade": 56, "hook": "woman with braided hair gathered over one shoulder",
     "payoff": "with braided hair over one shoulder, in a coral dress"},
    # + 2026-08-01: o operador viu a mesma mulher voltando no lote. Cinco
    # novas, dobrando o pool.
    {"idade": 61, "hook": "woman with a silver bob and long dangling earrings",
     "payoff": "with a silver bob, in a plum dress"},
    {"idade": 62, "hook": "woman with cropped gray hair and thick hoop earrings",
     "payoff": "with cropped gray hair, in a jade green dress"},
    {"idade": 54, "hook": "woman with a thick low bun and a mole above her lip",
     "payoff": "with a low bun, in a black dress"},
    {"idade": 63, "hook": "woman with tight gray curls and reading glasses pushed up on her head",
     "payoff": "with tight gray curls, in a lilac dress"},
    {"idade": 64, "hook": "woman with a blunt shoulder-length cut and a white streak at her temple",
     "payoff": "with a blunt shoulder-length cut, in a champagne gold dress"},
    # + 2026-08-02: mesma medicao que gerou os blocos dos REFS e das VITIMAS
    # acima, so' que do lado da mulher — o operador viu SEMPRE O MESMO ROSTO.
    # As dez acima descrevem a pessoa por CABELO mais um brinco: dez mulheres
    # descritas so' por cabelo sao a mesma mulher dez vezes, e o gerador
    # devolvia quase a mesma cara. As sete novas trazem os eixos rasos daqui:
    #   · PORTE — tall straight-backed, broad shoulders, thin wiry.
    #   · OCULOS — thick round, narrow reading, gold-rimmed em correntinha.
    #   · PELE — sardas de sol.
    #   · ANCORA FACIAL permanente (P6) em todas, e a MESMA nos dois campos:
    #     o `hook` e o `payoff` sao a cena 1 e a cena 4 da mesma mulher, e a
    #     ancora repetida e' o que faz o rosto voltar igual la' na frente.
    #   · a ancora e' sempre do lado ✅ de licoes-producao-veo §REF —
    #     DISTINTIVO, NUNCA DETERIORADO (cicatriz limpa, pinta, covinha,
    #     sinal de nascenca, dente separado). ⛔ dente lascado ficou de fora.
    #   · nenhuma repete ancora dos REFS nem das VITIMAS deste arquivo: os
    #     tres aparecem no mesmo quadro e ancora identica remenda o morphing
    #     que o F4b evita.
    #   · zero mencao a etnia: o motor injeta ETNIA[pagina] antes da marca.
    # ⛔ REESCRITA 2026-08-13 (era `a fine scar through her left eyebrow`, nos
    # DOIS campos): mesma ordem do operador que reescreveu os homens acima.
    # A ancora tinha de trocar nos dois campos ao mesmo tempo — `hook` e
    # `payoff` sao a cena 1 e a cena 4 da MESMA mulher, e ancora que so' troca
    # de um lado e' rosto que muda no meio do video.
    {"idade": 52,
     "hook": ("woman with dark hair in a high twisted knot, a tall "
              "straight-backed frame and heavy level brows over wide dark eyes"),
     "payoff": ("with dark hair in a high twisted knot and heavy level brows "
                "over wide dark eyes, in a forest green dress")},
    {"idade": 69,
     "hook": ("woman with white hair combed straight back, thick round glasses "
              "and a dark mole beside her nostril"),
     "payoff": ("with white hair combed straight back, thick round glasses and "
                "a dark mole beside her nostril, in a teal cardigan")},
    {"idade": 66,
     "hook": ("woman with a thin white braid down her back, narrow reading "
              "glasses low on her nose and a deep dimple in her right cheek"),
     "payoff": ("with a thin white braid down her back, narrow reading glasses "
                "and a deep dimple in her right cheek, in a mustard blouse")},
    # ⛔⛔ REESCRITA 2026-08-13 (era `a gap between her front teeth`, nos dois
    # campos): dente nunca e' ancora — e' a regiao que o gerador mais exagera, e
    # o CLEAN ja' pagou essa licao com foto de campo (CL25: `gap` virou dente
    # faltando). O eixo que a entrada trazia era o PORTE (ombros largos), e ele
    # fica; a ancora vai para a boca, que o plano medio ainda le' e que
    # nenhum REF nem VITIMA deste arquivo usa (ancora repetida entre as tres
    # pessoas do mesmo quadro remenda justamente o morphing que o F4b evita).
    {"idade": 53,
     "hook": ("woman with a heavy gray-streaked ponytail, broad shoulders and "
              "a pronounced Cupid's bow and a full lower lip"),
     "payoff": ("with a heavy gray-streaked ponytail, a pronounced Cupid's bow "
                "and a full lower lip, in a denim shirt dress")},
    {"idade": 68,
     "hook": ("woman with wispy silver hair in a loose bun, gold-rimmed "
              "glasses on a beaded chain and sun freckles across her cheeks"),
     "payoff": ("with wispy silver hair in a loose bun, gold-rimmed glasses "
                "and freckled cheeks, in a rose-pink cardigan")},
    {"idade": 65,
     "hook": ("woman with a tight iron-gray perm, heavy dark brows and a small "
              "birthmark high on her right cheek"),
     "payoff": ("with a tight iron-gray perm and a small birthmark high on her "
                "right cheek, in a copper dress")},
    # ⛔ REESCRITA 2026-08-13 (era `a sharply hooked nose`, nos dois campos):
    # nariz adunco nao esta' na lista de proibidos ao pe' da letra, mas e' a
    # mesma familia — o gerador o le' como caricatura de velhice e devolve
    # exatamente o rosto que o operador reprovou. A arquitetura do nariz
    # continua sendo a ancora; sai so' o adjetivo que deprecia.
    {"idade": 67,
     "hook": ("woman with a thick gray shag cut, a thin wiry build and a "
              "long straight nose with a fine bridge"),
     "payoff": ("with a thick gray shag cut, a thin wiry build and a long "
                "straight nose with a fine bridge, in an ivory blouse")},
    # ⭐⭐ + 2026-08-13 — NOVE MULHERES NOVAS, ordem do operador: *"aumente o
    # pool de opcoes substancialmente"*. 17 -> 26.
    # ⛔ A ANCORA E' A MESMA NOS DOIS CAMPOS, sempre: `hook` e' a cena 1 e
    # `payoff` e' a cena 4 da MESMA mulher. Ancora que so' aparece de um lado e'
    # rosto que troca no meio do video (P6).
    # ⛔ Nenhuma ancora daqui repete ancora dos REFS nem das VITIMAS deste
    # arquivo: os tres aparecem no MESMO quadro e ancora identica remenda o
    # morphing que o F4b existe para evitar.
    # ⛔ Zero deterioracao (sem cicatriz, sem dente, sem pele castigada, sem
    # nariz adunco) e zero cor de pele — a etnia entra por `ETNIA[pagina]` antes
    # da descricao. O que varia de textura e' saudavel: sardas, pele lisa,
    # levemente bronzeada.
    # ⚠️ TRES DAS NOVE USAM OCULOS, de proposito: com as quatro que ja' havia o
    # eixo fecha em 7 de 26 (~27%), que e' a faixa pedida. E' aqui que o eixo
    # `oculos` gira neste motor — no narrador ele e' 0% por causa do F4b.
    # ⚠️ Cada entrada mexe em PORTE + CABELO + ANCORA; seis delas trazem porte
    # explicito, que era o eixo mais raso do pool antigo.
    {"idade": 55,
     "hook": ("woman with a sleek dark chignon, a tall slender frame and high "
              "arched brows"),
     "payoff": ("with a sleek dark chignon and high arched brows, in a "
                "sapphire blue dress")},
    {"idade": 51,
     "hook": ("woman with long honey-brown hair loose past her shoulders, a "
              "full figure and a small gold stud in her left nostril"),
     "payoff": ("with long honey-brown hair loose past her shoulders and a "
                "small gold stud in her left nostril, in a terracotta wrap "
                "dress")},
    {"idade": 70,
     "hook": ("woman with soft white hair set in short waves, burgundy cat-eye "
              "glasses and a shallow cleft in her chin"),
     "payoff": ("with soft white hair set in short waves, burgundy cat-eye "
                "glasses and a shallow cleft in her chin, in a dove grey "
                "dress")},
    {"idade": 50,
     "hook": ("woman with a thick dark bob and a blunt fringe, a petite frame, "
              "smooth clear skin and almond-shaped hazel eyes"),
     "payoff": ("with a thick dark bob and a blunt fringe and almond-shaped "
                "hazel eyes, in an olive green dress")},
    {"idade": 71,
     "hook": ("woman with fine white hair pinned in a French twist, a small "
              "round frame and a beauty mark below her right eye"),
     "payoff": ("with fine white hair pinned in a French twist and a beauty "
                "mark below her right eye, in a chocolate brown dress")},
    {"idade": 72,
     "hook": ("woman with silver hair in a short bob with a deep side part, "
              "oversized amber-tinted glasses and laugh lines around a wide "
              "open smile"),
     "payoff": ("with silver hair in a short bob with a deep side part, "
                "oversized amber-tinted glasses and laugh lines around a wide "
                "open smile, in a wine-red blouse")},
    {"idade": 58,
     "hook": ("woman with long auburn hair pinned back on one side, a sturdy "
              "broad-shouldered build, lightly tanned skin and a strong low "
              "hairline over a broad forehead"),
     "payoff": ("with long auburn hair pinned back on one side and a strong "
                "low hairline over a broad forehead, in a turquoise dress")},
    {"idade": 62,
     "hook": ("woman with tight silver-white coils cut close to the head, "
              "black cat-eye glasses and a dimple that shows only on the left"),
     "payoff": ("with tight silver-white coils cut close to the head, black "
                "cat-eye glasses and a dimple that shows only on the left, in "
                "a cream linen dress")},
    {"idade": 66,
     "hook": ("woman with a thick chestnut braid coiled at the nape, a slim "
              "upright frame and pale grey eyes under dark lashes"),
     "payoff": ("with a thick chestnut braid coiled at the nape and pale grey "
                "eyes under dark lashes, in a dusty pink dress")},
]

# ---------------------------------------------------------------------------
# POOLS DE COPY — o molde e' sorteado, a frase cha' vence sempre (arsenal)
# ---------------------------------------------------------------------------

NUCLEO = ["Johnson", "pecker", "wiener", "tool", "soldier"]

HOOKS = [
    "Everyone at {evento} had already heard the gossip that his {o} doesn't work anymore. His hangs just like this.",
    "The whole {evento} had heard the gossip that his {o} quit on him. His hangs just like this.",
    "Every man at {evento} had heard the gossip that his {o} can't stand up anymore. His hangs like this.",
    "Word got around {evento} that his {o} doesn't work anymore. His hangs just like this.",
    "Every guy at {evento} had heard the gossip that his {o} can't finish anymore. She knows it. His hangs down like this.",
    "Half the people at {evento} had heard the gossip that his {o} can't get hard anymore. His hangs over his own fingers.",
    "The women at {evento} had already heard the gossip that his {o} stopped working. His wife told them. His droops like this.",
    "Nobody at {evento} was surprised. They'd heard the gossip that his {o} hasn't worked in two years. His stays down like this.",
    "Every husband at {evento} had heard the gossip that his {o} quit and his wife stopped asking. His stays folded like this.",
    "Everybody at {evento} heard the gossip that his {o} went dead on him. I was that man. His curls over his thumb.",
    "His crew at {evento} heard the gossip that his {o} gave out on him. Mine did too. His sinks into his lap.",
    "Neighbors at {evento} heard the gossip that his {o} went soft. I stopped reaching for my wife. His sags off his fingers.",
    "Cousins at {evento} heard the gossip that his {o} shut down. That was me at sixty. His hides in his own fist.",
]

QUEM_CONTOU = [
    "his own brother", "his brother-in-law", "a guy from the shop",
    "his fishing buddy", "his business partner", "the neighbor",
    "an old army friend", "his own son-in-law",
    # + 2026-08-01: o operador mediu vicio — sempre as mesmas bocas contando
    # o segredo no lote. Quatro fontes novas.
    "his barber", "a man from his church", "his old boss", "his cousin",
]

# ⛔ 2026-08-03 — FRASE ORFA. O operador leu um take renderizado e reprovou:
# "It isn't age. The blood flow got choked off." -> "deveria ser: it isn't age
# THAT'S CAUSING YOUR JOHN-SON NOT WORKING ANYMORE. Voce tem que contextualizar
# mais as coisas. Ta' deixando o viewer sem entender o contexto e do que se
# trata." O espectador ouvia fisiologia solta e so' descobria o assunto na
# ULTIMA frase — e o operador reprovou exatamente essa cena, com o orgao la'.
# ⭐ REGRA NOVA: toda frase que nomeia uma CAUSA carrega, NA MESMA FRASE, o que
#    ela quebra. Nao vale "aparece em algum lugar da cena".
#      certo:  "It isn't age that's got your {o} quitting."
#      errado: "It isn't age." / "The blood flow got choked off."
# Tres entradas deste pool tinham a causa numa frase e o alvo em outra (as de
# indice 2, 3 e 11 — as unicas do motor inteiro, medidas por varredura do pool,
# nao por sorteio). Consertadas abaixo. As demais ja' nasceram com causa e alvo
# na mesma frase e NAO foram tocadas: string validada e' constante.
# ⚠️ O alvo ENGORDA a frase e o teto da cena 2 e' 30 palavras. Onde nao coube,
#    encurtou-se OUTRA coisa da mesma entrada (o vocativo "brother", o dedo
#    "Right here") — nunca se subiu o teto nem se devolveu a frase vaga.
#    Pior caso medido depois: 29, 26 e 29 palavras.
# ⚠️ Pessoa mantida como a frase ja' usava (`your {o}`): estas falam com o
#    espectador. Terceira pessoa nao e' o defeito — o que se cobra e' REFERENTE.
# ⛔⛔ REVISAO 2026-08-03 — a [3] foi consertada DUAS vezes. A primeira tentativa
#    trocou "It's not your age, brother, and it's not you. The blood stopped
#    reaching your {o}." por "...and it's not you, the blood stopped reaching
#    your {o}.": apagou o vocativo e trocou o PONTO por VIRGULA. O medidor de
#    frase orfa zerou — ele corta a fala em [.!?] — mas o espectador ouvia
#    exatamente as mesmas palavras (95% identicas), com o alvo so' na palavra 14
#    de 15 da frase de causa. Medido: reescrever "." por "," nas 3 orfas do HEAD
#    zera o medidor sem acrescentar UMA palavra. O medidor mede pontuacao.
# ⭐ O aceite nao e' "a lente zerou": e' o ALVO PRESO A CAUSA pela oracao
#    relativa, como o operador escreveu ("it isn't age THAT'S CAUSING YOUR
#    JOHN-SON..."). Na [2] o alvo cai na palavra 9/9, na [11] na 8/9 e agora na
#    [3] na 8/11 — e nao na 14/15 atras de uma virgula.
DESCOBERTAS = [
    "That's when {quem} pulled him aside and gave him the gelatin trick. It's not age, brother, the blood flow to your {o} got choked off.",
    "That's when {quem} handed him the gelatin trick. It's not age, brother, your {o} got its blood flow choked off.",
    "That's when {quem} gave him the gelatin trick. It isn't age that's got your {o} quitting. The blood flow down there got choked off.",
    "That's when {quem} leaned over and whispered the gelatin trick. It's not your age that's starving your {o}, it's the blood.",
    "That's when {quem} finally told him about the gelatin trick. Your wife isn't bored, brother, and you're not done. The blood stopped filling your {o}.",
    "I laughed at the gelatin trick the first time. {quem} wouldn't let him laugh. Give it two days, brother, and the blood finds your {o} again.",
    "{quem} passed him the gelatin trick in a parking lot. Every man I know over sixty is on it now. The blood has to reach your {o}.",
    # + 2026-08-01: o operador mediu vicio — toda descoberta do lote abria em
    # "That's when" e chamava o cara de "brother". As novas nao fazem nenhum dos dois.
    "One night {quem} wrote the gelatin trick down for him on a napkin. The blood flow to your {o} got choked off.",
    "No doctor told him about the gelatin trick. It came from {quem}. The blood flow to your {o} got choked off.",
    "Two days later {quem} sent him the gelatin trick. The blood flow to your {o} got choked off, and it is fixable.",
    "It was {quem} who handed him the gelatin trick. The blood stopped reaching your {o}, and nobody tells you that.",
    "Same week, {quem} showed him the gelatin trick. It was never age that stopped your {o}. Down there, the blood flow got choked off.",
]

RITUAIS = [
    "That same night he stirred it into a glass and drank it. Stir it, drink it, give your {o} one week.",
    "That same night he stirred it into a glass and drank it. Do it tonight, before your {o} quits for good.",
    "That same night he mixed it into a glass and drank it. Stir it, drink it, and watch your {o} wake up.",
    "That same night he stirred it into a glass and drank it. Do it tonight and stop apologizing for your {o}.",
    "That same night he stirred it into a glass and drank it. She never saw. Do it tonight for your {o}.",
    "This is what we do at my house. One glass, one spoon, before bed. Stir it tonight and let your {o} answer.",
    "I drank mine standing at the sink so nobody would ask. He did the same. Stir it tonight, your {o} is waiting.",
    "He mixed his glass alone. Us guys do it after the house goes quiet. Stir yours tonight, before your {o} forgets how.",
    "Nobody in my house buys those pills anymore. He stirred his that night. Stir yours tonight and stop guessing about your {o}.",
    "First night I drank mine, I sat on the bed waiting. Stir yours tonight and give your {o} the same chance.",
    # + 2026-08-01: o operador mediu vicio — todo ritual do lote abria em
    # "That same night". As cinco novas trocam a abertura.
    "One glass of water, one spoon, one minute. He did it that night. Do it tonight for your {o}.",
    "He didn't wait. He stirred his glass that night. Stir yours tonight and watch what your {o} does.",
    "Warm water, one spoon, straight down. That's the whole thing. Give your {o} one week of it.",
    "My wife thinks mine is for my knees. Stir it tonight and your {o} gets the message.",
    "Takes about a minute. He's done it every night since. Start yours tonight, before your {o} quits.",
]

BRAGGING = ["telling that story", "bragging", "spreading the gossip herself",
            # + 2026-08-01: o operador mediu vicio — tres verbos so' pro lote
            # inteiro, o mesmo voltando toda hora. Cinco novos.
            "talking", "boasting", "going on", "crowing", "carrying on"]

# Cada fecho derruba UMA barreira do avatar (espinha-fixa §loop cena 4)
BARREIRAS = [
    "Nobody has to know but her.",
    "No doctor, no pharmacy counter.",
    "You do it in your own kitchen, in about a minute.",
    "Costs less than a cup of coffee.",
    "You never say the words out loud to anybody.",
    "Nothing to fill, nothing to explain.",
]

REDENCOES = [
    "Nineteen days later, {eco}. She wouldn't get off his knee, and now she's the one {brag} about his {o}. {barreira}",
    "Nineteen days later, {eco}. She stayed on his knee all night, and now she's the one {brag} about his {o}. {barreira}",
    "Nineteen days later, {eco}. The same men who laughed asked him what he was taking. She just kept {brag} about his {o}. {barreira}",
    "Nineteen days later, {eco}. They showed up an hour late because she wouldn't let him out of the bedroom. Now she's the one {brag} about his {o}. {barreira}",
    "Nineteen days later, {eco}. The same women who whispered about him now hear her {brag} about his {o} instead. {barreira}",
    "Nineteen days later, {eco}. This time his {o} stood up before she was even ready, and she's still {brag} about it. {barreira}",
    "Nineteen days later, {eco}. She's the one reaching for him at six in the morning now, and the one {brag} about his {o}. {barreira}",
    "Nineteen days later, {eco}. Mine came back the same way at sixty-five. She hasn't stopped {brag} about his {o} since. {barreira}",
    "Nineteen days later, {eco}. My wife locked our bedroom door at seven in the morning once. Now his wife is {brag} about his {o} to her sisters. {barreira}",
    # + 2026-08-01: o operador mediu vicio — a virada do lote sempre contada
    # com as mesmas duas imagens. Tres fechos novos, mais curtos.
    "Nineteen days later, {eco}. She never left his side, {brag} about his {o}. {barreira}",
    "Nineteen days later, {eco}. Nobody laughed this time, and they heard her {brag} about his {o}. {barreira}",
    "Nineteen days later, {eco}. She sat right down on him, {brag} about his {o}. {barreira}",
]

GATES = [
    "Follow me first, brother.",
    "Follow me first or I can't find your comment.",
    "Hit follow first, or Facebook won't deliver it.",
    # + 2026-08-01: o operador mediu vicio — "brother" caindo em todo CTA do
    # lote, porque o pool tinha 3 gates e um deles era vocativo.
    # ⛔ REGRA NOVA: no maximo 2 entradas deste pool com o vocativo "brother",
    # e a MAIORIA sem vocativo nenhum. Vale para toda expansao futura.
    "Follow me first.",
    "Hit follow before you comment.",
    "I only answer people who follow me.",
    "Facebook won't let me message you unless you follow.",
    "Follow first, I get too many comments to chase.",
    "Give me a follow, or your comment gets buried.",
    "Tap follow first, man, or I lose you.",
    "Follow me first, my friend, or I never see it.",
]

CTAS = [
    # ⭐ Alternativa pedida pelo operador em 2026-07-31, vista em campo:
    # a promessa e' A RECEITA, nao "o que eu uso" nem "onde eu compro".
    # E' a mais direta do pool e a unica que casa com a keyword RECIPE
    # que o Veo Editor ja' destaca na legenda.
    "Comment gelatin, and I'll send you the recipe tonight. {gate}",
    "Comment gelatin, and I'll send you the only one I trust tonight. {gate}",
    "Comment gelatin, and I'll send you that exact one today. {gate}",
    "Comment gelatin, and I'll send you the real source. The stuff on store shelves is watered-down powder. {gate}",
    "Comment gelatin, and I'll send it over tonight, so you never have to apologize in the dark again. {gate}",
    "Comment gelatin, and I'll send you the exact one he used. It shows up in a plain box. {gate}",
    "Comment gelatin, and I'll send you the one he got. Nineteen days from tonight, brother. {gate}",
    "Comment gelatin, and I'll send you what we pass around here, brother. Nobody outside this comment section finds out. {gate}",
    "Comment gelatin, and I'll send you the same one a man sent me at sixty-four. I didn't ask twice. {gate}",
    "Comment gelatin, and I'll send you the exact one. I typed it myself once, brother, and nobody in my house ever knew. {gate}",
    # + 2026-08-01: o operador mediu vicio — "brother" em quase todo CTA do
    # lote e sempre a mesma promessa. Quatro novos, nenhum com vocativo.
    "Comment gelatin, and the recipe goes out to you tonight. {gate}",
    # ⚠️ 2026-08-01 — auditoria de drifting. Era o UNICO CTA do pool cujo objeto
    # era um possessivo nu, sem substantivo em lugar nenhum da frase. E pior que
    # o buraco era a COLISAO DE ANTECEDENTE: 4 das 13 fundidas fecham a cena 2
    # em `she's {brag} about his.`, onde `his` e' o ORGAO — em ~31% dos sorteios
    # o espectador ouvia "about his [pecker]" e, 8 segundos depois, "where he
    # got his". A ultima frase do video virava piada involuntaria.
    # ⛔ E gastava 100% do folego em endereco de compra, contra a posicao do
    # operador escrita no cabecalho deste pool: a promessa e' A RECEITA.
    "Comment gelatin, and I'll send you the recipe and where he got the "
    "powder. {gate}",
    "Comment gelatin, and it's in your messages in ten minutes. {gate}",
    "Comment gelatin, and nobody else sees what I send you. {gate}",
]


# ---------------------------------------------------------------------------
# TABELAS DE TOKEN BANIDO — o linter do SHORT as le por `short_comum.lint_curto`
# ---------------------------------------------------------------------------

BANIDOS_TAKE = {
    "stiff": "adjetivo de estado em prompt de movimento derruba o video",
    "limp": "idem",
    "sags": "idem",
    "pulse": "tumescencia — IMAGE passa e o VIDEO e' recusado",
    "throb": "idem",
    "swelling": "idem",
    "engorged": "vocabulario anatomico — recusa",
    "geoduck": "so' no IMAGE; no TAKE usar 'the clam'",
    "neck": "no geoduck e' 'siphon', nunca 'neck'",
}

BANIDOS_IMAGE = {
    "large": "adjetivo nao dimensiona — o Veo normaliza",
    "big": "idem", "huge": "idem",
    "engorged": "vocabulario anatomico — recusa", "veins": "idem",
}

BANIDOS_GLOBAL = {
    "the victim": "rotulo que significa dano — municao pro classificador",
    "the narrator": "trocar por relacao nomeada",
}

BANIDOS_CTA = {"BOOK": "quebra a automacao DM", "YES": "quebra a automacao DM"}


# ---------------------------------------------------------------------------
# HELPERS E ARCO DE CINCO CENAS
# ---------------------------------------------------------------------------

def _palavras(txt):
    return len(re.findall(r"[A-Za-z']+", txt))


def _hook_fmt(hook, oc, o):
    """Formata o hook resolvendo a CONCORDANCIA do `{evento}`.

    ⚠️ BUG DE PRODUCAO, achado na auditoria de drifting de 2026-08-01.
    Os 14 `plateia_evento` comecam com "that" (`that wedding`, `that cookout`),
    porque 12 dos 13 hooks poem o `{evento}` depois de preposicao — `at
    {evento}`, `around {evento}` — e ali o demonstrativo e' o que faz a frase
    soar de boca, nao de folheto.

    O 13o hook poe o `{evento}` como NUCLEO DO SUJEITO ("The whole {evento}
    had heard...") e a mesma string vira "The whole THAT wedding had heard" —
    agramatical, e o Veo NARRA o erro em voz alta nos 2 segundos que decidem o
    scroll. Saia assim em 100% das vezes que esse hook era sorteado (7,7% dos
    videos).

    ⛔ Corrigido AQUI, no codigo, e nao no pool: nem o hook nem os 14 eventos
    sao redigitados. String validada e' constante (CLAUDE.md §Alcada) — o que
    estava errado era a montagem, nao a copy.
    """
    ev = oc["plateia_evento"]
    if "The whole {evento}" in hook or "the whole {evento}" in hook:
        ev = re.sub(r"^(that|this|the)\s+", "", ev, flags=re.I)
    return hook.format(evento=ev, o=o)


def _sortear_evitando(rng, pool, recentes, chave="id"):
    """Sorteia evitando os valores usados recentemente naquela pagina."""
    livres = [x for x in pool if x.get(chave, x) not in recentes]
    return rng.choice(livres if livres else pool)


# ⚠️ era `nova_fala` no arquivo de origem — renomeada porque este arquivo tem a
# sua propria `nova_fala`, de 3 cenas. Fora a linha do `def`, copia literal.
def _cta_curto(rng):
    """CTA + GATE somam num take so', e ninguem olhava a soma.

    ⛔ ORDEM: o CTA sai PRIMEIRO — e' ele que carrega o literal `Comment
    gelatin,` e a isca, os dois intocaveis — ja' reservando o gate mais curto.
    O GATE sai por ULTIMO porque e' o beat intercambiavel do par: e' ele que
    absorve a sobra em vez de ser cortado pelo fim do take.
    ⚠️ Fallback e' a entrada mais CURTA do pool, NUNCA `or pool`: `or pool`
    devolve o pool inteiro e reintroduz o estouro em silencio.
    ⭐ Medido em 4.000 sorteios da cadeia: max 25, 0,0% acima. Nenhuma entrada
    fica inalcancavel — 14/14 CTAS e 11/11 GATES continuam saindo.
    """
    cg = min(GATES, key=_palavras)

    def _ok(pool, monta):
        v = [x for x in pool if _palavras(monta(x)) <= TETO_FALA[3]]
        return v or [min(pool, key=lambda x: _palavras(monta(x)))]

    cta = rng.choice(_ok(CTAS, lambda c: c.format(gate=cg)))
    return cta.format(gate=rng.choice(
        _ok(GATES, lambda g: cta.format(gate=g))))


def _nova_fala_longo(spec, i, rng):
    """Re-sorteia a fala da cena i (0-4) mantendo o substantivo-nucleo daquela
    cena — a rotacao do orgao e' do video inteiro, nao da linha."""
    o = next((n for n in NUCLEO if n.lower() in spec["falas"][i].lower()), "Johnson")
    oc = spec["ocasiao"]
    if i == 0:
        return _hook_fmt(rng.choice(HOOKS), oc, o)
    if i == 1:
        return rng.choice(DESCOBERTAS).format(quem=rng.choice(QUEM_CONTOU), o=o)
    if i == 2:
        return rng.choice(RITUAIS).format(o=o)
    if i == 3:
        return rng.choice(REDENCOES).format(eco=oc["eco"], brag=rng.choice(BRAGGING),
                                            o=o, barreira=rng.choice(BARREIRAS))
    return _cta_curto(rng)


# ⚠️ era `sortear` no arquivo de origem — renomeada pelo mesmo motivo.
def _sortear_longo(pagina, rng, ledger, travas=None):
    # ⛔ A REF DESTE AGENTE SAI AQUI, no motor longo embutido — nao no
    # `sortear` de tres argumentos la' de baixo. Por isso a trava atravessa
    # `sc.sortear_curto` ate' aqui: sem isso o toggle acenderia e nao mudaria
    # nada, que e' o botao que mente.
    hist = ledger.get(pagina, {})
    # evita repetir o valor dos ultimos N videos da mesma pagina
    ev = lambda eixo, n: hist.get(eixo, [])[-n:]

    oc = _sortear_evitando(rng, OCASIOES, ev("ocasiao", 3))
    prop = _sortear_evitando(rng, PROPS, ev("prop", 3))
    amb = _sortear_evitando(rng, AMBIENTES, ev("ambiente", 2))
    # ⭐ MODO BELA / MODO FORTE — contrato do short_comum.
    # ⚠️ A REF deste angulo e' o NARRADOR (homem), e a mulher e' a vitima do
    # flagrante. Por isso `forte` vale para a REF e `bela` para as MULHERES.
    ref = (sc.ref_forte(REFS[0], rng) if (travas or {}).get("forte")
           else rng.choice(REFS))
    vit = rng.choice(VITIMAS)
    mul = rng.choice(MULHERES)

    # 4 substantivos distintos do nucleo, um por cena 1-4 (cota 75%)
    # ⛔ 2026-08-10 — SO' OS TRES APELIDOS SAO SORTEAVEIS (ordem do
    # operador, parque inteiro). `soldier` e `tool` seguem no NUCLEO porque
    # as LENTES os usam para DETECTAR o orgao; o que muda e' que nao saem
    # mais na fala. Ver `short_comum.orgaos_sorteaveis`.
    orgaos = sc.orgaos_sorteaveis(rng, 4)

    falas = [
        _hook_fmt(rng.choice(HOOKS), oc, orgaos[0]),
        rng.choice(DESCOBERTAS).format(quem=rng.choice(QUEM_CONTOU), o=orgaos[1]),
        rng.choice(RITUAIS).format(o=orgaos[2]),
        rng.choice(REDENCOES).format(eco=oc["eco"], brag=rng.choice(BRAGGING),
                                     o=orgaos[3], barreira=rng.choice(BARREIRAS)),
        _cta_curto(rng),
    ]

    return {
        "pagina": pagina, "ocasiao": oc, "prop": prop, "ambiente": amb,
        "ref": ref, "vitima": vit, "mulher": mul, "falas": falas,
    }


# ⚠️ era `montar` no arquivo de origem — renomeada pelo mesmo motivo. E' este
# que o `short_comum.montar_curto` roda para depois ficar so' com o MAPA.
def _montar_longo(spec):
    et = ETNIA[spec["pagina"]]
    ref, vit, mul = spec["ref"], spec["vitima"], spec["mulher"]
    prop, oc, amb = spec["prop"], spec["ocasiao"], spec["ambiente"]
    falas = spec["falas"]

    ref_desc = "a %d-year-old %s man with %s" % (ref["idade"], et, ref["marca"])
    vit_desc = "A %d-year-old %s %s" % (vit["idade"], et, vit["marca"])
    neg = NEGACAO_AVE if prop["marisco"] else ""
    luz = amb["luz"]

    b = {}

    # O cabecalho REF faz parte do bloco, igual ao "IMAGE 01/05:" dos outros.
    # E o que o parser do AdBatch usa para mandar este bloco para o painel
    # Consistencia Visual em vez de tentar encaixa-lo num slot da grade.
    # ⛔ Nao remover: sem ele a referencia e descartada em silencio.
    b["BLOCO 0 (REF)"] = (
        "REF 01: Photo of a real person, a %d-year-old %s man, chest up, facing camera, "
        "calm expression. Lean muscular build, chest and shoulders visible. %s. "
        "%s %s Plain gray background, soft light. No text, no watermark."
        % (ref["idade"], et, ref["marca"].capitalize(), ref["roupa"], ANTICELEB)
    )

    b["IMAGE 01/05"] = (
        "IMAGE 01/05: Medium shot at %s, %s, no logos anywhere. %s sits %s, "
        "head bowed, shoulders down. %s %s a %d-year-old %s %s laughs at the "
        "seated man, two blurred %s laugh behind her.%s %s %s"
        % (oc["cenario"], oc["detalhe"], vit_desc, oc["assento"],
           AGENCIA_IMAGE.format(prop_murcho=prop["murcho"], ref_desc=ref_desc),
           oc["posicao_mulher"], mul["idade"], et, mul["hook"],
           oc["plateia"], neg, oc["luz_hook"], CAUDA)
    )

    b["IMAGE 02/05"] = (
        "IMAGE 02/05: Medium close-up in %s. The same %d-year-old %s man, %s, "
        "%s, stands behind the %s, leaning slightly toward the camera, mouth open "
        "mid-word. %s He is alone in frame. %s %s"
        % (amb["set"], ref["idade"], et, ref["marca"], ref["roupa_curta"],
           amb["bancada"], D1_IMAGE, luz.capitalize(), CAUDA)
    )

    b["IMAGE 03/05"] = (
        "IMAGE 03/05: Close insert shot, same %s, %s A pair of hands tears open "
        "a small white sachet and pours powder into a glass of water, a spoon "
        "beside it. No face in frame. %s" % (amb["bancada"], luz, CAUDA)
    )

    b["IMAGE 04/05"] = (
        "IMAGE 04/05: Medium shot in a plain living room, %s The same "
        "%d-year-old %s %s, now in a clean white shirt, sits in an armchair "
        "grinning, head up. A %d-year-old %s woman %s sits sideways on his knee, "
        "arm around him, laughing. In her free hand she holds %s.%s %s"
        % (luz, vit["idade"], et, vit["marca"], mul["idade"], et,
           mul["payoff"], prop["ereto"], neg, CAUDA)
    )

    b["IMAGE 05/05"] = (
        "IMAGE 05/05: Close-up in the same %s, %s The same %d-year-old %s man, "
        "%s, alone, looking at camera with a confident half-smile, finger "
        "pointing at the lens. %s"
        % (amb["curto"], luz, ref["idade"], et, ref["marca"], CAUDA)
    )

    b["TAKE 01/05"] = (
        "TAKE 01/05: Animate the image exactly. Handheld iPhone, slight sway, "
        "no cuts. %s What he holds stays exactly as shown — %s The woman keeps "
        "laughing, the %s keep laughing in the background.\n"
        "Dialogue: \"%s\"\nAudio: %s No music."
        % (AGENCIA_TAKE.format(ref_curto=ref["cabelo"]), IMOBILIDADE,
           oc["plateia"], sonorizar(falas[0]), oc["audio"])
    )

    b["TAKE 02/05"] = (
        "TAKE 02/05: Animate the image exactly. Handheld iPhone, slight sway, "
        "no cuts. %s He is alone in frame, speaking with conviction.\n"
        "Dialogue: \"%s\"\nAudio: quiet room tone. No music." % (D1_TAKE, sonorizar(falas[1]))
    )

    b["TAKE 03/05"] = (
        "TAKE 03/05: Animate the image exactly. Handheld iPhone, slight sway, "
        "no cuts. Hands finish pouring the sachet, stir the glass in slow "
        "circles. No face enters frame.\n"
        "Dialogue: \"%s\"\nAudio: spoon clinking glass, quiet room tone. No music."
        % sonorizar(falas[2])
    )

    b["TAKE 04/05"] = (
        "TAKE 04/05: Animate the image exactly. Handheld iPhone, slight sway, "
        "no cuts. The man laughs silently, head tipping back. The woman laughs, "
        "tightens her arm around him; her other hand stays exactly where it is, "
        "holding it motionless the entire shot. Neither changes position. A "
        "man's voice speaks over the scene; the couple stays silent.\n"
        "Dialogue: \"%s\"\nAudio: quiet room tone, soft laughter. No music." % sonorizar(falas[3])
    )

    b["TAKE 05/05"] = (
        "TAKE 05/05: Animate the image exactly. Handheld iPhone, slight sway, "
        "no cuts. He looks at camera, calm, points his finger, speaks evenly.\n"
        "Dialogue: \"%s\"\nAudio: quiet room tone. No music." % sonorizar(falas[4])
    )

    return b


# ---------------------------------------------------------------------------
# INTERFACE (consumido por ui_agente.py)
# ---------------------------------------------------------------------------

# ⚠️ o `ui_agente` resolve estes nomes de pool ("OCASIOES", "PROPS"...) com
# getattr NO MOTOR. Antes eles so' existiam no `_lucas` e a UI caia no fallback
# `motor.base`; agora moram aqui e a busca acerta de primeira.
EIXOS_UI = [
    ("ocasiao", "OCASIÃO", "OCASIOES", "id"),
    ("prop", "PROP", "PROPS", "id"),
    ("ambiente", "AMBIENTE", "AMBIENTES", "id"),
    ("ref", "NARRADOR", "REFS", "marca"),
    ("vitima", "VÍTIMA", "VITIMAS", "marca"),
    ("mulher", "MULHER", "MULHERES", "hook"),
]

# ja' com a preposicao contraida — abrem a frase do resumo
PT_OCASIAO = {
    "casamento": "Num casamento", "confraternizacao": "Na confraternização da firma",
    "pescaria_firma": "Na pescaria da firma", "reuniao_firma": "Na reunião da firma",
    "churrasco": "Num churrasco de família", "jantar_amigos": "Num jantar de amigos",
    "aniversario": "Nas bodas de casamento", "clube_golfe": "No almoço do clube de golfe",
}


# ---------------------------------------------------------------------------
# ⭐ A FACHADA QUE O `short_comum` RECEBE COMO `base`
# ---------------------------------------------------------------------------
# 2026-08-03. As funcoes de `short_comum.py` recebem o arco longo por parametro
# e leem `base.X`, e o `short_comum` nao se toca — ele serve todos os agentes
# SHORT. Como nao ha' mais modulo para passar, a fachada e' montada aqui, a
# partir das definicoes deste proprio arquivo.
#
# ⛔ Nao pode ser o proprio modulo: `base.montar` tem de ser o de CINCO cenas e
# o deste modulo e' o de tres — o colapso passaria a chamar a si mesmo.
# ⛔ Nao acrescentar BANIDOS_CATEGORIA/ANIMAL/VAZAMENTO/FONTE: o `short_comum`
# procura as tabelas globais por `hasattr`, e o FLAGRANTE so' tem a
# BANIDOS_GLOBAL. Inventar tabela aqui mudaria o linter.
_LONGO = types.SimpleNamespace(
    ETNIA=ETNIA,
    NUCLEO=NUCLEO,
    CAUDA=CAUDA,
    NEGACAO_AVE=NEGACAO_AVE,
    sonorizar=sonorizar,
    _palavras=_palavras,
    BANIDOS_TAKE=BANIDOS_TAKE,
    BANIDOS_IMAGE=BANIDOS_IMAGE,
    BANIDOS_GLOBAL=BANIDOS_GLOBAL,
    BANIDOS_CTA=BANIDOS_CTA,
    montar=_montar_longo,
    sortear=_sortear_longo,
    nova_fala=_nova_fala_longo,
)


# ===========================================================================
# O SHORT — daqui para baixo, o que ja' era deste arquivo
# ===========================================================================

# ⭐ MAPA e' de onde vem a IMAGEM; MAPA_COPY e' de onde vem a FALA. A cena 3
# junta as duas coisas: a fala do CTA (base 5) por cima da cena do ritual.
#
# ⚠️ Ordem do operador, 2026-07-31: "estamos deixando espaco valioso nesses 22
# segundos apertados no lixo". A cena 3 era o close do CTA — um terco do video
# num talking head, zero informacao visual. Agora o espectador OUVE o pedido e
# VE o gelatin trick nos mesmos 8 segundos.

# ⚠️ E aqui a cena 3 nao vem pronta do base: a do ritual dele e' insert de
# maos, e o operador pediu "rosto aparente enquanto prepara". A recombinacao
# (set da cena 2 + acao da cena 3 + rosto) mora em short_comum.bancada_com_rosto
# — nenhum fragmento novo, e o motor longo fica intacto.
MAPA = (1, 4, 3)
MAPA_COPY = (1, None, 5)          # None = a fundida
CENAS_UI = ["1 · O FLAGRANTE", "2 · O TRUQUE + A VIRADA", "3 · CTA PREPARANDO"]

# ⚠️ Aqui as pontas NAO herdam o teto do motor base, e a excecao e' medida:
# os tetos do FLAGRANTE base estao defasados em relacao aos proprios pools
# dele — em 300 sorteios a cena 1 estoura o teto 22 em 69% das vezes e a cena
# 5 estoura o teto 24 em 49%. Herdar isso faria o linter do SHORT gritar em
# dois de cada tres videos, e aviso que sempre dispara e' aviso que ninguem le.
# Os numeros abaixo sao o p90 medido de cada pool herdado.
# ⛔ Recalibrar os tetos do motor BASE e' decisao do operador — nao foi feito.
# ⛔⛔ A CENA 2 CAIU DE 34 PARA 32 EM 2026-08-04 — 34 esta' ACIMA DO FISICO.
# 8 segundos a 4,0 palavras/s comportam 32 (licoes-de-construcao §5). Com teto
# 34 o lint aprovava fala de 33 e 34 palavras, e elas eram CORTADAS no render:
# medido, 6,7% das 6240 combinacoes do template x slots passavam de 32, e o que
# ficava de fora era sempre o fecho da virada.
# ⚠️ O linter era mudo porque comparava com o teto DECLARADO AQUI. Teto acima da
# capacidade fisica nao e' escolha de estilo — e' a trava desligada (§27).
# ⛔⛔ TETO 25 — ordem permanente do operador: nao pode haver corte de fala.
# ⚠️ A cena 3 cortava em 27,8%, e AQUI O TETO SOZINHO NAO RESOLVE: medido, ela
# continuava em 27,8% mesmo com o teto em 25, porque o CTA era montado com
# `rng.choice(CTAS).format(gate=rng.choice(GATES))` — sem consultar orcamento
# nenhum. Precisou do `_cta_curto` abaixo.
# ⛔⛔ TETO 25 — ordem permanente do operador, 2026-08-05: *"sempre meca. Nao
# pode haver cortes de fala."* O numero vem de RENDER, nao de conta: 32
# cortou e 28 cortou. Os exemplos que ele escreve a mao vivem em 16-25
# palavras (2,0-3,1 p/s). Ver licoes-de-construcao §28.
# ⭐⭐ MODOS DE REF — contrato compartilhado (short_comum),
# 2026-08-05. ⛔ Desligados, o prompt volta IDENTICO ao de antes
# do recurso — provado caractere por caractere.
MODO_FORTE = True

TETO_FALA = {1: 24, 2: 25, 3: 25}


# ---------------------------------------------------------------------------
# A COPY FUNDIDA — cena 2
# ---------------------------------------------------------------------------
# ⚠️ CURADORIA DO OPERADOR. Copy nova, montada a partir dos fragmentos ja'
# validados das DESCOBERTAS e REDENCOES do motor base.
#
# Todo item carrega, na mesma respiracao:
#   1. quem contou   -> {quem}, que e' o que faz a descoberta soar boca-a-boca
#   2. o mecanismo   -> `blood flow`
#   3. o ritual      -> `gelatin trick`
#   4. a virada      -> a mulher, dezenove dias depois
# ⛔ Sem {barreira}: a cena ja' carrega quatro beats e estourava o teto.
# ⚠️ Todo item precisa de `{o}` — o CTA nao nomeia o orgao, entao sem ele a
# cota cai para 1/3 e o linter reprova o sorteio.
FUNDIDAS = [
    "That's when {quem} gave him the gelatin trick. It's not age — the blood "
    "flow to your {o} got choked off. Nineteen days later she's {brag} about "
    "his.",

    # ⚠️ 2026-08-01 — auditoria de drifting. `Blood flow, not age` e' mecanismo
    # SEM DESTINO: homem de 50-65 que ouve "blood flow" solto compra circulacao
    # ou coracao, que e' outra categoria de produto. O F14 ja registrou a irma
    # `it's the flow, not the years` como falha de producao (farmacia Marcus,
    # 2026-07-28), com o diagnostico literal "abstrato: flow de que, onde?".
    # ⛔ Aqui a oracao e' o UNICO portador do mecanismo do video: a placa D1 em
    # corte, que explicava isso na imagem, morreu no colapso 5->3 (ver docstring).
    # O destino volta pelo fragmento verbatim das DESCOBERTAS do motor base, que
    # anexam o orgao em 12 de 12.
    "{quem} handed him the gelatin trick. It's not your age, brother — the "
    "blood flow to your {o} got choked off. Nineteen days later she wouldn't "
    "get off his knee.",

    "{quem} pulled him aside with the gelatin trick — the blood flow stopped "
    "reaching your {o}. Nineteen days later she's the one {brag} about his.",

    # ⚠️ mesma correcao, e aqui era a mais grave das tres: a absolvicao `it's
    # not you` e' copy validada (DESCOBERTAS idx 3), mas LA' ela vem com uma
    # segunda oracao que ancora o mecanismo no orgao em 2a pessoa. A fusao
    # colapsou as duas e perdeu a ancora — nesta linha o espectador NUNCA ouvia
    # `your {orgao}`: a unica mencao ao orgao chegava no fim e em 3a pessoa,
    # falando do outro cara.
    "That's when {quem} told him the gelatin trick. It's the blood flow to "
    "your {o}, not you. Nineteen days later the men who laughed asked what he "
    "was taking.",

    "{quem} gave him the gelatin trick that night. The blood flow to your {o} "
    "got choked off, and it is fixable. Nineteen days later she reaches for "
    "him first.",

    # + 2026-08-01: o operador mediu vicio no lote — a fundida saindo sempre
    # com a mesma abertura e com "brother". As oito novas trocam as duas
    # coisas, e cada uma continua carregando `gelatin trick`, `blood flow`
    # e o `{o}` que o linter exige.
    # ⚠️ a terceira da familia. Somadas, as tres saiam em 23,8% dos videos do
    # FLAGRANTE — o maior peso isolado da auditoria de 2026-08-01.
    "A week later {quem} passed him the gelatin trick. The blood flow to your "
    "{o} got choked off. Nineteen days after that she's {brag} about his.",

    "It was {quem} who handed him the gelatin trick. Blood flow to your {o} "
    "got choked off. Nineteen days later she's {brag} about his.",

    "The gelatin trick wasn't from a doctor. It came from {quem}. Blood flow "
    "to your {o}, not age. Nineteen days later she won't let him sleep.",

    "Same week, {quem} showed him the gelatin trick. Blood flow to your {o} "
    "got choked off. Nineteen days later the men who laughed asked him why.",

    "He drank it the night {quem} told him the gelatin trick. Blood flow to "
    "your {o}, not age. Nineteen days later she wouldn't get off his knee.",

    "Nobody knew {quem} had given him the gelatin trick. Blood flow to your "
    "{o}, not age. Nineteen days later she's {brag} about his.",

    "One glass a night, the gelatin trick from {quem}. The blood flow to your "
    "{o} got choked off. Nineteen days later she reaches for him first.",

    "It wasn't a pill, it was the gelatin trick from {quem}. Blood flow to "
    "your {o} got choked off. Nineteen days later nobody was laughing.",
]


def _fundir(spec, rng):
    o = sc.orgao_de(_LONGO, spec["falas_base"][3])
    # ⛔ O TEMPLATE sorteia UNIFORME e nao se re-sorteia. Re-sortear a copy
    # enviesaria o pool para as fundidas curtas; o estouro nasce do PRODUTO
    # template x slot, nao da frase. Entao quem cede sao os SLOTS.
    # ⚠️ Filtro determinístico, NUNCA laco de rejeicao: sem `while`, sem
    # `range(40)` — laco de rejeicao num motor que roda dentro da janela do
    # `.exe` e' risco de travar a interface na mao do operador.
    # ⚠️ Fallback = a entrada mais CURTA, nunca `or pool`: `or pool` devolve
    # tudo e reintroduz o estouro em silencio.
    # ⛔ 2026-08-05 — O TEMPLATE TAMBEM CEDE. O comentario acima dizia que so'
    # os slots cediam, e isso valia com teto 32: com teto 25 existem templates
    # que nao cabem NEM com o `quem` e o `brag` mais curtos do pool, e o
    # fallback entregava um estouro de 30 palavras. Agora o template e' filtrado
    # primeiro, contra os slots minimos, e so' depois os slots cedem.
    curto_b = min(BRAGGING, key=_palavras)
    curto_q = min(QUEM_CONTOU, key=_palavras)
    _vt = [t for t in FUNDIDAS
           if _palavras(t.format(o=o, quem=curto_q, brag=curto_b))
           <= TETO_FALA[2]]
    tpl = rng.choice(_vt or [min(FUNDIDAS, key=lambda t: _palavras(
        t.format(o=o, quem=curto_q, brag=curto_b)))])
    vq = [q for q in QUEM_CONTOU
          if _palavras(tpl.format(o=o, quem=q, brag=curto_b)) <= TETO_FALA[2]]
    quem = rng.choice(vq or [min(QUEM_CONTOU, key=_palavras)])
    vb = [b for b in BRAGGING
          if _palavras(tpl.format(o=o, quem=quem, brag=b)) <= TETO_FALA[2]]
    brag = rng.choice(vb or [min(BRAGGING, key=_palavras)])
    return tpl.format(o=o, quem=quem, brag=brag)


# ---------------------------------------------------------------------------
# CONTRATO DO MOTOR
# ---------------------------------------------------------------------------

def _carregar_ledger():
    import json
    if os.path.exists(LEDGER):
        with open(LEDGER, encoding="utf-8-sig") as f:
            return json.load(f)
    return {}


def _gravar_ledger(ledger, spec):
    import json
    p = ledger.setdefault(spec["pagina"], {})
    for eixo, val in (("ocasiao", spec["ocasiao"]["id"]),
                      ("prop", spec["prop"]["id"]),
                      ("ambiente", spec["ambiente"]["id"])):
        p.setdefault(eixo, []).append(val)
        p[eixo] = p[eixo][-12:]
    with open(LEDGER, "w", encoding="utf-8") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)


def sortear(pagina, rng, ledger, travas=None):
    return sc.sortear_curto(_LONGO, pagina, rng, ledger, MAPA, _fundir,
                            MAPA_COPY, travas)


def montar(spec):
    b = sc.montar_curto(_LONGO, spec, MAPA)
    # a cena 3 e' a unica que nao vem pronta do base — ver o comentario
    # do MAPA e a docstring de short_comum.bancada_com_rosto
    # ⚠️ DUAS cenas nao vem prontas do base, e as duas por ordem do
    # operador: a 2, para o narrador nao sumir no terco do meio; e a 3,
    # para o rosto aparecer enquanto prepara. As duas recombinam blocos
    # validados — ver as docstrings em short_comum.
    i2, t2 = sc.redencao_com_ref(_LONGO, spec, spec["falas"][1])
    b["IMAGE 02/03"], b["TAKE 02/03"] = i2, t2
    i3, t3 = sc.bancada_com_rosto(_LONGO, spec, spec["falas"][2])
    b["IMAGE 03/03"], b["TAKE 03/03"] = i3, t3
    # ⛔ trava de texto queimado em todo TAKE — o watermark que o
    # operador viu vazando nos reels da concorrente (2026-08-01).
    return sc.selar_takes(b)


def nova_fala(spec, i, rng):
    return sc.nova_fala_curta(_LONGO, spec, i, rng, MAPA, _fundir, MAPA_COPY)


def _recopiar_ocasiao(spec, rng):
    """A ocasiao entra no hook e no eco da cena fundida — trocar exige reescrever."""
    spec["falas"][0] = _nova_fala_longo(sc.espelho(spec, MAPA), 0, rng)
    spec["falas"][1] = _fundir(spec, rng)


EIXOS_QUE_MEXEM_NA_COPY = {"ocasiao": _recopiar_ocasiao}


# ---------------------------------------------------------------------------
# LINTER
# ---------------------------------------------------------------------------

def _imobilidade(spec, blocos, achados):
    # as duas cenas com prop na mao sobrevivem: a ruina e a redencao
    for cena in (1, 4):
        nome = "TAKE %02d/03" % (MAPA.index(cena) + 1)
        if "motionless" not in blocos[nome].lower():
            achados.append(("ERRO", "%s sem declaracao de imobilidade do prop" % nome))


def lint(spec, blocos):
    return sc.lint_curto(
        _LONGO, spec, blocos, MAPA, TETO_FALA,
        literais=("gelatin trick", "blood flow"),
        extras=(_imobilidade,))


# ---------------------------------------------------------------------------
# RESUMO
# ---------------------------------------------------------------------------

def resumo_pt(spec):
    et = "branca" if "white" in ETNIA[spec["pagina"]] else "negra"
    return ("%s, o colega segura %s no próprio colo enquanto o narrador aponta "
            "e a mesa ri. Na cena 2 vem o truque e a virada com a esposa, e na "
            "3 o CTA. Três cenas, elenco de pele %s."
            % (PT_OCASIAO.get(spec["ocasiao"]["id"], "No evento"),
               spec["prop"].get("pt", "o prop"), et))


# ---------------------------------------------------------------------------
# ⭐⭐ AUTOTESTE — o aceite deste motor deixa de ser RELATO e vira MEDICAO
# ---------------------------------------------------------------------------
# ⚠️ ESTE MOTOR NASCEU SEM `--autoteste` e ficou assim ate' 2026-08-13, quando os
# pools de gente e de ambiente foram ampliados por ordem do operador (*"melhore a
# aparencia e shape desses homens"* / *"aumente o pool de opcoes
# substancialmente, tambem dos ambientes"*). Pool grande sem sonda e' pior que
# pool pequeno: o vicio volta calado e ninguem ve' — foi exatamente assim que a
# mesma cara e o mesmo set voltaram no lote em 2026-08-01 e 2026-08-02.
# ⛔ `0 ERRO` num lote grande e' SUSPEITA, nao aprovacao: pode ser motor limpo ou
# regra morta. Por isso cada trava tem um sabotador logo abaixo, e o sabotador
# tem de CHEGAR onde a regra olha (licoes §16) — e' por isso que `_medir_pools`
# recebe as listas por ARGUMENTO em vez de ler o global.
_PROIBIDO_APARENCIA = (
    "scar", "broken nose", "chipped tooth", "missing tooth", "gap between",
    "sun damage", "sun-weathered", "weathered", "ruddy", "thin skin",
    "loose skin", "age spot", "sunken", "gaunt", "bony", "hollow",
    "leathery", "deeply lined", "crease between",
)
# ⚠️ `worn` NAO entra na lista acima, e a ausencia e' deliberada: neste pool a
# palavra e' PENTEADO (`a thick grey afro worn low`), nao desgaste. Token
# polissemico numa sonda gera falso positivo, e sonda que grita a' toa ensina o
# operador a ignorar o autoteste — que e' o custo que a §16 cobra.
_APROVACAO = (
    "handsome", "chiseled", "rugged", "strong jaw", "piercing eyes",
    "good-looking", "attractive", "not a celebrity", "not famous",
    "not a model",
)


def _medir_pools(ambientes, refs, vitimas, mulheres):
    """As travas de POOL deste motor, medidas — nunca declaradas.

    ⛔ As quatro listas entram por ARGUMENTO de proposito: e' o que deixa o
    sabotador plantar uma entrada suja sem encostar no motor de verdade. Trava
    que so' sabe olhar o global nao pode ser testada, e trava nao testada e'
    decoracao.
    """
    achados = []
    for nome, pool, piso in (("AMBIENTES", ambientes, 24), ("REFS", refs, 26),
                             ("VITIMAS", vitimas, 16), ("MULHERES", mulheres, 26)):
        if len(pool) < piso:
            achados.append("pool %s com %d entradas (piso %d)"
                           % (nome, len(pool), piso))
        txt = [str(x) for x in pool]
        for x in sorted({t for t in txt if txt.count(t) > 1}):
            achados.append("pool %s tem entrada REPETIDA: %s" % (nome, x[:70]))
        for x in txt:
            baixo = x.lower()
            for t in _PROIBIDO_APARENCIA:
                if t in baixo:
                    achados.append("pool %s: ancora DETERIORADA %r em %s"
                                   % (nome, t, x[:60]))
            for t in _APROVACAO:
                if t in baixo:
                    achados.append("pool %s: palavra de aprovacao/negacao %r em "
                                   "%s" % (nome, t, x[:60]))

    # ⛔ F4b, os tres eixos que sobrevivem ao plano medio: o narrador e'
    # cabeleira + barbeado + SEM oculos, a vitima e' careca + bigode + COM
    # oculos. Sem isto os dois viram o mesmo homem no mesmo quadro.
    for r in refs:
        marca = r["marca"].lower()
        for t in ("bald", "glasses", "mustache", "moustache"):
            if t in marca:
                achados.append("REF com %r na marca — o F4b da' isso a' VITIMA, "
                               "nunca ao narrador: %s" % (t, r["marca"][:60]))
        # ⚠️ `cabelo` vira `The {cabelo}-haired man` dentro do AGENCIA_TAKE:
        # virgula, ponto ou espaco sobrando ali sai narrado em voz alta.
        cab = r["cabelo"]
        if cab != cab.strip() or "," in cab or "." in cab:
            achados.append("REF com `cabelo` que nao cola em `{}-haired`: %r"
                           % cab)
    for v in vitimas:
        marca = v["marca"].lower()
        for t in ("bald", "glasses"):
            if t not in marca:
                achados.append("VITIMA sem %r — o F4b exige careca + bigode + "
                               "oculos: %s" % (t, v["marca"][:60]))
        if "mustache" not in marca and "moustache" not in marca:
            achados.append("VITIMA sem bigode — o F4b exige careca + bigode + "
                           "oculos: %s" % v["marca"][:60])

    # ⭐ O EIXO `OCULOS` GIRA NA MULHER, e so' nela: no narrador o F4b o zera e
    # na vitima ele e' 100%. Se a faixa cair aqui, o motor inteiro fica sem esse
    # eixo — que e' o defeito que o `medir_personagens.py` mede no repo todo.
    if mulheres:
        com = sum(1 for w in mulheres if "glasses" in w["hook"])
        if not 0.20 <= com / float(len(mulheres)) <= 0.35:
            achados.append("MULHERES com oculos em %.0f%% (faixa 20-35%%) — e' "
                           "o unico pool deste motor onde o eixo pode girar"
                           % (100.0 * com / len(mulheres)))
    for w in mulheres:
        # ⚠️ Forma da frase montada: `a 58-year-old white American WOMAN WITH
        # ... laughs` na cena 1 e `A 58-year-old white American woman WITH ...
        # sits` na cena 4. Entrada fora da forma sai agramatical no video.
        if not w["hook"].startswith("woman with "):
            achados.append("MULHER com `hook` fora da forma `woman with ...`: "
                           "%s" % w["hook"][:50])
        if not w["payoff"].startswith("with "):
            achados.append("MULHER com `payoff` fora da forma `with ...`: %s"
                           % w["payoff"][:50])

    for a in ambientes:
        for k in ("id", "set", "bancada", "curto", "luz"):
            if not a.get(k):
                achados.append("AMBIENTE %s sem a chave %r"
                               % (a.get("id", "?"), k))
        luz = a.get("luz", "")
        # ⚠️ A `luz` entra DUAS vezes na montagem: capitalizada na IMAGE 02 e
        # crua no meio da frase da IMAGE 03. Por isso o contrato e' minuscula no
        # comeco e ponto no fim — quebrar isso sai como frase partida no prompt.
        if luz and (not luz.endswith(".") or luz[0] != luz[0].lower()):
            achados.append("AMBIENTE %s com `luz` fora do contrato (minuscula "
                           "no inicio + ponto no fim): %r" % (a.get("id"), luz))
    return achados


def autoteste(n=600):
    """Os pools e as invariantes deste motor, medidos num lote de verdade.

    ⚠️ A cobertura e' a metade que importa depois de uma ampliacao: pool grande
    com sorteio que nunca alcanca metade dele e' pool pequeno com nome grande.
    """
    falhas = list(_medir_pools(AMBIENTES, REFS, VITIMAS, MULHERES))
    vistos = collections.defaultdict(set)

    for seed in range(n):
        spec = sortear("joe", random.Random(seed), {})
        blocos = montar(spec)
        for tipo, msg in lint(spec, blocos):
            if tipo == "ERRO":
                falhas.append("seed %d (%s): %s"
                              % (seed, spec["ambiente"]["id"], msg))
        vistos["ambiente"].add(spec["ambiente"]["id"])
        vistos["ref"].add(spec["ref"]["marca"])
        vistos["vitima"].add(spec["vitima"]["marca"])
        vistos["mulher"].add(spec["mulher"]["hook"])

    for eixo, pool in (("ambiente", AMBIENTES), ("ref", REFS),
                       ("vitima", VITIMAS), ("mulher", MULHERES)):
        if len(vistos[eixo]) != len(pool):
            falhas.append("%s: %d de %d nunca sorteados em %d videos"
                          % (eixo, len(pool) - len(vistos[eixo]), len(pool), n))

    # ---- CONTROLES POSITIVOS: cada trava SABE reprovar? --------------------
    ctrl = []
    _sujo = dict(REFS[0])
    _sujo["marca"] = "full silver hair and a clean pale scar through his left eyebrow"
    if not any("DETERIORADA" in m
               for m in _medir_pools(AMBIENTES, REFS + [_sujo], VITIMAS, MULHERES)):
        ctrl.append("a sonda de aparencia NAO acusa `scar` plantado no REFS")
    _elogio = dict(REFS[0])
    _elogio["marca"] = "a handsome face under thick silver hair"
    if not any("aprovacao" in m
               for m in _medir_pools(AMBIENTES, REFS + [_elogio], VITIMAS, MULHERES)):
        ctrl.append("a sonda NAO acusa palavra de aprovacao plantada no REFS")
    _careca = dict(REFS[0])
    _careca["marca"] = "bald man with a gray mustache and square glasses"
    if not any("F4b" in m
               for m in _medir_pools(AMBIENTES, REFS + [_careca], VITIMAS, MULHERES)):
        ctrl.append("a sonda NAO acusa narrador careca/de oculos (F4b)")
    _vit = dict(VITIMAS[0])
    _vit["marca"] = "a man with a full head of hair"
    if not any("VITIMA sem" in m
               for m in _medir_pools(AMBIENTES, REFS, VITIMAS + [_vit], MULHERES)):
        ctrl.append("a sonda NAO acusa vitima sem careca/bigode/oculos (F4b)")
    _amb = dict(AMBIENTES[0])
    _amb["id"], _amb["luz"] = "sabotador", "Warm lamp light"
    if not any("fora do contrato" in m
               for m in _medir_pools(AMBIENTES + [_amb], REFS, VITIMAS, MULHERES)):
        ctrl.append("a sonda NAO acusa `luz` capitalizada e sem ponto final")
    if not any("REPETIDA" in m
               for m in _medir_pools(AMBIENTES, REFS + [REFS[0]], VITIMAS, MULHERES)):
        ctrl.append("a sonda NAO acusa entrada REPETIDA no pool")
    # ⚠️ E o controle NEGATIVO, que fecha o par: o pool limpo nao pode ser
    # acusado. Regra que reprova tudo nunca foi testada.
    if _medir_pools(AMBIENTES, REFS, VITIMAS, MULHERES):
        ctrl.append("o pool limpo esta' sendo reprovado pela propria sonda")

    print("AMBIENTES %d | REFS %d | VITIMAS %d | MULHERES %d | %d videos"
          % (len(AMBIENTES), len(REFS), len(VITIMAS), len(MULHERES), n))
    print("vistos: ambientes %d/%d | refs %d/%d | vitimas %d/%d | mulheres %d/%d"
          % (len(vistos["ambiente"]), len(AMBIENTES),
             len(vistos["ref"]), len(REFS),
             len(vistos["vitima"]), len(VITIMAS),
             len(vistos["mulher"]), len(MULHERES)))
    print("oculos: narrador 0%% (F4b) | vitima 100%% (F4b) | mulher %.0f%%"
          % (100.0 * sum(1 for w in MULHERES if "glasses" in w["hook"])
             / len(MULHERES)))

    if ctrl:
        # ⛔ ASCII de proposito: o console do Windows e' cp1252 e o `⛔` levanta
        # UnicodeEncodeError — justamente na hora em que o relatorio importa.
        print("\n>> O AUTOTESTE ESTA' CEGO:")
        for c in ctrl:
            print("   %s" % c)
    if falhas:
        print("\n>> %d FALHA(S):" % len(falhas))
        for f in falhas[:20]:
            print("   %s" % f)
    if not falhas and not ctrl:
        print("\nAUTOTESTE OK - e os controles reprovam quando devem.")
    return 1 if (falhas or ctrl) else 0


def main():
    import argparse
    ap = argparse.ArgumentParser(description="Randomizador do agente FLAGRANTE SHORT")
    ap.add_argument("--autoteste", action="store_true",
                    help="mede os pools e as invariantes do motor (com controles)")
    ap.add_argument("--pagina", choices=sorted(ETNIA))
    ap.add_argument("--n", type=int, default=1)
    ap.add_argument("--seed", type=int)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    if a.autoteste:
        return autoteste()
    if not a.pagina:
        ap.error("--pagina obrigatorio")

    seed = a.seed if a.seed is not None else random.randrange(10 ** 6)
    rng = random.Random(seed)
    led = _carregar_ledger()
    for _ in range(a.n):
        spec = sortear(a.pagina, rng, led)
        blocos = montar(spec)
        print("=" * 72)
        print(resumo_pt(spec))
        # ⚠️ `sorted` agrupa BLOCO 0, depois todos os IMAGE, depois todos os
        # TAKE — que e' o formato de entrega do repo. Intercalar quebra a
        # colagem no AdBatch.
        for k in sorted(blocos):
            print("\n" + blocos[k])
        if not a.dry_run:
            _gravar_ledger(led, spec)
    return 0


if __name__ == "__main__":
    sys.exit(main())
