#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
flagrante_lucas.py — randomizador + gerador + linter do AGENTE FLAGRANTE.

Nasceu da sessao 2026-07-30, depois de 4 IMG 01 barradas seguidas e de uma
string travada (D1) corrompida por compressao manual. Tres licoes viraram
codigo:

  1. String travada NUNCA e' redigitada. Mora aqui como constante.
  2. Regra mecanica (cota do orgao, teto de fala, token banido) e' regex,
     nao julgamento.
  3. O modelo tem mode-collapse: solto, gravita pro mesmo prototipo. Os eixos
     sao SORTEADOS e a linha sorteada e' EXECUTADA, nunca escolhida (P1).

Uso:
    python funil-organico/flagrante_lucas.py --pagina ray --n 1
    python funil-organico/flagrante_lucas.py --pagina marcus --n 3 --seed 42
    python funil-organico/flagrante_lucas.py --pagina joe --n 1 --dry-run
    python funil-organico/flagrante_lucas.py --stats
    python funil-organico/flagrante_lucas.py --spec spec.json   # spec manual

Doutrina: AGENTE_ED_FLAGRANTE_V1.md · funil-organico/prop-metaforas.md
"""

import argparse
import json
import os
import random
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(AQUI, ".flagrante-ledger.json")

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

TITULO = "AGENTE FLAGRANTE"
SLUG = "flagrante"
SUBTITULO = "humilhação pública · gerador offline de prompts Veo"

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

ETNIA = {
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
]

VITIMAS = [
    {"idade": 63, "marca": "bald man with a thick gray mustache and black-framed glasses"},
    {"idade": 62, "marca": "bald man with a red mustache and wire-rimmed glasses"},
    {"idade": 65, "marca": "bald man with a white mustache and thick square glasses"},
    {"idade": 64, "marca": "bald man with a gray fringe above his ears, a bushy mustache and glasses"},
    {"idade": 61, "marca": "bald man with a short gray mustache and round wire glasses"},
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
]

# ---------------------------------------------------------------------------
# POOLS DE COPY — o molde e' sorteado, a frase cha' vence sempre (arsenal)
# ---------------------------------------------------------------------------

NUCLEO = ["Johnson", "soldier", "pecker", "manhood", "wiener", "tool", "old boy"]

HOOKS = [
    "Everyone at {evento} had already heard the gossip that his {o} doesn't work anymore. His hangs just like this.",
    "The whole {evento} had heard the gossip that his {o} quit on him. His hangs just like this.",
    "Every man at {evento} had heard the gossip that his {o} can't stand up anymore. His hangs like this.",
    "Word got around {evento} that his {o} doesn't work anymore. His hangs just like this.",
]

QUEM_CONTOU = [
    "his own brother", "his brother-in-law", "a guy from the shop",
    "his fishing buddy", "his business partner", "the neighbor",
    "an old army friend", "his own son-in-law",
]

DESCOBERTAS = [
    "That's when {quem} pulled him aside and gave him the gelatin trick. It's not age, brother, the blood flow to your {o} got choked off.",
    "That's when {quem} handed him the gelatin trick. It's not age, brother, your {o} got its blood flow choked off.",
    "That's when {quem} gave him the gelatin trick. It's not age. Right here, the blood flow to your {o} got choked off.",
]

RITUAIS = [
    "That same night he stirred it into a glass and drank it. Stir it, drink it, give your {o} one week.",
    "That same night he stirred it into a glass and drank it. Do it tonight, before your {o} quits for good.",
    "That same night he mixed it into a glass and drank it. Stir it, drink it, and watch your {o} wake up.",
]

BRAGGING = ["telling that story", "bragging", "spreading the gossip herself"]

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
]

GATES = [
    "Follow me first, brother.",
    "Follow me first or I can't find your comment.",
    "Hit follow first, or Facebook won't deliver it.",
]

CTAS = [
    "Comment GELATIN and I'll send you the only one I trust tonight. {gate}",
    "Comment GELATIN and I'll send you that exact one today. {gate}",
]

# ---------------------------------------------------------------------------
# LINTER
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

TETO_FALA = {1: 20, 2: 30, 3: 22, 4: 32, 5: 24}


def _palavras(txt):
    return len(re.findall(r"[A-Za-z']+", txt))


def lint(spec, blocos):
    achados = []
    falas = spec["falas"]

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
        rep = sorted({u for u in usados if usados.count(u) > 1})
        achados.append(("AVISO", "substantivo repetido no video: %s "
                                 "(cota nao e' licenca pra bordao)" % rep))

    total = 0
    for i, fala in enumerate(falas, 1):
        n = _palavras(fala)
        total += n
        if n > TETO_FALA[i]:
            achados.append(("AVISO", "cena %d com %d palavras (teto %d) — cortar "
                                     "UMA frase, nao reescrever menor"
                            % (i, n, TETO_FALA[i])))
    if total > 115:
        achados.append(("AVISO", "video com %d palavras (alvo ~90-105)" % total))

    corpo = " ".join(falas).lower()
    if "gelatin trick" not in corpo:
        achados.append(("ERRO", "expressao literal 'gelatin trick' ausente"))
    if "gelatin" not in falas[4].lower():
        achados.append(("ERRO", "CTA da cena 5 sem a keyword GELATIN"))
    for tok, motivo in BANIDOS_CTA.items():
        if re.search(r"\b%s\b" % tok, falas[4]):
            achados.append(("ERRO", "CTA usa '%s' — %s" % (tok, motivo)))

    for nome, txt in blocos.items():
        baixo = txt.lower()
        tabela = BANIDOS_TAKE if nome.startswith("TAKE") else BANIDOS_IMAGE
        for tok, motivo in tabela.items():
            if re.search(r"\b%s\b" % tok, baixo):
                achados.append(("ERRO", "%s contem '%s' — %s" % (nome, tok, motivo)))
        for tok, motivo in BANIDOS_GLOBAL.items():
            if tok in baixo:
                achados.append(("ERRO", "%s contem '%s' — %s" % (nome, tok, motivo)))

    for nome in ("TAKE 01/05", "TAKE 04/05"):
        if "motionless" not in blocos[nome].lower():
            achados.append(("ERRO", "%s sem declaracao de imobilidade do prop" % nome))

    if D1_IMAGE not in blocos["IMAGE 02/05"]:
        achados.append(("ERRO", "IMAGE 02 sem a string travada do D1 (F16)"))
    if D1_TAKE not in blocos["TAKE 02/05"]:
        achados.append(("ERRO", "TAKE 02 sem a string travada do D1 (F16)"))

    return achados


# ---------------------------------------------------------------------------
# INTERFACE (consumido por ui_agente.py)
# ---------------------------------------------------------------------------

EIXOS_UI = [
    ("ocasiao", "OCASIÃO", "OCASIOES", "id"),
    ("prop", "PROP", "PROPS", "id"),
    ("ambiente", "AMBIENTE", "AMBIENTES", "id"),
    ("ref", "NARRADOR", "REFS", "marca"),
    ("vitima", "VÍTIMA", "VITIMAS", "marca"),
    ("mulher", "MULHER", "MULHERES", "hook"),
]

CENAS_UI = ["1 · RUÍNA", "2 · DESCOBERTA", "3 · RITUAL", "4 · REDENÇÃO", "5 · CTA"]

# ja' com a preposicao contraida — abrem a frase do resumo
PT_OCASIAO = {
    "casamento": "Num casamento", "confraternizacao": "Na confraternização da firma",
    "pescaria_firma": "Na pescaria da firma", "reuniao_firma": "Na reunião da firma",
    "churrasco": "Num churrasco de família", "jantar_amigos": "Num jantar de amigos",
    "aniversario": "Nas bodas de casamento", "clube_golfe": "No almoço do clube de golfe",
}
PT_PROP = {
    "geoduck": "um geoduck", "banana": "uma banana", "okra": "um quiabo",
    "pepino": "um pepino", "aspargo": "um aspargo", "daikon": "um nabo daikon",
    "linguica": "uma linguiça",
}
PT_AMBIENTE = {
    "cozinha": "na cozinha", "cozinha_aberta": "na cozinha com ilha",
    "churrasqueira": "na área de churrasco", "varanda": "na varanda coberta",
    "garagem": "na garagem oficina", "copa": "na copa",
}


def resumo_pt(spec):
    et = "branca" if "white" in ETNIA[spec["pagina"]] else "negra"
    return ("%s, o colega segura %s murcho no próprio colo enquanto o narrador "
            "aponta e a mesa ri. As cenas 2 a 5 rodam %s. Elenco de pele %s."
            % (PT_OCASIAO.get(spec["ocasiao"]["id"], "Num evento"),
               PT_PROP.get(spec["prop"]["id"], "o prop"),
               PT_AMBIENTE.get(spec["ambiente"]["id"], "no set interno"), et))


def _recopiar_ocasiao(spec, rng):
    """A ocasiao alimenta o hook e o eco da cena 4 — trocar exige reescrever."""
    oc = spec["ocasiao"]
    o0 = next((n for n in NUCLEO if n.lower() in spec["falas"][0].lower()), "Johnson")
    o3 = next((n for n in NUCLEO if n.lower() in spec["falas"][3].lower()), "manhood")
    spec["falas"][0] = rng.choice(HOOKS).format(evento=oc["plateia_evento"], o=o0)
    spec["falas"][3] = rng.choice(REDENCOES).format(
        eco=oc["eco"], brag=rng.choice(BRAGGING), o=o3,
        barreira=rng.choice(BARREIRAS))


EIXOS_QUE_MEXEM_NA_COPY = {"ocasiao": _recopiar_ocasiao}


# ---------------------------------------------------------------------------
# SORTEIO
# ---------------------------------------------------------------------------

def _carregar_ledger():
    if os.path.exists(LEDGER):
        with open(LEDGER, encoding="utf-8-sig") as f:
            return json.load(f)
    return {}


def _sortear_evitando(rng, pool, recentes, chave="id"):
    """Sorteia evitando os valores usados recentemente naquela pagina."""
    livres = [x for x in pool if x.get(chave, x) not in recentes]
    return rng.choice(livres if livres else pool)


def sortear(pagina, rng, ledger):
    hist = ledger.get(pagina, {})
    # evita repetir o valor dos ultimos N videos da mesma pagina
    ev = lambda eixo, n: hist.get(eixo, [])[-n:]

    oc = _sortear_evitando(rng, OCASIOES, ev("ocasiao", 3))
    prop = _sortear_evitando(rng, PROPS, ev("prop", 3))
    amb = _sortear_evitando(rng, AMBIENTES, ev("ambiente", 2))
    ref = rng.choice(REFS)
    vit = rng.choice(VITIMAS)
    mul = rng.choice(MULHERES)

    # 4 substantivos distintos do nucleo, um por cena 1-4 (cota 75%)
    orgaos = rng.sample(NUCLEO, 4)

    falas = [
        rng.choice(HOOKS).format(evento=oc["plateia_evento"], o=orgaos[0]),
        rng.choice(DESCOBERTAS).format(quem=rng.choice(QUEM_CONTOU), o=orgaos[1]),
        rng.choice(RITUAIS).format(o=orgaos[2]),
        rng.choice(REDENCOES).format(eco=oc["eco"], brag=rng.choice(BRAGGING),
                                     o=orgaos[3], barreira=rng.choice(BARREIRAS)),
        rng.choice(CTAS).format(gate=rng.choice(GATES)),
    ]

    return {
        "pagina": pagina, "ocasiao": oc, "prop": prop, "ambiente": amb,
        "ref": ref, "vitima": vit, "mulher": mul, "falas": falas,
    }


def _gravar_ledger(ledger, spec):
    p = ledger.setdefault(spec["pagina"], {})
    for eixo, val in (("ocasiao", spec["ocasiao"]["id"]),
                      ("prop", spec["prop"]["id"]),
                      ("ambiente", spec["ambiente"]["id"])):
        p.setdefault(eixo, []).append(val)
        p[eixo] = p[eixo][-12:]
    with open(LEDGER, "w", encoding="utf-8") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)


# ---------------------------------------------------------------------------
# GERADOR
# ---------------------------------------------------------------------------

def montar(spec):
    et = ETNIA[spec["pagina"]]
    ref, vit, mul = spec["ref"], spec["vitima"], spec["mulher"]
    prop, oc, amb = spec["prop"], spec["ocasiao"], spec["ambiente"]
    falas = spec["falas"]

    ref_desc = "a %d-year-old %s man with %s" % (ref["idade"], et, ref["marca"])
    vit_desc = "A %d-year-old %s %s" % (vit["idade"], et, vit["marca"])
    neg = NEGACAO_AVE if prop["marisco"] else ""
    luz = amb["luz"]

    b = {}

    b["BLOCO 0 (REF)"] = (
        "Photo of a real person, a %d-year-old %s man, chest up, facing camera, "
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
           oc["plateia"], falas[0], oc["audio"])
    )

    b["TAKE 02/05"] = (
        "TAKE 02/05: Animate the image exactly. Handheld iPhone, slight sway, "
        "no cuts. %s He is alone in frame, speaking with conviction.\n"
        "Dialogue: \"%s\"\nAudio: quiet room tone. No music." % (D1_TAKE, falas[1])
    )

    b["TAKE 03/05"] = (
        "TAKE 03/05: Animate the image exactly. Handheld iPhone, slight sway, "
        "no cuts. Hands finish pouring the sachet, stir the glass in slow "
        "circles. No face enters frame.\n"
        "Dialogue: \"%s\"\nAudio: spoon clinking glass, quiet room tone. No music."
        % falas[2]
    )

    b["TAKE 04/05"] = (
        "TAKE 04/05: Animate the image exactly. Handheld iPhone, slight sway, "
        "no cuts. The man laughs silently, head tipping back. The woman laughs, "
        "tightens her arm around him; her other hand stays exactly where it is, "
        "holding it motionless the entire shot. Neither changes position. A "
        "man's voice speaks over the scene; the couple stays silent.\n"
        "Dialogue: \"%s\"\nAudio: quiet room tone, soft laughter. No music." % falas[3]
    )

    b["TAKE 05/05"] = (
        "TAKE 05/05: Animate the image exactly. Handheld iPhone, slight sway, "
        "no cuts. He looks at camera, calm, points his finger, speaks evenly.\n"
        "Dialogue: \"%s\"\nAudio: quiet room tone. No music." % falas[4]
    )

    return b


def imprimir(spec, blocos, achados):
    oc, prop, amb = spec["ocasiao"], spec["prop"], spec["ambiente"]
    print("=" * 72)
    print("SPEC SORTEADA — pagina %s | ocasiao %s (%s) | prop %s | set %s"
          % (spec["pagina"], oc["id"], oc["selo"], prop["id"], amb["id"]))
    print("=" * 72)
    print(blocos["BLOCO 0 (REF)"] + "\n")
    for k in sorted(k for k in blocos if k.startswith("IMAGE")):
        print("-" * 72)
        print(blocos[k] + "\n")
    for k in sorted(k for k in blocos if k.startswith("TAKE")):
        print("-" * 72)
        print(blocos[k] + "\n")
    print("=" * 72)
    if not achados:
        print("LINTER: OK — nenhuma violacao mecanica.")
    else:
        for nivel, msg in achados:
            print("[%s] %s" % (nivel, msg))
        n_erros = sum(1 for a in achados if a[0] == "ERRO")
        print("%d erro(s), %d aviso(s)." % (n_erros, len(achados) - n_erros))


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
            linha = ", ".join("%s:%d" % kv for kv in sorted(cont.items()))
            print("  %-10s %s" % (eixo, linha))


def main():
    ap = argparse.ArgumentParser(description="Randomizador do agente FLAGRANTE")
    ap.add_argument("--pagina", choices=sorted(ETNIA))
    ap.add_argument("--n", type=int, default=1)
    ap.add_argument("--seed", type=int, help="reproduzivel")
    ap.add_argument("--dry-run", action="store_true", help="nao grava ledger")
    ap.add_argument("--stats", action="store_true", help="uso dos pools")
    ap.add_argument("--spec", help="spec JSON manual (ignora o sorteio)")
    ap.add_argument("--lint", action="store_true", help="so' o linter")
    a = ap.parse_args()

    if a.stats:
        stats()
        return 0

    if a.spec:
        with open(a.spec, encoding="utf-8-sig") as f:
            spec = json.load(f)
        blocos = montar(spec)
        achados = lint(spec, blocos)
        if not a.lint:
            imprimir(spec, blocos, achados)
        return 1 if any(x[0] == "ERRO" for x in achados) else 0

    if not a.pagina:
        ap.error("informe --pagina <joe|ray|matt|marcus|chuck> (ou --spec/--stats)")

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
