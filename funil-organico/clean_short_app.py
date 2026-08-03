#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE CLEAN — app desktop offline.

Ponto de entrada enxuto: a interface mora em ui_agente.py (compartilhada por
todos os agentes portados) e a doutrina em clean_short.py.

⭐ Este agente declara TRAVAS_UI: o painel desenha botoes de `quem fala`
(homem/mulher) e `cena` (fileira/preparo) logo abaixo dos de pele, e o que
estiver selecionado NAO e' re-sorteado.

    python funil-organico/clean_short_app.py
"""

import os
import sys

if getattr(sys, "frozen", False):          # rodando como .exe do PyInstaller
    sys.path.insert(0, sys._MEIPASS)
else:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ui_agente                    # noqa: E402
import clean_short as motor         # noqa: E402

# o ledger acompanha o executavel, nao a pasta temporaria do PyInstaller
motor.LEDGER = os.path.join(ui_agente.base_dir(), ".clean-short-ledger.json")

if __name__ == "__main__":
    ui_agente.App(motor).mainloop()
