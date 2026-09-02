#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE LIVRO 5 — app desktop offline.

Interface em `ui_agente.py`, doutrina inteira em `livro5_short.py`.

5 takes de 8s = 40 segundos, destino AdBatch **Vertical 5**, fala em INGLES.
⛔ O TAKE 1 E' MUDO — e' o "antes". No Veo Editor, o rotulo `MONTH 1` entra
pelo campo de CTA fixo, queimado por cima, nunca pedido ao gerador.

    python funil-organico/livro5_short_app.py
"""

import os
import sys

if getattr(sys, "frozen", False):
    BASE = os.path.dirname(sys.executable)
    sys.path.insert(0, sys._MEIPASS)
else:
    BASE = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, BASE)

import ui_agente                # noqa: E402
import livro5_short as motor    # noqa: E402

motor.LEDGER = os.path.join(BASE, ".livro-5-ledger.json")

if __name__ == "__main__":
    ui_agente.App(motor).mainloop()
