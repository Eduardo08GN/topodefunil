#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""App offline do RARO 16 — so' o preparo na mesa, sem ninguem em quadro.

⛔ Este agente NAO usa gelatina e fecha em `recipe`, por ordem do operador
(2026-08-20). E' uma ROTA PROPRIA: os outros 31 motores fecham em `gelatin`
porque a VSL vende gelatina. Quem publicar isto apontando para aquela VSL
quebra a congruencia de proposito.

⭐ O que este painel deixa travar: o RARO, o METODO de preparo, o AMBIENTE, o
ANGULO, a MANIPULACAO e as MAOS.
⚠️ O metodo nao cruza livre com o raro: o campo `certo` de cada um sai da
tabela de quimica de extracao do operador — hidrossoluvel pede decoccao,
lipossoluvel pede leite, mucilagem pede molho frio. Travar um metodo que nao
extrai aquele raro faz o RARO ceder, nunca o metodo.
"""

import os
import sys

if getattr(sys, "frozen", False):          # rodando como .exe do PyInstaller
    sys.path.insert(0, sys._MEIPASS)
else:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ui_agente                   # noqa: E402
import raro16_short as motor     # noqa: E402

# o ledger acompanha o executavel, nao a pasta temporaria do PyInstaller
motor.LEDGER = os.path.join(ui_agente.base_dir(), ".gelahorse-16-ledger.json")

if __name__ == "__main__":
    ui_agente.App(motor).mainloop()
