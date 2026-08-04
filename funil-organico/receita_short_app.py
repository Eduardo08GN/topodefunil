#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE RECEITA SHORT — app desktop offline.

Ponto de entrada enxuto: a interface mora em ui_agente.py (compartilhada por
todos os agentes portados) e a doutrina em receita_short.py.

⭐ O que este painel tem de proprio:

  · ⭐⭐ CENA 1 na pre-selecao (TRAVAS_UI) — o TOGGLE que o operador pediu:
    `corte de maos` (macro de cima, so' as maos e a tigela, como a fonte) ou
    `terceira pessoa` (plano medio, ele em quadro preparando a receita). O
    default e' `livre`, que sorteia entre os dois.
  · NICHO na pre-selecao — as 9 familias de cozinha. Escolhido o nicho, o
    sorteio fica dentro dele, e a ETNIA sai de DENTRO do mundo (nunca solta).
  · O LUGAR da cena 3 com cadeado, e o pool dele e' filtrado pelo mundo em cena
    (`lugares_do_mundo`): cozinha de cabana apalache nao paga doca de marina.

⛔ Ledger PROPRIO (`.receita-short-ledger.json`), como todo agente.

    python funil-organico/receita_short_app.py
"""

import os
import sys

if getattr(sys, "frozen", False):          # rodando como .exe do PyInstaller
    sys.path.insert(0, sys._MEIPASS)
else:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ui_agente                   # noqa: E402
import receita_short as motor      # noqa: E402

# o ledger acompanha o executavel, nao a pasta temporaria do PyInstaller
motor.LEDGER = os.path.join(ui_agente.base_dir(), ".receita-short-ledger.json")

if __name__ == "__main__":
    ui_agente.App(motor).mainloop()
