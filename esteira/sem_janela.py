# -*- coding: utf-8 -*-
"""Nenhum processo filho abre janela de console. Chamar `aplicar()` cedo.

⛔⛔ O DEFEITO: num build `--windowed` do PyInstaller o app nao tem console, e
CADA processo filho no Windows abre o SEU. O operador viu isso em 2026-08-20 —
uma janela preta `C:\\ffmpeg\\bin\\ffmpeg.exe` por cima da ESTEIRA enquanto o
video baixava.

⚠️ E consertar so' as MINHAS chamadas nao bastaria. Sao quatro em `ler.py`
(uma delas dentro de um laco: **um processo por quadro da folha**, ou seja uma
janela por quadro), mas o `yt_dlp` dispara ffmpeg por conta propria para juntar
as faixas — e ele NAO esconde: medido no fonte dele, zero ocorrencia de
`CREATE_NO_WINDOW`, `STARTF_USESHOWWINDOW` ou `startupinfo`.

⭐ Por isso o remendo e' no `subprocess.Popen`, que e' por onde TODO mundo passa
— eu, o yt-dlp e qualquer biblioteca que venha depois. `subprocess.run` usa
`Popen` por dentro, entao ele vem junto de graca.

⛔ E ele e' idempotente e a prova de falha: se qualquer coisa der errado ao
aplicar, o app continua abrindo — janela de console e' feiura, nao e' motivo
para a ferramenta nao subir.
"""
import subprocess
import sys

CREATE_NO_WINDOW = 0x08000000
SW_HIDE = 0


def aplicar():
    if not sys.platform.startswith("win"):
        return False
    if getattr(subprocess.Popen, "_sem_janela", False):
        return True                      # ja' aplicado; nao empilhar remendo
    try:
        original = subprocess.Popen.__init__

        def com_janela_escondida(self, *a, **k):
            try:
                k["creationflags"] = k.get("creationflags", 0) | CREATE_NO_WINDOW
                si = k.get("startupinfo") or subprocess.STARTUPINFO()
                si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                si.wShowWindow = SW_HIDE
                k["startupinfo"] = si
            except Exception:  # noqa: BLE001
                pass             # ⚠️ na duvida, roda com janela e nao quebra
            return original(self, *a, **k)

        subprocess.Popen.__init__ = com_janela_escondida
        subprocess.Popen._sem_janela = True
        return True
    except Exception:  # noqa: BLE001
        return False
