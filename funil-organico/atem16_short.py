#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE ATEM 16 — 3 takes de 8s (24s), destino AdBatch **Vertical 3**.

⭐⭐ O PRIMEIRO AGENTE DO PARQUE EM ALEMAO, E O PRIMEIRO FORA DO NICHO DE ED
E DE EMAGRECIMENTO. Vende um INFOPRODUTO: `Begin To Breathe`, curso de
breathwork de Corrina Holzner (Beamdream Breathworks), 147 EUR.

⭐ A GRAMATICA DE CENA E' A DO PEE 16, por ordem do operador (*"irei usar a
copy visual do agente pee16 de referencia"*). O que atravessa literalmente:
  · a MANCHA em publico numa roupa CLARA, com a plateia rindo E apontando;
  · a vitima CHORANDO, cabeca baixa, sem nunca falar e sem olhar a lente;
  · o dedo da narradora apontando a MANCHA NO TECIDO — nunca a virilha, nunca
    encostando na outra pessoa (PE3, a construcao que o FLAGRANTE tomou como
    precedente depois das 4 recusas por agencia);
  · o modelo anatomico de ensino erguido para a lente na cena do mecanismo
    (D1 do PEE/FLAGRANTE, validado em render).
⛔ O ELENCO INTEIRO E' FEMININO, por ordem do operador: a vitima e' mulher e
quem narra e' mulher. `SEXOS = ("mulher",)`.

⛔⛔ A CAUSA DA MANCHA — E ESTA E' A UNICA DECISAO EM QUE EU NAO SEGUI O
BRIEFING AO PE DA LETRA, COM O MOTIVO ESCRITO.
O operador pediu *"a mulher tera mijado por conta de ataque de ansiedade"*. A
pagina de vendas do proprio produto EXCLUI essa pessoa, por escrito, em dois
lugares:
    "Nicht der richtige Moment, wenn... du gerade in einer akuten psychischen
     Krise bist — bitte such dir zuerst professionelle Unterstuetzung"
    "...bei [...] Trauma, psychischen Erkrankungen, PANIKATTACKEN [...] vorher
     mit deinem Arzt oder deiner Aerztin sprechen"
Vender "voce teve um ataque de panico, este curso resolve" e' vender contra a
contraindicacao declarada do produtor. Tres custos, todos reais e todos do
operador: refund alto, o produtor derrubando o afiliado, e a Alemanha e' o
mercado mais duro do mundo em alegacao de saude (HWG).
⭐ O CONSERTO NAO TIRA UMA VIRGULA DA CENA. A mancha, a plateia, o choro e o
dedo ficam intactos. O que muda e' a MOLDURA:
    causa    -> o sistema nervoso preso em alarme  (a propria pagina vende
                breathwork como *"eine der direktesten Verbindungen zu deinem
                Nervensystem"*)
    promessa -> regulacao em minutos               (bullet literal da pagina:
                *"dich in stressigen Momenten in Minuten regulieren"*)
⛔ Nenhuma das duas e' invencao minha: as duas sao copy da pagina do produto.
⚠️ REVERSIVEL EM UM POOL. Se o operador quiser o ataque de panico nominal, o
que muda e' `HOOKS` + `MECANISMOS` e mais nada — a lente `AT9` e' que os
proibe hoje, e desliga-la e' uma linha. A decisao e' dele (regra de alcada).

⭐⭐ O MECANISMO UNICO E' `Freemor Breathing®`, E ELE E' O MELHOR ATIVO DESTA
OFERTA. A pagina crava que e' *"die einzige Atemtechnik dieser Art im
deutschsprachigen Raum"* — respiracao consciente combinada com TREMOR
NEUROGENICO. Mecanismo proprietario, com nome, que o espectador NAO acha no
YouTube; a propria FAQ da pagina diz isso em resposta a `Kann ich das auch auf
YouTube finden?`. E' o equivalente exato do `gelatin trick` no resto do parque,
e a lente `AT5` cobra o literal no take 3.

⛔⛔ A LINGUA — O QUE E' ALEMAO E O QUE NAO E'.
    direcao de cena  -> INGLES  (os 33 motores fazem assim; o Veo desenha
                                 muito melhor a partir de ingles)
    linha Dialogue:  -> ALEMAO
    bloco Voice:     -> declara alema NATIVA, senao o TTS le' alemao com
                        sotaque ingles e o avatar nao se reconhece
⚠️ A legenda queimada nasce do Whisper rodando sobre o AUDIO, e o Veo Editor
ja' tem `Idioma: Alemao` no rodape — nao ha' nada a fazer do lado da legenda
alem de selecionar isso na hora de montar o lote.

⭐⭐ O TETO DE FALA E' EM SILABAS, E ESTE MOTOR E' O PRIMEIRO DO PARQUE ASSIM.
Todo motor daqui conta PALAVRAS porque em ingles as duas medidas andam juntas
(~1,4 silabas por palavra). Alemao tem ~1,7, e substantivo composto e' pior:
`Nervensystem` e' UMA palavra e QUATRO silabas. Um teto de 25 palavras em
alemao autoriza uma fala que nao cabe em 8 segundos, e fala que nao cabe sai
CORTADA no render sem ninguem ver — o modo de falha do §27 das licoes.
⛔ A unidade fisica e' a silaba: 8s a ~4,4 silabas/s = 35. O teto de palavras
fica como rede secundaria (20), nao como medida.
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
LEDGER = os.path.join(AQUI, ".atem-16-ledger.json")

TITULO = "AGENTE ATEM 16"
SLUG = "atem-16"
SUBTITULO = ("3 takes de 8s = 24 segundos · a mancha publica, o alarme que a "
             "causou, e o Freemor Breathing")

CENAS_UI = ["1 · A MANCHA", "2 · O ALARME", "3 · O METODO + CTA"]

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
TETO_SILABAS = 35
# ⚠️ 24, nao 20. A rede de palavras acusava falas de 21-22 palavras que o
# teto de SILABAS aprovava com folga (31 de 35) — e gate que acusa copy
# certa treina o operador a ignorar o gate. Ela existe so' para o caso
# patologico (muita monossilaba), nao para medir fala: quem mede e' a
# silaba.
TETO_PALAVRAS = 24
TETO_FALA = {1: TETO_PALAVRAS, 2: TETO_PALAVRAS, 3: TETO_PALAVRAS}

# ⛔⛔ A KEYWORD DO CTA. Nasce em `ATEM` — alema, curta, digitavel por qualquer
# um, e diz o produto. ⚠️ Ela TEM de estar cadastrada na automacao de DM antes
# do primeiro lote: comentario que entra sem keyword cadastrada e' mensagem que
# nao sai, que e' o preco ja' pago por `book`, `yes` e `horse` neste repo.
# ⭐ Editavel no campo de keyword da UI do Veo Editor, mesma mecanica do
# `gelahorse16`.
KEYWORD = "ATEM"

# ⭐ A ETNIA continua sendo o eixo de congruencia do repo (etnia do REF = etnia
# do avatar da pagina), so' que o mercado agora e' de lingua alema.
# ⏳ DIVIDA DECLARADA: o operador ainda nao passou as paginas deste funil. As
# chaves abaixo sao PROVISORIAS e existem para a UI ter o que desenhar — trocar
# pelos nomes reais quando as paginas nascerem.
ETNIA = {
    # ⭐ A PRIMEIRA PAGINA REAL deste funil (2026-09-01):
    #   facebook.com/profile.php?id=100091860330551
    # ⚠️ Ela nasceu com outro nome e outro assunto ("Kim Giang", capa de loja
    # de roupa, categoria Cidade) e esta' sendo reaproveitada. A chave e' `kim`
    # ate' o operador conseguir renomea-la; trocar a chave depois e' uma linha,
    # e o ledger nao depende dela.
    # ⛔ `white German` porque a CONGRUENCIA do repo e' etnia do REF = etnia do
    # AVATAR da pagina, e todos os 12 REFs deste motor sao alemas brancas. Se o
    # avatar mudar de etnia, esta linha muda junto — nunca uma sem a outra.
    "kim": "white German",
    # ⏳ provisorias, para a UI ter mais de uma opcao enquanto as outras paginas
    # nao nascem.
    "anna": "white German", "lena": "white German", "sofie": "white German",
    "derya": "Turkish German", "esra": "Turkish German",
}


# ===========================================================================
# STRINGS TRAVADAS — a gramatica de cena. NAO REESCREVER, NAO COMPRIMIR.
# ===========================================================================

# ⛔⛔ PE2 do PEE 16, copiado com o elenco trocado. O choro nao e' decoracao:
# e' o que transforma a mancha de PIADA em RUINA. Sem ele o video vira comedia
# e o espectador ri em vez de se reconhecer.
CHORO_IMAGE = (
    "head bowed, chin toward her chest, looking down at herself, crying hard — "
    "tears running down both cheeks, eyes red and squeezed shut, mouth twisted "
    "down, shoulders shaking. Both hands frozen at her sides."
)
CHORO_TAKE = (
    "she keeps crying, her shoulders shaking once with a sob, tears still on "
    "her cheeks, and she does not look up. She never speaks and never looks at "
    "the camera."
)

# ⛔⛔ PE3 — O DEDO APONTA A MANCHA NO TECIDO, NUNCA O CORPO, E NUNCA ENCOSTA.
# Roupa e' ancora segura. Esta construcao exata e' a que o FLAGRANTE adotou
# depois de QUATRO recusas por agencia, e ela e' o motivo de este angulo passar
# na moderacao enquanto o mesmo beat descrito de outro jeito nao passa.
NARRADORA_IMAGE = (
    "crouched on one knee beside her, right arm extended, index finger "
    "pointing directly at the stain on the fabric, not touching her, face "
    "turned toward the camera, mouth open mid-word"
)
NARRADORA_TAKE = (
    "The crouching woman speaks calmly to camera, her pointing finger stays on "
    "the stain on the fabric and never touches the other woman. Neither woman "
    "changes position."
)

# ⛔ PE4 — a plateia RI E APONTA. Sem terceiro em quadro, humilhacao publica
# vira acidente privado, e o angulo inteiro morre.
# ⭐ O substantivo e' PARAMETRO, nunca cravado: pedir `shoppers` num Bahnsteig
# poe compradores de supermercado numa plataforma de trem, e contradicao dentro
# do prompt o gerador resolve inventando um terceiro cenario. Licao do PEE.
PLATEIA_IMAGE = (
    "four blurred %s standing behind them, hands over their mouths mid-laugh, "
    "two of them pointing at her, clearly mocking her"
)

# ⛔⛔ RISADA NUNCA ENTRA NO AUDIO. O Veo sincroniza ROSTO com AUDIO — pista
# sonora de riso faz TODA cara em quadro rir, inclusive a que o texto manda
# estar em lagrimas. O operador pegou isto no FLAGRANTE 16 com o render na mao.
# ⭐ Nao faz falta nenhuma: a plateia continua rindo NA IMAGEM.
# ⛔⛔ E ELE E' POSITIVO. A primeira versao dizia "No laughter, no music."
# — e a propria lente AT11 a acusou. O falso positivo era o sintoma; a
# doenca e' que `No laughter` E' UMA NEGACAO, e negacao injeta o token,
# que e' a licao do `not a celebrity` escrita vinte linhas acima e
# cometida aqui mesmo assim. O audio diz o que EXISTE.
# ⚠️ `No music.` fica: e' o padrao dos 33 motores do parque, e troca-lo e'
# decisao de parque, nao deste arquivo.
AUDIO_MANCHA = ("Audio: room tone, distant footsteps and the shuffle of "
                "people moving past, only. No music.")

# ⭐ D1 do PEE/FLAGRANTE, com o orgao trocado pelo que ESTE angulo explica.
# ⛔ Por que um modelo anatomico e nao uma metafora nova (mola tensionada, elastico
# esticado): esta construcao — objeto do tamanho da mao, erguido, face virada
# para a lente, dedo apontando — tem validacao de render em DOIS motores. Uma
# metafora inedita nao tem. Prop novo e' hipotese, e hipotese se testa depois de
# o angulo ter linha de base.
D1_IMAGE = (
    "In her left hand she holds up toward the camera a hand-sized medical "
    "teaching model of the human nervous system — a flat-backed slab of molded "
    "plastic showing the spinal cord and the nerve branches fanning out from "
    "it, painted in cream, pale yellow and muted red the way a physiotherapy "
    "office display shows them, the whole model turned so its face is squared "
    "to the lens. Her right index finger points at the model."
)
D1_TAKE = (
    "She holds the plastic teaching model steady in her left hand and taps its "
    "face twice with her right index finger as she explains. The model stays "
    "squared to the camera and does not turn or tilt."
)

# ⭐⭐ O ATEMPLATZ — e ele e' copy da propria pagina do produto, nao invencao:
# *"Im Kurs erfaehrst du, wie du dir deinen persoenlichen 'Atemplatz'
# einrichten kannst"*. Usar o objeto que o curso ENSINA a montar como cenario
# do payoff e' congruencia de graca.
# ⛔ As duas maos (uma no peito, uma na barriga) sao a unica pose que diz
# "respiracao" sem uma palavra — e' o bit visual que faz o take 3 funcionar no
# mudo.
ATEMPLATZ_POSE = (
    "sitting upright and cross-legged on a low cushion, her left hand flat on "
    "her chest and her right hand flat on her belly, shoulders down and loose, "
    "eyes open and looking straight into the lens"
)

# ⛔⛔ SEM APARELHO EM QUADRO, E SEM DIZER QUE NAO HA'. Licao paga com um lote
# inteiro no VICK 16: o prompt dizia `with the phone in his free hand` e o
# gerador DESENHOU o telefone. E `no phone in frame` e' pior ainda — negacao
# injeta o token, que e' a mesma mecanica do `not a celebrity`.
# ⭐ A defesa e' positiva: as duas maos dela tem destino declarado em todos os
# tres quadros. Mao com tarefa nao segura telefone.

# ⛔ LAPIDE — `not a celebrity` NUNCA ENTROU AQUI, e nao pode entrar.
# A varredura de 2026-08-14 tirou a clausula de 30 arquivos e 112 strings. Quem
# faz o trabalho e' a ARQUITETURA FACIAL de cada entrada de `REFS`/`VITIMAS`:
# rosto especifico nao tem para onde derivar; rosto generico deriva para a
# media do treino, e a media tem nome.


# ===========================================================================
# POOLS DE CENA
# ===========================================================================

# ⭐ Lugares publicos do mundo de lingua alema. Cada entrada carrega o
# substantivo da PLATEIA (que o PLATEIA_IMAGE consome) e o locativo ALEMAO que
# a copy consome — os dois tem de descrever a MESMA gente no MESMO lugar.
LOCAIS = [
    {"id": "supermarkt", "plateia": "shoppers", "evento": "im Supermarkt",
     "cenario": "a busy supermarket aisle with tall shelves of packaged goods"},
    {"id": "kasse", "plateia": "customers", "evento": "an der Kasse",
     "cenario": "a supermarket checkout queue with a conveyor belt and a lit "
                "register display"},
    {"id": "apotheke", "plateia": "customers", "evento": "in der Apotheke",
     "cenario": "a pharmacy sales floor with white counters and shelves of "
                "boxes behind glass"},
    {"id": "bahnsteig", "plateia": "commuters", "evento": "auf dem Bahnsteig",
     "cenario": "a covered commuter train platform with a yellow edge line and "
                "an overhead departure board"},
    {"id": "wartezimmer", "plateia": "waiting patients",
     "evento": "im Wartezimmer",
     "cenario": "a doctors waiting room with a row of linked chairs and a "
                "magazine table"},
    {"id": "baeckerei", "plateia": "customers", "evento": "in der Baeckerei",
     "cenario": "a bakery counter queue with trays of bread rolls behind glass"},
    {"id": "buero", "plateia": "colleagues", "evento": "im Buero",
     "cenario": "an open plan office with desks, monitors and a glass meeting "
                "room behind"},
    {"id": "elternabend", "plateia": "parents", "evento": "beim Elternabend",
     "cenario": "a school classroom set up for a parents evening, adults on "
                "small chairs in a half circle"},
    {"id": "bus", "plateia": "passengers", "evento": "im Bus",
     "cenario": "the aisle of a city bus with grab poles and window seats"},
    {"id": "wochenmarkt", "plateia": "shoppers", "evento": "auf dem Wochenmarkt",
     "cenario": "an open air farmers market lane between produce stalls under "
                "canvas awnings"},
    {"id": "amt", "plateia": "people waiting", "evento": "auf dem Amt",
     "cenario": "a municipal office waiting hall with a numbered ticket display "
                "and rows of chairs"},
    {"id": "fitnessstudio", "plateia": "gym members", "evento": "im Fitnessstudio",
     "cenario": "a gym floor with treadmills and a rack of dumbbells along a "
                "mirrored wall"},
    {"id": "hochzeit", "plateia": "wedding guests", "evento": "auf der Hochzeit",
     "cenario": "a wedding reception hall with round tables, white cloths and "
                "string lights overhead"},
    {"id": "flughafen", "plateia": "travellers", "evento": "am Flughafen",
     "cenario": "an airport departure gate with a row of seats and a wall of "
                "windows onto the apron"},
    {"id": "restaurant", "plateia": "diners", "evento": "im Restaurant",
     "cenario": "a busy restaurant dining room with set tables and a service "
                "station along one wall"},
]

# ⛔ PE1 — A ROUPA E' SEMPRE CLARA. Numa calca escura a mancha nao le', e sem
# mancha legivel nao ha' angulo. Esta e' a unica trava de figurino do motor, e
# a lente `AT2` a cobra por lista, nao por adjetivo.
ROUPAS = [
    {"peca": "light grey cotton trousers"},
    {"peca": "pale beige chinos"},
    {"peca": "cream linen trousers"},
    {"peca": "light blue jeans"},
    {"peca": "pale pink cotton trousers"},
    {"peca": "sand coloured wide leg trousers"},
    {"peca": "pale khaki trousers"},
    {"peca": "off white summer trousers"},
    {"peca": "light grey jogging bottoms"},
    {"peca": "pale lilac cotton trousers"},
    {"peca": "light stone coloured work trousers"},
    {"peca": "washed out light denim trousers"},
]

# ⭐ A mancha em si. Varia a FORMA e o ESTAGIO, nunca o fato.
MANCHA = [
    "a dark wet patch spread across the front of the fabric and running down "
    "the inside of both thighs",
    "a large dark wet stain soaked through the front of the fabric, the edge "
    "of it still spreading down one leg",
    "the fabric soaked dark from the hip down to the knee on one side, the wet "
    "edge clearly outlined against the dry cloth",
    "a wide dark wet patch across the seat and front of the fabric, with a thin "
    "wet trail running down to the ankle",
    "the front of the fabric darkened and clinging wet, a small pool of liquid "
    "on the floor between her shoes",
]

# ⭐⭐ AS NARRADORAS — o arquetipo da coach do curso, com ROSTO ORIGINAL.
# ⛔⛔ O OPERADOR PEDIU EXPLICITAMENTE "ALGUEM PARECIDA", NAO ELA. Usar o rosto
# da produtora real seria gerar video sintetico de pessoa identificavel dizendo
# frases que ela nunca disse, dentro de uma cena de incontinencia. O arquetipo
# atravessa (mulher 30-45, cabelo claro, franja, ambiente de madeira, luz
# quente); o rosto e' construido aqui.
# ⛔ CADA ENTRADA CARREGA ARQUITETURA FACIAL — testa, orbita, ponte do nariz,
# maxilar, malar, orelha, sinal. E' isso, e nao nenhuma negacao, que impede o
# rosto de derivar para a media do treino.
# ⚠️ EXCECAO DECLARADA A LEI DO REF (20-35 anos, registro de beleza). Aqui a
# faixa e' 32-46 e o registro e' de PROFESSORA, nao de aspiracao: quem vende um
# curso de 147 EUR precisa parecer que da' aula ha' anos. Reverter e' trocar a
# autoridade pela beleza, e neste angulo a autoridade e' a oferta.
REFS = [
    {"id": "franja_reta", "idade": 38,
     "rotulo": "38a · loira escura com franja reta",
     "cabelo": "dark blonde hair worn loose to the collarbone with a blunt "
               "fringe cut level with the brow",
     "desc": "a broad flat forehead, deep-set grey green eyes under straight "
             "low brows, a narrow straight nose bridge with a rounded tip, a "
             "soft square jaw, high flat cheekbones, small attached earlobes, "
             "and a pale freckle just above the left brow"},
    {"id": "risca_meio", "idade": 41,
     "rotulo": "41a · castanho claro com risca ao meio",
     "cabelo": "light brown hair parted in the middle and falling straight "
               "past the shoulders",
     "desc": "a high rounded forehead, wide-set warm brown eyes with a slight "
             "downward tilt at the outer corner, a long nose bridge with a "
             "faint dip, a narrow tapering jaw, prominent rounded cheekbones, "
             "detached earlobes, and a small raised mole on the right jawline"},
    {"id": "coque_baixo", "idade": 44,
     "rotulo": "44a · grisalho claro em coque baixo",
     "cabelo": "ash blonde hair going silver at the temples, gathered in a low "
               "loose bun with strands escaping at the sides",
     "desc": "a narrow forehead with a widows peak, close-set pale blue eyes "
             "under thin arched brows, a short straight nose bridge, a "
             "prominent pointed chin, flat wide cheekbones, and a vertical "
             "crease between the brows that stays even when she is relaxed"},
    {"id": "ondulado_curto", "idade": 35,
     "rotulo": "35a · ondulado curto castanho",
     "cabelo": "mid brown wavy hair cut short to the jaw and tucked behind "
               "one ear",
     "desc": "a square forehead, large round dark brown eyes set far apart, a "
             "wide flat nose bridge with a broad tip, a strong angular jaw, "
             "high sharp cheekbones, a pierced left ear with one small gold "
             "stud, and a scatter of freckles across both cheeks"},
    {"id": "trenca_lateral", "idade": 33,
     "rotulo": "33a · trança lateral ruiva",
     "cabelo": "copper red hair in a loose side braid pulled over one shoulder",
     "desc": "a low forehead, almond hazel eyes under heavy straight brows, a "
             "slim nose bridge with a slightly upturned tip, a rounded soft "
             "jaw, subtle cheekbones, small close-set ears, and dense freckles "
             "straight across the nose bridge"},
    {"id": "rabo_alto", "idade": 36,
     "rotulo": "36a · rabo de cavalo alto castanho escuro",
     "cabelo": "dark brown hair pulled back into a high smooth ponytail",
     "desc": "a tall forehead, deep-set dark eyes under thick straight brows, "
             "a long narrow nose bridge with a small bump at the top, a broad "
             "square jaw, high tight cheekbones, attached earlobes, and a "
             "small scar through the outer end of the right eyebrow"},
    {"id": "franja_lateral", "idade": 42,
     "rotulo": "42a · franja lateral loira",
     "cabelo": "warm blonde hair to the shoulders with a long side swept "
               "fringe falling across the right brow",
     "desc": "a rounded forehead, round grey eyes under short arched brows, a "
             "short wide nose bridge with a rounded tip, a soft oval jaw with "
             "a shallow dimple in the chin, full low cheekbones, and a pale "
             "birthmark on the left side of the neck"},
    {"id": "cacheado_solto", "idade": 39,
     "rotulo": "39a · cacheado solto castanho",
     "cabelo": "dark curly hair worn loose and full to just below the "
               "shoulders",
     "desc": "a broad forehead with a low hairline, wide dark eyes under full "
             "curved brows, a straight medium nose bridge with a slightly "
             "flared base, a rounded jaw, wide high cheekbones, detached "
             "earlobes, and a small mole below the right corner of the mouth"},
    {"id": "liso_longo", "idade": 34,
     "rotulo": "34a · liso longo castanho claro",
     "cabelo": "light chestnut hair worn dead straight and long past the "
               "shoulder blades",
     "desc": "a narrow high forehead, oval green eyes set close under fine "
             "straight brows, a very narrow nose bridge with a fine pointed "
             "tip, a tapering jaw with a sharp chin, delicate cheekbones, and "
             "a single small stud in each earlobe"},
    {"id": "pixie_prata", "idade": 46,
     "rotulo": "46a · pixie prateado",
     "cabelo": "silver grey hair cut in a short pixie crop swept back off the "
               "forehead",
     "desc": "a wide flat forehead, hooded blue grey eyes under sparse "
             "straight brows, a strong straight nose bridge with a squared "
             "tip, a square jaw with a broad chin, angular cheekbones, large "
             "detached earlobes, and deep lines from the nose to the mouth "
             "corners"},
    {"id": "meio_preso", "idade": 37,
     "rotulo": "37a · meio preso castanho médio",
     "cabelo": "mid brown hair with the top half pinned back and the rest "
               "falling loose to the shoulders",
     "desc": "a rounded forehead, wide amber eyes under straight medium brows, "
             "a medium nose bridge with a rounded tip and a small crease "
             "across it, a soft square jaw, medium cheekbones, attached "
             "earlobes, and a faint pale scar on the left cheek"},
    {"id": "franja_cortina", "idade": 40,
     "rotulo": "40a · franja cortina loira escura",
     "cabelo": "dark blonde hair with a centre parted curtain fringe framing "
               "both sides of the face, the rest tied back",
     "desc": "a high broad forehead, deep-set brown eyes under thick low "
             "brows, a long straight nose bridge, a narrow jaw with a pointed "
             "chin, prominent angular cheekbones, small attached earlobes, and "
             "a raised beauty spot high on the left cheek ridge"},
]

# ⭐ AS VITIMAS — quem se molha. Mulheres comuns, 29-52, e cada uma com
# arquitetura facial propria pelo mesmo motivo das REFS.
# ⛔ ELA NUNCA FALA e nunca olha a lente (CHORO_TAKE). A voz do video e' da
# narradora nos tres takes, inclusive no take 1, onde ela esta' agachada ao
# lado — e' isso que transforma o acidente em testemunho.
VITIMAS = [
    {"id": "coque_desfeito", "idade": 34,
     "rotulo": "34a · coque desfeito",
     "desc": "a round face with a low forehead, small close-set brown eyes, a "
             "short wide nose bridge, a soft rounded jaw, and dark hair "
             "escaping from a bun that has half come loose"},
    {"id": "bob_liso", "idade": 41,
     "rotulo": "41a · chanel liso",
     "desc": "a long face with a high forehead, wide-set grey eyes, a long "
             "narrow nose bridge, a tapering jaw, and straight mid brown hair "
             "cut in a blunt bob level with the jaw"},
    {"id": "rabo_baixo", "idade": 29,
     "rotulo": "29a · rabo de cavalo baixo",
     "desc": "an oval face with a rounded forehead, large dark eyes under full "
             "brows, a straight medium nose bridge, a soft chin, and black "
             "hair pulled into a low ponytail"},
    {"id": "grisalho_curto", "idade": 52,
     "rotulo": "52a · curto grisalho",
     "desc": "a square face with a broad forehead, hooded pale eyes, a strong "
             "nose bridge with a small bump, a heavy square jaw, and short "
             "grey hair combed back flat"},
    {"id": "cacho_preso", "idade": 37,
     "rotulo": "37a · cachos presos",
     "desc": "a heart shaped face with a wide forehead, round brown eyes, a "
             "broad nose bridge with a flared base, a pointed chin, and dense "
             "dark curls gathered high on the head"},
    {"id": "trenca_longa", "idade": 46,
     "rotulo": "46a · trança longa",
     "desc": "a narrow face with deep-set green eyes, thin arched brows, a fine "
             "nose bridge, a sharp jaw, and long light brown hair in a single "
             "braid down the back"},
    {"id": "franja_pesada", "idade": 31,
     "rotulo": "31a · franja pesada",
     "desc": "a round face with small hazel eyes set close together, a short "
             "upturned nose, full cheeks, a soft chin, and dark red hair with "
             "a heavy fringe cut straight across the brow"},
    {"id": "solto_ondulado", "idade": 44,
     "rotulo": "44a · solto ondulado",
     "desc": "an oval face with a medium forehead, wide brown eyes with lines "
             "at the outer corners, a straight nose bridge, a rounded jaw, and "
             "shoulder length wavy brown hair worn loose"},
]

# ⭐ O ATEMPLATZ do take 3 — onde a narradora fecha. Todos interiores calmos,
# com a madeira e a luz quente do universo visual do produto.
AMBIENTES = [
    {"id": "estudio_madeira",
     "set": "a small breathwork studio with pale wood panelled walls, a folded "
            "wool blanket on the floor and a single potted plant in the corner",
     "luz": "warm late afternoon daylight from a tall window on the left"},
    {"id": "sotao",
     "set": "a converted attic room with a sloping white ceiling, exposed pine "
            "beams and a low bookshelf against the knee wall",
     "luz": "soft diffuse daylight from a roof window overhead"},
    {"id": "sala_tapete",
     "set": "a plain living room corner with a thick woven rug, a low wooden "
            "stool and a linen curtain drawn half across the window",
     "luz": "warm morning light falling in a band across the rug"},
    {"id": "varanda_envidracada",
     "set": "a glazed balcony room with wooden flooring, hanging plants and a "
            "view of bare tree tops through the glass",
     "luz": "flat bright overcast daylight through the glass"},
    {"id": "quarto_claro",
     "set": "a light bedroom corner with a made bed out of focus behind, a "
            "folded blanket and a small brass bowl on the floor",
     "luz": "low golden light from a lamp on the floor beside her"},
    {"id": "cabana",
     "set": "a wooden cabin room with visible log walls, a wool throw over a "
            "bench and a cast iron stove in the background",
     "luz": "warm firelight from one side and cool daylight from a small "
            "window on the other"},
    {"id": "sala_branca",
     "set": "a bare white walled practice room with a wide plank floor and a "
            "single stack of folded blankets against the wall",
     "luz": "even soft daylight from a large window behind the camera"},
    {"id": "jardim_inverno",
     "set": "a winter garden room with a tiled floor, tall leafy plants and "
            "white framed windows on two sides",
     "luz": "bright filtered daylight through the leaves"},
    {"id": "sotao_pedra",
     "set": "a renovated stone walled room with a rough plaster ceiling, a "
            "wide floor cushion and a wooden crate used as a side table",
     "luz": "warm directional light from a floor lamp behind the camera"},
    {"id": "estudio_espelho",
     "set": "a small studio with one mirrored wall, a wooden floor and a row "
            "of rolled mats stacked along the skirting",
     "luz": "cool even daylight from a skylight"},
]

# ⭐ O que ela veste no take 2 e no take 3 — registro de professora, nunca de
# aspiracao. Roupa que se pode sentar no chao com ela.
TRAJES = [
    "a soft oatmeal knit jumper and wide dark linen trousers",
    "a plain white long sleeved top and loose grey trousers",
    "a rust coloured ribbed cardigan over a black vest top and dark leggings",
    "a sage green loose linen shirt and cream trousers",
    "a charcoal wrap top and soft wide black trousers",
    "a cream cotton sweatshirt and dark green loose trousers",
    "a mustard fine knit jumper and black straight trousers",
    "a navy long sleeved cotton top and pale grey wide trousers",
]


# ===========================================================================
# POOLS DE COPY — ALEMAO
# ===========================================================================
# ⛔⛔ COPY E' ALCADA DO OPERADOR. Estas entradas sao PROPOSTA e precisam do
# carimbo dele antes do primeiro lote. Cada uma respeita, por construcao:
#   · o teto de 35 SILABAS (medido pelo autoteste, nao estimado);
#   · a moldura declarada na docstring (alarme / regulacao, nunca ataque de
#     panico e nunca cura);
#   · a lente `AT4` — nenhuma fala ENSINA o padrao respiratorio. A tecnica e' a
#     moeda, exatamente como a receita e' a moeda no resto do parque. Se o
#     video ensina, nao ha' motivo para comentar.
#
# ⭐ O MOLDE DO HOOK — os quatro elementos, nesta ordem, sempre:
#     <a mancha em {evento}> · <o dano social, curto> · <o vinculo> · <o alarme>
# Sem o VINCULO na mesma fala, a espectadora acha que o assunto e' bexiga e
# rola o feed. E' a regra PE6 do PEE 16 traduzida para este angulo.

HOOKS = [
    # ⛔⛔ O MOLDER E' DO OPERADOR (2026-09-01), e ele nao e' negociavel:
    #     <ela TEM a coisa que voce tem> · <desta vez escalou> · <a catastrofe>
    # A condicao vem ANTES da consequencia. Uma abertura que descreve o
    # acidente sem nomear a ansiedade faz a espectadora achar que o assunto e'
    # bexiga — e mulher com bexiga fraca nao compra curso de respiracao.
    # ⛔ NENHUMA entrada usa termo abstrato inventado (`der Alarm`, `unter
    # Strom`, `das System`). A lente `AT15` cobra o par ansiedade+catastrofe.
    "Sie dachte, sie hat ihre Angst im Griff. {Evento} machte sie sich vor "
    "allen nass.",
    "Sie hat seit Jahren Angstattacken. {Evento} war eine so stark, dass "
    "sie sich nass machte.",
    "Angst sitzt nicht nur im Kopf. {Evento} wurde sie so stark, dass sie "
    "sich nass machte.",
    "Sie ist nicht inkontinent. Sie hatte {evento} eine Angstattacke, und der "
    "Körper ließ los.",
    # ⛔ A versao anterior parava em "beruhig dich einfach": PRESSUPUNHA a
    # ansiedade sem a nomear. Quem chega no scroll nao sabe do que se trata.
    "Ihre Freundin sagt immer: beruhig dich einfach. {Evento} kam die "
    "Angst, und sie machte sich nass.",
    # ⛔ A versao anterior nomeava a condicao e nunca dizia o que aconteceu.
    "Sie nimmt seit Jahren Tropfen gegen die Angst. {Evento} machte sie "
    "sich trotzdem nass.",
    "Kennst du Angstattacken? {Evento} wurde sie so stark, dass sie es nicht "
    "halten konnte.",
    "Sie hatte {evento} eine Angstattacke. So stark, dass sie sich vor "
    "dreißig Leuten nass machte.",
    "Bei starker Angst lässt der Körper los. {Evento} ist ihr genau das "
    "passiert, vor allen.",
    "Sie hat es {evento} nicht mehr geschafft. Nicht die Blase — eine "
    "Angstattacke, vor allen.",
    # ⛔ A versao anterior fechava em "sahen es alle" — viram O QUE?
    "Zehn Jahre Angst, und niemand merkte etwas. {Evento} machte sie sich "
    "vor allen nass.",
    "Sie funktioniert für alle. {Evento} kam die Angst so stark, dass sie "
    "sich nass machte.",
]

# ⭐ O MECANISMO — take 2. Uma causa, dois sintomas, exatamente como o PE7 do
# PEE 16: o alarme explica a mancha E explica a noite sem sono.
# ⛔ NENHUMA ENTRADA DIZ `Panikattacke`, `Angststörung`, `Diagnose` ou `heilen`.
# Ver a docstring e a lente `AT9`.
MECANISMOS = [
    # ⛔⛔ MECANISMO UNICO DO PROBLEMA (Georgi) + "NAO E' SUA CULPA" (Benson).
    # Toda entrada faz DUAS coisas, e a segunda e' a que faltava por inteiro na
    # copy reprovada:
    #   1. nomeia UMA solucao que ela ja' tentou e que falhou;
    #   2. diz POR QUE falhou — aquilo mexe na CABECA, e a tensao esta' no CORPO.
    # Sem (1) a espectadora e' um cetico que ja' tentou de tudo e ouve mais uma
    # promessa; com (1) ela ouve a explicacao que ninguem deu a ela.
    # ⛔ Nada de `der Alarm`, `unter Strom`, `das System` — abstracao inventada
    # nao e' mecanismo, e a lente `AT17` bane a familia.
    "Angst ist keine Kopfsache. Der Körper schaltet um, und der "
    "Beckenboden lässt einfach los.",
    "Beruhig dich hilft deshalb nicht. Die Anspannung sitzt im Körper, nicht "
    "im Kopf.",
    "Atemübungen aus dem Internet erreichen den Kopf. Die Anspannung sitzt "
    "tiefer.",
    "Es ist nicht deine Schuld. Dein Körper hat gelernt, bei Angst alles "
    "loszulassen.",
    "Kein Arzt findet etwas, weil nichts kaputt ist. Es ist gespeicherte "
    "Anspannung.",
    "Beckenbodentraining bringt hier nichts. Du trainierst einen Muskel, der "
    "auf Angst reagiert.",
    "Reden hat ihr nicht geholfen. Die Angst steckte im Körper fest, nicht in "
    "ihrem Kopf.",
    "Jahre Angst stauen sich im Gewebe. Der Körper hält sie fest, bis er "
    "nicht mehr kann.",
    "Du machst nichts falsch. Dein Körper hält die alte Angst, und niemand "
    "hat sie je gelöst.",
    "Tabletten dämpfen den Kopf. Die Anspannung im Körper bleibt genau da, "
    "wo sie war.",
]

# ⭐⭐ O METODO — take 3, e o literal `Freemor Breathing` e' OBRIGATORIO em
# toda entrada (lente `AT5`). E' o mesmo papel do `gelatin trick` no parque:
# sem o nome proprio a espectadora acha que ja' sabe e nao comenta.
# ⛔ Nenhuma entrada ensina o padrao. Diz o que ele FAZ, nunca COMO se faz.
METODOS = [
    # ⛔⛔ MECANISMO UNICO DA SOLUCAO. A copy reprovada dizia *"bringt dich in
    # Minuten runter"* — desce de QUE? Agora toda entrada carrega o TREMOR
    # NEUROGENICO, que e' o que o `Freemor Breathing` tem e o YouTube nao:
    # o corpo DESCARREGA fisicamente a tensao guardada, em vez de a cabeca
    # tentar se acalmar. E' a resposta a "por que isto funciona onde o resto
    # falhou", e e' copy da propria pagina do produto.
    # ⚠️ NENHUMA entrada promete desaparecimento de sintoma. O que o metodo FAZ
    # e' mecanico e verificavel; o que ele CURA seria alegacao sob a HWG.
    "Freemor Breathing löst sie über neurogenes Zittern.",
    "Beim Freemor Breathing zittert der Körper sie raus.",
    "Freemor Breathing schüttelt die alte Angst aus dem Gewebe.",
    "Dafür gibt es Freemor Breathing: Atem plus Zittern.",
    "Freemor Breathing arbeitet im Körper, nicht im Kopf.",
    "Sie hat Freemor Breathing gelernt und zittern gelassen.",
    "Freemor Breathing holt die Anspannung raus, wo sie sitzt.",
    "Freemor Breathing gibt es nur bei ihr: Atem plus Zittern.",
]

# ⭐ A BARREIRA — derruba a objecao antes de ela nascer. Curta, sempre.
# ⛔⛔ SO' BARREIRA DE ACESSO. A barreira fecha o TAKE 2, onde a OFERTA ainda
# nao existe — o metodo so' e' nomeado no take 3. Uma barreira de COMPRA ali
# ("quatorze dias de garantia") e' dinheiro de volta de uma coisa que ninguem
# ainda ouviu falar: frase orfa, teste WTF, §17 das licoes. Saiu do pool, e a
# lente `AT14` proibe a familia inteira para ela nao voltar numa ampliacao.
BARREIRAS = [
    "Niemand muss davon wissen.",
    "Kein Arzt, keine Praxis.",
    "Zu Hause, in deinem Tempo.",
    "Du brauchst nur einen ruhigen Platz.",
    "Keine Termine, kein Warten.",
]

# ⛔⛔ O CTA DIZ ONDE A COISA CHEGA. E' o CT6 do contrato de 16s, e ele vale
# aqui inteiro: sem `in die Nachrichten` a espectadora comenta e depois nao
# sabe onde procurar, e a DM morre sem ser lida.
# ⭐ A keyword e' PARAMETRO (`KEYWORD`), nao literal — trocavel no painel sem
# reescrever pool nenhum.
CTAS = [
    "Kommentiere {kw}, ich schicke es dir in die Nachrichten.",
    "Schreib {kw}, es kommt in deine Nachrichten.",
    # ⛔ REESCRITA. Era "Ein Wort: {kw}." — a keyword SEM verbo de comando
    # na frente. Nessa forma o `trocar_keyword` nao casa, e um lote com a
    # palavra trocada no painel sairia com DUAS keywords diferentes: a nova
    # nas seis entradas e a velha nesta. Keyword parcialmente trocada e'
    # pior que keyword nao trocada. Lente `AT16`.
    "Kommentiere {kw}, dann liegt es in deinen Nachrichten.",
    "Kommentiere {kw} und schau in deine Nachrichten.",
    "Kommentiere {kw}. Es kommt heute in deine Nachrichten.",
    "Kennst du das? Dann kommentiere {kw}. Es kommt in deine Nachrichten.",
    "Kommentiere {kw}, und es ist heute in deinen Nachrichten.",
]


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

IMAGENS = ("IMAGE 01/03", "IMAGE 02/03", "IMAGE 03/03")
TAKES = ("TAKE 01/03", "TAKE 02/03", "TAKE 03/03")

# ⭐ Quantos sorteios de memoria por eixo. Numero baixo em pool pequeno faz o
# ledger travar (nada sobra para sortear); numero alto em pool grande nao
# custa nada. A regra e' ~1/3 do pool.
MEMORIA = {
    "local": 5, "roupa": 4, "mancha": 2, "ref": 4, "vitima": 3,
    "ambiente": 3, "traje": 3, "hook": 4, "mecanismo": 3, "metodo": 3,
    "barreira": 2, "cta": 2,
}


def _carregar_ledger():
    try:
        with io.open(LEDGER, encoding="utf-8") as f:
            return json.load(f)
    except (IOError, OSError, ValueError):
        return {}


def _gravar_ledger(led, spec, em_disco=True):
    """Anota o sorteio na memoria e, se pedido, grava em disco.

    ⛔⛔ `em_disco` NASCEU DE UM LOTE LIDO (2026-09-01). O `--dry-run` pulava
    esta funcao INTEIRA, entao a memoria anti-repeticao ficava inerte DENTRO da
    propria rodada: os cinco videos de um lote de revisao viam o mesmo
    historico vazio e 3 de 5 sairam com o mesmo hook, de um pool de 12.
    ⚠️ O estrago nao e' o lote — e' a CONCLUSAO que ele induz. Quem le' um lote
    assim acha que os pools sao pobres e vai "consertar" o que nao esta'
    quebrado.
    ⭐ A separacao certa: a memoria SEMPRE anota (ela e' o que faz o lote
    variar); o disco so' e' tocado quando o operador quer de fato consumir o
    historico.
    """
    for eixo, n in MEMORIA.items():
        v = spec.get("_id_%s" % eixo)
        if v is None:
            continue
        hist = led.setdefault(eixo, [])
        hist.append(v)
        del hist[:-n]
    if not em_disco:
        return
    try:
        with io.open(LEDGER, "w", encoding="utf-8") as f:
            f.write(json.dumps(led, ensure_ascii=False, indent=1))
    except (IOError, OSError):
        pass


def _evitando(rng, pool, recentes, chave=None):
    """Sorteia fora dos recentes; se nao sobrar nada, sorteia do pool inteiro.

    ⚠️ O fallback e' obrigatorio e nao e' preguica: sem ele um pool que encolhe
    (ou uma trava da UI que fixa um eixo) faz o motor levantar IndexError no
    meio do lote. Ledger e' preferencia, nunca condicao.
    """
    def _k(x):
        return x[chave] if chave else x
    livres = [x for x in pool if _k(x) not in recentes]
    return rng.choice(livres or list(pool))


def sortear(pagina, rng, led, travas=None):
    travas = travas or {}
    et = ETNIA[pagina]

    def _pega(eixo, pool, chave=None, trava_por=None):
        if trava_por and travas.get(eixo):
            alvo = travas[eixo]
            achados = [x for x in pool if x.get(trava_por) == alvo]
            if achados:
                return rng.choice(achados)
        return _evitando(rng, pool, led.get(eixo, []), chave)

    local = _pega("local", LOCAIS, "id", "id")
    roupa = _pega("roupa", ROUPAS, "peca", "peca")
    ref = _pega("ref", REFS, "id", "id")
    vitima = _pega("vitima", VITIMAS, "id", "id")
    ambiente = _pega("ambiente", AMBIENTES, "id", "id")

    mancha = _evitando(rng, MANCHA, led.get("mancha", []))
    traje = _evitando(rng, TRAJES, led.get("traje", []))
    hook = _evitando(rng, HOOKS, led.get("hook", []))
    mecanismo = _evitando(rng, MECANISMOS, led.get("mecanismo", []))
    metodo = _evitando(rng, METODOS, led.get("metodo", []))
    barreira = _evitando(rng, BARREIRAS, led.get("barreira", []))
    cta = _evitando(rng, CTAS, led.get("cta", []))

    ev = local["evento"]
    fala1 = hook.replace("{Evento}", ev[0].upper() + ev[1:]).replace(
        "{evento}", ev)
    # ⛔⛔ A BARREIRA FECHA O TAKE 2, NAO O 3 — e e' consequencia MEDIDA, nao
    # arrumacao. Com metodo + CTA + barreira no take 3 a fala chegava a 59
    # silabas contra um teto de 35: tres batidas num take de 8 segundos.
    # ⭐ O take 2 tem folga (o mecanismo fecha em ~20) e a barreira cai bem
    # ali: ela responde a objecao que o mecanismo acaba de levantar ("entao eu
    # teria de ir ao medico"). O take 3 fica com DUAS batidas, que e' o que
    # cabe.
    fala2 = "%s %s" % (mecanismo, barreira)
    fala3 = "%s %s" % (metodo, cta.replace("{kw}", KEYWORD))

    return {
        "pagina": pagina, "etnia": et,
        "local": local, "roupa": roupa, "mancha": mancha, "ref": ref,
        "vitima": vitima, "ambiente": ambiente, "traje": traje,
        # ⛔ LISTA, nao dicionario: o `ui_agente` le' `spec["falas"][i]`
        # com `i` vindo de `enumerate(CENAS_UI)` — zero-based — e faz
        # `list(spec["falas"])`. Com dicionario a janela morre no _render.
        "falas": [fala1.strip(), fala2.strip(), fala3.strip()],
        "_id_local": local["id"], "_id_roupa": roupa["peca"],
        "_id_mancha": mancha, "_id_ref": ref["id"],
        "_id_vitima": vitima["id"], "_id_ambiente": ambiente["id"],
        "_id_traje": traje, "_id_hook": hook, "_id_mecanismo": mecanismo,
        "_id_metodo": metodo, "_id_barreira": barreira, "_id_cta": cta,
    }


# ===========================================================================
# MONTAGEM
# ===========================================================================

def _M(txt):
    """Maiuscula na primeira letra, sem tocar no resto.

    ⚠️ Existe porque `CHORO_TAKE` e `CHORO_IMAGE` sao copia literal do PEE 16,
    onde entram no meio de uma frase e por isso nascem em minuscula. Reescrever
    a string travada para consertar a pontuacao seria mexer em copy validada em
    render — o ajuste mora aqui.
    """
    return txt[:1].upper() + txt[1:] if txt else txt


def montar(spec):
    ref, vit = spec["ref"], spec["vitima"]
    loc, roupa, amb = spec["local"], spec["roupa"], spec["ambiente"]
    et, traje = spec["etnia"], spec["traje"]
    f = spec["falas"]

    # ⛔⛔ O BLOCO DE VOZ E' TRAVADO E REPETIDO PALAVRA POR PALAVRA NOS TRES
    # TAKES. Cada take e' uma chamada de video SEPARADA — o modelo ve' UM take
    # por vez e nao tem o anterior. Pedir *"a mesma voz do take anterior"* e'
    # anafora sem antecedente. O que faz tres geracoes independentes
    # convergirem e' a descricao caber numa voz so'.
    # ⛔⛔ E ELA DECLARA ALEMA NATIVA. Sem isso o TTS le' o alemao com fonemas
    # ingleses e a espectadora alema descarta o video no primeiro segundo — e'
    # o unico defeito deste motor que nenhum outro do parque tem como existir.
    voz = ("Voice: one calm German woman in her late thirties speaking NATIVE "
           "GERMAN with a neutral standard German accent, pitched low and "
           "unhurried, close to the microphone at ordinary conversational "
           "volume, never raised and never whispered, speaking at the ordinary "
           "pace of everyday German speech. The pitch, the texture, the accent "
           "and the speed are identical in all three takes.")

    # ⭐ A ancora de identidade da narradora, por extenso nos TRES quadros. Sem
    # ela o take 2 devolve outra mulher — e o take 1 e o take 3 sao gerados
    # separadamente, entao nao ha' de onde o modelo herdar o rosto.
    # ⛔ A ETNIA NAO ENTRA NA ANCORA: as frases que a consomem ja' dizem o
    # gentilico, e duas vozes decidindo a mesma coisa o Veo resolve inventando
    # uma terceira. Defeito FT14 do FIGHT 16.
    ancora = "%s, %s" % (ref["desc"], ref["cabelo"])

    blocos = {}

    # -- BLOCO 0 (REF) -----------------------------------------------------
    blocos["BLOCO 0 (REF)"] = (
        "REF 01: Photo of a real person: a head and shoulders portrait of a "
        "%d-year-old %s woman, %s. Plain neutral grey background, soft even "
        "frontal light, the head upright and facing the lens. Slight sensor "
        "grain, raw amateur photo look. No on-screen text, no subtitles, no "
        "captions, no watermark." % (ref["idade"], et, ancora))

    # -- IMAGE 01/03 — A MANCHA -------------------------------------------
    blocos["IMAGE 01/03"] = (
        "IMAGE 01/03: %s %s A %d-year-old %s woman stands in the middle of the "
        "frame wearing %s, with %s. She stands %s Beside her is the woman from "
        "the reference photo, a %d-year-old %s woman, %s, wearing %s, %s. "
        "%s. Overhead daylight, ordinary indoor exposure. %s"
        % (ORIENTACAO, loc["cenario"].capitalize() + ".", vit["idade"], et,
           roupa["peca"], spec["mancha"], CHORO_IMAGE, ref["idade"], et,
           ancora, traje, NARRADORA_IMAGE, PLATEIA_IMAGE % loc["plateia"],
           CAUDA))

    blocos["TAKE 01/03"] = (
        # ⚠️ `_M` poe a maiuscula em `CHORO_TAKE`, que nasce em minuscula
        # porque no PEE ela entra no MEIO de uma frase. A string travada nao se
        # reescreve — quem se ajusta e' a montagem.
        "TAKE 01/03: Animate the image exactly. Handheld iPhone, slight sway, "
        "no cuts. %s %s The blurred %s behind them keep laughing and pointing. "
        "Nothing else in the frame moves.\n"
        "Dialogue: \"%s\"\n"
        "%s\n%s"
        % (NARRADORA_TAKE, _M(CHORO_TAKE), loc["plateia"], f[0], voz,
           AUDIO_MANCHA))

    # -- IMAGE 02/03 — O ALARME -------------------------------------------
    # ⭐ A narradora sozinha, no ATEMPLATZ, com o modelo anatomico erguido. O
    # set ja' e' o do take 3 de proposito: dois quadros no mesmo lugar deixam a
    # ESPECTADORA reconhecer o lugar, e o corte de ambiente do meio do video e'
    # o que mais custa continuidade num motor de tres geracoes separadas.
    blocos["IMAGE 02/03"] = (
        "IMAGE 02/03: %s %s The woman from the reference photo, a %d-year-old "
        "%s woman, %s, wearing %s, sits on a low cushion facing the lens, "
        "framed from the waist up. %s %s She is alone in the frame. %s"
        % (ORIENTACAO, amb["set"].capitalize() + ".", ref["idade"], et,
           ancora, traje, D1_IMAGE, amb["luz"].capitalize() + ".", CAUDA))

    blocos["TAKE 02/03"] = (
        "TAKE 02/03: Animate the image exactly. Handheld iPhone, slight sway, "
        "no cuts. %s Her eyes stay on the lens the whole time. She is alone in "
        "the shot and nothing new enters the frame.\n"
        "Dialogue: \"%s\"\n"
        "%s\n"
        "Audio: quiet room tone only. No music."
        % (D1_TAKE, f[1], voz))

    # -- IMAGE 03/03 — O METODO + CTA -------------------------------------
    # ⛔ O modelo anatomico SAI de quadro. Ele era a prova do alarme; no take 3
    # a prova e' a POSE, e prop antigo que fica vira ruido que o gerador tenta
    # justificar com movimento.
    blocos["IMAGE 03/03"] = (
        "IMAGE 03/03: %s %s The same woman from the reference photo, a "
        "%d-year-old %s woman, %s, wearing %s, %s, framed from the waist up. "
        "Her hands are the only things she is holding — nothing else is in "
        "her hands and nothing else rests on the cushion. %s She is alone in "
        "the frame. %s"
        % (ORIENTACAO, amb["set"].capitalize() + ".", ref["idade"], et,
           ancora, traje, ATEMPLATZ_POSE, amb["luz"].capitalize() + ".",
           CAUDA))

    blocos["TAKE 03/03"] = (
        "TAKE 03/03: Animate the image exactly. Handheld iPhone, slight sway, "
        "no cuts. Her chest rises once slowly under her left hand as she "
        "speaks — that is the only movement. Both hands stay flat where they "
        "are. Her eyes stay on the lens the whole time. She is alone in the "
        "shot and nothing new enters the frame.\n"
        "Dialogue: \"%s\"\n"
        "%s\n"
        "Audio: quiet room tone only. No music."
        % (f[2], voz))

    return blocos


# ===========================================================================
# LENTES
# ===========================================================================
# ⛔ Toda lente devolve ("ERRO", msg) ou ("AVISO", msg). ERRO aborta o video
# antes de ele ser impresso (ver `main`) — video com erro que chega a tela e'
# video que o operador copia, e e' o padrao "agente reprovado rodavel".

# ⭐ O padrao respiratorio E' A MOEDA. Se o video ensina, nao ha' motivo para
# comentar — e' o CT5 do contrato de 16s traduzido para este produto.
_ENSINA = re.compile(
    r"\b(?:vier|fünf|sechs|sieben|acht|zwei|drei|\d+)\s+(?:sekunden|mal|"
    r"atemzüge)\b"
    r"|\bein\s*[-–]\s*aus\b"
    r"|\batme\s+(?:tief\s+)?(?:ein|aus)\b"
    r"|\bdurch\s+die\s+nase\s+ein\b"
    r"|\bhalte\s+den\s+atem\b"
    r"|\bzähl(?:e|st)?\s+bis\b", re.I)

# ⛔ A moldura. Ver a docstring — estas palavras vendem contra a
# contraindicacao declarada do proprio produtor.
# ⛔ A MOLDURA, ESTREITADA EM 2026-09-01 POR ORDEM DO OPERADOR.
# Antes ela barrava tambem o vocabulario de ansiedade, porque a pagina do
# produto exclui por escrito quem tem `Panikattacken`. O operador reescreveu a
# copy nomeando ansiedade — e copy e' alcada dele.
# ⭐ O que fica barrado e' o que de fato cria risco sob a HWG alema: alegacao
# de CURA e de TRATAMENTO. Descrever a pessoa nao e' alegacao medica; prometer
# curar e'. `Angst` e `Angstattacke` passam; `heilen` e `Therapie` nao.
_MOLDURA = re.compile(
    r"\bangststörung\w*\b|\bpanikstörung\w*\b|\bdiagnose\w*\b"
    r"|\bheil(?:en|ung|t)\b|\btherapie\b|\bkrankheit\b"
    r"|\bgeheilt\b|\bbehandl\w*\b",
    re.I)

# ⛔ A palavra da gelatina nao entra aqui. O parque fala gelatina em 32
# motores, e copy colada de um deles traria a palavra junto sem ninguem ver.
_GELATINA = re.compile(r"\bgelatin\w*\b|\bgelatine\b", re.I)

# ⛔ Negacao de celebridade — a municao que a varredura de 2026-08-14 tirou de
# 30 arquivos. Esta lente existe para ela nunca voltar por copia.
_ANTICELEB = re.compile(
    r"\bnot\s+(?:a\s+)?(?:celebrity|celebrities|famous|model|models|actor|"
    r"actors)\b|\bno\s+celebrit", re.I)

# ⛔ Aparelho em quadro — licao paga com um lote inteiro no VICK 16. Pega tanto
# o pedido direto quanto a NEGACAO, que injeta o token do mesmo jeito.
_APARELHO = re.compile(r"\b(?:phone|smartphone|iphone\s+in|camera\s+in\s+her|"
                       r"filming|records?\s+her|handy)\b", re.I)

# ⭐⭐ O ELO. O hook TEM de ligar a mancha ao alarme na MESMA fala. Sem isso a
# espectadora acha que o assunto e' bexiga e rola o feed — e' a regra PE6 do
# PEE 16 (mijo + orgao + vinculo) traduzida para este angulo.
# ⛔ Ela existia so' como comentario acima do pool ate' 2026-09-01, e uma das
# doze entradas ja' a violava. Molde que nao vira codigo e' onde o vicio mora.
# ⭐⭐ O ELO — REESCRITO EM 2026-09-01, E A VERSAO ANTIGA COBRAVA O DEFEITO.
# Ela exigia `alarm|strom|system|druck|pause` na fala 1: ou seja, OBRIGAVA o
# vocabulario abstrato que o operador reprovou por drifting. Regra que codifica
# o vicio e' pior que regra ausente — ela impede o conserto.
# ⛔ O elo verdadeiro e' um PAR, e os dois lados sao concretos:
#     <a condicao que a espectadora TEM>  +  <a catastrofe que ela VE>
# Sem o primeiro ela acha que o assunto e' bexiga; sem o segundo nao ha' hook.
_ANSIEDADE = re.compile(
    r"\bangst\w*\b|\bpanik\w*\b", re.I)
_CATASTROFE = re.compile(
    r"\bnass\b|\beingenässt\b|\bblase\b|\blos\b"
    r"|\bhalten\b|\bgeschafft\b|\binkontinent\b|\bließ\b", re.I)

# ⛔ APARELHO NA FALA. O AT8 varre a DIRECAO (onde o token faz o gerador
# desenhar o telefone, licao do VICK 16); esta varre a FALA, onde o defeito e'
# outro: ninguem filma em nenhuma cena deste motor, entao mencionar filmagem
# levanta uma pergunta que o video nunca responde.
_APARELHO_FALA = re.compile(r"\bfilm\w*\b|\bhandy\b|\bkamera\b|\bvideo\b"
                            r"|\baufnahme\w*\b", re.I)

# ⛔⛔ AS ABSTRACOES QUE O OPERADOR REPROVOU, 2026-09-01. Cada uma foi um
# termo que EU inventei e usei na fala como se a espectadora ja' o conhecesse:
# `der Alarm` (que alarme?), `unter Strom` (idiomatico e vago), `das System`,
# `ohne Pause`. Teste WTF: se ela pode perguntar "do que ela esta' falando?",
# a copy e' DESCARTE. A lista existe para elas nao voltarem numa ampliacao.
# ⚠️ `Nervensystem` NAO entra: e' termo que a pagina do produto usa e que o
# publico alemao de wellness reconhece. O defeito era `das System` sozinho.
_ABSTRACAO = re.compile(
    r"\bder Alarm\b|\bam Alarm\b|\bim Alarm\b|\bAlarm\s+(?:sitzt|hält|läuft|raubt)"
    r"|\bunter (?:Strom|Dauerstrom)\b"
    r"|\bIhr System\b|\bDein System\b|\bohne Pause\b"
    r"|\bAusnahmezustand\b|\baufgegeben\b",
    re.I)

_RISADA_AUDIO = re.compile(r"audio:[^\n]*\blaugh", re.I)

# ⛔ Vocabulario de COMPRA. Ver a lapide do pool BARREIRAS: no take 2 nao ha'
# oferta ainda, entao garantia, preco e reembolso sao frase orfa.
_COMPRA = re.compile(
    r"\bgeld\s+zurück\b|\bgarantie\b|\brückgabe\b|\berstattung\b"
    r"|\bkostenlos\b|\bpreis\b|\beuro\b|\bbezahl\w*\b|\bkauf\w*\b",
    re.I)


# ⭐ A funcao de troca do compartilhado, importada de forma tolerante: o motor
# tem de rodar tambem no CLI puro, onde o `short_comum` pode nao estar no path.
# ⚠️ Se ela faltar, a `AT16` se cala em vez de mentir um "ok".
try:
    from short_comum import trocar_keyword as _sc_trocar
except ImportError:                                        # pragma: no cover
    _sc_trocar = None


def _direcao(txt):
    """O bloco sem a linha de fala — a lente le' CENA, nunca copy."""
    return txt.split("\nDialogue:")[0]


def lint(spec, blocos):
    ach = []
    f = spec["falas"]
    todos = "\n".join(blocos.values())
    direcoes = "\n".join(_direcao(v) for v in blocos.values())

    # AT1 — os tres quadros carregam orientacao e cauda
    for k in IMAGENS:
        if ORIENTACAO not in blocos[k]:
            ach.append(("ERRO", "AT1: %s sem a orientacao vertical — a AdBatch "
                                "entrega 16:9 e o reel sai com tarja." % k))
        if CAUDA not in blocos[k]:
            ach.append(("ERRO", "AT1: %s sem a cauda de textura." % k))

    # AT2 — a roupa e' clara e a mancha esta' descrita
    i1 = blocos["IMAGE 01/03"]
    if spec["roupa"]["peca"] not in i1:
        ach.append(("ERRO", "AT2: a roupa sorteada nao entrou na IMAGE 01."))
    if spec["mancha"] not in i1:
        ach.append(("ERRO", "AT2: a MANCHA nao entrou na IMAGE 01 — sem mancha "
                            "legivel nao ha' angulo."))
    if not re.search(r"\b(?:light|pale|cream|off white|sand|washed out|stone)\b",
                     spec["roupa"]["peca"], re.I):
        ach.append(("ERRO", "AT2: roupa escura no pool — numa calca escura a "
                            "mancha nao le'."))

    # AT3 — a testemunha e' obrigatoria, e o substantivo casa com o local
    if PLATEIA_IMAGE % spec["local"]["plateia"] not in i1:
        ach.append(("ERRO", "AT3: sem plateia em quadro — humilhacao publica "
                            "sem terceiro vira acidente privado."))
    if spec["local"]["plateia"] not in blocos["TAKE 01/03"]:
        ach.append(("ERRO", "AT3: o substantivo da plateia diverge entre a "
                            "IMAGE e o TAKE — o gerador inventa um terceiro."))

    # AT4 — nenhuma fala ensina o padrao
    for i in (0, 1, 2):
        if _ENSINA.search(f[i]):
            ach.append(("ERRO", "AT4: a fala %d ENSINA o padrao respiratorio. "
                                "A tecnica e' a moeda — se o video ensina, "
                                "ninguem comenta." % (i + 1)))

    # AT5 — o mecanismo tem nome proprio no take 3
    if "Freemor Breathing" not in f[2]:
        ach.append(("ERRO", "AT5: o take 3 nao nomeia `Freemor Breathing` — "
                            "sem o nome proprio a espectadora acha que ja' "
                            "sabe e nao comenta."))

    # AT6 — o teto FISICO, em silabas
    for i in (0, 1, 2):
        s = silabas_frase(f[i])
        p = palavras(f[i])
        if s > TETO_SILABAS:
            ach.append(("ERRO", "AT6: a fala %d tem %d silabas (teto %d) — nao "
                                "cabe em 8s e sai cortada no render."
                        % (i + 1, s, TETO_SILABAS)))
        elif s > TETO_SILABAS - 3:
            ach.append(("AVISO", "AT6: a fala %d tem %d silabas, no limite."
                        % (i + 1, s)))
        if p > TETO_PALAVRAS:
            ach.append(("AVISO", "AT6: a fala %d tem %d palavras (rede %d)."
                        % (i + 1, p, TETO_PALAVRAS)))

    # AT7 — o CTA diz a keyword E onde a coisa chega
    if KEYWORD not in f[2]:
        ach.append(("ERRO", "AT7: a keyword `%s` nao esta' no CTA." % KEYWORD))
    # ⚠️ `nachricht\w*`: singular e plural dizem a mesma coisa, e cobrar so'
    # o plural seria a lente medindo GRAMATICA em vez de FUNCAO. Ela quer
    # saber se o CTA diz ONDE a receita chega.
    if not re.search(r"\bnachricht\w*\b", f[2], re.I):
        ach.append(("ERRO", "AT7: o CTA nao diz ONDE a coisa chega — ela "
                            "comenta e depois nao sabe onde procurar."))

    # AT8 — nem negacao de celebridade, nem aparelho
    if _ANTICELEB.search(todos):
        ach.append(("ERRO", "AT8: negacao de celebridade no prompt — ela "
                            "INJETA o token que se quer evitar."))
    if _APARELHO.search(direcoes):
        ach.append(("ERRO", "AT8: aparelho descrito na direcao de cena — o "
                            "gerador DESENHA o aparelho (lote perdido no "
                            "VICK 16)."))

    # AT9 — a moldura declarada
    for i in (0, 1, 2):
        if _MOLDURA.search(f[i]):
            ach.append(("ERRO", "AT9: a fala %d usa vocabulario de diagnostico "
                                "ou de cura. O produtor exclui essa pessoa por "
                                "escrito na propria pagina — ver a docstring."
                        % (i + 1)))

    # AT17 — nenhuma abstracao inventada volta para a fala
    for i in (0, 1, 2):
        m = _ABSTRACAO.search(f[i])
        if m:
            ach.append(("ERRO", "AT17: a fala %d usa `%s` — abstracao que o "
                                "operador reprovou por drifting. A espectadora "
                                "nunca ouviu esse termo, entao ele nao compra "
                                "nada. Descarte, nao conserto."
                        % (i + 1, m.group(0))))

    # AT16 — a keyword tem de ser TROCAVEL de verdade
    # ⛔ Nao basta a palavra estar no CTA (AT7). O campo do painel so' compra
    # alguma coisa se a troca MUDAR o texto — e' a licao "slot tem que cumprir
    # funcao": o linter checa forma, e forma sem funcao e' o defeito que este
    # repo mais paga. Aqui a funcao e' medida, nao assumida.
    if _sc_trocar is not None:
        if _sc_trocar(f[2], KEYWORD, "PROBE") == f[2]:
            ach.append(("ERRO", "AT16: a keyword do CTA nao e' trocavel — o "
                                "campo do painel ficaria mudo e o lote sairia "
                                "com a palavra velha."))

    # AT15 — o hook carrega o ELO, e nenhuma fala fala em filmar
    if not _ANSIEDADE.search(f[0]):
        ach.append(("ERRO", "AT15: o hook nao NOMEIA a ansiedade — sem isso a "
                            "espectadora acha que o assunto e' bexiga, e "
                            "mulher com bexiga fraca nao compra curso de "
                            "respiracao."))
    if not _CATASTROFE.search(f[0]):
        ach.append(("ERRO", "AT15: o hook nao diz a catastrofe concreta. "
                            "Condicao sem consequencia visivel nao e' hook."))
    for i in (0, 1, 2):
        if _APARELHO_FALA.search(f[i]):
            ach.append(("ERRO", "AT15: a fala %d fala em filmagem ou aparelho. "
                                "Ninguem filma em cena nenhuma deste motor."
                        % (i + 1)))

    # AT14 — nenhuma barreira de COMPRA no take 2
    if _COMPRA.search(f[1]):
        ach.append(("ERRO", "AT14: barreira de COMPRA na fala 2 — o metodo so' "
                            "e' nomeado no take 3, entao garantia ou preco ali "
                            "fala de uma oferta que a espectadora ainda nao "
                            "ouviu. Frase orfa."))

    # AT10 — a gelatina nao mora aqui
    if _GELATINA.search(todos):
        ach.append(("ERRO", "AT10: a palavra da gelatina entrou neste motor — "
                            "copy colada de outro agente."))

    # AT11 — risada nunca no audio
    if _RISADA_AUDIO.search(blocos["TAKE 01/03"]):
        ach.append(("ERRO", "AT11: riso na pista de audio — o Veo sincroniza "
                            "rosto com audio e poe a chorando a rir."))

    # AT12 — a ancora de rosto atravessa os tres quadros
    n = sum(1 for k in IMAGENS if spec["ref"]["desc"] in blocos[k])
    if n < 3:
        ach.append(("ERRO", "AT12: a ancora de rosto da narradora esta' em "
                            "%d de 3 quadros — os tres sao geracoes separadas "
                            "e sem ela volta outra mulher." % n))

    # AT13 — o dedo aponta o tecido e nunca encosta
    if NARRADORA_TAKE not in blocos["TAKE 01/03"]:
        ach.append(("ERRO", "AT13: a trava do dedo saiu do TAKE 01 — e' a "
                            "construcao que fez este beat passar na moderacao "
                            "depois de 4 recusas por agencia."))

    return ach


# ===========================================================================
# UI
# ===========================================================================

EIXOS_UI = [
    ("local", "LOCAL", "LOCAIS", "id"),
    ("roupa", "ROUPA", "ROUPAS", "peca"),
    ("ref", "NARRADORA", "REFS", "id"),
    ("vitima", "VÍTIMA", "VITIMAS", "id"),
    ("ambiente", "ATEMPLATZ", "AMBIENTES", "id"),
]

# ⭐ O dropdown fixa a narradora para todo sorteio — mesma mecanica do MEL 16 e
# do PEE 16. E' ele que da' FUNCAO ao campo `rotulo` dos 12 REFs; sem esta
# linha os 12 textos seriam comentario caro.
DROPDOWNS_UI = [("ref", "NARRADORA", "REFS", "rotulo")]

PT_LOCAL = {
    "supermarkt": "No supermercado", "kasse": "Na fila do caixa",
    "apotheke": "Na farmácia", "bahnsteig": "Na plataforma do trem",
    "wartezimmer": "Na sala de espera", "baeckerei": "Na padaria",
    "buero": "No escritório", "elternabend": "Na reunião de pais",
    "bus": "No ônibus", "wochenmarkt": "Na feira",
    "amt": "Na repartição pública", "fitnessstudio": "Na academia",
    "hochzeit": "No casamento", "flughafen": "No aeroporto",
    "restaurant": "No restaurante",
}


def resumo_pt(spec):
    f = spec["falas"]
    return (
        "%s · página %s (%s)\n"
        "  LOCAL      %s\n"
        "  NARRADORA  %s\n"
        "  VÍTIMA     %s\n"
        "  ATEMPLATZ  %s\n"
        "  fala 1     %d sílabas / %d palavras\n"
        "  fala 2     %d sílabas / %d palavras\n"
        "  fala 3     %d sílabas / %d palavras"
        % (TITULO, spec["pagina"], spec["etnia"],
           PT_LOCAL.get(spec["local"]["id"], spec["local"]["id"]),
           spec["ref"]["rotulo"], spec["vitima"]["rotulo"],
           spec["ambiente"]["id"],
           silabas_frase(f[0]), palavras(f[0]),
           silabas_frase(f[1]), palavras(f[1]),
           silabas_frase(f[2]), palavras(f[2])))


# ===========================================================================
# AUTOTESTE
# ===========================================================================

def autoteste(n=400):
    print("=" * 70)
    print("AUTOTESTE — %s · %d sorteios" % (TITULO, n))
    print("=" * 70)

    rng = random.Random(20260901)
    led = {}
    erros, avisos = [], []
    vistos = {e: set() for e in MEMORIA}
    max_sil = {0: 0, 1: 0, 2: 0}
    falas = {0: set(), 1: set(), 2: set()}
    tam_bloco = 0

    for _ in range(n):
        pag = rng.choice(sorted(ETNIA))
        s = sortear(pag, rng, led, None)
        b = montar(s)
        for nivel, msg in lint(s, b):
            (erros if nivel == "ERRO" else avisos).append(msg)
        for e in MEMORIA:
            vistos[e].add(s["_id_%s" % e])
        for i in (0, 1, 2):
            max_sil[i] = max(max_sil[i], silabas_frase(s["falas"][i]))
            falas[i].add(s["falas"][i])
        tam_bloco = max(tam_bloco, max(len(v) for v in b.values()))
        # ⛔ `em_disco=False`: o autoteste sorteia 400 videos SINTETICOS e nao
        # pode enterrar a memoria real do operador debaixo deles. Ele usa um
        # `led` proprio ({}) justamente para nao ler o dele — gravar seria
        # desfazer metade do isolamento.
        _gravar_ledger(led, s, em_disco=False)

    print("\n1. LENTES")
    print("   ERRO  : %d" % len(erros))
    for m in sorted(set(erros))[:8]:
        print("      - %s" % m)
    print("   AVISO : %d (%d distintos)" % (len(avisos), len(set(avisos))))
    for m in sorted(set(avisos))[:5]:
        print("      - %s" % m)

    print("\n2. ALCANCE DOS POOLS")
    tamanhos = {
        "local": len(LOCAIS), "roupa": len(ROUPAS), "mancha": len(MANCHA),
        "ref": len(REFS), "vitima": len(VITIMAS), "ambiente": len(AMBIENTES),
        "traje": len(TRAJES), "hook": len(HOOKS), "mecanismo": len(MECANISMOS),
        "metodo": len(METODOS), "barreira": len(BARREIRAS), "cta": len(CTAS),
    }
    mortos = 0
    for e in sorted(tamanhos):
        viv, tot = len(vistos[e]), tamanhos[e]
        selo = "ok " if viv == tot else "MOR"
        if viv != tot:
            mortos += 1
        print("   %s %-10s %2d/%2d" % (selo, e, viv, tot))
    if mortos:
        print("   ⛔ %d pool(s) com entrada inalcancavel — entrada que nao sai "
              "esta' morta, e o autoteste a contava como viva." % mortos)

    print("\n3. TETO FISICO DE FALA (silabas, teto %d)" % TETO_SILABAS)
    for i in (0, 1, 2):
        print("   cena %d: maximo %2d silabas · %d falas distintas"
              % (i + 1, max_sil[i], len(falas[i])))

    print("\n4. TAMANHO DE BLOCO (teto da AdBatch: 3.900 caracteres)")
    print("   maior bloco gerado: %d caracteres" % tam_bloco)
    if tam_bloco > 3900:
        print("   ⛔ ACIMA DO TETO — a AdBatch corta em silencio.")

    print("\n5. CONTROLE NEGATIVO — as lentes acusam quando o defeito existe?")
    plantios = [
        ("AT5", lambda sp, bl: sp["falas"].__setitem__(
            2, sp["falas"][2].replace("Freemor Breathing", "Atemtechnik"))),
        ("AT9", lambda sp, bl: sp["falas"].__setitem__(
            1, "Das war eine Panikattacke und Freemor heilt sie.")),
        ("AT10", lambda sp, bl: bl.__setitem__(
            "IMAGE 02/03", bl["IMAGE 02/03"] + " A glass of gelatin.")),
        ("AT8", lambda sp, bl: bl.__setitem__(
            "IMAGE 01/03", bl["IMAGE 01/03"] + " Ordinary face, not a "
                                               "celebrity.")),
        ("AT3", lambda sp, bl: bl.__setitem__(
            "IMAGE 01/03", bl["IMAGE 01/03"].replace(
                PLATEIA_IMAGE % sp["local"]["plateia"], ""))),
        ("AT14", lambda sp, bl: sp["falas"].__setitem__(
            1, sp["falas"][1] + " Vierzehn Tage Geld zurück.")),
        ("AT15", lambda sp, bl: sp["falas"].__setitem__(
            0, "Ihr Körper hat vor allen versagt, mitten am Tag.")),
        ("AT17", lambda sp, bl: sp["falas"].__setitem__(
            1, sp["falas"][1] + " Der Alarm sitzt seit Jahren fest.")),
        ("AT4", lambda sp, bl: sp["falas"].__setitem__(
            0, "Atme vier Sekunden ein und sechs Sekunden aus.")),
        ("AT12", lambda sp, bl: bl.__setitem__(
            "IMAGE 03/03", bl["IMAGE 03/03"].replace(sp["ref"]["desc"], "a "
                                                                        "face"))),
    ]
    rng2 = random.Random(7)
    for nome, planta in plantios:
        pegou = 0
        for _ in range(40):
            s = sortear(rng2.choice(sorted(ETNIA)), rng2, {}, None)
            b = montar(s)
            planta(s, b)
            if any(m.startswith(nome + ":") for _n, m in lint(s, b)):
                pegou += 1
        selo = "ok " if pegou == 40 else "FALHA"
        print("   %s %-5s plantado 40x, acusado %d/40" % (selo, nome, pegou))

    print("\n6. SILABAS — o contador contra casos conhecidos")
    casos = [("Blase", 2), ("Nervensystem", 4), ("heute", 2), ("Atem", 2),
             ("Supermarkt", 3), ("Nachrichten", 3), ("Freemor", 2),
             ("eingenässt", 3), ("Ausnahmezustand", 5)]
    for w, esperado in casos:
        got = silabas(w)
        selo = "ok " if got == esperado else "!! "
        print("   %s %-16s %d (esperado %d)" % (selo, w, got, esperado))

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
    ap.add_argument("--pagina", choices=sorted(ETNIA), default="anna")
    ap.add_argument("--n", type=int, default=1)
    ap.add_argument("--seed", type=int)
    ap.add_argument("--local", choices=[x["id"] for x in LOCAIS])
    ap.add_argument("--ref", choices=[x["id"] for x in REFS])
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--autoteste", action="store_true")
    a = ap.parse_args()

    if a.autoteste:
        return autoteste()

    led = _carregar_ledger()
    rng = random.Random(a.seed)
    travas = {}
    if a.local:
        travas["local"] = a.local
    if a.ref:
        travas["ref"] = a.ref

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
