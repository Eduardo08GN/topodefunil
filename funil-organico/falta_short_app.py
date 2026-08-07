#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE FALTA SHORT — app desktop offline.

Ponto de entrada enxuto: a interface mora em ui_agente.py (compartilhada por
todos os agentes portados) e a doutrina em falta_short.py.

⭐ O que este painel tem de proprio:

  · O PROP como eixo sorteavel — geoduck OU a peca anatomica peniana, um por
    video. E' o objeto que recebe o despejo e que MUDA na tela: pescoco murcho
    -> ereto, corpo cavernoso caido -> ereto. Escolha do operador na entrevista
    de 2026-08-06.
  · DUAS mulheres nas tres cenas e NENHUM homem. A REF fala; a segunda e' muda,
    olha o prop e nunca a lente. Por isso o painel tem QUEM FALA e A AMIGA como
    eixos separados — sem isso o Veo poe dois rostos iguais no mesmo quadro.
  · MODO BELA de nascenca, por ordem dele (*mulheres extremamente lindas, roupa
    curta*). Com o modo ligado a REF e a amiga saem do pool bela, e a amiga
    nunca herda o cabelo da REF.
  · A REGIAO na pre-selecao (TRAVAS_UI) — as familias de mundo dos EUA. A ETNIA
    sai de DENTRO do mundo, nunca solta: variar etnia e' arrastar o mundo
    inteiro (cenario, traje, luz), nunca trocar so' o rosto.
  · O RARO no painel, sempre com o APOSTO colado (`maca root, that Andean root
    from Peru`) — nome cientifico soa a rotulo de farmacia.
  · A ISCA (a substancia despejada) e o PREPARO tambem, porque a copy os toca:
    a isca e' NOMEADA na cena 1 e o utensilio manda no verbo da cena 2.

⛔ Ledger PROPRIO (`.falta-short-ledger.json`), como todo agente.

    python funil-organico/falta_short_app.py
"""

import os
import sys

if getattr(sys, "frozen", False):          # rodando como .exe do PyInstaller
    sys.path.insert(0, sys._MEIPASS)
else:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ui_agente                  # noqa: E402
import falta_short as motor       # noqa: E402

# o ledger acompanha o executavel, nao a pasta temporaria do PyInstaller
motor.LEDGER = os.path.join(ui_agente.base_dir(), ".falta-short-ledger.json")

if __name__ == "__main__":
    ui_agente.App(motor).mainloop()
