#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE NECROSE SHORT — app desktop offline.

Ponto de entrada enxuto: a interface mora em ui_agente.py (compartilhada por
todos os agentes portados), e a doutrina inteira do NECROSE — strings travadas,
pools e o colapso para 3 cenas — em necrose_short.py.

    python funil-organico/necrose_short_app.py
"""

import os
import sys

if getattr(sys, "frozen", False):          # rodando como .exe do PyInstaller
    sys.path.insert(0, sys._MEIPASS)
else:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ui_agente                    # noqa: E402
import necrose_short as motor       # noqa: E402

# o ledger acompanha o executavel, nao a pasta temporaria do PyInstaller
motor.LEDGER = os.path.join(ui_agente.base_dir(), ".necrose-short-ledger.json")

if __name__ == "__main__":
    ui_agente.App(motor).mainloop()
