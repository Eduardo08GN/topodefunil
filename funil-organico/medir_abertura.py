#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
medir_abertura.py — a PRIMEIRA sentenca de cada cena tem referente?

⛔ POR QUE ESTE MEDIDOR EXISTE (licoes-de-construcao §21, 2026-08-04)

O operador leu um take renderizado e parou o lote:

    "I read every forum there is and found nothing"
    telespectador: "read WHAT? WTF? What the hell is she talking about?"

E deu a regra:

    "Sempre leia: se a sentenca da' afirmativo para possibilidade do leitor
     dizer «wtf he/she talking about?», e' drifting de copy vaga, e' DESCARTE
     de copy."

⚠️⚠️ A UNIDADE E' A PRIMEIRA SENTENCA, e e' por isso que este medidor precisou
existir mesmo com quatro lentes ja' rodando. Todas elas cobravam o lugar errado:

    cota do orgao ............ cobra a CENA        -> passa com o orgao na 3a frase
    §20 / RE12 ............... cobra a ULTIMA frase -> nao olha a abertura
    RE20 ..................... cobra o beat do vilao
    medir_contexto_copy ...... cobra causa sem alvo

O espectador chega no meio do scroll e ouve as sentencas EM SERIE. A primeira
chega sozinha, sem nada antes dela, e e' ela que decide se ele fica. Quem
escreve tem a cena inteira na memoria de trabalho e nao sente a falta.

⚠️ E A DESCULPA DO ORCAMENTO FOI MEDIDA E CAIU. A hipotese era que a copy ficava
curta para caber nos 8s. A coluna `folga` deste relatorio existe para responder
isso com numero: na primeira medicao (2026-08-04) as aberturas orfas tinham
folga MEDIA de +1,9 a +7,2 palavras. O espaco existia.

⛔⛔ O QUE ESTE MEDIDOR **NAO** DECIDE — leia antes de sair corrigindo copy.

Ele acha CANDIDATOS, nao veredictos. Quem julga e' o TESTE WTF, lido a olho:
*"da' para o espectador perguntar «do que ela esta' falando?»"*. Medido no
ESCANDALO logo depois da correcao da cena 2, ele acusou como orfas:

    "Guys still putting the cucumber in the donut at seventy do one thing first."
    "Your banana, her donut, five nights a week at sixty-five."

Essas frases NAO sao vagas — a metafora do prop (`cucumber in the donut`) diz ao
espectador exatamente do que se trata, e e' o hook fundador do agente. O medidor
as reprova so' porque procura substantivo do NUCLEO ou pessoa com posse, e a
metafora nao e' nenhum dos dois.

⚠️ E' o mesmo modo de falha da §16: lente que reprova o que esta' certo. Aqui ela
fica assim DE PROPOSITO — ampliar o padrao para aceitar metafora exigiria
codificar "o que o espectador entende", que nao e' regex. Por isso:

    o numero e' PONTO DE PARTIDA, a lista de frases e' o trabalho,
    e o veredito de cada uma e' humano.

⛔ Corolario: **nao use `--gate` como aceite automatico de motor** enquanto o
pool do agente usar metafora de prop no hook.

Uso:
    python funil-organico/medir_abertura.py
    python funil-organico/medir_abertura.py --motor escandalo_short --exemplos 8
    python funil-organico/medir_abertura.py --autoteste
    python funil-organico/medir_abertura.py --gate --motor escandalo_short
"""

import argparse
import importlib
import os
import random
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

# ⛔⛔ ESTA LISTA E' MANTIDA A MAO, e ficou DOZE motores atrasada — de 14 num
# parque de 26. Motor que nao esta' aqui nao e' medido, e "sem achado" nele
# significa "ninguem olhou", nao "esta' limpo". E' a §16 na forma mais barata de
# cometer: a regra media o que ja' estava na lista.
# ⚠️ Motor novo entra AQUI no mesmo commit em que nasce — junto com as listas do
# `medir_teto_fala`, `medir_deiticos`, `medir_contexto_copy` e `medir_alcance`.
MOTORES = ["clean_short", "clean_short_v2", "escandalo_short", "troca_short",
           "organicwave_short", "ressurreicao_short", "flagrante_short",
           "pee_short", "vazamento_short", "necrose_short", "exterior_short",
           "colo_short", "receita_short", "botica_short",
           # + 2026-07-28/08-05: os cinco motor-only, sem `AGENTE_ED_*.md`
           "dupla_short", "placa_short", "cha_short", "trio_short",
           "falta_short",
           # + 2026-08-08: a familia 16s — 2 takes de 8s, AdBatch Vertical 2
           "trio16_short", "dupla16_short", "falta16_short", "placa16_short",
           "troca16_short", "botica16_short", "colo16_short",
           "exterior16_short", "escandalo16_short",
           "ressurreicao16_short",
           "flagrante16_short",
           "good16_short",
           # + 2026-08-10: o BED 16, no commit em que nasce
           "bed16_short", "necrose16_short", "wife16_short"]

# ⭐ O QUE CONTA COMO REFERENTE, e a lista e' deliberadamente CURTA:
#   · o orgao (o pool NUCLEO do proprio motor), ou
#   · a pessoa dona do problema, nomeada com posse (`my husband`, `his wife`).
# ⛔ `it`, `this`, `that` NAO contam — sao exatamente o vicio que se mede.
PESSOA = re.compile(
    r"\b(my|his|her|your|our)\s+"
    r"(husband|wife|man|woman|partner|guy|old man|father|brother)\b"
    r"|\b(my|his|her)\s+\w+'s\b", re.I)


def sentencas(t):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", t or "") if s.strip()]


def tem_referente(frase, nucleo):
    baixo = frase.lower()
    return any(n in baixo for n in nucleo) or bool(PESSOA.search(frase))


def _palavras(s):
    return len(re.sub(r"\{\w+\}", "x", s or "").split())


def medir(nome, n=120, pagina="joe"):
    """Devolve (total, orfas, folga_media, exemplos) daquele motor."""
    m = importlib.import_module(nome)
    nucleo = [x.lower() for x in getattr(m, "NUCLEO", [])]
    teto = getattr(m, "TETO_FALA", {}) or {}
    total = orfas = 0
    folgas, exemplos = [], []
    for s in range(n):
        try:
            spec = m.sortear(pagina, random.Random(s), {})
        except Exception:
            break
        for i, fala in enumerate(spec["falas"], 1):
            sents = sentencas(fala)
            if not sents:
                continue
            total += 1
            if tem_referente(sents[0], nucleo):
                continue
            orfas += 1
            if teto.get(i):
                folgas.append(teto[i] - _palavras(fala))
            if len(exemplos) < 40:
                exemplos.append((i, sents[0]))
    folga = (sum(folgas) / float(len(folgas))) if folgas else 0.0
    return total, orfas, folga, exemplos


def autoteste():
    """⛔ Controles ANTES de qualquer numero ser olhado (licoes §16).

    O caso que o operador reprovou entra como controle NEGATIVO — se o medidor
    aprovar justamente ele, esta' medindo outra coisa.
    """
    nucleo = ["johnson", "pecker", "wiener", "soldier", "tool"]
    reprova = [
        "I read every forum there is and found nothing.",   # o caso do operador
        "She noticed.",
        "Two years of pills and nothing.",
        "It came back three times harder.",
        "That never worked on anybody.",
    ]
    aprova = [
        "I read every forum looking for something for his Johnson.",
        "She noticed my pecker harder than ever.",
        "Two years of pills and nothing moved his wiener.",
        "My husband stopped touching me.",
        "Nothing worked for his tool.",
    ]
    falhas = []
    for f in reprova:
        if tem_referente(f, nucleo):
            falhas.append("APROVOU o que devia reprovar: %r" % f)
    for f in aprova:
        if not tem_referente(f, nucleo):
            falhas.append("REPROVOU o que devia aprovar: %r" % f)
    if falhas:
        print(">> MEDIDOR CEGO:")
        for f in falhas:
            print("   %s" % f)
    else:
        print("autoteste do medidor: ok "
              "(5 controles negativos + 5 positivos, incluindo o caso do operador)")
    return 1 if falhas else 0


def main():
    ap = argparse.ArgumentParser(
        description="Mede aberturas de cena sem referente (o teste WTF)")
    ap.add_argument("--motor", choices=MOTORES)
    ap.add_argument("--n", type=int, default=120)
    ap.add_argument("--exemplos", type=int, default=2)
    ap.add_argument("--gate", action="store_true",
                    help="sai 1 se houver qualquer abertura orfa")
    ap.add_argument("--autoteste", action="store_true")
    a = ap.parse_args()

    if a.autoteste:
        return autoteste()
    if autoteste():
        return 1

    alvos = [a.motor] if a.motor else MOTORES
    print()
    print("%-22s %6s %6s %8s  %s" % ("motor", "cenas", "orfas", "%", "folga media"))
    print("-" * 72)
    pior = 0
    for nome in alvos:
        total, orfas, folga, exemplos = medir(nome, a.n)
        if not total:
            continue
        pior += orfas
        print("%-22s %6d %6d %7.1f%%  %+.1f palavras"
              % (nome, total, orfas, 100.0 * orfas / total, folga))
        vistos = set()
        for i, frase in exemplos:
            if frase in vistos:
                continue
            vistos.add(frase)
            if len(vistos) > a.exemplos:
                break
            print("        cena %d | %s" % (i, frase))
    print()
    # ⛔ ASCII de proposito: o console do Windows e' cp1252 e o `⚠️` levanta
    # UnicodeEncodeError — exatamente o bug ja' documentado nos autotestes do
    # COLO e do ESCANDALO, que eu repeti ao escrever este arquivo.
    print(">> Folga POSITIVA significa que sobrava espaco na fala: a copy nao "
          "ficou vaga por falta de lugar (licoes 21).")
    return 1 if (a.gate and pior) else 0


if __name__ == "__main__":
    raise SystemExit(main())
