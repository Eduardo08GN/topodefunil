#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE EXTERIOR SHORT — app desktop offline.

Ponto de entrada enxuto: a interface mora em ui_agente.py (compartilhada por
todos os agentes portados) e a doutrina em exterior_short.py.

⚠️ Como o RESSURREICAO, o TROCA e o ESCANDALO, este e' SHORT NATIVO: nao
colapsa motor longo nenhum — nao existe `exterior_lucas.py`. O
`exterior_short.py` e' motor completo (pools proprios) e so' toma emprestada a
maquinaria compartilhada do `short_comum.py`.

    python funil-organico/exterior_short_app.py
"""

import os
import sys

if getattr(sys, "frozen", False):          # rodando como .exe do PyInstaller
    BASE = os.path.dirname(sys.executable)
    sys.path.insert(0, sys._MEIPASS)
else:
    BASE = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, BASE)

import ui_agente                           # noqa: E402
import exterior_short as motor             # noqa: E402

# o ledger acompanha o executavel, nao a pasta temporaria do PyInstaller
motor.LEDGER = os.path.join(BASE, ".exterior-short-ledger.json")

if __name__ == "__main__":
    ui_agente.App(motor).mainloop()
