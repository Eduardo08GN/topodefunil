#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE PEE SHORT — 3 cenas de 8 segundos.

Deriva de `pee_lucas.py`. Nenhuma string travada, pool ou tabela e' duplicada.

    base 1 · A MANCHA + O VINCULO  ->  SHORT 1 · A MANCHA
    base 4 · REDENCAO              ->  SHORT 2 · O TRUQUE + A VIRADA (funde 2, 3 e 4)
    base 5 · CTA                   ->  SHORT 3 · CTA

⛔ O QUE O COLAPSO AMEACAVA
Duas coisas, e as duas sao espinha do angulo:
  · o literal `gelatin trick`, que morava nos RITUAIS (cena 3);
  · o **mecanismo da prostata** (PE7), que morava nos MECANISMOS (cena 2). No
    PEE o mecanismo nao e' `blood flow` generico: e' a prostata inchada
    apertando o cano, e e' isso que amarra a mancha ao orgao. Sem ele o hook
    faz uma afirmacao que o video nunca sustenta.
Os dois entram na copy fundida, e o linter trava nos dois.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import pee_lucas as base                                        # noqa: E402
import short_comum as sc                                        # noqa: E402

from pee_lucas import (ETNIA, NUCLEO, EIXOS_UI, BARREIRAS,       # noqa: E402,F401
                       PT_LOCAL, _palavras)

AQUI = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(AQUI, ".pee-short-ledger.json")

TITULO = "AGENTE PEE SHORT"
SUBTITULO = "a mancha pública, em 3 cenas · gerador offline de prompts Veo"
SLUG = "pee-short"

# ⭐ MAPA e' de onde vem a IMAGEM; MAPA_COPY e' de onde vem a FALA. A cena 3
# junta as duas coisas: a fala do CTA (base 5) por cima da cena do ritual.
#
# ⚠️ Ordem do operador, 2026-07-31: "estamos deixando espaco valioso nesses 22
# segundos apertados no lixo". A cena 3 era o close do CTA — um terco do video
# num talking head, zero informacao visual. Agora o espectador OUVE o pedido e
# VE o gelatin trick nos mesmos 8 segundos.

# ⚠️ E aqui a cena 3 nao vem pronta do base: a do ritual dele e' insert de
# maos, e o operador pediu "rosto aparente enquanto prepara". A recombinacao
# (set da cena 2 + acao da cena 3 + rosto) mora em short_comum.bancada_com_rosto
# — nenhum fragmento novo, e o motor longo fica intacto.
MAPA = (1, 4, 3)
MAPA_COPY = (1, None, 5)          # None = a fundida
CENAS_UI = ["1 · A MANCHA", "2 · O TRUQUE + A VIRADA", "3 · CTA PREPARANDO"]

# As pontas herdam o teto do motor base — os pools sao os mesmos, e no PEE eles
# estao bem calibrados (0% de estouro em 300 sorteios medidos). So' a cena 2
# tem teto proprio, porque a copy dela e' propria.
TETO_FALA = {1: base.TETO_FALA[1], 2: 34, 3: base.TETO_FALA[5]}


# ---------------------------------------------------------------------------
# A COPY FUNDIDA — cena 2
# ---------------------------------------------------------------------------
# ⚠️ CURADORIA DO OPERADOR. Copy nova, montada dos fragmentos ja' validados dos
# MECANISMOS, RITUAIS e REDENCOES do motor base.
#
# Todo item carrega, na mesma respiracao:
#   1. o mecanismo -> a `prostate` apertando o cano (PE7)
#   2. o ritual    -> a string literal `gelatin trick`
#   3. a virada    -> ele seco, dezenove dias depois, e ela
# ⛔ Sem {barreira}: tres beats ja' enchem os 8 segundos.
# ⚠️ Todo item precisa de `{o}` — o CTA nao nomeia o orgao.
FUNDIDAS = [
    "It's the prostate pressing the line flat — the same squeeze that starves "
    "your {o}. His brother gave him the gelatin trick. Nineteen days later he "
    "was dry, head up.",

    "His prostate clamped the pipe shut, and that same pressure shut his {o} "
    "down. The gelatin trick opened both. Nineteen days later she reaches for "
    "him first.",

    "It's his prostate choking the line — the same squeeze is why your {o} "
    "can't fill. One spoon of the gelatin trick, and nineteen days later he "
    "was dry.",

    "The prostate sits on that pipe and shuts your {o} down. His brother handed "
    "him the gelatin trick. Nineteen days later he walked in dry, head high.",

    "Pills don't touch this — it's the prostate pressing the line flat. The "
    "gelatin trick opened it, and nineteen days later his {o} hasn't quit "
    "since.",

    # + 2026-08-01: o operador mediu vicio — a mesma fundida em todo lote SHORT.
    # Pool ampliado; cada item continua carregando o literal `gelatin trick`,
    # a prostata no cano e o {o}, porque as cenas que os traziam sao as que caem.
    "A man at the barbershop handed him the gelatin trick. It opens the "
    "line the prostate was pinching shut, and it wakes your {o}. Nineteen days.",

    "Nineteen days is all it took. The gelatin trick got the pipe open under "
    "his prostate, and his {o} came back with it. She noticed first.",

    "Same prostate, two failures — the wet pants and the dead {o}. One spoon "
    "of the gelatin trick, and nineteen days later he was dry and she wasn't "
    "sleeping.",

    "If you get up twice a night, that's the prostate on the line, and your "
    "{o} is next. The gelatin trick opened his in nineteen days.",

    "A retired trucker told him about the gelatin trick. It gets under the "
    "prostate that's squeezing the pipe, and nineteen days later his {o} "
    "answered.",

    "Doctors treat the bladder and leave the rest. It's one prostate on one "
    "pipe. He stirred the gelatin trick into cold water and got his {o} back.",

    "Think of a thumb over a hose end — that's his prostate, and your {o} "
    "gets nothing. The gelatin trick moved the thumb. Nineteen days, dry and "
    "grinning.",

    "He laughed at the gelatin trick too. Then his prostate stopped sitting "
    "on that pipe, and three weeks later she was the one bragging about his {o}.",

    "The prostate closes the pipe first and your {o} second. Nobody tells you "
    "that. The gelatin trick opened both for him, and she noticed inside three "
    "weeks.",
]


def _fundir(spec, rng):
    o = sc.orgao_de(base, spec["falas_base"][3])
    return rng.choice(FUNDIDAS).format(o=o)


# ---------------------------------------------------------------------------
# CONTRATO DO MOTOR
# ---------------------------------------------------------------------------

def _carregar_ledger():
    import json
    if os.path.exists(LEDGER):
        with open(LEDGER, encoding="utf-8-sig") as f:
            return json.load(f)
    return {}


def _gravar_ledger(ledger, spec):
    import json
    p = ledger.setdefault(spec["pagina"], {})
    for eixo, val in (("local", spec["local"]["id"]),
                      ("roupa", spec["roupa"]["id"]),
                      ("ambiente", spec["ambiente"]["id"]),
                      ("prop", spec["prop"]["id"])):
        p.setdefault(eixo, []).append(val)
        p[eixo] = p[eixo][-12:]
    with open(LEDGER, "w", encoding="utf-8") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)


def sortear(pagina, rng, ledger):
    return sc.sortear_curto(base, pagina, rng, ledger, MAPA, _fundir, MAPA_COPY)


def montar(spec):
    b = sc.montar_curto(base, spec, MAPA)
    # a cena 3 e' a unica que nao vem pronta do base — ver o comentario
    # do MAPA e a docstring de short_comum.bancada_com_rosto
    # ⚠️ DUAS cenas nao vem prontas do base, e as duas por ordem do
    # operador: a 2, para o narrador nao sumir no terco do meio; e a 3,
    # para o rosto aparecer enquanto prepara. As duas recombinam blocos
    # validados — ver as docstrings em short_comum.
    i2, t2 = sc.redencao_com_ref(base, spec, spec["falas"][1])
    b["IMAGE 02/03"], b["TAKE 02/03"] = i2, t2
    i3, t3 = sc.bancada_com_rosto(base, spec, spec["falas"][2])
    b["IMAGE 03/03"], b["TAKE 03/03"] = i3, t3
    # ⛔ trava de texto queimado em todo TAKE — o watermark que o
    # operador viu vazando nos reels da concorrente (2026-08-01).
    return sc.selar_takes(b)


def nova_fala(spec, i, rng):
    return sc.nova_fala_curta(base, spec, i, rng, MAPA, _fundir, MAPA_COPY)


def _recopiar_local(spec, rng):
    """O local entra no hook — trocar exige reescreve-lo."""
    spec["falas"][0] = base.nova_fala(sc.espelho(spec, MAPA), 0, rng)


EIXOS_QUE_MEXEM_NA_COPY = {"local": _recopiar_local}


# ---------------------------------------------------------------------------
# LINTER
# ---------------------------------------------------------------------------

def _pe6_hook(spec, blocos, achados):
    """O hook diz o mijo, nomeia o orgao e AFIRMA o vinculo entre os dois."""
    h = spec["falas"][0].lower()
    if not any(t in h for t in ("peed", "wet", "soaked", "leak", "lost it")):
        achados.append(("ERRO", "PE6: o hook nao diz o mijo"))
    if not any(n.lower() in h for n in NUCLEO):
        achados.append(("ERRO", "PE6: o hook nao nomeia o orgao — hook so' de "
                                "mancha nao vende nada"))
    if not any(t in h for t in ("same thing", "same reason", "that's why",
                                "and that's why")):
        achados.append(("ERRO", "PE6: falta o VINCULO afirmado no hook "
                                "(a mancha e o orgao tem a MESMA causa)"))


def _pe1_roupa_clara(spec, blocos, achados):
    i1 = sc.bloco_base(blocos, MAPA, "IMAGE", 1).lower()
    for escura in base.ROUPA_ESCURA:
        if escura in i1:
            achados.append(("ERRO", "PE1: roupa escura ('%s') mata o contraste "
                                    "da mancha" % escura))


def _blocos_travados(spec, blocos, achados):
    i1 = sc.bloco_base(blocos, MAPA, "IMAGE", 1)
    for s, rot in ((base.CHORO_IMAGE, "choro PE2"),
                   (base.NARRADOR_IMAGE, "narrador PE3"),
                   (base.PLATEIA_IMAGE, "plateia PE4")):
        if s not in i1:
            achados.append(("ERRO", "a cena da mancha sem a string travada: %s" % rot))
    # a cena do payoff virou a 2 do SHORT, mas a trava do prop e' a mesma
    if "motionless" not in sc.bloco_base(blocos, MAPA, "TAKE", 4).lower():
        achados.append(("ERRO", "o TAKE do payoff sem declaracao de imobilidade "
                                "do prop"))


def lint(spec, blocos):
    return sc.lint_curto(
        base, spec, blocos, MAPA, TETO_FALA,
        literais=("gelatin trick", "prostate"),
        extras=(_pe6_hook, _pe1_roupa_clara, _blocos_travados))


# ---------------------------------------------------------------------------
# RESUMO
# ---------------------------------------------------------------------------

def resumo_pt(spec):
    et = "branca" if "white" in ETNIA[spec["pagina"]] else "negra"
    return ("%s, a mancha escura na calça dele com a plateia em volta. Na cena "
            "2 vem o truque e a virada, e na 3 o CTA. Três cenas, elenco de "
            "pele %s."
            % (PT_LOCAL.get(spec["local"]["id"], "No local"), et))
