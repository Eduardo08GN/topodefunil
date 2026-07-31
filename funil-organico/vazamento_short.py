#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE VAZAMENTO SHORT — 3 cenas de 8 segundos.

Deriva de `vazamento_lucas.py`. Nenhuma string travada, pool ou tabela e'
duplicada.

    base 1 · O VAZAMENTO        ->  SHORT 1 · O VAZAMENTO
    base 4 · MECANISMO + PROVA  ->  SHORT 2 · A RECEITA INCOMPLETA + A PROVA
    base 5 · CTA                ->  SHORT 3 · CTA

⛔ ESTE FOI O COLAPSO MAIS DELICADO DOS QUATRO
O angulo do VAZAMENTO **e'** a receita incompleta: a cena 2 dava metade da
receita (o bicarbonato) e a cena 3 revelava que sem o gelatin trick aquela
metade nao faz nada. As duas caem — ou seja, cai a isca E cai a virada, que
juntas sao o mecanismo inteiro do agente.

A copy fundida resolve as duas numa frase so': ela **introduz e revela na mesma
respiracao** ("baking soda alone does nothing without the gelatin trick"). Fica
mais apertado e, honestamente, mais direto — mas quem quiser a isca de verdade,
com o espectador anotando a receita antes da virada, usa a versao longa.

O linter trava na negacao literal `without the gelatin trick` (V6), que e' o
que impede a fundida de virar so' mais uma promessa.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import vazamento_lucas as base                                   # noqa: E402
import short_comum as sc                                         # noqa: E402

from vazamento_lucas import (ETNIA, NUCLEO, EIXOS_UI, BARREIRAS,  # noqa: E402,F401
                             PT_COZ, PT_QUI, _palavras, _idade_slots)

AQUI = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(AQUI, ".vazamento-short-ledger.json")

TITULO = "AGENTE VAZAMENTO SHORT"
SUBTITULO = "o corpo-prova e a receita incompleta, em 3 cenas · prompts Veo"
SLUG = "vazamento-short"

# ⭐ MAPA e' de onde vem a IMAGEM; MAPA_COPY e' de onde vem a FALA. A cena 3
# junta as duas coisas: a fala do CTA (base 5) por cima da cena do ritual.
#
# ⚠️ Ordem do operador, 2026-07-31: "estamos deixando espaco valioso nesses 22
# segundos apertados no lixo". A cena 3 era o close do CTA — um terco do video
# num talking head, zero informacao visual. Agora o espectador OUVE o pedido e
# VE o gelatin trick nos mesmos 8 segundos.
#
# No VAZAMENTO a cena que ja' tem rosto E maos trabalhando e' a 2 (a
# receita-isca: ele despeja o bicarbonato e mexe, falando com a camera). Ela
# fecha o arco em vez de brigar com ele — a fundida diz que bicarbonato sozinho
# nao faz nada, e o CTA por cima da imagem dele mexendo o bicarbonato oferece
# justamente a outra metade da receita.
MAPA = (1, 4, 2)
MAPA_COPY = (1, None, 5)          # None = a fundida
CENAS_UI = ["1 · O VAZAMENTO", "2 · A RECEITA INCOMPLETA + A PROVA",
            "3 · CTA PREPARANDO"]

# As pontas herdam o teto do motor base — mesmos pools, mesma regua.
TETO_FALA = {1: base.TETO_FALA[1], 2: 36, 3: base.TETO_FALA[5]}


# ---------------------------------------------------------------------------
# A COPY FUNDIDA — cena 2
# ---------------------------------------------------------------------------
# ⚠️ CURADORIA DO OPERADOR. Copy nova, montada dos fragmentos ja' validados das
# VIRADAS e PROVAS do motor base.
#
# Todo item carrega, na mesma respiracao:
#   1. a isca + a virada -> `without the gelatin trick` + o bicarbonato inutil
#   2. o mecanismo       -> `blood flow`
#   3. a prova           -> a moca, metade da idade dele
# ⛔ Sem {barreira}: tres beats ja' enchem os 8 segundos.
# ⚠️ Todo item precisa de `{o}` — o CTA nao nomeia o orgao.
FUNDIDAS = [
    "Without the gelatin trick, baking soda alone does nothing for your {o} — "
    "that's blood flow, choked off. She's {n_ext}, half my age, and she can't "
    "keep her hands off mine.",

    "Baking soda is half a recipe: without the gelatin trick your {o} stays "
    "down, because the blood flow is choked off. She's {n_ext} and she reaches "
    "for me first now.",

    "Without the gelatin trick that baking soda does nothing for your {o} — "
    "your blood flow got squeezed shut, not your age. Thirty-{n} years old, "
    "and she won't wait.",

    "Nobody gave you the other half, brother. Without the gelatin trick the "
    "baking soda leaves your {o} down and the blood flow shut. She's {n_ext} "
    "and she needed a minute.",

    "Without the gelatin trick, baking soda is half a recipe and the blood flow "
    "never reaches your {o}. She's {n_ext}, half my age, and she calls me every "
    "night.",
]


def _fundir(spec, rng):
    o = sc.orgao_de(base, spec["falas_base"][3])
    return rng.choice(FUNDIDAS).format(o=o, **_idade_slots(spec["mulher"]["idade"]))


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
    for eixo, val in (("cozinha", spec["cozinha"]["id"]),
                      ("quintal", spec["quintal"]["id"]),
                      ("prop", spec["prop"]["id"])):
        p.setdefault(eixo, []).append(val)
        p[eixo] = p[eixo][-12:]
    with open(LEDGER, "w", encoding="utf-8") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)


def sortear(pagina, rng, ledger):
    return sc.sortear_curto(base, pagina, rng, ledger, MAPA, _fundir, MAPA_COPY)


def _cena3(spec):
    """A bancada do VAZAMENTO sem o bicarbonato em quadro.

    ⚠️ A cena 2 do motor longo — que o MAPA usaria — e' literalmente ele
    despejando uma caixa de bicarbonato. Ordem do operador: no take 3 do SHORT
    o preparo e' so' gelatina e agua. Set, pessoa, luz e cauda continuam vindo
    do motor base; so' o que esta' em cima da mesa mudou, e mudou para a string
    travada de short_comum.
    """
    et = ETNIA[spec["pagina"]]
    ref, qui = spec["ref"], spec["quintal"]
    img = (
        "IMAGE 03/03: Medium shot in %s. Standing behind a weathered wooden "
        "table is the same %d-year-old %s man, %s, now wearing %s, thick "
        "forearms bare. On the table: %s. He is mid-action, both hands at the "
        "glass, speaking and looking directly at the camera. He is alone in "
        "the frame. %s The scene is lit by %s %s"
        % (qui["set"], ref["idade"], et, ref["marca"], ref["roupa2"],
           sc.MESA_GELATINA, base.ANTICELEB, qui["luz"], base.CAUDA)
    )
    take = (
        "TAKE 03/03: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway, no cuts. The %d-year-old man speaks to the "
        "camera while his hands work: %s. His eyes stay on the lens the whole "
        "time. He is the only person in the shot.\n"
        "Dialogue: \"%s\"\n"
        "Audio: outdoor ambient — distant birds, faint breeze, a spoon against "
        "glass. No music."
        % (ref["idade"], sc.ACAO_GELATINA, base.sonorizar(spec["falas"][2]))
    )
    return img, take


def montar(spec):
    b = sc.montar_curto(base, spec, MAPA)
    b["IMAGE 03/03"], b["TAKE 03/03"] = _cena3(spec)
    return b


def nova_fala(spec, i, rng):
    return sc.nova_fala_curta(base, spec, i, rng, MAPA, _fundir, MAPA_COPY)


EIXOS_QUE_MEXEM_NA_COPY = {}


# ---------------------------------------------------------------------------
# LINTER
# ---------------------------------------------------------------------------

def _hook(spec, blocos, achados):
    h = spec["falas"][0].lower()
    if not any(n.lower() in h for n in NUCLEO):
        achados.append(("ERRO", "o hook nao nomeia o orgao com substantivo"))
    if "blood flow" not in h:
        achados.append(("ERRO", "o hook nao nomeia o mecanismo (blood flow)"))


def _v6_negacao(spec, blocos, achados):
    """A virada virou a cena 2 do SHORT, mas a negacao continua obrigatoria."""
    f2 = spec["falas"][1].lower()
    if not any(n.lower() in f2 for n in NUCLEO):
        achados.append(("ERRO", "V6: a virada nao nomeia o orgao na mesma frase"))
    if "blood flow" not in f2:
        achados.append(("ERRO", "V6: falta o MUP emendado (o fluxo estrangulado)"))


def _blocos_travados(spec, blocos, achados):
    i1 = sc.bloco_base(blocos, MAPA, "IMAGE", 1)
    t1 = sc.bloco_base(blocos, MAPA, "TAKE", 1)
    for txt, s, rot in ((i1, base.GEODUCK_IMAGE, "geoduck V1"),
                        (i1, base.VAZAMENTO_IMAGE, "vazamento V2"),
                        (t1, base.GEODUCK_TAKE, "imobilidade V1"),
                        (t1, base.VAZAMENTO_TAKE, "poca V2")):
        if s not in txt:
            achados.append(("ERRO", "a cena do vazamento sem a string travada: %s" % rot))

    # V12 — a cena do casal virou a 2 do SHORT; a declaracao de idade dos DOIS
    # continua sendo o que segura o classificador
    i4 = sc.bloco_base(blocos, MAPA, "IMAGE", 4)
    if "fully clothed adults" not in i4:
        achados.append(("ERRO", "V12: a cena do casal sem a linha de abertura "
                                "declarando 'two fully clothed adults' com as "
                                "duas idades"))
    if i4.count("-year-old") < 2:
        achados.append(("ERRO", "V12: idade dos dois precisa estar em TODA mencao "
                                "na cena do casal (falha de classificador "
                                "documentada)"))

    # V10 — os DOIS sets sobrevivem agora que a cena 3 e' a bancada externa
    if "American flag" not in i1:
        achados.append(("AVISO", "V10: sem bandeira dos EUA no set interno"))
    if "American flag" not in sc.bloco_base(blocos, MAPA, "IMAGE", 2):
        achados.append(("AVISO", "V10: sem bandeira dos EUA no set externo"))

    # V8 — as cenas solo que sobraram
    for cena in (1, 2):
        nome = "IMAGE %02d/03" % (MAPA.index(cena) + 1)
        if "alone in the frame" not in blocos[nome]:
            achados.append(("AVISO", "V8: %s nao declara que ele esta sozinho" % nome))


def lint(spec, blocos):
    return sc.lint_curto(
        base, spec, blocos, MAPA, TETO_FALA,
        literais=("gelatin trick", "without the gelatin trick", "blood flow"),
        extras=(_hook, _v6_negacao, _blocos_travados))


# ---------------------------------------------------------------------------
# RESUMO
# ---------------------------------------------------------------------------

def resumo_pt(spec):
    et = "branca" if "white" in ETNIA[spec["pagina"]] else "negra"
    return ("Na %s, o corpo-prova de %d anos segura o geoduck que vaza. Na cena "
            "2 vem a receita incompleta e a prova com a moça, e na 3 o CTA. "
            "Três cenas, elenco de pele %s."
            % (PT_COZ.get(spec["cozinha"]["id"], "cozinha"),
               spec["ref"]["idade"], et))
