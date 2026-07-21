"""Instalador grafico do Veo Editor By EDDIE.

Empacotado com PyInstaller num unico .exe. Os arquivos do app viajam embutidos
no proprio executavel (--add-data) e sao extraidos para a pasta escolhida.

O que ele faz:
  1. Verifica Python e FFmpeg (instala pelo winget se faltar)
  2. Copia os arquivos do app para a pasta de destino
  3. Cria o ambiente virtual e instala as dependencias
  4. Cria o atalho na area de trabalho

Nao precisa de admin: instala no perfil do usuario.
"""

import os
import sys
import shutil
import threading
import subprocess
import tkinter as tk
from tkinter import ttk, filedialog

APP_NOME = "Veo Editor By EDDIE"
VERSAO = "1.2"  # app desktop (tkinter): sem navegador, mesma identidade visual
PADRAO = os.path.join(os.path.expanduser("~"), "VeoEditor")

# esconde a janela de console dos subprocessos
SEM_JANELA = subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0

BG = "#0d1117"
CARD = "#161b22"
INK = "#e6edf3"
DIM = "#8b949e"
AQUA = "#18cbb6"
RED = "#e0524a"


def recurso(rel):
    """Caminho de um arquivo embutido, funcionando congelado ou nao."""
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, rel)


def rodar(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8",
                          errors="replace", creationflags=SEM_JANELA, **kw)


def achar(nome):
    return shutil.which(nome)


class Instalador(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(f"{APP_NOME} - Instalador v{VERSAO}")
        self.configure(bg=BG)
        self.resizable(False, False)
        self.geometry("560x520")
        self._centralizar(560, 520)
        self.rodando = False
        self._montar()

    def _centralizar(self, w, h):
        x = (self.winfo_screenwidth() - w) // 2
        y = (self.winfo_screenheight() - h) // 2
        self.geometry(f"{w}x{h}+{x}+{y}")

    def _montar(self):
        tk.Label(self, text="Veo Editor", bg=BG, fg=INK,
                 font=("Segoe UI", 20, "bold")).pack(anchor="w", padx=28, pady=(26, 0))
        tk.Label(self, text="By EDDIE", bg=BG, fg=AQUA,
                 font=("Segoe UI", 20, "bold")).pack(anchor="w", padx=28)
        tk.Label(self, text="Esteira de producao: o zip baixado do Flow vira video editado sozinho.",
                 bg=BG, fg=DIM, font=("Segoe UI", 9)).pack(anchor="w", padx=28, pady=(4, 20))

        tk.Label(self, text="Instalar em:", bg=BG, fg=DIM,
                 font=("Segoe UI", 9)).pack(anchor="w", padx=28)
        linha = tk.Frame(self, bg=BG)
        linha.pack(fill="x", padx=28, pady=(4, 16))
        self.destino = tk.Entry(linha, bg=CARD, fg=INK, insertbackground=INK,
                                relief="flat", font=("Segoe UI", 10))
        self.destino.insert(0, PADRAO)
        self.destino.pack(side="left", fill="x", expand=True, ipady=7, padx=(0, 8))
        self.bt_procurar = tk.Button(linha, text="Procurar", command=self._procurar,
                                     bg=CARD, fg=INK, relief="flat", cursor="hand2",
                                     font=("Segoe UI", 9), padx=14, pady=5)
        self.bt_procurar.pack(side="right")

        self.bt_instalar = tk.Button(self, text="Instalar", command=self._iniciar,
                                     bg=AQUA, fg="#04231f", relief="flat", cursor="hand2",
                                     font=("Segoe UI", 11, "bold"), pady=9)
        self.bt_instalar.pack(fill="x", padx=28)

        self.barra = ttk.Progressbar(self, mode="determinate", maximum=100)
        self.barra.pack(fill="x", padx=28, pady=(14, 8))

        self.log = tk.Text(self, bg="#05080c", fg=DIM, relief="flat", height=11,
                           font=("Consolas", 9), wrap="word", padx=12, pady=10)
        self.log.pack(fill="both", expand=True, padx=28, pady=(0, 24))
        self.log.configure(state="disabled")

    def _procurar(self):
        p = filedialog.askdirectory(title="Escolha onde instalar")
        if p:
            self.destino.delete(0, "end")
            self.destino.insert(0, os.path.join(p, "VeoEditor"))

    def _diz(self, msg, cor=None):
        def _():
            self.log.configure(state="normal")
            if cor:
                tag = f"c{abs(hash(cor))}"
                self.log.tag_configure(tag, foreground=cor)
                self.log.insert("end", msg + "\n", tag)
            else:
                self.log.insert("end", msg + "\n")
            self.log.see("end")
            self.log.configure(state="disabled")
        self.after(0, _)

    def _progresso(self, v):
        self.after(0, lambda: self.barra.configure(value=v))

    def _iniciar(self):
        if self.rodando:
            return
        self.rodando = True
        self.bt_instalar.configure(state="disabled", text="Instalando...", bg=CARD, fg=DIM)
        self.bt_procurar.configure(state="disabled")
        threading.Thread(target=self._instalar, daemon=True).start()

    # ---------------- etapas ----------------

    def _instalar(self):
        try:
            destino = self.destino.get().strip().strip('"')
            self._etapas(destino)
        except Exception as e:  # noqa: BLE001
            self._diz("")
            self._diz(f"FALHOU: {e}", RED)
            self._fim(ok=False)

    def _etapas(self, destino):
        self._diz("Verificando pre-requisitos...")
        self._progresso(5)

        python = self._garantir_python()
        self._progresso(20)
        self._garantir_ffmpeg()
        self._progresso(30)

        self._diz("")
        self._diz(f"Copiando arquivos para {destino}")
        self._copiar(destino)
        self._progresso(40)

        self._diz("Criando ambiente virtual...")
        venv_py = self._criar_venv(python, destino)
        self._progresso(55)

        self._diz("Instalando dependencias (pode levar alguns minutos)...")
        self._deps(venv_py, destino)
        self._progresso(90)

        self._diz("Criando atalho na area de trabalho...")
        atalho = self._atalho(destino)
        self._progresso(100)

        self._diz("")
        self._diz("Instalacao concluida.", AQUA)
        self._diz(f"Atalho: {atalho}", AQUA)
        self._fim(ok=True, destino=destino)

    def _garantir_python(self):
        py = achar("python") or achar("python3")
        if py:
            v = rodar([py, "--version"]).stdout.strip()
            self._diz(f"  [ok] {v}")
            return py
        self._diz("  Python nao encontrado. Instalando pelo winget...", DIM)
        if not achar("winget"):
            raise RuntimeError(
                "Python nao esta instalado e o winget nao esta disponivel.\n"
                "Instale o Python 3.10+ em python.org marcando 'Add to PATH' e rode de novo."
            )
        rodar(["winget", "install", "-e", "--id", "Python.Python.3.12",
               "--accept-source-agreements", "--accept-package-agreements"])
        py = achar("python") or achar("python3")
        if not py:
            raise RuntimeError(
                "O Python foi instalado, mas ainda nao esta no PATH.\n"
                "Feche este instalador, reabra e rode de novo."
            )
        self._diz("  [ok] Python instalado")
        return py

    def _garantir_ffmpeg(self):
        if achar("ffmpeg"):
            self._diz("  [ok] FFmpeg encontrado")
            return
        self._diz("  FFmpeg nao encontrado. Instalando pelo winget...", DIM)
        if not achar("winget"):
            raise RuntimeError(
                "FFmpeg nao esta instalado e o winget nao esta disponivel.\n"
                "Instale o FFmpeg e coloque no PATH, depois rode de novo."
            )
        rodar(["winget", "install", "-e", "--id", "Gyan.FFmpeg",
               "--accept-source-agreements", "--accept-package-agreements"])
        if not achar("ffmpeg"):
            raise RuntimeError(
                "O FFmpeg foi instalado, mas ainda nao esta no PATH.\n"
                "Feche este instalador, reabra e rode de novo."
            )
        self._diz("  [ok] FFmpeg instalado")

    def _copiar(self, destino):
        os.makedirs(destino, exist_ok=True)
        for nome in ("app.py", "esteira.py", "pipeline.py", "captions.py",
                     "requirements.txt", "README.md"):
            shutil.copy(recurso(os.path.join("payload", nome)), os.path.join(destino, nome))
        # v1.2: app desktop tkinter — nao ha mais templates web
        shutil.rmtree(os.path.join(destino, "templates"), ignore_errors=True)
        self._diz("  [ok] arquivos copiados")

    def _criar_venv(self, python, destino):
        venv = os.path.join(destino, ".venv")
        venv_py = os.path.join(venv, "Scripts", "python.exe")
        if not os.path.isfile(venv_py):
            r = rodar([python, "-m", "venv", venv])
            if r.returncode != 0:
                raise RuntimeError("nao consegui criar o ambiente virtual:\n" + (r.stderr or "")[-500:])
        self._diz("  [ok] ambiente criado")
        return venv_py

    def _deps(self, venv_py, destino):
        rodar([venv_py, "-m", "pip", "install", "--upgrade", "pip", "--quiet"])
        r = rodar([venv_py, "-m", "pip", "install", "-r",
                   os.path.join(destino, "requirements.txt")])
        if r.returncode != 0:
            raise RuntimeError("falha ao instalar dependencias:\n" + (r.stdout or r.stderr or "")[-900:])
        self._diz("  [ok] dependencias instaladas")

    def _atalho(self, destino):
        venv_py = os.path.join(destino, ".venv", "Scripts", "pythonw.exe")
        if not os.path.isfile(venv_py):
            venv_py = os.path.join(destino, ".venv", "Scripts", "python.exe")
        app = os.path.join(destino, "app.py")
        # o Desktop verdadeiro vem do Windows, nao de um palpite em ~/Desktop:
        # com OneDrive ligado as duas pastas existem e a legada nao e a visivel.
        ps = (
            "$d = [Environment]::GetFolderPath('Desktop'); "
            f"$lnk = Join-Path $d '{APP_NOME}.lnk'; "
            "$w = New-Object -ComObject WScript.Shell; "
            "$s = $w.CreateShortcut($lnk); "
            f"$s.TargetPath = '{venv_py}'; "
            f"$s.Arguments = '\"{app}\"'; "
            f"$s.WorkingDirectory = '{destino}'; "
            "$s.IconLocation = 'shell32.dll,177'; "
            f"$s.Description = '{APP_NOME}'; "
            "$s.Save(); "
            "Write-Output $lnk"
        )
        r = rodar(["powershell", "-NoProfile", "-Command", ps])
        if r.returncode != 0:
            raise RuntimeError("nao consegui criar o atalho:\n" + (r.stderr or "")[-400:])
        saida = (r.stdout or "").strip()
        lnk = saida.splitlines()[-1].strip() if saida else "area de trabalho"
        self._diz("  [ok] atalho criado")
        return lnk

    def _fim(self, ok, destino=None):
        def _():
            self.rodando = False
            self.bt_procurar.configure(state="normal")
            if ok:
                self.bt_instalar.configure(text="Abrir agora", bg=AQUA, fg="#04231f",
                                           state="normal",
                                           command=lambda: self._abrir(destino))
            else:
                self.bt_instalar.configure(text="Tentar de novo", bg=AQUA, fg="#04231f",
                                           state="normal", command=self._iniciar)
        self.after(0, _)

    def _abrir(self, destino):
        pyw = os.path.join(destino, ".venv", "Scripts", "pythonw.exe")
        if not os.path.isfile(pyw):
            pyw = os.path.join(destino, ".venv", "Scripts", "python.exe")
        subprocess.Popen([pyw, os.path.join(destino, "app.py")], cwd=destino,
                         creationflags=SEM_JANELA)
        self.after(2500, self.destroy)


class Silencioso:
    """Mesmas etapas, sem GUI. Uso: veo_editor_installer.exe --silent [pasta]"""

    def __init__(self, destino):
        self._destino = destino

    def _diz(self, msg, cor=None):
        print(msg, flush=True)

    def _progresso(self, v):
        pass

    def _fim(self, ok, destino=None):
        self._ok = ok

    def executar(self):
        self._ok = False
        try:
            Instalador._etapas(self, self._destino)
        except Exception as e:  # noqa: BLE001
            print(f"FALHOU: {e}", flush=True)
            return 1
        return 0 if self._ok else 1

    # reaproveita as etapas da classe grafica
    _garantir_python = Instalador._garantir_python
    _garantir_ffmpeg = Instalador._garantir_ffmpeg
    _copiar = Instalador._copiar
    _criar_venv = Instalador._criar_venv
    _deps = Instalador._deps
    _atalho = Instalador._atalho


if __name__ == "__main__":
    if "--silent" in sys.argv:
        i = sys.argv.index("--silent")
        alvo = sys.argv[i + 1] if len(sys.argv) > i + 1 else PADRAO
        sys.exit(Silencioso(alvo).executar())
    Instalador().mainloop()
