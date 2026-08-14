# -*- coding: utf-8 -*-
"""Tira a declaracao de anti-celebridade do FONTE dos motores — uma vez so'.

    python funil-organico/tirar_anticeleb.py            # --dry-run (padrao)
    python funil-organico/tirar_anticeleb.py --aplicar   # grava
    python funil-organico/tirar_anticeleb.py --autoteste # so' os controles

⛔⛔ ORDEM DO OPERADOR, 2026-08-14: *"tire not a celebrity do prompt"*.
A doutrina existia desde 2026-07-31 (`CLAUDE.md` §CONTRA A CELEBRIDADE,
SILENCIO) e nunca tinha sido aplicada: a declaracao NAO E' NEUTRA — escrever a
negacao POE o token no campo, e o classificador casa TOKEN, nao intencao.

⛔ E NAO SE TROCA POR OUTRA NEGACAO: `not a model`, `not an actor`, `not
resembling any famous person` sao a MESMA municao com outra roupa. A defesa e'
descrever um rosto que nenhuma celebridade tem — e isso e' COPY, alcada do
operador. ⭐ AQUI SO' SE REMOVE, E A METADE POSITIVA FICA:
`"Ordinary relatable face, not a celebrity."` vira `"Ordinary relatable face."`

⚠️ POR QUE UMA FERRAMENTA E NAO EDICAO A MAO — o precedente e' o
`tirar_bandeira` do `short_comum.py` (2026-08-04): as 54 entradas do `APELO_EUA`
sao copy validada, e redigitar copy validada e' o erro que o repo ja' pagou (o
D1 comprimido na mao virou esqueleto 3D). O recorte e' REGULAR, entao ele sai
por substituicao verificada.

⛔⛔ AS LAPIDES FICAM. O repo guarda a explicacao de cada regra removida de
proposito — *regra que some sem explicacao volta no proximo agente nascido por
copia, e foi exatamente assim que a clausula chegou aqui*. Por isso a ferramenta
so' toca em STRING VIVA:

  · COMENTARIO  -> intocavel (é a memoria que impede a reincidencia)
  · DOCSTRING   -> intocavel
  · argumento de `re.compile(...)` -> intocavel (e' o DETECTOR, nao o defeito)
  · constante de nome de lente (`*_CONFORMIDADE`, `_CELEB*`, `_APROVACAO*`,
    `_PROIB*`, `_NEG*`, `_TEM_*`) -> intocavel
  · corpo de funcao `autoteste*` -> intocavel (sao os controles da lente)

⚠️ E o glob NAO e' `*_short.py`: `clean_short_v2.py` tem sufixo `_v2.py` e um
glob ingenuo perde o motor inteiro em silencio (4 ocorrencias vivas, 100% dos
videos). Aqui varre-se `*.py`.

O recorte e a lente moram no `short_comum.py` (`tirar_anticeleb` /
`lint_anticeleb`) — uma regra, um lugar. Esta ferramenta so' os aplica ao fonte.
"""
import argparse
import ast
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, RAIZ)

import short_comum as sc  # noqa: E402  (o recorte mora la')

# ⛔ nomes de constante que sao MATERIAL DE LENTE — apagar a negacao ali remove
# o detector, nao o defeito.
_LENTE = re.compile(r"CONFORMIDADE|_CELEB|_APROVACAO|_PROIB|_BANIDO|_VETO"
                    r"|_NEG|_TEM_|_MENDIGO|_DENTE|_RX$")

# ⛔ arquivos que a ferramenta nunca reescreve: ela propria (as strings deste
# cabecalho e dos controles) e os relatorios/medidores do scratchpad.
_FORA = ("tirar_anticeleb.py",)

# a lapide — CURTA e com PONTEIRO. ⚠️ Repetir o paragrafo da doutrina em 46
# arquivos cria 46 copias que envelhecem sozinhas.
LAPIDE = ("# ⛔ A negacao anti-celebridade saiu daqui em 2026-08-14, por "
          "ordem do operador\n"
          "# (*\"tire not a celebrity do prompt\"*): declaracao INJETA o token "
          "que ela nega.\n"
          "# A metade positiva ficou. Ver CLAUDE.md §\"CONTRA A "
          "CELEBRIDADE, SILENCIO\".\n")


# ---------------------------------------------------------------------------
# 1. QUEM ESTA' VIVO
# ---------------------------------------------------------------------------

def _linhas_intocaveis(arvore):
    """Linhas de docstring, de `re.compile(...)` e de constante de lente."""
    fora = set()
    for no in ast.walk(arvore):
        if isinstance(no, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef,
                           ast.ClassDef)):
            corpo = getattr(no, "body", [])
            if (corpo and isinstance(corpo[0], ast.Expr)
                    and isinstance(corpo[0].value, ast.Constant)
                    and isinstance(corpo[0].value.value, str)):
                d = corpo[0].value
                fora.update(range(d.lineno, getattr(d, "end_lineno", d.lineno) + 1))
        if (isinstance(no, ast.Call) and isinstance(no.func, ast.Attribute)
                and no.func.attr == "compile"):
            fora.update(range(no.lineno, getattr(no, "end_lineno", no.lineno) + 1))
        if isinstance(no, ast.Assign):
            nomes = [t.id for t in no.targets if isinstance(t, ast.Name)]
            if any(_LENTE.search(n) for n in nomes):
                fora.update(range(no.lineno,
                                  getattr(no, "end_lineno", no.lineno) + 1))
        # ⛔ os controles da lente citam a clausula de proposito: sao o que
        # prova que o recorte funciona. Comer os proprios testes seria a lente
        # que imprime OK sobre o nada.
        if isinstance(no, (ast.FunctionDef, ast.AsyncFunctionDef)) \
                and no.name.startswith("autoteste"):
            fora.update(range(no.lineno, getattr(no, "end_lineno", no.lineno) + 1))
    return fora


def _dono(arvore):
    """linha -> nome da constante atribuida, para o relatorio e a lapide."""
    dono = {}
    for no in ast.walk(arvore):
        if isinstance(no, (ast.Assign, ast.AnnAssign)):
            alvos = no.targets if isinstance(no, ast.Assign) else [no.target]
            try:
                nome = (alvos[0].id if isinstance(alvos[0], ast.Name)
                        else ast.unparse(alvos[0]))
            except Exception:
                nome = "?"
            for ln in range(no.lineno, getattr(no, "end_lineno", no.lineno) + 1):
                dono.setdefault(ln, (nome, no.lineno, no.col_offset))
    return dono


# ---------------------------------------------------------------------------
# 2. EMISSAO — o literal de volta ao fonte
# ---------------------------------------------------------------------------

def _emitir(texto, col, uma_linha, largura=79):
    """O texto como literal Python, quebrado na largura do arquivo.

    ⛔ `uma_linha` e' obrigatorio quando o literal original cabia numa linha so':
    ali ele pode estar FORA de parenteses, e concatenacao implicita em duas
    linhas sem parenteses e' SyntaxError. Como o recorte so' ENCURTA, nunca
    precisamos quebrar o que nao estava quebrado.
    """
    esc = texto.replace("\\", "\\\\").replace('"', '\\"')
    if uma_linha or not esc:
        return ['"%s"' % esc]
    teto = max(24, largura - col - 2)
    pedacos = re.findall(r"\S+[ \t]*|[ \t]+", esc) or [esc]
    segs, atual = [], ""
    for p in pedacos:
        if atual and len(atual) + len(p) > teto:
            segs.append(atual)
            atual = p
        else:
            atual += p
    if atual or not segs:
        segs.append(atual)
    return ['"%s"' % s for s in segs]


def _fatiar(linha, ini, fim=None):
    """Corte por BYTE UTF-8 — `col_offset` do ast e' byte, nao caractere."""
    b = linha.encode("utf-8")
    return (b[ini:fim] if fim is not None else b[ini:]).decode("utf-8")


# ---------------------------------------------------------------------------
# 3. O PASSE
# ---------------------------------------------------------------------------

def _stmts(arvore):
    """Os statements em ordem de documento.

    ⛔ O INDICE E' A CHAVE, e ele e' estavel porque o recorte NUNCA acrescenta
    nem remove statement — so' encurta literais. ⚠️ A primeira versao desta
    ferramenta casava a lapide pelo VALOR da string e enfiou 161 comentarios em
    lugar errado: a entrada do FALTA vira `""`, e `""` casa com TODA string
    vazia do arquivo. Chave por conteudo em arquivo grande sempre encontra
    homonimo; chave por posicao, nao.
    """
    fora = [n for n in ast.walk(arvore) if isinstance(n, ast.stmt)]
    fora.sort(key=lambda n: (n.lineno, n.col_offset))
    return fora


def _pais(arvore):
    pai = {}
    for no in ast.walk(arvore):
        for filho in ast.iter_child_nodes(no):
            pai[filho] = no
    return pai


def _stmt_do_no(no, pai):
    x = no
    while x is not None and not isinstance(x, ast.stmt):
        x = pai.get(x)
    return x


def _comentarios(fonte):
    """Linhas que sao SO' comentario — nada mais na linha."""
    fora = set()
    for i, l in enumerate(fonte.split("\n"), 1):
        if l.lstrip().startswith("#"):
            fora.add(i)
    return fora


def _achar_alvos(fonte):
    """(arvore, [(no, texto_novo)], [recusas]) — so' as STRINGS VIVAS que mudam.

    ⛔⛔ RECUSA O NO QUE TEM COMENTARIO NO MEIO. A reescrita substitui o VAO
    INTEIRO do literal, e um comentario entre dois pedacos de concatenacao
    implicita mora dentro desse vao — ele sairia junto, em silencio. Aconteceu
    de verdade no VAZAMENTO: o bloco `IMAGE 04/05` carrega, entre dois pedacos,
    a lapide da falha de continuidade de 2026-07-31 (o Veo trocou o corpo-prova
    por um senhor de oculos), e a primeira passada a apagou. Comentario que some
    e' memoria que some — e o repo guarda lapide exatamente para isso.
    ⭐ Recusar e reportar e' melhor que reescrever certo por acidente: o
    operador conserta os poucos casos a mao, sabendo quais sao.
    """
    arvore = ast.parse(fonte)
    intocaveis = _linhas_intocaveis(arvore)
    coment = _comentarios(fonte)
    alvos, recusas = [], []
    for no in ast.walk(arvore):
        if not (isinstance(no, ast.Constant) and isinstance(no.value, str)):
            continue
        if no.lineno in intocaveis:
            continue
        novo = sc.tirar_anticeleb(no.value)
        if novo == no.value:
            continue
        vao = set(range(no.lineno, getattr(no, "end_lineno", no.lineno) + 1))
        if vao & coment:
            recusas.append((no.lineno, sorted(vao & coment)))
            continue
        alvos.append((no, novo))
    return arvore, alvos, recusas


def _indices_com_lapide(fonte):
    """Indices de statement (ordem de documento) que perderam a clausula."""
    arvore, alvos, _ = _achar_alvos(fonte)
    if not alvos:
        return []
    pai = _pais(arvore)
    ordem = {id(s): i for i, s in enumerate(_stmts(arvore))}
    saida = set()
    for no, _ in alvos:
        s = _stmt_do_no(no, pai)
        if s is not None and id(s) in ordem:
            saida.add(ordem[id(s)])
    return sorted(saida)


def _por_lapide(fonte, indices):
    """Insere a lapide acima dos statements de indice `indices`."""
    arvore = ast.parse(fonte)
    stmts = _stmts(arvore)
    linhas = fonte.split("\n")
    for i in sorted(indices, reverse=True):
        if i >= len(stmts):
            continue
        s = stmts[i]
        ln, col = s.lineno, s.col_offset
        # ⛔ o `col_offset` e' BYTE; a lapide entra com o recuo do statement
        recuo = " " * len(_fatiar(linhas[ln - 1], 0, col))
        if LAPIDE.split("\n")[0] in "\n".join(linhas[max(0, ln - 4):ln]):
            continue                      # ja' tem lapide: nao empilha outra
        linhas[ln - 1:ln - 1] = [recuo + l
                                 for l in LAPIDE.rstrip("\n").split("\n")]
    return "\n".join(linhas)


def processar(caminho):
    """Devolve (fonte_novo, [(linha, const, antes, depois)])."""
    with io.open(caminho, encoding="utf-8") as fh:
        fonte = fh.read()
    try:
        arvore, alvos, recusas = _achar_alvos(fonte)
    except SyntaxError:
        return None, [], []
    if not alvos:
        return None, [], recusas

    dono = _dono(arvore)
    indices = _indices_com_lapide(fonte)

    linhas = fonte.split("\n")
    trocas = []
    # de tras para frente: assim os offsets dos nos ainda nao tocados valem
    for no, novo in sorted(alvos, key=lambda x: (x[0].lineno, x[0].col_offset),
                           reverse=True):
        l0, l1 = no.lineno - 1, no.end_lineno - 1
        prefixo = _fatiar(linhas[l0], 0, no.col_offset)
        sufixo = _fatiar(linhas[l1], no.end_col_offset)
        segs = _emitir(novo, len(prefixo), uma_linha=(l0 == l1))
        recuo = " " * len(prefixo)
        novas = [prefixo + segs[0]] + [recuo + s for s in segs[1:]]
        novas[-1] += sufixo
        linhas[l0:l1 + 1] = novas
        nome = dono.get(no.lineno, ("<inline>", no.lineno, 0))
        trocas.append((no.lineno, nome[0], no.value, novo))

    fonte_novo = "\n".join(linhas)
    ast.parse(fonte_novo)          # ⛔ so' devolve o que ainda compila
    fonte_novo = _por_lapide(fonte_novo, indices)
    ast.parse(fonte_novo)
    return fonte_novo, trocas, recusas


def lapidar_do_head(caminho):
    """Poe a lapide num arquivo JA' RECORTADO, lendo o HEAD para saber onde.

    ⚠️ Existe porque o recorte foi aplicado antes de a lapide estar certa. O
    HEAD e' a unica fonte de verdade de onde a clausula morava, e o indice de
    statement e' estavel entre as duas versoes. Se o numero de statements nao
    bater (arquivo editado a mao no meio), ela RECUSA em vez de chutar.
    """
    import subprocess
    rel = "funil-organico/" + os.path.basename(caminho)
    try:
        velho = subprocess.check_output(["git", "show", "HEAD:" + rel],
                                        cwd=os.path.dirname(RAIZ))
        velho = velho.decode("utf-8")
    except Exception as e:
        return None, "sem HEAD (%s)" % type(e).__name__
    indices = _indices_com_lapide(velho)
    if not indices:
        return None, None
    atual = io.open(caminho, encoding="utf-8").read()
    n_v, n_a = len(_stmts(ast.parse(velho))), len(_stmts(ast.parse(atual)))
    if n_v != n_a:
        return None, ("statements %d no HEAD contra %d agora — recusa, o "
                      "indice deixou de ser comparavel" % (n_v, n_a))
    return _por_lapide(atual, indices), None


# ---------------------------------------------------------------------------
# 4. CLI
# ---------------------------------------------------------------------------

def alvos_do_repo():
    fora_dir = ("agentes-de-terceiros",)
    saida = []
    for nome in sorted(os.listdir(RAIZ)):
        if not nome.endswith(".py") or nome in _FORA:
            continue
        if "lucas" in nome.lower():
            continue
        if any(d in RAIZ.lower() for d in fora_dir):
            continue
        saida.append(os.path.join(RAIZ, nome))
    return saida


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--aplicar", action="store_true",
                    help="grava (sem isto, so' mostra)")
    ap.add_argument("--dry-run", action="store_true", help="o padrao")
    ap.add_argument("--autoteste", action="store_true")
    ap.add_argument("--lapide", action="store_true",
                    help="so' a lapide, em arquivo ja' recortado (le o HEAD)")
    ap.add_argument("--curto", action="store_true",
                    help="so' o resumo, sem o antes/depois de cada string")
    a = ap.parse_args()

    falhas = sc.autoteste_anticeleb()
    if falhas:
        print("AUTOTESTE DO RECORTE REPROVADO (%d):" % len(falhas))
        for f in falhas:
            print("  - %s" % f)
        return 1
    print("autoteste do recorte: OK (controles positivos e negativos)")
    if a.autoteste:
        return 0

    if a.lapide:
        n = 0
        for caminho in alvos_do_repo():
            novo, motivo = lapidar_do_head(caminho)
            if motivo:
                print("  RECUSA %-30s %s" % (os.path.basename(caminho), motivo))
                continue
            if novo is None:
                continue
            n += 1
            print("  lapide %-30s" % os.path.basename(caminho))
            if a.aplicar:
                with io.open(caminho, "w", encoding="utf-8", newline="") as fh:
                    fh.write(novo)
        print("\n%s: %d arquivos lapidados"
              % ("APLICADO" if a.aplicar else "DRY-RUN", n))
        return 0

    n_arq = n_str = 0
    for caminho in alvos_do_repo():
        novo, trocas, recusas = processar(caminho)
        for ln, linhas_c in recusas:
            print("\n  RECUSA %s L%d: comentario DENTRO do literal "
                  "(linhas %s)"
                  % (os.path.basename(caminho), ln, linhas_c))
            print("         reescrever apagaria a lapide — conserto a mao")
        if not trocas:
            continue
        n_arq += 1
        n_str += len(trocas)
        print("\n=== %s  (%d strings)" % (os.path.basename(caminho), len(trocas)))
        if not a.curto:
            for ln, const, antes, depois in sorted(trocas):
                print("  L%-5d %s" % (ln, const))
                print("    - %s" % antes)
                print("    + %s" % (depois if depois else "<VAZIO>"))
        if a.aplicar:
            with io.open(caminho, "w", encoding="utf-8", newline="") as fh:
                fh.write(novo)
    print("\n%s: %d arquivos, %d strings"
          % ("APLICADO" if a.aplicar else "DRY-RUN", n_arq, n_str))
    return 0


if __name__ == "__main__":
    sys.exit(main())
