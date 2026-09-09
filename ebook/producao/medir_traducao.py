# -*- coding: utf-8 -*-
"""GATE DA ENTREGA TRADUZIDA — mede o PDF gerado contra o PT, não o código.
Uso: python medir_traducao.py [de|fr|todos]

⛔ Medidor de pool não mede função: o `lint_traducao.py` cobra os DADOS, este
cobra o PDF que o comprador abre. Roda depois de `build_tudo_tr.py`.
  1. Os 9 arquivos existem e abrem.
  2. Contagem de páginas contra o PT (crescer é permitido — a ordem do
     operador é "não espremer"; ENCOLHER é que seria suspeito).
  3. ⛔ Página ÓRFÃ: página com quase nada de texto é sobra de quebra e o PT
     tem ZERO delas. É o defeito que as duas línguas, sendo mais longas,
     introduzem — foi assim que apareceram as 4 do alemão.
  4. Português vazado no texto extraído do PDF.
"""
import importlib
import os
import re
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

import pypdfium2 as pdfium

AQUI = os.path.dirname(os.path.abspath(__file__))
PT = os.path.join(AQUI, "..", "Entregavel em PT")
LIMIAR_ORFA = 120     # chars
IDIOMAS = ("de", "fr", "en", "es")

PT_ARQUIVOS = [
 "Passo 1 - Comece Por Aqui.pdf",
 "Passo 2 - Cafés da Manhã.pdf",
 "Passo 3 - Almoços.pdf",
 "Passo 4 - Jantares.pdf",
 "Passo 5 - Sobremesas.pdf",
 "Passo 6 - Vitaminas, Sucos e Chás Detox.pdf",
 "Passo 7 - Bônus 1 - Dieta Vegetariana.pdf",
 "Passo 8 - Bônus 2 - Pilates Seca Barriga em Casa.pdf",
 "Passo 9 - Bônus 3 - 50 Hábitos e Exercícios.pdf",
]

TR_ARQUIVOS = {
 "de": ["Schritt 1 - Fang hier an.pdf",
        "Schritt 2 - Fruehstueck.pdf",
        "Schritt 3 - Mittagessen.pdf",
        "Schritt 4 - Abendessen.pdf",
        "Schritt 5 - Desserts.pdf",
        "Schritt 6 - Smoothies, Saefte und Detox-Tees.pdf",
        "Schritt 7 - Bonus 1 - Vegetarische Ernaehrung.pdf",
        "Schritt 8 - Bonus 2 - Pilates fuer einen flachen Bauch.pdf",
        "Schritt 9 - Bonus 3 - 50 Gewohnheiten und Uebungen.pdf"],
 "fr": ["Etape 1 - Commence ici.pdf",
        "Etape 2 - Petits-dejeuners.pdf",
        "Etape 3 - Dejeuners.pdf",
        "Etape 4 - Diners.pdf",
        "Etape 5 - Desserts.pdf",
        "Etape 6 - Smoothies, jus et thes detox.pdf",
        "Etape 7 - Bonus 1 - Alimentation vegetarienne.pdf",
        "Etape 8 - Bonus 2 - Pilates ventre plat.pdf",
        "Etape 9 - Bonus 3 - 50 habitudes et exercices.pdf"],
 "en": ["Step 1 - Start Here.pdf",
        "Step 2 - Breakfasts.pdf",
        "Step 3 - Lunches.pdf",
        "Step 4 - Dinners.pdf",
        "Step 5 - Desserts.pdf",
        "Step 6 - Smoothies, Juices and Detox Teas.pdf",
        "Step 7 - Bonus 1 - Vegetarian Diet.pdf",
        "Step 8 - Bonus 2 - Flat Belly Pilates at Home.pdf",
        "Step 9 - Bonus 3 - 50 Habits and Exercises.pdf"],
 "es": ["Paso 1 - Empieza aqui.pdf",
        "Paso 2 - Desayunos.pdf",
        "Paso 3 - Almuerzos.pdf",
        "Paso 4 - Cenas.pdf",
        "Paso 5 - Postres.pdf",
        "Paso 6 - Smoothies, jugos y tes detox.pdf",
        "Paso 7 - Bono 1 - Dieta Vegetariana.pdf",
        "Paso 8 - Bono 2 - Pilates para Abdomen Plano.pdf",
        "Paso 9 - Bono 3 - 50 Habitos y Ejercicios.pdf"],
}

PT_NO_PDF = ["Receita", "Porção", "Ingredientes", "Modo de preparo", "Mulheres",
             "Homens", "Preparo", "Rende", "colher", "xícara", "à vontade",
             "a gosto", "pitada", "punhado", "fatia", "emagrecer", "Passo",
             "Bônus", "Dica", "Nível", "Séries"]

# ⛔ EXCEÇÃO DECLARADA, no molde do `DESLIGADAS` do parque: um termo que a
# língua de destino usa DE VERDADE não pode ser acusado como português solto.
# O francês escreve "Séries" exatamente como o português — cobrar isso seria a
# lente reprovando copy certa, e lente que acusa o certo treina a ser ignorada.
# ⚠️ O espanhol escreve "Ingredientes" EXATAMENTE como o portugues — mesma
# situacao do "Séries" frances, e pela mesma razao: e' espanhol correto, nao
# portugues vazado. Sem a isencao a lente reprovaria as 150 receitas.
ISENTOS = {"fr": {"Séries"}, "de": set(), "en": set(),
           "es": {"Ingredientes"}}

_L = r"A-Za-zÀ-ÖØ-öø-ÿ0-9_"


def paginas(caminho):
    doc = pdfium.PdfDocument(caminho)
    return [doc[i].get_textpage().get_text_range() for i in range(len(doc))]


# ── AS DUAS PROVAS DO "MENOS PAGINAS" ──────────────────────────────────────
# ⛔ O modulo de dados por passo. O Passo 1 nao tem modulo (e' prosa gerada
# pelo build), entao ele nunca ganha perdao: fica no ERRO, como estava.
MODULO_DO_PASSO = {
    1: [("receitas_cafe", "RECEITAS")],
    2: [("receitas_almoco", "RECEITAS")],
    3: [("receitas_jantar", "RECEITAS")],
    4: [("receitas_sobremesa", "RECEITAS")],
    5: [("receitas_suco", "RECEITAS")],
    6: [("receitas_bonus_veg", "ALMOCOS"), ("receitas_bonus_veg", "JANTARES")],
    7: [("exercicios_pilates", "EXERCICIOS")],
    8: [("exercicios_habitos", "TEMAS")],
}

# ⛔ `prompt` nao e' renderizado (e' a instrucao da foto), e `img` e' numero.
NAO_RENDERIZA = {"prompt", "img"}


def _strings(no, saida):
    """Toda string que o modulo manda para a pagina, em qualquer profundidade
    — receita (dict), tema com `itens` aninhados, lista de passos."""
    if isinstance(no, list):
        for x in no:
            _strings(x, saida)
    elif isinstance(no, dict):
        for k, v in no.items():
            if k not in NAO_RENDERIZA:
                _strings(v, saida)
    elif isinstance(no, str) and no.strip():
        saida.append(no)


def _norm(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s)).strip().lower()


def _conteudo_faltando(lang, i_arq, texto_pdf):
    """Quantos trechos do modulo NAO aparecem no PDF. Zero = nada se perdeu."""
    alvos = []
    for base, attr in MODULO_DO_PASSO.get(i_arq, []):
        try:
            mod = importlib.import_module("%s_%s" % (base, lang))
        except ImportError:
            return 1, 0          # sem modulo nao ha' prova — segue ERRO
        _strings(getattr(mod, attr, []), alvos)
    if not alvos:
        return 1, 0
    plano = _norm(texto_pdf)
    # 40 chars bastam para identificar o trecho e sobram para o PDF quebrar
    faltando = sum(1 for a in alvos if _norm(a)[:40] and _norm(a)[:40] not in plano)
    return faltando, len(alvos)


def _mesmo_corpo(pdf_pt, pdf_tr, amostra=8):
    """A altura de glifo mais comum tem de bater. E' o que separa `a lingua e'
    mais curta` de `alguem diminuiu a fonte` — e diminuir fonte e' justamente
    o que a ordem do operador proibe."""
    def alturas(caminho):
        doc = pdfium.PdfDocument(caminho)
        conta = {}
        for i in range(min(len(doc), amostra)):
            tp = doc[i].get_textpage()
            for j in range(tp.count_chars()):
                cx = tp.get_charbox(j)
                h = round(cx[3] - cx[1], 1)
                if h > 0:
                    conta[h] = conta.get(h, 0) + 1
        return sorted(conta.items(), key=lambda x: -x[1])[:3]
    if not os.path.isfile(pdf_pt):
        return False
    a = [h for h, _ in alturas(pdf_pt)]
    b = [h for h, _ in alturas(pdf_tr)]
    return bool(a) and bool(b) and set(b) == set(a)


def medir(lang):
    erros = []
    observacoes = []
    isentos = ISENTOS.get(lang, set())
    termos = [t for t in PT_NO_PDF if t not in isentos]
    rx = [re.compile(r"(?<![" + _L + r"])" + re.escape(t) + r"(?![" + _L + r"])")
          for t in termos]
    DE = os.path.join(AQUI, "..", "Entregavel em %s" % lang.upper())

    print("%-52s %7s %7s  %s" % ("arquivo", "PT pg", "pg", "orfas"))
    tp = td = 0
    for i_arq, (p, d) in enumerate(zip(PT_ARQUIVOS, TR_ARQUIVOS[lang])):
        cp, cd = os.path.join(PT, p), os.path.join(DE, d)
        if not os.path.isfile(cd):
            erros.append("FALTA o arquivo: %s" % d)
            print("%-52s %7s %7s  %s" % (d[:52], "-", "AUSENTE", "-"))
            continue
        tx_pt = paginas(cp) if os.path.isfile(cp) else []
        tx = paginas(cd)
        tp += len(tx_pt)
        td += len(tx)

        orfas = [i + 1 for i, t in enumerate(tx) if len(t.strip()) < LIMIAR_ORFA]
        if orfas:
            erros.append("%s: %d pagina(s) orfa(s) -> %s" % (d, len(orfas), orfas))
        inteiro = "\n".join(tx)
        if tx_pt and len(tx) < len(tx_pt):
            # ⛔⛔ MENOS PAGINA E' SUSPEITA, NAO VEREDITO — e a lente agora tem
            # de PROVAR qual dos dois. "Espremido ou perdido" era um PROXY:
            # ele confunde `o idioma e' mais curto e a quebra caiu uma pagina
            # antes` com `sumiu receita`. Proxy que reprova o certo treina o
            # operador a ignorar o portao (a licao do `DESLIGADAS`) — e proxy
            # que passa o errado e' pior. Entao: se TODA string do modulo de
            # dados estiver no PDF e o corpo tiver a MESMA altura de glifo do
            # PT, esta provado que nada foi espremido nem perdido, e a linha
            # vira OBSERVACAO. Faltando UMA string, continua ERRO.
            falta, total = _conteudo_faltando(lang, i_arq, inteiro)
            corpo_ok = _mesmo_corpo(cp, cd)
            if falta or not corpo_ok or total == 0:
                erros.append(
                    "%s: tem MENOS paginas que o PT (%d < %d) e a prova NAO "
                    "fecha (%d de %d trechos ausentes, corpo igual ao PT: %s)"
                    % (d, len(tx), len(tx_pt), falta, total,
                       "sim" if corpo_ok else "NAO"))
            else:
                observacoes.append(
                    "%s: %d paginas contra %d do PT — PROVADO que nao ha' "
                    "perda: %d/%d trechos do modulo presentes no PDF e a "
                    "altura de glifo do corpo e' a mesma do PT. O idioma so' "
                    "e' mais curto e a quebra caiu antes."
                    % (d, len(tx), len(tx_pt), total, total))

        for termo, r in zip(termos, rx):
            if r.search(inteiro):
                erros.append("%s: portugues no PDF -> %r" % (d, termo))

        print("%-52s %7d %7d  %s" % (d[:52], len(tx_pt), len(tx),
                                     len(orfas) if orfas else "0"))
    print("%-52s %7d %7d" % ("TOTAL", tp, td))
    if isentos:
        print("  [isento] termo(s) que o idioma usa de verdade: %s"
              % ", ".join(sorted(isentos)))
    for o in observacoes:
        print("  [observacao] %s" % o)
    return erros


def main():
    alvo = sys.argv[1] if len(sys.argv) > 1 else "todos"
    langs = list(IDIOMAS) if alvo == "todos" else [alvo]
    todos = []
    for lang in langs:
        print("\n" + "=" * 22 + "  " + lang.upper() + "  " + "=" * 22)
        todos += medir(lang)
    print()
    if todos:
        for e in todos:
            print("  [ERRO] " + e)
        print("\nREPROVADO: %d problema(s)." % len(todos))
        return 1
    print("APROVADO: 9 arquivos por idioma, 0 pagina orfa, 0 portugues vazado.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
