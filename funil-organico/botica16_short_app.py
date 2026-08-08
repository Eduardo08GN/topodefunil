#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE BOTICA 16 — app desktop offline.

Ponto de entrada enxuto: a interface mora em ui_agente.py e a doutrina em
botica16_short.py.

⭐ O QUE MUDA EM RELACAO AO PAINEL DO BOTICA SHORT:

  · DUAS cenas de copy em vez de tres.
  · O METODO continua no painel e continua variando entre os DOZE — como
    OBJETO em quadro, nao como gesto. O utensilio em movimento morreu na
    fusao, por decisao do operador com as tres opcoes medidas.
  · O RARO continua falado, e com o APOSTO — ele ja' vivia na cena 1.

⛔ Ledger PROPRIO (`.botica-16-ledger.json`).

    python funil-organico/botica16_short_app.py
"""

import os
import sys

if getattr(sys, "frozen", False):          # rodando como .exe do PyInstaller
    sys.path.insert(0, sys._MEIPASS)
else:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ui_agente                  # noqa: E402
import botica16_short as motor    # noqa: E402

# o ledger acompanha o executavel, nao a pasta temporaria do PyInstaller
motor.LEDGER = os.path.join(ui_agente.base_dir(), ".botica-16-ledger.json")

if __name__ == "__main__":
    ui_agente.App(motor).mainloop()
