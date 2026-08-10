# -*- coding: utf-8 -*-
"""Gate do TETO DE FALA: nenhuma cena pode gerar mais de 32 palavras.

⛔ POR QUE ISTO EXISTE. O operador, 2026-08-04:
    *"cuidado pra nao extrapolar o teto. Se extrapolou, tem que ajustar senao
     vai ser cortado a fala por ter acabado o tempo do take."*

⚠️ E ele estava apontando para um defeito MUITO maior do que o meu deslize que
provocou o aviso. Medido no dia: SEIS dos quatorze motores geravam fala acima do
teto fisico, e ninguem sabia, porque nenhum medidor olhava para isso:

    vazamento    cena 3 estourava em 53,5% dos sorteios, ate' 48 palavras (6,0 p/s)
    exterior     cena 3 estourava em 95,7%
    vazamento    cena 2 em 32,5%
    organicwave  cena 2 em 9,0%
    flagrante    cena 2 em 6,0%
    necrose      cena 3 em 3,2%

⭐⭐ O TETO E' FISICO, NAO ESTETICO. `licoes-de-construcao.md` §5: capacidade real
de 8 segundos na nossa taxa de fala (3,4-4,0 p/s) = **27-32 palavras**. Passar
disso nao deixa a fala apertada — deixa a fala CORTADA, porque o take termina
antes dela. O espectador ouve meia frase e o CTA morre no ar.

⛔⛔ POR QUE O LINT DE CADA MOTOR NAO PEGAVA. Cada motor ja' tinha a lente do
proprio teto (RE11 e equivalentes) — e ela passava, porque comparava a fala com
o `TETO_FALA` DECLARADO NAQUELE ARQUIVO. Se o teto declarado e' 40, uma fala de
40 palavras passa no lint e e' cortada no render. **A lente conferia coerencia
interna, nao capacidade fisica.** E' a §16 na sua forma mais cara: a regra media
o que era facil medir, nao o que precisava ser verdade.

⚠️ E o `_cabem()` tem um fallback `or pool` que devolve o POOL INTEIRO quando
nada cabe. Ele existe por um bom motivo (lista vazia derrubaria o sorteio com
IndexError em vez de acusar pelo linter), mas e' um caminho de estouro
silencioso: quando o orcamento aperta, ele entrega a fala longa sem reclamar.

    python funil-organico/medir_teto_fala.py           # relatorio
    python funil-organico/medir_teto_fala.py --gate    # exit 1 se algum estoura
    python funil-organico/medir_teto_fala.py --motor vazamento --mostrar
"""
import argparse
import importlib
import os
import random
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
if AQUI not in sys.path:
    sys.path.insert(0, AQUI)

# ⛔ Escopo do repo: os quatorze SHORT. `*_lucas` nao existe para nos.
MOTORES = ["clean", "clean_short_v2", "escandalo", "troca", "organicwave",
           "ressurreicao", "flagrante", "pee", "vazamento", "necrose",
           "exterior", "colo", "receita", "botica",
           "dupla", "placa", "cha", "trio", "falta", "trio16", "dupla16", "falta16", "placa16", "troca16", "botica16", "colo16", "exterior16", "escandalo16", "ressurreicao16", "flagrante16", "good16",
           # + 2026-08-10: o BED 16, no commit em que nasce
           "bed16", "necrose16", "wife16"]

# ⭐⭐ O NUMERO QUE MANDA, e ele foi corrigido DUAS VEZES por render cortado.
#
#     32 -> cortou (BOTICA cena 1, 2026-08-04)
#     28 -> cortou (BOTICA cena 1, 2026-08-05)
#     25 -> e' o mais longo que o OPERADOR escreve a mao. Os exemplos dele
#           vivem entre 16 e 25 palavras, ou seja 2,0 a 3,1 palavras/s.
#
# ⛔ Eu cheguei aqui pelo caminho errado duas vezes: escolhi o numero pelo topo
# aritmetico da faixa (4,0 p/s) e esperei o render reprovar. A faixa 3,4-4,0 da
# §5 descreve o que a narracao PODE fazer no melhor caso, nao o que ela faz. O
# numero honesto e' o maior que ja' se viu falar inteiro — nao o maior que cabe
# na conta.
# ⚠️ Ordem do operador, 2026-08-05: *"sempre meca. Nao pode haver cortes de
# fala."* Este arquivo e' a resposta a primeira metade.
TETO_FISICO = 25
SEGUNDOS = 8.0


def carregar(nome):
    # ⚠️ o v2 do CLEAN quebra a convencao do nome de arquivo.
    return importlib.import_module(
        nome if nome.endswith("_v2") else "%s_short" % nome)


def medir(nome, n=600):
    """Devolve {cena: (estouros, maximo, exemplo_mais_longo)} e o teto declarado."""
    M = carregar(nome)
    pags = sorted(getattr(M, "ETNIA", {"joe": None}))
    est, mx, ex = {}, {}, {}
    for i in range(n):
        p = pags[i % len(pags)]
        # ⛔⛔ TRES ARGUMENTOS, SEMPRE. A versao anterior tentava
        # `sortear(p, rng, {}, {})` e caia para 3 no TypeError — e isso estava
        # ERRADO: o 4o posicional NAO e' `travas` em todo motor. No ESCANDALO e'
        # `degrau`, no RESSURREICAO e' `credibilidade`. Passar `{}` ali injetava
        # um degrau invalido e o motor gerava fala fora da escada, sem erro de
        # tipo — ou seja, o medidor media um motor em estado que o operador
        # nunca produz. Todos os eixos opcionais tem default, entao 3 basta.
        spec = M.sortear(p, random.Random(i), {})
        for c, fala in enumerate(spec["falas"], 1):
            q = M._palavras(fala)
            if q > mx.get(c, 0):
                mx[c], ex[c] = q, fala
            if q > TETO_FISICO:
                est[c] = est.get(c, 0) + 1
    return est, mx, ex, dict(getattr(M, "TETO_FALA", {})), n


def curva(alvos, n):
    """A distribuicao, e sobretudo o MINIMO que cada cena consegue gerar.

    ⭐⭐ O `min` e' o numero que decide a estrategia, e e' o que eu nunca tinha
    medido: se o minimo ja' esta' acima do teto fisico, BAIXAR O TETO NAO
    RESOLVE — o motor nao sabe falar mais curto, e o unico caminho e' encurtar
    a copy. Sem esta coluna a gente fica trocando teto e o render continua
    cortando.
    """
    print("%-16s %-4s %5s %5s %5s %5s   %s"
          % ("motor", "cena", "min", "p50", "p90", "max", "veredito"))
    print("-" * 86)
    ruins = 0
    for nome in alvos:
        try:
            M = carregar(nome)
        except Exception as e:                       # noqa: BLE001
            print("%-16s ERRO: %s" % (nome, str(e)[:40]))
            continue
        pags = sorted(getattr(M, "ETNIA", {"joe": None}))
        dist = {}
        for i in range(n):
            spec = M.sortear(pags[i % len(pags)], random.Random(i), {})
            for c, f in enumerate(spec["falas"], 1):
                dist.setdefault(c, []).append(M._palavras(f))
        for c in sorted(dist):
            v = sorted(dist[c])
            q = len(v)
            acima = 100.0 * sum(1 for x in v if x > TETO_FISICO) / q
            if v[0] > TETO_FISICO:
                ver = ("⛔ PISO %d > teto: BAIXAR O TETO NAO RESOLVE, "
                       "e' preciso encurtar copy" % v[0])
                ruins += 1
            elif acima > 0:
                ver = "⚠️ %.1f%% acima — cabe so' apertando o sorteio" % acima
                ruins += 1
            else:
                ver = "ok"
            print("%-16s %-4d %5d %5d %5d %5d   %s"
                  % (nome, c, v[0], v[q // 2], v[int(q * 0.9)], v[-1], ver))
    print("")
    print("cenas que ainda cortam fala: %d" % ruins)
    return 1 if ruins else 0


def main():
    ap = argparse.ArgumentParser(
        description="Gate do teto de fala: 8s comportam no maximo %d palavras"
                    % TETO_FISICO)
    ap.add_argument("--motor")
    ap.add_argument("--n", type=int, default=600)
    ap.add_argument("--mostrar", action="store_true",
                    help="imprime a fala mais longa de cada cena que estoura")
    ap.add_argument("--gate", action="store_true", help="exit 1 se algum estoura")
    ap.add_argument("--curva", action="store_true",
                    help="distribuicao por cena e o PISO do motor (o mais curto "
                         "que ele consegue gerar) — e' ele que diz se baixar o "
                         "teto resolve ou se e' preciso encurtar copy")
    a = ap.parse_args()

    alvos = [a.motor] if a.motor else MOTORES
    if a.curva:
        return curva(alvos, a.n)
    print("teto fisico: %d palavras em %.0fs (%.1f p/s)\n"
          % (TETO_FISICO, SEGUNDOS, TETO_FISICO / SEGUNDOS))
    print("%-16s %-12s %-14s %s"
          % ("motor", "TETO decl.", "max gerado", "estouro"))
    print("-" * 68)

    sujos = []
    for nome in alvos:
        try:
            est, mx, ex, decl, n = medir(nome, a.n)
        except Exception as e:                       # noqa: BLE001
            print("%-16s ERRO: %s" % (nome, str(e)[:44]))
            sujos.append(nome)
            continue
        s_decl = "/".join(str(decl.get(c, "?")) for c in sorted(decl))
        s_max = "/".join(str(mx.get(c, 0)) for c in sorted(mx))
        if est:
            partes = ["c%d %.1f%% (max %d = %.2f p/s)"
                      % (c, 100.0 * q / n, mx[c], mx[c] / SEGUNDOS)
                      for c, q in sorted(est.items())]
            print("%-16s %-12s %-14s %s"
                  % (nome, s_decl, s_max, "  ".join(partes)))
            sujos.append(nome)
            if a.mostrar:
                for c in sorted(est):
                    print("      cena %d (%d palavras): %s" % (c, mx[c], ex[c]))
        else:
            # ⚠️ teto declarado acima do fisico e' bomba armada: hoje nao
            # estoura por sorte do pool, e estoura no dia em que alguem
            # acrescentar uma entrada longa.
            altos = [c for c, v in decl.items() if v > TETO_FISICO]
            nota = ("teto declarado >%d nas cenas %s (nao atingido hoje)"
                    % (TETO_FISICO, altos)) if altos else "ok"
            print("%-16s %-12s %-14s %s" % (nome, s_decl, s_max, nota))

    if sujos:
        print("\nMOTORES QUE CORTAM FALA: %d de %d — %s"
              % (len(sujos), len(alvos), ", ".join(sujos)))
        return 1 if a.gate else 0
    print("\nNENHUM MOTOR ESTOURA o teto fisico.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
