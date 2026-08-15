#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE BANHO 16 3TAKES — app desktop offline.

Ponto de entrada enxuto: a interface mora em ui_agente.py e a doutrina em
banho16_3t_short.py.

⛔⛔ NAO SUBSTITUI o BANHO 16 nem o BANHO 16 V2. Os tres convivem, como o
CLEAN v1/v2. O que muda aqui e' o RELOGIO — TRES takes de ~5s em vez de dois
de 8s — e o relogio arrasta tudo: teto de 14 palavras por cena em vez de 25,
tres imagens em vez de duas, destino AdBatch **Vertical 3** em vez de
Vertical 2.

⭐ O PAINEL:

  · TRES cenas de copy (`O HOOK` · `O PREPARO` · `A REACAO + CTA`).
  · SEIS eixos, e o primeiro deles e' A COPY: sao 12 familias aprovadas uma a
    uma pelo operador em 14/08, e a familia e' ATOMICA — as tres cenas vem
    juntas, escritas para casar. ⛔ Nao ha' sorteio por beat aqui, e isso e'
    de proposito: no BANHO 16 o hook e o fecho vem de pools independentes, e
    5 dos 9 hooks abriam com as MESMAS tres palavras (medido: 55% dos
    sorteios). Combinacao nominal nunca foi a metrica; distancia percebida e'.
  · Os outros cinco eixos sao de CENA: O BANHEIRO, A SUPERFICIE, A MEDIDA,
    O ROTULO e A RECEITA.
  · DUAS pre-selecoes: `cenario` (box / banheira / pia) e ⭐⭐ `explica?`.
  · ⭐⭐ `explica?` E' UM EXPERIMENTO, nao um enfeite. Na fonte, o reel de
    melhor taxa de comentario (20,5 por mil views, 2,5x o segundo colocado) e'
    o UNICO dos sete que nao explica o mecanismo: ele avisa, promete e pede.
    ⚠️ Mas esse reel e' unico em TRES coisas ao mesmo tempo — hook de
    exclusao, sem mecanismo, e o mais curto — e com sete pontos nao da' para
    separar qual causa o que. Rodar 15 videos de cada lado responde em campo
    o que a fonte nao responde.
  · ⭐ UM TOGGLE, `MODO PESSOA`, e ele NASCE DESLIGADO. Ordem do operador:
    *"no sorteio gerar somente sem pessoas no quadro, pois foi o padrao que
    mais se repetiu e deu certo na pagina"* — 1 video em 7 da fonte tem gente.

⛔ Ledger PROPRIO (`.banho-16-3t-ledger.json`). Compartilhar o ledger com o
BANHO 16 faria a memoria de um motor apagar a frescura do outro.

    python funil-organico/banho16_3t_short_app.py
"""

import os
import sys

if getattr(sys, "frozen", False):          # rodando como .exe do PyInstaller
    sys.path.insert(0, sys._MEIPASS)
else:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ui_agente                     # noqa: E402
import banho16_3t_short as motor     # noqa: E402

# o ledger acompanha o executavel, nao a pasta temporaria do PyInstaller
motor.LEDGER = os.path.join(ui_agente.base_dir(), ".banho-16-3t-ledger.json")

if __name__ == "__main__":
    ui_agente.App(motor).mainloop()
