#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE PRATO 16 — app desktop offline.

Ponto de entrada enxuto: a interface mora em ui_agente.py e a doutrina em
prato16_short.py.

⭐ O PAINEL:

  · DUAS cenas de copy.
  · SEIS eixos: A REGIAO (15 cozinhas de fora dos EUA), QUEM FALA, A ESPOSA,
    A COR (da gelatina), O PRATO e A JARRA. ⛔ Eixo no painel que nao muda o
    video e' pior que eixo ausente — o operador troca, ve' que nada mudou e
    para de confiar no painel inteiro. Por isso os seis sao cobrados a cada
    sorteio pelo `lint_painel_honesto`.
  · Uma pre-selecao de REGIAO (`TRAVAS_UI`), que filtra o mundo sorteado.
  · ⭐⭐ DOIS TOGGLES, e o `ref forte` NASCE MARCADO (`MODOS_DEFAULT`).
    ⭐ E o FORTE deste motor chama `sc.ref_forte(..., maduros=True)`: o pool
    compartilhado e' 26-38 e este angulo e' de SENHOR. Ligar o toggle troca o
    CORPO dele, nunca o homem por um de trinta — foi exatamente esse defeito
    que o operador pegou no GOOD 16 em 2026-08-12.

⛔ Ledger PROPRIO (`.prato-16-ledger.json`).

    python funil-organico/prato16_short_app.py
"""

import os
import sys

if getattr(sys, "frozen", False):          # rodando como .exe do PyInstaller
    sys.path.insert(0, sys._MEIPASS)
else:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ui_agente                   # noqa: E402
import prato16_short as motor      # noqa: E402

# o ledger acompanha o executavel, nao a pasta temporaria do PyInstaller
motor.LEDGER = os.path.join(ui_agente.base_dir(), ".prato-16-ledger.json")

if __name__ == "__main__":
    ui_agente.App(motor).mainloop()
