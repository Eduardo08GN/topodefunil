# -*- coding: utf-8 -*-
"""Gera os NOVE PDFs de um idioma em "Entregavel em <LANG>/", na ordem dos passos.
Uso: python build_tudo_tr.py [de|fr|todos]

⛔ Cada build sobe o próprio servidor HTTP na porta 8132; rodar todos no MESMO
processo colide na porta. Por isso cada um roda como SUBPROCESSO, em série.
"""
import os
import subprocess
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

AQUI = os.path.dirname(os.path.abspath(__file__))
IDIOMAS = ("de", "fr")


def passos(lang):
    py = sys.executable
    return [("passo 1", [py, "build_frente_tr.py", lang]),
            ("passo 2", [py, "build_ebook_tr.py", lang, "cafe"]),
            ("passo 3", [py, "build_ebook_tr.py", lang, "almoco"]),
            ("passo 4", [py, "build_ebook_tr.py", lang, "jantar"]),
            ("passo 5", [py, "build_ebook_tr.py", lang, "sobremesa"]),
            ("passo 6", [py, "build_ebook_tr.py", lang, "suco"]),
            ("passo 7", [py, "build_bonus_veg_tr.py", lang]),
            ("passo 8", [py, "build_bonus_pilates_tr.py", lang]),
            ("passo 9", [py, "build_bonus3_tr.py", lang])]


def um_idioma(lang):
    falhas = []
    for rotulo, cmd in passos(lang):
        r = subprocess.run(cmd, cwd=AQUI, capture_output=True, text=True,
                           encoding="utf-8", errors="replace")
        saida = (r.stdout or "") + (r.stderr or "")
        linha = [l for l in saida.splitlines() if l.startswith("PDF:")]
        print("  %-8s %s" % (rotulo, linha[-1] if linha else "(sem saida PDF)"))
        if r.returncode != 0 or "FALHOU" in saida:
            falhas.append(rotulo)
            for l in saida.strip().splitlines()[-12:]:
                print("      " + l)

    saida_dir = os.path.join(AQUI, "Entregavel em %s" % lang.upper())
    if os.path.isdir(saida_dir):
        pdfs = sorted(f for f in os.listdir(saida_dir) if f.lower().endswith(".pdf"))
        total = sum(os.path.getsize(os.path.join(saida_dir, f)) for f in pdfs) / 1e6
        print("  -> %d arquivos, %.1f MB" % (len(pdfs), total))
    return falhas


def main():
    alvo = sys.argv[1] if len(sys.argv) > 1 else "todos"
    langs = list(IDIOMAS) if alvo == "todos" else [alvo]
    todas = {}
    for lang in langs:
        print("\n" + "=" * 22 + "  " + lang.upper() + "  " + "=" * 22)
        todas[lang] = um_idioma(lang)
    print("\n" + "=" * 60)
    ruim = {k: v for k, v in todas.items() if v}
    print("FALHAS:", ruim if ruim else "nenhuma")
    return 1 if ruim else 0


if __name__ == "__main__":
    sys.exit(main())
