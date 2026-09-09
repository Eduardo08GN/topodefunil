# -*- coding: utf-8 -*-
"""LENTE DAS TRADUÇÕES — cobra o que o olho não vê num arquivo de 700 linhas.

Uso:  python lint_traducao.py               (todos os idiomas traduzidos)
      python lint_traducao.py de            (só o alemão)
      python lint_traducao.py fr receitas_cafe_fr

⛔ UMA lente para TODOS os idiomas, nunca uma cópia por idioma: `lint_de.py` +
`lint_fr.py` seriam dois arquivos que divergem no primeiro conserto, e o
conserto chegaria a um idioma só. Idioma novo entra em `IDIOMAS`, não em
arquivo novo.

⛔ Aceite é MEDIÇÃO, nunca relato. O que ela cobra:
  1. PARIDADE com o PT — mesma contagem de receitas, e por receita a mesma
     contagem de ingredientes, passos e porcoes8. Receita perdida no meio de
     700 linhas não aparece lendo.
  2. VAZAMENTO de português — palavras que só existem em PT.
  3. MEDIDA não convertida — `xícara`, `colher de`, `col.` são erro por
     construção: nem a Alemanha nem a França têm xícara.
  4. CAMPO faltando ou vazio, e a flag `livre` divergindo.
  5. TETO de caractere na `porcoes8` — a coluna é a mais estreita e as duas
     línguas são mais longas que o português. Acusa, não corta.
"""
import importlib
import re
import sys

# o console do Windows nasce cp1252 e derruba acento/emoji na saida
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

IDIOMAS = ("de", "fr", "en", "es", "it")

# modulos de RECEITA: (pt, sufixo) -> o nome do modulo traduzido e' pt + "_" + lang
MODULOS = ["receitas_cafe", "receitas_almoco", "receitas_jantar",
           "receitas_sobremesa", "receitas_suco", "receitas_bonus_veg"]
# modulos de EXERCICIO: (pt, atributo da arvore)
MODULOS_EX = [("exercicios_pilates", "EXERCICIOS"),
              ("exercicios_habitos", "TEMAS")]

# palavras que denunciam copia esquecida do PT. ⛔ A lista e' de PORTUGUES, e
# por isso vale igual para os dois idiomas — nenhuma delas existe em alemao
# nem em frances (`porção`≠`portion`, `receita`≠`recette`, `fatia`≠`tranche`).
PT_SOLTO = [
    "colher", "xícara", "xicara", "col.", "à vontade", "a gosto", "pitada",
    "punhado", "fatia", "fatias", "copo", "receita", "porção", "porcao",
    "misture", "coloque", "aqueça", "aqueca", "deixe", "sirva", "junte",
    "leve ao fogo", "frigideira", "geladeira", "liquidificador", "tigela",
    "azeite", "ovos", "leite", "açúcar", "acucar", "farinha", "manteiga",
    "emagrecer", "saciedade", "gordura", "proteína", "proteina", "fibra",
    "você", "voce", "com que", "não", "nao ", "então", "entao",
]
# ⛔ FRONTEIRA DE PALAVRA, nunca substring: `gleiten` contem "leite" e
# `Preise` contem "reis". Substring acusou copy alema CERTA na primeira
# rodada, e lente que acusa o certo treina o operador a ignorar a lente.
# A classe cobre trema alemao E acento frances — senao `pincée` quebraria.
_L = r"A-Za-zÀ-ÖØ-öø-ÿ0-9_"
_PT_RX = [re.compile(r"(?<![" + _L + r"])" + re.escape(p) + r"(?![" + _L + r"])", re.I)
          for p in PT_SOLTO]

# ⛔⛔ EXCECAO DECLARADA POR IDIOMA, no molde do `ISENTOS` do medir_traducao.py
# (que ja' isenta "Séries" no frances e "Ingredientes" no espanhol).
# Um termo que a lingua de destino escreve EXATAMENTE como o portugues nao e'
# portugues vazado — e' a palavra certa. Sem isto o espanhol leva 35 ERRO nos
# cafes por escrever "proteína" e "fibra", que e' como se escreve em espanhol.
# ⚠️ Todo o resto da PT_SOLTO diverge de verdade no espanhol e SEGUE COBRADO:
# colher->cuchara · xícara->taza · gordura->grasa · geladeira->refrigerador ·
# frigideira->sartén · tigela->tazón · emagrecer->adelgazar · você->tú.
ISENTOS = {
    "es": {"proteína", "proteina", "fibra"},
    # ⚠️ O italiano escreve `proteina` e `fibra` exatamente assim. ⛔ Mas
    # `proteína` COM acento fica COBRADO: o italiano nao tem `í`, logo ali
    # seria portugues vazado de verdade. Isencao e' bisturi, nunca atacado.
    "it": {"proteina", "fibra"},
    "de": set(), "fr": set(), "en": set(),
}


def _isentos_de(tr_nome):
    """O idioma e' o sufixo do modulo traduzido (receitas_cafe_es -> es)."""
    return ISENTOS.get(tr_nome.rsplit("_", 1)[-1], frozenset())

# medidas que TEM de ter sumido
MEDIDA_ERRADA = re.compile(r"x[íi]cara|colher(es)? de|\bcol\.\s*(sopa|chá|cha)", re.I)

# ⛔⛔ A LENTE QUE FALTAVA. A `MEDIDA_ERRADA` acima so' pega sobra de
# PORTUGUES; sobra de IMPERIAL INGLES nunca teve lente nenhuma — e o §6 do
# glossario diz que o EN e' a UNICA versao imperial do produto, logo todo
# idioma novo nasce tendo de converter. O buraco apareceu no controle
# negativo do `exercicios_habitos_es`, justo o modulo onde o EN e' imperial
# de verdade (`3 miles`, `2 quarts`): eu converti na mao e NINGUEM estava
# olhando. Traducao conferida a olho e' relato, nao medicao.
#
# ⚠️ `foot|feet` fica FORA de proposito: em `knees in line with your feet`
# sao os pes do corpo, nao a unidade (o DE confirma, `Füße`). Palavra que
# gera falso positivo em texto legitimo treina o operador a ignorar a lente.
IMPERIAL_VAZADO = re.compile(
    r"\b\d[\d.,/ ]*\s*(miles?|inch(es)?|pounds?|lbs?|ounces?|oz|"
    r"quarts?|gallons?|cups?|tbsps?|tsps?|tablespoons?|teaspoons?)\b", re.I)


def _lang_de(tr_nome):
    return tr_nome.rsplit("_", 1)[-1]


_NUM_RX = re.compile(r"\d+(?:[.,]\d+)?")

# ⛔ EXCECAO DECLARADA E MEDIDA: a linha do PT que traz XICARA (ou a fracao
# que so' existe em xicara: ⅓ ⅔ ¾ ½ de xic.) tem de mudar de numero na
# traducao — e' a §1 do glossario, "A XICARA VIRA PESO", 68 ocorrencias.
# Sem esta isencao a lente acusa 48 linhas CERTAS, identicas em de/fr/es, e
# afoga as 3 erradas do espanhol no meio delas. Medido: com a isencao,
# de=0, fr=0, es=3, e as 3 do es sao defeito de verdade.
_XICARA = re.compile(r"x[íi]c|[½⅓⅔¾⅛⅜⅝⅞]")


def _numeros(s):
    """Os numeros de uma linha de porcao, para comparar com o PT.

    ⛔⛔ TODO `1` E' DESCARTADO, em qualquer posicao. Ali ele quase nunca e'
    quantidade — e' artigo ou unidade indivisivel (`1 fio de azeite` ->
    `etwas Olivenöl`, `1 batata-doce média` -> `1 mittlere Süßkartoffel`,
    `1 punhado` -> `un puñado`). A primeira versao desta lente descartava so'
    o `1` inicial e acusou CENTENAS de linhas certas em alemao: cada
    `· 1 fio de azeite` que virou `· etwas Olivenöl` contava como numero
    perdido. Lente que acusa o certo treina o operador a ignorar a lente.

    O que sobra — 4, 5, 150, 220 — e' a escada de quantidade de verdade, e
    essa NAO pode mudar entre idiomas metricos.
    """
    return [n for n in _NUM_RX.findall(s) if n != "1"]

CAMPOS = ["nome", "hook", "tempo", "rende", "kcal_base", "ings", "passos",
          "porcoes8", "dica"]
TETO_PORCAO = 78   # acusa; a decisao de encurtar e' do operador

# ⛔ `prompt` fica FORA da comparacao: ele nao e' replicado nas traducoes de
# proposito (a foto e' a mesma e prompt duplicado e' prompt que diverge).
IGNORA = {"prompt"}


def _trecho(texto, pos, raio=28):
    """O contexto ao redor do achado — sem ele, 'leite' num arquivo de 700
    linhas custa uma busca manual para descobrir que era `gleiten`."""
    a = max(0, pos - raio)
    return ("…" if a else "") + texto[a:pos + raio].replace("\n", " ") + "…"


def _lista(mod):
    """O bonus vegetariano nao usa RECEITAS: ele separa ALMOCOS e JANTARES,
    porque as metas de caloria do motor mudam entre os dois."""
    if hasattr(mod, "RECEITAS"):
        return list(mod.RECEITAS)
    return list(getattr(mod, "ALMOCOS", [])) + list(getattr(mod, "JANTARES", []))


def checar(pt_nome, tr_nome):
    erros, avisos = [], []
    try:
        tr = importlib.import_module(tr_nome)
    except ImportError:
        return None, None
    pt = importlib.import_module(pt_nome)
    L_pt, L_tr = _lista(pt), _lista(tr)

    if len(L_pt) != len(L_tr):
        erros.append("CONTAGEM: PT tem %d receitas, traducao tem %d"
                     % (len(L_pt), len(L_tr)))
        return erros, avisos

    for i, (a, b) in enumerate(zip(L_pt, L_tr), 1):
        ref = "#%02d %s" % (i, b.get("nome", "<sem nome>")[:38])

        # ⛔ A exigencia e' PARIDADE com o PT, nunca uma lista absoluta: as 10
        # bebidas `livre` (chas e aguas detox) NAO tem `porcoes8` no PT, e
        # cobrar o campo delas seria a lente inventando um defeito.
        for c in CAMPOS:
            if c not in a:
                continue
            if c not in b:
                erros.append("%s: campo faltando '%s'" % (ref, c))
            elif isinstance(b[c], str) and not b[c].strip():
                erros.append("%s: campo vazio '%s'" % (ref, c))

        # e o proprio `livre` tem de casar: bebida que perde a flag na traducao
        # ganha uma tabela de porcao que o PT nao tem, e vice-versa.
        if bool(a.get("livre")) != bool(b.get("livre")):
            erros.append("%s: flag 'livre' diverge (PT=%s, traducao=%s)"
                         % (ref, bool(a.get("livre")), bool(b.get("livre"))))

        for c in ("ings", "passos", "porcoes8"):
            if c in a and c in b and len(a[c]) != len(b[c]):
                erros.append("%s: '%s' tem %d no PT e %d na traducao"
                             % (ref, c, len(a[c]), len(b[c])))

        if "porcoes8" in b and not b.get("livre") and len(b["porcoes8"]) != 8:
            erros.append("%s: porcoes8 tem %d entradas, tem de ser 8"
                         % (ref, len(b["porcoes8"])))

        if a.get("kcal_base") != b.get("kcal_base"):
            erros.append("%s: kcal_base mudou (%s -> %s) — numero nao se traduz"
                         % (ref, a.get("kcal_base"), b.get("kcal_base")))

        # ⛔⛔ A ESCADA DE QUANTIDADE TEM DE SER A MESMA DO PT.
        # O `kcal_base` ja' era cobrado; a `porcoes8` e a `ings` NAO eram, e
        # sao onde o numero de verdade mora. A lente de forma acima confere
        # QUANTAS linhas ha', nunca O QUE ha' dentro — e foi assim que duas
        # linhas do espanhol sairam com `5` onde o pt/de/fr/en dizem `4`.
        # Numero nao se traduz: mudar um e' inventar, e a ordem do operador e'
        # "nao invente nada".
        # ⛔ So' vale entre idiomas METRICOS. O EN e' imperial por decisao
        # (§6) e ali o numero MUDA de proposito — cobrar seria acusar o certo.
        # ⛔ So' a `porcoes8`. A `ings` fica de fora porque ali a conversao
        # MUDA o numero por doutrina: `1 xícara de vagem` vira `110 g` (§1),
        # e cobrar isso seria acusar exatamente o que a traducao deve fazer.
        # Na `porcoes8` a escada ja' nasce em unidade final nos dois lados.
        if _lang_de(tr_nome) != "en":
            for j, (x, y) in enumerate(zip(a.get("porcoes8", []),
                                           b.get("porcoes8", []))):
                if _XICARA.search(x):
                    continue          # §1: aqui o numero MUDA por doutrina
                if _numeros(x) != _numeros(y):
                    erros.append(
                        "%s: porcoes8[%d] mudou de numero -> PT %r x traducao %r"
                        % (ref, j, x, y))

        texto = " ".join(
            [str(b.get(c, "")) for c in ("nome", "hook", "tempo", "rende", "dica")]
            + list(b.get("ings", [])) + list(b.get("passos", []))
            + list(b.get("porcoes8", [])))
        isentos = _isentos_de(tr_nome)
        for p, rx in zip(PT_SOLTO, _PT_RX):
            if p in isentos:
                continue
            m = rx.search(texto)
            if m:
                erros.append("%s: portugues solto -> %r (em %r)"
                             % (ref, p, _trecho(texto, m.start())))
        m = MEDIDA_ERRADA.search(texto)
        if m:
            erros.append("%s: medida nao convertida -> %r" % (ref, m.group(0)))
        if _lang_de(tr_nome) != "en":
            m = IMPERIAL_VAZADO.search(texto)
            if m:
                erros.append("%s: imperial ingles vazado -> %r"
                             % (ref, m.group(0)))

        for j, p in enumerate(b.get("porcoes8", [])):
            if len(p) > TETO_PORCAO:
                avisos.append("%s: porcoes8[%d] com %d chars (teto %d) -> %r"
                              % (ref, j, len(p), TETO_PORCAO, p[:60]))
    return erros, avisos


# ── modulos de EXERCICIO ────────────────────────────────────────────────
# Pilates e o Bonus 3 nao sao receitas: um e' EXERCICIOS (lista de dicts), o
# outro e' TEMAS (dicts com `itens` aninhados). Em vez de escrever uma lente
# por formato, esta compara as DUAS ARVORES: mesma forma, mesmas chaves, mesmo
# numero de itens — e varre todo texto do lado traduzido atras de PT solto.
def _forma(no, caminho, erros):
    a, b = no
    if isinstance(a, list):
        if not isinstance(b, list) or len(a) != len(b):
            erros.append("%s: lista com %d no PT e %s na traducao"
                         % (caminho, len(a), len(b) if isinstance(b, list) else "outro tipo"))
            return
        for i, (x, y) in enumerate(zip(a, b)):
            _forma((x, y), "%s[%d]" % (caminho, i), erros)
    elif isinstance(a, dict):
        if not isinstance(b, dict):
            erros.append("%s: dict no PT e outro tipo na traducao" % caminho)
            return
        for k in a:
            if k in IGNORA:
                continue
            if k not in b:
                erros.append("%s: chave faltando '%s'" % (caminho, k))
            else:
                _forma((a[k], b[k]), "%s.%s" % (caminho, k), erros)
    elif isinstance(a, str):
        if not isinstance(b, str) or not b.strip():
            erros.append("%s: texto vazio ou de outro tipo na traducao" % caminho)
    elif a != b:
        erros.append("%s: valor mudou (%r -> %r) — numero nao se traduz"
                     % (caminho, a, b))


def _varrer_texto(no, caminho, erros, isentos=frozenset(),
                  imperial_ok=False):
    """⛔ `isentos` NAO tem default util: quem chama tem de dizer o idioma.
    A isencao existia so' no ramo das receitas, e este ramo (pilates/bonus 3)
    nao a recebia — `proteína` e' identica em pt e es e virava ERRO aqui e
    nao la'. Mesma familia do defeito §7(a): a regra certa num lugar so'.
    """
    if isinstance(no, list):
        for i, x in enumerate(no):
            _varrer_texto(x, "%s[%d]" % (caminho, i), erros, isentos,
                          imperial_ok)
    elif isinstance(no, dict):
        for k, v in no.items():
            if k not in IGNORA:
                _varrer_texto(v, "%s.%s" % (caminho, k), erros, isentos,
                              imperial_ok)
    elif isinstance(no, str):
        for p, rx in zip(PT_SOLTO, _PT_RX):
            if p in isentos:
                continue
            m = rx.search(no)
            if m:
                erros.append("%s: portugues solto -> %r (em %r)"
                             % (caminho, p, _trecho(no, m.start())))
        m = MEDIDA_ERRADA.search(no)
        if m:
            erros.append("%s: medida nao convertida -> %r" % (caminho, m.group(0)))
        if not imperial_ok:
            m = IMPERIAL_VAZADO.search(no)
            if m:
                erros.append("%s: imperial ingles vazado -> %r"
                             % (caminho, m.group(0)))


def checar_ex(pt_nome, tr_nome, attr):
    try:
        tr = importlib.import_module(tr_nome)
    except ImportError:
        return None, None
    pt = importlib.import_module(pt_nome)
    erros = []
    _forma((getattr(pt, attr), getattr(tr, attr)), attr, erros)
    if not erros:                      # so' varre texto se a forma bate
        _varrer_texto(getattr(tr, attr), attr, erros,
                      _isentos_de(tr_nome), _lang_de(tr_nome) == "en")
    return erros, []


def _casa(filtro, tr_nome, pt_nome):
    """⛔ Substring, nao igualdade: `cafe` tem de achar `receitas_cafe_en`.
    A versao por igualdade fazia `lint en cafe` pular TODOS os modulos e
    imprimir "0 erro" — filtro que nao casa nada aprovava tudo em silencio,
    e o silencio era identico ao do aprovado (licao §43).
    """
    return any(f in tr_nome or f in pt_nome for f in filtro)


def main():
    args = [a for a in sys.argv[1:]]
    langs = [a for a in args if a in IDIOMAS] or list(IDIOMAS)
    filtro = [a for a in args if a not in IDIOMAS]

    total_e = total_a = 0
    vistos = []
    for lang in langs:
        print("=" * 24 + "  " + lang.upper() + "  " + "=" * 24)
        alvos = ([(p, "%s_%s" % (p, lang)) for p in MODULOS],
                 [(p, "%s_%s" % (p, lang), attr) for p, attr in MODULOS_EX])

        for pt_nome, tr_nome in alvos[0]:
            if filtro and not _casa(filtro, tr_nome, pt_nome):
                continue
            vistos.append(tr_nome)
            r = checar(pt_nome, tr_nome)
            if r == (None, None):
                print("%-26s  [--] ainda nao traduzido" % tr_nome)
                continue
            erros, avisos = r
            total_e += len(erros)
            total_a += len(avisos)
            print("%-26s  %s%s" % (
                tr_nome, "0 ERRO" if not erros else "%d ERRO" % len(erros),
                "" if not avisos else "  · %d aviso" % len(avisos)))
            for e in erros:
                print("    [ERRO]  " + e)
            for a in avisos:
                print("    [aviso] " + a)

        for pt_nome, tr_nome, attr in alvos[1]:
            if filtro and not _casa(filtro, tr_nome, pt_nome):
                continue
            vistos.append(tr_nome)
            r = checar_ex(pt_nome, tr_nome, attr)
            if r == (None, None):
                print("%-26s  [--] ainda nao traduzido" % tr_nome)
                continue
            erros, _ = r
            total_e += len(erros)
            print("%-26s  %s" % (tr_nome, "0 ERRO" if not erros else "%d ERRO" % len(erros)))
            for e in erros:
                print("    [ERRO]  " + e)
        print()

    print("TOTAL: %d erro(s), %d aviso(s)" % (total_e, total_a))
    # ⛔ Filtro que nao casa modulo nenhum e' ERRO, nunca aprovacao.
    if filtro and not vistos:
        print("[ERRO]  o filtro %r nao casou NENHUM modulo — nada foi verificado." % filtro)
        return 1
    return 1 if total_e else 0


if __name__ == "__main__":
    sys.exit(main())
