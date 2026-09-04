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
IDIOMAS = ("de", "fr", "en")

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
}

PT_NO_PDF = ["Receita", "Porção", "Ingredientes", "Modo de preparo", "Mulheres",
             "Homens", "Preparo", "Rende", "colher", "xícara", "à vontade",
             "a gosto", "pitada", "punhado", "fatia", "emagrecer", "Passo",
             "Bônus", "Dica", "Nível", "Séries"]

# ⛔ EXCEÇÃO DECLARADA, no molde do `DESLIGADAS` do parque: um termo que a
# língua de destino usa DE VERDADE não pode ser acusado como português solto.
# O francês escreve "Séries" exatamente como o português — cobrar isso seria a
# lente reprovando copy certa, e lente que acusa o certo treina a ser ignorada.
ISENTOS = {"fr": {"Séries"}, "de": set(), "en": set()}

_L = r"A-Za-zÀ-ÖØ-öø-ÿ0-9_"


def paginas(caminho):
    doc = pdfium.PdfDocument(caminho)
    return [doc[i].get_textpage().get_text_range() for i in range(len(doc))]


def medir(lang):
    erros = []
    isentos = ISENTOS.get(lang, set())
    termos = [t for t in PT_NO_PDF if t not in isentos]
    rx = [re.compile(r"(?<![" + _L + r"])" + re.escape(t) + r"(?![" + _L + r"])")
          for t in termos]
    DE = os.path.join(AQUI, "Entregavel em %s" % lang.upper())

    print("%-52s %7s %7s  %s" % ("arquivo", "PT pg", "pg", "orfas"))
    tp = td = 0
    for p, d in zip(PT_ARQUIVOS, TR_ARQUIVOS[lang]):
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
        if tx_pt and len(tx) < len(tx_pt):
            erros.append("%s: tem MENOS paginas que o PT (%d < %d) — sinal de "
                         "conteudo espremido ou perdido" % (d, len(tx), len(tx_pt)))

        inteiro = "\n".join(tx)
        for termo, r in zip(termos, rx):
            if r.search(inteiro):
                erros.append("%s: portugues no PDF -> %r" % (d, termo))

        print("%-52s %7d %7d  %s" % (d[:52], len(tx_pt), len(tx),
                                     len(orfas) if orfas else "0"))
    print("%-52s %7d %7d" % ("TOTAL", tp, td))
    if isentos:
        print("  [isento] termo(s) que o idioma usa de verdade: %s"
              % ", ".join(sorted(isentos)))
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
