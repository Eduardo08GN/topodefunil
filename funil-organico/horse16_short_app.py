#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE HORSE 16 — app desktop offline.

Ponto de entrada enxuto: a interface mora em ui_agente.py (compartilhada por
todos os agentes portados) e a doutrina em horse16_short.py.

    python funil-organico/horse16_short_app.py

⛔ Ledger PROPRIO: cada agente guarda a propria memoria de nao-repetir.
"""

import os
import sys

if getattr(sys, "frozen", False):          # rodando como .exe do PyInstaller
    sys.path.insert(0, sys._MEIPASS)
else:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ui_agente                     # noqa: E402
import horse16_short as motor        # noqa: E402

# o ledger acompanha o executavel, nao a pasta temporaria do PyInstaller
motor.LEDGER = os.path.join(ui_agente.base_dir(), ".horse-16-ledger.json")

if __name__ == "__main__":
    ui_agente.App(motor).mainloop()
