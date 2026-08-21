#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE RUTH 16 — app desktop offline.

Ponto de entrada enxuto: a interface mora em ui_agente.py e a doutrina em
ruth16_short.py.

⛔⛔ ELE NAO E' IRMAO DOS 32 DE GELATINA. Rota propria, oferta propria:
**emagrecimento**, CTA em `recipe`, e nada de gelatina no motor. Publicar isto
apontando para a VSL de gelatina quebra a congruencia de proposito. Mesmo
desenho do RARO 16.

⭐ O PAINEL:

  · TRES cenas de copy (`A HUMILHACAO` · `O REENCONTRO` · `A RECEITA + CTA`),
    destino AdBatch **Vertical 3**, teto de 25 palavras por cena (8,0s x 3,1
    palavras/s, os dois MEDIDOS — nao e' o 14 do BANHO 16 3T, que saiu de uma
    suposicao de take de 5s que a medicao desmentiu).
  · SEIS eixos: O DESASTRE, A PESSOA, O REENCONTRO, A PECA ANCORA, O ROSTO
    (REF) e A TESTEMUNHA.
  · ⭐⭐ **A PECA ANCORA e' o eixo que resolve o problema central do angulo.**
    A mesma pessoa aparece OBESA no take 1 e MAGRA nos takes 2 e 3, em quadros
    gerados separadamente — a continuidade mais cara que este parque ja' pediu.
    A saida veio da leitura otica: no melhor reel da fonte a MESMA blusa
    floral atravessa os dois atos, esticada no corpo obeso e caindo solta no
    corpo magro. Ancora de continuidade e prova de emagrecimento no mesmo
    objeto.
  · DUAS pre-selecoes: `o alvo` (mulher / homem / casal) e ⭐⭐ `rosto no ato
    1`.
  · ⭐⭐ `rosto no ato 1` E' UM EXPERIMENTO, nao um enfeite. A fonte esconde o
    rosto da pessoa obesa em 6 dos 15 reels e o mostra nos outros 9 — e o
    unico reel com testemunha de verdade em foco e' justamente um dos que
    MOSTRAM. Esconder facilita a continuidade e custa identificacao; mostrar
    faz o contrario. Quinze pontos nao separam as duas coisas; quinze videos
    de cada lado separam.
  · ⛔ A palavra do CTA e' campo (`recipe`). `yes` e `book` sao recusados pela
    propria UI — `yes` e' o que a fonte pede em praticamente todos os 60 posts
    e quebra a automacao de DM.

⛔ Ledger PROPRIO (`.ruth-16-ledger.json`).

    python funil-organico/ruth16_short_app.py
"""

import os
import sys

if getattr(sys, "frozen", False):          # rodando como .exe do PyInstaller
    sys.path.insert(0, sys._MEIPASS)
else:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ui_agente                # noqa: E402
import ruth16_short as motor    # noqa: E402

# o ledger acompanha o executavel, nao a pasta temporaria do PyInstaller
motor.LEDGER = os.path.join(ui_agente.base_dir(), ".ruth-16-ledger.json")

if __name__ == "__main__":
    ui_agente.App(motor).mainloop()
