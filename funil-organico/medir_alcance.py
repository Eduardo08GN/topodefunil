# -*- coding: utf-8 -*-
"""[ALCANCE] — quantas entradas de cada pool NUNCA chegam ao video.

⛔ POR QUE ISTO EXISTE. Entrada de pool que nao cabe somada aos MINIMOS dos
outros beats nunca e' sorteada. Ela nao e' rara: e' MORTA. E o autoteste de cada
motor a conta como opcao viva — o relatorio diz "18 GATES" enquanto a producao
usa 1. E' mode-collapse com relatorio verde.

⭐ O controle nasceu dentro do `trio16_short.py` (2026-08-08) e depois no
`troca_short.py`. Instalar a mao nos dezenove sairia caro e ficaria desatualizado
— aqui a mesma pergunta e' feita DE FORA, pela saida real, e por isso vale para
qualquer motor, tenha ele `_cabem`, `_na_faixa`, `_ok` ou filtro proprio.

⚠️⚠️ A PRIMEIRA VERSAO DESTA SONDA ERROU, e o erro e' instrutivo: ela olhava so'
`spec["falas"]` e acusou 18 dos 19 motores. Pool que alimenta os BLOCOS (traje,
corpo, apelo) nunca aparece na fala — eram falsos positivos em massa, e a
assinatura era visivel de longe: **pools 100% mortos em serie**. Uma lente que
acusa quase todo mundo esta' medindo a coisa errada, nao encontrando uma
epidemia. Com falas + blocos, e separando as tres perguntas abaixo, sobraram 12.

    1. o pool e' referenciado no proprio arquivo?  -> senao, e' POOL ORFAO
    2. quantas entradas aparecem na saida?         -> as demais sao INALCANCAVEIS
    3. quantas falas distintas por cena?           -> o efeito no lote

⛔ SEM `--gate` DE PROPOSITO. Quase todo achado que sobra e' copy longa demais
para o teto, e encurtar copy aprovada e' alcada do operador (CL15). Este arquivo
mostra o numero; a decisao e' dele.

    python funil-organico/medir_alcance.py
    python funil-organico/medir_alcance.py --motor receita --detalhe
"""
import argparse
import collections
import importlib
import os
import random
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
if AQUI not in sys.path:
    sys.path.insert(0, AQUI)

# ⛔ Escopo do repo: os SHORT. `*_lucas` nao existe para nos.
MOTORES = ["clean", "clean_short_v2", "escandalo", "troca", "organicwave",
           "ressurreicao", "flagrante", "pee", "vazamento", "necrose",
           "exterior", "colo", "receita", "botica", "dupla", "placa",
           "cha", "trio", "falta",
           "trio16", "dupla16", "falta16", "placa16", "troca16", "botica16",
           "colo16", "exterior16", "escandalo16", "ressurreicao16", "flagrante16", "good16"]

N = 400
# ⚠️ prefixo curto credita a entrada ERRADA quando duas comecam igual — foi
# exatamente esse o erro de medicao de 2026-08-08 de manha. Abaixo disto, pula.
MIN_PREFIXO = 20


def carregar(nome):
    return importlib.import_module(
        nome if nome.endswith("_v2") else "%s_short" % nome)


def prefixo(x):
    """O trecho literal ate' o primeiro placeholder — o unico pedaco da entrada
    que se pode procurar na saida sem formatar."""
    return re.split(r"[{%]", x)[0].strip()


def pools_de(M):
    """Pools de COPY: lista de strings longas. Descarta listas de tokens curtos
    (cores, nomes), que nao sao copy e nao respondem a teto de fala."""
    out = {}
    for att in dir(M):
        if not att.isupper():
            continue
        v = getattr(M, att)
        if (isinstance(v, list) and len(v) >= 4
                and all(isinstance(x, str) for x in v)
                and sum(len(x) > 25 for x in v) == len(v)):
            out[att] = v
    return out


def medir(nome, n=N):
    M = carregar(nome)
    pools = pools_de(M)
    if not pools:
        return None
    fonte = open(M.__file__, encoding="utf-8").read()
    orfaos = [a for a in pools if len(re.findall(r"\b%s\b" % a, fonte)) <= 1]

    pags = sorted(getattr(M, "ETNIA", {"joe": None}))
    vistos = collections.defaultdict(set)
    distintas = collections.defaultdict(set)
    for i in range(n):
        spec = M.sortear(pags[i % len(pags)], random.Random(i), {})
        blocos = M.montar(spec)
        texto = " ".join(spec["falas"]) + " " + " ".join(
            str(x) for x in (blocos.values() if isinstance(blocos, dict)
                             else blocos))
        for c, f in enumerate(spec["falas"], 1):
            distintas[c].add(f)
        for att, v in pools.items():
            for x in v:
                p = prefixo(x)
                if len(p) >= MIN_PREFIXO and p in texto:
                    vistos[att].add(x)

    mortos = []
    for att, v in sorted(pools.items()):
        if att in orfaos:
            continue
        usaveis = [x for x in v if len(prefixo(x)) >= MIN_PREFIXO]
        if len(usaveis) < 4:
            continue
        faltando = [x for x in usaveis if x not in vistos[att]]
        # ⚠️ 0 de N nao e' "pool morto": e' pool que esta sonda nao alcanca
        # (formatacao que apaga o prefixo). Acusar aqui seria o falso positivo
        # de novo — nao acuso, e o `--detalhe` mostra para quem quiser olhar.
        if len(faltando) == len(usaveis):
            continue
        if faltando:
            mortos.append((att, faltando, len(usaveis)))
    return mortos, distintas, orfaos, pools


def main():
    ap = argparse.ArgumentParser(
        description="entradas de pool que nunca chegam ao video")
    ap.add_argument("--motor")
    ap.add_argument("--n", type=int, default=N)
    ap.add_argument("--detalhe", action="store_true",
                    help="lista cada entrada inalcancavel com o tamanho dela")
    a = ap.parse_args()
    alvos = [a.motor] if a.motor else MOTORES

    print("[ALCANCE] falas + blocos, %d sorteios por motor\n" % a.n)
    print("%-14s %-20s %s"
          % ("motor", "falas dist./cena", "inalcancaveis / pools orfaos"))
    print("-" * 100)
    sujos, orf = [], []
    for nome in alvos:
        try:
            r = medir(nome, a.n)
        except Exception as e:                          # noqa: BLE001
            print("%-14s ERRO: %s" % (nome, str(e)[:60]))
            continue
        if r is None:
            print("%-14s (sem pool de copy reconhecivel)" % nome)
            continue
        mortos, dist, orfaos, pools = r
        s_dist = "/".join(str(len(dist[c])) for c in sorted(dist))
        det = []
        if mortos:
            sujos.append(nome)
            det.append("  ".join("%s %d/%d" % (att, len(f), t)
                                 for att, f, t in mortos))
        if orfaos:
            orf.append(nome)
            det.append("ORFAOS: " + ", ".join(sorted(orfaos)))
        print("%-14s %-20s %s" % (nome, s_dist, " | ".join(det) or "ok"))
        if a.detalhe and mortos:
            P = carregar(nome)._palavras
            for att, faltando, _t in mortos:
                print("   %s:" % att)
                for x in faltando:
                    print("      %2d p  %s" % (P(x), x))
    print("\ncom entrada inalcancavel: %d de %d — %s"
          % (len(sujos), len(alvos), ", ".join(sujos) or "-"))
    print("com pool orfao          : %d de %d — %s"
          % (len(orf), len(alvos), ", ".join(orf) or "-"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
