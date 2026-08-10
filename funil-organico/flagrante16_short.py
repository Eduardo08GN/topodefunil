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

import os
import re
import sys
import types

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import short_comum as sc                                        # noqa: E402

from nucleo_sonoro import sonorizar                             # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
# ⛔ Ledger proprio: 16s e 24s nao gastam o historico um do outro.
LEDGER = os.path.join(AQUI, ".flagrante-16-ledger.json")

TITULO = "AGENTE FLAGRANTE 16"
SUBTITULO = ("2 takes de 8s = 16 segundos · a humilhação pública, e o truque com o CTA no mesmo quadro")
SLUG = "flagrante-16"


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
# ⭐ A CARA DELE E' ANCORA POSITIVA, nao proibicao. Tirar `laughter` do audio
# resolveu a causa (o Veo sincroniza rosto com som), mas o rosto so' fica certo
# se o prompt DISSER como ele esta' — `never speaks` descreve a boca parada, e
# boca parada nao e' cara de humilhado.
# ⛔ Nada de `he does not laugh`: negacao cria o token que ela queria evitar,
# a mesma licao do `no foreign accent` do CL31.
#
# ⛔⛔ 2026-08-10, TERCEIRA VOLTA DO MESMO BUG — o operador mandou tres renders:
# *"o personagem que e' pra estar triste da risada junto"*. Tirar a risada do
# POOL DE AUDIO nao bastou, e agora se sabe por que: os pools de audio estao
# limpos ha' dias, mas a DIRECAO VISUAL diz `laughing` tres vezes. O Veo le'
# `laughing`, SINTETIZA a gargalhada que ninguem pediu, e depois sincroniza o
# rosto do homem sentado com o som que ele mesmo criou. A risada nao entrava
# pelo audio: entrava pela imagem e voltava como audio.
#
# ⭐ A ordem do operador e' a solucao: *"quero que as pessoas estejam rindo sem
# fazer absolutamente nenhum som"*. Entao o SILENCIO vira descricao POSITIVA e
# concreta, colada em cada mencao de riso — boca aberta, ombros tremendo, nada
# saindo. Descrever o silencio e' diferente de proibir o som: da' ao modelo uma
# imagem para desenhar em vez de um token para evitar.
AGENCIA_TAKE = (
    "The {ref_curto}-haired man speaks calmly to camera, his pointing finger "
    "stays close but never touches the seated man. The seated man keeps his "
    "head down, blinks slowly, never speaks, his fist stays on his own lap. "
    "His mouth stays closed and turned down at the corners and his eyes stay "
    "lowered the whole time, his face fallen and humiliated. The others around "
    "him are laughing in complete silence: their mouths are open and their "
    "shoulders shake, and not one sound comes out of them."
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
        "audio": "reception chatter, glasses clinking.",
    },
    {
        "id": "confraternizacao", "selo": "V",
        "cenario": "a company year-end holiday party in a break room",
        "detalhe": "paper garlands and a folding table with plastic cups",
        "assento": "on a folding chair", "posicao_mulher": "Across the room",
        "plateia": "coworkers", "plateia_evento": "that Christmas party",
        "eco": "the next company party",
        "luz_hook": "Warm string-light glow mixed with overhead fluorescent.",
        "audio": "party chatter, a plastic cup set down.",
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
        "audio": "water lapping the dock, a cooler lid closing.",
    },
    {
        "id": "reuniao_firma", "selo": "N",
        "cenario": "a company end-of-year meeting in a conference room",
        "detalhe": "long table with laptops and coffee cups",
        "assento": "at the table", "posicao_mulher": "Across the table",
        "plateia": "colleagues", "plateia_evento": "that company meeting",
        "eco": "same conference room",
        "luz_hook": "Flat office fluorescent light.",
        "audio": "office chatter, a laptop closing.",
    },
    {
        "id": "churrasco", "selo": "V",
        "cenario": "a family cookout in a backyard",
        "detalhe": "picnic table with paper plates, a grill smoking behind them",
        "assento": "at the picnic table", "posicao_mulher": "Across the table",
        "plateia": "relatives", "plateia_evento": "that cookout",
        "eco": "same backyard, same crowd",
        "luz_hook": "Late afternoon sunlight.",
        "audio": "cookout chatter, a grill hissing.",
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
        "audio": "dinner chatter, cutlery on plates.",
    },
    {
        "id": "aniversario", "selo": "V",
        "cenario": "a fortieth anniversary party in a rented hall",
        "detalhe": "a long table with a sheet cake and folding chairs",
        "assento": "at the table", "posicao_mulher": "Across the table",
        "plateia": "family members", "plateia_evento": "that anniversary party",
        "eco": "same hall, same song",
        "luz_hook": "Warm overhead hall light.",
        "audio": "party chatter, a chair scraping.",
    },
    {
        "id": "clube_golfe", "selo": "N",
        "cenario": "a clubhouse lunch after a golf round",
        "detalhe": "a corner table with iced tea glasses and golf gloves",
        "assento": "at the corner table", "posicao_mulher": "Across the table",
        "plateia": "club members", "plateia_evento": "that clubhouse",
        "eco": "same clubhouse table",
        "luz_hook": "Bright window daylight.",
        "audio": "clubhouse chatter, ice in a glass.",
    },
    # + 2026-08-01: o operador mediu vicio no lote — o mesmo punhado de
    # eventos voltando. Pool dobrado, todas selo N (ainda sem numero).
    # ⛔⛔ 2026-08-10 — IGREJA BANIDA DESTE AGENTE, POR ORDEM DIRETA DO
    # OPERADOR: *"Nunca jamais deve citar igreja em lugar nenhum, nem como
    # cenário nem nada."* A ocasiao `igreja_social` (salao paroquial depois do
    # culto) saiu inteira daqui, e junto saiu `a man from his church` do
    # QUEM_CONTOU e a linha dela do dicionario de resumo. Nao e' so' cenario:
    # e' QUALQUER mencao.
    # ⚠️ Pool de 14 -> 13 ocasioes. Nao repor com nada parecido (capela,
    # paroquia, congregacao, grupo de oracao).
    {
        "id": "clube_veteranos", "selo": "N",
        "cenario": "a veterans club hall on a Friday night",
        "detalhe": "small round tables with beer glasses, a bar counter behind them",
        "assento": "at a round table", "posicao_mulher": "Across the room",
        "plateia": "old servicemen", "plateia_evento": "that veterans hall",
        "eco": "same veterans hall, same table",
        "luz_hook": "Dim amber bar light.",
        "audio": "bar chatter, a glass set down on wood.",
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
        "audio": "pins falling, a ball rolling on wood.",
    },
    {
        "id": "lanchonete", "selo": "N",
        "cenario": "a roadside diner at Sunday breakfast",
        "detalhe": "a corner booth with coffee mugs and a napkin holder",
        "assento": "in the booth", "posicao_mulher": "Across the booth",
        "plateia": "diner regulars", "plateia_evento": "that diner booth",
        "eco": "same booth, same waitress",
        "luz_hook": "Hard morning light through the window blinds.",
        "audio": "diner chatter, mugs set on a counter.",
    },
    {
        "id": "reencontro", "selo": "N",
        "cenario": "a forty-year class reunion in a rented gym",
        "detalhe": "folding tables with punch bowls and paper streamers",
        "assento": "at a folding table", "posicao_mulher": "Across the table",
        "plateia": "old classmates", "plateia_evento": "that class reunion",
        "eco": "same gym, same crowd",
        "luz_hook": "Cool overhead gym light.",
        "audio": "reunion chatter, a punch ladle clinking.",
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
        "audio": "fairground chatter, a distant loudspeaker.",
    },
]

# Ancora de escala obrigatoria nos dois estados (F12 / F15).
# murcho: "no longer than his thumb" · ereto: "as long as her forearm"
# ⛔⛔ POOL ENXUTO A QUATRO — ordem do operador, 2026-08-10: *"remova todos os
# itens de prop que nao se parecem com penis, como aspargo, cenoura e qualquer
# coisa esquisita, deixe somente banana, linguica, pepino e beringela"*.
# Sairam: geoduck, okra, aspargo, daikon, cenoura, alho_poro.
# ⛔ E A TRES, no mesmo dia: *"remova o prop beringela"*. Restam banana,
# linguica e pepino — os tres alongados. A berinjela e' bojuda e nao
# le' como o orgao; foi a propria forma dela que a tirou do pool.
# ⚠️ COM O GEODUCK FORA, `marisco` e' False em todo o pool e a `NEGACAO_AVE`
# (a trava que impedia o Veo de desenhar um ganso) nunca mais dispara. Fica no
# codigo porque o campo continua existindo — se o geoduck voltar, a trava volta
# junto. Nao se remove guarda por estar ociosa.
#
# ⭐⭐ O MURCHO TEM UMA FORMA SO' — relato de campo do operador com quatro
# renders do MESMO prompt: em tres deles o Veo entregou coisa irreconhecivel
# (um anel, um toco, um embrulho) e so' num saiu certo — o prop caido, dobrando
# por cima da mao fechada. Ele apontou esse e pediu ele sempre.
# ⛔ Por isso a geometria NAO e' escrita item a item: e' um molde unico com o
# nome do item entrando num %s. Descricao livre por item foi o que deixou o
# gerador escolher — e ele escolheu errado em 3 de 4.
_MURCHO = ("a small %s held in his closed fist at his lap, no longer than his "
           "thumb, shriveled and wrinkled, completely limp and soft, the free "
           "end drooping down and folding over the side of his hand under its "
           "own weight, clearly unable to hold itself up")
_ERETO = ("%s held upright at shoulder height, stiff and straight, as long as "
          "her forearm and as thick as her wrist")

PROPS = [
    # ⚠️ O campo `pt` e' do Ed (2026-08-10) e fica: e' ele que o painel usa.
    {"id": "banana", "pt": "uma banana", "marisco": False,
     "murcho": _MURCHO % "banana, skin dull and spotted",
     "ereto": _ERETO % "a banana"},
    {"id": "linguica", "pt": "uma linguiça", "marisco": False,
     "murcho": _MURCHO % "cured sausage link",
     "ereto": _ERETO % "a cured sausage link"},
    {"id": "pepino", "pt": "um pepino", "marisco": False,
     "murcho": _MURCHO % "cucumber",
     "ereto": _ERETO % "a cucumber"},
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
    {"idade": 64, "marca": "full gray hair and a clean pale scar through his left eyebrow",
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
    {"idade": 74, "marca": "unusually broad square shoulders, thick steel gray hair parted low on one side and a raised white scar across the bridge of his nose",
     "cabelo": "steel gray", "roupa": "Plain mustard yellow crew-neck tee shirt.",
     "roupa_curta": "mustard yellow tee shirt"},
    {"idade": 58, "marca": "a short compact frame, a full head of tight coppery-brown curls and a small silver scar splitting his upper lip",
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
    {"idade": 61,
     "marca": "a thick grey afro worn low and a broad flattened nose",
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
]

VITIMAS = [
    {"idade": 63, "marca": "bald man with a thick gray mustache and black-framed glasses"},
    {"idade": 62, "marca": "bald man with a red mustache and wire-rimmed glasses"},
    {"idade": 65, "marca": "bald man with a white mustache and thick square glasses"},
    {"idade": 64, "marca": "bald man with a gray fringe above his ears, a bushy mustache and glasses"},
    {"idade": 61, "marca": "bald man with a short gray mustache and round wire glasses"},
    # + 2026-08-01: o operador viu o mesmo rosto de vitima voltando no lote.
    # Cinco novas, todas carecas de bigode e oculos (F4b).
    {"idade": 66, "marca": "bald man with a horseshoe mustache and heavy tortoiseshell glasses"},
    {"idade": 59, "marca": "bald man with a thin pencil mustache and gold aviator glasses"},
    {"idade": 67, "marca": "bald man with a bushy salt-and-pepper mustache and half-rim glasses"},
    {"idade": 68, "marca": "bald man with a drooping gray walrus mustache and rimless glasses"},
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
    {"idade": 58, "marca": "bald man, heavy-set and round-faced, with a chevron mustache streaked white on the left side and thick-lensed glasses"},
    {"idade": 72, "marca": "bald man, thin and deeply lined, with a dark mole beside his mouth, a sparse white mustache and half-moon glasses"},
    {"idade": 60, "marca": "bald man, short and barrel-chested, with a coin-sized dark birthmark on his crown, a bristly steel-gray mustache and boxy clear-framed glasses"},
    {"idade": 69, "marca": "bald man, tall and bony, with a clean scar across his scalp, a close-cropped charcoal mustache and narrow rectangular glasses on a beaded cord"},
    {"idade": 57, "marca": "bald man, stocky and sun-weathered, with a clean scar along his right jawline, a wide brush mustache and heavy black-framed bifocal glasses"},
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
    {"idade": 52,
     "hook": ("woman with dark hair in a high twisted knot, a tall "
              "straight-backed frame and a fine scar through her left eyebrow"),
     "payoff": ("with dark hair in a high twisted knot and a fine scar through "
                "her left eyebrow, in a forest green dress")},
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
    {"idade": 53,
     "hook": ("woman with a heavy gray-streaked ponytail, broad shoulders and "
              "a gap between her front teeth"),
     "payoff": ("with a heavy gray-streaked ponytail and a gap between her "
                "front teeth, in a denim shirt dress")},
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
    {"idade": 67,
     "hook": ("woman with a thick gray shag cut, a thin wiry build and a "
              "sharply hooked nose"),
     "payoff": ("with a thick gray shag cut, a thin wiry build and a sharply "
                "hooked nose, in an ivory blouse")},
]

# ---------------------------------------------------------------------------
# POOLS DE COPY — o molde e' sorteado, a frase cha' vence sempre (arsenal)
# ---------------------------------------------------------------------------

# ⛔⛔ `soldier` SAIU — ordem do operador na reforma de copy 16s (2026-08-10).
# Nos EUA `soldier` para o orgao soa a filme de guerra, nao a boca de homem de
# 50-70 anos; e este e' o unico motor do parque que ainda o carregava.
# ⭐ E O POOL NAO ENCOLHEU: saiu 1, entraram 3 (`manhood`, `equipment`,
# `old boy` ficou de fora de proposito — sao duas palavras e estouravam o
# orcamento de 14 do hook quando o `{evento}` vem com tres). 5 -> 6 entradas.
# ⚠️ As duas novas foram escolhidas contra a lista `ORGAO` do
# `medir_contexto_copy` (`manhood` e `equipment` ja' estao la'): apelido que
# aquele regex nao conhece faz a frase que NOMEIA o orgao ser contada como
# frase orfa, e o relatorio infla com falso positivo. `plumbing` foi testado e
# descartado exatamente por isso.
# ⚠️ `manhood` ja' tem grafia sonora no `nucleo_sonoro` (`man-hood`);
# `equipment` e' palavra comum e nao precisa de nenhuma.
NUCLEO = ["Johnson", "pecker", "wiener", "tool", "manhood", "equipment"]

# ===========================================================================
# ⭐⭐ A CENA 1 — FOFOCA + ANCORA + VIRADA (2026-08-09)
# ===========================================================================
# ⛔⛔ ORDEM DO OPERADOR. Ele leu um take renderizado e parou o lote:
#
#     "Neighbors at that company meeting heard the gossip that his soldier
#      went soft. I stopped reaching for my wife. His sags off his fingers."
#
#     *"ficaria melhor se a oracao «I stopped reaching for my wife. His sags
#      off his fingers.» tivesse funcao de REVIRAVOLTA: «mas um truque que ele
#      descobriu o fez dar a volta por cima». Muito mais coeso e menos copy
#      drifting."*
#
# ⚠️ O DEFEITO TINHA NOME, e ele estava em 8 dos 13 hooks: a terceira sentenca
# EMPILHAVA HUMILHACAO em vez de virar o jogo — e em cinco delas trocava de
# NARRADOR no meio do hook (`I stopped reaching for my wife`, `I was that man`,
# `Mine did too`, `That was me at sixty`). O espectador ouvia, em 8 segundos,
# a desgraca do colega, a desgraca do narrador e nenhuma saida. O video de 16s
# nao tem cena do meio para consertar isso: a cena 2 ja' entra no mecanismo.
#
# ⭐ O ARCO NOVO da cena 1, DOIS beats, na ordem em que o ouvido recebe:
#
#     HUMILHACAO   quem soube + a reacao publica  -> por que ele para de scrollar
#     VIRADA       `...the gelatin trick...`      -> a saida, com nome
#
# ⛔⛔ AS DUAS DECISOES ABAIXO SAO DO OPERADOR, E AS DUAS CONTRARIAM O QUE EU
# TINHA ESCRITO NA PRIMEIRA VERSAO. Eu levei dez candidatos; ele reescreveu
# quatro deles a mao, e os quatro concordavam entre si:
#
#   1. A ANCORA DO PROP SAIU. Eu tinha argumentado que `His pecker hangs like
#      this` era a unica frase que faz o geoduck no colo LER como o orgao. Ele
#      apagou a ancora nos QUATRO e pos no lugar a humilhacao explicita (`they
#      all laughed in front of him`, `They all mocked him`). O prop ja' esta'
#      no colo do sujeito EM QUADRO enquanto a fala diz que o {o} dele parou —
#      a ligacao se faz pela imagem, e as 5-6 palavras da ancora valem mais
#      compradas na risada, que e' o que este angulo vende.
#
#   2. O MECANISMO E' NOMEADO AQUI. Eu tinha travado `one trick` sem sobrenome
#      para nao queimar a lacuna de curiosidade. Ele reprovou:
#      *"Vc tem que ser mais claro e mais taxativo, nao pode dar vazao a
#      duvidas para os viewers. Sempre faca revisao adversarial: o viewer leigo
#      consegue ler/escutar rapido a copy e entender do que se trata? Se a
#      resposta for sequer um talvez, e' descarte."*
#      `one trick` e' exatamente um talvez. A lacuna que vende nao e' o NOME do
#      truque — e' a RECEITA, que so' o CTA entrega. Nomear cedo ancora e ainda
#      martela a keyword do comentario.
#
# ⛔ REVISAO ADVERSARIAL, a regra que sobra: TODA SENTENCA TEM ASSUNTO PROPRIO —
# ou nomeia o {o}, ou nomeia o `gelatin trick`. Nenhuma sobrevive de pronome
# emprestado da anterior. Foi o que matou `His droops like this.` (his O QUE?)
# e `One trick later, nobody laughs at him.` (que truque?).
#
# ⭐ ORCAMENTO GARANTIDO POR CONSTRUCAO, nao por solver: 11-14 + 8-10 = no
# maximo 24, que e' o teto. Nenhuma combinacao das 20 x 22 estoura, e por isso
# NENHUMA entrada fica inalcancavel — o solver de `_hook16` vira rede de
# seguranca, nao filtro. Foi assim que se matou o mode-collapse da versao
# anterior (quatro entradas levavam 67% do lote).

# ⚠️ 11-14 palavras com `{evento}` de 3 (o pior caso). Uma sentenca ou duas.
# ⛔ Toda entrada nomeia o `{o}` na PRIMEIRA sentenca — e' o referente que o
# `medir_abertura` cobra, e e' o que diz ao espectador do que se trata.
#
# ⭐⭐ CT2 DO CONTRATO DE COPY 16s (2026-08-10) — *"o take 1 enuncia a FALHA
# dele, com dano concreto e de preferencia um numero"*. Medido antes da
# reforma: 17% dos videos do FLAGRANTE saiam SEM falha enunciada, e a causa
# eram tres entradas — `was finished` (x2) e `was done`, que dizem que algo
# acabou sem dizer o que o corpo dele faz de errado. As tres foram reescritas
# com o verbo de falha explicito.
# ⭐ E ONDE CABIA, ENTROU UM NUMERO. A melhor linha medida do parque inteiro e'
# `He'd lose it ten minutes in.` — cinco palavras, um numero, um dano. Aqui o
# equivalente e' `quit ten minutes in`, `died two years ago`, `gave out at
# sixty`, `hasn't worked in three years`: o espectador nao ouve "ele piorou",
# ouve QUANTO.
# ⛔ Pool de 16 -> 20 entradas: a reforma nao encolhe repertorio.
HUMILHACOES16 = [
    "Everybody at {evento} heard his {o} quit on him last spring.",
    # ⚠️ `told everyone at {evento}`, nunca `told {evento}`: a metonimia funciona
    # em `The whole veterans hall knew` mas trava em `told that boat`, e frase que
    # trava o ouvido no segundo 2 e' scroll perdido. Sao as tres entradas de
    # `told` do pool — e assim elas tambem passam pela correcao de preposicao.
    "His wife told everyone at {evento} his {o} died two years ago.",
    # ⛔ era `his {o} was finished` — nao dizia o que o corpo faz de errado
    "Everyone at {evento} knows his {o} hasn't worked in three years.",
    "Everyone at {evento} laughed because his {o} quit ten minutes in.",
    "Word got around {evento} that his {o} quit at fifty-eight.",
    # ⛔ era `his {o} was done`
    "His own brother told everyone at {evento} his {o} was dead.",
    "Half of {evento} heard his {o} quit, and they mocked him.",
    "The women at {evento} heard his {o} stopped working last winter.",
    "Nobody at {evento} was surprised his {o} quit two years back.",
    "His crew at {evento} heard his {o} gave out at sixty.",
    "Every guy at {evento} knew his {o} quit on him at fifty.",
    # ⛔ era `his {o} was finished`
    "The whole {evento} knew his {o} quit, they said it out loud.",
    "Cousins at {evento} heard his {o} shut down, they laughed at him.",
    "Neighbors at {evento} heard his {o} went soft, they mocked him.",
    "The men at {evento} laughed at him because his {o} quit.",
    "His partner told everyone at {evento} his {o} hasn't worked in years.",
    # + 2026-08-10: quatro novas, todas com dano datado ou cronometrado.
    "Everyone at {evento} heard his {o} quits five minutes in.",
    "His wife laughed at {evento} and said his {o} stopped years ago.",
    # ⚠️ era `...failed him on their anniversary.` — com `{evento}` =
    # `that anniversary party` a frase saia com `anniversary` duas vezes em
    # onze palavras. Medido no sorteio, nao lido no pool.
    "The whole {evento} heard his {o} failed him in bed.",
    "Men at {evento} still joke that his {o} quit on him.",
]

# ⚠️ 9-10 palavras, TODAS nomeando `gelatin trick`.
# ⭐ Quatro portadores da virada, porque na fonte ela vem de lugares diferentes:
# o TEMPO (`nineteen days of`), um TERCEIRO (`a buddy gave him`), ELE MESMO
# (`he found`) e o PROPRIO NARRADOR (`I told him about`) — este ultimo e' do
# operador, e e' o mais forte: ele esta' apontando para o colega EM QUADRO.
# ⛔ Nada de verbo de ereccao (`stands up`, `works again`, `is back`) — licao
# paga em campo no COLO 16, 2026-08-09.
VIRADAS16 = [
    "Nineteen days of the gelatin trick fixed all that.",
    "Then a buddy at work gave him the gelatin trick.",
    "When he discovered the gelatin trick, all that changed.",
    "I told him about the gelatin trick, everything changed.",
    "Three weeks on the gelatin trick and nobody laughs now.",
    "The gelatin trick fixed him in nineteen days flat.",
    "Then his own brother handed him the gelatin trick.",
    "I gave him the gelatin trick, and it all changed.",
    "Two weeks of the gelatin trick shut them all up.",
    "He found the gelatin trick, and the jokes stopped.",
    "The gelatin trick ended every one of those jokes.",
    "I showed him the gelatin trick that same night.",
    # ⛔ 2026-08-10, CONFERENCIA — era `...and she bragged instead.`, e o `she`
    # nao tinha DONO. Medido no sorteio (nao lido no pool): em 12 de 400 videos
    # a virada saia com `she` depois de um hook que nunca nomeia mulher nenhuma
    # (`Half of that company meeting heard his Johnson quit, and they mocked
    # him. Nineteen days of the gelatin trick and she bragged instead.`) — o
    # espectador ouve `she` no segundo 7 e nao tem a quem atribuir. E' o modo de
    # falha "pronome generico e' drifting": nao se escreve frase melhor, nomeia-se
    # o referente. `instead` (instead de que?) saiu junto, e as 10 palavras
    # continuam de pe'. ⚠️ O `medir_deiticos` nao pega isto: ele varre `this`,
    # `that`, `here` — pronome pessoal orfao passa por baixo dele.
    "Nineteen days of the gelatin trick and his wife bragged.",
    "He got the gelatin trick from me, everything changed.",
    # + 2026-08-10, CONTRATO DE COPY 16s. As catorze acima sao do operador e
    # ficam LITERAIS (string validada e' constante). O que faltava era uma
    # FAMILIA em que a virada ja' diz o que a gelatina faz com o SANGUE — o
    # mesmo CT3 que a cena 2 passou a cobrar. Oito novas, todas <= 10 palavras,
    # e as mesmas quatro bocas de sempre (tempo · terceiro · ele · o narrador).
    "Nineteen days of the gelatin trick fixed his blood flow.",
    "A buddy gave him the gelatin trick for blood flow.",
    "He found the gelatin trick, and his blood flow changed.",
    "I gave him the gelatin trick that feeds blood flow.",
    "The gelatin trick gave his blood flow back.",
    "Two weeks of the gelatin trick changed his blood flow.",
    "His brother gave him the gelatin trick for blood flow.",
    "The gelatin trick started his blood flow again.",
]

QUEM_CONTOU = [
    "his own brother", "his brother-in-law", "a guy from the shop",
    "his fishing buddy", "his business partner", "the neighbor",
    "an old army friend", "his own son-in-law",
    # + 2026-08-01: o operador mediu vicio — sempre as mesmas bocas contando
    # o segredo no lote. Quatro fontes novas.
    "his barber", "his old boss", "his cousin", "a man from his gym",
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
    # ⛔⛔ O DEITICO — relato de campo do operador, 2026-08-10, o mesmo defeito
    # que ele pegou no PEE 16 e no NECROSE 16. Os 14 eventos sao DISTAIS
    # (`that dinner table`), mas o narrador esta' SENTADO A MESA, apontando o
    # dedo para o homem ao lado. Dizer "aquela mesa de jantar" de dentro dela
    # e' o dedo apontando para fora de onde ele ja' esta'.
    # ⚠️ Nao e' o tempo verbal: passado sobre cena ao vivo passaria. Quebra o
    # DEDO. ⛔ Corrigido na montagem, nunca no pool — mesma regra dos dois
    # blocos acima.
    if ev.lower().startswith("that "):
        ev = "this " + ev[5:]
    txt = hook.format(evento=ev, o=o)
    # ⚠️ MESMO BUG, OUTRA PREPOSICAO — achado na revisao adversarial de
    # 2026-08-09. Todos os 14 eventos aceitam `at`, menos um: `at that boat` e'
    # agramatical, e o Veo NARRA o erro nos 2 segundos que decidem o scroll.
    # ⛔ Consertado AQUI e nao no pool, pelo mesmo motivo do bloco acima: nem o
    # evento nem as 16 humilhacoes sao redigitados. O errado e' a montagem.
    return re.sub(r"\bat (that boat)\b", r"on \1", txt)


# ⛔ APOSENTADA em 2026-08-10, e fica aqui em vez de sumir porque regra que some
# sem explicacao e' divida. Ela servia ao `_fundir`: o beat do meio reservava a
# MEDIANA do pool seguinte, para nao ser generoso demais nem apertado demais.
# Com a reforma do CONTRATO DE COPY 16s os tres beats depois do MECANISMO
# passaram a ter comprimento FIXO (TRUQUE 6, GATE 3, CTA 8) — reservar a mediana
# de um pool onde minimo = maximo e' a mesma conta que reservar o minimo, com a
# diferenca de mentir sobre o porque. O `_fundir` reserva o minimo e o orcamento
# fecha por construcao (8+6+3+8 = 25).
def _mediana(vals):
    v = sorted(vals)
    return v[len(v) // 2]


def _hook16(oc, o, rng):
    """A cena 1 do 16s: HUMILHACAO + VIRADA, dentro das 24 palavras.

    ⭐ AQUI NAO HA' BEAT ESPREMIDO, e e' de proposito: as faixas foram escritas
    para que 11-14 + 9-10 nunca passe de 24. As duas escolhas sao LIVRES, as
    16 x 14 combinacoes saem todas, e o `_cabe` fica so' como rede — se alguem
    ampliar um pool com entrada longa demais no futuro, ele corta em vez de
    deixar a fala ser cortada no render.

    ⚠️ O `{evento}` varia de 2 a 3 palavras e ISSO ENTRA NO ORCAMENTO — por isso
    a humilhacao e' medida DEPOIS de formatada, nunca no template.
    """
    def _cabe(pool, reserva, fmt=None):
        def _n(x):
            return _palavras(fmt(x) if fmt else x)
        v = [x for x in pool if _n(x) + reserva <= TETO_FALA[1]]
        return v or [min(pool, key=_n)]

    fmt = lambda x: _hook_fmt(x, oc, o)                          # noqa: E731
    hum = fmt(rng.choice(_cabe(
        HUMILHACOES16, min(_palavras(x) for x in VIRADAS16), fmt)))
    vir = rng.choice(_cabe(VIRADAS16, _palavras(hum)))
    return "%s %s" % (hum, vir)


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
        # ⚠️ indice 2: com duas cenas, a fundida E a ultima.
        v = [x for x in pool if _palavras(monta(x)) <= TETO_FALA[2]]
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
        return _hook16(oc, o, rng)
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
    # ⚠️ ISTO E' DO ARCO DE CINCO CENAS e continua valendo la'. No 16s so'
    # `orgaos[0]` chega ao video (MAPA_COPY = (1, None)); as cenas 2-4 sao
    # descartadas pelo colapso, e a fundida repete `orgaos[0]` por ordem do CT4
    # — um apelido por video, nos dois takes. Ver `_fundir`.
    # ⛔⛔ CT4b (2026-08-10) — SO' TRES APELIDOS SAO SORTEAVEIS.
    # Ordem do operador: *"quero que vc use weiner e john-son pra se referir ao
    # orgao tb, nao apenas pec-ker"*. `soldier` soa filme de guerra para ouvido
    # americano e `tool` e' ambiguo em giria dos EUA; os dois seguem no NUCLEO
    # porque as LENTES os usam para DETECTAR o orgao — o que muda e' que nao
    # sao mais sorteaveis. O CT4 trava UM apelido por video; sem isto aqui, um
    # apelido por video vira o MESMO apelido no lote inteiro.
    _o1 = rng.choice(sc.APELIDOS_16)
    orgaos = [_o1] * 4

    falas = [
        _hook16(oc, orgaos[0], rng),
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
                # ⛔⛔ CL25 — O REF SORRI MOSTRANDO OS DENTES. Relato de campo do
        # operador, 2026-08-10: *"os dentes do narrador estao pessimos, parece
        # que estao podres ou que estao prestes a cair"*.
        # A REF dizia so' `calm expression` — boca fechada. Sem dentes na
        # imagem de identidade o Veo INVENTA a dentadura quando a boca abre no
        # take, e inventa mal. E' a mesma licao que o CLEAN pagou em
        # 2026-08-04 e resolveu com esta linha; aqui ela faltava.
        # ⚠️ A ancora e' POSITIVA e vai na REF, nao no TAKE: o take herda o
        # rosto do primeiro frame, entao e' o frame que precisa ter a boca
        # certa. Descrever dente no TAKE chega tarde.
        "REF 01: Photo of a real person, a %d-year-old %s man, chest up, facing camera, "
        "a wide warm natural smile with the lips parted, showing a full row of clean white teeth, the front teeth even, white and complete. The dense build of a man who lifts, thick through the chest and shoulders, forearms corded, skin taut and even. %s. "
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

    # ⚠️ A MULHER E A PLATEIA repetem o riso, e cada repeticao e' uma chance de
    # o modelo gerar som. O silencio anda junto com elas, na mesma sentenca —
    # regra no fim do prompt e' regra descartada (licoes-producao-veo).
    # ⚠️ E o AUDIO nomeia a ausencia, do mesmo jeito que `No music.` ja' faz e
    # funciona: a trilha e' so' o ambiente e a voz de quem narra.
    b["TAKE 01/05"] = (
        "TAKE 01/05: Animate the image exactly. Handheld iPhone, slight sway, "
        "no cuts. %s What he holds stays exactly as shown — %s The woman and "
        "the %s behind her go on laughing the same silent way, mouths open and "
        "no sound leaving them.\n"
        "Dialogue: \"%s\"\nAudio: %s Only that room tone and the speaking "
        "voice — no laughter, no laughing voices, no giggling, no chuckling "
        "anywhere on the track. No music."
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
    # ⛔ 2026-08-10, CONFERENCIA — SEIS DAS CATORZE OCASIOES NAO TINHAM LINHA
    # AQUI, e o `resumo_pt` caia no fallback generico "No evento" em 43% dos
    # sorteios (6/14, medido). O resumo e' onde o operador aprova ou re-sorteia
    # antes de gastar credito: fallback e' o painel dizendo "algum lugar".
    # As seis nasceram depois deste dicionario e ninguem voltou aqui.
    "clube_veteranos": "No clube dos veteranos",
    "boliche": "Na noite de boliche", "lanchonete": "Na lanchonete de estrada",
    "reencontro": "No reencontro de turma", "feira_condado": "Na feira do condado",
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
# ⚠️ DOIS, nao tres. Sai a cena 4 do base (a redencao): e' a que o colapso
# temporal come. Fica a 1 (o flagrante, o hook) e a 3 (a bancada, o payoff).
MAPA = (1, 3)
MAPA_COPY = (1, None)             # None = a fundida
# ⛔⛔ DUAS CENAS. A do meio (a redencao) morre como QUADRO; a fundida
# herda o quadro da CTA e leva o truque para dentro da fala.
CENAS_UI = ["1 · O FLAGRANTE", "2 · O TRUQUE + CTA"]

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

# ⛔⛔ DUAS CENAS no teto FISICO de 25.
# ⚠️ A fundida NAO herda os pools do motor de 24s: a menor FUNDIDA de la'
# tem 23 palavras e o menor CTA 10 — 33 contra teto 25.
TETO_FALA = {1: 24, 2: 25}


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


# ---------------------------------------------------------------------------
# ⭐⭐ A FALA DA CENA FUNDIDA — EIXOS COMPOSTOS (2026-08-09)
# ---------------------------------------------------------------------------
#     {MECANISMO} {O TRUQUE} {GATE} {CTA}       <- ordem de 2026-08-10
#
# ⛔⛔ A ORDEM MUDOU, E E' O CT1 DO CONTRATO DE COPY 16s. Ate' hoje o GATE vinha
# DEPOIS do CTA — `...I'll send the recipe. Hit follow first.` — e isso saiu em
# 100% dos 200 sorteios medidos. A ultima coisa no ouvido, colada no unico
# pedido que gera receita, era um segundo CTA nu. A posicao final e' a que fica;
# ela tem de ser o pedido. ⭐ O follow continua existindo — ele vai ANTES.
#
# ⭐ O ORCAMENTO FECHA POR CONSTRUCAO, nao por solver (a armadilha que ja' custou
# caro duas vezes esta semana):
#       MECANISMO  6-8   ·  TRUQUE  6 fixo  ·  GATE  3 fixo  ·  CTA  8 fixo
#       pior caso  8 + 6 + 3 + 8 = 25 = TETO_FALA[2]
# Nenhuma combinacao das 16 x 14 x 7 x 11 estoura, entao o `_cabe` do `_fundir`
# nunca filtra e NENHUMA entrada fica inalcancavel. E as entradas de cada pool
# tem tamanho PARECIDO de proposito: pool que vai de 6 a 14 palavras num teto de
# 25 nao e' pool de 12, e' pool de 4 com oito enfeites.
#
# ⛔⛔ VERBO NEUTRO DE TRANSFORMACAO, e isso e' lição paga em campo HOJE. No
# COLO 16 o operador mediu ~95% dos takes 1 reprovando no Veo e achou a causa
# testando UMA palavra por vez: trocar `stands up` por `changes` fez o gerador
# APROVAR. Verbo que descreve o orgao voltando a funcionar (`stands up`,
# `wakes up`, `is back`, `works again`) e' lido como tumescencia; `changes`
# nao descreve transformacao nenhuma em particular.
# ⚠️ E a minha primeira correcao la' falhou porque eu troquei o verbo por
# OUTRO jeito de dizer a mesma coisa. Aqui nasce neutro.
#
# ⛔ As ordens do operador que valem para todo pool novo:
#   · nomear e' obrigatorio — nada de pronome sem dono
#   · o CTA nomeia `recipe`, nunca `that exact one`

# ⚠️ 6-8 palavras. O mecanismo do FLAGRANTE e' o FLUXO DE SANGUE, e o contraste
# com a IDADE — e' o que a fonte diz e o que separa este angulo.
# ⛔ 2026-08-10: TRES ENTRADAS CAIRAM POR ORCAMENTO, nao por gosto — `The blood
# flow stopped reaching your {o}. Not age.` (9), `Blood flow to your {o} is the
# whole thing.` (9) e `It's the blood flow to your {o}, nothing else.` (9). Com
# o GATE mudando de lugar (CT1) o take 2 passou a ter quatro batidas e o teto
# de 25 nao comporta 9 aqui. Entraram sete novas de 8, e o pool subiu de 8 para
# 12: encurtar nunca pode virar encolher.
# ⛔ E TODA ENTRADA NOMEIA `your {o}` NA MESMA FRASE DA CAUSA — §17. Frase que
# diz `blood flow` e nao diz o que ela quebra vende circulacao ou coracao, que
# e' outra categoria de produto.
MECANISMOS16 = [
    # ⛔⛔ TODA ENTRADA CARREGA O LITERAL `blood flow`. A regra e' do repo, nao
    # minha: o MUP deste angulo e' a expressao exata, e o linter compartilhado
    # reprova a fala que a perde. A minha primeira versao usava `the blood`,
    # `circulation` e `the years` — 144 de 400 sorteios reprovados.
    "It's blood flow to your {o}, not age.",
    "It's blood flow reaching your {o}, not age.",
    "Your {o} runs on blood flow, not age.",
    "The blood flow to your {o} gave out.",
    "Blood flow to your {o}, not the years.",
    # + 2026-08-10
    "Your {o} lost its blood flow, not age.",
    "Blood flow stopped reaching your {o} years ago.",
    "Blood flow to your {o} got choked off.",
    "Age didn't stop your {o}. Blood flow did.",
    "Your {o} stopped getting blood flow, not age.",
    "Blood flow quit reaching your {o} at fifty.",
    "Your {o} needs blood flow, not another birthday.",
    # ⛔ AS QUATRO ABAIXO SAO CURTAS DE PROPOSITO (6-7 palavras), e entraram
    # depois de MEDIR o lote: com as doze de cima todas em 8 palavras, e os
    # outros tres beats de comprimento fixo, o take 2 saia com EXATAMENTE 25
    # palavras em 400 de 400 sorteios — encostado no teto fisico o video
    # inteiro, sem um dedo de margem. O teto veio de render, e render nao e'
    # deterministico. Agora o take 2 vive em 23-25.
    "Blood flow stopped reaching your {o}.",
    "Your {o} runs on blood flow.",
    "The blood flow to your {o} died.",
    "Blood flow, not age, feeds your {o}.",
]

# ⚠️ 6 palavras EXATAS em todas — o beat de comprimento fixo que fecha o
# orcamento do take 2. ⛔ O literal `gelatin trick` mora AQUI e e' obrigatorio.
# ⛔⛔ E NADA DE QUALIFICADOR COLADO NELE: o `_adjetivo_do_mecanismo` do
# `short_comum` e' ALLOWLIST — so' artigo, numeral, `secret` e `whole` podem
# vir antes do literal. A minha primeira versao tinha `His cousin's gelatin
# trick` e levou 56 reprovacoes em 400. O tempero vem DEPOIS.
#
# ⛔⛔ POOL INTEIRO REESCRITO — CT3 DO CONTRATO DE COPY 16s (2026-08-10).
# Medido: 95% dos videos do FLAGRANTE saiam com o mecanismo como ROTULO NU.
#     antes: "The gelatin trick turns that around."   <- turns O QUE around?
#     antes: "The gelatin trick changes that."        <- muda o que, de que
#                                                        para que?
# Nome de mecanismo sem razao ao lado nao vira crenca, vira ruido de marca. A
# sentenca agora carrega VERBO DE EFEITO + ALVO: o que a gelatina FAZ e COM O
# QUE ela faz — o sangue, que e' o MUP deste angulo.
# ⛔ E o verbo continua NEUTRO — licao paga no COLO 16: nada de `stands up`,
# `works again`, `is back`. Verbo que descreve o orgao voltando a funcionar e'
# lido como tumescencia e reprova no gerador (~95% dos takes 1).
# ⚠️ Metade diz `blood flow` e metade diz so' `the blood`: com o MECANISMO
# imediatamente antes, repetir a expressao inteira nas duas frases seguidas
# martela o ouvido em vez de fixar.
TRUQUES16 = [
    "The gelatin trick restores blood flow.",
    "The gelatin trick opens blood flow.",
    "The gelatin trick fixes blood flow.",
    "The gelatin trick unblocks blood flow.",
    "The gelatin trick clears blood flow.",
    "The gelatin trick keeps blood flowing.",
    # ⛔ 2026-08-10, CONFERENCIA — UMA ENTRADA CAIU E DUAS MUDARAM NA LEITURA EM
    # VOZ ALTA, e nenhuma delas era pega por lente nenhuma: as tres passam no
    # CT3 (tem verbo de efeito e tem alvo) e no teto. O que elas nao passam e' o
    # ouvido de quem escuta UMA vez.
    #   · `loosens blood flow` -> APAGADA. Solta-se o ENTUPIMENTO, nunca o
    #     fluxo; em ingles "loosens blood flow" chega ao contrario (afrouxar o
    #     fluxo = piorar). `opens`, `unblocks` e `clears` ja' dizem a mesma
    #     coisa do jeito certo e ficaram — nao se perde ideia, so' a frase errada.
    #   · `feeds the blood`    -> `feeds blood flow`. O sangue e' quem alimenta;
    #     "feeds the blood" inverte o sentido e deixa o ouvinte sem objeto.
    #   · `holds the blood`    -> `holds blood in`. Sem o `in` a frase pergunta
    #     "segura o sangue ONDE?" — e a preposicao E' o mecanismo deste angulo
    #     (o sangue que nao FICA). E' a formula do proprio CONTRATO, §CT3:
    #     `puts back what holds the blood in`.
    # ⚠️ 14 -> 13 entradas, e as 6 palavras exatas seguem de pe' nas treze.
    "The gelatin trick feeds blood flow.",
    "The gelatin trick moves the blood.",
    "The gelatin trick holds blood in.",
    "The gelatin trick pushes blood through.",
    "The gelatin trick puts blood back.",
    "The gelatin trick brings blood back.",
    "The gelatin trick starts blood moving.",
]

# ⚠️ 8 palavras EXATAS em todas, e TODAS nomeando `recipe`.
# ⛔⛔ POOL INTEIRO REESCRITO — CT6 DO CONTRATO DE COPY 16s (2026-08-10).
# Medido: 100% dos videos saiam com um CTA que nao dizia ONDE a receita chega.
# O KPI deste funil e' uma CONFISSAO PUBLICA: o comentario leva nome e foto e
# vai para o feed da esposa dele. Quanto melhor o diagnostico em 2a pessoa,
# mais caro fica comentar — e em 48 segundos de copy revisada nao havia UMA
# palavra baixando esse custo.
# ⭐ A clausula e' DE GRACA:
#       antes : "Comment gelatin, and I'll send the recipe."          (8)
#       depois: "Comment gelatin, and the recipe goes to your messages."  (8)
# Mesmo custo, e paga (a) o endereco da entrega, (b) a privacidade e (c) o fato
# de que nao e' na tela publica.
# ⛔ 8 -> 11 entradas.
# ⚠️ 2026-08-10 — CONECTOR OBRIGATORIO DEPOIS DA KEYWORD. Medido: 81% dos
# CTAs deste motor saiam como `Comment gelatin, your inbox gets...` — emenda
# de virgula na unica frase do video que gera receita. Sem conector as duas
# oracoes colidem no ouvido e o imperativo (`Comment gelatin`) deixa de soar
# como comando. Custa UMA palavra e havia 3 de folga no teto.
CTAS16 = [
    "Comment gelatin, and the recipe goes to your messages.",
    "Comment gelatin, and the recipe hits your messages.",
    "Comment gelatin, and the recipe lands in your messages.",
    "Comment gelatin, and the recipe arrives in your messages.",
    "Comment gelatin, and I'll send the recipe by message.",
    # ⛔ 2026-08-10, CONFERENCIA — era `and nobody else sees the recipe.` Esta
    # entrada passava no CT6 (o `ENTREGA_16` do short_comum tem `nobody (else )?
    # sees` na allowlist) e falhava na FUNCAO: e' a UNICA das onze que nunca diz
    # que a receita CHEGA a alguem. E o `recipe` aparece uma vez so' no video
    # inteiro — nesta sentenca. O espectador ouvia, na ultima respiracao, uma
    # receita que ele so' sabe que os OUTROS nao veem, e tinha de inferir que
    # ele proprio ganha alguma coisa. Agora diz as duas coisas em 8 palavras:
    # quem recebe (`your messages`) e a exclusividade (`only`).
    "Comment gelatin, and only your messages get the recipe.",
    "Comment gelatin, and the recipe comes to your inbox.",
    # ⚠️ era `I send the recipe in private.` — presente simples nao promete nada
    # em ingles americano ("I send" e' habito, "I'll send" e' promessa). Mesmas
    # 8 palavras: `I'll` conta como um token no `_palavras`.
    "Comment gelatin, and I'll send the recipe in private.",
    "Comment gelatin, and the recipe reaches your inbox.",
    # ⚠️ era `your messages get the recipe tonight.` — `your messages` como
    # SUJEITO de `get` soa a maquina; `your inbox gets` e' o que a boca diz.
    # Mesmas 8 palavras, mesma promessa, mesmo endereco.
    "Comment gelatin, and your inbox gets the recipe tonight.",
    "Comment gelatin, and the whole recipe hits your inbox.",
]

# ⚠️ 3 palavras EXATAS, FRASE SEPARADA — nunca colada no `Comment gelatin,`: a
# automacao de DM casa palavra EXATA.
# ⛔ 2026-08-10: `Followers only.` (2) e `Follow first, or it won't send.` (6)
# sairam. A segunda por orcamento; a primeira porque, com o gate agora ANTES do
# CTA (CT1), uma condicao nua no meio do folego lê como recusa antecipada.
# ⛔ Regra de 2026-08-01 mantida: no maximo 2 entradas com o vocativo
# `brother`, e a maioria sem vocativo nenhum. Aqui ha' uma. 5 -> 7 entradas.
# ⛔⛔ POOL APOSENTADO EM 2026-08-10 — ELE NAO CHEGA MAIS AO VIDEO.
# Ordem do operador: *"nao acho que deva ter follow me no cta, a mensagem e'
# enviada independente de seguirem ou nao"* (CT8 do CONTRATO-COPY-16S).
# O gate existia no repo inteiro por uma PREMISSA ERRADA sobre a automacao de
# DM, e quem opera a automacao corrigiu a premissa.
# ⚠️ POR QUE NAO FOI APAGADO: o autoteste e os contratos deste motor ainda o
# validam (contagem minima, vocativo, tamanho), e apagar exigiria mexer neles
# no mesmo commit em que a copy inteira mudou — duas cirurgias de uma vez e'
# como se perde o rastro do que quebrou o que.
# ⛔ ENTAO FICA ESTE AVISO: melhorar as entradas abaixo NAO muda um unico
# video. Se o follow voltar um dia, ele volta ANTES do CTA (CT1) e por decisao
# do operador, nao por alguem reativar a variavel.
GATES16 = [
    "Hit follow first.",
    "Follow, then comment.",
    "Follow me first.",
    "Tap follow first.",
    "Hit follow now.",
    "Follow before commenting.",
    "Follow me, brother.",
]


def _sem_eco(pool, fala1):
    """Tira do pool da cena 2 o truque cujo VERBO a cena 1 ja' gastou.

    ⛔ NASCEU DE UMA CONSEQUENCIA, nao de gosto. Quando o operador mandou nomear
    o `gelatin trick` ja' na cena 1 (2026-08-09), o literal passou a aparecer nas
    DUAS cenas — o que e' bom, martela a keyword. O que nao pode e' vir com o
    MESMO verbo colado nele oito segundos depois:

        cena 1: "When he discovered the gelatin trick, all that changed."
        cena 2: "The gelatin trick changes that."        <- disco arranhado

    Compara os radicais de 5 letras das palavras que vem DEPOIS do literal, dos
    dois lados. ⚠️ Radical, nao palavra: `changed` e `changes` sao o mesmo eco
    para o ouvido, e comparar a palavra inteira nao pegaria nenhum dos dois.
    ⚠️ Fallback e' o pool inteiro — filtro que zera nao pode zerar a escolha.

    ⛔⛔ O MUP NAO CONTA COMO ECO — conserto de 2026-08-10, e sem ele esta lente
    teria morrido calada. Com o CT3 a cena 2 passou a dizer `blood flow` ou
    `the blood` depois do literal em 14 de 14 truques, e a cena 1 diz o mesmo em
    8 das 22 viradas. Como `blood` e' radical de 5 letras, o filtro casava em
    TODAS as entradas nessas combinacoes, zerava, caia no fallback — e o guarda
    de eco do VERBO, que e' a razao de existir da funcao, deixava de existir sem
    nenhum aviso. `blood`/`flow` sao a expressao que o motor e' OBRIGADO a
    repetir; eco de MUP e' martelo, nao disco arranhado.
    """
    isentas = {"blood", "flow", "flows", "flowing"}

    def _radicais(txt):
        d = txt.lower().split("gelatin trick", 1)[-1]
        return {w[:5] for w in re.findall(r"[a-z]{5,}", d)
                if w not in isentas}

    gastos = _radicais(fala1)
    v = [x for x in pool if not (_radicais(x) & gastos)]
    return v or pool


def _fundir(spec, rng):
    """A cena fundida do 16s — reconstruida, nao herdada.

    ⛔ Os pools de 24s nao servem: a menor FUNDIDA de la' tem 23 palavras e o
    menor CTA 10, e 33 nao cabe em 25. Aqui sao quatro beats curtos.
    ⛔⛔ QUEM ESCOLHE PRIMEIRO RESERVA O MINIMO; QUEM ESCOLHE NO MEIO RESERVA A
    MEDIANA — regra medida no ESCANDALO 16, dos dois defeitos opostos.

    ⭐⭐ 2026-08-10 — A MEDIANA SAIU E O ORCAMENTO PASSOU A FECHAR NA MAO. Com
    TRUQUE, GATE e CTA de comprimento FIXO (6, 3 e 8) e o MECANISMO em 6-8, o
    pior caso e' 8+6+3+8 = 25, que e' o teto. Reservar mediana so' faz sentido
    quando o beat seguinte tem faixa larga — aqui ele nao tem, e reservar
    mediana passaria a CORTAR entradas legitimas de vez em quando. O `_cabe`
    continua no lugar como rede: se alguem ampliar um pool com entrada longa
    demais no futuro, ele filtra em vez de deixar a fala ser cortada no render.

    ⛔⛔ CT1: a ordem e' MECANISMO · TRUQUE · GATE · CTA. O video TERMINA no
    pedido. O gate vinha depois em 100% dos sorteios ate' hoje.
    ⛔⛔ CT4: o apelido do orgao sai da CENA 1, nao da cena 4 do arco longo.
    Era `falas_base[3]` — a redencao, uma cena que o colapso 5->3 COME — e por
    isso o apelido mudava no corte em 100% dos videos. Em 24s e cinco cenas o
    bordao e' o risco; em 16s e duas cenas o risco e' o oposto: o corte zera a
    memoria de trabalho, e trocar `pecker` por `Johnson` no segundo 9 obriga o
    espectador a remapear justamente quando ele ja' esta' com um pe' fora.
    ⚠️ Le de `spec["falas"][0]` e nao de `falas_base[0]` de proposito: as duas
    apontam para a MESMA string durante o sorteio, mas quando o operador
    re-sorteia so' a cena 1 pelo app e' `falas` que muda — e o apelido tem de
    acompanhar, senao o botao do painel quebra o CT4 em silencio.
    """
    o = sc.orgao_de(_LONGO, (spec.get("falas") or spec["falas_base"])[0])

    def _cabe(pool, reserva):
        def _n(x):
            return _palavras(x.format(o=o))
        v = [x for x in pool if _n(x) + reserva <= TETO_FALA[2]]
        return v or [min(pool, key=_n)]

    _mn_t = min(_palavras(x) for x in TRUQUES16)
    _mn_c = min(_palavras(x) for x in CTAS16)
    _mn_g = min(_palavras(x) for x in GATES16)

    # ⚠️ `falas_base[0]` E' A CENA 1 — `spec["falas"]` ainda nao existe aqui: e'
    # o `sortear_curto` que a monta DEPOIS, com o resultado desta funcao dentro.
    truques = _sem_eco(TRUQUES16, spec["falas_base"][0])

    # ⛔ ORDEM DE ESCOLHA (nao e' a ordem da frase): escolhe primeiro quem tem
    # MENOS substitutos. O CTA carrega o literal `Comment gelatin,` e a
    # cobertura de entrega — e' o beat que nao se pode encurtar — entao ele sai
    # primeiro, reservando o minimo dos outros tres. O GATE, que e' o mais
    # intercambiavel dos quatro, sai por ULTIMO e absorve a sobra.
    cta = rng.choice(_cabe(CTAS16, _mn_t + _mn_g
                           + min(_palavras(x.format(o=o))
                                 for x in MECANISMOS16)))
    mec = rng.choice(_cabe(MECANISMOS16,
                           _palavras(cta) + _mn_t + _mn_g)).format(o=o)
    tru = rng.choice(_cabe(truques, _palavras(mec) + _palavras(cta) + _mn_g))
    # ⛔⛔ CT8 (2026-08-10) — O BEAT DO FOLLOW SAIU DA FALA.
    # Ordem do operador: *"nao acho que deva ter follow me no cta, a
    # mensagem e' enviada independente de seguirem ou nao"*. O gate
    # existia no repo inteiro por uma PREMISSA ERRADA sobre a automacao
    # de DM, e quem opera a automacao corrigiu. As palavras liberadas
    # vao para o mecanismo e a prova.
    return "%s %s %s" % (mec, tru, cta)


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
    # ⛔⛔ SO' A BANCADA. A `redencao_com_ref` montava a cena 2 do motor de 24s,
    # e essa cena e' justamente a que o colapso temporal come. A fundida herda o
    # quadro da bancada com rosto — o payoff — e leva o truque para a fala.
    # ⚠️ `n=2, total=2`: sem isso a helper rotula `03/03` num video de duas
    # cenas, e a AdBatch Vertical 2 CONTA os rotulos.
    # ⭐ 2026-08-10 — `sache_erguido`: copo ja' pronto e roxo, sache rotulado
    # erguido na mao. Ordem do operador com dois renders na mao — o modo antigo
    # entregava ele MEXENDO AGUA TRANSPARENTE, sem gelatina nenhuma em quadro.
    # ⛔ O modo e' so' deste motor: os outros cinco que chamam esta funcao
    # seguem no `colher` e nao foram tocados.
    i2, t2 = sc.bancada_com_rosto(_LONGO, spec, spec["falas"][1], n=2, total=2,
                                  modo="sache_erguido")
    b["IMAGE 02/02"], b["TAKE 02/02"] = i2, t2
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
    """O prop na mao tem de ser declarado imovel no TAKE.

    ⛔⛔ DUAS COISAS ESTAVAM CRAVADAS AQUI e as duas quebraram no porte:
      · o rotulo `TAKE %02d/03` — num video de duas cenas o bloco chama-se
        `TAKE 01/02`, e a lente estourava com `KeyError`;
      · a lista `(1, 4)` — a cena 4 do motor base e' a redencao, que o colapso
        temporal COME. `MAPA.index(4)` nao existe mais.
    ⭐ Agora as duas saem do MAPA: o total e' `len(MAPA)` e so' se cobram as
    cenas do base que de fato sobreviveram ao colapso.
    """
    total = len(MAPA)
    for cena in (1, 4):
        if cena not in MAPA:
            continue
        nome = "TAKE %02d/%02d" % (MAPA.index(cena) + 1, total)
        if "motionless" not in blocos[nome].lower():
            achados.append(("ERRO", "%s sem declaracao de imobilidade do prop" % nome))


def _ct16(spec, blocos, achados):
    """As sete travas do CONTRATO DE COPY 16s, cobradas de dentro do motor.

    ⭐ `isca_absurda=False`: o FLAGRANTE nao promete nada no take 1 que ele
    mesmo va' desmentir — a cena 1 e' humilhacao publica + virada, nao substancia
    absurda. Por isso o CT7 (verbo de ereccao colado no orgao) vale nos DOIS
    takes aqui, e nao so' no do CTA.
    ⚠️ `sys.modules[__name__]` e nao `_LONGO`: a lente le' `base.NUCLEO`, e o
    NUCLEO e' deste modulo. `_LONGO` tambem o carrega, mas passar o modulo
    e' o contrato escrito no `short_comum` — um lugar so' de onde ler.
    """
    sc.lint_copy16(sys.modules[__name__], spec, achados, isca_absurda=False)


# ⛔⛔ LENTE APOSENTADA, e a aposentadoria e' declarada aqui porque a regra mora
# no `short_comum` (compartilhado — nao se mexe nele por um motor so').
#
#   `lint_curto` emite  AVISO "substantivo repetido no video: [...]"  quando o
#   mesmo apelido do orgao aparece em mais de uma cena. Essa regra nasceu no
#   arco de CINCO cenas, onde duas mencoes iguais em 24 segundos viram bordao.
#
#   O CT4 do CONTRATO DE COPY 16s REVERTE isso para a familia de dois takes, e a
#   reversao esta' medida: com dois takes o apelido mudava no corte em 100% dos
#   videos deste motor. Em 16 segundos o corte ZERA a memoria de trabalho — o
#   espectador ouve `pecker` no segundo 7 e `Johnson` no segundo 9 e tem de
#   remapear justamente quando ja' esta' com um pe' fora. A variacao continua
#   existindo ENTRE videos, que e' onde ela nunca custou nada.
#
# Logo: o AVISO passou a acusar exatamente o que o contrato EXIGE. Ele e'
# descartado abaixo — nao silenciado no `short_comum`, que serve os 19 motores
# de tres cenas onde a regra antiga continua valendo.
_APOSENTADA_CT4 = "substantivo repetido no video"


def _cl25_dentes(spec, blocos, achados):
    """⛔ O REF tem de sorrir mostrando os dentes — CL25, 2026-08-10.

    Sem esta ancora na imagem de identidade o Veo inventa a dentadura quando a
    boca abre no take, e inventa podre. Foi relato de campo com render na mao.
    ⚠️ A lente olha o REF, nao o TAKE: o take herda o rosto do primeiro frame.
    """
    ref = blocos.get("BLOCO 0 (REF)", "")
    for pedaco in ("natural smile", "clean white teeth", "even, white and complete"):
        if pedaco not in ref:
            achados.append(("ERRO", "CL25: o REF nao declara %r — sem dentes na "
                                    "imagem de identidade o Veo inventa banguelo"
                                    % pedaco))


def lint(spec, blocos):
    achados = sc.lint_curto(
        _LONGO, spec, blocos, MAPA, TETO_FALA,
        literais=("gelatin trick", "blood flow"),
        extras=(_imobilidade, _ct16, _cl25_dentes))
    return [(n, m) for n, m in achados
            if not (n == "AVISO" and m.startswith(_APOSENTADA_CT4))]


# ---------------------------------------------------------------------------
# RESUMO
# ---------------------------------------------------------------------------

def resumo_pt(spec):
    """⛔ 2026-08-10, CONFERENCIA — O RESUMO DESCREVIA TRES CENAS NUM MOTOR DE
    DUAS, e ainda punha o CTA numa cena 3 que nao existe desde que este arquivo
    nasceu. E' texto de painel, nao copy falada — mas e' o UNICO lugar onde o
    operador le' o video ANTES de gastar credito gerando, e resumo errado faz
    ele aprovar o que nao viu (licoes-de-construcao §30; o mesmo defeito ja'
    foi consertado no TRIO 16 e no FALTA 16 com essa justificativa).
    ⭐ Agora ele diz o que o AdBatch Vertical 2 vai receber: dois takes, a
    virada com o `gelatin trick` ja' dentro do take 1, e o pedido por ultimo
    (que e' o CT1 do CONTRATO DE COPY 16s).
    """
    et = "branca" if "white" in ETNIA[spec["pagina"]] else "negra"
    return ("16s, DOIS takes. Take 1: %s, o colega segura %s no próprio colo "
            "enquanto o narrador aponta e a mesa ri — e a virada com o gelatin "
            "trick vem ainda aí. Take 2: a bancada com rosto — o sangue como "
            "causa, o truque, o follow, e o CTA por último. Elenco de pele %s."
            % (PT_OCASIAO.get(spec["ocasiao"]["id"], "No evento"),
               spec["prop"].get("pt", "o prop"), et))
