#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE AMISH 16S — app desktop offline.

Ponto de entrada enxuto: a interface mora em ui_agente.py e a doutrina em
amish16_short.py.

⭐ E' o primeiro motor do parque FORA do nicho ED: emagrecimento, clonado dos
18 reels 50k+ da pagina Martha.Knows (lidos quadro a quadro em 21/08).

⭐ O PAINEL:

  · TRES cenas (DAY 1 mudo · DAY 47-57 mudo · SELFIE + CTA). A fala inteira
    mora na cena 3 — as duas primeiras sao mudas por fidelidade a fonte.
  · QUATRO eixos: A COPY (as 4 validadas, renumeradas por uso e views),
    O CENARIO (12 rotacoes da fazenda Amish), QUEM MUDA (o look do sujeito,
    filtrado pelo sexo travado) e A LEGENDA DAY (o estilo que o VEO escreve).
  · O seletor QUEM NARRA fixa um dos NOVE narradores — a vovo Amish e' a
    ancora (so' a COR do vestido dela roda), e ha' a moca de 25, o vovo
    Amish, os dois medicos, os dois indigenas e os dois curandeiros.
  · QUATRO pre-selecoes: copy (1-4), quem muda (homem/mulher) e as duas
    peles (narrador e sujeito). ⚠️ Indigenas e curandeiros tem identidade
    fixa: a trava de pele neles e' IGNORADA COM AVISO, nunca em silencio.
  · A palavra do CTA nasce YES — e' a da fonte (18 de 18) e a ordem do
    operador. ⛔ A automacao de DM da pagina nova tem de nascer cadastrada
    em YES, senao o comentario entra e a mensagem nao sai.

⛔ Ledger PROPRIO (`.amish-16s-ledger.json`).

    python funil-organico/amish16_short_app.py
"""

import os
import sys

if getattr(sys, "frozen", False):          # rodando como .exe do PyInstaller
    sys.path.insert(0, sys._MEIPASS)
else:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ui_agente                     # noqa: E402
import amish16_short as motor        # noqa: E402

# o ledger acompanha o executavel, nao a pasta temporaria do PyInstaller
motor.LEDGER = os.path.join(ui_agente.base_dir(), ".amish-16s-ledger.json")

if __name__ == "__main__":
    ui_agente.App(motor).mainloop()
