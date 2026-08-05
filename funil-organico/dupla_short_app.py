#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE DUPLA SHORT — app desktop offline.

Ponto de entrada enxuto: a interface mora em ui_agente.py (compartilhada por
todos os agentes portados) e a doutrina em dupla_short.py.

⭐ O que este painel tem de proprio:

  · NICHO na pre-selecao (TRAVAS_UI) — as 11 familias de botica (amish,
    americana, apalache, sulista, mexicana, caribenha, asiatica, sul_asiatica,
    africana, mediterranea, andina). A ETNIA sai de DENTRO do mundo, nunca
    solta.
  · O PREPARO com cadeado — doze utensilios, e o operador mandou que ele NAO
    fosse fixo: liquidificador travado engessava o repertorio visual do take.
  · O RARO no painel: um ingrediente pouco conhecido por video, e a fala o traz
    sempre com o APOSTO colado (`maca root, that Andean root from Peru`).
  · O COMUM e a ISCA tambem, porque a copy os NOMEIA — trocar um deles remonta
    a fala (EIXOS_QUE_MEXEM_NA_COPY).

⛔ Ledger PROPRIO (`.dupla-short-ledger.json`), como todo agente.

    python funil-organico/dupla_short_app.py
"""

import os
import sys

if getattr(sys, "frozen", False):          # rodando como .exe do PyInstaller
    sys.path.insert(0, sys._MEIPASS)
else:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ui_agente                  # noqa: E402
import dupla_short as motor      # noqa: E402

# o ledger acompanha o executavel, nao a pasta temporaria do PyInstaller
motor.LEDGER = os.path.join(ui_agente.base_dir(), ".dupla-short-ledger.json")

if __name__ == "__main__":
    ui_agente.App(motor).mainloop()
