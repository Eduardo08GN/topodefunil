# -*- coding: utf-8 -*-
"""Ponto de entrada do .exe do Veo Editor CTA FIXO.

⛔ ESTE ARQUIVO SO' EXISTE POR CAUSA DO CONGELAMENTO. Rodando pelo `.bat` com
   o venv, nada aqui e' usado — o `app.py` e' chamado direto. Ele existe para
   nao editar `app.py`, `esteira.py` nem `pipeline.py`, que estao em
   desenvolvimento ativo pelo outro autor: mexer neles renderia conflito a cada
   commit dele. Todo desvio mora aqui, de fora.

Dois defeitos que o `--onefile` do PyInstaller cria neste app, e o conserto:

1. AS PASTAS DA ESTEIRA SUMIAM COM O VIDEO DENTRO.
   `esteira.py` ancora tudo em
       BASE = os.environ.get("VEO_EDITOR_BASE") or dirname(abspath(__file__))
   e congelado o `__file__` aponta para a pasta temporaria `_MEIPASS`, que o
   Windows APAGA ao fechar o app. `01_entrada` ate `05_erros`, o
   `historico.csv` e todo video pronto nasceriam la' dentro e evaporariam.
   ⭐ O proprio autor deixou a saida pronta: a variavel `VEO_EDITOR_BASE`.
   Basta preenche-la antes de importar, e nenhuma linha dele muda.

2. O AUTO-EDITOR NAO SERIA ENCONTRADO.
   `pipeline._auto_editor()` procura o binario ao lado de `sys.executable` e,
   falhando, no PATH. Congelado, `sys.executable` e' o proprio `.exe` e o
   `auto-editor` so' existe dentro do venv — que o `.exe` existe justamente
   para dispensar. O passo de tirar silencio quebraria.
   ⭐ Conserto: o pacote `auto_editor` vai DENTRO do bundle, e o `.exe` vira
   seu proprio auto-editor quando chamado com `--__auto_editor`. Um `.bat` de
   uma linha ao lado do executavel faz a ponte, porque o codigo do autor monta
   o comando como `[AUTO_EDITOR, entrada, ...]` — uma string so', que nao
   comporta o argumento extra.

⚠️ O `.bat` e' reescrito a cada abertura de proposito: se o `.exe` for
   renomeado ou movido, a ponte se conserta sozinha na abertura seguinte.
"""

import os
import sys

SENTINELA = "--__auto_editor"


def _despachar_auto_editor():
    """O .exe fazendo de auto-editor. Chamado pela ponte .bat."""
    sys.argv = ["auto-editor"] + sys.argv[2:]
    from auto_editor.__main__ import main
    raise SystemExit(main())


def _ponte_auto_editor(base):
    """Escreve o .bat ao lado do .exe e devolve o caminho dele."""
    caminho = os.path.join(base, "auto-editor.bat")
    conteudo = (
        "@echo off\r\n"
        'REM Ponte gerada pelo veo_exe.py. O .exe faz de auto-editor.\r\n'
        'REM Nao editar: e reescrito a cada abertura do app.\r\n'
        '"%s" %s %%*\r\n' % (sys.executable, SENTINELA)
    )
    try:
        atual = ""
        if os.path.isfile(caminho):
            with open(caminho, encoding="utf-8") as f:
                atual = f.read()
        if atual != conteudo:
            with open(caminho, "w", encoding="utf-8") as f:
                f.write(conteudo)
    except OSError as e:
        print("[ponte] nao consegui escrever %s: %s" % (caminho, e), flush=True)
        return None
    return caminho


def main():
    congelado = getattr(sys, "frozen", False)

    if congelado and len(sys.argv) > 1 and sys.argv[1] == SENTINELA:
        _despachar_auto_editor()
        return

    if congelado:
        base = os.path.dirname(os.path.abspath(sys.executable))
        # (1) ancora a esteira na pasta do .exe, nao na temporaria
        os.environ.setdefault("VEO_EDITOR_BASE", base)

        # (2) ponte do auto-editor, montada ANTES de importar o pipeline,
        #     porque `AUTO_EDITOR` e' resolvido no import dele
        ponte = _ponte_auto_editor(base)
        import pipeline
        if ponte:
            pipeline.AUTO_EDITOR = ponte

    # ⛔ `import app` NAO abre a janela: o app.py nao tem funcao main(), tudo
    #    mora sob `if __name__ == "__main__"` — inclusive a TRAVA DE INSTANCIA
    #    UNICA e o foco da janela ja' aberta. Importado como modulo comum, o
    #    .exe abriria e fecharia sem desenhar nada. runpy executa o modulo com
    #    o nome __main__, entao aquele bloco roda inteiro, igual ao .bat.
    import runpy
    runpy.run_module("app", run_name="__main__")


if __name__ == "__main__":
    main()
