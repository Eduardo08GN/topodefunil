# -*- coding: utf-8 -*-
"""RECOMPILAR — o passo que faltava entre o motor e o que o operador clica.

    python funil-organico/recompilar.py            <- lista o que esta' atrasado
    python funil-organico/recompilar.py --aplicar  <- recompila so' os atrasados
    python funil-organico/recompilar.py --aplicar --tudo

⛔⛔ POR QUE ISTO EXISTE. O repo tem a regra *"agente maduro vira ferramenta"* e
o RUNBOOK ensina a compilar UM `.exe` por vez, na mao. Consequencia medida em
2026-08-20: **29 dos 55 executaveis estavam mais velhos que o proprio motor**,
alguns por uma semana. O operador clicava no icone e rodava codigo antigo — sem
nenhum aviso, porque `.exe` velho nao reclama.

⭐⭐ E ESSA E' A MESMA ARMADILHA, NAS DUAS DIRECOES, que este repo ja' pagou:
  · o `vick16` REPROVADO ficou rodavel e o operador gerou um lote inteiro nele
  · o `banho16_3t` APROVADO nunca foi entregue e ele nao tinha como roda-lo
Nos dois casos quem decide o que roda e' a PASTA, nunca o repo. Enquanto a
ponte for manual, ela vai estar quebrada na hora em que ninguem olhar.

⚠️ O QUE ELE COMPARA e' a data do `.exe` contra a do MOTOR (`<nome>_short.py`)
E a do `short_comum.py` — porque a maquinaria compartilhada entra dentro do
executavel congelado, e mexer nela envelhece TODOS os `.exe` de uma vez. Esse
segundo termo e' o que um `git status` nunca mostraria.
"""
import argparse
import os
import re
import shutil
import subprocess
import sys
import time

AQUI = os.path.dirname(os.path.abspath(__file__))
DESK = r"C:\Users\edlut\Desktop\agentes_py"
COMPARTILHADOS = ("short_comum.py", "ui_agente.py")


def _chave(txt):
    """`BANHO-16-3T` e `banho16_3t` colapsam na mesma chave.

    ⛔ E o sufixo `-SHORT` da pasta cai: a familia AGENTES-SHORT guarda o
    `BOTICA-SHORT`, cujo motor e' `botica_short.py` — sem tirar o sufixo, 19
    executaveis ficavam orfaos e a varredura os declarava "sem motor", que e'
    pior que erro: e' silencio.
    """
    k = re.sub(r"[^a-z0-9]", "", txt.lower())
    return k[:-5] if k.endswith("short") else k


def motores():
    """⛔ NAO basta varrer `*_short_app.py`: o `clean_short_v2_app.py` nao
    segue esse molde, e por isso o `CLEAN-SHORT-V2` saia como "sem motor
    casado" — um `.exe` que a ferramenta NAO ENXERGA, que e' exatamente a
    armadilha que ela existe para fechar. Aqui todo `*_app.py` entra, e o
    motor e' procurado nas duas formas de nome.
    """
    m = {}
    for f in os.listdir(AQUI):
        if not f.endswith("_app.py"):
            continue
        base = f[:-len("_app.py")]
        for cand in (base + ".py", base + "_short.py"):
            motor = os.path.join(AQUI, cand)
            if os.path.exists(motor):
                nome = cand[:-3]
                m[_chave(base)] = (nome, motor, os.path.join(AQUI, f))
                break
    return m


def familia(nome):
    """Quase a regra do `distribuir.py`, e a diferenca esta' medida.

    ⚠️ La' o teste e' `-16S?$` — ANCORADO NO FIM — e por isso `BANHO-16-3T`
    cai em AGENTES-NORMAIS, longe das outras dezesseis. Na area de trabalho
    ele mora em AGENTES-16, entao quem esta' errado e' a regra, nao a pasta.
    Aqui o `16` tambem conta no MEIO do nome.
    """
    if re.search(r"-16S?(-|$)", nome):
        return "AGENTES-16"
    if "-SHORT" in nome:
        return "AGENTES-SHORT"
    return "AGENTES-NORMAIS"


def _pasta_nova(nome):
    """O nome de pasta que a area de trabalho ja' usa, para um motor que nunca
    foi compilado.

    ⛔ Nao e' cosmetico por duas razoes. A chave tem de casar (`AMISH-16S`
    daria `amish16s` contra o `amish16` do motor, e a pasta sairia como
    "SEM MOTOR" na varredura seguinte, que e' pior que nao existir) e a
    FAMILIA e' lida do nome (`BANHO16-3T` cai em AGENTES-NORMAIS, longe das
    outras).

    ⭐ A convencao sai das 57 pastas que ja' existem: `RUTH-16`,
    `BANHO-16-3T`, `CLEAN-V1-16S`, `BOTICA-SHORT`, `ORGANICWAVE`. O `-SHORT`
    fica so' em quem NAO e' da familia 16.
    """
    n = nome
    curto = n.endswith("_short")
    if curto:
        n = n[:-len("_short")]
    n = n.upper().replace("_", "-")

    # o `16` cola na letra anterior em `AMISH16`/`BANHO16-3T`; separa
    i = n.find("16")
    while i > 0:
        if n[i - 1].isalpha():
            n = n[:i] + "-" + n[i:]
            break
        i = n.find("16", i + 2)

    dezesseis = ("-16" in n)
    if curto and not dezesseis:
        n += "-SHORT"
    return n


def inventario():
    m, out, vistos = motores(), [], set()
    piso = max(os.path.getmtime(os.path.join(AQUI, c))
               for c in COMPARTILHADOS if os.path.exists(os.path.join(AQUI, c)))
    for fam in sorted(os.listdir(DESK)):
        d = os.path.join(DESK, fam)
        if not os.path.isdir(d):
            continue
        for sub in sorted(os.listdir(d)):
            sd = os.path.join(d, sub)
            if not os.path.isdir(sd):
                continue
            exes = [f for f in os.listdir(sd) if f.lower().endswith(".exe")]
            if not exes:
                continue
            k = _chave(sub)
            if k not in m:
                out.append({"fam": fam, "pasta": sub, "exe": exes[0],
                            "estado": "SEM MOTOR"})
                continue
            nome, motor, app = m[k]
            te = os.path.getmtime(os.path.join(sd, exes[0]))
            # ⭐ o piso compartilhado entra na conta
            tm = max(os.path.getmtime(motor), piso)
            out.append({"fam": fam, "pasta": sub, "exe": exes[0], "nome": nome,
                        "motor": motor, "app": app, "dir": sd, "te": te,
                        "tm": tm,
                        "estado": "ATRASADO" if tm > te else "ok"})
            vistos.add(k)

    # ⭐⭐ MOTOR SEM EXE NENHUM. O laco acima varre PASTAS, entao um motor que
    # nunca foi compilado nao aparece — e a ferramenta imprimia "0 ATRASADOS",
    # que le como "tudo em dia". Foi assim que o AMISH 16S ficou invisivel.
    # ⛔ AUSENCIA NAO E' ZERO: o que nao se enumera, some.
    for k, (nome, motor, app) in sorted(m.items()):
        if k in vistos:
            continue
        pasta = _pasta_nova(nome)
        out.append({"fam": familia(pasta), "pasta": pasta,
                    "exe": "AGENTE-%s.exe" % pasta, "nome": nome,
                    "motor": motor, "app": app,
                    "dir": os.path.join(DESK, familia(pasta), pasta),
                    "te": 0, "tm": max(os.path.getmtime(motor), piso),
                    "estado": "SEM EXE"})
    return out


def compilar(it):
    # ⭐ pasta nova para motor que nunca foi compilado
    os.makedirs(it["dir"], exist_ok=True)
    tmp = os.path.join(os.environ.get("TEMP", "."), "rc_" + it["nome"])
    shutil.rmtree(tmp, ignore_errors=True)
    alvo = os.path.splitext(it["exe"])[0]
    r = subprocess.run(
        [sys.executable, "-m", "PyInstaller", "--noconfirm", "--clean",
         "--onefile", "--windowed", "--name", alvo, "--paths", AQUI,
         "--hidden-import", it["nome"],
         "--hidden-import", "short_comum", "--hidden-import", "ui_agente",
         "--distpath", os.path.join(tmp, "dist"),
         "--workpath", os.path.join(tmp, "build"),
         "--specpath", tmp, it["app"]],
        capture_output=True, text=True)
    novo = os.path.join(tmp, "dist", alvo + ".exe")
    if r.returncode or not os.path.exists(novo):
        return "FALHOU: " + (r.stderr or "")[-160:].replace("\n", " ")
    # ⚠️ o .exe travado por uma instancia aberta e' o gotcha do RUNBOOK
    try:
        shutil.copy2(novo, os.path.join(it["dir"], it["exe"]))
    except PermissionError:
        return "EM USO — feche o app e rode de novo"
    # ⭐ o .py do motor vai junto: as pastas ja' carregam uma copia, e uma copia
    # velha ao lado de um .exe novo e' a proxima confusao.
    for f in (it["motor"],) + tuple(os.path.join(AQUI, c) for c in COMPARTILHADOS):
        if os.path.exists(f):
            try:
                shutil.copy2(f, os.path.join(it["dir"], os.path.basename(f)))
            except PermissionError:
                pass
    return "ok"


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--aplicar", action="store_true")
    ap.add_argument("--tudo", action="store_true",
                    help="recompila mesmo o que esta' em dia")
    a = ap.parse_args()

    inv = inventario()
    orfaos = [i for i in inv if i["estado"] == "SEM MOTOR"]
    atrasados = [i for i in inv if i["estado"] == "ATRASADO"]
    novos = [i for i in inv if i["estado"] == "SEM EXE"]
    alvos = [i for i in inv if i["estado"] in ("ATRASADO", "ok", "SEM EXE")] \
        if a.tudo else atrasados + novos

    print("%d executaveis · %d ATRASADOS · %d SEM EXE · %d sem motor casado"
          % (len(inv) - len(novos), len(atrasados), len(novos), len(orfaos)))
    for i in novos:
        print("   NOVO %-14s %-20s motor %s, exe nenhum"
              % (i["fam"], i["pasta"], os.path.basename(i["motor"])))
    for i in atrasados:
        print("   %-16s %-20s exe %s < fonte %s"
              % (i["fam"], i["pasta"],
                 time.strftime("%d/%m %H:%M", time.localtime(i["te"])),
                 time.strftime("%d/%m %H:%M", time.localtime(i["tm"]))))
    for i in orfaos:
        print("   ?? %-16s %s" % (i["fam"], i["pasta"]))

    if not a.aplicar:
        print("\n(--dry-run. Use --aplicar para recompilar.)")
        return 0

    print("\nrecompilando %d..." % len(alvos))
    ruins = []
    for n, i in enumerate(alvos, 1):
        r = compilar(i)
        print("  [%2d/%2d] %-20s %s" % (n, len(alvos), i["pasta"], r))
        if r != "ok":
            ruins.append((i["pasta"], r))

    # ⛔ A CONFERENCIA E' DEPOIS, e e' ela que vale: recompilar sem reconferir
    # e' o mesmo relato-em-vez-de-medicao de sempre.
    restam = [i for i in inventario() if i["estado"] == "ATRASADO"]
    print("\nATRASADOS depois: %d" % len(restam))
    for i in restam:
        print("   ainda atrasado: %s" % i["pasta"])
    for p, r in ruins:
        print("   FALHA: %s — %s" % (p, r))
    return 1 if (restam or ruins) else 0


if __name__ == "__main__":
    sys.exit(main())
