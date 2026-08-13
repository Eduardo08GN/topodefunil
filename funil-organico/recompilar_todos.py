# -*- coding: utf-8 -*-
"""Recompila e entrega TODOS os .exe dos agentes.

⛔ O mapa motor -> pasta NAO e' adivinhado por nome: ele foi derivado lendo o
`.py` que ja' esta' dentro de cada pasta de entrega. Adivinhar por nome faz
`botica_short` cair na pasta do `botica16` — testado, e foi o que aconteceu na
primeira tentativa.

    python recompilar_todos.py            # todos
    python recompilar_todos.py good16     # so' os que casam com o filtro
"""
import glob
import json
import os
import shutil
import subprocess
import sys
import time

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = r"C:\Users\edlut\Desktop\agentes_py"
TMP = os.path.join(os.environ.get("TEMP", "."), "buildtodos")

# os arquivos que acompanham TODO agente na pasta de entrega
ACOMPANHAM = ("ui_agente.py", "short_comum.py", "nucleo_sonoro.py")

mapa = json.load(open(os.path.join(AQUI, "_mapa_exe.json")))
apps = sorted(os.path.basename(p)[:-7] for p in glob.glob(os.path.join(AQUI, "*_app.py"))
              if "lucas" not in p)
filtro = sys.argv[1] if len(sys.argv) > 1 else ""
alvos = [a for a in apps if a in mapa and (not filtro or filtro in a)]

print("recompilando %d agente(s)\n" % len(alvos), flush=True)
ok, falhou = [], []
t0 = time.time()

for i, motor in enumerate(alvos, 1):
    m = mapa[motor]
    exe, dest = m["exe"], os.path.join(RAIZ, m["fam"], m["sub"])
    app = motor + "_app.py"
    print("[%2d/%d] %-26s -> %s" % (i, len(alvos), motor, m["sub"]), flush=True)

    # ⚠️ .exe aberto trava a copia — o runbook lista isso como gotcha pago
    subprocess.run(["taskkill", "/F", "/IM", exe + ".exe"],
                   capture_output=True)

    r = subprocess.run(
        [sys.executable, "-m", "PyInstaller", "--noconfirm", "--clean",
         "--onefile", "--windowed", "--name", exe,
         "--paths", AQUI,
         "--hidden-import", motor,
         "--hidden-import", "ui_agente",
         "--hidden-import", "short_comum",
         "--hidden-import", "nucleo_sonoro",
         "--distpath", os.path.join(TMP, "dist"),
         "--workpath", os.path.join(TMP, "build"),
         "--specpath", TMP,
         app],
        cwd=AQUI, capture_output=True, text=True)

    novo = os.path.join(TMP, "dist", exe + ".exe")
    if r.returncode != 0 or not os.path.exists(novo):
        falhou.append((motor, (r.stderr or "")[-160:]))
        print("        FALHOU", flush=True)
        continue

    os.makedirs(dest, exist_ok=True)
    shutil.copy2(novo, os.path.join(dest, exe + ".exe"))
    for f in (motor + ".py", app) + ACOMPANHAM:
        o = os.path.join(AQUI, f)
        if os.path.exists(o):
            shutil.copy2(o, os.path.join(dest, f))
    ok.append(motor)
    print("        ok  %.1f MB" % (os.path.getsize(novo) / 1048576.0), flush=True)

print("\n%s\nOK: %d | FALHOU: %d | %.1f min"
      % ("=" * 60, len(ok), len(falhou), (time.time() - t0) / 60.0), flush=True)
for m, e in falhou:
    print("  FALHOU %-24s %s" % (m, e.replace("\n", " ")), flush=True)
