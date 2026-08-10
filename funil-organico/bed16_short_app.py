#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE BED 16 — app desktop offline.

Ponto de entrada enxuto: a interface mora em ui_agente.py e a doutrina em
bed16_short.py. Mesmo padrao do `good16_short_app.py`.

⭐ O QUE O PAINEL DESENHA AQUI:

  · DUAS cenas de copy (A CAMA E A TIGELA · A TIGELA NAS MAOS DELA).
  · QUATRO eixos: a regiao (que arrasta quarto + agua + luz + audio + traje
    dela + etnia), quem fala, a esposa e a tigela do trick.
  · UMA trava de pre-selecao: `regiao`, para o operador fechar um lote inteiro
    numa familia de mundo.
  · ⭐ O toggle MODO BELA, pelo contrato compartilhado (`MODO_BELA = True` no
    motor). DESLIGADO ele entrega a esposa realista do print (44-52); LIGADO,
    a REF do pool bela do repo — e o modo move idade, porte e o traje dela
    DENTRO da regiao ja' sorteada.
  · ⛔ NENHUM botao de sexo — este agente so' produz narrador HOMEM
    (`SEXOS = ("homem",)`), e botao que nao troca nada e' pior que botao
    nenhum.
  · O seletor de pele funciona pelo caminho padrao (troca de pagina): a etnia
    deste motor vem da PAGINA, e o mundo e' filtrado por ela.

⛔ Ledger PROPRIO (`.bed-16-ledger.json`) — 16s e 24s sao lotes diferentes e
cada um varre o repertorio sem gastar o frescor do outro.

    python funil-organico/bed16_short_app.py
"""

import os
import sys

if getattr(sys, "frozen", False):          # rodando como .exe do PyInstaller
    sys.path.insert(0, sys._MEIPASS)
else:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ui_agente                  # noqa: E402
import bed16_short as motor       # noqa: E402

# o ledger acompanha o executavel, nao a pasta temporaria do PyInstaller
motor.LEDGER = os.path.join(ui_agente.base_dir(), ".bed-16-ledger.json")

if __name__ == "__main__":
    ui_agente.App(motor).mainloop()
