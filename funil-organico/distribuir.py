#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Leva o motor do repo ate' o .exe na area de trabalho do operador.

    python funil-organico/distribuir.py                    # todos
    python funil-organico/distribuir.py --so PEE-SHORT     # um so'
    python funil-organico/distribuir.py --sem-build        # so' sincroniza
    python funil-organico/distribuir.py --novo RESSURREICAO-SHORT \\
        --motor ressurreicao_short.py                      # agente novo

Duas etapas, na ordem que o RUNBOOK-app-offline.md manda:
  1. SINCRONIZAR — copia do repo, para cada pasta de agente, todo .py que ja'
     existe la'. O ledger local (.json) nunca e' tocado.
  2. RECOMPILAR   — PyInstaller --onefile --windowed por agente.
     ⛔ Sem esta etapa a correcao NAO chega no operador: o .exe congela o codigo
     do dia em que foi compilado (RUNBOOK §O BUILD DO .exe).

⚠️ POR QUE ESTE ARQUIVO MORA NO REPO. Ele viveu duas sessoes como script de
rascunho e foi reescrito do zero cada vez. Recompilar .exe e' item do checklist
de entrega (licoes-de-construcao §checklist) — ferramenta de checklist nao pode
morar em pasta temporaria.
"""
import argparse
import glob
import os
import shutil
import subprocess
import sys
import tempfile

REPO = os.path.dirname(os.path.abspath(__file__))
DEST = os.path.join(os.path.expanduser("~"), "Desktop", "agentes_py")

# SHORT primeiro: e' o que esta' em producao hoje (AdBatch Vertical 3).
# ⛔ SO' OS SHORT. As pastas PEE / FLAGRANTE / VAZAMENTO / NECROSE (sem sufixo)
# sao os agentes de arco longo, com label `lucas`, que sairam para
# `agentes-de-terceiros/` em 2026-08-03. O operador mandou MANTER os .exe deles
# na area de trabalho como estao — e' exatamente por isso que eles nao entram
# aqui: o build falharia (o .py nao mora mais em funil-organico/) e, se um dia
# passasse, sobrescreveria o binario que ele pediu para preservar.
ORDEM = ["CLEAN-SHORT", "RESSURREICAO-SHORT", "ESCANDALO-SHORT", "TROCA-SHORT",
         "PEE-SHORT", "FLAGRANTE-SHORT", "VAZAMENTO-SHORT", "NECROSE-SHORT",
         "ORGANICWAVE-SHORT"]

# a maquinaria que TODO agente carrega — a interface e' compartilhada, so' o
# motor muda (CLAUDE.md §Agente maduro vira ferramenta)
COMUNS = ["short_comum.py", "ui_agente.py", "nucleo_sonoro.py"]


def agentes():
    for nome in ORDEM:
        pasta = os.path.join(DEST, nome)
        if not os.path.isdir(pasta):
            continue
        apps = [f for f in os.listdir(pasta) if f.endswith("_app.py")]
        exes = [f for f in os.listdir(pasta) if f.upper().endswith(".EXE")]
        if not apps:
            continue
        yield {"nome": nome, "pasta": pasta, "app": apps[0],
               "exe": exes[0] if exes else "AGENTE-%s.exe" % nome}


def bootstrap(nome, motor):
    """Cria a pasta de um agente NOVO. sincronizar() so' atualiza .py que ja'
    existe la' — de proposito, para nao espalhar motor de um agente na pasta de
    outro. Entao a primeira copia precisa de um passo explicito."""
    if nome not in ORDEM:
        return "⛔ %s nao esta' em ORDEM — acrescente antes, senao agentes() " \
               "nunca vai enxergar a pasta" % nome
    app = os.path.splitext(motor)[0] + "_app.py"
    for f in COMUNS + [motor, app]:
        if not os.path.exists(os.path.join(REPO, f)):
            return "⛔ falta no repo: %s" % f
    pasta = os.path.join(DEST, nome)
    if not os.path.isdir(pasta):
        os.makedirs(pasta)
    for f in COMUNS + [motor, app]:
        shutil.copyfile(os.path.join(REPO, f), os.path.join(pasta, f))
    return "pasta pronta com %s" % ", ".join(COMUNS + [motor, app])


def sincronizar(ag):
    """Copia do repo todo .py que a pasta do agente ja' tem. Nunca cria arquivo
    novo — se um .py nao esta' la', nao e' desse agente (use --novo)."""
    trocados = []
    for caminho in glob.glob(os.path.join(ag["pasta"], "*.py")):
        nome = os.path.basename(caminho)
        fonte = os.path.join(REPO, nome)
        if not os.path.exists(fonte):
            continue
        a = open(fonte, "rb").read().replace(b"\r\n", b"\n")
        b = open(caminho, "rb").read().replace(b"\r\n", b"\n")
        if a != b:
            shutil.copyfile(fonte, caminho)
            trocados.append(nome)
    return trocados


def matar(exe):
    """O .exe fica travado se uma instancia do app ficou pendurada (gotcha 3)."""
    proc = os.path.splitext(exe)[0]
    subprocess.run(["powershell", "-NoProfile", "-Command",
                    "Get-Process '%s' -ErrorAction SilentlyContinue | "
                    "Stop-Process -Force" % proc],
                   capture_output=True)


def compilar(ag):
    tmp = os.path.join(tempfile.gettempdir(), "build_" + ag["nome"])
    nome_exe = os.path.splitext(ag["exe"])[0]
    # o motor entra por --paths + --hidden-import: --add-data resolve relativo
    # ao --specpath e quebra (gotcha 1 do RUNBOOK)
    modulos = [os.path.splitext(f)[0] for f in os.listdir(ag["pasta"])
               if f.endswith(".py") and not f.endswith("_app.py")]
    cmd = [sys.executable, "-m", "PyInstaller", "--noconfirm", "--clean",
           "--onefile", "--windowed", "--name", nome_exe,
           "--paths", REPO,
           "--distpath", os.path.join(tmp, "dist"),
           "--workpath", os.path.join(tmp, "build"),
           "--specpath", tmp]
    for m in modulos:
        cmd += ["--hidden-import", m]
    # icone proprio se existir; senao o generico dos agentes
    for cand in ("%s.ico" % ag["nome"].lower(), "agente.ico"):
        icone = os.path.join(REPO, "icones", cand)
        if os.path.exists(icone):
            cmd += ["--icon", icone]
            break
    cmd.append(os.path.join(REPO, ag["app"]))

    r = subprocess.run(cmd, capture_output=True, text=True, errors="replace")
    if r.returncode != 0:
        return False, (r.stderr or r.stdout)[-700:]

    novo = os.path.join(tmp, "dist", nome_exe + ".exe")
    if not os.path.exists(novo):
        return False, "PyInstaller voltou 0 mas nao produziu %s" % novo
    matar(ag["exe"])
    shutil.copyfile(novo, os.path.join(ag["pasta"], ag["exe"]))
    return True, "%.1f MB" % (os.path.getsize(novo) / 1e6)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--so", help="so' este agente (nome da pasta)")
    ap.add_argument("--sem-build", action="store_true", help="so' sincroniza")
    ap.add_argument("--novo", help="cria a pasta de um agente novo")
    ap.add_argument("--motor", help="o <motor>.py do --novo")
    a = ap.parse_args()

    if a.novo:
        if not a.motor:
            print("⛔ --novo exige --motor <arquivo>.py")
            return 1
        msg = bootstrap(a.novo, a.motor)
        print("[%-18s] %s" % (a.novo, msg))
        if msg.startswith("⛔"):
            return 1
        a.so = a.so or a.novo

    falhas = 0
    for ag in agentes():
        if a.so and ag["nome"] != a.so:
            continue
        trocados = sincronizar(ag)
        print("[%-18s] sync: %s" % (ag["nome"],
                                    ", ".join(trocados) if trocados else "nada novo"))
        sys.stdout.flush()
        if a.sem_build:
            continue
        ok, msg = compilar(ag)
        print("[%-18s] build %s -> %s" % (ag["nome"], ag["exe"],
                                          "OK, " + msg if ok else "FALHOU"))
        if not ok:
            falhas += 1
            print("    %s" % msg.replace("\n", "\n    "))
        sys.stdout.flush()
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
