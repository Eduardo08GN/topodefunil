#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE NECROSE SHORT — 3 cenas de 8 segundos.

Deriva de `necrose_lucas.py`. Nao ha' uma linha de cena, uma string travada ou
uma tabela de token banido duplicada aqui: tudo isso continua morando no motor
base, e o SHORT herda toda correcao que entrar la'.

O colapso (decisao do operador, 2026-07-31):

    base 1 · A COMPARACAO   ->  SHORT 1 · O HOOK
    base 4 · A PROVA        ->  SHORT 2 · RITUAL + PROVA   (a copy funde 3 e 4)
    base 5 · CTA            ->  SHORT 3 · CTA

⚠️ A IMAGEM da cena 2 e' a do PAYOFF (o geoduck erguido, NE11), nao a da
bancada do ritual. A copy fundida termina em deitico — "came back like this" —
e esse "this" precisa ter no que apontar. O ritual vive na fala; o resultado,
no quadro.

⛔ O QUE O COLAPSO AMEACAVA
As cenas 2 e 3 do base levam embora DUAS coisas obrigatorias: o literal
`gelatin trick` (que morava nas RECEITAS_FALA da cena 3) e o MUP `blood flow`
(que morava nas CAUSAS da cena 2). Sem o primeiro o criativo deixa de ser
congruente com o que a VSL vende; sem o segundo o video promete sem explicar.
Por isso **os dois entram na copy fundida**, e o linter trava nos dois.

Some-se o NE10: a placa D1 em corte sagital era a cena 2 e nao sobrevive. Ela
e' a peca que EXPLICA, e no SHORT nao ha' tempo para explicar — a explicacao
virou a oracao de `blood flow` dentro da cena 2.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import necrose_lucas as base                                   # noqa: E402
import short_comum as sc                                       # noqa: E402

# o que a UI le' direto do motor base, sem intermediario
from necrose_lucas import (ETNIA, NUCLEO, EIXOS_UI, BARREIRAS,   # noqa: E402,F401
                           PT_ARQ, PT_REC, _palavras)

AQUI = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(AQUI, ".necrose-short-ledger.json")

TITULO = "AGENTE NECROSE SHORT"
SUBTITULO = "os dois órgãos lado a lado, em 3 cenas · gerador offline de prompts Veo"
SLUG = "necrose-short"

MAPA = (1, 4, 5)
CENAS_UI = ["1 · O HOOK", "2 · RITUAL + PROVA", "3 · CTA"]

# As pontas herdam o teto do motor base: sao os MESMOS pools, entao inventar
# outro numero aqui so' criaria duas verdades. So' a cena 2 tem teto proprio,
# porque a copy dela e' propria. 34 palavras em 8s e' leitura de anuncio, nao
# conversa — e e' o mesmo limite da cena mais carregada da versao longa. Acima
# disso o Veo atropela: foi medido em 45 e a fala saiu embolada.
TETO_FALA = {1: base.TETO_FALA[1], 2: 34, 3: base.TETO_FALA[5]}


# ---------------------------------------------------------------------------
# A COPY FUNDIDA — cena 2
# ---------------------------------------------------------------------------
# ⚠️ CURADORIA DO OPERADOR. Todo item aqui e' copy nova, escrita a partir dos
# fragmentos ja' validados das RECEITAS_FALA, CAUSAS e PROVAS do motor base.
# Nenhum item entra ou sai desta lista sem passar por ele.
#
# Cada item e' obrigado a carregar, na mesma respiracao:
#   1. o mecanismo   -> a string literal `blood flow`
#   2. o ritual      -> a string literal `gelatin trick` + o ingrediente {ing}
#   3. a prova       -> a evidencia em 1a pessoa, terminando em deitico
# O linter confere 1 e 2. O 3 e' julgamento.
#
# ⚠️ SEM {barreira} — e a ausencia e' deliberada. O ingrediente {ing} sozinho
# custa ~12 palavras e a barreira mais ~10; com os dois a cena batia em 45
# palavras, 5,6 por segundo, e o Veo atropela a fala. Os tres beats acima sao
# obrigatorios; a barreira e' tranquilizacao, e o funil ja' a repete adiante.
# ⛔ Nao devolver a barreira aqui sem cortar outra coisa.
# ⚠️ TODO item carrega `{o}`. Sem ele a cota do orgao cai para 1/3 (o CTA nao
# nomeia o orgao), e o linter reprova o sorteio inteiro. Medido: um unico
# template sem `{o}` reprovou 48 de 300 sorteios.
FUNDIDAS = [
    "Stir {ing}. That's the gelatin trick — it opens the blood flow your {o} "
    "lost. Mine came back like this.",

    "That's blood flow, choked off. Stir {ing} — the whole gelatin trick, and "
    "it walked my {o} back.",

    "The blood flow to your {o} got choked off. Stir {ing}. That's the gelatin "
    "trick, and this is me now.",

    "It's not age — the blood flow got strangled. Stir {ing}. That's the "
    "gelatin trick, and my {o} hasn't quit since.",

    "Stir {ing}. That's the gelatin trick, and the blood flow came back. So did "
    "my {o}.",
]


def _fundir(spec, rng):
    o = sc.orgao_de(base, spec["falas_base"][3], "soldier")
    return rng.choice(FUNDIDAS).format(o=o, ing=spec["receita"]["fala"])


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
    for eixo, val in (("arquetipo", spec["arquetipo"]["id"]),
                      ("familia", spec["arquetipo"]["familia"]),
                      ("receita", spec["receita"]["id"]),
                      ("mesa", spec["mesa"]["id"])):
        p.setdefault(eixo, []).append(val)
        p[eixo] = p[eixo][-12:]
    with open(LEDGER, "w", encoding="utf-8") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)


def sortear(pagina, rng, ledger):
    return sc.sortear_curto(base, pagina, rng, ledger, MAPA, _fundir)


def montar(spec):
    return sc.montar_curto(base, spec, MAPA)


def nova_fala(spec, i, rng):
    return sc.nova_fala_curta(base, spec, i, rng, MAPA, _fundir)


def _recopiar_receita(spec, rng):
    """A receita entra na fala fundida — trocar o prop exige reescreve-la."""
    spec["falas"][1] = _fundir(spec, rng)


EIXOS_QUE_MEXEM_NA_COPY = {"receita": _recopiar_receita}


# ---------------------------------------------------------------------------
# LINTER — as regras do NECROSE que sobrevivem ao colapso
# ---------------------------------------------------------------------------

def _limpar_animal(spec, direcao):
    # 'big' e' banido como adjetivo de DIMENSAO DE PROP e casava com
    # "a big chestnut quarter horse" em todo sorteio de cowboy/redneck
    for forma in (spec["animal"], spec["animal"].replace("a ", "", 1)):
        direcao = direcao.replace(forma, "")
    return direcao


def _ne7_hook(spec, blocos, achados):
    """O hook e' a comparacao: dois deiticos, condicional e orgao nomeado."""
    import re
    h = spec["falas"][0].lower()
    d = len(re.findall(r"\bthis\b|\bthese\b|\bthe other one\b|\bthat one\b", h))
    if d < 2:
        achados.append(("ERRO", "NE7: o hook nao aponta os DOIS modelos — "
                                "precisa de dois deiticos (%d encontrado)" % d))
    if not re.search(r"\bif\b", h) and not spec["falas"][0].rstrip().endswith("?"):
        achados.append(("ERRO", "NE7: o hook AFIRMA o estado do corpo dele. Tem "
                                "que ser condicional ('if...') ou pergunta — "
                                "claim de cura e a primeira linha da cerca"))
    if not any(n.lower() in h for n in NUCLEO):
        achados.append(("ERRO", "NE7: o hook nao nomeia o orgao com substantivo"))


def _blocos_travados(spec, blocos, achados):
    i1 = sc.bloco_base(blocos, MAPA, "IMAGE", 1)
    for s, rot in ((base.MODELO_PODRE, "modelo podre NE2"),
                   (base.MODELO_SAO, "modelo sao NE2")):
        if s not in i1:
            achados.append(("ERRO", "IMAGE 01 sem a string travada: %s" % rot))
    if "identical" not in i1:
        achados.append(("ERRO", "NE2: falta 'identical' na abertura do modelo sao "
                                "— sem isso o Veo desenha dois objetos diferentes"))
    if base.IMOBILIDADE_PAR not in sc.bloco_base(blocos, MAPA, "TAKE", 1):
        achados.append(("ERRO", "TAKE 01 sem a imobilidade do PAR (NE8)"))

    # NE11 — o payoff virou a cena 2 do SHORT, mas as travas sao as mesmas
    if base.GEODUCK_PAYOFF not in sc.bloco_base(blocos, MAPA, "IMAGE", 4):
        achados.append(("ERRO", "NE11: a cena do payoff sem a string travada do "
                                "geoduck (a spec dimensional e o que impede o "
                                "tamanho natural)"))
    if base.GEODUCK_TAKE not in sc.bloco_base(blocos, MAPA, "TAKE", 4):
        achados.append(("ERRO", "NE11: o TAKE do payoff sem a imobilidade + "
                                "negacao de ave"))

    # NE4 — o animal de status nas duas cenas que sobraram com ele
    nucleo_animal = spec["animal"].replace("a ", "", 1)
    for cena in (1, 4):
        nome = "IMAGE %02d/03" % (MAPA.index(cena) + 1)
        if nucleo_animal.lower() not in blocos[nome].lower():
            achados.append(("ERRO", "NE4: %s sem o animal de status (%s)"
                            % (nome, nucleo_animal)))

    # NE9 — todas as cenas sao solo
    for nome in sorted(k for k in blocos if k.startswith("IMAGE")):
        if "only person in the frame" not in blocos[nome].lower():
            achados.append(("AVISO", "NE9: %s nao declara que ele esta sozinho" % nome))


def lint(spec, blocos):
    return sc.lint_curto(
        base, spec, blocos, MAPA, TETO_FALA,
        literais=("gelatin trick", "blood flow"),
        limpar_direcao=_limpar_animal,
        extras=(_ne7_hook, _blocos_travados))


# ---------------------------------------------------------------------------
# RESUMO
# ---------------------------------------------------------------------------

def resumo_pt(spec):
    et = "branca" if "white" in ETNIA[spec["pagina"]] else "negra"
    return ("%s, o %s de %d anos sem camisa e muito musculoso mostra os dois "
            "órgãos lado a lado. Na cena 2 ele ergue só o são contra o céu "
            "enquanto conta %s (o gelatin trick), e na 3 vem o CTA. Três cenas, "
            "elenco de pele %s."
            % (PT_ARQ.get(spec["arquetipo"]["id"], "No cenário"),
               spec["arquetipo"]["familia"], spec["ref"]["idade"],
               PT_REC.get(spec["receita"]["id"], "o ritual"), et))
