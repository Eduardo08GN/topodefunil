#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE NECROSE 16 — app desktop offline.

Ponto de entrada enxuto: a interface mora em ui_agente.py (compartilhada por
todos os agentes portados) e a doutrina em necrose16_short.py.

⭐ 2 takes de 8s = 16 segundos, destino AdBatch Vertical 2. Nao substitui o
`necrose_short_app.py`: sao formatos diferentes, ledger proprio cada um, e os
dois convivem.

⭐ As duas cenas: os DOIS MODELOS anatomicos no pedestal (o hook) e o GEODUCK
erguido contra o ceu (o payoff), com mecanismo + prova + CTA na fala.

⛔ Ledger PROPRIO (`.necrose-16-ledger.json`).

    python funil-organico/necrose16_short_app.py
"""

import os
import sys

if getattr(sys, "frozen", False):          # rodando como .exe do PyInstaller
    sys.path.insert(0, sys._MEIPASS)
else:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ui_agente                     # noqa: E402
import necrose16_short as motor      # noqa: E402

# o ledger acompanha o executavel, nao a pasta temporaria do PyInstaller
motor.LEDGER = os.path.join(ui_agente.base_dir(), ".necrose-16-ledger.json")

if __name__ == "__main__":
    ui_agente.App(motor).mainloop()
