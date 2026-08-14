#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE ORGANIC WAVE 16 — app desktop offline.

Ponto de entrada enxuto: a interface mora em ui_agente.py (compartilhada por
todos os agentes portados) e a doutrina em organicwave16_short.py.

    python funil-organico/organicwave16_short_app.py

⛔ Ledger PROPRIO, separado do `organicwave_short`: 16s e 24s nao gastam o
historico um do outro.
"""

import os
import sys

if getattr(sys, "frozen", False):          # rodando como .exe do PyInstaller
    sys.path.insert(0, sys._MEIPASS)
else:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ui_agente                           # noqa: E402
import organicwave16_short as motor        # noqa: E402

# o ledger acompanha o executavel, nao a pasta temporaria do PyInstaller
motor.LEDGER = os.path.join(ui_agente.base_dir(), ".organicwave-16-ledger.json")

if __name__ == "__main__":
    ui_agente.App(motor).mainloop()
