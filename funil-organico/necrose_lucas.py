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
MODELO_PODRE = (
    "On the left, a free-standing three-dimensional anatomy teaching model of "
    "the male bladder and the tube below it, %s. This one is the old one: the "
    "rounded mass at the top is dark walnut-brown, shrivelled and knotted, its "
    "surface dull, dry and cracked, covered in irregular lumps and deep creases "
    "like a dried root. Two thin cords twist away from it, withered and "
    "darkened like dry twigs. The tube below hangs crooked and collapsed, "
    "pinched in at several points, ending in a small shrunken darkened bulb. "
    "Nothing on it reflects light." % SUPORTE
)

# ⚠️ "identical" na abertura e' OBRIGATORIO: sem ele o Veo desenha dois objetos
# de especies diferentes e a comparacao — que e' o video inteiro — some.
MODELO_SAO = (
    "On the right, an identical free-standing three-dimensional anatomy "
    "teaching model of the male bladder and the tube below it, %s. This one is "
    "the new one: the rounded mass at the top is pale salmon pink, full and "
    "smooth, its surface glossy and catching the light. Two clean straight "
    "cream-coloured tubes run from it. The tube below hangs thick, straight "
    "and even, its inner channel shown in darker pink, ending in a full "
    "rounded pink tip." % SUPORTE
)

# versoes curtas, para as cenas em que ele ergue UM modelo so'
PODRE_NA_MAO = (
    "the old model — the one whose rounded top is dark walnut-brown, shrivelled "
    "and knotted, dull and cracked, whose tube hangs crooked and pinched"
)
SAO_NA_MAO = (
    "the new model — the one whose rounded top is pale salmon pink, full and "
    "smooth, glossy and catching the light, whose tube hangs thick, straight "
    "and even, ending in a full rounded pink tip"
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

# NE5 — a alta montanha e' o segundo scroll-stop: o cenario sozinho ja' destoa
# de tudo que o avatar ve no feed do nicho (cozinha, consultorio, quintal).
MONTANHAS = [
    {"id": "cabana_pedra", "selo": "V",
     "set": "a rocky alpine mountaintop, snow-capped peaks filling the "
            "background, a small stone cabin with a chimney at frame-left, "
            "lichen-covered rock in the foreground, clear blue sky",
     "curto": "the same mountaintop",
     "luz": "Clear high-altitude daylight, cool and bright, soft shadows.",
     "audio": "high wind over rock, a distant bird"},
    {"id": "lago_glacial", "selo": "N",
     "set": "a rocky ledge above a glacier lake, snow-capped peaks across the "
            "water, scattered boulders, no buildings anywhere",
     "curto": "the same ledge above the lake",
     "luz": "Clear high-altitude daylight, cool and bright, soft shadows.",
     "audio": "high wind, water lapping far below"},
    {"id": "linha_das_arvores", "selo": "N",
     "set": "a high clearing at the treeline, dark pine forest behind him and "
            "bare snow peaks rising above it, moss and lichen on the rocks",
     "curto": "the same clearing",
     "luz": "Cool overcast mountain daylight, flat and even.",
     "audio": "wind through pines, a distant bird"},
    {"id": "campo_de_pedras", "selo": "N",
     "set": "a windswept boulder field high on a mountain, a low stone shelter "
            "behind him, grey sky over the peaks",
     "curto": "the same boulder field",
     "luz": "Flat grey mountain daylight, no hard shadows.",
     "audio": "hard wind over stone"},
]

# NE4 — a ESPECIE e' travada (lobo). So' a pelagem varia.
LOBOS = [
    {"id": "cinza", "desc": "a full-grown grey wolf"},
    {"id": "preto", "desc": "a full-grown black wolf"},
    {"id": "branco", "desc": "a full-grown white arctic wolf"},
]

# NE3 — autoridade SELVAGEM, nao clinica. Musculatura por GRUPO NOMEADO
# ("muscular" sozinho nao renderiza) + marca facial num rosto saudavel.
REFS = [
    {"idade": 62,
     "corpo": "a lean hard-muscled build with a broad chest and thick arms",
     "cabeca": "long gray hair under a wide-brimmed brown leather hat with a "
               "braided cord band, a thick gray beard reaching mid-chest",
     "marca": "unusually pale ice-blue eyes and a small notch missing from the "
              "top of his left ear"},
    {"idade": 65,
     "corpo": "a powerfully built muscular frame with a barrel chest and thick "
              "forearms",
     "cabeca": "gray hair tied back under a battered wide-brimmed felt hat, a "
               "full white beard reaching mid-chest",
     "marca": "a clean pale scar running through his right eyebrow"},
    {"idade": 58,
     "corpo": "a tall broad-shouldered muscular build with a wide back and "
              "strong neck",
     "cabeca": "shoulder-length salt-and-pepper hair under a dark brown leather "
               "hat with a braided cord band, a thick salt-and-pepper beard",
     "marca": "a deep vertical cleft in his chin and heavy weather lines around "
              "the eyes"},
    {"idade": 68,
     "corpo": "a lean hard-muscled build with visible definition in the chest, "
              "shoulders and arms",
     "cabeca": "long white hair under a wide-brimmed oiled canvas hat, a long "
               "white beard reaching the middle of his chest",
     "marca": "a prominent dark mole high on his right cheekbone"},
]

# NE6 — receita de COZINHA, preparada na tela. ⚠️ topica ou de preparo, nunca
# dose medica: sem miligramas, sem "duas vezes ao dia", sem alegacao de cura.
RECEITAS_PROP = [
    {"id": "curcuma", "selo": "V",
     "mesa": "a wooden spoon heaped with bright yellow turmeric powder, a "
             "second wooden spoon of black peppercorns, a glass jar of honey, "
             "a halved lemon, fresh ginger root and a wooden bowl of turmeric",
     "acao": "he tips the turmeric off the wooden spoon into a glass of water, "
             "sets that spoon down, tips in the peppercorns, then squeezes the "
             "halved lemon over the glass",
     "fala": "turmeric, a pinch of black pepper, honey and fresh lemon"},
    {"id": "gengibre", "selo": "N",
     "mesa": "a wooden board of sliced fresh ginger, a glass jar of honey, a "
             "halved lemon, a small bowl of cayenne and a wooden mug",
     "acao": "he drops the ginger slices into a wooden mug, spoons honey over "
             "them, taps in the cayenne and squeezes the halved lemon on top",
     "fala": "fresh ginger, raw honey, a pinch of cayenne and lemon"},
    {"id": "beterraba", "selo": "N",
     "mesa": "a wooden board of halved beets, a jar of honey, a stick of "
             "cinnamon, a wooden bowl and a glass",
     "acao": "he presses the beet halves over the glass, stirs in a spoon of "
             "honey and snaps the cinnamon stick into it",
     "fala": "pressed beet, a spoon of honey and a stick of cinnamon"},
    {"id": "alho", "selo": "N",
     "mesa": "a wooden board of crushed garlic cloves, a bottle of apple cider "
             "vinegar, a jar of raw honey and a wooden mug",
     "acao": "he scrapes the crushed garlic into the mug, pours the vinegar "
             "over it and stirs in a heavy spoon of honey",
     "fala": "crushed garlic, apple cider vinegar and raw honey"},
]

MESAS = [
    {"id": "mesa_madeira", "desc": "a weathered wooden table outdoors"},
    {"id": "laje_pedra", "desc": "a flat slab of rock used as a table"},
    {"id": "tronco", "desc": "a split log bench outside the cabin door"},
]

# ---------------------------------------------------------------------------
# POOLS DE COPY
# ---------------------------------------------------------------------------

NUCLEO = ["Johnson", "soldier", "pecker", "manhood", "wiener", "tool", "old boy"]

# NE7 — o hook e' "from this to this", com o gesto sincronizado na batida das
# palavras. A fonte abre nomeando o orgao no primeiro segundo.
HOOKS = [
    "If you want your {o} to go from this to this in one month, watch close.",
    "This is your {o} today. This is your {o} in one month. Watch close, brother.",
    "Your {o} looks like this right now. It can look like this by next month.",
    "One of these is your {o}. The other one is your {o} in thirty days.",
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
    "In a glass, stir {ing}. Drink it tonight, before your {o} quits for good.",
    "Grab a glass and stir {ing}. Do it tonight and give your {o} one week.",
    "In a glass: {ing}. Stir it, drink it, and let your {o} wake back up.",
    "Stir {ing} into a glass of water. One minute. Your {o} took years to quit.",
]

# NE — cena 4: MUS. "gelatin trick" literal e' obrigatorio, com o modelo SAO
# erguido contra o ceu. O podre saiu de cena: a ausencia e' o payoff.
PROVAS = [
    "But that recipe alone won't get you here. The gelatin trick is what rebuilt my {o}. {barreira}",
    "The recipe opens the door. The gelatin trick is what walked my {o} through it. {barreira}",
    "You need the other half, brother. The gelatin trick is what took my {o} from that one to this one. {barreira}",
    "Half a recipe gets you nowhere. The gelatin trick is what gave my {o} this back. {barreira}",
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
    for nome in ("TAKE 02/05", "TAKE 04/05"):
        if IMOBILIDADE_UM not in blocos[nome]:
            achados.append(("ERRO", "%s sem a imobilidade do modelo unico (NE8)" % nome))

    # NE4 — o lobo nas cenas 1 e 4
    for nome in ("IMAGE 01/05", "IMAGE 04/05"):
        if "wolf" not in blocos[nome].lower():
            achados.append(("ERRO", "NE4: %s sem o lobo" % nome))

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
    mont = _evitando(rng, MONTANHAS, hist.get("montanha", [])[-2:])
    lobo = _evitando(rng, LOBOS, hist.get("lobo", [])[-1:])
    rec = _evitando(rng, RECEITAS_PROP, hist.get("receita", [])[-2:])
    mesa = _evitando(rng, MESAS, hist.get("mesa", [])[-1:])
    ref = rng.choice(REFS)

    orgaos = rng.sample(NUCLEO, 4)
    falas = [
        rng.choice(HOOKS).format(o=orgaos[0]),
        rng.choice(CAUSAS).format(o=orgaos[1]),
        rng.choice(RECEITAS_FALA).format(o=orgaos[2], ing=rec["fala"]),
        rng.choice(PROVAS).format(o=orgaos[3], barreira=rng.choice(BARREIRAS)),
        rng.choice(CTAS).format(pacing=rng.choice(PACING), gate=rng.choice(GATES)),
    ]
    return {"pagina": pagina, "montanha": mont, "lobo": lobo, "receita": rec,
            "mesa": mesa, "ref": ref, "falas": falas}


def _gravar_ledger(ledger, spec):
    p = ledger.setdefault(spec["pagina"], {})
    for eixo, val in (("montanha", spec["montanha"]["id"]),
                      ("lobo", spec["lobo"]["id"]),
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
    ref, mont, rec, mesa = spec["ref"], spec["montanha"], spec["receita"], spec["mesa"]
    lobo = LOBO % spec["lobo"]["desc"]
    falas = spec["falas"]

    quem = ("a %d-year-old %s man, bare-chested, %s, %s, %s"
            % (ref["idade"], et, ref["corpo"], ref["cabeca"], ref["marca"]))
    mesmo = ("The same %d-year-old %s man, same hat, same beard, same %s, "
             "bare-chested." % (ref["idade"], et, ref["marca"]))

    b = {}

    b["BLOCO 0 (REF)"] = (
        "Photo of a real person, a %d-year-old %s man, chest up, facing the "
        "camera directly, neutral steady expression. Bare-chested, %s, tanned "
        "weathered skin. %s. %s. An ordinary everyday relatable person with a "
        "plain unremarkable face, not a celebrity, not a model, not an actor, "
        "not resembling any famous person. Plain neutral gray background, soft "
        "even frontal light. No subtitles, no captions, no burned-in text, no "
        "watermark."
        % (ref["idade"], et, ref["corpo"],
           ref["cabeca"][0].upper() + ref["cabeca"][1:],
           ref["marca"][0].upper() + ref["marca"][1:])
    )

    b["IMAGE 01/05"] = (
        "IMAGE 01/05: Medium shot on %s. Seated behind a ledge of rock is %s. "
        "He looks straight into the lens, mouth open mid-word.\n\n"
        "Standing on the rock in front of him are two anatomy models, side by "
        "side at chest height.\n\n%s\n\n%s\n\n"
        "Behind him on his right stands %s. He is the only person in the frame. "
        "%s %s %s"
        % (mont["set"], quem, MODELO_PODRE, MODELO_SAO, lobo, ANTICELEB,
           mont["luz"], CAUDA)
    )

    b["IMAGE 02/05"] = (
        "IMAGE 02/05: Medium close-up, %s, same background. %s He holds up in "
        "his right hand %s, lifted to shoulder height and turned toward the "
        "camera. His left index finger points at it. His expression is hard and "
        "serious, brow furrowed, mouth open mid-word. The second model is out of "
        "frame. He is the only person in the frame. %s %s %s"
        % (mont["curto"], mesmo, PODRE_NA_MAO, ANTICELEB, mont["luz"], CAUDA)
    )

    b["IMAGE 03/05"] = (
        "IMAGE 03/05: Medium shot at %s, %s behind it, same light. %s He stands "
        "behind the table mid-action, speaking to the camera. On the table: %s. "
        "He is the only person in the frame. %s %s %s"
        % (mesa["desc"], mont["curto"], mesmo, rec["mesa"], ANTICELEB,
           mont["luz"], CAUDA)
    )

    b["IMAGE 04/05"] = (
        "IMAGE 04/05: Low-angle medium shot on %s, open sky behind him. %s He "
        "stands tall and holds one anatomy model up high in his right hand, "
        "raised above his shoulder against the sky — %s, still mounted on its "
        "slim chrome stand. He is grinning, chin lifted. The old model is "
        "nowhere in the frame. Behind him on his right stands the same %s. He "
        "is the only person in the frame. %s %s %s"
        % (mont["curto"], mesmo, SAO_NA_MAO, spec["lobo"]["desc"].replace("a ", "", 1),
           ANTICELEB, mont["luz"], CAUDA)
    )

    b["IMAGE 05/05"] = (
        "IMAGE 05/05: Close-up on %s, same light. %s He is the only person in "
        "the frame. He looks straight into the lens, calm and confident, one "
        "corner of his mouth raised in a half-smile. His right index finger "
        "points directly at the camera. %s %s %s"
        % (mont["curto"], mesmo, ANTICELEB, mont["luz"], CAUDA)
    )

    b["TAKE 01/05"] = (
        "TAKE 01/05: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway, no cuts. The %d-year-old man speaks straight "
        "into the lens with force. On the word \"this\" he points at the left "
        "model, and on the second \"this\" he points at the right model — the "
        "two gestures land on the two words. %s Behind him the wolf shifts its "
        "weight once and keeps looking at the camera. He is the only person in "
        "the shot and no one else enters frame.\nDialogue: \"%s\"\n"
        "Audio: %s. No music."
        % (ref["idade"], IMOBILIDADE_PAR, sonorizar(falas[0]), mont["audio"])
    )

    b["TAKE 02/05"] = (
        "TAKE 02/05: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway, no cuts. The %d-year-old man holds the model "
        "steady at shoulder height and taps it twice with his left index finger "
        "as he speaks. %s He speaks with conviction and slows down on the last "
        "sentence. He is the only person in the shot.\nDialogue: \"%s\"\n"
        "Audio: %s. No music."
        % (ref["idade"], IMOBILIDADE_UM, sonorizar(falas[1]), mont["audio"])
    )

    b["TAKE 03/05"] = (
        "TAKE 03/05: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway, no cuts. His hands work while he talks: %s. "
        "His eyes stay on the lens the whole time. He is the only person in the "
        "shot.\nDialogue: \"%s\"\nAudio: %s, a spoon against glass. No music."
        % (rec["acao"], sonorizar(falas[2]), mont["audio"])
    )

    b["TAKE 04/05"] = (
        "TAKE 04/05: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway, no cuts. The %d-year-old man raises the model "
        "a little higher against the sky and grins wider, holding it steady "
        "above his shoulder for the whole take. %s Behind him the wolf turns its "
        "head once and looks back at the camera. He is the only person in the "
        "shot.\nDialogue: \"%s\"\nAudio: %s. No music."
        % (ref["idade"], IMOBILIDADE_UM, sonorizar(falas[3]), mont["audio"])
    )

    b["TAKE 05/05"] = (
        "TAKE 05/05: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway, no cuts. The %d-year-old man looks into the "
        "lens, calm and confident, and points his right index finger at the "
        "camera. He speaks directly and evenly, no rush.\nDialogue: \"%s\"\n"
        "Audio: %s. No music."
        % (ref["idade"], sonorizar(falas[4]), mont["audio"])
    )

    return b


# ---------------------------------------------------------------------------
# INTERFACE (consumido por ui_agente.py)
# ---------------------------------------------------------------------------

EIXOS_UI = [
    ("montanha", "MONTANHA", "MONTANHAS", "id"),
    ("lobo", "LOBO", "LOBOS", "id"),
    ("receita", "RECEITA", "RECEITAS_PROP", "id"),
    ("mesa", "MESA", "MESAS", "id"),
    ("ref", "MONTANHÊS", "REFS", "marca"),
]

CENAS_UI = ["1 · A COMPARAÇÃO", "2 · A CAUSA", "3 · A RECEITA",
            "4 · MECANISMO + PROVA", "5 · CTA"]

PT_MONT = {"cabana_pedra": "No topo da montanha, com a cabana de pedra",
           "lago_glacial": "Na saliência sobre o lago glacial",
           "linha_das_arvores": "Na clareira na linha das árvores",
           "campo_de_pedras": "No campo de pedras varrido pelo vento"}
PT_LOBO = {"cinza": "um lobo cinza", "preto": "um lobo preto",
           "branco": "um lobo branco do ártico"}
PT_REC = {"curcuma": "cúrcuma com pimenta, mel e limão",
          "gengibre": "gengibre com mel, caiena e limão",
          "beterraba": "beterraba com mel e canela",
          "alho": "alho com vinagre de maçã e mel"}


def resumo_pt(spec):
    et = "branca" if "white" in ETNIA[spec["pagina"]] else "negra"
    return ("%s, o montanhês de %d anos sem camisa mostra os dois órgãos lado a "
            "lado — o apodrecido e o são — com %s atrás dele. Na cena 3 ele "
            "prepara %s, e na 4 ergue só o são contra o céu. Elenco de pele %s."
            % (PT_MONT.get(spec["montanha"]["id"], "Na montanha"),
               spec["ref"]["idade"], PT_LOBO.get(spec["lobo"]["id"], "um lobo"),
               PT_REC.get(spec["receita"]["id"], "a receita"), et))


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
    print("SPEC SORTEADA — pagina %s | montanha %s (%s) | lobo %s | receita %s | mesa %s"
          % (spec["pagina"], spec["montanha"]["id"], spec["montanha"]["selo"],
             spec["lobo"]["id"], spec["receita"]["id"], spec["mesa"]["id"]))
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
