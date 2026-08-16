#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE gelaHORSE 16 — app desktop offline.

Ponto de entrada enxuto: a interface mora em ui_agente.py e a doutrina em
gelahorse16_short.py.

⭐ O PAINEL:

  · DUAS cenas de copy (2 takes de 8s, AdBatch Vertical 2).
  · DOIS eixos SORTEADOS SEPARADOS, que e' a arquitetura pedida pelo
    operador: A CENA (take 1), com 6 entradas — uma por reel lido quadro a
    quadro — e O GESTO (take 2), com 4, em pool propria.
    ⛔ Mas o AMBIENTE vem sempre do take 1. Se o gesto trouxesse a cozinha
    dele junto, o segundo quadro mudaria de lugar no meio do video, que e' o
    defeito que a ancora do IMAGE 02 existe para impedir. Sao 24 combinacoes
    com a continuidade preservada, e o autoteste mede as 24.
  · ⭐ O CAMPO DA PALAVRA DO CTA nasce em `gelatin`, e isso e' CONSERTO e
    nao copia: dos 13 CTAs da fonte, SETE pedem `yes` e TRES pedem `horse` —
    as duas banidas na automacao de DM. Publicar verbatim faria o comentario
    entrar e a mensagem nao sair.

⛔ Ledger PROPRIO (`.gelahorse-16-ledger.json`).

    python funil-organico/gelahorse16_short_app.py
"""

import os
import sys

if getattr(sys, "frozen", False):          # rodando como .exe do PyInstaller
    sys.path.insert(0, sys._MEIPASS)
else:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ui_agente                   # noqa: E402
import gelahorse16_short as motor     # noqa: E402

# o ledger acompanha o executavel, nao a pasta temporaria do PyInstaller
motor.LEDGER = os.path.join(ui_agente.base_dir(), ".gelahorse-16-ledger.json")

if __name__ == "__main__":
    ui_agente.App(motor).mainloop()
