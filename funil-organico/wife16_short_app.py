#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE WIFE 16 — app desktop offline.

Ponto de entrada enxuto: a interface mora em ui_agente.py e a doutrina em
wife16_short.py. Mesmo padrao do `good16_short_app.py`.

⭐ O QUE O PAINEL DESENHA AQUI:

  · DUAS cenas de copy (A CAMA FRIA · A VIRADA NA AGUA).
  · QUATRO eixos: a regiao (que arrasta quarto + agua + luz + audio + traje
    dela + etnia), quem fala, a esposa e o copo do trick.
  · UMA trava de pre-selecao: `regiao`, para o operador fechar um lote inteiro
    numa familia de mundo.
  · ⛔ NENHUM botao de sexo — este agente so' produz narrador HOMEM
    (`SEXOS = ("homem",)`), e botao que nao troca nada e' pior que botao
    nenhum.
  · ⛔ NENHUM toggle `ref bela` — a esposa ja' nasce sob a LEI DO REF em todas
    as entradas do pool, entao o toggle nao mudaria um pixel. Mesma razao.
  · O seletor de pele funciona pelo caminho padrao (troca de pagina): a etnia
    deste motor vem da PAGINA, e o mundo e' filtrado por ela.

⛔ Ledger PROPRIO (`.wife-16-ledger.json`) — 16s e 24s sao lotes diferentes e
cada um varre o repertorio sem gastar o frescor do outro.

    python funil-organico/wife16_short_app.py
"""

import os
import sys

if getattr(sys, "frozen", False):          # rodando como .exe do PyInstaller
    sys.path.insert(0, sys._MEIPASS)
else:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ui_agente                  # noqa: E402
import wife16_short as motor      # noqa: E402

# o ledger acompanha o executavel, nao a pasta temporaria do PyInstaller
motor.LEDGER = os.path.join(ui_agente.base_dir(), ".wife-16-ledger.json")

if __name__ == "__main__":
    ui_agente.App(motor).mainloop()
