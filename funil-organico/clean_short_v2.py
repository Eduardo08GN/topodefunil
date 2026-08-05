#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
clean_short_v2.py — randomizador + gerador + linter do AGENTE CLEAN **V2**.

⭐⭐ ESTE ARQUIVO E' UMA COPIA DO `clean_short.py` (2026-08-03), por ordem
literal do operador: *"voce NAO ira sobrescrever o clean short, voce ira COPIAR
o clean short atual, acrescentar tais alteracoes e criar o CLEAN SHORT V2"*.
O v1 fica INTACTO e continua sendo a fonte da verdade do CLEAN v1; este
arquivo e' a fonte da verdade do CLEAN V2. Ledger proprio
(`.clean-short-v2-ledger.json`), app proprio (`clean_short_v2_app.py`).

AS TRES MUDANCAS DO V2 (e so' elas — o resto e' copia caractere por caractere):

 [1] ⛔⛔ ETNIA LIVRE — A CONGRUENCIA DE ETNIA ESTA' DELIBERADAMENTE SUSPENSA
     NESTE V2, POR ORDEM DO OPERADOR, EM 2026-08-03.
     No v1 (e nos outros nove motores) a etnia do REF vem da PAGINA
     (`ETNIA[pagina]`), e o repo chama isso de congruencia INVIOLAVEL: REF =
     etnia do avatar da pagina. Aqui a etnia e' sorteada LIVRE do pool `ETNIAS`,
     sem nenhuma amarra com a pagina. O operador tomou a decisao com o
     trade-off na mesa e mandou nao reabrir: o video pode sair com REF de etnia
     diferente da do avatar da pagina em que vai ser postado, e essa
     incongruencia e' aceita.
     ⚠️ O dict `ETNIA` CONTINUA AQUI e nao pode sair: o seletor `pele
     clara/escura` do `ui_agente.py` le' `motor.ETNIA` para agrupar as paginas
     (`paginas_por_pele`), e sem ele o painel quebra. O que mudou e' que o
     motor nao USA mais `ETNIA[pagina]` para montar o REF.

 [2] ⭐⭐ TOGGLE DE TRAVA POR EIXO (`EIXOS_TRAVAVEIS`) — o painel desenha um
     cadeado ao lado de cada `trocar`. Cadeado fechado = aquele eixo NAO e'
     re-sorteado no SORTEAR VIDEO; o valor volta identico. O contrato e'
     generico e mora no `ui_agente.py`, atras de
     `getattr(motor, "EIXOS_TRAVAVEIS", [])` — os outros nove motores nao
     declaram nada e seguem intactos.
     ⚠️ A trava NAO e' "congelar a chave do spec e pronto": `item_a`, `item_b`
     e `truque` MANDAM na bancada, no despejo e na fala da cena 2. Travar so' a
     chave deixaria a copy falando de um item que nao esta' em cena (CL20). Por
     isso a trava entra em `sortear()` como `travas`, e o motor remonta o
     video inteiro em volta do valor travado.

 [3] ⛔ CONSERTO DO BOTAO `QUEM FALA` (bug achado na v1 e nao consertado la',
     por ordem do operador). O `EIXOS_UI` apontava o eixo `ref` para o pool
     `REFS_M` FIXO, enquanto `sortear()` usa `REFS_H if sexo == "homem" else
     REFS_M`: com homem selecionado, o botao `trocar` oferecia as MULHERES.
     Aqui o pool virou o callable `refs_do_sexo(spec)`, marcado com
     `.recebe_spec = True` — convencao nova do `ui_agente._pool`, aditiva: os
     pools callable dos outros motores (`homens_de(pagina)`,
     `mulheres_de(pagina)`) nao tem a marca e continuam recebendo a pagina.

 ⭐ E o painel ganhou os eixos que faltavam: `etnia`, `item_a`, `item_b` e
    `truque` — sem eles nao havia como trocar a receita sem re-sortear o video
    inteiro, que e' a dor que motivou o toggle.

--- doutrina herdada do v1, sem uma virgula de diferenca ---

A fileira apontada: profissional de saude sozinha(o) de scrub, uma fileira de
itens comestiveis na bancada, e o dedo ligando cada item a um beneficio.
ZERO prop falico, ZERO anatomia, ZERO vitima.

Fonte: Valentina Health & Wellness, 2 reels (13,3k e 7,1k comentarios).
Doutrina: AGENTE_ED_CLEAN_V1.md · concorrentes/clean-mapa-visual.md

⭐ SHORT NATIVO — 3 cenas de 8s. Nao deriva de motor longo e nao tera versao
longa (CL16). Duas FAMILIAS de cena, uma copy so':

    aponta   ela so' aponta, a bancada nao muda em nenhuma das 3 cenas
    preparo  ela PREPARA nas cenas 1 e 2 — um ingrediente por cena — e a
             cena 3 e' so' o resultado pronto ao lado da gelatina (CL17)

⭐ SEXO E' TRAVA, NAO SORTEIO (ordem do operador, 2026-08-02): o painel deixa
pre-selecionar homem/mulher e a escolha nao e' re-sorteada.

Uso:
    python funil-organico/clean_short.py --pagina chuck --n 1
    python funil-organico/clean_short.py --pagina ray --n 3 --seed 42 --dry-run
"""

import argparse
import collections
import json
import os
import random
import re

import short_comum as sc
from nucleo_sonoro import sonorizar

AQUI = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(AQUI, ".clean-short-v2-ledger.json")

TITULO = "AGENTE CLEAN V2"
SLUG = "clean-short-v2"
SUBTITULO = ("a fileira apontada, em 3 cenas · etnia livre + trava por eixo · "
             "gerador offline de prompts Veo")

# ⛔⛔ FORMATO ALINHADO AOS OUTROS NOVE MOTORES EM 2026-08-03. Este era o unico
# `ETNIA` que guardava DICT por pagina (`{"dominio": ..., "etnia": "branco"}`).
#
# O QUE ISSO QUEBRAVA, e o operador achou no app: o seletor `pele clara/escura`
# do `ui_agente.py` classifica com `"white" in ETNIA[pagina]`. Com string isso
# testa SUBSTRING e funciona; com dict testa CHAVE, nao acha `white` em lugar
# nenhum, e TODA pagina cai em `escura`. Resultado: o botao nao respondia e o
# agente so' gerava REF de pele escura.
# ⚠️ O campo `dominio` nao era lido em lugar nenhum do motor — so' o `["etnia"]`
# era usado, uma vez. Entao alinhar nao perdeu informacao nenhuma.
ETNIA = {
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
# ⭐⭐ V2 — ETNIA LIVRE (ordem do operador, 2026-08-03)
# ---------------------------------------------------------------------------
# ⛔ A congruencia REF = etnia do avatar da pagina — chamada de INVIOLAVEL no
# CLAUDE.md — esta' SUSPENSA neste v2, deliberadamente e por ordem dele, com o
# trade-off na mesa. A etnia do REF nao vem mais de `ETNIA[pagina]`: sai daqui,
# sorteada, e nao olha para a pagina.
# ⚠️ O dict `ETNIA` acima FICA: `ui_agente.paginas_por_pele` o le' para agrupar
# as paginas no seletor `pele clara/escura`, e sem ele o painel quebra.
#
# FORMATO: adjetivo pronto para entrar na frase que o motor ja' escreve —
# `"a %d-year-old %s %s" % (idade, etnia, man/woman)`. Por isso todas as
# entradas sao NEUTRAS EM GENERO ("Hispanic American", nunca "Latino"): o mesmo
# pool serve os REFS_M e os REFS_H, e "a 44-year-old Latino woman" sai errado.
#
# ⭐ 2026-08-03 — ESTA LISTA DEIXOU DE SER O EIXO. A etnia agora sai do MUNDO
# sorteado (`MUNDOS[i]["etnias"]`), porque etnia e nicho visual nao sao
# independentes — ver o bloco MUNDOS. O que sobrou para esta lista e' um papel
# so': ela e' o pool das etnias do consultorio moderno, o unico mundo que
# comporta as catorze (`"etnias": "todas"`).
ETNIAS = [
    "white American",
    "Black American",
    "Hispanic American",
    "Mexican American",
    "Puerto Rican American",
    "Caribbean American",
    "Asian American",
    "Filipino American",
    "Vietnamese American",
    "South Asian American",
    "Middle Eastern American",
    "Native American",
    "Pacific Islander American",
    "mixed-race American",
]

# ---------------------------------------------------------------------------
# ⭐ TRAVAS — eixos que o operador PRE-SELECIONA e o sorteio nao mexe
# ---------------------------------------------------------------------------
# Contrato lido pela ui_agente: [(chave, rotulo, [opcoes])]. O painel desenha um
# botao por opcao, e sortear() respeita o que estiver travado.
TRAVAS_UI = [
    ("sexo", "quem fala", ["homem", "mulher"]),
    ("familia", "cena", ["aponta", "preparo"]),
]

# ---------------------------------------------------------------------------
# ⭐⭐ V2 — EIXOS TRAVAVEIS (o cadeado do painel)
# ---------------------------------------------------------------------------
# Contrato novo, lido pela ui_agente com `getattr(motor, "EIXOS_TRAVAVEIS", [])`
# — os outros nove motores nao declaram e nao veem cadeado nenhum.
# Cada chave daqui e' aceita por `sortear()` dentro de `travas`, e o sorteio
# remonta o video INTEIRO em volta do valor travado. E' por isso que a trava
# nao pode ser "congelar a chave depois do sorteio": `item_a`, `item_b` e
# `truque` mandam na bancada (CL20), no despejo (CL17) e na fala da cena 2.
# ⚠️ `mundo` no lugar do antigo `cenario`: travar o cenario sozinho deixou de
# fazer sentido quando cenario, etnia, traje, luz e ambiencia passaram a ser a
# MESMA escolha. Travado o mundo, a etnia continua sorteando DENTRO dele.
EIXOS_TRAVAVEIS = ["familia", "mundo", "etnia", "ref",
                   "item_a", "item_b", "truque"]

# ⭐⭐ TRAVA DE PELE (2026-08-05, ordem do operador: *"quando eu travo a cor da
# pele para negro ou branco... preciso que sempre respeite"*).
# O seletor clara/escura do painel era um botao MORTO neste motor: ele troca a
# PAGINA, e o V2 ignora `ETNIA[pagina]` de proposito (etnia livre, sorteada de
# dentro do MUNDO). O operador clicava, o botao acendia, e o sorteio seguia
# aleatorio — pior que nao ter botao, porque PARECIA travado.
# Contrato aditivo, lido pela ui_agente com getattr: motor sem a flag nao muda.
PELE_TRAVAVEL = True

# ⭐ O painel formata o `{o}` dos rotulos de eixo com o orgao do sorteio
# (`your Johnson ready`, nunca `your {o} ready`). Opt-in por ordem do operador
# (2026-08-05): a correcao e' SO' do V2; o V1 fica exatamente como estava.
ROTULO_FORMATA_O = True


# ⛔⛔ A CLASSIFICACAO E' LISTA EXPLICITA, NUNCA "tudo que nao e' branco"
# (print de campo 2026-08-05): a primeira versao herdou a regra binaria do
# paginas_por_pele — clara = tem `white`, escura = o resto — e o operador
# travou `escura` e recebeu um REF Asian American. Para ele, escura = NEGRO.
# Asiatico, latino, mediterraneo, nativo e mestico nao sao nem clara nem
# escura: so' saem com a pele LIVRE.
PELE_ETNIAS = {
    "escura": ("Black American", "West African", "Jamaican American",
               "Caribbean American", "Creole American"),
    "clara": ("white American", "Cajun American"),
}


def _pele_de(etnia):
    """A pele da etnia pela lista explicita — ou None (neutra, so' no livre)."""
    for pele, ets in PELE_ETNIAS.items():
        if etnia in ets:
            return pele
    return None


# ⛔⛔ O NOME DA ETNIA NAO ANCORA A PELE (print de campo, 2026-08-05). Com a
# pele travada em `escura` o sorteio entregou `Caribbean American` — que ESTA'
# certo na lista — e o gerador devolveu quatro homens de pele clara: ele leu a
# etnia como NACIONALIDADE, nao como cor. Ordem do operador: *"no prompt nao
# esta' especificando para gerar uma pessoa negra, isso deve estar setado no
# bloco 0 de ref e nas 3 imagens caso seja travado"*.
# ⚠️ Duas ancoras, porque uma so' ja' provou ser fraca: a PALAVRA da raca antes
# da etnia (`Black Caribbean American`) e a CLAUSULA DE TOM logo depois
# (`deep brown skin`). Mesma logica do CL25: o que o gerador nao recebe, ele
# inventa — e o que ele recebe uma vez so', ele negocia.
# ⛔ So' com a pele TRAVADA. No sorteio livre a etnia continua saindo crua e a
# ambiguidade e' proposital: e' o repertorio que o eixo MUNDO existe para dar.
PELE_PROMPT = {
    "escura": ("Black", "deep brown skin"),
    "clara": ("White", "fair skin"),
}


def _comporta(mundo, pele):
    """O mundo tem alguma etnia daquela pele? ⚠️ Funcao de MODULO, nao closure:
    `sortear` e `_apos_mundo` decidem a mesma coisa e duas copias divergiriam
    (P9). Sem pele travada todo mundo comporta."""
    return not pele or any(_pele_de(e) == pele for e in mundo["etnias"])


def _mundo_da_pele(mundo, pele, rng):
    """Troca o mundo pelo mais proximo que COMPORTA a pele — mesma familia de
    preferencia. ⛔ A pele travada e' soberana: entre respeitar o mundo e
    respeitar a pele, quem cede e' o mundo (mesmo precedente do truque)."""
    if _comporta(mundo, pele):
        return mundo
    return rng.choice(
        [x for x in MUNDOS if x["familia"] == mundo["familia"]
         and _comporta(x, pele)]
        or [x for x in MUNDOS if _comporta(x, pele)])


def _etnia_visivel(etnia, pele):
    """(etnia como o prompt diz, clausula de tom) — o par de ancoras da pele.

    ⚠️ Sem duplicar a palavra: `Black American` e `white American` ja' a
    carregam, e `Black Black American` e' o tipo de frase que faz o gerador
    desconfiar do prompt inteiro."""
    if not pele:
        return etnia, ""
    palavra, tom = PELE_PROMPT[pele]
    if palavra.lower() in etnia.lower():
        return etnia, tom
    return "%s %s" % (palavra, etnia), tom

# ---------------------------------------------------------------------------
# STRINGS TRAVADAS — copia literal da doutrina. NAO REESCREVER.
# ---------------------------------------------------------------------------

# CL1 — ela/ele NUNCA toca em nada. E' o que torna o SHORT viavel: sem
# manipulacao nao ha' risco de continuidade entre blocos de 8s gerados
# separadamente (F12b: o Veo solta o objeto da mao).
# ⚠️ 2026-08-03 — A SUPERFICIE VIROU SLOT (`%s` no lugar do literal `counter`)
# nas quatro strings travadas abaixo e nos blocos. NAO e' reescrita de string
# validada: com o mundo clinico o slot recebe `counter` e o texto renderizado
# sai identico ao de antes, caractere por caractere — e' o que o `--autoteste`
# cobra em 400 videos. O slot existe porque um alpendre de pantano nao tem
# `counter`, e mandar o Veo desenhar um balcao de consultorio numa varanda de
# cipreste devolve os dois na mesma cena.
NAO_TOCA = ("%s never touches, opens, lifts or pours any of the ingredients on "
            "the %s — %s only points at them and explains.")

# CL9 — a bancada e' identica nas cenas 1 e 2 (familia A)
MESMA_BANCADA = ("in the same order and at the same levels, nothing moved, "
                 "nothing added, nothing removed")

# CL9 familia B — o copo muda, o resto nao. ⛔ Sem `at the same levels`: o nivel
# do copo SOBE a cada despejo, e pedir nivel identico e' ordem contraditoria —
# o Veo resolve desfazendo o preparo.
MESMA_BANCADA_B = ("Nothing has been added to the %s and nothing removed "
                   "from it — only the tall glass has changed.")

# CL14 familia B, cenas 1 e 2 — ela toca UM recipiente e so' ele. Substitui o
# NAO_TOCA nessas duas cenas; na cena 3 o NAO_TOCA volta inteiro.
TOCA_UM = ("%s touches only the container %s is pouring from. %s never touches, "
           "opens or lifts anything else on the %s.")

# CL21 — a gelatina pronta, SO' na cena 3
GELATINA = "a clear glass bowl of firm dark purple gelatin cubes, glossy and set"

# CL17 — anti-F12b nas cenas 1 e 2 da familia B: punho inteiro + antebraco
# apoiado. ⛔ Nunca `completely motionless` num recipiente que alguem segura:
# e' ordem impossivel e o Veo resolve SOLTANDO o objeto.
# ⚠️ O esqueleto e' o do mel, validado em render 2026-08-02 — so' o recipiente
# e o gesto trocam (tabela DESPEJO). String validada nao se redigita.
PEGADA = ("%s right hand is closed around the %s, the whole hand visibly "
          "wrapped around it, %s forearm resting steady on the %s "
          "as %s %s")

# ⭐⭐ CL29 — A VOZ E' SEMPRE INGLES AMERICANO (ordem do operador, 2026-08-05:
# *"todos os audios sempre tenham o sotaque americano, independentemente da
# etnia"*). O take 3 saiu com sotaque caribenho num mundo de mangueiras.
#
# ⚠️ POR QUE SO' O TAKE 3 DERRAPOU, medido lendo os tres blocos lado a lado:
# a linha de fala e' IDENTICA nos tres, mas nos takes 1 e 2 tudo o que vem
# depois dela fala da PESSOA (`He keeps his right hand closed around the
# box...`) e o audio ainda carrega o som do despejo. No take 3 a direcao inteira
# fala de OBJETOS parados e o audio fica so' com a ambiencia do MUNDO — e' a
# unica pista de voz que sobra, entao o gerador tira o sotaque do cenario.
# ⛔ A ambiencia NAO se toca (e' cena, alcada do operador): ancora-se a voz.
# ⚠️ Duas ancoras, como no CL25 e na trava de pele — uma so' ja' provou ser
# fraca duas vezes esta semana: uma na DIRECAO (onde ele fala) e outra no
# campo `Audio:` (onde o gerador decide o timbre).
# ⛔ Ancora POSITIVA: diz-se QUAL sotaque, nunca `no foreign accent`.
SOTAQUE = "in a natural American English accent"
VOZ = "The voice is natural American English with a standard United States accent"

ANTICELEB = ("Ordinary relatable face, not a celebrity, not a model, not an "
             "actor, not resembling any famous person.")
# ⭐ CL26 — a clausula anti-celebridade tem SEXO (ordem do operador,
# 2026-08-04: *"todas precisam ser absolutamente lindas"*). No homem, "cara
# comum" e' credibilidade. Na mulher, o `plain unremarkable face` brigava DE
# FRENTE com a ordem: o gerador recebia "linda" no corpo e "sem graca" no
# rosto na mesma frase, e resolvia a contradicao contra nos. A protecao de
# identidade (nao-celebridade) fica nas duas versoes; so' sai o "comum".
ANTICELEB_M = ("A strikingly beautiful face, not a celebrity, not resembling "
               "any famous person.")
# O par do REF 01 — mesma regra, na frase inteira de pessoa:
REF_ROSTO_H = ("An ordinary everyday relatable person with a plain "
               "unremarkable face, not a celebrity, not a model, not an "
               "actor, not resembling any famous person.")
REF_ROSTO_M = ("A strikingly beautiful woman, her face flawless and "
               "photogenic, her hair silky, smooth and healthy with a soft "
               "shine, yet not a celebrity, not an actress, not resembling "
               "any famous person.")
CAUDA = "Shot on iPhone, natural grain. No on-screen text, no watermark."

# ⛔⛔ OS DENTES SAO ANCORADOS (2026-08-03, falha em producao). A boca fica
# ABERTA mid-word nas tres IMAGEs e nada descrevia os dentes — e o que o
# gerador nao recebe, ele inventa: saiam homens com dente da frente torto,
# quebrado, e o Veo as vezes animava BANGUELO.
# ⚠️ Ancora POSITIVA, nunca negativa. `no missing teeth` e' negacao, e negacao
# nao cria forma — e' o mesmo erro do `with no label` do CL19, que devolveu
# caixa branca generica. Diz-se o que TEM: fileira completa e pareja.
# ⭐⭐ 2026-08-04 (foto de campo): a ancora de TEXTO sozinha nao segurou — o
# operador mandou o print de uma REF feminina banguela. A lei subiu de nivel:
# o REF 01 agora SORRI mostrando a fileira branca completa, e os dentes passam
# a morar na IMAGEM de identidade (5a alavanca — quando texto e imagem
# discordam, a imagem vence; as cenas seguem a foto). As ancoras de texto nas
# cenas continuam, como reforco.
DENTES = "%s front teeth even and complete"


# ---------------------------------------------------------------------------
# EIXOS SORTEAVEIS
# ---------------------------------------------------------------------------
FAMILIAS = [
    {"id": "aponta", "selo": "V", "nome": "a fileira apontada"},
    # ⭐ selo V desde 2026-08-02: o video 0726 saiu em 20,2s com despejo nas
    # DUAS cenas, o Veo nao soltou nenhum dos recipientes, e a copy chegou
    # palavra por palavra (transcrita e conferida contra o roteiro).
    {"id": "preparo", "selo": "V", "nome": "o preparo nas cenas 1 e 2"},
]

# ---------------------------------------------------------------------------
# ⭐⭐ MUNDOS — O NICHO VISUAL INTEIRO NUM EIXO SO' (2026-08-03)
# ---------------------------------------------------------------------------
# ⛔ O QUE ESTAVA ERRADO, na palavra do operador: *"variar etnias tal como o
# NECROSE quer dizer variar ate' o nivel de NICHO VISUAL — nativo da montanha,
# nativo do pantano, tribo africana — com adaptacao tematica visual alinhada a'
# etnia, e nao so' 'mudar o rosto do REF por etnia' como voce fez no v2"*.
#
# A primeira versao do v2 tinha DOIS eixos independentes: `ETNIAS` (14
# adjetivos soltos) e `CENARIOS` (6 consultorios). Sorteados separados, o
# resultado media exatamente o que ele viu no lote: **o mesmo consultorio com
# rosto diferente**. Trocar a etnia nao mudava um pixel do mundo.
#
# ⭐ A FORMA CERTA E' A DO NECROSE (NE5): la' o `ARQUETIPOS` e' UM EIXO SO' que
# carrega cenario + chapeu + animal juntos, com este motivo escrito no proprio
# arquivo — *"eles nao sao independentes; chapeu errado no cenario certo destroi
# a leitura em meio segundo"*. Aqui vale igual, e com mais um item na conta: a
# ETNIA tambem entra no pacote. Uma curandeira dos Apalaches num consultorio de
# diplomas nao le' como nada.
#
# Cada MUNDO carrega, congruentes entre si:
#     etnias  as etnias que aquele mundo comporta (a etnia SAI daqui)
#     desc    o cenario                      (%s = pronome objeto)
#     sup_a   a superficie com artigo        ("a wooden counter")
#     sup     a mesma, curta                 ("counter")
#     traje   a roupa                        (%s = cor)
#     curto   a roupa em 2 palavras, para o "same %s" das cenas 2 e 3
#     cores   as cores que aquela roupa aceita
#     luz     a luz da cena 1
#     luz_c   a mesma, curta, para o "same %s" da cena 3
#     audio   a ambiencia
#
# ⭐ O SORTEIO E' POR FAMILIA, DEPOIS POR MUNDO DENTRO DELA — nao uniforme sobre
# os 26. Sem isso a familia `clinica`, que tem 6 sets (os unicos com render
# validado, e por isso preservados inteiros), levaria 23% de todos os videos e o
# lote voltaria a parecer o de antes. Por familia ela leva 1/11.
#
# ⛔ ZERO texto legivel em qualquer set: o CAUDA promete "No on-screen text" nas
# tres imagens, e parede de gaveta com caractere escrito e' texto em cena. Por
# isso as gavetas do ervanario tem "brass pulls" e nao etiqueta.
# ⛔ ZERO objeto religioso: santo, altar, vela de igreja e amuleto sao terreno de
# moderacao sem upside nenhum de conversao.
# ⚠️ O selo `V` fica so' na familia `clinica`: os 6 sets dela vieram da fonte
# (Valentina Health & Wellness) e tem render atras. Os outros 20 sao `N` —
# extrapolacao nossa, sem render, e e' o operador quem valida no campo.
MUNDOS = [
    # ⛔⛔ A FAMILIA `clinica` SAIU EM 2026-08-05, POR ORDEM DO OPERADOR:
    # *"nao quero que os cenarios/mundo do agente v1 se repitam no agente da v2"*.
    # Eram SEIS mundos (diplomas_cidade, diplomas_jardim, farmacia,
    # consultorio_claro, sala_exame, escritorio_livros) e os seis eram copia
    # BYTE A BYTE dos CENARIOS do clean_short.py — mesmo id e mesmo `desc`.
    # Existiam para provar a refatoracao (o motor novo tinha de render igual ao
    # antigo no mundo clinico); essa prova ja' foi dada e arquivada no commit
    # do eixo MUNDO. Agora eles so' faziam o V2 repetir o V1.
    # ⚠️ Eram tambem os unicos `selo: V` e os unicos com `etnias: "todas"`. O
    # que sobra: 20 mundos, 10 familias, 19 etnias, e as duas peles da trava
    # continuam cobertas (escura em 6 mundos, clara em 4) — medido.
    # ⛔ O dict CLINICA logo abaixo FICA: ele e' a tabela de DEFAULTS que os
    # outros mundos herdam por setdefault, nao uma entrada de cenario.
    # ⛔ E o V1 nao foi tocado: quem se move e' o V2 (assert de carga abaixo).

    # ---- montanha dos Apalaches -------------------------------------------
    {"id": "apalache_varanda", "selo": "N", "familia": "apalache",
     "etnias": ["white American"],
     "desc": "the covered porch of a log cabin deep in the Appalachian woods, "
             "bunches of dried herbs hanging from the beams above %s and rows "
             "of glass jars on a plank shelf behind, dense green forest beyond",
     "sup_a": "a long plank table", "sup": "table",
     "traje": "%s cotton work shirt with the sleeves rolled to the elbow",
     "curto": "work shirt",
     "cores": ["faded blue", "dark green", "rust brown", "charcoal grey"],
     "luz": "Soft green forest daylight, low contrast.",
     "luz_c": "soft forest daylight",
     "audio": "insects, wind in the leaves"},
    {"id": "apalache_cozinha", "selo": "N", "familia": "apalache",
     "etnias": ["white American"],
     "desc": "the kitchen of a mountain cabin, a black cast-iron stove behind "
             "%s, bundles of dried herbs strung along a beam and a small "
             "window looking out on bare ridges",
     "sup_a": "a scrubbed pine table", "sup": "table",
     "traje": "%s flannel shirt buttoned to the collar",
     "curto": "flannel shirt",
     "cores": ["deep red", "forest green", "faded blue", "brown"],
     "luz": "Cool window light from frame-left, soft shadows.",
     "luz_c": "cool window light",
     "audio": "a wood fire ticking, wind at the window"},

    # ---- pantano do sul ----------------------------------------------------
    {"id": "pantano_alpendre", "selo": "N", "familia": "pantano",
     "etnias": ["Creole American", "Cajun American", "Black American"],
     "desc": "a wooden landing at the edge of a cypress swamp, hanging moss on "
             "the branches behind %s, a flat-bottomed boat tied up at the "
             "posts and still dark water beyond",
     "sup_a": "a weathered plank table", "sup": "table",
     "traje": "%s linen shirt with the sleeves rolled up",
     "curto": "linen shirt",
     "cores": ["off-white", "pale blue", "sand", "olive"],
     "luz": "Warm hazy swamp light, soft and diffused.",
     "luz_c": "warm hazy light",
     "audio": "frogs, water moving under the boards"},
    {"id": "pantano_varanda", "selo": "N", "familia": "pantano",
     "etnias": ["Creole American", "Cajun American", "Black American"],
     "desc": "a screened back porch in the bayou country, strings of dried red "
             "peppers and braided garlic hanging behind %s, tall wet green "
             "growth pressing against the screen beyond",
     "sup_a": "a painted wooden table", "sup": "table",
     "traje": "%s short-sleeved cotton shirt",
     "curto": "cotton shirt",
     "cores": ["pale yellow", "off-white", "sky blue", "faded green"],
     "luz": "Flat humid daylight through the screen, low contrast.",
     "luz_c": "flat humid daylight",
     "audio": "cicadas, a screen door creaking"},

    # ---- herbolaria mexicana ----------------------------------------------
    {"id": "herbolaria_mercado", "selo": "N", "familia": "herbolaria",
     "etnias": ["Mexican American", "Hispanic American"],
     "desc": "an herb stall inside a covered market, the wall behind %s hung "
             "thick with tied bundles of dried herbs and long strings of dried "
             "red chiles, woven baskets stacked at the sides",
     "sup_a": "a worn wooden market counter", "sup": "counter",
     "traje": "%s embroidered cotton blouse",
     "curto": "embroidered blouse",
     "cores": ["cream", "deep pink", "turquoise", "marigold yellow"],
     "luz": "Warm shaded market light, soft and even.",
     "luz_c": "warm shaded light",
     "audio": "a quiet market murmur far off"},
    {"id": "herbolaria_patio", "selo": "N", "familia": "herbolaria",
     "etnias": ["Mexican American", "Hispanic American"],
     "desc": "a shaded courtyard with thick adobe walls behind %s, rows of "
             "potted herbs on a low ledge and a climbing bougainvillea at the "
             "corner, bright sun on the far wall",
     "sup_a": "a tiled courtyard table", "sup": "table",
     "traje": "%s loose cotton shirt",
     "curto": "cotton shirt",
     "cores": ["white", "sky blue", "terracotta", "pale green"],
     "luz": "Bright bounced courtyard light, warm and soft.",
     "luz_c": "warm courtyard light",
     "audio": "birds in the courtyard, a far-off street"},

    # ---- África Ocidental --------------------------------------------------
    # ⚠️ O operador pediu "tribo africana" com todas as letras. O set descreve
    # LUGAR e MATERIAL (esteira, cabaca, tecido estampado, barro), nunca
    # "tribal" como adjetivo solto: adjetivo generico devolve fantasia de
    # carnaval, material concreto devolve lugar.
    {"id": "africa_mercado", "selo": "N", "familia": "africa",
     "etnias": ["West African", "Black American"],
     "desc": "an open-air market stall under a woven reed canopy, wide shallow "
             "baskets of dried roots, bark and leaves ranged behind %s, bolts "
             "of bright wax-print cloth hanging at the side",
     "sup_a": "a low wooden bench counter", "sup": "counter",
     "traje": "%s wax-print cotton tunic",
     "curto": "print tunic",
     "cores": ["indigo and gold", "deep green and white", "orange and black",
               "red and cream"],
     "luz": "Hot filtered daylight through the reed canopy, warm and dappled.",
     "luz_c": "warm filtered daylight",
     "audio": "a distant market, wind in the reeds"},
    {"id": "africa_patio", "selo": "N", "familia": "africa",
     "etnias": ["West African", "Black American"],
     "desc": "a swept earth courtyard with a mud-brick wall behind %s, round "
             "calabash bowls and clay pots set along the wall, the shade of a "
             "broad mango tree falling across the ground",
     "sup_a": "a low carved wooden table", "sup": "table",
     "traje": "%s embroidered cotton tunic",
     "curto": "cotton tunic",
     "cores": ["white", "deep indigo", "saffron", "burnt orange"],
     "luz": "Warm open shade under the tree, soft and clean.",
     "luz_c": "warm open shade",
     "audio": "birds, wind in the mango leaves"},

    # ---- ervanario do leste asiatico ---------------------------------------
    {"id": "ervanario_gavetas", "selo": "N", "familia": "ervanario",
     "etnias": ["Chinese American", "Korean American", "Asian American"],
     "desc": "an old herbal pharmacy, the whole wall behind %s a grid of small "
             "dark wooden apothecary drawers with round brass pulls, a rolling "
             "ladder against it",
     "sup_a": "a dark wood shop counter", "sup": "counter",
     "traje": "%s mandarin-collar cotton jacket",
     "curto": "collared jacket",
     "cores": ["indigo", "slate grey", "charcoal", "deep maroon"],
     "luz": "Warm low shop light, soft pools of light and shadow.",
     "luz_c": "warm shop light",
     "audio": "a very quiet room, a clock ticking somewhere"},
    {"id": "ervanario_bancada", "selo": "N", "familia": "ervanario",
     "etnias": ["Chinese American", "Korean American", "Asian American"],
     "desc": "a herbal shop workroom, tall glass jars of dried roots and bark "
             "lined on shelves behind %s, a brass hand scale and a stack of "
             "flat woven drying trays at the side",
     "sup_a": "a scrubbed wooden work counter", "sup": "counter",
     "traje": "%s linen wrap jacket",
     "curto": "wrap jacket",
     "cores": ["natural beige", "soft grey", "deep blue", "dark green"],
     "luz": "Even daylight from a high window, cool and soft.",
     "luz_c": "even daylight",
     "audio": "a very quiet room, faint street noise"},

    # ---- ayurveda ----------------------------------------------------------
    {"id": "ayurveda_sala", "selo": "N", "familia": "ayurveda",
     "etnias": ["South Asian American", "Indian American"],
     "desc": "a sunlit room with a long shelf of brass and copper vessels on "
             "the wall behind %s, rows of small glass jars of coloured powders "
             "beside them, a woven mat on the floor",
     "sup_a": "a low polished wooden table", "sup": "table",
     "traje": "%s cotton kurta",
     "curto": "cotton kurta",
     "cores": ["cream", "deep saffron", "olive green", "dusty rose"],
     "luz": "Warm sunlight through a high window, soft edges.",
     "luz_c": "warm window sunlight",
     "audio": "a quiet room, birds outside"},
    {"id": "ayurveda_varanda", "selo": "N", "familia": "ayurveda",
     "etnias": ["South Asian American", "Indian American"],
     "desc": "a shaded veranda with carved wooden pillars behind %s, hanging "
             "brass lamps unlit above and a green garden with broad-leaved "
             "plants beyond the rail",
     "sup_a": "a carved wooden table", "sup": "table",
     "traje": "%s linen kurta",
     "curto": "linen kurta",
     "cores": ["off-white", "pale blue", "sand", "deep teal"],
     "luz": "Soft green garden light in open shade, low contrast.",
     "luz_c": "soft garden light",
     "audio": "birds, leaves moving in the garden"},

    # ---- nativo norte-americano -------------------------------------------
    {"id": "nativo_ramada", "selo": "N", "familia": "nativo",
     "etnias": ["Native American"],
     "desc": "the shade of a juniper-pole ramada on high desert ground, a "
             "woven wool blanket in bold geometric bands hung on the rail "
             "behind %s, red rock country stretching away beyond",
     "sup_a": "a heavy plank table", "sup": "table",
     "traje": "%s cotton shirt with the sleeves rolled",
     "curto": "cotton shirt",
     "cores": ["deep turquoise", "rust red", "sand", "charcoal"],
     "luz": "Bright open shade against hard desert sun outside.",
     "luz_c": "bright open shade",
     "audio": "dry wind, a distant bird"},
    {"id": "nativo_rio", "selo": "N", "familia": "nativo",
     "etnias": ["Native American"],
     "desc": "a clearing beside a shallow stone-bedded river, tall pines "
             "closing in behind %s, drying racks of split herbs on trestles "
             "at the side and fast clear water beyond",
     "sup_a": "a split-log table", "sup": "table",
     "traje": "%s canvas shirt buttoned at the wrists",
     "curto": "canvas shirt",
     "cores": ["dark green", "faded blue", "brown", "slate grey"],
     "luz": "Cool dappled forest light off the water.",
     "luz_c": "cool dappled light",
     "audio": "water over stones, wind in the pines"},

    # ---- caribe ------------------------------------------------------------
    {"id": "caribe_varanda", "selo": "N", "familia": "caribe",
     "etnias": ["Caribbean American", "Jamaican American", "Black American"],
     # ⛔ CL2 — a primeira versao destes dois sets do Caribe trazia `banana`
     # (folha de bananeira aqui, penca verde no mercado). O proprio linter do
     # CLEAN reprovou 53 dos 600 videos da varredura: banana e' PROP FALICO e
     # este agente e' o unico que nao tem nenhum. Trocado por folhagem e tempero
     # que dao o mesmo lugar sem o objeto proibido.
     "desc": "the verandah of a brightly painted wooden house, louvered "
             "shutters in strong colour behind %s, broad-leaved tropical "
             "plants and hibiscus crowding the rail, bright sky beyond",
     "sup_a": "a painted plank table", "sup": "table",
     "traje": "%s short-sleeved cotton shirt",
     "curto": "cotton shirt",
     "cores": ["turquoise", "sun yellow", "white", "coral"],
     "luz": "Bright island daylight in open shade, warm and clean.",
     "luz_c": "bright open shade",
     "audio": "birds, wind in the banana leaves"},
    {"id": "caribe_mercado", "selo": "N", "familia": "caribe",
     "etnias": ["Caribbean American", "Jamaican American", "Black American"],
     "desc": "a roadside produce stall under a corrugated tin roof, bunches of "
             "thyme and strings of small red peppers hanging from the frame "
             "above %s, green hills out of focus beyond the road",
     "sup_a": "a rough plank stall counter", "sup": "counter",
     "traje": "%s cotton shirt open at the collar",
     "curto": "cotton shirt",
     "cores": ["pale green", "orange", "white", "sky blue"],
     "luz": "Hard tropical daylight softened under the tin roof.",
     "luz_c": "soft light under the roof",
     "audio": "birds, a vehicle passing far off"},

    # ---- ilhas do Pacifico / Filipinas ------------------------------------
    {"id": "pacifico_nipa", "selo": "N", "familia": "pacifico",
     "etnias": ["Filipino American", "Pacific Islander American"],
     "desc": "an open-sided hut with a thatched roof and split-bamboo walls "
             "behind %s, woven pandan mats rolled at the side, coconut palms "
             "and bright sky beyond the open wall",
     "sup_a": "a split-bamboo table", "sup": "table",
     "traje": "%s loose woven shirt",
     "curto": "woven shirt",
     "cores": ["natural cream", "pale blue", "deep red", "leaf green"],
     "luz": "Bright shade under the thatch, warm bounced light.",
     "luz_c": "bright shade",
     "audio": "wind in the palms, birds"},
    {"id": "pacifico_costa", "selo": "N", "familia": "pacifico",
     "etnias": ["Filipino American", "Pacific Islander American"],
     "desc": "a shaded platform above a black-sand shore, fishing floats and "
             "coiled rope hanging on the post behind %s, an outrigger canoe "
             "drawn up on the sand and flat sea beyond",
     "sup_a": "a weathered wooden table", "sup": "table",
     "traje": "%s short-sleeved cotton shirt",
     "curto": "cotton shirt",
     "cores": ["faded turquoise", "off-white", "deep blue", "sand"],
     "luz": "Bright even light bouncing off the water, soft shadows.",
     "luz_c": "bright even light",
     "audio": "small waves, wind over sand"},

    # ---- Oriente Medio -----------------------------------------------------
    {"id": "oriente_loja", "selo": "N", "familia": "oriente",
     "etnias": ["Middle Eastern American", "Lebanese American"],
     "desc": "a spice and herb shop, deep shelves of glass jars and open "
             "burlap sacks of dried herbs ranged behind %s, pierced brass "
             "lanterns hanging unlit above",
     "sup_a": "a worn wooden shop counter", "sup": "counter",
     "traje": "%s collarless linen shirt",
     "curto": "linen shirt",
     "cores": ["off-white", "sand", "deep olive", "slate blue"],
     "luz": "Warm low shop light with a shaft of daylight from the doorway.",
     "luz_c": "warm shop light",
     "audio": "a quiet shop, a far-off street"},
    {"id": "oriente_patio", "selo": "N", "familia": "oriente",
     "etnias": ["Middle Eastern American", "Lebanese American"],
     "desc": "a stone courtyard in deep shade, a pale plastered wall behind "
             "%s, a climbing grapevine over a trellis above and shallow "
             "drying trays of herbs along a stone ledge",
     "sup_a": "a stone slab table", "sup": "table",
     "traje": "%s loose cotton shirt",
     "curto": "cotton shirt",
     "cores": ["white", "pale grey", "sand", "deep blue"],
     "luz": "Cool courtyard shade with hot sun on the far wall.",
     "luz_c": "cool courtyard shade",
     "audio": "birds, a fountain somewhere"},
]

# ⛔ CONTRATO DO MUNDO CLINICO — copia literal do v2 anterior. Os 6 sets da
# familia `clinica` OMITEM superficie, traje, cores, luz e audio de proposito:
# eles herdam daqui, e e' este dict que garante que o motor novo renderiza
# aquela familia exatamente como o antigo renderizava (provado no --autoteste).
# ⚠️ `cores` e' o antigo pool `SCRUBS`, sem tirar nem acrescentar uma cor.
CLINICA = {
    "sup_a": "a wooden counter", "sup": "counter",
    "traje": "%s V-neck short-sleeved medical scrub top",
    "curto": "scrub top",
    "cores": ["deep burgundy", "deep teal", "navy blue", "forest green",
              "plum purple", "slate grey", "wine red", "petrol blue"],
    "luz": "Soft daylight from the window.",
    "luz_c": "soft daylight",
    "audio": "quiet office room tone",
    # ⚠️ `lugar` existe so' para as cenas 2 e 3, que dizem "in the same %s".
    # `room` e' o literal do v2 anterior e fica de pe' na clinica; num mercado a
    # ceu aberto ou num alpendre de pantano "room" e' a palavra errada e o Veo
    # responde fechando paredes em volta.
    "lugar": "room",
}
for _m in MUNDOS:
    if _m["familia"] != "clinica":
        _m.setdefault("lugar", "place")

for _m in MUNDOS:
    for _k, _v in CLINICA.items():
        _m.setdefault(_k, _v)
    if _m["etnias"] == "todas":
        _m["etnias"] = list(ETNIAS)

# As familias, na ordem em que aparecem — o sorteio pesa por FAMILIA, nunca por
# mundo solto (senao `clinica`, com 6 sets, domina o lote).
FAMILIAS_MUNDO = list(dict.fromkeys(m["familia"] for m in MUNDOS))

# ⛔⛔ NENHUM MUNDO DO V2 REPETE CENARIO DO V1 (ordem do operador, 2026-08-05).
# ⚠️ Lista CONGELADA aqui em vez de `import clean_short`: os SHORT sao
# autossuficientes por decisao de projeto (desacoplamento de 2026-08-03) e o
# app entregue nao leva o motor do V1 junto — um import quebraria o .exe. A
# copia e' segura porque o V1 esta' CONGELADO por ordem do operador; o
# `--autoteste` confere contra o arquivo real quando ele existe ao lado.
# ⛔ O `assinatura` pega o caso que o id sozinho nao pega: cenario clinico
# reescrito com id novo continua sendo o territorio do V1.
CENARIOS_V1 = ("diplomas_cidade", "diplomas_jardim", "farmacia",
               "consultorio_claro", "sala_exame", "escritorio_livros")
_ASSINATURA_V1 = ("bright medical office", "bright clinic room",
                  "bright consulting room", "bright examination room")
for _m in MUNDOS:
    assert _m["id"] not in CENARIOS_V1, (
        "mundo %r e' cenario do V1 — o V2 nao repete o V1" % _m["id"])
    for _a in _ASSINATURA_V1:
        assert _a not in _m["desc"], (
            "mundo %r usa o consultorio do V1 (%r)" % (_m["id"], _a))

# ⛔ assert de carga da TRAVA DE PELE: toda etnia do PELE_ETNIAS tem de existir
# em algum mundo — um rename de etnia nos MUNDOS nao pode deixar a lista
# apontando para o nada (a trava viraria botao morto de novo, em silencio).
_ETNIAS_EM_MUNDO = {e for _m in MUNDOS for e in _m["etnias"]}
for _p, _ets in PELE_ETNIAS.items():
    for _e in _ets:
        assert _e in _ETNIAS_EM_MUNDO, (
            "PELE_ETNIAS[%r] cita etnia que nenhum mundo tem: %r" % (_p, _e))
    assert any(_pele_de(e) == _p for e in _ETNIAS_EM_MUNDO), (
        "nenhum mundo comporta a pele %r" % _p)

# ⛔⛔ LEI DO REF — A REF MULHER E' SEMPRE MUITO BONITA (2026-08-03).
# Ordem do operador: *"quero todos os refs homens musculosos e todas as refs
# mulheres lindas no agente clean short"*. O CL24 (corpo treinado) resolveu o
# CORPO das duas; esta lei e' sobre o ROSTO e a IDADE dela.
#
# ⚠️ O POOL ANTERIOR ERA O MESMO ERRO DO RESSURREICAO E DO COLO, e esta e' a
# TERCEIRA vez: as tres ultimas entradas foram escritas para preencher os eixos
# `oculos` e `pele` do `medir_personagens.py`, e trouxeram
# `half-moon reading glasses low on her nose`, `silver-streaked hair`,
# `sun-weathered skin`, `deeply lined skin` e idade ate' 52. O medidor dava nota
# boa e devolvia a personagem errada num agente cuja REF vende para homem.
# Otimizar a metrica contra o objetivo.
# ⛔ A ancora facial continua obrigatoria (P6) — sem ela o Veo troca de rosto
# entre blocos. Mas ela e' DISTINTIVA e nunca DETERIORADA: marca de nascenca,
# covinha, olho de cor incomum, sarda, malar alto.
# ⛔⛔ DENTE NAO E' MARCA (CL25, foto de campo 2026-08-04): `a small gap
# between her front teeth` era ancora legitima, mas o gerador EXAGERA
# imperfeicao dentaria ate' virar dente faltando — o operador mandou o print.
# E' a regiao que os geradores mais erram; assert de carga logo abaixo.
# ⚠️ O eixo `oculos` fica ZERADO de proposito e a excecao esta' declarada no
# medidor. ⛔ So' no pool FEMININO: no REFS_H oculos e grisalho ficam, porque no
# homem eles leem como CREDIBILIDADE — o oposto do efeito na mulher.
# ⭐ CL26 — O CABELO E' SEMPRE HIDRATADO E COM BRILHO (2026-08-04, prints de
# campo): `thick auburn hair falling loose` sem qualificador de textura saiu
# RESSECADO, duro, sem hidratacao. Todo `cabeca` feminino carrega um token de
# saude capilar (glossy/silky/sleek/sheen/smooth) — assert de carga abaixo.
REFS_M = [
    {"idade": 29, "cabeca": "her hair in neat glossy cornrows pulled back",
     "marca": "a small dark beauty mark above her left eyebrow"},
    {"idade": 32, "cabeca": "her hair in a sleek shining low bun",
     "marca": "high cheekbones and a small scar at the corner of her jaw"},
    {"idade": 27, "cabeca": "shoulder-length glossy straight hair tucked behind her ears",
     "marca": "a light spray of freckles high on her cheeks"},
    {"idade": 34, "cabeca": "short soft natural curls, glossy and well-defined",
     "marca": "a deep dimple in her left cheek"},
    {"idade": 30, "cabeca": "long silky hair pulled back into a smooth high ponytail",
     "marca": "striking pale green eyes"},
    {"idade": 36, "cabeca": "long neat braids with a healthy sheen, gathered over one shoulder",
     "marca": "a small dark beauty mark on her chin"},
    {"idade": 28, "cabeca": "a blunt glossy dark bob",
     "marca": "full lips and a small dark beauty mark just below the outer "
              "corner of her left eye"},
    {"idade": 38, "cabeca": "thick silky auburn hair, smooth and glossy, falling loose past her shoulders",
     "marca": "a dense spray of freckles across her nose"},
    {"idade": 40, "cabeca": "smooth glossy dark hair with a sharp widow's peak, swept back",
     "marca": "eyes of two different colours, one green and one brown"},
    # + 2026-08-04: ampliacao por ordem do operador (*"aumente o pool de
    # personagens"*), espelhada do clean_short no rebase — la' as entradas
    # chegaram sem o token de cabelo do CL26 e com 2 ancoras repetidas; aqui
    # ja' entram corrigidas, identicas ao v1.
    {"idade": 26,
     "cabeca": "long silky jet-black hair in a single braid over one shoulder",
     "marca": "high round cheekbones and clear glowing skin"},
    {"idade": 31,
     "cabeca": "a sleek bleached-platinum bob cut sharp at the jaw",
     "marca": "a small silver hoop through her left nostril"},
    {"idade": 24,
     "cabeca": "thick glossy copper-red hair falling loose past her shoulders",
     "marca": "a dense spray of freckles over both cheeks and pale blue eyes"},
    {"idade": 33,
     "cabeca": "a big loose curl-out worn wide, soft and glossy",
     "marca": "full lips and a faint dimple in her right cheek"},
    {"idade": 28,
     "cabeca": "shoulder-length glossy auburn hair tucked behind one ear",
     "marca": "striking light amber eyes"},
    {"idade": 35,
     "cabeca": "waist-length box braids with a healthy sheen, gathered over one shoulder",
     "marca": "smooth luminous skin and a wide bright smile"},
    {"idade": 27,
     "cabeca": "very long silky straight dark hair parted in the middle",
     "marca": "arched brows and a small beauty mark high on her left cheek"},
    {"idade": 30,
     "cabeca": "chin-length smooth wavy caramel hair pushed back off her forehead",
     "marca": "a small heart-shaped birthmark below her right ear"},
]
REFS_H = [
    {"idade": 48, "cabeca": "short greying hair and a close-cropped beard", "marca": "a small scar through his right eyebrow"},
    {"idade": 52, "cabeca": "a clean-shaven head and a short grey beard", "marca": "deep lines across his forehead"},
    {"idade": 44, "cabeca": "short dark hair combed back, clean-shaven", "marca": "a small mole on his left cheek"},
    {"idade": 55, "cabeca": "thinning grey hair and a full grey moustache", "marca": "heavy creases at the corners of his eyes"},
    {"idade": 41, "cabeca": "short cropped hair and a neat goatee", "marca": "a faint scar on his chin"},
    {"idade": 50, "cabeca": "salt-and-pepper hair cut short, clean-shaven", "marca": "a small notch in his right eyebrow"},
    # + 2026-08-03 — mesmo motivo do REFS_M acima: oculos e pele estavam em 0%.
    # ⛔ Nenhuma repete a ancora facial das seis de cima (cicatriz na
    # sobrancelha, linhas na testa, pinta na bochecha, vincos no olho, cicatriz
    # no queixo, entalhe na sobrancelha): ancora repetida remenda o morphing.
    {"idade": 57, "cabeca": "a bald crown with grey at the sides and a chevron moustache, thin gold-rimmed glasses",
     "marca": "sun-weathered skin and a coin-sized birthmark on his left temple"},
    {"idade": 43, "cabeca": "thick dark hair with a sharp widow's peak, clean-shaven, boxy clear-framed glasses",
     "marca": "freckled skin across the bridge of his nose"},
    {"idade": 61, "cabeca": "a full head of white hair and a bristly white beard, heavy black-framed bifocals",
     "marca": "deeply lined skin and a pale scar along his right jaw"},
    # + 2026-08-04: ampliacao por ordem do operador, espelhada do clean_short
    # no rebase. A ultima chegou com `a wide gap between his two front teeth`
    # de marca — o assert do CL25 barrou (dente vira banguelo no Veo) e ela
    # entra ja' corrigida, identica ao v1.
    {"idade": 52,
     "cabeca": "a shaved head and a full salt-and-pepper beard",
     "marca": "a broad flattened nose that has been broken once"},
    {"idade": 45,
     "cabeca": "thick dark hair going grey at the temples, clean-shaven",
     "marca": "a deep vertical crease between his eyebrows"},
    {"idade": 57,
     "cabeca": "close-cropped iron-grey hair and a neat pencil moustache",
     "marca": "wire-rimmed glasses and a heavy square jaw"},
    {"idade": 41,
     "cabeca": "dark curls kept short and dense, a two-day shadow",
     "marca": "a notch cut through his right eyebrow"},
    {"idade": 60,
     "cabeca": "a bald crown with white hair close at the sides",
     "marca": "a thick white moustache and heavy hooded eyelids"},
    {"idade": 49,
     "cabeca": "wavy salt-and-pepper hair worn long at the collar",
     "marca": "a pale crescent scar on his left cheekbone"},
    {"idade": 54,
     "cabeca": "grey hair in a flat brush cut and a short greying beard",
     "marca": "very pale blue eyes under dark brows"},
    {"idade": 44,
     "cabeca": "close-cropped coils with a sharp lined edge, clean-shaven",
     "marca": "a single deep dimple in his left cheek"},
]

# ⛔ CL25 — assert de carga: nenhuma marca facial volta a pedir defeito de
# dente. O gap "saiu" uma vez SO' NA DOUTRINA e continuou no motor ate' a foto
# de campo de 2026-08-04 — regra sem assert e' regra que volta.
for _r in REFS_M + REFS_H:
    assert "teeth" not in _r["marca"] and "tooth" not in _r["marca"], (
        "CL25: marca facial cita dente: %r" % _r["marca"])
# ⛔ CL26 — assert de carga: todo cabelo feminino com token de saude capilar
for _r in REFS_M:
    assert any(t in _r["cabeca"] for t in ("glossy", "silky", "sleek",
                                           "sheen", "smooth")), (
        "CL26: cabelo feminino sem brilho/hidratacao: %r" % _r["cabeca"])

# CL14 — os DOIS ingredientes do truque. Piso e teto: sao dois, sempre, em
# todas as tres imagens. Nao precisam ser citados na copy — estao ali para
# ---------------------------------------------------------------------------
# ⭐ CL24 — O CORPO MASCULINO E' SEMPRE TREINADO (ordem do operador, 2026-08-03)
# ---------------------------------------------------------------------------
# O REF do CLEAN passa a ter corpo descrito: musculo e veia visiveis, saude
# evidente. A razao e' de conversao — quem da' conselho de vitalidade masculina
# tem de PARECER que o conselho funcionou nele.
#
# ⭐ SUBIU ~30% EM 2026-08-03 (segunda ordem do operador): o alvo passou a ser
# ATLETA, nao "pessoa que se cuida". Entraram massa nos ombros, deltoide e
# trapezio nomeados, veia que corre ate' o pulso.
# ⛔⛔ DESDE 2026-08-04 O CL24 E' SO' DO HOMEM. A mulher saiu dele — o pool
# antigo dava a ela deltoide, biceps e antebraco veiado, e o operador viu o
# resultado: "está gerando muito musculosa". O corpo dela mora no CL26 abaixo.
# ⛔ O teto continua: atleta, NAO fisiculturista. Nada de musculo estourado,
# corpo oleado, veia de competicao ou definicao de palco — o registro do
# CLEAN e' consultorio, e passar disso vira outro angulo.
# ⛔ E CONTINUA VALENDO O CL8: nunca tronco nu. O que se ve' e' o que um scrub
# de manga curta e decote em V deixa ver — antebraco, ombro, pescoco, colarinho.
# Corpo aparece PELA ROUPA, nunca sem ela.
# ⚠️ As frases NAO citam a peca de roupa de proposito: o v2 troca o traje
# conforme o MUNDO, e `under the scrub` sairia errado numa varanda. Descreve-se
# o corpo; a roupa assenta depois. Assim o mesmo pool serve os dois agentes e
# nao vira fragmento espelhado que envelhece em separado.
#
# ⚠️ ISTO MEXE NO SELO. O 🟢 do CLEAN foi medido em 24 geracoes SEM descricao de
# corpo. E em 2026-08-03 a mesma familia de frase (`toned arms`, `trim waist`)
# travou 4x seguidas no gerador de IMAGEM da capa da Denise — densidade de
# adjetivo de corpo e' superficie de bloqueio conhecida. Por isso cada linha
# aqui e' curta e ancorada em GEOMETRIA (ombro, antebraco, veia) em vez de
# empilhar adjetivo. Se vier recusa, a primeira coisa a encurtar e' esta.
CORPOS_H = [
    "the heavy trained build of an athlete, thick deltoids and a broad deep chest, forearms corded with veins standing out along them, skin clear and healthy",
    "a powerful athletic frame, wide square shoulders and heavy muscled arms, thick veins running down each forearm, plainly in hard condition",
    "a muscular athlete's build, a thick neck, heavy traps and broad shoulders, forearms roped with standing veins, healthy colour in his face",
    "the dense trained frame of a lifter, deep chest and thick round shoulders, arms heavy and veined to the wrist, clearly in peak health",
    "a hard muscular build with real mass across the shoulders and arms, veins raised along the forearms and the backs of his hands, skin clear and well",
    # + 2026-08-04: ampliacao por ordem do operador — *"aumente o pool de
    # personagens... faca isso para pelo menos outros 5 agentes shorts"*.
    # ⛔ Cada entrada difere das outras em >= 3 eixos fisicos (licoes §15).
    # ⚠️ Vieram do clean_short (rebase 2026-08-04) — la' tinham entrado no
    # CORPOS_M por engano de colagem; espelhadas aqui no mesmo commit para o
    # fragmento nao envelhecer separado.
    "the dense build of a man who lifts, thick through the chest and shoulders, forearms corded, skin taut and even",
    "a lean hard frame with a flat stomach and a visible line down the centre, shoulders square, skin clear",
    "the heavy-boned build of a wrestler, a thick neck and broad flat chest, arms full and solid, skin healthy",
    "a swimmer's build, long muscled arms and a wide back tapering to the waist, shoulders capped and round, skin clear",
]
# ---------------------------------------------------------------------------
# ⭐⭐ CL26 — O CORPO FEMININO E' SENSUAL, NUNCA MUSCULOSO (2026-08-04)
# ---------------------------------------------------------------------------
# Ordem do operador: *"a mulher deve ser sensual, ter apenas seios e gluteos
# avantajados, além de uma beleza facial incrivel, todas precisam ser
# absolutamente lindas, independente de selecionar para negras ou brancas"*.
# O pool anterior era o CL24 aplicado a ela (deltoide, biceps, veia) e saiu
# "muito musculosa" em producao.
# ⚠️ A anatomia da linha e' fixa: SILHUETA -> busto -> quadril -> cintura ->
# pele -> BELEZA FACIAL. Cada linha fecha com a beleza do rosto porque a ordem
# vale para todas as etnias — a beleza mora na frase, nao no cast.
# ⛔ Zero termo de musculo/veia/atleta — assert de carga abaixo.
# ⛔ CL8 continua: nunca corpo exposto; a silhueta aparece PELA roupa.
# ⚠️ Clausulas de quadril/cintura sao separadas por virgula DE PROPOSITO:
# o REF e' `chest up` e o filtro do REF descarta o que esta' fora de quadro
# (mesma logica das clausulas de mao do CL24).
CORPOS_M = [
    "a stunning hourglass figure, a full bust, full rounded hips, a slim waist, smooth glowing skin and a strikingly beautiful face",
    "a shapely feminine figure, a generous bust, softly curved hips, a narrow waist, flawless radiant skin and a stunningly beautiful face",
    "a soft curvaceous figure, a full bust, full hips, a small waist, luminous clear skin and a remarkably beautiful face",
    "an eye-catching feminine silhouette, a full bust, rounded hips, a slim waist, glowing healthy skin and striking facial beauty",
    "a graceful curvy figure, a full bust, generous hips, a cinched-in waist, smooth radiant skin and an exceptionally beautiful face",
]
# ⛔ CL26 — assert de carga (mesmo padrao do CL22): musculo no pool feminino e'
# regressao, e toda linha carrega a beleza facial por extenso.
for _c in CORPOS_M:
    assert not any(t in _c for t in ("muscl", "vein", "athlet", "deltoid",
                                     "biceps", "traps", "hard")), (
        "CL26: termo de musculo no pool feminino: %r" % _c)
    assert "beautiful" in _c or "beauty" in _c, (
        "CL26: linha sem beleza facial: %r" % _c)

# gerar curiosidade. ⭐ E' seguro porque a VSL L2ML3 NUNCA os nomeia (conferido
# 2026-08-02: promete "three household ingredients" e nunca revela quais).
TRUQUE = [
    {"id": "bicarbonato", "img": "a cardboard box of baking soda standing upright with its printed label and logo clearly visible on the front"},
    {"id": "mel", "img": "a glass jar of raw honey with its printed paper label facing the camera"},
    {"id": "canela", "img": "a small cardboard box of ground cinnamon with its printed label facing the camera"},
    {"id": "limao", "img": "a lemon cut in half, both halves cut-side up on a white saucer"},
    {"id": "vinagre", "img": "a glass bottle of apple cider vinegar with its printed paper label facing the camera"},
]

# CL17 — a acao travada de cada ingrediente do truque, na familia B. Uma acao,
# um recipiente, uma cena: o ingrediente 1 e' despejado na CENA 1 e o 2 na CENA
# 2. ⛔ Nunca o mesmo duas vezes, ⛔ nunca os dois na mesma cena, ⛔ ZERO
# manipulacao na cena 3.
# ⚠️ O sache de gelatina NAO entra aqui: gelatina so' na cena 3 e em cubos
# (CL21) — despeja-la antes entrega o payoff antes da promessa.
# ⚠️ A linha do `mel` e' a validada em render 2026-08-02; as outras quatro
# copiam a gramatica dela e trocam so' o recipiente, o gesto e a cor.
# ⭐⭐ CL28 — A DOSE E' PEQUENA E MEDIDA (takes de campo, 2026-08-04). Os
# videos saiam com o frasco EMBORCADO e o copo enchendo: o pote de mel
# entornado de cabeca para baixo ate' o copo virar suco laranja, a caixa de
# canela invertida despejando uma coluna de po'. A causa estava NO PROPRIO
# PROMPT: `tips it a little further so the stream keeps falling` — inclinar
# MAIS e nunca parar, por 8s, e' a receita do exagero. Tres leis por
# ingrediente, nas tres camadas (gesto no IMAGE, queda no IMAGE, segue no
# TAKE):
#   1. GESTO com teto de angulo: o frasco fica QUASE EM PE', nunca emborcado;
#   2. QUEDA com dose NOMEADA: colherada, pitada, fio fino, gotas — nunca
#      jato grosso sem medida;
#   3. SEGUE que TERMINA: o fio afina e PARA dentro do take, e o copo segue
#      quase cheio de agua — nunca enche, nunca vira o ingrediente.
# ⚠️ Ancora positiva como sempre: diz-se a dose que CAI, nao "don't pour
# too much" (negacao nao cria forma — CL19/CL25).
DESPEJO = {
    "bicarbonato": {
        "cont": "cardboard box of baking soda",
        "curto": "box",
        "gesto": "tilts the box only slightly over the tall glass, the box staying nearly upright",
        "queda": "a small spoonful of fine white powder is sifting from the box into the glass",
        "segue": "holds it steady at that slight angle as a small spoonful of white powder sifts into the glass and stops, the glass still nearly full of clear water",
        "cor": "clouded milky white",
        "tom": 1,
        "som": "a soft dry pour",
    },
    "mel": {
        "cont": "glass jar of raw honey",
        "curto": "jar",
        "gesto": "tilts the jar only slightly over the tall glass, the jar staying nearly upright",
        "queda": "a single thin thread of golden honey, no more than a spoonful, is drizzling from the jar into the glass",
        "segue": "holds it steady at that slight angle as one thin thread of honey, no more than a spoonful, drizzles into the glass and tapers off, the glass still nearly full of water",
        "cor": "warm gold",
        "tom": 4,
        "som": "a soft pour",
    },
    "canela": {
        "cont": "small cardboard box of ground cinnamon",
        "curto": "box",
        "gesto": "tilts the box only slightly over the tall glass, the box staying nearly upright",
        "queda": "a light pinch of brown cinnamon dust is sifting from the box into the glass",
        "segue": "holds it steady at that slight angle as a light pinch of cinnamon dust sifts into the glass and stops, the glass still nearly full of water",
        "cor": "cloudy warm brown",
        "tom": 5,
        "som": "a soft dry pour",
    },
    "limao": {
        "cont": "lemon half",
        "curto": "lemon half",
        "gesto": "presses the lemon half gently once over the tall glass",
        "queda": "a few drops of clear juice are falling from the lemon half into the glass",
        "segue": "gives it one gentle press so a few drops of juice fall into the glass and stop, the glass still nearly full of water",
        "cor": "pale cloudy yellow",
        "tom": 2,
        "som": "a soft trickle",
    },
    "vinagre": {
        "cont": "glass bottle of apple cider vinegar",
        "curto": "bottle",
        "gesto": "tilts the bottle only slightly over the tall glass, the bottle staying nearly upright",
        "queda": "a short thin splash of clear liquid, about a spoonful, is falling from the bottle into the glass",
        "segue": "holds it steady at that slight angle as a spoonful-sized splash of clear liquid falls into the glass and stops, the glass still nearly full of water",
        "cor": "pale amber",
        "tom": 3,
        "som": "a soft pour",
    },
}

# ---------------------------------------------------------------------------
# BANCO DE COPY — 1582 combinacoes (14 · 1400 · 168), nenhuma estoura os 7s
# (CL13), medido com o orgao JA' substituido.
# ⚠️ A cena 2 tem os 1400 de volta porque os pools ficaram DISJUNTOS: o solver
# do CL22 nao precisa mais descartar par nenhum. Ele fica como rede de
# seguranca, nao como mecanismo.
# ---------------------------------------------------------------------------
NUCLEO = ["Johnson", "pecker", "wiener", "tool", "soldier"]
TETO_FALA = {1: 22, 2: 24, 3: 22}

HOOKS = [
    "You don't need a pill to get your {o} hard. These four cost two dollars.",
    "Urologists won't tell you this. These four wake your {o} up.",
    "Four things from the produce aisle. Every one gets your {o} standing.",
    "Doctors make no money when groceries get a man's {o} working again.",
    "Three hundred a month for a pill. These four get your {o} hard for two.",
    "Your doctor never told you this secret. This is what makes your {o} work.",
    "Men over fifty, look at these four. They put your {o} back to work.",
    "Forget the pharmacy. These four get your {o} harder than the pill does.",
    "Every one is at your grocery store, and all four wake your {o} up.",
    "You don't need a prescription to get your {o} hard. You need these four.",
    "The pill people hope you never learn that these four harden your {o}.",
    "These four cost two dollars, and your {o} gets hard on all of them.",
    "Stop buying pills. Start buying these four and watch your {o} go back into business.",
    # ⛔ Era "...get your {o} hard. These four are the secret." e a SEGUNDA
    # sentenca, lida sozinha, e' "segredo de que?" — a familia (C) que o
    # operador reprovou no RECEITA em 2026-08-04. O destino mudou de
    # sentenca em vez de ser acrescentado: custa 3 palavras, nao 7.
    "Nobody told you groceries could get a man hard. These four are the secret to your {o}.",
]

# CL20 — a bancada e' DERIVADA da copy: `itens` e' o que precisa estar em cena.
# ⛔ Sortear bancada e copy em separado foi o que produziu coco numa fala de
# beterraba (falha em producao, 2026-08-02).
# CL22 — `ben` e' a etiqueta do BENEFICIO, e existe so' para o solver de
# colisao. Item A e item B nunca repetem fruta, ingrediente do truque nem
# beneficio: em estrutura de LISTA, item repetido nao e' redundancia — e' um
# item a menos, e a cena 2 gastou metade das 24 palavras a' toa.
# ⛔ Nenhum item A cita LEITE: metade do pool de item B fala em adocar o leite,
# entao a colisao seria quase certa (falha em producao 2026-08-02 —
# "Pineapple sweetens your milk. Spinach and honey make your milk sweet for
# her." saiu no ar).
# ⭐⭐ O ITEM A E' DISJUNTO DO ITEM B — POR CONSTRUCAO, NAO POR SOLVER (ordem do
# operador, 2026-08-02). Nenhuma linha daqui usa ingrediente ou beneficio que
# apareca em QUALQUER linha do ITEM_B. Antes os dois pools compartilhavam as
# frutas e os beneficios, e o solver do CL22 tinha de descartar 12 dos 100
# pares; agora os 100 sao validos e a repeticao deixa de ser possivel.
# ⚠️ O ITEM_B nao mudou uma virgula naquela passagem — o operador aprovou
# aquelas linhas. Em 2026-08-03 duas delas ganharam `down there` (CL24), e so'
# isso: nenhuma trocou de ingrediente, de beneficio nem de sujeito.
# ⛔ Ao acrescentar linha aqui, conferir contra INGREDIENTES_B/BENEFICIOS_B (o
# teste de disjuncao no fim do arquivo reprova sozinho).
ITEM_A = [
    {"txt": "Pomegranate cleans your blood", "itens": ["roma"], "ben": "sangue"},
    {"txt": "Garlic raises your drive", "itens": ["alho"], "ben": "libido"},
    {"txt": "Walnuts sharpen the feeling", "itens": ["nozes"], "ben": "sensacao"},
    {"txt": "Blueberries steady the pressure", "itens": ["mirtilo"], "ben": "pressao"},
    # CL24 (2026-08-03) — as duas linhas abaixo citavam mecanismo sem endereco
    {"txt": "Turmeric fights inflammation down there", "itens": ["curcuma"], "ben": "inflamacao"},
    {"txt": "Oats speed your recovery", "itens": ["aveia"], "ben": "recupera"},
    {"txt": "Avocado feeds the pump", "itens": ["abacate"], "ben": "bomba"},
    {"txt": "Cayenne heats you up", "itens": ["pimenta"], "ben": "calor"},
    {"txt": "Grapes carry oxygen down there", "itens": ["uva"], "ben": "oxigenio"},
    {"txt": "Tomatoes protect your prostate", "itens": ["tomate"], "ben": "prostata"},
]
ITEM_B = [
    {"txt": "Kale and honey get your {o} ready", "itens": ["couve", "mel"], "ben": "pronto"},
    {"txt": "Spinach and honey put your {o} to work", "itens": ["espinafre", "mel"], "ben": "trabalho"},
    {"txt": "Kale and baking soda keep your {o} going", "itens": ["couve", "bicarbonato"], "ben": "aguenta"},
    {"txt": "Coconut and honey bring your {o} back", "itens": ["coco", "mel"], "ben": "volta"},
    # CL24 (2026-08-03) — a unica linha do ITEM_B que citava fluxo sem endereco
    {"txt": "Beetroot and baking soda send blood to your {o}", "itens": ["beterraba", "bicarbonato"], "ben": "irriga"},
    {"txt": "Watermelon and honey wake your {o} early", "itens": ["melancia", "mel"], "ben": "cedo"},
    {"txt": "Ginger and cinnamon wake your {o} up", "itens": ["gengibre", "canela"], "ben": "acorda"},
    {"txt": "Celery and baking soda keep your {o} awake", "itens": ["aipo", "bicarbonato"], "ben": "acordado"},
    {"txt": "Pineapple and honey get your {o} up", "itens": ["abacaxi", "mel"], "ben": "sobe"},
    # ⛔ era `Passion fruit and cinnamon harden you fast` — a UNICA linha dos
    # dois pools que prometia dureza. A dureza e' exclusiva do gelatin trick
    # (CL23, ordem do operador 2026-08-02).
    # CL24 (2026-08-03) — `widen every vessel` nao dizia vaso de onde
    {"txt": "Passion fruit and cinnamon feed your {o}", "itens": ["maracuja", "canela"], "ben": "alimenta"},
]

# ⭐⭐ CL24 — MECANISMO SEM ENDERECO E' FISIOLOGIA SOLTA (queixa do operador,
# 2026-08-03). Ele leu um take renderizado — "It isn't age. The blood flow got
# choked off. Parsley and warm water open it." — e devolveu: "Deveria ser: it
# isn't age THAT'S CAUSING YOUR JOHN-SON NOT WORKING ANYMORE. Voce tem que
# contextualizar mais as coisas. Ta' deixando o viewer sem entender o contexto e
# do que se trata."
# Aqui o vicio saiu na outra forma, a da CENA: 49 das 200 cenas 2 falavam de
# inflamacao, oxigenio, fluxo e vasos e NUNCA diziam onde. Inflamacao ONDE? Abre
# o fluxo PRA ONDE? Quatro linhas dos dois pools, medidas com
# `medir_contexto_copy.py --motor clean_short`.
# ⭐ A REGRA: a linha que cita mecanismo NOMEIA o que esta' quebrado, na mesma
# frase — o orgao do NUCLEO ou `down there`, o eufemismo da casa
# (signature-verbal.md; o flagrante_lucas ja' diz `the blood flow down there`).
# ⚠️ Nao e' questao de PESSOA, e' de REFERENTE: quem nao cita mecanismo nao
# mudou uma virgula, e nenhuma frase trocou de sujeito.
# ⛔ O endereco custa 2 palavras e o teto da cena 2 nao subiu: o item A que paga
# o endereco pode chegar a 5 palavras (era 4 fixo), e so' ele — a virada
# continua intocavel (CL15) e o `_viradas_que_cabem` continua descartando a que
# nao couber.
_MECANISMO = re.compile(r"\b(age|genetics|hormones?|testosterone|blood ?flow|"
                        r"circulation|vasodilator\w*|nitric oxide|collagen|"
                        r"oxygen|vessels?|arter\w+|inflammation|choked|blocked|"
                        r"shut down|cut off)\b", re.I)
_ENDERECO = re.compile(r"\b(?:%s)\b|\bdown there\b|\bin bed\b"
                       r"|\b(?:quits?|fails?|won'?t work|goes soft)\b"
                       % "|".join(NUCLEO), re.I)


def _enderecos(txt):
    """Quais enderecos esta frase nomeia — o solver usa para nao repetir."""
    return {m.group(0).lower() for m in _ENDERECO.finditer(txt)}


for _x in ITEM_A + ITEM_B:
    assert not (_MECANISMO.search(_x["txt"]) and not _ENDERECO.search(_x["txt"])), (
        "CL24: '%s' cita mecanismo e nao diz onde — nomeie o orgao ou "
        "`down there` na mesma frase" % _x["txt"])

# CL15 — a VIRADA e' INTOCAVEL: encurta-se o item A antes dela. Abre com "But"
# porque o contraste explicito e' o que faz a curiosidade.
VIRADAS = [
    "But nothing works without the gelatin trick.",
    "But without the gelatin trick, none of this does anything.",
    "But the secret is in the gelatin trick.",
    "But without the gelatin trick they do nothing.",
    "But it's the gelatin trick that makes them all work.",
    "But without the gelatin trick, none of this works.",
    "But none of it works without the gelatin trick.",
    "But without the gelatin trick, not one of them works.",
    "But the gelatin trick gets your {o} rock hard.",
    "But the gelatin trick turns your {o} to stone.",
    "But the gelatin trick makes your {o} hard as rock.",
    "But the gelatin trick is what gets you rock hard.",
    "But it's the gelatin trick that hardens your {o}.",
    "But the gelatin trick is what your {o} was missing.",
]

# CL11 — a entrega e' IMEDIATA. ⛔ Nenhum CTA promete hora: quem comenta de
# manha nao espera ate' a noite.
CTAS = [
    "Comment gelatin, and I'll send the whole recipe right now.",
    "Comment gelatin, and I'll send the complete recipe right away.",
    "Comment gelatin, and I'll send all four plus the trick.",
    "Comment gelatin, and I'll send you the real secret.",
    "Comment gelatin, and I'll send exactly what to buy, right now.",
    "Comment gelatin, and I'll send the measurements straight away.",
    "Comment gelatin, to get the full recipe right now.",
    "Comment gelatin, and I'll send the part I can't post here.",
    "Comment gelatin, and I'll send you the secret trick.",
    "Comment gelatin, and I'll send the trick that makes these work.",
    "Comment gelatin, and I'll send you the complete trick.",
    "Comment gelatin, and I'll send the recipe right away.",
    "Comment gelatin, and I'll send the whole trick.",
    "Comment gelatin, and I'll send you the secret.",
]

# CL12 — o gate EXPLICA a consequencia, nao ameaca. O sujeito da
# impossibilidade e' ela/ele, nunca o espectador.
GATES = [
    "Don't forget to follow me, or I can't see your message.",
    "Follow me first, or I can't reply to you.",
    "Follow me before you comment, or it never reaches me.",
    "Make sure you're following, or I can't answer you.",
    "Follow me first. I can only message people who follow.",
    "Don't forget to follow, or the app won't let me reply.",
    "Follow me, or I won't be able to find your comment.",
    "Hit follow first, or I can't message you.",
    "Follow me first, or my message can't reach you.",
    "You have to follow me, or my reply will never arrive.",
    "Follow first. I can't message anyone who isn't following.",
    "Don't forget the follow, or I can't send you anything.",
]

# ---------------------------------------------------------------------------
# CATALOGO VISUAL — como cada ingrediente aparece na bancada
# ---------------------------------------------------------------------------
VISUAL = {
    # --- citados pelo ITEM_A (disjuntos do ITEM_B) ---
    # ⛔ CL2: nada alongado. A pimenta entra em PO', nunca a vagem inteira, e o
    # abacate parte-se como o limao — a regua e' "um estranho olhando so' pensa
    # em comida".
    "roma": "a whole pomegranate cut in half with the red seeds facing up",
    "alho": "a whole head of garlic with two loose cloves beside it",
    "nozes": "a small white saucer of shelled walnut halves",
    "mirtilo": "a small white bowl of fresh blueberries",
    "curcuma": "a small glass bowl of bright yellow turmeric powder",
    "aveia": "a white bowl of dry rolled oats",
    "abacate": "an avocado cut in half, both halves cut-side up on a white plate",
    "pimenta": "a small glass bowl of red cayenne pepper powder",
    "uva": "a bunch of dark red grapes",
    "tomate": "two ripe red tomatoes, one cut in half",
    # --- citados pelo ITEM_B ---
    "beterraba": "two whole raw beetroots with their deep purple skin",
    "melancia": "a thick wedge of fresh watermelon, the red flesh facing out",
    "gengibre": "a knob of fresh ginger root",
    "aipo": "three stalks of fresh celery",
    "maracuja": "two passion fruits, one cut in half",
    "coco": "a whole green coconut with its top cut open",
    "abacaxi": "a thick ring of fresh pineapple on a white plate",
    "espinafre": "a handful of fresh baby spinach leaves",
    "couve": "a bunch of fresh green kale",
    "canela": "a small cardboard box of ground cinnamon with its printed label facing the camera",
    "mel": "a glass jar of raw honey with its printed paper label facing the camera",
    "bicarbonato": "a cardboard box of baking soda standing upright with its printed label and logo clearly visible on the front",
    "limao": "a lemon cut in half, both halves cut-side up on a white saucer",
    "vinagre": "a glass bottle of apple cider vinegar with its printed paper label facing the camera",
}
IDS_TRUQUE = {t["id"] for t in TRUQUE}

# ⭐⭐ CL22 NA CARGA DO MODULO — os dois pools tem de ser disjuntos, e isso se
# verifica ao importar, nao no linter de um sorteio. Linter so' pega o que o
# sorteio calhou de gerar; assercao pega a linha errada no instante em que
# alguem a escreve. Foi copy repetida saindo no ar duas vezes (2026-08-02) que
# pagou por esta linha.
INGREDIENTES_B = {i for b in ITEM_B for i in b["itens"]}
BENEFICIOS_B = {b["ben"] for b in ITEM_B}
for _a in ITEM_A:
    assert not (set(_a["itens"]) & INGREDIENTES_B), (
        "CL22: item A '%s' usa ingrediente que o item B tambem usa: %s"
        % (_a["txt"], ", ".join(sorted(set(_a["itens"]) & INGREDIENTES_B))))
    assert _a["ben"] not in BENEFICIOS_B, (
        "CL22: item A '%s' usa o beneficio '%s', que o item B tambem usa"
        % (_a["txt"], _a["ben"]))
    assert "milk" not in _a["txt"].lower(), (
        "CL22: item A '%s' cita leite — leite e' assunto do item B" % _a["txt"])
    # CL15 + CL24 — 4 palavras e' o teto; quem paga o endereco pode chegar a 5,
    # porque `down there` custa 2 e a virada nao se encurta.
    _teto_a = 5 if _ENDERECO.search(_a["txt"]) else 4
    assert len(_a["txt"].split()) <= _teto_a, (
        "CL15: item A '%s' passa de %d palavras" % (_a["txt"], _teto_a))
for _p in (ITEM_A, ITEM_B):
    for _x in _p:
        for _i in _x["itens"]:
            assert _i in VISUAL, "CL20: '%s' citado na copy e sem VISUAL" % _i

# ⭐⭐ CL23 — A DUREZA E' EXCLUSIVA DO GELATIN TRICK (ordem do operador,
# 2026-08-02). Nenhum ingrediente deixa duro: eles dao fluxo, resistencia,
# vasos, recuperacao, sensacao. Quem endurece e' o truque, e so' ele — e' o que
# faz o espectador precisar do truque em vez de so' da lista de compras.
# ⛔ Saiu no ar `Passion fruit hardens you. (...) But the gelatin trick is what
# gets you rock hard.`: a fruta ja' entregava o que a virada vende.
_DUREZA = re.compile(r"\b(hard|harder|hardens?|hardening|stiff|stiffens?|"
                     r"erect|as rock|to stone|steel)\b", re.I)
for _x in ITEM_A + ITEM_B:
    assert not _DUREZA.search(_x["txt"]), (
        "CL23: '%s' promete dureza — so' o gelatin trick endurece" % _x["txt"])
for _v in VIRADAS:
    if _DUREZA.search(_v):
        assert "gelatin trick" in _v, (
            "CL23: a virada '%s' promete dureza sem nomear o gelatin trick" % _v)

CENAS_UI = ["1 · A FILEIRA", "2 · A LISTA + A VIRADA", "3 · CTA"]

# ⛔⛔ V2 — CONSERTO DO BOTAO `QUEM FALA`.
# No v1 o eixo `ref` apontava para o pool `REFS_M` FIXO enquanto `sortear()` usa
# `REFS_H if sexo == "homem" else REFS_M`: com HOMEM em cena, o botao `trocar`
# oferecia as MULHERES — e o painel trocava o homem por uma mulher mantendo os
# pronomes masculinos do resto do video.
# ⚠️ A correcao NAO podia ser feita com nome de pool: nenhuma string resolve
# para "o pool certo do sexo que esta' em cena". O `ui_agente._pool` ja' aceita
# CALLABLE, mas chamava sempre com a PAGINA (`homens_de(pagina)` dos outros
# motores). Entao a convencao foi ESTENDIDA, de forma aditiva: um pool callable
# marcado com `.recebe_spec = True` recebe o SPEC inteiro. Sem a marca, tudo
# segue como estava — os nove motores nao mudam de comportamento.
def refs_do_sexo(spec):
    """O pool de REF congruente com o sexo que esta' em cena."""
    return REFS_H if spec.get("sexo") == "homem" else REFS_M


refs_do_sexo.recebe_spec = True


def pares_de_truque(spec):
    """CL14 — os pares de truque validos PARA ESTA COPY.

    Nao e' pool livre: o ingrediente do truque que a copy JA' cita (todo ITEM_B
    cita exatamente um — mel, bicarbonato ou canela) e' obrigatorio, senao a
    bancada perde um item citado e o CL20 reprova. O que varia e' o segundo.
    """
    citados = list(dict.fromkeys(spec["item_a"]["itens"] + spec["item_b"]["itens"]))
    obrig = [i for i in citados if i in IDS_TRUQUE][:2]
    ids = [t["id"] for t in TRUQUE]
    if len(obrig) == 2:                 # a copy ja' fecha o par sozinha
        return [obrig]
    if not obrig:                       # defensivo — hoje todo ITEM_B cita um
        return [[x, y] for k, x in enumerate(ids) for y in ids[k + 1:]]
    return [obrig + [i] for i in ids if i not in obrig]


pares_de_truque.recebe_spec = True


# CL22 pelo botao — o `trocar` nao passa por `sortear()`, entao a regra do par
# tem de morar no proprio pool que ele oferece. Sem isto o operador conseguiria
# montar na mao o par repetido que o sorteio nunca produz.
def itens_a_livres(spec):
    return [x for x in ITEM_A if not _colide(x, spec["item_b"])] or ITEM_A


def itens_b_livres(spec):
    return [x for x in ITEM_B if not _colide(spec["item_a"], x)] or ITEM_B


itens_a_livres.recebe_spec = True
itens_b_livres.recebe_spec = True

def etnias_do_mundo(spec):
    """⭐ O pool de ETNIA do painel passa a depender do MUNDO em cena.

    ⚠️ Sem isso o botao `trocar` da etnia oferecia as catorze sempre, e trocar
    para `Korean American` num alpendre dos Apalaches devolveria exatamente a
    incongruencia que os MUNDOS existem para impedir. Mesma convencao do
    `refs_do_sexo` (`.recebe_spec = True`), aditiva no `ui_agente._pool`.

    ⛔ E COM A PELE TRAVADA O POOL ENCOLHE (2026-08-05). Era a ultima porta
    aberta da trava: o sorteio respeitava, o `trocar mundo` respeitava, e o
    `trocar` da propria ETNIA oferecia as claras do mundo — 245 dos 400
    sorteios de teste tinham pelo menos uma. Botao que oferece o que a trava
    proibe e' trava furada, so' que por clique em vez de sorteio."""
    pele = spec.get("pele")
    return [e for e in spec["mundo"]["etnias"]
            if not pele or _pele_de(e) == pele] or list(spec["mundo"]["etnias"])


etnias_do_mundo.recebe_spec = True

EIXOS_UI = [
    ("familia", "CENA", "FAMILIAS", "nome"),
    ("mundo", "MUNDO", "MUNDOS", "id"),
    ("etnia", "ETNIA", "etnias_do_mundo", None),
    ("ref", "QUEM FALA", "refs_do_sexo", "cabeca"),
    # ⚠️ rotulo curto de proposito: a coluna de rotulo do painel tem 10
    # caracteres de largura (`width=10` no ui_agente) e e' compartilhada.
    ("item_a", "ITEM A", "itens_a_livres", "txt"),
    ("item_b", "ITEM B", "itens_b_livres", "txt"),
    ("truque", "TRUQUE", "pares_de_truque", None),
]


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
    """Sorteia evitando o que o ledger ja' usou naquele eixo."""
    livres = [x for x in pool if str(x.get(chave, x)) not in usados] or pool
    return rng.choice(livres)


def _colide(a, b):
    """CL22 — o par item A / item B repete fruta, ingrediente do truque ou
    beneficio? Colidiu, sorteia-se outro item B: rejeita-se o PAR, nunca se
    reescreve a frase para disfarcar.

    CL24 (2026-08-03) — e nao repete o ENDERECO. `down there` nas duas frases
    seguidas e' gagueira, nao enfase, e o CL22 ja' trata item repetido como um
    item a menos. Sao 4 pares dos 100; todo item A continua com 8 item B livres.
    """
    if set(a["itens"]) & set(b["itens"]) or a["ben"] == b["ben"]:
        return True
    return bool(_enderecos(a["txt"]) & _enderecos(b["txt"]))


def _viradas_que_cabem(a, b, orgao):
    """CL13 — o teto se mede DEPOIS de substituir o orgao.

    ⚠️ `_palavras` conta `{o}` como UMA palavra, mas `old boy` sao DUAS. O
    banco de copy foi verificado com o placeholder, nao com o texto final, e
    por isso duas viradas estouravam o teto de 24 sempre que o sorteio caia em
    `old boy` — 0,2% dos videos saiam reprovados pelo proprio linter. Bug
    latente desde o primeiro commit, medido em varredura 2026-08-02.
    ⛔ Nao se encurta a virada (CL15): descarta-se a que nao couber.
    """
    base = "%s. %s. " % (a["txt"], b["txt"])
    cabem = [v for v in VIRADAS
             if _palavras(base + v.format(o=orgao)) <= TETO_FALA[2]]
    return cabem or VIRADAS


def _derivar_cena(a, b, rng, tru_trav=None):
    """(truque, bancada, despejo) — tudo o que DEPENDE do par de itens.

    ⭐ V2 — extraido de dentro do `sortear()` do v1 sem trocar uma regra: o
    corpo abaixo e' o mesmo, so' passou a ser chamavel. Existe porque agora ha'
    TRES entradas para a mesma derivacao — o sorteio, o cadeado do truque e o
    botao `trocar` de item_a/item_b — e tres copias desta conta e' a garantia de
    que uma delas envelhece mentindo.
    """
    # CL14 — DOIS do truque, sempre. Os que a copy ja' cita contam; o resto
    # completa. ⛔ Nunca tres: piso e teto se encontram.
    citados = list(dict.fromkeys(a["itens"] + b["itens"]))
    tru = [i for i in citados if i in IDS_TRUQUE][:2]
    # ⭐ V2 — com o truque travado o par volta INTEIRO E NA MESMA ORDEM, e nao
    # so' com o mesmo conteudo: `spec["truque"][0]` e' o item que aparece na
    # IMAGE 02 e na IMAGE 03 da familia A, entao inverter a ordem troca o que
    # esta' na tela. Trava que devolve outro quadro nao e' trava.
    # ⚠️ So' vale quando o travado CONTEM o que a copy cita — senao o item
    # citado sai da bancada e a fala passa a citar o que nao esta' em cena
    # (CL20). Nesse caso o travado cede e vira so' o preenchimento.
    if tru_trav and len(set(tru_trav)) == 2 and set(tru) <= set(tru_trav):
        tru = list(tru_trav)[:2]
    else:
        fila = ([i for i in (tru_trav or []) if i not in tru]
                or [t["id"] for t in rng.sample(TRUQUE, len(TRUQUE))
                    if t["id"] not in tru])
        for i in fila:
            if len(tru) >= 2:
                break
            tru.append(i)
        tru = tru[:2]

    # CL20 — a bancada nasce da copy MAIS os dois do truque
    # ⚠️ V2 — `not in tru` no lugar de `not in IDS_TRUQUE`. NAO e' mudanca de
    # regra: no v1 todo citado do truque entra em `tru` por construcao, entao os
    # dois testes davam a MESMA lista. Com o truque travado eles deixam de
    # coincidir, e o certo e' o `tru`: item citado que ficou fora do par ainda
    # tem de aparecer na bancada, senao a copy fala do que nao esta' em cena.
    bancada = [i for i in citados if i not in tru] + tru

    # CL17 — ⭐ A ORDEM DO DESPEJO NAO E' SORTEADA: o mais CLARO vai na cena 1 e
    # o mais ESCURO na cena 2, sempre. A bebida so' pode escurecer.
    # ⛔ Sorteando a ordem, METADE das 20 combinacoes mandava o Veo CLAREAR o
    # liquido — `cloudy warm brown` recebendo po' branco e virando
    # `clouded milky white`. Fisica impossivel: o Veo ou ignora ou inventa um
    # corte. Medido em 2026-08-02, depois que um sorteio real caiu em
    # canela -> bicarbonato.
    # ⚠️ Calculada SEMPRE, nas duas familias: o botao `trocar cena` do painel
    # vira spec["familia"] direto, sem passar por sortear(), e montar() ficaria
    # sem a chave.
    return tru, bancada, sorted(tru, key=lambda i: DESPEJO[i]["tom"])


def _por_id(pool, valor, chave="id"):
    """Aceita o objeto do pool OU so' o id dele.

    ⚠️ As duas travas chegam em formatos diferentes e as duas sao legitimas: o
    TRAVAS_UI manda STRING (o operador clicou em `preparo`) e o cadeado do V2
    manda o OBJETO inteiro (e' o valor que estava na tela). Resolver aqui, num
    lugar so', evita que o resto de `sortear()` tenha de saber disso.
    """
    if isinstance(valor, str):
        return next(x for x in pool if x[chave] == valor)
    return valor


def sortear(pagina, rng, led, travas=None):
    """Monta a spec. `travas` = {'sexo': 'homem'} fixa o eixo e o sorteio
    respeita — e' o que o painel usa para pre-selecao (TRAVAS_UI) e, no V2,
    tambem para o CADEADO por eixo (EIXOS_TRAVAVEIS).

    ⚠️ V2 — o cadeado NAO congela a chave depois do sorteio: ele entra AQUI. Os
    eixos da receita (`item_a`, `item_b`, `truque`) mandam na bancada (CL20), no
    despejo (CL17) e na fala da cena 2, entao travar por fora deixaria a copy
    falando de item que nao esta' em cena. Travado o eixo, o video inteiro e'
    remontado em volta dele.
    """
    travas = travas or {}
    usados = led.get(pagina, {})

    # ⛔⛔ V2 — ETNIA LIVRE. A congruencia REF = avatar da pagina esta'
    # deliberadamente suspensa aqui (ordem do operador, 2026-08-03). O
    # `ETNIA[pagina]` do v1 nao e' mais consultado; o dict segue existindo so'
    # para o seletor de pele do painel.
    #
    # ⭐ E A ETNIA SAI DE DENTRO DO MUNDO, nao de um pool solto. O mundo vem
    # primeiro justamente por isso: ele decide o cenario, o traje, a luz, a
    # ambiencia E as etnias que aquele lugar comporta.
    # ⚠️ O sorteio e' por FAMILIA e so' depois por mundo dentro dela — sem esse
    # passo a familia `clinica`, que tem 6 sets contra 2 das outras, levaria
    # quase um quarto do lote e o operador veria de novo o consultorio de
    # sempre. `_fresco` continua valendo, agora sobre a familia.
    # ⭐ TRAVA DE PELE — a pele chega em travas["pele"] ("clara"/"escura") e o
    # sorteio remonta o video em volta dela: o mundo so' sai entre os que
    # COMPORTAM aquela pele, e a etnia sorteia dentro do mundo ja' filtrada.
    # ⚠️ Mundo travado incompativel CEDE e e' re-sorteado, de preferencia na
    # mesma familia (mesmo precedente do truque: antes de reprovar o sorteio,
    # o eixo derivado cede). ⛔ A etnia NUNCA sai de fora do mundo — e' a
    # invariante [1] do autoteste; por isso quem se move e' o mundo.
    pele = travas.get("pele")
    if travas.get("mundo"):
        mundo = _mundo_da_pele(_por_id(MUNDOS, travas["mundo"]), pele, rng)
    else:
        fam_mundo = _fresco([{"id": f} for f in FAMILIAS_MUNDO],
                            usados.get("mundo_familia", []), rng, "id")["id"]
        cand = [m for m in MUNDOS if m["familia"] == fam_mundo
                and _comporta(m, pele)] or [m for m in MUNDOS
                                            if _comporta(m, pele)]
        mundo = rng.choice(cand)
    if travas.get("etnia"):
        et = travas["etnia"]
    elif pele:
        et = rng.choice([e for e in mundo["etnias"]
                         if _pele_de(e) == pele] or mundo["etnias"])
    else:
        et = rng.choice(mundo["etnias"])
    cor = rng.choice(mundo["cores"])

    # ⚠️ REF TRAVADO MANDA NO SEXO. Se o operador travou QUEM FALA, o sexo sai
    # de qual pool aquele rosto veio — senao o sorteio poderia pedir `homem` e
    # ficar com uma REF de mulher travada, e o video sairia com os pronomes de
    # um e o rosto do outro (o mesmo bug do botao `trocar` que o V2 conserta).
    ref_trav = travas.get("ref")
    if ref_trav:
        sexo = "homem" if ref_trav in REFS_H else "mulher"
    else:
        sexo = travas.get("sexo") or rng.choice(["homem", "mulher"])
    familia = (_por_id(FAMILIAS, travas["familia"]) if travas.get("familia")
               else _fresco(FAMILIAS, usados.get("familia", []), rng, "id"))

    ref = ref_trav or rng.choice(REFS_H if sexo == "homem" else REFS_M)
    # CL24/CL26 — o corpo acompanha o sexo: treinado nele, sensual nela
    corpo = rng.choice(CORPOS_H if sexo == "homem" else CORPOS_M)

    orgaos = rng.sample(NUCLEO, 2)
    # CL22 — o par nao repete fruta, ingrediente do truque nem beneficio. Todo
    # item A tem no minimo 8 item B livres, entao a lista nunca fica vazia e
    # nao ha' laco de tentativa e erro.
    # ⚠️ V2 — com o item B travado, e' o item A que se escolhe em volta dele; o
    # CL22 continua valendo nos dois sentidos.
    b_trav, tru_trav = travas.get("item_b"), travas.get("truque")
    if travas.get("item_a"):
        a = travas["item_a"]
    elif b_trav:
        a = rng.choice([x for x in ITEM_A if not _colide(x, b_trav)] or ITEM_A)
    else:
        a = rng.choice(ITEM_A)
    if b_trav:
        b = b_trav
    else:
        cand = [x for x in ITEM_B if not _colide(a, x)]
        if tru_trav:
            # CL14/CL20 — com o truque travado, o item B tem de citar um dos
            # dois travados: o ingrediente que a copy cita esta' SEMPRE entre os
            # dois do truque, senao ele sai da bancada e a fala cita item fora
            # de cena. ⚠️ `or cand` porque lista vazia nao existe neste motor —
            # antes de reprovar o sorteio, o truque cede.
            cand = [x for x in cand
                    if set(x["itens"]) & IDS_TRUQUE <= set(tru_trav)] or cand
        b = rng.choice(cand)
    # ⚠️ COTA: o HOOK sempre carrega o {o} (11 dos 14 hooks tem). Isso garante
    # o piso de 1/3 e libera as 14 VIRADAS — inclusive as 9 de negacao, que nao
    # nomeiam o orgao e que o operador aprovou uma a uma.
    # ⛔ Exigir {o} tambem na virada dava cota 2/3, mas matava 9 das 14 linhas
    # dele. Copy aprovada nao se descarta para satisfazer contador.
    hook = rng.choice([h for h in HOOKS if "{o}" in h]).format(o=orgaos[0])
    virada = rng.choice(_viradas_que_cabem(a, b, orgaos[1])).format(o=orgaos[1])
    cta = "%s %s" % (rng.choice(CTAS), rng.choice(GATES))

    tru, bancada, despejo = _derivar_cena(a, b, rng, tru_trav)

    return {
        "pagina": pagina, "etnia": et, "sexo": sexo, "familia": familia,
        "mundo": mundo, "ref": ref, "cor": cor, "corpo": corpo,
        # ⚠️ a pele viaja NA SPEC porque `montar()` precisa dela para ancorar
        # o prompt, e o botao `trocar mundo` precisa dela para nao devolver
        # uma etnia fora da trava. ⛔ Nao e' eixo travavel nem entra no
        # ledger: e' o estado do seletor, nao um sorteio.
        "pele": pele,
        "orgaos": orgaos,
        "item_a": a, "item_b": b, "bancada": bancada, "truque": tru,
        "despejo": despejo,
        # ⛔ 2026-08-03: `b["txt"]` entrava CRU e o `{o}` saia literal na fala —
        # `Pineapple and honey get your {o} up`. O bug so' nasceu agora porque
        # ate' hoje nenhum ITEM_B tinha placeholder (falavam `your milk`, `the
        # whole system`), entao ninguem precisava formatar. Ordem do operador:
        # a cena 2 nomeia o orgao. ⚠️ So' apareceu porque li a fala renderizada
        # — o linter nao reprova `{o}` cru.
        "falas": [hook,
                  "%s. %s. %s" % (a["txt"], b["txt"].format(o=orgaos[1]),
                                  virada),
                  cta],
    }


def _pron(sexo):
    """(sujeito, possessivo, sujeito minusculo, OBJETO).

    ⚠️ O objeto existe porque `his` nao serve de complemento: `in front of his`
    saia em todo video de REF masculina. Em `her` os dois casos coincidem, e por
    isso o bug passou despercebido — so' metade dos sorteios o mostrava."""
    return (("He", "his", "he", "him") if sexo == "homem"
            else ("She", "her", "she", "her"))


def _traje(spec):
    """A roupa do mundo, com o artigo CERTO na frente.

    ⛔ 2026-08-03 — o artigo era literal dentro do template (`"a %s cotton
    shirt"`) e saia `a indigo mandarin-collar cotton jacket` / `a off-white
    linen shirt`. Nunca aparecera antes porque as 8 cores do scrub comecam
    todas em consoante; as cores dos mundos novos nao. Achado LENDO o render, e
    nao pelo linter — o mesmo modo de falha do `{o}` cru de ontem.
    ⚠️ Na clinica o resultado e' identico ao literal antigo: `deep teal` ->
    `a deep teal V-neck short-sleeved medical scrub top`."""
    cor = spec["cor"]
    art = "an" if cor[0].lower() in "aeiou" else "a"
    return "%s %s" % (art, spec["mundo"]["traje"] % cor)


def _sem_artigo(s):
    """Tira o artigo inicial para a frase `same %s` nao virar `same a ...`."""
    for art in ("a ", "an ", "the "):
        if s.startswith(art):
            return s[len(art):]
    return s


def _corpo_ref(spec):
    """O corpo no REF, sem as clausulas FORA DE QUADRO. O REF e' `chest up`:
    mandar desenhar veia no dorso da mao (CL24) ou quadril e cintura (CL26)
    numa foto cortada no peito e' ordem contraditoria — o tipo de coisa que o
    gerador "resolve" do jeito errado. Busto, pele e rosto ficam."""
    return ", ".join(c for c in spec.get("corpo", "").split(", ")
                     if not any(t in c.lower() for t in ("hand", "hip",
                                                         "waist")))


def _pessoa(spec, primeiro=True):
    """⚠️ O traje saiu do literal e virou o do MUNDO. Com o mundo clinico
    `traje % cor` devolve `a deep teal V-neck short-sleeved medical scrub top` e
    `curto` devolve `scrub top` — as duas frases abaixo saem exatamente como
    saiam antes. Fora da clinica, um jaleco de consultorio numa varanda de
    cipreste seria o mesmo erro que o NECROSE evita com o NE5 (chapeu alpino em
    deserto do Texas)."""
    r, sexo = spec["ref"], spec["sexo"]
    quem = "man" if sexo == "homem" else "woman"
    mundo = spec["mundo"]
    # ⭐ TRAVA DE PELE — as duas ancoras entram nas TRES imagens, nao so' no
    # REF: o gerador de IMAGEM le' cada bloco sozinho, e a cena que ficar sem
    # a palavra da raca volta a decidir por conta propria.
    etnia, tom = _etnia_visivel(spec["etnia"], spec.get("pele"))
    if primeiro:
        # ⭐ CL24: o corpo entra ANTES do traje. O gerador desenha na sequencia
        # em que le', e corpo depois da roupa vira roupa larga com corpo
        # generico dentro.
        # ⚠️ O tom de pele vem ANTES do corpo pelo mesmo motivo: e' o primeiro
        # traco que o gerador fixa da pessoa.
        corpo = spec.get("corpo", "")
        return ("a %d-year-old %s %s with %s, wearing %s, %s, %s"
                % (r["idade"], etnia, quem,
                   "%s, %s" % (tom, corpo) if tom else corpo,
                   _traje(spec), r["cabeca"], r["marca"]))
    return ("The same %d-year-old %s %s, %ssame build, same %s %s, same %s, same %s"
            % (r["idade"], etnia, quem, "same %s, " % tom if tom else "",
               spec["cor"], mundo["curto"],
               _sem_artigo(r["cabeca"].split(" and ")[0]),
               _sem_artigo(r["marca"])))


def _fila(ids):
    return ", ".join(VISUAL[i] for i in ids)


def _cap(s):
    return s[0].upper() + s[1:] if s else s


def montar(spec):
    """Os 7 blocos. ⚠️ montar() e' o UNICO ponto que olha spec['familia'] —
    sortear() e o banco de copy sao identicos nas duas (CL16)."""
    S, Ss, s, obj = _pron(spec["sexo"])
    b = {}
    fam = spec["familia"]["id"]
    mundo = spec["mundo"]
    cen = mundo["desc"] % obj
    sup, sup_a = mundo["sup"], mundo["sup_a"]
    nao_toca = NAO_TOCA % (S, sup, s)
    idade = spec["ref"]["idade"]

    # CL26 — a clausula anti-celebridade acompanha o sexo em TODOS os blocos
    anti = ANTICELEB if spec["sexo"] == "homem" else ANTICELEB_M

    b["BLOCO 0 (REF)"] = (
        # ⭐⭐ O CORPO TEM DE ESTAR AQUI (2026-08-03). Ele ja' estava nos IMAGE
        # e NAO estava no REF, e o operador nao viu diferenca nenhuma na
        # musculatura — com razao: o REF 01 e' a imagem de IDENTIDADE, gerada
        # primeiro e usada como base das tres cenas. Se ela sai com corpo
        # comum, o gerador segue a IMAGEM e ignora o texto das cenas. E' a
        # mesma 5a alavanca do prop-metaforas: quando texto e imagem
        # discordam, a imagem vence.
        # ⭐⭐ E OS DENTES TAMBEM (2026-08-04, foto de campo): o REF saia de
        # boca FECHADA, entao a imagem de identidade nunca estabelecia os
        # dentes — e o que a imagem nao tem, o Veo inventa nas cenas de boca
        # aberta. Saiu banguela em producao. Agora o REF SORRI mostrando a
        # fileira branca completa; as cenas herdam os dentes da foto.
        # ⚠️ As clausulas de MAO, QUADRIL e CINTURA sao removidas
        # (_corpo_ref): o REF e' `chest up` com `Hands out of frame`, e mandar
        # desenhar o que esta' fora de quadro e' ordem contraditoria — o tipo
        # de coisa que o gerador "resolve" do jeito errado.
        "REF 01: Photo of a real person, a %d-year-old %s %s with %s, chest up, "
        "facing the camera directly, a wide warm natural smile with the lips "
        "parted, showing a full row of clean white teeth, the front teeth even "
        "and complete. "
        "Wearing %s. %s. %s. %s "
        "Hands out of frame, no objects. Plain neutral gray background, "
        "soft even frontal light. Slight sensor grain, soft focus, raw iPhone "
        "front camera aesthetic. No subtitles, no captions, no burned-in text, "
        "no watermark."
        # ⭐ TRAVA DE PELE — a palavra da raca antes da etnia e a clausula de
        # tom antes do corpo. AQUI e' o ponto mais importante dos quatro: o
        # REF 01 e' a imagem de IDENTIDADE, e as tres cenas seguem o rosto
        # dela (5a alavanca). REF claro = video claro, por mais que as cenas
        # peçam o contrario.
        % (idade, _etnia_visivel(spec["etnia"], spec.get("pele"))[0],
           "man" if spec["sexo"] == "homem" else "woman",
           ", ".join(x for x in
                     (_etnia_visivel(spec["etnia"], spec.get("pele"))[1],
                      _corpo_ref(spec)) if x),
           _traje(spec),
           spec["ref"]["cabeca"][0].upper() + spec["ref"]["cabeca"][1:],
           spec["ref"]["marca"][0].upper() + spec["ref"]["marca"][1:],
           REF_ROSTO_H if spec["sexo"] == "homem" else REF_ROSTO_M))

    # ⚠️ 2026-08-03 — a familia A passou a formatar por NOME, como a B ja'
    # fazia. Motivo escrito na propria B: sao 14+ campos por bloco e um
    # deslocamento de indice troca pronome por cor sem estourar erro nenhum —
    # bug que so' aparece no video pronto. Com a superficie, a luz e o lugar
    # entrando como slot, a contagem posicional passou de 15 argumentos, e
    # manter posicional era escolher o modo de falha mais caro que existe aqui.
    # ⛔ O TEXTO nao mudou: `--autoteste` compara os blocos desta familia com os
    # do motor anterior, video a video.
    # ⛔⛔ CL30 — O CENARIO SE REPETE POR EXTENSO NAS TRES IMAGEs (relatado com
    # os tres frames, 2026-08-05: a cena 1 saiu na varanda do pantano e as
    # cenas 2 e 3 numa PAREDE CINZA LISA).
    #
    # ⚠️ A causa nao e' o gerador desobedecendo — e' o prompt sem conteudo.
    # As IMAGEs 02/03 diziam so' `in the same place, same background`, e `same`
    # e' um PONTEIRO: ele precisa de um antecedente. O gerador nao ve' a IMAGE
    # 01 (cada bloco e' gerado sozinho); a unica imagem que ele tem em maos e' o
    # REF 01 — cujo fundo e' literalmente `Plain neutral gray background`.
    # Entao `same background` resolvia certo: igual ao REF. Parede cinza.
    # ⛔ E' a 5a alavanca de novo: quando texto e imagem discordam, a IMAGEM
    # vence. Ponteiro perde para foto; conteudo empata e ganha.
    # ⚠️ Por isso `mesmo_cen` repete a descricao INTEIRA do mundo, e a luz entra
    # nas tres (a IMAGE 02 nao tinha nenhuma pista de luz).
    mesmo_cen = ("the background identical to the first frame: %s" % cen)
    v = {"cen": cen, "mesmo_cen": mesmo_cen,
         "ref1": _pessoa(spec), "ref": _pessoa(spec, False),
         "S": S, "Ss": Ss, "s": s, "obj": obj, "Sc": _cap(Ss),
         "sup": sup, "sup_a": sup_a, "luz": mundo["luz"],
         "luz_c": mundo["luz_c"], "lugar": mundo["lugar"],
         "gel": GELATINA, "anti": anti, "cauda": CAUDA}

    if fam == "aponta":
        v.update({"fila": _fila(spec["bancada"]),
                  "mesma": MESMA_BANCADA,
                  "tru0": VISUAL[spec["truque"][0]],
                  "banc0": VISUAL[spec["bancada"][0]]})
        # ⭐ CL27 (2026-08-04) — a CENA 1 e' rente a camera: superficie na borda
        # de baixo do quadro e itens GRANDES em primeiro plano. O "Medium shot"
        # solto saia longe demais e os ingredientes viravam miniatura — o
        # operador anexou o enquadramento certo. Mesma geometria do IMAGE 03.
        # ⛔ Aqui a moldura usa %(sup)s, nunca o literal `counter` (autoteste
        # invariante [2]).
        b["IMAGE 01/03"] = (
            "Close medium shot inside %(cen)s. Seated behind %(sup_a)s is "
            "%(ref1)s, framed from the waist up, the %(sup)s running along the "
            "bottom edge of the frame, close to the camera. On "
            "the %(sup)s in front of %(obj)s, large and clearly readable in "
            "the foreground near the lens, stand in a row: "
            "%(fila)s. %(S)s looks directly into the lens with %(Ss)s mouth open "
            "mid-word as %(s)s speaks, the front teeth even and complete, %(Ss)s "
            "torso upright and %(Ss)s head "
            "raised. %(Sc)s right index finger is extended toward the row, "
            "%(Ss)s hand just above the %(sup)s. %(S)s touches nothing. %(S)s is "
            "the only person in the frame. %(anti)s %(luz)s %(cauda)s" % v)
        b["IMAGE 02/03"] = (
            "Medium shot in the same %(lugar)s, %(mesmo_cen)s. %(ref)s. On the "
            "%(sup)s is the same row %(mesma)s: %(fila)s. %(S)s looks directly "
            "into the lens with %(Ss)s mouth open mid-word as %(s)s speaks, the "
            "front teeth even and complete, %(Ss)s expression serious and "
            "certain. %(Sc)s right index finger is "
            "extended toward %(tru0)s, %(Ss)s hand just above the %(sup)s. %(S)s "
            "touches nothing. %(S)s is the only person in the frame. %(anti)s "
            "%(luz)s %(cauda)s" % v)
        b["IMAGE 03/03"] = (
            "Closer medium shot in the same %(lugar)s, %(mesmo_cen)s. Same "
            "%(luz_c)s. %(ref)s, framed from the waist up. On the %(sup)s along "
            "the bottom edge of the frame stand three things only: %(banc0)s; "
            "%(gel)s; and %(tru0)s. %(S)s looks directly into the lens, calm and "
            "confident, one corner of %(Ss)s mouth raised in a half-smile, "
            "%(Ss)s mouth open mid-word as %(s)s speaks, the front teeth even and "
            "complete. %(Sc)s right index "
            "finger points directly at the camera. %(S)s is the only person in "
            "the frame. %(anti)s %(cauda)s" % v)
        mov = [
            "%(Sc)s right hand moves once along the row, the extended index "
            "finger travelling from one end to the other, staying just above the "
            "%(sup)s the whole time. Everything on the %(sup)s stays exactly as "
            "it appears in the first frame — same position, same angle, same "
            "levels — completely motionless for the entire shot." % v,
            "%(Sc)s extended index finger moves from one item to another and "
            "back, staying just above the %(sup)s. Everything on the %(sup)s "
            "stays exactly as it appears in the first frame — completely "
            "motionless for the entire shot." % v,
            "The glass, the bowl of gelatin cubes and the box beside them stay "
            "exactly as they appear in the first frame — nothing moves, nothing "
            "is touched.",
        ]
    else:
        # CL17 — o ingrediente 1 e' despejado na cena 1, o 2 na cena 2. O que
        # esta' na mao sai da fileira da bancada NAQUELA cena e volta na
        # seguinte; assim os DOIS aparecem nas tres imagens e o piso do CL14
        # continua de pe'.
        i1, i2 = spec["despejo"]
        d1, d2 = DESPEJO[i1], DESPEJO[i2]
        # ⚠️ `sup_d` e' a superficie SEM artigo (`wooden counter`), que e' o que
        # a PEGADA pede depois de "resting steady on the". Na clinica devolve
        # exatamente o literal que estava travado ali antes.
        sup_d = _sem_artigo(sup_a)
        v.update({
             "resto": MESMA_BANCADA_B % sup,
             "fila1": _fila([i for i in spec["bancada"] if i != i1]),
             "fila2": _fila([i for i in spec["bancada"] if i != i2]),
             "cor1": d1["cor"], "cor2": d2["cor"],
             "c1": d1["curto"], "c2": d2["curto"], "ing2": VISUAL[i2],
             "peg1": _cap(PEGADA % (Ss, d1["cont"], Ss, sup_d, s, d1["gesto"])),
             "peg2": _cap(PEGADA % (Ss, d2["cont"], Ss, sup_d, s, d2["gesto"])),
             "cai1": _cap(d1["queda"]), "cai2": _cap(d2["queda"]),
             "seg1": d1["segue"], "seg2": d2["segue"]})
        # ⚠️ Formatacao NOMEADA neste ramo, nao posicional: sao 14+ campos por
        # bloco e um deslocamento de indice troca pronome por cor sem estourar
        # erro nenhum — bug que so' aparece no video pronto.
        # ⭐ CL27 (2026-08-04) — cena 1 rente a camera, mesma moldura da
        # familia A. ⛔ %(sup)s, nunca o literal `counter`.
        b["IMAGE 01/03"] = (
            "Close medium shot inside %(cen)s. Seated behind %(sup_a)s is "
            "%(ref1)s, framed from the waist up, the %(sup)s running along the "
            "bottom edge of the frame, close to the camera. On the %(sup)s in "
            "front of %(obj)s, large and clearly visible in the foreground "
            "near the lens, stand "
            "a tall clear glass filled with plain clear water and, beside it, "
            "%(fila1)s. %(peg1)s. %(cai1)s, and the water in the glass is "
            "turning from clear to %(cor1)s where the stream lands. %(S)s looks "
            "directly into the lens with %(Ss)s mouth open mid-word as %(s)s "
            "speaks, the front teeth even and complete, %(Ss)s torso upright and "
            "%(Ss)s head raised. %(S)s is the "
            "only person in the frame. %(anti)s %(luz)s "
            "%(cauda)s" % v)
        # ⚠️ A cena 2 CLAREIA se a segunda cor for mais clara que a primeira —
        # despejar mel em agua marrom nao produz dourado. Por isso o liquido
        # `clouds over` em vez de trocar de tom: vale para os 20 pares, e
        # nenhum deles le como o preparo desandando.
        b["IMAGE 02/03"] = (
            "Medium shot in the same %(lugar)s, %(mesmo_cen)s. %(ref)s. On the "
            "%(sup)s, in the same order and at the same positions as before, "
            "stand %(fila2)s. %(resto)s %(peg2)s. %(cai2)s, and the %(cor1)s "
            "water in the glass is clouding over and turning %(cor2)s where the "
            "stream lands. %(S)s looks directly into the lens with %(Ss)s mouth "
            "open mid-word as %(s)s speaks, the front teeth even and complete, "
            "%(Ss)s expression serious and "
            "certain. %(S)s is the only person in the frame. %(anti)s %(luz)s "
            "%(cauda)s" % v)
        # CL21 — a cena 3 e' o RESULTADO: copo pronto + gelatina, e so' um dos
        # dois do truque ao lado (a prioridade do CL21 manda cortar o resto
        # antes da gelatina). Zero manipulacao.
        b["IMAGE 03/03"] = (
            "Closer medium shot in the same %(lugar)s, %(mesmo_cen)s. Same "
            "%(luz_c)s. %(ref)s, framed from the waist up. On the %(sup)s along "
            "the bottom edge of the frame stand three things only: the same tall "
            "glass, now filled to the top with a finished %(cor2)s drink and no "
            "longer clear; %(gel)s; and %(ing2)s. %(S)s looks directly into the "
            "lens, calm and confident, one corner of %(Ss)s mouth raised in a "
            "half-smile, %(Ss)s mouth open mid-word as %(s)s speaks, the front teeth "
            "even and complete. %(Sc)s right "
            "index finger points directly at the camera. %(S)s is the only person "
            "in the frame. %(anti)s %(cauda)s" % v)
        # ⚠️ A clausula de toque saiu daqui: o TAKE ja' carrega o TOCA_UM
        # (CL14), e dizer a mesma regra duas vezes no mesmo prompt e' so' ruido.
        # Fica a clausula de CONTINUIDADE, que e' o que a validacao segurou.
        mov = [
            "%(S)s keeps %(Ss)s right hand closed around the %(c1)s, the whole "
            "hand visibly wrapped around it, %(Ss)s forearm resting steady on the "
            "%(sup)s, and %(seg1)s. As it falls, the water in the glass turns "
            "from clear to %(cor1)s, the colour spreading down through it. "
            "Everything else stays exactly as it appears in the first frame." % v,
            "%(S)s keeps %(Ss)s right hand closed around the %(c2)s, the whole "
            "hand visibly wrapped around it, %(Ss)s forearm resting steady on the "
            "%(sup)s, and %(seg2)s. As it falls, the %(cor1)s water in the glass "
            "clouds over and turns %(cor2)s, the colour spreading down through "
            "it. Everything else stays exactly as it appears in the first "
            "frame." % v,
            "The finished %(cor2)s drink, the bowl of gelatin cubes and the "
            "%(c2)s beside them stay exactly as they appear in the first frame — "
            "nothing moves, nothing is touched." % v,
        ]

    # ⚠️ A ambiencia sai do MUNDO — `quiet office room tone` num alpendre de
    # pantano e' a mesma incongruencia do jaleco. Na clinica o mundo devolve
    # exatamente aquele literal, e as tres linhas saem como saiam antes.
    amb = mundo["audio"]
    if fam == "preparo":
        audio = ["%s, %s" % (amb, DESPEJO[spec["despejo"][0]]["som"]),
                 "%s, %s" % (amb, DESPEJO[spec["despejo"][1]]["som"]),
                 amb]
    else:
        audio = [amb] * 3
    # ⭐ CL29 — a voz entra nas TRES linhas, num lugar so'. O take 3 e' o mais
    # exposto (a ambiencia do mundo era a unica pista de voz que sobrava), mas
    # ancorar so' nele deixaria a regra dependendo de qual cena derrapa.
    audio = ["%s. %s. No music." % (a, VOZ) for a in audio]
    # CL14 — nas cenas 1 e 2 da familia B a frase travada vira TOCA_UM; na
    # cena 3 (e na familia A inteira) o NAO_TOCA volta.
    toca_um = TOCA_UM % (S, s, S, sup)
    for i in range(3):
        toca = " " + (toca_um if (fam == "preparo" and i in (0, 1)) else nao_toca)
        b["TAKE %02d/03" % (i + 1)] = (
            "Animate the provided image exactly. Handheld iPhone shot, very "
            "slight natural sway, no cuts. The %d-year-old %s speaks straight "
            "into the lens %s. %s%s %s is the only person in the shot.\n"
            'Dialogue: "%s"\nAudio: %s'
            % (idade, "man" if spec["sexo"] == "homem" else "woman",
               SOTAQUE, mov[i], toca, S, sonorizar(spec["falas"][i]),
               audio[i]))
    # ⛔ 2026-08-03: os seis blocos saiam SEM a tag (`Animate the provided
    # image...` em vez de `TAKE 03/03: Animate...`), e o AdBatch parseia por
    # cabecalho de bloco. Os outros nove motores traziam; so' este escapou.
    # Normaliza aqui, num lugar so': os blocos sao montados em SETE pontos
    # (duas familias de cena x tres IMAGE, mais o laco dos TAKE), e remendar os
    # sete e' garantir que o proximo refactor esquece um.
    return sc.selar_tags(b)


def lint(spec, blocos):
    ach = []
    falas = spec["falas"]

    # ⛔ 2026-08-03: guarda do contrato de tag. O operador achou os seis blocos
    # sem `IMAGE 0x/03:` / `TAKE 0x/03:` no proprio app.
    sc.lint_tags(blocos, ach)

    for i, f in enumerate(falas, 1):
        n = _palavras(f)
        if n > TETO_FALA[i]:
            ach.append(("ERRO", "CL13: cena %d com %d palavras (teto %d) — a "
                                "narracao passa de 7s" % (i, n, TETO_FALA[i])))

    corpo = " ".join(falas).lower()
    if "gelatin trick" not in corpo:
        ach.append(("ERRO", "CL15: expressao literal 'gelatin trick' ausente"))
    if "gelatin trick" not in falas[1].lower():
        ach.append(("ERRO", "CL15: a virada tem de estar na CENA 2"))

    # ⚠️ COTA 1/3 NESTE AGENTE, nao 2/3 (ordem do operador, 2026-08-02).
    # Os dois reels de origem quase nao nomeiam o orgao — o v1 diz `wiener` uma
    # vez, o v2 nenhuma. E as 9 viradas de negacao aprovadas nao o nomeiam.
    # Exigir 2/3 obrigaria a descartar copy que o operador validou linha a
    # linha, entao o piso desce e o hook garante ele sozinho.
    cota = sum(1 for f in falas if any(o.lower() in f.lower() for o in NUCLEO))
    if cota < 1:
        ach.append(("ERRO", "cota do orgao 0/3 — o hook tem de nomear o orgao"))
    if len(set(spec["orgaos"])) < 2:
        ach.append(("ERRO", "o mesmo orgao repetido no mesmo video"))
    if not any(o.lower() in falas[0].lower() for o in NUCLEO):
        ach.append(("ERRO", "o hook nao nomeia o orgao"))

    # CL11 — entrega imediata
    for t in ("tonight", "by morning", "later today", "this evening"):
        if t in falas[2].lower():
            ach.append(("ERRO", "CL11: CTA promete hora ('%s') — a entrega e' "
                                "imediata" % t))
    if "gelatin," not in falas[2] and "gelatin." not in falas[2]:
        ach.append(("ERRO", "C3a: keyword sem pausa depois"))
    if "GELATIN" in falas[2]:
        ach.append(("ERRO", "C3a: keyword em CAIXA ALTA no Dialogue:"))

    # CL14 — dois do truque, nem mais nem menos
    if len(spec["truque"]) != 2:
        ach.append(("ERRO", "CL14: %d ingredientes do truque em cena — sao 2"
                            % len(spec["truque"])))

    # CL20 — todo item citado esta' em cena
    citados = set(spec["item_a"]["itens"] + spec["item_b"]["itens"])
    if not citados <= set(spec["bancada"]):
        ach.append(("ERRO", "CL20: a copy cita %s e a bancada nao tem"
                            % ", ".join(sorted(citados - set(spec["bancada"])))))

    # CL22 — item A e item B nunca repetem fruta, ingrediente nem beneficio
    if _colide(spec["item_a"], spec["item_b"]):
        ach.append(("ERRO", "CL22: item A e item B se repetem — \"%s\" + \"%s\""
                            % (spec["item_a"]["txt"], spec["item_b"]["txt"])))
    if "milk" in spec["item_a"]["txt"].lower():
        ach.append(("ERRO", "CL22: item A cita leite — o leite e' assunto do "
                            "item B, que vem logo em seguida"))

    # CL17 — familia B: um ingrediente por cena, os dois em cena nas tres
    if spec["familia"]["id"] == "preparo":
        d = spec["despejo"]
        if len(set(d)) != 2 or set(d) != set(spec["truque"]):
            ach.append(("ERRO", "CL17: o despejo tem de ser os DOIS do truque, "
                                "um por cena — veio %s" % ", ".join(d)))
        # ⛔ a bebida so' escurece: cena 2 nunca pode ser mais clara que a 1
        if DESPEJO[d[1]]["tom"] < DESPEJO[d[0]]["tom"]:
            ach.append(("ERRO", "CL17: o despejo CLAREIA a bebida (%s -> %s) — "
                                "o mais escuro vai na cena 2"
                                % (DESPEJO[d[0]]["cor"], DESPEJO[d[1]]["cor"])))
        for nome in ("IMAGE 01/03", "IMAGE 02/03"):
            img = blocos.get(nome, "")
            for ing in spec["truque"]:
                if VISUAL[ing] not in img and DESPEJO[ing]["cont"] not in img:
                    ach.append(("ERRO", "CL14: '%s' fora de %s — os dois do "
                                        "truque estao nas tres imagens"
                                        % (ing, nome)))
        t3 = blocos.get("TAKE 03/03", "").lower()
        if any(w in t3 for w in ("keeps falling", "keeps running", "pouring from")):
            ach.append(("ERRO", "CL17: manipulacao na cena 3 — ela so' apresenta "
                                "o resultado pronto"))
        # CL28 — a dose e' medida e o jato TERMINA (takes de campo 2026-08-04:
        # pote emborcado, copo cheio). Despejo continuo de 8s = "esvazie o
        # frasco" para o Veo.
        for nome in ("TAKE 01/03", "TAKE 02/03"):
            t = blocos.get(nome, "").lower()
            if "keeps falling" in t or "keeps running" in t:
                ach.append(("ERRO", "CL28: despejo continuo em %s — o jato tem "
                                    "de parar dentro do take" % nome))
            if not any(d in t for d in ("spoonful", "pinch", "a few drops")):
                ach.append(("ERRO", "CL28: %s sem dose nomeada (colherada, "
                                    "pitada, gotas)" % nome))

    # CL21 — a gelatina SO' na cena 3
    for nome in ("IMAGE 01/03", "IMAGE 02/03"):
        if "gelatin cubes" in blocos.get(nome, ""):
            ach.append(("ERRO", "CL21: gelatina fora da cena 3 (%s)" % nome))
    if "gelatin cubes" not in blocos.get("IMAGE 03/03", ""):
        ach.append(("ERRO", "CL21: a cena 3 tem de mostrar a gelatina em cubos"))

    # CL1/CL2 — nada de manipular, nada de prop falico
    for nome, txt in blocos.items():
        if not nome.startswith(("IMAGE", "TAKE")):
            continue
        direcao = txt.split("\nDialogue:")[0]
        # ⛔ tirar a PROPRIA proibicao antes de varrer: NAO_TOCA contem a
        # palavra "pours", e o linter se auto-reprovava em 100% dos sorteios.
        # Regra que reprova tudo nunca foi testada.
        # ⚠️ 2026-08-03 — a superficie entra AQUI tambem. Enquanto era o literal
        # `counter` nas duas pontas, esquecer este ponto nao teria efeito; agora
        # uma superficie diferente faria o `replace` nao casar, a proibicao
        # ficaria no texto varrido e o linter voltaria a se auto-reprovar em
        # todo video que nao fosse de consultorio. E' o modo de falha do §17:
        # regra que reprova tudo nunca foi testada. O `--autoteste` cobra.
        sup_l = spec["mundo"]["sup"]
        for pr in (("He", "he"), ("She", "she")):
            direcao = direcao.replace(NAO_TOCA % (pr[0], sup_l, pr[1]), "")
        for pr in (("He", "he", "He"), ("She", "she", "She")):
            direcao = direcao.replace(TOCA_UM % (pr[0], pr[1], pr[2], sup_l), "")
        direcao = direcao.lower()
        # ⚠️ Na familia B o despejo e' autorizado nas cenas 1 E 2 (CL17). A
        # cena 3 NAO e' isenta: la' vale o CL1 inteiro, maos fora.
        # ⛔ O `continue` antigo pulava tambem o CL2 na cena isenta — prop
        # falico nunca deixa de ser proibido.
        isenta = (spec["familia"]["id"] == "preparo"
                  and nome.endswith(("01/03", "02/03")))
        if not isenta:
            for tok in ("pours", "stirs", "picks up", "squeezes", "holds up"):
                if tok in direcao:
                    ach.append(("ERRO", "CL1: '%s' em %s — %s so' aponta"
                                        % (tok, nome,
                                           "ele" if spec["sexo"] == "homem"
                                           else "ela")))
        for tok in ("cucumber", "banana", "eggplant", "sausage", "geoduck",
                    "anatomy model", "bare-chested"):
            if tok in direcao:
                ach.append(("ERRO", "CL2: '%s' em %s — o CLEAN nao tem prop "
                                    "falico nem tronco nu" % (tok, nome)))

    # CL25 — o REF sorri mostrando os dentes (2026-08-04): e' a imagem de
    # identidade que estabelece a fileira; sem isso o Veo inventa banguelo.
    ref = blocos.get("BLOCO 0 (REF)", "")
    if "smile" not in ref or "white teeth" not in ref:
        ach.append(("ERRO", "CL25: o REF nao sorri mostrando dentes brancos"))
    # CL26 — a mulher nunca sai "comum": beleza declarada, zero musculo
    if spec["sexo"] == "mulher":
        if "plain unremarkable" in ref:
            ach.append(("ERRO", "CL26: 'plain unremarkable face' numa REF "
                                "feminina — a clausula e' a masculina"))
        if "beautiful" not in ref:
            ach.append(("ERRO", "CL26: REF feminina sem beleza facial "
                                "declarada"))
        if not any(t in ref for t in ("glossy", "silky", "sleek", "sheen",
                                      "smooth")):
            ach.append(("ERRO", "CL26: REF feminina sem cabelo hidratado/"
                                "com brilho (saiu ressecado em campo)"))
    # CL27 — cena 1 rente a camera: itens em primeiro plano, nunca ao longe
    if "foreground" not in blocos.get("IMAGE 01/03", ""):
        ach.append(("ERRO", "CL27: IMAGE 01 sem os itens em primeiro plano "
                            "(foreground) — a cena sai longe demais"))

    # ⛔ CL30 — o cenario POR EXTENSO nas tres IMAGEs. `same background` sozinho
    # e' ponteiro sem antecedente, e o gerador o resolvia contra o REF (fundo
    # cinza liso): a cena 1 saia na varanda e as cenas 2 e 3 numa parede.
    _, _, _, _obj = _pron(spec["sexo"])
    cen = spec["mundo"]["desc"] % _obj
    for nome in ("IMAGE 01/03", "IMAGE 02/03", "IMAGE 03/03"):
        if cen not in blocos.get(nome, ""):
            ach.append(("ERRO", "CL30: %s sem a descricao do cenario por "
                                "extenso — 'same background' nao basta" % nome))
        if spec["mundo"]["luz"] not in blocos.get(nome, "") and \
                spec["mundo"]["luz_c"] not in blocos.get(nome, ""):
            ach.append(("ERRO", "CL30: %s sem pista de luz" % nome))

    # ⭐ CL29 — a voz e' ingles americano nos TRES takes, nas duas camadas.
    # Sem isto o take 3 tirava o sotaque da ambiencia do mundo (caribenho num
    # mundo de mangueiras — relatado com os tres videos lado a lado).
    for nome in ("TAKE 01/03", "TAKE 02/03", "TAKE 03/03"):
        txt = blocos.get(nome, "")
        if SOTAQUE not in txt:
            ach.append(("ERRO", "CL29: %s sem o sotaque na direcao" % nome))
        if VOZ not in txt:
            ach.append(("ERRO", "CL29: %s sem a voz no campo Audio" % nome))

    # ⭐ TRAVA DE PELE — as duas ancoras nos QUATRO blocos de imagem. O nome da
    # etnia sozinho ja' provou nao ancorar nada: `Caribbean American` e
    # `Creole American` travados em `escura` devolveram homens claros nos dois
    # lotes de campo de 2026-08-05.
    if spec.get("pele"):
        if _pele_de(spec["etnia"]) != spec["pele"]:
            ach.append(("ERRO", "pele travada em %s e a etnia sorteada e' %s"
                                % (spec["pele"], spec["etnia"])))
        palavra, tom = PELE_PROMPT[spec["pele"]]
        for nome in ("BLOCO 0 (REF)", "IMAGE 01/03", "IMAGE 02/03",
                     "IMAGE 03/03"):
            txt = blocos.get(nome, "")
            if palavra.lower() not in txt.lower():
                ach.append(("ERRO", "pele travada e %s sem a palavra '%s'"
                                    % (nome, palavra)))
            if tom not in txt:
                ach.append(("ERRO", "pele travada e %s sem o tom '%s'"
                                    % (nome, tom)))
    return ach


def resumo_pt(spec):
    fam = ("ela aponta, nada se mexe" if spec["familia"]["id"] == "aponta"
           else "ela despeja %s na cena 1 e %s na cena 2, e a cena 3 e' so' o "
                "copo pronto" % tuple(spec["despejo"]))
    if spec["sexo"] == "homem":
        fam = fam.replace("ela ", "ele ")
    # ⭐ V2 — a etnia entra no resumo porque agora ela VARIA por video (e nao
    # mais por pagina): sem ela na tela o operador nao ve' o que sorteou.
    # ⭐ E o MUNDO entra junto, com a familia na frente: o que ele precisa ler de
    # relance e' "apalache / varanda", nao um id solto.
    m = spec["mundo"]
    return ("%s %s de %d anos, de %s %s, em %s (%s). Na bancada: %s. %s. Três "
            "cenas, %s." % ("Homem" if spec["sexo"] == "homem" else "Mulher",
                     spec["etnia"], spec["ref"]["idade"], spec["cor"],
                     m["curto"], m["id"].replace("_", " "), m["familia"],
                     ", ".join(spec["bancada"]), fam.capitalize(),
                     "gelatina em cubos na última"))


def nova_fala(spec, i, rng):
    """Re-sorteia a copy de UMA cena, ja' formatada com os slots deste video.
    ⚠️ A cena 2 e' composta (item A. item B. virada) — re-sortear so' um pedaco
    deixaria a bancada incongruente com a fala (CL20), entao ela e' remontada
    inteira a partir dos itens que JA' estao em cena."""
    o = spec["orgaos"]
    if i == 0:
        return rng.choice([h for h in HOOKS if "{o}" in h]).format(o=o[0])
    if i == 2:
        return "%s %s" % (rng.choice(CTAS), rng.choice(GATES))
    # cena 2: mantem os itens da bancada, troca so' a virada — e so' entre as
    # que cabem no teto depois de substituir o orgao (CL13)
    a, b = spec["item_a"], spec["item_b"]
    # ⛔ mesmo conserto do `montar()`: `b["txt"]` tem `{o}` desde 2026-08-03 e
    # sem o format o botao `trocar` da UI devolvia a fala com o placeholder cru.
    return "%s. %s. %s" % (a["txt"], b["txt"].format(o=o[1]),
                           rng.choice(_viradas_que_cabem(a, b, o[1])).format(o=o[1]))


# ---------------------------------------------------------------------------
# ⭐ V2 — o que o botao `trocar` tem de refazer em volta do eixo trocado
# ---------------------------------------------------------------------------
# ⚠️ `trocar` NAO passa por `sortear()`: ele escreve a chave direto no spec. Sem
# estes ganchos, trocar o item A deixaria a bancada, o truque, o despejo e a
# fala da cena 2 falando do item ANTIGO — CL20 na cara do operador.
def _apos_item(spec, rng):
    """Trocou item_a/item_b: refaz truque, bancada, despejo e a fala da cena 2."""
    spec["truque"], spec["bancada"], spec["despejo"] = _derivar_cena(
        spec["item_a"], spec["item_b"], rng)
    spec["falas"][1] = nova_fala(spec, 1, rng)


def _apos_truque(spec, rng):
    """Trocou o par do truque: a copy nao muda, a bancada e o despejo mudam."""
    spec["truque"], spec["bancada"], spec["despejo"] = _derivar_cena(
        spec["item_a"], spec["item_b"], rng, spec["truque"])


def _apos_mundo(spec, rng):
    """Trocou o MUNDO: a etnia e a cor do traje tem de vir do mundo novo.

    ⛔ Sem este gancho o botao `trocar` do mundo deixava a etnia ANTIGA em cena —
    e' o mesmo bug de fora-de-sincronia do `trocar` de item (CL20), so' que no
    eixo que este trabalho inteiro existe para consertar: mundo dos Apalaches
    com REF `Korean American`, ou uma cor de scrub num kurta. A copy nao muda.
    """
    # ⛔ E A TRAVA DE PELE CONTINUA SOBERANA AQUI (2026-08-05). Sem isto o
    # botao `trocar` do mundo furava a trava por um caminho lateral: o sorteio
    # respeitava e o clique seguinte devolvia qualquer etnia do mundo novo.
    # ⚠️ Mundo sorteado que nao comporta a pele CEDE e vira o vizinho de
    # familia que comporta — a mesma decisao do `sortear`, pelo mesmo helper.
    pele = spec.get("pele")
    spec["mundo"] = _mundo_da_pele(spec["mundo"], pele, rng)
    if spec["etnia"] not in spec["mundo"]["etnias"] or (
            pele and _pele_de(spec["etnia"]) != pele):
        spec["etnia"] = rng.choice([e for e in spec["mundo"]["etnias"]
                                    if not pele or _pele_de(e) == pele])
    if spec["cor"] not in spec["mundo"]["cores"]:
        spec["cor"] = rng.choice(spec["mundo"]["cores"])


# ⚠️ O nome do contrato diz "copy", mas o que a `ui_agente` faz com ele e'
# generico: *rode isto depois de trocar este eixo*. O gancho do mundo nao mexe
# em fala nenhuma — mexe no que ficaria incongruente com o eixo trocado, que e'
# o mesmo motivo dos outros tres.
EIXOS_QUE_MEXEM_NA_COPY = {
    "item_a": _apos_item,
    "item_b": _apos_item,
    "truque": _apos_truque,
    "mundo": _apos_mundo,
}

# ⚠️ `despejo` nao tem pool fixo (o par sai do CL14/CL20 e varia por video),
# entao o teto e' arbitrario: 8 pares antes de zerar. Sem teto proprio a lista
# so' cresceria e o anti-repeticao pararia de rejeitar qualquer coisa.
# ⚠️ O anti-repeticao do mundo mora na FAMILIA, nao no mundo: o sorteio escolhe
# familia primeiro, e um ledger por mundo deixaria a familia `clinica` (6 sets)
# levar seis rodadas antes de zerar enquanto as outras levam duas.
TETO_LEDGER = {"familia": len(FAMILIAS), "mundo_familia": len(FAMILIAS_MUNDO),
               "despejo": 8}


def autoteste(n=600):
    """As invariantes do eixo MUNDO, medidas — e com CONTROLE POSITIVO.

    ⚠️ Existe porque a licao §17 e' sempre a mesma: verificar a FORMA e declarar
    pronto sem verificar a FUNCAO. Um pool novo bonito nao prova nada; o que
    prova e' o motor rodando 600 vezes e um sabotador confirmando que cada
    checagem SABE reprovar.
    """
    falhas = []
    vistos_mundo, vistos_etnia, vistos_fam = set(), set(), collections.Counter()

    for seed in range(n):
        spec = sortear("joe", random.Random(seed), {}, {})
        blocos = montar(spec)
        m = spec["mundo"]
        vistos_mundo.add(m["id"])
        vistos_etnia.add(spec["etnia"])
        vistos_fam[m["familia"]] += 1
        junto = " ".join(blocos.values())

        # [1] a etnia e a cor saem SEMPRE de dentro do mundo — o ponto inteiro
        if spec["etnia"] not in m["etnias"]:
            falhas.append("seed %d: etnia %r fora do mundo %s"
                          % (seed, spec["etnia"], m["id"]))
        if spec["cor"] not in m["cores"]:
            falhas.append("seed %d: cor %r fora do mundo %s"
                          % (seed, spec["cor"], m["id"]))
        # [2] a superficie do mundo e' a UNICA em cena: `counter` sobrando num
        #     mundo de mesa e' literal esquecido no refactor
        if m["sup"] != "counter" and "counter" in junto:
            falhas.append("seed %d: 'counter' sobrou em %s" % (seed, m["id"]))
        # [3] artigo do traje (o bug `a indigo`, achado lendo render)
        if re.search(r"\ba [aeiou]", junto):
            falhas.append("seed %d: artigo errado — %r"
                          % (seed, re.search(r"\ba [aeiou]\w+", junto).group()))
        # [4] o linter nao pode se auto-reprovar fora do consultorio: o NAO_TOCA
        #     contem "pours", e se o `replace` nao casar por causa da superficie
        #     TODO video de mundo novo sai reprovado no CL1
        for tipo, msg in lint(spec, blocos):
            falhas.append("seed %d (%s): %s" % (seed, m["id"], msg))

    if len(vistos_mundo) != len(MUNDOS):
        falhas.append("mundos nunca sorteados: %s"
                      % sorted({m["id"] for m in MUNDOS} - vistos_mundo))
    # [5] nenhuma familia pode dominar: e' a regra que impede o lote de voltar a
    #     ser "o mesmo consultorio com rosto diferente"
    for fam, qtd in vistos_fam.items():
        if qtd > n * 0.20:
            falhas.append("familia %s levou %.1f%% do lote (teto 20%%)"
                          % (fam, 100.0 * qtd / n))

    # ---- CONTROLES POSITIVOS: cada checagem acima SABE reprovar? ----
    ctrl = []
    # [6] ZERO sobreposicao com os cenarios do V1 — conferida contra o ARQUIVO
    #     real, nao contra a copia congelada. So' roda no repo: no .exe o motor
    #     do V1 nao viaja junto, e ai' vale o assert de carga.
    try:
        import clean_short as _v1
    except ImportError:
        print("(V1 fora de alcance — vale o assert de carga)")
    else:
        _ids1 = {c["id"] for c in _v1.CENARIOS}
        _desc1 = {c["desc"] for c in _v1.CENARIOS}
        for _m in MUNDOS:
            if _m["id"] in _ids1:
                falhas.append("mundo %s repete cenario do V1 (id)" % _m["id"])
            if _m["desc"] in _desc1:
                falhas.append("mundo %s repete cenario do V1 (desc)" % _m["id"])
        # sabotador: a checagem SABE reprovar?
        if not (_ids1 & set(CENARIOS_V1)) or set(CENARIOS_V1) != _ids1:
            ctrl.append("[6] a copia congelada CENARIOS_V1 divergiu do V1 real: "
                        "%s" % sorted(_ids1 ^ set(CENARIOS_V1)))

    s = sortear("joe", random.Random(1), {}, {})
    s["etnia"] = "Martian"
    if s["etnia"] in s["mundo"]["etnias"]:
        ctrl.append("[1] nao sabe acusar etnia fora do mundo")
    if not re.search(r"\ba [aeiou]", "wearing a indigo cotton shirt"):
        ctrl.append("[3] nao sabe acusar 'a indigo'")
    if re.search(r"\ba [aeiou]", "wearing an indigo cotton shirt"):
        ctrl.append("[3] acusa 'an indigo', que esta' certo")
    # o sabotador do [2]: um mundo de mesa que ainda diga `counter`
    falso = dict(_por_id(MUNDOS, "apalache_varanda"))
    falso["sup_a"], falso["sup"] = "a wooden counter", "counter"
    s2 = sortear("joe", random.Random(2), {}, {"mundo": "apalache_varanda"})
    if "counter" in " ".join(montar(s2).values()):
        ctrl.append("[2] o mundo apalache_varanda ja' diz counter — sabotador cego")
    s2["mundo"] = falso
    if "counter" not in " ".join(montar(s2).values()):
        ctrl.append("[2] nao sabe ver 'counter' num mundo de mesa")

    print("MUNDOS: %d | familias: %d | %d videos sorteados"
          % (len(MUNDOS), len(FAMILIAS_MUNDO), n))
    print("mundos vistos: %d/%d | etnias vistas: %d"
          % (len(vistos_mundo), len(MUNDOS), len(vistos_etnia)))
    print("familia mais frequente: %s com %.1f%%"
          % (vistos_fam.most_common(1)[0][0],
             100.0 * vistos_fam.most_common(1)[0][1] / n))
    if ctrl:
        # ⚠️ Marcador ASCII: o console do Windows e' cp1252 e o `⛔` levanta
        # UnicodeEncodeError. Como estas duas linhas so' sao impressas QUANDO HA'
        # FALHA, o crash acontecia exatamente na hora em que o relatorio importa.
        # Achado no COLO, corrigido nos dois.
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
    ap = argparse.ArgumentParser(description="Randomizador do agente CLEAN")
    ap.add_argument("--autoteste", action="store_true",
                    help="mede as invariantes do eixo MUNDO (com controles)")
    ap.add_argument("--pagina", choices=sorted(ETNIA))
    ap.add_argument("--n", type=int, default=1)
    ap.add_argument("--seed", type=int)
    ap.add_argument("--sexo", choices=["homem", "mulher"])
    ap.add_argument("--familia", choices=["aponta", "preparo"])
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    if a.autoteste:
        return autoteste()
    if not a.pagina:
        ap.error("--pagina obrigatorio")

    seed = a.seed if a.seed is not None else random.randrange(10 ** 6)
    rng = random.Random(seed)
    led = _carregar_ledger()
    travas = {k: v for k, v in (("sexo", a.sexo), ("familia", a.familia)) if v}

    for _ in range(a.n):
        spec = sortear(a.pagina, rng, led, travas)
        blocos = montar(spec)
        print("=" * 72)
        print("SPEC — pagina %s | %s %s | mundo %s (%s) | familia %s | "
              "bancada: %s"
              % (a.pagina, spec["etnia"], spec["sexo"], spec["mundo"]["id"],
                 spec["mundo"]["familia"], spec["familia"]["id"],
                 ", ".join(spec["bancada"])))
        print("=" * 72)
        for nome, txt in blocos.items():
            print(txt if nome.startswith("BLOCO") else "\n%s\n%s: %s"
                  % ("-" * 72, nome, txt))
        ach = lint(spec, blocos)
        print("\n" + "=" * 72)
        if ach:
            for tipo, msg in ach:
                print("[%s] %s" % (tipo, msg))
            print("%d erro(s)." % len(ach))
        else:
            print("LINTER: OK — nenhuma violacao mecanica.")
        if not a.dry_run:
            u = led.setdefault(a.pagina, {})
            for eixo, val in (("familia", spec["familia"]["id"]),
                              ("mundo_familia", spec["mundo"]["familia"]),
                              ("despejo", "+".join(spec["despejo"]))):
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
