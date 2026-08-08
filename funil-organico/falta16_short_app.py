#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE FALTA 16 — app desktop offline.

Ponto de entrada enxuto: a interface mora em ui_agente.py e a doutrina em
falta16_short.py.

⭐ O QUE MUDA EM RELACAO AO PAINEL DO FALTA SHORT:

  · DUAS cenas de copy em vez de tres.
  · O botao `trocar` da copy FUNCIONA. No motor de 24s ele levantava
    `KeyError: 'substancia'` — a `nova_fala` passava cinco argumentos para uma
    funcao de tres e lia um campo que nao existe mais desde a reformulacao de
    2026-08-07. Ninguem viu porque aquele motor nao tem autoteste nem CLI.
  · O RARO continua no painel e continua FALADO — na cena 1, onde os 20
    DESMENTIDOS ja' o nomeavam. Na cena 2 ele fica no quadro, na bancada.

⛔ Ledger PROPRIO (`.falta-16-ledger.json`).

    python funil-organico/falta16_short_app.py
"""

import os
import sys

if getattr(sys, "frozen", False):          # rodando como .exe do PyInstaller
    sys.path.insert(0, sys._MEIPASS)
else:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ui_agente                  # noqa: E402
import falta16_short as motor     # noqa: E402

# o ledger acompanha o executavel, nao a pasta temporaria do PyInstaller
motor.LEDGER = os.path.join(ui_agente.base_dir(), ".falta-16-ledger.json")

if __name__ == "__main__":
    ui_agente.App(motor).mainloop()
