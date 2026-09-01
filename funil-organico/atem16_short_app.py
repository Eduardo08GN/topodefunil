#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE ATEM 16 — app desktop offline.

Ponto de entrada enxuto: a interface mora em `ui_agente.py` (compartilhada por
todos os agentes portados) e a doutrina inteira em `atem16_short.py`. Nenhuma
regra de cena ou de copy passa por este arquivo.

⭐ 3 takes de 8s = 24 segundos, destino AdBatch **Vertical 3**, lingua da fala
**ALEMA**. Na hora de montar o lote no Veo Editor, selecionar `Idioma: Alemao`
no rodape — a legenda queimada nasce do Whisper rodando sobre o audio, e com o
idioma errado ela sai transcrita como se fosse ingles.

    python funil-organico/atem16_short_app.py
"""

import os
import sys

if getattr(sys, "frozen", False):          # rodando como .exe do PyInstaller
    BASE = os.path.dirname(sys.executable)
    sys.path.insert(0, sys._MEIPASS)
else:
    BASE = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, BASE)

import ui_agente                 # noqa: E402
import atem16_short as motor     # noqa: E402

# ⚠️ O ledger acompanha o EXECUTAVEL, nao a pasta temporaria do PyInstaller —
# sem esta linha o historico anti-repeticao morre a cada fechamento do app e o
# operador recebe o mesmo sorteio no lote seguinte.
motor.LEDGER = os.path.join(BASE, ".atem-16-ledger.json")

if __name__ == "__main__":
    ui_agente.App(motor).mainloop()
