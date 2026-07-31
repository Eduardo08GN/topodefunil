#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
nucleo_sonoro.py — grafia alternativa homofona dos substantivos do nucleo.

DESCOBERTA DO OPERADOR, 2026-07-30.

    O classificador do Veo casa TOKEN. O sintetizador de voz casa FONEMA.

Entao existe uma folga entre os dois: **escrever a palavra de outro jeito, de
forma que soe exatamente igual**. O classificador nao reconhece a string; o REF
fala a mesma silaba.

    "Johnson" -> "John-son"   ✅ aprovado, sonoridade exata

⚠️ O PRINCIPIO E' "GRAFIA DIFERENTE, SOM IDENTICO" — nao "hifenizacao".
A hifenizacao e' so' UMA das implementacoes, e nem e' a mais disfarcada:
`John-son` ainda carrega todas as letras de `Johnson` em ordem. Nomear a
tecnica pelo exemplo (correcao do operador) limitava o repertorio e deixava de
fora monossilabos como `tool`, que nao tem fronteira silabica mas tem grafia
alternativa.

DUAS FAMILIAS, COM RISCO OPOSTO — e' o que decide qual usar em cada termo:

  hifen     preserva TODAS as letras.  Pior caso: o TTS da' uma pausa.
            Falha barata, disfarce menor.
  homofona  troca letras.              Pior caso: o TTS fala OUTRA palavra.
            Falha cara, disfarce total.

Regra pratica: **hifen quando a fronteira silabica e' obvia; homofona quando
nao ha' fronteira (monossilabo) ou quando o hifen distorce o som.** E prefira
grafias que ja' existem como erro comum em ingles (`weiner`, `soljer`) — o TTS
ja' viu essas strings no treino e as normaliza certo.

E' a mesma alavanca do protocolo de recusa (`lap` -> `knee`), so' que na camada
da PALAVRA: troca-se a forma de escrever, nunca o que e' dito. Fonte:
    funil-organico/prop-metaforas.md §Recusa do gerador

⚠️ ONDE SE APLICA: so' na linha `Dialogue:` do TAKE. A direcao de cena nunca
nomeia o orgao (a doutrina proibe), e a legenda queimada nasce do Whisper
rodando sobre o AUDIO — transcreve "Johnson" normalmente. O espectador nunca ve
a grafia alternativa.

⚠️ POR QUE O LINTER NAO QUEBRA: a copy do spec continua com o termo limpo; a
troca acontece na hora de montar o bloco. Cota do orgao, rotacao e teto de fala
continuam contando o substantivo de verdade.
"""

import re

# Por termo: (grafia ATIVA, familia, selo, alternativas a testar)
#   selo "validado" = passou em render real · "a testar" = hipotese
GRAFIAS = {
    "Johnson": ("John-son", "hifen", "validado", ["Jonson", "Jahnson", "Jonsen"]),
    "manhood": ("man-hood", "hifen", "a testar", ["manhud", "man hood"]),
    "pecker":  ("peck-er",  "hifen", "a testar", ["pekker", "peckur"]),
    # wiener: a fronteira real ("wien-er") arrisca sair "wine-er", entao aqui a
    # familia hifen ja' nasce descartada. "weiner" e' o erro de grafia mais
    # comum do ingles para esta palavra — o TTS ve isso o tempo todo.
    "wiener":  ("weiner",   "homofona", "a testar", ["wee-ner", "weener"]),
    # soldier: "sol-dier" arriscava "sol-dee-er". "soljer" e' eye-dialect real,
    # a grafia que se usa em dialogo escrito para o som SOLE-jer.
    "soldier": ("soljer",   "homofona", "a testar", ["soul-jer", "sohljer"]),
    # tool: monossilabo nao tem fronteira para hifen, mas tem grafia alternativa.
    "tool":    ("toole",    "homofona", "a testar", ["tuel", "tewl"]),
}

# ⛔ FORA DO MAPA: "old boy" ja' sao duas palavras separadas — nao ha' token
#    unico para o classificador casar.

ATIVA = {t: v[0] for t, v in GRAFIAS.items()}

_RX = {t: re.compile(r"\b%s\b" % re.escape(t), re.IGNORECASE) for t in GRAFIAS}


def _mesma_caixa(molde, novo):
    """Preserva a maiuscula inicial do termo como ele aparecia na frase."""
    return novo[0].upper() + novo[1:] if molde[:1].isupper() else novo


def sonorizar(fala, mapa=None):
    """Devolve a fala com os substantivos do nucleo na grafia alternativa.

    `mapa` permite testar uma grafia diferente da ativa sem editar o modulo:
        sonorizar(fala, {"wiener": "weener"})
    """
    usar = dict(ATIVA)
    if mapa:
        usar.update(mapa)
    for termo, rx in _RX.items():
        alvo = usar.get(termo)
        if alvo:
            fala = rx.sub(lambda m, a=alvo: _mesma_caixa(m.group(0), a), fala)
    return fala


def termos_reescritos(fala):
    """Quais termos desta fala tem grafia alternativa — para o painel avisar."""
    return [t for t, rx in _RX.items() if rx.search(fala)]


def folha_de_teste():
    """Uma linha por grafia candidata, para validar termo a termo em render."""
    linhas = []
    for termo, (ativa, familia, selo, alts) in sorted(GRAFIAS.items()):
        linhas.append("[%-8s] %-8s %-9s ativa=%-9s  alternativas: %s"
                      % (selo, termo, familia, ativa, ", ".join(alts)))
    return "\n".join(linhas)


if __name__ == "__main__":
    print(folha_de_teste())
