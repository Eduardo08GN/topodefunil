#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE ALFA 16 — app desktop offline.

Ponto de entrada enxuto: a interface mora em ui_agente.py e a doutrina em
alfa16_short.py. Mesmo padrao do `fight16_short_app.py`.

⭐ O QUE O PAINEL DESENHA AQUI:

  · DUAS cenas de copy (O AVISO · AS DUAS DO LADO).
  · SEIS eixos: o QUARTO do take 1, o AMBIENTE do take 2, quem fala, as DUAS
    mulheres (uma por botao) e o ENVOLTORIO delas.
  · ⛔⛔ OS DOIS EIXOS DE CENA SAO INDEPENDENTES — o operador ditou duas listas
    separadas, entao sao dois botoes, e trocar um NAO mexe no outro. Quem
    atravessa o corte sao as TRES PESSOAS, nunca a casa.
  · ⭐ DOIS botoes de mulher, e nao um: as duas aparecem nos DOIS takes e o
    operador precisa poder trocar UMA sem perder a outra. O sorteio garante
    que nunca saem iguais.
  · ⭐ O toggle MODO BELA move as DUAS pela `sc.ref_bela`.
  · ⭐ O toggle MODO FORTE tem POOL PROPRIO, 50+: ele nao troca a pessoa, troca
    o CORPO dela. O pool compartilhado do repo tem 26-38 anos e nao serve num
    angulo cujo REF o operador travou em 50+.
  · ⛔ NENHUM botao de sexo — este agente so' produz narrador HOMEM
    (`SEXOS = ("homem",)`), e botao que nao troca nada e' pior que botao
    nenhum.

⛔ Ledger PROPRIO (`.alfa-16-ledger.json`) — cada agente varre o proprio
repertorio sem gastar o frescor do outro.

    python funil-organico/alfa16_short_app.py
"""

import os
import sys

if getattr(sys, "frozen", False):          # rodando como .exe do PyInstaller
    sys.path.insert(0, sys._MEIPASS)
else:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ui_agente                    # noqa: E402
import alfa16_short as motor        # noqa: E402

# o ledger acompanha o executavel, nao a pasta temporaria do PyInstaller
motor.LEDGER = os.path.join(ui_agente.base_dir(), ".alfa-16-ledger.json")

if __name__ == "__main__":
    ui_agente.App(motor).mainloop()
