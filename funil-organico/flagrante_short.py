#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE FLAGRANTE SHORT — 3 cenas de 8 segundos.

Deriva de `flagrante_lucas.py`. Nenhuma string travada, pool ou tabela de token
banido e' duplicada aqui.

    base 1 · RUINA      ->  SHORT 1 · O FLAGRANTE
    base 4 · REDENCAO   ->  SHORT 2 · O TRUQUE + A VIRADA   (funde 2 e 4)
    base 5 · CTA        ->  SHORT 3 · CTA

⛔ O QUE O COLAPSO AMEACAVA
No FLAGRANTE o literal `gelatin trick` morava nas DESCOBERTAS — **a cena 2**,
que nao sobrevive. Junto com ele ia embora o MUP (`blood flow`), que vive na
mesma frase daquele pool. Os dois entram na copy fundida, e o linter trava.

⚠️ O QUE SE PERDE, e e' consciente: o **F16** (a placa D1 em corte sagital na
cena 2) nao tem onde morar num video de tres cenas. A explicacao anatomica cede
lugar a oracao de `blood flow` dentro da cena 2. Quem quiser o D1 usa a versao
longa.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import flagrante_lucas as base                                  # noqa: E402
import short_comum as sc                                        # noqa: E402

from flagrante_lucas import (ETNIA, NUCLEO, EIXOS_UI, BRAGGING,  # noqa: E402,F401
                             QUEM_CONTOU, PT_OCASIAO, _palavras)

AQUI = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(AQUI, ".flagrante-short-ledger.json")

TITULO = "AGENTE FLAGRANTE SHORT"
SUBTITULO = "humilhação pública, em 3 cenas · gerador offline de prompts Veo"
SLUG = "flagrante-short"

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
CENAS_UI = ["1 · O FLAGRANTE", "2 · O TRUQUE + A VIRADA", "3 · CTA PREPARANDO"]

# ⚠️ Aqui as pontas NAO herdam o teto do motor base, e a excecao e' medida:
# os tetos do FLAGRANTE base estao defasados em relacao aos proprios pools
# dele — em 300 sorteios a cena 1 estoura o teto 22 em 69% das vezes e a cena
# 5 estoura o teto 24 em 49%. Herdar isso faria o linter do SHORT gritar em
# dois de cada tres videos, e aviso que sempre dispara e' aviso que ninguem le.
# Os numeros abaixo sao o p90 medido de cada pool herdado.
# ⛔ Recalibrar os tetos do motor BASE e' decisao do operador — nao foi feito.
TETO_FALA = {1: 24, 2: 34, 3: 28}


# ---------------------------------------------------------------------------
# A COPY FUNDIDA — cena 2
# ---------------------------------------------------------------------------
# ⚠️ CURADORIA DO OPERADOR. Copy nova, montada a partir dos fragmentos ja'
# validados das DESCOBERTAS e REDENCOES do motor base.
#
# Todo item carrega, na mesma respiracao:
#   1. quem contou   -> {quem}, que e' o que faz a descoberta soar boca-a-boca
#   2. o mecanismo   -> `blood flow`
#   3. o ritual      -> `gelatin trick`
#   4. a virada      -> a mulher, dezenove dias depois
# ⛔ Sem {barreira}: a cena ja' carrega quatro beats e estourava o teto.
# ⚠️ Todo item precisa de `{o}` — o CTA nao nomeia o orgao, entao sem ele a
# cota cai para 1/3 e o linter reprova o sorteio.
FUNDIDAS = [
    "That's when {quem} gave him the gelatin trick. It's not age — the blood "
    "flow to your {o} got choked off. Nineteen days later she's {brag} about "
    "his.",

    "{quem} handed him the gelatin trick. Blood flow, brother, not your age. "
    "Nineteen days later she wouldn't get off his knee, and his {o} was ready.",

    "{quem} pulled him aside with the gelatin trick — the blood flow stopped "
    "reaching your {o}. Nineteen days later she's the one {brag} about his.",

    "That's when {quem} told him about the gelatin trick. It's blood flow, not "
    "you. Nineteen days later the same men who laughed asked about his {o}.",

    "{quem} gave him the gelatin trick that night. The blood flow to your {o} "
    "got choked off, and it is fixable. Nineteen days later she reaches for "
    "him first.",
]


def _fundir(spec, rng):
    o = sc.orgao_de(base, spec["falas_base"][3])
    return rng.choice(FUNDIDAS).format(
        o=o, quem=rng.choice(QUEM_CONTOU), brag=rng.choice(BRAGGING))


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
    for eixo, val in (("ocasiao", spec["ocasiao"]["id"]),
                      ("prop", spec["prop"]["id"]),
                      ("ambiente", spec["ambiente"]["id"])):
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
    img, take = sc.bancada_com_rosto(base, spec, spec["falas"][2])
    b["IMAGE 03/03"], b["TAKE 03/03"] = img, take
    return b


def nova_fala(spec, i, rng):
    return sc.nova_fala_curta(base, spec, i, rng, MAPA, _fundir, MAPA_COPY)


def _recopiar_ocasiao(spec, rng):
    """A ocasiao entra no hook e no eco da cena fundida — trocar exige reescrever."""
    spec["falas"][0] = base.nova_fala(sc.espelho(spec, MAPA), 0, rng)
    spec["falas"][1] = _fundir(spec, rng)


EIXOS_QUE_MEXEM_NA_COPY = {"ocasiao": _recopiar_ocasiao}


# ---------------------------------------------------------------------------
# LINTER
# ---------------------------------------------------------------------------

def _imobilidade(spec, blocos, achados):
    # as duas cenas com prop na mao sobrevivem: a ruina e a redencao
    for cena in (1, 4):
        nome = "TAKE %02d/03" % (MAPA.index(cena) + 1)
        if "motionless" not in blocos[nome].lower():
            achados.append(("ERRO", "%s sem declaracao de imobilidade do prop" % nome))


def lint(spec, blocos):
    return sc.lint_curto(
        base, spec, blocos, MAPA, TETO_FALA,
        literais=("gelatin trick", "blood flow"),
        extras=(_imobilidade,))


# ---------------------------------------------------------------------------
# RESUMO
# ---------------------------------------------------------------------------

def resumo_pt(spec):
    et = "branca" if "white" in ETNIA[spec["pagina"]] else "negra"
    return ("%s, o colega segura %s no próprio colo enquanto o narrador aponta "
            "e a mesa ri. Na cena 2 vem o truque e a virada com a esposa, e na "
            "3 o CTA. Três cenas, elenco de pele %s."
            % (PT_OCASIAO.get(spec["ocasiao"]["id"], "No evento"),
               spec["prop"].get("pt", "o prop"), et))
