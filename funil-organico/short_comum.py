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
      · "His hands stir the spoon while he talks" / "His eyes stay on the lens
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
        "sway, no cuts. His hands stir the spoon while he talks, tipping the "
        "sachet into the glass and stirring it in slow circles. His eyes stay on "
        "the lens the whole time. He is alone in the shot.\n"
        "Dialogue: \"%s\"\n"
        "Audio: spoon clinking glass, quiet room tone. No music."
        % (n, total, base.sonorizar(fala))
    )
    return img, take


def redencao_com_ref(base, spec, fala, n=2, total=3):
    """A redencao COM O NARRADOR em quadro — recombinacao, nao invencao.

    ⚠️ Ordem do operador, 2026-07-31.

    No FLAGRANTE e no PEE a cena da redencao mostra a VITIMA e a mulher; o
    narrador nao entra, e a fala dele roda em voiceover (`A man's voice speaks
    over the scene`). Isso funciona em 5 cenas, onde o REF aparece em 4 delas e
    some numa. **Em 3 cenas ele sumiria no terco do meio** — justo na cena da
    prova —, e o espectador perde a ancora de quem esta' falando com ele.

    Aqui o narrador volta ao quadro, exatamente como aparece na cena 1: ao
    fundo, atras do casal, falando para a camera. Cada pedaco vem de bloco
    validado:

      · o CASAL e o prop ereto ...... da cena 4 (`vit`, `mul`, `prop["ereto"]`)
      · o NARRADOR .................. da cena 1 e da 5, mesma construcao
      · a sala, a luz, a negacao de ave e a cauda ... da cena 4

    ⚠️ E o TAKE deixa de ser voiceover: agora quem fala esta' em quadro, entao
    diz `Only the man standing behind them speaks`. Sem isso a vitima dublaria
    a fala do narrador — a mesma falha que derrubou a cena do casal do
    VAZAMENTO.

    ⛔ Vive SO' no SHORT. O motor longo mantem o voiceover, que la' esta' certo.
    """
    et = base.ETNIA[spec["pagina"]]
    ref, vit, mul = spec["ref"], spec["vitima"], spec["mulher"]
    prop, amb = spec["prop"], spec["ambiente"]
    neg = base.NEGACAO_AVE if prop["marisco"] else ""

    img = (
        "IMAGE %02d/%02d: Medium shot in a plain living room, %s The same "
        "%d-year-old %s %s, now in a clean white shirt, sits in an armchair "
        "grinning, head up. A %d-year-old %s woman %s sits sideways on his "
        "knee, arm around him, laughing. In her free hand she holds %s. "
        "Standing behind the armchair, facing the camera and speaking, is the "
        "same %d-year-old %s man, %s, the one from the first scene.%s %s"
        % (n, total, amb["luz"], vit["idade"], et, vit["marca"],
           mul["idade"], et, mul["payoff"], prop["ereto"],
           ref["idade"], et, ref["marca"], neg, base.CAUDA)
    )
    take = (
        "TAKE %02d/%02d: Animate the image exactly. Handheld iPhone, slight "
        "sway, no cuts. The seated man laughs silently, head tipping back. The "
        "woman laughs, tightens her arm around him; her other hand stays "
        "exactly where it is, holding it motionless the entire shot. Neither "
        "of them changes position. Only the %d-year-old man standing behind "
        "them speaks, straight into the lens; the couple stays silent.\n"
        "Dialogue: \"%s\"\n"
        "Audio: quiet room tone, soft laughter. No music."
        % (n, total, ref["idade"], base.sonorizar(fala))
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
               limpar_direcao=None, extras=(), cota_min=2, teto_total=None,
               objetos_ok=()):
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

    # ⛔ valem para TODO agente SHORT, sem excecao — inclusive os que ainda
    # vao nascer (ordem do operador, 2026-08-02)
    lint_sem_texto(blocos, achados)
    # ⛔⛔ 2026-08-05: TAKE contra IMAGE. Vale para TODO agente SHORT, inclusive
    # os que ainda vao nascer. `objetos_ok` deixa o motor declarar as excecoes
    # que ele CONFERIU — e declarar excecao e' declarar que alguem olhou.
    lint_take_vs_image(blocos, achados, objetos_ok)
    if falas:
        lint_isca_cta(falas[-1], achados, "a cena 3 (CTA)")
        lint_cta_literal(falas[-1], achados, "a cena 3 (CTA)")

    for f in extras:
        f(spec, blocos, achados)

    return achados


# ---------------------------------------------------------------------------
# SORTEIO
# ---------------------------------------------------------------------------

def sortear_curto(base, pagina, rng, ledger, mapa, fundir, mapa_copy=None,
                  travas=None):
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
    # ⛔ A TRAVA ATRAVESSA ATE' O MOTOR LONGO. Nos agentes derivados a REF e'
    # sorteada la' dentro, e sem repassar o dicionario o toggle acenderia e nao
    # mudaria nada — o botao que mente, que ja' me pegou tres vezes hoje.
    # ⚠️ ADITIVO: motor longo que nao aceita `travas` continua sendo chamado com
    # tres argumentos, entao nada muda para quem nao declara o contrato.
    if travas:
        try:
            spec = base.sortear(pagina, rng, ledger, travas)
        except TypeError:
            spec = base.sortear(pagina, rng, ledger)
    else:
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


# ---------------------------------------------------------------------------
# ⛔ NADA DE TEXTO QUEIMADO NO VIDEO
# ---------------------------------------------------------------------------
# Achado em 2026-08-01, garimpando a Sofia Maren: os reels dela saem com o
# watermark `genaicontent` queimado no canto, vazado da ferramenta que ela usa.
# O operador viu e disse: "isso aqui nao e' pra aparecer nos nossos videos".
#
# Ao conferir, o buraco era nosso e era sistemico: o BLOCO 0 (REF) proibia
# texto ("No subtitles, no captions, no burned-in text, no watermark") e os
# IMAGE proibiam pela CAUDA — mas os TAKE, que sao os blocos que geram o
# VIDEO, nao diziam nada. Zero de 18 TAKEs nos seis motores SHORT. Imagem
# limpa nao impede o Veo de queimar legenda ou marca no movimento, e a legenda
# do nosso video nasce depois, no Veo Editor, a partir do Whisper — texto vindo
# do gerador entra por cima e nao ha como tirar.
#
# ⚠️ Entra ANTES do `Dialogue:`. Todas as diretivas de cena moram na prosa que
# antecede os campos estruturados; instrucao depois do `Audio:` fica orfa.
# ⚠️ Nao e' declaracao de conformidade (licoes-producao-veo §Declaracao e'
# municao): `not a celebrity` e `fully clothed` nomeiam a CATEGORIA que o
# classificador policia. Isto e' instrucao de RENDER, e e' a mesma string ja
# validada no BLOCO 0.
SEM_TEXTO_TAKE = "No on-screen text, no subtitles, no captions, no watermark."


def selar_tags(blocos):
    """Todo bloco IMAGE/TAKE comeca com o proprio nome. Idempotente.

    ⛔ Achado do operador em 2026-08-03, lendo o app: o CLEAN entregava os seis
    blocos SEM a tag — `Animate the provided image exactly...` em vez de
    `TAKE 03/03: Animate...`. Os outros nove motores traziam.

    POR QUE IMPORTA, e nao e' cosmetico: o AdBatch Vertical parseia o roteiro
    colado procurando os cabecalhos de bloco. Bloco sem tag ou entra no slot
    errado ou nao entra. E quando o operador copia os 3 IMAGE de uma vez, a tag
    e' a UNICA coisa que separa um do outro no texto corrido.

    ⚠️ `BLOCO 0 (REF)` fica de fora de proposito: la' a convencao e' `REF 01:`,
    que e' o que o AdBatch espera — nao o nome da chave.
    """
    for chave, txt in list(blocos.items()):
        if not chave.startswith(("IMAGE", "TAKE")):
            continue
        if txt.lstrip().startswith(chave):
            continue
        blocos[chave] = "%s: %s" % (chave, txt.lstrip())
    return blocos


def lint_tags(blocos, achados):
    """Guarda do contrato acima — sem isto ele sai de novo no proximo refactor."""
    for chave in sorted(blocos):
        if not chave.startswith(("IMAGE", "TAKE")):
            continue
        if not blocos[chave].lstrip().startswith(chave):
            achados.append(("ERRO", "%s nao comeca com a propria tag — o "
                                    "AdBatch parseia por cabecalho de bloco"
                            % chave))


def selar_takes(blocos):
    """Poe a trava de texto queimado em todo bloco TAKE. Idempotente."""
    for chave, txt in list(blocos.items()):
        if not chave.startswith("TAKE") or SEM_TEXTO_TAKE in txt:
            continue
        corte = txt.find("\nDialogue:")
        if corte == -1:                       # sem campo estruturado: vai no fim
            blocos[chave] = txt.rstrip() + " " + SEM_TEXTO_TAKE
        else:
            blocos[chave] = (txt[:corte].rstrip() + " " + SEM_TEXTO_TAKE
                             + txt[corte:])
    return blocos


# ---------------------------------------------------------------------------
# ⭐ A ISCA DO CTA — pedir sem oferecer nao faz ninguem comentar
# ---------------------------------------------------------------------------
# Ordem do operador, 2026-08-02, lendo o take 3 renderizado do ESCANDALO:
# "e' importante ter uma isca no mecanismo de copy falada na parte do cta, pois
# instiga e induz mais o telespectador a comentar: algo do tipo comente para
# receber {algo}". E, na mensagem seguinte: "isso tb vale pra qualquer outros
# agentes shorts que vc ira criar no futuro".
#
# Medido no dia: 22 CTAs em 7 agentes pediam o comentario sem dizer O QUE chega
# — "One word: gelatin, in the comments. That's the whole ask.", "Comment
# gelatin, and I'll take it from there.". O espectador e' convidado a pagar sem
# saber o que compra.
#
# ⚠️ POR QUE ISTO E' LINTER E NAO COMENTARIO: e' a terceira vez em dois dias que
# um slot passa no linter e nao cumpre a funcao pela qual existe (antes foram a
# prova que falava de preco e o mecanismo sem destino). O linter checava FORMA —
# placeholder, token banido, teto de palavras — e nunca checava FUNCAO. Regra
# verificavel por regex vira codigo; e' a doutrina do repo.
ISCA_CTA = re.compile(
    r"\b(recipe|measurements?|ingredients?|link|source|protocol)\b"
    r"|\bsend(?:ing)?\s+(?:you|it|them|over|the|all|my|that|what|where|how)\b"
    r"|\bi'?ll\s+(?:send|show|tell|write|give|walk|mail|text|dm)\b"
    r"|\b(?:in|to)\s+your\s+(?:inbox|messages|dm)\b"
    r"|\bwhere\s+to\s+(?:get|buy|find)\b|\bwhat\s+to\s+(?:buy|get|use)\b"
    r"|\bhow\s+much\b|\bthe\s+(?:exact|same|real|right)\s+one\b", re.I)


def lint_isca_cta(fala_cta, achados, rotulo="a cena do CTA"):
    """A fala que pede o comentario tem de dizer O QUE a pessoa recebe."""
    if not ISCA_CTA.search(fala_cta or ""):
        achados.append(("ERRO", "%s pede o comentario e nao diz o que chega — "
                                "sem isca o espectador nao tem por que comentar "
                                "(ordem do operador 2026-08-02)" % rotulo))


# ---------------------------------------------------------------------------
# ⛔⛔ O COMANDO DO CTA E' UM LITERAL: "Comment gelatin,"
# ---------------------------------------------------------------------------
# Ordem do operador, 2026-08-02, depois de ver videos renderizados com a
# legenda "COMMENT HONEY" e "COMMENT RECIPE": "Todos os agentes sem excecao,
# OBRIGATORIAMENTE devem ter a caption Comment Gelatin."
#
# ⚠️ POR QUE A LEGENDA DENUNCIA O AUDIO: a legenda do nosso video nasce no Veo
# Editor, do Whisper, EM CIMA DO AUDIO GERADO. Ela nao e' escrita por nos — ela
# e' a transcricao do que o modelo FALOU. Legenda errada significa fala errada,
# e fala errada quebra a automacao de DM, que so' responde a palavra exata.
#
# ⚠️ E POR QUE ISTO E' LITERAL E NAO "so' precisa conter gelatin": 14 dos 117
# CTAs pediam o comentario com outro verbo — "Type gelatin", "Say gelatin",
# "One word: gelatin", "Just the word gelatin". Variacao no comando e' margem
# para o modelo parafrasear, e parafrasear a keyword e' exatamente a falha que
# apareceu em campo. Um comando so', repetido em todo video, e' um token fixo
# que o modelo reproduz em vez de reinterpretar.
CTA_LITERAL = "Comment gelatin,"


def lint_cta_literal(fala_cta, achados, rotulo="a cena do CTA"):
    """O comando tem de ser o literal, sem variacao de verbo."""
    if CTA_LITERAL not in (fala_cta or ""):
        achados.append(("ERRO", "%s sem o literal %r — a legenda do video sai "
                                "do audio, e comando variavel faz o modelo "
                                "parafrasear a keyword (ordem do operador "
                                "2026-08-02)" % (rotulo, CTA_LITERAL)))


# ---------------------------------------------------------------------------
# ⛔ SE UMA CENA CRESCE, AS OUTRAS NAO CRESCEM
# ---------------------------------------------------------------------------
# Doutrina: RESSURREICAO §"Se a cena 1 cresce, nada cresce nas cenas 2 e 3", que
# declara literalmente "vira LINTER no short_comum.py e vale para todo SHORT que
# vier". Ate' 2026-08-02 a regra existia so' dentro do `ressurreicao_short.py` —
# o ponteiro da doutrina apontava para um arquivo que nao a tinha.
#
# O arco longo ja' proibe PICO2 da familia crescimento (o hook ja' cresceu; dois
# choques iguais somam a um). Em 24 segundos a regra fica mais dura: fora da
# cena que cresce, o prop e' OBJETO ESTATICO DECLARADO.
#
# ⚠️⚠️ POR QUE E' OPT-IN E NAO RODA SOZINHA DENTRO DO `lint_curto`: medido em
# 2026-08-02, 100 sorteios por motor. Ligada para todos, ela reprovaria
# ORGANICWAVE, FLAGRANTE, PEE, VAZAMENTO e NECROSE em **100% dos sorteios** —
# os cinco declaram o prop `stiff` no IMAGE do payoff, que la' e' o estado
# correto e validado em render. Linter que reprova tudo nunca foi testado
# (licoes-de-construcao §2), e ligar isto no automatico seria trocar um ponteiro
# morto por cinco motores quebrados. Quem cresce numa cena so' chama; os outros
# nao chamam.
CRESCIMENTO = re.compile(
    r"\b(grows?|growing|lengthens?|extends?|expands?|doubles?|swells?|swelling|"
    r"rises?|stiffens?|stiff|limp|sags?|erect|pulse|throb)\b", re.I)


def lint_nada_cresce(blocos, achados, excecao=(), rotulo="a regra"):
    """Vocabulario de crescimento fora dos blocos que tem licenca para cresce-lo.

    excecao — chaves de bloco onde crescer e' o trabalho (ex.: ("TAKE 01/03",)).
    ⚠️ So' varre a DIRECAO de cena: a fala nunca entra na varredura de token.
    """
    for nome in sorted(blocos):
        if nome in excecao or nome.startswith("BLOCO"):
            continue
        direcao = blocos[nome].split(chr(10) + "Dialogue:")[0]
        achado = sorted({m.group(0).lower()
                         for m in CRESCIMENTO.finditer(direcao)})
        if achado:
            achados.append(("ERRO", "%s: %s tem vocabulario de crescimento %s — "
                                    "so' a cena do bit visual cresce"
                            % (rotulo, nome, achado)))


# ---------------------------------------------------------------------------
# ⭐⭐ A BANDEIRA E' 50/50 — ordem do operador, 2026-08-04
# ---------------------------------------------------------------------------
# *"varie tb a presenca ou nao de bandeiras: todos os takes estao possuindo
#   bandeiras dos EUA, quero algo 50%/50% aparecendo, outra metade das
#   ocorrencias nao"*.
#
# ⛔ O ESTADO ANTERIOR ERA 100%, E POR CONSTRUCAO: a bandeira estava ESCRITA
# DENTRO da string de cada cenario (`...and a US flag on a floor stand in the
# corner`), em 4 motores — ESCANDALO, RESSURREICAO, TROCA e VAZAMENTO. Nao havia
# eixo para sortear; havia texto. O ESCANDALO ainda tinha um autoteste que
# EXIGIA a bandeira em 15/15 cenarios (ES13).
#
# ⚠️ POR QUE REMOCAO EXATA E NAO REESCRITA DOS POOLS: reescrever 56 strings de
# cenario a mao e' redigitar copy validada — o erro que o repo ja' pagou (o D1
# comprimido na mao virou esqueleto 3D). Aqui a clausula da bandeira e' um
# recorte REGULAR (comeca em `, ` ou ` and `, termina na proxima virgula), e ela
# sai por substituicao verificada em vez de por edicao humana.
#
# ⛔ E A REMOCAO E' COBRADA, NAO CONFIADA: `lint_bandeira` varre o TEXTO MONTADO
# e reprova se sobrou `flag`, se ficou virgula dupla, ` and ,` ou espaco duplo.
# Regex que erra em prosa erra silenciosamente; por isso a lente vem junto.
_BANDEIRA = re.compile(
    r"(?:,\s*|\s+and\s+)(?:a|an|the)\s+(?:small\s+|large\s+)?"
    r"(?:US|American)\s+flag\b[^,.]*", re.I)

_SUJEIRA = ((r"\s*,\s*,", ","), (r"\s+and\s*,", ","), (r"\s{2,}", " "),
            (r"\s+([,.])", r"\1"), (r",\s*$", ""), (r"\s+and\s*$", ""))


def tirar_bandeira(texto):
    """Devolve o texto sem a clausula da bandeira, com a prosa normalizada."""
    fora = _BANDEIRA.sub("", texto or "")
    for padrao, troca in _SUJEIRA:
        fora = re.sub(padrao, troca, fora)
    return fora.strip()


def tem_bandeira(texto):
    return re.search(r"\b(?:US|American)\s+flag\b", texto or "", re.I) is not None


def lint_bandeira(spec, blocos, achados, rotulo="bandeira"):
    """A bandeira aparece se e' para aparecer, e some inteira se nao e'.

    ⚠️ Varre o TEXTO MONTADO, nunca o pool (§19): a string do cenario e' montada
    dentro de um bloco maior, e `grep` no fonte nao ve frase quebrada entre
    literais adjacentes.
    """
    quer = bool(spec.get("bandeira"))
    for nome in sorted(blocos):
        if nome.startswith("BLOCO"):
            continue
        txt = blocos[nome]
        if not quer and tem_bandeira(txt):
            achados.append(("ERRO", "%s: %s sorteou SEM bandeira e o texto ainda "
                                    "traz uma — a remocao nao pegou a clausula"
                            % (rotulo, nome)))
        for padrao, msg in ((r",\s*,", "virgula dupla"),
                            (r"\s+and\s*,", "'and' orfao antes de virgula"),
                            (r"\s{2,}", "espaco duplo"),
                            (r"\s+[,.]", "espaco antes de pontuacao")):
            if re.search(padrao, txt):
                achados.append(("ERRO", "%s: %s com %s — a remocao da bandeira "
                                        "estragou a prosa" % (rotulo, nome, msg)))
    if quer and not any(tem_bandeira(t) for k, t in blocos.items()
                        if not k.startswith("BLOCO")):
        achados.append(("ERRO", "%s: sorteou COM bandeira e nenhum bloco a "
                                "mostra" % rotulo))


def autoteste_bandeira():
    """Controles positivos e negativos com as clausulas REAIS dos 4 motores.

    ⛔ Rodam ANTES de qualquer numero ser olhado (licoes §16). O caso que motiva
    a lente — texto que ficou com bandeira depois de sortear sem — e' o primeiro.
    """
    casos = [
        ("a home office with a full wall of dark hardback spines with gold "
         "detailing, two framed documents in dark wood frames with gold foil "
         "seals and a US flag on a floor stand in the corner",
         "a home office with a full wall of dark hardback spines with gold "
         "detailing, two framed documents in dark wood frames with gold foil "
         "seals"),
        ("a small older American kitchen with laminate counters and a window "
         "over the sink, a US flag magnet on the fridge door",
         "a small older American kitchen with laminate counters and a window "
         "over the sink"),
        ("a bright kitchen with a white refrigerator, a small American flag on "
         "a stand on the counter, and a bowl of lemons",
         "a bright kitchen with a white refrigerator, and a bowl of lemons"),
        ("the same wood-panelled study, the shelf of dark hardbacks behind her "
         "and the small US flag in its brass stand",
         "the same wood-panelled study, the shelf of dark hardbacks behind her"),
    ]
    falhas = []
    for entrada, esperado in casos:
        saida = tirar_bandeira(entrada)
        if saida != esperado:
            falhas.append("removeu errado:\n   deu = %r\n   era = %r"
                          % (saida, esperado))
        if tem_bandeira(saida):
            falhas.append("sobrou bandeira em %r" % saida)
    # ⛔ CONTROLE NEGATIVO: texto sem bandeira nao pode ser tocado
    limpo = "a plain kitchen with a stainless counter and a stack of chairs"
    if tirar_bandeira(limpo) != limpo:
        falhas.append("mexeu em texto que nao tinha bandeira: %r"
                      % tirar_bandeira(limpo))
    return falhas


def lint_sem_texto(blocos, achados):
    """Guarda da trava — sem isto ela sai de novo no proximo refactor."""
    for chave in sorted(blocos):
        if chave.startswith("TAKE") and SEM_TEXTO_TAKE not in blocos[chave]:
            achados.append(("ERRO", "%s sem a trava de texto queimado — o Veo "
                                    "pode gravar legenda ou marca no video, e "
                                    "a nossa legenda nasce depois, no Editor"
                            % chave))


# ---------------------------------------------------------------------------
# ⛔⛔ TAKE CONTRA IMAGE — a lente que faltava, e ela custou dois agentes
# ---------------------------------------------------------------------------
# Criada em 2026-08-05, ao rodar a etapa [7] do PLACA. O motor passava 600
# sorteios sem um ERRO e o TAKE 01 dizia *"Her right hand keeps the dish at the
# same height and the same tilt. Only the falling scatter moves"* — contra uma
# IMAGE sem prato e sem despejo. O TAKE 02 mandava tampar o liquidificador
# enquanto a IMAGE mostrava uma colher num caneco. Nada disso e' visivel a um
# linter que olha um bloco por vez.
#
# ⭐ A DOUTRINA QUE ELA DEFENDE: *contradicao entre IMAGE e TAKE e' PIOR que
# omissao — a omissao o gerador preenche com o frame; a contradicao ele resolve
# mexendo no que estava certo.* Estava escrita em comentario em seis motores e
# vigiada em nenhum.
#
# ⚠️ ESTA LENTE E' DE OBJETO, NAO DE PROSA. Ela nao tenta entender a cena: pega
# um punhado de substantivos que SO' fazem sentido se o objeto estiver em quadro,
# e cobra que quem aparece no TAKE apareca na IMAGE do MESMO bloco. Falso
# positivo aqui e' barato (o motor declara a excecao); falso negativo custou dois
# agentes entregues com prompt contraditorio.
OBJETOS_TAKE = {
    "the dish": ("dish",),
    "the falling scatter": ("falling", "scatter", "pouring", "tipped over"),
    "blender": ("blender",),
    "the lid": ("lid",),
    "the spoon": ("spoon",),
    "the long spoon": ("spoon",),
    "the mug": ("mug",),
    "the glass": ("glass",),
    "the card": ("card",),
    "the sign": ("card", "sign"),
    "the jug": ("jug", "blender"),
    "the pan": ("pan", "hotplate"),
    "the straw": ("straw",),
    "the mortar": ("mortar",),
    "the pestle": ("pestle",),
    "the sieve": ("sieve",),
    "the jar": ("jar",),
}


def _direcao(take):
    """So' a DIRECAO do TAKE — sem a fala e sem o audio.

    ⛔ A primeira versao desta lente lia o bloco inteiro e acusava o
    RESSURREICAO por *"You already own the glass"* — que esta' na FALA, onde a
    copy pode citar objeto que nao esta' em quadro (metafora, posse, memoria).
    Direcao e fala sao dois registros: um manda o gerador desenhar, o outro e'
    o que a boca diz. Confundir os dois e' o mesmo erro de categoria que fez a
    lente acusar cenario como se fosse gente.
    """
    for corte in ("\nDialogue:", 'Dialogue: "', "\nAudio:"):
        if corte in take:
            take = take.split(corte)[0]
    return take


def lint_take_vs_image(blocos, achados, excecoes=()):
    """Cobra que o objeto citado no TAKE exista na IMAGE do MESMO bloco.

    `excecoes` recebe as chaves de OBJETOS_TAKE que aquele motor sabe que sao
    seguras — mas declarar excecao e' declarar que ALGUEM CONFERIU, e fica
    escrito no motor com o porque.
    """
    for chave in sorted(blocos):
        if not chave.startswith("TAKE"):
            continue
        img = blocos.get(chave.replace("TAKE", "IMAGE"), "")
        if not img:
            continue
        low = _direcao(blocos[chave]).lower()
        for termo, provas in OBJETOS_TAKE.items():
            if termo in excecoes or termo not in low:
                continue
            if not any(p in img.lower() for p in provas):
                achados.append((
                    "ERRO",
                    "%s cita %r e a IMAGE do mesmo bloco nao tem esse objeto — "
                    "contradicao entre TAKE e IMAGE e' pior que omissao: o "
                    "gerador resolve mexendo no que estava certo" % (chave, termo)))

    # ⭐ A OUTRA METADE: contagem de gente. `only person in the shot` num TAKE
    # cuja IMAGE tem um segundo corpo e' ordem contraditoria, e o Veo resolve
    # APAGANDO o segundo corpo — que costuma ser justamente o bit do angulo.
    for chave in sorted(blocos):
        if not chave.startswith("TAKE"):
            continue
        img = blocos.get(chave.replace("TAKE", "IMAGE"), "").lower()
        if not img or "only person in the shot" not in _direcao(
                blocos[chave]).lower():
            continue
        # ⛔ AS PISTAS SAO DE PESSOA, NUNCA DE POSICAO. A primeira versao tinha
        # `behind her and` e `beside her at frame`, e as duas casavam com
        # CENARIO — *"the two framed documents behind her and the US flag"* no
        # ESCANDALO, *"a living room out of focus behind her and a small US
        # flag"* no RESSURREICAO. Falso positivo e' pior que lente nenhuma: o
        # operador aprende a ignorar a lente, e ela para de proteger o caso real.
        for pista in ("is a man", "stands a man", "a man shown", "her friend",
                      "second woman", "another woman", "is a %d-year-old man",
                      "man stands", "man is standing", "man sits"):
            if pista in img:
                achados.append((
                    "ERRO",
                    "%s declara `only person in the shot` e a IMAGE do mesmo "
                    "bloco tem um segundo corpo (%r) — o Veo resolve a "
                    "contradicao APAGANDO o segundo corpo" % (chave, pista)))
                break


def lint_painel_honesto(motor, spec, blocos, achados):
    """⛔⛔ EIXO DO PAINEL QUE NAO CHEGA AO VIDEO — criada em 2026-08-05.

    A auditoria da etapa [7] achou SETE eixos fantasma em dois motores: o
    PLACA desenhava SUBSTANCIA, METODO, COMUM e RARO no painel e o DUPLA
    desenhava SUBSTANCIA, METODO e COMUM — todos sorteados, todos rotacionados
    no ledger, nenhum chegando a bloco nenhum. Sobraram da copia do BOTICA,
    onde eles existem.

    ⚠️ Eixo que aparece no painel e nao muda o video e' PIOR que eixo ausente:
    o operador troca, le o prompt, ve que nada mudou, e para de confiar no
    painel inteiro. Mesma familia do cadeado que nao trava.

    ⭐ A lente e' de PRESENCA, nao de semantica: ela so' pergunta se o valor
    sorteado aparece em algum bloco. Eixo cujo valor e' um `id` interno
    (`mundo`, `metodo`) declara-se em `IGNORA_PAINEL` no motor.
    """
    junto = " ".join(blocos.values()).lower()
    ignora = set(getattr(motor, "IGNORA_PAINEL", ()) or ())
    ignora |= {"etnia", "cor", "mundo"}
    for eixo in [e[0] for e in getattr(motor, "EIXOS_UI", [])]:
        if eixo in ignora or eixo not in spec:
            continue
        # ⛔ QUALQUER campo do eixo serve como prova de presenca. A primeira
        # versao olhava so' `nome` e acusava o COMUM do CHA, que chega ao quadro
        # pelo campo `img` (`a shallow dish of deep red powder`) — o eixo estava
        # em cena, so' nao pelo nome. Lente que exige a prova numa forma so' e'
        # lente que inventa defeito.
        v = spec[eixo]
        if isinstance(v, dict):
            provas = [x for x in v.values() if isinstance(x, str) and len(x) > 3]
        elif isinstance(v, (tuple, list)):
            provas = [str(x) for x in v if isinstance(x, str) and len(x) > 3]
        else:
            provas = [str(v)]
        alvo = provas[0] if provas else None
        if provas and not any(p.lower() in junto for p in provas):
            achados.append((
                "ERRO",
                "PAINEL: o eixo %r esta' no painel e o valor sorteado (%r) nao "
                "aparece em bloco nenhum — o operador troca e o video nao muda"
                % (eixo, str(alvo)[:44])))


# ---------------------------------------------------------------------------
# ⭐⭐ MODO REF BELA — o toggle compartilhado
# ---------------------------------------------------------------------------
# Ordem do operador, 2026-08-05, lendo os lotes do DUPLA e do PLACA: *"gostei
# muito da ideia de ref feminina lindas super models com corpao e pouca roupa.
# Estou pensando em colocar um toggle de trava pra modo ref mulher bela em todos
# os ui ux pertinentes dos agentes shorts, que, quando ativados, gera refs
# mulheres com essas caracteristicas"*.
#
# ⛔ E' UM CONTRATO, NAO 16 IMPLEMENTACOES. O pool de REFs e o de roupas moram
# AQUI e valem para todo motor que declarar `MODO_BELA = True`. Um pool por
# motor divergiria em uma semana — e "duas classificacoes divergentes" e' o
# fragmento espelhado que a P9 proibe.
#
# ⚠️ ADITIVO: lido com `getattr`, entao motor que nao declara nada nao muda de
# comportamento. Mesma disciplina do `PELE_TRAVAVEL`.
#
# ⭐ O QUE O MODO MUDA, e sao TRES coisas, porque o operador nomeou as tres:
#   1. o CORPO e o ROSTO — pool proprio, registro top model;
#   2. a ROUPA — pouca, e com a perna em quadro;
#   3. a clausula ANTICELEB — `strikingly beautiful` no lugar de `ordinary
#      relatable face, not a model`, que brigava de frente com o resto (CL26).
# Mudar so' o rosto e deixar a roupa e a clausula velhas devolveria a
# contradicao que o CLEAN ja' pagou: o gerador recebe "linda" no corpo e "cara
# comum" no rosto na mesma frase, e resolve contra nos.

# ⛔ 30 entradas, CINCO ruivas de tons DIFERENTES (auburn, copper, ginger, dark
# red, mahogany) — ruiva nao e' uma cor so', e repetir `red hair` devolveria a
# mesma mulher cinco vezes.
# ⚠️ Cada uma varia CORPO, CABECA e MARCA juntos: duas mulheres de cabelo
# diferente e mesmo porte leem como a mesma pessoa (licao do medir_personagens).
REFS_BELAS = [
    # ⭐ AS OITO DE 28+ — existem para os motores com piso de idade (TR11,
    # ES11, RS19). Sem elas o `idade_min` nao tinha o que sortear.
    {"idade": 28, "corpo": "tall and sculpturally curvy with a narrow waist",
     "cabeca": "long dark hair falling in heavy glossy waves",
     "marca": "high cheekbones and a small beauty mark on the jaw"},
    {"idade": 29, "corpo": "statuesque and toned with long legs",
     "cabeca": "honey-blonde hair in a deep side part",
     "marca": "a wide full mouth and clear skin"},
    {"idade": 30, "corpo": "shapely and strong with a sculpted waist",
     "cabeca": "copper hair in loose waves past the shoulders",
     "marca": "a dense spray of freckles and a straight nose"},
    {"idade": 30, "corpo": "long-limbed and lean with square shoulders",
     "cabeca": "black hair in a sleek high ponytail",
     "marca": "sharp brows and a small gold hoop in one nostril"},
    {"idade": 31, "corpo": "curvy and sculpted with a very narrow waist",
     "cabeca": "chestnut hair cut into long layers",
     "marca": "a faint dimple in one cheek and full lips"},
    {"idade": 31, "corpo": "tall and athletic with a flat stomach",
     "cabeca": "dark auburn hair gathered in a low knot",
     "marca": "a small scar at the hairline and even skin"},
    {"idade": 32, "corpo": "softly curvy and toned with a long waist",
     "cabeca": "ash-blonde hair in a blunt shoulder cut",
     "marca": "a beauty mark above the lip and a strong jaw"},
    {"idade": 33, "corpo": "slim and sculptural with a graceful neck",
     "cabeca": "long box braids gathered high",
     "marca": "sculpted cheekbones and a small stud in one nostril"},
    {"idade": 23, "corpo": "tall and long-legged with a sculpted waist",
     "cabeca": "deep auburn hair falling in loose waves past her shoulders",
     "marca": "a light spray of freckles across her nose and green eyes"},
    {"idade": 26, "corpo": "sculptural with an hourglass figure and long legs",
     "cabeca": "copper-red hair in a high glossy ponytail",
     "marca": "pale green eyes and a small beauty mark above her lip"},
    {"idade": 22, "corpo": "willowy and sculpted with a flat stomach",
     "cabeca": "bright ginger hair cut in long layers",
     "marca": "heavy freckling across her cheeks and hazel eyes"},
    {"idade": 21, "corpo": "sculpturally curvy with a narrow waist",
     "cabeca": "dark red hair swept over one shoulder",
     "marca": "a small gold hoop in her left nostril and clear skin"},
    {"idade": 25, "corpo": "tall and statuesque with a sculpted line",
     "cabeca": "strawberry-blonde hair in a loose braid",
     "marca": "wide-set blue eyes and a faint scar through one eyebrow"},
    {"idade": 24, "corpo": "slim and toned with a dancer's line",
     "cabeca": "jet-black hair in a sleek centre part",
     "marca": "sharp cheekbones and a small mole on her jaw"},
    {"idade": 27, "corpo": "long-legged and slender with square shoulders",
     "cabeca": "platinum blonde hair in a blunt shoulder-length cut",
     "marca": "ice-blue eyes and a dimple in one cheek"},
    {"idade": 23, "corpo": "curvy and athletic with a small waist",
     "cabeca": "tight dark curls gathered high on her head",
     "marca": "clear deep brown skin and a wide bright smile"},
    {"idade": 22, "corpo": "tall and slim with an hourglass line",
     "cabeca": "chestnut hair in long beachy waves",
     "marca": "a gap between her front teeth and warm brown eyes"},
    {"idade": 21, "corpo": "petite and curvy with a defined waist",
     "cabeca": "honey-blonde hair in a high messy bun",
     "marca": "a scatter of freckles and full lips"},
    {"idade": 26, "corpo": "lean and toned with a flat stomach and long arms",
     "cabeca": "long jet-black hair worn straight to the waist",
     "marca": "almond eyes and a small stud in one nostril"},
    {"idade": 25, "corpo": "shapely with toned arms and a narrow waist",
     "cabeca": "caramel balayage falling past her shoulders",
     "marca": "a beauty mark at the corner of her right eye"},
    {"idade": 22, "corpo": "slim-hipped and elegant with a long neck",
     "cabeca": "sandy blonde hair in a fishtail braid",
     "marca": "a slight overbite that shows when she smiles"},
    {"idade": 23, "corpo": "curvy and strong with a small waist",
     "cabeca": "long box braids gathered over one shoulder",
     "marca": "high round cheekbones and a gold nose ring"},
    {"idade": 24, "corpo": "tall and lean with swimmer's shoulders",
     "cabeca": "auburn hair in a low glossy ponytail",
     "marca": "dark freckles across both cheeks and grey eyes"},
    {"idade": 27, "corpo": "softly curvy with a full figure and a narrow waist",
     "cabeca": "dark brown hair in heavy waves with a deep side part",
     "marca": "a small raised birthmark on her temple"},
    {"idade": 23, "corpo": "slim and supple with a very straight back",
     "cabeca": "copper hair cropped into a long bob",
     "marca": "pale skin, freckles and bright green eyes"},
    {"idade": 21, "corpo": "long-limbed and shapely with a defined waist",
     "cabeca": "black hair in a high sleek ponytail",
     "marca": "a thin scar along her jawline and full brows"},
    {"idade": 25, "corpo": "trim and athletic with a flat stomach",
     "cabeca": "golden blonde hair in loose waves",
     "marca": "a small dimple in one cheek only"},
    {"idade": 21, "corpo": "tall and willowy with narrow hips",
     "cabeca": "dark auburn hair in a half-up twist",
     "marca": "wide hazel eyes and a light dusting of freckles"},
    {"idade": 22, "corpo": "curvy with a small waist and long legs",
     "cabeca": "tight coils cropped close to the head",
     "marca": "sculpted cheekbones and a small gold stud"},
    {"idade": 26, "corpo": "slim with a long waist and square shoulders",
     "cabeca": "ash-brown hair in a sleek low bun",
     "marca": "grey-green eyes and a faint mark between her brows"},
    {"idade": 24, "corpo": "shapely and toned with a narrow waist",
     "cabeca": "ginger hair in loose curls past her shoulders",
     "marca": "heavy freckling and a small chin dimple"},
    {"idade": 27, "corpo": "tall and slim with a graceful neck",
     "cabeca": "long dark hair in a high crown braid",
     "marca": "a beauty mark high on her left cheek"},
    {"idade": 22, "corpo": "petite and shapely with a defined waist",
     "cabeca": "bleached blonde hair in a blunt chin-length bob",
     "marca": "wide dark eyes and a faint scar on her chin"},
    {"idade": 23, "corpo": "athletic and curvy with strong shoulders",
     "cabeca": "long waves in a rich mahogany red",
     "marca": "clear skin and a small hoop in her right nostril"},
    {"idade": 23, "corpo": "long-legged and lean with a flat stomach",
     "cabeca": "dark brown hair in a slicked-back ponytail",
     "marca": "sharp brows and a small mole under one eye"},
    {"idade": 25, "corpo": "curvy and confident with a very narrow waist",
     "cabeca": "honey-red hair falling in soft waves",
     "marca": "a dense spray of freckles across her nose"},
    {"idade": 21, "corpo": "slim and elegant with long arms",
     "cabeca": "black hair in a smooth shoulder-length cut",
     "marca": "a thin white streak at her temple and dark eyes"},
    {"idade": 24, "corpo": "tall with a small waist and full shoulders",
     "cabeca": "strawberry-blonde hair in a high loose bun",
     "marca": "green eyes and a small beauty spot on her cheekbone"},
]

# ⭐⭐ A ROUPA DO MODO. *"pouca roupa"*, e o eixo que o operador chamou de bullet
# de retencao no CHA: decote, saia curta, PERNA EM QUADRO.
# ⛔ SILHUETA VARIADA, nao a mesma peca em vinte cores. Vinte entradas do mesmo
# corte com cor diferente leem como uniforme, e uniforme mata a leitura de
# "pessoas diferentes" — foi essa a licao dos trajes por mundo do BOTICA.
# ⚠️ PALETA AMERICANA DE RUA. Fora: ochre, terracotta, sand, sage, rust, burnt
# orange — a paleta de terra que o gerador le como traje etnico, e que fez o
# operador perguntar *"norte americano costuma usar roupa de tribo?"*.
ROUPAS_BELAS = [
    ("%s ribbed knit halter top with a deep cowl front and a very short skirt",
     "knit cowl halter"),
    ("%s cropped tank with a deep scoop front and very short denim shorts",
     "deep-scoop tank"),
    ("%s halter top with a plunging front, worn with a short wrap skirt",
     "plunging halter"),
    ("%s satin cami with thin straps and a very short pleated skirt",
     "satin cami"),
    ("%s off-shoulder crop top with high-cut shorts", "off-shoulder crop"),
    ("%s tight ribbed crop top with a short A-line skirt", "ribbed crop top"),
    ("%s knotted shirt tied under the bust and open at the top, with cut-off "
     "shorts", "knotted shirt"),
    ("%s low-cut slip dress cut short above the knee", "short slip dress"),
    ("%s fitted crop top under an open shirt, with a mini skirt",
     "fitted crop top"),
    ("%s one-shoulder crop top with a very short skirt", "one-shoulder crop"),
    ("%s corset-style top with short denim cut-offs", "corset-style top"),
    ("%s zip-front top worn half unzipped with a very short skirt",
     "half-zipped top"),
    ("%s halter mini dress with an open back", "halter mini dress"),
    ("%s cropped cardigan buttoned once over bare skin, with a mini skirt",
     "single-button cardigan"),
    ("%s lace-trimmed cami with a short flared skirt", "lace-trimmed cami"),
    ("%s wrapped halter fastened behind with very short shorts", "tied halter"),
]

# ⛔⛔ O POOL ACIMA NAO USA VOCABULARIO QUE AS LENTES DO REPO VIGIAM. Tres
# entradas foram reescritas em 2026-08-05 porque o modo BELA, ao entrar, fez o
# linter de DOIS agentes reprovar por colisao de palavra, nao por defeito:
#   · `deep cowl neckline` -> o EX7 do DUPLA vigia `neck` perto do molusco, e
#     `neckline` contem `neck`;
#   · `low-rise denim shorts` -> o BO2 do CHA vigia vocabulario de CRESCIMENTO,
#     e `low-rise` contem `rise`.
# ⚠️ Pool compartilhado herda TODAS as lentes de TODOS os motores. Uma palavra
# inocente aqui reprova a producao de um agente que eu nem estava olhando — e o
# jeito de descobrir isso e' rodar o linter dos dois modos em todo motor, que e'
# o que a medicao abaixo faz.
# ⛔⛔ SEM EXTREMO DE BIQUINI — ordem do operador, 2026-08-05: *"pouca roupa
# (saia curta, tops, etc (sem extremo de biquini))"*. Toda entrada e' TOP + PECA
# DE BAIXO ou VESTIDO CURTO; nenhuma e' roupa de banho, nenhuma e' so' sutia.
# ⚠️ A linha e' essa: o hook vive de sex appeal, e roupa de banho tira o video
# do registro de "mulher na cozinha de casa" — que e' o que faz a receita
# parecer real.
# ⭐⭐ OS OLHOS FORA DO COMUM — ordem do operador, 2026-08-05: *"olhos azuis,
# roxos, verdes, amarelos, coisa bem diferente fora do comum"*.
# ⛔ E' UM EIXO PROPRIO, nao uma edicao das 30 marcas. Editar a `marca` de cada
# REF acoplaria olho e rosto para sempre: a mesma mulher sairia sempre com o
# mesmo olho, e o eixo que o operador quer VARIANDO ficaria travado por
# construcao. Separado, sao 30 x 14 combinacoes.
# ⚠️ Descricao de COR e de LUZ, nunca de lente de contato: `violet` e `amber` o
# gerador entrega como iris; `contact lenses` ele entrega como acessorio, e o
# artificio mata o "mulher de verdade na cozinha".
OLHOS_BELAS = [
    "striking pale blue eyes",
    "deep violet eyes",
    "bright emerald green eyes",
    "amber-yellow eyes",
    "pale grey-blue eyes that catch the light",
    "unusual golden-hazel eyes",
    "vivid turquoise eyes",
    "dark violet eyes with a pale ring",
    "clear ice-blue eyes",
    "luminous green eyes",
    "warm amber eyes",
    "one blue eye and one green eye",
    "deep indigo-blue eyes",
    "pale gold-flecked green eyes",
]

CORES_BELAS = ["black", "white", "scarlet", "cobalt", "hot pink", "emerald",
               "burgundy", "silver", "cream", "dusty rose", "gold",
               "denim blue"]

# ⛔ A CLAUSULA. Sem ela o gerador recebe "linda" no corpo e `ordinary relatable
# face, not a model` no rosto NA MESMA FRASE — o CLEAN pagou essa contradicao em
# 2026-08-04 (CL26) e resolveu do mesmo jeito. A protecao de IDENTIDADE fica
# inteira; so' sai o "comum" e o "nao e' modelo".
ANTICELEB_BELA = ("A strikingly beautiful face, not a celebrity, not "
                  "resembling any famous person.")



def _sem_olhos(marca):
    """A marca facial sem a mencao de olhos — o olho vem do eixo proprio.

    ⚠️ Limpa as tres formas que o pool usa: `X and <cor> eyes`, `<cor> eyes and
    X` e `<cor> eyes` sozinho. Se sobrar vazio, devolve `clear skin` — marca
    vazia derrubaria a frase do BLOCO 0 com uma virgula solta.
    """
    m = re.sub(r",?\s*\band\b[^,]*\beyes\b", "", marca, flags=re.I)
    m = re.sub(r"^[^,]*\beyes\b\s+and\s+", "", m, flags=re.I)
    m = re.sub(r"^[^,]*\beyes\b,?\s*", "", m, flags=re.I)
    m = re.sub(r"\s{2,}", " ", m).strip(" ,")
    return m or "clear skin"

def ref_bela(molde, rng, idade_min=None, banidos=()):
    """Uma REF do modo BELA no FORMATO DO MOTOR que pediu.

    `molde` e' uma entrada qualquer do pool original — serve so' para dizer
    QUAIS CAMPOS aquele motor espera. Os campos que o pool bela conhece
    (`idade`, `corpo`, `cabeca`, `marca`) sao preenchidos por ele; os que so'
    existem naquele motor (`roupa`, `oculos`, `porte`, `pele`, `pelo`...)
    recebem o valor coerente com o modo.

    ⛔ POR QUE NAO DEVOLVER O DICIONARIO CRU: os pools tem formatos diferentes —
    o RESSURREICAO tem `porte`/`rosto`/`oculos`, o FLAGRANTE tem `roupa_curta`,
    o VAZAMENTO tem `musculo`. Devolver o formato do pool bela quebraria o
    `montar()` de cada um com KeyError, e KeyError dentro do callback do tkinter
    morre CALADO — foi assim que o botao `trocar` de seis agentes ficou quebrado
    sem ninguem perceber em 2026-07-31.
    """
    # ⛔ O PISO DE IDADE E' DO MOTOR, nao do pool. O TROCA exige narradora
    # com 28+ (TR11: ela fala do marido) e o pool bela vai de 21 a 27 por ordem
    # do operador (*"novinhas"*). Os dois se chocaram em 200 de 200 sorteios ate'
    # este parametro existir. ⚠️ Quando NENHUMA entrada atinge o piso, ele CEDE
    # e a mais velha do pool entra: derrubar o sorteio por causa de um toggle
    # seria o botao que quebra o app, nao o que muda a REF.
    # ⛔⛔ O MOTOR PASSA A PROPRIA LISTA DE BANIDOS. O RESSURREICAO tem a RS23
    # (`BANIDOS_DESEJO`: sexy, curvy, revealing, cleavage...) e o pool bela usa
    # `curvy`. Filtrar aqui e' RESPEITAR a regra, nao furar: o modo entra por
    # baixo dela. Furar seria reintroduzir um vocabulario que ja' custou recusa.
    # ⚠️ Se o filtro esvaziar o pool, ele CEDE — derrubar o sorteio por causa de
    # um toggle e' o botao que quebra o app.
    _pool = REFS_BELAS
    if banidos:
        _b = tuple(x.lower() for x in banidos)
        _pool = [r for r in _pool
                 if not any(w in (r["corpo"] + " " + r["cabeca"] + " "
                                  + r["marca"]).lower() for w in _b)] or _pool
    if idade_min:
        # ⛔ O FALLBACK SAI DO POOL JA' FILTRADO (`_pool`), nunca do REFS_BELAS
        # inteiro. A primeira versao caia no `max(REFS_BELAS)` e trazia de volta
        # uma entrada que o filtro de BANIDOS tinha acabado de excluir — o
        # RESSURREICAO reprovava 65 de 200 com `curvy` vindo justamente dai'.
        # ⚠️ Fallback que ignora um filtro anterior e' a mesma familia do
        # `or pool` do `_cabem`: parece funcionar e desfaz a regra em silencio.
        _pool = [r for r in _pool if r["idade"] >= idade_min] or [
            max(_pool, key=lambda r: r["idade"])]
    base = dict(rng.choice(_pool))
    # ⭐ O OLHO E' SORTEADO A PARTE e entra NA MARCA — que e' o campo que todo
    # motor ja' renderiza. Assim ele chega ao quadro sem eu tocar em 16 motores.
    # ⛔ E O OLHO ANTIGO SAI ANTES. Quinze das 30 marcas ja' descrevem os olhos
    # (`... and green eyes`), e sem esta limpeza o prompt saia com DOIS:
    # *"luminous green eyes, wide-set blue eyes and a faint scar"*. Duas cores
    # para o mesmo par de olhos e' contradicao, e o gerador resolve inventando
    # uma terceira. Achado LENDO as tres primeiras saidas do helper.
    base["marca"] = "%s, %s" % (rng.choice(OLHOS_BELAS),
                                _sem_olhos(base["marca"]))
    _rp = ROUPAS_BELAS
    if banidos:
        _b = tuple(x.lower() for x in banidos)
        _rp = [p for p in ROUPAS_BELAS
               if not any(w in p[0].lower() for w in _b)] or ROUPAS_BELAS
    tpl, curto = rng.choice(_rp)
    roupa = tpl % rng.choice(CORES_BELAS)
    saida = {}
    for campo in molde:
        if campo in base:
            saida[campo] = base[campo]
        elif campo in ("roupa", "roupa2", "roupa_curta", "traje"):
            saida[campo] = roupa
        elif campo == "oculos":
            saida[campo] = ""            # ⛔ Lei do REF: zero oculos
        elif campo == "pelo":
            saida[campo] = ""
        elif campo in ("porte", "musculo"):
            saida[campo] = base["corpo"]
        elif campo == "rosto":
            saida[campo] = base["marca"]
        elif campo == "cabelo":
            saida[campo] = base["cabeca"]
        elif campo == "pele":
            saida[campo] = "clear even skin"
        elif campo == "id":
            saida[campo] = "bela_%d" % base["idade"]
        else:
            # ⚠️ Campo que este helper nao conhece MANTEM o valor do molde. E'
            # de proposito: inventar valor para campo desconhecido e' como o
            # `or pool` do `_cabem` — parece funcionar e mente em silencio.
            saida[campo] = molde[campo]
    saida["_bela"] = True
    saida["_roupa_curta"] = curto
    return saida


def traje_bela(rng):
    """Uma roupa do MODO BELA no formato `(template_com_%s_de_cor, curto)` —
    o mesmo que os pools de traje por mundo devolvem, para o motor nao precisar
    saber de onde ela veio."""
    tpl, curto = rng.choice(ROUPAS_BELAS)
    return (tpl, curto)


def corpo_bela(spec, sufixo=", %s"):
    """O CORPO da REF, para o motor colar na ancora quando o modo esta' ligado.

    ⛔ Devolve "" quando o modo esta' desligado — assim o motor cola sem `if`, e
    a cena normal nao muda um caractere.
    ⚠️ Existe porque em tres dos cinco primeiros motores ligados o `corpo` so'
    aparecia no BLOCO 0 e nunca na CENA: a REF entrava escultural na foto de
    referencia e generica no quadro. O operador pediu *"corpo escultural"*, e
    corpo que nao chega ao frame nao e' corpo.
    """
    if not spec.get("bela"):
        return ""
    r = spec.get("ref") or spec.get("narradora") or {}
    c = r.get("corpo") or r.get("porte") or ""
    return (sufixo % c) if c else ""


# ---------------------------------------------------------------------------
# ⭐⭐ MODO REF FORTE — o irmao masculino do MODO BELA
# ---------------------------------------------------------------------------
# Ordem do operador, 2026-08-05: *"quero um toggle similar para homens fortes
# bem musculosos, atraentes tb, que, quando ativados, serao capazes de gerar
# prompts refs dentro dessas caracteristicas"*.
#
# ⛔ MESMO CONTRATO DO BELA, de proposito: `MODO_FORTE = True` no motor, a UI
# desenha o botao, `travas["forte"]` chega no `sortear`, e o helper devolve a REF
# no FORMATO DAQUELE MOTOR. Dois contratos diferentes para a mesma ideia
# divergiriam na primeira manutencao.
#
# ⚠️ CORPO-PROVA x NARRADOR. Em varios motores o homem e' o CORPO-PROVA da cena
# 3 — o espectador tem de se ver nele. Musculoso demais afasta: `he could never
# be me`. Por isso o pool e' de homem FORTE E CRIVEL (pescador, mecanico,
# bombeiro), nao de fisiculturista — e o operador pediu "atraentes", nao
# "monstruosos".
REFS_FORTES = [
    {"idade": 29, "corpo": "tall and heavily built with broad shoulders and thick forearms",
     "cabeca": "dark hair cropped short with a faded side",
     "marca": "a strong square jaw and a short beard"},
    {"idade": 34, "corpo": "broad-chested and powerfully built with a thick neck",
     "cabeca": "close-shaved head",
     "marca": "a small scar through one eyebrow and heavy brows"},
    {"idade": 27, "corpo": "lean and cut with wide shoulders and a flat stomach",
     "cabeca": "dark curls kept short",
     "marca": "sharp cheekbones and a clean jawline"},
    {"idade": 31, "corpo": "heavy and solid through the chest and arms",
     "cabeca": "sandy hair pushed back",
     "marca": "a heavy stubble and a deep smile line"},
    {"idade": 36, "corpo": "thickset and strong with heavy shoulders",
     "cabeca": "greying hair cut close at the sides",
     "marca": "a weathered face and a full dark beard"},
    {"idade": 28, "corpo": "athletic and broad with defined arms",
     "cabeca": "black hair in a low fade",
     "marca": "a small chip in one front tooth and a wide smile"},
    {"idade": 33, "corpo": "tall and muscular with a deep chest",
     "cabeca": "auburn hair cut short and pushed to one side",
     "marca": "freckles across the nose and a strong brow"},
    {"idade": 30, "corpo": "powerfully built with thick arms and a narrow waist",
     "cabeca": "dark hair with a widow's peak",
     "marca": "a straight nose and a trimmed goatee"},
    {"idade": 26, "corpo": "solid and toned with square shoulders",
     "cabeca": "light brown hair worn a little long on top",
     "marca": "a dimple in one cheek and clean-shaven"},
    {"idade": 38, "corpo": "heavy through the chest and shoulders, still hard",
     "cabeca": "salt-and-pepper hair cropped short",
     "marca": "deep lines at the eyes and a grey-flecked beard"},
    {"idade": 32, "corpo": "broad and strong with heavy forearms",
     "cabeca": "black hair shaved at the sides",
     "marca": "a faded tattoo up one forearm and a hard jaw"},
    {"idade": 29, "corpo": "tall and rangy with wide shoulders and long arms",
     "cabeca": "dirty-blond hair pushed back off the forehead",
     "marca": "a cleft chin and pale stubble"},
    {"idade": 35, "corpo": "compact and thickly muscled through the neck and arms",
     "cabeca": "dark hair kept very short",
     "marca": "a broken nose set slightly off centre"},
    {"idade": 27, "corpo": "wide-shouldered and lean with a hard stomach",
     "cabeca": "tight dark curls cropped close",
     "marca": "a small keloid scar on the jaw and a bright smile"},
    {"idade": 31, "corpo": "strongly built with a barrel chest and thick wrists",
     "cabeca": "red-brown hair cut short",
     "marca": "heavy freckling on the arms and a copper beard"},
    {"idade": 34, "corpo": "tall and heavy-framed with wide shoulders",
     "cabeca": "grey-streaked dark hair combed back",
     "marca": "a deep vertical line between the brows"},
]

# ⭐ OS OLHOS, mesmo eixo do BELA — *"coisa bem diferente fora do comum"*.
OLHOS_FORTES = [
    "striking pale blue eyes",
    "deep grey-green eyes",
    "unusual amber eyes",
    "vivid green eyes",
    "ice-blue eyes under heavy brows",
    "dark violet-grey eyes",
    "pale gold-flecked hazel eyes",
    "one blue eye and one brown eye",
    "clear steel-blue eyes",
    "deep emerald eyes",
]

# ⭐ A ROUPA. *"fortes bem musculosos, atraentes"* — a roupa mostra o corpo sem
# virar academia: regata, camisa aberta, camiseta justa.
# ⛔ NADA DE SUNGA OU POSE DE FISICULTURISTA: o corpo-prova tem de ser um homem
# na cozinha de casa, nao um atleta em competicao. Corpo-prova que o espectador
# nao consegue ser nao prova nada.
ROUPAS_FORTES = [
    ("%s ribbed tank top that shows his shoulders and arms", "ribbed tank"),
    ("%s fitted t-shirt stretched across the chest", "fitted t-shirt"),
    ("%s work shirt with the sleeves cut off at the shoulder", "cut-off work shirt"),
    ("%s open flannel shirt over a tight white tank", "open flannel"),
    ("%s plain t-shirt with the sleeves rolled up over the biceps",
     "rolled-sleeve t-shirt"),
    ("%s henley with the buttons open at the chest", "open henley"),
    ("%s sleeveless denim shirt worn open over a bare chest",
     "open denim shirt"),
    ("%s tight athletic top damp across the back", "athletic top"),
    ("%s short-sleeved shirt unbuttoned to the middle of the chest",
     "unbuttoned shirt"),
    ("%s worn t-shirt with a torn collar, tight through the shoulders",
     "worn t-shirt"),
]

CORES_FORTES = ["black", "white", "charcoal", "navy", "olive", "burgundy",
                "denim blue", "grey", "forest green", "rust red"]

# ⛔ A clausula do rosto, no registro masculino. Mesma logica do CL26: se o corpo
# diz "powerfully built" e o rosto diz "ordinary relatable face, not a model", o
# gerador recebe as duas na mesma frase e resolve contra nos.
ANTICELEB_FORTE = ("A rugged good-looking face, not a celebrity, not "
                   "resembling any famous person.")


def ref_forte(molde, rng, idade_min=None, idade_max=None):
    """Uma REF masculina do MODO FORTE no FORMATO DO MOTOR que pediu.

    Espelho exato do `ref_bela` — ver a docstring de la' para o porque de nao
    devolver o dicionario cru.

    ⛔ A FAIXA E' DO MOTOR. O ESCANDALO tem `TETO_DIF_IDADE = 30` entre narradora
    e corpo-prova, e uma faixa propria para o figurante; o RESSURREICAO tem a
    mesma. Um pool compartilhado que ignore isso reprova a producao do motor —
    medido em 200 sorteios antes deste parametro existir.
    ⚠️ Quando NENHUMA entrada cabe na faixa, ela CEDE e a mais proxima entra:
    derrubar o sorteio por causa de um toggle seria o botao que quebra o app.
    """
    _pool = REFS_FORTES
    if idade_min is not None:
        _pool = [r for r in _pool if r["idade"] >= idade_min] or _pool
    if idade_max is not None:
        _pool = [r for r in _pool if r["idade"] <= idade_max] or [
            min(REFS_FORTES, key=lambda r: r["idade"])]
    base = dict(rng.choice(_pool))
    base["marca"] = "%s, %s" % (rng.choice(OLHOS_FORTES),
                                _sem_olhos(base["marca"]))
    tpl, curto = rng.choice(ROUPAS_FORTES)
    roupa = tpl % rng.choice(CORES_FORTES)
    saida = {}
    for campo in molde:
        if campo in base:
            saida[campo] = base[campo]
        elif campo in ("roupa", "roupa2", "roupa_curta", "traje"):
            saida[campo] = roupa
        elif campo in ("oculos", "pelo"):
            saida[campo] = ""
        elif campo in ("porte", "musculo"):
            saida[campo] = base["corpo"]
        elif campo == "rosto":
            saida[campo] = base["marca"]
        elif campo == "cabelo":
            saida[campo] = base["cabeca"]
        elif campo == "pele":
            saida[campo] = "clear skin"
        elif campo == "id":
            saida[campo] = "forte_%d" % base["idade"]
        else:
            saida[campo] = molde[campo]
    saida["_forte"] = True
    saida["_roupa_curta"] = curto
    return saida


def traje_forte(rng):
    """A roupa do MODO FORTE no formato `(template, curto)`."""
    return rng.choice(ROUPAS_FORTES)
