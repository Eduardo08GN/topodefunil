#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE CLEAN V2 16SEG — app desktop offline.

Ponto de entrada enxuto: a interface mora em ui_agente.py (compartilhada por
todos os agentes portados) e a doutrina em clean_v2_16s_short.py.

⭐ E' o CLEAN V2 em DOIS TAKES de 8s (16 segundos), destino AdBatch Vertical 2.
Nao substitui o `clean_short_v2_app.py`: sao formatos diferentes e os dois
coexistem, cada um com o seu ledger.

⭐ Traz o painel inteiro do V2 — nada foi tirado ao encurtar o video:

  · PRE-SELECAO (TRAVAS_UI) — `quem fala` e `cena` no topo, com `livre` de
    default; o que for escolhido nao e' re-sorteado.
  · CADEADO POR EIXO (EIXOS_TRAVAVEIS) — um botao `trava` ao lado de cada
    `trocar`. Fechado, aquele eixo volta identico no proximo SORTEAR VÍDEO.
    E' a trava da RECEITA: `ITEM A`, `ITEM B` e `TRUQUE` estao no painel.
  · ETNIA no painel — e ela e' LIVRE neste V2 (a congruencia com a etnia do
    avatar da pagina foi suspensa por ordem do operador, 2026-08-03).
  · MUNDO — os 20 mundos e as 10 familias, com a trava de pele soberana.

⛔ Ledger PROPRIO (`.clean-v2-16s-ledger.json`): o V2 de 3 cenas continua com o
dele, o V1 16seg com o dele, e os tres nao se misturam.

    python funil-organico/clean_v2_16s_short_app.py
"""

import os
import sys

if getattr(sys, "frozen", False):          # rodando como .exe do PyInstaller
    sys.path.insert(0, sys._MEIPASS)
else:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ui_agente                     # noqa: E402
import clean_v2_16s_short as motor   # noqa: E402

# o ledger acompanha o executavel, nao a pasta temporaria do PyInstaller
motor.LEDGER = os.path.join(ui_agente.base_dir(), ".clean-v2-16s-ledger.json")

if __name__ == "__main__":
    ui_agente.App(motor).mainloop()
