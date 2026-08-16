#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE PAR 16 — app desktop offline.

Ponto de entrada enxuto: a interface mora em ui_agente.py e a doutrina em
par16_short.py.

⭐ O PAINEL:

  · DUAS cenas de copy (2 takes de 8s, AdBatch Vertical 2).
  · QUATRO eixos: O MUNDO (take 1, 8 entradas — 5 com o par efetivamente
    filmado em cima e 3 TRANSPOSTAS, marcadas no rotulo e no resumo), A COPY
    (4 familias, com hook e prova PAREADOS no mesmo item — trocar so' o hook
    e' o defeito medido do FIGHT 16, onde cada beat lido sozinho estava certo e
    o par estava errado em 5 de 6), O GESTO (take 2, 5 entradas) e AS MAOS (8).
    ⛔ Mas o AMBIENTE vem sempre do take 1. Se o gesto trouxesse a bancada dele
    junto, o segundo quadro mudaria de lugar no meio do video — o defeito que a
    ancora do IMAGE 02 existe para impedir. Sao 160 combinacoes de mundo x
    copy x gesto, e o `--autoteste` VARRE AS 160 uma a uma em vez de amostrar.
  · ⭐ Trocar a copy de UMA cena re-sorteia AS DUAS, de proposito: o hook e a
    prova sao um par so'.
  · ⭐ O CAMPO DA PALAVRA DO CTA nasce em `gelatin` — aqui sem conserto
    nenhum, porque a fonte ja' pede `gelatin` em 7 de 7.

⛔ O que este agente NAO tem, e nao e' esquecimento: animal vivo, chapeu,
geoduck e sifao. E' o que o separa do `necrose16` em cada linha de prompt, e a
lente `PR11` cobra isso no texto montado.

⛔ Ledger PROPRIO (`.par-16-ledger.json`).

    python funil-organico/par16_short_app.py
"""

import os
import sys

if getattr(sys, "frozen", False):          # rodando como .exe do PyInstaller
    sys.path.insert(0, sys._MEIPASS)
else:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ui_agente                   # noqa: E402
import par16_short as motor        # noqa: E402

# o ledger acompanha o executavel, nao a pasta temporaria do PyInstaller
motor.LEDGER = os.path.join(ui_agente.base_dir(), ".par-16-ledger.json")

if __name__ == "__main__":
    ui_agente.App(motor).mainloop()
