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
    """Roda o montar() do motor base e devolve so' as cenas do mapa.

    ⛔⛔ O TOTAL VEM DO TAMANHO DO MAPA, nao mais cravado em 3. A familia 16s
    (2 takes de 8s) passa um mapa de dois, e com o `/03` fixo aqui os blocos
    sairiam rotulados `01/03` e `02/03` num video de duas cenas — o AdBatch
    Vertical 2 conta os rotulos e recusaria o roteiro.
    ⚠️ Comportamento dos motores de 3 cenas INALTERADO: `len(mapa)` e' 3 neles,
    e o formato `%02d/%02d` devolve exatamente `01/03` como antes.
    """
    b5 = base.montar(espelho(spec, mapa))
    total = len(mapa)

    b = {"BLOCO 0 (REF)": b5["BLOCO 0 (REF)"]}
    for novo, orig in enumerate(mapa, 1):
        for tipo in ("IMAGE", "TAKE"):
            velho = "%s %02d/05" % (tipo, orig)
            chave = "%s %02d/%02d" % (tipo, novo, total)
            b[chave] = b5[velho].replace("%s %02d/05:" % (tipo, orig),
                                         "%s %02d/%02d:" % (tipo, novo, total), 1)
    return b


def bancada_com_rosto(base, spec, fala, n=3, total=3, modo="colher"):
    """A cena do ritual COM O ROSTO em quadro — recombinacao, nao invencao.

    ⭐⭐ DOIS MODOS (2026-08-10). O parametro existe porque SEIS motores chamam
    esta funcao (FLAGRANTE, PEE e NECROSE, nas versoes short e 16) e a ordem do
    operador foi para UM deles. Mudar o corpo mudaria os seis calados.

      `colher`         o de sempre: copo com uma colher, sache vazio na bancada,
                       ele gira a colher enquanto fala. NAO SE TOCA.
      `sache_erguido`  o novo, so' do FLAGRANTE 16: o copo JA' esta' pronto,
                       roxo, parado na bancada, e ele ERGUE o sache branco
                       rotulado, mostrando para a lente enquanto fala.

    ⛔ POR QUE O MODO NOVO EXISTE — relato do operador com dois renders na mao
    (2026-08-10): *"o take 2 ele esta' mexendo a agua e nao despeja a gelatina"*.
    E' o mesmo defeito de familia do sache duplicado: a cena PROMETE o gelatin
    trick e MOSTRA um homem mexendo agua transparente. O espectador nao ve'
    gelatina nenhuma, e a fala fica sem lastro na imagem.
    ⭐ A solucao que ele ditou nao e' fazer o modelo despejar — despejo e' acao
    em dois estados e ja' provou que duplica objeto. E' tirar a acao do quadro:
    o copo ja' NASCE pronto e roxo (o resultado), e a prova do que ha' dentro
    dele passa a ser o SACHE ERGUIDO na mao (a causa). Zero movimento de
    preparo, duas evidencias paradas.

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

    # ⛔⛔ DUAS COLHERES — relato de campo do operador, 2026-08-10, com o render
    # na mao: colher DENTRO do copo e outra na mesa, e o sache aberto na mao,
    # obrigando a regerar o take varias vezes.
    #
    # A CAUSA NAO ERA A CONTAGEM, ERA A AGENDA. O TAKE mandava TRES acoes ao
    # mesmo tempo — `stir the spoon` + `tipping the sachet` + `stirring it in
    # slow circles` — para DUAS maos, e a IMAGE punha as duas maos no copo
    # com sache E colher em jogo. O modelo precisa da colher em dois estados
    # (parada enquanto ele despeja, girando enquanto mexe) e resolve
    # DESENHANDO DUAS. Mesma familia do 16S5: contradicao dentro do prompt,
    # e o gerador resolve duplicando em vez de escolher.
    #
    # ⭐ Agora e' UMA acao, UMA mao, UM estado: o sache JA' FOI despejado e
    # esta' vazio e dobrado na bancada; ele so' gira a colher. O despejo nao
    # se perde — ele acabou de acontecer, e a fala o nomeia.
    # ⚠️ E a contagem entra EXPLICITA (`exactly one spoon`): o objeto que ja'
    # duplicou uma vez precisa de numero, nao de artigo.
    if modo == "sache_erguido":
        return _bancada_sache(base, spec, fala, n, total, et, ref, amb, luz)
    img = (
        "IMAGE %02d/%02d: Medium shot in %s. The same %d-year-old %s man, %s, "
        "%s, stands behind the %s, speaking to the camera. On the counter in "
        "front of him are a tall glass of water with exactly one spoon standing "
        "in it, and one empty white sachet lying flat and folded beside the "
        "glass, already used. His right hand rests on the spoon; his left hand "
        "is open on the counter, holding nothing. There is exactly one spoon in "
        "the shot and nothing else on the counter. He is alone in frame. %s %s"
        % (n, total, amb["set"], ref["idade"], et, ref["marca"],
           ref["roupa_curta"], amb["bancada"], luz.capitalize(), base.CAUDA)
    )
    take = (
        "TAKE %02d/%02d: Animate the image exactly. Handheld iPhone, slight "
        "sway, no cuts. His right hand turns the spoon in the glass in slow "
        "circles while he talks — that is the only movement. His left hand "
        "stays where it is. The empty sachet stays flat on the counter and is "
        "never picked up. Nothing is poured and nothing new enters the frame. "
        "His eyes stay on the lens the whole time. He is alone in the shot.\n"
        "Dialogue: \"%s\"\n"
        "Audio: spoon clinking glass, quiet room tone. No music."
        % (n, total, base.sonorizar(fala))
    )
    return img, take


# ---------------------------------------------------------------------------
# ⭐⭐ O MODO `sache_erguido` — o copo pronto e o sache na mao (2026-08-10)
# ---------------------------------------------------------------------------
# ⛔ O ROTULO EM INGLES E' EXCECAO DECLARADA, e precisa ser declarada DENTRO do
# prompt. A cauda dos motores diz `no text`; um sache escrito e' texto. Sem
# desmanchar a contradicao o gerador escolhe um dos dois — e ja' escolheu errado
# antes. O precedente e' o `SACHE_ROTULO` do GOOD 16: a palavra esta' no OBJETO,
# impressa na embalagem, e a trava continua valendo para legenda, marca d'agua e
# texto de interface. Por isso a cauda daqui e' PROPRIA e nao usa `base.CAUDA`.
#
# ⚠️ ROXO, e nao "colorido": `vivid purple` e' a cor travada da gelatina em TODO
# o parque. Copo de cor indefinida devolve agua transparente, que e' exatamente
# o defeito que este modo existe para matar.
#
# ⚠️ E o copo NAO tem colher. A colher so' faz sentido com movimento de mexer, e
# aqui nao ha' preparo nenhum — deixa-la em quadro sem funcao e' convidar o
# modelo a inventar a acao de volta.
#
# ⭐ 2026-08-10 (2): o PEE 16 entrou no mesmo modo, pelo MESMO relato —
# *"copo de agua transparente mexendo com uma colher, e o saco da gelatina
# sem nome nenhum"*. Por isso a constante deixou de se chamar
# `SACHE_FLAGRANTE`: o rotulo nao e' de um agente, e' do modo.
SACHE_ROTULADO = (
    "a small white sachet with the words GELATIN HORSE TRICK printed across "
    "the front in plain black capital letters")

CAUDA_ROTULO = (
    "The printed words on the sachet are part of the packaging and are the "
    "only writing anywhere in the shot. iPhone shot, natural grain, no "
    "on-screen text, no subtitles, no captions, no watermark.")


def _bancada_sache(base, spec, fala, n, total, et, ref, amb, luz):
    """Copo pronto e roxo na bancada; o sache erguido na mao, para a lente."""
    img = (
        "IMAGE %02d/%02d: Medium shot in %s. The same %d-year-old %s man, %s, "
        # ⚠️ A SUPERFICIE E' UMA SO', e por isso `amb["bancada"]` entra DUAS
        # vezes. O molde antigo dizia `behind the dining table` e logo depois
        # `on the counter` — duas superficies na mesma frase, e o gerador tem
        # todo o direito de desenhar as duas. Mesmo defeito de familia das duas
        # colheres: contradicao dentro do prompt, resolvida por duplicacao.
        "%s, stands behind the %s, facing the camera. On that same %s in front "
        "of him stands one tall clear glass, already filled with vivid purple "
        "liquid, finished and untouched — there is no spoon in it and no spoon "
        "anywhere in the shot. He holds %s up beside his own face in his right "
        "hand, unopened and full, turned so the printed front faces the lens. "
        "His left hand rests flat on that same surface, which holds nothing "
        "else. He is alone in frame. %s %s"
        % (n, total, amb["set"], ref["idade"], et, ref["marca"],
           ref["roupa_curta"], amb["bancada"], amb["bancada"], SACHE_ROTULADO,
           luz.capitalize(), CAUDA_ROTULO)
    )
    take = (
        "TAKE %02d/%02d: Animate the image exactly. Handheld iPhone, slight "
        "sway, no cuts. He talks to the camera and holds the sachet up where "
        "it is, turning it very slightly so the printed front stays readable — "
        "that is the only movement. The glass of purple liquid stays where it "
        "is, still and untouched, the whole time. He never opens the "
        "sachet, never pours anything, never stirs, and never puts the sachet "
        "down. Nothing new enters the frame. His eyes stay on the lens the "
        "whole time. He is alone in the shot. The words printed on the sachet "
        "stay exactly as they are and are packaging, not added text.\n"
        "Dialogue: \"%s\"\n"
        "Audio: quiet room tone, his voice only. No music."
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

    ⛔⛔ O TOTAL NAO E' 3 — 2026-08-09. Esta funcao cravava `/03` e explodia com
    `KeyError: 'IMAGE 01/03'` no PEE 16, que tem DOIS blocos. E' a TERCEIRA peca
    da maquinaria compartilhada a assumir tres cenas: o `montar_curto` foi
    generalizado em 18aa6dd, o `sortear_curto` em 70228dd, e faltava esta.
    ⚠️ O total agora sai dos BLOCOS QUE EXISTEM, nao de constante nenhuma —
    assim nao ha' uma quarta peca esperando o proximo formato temporal.
    """
    n = mapa.index(cena_base) + 1
    for chave in blocos:
        if chave.startswith("%s %02d/" % (tipo, n)):
            return blocos[chave]
    raise KeyError("%s %02d/?? nao existe (blocos: %s)"
                   % (tipo, n, sorted(k for k in blocos if k.startswith(tipo))))


# ---------------------------------------------------------------------------
# LINTER
# ---------------------------------------------------------------------------

# ⛔⛔ O QUE PODE VIR COLADO EM `gelatin trick` — ordem do Ed, 2026-08-06,
# lendo um take renderizado: *"quiet gelatin trick???? que adjetivo sem sentido
# e nonsense e esse?"*.
#
# O pool do BOTICA varia o QUALIFICADOR do mecanismo de proposito, e a maioria
# diz algo real sobre ACESSO ou ORIGEM: `secret`, `nobody sells`, `kept in the
# family`, `I keep to myself`. Mas `quiet` nao diz nada — um truque silencioso
# nao significa coisa nenhuma, e ainda dilui o nome do mecanismo, que e' o
# centro de gravidade do funil inteiro.
#
# ⚠️ E' ALLOWLIST, nao lista de proibidos. Enumerar adjetivos ruins e' corrida
# perdida: o proximo seria `gentle`, `humble`, `simple`. O que se permite antes
# do literal e' artigo, numeral e os DOIS qualificadores aprovados — o resto do
# tempero vem DEPOIS do literal ("gelatin trick nobody sells"), onde ele
# qualifica sem se disfarcar de nome.
_ANTES_DO_MECANISMO = re.compile(r"\b(\w+)\s+gelatin\s+trick\b", re.I)
_QUALIFICADOR_OK = frozenset((
    "a", "an", "one", "the", "that", "this", "my", "her", "his", "same",
    "secret", "whole",
))


def _adjetivo_do_mecanismo(corpo, achados):
    for m in _ANTES_DO_MECANISMO.finditer(corpo):
        palavra = m.group(1).lower()
        if palavra not in _QUALIFICADOR_OK:
            achados.append((
                "ERRO",
                "qualificador '%s' colado em 'gelatin trick' — so' artigo, "
                "numeral, 'secret' ou 'whole' podem vir antes do literal; o "
                "resto qualifica DEPOIS ('gelatin trick nobody sells')"
                % palavra))


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
    # ⛔⛔ AVISO APOSENTADO EM 2026-08-10, e a aposentadoria e' ARITMETICA.
    # Ele cobrava substantivos DISTINTOS entre as cenas. O operador reduziu o
    # pool sorteavel a TRES apelidos (`pecker`, `wiener`, `Johnson`) no parque
    # inteiro — e um motor de CINCO cenas com tres termos REPETE por definicao.
    # Medido no dia da mudanca: 600 avisos em 120 sorteios por motor, todos
    # inevitaveis. Alarme que nao pode ser satisfeito nao e' alarme, e' ruido
    # que ensina a ignorar o linter inteiro (a mesma licao do piso do TROCA).
    # ⚠️ A regra que sobreviveu e' o CT4 do contrato 16s: UM apelido por
    # video, repetido nos dois takes — la' a repeticao e' o desenho, nao o
    # defeito, porque o corte de 8s zera a memoria de trabalho do espectador.
    if False and len(set(usados)) < len(usados):
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
    _adjetivo_do_mecanismo(corpo, achados)

    # CTA — a ULTIMA cena e' sempre a do CTA, tenha o motor 3 cenas ou 2.
    # ⛔⛔ ERA `falas[2]`, CRAVADO — 2026-08-08. Com o nascimento da familia
    # 16s (dois takes) isso virou IndexError no primeiro sorteio do TROCA 16,
    # que e' o unico dos cinco que usa `lint_curto` em vez de `lint` proprio.
    # ⭐ `falas[-1]` E' O MESMO INDICE para os motores de 3 cenas — e nao e' um
    # remendo: as duas linhas de `lint_isca_cta`/`lint_cta_literal` mais abaixo
    # neste mesmo arquivo JA' usavam `falas[-1]` para dizer "a cena do CTA".
    # A linha aqui e' que estava fora do idioma do proprio arquivo.
    # ⚠️ PROVADO, nao afirmado: hash das acusacoes de lint() dos 23 motores em
    # 60 sorteios cada, antes e depois — identico em 23 de 23.
    cta = falas[-1]
    # ⚠️ As tres travas abaixo saem da keyword ATUAL, nao do literal `gelatin`
    # (2026-08-15). Cravadas, elas reprovariam em 100% qualquer motor de
    # keyword trocada — e foi exatamente esse o modo de falha que apagou o CT1
    # nos tres BANHO sem ninguem ver.
    _kw = keyword_do_motor(base)
    if _kw not in cta.lower():
        achados.append(("ERRO", "CTA da cena 3 sem a keyword %s" % _kw.upper()))
    if _kw.upper() in cta:
        achados.append(("ERRO", "keyword em CAIXA ALTA no Dialogue: — em ALL "
                                "CAPS o Veo soletra; usar '%s'" % _kw))
    if ("%s," % _kw) not in cta and ("%s." % _kw) not in cta:
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
    # ⛔⛔ O PRIMEIRO BLOCO E' O QUE APRESENTA — e ele era identificado pela
    # STRING `01/03`, cravada na familia de 3 cenas. Nos motores de 16s o
    # primeiro bloco chama-se `01/02`, entao ele NAO era pulado e a ancora `the
    # same N-year-old` era cobrada justamente do bloco que apresenta o homem.
    # ⚠️ Passou despercebido nos sete primeiros 16s porque nenhum deles tem
    # homem na cena 1 — o EXTERIOR 16 e' o primeiro, e reprovou de cara.
    # ⭐ Agora o primeiro e' o MENOR da ordem alfabetica dos IMAGE, que e' o
    # `01/xx` em qualquer familia: 3 cenas, 2 cenas ou a que vier.
    _imgs = sorted(k for k in blocos if k.startswith("IMAGE"))
    for nome in _imgs:
        if _imgs and nome == _imgs[0]:
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
    # ⛔⛔ 2026-08-14: a negacao anti-celebridade nunca volta. Vale para TODO
    # agente SHORT, inclusive os que ainda vao nascer — regra que some sem
    # guarda volta no proximo agente nascido por copia, e foi exatamente assim
    # que a clausula chegou aos 30 motores. Os motores que nao passam por aqui
    # chamam `sc.lint_anticeleb` no proprio `lint()`.
    lint_anticeleb(blocos, achados)
    # ⛔⛔ 2026-08-05: TAKE contra IMAGE. Vale para TODO agente SHORT, inclusive
    # os que ainda vao nascer. `objetos_ok` deixa o motor declarar as excecoes
    # que ele CONFERIU — e declarar excecao e' declarar que alguem olhou.
    lint_take_vs_image(blocos, achados, objetos_ok)
    if falas:
        lint_isca_cta(falas[-1], achados, "a cena 3 (CTA)")
        lint_cta_literal(falas[-1], achados, "a cena 3 (CTA)", base)

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
    # ⛔⛔ O TAMANHO VEM DO MAPA, nao mais cravado em tres. A familia 16s passa
    # um `mapa_copy` de DOIS e a linha antiga indexava `mapa_copy[2]` — que
    # nao existe — estourando `IndexError: tuple index out of range` no
    # primeiro sorteio.
    # ⚠️ Cada posicao do mapa diz de onde vem a fala daquela cena: um numero
    # aponta para a fala do motor base, e `None` significa "esta e' a fundida".
    # Comportamento dos motores de 3 cenas INALTERADO por construcao.
    spec["falas"] = [fundir(spec, rng) if orig is None
                     else spec["falas_base"][orig - 1]
                     for orig in mapa_copy]
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
# ---------------------------------------------------------------------------
# ⭐⭐ E A PALAVRA VIROU CAMPO — 2026-08-15
# ---------------------------------------------------------------------------
# Ordem do operador: *"todos os agentes16 meus devem levar um ui ux input
# pertinente para alterar a palavra chave X do cta (que atualmente esta
# hardcoded em Gelatin)"*.
#
# ⛔⛔ O QUE MUDA E' A KEYWORD, NUNCA O MECANISMO. `gelatin` vive em TRES
# camadas neste repo, e so' a primeira e' esta:
#   1. a KEYWORD do CTA (`Comment gelatin,`) — o gatilho da automacao de DM;
#   2. o MECANISMO (`gelatin trick`) — o que a VSL vende, ~1.010 das 2.003
#      ocorrencias do parque. Trocar isto quebra a congruencia inviolavel;
#   3. o ROTULO DA CAIXA em quadro (`HORSE GELATIN`) — cena, alcada do
#      operador, e o `_ho1_caixa` do HORSE 16 EXIGE.
# Por isso a troca acontece sobre `spec["falas"]` e com o recorte ancorado em
# `Comment `: e' o que mantem as tres camadas separadas.
#
# ⚠️ E POR QUE NAO REPARAMETRIZAR OS POOLS: 22 motores interpolam a constante
# (`"%s and ..." % sc.CTA_LITERAL`), mas ~23 cravam a string na copy — 432
# linhas em 35 arquivos. Redigitar copy validada e' o erro que este repo ja'
# pagou. A troca e' SUBSTITUICAO VERIFICADA sobre a fala pronta.
KEYWORD_PADRAO = "gelatin"
_KEYWORD = KEYWORD_PADRAO

# ⛔ Palavras que NAO podem ser keyword, por fato medido em campo e nao por
# gosto: a automacao de DM responde a palavra CADASTRADA, e estas tem dono.
BANIDAS_KEYWORD = {
    "book": "quebra a automacao de DM — o TRIO 16 herdou `book` da fonte e "
            "teve de virar `gelatin`",
    "yes": "quebra a automacao de DM (proibida junto com `book` desde o "
           "WORKFLOW)",
    "comment": "e' o proprio verbo do comando — `Comment comment,` nao existe",
}


_KEYWORD_EXPLICITA = False


def keyword():
    """A palavra que o espectador tem de comentar, agora."""
    return _KEYWORD


def keyword_do_motor(base):
    """A keyword que VALE para ESTE motor.

    ⛔⛔ BURACO ACHADO AO CONSTRUIR O VICK 16, e ele derrubaria os tres BANHO do
    mesmo jeito: um motor cuja `KEYWORD_NATIVA` nao e' `gelatin` reprovava o
    proprio CTA em 100% dos sorteios quando rodado FORA do painel — porque as
    lentes liam a keyword do PROCESSO (`gelatin`, o padrao) e a fala carregava a
    nativa. O linter acusava copy que esta' certa, que e' a §16 das licoes.
    ⭐ A regra: se o operador trocou a palavra na tela, vale a dele; se ninguem
    trocou, vale a que os POOLS deste motor carregam escrita.
    """
    if _KEYWORD_EXPLICITA:
        return _KEYWORD
    return (getattr(base, "KEYWORD_NATIVA", KEYWORD_PADRAO) or
            KEYWORD_PADRAO).lower()


def cta_literal():
    """O comando completo, montado da keyword atual."""
    return "Comment %s," % _KEYWORD


def checar_keyword(palavra):
    """Devolve "" quando a palavra serve, ou a razao de nao servir.

    ⛔ Recusa em vez de avisar: keyword invalida nao produz video ruim — produz
    video que pede um comentario que NAO ACIONA NADA, e isso so' aparece dias
    depois, quando o operador estranha que ninguem recebeu a DM.
    """
    w = (palavra or "").strip()
    if not w:
        return "a keyword nao pode ficar vazia"
    if not re.fullmatch(r"[A-Za-z]{3,20}", w):
        return ("keyword tem de ser UMA palavra de 3 a 20 letras, sem espaco, "
                "numero ou acento — o Whisper transcreve o audio e a automacao "
                "casa a palavra exata")
    if w.lower() in BANIDAS_KEYWORD:
        return "`%s` esta' proibida: %s" % (w.lower(), BANIDAS_KEYWORD[w.lower()])
    return ""


def definir_keyword(palavra):
    """Troca a keyword do processo. Levanta ValueError se ela nao servir."""
    global _KEYWORD, CTA_LITERAL
    motivo = checar_keyword(palavra)
    if motivo:
        raise ValueError(motivo)
    global _KEYWORD_EXPLICITA
    _KEYWORD = palavra.strip().lower()
    _KEYWORD_EXPLICITA = True
    # ⚠️ A constante continua existindo e continua sendo a fonte dos 22 motores
    # que a interpolam. Ela e' REESCRITA aqui, e nao substituida por uma
    # funcao, porque `lint_cta_literal` a le' no momento da chamada — e os
    # pools que ja' a interpolaram no import sao consertados pelo
    # `trocar_keyword` sobre a fala, que e' o outro lado deste par.
    CTA_LITERAL = cta_literal()
    return _KEYWORD


# ⚠️ ANCORADO EM `Comment `, e essa ancora e' a feature inteira. Um
# `replace("gelatin", nova)` cru atingiria `gelatin trick` (o mecanismo) e o
# rotulo da caixa em quadro — 81% das ocorrencias sao justamente essas.
# ⚠️ E casa as QUATRO formas medidas no parque: `Comment gelatin,` (39x),
# `Comment gelatin` sem pontuacao (8x), `Comment gelatin.` (1x) e o
# `Comment Recipe` de caixa alta e sem virgula do BANHO 16 3T. O grupo 1
# preserva a capitalizacao original do verbo.
def trocar_keyword(texto, de, para):
    """Troca a palavra DO COMANDO do CTA, e nada mais."""
    if not texto or not de or de.lower() == (para or "").lower():
        return texto
    return re.sub(r"\b(Comment\s+)%s\b" % re.escape(de), r"\g<1>" + para,
                  texto, flags=re.I)


def aplicar_keyword(falas, nativa=KEYWORD_PADRAO):
    """As falas com a keyword ATUAL no lugar da NATIVA do motor.

    ⛔ `nativa` existe porque a palavra ja' NAO era uniforme antes desta
    feature: os tres BANHO usam `recipe` por ordem de 2026-08-13. Assumir
    `gelatin` para todos reescreveria uma excecao declarada em silencio.
    """
    if _KEYWORD == (nativa or "").lower():
        return list(falas)
    return [trocar_keyword(f, nativa, _KEYWORD) for f in falas]


CTA_LITERAL = "Comment gelatin,"


def lint_cta_literal(fala_cta, achados, rotulo="a cena do CTA", base=None):
    """O comando tem de ser o literal, sem variacao de verbo.

    ⚠️ `base` opcional: com o modulo do motor em maos a lente usa a keyword
    NATIVA dele. Sem ele, cai no literal do processo — que e' o comportamento
    de sempre para os 22 motores que nao declaram nada.
    """
    literal = ("Comment %s," % keyword_do_motor(base)) if base else CTA_LITERAL
    if literal not in (fala_cta or ""):
        achados.append(("ERRO", "%s sem o literal %r — a legenda do video sai "
                                "do audio, e comando variavel faz o modelo "
                                "parafrasear a keyword (ordem do operador "
                                "2026-08-02)" % (rotulo, literal)))


# ###########################################################################
# ⭐⭐⭐ CONTRATO DE COPY DA FAMILIA 16s — v2, 2026-08-10
# ###########################################################################
# ⛔ ORDEM DO OPERADOR: *"agentes troca16, ressurreicao16, exterior16,
# flagrante16, pee16, escandalo16, colo16 precisam de reformulacao total de
# suas copys"*, depois de uma revisao adversarial de 6 lentes independentes
# sobre 3 lotes renderizados (127 achados, 79 derrubados na refutacao, 48 de
# pe'). Doutrina completa e o porque de cada regra:
#     funil-organico/CONTRATO-COPY-16S.md
#
# ⚠️⚠️ POR QUE ISTO E' CODIGO E NAO SO' DOCUMENTO. Os sete defeitos abaixo
# foram MEDIDOS nos sete motores antes da reforma, 200 sorteios cada:
#
#     sentenca depois do CTA ......... 100% em 6 de 7 motores
#     `gelatin trick` como rotulo nu .. 60% a 100%
#     ingrediente entregue de graca ... 56% e 62% (ESCANDALO, RESSURREICAO)
#     verbo de ereccao no take do CTA . 12% a 100%
#     apelido do orgao muda no corte .. 98% a 100%
#
# Nao ha' um so' desses que um humano pegue relendo o pool: todos aparecem na
# COMBINACAO. Regra que so' vive em Markdown volta em duas semanas.
#
# ⭐ A ESTRUTURA TRAVADA DO VIDEO:
#     TAKE 1   gancho visual + A FALHA DELE, com dano concreto
#     TAKE 2   mecanismo COM RAZAO -> (prova) -> follow -> CTA        <- fim
#
# ⛔ E A DESCOBERTA QUE FAZ A CONTA FECHAR: a cobertura social nao cabe como
# beat proprio em 25 palavras. Ela mora DENTRO da sentenca do CTA —
# `Comment gelatin, and the recipe goes to your messages.` custa as MESMAS 9
# palavras do CTA antigo e entrega de graca (a) o endereco da entrega, (b) a
# privacidade e (c) o fato de que nao e' na tela publica. O KPI e' uma
# confissao publica num feed onde o comentario leva nome e foto; sem essa
# clausula, quanto melhor o diagnostico em 2a pessoa, mais caro fica comentar.

# ⚠️ Verbos que qualificam como RAZAO ao lado do `gelatin trick`. Lista
# generosa e para CRESCER — o que ela proibe e' o rotulo NU (`The gelatin
# trick is the half that works.`), nao um verbo especifico.
# ⛔ Nenhum verbo de ereccao entra aqui: `hard`, `stands up`, `works again` sao
# a licao paga em campo no COLO 16 (~95% de recusa do gerador, 2026-08-09).
VERBOS_EFEITO_16 = (
    "opens", "open", "firms", "firm", "fills", "fill", "feeds", "feed",
    "restores", "restore", "carries", "carry", "puts", "put", "brings",
    "bring", "holds", "hold", "keeps", "keep", "loosens", "loosen",
    "unblocks", "unblock", "clears", "clear", "moves", "move", "pushes",
    "push", "reaches", "reach", "does", "did", "changes", "changed",
    # + 2026-08-10: `sends` faltava e reprovou `The gelatin trick sends blood
    # flow to your {o}` — um mecanismo com verbo e alvo perfeitos. Terceira vez
    # no dia em que uma lista de verbos cresce por ter reprovado copy certa.
    # + `unchokes`, do NECROSE 16: e' o verbo que casa com o mecanismo do
    # angulo (`the blood flow got strangled`), e a lente o reprovava.
    "unchokes", "unchoke", "unclogs", "unclog", "revives", "revive",
    "sends", "send", "drives", "drive", "returns", "return", "repairs",
    "repair", "frees", "free",
    "fixed", "fixes", "turned", "turns", "ended", "ends", "stops", "stopped",
    "starts", "started", "gave", "gives", "made", "makes", "worked", "works",
    # + 2026-08-16, ao construir o DESCARTE 16: a lista tinha `clears`/`clear`
    # e NAO tinha o PASSADO `cleared` — que e' o verbo verbatim de tres dos
    # sete videos da fonte (*"It cleared the old blood blocking my flow"*,
    # v07/v06/v05). Um angulo que conta no PASSADO reprovava em 310 de 400
    # sorteios em cima de copy que esta' certa. Sexta vez que esta lista cresce
    # pelo mesmo motivo, e o conserto e' sempre o mesmo: a lente aprende o
    # verbo, a copy nao se dobra ao regex.
    # ⚠️ MEDIDO ANTES DE ENTRAR: `medir_copy16.py --gate` antes e depois. Somar
    # verbo aqui so' pode TIRAR acusacao do CT3, nunca criar — e o gate saiu
    # identico nos motores que ja' passavam.
    "cleared", "opened", "filled", "restored", "unblocked", "freed",
)

# ⛔ O ALVO: o mecanismo tem de dizer sobre O QUE ele age. Sem alvo, `blood
# flow` solto vende circulacao ou coracao, que e' outra categoria de produto
# (§17 — causa nomeada sem dizer o que ela quebra).
ALVOS_16 = ("blood", "body", "flow", "pressure")

# ⛔ A sentenca do CTA tem de dizer ONDE a receita chega. E' a cobertura
# social e a mecanica da entrega no mesmo folego.
ENTREGA_16 = re.compile(
    r"\b(your (messages?|inbox|dms?)|by message|in private|nobody (else )?sees)\b",
    re.I)

# ⛔⛔ CT8 — NENHUM PEDIDO DE FOLLOW NA FALA. Ordem do operador, 2026-08-10:
#     *"eu tb nao acho que deva ter que ter follow me no cta, a mensagem e'
#      enviada independente de seguirem ou nao"*
# ⚠️⚠️ ISTO REVERTE DOUTRINA ANTIGA, e a reversao e' de FATO, nao de gosto: o
# gate de follow existia no repo inteiro porque se acreditava que a automacao
# de DM so' alcancava seguidor. O operador, que e' quem opera a automacao,
# corrigiu a premissa. Toda a familia de pools GATES/FOLLOWS/GATES16/FOLLOWS16
# nasceu dessa premissa errada — sao 6 a 11 entradas por motor de copy que
# nunca deveria ter existido, ocupando 2 a 5 palavras num take de 25.
# ⭐ E o CT1 nasceu justamente porque esse beat vivia DEPOIS do CTA. Com o
# follow fora, o defeito mais caro do lote (100% dos sorteios em 6 de 7
# motores) deixa de ter de onde vir.
# ⚠️ A lente T16-2 (o `follow` nunca encosta na keyword) fica onde esta': ela
# passa a ser rede de seguranca para o dia em que alguem reintroduzir o beat.
FOLLOW_16 = re.compile(
    r"\b(follow(ers?|ing)?\b(?!\s*-?\s*up)|non-followers)\b", re.I)

# ⛔⛔ CT4b — OS TRES APELIDOS. Ordem do operador, 2026-08-10: *"quero que vc
# use weiner e john-son pra se referir ao orgao tb, nao apenas pec-ker"*.
# ⚠️ O CT4 trava UM apelido POR VIDEO; sem o CT4b isso vira UM apelido para o
# LOTE INTEIRO, que e' o mode-collapse com cara de consistencia. A variacao
# tem de existir ENTRE videos, e e' aqui que ela e' cobrada.
# ⛔ `soldier` saiu: soa filme de guerra para ouvido americano (revisao
# adversarial, lente de ouvido nativo). `tool` saiu por ambiguidade em giria
# dos EUA. Os dois continuam no `NUCLEO` de cada motor porque as lentes os
# usam para DETECTAR o orgao — o que muda e' que nao sao mais SORTEAVEIS.
APELIDOS_16 = ("pecker", "wiener", "Johnson")


def orgaos_sorteaveis(rng, n):
    """`n` apelidos do orgao, sorteados SO' entre os tres autorizados.

    ⛔ ORDEM DO OPERADOR, 2026-08-10, e ela vale para o PARQUE INTEIRO, nao so'
    para os 16s: *"todos os agentes que apresentam soldier como termo alusivo
    devem receber a pool de opcoes de termos alusivos wiener, john-son, peck-er
    somente"*.
    ⚠️ MEDIDO ANTES: 27 motores sorteavam termo fora dos tres — `tool` em ate'
    74% dos videos (receita_short) e `soldier` em ate' 72%. O FALTA sorteava
    ainda `manhood`, `member` e, pior, `john-son`/`peck-er` JA' HIFENIZADOS
    dentro da FALA: a hifenizacao e' do TAKE (ela existe para o Veo nao soletrar
    a palavra), e na fala ela vira texto quebrado.
    ⛔ `soldier` soa filme de guerra para ouvido americano e `tool` e' ambiguo
    em giria dos EUA — os dois seguem no `NUCLEO` de cada motor porque as
    LENTES os usam para DETECTAR o orgao. O que muda e' que nao sao sorteaveis.

    ⚠️ COM TRES TERMOS E CINCO CENAS NAO HA' COMO NAO REPETIR, e isso e'
    aritmetica, nao descuido: embaralha-se os tres e repete-se em ciclo, de modo
    que as N primeiras cenas nunca repitam entre si antes de esgotar o trio.
    """
    base = list(APELIDOS_16)
    rng.shuffle(base)
    return [base[i % len(base)] for i in range(n)]

# ⛔ Verbo de ereccao na fala do CTA — ali e' claim NOSSO sobre o produto.
# ⚠️ No take 1 da isca absurda ele e' permitido: la' a promessa e' justamente
# a que vai ser desmentida meio segundo depois, e proibi-la mataria o angulo.
ERECAO_16 = re.compile(
    r"\b(hard|harder|hardness|stands? up|stood up|wakes? up|woke up|"
    r"works? again|is back|comes? back|came back|swells?|swelling|erect)\b",
    re.I)

# ⛔ Ingrediente na fala = moeda gasta antes do pedido. A receita e' a UNICA
# coisa que o comentario compra; nomear o conteudo dela na tela publica esvazia
# o CTA nao so' deste video, mas dos outros 49 da mesma pagina.
# ⚠️ `gelatin` NAO entra: ela e' a keyword, tem de ser dita.
INGREDIENTES_16 = re.compile(
    r"\b(pomegranate|collagen|cacao|cocoa|garlic|parsley|cayenne|beet(root)?|"
    r"turmeric|ginger|honey|cinnamon|watermelon|citrulline|arginine|"
    r"maca|ginseng|nettle|celery|spinach|olive oil|coconut oil|flaxseed|"
    r"peanut butter|aloe|apple cider vinegar|baking soda|"
    # + 2026-08-12: `lemon` e `lime` FALTAVAM, e o buraco so' apareceu ao
    # construir o PRATO 16 — cujo angulo nomeia limao na fala. A lista conhecia
    # `baking soda` e nao conhecia o ingrediente mais comum de receita de
    # cozinha do repertorio inteiro (CHA, BOTICA e RECEITA todos o mostram em
    # cena). Qualquer motor podia entrega-lo na fala do CTA e o CT5 aplaudia.
    # ⚠️ MEDIDO ANTES DE ENTRAR: varredura de 60 sorteios em cada um dos 19
    # motores de 16s — NENHUM diz `lemon`/`lime` na fala do CTA hoje. A trava
    # fecha um buraco sem reprovar producao nenhuma que exista.
    r"lemons?|limes?)\b", re.I)

# ⛔⛔ A EXCLUSAO DA KEYWORD ERA POR AUSENCIA, e ausencia nao acompanha uma
# palavra que virou campo (2026-08-15). O comentario acima diz *"`gelatin` NAO
# entra: ela e' a keyword, tem de ser dita"* — verdade enquanto a keyword FOSSE
# `gelatin`. Com o campo, duas coisas passam a ser possiveis e as duas quebram
# em silencio:
#   · a keyword nova ser um item DA LISTA (`honey` e `ginger` sao candidatas
#     obvias — o repo tem angulo de mel e de cha) e o CT5 reprovar o proprio
#     CTA em 100% dos sorteios;
#   · `gelatin` deixar de ser keyword e continuar ISENTA, virando o unico
#     ingrediente do parque que pode ser entregue de graca na fala.
# Por isso a regra agora e' declarativa: a keyword ATUAL nunca conta como
# ingrediente, e `gelatin` volta a contar assim que deixar de ser keyword.
# ⚠️ `(?!\s+trick)` — e ele custou uma medicao. Sem a exclusao, `gelatin` era
# contado dentro de `gelatin trick`, que e' o MECANISMO e nao ingrediente: o
# CT5 reprovava o proprio CTA em 17 dos 25 motores assim que a keyword mudava.
# O erro era meu, do mesmo tipo que esta feature existe para impedir — confundir
# as duas camadas da palavra.
_RX_GELATINA = re.compile(r"\bgelatin[ea]?\b(?!\s+trick)", re.I)


def ingrediente_na_fala(txt):
    """O primeiro ingrediente nomeado na fala, ou None."""
    kw = keyword()
    for m in INGREDIENTES_16.finditer(txt or ""):
        if m.group(0).lower() != kw:
            return m.group(0)
    if kw != KEYWORD_PADRAO:
        m = _RX_GELATINA.search(txt or "")
        if m:
            return m.group(0)
    return None


_RX_SENT = re.compile(r"(?<=[.!?])\s+")


def _sentencas16(txt):
    return [s.strip() for s in _RX_SENT.split(txt or "") if s.strip()]


def lint_copy16(base, spec, achados, isca_absurda=True):
    """As sete travas do contrato de copy 16s. Chamada pelo `lint` do motor.

    base          — o modulo do motor (usa `NUCLEO`)
    isca_absurda  — True quando o take 1 do angulo E' uma promessa falsa que
                    ele mesmo desmente (TROCA, EXTERIOR, COLO). So' muda o
                    CT7: la' o verbo de ereccao e' a isca, nao o claim.
    """
    falas = spec["falas"]
    if len(falas) < 2:
        return
    f1, f2 = falas[0], falas[-1]
    sents = _sentencas16(f2)

    # --- CT1 — nada depois da sentenca do CTA -----------------------------
    # ⛔ O defeito mais caro do lote antigo, e o unico que estava em 6 de 7
    # motores em 100% dos sorteios. A ultima coisa no ouvido, colada no unico
    # pedido que gera receita, era `The algorithm hides me from non-followers`
    # / `Followers get answered first` / `Follow me.` — expectativa negativa,
    # condicional na recompensa, ou um segundo CTA nu. A posicao final e' a
    # que fica; ela tem de ser o pedido.
    #
    # ⛔⛔ SAO DUAS PERGUNTAS, E ELAS ERAM UMA SO' — defeito ACHADO EM CAMPO,
    # nao previsto (2026-08-15). A ancora era o substring cravado
    # `"comment gelatin"`; os tres BANHO usam `recipe` desde 2026-08-13, entao
    # `icta` era SEMPRE None neles, o `elif` NUNCA executava, e a funcao real
    # do CT1 — *nada depois da sentenca do CTA* — estava DESLIGADA DE FATO nos
    # tres havia dois dias. O CT6 morria junto (ele e' guardado por
    # `icta is not None`). E o `DESLIGADAS` perdoava o CT1 do BANHO por um
    # motivo DIFERENTE do que ele estava acusando, entao o gate imprimia
    # `0 de 1 — nenhum`. Trava que deixa de medir sem dizer nada e' a §41 das
    # licoes: forma verificada, funcao nao.
    # ⭐ Agora: se a keyword nao casar, isso vira UMA acusacao — e a posicao
    # continua sendo cobrada pela sentenca que tem `comment`, seja qual for a
    # palavra depois dele.
    kw = keyword_do_motor(base)
    icta = next((i for i, s in enumerate(sents)
                 if ("comment %s" % kw) in s.lower()), None)
    if icta is None:
        achados.append(("ERRO", "CT1: a fala do CTA nao tem a sentenca "
                                "`Comment %s,`" % kw))
        icta = next((i for i, s in enumerate(sents)
                     if "comment" in s.lower()), None)
    if icta is not None and icta != len(sents) - 1:
        achados.append(("ERRO", "CT1: ha' %d sentenca(s) DEPOIS do CTA (%r) — "
                                "o video tem de terminar no pedido, e o follow "
                                "vem ANTES dele"
                        % (len(sents) - 1 - icta, sents[-1])))

    # --- CT2 — a falha masculina e' enunciada no take 1 -------------------
    # ⛔ Em dois dos tres videos revisados nao existia UMA sentenca dizendo o
    # que o corpo dele faz de errado (`never changes` descreve nada). Sem
    # auto-reconhecimento nao ha' comentario: ele nao comenta porque a copy e'
    # boa, comenta porque se viu.
    # ⚠️ LISTA PARA CRESCER, e ela ja' cresceu uma vez no dia em que nasceu: a
    # primeira versao nao conhecia `killed` e reprovou `Same squeeze killed his
    # pecker two years ago` — uma sentenca que enuncia a falha melhor do que
    # metade da lista. Lente que reprova o que esta' certo e' o §16, e o
    # conserto e' a lente aprender o verbo, nao a copy se dobrar ao regex.
    if not re.search(r"\b(quit|quits|quitting|soft|softens|stopped|stops|"
                     r"dead|died|gave out|gives out|lose it|lost it|loses it|"
                     r"never works|doesn't work|does not work|hasn't worked|"
                     r"can't finish|couldn't|won't|failed|fails|shut down|"
                     r"went out|not working|no longer|killed|kills|wrecked|"
                     r"ruined|finished|gone|useless|nothing happens|"
                     # + 2026-08-10, segunda vez que a lista cresce no mesmo
                     # dia: reprovava `My pecker did nothing for eight months`
                     # e `My pecker hadn't worked in a year`, que enunciam a
                     # falha melhor que metade da lista. A lente aprende o
                     # verbo; a copy nao se dobra ao regex.
                     # + `has not worked` (a forma SEM contracao — a lista so'
                     # conhecia `hasn't worked`) e `hasn't stood`, do NECROSE
                     # 16. Quarta vez que esta lista cresce hoje, sempre pelo
                     # mesmo motivo: ela reprovou copy que enuncia a falha.
                     r"has not worked|hasn't stood|hasnt worked|"
                     # + `struggling to stay hard`, do FIGHT 16 — e' o hook
                     # VERBATIM da fonte, e enuncia a falha em 2a pessoa sem
                     # nomear o orgao (a formula segura do GOOD). Quinta vez que
                     # esta lista cresce por reprovar copy certa.
                     r"struggl\w*|can't stay|cannot stay|can't keep it|"
                     r"did nothing|does nothing|doing nothing|hadn't worked|"
                     r"had not worked|never worked|stopped responding)\b",
                     f1, re.I):
        achados.append(("AVISO", "CT2: o take 1 nao enuncia FALHA nenhuma — "
                                 "sem dano concreto o espectador nao se "
                                 "reconhece e nao comenta"))

    # --- CT3 — `gelatin trick` com razao na mesma sentenca ----------------
    # ⛔ Nome de mecanismo sem razao ao lado nao vira crenca: vira ruido de
    # marca. `The gelatin trick is the half that works.` nao diz o que a
    # gelatina FAZ, e o espectador nao tem no que acreditar.
    for s in sents + _sentencas16(f1):
        if "gelatin trick" not in s.lower():
            continue
        baixo = s.lower()
        tem_verbo = any(re.search(r"\b%s\b" % v, baixo) for v in VERBOS_EFEITO_16)
        tem_alvo = (any(n.lower() in baixo for n in base.NUCLEO)
                    or any(a in baixo for a in ALVOS_16))
        if not (tem_verbo and tem_alvo):
            achados.append(("ERRO", "CT3: `gelatin trick` sem razao em %r — a "
                                    "sentenca precisa de VERBO de efeito e de "
                                    "ALVO (o orgao, o sangue, o corpo)" % s))
        break

    # --- CT4 — um apelido do orgao por video ------------------------------
    # ⛔⛔ ISTO REVERTE A REGRA ANTERIOR, e a reversao e' declarada. Ate' hoje
    # varios motores EXIGIAM substantivos DIFERENTES entre as cenas ("duas
    # mencoes iguais em 16 segundos sao bordao") — e o resultado medido foi o
    # apelido mudando no corte em 98-100% dos videos. Em 24s e cinco cenas o
    # bordao e' o risco; em 16s e duas cenas o risco e' o oposto: o corte
    # zera a memoria de trabalho, e trocar `soldier` por `Johnson` no segundo
    # 9 obriga o espectador a remapear justamente quando ele ja' esta' com um
    # pe' fora. A variacao continua existindo ENTRE videos, que e' onde ela
    # nunca custou nada.
    n1 = {n for n in base.NUCLEO if n.lower() in f1.lower()}
    n2 = {n for n in base.NUCLEO if n.lower() in f2.lower()}
    if n1 and n2 and not (n1 & n2):
        achados.append(("ERRO", "CT4: o apelido do orgao MUDA no corte (%s -> "
                                "%s) — um termo por video, repetido nos dois "
                                "takes" % (sorted(n1), sorted(n2))))

    # --- CT5 — nenhum ingrediente nomeado na fala do CTA ------------------
    m = ingrediente_na_fala(f2)
    if m:
        achados.append(("ERRO", "CT5: a fala do CTA entrega o ingrediente %r —"
                                "a receita e' a UNICA moeda que o comentario "
                                "compra, e entregue uma vez ela esta' gasta "
                                "para todos os videos da pagina" % m))

    # --- CT6 — a sentenca do CTA diz ONDE a receita chega -----------------
    if icta is not None and not ENTREGA_16.search(sents[icta]):
        achados.append(("AVISO", "CT6: o CTA nao diz que a receita chega por "
                                 "MENSAGEM — o comentario leva nome e foto, e "
                                 "sem a cobertura o custo social de comentar "
                                 "fica maior que a curiosidade"))

    # --- CT7 — verbo de ereccao COM O ORGAO na mesma sentenca -------------
    # ⚠️⚠️ A PRIMEIRA VERSAO DESTA TRAVA PROIBIA O TOKEN EM QUALQUER LUGAR DA
    # FALA, e ela acusou o GOOD 16 em 87% dos sorteios — em cima de
    # `This leaves your body harder than it has felt in decades`, que e' a copy
    # DA FONTE de um video que converte e que passa no gerador justamente por
    # falar do CORPO. A licao paga no COLO nao e' sobre a palavra: e' sobre a
    # palavra COLADA NO ORGAO. `your soldier hard` reprova; `your body harder`
    # nao. Sem esta precisao a lente proibiria a unica formula segura que o
    # parque tem — e' o modo de falha §16, lente que reprova o que esta' certo.
    def _erecao_no_orgao(fala, rotulo):
        for s in _sentencas16(fala):
            m = ERECAO_16.search(s)
            if not m:
                continue
            if any(n.lower() in s.lower() for n in base.NUCLEO):
                achados.append((
                    "ERRO",
                    "CT7: %s diz %r na mesma sentenca do orgao (%r) — verbo que "
                    "descreve o orgao voltando a funcionar e' lido como "
                    "tumescencia e reprova no gerador (licao paga no COLO 16, "
                    "~95%% dos takes 1). Sobre o CORPO passa; sobre o ORGAO nao."
                    % (rotulo, m.group(0), s)))
                return

    _erecao_no_orgao(f2, "a fala do CTA")
    if not isca_absurda:
        _erecao_no_orgao(f1, "o take 1 (e este angulo nao tem isca absurda "
                             "para desmentir)")

    # --- CT8 — nenhum pedido de follow na fala ----------------------------
    for i, f in enumerate(falas, 1):
        m = FOLLOW_16.search(f)
        if m:
            achados.append(("ERRO", "CT8: o take %d pede follow (%r) — a DM sai "
                                    "para seguidor e nao-seguidor igual (ordem "
                                    "do operador 2026-08-10). O beat inteiro "
                                    "sai, e as palavras vao para o mecanismo"
                            % (i, m.group(0))))

    # --- CT4b — o apelido sorteado e' um dos tres -------------------------
    usados = n1 | n2
    fora = [n for n in usados if n.lower() not in
            [a.lower() for a in APELIDOS_16]]
    if fora:
        achados.append(("ERRO", "CT4b: o video usa %s — os apelidos sorteaveis "
                                "sao %s. `soldier` soa filme de guerra para "
                                "ouvido americano e `tool` e' ambiguo em giria "
                                "dos EUA; os dois seguem no NUCLEO so' para as "
                                "lentes DETECTAREM o orgao"
                        % (sorted(fora), list(APELIDOS_16))))


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


# ---------------------------------------------------------------------------
# ⛔⛔ CONTRA A CELEBRIDADE, SILENCIO — a negacao saiu do PROMPT (2026-08-14)
# ---------------------------------------------------------------------------
# Ordem do operador: *"tire not a celebrity do prompt"*. A doutrina ja' existia
# desde 2026-07-31 (`licoes-producao-veo.md` §*Declaracao e' municao*) e nunca
# tinha sido aplicada aos motores — a clausula seguia viva em 30 dos 44, e em 29
# deles em 100% dos videos.
#
# ⛔ A DECLARACAO NAO E' NEUTRA: escrever a negacao POE o token no campo, e o
# classificador casa TOKEN, nao intencao. A defesa nao e' negar celebridade; e'
# descrever um rosto que nenhuma celebridade tem — e isso e' COPY, alcada do
# operador. Aqui so' se REMOVE.
# ⛔ E NAO SE TROCA POR OUTRA NEGACAO: `not a model`, `not an actor`, `not
# resembling any famous person` sao a MESMA municao com outra roupa.
#
# ⚠️ POR QUE RECORTE E NAO REESCRITA DOS POOLS: o mesmo motivo do
# `tirar_bandeira` logo acima — as 54 entradas do APELO_EUA sao copy validada, e
# redigitar copy validada e' o erro que o repo ja' pagou (o D1 comprimido na mao
# virou esqueleto 3D). A clausula e' um recorte REGULAR (comeca numa virgula ou
# num `yet`/`and`, encadeia negacoes, termina no ponto), e sai por substituicao
# verificada — `tirar_anticeleb.py`, que reescreve o FONTE uma vez so'.
#
# ⛔ E A REMOCAO E' COBRADA, NAO CONFIADA: `lint_anticeleb` varre o TEXTO
# MONTADO (§19) e reprova se a negacao voltou. Regex que erra em prosa erra em
# silencio; por isso a lente vem junto e roda em todo motor, inclusive os que
# ainda vao nascer.
#
# ⚠️ `not famous` CRU FICA DE FORA do recorte, e a ausencia e' medida: o
# ESCANDALO tem fala aprovada — *"The gelatin trick is not famous"* — onde a
# palavra significa "o truque nao e' famoso", nada de conformidade. Alcancavel
# em 26/600 sorteios. Lente que reprova copy certa ensina o operador a ignorar a
# lente inteira (licoes §16), entao a lente le' a DIRECAO e nunca a fala.
# ⚠️ O ARTIGO E' OPCIONAL E O PLURAL ENTRA — medido, nao suposto. A primeira
# versao exigia `not a|an` e deixou o VAZAMENTO intacto em 100% dos videos: la'
# a frase fala de DUAS pessoas e sai sem artigo, *"not celebrities, not models,
# not actors"*. O inventario que abriu esta tarefa listava 20 formas vivas e
# tambem nao tinha essa — quem a achou foi a medicao do prompt gerado, nao o
# grep no fonte (§19: a unica medicao que vale e' a do texto montado).
_NEG_ANTICELEB = (
    r"not\s+(?:an?\s+)?(?:celebrity|celebrities|models?|actors?|"
    r"actress(?:es)?|public\s+figures?|famous\s+(?:person|people)|"
    r"movie\s+stars?|look-?alikes?)"
    r"|not\s+resembling\s+(?:any|anyone)[^,;.]*"
)

# a clausula inteira: um separador, uma negacao, e a cauda de negacoes irmas
_ANTICELEB = re.compile(
    r"(?:^[ \t]*|,\s*(?:yet\s+|but\s+|and\s+|though\s+)?"
    r"|\s+(?:yet|but|and|though)\s+)"
    r"(?:" + _NEG_ANTICELEB + r")"
    r"(?:\s*,\s*(?:and\s+)?(?:" + _NEG_ANTICELEB + r"))*", re.I)

# ⚠️ so' espaco horizontal: `\s` comeria a quebra de linha e emendaria o
# `Dialogue:` na direcao de cena.
_SUJEIRA_ANTI = ((r"[ \t]*,[ \t]*,", ","), (r"[ \t]+and[ \t]+,", ","),
                 (r"[ \t]{2,}", " "), (r"[ \t]+([,.;])", r"\1"),
                 (r",[ \t]*$", ""), (r"[ \t]+and[ \t]*$", ""))

# o que NUNCA pode sobrar no texto montado. ⛔ `not famous` entra CRU aqui de
# proposito — a lente le' so' a direcao, entao a fala do ESCANDALO fica fora do
# alcance dela e o token continua proibido em cena.
_TEM_ANTICELEB = re.compile(
    r"celebrit(?:y|ies)"
    r"|not\s+(?:an?\s+)?(?:models?|actors?|actress(?:es)?|public\s+figures?)"
    r"|not\s+resembling"
    r"|not\s+famous", re.I)


def tirar_anticeleb(texto):
    """Devolve o texto sem a clausula de anti-celebridade, prosa normalizada.

    ⛔ Texto que nao tinha a clausula sai INTACTO — nem a normalizacao roda
    nele. Sem essa guarda a funcao "consertaria" espacos de copy validada que
    ninguem mandou tocar.
    """
    if not texto:
        return texto
    fora = _ANTICELEB.sub("", texto)
    if fora == texto:
        return texto
    for padrao, troca in _SUJEIRA_ANTI:
        fora = re.sub(padrao, troca, fora)
    return fora


def tem_anticeleb(texto):
    return _TEM_ANTICELEB.search(texto or "")


def frase_anti(texto):
    """O slot `anti` ja' pontuado e com o espaco — vazio some INTEIRO.

    ⛔ Existe por causa do FALTA: la' a clausula era negacao PURA (`not
    resembling any famous person, not a celebrity`), sem metade descritiva, e o
    template escreve `%(anti)s. `. Com o slot vazio sobrava ponto orfao e espaco
    duplo — a sujeira que a lente foi escrita para pegar. Quem normaliza e' o
    slot, nao o pool: assim a copy dos outros agentes nao e' tocada.
    """
    t = (texto or "").strip().rstrip(".").strip()
    return (t + ". ") if t else ""


def _sem_fala(texto):
    """O bloco sem as linhas de `Dialogue:` — a lente le' CENA, nunca copy."""
    return "\n".join(l for l in str(texto or "").splitlines()
                     if not l.lstrip().startswith("Dialogue:"))


def lint_anticeleb(blocos, achados, rotulo="anticeleb"):
    """A negacao de conformidade nunca volta ao texto montado.

    ⚠️ Varre o TEXTO MONTADO, nunca o pool (§19): a clausula e' montada dentro
    de um bloco maior e `grep` no fonte nao ve frase quebrada entre literais
    adjacentes.
    """
    for nome in sorted(blocos):
        txt = _sem_fala(blocos[nome])
        m = tem_anticeleb(txt)
        if m:
            achados.append(("ERRO", "%s: %s traz %r — declaracao de "
                                    "conformidade INJETA o token que ela nega. "
                                    "A defesa e' descrever o rosto, nunca "
                                    "negar (CLAUDE.md §CONTRA A CELEBRIDADE, "
                                    "SILENCIO)" % (rotulo, nome, m.group(0))))
    # ⭐ a prosa vem JUNTO — a remocao so' esta' feita quando o texto que ficou
    # ainda e' texto. Medido em 5.280 sorteios dos 44 motores, com os toggles em
    # rodizio: ZERO acusacao. Se subir, e' recorte novo que estragou frase.
    lint_prosa_anti(blocos, achados, rotulo)


def lint_prosa_anti(blocos, achados, rotulo="anticeleb"):
    """A prosa depois do recorte: sem virgula dupla, `and` orfao ou espaco duplo.

    ⭐ Funcao separada, mas CHAMADA pela `lint_anticeleb` — quem cobra a
    remocao cobra junto o estado da frase que sobrou. Fica separada para poder
    ser medida sozinha, que foi como a regra do `and,` acabou apertada.
    """
    for nome in sorted(blocos):
        txt = _sem_fala(blocos[nome])
        # ⚠️ `and[ \t]+,` EXIGE espaco DOS DOIS LADOS, e o motivo foi medido: com
        # `and[ \t]*,` a lente acusava 89 vezes em 5 motores, e o campeao era o
        # EXTERIOR — que NUNCA teve a clausula. O texto era prosa legitima,
        # *"white powder still settled over its top third, and, lying on its
        # side beside it, a well-used ..."*: um aposto em ingles escreve `and,`
        # colado. Lente que reprova o que esta' certo ensina a ignorar a lente
        # inteira (licoes §16). A sujeira da REMOCAO tem espaco antes da virgula.
        for padrao, msg in ((r",[ \t]*,", "virgula dupla"),
                            (r"[ \t]+and[ \t]+,", "'and' orfao antes de virgula"),
                            (r"[ \t]{2,}", "espaco duplo"),
                            (r"[ \t]+[,.]", "espaco antes de pontuacao")):
            if re.search(padrao, txt):
                achados.append(("ERRO", "%s: %s com %s — a remocao da negacao "
                                        "estragou a prosa" % (rotulo, nome, msg)))


def autoteste_anticeleb():
    """Controles com as clausulas REAIS dos 44 motores, e os negativos.

    ⛔ Rodam ANTES de qualquer numero ser olhado (licoes §16). Os dois ultimos
    negativos sao os que decidem o desenho da lente: a fala do ESCANDALO e o
    texto que nunca teve clausula nenhuma.
    """
    casos = [
        # a forma classica, 4 negacoes encadeadas (BOTICA, CLEAN, COLO, RECEITA)
        ("Ordinary relatable face, not a celebrity, not a model, not an actor, "
         "not resembling any famous person.",
         "Ordinary relatable face."),
        # a curta (FLAGRANTE, NECROSE, PEE, VAZAMENTO)
        ("Ordinary relatable face, not a celebrity.", "Ordinary relatable face."),
        # a do registro BELA (CHA, DUPLA, PLACA, TRIO, short_comum)
        ("A strikingly beautiful face, not a celebrity, not resembling any "
         "famous person.", "A strikingly beautiful face."),
        # o retrato do APELO_EUA — copy validada, so' a cauda sai
        ("A head-turning everyday woman, carefully groomed, with bright eyes, "
         "full lips and a striking figure, not a celebrity, not resembling any "
         "famous person.",
         "A head-turning everyday woman, carefully groomed, with bright eyes, "
         "full lips and a striking figure."),
        # ⭐ o `yet` + `not an actress` do REF_ROSTO_M da familia CLEAN
        ("A strikingly beautiful woman, her face flawless and photogenic, her "
         "hair silky, smooth and healthy with a soft shine, yet not a "
         "celebrity, not an actress, not resembling any famous person.",
         "A strikingly beautiful woman, her face flawless and photogenic, her "
         "hair silky, smooth and healthy with a soft shine."),
        # ⛔ o FALTA: negacao PURA, sem metade descritiva — vira vazio
        ("Not resembling any famous person, not a celebrity", ""),
        ("not resembling any famous person, not a celebrity", ""),
        # a clausula NO MEIO de um bloco REF inteiro (COLO, NECROSE, RECEITA)
        ("REF 01: Photo of a real person. An ordinary everyday relatable person "
         "with a plain unremarkable face, not a celebrity, not a model, not an "
         "actor, not resembling any famous person. Hands out of frame.",
         "REF 01: Photo of a real person. An ordinary everyday relatable person "
         "with a plain unremarkable face. Hands out of frame."),
        # a variante sem `not resembling` (BED, GOOD, MEL, PRATO, WIFE)
        ("An ordinary everyday relatable person with a plain unremarkable face, "
         "not a celebrity, not a model, not an actor.",
         "An ordinary everyday relatable person with a plain unremarkable face."),
        # ⭐ `and not a celebrity` — separador que nao e' virgula
        ("A plain face and not a celebrity.", "A plain face."),
        # ⛔⛔ O PLURAL SEM ARTIGO, do VAZAMENTO — a forma que a primeira versao
        # do recorte deixou passar em 100% dos videos. Duas pessoas em quadro,
        # entao a frase sai no plural e o `not a|an` nao casa.
        ("Both are ordinary everyday relatable people with plain unremarkable "
         "faces, not celebrities, not models, not actors. The scene is lit by "
         "late afternoon sun.",
         "Both are ordinary everyday relatable people with plain unremarkable "
         "faces. The scene is lit by late afternoon sun."),
    ]
    falhas = []
    for entrada, esperado in casos:
        saida = tirar_anticeleb(entrada)
        if saida != esperado:
            falhas.append("recortou errado:\n   deu = %r\n   era = %r"
                          % (saida, esperado))
        if saida and tem_anticeleb(saida):
            falhas.append("sobrou negacao em %r" % saida)
        for padrao in (r",[ \t]*,", r"[ \t]{2,}", r"[ \t]+[,.]"):
            if re.search(padrao, saida or ""):
                falhas.append("prosa suja depois do recorte: %r" % saida)
    # ⛔⛔ CONTROLE NEGATIVO 1 — a fala aprovada do ESCANDALO. `not famous` ali
    # quer dizer "o truque nao e' famoso". Se o recorte a tocar, o motor perde
    # copy do operador.
    fala = ("The famous ones did nothing for his Johnson. The gelatin trick is "
            "not famous, cheap collagen, and it got him standing again.")
    if tirar_anticeleb(fala) != fala:
        falhas.append("comeu a fala aprovada do ESCANDALO: %r"
                      % tirar_anticeleb(fala))
    # ⛔ CONTROLE NEGATIVO 2 — texto que nunca teve clausula sai intacto
    limpo = "A 58-year-old man with a broad nose and a scar above his lip."
    if tirar_anticeleb(limpo) != limpo:
        falhas.append("mexeu em texto sem clausula: %r" % tirar_anticeleb(limpo))
    # ⛔ CONTROLE NEGATIVO 3 — a lente TEM de acusar quando a negacao volta
    provas = ("A face, not a celebrity.", "not resembling any famous person",
              "an ordinary face, not a model", "not an actor")
    for p in provas:
        if not tem_anticeleb(p):
            falhas.append("a lente NAO acusa %r" % p)
    if tem_anticeleb(limpo):
        falhas.append("a lente acusa texto limpo: %r" % limpo)
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
     "marca": "a beauty mark at the hairline and even skin"},
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
     "marca": "wide-set blue eyes and a small mole above one eyebrow"},
    {"idade": 24, "corpo": "slim and toned with a dancer's line",
     "cabeca": "jet-black hair in a sleek centre part",
     "marca": "sharp cheekbones and a small mole on her jaw"},
    {"idade": 27, "corpo": "long-legged and slender with square shoulders",
     "cabeca": "platinum blonde hair in a blunt shoulder-length cut",
     "marca": "ice-blue eyes and a dimple in one cheek"},
    {"idade": 23, "corpo": "curvy and athletic with a small waist",
     "cabeca": "tight dark curls gathered high on her head",
     "marca": "smooth-skinned with high round cheekbones and a beauty mark on "
              "one cheek"},
    {"idade": 22, "corpo": "tall and slim with an hourglass line",
     "cabeca": "chestnut hair in long beachy waves",
     "marca": "a full bow-shaped mouth and warm brown eyes"},
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
     "marca": "smooth-skinned, freckled across the nose and cheeks"},
    {"idade": 21, "corpo": "long-limbed and shapely with a defined waist",
     "cabeca": "black hair in a high sleek ponytail",
     "marca": "a small beauty mark along her jawline and full brows"},
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
     "marca": "grey-green eyes and a small gold stud in one ear"},
    {"idade": 24, "corpo": "shapely and toned with a narrow waist",
     "cabeca": "ginger hair in loose curls past her shoulders",
     "marca": "heavy freckling and a small chin dimple"},
    {"idade": 27, "corpo": "tall and slim with a graceful neck",
     "cabeca": "long dark hair in a high crown braid",
     "marca": "a beauty mark high on her left cheek"},
    {"idade": 22, "corpo": "petite and shapely with a defined waist",
     "cabeca": "bleached blonde hair in a blunt chin-length bob",
     "marca": "wide dark eyes and a small dimple in her chin"},
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

    # ⭐⭐ AMPLIACAO 2026-08-13 — ordem do operador: *"mulheres no modo bela
    # devem ser sempre extremamente lindas e atraentes e com pool de opcoes bem
    # grande para sorteio"* / *"aumente o pool de opcoes substancialmente"*.
    # 38 -> 94 entradas. ⛔ NENHUMA delas escreve `beautiful`, `gorgeous` ou
    # `stunning`: julgamento no prompt puxa o rosto para a MEDIA do banco de
    # imagem, que e' o oposto de "extremamente linda". A beleza entra por FEICAO
    # E FORMA — malar alto, cintura esculpida, onda pesada e brilhante — porque
    # forma concreta o gerador desenha e elogio ele so' interpreta.
    # ⛔ ZERO COR DE PELE e zero etnia: quem manda nisso e' o motor que chama
    # (congruencia com o avatar da pagina), e duas vozes no mesmo sintagma o
    # gerador resolve inventando. Sete entradas antigas foram REESCRITAS por
    # isso e pela regra DISTINTIVO-NUNCA-DETERIORADO (quatro `scar`, um `gap
    # between her front teeth`, `deep brown skin`, `pale skin` e `a faint mark
    # between her brows`) — cicatriz e dente faltando viram mendigo, e mendigo
    # ja' custou lote no PLACA 16.
    # ⚠️ AS 28+ SAO 24 DAS 56 NOVAS E NENHUMA DIZ `curvy`. E' medicao, nao
    # gosto: RESSURREICAO/TROCA/ESCANDALO pedem `idade_min=28` e o
    # RESSURREICAO ainda passa `banidos=BANIDOS_DESEJO` (que contem `curvy`).
    # Os dois filtros em serie deixavam CINCO entradas de pe' no pool de 38 —
    # pool grande que, filtrado, entrega a mesma narradora.
    # ⛔ E NENHUMA MARCA NOVA DIZ `eyes`: o olho vem do eixo proprio
    # (OLHOS_BELAS) e o `_sem_olhos` so' limpa as tres formas que o pool velho
    # usava. Marca com olho no FIM da frase escaparia da limpeza e o prompt
    # sairia com duas cores para o mesmo par de olhos.

    # --- 28 a 33 anos: o pool que sobra depois do piso de idade -------------
    {"idade": 28, "corpo": "tall and long-limbed with square shoulders and a "
                           "high waist",
     "cabeca": "dark chocolate-brown hair in a deep side part past the "
               "collarbone",
     "marca": "high cheekbones and a small mole below one temple"},
    {"idade": 28, "corpo": "statuesque and toned with a sculpted midriff",
     "cabeca": "platinum blonde hair in a sharp blunt bob",
     "marca": "heavy level brows and a cleft in her chin"},
    {"idade": 28, "corpo": "slim and athletic with a dancer's line",
     "cabeca": "russet-red hair in a thick French braid",
     "marca": "smooth-skinned with a light spray of freckles over the nose"},
    {"idade": 28, "corpo": "compact and athletic with a small frame",
     "cabeca": "blue-black hair in a high glossy ponytail",
     "marca": "smooth-skinned with wide-set brows and a dimple in each cheek"},
    {"idade": 29, "corpo": "long-legged and lean with a narrow waist",
     "cabeca": "jet-black hair in a glossy blunt fringe and long layers",
     "marca": "a sharp jaw and a tiny gold hoop high in one ear"},
    {"idade": 29, "corpo": "tall and sculptural with swimmer's shoulders",
     "cabeca": "dark blonde hair in a low twisted chignon",
     "marca": "a straight narrow nose and a dimple in her left cheek"},
    {"idade": 29, "corpo": "shapely and strong with a sculpted back and a small "
                           "waist",
     "cabeca": "cinnamon-red hair in loose ringlets to the shoulder",
     "marca": "dense freckling over the nose and a full bow-shaped mouth"},
    {"idade": 29, "corpo": "tall and slim-hipped with a long waist",
     "cabeca": "strawberry-blonde hair in a shaggy layered cut",
     "marca": "freckled cheeks and a soft rounded jaw"},
    {"idade": 30, "corpo": "petite and toned with a small frame and a narrow "
                           "waist",
     "cabeca": "espresso-dark hair in a high sleek bun",
     "marca": "lightly freckled, with wide arched brows and a beauty mark at "
              "the corner of the mouth"},
    {"idade": 30, "corpo": "long-limbed and slim with a very straight back",
     "cabeca": "honey-blonde hair in soft finger waves",
     "marca": "a strong straight nose and a single dimple when she smiles"},
    {"idade": 30, "corpo": "tall and lean with a long torso",
     "cabeca": "tight dark coils shaped into a rounded crown",
     "marca": "sculpted cheekbones and a small gold stud in one nostril"},
    {"idade": 30, "corpo": "trim and athletic with defined arms",
     "cabeca": "mahogany-red hair in a low glossy ponytail",
     "marca": "a square jaw, smooth-skinned, with a beauty mark on one temple"},
    {"idade": 30, "corpo": "shapely with a defined waist and long legs",
     "cabeca": "sandy blonde hair in a claw-clipped twist",
     "marca": "a wide mouth and a beauty mark on the left jaw"},
    {"idade": 31, "corpo": "statuesque with a full figure and a narrow waist",
     "cabeca": "ash-brown hair in long feathered layers",
     "marca": "a wide full mouth and a small mole under the jaw"},
    {"idade": 31, "corpo": "slim and sculptural with very straight posture",
     "cabeca": "titian-red hair swept into a half-up twist",
     "marca": "smooth-skinned with heavy freckling across both cheeks"},
    {"idade": 31, "corpo": "tall and toned with square shoulders",
     "cabeca": "long box braids gathered into a high crown",
     "marca": "high round cheekbones and a small hoop in one nostril"},
    {"idade": 31, "corpo": "lean and sculptural with a high waist",
     "cabeca": "deep auburn hair in long loose waves",
     "marca": "a straight nose and a small silver stud in one nostril"},
    {"idade": 32, "corpo": "long-legged and slim with a sculpted waist",
     "cabeca": "caramel-blonde hair in a deep centre part past the shoulders",
     "marca": "an upturned nose and a faint dimple in one cheek"},
    {"idade": 32, "corpo": "athletic and shapely with strong shoulders",
     "cabeca": "dark auburn hair in a thick fishtail braid",
     "marca": "smooth-skinned with a cleft chin and a level brow line"},
    {"idade": 32, "corpo": "tall and lean with a long clean line",
     "cabeca": "black hair cropped into a soft pixie",
     "marca": "sharp cheekbones and a beauty mark above the lip"},
    {"idade": 32, "corpo": "softly toned with a full figure and a small waist",
     "cabeca": "chestnut hair in heavy glossy waves",
     "marca": "a rounded jaw and a small birthmark behind one ear"},
    {"idade": 33, "corpo": "tall and statuesque with a long line through the "
                           "shoulders",
     "cabeca": "copper hair in a blunt shoulder-length cut",
     "marca": "a dusting of freckles and a level brow line"},
    {"idade": 33, "corpo": "slim and strong with a narrow waist and long arms",
     "cabeca": "dark brown hair in a slicked-back low ponytail",
     "marca": "smooth-skinned with a defined cupid's bow and a mole on one "
              "cheekbone"},
    {"idade": 33, "corpo": "long-limbed and toned with a flat midriff",
     "cabeca": "golden blonde hair in a loose braided crown",
     "marca": "smooth-skinned with a small stud in the upper ear"},

    # --- 21 a 27 anos: o registro `novinha` que o operador pediu em 08-05 ----
    {"idade": 21, "corpo": "petite and shapely with a very narrow waist",
     "cabeca": "butter-blonde hair in a high messy topknot",
     "marca": "a rounded chin and a dimple in one cheek"},
    {"idade": 21, "corpo": "tall and slim with long legs",
     "cabeca": "raven-black hair in a blunt chin-length bob",
     "marca": "heavy level brows and a beauty mark on the cheekbone"},
    {"idade": 21, "corpo": "long-limbed and lean with a flat midriff",
     "cabeca": "ginger hair in two loose braids",
     "marca": "dense freckling from cheek to cheek"},
    {"idade": 21, "corpo": "curvy and toned with a small waist",
     "cabeca": "dark brown hair in a curtain fringe and long layers",
     "marca": "a soft square jaw and a tiny gold hoop in one nostril"},
    {"idade": 21, "corpo": "trim and athletic with a flat midriff",
     "cabeca": "cherry-red dyed hair in a long straight cut",
     "marca": "smooth-skinned with a small chin dimple"},
    {"idade": 22, "corpo": "slim and athletic with square shoulders",
     "cabeca": "bleached platinum hair in a cropped pixie",
     "marca": "sculpted cheekbones and a cleft chin"},
    {"idade": 22, "corpo": "tall and sculptural with a long torso",
     "cabeca": "copper-red hair in a high sleek ponytail",
     "marca": "smooth-skinned with a scatter of freckles over the nose"},
    {"idade": 22, "corpo": "shapely with a full figure and a narrow waist",
     "cabeca": "chestnut hair in a low loose bun",
     "marca": "freckled over the nose, full lips and a small mole at the "
              "jawline"},
    {"idade": 22, "corpo": "trim and long-legged with a high waist",
     "cabeca": "honey-blonde hair in a shoulder-length shag",
     "marca": "an upturned nose and a dimple in one cheek only"},
    {"idade": 22, "corpo": "curvy and toned with long legs",
     "cabeca": "chocolate-brown hair in a high claw-clipped twist",
     "marca": "a straight nose and a beauty mark high on one cheek"},
    {"idade": 23, "corpo": "curvy and strong with a sculpted waist",
     "cabeca": "tight coils gathered into a high puff",
     "marca": "high round cheekbones and a small gold stud in one nostril"},
    {"idade": 23, "corpo": "slim and supple with a straight back",
     "cabeca": "dark red hair in a blunt long bob",
     "marca": "smooth-skinned with a beauty mark below the right cheekbone"},
    {"idade": 23, "corpo": "tall and lean with defined arms",
     "cabeca": "black hair in a braided crown",
     "marca": "a straight nose and a faint dimple in the chin"},
    {"idade": 23, "corpo": "petite and toned with a small frame",
     "cabeca": "caramel balayage in beachy waves",
     "marca": "a wide full mouth and a mole above the lip"},
    {"idade": 23, "corpo": "tall and slim with a high waist",
     "cabeca": "ash-blonde hair in a blunt shoulder cut with a middle part",
     "marca": "heavy level brows and a cleft chin"},
    {"idade": 24, "corpo": "long-legged and slim with a narrow waist",
     "cabeca": "ash-blonde hair in a sharp blunt bob",
     "marca": "heavy arched brows and a small hoop in the upper ear"},
    {"idade": 24, "corpo": "athletic and shapely with swimmer's shoulders",
     "cabeca": "auburn hair in a thick rope braid",
     "marca": "freckled cheeks and a strong straight nose"},
    {"idade": 24, "corpo": "tall and statuesque with a long clean line",
     "cabeca": "jet-black hair in a wet-look slick back",
     "marca": "sharp cheekbones and a beauty mark on the jaw"},
    {"idade": 24, "corpo": "curvy and compact with a defined waist",
     "cabeca": "golden blonde hair in loose spiral curls",
     "marca": "a rounded jaw and a dimple in each cheek"},
    {"idade": 24, "corpo": "long-limbed and shapely with a narrow waist",
     "cabeca": "deep burgundy-dyed hair in loose waves",
     "marca": "smooth-skinned with a faint dusting of freckles"},
    {"idade": 25, "corpo": "slim and sculptural with a flat midriff",
     "cabeca": "dark chestnut hair in a middle part down to the waist",
     "marca": "a narrow nose and a small birthmark on the temple"},
    {"idade": 25, "corpo": "tall and toned with wide square shoulders and a "
                           "narrow waist",
     "cabeca": "ginger hair in a low twisted chignon",
     "marca": "smooth-skinned with dense freckling over the nose"},
    {"idade": 25, "corpo": "shapely and strong with a small waist",
     "cabeca": "long micro braids gathered over one shoulder",
     "marca": "sculpted cheekbones and a gold nose ring"},
    {"idade": 25, "corpo": "long-limbed and lean with a high waist",
     "cabeca": "platinum blonde hair in soft finger waves",
     "marca": "a cleft chin and clear even skin"},
    {"idade": 26, "corpo": "curvy and toned with a very narrow waist",
     "cabeca": "mahogany-red hair in long layers",
     "marca": "a full bow-shaped mouth and a mole on one cheek"},
    {"idade": 26, "corpo": "tall and slim with a long torso",
     "cabeca": "dark brown hair in a high crown braid",
     "marca": "smooth-skinned with a soft rounded jaw and a small stud in one "
              "nostril"},
    {"idade": 26, "corpo": "athletic and lean with defined shoulders",
     "cabeca": "light brown hair with blonde ends in a shoulder-length blunt "
               "cut",
     "marca": "smooth-skinned with a dimple in the left cheek"},
    {"idade": 26, "corpo": "petite and shapely with a small frame",
     "cabeca": "black hair in a sharp blunt fringe, straight to the waist",
     "marca": "wide-set brows and a beauty mark above the lip"},
    {"idade": 27, "corpo": "tall and long-limbed with a sculpted waist",
     "cabeca": "strawberry-blonde hair in a loose fishtail braid",
     "marca": "a light spray of freckles and a level brow line"},
    {"idade": 27, "corpo": "slim and toned with a dancer's carriage",
     "cabeca": "dark auburn hair in a sleek low bun",
     "marca": "high cheekbones and a small mole beside the mouth"},
    {"idade": 27, "corpo": "shapely with a full figure and a long waist",
     "cabeca": "honey-brown hair in heavy waves",
     "marca": "a wide mouth and a dimple in one cheek"},
    {"idade": 27, "corpo": "lean and strong with square shoulders",
     "cabeca": "tight dark curls cropped close at the sides and full on top",
     "marca": "a sharp jaw and a row of small gold hoops in one ear"},
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

    # ⭐ AMPLIACAO 2026-08-13 — *"aumente o pool de opcoes substancialmente"*.
    # 16 -> 34 silhuetas. ⛔ O EIXO E' O CORTE, NAO A COR: a cor ja' e' um pool
    # separado (CORES_BELAS), entao acrescentar `%s` em vinte variacoes da mesma
    # peca so' multiplicaria uniforme. Cada entrada abaixo muda a CONSTRUCAO —
    # bandeau, bodysuit, romper, mesh por cima, camisa amarrada, macaquinho.
    # ⛔ E CONTINUA SEM: `neckline` (contem `neck`, e o EX7 do DUPLA vigia
    # `neck` ao lado do molusco), `low-rise` (contem `rise`, vocabulario de
    # CRESCIMENTO do BO2), `thigh`/`lap` (tokens banidos da cena do COLO),
    # `dungarees`/`overall` (a BO9 do BOTICA 16 reprova macacao aqui dentro) e
    # roupa de banho (*"sem extremo de biquini"*, operador 2026-08-05).
    ("%s bandeau top under an open cropped shirt, with a very short skirt",
     "bandeau and shirt"),
    ("%s scoop-front bodysuit worn with a very short denim skirt",
     "scoop bodysuit"),
    ("%s cropped halter with a tie front and short pleated shorts",
     "tie-front halter"),
    ("%s square-front crop top with a short button-through skirt",
     "square-front crop"),
    ("%s sleeveless mock polo cropped at the waist, with a tennis skirt",
     "cropped polo"),
    ("%s tube top under a small open denim jacket, with a mini skirt",
     "tube top and jacket"),
    ("%s deep V-front camisole with very short shorts", "V-front camisole"),
    ("%s cropped mesh long-sleeve over a fitted crop top, with a mini skirt",
     "mesh crop"),
    ("%s asymmetric one-shoulder mini dress", "one-shoulder dress"),
    ("%s ruched bodycon mini dress with thin straps", "ruched mini dress"),
    ("%s cropped hoodie cut short above the waist, with running shorts",
     "cropped hoodie"),
    ("%s wrap top tied at the side, with a very short flared skirt",
     "side-tied wrap top"),
    ("%s linen shirt knotted at the waist over a crop top, with cut-off shorts",
     "knotted linen shirt"),
    ("%s strappy cami with a lace hem and a very short skirt", "strappy cami"),
    ("%s racer-front tank cropped high, with tight short shorts",
     "racer tank"),
    ("%s velvet mini dress with long sleeves and a very short hem",
     "velvet mini dress"),
    ("%s button-front crop shirt left open at the top, with a denim mini skirt",
     "open crop shirt"),
    ("%s halter romper with a very short hem and an open back",
     "halter romper"),
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

    # ⭐ AMPLIACAO 2026-08-13 — *"aumente o pool de opcoes substancialmente"*.
    # 14 -> 30. ⛔ MESMA REGRA DA PRIMEIRA LEVA: cor e LUZ, nunca acessorio —
    # `contact lenses` o gerador entrega como objeto e o artificio mata o
    # "mulher de verdade na cozinha". Por isso a palavra `lenses` nao aparece
    # aqui (ela ainda casaria com o eixo OCULOS do medir_personagens, e a Lei
    # do REF e' zero oculos).
    "clear sea-green eyes",
    "pale aquamarine eyes",
    "dark honey-gold eyes",
    "storm-grey eyes",
    "deep sapphire-blue eyes",
    "bright copper-brown eyes",
    "violet-grey eyes with a dark rim",
    "clear jade-green eyes",
    "silvery grey eyes that catch the light",
    "light moss-green eyes",
    "warm topaz eyes",
    "dark eyes with a bright amber ring",
    "pale lilac-blue eyes",
    "vivid bottle-green eyes",
    "burnished bronze eyes",
    "one pale green eye and one warm brown eye",
]

# ⭐ AMPLIACAO 2026-08-13 — 12 -> 26 cores. ⛔ A PALETA CONTINUA AMERICANA DE
# RUA: nada de ochre, terracotta, sand, sage, rust ou burnt orange, que o
# gerador le como traje etnico (*"norte americano costuma usar roupa de
# tribo?"*, operador). E nada de `nude`, que num pool de roupa curta o gerador
# resolve tirando a roupa.
CORES_BELAS = ["black", "white", "scarlet", "cobalt", "hot pink", "emerald",
               "burgundy", "silver", "cream", "dusty rose", "gold",
               "denim blue",
               "navy", "royal blue", "lavender", "mint green", "cherry red",
               "charcoal", "ivory", "blush pink", "electric blue", "plum",
               "teal", "coral", "champagne", "wine red"]

# ⛔ A CLAUSULA DE ROSTO NO REGISTRO BELA. Sem ela o gerador recebe "linda" no
# corpo e `ordinary relatable face` no rosto NA MESMA FRASE — o CLEAN pagou essa
# contradicao em 2026-08-04 (CL26) e resolveu do mesmo jeito: aqui so' sai o
# "comum", e o que fica e' a descricao positiva.
# ⛔ A negacao anti-celebridade saiu daqui em 2026-08-14, por ordem do operador
# (*"tire not a celebrity do prompt"*): declaracao INJETA o token que ela nega.
# ⚠️ Esta constante e' lida por 13 motores dentro do `montar()`, pelo ramo
# `spec.get("bela")` — limpar aqui conserta o ramo LIGADO dos 13 de uma vez, e
# o ramo desligado saiu no `ANTICELEB` local de cada um.
# Ver CLAUDE.md §"CONTRA A CELEBRIDADE, SILENCIO".
ANTICELEB_BELA = ("A strikingly beautiful face.")



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

def ref_bela(molde, rng, idade_min=None, banidos=(), idade_max=None):
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
    # ⭐ O TETO, simetrico ao piso — 2026-08-10, pedido do operador no BOTICA 16:
    # *"a narradora sempre deve ser uma mulher jovem de 20 a 25 anos"*. O piso
    # ja' existia (TROCA/RESSURREICAO precisam de 28+); sem o teto, o mesmo pool
    # entregava 33 anos num motor que pediu 25.
    # ⚠️ CEDE do mesmo jeito que o piso, e pelo mesmo motivo: pool vazio derruba
    # o sorteio, e derrubar o sorteio por causa de um filtro e' o botao que
    # quebra o app em vez do que muda a REF.
    if idade_max:
        _pool = [r for r in _pool if r["idade"] <= idade_max] or [
            min(_pool, key=lambda r: r["idade"])]
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

# ---------------------------------------------------------------------------
# ⭐⭐ REFS_FORTES_MADUROS — O TIOZAO FORTE (2026-08-12)
# ---------------------------------------------------------------------------
# ⛔ Ordem do operador, lendo o painel do GOOD 16: *"eu vi aqui no good 16, que
# quando seta a referencia forte a idade do homem cai pra 30 e poucos. e' isso
# mesmo? n quis manter os tiozao forte?"* — e depois, para o agente novo:
# *"modo forte deve abarcar refs homens mais velhos tb"*.
#
# ⚠️ ELE ESTAVA CERTO, E ISSO FOI MEDIDO ANTES DE UMA LINHA SER ESCRITA: o
# `REFS_FORTES` inteiro tem 16 entradas de 26 a 38 anos. Nao havia UM homem
# acima de 38 no pool do parque. Ligar o MODO FORTE num motor cujo narrador tem
# 58 anos nao trocava o CORPO dele — trocava o HOMEM por um de 32. Nunca foi
# decisao de ninguem: era a unica opcao que o pool tinha.
#
# ⛔⛔ POOL SEPARADO, E OPT-IN PELO PARAMETRO `maduros` — nao acrescentado ao
# `REFS_FORTES`. Motor que hoje chama `ref_forte` sem faixa maxima passaria a
# receber um homem de 66 anos sem ninguem pedir, e ha' motores em que o corpo
# jovem E' o argumento. Aditivo: quem nao pede, nao recebe, e nenhum dos outros
# motores muda de comportamento.
#
# ⭐ A REGRA DO POOL: FORTE **E** VELHO, nunca "velho que ja' foi forte". O
# corpo tem de ler como treino ativo (peito, ombro, antebraco) num homem que a
# cabeca e o rosto declaram ter 50, 60, 68 anos.
# ⛔ E vale a doutrina de 2026-08-12 do PLACA 16: **DISTINTIVO, NUNCA
# DETERIORADO**. Nenhuma entrada traz cicatriz, nariz quebrado, dente lascado
# ou `weathered` — num homem de 60, dano renderiza como mendigo, nao como
# marca. As ancoras sao saudaveis: covinha, queixo fendido, mecha prateada,
# argola, sinal de nascenca, linhas de riso.
# ⛔ E nenhuma palavra de aprovacao (`handsome`, `chiseled`, `strong jaw`):
# elogio no prompt puxa o rosto para a media do banco de imagem, que e' o mesmo
# mecanismo pelo qual `not a celebrity` invoca a celebridade.
# ⚠️ NENHUMA descreve OLHOS: o `ref_forte` PREPENDA os olhos (`OLHOS_FORTES`) e
# roda `_sem_olhos` em cima da `marca`. Olho escrito aqui seria apagado adiante
# — eixo que o autor pensa ter escrito e o codigo remove em silencio.
REFS_FORTES_MADUROS = [
    {"idade": 48, "corpo": "the heavy trained build of an athlete, thick deltoids "
                           "and a broad deep chest, forearms corded with standing "
                           "veins, stomach flat",
     "cabeca": "dark hair going grey at the temples, cut short",
     "marca": "a deep cleft in the chin, clean-shaven"},
    {"idade": 50, "corpo": "the dense trained frame of a lifter, deep chest and "
                           "thick round shoulders, arms heavy and veined to the "
                           "wrist, waist trim",
     "cabeca": "a close-shaved scalp and a short salt-and-pepper beard",
     "marca": "laugh lines and a smooth even complexion"},
    {"idade": 52, "corpo": "a powerful athletic frame, wide square shoulders and "
                           "heavy muscled arms, thick veins running down each "
                           "forearm, stomach flat",
     "cabeca": "silver hair cut in a short crisp fade",
     "marca": "a dimple that shows in one cheek"},
    {"idade": 54, "corpo": "the built frame of a man who still trains hard, deep "
                           "chest and thick arms, forearms roped with veins, waist "
                           "trim",
     "cabeca": "grey hair worn short and pushed back, clean-shaven",
     "marca": "a silver streak running through one eyebrow"},
    {"idade": 55, "corpo": "a muscular athlete's build, thick neck and heavy "
                           "traps, wide shoulders, veins raised along both "
                           "forearms, stomach flat",
     "cabeca": "close-cropped white hair and a trimmed white beard",
     "marca": "a plain gold hoop in one ear"},
    {"idade": 57, "corpo": "the hard trained build of a lifter, real mass across "
                           "the chest and shoulders, arms cut and veined, waist "
                           "narrow",
     "cabeca": "a bald crown with grey at the sides and a full grey moustache",
     "marca": "a beauty mark high on one cheekbone"},
    {"idade": 58, "corpo": "a powerful athletic build, thick sloping shoulders and "
                           "heavy wrists, forearms corded with veins, stomach flat",
     "cabeca": "silver hair combed back from a high forehead",
     "marca": "a shallow cleft chin and smooth skin"},
    {"idade": 60, "corpo": "the heavy muscled frame of an athlete, broad deep "
                           "chest and thick arms, veins standing along the "
                           "forearms, waist trim",
     "cabeca": "short grey curls and a close-trimmed beard",
     "marca": "deep laugh lines at the corners of his mouth"},
    {"idade": 62, "corpo": "a powerfully muscled athlete's build, chest and upper "
                           "arms thick with muscle, forearms corded and veined, "
                           "stomach flat",
     "cabeca": "a cleanly shaved head and a short white goatee",
     "marca": "a straight narrow nose and smooth skin"},
    {"idade": 64, "corpo": "the dense trained frame of a lifter, still heavily "
                           "muscled through the shoulders and forearms, veins "
                           "raised, waist narrow",
     "cabeca": "thick white hair cut neatly above the collar, clean-shaven",
     "marca": "a dimple beside his mouth"},
    {"idade": 66, "corpo": "a muscular athletic build, muscle standing out across "
                           "the chest and shoulders, thick veined wrists and "
                           "forearms, stomach flat",
     "cabeca": "silver hair cropped very short and a full white beard kept "
               "neatly shaped",
     "marca": "a small pale birthmark near one temple"},
    {"idade": 68, "corpo": "the heavy trained build of an athlete, deep chest and "
                           "thick cut arms, forearms roped with veins, waist trim",
     "cabeca": "a bald head and a neat white moustache",
     "marca": "a cleft chin and heavy level brows"},
    # ⭐⭐ +6 ENTRADAS ACIMA DE 60 — 2026-08-12, poucas horas depois do pool
    # nascer. Ordem do operador para o GOOD 16: *"sempre que travar a
    # referencia de forte mantenha o homem acima de 60 anos no prompt"*.
    # ⚠️ O pool tinha 12 entradas de 48 a 68 e SO' QUATRO acima de 60. Um motor
    # que pede piso 61 ficava com quatro rostos — e quatro rostos num lote de
    # trinta videos e' o mesmo homem repetido. A lente do proprio GOOD 16 e'
    # que acusou (`so' 4 idade(s) distinta(s) acima de 60`).
    # ⛔ Mesmas regras das doze de cima, sem excecao: FORTE **E** VELHO,
    # DISTINTIVO E NUNCA DETERIORADO (nada de cicatriz, nariz quebrado, dente
    # lascado ou `weathered`), e ZERO palavra de aprovacao.
    # ⭐ ADITIVO: quem chama `ref_forte` sem `maduros=True` continua sem ver
    # nenhuma delas — conferido por medicao, nao por leitura.
    {"idade": 61, "corpo": "a powerful athlete's frame, broad muscled chest and "
                           "shoulders, forearms thick and veined, waist still flat",
     "cabeca": "thick steel-grey hair combed back, cut short at the sides",
     "marca": "a birthmark below the left ear and an even complexion"},
    {"idade": 63, "corpo": "the hard built frame of a lifter, heavily muscled "
                           "across the back and arms, chest square and hard, "
                           "stomach flat",
     "cabeca": "a clean-shaved head and a close white beard",
     "marca": "a deep cleft chin and clear skin"},
    {"idade": 65, "corpo": "a densely muscled athletic build, shoulders full, "
                           "forearms corded, upright posture and a trim waist",
     "cabeca": "short white hair with a silver streak swept off the forehead",
     "marca": "laugh lines at the corners of both eyes"},
    {"idade": 67, "corpo": "the heavy trained frame of a lifter, thick muscle "
                           "through the neck and upper arms, chest full and hard, "
                           "waist narrow",
     "cabeca": "close-cropped grey hair and a trimmed grey moustache",
     "marca": "a small gold hoop in the left ear"},
    {"idade": 70, "corpo": "a muscular athlete's build, hard chest and thick "
                           "veined forearms, square shoulders, stomach flat",
     "cabeca": "full silver hair worn a little long and a short silver beard",
     "marca": "a dimple in one cheek and a smooth even complexion"},
    {"idade": 72, "corpo": "the trained frame of a lifelong athlete, lean and hard "
                           "through the chest, arms still thick with muscle, "
                           "stomach flat",
     "cabeca": "white hair in a flat crop and a clipped white beard",
     "marca": "wide-set eyes and a raised mole on the right cheekbone"},
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
# diz "powerfully built" e o rosto diz "ordinary relatable face", o gerador
# recebe as duas na mesma frase e resolve contra nos.
# ⛔ A negacao anti-celebridade saiu daqui em 2026-08-14, por ordem do operador
# (*"tire not a celebrity do prompt"*): declaracao INJETA o token que ela nega.
# ⚠️ Lida por 3 motores (GOOD 16, MEL 16, PRATO 16) pelo ramo
# `spec.get("forte")`. Ver CLAUDE.md §"CONTRA A CELEBRIDADE, SILENCIO".
ANTICELEB_FORTE = ("A rugged good-looking face.")


def ref_forte(molde, rng, idade_min=None, idade_max=None, maduros=False):
    """Uma REF masculina do MODO FORTE no FORMATO DO MOTOR que pediu.

    Espelho exato do `ref_bela` — ver a docstring de la' para o porque de nao
    devolver o dicionario cru.

    ⛔ A FAIXA E' DO MOTOR. O ESCANDALO tem `TETO_DIF_IDADE = 30` entre narradora
    e corpo-prova, e uma faixa propria para o figurante; o RESSURREICAO tem a
    mesma. Um pool compartilhado que ignore isso reprova a producao do motor —
    medido em 200 sorteios antes deste parametro existir.
    ⚠️ Quando NENHUMA entrada cabe na faixa, ela CEDE e a mais proxima entra:
    derrubar o sorteio por causa de um toggle seria o botao que quebra o app.

    maduros — soma o `REFS_FORTES_MADUROS` (48-68 anos) ao pool. ⛔ OPT-IN, e a
    razao esta' no cabecalho daquele pool: sem ele, ligar o MODO FORTE num motor
    de narrador de 58 anos trocava o HOMEM por um de 32 em vez de trocar o CORPO
    dele. Motor que nao pede continua recebendo so' o pool 26-38 — e por isso
    nenhum dos outros muda de comportamento.
    """
    _pool = REFS_FORTES + REFS_FORTES_MADUROS if maduros else REFS_FORTES
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


# ---------------------------------------------------------------------------
# ⭐⭐ A HIERARQUIA DO MECANISMO — diretriz do operador, 2026-08-06
# ---------------------------------------------------------------------------
# *"Registre essa diretriz pra todo take 2 que haja recipe prep com a cena."*
#
# ⛔ O DEFEITO: numa cena 2 que MOSTRA o preparo, a fala enumera ingredientes —
# e o `gelatin trick` entrava no fim da enumeracao, com o mesmo peso do alho:
#
#     "...garlic, and ginkgo, the leaf off that ancient Chinese tree.
#      Then boil it ten minutes, and one gelatin trick."
#
# O espectador ouve uma lista de compras com sete itens. O `gelatin trick` e' o
# CENTRO DE GRAVIDADE do funil — e' o que a VSL vende e a palavra que o CTA pede
# — e estava coadjuvante.
#
# ⭐ A FORMA QUE O OPERADOR ESCREVEU A MAO:
#
#     "...and ginkgo, the leaf off that ancient Chinese tree
#      and... THE SECRET: the gelatin trick."
#
# Sao TRES partes, e nenhuma e' opcional:
#   1. a CONJUNCAO que separa da lista (`and`, `plus`, `then`);
#   2. o ROTULO que anuncia hierarquia, seguido de DOIS PONTOS — `the secret:`,
#      `the one thing nobody sells:`, `the part I hold back:`;
#   3. o LITERAL `gelatin trick`, intocavel.
# Sem o rotulo, o trick volta a ser alho. E' o rotulo que diz ao espectador que
# o que vem depois nao e' ingrediente: e' o mecanismo.
#
# ⚠️ ONDE APLICA: cena 2 que tem PREPARO EM QUADRO (bancada, panela, copo,
# liquidificador). Onde a cena 2 nao mostra preparo, a fala nao esta' enumerando
# e nao ha' lista da qual se destacar.
#
# ⛔ E DE ONDE SAI O ESPACO: da RECEITA, sempre. O quadro JA' MOSTRA os
# ingredientes; o que o quadro nao mostra — e por isso so' a fala carrega — e' o
# segredo. O operador foi explicito: *"retire um ingrediente da elencacao entao,
# melhor fazer assim e manter a hierarquia"*.
# ⚠️ Foi esse o meu erro de projeto: com o teto de 25 apertando, eu encurtei o
# SEGREDO de 8 para 4 palavras. Fiz o beat errado ceder — encolhi justamente o
# unico que nao podia encolher.
ROTULOS_HIERARQUIA = (
    "secret", "one thing", "part i hold", "part nobody", "step nobody",
    "piece nobody", "last thing", "one step", "thing more", "part that does",
    "quiet one", "one i never", "what nobody",
    # ⚠️ acrescentados ao medir: a lista incompleta reprovava rotulo VALIDO
    # (`and one more thing: the gelatin trick`) — lente cuja tabela nao
    # acompanha o repertorio vira falso positivo silencioso.
    "more thing", "one secret", "the real", "hold back", "keep back",
    "never post", "grandmother", "nobody sells", "nobody tells",
    "nobody posts", "part that", "last thing", "one step",
)


def lint_hierarquia_mecanismo(spec, blocos, achados, cena=2, rotulo="HIER"):
    """Cobra que o `gelatin trick` da cena com PREPARO venha anunciado.

    ⛔ So' roda quando a IMAGE daquela cena mostra preparo — bancada, panela,
    copo, liquidificador. Sem preparo em quadro nao ha' enumeracao, e sem
    enumeracao nao ha' do que se destacar.
    ⚠️ A lente e' de FORMA (dois pontos depois de um rotulo), nao de semantica:
    ela nao tenta julgar se o rotulo e' bom. Lente que tenta julgar gosto vira
    ruido; esta so' garante que a hierarquia EXISTE.
    """
    fala = (spec.get("falas") or [""] * 3)[cena - 1] or ""
    if "gelatin trick" not in fala.lower():
        return
    # ⛔⛔ O GATILHO E' A ENUMERACAO, NAO A BANCADA. A primeira versao usava
    # "a IMAGE mostra preparo" como proxy de "a fala esta' enumerando", e errou
    # em cinco motores: no CLEAN a fala e' *"But nothing works without the
    # gelatin trick"* e no COLO e' *"That's the gelatin trick, and your {o}..."*
    # — nos dois o trick ABRE a oracao, que e' hierarquia maxima. Nao havia
    # lista da qual se destacar, e a lente reprovava 150 de 150.
    # ⚠️ Terceira vez hoje que uma lente minha reprova por proxy errado. Falso
    # positivo e' pior que lente nenhuma: o operador aprende a ignorar.
    # ⭐ O teste certo: ANTES do literal ha' uma ENUMERACAO de ingredientes —
    # duas virgulas ou mais, ou dois ingredientes nomeados. So' entao o trick
    # corre o risco de virar item N.
    antes = fala.lower().split("gelatin trick")[0]
    # ⛔⛔ SO' CONTA A SENTENCA EM QUE O TRICK ESTA'. Se ele abre a propria
    # oracao — `... first thing. Plus the gelatin trick.` — ele JA' esta'
    # destacado: a hierarquia veio do ponto final, nao precisa de rotulo.
    # ⚠️ Isso reprovava CLEAN, COLO e PLACA, e nos tres a construcao estava
    # certa: `But without the gelatin trick they do nothing` (contraste),
    # `That's the gelatin trick, and...` (abre a sentenca). Quarta vez hoje que
    # uma lente minha reprova por proxy errado — e a terceira em que o conserto
    # e' OLHAR MENOS TEXTO, nao mais.
    _sent = antes
    for corte in (". ", "! ", "? "):
        if corte in _sent:
            _sent = _sent.rsplit(corte, 1)[1]
    _ingr = ("lemon", "ginger", "garlic", "honey", "beet", "pomegranate",
             "carrot", "juice", "powder", "water", "clove", "spoon", "milk",
             "watermelon", "fenugreek")
    enumera = (_sent.count(",") >= 2
               or sum(1 for w in _ingr if w in _sent) >= 2)
    if not enumera:
        return
    antes = _sent
    # ⛔⛔ O QUE MARCA A HIERARQUIA E' O SEPARADOR, NAO A PALAVRA. A versao
    # anterior exigia um rotulo de uma LISTA FECHADA, e reprovava rotulos
    # perfeitamente validos que eu nao tinha previsto — `a step I keep:`, `a
    # secret —`, `something I do not show:`. Lista fechada de linguagem natural
    # nunca fecha: sempre falta a proxima forma.
    # ⭐ O teste robusto: entre a enumeracao e o literal ha' DOIS PONTOS ou
    # TRAVESSAO. E' o sinal tipografico da revelacao, e ele independe de qual
    # substantivo o redator escolheu. Quinta correcao desta lente hoje, e a
    # unica que nao depende de eu adivinhar vocabulario.
    if re.search(r"[:—–]\s*(the\s+)?$", antes[-40:]):
        return
    achados.append((
        "ERRO",
        "%s: o `gelatin trick` da cena %d entra como item da lista, sem "
        "hierarquia. Numa cena que MOSTRA o preparo a fala enumera, e o "
        "mecanismo fica com o peso do alho. Falta o rotulo com dois pontos "
        "antes dele (`and the secret: the gelatin trick`) — diretriz do "
        "operador, 2026-08-06. %r" % (rotulo, cena, fala[-70:])))
