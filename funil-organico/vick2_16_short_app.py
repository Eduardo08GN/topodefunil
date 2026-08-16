#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE VICK 2 16 — app desktop offline.

Ponto de entrada enxuto: a interface mora em ui_agente.py e a doutrina em
vick2_16_short.py.

⭐ O PAINEL:

  · DUAS cenas de copy (2 takes de 8s, AdBatch Vertical 2).
  · TRES eixos, e o primeiro deles E' A FONTE: A CENA — as 15 entradas sao os
    15 videos-fonte, cada um com o ambiente, a superficie, o angulo e a
    sequencia de gestos que aquele video faz. Nao ha cena inventada.
  · ONDE ELE PASSA — a regiao do corpo que recebe a pomada (nuca, peitoral,
    ombro, braco, barriga).
    ⛔⛔ TRAVAR ESTE EIXO RESTRINGE A CENA. So' 4 dos 15 videos aplicam a
    pomada no corpo; se o sorteio ignorasse isso, escolher `barriga` cairia
    numa cena que so' mexe o pote e o operador concluiria que o botao nao faz
    nada. Botao que promete e entrega outra coisa e' pior que botao ausente.
    ⚠️ E a REGIAO CARREGA A PROPRIA CAMERA: a nuca so' se ve' por tras, a
    barriga so' de frente. Sem esse acoplamento, metade dos videos mostraria
    um homem esfregando algo fora de quadro.
  · O HOOK — as 12 aberturas, todas verbatim dos videos da fonte.
  · ⭐ O CAMPO DA PALAVRA DO CTA. Este motor nasce em `recipe`, que e' a
    keyword dos 15 videos. ⛔ Trocar ali exige cadastrar a palavra na
    automacao de DM ANTES, senao o comentario entra e a mensagem nao sai.

⛔ SEM CELULAR EM QUADRO, e essa e' a razao de o agente existir. O `vick16`
escrevia `POV of a man ... with the phone in his free hand` no prompt de IMAGEM
e o gerador DESENHAVA o telefone. Aqui a camera descreve o angulo e a palavra
`phone` nao existe no motor — a lente VK1 reprova quem puser.

⛔ Ledger PROPRIO (`.vick2-16-ledger.json`).

    python funil-organico/vick2_16_short_app.py
"""

import os
import sys

if getattr(sys, "frozen", False):          # rodando como .exe do PyInstaller
    sys.path.insert(0, sys._MEIPASS)
else:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ui_agente                   # noqa: E402
import vick2_16_short as motor     # noqa: E402

# o ledger acompanha o executavel, nao a pasta temporaria do PyInstaller
motor.LEDGER = os.path.join(ui_agente.base_dir(), ".vick2-16-ledger.json")

if __name__ == "__main__":
    ui_agente.App(motor).mainloop()
