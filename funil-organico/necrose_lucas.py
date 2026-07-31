#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
necrose_lucas.py — randomizador + gerador + linter do AGENTE NECROSE.

Os dois orgaos lado a lado: dois modelos anatomicos 3D em pedestal de aco, um
APODRECIDO e um SAO, nas maos de um montanhes de tronco nu com um lobo, no topo
de uma montanha nevada. Fonte: Alaskan Mountain Men Tips,
reel 1740829770294515 — 1.9K reacoes / 307 comentarios / 103 shares.

Mesma arquitetura dos outros motores:
  1. String travada NUNCA e' redigitada. Mora aqui como constante.
  2. Regra mecanica e' regex, nao julgamento.
  3. Os eixos sao SORTEADOS e a linha sorteada e' EXECUTADA (P1).

⚠️ SELO 🟡 — PORTADO ANTES DO PRIMEIRO RENDER (decisao do operador,
2026-07-30). O par de modelos nunca passou por moderacao. Se a fila de
reformulacao do agente (§SELO DE RISCO) for acionada, e' AQUI que a string
muda — e ela muda em UM lugar so'.

Uso:
    python funil-organico/necrose_lucas.py --pagina ray --n 1
    python funil-organico/necrose_lucas.py --pagina joe --n 3 --seed 42 --dry-run
    python funil-organico/necrose_lucas.py --stats

Doutrina: AGENTE_ED_NECROSE_V1.md · concorrentes/alaskan-mountain-men-mapa-visual.md
"""

import argparse
import json
import os
import random
import re
import sys

from nucleo_sonoro import sonorizar

AQUI = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(AQUI, ".necrose-ledger.json")

TITULO = "AGENTE NECROSE"
SLUG = "necrose"
SUBTITULO = "os dois órgãos lado a lado · gerador offline de prompts Veo"

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

ETNIA = {
    "joe": "white American", "ray": "white American", "matt": "white American",
    "marcus": "Black American", "chuck": "Black American",
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
     "acao": "he tears the sachet open, tips the powder into the glass of "
             "water and stirs it in slow circles",
     "fala": "a spoonful of gelatin into a glass of cold water"},
    {"id": "gelatina_bicarbonato", "selo": "V",
     "mesa": "a plain white sachet of pale powder with no label, an open box "
             "of baking soda, a glass jar and a wooden spoon",
     "acao": "he tips the powder from the sachet into the jar, pours the "
             "baking soda in over it and stirs the two together for a minute",
     "fala": "a spoonful of gelatin into a jar of baking soda"},
    {"id": "gelatina_mel", "selo": "N",
     "mesa": "a plain white sachet of pale powder with no label, a wooden mug "
             "of warm water, a jar of honey and a spoon",
     "acao": "he empties the sachet into the wooden mug, spoons honey in after "
             "it and stirs until the powder is gone",
     "fala": "a spoonful of gelatin and a spoon of honey into warm water"},
    {"id": "gelatina_limao", "selo": "N",
     "mesa": "a plain white sachet of pale powder with no label, a glass of "
             "cold water, a halved lemon and a metal spoon",
     "acao": "he empties the sachet into the glass, squeezes the halved lemon "
             "over it and stirs it through",
     "fala": "a spoonful of gelatin into cold water with fresh lemon"},
]

MESAS = [
    {"id": "mesa_madeira", "desc": "a weathered wooden table outdoors"},
    {"id": "laje_pedra", "desc": "a flat slab of rock used as a table"},
    {"id": "tronco", "desc": "a split log bench"},
    {"id": "tampa_caminhonete", "desc": "the open tailgate of an old pickup truck"},
    {"id": "barril", "desc": "the top of an upturned wooden barrel"},
]

# ---------------------------------------------------------------------------
# POOLS DE COPY
# ---------------------------------------------------------------------------

NUCLEO = ["Johnson", "soldier", "pecker", "manhood", "wiener", "tool", "old boy"]

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
HOOKS = [
    "If you want your {o} to go from this to this in one month, watch close.",
    "If your {o} looks more like this one than that one, watch close, brother.",
    "Nobody wants this one. If you want your {o} to look like that one, watch close.",
    "If you had to pick tonight, is your {o} this one or that one?",
]

# NE — cena 2: o MUP de Georgi (alivio de culpa + vilao), com o modelo PODRE
# erguido. ⚠️ "blood flow" literal e' obrigatorio (o linter cobra).
CAUSAS = [
    "This is not what age does to a man, brother. This is what happens when the blood flow to your {o} gets choked off.",
    "Nobody is born with this. Your {o} got here because the blood flow to it got shut down, year after year.",
    "It's not age and it's not you. Something squeezed the blood flow to your {o} shut, and nobody told you.",
    "Doctors call this getting older. It isn't. The blood flow to your {o} got strangled, and that is fixable.",
]

RECEITAS_FALA = [
    "Stir {ing}. That's the gelatin trick, and your {o} feels it inside a week.",
    "Stir {ing}. One minute. That's the gelatin trick — do it before your {o} quits for good.",
    "Tonight, stir {ing}. They call it the gelatin trick. Your {o} took years to get this bad.",
    "Stir {ing}. That is the whole gelatin trick, and it is what walked my {o} back.",
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
]

BARREIRAS = [
    "You do it in your own kitchen, in about a minute.",
    "No doctor, no pharmacy counter, nobody has to know.",
    "A trick you can do from the comfort of your own home.",
    "Costs less than a cup of coffee and nobody sees you buy it.",
    "Nothing to fill, nothing to explain to anybody.",
]

PACING = [
    "Next Friday night she'll ask what changed.",
    "Next Friday night, when she asks what changed, you'll remember this.",
    "A month from tonight you won't recognise yourself.",
]

GATES = [
    "Follow me first, or my message never lands.",
    "Follow me first, or I won't have any way to find your comment, brother.",
    "Hit follow right now, or Facebook can't deliver it.",
]

CTAS = [
    "{pacing} Comment GELATIN and I'll send you the only one I trust. {gate}",
    "{pacing} Comment GELATIN and I'll send you the exact one I use. {gate}",
    "{pacing} Comment GELATIN and I'll send you where I get mine. {gate}",
]

# ---------------------------------------------------------------------------
# LINTER
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

TETO_FALA = {1: 20, 2: 26, 3: 26, 4: 30, 5: 34}


def _palavras(txt):
    return len(re.findall(r"[A-Za-z']+", txt))


def lint(spec, blocos):
    achados = []
    falas = spec["falas"]

    # cota do orgao (>= 4 das 5), rotacionada
    cenas, usados = [], []
    for i, fala in enumerate(falas, 1):
        baixo = fala.lower()
        hit = next((n for n in NUCLEO if n.lower() in baixo), None)
        if hit:
            cenas.append(i)
            usados.append(hit)
    if len(cenas) < 4:
        achados.append(("ERRO", "cota do orgao: %d/5 (minimo 4). Cenas sem "
                                "substantivo do nucleo: %s"
                        % (len(cenas), [i for i in range(1, 6) if i not in cenas])))
    if len(set(usados)) < len(usados):
        achados.append(("AVISO", "substantivo repetido no video: %s"
                        % sorted({u for u in usados if usados.count(u) > 1})))

    # NE7 — o hook e' a comparacao: precisa de DOIS deiticos, um por modelo.
    # ⚠️ Nao basta procurar "this": "One of these is your {o}. The other one..."
    # cumpre a regra com outras palavras. O que a regra exige e' o PAR apontado,
    # nao a string "from this to this".
    h = falas[0].lower()
    deiticos = len(re.findall(r"\bthis\b|\bthese\b|\bthe other one\b|\bthat one\b", h))
    if deiticos < 2:
        achados.append(("ERRO", "NE7: o hook nao aponta os DOIS modelos — "
                                "precisa de dois deiticos (%d encontrado)" % deiticos))

    # ⚠️ O hook e CONDICIONAL ou PERGUNTA, nunca afirmacao sobre o corpo dele.
    # Afirmar o estado ("your {o} looks like this") junto com a promessa de
    # virada ("it can look like this by next month") e diagnostico + claim de
    # cura: foi o que derrubou o video da cena 1 na politica de conteudo nocivo
    # (2026-07-31), com o IMAGE ja aprovado.
    if not re.search(r"\bif\b", h) and not falas[0].rstrip().endswith("?"):
        achados.append(("ERRO", "NE7: o hook AFIRMA o estado do corpo dele. Tem "
                                "que ser condicional ('if...') ou pergunta — "
                                "claim de cura e a primeira linha da cerca"))
    if not any(n.lower() in h for n in NUCLEO):
        achados.append(("ERRO", "NE7: o hook nao nomeia o orgao com substantivo"))

    # MUP na cena 2
    if "blood flow" not in falas[1].lower():
        achados.append(("ERRO", "cena 2 sem o MUP (a string literal 'blood flow')"))

    # tetos
    total = 0
    for i, fala in enumerate(falas, 1):
        n = _palavras(fala)
        total += n
        if n > TETO_FALA[i]:
            achados.append(("AVISO", "cena %d com %d palavras (teto %d) — cortar "
                                     "UMA frase, nao reescrever menor" % (i, n, TETO_FALA[i])))
    # 125 e nao 105: o CTA carrega TRES obrigatorios (future pacing + GELATIN +
    # follow-gate) e nao cabe no teto do arsenal. Mesmo criterio do VAZAMENTO.
    if total > 125:
        achados.append(("AVISO", "video com %d palavras (alvo ~90-105)" % total))

    corpo = " ".join(falas).lower()
    if "gelatin trick" not in corpo:
        achados.append(("ERRO", "expressao literal 'gelatin trick' ausente"))
    if "gelatin" not in falas[4].lower():
        achados.append(("ERRO", "CTA da cena 5 sem a keyword GELATIN"))
    for tok, motivo in BANIDOS_CTA.items():
        if re.search(r"\b%s\b" % tok, falas[4]):
            achados.append(("ERRO", "CTA usa '%s' — %s" % (tok, motivo)))

    # tokens banidos por bloco (so' na DIRECAO de cena, nunca na fala)
    for nome, txt in blocos.items():
        direcao = txt.split(chr(10) + "Dialogue:")[0]
        # ⚠️ o ANIMAL sai da varredura: 'big' e' banido como adjetivo de
        # DIMENSAO DE PROP, e casava com "a big chestnut quarter horse" em todo
        # sorteio de cowboy/redneck (mesmo falso positivo do 'big-box' no PEE).
        # (a IMAGE 04 usa o animal sem o artigo: "the same big chestnut horse")
        for forma in (spec["animal"], spec["animal"].replace("a ", "", 1)):
            direcao = direcao.replace(forma, "")
        baixo = direcao.lower()
        tabela = BANIDOS_TAKE if nome.startswith("TAKE") else BANIDOS_IMAGE
        for tok, motivo in tabela.items():
            if re.search(r"\b%s\b" % tok, baixo):
                achados.append(("ERRO", "%s contem '%s' — %s" % (nome, tok, motivo)))
        for tabela2 in (BANIDOS_CATEGORIA, BANIDOS_ANIMAL, BANIDOS_GLOBAL):
            for tok, motivo in tabela2.items():
                if tok in baixo:
                    achados.append(("ERRO", "%s contem '%s' — %s" % (nome, tok, motivo)))

    # NE1/NE2 — os blocos travados dos dois modelos, integros
    i1 = blocos["IMAGE 01/05"]
    for s, rot in ((MODELO_PODRE, "modelo podre NE2"),
                   (MODELO_SAO, "modelo sao NE2")):
        if s not in i1:
            achados.append(("ERRO", "IMAGE 01 sem a string travada: %s" % rot))
    if "identical" not in i1:
        achados.append(("ERRO", "NE2: falta 'identical' na abertura do modelo sao "
                                "— sem isso o Veo desenha dois objetos diferentes"))

    # NE8 — no TAKE nada muda de estado
    if IMOBILIDADE_PAR not in blocos["TAKE 01/05"]:
        achados.append(("ERRO", "TAKE 01 sem a imobilidade do PAR (NE8)"))
    # NE11 — a cena 4 e o geoduck, com a spec dimensional e a negacao de ave
    if GEODUCK_PAYOFF not in blocos["IMAGE 04/05"]:
        achados.append(("ERRO", "NE11: IMAGE 04 sem a string travada do geoduck "
                                "(a spec dimensional e o que impede o tamanho natural)"))
    if GEODUCK_TAKE not in blocos["TAKE 04/05"]:
        achados.append(("ERRO", "NE11: TAKE 04 sem a imobilidade + negacao de ave"))

    # NE10 — a cena 2 e o D1, e a string travada dele nao se comprime
    if D1_IMAGE not in blocos["IMAGE 02/05"]:
        achados.append(("ERRO", "NE10: IMAGE 02 sem a string travada do D1"))
    if D1_TAKE not in blocos["TAKE 02/05"]:
        achados.append(("ERRO", "NE10: TAKE 02 sem a string travada do D1"))

    # NE4 — o animal de status nas cenas 1 e 4. A ESPECIE varia com o
    # arquetipo (lobo, cavalo, touro, urso, jacare...), entao o que se confere
    # e' o animal DAQUELE sorteio, nao a palavra "wolf".
    nucleo_animal = spec["animal"].replace("a ", "", 1)
    for nome in ("IMAGE 01/05", "IMAGE 04/05"):
        if nucleo_animal.lower() not in blocos[nome].lower():
            achados.append(("ERRO", "NE4: %s sem o animal de status (%s)"
                            % (nome, nucleo_animal)))

    # NE9 — todas as cenas sao solo
    for nome in sorted(k for k in blocos if k.startswith("IMAGE")):
        if "only person in the frame" not in blocos[nome].lower():
            achados.append(("AVISO", "NE9: %s nao declara que ele esta sozinho" % nome))

    return achados


# ---------------------------------------------------------------------------
# SORTEIO
# ---------------------------------------------------------------------------

def _carregar_ledger():
    if os.path.exists(LEDGER):
        with open(LEDGER, encoding="utf-8-sig") as f:
            return json.load(f)
    return {}


def _evitando(rng, pool, recentes):
    livres = [x for x in pool if x.get("id") not in recentes]
    return rng.choice(livres if livres else pool)


def sortear(pagina, rng, ledger):
    hist = ledger.get(pagina, {})
    arq = _evitando(rng, ARQUETIPOS, hist.get("arquetipo", [])[-4:])
    rec = _evitando(rng, RECEITAS_PROP, hist.get("receita", [])[-2:])
    mesa = _evitando(rng, MESAS, hist.get("mesa", [])[-2:])
    ref = rng.choice(REFS)
    animal = rng.choice(arq["animais"])      # so as congruentes com o arquetipo

    orgaos = rng.sample(NUCLEO, 4)
    falas = [
        rng.choice(HOOKS).format(o=orgaos[0]),
        rng.choice(CAUSAS).format(o=orgaos[1]),
        rng.choice(RECEITAS_FALA).format(o=orgaos[2], ing=rec["fala"]),
        rng.choice(PROVAS).format(o=orgaos[3], barreira=rng.choice(BARREIRAS)),
        rng.choice(CTAS).format(pacing=rng.choice(PACING), gate=rng.choice(GATES)),
    ]
    return {"pagina": pagina, "arquetipo": arq, "animal": animal,
            "receita": rec, "mesa": mesa, "ref": ref, "falas": falas}


def _gravar_ledger(ledger, spec):
    p = ledger.setdefault(spec["pagina"], {})
    for eixo, val in (("arquetipo", spec["arquetipo"]["id"]),
                      ("familia", spec["arquetipo"]["familia"]),
                      ("receita", spec["receita"]["id"]),
                      ("mesa", spec["mesa"]["id"])):
        p.setdefault(eixo, []).append(val)
        p[eixo] = p[eixo][-12:]
    with open(LEDGER, "w", encoding="utf-8") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)


# ---------------------------------------------------------------------------
# GERADOR
# ---------------------------------------------------------------------------

def montar(spec):
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

    b["BLOCO 0 (REF)"] = (
        "Photo of a real person, a %d-year-old %s man, chest up, facing the "
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
        "very slight natural sway, no cuts. His hands work while he talks: %s. "
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


# ---------------------------------------------------------------------------
# INTERFACE (consumido por ui_agente.py)
# ---------------------------------------------------------------------------

EIXOS_UI = [
    ("arquetipo", "ARQUÉTIPO", "ARQUETIPOS", "id"),
    ("receita", "RITUAL", "RECEITAS_PROP", "id"),
    ("mesa", "BANCADA", "MESAS", "id"),
    ("ref", "O HOMEM", "REFS", "marca"),
]

CENAS_UI = ["1 · A COMPARAÇÃO", "2 · A CAUSA", "3 · O GELATIN TRICK",
            "4 · A PROVA", "5 · CTA"]

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


def resumo_pt(spec):
    et = "branca" if "white" in ETNIA[spec["pagina"]] else "negra"
    return ("%s, o %s de %d anos sem camisa e muito musculoso mostra os dois "
            "órgãos lado a lado — o apodrecido e o são. Na cena 3 ele prepara "
            "%s (o gelatin trick), e na 4 ergue só o são contra o céu. Elenco "
            "de pele %s."
            % (PT_ARQ.get(spec["arquetipo"]["id"], "No cenário"),
               spec["arquetipo"]["familia"], spec["ref"]["idade"],
               PT_REC.get(spec["receita"]["id"], "o ritual"), et))


def _recopiar_receita(spec, rng):
    """A receita entra na fala da cena 3 — trocar o prop exige reescrever."""
    o = next((n for n in NUCLEO if n.lower() in spec["falas"][2].lower()), "soldier")
    spec["falas"][2] = rng.choice(RECEITAS_FALA).format(
        o=o, ing=spec["receita"]["fala"])


EIXOS_QUE_MEXEM_NA_COPY = {"receita": _recopiar_receita}


def nova_fala(spec, i, rng):
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
    return rng.choice(CTAS).format(pacing=rng.choice(PACING), gate=rng.choice(GATES))


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def imprimir(spec, blocos, achados):
    print("=" * 72)
    print("SPEC SORTEADA — pagina %s | arquetipo %s (%s, %s) | animal %s | "
          "ritual %s | bancada %s"
          % (spec["pagina"], spec["arquetipo"]["id"], spec["arquetipo"]["familia"],
             spec["arquetipo"]["selo"], spec["animal"], spec["receita"]["id"],
             spec["mesa"]["id"]))
    print("=" * 72)
    print(blocos["BLOCO 0 (REF)"] + "\n")
    for k in sorted(k for k in blocos if k.startswith("IMAGE")):
        print("-" * 72); print(blocos[k] + "\n")
    for k in sorted(k for k in blocos if k.startswith("TAKE")):
        print("-" * 72); print(blocos[k] + "\n")
    print("=" * 72)
    if not achados:
        print("LINTER: OK — nenhuma violacao mecanica.")
    else:
        for nivel, msg in achados:
            print("[%s] %s" % (nivel, msg))
        n = sum(1 for a in achados if a[0] == "ERRO")
        print("%d erro(s), %d aviso(s)." % (n, len(achados) - n))


def stats():
    ledger = _carregar_ledger()
    if not ledger:
        print("ledger vazio — nenhum video sorteado ainda.")
        return
    for pag, eixos in sorted(ledger.items()):
        print("\n%s" % pag.upper())
        for eixo, vals in sorted(eixos.items()):
            cont = {}
            for v in vals:
                cont[v] = cont.get(v, 0) + 1
            print("  %-10s %s" % (eixo, ", ".join("%s:%d" % kv for kv in sorted(cont.items()))))


def main():
    ap = argparse.ArgumentParser(description="Randomizador do agente NECROSE")
    ap.add_argument("--pagina", choices=sorted(ETNIA))
    ap.add_argument("--n", type=int, default=1)
    ap.add_argument("--seed", type=int)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--stats", action="store_true")
    a = ap.parse_args()

    if a.stats:
        stats(); return 0
    if not a.pagina:
        ap.error("informe --pagina <joe|ray|matt|marcus|chuck> (ou --stats)")

    rng = random.Random(a.seed)
    ledger = _carregar_ledger()
    saida = 0
    for i in range(a.n):
        spec = sortear(a.pagina, rng, ledger)
        blocos = montar(spec)
        achados = lint(spec, blocos)
        if a.n > 1:
            print("\n\n########## VIDEO %d/%d ##########\n" % (i + 1, a.n))
        imprimir(spec, blocos, achados)
        if any(x[0] == "ERRO" for x in achados):
            saida = 1
        if not a.dry_run:
            _gravar_ledger(ledger, spec)
    return saida


if __name__ == "__main__":
    sys.exit(main())
