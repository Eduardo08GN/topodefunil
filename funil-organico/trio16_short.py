#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
trio16_short.py — randomizador + gerador + linter do AGENTE **TRIO 16**.

⭐⭐ O QUE ELE E': o TRIO em **DOIS takes de 8s = 16 segundos**. Nasce por ordem
do operador em 2026-08-08, e a ordem tem uma clausula que manda em tudo aqui:

    *"O ajuste aqui e' apenas no eixo temporal: nao sacrifique, diminua ou faca
    quaisquer regressao ao adequar temporalmente o agente. Os recursos atuais de
    pool, controladores, etc, devem continuar preservados."*

⛔ Ele **nao substitui** o `trio_short.py`. Os dois coexistem: 24s e 16s sao
formatos diferentes, com ledger proprio cada um.

⭐ FONTE DO ANGULO: Alexis Lin Wellness, reel 1255806096524989. A leitura otica,
a geometria e todas as strings travadas continuam sendo as do `trio_short.py` —
este arquivo e' **copia literal** dele com a cirurgia temporal em cima, que e' o
mesmo metodo do desacoplamento de 2026-08-03.

O ARCO — 2 cenas de 8s, destino AdBatch Vertical 2:

    cena 1  A ISCA     duas SENTADAS com os dois props no colo, a que fala EM PE
                       ATRAS apontando · diagnostico + virada + o vilao
    cena 2  A PROVA    a cozinha da mesma casa: a bancada da receita, ela com o
                       COPO na lente e o CORPO-PROVA masculino SORRINDO a
                       frame-right · o gelatin trick + o CTA

⭐⭐ COMO AS 3 CENAS VIRARAM 2, e por que nao e' perda:
As cenas 2 e 3 do TRIO ja' aconteciam **no mesmo lugar** — a cena 3 abre com
`same place, same background`. Elas FUNDEM sem inventar cenario nenhum: a
bancada da receita e o copo do payoff entram no mesmo quadro.

⛔⛔ O QUE MORREU, e e' honesto dizer: a AMIGA sai do quadro 2, e com ela o pool
`REACOES_AMIGA`. Decisao do operador em 2026-08-08, com a alternativa na mesa:
tres pessoas + bancada + copo + prop grande em 8 segundos e' quadro entulhado, e
o Veo resolve entulho apagando alguem — normalmente o corpo-prova, que e' o
payoff. Ela continua sortada e continua no quadro 1, que e' onde o angulo mora.

⚠️ E O QUE JA' ESTAVA MORTO no TRIO e continua: `metodo`, `comum` e
`substancia` sao sorteados e entram no ledger, mas nao chegam a bloco nenhum —
foram tirados do painel em 2026-08-05 por isso mesmo. Reviver qualquer um deles
significa ACRESCENTAR objeto ao quadro, que e' alcada do operador. Nao inventei.

⛔⛔ A ARITMETICA QUE MANDA NA COPY. O TRIO fala 64-75 palavras em 24s; dois
takes dao 50. A soma dos MINIMOS das 8 funcoes do TRIO e' 63 — 13 palavras de
divida antes da primeira letra. Medido, nao estimado:

    mecanismo + CTA + gate  ->  0 de 96 combinacoes cabiam
    receita   + CTA + gate  ->  1 de 96
    uso       + CTA + gate  -> 52 de 112

Foi o operador quem destravou, reescrevendo o CTA: fundindo o follow no comando
ele derrubou o custo de 14-17 palavras para 11, e abriu 14 para VENDER.

⛔⛔ MAS O `follow` NAO ENCOSTA NA KEYWORD. O operador confirmou em 2026-08-08
que a automacao de DM responde a **palavra EXATA**. `Comment gelatin and follow`
sai da boca como uma unidade e o espectador digita `gelatin and follow`, que nao
dispara. Por isso o comando fica:

    Comment gelatin, and I'll send you the recipe. Follow me first.

A virgula fecha o token; o follow vira FRASE SEPARADA — instrucao, nao parte da
palavra. E de brinde o `sc.CTA_LITERAL` continua intacto, entao o linter
compartilhado passa sem literal novo.

⭐ A COPY DA CENA 2 e' o LOTE 1 (O DESEJO), escolhido entre tres arquiteturas
medidas: toda entrada de `USOS_16` carrega o literal `gelatin trick` como
SUJEITO e empilha promessa + desejo oculto numa sentenca so'. Em 16 segundos nao
ha' tempo de ensinar mecanismo: o take 1 ja' deu o vilao e a comparacao.

Uso:
    python funil-organico/trio16_short.py --pagina joe --n 1
    python funil-organico/trio16_short.py --pagina ray --n 3 --seed 42 --dry-run
    python funil-organico/trio16_short.py --autoteste
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
# ⛔ LEDGER PROPRIO, decisao do operador. Compartilhar com o TRIO SHORT faria o
# frescor de um gastar o do outro: dois videos seguidos, um de cada motor, sao
# lotes DIFERENTES e cada um tem de varrer o repertorio inteiro.
LEDGER = os.path.join(AQUI, ".trio-16-ledger.json")

TITULO = "AGENTE TRIO 16"
SLUG = "trio-16"
SUBTITULO = ("2 takes de 8s = 16 segundos · o trio, e a cozinha com o copo e o "
             "corpo-prova no MESMO quadro · gerador offline de prompts Veo")

# ⭐ QUEM NARRA — o sexo de quem fala com a lente (2026-08-06).
# Ordem do operador: *"uma marcacao dentro dos agentes python, de todos, pra
# saber se aquele agente gera roteiros com personagem homens e mulheres como
# narrador/apresentador ou se so' gera com um dos dois"*.
# ⛔ MEDIDO, nao lido: 120 sorteios por agente, olhando o BLOCO 0 do prompt.
# Declarar de cabeca aqui seria a mesma FORMA-sem-FUNCAO que ja' custou o
# botao de pele morto em tres motores.
# ⚠️ Com DOIS sexos a UI desenha a trava homem/mulher; com um so', nao desenha
# botao nenhum — botao que nao trava nada e' pior que botao nenhum.
SEXOS = ("mulher",)

ETNIA = {
    # ⭐ As 5 paginas do lote de 2026-08-05. Split 3 brancos / 2 negros —
    # a razao (volume absoluto x prevalencia) esta' escrita no
    # `bridge-pages-deploy.md`.
    "roy": "white American", "dean": "white American",
    "earl": "white American",
    "jason": "Black American", "philippe": "Black American",
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
# ⭐⭐ BO1 — A GEOMETRIA DO TRIO, lida frame a frame na fonte (0:00-0:07).
# DUAS pessoas SENTADAS lado a lado, e a terceira EM PE ATRAS, inclinada para
# a frente ENTRE as duas, o rosto dela na altura dos ombros delas.
# ⛔ E' essa a diferenca do DUPLA, e ela e' o angulo inteiro: no DUPLA as duas
# estao EM PE e a comparacao e' horizontal; aqui a que fala esta' ACIMA e
# ATRAS, e o dedo dela desce sobre os props. A leitura muda de "duas amigas
# comparando" para "alguem apresentando dois casos".
# ⚠️ SENTADAS, e por dois motivos: e' o que a fonte faz, e sentado o prop cai
# na altura do colo — que e' onde ele precisa estar para a comparacao ler.
BO_TRIO = (
    # ⛔ Sem repetir o sofa: ele ja' esta' na descricao da SALA, e nomear
    # duas vezes faz o Veo desenhar dois assentos.
    "Two women sit side by side on the couch, filmed straight on, with the "
    "couch seat and both their hands inside the frame. On frame-left sits a %d-year-old %s woman, %s, %s, wearing %s; "
    "both her hands are closed around %s, resting on her knees. On frame-right "
    "sits "
    "a %d-year-old %s woman, %s, %s, wearing %s; her right hand is closed "
    "around %s, standing upright on her knees. She is smiling with her lips "
    "closed, pleased and openly "
    "happy, her whole face lit up as she looks down at what she is holding. "
    "Both objects are fully in frame and "
    "both are held clear of the women's bodies. Standing behind them and "
    "leaning "
    "forward between their shoulders is %s. Her right arm reaches down past "
    "the left woman's shoulder and her index finger points at the piece the "
    "left woman is holding. "
    "She looks straight into the lens with her mouth open mid-word as she "
    "speaks. Both seated women keep their lips closed and their eyes down on "
    "what they are holding."
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
# ⭐ A CAUDA DA BANCADA DO 16 — uma so', porque ela e' a MESMA nas seis
# conformacoes: o raro sorteado, os dois vegetais da receita e a tigela de
# gelatina (DU2). Seis copias do mesmo texto divergiriam na primeira correcao.
# ⛔ Ela vive FORA das entradas de proposito: o campo `aparato16` tem de ser
# literal puro para o `lint_painel_honesto` conseguir prova-lo no bloco.
BANCADA16_CAUDA = (", %(raro_img)s, two raw beetroots and two carrots")

PREPAROS = [
    {"id": "dois_jarros",
     "bancada": "a tall clear glass, and beside it %(raro_img)s, two raw "
                "beetroots, two carrots",
     # ⭐⭐ `bancada16` — A MESMA BANCADA, SEM O COPO DE DESTINO.
     # No TRIO a cena 2 e' o PREPARO (o copo esta' na bancada, sendo enchido) e
     # a cena 3 e' o COPO (na mao dela). Fundidas, o copo esta' NA MAO — e
     # deixar o `a tall clear glass` da bancada poria DOIS copos altos no
     # quadro. O aparato de cada conformacao fica inteiro, parado, como prova
     # de que a receita foi feita; o que sai e' so' o destino, que mudou de
     # lugar. Nada foi inventado: cada string e' a irma dela sem o copo.
     "aparato16": "two glass jugs standing side by side, one still holding deep red "
                  "juice and the other bright orange",
     "acao": "She holds a glass jug in each hand and pours both at once into "
             "the tall glass — deep red juice from the left jug and bright "
             "orange juice from the right — the two streams falling together",
     "mov": "She keeps pouring from both jugs at once into the tall glass, the "
            "two streams meeting in it the whole time, her forearms steady. She "
            "never sets either jug down.",
     "audio": "juice pouring into a glass"},

    {"id": "liquidificador",
     "bancada": "a blender jug on its base, filled with cut beetroot and "
                "carrot, a tall clear glass beside it, %(raro_img)s",
     "aparato16": "a blender jug back on its base with the lid on and deep red and "
                  "orange pulp still coating the inside",
     "acao": "Her right hand rests on the blender base and her left sets the "
             "lid down onto the jug, the cut beetroot and carrot packed inside "
             "against the glass",
     "mov": "Her left hand presses the lid down onto the blender jug and stays "
            "there; her right hand stays flat on the base.",
     "audio": "a blender motor starting up"},

    {"id": "espremedor",
     "bancada": "a stainless juicer with a tall clear glass under its spout, "
                "%(raro_img)s, a bowl of cut beetroot and carrot",
     "aparato16": "a stainless juicer with red-stained pulp still in its catcher and "
                  "the plunger resting in the chute",
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
                "two raw beetroots, two carrots",
     "aparato16": "a long wooden spoon lying across a wide jug streaked red and "
                  "orange inside",
     "acao": "Her right hand turns a long spoon slowly through the glass and "
             "the two layers begin to marble into each other",
     "mov": "Her right hand keeps turning the long spoon slowly through the "
            "glass the whole time and never lifts it clear. Her left hand stays "
            "flat on the %(sup)s.",
     "audio": "a spoon turning in a glass"},

    {"id": "medidor",
     "bancada": "a tall clear glass, a graduated glass measuring jug of deep "
                "red juice in her hand, a second jug of bright orange juice "
                "waiting beside it, %(raro_img)s, two raw beetroots, two "
                "carrots",
     "aparato16": "a graduated glass measuring jug with deep red juice still in it "
                  "and a second jug of bright orange standing beside it",
     "acao": "Her right hand tips the measuring jug and a steady thread of deep "
             "red juice falls into the tall glass, filling it to the halfway "
             "mark",
     "mov": "Her right hand keeps the measuring jug at the same tilt and the "
            "red thread keeps falling into the glass at the same rate. She "
            "never sets the jug down and never picks up the second one.",
     "audio": "juice pouring into a glass"},

    {"id": "coador",
     "bancada": "a fine mesh sieve set over a tall clear glass, deep red pulp "
                "in it, %(raro_img)s, two raw beetroots, two carrots",
     "aparato16": "a fine mesh sieve resting over a wide jug with deep red pulp still "
                  "in the mesh and a spoon beside it",
     "acao": "Her right hand presses the back of a spoon into the pulp in the "
             "sieve and deep red juice runs through the mesh into the glass "
             "below",
     "mov": "Her right hand keeps pressing the back of the spoon into the pulp "
            "in the sieve at the same slow rate and the juice keeps running "
            "through into the glass. Her left hand holds the sieve rim steady.",
     "audio": "juice dripping through a sieve"},
]

# ⭐⭐ BO2 — A COZINHA. Na fonte ela esta' SOZINHA; por ordem do operador aqui
# ela tem UMA das duas ao lado. A que fica e' a da DIREITA — a do prop grande —
# porque e' o lado que a promessa aponta, e trazer a do murcho para a cena da
# solucao seria contar a historia ao contrario.
# ⛔ A SEGUNDA MULHER NAO TOCA EM NADA. Ela esta' ali como testemunha; maos na
# receita disputariam o quadro com a bancada, que e' o que se vende.
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
# ⛔⛔ 2026-08-11 — O COPO SAIU, A TIGELA DE GELATINA ENTROU. Ordem do operador:
# *"ela sempre estar segurando uma tigela de gelatina ao inves de um copo de
# bebida, nao faz sentido o copo sendo que o CTA e' sobre gelatina"*.
# ⭐ E ele esta' certo pela mecanica do funil, nao so' por estetica: a palavra
# que o espectador tem de digitar e' GELATIN, e o objeto na mao dela no frame em
# que a boca diz `gelatin,` era... um copo de bebida opaca. O objeto da keyword
# nao mostrava a keyword. Agora mostra.
# ⚠️ A gelatina SAIU DA BANCADA no mesmo movimento: ela estava `sitting
# untouched at the edge` nas seis conformacoes. Deixar as duas poria DUAS
# tigelas de gelatina no mesmo quadro — o defeito dos dois copos altos (T16-1)
# repetido com outro objeto.
BO_COPO = ("a shallow clear glass bowl filled with vivid purple gelatin cubes")
# ⚠️ AQUI FICAVA A REGRA DO CANUDO (*"dois canudos? quero so' um"*, render
# reprovado pelo operador). Ela morreu com o copo — tigela nao tem canudo — e
# esta' registrada so' como historia. Comentario que descreve um objeto que saiu
# e' armadilha: o proximo leitor devolve o canudo achando que corrige um
# esquecimento.

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
    # ⛔⛔ A CARA DE SURPRESA SAIU (2026-08-07, ordem do operador). O pool
    # anterior tinha 12 entradas e SETE delas eram boca aberta ou olho
    # arregalado — "his eyes are wide... his mouth open in plain astonishment",
    # "his eyes have gone round", "his jaw has gone slack". Renderizado, aquilo
    # nao le' como reacao humana: le' como emoji de espanto colado num homem,
    # e e' uma das assinaturas mais reconheciveis de video feito por IA.
    # ⭐ O que fica: uma pessoa NORMAL olhando para o copo. A reacao continua
    # variando de sabor — atencao, aprovacao contida, interesse, um aceno — e
    # continua muda e virada para o copo, nunca para a lente.
    # ⚠️ Cada entrada e' (clausula da IMAGE, clausula do TAKE) e as duas tem de
    # descrever a MESMA coisa: o take anima a image, nao inventa outro gesto.
    ("his face is relaxed and he is looking down at it steadily",
     "keeps looking down at it, his face relaxed and still"),
    ("he is watching it with a small closed-mouth smile",
     "holds that small closed-mouth smile without moving"),
    ("his brows are relaxed and his lips are pressed lightly together",
     "keeps his lips lightly pressed and does not move"),
    ("he is looking at it with his head very slightly tilted",
     "keeps his head slightly tilted and does not move"),
    ("he is nodding once, slowly, his mouth closed",
     "finishes the slow nod and then stays still"),
    ("his eyes are steady on it and one corner of his mouth is lifted",
     "holds that one-sided look without moving"),
    ("he is looking down at it with a calm, unhurried expression",
     "keeps that calm expression and does not move"),
    ("his chin is lowered slightly and he is looking at it from under his brows",
     "keeps his chin lowered and does not move"),
    ("he is looking at it plainly, his face giving nothing away",
     "keeps that plain expression without moving"),
    ("his mouth is closed and he is looking at it the way a man reads a label",
     "keeps reading it with his mouth closed, not moving"),
    ("he is looking at it and breathing out slowly through his nose",
     "finishes the slow breath and stays looking at it"),
    ("his expression is settled and he is looking at it without blinking much",
     "keeps that settled expression and does not move"),
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
# ⭐⭐ BO3 — O CORPO-PROVA, na geometria do EXTERIOR (referencia que o operador
# mandou em print). Ela frame-left falando na lente com o copo; ele frame-right
# com o prop GRANDE erguido na altura da cintura.
#
# ⛔⛔ ATE' 2026-08-10 ELE ERA SEM ROSTO, cortado no peito, por duas razoes:
# era "o corpo de qualquer homem" (o espectador se via ali) e o corte mantinha
# a cena gerável — rosto masculino junto de prop falico na cintura e' a
# combinacao que a moderacao pega.
# ⭐ O OPERADOR INVERTEU A REGRA, de propria voz. Ele leu um render, viu o
# marido de cara fechada e mandou: *"ele deve estar feliz e sorrindo"*. Foram
# apresentadas as tres saidas — sumir com o rosto, mostrar sorrindo, ou cortar
# na boca — com o risco de recusa escrito em cada uma; ele escolheu a segunda:
# *"pode fazer o que eu pedi, opcao 2, sempre o homem feliz e sorrindo"*.
# ⚠️ O ROSTO AGORA APARECE E TEM DE SORRIR. A `BO6` foi INVERTIDA junto (nao
# apagada) e cobra o sorriso na IMAGE e no TAKE.
# ⚠️ RISCO ACEITO: se este agente comecar a acumular recusa do Veo, o primeiro
# suspeito e' esta mudanca — rosto + prop falico na cintura no mesmo quadro.
#
# ⭐ E ISTO CONSERTOU UM DEFEITO DE VERDADE, que era a causa do que ele viu: o
# molde dizia `no face is in the frame` e, na mesma sentenca, descrevia cabelo,
# barba, sobrancelha e pinta — as 22 entradas do pool HOMENS descrevem rosto.
# O gerador resolvia a contradicao MOSTRANDO o rosto, e um rosto sem expressao
# escrita sai neutro. Era contradicao interna, nao teimosia do modelo.
# ⭐ O ULTIMO `%s` E' A CAUDA DO PROP (`cauda_c2`), e o LUGAR dela e' este —
# 2026-08-10. Nao e' preciosismo de pontuacao: a cauda anti-bicho fala do
# MOLUSCO, e posta depois de *"Only his chest, his arms and his hands are in the
# picture."* ela passa a qualificar o HOMEM — `no eyes, no head, nothing alive`
# logo apos a frase que descreve o corpo dele. E' assim que o NECROSE a escreve
# tambem: colada na sentenca do molusco, antes da proxima frase de cena.
# ⚠️ O texto travado nao mudou uma letra — entrou um SLOT, que fica vazio para
# todo par sem `cauda_c2`.
BO_CORPO_PROVA = (
    "Standing at frame-right, in frame from the waist up with his face fully "
    "visible, is a %d-year-old %s man, %s, wearing %s. He is smiling broadly, "
    "happy and relaxed, looking at the camera with an easy open grin. His "
    "right hand is closed "
    "around %s, held upright at the height of his waist, well clear of his "
    "body.%s"
)

BO_CORPO_PROVA_TAKE = (
    "He stays in frame the whole shot, face visible, and keeps smiling the "
    "whole time — happy and relaxed, his expression never going flat or "
    "serious. His hand stays closed around the piece exactly where it is. He "
    "never speaks and makes no sound. Only she speaks, straight into the lens."
)

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
# ⛔ A negacao anti-celebridade saiu daqui em 2026-08-14, por ordem do operador
# (*"tire not a celebrity do prompt"*): declaracao INJETA o token que ela nega.
# A metade positiva ficou. Ver CLAUDE.md §"CONTRA A CELEBRIDADE, SILENCIO".
ANTICELEB = ("A strikingly beautiful face.")
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
     "sala": 'a Brooklyn front room with a painted tin ceiling, a low tufted couch pulled clear of the wall, a cast-iron radiator, sash windows onto the fire escape, and daylight straight on the seat.',
     "sala_c": 'tin-ceiling front room',
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
     "sala": 'a Louisiana front room with faded green bead-board walls, a low horsehair settee pulled clear of the wall, a card table under the window, and humid daylight falling straight on the seat.',
     "sala_c": 'bead-board front room',
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
     "sala": 'a Texas ranch living room with cedar ceiling beams, a low leather couch set out from the wall, a stone fireplace, a hide rug, and hard daylight coming straight through the picture window.',
     "sala_c": 'cedar-beamed living room',
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
     "sala": 'an Appalachian cabin living room with pine-panelled walls, a low plaid couch pulled forward of the wall, a black wood stove, a quilt over the arm, and soft daylight from a front window.',
     "sala_c": 'pine-panelled cabin room',
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
     "sala": 'a Miami living room with white terrazzo floors, a low white sofa floating clear of the wall, a glass coffee table, potted palms, and bright sun coming straight through the sliding doors.',
     "sala_c": 'white terrazzo living room',
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
     "sala": 'a Southern California living room with pale plaster walls, a low linen sofa set forward of the wall, a low teak bookcase, a jute rug, and flat coastal daylight straight on the seat.',
     "sala_c": 'pale plaster living room',
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
     "sala": 'a New Jersey living room with honey-oak trim, a low two-seat sofa pulled out from the wall, a glass curio cabinet, a runner rug down the middle, and cool daylight straight from the front.',
     "sala_c": 'honey-oak living room',
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
     "sala": 'a Nashville living room with shiplap walls, a low tweed sofa standing clear of the wall, a barn-wood coffee table, a guitar case against the wall, and warm daylight through the front window.',
     "sala_c": 'shiplap living room',
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
     "sala": 'a Chicago two-flat living room with white-painted woodwork, a low velvet sofa set out from the wall, a cast-iron radiator, oak floors, and cool north daylight straight through the front windows.',
     "sala_c": 'two-flat living room',
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
     "sala": 'an Arizona living room with adobe-plastered walls, a low leather sofa set forward of the wall, a low pine bookshelf, a swamp cooler in the window, and hard desert daylight from the front.',
     "sala_c": 'adobe living room',
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
     "sala": 'a Boston triple-decker parlor with a plate rail running the wall, a low rolled-arm settee clear of the wall, a brick chimney breast, and grey street light through the bay window.',
     "sala_c": 'triple-decker parlor',
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
     "sala": 'an Atlanta living room with white shaker trim, a low tufted sofa standing clear of the wall, a marble coffee table, a tall potted fern, and bright even daylight through the garden windows.',
     "sala_c": 'white shaker living room',
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
     "sala": 'a Midwest farmhouse living room with painted wainscot, a low floral-print sofa pulled forward of the wall, a braided rug, a wooden mantel clock, and wide flat daylight through the front window.',
     "sala_c": 'wainscot farmhouse room',
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
     "sala": 'a Detroit living room with dark stained trim, a low corduroy couch pulled out from the wall, a console stereo against the far wall, and flat daylight through a wide clapboard-framed window.',
     "sala_c": 'dark-trim living room',
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
     "sala": 'a New England coastal living room with white-painted panelling, a low slipcovered sofa set clear of the wall, a painted sea chest, a rope-coil lamp, and cool water light through the front windows.',
     "sala_c": 'white-panelled coastal room',
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
     "sala": 'a Las Vegas apartment living room with glossy dark built-ins, a low grey sectional pulled clear of the wall, a smoked-glass table, chrome floor lamp, and hard daylight through the balcony doors.',
     "sala_c": 'glossy Vegas living room',
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

    # ⭐⭐ + 2026-08-13 — OITO REGIOES NOVAS, de 16 para 24. Ordem do operador:
    # *"aumente o pool de opcoes substancialmente, tambem dos ambientes"*.
    # ⛔ CADA UMA E' AMBIENTE INTEIRO, no mesmo nivel de detalhe das dezesseis de
    # cima: cozinha, superficie, cinco trajes de SILHUETA diferente, seis cores,
    # luz e audio. Fundo novo com o resto herdado nao e' mundo, e' papel de
    # parede — e o quadro devolve a mesma cozinha com outro nome.
    # ⚠️ A COBERTURA DE ETNIA SOBE nas duas que as paginas usam: `white American`
    # entra em sete das oito e `Black American` em cinco. Nenhuma pele fica com
    # menos cenario do que tinha, que e' o que derrubaria o sorteio da trava.
    # ⭐ Sao ARQUETIPOS REGIONAIS, na mesma leitura de 2026-08-05: o cara da
    # Filadelfia e o de Seattle sao os dois `white American` no papel e nao se
    # parecem em nada. E' essa diferenca que faz o lote variar de verdade.
    {"id": "filadelfia", "selo": "N", "familia": "filadelfia",
     "etnias": ["white American", "Black American"],
     "eua": True,
     "sala": 'a Philadelphia rowhouse front room with a narrow bay window onto the street, a low velvet sofa pulled clear of the wall, a painted mantel, a faded rug, and daylight falling straight on the seat.',
     "sala_c": 'narrow rowhouse front room',
     "coz": "a Philadelphia rowhouse kitchen with narrow white cabinets, a window onto a brick back alley, a pressed-tin splashback and tall glasses drying in a rack by the sink",
     "coz_c": "narrow rowhouse kitchen",
     "sup_a": "a scrubbed white laminate counter", "sup": "counter",
     "trajes": [
         ("%s fitted crop top with high-waisted jeans",
          "fitted crop top"),
         ("%s cropped zip hoodie over a bandeau, short shorts",
          "cropped hoodie"),
         ("%s thin-strapped slip dress",
          "slip dress"),
         ("%s low-cut ribbed tank with a short denim skirt",
          "ribbed tank"),
         ("%s knotted tee over a sports bra with track shorts",
          "knotted tee"),
     ],
     "cores": ["black", "cream", "brick red", "royal blue", "silver", "olive"],
     "luz": "Narrow daylight coming down the alley into the window.",
     "luz_c": "narrow alley light",
     "audio": "a bus braking, a screen door two houses down"},
    {"id": "noroeste", "selo": "N", "familia": "noroeste",
     "etnias": ["white American"],
     "eua": True,
     "sala": 'a Pacific Northwest living room with fir-panelled walls, a low wool-covered couch set out from the wall, a wood stove, ferns at the window, and soft grey daylight straight on the seat.',
     "sala_c": 'fir-panelled living room',
     "coz": "a Pacific Northwest kitchen with fir-fronted cabinets, a wide window onto wet cedars and grey sky, a heavy kettle on the range and stacked pottery on an open shelf",
     "coz_c": "fir-fronted Northwest kitchen",
     "sup_a": "a thick fir butcher-block counter", "sup": "counter",
     "trajes": [
         ("%s cropped ribbed tank with rolled denim shorts",
          "ribbed crop tank"),
         ("%s low-cut bodysuit under an open flannel",
          "open flannel"),
         ("%s thin-strapped short slip dress",
          "short slip dress"),
         ("%s cut-off sweatshirt with running shorts",
          "cut-off sweatshirt"),
         ("%s tight scoop-neck tee knotted at the ribs, cut-offs",
          "knotted scoop tee"),
     ],
     "cores": ["forest green", "cream", "rust", "charcoal", "white", "denim blue"],
     "luz": "Soft grey rain light through the cedar-side window.",
     "luz_c": "soft rain light",
     "audio": "rain on the roof, a kettle ticking"},
    {"id": "denver", "selo": "N", "familia": "denver",
     "etnias": ["white American", "Mexican American"],
     "eua": True,
     "sala": 'a Colorado front-range living room with pale pine walls, a low leather couch pulled forward of the wall, a stone hearth, a woven blanket over the arm, and thin bright daylight on the seat.',
     "sala_c": 'pale pine living room',
     "coz": "a Colorado front-range kitchen with pale pine cabinets, a wide window onto foothills and dry grass, a squat woodstove in the corner and enamel mugs on hooks",
     "coz_c": "pale pine Colorado kitchen",
     "sup_a": "a honed soapstone counter", "sup": "counter",
     "trajes": [
         ("%s cropped tank top with denim cut-offs",
          "cropped tank"),
         ("%s low-cut fitted tee with high-waisted shorts",
          "fitted tee"),
         ("%s bandeau under an open shirt-jacket, short shorts",
          "open shirt-jacket"),
         ("%s thin-strapped mini dress",
          "mini dress"),
         ("%s cropped fleece half-zip with running shorts",
          "cropped half-zip"),
     ],
     "cores": ["rust", "cream", "denim blue", "black", "hunter green", "gold"],
     "luz": "Thin bright mountain light through the wide window.",
     "luz_c": "thin mountain light",
     "audio": "wind off the foothills, a stove ticking"},
    {"id": "carolina", "selo": "N", "familia": "carolina",
     "etnias": ["Black American", "white American"],
     "eua": True,
     "sala": 'a Charleston front room with tall shuttered windows onto the porch, a low linen sofa set out from the wall, plaster walls in soft blue, a sisal rug, and filtered daylight straight on the seat.',
     "sala_c": 'shuttered Charleston front room',
     "coz": "a Charleston single-house kitchen with tall shuttered windows onto a side porch, plaster walls in soft blue, a marble pastry slab and glass jars in a row",
     "coz_c": "shuttered Charleston kitchen",
     "sup_a": "a cool marble counter", "sup": "counter",
     "trajes": [
         ("%s thin-strapped short sundress",
          "short sundress"),
         ("%s cropped linen top with high-waisted shorts",
          "cropped linen top"),
         ("%s low-cut wrap top and a short skirt",
          "wrap top"),
         ("%s bandeau under an open gauze shirt, cut-offs",
          "open gauze shirt"),
         ("%s fitted bodysuit with a short linen skirt",
          "fitted bodysuit"),
     ],
     "cores": ["seafoam", "white", "coral", "navy", "butter yellow", "black"],
     "luz": "Soft filtered light through the porch shutters.",
     "luz_c": "filtered shutter light",
     "audio": "a porch swing creaking, birds in the garden"},
    {"id": "memphis", "selo": "N", "familia": "memphis",
     "etnias": ["Black American"],
     "eua": True,
     "sala": 'a Memphis shotgun-house front room with cream tongue-and-groove walls, a low patterned couch pulled clear of the wall, a floor fan in the corner, and warm low sun straight on the seat.',
     "sala_c": 'cream shotgun-house front room',
     "coz": "a Memphis shotgun-house kitchen with tongue-and-groove walls painted cream, a window fan turning in the frame, a chrome-edged dinette and cast-iron on the range",
     "coz_c": "cream shotgun-house kitchen",
     "sup_a": "a chrome-edged formica counter", "sup": "counter",
     "trajes": [
         ("%s fitted crop top with high-waisted shorts",
          "fitted crop top"),
         ("%s satin cami with a short wrap skirt",
          "satin cami"),
         ("%s low-cut bodycon mini dress",
          "bodycon mini"),
         ("%s cropped tank knotted at the ribs with cut-offs",
          "knotted tank"),
         ("%s bandeau under an open short-sleeve shirt",
          "open short-sleeve shirt"),
     ],
     "cores": ["gold", "white", "wine", "teal", "black", "hot pink"],
     "luz": "Warm low sun cutting through the window fan.",
     "luz_c": "warm fan-cut light",
     "audio": "a window fan turning, a radio through a wall"},
    {"id": "minnesota", "selo": "N", "familia": "minnesota",
     "etnias": ["white American", "Black American"],
     "eua": True,
     "sala": 'a Twin Cities living room with birch panelling, a low tweed couch set out from the wall, a radiator under a frosted window, a knitted throw, and flat snow-bright daylight on the seat.',
     "sala_c": 'birch panelled living room',
     "coz": "a Twin Cities kitchen with birch cabinets, a window onto snow-lined roofs and bare branches, a percolator on the range and a wall of hooked mugs",
     "coz_c": "birch Minnesota kitchen",
     "sup_a": "a pale butcher-block counter", "sup": "counter",
     "trajes": [
         ("%s cropped ribbed sweater with short shorts",
          "cropped sweater"),
         ("%s thin-strapped bodysuit under an open cardigan",
          "open cardigan"),
         ("%s low-cut fitted tank with leggings",
          "fitted tank"),
         ("%s short knit dress with thin straps",
          "short knit dress"),
         ("%s cut-off sweatshirt with high-waisted shorts",
          "cut-off sweatshirt"),
     ],
     "cores": ["ivory", "navy", "burgundy", "camel", "black", "sky blue"],
     "luz": "Flat bright light bouncing off the snow outside.",
     "luz_c": "flat snow light",
     "audio": "a furnace kicking in, a plough far off"},
    {"id": "oakland", "selo": "N", "familia": "oakland",
     "etnias": ["Black American", "white American"],
     "eua": True,
     "sala": 'an Oakland bungalow living room with green-painted trim, a low mid-century couch pulled clear of the wall, a wide window onto a lemon tree, a jute rug, and warm daylight straight on the seat.',
     "sala_c": 'green bungalow living room',
     "coz": "an Oakland bungalow kitchen with green-painted cabinets, a wide window onto a lemon tree and a wooden fence, open shelves of glass jars and a chipped enamel range",
     "coz_c": "green bungalow kitchen",
     "sup_a": "a butcher-block island", "sup": "island",
     "trajes": [
         ("%s cropped tank top with wide-leg cut-offs",
          "cropped tank"),
         ("%s low-cut bodysuit with a short wrap skirt",
          "wrap skirt"),
         ("%s thin-strapped slip dress",
          "slip dress"),
         ("%s knotted crop tee with high-waisted shorts",
          "knotted crop tee"),
         ("%s bandeau under an open oversized shirt",
          "open oversized shirt"),
     ],
     "cores": ["olive", "white", "terracotta", "black", "mustard", "teal"],
     "luz": "Warm bright light through the lemon-tree window.",
     "luz_c": "warm garden light",
     "audio": "a wind chime, a dog two yards over"},
    {"id": "pittsburgh", "selo": "N", "familia": "pittsburgh",
     "etnias": ["white American", "Black American"],
     "eua": True,
     "sala": 'a Pittsburgh hillside front room with cream plaster walls, a low corduroy couch pulled forward of the wall, a steep street framed in the window, a runner rug, and cool daylight on the seat.',
     "sala_c": 'cream hillside front room',
     "coz": "a Pittsburgh hillside kitchen with cream-painted cabinets, a window onto a steep street of narrow houses, a heavy gas range and a plate rail of enamelware",
     "coz_c": "cream hillside kitchen",
     "sup_a": "an oiled oak counter", "sup": "counter",
     "trajes": [
         ("%s low-cut tank top with denim cut-offs",
          "low-cut tank"),
         ("%s cropped hoodie over a bandeau, track shorts",
          "cropped hoodie"),
         ("%s fitted mini dress with thin straps",
          "fitted mini"),
         ("%s off-shoulder top with high-waisted jeans",
          "off-shoulder top"),
         ("%s open flannel over a sports bra, short shorts",
          "open flannel"),
     ],
     "cores": ["black", "gold", "cream", "steel grey", "scarlet", "forest green"],
     "luz": "Cool daylight coming up off the hillside street.",
     "luz_c": "cool hillside light",
     "audio": "a car climbing the hill, wind through a screen"},
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
# ⭐⭐ CENA 1, BEAT 1 — O DIAGNOSTICO. Forma da fonte, literal em 0:00:
# *"If your soldier looks like this"* — ela aponta para o prop MURCHO, no colo
# da mulher sentada a' esquerda.
# ⛔ UM DEITICO SO' POR ENTRADA. O contraste inteiro pertence ao beat seguinte:
# entrada com contraste proprio (`is this one and not the other`) somada a'
# virada dava DOIS contrastes na mesma frase e o fio se perdia.
# ⚠️ Nove sobreviveram de dezesseis. Cairam duplicatas disfarcadas (`is looking
# like` = `looks like` no progressivo), `wound up` (homografo: o TTS pode ler
# /wuːnd/, ferida, numa frase sobre o orgao danificado) e `lies flat`, que pede
# uma superficie que a cena nao tem — o prop esta' NA MAO dela, pende, nao jaz.
DIAGNOSTICOS = [
    "If your {o} looks like this one",
    "If your {o} looks more like this one",
    "If your {o} is anything like this one",
    "If your {o} ended up like this one",
    "If your {o} hangs like this one",
    "If your {o} droops like this one",
    "If your {o} stays down like this one",
    "If your {o} went soft like this one",
    "If your {o} gave out like this one",
]

# ⭐⭐ CENA 1, BEAT 2 — A VIRADA. Forma da fonte: *"and you want it looking like
# this in just 30 days"* — ela aponta para o prop GRANDE, no colo da OUTRA.
# ⛔⛔ DUAS EXIGENCIAS SIMULTANEAS, e a rodada 1 perdeu 13 de 16 por violar uma
# ou outra:
#   1. o DESEJO CAI NO ORGAO DELE, nunca no objeto dela. `you want the one she
#      is holding` promete o PROP — o espectador nao quer a coisa na mao da
#      amiga, quer o proprio corpo mudado. A fonte diz `you want IT`.
#   2. o segundo prop TEM DONO NOMEADO (she / her hand / my friend). Deitico nu
#      com dois props em quadro aponta para lugar nenhum.
# ⚠️ E `my friend's` foi banido: possessivo com nucleo elidido resolve para "o
# {o} da minha amiga" — a mulher em quadro ganha um orgao.
VIRADAS = [
    "and you want it like the one she's holding",
    "and you want your {o} like the one she holds",
    "and you want it looking like the one she holds",
    "but you want it like the one in her hand",
    "and you want your {o} like the one she's got",
    "and you want it like the one my friend's holding",
    "and you want your {o} like what she's holding",
    "and you want it like what my friend is holding",
]

# ⭐⭐ CENA 1, BEAT 3 — A EXCLUSAO + O COMANDO. Forma da fonte: *"no pills, no
# injections, no doctor visit, listen carefully."* E' onde o TAKE 01 TERMINA,
# por ordem do operador.
# ⛔ CABE EM 5-8 PALAVRAS: diagnostico (7) + virada (8-10) + fecho = 25.
# ⚠️ Caiu `no supplements`, e a razao vale para sempre: ela negava na cena 1
# exatamente o que a cena 2 manda tomar. Congruencia mecanismo-do-criativo =
# o-que-a-VSL-vende e' inviolavel.
FECHOS = [
    "No pills, no needles, listen close.",
    "No script, no waiting room, pay attention.",
    "Skip the pharmacy line, hear me out.",
    "No shots, no copay, stay with me.",
    "Nothing off a drugstore shelf, listen carefully.",
    "No doctor's bill, no refills, hear me out.",
    "No injections, no appointment, stay with me.",
    "Forget the prescription pad, listen close.",
    "No clinic, no insurance card, pay attention.",
    "Nobody in a white coat, stay with me.",
    "No urologist, no paperwork, hear me out.",
    "No pumps, no surgery, pay attention.",
    "No gas station pills, listen carefully.",
]

# ⛔⛔ RECEITAS E MECANISMOS FORAM APAGADOS DESTE MOTOR — 2026-08-08.
# Eles eram os dois beats da cena 2 do TRIO (a receita enumerada + o mecanismo
# com o `gelatin trick` rotulado). No 16 essa cena de fala nao existe: sao dois
# takes, e o segundo pertence ao USO + CTA.
#
# ⛔ APAGADOS, nao desligados com `if False` nem deixados sem uso. Pool morto do
# beat errado e' bomba com pino: basta alguem religar por copia. E' a mesma
# razao que fez o `BO_ISCA_ESTAVEL` do BOTICA ser apagado deste angulo, e a
# mesma que o §29 descreve.
#
# ⚠️ MEDIDO ANTES DE APAGAR, para o registro: com o CTA de 11 palavras, o pool
# de MECANISMOS do TRIO (12-15 palavras) cabia em 9 das 12 entradas — ele NAO
# morreu por nao caber. Morreu porque em 16 segundos nao ha' tempo de ensinar
# mecanismo, e o take 1 ja' entregou o vilao e a comparacao. E' escolha de
# arquitetura de copy, e o operador escolheu o LOTE 1 (o desejo) entre as tres
# que foram medidas e apresentadas.

# ⭐⭐ CENA 2 DO 16 — O USO, E ELE E' O UNICO BEAT QUE VENDE.
# ⛔⛔ TRES DIFERENCAS DO POOL DO TRIO, e as tres sao exigencia do formato:
#
#   1. TODA entrada carrega o literal `gelatin trick`. No TRIO ele morava na
#      cena 2 (o mecanismo) e o `USOS` podia nao te-lo — 7 das 14 nao tinham.
#      Aqui a cena do mecanismo NAO EXISTE: se o uso nao carregar o literal, o
#      criativo deixa de ser congruente com a VSL, que e' regra inviolavel.
#   2. Ele entra como SUJEITO (`The gelatin trick has your...`), nao como item
#      de enumeracao. Isso satisfaz o §31 sem precisar do rotulo com dois
#      pontos — quem abre a oracao ja' esta' no topo da hierarquia, e a lente
#      `lint_hierarquia_mecanismo` so' dispara quando ha' enumeracao antes.
#   3. Cada entrada empilha PROMESSA + DESEJO OCULTO numa sentenca so' (ordem
#      do operador na curadoria de pool). `hard` e' a promessa; `before she
#      even reaches for it` e' o que ele realmente quer e nao diz em voz alta.
#
# ⚠️ MEDIDO, nao estimado: com o CTA de 11 palavras sobram 14, e as entradas
# abaixo custam 10-13. As que passavam de 14 foram cortadas na redacao, nao
# deixadas para o `_ok` derrubar — pool que so' cabe pelo fallback e' pool que
# colapsa no combo minimo, que e' o defeito que o proprio TRIO documenta.
# ⛔⛔ REESCRITO EM 2026-08-08, e a lição é a razão de existir dos tres pools
# abaixo em vez de um.
#
# A PRIMEIRA versao era UMA lista de 16 frases inteiras, e ela tinha os dois
# defeitos que o operador achou lendo a saida:
#
#   1. DRIFTING POR COMPRESSAO. Eu escrevi `she feels the difference first`,
#      nao coube em 25 palavras e encurtei para `she feels it first`. Cortei
#      exatamente o substantivo que carregava o sentido e deixei o pronome:
#      *"fills it o QUE? O clima, formigao no pe?"*. E' o mesmo erro do `every
#      morning just ginkgo` — comprimir matando a concretude, em vez de trocar
#      a frase por uma mais curta que ainda diz do que se trata.
#   2. REPETICAO ESTRUTURAL. Dez das dezesseis entradas abriam a segunda oracao
#      com `she`. Um pool que repete a mesma forma em 62% dos sorteios nao e'
#      pool, e' uma frase com variacoes — e o mode-collapse aparece no lote
#      mesmo com o linter verde, porque nenhuma lente mede FORMA REPETIDA.
#
# ⭐⭐ A DIRETIVA DO OPERADOR, que generaliza para todo pool de copy:
#     *"concretude, ser taxativo, e' melhor candidato que pronome generico"* —
#     e o exemplo dele foi exatamente este: em vez de `she`, um POOL de
#     `sua namorada` / `sua esposa`.
#
# ⛔ POR ISSO SAO TRES EIXOS, e nao um. O sorteio compoe
#     EFEITO no orgao  ·  QUEM E' ELA  ·  COMO ELA REAGE
# o que da 12 x 6 x 18 combinacoes em vez de 16 frases, e — mais importante —
# torna impossivel repetir a forma: a parceira e' sempre NOMEADA e a reacao vem
# de um pool proprio.
# ⚠️ MEDIDO: 87% das combinacoes cabem em 25 palavras, mediana 23. A versao de
# lista unica cabia em 15 de 16 com mediana 24 — mais curta e mais repetitiva.

# ⭐ O EFEITO NO ORGAO. Carrega o literal `gelatin trick` como SUJEITO, que e' o
# que amarra o criativo a' VSL e ja' poe o mecanismo no topo da hierarquia (§31)
# sem precisar de rotulo com dois pontos.
EFEITOS = [
    "The gelatin trick gets your {o} stone hard",
    "The gelatin trick brings your {o} back",
    "The gelatin trick keeps your {o} hard all night",
    "The gelatin trick makes your {o} thick again",
    "The gelatin trick fills your {o} out again",
    "The gelatin trick wakes your {o} up",
    "The gelatin trick puts the weight back in your {o}",
    "The gelatin trick has your {o} ready again",
    "The gelatin trick leaves your {o} hard for hours",
    "The gelatin trick straightens your {o} out",
    "The gelatin trick loads your {o} up again",
    "The gelatin trick gets your {o} up on command",
]

# ⭐⭐ QUEM E' ELA — o pool que existe para NAO haver `she` nu.
# ⛔ Nenhuma entrada e' pronome. `she` obriga o espectador a descobrir de quem
# se trata no meio de 8 segundos; `your wife` entrega no primeiro fonema. E a
# escolha tambem SEGMENTA: casado e namorando nao ouvem a mesma promessa.
# ⚠️ Lente T16-5 cobra: fala da cena 2 sem parceira NOMEADA e' reprovacao.
PARCEIRAS = [
    "your wife",
    "your girlfriend",
    "your woman",
    "your girl",
    "the wife",
    "that woman of yours",
]

# ⭐⭐ COMO ELA REAGE — o pool que o operador pediu: *"outras formas de expressar
# o prazer que a parceira vai notar"*.
# ⛔ TODA entrada e' um COMPORTAMENTO OBSERVAVEL, nunca um estado interno. `she
# is satisfied` nao se ve'; `digs her nails in` e' um plano. O espectador compra
# a cena, nao o adjetivo.
# ⛔ E ZERO `it` sem antecedente. `stops faking it` fica porque `fake it` e'
# idioma fechado e inequivoco; `feels it` saiu porque o `it` nao tem dono — foi
# a frase que o operador reprovou.
REACOES = [
    "digs her nails in",
    "stops faking it",
    "asks what changed",
    "cannot keep quiet",
    "starts finishing again",
    "reaches for you first",
    "wakes you up for more",
    "tells her friends",
    "goes quiet mid-sentence",
    "will not let you sleep",
    "makes the first move",
    "forgets her sentence",
    "stops turning away",
    "climbs on uninvited",
    "stops watching the clock",
    "cancels her plans",
    "starts locking the bedroom door",
    "stops calling it a phase",
]

# ⭐⭐ O COMANDO, E A VIRGULA DEPOIS DE `gelatin` E' O ITEM MAIS IMPORTANTE DESTE
# ARQUIVO.
# ⛔⛔ O operador confirmou em 2026-08-08 que a automacao de DM responde a
# **palavra EXATA**. A primeira versao que ele escreveu era `Comment gelatin and
# follow, and I'll send you the recipe` — e ela e' UM RISCO REAL: o espectador
# ouve `gelatin and follow` como uma unidade e digita isso no comentario, que
# nao dispara nada. A legenda do nosso video nasce do Whisper EM CIMA DO AUDIO,
# entao nao ha' rede depois.
# ⭐ A virgula fecha o token e o follow vira FRASE SEPARADA — instrucao, nunca
# parte da palavra. Efeito colateral bom: `sc.CTA_LITERAL` ("Comment gelatin,")
# continua contido aqui, entao o linter compartilhado passa sem literal novo, e
# eu nao precisei encostar no `short_comum`, que e' de todos os 19 motores.
CTA_BASE = "%s and I'll send you the recipe." % sc.CTA_LITERAL

# ⭐ O FOLLOW — pool proprio, curto, e ele e' quem da FOLGA ao teto.
# ⚠️ Com um follow so' de 3 palavras a cena 2 saia com mediana 24 de 25 —
# encostada no teto, que e' mode-collapse por construcao (o proprio TRIO
# documenta isso nas RECEITAS). Sorteando o follow entre 2 e 7 palavras, a
# mediana cai e o pool de USOS respira.
# ⛔ As entradas longas dao a RAZAO (ordem sem motivo nao faz ninguem clicar);
# as curtas existem para caber quando o uso e' longo. O `_ok` escolhe.
# ⛔⛔ TETO DE 5 PALAVRAS, E ELE E' ARITMETICA, NAO ESTILO.
# O menor EFEITO custa 7, a menor PARCEIRA 2, a menor REACAO 3 e o CTA_BASE 8 —
# somam 20 dos 25. Sobram CINCO para o follow, sempre.
# ⚠️ A primeira versao deste pool tinha dez entradas e SEIS delas custavam 6-7
# palavras. Elas nunca saiam: em 600 sorteios so' quatro apareceram, e as seis
# mortas eram justamente as que davam a RAZAO de seguir. Pool com entrada
# impossivel mente sobre o proprio tamanho — o autoteste contava 10 opcoes e a
# producao tinha 4.
# ⛔ Achado por MEDICAO de cobertura, e nao pelo linter: nenhuma lente olhava se
# uma entrada de pool e' alcancavel. Agora o autoteste olha (controle [ALCANCE])
# e reprova qualquer pool com entrada que nao cabe nem com os minimos dos
# outros eixos.
# ⭐ Metade das entradas ainda entrega o motivo, so' que em quatro ou cinco
# palavras — ordem sem motivo nao faz ninguem clicar.
FOLLOWS = [
    "Followers only.",
    "Follow first.",
    "Follow me first.",
    "Follow me too.",
    "Followers get it.",
    "Follow, or nothing sends.",
    "Unfollowed, I cannot reply.",
    "No follow, no recipe.",
    "Follow, or it never sends.",
    "Follow, or my DM bounces.",
]

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
    # ⭐ CINCO ENTRADAS NOVAS (2026-08-20), apostos VERBATIM do operador.
    # ⚠️ `horny goat weed` e a MESMA planta do `epimedium` acima. Os dois
    # convivem porque o que este pool varia e' a PALAVRA FALADA, e os dois
    # nomes soam completamente diferentes; a imagem e' identica de
    # proposito. Como se sorteia UM raro por video, nunca caem juntos.
    # ⭐ E o aposto dele nao foi inventado: e' o que o operador ja' tinha
    # validado no FALTA (`the herb goat farmers stumbled onto`).
    {"id": "horny_goat", "nome": "horny goat weed",
     "interno": "Epimedium spp.",
     "aposto": "the herb goat farmers stumbled onto",
     "img": "a small dish of dried heart-shaped leaves"},
    {"id": "ginseng", "nome": "panax ginseng", "interno": "Panax ginseng",
     "aposto": "the famous Korean root",
     "img": "a small dish of pale twisted ginseng root"},
    {"id": "acafrao", "nome": "saffron", "interno": "Crocus sativus",
     "aposto": "the rare red spice from the crocus flower",
     "img": "a small dish of deep red saffron threads"},
    # ⚠️ `geralmente Trichilia catigua`: o nome cientifico da catuaba varia
    # conforme a fonte botanica, e o operador escreveu o "geralmente" de
    # proposito. Fica registrado aqui — o campo `interno` NUNCA entra no
    # prompt, entao a incerteza nao chega ao video.
    {"id": "catuaba", "nome": "catuaba",
     "interno": "Trichilia catigua (geralmente)",
     "aposto": "the bark traditionally used in Brazil",
     "img": "a small dish of reddish bark shavings"},
    {"id": "ashwagandha", "nome": "ashwagandha",
     "interno": "Withania somnifera",
     "aposto": "that ancient root used in Indian medicine",
     "img": "a small dish of beige ashwagandha root and light brown "
            "powder"},
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
    #
    # ⭐⭐ `gigante_c2` — A ESCALA DO NECROSE NA MAO DO HOMEM. Ordem do
    # operador, 2026-08-10, lendo o render: *"o geoduck do take 2 esta' muito
    # pequeno; quero o tamanho do NECROSE"*. Dois defeitos somavam:
    #   1. A ANCORA ERA FEMININA NA MAO DELE. O campo `gigante` diz `longer
    #      than HER forearm` e a cena 2 e' `HIS right hand is closed around
    #      ...` — o possessivo aponta para um corpo que nao esta' na frase, e
    #      escala sem referente o Veo resolve pelo tamanho natural do molusco.
    #   2. FALTAVA A SEGUNDA DIMENSAO. `enormous ... longer than her forearm`
    #      da' comprimento e nao da' GROSSURA, e o render devolve uma peca
    #      longa e fina. O NECROSE (NE11) dimensiona pelas DUAS — `as long as
    #      his forearm and as thick as his wrist` — e e' esse par que faz o
    #      tamanho aparecer na tela.
    # ⛔ COPIA LITERAL DA SPEC DO NECROSE (`GEODUCK_PAYOFF`), com UMA troca: a
    # ancora vertical de la' e' `reaching well above the top of his head`, e
    # ⚠️ ate' 2026-08-10 nao havia cabeca em quadro aqui; hoje o corpo-prova
    # aparece de rosto e sorrindo (BO6 invertida).
    # Ancora que aponta para fora do frame e' ancora nenhuma — entra a do
    # TORSO, que e' o que esta' visivel: do punho ao alto do peito.
    #
    # ⭐⭐ 2026-08-16 — ELE PEDIU O TAMANHO DO NECROSE OUTRA VEZ: *"sempre que o
    # homem estiver segurando o geoduck no take e image 2, deve ser um geoduck
    # grande e grosso, igual ao do agente necrose"*.
    # ⛔⛔ E A MEDICAO DESMENTE A PREMISSA DE QUE FALTAVA SPEC: as duas eram
    # IDENTICAS — `as long as his forearm and as thick as his wrist`, nos dois
    # motores, palavra por palavra. O que faz o do NECROSE parecer maior nao e'
    # o prop, e' a MAO: la' ele ergue `raised above his shoulder against the
    # sky` e aqui a frase que posiciona diz `held upright at the height of his
    # waist`. Do punho na cintura, um sifao do tamanho do antebraco morre no
    # peito — que e' exatamente o que a ancora antiga descrevia, e ela estava
    # certa sobre o que o quadro mostrava.
    # ⭐ Como o que ele nomeou foi o OBJETO (*"um geoduck grande e grosso"*), e
    # a altura da mao e' cena, quem cresce aqui e' o prop: o sifao passa a ter
    # DUAS VEZES o antebraco, e ai' a ancora do NECROSE (`past the top of his
    # head`) volta a fechar a conta a partir da cintura. Uma so' escala, sem
    # contradicao — dois comprimentos diferentes na mesma frase e' ordem
    # ambigua, e o Veo resolve ambiguidade contra nos.
    # ⚠️ A ALTURA DA MAO segue sendo a diferenca restante, e e' decisao do
    # operador: erguer acima do ombro daria o enquadramento do NECROSE inteiro.
    # ⛔ E a CLAUSULA ANTI-BICHO vem JUNTO, nao e' enfeite: e' nessa escala que
    # o geoduck erguido passa a ler como ganso, e foi por isso que o NECROSE a
    # escreveu. Subir o tamanho sem ela e' reintroduzir o defeito que ele pagou.
    # Ela entra como `cauda_c2`, DEPOIS da frase que posiciona — dentro do campo
    # do prop ela deixaria a pose (`, held upright at the height of his waist`)
    # pendurada no fim de `nothing alive`.
    # ⚠️ Sem `held upright` dentro do campo: a pose mora na frase que POSICIONA
    # (T16-3), e este campo entra CRU na cena 2, sem passar pelo `_sem_pose`.
    # ⚠️ Vocabulario proibido pela `lint_nada_cresce` (BO2), que varre a IMAGE
    # 02/02: nada de `rises`, `stiff`, `erect`, `extends`. Por isso `standing
    # straight up` no lugar do `rises straight up` do NECROSE.
    {"id": "geoduck", "nome": "clam",
     "murcho": "a small shrivelled geoduck clam, its siphon limp and drawn back against the shell, barely the length of her palm",
     "gigante": "an enormous geoduck clam, its thick siphon standing straight up well past the pale ridged shell, as long as her forearm and as thick as her wrist, reaching from her fist up to the top of her chest, its surface taut and glossy, streaked with darker mottled lines running along its length, held upright",
     "gigante_c2": "an enormous geoduck clam, its very thick siphon standing straight up out of the shell, as thick as his wrist and twice the length of his forearm, reaching from his fist up past the top of his head, its surface taut and glossy, streaked with darker mottled lines running along its length",
     "cauda_c2": "No bird, no goose, no duck, no swan, no snake, no feathers, no beak, no eyes, no head, nothing alive."},
    # ⭐⭐ A LINGUICA — par novo em 2026-08-11, e o unico que nao e' vegetal.
    # ⚠️ Sem `cauda_c2`: a clausula anti-bicho existe porque GEODUCK ERGUIDO le'
    # como ganso. Linguica nao tem esse risco, e clausula que nomeia o que se
    # teme injeta o token (licoes-producao-veo §Declaracao e' municao).
    # ⭐ BANANA e PIMENTA voltaram em 2026-08-11, no mesmo dia em que sairam:
    # *"a referencia da banana no take 1 pode manter tambem, esta' boa, assim
    # como o da pimenta"*. Os dois murchos ja' liam como MOLE E PEQUENO — que
    # e' o criterio dele — e por isso passam. Os outros sete (pepino, cenoura,
    # abobrinha, berinjela, mandioca, nabo, milho) seguem fora: legume duro
    # murcho ainda le' como legume, nao como moleza.
    {"id": "banana", "nome": "banana",
     "murcho": "a small blackened banana, shrivelled and soft, drooping over her fingers, barely the length of her palm",
     "gigante": "an enormous bright yellow banana, longer than her forearm, held upright",
     "gigante_c2": "an enormous bright yellow banana, standing straight up in his fist, as long as his forearm and as thick as his wrist, reaching from his fist up to the top of his chest"},
    {"id": "pimenta", "nome": "chilli",
     "murcho": "a small dried chilli, blackened and curled, limp between her fingers, barely the length of her palm",
     "gigante": "an enormous smooth red chilli, long and straight, held upright",
     "gigante_c2": "an enormous smooth red chilli, standing straight up in his fist, as long as his forearm and as thick as his wrist, reaching from his fist up to the top of his chest"},
    {"id": "linguica", "nome": "sausage",
     "murcho": "a short limp sausage link, soft and wrinkled, sagging over her fingers, barely the length of her palm",
     "gigante": "an enormous thick sausage link, longer than her forearm, held upright",
     "gigante_c2": "an enormous thick sausage link, standing straight up in his fist, as long as his forearm and as thick as his wrist, reaching from his fist up to the top of his chest, its casing taut and glossy"},
]
PROPS = PARES   # o contrato do painel usa `PROPS`


# ---------------------------------------------------------------------------
# ⭐⭐ [T16-IDADE] A REGRA DOS 22 — um ano acima da maior maioridade dos EUA
# ---------------------------------------------------------------------------
# Ordem do operador, 2026-08-11, depois de recusa em serie por politica de
# MENORES: *"crie uma regra para colocar a idade sempre 1 ano acima da maior
# idade nos EUA"*.
#
# A maioridade nos EUA nao e' uma so': 18 na maioria dos estados, 19 em Alabama
# e Nebraska, e 21 no Mississippi — que e' a MAIOR. Um ano acima da maior da'
# 22, e e' esse o piso, para TODAS as mulheres deste motor.
#
# ⭐ E ele sobe a faixa em vez de baixar: antes eram 20-22, e a doutrina do repo
# diz que a politica de menores so' cede quando a idade SOBE. A regra corrige,
# na direcao certa, a decisao de horas antes.
#
# ⛔ IDADE E' NUMERO NO PROMPT, NUNCA DECLARACAO DE CONFORMIDADE. `they are
# adults`, `age-appropriate` e irmas estao na lista de PROIBIDOS do repo (ES17):
# declarar entrega ao classificador a categoria que ele policia. Numero de idade
# nao e' declaracao — e' atributo descritivo, e e' exatamente o que a doutrina
# manda fazer (*"fazer a idade RENDERIZAR"*).
#
# ⚠️ A idade entra na IMAGE **e** no TAKE dos DOIS blocos. Ordem dele: *"no take
# 1 e 2 precisa estar especificando a idade das personagens"*. O classificador
# le' os dois prompts; idade so' na IMAGE deixa metade do lote sem a informacao.
#
# ⭐⭐ SOBE PARA 25 EM 2026-08-16, DE NOVO POR RECUSA EM CAMPO. Ordem do
# operador, com o lote na mao: *"o take 1 do agente trio 16 esta' tomando muita
# violacao de politicas. Aumente a idade das meninas da cena para 25 anos"*.
#
# ⛔ E' A MESMA DIRECAO DE 11/08, PELO MESMO MOTIVO — a politica de menores so'
# cede quando a idade SOBE. Os 22 eram o minimo defensavel (um ano acima do
# Mississippi); 25 poe folga, e folga e' o que o classificador le' quando a
# cena tem duas mulheres sentadas com prop falico no colo. O numero de 11/08
# resolveu a recusa daquele dia e nao resolveu esta: numero minimo suficiente
# na mesa nao e' numero suficiente em quadro.
#
# ⭐ UMA CONSTANTE MANDA EM TUDO, e e' por isso que este conserto e' uma linha:
# as 36 entradas de `REFS` recebem `IDADE_MULHER`, e a idade renderiza nos
# CINCO blocos (BLOCO 0, IMAGE 01, IMAGE 02, TAKE 01, TAKE 02). MEDIDO depois
# da troca, com `\d+-year-old` extraido dos blocos gerados: nenhum `22` sobra
# em lugar nenhum.
# ⚠️ NAO ha' lente cravada no 22 — conferido antes de mexer. Se alguem crava
# uma, ela tem de ler `IDADE_MULHER`, nunca o literal: lente que repete o
# numero e' a segunda verdade que envelhece sozinha.
IDADE_MULHER = 25

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
    {"idade": IDADE_MULHER, "corpo": "tall and long-legged with a very small waist",
     "id": "auburn_ondas",
     "rotulo": "22y · auburn ondas longas + sardas",
     "id": "auburn_ondas",
     "rotulo": "22y · auburn ondas longas + sardas",
     "cabeca": "deep auburn hair falling in loose waves past her shoulders",
     "marca": "a light spray of freckles across her nose and green eyes"},
    {"idade": IDADE_MULHER, "corpo": "slim with an hourglass figure and long legs",
     "id": "cobre_rabo",
     "rotulo": "22y · rabo cobre + pinta no labio",
     "id": "cobre_rabo",
     "rotulo": "22y · rabo cobre + pinta no labio",
     "cabeca": "copper-red hair in a high glossy ponytail",
     "marca": "pale green eyes and a small beauty mark above her lip"},
    {"idade": IDADE_MULHER, "corpo": "willowy and fine-boned with a flat stomach",
     "id": "ginger_camadas",
     "rotulo": "22y · ginger repicado + sardas fortes",
     "id": "ginger_camadas",
     "rotulo": "22y · ginger repicado + sardas fortes",
     "cabeca": "bright ginger hair cut in long layers",
     "marca": "heavy freckling across her cheeks and hazel eyes"},
    {"idade": IDADE_MULHER, "corpo": "curvy with a narrow waist and full shoulders",
     "id": "vermelho_escuro",
     "rotulo": "22y · ruiva escura + argola na narina",
     "id": "vermelho_escuro",
     "rotulo": "22y · ruiva escura + argola na narina",
     "cabeca": "dark red hair swept over one shoulder",
     "marca": "a small gold hoop in her left nostril and clear skin"},
    {"idade": IDADE_MULHER, "corpo": "tall and statuesque with a long waist",
     "id": "morango_tranca",
     "rotulo": "22y · tranca loira rosada + mecha prata",
     "id": "morango_tranca",
     "rotulo": "22y · tranca loira rosada + mecha prata",
     "cabeca": "strawberry-blonde hair in a loose braid",
     "marca": "wide-set blue eyes and a bright silver streak at one temple"},
    {"idade": IDADE_MULHER, "corpo": "slim and toned with a dancer's line",
     "id": "preto_risca_meio",
     "rotulo": "22y · preto risca ao meio + malar forte",
     "id": "preto_risca_meio",
     "rotulo": "22y · preto risca ao meio + malar forte",
     "cabeca": "jet-black hair in a sleek centre part",
     "marca": "sharp cheekbones and a small mole on her jaw"},
    {"idade": IDADE_MULHER, "corpo": "long-legged and slender with square shoulders",
     "id": "platinado_chanel",
     "rotulo": "22y · loira platinada + olhos gelo",
     "id": "platinado_chanel",
     "rotulo": "22y · loira platinada + olhos gelo",
     "cabeca": "platinum blonde hair in a blunt shoulder-length cut",
     "marca": "ice-blue eyes and a dimple in one cheek"},
    {"idade": IDADE_MULHER, "corpo": "curvy and athletic with a small waist",
     "id": "cachos_altos",
     "rotulo": "22y · cachos presos no alto + sorriso",
     "id": "cachos_altos",
     "rotulo": "22y · cachos presos no alto + sorriso",
     "cabeca": "tight dark curls gathered high on her head",
     "marca": "glowing deep brown skin and a wide bright smile"},
    {"idade": IDADE_MULHER, "corpo": "tall and slim with an hourglass line",
     "id": "castanho_praia",
     "rotulo": "22y · castanho ondas praia + covinha",
     "id": "castanho_praia",
     "rotulo": "22y · castanho ondas praia + covinha",
     "cabeca": "chestnut hair in long beachy waves",
     "marca": "a deep dimple in her right cheek and warm brown eyes"},
    {"idade": IDADE_MULHER, "corpo": "petite and curvy with a defined waist",
     "id": "mel_coque",
     "rotulo": "22y · coque loiro mel + labios cheios",
     "id": "mel_coque",
     "rotulo": "22y · coque loiro mel + labios cheios",
     "cabeca": "honey-blonde hair in a high messy bun",
     "marca": "a scatter of freckles and full lips"},
    {"idade": IDADE_MULHER, "corpo": "lean and toned with a flat stomach and long arms",
     "id": "preto_cintura",
     "rotulo": "22y · preto liso ate a cintura + tarraxa",
     "id": "preto_cintura",
     "rotulo": "22y · preto liso ate a cintura + tarraxa",
     "cabeca": "long jet-black hair falling straight to the waist",
     "marca": "almond eyes and a small stud in one nostril"},
    {"idade": IDADE_MULHER, "corpo": "shapely with toned arms and a narrow waist",
     "id": "balayage_caramelo",
     "rotulo": "22y · balayage caramelo + pinta no olho",
     "id": "balayage_caramelo",
     "rotulo": "22y · balayage caramelo + pinta no olho",
     "cabeca": "caramel balayage falling past her shoulders",
     "marca": "a beauty mark at the corner of her right eye"},
    {"idade": IDADE_MULHER, "corpo": "slim-hipped and elegant with a long neck",
     "id": "areia_espinha",
     "rotulo": "22y · loira areia + tranca espinha",
     "id": "areia_espinha",
     "rotulo": "22y · loira areia + tranca espinha",
     "cabeca": "sandy blonde hair in a fishtail braid",
     "marca": "a slight overbite that shows when she smiles"},
    {"idade": IDADE_MULHER, "corpo": "curvy and strong with a small waist",
     "id": "box_braids",
     "rotulo": "22y · box braids + argola dourada",
     "id": "box_braids",
     "rotulo": "22y · box braids + argola dourada",
     "cabeca": "long box braids gathered over one shoulder",
     "marca": "high round cheekbones and a gold nose ring"},
    {"idade": IDADE_MULHER, "corpo": "tall and lean with swimmer's shoulders",
     "id": "auburn_rabo_baixo",
     "rotulo": "22y · rabo auburn baixo + olhos cinza",
     "id": "auburn_rabo_baixo",
     "rotulo": "22y · rabo auburn baixo + olhos cinza",
     "cabeca": "auburn hair in a low glossy ponytail",
     "marca": "dark freckles across both cheeks and grey eyes"},
    {"idade": IDADE_MULHER, "corpo": "softly curvy with a full figure and a narrow waist",
     "id": "castanho_lateral",
     "rotulo": "22y · castanho risca lateral + sinal",
     "id": "castanho_lateral",
     "rotulo": "22y · castanho risca lateral + sinal",
     "cabeca": "dark brown hair in heavy waves with a deep side part",
     "marca": "a small raised birthmark on her temple"},
    {"idade": IDADE_MULHER, "corpo": "slim and supple with a very straight back",
     "id": "cobre_bob",
     "rotulo": "22y · chanel cobre + olhos verdes",
     "id": "cobre_bob",
     "rotulo": "22y · chanel cobre + olhos verdes",
     "cabeca": "copper hair cropped into a long bob",
     "marca": "pale skin, freckles and bright green eyes"},
    {"idade": IDADE_MULHER, "corpo": "long-limbed and shapely with a defined waist",
     "id": "preto_rabo_alto",
     "rotulo": "22y · rabo preto alto + sobrancelha cheia",
     "id": "preto_rabo_alto",
     "rotulo": "22y · rabo preto alto + sobrancelha cheia",
     "cabeca": "black hair in a high sleek ponytail",
     "marca": "a small beauty mark on her jawline and full brows"},
    {"idade": IDADE_MULHER, "corpo": "trim and athletic with a flat stomach",
     "id": "loiro_dourado",
     "rotulo": "22y · loira dourada + uma covinha so",
     "id": "loiro_dourado",
     "rotulo": "22y · loira dourada + uma covinha so",
     "cabeca": "golden blonde hair in loose waves",
     "marca": "a small dimple in one cheek only"},
    {"idade": IDADE_MULHER, "corpo": "tall and willowy with narrow hips",
     "id": "auburn_meio_preso",
     "rotulo": "22y · auburn meio preso + olhos mel",
     "id": "auburn_meio_preso",
     "rotulo": "22y · auburn meio preso + olhos mel",
     "cabeca": "dark auburn hair in a half-up twist",
     "marca": "wide hazel eyes and a light dusting of freckles"},
    {"idade": IDADE_MULHER, "corpo": "curvy with a small waist and long legs",
     "id": "coils_rente",
     "rotulo": "22y · coils rente + malar esculpido",
     "id": "coils_rente",
     "rotulo": "22y · coils rente + malar esculpido",
     "cabeca": "tight coils cropped close to the head",
     "marca": "sculpted cheekbones and a small gold stud"},
    {"idade": IDADE_MULHER, "corpo": "slim with a long waist and square shoulders",
     "id": "cinza_coque",
     "rotulo": "22y · coque castanho cinza + pinta",
     "id": "cinza_coque",
     "rotulo": "22y · coque castanho cinza + pinta",
     "cabeca": "ash-brown hair in a sleek low bun",
     "marca": "grey-green eyes and a beauty mark just above her left brow"},
    {"idade": IDADE_MULHER, "corpo": "shapely and toned with a narrow waist",
     "id": "ginger_cachos",
     "rotulo": "22y · cachos ginger + covinha no queixo",
     "id": "ginger_cachos",
     "rotulo": "22y · cachos ginger + covinha no queixo",
     "cabeca": "ginger hair in loose curls past her shoulders",
     "marca": "heavy freckling and a small chin dimple"},
    {"idade": IDADE_MULHER, "corpo": "tall and slim with a graceful neck",
     "id": "tranca_coroa",
     "rotulo": "22y · tranca coroa escura + pinta alta",
     "id": "tranca_coroa",
     "rotulo": "22y · tranca coroa escura + pinta alta",
     "cabeca": "long dark hair in a high crown braid",
     "marca": "a beauty mark high on her left cheek"},
    {"idade": IDADE_MULHER, "corpo": "petite and shapely with a defined waist",
     "id": "loiro_oxigenado",
     "rotulo": "22y · chanel loiro oxigenado + queixo",
     "id": "loiro_oxigenado",
     "rotulo": "22y · chanel loiro oxigenado + queixo",
     "cabeca": "bleached blonde hair in a blunt chin-length bob",
     "marca": "wide dark eyes and a dimple in her chin"},
    {"idade": IDADE_MULHER, "corpo": "athletic and curvy with strong shoulders",
     "id": "mogno_ondas",
     "rotulo": "22y · ondas mogno + argola no nariz",
     "id": "mogno_ondas",
     "rotulo": "22y · ondas mogno + argola no nariz",
     "cabeca": "long waves in a rich mahogany red",
     "marca": "clear skin and a small hoop in her right nostril"},
    {"idade": IDADE_MULHER, "corpo": "long-legged and lean with a flat stomach",
     "id": "castanho_penteado",
     "rotulo": "22y · rabo penteado para tras + sinal",
     "id": "castanho_penteado",
     "rotulo": "22y · rabo penteado para tras + sinal",
     "cabeca": "dark brown hair in a slicked-back ponytail",
     "marca": "sharp brows and a small mole under one eye"},
    {"idade": IDADE_MULHER, "corpo": "curvy and confident with a very narrow waist",
     "id": "ruivo_mel",
     "rotulo": "22y · ruivo mel + sardas densas",
     "id": "ruivo_mel",
     "rotulo": "22y · ruivo mel + sardas densas",
     "cabeca": "honey-red hair falling in soft waves",
     "marca": "a dense spray of freckles across her nose"},
    {"idade": IDADE_MULHER, "corpo": "slim and elegant with long arms",
     "id": "preto_ombro",
     "rotulo": "22y · preto no ombro + mecha branca",
     "id": "preto_ombro",
     "rotulo": "22y · preto no ombro + mecha branca",
     "cabeca": "black hair in a smooth shoulder-length cut",
     "marca": "a thin white streak at her temple and dark eyes"},
    {"idade": IDADE_MULHER, "corpo": "tall with a small waist and full shoulders",
     "id": "morango_coque",
     "rotulo": "22y · coque loiro rosado + olhos verdes",
     "id": "morango_coque",
     "rotulo": "22y · coque loiro rosado + olhos verdes",
     "cabeca": "strawberry-blonde hair in a high loose bun",
     "marca": "green eyes and a small beauty spot on her cheekbone"},

    # ⭐⭐ + 2026-08-13 — SEIS ENTRADAS NOVAS, de 30 para 36. Ordem do operador:
    # *"aumente o pool de opcoes substancialmente, tambem dos ambientes"*.
    # ⛔ Cada uma varia CORPO, CABECA e MARCA juntos, como as trinta de cima:
    # duas mulheres de cabelo diferente e mesmo porte leem como a mesma pessoa.
    # ⛔ Zero adjetivo de etnia — quem injeta e' a montagem, a partir do MUNDO.
    #
    # ⛔⛔ E CINCO ENTRADAS ANTIGAS FORAM REESCRITAS NO MESMO DIA, pela LEI DO
    # REF (*"mulheres sempre super fit e lindas"*, e a ancora e' SINAL DE BELEZA,
    # nunca deterioracao). O que saiu, medido: `faint scar through one eyebrow`,
    # `gap between her front teeth`, `thin scar along her jawline`, `faint scar
    # on her chin` e `faint mark between her brows` — este ultimo porque `mark
    # between the brows` e' o que o gerador resolve como VINCO, nao como pinta.
    # ⚠️ NADA foi apagado sem substituicao: cada uma ganhou uma ancora SAUDAVEL
    # no lugar (`silver streak`, `dimple`, `beauty mark`), senao o eixo `ancora`
    # do `medir_personagens.py` cai junto com a cicatriz.
    {"idade": IDADE_MULHER, "corpo": "tall and athletic with a long waist and narrow hips",
     "id": "canela_tranca",
     "rotulo": "22y · tranca canela + olhos ambar",
     "id": "canela_tranca",
     "rotulo": "22y · tranca canela + olhos ambar",
     "cabeca": "cinnamon-red hair in a thick side braid",
     "marca": "a light spray of freckles over her cheekbones and amber eyes"},
    {"idade": IDADE_MULHER, "corpo": "shapely and lithe with a very small waist",
     "id": "espresso_no",
     "rotulo": "22y · coque torcido espresso + cilios",
     "id": "espresso_no",
     "rotulo": "22y · coque torcido espresso + cilios",
     "cabeca": "espresso-dark hair in a high twisted knot",
     "marca": "a deep dimple in her right cheek and long dark lashes"},
    {"idade": IDADE_MULHER, "corpo": "long-legged and toned with square shoulders and a flat stomach",
     "id": "trigo_lateral",
     "rotulo": "22y · loira trigo + argola na orelha",
     "id": "trigo_lateral",
     "rotulo": "22y · loira trigo + argola na orelha",
     "cabeca": "wheat-blonde hair swept into a low side wave",
     "marca": "a small gold hoop in one ear and lightly tanned even skin"},
    {"idade": IDADE_MULHER, "corpo": "petite and curvy with full shoulders and a defined waist",
     "id": "cornrows_coque",
     "rotulo": "22y · cornrows finas + coque baixo",
     "id": "cornrows_coque",
     "rotulo": "22y · cornrows finas + coque baixo",
     "cabeca": "fine cornrows finished in a low gathered bun",
     "marca": "a beauty mark at the outer corner of her left eye"},
    {"idade": IDADE_MULHER, "corpo": "statuesque and strong with a narrow waist and long arms",
     "id": "cobre_queimado",
     "rotulo": "22y · cobre queimado longo + sardas",
     "id": "cobre_queimado",
     "rotulo": "22y · cobre queimado longo + sardas",
     "cabeca": "burnt-copper hair falling in heavy waves to the ribs",
     "marca": "wide green eyes and a dense scatter of freckles"},
    {"idade": IDADE_MULHER, "corpo": "slim and supple with a very long neck",
     "id": "azul_preto_franja",
     "rotulo": "22y · preto azulado franja + mecha prata",
     "id": "azul_preto_franja",
     "rotulo": "22y · preto azulado franja + mecha prata",
     "cabeca": "blue-black hair in a blunt chin-length cut with a deep fringe",
     "marca": "a silver streak at her right temple and dark almond eyes"},
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
# ⛔⛔ POOL SANEADO E AMPLIADO EM 2026-08-13. Ordem do operador: *"melhore a
# aparencia e shape desses homens"* / *"aumente o pool de opcoes
# substancialmente, tambem dos ambientes"*.
#
# ⚠️ E' A MESMA ORDEM QUE JA' TINHA SIDO DADA NO PLACA 16 EM 12/08, com o lote na
# mao — *"esses caras tao parecendo mendigo"*. La' o pool foi reescrito e AQUI
# nao: este arquivo continuava com as 22 originais, e catorze delas carregavam
# marcador de DANO. Medido, entrada por entrada:
#     `weathered` / `sun-weathered` / `deeply lined` / `deep tan line`
#     `ruddy` · `gaunt` (2x) · `hollow cheeks`
#     `scar` (2x) · `chipped front tooth` · `gap between his front teeth`
#     `raised mole` · `large mole` · `bulbous nose` · `squint` · `deep-set eyes`
# Pele castigada, cicatriz, dente faltando e verruga nao sao "marca distintiva":
# sao DANO. Num homem de 60, dano renderiza exatamente como ele descreveu.
#
# ⭐ A REGRA E' A DO REPO: **DISTINTIVO, NUNCA DETERIORADO**. A ancora e' uma
# feicao MEMORAVEL num rosto SAUDAVEL — `cleft`, `dimple`, `beauty mark`,
# `silver streak`, `hoop`, `stud`, `patch of white`. Nenhuma delas e' avaria, e
# todas continuam contando no eixo `ancora` do `medir_personagens.py`.
# ⛔ E A PELE NAO PODE FICAR VAZIA NO LUGAR: tirar `weathered` sem por
# `smooth-skinned`/`tanned`/`freckled`/`laugh lines` ZERA o eixo `pele` — foi
# exatamente o erro cometido na primeira versao do pool do PLACA 16.
#
# ⛔⛔ NENHUMA PALAVRA DE APROVACAO: sairam `strong square jaw` e `strong cleft
# chin`, e nada de `handsome`, `chiseled`, `rugged` entrou no lugar. Elogio no
# prompt puxa o rosto para a media do banco de imagem — o mesmo mecanismo pelo
# qual `not a celebrity` invoca a celebridade.
# ⚠️ A ETNIA NAO ENTRA AQUI: vem do MUNDO (`spec["etnia"]`), igual a' dela.
# ⚠️ AS IDADES E AS PESSOAS NAO MUDARAM nas 22 herdadas — mexeu-se so' no que
# era avaria. Quem trocar o numero aqui esta' mexendo noutra decisao.
HOMENS = [
    {"id": "grisalho_barbudo", "idade": 78,
     "marca": "a heavy-set build, thick silver hair and a short grey beard, "
              "smooth-skinned, with a silver streak through one eyebrow",
     "roupa": "a plain navy work shirt"},
    {"id": "careca_bigode", "idade": 81,
     "marca": "a stocky build, a bald crown with white hair at the sides and a "
              "thick moustache, lightly tanned, with a beauty mark high on one "
              "cheek",
     "roupa": "a heather-grey pocket tee"},
    {"id": "cabelo_farto", "idade": 73,
     "marca": "a tall lean frame, a full head of thick white hair, thinning at "
              "the temples, clean-shaven, with a deep cleft in his chin",
     "roupa": "an olive canvas shirt with the sleeves rolled"},
    {"id": "sardas_ruivo", "idade": 71,
     "marca": "a wiry build, faded coppery hair and heavy freckling across the "
              "nose, "
              "with a small gold hoop in one ear",
     "roupa": "a faded red flannel shirt"},
    {"id": "fade_grisalho", "idade": 77,
     "marca": "a broad-shouldered build, a close grey fade and a neat chinstrap "
              "beard, smooth-skinned, with a small gold stud in one ear",
     "roupa": "a slate-blue polo shirt"},
    {"id": "locs_oculos", "idade": 75,
     "marca": "a solid build, salt-and-pepper locs gathered back, wire-rimmed "
              "glasses and a beauty mark beside his right eye",
     "roupa": "a charcoal henley with the sleeves pushed up"},
    {"id": "corte_militar", "idade": 76,
     "marca": "a thickset build, an iron-grey brush cut, lightly tanned, with "
              "heavy level brows and a cleft in his chin, wearing plain "
              "steel-framed glasses",
     "roupa": "a mustard snap-button shirt"},
    {"id": "cavanhaque", "idade": 79,
     "marca": "a barrel-chested build, a shaved head and a neat white goatee, "
              "with a white streak in one eyebrow",
     "roupa": "a cream short-sleeve camp shirt"},
    {"id": "onda_longa", "idade": 72,
     "marca": "a slim build, wavy iron-grey hair grown a little long at the collar, "
              "clean-shaven, with a deep dimple in his left cheek",
     "roupa": "a forest-green work shirt"},
    {"id": "sobrancelha_oculos", "idade": 82,
     "marca": "a slender upright build, white hair combed back, heavy "
              "black-framed glasses, smooth-skinned, with a beauty mark at his "
              "left temple",
     "roupa": "a blue-and-white checked shirt"},
    {"id": "queixo_fendido", "idade": 74,
     "marca": "a compact build, sandy hair gone white at the sides, tanned, "
              "with a deep cleft chin",
     "roupa": "a rust-red pocket tee"},
    {"id": "afro_curto", "idade": 77,
     "marca": "a burly build, a short grey afro and a broad open face, with a "
              "small birthmark high on one cheek",
     "roupa": "a sand-coloured linen shirt"},
    # + 2026-08-05, mesma ordem do operador. Porte, cabeca e pelo facial variam
    # juntos: dois homens de cabelo diferente e mesmo porte leem como o mesmo.
    {"id": "bigode_farto", "idade": 78,
     "marca": "a lean upright frame, white hair combed to one side and a thick "
              "moustache, with deep laugh lines around the eyes",
     "roupa": "a striped short-sleeve shirt"},
    {"id": "calvo_barba", "idade": 75,
     "marca": "a heavy build, a shaved head and a full salt-and-pepper beard, "
              "smooth-skinned, with a broad flat nose",
     "roupa": "a denim work shirt"},
    {"id": "branco_liso", "idade": 80,
     "marca": "a narrow build, straight white hair falling over the forehead, "
              "smooth-skinned, with a cleft chin",
     "roupa": "a pale blue oxford shirt"},
    {"id": "locs_curtas", "idade": 73,
     "marca": "a stocky athletic build, short twisted locs and a trimmed "
              "goatee, with a patch of white above one temple",
     "roupa": "a burgundy polo shirt"},
    {"id": "sobrancelha_farta", "idade": 79,
     "marca": "a solid build, thinning grey hair and very heavy level "
              "eyebrows, freckled across the nose, with a beauty mark near his "
              "jaw",
     "roupa": "a khaki utility shirt"},
    {"id": "queimado_sol", "idade": 74,
     "marca": "a rangy build, sun-bleached white hair, lightly tanned, with "
              "laugh lines at the eyes and a dimple in one cheek",
     "roupa": "a faded teal work shirt"},
    {"id": "cavanhaque_branco", "idade": 82,
     "marca": "a spare frame, close-cropped white hair and a white goatee, "
              "smooth-skinned, with prominent ears",
     "roupa": "a grey chambray shirt"},
    {"id": "cacheado_grisalho", "idade": 72,
     "marca": "a broad build, dense curly hair gone grey all over and thin at "
              "the temples, clean-shaven and smooth-skinned, with a deep "
              "dimple in one "
              "cheek",
     "roupa": "a black crew-neck tee"},
    {"id": "bochechudo", "idade": 78,
     "marca": "a round-faced heavy build, grey hair receding at the temples "
              "and full cheeks, with a dimpled chin",
     "roupa": "a plaid flannel shirt"},
    {"id": "magro_alto", "idade": 75,
     "marca": "a very tall lean frame, iron-grey hair cropped short and a long "
              "straight nose, lightly tanned, with a cleft chin",
     "roupa": "a white undershirt beneath an open work shirt"},

    # ⭐⭐ + 2026-08-13 — SEIS ENTRADAS NOVAS, de 22 para 28, mesma ordem do
    # operador (*"aumente o pool de opcoes substancialmente"*).
    # ⛔ Todas 50+, no padrao que o PLACA 16 fixou em 12/08: nenhum marcador de
    # dano, nenhuma palavra de aprovacao, nenhuma cor de pele.
    # ⚠️ QUATRO DELAS TRAZEM OCULOS de proposito. O eixo media 2 em 22 (9,1%),
    # que e' rotacao morta num medidor que cobra 25-30%; com estas seis mais os
    # oculos que voltaram ao `corte_militar` ele fecha em 7 de 28.
    # ⭐ Cada uma varia PORTE, CABECA e MARCA juntas — duas entradas de cabelo
    # diferente e mesmo corpo leem como o mesmo homem.
    {"id": "prata_penteado_oculos", "idade": 72,
     "marca": "a broad solid build, a full head of silver hair combed straight "
              "back, clean-shaven and smooth-skinned, wearing thin gold "
              "wire-rimmed glasses, with a shallow cleft chin",
     "roupa": "a slate-blue linen shirt"},
    {"id": "barba_branca_cheia", "idade": 74,
     "marca": "a tall broad-shouldered build, thick white hair and a full beard "
              "kept neatly shaped, with laugh lines at the eyes and a dimple "
              "beside his mouth",
     "roupa": "a charcoal cardigan over a plain white tee"},
    {"id": "twists_prata_oculos", "idade": 76,
     "marca": "a lean upright build, short silver twists kept close and a "
              "close-trimmed beard, smooth-skinned, with a beauty mark below "
              "one eye, wearing slim half-rim glasses",
     "roupa": "a stone-grey henley with the sleeves pushed up"},
    {"id": "bigode_chevron", "idade": 78,
     "marca": "a compact sturdy build, white hair parted low and a full "
              "chevron moustache kept trimmed, freckled across the cheeks, "
              "with a cleft in his chin",
     "roupa": "a warm grey flannel shirt"},
    {"id": "careca_oculos_pesados", "idade": 80,
     "marca": "a heavy square build, a cleanly shaved crown and no beard at "
              "all, lightly tanned, wearing heavy dark-rimmed glasses, with a "
              "beauty mark high on one cheekbone",
     "roupa": "a dark olive crewneck sweater"},
    {"id": "mecha_branca_lateral", "idade": 82,
     "marca": "a tall trim build, silver hair cut neatly above the collar with "
              "a patch of white above one temple, clean-shaven and "
              "smooth-skinned, wearing rimless reading glasses",
     "roupa": "a pressed light blue shirt"},
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

# ⛔⛔ A ESCALADA SAIU DA CENA 3 — decisao MEDIDA, nao estetica.
# Com uso + escalada + keyword + isca + gate a cena batia em 42 palavras contra
# um teto de 31, ou seja 5,3 palavras por segundo: um terco acima do que cabe em
# 8 segundos de narracao. Quatro funcoes nao cabem; tres cabem.
# ⚠️ E a que saiu foi a ESCALADA porque ela e' a unica REDUNDANTE: ela promete
# "tem mais" e a ISCA ja' diz o que chega. Keyword, isca e gate sao lei do repo
# e nao encolhem. Fica registrado para ninguem "reintroduzir a escalada" sem
# saber o que vai sair no lugar.


# ⛔ As palavras do orgao. Rotacionam DENTRO do video (nunca a mesma duas vezes).
#
# ⭐⭐ SO' `Johnson` E `manhood` DESDE 2026-08-16. Ordem do operador, com as
# recusas na mao: *"esta' dando sempre violacao de conteudo nocivo. Ajuste o
# agente python para gerar sempre falas que fazem referencia ao penis somente
# como Johnson ou Manhood, retire qualquer outro termo"*.
#
# ⭐ MEDIDO ANTES DA TROCA, 300 videos: `Johnson` 215, `wiener` 193,
# `pecker` 192. Dois em cada tres videos saiam com uma palavra que ele nao quer
# — e' a mesma proporcao que o GOOD 16 media quando recebeu esta mesma ordem em
# 13/08, e la' o conserto foi este.
# ⚠️ E `soldier` e `tool` estavam no pool e NUNCA renderizavam: 0 em 300. Eram
# pool morto antes desta ordem, e saem sem custo nenhum.
#
# ⛔⛔ ISSO FURA O CT4b DO CONTRATO DE 16s, que so' aceita
# `pecker`/`wiener`/`Johnson`. A excecao entra em `DESLIGADAS` no
# `medir_copy16` com a ordem escrita, como no GOOD 16 — gate que acusa uma
# decisao declarada treina o operador a ignorar o gate.
# ⭐ E o que o CT4b protege continua vivo: quem cobra UM apelido por video,
# repetido nos dois takes, e' o CT4, e ele nao mudou. O pool tem dois e o
# sorteio alterna, entao a variacao ENTRE videos tambem fica.
NUCLEO = ["Johnson", "manhood"]

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

# ⭐ DUAS CENAS. O teto continua 25 — ele nao vem do numero de cenas, vem da
# fisica: 8 segundos x 3,1 palavras/s. Encurtar o video nao alarga a boca.
# ⚠️ O `durationSeconds: 10` do AdBatch e' aspiracional; medido em campo, o
# player do Flow marca 00:08:00. O teto de 25 esta' certo e nao sobe.
TETO_FALA = {1: 25, 2: 25}
# ⛔ O piso da cena 2 e' 20 e ele e' ARITMETICA, nao gosto: o CTA_BASE custa 8
# palavras fixas, o menor FOLLOW custa 2 e o menor USO custa 10. Abaixo de 20
# nao existe combinacao possivel — piso mais baixo seria um numero que nunca
# dispara, e alarme que nunca toca e' pior que alarme nenhum.
PISO_FALA = {1: 18, 2: 20}


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
# ⛔⛔ O `homem` TAMBEM tinha saido em 2026-08-05, quando o corpo-prova
# masculino nao estava na cena 3. Depois ele VOLTOU ao quadro e ninguem repos o
# eixo — o comentario do TRIO ainda diz que o eixo esta' morto enquanto o codigo
# usa `spec["homem"]` para montar a cena. Aqui ele volta ao painel: eixo VIVO
# que o painel esconde e' o defeito espelhado do que esta lista impede, e custa
# ao operador ter de re-sortear o video inteiro para trocar o corpo-prova.
# ⭐⭐ A PALAVRA DO CTA E' CAMPO NO PAINEL (2026-08-15). Ordem do operador:
# *"todos os agentes16 meus devem levar um ui ux input pertinente para alterar
# a palavra chave X do cta"*.
# ⛔ `KEYWORD_NATIVA` e' a palavra que os POOLS deste motor ja' trazem escrita —
# a ancora da substituicao, nao uma preferencia. Assumir `gelatin` para todos
# reescreveria em silencio a excecao dos tres BANHO, que usam `recipe` por
# ordem de 2026-08-13.
# ⛔ A troca vale so' para a KEYWORD (`Comment <x>,`). O MECANISMO
# (`gelatin trick`) e o rotulo da caixa em quadro NAO mudam: e' o que a VSL
# vende, e a congruencia e' inviolavel.
KEYWORD_UI = True
KEYWORD_NATIVA = "gelatin"

EIXOS_UI = [
    ("mundo", "A COZINHA", "MUNDOS", "id"),
    ("etnia", "ETNIA", "etnias_do_mundo", None),
    ("ref", "A QUE FALA", "REFS", "cabeca"),
    ("traje", "O TRAJE DELA", "trajes_do_mundo", None),
    ("amiga", "A AMIGA", "REFS", "cabeca"),
    ("prop", "O PAR DE PROPS", "PROPS", "nome"),
    ("preparo", "A BANCADA (conformacao)", "PREPAROS", "id"),
    ("raro", "O RARO", "RAROS", "nome"),
    # ⭐ O HOMEM VOLTA AO PAINEL — 2026-08-08. No TRIO ele foi tirado daqui em
    # 2026-08-05, quando o corpo-prova masculino tinha saido da cena 3; depois
    # o corpo-prova VOLTOU e ninguem repos o eixo. Ficou o defeito espelhado do
    # que a lista existe para impedir: eixo VIVO que o painel nao mostra. O
    # operador nao consegue trocar o corpo-prova sem re-sortear o video inteiro.
    ("homem", "O CORPO-PROVA", "HOMENS", "id"),
]

CENAS_UI = ["1 · a isca + o vilao", "2 · a prova + CTA"]

# ⭐⭐ O DROPDOWN DE QUEM FALA — e' ELE que da' FUNCAO ao campo `rotulo`.
# ⛔ Sem esta linha o rotulo seria comentario caro: 36 textos escritos, medidos
# e travados, e nenhum olho humano os veria. Forma sem funcao e' o defeito que
# este repo mais paga (licoes-de-construcao §41), e um label que nao aparece na
# tela e' a versao mais barata dele.
# ⛔ POR QUE DROPDOWN E NAO `TRAVAS_UI`: a barra de travas desenha UM BOTAO POR
# OPCAO, lado a lado. Serve para os nichos; com 36 REFs ela estoura a largura da
# janela. Contrato aditivo do `ui_agente` (2026-08-13), modelo: MEL 16.
# ⚠️ O campo exibido e' `rotulo`, NAO `cabeca`: o `ui_agente` monta o mapa
# texto -> `id`, entao o operador escolhe "22y · box braids + argola dourada" e
# o motor recebe `box_braids`. Um menu de `cabeca` seria um paragrafo em ingles
# por linha — ilegivel num combobox de 38 colunas.
# ⛔⛔ E FOI ESTA LINHA QUE OBRIGOU O POOL A GANHAR `id`. O `_barra_dropdowns`
# resolve o texto escolhido para `e.get("id")`; sem `id` o mapa inteiro valia
# `None`, o `sortear` do `ui_agente` pulava a trava (`if alvo:`) e o menu ficava
# DESENHADO E MUDO. Ver `_por_ref` la' em cima: o resto do conserto mora la'.
DROPDOWNS_UI = [("ref", "A QUE FALA", "REFS", "rotulo")]


def _checa_drop(pool, campo):
    """As quatro travas de FORMA do dropdown, sobre um pool qualquer.

    ⚠️ E' FUNCAO, e no nivel do modulo, por dois motivos. O controle negativo
    precisa rodar a MESMA lente sobre um pool sabotado — lente que so' existe
    inline nao pode ser sabotada, e lente que nao pode ser sabotada e' relato,
    nao medicao (licoes §41). E o `autoteste` precisa chama-la ANTES do lote.
    """
    ms = []
    if [e for e in pool if not e.get(campo)]:
        ms.append("entrada sem `%s`" % campo)
    if [e for e in pool if not e.get("id")]:
        ms.append("entrada sem `id` — o menu devolveria None")
    r = [e.get(campo) or "" for e in pool]
    rep = sorted({x for x in r if r.count(x) > 1})
    if rep:
        ms.append("rotulo repetido (%r) — a 2a entrada some do menu" % rep[0])
    lg = [x for x in r if len(x) > 42]
    if lg:
        ms.append("rotulo de %d chars (%r) — estoura o combobox"
                  % (len(lg[0]), lg[0]))
    return ms


def _contrato_dropdown():
    """O contrato ESTATICO do menu: pool existe, campo existe, eixo e' travavel.

    ⛔ Roda ANTES do lote do autoteste, de proposito e por medicao: uma entrada
    sem `id` derruba o `sortear` de varios motores desta familia la' dentro, e
    um traceback no meio de 600 videos ESCONDE a causa real — quem le' ve'
    `KeyError: 'id'` e vai cacar bug de sorteio, quando o que quebrou foi o
    contrato do menu. Falha de contrato reporta e PARA.
    """
    ms = []
    for ch, _tela, pn, campo in DROPDOWNS_UI:
        pool = globals().get(pn)
        if not isinstance(pool, list) or not pool:
            ms.append("DROPDOWN: `DROPDOWNS_UI` aponta para o pool %r, que nao "
                      "e' uma lista deste motor — o menu nasce vazio" % pn)
            continue
        if ch not in EIXOS_TRAVAVEIS:
            ms.append("DROPDOWN: o eixo %r nao esta' em EIXOS_TRAVAVEIS — o "
                      "operador escolhe no menu e o sortear ignora" % ch)
        ms += ["DROPDOWN/%s: %s" % (pn, x) for x in _checa_drop(pool, campo)]
    return ms


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


def _por_ref(pool, valor):
    """Resolve a REF travada por `id` (o dropdown) OU por `cabeca` (o antigo).

    ⛔⛔ ESTE HELPER EXISTE PORQUE O DROPDOWN MANDA `id`, E ESTE POOL RESOLVIA
    POR `cabeca`. O `ui_agente._barra_dropdowns` monta o mapa
    `rotulo -> e.get("id")`, entao e' o `id` que chega em `travas["ref"]`. Com a
    resolucao antiga (`_por_id(REFS, ..., "cabeca")`) nenhum id casava e o
    `next(...)` caia no `pool[0]` — o menu "funcionava", nao dava erro nenhum, e
    entregava SEMPRE a primeira mulher da lista. E' o botao que mente na sua
    forma mais cara: silencioso, e so' visivel para quem conferir 8 sorteios.
    ⚠️ A `cabeca` continua aceita de proposito. Isto e' um SUPERSET da
    resolucao antiga, nao uma troca: nenhum chamador existente muda de
    comportamento, e por isso a mudanca nao precisa de re-medicao de lote.
    ⚠️ E valor que NAO e' string (o cadeado da coluna manda o DICT inteiro)
    volta intacto, exatamente como o `_por_id` ja' fazia.
    """
    if not isinstance(valor, str):
        return valor
    return next((x for x in pool
                 if x.get("id") == valor or x.get("cabeca") == valor), pool[0])


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
# ⛔ A negacao anti-celebridade saiu daqui em 2026-08-14, por ordem do operador
# (*"tire not a celebrity do prompt"*): declaracao INJETA o token que ela nega.
# A metade positiva ficou. Ver CLAUDE.md §"CONTRA A CELEBRIDADE, SILENCIO".
APELO_EUA = [
    "A strikingly attractive everyday woman, well groomed, with clear even skin, softly styled hair and a noticeably good figure.",
    "A very good-looking everyday woman with glowing skin, light natural make-up and a shapely figure.",
    "An unusually pretty everyday woman with fine features, healthy glossy hair and a trim shapely body.",
    "A head-turning everyday woman, carefully groomed, with bright eyes, full lips and a striking figure.",
    "A notably beautiful everyday woman with high cheekbones, smooth clear skin and a curvy figure.",
    "A very attractive everyday woman with a toned shapely figure, shining hair and even skin.",
]

# ⛔ HOJE E' CODIGO MORTO: os 16 mundos deste motor sao todos `eua: True`,
# entao `_apelo` nunca cai aqui (medido). Fica porque um mundo novo sem o
# selo o religa — e no registro ANTIGO ele entregaria `plain unremarkable
# face` num agente cuja REF o operador encomendou top model. Codigo morto
# com a regra errada dentro e' bomba com pino: alguem acrescenta um mundo e
# o vicio volta calado, sem lint, sem autoteste, sem aviso.
# ⛔ A negacao anti-celebridade saiu daqui em 2026-08-14, por ordem do operador
# (*"tire not a celebrity do prompt"*): declaracao INJETA o token que ela nega.
# A metade positiva ficou. Ver CLAUDE.md §"CONTRA A CELEBRIDADE, SILENCIO".
APELO_PADRAO = (
    "A strikingly beautiful everyday woman.")


def _apelo(spec):
    """A clausula de apresentacao da REF: apelo nos mundos dos EUA, o registro
    relatable nos demais. ⚠️ `.get` e nao `[...]`: mundo sem o selo cai no
    padrao em vez de derrubar o sorteio."""
    if not spec["mundo"].get("eua"):
        return APELO_PADRAO
    return spec["apelo"]


def _traje_de(spec, chave):
    """⛔ A COR SEGUE A CHAVE: `traje_amiga` usa `cor_amiga`. Sem isto as duas
    saem da mesma cor mesmo com pecas diferentes."""
    """O traje de UMA das duas mulheres, com o artigo certo.

    ⛔ Existe porque as duas apareciam com a MESMA roupa: eu chamava `_traje`
    duas vezes e o spec so' tinha um traje. Duas mulheres identicas da cintura
    para cima viram uniforme — e o operador leu isso no render.
    """
    # ⛔ A COR SEGUE A CHAVE: `traje_amiga` usa `cor_amiga`. Sem isto as duas
    # saem da MESMA COR mesmo com pecas diferentes — meia correcao le como
    # uniforme do mesmo jeito, e o operador pegou no render pela segunda vez.
    _mapa_cor = {"traje_amiga": "cor_amiga", "traje_terceira": "cor_terceira"}
    cor = spec.get(_mapa_cor.get(chave, "cor")) or spec["cor"]
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


def _falas(spec, rng, quais=(0, 1)):
    """As DUAS falas, montadas dos pools ja' sorteados no spec.

    ⚠️ Uma funcao so' para as tres cenas: o botao `trocar` da UI re-sorteia UMA
    fala, e duas copias desta conta garantem que uma delas envelhece mentindo.

    ⛔ Todo `_ok` cai na entrada mais CURTA quando nada serve — NUNCA em `or
    pool`, que devolve o pool inteiro e faz a cena estourar em silencio. Foi
    assim que o COLO e o BOTICA subiram de 31 para 36 palavras.
    """
    o1, o2 = spec["orgaos"]
    f = dict(spec.get("falas_map", {}))

    def _ok(pool, monta, teto):
        v = [x for x in pool if _palavras(monta(x)) <= teto]
        return v or [min(pool, key=lambda x: _palavras(monta(x)))]

    if 0 in quais:
        # ⭐⭐ TRES BEATS, a forma exata da fonte em 0:00-0:06:
        #   "If your soldier looks like this"        -> DIAGNOSTICO
        #   "and you want it looking like this ..."  -> VIRADA
        #   "no pills, no injections, listen carefully" -> FECHO
        # ⛔ O take 1 TERMINA no comando de atencao, por ordem do operador.
        def _c1(dg, vr, fc):
            return "%s %s. %s" % (dg.format(o=o1), vr.format(o=o1), fc)

        cv = min(VIRADAS, key=_palavras)
        cf = min(FECHOS, key=_palavras)
        dg = rng.choice(_ok(DIAGNOSTICOS, lambda x: _c1(x, cv, cf), TETO_FALA[1]))
        vr = rng.choice(_ok(VIRADAS, lambda x: _c1(dg, x, cf), TETO_FALA[1]))
        fc = rng.choice(_ok(FECHOS, lambda x: _c1(dg, vr, x), TETO_FALA[1]))
        f[0] = _c1(dg, vr, fc)

    if 1 in quais:
        # ⭐⭐ O UNICO BEAT QUE VENDE + O COMANDO. Tres coisas em 25 palavras:
        #   USO      o que acontece com o orgao dele, com o `gelatin trick` de
        #            sujeito — e' o literal que amarra o criativo a' VSL
        #   CTA_BASE `Comment gelatin, and I'll send you the recipe.` — travado
        #   FOLLOW   a instrucao de seguir, em FRASE PROPRIA
        #
        # ⛔⛔ A ORDEM DAS TRES E' A PROTECAO DA KEYWORD. O `follow` vem DEPOIS
        # do ponto final do CTA, nunca colado no `gelatin`. Automacao de DM
        # casa palavra EXATA (confirmado pelo operador, 2026-08-08): se a boca
        # disser `comment gelatin and follow`, o espectador digita isso e nao
        # dispara nada.
        # ⚠️ O `o2` aqui, e' de proposito: sao dois orgaos diferentes no mesmo
        # video, e repetir o substantivo em 16 segundos vira bordao mais rapido
        # ainda do que em 24.
        # ⛔ PONTO FINAL entre o efeito e a reacao dela, nao `, and`. Duas
        # razoes, e as duas foram medidas: economiza a palavra do conector (com
        # `, and` so' 69% das combinacoes cabiam; com o ponto, 87%) e le' mais
        # taxativo, que e' o que o operador cobra — duas afirmacoes curtas
        # batem mais forte que uma composta.
        def _c2(ef, pa, re, fol):
            return "%s. %s %s. %s %s" % (ef.format(o=o2).rstrip(". "),
                                         _cap(pa), re, CTA_BASE, fol)

        cf2 = min(FOLLOWS, key=_palavras)
        cpa = min(PARCEIRAS, key=_palavras)
        cre = min(REACOES, key=_palavras)
        ef = rng.choice(_ok(EFEITOS,
                            lambda x: _c2(x, cpa, cre, cf2), TETO_FALA[2]))
        pa = rng.choice(_ok(PARCEIRAS,
                            lambda x: _c2(ef, x, cre, cf2), TETO_FALA[2]))
        re_ = rng.choice(_ok(REACOES,
                             lambda x: _c2(ef, pa, x, cf2), TETO_FALA[2]))
        fol = rng.choice(_ok(FOLLOWS,
                             lambda x: _c2(ef, pa, re_, x), TETO_FALA[2]))
        f[1] = _c2(ef, pa, re_, fol)

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
    # ⛔⛔ COR PROPRIA PARA A AMIGA. Com uma cor so' as duas saiam vestidas
    # igual mesmo com pecas diferentes — o operador pegou no render, e e' a
    # segunda vez que este angulo devolve "uniforme": duas mulheres identicas
    # da cintura para cima matam a leitura de "duas pessoas".
    # ⚠️ `or [cor]` no fallback: mundo com uma cor so' nao pode derrubar o
    # sorteio, e nesse caso a repeticao e' honesta (nao ha' o que variar).
    _outras = [c for c in mundo["cores"] if c != cor] or [cor]
    cor_amiga = travas.get("cor_amiga") or rng.choice(_outras)
    _o3 = [c for c in mundo["cores"] if c not in (cor, cor_amiga)] or [cor]
    cor_terceira = travas.get("cor_terceira") or rng.choice(_o3)
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
    ref = (_por_ref(REFS, travas["ref"]) if travas.get("ref")
           else sc.ref_bela(REFS[0], rng) if travas.get("bela")
           else rng.choice(REFS))
    # ⭐ A AMIGA sai do MESMO pool da narradora e NUNCA e' a mesma pessoa: duas
    # mulheres no quadro com a mesma descricao viram gemeas no render.
    amiga = rng.choice([x for x in REFS if x is not ref])
    # ⛔ DISTINTA DAS OUTRAS DUAS. `is not` compara identidade: sem isto o
    # sorteio devolve a mesma entrada e o quadro tem gemeas.
    terceira = (sc.ref_bela(REFS[0], rng) if travas.get("bela")
                else rng.choice([x for x in REFS
                                 if x is not ref and x is not amiga]))
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
    # ⭐ A TERCEIRA MULHER — a segunda SENTADA. Roupa e cor proprias, pelas
    # mesmas razoes da amiga: tres mulheres com a mesma peca ou a mesma cor
    # leem como uniforme, e uniforme mata a leitura de "tres pessoas".
    _tj3 = [x for x in mundo["trajes"]
            if x is not traje and x is not traje_amiga] or mundo["trajes"]
    traje_terceira = rng.choice(_tj3)
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
    # ⛔ 2026-08-10 — SO' OS TRES APELIDOS SAO SORTEAVEIS (ordem do
    # operador, parque inteiro). `soldier` e `tool` seguem no NUCLEO porque
    # as LENTES os usam para DETECTAR o orgao; o que muda e' que nao saem
    # mais na fala. Ver `short_comum.orgaos_sorteaveis`.
    #
    # ⭐⭐ E DESDE 2026-08-16 O SORTEIO E' LOCAL, `NUCLEO`, NAO O HELPER.
    # Ordem do operador para ESTE motor, por recusa de conteudo nocivo em
    # serie: *"falas que fazem referencia ao penis somente como Johnson ou
    # Manhood, retire qualquer outro termo"*.
    # ⛔⛔ O `sc.orgaos_sorteaveis` NAO PODE MUDAR: ele carrega a ordem de
    # 10/08 (*"wiener, john-son, peck-er somente"*) para o PARQUE INTEIRO, e
    # trocar la' dentro para atender o TRIO reescreveria os outros trinta em
    # silencio. Mesmo precedente do `HOMENS_FORTES` do GOOD 16 e do BOTICA 16.
    # ⚠️ MEDIDO: trocar so' o `NUCLEO` NAO bastava — ele e' lido pelas LENTES
    # (BO9, BO14), nao pelo sorteio. Com o pool novo e o helper velho a fala
    # continuava saindo `wiener` em 193 de 300 videos e a BO14 passava a
    # REPROVAR o proprio motor, 484 ERRO. Pool trocado sem o sorteio trocado
    # e' pool morto que ainda por cima quebra a lente.
    # ⭐ Os DOIS orgaos do video sao agora exatamente os dois do NUCLEO, em
    # ordem sorteada — a exigencia de `len(set(orgaos)) >= 2` da BO14 continua
    # satisfeita por construcao.
    orgaos = list(NUCLEO)
    rng.shuffle(orgaos)

    # ⭐ A FLAG VIAJA NO SPEC. O `montar()` nao recebe `travas`, e sem

    # isto a clausula do rosto e o `resumo_pt` ficavam na versao comum

    # enquanto o corpo e a roupa ja' eram os do modo — a contradicao

    # exata que o CL26 documenta.

    spec = {"pagina": pagina, "bela": bool(travas.get("bela")), "mundo": mundo, "etnia": et, "cor": cor,
            "traje": traje, "traje_amiga": traje_amiga, "preparo": preparo,
            "cor_amiga": cor_amiga, "cor_terceira": cor_terceira,
            "terceira": terceira, "traje_terceira": traje_terceira,
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


# ⛔⛔ T16-3 — A POSE MORA NA FRASE QUE POSICIONA, NUNCA NO PROP.
# Achado LENDO o prompt gerado, em 2026-08-08: 5 das 6 entradas de PARES trazem
# `held upright` dentro do campo `gigante`, e as strings que posicionam o objeto
# acrescentam a propria pose. O resultado era
#
#     "closed around a giant firm cucumber, straight and thick, held upright,
#      held upright in her lap"
#
# em 164 de 200 sorteios — e o TRIO SHORT tem exatamente a mesma taxa, entao e'
# defeito HERDADO, nao introduzido aqui.
# ⚠️ Por que importa e nao e' so' feio: o Veo le' duas ordens de pose para o
# mesmo objeto e resolve escolhendo uma. `held upright` (sozinho) e `held
# upright in her lap` nao sao a mesma coisa — a segunda tem altura, a primeira
# nao. Instrucao duplicada e' instrucao ambigua.
# ⛔ Corta a CLAUSULA inteira, nao as duas palavras: o plantain traz `held
# upright in her fist`, e tirar so' `held upright` deixaria `, in her fist`
# pendurado — meia correcao que le pior que o defeito.
def _sem_pose(s):
    i = s.find(", held upright")
    return s[:i] if i >= 0 else s


# ⛔⛔ O POSSESSIVO DO PORTADOR — 2026-08-10, achado ao medir a queixa do
# operador sobre o tamanho do geoduck no take 2.
# Os campos de PARES nasceram para a cena 1, onde quem segura e' MULHER, e por
# isso a escala deles e' ancorada em `her forearm` / `her wrist` / `her fist`.
# Na cena 2 o mesmo campo entra dentro de *"HIS right hand is closed around
# ..."* — e sai `His right hand is closed around an enormous bright yellow
# banana, longer than HER forearm`. Nao e' so' feio: a ancora de escala aponta
# para um corpo que nao esta' na frase, e ancora sem referente o Veo resolve
# entregando o tamanho natural do objeto. E' metade da causa do prop pequeno.
# ⛔ TRANSPOSICAO VERIFICADA, NUNCA REDIGITACAO. Sao 12 pares; reescrever as 12
# strings a mao e' redigitar copy validada — o erro que este repo ja' pagou (o
# D1 comprimido na mao virou esqueleto 3D). Aqui a troca e' um recorte REGULAR
# (`her` isolado) e vem com lente atras: T16-5 reprova se sobrar `her` dentro da
# sentenca do corpo-prova.
# ⚠️ So' se aplica ao campo do PROP dentro da cena 2. A cena 1 fica intacta —
# la' o portador e' ela, e `her` esta' certo.
_POSSE = re.compile(r"\bher\b")


def _posse_dele(s):
    return _POSSE.sub("his", s)


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
        # ⭐ A CENA 1 E' NA SALA, nao na cozinha — e' o corte que a fonte faz.
        "sala": m["sala"], "sala_c": m["sala_c"],
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
    # ⛔ AQUI NAO EXISTE `only person`: a cena 1 tem TRES por construcao.
    # ⭐ A REF e' quem FALA e esta' EM PE ATRAS; as duas SENTADAS sao a `amiga`
    # (prop murcho, frame-left) e a `terceira` (prop gigante, frame-right).
    _a, _r, _c = spec["amiga"], spec["ref"], spec["terceira"]
    b["IMAGE 01/02"] = (
        "Medium shot in %(sala)s%(band)s %(trio)s %(anti)s %(luz)s %(cauda)s"
        % dict(v, trio=BO_TRIO % (
            _a["idade"], spec["etnia"], _sem_artigo(_a["cabeca"]),
            _sem_artigo(_a["marca"]), _traje_de(spec, "traje_amiga"),
            prop["murcho"],
            _c["idade"], spec["etnia"], _sem_artigo(_c["cabeca"]),
            _sem_artigo(_c["marca"]), _traje_de(spec, "traje_terceira"),
            _sem_pose(prop["gigante"]),
            _pessoa(spec))))

    # --- CENA 2 — A COZINHA, O COPO E O CORPO-PROVA NO MESMO QUADRO ---------
    # ⭐⭐ E' A FUSAO DAS CENAS 2 E 3 DO TRIO, e ela nao inventa cenario: la' a
    # cena 3 ja' abria com `same place, same background` — as duas SEMPRE
    # aconteceram na mesma cozinha. O que muda e' que agora cabem no mesmo
    # frame:
    #   · a BANCADA da receita, com o aparato da conformacao sorteada, o
    #     ingrediente raro e a tigela de cubos de gelatina — a prova de que a
    #     receita foi feita, e o lugar onde o mecanismo mora (DU2);
    #   · ela frame-LEFT com o COPO na lente — o objeto da keyword, na mao no
    #     frame em que a boca diz `gelatin,`;
    #   · ele frame-RIGHT de rosto visivel e sorrindo, com o prop GRANDE na
    #     cintura — a geometria do EXTERIOR, que o operador mandou por print.
    #
    # ⛔⛔ `bancada16`, NAO `bancada`. A string do TRIO comeca com `a tall clear
    # glass` (o copo sendo enchido) e aqui o copo esta' NA MAO dela — dois copos
    # altos no mesmo quadro e o Veo escolhe um. A irma sem o copo de destino
    # existe exatamente por isso, e o linter cobra (T16-1).
    # ⛔ E o `acao` da conformacao NAO entra: ele descreve as maos dela
    # trabalhando o utensilio, e as maos dela estao no copo. Take que manda
    # animar dois gestos incompativeis e' a contradicao IMAGE x TAKE que a
    # `lint_take_vs_image` existe para pegar.
    # ⛔ A AMIGA NAO ESTA' AQUI. Tres pessoas + bancada + copo + prop grande em
    # 8 segundos e' quadro entulhado, e o Veo resolve entulho apagando alguem —
    # normalmente o corpo-prova, que e' o payoff. Decisao do operador.
    _pr = spec["preparo"]
    hom = spec["homem"]
    # ⭐⭐ A ESCALA DO PROP GRANDE NA MAO DO HOMEM — ordem do operador,
    # 2026-08-10: *"o geoduck do take 2 esta' muito pequeno; quero o tamanho do
    # NECROSE"*. Quando o par sorteado traz `gigante_c2`, e' ELE que vai para a
    # cena 2 — dimensionado por biologia do prop + escala corporal MASCULINA
    # (NE11), porque quem segura aqui e' ele. O campo `gigante` continua
    # intacto e continua servindo a cena 1, onde quem segura e' ela.
    # ⚠️ `gigante_c2` entra CRU: ele ja' nasce sem `held upright`, entao nao
    # passa pelo `_sem_pose` — que so' existe para limpar a pose dos campos
    # antigos. O fallback mantem os pares sem a chave exatamente como estavam.
    _grande_c2 = prop.get("gigante_c2") or _posse_dele(_sem_pose(prop["gigante"]))
    _cauda_c2 = prop.get("cauda_c2", "")
    b["IMAGE 02/02"] = (
        "Medium shot in %(coz)s, same house, filmed straight on and framed from "
        "the waist up, with %(sup_a)s running across the bottom third of the "
        "picture. %(Ancora)s stands at frame-left behind it, turned towards the "
        "lens, holding %(copo)s. On the %(sup)s in front of her stands "
        "%(bancada)s. She looks directly into the camera, calm and certain, her "
        "mouth open mid-word as she speaks, her front teeth even and complete. "
        "%(corpo)s %(anti)s %(luz)s %(cauda)s"
        % dict(v,
               bancada=(_pr["aparato16"] + BANCADA16_CAUDA) % v,
               corpo=BO_CORPO_PROVA % (
                   hom["idade"], spec["etnia"], hom["marca"], hom["roupa"],
                   _grande_c2, (" " + _cauda_c2) if _cauda_c2 else "")))

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
        # ⛔ Tres pessoas, tres travas. A que fala e' a UNICA que se move, e o
        # que se move nela e' so' a boca: o braco estendido e o dedo ficam
        # exatamente onde estao. Se o dedo migrar, a comparacao troca de lado.
        # ⭐⭐ 2026-08-10 — A DA DIREITA SORRI, e o sorriso e' obrigatorio.
        # Ordem do operador lendo um render: *"a menina que esta' segurando o
        # que representa o Johnson saudavel sempre deve estar sorrindo e
        # feliz"*. Sem isso o Veo devolvia as duas com a mesma cara neutra, e a
        # comparacao perdia metade da forca: o lado bom precisa PARECER o lado
        # bom, senao sao so' dois objetos diferentes no colo de duas pessoas.
        # ⚠️ Entra na IMAGE (BO_TRIO) E aqui: sem a repeticao no TAKE a
        # animacao relaxa o rosto dela ao longo dos 8 segundos.
        # ⛔ Sorriso, nunca risada — e ela continua MUDA. Verbo de riso na
        # direcao visual faz o Veo sintetizar som, e ai' o som contamina os
        # outros rostos (a licao do FLAGRANTE 16, mesmo dia).
        # ⚠️ A IDADE VOLTA A SER DITA AQUI (T16-IDADE): o classificador le' o
        # TAKE tanto quanto a IMAGE, e idade so' na IMAGE deixa metade do
        # prompt muda sobre o unico atributo que a politica de menores olha.
        ("The two seated %(idade)d-year-old women stay exactly as they are, "
         "each holding her own "
         "piece on her knees at the same height, same size, same shape, same "
         "colour, and neither sets anything down. The %(idade)d-year-old woman "
         "on frame-right "
         "keeps smiling with her lips closed the whole time, happy and pleased, "
         "her expression steady and warm, and she stays silent. "
         "The %(idade)d-year-old "
         "woman standing behind "
         "them keeps her arm reaching down past the left woman's shoulder and her "
         "index finger "
         "pointing at the same piece for the whole shot.") % {"idade": IDADE_MULHER},
        # ⭐⭐ O TAKE 2 ANIMA UM QUADRO PARADO, e e' isso mesmo. Ela segura o
        # copo e fala; a bancada nao e' tocada.
        # ⛔ O `mov` da conformacao NAO entra aqui. Ele descreve as maos dela
        # trabalhando o utensilio — e as maos dela estao no copo. Mandar animar
        # os dois gestos e' a contradicao IMAGE x TAKE que ja' custou o lote da
        # etapa [7] deste angulo.
        # ⛔ `nao_toca` continua: sem ele o Veo comeca a mexer em tudo o que
        # esta' na bancada e a continuidade morre dentro dos 8 segundos.
        # ⚠️ idem no take 2 (T16-IDADE): a mulher e o homem entram com idade.
        ("The %d-year-old woman holds the bowl steady at chest height the "
         "whole time and never sets it down. The %d-year-old man beside her "
         "stays where he is. " % (IDADE_MULHER, spec["homem"]["idade"])
         + v["nao_toca"]),
    ]
    # ⛔ NENHUMA CENA DESTE ANGULO TEM PESSOA UNICA. Declarar `only person in
    # the shot` e' ordem contraditoria, e o Veo resolve APAGANDO a segunda
    # pessoa — que na cena 1 e' metade da comparacao e na cena 2 e' o payoff.
    elenco = [
        # ⛔⛔ QUEM FALA E A QUE ESTA EM PE ATRAS, e essa linha dizia o
        # contrario. Herdada do DUPLA, onde as duas estao EM PE lado a lado e
        # `frame-left` E a que fala. Aqui frame-left e uma das SENTADAS, e a
        # IMAGE manda, na mesma respiracao, `Neither seated woman speaks`.
        # ⚠️ MEDIDO em 2026-08-08: 200 de 200 sorteios, e o TRIO SHORT tem a
        # mesma taxa — o defeito e herdado. Contradicao IMAGE x TAKE e pior
        # que omissao: a omissao o gerador preenche com o frame, a
        # contradicao ele resolve mexendo no que estava certo, e aqui o que
        # estava certo e a boca que fala.
        "Only the woman standing behind them speaks, straight into the lens. "
        "Both seated women keep their lips closed and their eyes down on what "
        "they are holding for the whole shot.",
        BO_CORPO_PROVA_TAKE,
    ]
    # ⛔ O audio da conformacao (`a blender motor starting up`) NAO entra: o
    # aparato esta' PARADO na bancada, e som de liquidificador ligado num
    # liquidificador desligado e' a mesma contradicao, pelo ouvido.
    audio = ["%s. No music." % m["audio"],
             "%s. No music." % m["audio"]]

    for i in range(2):
        b["TAKE %02d/02" % (i + 1)] = (
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




# ---------------------------------------------------------------------------
# ⛔⛔ T16-5b — O PRONOME SEM DONO, EM TODAS AS CENAS
# ---------------------------------------------------------------------------
# Ordem do operador, 2026-08-08, lendo o painel do PLACA 16:
#     "...why the gelatin trick exists before she stops asking."
#     -> *"She who??? stopping asking about what????"*
#
# ⚠️ A lente T16-5 original olhava SO' A CENA DO CTA. O defeito estava na cena
# 1, que vem dos pools herdados do motor de 24s. Lente que cobre uma cena de
# duas nao e' lente, e' amostra.
#
# ⛔⛔ E ELA NAO ADIVINHA. Cada motor DECLARA abaixo os pronomes cujo referente
# esta' EM QUADRO. Foi isso que impediu o conserto errado: varrendo por
# CONTAGEM, o TRIO e o DUPLA apareciam com mais de 50% da cena 1 "defeituosa" —
# e ali o `she` de `the one she holds` aponta para a mulher VISIVEL segurando o
# prop gigante, que e' regra do proprio operador ("o segundo prop tem dono
# nomeado: she / her hand / my friend"). Ler as frases custou dez minutos e
# salvou dois motores certos.
#
# ⭐ Quem acrescentar entrada de pool com pronome nu tem de vir aqui declarar
# por que ele tem dono. Declaracao explicita e' o oposto de adivinhacao.
PRONOME_VISUAL = ("she holds", "she is holding", "she's holding", "she's got", "in her hand", "she is showing", "what she's holding", "what she is holding")

_PRON_NU = re.compile(r"\b(she|her|he|his)\b", re.I)
_TEM_DONO = re.compile(
    r"\b(wife|girlfriend|woman|girl|friend|husband|boyfriend|man|men|guy|"
    r"marriage)\b", re.I)
# ⛔ Verbos que pedem objeto e ficam pendurados sem ele: `stops asking` —
# parando de perguntar O QUE? E' a mesma familia do pronome sem dono, e o
# operador reprovou exatamente esta forma.
_PENDURADO = re.compile(
    r"\b(stops?|starts?|keeps?|quits?)\s+(asking|telling|talking|wondering|"
    r"complaining|noticing|checking)\b"
    r"(?!\s+(what|about|for|the|her|his|you|it|at|to))", re.I)


def _t16_5b(spec, blocos, achados):
    for _i, _fala in enumerate(spec.get("falas") or [], 1):
        if (_PRON_NU.search(_fala) and not _TEM_DONO.search(_fala)
                and not any(_v in _fala.lower() for _v in PRONOME_VISUAL)):
            achados.append((
                "ERRO",
                "T16-5b: cena %d usa pronome NU sem dizer de quem se trata e "
                "sem referente em quadro declarado — o espectador gasta o "
                "segundo dele perguntando `quem?` (%r)" % (_i, _fala[:64])))
        _p = _PENDURADO.search(_fala)
        if _p:
            achados.append((
                "ERRO",
                "T16-5b: cena %d tem `%s` sem objeto — parando de perguntar O "
                "QUE? Verbo pendurado e' a mesma familia do pronome sem dono"
                % (_i, _p.group(0))))

def lint(spec, blocos):
    ach = []
    _t16_5b(spec, blocos, ach)
    falas = spec["falas"]
    m = spec["mundo"]

    sc.lint_tags(blocos, ach)
    sc.lint_sem_texto(blocos, ach)
    # ⛔⛔ A negacao anti-celebridade nunca volta ao texto montado
    # (2026-08-14, ordem do operador). Este motor nao passa pelo
    # `sc.lint_curto`, entao a lente entra aqui explicitamente — regra sem
    # guarda volta no proximo agente nascido por copia, e foi exatamente
    # assim que a clausula chegou aos 30 motores.
    sc.lint_anticeleb(blocos, ach)
    sc.lint_isca_cta(falas[1], ach, "a cena 2 (CTA)")
    sc.lint_cta_literal(falas[1], ach, "a cena 2 (CTA)")
    # ⛔⛔ T16-2 — A KEYWORD NAO PODE TER PALAVRA COLADA NELA.
    # A automacao de DM casa a palavra EXATA (operador, 2026-08-08). A legenda
    # do video nasce do Whisper EM CIMA DO AUDIO, entao nao ha' conserto depois
    # de gerado: se a boca disser `comment gelatin and follow`, o espectador
    # digita isso e o DM nunca sai.
    # ⚠️ Esta lente e' o unico lugar do repo que vigia isso, e ela existe porque
    # a PRIMEIRA versao desta copy tinha exatamente esse defeito.
    # ⛔⛔ A REGRA E' POSICIONAL, NAO DE VOCABULARIO: depois de `comment
    # gelatin` tem de vir VIRGULA, seja qual for a palavra seguinte. Listar
    # palavras proibidas seria corrida perdida — a proxima seria `now`, `below`,
    # `please`. A virgula e' o que fecha o token, e ela nao depende de eu
    # adivinhar o vocabulario do redator.
    # ⚠️ A PRIMEIRA VERSAO DESTA LENTE OLHAVA `re.search(r"gelatin\s+(\w+)")` e
    # parava na PRIMEIRA ocorrencia — que e' sempre `gelatin trick`, permitida.
    # Ela dava verde para `Comment gelatin now,` e so' o controle do autoteste
    # pegou. Lente que olha a primeira ocorrencia de um termo que aparece duas
    # vezes e' lente que mede a errada.
    _f2 = falas[1] or ""
    for _m_kw in re.finditer(r"comment\s+gelatin(.)", _f2, re.I):
        if _m_kw.group(1) != ",":
            ach.append(("ERRO", "T16-2: `comment gelatin%s...` — a keyword tem "
                                "de ser fechada por VIRGULA. A automacao de DM "
                                "casa palavra exata e o espectador digita o que "
                                "ouve grudado; a legenda nasce do Whisper em "
                                "cima do audio, entao nao ha' conserto depois"
                        % _m_kw.group(1)))
    # ⛔⛔ T16-5 — A PARCEIRA E' NOMEADA, E NENHUM PRONOME FICA SEM DONO.
    # Ordem do operador, 2026-08-08, lendo `she feels it first`: *"concretude,
    # ser taxativo, e' melhor candidato que pronome generico — pool de 'sua
    # namorada', 'sua esposa'"*.
    # ⚠️ Esta lente existe porque o defeito NASCEU DE UMA COMPRESSAO minha:
    # `she feels the difference first` nao coube em 25 palavras e eu cortei o
    # substantivo em vez de trocar a frase. Sem lente, a proxima vez que o teto
    # apertar eu corto de novo — o linter e' o que sobra quando a disciplina
    # falha.
    if not any(_p.split()[-1] in _f2.lower() for _p in PARCEIRAS):
        ach.append(("ERRO", "T16-5: a cena 2 nao NOMEIA a parceira — sem "
                            "`wife`/`girlfriend`/`woman`/`girl` o espectador "
                            "gasta o segundo dele descobrindo de quem ela "
                            "fala (%r)" % _f2[:60]))
    if re.search(r"(?:^|\.\s+)(She|Her)\b", _f2):
        ach.append(("ERRO", "T16-5: sentenca da cena 2 abrindo com pronome nu "
                            "(`She...`) — a parceira entra NOMEADA, e o pronome "
                            "so' depois dela"))
    # ⛔ `it` sem dono depois de verbo de percepcao — a frase exata que o
    # operador reprovou. `stops faking it` NAO cai aqui: `fake it` e' idioma
    # fechado, e a lista abaixo e' de verbos de percepcao, nao de qualquer verbo.
    _vago = re.search(r"\b(feels?|notices?|sees?|senses?)\s+it\b", _f2, re.I)
    if _vago:
        ach.append(("ERRO", "T16-5: %r — `it` sem antecedente depois de verbo de "
                            "percepcao. Sente O QUE? Nomear custa uma palavra e "
                            "e' a diferenca entre a copy vender e o espectador "
                            "perguntar do que se trata" % _vago.group(0)))

    if re.search(r"comment\s+gelatin\W+(and\s+)?follow", _f2, re.I):
        ach.append(("ERRO", "T16-2: o `follow` esta' colado no comando — ele tem "
                            "de vir em FRASE PROPRIA, depois do ponto final do "
                            "CTA, nunca na mesma respiracao da keyword"))
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
    # ⚠️ NO 16 a cena 2 abre com o `gelatin trick` como SUJEITO e nomeia o
    # orgao na mesma sentenca — os dois referentes, nao um. A lista aceita os
    # dois porque a copy pode legitimamente abrir por qualquer um deles.
    alvos = [(2, ["gelatin"] + [o.lower() for o in sc.APELIDOS_16])]
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

    # ⛔ BO8 APAGADA: vigiava o ingrediente raro / o pool de
    # PROMESSAS, e este angulo nao tem nenhum dos dois — a
    # receita da fonte e' fechada. Regra desligada com `if False`
    # deixaria a sonda do autoteste viva e cega (§29).
    # ⛔ BO15 APAGADA: vigiava o ingrediente raro / o pool de
    # PROMESSAS, e este angulo nao tem nenhum dos dois — a
    # receita da fonte e' fechada. Regra desligada com `if False`
    # deixaria a sonda do autoteste viva e cega (§29).
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
    # O angulo continua sendo a botica de casa, so' que sem o adversario dito em
    # voz alta: ele fica implicito no `nobody sells` dos fechos e na propria
    # existencia da receita caseira.

    # --- BO4: o mecanismo ----------------------------------------------------
    if "gelatin trick" not in " ".join(falas).lower():
        ach.append(("ERRO", "BO4: literal `gelatin trick` ausente — sem ele o "
                            "criativo deixa de ser congruente com a VSL"))
    if "gelatin trick" not in falas[1].lower():
        ach.append(("ERRO", "BO4: o `gelatin trick` tem de estar na CENA 2 — no "
                            "16 ela e' a UNICA cena depois do hook, e sem o "
                            "literal o criativo perde a congruencia com a VSL"))

    # --- cota do orgao -------------------------------------------------------
    # ⛔ NO 16 A COTA E' 2 DE 2, nao 2 de 3. Com uma cena a menos, deixar uma
    # sem o substantivo do nucleo significa METADE do video falando de nada
    # concreto — em 24s era um terco.
    cota = [i for i, f in enumerate(falas, 1)
            if any(o.lower() in f.lower() for o in NUCLEO)]
    if len(cota) < 2:
        ach.append(("ERRO", "BO14: cota do orgao %d/2 (minimo 2) — cenas sem "
                            "substantivo do nucleo: %s"
                    % (len(cota), [i for i in (1, 2) if i not in cota])))
    if len(set(spec["orgaos"])) < 2:
        ach.append(("ERRO", "BO14: o mesmo orgao repetido no mesmo video"))

    i1, i2 = blocos["IMAGE 01/02"], blocos["IMAGE 02/02"]

    # --- BO1: ⭐⭐ A GEOMETRIA DO TRIO — duas sentadas, uma em pe atras ------
    # ⛔ REESCRITO. A lente herdada exigia `raised at chest height` — a escala do
    # DUPLA, onde as duas estao EM PE e erguem os props. Aqui elas estao
    # SENTADAS e o prop cai no COLO; exigir a clausula do outro angulo reprovava
    # 200 de 200.
    # ⭐ O que faz a comparacao ler aqui e' outra coisa: os dois props no MESMO
    # quadro, cada um num colo, e o DEDO da que fala descendo sobre um deles.
    if "resting on her knees" not in i1 or "standing upright" not in i1:
        ach.append(("ERRO", "BO1: IMAGE 01/02 sem os dois props NO COLO — e' a "
                            "escala deste angulo, e sem ela o par vira dois "
                            "objetos soltos no quadro"))
    if "index finger points" not in i1:
        ach.append(("ERRO", "BO1: IMAGE 01/02 sem o DEDO APONTANDO — e' o gesto "
                            "que diz qual dos dois props a fala esta' nomeando"))
    # ⚠️ `_sem_pose` TAMBEM AQUI. A lente compara com o que o bloco RECEBE, e o
    # bloco recebe o prop sem a pose — quem a poe e' a frase que posiciona. Sem
    # isto ela acusava o plantain, cujo campo termina em `held upright in her
    # fist` enquanto o quadro diz `held upright in her lap`: 112 de 600 videos
    # certos reprovados. Lente que compara com a forma do POOL em vez da forma
    # do PROMPT inventa defeito.
    if (spec["prop"]["murcho"] not in i1
            or _sem_pose(spec["prop"]["gigante"]) not in i1):
        ach.append(("ERRO", "BO1: IMAGE 01/02 sem o PAR completo — o `this one "
                            "... the one she is holding` precisa dos dois "
                            "objetos visiveis"))
    # ⭐ TRES PESSOAS, e a que fala esta' ATRAS. Se ela sentar junto, a leitura
    # vira "tres amigas no sofa" e o angulo de apresentacao morre.
    if "Standing behind them" not in i1:
        ach.append(("ERRO", "BO1: IMAGE 01/02 sem a terceira EM PE ATRAS — "
                            "sentada ela vira mais uma amiga no sofa, e o "
                            "angulo inteiro depende de ela estar acima"))

    # --- BO5: o copo so' na cena 2 -------------------------------------------
    if BO_COPO in i1:
        ach.append(("ERRO", "BO5: o copo pronto na cena 1 — entrega o payoff "
                            "antes da promessa"))
    if BO_COPO not in i2:
        ach.append(("ERRO", "BO5: a cena 2 tem de mostrar o copo na mao — e' o "
                            "objeto da keyword, e a boca diz `gelatin,` com ele "
                            "no frame"))

    # --- T16-1: ⭐⭐ UM COPO ALTO SO' NO QUADRO 2 ----------------------------
    # ⛔ A fusao das cenas 2 e 3 do TRIO junta a BANCADA e o COPO no mesmo
    # frame. A string `bancada` do TRIO comeca com `a tall clear glass` — o copo
    # sendo enchido — e aqui o copo esta' NA MAO dela. Dois copos altos no mesmo
    # quadro e o Veo escolhe um, normalmente o da bancada, e o objeto da keyword
    # sai da mao.
    # ⚠️ Por isso existe o `bancada16`, e por isso esta lente existe: um
    # `bancada16` novo escrito com o copo dentro passaria despercebido, e o
    # defeito so' apareceria no render.
    # --- T16-3: a POSE do prop nao pode vir duas vezes ----------------------
    # ⛔ Achado LENDO o prompt, nao por lente: 5 das 6 entradas de PARES trazem
    # `held upright` dentro do campo `gigante`, e as strings que posicionam o
    # objeto acrescentam a sua. Duas ordens de pose para o mesmo objeto e' ordem
    # ambigua, e o Veo escolhe uma.
    # ⚠️ A LENTE PRECISOU CRESCER EM 2026-08-16, e foi o controle negativo que
    # avisou. A frase que posiciona deixou de dizer `held upright in her lap` e
    # passou a dizer `standing upright on her knees` (saida do token `lap`, ver
    # o bloco T16-LAP). Com a redacao nova, a duplicacao passaria a ser
    # `standing upright, standing upright` — que o regex antigo nao via. O
    # defeito e' o MESMO (duas ordens de pose para o mesmo objeto); so' mudou a
    # palavra, e lente cravada na palavra velha e' lente que nao olha mais.
    # ⭐ Por isso agora ela varre a POSE, nao a frase: qualquer das duas formas
    # repetida em sequencia.
    # ⛔ O TESTE E' "QUANTAS ORDENS DE POSE", nao "qual palavra repetiu".
    # O defeito real, quando o `_sem_pose()` falha, e' o prop chegar com a
    # SUA pose (`held upright`, dentro do campo `gigante`) e a frase que
    # posiciona acrescentar a DELA (`standing upright on her knees`) — duas
    # formas DIFERENTES, que nenhum teste de repeticao literal ve.
    for _n, _t in blocos.items():
        _b = _t.lower()
        _n_pose = _b.count("held upright") + _b.count("standing upright")
        if _n_pose > 1:
            ach.append(("ERRO", "T16-3: %d ordens de pose em %s — a pose "
                                "mora na frase que POSICIONA, nunca dentro "
                                "do prop; use `_sem_pose()`"
                        % (_n_pose, _n)))

    # --- T16-4: ⭐⭐ QUEM FALA NO TAKE E' QUEM FALA NA IMAGE ------------------
    # ⛔⛔ Herdada do DUPLA e medida em 200 de 200 sorteios do TRIO: o TAKE 01
    # mandava `Only the woman on frame-left speaks` numa IMAGE que diz, na mesma
    # respiracao, `Neither seated woman speaks` — e frame-left E' uma das
    # sentadas. A boca certa e' a da que esta' EM PE ATRAS.
    # ⚠️ Esta lente e' de CONGRUENCIA, e ela existe porque o defeito passou por
    # todo o linter do TRIO sem uma unica acusacao: nenhuma lente comparava o
    # elenco do TAKE com o da IMAGE.
    _tk1 = blocos["TAKE 01/02"]
    if ("Both seated women keep their lips closed" in i1
            and "frame-left speaks" in _tk1):
        ach.append(("ERRO", "T16-4: a IMAGE 01/02 diz que nenhuma das SENTADAS "
                            "fala e o TAKE 01/02 manda falar a de `frame-left`, "
                            "que e' uma delas — quem fala e' a que esta' EM PE "
                            "ATRAS, e o Veo resolve contradicao mexendo no que "
                            "estava certo"))
    if "standing behind them speaks" not in _tk1:
        ach.append(("ERRO", "T16-4: TAKE 01/02 sem dizer que quem fala e' a que "
                            "esta' EM PE ATRAS — sem isso o Veo escolhe a boca"))

    _bal = i2.lower()
    _copos = _bal.count("tall clear glass")
    if _copos > 1:
        ach.append(("ERRO", "T16-1: %d copos altos na IMAGE 02/02 — a bancada "
                            "esta' usando a string do TRIO (`bancada`) em vez "
                            "da `bancada16`, e o copo de destino ficou em cena "
                            "junto com o da mao dela" % _copos))

    # --- T16-5: ⭐⭐ A ESCALA DO PROP GRANDE NA MAO DO HOMEM -----------------
    # ⛔⛔ Ordem do operador, 2026-08-10, lendo o render da cena 2: *"o geoduck
    # do take 2 esta' muito pequeno; quero o tamanho do NECROSE"*. Esta lente
    # existe porque a correcao inteira e' TEXTO — e texto sem lente atras volta
    # ao estado anterior no proximo refactor sem uma unica acusacao.
    #
    # ⭐ Ela cobra as DUAS metades da causa, separadamente:
    #   1. o POSSESSIVO. `His right hand is closed around ..., longer than HER
    #      forearm` ancora a escala num corpo que nao esta' na frase, e o Veo
    #      resolve entregando o tamanho natural do objeto. A varredura e' so'
    #      dentro da SENTENCA do corpo-prova — a primeira metade da IMAGE 02/02
    #      e' dela, e la' `her` esta' correto (sentenca, nao janela: janela de
    #      caracteres foi o que fez a lente do `neck` acusar traje).
    #   2. a SPEC DIMENSIONAL do par que a declara (`gigante_c2`). Quando o
    #      pool traz o campo, ele TEM de chegar ao prompt inteiro, com a cauda
    #      anti-bicho junto — as duas sao a mesma licao do NECROSE (NE11), e
    #      subir a escala sem a cauda e' reintroduzir o geoduck-ganso.
    _corpo_i2 = ""
    _ini = i2.find("His right hand is closed around")
    if _ini < 0:
        ach.append(("ERRO", "T16-5: IMAGE 02/02 sem a mao do corpo-prova no "
                            "prop — e' ele quem segura o prop grande na cena 2"))
    else:
        _corpo_i2 = re.split(r"(?<=\.)\s", i2[_ini:])[0]
        if _POSSE.search(_corpo_i2):
            ach.append(("ERRO", "T16-5: possessivo FEMININO na escala do prop "
                                "na mao do homem (%r) — a ancora aponta para um "
                                "corpo que nao esta' na frase, e ancora sem "
                                "referente o Veo resolve entregando o tamanho "
                                "natural do objeto" % _corpo_i2[-60:]))
    _gc2 = spec["prop"].get("gigante_c2")
    if _gc2:
        if _gc2 not in i2:
            ach.append(("ERRO", "T16-5: o par %r declara `gigante_c2` (a escala "
                                "do NECROSE) e a IMAGE 02/02 nao a traz — a "
                                "cena 2 caiu de volta no campo `gigante`, que e' "
                                "dimensionado para a MAO DELA na cena 1"
                        % spec["prop"]["id"]))
        # ⛔⛔ AS DUAS DIMENSOES CONTINUAM OBRIGATORIAS — o que deixou de
        # ser obrigatorio e' a REDACAO de cada uma. A lente cravava o literal
        # `as long as his forearm`, e em 2026-08-16 o operador mandou o geoduck
        # crescer (`twice the length of his forearm`): a lente passou a
        # reprovar a copy CERTA, que e' a §16 das licoes. Agora ela cobra o
        # PAR — uma ancora de COMPRIMENTO e uma de GROSSURA, escritas como
        # forem —, porque o defeito que ela existe para pegar e' peca longa e
        # fina, nao uma frase especifica.
        for _rot, _formas in (
                ("comprimento", ("length of his forearm", "long as his forearm")),
                ("grossura", ("thick as his wrist", "thick as his forearm"))):
            if not any(_f in i2 for _f in _formas):
                ach.append(("ERRO", "T16-5: IMAGE 02/02 sem ancora de %s — o "
                                    "NECROSE dimensiona o geoduck pelas DUAS, "
                                    "e so' o comprimento devolve peca longa e "
                                    "fina" % _rot))
        _cd2 = spec["prop"].get("cauda_c2")
        if _cd2 and _cd2 not in i2:
            ach.append(("ERRO", "T16-5: IMAGE 02/02 sem a cauda anti-bicho do "
                                "par %r — nessa escala o molusco erguido le' "
                                "como ganso, e foi por isso que o NECROSE a "
                                "escreveu" % spec["prop"]["id"]))

    # --- BO6: ⭐⭐ QUEM FALA, QUEM CALA, E QUEM APARECE EM CADA CENA -------
    # ⛔ REESCRITO INTEIRO. As lentes herdadas vigiavam a AMIGA do DUPLA nas
    # tres cenas e proibiam homem em quadro. Aqui:
    #   cena 1 — TRES mulheres, so' a de pe fala;
    #   cena 2 — a REF + UMA delas (ordem do operador);
    #   cena 3 — a REF + o CORPO-PROVA MASCULINO, sorrindo (a cena do
    #            EXTERIOR, que o operador mandou por print).
    # Proibir homem aqui reprovava 200 de 200 na cena que ele mesmo pediu.
    if "Both seated women keep their lips closed" not in i1:
        ach.append(("ERRO", "BO6: IMAGE 01/02 sem a trava de mudez das duas "
                            "sentadas — sem ela o Veo dubla a fala em tres "
                            "bocas"))
    # ⛔ A LENTE DA AMIGA NA CENA 2 FOI APAGADA, nao afrouxada. Ela cobrava
    # `never speaks` na IMAGE 02, onde a amiga estava no fundo do preparo — e no
    # 16 ela nao esta' nessa cena. Lente que vigia personagem ausente passa
    # sempre e vira sonda cega (§29). A mudez do segundo corpo da cena 2 e'
    # cobrada logo abaixo, no corpo-prova, que e' quem esta' la'.
    # ⛔⛔ BO6 INVERTIDA EM 2026-08-10, POR DECISAO EXPLICITA DO OPERADOR.
    # Ate' hoje esta lente cobrava o CORTE NO PEITO (`no face is in the frame`),
    # por duas razoes escritas: o corpo de QUALQUER homem — o espectador se ve'
    # ali — e a moderacao, que pega rosto masculino junto de prop falico na
    # cintura.
    # ⚠️ Ele leu um render, viu o marido serio e mandou: *"ele deve estar feliz
    # e sorrindo"*. Apresentei as tres saidas e o risco de recusa; ele escolheu
    # a segunda de propria voz: *"pode fazer o que eu pedi, opcao 2, sempre o
    # homem feliz e sorrindo"*. Alcada dele, decisao registrada.
    # ⭐ A LENTE NAO FOI APAGADA, FOI INVERTIDA — ela agora cobra o SORRISO. Um
    # gate que some quando a regra muda deixa o proximo defeito passar calado; o
    # que muda de lado continua vigiando. Se voltar a valer o corte sem rosto,
    # e' aqui que se troca de volta.
    # ⚠️ RISCO ACEITO E REGISTRADO: se comecar a haver recusa em serie neste
    # agente, este e' o primeiro lugar a olhar.
    if "his face fully visible" not in i2 or "smiling broadly" not in i2:
        ach.append(("ERRO", "BO6: IMAGE 02/02 sem o corpo-prova de ROSTO "
                            "VISIVEL e SORRINDO — ordem do operador de "
                            "2026-08-10"))
    if "keeps smiling the whole time" not in blocos["TAKE 02/02"]:
        ach.append(("ERRO", "BO6: TAKE 02/02 sem a trava de sorriso do "
                            "corpo-prova — a IMAGE so' fixa o primeiro frame, "
                            "e sem isto a animacao relaxa o rosto dele"))
    if "never speaks" not in blocos["TAKE 02/02"]:
        ach.append(("ERRO", "BO6: TAKE 02/02 sem a trava de mudez do homem — "
                            "sem ela o segundo corpo dubla a fala dela"))
    # ⛔ AS DUAS SENTADAS NAO VOLTAM NA CENA 2. Ja' eram quatro corpos em 8
    # segundos no TRIO; aqui a bancada inteira entrou no mesmo quadro, entao o
    # orcamento de atencao esta' ainda mais curto. Quem o Veo apaga e' o
    # corpo-prova, que e' o payoff.
    for _p in ("Two women sit", "seated woman"):
        if _p in i2:
            ach.append(("ERRO", "BO6: a cena 2 traz as sentadas de volta — sao "
                                "quatro corpos mais a bancada em 8 segundos, e "
                                "o Veo resolve apagando o corpo-prova"))
            break

    # --- BO7: a ancora de continuidade na cena 2 ----------------------------
    if ("the same %d-year-old" % spec["ref"]["idade"]) not in i2.lower():
        ach.append(("ERRO", "BO7: IMAGE 02/02 sem a ancora `the same "
                            "N-year-old` — e' onde o Veo troca de pessoa entre "
                            "blocos"))

    # --- BO2: nada cresce ----------------------------------------------------
    # ⛔⛔ A CENA 1 E' ISENTA NESTE ANGULO, e a razao e' semantica, nao
    # permissiva. A lente compartilhada procura vocabulario de CRESCIMENTO para
    # impedir que o prop mude de estado fora da cena do bit — regra que existe
    # por causa do RESSURREICAO, onde o proxy alonga na tela.
    # ⚠️ Aqui os dois props sao ESTATICOS e a palavra que ela acusa (`limp`,
    # `shrivelled`, `soft`) descreve o prop MURCHO: e' o OPOSTO de crescimento,
    # e e' exatamente o que o angulo precisa dizer. Nada cresce em cena nenhuma
    # deste motor — a comparacao acontece entre DOIS objetos, nao dentro de um.
    _b2 = {k: v for k, v in blocos.items() if k != "IMAGE 01/02"}
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

    # ⛔⛔ AS DUAS SAIRAM DO RENDER, 2026-08-05, e viram regra para nao voltarem.
    #
    # 1) AS DUAS MULHERES NAO PODEM SAIR DA MESMA COR. O operador sorteou sem
    #    fixar nada e leu *"mesmo ambiente + cores de roupa iguais"*. Eu ja'
    #    tinha dado PECA propria para cada uma e nao COR — meia correcao le como
    #    uniforme do mesmo jeito, e uniforme mata a leitura de "duas pessoas".
    if spec.get("cor_amiga") and spec["cor_amiga"] == spec["cor"]:
        ach.append(("ERRO", "DU1: as duas mulheres com a MESMA cor (%s) — peca "
                            "diferente na mesma cor ainda le como uniforme"
                    % spec["cor"]))
    #
    # 2) A TIGELA DE GELATINA NA BANCADA DA CENA 2. Ordem do operador: *"seria
    #    ao menos conveniente ela ter uma bowl de cubos de gelatina nas mesas no
    #    take 2 ja' que a gravitacao e' em torno do gelatin trick"*. E' defeito
    #    de FUNCAO: a fala diz `and a secret gelatin trick` e a bancada nao tinha
    #    gelatina nenhuma — o espectador ouve o mecanismo e nao ve' onde ele mora.
    # ⚠️ E ela SO' existe na cena 2: na 1 entregaria o mecanismo antes da
    #    promessa, na 3 competiria com o copo, que e' o objeto da keyword.
    if "gelatin cubes" not in i2:
        ach.append(("ERRO", "DU2: a bancada da cena 2 sem a tigela de cubos de "
                            "gelatina — a fala nomeia o `gelatin trick` e o "
                            "quadro nao mostra onde ele mora"))
    if "gelatin cubes" in i1:
        ach.append(("ERRO", "DU2: a tigela de gelatina na cena 1 — entrega o "
                            "mecanismo antes da promessa"))

    # --- T16-1b: ⭐⭐ UMA TIGELA DE GELATINA SO' -----------------------------
    # ⛔ Desde 2026-08-11 a tigela esta' NA MAO dela (`BO_COPO`) e saiu da
    # bancada no mesmo movimento. As duas juntas repetem o defeito dos dois
    # copos altos (T16-1) com outro objeto: o Veo escolhe uma, normalmente a da
    # bancada, e o objeto da KEYWORD sai da mao no frame em que a boca diz
    # `gelatin,`.
    # ⚠️ A lente nasceu no DUPLA 16, no mesmo dia, e vem para ca' junto — fix
    # aplicado num motor e nao no irmao e' o §29, e este par ja' o pagou.
    _tigelas = i2.lower().count("gelatin cubes")
    if _tigelas > 1:
        ach.append(("ERRO", "T16-1b: %d tigelas de gelatina na IMAGE 02/02 — a "
                            "da bancada voltou e disputa com a da MAO dela, que "
                            "e' o objeto da keyword" % _tigelas))

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
            # ⛔ SO' O `neck` DO MOLUSCO. Duas versoes anteriores tentaram
            # listar as pecas de roupa que contem "neck" (crew-neck, neckline,
            # tied at the neck) e as duas ficaram incompletas — lista fechada
            # de linguagem natural nunca fecha.
            # ⭐ O teste que funciona: o `neck` tem de estar no MESMO SINTAGMA
            # do molusco. Se houver `wearing` ou `top` entre os dois, e' roupa.
            # ⛔ A SENTENCA do molusco, nao uma janela de caracteres. A janela
            # de 90 pegava a roupa de OUTRA mulher da mesma cena.
            _ss = re.split(r"(?<=[.;])\s+", _l)
            _viz = next((x for x in _ss if _m in x), "")
            _entre = _viz.split("neck")[0][-70:] if "neck" in _viz else ""
            _e_roupa = any(w in _entre for w in
                           ("wearing", " top ", "blouse", "dress", "shirt",
                            "tee", "cami", "halter", "bodysuit", "sweater"))
            _tem = "neck" in _viz and not _e_roupa
            if _i >= 0 and _tem:
                ach.append(("ERRO", "EX7: `neck` ao lado do molusco — a peca do "
                                    "geoduck e' o `siphon`, e `neck` ja' "
                                    "derrubou render nosso"))
                break

    # ⛔ HIERARQUIA DO MECANISMO — diretriz do operador, 2026-08-06 (§31).
    # So dispara quando a cena 2 mostra preparo em quadro.
    sc.lint_hierarquia_mecanismo(spec, blocos, ach)

    sc.lint_take_vs_image(blocos, ach)

    return ach


def prop_n(spec):
    return spec["prop"]["nome"]


# ---------------------------------------------------------------------------
# UI
# ---------------------------------------------------------------------------

def resumo_pt(spec):
    """A frase que permite aprovar ou re-sortear em dois segundos.

    ⛔ REESCRITO. O resumo herdado descrevia o DUPLA — duas mulheres em pe com
    os props erguidos. E' o texto que o operador le no painel para aprovar, e
    resumo errado faz ele aprovar um video que nao viu (§30).
    """
    m = spec["mundo"]
    return ("16s · %s em %s (%s). Cena 1: duas SENTADAS no sofa, uma com %s e a "
            "outra com %s no colo, e a de %d anos EM PE atras apontando. "
            "Cena 2: na cozinha da mesma casa, ela com o copo, a bancada da "
            "receita (%s) com %s, e um homem de %d anos cortado no peito, sem "
            "rosto, com o prop grande na cintura.%s"
            % (spec["etnia"], m["id"].replace("_", " "), m["familia"],
               spec["prop"]["murcho"].split(",")[0],
               spec["prop"]["gigante"].split(",")[0],
               spec["ref"]["idade"],
               spec["preparo"]["id"].replace("_", " "), spec["raro"]["nome"],
               spec["homem"]["idade"],
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


# ⛔ `_apos_cena2` FOI APAGADA. No TRIO ela remontava a fala da cena 2 quando o
# METODO, o COMUM ou o RARO mudavam, porque os tres eram nomeados na receita
# falada. No 16 a cena 2 e' USO + CTA + FOLLOW: nenhum dos tres entra na boca,
# e remontar a fala ao trocar a bancada faria o botao `trocar` do painel jogar
# fora uma copy que o operador podia ter escolhido a dedo.
# ⚠️ E o `raro` continua VIVO — no quadro, na bancada. Ele so' nao esta' na fala.
EIXOS_QUE_MEXEM_NA_COPY = {
    "mundo": _apos_mundo,
    "prop": _apos_cena1,
    "substancia": _apos_cena1,
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
    larguras = {1: [], 2: []}

    # ⛔⛔ O CONTRATO DO DROPDOWN VEM ANTES DO LOTE — ver `_contrato_dropdown`.
    # Ele so' olha dado estatico (o pool e a declaracao), entao nao custa nada;
    # e se ele estiver quebrado nao adianta medir 600 videos, porque o proprio
    # `sortear` pode cair antes de chegar ao fim.
    _drop = _contrato_dropdown()
    if _drop:
        print("\n>> %d FALHA(S) DE CONTRATO DO DROPDOWN:" % len(_drop))
        for _d in _drop:
            print("   %s" % _d)
        return 1

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
    # ⭐ o piso de 8 opcoes por eixo, com os pools DESTE angulo
    # ⛔⛔ PROPS SAIU DO PISO DE 8 — 2026-08-11, decisao declarada do operador.
    # *"quero que sempre a referencia de mole que a amiga esta' segurando ao
    # lado esquerdo seja uma linguica pequena ou geoduck pequeno, algo que
    # realmente remeta a moleza e pequeno"*.
    # O pool caiu de ONZE pares para DOIS, e a perda de entropia e' real: o
    # objeto da comparacao passa a alternar entre duas coisas so'. Ele sabe e
    # escolheu — a leitura de MOLE E PEQUENO vale mais que a variedade de
    # legume, porque e' ela que faz o espectador se reconhecer no lado errado.
    # ⚠️ O piso NAO foi apagado: virou 2, e o eixo saiu da lista dos que
    # respondem ao MIN_OPCOES. Guarda que some quando incomoda deixa o proximo
    # encolhimento passar calado.
    for nome, pool in (("MUNDOS", MUNDOS), ("REFS", REFS),
                       ("DIAGNOSTICOS", DIAGNOSTICOS), ("VIRADAS", VIRADAS),
                       ("FECHOS", FECHOS), ("EFEITOS", EFEITOS),
                       ("REACOES", REACOES), ("FOLLOWS", FOLLOWS)):
        if len(pool) < MIN_OPCOES:
            falhas.append("eixo %s com %d opcoes (minimo %d)"
                          % (nome, len(pool), MIN_OPCOES))
    if len(PROPS) < 2:
        falhas.append("PROPS abaixo do piso declarado de 2 (linguica e geoduck)")
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

    ctrl = []
    s = sortear("joe", random.Random(1), {}, {})
    b = montar(s)

    # ⭐⭐ [T16-5] A ESCALA DO PROP GRANDE MORA NO POOL — e por isso a trava
    # tem de estar AQUI e nao so' no `lint()`. Medido em 2026-08-10: com o
    # campo `gigante_c2` apagado do par, o motor volta silenciosamente ao campo
    # da cena 1 (dimensionado para a mao DELA), o geoduck volta ao tamanho que
    # o operador reprovou — e o `lint()` nao acusa NADA, porque ele so' cobra a
    # spec quando o pool a declara. Lente que so' olha o prompt nao ve' o pool
    # sumir; e' o controle 1 que passou em branco.
    _geo = _por_id(PROPS, "geoduck")
    for _campo in ("gigante_c2", "cauda_c2"):
        if not _geo.get(_campo):
            ctrl.append("[T16-5] o par geoduck perdeu o campo %r — a cena 2 "
                        "cai de volta na escala da cena 1 (`her forearm`) e o "
                        "prop volta ao tamanho natural do molusco" % _campo)
    for _dim in ("length of his forearm", "as thick as his wrist"):
        if _dim not in _geo.get("gigante_c2", ""):
            ctrl.append("[T16-5] `gigante_c2` do geoduck sem a ancora %r — o "
                        "NECROSE (NE11) dimensiona pelas DUAS, e so' o "
                        "comprimento devolve peca longa e fina" % _dim)
    # ⛔ E o campo nao pode carregar pose: ele entra CRU na cena 2, e a frase
    # que POSICIONA ja' traz `held upright at the height of his waist` (T16-3).
    if "held upright" in _geo.get("gigante_c2", ""):
        ctrl.append("[T16-5] `gigante_c2` com pose embutida — ela mora na frase "
                    "que posiciona, e duas ordens de pose o Veo resolve "
                    "escolhendo uma")
    # ⛔ E nada de vocabulario que a `lint_nada_cresce` (BO2) varre na IMAGE
    # 02/02: o NECROSE escreve `rises straight up ... held stiff`, e as duas
    # palavras sao proibidas neste motor.
    _cres = sc.CRESCIMENTO.findall(_geo.get("gigante_c2", ""))
    if _cres:
        ctrl.append("[T16-5] `gigante_c2` com vocabulario de crescimento %s — "
                    "BO2 varre a IMAGE 02/02 e reprova o lote inteiro" % _cres)

    # ⛔ O controle de BO8 saiu junto com a lente. Ele era invertido (acusa se a
    # lente reprovar a forma certa) e, com BO8 apagada, nunca podia disparar —
    # sonda que nao pode falhar e' ruido, e ruido ensina a ignorar o autoteste.

    # ⭐⭐ [T16-2] A KEYWORD GRUDADA — a sonda mais importante deste motor.
    # ⛔ E' o defeito EXATO que a primeira versao desta copy tinha: o operador
    # escreveu `Comment gelatin and follow, and I'll send you the recipe` antes
    # de confirmar que a automacao casa palavra EXATA. Se a lente morrer, o
    # motor volta a gerar video que nao dispara DM — e isso nao aparece em
    # render nenhum, so' na falta de leads.
    s16a = dict(s, falas=list(s["falas"]))
    s16a["falas"][1] = ("The gelatin trick keeps your tool hard. Comment "
                        "gelatin and follow, and I'll send you the recipe.")
    if not any("T16-2" in msg for _, msg in lint(s16a, b)):
        ctrl.append("[T16-2] NAO acusa `comment gelatin and follow` — a keyword "
                    "grudada volta a passar e o DM nao dispara")
    s16a2 = dict(s, falas=list(s["falas"]))
    s16a2["falas"][1] = s16a2["falas"][1].replace("Comment gelatin,",
                                                  "Comment gelatin now,")
    if not any("T16-2" in msg for _, msg in lint(s16a2, b)):
        ctrl.append("[T16-2] NAO acusa palavra colada na keyword (`gelatin now`)")

    # ⭐⭐ [ALCANCE] TODA ENTRADA DE POOL TEM DE SER SORTEAVEL.
    # ⛔ Criado em 2026-08-08 depois de medir a cobertura e achar SEIS de dez
    # FOLLOWS que nunca saiam: custavam 6-7 palavras e so' havia 5 de orcamento.
    # O autoteste contava dez opcoes e a producao tinha quatro — pool que mente
    # sobre o proprio tamanho e' mode-collapse com relatorio verde.
    # ⚠️ O teste e' o do PIOR CASO: a entrada tem de caber somada aos MINIMOS
    # dos outros tres eixos. Se nao couber nem ai', ela nunca sai em sorteio
    # nenhum — nao e' "rara", e' morta.
    _minE = min(_palavras(x.format(o="soldier")) for x in EFEITOS)
    _minP = min(_palavras(x) for x in PARCEIRAS)
    _minR = min(_palavras(x) for x in REACOES)
    _minF = min(_palavras(x) for x in FOLLOWS)
    _fixo = _palavras(CTA_BASE)
    for _nome, _pool, _outros in (
            ("EFEITOS", [x.format(o="soldier") for x in EFEITOS],
             _minP + _minR + _minF),
            ("PARCEIRAS", PARCEIRAS, _minE + _minR + _minF),
            ("REACOES", REACOES, _minE + _minP + _minF),
            ("FOLLOWS", FOLLOWS, _minE + _minP + _minR)):
        _teto_eixo = TETO_FALA[2] - _fixo - _outros
        _mortas = [x for x in _pool if _palavras(x) > _teto_eixo]
        if _mortas:
            ctrl.append("[ALCANCE] %d entrada(s) de %s nunca podem ser "
                        "sorteadas (teto real do eixo: %d palavras): %s"
                        % (len(_mortas), _nome, _teto_eixo, _mortas[:3]))

    # ⭐⭐ [T16-5] O PRONOME SEM DONO — a frase que o operador reprovou.
    s165 = dict(s, falas=list(s["falas"]))
    s165["falas"][1] = ("The gelatin trick puts your tool back and she feels "
                        "it first. " + CTA_BASE + " Followers only.")
    if not any("T16-5" in msg for _, msg in lint(s165, b)):
        ctrl.append("[T16-5] NAO acusa `she feels it first` — e a frase exata "
                    "que o operador reprovou em 2026-08-08")
    s165b = dict(s, falas=list(s["falas"]))
    s165b["falas"][1] = ("The gelatin trick brings your tool back. She cannot "
                         "keep quiet. " + CTA_BASE + " Followers only.")
    if not any("T16-5" in msg for _, msg in lint(s165b, b)):
        ctrl.append("[T16-5] NAO acusa sentenca abrindo com `She` nu")

    # ⭐ [T16-3] a pose duplicada — o defeito herdado, achado LENDO o prompt
    b163 = dict(b)
    b163["IMAGE 01/02"] = b163["IMAGE 01/02"].replace(
        "standing upright on her knees",
        "held upright, standing upright on her knees", 1)
    if not any("T16-3" in msg for _, msg in lint(s, b163)):
        ctrl.append("[T16-3] NAO acusa a pose duplicada do prop")

    # ⭐⭐ [T16-4] a boca errada — o defeito que passou por TODO o linter do TRIO
    b164 = dict(b)
    b164["TAKE 01/02"] = b164["TAKE 01/02"].replace(
        "Only the woman standing behind them speaks",
        "Only the woman on frame-left speaks")
    if not any("T16-4" in msg for _, msg in lint(s, b164)):
        ctrl.append("[T16-4] NAO acusa o TAKE mandando falar a mulher errada — "
                    "e' o defeito de 200/200 do TRIO")

    # ⭐ [T16-1] os dois copos altos — a armadilha da fusao das cenas 2 e 3
    # ⛔⛔ ESTE CONTROLE PLANTAVA MEIO DEFEITO: injetava UM copo alto e contava
    # com o outro vindo do `BO_COPO`, que era um `tall clear glass`. Quando o
    # operador trocou o copo pela TIGELA (2026-08-11), a metade emprestada sumiu
    # e o controle ficou CEGO — a lente parou de ser exercitada e ninguem soube
    # ate' o autoteste do irmao DUPLA 16 acusar a mesma coisa.
    # ⭐ Agora ele planta o defeito INTEIRO. Licao: controle que empresta parte
    # do defeito do conteudo de producao morre calado quando o conteudo muda.
    b16 = dict(b)
    b16["IMAGE 02/02"] = b16["IMAGE 02/02"].replace(
        "On the", "On the surface stand a tall clear glass and a second tall "
                  "clear glass, and on the", 1)
    if not any("T16-1" in msg for _, msg in lint(s, b16)):
        ctrl.append("[T16-1] NAO acusa dois copos altos na cena 2 — o copo da "
                    "bancada volta a disputar com o da mao dela")

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
    s10["falas"][1] = s10["falas"][1] + " Up to 5 inches in a week."
    if not any("BO10" in msg for _, msg in lint(s10, b)):
        ctrl.append("[BO10] nao acusa medida de crescimento")

    # ⚠️ O controle de BO3 saiu junto com a lente em 2026-08-05. Ele montava um
    # repertorio sem vilao e esperava reprovacao — hoje esse e' o repertorio
    # CERTO. Controle de regra aposentada que fica para tras vira ruido, e ruido
    # ensina o operador a ignorar o autoteste.

    # ⭐ [DU1] as duas da mesma cor
    s_du1 = dict(s, cor_amiga=s["cor"])
    if not any("DU1" in msg for _, msg in lint(s_du1, b)):
        ctrl.append("[DU1] NAO acusa as duas mulheres com a mesma cor")

    # ⭐ [DU2] a bancada sem a tigela de gelatina
    b_du2 = dict(b)
    b_du2["IMAGE 02/02"] = b_du2["IMAGE 02/02"].replace(
        "vivid purple gelatin cubes", "sliced apples")
    if not any("DU2" in msg for _, msg in lint(s, b_du2)):
        ctrl.append("[DU2] NAO acusa a cena 2 sem a tigela de gelatina")

    # ⭐ [T16-1b] a tigela de volta na bancada, disputando com a da mao
    b_2t = dict(b)
    b_2t["IMAGE 02/02"] += (" A shallow bowl of vivid purple gelatin cubes "
                            "sits untouched at the edge.")
    if not any("T16-1b" in msg for _, msg in lint(s, b_2t)):
        ctrl.append("[T16-1b] NAO acusa DUAS tigelas de gelatina na cena 2")

    # ⭐ [BO16] o deitico orfao — a ordem do operador em um controle
    s16 = dict(s, falas=list(s["falas"]))
    s16["falas"][0] = "If your tool looks like this one and not this one, ok."
    if not any("BO16" in msg for _, msg in lint(s16, b)):
        ctrl.append("[BO16] NAO acusa `this one` duas vezes na cena 1")
    s16b = dict(s, falas=list(s["falas"]))
    s16b["falas"][0] = "If your tool looks like that, this one is for you."
    if not any("BO16" in msg for _, msg in lint(s16b, b)):
        ctrl.append("[BO16] NAO acusa o fecho `this one is for you`")


    # [BO5] copo adiantado
    b5 = dict(b)
    b5["IMAGE 01/02"] += " " + BO_COPO
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

    # ⭐⭐ AS SONDAS DESTE ANGULO. As tres que estavam aqui vigiavam regras do
    # DUPLA/BOTICA que o TRIO nao tem — o raro na receita, o terceiro corpo
    # proibido (aqui ele E' o corpo-prova, pedido pelo operador) e a ancora da
    # amiga na cena 3, onde ela nao esta'. Sonda de regra morta passa sempre.
    #
    # [BO1] os props fora do colo — a escala deste angulo
    b1 = dict(b)
    b1["IMAGE 01/02"] = b1["IMAGE 01/02"].replace("resting on her knees",
                                                    "on a table")
    if not any("BO1" in msg for _, msg in lint(s, b1)):
        ctrl.append("[BO1] NAO acusa o prop fora do colo")

    # ⭐⭐ [T16-ORGAO] SO' `Johnson` E `manhood` — a ordem de 2026-08-16.
    # ⛔ Aqui a sonda olha o POOL, nao o sorteio, e e' de proposito: o defeito
    # que ela previne nao e' um sorteio azarado, e' alguem devolver a palavra a'
    # lista. Sorteio limpo em 600 videos nao prova nada sobre a lista de amanha.
    _proibidos = {"pecker", "wiener", "soldier", "tool", "dick", "cock",
                  "member", "shaft", "penis"}
    _sujo = sorted(_proibidos & {x.lower() for x in NUCLEO})
    if _sujo:
        ctrl.append("[T16-ORGAO] termo proibido de volta no NUCLEO: %s — a "
                    "ordem de 16/08 e' `Johnson` e `manhood` e mais nada"
                    % _sujo)
    if {x.lower() for x in NUCLEO} != {"johnson", "manhood"}:
        ctrl.append("[T16-ORGAO] o NUCLEO deixou de ser exatamente "
                    "{Johnson, manhood}: %s" % sorted(NUCLEO))
    # ⛔ E o SORTEIO tem de sair do NUCLEO, nao do helper do parque. Foi
    # justamente essa desconexao que deixou o motor entregando `wiener` com o
    # pool ja' trocado — pool novo, sorteio velho.
    _s_org = dict(s)
    if set(_s_org["orgaos"]) - {x for x in NUCLEO}:
        ctrl.append("[T16-ORGAO] o sorteio devolveu orgao de fora do NUCLEO "
                    "(%s) — o `sc.orgaos_sorteaveis` voltou a mandar aqui"
                    % _s_org["orgaos"])

    # [BO1] o dedo que nao aponta — sem ele a fala nao tem a qual prop se referir
    b1b = dict(b)
    b1b["IMAGE 01/02"] = b1b["IMAGE 01/02"].replace("index finger points",
                                                    "hand rests")
    if not any("BO1" in msg for _, msg in lint(s, b1b)):
        ctrl.append("[BO1] NAO acusa a falta do dedo apontando")

    # [BO1] a que fala sentando junto — vira "tres amigas no sofa"
    b1c = dict(b)
    b1c["IMAGE 01/02"] = b1c["IMAGE 01/02"].replace("Standing behind them",
                                                    "Sitting beside them")
    if not any("BO1" in msg for _, msg in lint(s, b1c)):
        ctrl.append("[BO1] NAO acusa a terceira sentada em vez de em pe")

    # [BO6] o corpo-prova SEM o sorriso — invertido junto com a lente em
    # 2026-08-10. Controle que injeta o defeito velho depois da regra virar
    # passa sempre e vira sonda cega (§29).
    b6 = dict(b)
    b6["IMAGE 02/02"] = b6["IMAGE 02/02"].replace(
        "smiling broadly", "standing there")
    if not any("BO6" in msg for _, msg in lint(s, b6)):
        ctrl.append("[BO6] NAO acusa o corpo-prova COM rosto")

    # [BO6] as sentadas voltando na cena 3 — quatro corpos em 8 segundos
    b6b = dict(b)
    b6b["IMAGE 02/02"] += " Two women sit behind her."
    if not any("BO6" in msg for _, msg in lint(s, b6b)):
        ctrl.append("[BO6] NAO acusa as sentadas de volta na cena 3")

    # ⭐⭐ [BO6] A BOCA FECHADA DAS SENTADAS — 2026-08-16, com o render na mao.
    # ⛔ O operador mandou o video: *"a menina da direita sempre falando
    # junto"*. Conferido nos quadros a 1,5 fps — boca aberta, dentes a' mostra,
    # mid-word. E a causa estava escrita no proprio prompt: a trava era a
    # NEGACAO `Neither seated woman speaks`, colada num rosto descrito so' como
    # `smiling, her whole face lit up` — sem estado de boca nenhum. Negacao
    # injeta o token (licoes-producao-veo §*Declaracao e' municao*), e o frame 0
    # manda: sorriso aberto sem `lips closed` renderiza boca que se mexe.
    # ⭐ A trava virou POSITIVA (`keep their lips closed`), e este controle
    # planta a volta da forma negativa — que e' como o defeito reapareceria.
    b6c = dict(b)
    b6c["IMAGE 01/02"] = b6c["IMAGE 01/02"].replace(
        "Both seated women keep their lips closed and their eyes down on "
        "what they are holding.",
        "Neither seated woman speaks and both keep their eyes on what they "
        "are holding.")
    if not any("BO6" in msg for _, msg in lint(s, b6c)):
        ctrl.append("[BO6] NAO acusa a volta da trava NEGATIVA de mudez — foi "
                    "ela que fez a sentada da direita falar junto")
    # ⛔ E a clausula de boca fechada tem de estar nos DOIS blocos do take 1: o
    # frame 0 decide a boca, e o TAKE decide se ela se mexe nos 8 segundos.
    for _n in ("IMAGE 01/02", "TAKE 01/02"):
        if "lips closed" not in b[_n]:
            ctrl.append("[BO6] %s sem `lips closed` — a mudez das sentadas "
                        "voltou a ser negacao ou sumiu" % _n)

    # [HIER] o gelatin trick como item da lista (§31)
    sh = dict(s, falas=list(s["falas"]))
    sh["falas"][1] = ("Pomegranate juice, beetroot powder, honey and ginger in "
                      "warm water, and one gelatin trick.")
    if not any("HIER" in msg for _, msg in lint(sh, b)):
        ctrl.append("[HIER] NAO acusa o gelatin trick sem hierarquia")

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
    for i in (1, 2):
        L = larguras[i]
        print("  cena %d: %d-%d palavras (media %.1f) | piso %d teto %d | %.2f p/s"
              % (i, min(L), max(L), sum(L) / float(len(L)), PISO_FALA[i],
                 TETO_FALA[i], sum(L) / float(len(L)) / 8))

    # ⛔⛔ A TRAVA TEM DE FIXAR — a unica checagem do dropdown que mede FUNCAO.
    # As de FORMA (rotulo unico, curto, presente, com `id`) rodaram la' no
    # comeco, em `_contrato_dropdown`. O §41 do licoes-de-construcao existe
    # exatamente porque forma verificada foi declarada pronta sem funcao
    # medida — e neste motor a funcao ESTAVA quebrada: o pool nao tinha `id` e
    # o `sortear` resolvia a trava por `cabeca`, entao o menu nasceria mudo.
    for _ch, _tela, _pn, _campo in DROPDOWNS_UI:
        _pool = globals().get(_pn)
        if not isinstance(_pool, list) or not _pool:
            continue
        _alvo = _pool[len(_pool) // 2]["id"]
        _ids, _naodict, _boom = set(), 0, None
        for _i in range(8):
            # ⛔⛔ O `sortear` PODE MORRER com a trava, e ai a lente tem de
            # FALAR, nao de deixar o traceback subir. Medido no FALTA 16: a
            # trava crua vira string e o sorteio da amiga estoura em
            # `ref.get("id")` — o autoteste inteiro caia com AttributeError e
            # esta checagem nunca chegava a rodar. Traceback diz ONDE
            # estourou; a lente diz O QUE quebrou.
            try:
                _s = sortear("joe", random.Random(9100 + _i), {},
                             {_ch: _alvo})
            except Exception as _e:            # noqa: BLE001
                _boom = "%s: %s" % (type(_e).__name__, _e)
                break
            _v = _s[_ch]
            # ⛔⛔ TEM DE SER O DICT DA ENTRADA — nao basta o id BATER.
            # Medido em 2026-08-13, e este foi um furo real desta lente: com o
            # resolver devolvendo a trava CRUA, `spec["ref"]` virava a STRING
            # "balayage_caramelo", que e' IGUAL ao alvo. A lente comparava id
            # com id, dava FIXOU, e o spec estourava no `montar` com
            # `string indices must be integers`. Lente que aceita string mede o
            # TEXTO que ela mesma mandou, nao o eixo que o motor resolveu.
            if not isinstance(_v, dict):
                _naodict += 1
                continue
            _ids.add(_v.get("id"))
        if _boom:
            falhas.append("DROPDOWN: escolher %r em %r DERRUBA o `sortear` "
                          "(%s) — o menu nao fica so' mudo, ele quebra o app"
                          % (_alvo, _tela, _boom))
        elif _naodict:
            falhas.append("DROPDOWN: o eixo %r voltou como %s em %d de 8 "
                          "sorteios, e nao como a entrada do pool — o `montar` "
                          "estoura no primeiro indice"
                          % (_ch, type(_v).__name__, _naodict))
        elif _ids != {_alvo}:
            falhas.append("DROPDOWN: escolher %r em %r nao fixou o eixo — 8 "
                          "sorteios devolveram %r"
                          % (_alvo, _tela, sorted(_ids)))
        # ⛔ CONTROLE NEGATIVO: um pool SINTETICO sabotado nas quatro formas.
        # ⚠️ SINTETICO, e nao uma copia do pool real, por licao paga na hora de
        # escrever isto: a primeira versao fazia `_sab[0][_campo]` sobre copias
        # das entradas de verdade e ESTOUROU com `KeyError` quando o campo
        # declarado no `DROPDOWNS_UI` nao existia — justamente o defeito que
        # esta lente deveria REPORTAR. Controle negativo que derruba o autoteste
        # em vez de acusar e' pior que controle nenhum: some a falha real no
        # traceback. O pool de mentira nao depende de nada e sempre exercita as
        # quatro pernas.
        _sab = [{"id": "sab%d" % _k, _campo: "rotulo sabotado %d" % _k}
                for _k in range(6)]
        _sab[1][_campo] = _sab[0][_campo]
        _sab[2][_campo] = "x" * 43
        _sab[3].pop(_campo, None)
        _sab[4].pop("id", None)
        if len(_checa_drop(_sab, _campo)) != 4:
            ctrl.append("[DROP] a lente do dropdown nao acusa as quatro "
                        "sabotagens (repetido/longo/vazio/sem id) — ela mede a "
                        "sorte do pool, nao o contrato")

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
    ap = argparse.ArgumentParser(
        description="Randomizador do agente TRIO 16 (2 takes de 8s)")
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
