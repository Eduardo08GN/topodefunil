#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE GELO 16 — 3 takes de 8s (24s), destino AdBatch **Vertical 3**.

⭐⭐ O ANGULO E' A IMAGEM. Uma alema sentada de pernas cruzadas SOBRE o gelo —
lagoa glacial, lingua de geleira, praia de gelo negro — falando calmamente para
a lente enquanto o mundo em volta diz que ninguem deveria estar ali.
Modelado no short do Wim Hof que o operador garimpou (`When anxiety speaks, be
still, and breathe`), com o homem trocado por mulher e a fala trazida para o
alemao.

⛔⛔ NAO HOUVE LEITURA OTICA, E ISSO E' DIVIDA DECLARADA. O YouTube bloqueou o
acesso e so' sobraram o titulo, uma legenda do print (`YOU BRING IT ALL INTO
CALMNESS`) e o quadro visivel. O POOL VISUAL sai desse quadro; o POOL DE FALA
e' construcao nossa sob o contrato, nao verbatim. Pool nasce de video lido —
quando o operador conseguir a transcricao, os HOOKS se refazem.

⛔⛔ ELA SENTA SOBRE O GELO, NUNCA DENTRO DA AGUA. Ordem do operador, e ela
tambem e' a decisao segura: respiracao seguida de imersao e' o mecanismo do
desmaio de aguas rasas, que mata gente que sabe nadar. Um criativo que mostra
alguem respirando dentro de agua gelada convida a copia. A lente `GE4` bane
imersao do pool inteiro.

⭐ E O GELO NAO E' O METODO — ESSA E' A ESPINHA DA COPY. A oferta e' o
`Begin To Breathe`, que vende respiracao, e a pagina cita frio so' como
complemento OPCIONAL depois da respiracao. Se o video prometer frio, a VSL
entrega outra coisa e o clique morre na pagina.
Por isso o arco e':
    take 1  a imagem impossivel, e ela ja' devolve o merito para a RESPIRACAO
    take 2  por que o que ela ja' tentou falhou
    take 3  `dafuer brauchst du kein Eis` — a barreira cai e o gelo sai de cena
A ultima fala existe para desarmar a propria isca: o gelo trouxe o olho, e a
oferta nao precisa dele.

⛔ Elenco feminino, persona NOVA. O arquetipo da coach de tricô do ATEM 16 nao
sustenta uma lagoa glacial — aqui o corpo e' de quem enfrenta frio.
⛔ Ela FALA em quadro, olhando a lente, como no video de referencia.

⚠️ O teto de fala continua em SILABAS (35 em 8s), pela razao registrada no
ATEM 16: alemao gasta ~1,7 silabas por palavra e um teto de palavras autoriza
fala que nao cabe.
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
LEDGER = os.path.join(AQUI, ".gelo-16-ledger.json")

TITULO = "AGENTE GELO 16"
SLUG = "gelo-16"
SUBTITULO = ("3 takes de 8s = 24 segundos · ela sentada sobre o gelo, e o "
             "metodo que nao precisa de gelo nenhum")

CENAS_UI = ["1 · O GELO", "2 · POR QUE FALHOU", "3 · A BARREIRA + CTA"]

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

# ⛔⛔ A POSE. Ela senta SOBRE o gelo, de pernas cruzadas, costas retas, ombros
# soltos. E' a pose do video de referencia e e' o que separa "mulher passando
# frio" de "mulher no controle" — o corpo relaxado num lugar que deveria
# encolher qualquer um e' o bit visual inteiro do angulo.
POSE = (
    "sitting upright and cross-legged directly on the ice, her back straight "
    "and her shoulders down and loose, both hands resting open on her knees "
    "with the palms turned up, her face calm and unstrained"
)

# ⛔⛔ ELA NAO TREME E NAO SE ENCOLHE. Sem esta trava o gerador desenha a
# reacao obvia ao frio — ombros subidos, bracos cruzados, careta — e o quadro
# passa a dizer o contrario da fala. A calma no frio E' a promessa.
# ⚠️ E' clausula POSITIVA: descreve o corpo solto, nunca `not shivering`.
# Negacao injeta o token, e o token aqui e' justamente o tremor.
CALMA = (
    "Her breathing is slow and even, her jaw is relaxed and her hands stay "
    "open. She holds the posture the way someone holds it in a warm room."
)

# ⛔ O TRAJE. Maiô preto simples e nada mais. Torso nu como no video de
# referencia nao e' opcao com elenco feminino — e' recusa certa.
# ⚠️ Traje de banho por si passa (medido no parque: `bikini` aparece em 64 de
# 200 blocos do DUPLA e em 56 de 200 do TRIO, e os dois passam). O que derruba
# e' o COMPOSTO — peito nu, corpos colados, vocabulario de formato de torso.
# Aqui a geometria e' de meditacao: sentada, simetrica, maos nos joelhos.
TRAJE = ("a plain black one-piece athletic swimsuit")

# ⭐ O VAPOR DA RESPIRACAO. E' a unica prova em quadro de que faz frio de
# verdade, e e' o que ancora a fala na imagem: ela FALA sobre respiracao e o
# espectador VE a respiracao dela.
VAPOR = ("Her breath leaves her mouth in a visible plume of vapour in the "
         "cold air with every phrase.")

# ⚠️ "iPhone shot" e nao "shot on a phone": a palavra solta  e o que a
# lente GE8 procura, e ela existe porque escrever o aparelho faz o gerador
# DESENHAR o aparelho (lote perdido no VICK 16).
CAUDA_GELO = ("iPhone shot from a low angle at her eye level, natural "
              "grain, no text, no watermark.")

# ===========================================================================
# POOLS DE CENA
# ===========================================================================

# ⭐⭐ OS MUNDOS DE GELO. Cada entrada e' um lugar onde a presenca de uma
# pessoa sentada e imovel e' visualmente absurda — que e' o hook.
# ⛔ NENHUM tem ela dentro da agua. Ver a lente `GE4` e a docstring.
MUNDOS = [
    {"id": "lagoa_glacial",
     "set": "a glacial lagoon, seated on a broad flat slab of pale blue ice "
            "at the water's edge, with dozens of icebergs floating on still "
            "grey water behind her and a glacier wall far off on the horizon",
     "luz": "flat overcast Arctic daylight, no visible sun"},
    {"id": "praia_gelo_negro",
     "set": "a black volcanic sand beach strewn with chunks of clear glacier "
            "ice, seated on the largest chunk, with grey surf breaking behind "
            "her",
     "luz": "low golden light raking across the ice from the left"},
    {"id": "lingua_geleira",
     "set": "the cracked blue tongue of a glacier, seated on a level shelf of "
            "ice with deep crevasses running away behind her",
     "luz": "bright flat white daylight, heavy cloud"},
    {"id": "lago_congelado",
     "set": "the frozen surface of a mountain lake, seated at the centre of a "
            "wide sheet of dark blue ice with cracks radiating outward, bare "
            "peaks on every horizon",
     "luz": "clear blue winter light with hard shadows"},
    {"id": "boca_caverna",
     "set": "the mouth of an ice cave, seated on the ice floor just inside "
            "with the deep blue curved ceiling above and the white daylight "
            "of the entrance behind her",
     "luz": "cold blue light bouncing off the ice walls"},
    {"id": "cachoeira_congelada",
     "set": "the base of a frozen waterfall, seated on the ice mound at its "
            "foot with the great column of frozen water rising behind her",
     "luz": "dim blue shade with a bright sky above the falls"},
    {"id": "fiorde",
     "set": "the shore of a fjord in winter, seated on a snow covered boulder "
            "at the waterline with dark cliffs falling into black water "
            "behind her",
     "luz": "long low orange light near the horizon"},
    {"id": "campo_neve",
     "set": "an open snowfield, seated on a bare patch of wind-scoured ice "
            "with nothing else in any direction to the horizon",
     "luz": "flat white whiteout light with almost no shadow"},
    {"id": "rio_congelado",
     "set": "a frozen river, seated on a plate of ice mid-channel with frost "
            "covered rocks and bare black trees along both banks",
     "luz": "pale early morning light and low mist over the ice"},
    {"id": "floresta_gelada",
     "set": "a clearing in a snow-laden pine forest, seated on a flat rock "
            "under frost, the branches heavy with snow all around her",
     "luz": "soft diffuse light filtering through the trees"},
]

# ⭐⭐ AS NARRADORAS — persona NOVA, por ordem do operador. Corpo de quem
# enfrenta frio: atletica, pele marcada, cabelo molhado ou com cristais de
# gelo. ⛔ Nada do arquetipo de tricô do ATEM 16.
# ⛔ Cada entrada carrega ARQUITETURA FACIAL. E' isso, e nenhuma negacao, que
# impede o rosto de derivar para a media do treino.
REFS = [
    {"id": "trenca_molhada", "idade": 36,
     "rotulo": "36a · trança molhada, loira escura",
     "cabelo": "dark blonde hair soaked and pulled back into a single braid "
               "with frost forming on the loose strands",
     "desc": "a broad flat forehead, deep-set pale grey eyes under straight "
             "low brows, a narrow straight nose bridge with a rounded tip, a "
             "strong square jaw, high flat cheekbones reddened by the cold, "
             "small attached earlobes, and a pale scar through the left "
             "eyebrow"},
    {"id": "curto_escuro", "idade": 41,
     "rotulo": "41a · curto escuro, malar alto",
     "cabelo": "dark brown hair cut short above the ears and slicked back wet",
     "desc": "a high narrow forehead, close-set dark eyes under thick "
             "straight brows, a long nose bridge with a small bump at the "
             "top, a lean angular jaw, very prominent cheekbones, detached "
             "earlobes, and deep lines at the outer corners of both eyes"},
    {"id": "coque_gelado", "idade": 33,
     "rotulo": "33a · coque com gelo, ruiva",
     "cabelo": "copper red hair twisted into a tight wet bun with ice "
               "crystals clinging to the front hairline",
     "desc": "a low rounded forehead, wide-set green eyes under thin arched "
             "brows, a slim nose bridge with a slightly upturned tip, a "
             "rounded jaw with a square chin, subtle cheekbones, and dense "
             "freckles across the nose bridge and both cheeks"},
    {"id": "raspado_lateral", "idade": 38,
     "rotulo": "38a · lateral raspada, castanho",
     "cabelo": "mid brown hair shaved close on one side and long and wet on "
               "the other, tucked behind the shaved ear",
     "desc": "a square forehead, large round amber eyes set far apart, a wide "
             "flat nose bridge with a broad tip, a heavy square jaw, sharp "
             "high cheekbones, a pierced left ear with one small steel ring, "
             "and a raised mole below the right eye"},
    {"id": "grisalho_curto", "idade": 45,
     "rotulo": "45a · grisalho curto, pele marcada",
     "cabelo": "steel grey hair in a short wet crop pushed straight back off "
               "the forehead",
     "desc": "a wide lined forehead, hooded blue eyes under sparse straight "
             "brows, a strong straight nose bridge with a squared tip, a "
             "broad square jaw, angular cheekbones, large detached earlobes, "
             "and weathered skin with deep lines from the nose to the mouth"},
    {"id": "longo_solto", "idade": 31,
     "rotulo": "31a · longo solto, castanho claro",
     "cabelo": "light chestnut hair worn long and loose, wet and heavy down "
               "her back with frost on the ends",
     "desc": "a tall forehead, oval hazel eyes with a slight downward tilt at "
             "the outer corner, a fine narrow nose bridge with a pointed tip, "
             "a tapering jaw with a pointed chin, delicate cheekbones, and a "
             "small dark mole on the right side of the neck"},
    {"id": "rabo_alto", "idade": 34,
     "rotulo": "34a · rabo alto, preto",
     "cabelo": "black hair pulled into a high wet ponytail that hangs "
               "straight down",
     "desc": "a rounded forehead with a low hairline, deep-set dark brown "
             "eyes under full curved brows, a straight medium nose bridge "
             "with a flared base, a rounded jaw, wide high cheekbones, and a "
             "small vertical scar on the point of the chin"},
    {"id": "franja_molhada", "idade": 39,
     "rotulo": "39a · franja molhada, loira",
     "cabelo": "warm blonde hair to the jaw with a wet blunt fringe stuck "
               "flat against the forehead",
     "desc": "a broad forehead, round grey blue eyes under short arched "
             "brows, a short wide nose bridge with a rounded tip, a soft "
             "square jaw with a shallow dimple in the chin, full low "
             "cheekbones, and a pale birthmark high on the left cheek"},
]

# ⭐ O GESTO — a UNICA coisa que se move no take. Pool pequeno de proposito:
# imobilidade e' o angulo, e gesto grande num lugar como esse vira agitacao.
GESTOS = [
    "she turns both palms a little further open on her knees as she finishes",
    "she lowers her chin once, slowly, on her last word",
    "she lifts her right hand off her knee and lays it flat on her own "
    "breastbone, and leaves it there",
    "she closes her eyes for one full second in the middle of the sentence "
    "and opens them again",
    "she draws one slow breath in before she starts, her ribcage lifting "
    "visibly",
]

# ===========================================================================
# POOLS DE COPY — ALEMAO
# ===========================================================================

# ⛔⛔ COPY E' ALCADA DO OPERADOR. Estas entradas sao PROPOSTA e nao vieram de
# leitura otica — ver a divida declarada na docstring.
#
# ⭐⭐ A ESPINHA, e ela existe para resolver a tensao do angulo: a IMAGEM e'
# gelo e a OFERTA e' respiracao.
#   take 1  a imagem impossivel, e ela devolve o merito para a RESPIRACAO
#   take 2  por que o que a espectadora ja' tentou nao funcionou
#   take 3  `dafuer brauchst du kein Eis` — a barreira cai e o gelo sai
# ⛔ Sem a terceira batida o video promete frio e a VSL entrega respiracao. A
# lente `GE5` cobra que o take 3 dispense o gelo por escrito.

# ⭐ O HOOK. Toda entrada faz a MESMA virada: nega a explicacao obvia (ela e'
# durona, ela e' diferente) e devolve o merito a algo que a espectadora
# tambem tem — o proprio folego.
HOOKS = [
    "Ich sitze hier nicht, weil ich hart bin. Ich sitze hier, weil ich anders "
    "atme.",
    "Das hier ist kein Mut. Das ist Atmung, und du hast sie auch.",
    "Jeder denkt, das geht nur mit Willenskraft. Es geht mit Atmung.",
    "Mein Körper friert genauso wie deiner. Meine Atmung macht den "
    "Unterschied.",
    "Vor drei Jahren hätte ich hier keine zehn Sekunden gesessen. Heute atme "
    "ich anders.",
    "Das Eis ist nicht das Schwere daran. Das Schwere ist, ruhig zu bleiben.",
    "Ich bin nicht besonders. Ich weiß nur, wie ich atmen muss.",
    "Wer das sieht, denkt an Kälte. Es geht die ganze Zeit um Atmung.",
]

# ⭐ POR QUE FALHOU. Toda entrada nomeia UMA coisa que ela ja' tentou e diz
# por que nao pegou: aquilo trabalha na CABECA, e o problema esta' no CORPO.
# ⛔ Nada de metafora inventada. Tabletten, Ärztin, Reden, Apps sao coisas que
# a espectadora reconhece sem traducao.
MECANISMOS = [
    "Tabletten beruhigen den Kopf. Diese Atmung beruhigt den Nerv, der die "
    "Angst auslöst.",
    "Reden hilft dem Kopf. Deinem Körper hat nie jemand beigebracht, wie er "
    "runterkommt.",
    "Deine Ärztin behandelt die Angst. Niemand zeigt dir, was dein Atem damit "
    "macht.",
    "Apps zählen dir Sekunden vor. Sie erreichen den Nerv nicht, um den es "
    "geht.",
    "Du kannst dich nicht ruhig denken. Ruhe entsteht über den Atem, nicht "
    "über den Kopf.",
    "Jahre Therapie, und der Körper ist immer noch angespannt. Da kommt kein "
    "Gespräch hin.",
    "Kein Arzt findet daran etwas, weil nichts kaputt ist. Dein Atem läuft "
    "nur falsch.",
]

# ⭐⭐ A BARREIRA + O CTA, e as duas coisas na mesma fala por construcao.
# ⛔ TODA entrada dispensa o gelo (`kein Eis`, `keine Kälte`, `zu Hause`). E'
# o que impede o video de prometer uma coisa e a pagina vender outra, e a
# lente `GE5` a cobra.
CTAS = [
    "Dafür brauchst du kein Eis. Nur zwei Minuten. Kommentiere {kw} für die "
    "Methode.",
    # ⛔ REESCRITA. Dizia "ich schicke sie dir" —  sem dono e sem dizer
    # ONDE chega. A lente GE7 acusou, e ela estava certa.
    "Du brauchst keine Kälte und keine Ausrüstung. Kommentiere {kw} für die "
    "Methode.",
    "Das geht bei dir zu Hause, ohne Eis. Kommentiere {kw} und schau in deine "
    "Nachrichten.",
    "Kein Eis, kein Studio, keine Termine. Kommentiere {kw} für die Methode.",
    "Die Methode funktioniert auch im Warmen. Kommentiere {kw}, sie kommt in "
    "deine Nachrichten.",
    "Du musst dafür nirgendwo hin. Kommentiere {kw}, dann liegt sie in deinen "
    "Nachrichten.",
]

# ===========================================================================
# ⭐⭐ A COPY PAREADA — alemao canonico, portugues para o operador LER
# ===========================================================================
# ⛔ O ALEMAO E' O CANONICO. E' ele que vai para a linha `Dialogue:`; o
# portugues existe para o operador entender o que esta' aprovando.
# ⚠️ Toda entrada dos tres pools TEM de estar aqui. O autoteste cobra: pool
# sem par e' fala que o operador aprova sem ler.
PT = {
    # --- o hook ---------------------------------------------------------
    "Ich sitze hier nicht, weil ich hart bin. Ich sitze hier, weil ich anders "
    "atme.":
        "Não estou sentada aqui porque sou durona. Estou aqui porque respiro "
        "diferente.",
    "Das hier ist kein Mut. Das ist Atmung, und du hast sie auch.":
        "Isto aqui não é coragem. É respiração, e você também tem.",
    "Jeder denkt, das geht nur mit Willenskraft. Es geht mit Atmung.":
        "Todo mundo acha que isso só vai com força de vontade. Vai com "
        "respiração.",
    "Mein Körper friert genauso wie deiner. Meine Atmung macht den "
    "Unterschied.":
        "Meu corpo sente frio igual ao seu. Minha respiração é que faz a "
        "diferença.",
    "Vor drei Jahren hätte ich hier keine zehn Sekunden gesessen. Heute atme "
    "ich anders.":
        "Três anos atrás eu não aguentaria dez segundos aqui. Hoje eu respiro "
        "diferente.",
    "Das Eis ist nicht das Schwere daran. Das Schwere ist, ruhig zu bleiben.":
        "O gelo não é a parte difícil. O difícil é continuar calma.",
    "Ich bin nicht besonders. Ich weiß nur, wie ich atmen muss.":
        "Eu não sou especial. Eu só sei como preciso respirar.",
    "Wer das sieht, denkt an Kälte. Es geht die ganze Zeit um Atmung.":
        "Quem vê isso pensa em frio. O assunto o tempo todo é respiração.",

    # --- por que falhou -------------------------------------------------
    "Tabletten beruhigen den Kopf. Diese Atmung beruhigt den Nerv, der die "
    "Angst auslöst.":
        "Comprimidos acalmam a cabeça. Essa respiração acalma o nervo que "
        "dispara a ansiedade.",
    "Reden hilft dem Kopf. Deinem Körper hat nie jemand beigebracht, wie er "
    "runterkommt.":
        "Falar ajuda a cabeça. Ninguém nunca ensinou seu corpo a desacelerar.",
    "Deine Ärztin behandelt die Angst. Niemand zeigt dir, was dein Atem damit "
    "macht.":
        "Sua médica trata a ansiedade. Ninguém te mostra o que a sua "
        "respiração faz com ela.",
    "Apps zählen dir Sekunden vor. Sie erreichen den Nerv nicht, um den es "
    "geht.":
        "Aplicativos contam os segundos para você. Eles não alcançam o nervo "
        "que importa.",
    "Du kannst dich nicht ruhig denken. Ruhe entsteht über den Atem, nicht "
    "über den Kopf.":
        "Você não consegue pensar até ficar calma. A calma vem pela "
        "respiração, não pela cabeça.",
    "Jahre Therapie, und der Körper ist immer noch angespannt. Da kommt kein "
    "Gespräch hin.":
        "Anos de terapia, e o corpo continua tenso. Conversa nenhuma chega "
        "lá.",
    "Kein Arzt findet daran etwas, weil nichts kaputt ist. Dein Atem läuft "
    "nur falsch.":
        "Nenhum médico acha nada, porque não há nada quebrado. A sua "
        "respiração é que está errada.",

    # --- a barreira + CTA -----------------------------------------------
    # ⚠️ Com `{kw}` ja' resolvido para a keyword do painel — o operador ve' a
    # palavra que vai sair no video, nao um slot.
    "Dafür brauchst du kein Eis. Nur zwei Minuten. Kommentiere %(k)s für die "
    "Methode.":
        "Para isso você não precisa de gelo. Só dois minutos. Comente %(k)s "
        "para receber o método.",
    "Du brauchst keine Kälte und keine Ausrüstung. Kommentiere %(k)s für die "
    "Methode.":
        "Você não precisa de frio nem de equipamento. Comente %(k)s para "
        "receber o método.",
    "Das geht bei dir zu Hause, ohne Eis. Kommentiere %(k)s und schau in "
    "deine Nachrichten.":
        "Isso funciona na sua casa, sem gelo. Comente %(k)s e olhe nas suas "
        "mensagens.",
    "Kein Eis, kein Studio, keine Termine. Kommentiere %(k)s für die "
    "Methode.":
        "Sem gelo, sem estúdio, sem consulta. Comente %(k)s para receber o "
        "método.",
    "Die Methode funktioniert auch im Warmen. Kommentiere %(k)s, sie kommt in "
    "deine Nachrichten.":
        "O método funciona no calor também. Comente %(k)s, ele chega nas suas "
        "mensagens.",
    "Du musst dafür nirgendwo hin. Kommentiere %(k)s, dann liegt sie in "
    "deinen Nachrichten.":
        "Você não precisa ir a lugar nenhum. Comente %(k)s, e ele fica nas "
        "suas mensagens.",
}


def traduzir(fala):
    """O portugues de uma fala alema, ou None se ela nao tem par.

    ⛔ Devolve None de proposito quando nao conhece. O painel mostra isso em
    vermelho; inventar traducao aqui seria deixar o operador aprovar uma fala
    que ele nao leu.
    """
    for de, pt in PT.items():
        if de % {"k": KEYWORD} == fala:
            return pt % {"k": KEYWORD}
    return None


# ⭐ A flag que o `ui_agente` le' por `getattr`. Motor que nao a declara nao
# ve' diferenca nenhuma — o acrescimo no painel e' ADITIVO.
COPY_PAREADA = True


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

# ⭐ ~1/3 do pool, para o ledger preferir sem travar.
MEMORIA = {"mundo": 3, "ref": 3, "gesto": 2, "hook": 3, "mecanismo": 2,
           "cta": 2}


def _carregar_ledger():
    try:
        with io.open(LEDGER, encoding="utf-8") as f:
            return json.load(f)
    except (IOError, OSError, ValueError):
        return {}


def _gravar_ledger(led, spec, em_disco=True):
    """Anota na memoria e, se pedido, grava em disco.

    ⛔ `em_disco` herdado do ATEM 16: o `--dry-run` pulava esta funcao inteira
    e a memoria ficava inerte DENTRO da rodada, fazendo um lote de revisao
    sair muito mais pobre do que o motor e'. A memoria SEMPRE anota; so' o
    disco e' poupado.
    """
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
    """⚠️ O fallback e' obrigatorio: ledger e' preferencia, nunca condicao."""
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

    mundo = _pega("mundo", MUNDOS, "id")
    ref = _pega("ref", REFS, "id")
    gesto = _evitando(rng, GESTOS, led.get("gesto", []))
    hook = _evitando(rng, HOOKS, led.get("hook", []))
    mec = _evitando(rng, MECANISMOS, led.get("mecanismo", []))
    cta = _evitando(rng, CTAS, led.get("cta", []))

    return {
        "pagina": pagina, "etnia": et,
        "mundo": mundo, "ref": ref, "gesto": gesto,
        "falas": [hook.strip(), mec.strip(),
                  cta.replace("{kw}", KEYWORD).strip()],
        "_id_mundo": mundo["id"], "_id_ref": ref["id"], "_id_gesto": gesto,
        "_id_hook": hook, "_id_mecanismo": mec, "_id_cta": cta,
    }

# ===========================================================================
# MONTAGEM
# ===========================================================================

def montar(spec):
    ref, mundo, et = spec["ref"], spec["mundo"], spec["etnia"]
    f = spec["falas"]
    anc = "%s, %s" % (ref["desc"], ref["cabelo"])

    # ⛔⛔ A VOZ E' TRAVADA E REPETIDA NOS TRES TAKES. Cada take e' uma chamada
    # separada e o modelo nao ve' o anterior — pedir "a mesma voz" e' anafora
    # sem antecedente. E ela declara ALEMA NATIVA, senao o TTS le' alemao com
    # fonemas ingleses.
    # ⭐ `steady and unhurried despite the cold` faz trabalho de CENA: voz
    # tremida contradiria a calma que o quadro promete.
    voz = ("Voice: one calm German woman in her late thirties speaking NATIVE "
           "GERMAN with a neutral standard German accent, pitched low and "
           "steady and unhurried despite the cold, close to the microphone at "
           "ordinary conversational volume, never raised and never whispered, "
           "speaking at the ordinary pace of everyday German speech. The "
           "pitch, the texture, the accent and the speed are identical in all "
           "three takes.")

    b = {}
    b["BLOCO 0 (REF)"] = (
        "REF 01: Photo of a real person: a head and shoulders portrait of a "
        "%d-year-old %s woman, %s. Plain neutral grey background, soft even "
        "frontal light, the head upright and facing the lens. Slight sensor "
        "grain, raw amateur photo look. No on-screen text, no subtitles, no "
        "captions, no watermark." % (ref["idade"], et, anc))

    # ⭐ OS TRES QUADROS SAO O MESMO LUGAR. O angulo e' uma imagem so', e
    # trocar de mundo no meio de 24s desperdiça a unica coisa que ele tem.
    # O que muda entre eles e' o ENQUADRAMENTO: aberto, medio, fechado.
    base = ("%%s %s She is a %d-year-old %s woman, %s, wearing %s, %s. %s %s"
            % ("%s", ref["idade"], et, anc, TRAJE, POSE, CALMA, CAUDA_GELO))

    # ⛔⛔ O ROTULO `IMAGE 0n/03:` E' OBRIGATORIO. O parser da AdBatch separa
    # os blocos por ele; sem ele o lote inteiro entra como um bloco so'.
    # ⚠️ Ele JA' FALTOU: o autoteste cravava 0 ERRO em 400 sorteios enquanto
    # os tres quadros saiam sem cabecalho em 100% dos videos, porque as lentes
    # cobravam orientacao e cauda e nunca o rotulo. A `GE14` existe por isso.
    # ⭐ E os tres sao montados por LACO, nao por tres expressoes com
    # `.replace()` encadeado — foi nesse encadeamento que o rotulo sumiu.
    planos = ("Wide shot with her small in the frame and the place large "
              "around her.",
              "Medium shot framing her from the knees up.",
              "Closer shot framing her from the waist up.")
    lugar = mundo["set"].capitalize() + ", " + mundo["luz"] + "."
    for k, plano in zip(IMAGENS, planos):
        b[k] = ("%s: %s %s %s She is a %d-year-old %s woman, %s, wearing %s, "
                "%s. %s %s"
                % (k, ORIENTACAO, lugar, plano, ref["idade"], et, anc,
                   TRAJE, POSE, CALMA, CAUDA_GELO))

    for i, k in enumerate(TAKES):
        # ⛔ O GESTO E' A UNICA COISA QUE SE MOVE, e so' no take 1. Nos outros
        # dois ela fica imovel: imobilidade num lugar como esse E' o angulo, e
        # movimento demais vira agitacao.
        # ⚠️ Maiuscula: o gesto nasce em minuscula no pool porque la' ele e'
        # uma oracao solta, e aqui entra logo depois de um ponto.
        g = spec["gesto"]
        mov = ((g[:1].upper() + g[1:]) if i == 0
               else "She does not move except to speak")
        b[k] = ("%s: Animate the image exactly. Locked-off shot on a tripod, "
                "no handheld movement and no cuts. She speaks calmly straight "
                "into the lens. %s. Her posture does not change, her hands "
                "stay open on her knees, her shoulders stay down and her "
                "back stays straight the whole time. %s Nothing else in the frame "
                "moves except drifting ice and water far behind her.\n"
                'Dialogue: "%s"\n%s\n'
                "Audio: wind over ice and distant water only. No music."
                % (k, mov, VAPOR, f[i], voz))
    return b

# ===========================================================================
# LENTES
# ===========================================================================

# ⛔ Toda lente devolve ("ERRO", msg) ou ("AVISO", msg). ERRO aborta o video
# ANTES de ele ser impresso — video com erro que chega a tela e' video que o
# operador copia.

# ⛔⛔ GE4 — ELA NUNCA ENTRA NA AGUA. Ordem do operador e decisao de seguranca:
# respiracao seguida de imersao em agua fria e' o mecanismo do desmaio de
# aguas rasas, que mata gente que sabe nadar. Um criativo que mostra alguem
# respirando dentro de agua gelada convida a copia, e a copia mata.
_IMERSAO = re.compile(
    r"\b(?:in(?:to)?|under)\s+(?:the\s+)?(?:water|lagoon|lake|river|sea|ocean)\b"
    r"|\bsubmerged\b|\bimmersed\b|\bwaist\s+deep\b|\bchest\s+deep\b"
    r"|\bplunge\w*\b|\bwades?\b|\bswims?\b|\bbathing\b",
    re.I)

# ⛔⛔ GE13 — TORSO NU NUNCA. O video de referencia e' um homem sem camisa; com
# elenco feminino isso e' recusa certa. O `TRAJE` e' string travada e a lente
# cobra o outro lado: nenhuma palavra de nudez entra no bloco.
_NUDEZ = re.compile(
    r"\btopless\b|\bbare[- ]chested\b|\bshirtless\b|\bnude\b"
    r"|\bnaked\b|\bbare\s+(?:breasts?|chest|torso)\b", re.I)

# ⛔ GE3 — O CORPO NAO REAGE AO FRIO. Sem isto o gerador desenha a reacao
# obvia (ombros subidos, bracos cruzados, careta) e o quadro passa a dizer o
# contrario da fala. A calma no frio E' a promessa do angulo.
_ENCOLHIDA = re.compile(
    r"\bshiver\w*\b|\btrembl\w*\b|\bhunch\w*\b|\bhugging\s+herself\b"
    r"|\barms\s+crossed\b|\bgrimac\w*\b|\bwincing\b"
    r"|\bteeth\s+chattering\b", re.I)

# ⭐⭐ GE5 — O TAKE 3 DISPENSA O GELO, POR ESCRITO. E' a lente mais importante
# do motor. A IMAGEM e' gelo e a OFERTA e' respiracao: sem esta batida o video
# promete frio e a VSL entrega outra coisa, e o clique morre na pagina.
_SEM_GELO = re.compile(
    r"\bkein\w*\s+eis\b|\bkeine\s+kält?e\b|\bzu\s+hause\b"
    r"|\bim\s+warmen\b|\bnirgendwo\s+hin\b|\bauch\s+im\s+warmen\b",
    re.I)

# ⛔ GE10 — a tecnica e' a moeda. Se o video ensina o padrao, nao ha' motivo
# para comentar.
_ENSINA = re.compile(
    r"\b(?:vier|fünf|sechs|sieben|acht|zwei|drei|\d+)\s+(?:sekunden|atemzüge)\b"
    r"|\batme\s+(?:tief\s+)?(?:ein|aus)\b|\bhalte\s+den\s+atem\b"
    r"|\bzähl(?:e|st)?\s+bis\b", re.I)

# ⛔ GE9 — alegacao de cura e tratamento. Ansiedade pode ser NOMEADA (ordem do
# operador); prometer curar e' o que morde sob a HWG alema.
_MOLDURA = re.compile(
    r"\bangststörung\w*\b|\bpanikstörung\w*\b|\bdiagnose\w*\b"
    r"|\bheil(?:en|ung|t)\b|\btherapiert\b|\bkrankheit\b|\bgeheilt\b"
    r"|\bbehandl\w*\b", re.I)

# ⛔ GE8 — a municao que a varredura de 2026-08-14 tirou de 30 arquivos, e o
# aparelho que o VICK 16 pagou com um lote inteiro.
_ANTICELEB = re.compile(
    r"\bnot\s+(?:a\s+)?(?:celebrity|celebrities|famous|model|models|actor|actors)\b"
    r"|\bno\s+celebrit", re.I)
_APARELHO = re.compile(
    r"\b(?:phone|smartphone|handy|filming|records?\s+her)\b", re.I)


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

    for k in IMAGENS:
        if ORIENTACAO not in blocos[k]:
            ach.append(("ERRO", "GE1: %s sem a orientacao vertical." % k))
        if CAUDA_GELO not in blocos[k]:
            ach.append(("ERRO", "GE1: %s sem a cauda de textura." % k))
        if not blocos[k].startswith(k + ":"):
            ach.append(("ERRO", "GE14: %s nao comeca com o proprio rotulo. "
                                "O parser da AdBatch separa os blocos por "
                                "esse cabecalho — sem ele o lote entra como "
                                "um bloco so'." % k))
        if POSE not in blocos[k] or CALMA not in blocos[k]:
            ach.append(("ERRO", "GE2: %s sem a pose ou sem a clausula de "
                                "calma — o corpo solto num lugar que deveria "
                                "encolher qualquer um E' o angulo." % k))
        if TRAJE not in blocos[k]:
            ach.append(("ERRO", "GE13: %s sem o traje travado." % k))

    if _IMERSAO.search(direcoes):
        ach.append(("ERRO", "GE4: alguem entra na agua. Respiracao mais "
                            "imersao e' o mecanismo do desmaio de aguas "
                            "rasas — ela senta SOBRE o gelo, sempre."))
    if _NUDEZ.search(direcoes):
        ach.append(("ERRO", "GE13: vocabulario de nudez no prompt."))
    if _ENCOLHIDA.search(direcoes):
        ach.append(("ERRO", "GE3: o corpo reage ao frio. A calma no frio e' a "
                            "promessa; corpo encolhido diz o contrario da "
                            "fala."))
    if not _SEM_GELO.search(f[2]):
        ach.append(("ERRO", "GE5: o take 3 nao dispensa o gelo. A imagem e' "
                            "gelo e a oferta e' respiracao — sem esta batida "
                            "o video promete frio e a VSL entrega outra "
                            "coisa."))
    for i in (0, 1, 2):
        if _ENSINA.search(f[i]):
            ach.append(("ERRO", "GE10: a fala %d ENSINA o padrao. A tecnica e' "
                                "a moeda." % (i + 1)))
        if _MOLDURA.search(f[i]):
            ach.append(("ERRO", "GE9: a fala %d alega cura ou tratamento."
                        % (i + 1)))
        n = silabas_frase(f[i])
        if n > TETO_SILABAS:
            ach.append(("ERRO", "GE6: a fala %d tem %d silabas (teto %d) — "
                                "nao cabe em 8s e sai cortada no render."
                        % (i + 1, n, TETO_SILABAS)))
        elif n > TETO_SILABAS - 3:
            ach.append(("AVISO", "GE6: a fala %d tem %d silabas, no limite."
                        % (i + 1, n)))

    if KEYWORD not in f[2]:
        ach.append(("ERRO", "GE7: a keyword `%s` nao esta' no CTA." % KEYWORD))
    if not re.search(r"\bnachricht\w*\b|\bmethode\b", f[2], re.I):
        ach.append(("ERRO", "GE7: o CTA nao diz o que ela recebe nem onde."))
    if _sc_trocar is not None and _sc_trocar(f[2], KEYWORD, "PROBE") == f[2]:
        ach.append(("ERRO", "GE11: a keyword nao e' trocavel — o campo do "
                            "painel ficaria mudo."))
    if _ANTICELEB.search(todos):
        ach.append(("ERRO", "GE8: negacao de celebridade — ela INJETA o token "
                            "que se quer evitar."))
    if _APARELHO.search(direcoes):
        ach.append(("ERRO", "GE8: aparelho na direcao de cena — o gerador o "
                            "DESENHA (lote perdido no VICK 16)."))
    n = sum(1 for k in IMAGENS if spec["ref"]["desc"] in blocos[k])
    if n < 3:
        ach.append(("ERRO", "GE12: a ancora de rosto esta' em %d de 3 quadros "
                            "— os tres sao geracoes separadas." % n))
    return ach

# ===========================================================================
# UI
# ===========================================================================

EIXOS_UI = [
    ("mundo", "MUNDO DE GELO", "MUNDOS", "id"),
    ("ref", "NARRADORA", "REFS", "id"),
]

# ⭐ Fixa a narradora para todo sorteio — e' ele que da' FUNCAO ao campo
# `rotulo` dos 8 REFs. Forma sem funcao e' o defeito que este repo mais paga.
DROPDOWNS_UI = [("ref", "NARRADORA", "REFS", "rotulo")]

PT_MUNDO = {
    "lagoa_glacial": "Na lagoa glacial",
    "praia_gelo_negro": "Na praia de areia negra com gelo",
    "lingua_geleira": "Na língua da geleira",
    "lago_congelado": "No lago congelado",
    "boca_caverna": "Na boca da caverna de gelo",
    "cachoeira_congelada": "Na cachoeira congelada",
    "fiorde": "Na margem do fiorde",
    "campo_neve": "No campo de neve aberto",
    "rio_congelado": "No rio congelado",
    "floresta_gelada": "Na clareira da floresta gelada",
}


def resumo_pt(spec):
    f = spec["falas"]
    return ("%s · página %s (%s)\n"
            "  MUNDO      %s\n"
            "  NARRADORA  %s\n"
            "  fala 1     %d sílabas / %d palavras\n"
            "  fala 2     %d sílabas / %d palavras\n"
            "  fala 3     %d sílabas / %d palavras"
            % (TITULO, spec["pagina"], spec["etnia"],
               PT_MUNDO.get(spec["mundo"]["id"], spec["mundo"]["id"]),
               spec["ref"]["rotulo"],
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

    rng = random.Random(20260902)
    led = {}
    erros, avisos = [], []
    vistos = {e: set() for e in MEMORIA}
    pior = [0, 0, 0]
    falas = [set(), set(), set()]
    maior = 0

    for _ in range(n):
        s_ = sortear(rng.choice(sorted(ETNIA)), rng, led, None)
        b = montar(s_)
        for nivel, msg in lint(s_, b):
            (erros if nivel == "ERRO" else avisos).append(msg)
        for e in MEMORIA:
            vistos[e].add(s_["_id_%s" % e])
        for i in (0, 1, 2):
            pior[i] = max(pior[i], silabas_frase(s_["falas"][i]))
            falas[i].add(s_["falas"][i])
        maior = max(maior, max(len(v) for v in b.values()))
        _gravar_ledger(led, s_, em_disco=False)

    print("\n1. LENTES")
    print("   ERRO  : %d" % len(erros))
    for m in sorted(set(erros))[:8]:
        print("      - %s" % m)
    print("   AVISO : %d (%d distintos)" % (len(avisos), len(set(avisos))))
    for m in sorted(set(avisos))[:4]:
        print("      - %s" % m)

    print("\n2. ALCANCE DOS POOLS")
    tam = {"mundo": len(MUNDOS), "ref": len(REFS), "gesto": len(GESTOS),
           "hook": len(HOOKS), "mecanismo": len(MECANISMOS), "cta": len(CTAS)}
    mortos = 0
    for e in sorted(tam):
        viv = len(vistos[e])
        if viv != tam[e]:
            mortos += 1
        print("   %s %-10s %2d/%2d" % ("ok " if viv == tam[e] else "MOR",
                                       e, viv, tam[e]))
    if mortos:
        print("   ⛔ %d pool(s) com entrada inalcancavel." % mortos)

    print("\n3. TETO FISICO DE FALA (silabas, teto %d)" % TETO_SILABAS)
    for i in (0, 1, 2):
        print("   cena %d: maximo %2d silabas · %d falas distintas"
              % (i + 1, pior[i], len(falas[i])))

    print("\n4. TAMANHO DE BLOCO (teto da AdBatch: 3.900 caracteres)")
    print("   maior bloco gerado: %d caracteres" % maior)

    print("\n5. CONTROLE NEGATIVO — as lentes acusam o defeito plantado?")
    plantios = [
        ("GE4", lambda sp, bl: bl.__setitem__(
            "IMAGE 01/03", bl["IMAGE 01/03"] + " She is submerged in the water.")),
        ("GE13", lambda sp, bl: bl.__setitem__(
            "IMAGE 02/03", bl["IMAGE 02/03"] + " She is bare-chested.")),
        ("GE3", lambda sp, bl: bl.__setitem__(
            "IMAGE 03/03", bl["IMAGE 03/03"] + " She is shivering hard.")),
        ("GE5", lambda sp, bl: sp["falas"].__setitem__(
            2, "Kommentiere %s für die Methode." % KEYWORD)),
        ("GE10", lambda sp, bl: sp["falas"].__setitem__(
            0, "Atme vier Sekunden ein und wieder aus.")),
        ("GE9", lambda sp, bl: sp["falas"].__setitem__(
            1, "Das heilt deine Angststörung für immer.")),
        ("GE8", lambda sp, bl: bl.__setitem__(
            "IMAGE 01/03", bl["IMAGE 01/03"] + " Ordinary face, not a celebrity.")),
        ("GE12", lambda sp, bl: bl.__setitem__(
            "IMAGE 03/03", bl["IMAGE 03/03"].replace(sp["ref"]["desc"], "a face"))),
        ("GE14", lambda sp, bl: bl.__setitem__(
            "IMAGE 01/03",
            bl["IMAGE 01/03"].replace("IMAGE 01/03: ", "", 1))),
        ("GE2", lambda sp, bl: bl.__setitem__(
            "IMAGE 02/03", bl["IMAGE 02/03"].replace(CALMA, ""))),
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
        print("   %s %-5s plantado 40x, acusado %d/40"
              % ("ok " if pegou == 40 else "FALHA", nome, pegou))

    print("\n6. TRADUCAO — toda entrada dos tres pools tem par em PT?")
    faltam = []
    for pool, rot in ((HOOKS, "hook"), (MECANISMOS, "mecanismo"),
                      (CTAS, "cta")):
        for e in pool:
            if traduzir(e.replace("{kw}", KEYWORD)) is None:
                faltam.append("%s: %s" % (rot, e[:52]))
    print("   entradas sem par: %d de %d"
          % (len(faltam), len(HOOKS) + len(MECANISMOS) + len(CTAS)))
    for x in faltam[:6]:
        print("      - %s" % x)
    if faltam:
        erros.append("TRADUCAO: %d entradas sem par em PT — o operador "
                     "aprovaria fala que nao leu." % len(faltam))

    print("\n7. SILABAS — o contador contra casos conhecidos")
    for palavra, esperado in (("Eis", 1), ("Atmung", 2), ("Kälte", 2),
                              ("Nachrichten", 3), ("Methode", 3),
                              ("Willenskraft", 3)):
        got = silabas(palavra)
        print("   %s %-14s %d (esperado %d)"
              % ("ok " if got == esperado else "!! ", palavra, got, esperado))

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
    ap.add_argument("--pagina", choices=sorted(ETNIA), default="kim")
    ap.add_argument("--n", type=int, default=1)
    ap.add_argument("--seed", type=int)
    ap.add_argument("--mundo", choices=[x["id"] for x in MUNDOS])
    ap.add_argument("--ref", choices=[x["id"] for x in REFS])
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--autoteste", action="store_true")
    a = ap.parse_args()

    if a.autoteste:
        return autoteste()

    led = _carregar_ledger()
    rng = random.Random(a.seed)
    travas = {}
    if a.mundo:
        travas["mundo"] = a.mundo
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
