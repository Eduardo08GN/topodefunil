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
           "exterior", "colo", "receita", "botica"]

# ⭐ O numero que manda. 8s x 4,0 palavras/s, o topo da faixa medida.
TETO_FISICO = 32
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
        # ⚠️ duas assinaturas convivem no repo.
        try:
            spec = M.sortear(p, random.Random(i), {}, {})
        except TypeError:
            spec = M.sortear(p, random.Random(i), {})
        for c, fala in enumerate(spec["falas"], 1):
            q = M._palavras(fala)
            if q > mx.get(c, 0):
                mx[c], ex[c] = q, fala
            if q > TETO_FISICO:
                est[c] = est.get(c, 0) + 1
    return est, mx, ex, dict(getattr(M, "TETO_FALA", {})), n


def main():
    ap = argparse.ArgumentParser(
        description="Gate do teto de fala: 8s comportam no maximo %d palavras"
                    % TETO_FISICO)
    ap.add_argument("--motor")
    ap.add_argument("--n", type=int, default=600)
    ap.add_argument("--mostrar", action="store_true",
                    help="imprime a fala mais longa de cada cena que estoura")
    ap.add_argument("--gate", action="store_true", help="exit 1 se algum estoura")
    a = ap.parse_args()

    alvos = [a.motor] if a.motor else MOTORES
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
