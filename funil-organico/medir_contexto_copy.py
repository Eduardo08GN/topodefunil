# -*- coding: utf-8 -*-
"""A copy diz DE QUE SE TRATA, ou o espectador tem de adivinhar?

    python funil-organico/medir_contexto_copy.py
    python funil-organico/medir_contexto_copy.py --gate      # sai 1 se houver
    python funil-organico/medir_contexto_copy.py --autoteste
    python funil-organico/medir_contexto_copy.py --motor troca_short

POR QUE ESTE ARQUIVO EXISTE (2026-08-03). O operador leu um take renderizado:

    "It isn't age. The blood flow got choked off. Parsley and warm water open
     it. Real vasodilators. And the gelatin trick is what keeps his old boy
     open."

    -> "Deveria ser: it isn't age THAT'S CAUSING YOUR JOHN-SON NOT WORKING
        ANYMORE. Ta' deixando o viewer sem entender o contexto e do que se
        trata. Arrume isso em todos os agentes."

Idade causando O QUE? Estrangulado ONDE? O espectador ouve fisiologia solta por
cinco segundos, e quando o orgao finalmente aparece, aparece na ULTIMA frase e
em terceira pessoa. Medido no dia da queixa: **8 de 9 motores** tinham o vicio,
de 19% a 100% das frases causais.

DUAS FORMAS, e o medidor cobra as duas:
  [A] FRASE ORFA  — a frase nomeia uma CAUSA e nao diz sobre o que ela age.
  [B] CENA ORFA   — a cena inteira fala de mecanismo e nunca nomeia o problema.

⚠️ TERCEIRA PESSOA NAO E' O VICIO. No FLAGRANTE e no PEE a narradora conta a
historia de um TERCEIRO e o espectador se identifica: `his old boy went soft` e'
o formato daquele angulo. O que se cobra e' REFERENTE, nunca pessoa.

⛔ ESTE MEDIDOR JA' MENTIU DUAS VEZES antes de servir, e as duas viraram
controle no `--autoteste`:
  v1 contou `his {o}` como vicio -> 400 em 200 videos no FLAGRANTE, tudo falso.
  v2 mediu por CENA ("o orgao aparece em algum lugar?") -> APROVOU exatamente a
     cena que o operador reprovou, porque `his old boy` esta' na ultima frase.
     A queixa e' de FRASE.
  e o regex de `age` pegava `Half my age, and she's the one who won't wait` —
     que fala da idade DELA e nao e' alegacao causal nenhuma. Por isso a causa
     so' conta em MOLDURA EXPLICATIVA: negada, culpada ou vendida como desculpa.
"""
import argparse
import collections
import importlib
import os
import random
import re
import sys

# ⛔ MESMO REMENDO DO `medir_personagens.py` (linha 51), e pela mesma razao
# medida em 2026-08-13: este gate MORREU no proprio rodape, com
# UnicodeEncodeError, ao imprimir a lista de travas DESLIGADAS — o console
# do Windows e' cp1252 e os marcadores nao cabem nele.
# ⚠️ E o padrao caro se repetiu inteiro: o rodape so' roda QUANDO HA' ALGO
# A REPORTAR, entao o gate quebrava exatamente na hora em que tinha algo a
# dizer, e nunca no caminho feliz. Gate que morre calado na hora do recado
# treina o operador a ignorar o gate.
for _f in (sys.stdout, sys.stderr):
    try:
        _f.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

FO = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, FO)

# ⛔⛔ SO' OS SHORT. Ordem do operador em 2026-08-03: "os agentes que nao sao do
# tipo SHORT e os que tem label `lucas` NAO entram no nosso escopo de
# melhoramento". O que esta' em producao e' o AdBatch Vertical 3, que consome
# video de 3 cenas — medir o arco longo de 5 cenas gasta tempo em coisa que nao
# vira video postado.
# ⚠️ E A ARMADILHA: os quatro SHORT DERIVADOS fazem `import <agente>_lucas as
# base` e puxam os pools de copy de la'. Entao o conserto e' escrito no arquivo
# `_lucas` e o efeito TEM DE SER MEDIDO AQUI, no `_short`. Medir o `_lucas`
# mede o arco longo, que esta' fora de escopo e tem tetos diferentes.
# ⚠️ 2026-08-03: `exterior_short` entrou aqui NO MESMO COMMIT em que nasceu.
# Gate que nao ve' o motor nao reprova o motor — ele so' produz um "passou"
# mentiroso (§7 das licoes, e e' o mesmo defeito que deixou o elenco masculino
# inteiro de tres motores fora do `medir_personagens.py`).
# ⚠️ 2026-08-03: `clean_short_v2` entrou aqui na revisao do proprio v2. Ele
# tinha nascido FORA desta lista — o `--gate` rodava verde sem nunca ter olhado
# para o motor novo, que e' exatamente o "passou" mentiroso descrito acima.
MOTORES = ["clean_short", "clean_short_v2", "escandalo_short", "troca_short",
           "organicwave_short", "ressurreicao_short", "flagrante_short",
           "pee_short", "vazamento_short", "necrose_short", "exterior_short",
           "colo_short", "receita_short", "botica_short",
           "dupla_short", "placa_short", "cha_short", "trio_short",
           # ⚠️ 2026-08-06: `falta_short` entrou aqui pelo MESMO motivo do
           # v2 acima — nasceu fora da lista e o `--gate` passou verde sem
           # nunca ter olhado para ele.
           "falta_short",
           "trio16_short",
           "dupla16_short",
           "falta16_short",
           "placa16_short",
           "troca16_short",
           "botica16_short",
           "colo16_short", "exterior16_short", "escandalo16_short",
           # + 2026-08-08: o CLEAN V1 16SEG
           "clean_v1_16s_short",
           "ressurreicao16_short",
           "flagrante16_short", "good16_short",
           # + 2026-08-10: o BED 16 entra AQUI no commit em que nasce — gate
           # que nao ve' o motor nao reprova o motor, so' produz um "passou"
           # mentiroso.
           "bed16_short", "necrose16_short", "wife16_short",
           # + 2026-08-10: o FIGHT 16, no commit em que nasce
           "fight16_short",
           # ⚠️ 2026-08-10: `pee16_short` entrou aqui na reforma dos pools
           # de personagem dele. Ele NUNCA tinha estado nesta lista — o
           # motor existe desde 08-09 e este medidor nunca olhou para ele.
           # Gate que nao ve o motor nao reprova o motor (licoes §7).
           "pee16_short",
           "alfa16_short",
           # + 2026-08-14: o ORGANIC WAVE 16, no commit em que nasce.
           "organicwave16_short",
           # + 2026-08-14: o HORSE 16, no commit em que nasce.
           "horse16_short"]
PAGINAS = ["joe", "marcus", "ray", "chuck", "matt"]
N = 200

ORGAO = (r"john-?son|pecker|peck-?er|wiener|manhood|soldier|old boy|tool|"
         r"equipment|hardware")

# [A] a FRASE alega uma causa — so' em moldura EXPLICATIVA
CAUSA = re.compile(
    r"\b(it'?s|it is|it was|that'?s|this is)\s*(not|never|n'?t)?\s*"
    r"(your |his |my )?(age|aging|genetics|hormones?|testosterone)\b"
    r"|\b(blam\w+|call\w+ it|sold you|the)\s+"
    r"(your |his |the )?(age|aging)( excuse)?\b"
    r"|\b(blood ?flow|circulation|blood|pressure|vessels?|arter\w+)\b"
    r"[^.]{0,40}\b(choked|blocked|shut|cut off|closed|starved|died|stopped)\b"
    r"|\b(choked off|blocked off|shut down|cut off|closed off)\b", re.I)

# [B] a CENA fala de mecanismo/fisiologia
MECANISMO = re.compile(
    r"\b(age|genetics|hormones?|testosterone|blood ?flow|circulation|"
    r"vasodilator\w*|nitric oxide|collagen|oxygen|vessels?|arter\w+|"
    r"inflammation|choked|blocked|shut down|cut off)\b", re.I)

# o ALVO — o que esta' quebrado, em qualquer pessoa
# ⚠️⚠️ CRESCEU EM 2026-08-10, e pelo motivo de sempre: ELA REPROVOU COPY CERTA.
# O FIGHT 16 nasceu com o hook VERBATIM da fonte (`Struggling to stay hard?`) e
# 116 de 400 cenas cairam como orfas [B] — a cena nomeia a causa (`age`) e diz
# exatamente o que ela quebra, so' que numa forma que este regex nao conhecia.
# ⛔ `stay hard` / `stay firm` / `keep it up` sao a formula MAIS SEGURA do parque
# para enunciar a falha: elas falam do CORPO sem nomear o orgao, que e' o que faz
# o CT7 passar por construcao e o gerador nao recusar. A lista so' conhecia
# `stay SOFT` — a forma negativa, que quase nenhum motor usa.
# ⚠️ E' a mesma correcao que o `sc.lint_copy16` levou hoje ao aprender
# `struggl\w*`: o medidor aprende a forma, a copy nao se dobra ao regex
# (licoes §16 — lente que reprova o que esta' certo treina o operador a ignorar
# o relatorio inteiro).
ALVO = re.compile(
    r"\b(%s)\b"
    r"|\b(went|goes|going|stay\w*|get\w*) soft\b"
    r"|\b(stay|staying|stayed) (hard|firm)\b|\bkeep(ing)? it up\b"
    r"|\b(quit\w*|fail\w*|stopped working|won'?t work|doesn'?t work|"
    r"not working|gone quiet)\b"
    r"|\berection\b|\bin bed\b|\bdown there\b|\bbedroom\b" % ORGAO, re.I)

# controles: (texto, deve_ser_orfa)
CONTROLES_A = [
    (u"It isn't age.", True),
    (u"The blood flow got choked off.", True),
    (u"They sold you the age excuse.", True),
    (u"It isn't age that's got your John-son quitting on you.", False),
    (u"The blood flow to his old boy got choked off.", False),
    (u"Half my age, and she's the one who won't wait.", False),
    (u"She wakes up, feels that, and says nothing.", False),
]


def frases(t):
    return [f.strip() for f in re.split(r"(?<=[.!?])\s+", t) if f.strip()]


def autoteste():
    falhas = 0
    for txt, esperado in CONTROLES_A:
        tem_causa = bool(CAUSA.search(txt))
        orfa = tem_causa and not ALVO.search(txt)
        if orfa != esperado:
            print("  AUTOTESTE FALHOU  esperava orfa=%s, deu %s: %r"
                  % (esperado, orfa, txt))
            falhas += 1
    print("autoteste do medidor: %s"
          % ("%d falha(s)" % falhas if falhas else "ok"))
    return falhas


def medir(nome):
    m = importlib.import_module(nome)
    rng = random.Random(20260803)
    ledger = {}
    tot = causa = orfa_a = 0
    cena_mec = collections.Counter()
    cena_orfa = collections.Counter()
    ex_a, ex_b = [], []
    for i in range(N):
        try:
            spec = m.sortear(PAGINAS[i % len(PAGINAS)], rng, ledger)
        except Exception as e:                               # noqa: BLE001
            return None, "sortear falhou: %s" % e
        for j, fala in enumerate(spec.get("falas", []), 1):
            if MECANISMO.search(fala):
                cena_mec[j] += 1
                if not ALVO.search(fala):
                    cena_orfa[j] += 1
                    if len(ex_b) < 2 and fala not in ex_b:
                        ex_b.append(fala)
            for fr in frases(fala):
                tot += 1
                if not CAUSA.search(fr):
                    continue
                causa += 1
                if not ALVO.search(fr):
                    orfa_a += 1
                    if len(ex_a) < 3 and fr not in ex_a:
                        ex_a.append(fr)
    return {"frases": tot, "causa": causa, "orfa_a": orfa_a,
            "cena_mec": dict(cena_mec), "cena_orfa": dict(cena_orfa),
            "orfa_b": sum(cena_orfa.values()),
            "ex_a": ex_a, "ex_b": ex_b}, None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gate", action="store_true")
    ap.add_argument("--autoteste", action="store_true")
    ap.add_argument("--motor")
    args = ap.parse_args()

    falhas = autoteste()
    if args.autoteste:
        return 1 if falhas else 0
    if falhas:
        print("⛔ o medidor esta' quebrado — conserte o regex antes de confiar "
              "no relatorio abaixo")

    alvos = [args.motor] if args.motor else MOTORES
    print("\n%-20s %7s %7s %8s %8s" %
          ("motor", "frases", "causa", "[A]orfa", "[B]cena"))
    print("-" * 56)
    sujos = []
    exemplos = []
    for nome in alvos:
        r, erro = medir(nome)
        if erro:
            print("%-20s  %s" % (nome, erro))
            continue
        print("%-20s %7d %7d %8d %8d"
              % (nome, r["frases"], r["causa"], r["orfa_a"], r["orfa_b"]))
        if r["orfa_a"] or r["orfa_b"]:
            sujos.append(nome)
            for e in r["ex_a"]:
                exemplos.append(("%s [A]" % nome, e))
            for e in r["ex_b"]:
                exemplos.append(("%s [B]" % nome, e[:104]))
    print()
    for rot, e in exemplos:
        print("  %-24s %s" % (rot, e))
    print("\nMOTORES COM COPY ORFA: %d de %d" % (len(sujos), len(alvos)))
    if args.gate and sujos:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
