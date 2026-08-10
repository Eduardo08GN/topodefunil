# -*- coding: utf-8 -*-
"""medir_copy16.py — o CONTRATO DE COPY 16s, cobrado de fora, motor por motor.

⛔ POR QUE EXISTE, E POR QUE E' SEPARADO DO `lint` DE CADA MOTOR.

Em 2026-08-10 o operador mandou reformular a copy de sete agentes da familia
16s. A revisao adversarial que motivou a ordem (6 lentes independentes, 127
achados, 79 derrubados na refutacao) nao encontrou defeitos de ESTILO: encontrou
sete defeitos ESTRUTURAIS, cada um presente em quase todos os motores ao mesmo
tempo. Medido ANTES da reforma, 200 sorteios por motor:

    motor            p/CTA rotulo ingred erecao 2nomes
    troca16           100%    73%     0%     0%   100%
    ressurreicao16    100%   100%    62%    22%   100%
    exterior16        100%   100%     0%   100%   100%
    flagrante16       100%   100%     0%     0%   100%
    pee16              26%    60%     0%    54%    98%
    escandalo16       100%   100%    56%     0%   100%
    colo16            100%    64%     0%    12%   100%

Defeito que aparece em sete motores nao e' erro de quem escreveu o pool — e'
ausencia de contrato. O contrato mora em `short_comum.lint_copy16`; este arquivo
o cobra DE FORA, pelo sorteio real, para que:

  1. de' para medir um motor ANTES de ele ligar a lente (senao nao ha' "antes");
  2. o numero seja do VIDEO gerado, nao do pool lido — os sete defeitos acima
     vivem na COMBINACAO, e nenhum deles aparece relendo a lista de strings.

⚠️ A LISTA DE MOTORES E' MANTIDA A MAO. Motor 16s novo entra AQUI no mesmo
commit em que nasce, junto com as listas do `medir_teto_fala`, `medir_deiticos`,
`medir_contexto_copy`, `medir_abertura` e `medir_alcance`.

    python funil-organico/medir_copy16.py
    python funil-organico/medir_copy16.py --motor colo16 --exemplos 5
    python funil-organico/medir_copy16.py --gate
"""
import argparse
import collections
import importlib
import os
import random
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
if AQUI not in sys.path:
    sys.path.insert(0, AQUI)

import short_comum as sc                                        # noqa: E402

MOTORES = ["troca16", "ressurreicao16", "exterior16", "flagrante16",
           "pee16", "escandalo16", "colo16",
           # os demais 16s: entram na medicao desde ja', mesmo antes da
           # reforma — numero que ninguem olha e' numero que envelhece
           "trio16", "dupla16", "falta16", "placa16", "botica16", "good16",
           # + 2026-08-10: o BED 16 entra AQUI no commit em que nasce — ele
           # ja' nasce sob o contrato, e motor fora da lista nao e' medido.
           "bed16", "necrose16", "wife16",
           # + 2026-08-10: o FIGHT 16, no commit em que nasce
           "fight16"]

# ⛔ Angulos cuja cena 1 E' uma promessa falsa que o proprio video desmente.
# So' muda o CT7: la' o verbo de ereccao e' a isca, nao o claim.
ISCA_ABSURDA = {"troca16", "exterior16", "colo16"}

N = 200


def medir(nome, n=N, exemplos=0):
    M = importlib.import_module("%s_short" % nome)
    pags = sorted(getattr(M, "ETNIA", {"joe": None}))
    contas = collections.Counter()
    amostras = collections.defaultdict(list)
    apelidos = collections.Counter()
    for i in range(n):
        spec = M.sortear(pags[i % len(pags)], random.Random(i), {})
        corpo = " ".join(spec["falas"]).lower()
        for ap in sc.APELIDOS_16:
            if ap.lower() in corpo:
                apelidos[ap] += 1
        achados = []
        sc.lint_copy16(M, spec, achados,
                       isca_absurda=(nome in ISCA_ABSURDA))
        vistos = set()
        for nivel, msg in achados:
            ct = msg.split(":", 1)[0]
            if ct in vistos:
                continue
            vistos.add(ct)
            contas[ct] += 1
            if exemplos and len(amostras[ct]) < exemplos:
                amostras[ct].append((nivel, msg, spec["falas"]))
    return contas, amostras, apelidos


CTS = ["CT1", "CT2", "CT3", "CT4", "CT4b", "CT5", "CT6", "CT7", "CT8"]
ROTULO = {
    "CT1": "sentenca depois do CTA",
    "CT2": "take 1 sem falha enunciada",
    "CT3": "`gelatin trick` sem razao",
    "CT4": "apelido muda no corte",
    "CT5": "ingrediente na fala",
    "CT6": "CTA sem endereco de entrega",
    "CT7": "verbo de ereccao no take do CTA",
    "CT4b": "apelido fora de pecker/wiener/Johnson",
    "CT8": "pede follow na fala (a DM sai igual)",
}

# ⚠️ O CT4 sozinho garante UM apelido por video — e um apelido por video pode
# ser o MESMO apelido em todo o lote, que e' mode-collapse com cara de
# consistencia. Esta coluna mostra a reparticao real entre os tres.


def main():
    ap = argparse.ArgumentParser(
        description="cobra o CONTRATO DE COPY 16s pelo sorteio real")
    ap.add_argument("--motor", choices=MOTORES)
    ap.add_argument("--n", type=int, default=N)
    ap.add_argument("--exemplos", type=int, default=0)
    ap.add_argument("--gate", action="store_true",
                    help="sai 1 se qualquer motor violar qualquer CT")
    a = ap.parse_args()
    alvos = [a.motor] if a.motor else MOTORES

    print("\nCONTRATO DE COPY 16s — %d sorteios por motor, %% de videos que "
          "violam" % a.n)
    print("-" * 88)
    print("%-16s %s   %s" % ("motor", "  ".join("%-5s" % c for c in CTS),
                            "/".join(sc.APELIDOS_16)))
    print("-" * 88)
    sujos = []
    for nome in alvos:
        try:
            contas, amostras, apelidos = medir(nome, a.n, a.exemplos)
        except Exception as e:                              # noqa: BLE001
            print("%-16s ERRO: %s" % (nome, str(e)[:60]))
            sujos.append(nome)
            continue
        if any(contas[c] for c in CTS):
            sujos.append(nome)
        rep = "/".join("%d" % (100 * apelidos[x] // a.n)
                       for x in sc.APELIDOS_16)
        print("%-16s %s   %s"
              % (nome, "  ".join("%4d%%" % (100 * contas[c] // a.n)
                                 for c in CTS), rep))
        if a.exemplos:
            for c in CTS:
                for nivel, msg, falas in amostras.get(c, []):
                    print("    [%s] %s" % (nivel, msg[:120]))
                    for j, f in enumerate(falas, 1):
                        print("        %d| %s" % (j, f))
    print("-" * 88)
    for c in CTS:
        print("  %-4s %s" % (c, ROTULO[c]))
    print("\nmotores que violam o contrato: %d de %d — %s"
          % (len(sujos), len(alvos), ", ".join(sujos) or "nenhum"))
    return 1 if (a.gate and sujos) else 0


if __name__ == "__main__":
    sys.exit(main())
