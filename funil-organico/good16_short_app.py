#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE GOOD 16 — app desktop offline.

Ponto de entrada enxuto: a interface mora em ui_agente.py e a doutrina em
good16_short.py.

⭐ O PAINEL, como ele esta' depois da passada de 2026-08-10:

  · DUAS cenas de copy em vez de tres.
  · QUATRO eixos: A REGIAO (15 arquetipos dos EUA), QUEM FALA, A MULHER e A
    TIGELA. ⛔ Eixo no painel que nao muda o video e' pior que eixo ausente —
    o operador troca, ve' que nada mudou e para de confiar no painel inteiro.
    Por isso os quatro sao cobrados a cada sorteio pelo `lint_painel_honesto`.
  · Uma pre-selecao de REGIAO (`TRAVAS_UI`), que filtra o mundo sorteado.
  · ⭐⭐ DOIS TOGGLES DE MODO, e o `ref forte` NASCE MARCADO — o motor declara
    `MODOS_DEFAULT = ("forte",)` e a `ui_agente` le' isso com `getattr`. Ordem
    do operador, 2026-08-10.
  · ⛔ SAIU O TOGGLE DE ENQUADRAMENTO (`casal na agua` / `so as maos`): o macro
    sem rosto foi aposentado por ordem do operador, e com um enquadramento so'
    o eixo deixou de existir. Ver o tumulo no cabecalho do `good16_short.py`.

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
