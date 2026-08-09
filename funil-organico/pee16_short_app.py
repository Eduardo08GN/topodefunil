#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE PEE 16 — app desktop offline.

Ponto de entrada enxuto: a interface mora em ui_agente.py (compartilhada por
todos os agentes portados) e a doutrina em pee16_short.py.

⭐ 2 takes de 8s = 16 segundos, destino AdBatch Vertical 2. Nao substitui o
`pee_short_app.py`: sao formatos diferentes, ledger proprio cada um.

⛔⛔ ESTE ARQUIVO FALTAVA (2026-08-09). O `pee16_short.py` estava no repo desde
o commit do PEE 16, mas sem o `_app.py` ele nao podia virar `.exe` — o build
morria com *"Script file does not exist"*. Foi o unico dos 14 motores de 16s
sem ponto de entrada, e so' apareceu ao levantar quais angulos ja' tem versao
de 16 segundos. ⚠️ E' copia literal da forma dos outros treze; nenhuma regra
de cena ou copy passa por aqui.

    python funil-organico/pee16_short_app.py
"""

import os
import sys

if getattr(sys, "frozen", False):          # rodando como .exe do PyInstaller
    BASE = os.path.dirname(sys.executable)
    sys.path.insert(0, sys._MEIPASS)
else:
    BASE = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, BASE)

import ui_agente                # noqa: E402
import pee16_short as motor     # noqa: E402

# o ledger acompanha o executavel, nao a pasta temporaria do PyInstaller
motor.LEDGER = os.path.join(BASE, ".pee-16-ledger.json")

if __name__ == "__main__":
    ui_agente.App(motor).mainloop()
