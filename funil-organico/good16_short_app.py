#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE GOOD 16 — app desktop offline.

Ponto de entrada enxuto: a interface mora em ui_agente.py e a doutrina em
good16_short.py.

⭐ O QUE MUDA EM RELACAO AO PAINEL DO COLO SHORT:

  · DUAS cenas de copy em vez de tres.
  · ⛔ O eixo A RECEITA SAIU DO PAINEL. Ele vivia SO' na fala da cena 2, que no
    16 virou prova + CTA + gate, e o layout da bancada e' string fixa — a
    receita nao chega a quadro nenhum. Eixo no painel que nao muda o video e'
    pior que eixo ausente: o operador troca, ve' que nada mudou e para de
    confiar no painel inteiro.
  · O resto dos eixos continua: mundo, etnia, ref, homem, prop, substancia.

⛔ Ledger PROPRIO (`.good-16-ledger.json`).

    python funil-organico/good16_short_app.py
"""

import os
import sys

if getattr(sys, "frozen", False):          # rodando como .exe do PyInstaller
    sys.path.insert(0, sys._MEIPASS)
else:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ui_agente                  # noqa: E402
import good16_short as motor      # noqa: E402

# o ledger acompanha o executavel, nao a pasta temporaria do PyInstaller
motor.LEDGER = os.path.join(ui_agente.base_dir(), ".good-16-ledger.json")

if __name__ == "__main__":
    ui_agente.App(motor).mainloop()
