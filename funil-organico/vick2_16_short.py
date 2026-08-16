# -*- coding: utf-8 -*-
"""VICK 2 16 — as QUINZE cenas da fonte, uma por sorteio.

    python funil-organico/vick2_16_short.py --autoteste
    python funil-organico/vick2_16_short.py --pagina joe

===============================================================================
 ⛔⛔ POR QUE ESTE AGENTE EXISTE, E O QUE O `vick16` ERROU
===============================================================================
Ordem do operador (2026-08-16), com o lote renderizado na tela:

    *"Tire celular das cenas do agente vick16. Voce nao respeitou as copys
    visuais tb, onde ha, em alguns dos videos fontes, homens massageando
    sempre uma parte do corpo com o Vick VapoRub. Quero que vc construa um
    novo agente do zero chamado vick2_16, pois esse ficou uma merda."*

E depois, fechando o desenho:

    *"quero que no take 1 tenha sorteio de cada uma das cenas dos videos
    fontes, pool de acoes sendo cada cena dos videos fontes"*

 1. **O CELULAR APARECIA NO QUADRO, E A CULPA E' DO PROMPT.** O `vick16`
    descrevia a camera assim: `POV of a man standing over the surface with the
    phone in his free hand`. O gerador de IMAGEM nao entende isso como
    instrucao de enquadramento — ele **desenha o telefone**, e os renders
    saiam com uma mao segurando um celular no meio da cena.
    ⭐ AQUI A CAMERA DESCREVE O ANGULO E NUNCA O APARELHO. Nenhuma string
    deste arquivo contem `phone`, `camera`, `iPhone` ou `filming` dentro de um
    bloco IMAGE — e a lente VK1 reprova se alguem puser.

 2. **A MASSAGEM NO CORPO FOI IGNORADA, E A LEITURA OTICA TINHA VISTO.** Nao
    foi falha de leitura — o mapa dizia, com todas as letras:
        v03 *"ele passa a bolota de creme branco na propria NUCA, esfrega"*
        v09 *"ele ESFREGA e espalha um bolo de creme branco no proprio peito"*
        v10 *"esfrega a pomada na nuca com movimentos circulares"*
        v15 *"PASSA O CREME NA NUCA, a mancha branca fica bem visivel"*
    Eu li e nao usei. **Quatro dos quinze videos aplicam a pomada no corpo**, e
    isso e' o beat que prova o mecanismo — sem ele o video mostra alguem
    mexendo um pote e nunca diz o que se faz com aquilo.

 3. **O POOL AGORA E' A PROPRIA FONTE.** Nao ha cena inventada, nao ha acao
    inventada: as 15 entradas de `CENAS` sao os 15 videos, cada um com o
    ambiente, a superficie, o angulo e **a sequencia de gestos que aquele
    video faz**, em dois takes. O `vick16` tinha 100 cenas construidas e o
    operador reprovou por "elemento visual sem nexo"; aqui o nexo vem de
    graca, porque cada cena JA' EXISTE e ja' foi filmada.

===============================================================================
 A FONTE
===============================================================================
15 reels em `C:/Users/edlut/Music/OKC-Likes-Viewer-master/vick`, 300s, lidos a
2 quadros/s (566 quadros, um a um) e transcritos com `faster-whisper small.en`.
Mapa completo: [`concorrentes/vick-mapa-visual.md`](../concorrentes/vick-mapa-visual.md).

⭐⭐ O MECANISMO: abre o pote de VapoRub, despeja o po de gelatina Knox DENTRO
dele, mistura com o dedo, as vezes acrescenta mel — e em quatro dos quinze o
homem **passa a mistura na propria nuca ou no peito**. A fala nunca nomeia
nada disso; ela diz `toxic buildup`, `flushes the plaque`.

⛔ Mesma fonte dos tres BANHO; o que separa e' o VICKS, em 13 dos 15.
⛔ A frase do rodeio (v03) nao entra: e' exclusiva do `banho16_v2`.
⛔ TODA FALA E' VERBATIM DA FONTE — cada beat carrega o `v` do video de onde
saiu, e o autoteste conta quantos chegaram sem origem (tem de ser zero).
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

APP = TITULO = "AGENTE VICK 2 16"
SUBTITULO = ("2 takes de 8s · as 15 cenas REAIS da fonte, uma por sorteio · "
             "4 delas passam a pomada no corpo · sem celular em quadro")
SLUG = "vick2-16"
SEXOS = ("homem",)
CENAS_UI = ["1 · O HOOK", "2 · O MECANISMO + CTA"]
LEDGER = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      ".vick2-16-ledger.json")

KEYWORD_UI = True
KEYWORD_NATIVA = "recipe"

TETO_FALA = {1: 25, 2: 25}
PISO_FALA = {1: 8, 2: 10}

NUCLEO = ("baseball bat", "small bat", "shrinking bat", "pipes")

BANIDOS_CTA = {"book": "quebra a automacao de DM",
               "yes": "quebra a automacao de DM"}
BANIDOS_IMAGE = {}
BANIDOS_TAKE = {}
BANIDOS_BLOCO = {}

ETNIA = {"joe": "white American", "marcus": "Black American",
         "ray": "white American", "chuck": "white American",
         "matt": "white American"}


# ===========================================================================
# ⭐⭐ AS 15 CENAS — cada uma E' UM VIDEO DA FONTE
# ===========================================================================
# ⛔ Nada aqui foi inventado. `amb`, `sup`, `cam`, `t1` e `t2` saem da leitura
# otica quadro a quadro daquele video especifico.
# ⛔ `cam` DESCREVE O ANGULO E NUNCA O APARELHO — foi o telefone escrito no
# prompt que fez o gerador desenhar um celular na mao do homem.
# ⭐ `corpo=True` marca os quatro videos em que ele PASSA A POMADA no proprio
# corpo. Esse beat prova o mecanismo, e foi o que a v1 deixou de fora.
CENAS = [
    {"id": "v01_borda_banheira", "v": "v01", "corpo": False,
     "curto": "borda da banheira enchendo",
     "amb": "a small older bathroom, the white alcove tub filling behind with a "
            "chrome spout pouring, white square tile with dark grout",
     "sup": "the flat white capping ledge on top of the tub surround",
     "cam": "Shot from above at about forty-five degrees, handheld with a "
            "slight constant drift, closing in slowly",
     "audio": "tap water running into the filling tub, a small tiled echo",
     "t1": "his index finger is sunk into the jar, lifting a small lump of the "
           "white cream clear of the rim and holding it up",
     "t2": "the mixture in the jar has risen into a pale foam of large bubbles "
           "that reaches the rim"},

    {"id": "v02_copo_ambar", "v": "v02", "corpo": False,
     "curto": "copo âmbar na bancada da pia",
     "amb": "a bright clean bathroom with daylight from a window and a "
            "frameless mirror behind",
     "sup": "the white cultured-marble vanity top, left of the oval basin",
     "cam": "Locked off at chest height, angled twenty-five degrees down onto "
            "the vanity, the frame never moving",
     "audio": "quiet room tone, a spoon clinking against glass",
     "t1": "his hands hold a torn sachet over a tall glass of amber liquid and "
           "the pale powder is falling onto the surface, floating there as a "
           "white island",
     "t2": "the long spoon is lifted out of the glass and the thickened liquid "
           "runs off it in slow heavy ropes"},

    {"id": "v03_nuca_deck", "v": "v03", "corpo": True,
     "curto": "creme na nuca · deck de cerâmica",
     "amb": "a home bathroom with a large built-in tub filled with pale mint "
            "water and warm beige walls",
     "sup": "the wide beige ceramic tub deck, grout lines crossing it",
     "cam": "Shot from behind and just above his shoulder at head height, "
            "handheld, he never turns to the viewer",
     "audio": "still bath water lapping faintly, a small tiled echo",
     "t1": "he is rubbing a lump of white cream into the back of his own neck "
           "with two fingers, the white smear clearly spread across the nape",
     "t2": "on the tub deck below, honey is running from a tilted spoon onto "
           "the powder heaped in the open jar and the mixture is foaming up"},

    {"id": "v04_caddy_inox", "v": "v04", "corpo": False,
     "curto": "caddy de inox sob o chuveiro",
     "amb": "a closed shower stall, two cream tiled walls meeting at a corner, "
            "the dark shower head running a fan of water in front",
     "sup": "a brushed stainless corner caddy clamped to the dark riser pole",
     "cam": "Framed straight at the corner from chest height, tilted slightly "
            "down, almost still",
     "audio": "the shower running steady on tile, water pattering on the caddy",
     "t1": "one hand holds the open jar up while the other tips the torn box "
           "and a visible jet of pale powder falls into it",
     "t2": "the jar is held up toward the viewer, the pale foam risen to the rim "
           "and water beading on the outside of the glass"},

    {"id": "v05_banquinho", "v": "v05", "corpo": False,
     "curto": "banquinho de madeira ao lado da banheira",
     "amb": "a domestic bathroom, a white alcove tub half full of still "
            "blue-green water, a coiled hand-shower hose on the wall",
     "sup": "the pale wooden seat of a low solid-wood stool pushed against the "
            "outer skirt of the tub",
     "cam": "Shot from waist height looking down at about forty-five degrees, "
            "the stool running diagonally across the frame",
     "audio": "still bath water shifting, a small room echo",
     "t1": "his finger is lifted out of the jar with cream hanging off the tip "
           "in a thread, the open jar held below it",
     "t2": "honey is pouring from a metal spoon into the jar and the mixture "
           "has swollen into a pale foam"},

    {"id": "v06_nicho_madeira", "v": "v06", "corpo": False,
     "curto": "nicho na parede de madeira de demolição",
     "amb": "a shower walled in grey reclaimed barn wood with heavy knots and "
            "grain, a rain head pouring a straight curtain of water",
     "sup": "the smooth white plaster floor of a square niche cut into the "
            "wood wall",
     "cam": "Frontal and almost perpendicular to the wall at chest height, the "
            "niche centred and symmetrical like a vitrine, static",
     "audio": "the rain head drumming on the shower floor",
     "t1": "both hands hold the box and the open jar out under the falling "
           "water, tipping a continuous jet of pale powder from one into the "
           "other, the water soaking both",
     "t2": "the jar stands back in the niche with the mixture risen into a "
           "pale foam, water running past the mouth of the niche"},

    {"id": "v07_caddy_arame", "v": "v07", "corpo": False,
     "curto": "caddy de arame cromado",
     "amb": "a small tiled shower with the head running the whole time, water "
            "crossing the frame diagonally and speckling the foreground",
     "sup": "the upper tray of a two-tier chrome wire caddy hung from the "
            "shower pipe at chest height",
     "cam": "Chest height pointing slightly down at the wire tray, nearly "
            "still, water crossing in front",
     "audio": "water pattering through the wire tray and onto the floor",
     "t1": "both hands present the open jar to the viewer, turning it, the torn "
           "box held beside it",
     "t2": "a finger is lifted from the jar with a heavy lump of white cream "
           "hanging from it, the foam risen behind"},

    {"id": "v08_tabua_cozinha", "v": "v08", "corpo": False,
     "curto": "tábua de açougueiro na cozinha",
     "amb": "a rustic country kitchen with hard morning sun raking across the "
            "counter from a wooden window frame",
     "sup": "a pale butcher-block counter with visible glue joints, knife "
            "scores and dark water stains",
     "cam": "Over the shoulder at about forty-five degrees, looking down onto "
            "the bowl on the counter",
     "audio": "kitchen room tone, a spoon tapping wood, birds outside",
     "t1": "both hands hold a torn sachet over an empty bowl and a vivid blue "
           "pour is falling out of it, spreading across the bottom",
     "t2": "amber honey is running in a thick continuous ribbon over the blue, "
           "which has set into a turquoise gel with a spiral in the middle"},

    {"id": "v09_peito_marmore", "v": "v09", "corpo": True,
     "curto": "creme no peito · mármore com LED azul",
     "amb": "an upmarket bathroom with white veined marble and a blue LED strip "
            "running along the tub edge and the wall",
     "sup": "the white marble vanity top, the basin cropped at the bottom edge",
     "cam": "Fixed at hip height, frontal and very slightly low, his torso "
            "centred",
     "audio": "a quiet room, water moving once in the tub",
     "t1": "he is rubbing a lump of white cream across his own bare chest in "
           "circles with his right hand while his left holds the open jar and "
           "the turquoise lid, the glossy smear clearly visible on the skin",
     "t2": "over the tub edge, a long thick ribbon of amber honey is falling "
           "from a raised spoon into the jar and crossing half the frame",
     "peito": True},

    {"id": "v10_nuca_pia", "v": "v10", "corpo": True,
     "curto": "pomada na nuca · bancada azulejada",
     "amb": "an old lived-in American bathroom, chequered beige tile to half "
            "height, cream paint above, frosted glass window to the right",
     "sup": "the tiled sink counter, stained grout between the beige squares",
     "cam": "From behind and just to his left at shoulder height, almost "
            "touching, his back filling the frame",
     "audio": "a quiet house, a tap dripping once",
     "t1": "he is rubbing the ointment into the back of his neck in circles "
           "with his head bowed, the white cream covering a widening area from "
           "the base of the nape up to the hairline",
     "t2": "on the counter, one hand tips a sachet and a jet of pale powder "
           "falls into the open jar while the other holds a spoon of honey "
           "dripping above it"},

    {"id": "v11_prateleira_macica", "v": "v11", "corpo": False,
     "curto": "prateleira de madeira maciça no box",
     "amb": "a closed shower stall with large off-white tile and a dark round "
            "rain head running water the whole time",
     "sup": "a thick varnished honey-oak corner shelf wedged into the corner, "
            "water beading on it",
     "cam": "Chest height looking down into the corner of the stall, the frame "
            "never moving",
     "audio": "the shower running steadily, water hitting wood",
     "t1": "both hands raise the box to the viewer with the label turned out, "
           "the open jar waiting below",
     "t2": "a finger is lifted in the foreground with the white ointment "
           "hanging and running off it, the jar held underneath"},

    {"id": "v12_tampa_vaso", "v": "v12", "corpo": False,
     "curto": "tampa do vaso como bancada",
     "amb": "a clean modern bathroom, large beige tile with a border course, "
            "a white two-piece toilet centred",
     "sup": "the closed white toilet lid, used flat as a work surface",
     "cam": "Standing in front of it at chest height, angled thirty degrees "
            "down, position almost fixed",
     "audio": "a very quiet house, a spoon touching glass",
     "t1": "a spoon carrying a white block of set gelatin is being lowered "
           "into a tall blue glass",
     "t2": "a thick ribbon of amber is falling from the spoon and sinking in a "
           "spiral through the blue, settling as a golden layer at the bottom"},

    {"id": "v13_tampo_cuba", "v": "v13", "corpo": False,
     "curto": "tigela no tampo à direita da cuba",
     "amb": "a plain home bathroom, a white basin set in cultured marble with "
            "a two-handle chrome tap",
     "sup": "the flat white counter to the right of the basin, the bowl "
            "standing on the dry top and not in the sink",
     "cam": "From chest height looking straight down at about sixty degrees, "
            "handheld with a slight drift",
     "audio": "a tap dripping once, tiled room tone",
     "t1": "a hand tips an open paper sachet over a bowl of clear water and "
           "blue powder is falling in, spreading as a cloud through it",
     "t2": "honey is pouring from a spoon in an unbroken thread into the "
           "thickened blue gel, chia seeds floating in a dark patch on top"},

    {"id": "v14_granito_regua", "v": "v14", "corpo": False,
     "curto": "creme descendo pela régua · granito bege",
     "amb": "a shower stall with the water running the whole time, curtains of "
            "spray crossing the frame, mottled beige stone walls",
     "sup": "a built-in quarter-circle corner shelf in mottled beige granite, "
            "soaked",
     "cam": "At eye height facing the corner of the stall straight on, not "
            "angled down, zooming in slowly",
     "audio": "the shower running on stone, water hitting the shelf",
     "t1": "he has taken a little white cream on his fingertip and is wiping it "
           "downward along the face of the wooden ruler standing on the shelf",
     "t2": "the powder has been tipped into the open jar and his finger is "
           "pressing the mixture down, the foam rising around it"},

    {"id": "v15_nuca_espelho", "v": "v15", "corpo": True,
     "curto": "creme na nuca diante do espelho",
     "amb": "a bathroom in front of a mirrored cabinet, its glass shelf behind "
            "him crowded with brushes and bottles",
     "sup": "no counter at all in this shot: he holds the open jar in his own "
            "hand",
     "cam": "Over his shoulder at chest height, a little behind and to his "
            "right, the mirror giving back part of his face",
     "audio": "a quiet bathroom, a lid set down on glass",
     "t1": "with his back to the mirror he has taken white cream from the jar "
           "with two fingers and is spreading it across the back of his neck, "
           "the white smear reaching round to the side of the throat",
     "t2": "down on the tub step, both hands tip a torn sachet and the pale "
           "powder falls into the open jar with the turquoise lid parked "
           "beside it"},
]


# ===========================================================================
# ⭐⭐ A REGIAO DO CORPO — eixo pedido pelo operador (2026-08-16)
# ===========================================================================
# *"Quero itens dentro da pool que variem qual regiao do corpo esta havendo a
# massagem com o Vick VapoRub: ora peitoral, ora nuca, ora braco, ora barriga,
# ora ombro."*
#
# ⛔⛔ A REGIAO CARREGA A PROPRIA CAMERA, e isso nao e' capricho: esfregar a
# NUCA so' se ve' POR TRAS; a BARRIGA so' se ve' DE FRENTE. Se a regiao fosse
# sorteada solta e o angulo viesse da cena, metade dos videos mostraria um
# homem esfregando algo que a camera nao alcanca. E' o mesmo acoplamento que
# derrubou a primeira tentativa deste agente — aqui ele esta' declarado.
#
# ⚠️ DUAS SAO LIDAS, TRES SAO CONSTRUIDAS. A fonte so' faz nuca (v03, v10, v15)
# e peito (v09); ombro, braco e barriga sao extrapolacao sob a ordem acima, e
# ficam marcadas para o campo saber a que atribuir resultado.
REGIOES = [
    {"id": "nuca", "curto": "nuca", "fonte": "lido",
     "img": "rubbing a lump of the white cream into the back of his own neck "
            "with two fingers, the white smear clearly spread across the nape",
     "cam": "Shot from behind and just above his shoulder at head height, his "
            "head bowed, he never turns toward the viewer"},
    {"id": "peito", "curto": "peitoral", "fonte": "lido",
     "img": "rubbing a lump of the white cream across his own bare chest in "
            "slow circles with one hand, the glossy smear left on the skin",
     "cam": "Frontal at chest height, very slightly low, his torso centred"},
    {"id": "ombro", "curto": "ombro", "fonte": "construido",
     "img": "working the white cream into the top of his own shoulder with the "
            "opposite hand, the smear sitting over the muscle",
     "cam": "Three-quarter view from the front at chest height, the worked "
            "shoulder nearer the viewer"},
    {"id": "braco", "curto": "braço", "fonte": "construido",
     "img": "spreading the white cream along his own forearm from the wrist "
            "upward, the pale film left on the skin",
     "cam": "Looking down along his own arm from just above it, the forearm "
            "running diagonally across the frame"},
    {"id": "barriga", "curto": "barriga", "fonte": "construido",
     "img": "smoothing the white cream low across his own stomach with a flat "
            "palm, the smear catching the light",
     "cam": "Frontal at chest height looking slightly down, his stomach "
            "filling the lower half of the frame"},
]


# ===========================================================================
# ⛔ O QUE E' CONSTANTE — a licao que o `vick16` v2 aprendeu e esta versao herda
# ===========================================================================
# Os props sao os mesmos nos quinze videos. Eles NAO sao pool: sao a assinatura
# da pagina, e foi somar eixos sorteados que produziu o "elemento visual sem
# nexo" da primeira tentativa.
PROPS = ("an open cobalt-blue jar of vapour rub with its turquoise lid lying "
         "beside it, a torn gelatin sachet, a plain yellow wooden ruler lying "
         "untouched, and a brown cardboard sign with `growth hack` written on "
         "it in black marker leaning against the wall behind")

PROPS_CURTO = ("the same blue jar, the torn sachet, the wooden ruler and the "
               "cardboard sign")

HOMEM = ("a %d-year-old %s man with heavy weathered hands, thick knuckles and "
         "sun spots across the backs")

LUZ = "plain domestic light, no colour cast"

# ⛔⛔ A CAUDA NAO NOMEIA APARELHO NENHUM. A do `vick16` dizia `Shot on an
# iPhone held in one hand` e a camera dizia `with the phone in his free hand` —
# o gerador desenhava o telefone na mao do homem. Aqui se pede a ESTETICA, e a
# palavra `phone` nao existe no arquivo.
# ⛔ E NAO SE ESCREVE `no phone in frame`: negacao INJETA o token, e' a licao do
# `not a celebrity` que o parque inteiro pagou. Silencio, nao negacao.
CAUDA = ("Everyday amateur snapshot look, slight natural sway, soft sensor "
         "grain. No on-screen text, no subtitles, no captions, no watermark.")


# ===========================================================================
# A COPY — VERBATIM DA FONTE, cada beat com o video de origem
# ===========================================================================
HOOKS = [
    {"v": "v01", "txt": "I am {idade} and this is the shower hack I use every "
     "night to look bigger and last longer."},
    {"v": "v02", "txt": "If you are single, do not try this. If you are "
     "married, try it in moderation."},
    {"v": "v03", "txt": "If you are a man over 50 and you are not doing this "
     "trick yet, you are already falling behind."},
    {"v": "v05", "txt": "Struggling to stay hard, or with your small size? "
     "That is not about getting older."},
    {"v": "v06", "txt": "I am {idade} and I fixed my small bat with a shower "
     "habit."},
    {"v": "v08", "txt": "Over 60 and tired of going soft or feeling small? "
     "This kitchen hack makes you hard."},
    {"v": "v09", "txt": "At {idade} I wake up bigger than I did in my twenties "
     "with this trick."},
    {"v": "v10", "txt": "Why accept a shrinking bat and going soft? At {idade} "
     "I stopped accepting it."},
    {"v": "v11", "txt": "My wife almost cheated on me. She said to my face "
     "that I was not enough for her anymore."},
    {"v": "v12", "txt": "Is going soft ruining the mood? A bizarre nighttime "
     "trick saved my marriage."},
    {"v": "v13", "txt": "Over 50 and tired of going soft or feeling small? "
     "This shower hack brings your size back."},
    {"v": "v15", "txt": "Stop accepting a shrinking bat. I am {idade} and a "
     "bizarre nighttime habit restored my size."},
]

MECANISMOS = [
    {"v": "v06", "txt": "It simply unclogs the toxic build-up stopping your "
     "blood flow."},
    {"v": "v09", "txt": "It melts the invisible blockage choking your blood "
     "supply while you sleep."},
    {"v": "v12", "txt": "It flushes the hidden blockages trapping your blood."},
    {"v": "v05", "txt": "This morning trick flushes out the toxins clogging "
     "your blood vessels."},
    {"v": "v08", "txt": "It flushes the build-up choking your blood flow and "
     "brings back your real size."},
    {"v": "v01", "txt": "This recipe removes the toxic build-up sitting in "
     "your arteries."},
    {"v": "v10", "txt": "It flushes the plaque choking your vessels and forces "
     "the blood back down."},
]

PROVAS = [
    {"v": "v11", "txt": "Fifteen seconds in the shower, one ingredient you "
     "already walked past at the supermarket."},
    {"v": "v11", "txt": "Twenty-one days later I was four inches bigger."},
    {"v": "v03", "txt": "I use zero blue pills."},
    {"v": "v05", "txt": "Men are having brutal results in forty-eight hours."},
    {"v": "v01", "txt": "No side effects, no pharmacy."},
    {"v": "v10", "txt": "No blue pills, no pharmacy."},
    {"v": "v06", "txt": "Once the pipes are clear you get maximum size."},
]

CTAS = [
    {"v": "v11", "txt": "Comment recipe, and I will send it to you right now."},
    {"v": "v03", "txt": "Comment recipe, for the step-by-step video."},
    {"v": "v08", "txt": "Comment recipe, and I will send you the step-by-step."},
    {"v": "v01", "txt": "Comment recipe, and I will send you the full video."},
]

IDADES = (64, 65, 66, 67, 72, 74)


# ===========================================================================
# SORTEIO
# ===========================================================================
EIXOS_LEDGER = ("cena", "regiao", "hook", "mecanismo", "prova", "cta")


def _chave(x):
    return x.get("id") or x.get("v")


def _carregar_ledger():
    try:
        with open(LEDGER, "r", encoding="utf-8") as f:
            return json.load(f)
    except (IOError, ValueError):
        return {}


def _anotar(ledger, spec):
    hist = ledger.setdefault(spec["pagina"], {})
    for eixo in EIXOS_LEDGER:
        val = spec.get(eixo)
        if isinstance(val, dict):
            hist.setdefault(eixo, []).append(_chave(val))


def _gravar_ledger(ledger, spec=None):
    if spec is not None:
        _anotar(ledger, spec)
    try:
        with open(LEDGER, "w", encoding="utf-8") as f:
            json.dump(ledger, f, ensure_ascii=False, indent=1)
    except IOError:
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


def _cap(s):
    return s[0].upper() + s[1:] if s else s


_RX_ORGAO = re.compile(
    r"\b(%s)\b" % "|".join(re.escape(n) for n in sorted(NUCLEO, key=len,
                                                        reverse=True)), re.I)


def _orgaos(txt):
    return {m.group(0).lower() for m in _RX_ORGAO.finditer(txt or "")}


def _gesto(spec):
    """O gesto do take 1: da REGIAO quando a cena tem massagem, senao da cena.

    ⛔ E o ANGULO acompanha o gesto, nunca o contrario. A camera da cena mostra
    a superficie; a camera da regiao mostra o CORPO. Trocar o gesto e manter o
    angulo entrega um homem esfregando algo fora de quadro.
    """
    c = spec["cena"]
    if c["corpo"]:
        return c["cam_corpo"] if False else spec["regiao"]["img"]
    return c["t1"]


def _angulo(spec):
    c = spec["cena"]
    return spec["regiao"]["cam"] if c["corpo"] else c["cam"]


def _falas(spec, rng, quais=(0, 1)):
    f = dict(enumerate(spec.get("falas", ["", ""])))
    if 0 in quais:
        f[0] = spec["hook"]["txt"].replace("{idade}", str(spec["idade"]))
    if 1 in quais:
        # ⛔ O TRIO INTEIRO e' sorteado entre as combinacoes que cabem nos 25 —
        # e nao em cascata. Em cascata a PROVA (o beat concreto) so' cabia em
        # 26% dos videos, e ela e' justamente o antidoto do drifting.
        # ⛔ E o trio nao pode trazer um apelido do orgao que brigue com o do
        # hook: o CT4 se resolve na ESCOLHA, nunca reescrevendo o texto, senao
        # o verbatim se perde — que e' a unica guarda contra a copy vaga.
        do_hook = _orgaos(f.get(0) or (spec.get("falas") or [""])[0])
        trios = [(p, m, c) for p in PROVAS for m in MECANISMOS for c in CTAS
                 if _palavras(p["txt"]) + _palavras(m["txt"])
                 + _palavras(c["txt"]) <= TETO_FALA[2]
                 and len(do_hook | _orgaos(p["txt"]) | _orgaos(m["txt"])
                         | _orgaos(c["txt"])) <= 1]
        if trios:
            p, m, c = rng.choice(trios)
            spec["prova"], spec["mecanismo"], spec["cta"] = p, m, c
            f[1] = " ".join((m["txt"], p["txt"], c["txt"]))
        else:
            spec["prova"] = None
            f[1] = " ".join((spec["mecanismo"]["txt"], spec["cta"]["txt"]))
    return f


def _cenas_possiveis(travas):
    """As cenas que podem sair, dadas as travas.

    ⛔ Se o operador TRAVOU uma regiao do corpo, so' as cenas COM massagem
    podem sair — senao ele escolhe `barriga`, cai numa cena que so' mexe o
    pote e conclui que o botao nao faz nada. Botao que promete e entrega outra
    coisa e' pior que botao ausente (licao GO21 do GOOD 16).
    """
    if travas.get("regiao"):
        return [c for c in CENAS if c["corpo"]] or list(CENAS)
    return list(CENAS)


def sortear(pagina, rng, ledger, travas=None):
    travas = travas or {}
    hist = (ledger or {}).get(pagina, {})
    spec = {
        "pagina": pagina,
        "etnia": ETNIA.get(pagina, "white American"),
        "idade": rng.choice(IDADES),
        # ⭐ O EIXO PEDIDO PELO OPERADOR: cada sorteio pega UMA das 15 cenas da
        # fonte, com a acao daquele video.
        "cena": (_por_id(CENAS, travas["cena"]) if travas.get("cena")
                 else _fresco(_cenas_possiveis(travas),
                              hist.get("cena", [])[-6:], rng)),
        # ⭐ So' as cenas de corpo usam; nas outras fica None e o `t1` da cena
        # vale como esta'. Sortear regiao para uma cena que nao tem massagem
        # seria eixo no painel que nao muda o video — o defeito que este repo
        # chama de botao que mente.
        "regiao": (_por_id(REGIOES, travas["regiao"]) if travas.get("regiao")
                   else _fresco(REGIOES, hist.get("regiao", [])[-3:], rng)),
        "hook": (_por_id(HOOKS, travas["hook"], "v") if travas.get("hook")
                 else _fresco(HOOKS, hist.get("hook", [])[-5:], rng)),
        "mecanismo": _fresco(MECANISMOS, hist.get("mecanismo", [])[-3:], rng),
        "cta": _fresco(CTAS, hist.get("cta", [])[-2:], rng),
    }
    spec["falas"] = [v for _, v in sorted(_falas(spec, rng).items())]
    return spec


def nova_fala(spec, i, rng):
    if i == 0:
        spec["hook"] = _fresco(HOOKS, [spec["hook"]["v"]], rng)
    else:
        spec["mecanismo"] = _fresco(MECANISMOS, [spec["mecanismo"]["v"]], rng)
        spec["cta"] = _fresco(CTAS, [spec["cta"]["v"]], rng)
    return _falas(spec, rng, quais=(i,))[i]


# ===========================================================================
# MONTAGEM
# ===========================================================================
def montar(spec):
    c = spec["cena"]
    h = HOMEM % (spec["idade"], spec["etnia"])
    b = {}

    b["BLOCO 0 (REF)"] = (
        "REF 01: Photo of a real person, %s, chest up, facing forward, calm "
        "steady expression. Plain neutral gray background, soft even frontal "
        "light, hands out of frame, no objects. Slight sensor grain, raw "
        "amateur photo look. No subtitles, no captions, no burned-in text, no "
        "watermark." % h)

    # ⛔ A ORDEM E' GRAMATICA: os props vem antes da superficie porque varias
    # superficies terminam numa oracao subordinada, e o verbo caia depois dela.
    b["IMAGE 01/02"] = (
        "IMAGE 01/02: Inside %s. On %s stand %s. In frame is %s, and %s. %s. "
        "%s. %s"
        % (c["amb"], c["sup"], PROPS, h, _gesto(spec), _angulo(spec),
           _cap(LUZ), CAUDA))

    b["IMAGE 02/02"] = (
        "IMAGE 02/02: Inside %s, the same place in the same framing. On %s, "
        "%s. %s are still in frame. It is the same %d-year-old %s man "
        "from the first scene, not a different person. %s. %s. %s"
        % (c["amb"], c["sup"], c["t2"], _cap(PROPS_CURTO),
           spec["idade"], spec["etnia"], _angulo(spec), _cap(LUZ), CAUDA))

    b["TAKE 01/02"] = (
        "TAKE 01/02: Animate the provided image exactly. %s and there are no "
        "cuts. He does the movement once, slowly, and stops. Audio: %s. Only "
        "he speaks.\nDialogue: \"%s\""
        % (_angulo(spec), c["audio"], spec["falas"][0]))

    b["TAKE 02/02"] = (
        "TAKE 02/02: Animate the provided image exactly. %s and there are no "
        "cuts. The movement finishes and settles; nothing else in the frame "
        "changes. Audio: %s. Only he speaks.\nDialogue: \"%s\""
        % (_angulo(spec), c["audio"], spec["falas"][1]))

    return sc.selar_takes(sc.selar_tags(b))


# ===========================================================================
# AS LENTES
# ===========================================================================
_RX_APARELHO = re.compile(
    r"\b(phone|iphone|smartphone|handset|camera|camcorder|lens|filming|filmed|"
    r"recording|selfie|tripod|gimbal)\b", re.I)


def _vk1_sem_celular(spec, blocos, ach):
    """⛔⛔ A LENTE QUE ESTE AGENTE EXISTE PARA TER.

    O `vick16` escrevia `POV of a man ... with the phone in his free hand` e o
    gerador DESENHAVA o telefone: os renders sairam com um celular no meio da
    cena. Descrever o aparelho num prompt de IMAGEM nao instrui enquadramento,
    instrui CONTEUDO.
    ⚠️ Vale nos blocos de IMAGE, onde o modelo desenha. Nos TAKE a palavra
    `camera` seria igualmente perigosa, entao a lente cobre os quatro.
    """
    for k, v in blocos.items():
        if k.startswith("BLOCO"):
            continue
        m = _RX_APARELHO.search(v)
        if m:
            ach.append(("ERRO", "VK1: %s nomeia %r — aparelho escrito no prompt "
                                "vira aparelho DESENHADO no quadro"
                        % (k, m.group(0))))


def _vk2_cena_inteira(spec, blocos, ach):
    """A cena sorteada tem de chegar inteira: lugar, superficie e o gesto."""
    c = spec["cena"]
    if c["amb"] not in blocos["IMAGE 01/02"]:
        ach.append(("ERRO", "VK2: a IMAGE 01 nao acontece no ambiente sorteado"))
    if c["sup"] not in blocos["IMAGE 01/02"]:
        ach.append(("ERRO", "VK2: a IMAGE 01 sem a superficie da cena"))
    if _gesto(spec) not in blocos["IMAGE 01/02"]:
        ach.append(("ERRO", "VK2: a IMAGE 01 sem o GESTO daquele video — e' o "
                            "gesto que faz a cena ser aquela cena"))
    if c["t2"] not in blocos["IMAGE 02/02"]:
        ach.append(("ERRO", "VK2: a IMAGE 02 sem o payoff daquele video"))


def _vk3_props(spec, blocos, ach):
    """Os props sao CONSTANTES na fonte — nao sao opcionais."""
    if PROPS not in blocos["IMAGE 01/02"]:
        ach.append(("ERRO", "VK3: a IMAGE 01 sem os props travados"))
    if _cap(PROPS_CURTO) not in blocos["IMAGE 02/02"]:
        ach.append(("ERRO", "VK3: a IMAGE 02 sem os props travados"))


def _vk4_copy_com_origem(spec, blocos, ach):
    """⛔ Toda fala tem de ser verbatim da fonte — a guarda contra o drifting."""
    origem = {h["txt"].replace("{idade}", str(spec["idade"])) for h in HOOKS}
    if spec["falas"][0] not in origem:
        ach.append(("ERRO", "VK4: a fala 1 nao e' verbatim de nenhum video"))
    for beat in (spec["mecanismo"], spec.get("prova"), spec["cta"]):
        if beat and beat["txt"] not in spec["falas"][1]:
            ach.append(("ERRO", "VK4: o beat %s nao chegou a fala 2" % beat["v"]))


def _vk5_orcamento(spec, blocos, ach):
    for i, fala in enumerate(spec["falas"], 1):
        n = _palavras(fala)
        if n > TETO_FALA[i]:
            ach.append(("ERRO", "VK5: cena %d com %d palavras (teto %d)"
                        % (i, n, TETO_FALA[i])))
        if n < PISO_FALA[i]:
            ach.append(("AVISO", "VK5: cena %d com so' %d palavras" % (i, n)))


def _vk6_fala_no_take(spec, blocos, ach):
    for i, k in enumerate(("TAKE 01/02", "TAKE 02/02")):
        if ('Dialogue: "%s"' % spec["falas"][i]) not in blocos[k]:
            ach.append(("ERRO", "VK6: a fala %d nao chega verbatim ao %s"
                        % (i + 1, k)))


def _ct16(spec, blocos, ach):
    """⛔ CT4b desligado (apelidos da fonte) e CT5 desligado: aqui a moeda do
    comentario e' o PASSO A PASSO, nao a receita. Foi proibir o concreto que
    produziu o drifting da primeira tentativa."""
    fora = []
    sc.lint_copy16(sys.modules[__name__], spec, fora)
    ach.extend(x for x in fora if not x[1].startswith(("CT4b:", "CT5:")))


def _anticeleb(spec, blocos, ach):
    sc.lint_anticeleb(blocos, ach)


def _painel(spec, blocos, ach):
    sc.lint_painel_honesto(sys.modules[__name__], spec, blocos, ach)


def lint(spec, blocos):
    return sc.lint_curto(
        sys.modules[__name__], spec, blocos, (1, 2), TETO_FALA,
        literais=("recipe",), cota_min=0,
        extras=(_ct16, _anticeleb, _painel, _vk1_sem_celular, _vk2_cena_inteira,
                _vk3_props, _vk4_copy_com_origem, _vk5_orcamento,
                _vk6_fala_no_take))


# ===========================================================================
# RESUMO E PAINEL
# ===========================================================================
def resumo_pt(spec):
    c = spec["cena"]
    return ("16s, DOIS takes. A CENA E' O %s DA FONTE: %s.%s "
            "Take 1 — %s. Take 2 — %s. Homem de %d anos, %s, e os mesmos "
            "props dos quinze videos (pote azul, sache, regua, placa "
            "`growth hack`). Beats: hook %s · mecanismo %s · prova %s · CTA "
            "%s, todos verbatim. Fecha em `recipe`. SEM celular em quadro."
            # ⚠️ O resumo mostra o gesto RESOLVIDO, nao o `t1` cravado da cena:
            # com a regiao sorteada, o texto da cena esta' desatualizado e o
            # operador leria "nuca" num video de barriga. Painel que descreve
            # outra coisa que o prompt e' pior que painel sem descricao.
            % (c["v"].upper(), c["curto"],
               ("  ⭐ ELE PASSA A POMADA NO %s."
                % spec["regiao"]["curto"].upper()) if c["corpo"] else "",
               _gesto(spec)[:90], c["t2"][:90], spec["idade"], spec["etnia"],
               spec["hook"]["v"], spec["mecanismo"]["v"],
               spec["prova"]["v"] if spec.get("prova") else "—",
               spec["cta"]["v"]))


EIXOS_UI = [
    ("cena", "A CENA (o vídeo da fonte)", "CENAS", "curto"),
    ("regiao", "ONDE ELE PASSA", "REGIOES", "curto"),
    ("hook", "O HOOK", "HOOKS", "v"),
]
EIXOS_TRAVAVEIS = ["cena", "regiao", "hook"]
DROPDOWNS_UI = [("cena", "A CENA", "CENAS", "curto")]
IGNORA_PAINEL = ("hook", "regiao")


# ===========================================================================
# AUTOTESTE
# ===========================================================================
def _autoteste(n=400, seed=20260816):
    rng = random.Random(seed)
    led, erros = {}, collections.Counter()
    vistos = collections.Counter()
    falas = {1: set(), 2: set()}
    pal = {1: [], 2: []}
    sem_origem = corpo = com_prova = 0
    for _ in range(n):
        sp = sortear("joe", rng, led)
        _anotar(led, sp)
        bl = montar(sp)
        for nivel, txt in lint(sp, bl):
            if nivel == "ERRO":
                erros[txt.split(":")[0]] += 1
        vistos[sp["cena"]["id"]] += 1
        corpo += bool(sp["cena"]["corpo"])
        com_prova += bool(sp.get("prova"))
        for i in (1, 2):
            falas[i].add(sp["falas"][i - 1])
            pal[i].append(_palavras(sp["falas"][i - 1]))
        beats = [sp["hook"], sp["mecanismo"], sp["cta"]]
        if sp.get("prova"):
            beats.append(sp["prova"])
        junto = " ".join(sp["falas"])
        for b in beats:
            if b["txt"].replace("{idade}", str(sp["idade"])) not in junto:
                sem_origem += 1

    print("%s — %d sorteios (seed %d)" % (APP, n, seed))
    print("  cenas da fonte: %d de %d alcancadas · min %dx · max %dx"
          % (len(vistos), len(CENAS), min(vistos.values()), max(vistos.values())))
    print("  a POMADA NO CORPO aparece em %d%% dos videos (%d das %d cenas "
          "tem o beat)" % (100 * corpo // n,
                           sum(1 for c in CENAS if c["corpo"]), len(CENAS)))
    for i in (1, 2):
        print("  cena %d: %3d falas distintas · palavras %d/%d/%d"
              % (i, len(falas[i]), min(pal[i]), sum(pal[i]) // len(pal[i]),
                 max(pal[i])))
    print("  o beat CONCRETO entra em %d%% dos videos" % (100 * com_prova // n))
    print("  beats sem origem na fonte: %d  %s"
          % (sem_origem, "(toda fala e' verbatim)" if not sem_origem
             else "<-- FALHA"))
    print("  linter: %d ERRO" % sum(erros.values()))
    for k, v in erros.most_common(8):
        print("     %4dx %s" % (v, k))
    return sum(erros.values()) + sem_origem


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
