#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE DESCARTE 16 — app desktop offline.

Ponto de entrada enxuto: a interface mora em ui_agente.py e a doutrina em
descarte16_short.py.

⭐ O PAINEL:

  · DUAS cenas de copy (2 takes de 8s, AdBatch Vertical 2).
  · TRES eixos travaveis: A SUPERFICIE DO DESCARTE (6 entradas — 1 lida no v07
    e 5 transpostas, marcadas), O GESTO do take 2 (4 entradas) e AS MAOS (6
    entradas de arquitetura de mao).
    ⛔ O AMBIENTE vem SEMPRE do take 1. Se o gesto arrastasse a bancada dele
    junto, o segundo quadro mudaria de lugar no meio do video — o defeito que a
    ancora do IMAGE 02 existe para impedir. Sao 24 combinacoes com a
    continuidade preservada, e o autoteste mede as 24.
  · ⭐ O CAMPO DA PALAVRA DO CTA nasce em `gelatin`. `book` e `yes` estao
    banidos: quebram a automacao de DM.

⛔ SEM PECA ANATOMICA E SEM PROP FALICO em quadro nenhum — e' propriedade do
angulo, e e' o que zera o custo de moderacao deste motor.

⛔ Ledger PROPRIO (`.descarte-16-ledger.json`).

    python funil-organico/descarte16_short_app.py
"""

import os
import sys

if getattr(sys, "frozen", False):          # rodando como .exe do PyInstaller
    sys.path.insert(0, sys._MEIPASS)
else:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ui_agente                     # noqa: E402
import descarte16_short as motor     # noqa: E402

# o ledger acompanha o executavel, nao a pasta temporaria do PyInstaller
motor.LEDGER = os.path.join(ui_agente.base_dir(), ".descarte-16-ledger.json")

if __name__ == "__main__":
    ui_agente.App(motor).mainloop()
