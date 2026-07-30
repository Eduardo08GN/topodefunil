#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
nucleo_sonoro.py — reescrita fonetica dos substantivos do nucleo.

DESCOBERTA DO OPERADOR, 2026-07-30. O classificador do Veo casa TOKEN; o
sintetizador de voz casa FONEMA. Hifenizar o substantivo na fronteira silabica
quebra o match do classificador sem mudar UMA sílaba do que o REF fala.

    "Johnson" -> "John-son"   ✅ aprovado, e o REF falou com a sonoridade exata

E' a mesma alavanca do protocolo de recusa (`lap` -> `knee`), so' que na camada
da PALAVRA em vez da geometria: troca-se a forma de escrever, nunca o que e'
dito. Fonte da verdade do protocolo:
    funil-organico/prop-metaforas.md §Recusa do gerador

⚠️ ONDE ISTO SE APLICA: **so' na linha Dialogue: do TAKE**, que e' o que o
gerador le como fala. A direcao de cena nunca nomeia o orgao (a doutrina
proibe), e a legenda queimada nasce do Whisper rodando sobre o AUDIO — entao
ela transcreve "Johnson" normalmente, sem hifen. O espectador nunca ve isto.

⚠️ POR QUE O LINTER NAO QUEBRA: a copy do spec continua com o termo limpo. A
reescrita acontece no momento de montar o bloco. Assim a cota do orgao, a
rotacao e o teto de fala continuam contando o substantivo de verdade.
"""

import re

# 🟢 = validado em producao · 🟡 = hipotese, vale um render de teste por termo
NUCLEO_SONORO = {
    "Johnson": "John-son",   # 🟢 validado pelo operador 2026-07-30
    "manhood": "man-hood",   # 🟡 composto: o caso mais seguro pro TTS
    "pecker": "peck-er",     # 🟡 fronteira silabica limpa, "peck" e' palavra real
    "wiener": "wee-ner",     # 🟡 NAO e' "wien-er" de proposito: isso arrisca
                             #    sair "wine-er". "wee-ner" forca a sonoridade.
}

# ⛔ FORA DO MAPA, e por que:
#   soldier  — "sol-dier" arrisca "sol-dee-er"; e nao e' palavra de corpo
#   tool     — monossilabo, nao tem fronteira onde cortar
#   old boy  — ja' sao duas palavras separadas

_RX = {termo: re.compile(r"\b%s\b" % re.escape(termo), re.IGNORECASE)
       for termo in NUCLEO_SONORO}


def _mesma_caixa(molde, novo):
    """Preserva a maiuscula inicial do termo como ele aparecia na frase."""
    return novo[0].upper() + novo[1:] if molde[:1].isupper() else novo


def sonorizar(fala):
    """Devolve a fala com os substantivos do nucleo reescritos foneticamente."""
    for termo, rx in _RX.items():
        fala = rx.sub(lambda m: _mesma_caixa(m.group(0), NUCLEO_SONORO[termo]), fala)
    return fala


def termos_reescritos(fala):
    """Quais termos esta fala teve reescritos — para o painel avisar."""
    return [t for t, rx in _RX.items() if rx.search(fala)]
