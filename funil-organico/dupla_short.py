#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
botica_short.py — randomizador + gerador + linter do AGENTE **BOTICA** (SHORT).

⭐ FONTE: True Health, reel facebook.com/reel/3973945436069257 (52,2s).
**1K reacoes / 1K comentarios / 53 shares** — e comentario e' o KPI do nosso
funil, entao a razao 1:1 com reacao e' o numero que importa aqui.
Baixado pela rota 2b do RUNBOOK-watch-videos, transcrito com Whisper e lido
frame a frame em 2026-08-04.

⭐ O QUE E' O ANGULO, em uma frase: uma mulher de traje tradicional, numa cozinha
forrada de potes de ervas secas, prepara uma receita caseira na frente da camera
— e o vilao e' a FARMACIA. A botica de casa contra a botica da esquina.

⛔ O QUE NENHUM DOS 13 AGENTES ANTERIORES TEM: a prova e' a **receita sendo
PREPARADA em cena**, com utensilio em movimento. Os outros mostram bancada
parada ou despejo; aqui a mao trabalha.

O ARCO — 3 cenas de 8s, destino AdBatch Vertical 3:

    cena 1  A ISCA      o prop gigante na lente + o despejo + O VILAO
    cena 2  O PREPARO   o metodo em acao + o ingrediente raro + gelatin trick
    cena 3  O COPO      o copo na lente + o HOMEM MUDO atras + o CTA

⚠️ A FALA DA FONTE, integral, que este motor TRADUZ (nunca inventa):
    "Did you know that if you add saffron to banana, this happens?
     Pharmacies don't want you to know this.
     In a mixer, add one chopped banana, a pinch of saffron, then add a
     tablespoon of honey, and squeeze half a lime. You can buy some of these
     products at Walmart or Costco. In the end, add a glass of water and blend
     well. Drink this every morning to increase blood flow and circulation to
     your wiener naturally. Want to learn another natural trick that could help
     your wiener grow up to 5 inches faster in a week? Comment wiener below and
     I'll personally send it to you. But don't forget to follow me. Otherwise,
     I can't find you."

⚠️ O Whisper ouviu `winner`: e' **wiener**, que ja' e' palavra do nosso NUCLEO.

⛔⛔ AS SEIS ORDENS DO OPERADOR NESTE AGENTE (2026-08-04), todas verificadas por
linter, nao por comentario:

  1. O METODO DE PREPARO NAO E' FIXO. *"nao fixe liquidificador = vai engessar o
     repertorio visual do take e tornar os videos muito parecidos entre si"*.
     O liquidificador da fonte e' UMA entrada de METODOS, nao a cena.
  2. O PROP sai do pool **ja' validado prompt a prompt no COLO** — banana,
     banana-da-terra, berinjela, cenoura, pastinaca. Pepino e abobrinha foram
     recusados pelo gerador e nao entram.
  3. ETNIA ARRASTA O MUNDO, e o pool inclui o americano tipico.
  4. UM ingrediente raro por video, sorteado entre os nove.
  5. O homem da cena 3 e' MUDO.
  6. ⛔ ZERO claim numerico de centimetro. A fonte promete "5 inches faster in a
     week"; nos ficamos com a promessa sem a medida.

⭐⭐ E ESTE AGENTE NASCE COM A §21 APLICADA: a PRIMEIRA sentenca de cada cena
nomeia o referente. Nao ha' uma abertura orfa neste motor, por construcao e por
linter (BO9). E' o primeiro que nasce assim.

Uso:
    python funil-organico/botica_short.py --pagina joe --n 1
    python funil-organico/botica_short.py --pagina ray --n 3 --seed 42 --dry-run
    python funil-organico/botica_short.py --autoteste
"""

import argparse
import collections
import json
import os
import random
import re
import sys

import short_comum as sc
from nucleo_sonoro import sonorizar

AQUI = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(AQUI, ".dupla-short-ledger.json")

TITULO = "AGENTE DUPLA SHORT"
SLUG = "dupla-short"
SUBTITULO = ("duas mulheres, dois props · o antes e o depois no MESMO "
             "quadro · gerador offline de prompts Veo")

ETNIA = {
    "joe": "white American", "ray": "white American", "matt": "white American",
    "marcus": "Black American", "chuck": "Black American",
    "hank": "white American", "wade": "white American",
    "isaiah": "Black American", "curtis": "Black American",
    "otis": "Black American",
}


# ⭐⭐ PELE TRAVAVEL — contrato aditivo criado no CLEAN V2 em 2026-08-05, e este
# motor tem exatamente o mesmo defeito que o criou: o seletor clara/escura do
# painel troca a PAGINA, e este motor IGNORA `ETNIA[pagina]` de proposito (a
# etnia sai de dentro do MUNDO, doutrina "etnia arrasta o mundo inteiro"). O
# operador clicava, o botao acendia, e o sorteio seguia aleatorio — pior que nao
# ter botao, porque PARECIA travado.
# ⚠️ Lido pela ui_agente com `getattr`: motor sem a flag nao muda de comportamento.
PELE_TRAVAVEL = True


# ⛔⛔ A CLASSIFICACAO E' LISTA EXPLICITA, NUNCA "tudo que nao e' branco".
# Correcao de campo do operador em 2026-08-05, com print: no CLEAN V2 ele travou
# `escura` e recebeu um REF Asian American. **Para ele, escura = NEGRO.**
# ⚠️ Asiatico, latino, mediterraneo, nativo e mestico nao sao nem clara nem
# escura — so' saem com a pele LIVRE. A regra binaria do `paginas_por_pele`
# (clara = tem `white`, escura = o resto) e' o que produzia o defeito, e eu a
# tinha herdado meia hora antes achando que estava sendo congruente.
# ⛔ Mesma lista dos outros motores: classificacoes divergentes entre agentes
# seriam o fragmento espelhado que a P9 proibe.
PELE_ETNIAS = {
    "escura": ("Black American",),
    "clara": ("white American",),
}


def _pele_de(etnia):
    """A pele da etnia pela lista explicita — ou None (neutra, so' no livre)."""
    for pele, ets in PELE_ETNIAS.items():
        if etnia in ets:
            return pele
    return None


# ---------------------------------------------------------------------------
# STRINGS TRAVADAS — leitura otica da fonte. NAO REESCREVER.
# ---------------------------------------------------------------------------

# ⭐⭐ BO1 — A ISCA NA LENTE. E' o hook inteiro em uma frase, lido no frame 0:00:
# o prop descascado ocupa METADE do quadro porque esta' empurrado para a lente,
# perto da camera, e o corpo dela fica pequeno atras. A tacinha da substancia
# vem na outra mao, mais alta, e despeja por cima aos 0:05.
# ⛔ A escala vem do ENQUADRAMENTO (mao esticada para a lente), nunca de dizer
# que o objeto e' gigante: `absurdly oversized` esta' no selo de risco do
# banco-hooks e ja' custou recusa.
# ⭐⭐ O QUADRO 1 — O DEITICO DUPLO. Lido na fonte a 1 fps: as duas ficam lado
# a lado contra a parede, cada uma com UM prop erguido a altura do peito. A da
# esquerda fala; a da direita nao abre a boca.
# ⛔ Os dois props no MESMO frame, e nenhum deles encostado no corpo de ninguem:
# proxy junto do corpo e' o que a moderacao pega (ver prop-metaforas).
BO_DUPLA = (
    "Two women stand side by side, shoulder to shoulder, filmed straight on "
    "from the waist up. On frame-left is a %d-year-old %s woman, %s, %s, "
    "wearing %s; she holds %s raised at chest height in her right hand. On "
    "frame-right is a %d-year-old %s woman, %s, %s, wearing %s; she holds %s "
    "raised at chest height in her left hand. Both objects are fully in frame "
    "and neither touches either woman's body. The woman on the left looks "
    "straight into the lens with her mouth open mid-word as she speaks. The "
    "woman on the right keeps her mouth closed and never speaks."
)

# ⛔ BO2 — no TAKE da cena 1 o prop NAO muda de estado. Este agente nao tem
# crescimento: quem cresce e' o RESSURREICAO. O bit visual aqui e' a COMPARACAO.
# ⚠️ Nunca `completely motionless` num objeto que a mao segura — ordem impossivel,
# e o Veo resolve SOLTANDO o objeto (F12b). Diz-se pela POSICAO.
# ⛔⛔ O `BO_ISCA_ESTAVEL` do BOTICA FOI APAGADO daqui. Ele descrevia *"Her right
# hand keeps the dish... Only the falling scatter moves"* — prato e despejo, numa
# cena de dois props erguidos. Enquanto ele existia no arquivo, bastava alguem
# religa-lo por copia; string morta do angulo errado e' bomba com pino.

# ⭐⭐ BO3 — O PREPARO. ⛔ ORDEM DO OPERADOR: o utensilio NAO E' FIXO. A fonte usa
# liquidificador; travar isso faria os videos deste agente parecerem o mesmo
# video. O metodo entra pelo pool METODOS e o verbo acompanha.
# ⭐⭐ O QUADRO 2 — O DESPEJO DUPLO. Lido na fonte: ela segura UM JARRO EM CADA
# MAO e despeja os dois AO MESMO TEMPO num copo alto — beterraba (vermelho) e
# cenoura (laranja). Os dois jatos caindo juntos sao o bit visual desta cena, e
# a cor faz o trabalho: vermelho e laranja num copo transparente.
# ⚠️ A SEGUNDA MULHER continua em quadro, atras, MUDA. Sem isso o Veo perde a
# dupla entre a cena 1 e a 3 e devolve outra pessoa no payoff.
# ⭐⭐ AS CONFORMACOES DO PREPARO — ordem do operador, 2026-08-05, lendo o lote:
# *"eu te falei pra voce criar uma pool de conformacao de prep receita diferente,
# nao quero so' essa conformacao da ref pouring duas jarras num copo, escolha
# mais pelo menos 4 conformacoes pra pool"*.
#
# ⛔ A RECEITA NAO MUDA — beterraba + cenoura + o raro + o gelatin trick, que e'
# o que a fala nomeia. O que varia e' a FISICA: como os dois sucos chegam ao
# copo. Trocar os ingredientes junto quebraria a copy, que e' alcada do operador.
#
# ⛔⛔ CADA ENTRADA CARREGA O SEU `mov` E O SEU `audio`. E' obrigatorio, nao
# organizacao: se o movimento vier de fora, o TAKE volta a mandar socar pilao
# numa cena de despejo — o defeito que a lente `lint_take_vs_image` foi criada
# para pegar hoje. Conformacao e movimento sao a mesma decisao.
#
# ⚠️ A BETERRABA APARECE EM TODAS. A versao anterior punha *"a whole pomegranate
# and two carrots"* na bancada enquanto a boca dizia `beetroot juice` — a fruta
# errada em 88,8% dos videos, achada na auditoria da etapa [7].
PREPAROS = [
    {"id": "dois_jarros",
     "bancada": "a tall clear glass, and beside it %(raro_img)s, two raw "
                "beetroots and two carrots",
     "acao": "She holds a glass jug in each hand and pours both at once into "
             "the tall glass — deep red juice from the left jug and bright "
             "orange juice from the right — the two streams falling together",
     "mov": "She keeps pouring from both jugs at once into the tall glass, the "
            "two streams meeting in it the whole time, her forearms steady. She "
            "never sets either jug down.",
     "audio": "juice pouring into a glass"},

    {"id": "liquidificador",
     "bancada": "a blender jug on its base, filled with cut beetroot and "
                "carrot, a tall clear glass beside it and %(raro_img)s",
     "acao": "Her right hand rests on the blender base and her left sets the "
             "lid down onto the jug, the cut beetroot and carrot packed inside "
             "against the glass",
     "mov": "Her left hand presses the lid down onto the blender jug and stays "
            "there; her right hand stays flat on the base.",
     "audio": "a blender motor starting up"},

    {"id": "espremedor",
     "bancada": "a stainless juicer with a tall clear glass under its spout, "
                "%(raro_img)s and a bowl of cut beetroot and carrot",
     "acao": "Her right hand pushes a carrot down the juicer chute with the "
             "plunger while bright orange juice runs from the spout into the "
             "glass, a beetroot already fed through and staining the pulp red",
     "mov": "Her right hand keeps pressing the plunger down the chute at the "
            "same slow rate and the juice keeps running from the spout into the "
            "glass. Her left hand stays flat on the %(sup)s.",
     "audio": "a juicer running"},

    {"id": "camadas",
     "bancada": "a tall clear glass already filled in two layers — deep red "
                "below and bright orange above — with %(raro_img)s beside it, "
                "two raw beetroots and two carrots",
     "acao": "Her right hand turns a long spoon slowly through the glass and "
             "the two layers begin to marble into each other",
     "mov": "Her right hand keeps turning the long spoon slowly through the "
            "glass the whole time and never lifts it clear. Her left hand stays "
            "flat on the %(sup)s.",
     "audio": "a spoon turning in a glass"},

    {"id": "medidor",
     "bancada": "a tall clear glass, a graduated glass measuring jug of deep "
                "red juice in her hand, a second jug of bright orange juice "
                "waiting beside it, %(raro_img)s, two raw beetroots and two "
                "carrots",
     "acao": "Her right hand tips the measuring jug and a steady thread of deep "
             "red juice falls into the tall glass, filling it to the halfway "
             "mark",
     "mov": "Her right hand keeps the measuring jug at the same tilt and the "
            "red thread keeps falling into the glass at the same rate. She "
            "never sets the jug down and never picks up the second one.",
     "audio": "juice pouring into a glass"},

    {"id": "coador",
     "bancada": "a fine mesh sieve set over a tall clear glass, deep red pulp "
                "in it, %(raro_img)s, two raw beetroots and two carrots",
     "acao": "Her right hand presses the back of a spoon into the pulp in the "
             "sieve and deep red juice runs through the mesh into the glass "
             "below",
     "mov": "Her right hand keeps pressing the back of the spoon into the pulp "
            "in the sieve at the same slow rate and the juice keeps running "
            "through into the glass. Her left hand holds the sieve rim steady.",
     "audio": "juice dripping through a sieve"},
]

BO_PREPARO = (
    "Medium shot in %(coz)s, filmed straight on at the height of the %(sup)s, "
    "framed so that %(sup_a)s runs across the bottom third of the picture. "
    "Standing behind it, centred in the frame, is %(ancora)s. On the %(sup)s in "
    "front of her stands %(bancada)s. %(acao)s. She looks directly into the lens "
    "with her mouth open mid-word as she speaks. %(amiga)s"
)

# ⭐ A AMIGA — a segunda mulher, MUDA nas tres cenas. Ela e' quem segura o prop
# gigante na cena 1 e quem faz a comparacao existir.
# ⛔ `never speaks` e' obrigatorio: sem isso o Veo dubla as duas.
BO_AMIGA_FUNDO = (
    "Standing a step behind her and slightly to frame-right is the same "
    "%d-year-old %s woman from the first scene, %s, %s, wearing %s; %s, and she "
    "never speaks."
)

# ⛔ BO4 — ela nunca toca no resto da bancada. Sem isto o Veo comeca a mexer em
# tudo o que esta' em quadro e a continuidade entre os blocos de 8s morre.
BO_NAO_TOCA = ("Nothing else on the %s is touched, moved, opened or lifted, and "
               "nothing is added to it or taken away.")

# ⭐ BO5 — O COPO DO PAYOFF, lido em 0:30: ela empurra o copo para a lente com a
# mao, o liquido opaco e cremoso, dois canudos dentro.
# ⛔ Ele so' existe na CENA 3, e e' o objeto da keyword — esta' na mao no frame em
# que a boca diz `gelatin,`. Mostra-lo antes entrega o payoff antes da promessa.
# ⛔ Aqui estava `... a thick pale drink, two a single paper straw standing in
# it` — literal QUEBRADO, indo inteiro para o prompt. Nasceu de um replace meu
# que trocou "paper straws" por "a single paper straw" e deixou o "two" da linha
# de cima. Consertei no PLACA e nao aqui: correcao aplicada num motor e nao no
# irmao e' o mesmo modo de falha que o §29 descreve, na direcao oposta.
BO_COPO = ("a tall clear glass filled to the top with a thick pale drink, a "
           "single paper straw standing in it")
# ⛔ UM canudo. Eram dois e o operador reprovou o render: *"dois canudos? quero
# so' um"*. Dois canudos leem como bebida COMPARTILHADA — e este copo e' dele.

# ⭐⭐ BO6 — O HOMEM MUDO. Ordem do operador: *"no take final, alem do ref
# falando, havera um homem sempre atras, com cara de espanto e surpresa e
# olhando para o objeto na mao do ref"*.
# ⛔ Ele olha para O COPO, nunca para a lente, e NUNCA fala. E' a mesma mecanica
# da plateia congelada do ESCANDALO: ele encena o espanto NO LUGAR do espectador.
# ⚠️ `Only she speaks` e' obrigatorio no TAKE — sem isso o segundo corpo dubla a
# fala dela, que e' a falha que derrubou a cena do casal do VAZAMENTO.
# ⭐⭐ A FEICAO DELE E' POOL desde 2026-08-05 — ordem do operador: *"A feicao de
# reacao do cara no take 3 tem que variar tb na pool, se sorrindo, cara de
# surpresa, etc"*. Antes era UMA string travada (olhos arregalados, boca
# aberta), e por isso os tres prints que ele mandou tinham o mesmo homem com a
# mesma cara.
# ⛔ O QUE NAO VARIA, porque e' a mecanica do angulo e o linter trava: ele olha
# o COPO e nunca a lente, e NUNCA fala. A reacao muda de SABOR (espanto, riso,
# incredulidade, orgulho), nunca de direcao nem de mudez.
# ⚠️ Cada entrada e' (clausula da IMAGE, clausula do TAKE) e as duas tem de
# descrever a MESMA coisa: o take anima a image, nao inventa outro gesto — e
# contradicao entre os dois e' pior que omissao, porque o Veo resolve mexendo
# no que estava certo.
# ⭐⭐ AS REACOES DA AMIGA — pool PROPRIO, e ele existe porque o operador leu o
# render e reprovou: *"personagem com cara de nojo?"*.
# ⛔ A amiga reagia com o pool do HOMEM ESPANTADO, que tem entradas de duvida e
# incredulidade (`eyebrows drawn together`, `caught between a frown and a smile`,
# `plainly not believing it`). Numa mulher jovem ao lado de outra, franzir a
# testa nao le como espanto — le como NOJO, e nojo no rosto de quem esta' ao lado
# do prop mata a promessa inteira.
# ⚠️ Aqui so' entra o que e' POSITIVO: admiracao, riso, surpresa boa, orgulho.
# Nada de franzir, estreitar os olhos ou duvidar.
REACOES_AMIGA = [
    ("her eyebrows are raised and she is smiling widely, delighted",
     "holds that delighted smile without moving"),
    ("she is laughing openly with her head tipped back a little",
     "keeps laughing silently without moving"),
    ("her eyes are wide and she is grinning, plainly impressed",
     "holds that impressed grin without moving"),
    ("she is smiling with her lips pressed together, eyebrows high",
     "holds that closed-lip smile without moving"),
    ("her mouth is open in a happy gasp, eyes bright",
     "holds that open, happy expression without moving"),
    ("she is beaming, one hand resting on the other woman's shoulder",
     "keeps beaming, hand steady on the shoulder"),
    ("her chin is lifted and she is nodding, smiling broadly",
     "keeps nodding and smiling broadly"),
    ("she is smiling with her eyes crinkled at the corners, amused",
     "holds that amused smile without moving"),
    ("her eyebrows are high and she is biting back a laugh",
     "keeps biting back the laugh without moving"),
    ("she is smiling wide with her eyes on the object, clearly approving",
     "holds that approving smile without moving"),
    ("her mouth is open in a silent wow, eyes shining",
     "holds that silent wow without moving"),
    ("she is grinning and raising both eyebrows at once",
     "holds that raised-eyebrow grin without moving"),
]

REACOES_HOMEM = [
    ("his eyes are wide and his eyebrows are raised, his mouth open in plain "
     "astonishment",
     "holds his astonished expression without moving"),
    ("a slow grin is spreading across his face and his eyebrows are lifted",
     "holds that spreading grin without moving"),
    ("his eyebrows are drawn together and his head is tilted, caught between "
     "a frown and a smile",
     "holds that half-frowning, half-smiling look without moving"),
    ("his lips are pressed shut and his brows are high, plainly holding back "
     "a laugh",
     "keeps his lips pressed shut on the laugh without moving"),
    ("he is grinning openly, eyes crinkled at the corners",
     "holds that open grin without moving"),
    ("one eyebrow is raised and his mouth is slightly open as he leans a "
     "little closer",
     "holds that leaning, one-eyebrow look without moving"),
    ("his jaw has gone slack and he is blinking slowly, as if recounting "
     "something",
     "keeps that slack-jawed look without moving"),
    ("his mouth is open in a delighted laugh with no sound coming out",
     "holds that silent, delighted laugh without moving"),
    ("his chin is lifted and he is nodding very slightly, mouth open",
     "keeps his chin lifted and nods very slightly"),
    ("his eyes have gone round and one hand has stopped halfway to his mouth",
     "keeps his hand frozen halfway to his mouth"),
    ("his brows are high and he is smiling with his mouth closed, looking "
     "pleased with himself",
     "holds that closed-mouth, pleased smile without moving"),
    ("his eyes are narrowed slightly and his mouth is open, plainly not "
     "believing it",
     "holds that disbelieving look without moving"),
]

BO_HOMEM = (
    "Standing behind her and slightly to frame-left, close enough to be in the "
    "same focus, is a %d-year-old %s man, %s, wearing %s. %s, and he is "
    "looking directly at the glass in her hand — never at the camera."
)
# ⛔ Aqui estava `BO_HOMEM_TAKE` — *"The man behind her..."* — herdado do
# BOTICA e usado na cena 3 deste motor, que NAO TEM HOMEM. A segunda pessoa aqui
# e' a AMIGA, e ela e' o angulo inteiro: duas mulheres, uma com o prop murcho e
# a outra com o grande. Mandar o Veo animar "o homem atras dela" numa imagem de
# duas mulheres e' pedir que ele invente um terceiro corpo ou troque a amiga.
BO_AMIGA_TAKE = (
    "The other woman %s, eyes on what she is holding the whole time, and never "
    "speaks. Only the woman on frame-left speaks, straight into the lens."
)

# ⛔ BO7 — A ANCORA DE CONTINUIDADE. Rosto E idade, nunca so' roupa: no VAZAMENTO
# a ancora estava na camisa e o render devolveu um senhor de oculos e bigode no
# lugar do corpo-prova.
# ⚠️ Comeca em minuscula: entra no meio da frase e o `_cap` a levanta quando abre.
BO_ANCORA = ("the same %d-year-old %s woman from the first scene, same %s, same "
             "%s, same %s")

# ⭐⭐ A CLAUSULA ANTI-CELEBRIDADE, NO REGISTRO DE MULHER. Ordem do operador,
# 2026-08-05, lendo o prompt gerado: a REF deste angulo **e' top model**.
# ⛔ `Ordinary relatable face, not a model` brigava DE FRENTE com o pool: o
# gerador recebia "tall and long-legged, strikingly beautiful" no corpo e "cara
# comum, nao e' modelo" no rosto NA MESMA FRASE, e resolvia a contradicao contra
# nos — rosto sem graca em cima de um corpo encomendado bonito.
# ⚠️ E' o mesmo conserto que o CLEAN ja' tinha feito (CL26): a protecao de
# IDENTIDADE (nao-celebridade) fica; so' sai o "comum" e o "nao e' modelo".
ANTICELEB = ("A strikingly beautiful face, not a celebrity, not resembling "
             "any famous person.")
CAUDA = "Shot on iPhone, natural grain. No on-screen text, no watermark."


# ---------------------------------------------------------------------------
# ⭐⭐ MUNDOS — A BOTICA, E A ETNIA SAI DE DENTRO DELA
# ---------------------------------------------------------------------------
# ⛔ NAO EXISTE EIXO `etnia` SOLTO. Ordem do operador: *"variar etnia e' arrastar
# o mundo inteiro — cenario, traje, luz, audio"*. Aqui o mundo carrega tambem a
# TRADICAO DE ERVAS, que e' a autoridade do angulo.
# ⚠️ O operador mandou incluir o americano tipico no pool ("mundo entre varios,
# inclui tb o tipico cidadao norte americano").
# ⛔ ZERO texto legivel em qualquer set: a CAUDA promete "No on-screen text", e
# pote de erva com etiqueta escrita e' texto em cena. Os potes entram como
# `unlabelled glass jars`.
# ⚠️ O selo `V` fica so' no mundo da fonte (o amish); os outros sao `N`.
# ⛔⛔ ARQUETIPOS REGIONAIS DOS EUA — reescrito em 2026-08-05 por duas ordens
# do operador, dadas lendo o lote gerado:
#
#   1. *"quando eu me referi a etnia dentro dos EUA eu me referia ao pessoal
#      tipico do Brooklyn, pessoal tipico da Louisiana, pessoal tipico do Texas
#      — cada regiao dentro dos EUA tem seu arquetipo, e nao 'polish american'
#      como vc fez"*.
#      ⚠️ Eu tinha FILTRADO os mundos do BOTICA, que sao de HERANCA IMIGRANTE
#      (polonesa, italo-americana, amish). E' outra coisa: heranca e' de onde a
#      familia veio; arquetipo regional e' quem a pessoa E' hoje. O cara do
#      Brooklyn e o do Texas sao os dois `white American` no papel e nao se
#      parecem em nada — e e' essa diferenca que faz o lote variar de verdade.
#
#   2. *"estamos no nicho de ED, nao quero excesso de roupa nas refs femininas"*.
#      ⚠️ Os trajes herdados eram blusas folcloricas fechadas ate' o pescoco.
#      Num funil onde a REF E' a bullet de retencao, roupa fechada e' o hook
#      jogado fora. Todos os trajes abaixo mostram corpo — e cada um no idioma
#      da regiao, porque cut-off jeans no Texas e biquini em Miami nao sao a
#      mesma coisa.
#
# ⭐ A ETNIA CONTINUA SAINDO DE DENTRO DO MUNDO, mas agora ela e' consequencia
# da REGIAO e nao de um rotulo: Atlanta e' Black American, Miami tem cubano,
# Texas e Arizona tem mexicano-americano, e o resto varia dentro da regiao.
MUNDOS = [
    {"id": "brooklyn", "selo": "N", "familia": "brooklyn",
     "etnias": ["white American", "Black American"],
     "eua": True,
     "coz": "a Brooklyn apartment kitchen with a painted tin ceiling, a fire escape outside the window and open shelves of mismatched mugs above a chipped subway-tiled wall",
     "coz_c": "tin-ceiling Brooklyn kitchen",
     "sup_a": "a scratched stainless counter", "sup": "counter",
     "trajes": [
         ("%s cropped ribbed tank top with denim cut-offs",
          "cropped tank"),
         ("%s tight bodysuit under an open oversized shirt",
          "open shirt"),
         ("%s low-cut fitted crop top and high-waisted shorts",
          "fitted crop top"),
         ("%s thin-strapped mini dress",
          "mini dress"),
         ("%s cut-off tee knotted above the waist with track shorts",
          "knotted tee"),
     ],
     "cores": ["black", "white", "burgundy", "cobalt", "grey", "scarlet"],
     "luz": "Hard afternoon light through the fire-escape window.",
     "luz_c": "fire-escape light",
     "audio": "a subway rumbling, a siren far off"},
    {"id": "louisiana", "selo": "N", "familia": "louisiana",
     "etnias": ["Black American", "white American"],
     "eua": True,
     "coz": "a Louisiana kitchen with bead-board walls in faded green, a ceiling fan turning slowly, a screen door onto a wet yard and cast-iron hanging over a gas range",
     "coz_c": "green bead-board Louisiana kitchen",
     "sup_a": "a worn butcher-block counter", "sup": "counter",
     "trajes": [
         ("%s thin cotton camisole with frayed denim shorts",
          "cotton camisole"),
         ("%s halter top tied at the neck with a short wrap skirt",
          "halter top"),
         ("%s low-cut sundress with the straps off the shoulder",
          "off-shoulder sundress"),
         ("%s cropped tank with cut-off shorts",
          "cropped tank"),
         ("%s sheer blouse knotted at the ribs over a bandeau",
          "knotted blouse"),
     ],
     "cores": ["emerald", "white", "hot pink", "cobalt", "black", "gold"],
     "luz": "Warm damp light through the screen door.",
     "luz_c": "warm bayou light",
     "audio": "cicadas, a ceiling fan, rain on the porch"},
    {"id": "texas", "selo": "N", "familia": "texas",
     "etnias": ["white American", "Mexican American"],
     "eua": True,
     "coz": "a Texas ranch kitchen with cedar beams, a wide window onto dry scrub and fence line, talavera tiles behind a big range and a pine dresser of jars",
     "coz_c": "cedar-beamed Texas kitchen",
     "sup_a": "a thick mesquite counter", "sup": "counter",
     "trajes": [
         ("%s pearl-snap shirt tied at the ribs with denim cut-offs",
          "tied pearl-snap"),
         ("%s cropped tank top and short denim skirt",
          "cropped tank"),
         ("%s low-cut fitted tee with high-waisted shorts",
          "fitted tee"),
         ("%s bandeau top under an open flannel, short shorts",
          "open flannel"),
         ("%s short sundress with a tooled leather belt",
          "short sundress"),
     ],
     "cores": ["denim blue", "white", "scarlet", "black", "turquoise", "cream"],
     "luz": "Hard dry sunlight through the scrub-side window.",
     "luz_c": "hard Texas sun",
     "audio": "wind over dry grass, a distant gate"},
    {"id": "apalache", "selo": "N", "familia": "apalache",
     "etnias": ["white American"],
     "eua": True,
     "coz": "an Appalachian cabin kitchen with finished pine panelling, glass-front cabinets of preserves, cast-iron on a rail and a black enamel range",
     "coz_c": "pine cabin kitchen",
     "sup_a": "a thick oiled butcher-block counter", "sup": "counter",
     "trajes": [
         ("%s cut-off tee knotted at the waist with denim shorts",
          "knotted tee"),
         ("%s thin-strapped tank top and short cut-offs",
          "strappy tank"),
         ("%s open flannel over a low-cut vest top",
          "open flannel"),
         ("%s short button-front dress left open at the collar",
          "short dress"),
         ("%s cropped sweatshirt with running shorts",
          "cropped sweatshirt"),
     ],
     "cores": ["dark red", "denim blue", "forest green", "white", "black", "cream"],
     "luz": "Soft mountain daylight through a small window.",
     "luz_c": "soft mountain light",
     "audio": "birds, wind in the pines, a wood stove"},
    {"id": "miami", "selo": "N", "familia": "miami",
     "etnias": ["Cuban American", "Black American"],
     "eua": True,
     "coz": "a Miami kitchen with white gloss cabinets, a wall of glass onto palms and bright sky, terrazzo underfoot and a row of tall glasses on the counter",
     "coz_c": "white gloss Miami kitchen",
     "sup_a": "a polished quartz counter", "sup": "counter",
     "trajes": [
         ("%s bikini top under an open linen shirt",
          "open linen shirt"),
         ("%s cropped halter and short wrap skirt",
          "cropped halter"),
         ("%s low-cut bodycon mini dress",
          "bodycon mini"),
         ("%s bandeau top with high-cut shorts",
          "bandeau top"),
         ("%s sheer cover-up over a swim top",
          "sheer cover-up"),
     ],
     "cores": ["hot pink", "turquoise", "white", "lime green", "black", "gold"],
     "luz": "Bright hard sun through the glass wall.",
     "luz_c": "bright Miami sun",
     "audio": "palms in the wind, a pool filter"},
    {"id": "california", "selo": "N", "familia": "california",
     "etnias": ["white American", "Mexican American"],
     "eua": True,
     "coz": "a Southern California kitchen with pale open shelving, a sliding door onto a sun-bleached patio, potted succulents and a row of amber jars",
     "coz_c": "sun-bleached California kitchen",
     "sup_a": "a pale concrete counter", "sup": "counter",
     "trajes": [
         ("%s cropped ribbed tank with high-waisted denim shorts",
          "ribbed crop tank"),
         ("%s thin-strapped slip dress",
          "slip dress"),
         ("%s bikini top under an open oversized shirt",
          "open oversized shirt"),
         ("%s low-cut bodysuit with short linen shorts",
          "low-cut bodysuit"),
         ("%s knotted crop tee and cut-offs",
          "knotted crop tee"),
     ],
     "cores": ["white", "black", "dusty rose", "denim blue", "olive", "cream"],
     "luz": "Flat bright coastal daylight.",
     "luz_c": "flat coastal light",
     "audio": "gulls far off, a wind chime"},
    {"id": "jersey", "selo": "N", "familia": "jersey",
     "etnias": ["white American"],
     "eua": True,
     "coz": "a New Jersey kitchen with honey-oak cabinets, a bay window onto a small back yard, a wall clock and a crowded fridge door",
     "coz_c": "honey-oak Jersey kitchen",
     "sup_a": "a speckled laminate counter", "sup": "counter",
     "trajes": [
         ("%s tight low-cut tank top with leggings",
          "low-cut tank"),
         ("%s cropped hoodie with short shorts",
          "cropped hoodie"),
         ("%s fitted mini dress with thin straps",
          "fitted mini"),
         ("%s off-shoulder top and denim cut-offs",
          "off-shoulder top"),
         ("%s sports bra under an open zip-up, short shorts",
          "open zip-up"),
     ],
     "cores": ["black", "hot pink", "white", "navy", "silver", "scarlet"],
     "luz": "Cool grey daylight through the bay window.",
     "luz_c": "cool bay-window light",
     "audio": "a highway hum, a dog next door"},
    {"id": "nashville", "selo": "N", "familia": "nashville",
     "etnias": ["white American"],
     "eua": True,
     "coz": "a Nashville kitchen with shiplap walls, a farmhouse sink under a window onto a green yard, string lights along a shelf and mason jars in a row",
     "coz_c": "shiplap Nashville kitchen",
     "sup_a": "a thick reclaimed-oak counter", "sup": "counter",
     "trajes": [
         ("%s cropped tank top with a short denim skirt",
          "cropped tank"),
         ("%s knotted gingham shirt over cut-offs",
          "knotted gingham"),
         ("%s thin-strapped short sundress with boots",
          "short sundress"),
         ("%s low-cut fitted tee and high-waisted shorts",
          "fitted tee"),
         ("%s bandeau under an open denim shirt",
          "open denim shirt"),
     ],
     "cores": ["denim blue", "white", "scarlet", "black", "cream", "emerald"],
     "luz": "Warm golden light through the sink window.",
     "luz_c": "warm golden light",
     "audio": "a screen door, crickets starting"},
    {"id": "chicago", "selo": "N", "familia": "chicago",
     "etnias": ["Black American", "white American"],
     "eua": True,
     "coz": "a Chicago two-flat kitchen with white-painted cabinets, a radiator under the window, the brick of the next building outside and a heavy enamel stove",
     "coz_c": "white two-flat kitchen",
     "sup_a": "a polished granite counter", "sup": "counter",
     "trajes": [
         ("%s fitted crop top with high-waisted jeans",
          "fitted crop top"),
         ("%s thin-strapped bodysuit under an open shirt",
          "open shirt"),
         ("%s low-cut mini dress",
          "mini dress"),
         ("%s cropped sweater with short shorts",
          "cropped sweater"),
         ("%s tank top knotted at the waist with leggings",
          "knotted tank"),
     ],
     "cores": ["burgundy", "royal blue", "black", "white", "camel", "scarlet"],
     "luz": "Cool north light off the brick.",
     "luz_c": "cool north light",
     "audio": "a radiator ticking, traffic below"},
    {"id": "arizona", "selo": "N", "familia": "arizona",
     "etnias": ["Mexican American", "white American"],
     "eua": True,
     "coz": "an Arizona kitchen with adobe-plastered walls, a deep window onto red rock and cactus, saltillo tile underfoot and clay jars on an open shelf",
     "coz_c": "adobe Arizona kitchen",
     "sup_a": "a smooth concrete counter", "sup": "counter",
     "trajes": [
         ("%s cropped tank top with short denim cut-offs",
          "cropped tank"),
         ("%s low-cut sundress with the straps slipped down",
          "slipped sundress"),
         ("%s bikini top under an open gauze shirt",
          "open gauze shirt"),
         ("%s bandeau and high-waisted shorts",
          "bandeau"),
         ("%s thin-strapped bodysuit with a short wrap skirt",
          "wrap skirt"),
     ],
     "cores": ["turquoise", "white", "black", "scarlet", "denim blue", "cream"],
     "luz": "Hard desert sun through the deep window.",
     "luz_c": "hard desert sun",
     "audio": "wind over dry ground, a distant truck"},
    {"id": "boston", "selo": "N", "familia": "boston",
     "etnias": ["white American"],
     "eua": True,
     "coz": "a Boston triple-decker kitchen with painted wainscot, a window onto a narrow street of brick houses, a kettle on the hob and a plate rail of china",
     "coz_c": "painted triple-decker kitchen",
     "sup_a": "a worn maple counter", "sup": "counter",
     "trajes": [
         ("%s fitted low-cut tank with denim shorts",
          "low-cut tank"),
         ("%s cropped college sweatshirt and short shorts",
          "cropped sweatshirt"),
         ("%s thin-strapped slip dress",
          "slip dress"),
         ("%s open flannel over a bandeau, cut-offs",
          "open flannel"),
         ("%s tight ribbed top with a short skirt",
          "ribbed top"),
     ],
     "cores": ["navy", "white", "brick red", "forest green", "grey", "black"],
     "luz": "Cool overcast light through the street window.",
     "luz_c": "cool street light",
     "audio": "traffic, a church bell far off"},
    {"id": "atlanta", "selo": "N", "familia": "atlanta",
     "etnias": ["Black American"],
     "eua": True,
     "coz": "an Atlanta kitchen with white shaker cabinets and a subway-tiled splashback, a wide window onto a kept garden and labelled jars on floating shelves",
     "coz_c": "white shaker Atlanta kitchen",
     "sup_a": "a honed black granite island", "sup": "island",
     "trajes": [
         ("%s fitted crop top with high-waisted shorts",
          "fitted crop top"),
         ("%s low-cut bodycon mini dress",
          "bodycon mini"),
         ("%s satin cami with short shorts",
          "satin cami"),
         ("%s bandeau under an open cropped jacket",
          "open cropped jacket"),
         ("%s thin-strapped bodysuit and a short wrap skirt",
          "wrap skirt"),
     ],
     "cores": ["dusty rose", "white", "black", "teal", "gold", "wine"],
     "luz": "Bright even daylight through the garden window.",
     "luz_c": "bright garden light",
     "audio": "birds in the garden, a fridge humming"},
    {"id": "meio_oeste", "selo": "N", "familia": "meio_oeste",
     "etnias": ["white American"],
     "eua": True,
     "coz": "a Midwest farmhouse kitchen with painted wainscot and a wide window onto flat corn fields, glass-front cabinets of preserves and a cream enamel range",
     "coz_c": "farmhouse kitchen",
     "sup_a": "a thick maple butcher-block counter", "sup": "counter",
     "trajes": [
         ("%s knotted gingham shirt with denim cut-offs",
          "knotted gingham"),
         ("%s cropped tank top and short shorts",
          "cropped tank"),
         ("%s thin-strapped short sundress",
          "short sundress"),
         ("%s low-cut fitted tee with high-waisted shorts",
          "fitted tee"),
         ("%s open plaid shirt over a vest top, cut-offs",
          "open plaid"),
     ],
     "cores": ["denim blue", "white", "scarlet", "black", "cream", "hunter green"],
     "luz": "Wide flat daylight off the fields.",
     "luz_c": "flat prairie light",
     "audio": "wind over the fields, a screen door"},
    {"id": "detroit", "selo": "N", "familia": "detroit",
     "etnias": ["Black American", "white American"],
     "eua": True,
     "coz": "a Detroit kitchen with dark-painted cabinets, a window onto a wide quiet street of clapboard houses, a heavy old range and a row of glass jars",
     "coz_c": "dark-painted Detroit kitchen",
     "sup_a": "a scratched steel counter", "sup": "counter",
     "trajes": [
         ("%s fitted crop top with track shorts",
          "fitted crop top"),
         ("%s low-cut bodysuit under an open shirt",
          "open shirt"),
         ("%s cropped hoodie and short shorts",
          "cropped hoodie"),
         ("%s thin-strapped mini dress",
          "mini dress"),
         ("%s tank knotted at the ribs with high-waisted jeans",
          "knotted tank"),
     ],
     "cores": ["black", "burgundy", "royal blue", "silver", "white", "olive"],
     "luz": "Flat grey daylight through the street window.",
     "luz_c": "flat street light",
     "audio": "a car passing, wind through a screen"},
    {"id": "nova_inglaterra", "selo": "N", "familia": "nova_inglaterra",
     "etnias": ["white American"],
     "eua": True,
     "coz": "a New England coastal kitchen with white-painted panelling and a window onto grey water and rigging, glass-front cabinets and a cream enamel range",
     "coz_c": "white-panelled coastal kitchen",
     "sup_a": "a honed slate counter", "sup": "counter",
     "trajes": [
         ("%s cropped striped top with denim cut-offs",
          "cropped striped top"),
         ("%s thin-strapped slip dress",
          "slip dress"),
         ("%s bikini top under an open oversized shirt",
          "open oversized shirt"),
         ("%s low-cut fitted tank with short shorts",
          "fitted tank"),
         ("%s knotted tee over a bandeau, cut-offs",
          "knotted tee"),
     ],
     "cores": ["navy", "white", "seafoam", "brick red", "black", "coral"],
     "luz": "Cool bright light off the water.",
     "luz_c": "cool sea light",
     "audio": "gulls and rigging outside"},
    {"id": "vegas", "selo": "N", "familia": "vegas",
     "etnias": ["white American", "Mexican American"],
     "eua": True,
     "coz": "a Las Vegas apartment kitchen with glossy dark cabinets, a sliding door onto a balcony over low desert rooftops and a row of tall glasses",
     "coz_c": "glossy Vegas kitchen",
     "sup_a": "a black quartz counter", "sup": "counter",
     "trajes": [
         ("%s tight low-cut bodycon mini dress",
          "bodycon mini"),
         ("%s bikini top with short satin shorts",
          "bikini top"),
         ("%s cropped halter and a short skirt",
          "cropped halter"),
         ("%s sheer robe over a bandeau and shorts",
          "sheer robe"),
         ("%s thin-strapped bodysuit with high-cut shorts",
          "bodysuit"),
     ],
     "cores": ["black", "gold", "hot pink", "silver", "scarlet", "white"],
     "luz": "Hard desert light through the balcony door.",
     "luz_c": "hard balcony light",
     "audio": "distant traffic, an air-conditioner"},
]

FAMILIAS_MUNDO = list(dict.fromkeys(m["familia"] for m in MUNDOS))


# ---------------------------------------------------------------------------
# ⭐ METODOS — O PREPARO, E ELE NAO E' FIXO
# ---------------------------------------------------------------------------
# ⛔⛔ ORDEM DO OPERADOR, 2026-08-04: *"nao fixe liquidificador = vai engessar o
# repertorio visual do take e tornar os videos muito parecidos entre si e
# repetitivos"*.
# A fonte usa liquidificador; aqui ele e' UMA entrada de doze. O `acao` e' o
# verbo que o TAKE anima, e ele acompanha o utensilio — sem isso o bloco manda
# "she blends" com um pilao na mao.
# ⚠️ `vaso_curto` existe para a pegada anti-F12b: punho inteiro em volta do
# recipiente. O Veo solta objeto que a mao "segura" sem estar descrito.
METODOS = [
    {"id": "liquidificador", "selo": "V",
     "vaso": "a glass blender jug on its base",
     "curto": "the blender jug",
     "acao": "tips the last of it in and sets the lid on",
     "fala": "Blend it"},
    {"id": "pilao", "selo": "N",
     "vaso": "a heavy stone mortar with the pestle standing in it",
     "curto": "the stone mortar",
     "acao": "works the pestle round in slow circles",
     "fala": "Grind it down"},
    {"id": "jarra_colher", "selo": "N",
     "vaso": "a tall glass jug with a long wooden spoon in it",
     "curto": "the glass jug",
     "acao": "turns the long spoon through it twice",
     "fala": "Stir it through"},
    {"id": "tigela_fouet", "selo": "N",
     "vaso": "a wide ceramic bowl with a wire whisk resting in it",
     "curto": "the ceramic bowl",
     "acao": "beats it with the whisk in short strokes",
     "fala": "Whisk it together"},
    {"id": "garrafa", "selo": "N",
     "vaso": "a capped glass bottle half full",
     "curto": "the glass bottle",
     "acao": "caps it and shakes it twice",
     "fala": "Shake it hard"},
    {"id": "bule_infusor", "selo": "N",
     "vaso": "a clear glass teapot with a metal infuser basket sitting in the top",
     "curto": "the glass teapot",
     "acao": "presses the infuser basket down into it",
     "fala": "Steep it"},
    {"id": "moedor", "selo": "N",
     "vaso": "a hand-crank grinder clamped to the edge of the surface",
     "curto": "the grinder",
     "acao": "turns the crank steadily",
     "fala": "Grind it fine"},
    {"id": "coador_pano", "selo": "N",
     "vaso": "a wide jar with a square of cloth tied over its mouth",
     "curto": "the cloth-covered jar",
     "acao": "presses the mixture through the cloth with the back of a spoon",
     "fala": "Strain it"},
    {"id": "panela_esmalte", "selo": "N",
     "vaso": "a small enamel pan on a low flame",
     "curto": "the enamel pan",
     "acao": "folds it through with a wooden spoon",
     "fala": "Warm it through"},
    {"id": "almofariz_madeira", "selo": "N",
     "vaso": "a deep wooden mortar with a long pestle",
     "curto": "the wooden mortar",
     "acao": "pounds it down with the long pestle",
     "fala": "Pound it"},
    {"id": "prensa_frances", "selo": "N",
     "vaso": "a glass press pot with the plunger raised",
     "curto": "the press pot",
     "acao": "pushes the plunger slowly down through it",
     "fala": "Press it down"},
    {"id": "peneira_tigela", "selo": "N",
     "vaso": "a fine metal sieve resting over a glass bowl",
     "curto": "the metal sieve",
     "acao": "taps the sieve so it falls through into the bowl",
     "fala": "Sift it in"},
]


# ---------------------------------------------------------------------------
# ⭐⭐ RAROS — OS INGREDIENTES QUE O OPERADOR MANDOU ENTRAR
# ---------------------------------------------------------------------------
# ⛔ ORDEM DO OPERADOR, 2026-08-04, com a diretiva de incorporacao inteira:
#
#     [NOME POPULAR] + [APOSTO CONTEXTUAL DISTINTIVO E SUCINTO]
#
# O aposto existe para que quem NUNCA ouviu falar do ingrediente entenda na hora
# O QUE E', DE ONDE VEM ou POR QUE E' RECONHECIVEL.
#
# ⛔ O QUE O APOSTO NAO PODE SER: descricao visual generica da planta. *"aquela
# raiz redondinha"*, *"aquelas sementes amarelas"* nao identificam nada — varias
# plantas compartilham isso. O aposto e' ORIGEM, TRADICAO, NOME POPULAR
# ALTERNATIVO ou caracteristica botanica realmente distintiva.
#
# ⛔ ZERO NOME CIENTIFICO NA FALA. O binomio vive no campo `interno`, que existe
# so' para producao e NUNCA entra no prompt. Falar `Lepidium meyenii` quebra o
# tom UGC na hora.
#
# ⛔ NAO INVENTAR: origem, propriedade, povo, regiao, historia ou beneficio. Se a
# caracteristica nao for defensavel, a formulacao fica mais neutra. Cada aposto
# abaixo e' factualmente sustentavel.
#
# ⚠️ REGRA DE ECONOMIA: 3 a 10 palavras. E de NATURALIDADE: as construcoes VARIAM
# — `that root...`, `a traditional herb...`, `the famous...`, `the leaf off
# that...`, `known for generations...`. Nao pode parecer doze copias da mesma
# formula gramatical, que e' o que o operador pediu explicitamente.
RAROS = [
    {"id": "maca", "nome": "maca root", "interno": "Lepidium meyenii",
     "aposto": "that Andean root from Peru",
     "img": "a small dish of pale yellow maca powder"},
    {"id": "tongkat", "nome": "tongkat ali", "interno": "Eurycoma longifolia",
     "aposto": "a root from the forests of Southeast Asia",
     "img": "a small dish of coarse light-brown root shavings"},
    {"id": "tribulus", "nome": "tribulus", "interno": "Tribulus terrestris",
     "aposto": "that spiny fruit that grows along the ground",
     "img": "a small dish of dried spiny seed pods"},
    {"id": "epimedium", "nome": "epimedium", "interno": "Epimedium spp.",
     "aposto": "the herb they call horny goat weed",
     "img": "a small dish of dried heart-shaped leaves"},
    {"id": "fenogrego", "nome": "fenugreek", "interno": "Trigonella foenum-graecum",
     "aposto": "the golden seed of the Mediterranean",
     "img": "a small dish of hard golden-brown seeds"},
    {"id": "muirapuama", "nome": "muira puama", "interno": "Ptychopetalum olacoides",
     "aposto": "an Amazon root known for generations",
     "img": "a small dish of chipped pale bark and root"},
    {"id": "ginkgo", "nome": "ginkgo", "interno": "Ginkgo biloba",
     "aposto": "the leaf off that ancient Chinese tree",
     "img": "a small dish of dried fan-shaped leaves"},
    {"id": "mucuna", "nome": "mucuna", "interno": "Mucuna pruriens",
     "aposto": "the famous velvet bean of the tropics",
     "img": "a small dish of dark glossy beans"},
    {"id": "salsaparrilha", "nome": "sarsaparilla", "interno": "Smilax spp.",
     "aposto": "a vine root native to the Americas",
     "img": "a small dish of dried twisted root pieces"},
]

# ⛔ O APOSTO E' OBRIGATORIO E O LINTER COBRA (BO8). Sem ele o ingrediente e' um
# nome aleatorio jogado no roteiro, e o espectador pensa "esse cara comecou a dar
# uma aula de botanica" — que e' o oposto do objetivo.


# ---------------------------------------------------------------------------
# ⭐ COMUNS — o que ja' esta' na cozinha das pessoas
# ---------------------------------------------------------------------------
# ⚠️ CASADOS E COMPLEMENTARES aos raros, nunca excludentes (ordem do operador).
# A receita e' sempre `comum + gelatina + raro`.
COMUNS = [
    {"id": "mel", "nome": "raw honey",
     "img": "an open jar of thick amber honey with a wooden dipper"},
    {"id": "limao", "nome": "half a lemon",
     "img": "a lemon cut in half on a small board"},
    {"id": "bicarbonato", "nome": "baking soda",
     "img": "an unlabelled squat orange tub of white powder"},
    {"id": "canela", "nome": "ground cinnamon",
     "img": "a short unlabelled jar of red-brown powder"},
    {"id": "gengibre", "nome": "fresh ginger",
     "img": "a knob of fresh ginger root grated into a dish"},
    {"id": "curcuma", "nome": "turmeric",
     "img": "an unlabelled jar of deep yellow powder"},
    {"id": "aveia", "nome": "a spoon of oats",
     "img": "a small bowl of rolled oats"},
    {"id": "leite", "nome": "warm milk",
     "img": "a small jug of milk"},
    {"id": "beterraba", "nome": "beet powder",
     "img": "a shallow dish of deep red powder"},
    {"id": "caiena", "nome": "a pinch of cayenne",
     "img": "a tiny unlabelled shaker of bright red powder"},
]


# ---------------------------------------------------------------------------
# ⭐ SUBSTANCIAS — o que ela despeja sobre o prop na cena 1
# ---------------------------------------------------------------------------
# ⚠️ A fonte despeja acafrao em fios vermelhos sobre a banana branca, e o
# CONTRASTE de cor e' metade do bit visual. Todas as entradas caem em fio, po' ou
# grao visivel — liquido transparente nao se ve' cair no scroll.
SUBSTANCIAS = [
    {"id": "acafrao", "selo": "V", "nome": "saffron",
     "dish": "a small glass dish of deep red saffron threads",
     "queda": "a scatter of fine red threads"},
    {"id": "paprica", "selo": "N", "nome": "smoked paprika",
     "dish": "a small glass dish of dark red powder",
     "queda": "a fall of fine dark red powder"},
    {"id": "hibisco", "selo": "N", "nome": "dried hibiscus",
     "dish": "a small glass dish of dried crimson petals",
     "queda": "a scatter of dried crimson petals"},
    {"id": "cravo", "selo": "N", "nome": "whole cloves",
     "dish": "a small glass dish of dark brown cloves",
     "queda": "a scatter of small dark cloves"},
    {"id": "erva_mate", "selo": "N", "nome": "crushed green tea",
     "dish": "a small glass dish of coarse green leaf",
     "queda": "a fall of coarse green leaf"},
    {"id": "semente_abobora", "selo": "N", "nome": "pumpkin seed",
     "dish": "a small glass dish of flat green seeds",
     "queda": "a scatter of flat green seeds"},
    {"id": "canela_pau", "selo": "N", "nome": "crushed cinnamon",
     "dish": "a small glass dish of coarse red-brown bark",
     "queda": "a fall of coarse red-brown bark"},
    {"id": "rosa_mosqueta", "selo": "N", "nome": "crushed rosehip",
     "dish": "a small glass dish of coarse orange-red pieces",
     "queda": "a scatter of coarse orange-red pieces"},
]


# ---------------------------------------------------------------------------
# ⭐ PROPS — reuso do pool VALIDADO PROMPT A PROMPT no COLO (2026-08-03)
# ---------------------------------------------------------------------------
# ⛔ ORDEM DO OPERADOR: *"use o pool"*. Sao CINCO e isso e' de proposito.
#   PASSA  quem quebra a leitura de cilindro — casca dobrada (banana,
#          banana-da-terra), afunilamento conico (cenoura, pastinaca) ou cabo
#          no topo (berinjela)
#   CAI    cilindro de DIAMETRO CONSTANTE terminando em PONTA ROMBA — pepino
#          (2 recusas), abobrinha (1), daikon (1)
# ⛔ Nao completar o pool com entradas nao testadas para "bater o piso": foi
# exatamente esse o erro que o COLO documenta. Pool e' o que passou.
# ⭐⭐ PARES DE PROP — MESMA ESPECIE, ESCALA OPOSTA. Ordem do operador, e a
# razao e' de leitura: com a MESMA especie nos dois lados, so' mudam o
# TAMANHO e o ESTADO, e o espectador fecha a comparacao sem pensar. Especie
# cruzada (banana murcha vs geoduck) faria ele comparar duas coisas.
# ⛔ OS DOIS FICAM NO MESMO QUADRO, um por mulher, erguidos a altura do
# peito — lido na fonte, frame a frame. E' isso que faz o `from this to
# this` resolver: o deitico duplo aponta para dois objetos VISIVEIS.
PARES = [
    # ⭐⭐ O GEODUCK — ordem do operador, 2026-08-05: *"esta faltando prop
    # geoduck no dupla e no outro"*. E' o par de maior semelhanca anatomica do
    # repertorio, e por isso o de maior risco de moderacao.
    # ⛔ DUAS TRAVAS DE FORMA, herdadas do EXTERIOR (regra EX7, paga em recusa):
    #   1. a peca e' o `siphon`, NUNCA `neck`;
    #   2. a especie so' e' nomeada na IMAGE; no TAKE ele e' `the piece`.
    # ⚠️ A escala e' DIFERENCIAL como nos outros pares: o murcho e' curto E
    # recolhido, o gigante e' longo E estendido. Mudar so' o tamanho leria como
    # a mesma peca de perto e de longe.
    {"id": "geoduck", "nome": "clam",
     "murcho": "a small shrivelled geoduck clam, its siphon limp and drawn back against the shell, barely the length of her palm",
     "gigante": "an enormous geoduck clam, its thick siphon extending straight out well past the shell, longer than her forearm, held upright"},
    {"id": "banana", "nome": "banana",
     "murcho": "a small blackened banana, shrivelled and soft, barely the length of her palm",
     "gigante": "an enormous bright yellow banana, longer than her forearm, held upright"},
    {"id": "plantain", "nome": "plantain",
     "murcho": "a small withered plantain gone dark and limp",
     "gigante": "a huge green plantain, thick and straight, held upright in her fist"},
    {"id": "pepino", "nome": "cucumber",
     "murcho": "a shrunken cucumber, wrinkled along its whole length and bent over",
     "gigante": "a giant firm cucumber, straight and thick, held upright"},
    {"id": "cenoura", "nome": "carrot",
     "murcho": "a thin shrivelled carrot, bent and dried out",
     "gigante": "an enormous straight carrot, thick as her wrist, held upright"},
    {"id": "abobrinha", "nome": "zucchini",
     "murcho": "a small soft zucchini, collapsed in the middle",
     "gigante": "a giant firm zucchini, long and straight, held upright"},
    {"id": "berinjela", "nome": "eggplant",
     "murcho": "a small wrinkled eggplant, dull and shrunken",
     "gigante": "a huge glossy purple eggplant, long and firm, held upright"},
    {"id": "mandioca", "nome": "cassava root",
     "murcho": "a short dried cassava root, cracked and shrunken",
     "gigante": "a very long thick cassava root, held upright in her hand"},
    {"id": "nabo", "nome": "parsnip",
     "murcho": "a thin limp parsnip, browned and bent",
     "gigante": "an enormous pale parsnip, thick and straight, held upright"},
    {"id": "milho", "nome": "corn cob",
     "murcho": "a stunted corn cob with shrivelled kernels",
     "gigante": "a giant corn cob, thick and full, held upright"},
    {"id": "pimenta", "nome": "chilli",
     "murcho": "a small dried chilli, blackened and curled",
     "gigante": "an enormous smooth red chilli, long and straight, held upright"},
]
PROPS = PARES   # o contrato do painel usa `PROPS`


# ---------------------------------------------------------------------------
# ⭐ REFS — a boticaria
# ---------------------------------------------------------------------------
# ⛔⛔ LEI DO REF — ela e' sempre bonita. Ordem permanente do operador, ja' dada
# em tres agentes (CLEAN, COLO, RESSURREICAO) e reafirmada no ESCANDALO em
# 2026-08-04: *"mulheres sempre super fit e lindas"*.
# ⚠️ DECISAO DECLARADA: a fonte e' uma mulher de ~40 de oculos, e a autoridade
# dela vem de PARECER curandeira. Eu escolhi a lei do operador sobre a fonte — a
# tradicao entra pelo TRAJE do mundo, nao pelo desgaste do rosto. E' uma linha
# para inverter se ele discordar.
# ⛔ Zero oculos, zero grisalho, zero pele castigada. A ancora facial e' SINAL DE
# BELEZA, nunca deterioracao.
# ⛔ Zero adjetivo de etnia nas entradas: quem injeta e' a montagem, a partir do
# MUNDO. Mesmo contrato do COLO, NECROSE e EXTERIOR.
# ⭐⭐ REFS ESTILO TOP MODEL — ordem do operador, 2026-08-05: *"alimente
# mais o pool de roupas e personagens (lembre-se, mulheres lindas, estilo
# top model)"* e *"quero ruivas lindas tb"*.
# ⚠️ 30 entradas, CINCO ruivas de tons diferentes (auburn, copper, ginger,
# dark red, mahogany) — ruiva nao e' uma cor so', e repetir "red hair" em
# cinco entradas devolveria a mesma mulher cinco vezes.
# ⛔ Cada uma varia CORPO, CABECA e MARCA juntos. Duas mulheres de cabelo
# diferente e mesmo porte leem como a mesma pessoa — foi essa a licao que
# criou o `medir_personagens.py`.
REFS = [
    {"idade": 24, "corpo": "tall and long-legged with a very small waist",
     "cabeca": "deep auburn hair falling in loose waves past her shoulders",
     "marca": "a light spray of freckles across her nose and green eyes"},
    {"idade": 27, "corpo": "slim with an hourglass figure and long legs",
     "cabeca": "copper-red hair in a high glossy ponytail",
     "marca": "pale green eyes and a small beauty mark above her lip"},
    {"idade": 23, "corpo": "willowy and fine-boned with a flat stomach",
     "cabeca": "bright ginger hair cut in long layers",
     "marca": "heavy freckling across her cheeks and hazel eyes"},
    {"idade": 29, "corpo": "curvy with a narrow waist and full shoulders",
     "cabeca": "dark red hair swept over one shoulder",
     "marca": "a small gold hoop in her left nostril and clear skin"},
    {"idade": 26, "corpo": "tall and statuesque with a long waist",
     "cabeca": "strawberry-blonde hair in a loose braid",
     "marca": "wide-set blue eyes and a faint scar through one eyebrow"},
    {"idade": 25, "corpo": "slim and toned with a dancer's line",
     "cabeca": "jet-black hair in a sleek centre part",
     "marca": "sharp cheekbones and a small mole on her jaw"},
    {"idade": 28, "corpo": "long-legged and slender with square shoulders",
     "cabeca": "platinum blonde hair in a blunt shoulder-length cut",
     "marca": "ice-blue eyes and a dimple in one cheek"},
    {"idade": 24, "corpo": "curvy and athletic with a small waist",
     "cabeca": "tight dark curls gathered high on her head",
     "marca": "glowing deep brown skin and a wide bright smile"},
    {"idade": 30, "corpo": "tall and slim with an hourglass line",
     "cabeca": "chestnut hair in long beachy waves",
     "marca": "a gap between her front teeth and warm brown eyes"},
    {"idade": 22, "corpo": "petite and curvy with a defined waist",
     "cabeca": "honey-blonde hair in a high messy bun",
     "marca": "a scatter of freckles and full lips"},
    {"idade": 27, "corpo": "lean and toned with a flat stomach and long arms",
     "cabeca": "long jet-black hair worn straight to the waist",
     "marca": "almond eyes and a small stud in one nostril"},
    {"idade": 26, "corpo": "shapely with toned arms and a narrow waist",
     "cabeca": "caramel balayage falling past her shoulders",
     "marca": "a beauty mark at the corner of her right eye"},
    {"idade": 23, "corpo": "slim-hipped and elegant with a long neck",
     "cabeca": "sandy blonde hair in a fishtail braid",
     "marca": "a slight overbite that shows when she smiles"},
    {"idade": 31, "corpo": "curvy and strong with a small waist",
     "cabeca": "long box braids gathered over one shoulder",
     "marca": "high round cheekbones and a gold nose ring"},
    {"idade": 25, "corpo": "tall and lean with swimmer's shoulders",
     "cabeca": "auburn hair in a low glossy ponytail",
     "marca": "dark freckles across both cheeks and grey eyes"},
    {"idade": 28, "corpo": "softly curvy with a full figure and a narrow waist",
     "cabeca": "dark brown hair in heavy waves with a deep side part",
     "marca": "a small raised birthmark on her temple"},
    {"idade": 24, "corpo": "slim and supple with a very straight back",
     "cabeca": "copper hair cropped into a long bob",
     "marca": "pale skin, freckles and bright green eyes"},
    {"idade": 29, "corpo": "long-limbed and shapely with a defined waist",
     "cabeca": "black hair in a high sleek ponytail",
     "marca": "a thin scar along her jawline and full brows"},
    {"idade": 26, "corpo": "trim and athletic with a flat stomach",
     "cabeca": "golden blonde hair in loose waves",
     "marca": "a small dimple in one cheek only"},
    {"idade": 22, "corpo": "tall and willowy with narrow hips",
     "cabeca": "dark auburn hair in a half-up twist",
     "marca": "wide hazel eyes and a light dusting of freckles"},
    {"idade": 30, "corpo": "curvy with a small waist and long legs",
     "cabeca": "tight coils cropped close to the head",
     "marca": "sculpted cheekbones and a small gold stud"},
    {"idade": 27, "corpo": "slim with a long waist and square shoulders",
     "cabeca": "ash-brown hair in a sleek low bun",
     "marca": "grey-green eyes and a faint mark between her brows"},
    {"idade": 25, "corpo": "shapely and toned with a narrow waist",
     "cabeca": "ginger hair in loose curls past her shoulders",
     "marca": "heavy freckling and a small chin dimple"},
    {"idade": 28, "corpo": "tall and slim with a graceful neck",
     "cabeca": "long dark hair in a high crown braid",
     "marca": "a beauty mark high on her left cheek"},
    {"idade": 23, "corpo": "petite and shapely with a defined waist",
     "cabeca": "bleached blonde hair in a blunt chin-length bob",
     "marca": "wide dark eyes and a faint scar on her chin"},
    {"idade": 31, "corpo": "athletic and curvy with strong shoulders",
     "cabeca": "long waves in a rich mahogany red",
     "marca": "clear skin and a small hoop in her right nostril"},
    {"idade": 24, "corpo": "long-legged and lean with a flat stomach",
     "cabeca": "dark brown hair in a slicked-back ponytail",
     "marca": "sharp brows and a small mole under one eye"},
    {"idade": 26, "corpo": "curvy and confident with a very narrow waist",
     "cabeca": "honey-red hair falling in soft waves",
     "marca": "a dense spray of freckles across her nose"},
    {"idade": 29, "corpo": "slim and elegant with long arms",
     "cabeca": "black hair in a smooth shoulder-length cut",
     "marca": "a thin white streak at her temple and dark eyes"},
    {"idade": 25, "corpo": "tall with a small waist and full shoulders",
     "cabeca": "strawberry-blonde hair in a high loose bun",
     "marca": "green eyes and a small beauty spot on her cheekbone"},
]


# ---------------------------------------------------------------------------
# ⭐⭐ HOMENS — o espantado MUDO da cena 3
# ---------------------------------------------------------------------------
# ⛔ Ordem do operador: *"no take final, alem do ref falando, havera um homem
# sempre atras, com cara de espanto e surpresa e olhando para o objeto na mao do
# ref"*. E, perguntado se ele fala: *"Mudo"*.
# ⚠️ A etnia dele vem do MUNDO, igual a' dela — congruencia de casal no mesmo
# quadro (mesma regra do COLO).
# ⚠️ Ele existe para encenar o espanto NO LUGAR do espectador, que e' a mecanica
# da plateia congelada do ESCANDALO. Por isso ele olha o COPO, nunca a lente.
HOMENS = [
    {"id": "grisalho_barbudo", "idade": 58,
     "marca": "a heavy-set build, thick silver hair and a short grey beard, "
              "weathered skin and a pale scar through one eyebrow",
     "roupa": "a plain navy work shirt"},
    {"id": "careca_bigode", "idade": 63,
     "marca": "a stocky build, a bald crown with white hair at the sides and a "
              "thick moustache, ruddy skin and a large mole on his cheek",
     "roupa": "a heather-grey pocket tee"},
    {"id": "cabelo_farto", "idade": 46,
     "marca": "a tall lean frame, a full head of dark hair going grey at the "
              "temples, clean-shaven, with a deep cleft in his chin",
     "roupa": "an olive canvas shirt with the sleeves rolled"},
    {"id": "sardas_ruivo", "idade": 41,
     "marca": "a wiry build, coppery hair and heavy freckling across the nose, "
              "with a gap between his front teeth",
     "roupa": "a faded red flannel shirt"},
    {"id": "fade_grisalho", "idade": 55,
     "marca": "a broad-shouldered build, a close grey fade and a neat chinstrap "
              "beard, smooth skin and a small gold stud in one ear",
     "roupa": "a slate-blue polo shirt"},
    {"id": "locs_oculos", "idade": 49,
     "marca": "a solid build, salt-and-pepper locs gathered back, wire-rimmed "
              "glasses and a raised mole beside his right eye",
     "roupa": "a charcoal henley with the sleeves pushed up"},
    {"id": "corte_militar", "idade": 52,
     "marca": "a thickset build, an iron-grey brush cut, sun-weathered skin and "
              "a broad nose broken once",
     "roupa": "a mustard snap-button shirt"},
    {"id": "cavanhaque", "idade": 60,
     "marca": "a barrel-chested build, a shaved head and a neat white goatee, "
              "with a white streak in one eyebrow",
     "roupa": "a cream short-sleeve camp shirt"},
    {"id": "onda_longa", "idade": 44,
     "marca": "a slim build, wavy dark hair worn a little long at the collar, "
              "clean-shaven, with a deep dimple in his left cheek",
     "roupa": "a forest-green work shirt"},
    {"id": "sobrancelha_oculos", "idade": 66,
     "marca": "a gaunt frame, white hair combed back, heavy black-framed "
              "glasses and deeply lined skin",
     "roupa": "a blue-and-white checked shirt"},
    {"id": "queixo_fendido", "idade": 47,
     "marca": "a compact build, sandy hair going grey at the sides, tanned skin "
              "and a strong cleft chin",
     "roupa": "a rust-red pocket tee"},
    {"id": "afro_curto", "idade": 54,
     "marca": "a burly build, a short grey afro and a broad open face, with a "
              "small birthmark high on one cheek",
     "roupa": "a sand-coloured linen shirt"},
    # + 2026-08-05, mesma ordem do operador. Porte, cabeca e pelo facial variam
    # juntos: dois homens de cabelo diferente e mesmo porte leem como o mesmo.
    {"id": "bigode_farto", "idade": 57,
     "marca": "a lean upright frame, dark hair combed to one side and a thick "
              "moustache, with deep laugh lines around the eyes",
     "roupa": "a striped short-sleeve shirt"},
    {"id": "calvo_barba", "idade": 51,
     "marca": "a heavy build, a shaved head and a full salt-and-pepper beard, "
              "with a broad flat nose",
     "roupa": "a denim work shirt"},
    {"id": "branco_liso", "idade": 62,
     "marca": "a narrow build, straight white hair falling over the forehead, "
              "hollow cheeks and a cleft chin",
     "roupa": "a pale blue oxford shirt"},
    {"id": "locs_curtas", "idade": 45,
     "marca": "a stocky athletic build, short twisted locs and a trimmed "
              "goatee, with a small scar on his temple",
     "roupa": "a burgundy polo shirt"},
    {"id": "sobrancelha_farta", "idade": 59,
     "marca": "a solid build, thinning grey hair and very heavy dark eyebrows, "
              "with a bulbous nose",
     "roupa": "a khaki utility shirt"},
    {"id": "queimado_sol", "idade": 48,
     "marca": "a rangy build, sun-bleached brown hair and a deep tan line "
              "across the forehead, with a squint at the corners of both eyes",
     "roupa": "a faded teal work shirt"},
    {"id": "cavanhaque_branco", "idade": 65,
     "marca": "a spare frame, close-cropped white hair and a white goatee, "
              "with prominent ears",
     "roupa": "a grey chambray shirt"},
    {"id": "cacheado_grisalho", "idade": 43,
     "marca": "a broad build, dense curly hair going grey at the temples and a "
              "strong square jaw, with a chipped front tooth",
     "roupa": "a black crew-neck tee"},
    {"id": "bochechudo", "idade": 56,
     "marca": "a round-faced heavy build, dark hair receding at the temples "
              "and full cheeks, with a dimpled chin",
     "roupa": "a plaid flannel shirt"},
    {"id": "magro_alto", "idade": 50,
     "marca": "a very tall gaunt frame, iron-grey hair cropped short and a "
              "long straight nose, with deep-set eyes",
     "roupa": "a white undershirt beneath an open work shirt"},
]


# ---------------------------------------------------------------------------
# COPY — cena 1: A ISCA + O VILAO
# ---------------------------------------------------------------------------
# ⭐ ESTRUTURA DA FONTE, literal:
#     "Did you know that if you add saffron to banana, this happens?
#      Pharmacies don't want you to know this."
#
# ⛔⛔ §21 APLICADA DESDE O NASCIMENTO: a PRIMEIRA sentenca NOMEIA os dois objetos
# em cena (a substancia e o prop). Nenhuma abertura deste motor deixa o
# espectador perguntando "do que ela esta' falando?". Cobrado pela BO9.
# ⛔⛔⛔ REESCRITO EM 2026-08-04 — A CENA 1 PARA DE FALAR DO VEGETAL.
#
# O operador leu o TAKE 01 renderizado:
#
#     "Nobody told you what crushed cinnamon does to an eggplant, did they?"
#     -> "Erro grave: fala APENAS do vegetal. Deveria dizer: «My husband's
#         John-son was dead for years till I discovered this golden seed of the
#         Mediterranean secret ingredient»"
#
# ⛔ O DEFEITO: o espectador via uma mulher despejando canela numa berinjela e
# ouvia falar sobre UMA BERINJELA. Nao havia homem, nao havia orgao, nao havia
# problema — ele concluia que o video era de culinaria e rolava. O prop e' um
# PROXY do orgao, e sem a copy fazendo a ligacao ele nao e' metafora, e' legume.
#
# ⚠️⚠️ E O QUE ISSO EXPOS SOBRE A MINHA LENTE: eu tinha construido a BO9 para
# exigir que a abertura "nomeasse o referente", e DEFINI referente como o prop e
# a substancia — ou seja, *o que aparece no quadro*. A lente rodou verde e a copy
# estava errada. Medi "a abertura nomeia o que APARECE?" quando a regra e' "a
# abertura nomeia o que esta' EM JOGO?". O que esta' no quadro sao adereços; o
# que esta' em jogo e' o orgao do marido dela. (licoes §22)
#
# ⭐ AS CINCO PARTES, todas obrigatorias, na ordem que o operador ditou:
#     1. QUEM ................ `my husband` / `my man` — pessoalidade
#     2. O ORGAO ............. `{o}`
#     3. O PROBLEMA COM DURACAO  `was dead for years`
#     4. A VIRADA ............ `till I found`
#     5. O RARO COM O APOSTO . enquadrado como SEGREDO, nao como revelacao
#
# ⚠️ O RARO APARECE NAS DUAS CENAS, e o operador autorizou: *"no take um refere-se
# com aposto mecanismo unico secreto (hook-bullet de curiosidade / exclusividade
# / misterio) e NAO revelacao"*. Por isso o APOSTO e' pago AQUI, na cena 1, onde
# ele e' curiosidade; a cena 2 nomeia o raro sem repeti-lo — repetir custaria ~8
# palavras num video de 24 segundos.
#
# ⛔ O PROP GIGANTE CONTINUA NO QUADRO (ordem do operador), agora como metafora
# MUDA: a imagem carrega o proxy, a fala carrega o que esta' em jogo.
# ⛔⛔ REESTRUTURADO EM 2026-08-05 — A CENA 1 VIROU TRES BEATS COMPOSTOS.
# O operador comparou o que o agente gerou com o que ele queria:
#
#   gerado: "The chemist kept selling us refills while my husband's weiner
#            stayed dead, until mucuna, the famous velvet bean of the tropics
#            and a gelatin trick."
#   ele:    "My husband's weiner stayed dead, things changed when i discovered
#            mucuna, the famous velvet bean of the tropics and a secret gelatin
#            trick."
#
# ⭐ TRES DIFERENCAS, e nenhuma e' de comprimento:
#   1. O PROBLEMA ABRE. O vilao ocupava a abertura e empurrava o problema para
#      o meio — e a abertura pertence ao que esta' em jogo.
#   2. `until {r}` NAO TEM VERBO. "until mucuna, the famous velvet bean" promete
#      uma virada e entrega um substantivo: a frase fica truncada. A virada
#      precisa de verbo — "Things changed when I discovered".
#   3. `secret` entra como ADJETIVO do mecanismo (`a secret gelatin trick`).
#      ⚠️ De proposito DIFERENTE da cena 2, que usa `and a secret: the gelatin
#      trick` — a mesma construcao duas vezes em 24 segundos vira bordao.
#
# ⛔ O VILAO SAIU DO ESCOPO DA CENA 1, por ordem expressa dele. Consequencia
# registrada: a farmacia so' existia nessas iscas, entao ela sai do video
# inteiro. A lente BO3 foi aposentada junto — regra que cobra o que o operador
# mandou tirar e' regra que reprova a producao.
#
# ⛔⛔ E O INGLES DO EXEMPLO DELE NAO FOI COPIADO — ordem dele: *"tomar cuidado
# com o efeito maritaca seu: minha coesao de escrita do ingles no exemplo ta'
# errada, ajustar isso"*. A frase dele e' comma splice com `i` minusculo
# ("stayed dead, things changed when i discovered"). Aqui o problema fecha em
# PONTO, a virada abre em maiuscula, e o aposto do raro leva virgula dos DOIS
# lados, como manda a gramatica. O que se copia do exemplo e' a FORMA (§26).
#
# ⭐ POOL COMPOSTA, nao lista chapada: 16 problemas x 12 viradas x 6 fechos =
# 1152 aberturas distintas antes de multiplicar pelos 9 raros. O operador pediu
# "um pool rico com variacoes do sentido", e variacao de sentido se consegue
# combinando beats, nao repetindo a mesma frase com sinonimos.
# ⛔⛔ ENCURTADAS DE 7-11 PARA 4-6 PALAVRAS EM 2026-08-05 — segunda evidencia
# de corte no mesmo dia. O operador mandou o render:
#   "My husband stopped reaching for me, and his John-son was why. Things
#    changed when I discovered fenugreek, ... and a secret gelatin trick."
# ...e a fala CORTOU em `secret`. A linha tinha 28 palavras — exatamente o
# teto que eu tinha acabado de definir como seguro.
#
# ⭐ A ARITMETICA QUE EU NAO TINHA FEITO: o raro mais longo custa 10 palavras
# (o aposto e' obrigatorio, BO8), a virada mais curta 5 e o fecho mais curto
# 5. Sao 20 palavras COMPROMETIDAS antes de a abertura dizer qualquer coisa.
# Abertura de 11 palavras nao cabia em teto nenhum que respeitasse o relogio.
# ⛔ Ordem dele: *"usar formas de escrever sentencas mais curtas que fala do
# John-son do marido nao funcionar"*. Todas dizem QUEM (`my husband`) e O QUE
# (`{o}`) em 4-6 palavras, que e' o minimo que a BO9 aceita — e a variacao
# mora no VERBO da falha, nao em adornos.
# ⭐⭐ CENA 1, primeiro beat — A CONDICAO. Fiel a fonte: *"If you want your
# smelly and small soldier to go from this..."*.
# ⛔ TODA entrada nomeia o `{o}` na abertura. E' o hook mais direto que existe
# no repo junto com o VARANDA descartado, e e' o que faz o homem parar.
# ⚠️ `smelly` da fonte SAIU: cheiro nao e' o que a VSL vende, e o desejo do
# espectador nao esta' em cheirar melhor. O que fica e' PEQUENO/MURCHO, que e'
# o que o prop da esquerda mostra.
# ⭐⭐ CENA 1, primeiro beat — A CONDICAO. Fiel a fonte: *"If you want your
# smelly and small soldier to go from this..."*.
# ⛔⛔ TODA ENTRADA TERMINA EM `from this`, sem excecao. A primeira versao
# misturava formas ("If you are done with a small {o}") e o segundo deitico
# nao encaixava: saia **"If you are done with a small soldier TO THIS ONE
# RIGHT HERE"** — gramatical no papel, sem sentido na boca. Achado LENDO a
# saida (§19), que e' onde esse tipo de defeito aparece.
# ⚠️ `smelly` da fonte SAIU: cheiro nao e' o que a VSL vende.
# ⭐⭐ CENA 1, primeiro beat — O DIAGNOSTICO, nao a promessa.
# ⛔ ORDEM DO OPERADOR, 2026-08-05, lendo o lote: *"faltou a fala 'if your
# john-son look like this (apontando pro prop murcho) rather than (apontando o
# grande), so this secret trick is for you'. Senao a copy visual das duas
# segurando uma um prop murcho e a outra um duro perde o sentido e a funcao
# pratica."*
#
# ⚠️ E ele esta' apontando um erro de FUNCAO, nao de estilo. A versao anterior
# dizia `If you want your {o} to go FROM THIS TO THIS` — uma TRANSFORMACAO, que
# o espectador assiste de fora. `looks like this RATHER THAN this` e' um
# DIAGNOSTICO: obriga o cara a se reconhecer no prop murcho antes de ouvir a
# oferta. Sem isso os dois props em quadro viram decoracao — a imagem mostra uma
# comparacao que a fala nao usa.
# ⛔⛔ NENHUMA ENTRADA CARREGA CONTRASTE PROPRIO. Sairam tres em 2026-08-05:
#   · `is this one and not the other` — ja' era uma VIRADA, e com a virada
#     sorteada por cima saia *"is this one and not the other instead of the one
#     my friend has"*: dois contrastes na mesma frase, e o fio se perde;
#   · `is the one on the left` e `looks like the one on my side` — posicao de
#     QUADRO, que o espectador nao mapeia. Ele ve' duas mulheres, nao um eixo.
# ⭐ O primeiro deitico fica com quem FALA, porque e' ela que segura o murcho e
# a lente esta' nela. Quem nomeia o outro lado e' a VIRADA.
PROBLEMAS = [
    "If your {o} looks like this one",
    "If your {o} looks more like this one",
    "If this is what your {o} looks like",
    "If your {o} is closer to this one",
    "If your {o} has been looking like this one",
    "If your {o} ended up like this one",
    "If your {o} matches this one here",
    "If your {o} went the way of this one",
    "If your {o} turned into this one",
    "If your {o} has gone the way of this one",
    "If your {o} sits closer to this one",
    "If your {o} is looking like this one lately",
]

# ⭐⭐ CENA 1, segundo beat — O SEGUNDO DEITICO. E' a metade que fecha o `from
# this TO THIS`, e ela e' curta de proposito: quem carrega o significado e' o
# PROP na mao da outra mulher, nao a palavra.
# ⛔ LIDO NA FONTE, e e' por isso que este beat existe separado: os dois props
# ficam NO MESMO QUADRO, um por mulher, erguidos a altura do peito. O deitico
# duplo so' resolve porque a comparacao esta' na tela — texto nenhum
# substituiria isso.
# ⭐⭐ CENA 1, segundo beat — O CONTRASTE EXPLICITO. `rather than` / `and not`
# e' o que fecha o par: sem a conjuncao adversativa os dois deiticos ficam
# soltos e o espectador nao sabe qual dos dois e' ele.
# ⛔ Beat CURTO de proposito: quem carrega o significado e' o PROP na mao da
# outra mulher, erguido a altura do peito (lido na fonte). A palavra so' aponta.
# ⛔⛔ TODA ENTRADA NOMEIA QUEM SEGURA O OUTRO PROP. Ordem do operador,
# 2026-08-05, lendo o render *"If your peck-er has been looking like this one
# and not this one, this secret is for you"*: **"excesso de pronome. A proxy que
# a amiga ao lado esta segurando voce tem que especificar pro telespectador"** —
# e a forma que ele escreveu a mao: *"essa daqui e nao A QUE MINHA AMIGA ESTA
# SEGURANDO"*.
# ⚠️ `this one` DUAS VEZES na mesma frase e' deitico sem referente: os dois
# apontam para lugar nenhum e o espectador nao sabe qual e' qual. O primeiro
# deitico (`this one`) fica com quem fala, porque ela segura o murcho e a lente
# esta' nela; o SEGUNDO tem de dizer que o outro esta' na mao da amiga.
# ⛔ Metade das entradas antigas era `this one` puro. As oito que sobreviveram
# viraram catorze, e todas nomeiam a amiga ou a mao dela.
VIRADAS = [
    "and not the one my friend is holding",
    "rather than the one my friend is holding",
    "and not the one she is holding",
    "rather than the one she is holding",
    "and not the one in her hand",
    "rather than the one in her hand",
    "and not the one my girl is holding",
    "instead of the one my friend has",
    "and not the one she has got there",
    # ⛔ Aqui esteve `rather than the one beside me` — e "beside me" e' quem
    # FALA, nao a amiga. O deitico voltava para o proprio murcho dela.
    "rather than the one she is showing you",
    "and not the one my friend brought",
    "instead of the one in her hand",
    "and not the big one she is holding",
    "rather than the one my friend is showing you",
]

# ⚠️ O fecho vem depois do aposto do raro, entao a virgula ANTES dele mora na
# montagem (`%s, %s`), nunca aqui — senao o aposto fica sem fechar.
# ⭐ CENA 1, fecho — A PROMESSA DE ENTREGA, literal da fonte: *"just follow
# the recipe we're about to show you"*. O operador travou o take 1 ate' aqui.
# ⚠️ `we` no plural, sempre: sao DUAS em quadro, e a fonte diz `we`.
# ⭐ CENA 1, fecho — A QUALIFICACAO. `is for you` fecha o diagnostico: quem se
# reconheceu no prop murcho acabou de ser convocado. Exclui quem nao se
# reconheceu, e exclusao e' o que faz o resto assistir.
# ⛔⛔ TODO FECHO NOMEIA O QUE E' QUE E' PARA ELE. Sairam tres em 2026-08-05
# (`this one is for you`, `then this is for you, brother`, `then keep watching,
# this is for you`): eram um TERCEIRO deitico numa frase que ja' tinha dois, e
# nenhum dizia o que o espectador ganha. *"this one is for you"* logo depois de
# *"this one and not the one she is holding"* faz o `this one` apontar para o
# prop, nao para o truque — a frase promete um vegetal.
FECHOS = [
    "this secret trick is for you",
    "then this gelatin trick is for you",
    "then the gelatin trick is for you",
    "this secret is for you",
    "this trick was made for you",
    "this gelatin trick is for you",
    "then this recipe is for you",
    "this little trick is for you",
]

# ⛔ O VILAO — na fonte e' `Pharmacies don't want you to know this.` O operador
# mandou este beat entrar tambem no RECEITA no mesmo dia; aqui ele e' da fonte.
# ⛔ REGRA DE FUNCAO: toda entrada NOMEIA QUEM esconde ou QUEM lucra. Queixa sem
# dono devolve a culpa para o espectador.
# ⛔⛔ O MODELO DO VILAO TEM TRES PARTES — ordem do operador, 2026-08-04, depois
# de ler "They will sell you a monthly plan before they sell you the truth":
#     *"who will sell what and with what purpose? No lugar deveria ter: the
#      pharmacy industry will sell you pills and not let you know the truth
#      that works"*
#
#     [QUEM] + [o que ele te VENDE] + [o que ele te ESCONDE]
#
# ⛔ PRONOME NAO E' QUEM. `They`, `nobody`, `somebody` nao nomeiam ninguem, e a
# primeira versao deste pool (e da lente que o cobra) aceitava os tres.
# ⛔⛔ POOL APOSENTADO EM 2026-08-05 — NAO E' MAIS SORTEADO POR NINGUEM.
# O operador mandou tirar este beat da cena 1 porque ele era o que estourava o
# teto e cortava a fala. As dez entradas ficam AQUI, e nao apagadas, por dois
# motivos: e' copy curada que pode voltar se a cena 1 ganhar folego, e apagar
# copy aprovada sem registro e' como o repertorio some sem ninguem notar.
# ⚠️ O vilao continua no video — ele desceu para dentro das ISCAS, em seis das
# vinte e duas entradas. A lente BO3 passou a cobrar isso no POOL, e nao no
# sorteio, porque o proprio exemplo que o operador escreveu nao tem vilao.
VILOES_APOSENTADO = [
    "The pharmacy industry sells you pills and keeps the kitchen mix off the label.",
    "No drug company makes a cent off a kitchen shelf.",
    "The chemists keep the two-dollar mix off the shelf; they cannot bill you for it.",
    "The chemists would rather sell you the box behind the counter.",
    "Doctors do not hand the cheap recipe out, and not because it fails.",
    "The drug companies advertise the pill and never the mix that hardens him.",
    "The pill companies need you buying the little blue box instead.",
    "My grandmother knew this recipe. Then the drug industry put a price on it.",
    "The pharmacy sells you a monthly refill and hides the mix that costs pennies.",
    "Every pharmacy ad sells the expensive pill and buries the cheap recipe.",
]


# ---------------------------------------------------------------------------
# COPY — cena 2: O PREPARO (o mecanismo)
# ---------------------------------------------------------------------------
# ⛔⛔ CONGRUENCIA INVIOLAVEL: o mecanismo do criativo e' o que a VSL vende, e a
# nossa vende GELATIN nas paginas. A fonte manda banana + acafrao + mel + limao;
# nos mantemos a FORMA (caseiro, tres ingredientes, um utensilio) e ancoramos no
# `gelatin trick`. O que varia e' o acompanhamento, nunca a ancora.
# ⛔ O literal `gelatin trick` e' obrigatorio nesta cena e o linter trava nele.
#
# ⭐ O SLOT `{r}` E' O INGREDIENTE RARO **COM O APOSTO COLADO** — a montagem
# injeta `nome, aposto`, nunca o nome sozinho (BO8).
# ⚠️ ENCURTADAS EM 2026-08-04 por ARITMETICA, nao por gosto. A cena 2 passou a
# carregar TRES beats — receita + o passo retido + a promessa — e o modelo do
# passo retido e' mais longo que o antigo. Com as receitas anteriores a conta
# dava 42 palavras contra teto de 32. Quem entra por ultimo nao paga a conta
# sozinho: as tres partes encolhem juntas.
# ⛔⛔ O VASO SAIU DA FALA EM 2026-08-05. Toda entrada terminava em `into
# the {v}` e o operador reescreveu o take sem isso.
# ⚠️ A razao e' economia pura: o vaso ESTA' NO QUADRO — a mao dela esta'
# fechada nele, o audio traz o som dele, e a IMAGE o descreve. Dizer em voz
# alta o que a imagem ja' mostra gasta 3 a 4 palavras num take de 8s e nao
# acrescenta nada que o espectador nao esteja vendo.
# ⭐ `{v}` continua no dict do metodo e no prompt de IMAGE. So' saiu da FALA.
# ⛔⛔ A GELATINA SAIU DA LISTA DE INGREDIENTES EM 2026-08-05, e a mudanca e'
# do operador: *"Fresh ginger and epimedium and a secret: the gelatin trick"*.
# ⭐ E' melhor do que estava, por dois motivos que valem registrar:
#   1. ECONOMIA — a receita falada listava `gelatin` e depois a ancora dizia
#      `gelatin trick`. A palavra aparecia duas vezes num take de 8s.
#   2. CURIOSIDADE — listar a gelatina COMO INGREDIENTE e depois chamar o
#      conjunto de `gelatin trick` entrega o mecanismo. Deixando-a fora da
#      lista, o que o espectador VE e' uma receita incompleta e o que falta
#      tem nome. E' a lacuna que o comentario compra — a mesma funcao da
#      opcao `c` de 2026-08-04, agora em 6 palavras em vez de 7 e sem uma
#      sentenca propria.
# ⚠️ `gelatin` continua sendo dito (dentro de `gelatin trick`) e a gelatina
# continua NO QUADRO e no prompt de IMAGE. So' saiu da ENUMERACAO falada.
# ⛔⛔ A GELATINA SAIU DA LISTA DE INGREDIENTES EM 2026-08-05, ordem do
# operador: *"Fresh ginger and epimedium and a secret: the gelatin trick"*.
# ⭐ E' melhor do que estava, por dois motivos:
#   1. ECONOMIA — a receita listava `gelatin` e a ancora repetia `gelatin
#      trick`. A palavra saia duas vezes num take de 8s.
#   2. CURIOSIDADE — listar a gelatina e depois chamar o conjunto de `gelatin
#      trick` ENTREGA o mecanismo. Fora da lista, o espectador ve uma receita
#      incompleta e o que falta tem nome. E' a lacuna que o comentario compra.
# ⚠️ `gelatin` continua sendo dito (dentro de `gelatin trick`) e a gelatina
# continua no QUADRO e no prompt de IMAGE. So' saiu da enumeracao falada.
#
# ⛔⛔ E NENHUMA ENTRADA COMECA COM ADJETIVO — licao paga no primeiro render.
# A primeira versao tinha `Fresh {c} and {r}` e o sorteio devolveu
# **`Fresh fresh ginger and maca root`**, porque `fresh ginger` JA' e' o nome
# do ingrediente no pool COMUNS. Template que qualifica um slot preenchido
# por outro pool duplica quando os dois carregam a mesma palavra — e nenhum
# linter pega isso, porque a frase e' gramatical. Achado LENDO a saida (§19).
# ⭐⭐ CENA 2 — OS DOIS SUCOS, lidos na fonte: ela despeja DOIS JARROS AO MESMO
# TEMPO, beterraba (vermelho) e cenoura (laranja), num copo alto. O despejo
# duplo e' o bit visual desta cena e por isso os DOIS sucos ficam na fala.
# ⛔ Nenhuma entrada se auto-fecha: o beat do raro emenda logo depois.
RECEITAS = [
    "A cup of beetroot juice and a cup of carrot juice",
    "Beetroot juice and carrot juice, one cup each",
    "One cup of beetroot, one cup of carrot",
    "Equal parts beetroot juice and carrot juice",
    "A cup of beet juice with a cup of carrot",
    "Beetroot and carrot juice, a cup of each",
    "One cup beetroot, one cup carrot, in a big glass",
    "Two cups: beetroot juice and carrot juice",
]

# ⛔ A ANCORA. Toda entrada traz o literal `gelatin trick` E nomeia o orgao — as
# duas coisas que o colapso de 52 segundos para 24 ameacava levar embora.
# ⛔⛔ REESCRITO EM 2026-08-04 — O PASSO RETIDO, NAO A REVELACAO.
#
# Ordem do operador, lendo o TAKE 02 renderizado
# ("Into the metal sieve: gelatin, oats, and tongkat ali. That is the gelatin
#  trick, and your weiner feels it first."):
#
#     *"Tome cuidado ao dizer que X E' o gelatin trick: pode matar a
#      curiosidade."*
#
# ⛔ E ele esta' certo pela mecanica do funil: se a cena 2 mostra a receita
# INTEIRA e ainda bate o martelo dizendo que aquilo E' o mecanismo, o espectador
# ja' tem tudo — e nao ha' motivo para comentar. O CTA vende o que a cena 2
# entregou de graca.
#
# ⭐ A FORMA ESCOLHIDA PELO OPERADOR (opcao `c`): FALTA UM PASSO.
#     "There's one step I'm not showing here. That's the gelatin trick."
# A receita fica visivel e verdadeira; o que falta e' um passo, e o passo tem
# nome. A lacuna e' o que o comentario compra.
# ⚠️ O literal `gelatin trick` continua obrigatorio (congruencia com a VSL) — ele
# e' NOMEADO, so' nao e' ENTREGUE. Nomear nao gasta; entregar gasta.
# ⛔⛔ REESCRITO EM 2026-08-05 — A CLAUSULA DE RETENCAO SAIU.
# Ordem do operador lendo o TAKE 02: *"retirar 'There's one step I'm not
# showing here.' esse bullet copy falada nao e' relevante o suficiente pra
# ocupar espaco precioso de tempo"*. Eram 7 palavras num take de 8s.
#
# ⚠️ ISTO REVERTE A OPCAO `c` QUE ELE MESMO ESCOLHEU EM 2026-08-04, e a
# consequencia esta' registrada aqui de proposito: sem o passo retido, a
# cena 2 passa a EQUIPARAR a receita visivel ao mecanismo — que e' o que
# ele tinha alertado (*"pode matar a curiosidade"*). Ele viu os renders e
# decidiu que as 7 palavras custam mais do que a lacuna compra. A lente
# BO15 continua barrando a forma pior (equiparar E emendar o beneficio na
# MESMA sentenca), que e' o caso que entrega tudo de uma vez.
# ⛔⛔ REESCRITO 2026-08-05 — A ANCORA DEIXOU DE SER SENTENCA E VIROU CLAUSULA.
# Forma do operador: *"Fresh ginger and epimedium AND A SECRET: the gelatin
# trick"*. Antes eram duas sentencas (`... into the mortar. That's the gelatin
# trick.`); agora e' uma so'.
# ⭐ E isto RECUPERA a curiosidade que a versao anterior tinha matado. Em
# 2026-08-04 ele mandou tirar `There's one step I'm not showing here` por
# custar 7 palavras, e o que sobrou (`That's the gelatin trick`) EQUIPARAVA a
# receita ao mecanismo — o risco que ele mesmo tinha apontado. `and a secret:`
# custa 3 palavras e faz o mesmo trabalho da retencao: a receita visivel esta'
# incompleta, e o que falta tem nome.
# ⭐ CENA 2, segundo beat — O RARO + O SEGREDO. Na fonte o acafrao aparece em
# FIOS SOLTOS numa tigela ao lado do copo (lido no frame), e ela o chama de "the
# most essential part". Aqui ele e' o pool de RAROS, sempre com o aposto.
# ⛔ `gelatin trick` entra como SEGREDO, nao como ingrediente da lista — a
# lacuna e' o que o comentario compra. Mesma forma do BOTICA.
ANCORAS = [
    "%s. Then a pinch of {r} and a secret gelatin trick",
    "%s. Add a pinch of {r}, plus a secret gelatin trick",
    "%s. In goes a pinch of {r} and a secret gelatin trick",
    "%s. Finish with {r} and a secret gelatin trick",
    "%s. Then {r}, and one secret gelatin trick",
    "%s. Stir in {r} plus a secret gelatin trick",
    "%s. Top it with {r} and a secret gelatin trick",
    "%s. A pinch of {r}, then the secret gelatin trick",
]

# ---------------------------------------------------------------------------
# ⭐⭐ PROMESSAS — o terceiro beat da cena 2, no lugar do bullet de loja
# ---------------------------------------------------------------------------
# ⛔ ORDEM DO OPERADOR, 2026-08-04: *"usar bullet de store, loja nao tem funcao
# pratica: melhor seria bullet de promessa"*. O `ONDE` (`You can buy all of it
# at Walmart`) era fiel a' fonte e nao movia ninguem — saiu do pool inteiro.
#
# ⛔⛔ E A RESSALVA DELE E' A REGRA DESTE POOL: *"«you'll be a new person» apenas
# seria vago pq pode ser nova pessoa por qualquer circunstancia — o que seria
# copy drifting"*. Novo POR QUE? Toda entrada nomeia o ORGAO, ou nomeia o que a
# mulher percebe NELE. Promessa sem referente e' a §20 outra vez.
#
# ⚠️ FALA COM O HOMEM, em 2a pessoa. A narradora e' a esposa e ate' aqui ela
# contava do marido dela; neste beat ela vira para a lente e fala com QUEM
# ASSISTE — que e' homem. `Seu marido sera' outro` conversaria com a esposa
# dele, nao com ele.
# ⚠️ VARIACAO ALTA por ordem explicita: *"capriche nas variacoes de pool
# semantica aqui, nao quero videos repetitivos mesmo sorteando"*. Sao 16, em
# quatro familias semanticas — o corpo dele, a reacao dela, a rotina que volta,
# e o homem que ele era.
# ⛔⛔ TODA ENTRADA CARREGA `{o}` — e o linter cobra dos dois lados (BO15).
# A primeira versao tinha cinco sem: `Mornings go back to what they were`
# (que manhas?), `You get back the version of yourself she fell for` (versao em
# que sentido?), `She stops pretending to be asleep` (de que ela desistiu?).
# Sao exatamente a promessa vaga que o operador descreveu — nova pessoa POR
# QUALQUER CIRCUNSTANCIA. A regra e' simples e verificavel: promessa sem orgao
# nao entra.
# ⭐⭐ O CRITERIO DE CURADORIA, e ele vale para QUALQUER pool deste repo.
# Ordem do operador, 2026-08-04: *"«your wife will notice before you do» >>
# «you'll be a new person». Copys que fazem STACK de varios angulos de apelos
# persuasivos sempre vencem na curadoria de candidatos"*. E, na mensagem
# seguinte, o par que ele nomeia: **PROMESSA + DESEJO OCULTO**.
#
# A linha entrega um RESULTADO e, na mesma respiracao, toca o que o espectador
# quer e nao diz em voz alta. `you'll be a new person` so' promete — e promete
# vago, porque novo pode ser por qualquer circunstancia.
#
# ⛔ AUDITADAS UMA A UMA E QUATRO FORAM TROCADAS por entregarem so' a promessa:
#   `Your {o} remembers what it used to do.`        so' resultado
#   `Your {o} answers the first time again.`        so' resultado
#   `Your {o} makes mornings what they used to be.` so' resultado
#   `You'll stop planning your night around...`     so' alivio, sem ela
#
# ⚠️ E EMPILHAR NAO AFROUXA O REFERENTE: toda entrada continua com `{o}`. A forma
# que ganha e' `your wife will notice your {o} before you do` — os dois angulos
# **e** o objeto. Sem o objeto, e' "notara' o que?" (§20).
#
# O desejo oculto deste funil: ela querer de novo · ela tomar a iniciativa · ele
# parar de ser motivo de pena · nao precisar explicar nada.
# ⭐ CENA 2, fecho — A PROMESSA. Ela amarra de volta nos DOIS PROPS da cena 1
# ("stops looking like the small one", "goes back to the big one"), que e' o
# que so' este angulo pode fazer: o espectador viu os dois no mesmo quadro.
# ⛔ Toda entrada nomeia o ORGAO e traz ELA — reacao dela e' prova, auto-relato
# e' alegacao (criterio de curadoria do operador).
# ⭐ CENA 2, fecho — A PROMESSA. Ela amarra de volta nos DOIS PROPS da cena 1,
# que e' o que so' este angulo pode fazer: o espectador viu os dois no mesmo
# quadro.
# ⛔⛔ TODA ENTRADA TRAZ O ORGAO **E** ELA. A primeira versao tinha seis
# promessas sem `she/her/wife` e a lente BO15 reprovou — com razao, e a regra
# e' criterio de curadoria do operador: `my {o} is harder` e' alegacao do
# proprio homem, `she noticed` e' evidencia. Prova que vem da reacao
# involuntaria de terceiro e' crivel de um jeito que auto-relato nunca e'.
PROMESSAS = [
    "Your wife will see your {o} stop looking like the small one.",
    "Your wife will notice your {o} first.",
    "She will watch your {o} go back to the big one.",
    "She will feel your {o} before she says anything.",
    "Your wife will not believe your {o}.",
    "Your {o} answers again, and she knows it.",
    "She stops pretending, and your {o} is why.",
    "Your {o} wakes before she does.",
    "Your wife will want your {o} again.",
    "Your {o} shows up, and she notices.",
    "She reaches over again, and your {o} is why.",
    "Your wife will talk about your {o} before you do.",
]



# ---------------------------------------------------------------------------
# COPY — cena 3: O COPO + O CTA
# ---------------------------------------------------------------------------
# ⭐ A FONTE: "Drink this every morning to increase blood flow and circulation to
# your wiener naturally. Want to learn another natural trick that could help your
# wiener grow up to 5 inches faster in a week? Comment wiener below and I'll
# personally send it to you. But don't forget to follow me. Otherwise I can't
# find you."
#
# ⛔⛔ O CENTIMETRO SAI. Ordem do operador: *"so' a promessa sem centimetro"*.
# A fonte promete `5 inches faster in a week`; nos ficamos com a promessa. O
# linter varre qualquer medida (BO10).
# ⭐⭐ CENA 3 — O USO + O CORPO-PROVA. A fonte NAO tem esta cena (ela termina
# com a mulher segurando o frasco de suplemento). O homem mudo e espantado e'
# comissao do operador.
# ⛔ A fala NAO descreve o prop nem o homem — quem descreve e' a IMAGE. Dizer em
# voz alta o que o quadro mostra gasta o orcamento de 8s.
USOS = [
    "Drink it every morning and your {o} does the rest",
    "One glass a day and your {o} answers",
    "Drink this daily and your {o} comes back",
    "Every morning, and your {o} stops going quiet",
    "One glass each morning and your {o} holds",
    "Drink it warm and your {o} shows up for her",
    "A glass a day, and your {o} does the talking",
    "Drink it first thing and your {o} follows",
    "One glass every morning and your {o} wakes up",
    "Drink it daily and your {o} stops letting you down",
]

# ⛔⛔ A ESCALADA SAIU DA CENA 3 — decisao MEDIDA, nao estetica.
# Com uso + escalada + keyword + isca + gate a cena batia em 42 palavras contra
# um teto de 31, ou seja 5,3 palavras por segundo: um terco acima do que cabe em
# 8 segundos de narracao. Quatro funcoes nao cabem; tres cabem.
# ⚠️ E a que saiu foi a ESCALADA porque ela e' a unica REDUNDANTE: ela promete
# "tem mais" e a ISCA ja' diz o que chega. Keyword, isca e gate sao lei do repo
# e nao encolhem. Fica registrado para ninguem "reintroduzir a escalada" sem
# saber o que vai sair no lugar.
ISCAS_ENTREGA = [
    "the whole recipe", "the full recipe", "the complete recipe",
    "the exact recipe", "the recipe and the measurements",
    "the recipe and the doses", "the exact measurements",
    "the recipe", "the full routine", "the whole thing written out",
    # + 2026-08-05 — sintagma NOMINAL curto: e' o que o CTA promete no DM.
    # ⚠️ Tres das minhas primeiras entradas aqui (`the exact recipe`, `the
    # complete recipe`, `the recipe and the doses`) JA' EXISTIAM nas linhas
    # acima, e a duplicata passou despercebida porque o bloco antigo tem varias
    # entradas por linha. Duplicata dobra em silencio a chance da linha e ocupa
    # um slot que devia ser repertorio novo — agora ha' trava no autoteste.
    "the full measurements",
    "the written recipe",
    "the exact steps",
    "every step of it",
    "the recipe in full",
    "the missing step",
    "the whole method",
    "the recipe and the timing",
]

GATES = [
    "But you have to follow me, or I cannot reach you.",
    "Follow me first, or I cannot reply to you.",
    "Make sure you are following, or I cannot message you back.",
    "Follow me before you comment, or it never reaches me.",
    "Hit follow first, or my message cannot get to you.",
    "Follow me, or I will not be able to find your comment.",
    "Follow me first, or I cannot reply.",
    "Do not forget to follow, or the app will not let me answer.",
    # + 2026-08-05 — o gate e' o beat que cede espaco quando o teto aperta
    "Follow me first, or your comment will not reach me.",
    "You have to follow me, or I will not find you.",
    "Follow me before you comment, or I cannot send it.",
    "Follow first, otherwise I have no way to answer.",
    "I can only reply if you are following me.",
    "Follow me, or your comment gets lost in the pile.",
    "Follow me first, or the message will not go through.",
    "You must be following me for me to reply.",
    "Follow me, otherwise I cannot get back to you.",
    "Follow first, or I have no way to send it.",
]

# ⛔ As palavras do orgao. Rotacionam DENTRO do video (nunca a mesma duas vezes).
NUCLEO = ["Johnson", "pecker", "wiener", "soldier", "tool"]

# ⚠️ MEDIDOS CONTRA A CAPACIDADE REAL de 8s de narracao (~3,4-4,0 p/s = 27-32
# palavras). ⛔ Teto folgado nao e' seguranca: e' frase morta esperando nascer
# (licoes §5). A cena 2 e' a mais densa por construcao — receita + aposto +
# gelatin trick + orgao.
# ⚠️ RECALIBRADOS EM 2026-08-04, quando o APOSTO mudou de cena. A cena 1 passou a
# carregar quem + orgao + problema + descoberta + o raro com aposto, e a cena 2
# ficou so' com a receita. Medido depois da mudanca: cena 1 subiu para 28-38 e a
# cena 2 caiu para 21-30. Teto e piso seguem o que os pools REALMENTE produzem —
# teto que nenhuma combinacao alcanca e' decorativo, e piso que ninguem atinge
# vira AVISO permanente que se aprende a ignorar (licoes §5).
# ⛔⛔ A CENA 1 CAIU DE 32 PARA 28 EM 2026-08-05, e a evidencia e' um render.
# O operador mandou o TAKE 01 com a fala CORTADA — e ela tinha exatamente 32
# palavras, o teto. Ou seja: 32 (4,0 palavras/s, o TOPO da faixa 3,4-4,0 da
# doutrina) e' agressivo demais na pratica desta narradora. O exemplo que ele
# reescreveu a mao tem 25 palavras (3,1 p/s).
# ⚠️ 28 = 3,5 p/s, a metade conservadora da faixa. O piso cai junto porque a
# cena perdeu um beat inteiro (o vilao).
# ⚠️ cena 2: teto 32 -> 28 e piso 22 -> 15 em 2026-08-05. A receita perdeu o
# vaso e o operador quer a cena CURTA — o exemplo que ele escreveu a mao tem
# 16 palavras. Piso 22 acusaria silencio numa fala que ele mesmo pediu.
# ⛔⛔ CENA 1: 28 -> 25 EM 2026-08-05. SEGUNDA evidencia de corte no mesmo dia.
# Primeiro 32 cortou; baixei para 28 e 28 CORTOU TAMBEM. O numero nao sai de
# calculo, sai de render (licoes §28).
# ⚠️ 25 palavras = 3,1 p/s, que e' a taxa dos exemplos que o operador escreve
# a mao. E 25 e' exatamente o pior caso viavel da cena 1: abertura 5 + virada
# 5 + raro 10 + fecho 5.
# ⛔ A CENA 3 CONTINUA EM 31 E ISSO E' RISCO CONHECIDO — ver o relatorio ao
# operador. Baixa-la exige encurtar o CTA, que e' alcada dele.
# ⛔⛔ TETO 25 — ordem permanente do operador, 2026-08-05: *"sempre meca. Nao
# pode haver cortes de fala."* O numero vem de render, nao de conta: 32
# cortou, 28 cortou. Os exemplos que ele escreve a mao vivem em 16-25
# palavras (2,0-3,1 palavras/s).
# ⚠️ cena 2 cortava em 12,8%. A cadeia ja' reserva ancora e promessa antes da receita.
# ⛔ NAO baixar o [3] junto: medido, ele vai de max 31 para 36 pelo `or pool`.
# ⭐⭐ MODO REF BELA — contrato compartilhado (short_comum), 2026-08-05.
# Ordem do operador: *"toggle de trava pra modo ref mulher bela em todos os ui
# ux pertinentes dos agentes shorts, que, quando ativados, gera refs mulheres
# com essas caracteristicas"* — super model, corpao, pouca roupa.
# ⛔ O pool e o helper moram no `short_comum`: um pool por motor divergiria em
# uma semana, e classificacao divergente e' o fragmento espelhado que a P9 proibe.
MODO_BELA = True

TETO_FALA = {1: 25, 2: 25, 3: 25}
PISO_FALA = {1: 18, 2: 15, 3: 23}


# ---------------------------------------------------------------------------
# TRAVAS E EIXOS DO PAINEL
# ---------------------------------------------------------------------------
# ⚠️ ⛔ NAO declarar "livre" aqui: a barra do `ui_agente` ja' o prepende. Motor que
# declara ganha o botao DUPLICADO — defeito achado lendo o print do .exe em
# 2026-08-04 e corrigido na UI, mas nao ha' motivo para recria-lo no dado.
TRAVAS_UI = [
    ("familia_mundo", "nicho", FAMILIAS_MUNDO),
]

EIXOS_TRAVAVEIS = ["mundo", "etnia", "ref", "homem", "prop", "substancia",
                   "metodo", "comum", "raro", "cor", "traje"]


def etnias_do_mundo(spec):
    """O pool de ETNIA depende do MUNDO em cena — trocar para uma etnia que
    aquele mundo nao comporta e' exatamente a incongruencia que os MUNDOS
    existem para impedir."""
    return list(spec["mundo"]["etnias"])


etnias_do_mundo.recebe_spec = True


def trajes_do_mundo(spec):
    """O pool de TRAJE depende do MUNDO — kurta em cozinha amish e' a mesma
    incongruencia que a etnia errada. A UI lista os nomes curtos."""
    return [x[1] for x in spec["mundo"]["trajes"]]


trajes_do_mundo.recebe_spec = True

# ⛔⛔ TRES EIXOS SAIRAM DAQUI EM 2026-08-05, achados na auditoria da etapa [7]:
# SUBSTANCIA, METODO e COMUM eram sorteados, rotacionados no ledger e desenhados
# no painel — e NAO CHEGAVAM A NENHUM BLOCO. A cena 1 deste angulo e' a
# COMPARACAO de dois props (nao ha' despejo, logo nao ha' substancia), e a cena 2
# e' o DESPEJO DOS DOIS SUCOS (nao ha' utensilio, logo nao ha' metodo).
# ⚠️ Eixo que aparece no painel e nao muda o video e' pior que eixo ausente: o
# operador troca, olha o prompt, ve que nada mudou, e para de confiar no painel.
# ⛔ O `homem` tambem saiu: a cena 3 deste angulo e' das DUAS MULHERES, e o
# corpo-prova masculino do BOTICA foi removido junto.
EIXOS_UI = [
    ("mundo", "A COZINHA", "MUNDOS", "id"),
    ("etnia", "ETNIA", "etnias_do_mundo", None),
    ("ref", "A QUE FALA", "REFS", "cabeca"),
    ("traje", "O TRAJE DELA", "trajes_do_mundo", None),
    ("amiga", "A AMIGA", "REFS", "cabeca"),
    ("prop", "O PAR DE PROPS", "PROPS", "nome"),
    ("preparo", "A BANCADA (conformacao)", "PREPAROS", "id"),
    ("raro", "O RARO", "RAROS", "nome"),
]

CENAS_UI = ["1 · a isca + o vilao", "2 · o preparo", "3 · o copo + CTA"]


# ---------------------------------------------------------------------------
# MAQUINARIA
# ---------------------------------------------------------------------------

def _palavras(s):
    return len(re.sub(r"\{\w+\}", "x", s or "").split())


def _carregar_ledger():
    try:
        with open(LEDGER, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


def _gravar_ledger(led):
    try:
        with open(LEDGER, "w", encoding="utf-8") as f:
            json.dump(led, f, ensure_ascii=False, indent=1)
    except OSError:
        pass


def _fresco(pool, usados, rng, chave):
    livres = [x for x in pool if str(x.get(chave, x)) not in usados] or pool
    return rng.choice(livres)


def _por_id(pool, valor, chave="id"):
    if isinstance(valor, str):
        return next((x for x in pool if x.get(chave) == valor), pool[0])
    return valor


def _artigo(s):
    return "an" if s[:1].lower() in "aeiou" else "a"


def _fresco_traje(pool, usados, rng):
    """Como `_fresco`, mas o pool de trajes e' de TUPLAS `(template, curto)` e
    nao de dicts — `_fresco` chama `.get()` e quebra. A chave de frescor e' o
    nome curto.
    ⚠️ `or pool` aqui e' correto e nao e' o estouro silencioso do teto: quando
    todos ja' sairam, repetir e' a unica saida possivel.
    """
    livres = [x for x in pool if x[1] not in usados] or pool
    return rng.choice(livres)


def _por_traje(mundo, curto):
    """Acha o traje do mundo pelo nome curto (a trava da UI guarda o curto).

    ⚠️ Devolve o primeiro do mundo quando o curto nao pertence a ele — o
    operador pode ter travado um traje e depois trocado de mundo, e travar
    `kurta` num mundo amish nao pode derrubar o sorteio.
    """
    # ⛔⛔ ACEITA TUPLA. A `ui_agente.travas()` devolve o VALOR QUE ESTA' NA TELA,
    # e o valor na tela e' a TUPLA `(template, curto)` — nao o curto. Com esta
    # funcao aceitando so' string, o cadeado do traje APARECIA e nao segurava.
    # ⚠️ Consertei isto no CHA de manha e NAO nos dois irmaos, que foram
    # construidos do mesmo tronco. Correcao aplicada num motor e nao nos irmaos
    # e' o §29 na direcao oposta — e so' apareceu porque o cadeado passou a ser
    # MEDIDO (travar, sortear 30x, conferir), nunca declarado.
    # ⭐ TRAVA EXPLICITA VENCE O MUNDO: os trajes destes motores sao roupa
    # americana de rua, nao traje etnico, e atravessam qualquer mundo.
    if isinstance(curto, (tuple, list)):
        return tuple(curto)
    for x in mundo["trajes"]:
        if x[1] == curto:
            return x
    return mundo["trajes"][0]


# ⭐⭐ O APELO DA REF — ordem do operador, 2026-08-05: *"As mulheres tem que ter
# mais sex appeal tb, quando for dos EUA"*.
# ⛔ E havia uma CONTRADICAO LITERAL no BLOCO 0: ele mandava *"an ordinary
# everyday relatable person with a plain unremarkable face, NOT A MODEL"*. Pedir
# apelo com essa frase no prompt e' dar duas ordens opostas ao gerador, e ele
# resolve pela ultima. A frase saiu dos mundos dos EUA e ficou nos outros.
# ⚠️ O QUE FICA NOS DOIS CASOS: `not a celebrity, not resembling any famous
# person`. Essa nao e' estetica — e' a trava de identidade que impede o gerador
# de devolver o rosto de alguem real.
# ⚠️ E a estetica UGC continua: iPhone cru, grao, luz frontal. O apelo entra na
# PESSOA, nao na producao — modelo em estudio nao converte neste funil.
# ⚠️ REFORCADO EM 2026-08-05: *"pelo amor de Deus, DE mais sex appeal pra
# essas mulheres, estao muito feias e sem shape"*. A primeira versao falava
# so' de rosto e cabelo — e o BLOCO 0 e' `chest up`, entao rosto sozinho nao
# resolve FIGURA. Agora a clausula nomeia o corpo, e o campo `corpo` das 22
# REFS foi reescrito junto: ele dizia `slim and upright`, `lean and
# long-limbed` — descricao atletica e neutra, que o gerador le como magra e
# sem forma.
# ⛔ Continua tasteful de proposito: `figure`, `shapely`, `toned`. Termo
# explicito nao converte melhor e ainda arrisca recusa do gerador, que custa
# lote (ver RUNBOOK-bisseccao-moderacao).
APELO_EUA = [
    "A strikingly attractive everyday woman, well groomed, with clear even skin, softly styled hair and a noticeably good figure, not a celebrity, not resembling any famous person.",
    "A very good-looking everyday woman with glowing skin, light natural make-up and a shapely figure, not a celebrity, not resembling any famous person.",
    "An unusually pretty everyday woman with fine features, healthy glossy hair and a trim shapely body, not a celebrity, not resembling any famous person.",
    "A head-turning everyday woman, carefully groomed, with bright eyes, full lips and a striking figure, not a celebrity, not resembling any famous person.",
    "A notably beautiful everyday woman with high cheekbones, smooth clear skin and a curvy figure, not a celebrity, not resembling any famous person.",
    "A very attractive everyday woman with a toned shapely figure, shining hair and even skin, not a celebrity, not resembling any famous person.",
]

# ⛔ HOJE E' CODIGO MORTO: os 16 mundos deste motor sao todos `eua: True`,
# entao `_apelo` nunca cai aqui (medido). Fica porque um mundo novo sem o
# selo o religa — e no registro ANTIGO ele entregaria `plain unremarkable
# face` num agente cuja REF o operador encomendou top model. Codigo morto
# com a regra errada dentro e' bomba com pino: alguem acrescenta um mundo e
# o vicio volta calado, sem lint, sem autoteste, sem aviso.
APELO_PADRAO = (
    "A strikingly beautiful everyday woman, not a celebrity, not resembling "
    "any famous person.")


def _apelo(spec):
    """A clausula de apresentacao da REF: apelo nos mundos dos EUA, o registro
    relatable nos demais. ⚠️ `.get` e nao `[...]`: mundo sem o selo cai no
    padrao em vez de derrubar o sorteio."""
    if not spec["mundo"].get("eua"):
        return APELO_PADRAO
    return spec["apelo"]


def _traje_de(spec, chave):
    """O traje de UMA das duas mulheres, com o artigo certo.

    ⛔ Existe porque as duas apareciam com a MESMA roupa: eu chamava `_traje`
    duas vezes e o spec so' tinha um traje. Duas mulheres identicas da cintura
    para cima viram uniforme — e o operador leu isso no render.
    """
    cor = spec["cor"]
    return "%s %s" % (_artigo(cor), spec[chave][0] % cor)


def _traje(spec):
    """A roupa SORTEADA do mundo, com o artigo certo.

    ⛔ O artigo NAO mora no template: cores como `off-white`, `indigo` e `olive`
    sairiam `a off-white` — bug pago no CLEAN v2 e achado LENDO o render.
    ⚠️ Ate' 2026-08-05 isto lia `spec["mundo"]["traje"]`, UM traje por mundo, e
    o operador mandou tres prints de tres mundos diferentes com a mesma blusa
    bege. Agora o traje e' um eixo proprio, sorteado entre cinco silhuetas.
    """
    cor = spec["cor"]
    return "%s %s" % (_artigo(cor), spec["traje"][0] % cor)


def _sem_artigo(s):
    for art in ("a ", "an ", "the "):
        if s.startswith(art):
            return s[len(art):]
    return s


def _cap(s):
    return s[0].upper() + s[1:] if s else s


def _cabem(pool, monta, teto):
    """As entradas que cabem no teto. ⛔ DESCARTA-SE A LINHA, NUNCA SE ENCURTA
    (CL15): as linhas foram aprovadas uma a uma, e reescrever menor para caber e'
    trocar copy validada por copy nova sem validacao."""
    return [x for x in pool if _palavras(monta(x)) <= teto] or pool


def _na_faixa(pool, monta, piso, teto):
    """As entradas que caem DENTRO da faixa — piso E teto, nao so' o teto.

    ⛔ O `_cabem` sozinho so' impede a fala de ESTOURAR. Medido neste motor:
    26,7% das cenas 1 saiam ABAIXO do piso, a mais curta com 14 palavras em 8
    segundos — 1,75 palavra por segundo, ou seja metade do take em silencio.
    Teto sem piso troca "fala atropelada" por "ar morto", que e' o mesmo defeito
    do outro lado (licoes §5).
    ⚠️ Degrada em dois passos em vez de estourar: tenta a faixa inteira, depois
    so' o teto, e por fim o pool cru — assim quem aparece e' o LINTER, nunca um
    IndexError.
    """
    dentro = [x for x in pool if piso <= _palavras(monta(x)) <= teto]
    return dentro or _cabem(pool, monta, teto)


def _com_o(pool):
    return [x for x in pool if "{o}" in x]


def raro_falado(raro):
    """⭐ BO8 — o ingrediente raro NUNCA sai sozinho na fala.

    `[NOME POPULAR] + [APOSTO]`, que e' a diretiva inteira do operador em uma
    funcao. ⛔ O `interno` (o binomio cientifico) existe so' para producao e nao
    pode chegar ao prompt: `Lepidium meyenii` na boca quebra o tom UGC na hora.
    """
    return "%s, %s" % (raro["nome"], raro["aposto"])


def _falas(spec, rng, quais=(0, 1, 2)):
    """Monta as falas pedidas a partir dos pools ja' sorteados no spec.

    ⚠️ Uma funcao so' para as tres cenas: o botao `trocar` da UI re-sorteia UMA
    fala, e duas copias desta conta garantem que uma delas envelhece mentindo.

    ⭐ A COTA DO ORGAO E' GARANTIDA NO SORTEIO, nao so' cobrada no linter: a cena
    2 sempre o nomeia (todas as ANCORAS trazem `{o}`) e a cena 3 tambem (todos os
    USOS trazem). Linter que reprova o proprio motor e' aviso, nao defesa.
    """
    o1, o2 = spec["orgaos"]
    f = dict(spec.get("falas_map", {}))

    if 0 in quais:
        # ⭐ O APOSTO E' PAGO AQUI, na cena 1, onde ele e' HOOK DE CURIOSIDADE.
        # ⛔ O prop e a substancia SAIRAM da fala (2026-08-04): a cena 1 falava
        # do vegetal e o espectador achava que era culinaria. Eles continuam no
        # QUADRO como metafora muda — a imagem carrega o proxy, a fala carrega o
        # que esta' em jogo, que e' o orgao do marido dela.
        # ⛔⛔ A CENA 1 E' UMA ISCA SO', DESDE 2026-08-05. Ordem do operador
        # lendo o TAKE 01 renderizado com a fala cortada: *"Retire 'Every
        # pharmacy ad sells the expensive pill and buries the cheap recipe' e
        # use bullets curtos"*.
        # ⚠️ O beat do vilao custava 9 a 14 palavras num take que ja' apertava,
        # e era ele que empurrava a cena para o teto. O vilao NAO sumiu: ele
        # desceu para dentro da isca, em seis das vinte e duas entradas.
        # ⭐ TRES BEATS, sorteados em CADEIA e do mais longo para o mais curto:
        # o FECHO carrega o literal `gelatin trick` (intocavel), a VIRADA e o
        # problema cedem em volta. ⛔ Fallback e' a entrada mais CURTA, nunca
        # `or pool`.
        # ⛔ O RARO NAO ENTRA NA CENA 1. Aqui a cena 1 e' o deitico duplo
        # (`from this to this`) mais a promessa de entrega — o ingrediente so'
        # aparece na panela, na cena 2. Herdado do motor de origem e removido.
        def _c1(pb, vr, fc):
            return "%s %s, %s." % (pb.format(o=o1), vr, fc)

        cv = min(VIRADAS, key=_palavras)
        cf = min(FECHOS, key=_palavras)
        pb = rng.choice(_cabem(PROBLEMAS, lambda x: _c1(x, cv, cf),
                               TETO_FALA[1]))
        vr = rng.choice(_cabem(VIRADAS, lambda x: _c1(pb, x, cf),
                               TETO_FALA[1]))
        fc = rng.choice(_cabem(FECHOS, lambda x: _c1(pb, vr, x),
                               TETO_FALA[1]))
        f[0] = _c1(pb, vr, fc)

    if 1 in quais:
        met, com, raro = spec["metodo"], spec["comum"], spec["raro"]
        # ⚠️ SEM o aposto aqui: ele ja' foi pago na cena 1. Repetir os 5-9
        # palavras do aposto num video de 24 segundos e' pagar duas vezes pela
        # mesma informacao — e a cena 2 e' a mais densa das tres.
        # ⭐ SLOTS PROPRIOS: a receita e' fixa (os dois sucos que estao NO
        # QUADRO) e quem carrega o `{r}` e' a ancora, no beat do acafrao.
        # ⭐ `{r}` traz o raro FALADO (nome + aposto colado), como manda a BO8:
        # `saffron, the red thread they pick by hand`. Nome solto e' termo
        # aleatorio jogado no roteiro.
        # ⛔ SEM APOSTO NESTE ANGULO, e a razao e' a fonte: ela diz apenas "a
        # pinch of saffron", sem explicar o que e'. O aposto e' regra do BOTICA,
        # onde o raro E' o segredo; aqui o segredo e' o `gelatin trick` e o raro
        # e' so' mais um ingrediente do copo. Medido: com aposto a cena 2 ia a
        # 39 palavras contra teto de 25.
        rec_slots = dict(r=raro["nome"])
        # ⚠️ O ESPACO DA PROMESSA E' RESERVADO NA CONTA DESDE O PRIMEIRO SORTEIO.
        # Sem isso a receita e a ancora sao escolhidas contra o teto cheio, a
        # promessa entra por cima e a cena estoura — foi o que aconteceu quando
        # o terceiro beat entrou: 34 a 40 palavras contra teto de 32. Quem
        # escolhe primeiro tem de saber o que ainda vem depois.
        curto_a = min(ANCORAS,
                      key=lambda a: _palavras((a % "").format(**rec_slots)))
        curto_p = min(PROMESSAS, key=_palavras)
        rec = rng.choice(_cabem(
            RECEITAS,
            lambda x: ((curto_a % x).format(**rec_slots)).format(o=o2)
            + " " + curto_p.format(o=o2),
            TETO_FALA[2]))
        anc = rng.choice(_cabem(
            ANCORAS,
            lambda a: _cap(((a % rec).format(**rec_slots)).format(o=o2))
            + " " + curto_p.format(o=o2),
            TETO_FALA[2]))
        # ⛔ `_cap` porque a receita ABRE a sentenca. Ate' 2026-08-05 ela comecava
        # com o literal `Gelatin,` e a maiuscula vinha de graca; com a gelatina
        # fora da lista, o primeiro token passou a ser `{c}` em minuscula e o
        # render saiu **`baking soda, fenugreek and one secret...`**. Achado LENDO
        # a saida, nao pelo linter — frase em minuscula e' gramaticalmente valida.
        meio = _cap(((anc % rec).format(**rec_slots)).format(o=o2))
        # ⚠️ a ancora nao traz ponto final (ela e' clausula), entao ele entra
        # aqui — sem isso o render saia "...gelatin trick Your wife will..."
        if not meio.rstrip().endswith("."):
            meio = meio.rstrip() + "."
        # ⭐ A PROMESSA fecha a cena 2, no lugar do bullet de loja. Ela fala com
        # o HOMEM que assiste, em 2a pessoa, e nomeia o orgao ou o que ela nota
        # nele — promessa sem referente e' "novo por que?".
        prom = rng.choice(_na_faixa(
            PROMESSAS, lambda x: meio + " " + x.format(o=o2),
            PISO_FALA[2], TETO_FALA[2]))
        f[1] = "%s %s" % (meio, prom.format(o=o2))

    if 2 in quais:
        isca_e = rng.choice(ISCAS_ENTREGA)
        curto_g = min(GATES, key=_palavras)

        def _c3(uso, gate):
            # ⚠️ ponto depois do USO: ele e' frase inteira e o CTA abre outra.
            # Sem isso o render saia "...your soldier wakes up Comment gelatin".
            return "%s. %s and I'll send you %s. %s" % (
                uso.format(o=o1).rstrip("."), sc.CTA_LITERAL, isca_e, gate)

        # ⛔ 2026-08-05 — `_cabem` termina em `or pool`, e com teto 25 ele
        # devolvia o pool INTEIRO: a cena 3 subiu de max 31 para 36. Aqui o
        # fallback e' a entrada mais CURTA, e a ISCA tambem cede — ela e' o
        # unico slot com folga (`the whole recipe` vs `the recipe and the
        # measurements`), e o `Comment gelatin,` e' intocavel.
        def _ok(pool, monta):
            v = [x for x in pool if _palavras(monta(x)) <= TETO_FALA[3]]
            return v or [min(pool, key=lambda x: _palavras(monta(x)))]

        isca_e = min(ISCAS_ENTREGA, key=_palavras) if _palavras(
            _c3(min(USOS, key=_palavras), curto_g)) > TETO_FALA[3] else isca_e
        uso = rng.choice(_ok(USOS, lambda u: _c3(u, curto_g)))
        gate = rng.choice(_ok(GATES, lambda g: _c3(uso, g)))
        f[2] = _c3(uso, gate)

    return f


def sortear(pagina, rng, led, travas=None):
    """Monta a spec. `travas` fixa eixos (pre-selecao do painel e cadeado)."""
    travas = travas or {}
    usados = led.get(pagina, {})

    # ⭐ TRAVA DE PELE — a pele chega em travas["pele"] ("clara"/"escura") e o
    # sorteio REMONTA O VIDEO EM VOLTA DELA: o mundo so' sai entre os que
    # COMPORTAM aquela pele, e a etnia sorteia dentro do mundo ja' filtrado.
    # ⛔ A ETNIA NUNCA SAI DE FORA DO MUNDO — e' a invariante do autoteste, e e'
    # ela que faz "etnia arrasta o mundo inteiro" ser verdade em vez de slogan.
    # Por isso quem se move e' o MUNDO, nunca a etnia.
    # ⚠️ Mundo travado incompativel CEDE e e' re-sorteado, de preferencia na
    # mesma familia: antes de derrubar o sorteio, o eixo derivado cede.
    pele = travas.get("pele")

    def _comporta(m):
        return not pele or any(_pele_de(e) == pele for e in m["etnias"])

    def _etnias_ok(m):
        """As etnias do mundo que servem a' pele pedida. ⛔ Sem este filtro o
        mundo passava (tem UMA etnia da pele) e a etnia sorteava entre TODAS as
        dele — foi assim que `escura` devolveu Asian American."""
        return [e for e in m["etnias"] if not pele or _pele_de(e) == pele]

    fam_trava = travas.get("familia_mundo")
    if travas.get("mundo"):
        mundo = _por_id(MUNDOS, travas["mundo"])
        if not _comporta(mundo):
            mundo = rng.choice(
                [m for m in MUNDOS if m["familia"] == mundo["familia"]
                 and _comporta(m)]
                or [m for m in MUNDOS if _comporta(m)]
                or [mundo])
    else:
        if fam_trava and fam_trava != "livre":
            fam = fam_trava
        else:
            fam = _fresco([{"id": x} for x in FAMILIAS_MUNDO],
                          usados.get("familia_mundo", []), rng, "id")["id"]
        cand = [m for m in MUNDOS if m["familia"] == fam and _comporta(m)]
        # ⛔ Familia sem mundo daquela pele: a FAMILIA cede, a pele nao.
        # ⛔⛔ E SE NEM O FALLBACK TIVER MUNDO, A PELE CEDE — nao o sorteio.
        # Achado sabotando `_pele_de` para provar que a sonda acusa: o
        # `rng.choice([])` levantava IndexError e derrubava o app do operador.
        # Perder a trava e' ruim; quebrar o app na mao dele e' pior, e um pool
        # de mundos editado amanha pode zerar uma das peles sem ninguem notar.
        mundo = rng.choice(cand
                           or [m for m in MUNDOS if _comporta(m)]
                           or MUNDOS)

    et = travas.get("etnia") or rng.choice(_etnias_ok(mundo)
                                           or mundo["etnias"])
    cor = travas.get("cor") or rng.choice(mundo["cores"])
    # ⭐ O TRAJE E' EIXO PROPRIO desde 2026-08-05, com pool por mundo. Cada
    # entrada e' (template_com_%s_de_cor, nome_curto) — o curto tem de vir do
    # traje SORTEADO, senao a ancora descreve uma roupa que nao esta' em cena.
    reacao = _fresco_traje(REACOES_HOMEM, usados.get("reacao", []), rng)
    apelo = rng.choice(APELO_EUA)
    # ⛔ NO MODO BELA A ROUPA TAMBEM MUDA. O operador nomeou TRES coisas —
    # *"super models com corpao e pouca roupa"* — e trocar so' o rosto e o corpo
    # deixaria a REF de biquini de tricô amish. Aqui o traje vem do MUNDO, entao
    # o modo o substitui pelo pool proprio do `short_comum`.
    traje = (_por_traje(mundo, travas["traje"]) if travas.get("traje")
             else sc.traje_bela(rng) if travas.get("bela")
             else _fresco_traje(mundo["trajes"], usados.get("traje", []), rng))
    ref = (_por_id(REFS, travas["ref"], "cabeca") if travas.get("ref")
           else sc.ref_bela(REFS[0], rng) if travas.get("bela")
           else rng.choice(REFS))
    # ⭐ A AMIGA sai do MESMO pool da narradora e NUNCA e' a mesma pessoa: duas
    # mulheres no quadro com a mesma descricao viram gemeas no render.
    amiga = rng.choice([x for x in REFS if x is not ref])
    # ⛔ TRAJE PROPRIO PARA CADA UMA. O operador leu o render e perguntou *"que
    # roupa e' essa?"* — as duas apareciam com o MESMO vestido, porque eu passava
    # `_traje(spec)` duas vezes. Duas mulheres identicas da cintura para cima
    # viram uniforme, e uniforme mata a leitura de "duas pessoas".
    # ⛔⛔ `x is not traje`, NAO `x is not None`. A versao anterior filtrava
    # coisa nenhuma — `None` nunca esta' no pool — e as duas sortavam a MESMA
    # roupa em 20,7% dos videos, que e' exatamente o defeito que este bloco foi
    # escrito para impedir. O comentario dizia a intencao certa e o codigo fazia
    # outra coisa: comentario nao e' guarda.
    _tj = [x for x in mundo["trajes"] if x is not traje] or mundo["trajes"]
    traje_amiga = rng.choice(_tj)
    # ⚠️ a reacao dela e' sorteada junto — ordem do operador: "ambas com pool de
    # cara de espanto, ou risos, etc".
    reacao_amiga = _fresco_traje(REACOES_AMIGA,
                                 usados.get("reacao_amiga", []), rng)
    # ⛔ O eixo HOMEM ficou MORTO quando o corpo-prova masculino saiu da cena
    # 3 (etapa [7], 2026-08-05). Continua sorteado so' para o `resumo_pt` e o
    # ledger nao quebrarem, e NAO recebe o MODO_FORTE: modo que nao muda pixel
    # nenhum e' botao que mente.
    homem = (_por_id(HOMENS, travas["homem"]) if travas.get("homem")
             else _fresco(HOMENS, usados.get("homem", []), rng, "id"))
    prop = (_por_id(PROPS, travas["prop"]) if travas.get("prop")
            else _fresco(PROPS, usados.get("prop", []), rng, "id"))
    sub = (_por_id(SUBSTANCIAS, travas["substancia"])
           if travas.get("substancia")
           else _fresco(SUBSTANCIAS, usados.get("substancia", []), rng, "id"))
    met = (_por_id(METODOS, travas["metodo"]) if travas.get("metodo")
           else _fresco(METODOS, usados.get("metodo", []), rng, "id"))
    com = (_por_id(COMUNS, travas["comum"]) if travas.get("comum")
           else _fresco(COMUNS, usados.get("comum", []), rng, "id"))
    # ⭐ UM raro por video, sorteado entre os nove (ordem do operador)
    raro = (_por_id(RAROS, travas["raro"]) if travas.get("raro")
            else _fresco(RAROS, usados.get("raro", []), rng, "id"))
    # ⭐ A CONFORMACAO DO PREPARO — eixo proprio desde 2026-08-05, por ordem do
    # operador. Entra no ledger como os outros: a mesma bancada em videos
    # seguidos da mesma pagina e' o que ele ve' primeiro no lote.
    preparo = (_por_id(PREPAROS, travas["preparo"]) if travas.get("preparo")
               else _fresco(PREPAROS, usados.get("preparo", []), rng, "id"))

    # ⛔ Dois orgaos DIFERENTES no mesmo video: repetir o substantivo em 24
    # segundos vira bordao.
    orgaos = rng.sample(NUCLEO, 2)

    # ⭐ A FLAG VIAJA NO SPEC. O `montar()` nao recebe `travas`, e sem

    # isto a clausula do rosto e o `resumo_pt` ficavam na versao comum

    # enquanto o corpo e a roupa ja' eram os do modo — a contradicao

    # exata que o CL26 documenta.

    spec = {"pagina": pagina, "bela": bool(travas.get("bela")), "mundo": mundo, "etnia": et, "cor": cor,
            "traje": traje, "traje_amiga": traje_amiga, "preparo": preparo,
            "reacao": reacao, "apelo": apelo,
            "reacao_amiga": reacao_amiga,
            "ref": ref, "amiga": amiga, "homem": homem,
            "prop": prop, "substancia": sub,
            "metodo": dict(met, vaso_fala=_sem_artigo(met["curto"])),
            "comum": com, "raro": raro, "orgaos": orgaos,
            # ⭐ 50/50, ordem do operador 2026-08-04
            "bandeira": rng.random() < 0.5}
    spec["falas"] = [v for _, v in sorted(_falas(spec, rng).items())]
    return spec


def _pessoa(spec):
    r = spec["ref"]
    return ("a %d-year-old %s woman, %s, %s, %s, wearing %s"
            % (r["idade"], spec["etnia"], r["corpo"], r["cabeca"], r["marca"],
               _traje(spec)))


def _ancora(spec):
    """⛔ BO7 — rosto E idade, nunca so' roupa."""
    r = spec["ref"]
    return BO_ANCORA % (r["idade"], spec["etnia"], _sem_artigo(r["cabeca"]),
                        _sem_artigo(r["marca"]), spec["traje"][1])


# ⭐ A BANDEIRA, 50/50 — ordem do operador. Ela nao mora nas strings de cenario
# deste motor (aprendemos no ESCANDALO que isso a torna obrigatoria por
# construcao): entra como clausula propria, e some inteira quando o sorteio diz.
BANDEIRA = " A US flag hangs on the wall behind her."


def montar(spec):
    """Os 7 blocos. Formatacao NOMEADA de ponta a ponta — sao 15+ campos por
    bloco, e um deslocamento de indice posicional troca pronome por cor sem
    estourar erro nenhum (bug que so' aparece no video pronto)."""
    m, ref, met = spec["mundo"], spec["ref"], spec["metodo"]
    com, raro, hom = spec["comum"], spec["raro"], spec["homem"]
    prop, sub = spec["prop"], spec["substancia"]
    band = BANDEIRA if spec.get("bandeira") else ""

    v = {
        "coz": m["coz"], "coz_c": m["coz_c"],
        "sup_a": m["sup_a"], "sup": m["sup"],
        "luz": m["luz"], "luz_c": m["luz_c"],
        "etnia": spec["etnia"], "idade": ref["idade"],
        "pessoa": _pessoa(spec), "ancora": _ancora(spec),
        "Ancora": _cap(_ancora(spec)),
        "vaso": met["vaso"], "vaso_curto": met["curto"], "acao": met["acao"],
        "comum_img": com["img"], "raro_img": raro["img"],
        "copo": BO_COPO, "anti": (sc.ANTICELEB_BELA if spec.get("bela") else ANTICELEB), "cauda": CAUDA, "band": band,
    }
    v["nao_toca"] = BO_NAO_TOCA % m["sup"]

    b = {}
    b["BLOCO 0 (REF)"] = (
        "REF 01: Photo of a real person, a %(idade)d-year-old %(etnia)s woman, "
        "chest up, facing the camera directly, neutral steady expression with "
        "her mouth closed. %(pessoa_curta)s %(apelo)s Hands out of frame, "
        "no objects. Plain neutral gray background, soft even frontal light. "
        "Slight sensor grain, soft focus, raw iPhone front camera aesthetic. "
        "No subtitles, no captions, no burned-in text, no watermark."
        % dict(v, apelo=_apelo(spec), pessoa_curta="%s. %s. Wearing %s."
               % (_cap(ref["cabeca"]), _cap(ref["marca"]), _traje(spec))))

    # --- CENA 1 — A ISCA NA LENTE + O VILAO ---------------------------------
    # ⛔ O despejo JA' ESTA' acontecendo no frame 0: nao ha' frame de "antes".
    # Mesma economia do EXTERIOR e do TROCA — 8 segundos nao pagam preparacao.
    # ⛔ AQUI NAO EXISTE `only person`: a cena 1 tem DUAS por construcao. A
    # trava de pessoa unica das outras cenas foi removida junto (BO6 reescrito).
    _a, _r = spec["amiga"], spec["ref"]
    b["IMAGE 01/03"] = (
        "Medium shot in %(coz)s.%(band)s %(duplo)s %(anti)s %(luz)s %(cauda)s"
        % dict(v, duplo=BO_DUPLA % (
            _r["idade"], spec["etnia"], _sem_artigo(_r["cabeca"]),
            _sem_artigo(_r["marca"]), _traje(spec), prop["murcho"],
            _a["idade"], spec["etnia"], _sem_artigo(_a["cabeca"]),
            _sem_artigo(_a["marca"]), _traje_de(spec, "traje_amiga"),
            prop["gigante"])))

    # --- CENA 2 — O PREPARO (o mecanismo) -----------------------------------
    # ⚠️ O utensilio VARIA (ordem do operador) e o verbo do TAKE acompanha.
    _pr = spec["preparo"]
    b["IMAGE 02/03"] = (
        "%(cena)s %(anti)s %(luz)s %(cauda)s"
        % dict(v, cena=BO_PREPARO % dict(
            v,
            bancada=_pr["bancada"] % v,
            acao=_pr["acao"],
            amiga=BO_AMIGA_FUNDO % (
                _a["idade"], spec["etnia"], _sem_artigo(_a["cabeca"]),
                _sem_artigo(_a["marca"]), _traje_de(spec, "traje_amiga"),
                spec["reacao_amiga"][0]))))

    # --- CENA 3 — AS DUAS + O PROP GIGANTE + O COPO + O CTA -----------------
    # ⭐ O objeto da keyword esta' NA MAO no frame em que a boca diz `gelatin,`.
    # ⛔⛔ TRES CORRECOES, todas achadas na auditoria da etapa [7]:
    #   1. HAVIA UM HOMEM AQUI. Heranca do BOTICA, e o operador nunca o pediu —
    #      a ordem dele foi *"o take final deve ter as duas mulheres novinhas
    #      lindas com uma delas segurando o geoduck ereto e bem grande"*. Com
    #      ele a cena tinha TRES pessoas e o terceiro corpo roubava o quadro do
    #      prop, que e' o payoff.
    #   2. O PROP GIGANTE NAO ESTAVA EM QUADRO. A ordem do operador pede ele
    #      explicitamente, e sem ele a cena 3 nao desmente o murcho da cena 1.
    #   3. A amiga usava `_traje(spec)` — a roupa da OUTRA. As duas apareciam
    #      iguais aqui mesmo depois de eu consertar as cenas 1 e 2.
    b["IMAGE 03/03"] = (
        "Closer medium shot in the same place, same background, same %(luz_c)s, "
        "filmed straight on and framed from the waist up. %(Ancora)s, standing "
        "centred in the frame and turned towards the lens, holding %(gigante)s. "
        "Her other hand holds %(copo)s. She looks directly into the camera, calm "
        "and certain, her mouth open mid-word as she speaks, her front teeth "
        "even and complete. %(amiga)s %(anti)s %(cauda)s"
        % dict(v, gigante=prop["gigante"],
               amiga=_cap(BO_AMIGA_FUNDO % (
                   _a["idade"], spec["etnia"], _sem_artigo(_a["cabeca"]),
                   _sem_artigo(_a["marca"]), _traje_de(spec, "traje_amiga"),
                   spec["reacao_amiga"][0]))))

    # ⛔⛔ O TAKE ANIMA A IMAGE — ELE NAO INVENTA OUTRO GESTO. Contradicao entre
    # IMAGE e TAKE e' pior que omissao: a omissao o gerador preenche com o frame;
    # a contradicao ele resolve mexendo no que estava certo.
    # ⛔⛔ OS TRES MOVIMENTOS ERAM OS DO BOTICA — achados pela lente
    # `lint_take_vs_image`, criada hoje ao rodar a etapa [7]. Este motor passava
    # 600 sorteios sem ERRO com os tres contradizendo a propria IMAGE:
    #   cena 1: mandava segurar um PRATO com po' caindo, e a IMAGE tem duas
    #           mulheres erguendo dois props — nao ha' prato nem despejo;
    #   cena 2: mandava socar PILAO / tampar LIQUIDIFICADOR, e a IMAGE mostra
    #           ela despejando DOIS JARROS de suco ao mesmo tempo;
    #   cena 3: falava de "the man behind her", e aqui nao ha' homem nenhum —
    #           a segunda pessoa e' a AMIGA, que e' o angulo inteiro.
    mov = [
        ("Both women keep their arms exactly where they are, each holding her "
         "own piece at the same height and the same distance from the lens, "
         "same size, same shape, same colour. Neither lowers her arm and "
         "neither sets anything down."),
        # ⛔ O movimento vem da CONFORMACAO SORTEADA, nunca de uma string fixa:
        # e' isso que impede o TAKE de descrever outra bancada.
        # ⚠️ O `mov` passa pelo `% v` como a bancada. Sem isso o `%(sup)s` saia
        # CRU no prompt em 201 de 600 videos — e nenhum linter pegava, porque o
        # guard de placeholder olha os blocos e o TAKE e' montado depois deles.
        # Achado LENDO as seis conformacoes geradas, uma a uma.
        ((spec["preparo"]["mov"] % v) + " " + v["nao_toca"]),
        ("She holds the glass steady at chest height the whole time and never "
         "sets it down. Her other hand keeps the piece upright and never lowers "
         "it."),
    ]
    # ⛔ NENHUMA CENA DESTE ANGULO TEM PESSOA UNICA — sao duas mulheres nas
    # tres. Declarar `only person in the shot` e' ordem contraditoria, e o Veo
    # resolve APAGANDO a segunda, que e' o bit inteiro do angulo.
    elenco = [
        "Only the woman on frame-left speaks, straight into the lens. The other "
        "never speaks and keeps her eyes on what she is holding.",
        "She is the only person in the shot.",
        BO_AMIGA_TAKE % spec["reacao_amiga"][1],
    ]
    audio = ["%s. No music." % m["audio"],
             # ⛔ O som tambem sai da conformacao — ele tambem e' parte do
             # prompt, e tambem contradizia a IMAGE quando vinha de fora.
             "%s, %s. No music." % (m["audio"], spec["preparo"]["audio"]),
             "%s. No music." % m["audio"]]

    for i in range(3):
        b["TAKE %02d/03" % (i + 1)] = (
            "Animate the provided image exactly. Handheld iPhone shot, very "
            "slight natural sway, no cuts. %s %s\n"
            'Dialogue: "%s"\nAudio: %s'
            % (mov[i], elenco[i], sonorizar(spec["falas"][i]), audio[i]))

    return sc.selar_takes(sc.selar_tags(b))


# ---------------------------------------------------------------------------
# LINTER
# ---------------------------------------------------------------------------

def _sentencas(fala):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", fala or "") if s.strip()]


# ⛔ BO10 — ZERO MEDIDA DE CRESCIMENTO. A fonte promete "5 inches faster in a
# week"; ordem do operador: *"so' a promessa sem centimetro"*.
MEDIDA = re.compile(r"\b\d+\s*(inch|inches|cm|centimet\w*)\b"
                    r"|\b(an|one|two|three|four|five)\s+(inch|inches)\b", re.I)

# ⛔ BO11 — nome cientifico NUNCA na fala.
# ⛔⛔ `epimedium\s+\w+` REPROVAVA A COPY DO PROPRIO OPERADOR — corrigido
# 2026-08-05. O padrao existia para pegar o binomio `Epimedium spp.`, mas casava
# `epimedium` seguido de QUALQUER palavra: a frase que ele escreveu a mao
# ("Fresh ginger and epimedium and a secret") era acusada de nome cientifico.
# ⚠️ `epimedium` E' o nome POPULAR no nosso pool — esta' no campo `nome`, e BO8
# exige que ele apareca na cena 2. A lente estava proibindo o que outra lente
# obrigava, e so' nao explodia antes porque a receita antiga punha uma virgula
# depois dele. Mudar a ordem das palavras acordou o conflito.
# ⭐ Agora so' o que e' de fato binomio: o epiteto tem de ser `spp.` ou um nome
# de especie, nunca uma palavra funcional do ingles.
CIENTIFICO = re.compile(
    r"\b(lepidium|eurycoma|tribulus terrestris|epimedium\s+(?:spp\.?|"
    r"grandiflorum|sagittatum|brevicornum|koreanum)|trigonella|"
    r"ptychopetalum|ginkgo biloba|mucuna pruriens|smilax\s+(?:spp\.?|\w+ata))"
    r"\b", re.I)


def lint(spec, blocos):
    ach = []
    falas = spec["falas"]
    m = spec["mundo"]

    sc.lint_tags(blocos, ach)
    sc.lint_sem_texto(blocos, ach)
    sc.lint_isca_cta(falas[2], ach, "a cena 3 (CTA)")
    sc.lint_cta_literal(falas[2], ach, "a cena 3 (CTA)")
    sc.lint_bandeira(spec, blocos, ach, rotulo="BO12")

    if not blocos.get("BLOCO 0 (REF)", "").lstrip().upper().startswith("REF"):
        ach.append(("ERRO", "BLOCO 0 sem o cabecalho REF — o AdBatch descarta a "
                            "referencia em silencio"))

    # --- tetos e pisos ------------------------------------------------------
    for i, f in enumerate(falas, 1):
        n = _palavras(f)
        if n > TETO_FALA[i]:
            ach.append(("ERRO", "BO13: cena %d com %d palavras (teto %d) — a "
                                "narracao passa de 7s" % (i, n, TETO_FALA[i])))
        if n < PISO_FALA[i]:
            ach.append(("AVISO", "BO13: cena %d com %d palavras (piso %d) — "
                                 "sobra silencio nos 8s" % (i, n, PISO_FALA[i])))

    # --- BO9: ⭐⭐ A ABERTURA DE CADA CENA TEM REFERENTE (licoes §21) ---------
    # ⛔ Este agente NASCE com a regra aplicada, e e' o primeiro. A primeira
    # sentenca e' a que o espectador ouve antes de qualquer outra, sozinha, no
    # scroll — e era a unica que nenhuma lente minha olhava.
    # ⛔⛔ A DEFINICAO DE `referente` MUDOU EM 2026-08-04, E ESSE FOI O DEFEITO.
    # A versao anterior aceitava, na cena 1, o PROP e a SUBSTANCIA — ou seja, o
    # que aparece no quadro. A lente rodava verde e a copy falava do vegetal.
    # O que esta' em quadro sao adereços; o que esta' EM JOGO e' o orgao do
    # marido dela. A cena 1 agora exige ORGAO **e** o homem.
    # ⚠️ a cena 2 deste angulo abre com a RECEITA (beterraba e cenoura), que e'
    # referente concreto em 100% do pool — os termos abaixo cobrem isso.
    # ⚠️ a cena 2 deste angulo ABRE com a receita (beterraba + cenoura), nao com
    # o orgao — e' referente concreto em 100% do pool, so' que outro.
    alvos = [(2, ["gelatin", "beet", "carrot", "juice"]
                 + [o.lower() for o in NUCLEO]),
             (3, [o.lower() for o in NUCLEO])]
    for i, termos in alvos:
        sents = _sentencas(falas[i - 1])
        if not sents:
            continue
        baixo = sents[0].lower()
        if not any(t.lower() in baixo for t in termos):
            ach.append(("ERRO", "BO9: a abertura da cena %d nao nomeia o "
                                "referente — %r deixa o espectador perguntando "
                                "'do que ela esta' falando?' no segundo em que "
                                "ele decide se fica (licoes §21)"
                        % (i, sents[0])))
    sents1 = _sentencas(falas[0])
    if sents1:
        a1 = sents1[0].lower()
        if not any(o.lower() in a1 for o in NUCLEO):
            ach.append(("ERRO", "BO9: a abertura da cena 1 nao nomeia o ORGAO — "
                                "%r fala do adereço e nao do que esta' em jogo, "
                                "e o espectador acha que e' culinaria"
                        % sents1[0]))
        # ⛔ REESCRITO PARA ESTE ANGULO. No BOTICA a narradora fala do MARIDO
        # dela; aqui ela fala com o ESPECTADOR em segunda pessoa (`If you want
        # your {o} to go from this...`). Cobrar `my husband` reprovaria 100% da
        # producao. O que importa continua sendo haver PESSOA na frase — e aqui
        # a pessoa e' `you`, que e' mais forte: e' o proprio espectador.
        if not re.search(r"\byou\b|\byours?\b", a1):
            ach.append(("ERRO", "BO9: a abertura da cena 1 nao fala COM alguem — "
                                "sem `you/your` a promessa nao tem dono (%r)"
                        % sents1[0]))

    # --- BO8: ⭐⭐ O RARO E O APOSTO, e o aposto mora na CENA 1 --------------
    # ⚠️ Ordem do operador: o raro aparece nas DUAS cenas — na 1 como "mecanismo
    # unico secreto" (curiosidade), na 2 como receita. O APOSTO e' pago na 1;
    # repeti-lo na 2 custaria 5-9 palavras no take mais denso dos tres.
    raro = spec["raro"]
    # ⛔ No BOTICA o raro era o segredo da cena 1. Aqui a cena 1 e' o DEITICO
    # DUPLO e o raro entra na cena 2, com o acafrao da fonte.
    # ⛔⛔ AS DUAS REGRAS DO BOTICA (raro na cena 1, aposto obrigatorio) FORAM
    # APAGADAS, nao desligadas com `if False`. Elas nao valem aqui: a cena 1 e' o
    # deitico duplo e a fonte diz apenas *"a pinch of saffron"*, sem explicar. O
    # aposto custaria 5-9 palavras e MEDIDO levava a cena 2 a 39 contra teto 25.
    # ⚠️ `if False` nao e' apagar: ele deixa a SONDA correspondente do autoteste
    # viva e cega, passando sempre sem proteger nada (§29). Foi assim que este
    # motor ficou o dia inteiro com um controle decorativo.
    if raro["nome"] not in falas[1]:
        ach.append(("ERRO", "BO8: a cena 2 nao nomeia o ingrediente raro (%s) na "
                            "receita" % raro["nome"]))
    for r in RAROS:
        if not 3 <= len(r["aposto"].split()) <= 12:
            ach.append(("ERRO", "BO8: aposto de %r com %d palavras (regra de "
                                "economia: 3-10, teto duro 12)"
                        % (r["nome"], len(r["aposto"].split()))))

    # --- BO15: ⭐ a PROMESSA nomeia o orgao, e o mecanismo nao e' ENTREGUE ---
    # ⛔ Ordem do operador, 2026-08-04, duas partes:
    #   1. *"tome cuidado ao dizer que X E' o gelatin trick: pode matar a
    #      curiosidade"* -> a cena 2 declara um passo RETIDO, nunca equipara a
    #      receita visivel ao mecanismo.
    #   2. *"«you'll be a new person» apenas seria vago pq pode ser nova pessoa
    #      por qualquer circunstancia"* -> promessa sem orgao e' promessa de
    #      nada.
    # ⭐⭐ O STACK E' COBRADO, NAO CONFIADO. Criterio de curadoria do operador:
    # a linha vence quando empilha PROMESSA + DESEJO OCULTO, e o desejo oculto
    # deste funil mora na REACAO DELA. A involuntariedade e' a alavanca de
    # credibilidade: `my {o} is harder` e' alegacao, `she noticed before I did`
    # e' evidencia — por isso toda promessa tem de ter ELA em cena, nao so' o
    # resultado.
    for linha in PROMESSAS:
        if "{o}" not in linha:
            ach.append(("ERRO", "BO15: promessa sem `{o}` — %r e' 'novo por "
                                "que?'" % linha))
        if not re.search(r"\b(she|her|wife)\b", linha, re.I):
            ach.append(("ERRO", "BO15: promessa sem o DESEJO OCULTO — %r entrega "
                                "so' o resultado. Sem a reacao dela e' alegacao "
                                "do proprio homem, e alegacao nao prova nada"
                        % linha))
    ultima = _sentencas(falas[1])[-1] if _sentencas(falas[1]) else ""
    if not any(o.lower() in ultima.lower() for o in NUCLEO):
        ach.append(("ERRO", "BO15: a promessa que fecha a cena 2 nao nomeia o "
                            "orgao — %r promete mudanca sem dizer em que"
                    % ultima))
    # ⛔ E o mecanismo NAO pode ser entregue como equivalente da receita: se a
    # cena 2 diz "that is the gelatin trick" logo depois de listar tudo, o
    # espectador ja' tem o produto e nao tem por que comentar.
    if re.search(r"(that|this) is the gelatin trick[^.]*\band\b", falas[1], re.I):
        ach.append(("ERRO", "BO15: a cena 2 equipara a receita visivel ao "
                            "mecanismo e emenda o beneficio — isso entrega o "
                            "produto de graca e mata a curiosidade que o CTA "
                            "existe para cobrar"))

    # --- BO11: zero nome cientifico na fala ---------------------------------
    corpo = " ".join(falas)
    hit = CIENTIFICO.search(corpo)
    if hit:
        ach.append(("ERRO", "BO11: nome cientifico na fala (%r) — o binomio vive "
                            "no campo `interno`, nunca na boca do personagem"
                    % hit.group(0)))

    # --- BO10: zero medida de crescimento -----------------------------------
    hit = MEDIDA.search(corpo)
    if hit:
        ach.append(("ERRO", "BO10: medida de crescimento na fala (%r) — ordem do "
                            "operador: so' a promessa, sem centimetro"
                    % hit.group(0)))

    # --- BO3: APOSENTADA EM 2026-08-05 -------------------------------------
    # ⛔ Ordem do operador: *"tirar o vilao do escopo do take 1"*. A lente cobrava
    # que uma parcela das iscas nomeasse a farmacia; sem vilao na cena 1 ela
    # reprovaria 100% da producao. Regra que cobra o que o operador mandou tirar
    # nao e' defesa, e' sabotagem.
    # ⚠️ CONSEQUENCIA REGISTRADA, porque ela e' real e ele decidiu com ela na
    # mesa: a farmacia so' existia nessas iscas — zero mencoes em ANCORAS,
    # PROMESSAS, RECEITAS, USOS, GATES e ISCAS_ENTREGA. Ela sai do video inteiro.
    # O angulo continua sendo a botica de casa, so' que sem o adversario dito em
    # voz alta: ele fica implicito no `nobody sells` dos fechos e na propria
    # existencia da receita caseira.

    # --- BO4: o mecanismo ----------------------------------------------------
    if "gelatin trick" not in " ".join(falas).lower():
        ach.append(("ERRO", "BO4: literal `gelatin trick` ausente — sem ele o "
                            "criativo deixa de ser congruente com a VSL"))
    if "gelatin trick" not in falas[1].lower():
        ach.append(("ERRO", "BO4: o `gelatin trick` tem de estar na CENA 2, que "
                            "e' a cena do mecanismo"))

    # --- cota do orgao -------------------------------------------------------
    cota = [i for i, f in enumerate(falas, 1)
            if any(o.lower() in f.lower() for o in NUCLEO)]
    if len(cota) < 2:
        ach.append(("ERRO", "BO14: cota do orgao %d/3 (minimo 2) — cenas sem "
                            "substantivo do nucleo: %s"
                    % (len(cota), [i for i in (1, 2, 3) if i not in cota])))
    if len(set(spec["orgaos"])) < 2:
        ach.append(("ERRO", "BO14: o mesmo orgao repetido no mesmo video"))

    i1, i3 = blocos["IMAGE 01/03"], blocos["IMAGE 03/03"]

    # --- BO1: a isca na lente ------------------------------------------------
    # ⛔ REESCRITO: no BOTICA a escala vinha do ENQUADRAMENTO (mao esticada para
    # a lente). Aqui ela vem da COMPARACAO — dois props no mesmo quadro, um
    # murcho e um gigante. Exigir a clausula do outro angulo reprovaria tudo.
    if "raised at chest height" not in i1:
        ach.append(("ERRO", "BO1: IMAGE 01/03 sem a escala por ENQUADRAMENTO — "
                            "sem ela o prop vira um objeto qualquer na mao"))
    # ⛔ AQUI SAO DOIS PROPS, nao um. A lente herdada olhava `prop["img"]`;
    # neste angulo o par murcho/gigante tem de estar INTEIRO no quadro 1 — se
    # so' um aparece, o `from this to this` fica sem a metade que ele aponta.
    if spec["prop"]["murcho"] not in i1 or spec["prop"]["gigante"] not in i1:
        ach.append(("ERRO", "BO1: IMAGE 01/03 sem o prop sorteado"))

    # --- BO5: o copo so' na cena 3 -------------------------------------------
    for nome in ("IMAGE 01/03", "IMAGE 02/03"):
        if BO_COPO in blocos[nome]:
            ach.append(("ERRO", "BO5: o copo pronto fora da cena 3 (%s) — "
                                "entrega o payoff antes da promessa" % nome))
    if BO_COPO not in i3:
        ach.append(("ERRO", "BO5: a cena 3 tem de mostrar o copo na mao — e' o "
                            "objeto da keyword"))

    # --- BO6: ⭐⭐ AS DUAS MULHERES, e SO' elas ------------------------------
    # ⛔⛔ REESCRITO. As tres regras que estavam aqui vigiavam um HOMEM MUDO —
    # heranca literal do BOTICA, num angulo que o operador definiu como *"duas
    # mulheres novinhas lindas"*. Elas cobravam que ele olhasse o copo, que
    # tivesse trava de mudez e que so' existisse na cena 3, e o motor obedecia:
    # a cena 3 saia com TRES pessoas e o terceiro corpo roubava o quadro do prop
    # gigante, que e' o payoff. Achado na auditoria da etapa [7].
    # ⭐ O que a lente vigia agora e' o angulo de verdade: a AMIGA nas tres
    # cenas, muda, e nenhum terceiro corpo.
    _a_idade = "the same %d-year-old" % spec["amiga"]["idade"]
    for nome in ("IMAGE 01/03", "IMAGE 02/03", "IMAGE 03/03"):
        if "never speaks" not in blocos[nome]:
            ach.append(("ERRO", "BO6: %s sem a trava de mudez da segunda mulher "
                                "— sem ela o Veo dubla a fala nas duas bocas "
                                "(falha que derrubou a cena do casal do "
                                "VAZAMENTO)" % nome))
    if "never speaks" not in blocos["TAKE 03/03"]:
        ach.append(("ERRO", "BO6: TAKE 03/03 sem a trava de mudez"))
    # ⛔ NENHUM TERCEIRO CORPO. O homem do BOTICA saiu; se ele voltar por
    # copia, esta lente grita antes do render.
    for nome in ("IMAGE 01/03", "IMAGE 02/03", "IMAGE 03/03"):
        for pista in (" man,", " man ", " his ", " he "):
            if pista in blocos[nome].replace("American man", "AMERICANO"):
                ach.append(("ERRO", "BO6: %s tem um HOMEM em quadro (%r) — este "
                                    "angulo e' de duas mulheres, e o terceiro "
                                    "corpo rouba o quadro do prop"
                            % (nome, pista.strip())))
                break
    if "only person" in i3:
        ach.append(("ERRO", "BO6: a cena 3 declara pessoa UNICA e tem DUAS — "
                            "ordem contraditoria: o Veo resolve apagando a "
                            "amiga, que e' o angulo inteiro"))
    # ⭐ A AMIGA TEM ANCORA PROPRIA nas cenas 2 e 3 — sem ela o Veo troca a
    # segunda mulher entre os blocos e a comparacao perde o dono.
    for nome in ("IMAGE 02/03", "IMAGE 03/03"):
        if _a_idade not in blocos[nome].lower() and _a_idade.lower() not in blocos[nome].lower():
            ach.append(("ERRO", "BO6: %s sem a ancora da segunda mulher (%s) — "
                                "e' onde o Veo a troca por outra pessoa"
                        % (nome, _a_idade)))

    # --- BO7: a ancora de continuidade nas cenas 2 e 3 ----------------------
    for nome in ("IMAGE 02/03", "IMAGE 03/03"):
        if ("the same %d-year-old" % spec["ref"]["idade"]
                not in blocos[nome].lower()):
            ach.append(("ERRO", "BO7: %s sem a ancora `the same N-year-old` — e' "
                                "onde o Veo troca de pessoa entre blocos" % nome))

    # --- BO2: nada cresce ----------------------------------------------------
    # ⛔⛔ A CENA 1 E' ISENTA NESTE ANGULO, e a razao e' semantica, nao
    # permissiva. A lente compartilhada procura vocabulario de CRESCIMENTO para
    # impedir que o prop mude de estado fora da cena do bit — regra que existe
    # por causa do RESSURREICAO, onde o proxy alonga na tela.
    # ⚠️ Aqui os dois props sao ESTATICOS e a palavra que ela acusa (`limp`,
    # `shrivelled`, `soft`) descreve o prop MURCHO: e' o OPOSTO de crescimento,
    # e e' exatamente o que o angulo precisa dizer. Nada cresce em cena nenhuma
    # deste motor — a comparacao acontece entre DOIS objetos, nao dentro de um.
    _b2 = {k: v for k, v in blocos.items() if k != "IMAGE 01/03"}
    sc.lint_nada_cresce(_b2, ach, rotulo="BO2")

    # --- P12: zero marca legivel NA IMAGEM ----------------------------------
    # ⚠️ As marcas DITAS (Walmart/Costco) sao permitidas por ordem do operador —
    # a varredura e' so' sobre a direcao de cena, nunca sobre a fala.
    for nome, txt in blocos.items():
        if nome.startswith("BLOCO"):
            continue
        direcao = txt.split("\nDialogue:")[0]
        for marca in ("walmart", "costco", "arm & hammer", "printed label",
                      "logo", "brand name"):
            if marca in direcao.lower():
                ach.append(("ERRO", "P12: %s traz marca/rotulo legivel na IMAGEM "
                                    "(%r) — na fala e' permitido, em cena nao"
                            % (nome, marca)))

    # --- a superficie do mundo e' a unica em cena ---------------------------
    # ⚠️ SO' A DIRECAO DE CENA. A fala nunca entra na varredura de token: um
    # VILAO diz "the box behind the counter", que e' ingles correto e nao tem
    # nada a ver com a superficie do mundo. Copiei esta regra do COLO e perdi o
    # escopo — a lente acusou 70 de 600 sorteios que estavam certos (§16).
    junto = " ".join(t.split(chr(10) + "Dialogue:")[0]
                     for k, t in blocos.items() if not k.startswith("BLOCO"))
    if m["sup"] != "counter" and re.search(r"\bcounter\b", junto):
        ach.append(("ERRO", "`counter` sobrou num mundo de %s (%s) — literal "
                            "esquecido no refactor" % (m["sup"], m["id"])))
    if re.search(r"\ba [aeiou]", junto):
        ach.append(("ERRO", "artigo errado: %r"
                    % re.search(r"\ba [aeiou]\w+", junto).group()))
    if re.findall(r"\{\w+\}", junto):
        ach.append(("ERRO", "placeholder cru no prompt: %s"
                    % re.findall(r"\{\w+\}", junto)[:3]))

    # ⛔⛔ TAKE CONTRA IMAGE — 2026-08-05. Este motor tem `lint()` proprio e NAO
    # passa pelo `lint_curto`, entao a lente compartilhada nao chegava aqui.
    # ⚠️ Foi assim que a primeira varredura deu "limpo" para sete motores: eles
    # nunca rodaram a lente. "Limpo" sem cobertura e' o pior resultado possivel,
    # porque parece verde. Medir a lente e' medir TAMBEM se ela e' chamada.
    # ⛔ PAINEL HONESTO — 2026-08-05. Nenhum eixo desenhado no painel pode
    # deixar de chegar ao video.
    # ⛔⛔ O SEGUNDO DEITICO TEM DE NOMEAR QUEM SEGURA O OUTRO PROP.
    # Ordem do operador, 2026-08-05, lendo o render *"like this one and not this
    # one"*: **"excesso de pronome. A proxy que a amiga ao lado esta segurando
    # voce tem que especificar pro telespectador"**.
    # ⚠️ Dois `this one` na mesma frase apontam para lugar nenhum: o espectador
    # ve' dois objetos e nao sabe qual e' qual, e o hook inteiro depende disso.
    for _v in VIRADAS:
        if not re.search(r"\b(she|her|my friend|my girl)\b", _v):
            ach.append(("ERRO", "BO16: a virada %r nao nomeia quem segura o "
                                "outro prop — deitico sem referente" % _v))
    _f1 = (spec["falas"][0] or "")
    if len(re.findall(r"\bthis one\b", _f1, re.I)) > 1:
        ach.append(("ERRO", "BO16: a cena 1 diz `this one` duas vezes — os dois "
                            "deiticos apontam para lugar nenhum e o espectador "
                            "nao sabe qual e' qual (%r)" % _f1))
    # ⛔ O FECHO nao pode ser mais um deitico: `this one is for you` logo depois
    # do par faz o `this one` apontar para o PROP, e a frase promete um vegetal.
    if re.search(r"\bthis one is for you\b", _f1, re.I):
        ach.append(("ERRO", "BO16: o fecho da cena 1 e' um terceiro deitico — "
                            "ele tem de nomear O QUE e' que e' para ele"))

    sc.lint_painel_honesto(sys.modules[__name__], spec, blocos, ach)

    # ⛔⛔ AS TRAVAS DE FORMA DO GEODUCK, que o EXTERIOR pagou em recusa (EX7).
    # ⚠️ Elas nasceram como "escrevi a string certa" — e regra que depende de eu
    # lembrar nao e' regra. Custam duas linhas e valem para qualquer prop novo.
    _tk = " ".join(v for k, v in blocos.items() if k.startswith("TAKE")).lower()
    for _proibido in ("geoduck", "clam"):
        if _proibido in _tk:
            ach.append(("ERRO", "EX7: o TAKE nomeia a especie (%r) — no TAKE o "
                                "prop e' generico; a especie so' vive na IMAGE"
                        % _proibido))
    # ⛔ SO' O `neck` DO MOLUSCO. A primeira versao olhava a palavra solta e
    # acusava `a halter top tied at the neck` — o TRAJE, em 11 de 600 videos.
    # Falso positivo e' pior que lente nenhuma: o operador aprende a ignorar.
    for _b in blocos.values():
        _l = _b.lower()
        for _m in ("clam", "shell", "geoduck"):
            _i = _l.find(_m)
            if _i >= 0 and "neck" in _l[max(0, _i - 90):_i + 90]:
                ach.append(("ERRO", "EX7: `neck` ao lado do molusco — a peca do "
                                    "geoduck e' o `siphon`, e `neck` ja' "
                                    "derrubou render nosso"))
                break

    sc.lint_take_vs_image(blocos, ach)

    return ach


def prop_n(spec):
    return spec["prop"]["nome"]


# ---------------------------------------------------------------------------
# UI
# ---------------------------------------------------------------------------

def resumo_pt(spec):
    m = spec["mundo"]
    # ⛔ REESCRITO. Aqui estava o resumo do BOTICA, palavra por palavra — ele
    # anunciava despejo, liquidificador e "um homem mudo e espantado atras",
    # e este angulo nao tem homem nenhum: sao DUAS MULHERES. E' o texto que o
    # operador le para aprovar em dois segundos. Achado na etapa [7].
    return ("Duas mulheres %s de %d e %d anos, em %s (%s). Cena 1: lado a lado, "
            "uma com %s e a outra com %s, erguidos a altura do peito. Cena 2: a "
            "bancada com a receita. Cena 3: as duas, com o prop grande na mao "
            "dela.%s"
            % (spec["etnia"], spec["ref"]["idade"], spec["amiga"]["idade"],
               m["id"].replace("_", " "), m["familia"],
               spec["prop"]["murcho"].split(",")[0],
               spec["prop"]["gigante"].split(",")[0],
               " Com bandeira." if spec.get("bandeira") else " Sem bandeira."))


def nova_fala(spec, i, rng):
    spec["falas_map"] = {j: f for j, f in enumerate(spec["falas"])}
    return _falas(spec, rng, quais=(i,))[i]


def _apos_mundo(spec, rng):
    """Trocou o MUNDO: etnia e cor tem de vir do mundo novo, senao o botao
    `trocar` deixa em cena a incongruencia que os MUNDOS existem para impedir."""
    if spec["etnia"] not in spec["mundo"]["etnias"]:
        spec["etnia"] = rng.choice(spec["mundo"]["etnias"])
    if spec["cor"] not in spec["mundo"]["cores"]:
        spec["cor"] = rng.choice(spec["mundo"]["cores"])


def _apos_cena1(spec, rng):
    """Trocou o PROP ou a SUBSTANCIA: a cena 1 os NOMEIA (BO9), entao a fala tem
    de ser remontada — senao a boca fala de um objeto que nao esta' em cena."""
    spec["falas"][0] = nova_fala(spec, 0, rng)


def _apos_cena2(spec, rng):
    """Trocou o METODO, o COMUM ou o RARO: os tres estao NA FALA da cena 2."""
    if "vaso_fala" not in spec["metodo"]:
        spec["metodo"] = dict(spec["metodo"],
                              vaso_fala=_sem_artigo(spec["metodo"]["curto"]))
    spec["falas"][1] = nova_fala(spec, 1, rng)


EIXOS_QUE_MEXEM_NA_COPY = {
    "mundo": _apos_mundo,
    "prop": _apos_cena1,
    "substancia": _apos_cena1,
    "metodo": _apos_cena2,
    "comum": _apos_cena2,
    "raro": _apos_cena2,
}

TETO_LEDGER = {"familia_mundo": len(FAMILIAS_MUNDO), "prop": len(PROPS),
               "substancia": len(SUBSTANCIAS), "metodo": len(METODOS),
               "comum": len(COMUNS), "raro": len(RAROS), "homem": len(HOMENS)}

MIN_OPCOES = 8


# ---------------------------------------------------------------------------
# AUTOTESTE
# ---------------------------------------------------------------------------

def autoteste(n=600):
    """As invariantes do agente, MEDIDAS, com controles positivos e negativos.

    ⚠️ `0 ERRO` num lote grande e' SUSPEITA, nao aprovacao: pode ser motor limpo
    ou regra morta. Por isso cada trava tem um sabotador, e o sabotador tem de
    CHEGAR onde a regra olha (licoes §16).
    """
    falhas = []
    vistos = collections.defaultdict(set)
    fam = collections.Counter()
    band = collections.Counter()
    larguras = {1: [], 2: [], 3: []}

    for seed in range(n):
        spec = sortear("joe", random.Random(seed), {}, {})
        blocos = montar(spec)
        for tipo, msg in lint(spec, blocos):
            if tipo == "ERRO":
                falhas.append("seed %d (%s): %s" % (seed, spec["mundo"]["id"], msg))
        for eixo, chave in (("mundo", "id"), ("prop", "id"), ("substancia", "id"),
                            ("metodo", "id"), ("comum", "id"), ("raro", "id"),
                            ("homem", "id")):
            vistos[eixo].add(spec[eixo][chave])
        vistos["etnia"].add(spec["etnia"])
        vistos["ref"].add(spec["ref"]["marca"])
        fam[spec["mundo"]["familia"]] += 1
        band[bool(spec["bandeira"])] += 1
        for i, f in enumerate(spec["falas"], 1):
            larguras[i].append(_palavras(f))
        if spec["etnia"] not in spec["mundo"]["etnias"]:
            falhas.append("seed %d: etnia fora do mundo" % seed)

    for eixo, pool in (("mundo", MUNDOS), ("prop", PROPS),
                       ("substancia", SUBSTANCIAS), ("metodo", METODOS),
                       ("comum", COMUNS), ("raro", RAROS), ("homem", HOMENS)):
        if len(vistos[eixo]) != len(pool):
            falhas.append("%s: %d de %d nunca sorteados"
                          % (eixo, len(pool) - len(vistos[eixo]), len(pool)))
    for nome, pool in (("MUNDOS", MUNDOS), ("METODOS", METODOS),
                       ("RAROS", RAROS), ("COMUNS", COMUNS),
                       ("SUBSTANCIAS", SUBSTANCIAS), ("REFS", REFS),
                       ("HOMENS", HOMENS), ("PROBLEMAS", PROBLEMAS),
                       ("VIRADAS", VIRADAS), ("FECHOS", FECHOS),
                       ("USOS", USOS),
                       ("ISCAS_ENTREGA", ISCAS_ENTREGA)):
        # ⚠️ PROPS tem piso PROPRIO de 5 e ele e' EMPIRICO: o pool e' o conjunto
        # dos props que PASSARAM no gerador em teste manual (COLO, 2026-08-03).
        if len(pool) < MIN_OPCOES:
            falhas.append("eixo %s com %d opcoes (minimo %d)"
                          % (nome, len(pool), MIN_OPCOES))
    if len(PROPS) < 5:
        falhas.append("PROPS abaixo do piso empirico de 5")
    for f, q in fam.items():
        if q > n * 0.25:
            falhas.append("familia %s levou %.1f%% do lote (teto 25%%)"
                          % (f, 100.0 * q / n))
    for k, q in band.items():
        if not 0.35 <= q / float(n) <= 0.65:
            falhas.append("bandeira %s em %.1f%% do lote (faixa 35-65%%)"
                          % (k, 100.0 * q / n))

    # ---- CONTROLES ---------------------------------------------------------
    # ⛔⛔ NENHUM POOL COM ENTRADA REPETIDA — trava criada em 2026-08-05.
    # Ao ampliar os pools eu acrescentei tres iscas que JA' EXISTIAM. Duplicata
    # nao quebra nada: ela dobra em silencio a chance daquela linha e ocupa um
    # slot que deveria ser repertorio novo. O sintoma so' apareceu porque a
    # cobertura media 15 de 18 sem conseguir apontar as faltantes.
    # ⚠️ Compara pelo TEXTO da entrada, nao pelo objeto — pools de tupla e de
    # dict entram por `str`.
    for _n, _p in (("PROBLEMAS", PROBLEMAS), ("VIRADAS", VIRADAS),
                   ("FECHOS", FECHOS), ("RECEITAS", RECEITAS),
                   ("ANCORAS", ANCORAS), ("PROMESSAS", PROMESSAS),
                   ("USOS", USOS), ("ISCAS_ENTREGA", ISCAS_ENTREGA),
                   ("GATES", GATES), ("REFS", REFS), ("HOMENS", HOMENS),
                   ("REACOES_HOMEM", REACOES_HOMEM), ("MUNDOS", MUNDOS)):
        _txt = [str(_x) for _x in _p]
        _rep = sorted({_x for _x in _txt if _txt.count(_x) > 1})
        for _x in _rep:
            falhas.append("pool %s tem entrada REPETIDA: %s" % (_n, _x[:70]))

    ctrl = []
    s = sortear("joe", random.Random(1), {}, {})
    b = montar(s)

    # ⭐ [BO8] o raro FORA da cena 2 — a regra que este angulo de fato tem.
    # ⚠️ A sonda anterior mexia em `falas[0]` procurando aposto, e o aposto foi
    # DISPENSADO aqui por medicao. Ela passava sempre. Sonda de regra morta e'
    # decoracao — e decoracao que faz o autoteste inteiro perder o direito de
    # ser acreditado, porque ele imprime "OK" do mesmo jeito.
    s8 = dict(s, falas=list(s["falas"]))
    s8["falas"][1] = s8["falas"][1].replace(s["raro"]["nome"], "something")
    if not any("BO8" in msg for _, msg in lint(s8, b)):
        ctrl.append("[BO8] NAO acusa o raro ausente da receita da cena 2")
    if any("BO8" in msg for _, msg in lint(s, b)):
        ctrl.append("[BO8] acusa a forma CERTA (raro nomeado na cena 2)")

    # ⭐ [BO9] o caso que o operador reprovou: a cena 1 falando do vegetal
    s9b = dict(s, falas=list(s["falas"]))
    s9b["falas"][0] = ("Nobody told you what crushed cinnamon does to an "
                       "eggplant, did they? " + _sentencas(s["falas"][0])[-1])
    if not any("BO9" in msg for _, msg in lint(s9b, b)):
        ctrl.append("[BO9] NAO acusa a cena 1 falando so' do vegetal — o caso "
                    "que o operador reprovou passa pelo medidor")

    # ⭐ [BO9] a abertura orfa — a licao §21 como controle
    s9 = dict(s, falas=list(s["falas"]))
    s9["falas"][0] = "Did you know that this happens? " + _sentencas(s["falas"][0])[-1]
    if not any("BO9" in msg for _, msg in lint(s9, b)):
        ctrl.append("[BO9] NAO acusa abertura sem referente (licoes §21)")

    # [BO11] nome cientifico
    s11 = dict(s, falas=list(s["falas"]))
    s11["falas"][1] = s11["falas"][1] + " Lepidium meyenii, to be exact."
    if not any("BO11" in msg for _, msg in lint(s11, b)):
        ctrl.append("[BO11] nao acusa nome cientifico na fala")

    # [BO10] o centimetro que o operador cortou
    s10 = dict(s, falas=list(s["falas"]))
    s10["falas"][2] = s10["falas"][2] + " Up to 5 inches in a week."
    if not any("BO10" in msg for _, msg in lint(s10, b)):
        ctrl.append("[BO10] nao acusa medida de crescimento")

    # ⚠️ O controle de BO3 saiu junto com a lente em 2026-08-05. Ele montava um
    # repertorio sem vilao e esperava reprovacao — hoje esse e' o repertorio
    # CERTO. Controle de regra aposentada que fica para tras vira ruido, e ruido
    # ensina o operador a ignorar o autoteste.

    # ⭐ [BO16] o deitico orfao — a ordem do operador em um controle
    s16 = dict(s, falas=list(s["falas"]))
    s16["falas"][0] = "If your tool looks like this one and not this one, ok."
    if not any("BO16" in msg for _, msg in lint(s16, b)):
        ctrl.append("[BO16] NAO acusa `this one` duas vezes na cena 1")
    s16b = dict(s, falas=list(s["falas"]))
    s16b["falas"][0] = "If your tool looks like that, this one is for you."
    if not any("BO16" in msg for _, msg in lint(s16b, b)):
        ctrl.append("[BO16] NAO acusa o fecho `this one is for you`")

    # ⭐⭐ [BO6] AS SONDAS DO ANGULO CERTO. As duas que estavam aqui vigiavam o
    # HOMEM MUDO do BOTICA — e a segunda apontava para `never at the camera`,
    # literal que este motor nao tem mais. Ela passava sempre, e foi ela que
    # deixou o homem do BOTICA morar na cena 3 deste agente por um dia inteiro.
    b6 = dict(b)
    b6["TAKE 03/03"] = b6["TAKE 03/03"].replace("never speaks", "also speaks")
    if not any("BO6" in msg for _, msg in lint(s, b6)):
        ctrl.append("[BO6] NAO acusa a segunda mulher sem a trava de mudez")
    # ⭐ o terceiro corpo — o defeito de verdade, plantado
    b6b = dict(b)
    b6b["IMAGE 03/03"] = b6b["IMAGE 03/03"].replace(
        "%(anti)s" % {"anti": ANTICELEB},
        "Behind them stands a 60-year-old man, his mouth open. " + ANTICELEB)
    if not any("BO6" in msg for _, msg in lint(s, b6b)):
        ctrl.append("[BO6] NAO acusa um TERCEIRO CORPO na cena 3")
    # ⭐ a ancora da segunda mulher, sem a qual o Veo a troca entre os blocos
    b6c = dict(b)
    b6c["IMAGE 03/03"] = b6c["IMAGE 03/03"].replace(
        "the same %d-year-old" % s["amiga"]["idade"], "a")
    if not any("BO6" in msg for _, msg in lint(s, b6c)):
        ctrl.append("[BO6] NAO acusa a cena 3 sem a ancora da segunda mulher")

    # [BO5] copo adiantado
    b5 = dict(b)
    b5["IMAGE 01/03"] += " " + BO_COPO
    if not any("BO5" in msg for _, msg in lint(s, b5)):
        ctrl.append("[BO5] nao acusa o copo fora da cena 3")

    # [BO4] gelatin trick fora da cena 2
    s4 = dict(s, falas=list(s["falas"]))
    s4["falas"][1] = s4["falas"][1].replace("gelatin trick", "morning routine")
    if not any("BO4" in msg for _, msg in lint(s4, b)):
        ctrl.append("[BO4] nao acusa a cena 2 sem o `gelatin trick`")

    # ⭐⭐ [PELE] A TRAVA DE PELE, MEDIDA — nao declarada. Contrato criado em
    # 2026-08-05 porque o seletor clara/escura era um botao MORTO neste motor
    # (etnia livre, vinda do mundo). Um contrato novo sem sonda e' a mesma
    # armadilha do §29: ninguem percebe quando ele para de valer.
    # ⛔ Duas invariantes, as duas cobradas em 120 sorteios por pele:
    #   1. a pele sorteada e' a pedida;
    #   2. a etnia continua vindo de DENTRO do mundo — se ela passar a sair
    #      solta para satisfazer a trava, "etnia arrasta o mundo" virou slogan.
    for _pele in ("clara", "escura"):
        # ⛔ A COBERTURA E' CHECADA ANTES DOS 120 SORTEIOS. Ao contrario, a
        # sonda gastava 120 sorteios contra uma trava impossivel e so' depois
        # reportava — e no caminho podia derrubar o proprio autoteste.
        if not [m for m in MUNDOS
                if any(_pele_de(e) == _pele for e in m["etnias"])]:
            ctrl.append("[PELE] nenhum mundo comporta %r — a trava nao tem o "
                        "que sortear e a pele vai ceder calada" % _pele)
            continue
        _fora, _solta = 0, 0
        _vistas = set()
        for _k in range(120):
            _s = sortear("joe", random.Random(_k), {}, {"pele": _pele})
            _vistas.add(_s["etnia"])
            if _pele_de(_s["etnia"]) != _pele:
                _fora += 1
            if _s["etnia"] not in _s["mundo"]["etnias"]:
                _solta += 1
        if _fora:
            ctrl.append("[PELE] trava %r furou em %d de 120 sorteios"
                        % (_pele, _fora))
        if _solta:
            ctrl.append("[PELE] a etnia saiu de FORA do mundo em %d de 120 — a "
                        "trava esta' sendo satisfeita quebrando a invariante"
                        % _solta)
        # ⛔⛔ A TERCEIRA INVARIANTE, e ela e' correcao DE CAMPO do operador
        # (2026-08-05, com print): `escura` significa NEGRO. Asiatico, latino e
        # mestico nao sao nem clara nem escura — so' saem com a pele LIVRE.
        # ⚠️ Checar so' `_pele_de(etnia) == pele` NAO pega isto: com a regra
        # binaria antiga (`clara = tem white, escura = o resto`) o Asian
        # American passava como "escura" e a sonda dizia OK. A sonda tem de
        # olhar as etnias QUE SAIRAM contra a lista explicita.
        _fora_lista = _vistas - set(PELE_ETNIAS[_pele])
        if _fora_lista:
            ctrl.append("[PELE] a trava %r devolveu etnia fora da lista: %s — "
                        "escura significa NEGRO, e neutras so' saem no livre"
                        % (_pele, ", ".join(sorted(_fora_lista))))

    # o lote limpo NAO pode ser acusado
    if [x for t, x in lint(s, b) if t == "ERRO"]:
        ctrl.append("o lote limpo esta' sendo reprovado — regra que reprova "
                    "tudo nunca foi testada")

    print("MUNDOS %d em %d familias | METODOS %d | RAROS %d | COMUNS %d | "
          "SUBSTANCIAS %d | REFS %d | HOMENS %d"
          % (len(MUNDOS), len(FAMILIAS_MUNDO), len(METODOS), len(RAROS),
             len(COMUNS), len(SUBSTANCIAS), len(REFS), len(HOMENS)))
    print("%d videos | mundos %d/%d | etnias %d | metodos %d/%d | raros %d/%d"
          % (n, len(vistos["mundo"]), len(MUNDOS), len(vistos["etnia"]),
             len(vistos["metodo"]), len(METODOS), len(vistos["raro"]),
             len(RAROS)))
    print("familia mais frequente: %s com %.1f%% | bandeira COM %.1f%%"
          % (fam.most_common(1)[0][0], 100.0 * fam.most_common(1)[0][1] / n,
             100.0 * band[True] / n))
    for i in (1, 2, 3):
        L = larguras[i]
        print("  cena %d: %d-%d palavras (media %.1f) | piso %d teto %d | %.2f p/s"
              % (i, min(L), max(L), sum(L) / float(len(L)), PISO_FALA[i],
                 TETO_FALA[i], sum(L) / float(len(L)) / 8))

    if ctrl:
        # ⛔ ASCII de proposito: o console do Windows e' cp1252.
        print("\n>> O AUTOTESTE ESTA' CEGO:")
        for c in ctrl:
            print("   %s" % c)
    if falhas:
        print("\n>> %d FALHA(S):" % len(falhas))
        for f in falhas[:20]:
            print("   %s" % f)
    if not falhas and not ctrl:
        print("\nAUTOTESTE OK — e os controles reprovam quando devem.")
    return 1 if (falhas or ctrl) else 0


def main():
    ap = argparse.ArgumentParser(description="Randomizador do agente BOTICA SHORT")
    ap.add_argument("--pagina", choices=sorted(ETNIA))
    ap.add_argument("--n", type=int, default=1)
    ap.add_argument("--seed", type=int)
    ap.add_argument("--nicho", choices=FAMILIAS_MUNDO)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--autoteste", action="store_true")
    a = ap.parse_args()
    if a.autoteste:
        return autoteste()
    if not a.pagina:
        ap.error("--pagina obrigatorio")

    seed = a.seed if a.seed is not None else random.randrange(10 ** 6)
    rng = random.Random(seed)
    led = _carregar_ledger()
    travas = {"familia_mundo": a.nicho} if a.nicho else {}

    for _ in range(a.n):
        spec = sortear(a.pagina, rng, led, travas)
        blocos = montar(spec)
        print("=" * 72)
        print("SPEC — pagina %s | seed %s" % (a.pagina, seed))
        print(resumo_pt(spec))
        print("=" * 72)
        for nome, txt in blocos.items():
            print(txt if nome.startswith("BLOCO")
                  else "\n%s\n%s" % ("-" * 72, txt))
        ach = lint(spec, blocos)
        print("\n" + "=" * 72)
        if ach:
            for tipo, msg in ach:
                print("[%s] %s" % (tipo, msg))
            print("%d achado(s)." % len(ach))
        else:
            print("LINTER: OK — nenhuma violacao mecanica.")
        if not a.dry_run:
            u = led.setdefault(a.pagina, {})
            for eixo, val in (("familia_mundo", spec["mundo"]["familia"]),
                              ("prop", spec["prop"]["id"]),
                              ("substancia", spec["substancia"]["id"]),
                              ("metodo", spec["metodo"]["id"]),
                              ("comum", spec["comum"]["id"]),
                              ("raro", spec["raro"]["id"]),
                              ("homem", spec["homem"]["id"])):
                u.setdefault(eixo, [])
                if val not in u[eixo]:
                    u[eixo].append(val)
                if len(u[eixo]) >= TETO_LEDGER[eixo]:
                    u[eixo] = [val]
    if not a.dry_run:
        _gravar_ledger(led)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
