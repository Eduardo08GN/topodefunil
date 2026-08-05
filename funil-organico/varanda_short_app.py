#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE VARANDA SHORT — app desktop offline.

Ponto de entrada enxuto: a interface mora em ui_agente.py (compartilhada por
todos os agentes portados) e a doutrina em varanda_short.py.

⭐ O que este painel tem de proprio:

  · A REF e' a BULLET DE RETENCAO, e nao um figurante. Ordem do operador ao
    encomendar o agente: *"a ref mulher tem que ser extremamente linda e com um
    corpo muito atrativo, e' imperativo que ela use roupas com muito decote,
    que mostre bastante o corpo, saias curtas, pernas"*. Por isso o FIGURINO e'
    eixo proprio e travavel — nos outros agentes a roupa vem de dentro do mundo.
  · ETNIA SOLTA. Aqui o mundo NAO arrasta a etnia: a casa e' sempre americana
    (varanda com bandeira, cozinha de casa), e so' a REF varia. Foi decisao do
    operador, contra o padrao do BOTICA, e esta' registrada no motor.
  · O RARO no painel, herdado do BOTICA: um ingrediente pouco conhecido por
    video, sempre com o APOSTO colado (`maca root, that Andean root from Peru`).
  · AS DUAS AMIGAS do take 3, cada uma com a propria reacao sorteada.

⛔ Ledger PROPRIO (`.varanda-short-ledger.json`), como todo agente.

    python funil-organico/varanda_short_app.py
"""

import os
import sys

if getattr(sys, "frozen", False):          # rodando como .exe do PyInstaller
    sys.path.insert(0, sys._MEIPASS)
else:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ui_agente                   # noqa: E402
import varanda_short as motor      # noqa: E402

# o ledger acompanha o executavel, nao a pasta temporaria do PyInstaller
motor.LEDGER = os.path.join(ui_agente.base_dir(), ".varanda-short-ledger.json")

if __name__ == "__main__":
    ui_agente.App(motor).mainloop()
