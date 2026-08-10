#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE FIGHT 16 — app desktop offline.

Ponto de entrada enxuto: a interface mora em ui_agente.py e a doutrina em
fight16_short.py. Mesmo padrao do `bed16_short_app.py`.

⭐ O QUE O PAINEL DESENHA AQUI:

  · DUAS cenas de copy (A BRIGA · O CASAL COLADO).
  · QUATRO eixos: o QUARTO DA BRIGA (take 1), o AMBIENTE DO CASAL (take 2),
    quem fala e a mulher.
  · ⛔⛔ OS DOIS EIXOS DE CENA SAO INDEPENDENTES, e e' isso que separa este
    painel do BED 16: la' um botao so' (a regiao) move os dois ambientes,
    porque os dois sao da mesma casa. Aqui o operador declarou duas listas
    separadas, entao sao dois botoes — e trocar um NAO mexe no outro.
  · ⭐ O toggle MODO BELA, pelo contrato compartilhado (`MODO_BELA = True` no
    motor). DESLIGADO ele entrega a mulher realista do print (34-43); LIGADO,
    a REF do pool bela do repo — e o modo move idade, porte, marca e o traje
    dela DENTRO do quarto e do ambiente ja' sorteados.
  · ⛔ NENHUM botao de sexo — este agente so' produz narrador HOMEM
    (`SEXOS = ("homem",)`), e botao que nao troca nada e' pior que botao
    nenhum.
  · ⛔ NENHUMA trava de lote: os dois eixos de cena ja' sao curtos e ja' sao
    travaveis video a video pelo cadeado. Um segundo controle para a mesma
    coisa e' onde o operador para de confiar no painel.
  · O seletor de pele funciona pelo caminho padrao (troca de pagina): a etnia
    deste motor vem da PAGINA e governa o HOMEM, que e' quem fala.

⛔ Ledger PROPRIO (`.fight-16-ledger.json`) — 16s e 24s sao lotes diferentes e
cada um varre o repertorio sem gastar o frescor do outro.

    python funil-organico/fight16_short_app.py
"""

import os
import sys

if getattr(sys, "frozen", False):          # rodando como .exe do PyInstaller
    sys.path.insert(0, sys._MEIPASS)
else:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ui_agente                    # noqa: E402
import fight16_short as motor       # noqa: E402

# o ledger acompanha o executavel, nao a pasta temporaria do PyInstaller
motor.LEDGER = os.path.join(ui_agente.base_dir(), ".fight-16-ledger.json")

if __name__ == "__main__":
    ui_agente.App(motor).mainloop()
