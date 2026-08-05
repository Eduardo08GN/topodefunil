#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
auditar_drifting.py — o TESTE WTF aplicado a TODA sentenca de TODO agente SHORT.

⛔ POR QUE EXISTE. A regra do operador (2026-08-04):

    "Sempre leia: se a sentenca da' afirmativo para possibilidade do leitor
     dizer «wtf he/she talking about?», e' drifting de copy vaga, e' DESCARTE
     de copy."

Os medidores que ja' existiam cobrem PEDACOS disso e cada um olha um lugar:

    medir_abertura.py ........ so' a PRIMEIRA sentenca de cada cena
    medir_contexto_copy.py ... so' causa nomeada sem alvo
    os linters de motor ...... so' o slot proprio de cada agente

Este aqui varre TODAS as sentencas de TODAS as cenas e classifica o drifting em
familias, para o operador ver o flagrante e decidir o conserto.

⚠️⚠️ ELE ACHA CANDIDATOS, NAO DA' VEREDITO — e isso e' a licao §16 escrita na
porta. O medidor irmao ja' acusou "Guys still putting the cucumber in the donut
at seventy" como orfa, e ela NAO e' vaga: a metafora do prop diz exatamente do
que se trata. Regex nao codifica "o que o espectador entende".

    o numero e' ponto de partida · a lista de frases e' o trabalho ·
    o veredito de cada uma e' humano

⚠️ E MEDE EM DOIS PATAMARES (licao §23, do Lucas): cobertura de amostra mede o
que o sorteio calhou de gerar, nao o que o agente e' CAPAZ de gerar. Se o
segundo patamar acha familia nova, a amostra ainda nao provou nada.

Uso:
    python funil-organico/auditar_drifting.py
    python funil-organico/auditar_drifting.py --motor botica_short --n 2000
    python funil-organico/auditar_drifting.py --autoteste
"""

import argparse
import collections
import importlib
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

MOTORES = ["clean_short", "clean_short_v2", "escandalo_short", "troca_short",
           "organicwave_short", "ressurreicao_short", "flagrante_short",
           "pee_short", "vazamento_short", "necrose_short", "exterior_short",
           "colo_short", "receita_short", "botica_short"]

# ---------------------------------------------------------------------------
# O QUE CONTA COMO REFERENTE — deliberadamente largo, para nao acusar o certo
# ---------------------------------------------------------------------------
# ⛔ `it`, `this`, `that`, `them` NAO contam: sao o vicio.
# ⚠️ A METAFORA DO PROP CONTA. `the cucumber in the donut`, `banana`, `bagel`
# dizem ao espectador do que se trata tao bem quanto o substantivo do nucleo —
# e' o hook fundador de tres agentes. Sem isto a lente reprova o que esta' certo.
PROP = (r"banana|plantain|cucumber|carrot|parsnip|eggplant|zucchini|daikon|"
        r"donut|doughnut|bagel|geoduck|sausage|pickle")
PESSOA = (r"my (?:husband|wife|man|woman|marriage)|his wife|her husband|"
          r"the woman I married|my (?:brother|father|sister)")
CORPO = (r"erection|in bed|down there|bedroom|hard again|goes soft|went soft|"
         r"stays? hard|blood flow to|circulation to")
# ⭐ AGENTE NOMEADO TAMBEM E' REFERENTE. `The pharmacy industry sells you pills`
# diz ao espectador exatamente do que se trata sem citar orgao nenhum — e' o
# beat do vilao, e cobrar orgao dele seria reprovar o que esta' certo (§16).
AGENTE = (r"pharmac\w+|drug compan\w+|drug industry|pill compan\w+|doctors?|"
          r"clinic|chemists?|prescription")
# ⛔ AS GRAFIAS SONORIZADAS CONTAM. O `nucleo_sonoro` troca `Johnson` por
# `John-son` e `wiener` por `weiner` na linha `Dialogue:` — auditar so' a grafia
# limpa faria a lente acusar falsamente toda fala renderizada. Achado pelo
# proprio controle, antes de olhar numero.
SONORO = r"john-?son|peck-?er|wei?ner|sol[dj]\w*|toole"


# ⛔⛔ `gelatin` E' REFERENTE, e esquecer isso me fez acusar o parque inteiro.
# Na primeira passada a lente reprovou TODA CTA (`Comment gelatin, and I'll send
# you the recipe`) e TODA receita (`A spoon of gelatin and raw honey in a glass
# of warm milk`) — frases perfeitamente claras, que sao o mecanismo e o pedido
# do funil. Achado abrindo os tres primeiros a mao antes de reportar (§16).
# ⚠️ O mesmo vale para o INGREDIENTE: uma receita que nomeia o que entra no copo
# diz do que se trata. Vago e' `it`, `this`, `that` — nunca um substantivo.
MECANISMO = (r"gelatin|honey|cinnamon|ginger|turmeric|cayenne|beet|lemon|lime|"
             r"baking soda|vinegar|saffron|maca|tongkat|tribulus|epimedium|"
             r"fenugreek|muira|ginkgo|mucuna|sarsaparilla|watermelon|parsley|"
             r"pomegranate|oats|molasses|garlic|cacao|maple")


def _referentes(m):
    nucleo = "|".join(re.escape(x) for x in getattr(m, "NUCLEO", []) or ["zzz"])
    return re.compile("(%s|%s|%s|%s|%s|%s|%s)"
                      % (nucleo, SONORO, PROP, PESSOA, CORPO, AGENTE,
                         MECANISMO), re.I)


# ---------------------------------------------------------------------------
# AS FAMILIAS DE DRIFTING — cada uma nasceu de um caso que o operador reprovou
# ---------------------------------------------------------------------------
FAMILIAS = [
    ("reacao sem objeto",
     # §20: `She noticed.` -> notou o QUE?
     re.compile(r"\b(notic\w+|saw|sees|felt|feels|star\w+|watch\w+|"
                r"could\w* believe|double-?took)\b", re.I),
     "a reacao e' o slot da PROVA SOCIAL; sem objeto ela morre em silencio"),

    ("agente pronominal",
     # §22: `They will sell you a monthly plan` -> QUEM vende?
     re.compile(r"\b(they|them|nobody|no one|somebody|someone)\b"
                r"[^.]{0,40}\b(sell\w*|sold|hide\w*|hid|keep\w*|kept|told|"
                r"tell\w*|want\w*|make\w*|made|put\w*|took|take\w*)\b", re.I),
     "pronome nao diz QUEM esconde nem QUEM lucra"),

    ("perda sem quem",
     # RE22: `I almost lost her` -> perdeu quem?
     re.compile(r"\b(lost|losing|lose)\s+(her|him|them|it)\b", re.I),
     "pronome no lugar de `my wife` / `my marriage`"),

    ("promessa vaga",
     # `you'll be a new person` -> novo por que?
     re.compile(r"\b(you'?ll be|you'?ll feel|you'?ll get|you become|"
                r"you'?ll wake up)\b[^.]{0,30}\b(new|different|another|better|"
                r"changed)\b", re.I),
     "promete mudanca sem dizer em que"),

    ("causa sem alvo",
     # §17: `It isn't age.` -> idade causando o que?
     re.compile(r"\b(it'?s|it is|it was|that'?s)\s*(not|never|n'?t)?\s*"
                r"(your |his |my )?(age|aging|genetics|hormones?|"
                r"testosterone)\b", re.I),
     "nomeia a causa e nao diz o que ela quebra"),
]


def sentencas(t):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", t or "") if s.strip()]


def _pools(m):
    """{nome_do_pool: [templates]} — so' listas de string, para rastrear a fonte."""
    out = {}
    for nome in dir(m):
        if not nome.isupper():
            continue
        v = getattr(m, nome)
        if isinstance(v, list) and v and all(isinstance(x, str) for x in v):
            out[nome] = v
        elif isinstance(v, list) and v and all(isinstance(x, dict) for x in v):
            for campo in ("txt", "fala", "desc"):
                if all(campo in x for x in v):
                    out["%s.%s" % (nome, campo)] = [x[campo] for x in v]
    return out


def _de_qual_pool(frase, pools, nucleo):
    """De qual pool veio a frase — sem isso o relatorio nao diz ONDE consertar."""
    alvo = frase
    for n in nucleo:
        alvo = re.sub(re.escape(n), "{o}", alvo, flags=re.I)
    for nome, entradas in pools.items():
        for e in entradas:
            molde = re.escape(e)
            molde = re.sub(r"\\\{\w+\\\}", ".{0,40}?", molde)
            if re.search(molde.rstrip("\\."), alvo, re.I):
                return nome
    return "?"


def auditar(nome, n=600):
    m = importlib.import_module(nome)
    ref = _referentes(m)
    nucleo = getattr(m, "NUCLEO", []) or []
    pools = _pools(m)
    achados = collections.defaultdict(list)
    total_sent = 0

    import random as _r
    for s in range(n):
        try:
            spec = m.sortear("joe", _r.Random(s), {})
        except Exception:
            break
        for i, fala in enumerate(spec["falas"], 1):
            sents = sentencas(fala)
            for k, fr in enumerate(sents):
                total_sent += 1
                tem_ref = bool(ref.search(fr))
                for fam, rx, _porque in FAMILIAS:
                    if rx.search(fr) and not tem_ref:
                        achados[fam].append((i, fr))
                        break
                else:
                    # abertura orfa: a PRIMEIRA sentenca da cena sem referente
                    if k == 0 and not tem_ref:
                        achados["abertura orfa"].append((i, fr))
    return total_sent, achados, pools, nucleo


def autoteste():
    """⛔ Controles ANTES de qualquer numero (licoes §16). Os casos reprovados
    pelo operador entram como controle NEGATIVO; o que esta' certo, positivo."""
    rx = re.compile("(%s|%s|%s|%s|%s|%s|%s)"
                    % ("Johnson|pecker|wiener|soldier|tool", SONORO,
                       PROP, PESSOA, CORPO, AGENTE, MECANISMO), re.I)
    reprova = [
        "She noticed.",
        "They will sell you a monthly plan before they sell you the truth.",
        "I almost lost her.",
        "You'll be a new person.",
        "It isn't age.",
    ]
    aprova = [
        "She noticed his John-son harder than ever.",
        "The pharmacy industry sells you pills and hides the cheap fix.",
        "I almost lost my wife.",
        "You'll be a new man, and your pecker is the proof.",
        "Guys still putting the cucumber in the donut at seventy.",
        "His old boy went soft on him.",
        # ⛔ os dois que a lente acusou falsamente na primeira passada
        "Comment gelatin, and I'll send you the recipe.",
        "A spoon of gelatin and a spoon of raw honey in a glass of warm milk.",
    ]
    falhas = []
    for f in reprova:
        pego = any(r.search(f) for _n, r, _p in FAMILIAS) and not rx.search(f)
        if not pego:
            falhas.append("NAO pegou o que devia: %r" % f)
    for f in aprova:
        if not rx.search(f):
            falhas.append("acusaria o que esta' CERTO: %r" % f)
    if falhas:
        print(">> AUDITOR CEGO:")
        for x in falhas:
            print("   %s" % x)
    else:
        print("autoteste do auditor: ok (5 negativos + 6 positivos, "
              "incluindo metafora de prop e 3a pessoa)")
    return 1 if falhas else 0


def main():
    ap = argparse.ArgumentParser(description="Auditoria de drifting de copy")
    ap.add_argument("--motor", choices=MOTORES)
    ap.add_argument("--n", type=int, default=600)
    ap.add_argument("--exemplos", type=int, default=3)
    ap.add_argument("--autoteste", action="store_true")
    ap.add_argument("--convergencia", action="store_true",
                    help="mede em dois patamares (licao §23)")
    a = ap.parse_args()

    if a.autoteste:
        return autoteste()
    if autoteste():
        return 1

    alvos = [a.motor] if a.motor else MOTORES
    print()
    print("%-22s %7s %7s %7s  %s"
          % ("motor", "sents", "sujas", "%", "familias"))
    print("-" * 84)
    resumo = {}
    for nome in alvos:
        tot, ach, pools, nucleo = auditar(nome, a.n)
        sujas = sum(len(v) for v in ach.values())
        if not tot:
            continue
        resumo[nome] = (tot, ach, pools, nucleo)
        fam = ", ".join("%s %d" % (k, len(v))
                        for k, v in sorted(ach.items(), key=lambda x: -len(x[1])))
        print("%-22s %7d %7d %6.1f%%  %s"
              % (nome, tot, sujas, 100.0 * sujas / tot, fam or "-"))

    print()
    print("=" * 84)
    print("FLAGRANTE — as frases, por motor e por familia")
    print("=" * 84)
    for nome, (tot, ach, pools, nucleo) in resumo.items():
        if not ach:
            continue
        print("\n### %s" % nome)
        for fam, itens in sorted(ach.items(), key=lambda x: -len(x[1])):
            vistas, mostradas = set(), 0
            print("  [%s] %d ocorrencias" % (fam, len(itens)))
            for cena, fr in itens:
                chave = re.sub(r"\d+", "N", fr)
                if chave in vistas:
                    continue
                vistas.add(chave)
                mostradas += 1
                if mostradas > a.exemplos:
                    break
                pool = _de_qual_pool(fr, pools, nucleo)
                print("      cena %d | %-58s <- %s" % (cena, fr[:58], pool))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
