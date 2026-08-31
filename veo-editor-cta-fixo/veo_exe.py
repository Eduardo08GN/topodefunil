# -*- coding: utf-8 -*-
"""Ponto de entrada do .exe do Veo Editor CTA FIXO.

⛔ ESTE ARQUIVO SO' EXISTE POR CAUSA DO CONGELAMENTO. Rodando pelo `.bat` com
   o venv, nada aqui e' usado — o `app.py` e' chamado direto. Ele existe para
   nao editar `app.py`, `esteira.py` nem `pipeline.py`, que estao em
   desenvolvimento ativo pelo outro autor: mexer neles renderia conflito a
   cada commit dele. Todo desvio mora aqui, de fora.

Dois defeitos que o `--onefile` cria neste app, e o conserto de cada um:

1. AS PASTAS DA ESTEIRA SUMIAM COM O VIDEO DENTRO.
   `esteira.py` ancora tudo em `dirname(abspath(__file__))`, e congelado isso
   e' a pasta temporaria `_MEIPASS`, que o Windows APAGA ao fechar o app.
   `01_entrada` ate `05_erros`, o `historico.csv` e todo video pronto
   nasceriam la' e evaporariam no fechamento.
   ⭐ O proprio autor deixou a saida pronta: a variavel `VEO_EDITOR_BASE`.

2. O AUTO-EDITOR NAO SERIA ENCONTRADO.
   `pipeline._auto_editor()` procura o binario ao lado de `sys.executable` e
   depois no PATH. Congelado, `sys.executable` e' o proprio `.exe` e o
   `auto-editor` so' existe dentro do venv — que o `.exe` dispensa.

⛔⛔ A PRIMEIRA TENTATIVA DE CONSERTAR O (2) FOI REPROVADA EM CAMPO, e a
    licao vale mais que o conserto. Ela punha um `auto-editor.bat` de uma
    linha ao lado do executavel, chamando o proprio `.exe` com um argumento
    sentinela. Parecia limpo e morreu no primeiro lote real:

        Security validation failure: parent process has different executable!

    A mensagem vem do BOOTLOADER do PyInstaller, nao do nosso codigo nem do
    auto-editor (a string esta' dentro do `runw.exe`). Em `--onefile` ele
    valida quem e' o processo pai, e a ponte criava a cadeia
    `exe -> cmd.exe -> exe`: pai diferente, execucao recusada.

    ⭐ O conserto certo elimina o processo filho em vez de tentar autoriza-lo.
    O `auto_editor` ja' esta' DENTRO do bundle, entao ele roda no MESMO
    processo, por chamada de funcao. Sem subprocess, sem `.bat`, sem
    bootloader no caminho. `pipeline._run` e' global do modulo, entao da'
    para interceptar so' a chamada do auto-editor e deixar todas as outras
    (ffmpeg, ffprobe) seguindo pelo subprocess normal.

⚠️ E `import app` NAO abre a janela: `app.py` nao tem `main()`, tudo mora sob
   `if __name__ == "__main__"`, inclusive a trava de instancia unica e o foco
   da janela ja' aberta. Por isso `runpy.run_module(run_name="__main__")`.
"""

import os
import sys


class _Resultado(object):
    """O minimo que `pipeline._run` promete a quem chama: codigo e saidas."""

    def __init__(self, returncode, stdout, stderr):
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr


# marcador que substitui o caminho do binario. Nunca chega a virar comando:
# o `_run` remendado o intercepta antes.
SENTINELA_AE = "<<auto-editor-embutido>>"


def _rodar_auto_editor(args, cwd=None):
    """Roda o auto_editor NO MESMO PROCESSO, imitando o subprocess."""
    import contextlib
    import io as _io

    argv_antigo = sys.argv
    cwd_antigo = os.getcwd()
    saida, erro = _io.StringIO(), _io.StringIO()
    codigo = 0
    try:
        if cwd:
            os.chdir(cwd)
        sys.argv = ["auto-editor"] + [str(a) for a in args]
        from auto_editor.__main__ import main as ae_main
        with contextlib.redirect_stdout(saida), contextlib.redirect_stderr(erro):
            try:
                ae_main()
            except SystemExit as e:
                codigo = int(e.code or 0)
    except Exception as e:                                   # noqa: BLE001
        codigo = 1
        erro.write("auto-editor embutido falhou: %r" % (e,))
    finally:
        sys.argv = argv_antigo
        try:
            os.chdir(cwd_antigo)
        except OSError:
            pass
    return _Resultado(codigo, saida.getvalue(), erro.getvalue())


def _limpar_ponte_velha(base):
    """Apaga o auto-editor.bat da tentativa reprovada, se ele sobrou."""
    velho = os.path.join(base, "auto-editor.bat")
    try:
        if os.path.isfile(velho):
            with open(velho, encoding="utf-8", errors="replace") as f:
                if "veo_exe" in f.read():          # so' o NOSSO, nunca outro
                    os.remove(velho)
    except OSError:
        pass


def main():
    if not getattr(sys, "frozen", False):
        import runpy
        runpy.run_module("app", run_name="__main__")
        return

    # o auto_editor usa multiprocessing; congelado ele precisa disto ANTES
    # de qualquer pool, senao o Windows re-executa o .exe do zero.
    import multiprocessing
    multiprocessing.freeze_support()

    # ⛔ O CONSOLE PRETO QUE APARECIA NO MEIO DA EDICAO.
    # O `auto_editor.__main__` nao faz o trabalho em Python: ele re-executa
    # um `auto-editor.exe` PROPRIO de 37 MB que vem dentro do pacote
    # (`subprocess.run([binary_path] + argv)`, sem creationflags). Rodar o
    # main "no mesmo processo" so' chegava ate' o Python dele — o binario
    # ainda nascia com console.
    # ⭐ Como o editor nao controla essa chamada, a flag e' imposta no
    # `subprocess.Popen` INTEIRO: todo processo filho deste .exe nasce sem
    # janela. `subprocess.run` tambem passa por aqui, entao cobre os dois.
    # ⚠️ So' quando CONGELADO. Pelo .bat com venv o console e' util para ver
    # erro, e nada disto roda.
    if os.name == "nt":
        import subprocess as _sp
        _CNW = getattr(_sp, "CREATE_NO_WINDOW", 0x08000000)
        _PopenOriginal = _sp.Popen

        class _PopenSemJanela(_PopenOriginal):
            def __init__(self, *a, **kw):
                kw["creationflags"] = kw.get("creationflags", 0) | _CNW
                _PopenOriginal.__init__(self, *a, **kw)

        _sp.Popen = _PopenSemJanela

    base = os.path.dirname(os.path.abspath(sys.executable))
    os.environ.setdefault("VEO_EDITOR_BASE", base)          # (1)
    _limpar_ponte_velha(base)

    import pipeline                                          # (2)
    pipeline.AUTO_EDITOR = SENTINELA_AE
    _run_original = pipeline._run

    def _run_remendado(cmd, cwd=None):
        if cmd and cmd[0] == SENTINELA_AE:
            r = _rodar_auto_editor(list(cmd[1:]), cwd)
            if r.returncode != 0:
                raise RuntimeError(
                    "comando falhou (auto-editor embutido):\n%s"
                    % (r.stderr or r.stdout)[-1800:])
            return r
        return _run_original(cmd, cwd)

    pipeline._run = _run_remendado

    import runpy
    runpy.run_module("app", run_name="__main__")


if __name__ == "__main__":
    main()
