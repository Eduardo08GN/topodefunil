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

# ⛔ REMENDO DE CONSOLE, o mesmo do `medir_personagens.py` (linha 51). O
# console do Windows e' cp1252 e os marcadores deste arquivo nao cabem nele.
# ⚠️ O padrao que faz o bug ser caro: os prints com marcador so' rodam QUANDO
# HA' ALGO A REPORTAR, entao o crash acontece exatamente na hora em que a
# mensagem importa, e nunca no caminho feliz.
for _f in (sys.stdout, sys.stderr):
    try:
        _f.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

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

# ⛔⛔ O MAPA E' O ARTEFATO QUE JA' CUSTOU CARO: foi um destino errado nele que
# sobrescreveu 4 .exe do OUTRO AUTOR. E `OK: 43 | FALHOU: 0` passou verde no
# mesmo dia — a linha de sucesso NAO prova destino, entao o mapa tem de se
# provar ANTES de construir.
# ⚠️ As duas mentiras que ele ja' contou, agora cobradas:
#   (a) entrada sem `<motor>_app.py` — nao e' construivel, so' afirma que um
#       motor mora numa pasta. Foi assim que `flagrante_lucas` acabou apontando
#       para a NOSSA `AGENTES-SHORT\FLAGRANTE-SHORT`: o mapa foi derivado lendo
#       os `.py` de dentro da pasta, e la' ainda havia um `*_lucas.py` sobrando
#       de antes do desacoplamento de 2026-08-03.
#   (b) duas entradas para a MESMA pasta — uma delas esta' errada por definicao,
#       e e' exatamente a forma do acidente (dois motores, um destino).
_sem_app = sorted(k for k in mapa if not os.path.exists(os.path.join(AQUI, k + "_app.py")))
_por_pasta = {}
for _k, _v in mapa.items():
    _por_pasta.setdefault(os.path.normcase(os.path.join(_v["fam"], _v["sub"])), []).append(_k)
_colisao = {k: sorted(v) for k, v in _por_pasta.items() if len(v) > 1}
if _sem_app or _colisao:
    print("⛔ MAPA INCONSISTENTE — corrija `_mapa_exe.json` antes de construir:")
    for _k in _sem_app:
        print("   sem %s_app.py: %s" % (_k, _k))
    for _p, _ms in sorted(_colisao.items()):
        print("   dois motores no mesmo destino %s: %s" % (_p, ", ".join(_ms)))
    sys.exit(2)

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
