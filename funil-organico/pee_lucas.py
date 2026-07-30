#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
pee_lucas.py — randomizador + gerador + linter do AGENTE PEE.

O hook fundador do M15: a mancha molhada na roupa clara, no corredor da loja,
o narrador agachado apontando e a plateia rindo. Fonte: Tanisha Rivers,
reel 1669109991889559 — 1.5K / 583 / 311, 20-50x a media da pagina.

Mesma arquitetura do flagrante_lucas.py:
  1. String travada NUNCA e' redigitada. Mora aqui como constante.
  2. Regra mecanica e' regex, nao julgamento.
  3. Os eixos sao SORTEADOS e a linha sorteada e' EXECUTADA (P1).

Uso:
    python funil-organico/pee_lucas.py --pagina marcus --n 1
    python funil-organico/pee_lucas.py --pagina joe --n 3 --seed 42 --dry-run
    python funil-organico/pee_lucas.py --stats

Doutrina: AGENTE_ED_PEE_V1.md · AGENTE_ED_FLAGRANTE_V1.md (cenas 2-5)
"""

import argparse
import json
import os
import random
import re
import sys

from nucleo_sonoro import sonorizar

AQUI = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(AQUI, ".pee-ledger.json")

TITULO = "AGENTE PEE"
SLUG = "pee"
SUBTITULO = "a mancha pública · gerador offline de prompts Veo"

# ---------------------------------------------------------------------------
# STRINGS TRAVADAS — copia literal da doutrina. NAO REESCREVER, NAO COMPRIMIR.
# ---------------------------------------------------------------------------

# PE2 — o choro nao e' opcional: e' o que transforma a mancha de piada em ruina
CHORO_IMAGE = (
    "head bowed, chin toward his chest, looking down at himself, crying hard — "
    "tears running down both cheeks, eyes red and squeezed shut, mouth twisted "
    "down, shoulders shaking. Both hands fidgeting with the hem of his t-shirt."
)
CHORO_TAKE = (
    "he keeps crying, his shoulders shaking once with a sob, tears still on his "
    "cheeks, and he does not look up. He never speaks and never looks at the camera."
)

# PE3 — o dedo aponta a MANCHA NA ROUPA, nunca a virilha. Roupa e' ancora segura,
# e ninguem encosta nele — e' a construcao que o F12b do FLAGRANTE tomou como
# precedente depois das 4 recusas por agencia.
NARRADOR_IMAGE = (
    "crouched on one knee beside him, right arm extended, index finger pointing "
    "directly at the stain on the fabric, not touching him, face turned toward "
    "the camera, mouth open mid-word"
)
NARRADOR_TAKE = (
    "The crouching man speaks calmly to camera, his pointing finger stays on the "
    "stain on the fabric and never touches the other man. Neither man changes position."
)

# PE4 — plateia ri E aponta (ordem do operador). Sem isso vira acidente triste.
PLATEIA_IMAGE = (
    "four blurred shoppers standing behind them, hands over their mouths "
    "mid-laugh, two of them pointing at him, clearly mocking him"
)

# D1 — o modelo anatomico da cena 2 (mesma string do FLAGRANTE F16)
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

IMOBILIDADE = ("same position, same angle, same shape — completely motionless "
               "for the entire shot.")
NEGACAO_AVE = (" No bird, no goose, no duck, no swan, no snake, no feathers, "
               "no beak, no eyes, no head, nothing alive.")
ANTICELEB = "Ordinary relatable face, not a celebrity."
CAUDA = "iPhone shot, natural grain, no text, no watermark."

ETNIA = {
    "joe": "white American", "ray": "white American", "matt": "white American",
    "marcus": "Black American", "chuck": "Black American",
}

# ---------------------------------------------------------------------------
# POOLS SORTEAVEIS
# ---------------------------------------------------------------------------

# PE5 — sempre lugar publico movimentado, zero marca legivel (P12).
# ⚠️ Nao existe versao privada da mancha: sem plateia nao ha' flagrante.
LOCAIS = [
    {"id": "mercado", "selo": "V",
     "cenario": "a busy big-box supermarket aisle",
     "detalhe": "full shelves on both sides, a shopping cart beside him, "
                "an out-of-focus aisle sign with no readable text",
     "plateia": "shoppers", "plateia_evento": "that store",
     "eco": "the same aisle",
     "luz": "Hard fluorescent overhead light.",
     "audio": "store ambience, laughter, a cart rolling."},
    {"id": "farmacia", "selo": "N",
     "cenario": "a pharmacy aisle",
     "detalhe": "shelves of unlabeled boxes, a counter out of focus behind them",
     "plateia": "customers", "plateia_evento": "that pharmacy",
     "eco": "the same pharmacy counter",
     "luz": "Flat white pharmacy light.",
     "audio": "quiet store ambience, laughter, a scanner beeping."},
    {"id": "fila_caixa", "selo": "V",
     "cenario": "a supermarket checkout line",
     "detalhe": "a conveyor belt with groceries, a register out of focus, "
                "no readable brand names",
     "plateia": "people in line", "plateia_evento": "that checkout line",
     "eco": "the same checkout line",
     "luz": "Hard fluorescent overhead light.",
     "audio": "checkout beeps, laughter, bags rustling."},
    {"id": "ferragens", "selo": "N",
     "cenario": "a hardware store aisle",
     "detalhe": "racks of tools and paint cans, a flatbed cart beside him, "
                "no readable brand names",
     "plateia": "customers", "plateia_evento": "that hardware store",
     "eco": "the same tool aisle",
     "luz": "Cool warehouse overhead light.",
     "audio": "warehouse ambience, laughter, a cart squeaking."},
    {"id": "hortifruti", "selo": "N",
     "cenario": "the produce section of a supermarket",
     "detalhe": "crates of fruit and vegetables, a misting sprayer above them",
     "plateia": "shoppers", "plateia_evento": "that produce aisle",
     "eco": "the same produce aisle",
     "luz": "Bright white produce light.",
     "audio": "store ambience, laughter, the mist sprayer hissing."},
    {"id": "conveniencia", "selo": "N",
     "cenario": "a gas station convenience store",
     "detalhe": "a coffee counter and snack racks, a glass door out of focus, "
                "no readable brand names",
     "plateia": "customers", "plateia_evento": "that gas station",
     "eco": "the same store counter",
     "luz": "Harsh white overhead light.",
     "audio": "store ambience, laughter, a door chime."},
]

# PE1 — a mancha vive do CONTRASTE. Roupa de baixo sempre CLARA.
# ⛔ Calca escura mata o hook: a mancha some e o video perde a evidencia.
ROUPAS = [
    {"id": "khaki_shorts", "peca": "light khaki cargo shorts"},
    {"id": "moletom_cinza", "peca": "light gray sweatpants"},
    {"id": "chino_bege", "peca": "beige chinos"},
    {"id": "linho_creme", "peca": "cream linen trousers"},
    {"id": "calca_areia", "peca": "pale tan work pants"},
]

# Fila de reformulacao do selo 🟡 — se a formulacao 1 recusar, tentar a 2 etc.
MANCHA = [
    "a large dark wet stain spreading across the front of his {peca}",
    "a large dark patch of wet fabric across the front of his {peca}",
    "his {peca} are soaked dark down the front",
]

# Set das cenas 2/3/5 (PE8 — cenas 2-5 sao o FLAGRANTE, luz travada nas 4)
AMBIENTES = [
    {"id": "cozinha", "set": "a plain kitchen, cabinets and a window behind him",
     "bancada": "counter", "curto": "kitchen", "luz": "warm lamp light."},
    {"id": "cozinha_aberta",
     "set": "an open-plan kitchen with an island, a living room out of focus behind him",
     "bancada": "island", "curto": "kitchen",
     "luz": "warm even light from a window frame-left."},
    {"id": "churrasqueira",
     "set": "an outdoor grill station in a backyard, a wooden fence behind him",
     "bancada": "grill counter", "curto": "grill station",
     "luz": "late afternoon sunlight from frame-left."},
    {"id": "varanda",
     "set": "a covered back porch, a screen door and potted plants behind him",
     "bancada": "porch table", "curto": "back porch", "luz": "soft shaded daylight."},
    {"id": "garagem",
     "set": "a clean home garage workshop, pegboard tools on the wall behind him",
     "bancada": "workbench", "curto": "garage workshop",
     "luz": "cool overhead shop light."},
]

# PE9 — contraste ≥3 eixos garantido por CONSTRUCAO: o narrador sempre tem
# cabeleira farta, e' barbeado e nao usa oculos; a vitima e' sempre careca,
# de bigode e de oculos. Nenhuma verificacao necessaria (F4b).
REFS = [
    {"idade": 66, "marca": "full silver hair and a notched left ear",
     "cabelo": "silver", "roupa": "Plain navy crew-neck tee shirt.",
     "roupa_curta": "navy tee shirt"},
    {"idade": 64, "marca": "full gray hair and a clean pale scar through his left eyebrow",
     "cabelo": "gray", "roupa": "Plain olive crew-neck tee shirt.",
     "roupa_curta": "olive tee shirt"},
    {"idade": 68, "marca": "thick white hair and a deep cleft in his chin",
     "cabelo": "white", "roupa": "Plain charcoal crew-neck tee shirt.",
     "roupa_curta": "charcoal tee shirt"},
    {"idade": 65, "marca": "full salt-and-pepper hair and a gold crown on one front tooth",
     "cabelo": "salt-and-pepper", "roupa": "Plain slate blue crew-neck tee shirt.",
     "roupa_curta": "slate blue tee shirt"},
    {"idade": 67, "marca": "thick silver hair and a prominent dark mole on his left cheekbone",
     "cabelo": "silver", "roupa": "Plain black crew-neck tee shirt.",
     "roupa_curta": "black tee shirt"},
]

VITIMAS = [
    {"idade": 63, "marca": "bald man with a thick gray mustache and black-framed glasses",
     "camisa": "a pale blue t-shirt"},
    {"idade": 62, "marca": "bald man with a red mustache and wire-rimmed glasses",
     "camisa": "a white polo shirt"},
    {"idade": 65, "marca": "bald man with a white mustache and thick square glasses",
     "camisa": "a light gray t-shirt"},
    {"idade": 61, "marca": "bald man with a short gray mustache and round wire glasses",
     "camisa": "a pale yellow polo shirt"},
]

MULHERES = [
    {"idade": 58, "payoff": "with chin-length wavy hair, in a red dress"},
    {"idade": 59, "payoff": "with long straight hair, in a navy wrap dress"},
    {"idade": 57, "payoff": "with short curly hair, in an emerald dress"},
    {"idade": 60, "payoff": "with shoulder-length hair, in a burgundy dress"},
]

# prop do payoff (cena 4) — F15: ja' ereto no IMAGE, dimensionado por escala
PROPS = [
    {"id": "banana", "marisco": False,
     "ereto": "a banana upright at shoulder height, held stiff and straight, "
              "as long as her forearm and as thick as her wrist"},
    {"id": "geoduck", "marisco": True,
     "ereto": "a geoduck clam upright by its shell at shoulder height, its siphon "
              "held stiff and straight, as long as her forearm and as thick as her wrist"},
    {"id": "pepino", "marisco": False,
     "ereto": "a cucumber upright at shoulder height, held stiff and straight, "
              "as long as her forearm and as thick as her wrist"},
    {"id": "daikon", "marisco": False,
     "ereto": "a daikon radish upright at shoulder height, held stiff and straight, "
              "as long as her forearm and as thick as her wrist"},
]

# ---------------------------------------------------------------------------
# POOLS DE COPY
# ---------------------------------------------------------------------------

NUCLEO = ["Johnson", "soldier", "pecker", "manhood", "wiener", "tool", "old boy"]

# PE6 ⭐ — a regra mais importante do agente. O hook LIGA o mijo ao orgao NA
# MESMA FALA. Hook so' de mijo REPROVA: o homem com ED nao se reconhece, acha
# que o assunto e' bexiga e rola. Estrutura obrigatoria:
#   fato do mijo + aparte + orgao nomeado + VINCULO afirmado
VINCULOS = ["same thing", "same reason", "and that's why"]

HOOKS = [
    "He peed himself in {evento} because he couldn't hold it in. Poor guy... same thing killed his {o} two years ago.",
    "He wet his pants in {evento} and everybody saw. Poor guy... same reason his {o} quit on him.",
    "He soaked right through in {evento}. Poor guy... same thing that made him leak is why his {o} doesn't work.",
    "He lost it right there in {evento}. Poor guy... and that's why his {o} hasn't worked in two years.",
    "He wet his pants in {evento}. His wife wasn't even surprised. Same reason his {o} stopped working two years back.",
    "He peed his pants in {evento}. His brother in law still tells that story. Same thing shut his {o} down.",
    "He soaked his pants in {evento}. His wife stopped reaching for him two years ago. Same reason his {o} plays dead.",
    "She said it was fine when he peed in {evento}. She says that in bed too. Same reason his {o} quit.",
    "He leaked down his leg in {evento}. Hasn't asked a woman out since the divorce. Same reason his {o} stays down.",
    "He started leaking in {evento}. His wife already told her friends about it. Same reason his {o} does nothing.",
    "He peed right there in {evento}. That was me in 2019. Same reason my {o} went out that year.",
    "He peed in {evento} today. I did the same in 2019. Every man I know has. Same thing took our {o}.",
]

# PE7 — a cena 2 EXPLICA o vinculo que o hook afirmou. Uma causa, dois sintomas.
MECANISMOS = [
    "It's his prostate squeezing the pipe shut. Same pressure keeps the blood out of your {o}.",
    "His prostate is clamping down on the pipe. That same pressure is what starves your {o}.",
    "It's the prostate choking the line. The same squeeze is why your {o} can't fill anymore.",
    "It's not his age. His prostate swelled up and pinched the pipe. Same pinch is why no blood gets to your {o}.",
    "Pills don't touch this. It's his prostate pressing the line flat, and that same press is why your {o} can't fill.",
    "They never told him why, because a fixed man buys nothing. His prostate is sitting on that pipe and shutting your {o} down.",
    "Picture a boot standing on a garden hose. That's his prostate on the line, and it's why your {o} won't fill.",
    "The dripping came first. That's his prostate closing the pipe, and it closes on your {o} a year or two later.",
    "His doctor treated the bladder and never mentioned the rest. Same prostate pressing the same pipe is what took your {o} down.",
    "Blood doesn't reach your {o} anymore. It's the same prostate pinching the same line that sends him to the bathroom all night.",
    "They'll call it two different problems. It's one. His prostate is on the pipe, and that's why your {o} stays down.",
    "I know this one. My prostate grew over the line and closed it. I leaked. Then my {o} went half. Then nothing.",
    "Us guys all have the same prostate leaning on the same line. That's why we drip, and that's why our {o} sleeps through it.",
]

RITUAIS = [
    "That's when his brother gave him the gelatin trick. He stirred it into a glass that same night. Give your {o} one week.",
    "That's when a buddy handed him the gelatin trick. He drank it that same night. Stir it, drink it, and watch your {o} wake up.",
    "That's when his son-in-law gave him the gelatin trick. He mixed it into a glass that night. Do it before your {o} quits for good.",
    "A guy at the barbershop gave him the gelatin trick. He stirred a spoonful into cold water before bed. Do it tonight and your {o} answers by Friday.",
    "An old army buddy called him that night with the gelatin trick. One spoon, warm water, stirred slow. Do the same tonight and give your {o} nine days.",
    "His fishing partner gave him the gelatin trick. He mixed it in the kitchen that same night. Give your {o} two weeks and stop saying sorry in the dark.",
    "His nephew texted him the gelatin trick. He mixed a spoonful into his morning drink. Do the same and your {o} wakes up before you do.",
    "I found the gelatin trick in 2019, brother. I stirred one spoon into cold water that night. Nine days later my {o} answered.",
    "The gelatin trick is what we do at home now. A spoonful in half a glass of cold water. Your {o} shows up before the weekend.",
]

BARREIRAS = [
    "Nobody has to know but her.",
    "No doctor, no pharmacy counter.",
    "You do it in your own kitchen, in about a minute.",
    "Costs less than a cup of coffee.",
    "You never say the words out loud to anybody.",
]

# F1 — o eco deste angulo: ele volta ao mesmo lugar SECO e de cabeca erguida
REDENCOES = [
    "Nineteen days later he walked back into {eco} dry, head up. Now she's the one bragging about his {o}. {barreira}",
    "Nineteen days later he was back in {eco}, dry and standing tall. Now she won't stop talking about his {o}. {barreira}",
    "Twenty six days later he was back in {eco} dry, head high. She says his {o} wakes up before the alarm. {barreira}",
    "Sixteen days later he walked into {eco} dry, head up. His {o} left her needing a minute to catch her breath. {barreira}",
    "Eighteen days later he was back in {eco} dry, chin up. She reaches for him first now. His {o} never quits. {barreira}",
    "Twenty four days later he walked into {eco} dry, head up. Now she asks for a night off from his {o}. {barreira}",
]

GATES = [
    "Follow me first, brother.",
    "Follow me first or I can't find your comment.",
    "Hit follow first, or Facebook won't deliver it.",
]

CTAS = [
    "Comment GELATIN and I'll send you the only one I trust tonight. {gate}",
    "Comment GELATIN and I'll send you that exact one today. {gate}",
    "Comment GELATIN and I'll send you where to get the right one. {gate}",
    "Comment GELATIN now and thank me Friday night. I'll send it over today. {gate}",
    "Comment GELATIN tonight. Somebody always reports this and the video goes down by morning. {gate}",
    "One word. Comment GELATIN and it's in your inbox tonight. {gate}",
    "Comment GELATIN and I'll send you the source. I can't name it here. {gate}",
    "Comment GELATIN and I'll send the same one he used. {gate}",
    "Comment GELATIN. The store stuff did nothing for you. I'll send the real one. {gate}",
    "Comment GELATIN and I'll send you the one we use at home. {gate}",
]

# ---------------------------------------------------------------------------
# LINTER
# ---------------------------------------------------------------------------

BANIDOS_TAKE = {
    "stiff": "adjetivo de estado em prompt de movimento derruba o video",
    "limp": "idem", "sags": "idem",
    "pulse": "tumescencia — IMAGE passa e o VIDEO e' recusado",
    "throb": "idem", "swelling": "idem",
    "engorged": "vocabulario anatomico — recusa",
    "geoduck": "so' no IMAGE; no TAKE usar 'the clam'",
    "neck": "no geoduck e' 'siphon', nunca 'neck'",
}
BANIDOS_IMAGE = {
    # 'big(?!-box)': o banimento e' de DIMENSAO de prop. Sem o lookahead, o
    # cenario 'big-box supermarket' era acusado em todo sorteio do local mercado.
    "big(?!-box)": "adjetivo nao dimensiona — o Veo normaliza",
    "huge": "idem", "engorged": "vocabulario anatomico — recusa", "veins": "idem",
}

BANIDOS_GLOBAL = {
    "the victim": "rotulo que significa dano — municao pro classificador",
    "the narrator": "trocar por relacao nomeada",
}
BANIDOS_CTA = {"BOOK": "quebra a automacao DM", "YES": "quebra a automacao DM"}

# roupa escura mata o hook (PE1) — o pool ja' impede, o linter e' rede
ROUPA_ESCURA = ["dark jeans", "black pants", "navy trousers", "dark trousers",
                "black shorts", "dark slacks"]

TETO_FALA = {1: 24, 2: 26, 3: 30, 4: 36, 5: 24}


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
        rep = sorted({u for u in usados if usados.count(u) > 1})
        achados.append(("AVISO", "substantivo repetido no video: %s" % rep))

    # PE6 — o hook precisa do MIJO + do ORGAO + do VINCULO, na mesma fala
    h = falas[0].lower()
    tem_mijo = any(t in h for t in ("peed", "wet his", "soaked", "leak", "lost it"))
    tem_orgao = any(n.lower() in h for n in NUCLEO)
    tem_vinculo = any(v in h for v in VINCULOS)
    if not tem_mijo:
        achados.append(("ERRO", "PE6: o hook nao diz o mijo"))
    if not tem_orgao:
        achados.append(("ERRO", "PE6: o hook nao nomeia o orgao — hook so' de "
                                "mijo REPROVA, o alvo com ED nao se reconhece"))
    if not tem_vinculo:
        achados.append(("ERRO", "PE6: falta o VINCULO afirmado no hook "
                                "(%s)" % " / ".join(VINCULOS)))

    # PE7 — a cena 2 explica o mecanismo
    c2 = falas[1].lower()
    if "prostate" not in c2:
        achados.append(("ERRO", "PE7: a cena 2 nao explica o mecanismo "
                                "(prostata apertando o cano)"))

    # tetos de fala
    total = 0
    for i, fala in enumerate(falas, 1):
        n = _palavras(fala)
        total += n
        if n > TETO_FALA[i]:
            achados.append(("AVISO", "cena %d com %d palavras (teto %d) — cortar "
                                     "UMA frase, nao reescrever menor" % (i, n, TETO_FALA[i])))
    if total > 125:
        achados.append(("AVISO", "video com %d palavras (alvo ~90-105)" % total))

    corpo = " ".join(falas).lower()
    if "gelatin trick" not in corpo:
        achados.append(("ERRO", "expressao literal 'gelatin trick' ausente"))
    if "gelatin" not in falas[4].lower():
        achados.append(("ERRO", "CTA da cena 5 sem a keyword GELATIN"))
    for tok, motivo in BANIDOS_CTA.items():
        if re.search(r"\b%s\b" % tok, falas[4]):   # o linter confere a copy LIMPA
            achados.append(("ERRO", "CTA usa '%s' — %s" % (tok, motivo)))

    # tokens banidos por bloco
    for nome, txt in blocos.items():
        # O banimento de vocabulario de estado (stiff/limp/sags...) vale para a
        # DIRECAO DE CENA, nao para a fala: a falha documentada foi um prompt de
        # movimento descrevendo o prop. Estado dito pelo narrador e' copy normal
        # e validada ("can't get hard", "plays dead"). Entao so' varremos o que
        # vem antes de "Dialogue:".
        direcao = txt.split(chr(10) + "Dialogue:")[0]
        baixo = direcao.lower()
        tabela = BANIDOS_TAKE if nome.startswith("TAKE") else BANIDOS_IMAGE
        for tok, motivo in tabela.items():
            if re.search(r"\b%s\b" % tok, baixo):
                achados.append(("ERRO", "%s contem '%s' — %s" % (nome, tok, motivo)))
        for tok, motivo in BANIDOS_GLOBAL.items():
            if tok in baixo:
                achados.append(("ERRO", "%s contem '%s' — %s" % (nome, tok, motivo)))

    # PE1 — roupa clara, sempre
    i1 = blocos["IMAGE 01/05"].lower()
    for escura in ROUPA_ESCURA:
        if escura in i1:
            achados.append(("ERRO", "PE1: roupa escura ('%s') mata o contraste "
                                    "da mancha" % escura))

    # blocos travados integros
    for nome, s, rot in (("IMAGE 01/05", CHORO_IMAGE, "choro PE2"),
                         ("IMAGE 01/05", NARRADOR_IMAGE, "narrador PE3"),
                         ("IMAGE 01/05", PLATEIA_IMAGE, "plateia PE4"),
                         ("IMAGE 02/05", D1_IMAGE, "D1"),
                         ("TAKE 02/05", D1_TAKE, "D1 no take")):
        if s not in blocos[nome]:
            achados.append(("ERRO", "%s sem a string travada: %s" % (nome, rot)))

    if "motionless" not in blocos["TAKE 04/05"].lower():
        achados.append(("ERRO", "TAKE 04 sem declaracao de imobilidade do prop"))

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
    local = _evitando(rng, LOCAIS, hist.get("local", [])[-3:])
    roupa = _evitando(rng, ROUPAS, hist.get("roupa", [])[-2:])
    amb = _evitando(rng, AMBIENTES, hist.get("ambiente", [])[-2:])
    prop = _evitando(rng, PROPS, hist.get("prop", [])[-2:])
    ref, vit, mul = rng.choice(REFS), rng.choice(VITIMAS), rng.choice(MULHERES)

    orgaos = rng.sample(NUCLEO, 4)
    falas = [
        rng.choice(HOOKS).format(evento=local["plateia_evento"], o=orgaos[0]),
        rng.choice(MECANISMOS).format(o=orgaos[1]),
        rng.choice(RITUAIS).format(o=orgaos[2]),
        rng.choice(REDENCOES).format(eco=local["eco"], o=orgaos[3],
                                     barreira=rng.choice(BARREIRAS)),
        rng.choice(CTAS).format(gate=rng.choice(GATES)),
    ]
    return {"pagina": pagina, "local": local, "roupa": roupa, "ambiente": amb,
            "prop": prop, "ref": ref, "vitima": vit, "mulher": mul,
            "mancha": MANCHA[0], "falas": falas}


def _gravar_ledger(ledger, spec):
    p = ledger.setdefault(spec["pagina"], {})
    for eixo, val in (("local", spec["local"]["id"]), ("roupa", spec["roupa"]["id"]),
                      ("ambiente", spec["ambiente"]["id"]), ("prop", spec["prop"]["id"])):
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
    prop, loc, amb, roupa = spec["prop"], spec["local"], spec["ambiente"], spec["roupa"]
    falas = spec["falas"]
    luz = amb["luz"]
    neg = NEGACAO_AVE if prop["marisco"] else ""
    mancha = spec["mancha"].format(peca=roupa["peca"])

    b = {}

    b["BLOCO 0 (REF)"] = (
        "Photo of a real person, a %d-year-old %s man, chest up, facing camera, "
        "calm expression. Lean muscular build, chest and shoulders visible. %s. "
        "%s %s Plain gray background, soft light. No text, no watermark."
        % (ref["idade"], et, ref["marca"].capitalize(), ref["roupa"], ANTICELEB)
    )

    b["IMAGE 01/05"] = (
        "IMAGE 01/05: Medium shot in %s, %s. Standing in the middle is a "
        "%d-year-old %s %s, wearing %s, with %s. He stands there, %s "
        "Beside him is a %d-year-old %s man with %s, %s, and %s. "
        "%s %s %s"
        % (loc["cenario"], loc["detalhe"], vit["idade"], et, vit["marca"],
           vit["camisa"], mancha, CHORO_IMAGE,
           ref["idade"], et, ref["marca"], NARRADOR_IMAGE, PLATEIA_IMAGE,
           ANTICELEB, loc["luz"], CAUDA)
    )

    b["IMAGE 02/05"] = (
        "IMAGE 02/05: Medium close-up in %s. The same %d-year-old %s man, %s, "
        "%s, stands behind the %s, leaning slightly toward the camera, mouth "
        "open mid-word. %s He is alone in frame. %s %s"
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
        "%d-year-old %s %s, now in a clean white shirt and dry trousers, sits in "
        "an armchair grinning, head up, a total reversal of his bowed posture in "
        "the store. A %d-year-old %s woman %s sits sideways on his knee, the way "
        "a newlywed poses for a photograph, arm around him, laughing. In her free "
        "hand she holds %s.%s %s"
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
        "TAKE 01/05: Animate the image exactly. Handheld iPhone, slight sway, no "
        "cuts. %s The standing man does not move from where he is — %s Behind "
        "them the blurred %s keep laughing, two still pointing. Only the "
        "crouching man speaks.\nDialogue: \"%s\"\nAudio: %s No music."
        % (NARRADOR_TAKE, CHORO_TAKE, loc["plateia"], sonorizar(falas[0]), loc["audio"])
    )

    b["TAKE 02/05"] = (
        "TAKE 02/05: Animate the image exactly. Handheld iPhone, slight sway, no "
        "cuts. %s He is alone in frame, speaking with conviction.\n"
        "Dialogue: \"%s\"\nAudio: quiet room tone. No music." % (D1_TAKE, sonorizar(falas[1]))
    )

    b["TAKE 03/05"] = (
        "TAKE 03/05: Animate the image exactly. Handheld iPhone, slight sway, no "
        "cuts. Hands finish pouring the sachet, stir the glass in slow circles. "
        "No face enters frame.\nDialogue: \"%s\"\n"
        "Audio: spoon clinking glass, quiet room tone. No music." % sonorizar(falas[2])
    )

    b["TAKE 04/05"] = (
        "TAKE 04/05: Animate the image exactly. Handheld iPhone, slight sway, no "
        "cuts. The man laughs silently, head tipping back. The woman laughs, "
        "tightens her arm around him; her other hand stays exactly where it is, "
        "holding it motionless the entire shot. Neither changes position. A man's "
        "voice speaks over the scene; the couple stays silent.\n"
        "Dialogue: \"%s\"\nAudio: quiet room tone, soft laughter. No music." % sonorizar(falas[3])
    )

    b["TAKE 05/05"] = (
        "TAKE 05/05: Animate the image exactly. Handheld iPhone, slight sway, no "
        "cuts. He looks at camera, calm, points his finger, speaks evenly.\n"
        "Dialogue: \"%s\"\nAudio: quiet room tone. No music." % sonorizar(falas[4])
    )

    return b


# ---------------------------------------------------------------------------
# INTERFACE (consumido por ui_agente.py)
# ---------------------------------------------------------------------------

EIXOS_UI = [
    ("local", "LOCAL", "LOCAIS", "id"),
    ("roupa", "ROUPA", "ROUPAS", "peca"),
    ("ambiente", "AMBIENTE", "AMBIENTES", "id"),
    ("prop", "PROP CENA 4", "PROPS", "id"),
    ("ref", "NARRADOR", "REFS", "marca"),
    ("vitima", "VÍTIMA", "VITIMAS", "marca"),
    ("mulher", "MULHER", "MULHERES", "payoff"),
]

CENAS_UI = ["1 · A MANCHA + O VÍNCULO", "2 · O MECANISMO", "3 · RITUAL",
            "4 · REDENÇÃO", "5 · CTA"]

PT_LOCAL = {
    "mercado": "No corredor do mercado", "farmacia": "No corredor da farmácia",
    "fila_caixa": "Na fila do caixa", "ferragens": "Na loja de ferragens",
    "hortifruti": "No hortifrúti", "conveniencia": "Na loja de conveniência",
}
PT_AMB = {"cozinha": "na cozinha", "cozinha_aberta": "na cozinha com ilha",
          "churrasqueira": "na área de churrasco", "varanda": "na varanda coberta",
          "garagem": "na garagem oficina"}


def resumo_pt(spec):
    et = "branca" if "white" in ETNIA[spec["pagina"]] else "negra"
    return ("%s, o homem se mija na calça clara e chora olhando a própria mancha, "
            "enquanto o narrador agacha e aponta e a plateia ri e aponta. As cenas "
            "2 a 5 rodam %s. Elenco de pele %s."
            % (PT_LOCAL.get(spec["local"]["id"], "Num lugar público"),
               PT_AMB.get(spec["ambiente"]["id"], "no set interno"), et))


def _recopiar_local(spec, rng):
    """O local alimenta o hook e o eco da cena 4 — trocar um exige reescrever."""
    loc = spec["local"]
    baixo0, baixo3 = spec["falas"][0].lower(), spec["falas"][3].lower()
    o0 = next((n for n in NUCLEO if n.lower() in baixo0), "Johnson")
    o3 = next((n for n in NUCLEO if n.lower() in baixo3), "manhood")
    spec["falas"][0] = rng.choice(HOOKS).format(evento=loc["plateia_evento"], o=o0)
    spec["falas"][3] = rng.choice(REDENCOES).format(
        eco=loc["eco"], o=o3, barreira=rng.choice(BARREIRAS))


def nova_fala(spec, i, rng):
    """Re-sorteia a fala da cena i (0-4) mantendo o substantivo-nucleo daquela cena."""
    o = next((n for n in NUCLEO if n.lower() in spec["falas"][i].lower()), "Johnson")
    loc = spec["local"]
    if i == 0:
        return rng.choice(HOOKS).format(evento=loc["plateia_evento"], o=o)
    if i == 1:
        return rng.choice(MECANISMOS).format(o=o)
    if i == 2:
        return rng.choice(RITUAIS).format(o=o)
    if i == 3:
        return rng.choice(REDENCOES).format(eco=loc["eco"], o=o,
                                            barreira=rng.choice(BARREIRAS))
    return rng.choice(CTAS).format(gate=rng.choice(GATES))

EIXOS_QUE_MEXEM_NA_COPY = {"local": _recopiar_local}


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def imprimir(spec, blocos, achados):
    print("=" * 72)
    print("SPEC SORTEADA — pagina %s | local %s (%s) | roupa %s | set %s | prop %s"
          % (spec["pagina"], spec["local"]["id"], spec["local"]["selo"],
             spec["roupa"]["id"], spec["ambiente"]["id"], spec["prop"]["id"]))
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
    ap = argparse.ArgumentParser(description="Randomizador do agente PEE")
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
