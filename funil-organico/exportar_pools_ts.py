#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
EXPORTADOR DE POOLS — Python -> JSON, para o porte TypeScript do micro-SaaS OW.

⛔⛔ POR QUE ESTA FERRAMENTA EXISTE, e por que ela nao e' opcional.

O micro-SaaS do cliente OrganicWave reescreve dois motores em TypeScript
(decisao do operador, 2026-08-14). A doutrina do repo proibe **redigitar string
validada**: *"String validada e' constante, nunca redigitada — comprimir o D1 na
mao ja' entregou esqueleto 3D no lugar da placa em corte."*

Um porte feito a mao redigitaria ~1.800 linhas de pool. Este script tira a mao
humana do caminho: ele IMPORTA o motor e despeja as constantes como JSON, byte
por byte iguais ao que o Python sorteia hoje. O TypeScript reimplementa so' a
LOGICA (sortear/montar), que e' codigo e nao copy.

⚠️ E ELE E' DE MAO UNICA, DE PROPOSITO. O operador declarou o fork em
2026-08-14: *"qualquer alteracao que fizer nos meus exes, agentes, trate como se
nem houvesse essa guia; e qualquer pedido de alteracao nos agentes16OW, vc
alterara o typescript"*. Entao este script serve o BOOTSTRAP e as vezes em que
ELE mandar re-sincronizar. Ele nao roda sozinho, nao entra em hook, e nao volta
do TS para o Python.

USO
    python funil-organico/exportar_pools_ts.py \
        --motor organicwave16_short --destino <pasta>
    python funil-organico/exportar_pools_ts.py --tudo

O QUE SAI
    <destino>/pools.json   todas as constantes MAIUSCULAS serializaveis
    <destino>/meta.json    o contrato de UI que o `ui_agente` le' por getattr

⚠️ O QUE NAO SAI, e por que nao pode sair calado: funcoes, regexes compilados,
modulos e qualquer objeto nao serializavel. Cada descarte e' LISTADO no stdout —
descarte silencioso aqui viraria pool faltando no produto do cliente, e ninguem
notaria ate' o aluno gerar um video sem o beat.
"""

import argparse
import importlib
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

# ⛔ Os dois agentes que o operador escolheu para o micro-SaaS (2026-08-14).
MOTORES = {
    "organicwave16": "organicwave16_short",
    "clean16": "clean_v2_16s_short",
}

# O contrato que o `ui_agente` le' por `getattr(motor, nome, default)`. Sao
# estes nomes que a tela do SaaS precisa para se desenhar sozinha, do mesmo
# jeito que o tkinter se desenha.
CONTRATO_UI = (
    "TITULO", "SUBTITULO", "SLUG", "CENAS_UI", "TETO_FALA", "PISO_FALA",
    "ETNIA", "ETNIAS", "SEXOS", "EIXOS_UI", "TRAVAS_UI", "EIXOS_TRAVAVEIS",
    "DROPDOWNS_UI", "PELE_TRAVAVEL", "MODOS_DEFAULT", "IGNORA_PAINEL",
    "ROTULO_FORMATA_O", "MODO_BELA", "MODO_FORTE", "MODO_RECEITA",
    "MODO_LEVE", "MODO_PESSOA", "NUCLEO", "TETO_LEDGER",
)

RX_CONST = re.compile(r"^[A-Z][A-Z0-9_]*$")

# ⛔⛔ OS POOLS DOS MODOS NAO MORAM NO MOTOR — MORAM NO `short_comum`.
# O laco principal abaixo varre `dir(mod)` do MOTOR, e `sc.REFS_BELAS` /
# `sc.REFS_FORTES` nao aparecem la' (o motor importa o modulo como `sc`, que e'
# minusculo e nao casa o RX_CONST). Resultado, medido no porte do CLEAN V2 16s:
# o `pools.json` saia SEM uma unica entrada dos dois toggles, e o TypeScript
# teria de redigitar 94 + 34 entradas de pool a mao — exatamente o que este
# script existe para impedir.
#
# ⚠️ A exportacao e' CONDICIONADA A' FLAG do motor, nao incondicional: quem nao
# declara `MODO_BELA`/`MODO_FORTE` nao chama `ref_bela`/`ref_forte` e nao pode
# ganhar pool novo no JSON so' porque o extrator mudou. Medido: com esta regra o
# `organicwave16/pools.json` sai byte a byte igual ao de antes (ele nao declara
# nenhuma das duas flags), e so' o `clean16` ganha as chaves `SC_*`.
#
# ⚠️ O prefixo `SC_` nao e' enfeite: diz de onde a string veio. Um dia o
# `short_comum` pode ganhar um `REFS_BELAS` diferente do de um motor que declare
# o proprio, e sem o prefixo uma chave sobrescreveria a outra em silencio.
COMPARTILHADOS_MODO = {
    "MODO_BELA": ("REFS_BELAS", "OLHOS_BELAS", "ROUPAS_BELAS", "CORES_BELAS"),
    "MODO_FORTE": ("REFS_FORTES", "REFS_FORTES_MADUROS", "OLHOS_FORTES",
                   "ROUPAS_FORTES", "CORES_FORTES"),
}



def _serializavel(v):
    """Converte o que da', devolve `None` (e o motivo) para o que nao da'."""
    if isinstance(v, (str, int, float, bool)) or v is None:
        return v, None
    if isinstance(v, (list, tuple)):
        fora = []
        for x in v:
            conv, motivo = _serializavel(x)
            if motivo:
                return None, "item: %s" % motivo
            fora.append(conv)
        return fora, None
    if isinstance(v, set):
        # ⚠️ set nao tem ordem estavel entre execucoes do Python. Ordenar aqui
        # e' o que impede o JSON de mudar sozinho de um build para o outro.
        try:
            return sorted(v), None
        except TypeError:
            return None, "set heterogeneo"
    if isinstance(v, dict):
        fora = {}
        for k, x in v.items():
            if not isinstance(k, (str, int)):
                return None, "chave %r nao e' str/int" % (k,)
            conv, motivo = _serializavel(x)
            if motivo:
                return None, "valor de %r: %s" % (k, motivo)
            fora[str(k)] = conv
        return fora, None
    return None, type(v).__name__


def exportar(nome_curto, modulo, destino):
    mod = importlib.import_module(modulo)
    pools, meta, descartes = {}, {}, []

    for nome in sorted(dir(mod)):
        if not RX_CONST.match(nome):
            continue
        valor = getattr(mod, nome)
        conv, motivo = _serializavel(valor)
        if motivo:
            descartes.append((nome, motivo))
            continue
        pools[nome] = conv
        if nome in CONTRATO_UI:
            meta[nome] = conv

    # ⭐ Os pools dos MODOS, que vem do `short_comum` e nao do motor — ver a
    # nota do COMPARTILHADOS_MODO. ⛔ Falta de pool aqui e' DESCARTE LISTADO,
    # nunca silencio: se `short_comum` renomear um pool, o porte TS ficaria com
    # o toggle ligado e o pool vazio, e o aluno receberia um prompt com o campo
    # em branco em vez de um erro.
    sc = importlib.import_module("short_comum")
    for flag, nomes in sorted(COMPARTILHADOS_MODO.items()):
        if not getattr(mod, flag, False):
            continue
        for nome in nomes:
            valor = getattr(sc, nome, None)
            if valor is None:
                descartes.append(("SC_" + nome, "ausente em short_comum"))
                continue
            conv, motivo = _serializavel(valor)
            if motivo:
                descartes.append(("SC_" + nome, motivo))
                continue
            pools["SC_" + nome] = conv

    # ⚠️ o contrato de UI que o motor NAO declara e' informacao, nao ausencia:
    # a tela do SaaS decide o que desenhar por presenca, igual ao tkinter.
    meta["_ausentes"] = [n for n in CONTRATO_UI if n not in meta]
    meta["_motor"] = modulo
    meta["_agente"] = nome_curto

    if not os.path.isdir(destino):
        os.makedirs(destino)
    for arquivo, dados in (("pools.json", pools), ("meta.json", meta)):
        caminho = os.path.join(destino, arquivo)
        with open(caminho, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=1, sort_keys=True)
            f.write("\n")

    total = sum(len(v) if isinstance(v, (list, dict)) else 1
                for v in pools.values())
    print("%-14s %-22s %3d constantes, %5d entradas -> %s"
          % (nome_curto, modulo, len(pools), total, destino))
    if descartes:
        print("   descartados (nao serializaveis):")
        for n, motivo in descartes:
            print("     %-22s %s" % (n, motivo))
    if meta["_ausentes"]:
        print("   sem declarar no contrato de UI: %s"
              % ", ".join(meta["_ausentes"]))
    return pools


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--motor", choices=sorted(MOTORES))
    ap.add_argument("--destino")
    ap.add_argument("--tudo", action="store_true")
    ap.add_argument("--raiz",
                    default=r"C:\Users\edlut\projetosweb\automaweb\src\lib\agentes",
                    help="pasta do porte TS no repo do cliente")
    a = ap.parse_args()

    if a.tudo:
        for curto, modulo in sorted(MOTORES.items()):
            exportar(curto, modulo, os.path.join(a.raiz, curto))
        return
    if not a.motor:
        ap.error("informe --motor ou --tudo")
    destino = a.destino or os.path.join(a.raiz, a.motor)
    exportar(a.motor, MOTORES[a.motor], destino)


if __name__ == "__main__":
    main()
