#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Desenha os icones dos .exe — um para os agentes, outro para o Veo Editor.

    python funil-organico/icones/gerar_icones.py

Requer Pillow (`pip install pillow`) e roda no Python do SISTEMA, nao no venv
do editor. Roda uma vez; o `.ico` fica versionado e o build so' o consome.

O DESENHO
---------
Quadrado de cantos arredondados com o degrade da marca, e por cima um quadro
9:16 branco — o formato que a operacao inteira produz. Dentro do quadro, o
glifo que separa as duas familias:

    agentes      laranja (#ff6a3d -> #e0522a)   um raio  = gera
    veo editor   teal    (#2ec4b6 -> #1f9e93)   um play  = edita

⚠️ Legibilidade em 16px e' o criterio, nao a beleza em 256. Por isso o glifo e'
uma silhueta cheia e nao um contorno: contorno de 1px vira cinza no icone
pequeno da barra de tarefas.
"""

import os

from PIL import Image, ImageDraw

AQUI = os.path.dirname(os.path.abspath(__file__))
LADO = 512                      # desenha grande e reduz — antialias de graca
TAMANHOS = [(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)]


def _degrade(tam, c1, c2):
    """Degrade vertical simples, sem dependencia extra."""
    img = Image.new("RGB", (1, tam), c1)
    px = img.load()
    for y in range(tam):
        t = y / float(tam - 1)
        px[0, y] = tuple(int(a + (b - a) * t) for a, b in zip(c1, c2))
    return img.resize((tam, tam))


def desenhar(c1, c2, glifo):
    base = Image.new("RGBA", (LADO, LADO), (0, 0, 0, 0))

    # a pastilha de cantos arredondados
    mask = Image.new("L", (LADO, LADO), 0)
    ImageDraw.Draw(mask).rounded_rectangle(
        [0, 0, LADO - 1, LADO - 1], radius=int(LADO * 0.22), fill=255)
    base.paste(_degrade(LADO, c1, c2), (0, 0), mask)

    d = ImageDraw.Draw(base)

    # o quadro 9:16 branco, centrado
    qh = int(LADO * 0.60)
    qw = int(qh * 9 / 16.0)
    x0, y0 = (LADO - qw) // 2, (LADO - qh) // 2
    d.rounded_rectangle([x0, y0, x0 + qw, y0 + qh],
                        radius=int(qw * 0.16), fill=(255, 255, 255, 245))

    cx, cy = LADO // 2, LADO // 2
    if glifo == "raio":
        # raio: silhueta cheia, na cor da pastilha para "vazar" o quadro
        u = qw * 0.34
        d.polygon([(cx + u * 0.35, cy - u * 1.5), (cx - u * 0.75, cy + u * 0.15),
                   (cx - u * 0.05, cy + u * 0.15), (cx - u * 0.35, cy + u * 1.5),
                   (cx + u * 0.85, cy - u * 0.25), (cx + u * 0.1, cy - u * 0.25)],
                  fill=c1)
    else:
        # play: triangulo cheio, mesma logica
        u = qw * 0.30
        d.polygon([(cx - u * 0.55, cy - u), (cx - u * 0.55, cy + u),
                   (cx + u * 0.95, cy)], fill=c1)

    return base


def salvar(img, nome):
    caminho = os.path.join(AQUI, nome)
    img.save(caminho, format="ICO", sizes=TAMANHOS)
    print("%-16s %d bytes" % (nome, os.path.getsize(caminho)))


if __name__ == "__main__":
    salvar(desenhar((255, 106, 61), (224, 82, 42), "raio"), "agente.ico")
    salvar(desenhar((46, 196, 182), (31, 158, 147), "play"), "editor.ico")
