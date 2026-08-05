#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE CHA SHORT — app desktop offline.

Ponto de entrada enxuto: a interface mora em ui_agente.py (compartilhada por
todos os agentes portados) e a doutrina em cha_short.py.

Fonte: reel 1669063827687365 (31K views · 1.4K reacoes · **2.4K comentarios**).
Comentarios acima das reacoes — este angulo e' o melhor CTA de comentario do
repertorio, e e' por isso que ele existe.

⭐ O que este painel tem de proprio:

  · A CASA e' UM eixo so' — varanda E cozinha juntas. E' o unico agente do
    repertorio com corte de ambiente dentro do video (a fonte corta em 0:07), e
    sortear os dois separados devolveria uma varanda do Texas com uma cozinha do
    Brooklyn. Dezesseis casas em treze arquetipos REGIONAIS dos EUA (Brooklyn,
    Louisiana, Texas, Apalaches, Miami, Detroit...), nunca heranca imigrante.
  · O TRAJE logo abaixo da REF, e com cadeado. Nao e' vaidade de painel: e' a
    bullet de retencao deste angulo por ordem do operador, e o eixo que o
    operador mais vai querer travar quando um lote sair bom.
  · O RARO no painel: um ingrediente pouco conhecido por video, e a fala o traz
    sempre com o APOSTO colado (`maca root, that Andean root from Peru`).
  · O COMUM tambem, porque a copy os NOMEIA — trocar um deles remonta a fala da
    cena 2 (EIXOS_QUE_MEXEM_NA_COPY).

⛔ O que este agente NAO tem, porque a fonte nao tem: homem em cena, corpo-prova,
prop falico, substancia absurda, vilao. O objeto e' a CANECA DE CHA, estendida no
braco esticado para a lente. Se um desses eixos reaparecer no painel, alguem
religou pool morto do BOTICA — e o video sai com a fala certa e a imagem de outro
angulo (licoes §29).

⛔ Ledger PROPRIO (`.cha-short-ledger.json`), como todo agente.

    python funil-organico/cha_short_app.py
"""

import os
import sys

if getattr(sys, "frozen", False):          # rodando como .exe do PyInstaller
    sys.path.insert(0, sys._MEIPASS)
else:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ui_agente               # noqa: E402
import cha_short as motor      # noqa: E402

# o ledger acompanha o executavel, nao a pasta temporaria do PyInstaller
motor.LEDGER = os.path.join(ui_agente.base_dir(), ".cha-short-ledger.json")

if __name__ == "__main__":
    ui_agente.App(motor).mainloop()
