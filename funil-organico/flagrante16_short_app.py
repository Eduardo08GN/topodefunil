#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE FLAGRANTE SHORT — app desktop offline.

Ponto de entrada enxuto: a interface mora em ui_agente.py (compartilhada por
todos os agentes portados) e TODA a doutrina — pools, strings travadas, tabelas
de token banido e o colapso para 3 cenas — mora em flagrante16_short.py.

⭐ 2026-08-03: ate' hoje esta linha mandava o leitor procurar a doutrina em
flagrante_lucas.py. Nao ha' mais nada la': o motor virou autossuficiente e os
`*_lucas` sao de terceiro, fora do repo de trabalho. Ponteiro corrigido para
nao sobreviver a saida do arquivo.

    python funil-organico/flagrante16_short_app.py
"""

import os
import sys

if getattr(sys, "frozen", False):          # rodando como .exe do PyInstaller
    sys.path.insert(0, sys._MEIPASS)
else:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ui_agente                    # noqa: E402
import flagrante16_short as motor       # noqa: E402

# o ledger acompanha o executavel, nao a pasta temporaria do PyInstaller
motor.LEDGER = os.path.join(ui_agente.base_dir(), ".flagrante-short-ledger.json")

if __name__ == "__main__":
    ui_agente.App(motor).mainloop()
