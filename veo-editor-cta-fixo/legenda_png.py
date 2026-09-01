# -*- coding: utf-8 -*-
"""Desenha a LEGENDA FIXA como PNG transparente, com emoji COLORIDO.

⛔ POR QUE ISTO EXISTE, e por que nao da' para fazer no ASS.
   O ffmpeg queima legenda pelo libass, e o libass le apenas a camada de
   CONTORNO das fontes de emoji coloridas. Medido em render: coracao, fogo,
   mao e bebe sairam como linha branca. Nao e' ajuste, e' o que a biblioteca
   sabe fazer.

⭐ A saida e' desenhar a linha inteira FORA do ASS, com Pillow, que suporta
   `embedded_color=True` e le a camada de cor da `seguiemj.ttf`. Medido:
   o shrug saiu com (247,99,12) e (253,206,76) no PNG, cores que preto e
   branco nao produzem.

⛔ TEXTO E EMOJI PRECISAM DE FONTES DIFERENTES, e por isso a linha e' montada
   PEDACO A PEDACO em vez de num `draw.text` so'. A Arial Black nao tem o
   glifo do emoji e a Segoe UI Emoji nao serve para texto. Cada trecho e'
   medido e desenhado na sua fonte, na mesma linha de base.

⚠️ O emoji e' desenhado SEM contorno de proposito. Contorno preto em volta de
   um emoji colorido engrossa a silhueta e suja a cor; na referencia que o
   operador quer copiar o emoji e' limpo e so' o texto tem contorno.
"""

import os
import re

FONTE_TEXTO = r"C:\Windows\Fonts\ariblk.ttf"       # Arial Black
FONTE_EMOJI = r"C:\Windows\Fonts\seguiemj.ttf"     # Segoe UI Emoji (colorida)

# ⚠️ A Segoe UI Emoji so' entrega a camada COLORIDA em tamanhos que ela
# tem em bitmap. Fora deles o Pillow cai para o contorno e a cor some.
# 109 e' o tamanho nativo dela; qualquer outro e' redimensionado depois.
TAM_EMOJI_NATIVO = 109

_RE_EMOJI = re.compile(
    "([\U0001F000-\U0001FAFF\u2600-\u27BF\u2B00-\u2BFF\uFE0F\u200D]+)")


def _pedacos(texto):
    """Quebra a linha em [(trecho, e_emoji), ...] preservando a ordem."""
    saida = []
    for parte in _RE_EMOJI.split(texto):
        if parte:
            saida.append((parte, bool(_RE_EMOJI.fullmatch(parte))))
    return saida


def tem_emoji(texto):
    return bool(texto and _RE_EMOJI.search(texto))


def render(texto, largura_video, altura_video, cor_texto=(255, 255, 255),
           cor_contorno=(0, 0, 0), max_chars=24, out_path=None):
    """Devolve o caminho de um PNG transparente com a linha desenhada.

    A quebra em `max_chars` imita a do ASS para o texto nao sair mais largo
    que la'. As metricas nao batem caractere a caractere entre libass e
    Pillow, mas a contagem de caracteres e' a mesma regra dos dois.
    """
    from PIL import Image, ImageDraw, ImageFont

    tam = max(20, int(round(altura_video * 0.048)))     # o mesmo do ASS
    borda = max(3, int(round(altura_video * 0.004)))
    f_txt = ImageFont.truetype(FONTE_TEXTO, tam)
    f_emo = ImageFont.truetype(FONTE_EMOJI, TAM_EMOJI_NATIVO)
    escala_emo = tam / float(TAM_EMOJI_NATIVO)

    # quebra em linhas pela contagem de caracteres, como o ASS faz
    linhas, atual = [], ""
    for palavra in texto.split(" "):
        if atual and len(atual) + 1 + len(palavra) > max_chars:
            linhas.append(atual)
            atual = palavra
        else:
            atual = (atual + " " + palavra).strip()
    if atual:
        linhas.append(atual)

    alt_linha = int(tam * 1.25)
    tela = Image.new("RGBA", (largura_video, alt_linha * len(linhas) + borda * 4),
                     (0, 0, 0, 0))
    d = ImageDraw.Draw(tela)

    for i, linha in enumerate(linhas):
        pedacos = _pedacos(linha)
        # mede a linha inteira para centralizar
        larg = 0
        for trecho, e_emo in pedacos:
            if e_emo:
                larg += int(f_emo.getlength(trecho) * escala_emo)
            else:
                larg += int(f_txt.getlength(trecho))
        x = (largura_video - larg) // 2
        y = borda * 2 + i * alt_linha

        for trecho, e_emo in pedacos:
            if e_emo:
                # ⛔ o emoji e' desenhado em tamanho NATIVO num quadro proprio
                # e so' depois reduzido: desenhar direto no tamanho final faz
                # o Pillow perder a camada de cor.
                w = max(1, int(f_emo.getlength(trecho)))
                tmp = Image.new("RGBA", (w + 20, TAM_EMOJI_NATIVO + 40), (0, 0, 0, 0))
                ImageDraw.Draw(tmp).text((0, 0), trecho, font=f_emo,
                                         embedded_color=True)
                tmp = tmp.crop(tmp.getbbox() or (0, 0, 1, 1))
                nw = max(1, int(tmp.width * escala_emo))
                nh = max(1, int(tmp.height * escala_emo))
                tmp = tmp.resize((nw, nh), Image.LANCZOS)
                tela.alpha_composite(tmp, (x, y + (tam - nh) // 2 + int(tam * .1)))
                x += int(w * escala_emo)
            else:
                d.text((x, y), trecho, font=f_txt, fill=cor_texto + (255,),
                       stroke_width=borda, stroke_fill=cor_contorno + (255,))
                x += int(f_txt.getlength(trecho))

    tela = tela.crop(tela.getbbox() or (0, 0, 1, 1))
    if out_path is None:
        import tempfile
        out_path = os.path.join(tempfile.gettempdir(), "legenda_fixa.png")
    tela.save(out_path)
    return out_path
