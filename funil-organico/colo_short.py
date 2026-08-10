#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
colo_short.py — randomizador + gerador + linter do AGENTE **COLO** (SHORT).

⭐ FONTE: SOFIA MAREN, reel facebook.com/reel/1580259273673843 (40s, 3,2K views,
30 reacoes, 14 comentarios). Transcrito com Whisper e conferido frame a frame em
2026-08-03. A copy falada da fonte, INTEIRA, esta' em
`concorrentes/sofia-maren-colo-mapa-visual.md` — este motor nao inventa copy, ele
TRADUZ a de la' para o nosso mecanismo (gelatin trick / Comment gelatin).

⭐ O QUE E' O ANGULO, em uma frase: ela manda despejar uma substancia absurda
sobre um prop falico apoiado no PROPRIO COLO, desmente a promessa na mesma
respiracao e entrega a receita de verdade. O bit visual e' a geometria do colo —
por isso o agente se chama COLO e nao "isca" (que ja' e' o nome do slot do CTA).

O ARCO — 3 cenas de 8s, destino AdBatch Vertical 3:

    cena 1  SENTADA   a isca no colo + o desmentido      (o hook)
    cena 2  DE PE'    a receita na bancada               (o mecanismo)
    cena 3  DE PE'    o copo pronto + a gelatina na mao  (o CTA)

⚠️ A TROCA DE AMBIENTE ENTRE A CENA 1 E A 2 E' ORDEM DO OPERADOR (2026-08-03),
e e' o corte que a fonte faz: ela abre sentada na poltrona do escritorio com o
prop no colo e corta para de pe' na bancada da cozinha. O custo esta' declarado
e aceito: sao DOIS sets por video, e blocos de 8s gerados separadamente com
cenario diferente sao a situacao em que o Veo mais troca de pessoa. A defesa e'
a ancora de continuidade (CO7), que aqui e' obrigatoria nas cenas 2 e 3.

⚠️ ETNIA ARRASTA O MUNDO INTEIRO (ordem do operador, 2026-08-03, com todas as
letras: *"variar etnia e' variar ate' o nivel de nicho visual, e nao so' mudar o
rosto do REF"*). Nao ha' eixo `etnia` solto neste motor: ela sai de dentro do
MUNDO, junto com a sala, a bancada, o traje, a luz e a ambiencia. Mesma forma do
`ARQUETIPOS` do NECROSE (NE5) e do `MUNDOS` do CLEAN v2.

Uso:
    python funil-organico/colo_short.py --pagina joe --n 1
    python funil-organico/colo_short.py --pagina ray --n 3 --seed 42 --dry-run
    python funil-organico/colo_short.py --autoteste
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
LEDGER = os.path.join(AQUI, ".colo-short-ledger.json")

TITULO = "AGENTE COLO SHORT"
SLUG = "colo-short"
SUBTITULO = ("a isca no colo, em 3 cenas · etnia arrasta o mundo · "
             "gerador offline de prompts Veo")

# O dict que a `ui_agente.paginas_por_pele` le' para agrupar as paginas no
# seletor `pele clara/escura`. ⚠️ Ele NAO governa a etnia do video neste motor
# (ver MUNDOS) — mas sem ele o painel quebra, e a classificacao e' por
# SUBSTRING (`"white" in ...`), entao o formato tem de ser string.
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
    # lote 1 (2026-07)
    "joe": "white American", "ray": "white American", "matt": "white American",
    "marcus": "Black American", "chuck": "Black American",
    # ⭐ lote 2 (2026-08-03) — as cinco paginas novas do Facebook. A chave e
    # a etnia saem do AVATAR REAL da pagina, nao de preferencia: a
    # congruencia inviolavel do repo e etnia do REF = etnia do avatar.
    #   Hank Male Tips Hub ....... clara   -> secondwindformen.site
    #   Wade All Natural Hub ..... clara   -> strengthandflow.site
    #   Isaiah Vitality Men Tips . escura  -> dailyvitalitymethod.site
    #   Curtis Reset Hub ......... escura  -> menresethub.site
    #   Otis Men Reset Hub ....... escura  -> mensresetclub.online
    # Pareamento pagina<->bridge: funil-organico/automacao-comentario-dm.md
    "hank": "white American", "wade": "white American",
    "isaiah": "Black American", "curtis": "Black American",
    "otis": "Black American",
}


# ---------------------------------------------------------------------------
# STRINGS TRAVADAS — copia da leitura otica da fonte. NAO REESCREVER.
# ---------------------------------------------------------------------------

# ⭐⭐ CO1 — A GEOMETRIA DO COLO. E' o agente inteiro em uma frase, e e' o unico
# bloco que nao pode ser afrouxado: sem o prop APOIADO NO PROPRIO COLO dela o
# video vira mais uma narradora despejando coisa numa bancada, que e' o que
# quatro outros agentes nossos ja' fazem.
# ⚠️ Lida frame a frame na fonte (t=00:00 e t=00:09): ela esta' SENTADA de frente
# para a camera, joelhos abertos, o prop EM PE' apoiado na frente do assento
# entre os joelhos, a mao esquerda segurando a base, a direita despejando de uma
# garrafa de vidro inclinada, e o jorro cai em fio sobre o topo do prop.
# ⛔ A base na mao NAO e' enfeite: e' a mesma correcao que o RESSURREICAO pagou
# em render — prop em pe' sem nada segurando entra na mesa, e o Veo resolve a
# fisica inventando.
#
# ⚠️⚠️ 2026-08-03 — REESCRITA DEPOIS DE O OPERADOR MANDAR O CROP AMPLIADO E
# PEDIR CONFORMIDADE POSICIONAL DE TODOS OS ELEMENTOS. A primeira versao dizia
# que o prop ficava "em pe' na beirada do assento entre os joelhos". ERRADO: na
# fonte ele esta' EM PE' DENTRO DO PUNHO ESQUERDO FECHADO, acima do colo, com o
# antebraco apoiado na coxa. Assento e punho sao dois quadros diferentes.
#
# ⛔ O QUE ESTA' TRAVADO AQUI, elemento por elemento — cada um com POSICAO NO
# QUADRO, ALTURA NO CORPO e RELACAO com os outros. Descricao sem posicao e'
# convite ao gerador arranjar por conta, e foi assim que o EXTERIOR pagou o
# `the box` generico e o RESSURREICAO pagou o prop entrando na mesa:
#   1. CAMERA .... frontal, altura do peito dela, enquadrando do meio da coxa
#                  para cima. ⛔ Nunca de cima: plongee fecha o V das pernas.
#   2. PERNAS .... joelhos abertos, coxas em V ocupando o terco inferior
#   3. PROP ...... vertical dentro do punho ESQUERDO, acima do colo, centrado
#                  entre os joelhos, ponta para cima, antebraco na coxa
#   4. FRASCO .... mao DIREITA, altura da cintura, um palmo acima do topo do
#                  prop e ligeiramente a frame-left dele, bocal para baixo ~45°
#   5. JORRO ..... linha unica e continua do bocal ate' o topo do prop,
#                  atravessando o vao — e' o vao que faz o jorro existir
#   6. ROSTO ..... acima e atras da mao levantada, ombros quadrados na lente
# ⚠️ As MAOS estao conferidas na fonte, nao supostas: ela esta' de frente, entao
# a mao que aparece a' esquerda do espectador e' a DIREITA dela (a do frasco), e
# a que aparece a' direita e' a ESQUERDA (a do prop).
# ⛔⛔ A PRIMEIRA VERSAO DESTA TRAVADA FOI JOGADA FORA EM 2026-08-03, E
# A LICAO E' MINHA. O operador pos o render do agente ao lado do print da fonte:
# *"Cade a perna do homem? Quem segura o prop e' o segundo personagem, com a
# cintura pra cima cortado no frame do video. Esta' bem errado essa
# assertividade sua."*
#
# Ele esta' certo. Eu li o frame e COLAPSEI DOIS PERSONAGENS EM UM: as pernas de
# calca caqui que ocupam a metade de baixo do quadro NAO sao dela — sao de um
# HOMEM sentado de frente para a camera, cortado na cintura, sem rosto e sem
# tronco. E' a MAO DELE que segura o prop em pe' no proprio colo. Ela entra por
# tras, do peito para cima, e despeja. O motor gerava a narradora com o prop
# entre as PROPRIAS pernas — outro video, e sem o personagem que da' ao hook o
# dono do problema.
#
# ⚠️ O QUE FICA: eu declarei conformidade posicional elemento por elemento sobre
# uma leitura que nunca conferi com a pergunta certa — *de quem e' esta perna?*.
# Descricao detalhada de um quadro errado e' pior que descricao vaga: ela TRAVA
# o erro. Regra: **antes de travar geometria com duas partes de corpo, contar
# quantas PESSOAS ha' no quadro.**
#
# ⛔ OS ELEMENTOS, com posicao, altura e DONO:
#   1. CAMERA .... frontal, na altura do colo de quem esta' sentado
#   2. HOMEM ..... metade de baixo do quadro, perto da camera, joelhos abertos,
#                  CORTADO NA CINTURA — zero rosto, zero tronco
#   3. PROP ...... vertical no punho ESQUERDO DELE, apoiado na coxa dele
#   4. MULHER .... atras do colo dele, cabeca e ombros ACIMA dos joelhos dele
#   5. FRASCO .... mao DIREITA DELA, sobre o colo dele, um palmo acima do topo
#                  do prop e ligeiramente a frame-left, bocal para baixo ~45°
#   6. JORRO ..... linha unica atravessando o vao ate' o topo do prop
#
# ⭐⭐⭐ ESTA E' A "H5" — VALIDADA EM CAMPO, PROMPT A PROMPT, EM 2026-08-03.
# ⛔ NAO REESCREVER, NAO COMPRIMIR, NAO "MELHORAR". Cada palavra aqui custou uma
# geracao, e a versao anterior desta travada era barrada pelo gerador em 2 de
# cada 3 lotes.
#
# COMO ELA NASCEU — o operador parou a alteracao do agente e mandou testar
# manualmente, uma hipotese por vez: *"em vez de ficar alterando o agente toda
# hora, vamos primeiro fazer o teste prompt a prompt; validamos o prompt, dai
# partimos para ajustar o agente"*. Foram cinco hipoteses ate' esta passar:
#   H1  trocou lap/thigh/knees apart/cropped at the waist por vocabulario de
#       MOVEL e ENQUADRAMENTO ................................ passou, prop longe
#   H2  + antebraco apoiado na perna + base na beirada do assento .... REGRESSAO
#       (tres mudancas numa frase so'; o `forearm resting` criou uma segunda
#       instrucao para a MESMA mao e o gerador abriu a mao no joelho)
#   H3  = H1 com `held in close to him` ............... melhor, prop ainda alto
#   H4  + `below the level of the chair back` ....................... REGRESSAO
#       (a cadeira virou ASSUNTO e a cena se reorganizou em volta dela)
#   H5  = H3 com a CAMERA baixa e a consequencia declarada ......... ✅ VALIDADA
#
# ⛔ AS DUAS LICOES QUE AS REGRESSOES PAGARAM, e elas valem para qualquer travada
# deste repo:
#   · nunca dar ao gerador uma SEGUNDA instrucao para a mesma parte do corpo —
#     ele resolve a contradicao mexendo no que estava certo;
#   · nunca ancorar altura num MOVEL que esta' em quadro — o movel vira assunto.
# A ancora certa e' a CAMERA, e a consequencia se declara (`so that his legs
# fill the bottom half of the frame`).
#
# ⛔ TOKENS BANIDOS NESTA CENA, medidos: `lap` · `thigh` · `knees apart` ·
# `between his knees` · `cropped at the waist`. Nenhum deles descreve nada que a
# imagem precise — o mesmo quadro sai com cadeira, joelho e enquadramento.
CO_GEOMETRIA = (
    "Filmed straight on from low down and close in, at the height of the "
    "seated man's knees, so that his legs fill the bottom half of the frame. "
    "The foreground of the shot, close to the camera, is a man sitting in a "
    "chair, turned squarely to the camera, wearing %s; the framing takes in "
    "only his legs and his hands, with his head and upper body out of shot. %s "
    "Standing upright in his closed left hand, held in close to him with his "
    "fist just clear of his body and the tip reaching no higher than his knees, "
    "is %s; his fist is closed around %s and the tip points straight up for the "
    "whole shot. Directly behind him, seated and facing the lens squarely with "
    "her head and shoulders above him, is %s. She holds %s out over it in her "
    "right hand, tipped mouth-down at about forty-five degrees and a hand's "
    "width above the top, and %s falls in one unbroken line onto the very top "
    "of it. The setting behind her stays visible over both her shoulders."
)

# ⛔ CO2 — no TAKE da cena 1 o prop NAO muda de estado. Este agente nao tem
# crescimento: quem cresce e' o RESSURREICAO, e la' o morph e' o bit visual. Aqui
# o bit visual e' o DESPEJO. Duas mecanicas de choque no mesmo video somam a uma.
# ⚠️ ⛔ Nunca `completely motionless` num objeto que uma mao segura: e' ordem
# impossivel e o Veo resolve SOLTANDO o objeto (F12b). Diz-se pela POSICAO.
# ⛔ `thigh` saiu daqui tambem: e' token banido nesta cena (ver CO_GEOMETRIA), e
# o TAKE nao pode reintroduzir o que o IMAGE evitou — o bloco de video passa
# pelo mesmo classificador.
CO_PROP_ESTAVEL = (
    "His left fist stays closed around it and he keeps it in exactly the same "
    "place, at the same height and the same angle, same size, same shape, same "
    "colour. He does not shift, his knees stay where they are and his face "
    "never comes into the frame. Her right hand keeps the bottle at the same "
    "height and the same tilt. Only the falling stream moves, and only she "
    "speaks."
)

# ⛔ CO3 — a bancada das cenas 2 e 3 e' a MESMA, e a unica coisa que muda entre
# elas e' o copo. Copia da gramatica ja' validada em render no CLEAN (familia B).
CO_MESMA_BANCADA = ("Nothing has been added to the %s and nothing removed from "
                    "it — only the tall glass has changed.")

# ⛔ CO4 — a pegada anti-F12b da cena 2: punho inteiro em volta do recipiente e
# antebraco apoiado. Esqueleto copiado do CLEAN, validado em render 2026-08-02.
CO_PEGADA = ("Her right hand is closed around the %s, the whole hand visibly "
             "wrapped around it, her forearm resting steady on the %s as she %s")

# ⛔ CO5 — a gelatina pronta so' existe na CENA 3, e e' ela o objeto da keyword.
# ⭐ Ela esta' NA MAO dela no frame em que a boca diz `gelatin,` — a fonte faz
# exatamente isso com o livro (t=00:35), que e' a keyword dela (`book`). O objeto
# da keyword na mao e' o que faz a palavra grudar.
CO_GELATINA = ("a clear glass bowl of firm vivid purple gelatin cubes, glossy "
               "and set")
# ⚠️ POSICAO LIDA NA FONTE (t=00:35): o objeto da keyword sobe na mao ESQUERDA,
# a frame-right, na altura da bochecha, e o indicador DIREITO cruza o corpo e
# aponta para ele. O copo pronto fica embaixo, a frame-left. ⛔ Objeto da
# keyword atras do corpo ou abaixo do peito nao e' visto no scroll.
CO_KEYWORD_NA_MAO = (
    "Her left hand is raised at frame-right, level with her cheek and just "
    "clear of her face, holding %s, turned so the cubes face the lens; her "
    "right index finger reaches across and points at it from just below."
)

# ⛔ A BANCADA DA CENA 2 — posicao de cada objeto, da esquerda para a direita.
# ⚠️ Sem as posicoes o Veo empilha tudo no centro e a fileira some. A gramatica
# de fileira posicionada vem do CLEAN, validada em render.
CO_BANCADA_LAYOUT = (
    "On the %s in front of her, standing along the bottom third of the frame: "
    "at frame-left a small bowl of ground spice on a folded cloth, in the "
    "centre directly in front of her a tall clear glass of water, and at "
    "frame-right a wooden board with a metal spoon lying on it"
)

# ⛔ CO6 — ela nunca toca no resto da bancada. Sem isto o Veo comeca a mexer em
# tudo o que esta' em quadro e a continuidade entre os blocos de 8s morre.
CO_NAO_TOCA = ("She never touches, opens, lifts or pours anything else on the "
               "%s.")

# ⛔⛔ CO7 — A ANCORA DE CONTINUIDADE, e neste agente ela e' CRITICA.
# Os outros SHORT rodam as 3 cenas no mesmo cenario; aqui a cena 1 e' na sala,
# sentada, e as cenas 2 e 3 sao na bancada, de pe'. Cenario diferente entre
# blocos gerados separadamente e' exatamente onde o Veo troca de pessoa — e o
# TAKE diz "She is the only person", entao a estranha fala a fala dela.
# ⚠️ A ancora e' de ROSTO E IDADE, nunca so' de roupa: no VAZAMENTO a ancora
# estava na camisa e o render devolveu outra pessoa (registrado no short_comum).
# ⚠️ Comeca em MINUSCULA de proposito: ela entra no meio da frase na cena 2
# (`...is the same 29-year-old...`) e no comeco da frase na cena 3, onde o
# `_cap` a levanta. A primeira versao saia `is The same 29-year-old` — maiuscula
# no meio da frase, achado lendo o render.
CO_ANCORA = "the same %d-year-old %s woman from the first scene, same %s %s, same %s, same %s"

ANTICELEB = ("Ordinary relatable face, not a celebrity, not a model, not an "
             "actor, not resembling any famous person.")
CAUDA = "Shot on iPhone, natural grain. No on-screen text, no watermark."


# ---------------------------------------------------------------------------
# ⭐⭐ MUNDOS — O NICHO VISUAL INTEIRO NUM EIXO SO'
# ---------------------------------------------------------------------------
# ⛔ NAO EXISTE EIXO `etnia` NESTE MOTOR. Ordem do operador, 2026-08-03: *"variar
# etnias tal como o NECROSE quer dizer variar ate' o nivel de NICHO VISUAL —
# nativo da montanha, nativo do pantano, tribo africana — com adaptacao tematica
# visual alinhada a' etnia, e nao so' mudar o rosto do REF por etnia"*.
# Etnia, sala, bancada, traje, luz e ambiencia sao UMA escolha so'.
#
# Cada MUNDO carrega, congruentes entre si:
#     etnias   as etnias que aquele mundo comporta
#     sala     o set da CENA 1 (ela sentada) — onde mora a autoridade dela
#     sala_c   o mesmo, curto
#     banc     o set das CENAS 2 e 3 (ela de pe')
#     sup_a    a superficie da bancada, com artigo
#     sup      a mesma, curta
#     traje    a roupa (%s = cor) — ⛔ SEM artigo: `_traje()` calcula `a`/`an`
#     curto    a roupa em 2 palavras, para a ancora de continuidade
#     cores    as cores que aquela roupa aceita
#     luz      a luz
#     luz_c    a mesma, curta
#     audio    a ambiencia
#
# ⭐ O SORTEIO E' POR FAMILIA, DEPOIS POR MUNDO DENTRO DELA. Sem esse passo a
# familia com mais sets domina o lote — medido no CLEAN v2 no mesmo dia.
# ⛔ ZERO texto legivel em qualquer set: a CAUDA promete "No on-screen text", e
# parede de diploma com letra em foco e' texto em cena. Por isso os diplomas da
# fonte entram como "framed certificates" sem mencao ao que esta' escrito.
# ⚠️ O selo `V` fica so' no mundo da fonte; os outros sao `N` (extrapolacao
# nossa, sem render — quem valida em campo e' o operador).
# ⭐⭐ TRAVA DE PELE (2026-08-06, ordem do operador: *"ajuste todos os agentes
# python para serem compativeis com o item de selecionar a cor de pele"*).
# ⛔ Este motor tinha o MESMO botao morto que o CLEAN V2 tinha: a etnia sai de
# dentro do MUNDO, nao de `ETNIA[pagina]`, entao o seletor clara/escura do
# painel — que funciona trocando a PAGINA — acendia e o sorteio seguia
# aleatorio. Achado medindo os 18 agentes, nao lendo o codigo.
# ⚠️ Lista EXPLICITA, nunca "tudo que nao e' branco": e' a mesma correcao que o
# CLEAN V2 pagou em campo (travou `escura` e recebeu um Asian American).
PELE_ETNIAS = {
    # ⚠️ Mexican American e Cuban American ficam FORA das duas listas de
    # proposito, exatamente como no TRIO: a trava de pele filtra por elas, e
    # forcar uma classificacao produziria o erro que o CLEAN V2 pagou em
    # campo (travou `escura` e recebeu um Asian American).
    "escura": ("Black American",),
    "clara": ("white American",),
}
PELE_TRAVAVEL = True


def _pele_de(etnia):
    """A pele da etnia pela lista explicita — ou None (neutra, so' no livre)."""
    for _pele, _ets in PELE_ETNIAS.items():
        if etnia in _ets:
            return _pele
    return None


MUNDOS = [
    # ---- brooklyn ----
    {"id": "brooklyn", "selo": "N", "familia": "brooklyn",
     "etnias": ["white American", "Black American"],
     "sala": "the front parlor of a Brooklyn brownstone apartment, a worn "
             "velvet armchair set against the exposed brick wall, a tall "
             "sash window at frame-right with a black fire escape and the "
             "plain brick wall of the building across the street beyond, "
             "small potted plants crowded on the sill where the sun comes "
             "in",
     "sala_c": "the same brownstone parlor",
     "banc": "the narrow galley kitchen of the same brownstone apartment, "
             "a tiled wall and open shelves of glass jars behind her, the "
             "same sash-window light reaching down the hall",
     "sup_a": "a narrow stainless steel counter",
     "sup": "counter",
     "trajes": [
         ["%s cropped ribbed tank top with high-waisted vintage jeans",
          "cropped tank"],
         ["%s bias-cut satin slip dress with thin straps and bare shoulders",
          "slip dress"],
         ["%s cropped baby tee tucked into a denim mini skirt",
          "baby tee"],
         ["%s tube top with hip-slung cargo pants slung at the hips",
          "tube top"],
         ["%s fine-knit mesh long-sleeve crop top with a leather mini skirt",
          "mesh crop"],
     ],
     "cores": ["black", "washed burgundy", "bone white", "olive green"],
     "luz": "Hard afternoon sun cutting in slanted bars through the tall "
            "sash window at frame-right.",
     "luz_c": "hard slanted sunlight",
     "audio": "distant traffic, a subway rumbling",
     },
    # ---- jersey ----
    {"id": "jersey", "selo": "N", "familia": "jersey",
     "etnias": ["white American"],
     "sala": "the carpeted den of a New Jersey split-level house, a big "
             "plaid sectional sofa along the wood-paneled wall, a sliding "
             "glass door at frame-left standing open onto a small deck "
             "with an above-ground pool out of focus beyond, a brass floor "
             "lamp in the corner",
     "sala_c": "the same paneled den",
     "banc": "the kitchen up the short flight of the same split-level, oak "
             "cabinets and a window over the sink looking out at the same "
             "deck",
     "sup_a": "a speckled laminate kitchen island",
     "sup": "island",
     "trajes": [
         ["%s velour tracksuit jacket unzipped over a cropped top with hip-slung track pants",
          "velour tracksuit"],
         ["%s halter-neck bodycon mini dress",
          "bodycon dress"],
         ["%s cropped hoodie cut short above tight high-waisted leggings",
          "cropped hoodie"],
         ["%s strappy scoop-neck bodysuit with high-waisted denim shorts",
          "strappy bodysuit"],
         ["%s fitted off-the-shoulder crop top with hip-slung flare jeans",
          "off-shoulder crop"],
     ],
     "cores": ["hot pink", "white", "black", "gold"],
     "luz": "Warm low light spilling in through the open sliding door, the "
            "paneled corners of the room falling into deep shadow.",
     "luz_c": "warm low door light",
     "audio": "a window fan humming, cicadas",
     },
    # ---- boston ----
    {"id": "boston", "selo": "N", "familia": "boston",
     "etnias": ["white American"],
     "sala": "the second-floor front room of a Boston triple-decker, a "
             "padded bow-window seat built into the tall bay window with "
             "white wainscoting behind it and a cast-iron radiator at one "
             "end, wet slate rooftops and brick chimneys of the block "
             "filling the panes and a flat pale sky washing the room",
     "sala_c": "the same bow-window seat",
     "banc": "the kitchen at the back of the same triple-decker, painted "
             "cabinets and a deep porcelain sink behind her, the wooden "
             "back-porch stairs through the window",
     "sup_a": "a chipped porcelain-topped kitchen table",
     "sup": "table",
     "trajes": [
         ["%s cable-knit crop sweater with a pleated tennis skirt",
          "crop sweater"],
         ["%s ribbed turtleneck cropped at the ribs with a corduroy mini skirt",
          "cropped turtleneck"],
         ["%s cropped sleeveless polo shirt with a plaid wool mini skirt",
          "cropped polo"],
         ["%s cropped rugby-stripe top with high-waisted running shorts",
          "rugby crop"],
         ["%s waffle-knit thermal top cropped above the navel with bike shorts",
          "cropped thermal"],
     ],
     "cores": ["navy", "heather grey", "cream", "deep crimson"],
     "luz": "Flat cool overcast light off the pale sky, almost no shadow.",
     "luz_c": "flat overcast light",
     "audio": "a radiator ticking, quiet street",
     },
    # ---- nova_inglaterra ----
    {"id": "nova_inglaterra", "selo": "N", "familia": "nova_inglaterra",
     "etnias": ["white American"],
     "sala": "the keeping room of an old New England farmhouse, a "
             "black-painted Windsor chair on a hooked rug over wide pine "
             "floorboards, a deep brick hearth with a cast-iron kettle on "
             "its crane and a low fire in it behind the chair, maple "
             "branches in full leaf outside the small-paned window at "
             "frame-left",
     "sala_c": "the same farmhouse keeping room",
     "banc": "the kitchen through the doorway of the same farmhouse, a dry "
             "sink and a shelf of stoneware crocks behind her, the same "
             "small-paned windows along the wall",
     "sup_a": "a worn soapstone counter",
     "sup": "counter",
     "trajes": [
         ["%s gingham crop top with denim cut-offs",
          "gingham crop"],
         ["%s short cotton sundress with thin straps and a full skirt",
          "short sundress"],
         ["%s flannel shirt knotted high above the waist over a fitted camisole with a short chambray skirt",
          "knotted flannel"],
         ["%s cotton eyelet crop top with high-waisted linen shorts",
          "eyelet crop"],
         ["%s fitted crop top under cut-off denim overall shorts",
          "overall shorts"],
     ],
     "cores": ["barn red", "soft indigo", "buttermilk white", "seafoam green"],
     "luz": "Warm firelight off the low hearth mixed with pale daylight "
            "from the small-paned window.",
     "luz_c": "firelight and pale daylight",
     "audio": "a crackling fire, birdsong",
     },
    # ---- louisiana ----
    {"id": "louisiana", "selo": "N", "familia": "louisiana",
     "etnias": ["Black American", "white American"],
     "sala": "the front room of a Louisiana shotgun house, a worn velvet "
             "armchair beside tall shuttered French doors, a slow ceiling "
             "fan turning above her and a live oak draped with Spanish "
             "moss out on the street beyond",
     "sala_c": "the same shotgun house room",
     "banc": "the narrow kitchen at the back of the same shotgun house, "
             "beadboard cabinets and a heavy cast-iron skillet by the "
             "window, the shuttered French doors of the front room visible "
             "down the hall",
     "sup_a": "a scarred cypress-wood counter",
     "sup": "counter",
     "trajes": [
         ["%s cropped eyelet camisole with a short seersucker skirt",
          "eyelet camisole"],
         ["%s off-the-shoulder crop top with a short flared skirt",
          "off-shoulder crop"],
         ["%s bias-cut slip dress with thin straps, cut above the knee",
          "slip dress"],
         ["%s lace-trimmed corset top with high-waisted cotton shorts",
          "corset top"],
         ["%s strapless cotton romper cut short above the knee",
          "short romper"],
     ],
     "cores": ["cream", "deep magenta", "faded blue", "moss green"],
     "luz": "Warm humid afternoon light through the shutters, slatted "
            "shadows falling across the floor.",
     "luz_c": "warm slatted shutter light",
     "audio": "ceiling fan hum, cicadas outside",
     },
    # ---- atlanta ----
    {"id": "atlanta", "selo": "N", "familia": "atlanta",
     "etnias": ["Black American"],
     "sala": "the living room of a modern Atlanta townhouse, a low grey "
             "sectional sofa against an exposed brick wall, a tall "
             "monstera in a woven basket at frame-left and "
             "floor-to-ceiling windows showing green treetops over the "
             "city",
     "sala_c": "the same townhouse living room",
     "banc": "the open kitchen of the same townhouse, matte black cabinets "
             "and a subway-tile backsplash behind her, the grey sectional "
             "and the brick wall out of focus beyond",
     "sup_a": "a white quartz kitchen island",
     "sup": "island",
     "trajes": [
         ["%s cropped ribbed workout tank with high-waisted leggings",
          "workout tank"],
         ["%s cropped hoodie ending above the waist with matching bike shorts",
          "cropped hoodie"],
         ["%s satin camisole with a low back and a short pencil skirt",
          "satin camisole"],
         ["%s sheer long-sleeve mesh crop top over a fitted sports top with cropped joggers",
          "mesh crop"],
         ["%s one-shoulder knit crop top with a short faux-leather skirt",
          "one-shoulder knit"],
     ],
     "cores": ["black", "warm caramel", "ivory", "deep plum"],
     "luz": "Cool bright daylight from the tall windows, crisp and even.",
     "luz_c": "cool tall-window daylight",
     "audio": "faint city traffic hum",
     },
    # ---- nashville ----
    {"id": "nashville", "selo": "N", "familia": "nashville",
     "etnias": ["white American"],
     "sala": "the front room of a Nashville craftsman bungalow, a worn tan "
             "leather bench under a wide window with wooden blinds, a "
             "stone hearth with a rough cedar mantel behind her and an "
             "acoustic guitar on a stand in the corner",
     "sala_c": "the same bungalow front room",
     "banc": "the kitchen of the same bungalow, painted shaker cabinets "
             "and open pine shelves behind her, the stone hearth and cedar "
             "mantel showing through the doorway",
     "sup_a": "a worn oak farmhouse table",
     "sup": "table",
     "trajes": [
         ["%s gingham crop top knotted high at the ribs with denim cut-off shorts",
          "gingham crop"],
         ["%s fringed suede halter top with a denim mini skirt",
          "fringed halter"],
         ["%s pearl-snap western shirt worn open over a cropped rib tank with high-waisted jeans",
          "western shirt"],
         ["%s cropped leather jacket over a fitted lace bodysuit with a short corduroy skirt",
          "leather jacket"],
         ["%s short tiered denim dress with a square neckline",
          "tiered dress"],
     ],
     "cores": ["off-white", "rust red", "dusty gold", "black"],
     "luz": "Soft grey-blue daylight through the wide window, flat and "
            "even.",
     "luz_c": "flat grey-blue daylight",
     "audio": "a quiet street, wind chimes",
     },
    # ---- miami ----
    {"id": "miami", "selo": "N", "familia": "miami",
     "etnias": ["Cuban American", "Black American"],
     "sala": "the living room of a pastel Miami apartment, a rattan "
             "peacock chair against a wall of jalousie windows, a polished "
             "terrazzo floor and tall palms swaying just outside the glass",
     "sala_c": "the same pastel living room",
     "banc": "the galley kitchen of the same apartment, mint-green tile "
             "behind her and a small stovetop coffee pot on the burner, "
             "the terrazzo floor running in from the living room",
     "sup_a": "a tiled breakfast bar",
     "sup": "bar",
     "trajes": [
         ["%s halter crop top with high-waisted linen shorts",
          "halter crop"],
         ["%s cut-out bodysuit with a wrap mini skirt",
          "cutout bodysuit"],
         ["%s ruched bandeau top with high-waisted white jeans",
          "bandeau top"],
         ["%s cropped tie-front shirt with a short ruffled rumba skirt",
          "tie-front shirt"],
         ["%s strappy bodycon mini dress",
          "bodycon mini"],
     ],
     "cores": ["hot coral", "white", "aqua blue", "lime green"],
     "luz": "Hard bright sun bounced off the pale walls, clean and "
            "high-key.",
     "luz_c": "bright high-key sun",
     "audio": "palm fronds rustling, distant gulls",
     },
    # ---- california ----
    {"id": "california", "selo": "N", "familia": "california",
     "etnias": ["white American", "Mexican American"],
     "sala": "the living room of a Southern California bungalow with pale "
             "plaster walls and a jute rug, a low rattan armchair with "
             "flat canvas cushions, a hanging macrame planter and a row of "
             "potted ferns along the sill, a wide picture window at "
             "frame-left opening onto a sun-bleached patio",
     "sala_c": "the same bungalow living room",
     "banc": "the kitchen of the same bungalow, pale open shelving stacked "
             "with ceramic bowls behind her and the same patio glare "
             "coming through the door",
     "sup_a": "a pale concrete counter",
     "sup": "counter",
     "trajes": [
         ["%s cropped ribbed tank with high-waisted linen shorts",
          "ribbed crop"],
         ["%s thin-strapped slip dress cut short above the knee",
          "slip dress"],
         ["%s triangle bikini top under an open gauze shirt, with a short sarong tied at the hip",
          "gauze shirt"],
         ["%s cropped terry-cloth polo with matching micro shorts",
          "terry set"],
         ["%s low-cut halter crop top with a short wrap skirt",
          "halter crop"],
     ],
     "cores": ["white", "sand beige", "faded olive", "black"],
     "luz": "Flat bright coastal daylight, soft-edged and even, from the "
            "picture window at frame-left.",
     "luz_c": "flat coastal daylight",
     "audio": "a wind chime, distant gulls",
     },
    # ---- arizona ----
    {"id": "arizona", "selo": "N", "familia": "arizona",
     "etnias": ["Mexican American", "white American"],
     "sala": "the front room of an Arizona adobe house with thick "
             "ochre-plastered walls, a low carved wooden bench heaped with "
             "striped wool blankets, a beehive corner fireplace at "
             "frame-right and a deep-set window dropping hard desert sun "
             "across the saltillo tile floor",
     "sala_c": "the same adobe front room",
     "banc": "the kitchen of the same adobe house, clay jars and dried "
             "chile bundles on an open shelf behind her, the same deep-set "
             "window looking out on red rock and cactus",
     "sup_a": "a hand-painted tile counter",
     "sup": "counter",
     "trajes": [
         ["%s off-shoulder crop blouse with embroidered trim and a short tiered skirt",
          "crop blouse"],
         ["%s bandeau top with hip-slung canvas shorts",
          "bandeau top"],
         ["%s square-neck crop top tucked into a short pleated skirt",
          "square crop"],
         ["%s short button-front sundress worn open at the throat, cut well above the knee",
          "short sundress"],
         ["%s crochet crop top with high-waisted shorts",
          "crochet crop"],
     ],
     "cores": ["turquoise", "terracotta", "cream", "black"],
     "luz": "Hard desert sun through the deep-set window, shadows cut "
            "sharp on the tile.",
     "luz_c": "hard desert sun",
     "audio": "dry wind, a distant truck",
     },
    # ---- vegas ----
    {"id": "vegas", "selo": "N", "familia": "vegas",
     "etnias": ["white American", "Mexican American"],
     "sala": "the living room of a top-floor Las Vegas apartment with "
             "glossy dark built-ins along the wall and a polished concrete "
             "floor, a low grey sectional with a smoked-glass table in "
             "front of her, a chrome floor lamp at frame-right and "
             "floor-to-ceiling balcony glass behind showing low desert "
             "rooftops",
     "sala_c": "the same top-floor living room",
     "banc": "the kitchen of the same top-floor apartment, glossy dark "
             "cabinets and a stack of tumblers by the sink behind her, "
             "light off the same balcony glass filling the room",
     "sup_a": "a black quartz island",
     "sup": "island",
     "trajes": [
         ["%s tight low-cut bodycon mini dress",
          "bodycon mini"],
         ["%s satin cami with thin straps and short satin shorts",
          "satin cami"],
         ["%s cropped mesh-panel top with a short leather skirt",
          "mesh crop"],
         ["%s sheer robe worn open over a bra top and high-cut shorts",
          "sheer robe"],
         ["%s one-shoulder bodysuit with a very short skirt",
          "one-shoulder bodysuit"],
     ],
     "cores": ["black", "gold", "silver", "hot pink"],
     "luz": "Cool even light bouncing off the balcony glass and the "
            "polished floor.",
     "luz_c": "cool bounced light",
     "audio": "an air-conditioner, faint traffic",
     },
    # ---- texas ----
    {"id": "texas", "selo": "N", "familia": "texas",
     "etnias": ["white American", "Mexican American"],
     "sala": "the den of a Texas ranch house with cedar beams overhead and "
             "a rough stone fireplace behind her, a worn leather club "
             "chair with a folded hide over the arm, a pair of dusty boots "
             "on the plank floor and a screen door standing open onto dry "
             "scrub at frame-left",
     "sala_c": "the same ranch den",
     "banc": "the kitchen of the same ranch house, a pine hutch stacked "
             "with enamel plates and a cast-iron skillet behind her, the "
             "same screen door letting the hot scrub light in",
     "sup_a": "a thick mesquite butcher block",
     "sup": "block",
     "trajes": [
         ["%s pearl-snap western shirt knotted high at the ribs with short denim cut-offs",
          "knotted pearl-snap"],
         ["%s bandana halter tied at the back with a short suede skirt",
          "bandana halter"],
         ["%s low-cut fitted tee tucked into short shorts with a tooled leather belt",
          "fitted tee"],
         ["%s fringed crop top with a short denim skirt",
          "fringed crop"],
         ["%s gingham tie-front top cropped at the ribs with high-waisted shorts",
          "gingham tie-front"],
     ],
     "cores": ["washed indigo", "white", "scarlet", "black"],
     "luz": "Warm low afternoon light coming flat through the open screen "
            "door.",
     "luz_c": "warm afternoon light",
     "audio": "cicadas, a screen door tapping",
     },
    # ---- apalache ----
    {"id": "apalache", "selo": "N", "familia": "apalache",
     "etnias": ["white American"],
     "sala": "the front room of a hollow farmhouse in the Appalachian "
             "mountains, a horsehair settee under a quilt pieced in small "
             "squares, a fiddle and a hand-carved walking stick hanging on "
             "the plank wall behind her, a rag rug over the wide "
             "floorboards and a laurel-choked slope filling the window at "
             "frame-left",
     "sala_c": "the same farmhouse front room",
     "banc": "the kitchen of the same hollow farmhouse, a punched-tin "
             "jelly cupboard and a hand pump at the dry sink behind her, "
             "the same laurel slope in the window",
     "sup_a": "a battered oak kitchen table",
     "sup": "table",
     "trajes": [
         ["%s gingham crop top knotted under the bust with cut-off denim shorts",
          "gingham crop"],
         ["%s thin cotton sundress cut short above the knee, straps slipped off the shoulders",
          "short sundress"],
         ["%s calico halter top tied behind the neck with cut-off denim shorts",
          "calico halter"],
         ["%s plaid flannel shirt worn open over a fitted cropped tank and frayed jean shorts",
          "open flannel"],
         ["%s cut-off denim shortalls buckled loose over a snug cropped tee, legs bare",
          "denim shortalls"],
     ],
     "cores": ["faded red", "washed blue", "cream", "moss green"],
     "luz": "Grey light off a wet hollow coming flat through the window, "
            "cool and low-contrast.",
     "luz_c": "flat hollow light",
     "audio": "creek water, a hound barking",
     },
    # ---- meio_oeste ----
    {"id": "meio_oeste", "selo": "N", "familia": "meio_oeste",
     "etnias": ["white American"],
     "sala": "the wood-panelled family room of a Midwestern farmhouse, a "
             "brown corduroy sofa with a crocheted afghan folded over the "
             "arm, a boxy wooden console cabinet at frame-left with a "
             "ceramic pheasant on top, and a wide window behind the sofa "
             "opening onto flat corn fields",
     "sala_c": "the same panelled family room",
     "banc": "the kitchen of the same Midwestern farmhouse, harvest-gold "
             "cabinets and a window over the sink behind her, the same "
             "corn fields flat beyond the glass",
     "sup_a": "a wide steel-edged kitchen counter",
     "sup": "counter",
     "trajes": [
         ["%s cropped cutoff sweatshirt slipping off one shoulder with denim shorts",
          "cut sweatshirt"],
         ["%s bandeau top with high-waisted denim shorts, shoulders and midriff bare",
          "bandeau top"],
         ["%s stretch bodysuit with a scooped neckline and a short pleated skirt",
          "scooped bodysuit"],
         ["%s sleeveless jersey crop top knotted at the hip over running shorts",
          "jersey crop"],
         ["%s thin-strap cotton camisole with the hem loose over jeans rolled low on the hips",
          "strap camisole"],
     ],
     "cores": ["cream", "faded maroon", "navy blue", "butter yellow"],
     "luz": "Low late-day sun raking in sideways over the fields, long "
            "warm shadows across the panelling.",
     "luz_c": "low raking sun",
     "audio": "wind over fields, distant tractor",
     },
    # ---- chicago ----
    {"id": "chicago", "selo": "N", "familia": "chicago",
     "etnias": ["Black American", "white American"],
     "sala": "the front room of a Chicago two-flat, a low velvet couch set "
             "into a three-pane bay window, dark oak trim and a built-in "
             "bookcase with leaded glass doors behind her, a cast-iron "
             "radiator under the sill and the brick wall of the next "
             "building close beyond the glass",
     "sala_c": "the same bay-window front room",
     "banc": "the galley kitchen of the same two-flat, painted cabinets "
             "and the glazed back door onto the wooden rear stairs behind "
             "her",
     "sup_a": "a chipped white tile counter",
     "sup": "counter",
     "trajes": [
         ["%s cropped hoodie cut off above the navel with high-waisted leggings",
          "cropped hoodie"],
         ["%s satin slip dress on thin straps, cut short above the knee",
          "satin slip"],
         ["%s fitted crop tank under an open oversized leather jacket, midriff bare, with low-slung wide-leg trousers",
          "crop tank"],
         ["%s bodycon knit mini dress with a bare back",
          "mini dress"],
         ["%s cropped puffer vest zipped over a thin long-sleeve top, midriff bare, with high-waisted jeans",
          "puffer crop"],
     ],
     "cores": ["black", "deep burgundy", "silver grey", "ivory"],
     "luz": "Cool blue north light bouncing off the brick wall next door, "
            "soft and even.",
     "luz_c": "cool north light",
     "audio": "an el train, muffled traffic",
     },
    # ---- detroit ----
    {"id": "detroit", "selo": "N", "familia": "detroit",
     "etnias": ["Black American", "white American"],
     "sala": "the living room of a Detroit brick bungalow, a tufted "
             "leather armchair pulled up to a tiled fireplace, a wide "
             "plaster arch through to the dining room behind her, a floor "
             "lamp with a fringed shade throwing light in from frame-right "
             "and a pale cold window over the front porch",
     "sala_c": "the same bungalow living room",
     "banc": "the kitchen of the same brick bungalow, painted steel "
             "cabinets and the swinging door through to that same dining "
             "room behind her, checkered vinyl underfoot",
     "sup_a": "a boomerang-pattern formica dinette table",
     "sup": "table",
     "trajes": [
         ["%s knotted jersey tee tied above the waist with track pants rolled low at the hip",
          "knotted tee"],
         ["%s off-the-shoulder knit top cropped above the navel with fitted jeans",
          "off-shoulder knit"],
         ["%s fitted sleeveless turtleneck cropped at the ribs with a wrap mini skirt",
          "turtleneck crop"],
         ["%s zip-front velour track top cropped at the ribs, unzipped at the chest, with hip-slung wide jeans",
          "track top"],
         ["%s sleeveless mini dress cut above the knee with a front zip pulled low at the chest",
          "zip mini"],
     ],
     "cores": ["charcoal", "deep red", "off-white", "cobalt blue"],
     "luz": "Warm lamplight indoors set against the pale cold daylight at "
            "the window behind her.",
     "luz_c": "warm indoor lamplight",
     "audio": "furnace humming, a passing car",
     },
]

FAMILIAS_MUNDO = list(dict.fromkeys(m["familia"] for m in MUNDOS))


# ---------------------------------------------------------------------------
# ⭐ NARRADORAS — o rosto
# ---------------------------------------------------------------------------
# ⛔ ZERO adjetivo de etnia dentro das entradas: quem injeta e' a montagem, a
# partir do MUNDO. Mesmo contrato do NECROSE (o motor injeta antes da marca) e do
# EXTERIOR (EX10) — pool unico serve todos os mundos, e o linter cobra.
# ⚠️ PORTE E IDADE seguem a fonte: ela e' magra, em forma e tem por volta de 35.
# Este e' um agente em que a narradora aparece de corpo inteiro, sentada e de
# pe', e o publico e' masculino — a apresentacao dela e' carga funcional.
# ⚠️ MARCA FACIAL OBRIGATORIA em toda entrada: sem ancora distintiva o Veo
# devolve o mesmo rosto generico em todo video e, pior, troca de pessoa entre os
# blocos de 8s (que aqui sao em cenarios diferentes — CO7).
# ⚠️ Os eixos que o `medir_personagens.py` cobra estao todos cobertos: cabelo,
# oculos, pele, porte e ancora. ⛔ `pelo_facial` e' zero POR DOUTRINA: sao todas
# mulheres.
# ⛔⛔ LEI DO REF — A NARRADORA E' SEMPRE MUITO BONITA E JOVEM.
# Ordem do operador, 2026-08-03, olhando o lote: *"ref mulheres sempre muito
# lindas"*. Vale como lei permanente deste agente, nao como ajuste de lote.
#
# ⚠️ ESTE POOL FOI REESCRITO PORQUE A PRIMEIRA VERSAO ERA O MESMO ERRO QUE JA'
# CUSTOU O RESSURREICAO: eu escrevi as entradas otimizando para o
# `medir_personagens.py`, que premia OCULOS, PELE MARCADA e LINHAS PROFUNDAS —
# e o pool devolveu narradoras de 40, 42 e 44 anos, grisalhas, de oculos de
# leitura e "deeply lined skin", num agente em que ela e' quem vende para homem.
# Otimizar a metrica contra o objetivo. O eixo `oculos` fica ZERADO de proposito
# e a excecao esta' declarada no medidor.
#
# ⛔ A ANCORA FACIAL CONTINUA OBRIGATORIA (P6) — sem ela o Veo troca de rosto
# entre os blocos de 8s, e neste agente a cena 1 e a 2 sao em ambientes
# diferentes, que e' onde ele mais troca. Mas ela e' DISTINTIVA, NUNCA
# DETERIORADA (licoes-producao-veo §REF): sinal de beleza — marca de nascenca,
# covinha, olho de cor incomum, sarda, falha entre os dentes da frente, malar
# alto. ⛔ Nunca dente lascado, palpebra caida, pele castigada.
NARRADORAS = [
    {"idade": 25,
     "cabeca": "long loose waves falling well past her shoulders",
     "marca": "a tiny dark mole at the outer corner of her left eye",
     "corpo": "a full hourglass shape with a very narrow waist, a heavy "
              "round bust, a soft flat belly, broad curved hips and strong "
              "shapely legs",
     },
    {"idade": 31,
     "cabeca": "long spiral curls hanging loose down her back",
     "marca": "a deep dimple that shows only in her right cheek",
     "corpo": "tall and statuesque with wide hips and a long torso, a high "
              "full chest, a firm smooth midriff, a deep round backside "
              "and very long muscular legs",
     },
    {"idade": 22,
     "cabeca": "a blunt glossy cut falling to mid-back",
     "marca": "a scattering of dark freckles across the bridge of her nose",
     "corpo": "short and thickly curvy from top to bottom, a full soft "
              "bust, a rounded softly padded tummy, wide generous hips and "
              "short thick legs",
     },
    {"idade": 28,
     "cabeca": "loose curtain-banged hair falling past her shoulders",
     "marca": "a pair of unusually pale grey eyes under straight dark "
              "brows",
     "corpo": "an athletic build on a wide-hipped frame, a full high bust, "
              "a firm ridged stomach, a lifted muscular seat and long "
              "powerful legs",
     },
    {"idade": 34,
     "cabeca": "waist-length hair parted straight down the middle",
     "marca": "a small crescent-shaped birthmark on her left temple",
     "corpo": "full-figured and soft all over, a very full heavy bust, a "
              "rounded soft waistline, a broad heavy rear and smooth full "
              "legs",
     },
    {"idade": 26,
     "cabeca": "a deep side part with thick loose curls",
     "marca": "a fine pale scar tracing the line of her jaw",
     "corpo": "a pear-shaped build with a small waist, a rounded "
              "medium-full bust, a smooth flat midriff, very wide flaring "
              "hips and long heavy legs",
     },
    {"idade": 30,
     "cabeca": "heavy blown-out hair swinging below her shoulder blades",
     "marca": "a tiny gold stud set in her left nostril",
     "corpo": "broad-shouldered and solidly built, a full weighty chest, a "
              "thick firm middle, a broad round bottom and sturdy thick "
              "legs",
     },
    {"idade": 23,
     "cabeca": "long choppy layers falling loose past her chest",
     "marca": "a narrow gap between her two front teeth",
     "corpo": "a top-heavy build with sloping shoulders and a short "
              "cinched waist, a very full high bust, a taut flat stomach, "
              "a high round seat and smooth thick legs",
     },
    {"idade": 33,
     "cabeca": "poker-straight hair hanging loose past her elbows",
     "marca": "one hazel eye and one clear blue eye",
     "corpo": "tall and full-figured with a long waist, a large soft bust, "
              "a gently curved stomach, heavy rounded hips and long thick "
              "legs",
     },
    {"idade": 29,
     "cabeca": "long hair tousled and pushed over one shoulder",
     "marca": "a shallow cleft in the middle of her chin",
     "corpo": "a short strong frame with a nipped-in waist, a round high "
              "chest, a firm flat abdomen, a very full lifted rear and "
              "short muscular legs",
     },
    {"idade": 27,
     "cabeca": "a blunt jet-black bob cut level at the chin",
     "marca": "a dark beauty mark high on her right cheekbone",
     "corpo": "a deep hourglass shape with a hand-span waist, a heavy "
              "round bust, a soft rounded lower belly, a wide flaring seat "
              "and full tapering legs",
     },
    {"idade": 31,
     "cabeca": "a cropped pixie feathered soft across the forehead",
     "marca": "a deep dimple that dents her left cheek when she talks",
     "corpo": "a tall statuesque frame that carries real weight, a heavy "
              "low-set bust, a gently domed stomach, a broad deep backside "
              "and long thick legs",
     },
    {"idade": 24,
     "cabeca": "honey-blonde waves cut short just below the ears",
     "marca": "a scatter of freckles across the bridge of her nose",
     "corpo": "a top-heavy build with a sharply nipped waist, a very full "
              "high shelf of a bust, a small soft curve below the navel, a "
              "wide round bottom and sturdy smooth legs",
     },
    {"idade": 29,
     "cabeca": "a soft brown mid-length cut with heavy curtain bangs",
     "marca": "a fine pale scar cutting through her left eyebrow",
     "corpo": "an athletic build with a broad flaring pelvis, a firm high "
              "bust, a hard flat abdomen with a visible center line, a "
              "squared muscular seat and thick sprinter legs",
     },
    {"idade": 22,
     "cabeca": "short tight curls piled full and high",
     "marca": "wide-set eyes of an unusual amber gold",
     "corpo": "a pear-shaped body with a tiny waist above heavy hips, a "
              "round upturned bust, a smooth flat stomach, a wide low-set "
              "rear and full heavy legs",
     },
    {"idade": 33,
     "cabeca": "a chestnut lob shaved close underneath on one side",
     "marca": "a tiny silver stud in her left nostril",
     "corpo": "a tall broad-shouldered frame, a full round bust set high, "
              "a long smooth stomach, a firm shelf-like rear and very long "
              "strong legs",
     },
    {"idade": 26,
     "cabeca": "a copper-red wolf cut layered to the collarbone",
     "marca": "a small mole just below the corner of her mouth",
     "corpo": "a short plush body with a low easy waist, a large heavy "
              "bust, a rounded padded belly, a broad wide-set bottom and "
              "thick smooth legs",
     },
    {"idade": 30,
     "cabeca": "a dark undercut with the top swept long",
     "marca": "a narrow gap between her front teeth and a small mole below "
              "one eye",
     "corpo": "a curvy build cinched hard at the middle, a rounded medium "
              "bust, a firm flat stomach, a very deep round rear and short "
              "thick legs",
     },
    {"idade": 23,
     "cabeca": "an ash-blonde shag falling loose to the shoulders",
     "marca": "one bright grey eye and one deep brown eye",
     "corpo": "a long-limbed body wide at the chest and hips, a heavy full "
              "bust, a softly rounded lower stomach, a big sloping rear "
              "and long thick legs",
     },
    {"idade": 34,
     "cabeca": "a side-parted crop set into shining finger waves",
     "marca": "a small crescent birthmark on her jaw below one ear",
     "corpo": "a big strong frame with a wide back and heavy hips, a full "
              "weighty bust, a firm stomach under a soft layer, a very "
              "round high rear and thick powerful legs",
     },
    {"idade": 26,
     "cabeca": "a long sleek jet-black ponytail pulled high",
     "marca": "a shallow cleft in her chin",
     "corpo": "a full hourglass build with a very small waist, a heavy "
              "round bust, a soft flat stomach, wide firm glutes and long "
              "smooth legs",
     },
    {"idade": 31,
     "cabeca": "honey-blonde hair wrapped into a glossy topknot",
     "marca": "a small dark mole at the outer corner of her left eye",
     "corpo": "a tall statuesque build with a long torso, a very full high "
              "bust, a smooth softly toned stomach, heavy round glutes and "
              "long strong legs",
     },
    {"idade": 24,
     "cabeca": "one thick chestnut braid over her shoulder",
     "marca": "a tiny beauty mark high on her right cheekbone",
     "corpo": "a short deeply curved build, a large soft low bust, a "
              "rounded belly, wide heavy glutes and short thick legs",
     },
    {"idade": 29,
     "cabeca": "a tight three-strand braid pinned down her back",
     "marca": "a small gold stud in her right nostril",
     "corpo": "a broad-shouldered athletic build with wide hips, a full "
              "bust, a hard flat stomach, wide round glutes and thick "
              "strong legs",
     },
    {"idade": 22,
     "cabeca": "copper-red hair twisted into a low bun",
     "marca": "a crescent-shaped birthmark at her right temple",
     "corpo": "a long-limbed curvy build with a small waist, a high round "
              "bust, a narrow midsection, high firm glutes and very long "
              "legs",
     },
    {"idade": 34,
     "cabeca": "half her dark waves clipped back loosely",
     "marca": "a deep dimple that shows only in her left cheek",
     "corpo": "an evenly plush build with a low soft waist, a heavy full "
              "bust sitting low, a full soft stomach, broad soft glutes "
              "and full smooth legs",
     },
    {"idade": 27,
     "cabeca": "dark brown hair in two neat space buns",
     "marca": "a narrow pale scar just under her lower lip",
     "corpo": "a top-heavy build with a narrow waist, a very full heavy "
              "bust, a small soft stomach, neat high glutes and straight "
              "strong legs",
     },
    {"idade": 25,
     "cabeca": "a red bandana tying back her thick curls",
     "marca": "a narrow gap between her front teeth and a light spray of "
              "freckles across her nose",
     "corpo": "a deep pear-shaped build, a full soft bust, a soft flat "
              "stomach, very wide heavy glutes and thick smooth legs",
     },
    {"idade": 32,
     "cabeca": "a wide braid wrapped over her head",
     "marca": "a small pale birthmark shaped like a comma below her left "
              "eye",
     "corpo": "a tall heavy-set build with wide square shoulders, a high "
              "generous bust, a firm rounded stomach, deep round glutes "
              "and long heavy legs",
     },
    {"idade": 28,
     "cabeca": "caramel hair twisted up into a claw clip",
     "marca": "a fine pale scar splitting her right eyebrow",
     "corpo": "a strong-hipped curvy build with a small waist, a firm "
              "round bust, a soft toned stomach, high lifted round glutes "
              "and heavy smooth legs",
     },
]



# ---------------------------------------------------------------------------
# ⭐ PROPS — o objeto no colo
# ---------------------------------------------------------------------------
# ⚠️ POOL DE PROXIES, decisao do operador (2026-08-03), contra a alternativa de
# travar em banana como a fonte. A copy NOMEIA o prop sorteado com todas as
# letras (`on your banana`, `on your cucumber`) — ordem dele: *"seja direto na
# referencia do prop, sem drifting copy"*.
# ⛔ Por isso todo prop tem de caber em `on your %s` na boca de alguem falando
# ingles americano. E' o filtro que exclui geoduck e mariscos: `on your geoduck`
# nao e' frase que se diz. Este agente nao tem marisco — e' produce.
# ⚠️ `em_pe` descreve como o objeto FICA EM PE', que e' a exigencia do CO1: prop
# que nao para em pe' sozinho nao serve a este hook.
# ---------------------------------------------------------------------------
# ⭐ HOMENS — o segundo personagem da cena 1, cortado na cintura
# ---------------------------------------------------------------------------
# ⛔ ELE E' O DONO DO PROBLEMA, e por isso existe: sem ele o hook e' uma mulher
# despejando oleo numa fruta; com ele, e' o colo de um homem sendo tratado na
# frente da camera. Foi o que eu tinha perdido na primeira leitura da fonte.
# ⛔ ZERO ROSTO E ZERO TRONCO — corte na cintura. E' a mesma economia do EX5 do
# EXTERIOR: um rosto a menos para manter identico entre blocos de 8s. Aqui o
# corte e' mais alto ainda (so' pernas e maos), entao a ANCORA DISTINTIVA TEM DE
# MORAR NA MAO E NA CALCA — nao ha' onde mais.
# ⛔ Zero adjetivo de etnia nas entradas: quem injeta e' a montagem, a partir do
# MUNDO. Mesmo contrato das NARRADORAS.
# ⚠️ A calca e' sempre COMPRIDA e o joelho fica coberto: perna nua de homem
# adulto sentado com o colo em primeiro plano e' geometria que o classificador
# olha com lupa, sem nada a ganhar em conversao.
HOMENS = [
    {"id": "cargo_caqui", "selo": "V",
     "calca": "loose khaki cargo trousers",
     "maos": "broad and squared, with short blunt nails",
     "marca": "a plain gold wedding band on his left ring finger"},
    {"id": "jeans_escuro", "selo": "N",
     "calca": "dark straight-leg jeans",
     "maos": "large, with heavy knuckles",
     "marca": "a pale old scar across the back of his left hand"},
    {"id": "moletom_cinza", "selo": "N",
     "calca": "grey sweatpants",
     "maos": "thick-fingered, the skin dry across the knuckles",
     "marca": "a wide steel watch loose on his left wrist"},
    {"id": "chino_bege", "selo": "N",
     "calca": "beige chino trousers",
     "maos": "long and bony, with prominent veins",
     "marca": "a faded green tattoo band around his left wrist"},
    {"id": "jeans_gasto", "selo": "N",
     "calca": "faded blue jeans worn white at the knee",
     "maos": "work-hardened, with calloused palms",
     "marca": "a thumbnail ridged and darkened from an old injury"},
    {"id": "calca_lona", "selo": "N",
     "calca": "heavy brown canvas work trousers",
     "maos": "big and weathered, with cracked skin at the joints",
     "marca": "a thick silver ring on his left index finger"},
    {"id": "moletom_marinho", "selo": "N",
     "calca": "navy jogging bottoms with a drawstring",
     "maos": "soft and wide, with neatly cut nails",
     "marca": "a small dark mole on the back of his left hand"},
    {"id": "calca_social", "selo": "N",
     "calca": "charcoal dress trousers with a pressed crease",
     "maos": "clean and slim",
     "marca": "a leather-strapped watch sitting square on his left wrist"},
    {"id": "bermuda_comprida", "selo": "N",
     "calca": "long olive utility trousers with a side pocket",
     "maos": "square, with sun-darkened backs",
     "marca": "a white band of untanned skin where a ring used to be"},
    {"id": "jeans_preto", "selo": "N",
     "calca": "black jeans",
     "maos": "heavy, with thick wrists",
     "marca": "a raised knuckle on his left middle finger, healed crooked"},
    # + 2026-08-04: ampliacao por ordem do operador — *"aumente o pool de
    # personagens... faca isso para pelo menos outros 5 agentes shorts"*.
    # ⛔ Cada entrada difere das outras em >= 3 eixos fisicos (licoes §15):
    # contar entradas nao basta, o que conta e' quantos eixos elas acionam.
    {"id": "sarja_verde", "selo": "N",
     "calca": "dark green twill trousers",
     "maos": "wide and flat-backed, the nails short and clean",
     "marca": "a woven leather band on his left wrist"},
    {"id": "jeans_claro", "selo": "N",
     "calca": "light stonewashed jeans",
     "maos": "narrow and long-fingered, the tendons standing out",
     "marca": "a black rubber sports watch on his left wrist"},
    {"id": "corduroy_ferrugem", "selo": "N",
     "calca": "rust corduroy trousers",
     "maos": "square and heavy, the palms deeply lined",
     "marca": "a copper ring worn thin on his left middle finger"},
    {"id": "moletom_carvao", "selo": "N",
     "calca": "charcoal jogging bottoms with a drawstring",
     "maos": "thick through the palm, the knuckles darkened",
     "marca": "a faint white burn mark across the back of his left hand"},
    {"id": "cargo_cinza", "selo": "N",
     "calca": "grey cargo trousers with a knee pocket",
     "maos": "big and blunt, the fingertips flattened",
     "marca": "a split thumbnail healed into two ridges"},
    {"id": "linho_areia", "selo": "N",
     "calca": "sand-coloured linen trousers",
     "maos": "smooth and even, with neatly filed nails",
     "marca": "a slim silver band on his left ring finger"},
]

# ⭐⭐ POOL VALIDADO PROMPT A PROMPT EM 2026-08-03. Cada entrada aqui custou uma
# geracao real, e as strings sao EXATAMENTE as que passaram — ⛔ nao redigitar,
# nao "melhorar", nao harmonizar.
#
# ⛔ A REGRA DE FORMA QUE OS NOVE TESTES DESENHARAM:
#     PASSA  quem quebra a leitura de cilindro — casca dobrada (banana,
#            banana-da-terra), afunilamento conico (cenoura, pastinaca) ou
#            cabo no topo (berinjela)
#     CAI    cilindro de DIAMETRO CONSTANTE terminando em PONTA ROMBA —
#            pepino (2 recusas), abobrinha (1), daikon (1)
# ⚠️ A cor NAO e' o discriminante: a banana-da-terra e' verde e passa; o daikon
# e' branco e cai. Foi hipotese minha durante o teste e foi refutada pelo daikon.
# ⚠️ O MILHO saiu por outro motivo — nao politica, COMPOSICAO: a palha aberta em
# tiras e' uma silhueta grande que sequestra o quadro, e o render colapsou os
# dois personagens num so'.
#
# ⛔ SAO CINCO, E ISSO E' DE PROPOSITO. O piso de eixo visual deste motor e' 7, e
# eu NAO vou completar com entradas nao testadas: foi exatamente esse o erro do
# lote anterior (dez props no pool, cinco nunca gerados, quatro reprovados em
# campo). Pool e' o que passou, nao o que cabe. `abobora_pescoco` ficou de fora
# por nao ter sido testado, nao por ter falhado — um render resolve.
#
# ⚠️ HIPOTESE REGISTRADA E NAO APLICADA: os props de corte reto (berinjela,
# cenoura, pastinaca) sairam com o prop mais ALTO que os de casca dobrada, e o
# operador os classificou como "razoavel" contra o "lindamente" da
# banana-da-terra. A leitura e' que o punho sem agarre concreto solta o objeto
# mais alto. ⛔ NAO foi aplicado: mexer no `punho` deles seria reescrever string
# validada por deducao minha, sem teste — o erro que este dia inteiro custou a
# aprender. Testar antes de aplicar.
PROPS = [
    {"id": "banana_da_terra", "selo": "V", "nome": "plantain",
     "img": "a large green plantain, peeled halfway with the thick peel "
            "folded back around its base",
     "punho": "its folded peel"},
    {"id": "banana", "selo": "V", "nome": "banana",
     "img": "a ripe yellow banana, peeled halfway down with the peel folded "
            "back in strips around its base",
     "punho": "its folded peel"},
    {"id": "berinjela", "selo": "V", "nome": "eggplant",
     "img": "a long slim purple eggplant with its green cap still on, the "
            "lower end squared off flat",
     "punho": "its squared-off lower end"},
    {"id": "cenoura", "selo": "V", "nome": "carrot",
     "img": "a thick orange carrot with the greens cut off and the wide end "
            "squared flat",
     "punho": "its wide cut end"},
    {"id": "pastinaca", "selo": "V", "nome": "parsnip",
     "img": "a large pale parsnip, the thick end trimmed flat",
     "punho": "its trimmed lower end"},
]



# ---------------------------------------------------------------------------
# ⭐ SUBSTANCIAS — a isca absurda que ela manda despejar
# ---------------------------------------------------------------------------
# ⚠️ TODAS LIQUIDAS E DESPEJADAS DE UM RECIPIENTE. A fonte despeja black seed oil
# de uma garrafinha de vidro escuro, e o jorro em fio e' metade do bit visual —
# po' nao cai em fio e o hook perde o movimento.
# ⛔ Zero marca legivel aqui (a P12 vale integralmente neste agente): a excecao
# nominal da marca real e' do EXTERIOR e so' dele.
SUBSTANCIAS = [
    {"id": "black_seed", "selo": "V", "nome": "black seed oil",
     "frasco": "a small dark glass bottle with no label",
     "jorro": "a thin line of near-black oil"},
    {"id": "mamona", "selo": "N", "nome": "castor oil",
     "frasco": "a small clear glass bottle with no label",
     "jorro": "a thick slow thread of clear oil"},
    {"id": "azeite", "selo": "N", "nome": "olive oil",
     "frasco": "a green glass cruet with a narrow spout",
     "jorro": "a thin line of golden-green oil"},
    {"id": "mel", "selo": "N", "nome": "raw honey",
     "frasco": "an unlabelled glass jar with a wide mouth",
     "jorro": "a slow thick thread of amber honey"},
    {"id": "vinagre", "selo": "N", "nome": "apple cider vinegar",
     "frasco": "a dark unlabelled glass bottle",
     "jorro": "a thin clear amber stream"},
    {"id": "coco", "selo": "N", "nome": "coconut oil",
     "frasco": "a wide unlabelled glass jar",
     "jorro": "a thin stream of clear melted oil"},
    {"id": "gergelim", "selo": "N", "nome": "sesame oil",
     "frasco": "a slim brown glass bottle with no label",
     "jorro": "a thin line of dark amber oil"},
    {"id": "abobora", "selo": "N", "nome": "pumpkin seed oil",
     "frasco": "a squat dark green glass bottle",
     "jorro": "a thin line of very dark green oil"},
    {"id": "aloe", "selo": "N", "nome": "aloe juice",
     "frasco": "a tall clear unlabelled bottle",
     "jorro": "a clear slightly thick stream"},
    {"id": "beterraba", "selo": "N", "nome": "beet juice",
     "frasco": "a clear glass carafe",
     "jorro": "a deep red-purple stream"},
    {"id": "linhaca", "selo": "N", "nome": "flaxseed oil",
     "frasco": "a small amber glass bottle with no label",
     "jorro": "a thin line of pale gold oil"},
    {"id": "oregano", "selo": "N", "nome": "oregano oil",
     "frasco": "a tiny dark dropper bottle with no label",
     "jorro": "a thin dark green stream"},
]


# ---------------------------------------------------------------------------
# COPY — cena 1: A ISCA + O DESMENTIDO
# ---------------------------------------------------------------------------
# ⭐ ESTRUTURA COPIADA DA FONTE, palavra por palavra no esqueleto:
#     "Pour black seed oil on your banana and watch how you will start lasting
#      hours in the bedroom. || Stop falling for that nonsense. But here is what
#      will actually work."
# ⛔ AS DUAS METADES ANDAM JUNTAS, SEMPRE. A promessa sozinha e' uma alegacao
# nossa; seguida do desmentido ela e' a isca que o video existe para derrubar. O
# linter cobra o par (CO8) — e e' regra de FUNCAO, do tipo que o repo aprendeu a
# cobrar depois de tres slots que passavam na forma e nao cumpriam o papel.
ISCAS_PROMESSA = [
    "and watch how you'll start lasting hours in the bedroom",
    "and watch how you'll be ready again in ten minutes",
    "and watch how you'll go all night like you're twenty",
    "and watch how it fixes your {o} by the weekend",
    "and watch how you'll never go soft again",
    "and watch how your {o} stands up on command",
    "and watch how you'll last three times longer tonight",
    "and watch how it wakes your {o} up in one day",
]

# ---------------------------------------------------------------------------
# ⛔ NAO HA' BULLET DE PROVA SOCIAL — E' DECISAO MEDIDA, NAO ESQUECIMENTO
# ---------------------------------------------------------------------------
# O operador pediu, em 2026-08-03: *"vc pode incluir um bullet na copy falada
# pra dizer o quanto ela esta' satisfeita com o desempenho do parceiro (bullet
# prova social) SE JULGAR QUE HA' MUITO ESPACO DE TEMPO SOBRANDO no take"*.
#
# A condicao dele era o espaco, entao a resposta foi medida e nao estimada:
#   · com bullets de 9 a 13 palavras -> entrou em   0 de 600 videos (0,0%)
#   · com bullets de 6 a 8 palavras  -> entrou em 122 de 600 videos (20,3%),
#     e custava 0,16 p/s na cena 1 (3,08 -> 3,24), que e' a cena do HOOK
# Com o numero na mesa ele decidiu: *"nao precisa incluir o bullet tb, ja' que
# nao sobra espaco"*. O pool foi removido.
#
# ⚠️ FICA REGISTRADO PARA NAO SER REABERTO NO ESCURO: o video ja' roda a 3,48
# palavras por segundo, que e' a capacidade real de narracao. Qualquer bullet
# novo nesta copy nao "cabe" — ele EMPURRA outra coisa para fora. Quem quiser
# incluir um, inclua sabendo o que vai sair no lugar.

DESMENTIDOS = [
    "Stop falling for that nonsense. Here's what actually works.",
    "Stop wasting food on that. Here's what actually works.",
    "That does nothing. Here's what actually works.",
    "None of that is true. Here's what actually works.",
    "Quit believing that. Here's what actually works.",
    "That's a waste of your time. Here's what actually works.",
    "It won't do a thing. Here's what actually works.",
]


# ---------------------------------------------------------------------------
# COPY — cena 2: A RECEITA (o mecanismo)
# ---------------------------------------------------------------------------
# ⛔⛔ CONGRUENCIA INVIOLAVEL: o mecanismo do criativo e' o que a VSL vende, e a
# nossa vende GELATIN nas cinco paginas. A fonte manda curcuma + gengibre + suco
# de melancia + suco de roma; nos mantemos a FORMA (po' + liquido, de manha, em
# jejum) e trocamos o miolo pela gelatina. O que varia e' o acompanhamento,
# nunca a ancora.
# ⛔ O literal `gelatin trick` e' obrigatorio nesta cena e o linter trava nele.
# ⚠️ A fonte diz "a tablespoon of X to a glass of Y" — e' a gramatica de receita
# que soa caseira. Mantida.
RECEITAS = [
    # ⛔⛔ MEDIDA E VASILHAME SAIRAM DA BOCA (2026-08-07, ordem do operador:
    # *"pronunciar spoon, etc e' desperdicar tempo valioso; o mesmo vale para
    # 'half of a lemon' em vez de apenas 'lemon'"* · *"ela nao precisa ter que
    # falar colher para aparecer uma colher na receita, tanto faz"*).
    # A colher CONTINUA em cena — so' sai do audio.
    #
    # ⭐ E NAO E' ECONOMIA DE ESTILO, E' O CORTE DE FALA: a cena 2 declarava
    # teto de 32 palavras contra o limite fisico de 25 em 8s, e 100% das falas
    # estouravam. `A spoon of gelatin and a spoon of cocoa in a glass of warm
    # milk` gastava NOVE palavras em duas colheres e um copo que o quadro ja'
    # mostra. Agora sao quatro.
    # ⚠️ FICA o momento do dia (vende habito) e FICA `gelatin`, que e' o
    # literal do mecanismo e a palavra do CTA.
    "Gelatin and ginger in pomegranate juice, every morning on an empty "
    "stomach",
    "Gelatin and turmeric in warm water, first thing in the morning",
    "Gelatin in watermelon juice, every morning before you eat anything",
    "Gelatin and lemon in cold water, every single morning",
    "Gelatin and raw honey in warm milk, before bed",
    "Gelatin and cinnamon in black coffee, every morning",
    "Gelatin and beet powder in water, on an empty stomach",
    "Gelatin in orange juice with cayenne, every morning",
    "Gelatin and ginger in warm water, twice a day",
    "Gelatin and cocoa in warm milk, every night",
]

# ⛔ A ANCORA. Toda entrada traz o literal `gelatin trick` E nomeia o orgao — sao
# as duas coisas que o colapso de 5 cenas para 3 ameacava levar embora.
ANCORAS = [
    "That's the gelatin trick, and your {o} wakes up in days",
    "That's the gelatin trick, and your {o} comes back within days",
    "That's the gelatin trick. Give it a week and your {o} answers again",
    "That's the gelatin trick, and it's your {o} that feels it first",
    "That's the gelatin trick — days, not months, and your {o} is back",
    "That's the gelatin trick, and your {o} stops letting you down",
    "That's the gelatin trick, and your {o} gets hard like it used to",
]


# ---------------------------------------------------------------------------
# COPY — cena 3: O CTA
# ---------------------------------------------------------------------------
# ⭐ A FONTE JA' TEM A NOSSA MECANICA INTEIRA, e por isso a cena 3 e' a mais
# fiel das tres: "If you want the complete circulation routine that takes this
# ten times further... Comment book and I will send you my bedroom protocol, but
# you have to follow me or I won't be able to reach out to you."
#     escalada  ->  ROTINAS
#     keyword   ->  CTA_LITERAL (`Comment gelatin,`) — literal do repo
#     isca      ->  ISCAS_ENTREGA (quase sempre `recipe`, ordem do operador)
#     gate      ->  GATES
ROTINAS = [
    "If you want the full routine that takes this ten times further",
    "If you want the complete protocol that takes this much further",
    "If you want the whole thing that gets your {o} all the way back",
    "If you want the rest of what I put together for men over forty",
    "If you want the full version of this that works ten times faster",
    "If you want everything I use with my clients",
    "If you want the complete routine that fixes your {o} for good",
    "If you want the part I'm not allowed to post here",
    # ⚠️ AS SEIS CURTAS ABAIXO EXISTEM POR ARITMETICA DE TEMPO, medida no
    # `--autoteste`. A cena 3 da FONTE roda de 0:23 a 0:40 — 17 segundos para
    # ~40 palavras. A nossa tem 8, e carrega as mesmas quatro funcoes
    # (escalada + keyword + isca + follow-gate), sendo que tres delas sao lei do
    # repo e nao encolhem. Sobra a ESCALADA como unica alavanca.
    # ⛔ Isto NAO e' encurtar linha aprovada (CL15): sao entradas NOVAS, no
    # comprimento que o formato paga. As longas continuam no pool e entram
    # sempre que a combinacao couber.
    # ⚠️ Metade traz `{o}`: com a cota do orgao caindo na cena 3, o sorteio fica
    # preso ao subconjunto `{o}`, e se ele so' tivesse linhas longas o teto
    # seria inalcancavel — que foi exatamente o que a primeira medicao mostrou.
    "If you want the whole routine for your {o}",
    "If you want what actually rebuilds your {o}",
    "If you want the real fix for your {o}",
    "If you want the rest of it",
    "If you want the whole protocol",
    "If you want everything else I use",
]

# ⚠️ `recipe` domina de proposito: ordem do operador, 2026-08-03 —
# *"sempre comente gelatin pra receber algo {isca} (geralmente sera recipe
# mesmo)"*. As outras existem para o lote nao virar bordao.
ISCAS_ENTREGA = [
    "the whole recipe", "the full recipe", "the complete recipe",
    "the exact recipe", "the recipe and the measurements",
    "my whole protocol", "the full routine", "the exact measurements",
    "the recipe", "the recipe and the doses",
]

GATES = [
    "But you have to follow me, or I can't reach you.",
    "Follow me first, or I can't reply to you.",
    "Don't forget to follow, or the app won't let me answer.",
    "Follow me before you comment, or it never reaches me.",
    "Make sure you're following, or I can't message you back.",
    "Hit follow first, or my message can't get to you.",
    "Follow me, or I won't be able to find your comment.",
    "Follow me first, or I can't reply.",
    "Follow me, or I can't message you.",
]

# ⛔ As palavras do orgao. Rotacionam DENTRO do video (nunca a mesma duas vezes).
NUCLEO = ["Johnson", "pecker", "wiener", "soldier", "tool"]

# ⚠️ Bandas medidas contra a capacidade real de 8s de narracao (~3,4 p/s). O
# autoteste mede a faixa que os pools REALMENTE produzem e reprova se o teto for
# estourado — teto que nenhuma combinacao alcanca e' teto decorativo.
# ⚠️ MEDIDOS CONTRA A CAPACIDADE REAL de 8s de narracao (~3,4 p/s = ~27
# palavras), nao escolhidos no olho. O `_cabem` faz o teto valer no SORTEIO, e o
# `--autoteste` imprime a faixa que os pools REALMENTE produzem — teto que
# nenhuma combinacao alcanca e' teto decorativo, e teto que toda combinacao
# estoura e' motor produzindo video reprovado.
# ⚠️ A cena 3 e' a mais densa das tres por construcao: ela carrega escalada +
# keyword + isca + follow-gate, quatro funcoes em 8 segundos. O EXTERIOR roda a
# dele a 4,20 p/s e o operador decidiu medir em campo; esta fica em ~3,9.
# ⛔⛔ TETO 25 — ordem permanente do operador, 2026-08-05: *"sempre meca. Nao
# pode haver cortes de fala."* O numero vem de render, nao de conta: 32
# cortou, 28 cortou. Os exemplos que ele escreve a mao vivem em 16-25
# palavras (2,0-3,1 palavras/s).
# ⚠️ cena 1 cortava em 29,5%. A cadeia ja' reservava o espaco; so' o teto estava largo.
# ⛔ NAO baixar [2] e [3] junto: medido, a cena 2 vai de max 32 para 34 e a 3 de
# 31 para 37, porque o `_cabem` termina em `or pool` e devolve tudo quando nada
# cabe. Baixar o teto dessas duas PIORA.
# ⭐⭐ MODO REF BELA — contrato compartilhado (short_comum), 2026-08-05.
# Ordem do operador: *"toggle de trava pra modo ref mulher bela em todos os ui
# ux pertinentes dos agentes shorts, que, quando ativados, gera refs mulheres
# com essas caracteristicas"* — super model, corpao, pouca roupa.
# ⛔ O pool e o helper moram no `short_comum`: um pool por motor divergiria em
# uma semana, e classificacao divergente e' o fragmento espelhado que a P9 proibe.
MODO_BELA = True

# ⛔ O TETO DA CENA 2 CAIU DE 32 PARA 25 (2026-08-07). O 32 era o teto da copy
# VERBOSA — `A spoon of gelatin and a spoon of cocoa in a glass of warm milk`
# gastava nove palavras em duas colheres e um copo. Com medida e vasilhame fora
# da boca, a fala cabe no limite FISICO de 25 em 8s, que e' o mesmo dos outros
# 18 motores. O medidor acusava 100% de corte de fala nesta cena; agora 0%.
# ⚠️ Teto declarado acima do fisico nao e' folga, e' permissao para cortar fala.
TETO_FALA = {1: 25, 2: 25, 3: 25}
# ⚠️ O piso da cena 2 caiu de 22 para 18 pelo MESMO motivo do teto: a fala
# enxuta entrega o mesmo conteudo em menos palavra, e piso alto demais nao
# produz densidade — produz um filtro que rejeita a copy boa e devolve a longa.
PISO_FALA = {1: 20, 2: 18, 3: 24}


# ---------------------------------------------------------------------------
# TRAVAS E EIXOS DO PAINEL
# ---------------------------------------------------------------------------
TRAVAS_UI = [
    ("familia_mundo", "nicho", ["livre"] + FAMILIAS_MUNDO),
]

EIXOS_TRAVAVEIS = ["mundo", "etnia", "ref", "homem", "prop",
                   "substancia", "receita"]


def etnias_do_mundo(spec):
    """O pool de ETNIA depende do MUNDO em cena — trocar para uma etnia que
    aquele mundo nao comporta e' exatamente a incongruencia que os MUNDOS
    existem para impedir."""
    return list(spec["mundo"]["etnias"])


etnias_do_mundo.recebe_spec = True

EIXOS_UI = [
    ("mundo", "MUNDO", "MUNDOS", "id"),
    ("etnia", "ETNIA", "etnias_do_mundo", None),
    ("ref", "QUEM FALA", "NARRADORAS", "cabeca"),
    ("homem", "O COLO", "HOMENS", "calca"),
    ("prop", "O PROP", "PROPS", "nome"),
    ("substancia", "A ISCA", "SUBSTANCIAS", "nome"),
    ("receita", "RECEITA", "RECEITAS", None),
]

CENAS_UI = ["1 · a isca no colo", "2 · a receita", "3 · o CTA"]


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
        return next((x for x in pool if x[chave] == valor), pool[0])
    return valor


def _artigo(s):
    return "an" if s[:1].lower() in "aeiou" else "a"


def _traje(spec):
    """A roupa SORTEADA do mundo, com o artigo certo.

    ⛔ O artigo NAO mora no template: cores como `off-white`, `indigo` e
    `olive` sairiam `a off-white` — bug pago no CLEAN v2 no mesmo dia, e achado
    LENDO o render, nao pelo linter.

    ⭐⭐ ERA UM TRAJE POR MUNDO, agora sao CINCO e o traje e' EIXO SORTEADO
    (2026-08-06, ordem do operador). Com um traje fixo por mundo, escolher a
    regiao escolhia a roupa — e um lote inteiro de uma regiao saia com a mesma
    blusa em quatro cores. O traje sorteado viaja no spec, entao a montagem
    e a ancora de continuidade leem o MESMO par.
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
    """As entradas do pool que cabem no teto daquela cena.

    ⛔ DESCARTA-SE A LINHA QUE NAO CABE, NUNCA SE ENCURTA A LINHA. E' a mesma
    regra do CLEAN (CL15) e pelo mesmo motivo: as linhas foram aprovadas uma a
    uma, e reescrever menor para caber e' trocar copy validada por copy nova sem
    validacao. Medido antes desta funcao existir: 348 dos 600 videos estouravam
    o teto — a cena 3 chegava a 37 palavras, 4,6 p/s, um terco acima do que cabe
    em 8 segundos de narracao.
    ⚠️ `or pool` porque lista vazia nao pode existir: antes de reprovar o
    sorteio, o teto cede e o linter reclama — e' ele quem tem de aparecer, nao
    um IndexError.
    """
    return [x for x in pool if _palavras(monta(x)) <= teto] or pool


def _com_o(pool):
    """As entradas que nomeiam o orgao."""
    return [x for x in pool if "{o}" in x]


def _falas(spec, rng, quais=(0, 1, 2)):
    """Monta as falas pedidas a partir dos pools ja' sorteados no spec.

    ⚠️ Uma funcao so' para as tres cenas, e nao tres blocos espalhados: o botao
    `trocar` da UI re-sorteia UMA fala, e duas copias desta conta e' a garantia
    de que uma delas envelhece mentindo (licao paga no CLEAN v2).

    ⭐ A COTA DO ORGAO E' GARANTIDA AQUI, NO SORTEIO — nao so' cobrada no linter.
    A cena 2 sempre nomeia o orgao (todas as ANCORAS trazem `{o}`), mas so' 4 das
    8 promessas e 2 das 8 rotinas trazem: sorteando solto, 1 em cada 3 videos
    saia com cota 1/3 e era o MOTOR que produzia o video reprovado. Linter que
    reprova o proprio motor e' aviso, nao defesa. O sorteio escolhe qual das
    pontas carrega o orgao e tira dela do subconjunto certo.
    """
    o1, o2 = spec["orgaos"]
    f = dict(spec.get("falas_map", {}))

    # quem, entre as pontas, tem de nomear o orgao nesta montagem
    if set(quais) >= {0, 2}:
        ponta = rng.choice([0, 2])
    else:
        # re-sorteio de UMA cena: so' obriga se as outras duas nao dao a cota
        outras = [v for k, v in f.items() if k not in quais]
        ja = sum(1 for v in outras
                 if any(n.lower() in v.lower() for n in NUCLEO))
        ponta = quais[0] if ja < 2 else None

    if 0 in quais:
        pool = _com_o(ISCAS_PROMESSA) if ponta == 0 else ISCAS_PROMESSA
        cabeca = "Pour %s on your %s " % (spec["substancia"]["nome"],
                                          spec["prop"]["nome"])
        curto = min(DESMENTIDOS, key=_palavras)
        pool = _cabem(pool, lambda p: cabeca + p.format(o=o1) + ". " + curto,
                      TETO_FALA[1])
        prom = rng.choice(pool).format(o=o1)
        desm = rng.choice(_cabem(DESMENTIDOS,
                                 lambda d: cabeca + prom + ". " + d,
                                 TETO_FALA[1]))
        f[0] = "%s%s. %s" % (cabeca, prom, desm)

    if 1 in quais:
        anc = rng.choice(_cabem(ANCORAS,
                                lambda a: spec["receita"] + ". "
                                + a.format(o=o2) + ".", TETO_FALA[2]))
        f[1] = "%s. %s." % (spec["receita"], anc.format(o=o2))

    if 2 in quais:
        pool = _com_o(ROTINAS) if ponta == 2 else ROTINAS
        isca = rng.choice(ISCAS_ENTREGA)

        def _c3(rot, gate):
            return "%s — %s and I'll send you %s. %s" % (
                rot.format(o=o2), sc.CTA_LITERAL, isca, gate)

        # ⛔ 2026-08-05 — `_cabem` termina em `or pool` e com teto 25 devolvia o
        # pool INTEIRO: a cena 3 subiu de max 31 para 36. Fallback passa a ser a
        # entrada mais CURTA, e a ISCA cede junto (unico slot com folga; o
        # `Comment gelatin,` e' intocavel).
        curto_g = min(GATES, key=_palavras)

        def _ok(p, monta):
            v = [x for x in p if _palavras(monta(x)) <= TETO_FALA[3]]
            return v or [min(p, key=lambda x: _palavras(monta(x)))]

        if _palavras(_c3(min(pool, key=_palavras), curto_g)) > TETO_FALA[3]:
            isca = min(ISCAS_ENTREGA, key=_palavras)
        rot = rng.choice(_ok(pool, lambda r: _c3(r, curto_g)))
        gate = rng.choice(_ok(GATES, lambda g: _c3(rot, g)))
        f[2] = _c3(rot, gate)

    return f


def sortear(pagina, rng, led, travas=None):
    """Monta a spec. `travas` fixa eixos (pre-selecao do painel e cadeado)."""
    travas = travas or {}
    usados = led.get(pagina, {})

    # ⭐ O MUNDO VEM PRIMEIRO: ele decide sala, bancada, traje, luz, ambiencia E
    # as etnias que aquele lugar comporta. Sorteio por FAMILIA e so' depois por
    # mundo dentro dela — sem isso a familia com mais sets domina o lote.
    # ⭐ TRAVA DE PELE — o mundo so' sai entre os que COMPORTAM a pele, e a
    # etnia sorteia dentro do mundo ja' filtrada.
    # ⛔ O filtro da ETNIA e' tao necessario quanto o do mundo: sem ele o mundo
    # passa (tem UMA etnia da pele) e a etnia sorteia entre TODAS as dele.
    _pele = travas.get("pele")

    def _comporta(_m):
        return not _pele or any(_pele_de(e) == _pele for e in _m["etnias"])

    def _etnias_ok(_m):
        return [e for e in _m["etnias"] if not _pele or _pele_de(e) == _pele]

    fam_trava = travas.get("familia_mundo")
    if travas.get("mundo"):
        mundo = _por_id(MUNDOS, travas["mundo"])
        if not _comporta(mundo):
            # ⛔ entre respeitar o mundo e respeitar a pele, cede o MUNDO
            mundo = rng.choice([m for m in MUNDOS
                                if m["familia"] == mundo["familia"]
                                and _comporta(m)]
                               or [m for m in MUNDOS if _comporta(m)])
    else:
        if fam_trava and fam_trava != "livre":
            fam = fam_trava
        else:
            fam = _fresco([{"id": f} for f in FAMILIAS_MUNDO],
                          usados.get("familia_mundo", []), rng, "id")["id"]
        _cand = [m for m in MUNDOS if m["familia"] == fam
                 and _comporta(m)]
        # familia sem mundo daquela pele: a FAMILIA cede, a pele nao
        mundo = rng.choice(_cand or [m for m in MUNDOS if _comporta(m)])

    et = travas.get("etnia") or rng.choice(_etnias_ok(mundo))
    cor = rng.choice(mundo["cores"])
    # ⭐ O TRAJE E' EIXO: cinco por mundo, sorteado por video. Viaja no spec
    # como o par [template, curto] — a montagem usa o template, a ancora de
    # continuidade usa o curto, e os dois SAO O MESMO par por construcao.
    traje = rng.choice(mundo["trajes"])
    ref = (travas.get("ref")
           or (sc.ref_bela(NARRADORAS[0], rng) if travas.get("bela")
               else rng.choice(NARRADORAS)))
    prop = (_por_id(PROPS, travas["prop"]) if travas.get("prop")
            else _fresco(PROPS, usados.get("prop", []), rng, "id"))
    subst = (_por_id(SUBSTANCIAS, travas["substancia"])
             if travas.get("substancia")
             else _fresco(SUBSTANCIAS, usados.get("substancia", []), rng, "id"))
    receita = travas.get("receita") or rng.choice(RECEITAS)
    # ⛔ O SEGUNDO PERSONAGEM da cena 1 — o dono do colo. Sem ele o hook e' uma
    # mulher despejando oleo numa fruta.
    homem = (_por_id(HOMENS, travas["homem"]) if travas.get("homem")
             else _fresco(HOMENS, usados.get("homem", []), rng, "id"))

    # ⛔ Dois orgaos DIFERENTES no mesmo video: repetir o substantivo em 24
    # segundos vira bordao.
    # ⛔ 2026-08-10 — SO' OS TRES APELIDOS SAO SORTEAVEIS (ordem do
    # operador, parque inteiro). `soldier` e `tool` seguem no NUCLEO porque
    # as LENTES os usam para DETECTAR o orgao; o que muda e' que nao saem
    # mais na fala. Ver `short_comum.orgaos_sorteaveis`.
    orgaos = sc.orgaos_sorteaveis(rng, 2)

    # ⭐ A FLAG VIAJA NO SPEC. O `montar()` nao recebe `travas`, e sem

    # isto a clausula do rosto e o `resumo_pt` ficavam na versao comum

    # enquanto o corpo e a roupa ja' eram os do modo — a contradicao

    # exata que o CL26 documenta.

    spec = {"pagina": pagina, "bela": bool(travas.get("bela")), "mundo": mundo, "etnia": et, "cor": cor, "traje": traje,
            "ref": ref, "homem": homem, "prop": prop, "substancia": subst,
            "receita": receita, "orgaos": orgaos}
    spec["falas"] = [v for _, v in sorted(_falas(spec, rng).items())]
    return spec


def _pessoa(spec):
    return ("a %d-year-old %s woman, %s, %s, %s, wearing %s"
            % (spec["ref"]["idade"], spec["etnia"], spec["ref"]["corpo"],
               spec["ref"]["cabeca"], spec["ref"]["marca"], _traje(spec)))


def _ancora(spec):
    """⛔ CO7 — a ancora de continuidade das cenas 2 e 3. Rosto E idade, nunca
    so' roupa: a troca de ambiente entre a cena 1 e a 2 e' onde o Veo mais troca
    de pessoa, e o TAKE diz `She is the only person`."""
    r = spec["ref"]
    return CO_ANCORA % (r["idade"], spec["etnia"], spec["cor"],
                        spec["traje"][1],
                        _sem_artigo(r["cabeca"].split(" and ")[0]),
                        _sem_artigo(r["marca"]))


def montar(spec):
    """Os 7 blocos. Formatacao NOMEADA de ponta a ponta — sao 15+ campos por
    bloco, e um deslocamento de indice posicional troca pronome por cor sem
    estourar erro nenhum (bug que so' aparece no video pronto)."""
    m, ref, prop = spec["mundo"], spec["ref"], spec["prop"]
    sub, hom = spec["substancia"], spec["homem"]
    v = {
        "sala": m["sala"], "sala_c": m["sala_c"], "banc": m["banc"],
        "sup": m["sup"], "sup_a": m["sup_a"], "sup_d": _sem_artigo(m["sup_a"]),
        "luz": m["luz"], "luz_c": m["luz_c"],
        "pessoa": _pessoa(spec), "ancora": _ancora(spec),
        "Ancora": _cap(_ancora(spec)),
        "idade": ref["idade"], "etnia": spec["etnia"],
        "prop_img": prop["img"], "prop_punho": prop["punho"],
        "prop_curto": prop["nome"],
        "frasco": sub["frasco"], "jorro": sub["jorro"],
        "gel": CO_GELATINA, "keyword": CO_KEYWORD_NA_MAO % CO_GELATINA,
        "estavel": CO_PROP_ESTAVEL,
        "nao_toca": CO_NAO_TOCA % m["sup"],
        "resto": CO_MESMA_BANCADA % m["sup"],
        "anti": (sc.ANTICELEB_BELA if spec.get("bela") else ANTICELEB),
        "cauda": CAUDA,
    }
    # ⛔ `_cap` no jorro: ele abre frase dentro da travada, e sem isto o bloco
    # sai com `a thin line of golden-green oil falls...` em minuscula no meio do
    # texto. Achado LENDO o render — o linter passou 600/600.
    # ⚠️ A etnia do homem vem do MUNDO, igual a' dela — congruencia de casal na
    # mesma cena. E ela entra na MAO, que e' a unica pele dele em quadro.
    # ⚠️ A etnia dele vem do MUNDO, igual a' dela, e entra na MAO — a unica pele
    # dele em quadro. ⛔ O campo `maos` nao repete o substantivo `hands`: a
    # primeira versao saia "His Hispanic American hands, broad squared hands
    # with short blunt nails" (achado lendo o render).
    v["homem_maos"] = ("His hands are the only skin of his in the frame — %s, "
                       "%s, and %s." % (spec["etnia"], hom["maos"],
                                        hom["marca"]))
    v["geometria"] = CO_GEOMETRIA % (hom["calca"], v["homem_maos"],
                                     v["prop_img"], v["prop_punho"],
                                     v["pessoa"], sub["frasco"],
                                     _cap(sub["jorro"]))
    v["layout"] = CO_BANCADA_LAYOUT % m["sup"]
    # ⛔ A pegada e' no SACHE, nao no copo: e' o sache que ela inclina, e o copo
    # fica parado na bancada. Punho inteiro em volta + antebraco apoiado e' o
    # anti-F12b (o Veo solta objeto que a mao "segura" sem estar descrita).
    v["pegada"] = _cap(CO_PEGADA % ("open white sachet of pale powder with no "
                                    "label", v["sup_d"],
                                    "tips it over the tall glass"))

    b = {}
    b["BLOCO 0 (REF)"] = (
        "REF 01: Photo of a real person, a %(idade)d-year-old %(etnia)s woman, "
        "chest up, facing the camera directly, neutral steady expression with "
        "her mouth closed. %(pessoa_curta)s An ordinary everyday relatable "
        "person with a plain unremarkable face, not a celebrity, not a model, "
        "not an actor, not resembling any famous person. Hands out of frame, "
        "no objects. Plain neutral gray background, soft even frontal light. "
        "Slight sensor grain, soft focus, raw iPhone front camera aesthetic. "
        "No subtitles, no captions, no burned-in text, no watermark."
        % dict(v, pessoa_curta="%s. %s. Wearing %s."
               % (_cap(ref["cabeca"]), _cap(ref["marca"]), _traje(spec))))

    # --- CENA 1 — SENTADA, A ISCA NO COLO (o hook) --------------------------
    # ⛔ O jorro JA' ESTA' caindo no frame 0: nao ha' frame de "antes". A mesma
    # economia do EXTERIOR e do TROCA — o video abre com a acao em andamento,
    # porque 8 segundos nao pagam uma preparacao.
    # ⚠️ A pessoa entra DENTRO da geometria, nao antes dela: a primeira versao
    # abria com "Seated in the chair, facing the camera, is <pessoa>." e a
    # travada logo em seguida repetia "She is sitting in a chair facing the
    # camera" — a mesma ordem dita duas vezes no mesmo bloco e' ruido, e ruido
    # em prompt de imagem e' superficie para o gerador escolher sozinho.
    b["IMAGE 01/03"] = (
        "Medium shot in %(sala)s. %(geometria)s She is looking straight into "
        "the lens with her mouth open mid-word as she speaks. They are the "
        "only two people in the frame, and his face is not in it. %(anti)s "
        "%(luz)s %(cauda)s" % v)

    # --- CENA 2 — DE PE' NA BANCADA, A RECEITA (o mecanismo) ----------------
    # ⚠️ MUDA DE AMBIENTE (ordem do operador): a fonte corta de sentada para de
    # pe' na cozinha exatamente aqui. A ancora de continuidade (CO7) e' o que
    # segura o rosto atravessando o corte.
    # ⛔ O prop do colo NAO vem junto: ele ficou na cena 1, que e' onde a isca
    # mora. Traze-lo para a bancada misturaria a isca desmentida com o mecanismo
    # verdadeiro no mesmo quadro.
    b["IMAGE 02/03"] = (
        "Medium shot in %(banc)s, filmed straight on at chest height and "
        "framed from the waist up. Standing behind %(sup_a)s, centred in the "
        "frame, is %(ancora)s. %(layout)s. %(pegada)s, held a hand's width "
        "above the rim, and a fall of pale powder is dropping from it straight "
        "down into the glass. Her left hand rests flat on the %(sup)s beside "
        "the glass. She looks directly into the lens with her mouth open "
        "mid-word as she speaks, her expression serious and certain. She is "
        "the only person in the frame. %(anti)s %(luz)s %(cauda)s" % v)

    # --- CENA 3 — O CTA, COM A GELATINA NA MAO ------------------------------
    # ⭐ O objeto da keyword esta' NA MAO no frame em que a boca diz `gelatin,`.
    # A fonte faz isso com o livro (t=00:35), que e' a keyword dela.
    # ⛔ CO5 — a gelatina em cubos so' aparece AQUI. Mostra-la antes entrega o
    # payoff antes da promessa.
    b["IMAGE 03/03"] = (
        "Closer medium shot in the same place, same background, same %(luz_c)s, "
        "filmed straight on and framed from the waist up. %(Ancora)s, standing "
        "centred in the frame. On the %(sup)s along the bottom edge of the "
        "frame, at frame-left, stands the same tall glass, now filled with the "
        "finished drink and no longer clear. %(keyword)s She looks directly "
        "into the lens, calm and confident, one corner of her mouth raised in "
        "a half-smile, her mouth open mid-word as she speaks. She is the only "
        "person in the frame. %(anti)s %(cauda)s" % v)

    # ⛔⛔ O TAKE ANIMA A IMAGE — ELE NAO INVENTA OUTRO GESTO.
    # ⚠️ As duas primeiras versoes destes movimentos CONTRADIZIAM o proprio
    # bloco de imagem, e nenhum linter pegou; so' apareceu lendo o render:
    #   · TAKE 02 dizia "right hand closed around the tall glass ... stirs the
    #     spoon", mas a IMAGE 02 poe a direita no SACHE e a esquerda apoiada na
    #     bancada. Duas maos em dois lugares diferentes no mesmo bloco: o Veo
    #     resolve trocando a mao no meio do take.
    #   · TAKE 03 dizia "taps it with her LEFT index finger", mas a IMAGE 03 poe
    #     a gelatina NA ESQUERDA e o indicador DIREITO apontando.
    # Contradicao entre IMAGE e TAKE e' pior que omissao: a omissao o gerador
    # preenche com o frame; a contradicao ele resolve mexendo no que estava
    # certo.
    mov = [
        "%(estavel)s She never moves the bottle away and never sets it "
        "down." % v,
        "She keeps her right hand closed around the sachet, her forearm "
        "resting steady on the %(sup)s, and tips it a little further so the "
        "pale powder keeps falling into the glass. Her left hand stays flat on "
        "the %(sup)s beside the glass. Everything else on the %(sup)s stays "
        "exactly as it appears in the first frame. %(nao_toca)s" % v,
        "She holds the bowl of gelatin cubes steady in her raised left hand "
        "beside her face the whole time, and her right index finger taps "
        "towards it twice as she speaks. The finished drink on the %(sup)s "
        "stays exactly as it appears in the first frame — nothing moves, "
        "nothing else is touched." % v,
    ]
    audio = ["%s, a soft pour. No music." % m["audio"],
             "%s, a spoon against glass. No music." % m["audio"],
             "%s. No music." % m["audio"]]

    # ⛔ O ELENCO MUDA ENTRE AS CENAS e a frase travada tem de acompanhar: a
    # cena 1 tem DOIS (ela + o colo dele), as cenas 2 e 3 tem ela sozinha.
    # ⚠️ Na cena 1 e' `only she speaks`, nunca `she is the only person`: afirmar
    # que ela e' a unica com um segundo corpo em quadro e' ordem contraditoria, e
    # o Veo resolve APAGANDO O HOMEM — justamente o personagem que da' ao hook o
    # dono do problema.
    elenco = ["He never speaks and his face never enters the frame; only she "
              "speaks.",
              "She is the only person in the shot.",
              "She is the only person in the shot."]
    for i in range(3):
        b["TAKE %02d/03" % (i + 1)] = (
            "Animate the provided image exactly. Handheld iPhone shot, very "
            "slight natural sway, no cuts. The %d-year-old woman speaks "
            "straight into the lens. %s %s\n"
            'Dialogue: "%s"\nAudio: %s'
            % (ref["idade"], mov[i], elenco[i], sonorizar(spec["falas"][i]),
               audio[i]))

    return sc.selar_takes(sc.selar_tags(b))


# ---------------------------------------------------------------------------
# LINTER
# ---------------------------------------------------------------------------

def lint(spec, blocos):
    ach = []
    falas = spec["falas"]
    m = spec["mundo"]

    sc.lint_tags(blocos, ach)
    sc.lint_sem_texto(blocos, ach)
    sc.lint_isca_cta(falas[2], ach, "a cena 3 (CTA)")
    sc.lint_cta_literal(falas[2], ach, "a cena 3 (CTA)")

    if not blocos.get("BLOCO 0 (REF)", "").lstrip().upper().startswith("REF"):
        ach.append(("ERRO", "BLOCO 0 sem o cabecalho REF — o AdBatch descarta a "
                            "referencia em silencio"))

    # --- tetos e pisos ------------------------------------------------------
    for i, f in enumerate(falas, 1):
        n = _palavras(f)
        if n > TETO_FALA[i]:
            ach.append(("ERRO", "CO9: cena %d com %d palavras (teto %d) — a "
                                "narracao passa de 7s" % (i, n, TETO_FALA[i])))
        if n < PISO_FALA[i]:
            ach.append(("AVISO", "CO9: cena %d com %d palavras (piso %d) — "
                                 "sobra silencio nos 8s" % (i, n, PISO_FALA[i])))

    # --- CO8: a promessa NUNCA anda sem o desmentido ------------------------
    # ⚠️ Regra de FUNCAO, nao de forma. A cena 1 faz uma alegacao forte de
    # performance sexual; ela so' e' aceitavel porque o video a derruba dois
    # segundos depois. Promessa sozinha e' o nosso video fazendo a alegacao.
    if "actually works" not in falas[0].lower():
        ach.append(("ERRO", "CO8: a cena 1 promete e nao desmente — a promessa "
                            "so' existe para ser derrubada na mesma respiracao"))

    # --- o prop e a substancia sao NOMEADOS na fala -------------------------
    # ⚠️ Ordem do operador: "seja direto na referencia do prop, sem drifting".
    if ("on your %s" % spec["prop"]["nome"]) not in falas[0]:
        ach.append(("ERRO", "CO10: a cena 1 nao diz `on your %s` — o prop em "
                            "cena tem de ser o prop na boca dela"
                    % spec["prop"]["nome"]))
    if spec["substancia"]["nome"] not in falas[0]:
        ach.append(("ERRO", "CO10: a cena 1 nao nomeia a substancia (%s) que "
                            "esta' sendo despejada em quadro"
                    % spec["substancia"]["nome"]))

    # --- o mecanismo ---------------------------------------------------------
    corpo = " ".join(falas).lower()
    if "gelatin trick" not in corpo:
        ach.append(("ERRO", "CO11: literal `gelatin trick` ausente — sem ele o "
                            "criativo deixa de ser congruente com a VSL"))
    if "gelatin trick" not in falas[1].lower():
        ach.append(("ERRO", "CO11: o `gelatin trick` tem de estar na CENA 2, "
                            "que e' a cena do mecanismo"))

    # --- cota do orgao -------------------------------------------------------
    cota = [i for i, f in enumerate(falas, 1)
            if any(o.lower() in f.lower() for o in NUCLEO)]
    if len(cota) < 2:
        ach.append(("ERRO", "CO12: cota do orgao %d/3 (minimo 2) — cenas sem "
                            "substantivo do nucleo: %s"
                    % (len(cota), [i for i in (1, 2, 3) if i not in cota])))
    if len(set(spec["orgaos"])) < 2:
        ach.append(("ERRO", "CO12: o mesmo orgao repetido no mesmo video"))

    # --- CO7: a ancora de continuidade nas cenas 2 e 3 ----------------------
    for nome in ("IMAGE 02/03", "IMAGE 03/03"):
        if ("the same %d-year-old" % spec["ref"]["idade"]
                not in blocos[nome].lower()):
            ach.append(("ERRO", "CO7: %s sem a ancora `The same N-year-old` — a "
                                "cena 1 e a 2 sao em ambientes DIFERENTES neste "
                                "agente, e e' ai' que o Veo troca de pessoa"
                        % nome))

    # --- CO13: o elenco da cena 1 sao DOIS, e ele nao tem rosto -------------
    # ⛔⛔ Esta regra existe porque eu ERREI a leitura da fonte e o operador
    # achou no render: as pernas do quadro sao de um SEGUNDO PERSONAGEM, um
    # homem cortado na cintura, e e' a mao dele que segura o prop. O motor
    # gerava a narradora com o prop entre as proprias pernas.
    # ⚠️ Cobrado dos DOIS lados, senao um refactor futuro derruba o homem de
    # novo em silencio: a cena 1 TEM de trazer o corte na cintura e NAO PODE
    # dizer que ela e' a unica pessoa; as cenas 2 e 3 TEM de dizer.
    # ⚠️ OS MARCADORES SAO OS DA TRAVADA VALIDADA (H5), nao os da versao antiga:
    # `cropped at the waist` e `no torso and no face` eram do texto que o
    # gerador barrava em 2 de cada 3 lotes. Linter que cobra a frase errada
    # reprova justamente o prompt que passou.
    i1 = blocos["IMAGE 01/03"]
    if "only his legs and his hands" not in i1:
        ach.append(("ERRO", "CO13: IMAGE 01/03 sem o recorte do homem — sem ele "
                            "o Veo poe o rosto e o tronco dele em quadro, e sao "
                            "dois blocos de 8s depois em que ele nao existe"))
    if "his head and upper body out of shot" not in i1:
        ach.append(("ERRO", "CO13: IMAGE 01/03 nao mantem a cabeca e o tronco "
                            "dele fora de quadro — rosto em quadro vira pessoa "
                            "para manter identica entre blocos"))
    # ⛔ OS TOKENS QUE O GERADOR BARROU, medidos prompt a prompt em 2026-08-03.
    # Guarda contra o proximo refactor reintroduzir a frase que ja' custou dois
    # lotes recusados.
    # ⚠️ Limite de palavra, nao substring: `lap` cru acusaria `overlapping` e
    # `collapsed`, e linter que reprova o que esta' certo nunca foi testado.
    for tok in ("lap", "thigh", "thighs", "knees apart", "between his knees",
                "cropped at the waist"):
        alvo = "%s %s" % (i1.lower(), blocos["TAKE 01/03"].lower())
        if re.search(r"\b%s\b" % tok, alvo):
            ach.append(("ERRO", "CO13: token banido nesta cena — %r foi medido "
                                "como recusa do gerador; o mesmo quadro se diz "
                                "com cadeira, joelho e enquadramento" % tok))
    if "only person" in i1 or "only person" in blocos["TAKE 01/03"]:
        ach.append(("ERRO", "CO13: a cena 1 declara pessoa UNICA e tem DUAS — "
                            "ordem contraditoria: o Veo resolve apagando o "
                            "homem, que e' o dono do problema"))
    for nome in ("IMAGE 02/03", "IMAGE 03/03", "TAKE 02/03", "TAKE 03/03"):
        if "only person" not in blocos[nome]:
            ach.append(("ERRO", "CO13: %s sem a trava de pessoa unica — o homem "
                                "so' existe na cena 1" % nome))
    if spec["homem"]["marca"] not in i1:
        ach.append(("ERRO", "CO13: o homem entrou sem ancora distintiva na mao "
                            "— ele nao tem rosto, entao a mao e a calca sao a "
                            "unica identidade que ele tem"))

    # --- CO5: a gelatina em cubos so' na cena 3 -----------------------------
    for nome in ("IMAGE 01/03", "IMAGE 02/03"):
        if "gelatin cubes" in blocos[nome]:
            ach.append(("ERRO", "CO5: gelatina em cubos fora da cena 3 (%s) — "
                                "entrega o payoff antes da promessa" % nome))
    if "gelatin cubes" not in blocos["IMAGE 03/03"]:
        ach.append(("ERRO", "CO5: a cena 3 tem de mostrar a gelatina em cubos "
                            "na mao — e' o objeto da keyword"))

    # --- CO2: nada cresce ----------------------------------------------------
    # ⚠️ Este agente NAO tem cena de crescimento: o bit visual e' o despejo. A
    # excecao e' vazia de proposito.
    sc.lint_nada_cresce(blocos, ach, rotulo="CO2")

    # --- P12: zero marca legivel (a excecao do EXTERIOR e' so' dele) --------
    for nome, txt in blocos.items():
        if nome.startswith("BLOCO"):
            continue
        for marca in ("arm & hammer", "great value", "kroger", "brand name",
                      "printed label", "logo"):
            if marca in txt.lower():
                ach.append(("ERRO", "P12: %s traz marca/rotulo legivel (%r) — a "
                                    "excecao da marca real e' nominal do "
                                    "EXTERIOR" % (nome, marca)))

    # --- a superficie do mundo e' a unica em cena ---------------------------
    junto = " ".join(v for k, v in blocos.items() if not k.startswith("BLOCO"))
    if m["sup"] != "counter" and re.search(r"\bcounter\b", junto):
        ach.append(("ERRO", "`counter` sobrou num mundo de %s (%s) — literal "
                            "esquecido no refactor" % (m["sup"], m["id"])))
    if re.search(r"\ba [aeiou]", junto):
        ach.append(("ERRO", "artigo errado: %r"
                    % re.search(r"\ba [aeiou]\w+", junto).group()))

    # ⛔⛔ TAKE CONTRA IMAGE — 2026-08-05. Este motor tem `lint()` proprio e NAO
    # passa pelo `lint_curto`, entao a lente compartilhada nao chegava aqui.
    # ⚠️ Foi assim que a primeira varredura deu "limpo" para sete motores: eles
    # nunca rodaram a lente. "Limpo" sem cobertura e' o pior resultado possivel,
    # porque parece verde. Medir a lente e' medir TAMBEM se ela e' chamada.
    # ⛔ PAINEL HONESTO — 2026-08-05. Nenhum eixo desenhado no painel pode
    # deixar de chegar ao video.
    sc.lint_painel_honesto(sys.modules[__name__], spec, blocos, ach)

    # ⛔ HIERARQUIA DO MECANISMO — diretriz do operador, 2026-08-06 (§31).
    # So dispara quando a cena 2 mostra preparo em quadro.
    sc.lint_hierarquia_mecanismo(spec, blocos, ach)

    sc.lint_take_vs_image(blocos, ach)

    return ach


# ---------------------------------------------------------------------------
# UI
# ---------------------------------------------------------------------------

def resumo_pt(spec):
    m = spec["mundo"]
    # ⚠️ A receita corta na VIRGULA, nao em 48 caracteres: o corte cego partia a
    # frase no meio ("in a ") e o operador lia um resumo truncado no painel.
    receita = spec["receita"].split(",")[0].lower()
    # ⚠️ O `(familia)` saiu: com os mundos por REGIAO o id E' a familia, e o
    # painel escrevia "em chicago (chicago)". Repetir a mesma palavra entre
    # parenteses nao informa nada — so' ensina o operador a ignorar o resumo.
    return ("Mulher %s de %d anos, de %s %s, em %s. Cena 1 sentada: "
            "despeja %s sobre %s no colo. Cenas 2 e 3 de pé na bancada: %s. "
            "Gelatina em cubos na mão no CTA."
            % (spec["etnia"], spec["ref"]["idade"], spec["cor"], spec["traje"][1],
               m["id"].replace("_", " "),
               spec["substancia"]["nome"], spec["prop"]["nome"], receita))


def nova_fala(spec, i, rng):
    """Re-sorteia a copy de UMA cena, ja' formatada com os slots deste video."""
    spec["falas_map"] = {j: f for j, f in enumerate(spec["falas"])}
    return _falas(spec, rng, quais=(i,))[i]


def _apos_mundo(spec, rng):
    """Trocou o MUNDO: etnia e cor tem de vir do mundo novo, senao o botao
    `trocar` deixa em cena a incongruencia que os MUNDOS existem para impedir."""
    if spec["etnia"] not in spec["mundo"]["etnias"]:
        spec["etnia"] = rng.choice(spec["mundo"]["etnias"])
    if spec["cor"] not in spec["mundo"]["cores"]:
        spec["cor"] = rng.choice(spec["mundo"]["cores"])


def _apos_prop(spec, rng):
    """Trocou o PROP ou a SUBSTANCIA: a cena 1 os NOMEIA (CO10), entao a fala
    tem de ser remontada — senao a boca fala de um objeto que nao esta' em cena."""
    spec["falas"][0] = nova_fala(spec, 0, rng)


def _apos_receita(spec, rng):
    """Trocou a RECEITA: ela E' a fala da cena 2."""
    spec["falas"][1] = nova_fala(spec, 1, rng)


EIXOS_QUE_MEXEM_NA_COPY = {
    "mundo": _apos_mundo,
    "prop": _apos_prop,
    "substancia": _apos_prop,
    "receita": _apos_receita,
}

TETO_LEDGER = {"familia_mundo": len(FAMILIAS_MUNDO), "prop": len(PROPS),
               "substancia": len(SUBSTANCIAS), "homem": len(HOMENS)}

MIN_OPCOES = 7          # piso por eixo visual


# ---------------------------------------------------------------------------
# AUTOTESTE
# ---------------------------------------------------------------------------

def autoteste(n=600):
    """As invariantes do agente, MEDIDAS, com controles positivos.

    ⚠️ Existe porque a licao §17 e' sempre a mesma: verificar a FORMA e declarar
    pronto sem verificar a FUNCAO. Pool bonito nao prova nada; o que prova e' o
    motor rodando 600 vezes e um sabotador confirmando que cada checagem SABE
    reprovar.
    """
    falhas = []
    vistos = collections.defaultdict(set)
    fam = collections.Counter()
    larguras = {1: [], 2: [], 3: []}

    for seed in range(n):
        spec = sortear("joe", random.Random(seed), {}, {})
        blocos = montar(spec)
        for tipo, msg in lint(spec, blocos):
            if tipo == "ERRO":
                falhas.append("seed %d (%s): %s" % (seed, spec["mundo"]["id"], msg))
        vistos["mundo"].add(spec["mundo"]["id"])
        vistos["etnia"].add(spec["etnia"])
        vistos["prop"].add(spec["prop"]["id"])
        vistos["substancia"].add(spec["substancia"]["id"])
        vistos["ref"].add(spec["ref"]["idade"])
        vistos["homem"].add(spec["homem"]["id"])
        fam[spec["mundo"]["familia"]] += 1
        for i, f in enumerate(spec["falas"], 1):
            larguras[i].append(_palavras(f))
        if spec["etnia"] not in spec["mundo"]["etnias"]:
            falhas.append("seed %d: etnia fora do mundo" % seed)

    # cobertura
    for eixo, pool in (("mundo", MUNDOS), ("prop", PROPS),
                       ("substancia", SUBSTANCIAS), ("homem", HOMENS)):
        if len(vistos[eixo]) != len(pool):
            falhas.append("%s: %d de %d nunca sorteados"
                          % (eixo, len(pool) - len(vistos[eixo]), len(pool)))
    for nome, pool in (("MUNDOS", MUNDOS), ("NARRADORAS", NARRADORAS),
                       ("PROPS", PROPS), ("SUBSTANCIAS", SUBSTANCIAS),
                      ("HOMENS", HOMENS),
                       ("RECEITAS", RECEITAS), ("ROTINAS", ROTINAS),
                       ("DESMENTIDOS", DESMENTIDOS),
                       ("ISCAS_PROMESSA", ISCAS_PROMESSA)):
        # ⚠️ PROPS tem piso PROPRIO de 5, e ele e' EMPIRICO: o pool e' o conjunto
        # dos props que PASSARAM no gerador em teste manual (2026-08-03), nao o
        # que cabe no piso generico. Completar com entradas nao testadas para
        # bater 7 foi exatamente o erro do lote anterior — dez no pool, quatro
        # reprovados em campo. ⛔ Quem quiser subir este piso sobe TESTANDO um
        # prop novo, uma geracao por entrada.
        piso = 5 if nome == "PROPS" else MIN_OPCOES
        if len(pool) < piso:
            falhas.append("eixo %s com %d opcoes (minimo %d)"
                          % (nome, len(pool), piso))
    # nenhuma familia domina
    for f, q in fam.items():
        if q > n * 0.25:
            falhas.append("familia %s levou %.1f%% do lote (teto 25%%)"
                          % (f, 100.0 * q / n))

    # ---- CONTROLES POSITIVOS ----------------------------------------------
    ctrl = []
    s = sortear("joe", random.Random(1), {}, {})
    b = montar(s)
    # [CO10] o prop na boca
    s2 = dict(s, falas=list(s["falas"]))
    s2["falas"][0] = s2["falas"][0].replace("on your %s" % s["prop"]["nome"],
                                            "on it")
    if not any("CO10" in msg for _, msg in lint(s2, b)):
        ctrl.append("[CO10] nao acusa a cena 1 sem nomear o prop")
    # [CO8] promessa sem desmentido
    s3 = dict(s, falas=list(s["falas"]))
    s3["falas"][0] = s3["falas"][0].replace("actually works", "great")
    if not any("CO8" in msg for _, msg in lint(s3, b)):
        ctrl.append("[CO8] nao acusa promessa sem desmentido")
    # [CO11] gelatin trick fora da cena 2
    s4 = dict(s, falas=list(s["falas"]))
    s4["falas"][1] = s4["falas"][1].replace("gelatin trick", "morning routine")
    if not any("CO11" in msg for _, msg in lint(s4, b)):
        ctrl.append("[CO11] nao acusa a cena 2 sem o `gelatin trick`")
    # [CO7] ancora removida
    b5 = dict(b)
    b5["IMAGE 02/03"] = b5["IMAGE 02/03"].replace(
        "the same %d-year-old" % s["ref"]["idade"], "a")
    if not any("CO7" in msg for _, msg in lint(s, b5)):
        ctrl.append("[CO7] nao acusa a cena 2 sem a ancora de continuidade")
    # [CO13] o homem apagado da cena 1 — o defeito que o operador achou
    b7 = dict(b)
    b7["IMAGE 01/03"] = b7["IMAGE 01/03"].replace("only his legs and his hands", "his whole body")
    if not any("CO13" in msg for _, msg in lint(s, b7)):
        ctrl.append("[CO13] nao acusa a cena 1 sem o corte na cintura")
    b8 = dict(b)
    b8["IMAGE 01/03"] += " She is the only person in the frame."
    if not any("CO13" in msg for _, msg in lint(s, b8)):
        ctrl.append("[CO13] nao acusa a cena 1 declarando pessoa unica com duas")
    b9 = dict(b)
    b9["IMAGE 02/03"] = b9["IMAGE 02/03"].replace("only person", "main person")
    if not any("CO13" in msg for _, msg in lint(s, b9)):
        ctrl.append("[CO13] nao acusa a cena 2 sem a trava de pessoa unica")
    # [CO5] gelatina adiantada
    b6 = dict(b)
    b6["IMAGE 01/03"] += " " + CO_GELATINA
    if not any("CO5" in msg for _, msg in lint(s, b6)):
        ctrl.append("[CO5] nao acusa gelatina fora da cena 3")
    # e o lote limpo NAO pode ser acusado
    if [m for t, m in lint(s, b) if t == "ERRO"]:
        ctrl.append("o lote limpo esta' sendo reprovado — regra que reprova "
                    "tudo nunca foi testada")

    print("MUNDOS %d em %d familias | NARRADORAS %d | PROPS %d | SUBSTANCIAS %d"
          % (len(MUNDOS), len(FAMILIAS_MUNDO), len(NARRADORAS), len(PROPS),
             len(SUBSTANCIAS)))
    print("%d videos | mundos vistos %d/%d | etnias %d | props %d | iscas %d"
          % (n, len(vistos["mundo"]), len(MUNDOS), len(vistos["etnia"]),
             len(vistos["prop"]), len(vistos["substancia"])))
    print("familia mais frequente: %s com %.1f%%"
          % (fam.most_common(1)[0][0], 100.0 * fam.most_common(1)[0][1] / n))
    for i in (1, 2, 3):
        L = larguras[i]
        print("  cena %d: %d–%d palavras (media %.1f) | piso %d teto %d | %.2f p/s"
              % (i, min(L), max(L), sum(L) / float(len(L)), PISO_FALA[i],
                 TETO_FALA[i], sum(L) / float(len(L)) / 8))
    print("  video: media %.1f palavras"
          % (sum(sum(larguras[i]) for i in (1, 2, 3)) / float(n)))

    if ctrl:
        # ⚠️ Marcador ASCII de proposito: o console do Windows e' cp1252 e o
        # `⛔` levanta UnicodeEncodeError. Como esta linha so' e' impressa
        # QUANDO HA' FALHA, o crash acontecia exatamente na hora em que o
        # relatorio importa — bug irmao no clean_short_v2, corrigido junto.
        print("\n>> O AUTOTESTE ESTA' CEGO:")
        for c in ctrl:
            print("   %s" % c)
    if falhas:
        print("\n>> %d FALHA(S):" % len(falhas))
        for f in falhas[:20]:
            print("   %s" % f)
    if not falhas and not ctrl:
        print("\nAUTOTESTE OK — e os controles positivos reprovam quando devem.")
    return 1 if (falhas or ctrl) else 0


def main():
    ap = argparse.ArgumentParser(description="Randomizador do agente COLO SHORT")
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
                              ("homem", spec["homem"]["id"]),
                              ("substancia", spec["substancia"]["id"])):
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
