#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE LIVRO 5 — 5 takes de 8s (40s), destino AdBatch **Vertical 5**.

⭐⭐ O DEPOIMENTO DE TRANSFORMACAO. Uma pessoa conta em primeira pessoa como
saiu do fundo do poco com um livro de receitas de 10 dolares. Nao ha' CTA
falado, nao ha' pedido: o video inteiro E' a prova.

⛔ LEITURA OTICA FEITA, cinco videos baixados e transcritos (2026-09-02):
`lucas_045` `lucas_052` `lucas_053` `lucas_057` `lucas_100`. Sao do Lucas,
gerados no Veo e montados no Veo Editor CTA FIXO; o operador confirmou que
modelar em cima deles esta' combinado com ele.

⭐⭐ O ESQUELETO E' RIGIDO — NOVE BATIDAS, EM CINCO DE CINCO:
   1 quem ela e', em uma frase
   2 a HUMILHACAO FISICA concreta
   3 o numero do fundo do poco
   4 quem trouxe o livro
   5 o preco, dito para ser desprezado
   6 o resultado DESTA SEMANA
   7 o mecanismo em lista de tres
   8 o numero grande + o tamanho da roupa
   9 o fechamento na MESMA IMAGEM da batida 2, invertida

⛔⛔ A BATIDA 9 E' A ESPINHA, E POR ISSO 2 E 9 NASCEM DO MESMO POOL.
`couldn't tie my shoes without sitting down` fecha em `tied my shoes standing
up`. `my grandchildren got tired of carrying me` fecha em `they don't carry me
anymore, I walk with them`. `couldn't chase them at the park` fecha em `I
chased all three and I wasn't the one who got tired first`.
Separar as duas em pools independentes quebraria o video em 100% dos sorteios
— o sorteio cruzaria a humilhacao de um com o desfecho de outro. Elas sao UM
campo com duas metades, e a lente `LV1` cobra que as duas venham do mesmo par.

⭐⭐ O TAKE 1 E' MUDO, E ISSO E' MEDIDO: os cinco videos abrem sem uma palavra
por 6,6 · 6,6 · 7,4 · 7,2 · 8,1 segundos. E' a pessoa GORDA na cozinha, com o
rotulo `MONTH 1` queimado, bebendo. A fala so' comeca depois do corte para a
pessoa magra. O silencio da' tempo de o espectador registrar o ANTES.

⛔ O TETO DE FALA E' 22 PALAVRAS por take, e tambem e' medido: 654 palavras em
232 segundos nos cinco videos = **2,82 palavras por segundo**. Nao e' chute.

⚠️ E O ANTES E O DEPOIS SAO DUAS PESSOAS DIFERENTES, assumidamente. Nenhum dos
cinco tenta ancora de rosto: o corpo muda por completo, o cenario muda por
completo, e o que amarra e' etnia + faixa etaria + cabelo. Quem faz o trabalho
de dizer "passou tempo" e' o rotulo `MONTH 1`, nao a continuidade. E' o oposto
da decisao do RUTH 16, e esta' registrado como escolha da fonte, nao como
descuido nosso.

⛔ O ROTULO `MONTH 1` E' QUEIMADO NO EDITOR, nao pedido ao gerador. E ⚠️ o lote
da fonte saiu com `MOUNTH 1` em varios videos — erro de digitacao num campo de
config, replicado em N pecas. A lente `LV7` bane a grafia errada do motor.
"""

import argparse
import io
import json
import os
import random
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

AQUI = os.path.dirname(os.path.abspath(__file__))

# ⛔ Ledger proprio: nenhum outro motor gasta o historico deste.
LEDGER = os.path.join(AQUI, ".livro-5-ledger.json")

TITULO = "AGENTE LIVRO 5"
SLUG = "livro-5"
SUBTITULO = ("5 takes de 8s = 40 segundos · o antes mudo, e o depoimento "
             "que fecha na mesma imagem em que abriu")

CENAS_UI = ["1 · O ANTES (mudo)", "2 · QUEM SOU + A HUMILHACAO",
            "3 · O FUNDO + O LIVRO", "4 · A PRIMEIRA SEMANA",
            "5 · O NUMERO + A VIRADA"]

ORIENTACAO = "Vertical 9:16 portrait orientation."
CAUDA = "iPhone shot, natural grain, no text, no watermark."

# ⛔ NUCLEO VAZIO, como no RUTH 16. Este angulo nao tem orgao para apelidar, e
# por isso o CT4/CT4b do contrato de 16s nao se aplicam por CONSTRUCAO — nao
# por excecao declarada. Excecao que nao suprime nada e' ruido.
NUCLEO = ()

# ⭐ Quem narra. Um sexo so' -> a UI nao desenha a trava homem/mulher, e botao
# que nao trava nada e' pior que botao nenhum.
SEXOS = ("mulher",)

# ⭐ TETO FISICO — ver a docstring. O numero que manda e' o de SILABAS.
# ⛔ MEDIDO nos cinco videos da fonte: 654 palavras em 232s = 2,82
# palavras/s. Em 8s cabem 22. ⚠️ Aqui a unidade e' a PALAVRA e nao a
# silaba: o teto em silabas nasceu no ATEM porque ALEMAO tem 1,7
# silabas por palavra e a contagem de palavra mentia. Em ingles as duas
# medidas andam juntas, entao a palavra basta.
TETO_PALAVRAS_TAKE = 22
TETO_SILABAS = 99
# ⚠️ 24, nao 20. A rede de palavras acusava falas de 21-22 palavras que o
# teto de SILABAS aprovava com folga (31 de 35) — e gate que acusa copy
# certa treina o operador a ignorar o gate. Ela existe so' para o caso
# patologico (muita monossilaba), nao para medir fala: quem mede e' a
# silaba.
TETO_PALAVRAS = 24
# ⚠️ Uma chave por cena — o `ui_agente` le' `TETO_FALA[i+1]` para desenhar o
# contador de cada caixa. Com tres chaves (as herdadas do GELO 16) a janela
# morria em KeyError na quarta.
# ⛔ A cena 1 tem teto ZERO porque ela e' MUDA — o contador mostrando "0/0"
# e' a forma de o painel dizer isso sem uma palavra de explicacao.
TETO_FALA = {1: 0, 2: TETO_PALAVRAS_TAKE, 3: TETO_PALAVRAS_TAKE,
             4: TETO_PALAVRAS_TAKE, 5: TETO_PALAVRAS_TAKE}

# ⛔⛔ A KEYWORD DO CTA. Nasce em `ATEM` — alema, curta, digitavel por qualquer
# um, e diz o produto. ⚠️ Ela TEM de estar cadastrada na automacao de DM antes
# do primeiro lote: comentario que entra sem keyword cadastrada e' mensagem que
# nao sai, que e' o preco ja' pago por `book`, `yes` e `horse` neste repo.
# ⭐ Editavel no campo de keyword da UI do Veo Editor, mesma mecanica do
# `gelahorse16`.
# ⛔ ESTE ANGULO NAO TEM CTA FALADO. Nenhum dos cinco videos da fonte
# pede nada — o video inteiro e' prova. A keyword existe so' para o
# painel nao quebrar; ela nunca entra na fala, e a lente `LV6` garante.
KEYWORD = "RECIPE"

# ⭐ A ETNIA continua sendo o eixo de congruencia do repo (etnia do REF = etnia
# do avatar da pagina), so' que o mercado agora e' de lingua alema.
# ⏳ DIVIDA DECLARADA: o operador ainda nao passou as paginas deste funil. As
# chaves abaixo sao PROVISORIAS e existem para a UI ter o que desenhar — trocar
# pelos nomes reais quando as paginas nascerem.
# ⛔⛔ AMERICANA, e isso e' conserto de um defeito que so' apareceu LENDO O
# VIDEO: o `ETNIA` veio por copia do GELO 16, que e' alemao, e o motor gerava
# `white German man` falando ingles sobre LIBRAS e TAMANHO 20. O autoteste
# cravava 0 ERRO — nenhuma lente conhece geografia.
# ⭐ As cinco paginas sao as do funil de emagrecimento que ja' esta' no ar
# (mesmo conjunto do RUTH 16), split 3 claras / 2 escuras.
ETNIA = {
    "joe": "white American", "ray": "white American", "matt": "white American",
    "marcus": "Black American", "chuck": "Black American",
}


# ===========================================================================
# STRINGS TRAVADAS — a gramatica de cena. NAO REESCREVER, NAO COMPRIMIR.
# ===========================================================================

# ⛔⛔ O ROTULO DO ANTES. Queimado no Veo Editor, NUNCA pedido ao gerador —
# gerador escreve texto errado, e a fonte prova: o lote do Lucas saiu com
# `MOUNTH 1` em varias pecas, erro de digitacao num campo de config replicado
# em N videos. A lente `LV7` bane a grafia errada deste motor.
# ⚠️ A string existe aqui para DOCUMENTAR o que o operador digita no painel,
# e nao entra em prompt nenhum.
ROTULO_ANTES = "MONTH 1"

# ⛔⛔ O TAKE 1 E' MUDO. Medido nos cinco videos: 6,6 · 6,6 · 7,4 · 7,2 · 8,1
# segundos sem uma palavra. E' o que da' tempo de o espectador registrar o
# ANTES antes de a voz existir.
SILENCIO = ("Audio: quiet room tone only. Nobody speaks, there is no voice "
            "and no music.")

# ⭐ O GESTO DO ANTES: sempre com o copo na mao, sempre olhando para baixo,
# sempre parada. Nos cinco videos a pessoa gorda nunca fala, nunca sorri e
# nunca olha para a lente.
POSE_ANTES = (
    "standing still and facing the camera, holding a tall glass of %s at "
    "chest height in one hand, her eyes lowered toward the glass, her mouth "
    "closed, her free arm hanging at her side"
)

# ⛔ O DEPOIS FALA PARA A LENTE, de pe, corpo inteiro em quadro. Nos cinco a
# pessoa magra esta' sempre de pe numa sala clara, nunca sentada.
POSE_DEPOIS = (
    "standing upright in the middle of the frame facing the camera, framed "
    "from the knees up, both arms relaxed and moving a little as she talks, "
    "her mouth open mid-word, looking straight into the lens"
)

CAUDA_LV = ("Shot on a tripod at chest height, natural indoor light, slight "
            "sensor grain, no text and no watermark.")

# ===========================================================================
# POOLS DE CENA
# ===========================================================================

# ⭐⭐ O PAR HUMILHACAO/VIRADA — O POOL MAIS IMPORTANTE DO MOTOR.
# ⛔ As batidas 2 e 9 sao A MESMA IMAGEM, invertida, e por isso moram no MESMO
# registro. Separa-las em dois pools faria o sorteio cruzar a humilhacao de
# uma pessoa com o desfecho de outra, e o video quebraria em 100% dos casos.
# ⚠️ Todas as quatro primeiras entradas sao VERBATIM da fonte; as outras
# seguem o molde. Cada uma carrega tambem QUEM a pessoa e' (batida 1), porque
# a humilhacao so' faz sentido dentro da vida dela.
VIDAS = [
    {"id": "sapato", "idade": 58, "sexo": "mulher",
     "quem": "Seven months ago",
     "dor": "I couldn't tie my own shoes without sitting down",
     "virada": "last week I tied my shoes standing up without thinking "
               "about it",
     "rotulo": "58a · o sapato"},
    {"id": "parque", "idade": 38, "sexo": "mulher",
     "quem": "I have three kids under 10",
     "dor": "I couldn't chase them at the park without stopping for breath",
     "virada": "Saturday I chased all three and I wasn't the one who got "
               "tired",
     "rotulo": "38a · o parque"},
    {"id": "carro", "idade": 70, "sexo": "mulher",
     "quem": "I'm 70 years old",
     "dor": "my own grandchildren got tired of carrying me to the car",
     "virada": "my grandchildren don't carry me anymore, I walk with them",
     "rotulo": "70a · o carro"},
    {"id": "terno", "idade": 63, "sexo": "homem",
     "quem": "My wife died two years ago",
     "dor": "I gained fifty pounds in a year and stopped recognizing myself",
     "virada": "the suit from our anniversary fits, and I wish she could see "
               "me",
     "rotulo": "63a · o terno"},
    {"id": "escada", "idade": 61, "sexo": "mulher",
     "quem": "I live on the second floor",
     "dor": "I had to stop halfway up my own stairs and hold the rail",
     "virada": "I carry the groceries up in one trip without the rail",
     "rotulo": "61a · a escada"},
    {"id": "cinto", "idade": 55, "sexo": "homem",
     "quem": "I drive a truck for a living",
     "dor": "I needed a seatbelt extender on my son's wedding flight",
     "virada": "I flew out last month and the belt closed with room to "
               "spare",
     "rotulo": "55a · o cinto"},
    {"id": "chao", "idade": 44, "sexo": "mulher",
     "quem": "I'm a grandmother at 44",
     "dor": "I couldn't get down on the floor to play with the baby",
     "virada": "I sit on the floor with her and get back up on my own",
     "rotulo": "44a · o chao"},
    {"id": "espelho", "idade": 49, "sexo": "mulher",
     "quem": "I stopped going to family parties",
     "dor": "I hid in the back of every photo for six years",
     "virada": "I'm in the front of her wedding photo, and I asked to be "
               "there",
     "rotulo": "49a · a foto"},
]

# ⭐ A PORTA DE ENTRADA. Cada video entra por UMA e cita as outras de
# passagem — e' a batida 7, a lista de tres. Verbatim da fonte onde possivel.
PORTAS = [
    {"id": "suco", "liquido": "bright green vegetable juice",
     "primeira": "I picked one juice that first morning just to try",
     "lista": "the teas at night, the soups, the 30-minute dinners"},
    {"id": "sopa", "liquido": "clear broth soup in a mug",
     "primeira": "I made a pot of soup Sunday and ate it all week",
     "lista": "the juices in the morning, the teas, the 30-minute dinners"},
    {"id": "cha", "liquido": "dark herbal tea",
     "primeira": "I started with the teas, one before bed",
     "lista": "then the breakfasts, then the soups, then the dinners"},
    {"id": "vermelho", "liquido": "deep red beet juice",
     "primeira": "I made three of them the first day, just to check",
     "lista": "the teas at night, the soups, the 30-minute dinners"},
    {"id": "laranja", "liquido": "fresh orange juice",
     "primeira": "I made my first juice on a Monday morning",
     "lista": "the soups, the teas, the 30-minute dinners"},
]

# ⭐ QUEM TROUXE O LIVRO. Nunca a propria pessoa: sempre alguem de confianca,
# e sempre de graca ou quase. E' a barreira caindo por POSSE.
FONTES_LIVRO = [
    "My daughter sent me this recipe book",
    "Someone at church showed me this book on their phone",
    "I don't even remember who told me about this book",
    "My sister left it on my counter and said nothing",
    "A woman at work wrote the name on a napkin for me",
]

# ⭐⭐ O PRECO, DITO PARA SER DESPREZADO. Nunca vendido — sempre minimizado.
# `$10 and I figured I had nothing to lose but the money` e' o molde.
PRECOS = [
    "It was ten dollars. I almost didn't buy it",
    "Ten dollars. I had nothing to lose but the money",
    "It cost less than the shakes I'd been buying",
    "Ten dollars. I've wasted more on a bad lunch",
]

# ⭐⭐ O RESULTADO DESTA SEMANA — a batida 6, e a mais subestimada das nove.
# E' o unico numero que a espectadora consegue imaginar acontecendo COM ELA
# nesta semana, e por isso ele vale mais que o numero grande do fim.
PRIMEIRA_SEMANA = [
    "By Friday I had lost nine pounds",
    "By Friday I'd lost seven pounds",
    "Eleven pounds the first month, no workouts",
    "The first week the scale moved six pounds",
]

# ⭐ O NUMERO GRANDE + O TAMANHO DA ROUPA. Nos cinco videos os dois vem
# sempre juntos: peso perdido E numero de roupa. O peso e' o dado; a roupa e'
# o que ela consegue VER.
NUMEROS = [
    "Ninety pounds gone",
    "Seventy seven pounds, size twenty to eight",
    "Eighty four pounds, size twenty to six",
    "Sixty six pounds, and two prescriptions gone",
    "Sixty eight pounds",
]

# ⭐ A TESTEMUNHA que valida sem ser paga. Sempre alguem proximo, e sempre
# reagindo com espanto, nunca com elogio.
TESTEMUNHAS = [
    "My sister asked me if I'd had surgery",
    "My doctor looked at my blood work and asked what I was doing differently",
    "My kids ate the same food I did and nobody noticed it was a diet",
    "The woman at the pharmacy didn't recognise me",
    "My own brother walked past me at the store",
]

# ⭐ Os dois mundos. O ANTES e' sempre cozinha de madeira escura e apertada; o
# DEPOIS e' sempre sala clara e aberta. A luz faz metade do trabalho.
COZINHAS = [
    "a cramped kitchen with dark oak cabinets and a small window over the "
    "sink",
    "a narrow galley kitchen with wood cabinets and a dim overhead lamp",
    "an older kitchen with brown tile and a refrigerator covered in "
    "children's drawings",
    "a small kitchen corner with laminate counters and a cluttered "
    "countertop",
]
# ⛔⛔ O POOL DE SALAS MORREU EM 2026-09-02, e a lapide fica.
# Ele existia porque a FONTE troca de lugar entre o antes e o depois (medido:
# cozinha -> sala, cozinha -> playground, mesa -> varanda). O operador mandou o
# contrario, e com razao: no MESMO quadro o espectador nao precisa acreditar
# que sao a mesma pessoa, ele ve'. Trocar de lugar era o que ESCONDIA o salto.
# ⚠️ A lapide fica para ninguem "consertar" isto de volta lendo a fonte.


# ⭐ O corpo do ANTES. Descrito por FORMA e AREA DE QUADRO, nunca por
# adjetivo — a licao do RUTH 16: o gerador nao desenha adjetivo, desenha
# forma. Sem isto ele devolve uma pessoa comum.
# ⛔⛔ OS DOIS CORPOS SAO A UNICA COISA QUE MUDA ENTRE OS QUADROS 1 E 2.
# Cenario, enquadramento, roupa, pose, luz e copo sao identicos — e' o que
# transforma o par em COMPARACAO em vez de em duas fotos soltas.
# ⭐ A descricao e' por FORMA, AREA DE QUADRO e o que a ROUPA faz, nunca por
# adjetivo: o gerador nao desenha "gorda", desenha volume e tecido esticado.
# E' a licao do RUTH 16, onde adjetivo devolvia pessoa comum.
CORPO_ANTES = (
    "She is very heavy. Her body fills most of the width of the frame and her "
    "stomach stands out well past her chest, pushing the %s tight across the "
    "front so the fabric strains between the seams. Her upper arms fill the "
    "sleeves completely, and her chin and jaw are soft and rounded."
)
# ⚠️ A MESMA PECA, e e' ela que carrega a prova: esticada no primeiro quadro,
# sobrando no segundo. Ancora e prova no mesmo objeto — RUTH 16.
CORPO_DEPOIS = (
    "She is slim and stands straight. The same %s now hangs loose and empty "
    "on her, falling straight from her shoulders with room to spare at the "
    "waist. Her arms are thin inside the sleeves, her collarbones show at the "
    "neckline, and her jaw and cheekbones are clearly defined."
)

# ⭐ A PECA. Uma so' por video, e a mesma nos dois quadros.
ROUPAS = [
    {"id": "camiseta_cinza", "peca": "plain grey t-shirt",
     "baixo": "dark jeans"},
    {"id": "moletom_azul", "peca": "faded blue sweatshirt",
     "baixo": "black leggings"},
    {"id": "polo_bege", "peca": "beige knit polo shirt",
     "baixo": "dark trousers"},
    {"id": "camisa_xadrez", "peca": "green plaid button shirt",
     "baixo": "khaki trousers"},
    {"id": "blusa_bordo", "peca": "burgundy long sleeved top",
     "baixo": "black trousers"},
]

# ===========================================================================
# POOLS DE COPY — ALEMAO
# ===========================================================================


# ===========================================================================
# MEDIDA DE FALA — SILABAS
# ===========================================================================

_VOGAIS = "aeiouyäöü"
# ⭐ Ditongos alemaes contam UMA silaba. Sem esta lista `Deutschland` conta 3
# em vez de 2 e `heute` conta 3 em vez de 2, e o teto passa a reprovar copy
# que cabe. A ordem importa: os de duas letras sao testados antes das vogais
# soltas.
_DITONGOS = ("eu", "äu", "ei", "ai", "au", "ie")


def silabas(palavra):
    """Silabas de UMA palavra alema, por grupo vocalico com ditongos.

    ⚠️ E' aproximacao, e de proposito: contar silaba alema com exatidao pede
    dicionario, e dicionario nao cabe num .exe de agente. O erro desta funcao
    e' de +-1 por palavra longa e SEMPRE para cima nos compostos, que e' o
    lado seguro — ela superestima a fala e o teto reprova antes do render.
    """
    p = palavra.lower()
    p = re.sub(r"[^a-zäöüß]", "", p)
    if not p:
        return 0
    n, i = 0, 0
    while i < len(p):
        if p[i] in _VOGAIS:
            n += 1
            if p[i:i + 2] in _DITONGOS:
                i += 2
            else:
                i += 1
            while i < len(p) and p[i] in _VOGAIS:
                # vogais seguidas que nao formam ditongo listado contam junto
                # (`ee` em `Seele`, `aa` em `Saal`) — um nucleo, uma silaba.
                i += 1
        else:
            i += 1
    # `-e` final atono continua sendo silaba em alemao (`Blase` = 2), entao
    # nao ha' o desconto que o ingles faria.
    return max(1, n)


def silabas_frase(txt):
    return sum(silabas(w) for w in txt.split())


def palavras(txt):
    return len([w for w in txt.split() if re.search(r"[a-zA-ZäöüÄÖÜß]", w)])


# ⛔ O `ui_agente` chama `motor._palavras` (com underscore) para desenhar o
# contador de palavras de cada cena. Sem este alias a janela abre e o contador
# morre na primeira fala.
_palavras = palavras

# ⛔⛔ A KEYWORD NATIVA, que o `ui_agente._keyword_nativa()` le'. Sem ela a UI
# assume `gelatin` (o padrao do `short_comum`), a comparacao com a palavra
# digitada nunca bate do jeito certo e a troca sai errada em silencio.
KEYWORD_NATIVA = KEYWORD


# ===========================================================================
# SORTEIO E LEDGER
# ===========================================================================

IMAGENS = ("IMAGE 01/05", "IMAGE 02/05", "IMAGE 03/05", "IMAGE 04/05",
           "IMAGE 05/05")
TAKES = ("TAKE 01/05", "TAKE 02/05", "TAKE 03/05", "TAKE 04/05", "TAKE 05/05")

MEMORIA = {"vida": 3, "porta": 2, "fonte": 2, "preco": 2, "semana": 2,
           "numero": 2, "testemunha": 2, "cozinha": 2, "roupa": 2}


def _carregar_ledger():
    try:
        with io.open(LEDGER, encoding="utf-8") as f:
            return json.load(f)
    except (IOError, OSError, ValueError):
        return {}


def _gravar_ledger(led, spec, em_disco=True):
    """A memoria SEMPRE anota; so' o disco e' poupado no --dry-run."""
    for eixo, n in MEMORIA.items():
        v = spec.get("_id_%s" % eixo)
        if v is None:
            continue
        h = led.setdefault(eixo, [])
        h.append(v)
        del h[:-n]
    if not em_disco:
        return
    try:
        with io.open(LEDGER, "w", encoding="utf-8") as f:
            f.write(json.dumps(led, ensure_ascii=False, indent=1))
    except (IOError, OSError):
        pass


def _evitando(rng, pool, recentes, chave=None):
    def _k(x):
        return x[chave] if chave else x
    livres = [x for x in pool if _k(x) not in recentes]
    return rng.choice(livres or list(pool))


def sortear(pagina, rng, led, travas=None):
    travas = travas or {}
    et = ETNIA[pagina]

    def _pega(eixo, pool, chave):
        if travas.get(eixo):
            ach = [x for x in pool if x.get(chave) == travas[eixo]]
            if ach:
                return rng.choice(ach)
        return _evitando(rng, pool, led.get(eixo, []), chave)

    vida = _pega("vida", VIDAS, "id")
    porta = _pega("porta", PORTAS, "id")
    fonte = _evitando(rng, FONTES_LIVRO, led.get("fonte", []))
    preco = _evitando(rng, PRECOS, led.get("preco", []))
    semana = _evitando(rng, PRIMEIRA_SEMANA, led.get("semana", []))
    numero = _evitando(rng, NUMEROS, led.get("numero", []))
    test = _evitando(rng, TESTEMUNHAS, led.get("testemunha", []))
    coz = _evitando(rng, COZINHAS, led.get("cozinha", []))
    roupa = _pega("roupa", ROUPAS, "id")

    # ⛔⛔ AS CINCO FALAS. A 1 e' VAZIA por construcao — o take 1 e' mudo, e
    # medido: os cinco videos da fonte abrem sem uma palavra por 6,6 a 8,1
    # segundos. Fala no take 1 mataria o unico momento em que o espectador
    # olha o ANTES sem nada competindo.
    # ⭐ E a fala 5 fecha com `vida["virada"]`, que e' a MESMA IMAGEM da fala
    # 2 invertida. As duas vem do mesmo registro por isso.
    def _M(t):
        """Maiuscula na primeira letra.

        ⛔ Os campos `dor` e `virada` nascem em minuscula no pool porque
        alguns sao oracoes que continuam a frase anterior. Aqui `dor` abre
        sentenca propria, e sem isto o video saia com `I'm 70 years old. my
        own grandchildren...`. Achado LENDO O LOTE — a lente `LV9` varria so'
        os blocos de IMAGE e nao as falas, e passou a varrer as duas.
        """
        return t[:1].upper() + t[1:] if t else t

    falas = [
        "",
        "%s. %s." % (vida["quem"], _M(vida["dor"])),
        "%s. %s." % (fonte, preco),
        "%s. %s." % (porta["primeira"], semana),
        "%s. And %s." % (numero, vida["virada"]),
    ]

    return {
        "pagina": pagina, "etnia": et,
        "vida": vida, "porta": porta, "cozinha": coz, "roupa": roupa,
        "testemunha": test, "lista": porta["lista"],
        "falas": falas,
        "_id_vida": vida["id"], "_id_porta": porta["id"], "_id_fonte": fonte,
        "_id_preco": preco, "_id_semana": semana, "_id_numero": numero,
        "_id_testemunha": test, "_id_cozinha": coz,
        "_id_roupa": roupa["id"],
    }

# ===========================================================================
# MONTAGEM
# ===========================================================================

def montar(spec):
    vida, porta, et = spec["vida"], spec["porta"], spec["etnia"]
    f = spec["falas"]
    subst = "man" if vida["sexo"] == "homem" else "woman"
    ela = "he" if vida["sexo"] == "homem" else "she"
    dela = "his" if vida["sexo"] == "homem" else "her"

    def _M(txt):
        """Maiuscula na primeira letra.

        ⚠️ `POSE_ANTES` e `POSE_DEPOIS` nascem em minuscula porque sao oracoes
        soltas, e na montagem entram logo depois de um ponto. A string travada
        nao se reescreve — quem se ajusta e' a montagem. Mesmo conserto ja'
        feito no ATEM 16 e no GELO 16.
        """
        return txt[:1].upper() + txt[1:] if txt else txt

    def _p(txt):
        """A pose e o corpo vem escritos no feminino; troca quando e' homem."""
        if vida["sexo"] != "homem":
            return txt
        for a, b in (("She is", "He is"), ("she ", "he "), ("her ", "his "),
                     ("Her ", "His ")):
            txt = txt.replace(a, b)
        return txt

    voz = ("Voice: one %s American %s in %s %ss, speaking plainly and warmly "
           "to camera at ordinary conversational volume, unhurried, the way "
           "someone tells a story they have told before. The pitch, the "
           "texture and the accent are identical in every take."
           % (et.split()[0].lower(), subst, dela,
              "sixtie" if vida["idade"] >= 60 else "fortie"))

    b = {}
    b["BLOCO 0 (REF)"] = (
        "REF 01: Photo of a real person: a head and shoulders portrait of a "
        "%d-year-old %s %s with an ordinary relatable face, plain neutral "
        "grey background, soft even frontal light, the head upright and "
        "facing the lens. Slight sensor grain, raw amateur photo look. No "
        "on-screen text, no subtitles, no captions, no watermark."
        % (vida["idade"], et, subst))

    # ⛔⛔ OS CINCO QUADROS SAO O MESMO LUGAR, O MESMO ENQUADRAMENTO, A MESMA
    # ROUPA E A MESMA LUZ. So' o CORPO muda entre o quadro 1 e os outros
    # quatro. Ordem do operador, e ela e' melhor que a fonte: com o mesmo
    # quadro o espectador nao precisa ACREDITAR que sao a mesma pessoa, ele
    # VE. Trocar de lugar, como a fonte faz, e' o que ESCONDE o salto.
    # ⚠️ O preco: no mesmo quadro qualquer diferenca de rosto ou de luz vira
    # mentira obvia. Por isso o `lugar`, a `roupa` e a `luz` sao montados UMA
    # vez e reusados nos cinco — a lente `LV10` cobra que sejam identicos.
    lugar = spec["cozinha"].capitalize() + "."
    peca = spec["roupa"]["peca"]
    baixo = spec["roupa"]["baixo"]
    luz = ("Flat even daylight from a window on the left, the same light in "
           "every shot.")

    # ⚠️ O rotulo `MONTH 1` NAO e' pedido ao gerador: ele e' queimado no Veo
    # Editor. Pedir texto devolve `MOUNTH`, e a fonte prova.
    b["IMAGE 01/05"] = (
        "IMAGE 01/05: %s %s A %d-year-old %s %s stands in the middle of the "
        "frame facing the camera, framed from the knees up, wearing a %s and "
        "%s. %s %s %s %s"
        % (ORIENTACAO, lugar, vida["idade"], et, subst, peca, baixo,
           _p(CORPO_ANTES % peca),
           _M(_p(POSE_ANTES % porta["liquido"])) + ".", luz, CAUDA_LV))

    # ⭐⭐ IMAGE 02 — O ESPELHO. A MESMA pose do quadro 1, o MESMO copo, a
    # MESMA roupa, o MESMO lugar. So' o corpo mudou. E' este par que faz o
    # antes/depois: o olho nao compara duas poses diferentes, compara duas
    # versoes da MESMA pose.
    # ⚠️ Ele nao gasta um take: a AdBatch usa a IMAGE como PRIMEIRO QUADRO, e
    # o `TAKE 02` anima ela baixando o copo e comecando a falar.
    b["IMAGE 02/05"] = (
        "IMAGE 02/05: %s %s The same %d-year-old %s %s stands in exactly the "
        "same spot, in the same framing from the knees up, wearing the same "
        "%s and %s. %s %s %s %s"
        % (ORIENTACAO, lugar, vida["idade"], et, subst, peca, baixo,
           _p(CORPO_DEPOIS % peca),
           _M(_p(POSE_ANTES % porta["liquido"])) + ".", luz, CAUDA_LV))

    # ⭐ Os tres ultimos quadros: mesma pessoa, mesmo lugar, ja' falando.
    for k in IMAGENS[2:]:
        b[k] = ("%s: %s %s The same %d-year-old %s %s stands in exactly the "
                "same spot, in the same framing from the knees up, wearing "
                "the same %s and %s. %s %s %s %s"
                % (k, ORIENTACAO, lugar, vida["idade"], et, subst, peca,
                   baixo, _p(CORPO_DEPOIS % peca),
                   _M(_p(POSE_DEPOIS)) + ".", luz, CAUDA_LV))

    # ⛔ TAKE 01 — MUDO. Sem `Dialogue:`, sem voz.
    b["TAKE 01/05"] = (
        "TAKE 01/05: Animate the image exactly. Locked-off tripod shot, no "
        "camera movement and no cuts. %s lifts the glass halfway to %s mouth "
        "and lowers it again without drinking, and that is the only movement. "
        "%s never speaks, never smiles and never looks at the lens. Nothing "
        "else in the frame moves.\n%s"
        % (ela.capitalize(), dela, ela.capitalize(), SILENCIO))

    # ⭐ TAKE 02 — a virada acontece DENTRO do take: ela abaixa o copo,
    # levanta os olhos e comeca a falar. O primeiro quadro ainda e' o espelho
    # do 01; no ultimo ela ja' esta' olhando a lente.
    b["TAKE 02/05"] = (
        "TAKE 02/05: Animate the image exactly. Locked-off tripod shot, no "
        "camera movement and no cuts. %s starts in the same position as the "
        "previous shot, then lowers the glass to %s side, lifts %s eyes to "
        "the lens and begins to speak. %s does not walk or turn and stays in "
        "the same spot. Nothing else in the frame moves.\n"
        'Dialogue: "%s"\n%s\n'
        "Audio: quiet room tone only. No music."
        % (ela.capitalize(), dela, dela, ela.capitalize(), f[1], voz))

    for i, k in enumerate(TAKES[2:], 2):
        b[k] = ("%s: Animate the image exactly. Locked-off tripod shot, no "
                "camera movement and no cuts. %s talks straight to the lens "
                "with small natural hand movements and does not walk or turn. "
                "Nothing else in the frame moves.\n"
                'Dialogue: "%s"\n%s\n'
                "Audio: quiet room tone only. No music."
                % (k, ela.capitalize(), f[i], voz))
    return b

# ===========================================================================
# LENTES
# ===========================================================================

# ⛔⛔ LV7 — A GRAFIA ERRADA DO ROTULO. O lote da fonte saiu com `MOUNTH 1`
# queimado em varias pecas: um caractere errado num campo de config do editor,
# replicado em N videos. Legenda queimada nao tem revisao depois.
_MOUNTH = re.compile(r"\bmounth\b|\bmonths\s+1\b", re.I)

# ⛔ LV6 — ESTE ANGULO NAO TEM CTA FALADO. Nenhum dos cinco videos da fonte
# pede nada; o video inteiro e' prova. Um pedido no fim quebraria o unico
# formato do parque que converte sem pedir.
_CTA = re.compile(
    r"\bcomment\b|\bdm me\b|\blink in bio\b|\btype \w+ below\b"
    r"|\bclick \w+\b|\bsend me\b", re.I)

# ⛔ LV5 — nenhuma promessa medica nem numero de saude. A fonte fala de PESO e
# de ROUPA, nunca de cura. `my doctor took me off two medications` e' relato
# de terceiro sobre o passado, e passa; `this cures diabetes` nao.
_CURA = re.compile(
    r"\bcures\b|\bcured\b|\bheals?\b|\btreats?\b|\bdiabetes\b"
    r"|\bcancer\b|\bblood pressure\b|\bdisease\b", re.I)

_ANTICELEB = re.compile(
    r"\bnot\s+(?:a\s+)?(?:celebrity|celebrities|famous|model|actor)\b",
    re.I)
_APARELHO = re.compile(
    r"\b(?:phone|smartphone|filming|records?\s+her)\b", re.I)

try:
    from short_comum import trocar_keyword as _sc_trocar   # noqa: F401
except ImportError:                                        # pragma: no cover
    pass


def _direcao(txt):
    return txt.split("\nDialogue:")[0]


def _M(t):
    """Maiuscula na primeira letra — usada pela montagem e pelo lint."""
    return t[:1].upper() + t[1:] if t else t


def lint(spec, blocos):
    ach = []
    f = spec["falas"]
    todos = "\n".join(blocos.values())
    direcoes = "\n".join(_direcao(v) for v in blocos.values())
    vida = spec["vida"]

    for k in IMAGENS:
        if not blocos[k].startswith(k + ":"):
            ach.append(("ERRO", "LV0: %s nao comeca com o proprio rotulo — o "
                                "parser da AdBatch separa os blocos por ele."
                        % k))
        if ORIENTACAO not in blocos[k]:
            ach.append(("ERRO", "LV0: %s sem a orientacao vertical." % k))
        if re.search(r"\.\s+[a-z]", blocos[k]):
            ach.append(("ERRO", "LV9: %s tem frase comecando em MINUSCULA "
                                "depois de ponto. Prosa quebrada faz o "
                                "gerador inventar — o defeito ja' apareceu no "
                                "ATEM, no GELO e aqui." % k))
        if CAUDA_LV not in blocos[k]:
            ach.append(("ERRO", "LV0: %s sem a cauda de textura." % k))

    # ⛔⛔ LV1 — A ESPINHA DO ANGULO. A fala 5 tem de fechar na MESMA imagem em
    # que a fala 2 abriu. Se as duas viessem de registros diferentes, o video
    # abriria numa humilhacao e fecharia noutra, e o formato perde o que o faz
    # funcionar sem CTA nenhum.
    # ⚠️ `[1:]`: a montagem capitaliza a `dor` para ela abrir sentenca, entao
    # a string crua do pool nunca casa inteira. Mesmo falso positivo da `LV4`,
    # e a segunda vez que ele aparece neste arquivo.
    if vida["dor"][1:] not in f[1]:
        ach.append(("ERRO", "LV1: a fala 2 nao carrega a humilhacao do "
                            "registro sorteado."))
    if vida["virada"] not in f[4]:
        ach.append(("ERRO", "LV1: a fala 5 nao fecha na virada do MESMO "
                            "registro — abrir numa humilhacao e fechar noutra "
                            "mata o formato."))

    # ⛔ LV2 — o take 1 e' MUDO
    if f[0].strip():
        ach.append(("ERRO", "LV2: o take 1 tem fala. Medido na fonte: os "
                            "cinco videos abrem sem uma palavra por 6,6 a 8,1 "
                            "segundos."))
    if "Dialogue:" in blocos["TAKE 01/05"]:
        ach.append(("ERRO", "LV2: o TAKE 01 tem linha de Dialogue."))
    if SILENCIO not in blocos["TAKE 01/05"]:
        ach.append(("ERRO", "LV2: o TAKE 01 sem a trava de silencio."))

    # ⛔ LV3 — o teto de fala, medido em 2,82 palavras/s
    for i in (1, 2, 3, 4):
        n = palavras(f[i])
        if n > TETO_PALAVRAS_TAKE:
            ach.append(("ERRO", "LV3: a fala %d tem %d palavras (teto %d) — a "
                                "fonte fala 2,82 palavras/s, entao isso nao "
                                "cabe em 8s e sai cortado."
                        % (i + 1, n, TETO_PALAVRAS_TAKE)))
        elif n > TETO_PALAVRAS_TAKE - 2:
            ach.append(("AVISO", "LV3: a fala %d tem %d palavras, no limite."
                        % (i + 1, n)))

    # ⛔ LV4 — o antes e o depois nao trocam de lugar
    # ⛔⛔ LV4 / LV10 — O MESMO QUADRO NOS CINCO. Lugar, roupa e luz sao a
    # ancora do par antes/depois: se qualquer um mudar, o par deixa de ser
    # comparacao e vira duas fotos soltas.
    # ⚠️ A comparacao ignora o PRIMEIRO caractere: a montagem aplica
    # `.capitalize()` no lugar. Comparar o texto cru acusava 100% dos videos.
    for k in IMAGENS:
        if spec["cozinha"][1:] not in blocos[k]:
            ach.append(("ERRO", "LV4: %s nao esta' no MESMO lugar dos outros "
                                "— o par antes/depois so' e' comparacao se o "
                                "quadro nao mudar." % k))
        if k in ("IMAGE 01/05", "IMAGE 02/05"):
            # ⛔⛔ LV11 — O PAR ESPELHO. Os dois quadros tem de carregar a
            # MESMA pose do copo, caractere por caractere. Se divergirem, o
            # par deixa de ser antes/depois e vira duas fotos soltas.
            # ⚠️ Compara o trecho SEM genero: a montagem troca `her`->`his`
            # quando o elenco e' masculino, entao a string crua nunca casa.
            # Terceiro falso positivo do mesmo tipo neste arquivo — o padrao
            # e' sempre comparar a string do pool contra o texto ja'
            # transformado pela montagem.
            copo = ("holding a tall glass of %s at chest height in one hand"
                    % spec["porta"]["liquido"])
            if copo not in blocos[k]:
                ach.append(("ERRO", "LV11: %s nao tem a pose do copo. O "
                                    "quadro 1 e o 2 sao a MESMA pose com "
                                    "corpos diferentes — e' isso que faz o "
                                    "antes/depois." % k))
        if spec["roupa"]["peca"] not in blocos[k]:
            ach.append(("ERRO", "LV10: %s nao usa a MESMA peca de roupa. Ela "
                                "e' a ancora E a prova: esticada no primeiro "
                                "quadro, sobrando nos outros." % k))

    for i in (1, 2, 3, 4):
        if _CTA.search(f[i]):
            ach.append(("ERRO", "LV6: a fala %d pede alguma coisa. Este "
                                "angulo nao tem CTA falado — o video inteiro "
                                "e' prova." % (i + 1)))
        if _CURA.search(f[i]):
            ach.append(("ERRO", "LV5: a fala %d faz alegacao de saude. A "
                                "fonte fala de PESO e de ROUPA, nunca de "
                                "cura." % (i + 1)))
    for i in (1, 2, 3, 4):
        if re.search(r"\.\s+[a-z]", f[i]):
            ach.append(("ERRO", "LV9: a fala %d tem frase comecando em "
                                "MINUSCULA depois de ponto." % (i + 1)))
    if _MOUNTH.search(todos):
        ach.append(("ERRO", "LV7: grafia errada do rotulo do mes. A fonte saiu "
                            "com `MOUNTH 1` queimado em varias pecas."))
    if _ANTICELEB.search(todos):
        ach.append(("ERRO", "LV8: negacao de celebridade — ela INJETA o token."))
    if _APARELHO.search(direcoes):
        ach.append(("ERRO", "LV8: aparelho na direcao de cena — o gerador o "
                            "DESENHA (lote perdido no VICK 16)."))
    return ach

# ===========================================================================
# UI
# ===========================================================================

EIXOS_UI = [
    ("vida", "A VIDA (dor + virada)", "VIDAS", "id"),
    ("porta", "A PORTA DE ENTRADA", "PORTAS", "id"),
    ("roupa", "A PECA (a mesma nos 2)", "ROUPAS", "id"),
]

DROPDOWNS_UI = [("vida", "A VIDA", "VIDAS", "rotulo")]

PT_VIDA = {
    "sapato": "Nao amarrava o sapato de pe",
    "parque": "Nao corria atras dos filhos no parque",
    "carro": "Os netos a carregavam ate' o carro",
    "terno": "Nao cabia mais no terno do aniversario",
    "escada": "Parava no meio da propria escada",
    "cinto": "Pediu extensor de cinto no aviao",
    "chao": "Nao sentava no chao com a neta",
    "espelho": "Se escondia no fundo das fotos",
}


def resumo_pt(spec):
    f = spec["falas"]
    return ("%s · pagina %s (%s)\n"
            "  A VIDA     %s\n"
            "  ENTRADA    %s\n"
            "  take 1     MUDO (o antes)\n"
            "  fala 2     %d palavras\n"
            "  fala 3     %d palavras\n"
            "  fala 4     %d palavras\n"
            "  fala 5     %d palavras   (teto %d)"
            % (TITULO, spec["pagina"], spec["etnia"],
               PT_VIDA.get(spec["vida"]["id"], spec["vida"]["id"]),
               spec["porta"]["id"],
               palavras(f[1]), palavras(f[2]), palavras(f[3]),
               palavras(f[4]), TETO_PALAVRAS_TAKE))

# ===========================================================================
# AUTOTESTE
# ===========================================================================

def autoteste(n=400):
    print("=" * 70)
    print("AUTOTESTE — %s · %d sorteios" % (TITULO, n))
    print("=" * 70)

    rng = random.Random(20260902)
    led = {}
    erros, avisos = [], []
    vistos = {e: set() for e in MEMORIA}
    pior = [0, 0, 0, 0, 0]
    maior = 0

    for _ in range(n):
        sp = sortear(rng.choice(sorted(ETNIA)), rng, led, None)
        b = montar(sp)
        for nivel, msg in lint(sp, b):
            (erros if nivel == "ERRO" else avisos).append(msg)
        for e in MEMORIA:
            vistos[e].add(sp["_id_%s" % e])
        for i in range(5):
            pior[i] = max(pior[i], palavras(sp["falas"][i]))
        maior = max(maior, max(len(v) for v in b.values()))
        _gravar_ledger(led, sp, em_disco=False)

    print("\n1. LENTES")
    print("   ERRO  : %d" % len(erros))
    for m in sorted(set(erros))[:8]:
        print("      - %s" % m)
    print("   AVISO : %d (%d distintos)" % (len(avisos), len(set(avisos))))

    print("\n2. ALCANCE DOS POOLS")
    tam = {"vida": len(VIDAS), "porta": len(PORTAS),
           "fonte": len(FONTES_LIVRO), "preco": len(PRECOS),
           "semana": len(PRIMEIRA_SEMANA), "numero": len(NUMEROS),
           "testemunha": len(TESTEMUNHAS), "cozinha": len(COZINHAS),
           "roupa": len(ROUPAS)}
    mortos = 0
    for e in sorted(tam):
        viv = len(vistos[e])
        if viv != tam[e]:
            mortos += 1
        print("   %s %-11s %2d/%2d" % ("ok " if viv == tam[e] else "MOR",
                                       e, viv, tam[e]))
    if mortos:
        print("   ⛔ %d pool(s) com entrada inalcancavel." % mortos)

    print("\n3. TETO DE FALA (%d palavras, medido em 2,82 pal/s)"
          % TETO_PALAVRAS_TAKE)
    for i in range(5):
        rot = "MUDO" if i == 0 else "%2d palavras" % pior[i]
        print("   take %d: maximo %s" % (i + 1, rot))

    print("\n4. TAMANHO DE BLOCO (teto da AdBatch: 3.900)")
    print("   maior bloco gerado: %d caracteres" % maior)

    print("\n5. CONTROLE NEGATIVO")
    plantios = [
        ("LV1", lambda sp, bl: sp["falas"].__setitem__(
            4, "Ninety pounds gone. And I feel great.")),
        ("LV2", lambda sp, bl: sp["falas"].__setitem__(0, "Look at me.")),
        ("LV3", lambda sp, bl: sp["falas"].__setitem__(
            1, " ".join(["word"] * 40))),
        ("LV4", lambda sp, bl: bl.__setitem__(
            "IMAGE 03/05",
            bl["IMAGE 03/05"].replace(sp["cozinha"][1:], " garage"))),
        ("LV11", lambda sp, bl: bl.__setitem__(
            "IMAGE 02/05",
            bl["IMAGE 02/05"].replace("Standing still and facing", "Sitting"))),
        ("LV10", lambda sp, bl: bl.__setitem__(
            "IMAGE 02/05",
            bl["IMAGE 02/05"].replace(sp["roupa"]["peca"], "a dress"))),
        ("LV5", lambda sp, bl: sp["falas"].__setitem__(
            2, "It cured my diabetes in three weeks.")),
        ("LV6", lambda sp, bl: sp["falas"].__setitem__(
            3, "Comment RECIPE and I will send it to you.")),
        ("LV7", lambda sp, bl: bl.__setitem__(
            "IMAGE 01/05", bl["IMAGE 01/05"] + " The words MOUNTH 1 appear.")),
        ("LV8", lambda sp, bl: bl.__setitem__(
            "IMAGE 02/05", bl["IMAGE 02/05"] + " Ordinary face, not a celebrity.")),
        ("LV9", lambda sp, bl: bl.__setitem__(
            "IMAGE 02/05", bl["IMAGE 02/05"] + " she looks away.")),
        ("LV0", lambda sp, bl: bl.__setitem__(
            "IMAGE 01/05", bl["IMAGE 01/05"].replace("IMAGE 01/05: ", "", 1))),
    ]
    r2 = random.Random(7)
    for nome, planta in plantios:
        pegou = 0
        for _ in range(40):
            sp = sortear(r2.choice(sorted(ETNIA)), r2, {}, None)
            bl = montar(sp)
            planta(sp, bl)
            if any(m.startswith(nome + ":") for _n, m in lint(sp, bl)):
                pegou += 1
        print("   %s %-4s plantado 40x, acusado %d/40"
              % ("ok " if pegou == 40 else "FALHA", nome, pegou))

    print("\n" + "=" * 70)
    print("VEREDITO: %s" % ("REPROVADO — ha' ERRO de lente" if erros
                            else "aprovado, 0 ERRO em %d sorteios" % n))
    print("=" * 70)
    return 1 if erros else 0

# ===========================================================================
# CLI
# ===========================================================================

def main():
    # ⚠️ O console do Windows e' cp1252 e os marcadores da doutrina nao cabem
    # nele. Sem isto o motor morre com UnicodeEncodeError ANTES de imprimir o
    # primeiro bloco — e morre so' no caminho em que ha' algo a dizer.
    for _f in (sys.stdout, sys.stderr):
        try:
            _f.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass

    ap = argparse.ArgumentParser(description=TITULO)
    ap.add_argument("--pagina", choices=sorted(ETNIA), default="joe")
    ap.add_argument("--n", type=int, default=1)
    ap.add_argument("--seed", type=int)
    ap.add_argument("--vida", choices=[x["id"] for x in VIDAS])
    ap.add_argument("--porta", choices=[x["id"] for x in PORTAS])
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--autoteste", action="store_true")
    a = ap.parse_args()

    if a.autoteste:
        return autoteste()

    led = _carregar_ledger()
    rng = random.Random(a.seed)
    travas = {}
    if a.vida:
        travas["vida"] = a.vida
    if a.porta:
        travas["porta"] = a.porta

    # ⛔⛔ VIDEO COM ERRO NAO CHEGA A SER IMPRESSO. Se os blocos saem primeiro e
    # o diagnostico depois, o operador ja' copiou o roteiro antes de ler o
    # rodape — e' o padrao "agente reprovado rodavel" dentro do proprio motor.
    TENTATIVAS = 12
    for _ in range(a.n):
        ruins = []
        for tentativa in range(TENTATIVAS):
            s = sortear(a.pagina, rng, led, travas)
            b = montar(s)
            ach = lint(s, b)
            ruins = [x for x in ach if x[0] == "ERRO"]
            if not ruins:
                break
        if ruins:
            print("=" * 70)
            print("[ABORTADO] %d sorteios seguidos com ERRO — o defeito nao e' "
                  "de sorteio, e' de POOL. Abaixo so' o diagnostico:"
                  % TENTATIVAS)
            for nivel, msg in ruins:
                print("   [%s] %s" % (nivel, msg))
            print("=" * 70)
            continue
        print("=" * 70)
        print(resumo_pt(s))
        if tentativa:
            print("(%d re-sorteio(s) ate' passar nas lentes)" % tentativa)
        print("=" * 70)
        for k in ("BLOCO 0 (REF)",) + IMAGENS + TAKES:
            print("\n%s\n" % b[k])
        for nivel, msg in ach:
            print("[%s] %s" % (nivel, msg))
        # ⛔ A memoria anota SEMPRE — e' ela que faz os videos do lote diferirem
        # entre si. O `--dry-run` so' impede tocar no arquivo.
        _gravar_ledger(led, s, em_disco=not a.dry_run)
    return 0


if __name__ == "__main__":
    sys.exit(main())
