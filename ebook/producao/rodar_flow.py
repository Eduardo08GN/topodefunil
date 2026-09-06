# -*- coding: utf-8 -*-
# Loader ASCII para rodar o `gerar_fotos_flow.py` dentro do browser-harness.
#
# ⛔ POR QUE ELE EXISTE: o stdin do harness nao garante UTF-8. Um script com
# simbolos fora do ASCII no docstring, piped direto, morre em
# UnicodeEncodeError antes de executar uma linha. Este loader e' ascii puro e
# abre o arquivo de verdade com encoding explicito.
#
#   BH_SCRIPT=<caminho absoluto de gerar_fotos_flow.py> #   BH_PROMPTS=prompts.json BH_OUT=fotos browser-harness < rodar_flow.py
import io, os
p = os.environ["BH_SCRIPT"]
exec(compile(io.open(p, encoding="utf-8").read(), p, "exec"), globals())
