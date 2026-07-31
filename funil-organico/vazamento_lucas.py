#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
vazamento_lucas.py — randomizador + gerador + linter do AGENTE VAZAMENTO.

O REF e' o corpo-prova: sem camisa, musculoso aos ~70, segurando o geoduck
gigante que VAZA — e entregando uma receita de supermercado que ele mesmo
declara incompleta sem o mecanismo. Fonte: Kofi&Simba, reel 1555163349606149
(703 reacoes / 254 comentarios / 36 shares — 254 comentarios e' conversao de
comentario, o KPI do funil).

Mesma arquitetura do flagrante_lucas.py / pee_lucas.py:
  1. String travada NUNCA e' redigitada. Mora aqui como constante.
  2. Regra mecanica e' regex, nao julgamento.
  3. Os eixos sao SORTEADOS e a linha sorteada e' EXECUTADA (P1).

Uso:
    python funil-organico/vazamento_lucas.py --pagina chuck --n 1
    python funil-organico/vazamento_lucas.py --pagina joe --n 3 --seed 42 --dry-run
    python funil-organico/vazamento_lucas.py --stats

Doutrina: AGENTE_ED_VAZAMENTO_V1.md
"""

import argparse
import json
import os
import random
import re
import sys

from nucleo_sonoro import sonorizar

AQUI = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(AQUI, ".vazamento-ledger.json")

TITULO = "AGENTE VAZAMENTO"
SLUG = "vazamento"
SUBTITULO = "o corpo-prova e a receita incompleta · gerador offline de prompts Veo"

# ---------------------------------------------------------------------------
# STRINGS TRAVADAS — copia literal da doutrina. NAO REESCREVER, NAO COMPRIMIR.
# ---------------------------------------------------------------------------

# V1 — o geoduck e' GIGANTE, MOLE e seguro com AS DUAS MAOS (ordem do operador).
# Dimensao por ESCALA CORPORAL, nunca por adjetivo (large/big sao normalizados).
GEODUCK_IMAGE = (
    "He holds a very large geoduck clam with both hands against his bare chest, "
    "gripping the pale ridged shell. Its siphon hangs straight down over his lap, "
    "completely soft and slack, as long as his forearm and as thick as his wrist, "
    "drooping under its own weight with a rounded blunt tip, pale tan, its surface "
    "dull and slightly wrinkled. No bird, no goose, no duck, no swan, no snake, no "
    "feathers, no beak, no eyes, no head, nothing alive."
)

# V1 no TAKE — o estado vive no IMAGE; vocabulario firme<->murcho em prompt de
# movimento derruba o video (regra dos dois lados). ⛔ nunca 'geoduck', nunca 'neck'.
GEODUCK_TAKE = (
    "The clam stays exactly as it appears in the first frame — same position, same "
    "angle, same shape — completely motionless for the entire shot. It is a still "
    "object and nothing about it changes. No bird, no goose, no duck, no swan, no "
    "snake, no worm, no tentacle, no feathers, no beak, no eyes, no head, nothing "
    "alive, nothing with a face."
)

# V2 ⭐ — o vazamento e' a assinatura, e se descreve como SALMOURA DE MARISCO.
# As 4 pecas que ancoram em peixaria e nao em corpo: clear briny liquid, brine,
# fresh clam, fishmonger's counter. ⛔ leaking / white / milky / fluido corporal.
VAZAMENTO_IMAGE = (
    "A thin trickle of clear briny liquid runs from the tip of the siphon and pools "
    "in a small puddle on the wooden table below, the way brine drains from a fresh "
    "clam on a fishmonger's counter."
)
VAZAMENTO_TAKE = "The puddle on the table slowly widens; the clam itself never moves."

# Fila de fallback do V2 (selo 🟡 nao testado) — se recusar, tentar na ordem
VAZAMENTO_FALLBACK = [
    "a small puddle of clear brine already pooled on the table beneath it",
    "the shell and siphon glisten, wet with brine",
]

ANTICELEB = "Ordinary relatable face, not a celebrity."
CAUDA = "iPhone shot, natural grain, no text, no watermark."

ETNIA = {
    "joe": "white American", "ray": "white American", "matt": "white American",
    "marcus": "Black American", "chuck": "Black American",
}

# ---------------------------------------------------------------------------
# POOLS SORTEAVEIS
# ---------------------------------------------------------------------------

# V9 — dois settings, troca na cena 2. Cena 1 INTERIOR, cenas 2-5 EXTERIOR.
# V10 — a bandeira dos EUA aparece nos DOIS settings.
COZINHAS = [
    {"id": "cozinha_branca",
     "set": "a modest American kitchen, white cabinets, a stainless steel "
            "refrigerator, a small American flag on a stand on the counter",
     "luz": "Cool white overhead kitchen light, flat and even."},
    {"id": "cozinha_carvalho",
     "set": "a modest American kitchen, oak cabinets, a hanging bunch of dried "
            "herbs, a small American flag on a stand beside the bread box",
     "luz": "Warm overhead kitchen light, slight shadow under the chin."},
    {"id": "cozinha_creme",
     "set": "a modest American kitchen, cream-painted cabinets, a bowl of lemons, "
            "a small American flag on a stand by the window",
     "luz": "Cool white overhead kitchen light, flat and even."},
]

QUINTAIS = [
    {"id": "cerca_madeira",
     "set": "the backyard of a modest American home, a wooden privacy fence, mowed "
            "grass, a small American flag mounted by the back door, potted flowers",
     "luz": "late afternoon golden sunlight from frame-left, long soft shadows."},
    {"id": "churrasqueira",
     "set": "the backyard of a modest American home, a chain-link fence with hedges, "
            "a covered charcoal grill, a small American flag by the back door",
     "luz": "late afternoon golden sunlight from frame-right, long soft shadows."},
    {"id": "lenha",
     "set": "the backyard of a modest American home, a low wooden fence, a stack of "
            "firewood against the wall, a small American flag by the back door",
     "luz": "late afternoon golden sunlight from frame-left, long soft shadows."},
    {"id": "varanda_quintal",
     "set": "the backyard of a modest American home, a wicker sofa with cushions, "
            "dry golden grass, a small American flag mounted by the back door",
     "luz": "late afternoon golden sunlight from frame-right, warm and directional."},
]

# V3 ⭐ — o REF e' o corpo-prova: tronco NU, musculatura por GRUPO NOMEADO
# (`muscular` sozinho nao renderiza). ⛔ sem barriga proeminente: aqui ele e' o
# DEPOIS ambulante. Marca facial obrigatoria, num rosto saudavel (nunca avaria).
REFS = [
    {"idade": 69, "musculo": "a lean hard-muscled build with visible definition in "
                             "the chest, shoulders and arms",
     "marca": "short silver hair swept back and a clean pale scar through his left eyebrow",
     "roupa2": "a faded olive linen shirt unbuttoned halfway, sleeves rolled to the elbows"},
    {"idade": 71, "musculo": "a powerfully built muscular frame with a broad chest "
                             "and thick arms",
     "marca": "thick silver-white hair parted on the side and a prominent dark mole "
              "on his right cheekbone",
     "roupa2": "a light blue short-sleeve work shirt, open at the collar"},
    {"idade": 68, "musculo": "a heavy-set powerful build, barrel chest and thick "
                             "muscular forearms",
     "marca": "close-cropped hair with a bold white streak on the left side and a "
              "gold crown on his upper right front tooth",
     "roupa2": "a mustard-yellow short-sleeve button-down shirt"},
    {"idade": 70, "musculo": "a tall broad-shouldered muscular build with a wide "
                             "back and strong neck",
     "marca": "thick gray hair and a deep vertical cleft in his chin",
     "roupa2": "a rust-red short-sleeve snap-button shirt, open at the collar"},
    {"idade": 67, "musculo": "a lean hard-muscled build with visible definition in "
                             "the chest, shoulders and arms",
     "marca": "full silver hair and a small notch missing from the top of his left ear",
     "roupa2": "a faded denim shirt with the sleeves cut off"},
]

# V12 ⭐ — a mulher de 30-35 na cena 4, SEMPRE. Linda, abracada em pe, muda, rindo.
# A idade dos DOIS vai escrita em toda mencao (falha documentada: classificador
# barra por menores sem isso). ⛔ nunca colo, nunca joelho neste agente.
MULHERES = [
    {"idade": 33, "desc": "long chestnut-brown wavy hair past her shoulders, a small "
                          "beauty mark on her left jaw, a fitted coral summer dress"},
    {"idade": 34, "desc": "long dark blonde hair past her shoulders, a small notch in "
                          "her right eyebrow, a fitted white tank top and blue jeans"},
    {"idade": 32, "desc": "long braided hair gathered over one shoulder, a small beauty "
                          "mark high on her right cheekbone, a fitted emerald summer dress"},
    {"idade": 35, "desc": "long straight black hair past her waist, a small dark beauty "
                          "mark below her left eye, a fitted turquoise summer dress"},
]

# Prop do payoff (cena 4) — F15: JA' ereto no IMAGE, dimensionado por escala
# corporal. ⛔ nunca `engorged`/`veins`/`a third thicker` (recusa documentada).
PROPS_PAYOFF = [
    {"id": "daikon", "desc": "a very large daikon radish as long as his forearm and "
                             "as thick as his wrist, stiff and straight, its surface "
                             "taut and pale, reaching above his shoulder"},
    {"id": "pepino", "desc": "a very large cucumber as long as his forearm and as "
                             "thick as his wrist, stiff and straight, its surface taut "
                             "and glossy, reaching above his shoulder"},
    {"id": "banana", "desc": "a very large banana as long as his forearm and as thick "
                             "as his wrist, stiff and straight, its surface taut, "
                             "reaching above his shoulder"},
    {"id": "mandioca", "desc": "a very large cassava root as long as his forearm and "
                               "as thick as his wrist, stiff and straight, its surface "
                               "taut and pale, reaching above his shoulder"},
]

# ---------------------------------------------------------------------------
# POOLS DE COPY
# ---------------------------------------------------------------------------

NUCLEO = ["Johnson", "soldier", "pecker", "manhood", "wiener", "tool", "old boy"]

# O hook herda a ECONOMIA da fonte: orgao nomeado + mecanismo + comando, em <=8s
HOOKS = [
    "This is what happens to your {o} when American men ignore blood flow too long. Do this tonight.",
    "Your {o} stopped showing up years ago. That's blood flow choked off. Do this before it's too late.",
    "This is what ignoring blood flow does to your {o}. Fix yours tonight, brother.",
    "American men let this happen to their {o} every day. Blood flow. Do this before it's too late.",
    "Your wife stopped reaching for you. Nobody told you your {o} lost blood flow. Fix it tonight.",
    "Doctors billed you for twenty years and never once checked the blood flow to your {o}. Do this tonight.",
    "She already knows your {o} won't work tonight. That's blood flow choked off. Fix it before Friday.",
    "You apologized in the dark again last night. Blood flow quit reaching your {o}. Do this tonight.",
    "She said it's okay, honey, and rolled over. It's blood flow, not you. Fix your {o} tonight.",
    "You plan your nights around a pill that never opened the blood flow to your {o}. Do this tonight instead.",
    "Nobody in my house buys those pills anymore. Blood flow quit your {o}, brother. Stop paying them.",
    "I went four years without finishing once, brother. Blood flow quit my {o}. Give me sixty seconds.",
    "For four years I told my wife I was just tired. Blood flow quit my {o}. Don't lie to her.",
    "I lost my confidence. I stopped touching my wife. Blood flow quit my {o}. Your turn's coming.",
]

# V5 — a receita e' gelatin + baking soda, PREPARADA NA TELA pelas maos dele.
# ⚠️ topica ou de preparo, nunca dose medica: sem miligramas, sem cura.
RECEITAS = [
    "Men, stir a spoonful of gelatin into baking soda for one minute. Do it before your {o} quits for good.",
    "Men, mix a spoonful of gelatin with baking soda in a jar. Stir it. Your {o} is about to wake back up.",
    "Men, stir gelatin into baking soda, one full minute. That's the first half of getting your {o} back.",
    "Men, stir gelatin and baking soda in a coffee mug while she's asleep. She doesn't need to know why your {o} came back.",
    "Men, pour the baking soda over the gelatin and stir it one full minute. She's still asking. Your {o} still isn't answering.",
    "Men, mix gelatin into baking soda and stir until it's smooth. Do it tonight and check your {o} in the morning.",
    "Men, one spoon of gelatin, one spoon of baking soda, stir. Takes a minute. Your {o} took twenty years to quit.",
    "Men, mix gelatin with baking soda and stir. Costs a dollar. The pill people charged you thirty a month for your {o}.",
    "Men, mix gelatin with baking soda in a glass and stir. Do it before Saturday, before she finds out your {o} doesn't work.",
    "Men, stir gelatin into baking soda right on the counter. Your {o} worked fine at thirty. Get it back.",
    "Every man in my family keeps gelatin and baking soda on the counter. Mix them, stir a minute. Your {o} needs both.",
    "Us guys don't order anything. Gelatin, baking soda, a spoon. Stir one minute. Nobody has to know your {o} needs it.",
    "We keep gelatin next to the coffee in this house. Stir a spoonful into baking soda. Your {o} gets one minute of your day.",
]

# V6 ⭐⭐ — a regra central: a receita que ele acabou de dar e' INCOMPLETA.
# (1) a negacao vem antes da solucao, (2) o orgao e' nomeado na mesma frase,
# (3) usa o sim que o espectador ja' deu. ⛔ nunca `not just any gelatin`.
VIRADAS = [
    "But here's what most guys never find out. Without the gelatin trick, baking soda alone does nothing for your {o}. It's not age, brother — your blood flow got choked off.",
    "But here's the thing most guys never realize. Without the gelatin trick, baking soda on its own does nothing for your {o}. It's not age. Your blood flow got choked off.",
    "You didn't fail, brother. Nobody gave you the other half. Without the gelatin trick, baking soda does nothing for your {o}. It's not age — your blood flow got choked off.",
    "Stop right there. Without the gelatin trick, that baking soda is half a recipe and your {o} stays down. It's not age. Your blood flow got squeezed shut.",
    "I gave you half on purpose. Without the gelatin trick, that recipe does nothing for your {o}. It's not age, brother — your blood flow got pinched off decades ago.",
    "Now don't go telling the guys yet. Without the gelatin trick, baking soda by itself does nothing for your {o}. It's not age, brother. Your blood flow got shut down.",
    "You're one ingredient short, brother. Without the gelatin trick, baking soda does nothing for your {o}. It's not age. Your blood flow got choked off while you waited.",
    "She's waited two years already. Without the gelatin trick, baking soda does nothing for your {o}, and she waits two more. It's not age — your blood flow got choked off.",
    "I mixed that same spoon for a year and nothing moved. Without the gelatin trick, baking soda does nothing for your {o}. It's not age, brother — your blood flow got clamped shut.",
    "I did this wrong first. I quit for a month. I told my wife it was over. Without the gelatin trick, baking soda does nothing for your {o} — your blood flow stays shut.",
    "Every man I gave this to called me back angry. Without the gelatin trick, baking soda does nothing for your {o}. It's not age — your blood flow got sealed off years back.",
]

# V12 — a copy da cena 4 e' DIRETA sobre ela, com o substantivo-nucleo.
# ⛔ reacao generica (`life is good again`) nao conta.
PROVAS = [
    "She's half my age and she can't keep her hands off my {o}. Thirty-{n} years old and she calls me every night. {barreira}",
    "She's {n_ext} and she can't keep her hands off my {o}. Half my age, and she's the one who won't wait. {barreira}",
    "Thirty-{n} years old and she told her girlfriends about my {o}. Half my age, and I'm what she brags about. {barreira}",
    "She's {n_ext}. Half my age, and she asked me for a break. My {o} doesn't tap out first anymore. {barreira}",
    "Thirty-{n} years old and she reaches for me first now. Half my age, and my {o} is why she stays. {barreira}",
    "She's {n_ext} and she drives an hour over on a Tuesday night. Half my age, and my {o} is why. {barreira}",
    "She's {n_ext}, half my age, and she needed a minute to catch her breath. My {o} did that. {barreira}",
    "Us guys pass this around now. My {o} works and she's {n_ext}. She couldn't sit still the next day. Thirty-{n} years old. {barreira}",
]

BARREIRAS = [
    "A trick you can do from the comfort of your own home.",
    "No doctor, no pharmacy counter, nobody has to know.",
    "You do it in your own kitchen, in about a minute.",
    "Costs less than a cup of coffee and nobody sees you buy it.",
    "Nothing to fill, nothing to explain to anybody.",
]

PACING = [
    "Next Friday night, when she asks what changed, you'll remember this video.",
    "Next Friday night she'll ask what changed. You'll remember this.",
]

GATES = [
    "Make sure you're following me first, or I won't have any way to find your comment, brother.",
    "Follow me first, or Facebook can't deliver it, brother.",
    "Hit follow right now, or my message never lands.",
]

CTAS = ["{pacing} Comment gelatin, and I'll send you the only one I trust today. {gate}",
    "{pacing} Comment gelatin, and I'll send you the exact one I use, tonight. {gate}",
    "{pacing} Comment gelatin, and I'll send you where I get mine. {gate}",
    "{pacing} Comment gelatin, and I'll send you the full video today. {gate}",
    "{pacing} Comment gelatin, and I'll send you what to buy and where. {gate}",
    "{pacing} Comment gelatin, and I'll send the whole thing over before this comes down. {gate}",
    "{pacing} Comment gelatin, and I'll send you the gelatin trick tonight. {gate}",
    "{pacing} Comment gelatin, and I'll send you the other half of that recipe. {gate}",
    "{pacing} Comment gelatin, and I'll send you the same one I sent my brother. {gate}",
    "{pacing} Comment gelatin, and I'll send you the one we use at my house. I can't name it here. {gate}",
    "{pacing} I waited four years to find this, brother. Comment gelatin, and you won't wait four days. {gate}",
    "{pacing} Comment gelatin, and I'll send you what my own wife went looking for. She found it before I did. {gate}",
]

# ---------------------------------------------------------------------------
# LINTER
# ---------------------------------------------------------------------------

BANIDOS_TAKE = {
    "geoduck": "so' no IMAGE; no TAKE usar 'the clam' (V1)",
    "neck": "no geoduck e' 'siphon', nunca 'neck' (V1)",
    "stiff": "adjetivo de estado em prompt de movimento derruba o video",
    "limp": "idem", "sags": "idem", "pulse": "tumescencia — o VIDEO e' recusado",
    "throb": "idem", "swelling": "idem",
}
BANIDOS_IMAGE = {
    "big": "adjetivo nao dimensiona — o Veo normaliza (V1)",
    "huge": "idem", "engorged": "vocabulario anatomico — recusa", "veins": "idem",
}
# V2 — o vazamento nunca sai do dominio da peixaria
BANIDOS_VAZAMENTO = {
    "leaking": "verbo do prop — usar o vocabulario de salmoura (V2)",
    "milky": "a cor faz a leitura virar outra coisa (V2)",
    "cloudy": "idem (V2)",
    "dripping fluid": "sem qualificar — ancorar em peixaria (V2)",
}
# V7 — zero ingrediente-fantasma importado da fonte
BANIDOS_FONTE = {
    "horse gelatin": "ingrediente-fantasma do Kofi — nosso mecanismo e' o gelatin trick (V7)",
    "equine collagen": "idem (V7)",
}
BANIDOS_GLOBAL = {"the victim": "rotulo que significa dano",
                  "the narrator": "trocar por relacao nomeada"}
BANIDOS_CTA = {"BOOK": "quebra a automacao DM", "YES": "quebra a automacao DM"}

# cena 5 com teto folgado (40): future pacing + GELATIN + follow-gate sao
# TRES obrigatorios e nao cabem nas 16-20 palavras do arsenal.
TETO_FALA = {1: 20, 2: 24, 3: 34, 4: 32, 5: 40}


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
        achados.append(("AVISO", "substantivo repetido no video: %s"
                        % sorted({u for u in usados if usados.count(u) > 1})))

    # V6 — a virada na forma travada: negacao ANTES da solucao, orgao na frase
    c3 = falas[2].lower()
    if "without the gelatin trick" not in c3:
        achados.append(("ERRO", "V6: a cena 3 nao tem a negacao 'without the "
                                "gelatin trick' — a negacao vem ANTES da solucao"))
    if not any(n.lower() in c3 for n in NUCLEO):
        achados.append(("ERRO", "V6: a virada nao nomeia o orgao na mesma frase"))
    if "blood flow" not in c3:
        achados.append(("ERRO", "V6: falta o MUP emendado (o fluxo estrangulado)"))

    # hook: orgao + mecanismo + comando, em <=8s
    h = falas[0].lower()
    if not any(n.lower() in h for n in NUCLEO):
        achados.append(("ERRO", "o hook nao nomeia o orgao com substantivo"))
    if "blood flow" not in h:
        achados.append(("ERRO", "o hook nao nomeia o mecanismo (blood flow)"))

    # V12 — a copy da cena 4 e' direta sobre ela
    if "she" not in falas[3].lower():
        achados.append(("ERRO", "V12: a copy da cena 4 nao fala dela"))

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
    # NE12/C3a (falha em campo, Lucas/NECROSE 2026-07-31): a keyword em CAIXA
    # ALTA e colada no `and` saiu narrada como "gelatine", e a legenda queimada
    # repetiu o erro, brigando com o CTA fixado do topo que dizia GELATIN.
    #   - a VIRGULA forca a micro-pausa que impede a liaison com a palavra seguinte
    #   - a MINUSCULA evita o Erro Fatal 12 do V4 (em ALL CAPS o Veo soletra)
    # Sao ERRO e nao AVISO: a keyword e' o gatilho da automacao Comentario->DM e
    # o defeito nao aparece em metrica visual nenhuma — o video sobe bonito e a
    # DM nunca dispara.
    if "GELATIN" in falas[4]:
        achados.append(("ERRO", "keyword em CAIXA ALTA no Dialogue: — em ALL "
                                "CAPS o Veo soletra; usar 'gelatin' (C3a)"))
    if "gelatin," not in falas[4] and "gelatin." not in falas[4]:
        achados.append(("ERRO", "keyword sem pausa depois — sem a virgula o Veo "
                                "emenda e narra 'gelatine'; usar "
                                "'Comment gelatin, and ...' (C3a)"))
    for tok, motivo in BANIDOS_CTA.items():
        if re.search(r"\b%s\b" % tok, falas[4]):   # o linter confere a copy LIMPA
            achados.append(("ERRO", "CTA usa '%s' — %s" % (tok, motivo)))
    for tok, motivo in BANIDOS_FONTE.items():
        if tok in corpo:
            achados.append(("ERRO", "copy usa '%s' — %s" % (tok, motivo)))

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
        for tabela2 in (BANIDOS_VAZAMENTO, BANIDOS_GLOBAL, BANIDOS_FONTE):
            for tok, motivo in tabela2.items():
                if tok in baixo:
                    achados.append(("ERRO", "%s contem '%s' — %s" % (nome, tok, motivo)))

    # blocos travados integros
    for nome, s, rot in (("IMAGE 01/05", GEODUCK_IMAGE, "geoduck V1"),
                         ("IMAGE 01/05", VAZAMENTO_IMAGE, "vazamento V2"),
                         ("TAKE 01/05", GEODUCK_TAKE, "imobilidade V1"),
                         ("TAKE 01/05", VAZAMENTO_TAKE, "poca V2")):
        if s not in blocos[nome]:
            achados.append(("ERRO", "%s sem a string travada: %s" % (nome, rot)))

    # V12 — idade dos DOIS declarada na abertura da cena 4
    i4 = blocos["IMAGE 04/05"]
    if "fully clothed adults" not in i4:
        achados.append(("ERRO", "V12: IMAGE 04 sem a linha de abertura declarando "
                                "'two fully clothed adults' com as duas idades"))
    if i4.count("-year-old") < 2:
        achados.append(("ERRO", "V12: idade dos dois precisa estar em TODA mencao "
                                "na cena 4 (falha de classificador documentada)"))

    # V10 — bandeira nos dois settings
    if "American flag" not in blocos["IMAGE 01/05"]:
        achados.append(("AVISO", "V10: sem bandeira dos EUA no set interno"))
    if "American flag" not in blocos["IMAGE 02/05"]:
        achados.append(("AVISO", "V10: sem bandeira dos EUA no set externo"))

    # V8 — cenas 1-3 e 5 sao SOLO
    for nome in ("IMAGE 01/05", "IMAGE 02/05", "IMAGE 03/05", "IMAGE 05/05"):
        if "alone in the frame" not in blocos[nome]:
            achados.append(("AVISO", "V8: %s nao declara que ele esta sozinho" % nome))

    return achados


# ---------------------------------------------------------------------------
# SORTEIO
# ---------------------------------------------------------------------------

# A idade dela entra na fala de duas formas: {n_ext} e' o numero inteiro por
# extenso ("thirty-four") e {n} e' so' a UNIDADE em palavra ("four"), para os
# moldes que escrevem "Thirty-{n} years old".
# ⚠️ Passar o digito cru (idade - 30) entregava "Thirty-4" na fala — bug visto
# no painel em 2026-07-30. O REF fala o que esta' escrito.
IDADE_EXT = {
    30: ("thirty", "thirty"), 31: ("thirty-one", "one"),
    32: ("thirty-two", "two"), 33: ("thirty-three", "three"),
    34: ("thirty-four", "four"), 35: ("thirty-five", "five"),
}


def _idade_slots(idade):
    ext, unidade = IDADE_EXT[idade]
    return {"n_ext": ext, "n": unidade}


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
    coz = _evitando(rng, COZINHAS, hist.get("cozinha", [])[-2:])
    qui = _evitando(rng, QUINTAIS, hist.get("quintal", [])[-2:])
    prop = _evitando(rng, PROPS_PAYOFF, hist.get("prop", [])[-2:])
    ref, mul = rng.choice(REFS), rng.choice(MULHERES)

    orgaos = rng.sample(NUCLEO, 4)
    falas = [
        rng.choice(HOOKS).format(o=orgaos[0]),
        rng.choice(RECEITAS).format(o=orgaos[1]),
        rng.choice(VIRADAS).format(o=orgaos[2]),
        rng.choice(PROVAS).format(o=orgaos[3], barreira=rng.choice(BARREIRAS),
                                  **_idade_slots(mul["idade"])),
        rng.choice(CTAS).format(pacing=rng.choice(PACING), gate=rng.choice(GATES)),
    ]
    return {"pagina": pagina, "cozinha": coz, "quintal": qui, "prop": prop,
            "ref": ref, "mulher": mul, "falas": falas}


def _gravar_ledger(ledger, spec):
    p = ledger.setdefault(spec["pagina"], {})
    for eixo, val in (("cozinha", spec["cozinha"]["id"]),
                      ("quintal", spec["quintal"]["id"]),
                      ("prop", spec["prop"]["id"])):
        p.setdefault(eixo, []).append(val)
        p[eixo] = p[eixo][-12:]
    with open(LEDGER, "w", encoding="utf-8") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)


# ---------------------------------------------------------------------------
# GERADOR
# ---------------------------------------------------------------------------

def montar(spec):
    et = ETNIA[spec["pagina"]]
    ref, mul, prop = spec["ref"], spec["mulher"], spec["prop"]
    coz, qui, falas = spec["cozinha"], spec["quintal"], spec["falas"]
    luz_ext = qui["luz"]

    roupa_s = re.sub(r"^an? ", "", ref["roupa2"])   # sem artigo, para "the same ..."
    corpo = ("bare-chested, %s, skin with a light sheen of sweat. %s."
             % (ref["musculo"], ref["marca"].capitalize()))

    b = {}

    b["BLOCO 0 (REF)"] = (
        "Photo of a real person, a %d-year-old %s man, chest up, facing the camera "
        "directly, jaw tight, brow furrowed, mouth open mid-shout. %s. Heavy crow's "
        "feet, clean-shaven, tanned skin with visible pores. %s No text, no watermark."
        % (ref["idade"], et, corpo.rstrip("."), ANTICELEB)
    )

    b["IMAGE 01/05"] = (
        "IMAGE 01/05: Medium shot inside %s. Seated behind a wooden kitchen table is "
        "a %d-year-old %s man, %s Jaw tight, brow furrowed, eyes locked on the lens, "
        "mouth open mid-shout. %s %s He is alone in the frame. %s %s %s"
        % (coz["set"], ref["idade"], et, corpo, GEODUCK_IMAGE, VAZAMENTO_IMAGE,
           ANTICELEB, coz["luz"], CAUDA)
    )

    b["IMAGE 02/05"] = (
        "IMAGE 02/05: Medium shot in %s. Standing behind a weathered wooden table is "
        "the same %d-year-old %s man, %s, now wearing %s, thick forearms bare. He is "
        "mid-action: his right hand tilts an open box of baking soda, pouring white "
        "powder into a glass jar of gelatin on the table. His left hand holds a wooden "
        "stirring stick above the jar. He is speaking, looking directly at the camera. "
        "He is alone in the frame. %s The scene is lit by %s %s"
        % (qui["set"], ref["idade"], et, ref["marca"], ref["roupa2"], ANTICELEB,
           luz_ext, CAUDA)
    )

    b["IMAGE 03/05"] = (
        "IMAGE 03/05: Medium close-up, same backyard, same table with the open jar and "
        "the box of baking soda. The same %d-year-old %s man, %s, same %s. He leans "
        "toward the camera, his right index finger pointing directly at the lens, his "
        "left hand flat on the table. Expression hard and urgent, brow furrowed, mouth "
        "open mid-word. He is alone in the frame. %s Late afternoon %s %s"
        % (ref["idade"], et, ref["marca"], roupa_s, ANTICELEB, luz_ext, CAUDA)
    )

    b["IMAGE 04/05"] = (
        "IMAGE 04/05: Medium shot, same backyard, same fence and flag. Two fully "
        "clothed adults, a %d-year-old woman and a %d-year-old man. The %d-year-old "
        "%s man, %s, wearing the same %s, stands tall, chin lifted, grinning broadly. In his right "
        "hand, held upright at shoulder height, he grips %s. A %d-year-old %s woman, "
        "strikingly beautiful, %s, visibly toned arms. She has both arms wrapped around "
        "his shoulders from the side, leaning her head against him, laughing openly. "
        "Both are ordinary everyday relatable people with plain unremarkable faces, "
        "not celebrities, not models, not actors. The scene is lit by %s %s"
        % (mul["idade"], ref["idade"], ref["idade"], et, ref["marca"], roupa_s,
           prop["desc"], mul["idade"], et, mul["desc"], luz_ext, CAUDA)
    )

    b["IMAGE 05/05"] = (
        "IMAGE 05/05: Close-up, same backyard. The same %d-year-old %s man, %s, wearing "
        "the same %s. He is alone in the frame. He looks straight into the lens, calm and "
        "confident, one corner of his mouth raised in a half-smile. His right index "
        "finger points directly at the camera. %s The scene is lit by %s %s"
        % (ref["idade"], et, ref["marca"], roupa_s, ANTICELEB, luz_ext, CAUDA)
    )

    b["TAKE 01/05"] = (
        "TAKE 01/05: Animate the provided image exactly. Handheld iPhone shot, very "
        "slight natural sway, no cuts. The %d-year-old man stares into the lens with "
        "fury, brow furrowed, jaw tight, and speaks with force, leaning forward once "
        "mid-sentence. His hands grip the shell and do not move. %s %s He is the only "
        "person in the shot.\nDialogue: \"%s\"\n"
        "Audio: quiet kitchen hum, faint refrigerator buzz. No music."
        % (ref["idade"], GEODUCK_TAKE, VAZAMENTO_TAKE, sonorizar(falas[0]))
    )

    b["TAKE 02/05"] = (
        "TAKE 02/05: Animate the provided image exactly. Handheld iPhone shot, very "
        "slight natural sway, no cuts. The %d-year-old man speaks to the camera while "
        "his hands work: he finishes pouring the baking soda, sets the box down, picks "
        "up the wooden stick, and stirs the mixture inside the jar in slow circles. His "
        "eyes stay on the lens the whole time. He is the only person in the shot and no "
        "one else enters frame.\nDialogue: \"%s\"\n"
        "Audio: outdoor ambient — distant birds, faint breeze. No music."
        % (ref["idade"], sonorizar(falas[1]))
    )

    b["TAKE 03/05"] = (
        "TAKE 03/05: Animate the provided image exactly. Handheld iPhone shot, very "
        "slight natural sway, no cuts. The %d-year-old man leans toward the camera, "
        "pointing his right index finger at the lens, expression dead serious. His left "
        "hand presses flat on the table once for emphasis. He slows down on the last "
        "sentence. He is the only person in the shot.\nDialogue: \"%s\"\n"
        "Audio: outdoor ambient — same birds, faint breeze. No music."
        % (ref["idade"], sonorizar(falas[2]))
    )

    b["TAKE 04/05"] = (
        "TAKE 04/05: Animate the provided image exactly. Handheld iPhone shot, very "
        "slight natural sway, no cuts. The %d-year-old man grins wide and laughs once "
        "at his own line, his head tipping back briefly. His right arm stays exactly "
        "where it is, holding it upright at shoulder height the entire take — it stays "
        "exactly as it appears in the first frame, same position, same angle, same "
        "shape, completely motionless for the entire shot. The %d-year-old woman laughs "
        "openly, her head tipping against his shoulder, both arms wrapped around him, "
        "swaying slightly with her laughter. Only he speaks; she is silent and "
        "laughing.\nDialogue: \"%s\"\n"
        "Audio: outdoor ambient — birds, her laughter warm and audible. No music."
        % (ref["idade"], mul["idade"], sonorizar(falas[3]))
    )

    b["TAKE 05/05"] = (
        "TAKE 05/05: Animate the provided image exactly. Handheld iPhone shot, very "
        "slight natural sway, no cuts. The %d-year-old man looks into the lens, calm "
        "and confident, and points his right index finger at the camera. He speaks "
        "directly and evenly, no rush.\nDialogue: \"%s\"\n"
        "Audio: outdoor ambient, faint breeze. No music." % (ref["idade"], sonorizar(falas[4]))
    )

    return b


# ---------------------------------------------------------------------------
# INTERFACE (consumido por ui_agente.py)
# ---------------------------------------------------------------------------

EIXOS_UI = [
    ("cozinha", "COZINHA", "COZINHAS", "id"),
    ("quintal", "QUINTAL", "QUINTAIS", "id"),
    ("prop", "PROP CENA 4", "PROPS_PAYOFF", "id"),
    ("ref", "REF (corpo-prova)", "REFS", "marca"),
    ("mulher", "MULHER", "MULHERES", "desc"),
]

CENAS_UI = ["1 · O VAZAMENTO", "2 · A RECEITA-ISCA", "3 · A VIRADA",
            "4 · MECANISMO + PROVA", "5 · CTA"]

PT_COZ = {"cozinha_branca": "cozinha branca", "cozinha_carvalho": "cozinha de carvalho",
          "cozinha_creme": "cozinha creme"}
PT_QUI = {"cerca_madeira": "no quintal de cerca de madeira",
          "churrasqueira": "no quintal com churrasqueira",
          "lenha": "no quintal com a pilha de lenha",
          "varanda_quintal": "no quintal com sofá de vime"}
PT_PROP = {"daikon": "um nabo daikon", "pepino": "um pepino",
           "banana": "uma banana", "mandioca": "uma mandioca"}


def resumo_pt(spec):
    et = "branca" if "white" in ETNIA[spec["pagina"]] else "negra"
    return ("Na %s, o REF de %d anos sem camisa segura o geoduck gigante e mole que "
            "goteja no colo, com raiva na cara. Da cena 2 em diante ele prepara a "
            "receita %s, e na 4 aparece com %s firme na mão e a mulher de %d anos "
            "abraçada nele. Elenco de pele %s."
            % (PT_COZ.get(spec["cozinha"]["id"], "cozinha"), spec["ref"]["idade"],
               PT_QUI.get(spec["quintal"]["id"], "no quintal"),
               PT_PROP.get(spec["prop"]["id"], "o prop"), spec["mulher"]["idade"], et))


def _recopiar_mulher(spec, rng):
    """A idade dela entra na copy da cena 4 — trocar exige reescrever a fala."""
    mul = spec["mulher"]
    o3 = next((n for n in NUCLEO if n.lower() in spec["falas"][3].lower()), "manhood")
    spec["falas"][3] = rng.choice(PROVAS).format(
        o=o3, barreira=rng.choice(BARREIRAS), **_idade_slots(mul["idade"]))


def nova_fala(spec, i, rng):
    """Re-sorteia a fala da cena i (0-4) mantendo o substantivo-nucleo daquela cena."""
    o = next((n for n in NUCLEO if n.lower() in spec["falas"][i].lower()), "Johnson")
    mul = spec["mulher"]
    if i == 0:
        return rng.choice(HOOKS).format(o=o)
    if i == 1:
        return rng.choice(RECEITAS).format(o=o)
    if i == 2:
        return rng.choice(VIRADAS).format(o=o)
    if i == 3:
        return rng.choice(PROVAS).format(o=o, barreira=rng.choice(BARREIRAS),
                                         **_idade_slots(mul["idade"]))
    return rng.choice(CTAS).format(pacing=rng.choice(PACING), gate=rng.choice(GATES))

EIXOS_QUE_MEXEM_NA_COPY = {"mulher": _recopiar_mulher}


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def imprimir(spec, blocos, achados):
    print("=" * 72)
    print("SPEC SORTEADA — pagina %s | cozinha %s | quintal %s | prop %s | REF %dy"
          % (spec["pagina"], spec["cozinha"]["id"], spec["quintal"]["id"],
             spec["prop"]["id"], spec["ref"]["idade"]))
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
    ap = argparse.ArgumentParser(description="Randomizador do agente VAZAMENTO")
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
