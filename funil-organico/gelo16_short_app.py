#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE GELO 16 — app desktop offline.

Ponto de entrada enxuto: a interface mora em `ui_agente.py` e a doutrina
inteira em `gelo16_short.py`. Nenhuma regra de cena ou de copy passa aqui.

3 takes de 8s = 24 segundos, destino AdBatch **Vertical 3**, fala em ALEMAO.
No Veo Editor, selecionar `Idioma: Alemao` e `Precisao: small` no rodape.

    python funil-organico/gelo16_short_app.py
"""

import os
import sys

if getattr(sys, "frozen", False):
    BASE = os.path.dirname(sys.executable)
    sys.path.insert(0, sys._MEIPASS)
else:
    BASE = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, BASE)

import ui_agente                 # noqa: E402
import gelo16_short as motor     # noqa: E402

# o ledger acompanha o EXECUTAVEL, nao a pasta temporaria do PyInstaller
motor.LEDGER = os.path.join(BASE, ".gelo-16-ledger.json")

if __name__ == "__main__":
    ui_agente.App(motor).mainloop()
