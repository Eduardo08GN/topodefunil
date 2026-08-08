#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE DUPLA 16 — app desktop offline.

Ponto de entrada enxuto: a interface mora em ui_agente.py (compartilhada por
todos os agentes portados) e a doutrina em dupla16_short.py.

⭐ O QUE MUDA EM RELACAO AO PAINEL DO DUPLA SHORT:

  · DUAS cenas de copy em vez de tres. A interface le' `len(CENAS_UI)` e desenha
    o que o motor declarar — nao ha' nada de 3 cravado nela.
  · A BANCADA continua com cadeado (seis conformacoes), mas quem chega ao quadro
    e' o campo `aparato16` — o aparato parado, sem o copo de destino, porque o
    copo esta' na mao dela junto com o prop gigante.
  · O RARO continua no painel e continua VIVO: ele so' deixou de ser FALADO
    (nao cabe nas 25 palavras da cena 2 — medido), e segue no quadro, na
    bancada.

⛔ Ledger PROPRIO (`.dupla-16-ledger.json`), separado do DUPLA SHORT: sao lotes
   diferentes e cada um tem de varrer o repertorio inteiro sem gastar o frescor
   do outro.

    python funil-organico/dupla16_short_app.py
"""

import os
import sys

if getattr(sys, "frozen", False):          # rodando como .exe do PyInstaller
    sys.path.insert(0, sys._MEIPASS)
else:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ui_agente                  # noqa: E402
import dupla16_short as motor     # noqa: E402

# o ledger acompanha o executavel, nao a pasta temporaria do PyInstaller
motor.LEDGER = os.path.join(ui_agente.base_dir(), ".dupla-16-ledger.json")

if __name__ == "__main__":
    ui_agente.App(motor).mainloop()
