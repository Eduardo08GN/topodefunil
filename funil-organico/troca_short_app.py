#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE TROCA SHORT — app desktop offline.

Ponto de entrada enxuto: a interface mora em ui_agente.py (compartilhada por
todos os agentes portados) e a doutrina em troca_short.py.

⚠️ Ao contrario dos outros SHORT, este nao colapsa um motor longo: nao existe
`troca_lucas.py`. O `troca_short.py` e' motor completo (pools proprios) e so'
toma emprestada a maquinaria compartilhada do `short_comum.py`.

    python funil-organico/troca_short_app.py
"""

import os
import sys

if getattr(sys, "frozen", False):          # rodando como .exe do PyInstaller
    BASE = os.path.dirname(sys.executable)
    sys.path.insert(0, sys._MEIPASS)
else:
    BASE = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, BASE)

import ui_agente                    # noqa: E402
import troca_short as motor         # noqa: E402

# o ledger acompanha o executavel, nao a pasta temporaria do PyInstaller
motor.LEDGER = os.path.join(BASE, ".troca-short-ledger.json")

if __name__ == "__main__":
    ui_agente.App(motor).mainloop()
