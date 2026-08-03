#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE COLO SHORT — app desktop offline.

Ponto de entrada enxuto: a interface mora em ui_agente.py (compartilhada por
todos os agentes portados) e a doutrina em colo_short.py.

⭐ O que este painel tem de proprio:

  · NICHO na pre-selecao (TRAVAS_UI) — as 9 familias de mundo (americana,
    apalache, sulista, mexicana, caribenha, asiatica, sul_asiatica, africana,
    mediterranea) com `livre` de default. Escolhido o nicho, o sorteio fica
    dentro dele.
  · MUNDO com cadeado — e a ETNIA sai de DENTRO do mundo, nunca solta: o pool
    do botao `trocar` da etnia e' o do mundo em cena (`etnias_do_mundo`).
  · O PROP e A ISCA no painel, porque a copy da cena 1 os NOMEIA com todas as
    letras — trocar um deles remonta a fala (EIXOS_QUE_MEXEM_NA_COPY).

⛔ Ledger PROPRIO (`.colo-short-ledger.json`), como todo agente.

    python funil-organico/colo_short_app.py
"""

import os
import sys

if getattr(sys, "frozen", False):          # rodando como .exe do PyInstaller
    sys.path.insert(0, sys._MEIPASS)
else:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ui_agente                # noqa: E402
import colo_short as motor      # noqa: E402

# o ledger acompanha o executavel, nao a pasta temporaria do PyInstaller
motor.LEDGER = os.path.join(ui_agente.base_dir(), ".colo-short-ledger.json")

if __name__ == "__main__":
    ui_agente.App(motor).mainloop()
