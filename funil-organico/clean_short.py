#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
clean_short.py — randomizador + gerador + linter do AGENTE CLEAN.

A aponta apontada: profissional de saude sozinha(o) de scrub, uma aponta de
itens comestiveis na bancada, e o dedo ligando cada item a um beneficio.
ZERO prop falico, ZERO anatomia, ZERO vitima.

Fonte: Valentina Health & Wellness, 2 reels (13,3k e 7,1k comentarios).
Doutrina: AGENTE_ED_CLEAN_V1.md · concorrentes/clean-mapa-visual.md

⭐ SHORT NATIVO — 3 cenas de 8s. Nao deriva de motor longo e nao tera versao
longa (CL16). Duas FAMILIAS de cena, uma copy so'.

⭐ SEXO E' TRAVA, NAO SORTEIO (ordem do operador, 2026-08-02): o painel deixa
pre-selecionar homem/mulher e a escolha nao e' re-sorteada.

Uso:
    python funil-organico/clean_short.py --pagina chuck --n 1
    python funil-organico/clean_short.py --pagina ray --n 3 --seed 42 --dry-run
"""

import argparse
import json
import os
import random
import re
import sys

from nucleo_sonoro import sonorizar

AQUI = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(AQUI, ".clean-short-ledger.json")

TITULO = "AGENTE CLEAN"
SLUG = "clean-short"
SUBTITULO = "a aponta apontada, em 3 cenas · gerador offline de prompts Veo"

ETNIA = {
    "joe":    {"dominio": "manresethub.pro",        "etnia": "branco"},
    "marcus": {"dominio": "vitalresetlab.site",     "etnia": "negro"},
    "ray":    {"dominio": "primalvitalityhub.site", "etnia": "branco"},
    "chuck":  {"dominio": "allmensnatural.site",    "etnia": "negro"},
    "matt":   {"dominio": "steadystrengthhub.site", "etnia": "branco"},
}
_ET = {"branco": "white American", "negro": "Black American"}

# ---------------------------------------------------------------------------
# ⭐ TRAVAS — eixos que o operador PRE-SELECIONA e o sorteio nao mexe
# ---------------------------------------------------------------------------
# Contrato lido pela ui_agente: [(chave, rotulo, [opcoes])]. O painel desenha um
# botao por opcao, e sortear() respeita o que estiver travado.
TRAVAS_UI = [
    ("sexo", "quem fala", ["homem", "mulher"]),
    ("familia", "cena", ["aponta", "preparo"]),
]

# ---------------------------------------------------------------------------
# STRINGS TRAVADAS — copia literal da doutrina. NAO REESCREVER.
# ---------------------------------------------------------------------------

# CL1 — ela/ele NUNCA toca em nada. E' o que torna o SHORT viavel: sem
# manipulacao nao ha' risco de continuidade entre blocos de 8s gerados
# separadamente (F12b: o Veo solta o objeto da mao).
NAO_TOCA = ("%s never touches, opens, lifts or pours any of the ingredients on "
            "the counter — %s only points at them and explains.")

# CL9 — a bancada e' identica nas cenas 1 e 2
MESMA_BANCADA = ("in the same order and at the same levels, nothing moved, "
                 "nothing added, nothing removed")

# CL21 — a gelatina pronta, SO' na cena 3
GELATINA = "a clear glass bowl of firm dark purple gelatin cubes, glossy and set"

# CL17 — anti-F12b na cena 2 da familia B: punho inteiro + antebraco apoiado.
# ⛔ Nunca `completely motionless` num recipiente que alguem segura: e' ordem
# impossivel e o Veo resolve SOLTANDO o objeto.
PEGADA = ("%s right hand is closed around the glass jar of raw honey, the whole "
          "hand visibly wrapped around it, %s forearm resting steady on the "
          "wooden counter as %s tilts the jar over the tall glass")

ANTICELEB = ("Ordinary relatable face, not a celebrity, not a model, not an "
             "actor, not resembling any famous person.")
CAUDA = "Shot on iPhone, natural grain. No on-screen text, no watermark."

# ---------------------------------------------------------------------------
# EIXOS SORTEAVEIS
# ---------------------------------------------------------------------------
FAMILIAS = [
    {"id": "aponta", "selo": "V", "nome": "a aponta apontada"},
    {"id": "preparo", "selo": "V", "nome": "o preparo na cena 2"},
]

CENARIOS = [
    {"id": "diplomas_cidade", "desc": "a bright medical office, four framed diplomas in dark frames on the wall behind %s, a tall window with an out-of-focus city skyline, a large green plant in the corner"},
    {"id": "diplomas_jardim", "desc": "a bright medical office, five framed diplomas in dark frames on the wall behind %s, a window looking out on green trees, a tall potted plant beside it"},
    {"id": "farmacia", "desc": "a bright clinic room, a long shelf of amber medicine bottles on the wall behind %s, a window with soft daylight, white cabinets below the shelf"},
    {"id": "consultorio_claro", "desc": "a bright consulting room, three framed certificates on the pale wall behind %s, a window with sheer curtains, a small green plant on the sill"},
    {"id": "sala_exame", "desc": "a bright examination room, two framed diplomas on the wall behind %s, a folded white examination couch out of focus at the side, a window with daylight"},
    {"id": "escritorio_livros", "desc": "a bright medical office, a low bookshelf of thick medical books behind %s, three framed diplomas above it, a window with an out-of-focus street"},
]

SCRUBS = ["deep burgundy", "deep teal", "navy blue", "forest green",
          "plum purple", "slate grey", "wine red", "petrol blue"]

# CL8 — a REF pode ser homem ou mulher. ⛔ Nunca tronco nu: isso e' VAZAMENTO,
# nao CLEAN. Ele explica, igual a ela.
REFS_M = [
    {"idade": 44, "cabeca": "her hair in neat cornrows pulled back", "marca": "a small mole above her left eyebrow"},
    {"idade": 41, "cabeca": "her hair in a low tidy bun", "marca": "a small scar at the corner of her jaw"},
    {"idade": 47, "cabeca": "shoulder-length straight hair tucked behind her ears", "marca": "a faint freckle high on her right cheek"},
    {"idade": 39, "cabeca": "short natural curls kept close", "marca": "a small gap between her front teeth"},
    {"idade": 50, "cabeca": "greying hair pulled back into a tight ponytail", "marca": "deep smile lines around her eyes"},
    {"idade": 45, "cabeca": "long braids gathered over one shoulder", "marca": "a small dark mole on her chin"},
]
REFS_H = [
    {"idade": 48, "cabeca": "short greying hair and a close-cropped beard", "marca": "a small scar through his right eyebrow"},
    {"idade": 52, "cabeca": "a clean-shaven head and a short grey beard", "marca": "deep lines across his forehead"},
    {"idade": 44, "cabeca": "short dark hair combed back, clean-shaven", "marca": "a small mole on his left cheek"},
    {"idade": 55, "cabeca": "thinning grey hair and a full grey moustache", "marca": "heavy creases at the corners of his eyes"},
    {"idade": 41, "cabeca": "short cropped hair and a neat goatee", "marca": "a faint scar on his chin"},
    {"idade": 50, "cabeca": "salt-and-pepper hair cut short, clean-shaven", "marca": "a small notch in his right eyebrow"},
]

# CL14 — os DOIS ingredientes do truque. Piso e teto: sao dois, sempre, em
# todas as tres imagens. Nao precisam ser citados na copy — estao ali para
# gerar curiosidade. ⭐ E' seguro porque a VSL L2ML3 NUNCA os nomeia (conferido
# 2026-08-02: promete "three household ingredients" e nunca revela quais).
TRUQUE = [
    {"id": "bicarbonato", "img": "a cardboard box of baking soda standing upright with its printed label and logo clearly visible on the front"},
    {"id": "mel", "img": "a glass jar of raw honey with its printed paper label facing the camera"},
    {"id": "canela", "img": "a small cardboard box of ground cinnamon with its printed label facing the camera"},
    {"id": "limao", "img": "a lemon cut in half, both halves cut-side up on a white saucer"},
    {"id": "vinagre", "img": "a glass bottle of apple cider vinegar with its printed paper label facing the camera"},
]

# ---------------------------------------------------------------------------
# BANCO DE COPY — verificado em 1582 combinacoes, nenhuma estoura os 7s (CL13)
# ---------------------------------------------------------------------------
NUCLEO = ["Johnson", "soldier", "pecker", "manhood", "wiener", "tool", "old boy"]
TETO_FALA = {1: 22, 2: 24, 3: 22}

HOOKS = [
    "You don't need a pill to get hard. These four are two dollars.",
    "Urologists won't tell you this. These four wake your {o} up.",
    "Four things from the produce aisle. Every one helps your {o}.",
    "Doctors make no money when a man fixes his {o} with groceries.",
    "You pay three hundred a month for what these four do for two dollars.",
    "Your doctor never told you this secret. This is what makes your {o} work.",
    "Men over fifty, look at these four. Your {o} has been waiting.",
    "Forget the pharmacy. These four do more for your {o} than the pill.",
    "Every one of these is at your grocery store. Your {o} needs all four.",
    "You don't need a prescription to get hard. You need these four.",
    "The pill people hope you never learn what these do for your {o}.",
    "These four cost less than two dollars. Your {o} feels all of them.",
    "Stop buying pills. Start buying these four and watch your {o}.",
    "Nobody told you groceries could get your {o} hard. These four are the secret.",
]

# CL20 — a bancada e' DERIVADA da copy: `itens` e' o que precisa estar em cena.
# ⛔ Sortear bancada e copy em separado foi o que produziu coco numa fala de
# beterraba (falha em producao, 2026-08-02).
ITEM_A = [
    {"txt": "Beetroot opens the flow", "itens": ["beterraba"]},
    {"txt": "Watermelon builds your stamina", "itens": ["melancia"]},
    {"txt": "Pomegranate pushes blood down", "itens": ["roma"]},
    {"txt": "Ginger wakes the system", "itens": ["gengibre"]},
    {"txt": "Celery thickens the tip", "itens": ["aipo"]},
    {"txt": "Passion fruit hardens you", "itens": ["maracuja"]},
    {"txt": "Coconut restores your twenties", "itens": ["coco"]},
    {"txt": "Pineapple sweetens your milk", "itens": ["abacaxi"]},
    {"txt": "Spinach keeps you going", "itens": ["espinafre"]},
    {"txt": "Cinnamon steadies the pressure", "itens": ["canela"]},
]
ITEM_B = [
    {"txt": "Kale and honey make your milk sweet for the girls", "itens": ["couve", "mel"]},
    {"txt": "Spinach and honey make your milk sweet for her", "itens": ["espinafre", "mel"]},
    {"txt": "Kale and baking soda keep you going all night", "itens": ["couve", "bicarbonato"]},
    {"txt": "Coconut and honey bring your twenties back", "itens": ["coco", "mel"]},
    {"txt": "Beetroot and baking soda open the blood flow", "itens": ["beterraba", "bicarbonato"]},
    {"txt": "Watermelon and honey sweeten your milk for the girls", "itens": ["melancia", "mel"]},
    {"txt": "Ginger and cinnamon wake the whole system up", "itens": ["gengibre", "canela"]},
    {"txt": "Celery and baking soda thicken your milk", "itens": ["aipo", "bicarbonato"]},
    {"txt": "Pineapple and honey make your milk sweet", "itens": ["abacaxi", "mel"]},
    {"txt": "Passion fruit and cinnamon harden you fast", "itens": ["maracuja", "canela"]},
]

# CL15 — a VIRADA e' INTOCAVEL: encurta-se o item A antes dela. Abre com "But"
# porque o contraste explicito e' o que faz a curiosidade.
VIRADAS = [
    "But nothing works without the gelatin trick.",
    "But without the gelatin trick, none of this does anything.",
    "But the secret is in the gelatin trick.",
    "But without the gelatin trick they do nothing.",
    "But it's the gelatin trick that makes them all work.",
    "But without the gelatin trick, none of this works.",
    "But none of it works without the gelatin trick.",
    "But without the gelatin trick, not one of them works.",
    "But the gelatin trick gets your {o} rock hard.",
    "But the gelatin trick turns your {o} to stone.",
    "But the gelatin trick makes your {o} hard as rock.",
    "But the gelatin trick is what gets you rock hard.",
    "But it's the gelatin trick that hardens your {o}.",
    "But the gelatin trick is what your {o} was missing.",
]

# CL11 — a entrega e' IMEDIATA. ⛔ Nenhum CTA promete hora: quem comenta de
# manha nao espera ate' a noite.
CTAS = [
    "Comment gelatin, and I'll send the whole recipe right now.",
    "Comment gelatin, and I'll send the complete recipe right away.",
    "Comment gelatin, and I'll send all four plus the trick.",
    "Comment gelatin, and I'll send you the real secret.",
    "Comment gelatin, and I'll send exactly what to buy, right now.",
    "Comment gelatin, and I'll send the measurements straight away.",
    "Comment gelatin, to get the full recipe right now.",
    "Comment gelatin, and I'll send the part I can't post here.",
    "Comment gelatin, and I'll send you the secret trick.",
    "Comment gelatin, and I'll send the trick that makes these work.",
    "Comment gelatin, and I'll send you the complete trick.",
    "Comment gelatin, and I'll send the recipe right away.",
    "Comment gelatin, and I'll send the whole trick.",
    "Comment gelatin, and I'll send you the secret.",
]

# CL12 — o gate EXPLICA a consequencia, nao ameaca. O sujeito da
# impossibilidade e' ela/ele, nunca o espectador.
GATES = [
    "Don't forget to follow me, or I can't see your message.",
    "Follow me first, or I can't reply to you.",
    "Follow me before you comment, or it never reaches me.",
    "Make sure you're following, or I can't answer you.",
    "Follow me first. I can only message people who follow.",
    "Don't forget to follow, or the app won't let me reply.",
    "Follow me, or I won't be able to find your comment.",
    "Hit follow first, or I can't message you.",
    "Follow me first, or my message can't reach you.",
    "You have to follow me, or my reply will never arrive.",
    "Follow first. I can't message anyone who isn't following.",
    "Don't forget the follow, or I can't send you anything.",
]

# ---------------------------------------------------------------------------
# CATALOGO VISUAL — como cada ingrediente aparece na bancada
# ---------------------------------------------------------------------------
VISUAL = {
    "beterraba": "two whole raw beetroots with their deep purple skin",
    "melancia": "a thick wedge of fresh watermelon, the red flesh facing out",
    "roma": "a whole pomegranate cut in half with the red seeds facing up",
    "gengibre": "a knob of fresh ginger root",
    "aipo": "three stalks of fresh celery",
    "maracuja": "two passion fruits, one cut in half",
    "coco": "a whole green coconut with its top cut open",
    "abacaxi": "a thick ring of fresh pineapple on a white plate",
    "espinafre": "a handful of fresh baby spinach leaves",
    "couve": "a bunch of fresh green kale",
    "canela": "a small cardboard box of ground cinnamon with its printed label facing the camera",
    "mel": "a glass jar of raw honey with its printed paper label facing the camera",
    "bicarbonato": "a cardboard box of baking soda standing upright with its printed label and logo clearly visible on the front",
    "limao": "a lemon cut in half, both halves cut-side up on a white saucer",
    "vinagre": "a glass bottle of apple cider vinegar with its printed paper label facing the camera",
}
IDS_TRUQUE = {t["id"] for t in TRUQUE}

CENAS_UI = ["1 · A FILEIRA", "2 · A LISTA + A VIRADA", "3 · CTA"]

EIXOS_UI = [
    ("familia", "CENA", "FAMILIAS", "nome"),
    ("cenario", "CENÁRIO", "CENARIOS", "id"),
    ("ref", "QUEM FALA", "REFS_M", "cabeca"),
]


def _palavras(s):
    return len(re.sub(r"\{\w+\}", "x", s or "").split())


def _carregar_ledger():
    try:
        with open(LEDGER, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


def _gravar_ledger(led):
    try:
        with open(LEDGER, "w", encoding="utf-8") as f:
            json.dump(led, f, ensure_ascii=False, indent=1)
    except OSError:
        pass


def _fresco(pool, usados, rng, chave):
    """Sorteia evitando o que o ledger ja' usou naquele eixo."""
    livres = [x for x in pool if str(x.get(chave, x)) not in usados] or pool
    return rng.choice(livres)


def sortear(pagina, rng, led, travas=None):
    """Monta a spec. `travas` = {'sexo': 'homem'} fixa o eixo e o sorteio
    respeita — e' o que o painel usa para pre-selecao (TRAVAS_UI)."""
    travas = travas or {}
    usados = led.get(pagina, {})
    et = _ET[ETNIA[pagina]["etnia"]]

    sexo = travas.get("sexo") or rng.choice(["homem", "mulher"])
    fam_id = travas.get("familia")
    familia = (next(f for f in FAMILIAS if f["id"] == fam_id) if fam_id
               else _fresco(FAMILIAS, usados.get("familia", []), rng, "id"))

    ref = rng.choice(REFS_H if sexo == "homem" else REFS_M)
    cenario = _fresco(CENARIOS, usados.get("cenario", []), rng, "id")
    scrub = rng.choice(SCRUBS)

    orgaos = rng.sample(NUCLEO, 2)
    a = rng.choice(ITEM_A)
    b = rng.choice(ITEM_B)
    # ⚠️ COTA: o HOOK sempre carrega o {o} (11 dos 14 hooks tem). Isso garante
    # o piso de 1/3 e libera as 14 VIRADAS — inclusive as 9 de negacao, que nao
    # nomeiam o orgao e que o operador aprovou uma a uma.
    # ⛔ Exigir {o} tambem na virada dava cota 2/3, mas matava 9 das 14 linhas
    # dele. Copy aprovada nao se descarta para satisfazer contador.
    hook = rng.choice([h for h in HOOKS if "{o}" in h]).format(o=orgaos[0])
    virada = rng.choice(VIRADAS).format(o=orgaos[1])
    cta = "%s %s" % (rng.choice(CTAS), rng.choice(GATES))

    # CL14 — DOIS do truque, sempre. Os que a copy ja' cita contam; o resto
    # completa. ⛔ Nunca tres: piso e teto se encontram.
    citados = list(dict.fromkeys(a["itens"] + b["itens"]))
    tru = [i for i in citados if i in IDS_TRUQUE]
    for t in rng.sample(TRUQUE, len(TRUQUE)):
        if len(tru) >= 2:
            break
        if t["id"] not in tru:
            tru.append(t["id"])
    tru = tru[:2]

    # CL20 — a bancada nasce da copy MAIS os dois do truque
    bancada = [i for i in citados if i not in IDS_TRUQUE] + tru

    return {
        "pagina": pagina, "etnia": et, "sexo": sexo, "familia": familia,
        "cenario": cenario, "ref": ref, "scrub": scrub, "orgaos": orgaos,
        "item_a": a, "item_b": b, "bancada": bancada, "truque": tru,
        "falas": [hook, "%s. %s. %s" % (a["txt"], b["txt"], virada), cta],
    }


def _pron(sexo):
    return ("He", "his", "he") if sexo == "homem" else ("She", "her", "she")


def _pessoa(spec, primeiro=True):
    r, sexo = spec["ref"], spec["sexo"]
    quem = "man" if sexo == "homem" else "woman"
    if primeiro:
        return ("a %d-year-old %s %s, wearing a %s V-neck short-sleeved medical "
                "scrub top, %s, %s" % (r["idade"], spec["etnia"], quem,
                                       spec["scrub"], r["cabeca"], r["marca"]))
    return ("The same %d-year-old %s %s, same %s scrub top, same %s, same %s"
            % (r["idade"], spec["etnia"], quem, spec["scrub"],
               r["cabeca"].split(" and ")[0], r["marca"]))


def _fila(ids):
    return ", ".join(VISUAL[i] for i in ids)


def montar(spec):
    """Os 7 blocos. ⚠️ montar() e' o UNICO ponto que olha spec['familia'] —
    sortear() e o banco de copy sao identicos nas duas (CL16)."""
    S, Ss, s = _pron(spec["sexo"])
    b = {}
    fam = spec["familia"]["id"]
    cen = spec["cenario"]["desc"] % ("her" if spec["sexo"] == "mulher" else "him")
    nao_toca = NAO_TOCA % (S, s)
    idade = spec["ref"]["idade"]

    b["BLOCO 0 (REF)"] = (
        "REF 01: Photo of a real person, a %d-year-old %s %s, chest up, facing "
        "the camera directly, neutral steady expression with %s mouth closed. "
        "Wearing a %s V-neck short-sleeved medical scrub top. %s. %s. An "
        "ordinary everyday relatable person with a plain unremarkable face, not "
        "a celebrity, not a model, not an actor, not resembling any famous "
        "person. Hands out of frame, no objects. Plain neutral gray background, "
        "soft even frontal light. Slight sensor grain, soft focus, raw iPhone "
        "front camera aesthetic. No subtitles, no captions, no burned-in text, "
        "no watermark."
        % (idade, spec["etnia"], "man" if spec["sexo"] == "homem" else "woman",
           Ss, spec["scrub"], spec["ref"]["cabeca"][0].upper() + spec["ref"]["cabeca"][1:],
           spec["ref"]["marca"][0].upper() + spec["ref"]["marca"][1:]))

    if fam == "aponta":
        fila = _fila(spec["bancada"])
        b["IMAGE 01/03"] = (
            "Medium shot inside %s. Seated behind a wooden counter is %s. On the "
            "counter in front of %s, at chest height, stand in a row: %s. %s looks "
            "directly into the lens with %s mouth open mid-word as %s speaks, %s "
            "torso upright and %s head raised. %s right index finger is extended "
            "toward the row, %s hand just above the counter. %s touches nothing. "
            "%s is the only person in the frame. %s Soft daylight from the window. %s"
            % (cen, _pessoa(spec), Ss, fila, S, Ss, s, Ss, Ss, Ss, Ss, S, S,
               ANTICELEB, CAUDA))
        b["IMAGE 02/03"] = (
            "Medium shot in the same room, same background. %s. On the counter is "
            "the same row %s: %s. %s looks directly into the lens with %s mouth "
            "open mid-word as %s speaks, %s expression serious and certain. %s "
            "right index finger is extended toward %s, %s hand just above the "
            "counter. %s touches nothing. %s is the only person in the frame. %s %s"
            % (_pessoa(spec, False), MESMA_BANCADA, fila, S, Ss, s, Ss, Ss,
               VISUAL[spec["truque"][0]], Ss, S, S, ANTICELEB, CAUDA))
        b["IMAGE 03/03"] = (
            "Closer medium shot in the same room, same background, same soft "
            "daylight. %s, framed from the waist up. On the counter along the "
            "bottom edge of the frame stand three things only: %s; %s; and %s. %s "
            "looks directly into the lens, calm and confident, one corner of %s "
            "mouth raised in a half-smile, %s mouth open mid-word as %s speaks. %s "
            "right index finger points directly at the camera. %s is the only "
            "person in the frame. %s %s"
            % (_pessoa(spec, False), VISUAL[spec["bancada"][0]], GELATINA,
               VISUAL[spec["truque"][0]], S, Ss, Ss, s, Ss, S, ANTICELEB, CAUDA))
        mov = [
            "%s right hand moves once along the row, the extended index finger "
            "travelling from one end to the other, staying just above the counter "
            "the whole time. Everything on the counter stays exactly as it appears "
            "in the first frame — same position, same angle, same levels — "
            "completely motionless for the entire shot." % Ss,
            "%s extended index finger moves from one item to another and back, "
            "staying just above the counter. Everything on the counter stays "
            "exactly as it appears in the first frame — completely motionless for "
            "the entire shot." % Ss,
            "The glass, the bowl of gelatin cubes and the box beside them stay "
            "exactly as they appear in the first frame — nothing moves, nothing "
            "is touched.",
        ]
    else:
        outros = [i for i in spec["bancada"] if i != "mel"]
        fila = _fila(outros)
        b["IMAGE 01/03"] = (
            "Medium shot inside %s. Seated behind a wooden counter is %s. On the "
            "counter in front of %s, at chest height, stand a tall clear glass "
            "filled with plain clear water, and %s. %s looks directly into the "
            "lens with %s mouth open mid-word as %s speaks, %s torso upright and "
            "%s head raised. %s right index finger is extended toward the glass of "
            "clear water, %s hand just above the counter. %s touches nothing. %s "
            "is the only person in the frame. %s Soft daylight from the window. %s"
            % (cen, _pessoa(spec), Ss, fila, S, Ss, s, Ss, Ss, Ss, Ss, S, S,
               ANTICELEB, CAUDA))
        b["IMAGE 02/03"] = (
            "Medium shot in the same room, same background. %s. %s. A slow thread "
            "of golden honey is falling from the jar into the glass, and the water "
            "in the glass is turning from clear to warm gold where the stream "
            "lands. Everything else on the counter is exactly where it was: %s. %s "
            "looks directly into the lens with %s mouth open mid-word as %s speaks, "
            "%s expression serious and certain. %s is the only person in the frame. "
            "%s %s"
            % (_pessoa(spec, False), PEGADA % (Ss, Ss, s), fila, S, Ss, s, Ss, S,
               ANTICELEB, CAUDA))
        b["IMAGE 03/03"] = (
            "Closer medium shot in the same room, same background, same soft "
            "daylight. %s, framed from the waist up. On the counter along the "
            "bottom edge of the frame stand three things only: the same tall "
            "glass, now filled to the top with a finished warm golden drink and no "
            "longer clear; %s; and %s. %s looks directly into the lens, calm and "
            "confident, one corner of %s mouth raised in a half-smile, %s mouth "
            "open mid-word as %s speaks. %s right index finger points directly at "
            "the camera. %s is the only person in the frame. %s %s"
            % (_pessoa(spec, False), GELATINA, VISUAL["mel"], S, Ss, Ss, s, Ss,
               S, ANTICELEB, CAUDA))
        mov = [
            "%s extended index finger moves once along the row, staying just above "
            "the counter. Everything on the counter stays exactly as it appears in "
            "the first frame — completely motionless for the entire shot, and the "
            "water in the glass stays clear." % Ss,
            "%s keeps %s right hand closed around the jar, the whole hand visibly "
            "wrapped around it, %s forearm resting steady on the counter, and "
            "tilts it a little further so the thread of honey keeps falling into "
            "the glass. As it falls, the water in the glass turns from clear to "
            "warm gold, the colour spreading down through it. %s touches only the "
            "jar %s is pouring from, and everything else stays exactly as it "
            "appears in the first frame." % (S, Ss, Ss, S, s),
            "The finished golden drink, the bowl of gelatin cubes and the jar "
            "beside them stay exactly as they appear in the first frame — nothing "
            "moves, nothing is touched.",
        ]

    audio = ["quiet office room tone. No music.",
             "quiet office room tone, a soft pour. No music." if fam == "preparo"
             else "quiet office room tone. No music.",
             "quiet office room tone. No music."]
    for i in range(3):
        toca = "" if (fam == "preparo" and i == 1) else " " + nao_toca
        b["TAKE %02d/03" % (i + 1)] = (
            "Animate the provided image exactly. Handheld iPhone shot, very "
            "slight natural sway, no cuts. The %d-year-old %s speaks straight "
            "into the lens. %s%s %s is the only person in the shot.\n"
            'Dialogue: "%s"\nAudio: %s'
            % (idade, "man" if spec["sexo"] == "homem" else "woman",
               mov[i], toca, S, sonorizar(spec["falas"][i]), audio[i]))
    return b


def lint(spec, blocos):
    ach = []
    falas = spec["falas"]

    for i, f in enumerate(falas, 1):
        n = _palavras(f)
        if n > TETO_FALA[i]:
            ach.append(("ERRO", "CL13: cena %d com %d palavras (teto %d) — a "
                                "narracao passa de 7s" % (i, n, TETO_FALA[i])))

    corpo = " ".join(falas).lower()
    if "gelatin trick" not in corpo:
        ach.append(("ERRO", "CL15: expressao literal 'gelatin trick' ausente"))
    if "gelatin trick" not in falas[1].lower():
        ach.append(("ERRO", "CL15: a virada tem de estar na CENA 2"))

    # ⚠️ COTA 1/3 NESTE AGENTE, nao 2/3 (ordem do operador, 2026-08-02).
    # Os dois reels de origem quase nao nomeiam o orgao — o v1 diz `wiener` uma
    # vez, o v2 nenhuma. E as 9 viradas de negacao aprovadas nao o nomeiam.
    # Exigir 2/3 obrigaria a descartar copy que o operador validou linha a
    # linha, entao o piso desce e o hook garante ele sozinho.
    cota = sum(1 for f in falas if any(o.lower() in f.lower() for o in NUCLEO))
    if cota < 1:
        ach.append(("ERRO", "cota do orgao 0/3 — o hook tem de nomear o orgao"))
    if len(set(spec["orgaos"])) < 2:
        ach.append(("ERRO", "o mesmo orgao repetido no mesmo video"))
    if not any(o.lower() in falas[0].lower() for o in NUCLEO):
        ach.append(("ERRO", "o hook nao nomeia o orgao"))

    # CL11 — entrega imediata
    for t in ("tonight", "by morning", "later today", "this evening"):
        if t in falas[2].lower():
            ach.append(("ERRO", "CL11: CTA promete hora ('%s') — a entrega e' "
                                "imediata" % t))
    if "gelatin," not in falas[2] and "gelatin." not in falas[2]:
        ach.append(("ERRO", "C3a: keyword sem pausa depois"))
    if "GELATIN" in falas[2]:
        ach.append(("ERRO", "C3a: keyword em CAIXA ALTA no Dialogue:"))

    # CL14 — dois do truque, nem mais nem menos
    if len(spec["truque"]) != 2:
        ach.append(("ERRO", "CL14: %d ingredientes do truque em cena — sao 2"
                            % len(spec["truque"])))

    # CL20 — todo item citado esta' em cena
    citados = set(spec["item_a"]["itens"] + spec["item_b"]["itens"])
    if not citados <= set(spec["bancada"]):
        ach.append(("ERRO", "CL20: a copy cita %s e a bancada nao tem"
                            % ", ".join(sorted(citados - set(spec["bancada"])))))

    # CL21 — a gelatina SO' na cena 3
    for nome in ("IMAGE 01/03", "IMAGE 02/03"):
        if "gelatin cubes" in blocos.get(nome, ""):
            ach.append(("ERRO", "CL21: gelatina fora da cena 3 (%s)" % nome))
    if "gelatin cubes" not in blocos.get("IMAGE 03/03", ""):
        ach.append(("ERRO", "CL21: a cena 3 tem de mostrar a gelatina em cubos"))

    # CL1/CL2 — nada de manipular, nada de prop falico
    for nome, txt in blocos.items():
        if not nome.startswith(("IMAGE", "TAKE")):
            continue
        direcao = txt.split("\nDialogue:")[0]
        # ⛔ tirar a PROPRIA proibicao antes de varrer: NAO_TOCA contem a
        # palavra "pours", e o linter se auto-reprovava em 100% dos sorteios.
        # Regra que reprova tudo nunca foi testada.
        for pr in (("He", "he"), ("She", "she")):
            direcao = direcao.replace(NAO_TOCA % pr, "")
        direcao = direcao.lower()
        if nome.endswith("02/03") and spec["familia"]["id"] == "preparo":
            continue
        for tok in ("pours", "stirs", "picks up", "squeezes", "holds up"):
            if tok in direcao:
                ach.append(("ERRO", "CL1: '%s' em %s — %s so' aponta"
                                    % (tok, nome, "ele" if spec["sexo"] == "homem"
                                       else "ela")))
        for tok in ("cucumber", "banana", "eggplant", "sausage", "geoduck",
                    "anatomy model", "bare-chested"):
            if tok in direcao:
                ach.append(("ERRO", "CL2: '%s' em %s — o CLEAN nao tem prop "
                                    "falico nem tronco nu" % (tok, nome)))
    return ach


def resumo_pt(spec):
    fam = ("ela aponta, nada se mexe" if spec["familia"]["id"] == "aponta"
           else "ela prepara na cena 2, o copo muda de cor")
    if spec["sexo"] == "homem":
        fam = fam.replace("ela ", "ele ")
    return ("%s de %d anos, de scrub %s, num %s. Na bancada: %s. %s. Três cenas, "
            "%s." % ("Homem" if spec["sexo"] == "homem" else "Mulher",
                     spec["ref"]["idade"], spec["scrub"],
                     spec["cenario"]["id"].replace("_", " "),
                     ", ".join(spec["bancada"]), fam.capitalize(),
                     "gelatina em cubos na última"))


def nova_fala(spec, i, rng):
    """Re-sorteia a copy de UMA cena, ja' formatada com os slots deste video.
    ⚠️ A cena 2 e' composta (item A. item B. virada) — re-sortear so' um pedaco
    deixaria a bancada incongruente com a fala (CL20), entao ela e' remontada
    inteira a partir dos itens que JA' estao em cena."""
    o = spec["orgaos"]
    if i == 0:
        return rng.choice([h for h in HOOKS if "{o}" in h]).format(o=o[0])
    if i == 2:
        return "%s %s" % (rng.choice(CTAS), rng.choice(GATES))
    # cena 2: mantem os itens da bancada, troca so' a virada
    return "%s. %s. %s" % (spec["item_a"]["txt"], spec["item_b"]["txt"],
                           rng.choice(VIRADAS).format(o=o[1]))


EIXOS_QUE_MEXEM_NA_COPY = {}


def main():
    ap = argparse.ArgumentParser(description="Randomizador do agente CLEAN")
    ap.add_argument("--pagina", choices=sorted(ETNIA))
    ap.add_argument("--n", type=int, default=1)
    ap.add_argument("--seed", type=int)
    ap.add_argument("--sexo", choices=["homem", "mulher"])
    ap.add_argument("--familia", choices=["aponta", "preparo"])
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    if not a.pagina:
        ap.error("--pagina obrigatorio")

    seed = a.seed if a.seed is not None else random.randrange(10 ** 6)
    rng = random.Random(seed)
    led = _carregar_ledger()
    travas = {k: v for k, v in (("sexo", a.sexo), ("familia", a.familia)) if v}

    for _ in range(a.n):
        spec = sortear(a.pagina, rng, led, travas)
        blocos = montar(spec)
        print("=" * 72)
        print("SPEC — pagina %s | %s | familia %s | bancada: %s"
              % (a.pagina, spec["sexo"], spec["familia"]["id"],
                 ", ".join(spec["bancada"])))
        print("=" * 72)
        for nome, txt in blocos.items():
            print(txt if nome.startswith("BLOCO") else "\n%s\n%s: %s"
                  % ("-" * 72, nome, txt))
        ach = lint(spec, blocos)
        print("\n" + "=" * 72)
        if ach:
            for tipo, msg in ach:
                print("[%s] %s" % (tipo, msg))
            print("%d erro(s)." % len(ach))
        else:
            print("LINTER: OK — nenhuma violacao mecanica.")
        if not a.dry_run:
            u = led.setdefault(a.pagina, {})
            for eixo, val in (("familia", spec["familia"]["id"]),
                              ("cenario", spec["cenario"]["id"])):
                u.setdefault(eixo, [])
                if val not in u[eixo]:
                    u[eixo].append(val)
                if len(u[eixo]) >= len({"familia": FAMILIAS,
                                        "cenario": CENARIOS}[eixo]):
                    u[eixo] = [val]
    if not a.dry_run:
        _gravar_ledger(led)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
