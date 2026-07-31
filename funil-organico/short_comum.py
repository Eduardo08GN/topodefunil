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


def bancada_com_rosto(base, spec, fala, n=3, total=3):
    """A cena do ritual COM O ROSTO em quadro — recombinacao, nao invencao.

    ⚠️ Ordem do operador, 2026-07-31: "rosto aparente enquanto prepara".

    No FLAGRANTE e no PEE a cena do ritual e' um **insert de maos**: a string
    travada diz literalmente `A pair of hands ... No face in frame`. Serve
    quando ela e' a terceira de cinco cenas e o rosto ja' apareceu antes e
    depois. Nao serve como cena 3 de tres, que e' onde mora o CTA: `follow me
    first` e' um pedido, e pedido sem cara nao converte.

    Esta funcao monta a cena que faltava **sem inventar nada** — cada pedaco
    vem de um bloco ja' validado em render:

      · o SET e a BANCADA .... da cena 2 (`amb["set"]`, `amb["bancada"]`)
      · a PESSOA ............. da cena 2, mesma construcao e mesmos campos
      · a ACAO ............... da cena 3 (sache, copo d'agua, colher, girar)
      · a LUZ e a CAUDA ...... dos dois
      · "His hands work while he talks" / "His eyes stay on the lens the whole
        time" .... copiado literal do TAKE 03 do NECROSE, que ja' roda com
        rosto em quadro e passou em render

    ⛔ Isto vive SO' no SHORT. O motor longo continua com o insert de maos —
    la' a regra dele esta' certa.
    """
    et = base.ETNIA[spec["pagina"]]
    ref, amb = spec["ref"], spec["ambiente"]
    luz = amb["luz"]

    img = (
        "IMAGE %02d/%02d: Medium shot in %s. The same %d-year-old %s man, %s, "
        "%s, stands behind the %s, speaking to the camera. On the counter in "
        "front of him are an open white sachet, a glass of water and a spoon, "
        "and both his hands are at the glass mid-action. He is alone in frame. "
        "%s %s"
        % (n, total, amb["set"], ref["idade"], et, ref["marca"],
           ref["roupa_curta"], amb["bancada"], luz.capitalize(), base.CAUDA)
    )
    take = (
        "TAKE %02d/%02d: Animate the image exactly. Handheld iPhone, slight "
        "sway, no cuts. His hands work while he talks: he finishes pouring the "
        "sachet into the glass and stirs it in slow circles. His eyes stay on "
        "the lens the whole time. He is alone in the shot.\n"
        "Dialogue: \"%s\"\n"
        "Audio: spoon clinking glass, quiet room tone. No music."
        % (n, total, base.sonorizar(fala))
    )
    return img, take


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

    # ⛔ ANCORA DE CONTINUIDADE. Toda cena depois da primeira que mostra o
    # homem tem de dize-lo com "the same N-year-old ... man". Sem isso o Veo
    # desenha OUTRA pessoa: no VAZAMENTO a ancora estava na camisa ("wearing
    # the same shirt") e o render devolveu um senhor de oculos e bigode no
    # lugar do corpo-prova — e como o TAKE diz "Only he speaks", o estranho
    # falava a fala do REF. Relatado em producao, 2026-07-31.
    # O insert de maos nao entra: ele nao mostra pessoa nenhuma.
    for nome in sorted(k for k in blocos if k.startswith("IMAGE")):
        if nome.endswith("01/03"):
            continue
        txt = blocos[nome]
        if re.search(r"\d+-year-old[^.]{0,40}\bman\b", txt) and \
                not re.search(r"the same \d+-year-old", txt, re.I):
            achados.append(("ERRO", "%s mostra o homem sem a ancora 'the same "
                                    "N-year-old ... man' — o Veo troca de "
                                    "pessoa e o estranho fala a fala do REF"
                            % nome))

    for f in extras:
        f(spec, blocos, achados)

    return achados


# ---------------------------------------------------------------------------
# SORTEIO
# ---------------------------------------------------------------------------

def sortear_curto(base, pagina, rng, ledger, mapa, fundir, mapa_copy=None):
    """Sorteia pelo motor base e colapsa as 5 falas em 3.

    `fundir(spec, rng)` devolve a fala da cena 2 do SHORT — a fundida. As
    outras duas sao as originais, intactas: elas ja' foram validadas em campo
    e nao ha' motivo para reescreve-las.

    ⭐ `mapa` e `mapa_copy` sao COISAS DIFERENTES, e essa separacao e' o que
    permite aproveitar os 22 segundos:

        mapa      — de qual cena do base vem a IMAGEM e a direcao de cena
        mapa_copy — de qual cena do base vem a FALA

    Sem ela, a cena 3 do SHORT so' podia ser o close do CTA: fala de CTA
    obrigava imagem de CTA. Com ela, a fala do CTA pode rodar por cima da
    bancada do ritual — o espectador OUVE o pedido e VE o gelatin trick nos
    mesmos 8 segundos, em vez de olhar um talking head por um terco do video.
    """
    mapa_copy = mapa_copy or mapa
    spec = base.sortear(pagina, rng, ledger)
    spec["falas_base"] = list(spec["falas"])
    spec["falas"] = [spec["falas_base"][mapa_copy[0] - 1],
                     fundir(spec, rng),
                     spec["falas_base"][mapa_copy[2] - 1]]
    return spec


def nova_fala_curta(base, spec, i, rng, mapa, fundir, mapa_copy=None):
    """Re-sorteia a fala da cena i (0-2) do SHORT.

    As pontas delegam ao motor base — o hook e o CTA sao os mesmos pools de
    sempre. So' o meio e' proprio do SHORT.
    """
    if i == 1:
        return fundir(spec, rng)
    mapa_copy = mapa_copy or mapa
    return base.nova_fala(espelho(spec, mapa), mapa_copy[i] - 1, rng)


def orgao_de(base, fala, padrao="Johnson"):
    """O substantivo-nucleo que ja' esta' naquela fala (a rotacao e' do video)."""
    baixo = fala.lower()
    return next((n for n in base.NUCLEO if n.lower() in baixo), padrao)
