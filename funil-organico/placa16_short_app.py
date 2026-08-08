#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE PLACA 16 — app desktop offline.

Ponto de entrada enxuto: a interface mora em ui_agente.py e a doutrina em
placa16_short.py.

⭐ O QUE MUDA EM RELACAO AO PAINEL DO PLACA SHORT:

  · DUAS cenas de copy em vez de tres.
  · A PLACA continua com cadeado — e' o eixo que da' nome ao agente e o unico
    do repertorio que poe TEXTO em cena de proposito.
  · O CORPO-PROVA passa a estar na cena 2, que agora e' o payoff.

⛔ Ledger PROPRIO (`.placa-16-ledger.json`).

    python funil-organico/placa16_short_app.py
"""

import os
import sys

if getattr(sys, "frozen", False):          # rodando como .exe do PyInstaller
    sys.path.insert(0, sys._MEIPASS)
else:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ui_agente                  # noqa: E402
import placa16_short as motor     # noqa: E402

# o ledger acompanha o executavel, nao a pasta temporaria do PyInstaller
motor.LEDGER = os.path.join(ui_agente.base_dir(), ".placa-16-ledger.json")

if __name__ == "__main__":
    ui_agente.App(motor).mainloop()
