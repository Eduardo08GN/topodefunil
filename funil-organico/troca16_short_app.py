#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE TROCA 16 — app desktop offline.

Ponto de entrada enxuto: a interface mora em ui_agente.py e a doutrina em
troca16_short.py.

⭐ O QUE MUDA EM RELACAO AO PAINEL DO TROCA SHORT:

  · DUAS cenas de copy em vez de tres.
  · ⛔ Este e' o UNICO dos cinco portes em que as cenas 2 e 3 NAO FUNDIRAM. O
    operador escolheu preservar o CORPO-PROVA, e a troca desceu da tela para a
    fala (pool `TROCAS16`). O eixo `bancada` continua no painel porque a
    bancada-recibo vive na cena 1.

⛔ Ledger PROPRIO (`.troca-16-ledger.json`).

    python funil-organico/troca16_short_app.py
"""

import os
import sys

if getattr(sys, "frozen", False):          # rodando como .exe do PyInstaller
    sys.path.insert(0, sys._MEIPASS)
else:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ui_agente                  # noqa: E402
import troca16_short as motor     # noqa: E402

# o ledger acompanha o executavel, nao a pasta temporaria do PyInstaller
motor.LEDGER = os.path.join(ui_agente.base_dir(), ".troca-16-ledger.json")

if __name__ == "__main__":
    ui_agente.App(motor).mainloop()
