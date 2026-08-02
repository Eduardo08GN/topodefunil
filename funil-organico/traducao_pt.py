#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
traducao_pt.py — tradução EXATA da copy dos agentes, offline.

Não é tradutor de máquina. A copy dos motores nasce de **templates com slots**
(`"If you want your {o} to go from this to this..."`), então a tradução é uma
TABELA ligada a esses templates:

    1. casa a fala renderizada contra os templates conhecidos (regex derivada
       do próprio template, com `(.+?)` no lugar de cada slot)
    2. captura o que o sorteio pôs em cada slot
    3. traduz cada slot — recursivamente, porque slot como {gate} ou {barreira}
       é ele mesmo um template de outro pool
    4. monta o template PT com os slots traduzidos

Resultado: determinístico, sem rede, e exato enquanto a copy não for editada
à mão. Copy editada cai no modo APROXIMADO, e o app diz isso na cara.

⚠️ ISTO NÃO MEXE EM NADA DO OPERACIONAL. É consulta: recebe uma fala e
devolve o português. Nenhum motor importa este módulo, nenhum prompt muda.
O botão que a expõe é um patch local (Agentes Unicos Ed/app-traducao).

⛔ QUEM ESCREVE COPY NOVA ESCREVE O PT JUNTO, no mesmo commit. É o único jeito
de a tabela não envelhecer: a auditoria de drifting de 2026-08-01 derrubou a
cobertura de 100% para 58% num dia. Confira com:

    python funil-organico/traducao_pt.py --checar
"""
import re
import unicodedata

try:
    from traducao_dados import PT, TERMOS
except ImportError:                                   # pragma: no cover
    PT, TERMOS = {}, {}

_SLOT = re.compile(r"\{(\w+)\}")


def _limpo(s):
    """Normaliza para casar: espaço colapsado, aspas e travessões unificados."""
    s = unicodedata.normalize("NFC", s or "")
    for a, b in (("’", "'"), ("‘", "'"), ("“", '"'),
                 ("”", '"'), ("—", "-"), ("–", "-"),
                 ("�", "-")):
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip()


def _compilar(tpl):
    """Template -> (regex, [nomes dos slots na ordem])."""
    nomes, partes = [], []
    for p in re.split(r"(\{\w+\})", tpl):
        m = _SLOT.fullmatch(p)
        if m:
            nomes.append(m.group(1))
            partes.append(r"(.+?)")
        else:
            partes.append(re.escape(_limpo(p)))
    return re.compile(r"^\s*" + "".join(partes) + r"\s*$", re.I | re.S), nomes


# índice montado uma vez. Ordem: mais literal primeiro, senão um template curto
# e cheio de slots engole a frase que pertence a um template específico.
_INDICE = None


def _indice():
    global _INDICE
    if _INDICE is None:
        itens = []
        for en, pt in PT.items():
            rx, nomes = _compilar(en)
            literal = len(_SLOT.sub("", en))
            itens.append((literal, en, pt, rx, nomes))
        itens.sort(key=lambda x: -x[0])
        _INDICE = itens
    return _INDICE


def _slot(valor):
    """Traduz o conteúdo de um slot: termo do glossário, ou outro template."""
    v = _limpo(valor)
    if not v:
        return v
    chave = v.rstrip(" .,!?").lower()
    if chave in TERMOS:
        fim = v[len(v.rstrip(" .,!?")):]
        return TERMOS[chave] + fim
    achado = _casar(v)
    if achado:
        return achado[0]
    return v                                   # número, nome próprio, etc.


def _casar(texto):
    """(traducao, exata?) ou None."""
    alvo = _limpo(texto)
    for _lit, _en, pt, rx, nomes in _indice():
        m = rx.match(alvo)
        if not m:
            continue
        valores = {n: _slot(g) for n, g in zip(nomes, m.groups())}
        try:
            return pt.format(**valores), True
        except (KeyError, IndexError):
            continue
    return None


def traduzir(texto):
    """
    Devolve (portugues, exata).

    `exata=False` significa que a frase inteira não casou com nenhum template —
    o que na prática quer dizer copy editada à mão. Aí traduz frase a frase o
    que der, e o que não der fica em inglês, marcado.
    """
    if not _limpo(texto):
        return "", True
    achado = _casar(texto)
    if achado:
        return achado[0], True

    # Fala COMPOSTA: vários agentes montam a cena concatenando pools (o TROCA
    # faz isso nas três). Nenhum template casa a linha inteira, mas cada
    # sentença casa a sua — e o resultado disso é tão exato quanto o casamento
    # direto. Só é "aproximada" quando sobra sentença sem traducao, que na
    # prática quer dizer copy editada à mão.
    pedacos = re.split(r"(?<=[.!?])\s+", _limpo(texto))
    saida, faltou = [], False
    for p in pedacos:
        a = _casar(p)
        if a:
            saida.append(a[0])
        else:
            saida.append(p)
            faltou = True
    return " ".join(saida), not faltou


# ---------------------------------------------------------------------------
# O VERIFICADOR — e' ele que impede a tabela de envelhecer
# ---------------------------------------------------------------------------
# Sem isto, a unica forma de descobrir que a copy nova nao tem PT e' abrir o
# app e ver "≈ aproximada". A auditoria de drifting de 2026-08-01 derrubou a
# cobertura de 100% para 58% e ninguem percebeu ate alguem clicar no botao.

_IGNORA_POOL = {"CENAS_UI", "EIXOS_UI", "BANIDOS_TAKE", "BANIDOS_IMAGE",
                "BANIDOS_CTA", "NUCLEO", "JANELAS_TEMPO"}
_VISUAL = ("shot", "camera", "frame", "lens", "iphone", "watermark",
           "on-screen", "no subtitles", "medium ", "close-up", "low-angle")


def _eh_copy(s):
    b = s.lower()
    return len(s.split()) >= 3 and not any(v in b for v in _VISUAL)


def checar(alvo=None):
    """Varre os pools dos motores e devolve {modulo.POOL: [strings sem PT]}."""
    import ast
    import collections
    import glob
    import os
    aqui = os.path.dirname(os.path.abspath(__file__))
    falta = collections.defaultdict(list)
    total = 0
    arqs = sorted(set(glob.glob(os.path.join(aqui, "*_lucas.py")) +
                      glob.glob(os.path.join(aqui, "*_short.py")) +
                      [os.path.join(aqui, "short_comum.py")]))
    for caminho in arqs:
        mod = os.path.basename(caminho)[:-3]
        if alvo and alvo.lower() not in mod.lower():
            continue
        with open(caminho, encoding="utf-8") as f:
            try:
                arvore = ast.parse(f.read())
            except SyntaxError:
                continue
        for node in arvore.body:
            if not (isinstance(node, ast.Assign)
                    and isinstance(node.value, (ast.List, ast.Tuple))):
                continue
            a = node.targets[0]
            nome = a.id if isinstance(a, ast.Name) else ""
            if not nome.isupper() or nome in _IGNORA_POOL:
                continue
            vistos = set()
            for x in ast.walk(node.value):
                if not (isinstance(x, ast.Constant)
                        and isinstance(x.value, str) and _eh_copy(x.value)):
                    continue
                s = x.value
                if s in vistos:
                    continue
                vistos.add(s)
                total += 1
                if s.lower().rstrip(" .,!?") in TERMOS or _casar(s):
                    continue
                falta["%s.%s" % (mod, nome)].append(s)
    return falta, total


def _cli():
    import sys
    alvo = next((a for a in sys.argv[1:] if not a.startswith("-")), None)
    despejar = "--listar" in sys.argv
    falta, total = checar(alvo)
    som = sum(len(v) for v in falta.values())
    if despejar:
        for pool in sorted(falta):
            print("### %s (%d)" % (pool, len(falta[pool])))
            for s in sorted(falta[pool]):
                print(repr(s))
            print()
    pct = 100.0 * (total - som) / total if total else 100.0
    print("copy nos pools: %d | sem traducao: %d | cobertura %.1f%%"
          % (total, som, pct))
    if som:
        import collections
        por = collections.Counter()
        for p, v in falta.items():
            por[p.split(".")[0]] += len(v)
        for n, c in por.most_common():
            print("  %-22s %d" % (n, c))
        print()
        print("  detalhe:  python traducao_pt.py <agente> --listar")
    return 1 if som else 0


if __name__ == "__main__":
    raise SystemExit(_cli())
