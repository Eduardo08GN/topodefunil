#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
FLAGRANTE LUCAS — app desktop offline do agente FLAGRANTE.

Ponto de entrada enxuto: a interface mora em ui_agente.py (compartilhada por
todos os agentes portados) e a doutrina em flagrante_lucas.py.

    python funil-organico/flagrante_lucas_app.py
"""

import os
import sys

if getattr(sys, "frozen", False):          # rodando como .exe do PyInstaller
    sys.path.insert(0, sys._MEIPASS)
else:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ui_agente                     # noqa: E402
import flagrante_lucas as motor      # noqa: E402

# o ledger acompanha o executavel, nao a pasta temporaria do PyInstaller
motor.LEDGER = os.path.join(ui_agente.base_dir(), ".flagrante-ledger.json")

if __name__ == "__main__":
    ui_agente.App(motor).mainloop()
