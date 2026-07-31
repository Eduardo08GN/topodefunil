#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Maquinaria compartilhada dos agentes SHORT — 3 cenas de 8s.

POR QUE DERIVAR EM VEZ DE COPIAR
--------------------------------
Um `<agente>_short.py` NAO e' uma copia do motor base. Ele **importa** o base e
so' declara o que muda: quais cenas sobrevivem, a copy fundida da cena 2, os
tetos e os rotulos. Todas as strings travadas, pools de eixo, tabelas de token
banido e regras de doutrina continuam morando num lugar so'.

E' a mesma regra P9 da UI compartilhada: copia envelhece e mente. Se o D1 for
corrigido no motor base, o SHORT ja' nasce corrigido — sem ninguem lembrar.

O COLAPSO
---------
    base 1  ->  SHORT 1   (o hook — o bit visual que segura o scroll)
    base 4  ->  SHORT 2   (o payoff. A copy e' RITUAL + PROVA fundidos)
    base 5  ->  SHORT 3   (o CTA — travado em GELATIN pela automacao DM)

⚠️ **A imagem da cena 2 e' a do PAYOFF, nao a do ritual.** A copy fundida
termina em deitico ("came back like this"), e esse "this" precisa ter no que
apontar. O ritual vive na fala; o resultado, no quadro. Nenhuma cena nova e'
inventada — so' sobrevivem as ja' validadas em render.

⛔ O LITERAL `gelatin trick` — a armadilha deste formato
-------------------------------------------------------
Ele mora em cenas DIFERENTES em cada agente: NECROSE nas RECEITAS_FALA (3),
FLAGRANTE nas DESCOBERTAS (2), PEE nos RITUAIS (3), VAZAMENTO nas VIRADAS (3).
Todas caem no colapso. Sem ele o criativo deixa de ser congruente com o que a
VSL vende — que e' regra inviolavel, nao preferencia.

Por isso **a copy fundida da cena 2 carrega o literal obrigatoriamente**, e o
linter do SHORT trava nisso. Mesmo raciocinio para o MUP (`blood flow`) e, no
VAZAMENTO, para a negacao `without the gelatin trick`.
"""

import re


# ---------------------------------------------------------------------------
# GERADOR
# ---------------------------------------------------------------------------

def espelho(spec, mapa):
    """O spec do SHORT no formato que o motor base espera (5 falas).

    As 3 falas do SHORT voltam para as posicoes de origem; as duas cenas que
    nao sobrevivem mantem a fala original do sorteio. Serve tanto para chamar
    `base.montar()` quanto `base.nova_fala()` sem duplicar nada deles.
    """
    cheio = dict(spec)
    f5 = list(spec["falas_base"])
    for novo, orig in enumerate(mapa):
        f5[orig - 1] = spec["falas"][novo]
    cheio["falas"] = f5
    return cheio


def montar_curto(base, spec, mapa):
    """Roda o montar() do motor base e devolve so' as cenas do mapa, /03."""
    b5 = base.montar(espelho(spec, mapa))

    b = {"BLOCO 0 (REF)": b5["BLOCO 0 (REF)"]}
    for novo, orig in enumerate(mapa, 1):
        for tipo in ("IMAGE", "TAKE"):
            velho = "%s %02d/05" % (tipo, orig)
            chave = "%s %02d/03" % (tipo, novo)
            b[chave] = b5[velho].replace("%s %02d/05:" % (tipo, orig),
                                         "%s %02d/03:" % (tipo, novo), 1)
    return b


def bloco_base(blocos, mapa, tipo, cena_base):
    """O bloco do SHORT que corresponde a uma cena do motor base.

    Escrever `blocos["IMAGE 04/05"]` numa regra de linter do SHORT nao acha
    nada — a cena 4 virou 02/03. Este helper faz a traducao, para que as
    regras continuem sendo escritas em termos da cena ORIGINAL, que e' como a
    doutrina fala delas (NE11 = "a cena 4 e o geoduck").
    """
    return blocos["%s %02d/03" % (tipo, mapa.index(cena_base) + 1)]


# ---------------------------------------------------------------------------
# LINTER
# ---------------------------------------------------------------------------

def lint_curto(base, spec, blocos, mapa, teto_fala, literais=(),
               limpar_direcao=None, extras=(), cota_min=2, teto_total=None):
    """As regras que valem para qualquer SHORT de 3 cenas.

    Reusa as TABELAS do motor base (BANIDOS_*), nunca as reescreve. O que muda
    e' so' o alcance: 3 cenas em vez de 5, e a cota proporcional.

    literais       — strings que TEM de aparecer no corpo das 3 falas
                     (o `gelatin trick`, o MUP, a negacao do VAZAMENTO...)
    limpar_direcao — f(spec, texto) que tira da varredura o que da' falso
                     positivo (o animal do NECROSE, p.ex.)
    extras         — [f(spec, blocos, achados)] com as regras do agente
    """
    achados = []
    falas = spec["falas"]
    # o teto do video e' a soma dos tetos das cenas — um numero magico aqui
    # criaria uma segunda verdade que envelhece sozinha
    if teto_total is None:
        teto_total = sum(teto_fala.values())

    # o bloco 0 tem de carregar o cabecalho REF (contrato do parser do AdBatch)
    if not blocos.get("BLOCO 0 (REF)", "").lstrip().upper().startswith("REF"):
        achados.append(("ERRO", "BLOCO 0 sem o cabecalho REF: o AdBatch "
                                "descarta a referencia em silencio"))

    # cota do orgao, rotacionada. 2 de 3 e' o equivalente proporcional do
    # 4 de 5 da versao longa — 3 de 3 viraria bordao em 24 segundos.
    cenas, usados = [], []
    for i, fala in enumerate(falas, 1):
        baixo = fala.lower()
        hit = next((n for n in base.NUCLEO if n.lower() in baixo), None)
        if hit:
            cenas.append(i)
            usados.append(hit)
    if len(cenas) < cota_min:
        achados.append(("ERRO", "cota do orgao: %d/3 (minimo %d). Cenas sem "
                                "substantivo do nucleo: %s"
                        % (len(cenas), cota_min,
                           [i for i in (1, 2, 3) if i not in cenas])))
    if len(set(usados)) < len(usados):
        achados.append(("AVISO", "substantivo repetido no video: %s"
                        % sorted({u for u in usados if usados.count(u) > 1})))

    # tetos
    total = 0
    for i, fala in enumerate(falas, 1):
        n = base._palavras(fala)
        total += n
        if n > teto_fala[i]:
            achados.append(("AVISO", "cena %d com %d palavras (teto %d) — cortar "
                                     "UMA frase, nao reescrever menor"
                            % (i, n, teto_fala[i])))
    if total > teto_total:
        achados.append(("AVISO", "video com %d palavras (alvo ~60-%d)"
                        % (total, teto_total)))

    corpo = " ".join(falas).lower()

    # ⛔ os literais que o colapso ameaca: o `gelatin trick` cai junto com as
    # cenas 2 e 3 em TODOS os agentes. Sem ele nao ha' congruencia com a VSL.
    for lit in literais:
        if lit.lower() not in corpo:
            achados.append(("ERRO", "expressao literal '%s' ausente — ela morava "
                                    "numa cena que o SHORT nao tem, e precisa "
                                    "vir na copy fundida" % lit))

    # CTA — a cena 3 do SHORT e' a cena 5 do base, mesmas travas
    cta = falas[2]
    if "gelatin" not in cta.lower():
        achados.append(("ERRO", "CTA da cena 3 sem a keyword GELATIN"))
    if "GELATIN" in cta:
        achados.append(("ERRO", "keyword em CAIXA ALTA no Dialogue: — em ALL "
                                "CAPS o Veo soletra; usar 'gelatin'"))
    if "gelatin," not in cta and "gelatin." not in cta:
        achados.append(("ERRO", "keyword sem virgula depois — sem a micro-pausa "
                                "o Veo emenda e narra 'gelatine'"))
    for tok, motivo in base.BANIDOS_CTA.items():
        if re.search(r"\b%s\b" % tok, cta):
            achados.append(("ERRO", "CTA usa '%s' — %s" % (tok, motivo)))

    # tokens banidos por bloco (so' na DIRECAO de cena, nunca na fala)
    globais = [t for t in ("BANIDOS_CATEGORIA", "BANIDOS_ANIMAL", "BANIDOS_GLOBAL",
                           "BANIDOS_VAZAMENTO", "BANIDOS_FONTE")
               if hasattr(base, t)]
    for nome, txt in blocos.items():
        direcao = txt.split(chr(10) + "Dialogue:")[0]
        if limpar_direcao:
            direcao = limpar_direcao(spec, direcao)
        baixo = direcao.lower()
        tabela = base.BANIDOS_TAKE if nome.startswith("TAKE") else base.BANIDOS_IMAGE
        for tok, motivo in tabela.items():
            if re.search(r"\b%s\b" % tok, baixo):
                achados.append(("ERRO", "%s contem '%s' — %s" % (nome, tok, motivo)))
        for t in globais:
            for tok, motivo in getattr(base, t).items():
                if tok in baixo:
                    achados.append(("ERRO", "%s contem '%s' — %s" % (nome, tok, motivo)))

    for f in extras:
        f(spec, blocos, achados)

    return achados


# ---------------------------------------------------------------------------
# SORTEIO
# ---------------------------------------------------------------------------

def sortear_curto(base, pagina, rng, ledger, mapa, fundir):
    """Sorteia pelo motor base e colapsa as 5 falas em 3.

    `fundir(spec, rng)` devolve a fala da cena 2 do SHORT — a fundida. As
    outras duas sao as originais das cenas do mapa, intactas: elas ja' foram
    validadas em campo e nao ha' motivo para reescreve-las.
    """
    spec = base.sortear(pagina, rng, ledger)
    spec["falas_base"] = list(spec["falas"])
    spec["falas"] = [spec["falas_base"][mapa[0] - 1],
                     fundir(spec, rng),
                     spec["falas_base"][mapa[2] - 1]]
    return spec


def nova_fala_curta(base, spec, i, rng, mapa, fundir):
    """Re-sorteia a fala da cena i (0-2) do SHORT.

    As pontas delegam ao motor base — o hook e o CTA sao os mesmos pools de
    sempre. So' o meio e' proprio do SHORT.
    """
    if i == 1:
        return fundir(spec, rng)
    return base.nova_fala(espelho(spec, mapa), mapa[i] - 1, rng)


def orgao_de(base, fala, padrao="Johnson"):
    """O substantivo-nucleo que ja' esta' naquela fala (a rotacao e' do video)."""
    baixo = fala.lower()
    return next((n for n in base.NUCLEO if n.lower() in baixo), padrao)
