#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE VICK 16 — app desktop offline.

Ponto de entrada enxuto: a interface mora em ui_agente.py e a doutrina em
vick16_short.py.

⭐ O PAINEL:

  · DUAS cenas de copy (2 takes de 8s, AdBatch Vertical 2).
  · TRES eixos, e o primeiro deles e' o maior do parque: A CENA (100 entradas,
    100 superficies DISTINTAS), O GESTO (95) e QUEM (100).
    ⛔⛔ A CENA E' A UNIDADE ATOMICA — ambiente, superficie, camera,
    enquadramento, luz e audio viajam JUNTOS num objeto so. Nao ha eixo de
    "ambiente" separado, e isso NAO e' esquecimento: com os dois soltos o
    sorteio cruzaria `prateleira de canto do box` com `espreguicadeira de
    praia`. E' o defeito que o commit dfb5d88 documenta.
  · Uma pre-selecao de HOOK (`TRAVAS_UI`): livre | mecanismo | historia.
    ⭐ As duas familias nunca se misturam no mesmo video — a de MECANISMO abre
    em idade ou condicao, a de HISTORIA abre numa perda concreta da relacao.
    Foi o v11 da fonte que virou esse segundo eixo, por ordem do operador.
  · ⭐ O CAMPO DA PALAVRA DO CTA. Este motor nasce em `recipe`, nao em
    `gelatin` — e' a keyword dos 15 videos da fonte. Trocar ali vale para o
    video inteiro; ⛔ mas a palavra tem de estar cadastrada na automacao de DM
    ANTES, senao o comentario entra e a mensagem nao sai.
  · SEM toggles de modo: a presenca da pessoa (so as maos, maos e antebraco,
    tronco, corpo inteiro) e' EIXO SORTEADO dentro de QUEM, nao botao.

⛔ Ledger PROPRIO (`.vick-16-ledger.json`) — memoria de 12 por eixo, que e' o
dobro da dos irmaos: com 100 entradas por pool, sorteio sem memoria repete
igual e o operador conclui que o pool e' pequeno.

    python funil-organico/vick16_short_app.py
"""

import os
import sys

if getattr(sys, "frozen", False):          # rodando como .exe do PyInstaller
    sys.path.insert(0, sys._MEIPASS)
else:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ui_agente                   # noqa: E402
import vick16_short as motor       # noqa: E402

# o ledger acompanha o executavel, nao a pasta temporaria do PyInstaller
motor.LEDGER = os.path.join(ui_agente.base_dir(), ".vick-16-ledger.json")

if __name__ == "__main__":
    ui_agente.App(motor).mainloop()
