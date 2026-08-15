# -*- coding: utf-8 -*-
"""Conserta o erro de destino dos quatro pares FLAGRANTE/NECROSE/PEE/VAZAMENTO.

⛔⛔ O ERRO: o `recompilar_todos.py` mapeou `flagrante_short` (e os outros tres)
para `AGENTES-NORMAIS\\FLAGRANTE`, que e' a pasta do agente LONGO — cujo app e'
`flagrante_lucas_app.py`, do outro autor. Resultado: os quatro `.exe` de
AGENTES-NORMAIS passaram a abrir o agente SHORT, e as quatro pastas de
AGENTES-SHORT ficaram sem atualizacao.

⚠️ A causa raiz foi eu completar o mapa NA MAO quando a derivacao automatica
disse "sem pasta". A derivacao estava certa: nao havia pasta porque aqueles
quatro motores SHORT moram em AGENTES-SHORT com o sufixo -SHORT no nome, e a
pasta sem sufixo e' de outro agente. Palpite meu no lugar de medicao.

Este script:
  1. reconstroi os quatro LONGOS a partir do `*_lucas_app.py` (fonte em
     `agentes-de-terceiros/`, que e' onde eles moram no repo);
  2. reconstroi os quatro SHORT na pasta certa, `AGENTES-SHORT\\*-SHORT`.
"""
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
TERCEIROS = os.path.join(os.path.dirname(AQUI), "agentes-de-terceiros")
RAIZ = r"C:\Users\edlut\Desktop\agentes_py"
TMP = os.path.join(os.environ.get("TEMP", "."), "buildconserto")

NOMES = ("flagrante", "necrose", "pee", "vazamento")

TAREFAS = []
for n in NOMES:
    # o LONGO (do outro autor) — fonte em agentes-de-terceiros
    TAREFAS.append({
        "app": n + "_lucas_app.py", "cwd": TERCEIROS, "motor": n + "_lucas",
        "exe": "AGENTE-" + n.upper(),
        "dest": os.path.join(RAIZ, "AGENTES-NORMAIS", n.upper()),
        "extra": [AQUI],   # o lucas importa ui_agente/short_comum do funil
    })
    # o SHORT (nosso) — fonte em funil-organico
    TAREFAS.append({
        "app": n + "_short_app.py", "cwd": AQUI, "motor": n + "_short",
        "exe": "AGENTE-" + n.upper() + "-SHORT",
        "dest": os.path.join(RAIZ, "AGENTES-SHORT", n.upper() + "-SHORT"),
        "extra": [],
    })

print("reconstruindo %d binarios (4 longos + 4 short)\n" % len(TAREFAS), flush=True)
ok, ruim = [], []
t0 = time.time()

for i, t in enumerate(TAREFAS, 1):
    print("[%d/%d] %-26s -> %s" % (i, len(TAREFAS), t["app"],
                                   os.path.basename(t["dest"])), flush=True)
    subprocess.run(["taskkill", "/F", "/IM", t["exe"] + ".exe"],
                   capture_output=True)
    paths = [t["cwd"]] + t["extra"]
    cmd = [sys.executable, "-m", "PyInstaller", "--noconfirm", "--clean",
           "--onefile", "--windowed", "--name", t["exe"]]
    for p in paths:
        cmd += ["--paths", p]
    cmd += ["--hidden-import", t["motor"],
            "--hidden-import", "ui_agente",
            "--hidden-import", "short_comum",
            "--hidden-import", "nucleo_sonoro",
            "--distpath", os.path.join(TMP, "dist"),
            "--workpath", os.path.join(TMP, "build"),
            "--specpath", TMP, t["app"]]
    r = subprocess.run(cmd, cwd=t["cwd"], capture_output=True, text=True)
    novo = os.path.join(TMP, "dist", t["exe"] + ".exe")
    if r.returncode != 0 or not os.path.exists(novo):
        ruim.append((t["exe"], (r.stderr or "")[-200:]))
        print("        FALHOU", flush=True)
        continue
    os.makedirs(t["dest"], exist_ok=True)
    shutil.copy2(novo, os.path.join(t["dest"], t["exe"] + ".exe"))
    # os fontes que acompanham
    for f in (t["motor"] + ".py", t["app"]):
        o = os.path.join(t["cwd"], f)
        if os.path.exists(o):
            shutil.copy2(o, os.path.join(t["dest"], f))
    for f in ("ui_agente.py", "short_comum.py", "nucleo_sonoro.py"):
        shutil.copy2(os.path.join(AQUI, f), os.path.join(t["dest"], f))
    ok.append(t["exe"])
    print("        ok  %.1f MB" % (os.path.getsize(novo) / 1048576.0), flush=True)

print("\nOK: %d | FALHOU: %d | %.1f min"
      % (len(ok), len(ruim), (time.time() - t0) / 60.0), flush=True)
for e, msg in ruim:
    print("  FALHOU %-26s %s" % (e, msg.replace("\n", " ")), flush=True)
