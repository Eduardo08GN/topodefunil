#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE NECROSE SHORT — 3 cenas de 8 segundos.

⭐ 2026-08-03 — ESTE ARQUIVO E' A FONTE DA VERDADE DO ANGULO NECROSE.
Ele derivava de `necrose_lucas.py` e herdava de la' as strings travadas, os
pools sorteaveis, as tabelas de token banido e o motor de 5 cenas. Os `*_lucas`
sao de terceiro e saem do repo de trabalho, entao tudo o que era herdado foi
COPIADO PARA CA', caractere por caractere. Nao ha' mais nenhum `import
*_lucas`: correcao de regra do NECROSE entra NESTE arquivo.

O colapso (decisao do operador, 2026-07-31):

    arco 1 · A COMPARACAO   ->  SHORT 1 · O HOOK
    arco 4 · A PROVA        ->  SHORT 2 · RITUAL + PROVA   (a copy funde 3 e 4)
    arco 5 · CTA            ->  SHORT 3 · CTA

⚠️ A IMAGEM da cena 2 e' a do PAYOFF (o geoduck erguido, NE11), nao a da
bancada do ritual. A copy fundida termina em deitico — "came back like this" —
e esse "this" precisa ter no que apontar. O ritual vive na fala; o resultado,
no quadro.

⛔ O QUE O COLAPSO AMEACAVA
As cenas 2 e 3 do arco longo levam embora DUAS coisas obrigatorias: o literal
`gelatin trick` (que morava nas RECEITAS_FALA da cena 3) e o MUP `blood flow`
(que morava nas CAUSAS da cena 2). Sem o primeiro o criativo deixa de ser
congruente com o que a VSL vende; sem o segundo o video promete sem explicar.
Por isso **os dois entram na copy fundida**, e o linter trava nos dois.

Some-se o NE10: a placa D1 em corte sagital era a cena 2 e nao sobrevive. Ela
e' a peca que EXPLICA, e no SHORT nao ha' tempo para explicar — a explicacao
virou a oracao de `blood flow` dentro da cena 2.
"""

import os
import re
import sys
import types

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import short_comum as sc                                       # noqa: E402
from nucleo_sonoro import sonorizar                            # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(AQUI, ".necrose-short-ledger.json")

TITULO = "AGENTE NECROSE SHORT"
SUBTITULO = "os dois órgãos lado a lado, em 3 cenas · gerador offline de prompts Veo"
SLUG = "necrose-short"


# ###########################################################################
# ⭐ BLOCO INLINEADO — 2026-08-03
# ###########################################################################
# Ate' hoje tudo daqui ate' o fim do bloco chegava importado do motor `_lucas`
# e era lido como `base.X`. Os `*_lucas` sao de um terceiro e saem do repo de
# trabalho, entao este motor virou AUTOSSUFICIENTE: as definicoes foram
# copiadas LITERALMENTE de la', com os comentarios originais, que sao a memoria
# da regra. Deste dia em diante ESTE arquivo e' a fonte da verdade do NECROSE.
#
# Foi renomeado o que colidia com nome ja' existente no SHORT, e so' isso:
#   TETO_FALA -> TETO_FALA_LONGO   (o do arco de 5 cenas)
#   sortear   -> _sortear_longo
#   montar    -> _montar_longo
#   nova_fala -> _nova_fala_longo
# Nenhum texto de prompt, pool de copy ou string travada foi tocado.
# ###########################################################################


# ---------------------------------------------------------------------------
# STRINGS TRAVADAS — copia literal da doutrina. NAO REESCREVER, NAO COMPRIMIR.
# ---------------------------------------------------------------------------

# NE1 — o prop NAO e' o D1. O D1 e' placa chapada em corte sagital e serve para
# EXPLICAR; aqui sao modelos 3D inteiros em suporte e servem para COMPARAR.
# ⛔ Nunca "the male reproductive system": categoria faz o gerador escolher o
# corte, e ele escolhe o mais comum do treino (torso abdominal / esqueleto).
SUPORTE = ("mounted upright on a slim chrome stand with a square steel base, "
           "the kind that sits on a urology office desk")

# NE2 — a deterioracao e' em CINCO EIXOS simultaneos: cor, superficie, volume,
# contorno e eixo. NUNCA em tamanho. "damaged"/"unhealthy"/"small" nao
# descrevem nada — o Veo normaliza para dois modelos parecidos e o angulo morre.
# ⚠️ A PECA E' O ORGAO INTEIRO, NAO A BEXIGA (correcao do operador,
# 2026-07-30). A primeira versao dizia "the bladder and the tube below it" e o
# Veo entregou o minimo: uma bexiga com um toco. O print da fonte mostra a
# massa arredondada no topo E um EIXO LONGO E GROSSO descendo, com o canal
# interno em corte e o corpo oval na base. A geometria tem que estar escrita:
# comprimento relativo ("twice as long as the bladder is wide"), direcao
# ("forward and down") e as tres partes nomeadas.
GEOMETRIA = (
    "The model shows, from top to bottom: a rounded bladder at the top; then a "
    "long thick cylindrical shaft running forward and downward from it, which "
    "makes up more than half the total height of the whole model, with its "
    "inner channel cut away along its entire length and a rounded cap at the "
    "far end; and a single oval gland hanging in a loose sac at the base of "
    "that shaft"
)

MODELO_PODRE = (
    "On the left, a free-standing three-dimensional male reproductive anatomy "
    "teaching model, %s. %s. This one is the old one. The bladder at the top "
    "is dark walnut-brown, shrivelled and knotted, its surface dull, dry and "
    "cracked, covered in irregular lumps and deep creases like a dried root. "
    "Two thin cords twist away from it, withered and darkened like dry twigs. "
    "The long shaft below is shrunken and crooked, pinched in at several "
    "points along its length, its surface grey-brown and wrinkled, the cut-away "
    "channel inside it narrowed to a thread, ending in a small shrunken "
    "darkened cap. The oval gland at its base is dark and puckered and the sac "
    "around it is shrivelled. Nothing on this model reflects light."
    % (SUPORTE, GEOMETRIA)
)

# "identical" na abertura e OBRIGATORIO: sem ele o Veo desenha dois objetos de
# especies diferentes e a comparacao — que e o video inteiro — some.
MODELO_SAO = (
    "On the right, an identical free-standing three-dimensional male "
    "reproductive anatomy teaching model, %s. %s. This one is the new one. The "
    "bladder at the top is pale salmon pink, full and smooth, its surface "
    "glossy and catching the light. Two clean straight cream-coloured tubes "
    "run from it. The long shaft below is thick, straight and full along its "
    "entire length, its surface smooth pale pink, the cut-away channel inside "
    "it wide and open in darker pink, ending in a full rounded pink cap. The "
    "oval gland at its base is smooth and full and the sac around it is plump."
    % (SUPORTE, GEOMETRIA)
)

# NE11 - A CENA 4 E O GEODUCK GIGANTE COM O SIFAO ERETO (ordem do operador,
# 2026-07-30). O payoff deixa de ser o modelo sao e passa a ser o proxy falico
# ereto — o padrao de climax do F15, e o geoduck ja tem lote validado atras
# dele. Consequencia de arco: a COMPARACAO acontece toda na cena 1; a cena 4
# nao repete o modelo, ela ENTREGA a promessa em outro objeto.
#
# ⚠️ SPEC DIMENSIONAL OBRIGATORIA: "ereto" sozinho sai timido — o Veo entrega o
# tamanho natural do molusco, e prop de tamanho natural nao e promessa nenhuma
# (falha em producao, Chuck/colo v3). Dimensiona-se por BIOLOGIA DO PROP e
# ESCALA CORPORAL, nunca por anatomia nem por comparacao ao "normal": a versao
# com engorged / raised veins / a third thicker foi RECUSADA (Chuck/colo v4).
GEODUCK_PAYOFF = (
    "a very large geoduck clam, gripping the pale ridged shell. Its siphon "
    "rises straight up out of the shell, held stiff and straight, as long as "
    "his forearm and as thick as his wrist, reaching well above the top of his "
    "head, its surface taut and glossy, streaked with darker mottled lines "
    "running along its length. No bird, no goose, no duck, no swan, no snake, "
    "no feathers, no beak, no eyes, no head, nothing alive."
)

# ⛔ No TAKE nunca se escreve "geoduck" (so no IMAGE) nem "neck" (e "siphon").
# E o estado vive no IMAGE: vocabulario de firme<->murcho em prompt de
# movimento derruba a geracao de video mesmo com o IMAGE aprovado.
GEODUCK_TAKE = (
    "The clam stays exactly as it appears in the first frame — same position, "
    "same angle, same shape — completely motionless for the entire shot. It is "
    "a still object and nothing about it changes. No bird, no goose, no duck, "
    "no swan, no snake, no worm, no tentacle, no feathers, no beak, no eyes, "
    "no head, nothing alive, nothing with a face."
)

# NE10 - A CENA 2 E O D1: A PLACA EM CORTE SAGITAL, ERGUIDA POR ELE
# (ordem do operador, 2026-07-30, depois da recusa da IMG 02).
# O D1 e a peca que EXPLICA — e a cena 2 e a explicacao. Antes ela erguia o
# modelo podre em close, que foi o unico bloco recusado do lote. O D1 tem DOIS
# renders validados atras dele, entao a troca nao e uma reformulacao com risco:
# e a substituicao de um bloco 0-render por um bloco 2-renders.
# Consequencia de arco: o modelo podre passa a existir SO na cena 1, no
# pedestal. Ele nunca mais vai para a mao.
# ⛔ Copia literal de prop-metaforas.md §D1. NAO REESCREVER, NAO COMPRIMIR:
# comprimir esta string ja entregou esqueleto 3D no lugar da placa.
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

# NE8 — no TAKE nenhum dos dois muda de estado. A comparacao e' entre DOIS
# OBJETOS, nao uma transformacao: nada apodrece nem sara na tela.
IMOBILIDADE_PAR = (
    "Both models stay exactly as they appear in the first frame — same colour, "
    "same shape, same surface — nothing about either one changes, and neither "
    "leaves its stand."
)
IMOBILIDADE_UM = (
    "The model stays exactly as it appears in the first frame — same colour, "
    "same shape, same surface — nothing about it changes, and it never turns "
    "or tilts."
)

# NE4 — o lobo e' prop de STATUS masculino (a alavanca do leao do Kofi), nao de
# credibilidade medica. ⛔ nunca dog, nunca husky, nunca deitado.
LOBO = ("%s standing behind him on his right, head turned toward the camera, "
        "in focus")

ANTICELEB = "Ordinary relatable face, not a celebrity."
CAUDA = "Shot on iPhone, natural grain. No on-screen text, no watermark."

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
    # lote 1 (2026-07)
    "joe": "white American", "ray": "white American", "matt": "white American",
    "marcus": "Black American", "chuck": "Black American",
    # ⭐ lote 2 (2026-08-03) — as cinco paginas novas do Facebook. A chave e
    # a etnia saem do AVATAR REAL da pagina, nao de preferencia: a
    # congruencia inviolavel do repo e etnia do REF = etnia do avatar.
    #   Hank Male Tips Hub ....... clara   -> secondwindformen.site
    #   Wade All Natural Hub ..... clara   -> strengthandflow.site
    #   Isaiah Vitality Men Tips . escura  -> dailyvitalitymethod.site
    #   Curtis Reset Hub ......... escura  -> menresethub.site
    #   Otis Men Reset Hub ....... escura  -> mensresetclub.online
    # Pareamento pagina<->bridge: funil-organico/automacao-comentario-dm.md
    "hank": "white American", "wade": "white American",
    "isaiah": "Black American", "curtis": "Black American",
    "otis": "Black American",
}

# ---------------------------------------------------------------------------
# POOLS SORTEAVEIS
# ---------------------------------------------------------------------------

# NE5 - O ARQUETIPO E UM EIXO SO: CENARIO + CHAPEU + ANIMAL.
# Antes cenario e persona eram eixos separados, e o sorteio podia cruzar um
# deserto do Texas com chapeu de montanhes alpino. O arquetipo carrega os tres
# juntos porque eles nao sao independentes - chapeu errado no cenario certo
# destroi a leitura em meio segundo.
#
# O ANIMAL saiu do NE4 como "lobo" e virou "animal selvagem de status,
# congruente com o arquetipo" (extrapolacao pedida pelo operador 2026-07-30).
# A regra que importa continua de pe: e prop de DOMINANCIA, nunca bicho de
# estimacao. PROIBIDO cachorro, husky, gato, animal deitado ou de coleira.
#
# selo: V = arquetipo da fonte - N = extrapolacao nossa
ARQUETIPOS = [
    # ---- montanhes alpino (o arquetipo da fonte) ----
    {"id": "montanhes_cabana", "selo": "V", "familia": "montanhes",
     "set": "a rocky alpine mountaintop, snow-capped peaks filling the "
            "background, a small stone cabin with a chimney at frame-left, "
            "lichen-covered rock in the foreground, clear blue sky",
     "curto": "the same mountaintop",
     "chapeu": "a wide-brimmed brown leather hat with a braided cord band",
     "animais": ["a full-grown grey wolf", "a full-grown white arctic wolf"],
     "luz": "Clear high-altitude daylight, cool and bright, soft shadows.",
     "audio": "high wind over rock, a distant bird"},
    {"id": "montanhes_lago", "selo": "N", "familia": "montanhes",
     "set": "a rocky ledge above a glacier lake, snow-capped peaks across the "
            "water, scattered boulders, no buildings anywhere",
     "curto": "the same ledge above the lake",
     "chapeu": "a battered wide-brimmed felt hat",
     "animais": ["a full-grown grey wolf", "a full-grown black wolf"],
     "luz": "Clear high-altitude daylight, cool and bright, soft shadows.",
     "audio": "high wind, water lapping far below"},
    {"id": "montanhes_pinheiros", "selo": "N", "familia": "montanhes",
     "set": "a high clearing at the treeline, dark pine forest behind him and "
            "bare snow peaks rising above it, moss and lichen on the rocks",
     "curto": "the same clearing",
     "chapeu": "a wide-brimmed oiled canvas hat",
     "animais": ["a full-grown grey wolf", "a full-grown black wolf"],
     "luz": "Cool overcast mountain daylight, flat and even.",
     "audio": "wind through pines, a distant bird"},

    # ---- cowboy ----
    {"id": "cowboy_curral", "selo": "N", "familia": "cowboy",
     "set": "a ranch corral at golden hour, a weathered split-rail fence "
            "behind him, dry pasture and low hills beyond it, dust in the air",
     "curto": "the same corral",
     "chapeu": "a sweat-stained tan cowboy hat",
     "animais": ["a big chestnut quarter horse", "a heavy longhorn bull"],
     "luz": "Low golden hour sunlight from frame-left, long shadows.",
     "audio": "cattle lowing, wind over dry grass"},
    {"id": "cowboy_mesa", "selo": "N", "familia": "cowboy",
     "set": "a red rock desert mesa, layered canyon walls behind him, dry "
            "brush and cracked ground, a wide empty sky",
     "curto": "the same mesa",
     "chapeu": "a black wide-brimmed cowboy hat",
     "animais": ["a big black stallion", "a lone coyote"],
     "luz": "Hard desert sunlight, warm and high-contrast.",
     "audio": "dry wind, a distant hawk"},

    # ---- nativo norte-americano ----
    {"id": "nativo_planicie", "selo": "N", "familia": "nativo norte-americano",
     "set": "high open plains under an enormous sky, tall dry grass moving in "
            "the wind, a hide-covered lodge far behind him",
     "curto": "the same plain",
     "chapeu": "a beaded leather band across his forehead",
     "animais": ["a full-grown grey wolf", "a spotted paint horse"],
     "luz": "Wide prairie daylight, warm and even.",
     "audio": "wind across open grass"},
    {"id": "nativo_canyon", "selo": "N", "familia": "nativo norte-americano",
     "set": "the mouth of a sandstone canyon, red rock walls rising on both "
            "sides, a shallow river running over stones behind him",
     "curto": "the same canyon mouth",
     "chapeu": "a strip of woven cloth tied around his head",
     "animais": ["a full-grown grey wolf", "a golden eagle on a rock"],
     "luz": "Warm reflected canyon light, soft and glowing.",
     "audio": "water over stones, wind in the canyon"},

    # ---- redneck ----
    {"id": "redneck_varanda", "selo": "N", "familia": "redneck",
     "set": "the porch of a weathered wooden farmhouse in the rural South, an "
            "old pickup truck out of focus in the yard, tall trees behind it",
     "curto": "the same porch",
     "chapeu": "a faded trucker cap pushed back on his head",
     "animais": ["a heavy longhorn bull behind the fence",
                 "a big wild boar at the treeline"],
     "luz": "Warm late afternoon sunlight, soft shadows.",
     "audio": "cicadas, a screen door creaking"},
    {"id": "redneck_celeiro", "selo": "N", "familia": "redneck",
     "set": "the open door of a weathered red barn, stacked hay bales behind "
            "him, a dirt yard and tall grass beyond",
     "curto": "the same barn door",
     "chapeu": "a sweat-stained trucker cap",
     "animais": ["a big chestnut quarter horse", "a heavy longhorn bull"],
     "luz": "Warm afternoon sunlight raking in through the barn door.",
     "audio": "wind in dry grass, a distant tractor"},

    # ---- curandeiro / herbalista ----
    {"id": "curandeiro_apalache", "selo": "N", "familia": "curandeiro",
     "set": "the porch of a log cabin deep in the Appalachian woods, bunches "
            "of dried herbs hanging from the beams and rows of glass jars on a "
            "shelf behind him, dense green forest beyond",
     "curto": "the same cabin porch",
     "chapeu": "no hat, his long gray hair loose",
     "animais": ["a full-grown black bear at the treeline",
                 "a great horned owl on the porch rail"],
     "luz": "Soft green forest daylight, low contrast.",
     "audio": "insects, wind in the leaves"},
    {"id": "curandeiro_pantano", "selo": "N", "familia": "curandeiro",
     "set": "a wooden landing at the edge of a cypress swamp, moss hanging "
            "from the branches, a flat-bottomed boat tied up behind him, still "
            "dark water",
     "curto": "the same landing",
     "chapeu": "a frayed straw hat",
     "animais": ["a big alligator on the bank", "a great blue heron"],
     "luz": "Warm hazy swamp light, soft and diffused.",
     "audio": "frogs, water moving under the boards"},

    # + 2026-08-01: o operador mediu vicio no lote - os mesmos cenarios
    # voltando. Um set novo por familia, com chapeu e animais congruentes.
    {"id": "montanhes_rio", "selo": "N", "familia": "montanhes",
     "set": "a gravel bar on a wide mountain river, fast grey water running "
            "past behind him, snow-dusted peaks upstream, bare cottonwoods "
            "on the far bank",
     "curto": "the same river bar",
     "chapeu": "a fur trapper's hat with the ear flaps tied up",
     "animais": ["a full-grown grey wolf", "a full-grown black bear"],
     "luz": "Flat cold river-valley daylight, silver and even.",
     "audio": "running water, wind over gravel"},
    {"id": "cowboy_moinho", "selo": "N", "familia": "cowboy",
     "set": "a windmill and stock tank alone in open grazing land, the "
            "rusted steel vanes turning slowly behind him, a flat horizon in "
            "every direction",
     "curto": "the same windmill",
     "chapeu": "a pale straw cowboy hat with a tightly curled brim",
     "animais": ["a heavy longhorn bull", "a rangy buckskin horse"],
     "luz": "High dry sunlight, hard and clean.",
     "audio": "the windmill creaking, wind over open ground"},
    {"id": "nativo_butte", "selo": "N", "familia": "nativo norte-americano",
     "set": "the flat top of a butte at first light, the shadowed valley far "
            "below, a line of dark hills on the horizon, loose stone "
            "underfoot",
     "curto": "the same butte top",
     "chapeu": "a flat-brimmed black hat with a low crown",
     "animais": ["a full-grown grey wolf", "a lone coyote"],
     "luz": "Low first light from frame-right, long cold shadows.",
     "audio": "thin wind, a distant coyote"},
    {"id": "redneck_lago", "selo": "N", "familia": "redneck",
     "set": "a gravel boat ramp at a farm pond, a flat aluminium boat pulled "
            "half out of the water behind him, cattails and low woods around "
            "the far bank",
     "curto": "the same boat ramp",
     "chapeu": "a camouflage cap with a frayed brim",
     "animais": ["a full-grown wild boar", "a heavy longhorn bull"],
     "luz": "Bright hazy midday light coming off the water.",
     "audio": "water slapping the boat, bullfrogs"},
    {"id": "curandeiro_clareira", "selo": "N", "familia": "curandeiro",
     "set": "a mountain meadow of tall wildflowers, drying racks of cut "
            "herbs on trestles behind him, wooded ridges rising on both "
            "sides",
     "curto": "the same meadow",
     "chapeu": "a faded red bandana tied over his head",
     "animais": ["a full-grown black bear", "a full-grown bull elk"],
     "luz": "Warm open meadow daylight, soft and clear.",
     "audio": "bees, wind through tall grass"},

    # + 2026-08-02: mesma passada de repertorio que abriu o pool REFS logo
    # abaixo. ⚠️ ESTE bloco NAO e' ganho de personagem — arquetipo e' CENARIO
    # + CHAPEU + ANIMAL (NE5), e o rosto mora nos REFS. E' ganho de CENARIO:
    # os dezesseis acima ja' repetiam luz e fundo no lote, e a familia
    # montanhes e a nativa eram as unicas com set de INVERNO e de AGUA
    # PARADA zerados. As duas novas entram exatamente por ai:
    #   · montanhes_passo — o unico set de neve fechada do pool, com luz azul
    #     chapada sem sombra, e dois animais novos (alce macho, carcaju).
    #   · nativo_lago — o unico set de agua parada com bruma, luz fria vinda
    #     de baixo, e lince, que ainda nao existia no pool.
    #   · ⛔ ZERO OCULOS no `chapeu`: o montanhes do NECROSE e' o PROPRIO
    #     narrador/REF, e a string `mesmo` das cenas 2-5 so' reafirma "same
    #     hat, same beard, same <marca>" — oculos sumiriam da cena 2 em
    #     diante e o Veo trocaria de pessoa (P6). Chapeu e' chapeu.
    #   · os `animais` comecam todos em "a ": a IMAGE 04 faz
    #     .replace("a ", "", 1) e um "an ..." sairia "the same an ...".
    #   · o animal continua prop de DOMINANCIA (NE4), nunca bicho de
    #     estimacao: nada deitado, nada de coleira.
    {"id": "montanhes_passo", "selo": "N", "familia": "montanhes",
     "set": "a windswept high pass in deep winter, a cairn of stacked flat "
            "stones beside him, an unbroken snowfield falling away behind "
            "and bare black rock above",
     "curto": "the same snow pass",
     "chapeu": "a thick knitted wool cap pulled down over his ears",
     "animais": ["a full-grown bull moose", "a heavy-shouldered wolverine"],
     "luz": "Flat cold blue winter light off the snow, almost shadowless.",
     "audio": "wind driving loose snow over stone"},
    {"id": "nativo_lago", "selo": "N", "familia": "nativo norte-americano",
     "set": "a stony northern lakeshore in the last hour of daylight, a "
            "birch-bark canoe pulled up on the stones behind him, dark "
            "spruce forest across flat water, low mist on the surface",
     "curto": "the same lakeshore",
     "chapeu": "a headband of dark otter fur",
     "animais": ["a full-grown bull elk", "a full-grown lynx"],
     "luz": "Cool blue light coming off still water, soft and even.",
     "audio": "water lapping on stones, a loon calling"},
]

# NE4 - o animal e prop de STATUS (a alavanca do leao do Kofi), nao de
# credibilidade medica. A ESPECIE vem do arquetipo; aqui so se sorteia qual das
# congruentes. PROIBIDO cachorro, husky, coleira, animal deitado.

# NE3 - autoridade SELVAGEM, nao clinica. Musculatura por GRUPO NOMEADO e
# PESADA (ordem do operador 2026-07-30: "todo REF deve ser super musculoso" -
# a primeira leva saiu magra). O CHAPEU NAO MORA AQUI: vem do arquetipo, senao
# o sorteio cruza deserto do Texas com chapeu alpino.
REFS = [
    {"idade": 62,
     "corpo": "a heavily muscled build - a broad slab of chest, thick arms, "
              "and clearly cut abdominal muscles",
     "cabeca": "long gray hair and a thick gray beard reaching mid-chest",
     "marca": "unusually pale ice-blue eyes and a small notch missing from the "
              "top of his left ear"},
    {"idade": 65,
     "corpo": "a powerfully built heavily muscled frame - a barrel chest, "
              "thick corded forearms and a hard flat stomach",
     "cabeca": "gray hair tied back and a full white beard reaching mid-chest",
     "marca": "a clean pale scar running through his right eyebrow"},
    {"idade": 58,
     "corpo": "a tall heavily muscled build - wide shoulders, a thick neck, a "
              "broad slab of chest and visible abdominal muscles",
     "cabeca": "shoulder-length salt-and-pepper hair and a thick "
               "salt-and-pepper beard",
     "marca": "a deep vertical cleft in his chin and heavy weather lines "
              "around the eyes"},
    {"idade": 68,
     "corpo": "a heavily muscled build - a broad chest, thick arms and "
              "shoulders and clearly cut abdominal muscles",
     "cabeca": "long white hair and a long white beard reaching the middle of "
               "his chest",
     "marca": "a prominent dark mole high on his right cheekbone"},
    # + 2026-08-01: o operador mediu vicio no lote - o mesmo rosto voltando
    # video apos video. Pool de 4 para 11.
    {"idade": 55,
     "corpo": "a heavily muscled slab-sided build - a deep chest, thick "
              "shoulders and a hard ridged stomach",
     "cabeca": "a thick dark brown mane pushed back off his forehead and a "
               "short square-cut brown beard",
     "marca": "a pale crescent scar along the left side of his jaw"},
    {"idade": 57,
     "corpo": "a heavily muscled weathered frame - a broad chest, thick "
              "roped forearms and clearly cut abdominal muscles",
     "cabeca": "a long rust-red mane going gray at the temples and a full "
               "red beard split into two braids",
     "marca": "a gold tooth that shows on the left side when he talks"},
    {"idade": 60,
     "corpo": "a heavily muscled compact frame - a thick barrel chest, "
              "short powerful arms and clearly cut abdominal muscles",
     "cabeca": "wiry black hair going gray at the sides and a dense black "
               "beard streaked with white",
     "marca": "a small raised scar splitting the middle of his lower lip"},
    {"idade": 61,
     "corpo": "a lean heavily muscled frame - a broad slab of chest, thick "
              "arms and a hard ridged stomach",
     "cabeca": "a long silver ponytail pulled back tight and a short "
               "close-trimmed white beard",
     "marca": "eyes of two different colours, one green and one brown, and "
              "a shallow cleft high on his forehead"},
    {"idade": 63,
     "corpo": "a heavily muscled thickset build - a broad chest, heavy arms "
              "and a hard stomach with clearly cut abdominal muscles",
     "cabeca": "thick sandy hair sun-bleached at the ends and a full "
               "copper-blond beard reaching his collarbone",
     "marca": "a clean pale scar across the bridge of his nose"},
    {"idade": 64,
     "corpo": "a heavily muscled frame - a broad slab of chest, thick corded "
              "arms and clearly cut abdominal muscles",
     "cabeca": "a bald crown with long gray hair falling at the sides and a "
               "wide gray beard reaching mid-chest",
     "marca": "a dark birthmark the shape of a thumbprint below his right ear"},
    {"idade": 67,
     "corpo": "a powerfully built heavily muscled frame - a deep chest, "
              "thick shoulders and a hard stomach with cut abdominal muscles",
     "cabeca": "a white widow's peak swept straight back and a long forked "
               "white beard tied with two leather cords",
     "marca": "a pale scar through his upper lip and a heavy silver hoop in "
              "his left earlobe"},
    # + 2026-08-02: o operador mediu o pool inteiro e viu SEMPRE O MESMO ROSTO.
    # As onze acima variam cabelo e barba e mais nada de estrutural, entao o
    # gerador recebia quase a mesma frase e devolvia quase o mesmo montanhes.
    # A nova abre o eixo ZERADO deste pool: OCULOS (0/11), que nenhuma das onze
    # menciona — e traz junto um PORTE novo (cintura grossa, nao seca).
    #   · 68 — oculos de leitura na ponta do nariz mais falha entre os dentes
    #     da frente; barba branca curta de um polegar, corte escovinha.
    #   · a ancora e' do lado ✅ de licoes-producao-veo §REF — DISTINTIVO,
    #     NUNCA DETERIORADO (falha entre os dentes, nao dente lascado).
    #   · o CHAPEU nao mora aqui (NE5): vem do arquetipo.
    #   · zero mencao a etnia: o motor injeta ETNIA[pagina] antes da marca.
    {"idade": 68,
     "corpo": "a heavily muscled thick-waisted frame - a deep heavy chest, "
              "forearms like fence posts and a hard stomach with clearly cut "
              "abdominal muscles",
     "cabeca": "coarse iron-gray hair in a flat brush cut and a short "
               "bristly white beard no longer than a thumb",
     "marca": "a wide gap between his two front teeth that shows whenever he "
              "talks, and thin gold-rimmed reading glasses on the end of his "
              "nose"},
]

# NE6 - O RITUAL E O GELATIN TRICK (correcao do operador, 2026-07-30).
# A primeira versao copiou a receita da FONTE (curcuma + pimenta + mel + limao)
# e quebrou a congruencia inviolavel: o mecanismo do criativo tem que ser o que
# a VSL vende, e a nossa vende GELATIN nas cinco paginas. Acafrao vira video
# sobre acafrao. O que varia e COMO a gelatina e preparada, nunca o que e.
# Topica ou de preparo, nunca dose medica.
RECEITAS_PROP = [
    {"id": "gelatina_agua", "selo": "V",
     "mesa": "a plain white sachet of pale powder with no label, a clear glass "
             "of water and a metal spoon",
     "acao": "tearing the sachet open, tipping the powder into the glass "
             "of water and stirring it in slow circles",
     "fala": "gelatin into cold water"},
    {"id": "gelatina_bicarbonato", "selo": "V",
     "mesa": "a plain white sachet of pale powder with no label, an open box "
             "of baking soda, a glass jar and a wooden spoon",
     "acao": "tipping the powder from the sachet into the jar, pouring "
             "the baking soda in over it and stirring the two together for a minute",
     "fala": "gelatin into baking soda"},
    {"id": "gelatina_mel", "selo": "N",
     "mesa": "a plain white sachet of pale powder with no label, a wooden mug "
             "of warm water, a jar of honey and a spoon",
     "acao": "emptying the sachet into the wooden mug, spooning honey in "
             "after it and stirring until the powder is gone",
     "fala": "a spoonful of gelatin and a spoon of honey into warm water"},
    {"id": "gelatina_limao", "selo": "N",
     "mesa": "a plain white sachet of pale powder with no label, a glass of "
             "cold water, a halved lemon and a metal spoon",
     "acao": "emptying the sachet into the glass, squeezing the halved "
             "lemon over it and stirring it through",
     "fala": "gelatin into cold water with fresh lemon"},
    # + 2026-08-01: o operador mediu vicio no lote - o mesmo ritual voltando.
    # O que varia continua sendo COMO a gelatina e preparada, nunca o que e.
    {"id": "gelatina_cafe", "selo": "N",
     "mesa": "a plain white sachet of pale powder with no label, an enamel "
             "mug of black coffee and a metal spoon",
     "acao": "tearing the sachet open, shaking the powder into the mug of "
             "coffee and stirring it until the powder is gone",
     "fala": "gelatin into black coffee"},
    {"id": "gelatina_vinagre", "selo": "N",
     "mesa": "a plain white sachet of pale powder with no label, a glass jar "
             "of water, a dark bottle of cider vinegar and a wooden spoon",
     "acao": "emptying the sachet into the jar, pouring a capful of the "
             "vinegar in after it and stirring the two together",
     "fala": "gelatin into water with a capful of cider vinegar"},
    {"id": "gelatina_leite", "selo": "N",
     "mesa": "a plain white sachet of pale powder with no label, a tin cup of "
             "warm milk and a long-handled spoon",
     "acao": "tipping the powder from the sachet into the tin cup and "
             "whisking it into the warm milk until it thickens",
     "fala": "gelatin into warm milk"},
    {"id": "gelatina_sal", "selo": "N",
     "mesa": "a plain white sachet of pale powder with no label, a small dish "
             "of coarse sea salt, a glass of warm water and a metal spoon",
     "acao": "tearing the sachet open into the glass, pinching the coarse "
             "salt in over it and stirring it through the warm water",
     "fala": "gelatin and salt into warm water"},
    {"id": "gelatina_canela", "selo": "N",
     "mesa": "a plain white sachet of pale powder with no label, a heap of "
             "ground cinnamon on a saucer, a mug of hot water and a spoon",
     "acao": "emptying the sachet into the mug, tapping the ground cinnamon "
             "in over it and stirring until nothing is left floating",
     "fala": "gelatin and cinnamon into hot water"},
]

MESAS = [
    {"id": "mesa_madeira", "desc": "a weathered wooden table outdoors"},
    {"id": "laje_pedra", "desc": "a flat slab of rock used as a table"},
    {"id": "tronco", "desc": "a split log bench"},
    {"id": "tampa_caminhonete", "desc": "the open tailgate of an old pickup truck"},
    {"id": "barril", "desc": "the top of an upturned wooden barrel"},
    # + 2026-08-01: o operador viu a mesma bancada voltando no lote.
    # Pool de 5 para 12.
    {"id": "toco_arvore", "desc": "a wide flat tree stump used as a table"},
    {"id": "carretel", "desc": "an old wooden cable spool stood on its end"},
    {"id": "bancada_cavalete", "desc": "a workbench of rough sawn planks on trestles"},
    {"id": "caixa_ferramenta", "desc": "the flat lid of a battered steel toolbox on a crate"},
    {"id": "mesa_campanha", "desc": "a folding camp table with a scuffed canvas top"},
    {"id": "fogao_campo", "desc": "the cold iron top of an old camp stove"},
    {"id": "tabua_lenha", "desc": "a board laid flat across a stack of split firewood"},
]

# ---------------------------------------------------------------------------
# POOLS DE COPY
# ---------------------------------------------------------------------------

NUCLEO = ["Johnson", "pecker", "wiener", "tool", "soldier"]

# NE7 — o hook e' "from this to this", com o gesto sincronizado na batida das
# palavras. A fonte abre nomeando o orgao no primeiro segundo.
# NE7 - o hook e a comparacao, com o gesto sincronizado na batida das palavras.
# ⚠️ E ELE E CONDICIONAL OU PERGUNTA, NUNCA AFIRMACAO SOBRE O CORPO DELE.
# "Your {o} looks like this right now. It can look like this by next month" foi
# RECUSADO pela politica de CONTEUDO NOCIVO (2026-07-31), com o IMAGE ja
# aprovado. Lido pelo classificador: diagnostico do corpo do espectador +
# promessa de transformacao com prazo, ilustrados por tecido necrosado — isso e
# desinformacao em saude, e claim de cura e a PRIMEIRA das quatro linhas da
# cerca no arsenal.
# A fonte nunca afirma, ela CONDICIONA: "If you want your soldier to go from
# this to this in just one month". Tres dos quatro hooks tinham se afastado
# dessa forma sem que eu percebesse.
#
# ⭐ 2026-08-03 — FRASE ORFA (queixa do operador, lendo um take renderizado:
# "Voce tem que contextualizar mais as coisas. Ta' deixando o viewer sem
# entender o contexto e do que se trata"). REGRA NOVA: toda frase que nomeia
# uma CAUSA carrega, NA MESMA FRASE, o que ela quebra — nao vale o orgao
# aparecer "em algum lugar da cena", que foi exatamente o que ele reprovou.
#   errado: "Your doctor calls it age."   -> idade estragando O QUE?
#   certo:  "Your doctor blames age when a man's {o} quits."
# Alterado aqui so' o [5]. Os outros sete nao tem o vicio: ou nao nomeiam
# causa nenhuma, ou apontam os dois modelos com deitico + gesto sincronizado
# (NE7), que e' o formato do angulo.
HOOKS = [
    "If you want your {o} to go from this to this in one month, watch close.",
    "If your {o} looks more like this one than that one, watch close, brother.",
    "Nobody wants this one. If you want your {o} to look like that one, watch close.",
    "If you had to pick tonight, is your {o} this one or that one?",
    # + 2026-08-01: o pool tinha 4 entradas e a cena 1 — a fala mais importante
    # do video — repetia dentro do lote. Pool de 4 para 8, e no maximo 1 entrada
    # usa o vocativo "brother".
    "If your wife could see your {o} tonight, would she see this one or that one?",
    "Your doctor blames age when a man's {o} quits. He's wrong. Is yours this one or that one?",
    "Waiting turns that one into this one. How close is your {o} tonight?",
    "This one costs a man his marriage. That one keeps it. Which is your {o}?",
]

# NE — cena 2: o MUP de Georgi (alivio de culpa + vilao), com o modelo PODRE
# erguido. ⚠️ "blood flow" literal e' obrigatorio (o linter cobra).
#
# ⭐ 2026-08-03 — FRASE ORFA. Mesma queixa do operador que reescreveu o HOOKS
# [5] acima: a fala abria com uma causa solta ("It's not age and it's not
# you.", "Doctors call this getting older. It isn't.", "You did not eat your
# way into that.", "Sitting still all day does it.") e o espectador passava
# 4-5 segundos ouvindo fisiologia sem saber do que se tratava — o orgao so'
# chegava na frase seguinte. REGRA NOVA: a frase que nomeia a causa carrega o
# alvo NA MESMA FRASE.
# COMO SE CONSERTOU, sem estourar o TETO_FALA[2]=26: em vez de repetir o
# substantivo em duas frases (com "old boy" isso custa +2 palavras e estoura),
# a causa e o mecanismo viraram UMA frase e o orgao entrou nas primeiras
# palavras dela. Alterados: [0], [2], [3], [4], [8].
# Intocados: [1], [5], [6], [7] — nessas a frase causal ja' nomeia o orgao.
CAUSAS = [
    "What stopped your {o} wasn't age, brother — the blood flow to it got choked off, year after year.",
    "Nobody is born with this. Your {o} got here because the blood flow to it got shut down, year after year.",
    "It's not age that shut your {o} down, and it's not you — something squeezed its blood flow off, and nobody told you.",
    "Doctors call it age when your {o} goes quiet. It isn't — the blood flow to your {o} got strangled, and that is fixable.",
    # + 2026-08-01: o operador mediu vicio no lote - as mesmas quatro causas
    # voltando, e "brother" em cima do hook. As novas entram sem vocativo.
    "Nothing you eat did that to your {o} — the blood flow to it got choked off, quiet, year after year.",
    "Your heart still pumps fine. It's the small blood flow down to your {o} that got choked off first.",
    "That didn't happen overnight and it isn't your fault. Blood flow to your {o} gets choked off a little each year.",
    "Ask any man out here past sixty. The blood flow to his {o} got choked off and nobody ever told him why.",
    "Sitting still all day is what shuts your {o} down — the blood flow to it gets choked off and stays choked.",
]

RECEITAS_FALA = [
    "Stir {ing}. That's the gelatin trick, and your {o} feels it inside a week.",
    "Stir {ing}. One minute. That's the gelatin trick — do it before your {o} quits for good.",
    "Tonight, stir {ing}. They call it the gelatin trick. Your {o} took years to get this bad.",
    "Stir {ing}. That is the whole gelatin trick, and it is what walked my {o} back.",
    # + 2026-08-01: o operador mediu vicio no lote - as mesmas quatro falas de
    # ritual voltando. Pool de 4 para 10.
    "Before bed, stir {ing}. That's the gelatin trick your {o} needs.",
    "Want your {o} back? Stir {ing}. That is the gelatin trick.",
    "My {o} runs on this now. Stir {ing}. That's the gelatin trick.",
    "One minute, no more. Stir {ing}. Gelatin trick, and your {o} answers.",
    "Don't wait on your {o}. Stir {ing}. That's the gelatin trick.",
    "Out here we stir {ing}. Gelatin trick. Your {o} wakes up.",
]

# NE — cena 4: MUS. "gelatin trick" literal e' obrigatorio, com o modelo SAO
# erguido contra o ceu. O podre saiu de cena: a ausencia e' o payoff.
# ⚠️ Com o NE11 os dois modelos saem da cena 4 — quem esta no quadro e o
# geoduck. Templates que diziam "went from that one to this one" viravam deixis
# para objeto AUSENTE (4a forma de vagueza). A copy aqui aponta para o que esta
# na mao, ou narra o modelo podre como MEMORIA da cena 1, nunca como gesto.
PROVAS = [
    "This is my {o} after one month of that trick. {barreira}",
    "One month of the gelatin trick, and this is what I carry now. My {o} has not quit since. {barreira}",
    "That rotten one on the stand was me last year. This is my {o} today. {barreira}",
    "Nineteen days of the gelatin trick and my {o} came back like this. {barreira}",
    # + 2026-08-01: o operador mediu vicio no lote - as mesmas quatro provas
    # voltando. Pool de 4 para 10.
    "This is what a month of the gelatin trick did for my {o}. {barreira}",
    "My wife noticed before I said a word. That's my {o} on that trick. {barreira}",
    "Four weeks ago mine matched the old one. Now my {o} looks like this. {barreira}",
    "Thirty days on the gelatin trick. My {o} has not let me down since. {barreira}",
    "I carry this now instead of an excuse. That trick gave my {o} back. {barreira}",
    "A spoonful of gelatin, every night. That is what my {o} runs on now. {barreira}",
]

BARREIRAS = [
    "You do it in your own kitchen, in about a minute.",
    "No doctor, no pharmacy counter, nobody has to know.",
    "A trick you can do from the comfort of your own home.",
    "Costs less than a cup of coffee and nobody sees you buy it.",
    "Nothing to fill, nothing to explain to anybody.",
    # + 2026-08-01: o operador mediu vicio no lote - as mesmas barreiras
    # voltando. Pool de 5 para 8.
    "Nobody has to see you do it.",
    "No appointment, no waiting room, no questions.",
    "Any grocery store in town has it on the shelf.",
]

PACING = [
    # ⛔ CONSERTO 2026-08-03 — MUDANCA SEM DIZER O QUE MUDOU.
    # Queixa do operador, lendo as falas no proprio app: "My sister asked what
    # changed." -> "O que mudou?". A frase abria a pergunta e a fala acabava:
    # se a frase pergunta, a proxima RESPONDE — e aqui nao havia proxima.
    # ⭐ Isto pesa dobrado nesta cena: a cena 3 e' o CTA e e' a UNICA das tres
    # que nao nomeia o orgao (cota 2/3). Com o future pacing vago, os 8 segundos
    # inteiros do pedido nao diziam o que o homem ganha. Agora dizem, com o
    # verbo de resultado do registro da casa (`hard again`).
    # ⛔ RS10 / A LINHA DO NECROSE: aqui NAO entra substantivo do NUCLEO. Esta
    # cena e' toda feita de marcador de prazo ("Next Friday night", "tonight",
    # "A month from tonight"), e `your <orgao>` + prazo no mesmo take de 8s foi
    # o que derrubou um video nosso por conteudo nocivo. O resultado entra so'
    # pelo verbo e pelo pronome — zero anatomia, zero medida.
    # ⚠️ Teto: [1] e [2] ficaram com o MESMO numero de palavras de antes; so' o
    # [0] custou +2, e ele e' o mais curto do pool. O TETO_FALA[3]=34 nao subiu.
    # Alterados: [0], [1], [2]. Dos outros tres, [3] e [5] prometem uma REACAO
    # nomeada (agradecer, sorrir), que nao e' mudanca de objeto oculto.
    # ⚠️ [4] ("see what Saturday feels like") NAO nomeia reacao nenhuma e e' o
    # unico residuo vago do pool — 121 falas de cena 3 medidas em varredura
    # ampla. Nao foi tocado: nao abre pergunta nem afirma mudanca, entao nao e'
    # o vicio que o operador apontou, e copy e' alcada do Ed.
    "Next Friday night she'll ask why you're hard again.",
    "When she asks how you got hard again, you'll remember tonight.",
    "A month from tonight you'll be hard again.",
    # + 2026-08-01: o operador mediu vicio no lote - o mesmo future pacing em
    # todo CTA. Pool de 3 para 6.
    "Two weeks from now you'll thank me.",
    "Do it tonight and see what Saturday feels like.",
    "This time next month you'll be grinning.",
]

GATES = [
    "Follow me first, or my message never lands.",
    "Follow me first, or I won't have any way to find your comment, brother.",
    "Hit follow right now, or Facebook can't deliver it.",
    # + 2026-08-01: o operador mediu vicio no lote - "brother" saindo em todo
    # CTA. REGRA NOVA DO POOL: no maximo 2 entradas com o vocativo "brother",
    # e a maioria sem vocativo nenhum.
    "Tap follow first. My inbox is shut to strangers.",
    "Follow first. Facebook only lets me reply to followers.",
    "Follow first. I get hundreds of these a day.",
    "Follow me, fellas. The algorithm buries me otherwise.",
    "Follow now. I only answer the ones that follow.",
    "Give me a follow first, man. Takes one second.",
    "Follow first, then comment. That's the whole thing.",
    "Hit follow tonight. I clear the comments by morning.",
]

# NE12 (falha em campo, Lucas/nativo-canyon 2026-07-31): a keyword saia em CAIXA
# ALTA e colada no `and`. O Veo narrou "gelatine" e a legenda automatica queimou
# GELATINE no rodape, brigando com o CTA fixado do topo que dizia GELATIN.
#   - a VIRGULA forca a micro-pausa que impede a liaison com a palavra seguinte
#   - a MINUSCULA evita o Erro Fatal 12 do V4 (em ALL CAPS o Veo soletra)
# Prova no mesmo render: cena 3 tem 'gelatin' minusculo 2x e o TTS acertou as
# duas; a cena 5 em caixa alta sem virgula errou.
# Caixa alta fica SO' no CTA fixado do topo — e' imagem, nao passa pelo TTS.
CTAS = [
    # ⭐ Alternativa pedida pelo operador em 2026-07-31, vista em campo:
    # a promessa e' A RECEITA, nao "o que eu uso" nem "onde eu compro".
    # E' a mais direta do pool e a unica que casa com a keyword RECIPE
    # que o Veo Editor ja' destaca na legenda.
    "{pacing} Comment gelatin, and I'll send you the recipe. {gate}",
    "{pacing} Comment gelatin, and I'll send you the only one I trust. {gate}",
    "{pacing} Comment gelatin, and I'll send you the exact one I use. {gate}",
    "{pacing} Comment gelatin, and I'll send you where I get mine. {gate}",
    # + 2026-08-01: o operador mediu vicio no lote - os mesmos quatro CTAs
    # voltando. Pool de 4 para 12, keyword sempre minuscula e com virgula.
    "{pacing} Comment gelatin, and the recipe is yours. {gate}",
    "{pacing} Comment gelatin, and I'll write you back tonight. {gate}",
    # ⛔ AQUI HAVIA UMA SEGUNDA COPIA de "and I'll send you the recipe."
    # (2026-08-08). Ela e' a PRIMEIRA do pool, com o comentario que explica por
    # que ela existe — a expansao de 2026-08-01 a reescreveu sem notar. Dobrava
    # a chance justamente do CTA mais generico.
    "{pacing} Comment gelatin, and it lands in your messages tonight. {gate}",
    "{pacing} Comment gelatin, one word, and the recipe is yours. {gate}",
    "{pacing} Comment gelatin, and I'll send you the whole thing tonight. {gate}",
    "{pacing} Comment gelatin, and the recipe lands in your messages tonight. {gate}",
    "{pacing} Comment gelatin, and I'll send the recipe steps in order. {gate}",
]

# ---------------------------------------------------------------------------
# TABELAS DE TOKEN BANIDO (o linter do SHORT reusa estas, via short_comum)
# ---------------------------------------------------------------------------

BANIDOS_TAKE = {
    "stiff": "adjetivo de estado em prompt de movimento derruba o video",
    "limp": "idem", "sags": "idem",
    "pulse": "tumescencia — IMAGE passa e o VIDEO e' recusado",
    "throb": "idem", "swelling": "idem",
    "rots": "no TAKE nada apodrece nem sara: e' comparacao, nao transformacao (NE8)",
    "heals": "idem (NE8)",
    # entraram com o NE11 (a cena 4 virou geoduck): quando o linter foi escrito
    # o agente nao tinha molusco nenhum
    "geoduck": "so' no IMAGE; no TAKE usar 'the clam' (NE11)",
    "neck": "no geoduck e' 'siphon', nunca 'neck' (NE11)",
}
BANIDOS_IMAGE = {
    # NE2: adjetivo generico nao descreve — o Veo normaliza os dois modelos
    "damaged": "nao descreve nada — percorrer os CINCO eixos (NE2)",
    "unhealthy": "idem (NE2)",
    "diseased organ": "idem (NE2)",
    "big": "adjetivo nao dimensiona", "huge": "idem",
}
# NE1 — a categoria entrega o corte errado (falha documentada no D1)
BANIDOS_CATEGORIA = {
    "the male reproductive system": "categoria — o gerador escolhe o corte e "
                                    "escolhe o mais comum do treino (NE1)",
    "cross-section": "nao diz o plano (NE1)",
}
# NE4 — o lobo e' lobo
BANIDOS_ANIMAL = {
    "dog": "o prop e' LOBO, nao cachorro (NE4)",
    "husky": "idem (NE4)",
    "german shepherd": "idem (NE4)",
}
BANIDOS_GLOBAL = {"the victim": "rotulo que significa dano",
                  "the narrator": "trocar por relacao nomeada"}
BANIDOS_CTA = {"BOOK": "quebra a automacao DM", "YES": "quebra a automacao DM"}

# ⚠️ ESTE E' O TETO DO ARCO DE 5 CENAS, e nao o do SHORT. Sao dois
# dicionarios diferentes e nao se misturam: o `TETO_FALA` la' embaixo tem 3
# chaves (as cenas do SHORT) e este tem 5 (as cenas do arco longo, indexadas
# pela numeracao original). O SHORT le' daqui as duas pontas que ele herda
# inteiras — a cena 1 (hook) e a cena 5 (CTA) — para nao criar uma segunda
# verdade. Confundir os dois troca o teto de palavra do agente inteiro.
TETO_FALA_LONGO = {1: 20, 2: 26, 3: 26, 4: 30, 5: 34}


# ---------------------------------------------------------------------------
# MOTOR DO ARCO LONGO — sorteio e montagem das 5 cenas
# ---------------------------------------------------------------------------
# ⚠️ O SHORT NAO ABANDONA ESTE MOTOR: ele sorteia pelo arco de 5 cenas e depois
# colapsa (short_comum.sortear_curto / montar_curto). Os tres callables abaixo
# sao os do arco longo e tem os nomes com sufixo `_longo` justamente para nao
# colidirem com o `sortear`/`montar`/`nova_fala` do SHORT, que sao outra coisa.


def _palavras(txt):
    return len(re.findall(r"[A-Za-z']+", txt))


def _evitando(rng, pool, recentes):
    livres = [x for x in pool if x.get("id") not in recentes]
    return rng.choice(livres if livres else pool)


def _sortear_longo(pagina, rng, ledger, travas=None):
    # ⛔ A REF DESTE AGENTE SAI AQUI, no motor longo embutido — nao no
    # `sortear` de tres argumentos la' de baixo. Por isso a trava atravessa
    # `sc.sortear_curto` ate' aqui: sem isso o toggle acenderia e nao mudaria
    # nada, que e' o botao que mente.
    hist = ledger.get(pagina, {})
    arq = _evitando(rng, ARQUETIPOS, hist.get("arquetipo", [])[-4:])
    rec = _evitando(rng, RECEITAS_PROP, hist.get("receita", [])[-2:])
    mesa = _evitando(rng, MESAS, hist.get("mesa", [])[-2:])
    # ⭐ MODO FORTE — a REF deste angulo e' o montanhes de tronco nu.
    ref = (sc.ref_forte(REFS[0], rng) if (travas or {}).get("forte")
           else rng.choice(REFS))
    animal = rng.choice(arq["animais"])      # so as congruentes com o arquetipo

    orgaos = rng.sample(NUCLEO, 4)
    falas = [
        rng.choice(HOOKS).format(o=orgaos[0]),
        rng.choice(CAUSAS).format(o=orgaos[1]),
        rng.choice(RECEITAS_FALA).format(o=orgaos[2], ing=rec["fala"]),
        rng.choice(PROVAS).format(o=orgaos[3], barreira=rng.choice(BARREIRAS)),
        _cta(rng),
    ]
    return {"pagina": pagina, "arquetipo": arq, "animal": animal,
            "receita": rec, "mesa": mesa, "ref": ref, "falas": falas}


def _montar_longo(spec):
    et = ETNIA[spec["pagina"]]
    ref, arq, rec, mesa = spec["ref"], spec["arquetipo"], spec["receita"], spec["mesa"]
    animal = LOBO % spec["animal"]
    falas = spec["falas"]

    # o chapeu vem do ARQUETIPO, nunca do REF (NE5)
    quem = ("a %d-year-old %s man, bare-chested, %s, %s, wearing %s, %s"
            % (ref["idade"], et, ref["corpo"], ref["cabeca"], arq["chapeu"],
               ref["marca"]))
    # marca sem o artigo: depois de "same" ele sobra ("same a deep cleft...")
    marca_s = re.sub(r"^an? ", "", ref["marca"])
    mesmo = ("The same %d-year-old %s man, same hat, same beard, same %s, "
             "bare-chested and heavily muscled."
             % (ref["idade"], et, marca_s))

    b = {}

    # O cabecalho REF faz parte do bloco, igual ao "IMAGE 01/05:" dos outros.
    # E o que o parser do AdBatch usa para mandar este bloco para o painel
    # Consistencia Visual em vez de tentar encaixa-lo num slot da grade.
    # ⛔ Nao remover: sem ele a referencia e descartada em silencio.
    b["BLOCO 0 (REF)"] = (
        "REF 01: Photo of a real person, a %d-year-old %s man, chest up, facing the "
        "camera directly, neutral steady expression. Bare-chested, %s, tanned "
        "weathered skin. %s. Wearing %s. %s. An ordinary everyday relatable "
        "person with a plain unremarkable face, not a celebrity, not a model, "
        "not an actor, not resembling any famous person. Plain neutral gray "
        "background, soft even frontal light. No subtitles, no captions, no "
        "burned-in text, no watermark."
        % (ref["idade"], et, ref["corpo"],
           ref["cabeca"][0].upper() + ref["cabeca"][1:], arq["chapeu"],
           ref["marca"][0].upper() + ref["marca"][1:])
    )

    b["IMAGE 01/05"] = (
        "IMAGE 01/05: Medium shot at %s. Sitting in front of it is %s. He looks "
        "straight into the lens, mouth open mid-word.\n\n"
        "Standing on a flat surface in front of him are two anatomy models, "
        "side by side at chest height.\n\n%s\n\n%s\n\n"
        "Behind him on his right stands %s. He is the only person in the frame. "
        "%s %s %s"
        % (arq["set"], quem, MODELO_PODRE, MODELO_SAO, animal, ANTICELEB,
           arq["luz"], CAUDA)
    )

    b["IMAGE 02/05"] = (
        "IMAGE 02/05: Medium shot at %s, same background. %s %s His expression "
        "is hard and serious, brow furrowed, mouth open mid-word. He is the "
        "only person in the frame. %s %s %s"
        % (arq["curto"], mesmo, D1_IMAGE, ANTICELEB, arq["luz"], CAUDA)
    )

    b["IMAGE 03/05"] = (
        "IMAGE 03/05: Medium shot at %s, %s behind it, same light. %s He stands "
        "behind it mid-action, speaking to the camera. On it: %s. He is the "
        "only person in the frame. %s %s %s"
        % (mesa["desc"], arq["curto"], mesmo, rec["mesa"], ANTICELEB,
           arq["luz"], CAUDA)
    )

    b["IMAGE 04/05"] = (
        "IMAGE 04/05: Low-angle medium shot at %s, open sky behind him. %s He "
        "stands tall and holds up high in his right hand, raised above his "
        "shoulder against the sky, %s He is grinning, chin lifted. Neither "
        "anatomy model is anywhere in the frame. Behind him on his right stands "
        "the same %s. He is the only person in the frame. %s %s %s"
        % (arq["curto"], mesmo, GEODUCK_PAYOFF,
           spec["animal"].replace("a ", "", 1), ANTICELEB, arq["luz"], CAUDA)
    )

    b["IMAGE 05/05"] = (
        "IMAGE 05/05: Close-up at %s, same light. %s He is the only person in "
        "the frame. He looks straight into the lens, calm and confident, one "
        "corner of his mouth raised in a half-smile. His right index finger "
        "points directly at the camera. %s %s %s"
        % (arq["curto"], mesmo, ANTICELEB, arq["luz"], CAUDA)
    )

    b["TAKE 01/05"] = (
        "TAKE 01/05: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway, no cuts. The %d-year-old man speaks straight "
        "into the lens with force. On the word \"this\" he points at the left "
        "model, and on the second \"this\" he points at the right model - the "
        "two gestures land on the two words. %s Behind him the animal shifts "
        "its weight once and keeps looking at the camera. He is the only person "
        "in the shot and no one else enters frame.\nDialogue: \"%s\"\n"
        "Audio: %s. No music."
        % (ref["idade"], IMOBILIDADE_PAR, sonorizar(falas[0]), arq["audio"])
    )

    b["TAKE 02/05"] = (
        "TAKE 02/05: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway, no cuts. %s He speaks with conviction and "
        "slows down on the last sentence. He is the only person in the shot."
        + chr(10) + "Dialogue: \"%s\"" + chr(10) + "Audio: %s. No music."
    ) % (D1_TAKE, sonorizar(falas[1]), arq["audio"])

    b["TAKE 03/05"] = (
        "TAKE 03/05: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway, no cuts. His hands stir the spoon while he talks, %s. "
        "His eyes stay on the lens the whole time. He is the only person in the "
        "shot.\nDialogue: \"%s\"\nAudio: %s, a spoon against glass. No music."
        % (rec["acao"], sonorizar(falas[2]), arq["audio"])
    )

    b["TAKE 04/05"] = (
        "TAKE 04/05: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway, no cuts. The %d-year-old man raises his arm "
        "a little higher against the sky and grins wider, holding it steady "
        "above his shoulder for the whole take. %s Behind him the animal turns "
        "its head once and looks back at the camera. He is the only person in "
        "the shot."
        + chr(10) + "Dialogue: \"%s\"" + chr(10) + "Audio: %s. No music."
    ) % (ref["idade"], GEODUCK_TAKE, sonorizar(falas[3]), arq["audio"])

    b["TAKE 05/05"] = (
        "TAKE 05/05: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway, no cuts. The %d-year-old man looks into the "
        "lens, calm and confident, and points his right index finger at the "
        "camera. He speaks directly and evenly, no rush.\nDialogue: \"%s\"\n"
        "Audio: %s. No music."
        % (ref["idade"], sonorizar(falas[4]), arq["audio"])
    )

    return b


def _nova_fala_longo(spec, i, rng):
    """Re-sorteia a fala da cena i (0-4) mantendo o substantivo-nucleo dela."""
    o = next((n for n in NUCLEO if n.lower() in spec["falas"][i].lower()), "soldier")
    if i == 0:
        return rng.choice(HOOKS).format(o=o)
    if i == 1:
        return rng.choice(CAUSAS).format(o=o)
    if i == 2:
        return rng.choice(RECEITAS_FALA).format(o=o, ing=spec["receita"]["fala"])
    if i == 3:
        return rng.choice(PROVAS).format(o=o, barreira=rng.choice(BARREIRAS))
    return _cta(rng)


# ---------------------------------------------------------------------------
# INTERFACE HERDADA (consumida por ui_agente.py)
# ---------------------------------------------------------------------------
# EIXOS_UI cita os pools pelo NOME em string; o `ui_agente._pool` resolve por
# getattr no modulo. Antes caia no fallback `motor.base`; agora os pools moram
# aqui e o getattr direto acerta.

EIXOS_UI = [
    ("arquetipo", "ARQUÉTIPO", "ARQUETIPOS", "id"),
    ("receita", "RITUAL", "RECEITAS_PROP", "id"),
    ("mesa", "BANCADA", "MESAS", "id"),
    ("ref", "O HOMEM", "REFS", "marca"),
]

PT_ARQ = {
    "montanhes_cabana": "No topo da montanha, na cabana de pedra",
    "montanhes_lago": "Na saliência sobre o lago glacial",
    "montanhes_pinheiros": "Na clareira na linha das árvores",
    "cowboy_curral": "No curral do rancho, no fim da tarde",
    "cowboy_mesa": "Na mesa de rocha vermelha do deserto",
    "nativo_planicie": "Na planície aberta sob o céu enorme",
    "nativo_canyon": "Na boca do cânion de arenito",
    "redneck_varanda": "Na varanda da casa de fazenda do Sul",
    "redneck_celeiro": "Na porta do celeiro vermelho",
    "curandeiro_apalache": "Na varanda da cabana de tora, nos Apalaches",
    "curandeiro_pantano": "No atracadouro do pântano de ciprestes",
}
PT_REC = {
    "gelatina_agua": "a gelatina num copo de água gelada",
    "gelatina_bicarbonato": "a gelatina com bicarbonato num pote",
    "gelatina_mel": "a gelatina com mel em água morna",
    "gelatina_limao": "a gelatina em água gelada com limão",
}


# ---------------------------------------------------------------------------
# O PACOTE QUE O `short_comum` RECEBE COMO `base`
# ---------------------------------------------------------------------------
# `short_comum` e' generico: ele le' `base.NUCLEO`, `base.BANIDOS_*`,
# `base.sortear`, `base.montar` e `base.nova_fala` de um objeto que recebe por
# parametro. Antes esse objeto era o modulo `necrose_lucas`. Agora e' este
# pacote de nomes locais — mesmo conteudo, sem dependencia de terceiro.
#
# ⛔ Os tres callables sao os do ARCO LONGO. Passar aqui o `sortear`/`montar`/
# `nova_fala` do SHORT faria o colapso rodar em cima de si mesmo.
# ⚠️ Ficam de fora, DE PROPOSITO, BANIDOS_VAZAMENTO e BANIDOS_FONTE: o
# `lint_curto` testa com `hasattr` e o NECROSE nunca teve essas tabelas.
# ⚠️ ETNIA, CAUDA e sonorizar entram mesmo o NECROSE nao os chamando hoje:
# quem le' esses tres e' o `bancada_com_rosto`/`redencao_com_ref` do
# `short_comum`, e enquanto o `base` era o MODULO eles estavam la'. Sem eles o
# pacote seria menor que o contrato e o dia em que alguem plugasse uma dessas
# duas cenas no NECROSE quebraria em AttributeError.
_LONGO = types.SimpleNamespace(
    NUCLEO=NUCLEO,
    _palavras=_palavras,
    BANIDOS_TAKE=BANIDOS_TAKE,
    BANIDOS_IMAGE=BANIDOS_IMAGE,
    BANIDOS_CATEGORIA=BANIDOS_CATEGORIA,
    BANIDOS_ANIMAL=BANIDOS_ANIMAL,
    BANIDOS_GLOBAL=BANIDOS_GLOBAL,
    BANIDOS_CTA=BANIDOS_CTA,
    ETNIA=ETNIA,
    CAUDA=CAUDA,
    sonorizar=sonorizar,
    sortear=_sortear_longo,
    montar=_montar_longo,
    nova_fala=_nova_fala_longo,
)

# ###########################################################################
# ⭐ FIM DO BLOCO INLINEADO
# ###########################################################################


# ⭐ MAPA e' de onde vem a IMAGEM; MAPA_COPY e' de onde vem a FALA. A cena 3
# junta as duas coisas: a imagem da BANCADA (arco 3, o gelatin trick sendo
# preparado, com o rosto em quadro e a colher batendo no vidro) por baixo da
# fala do CTA (arco 5).
#
# ⚠️ Ordem do operador, 2026-07-31: "estamos deixando espaco valioso nesses 22
# segundos apertados no lixo". A cena 3 era o close do CTA — um terco do video
# num talking head contra fundo liso, zero informacao visual. Agora o
# espectador OUVE o pedido e VE o gelatin trick nos mesmos 8 segundos.
#
# ⛔ Nao ha' cena nova aqui: a bancada e' o bloco 3 do arco longo, ja' validado
# em render. So' mudou qual fala roda por cima dele.
MAPA = (1, 4, 3)
MAPA_COPY = (1, None, 5)          # None = a fundida, que nao vem do arco longo
CENAS_UI = ["1 · O HOOK", "2 · RITUAL + PROVA", "3 · CTA SOBRE A BANCADA"]

# As pontas herdam o teto do arco longo: sao os MESMOS pools, entao inventar
# outro numero aqui so' criaria duas verdades. So' a cena 2 tem teto proprio,
# porque a copy dela e' propria. 34 palavras em 8s e' leitura de anuncio, nao
# conversa — e e' o mesmo limite da cena mais carregada da versao longa. Acima
# disso o Veo atropela: foi medido em 45 e a fala saiu embolada.
# ⛔⛔ CENAS 2 E 3 CAIRAM PARA 32 EM 2026-08-04. 34 (cena 2) e o herdado da
# cena 5 longa (cena 3) estao ACIMA DO FISICO: 8s a 4,0 palavras/s = 32
# (licoes §5). Na longa o CTA tinha uma cena inteira so' para ele; aqui
# divide os mesmos 8s com o pacing e o gate. Medido antes: cena 3 estourava
# em 3,2% e cena 2 em 1,7%, e o que ficava de fora era o FIM do gate de
# follow — a maquina de conversao morrendo no ar.
# ⛔⛔ TETO 25 — ordem permanente do operador, 2026-08-05: *"sempre meca. Nao
# pode haver cortes de fala."* O numero vem de RENDER, nao de conta: 32
# cortou e 28 cortou. Os exemplos que ele escreve a mao vivem em 16-25
# palavras (2,0-3,1 p/s). Ver licoes-de-construcao §28.
# ⭐⭐ MODOS DE REF — contrato compartilhado (short_comum),
# 2026-08-05. ⛔ Desligados, o prompt volta IDENTICO ao de antes
# do recurso — provado caractere por caractere.
MODO_FORTE = True

TETO_FALA = {1: TETO_FALA_LONGO[1], 2: 25, 3: 25}


# ---------------------------------------------------------------------------
# A COPY FUNDIDA — cena 2
# ---------------------------------------------------------------------------
# ⚠️ CURADORIA DO OPERADOR. Todo item aqui e' copy nova, escrita a partir dos
# fragmentos ja' validados das RECEITAS_FALA, CAUSAS e PROVAS do arco longo.
# Nenhum item entra ou sai desta lista sem passar por ele.
#
# Cada item e' obrigado a carregar, na mesma respiracao:
#   1. o mecanismo   -> a string literal `blood flow`
#   2. o ritual      -> a string literal `gelatin trick` + o ingrediente {ing}
#   3. a prova       -> a evidencia em 1a pessoa, terminando em deitico
# O linter confere 1 e 2. O 3 e' julgamento.
#
# ⚠️ SEM {barreira} — e a ausencia e' deliberada. O ingrediente {ing} sozinho
# custa ~12 palavras e a barreira mais ~10; com os dois a cena batia em 45
# palavras, 5,6 por segundo, e o Veo atropela a fala. Os tres beats acima sao
# obrigatorios; a barreira e' tranquilizacao, e o funil ja' a repete adiante.
# ⛔ Nao devolver a barreira aqui sem cortar outra coisa.
# ⚠️ TODO item carrega `{o}`. Sem ele a cota do orgao cai para 1/3 (o CTA nao
# nomeia o orgao), e o linter reprova o sorteio inteiro. Medido: um unico
# template sem `{o}` reprovou 48 de 300 sorteios.
FUNDIDAS = [
    # ⛔ CONSERTO 2026-08-03 — VERBO DE ENCANAMENTO NO LUGAR DO RESULTADO.
    # Queixa do operador, lendo as falas no proprio app: "Com tanto verbo que
    # voce poderia usar de forma mais obvia pra dizer que DEIXA O PINTO MELHOR,
    # voce usa 'opens'?" — e ele reclamou de `opens it` / `what opens it` no
    # mesmo dia, em tres agentes.
    # ⭐ A regra: o `blood flow` continua obrigatorio (o linter cobra o MUP),
    # mas ele nao pode ser o OBJETO do unico verbo da frase. O mecanismo abrindo
    # e' encanamento; o homem quer o resultado. Entra verbo de resultado, dito
    # como um homem diria: `got my {o} hard again`.
    # ⛔ NAO se troca `open` por outro eufemismo de encanamento (`unblocks`,
    # `restores flow`, `frees it up`) — trocar metafora por metafora nao
    # conserta nada (licoes-de-construcao §17).
    # ⚠️ O gasto de palavra foi pago DENTRO da propria entrada: "Mine came back
    # like this" encurtou para "Like this", e as duas ficaram com o mesmo
    # tamanho de antes. O TETO_FALA[2]=34 nao subiu.
    # ⚠️ RS10: nenhuma das duas junta `your {o}` com marcador de prazo — as duas
    # falam do orgao em 1a pessoa (`my {o}`) e nao tem prazo nem medida.
    # Alterados: [0] e [7]. Nenhuma outra entrada tem verbo de encanamento.
    "Stir {ing}. That's the gelatin trick — it got the blood flow back and my "
    "{o} hard again. Like this.",

    # ⛔ CONSERTO 2026-08-03 — FRASE ORFA. As tres entradas marcadas abaixo
    # abriam com a causa e so' nomeavam o orgao DUAS FRASES DEPOIS. Queixa
    # literal do operador, lendo um take renderizado de outro agente: "It isn't
    # age. The blood flow got choked off." -> "deveria ser it isn't age THAT'S
    # CAUSING YOUR JOHN-SON NOT WORKING ANYMORE. Ta' deixando o viewer sem
    # entender o contexto e do que se trata."
    # ⭐ A regra: a frase que nomeia a CAUSA carrega, NA MESMA FRASE, o que ela
    # quebra. Nao vale "o orgao aparece em algum lugar da fala".
    # ⚠️ O gasto de palavra foi pago encurtando a MESMA entrada, nunca subindo
    # o TETO_FALA (cena 2 = 34).
    "That rotten one was the blood flow to my {o}, choked off. Stir {ing} — the "
    "whole gelatin trick, and it walked back.",

    "The blood flow to your {o} got choked off. Stir {ing}. That's the gelatin "
    "trick, and this is me now.",

    # ⛔ conserto 2026-08-03 — frase orfa (ver o bloco acima)
    "It's not age — it's the blood flow to your {o}, strangled. Stir {ing}. "
    "That's the gelatin trick, and mine hasn't quit since.",

    "Stir {ing}. That's the gelatin trick, and the blood flow came back. So did "
    "my {o}.",

    # + 2026-08-01: o operador mediu vicio no lote - as mesmas cinco fundidas
    # voltando. Pool de 5 para 14; todo item novo carrega os tres beats.
    "It was blood flow all along. Stir {ing}. That's the gelatin trick, "
    "and my {o} came back like this.",

    "Nobody told me it was blood flow. Stir {ing}. The gelatin trick. My "
    "{o} looks like this now.",

    # ⛔ conserto 2026-08-03 — verbo de encanamento (ver o bloco no topo do
    # pool). `opened the blood flow back up` e' o mesmo vicio do [0], so' que
    # no passado; e `ended up like this` nao diz o que ele virou.
    "Stir {ing}. Gelatin trick. The blood flow came back and it got my {o} "
    "hard again. Like this.",

    "Doctors said age. It was blood flow. Stir {ing} — the gelatin trick — "
    "and look what my {o} does now.",

    # ⛔ conserto 2026-08-03 — frase orfa (ver o bloco acima)
    "The blood flow to your {o} gets choked off, that's all. Stir {ing}. "
    "That's the gelatin trick. This is mine now.",

    "Stir {ing} every night. Gelatin trick. It brings the blood flow back "
    "— my {o} hasn't quit since.",

    "Same blood flow that feeds your heart feeds your {o}. Stir {ing}. "
    "Gelatin trick. Mine came back like this.",

    "Thirty days. Stir {ing} — that's the gelatin trick — and the blood "
    "flow came back to my {o}. Like this.",

    "Age isn't it. The blood flow to your {o} got choked off. Stir {ing}. "
    "Gelatin trick. Look at mine.",
]


def _cta(rng, teto=None):
    """PACING + molde do CTA + GATE somam num take so', e ninguem olhava.

    ⛔ ORDEM DELIBERADA: o molde do CTA sai primeiro (carrega a isca e o
    literal `Comment gelatin,`, que sao intocaveis), o pacing depois, e o
    GATE por ULTIMO — o gate e' o beat intercambiavel do trio, entao e' ele
    que absorve a sobra em vez de ser cortado pelo fim do take.
    ⚠️ Fallback = a entrada mais CURTA, NUNCA `or pool`: `or pool` devolve o
    pool inteiro e reintroduz o estouro em silencio.
    """
    teto = TETO_FALA[3] if teto is None else teto
    cp = min(PACING, key=_palavras)
    cg = min(GATES, key=_palavras)

    def _ok(pool, monta):
        return ([x for x in pool if _palavras(monta(x)) <= teto]
                or [min(pool, key=lambda x: _palavras(monta(x)))])

    c = rng.choice(_ok(CTAS, lambda c: c.format(pacing=cp, gate=cg)))
    p = rng.choice(_ok(PACING, lambda p: c.format(pacing=p, gate=cg)))
    g = rng.choice(_ok(GATES, lambda g: c.format(pacing=p, gate=g)))
    return c.format(pacing=p, gate=g)


def _fundir(spec, rng):
    o = sc.orgao_de(_LONGO, spec["falas_base"][3], "soldier")
    ing = spec["receita"]["fala"]
    # ⚠️ o {ing} vai de 7 a 12 palavras e JA' foi decidido pelo sorteio do
    # PROP — a fundida tinha de ceder a ele, e nao o contrario.
    # ⛔ nunca `or FUNDIDAS`.
    # ⛔ 2026-08-05 — quando NENHUMA fundida cabe com aquele `ing`, o fallback
    # entregava a mais curta e ainda assim estourava (medido: max 27 com teto
    # 25). Nesse caso quem cede e' a RECEITA: troca-se por uma mais curta que
    # permita ao menos uma fundida caber. O prop em cena nao muda — `ing` e' so'
    # a enumeracao falada.
    def _cabem_com(g):
        return [x for x in FUNDIDAS
                if _palavras(x.format(o=o, ing=g)) <= TETO_FALA[2]]

    cabem = _cabem_com(ing)
    if not cabem:
        for alt in sorted(RECEITAS_PROP, key=lambda r: _palavras(r["fala"])):
            if _cabem_com(alt["fala"]):
                ing, cabem = alt["fala"], _cabem_com(alt["fala"])
                break
    x = (rng.choice(cabem) if cabem
         else min(FUNDIDAS, key=lambda y: _palavras(y.format(o=o, ing=ing))))
    return x.format(o=o, ing=ing)


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
    for eixo, val in (("arquetipo", spec["arquetipo"]["id"]),
                      ("familia", spec["arquetipo"]["familia"]),
                      ("receita", spec["receita"]["id"]),
                      ("mesa", spec["mesa"]["id"])):
        p.setdefault(eixo, []).append(val)
        p[eixo] = p[eixo][-12:]
    with open(LEDGER, "w", encoding="utf-8") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)


def sortear(pagina, rng, ledger, travas=None):
    return sc.sortear_curto(_LONGO, pagina, rng, ledger, MAPA, _fundir,
                            MAPA_COPY, travas)


def montar(spec):
    # ⛔ trava de texto queimado em todo TAKE — o watermark que o
    # operador viu vazando nos reels da concorrente (2026-08-01).
    return sc.selar_takes(sc.montar_curto(_LONGO, spec, MAPA))


def nova_fala(spec, i, rng):
    return sc.nova_fala_curta(_LONGO, spec, i, rng, MAPA, _fundir, MAPA_COPY)


def _recopiar_receita(spec, rng):
    """A receita entra na fala fundida — trocar o prop exige reescreve-la."""
    spec["falas"][1] = _fundir(spec, rng)


EIXOS_QUE_MEXEM_NA_COPY = {"receita": _recopiar_receita}


# ---------------------------------------------------------------------------
# LINTER — as regras do NECROSE que sobrevivem ao colapso
# ---------------------------------------------------------------------------

def _limpar_animal(spec, direcao):
    # 'big' e' banido como adjetivo de DIMENSAO DE PROP e casava com
    # "a big chestnut quarter horse" em todo sorteio de cowboy/redneck
    for forma in (spec["animal"], spec["animal"].replace("a ", "", 1)):
        direcao = direcao.replace(forma, "")
    return direcao


def _ne7_hook(spec, blocos, achados):
    """O hook e' a comparacao: dois deiticos, condicional e orgao nomeado."""
    h = spec["falas"][0].lower()
    d = len(re.findall(r"\bthis\b|\bthese\b|\bthe other one\b|\bthat one\b", h))
    if d < 2:
        achados.append(("ERRO", "NE7: o hook nao aponta os DOIS modelos — "
                                "precisa de dois deiticos (%d encontrado)" % d))
    if not re.search(r"\bif\b", h) and not spec["falas"][0].rstrip().endswith("?"):
        achados.append(("ERRO", "NE7: o hook AFIRMA o estado do corpo dele. Tem "
                                "que ser condicional ('if...') ou pergunta — "
                                "claim de cura e a primeira linha da cerca"))
    if not any(n.lower() in h for n in NUCLEO):
        achados.append(("ERRO", "NE7: o hook nao nomeia o orgao com substantivo"))


def _blocos_travados(spec, blocos, achados):
    i1 = sc.bloco_base(blocos, MAPA, "IMAGE", 1)
    for s, rot in ((MODELO_PODRE, "modelo podre NE2"),
                   (MODELO_SAO, "modelo sao NE2")):
        if s not in i1:
            achados.append(("ERRO", "IMAGE 01 sem a string travada: %s" % rot))
    if "identical" not in i1:
        achados.append(("ERRO", "NE2: falta 'identical' na abertura do modelo sao "
                                "— sem isso o Veo desenha dois objetos diferentes"))
    if IMOBILIDADE_PAR not in sc.bloco_base(blocos, MAPA, "TAKE", 1):
        achados.append(("ERRO", "TAKE 01 sem a imobilidade do PAR (NE8)"))

    # NE11 — o payoff virou a cena 2 do SHORT, mas as travas sao as mesmas
    if GEODUCK_PAYOFF not in sc.bloco_base(blocos, MAPA, "IMAGE", 4):
        achados.append(("ERRO", "NE11: a cena do payoff sem a string travada do "
                                "geoduck (a spec dimensional e o que impede o "
                                "tamanho natural)"))
    if GEODUCK_TAKE not in sc.bloco_base(blocos, MAPA, "TAKE", 4):
        achados.append(("ERRO", "NE11: o TAKE do payoff sem a imobilidade + "
                                "negacao de ave"))

    # NE4 — o animal de status nas duas cenas que sobraram com ele
    nucleo_animal = spec["animal"].replace("a ", "", 1)
    for cena in (1, 4):
        nome = "IMAGE %02d/03" % (MAPA.index(cena) + 1)
        if nucleo_animal.lower() not in blocos[nome].lower():
            achados.append(("ERRO", "NE4: %s sem o animal de status (%s)"
                            % (nome, nucleo_animal)))

    # NE9 — todas as cenas sao solo
    for nome in sorted(k for k in blocos if k.startswith("IMAGE")):
        if "only person in the frame" not in blocos[nome].lower():
            achados.append(("AVISO", "NE9: %s nao declara que ele esta sozinho" % nome))


def lint(spec, blocos):
    return sc.lint_curto(
        _LONGO, spec, blocos, MAPA, TETO_FALA,
        literais=("gelatin trick", "blood flow"),
        limpar_direcao=_limpar_animal,
        extras=(_ne7_hook, _blocos_travados))


# ---------------------------------------------------------------------------
# RESUMO
# ---------------------------------------------------------------------------

def resumo_pt(spec):
    et = "branca" if "white" in ETNIA[spec["pagina"]] else "negra"
    return ("%s, o %s de %d anos sem camisa e muito musculoso mostra os dois "
            "órgãos lado a lado. Na cena 2 ele ergue só o são contra o céu, e "
            "na 3 faz o CTA enquanto prepara %s na bancada. Três cenas, elenco "
            "de pele %s."
            % (PT_ARQ.get(spec["arquetipo"]["id"], "No cenário"),
               spec["arquetipo"]["familia"], spec["ref"]["idade"],
               PT_REC.get(spec["receita"]["id"], "o ritual"), et))
