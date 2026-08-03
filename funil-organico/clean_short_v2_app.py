#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE CLEAN V2 — app desktop offline.

Ponto de entrada enxuto: a interface mora em ui_agente.py (compartilhada por
todos os agentes portados) e a doutrina em clean_short_v2.py.

⭐ O que este app tem e o do v1 nao tem:

  · PRE-SELECAO (TRAVAS_UI) — `quem fala` e `cena` no topo, com `livre` de
    default; o que for escolhido nao e' re-sorteado.
  · CADEADO POR EIXO (EIXOS_TRAVAVEIS) — um botao `trava` ao lado de cada
    `trocar`. Fechado, aquele eixo volta identico no proximo SORTEAR VÍDEO.
    E' a trava da RECEITA: `ITEM A`, `ITEM B` e `TRUQUE` estao no painel.
  · ETNIA no painel — e ela e' LIVRE neste v2 (a congruencia com a etnia do
    avatar da pagina foi suspensa por ordem do operador, 2026-08-03).

⛔ Ledger PROPRIO (`.clean-short-v2-ledger.json`): o v1 continua com o dele, e
os dois nao se misturam.

    python funil-organico/clean_short_v2_app.py
"""

import os
import sys

if getattr(sys, "frozen", False):          # rodando como .exe do PyInstaller
    sys.path.insert(0, sys._MEIPASS)
else:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ui_agente                    # noqa: E402
import clean_short_v2 as motor      # noqa: E402

# o ledger acompanha o executavel, nao a pasta temporaria do PyInstaller
motor.LEDGER = os.path.join(ui_agente.base_dir(), ".clean-short-v2-ledger.json")

if __name__ == "__main__":
    ui_agente.App(motor).mainloop()
