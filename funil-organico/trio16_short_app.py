#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE TRIO 16 — app desktop offline.

Ponto de entrada enxuto: a interface mora em ui_agente.py (compartilhada por
todos os agentes portados) e a doutrina em trio16_short.py.

⭐ O QUE MUDA EM RELACAO AO PAINEL DO TRIO SHORT:

  · DUAS cenas de copy em vez de tres. A interface le' `len(CENAS_UI)` e desenha
    o que o motor declarar — nao ha' nada de 3 cravado nela.
  · O CORPO-PROVA (`homem`) volta ao painel. No TRIO ele e' um eixo VIVO que a
    lista escondia: o operador nao conseguia trocar o homem sem re-sortear o
    video inteiro.
  · A BANCADA continua com cadeado (seis conformacoes), mas quem chega ao quadro
    e' o campo `aparato16` — o aparato parado, sem o copo de destino, porque o
    copo esta' na mao dela.

⛔ Ledger PROPRIO (`.trio-16-ledger.json`), separado do TRIO SHORT por decisao
   do operador: sao lotes diferentes e cada um tem de varrer o repertorio
   inteiro sem gastar o frescor do outro.

    python funil-organico/trio16_short_app.py
"""

import os
import sys

if getattr(sys, "frozen", False):          # rodando como .exe do PyInstaller
    sys.path.insert(0, sys._MEIPASS)
else:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ui_agente                  # noqa: E402
import trio16_short as motor      # noqa: E402

# o ledger acompanha o executavel, nao a pasta temporaria do PyInstaller
motor.LEDGER = os.path.join(ui_agente.base_dir(), ".trio-16-ledger.json")

if __name__ == "__main__":
    ui_agente.App(motor).mainloop()
