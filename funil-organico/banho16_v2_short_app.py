#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE BANHO 16 V2 — app desktop offline.

Ponto de entrada enxuto: a interface mora em ui_agente.py e a doutrina em
banho16_v2_short.py.

⭐ O PAINEL:

  · DUAS cenas de copy.
  · CINCO eixos: O BANHEIRO, A SUPERFICIE, A MEDIDA, O ROTULO e A RECEITA.
    ⛔ Eixo no painel que nao muda o video e' pior que eixo ausente — o
    operador troca, ve' que nada mudou e para de confiar no painel inteiro.
  · Uma pre-selecao de CENARIO (`box` / `banheira` / `pia`), que filtra o
    banheiro sorteado.
  · ⭐⭐ UM TOGGLE, `MODO PESSOA`, e ele NASCE DESLIGADO. Ordem do operador:
    *"no sorteio gerar somente sem pessoas no quadro, pois foi o padrao que
    mais se repetiu e deu certo na pagina"* — 1 video em 7 da fonte tem gente.
    Ligado, o take 1 ganha um homem de costas no espelho passando o creme na
    propria nuca, como no unico reel da fonte que tem alguem em quadro.

⛔ Ledger PROPRIO (`.banho-16-v2-ledger.json`).

    python funil-organico/banho16_v2_short_app.py
"""

import os
import sys

if getattr(sys, "frozen", False):          # rodando como .exe do PyInstaller
    sys.path.insert(0, sys._MEIPASS)
else:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ui_agente                   # noqa: E402
import banho16_v2_short as motor      # noqa: E402

# o ledger acompanha o executavel, nao a pasta temporaria do PyInstaller
motor.LEDGER = os.path.join(ui_agente.base_dir(), ".banho-16-v2-ledger.json")

if __name__ == "__main__":
    ui_agente.App(motor).mainloop()
