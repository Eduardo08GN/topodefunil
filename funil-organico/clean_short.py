#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
clean_short.py — randomizador + gerador + linter do AGENTE CLEAN.

A fileira apontada: profissional de saude sozinha(o) de scrub, uma fileira de
itens comestiveis na bancada, e o dedo ligando cada item a um beneficio.
ZERO prop falico, ZERO anatomia, ZERO vitima.

Fonte: Valentina Health & Wellness, 2 reels (13,3k e 7,1k comentarios).
Doutrina: AGENTE_ED_CLEAN_V1.md · concorrentes/clean-mapa-visual.md

⭐ SHORT NATIVO — 3 cenas de 8s. Nao deriva de motor longo e nao tera versao
longa (CL16). Duas FAMILIAS de cena, uma copy so':

    aponta   ela so' aponta, a bancada nao muda em nenhuma das 3 cenas
    preparo  ela PREPARA nas cenas 1 e 2 — um ingrediente por cena — e a
             cena 3 e' so' o resultado pronto ao lado da gelatina (CL17)

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
SUBTITULO = "a fileira apontada, em 3 cenas · gerador offline de prompts Veo"

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

# CL9 — a bancada e' identica nas cenas 1 e 2 (familia A)
MESMA_BANCADA = ("in the same order and at the same levels, nothing moved, "
                 "nothing added, nothing removed")

# CL9 familia B — o copo muda, o resto nao. ⛔ Sem `at the same levels`: o nivel
# do copo SOBE a cada despejo, e pedir nivel identico e' ordem contraditoria —
# o Veo resolve desfazendo o preparo.
MESMA_BANCADA_B = ("Nothing has been added to the counter and nothing removed "
                   "from it — only the tall glass has changed.")

# CL14 familia B, cenas 1 e 2 — ela toca UM recipiente e so' ele. Substitui o
# NAO_TOCA nessas duas cenas; na cena 3 o NAO_TOCA volta inteiro.
TOCA_UM = ("%s touches only the container %s is pouring from. %s never touches, "
           "opens or lifts anything else on the counter.")

# CL21 — a gelatina pronta, SO' na cena 3
GELATINA = "a clear glass bowl of firm dark purple gelatin cubes, glossy and set"

# CL17 — anti-F12b nas cenas 1 e 2 da familia B: punho inteiro + antebraco
# apoiado. ⛔ Nunca `completely motionless` num recipiente que alguem segura:
# e' ordem impossivel e o Veo resolve SOLTANDO o objeto.
# ⚠️ O esqueleto e' o do mel, validado em render 2026-08-02 — so' o recipiente
# e o gesto trocam (tabela DESPEJO). String validada nao se redigita.
PEGADA = ("%s right hand is closed around the %s, the whole hand visibly "
          "wrapped around it, %s forearm resting steady on the wooden counter "
          "as %s %s")

ANTICELEB = ("Ordinary relatable face, not a celebrity, not a model, not an "
             "actor, not resembling any famous person.")
CAUDA = "Shot on iPhone, natural grain. No on-screen text, no watermark."

# ---------------------------------------------------------------------------
# EIXOS SORTEAVEIS
# ---------------------------------------------------------------------------
FAMILIAS = [
    {"id": "aponta", "selo": "V", "nome": "a fileira apontada"},
    # ⚠️ selo N: o despejo na CENA 2 passou em render (2026-08-02); o da CENA 1
    # ainda nao. Selo e' medicao, nao palpite — desce ate' o primeiro lote.
    {"id": "preparo", "selo": "N", "nome": "o preparo nas cenas 1 e 2"},
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

# CL17 — a acao travada de cada ingrediente do truque, na familia B. Uma acao,
# um recipiente, uma cena: o ingrediente 1 e' despejado na CENA 1 e o 2 na CENA
# 2. ⛔ Nunca o mesmo duas vezes, ⛔ nunca os dois na mesma cena, ⛔ ZERO
# manipulacao na cena 3.
# ⚠️ O sache de gelatina NAO entra aqui: gelatina so' na cena 3 e em cubos
# (CL21) — despeja-la antes entrega o payoff antes da promessa.
# ⚠️ A linha do `mel` e' a validada em render 2026-08-02; as outras quatro
# copiam a gramatica dela e trocam so' o recipiente, o gesto e a cor.
DESPEJO = {
    "bicarbonato": {
        "cont": "cardboard box of baking soda",
        "curto": "box",
        "gesto": "tips the box over the tall glass",
        "queda": "a short stream of fine white powder is falling from the box into the glass",
        "segue": "tips it a little further so the stream of white powder keeps falling into the glass",
        "cor": "clouded milky white",
        "tom": 1,
        "som": "a soft dry pour",
    },
    "mel": {
        "cont": "glass jar of raw honey",
        "curto": "jar",
        "gesto": "tilts the jar over the tall glass",
        "queda": "a slow thread of golden honey is falling from the jar into the glass",
        "segue": "tilts it a little further so the thread of honey keeps falling into the glass",
        "cor": "warm gold",
        "tom": 4,
        "som": "a soft pour",
    },
    "canela": {
        "cont": "small cardboard box of ground cinnamon",
        "curto": "box",
        "gesto": "tips the box over the tall glass",
        "queda": "a fine fall of brown cinnamon dust is dropping from the box into the glass",
        "segue": "tips it a little further so the brown cinnamon dust keeps falling into the glass",
        "cor": "cloudy warm brown",
        "tom": 5,
        "som": "a soft dry pour",
    },
    "limao": {
        "cont": "lemon half",
        "curto": "lemon half",
        "gesto": "presses the lemon half over the tall glass",
        "queda": "clear juice is running from the lemon half down into the glass",
        "segue": "presses it a little harder so the juice keeps running down into the glass",
        "cor": "pale cloudy yellow",
        "tom": 2,
        "som": "a soft trickle",
    },
    "vinagre": {
        "cont": "glass bottle of apple cider vinegar",
        "curto": "bottle",
        "gesto": "tilts the bottle over the tall glass",
        "queda": "a thin clear stream is running from the bottle into the glass",
        "segue": "tilts it a little further so the clear stream keeps running into the glass",
        "cor": "pale amber",
        "tom": 3,
        "som": "a soft pour",
    },
}

# ---------------------------------------------------------------------------
# BANCO DE COPY — 1582 combinacoes (14 · 1400 · 168), nenhuma estoura os 7s
# (CL13), medido com o orgao JA' substituido.
# ⚠️ A cena 2 tem os 1400 de volta porque os pools ficaram DISJUNTOS: o solver
# do CL22 nao precisa mais descartar par nenhum. Ele fica como rede de
# seguranca, nao como mecanismo.
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
# CL22 — `ben` e' a etiqueta do BENEFICIO, e existe so' para o solver de
# colisao. Item A e item B nunca repetem fruta, ingrediente do truque nem
# beneficio: em estrutura de LISTA, item repetido nao e' redundancia — e' um
# item a menos, e a cena 2 gastou metade das 24 palavras a' toa.
# ⛔ Nenhum item A cita LEITE: metade do pool de item B fala em adocar o leite,
# entao a colisao seria quase certa (falha em producao 2026-08-02 —
# "Pineapple sweetens your milk. Spinach and honey make your milk sweet for
# her." saiu no ar).
# ⭐⭐ O ITEM A E' DISJUNTO DO ITEM B — POR CONSTRUCAO, NAO POR SOLVER (ordem do
# operador, 2026-08-02). Nenhuma linha daqui usa ingrediente ou beneficio que
# apareca em QUALQUER linha do ITEM_B. Antes os dois pools compartilhavam as
# frutas e os beneficios, e o solver do CL22 tinha de descartar 12 dos 100
# pares; agora os 100 sao validos e a repeticao deixa de ser possivel.
# ⚠️ O ITEM_B nao mudou uma virgula — o operador aprovou aquelas linhas.
# ⛔ Ao acrescentar linha aqui, conferir contra INGREDIENTES_B/BENEFICIOS_B (o
# teste de disjuncao no fim do arquivo reprova sozinho).
ITEM_A = [
    {"txt": "Pomegranate cleans your blood", "itens": ["roma"], "ben": "sangue"},
    {"txt": "Garlic raises your drive", "itens": ["alho"], "ben": "libido"},
    {"txt": "Walnuts sharpen the feeling", "itens": ["nozes"], "ben": "sensacao"},
    {"txt": "Blueberries steady the pressure", "itens": ["mirtilo"], "ben": "pressao"},
    {"txt": "Turmeric fights inflammation", "itens": ["curcuma"], "ben": "inflamacao"},
    {"txt": "Oats speed your recovery", "itens": ["aveia"], "ben": "recupera"},
    {"txt": "Avocado feeds the pump", "itens": ["abacate"], "ben": "bomba"},
    {"txt": "Cayenne heats you up", "itens": ["pimenta"], "ben": "calor"},
    {"txt": "Grapes carry oxygen down", "itens": ["uva"], "ben": "oxigenio"},
    {"txt": "Tomatoes protect your prostate", "itens": ["tomate"], "ben": "prostata"},
]
ITEM_B = [
    {"txt": "Kale and honey make your milk sweet for the girls", "itens": ["couve", "mel"], "ben": "leite"},
    {"txt": "Spinach and honey make your milk sweet for her", "itens": ["espinafre", "mel"], "ben": "leite"},
    {"txt": "Kale and baking soda keep you going all night", "itens": ["couve", "bicarbonato"], "ben": "aguenta"},
    {"txt": "Coconut and honey bring your twenties back", "itens": ["coco", "mel"], "ben": "vinte-anos"},
    {"txt": "Beetroot and baking soda open the blood flow", "itens": ["beterraba", "bicarbonato"], "ben": "fluxo"},
    {"txt": "Watermelon and honey sweeten your milk for the girls", "itens": ["melancia", "mel"], "ben": "leite"},
    {"txt": "Ginger and cinnamon wake the whole system up", "itens": ["gengibre", "canela"], "ben": "acorda"},
    {"txt": "Celery and baking soda thicken your milk", "itens": ["aipo", "bicarbonato"], "ben": "engrossa"},
    {"txt": "Pineapple and honey make your milk sweet", "itens": ["abacaxi", "mel"], "ben": "leite"},
    # ⛔ era `Passion fruit and cinnamon harden you fast` — a UNICA linha dos
    # dois pools que prometia dureza. A dureza e' exclusiva do gelatin trick
    # (CL23, ordem do operador 2026-08-02).
    {"txt": "Passion fruit and cinnamon widen every vessel", "itens": ["maracuja", "canela"], "ben": "vasos"},
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
    # --- citados pelo ITEM_A (disjuntos do ITEM_B) ---
    # ⛔ CL2: nada alongado. A pimenta entra em PO', nunca a vagem inteira, e o
    # abacate parte-se como o limao — a regua e' "um estranho olhando so' pensa
    # em comida".
    "roma": "a whole pomegranate cut in half with the red seeds facing up",
    "alho": "a whole head of garlic with two loose cloves beside it",
    "nozes": "a small white saucer of shelled walnut halves",
    "mirtilo": "a small white bowl of fresh blueberries",
    "curcuma": "a small glass bowl of bright yellow turmeric powder",
    "aveia": "a white bowl of dry rolled oats",
    "abacate": "an avocado cut in half, both halves cut-side up on a white plate",
    "pimenta": "a small glass bowl of red cayenne pepper powder",
    "uva": "a bunch of dark red grapes",
    "tomate": "two ripe red tomatoes, one cut in half",
    # --- citados pelo ITEM_B ---
    "beterraba": "two whole raw beetroots with their deep purple skin",
    "melancia": "a thick wedge of fresh watermelon, the red flesh facing out",
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

# ⭐⭐ CL22 NA CARGA DO MODULO — os dois pools tem de ser disjuntos, e isso se
# verifica ao importar, nao no linter de um sorteio. Linter so' pega o que o
# sorteio calhou de gerar; assercao pega a linha errada no instante em que
# alguem a escreve. Foi copy repetida saindo no ar duas vezes (2026-08-02) que
# pagou por esta linha.
INGREDIENTES_B = {i for b in ITEM_B for i in b["itens"]}
BENEFICIOS_B = {b["ben"] for b in ITEM_B}
for _a in ITEM_A:
    assert not (set(_a["itens"]) & INGREDIENTES_B), (
        "CL22: item A '%s' usa ingrediente que o item B tambem usa: %s"
        % (_a["txt"], ", ".join(sorted(set(_a["itens"]) & INGREDIENTES_B))))
    assert _a["ben"] not in BENEFICIOS_B, (
        "CL22: item A '%s' usa o beneficio '%s', que o item B tambem usa"
        % (_a["txt"], _a["ben"]))
    assert "milk" not in _a["txt"].lower(), (
        "CL22: item A '%s' cita leite — leite e' assunto do item B" % _a["txt"])
    assert len(_a["txt"].split()) <= 4, (
        "CL15: item A '%s' passa de 4 palavras" % _a["txt"])
for _p in (ITEM_A, ITEM_B):
    for _x in _p:
        for _i in _x["itens"]:
            assert _i in VISUAL, "CL20: '%s' citado na copy e sem VISUAL" % _i

# ⭐⭐ CL23 — A DUREZA E' EXCLUSIVA DO GELATIN TRICK (ordem do operador,
# 2026-08-02). Nenhum ingrediente deixa duro: eles dao fluxo, resistencia,
# vasos, recuperacao, sensacao. Quem endurece e' o truque, e so' ele — e' o que
# faz o espectador precisar do truque em vez de so' da lista de compras.
# ⛔ Saiu no ar `Passion fruit hardens you. (...) But the gelatin trick is what
# gets you rock hard.`: a fruta ja' entregava o que a virada vende.
_DUREZA = re.compile(r"\b(hard|harder|hardens?|hardening|stiff|stiffens?|"
                     r"erect|as rock|to stone|steel)\b", re.I)
for _x in ITEM_A + ITEM_B:
    assert not _DUREZA.search(_x["txt"]), (
        "CL23: '%s' promete dureza — so' o gelatin trick endurece" % _x["txt"])
for _v in VIRADAS:
    if _DUREZA.search(_v):
        assert "gelatin trick" in _v, (
            "CL23: a virada '%s' promete dureza sem nomear o gelatin trick" % _v)

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


def _colide(a, b):
    """CL22 — o par item A / item B repete fruta, ingrediente do truque ou
    beneficio? Colidiu, sorteia-se outro item B: rejeita-se o PAR, nunca se
    reescreve a frase para disfarcar."""
    return bool(set(a["itens"]) & set(b["itens"])) or a["ben"] == b["ben"]


def _viradas_que_cabem(a, b, orgao):
    """CL13 — o teto se mede DEPOIS de substituir o orgao.

    ⚠️ `_palavras` conta `{o}` como UMA palavra, mas `old boy` sao DUAS. O
    banco de copy foi verificado com o placeholder, nao com o texto final, e
    por isso duas viradas estouravam o teto de 24 sempre que o sorteio caia em
    `old boy` — 0,2% dos videos saiam reprovados pelo proprio linter. Bug
    latente desde o primeiro commit, medido em varredura 2026-08-02.
    ⛔ Nao se encurta a virada (CL15): descarta-se a que nao couber.
    """
    base = "%s. %s. " % (a["txt"], b["txt"])
    cabem = [v for v in VIRADAS
             if _palavras(base + v.format(o=orgao)) <= TETO_FALA[2]]
    return cabem or VIRADAS


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
    # CL22 — o par nao repete fruta, ingrediente do truque nem beneficio. Todo
    # item A tem no minimo 8 item B livres, entao a lista nunca fica vazia e
    # nao ha' laco de tentativa e erro.
    b = rng.choice([x for x in ITEM_B if not _colide(a, x)])
    # ⚠️ COTA: o HOOK sempre carrega o {o} (11 dos 14 hooks tem). Isso garante
    # o piso de 1/3 e libera as 14 VIRADAS — inclusive as 9 de negacao, que nao
    # nomeiam o orgao e que o operador aprovou uma a uma.
    # ⛔ Exigir {o} tambem na virada dava cota 2/3, mas matava 9 das 14 linhas
    # dele. Copy aprovada nao se descarta para satisfazer contador.
    hook = rng.choice([h for h in HOOKS if "{o}" in h]).format(o=orgaos[0])
    virada = rng.choice(_viradas_que_cabem(a, b, orgaos[1])).format(o=orgaos[1])
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

    # CL17 — ⭐ A ORDEM DO DESPEJO NAO E' SORTEADA: o mais CLARO vai na cena 1 e
    # o mais ESCURO na cena 2, sempre. A bebida so' pode escurecer.
    # ⛔ Sorteando a ordem, METADE das 20 combinacoes mandava o Veo CLAREAR o
    # liquido — `cloudy warm brown` recebendo po' branco e virando
    # `clouded milky white`. Fisica impossivel: o Veo ou ignora ou inventa um
    # corte. Medido em 2026-08-02, depois que um sorteio real caiu em
    # canela -> bicarbonato.
    # ⚠️ Calculada SEMPRE, nas duas familias: o botao `trocar cena` do painel
    # vira spec["familia"] direto, sem passar por sortear(), e montar() ficaria
    # sem a chave.
    despejo = sorted(tru, key=lambda i: DESPEJO[i]["tom"])

    return {
        "pagina": pagina, "etnia": et, "sexo": sexo, "familia": familia,
        "cenario": cenario, "ref": ref, "scrub": scrub, "orgaos": orgaos,
        "item_a": a, "item_b": b, "bancada": bancada, "truque": tru,
        "despejo": despejo,
        "falas": [hook, "%s. %s. %s" % (a["txt"], b["txt"], virada), cta],
    }


def _pron(sexo):
    """(sujeito, possessivo, sujeito minusculo, OBJETO).

    ⚠️ O objeto existe porque `his` nao serve de complemento: `in front of his`
    saia em todo video de REF masculina. Em `her` os dois casos coincidem, e por
    isso o bug passou despercebido — so' metade dos sorteios o mostrava."""
    return (("He", "his", "he", "him") if sexo == "homem"
            else ("She", "her", "she", "her"))


def _sem_artigo(s):
    """Tira o artigo inicial para a frase `same %s` nao virar `same a ...`."""
    for art in ("a ", "an ", "the "):
        if s.startswith(art):
            return s[len(art):]
    return s


def _pessoa(spec, primeiro=True):
    r, sexo = spec["ref"], spec["sexo"]
    quem = "man" if sexo == "homem" else "woman"
    if primeiro:
        return ("a %d-year-old %s %s, wearing a %s V-neck short-sleeved medical "
                "scrub top, %s, %s" % (r["idade"], spec["etnia"], quem,
                                       spec["scrub"], r["cabeca"], r["marca"]))
    return ("The same %d-year-old %s %s, same %s scrub top, same %s, same %s"
            % (r["idade"], spec["etnia"], quem, spec["scrub"],
               _sem_artigo(r["cabeca"].split(" and ")[0]),
               _sem_artigo(r["marca"])))


def _fila(ids):
    return ", ".join(VISUAL[i] for i in ids)


def _cap(s):
    return s[0].upper() + s[1:] if s else s


def montar(spec):
    """Os 7 blocos. ⚠️ montar() e' o UNICO ponto que olha spec['familia'] —
    sortear() e o banco de copy sao identicos nas duas (CL16)."""
    S, Ss, s, obj = _pron(spec["sexo"])
    b = {}
    fam = spec["familia"]["id"]
    cen = spec["cenario"]["desc"] % obj
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
            % (cen, _pessoa(spec), obj, fila, S, Ss, s, Ss, Ss, _cap(Ss), Ss, S, S,
               ANTICELEB, CAUDA))
        b["IMAGE 02/03"] = (
            "Medium shot in the same room, same background. %s. On the counter is "
            "the same row %s: %s. %s looks directly into the lens with %s mouth "
            "open mid-word as %s speaks, %s expression serious and certain. %s "
            "right index finger is extended toward %s, %s hand just above the "
            "counter. %s touches nothing. %s is the only person in the frame. %s %s"
            % (_pessoa(spec, False), MESMA_BANCADA, fila, S, Ss, s, Ss, _cap(Ss),
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
               VISUAL[spec["truque"][0]], S, Ss, Ss, s, _cap(Ss), S,
               ANTICELEB, CAUDA))
        mov = [
            "%s right hand moves once along the row, the extended index finger "
            "travelling from one end to the other, staying just above the counter "
            "the whole time. Everything on the counter stays exactly as it appears "
            "in the first frame — same position, same angle, same levels — "
            "completely motionless for the entire shot." % _cap(Ss),
            "%s extended index finger moves from one item to another and back, "
            "staying just above the counter. Everything on the counter stays "
            "exactly as it appears in the first frame — completely motionless for "
            "the entire shot." % _cap(Ss),
            "The glass, the bowl of gelatin cubes and the box beside them stay "
            "exactly as they appear in the first frame — nothing moves, nothing "
            "is touched.",
        ]
    else:
        # CL17 — o ingrediente 1 e' despejado na cena 1, o 2 na cena 2. O que
        # esta' na mao sai da fileira da bancada NAQUELA cena e volta na
        # seguinte; assim os DOIS aparecem nas tres imagens e o piso do CL14
        # continua de pe'.
        i1, i2 = spec["despejo"]
        d1, d2 = DESPEJO[i1], DESPEJO[i2]
        v = {"ref1": _pessoa(spec), "ref": _pessoa(spec, False), "cen": cen,
             "S": S, "Ss": Ss, "s": s, "gel": GELATINA, "anti": ANTICELEB,
             "cauda": CAUDA, "resto": MESMA_BANCADA_B, "obj": obj,
             "fila1": _fila([i for i in spec["bancada"] if i != i1]),
             "fila2": _fila([i for i in spec["bancada"] if i != i2]),
             "cor1": d1["cor"], "cor2": d2["cor"],
             "c1": d1["curto"], "c2": d2["curto"], "ing2": VISUAL[i2],
             "Sc": Ss[0].upper() + Ss[1:],   # "Her"/"His" em inicio de frase
             "peg1": _cap(PEGADA % (Ss, d1["cont"], Ss, s, d1["gesto"])),
             "peg2": _cap(PEGADA % (Ss, d2["cont"], Ss, s, d2["gesto"])),
             "cai1": _cap(d1["queda"]), "cai2": _cap(d2["queda"]),
             "seg1": d1["segue"], "seg2": d2["segue"]}
        # ⚠️ Formatacao NOMEADA neste ramo, nao posicional: sao 14+ campos por
        # bloco e um deslocamento de indice troca pronome por cor sem estourar
        # erro nenhum — bug que so' aparece no video pronto.
        b["IMAGE 01/03"] = (
            "Medium shot inside %(cen)s. Seated behind a wooden counter is "
            "%(ref1)s. On the counter in front of %(obj)s, at chest height, stand "
            "a tall clear glass filled with plain clear water and, beside it, "
            "%(fila1)s. %(peg1)s. %(cai1)s, and the water in the glass is "
            "turning from clear to %(cor1)s where the stream lands. %(S)s looks "
            "directly into the lens with %(Ss)s mouth open mid-word as %(s)s "
            "speaks, %(Ss)s torso upright and %(Ss)s head raised. %(S)s is the "
            "only person in the frame. %(anti)s Soft daylight from the window. "
            "%(cauda)s" % v)
        # ⚠️ A cena 2 CLAREIA se a segunda cor for mais clara que a primeira —
        # despejar mel em agua marrom nao produz dourado. Por isso o liquido
        # `clouds over` em vez de trocar de tom: vale para os 20 pares, e
        # nenhum deles le como o preparo desandando.
        b["IMAGE 02/03"] = (
            "Medium shot in the same room, same background. %(ref)s. On the "
            "counter, in the same order and at the same positions as before, "
            "stand %(fila2)s. %(resto)s %(peg2)s. %(cai2)s, and the %(cor1)s "
            "water in the glass is clouding over and turning %(cor2)s where the "
            "stream lands. %(S)s looks directly into the lens with %(Ss)s mouth "
            "open mid-word as %(s)s speaks, %(Ss)s expression serious and "
            "certain. %(S)s is the only person in the frame. %(anti)s "
            "%(cauda)s" % v)
        # CL21 — a cena 3 e' o RESULTADO: copo pronto + gelatina, e so' um dos
        # dois do truque ao lado (a prioridade do CL21 manda cortar o resto
        # antes da gelatina). Zero manipulacao.
        b["IMAGE 03/03"] = (
            "Closer medium shot in the same room, same background, same soft "
            "daylight. %(ref)s, framed from the waist up. On the counter along "
            "the bottom edge of the frame stand three things only: the same tall "
            "glass, now filled to the top with a finished %(cor2)s drink and no "
            "longer clear; %(gel)s; and %(ing2)s. %(S)s looks directly into the "
            "lens, calm and confident, one corner of %(Ss)s mouth raised in a "
            "half-smile, %(Ss)s mouth open mid-word as %(s)s speaks. %(Sc)s right "
            "index finger points directly at the camera. %(S)s is the only person "
            "in the frame. %(anti)s %(cauda)s" % v)
        # ⚠️ A clausula de toque saiu daqui: o TAKE ja' carrega o TOCA_UM
        # (CL14), e dizer a mesma regra duas vezes no mesmo prompt e' so' ruido.
        # Fica a clausula de CONTINUIDADE, que e' o que a validacao segurou.
        mov = [
            "%(S)s keeps %(Ss)s right hand closed around the %(c1)s, the whole "
            "hand visibly wrapped around it, %(Ss)s forearm resting steady on the "
            "counter, and %(seg1)s. As it falls, the water in the glass turns "
            "from clear to %(cor1)s, the colour spreading down through it. "
            "Everything else stays exactly as it appears in the first frame." % v,
            "%(S)s keeps %(Ss)s right hand closed around the %(c2)s, the whole "
            "hand visibly wrapped around it, %(Ss)s forearm resting steady on the "
            "counter, and %(seg2)s. As it falls, the %(cor1)s water in the glass "
            "clouds over and turns %(cor2)s, the colour spreading down through "
            "it. Everything else stays exactly as it appears in the first "
            "frame." % v,
            "The finished %(cor2)s drink, the bowl of gelatin cubes and the "
            "%(c2)s beside them stay exactly as they appear in the first frame — "
            "nothing moves, nothing is touched." % v,
        ]

    if fam == "preparo":
        audio = ["quiet office room tone, %s. No music."
                 % DESPEJO[spec["despejo"][0]]["som"],
                 "quiet office room tone, %s. No music."
                 % DESPEJO[spec["despejo"][1]]["som"],
                 "quiet office room tone. No music."]
    else:
        audio = ["quiet office room tone. No music."] * 3
    # CL14 — nas cenas 1 e 2 da familia B a frase travada vira TOCA_UM; na
    # cena 3 (e na familia A inteira) o NAO_TOCA volta.
    toca_um = TOCA_UM % (S, s, S)
    for i in range(3):
        toca = " " + (toca_um if (fam == "preparo" and i in (0, 1)) else nao_toca)
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

    # CL22 — item A e item B nunca repetem fruta, ingrediente nem beneficio
    if _colide(spec["item_a"], spec["item_b"]):
        ach.append(("ERRO", "CL22: item A e item B se repetem — \"%s\" + \"%s\""
                            % (spec["item_a"]["txt"], spec["item_b"]["txt"])))
    if "milk" in spec["item_a"]["txt"].lower():
        ach.append(("ERRO", "CL22: item A cita leite — o leite e' assunto do "
                            "item B, que vem logo em seguida"))

    # CL17 — familia B: um ingrediente por cena, os dois em cena nas tres
    if spec["familia"]["id"] == "preparo":
        d = spec["despejo"]
        if len(set(d)) != 2 or set(d) != set(spec["truque"]):
            ach.append(("ERRO", "CL17: o despejo tem de ser os DOIS do truque, "
                                "um por cena — veio %s" % ", ".join(d)))
        # ⛔ a bebida so' escurece: cena 2 nunca pode ser mais clara que a 1
        if DESPEJO[d[1]]["tom"] < DESPEJO[d[0]]["tom"]:
            ach.append(("ERRO", "CL17: o despejo CLAREIA a bebida (%s -> %s) — "
                                "o mais escuro vai na cena 2"
                                % (DESPEJO[d[0]]["cor"], DESPEJO[d[1]]["cor"])))
        for nome in ("IMAGE 01/03", "IMAGE 02/03"):
            img = blocos.get(nome, "")
            for ing in spec["truque"]:
                if VISUAL[ing] not in img and DESPEJO[ing]["cont"] not in img:
                    ach.append(("ERRO", "CL14: '%s' fora de %s — os dois do "
                                        "truque estao nas tres imagens"
                                        % (ing, nome)))
        t3 = blocos.get("TAKE 03/03", "").lower()
        if any(w in t3 for w in ("keeps falling", "keeps running", "pouring from")):
            ach.append(("ERRO", "CL17: manipulacao na cena 3 — ela so' apresenta "
                                "o resultado pronto"))

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
        for pr in (("He", "he", "He"), ("She", "she", "She")):
            direcao = direcao.replace(TOCA_UM % pr, "")
        direcao = direcao.lower()
        # ⚠️ Na familia B o despejo e' autorizado nas cenas 1 E 2 (CL17). A
        # cena 3 NAO e' isenta: la' vale o CL1 inteiro, maos fora.
        # ⛔ O `continue` antigo pulava tambem o CL2 na cena isenta — prop
        # falico nunca deixa de ser proibido.
        isenta = (spec["familia"]["id"] == "preparo"
                  and nome.endswith(("01/03", "02/03")))
        if not isenta:
            for tok in ("pours", "stirs", "picks up", "squeezes", "holds up"):
                if tok in direcao:
                    ach.append(("ERRO", "CL1: '%s' em %s — %s so' aponta"
                                        % (tok, nome,
                                           "ele" if spec["sexo"] == "homem"
                                           else "ela")))
        for tok in ("cucumber", "banana", "eggplant", "sausage", "geoduck",
                    "anatomy model", "bare-chested"):
            if tok in direcao:
                ach.append(("ERRO", "CL2: '%s' em %s — o CLEAN nao tem prop "
                                    "falico nem tronco nu" % (tok, nome)))
    return ach


def resumo_pt(spec):
    fam = ("ela aponta, nada se mexe" if spec["familia"]["id"] == "aponta"
           else "ela despeja %s na cena 1 e %s na cena 2, e a cena 3 e' so' o "
                "copo pronto" % tuple(spec["despejo"]))
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
    # cena 2: mantem os itens da bancada, troca so' a virada — e so' entre as
    # que cabem no teto depois de substituir o orgao (CL13)
    a, b = spec["item_a"], spec["item_b"]
    return "%s. %s. %s" % (a["txt"], b["txt"],
                           rng.choice(_viradas_que_cabem(a, b, o[1])).format(o=o[1]))


EIXOS_QUE_MEXEM_NA_COPY = {}

# ⚠️ `despejo` nao tem pool fixo (o par sai do CL14/CL20 e varia por video),
# entao o teto e' arbitrario: 8 pares antes de zerar. Sem teto proprio a lista
# so' cresceria e o anti-repeticao pararia de rejeitar qualquer coisa.
TETO_LEDGER = {"familia": len(FAMILIAS), "cenario": len(CENARIOS), "despejo": 8}


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
                              ("cenario", spec["cenario"]["id"]),
                              ("despejo", "+".join(spec["despejo"]))):
                u.setdefault(eixo, [])
                if val not in u[eixo]:
                    u[eixo].append(val)
                if len(u[eixo]) >= TETO_LEDGER[eixo]:
                    u[eixo] = [val]
    if not a.dry_run:
        _gravar_ledger(led)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
