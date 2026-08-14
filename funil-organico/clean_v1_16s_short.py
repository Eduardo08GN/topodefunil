#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
clean_v1_16s_short.py — o AGENTE CLEAN V1 em DOIS TAKES (16 segundos).

⭐⭐ COPIA LITERAL DO `clean_short.py` (V1), adaptada SO' NO EIXO TEMPORAL.
Ordem do operador, 2026-08-08: *"o ajuste aqui e' apenas no eixo temporal: nao
sacrifique, diminua ou faca quaisquer regressao que ocasione perda de entropia
ao adequar temporalmente o agente"*. Por isso nenhum pool encolheu — dois
cresceram.

⛔ O V1 ORIGINAL NAO FOI TOCADO. Este arquivo e' agente NOVO, com ledger
proprio, teto de 30 posts proprio e pastas proprias no Angulos.

O QUE MUDOU EM RELACAO AO V1
  · 3 cenas de 8s  ->  2 cenas de 8s (teto de 20 palavras por take, ~7s de
    narracao com 1s de margem, que foi a margem que ele pediu)
  · a cena 2 do V1 (ITEM_A + ITEM_B + VIRADA) some como CENA; a virada migra
    para o take 2 e o item entra nele quando cabe. Os dois pools continuam
    sorteados e continuam montando a BANCADA — o que caiu foi a fala, nao a
    entropia visual (ordem dele: *"libera so' 1 item, mantendo os outros na
    imagem pra despertar a curiosidade visual"*).
  · HOOKS 14 -> 30 (os 14 do V1 + 3 moldes que ele escreveu + 13 aprovados
    um a um em 2026-08-08)
  · CTAS reescritos: todos NOMEIAM O FORMATO VIDEO e PROMETEM a entrega —
    citar o video sem prometer o envio foi reprovado por ele
  · GATES comprimidos de 8-11 para 2-7 palavras. Sem isso o pedido de seguir
    nao caberia em take nenhum e cairia em 100% dos videos
  · ancora de SOTAQUE AMERICANO nos dois takes (CL29/CL31, nascidas no V2)
  · 16S6 (2026-08-09): ancora de TRILHA reforcada (o `No music.` de duas
    palavras nao segurava — trilha em 20+ takes de campo) e ancora de RITMO
    (fala curta saia em camera lenta para encher os 8 segundos)

    aponta   ela so' aponta, a bancada nao muda em nenhuma das 2 cenas
    preparo  ela PREPARA na cena 1 e a cena 2 e' o resultado pronto ao lado
             da gelatina (CL17 adaptado: um despejo em cena, nao dois)

Fonte: Valentina Health & Wellness, 2 reels (13,3k e 7,1k comentarios).
Doutrina: AGENTE_ED_CLEAN_V1.md · concorrentes/clean-mapa-visual.md

Uso:
    python funil-organico/clean_v1_16s_short.py --pagina chuck --n 1
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
LEDGER = os.path.join(AQUI, ".clean-v1-16s-ledger.json")

TITULO = "AGENTE CLEAN V1 16SEG"
SLUG = "clean-v1-16s"
SUBTITULO = "a fileira apontada, em 2 cenas · gerador offline de prompts Veo"

# ⭐ QUEM NARRA — contrato lido pela UI (2026-08-06). Herdado do V1: os dois.
SEXOS = ("homem", "mulher")

# ⭐⭐ CL29/CL31 — SOTAQUE AMERICANO, herdado do V2 em 2026-08-08.
# O V1 nao tem estas ancoras porque elas nasceram no V2, depois do relato de
# campo de takes com sotaque errado. O 16seg ja' nasce com as duas: a voz ABRE
# o campo `Audio:` (a ambiencia emoldurava o campo e o gerador tirava o timbre
# dela) e o sotaque tem NOME PROPRIO, nao adjetivo generico.
# ⛔ Ancora POSITIVA: diz-se QUAL sotaque, nunca `no foreign accent`.
SOTAQUE = ("in a flat General American accent, the neutral accent of United "
           "States network television")
VOZ = ("The voice is flat General American, the neutral English of United "
       "States network television")
for _a in (SOTAQUE, VOZ):
    assert "General American" in _a, "ancora sem o nome do sotaque: %r" % _a
    assert not re.search(r"\bno\s+\w+\s+accent", _a, re.I), (
        "ancora NEGATIVA — diz-se qual sotaque e', nunca qual nao e'")

# ⭐⭐ 16S6 (2026-08-09) — DUAS ANCORAS NASCIDAS DE RELATO DE CAMPO. As duas
# tem a MESMA causa raiz do CL31: a regra estava escrita, so' que na posicao
# mais fraca do prompt e na forma que o gerador menos respeita.
#
# (a) TRILHA — `No music.` NAO segurava. O operador contou trilha em mais de
#     20 takes. Duas palavras NEGATIVAS no FIM do campo `Audio:` sao o pior
#     lugar possivel. A receita e' a do CL31, aplicada a outro eixo:
#       POSICAO     a regra deixa de ser rabicho e passa a FECHAR o campo;
#       POSITIVO    declara-se o conjunto COMPLETO do que EXISTE antes de
#                   negar o que nao existe;
#       CONCRETUDE  `raw sound recorded live by the phone microphone` exclui
#                   trilha por CONSTRUCAO — trilha e' pos-producao, e som
#                   cru nao tem pos-producao;
#       SINONIMO    o gerador casa TOKEN. Quem so' le `music` nao cobre
#                   `song`, `soundtrack`, `score`, `melody`, `beat`.
#
# (b) RITMO — take de fala curta saia com o personagem falando em CAMERA
#     LENTA. O gerador le a duracao do clipe como duracao da FALA e estica as
#     silabas ate' encher os 8s. Por isso nao basta pedir velocidade normal:
#     tem de estar escrito que SOBRAR SILENCIO no fim e' o resultado certo.
#     Sem a segunda metade ele continua achando que precisa preencher o tempo.
#     ⛔ A ancora fala da BOCA, nunca do corpo: na familia `preparo` a cena 1
#     tem despejo em andamento, e mandar "ficar parado" contradiria o `mov` —
#     contradicao dentro do prompt e' o que faz o Veo apagar o que estava certo.
SEM_TRILHA = (
    "This is raw sound recorded live by the phone microphone, with nothing "
    "added afterwards: the whole audio track is the speaking voice plus that "
    "room tone and nothing else. There is no music anywhere in this clip: no "
    "song, no soundtrack, no score, no background music, no melody, no "
    "instruments, no beat. Where nobody is speaking there is room tone only, "
    "never music")
# ⚠️ `%(S)s` so' no INICIO de frase e `%(s)s` no meio. A primeira versao usava
# o pronome maiusculo nas tres posicoes e saia *"on purpose: She says it"* —
# defeito que nao quebra nada, aparece no prompt colado no Veo e so' se ve
# lendo o bloco pronto.
RITMO = (
    "%(S)s delivers the line at a normal conversational speed, the ordinary "
    "pace of everyday American speech, and never stretches, drags or slows the "
    "words down. The line is short on purpose: %(s)s says it once at that "
    "normal speed and then stops speaking, mouth closed, still looking into "
    "the lens. The leftover silence at the end of the clip is expected and "
    "correct, and %(s)s never slows the delivery down to fill the time. "
    "Everything in the shot plays at real-time speed.")
for _t in ("no song", "no soundtrack", "no score", "no background music",
           "no melody", "no beat"):
    assert _t in SEM_TRILHA, "ancora de trilha sem o sinonimo %r" % _t
assert "raw sound recorded live" in SEM_TRILHA, (
    "ancora de trilha sem a ancora POSITIVA de som cru")
for _t in ("normal conversational speed", "expected and correct",
           "real-time speed"):
    assert _t in RITMO, "ancora de ritmo sem %r" % _t

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
# ⭐ QUEM NARRA — o sexo de quem fala com a lente (2026-08-06).
# Ordem do operador: *"uma marcacao dentro dos agentes python, de todos, pra
# saber se aquele agente gera roteiros com personagem homens e mulheres como
# narrador/apresentador ou se so' gera com um dos dois"*.
# ⛔ MEDIDO, nao lido: 120 sorteios por agente, olhando o BLOCO 0 do prompt.
# Declarar de cabeca aqui seria a mesma FORMA-sem-FUNCAO que ja' custou o
# botao de pele morto em tres motores.
# ⚠️ Com DOIS sexos a UI desenha a trava homem/mulher; com um so', nao desenha
# botao nenhum — botao que nao trava nada e' pior que botao nenhum.
SEXOS = ("homem", "mulher")

ETNIA = {
    # ⭐ As 5 paginas do lote de 2026-08-05. Split 3 brancos / 2 negros —
    # a razao esta' no `bridge-pages-deploy.md`.
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
# ⭐ TRAVAS — eixos que o operador PRE-SELECIONA e o sorteio nao mexe
# ---------------------------------------------------------------------------
# Contrato lido pela ui_agente: [(chave, rotulo, [opcoes])]. O painel desenha um
# botao por opcao, e sortear() respeita o que estiver travado.
TRAVAS_UI = [
    ("sexo", "quem fala", ["homem", "mulher"]),
    ("familia", "cena", ["aponta", "preparo"]),
]

# ---------------------------------------------------------------------------
# STRINGS TRAVADAS — copia literal da doutrina. NAO REESCREVER.
# ---------------------------------------------------------------------------

# CL1 — ela/ele NUNCA toca em nada. E' o que torna o SHORT viavel: sem
# manipulacao nao ha' risco de continuidade entre blocos de 8s gerados
# separadamente (F12b: o Veo solta o objeto da mao).
NAO_TOCA = ("%s never touches, opens, lifts or pours any of the ingredients on "
            "the counter — %s only points at them and explains.")

# CL9 — a bancada e' identica nas cenas 1 e 2 (familia A)
MESMA_BANCADA = ("in the same order and at the same levels, nothing moved, "
                 "nothing added, nothing removed")

# CL9 familia B — o copo muda, o resto nao. ⛔ Sem `at the same levels`: o nivel
# do copo SOBE a cada despejo, e pedir nivel identico e' ordem contraditoria —
# o Veo resolve desfazendo o preparo.
MESMA_BANCADA_B = ("Nothing has been added to the counter and nothing removed "
                   "from it — only the tall glass has changed.")

# CL14 familia B, cenas 1 e 2 — ela toca UM recipiente e so' ele. Substitui o
# NAO_TOCA nessas duas cenas; na cena 3 o NAO_TOCA volta inteiro.
TOCA_UM = ("%s touches only the container %s is pouring from. %s never touches, "
           "opens or lifts anything else on the counter.")

# CL21 — a gelatina pronta, SO' na cena 3
GELATINA = "a clear glass bowl of firm vivid purple gelatin cubes, glossy and set"

# CL17 — anti-F12b nas cenas 1 e 2 da familia B: punho inteiro + antebraco
# apoiado. ⛔ Nunca `completely motionless` num recipiente que alguem segura:
# e' ordem impossivel e o Veo resolve SOLTANDO o objeto.
# ⚠️ O esqueleto e' o do mel, validado em render 2026-08-02 — so' o recipiente
# e o gesto trocam (tabela DESPEJO). String validada nao se redigita.
PEGADA = ("%s right hand is closed around the %s, the whole hand visibly "
          "wrapped around it, %s forearm resting steady on the wooden counter "
          "as %s %s")

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

CENARIOS = [
    {"id": "diplomas_cidade", "desc": "a bright medical office, four framed diplomas in dark frames on the wall behind %s, a tall window with an out-of-focus city skyline, a large green plant in the corner"},
    {"id": "diplomas_jardim", "desc": "a bright medical office, five framed diplomas in dark frames on the wall behind %s, a window looking out on green trees, a tall potted plant beside it"},
    {"id": "farmacia", "desc": "a bright clinic room, a long shelf of amber medicine bottles on the wall behind %s, a window with soft daylight, white cabinets below the shelf"},
    {"id": "consultorio_claro", "desc": "a bright consulting room, three framed certificates on the pale wall behind %s, a window with sheer curtains, a small green plant on the sill"},
    {"id": "sala_exame", "desc": "a bright examination room, two framed diplomas on the wall behind %s, a folded white examination couch out of focus at the side, a window with daylight"},
    {"id": "escritorio_livros", "desc": "a bright medical office, a low bookshelf of thick medical books behind %s, three framed diplomas above it, a window with an out-of-focus street"},
    # ⭐⭐ + 2026-08-13 — DOZE CENARIOS NOVOS, ordem do operador: *"aumente o
    # pool de opcoes substancialmente, tambem dos ambientes"*. 6 -> 18.
    # ⛔ Mesmas DUAS chaves das seis de cima e mais nada — `id` e `desc` — e o
    # `desc` carrega UM unico `%s`, que e' o pronome objeto da montagem
    # ("behind her" / "behind him"). Dois `%s` numa entrada nova sai TypeError
    # na mao do operador; zero `%s` apaga a pessoa do cenario.
    # ⛔ Mesmo nivel de detalhe das seis antigas: tipo de sala + o que esta' na
    # parede + a janela + UM objeto a mais. Entrada mais pobre que as vizinhas
    # e' cenario que le' como fundo generico ao lado dos outros.
    # ⛔ ZERO texto legivel em qualquer set — a CAUDA promete "No text" nas tres
    # imagens. Por isso os frascos sao `unlabelled` e nao ha' quadro anatomico,
    # placa nem etiqueta: parede com caractere escrito e' texto em cena.
    # ⚠️ NENHUM ID NOVO REPETE MUNDO DO V2 e nenhum `desc` novo sai do registro
    # clinico — a divisao de territorio de 2026-08-05 (*"nao quero que os
    # cenarios/mundo do agente v1 se repitam no agente da v2"*) continua de pe',
    # e o `CENARIOS_V1` congelado la' foi atualizado no MESMO commit. Copia
    # congelada que nao acompanha o original deixa o controle [6] cego.
    {"id": "consultorio_madeira", "desc": "a bright medical office, a wall of warm wood panelling behind %s, two framed diplomas in slim brass frames, a tall window with soft daylight and a low fern on a stand"},
    {"id": "sala_ultrassom", "desc": "a bright clinic room, an ultrasound cart with a dark screen parked at the side behind %s, plain white shelving along the wall, a window with a pale blind half raised"},
    {"id": "consultorio_azul", "desc": "a bright consulting room, a pale blue wall behind %s with four framed certificates in a neat row, a window onto a courtyard and a small watering can on the sill"},
    {"id": "sala_espera", "desc": "a bright waiting room, a row of upholstered chairs and a low table out of focus behind %s, a wide window onto a green hedge and a tall potted palm at the corner"},
    {"id": "laboratorio", "desc": "a bright laboratory room, a rack of clean glass flasks and a centrifuge out of focus behind %s, white cabinets below them and a long window with even daylight"},
    {"id": "consultorio_tijolo", "desc": "a bright medical office, an exposed brick wall behind %s with three framed diplomas, a black-framed window onto an out-of-focus street and a tall dracaena in the corner"},
    {"id": "sala_terapia", "desc": "a bright therapy room, a padded treatment table folded flat against the wall behind %s, a rack of rolled exercise mats at the side and a window with daylight"},
    {"id": "consultorio_verde", "desc": "a bright consulting room, a deep green wall behind %s with two framed certificates, a wide window with sheer curtains and a monstera in a woven basket"},
    {"id": "farmacia_balcao", "desc": "a bright clinic room, a long wall of unlabelled amber bottles and plain white tubs behind %s, a low glass display case at the side and a window with soft daylight"},
    {"id": "sala_reuniao", "desc": "a bright medical office, a plain white wall behind %s with five framed diplomas in dark frames, a long window onto trees and a glass jug of water on a side table"},
    {"id": "consultorio_cinza", "desc": "a bright examination room, a soft grey wall behind %s, a stainless steel trolley with folded white towels at the side and a window with a half-open blind"},
    {"id": "consultorio_terraco", "desc": "a bright medical office, a broad desk with a closed laptop at the side, a pale sage wall behind %s with one large framed diploma and a window looking out on a rooftop garden"},
]

SCRUBS = ["deep burgundy", "deep teal", "navy blue", "forest green",
          "plum purple", "slate grey", "wine red", "petrol blue"]

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
    {"idade": 29,
     "rotulo": "29y · cornrows + sinal na sobrancelha",
     "cabeca": "her hair in neat glossy cornrows pulled back",
     "marca": "a small dark beauty mark above her left eyebrow"},
    {"idade": 32,
     "rotulo": "32y · coque baixo + malar alto",
     "cabeca": "her hair in a sleek shining low bun",
     "marca": "high cheekbones and a small dark beauty mark at the corner of her jaw"},
    {"idade": 27,
     "rotulo": "27y · liso na altura do ombro + sardas",
     "cabeca": "shoulder-length glossy straight hair tucked behind her ears",
     "marca": "a light spray of freckles high on her cheeks"},
    {"idade": 34,
     "rotulo": "34y · cachos curtos + covinha funda",
     "cabeca": "short soft natural curls, glossy and well-defined",
     "marca": "a deep dimple in her left cheek"},
    {"idade": 30,
     "rotulo": "30y · rabo de cavalo alto + olho verde",
     "cabeca": "long silky hair pulled back into a smooth high ponytail",
     "marca": "striking pale green eyes"},
    {"idade": 36,
     "rotulo": "36y · trancas longas + sinal no queixo",
     "cabeca": "long neat braids with a healthy sheen, gathered over one shoulder",
     "marca": "a small dark beauty mark on her chin"},
    {"idade": 28,
     "rotulo": "28y · chanel escuro + boca cheia",
     "cabeca": "a blunt glossy dark bob",
     "marca": "full lips and a small dark beauty mark just below the outer "
              "corner of her left eye"},
    {"idade": 38,
     "rotulo": "38y · ruivo solto + sardas no nariz",
     "cabeca": "thick silky auburn hair, smooth and glossy, falling loose past her shoulders",
     "marca": "a dense spray of freckles across her nose"},
    {"idade": 40,
     "rotulo": "40y · bico de viuva + olhos bicolores",
     "cabeca": "smooth glossy dark hair with a sharp widow's peak, swept back",
     "marca": "eyes of two different colours, one green and one brown"},
    # + 2026-08-04: ampliacao por ordem do operador — *"aumente o pool de
    # personagens... faca isso para pelo menos outros 5 agentes shorts"*.
    # ⛔ Cada entrada difere das outras em >= 3 eixos fisicos (licoes §15):
    # contar entradas nao basta, o que conta e' quantos eixos elas acionam.
    # ⚠️ Ajustadas na resolucao do rebase (2026-08-04): todo cabelo ganhou o
    # token de hidratacao do CL26 (o assert barrou `long jet-black hair` seco),
    # e duas ancoras REPETIDAS foram trocadas — covinha funda na bochecha
    # esquerda (= idade 34) e heterocromia verde/marrom (= idade 40). Ancora
    # repetida remenda o morphing, regra do proprio pool.
    {"idade": 26,
     "rotulo": "26y · tranca preta unica + malar redondo",
     "cabeca": "long silky jet-black hair in a single braid over one shoulder",
     "marca": "high round cheekbones and clear glowing skin"},
    {"idade": 31,
     "rotulo": "31y · chanel platinado + argola no nariz",
     "cabeca": "a sleek bleached-platinum bob cut sharp at the jaw",
     "marca": "a small silver hoop through her left nostril"},
    {"idade": 24,
     "rotulo": "24y · ruivo cobre + olho azul claro",
     "cabeca": "thick glossy copper-red hair falling loose past her shoulders",
     "marca": "a dense spray of freckles over both cheeks and pale blue eyes"},
    {"idade": 33,
     "rotulo": "33y · cachos volumosos + covinha leve",
     "cabeca": "a big loose curl-out worn wide, soft and glossy",
     "marca": "full lips and a faint dimple in her right cheek"},
    {"idade": 28,
     "rotulo": "28y · castanho ruivo + olho ambar",
     "cabeca": "shoulder-length glossy auburn hair tucked behind one ear",
     "marca": "striking light amber eyes"},
    {"idade": 35,
     "rotulo": "35y · box braids ate a cintura + sorriso",
     "cabeca": "waist-length box braids with a healthy sheen, gathered over one shoulder",
     "marca": "smooth luminous skin and a wide bright smile"},
    {"idade": 27,
     "rotulo": "27y · liso longo com risca ao meio",
     "cabeca": "very long silky straight dark hair parted in the middle",
     "marca": "arched brows and a small beauty mark high on her left cheek"},
    {"idade": 30,
     "rotulo": "30y · caramelo ondulado + marca coracao",
     "cabeca": "chin-length smooth wavy caramel hair pushed back off her forehead",
     "marca": "a small heart-shaped birthmark below her right ear"},
]
REFS_H = [
    {"idade": 48,
     "rotulo": "48y · grisalho curto + fenda no queixo",
     "cabeca": "short greying hair and a close-cropped beard", "marca": "a deep cleft in his chin"},
    {"idade": 52,
     "rotulo": "52y · careca + barba grisalha curta",
     "cabeca": "a clean-shaven head and a short grey beard", "marca": "heavy level brows over wide-set eyes"},
    {"idade": 44,
     "rotulo": "44y · escuro penteado + pinta na bochecha",
     "cabeca": "short dark hair combed back, clean-shaven", "marca": "a small mole on his left cheek"},
    {"idade": 55,
     "rotulo": "55y · ralo grisalho + bigode farto",
     "cabeca": "thinning grey hair and a full grey moustache", "marca": "laugh lines at the corners of his eyes"},
    {"idade": 41,
     "rotulo": "41y · rente + cavanhaque + brinco de ouro",
     "cabeca": "short cropped hair and a neat goatee", "marca": "a small gold stud in his left earlobe"},
    {"idade": 50,
     "rotulo": "50y · sal-e-pimenta + barbeado",
     "cabeca": "salt-and-pepper hair cut short, clean-shaven", "marca": "a small notch in his right eyebrow"},
    # + 2026-08-03 — mesmo motivo do REFS_M acima: oculos e pele estavam em 0%.
    # ⛔ Nenhuma repete a ancora facial das seis de cima (cicatriz na
    # sobrancelha, linhas na testa, pinta na bochecha, vincos no olho, cicatriz
    # no queixo, entalhe na sobrancelha): ancora repetida remenda o morphing.
    {"idade": 57,
     "rotulo": "57y · careca + bigode + oculos dourados",
     "cabeca": "a bald crown with grey at the sides and a chevron moustache, thin gold-rimmed glasses",
     "marca": "lightly tanned even skin and a coin-sized birthmark on his left temple"},
    {"idade": 43,
     "rotulo": "43y · bico de viuva + oculos claros",
     "cabeca": "thick dark hair with a sharp widow's peak, clean-shaven, boxy clear-framed glasses",
     "marca": "freckled skin across the bridge of his nose"},
    {"idade": 61,
     "rotulo": "61y · branco farto + barba + bifocais",
     "cabeca": "a full head of white hair and a bristly white beard, heavy black-framed bifocals",
     "marca": "smooth even skin and a wide easy smile"},
    # + 2026-08-04: ampliacao por ordem do operador — *"aumente o pool de
    # personagens... faca isso para pelo menos outros 5 agentes shorts"*.
    # ⛔ Cada entrada difere das outras em >= 3 eixos fisicos (licoes §15):
    # contar entradas nao basta, o que conta e' quantos eixos elas acionam.
    {"idade": 52,
     "rotulo": "52y · careca + barba sal-e-pimenta cheia",
     "cabeca": "a shaved head and a full salt-and-pepper beard",
     "marca": "a broad straight nose with a wide bridge"},
    {"idade": 45,
     "rotulo": "45y · escuro com tempora grisalha + mecha",
     "cabeca": "thick dark hair going grey at the temples, clean-shaven",
     "marca": "a patch of white hair above his left temple"},
    {"idade": 57,
     "rotulo": "57y · rente + bigode fino + oculos de aro",
     "cabeca": "close-cropped iron-grey hair and a neat pencil moustache",
     "marca": "wire-rimmed glasses and high wide cheekbones"},
    {"idade": 41,
     "rotulo": "41y · cachos escuros + barba por fazer",
     "cabeca": "dark curls kept short and dense, a two-day shadow",
     "marca": "a notch cut through his right eyebrow"},
    {"idade": 60,
     "rotulo": "60y · careca + bigode branco grosso",
     "cabeca": "a bald crown with white hair close at the sides",
     "marca": "a thick white moustache and a small dark beauty mark below his right eye"},
    {"idade": 49,
     "rotulo": "49y · ondulado sal-e-pimenta + sardas",
     "cabeca": "wavy salt-and-pepper hair worn long at the collar",
     "marca": "a light spray of freckles across the bridge of his nose"},
    {"idade": 54,
     "rotulo": "54y · escovinha grisalha + olho azul",
     "cabeca": "grey hair in a flat brush cut and a short greying beard",
     "marca": "very pale blue eyes under dark brows"},
    {"idade": 44,
     "rotulo": "44y · coils rente + covinha funda",
     "cabeca": "close-cropped coils with a sharp lined edge, clean-shaven",
     # ⛔ era `a wide gap between his two front teeth` — o assert do CL25
     # barrou no primeiro merge (dente nao e' marca; vira banguelo no Veo)
     "marca": "a single deep dimple in his left cheek"},
]

# ⭐⭐ 2026-08-13 — DOZE MARCAS FACIAIS REESCRITAS, ordem do operador:
# *"melhore a aparencia e shape desses homens"*. Onze no REFS_H e uma no
# REFS_M, e o motivo e' um so': elas descreviam DANO, nao feicao.
#   · cicatriz (4x): `a small scar through his right eyebrow`, `a faint scar on
#     his chin`, `a pale crescent scar on his left cheekbone`, `a pale scar
#     along his right jaw` — e no feminino `a small scar at the corner of her
#     jaw`, que ainda por cima contrariava o proprio bloco acima ("ancora
#     DISTINTIVA e nunca DETERIORADA").
#   · pele castigada (2x): `sun-weathered skin`, `deeply lined skin`.
#   · vinco e ruga (3x): `deep lines across his forehead`, `heavy creases at the
#     corners of his eyes`, `a deep vertical crease between his eyebrows`.
#   · nariz quebrado: `a broad flattened nose that has been broken once`.
#   · palpebra caida: `heavy hooded eyelids`.
#   · e uma PALAVRA DE APROVACAO: `a heavy square jaw`. Elogio no prompt puxa o
#     rosto para a media do banco de imagem — mesmo mecanismo pelo qual dizer
#     "not a celebrity" invoca a celebridade. Descreve-se FEICAO, nunca juizo.
# ⛔ CADA UMA MANTEVE O EIXO QUE CARREGAVA (oculos, pele, porte, careca) e
# trocou so' a ancora, por uma do lado ✅: covinha, fenda no queixo, mecha
# branca na tempora, sarda, malar alto, linhas de riso, argola, beleza-marca,
# sobrancelha cheia e reta.
# ⚠️ As doze estao IDENTICAS nos tres motores da familia CLEAN — o fragmento
# nao pode envelhecer separado.
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
    # ⛔ Cada entrada difere das outras em >= 3 eixos fisicos (licoes §15):
    # contar entradas nao basta, o que conta e' quantos eixos elas acionam.
    # ⚠️ Estas 4 entraram originalmente no CORPOS_M por engano de colagem
    # (sao corpos de homem: "a man who lifts", "wrestler") — movidas para ca'
    # na resolucao do rebase de 2026-08-04, sem perder uma linha.
    "the dense build of a man who lifts, thick through the chest and shoulders, forearms corded, skin taut and even",
    "a lean hard frame with a flat stomach and a visible line down the centre, shoulders square, skin clear",
    "the heavy-boned build of a wrestler, a thick neck and broad flat chest, arms full and solid, skin healthy",
    "a swimmer's build, long muscled arms and a wide back tapering to the waist, shoulders capped and round, skin clear",
    # ⭐⭐ + 2026-08-13 — NOVE CORPOS NOVOS, ordem do operador: *"melhore a
    # aparencia e shape desses homens"* / *"aumente o pool de opcoes
    # substancialmente"*. 9 -> 18.
    # ⛔ IDENTICO NOS TRES MOTORES DA FAMILIA CLEAN (clean_short,
    # clean_v1_16s, clean_v2_16s). Eles nasceram por copia literal; pool que
    # diverge entre irmaos deixa de ter fonte da verdade e envelhece separado.
    # ⛔ O TETO DO CL24 CONTINUA: atleta, NAO fisiculturista. Zero musculo
    # estourado, zero corpo oleado, zero veia de competicao, zero definicao de
    # palco — o registro do CLEAN e' consultorio, e passar disso vira outro
    # angulo. E o CL8 tambem: nunca tronco nu, o corpo aparece PELA roupa.
    # ⚠️ Cada linha e' curta e ancorada em GEOMETRIA (ombro, costas, antebraco,
    # veia) em vez de empilhar adjetivo — densidade de adjetivo de corpo e'
    # superficie de bloqueio conhecida do gerador de imagem (2026-08-03). Se
    # vier recusa, a primeira coisa a encurtar continua sendo esta.
    # ⛔ Zero palavra de aprovacao (`handsome`, `chiseled`, `rugged`): elogio
    # puxa o rosto para a media do banco de imagem. O que entra e' FORMA.
    "the compact powerful build of a gymnast, thick shoulders and a deep chest, forearms tight and veined, skin clear and even",
    "a boxer's frame, wide across the back and narrow at the waist, cords standing out in the forearms, good colour in his face",
    "a heavy rower's build, thick through the upper back and shoulders, veins tracking down each forearm, skin healthy",
    "the solid build of a man who trains every day, round shoulder caps and a thick chest, hands and forearms plainly worked",
    "a tall powerful frame with long thick arms and a broad chest, veins raised along each forearm, clearly in good health",
    "a stocky trained build, a short thick neck and heavy shoulders, forearms full and corded, skin clear",
    "the athletic build of a climber, lean and dense through the shoulders and back, forearms closely veined, healthy colour",
    "a broad athletic frame, thick traps rising to the neck, arms heavy and veined, skin clear and taut",
    "the trained build of a former athlete, still thick through the chest and shoulders, forearms roped, skin even and healthy",
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

# CL14 — os DOIS ingredientes do truque. Piso e teto: sao dois, sempre, em
# todas as tres imagens. Nao precisam ser citados na copy — estao ali para
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
# ⭐⭐ MODOS DE REF — contrato compartilhado (short_comum), 2026-08-05.
# Ordem do operador: toggles de `ref bela` (super model, corpo
# escultural, pouca roupa, olhos fora do comum) e `ref forte` (homem
# musculoso e atraente). ⛔ Desligados, o prompt volta IDENTICO ao de
# antes do recurso — provado caractere por caractere em 200 seeds.
MODO_BELA = True
MODO_FORTE = True

# ⭐⭐ O EIXO TEMPORAL — 2 takes de 8s, 20 palavras cada.
# Ordem do operador: *"a copy precisa ter no máximo 15 segundos, os takes
# possuem 8 segundos mas quero dar uma margem de segurança de 1 segundo na
# narração"*. 20 palavras ≈ 7s de fala; o V1 levava 24 em 8s.
TETO_FALA = {1: 20, 2: 20}

# ⭐ ORDEM DE CORTE quando o teto aperta (ordem dele, 2026-08-08):
# `Comment gelatin` e a referencia ao VIDEO nunca caem; o gate de seguir e' o
# primeiro candidato, e mesmo assim so' depois de esgotar as combinacoes que
# cabem COM ele — *"só faça em último caso"*. O item e' o segundo.
ORDEM_CORTE = ("gate", "item")

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

    # ⭐⭐ 16S3 (2026-08-08) — OS 16 HOOKS DO 16SEG. Aqui esta' a reposicao de
    # entropia que o operador exigiu: com 2 cenas o take 1 e' METADE do video,
    # e com os 14 do V1 ele teria 70 falas contra 1.411 do take 2 — 20x de
    # diferenca justo no beat que segura o espectador. Medido, nao estimado.
    # Os TRES primeiros sao os moldes que ele mesmo escreveu; os treze
    # seguintes foram aprovados um a um, de uma lista de vinte.
    # ⛔ Valor de vilao SEMPRE em centenas (regra dele): `nine hundred`.
    "Four things on this counter put a man's {o} back to work at sixty. Nobody sells you the fourth.",
    "Doctors never mention this counter. Three of these feed a tired {o} — the fourth gets it rock hard.",
    "The pharmacy charges nine hundred dollars to do what this shelf does for a man's {o}. Watch the last one.",
    "Three of these you already know. The fourth is what your {o} was waiting for.",
    "Insurance won't cover what makes your {o} work. This counter costs two dollars.",
    "A man at seventy with a working {o} isn't lucky. He knows these four.",
    "Your wife notices your {o} before you do. These four are why.",
    "The pill wears off in four hours. These four keep your {o} answering.",
    "Nobody prints this list. All four wake your {o}, and the last one does the work.",
    "Your {o} didn't quit on you. Nobody showed you these four.",
    "Men who still use their {o} at sixty-eight keep these four on the counter.",
    "A pharmacist told me these four beat the pills he sells for your {o}.",
    "Waking up hard at sixty isn't genetics. It's these four, and your {o} knows it.",
    "Doctors get paid nine hundred a month to never mention these four to your {o}.",
    "Nine hundred dollar prescriptions, and this counter beats them for your {o}.",
    "Nineteen days on these four and your {o} works like it did at thirty.",
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
# ⭐ 16S1 — o verbo que PROMETE a entrega do video. Sem ele, o CTA so'
# descreve — foi o que reprovou tres candidatos em 2026-08-08.
_ENTREGA = re.compile(r"\bi'?ll send\b|\byou'?ll get\b|\bto get\b|"
                      r"\bcomes\b|\bis yours\b", re.I)

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
# ⭐⭐ 16S1 (2026-08-08) — TODO CTA NOMEIA O FORMATO **VIDEO** E PROMETE A
# ENTREGA. Ordem do operador: *"é importante deixar claro em todos que o truque
# será entregue em formato de vídeo... para preparar a pessoa para assistir a
# VSL"*. Quem comenta esperando texto e recebe VSL abandona nos primeiros
# segundos; nomear o formato entrega a pessoa preparada.
# ⛔ CITAR O VIDEO NAO BASTA — TEM QUE PROMETER QUE ELE CHEGA. Ele reprovou
# `the video shows exactly what to buy` e `the video shows the trick that
# works`: os dois descrevem o video sem dizer que e' enviado. O linter cobra as
# duas metades (ver 16S1 no lint).
CTAS = [
    "Comment gelatin, and I'll send the whole recipe on video.",
    "Comment gelatin, and the complete recipe comes as a video.",
    "Comment gelatin, and I'll send all four on video.",
    "Comment gelatin, and I'll send the real secret on video.",
    "Comment gelatin, and I'll send the measurements on video.",
    # ⚠️ a virgula depois de `gelatin` nao e' estilo: e' o C3a. A keyword
    # precisa de pausa, senao a automacao de DM le' errado o comentario.
    "Comment gelatin, to get the full recipe on video.",
    "Comment gelatin, and I'll send the secret trick on video.",
    "Comment gelatin, and I'll send the complete trick on video.",
    "Comment gelatin, and I'll send the whole trick on video.",
    "Comment gelatin, and I'll send you the secret video.",
    "Comment gelatin, and I'll send the step-by-step video.",
    "Comment gelatin, and I'll send the video with the amounts.",
    "Comment gelatin, and I'll send the video right now.",
    "Comment gelatin, and I'll send the video to your inbox.",
]

# CL12 — o gate EXPLICA a consequencia, nao ameaca. O sujeito da
# impossibilidade e' ela/ele, nunca o espectador.
# ⭐⭐ 16S2 — COMPRIMIDOS DE 8-11 PARA 2-7 PALAVRAS, um para um, cada um
# guardando o SEU motivo (nao vejo sua mensagem / o app bloqueia / so' respondo
# quem segue / so' seguidor recebe). Medido antes de comprimir: com os gates
# longos do V1, virada + CTA + gate estourava o teto em 100% das combinacoes e
# o pedido de seguir sumiria de TODO video. Com estes, ele aparece em ~40%.
GATES = [
    "Follow first.",
    "Follow me first.",
    "Hit follow first.",
    "Follow before you comment.",
    "Make sure you're following.",
    "Only followers get it.",
    "I only message followers.",
    "Follow me and it's yours.",
    "Follow so I can reply.",
    "Follow me, or I can't reply.",
    "Follow me, or it won't reach you.",
    "Follow, or the app blocks my message.",
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

CENAS_UI = ["1 · A FILEIRA", "2 · A VIRADA + CTA"]

EIXOS_UI = [
    ("familia", "CENA", "FAMILIAS", "nome"),
    ("cenario", "CENÁRIO", "CENARIOS", "id"),
    ("ref", "QUEM FALA", "REFS_M", "cabeca"),
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


def sortear(pagina, rng, led, travas=None):
    """Monta a spec. `travas` = {'sexo': 'homem'} fixa o eixo e o sorteio
    respeita — e' o que o painel usa para pre-selecao (TRAVAS_UI)."""
    travas = travas or {}
    usados = led.get(pagina, {})
    et = ETNIA[pagina]

    sexo = travas.get("sexo") or rng.choice(["homem", "mulher"])
    fam_id = travas.get("familia")
    familia = (next(f for f in FAMILIAS if f["id"] == fam_id) if fam_id
               else _fresco(FAMILIAS, usados.get("familia", []), rng, "id"))

    # ⭐ MODO BELA / MODO FORTE — contrato do short_comum, 2026-08-05.
    # ⛔ O SEXO MANDA em qual modo se aplica: `bela` so' vale quando a REF e'
    # mulher, `forte` so' quando e' homem. Aplicar o modo errado devolveria uma
    # mulher com barba cerrada — e o `sexo` ja' esta' sorteado aqui em cima.
    if sexo == "homem":
        ref = (sc.ref_forte(REFS_H[0], rng) if travas.get("forte")
               else rng.choice(REFS_H))
    else:
        ref = (sc.ref_bela(REFS_M[0], rng) if travas.get("bela")
               else rng.choice(REFS_M))
    # CL24/CL26 — o corpo acompanha o sexo: treinado nele, sensual nela
    corpo = rng.choice(CORPOS_H if sexo == "homem" else CORPOS_M)
    cenario = _fresco(CENARIOS, usados.get("cenario", []), rng, "id")
    scrub = rng.choice(SCRUBS)
    # ⛔ 2026-08-10 — SO' OS TRES APELIDOS SAO SORTEAVEIS (ordem do
    # operador, parque inteiro). `soldier` e `tool` seguem no NUCLEO porque
    # as LENTES os usam para DETECTAR o orgao; o que muda e' que nao saem
    # mais na fala. Ver `short_comum.orgaos_sorteaveis`.

    orgaos = sc.orgaos_sorteaveis(rng, 2)
    a = rng.choice(ITEM_A)
    # CL22 — o par nao repete fruta, ingrediente do truque nem beneficio. Todo
    # item A tem no minimo 8 item B livres, entao a lista nunca fica vazia e
    # nao ha' laco de tentativa e erro.
    b = rng.choice([x for x in ITEM_B if not _colide(a, x)])
    # ⚠️ COTA: o HOOK sempre carrega o {o} (11 dos 14 hooks tem). Isso garante
    # o piso de 1/3 e libera as 14 VIRADAS — inclusive as 9 de negacao, que nao
    # nomeiam o orgao e que o operador aprovou uma a uma.
    # ⛔ Exigir {o} tambem na virada dava cota 2/3, mas matava 9 das 14 linhas
    # dele. Copy aprovada nao se descarta para satisfazer contador.
    hook = rng.choice([h for h in HOOKS if "{o}" in h]).format(o=orgaos[0])
    fala2 = _montar_take2(a, orgaos[1], rng)

    # CL14 — DOIS do truque, sempre. Os que a copy ja' cita contam; o resto
    # completa. ⛔ Nunca tres: piso e teto se encontram.
    citados = list(dict.fromkeys(a["itens"] + b["itens"]))
    tru = [i for i in citados if i in IDS_TRUQUE]
    for t in rng.sample(TRUQUE, len(TRUQUE)):
        if len(tru) >= 2:
            break
        if t["id"] not in tru:
            tru.append(t["id"])
    tru = tru[:2]

    # CL20 — a bancada nasce da copy MAIS os dois do truque
    bancada = [i for i in citados if i not in IDS_TRUQUE] + tru

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
    despejo = sorted(tru, key=lambda i: DESPEJO[i]["tom"])

    return {
        "pagina": pagina, "etnia": et, "sexo": sexo, "familia": familia,
        "cenario": cenario, "ref": ref, "scrub": scrub, "corpo": corpo,
        "orgaos": orgaos,
        "item_a": a, "item_b": b, "bancada": bancada, "truque": tru,
        "despejo": despejo,
        # ⛔ 2026-08-03: `b["txt"]` entrava CRU e o `{o}` saia literal na fala —
        # `Pineapple and honey get your {o} up`. O bug so' nasceu agora porque
        # ate' hoje nenhum ITEM_B tinha placeholder (falavam `your milk`, `the
        # whole system`), entao ninguem precisava formatar. Ordem do operador:
        # a cena 2 nomeia o orgao. ⚠️ So' apareceu porque li a fala renderizada
        # — o linter nao reprova `{o}` cru.
        # ⭐ 16S — DUAS falas. A cena 2 do V1 (item A + item B + virada) deixou
        # de ser cena: a virada migrou para o take 2 e o item entra nele quando
        # cabe. Os dois pools continuam sorteados e continuam montando a
        # BANCADA — a fileira em cena nao perdeu um item sequer.
        "falas": [hook, fala2],
    }


def _montar_take2(item, orgao, rng):
    """`[ITEM] {VIRADA} {CTA} [GATE]`, na ordem de corte que ele fixou.

    ⛔ O corte NAO e' arbitrario: tenta-se primeiro a forma CHEIA, e so' quando
    ela nao cabe e' que algo sai — o gate antes do item (ORDEM_CORTE), porque
    foi o que ele mandou (*"priorize o pedido para seguir, mas só faça em
    último caso"*).

    ⚠️ A virada do V1 abre com `But`, que so' faz sentido depois do item.
    Sem item, o `But` cai e a frase e' recapitalizada — senao o take 2 abriria
    com um "Mas" pendurado no nada.
    """
    def cabe(t):
        return _palavras(t) <= TETO_FALA[2]

    def corpo_com(v):
        return "%s, %s" % (item["txt"], v[0].lower() + v[1:])

    def corpo_sem(v):
        s = v[4:] if v.startswith("But ") else v
        return s[0].upper() + s[1:]

    # ⛔ NAO se sorteia virada e CTA e depois se TESTA se o item coube: assim o
    # item entrava em 5% dos videos, porque so' o par mais curto de todos o
    # aceitava. Sorteia-se a FORMA primeiro e depois um par que cabe NELA —
    # medido, o item sobe de 5% para ~50%.
    formas = [corpo_com, corpo_sem]
    rng.shuffle(formas)
    for forma in formas:
        pares = [(v, c) for v in VIRADAS for c in CTAS
                 if cabe("%s %s" % (forma(v.format(o=orgao)), c))]
        if not pares:
            continue
        v, c = rng.choice(pares)
        base = "%s %s" % (forma(v.format(o=orgao)), c)
        gates = [g for g in GATES if cabe("%s %s" % (base, g))]
        return "%s %s" % (base, rng.choice(gates)) if gates else base
    # ⛔ rede: virada sem item + CTA cabe sempre (medido, 196/196 combinacoes)
    return "%s %s" % (corpo_sem(rng.choice(VIRADAS).format(o=orgao)),
                      rng.choice(CTAS))


def _pron(sexo):
    """(sujeito, possessivo, sujeito minusculo, OBJETO).

    ⚠️ O objeto existe porque `his` nao serve de complemento: `in front of his`
    saia em todo video de REF masculina. Em `her` os dois casos coincidem, e por
    isso o bug passou despercebido — so' metade dos sorteios o mostrava."""
    return (("He", "his", "he", "him") if sexo == "homem"
            else ("She", "her", "she", "her"))


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
    """⭐ CL24/CL26: o corpo entra LOGO DEPOIS da idade/etnia e ANTES do traje.

    A ordem importa. O gerador desenha na sequencia em que le', e corpo depois
    da roupa vira roupa larga com corpo generico dentro. Antes dela, a roupa
    assenta sobre o corpo que ja' existe."""
    r, sexo = spec["ref"], spec["sexo"]
    quem = "man" if sexo == "homem" else "woman"
    corpo = spec.get("corpo", "")
    if primeiro:
        return ("a %d-year-old %s %s with %s, wearing a %s V-neck short-sleeved "
                "medical scrub top, %s, %s"
                % (r["idade"], spec["etnia"], quem, corpo, spec["scrub"],
                   r["cabeca"], r["marca"]))
    # nas cenas 2 e 3 o corpo e' RE-ANCORA curta: repetir a descricao inteira
    # gasta prompt e o Veo ja' tem o frame anterior como referencia
    return ("The same %d-year-old %s %s, same build, same %s scrub top, "
            "same %s, same %s"
            % (r["idade"], spec["etnia"], quem, spec["scrub"],
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
    cen = spec["cenario"]["desc"] % obj
    nao_toca = NAO_TOCA % (S, s)
    idade = spec["ref"]["idade"]

    # CL26 — a clausula anti-celebridade acompanha o sexo em TODOS os blocos
    anti = ANTICELEB if spec["sexo"] == "homem" else ANTICELEB_M

    # ⭐⭐ 16S5 — O ITEM QUE A FALA CITA TEM DE ESTAR NA CENA 2 (2026-08-08).
    # Relato dele com o video pronto: *"no final ele fala sobre abacate e
    # gelatina, mas o que aparece na cena e' a canela + gelatina"*. Medido: 54%
    # dos take 2 que citavam ingrediente mostravam OUTRO — todos na familia
    # `preparo`, onde a imagem final desenha o copo pronto, a gelatina e o
    # ingrediente do DESPEJO, que nao tem relacao com o que a fala nomeou.
    # ⚠️ A regra dele tem duas metades, e a segunda importa tanto quanto:
    # *"caso o CTA cite somente a gelatina, ai nao tem problema gerar qualquer
    # ingrediente"*. Por isso `citado` e' None quando a fala nao nomeia item —
    # e nesse caso a cena segue como estava.
    citado = (spec["item_a"]["itens"][0]
              if spec["item_a"]["txt"] in spec["falas"][1] else None)

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
        "Wearing a %s V-neck short-sleeved medical scrub top. %s. %s. %s "
        "Hands out of frame, no objects. Plain neutral gray background, "
        "soft even frontal light. Slight sensor grain, soft focus, raw iPhone "
        "front camera aesthetic. No subtitles, no captions, no burned-in text, "
        "no watermark."
        % (idade, spec["etnia"], "man" if spec["sexo"] == "homem" else "woman",
           _corpo_ref(spec),
           spec["scrub"], spec["ref"]["cabeca"][0].upper() + spec["ref"]["cabeca"][1:],
           spec["ref"]["marca"][0].upper() + spec["ref"]["marca"][1:],
           REF_ROSTO_H if spec["sexo"] == "homem" else REF_ROSTO_M))

    if fam == "aponta":
        fila = _fila(spec["bancada"])
        # ⭐ CL27 (2026-08-04) — a CENA 1 e' rente a camera: bancada na borda de
        # baixo do quadro e itens GRANDES em primeiro plano. O "Medium shot"
        # solto saia longe demais e os ingredientes viravam miniatura — o
        # operador anexou o enquadramento certo (homem apontando, caixas
        # legiveis perto da lente). E' a MESMA geometria que o IMAGE 03 ja'
        # usava e que valida bem: waist up + bottom edge of the frame.
        b["IMAGE 01/03"] = (
            "Close medium shot inside %s. Seated behind a wooden counter is %s, "
            "framed from the waist up, the counter running along the bottom "
            "edge of the frame, close to the camera. On the counter in front "
            "of %s, large and clearly readable in the foreground near the "
            "lens, stand in a row: %s. %s looks "
            "directly into the lens with %s mouth open mid-word as %s speaks, the front "
            "teeth even and complete, %s "
            "torso upright and %s head raised. %s right index finger is extended "
            "toward the row, %s hand just above the counter. %s touches nothing. "
            "%s is the only person in the frame. %s Soft daylight from the window. %s"
            % (cen, _pessoa(spec), obj, fila, S, Ss, s, Ss, Ss, _cap(Ss), Ss, S, S,
               anti, CAUDA))
        b["IMAGE 02/03"] = (
            "Medium shot in the same room, same background. %s. On the counter is "
            "the same row %s: %s. %s looks directly into the lens with %s mouth "
            "open mid-word as %s speaks, the front teeth even and complete, %s "
            "expression serious and certain. %s "
            "right index finger is extended toward %s, %s hand just above the "
            "counter. %s touches nothing. %s is the only person in the frame. %s %s"
            % (_pessoa(spec, False), MESMA_BANCADA, fila, S, Ss, s, Ss, _cap(Ss),
               VISUAL[spec["truque"][0]], Ss, S, S, anti, CAUDA))
        b["IMAGE 03/03"] = (
            "Closer medium shot in the same room, same background, same soft "
            "daylight. %s, framed from the waist up. On the counter along the "
            "bottom edge of the frame stand three things only: %s; %s; and %s. %s "
            "looks directly into the lens, calm and confident, one corner of %s "
            "mouth raised in a half-smile, %s mouth open mid-word as %s speaks, the "
            "front teeth even and complete. %s "
            "right index finger points directly at the camera. %s is the only "
            "person in the frame. %s %s"
            # ⭐ 16S5 — o primeiro objeto e' o ingrediente CITADO na fala
            % (_pessoa(spec, False), VISUAL[citado or spec["bancada"][0]],
               GELATINA, VISUAL[spec["truque"][0]], S, Ss, Ss, s, _cap(Ss), S,
               anti, CAUDA))
        mov = [
            "%s right hand moves once along the row, the extended index finger "
            "travelling from one end to the other, staying just above the counter "
            "the whole time. Everything on the counter stays exactly as it appears "
            "in the first frame — same position, same angle, same levels — "
            "completely motionless for the entire shot." % _cap(Ss),
            "%s extended index finger moves from one item to another and back, "
            "staying just above the counter. Everything on the counter stays "
            "exactly as it appears in the first frame — completely motionless for "
            "the entire shot." % _cap(Ss),
            # ⛔⛔ 16S4 — ESTA FRASE ERA GENERICA E MENTIA. No V1 ela e' a cena
            # 3 e diz `The glass, the bowl of gelatin cubes and the box beside
            # them`, mas a familia `aponta` nao tem copo nem caixa: a IMAGE
            # mostra o item da bancada, a gelatina e o item do truque. Achado
            # LENDO o lote, nao pelo linter — no V1 passava por ser 1 de 3
            # cenas; aqui e' METADE do video.
            # ⚠️ Agora a frase e' DERIVADA dos mesmos tres objetos que a IMAGE
            # 02/02 desenha, entao ela nao pode divergir.
            "The three things on the counter, the bowl of gelatin cubes among "
            "them, stay exactly as they appear in the first frame — nothing "
            "moves, nothing is touched.",
        ]
    else:
        # CL17 — o ingrediente 1 e' despejado na cena 1, o 2 na cena 2. O que
        # esta' na mao sai da fileira da bancada NAQUELA cena e volta na
        # seguinte; assim os DOIS aparecem nas tres imagens e o piso do CL14
        # continua de pe'.
        i1, i2 = spec["despejo"]
        d1, d2 = DESPEJO[i1], DESPEJO[i2]
        v = {"ref1": _pessoa(spec), "ref": _pessoa(spec, False), "cen": cen,
             "S": S, "Ss": Ss, "s": s, "gel": GELATINA, "anti": anti,
             "cauda": CAUDA, "resto": MESMA_BANCADA_B, "obj": obj,
             "fila1": _fila([i for i in spec["bancada"] if i != i1]),
             "fila2": _fila([i for i in spec["bancada"] if i != i2]),
             "cor1": d1["cor"], "cor2": d2["cor"],
             # ⭐ 16S5 — o terceiro objeto da cena 2 e' o ingrediente CITADO
             # na fala. Sem `citado`, volta a ser o do despejo, como antes.
             "c1": d1["curto"], "c2": d2["curto"],
             "ing2": VISUAL[citado or i2],
             "Sc": Ss[0].upper() + Ss[1:],   # "Her"/"His" em inicio de frase
             "peg1": _cap(PEGADA % (Ss, d1["cont"], Ss, s, d1["gesto"])),
             "peg2": _cap(PEGADA % (Ss, d2["cont"], Ss, s, d2["gesto"])),
             "cai1": _cap(d1["queda"]), "cai2": _cap(d2["queda"]),
             "seg1": d1["segue"], "seg2": d2["segue"]}
        # ⚠️ Formatacao NOMEADA neste ramo, nao posicional: sao 14+ campos por
        # bloco e um deslocamento de indice troca pronome por cor sem estourar
        # erro nenhum — bug que so' aparece no video pronto.
        # ⭐ CL27 (2026-08-04) — cena 1 rente a camera, mesma moldura da
        # familia A: bancada na borda de baixo, itens grandes perto da lente.
        b["IMAGE 01/03"] = (
            "Close medium shot inside %(cen)s. Seated behind a wooden counter is "
            "%(ref1)s, framed from the waist up, the counter running along the "
            "bottom edge of the frame, close to the camera. On the counter in "
            "front of %(obj)s, large and clearly visible in the foreground "
            "near the lens, stand "
            "a tall clear glass filled with plain clear water and, beside it, "
            "%(fila1)s. %(peg1)s. %(cai1)s, and the water in the glass is "
            "turning from clear to %(cor1)s where the stream lands. %(S)s looks "
            "directly into the lens with %(Ss)s mouth open mid-word as %(s)s "
            "speaks, the front teeth even and complete, %(Ss)s torso upright and "
            "%(Ss)s head raised. %(S)s is the "
            "only person in the frame. %(anti)s Soft daylight from the window. "
            "%(cauda)s" % v)
        # ⚠️ A cena 2 CLAREIA se a segunda cor for mais clara que a primeira —
        # despejar mel em agua marrom nao produz dourado. Por isso o liquido
        # `clouds over` em vez de trocar de tom: vale para os 20 pares, e
        # nenhum deles le como o preparo desandando.
        b["IMAGE 02/03"] = (
            "Medium shot in the same room, same background. %(ref)s. On the "
            "counter, in the same order and at the same positions as before, "
            "stand %(fila2)s. %(resto)s %(peg2)s. %(cai2)s, and the %(cor1)s "
            "water in the glass is clouding over and turning %(cor2)s where the "
            "stream lands. %(S)s looks directly into the lens with %(Ss)s mouth "
            "open mid-word as %(s)s speaks, the front teeth even and complete, "
            "%(Ss)s expression serious and "
            "certain. %(S)s is the only person in the frame. %(anti)s "
            "%(cauda)s" % v)
        # CL21 — a cena 3 e' o RESULTADO: copo pronto + gelatina, e so' um dos
        # dois do truque ao lado (a prioridade do CL21 manda cortar o resto
        # antes da gelatina). Zero manipulacao.
        b["IMAGE 03/03"] = (
            "Closer medium shot in the same room, same background, same soft "
            "daylight. %(ref)s, framed from the waist up. On the counter along "
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
            "counter, and %(seg1)s. As it falls, the water in the glass turns "
            "from clear to %(cor1)s, the colour spreading down through it. "
            "Everything else stays exactly as it appears in the first frame." % v,
            "%(S)s keeps %(Ss)s right hand closed around the %(c2)s, the whole "
            "hand visibly wrapped around it, %(Ss)s forearm resting steady on the "
            "counter, and %(seg2)s. As it falls, the %(cor1)s water in the glass "
            "clouds over and turns %(cor2)s, the colour spreading down through "
            "it. Everything else stays exactly as it appears in the first "
            "frame." % v,
            # ⛔ 16S5 — NAO se nomeia mais o vasilhame aqui. Ele era `%(c2)s`
            # (o pote do despejo), e desde que a cena 2 passou a mostrar o
            # ingrediente CITADO na fala, o pote pode nao estar mais em quadro:
            # o TAKE citava `the jar` e a IMAGE nao tinha jar nenhum em 54 dos
            # 400 sorteios. Contradicao entre TAKE e IMAGE e' pior que omissao.
            "The finished %(cor2)s drink, the bowl of gelatin cubes and the "
            "third item beside them stay exactly as they appear in the first "
            "frame — nothing moves, nothing is touched." % v,
        ]

    # ⭐⭐ 16S — DE TRES BLOCOS PARA DOIS. A cena do MEIO cai; ficam a fileira
    # (cena 1) e o resultado com a gelatina (a antiga cena 3). Os tres IMAGE
    # continuam sendo MONTADOS acima, com o mesmo codigo validado do V1, e a
    # selecao acontece aqui — reescrever a construcao para duas cenas seria
    # reescrever sete pontos de montagem e perder as regras que cada um carrega.
    # ⚠️ Na familia `preparo` isso quer dizer UM despejo em cena, nao dois: a
    # cena 1 despeja o ingrediente mais claro e a cena 2 mostra o copo pronto.
    # O segundo do truque continua na bancada e continua no CL14.
    b["IMAGE 01/02"] = b.pop("IMAGE 01/03")
    b["IMAGE 02/02"] = b.pop("IMAGE 03/03")
    del b["IMAGE 02/03"]
    mov = [mov[0], mov[2]]

    if fam == "preparo":
        amb = ["quiet office room tone, %s"
               % DESPEJO[spec["despejo"][0]]["som"],
               "quiet office room tone"]
    else:
        amb = ["quiet office room tone"] * 2
    # ⭐ CL31 — a VOZ ABRE o campo `Audio:` e a ambiencia vem atras. Era a
    # ambiencia que abria, e o gerador tirava o timbre do lugar.
    # ⭐⭐ 16S6 — e o campo FECHA com a ancora de trilha, que antes era um
    # `No music.` de duas palavras e nao segurava em campo.
    audio = ["%s. %s. %s." % (VOZ, a[0].upper() + a[1:], SEM_TRILHA)
             for a in amb]
    # CL14 — na cena 1 da familia B a frase travada vira TOCA_UM; na cena 2
    # (e na familia A inteira) o NAO_TOCA volta.
    toca_um = TOCA_UM % (S, s, S)
    # ⭐⭐ 16S6 — o RITMO entra COLADO na ancora de sotaque, antes do movimento:
    # as duas descrevem a MESMA coisa (como a fala sai da boca) e separa-las
    # pelo bloco de movimento e' o que deixava a segunda solta no fim do
    # paragrafo, de onde o gerador ja' descartou o `No music.`
    ritmo = RITMO % {"S": S, "s": s}
    for i in range(2):
        toca = " " + (toca_um if (fam == "preparo" and i == 0) else nao_toca)
        b["TAKE %02d/02" % (i + 1)] = (
            "Animate the provided image exactly. Handheld iPhone shot, very "
            "slight natural sway, no cuts. The %d-year-old %s speaks straight "
            "into the lens %s. %s %s%s %s is the only person in the shot.\n"
            'Dialogue: "%s"\nAudio: %s'
            % (idade, "man" if spec["sexo"] == "homem" else "woman",
               SOTAQUE, ritmo, mov[i], toca, S, sonorizar(spec["falas"][i]),
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

    # ⭐⭐ 16S1 — o CTA nomeia o VIDEO **e** promete a entrega. Citar o
    # video sem prometer o envio foi reprovado pelo operador em
    # 2026-08-08: `the video shows...` descreve, nao entrega.
    if "video" not in falas[1].lower():
        ach.append(("ERRO", "16S1: o CTA nao nomeia o formato VIDEO — o "
                            "espectador precisa saber que vai assistir"))
    if not _ENTREGA.search(falas[1]):
        ach.append(("ERRO", "16S1: o CTA cita o video mas nao promete a "
                            "entrega (send / get / comes)"))

    # ⚠️ COTA 1/3 NESTE AGENTE, nao 2/3 (ordem do operador, 2026-08-02).
    # Os dois reels de origem quase nao nomeiam o orgao — o v1 diz `wiener` uma
    # vez, o v2 nenhuma. E as 9 viradas de negacao aprovadas nao o nomeiam.
    # Exigir 2/3 obrigaria a descartar copy que o operador validou linha a
    # linha, entao o piso desce e o hook garante ele sozinho.
    cota = sum(1 for f in falas if any(o.lower() in f.lower() for o in NUCLEO))
    if cota < 1:
        ach.append(("ERRO", "cota do orgao 0/2 — o hook tem de nomear o orgao"))
    if len(set(spec["orgaos"])) < 2:
        ach.append(("ERRO", "o mesmo orgao repetido no mesmo video"))
    if not any(o.lower() in falas[0].lower() for o in NUCLEO):
        ach.append(("ERRO", "o hook nao nomeia o orgao"))

    # CL11 — entrega imediata
    for t in ("tonight", "by morning", "later today", "this evening"):
        if t in falas[1].lower():
            ach.append(("ERRO", "CL11: CTA promete hora ('%s') — a entrega e' "
                                "imediata" % t))
    if "gelatin," not in falas[1] and "gelatin." not in falas[1]:
        ach.append(("ERRO", "C3a: keyword sem pausa depois"))
    if "GELATIN" in falas[1]:
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
        for nome in ("IMAGE 01/02",):
            img = blocos.get(nome, "")
            for ing in spec["truque"]:
                if VISUAL[ing] not in img and DESPEJO[ing]["cont"] not in img:
                    ach.append(("ERRO", "CL14: '%s' fora de %s — os dois do "
                                        "truque estao nas tres imagens"
                                        % (ing, nome)))
        t3 = blocos.get("TAKE 02/02", "").lower()
        if any(w in t3 for w in ("keeps falling", "keeps running", "pouring from")):
            ach.append(("ERRO", "CL17: manipulacao na cena 2 — ela so' apresenta "
                                "o resultado pronto"))
        # CL28 — a dose e' medida e o jato TERMINA (takes de campo 2026-08-04:
        # pote emborcado, copo cheio). Despejo continuo de 8s = "esvazie o
        # frasco" para o Veo.
        for nome in ("TAKE 01/02",):
            t = blocos.get(nome, "").lower()
            if "keeps falling" in t or "keeps running" in t:
                ach.append(("ERRO", "CL28: despejo continuo em %s — o jato tem "
                                    "de parar dentro do take" % nome))
            if not any(d in t for d in ("spoonful", "pinch", "a few drops")):
                ach.append(("ERRO", "CL28: %s sem dose nomeada (colherada, "
                                    "pitada, gotas)" % nome))

    # CL21 — a gelatina SO' na cena 3
    for nome in ("IMAGE 01/02",):
        if "gelatin cubes" in blocos.get(nome, ""):
            ach.append(("ERRO", "CL21: gelatina fora da cena 3 (%s)" % nome))
    if "gelatin cubes" not in blocos.get("IMAGE 02/02", ""):
        ach.append(("ERRO", "CL21: a cena 2 tem de mostrar a gelatina em cubos"))

    # CL1/CL2 — nada de manipular, nada de prop falico
    for nome, txt in blocos.items():
        if not nome.startswith(("IMAGE", "TAKE")):
            continue
        direcao = txt.split("\nDialogue:")[0]
        # ⛔ tirar a PROPRIA proibicao antes de varrer: NAO_TOCA contem a
        # palavra "pours", e o linter se auto-reprovava em 100% dos sorteios.
        # Regra que reprova tudo nunca foi testada.
        for pr in (("He", "he"), ("She", "she")):
            direcao = direcao.replace(NAO_TOCA % pr, "")
        for pr in (("He", "he", "He"), ("She", "she", "She")):
            direcao = direcao.replace(TOCA_UM % pr, "")
        direcao = direcao.lower()
        # ⚠️ Na familia B o despejo e' autorizado nas cenas 1 E 2 (CL17). A
        # cena 3 NAO e' isenta: la' vale o CL1 inteiro, maos fora.
        # ⛔ O `continue` antigo pulava tambem o CL2 na cena isenta — prop
        # falico nunca deixa de ser proibido.
        isenta = (spec["familia"]["id"] == "preparo"
                  and nome.endswith("01/02"))
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
    if "foreground" not in blocos.get("IMAGE 01/02", ""):
        ach.append(("ERRO", "CL27: IMAGE 01 sem os itens em primeiro plano "
                            "(foreground) — a cena sai longe demais"))

    # ⭐⭐ 16S6 — as duas ancoras novas nos DOIS takes, e a de trilha no lugar
    # certo. ⚠️ O `Audio:` e' cobrado por POSICAO, nao so' por presenca: o que
    # falhou em campo nao foi a ausencia da regra, foi ela estar no fim como
    # rabicho de duas palavras. Lente que so' procura a string aprovaria de
    # novo exatamente o prompt que gerou os 20 takes com trilha.
    for nome in ("TAKE 01/02", "TAKE 02/02"):
        t = blocos.get(nome, "")
        direcao, _, aud = t.partition("\nAudio: ")
        if "normal conversational speed" not in direcao:
            ach.append(("ERRO", "16S6: %s sem a ancora de RITMO — fala curta "
                                "sai esticada para encher os 8s" % nome))
        if "expected and correct" not in direcao:
            ach.append(("ERRO", "16S6: %s manda falar normal mas nao AUTORIZA "
                                "o silencio no fim — sem isso o gerador "
                                "continua enchendo o tempo" % nome))
        if not aud.startswith(VOZ):
            ach.append(("ERRO", "CL31: %s — o campo Audio nao ABRE com a voz"
                                % nome))
        # ⛔ LITERAIS, nunca `endswith(SEM_TRILHA)`. A primeira versao cobrava a
        # saida CONTRA A PROPRIA CONSTANTE: enfraquecer SEM_TRILHA mudava os
        # dois lados da comparacao e a lente aprovava calada. O controle
        # negativo pegou — voltei a ancora para `No music` e nao saiu um erro.
        # Guarda que se move junto com o que guarda nao guarda nada.
        if "raw sound recorded live" not in aud:
            ach.append(("ERRO", "16S6: %s sem a ancora POSITIVA de som cru — "
                                "so' negar `music` nao segurou em campo"
                                % nome))
        for _s in ("no song", "no soundtrack", "no score",
                   "no background music", "no melody", "no beat"):
            if _s not in aud:
                ach.append(("ERRO", "16S6: %s sem o sinonimo '%s' — o gerador "
                                    "casa TOKEN, nao sentido" % (nome, _s)))
        if not aud.rstrip().endswith("never music."):
            ach.append(("ERRO", "16S6: %s — o campo Audio nao FECHA na ancora "
                                "de trilha; foi de rabicho no fim que o "
                                "`No music.` velho nao segurou" % nome))
    # ⛔⛔ TAKE CONTRA IMAGE — 2026-08-05. Este motor tem `lint()` proprio e NAO
    # passa pelo `lint_curto`, entao a lente compartilhada nao chegava aqui.
    # ⚠️ Foi assim que a primeira varredura deu "limpo" para sete motores: eles
    # nunca rodaram a lente. "Limpo" sem cobertura e' o pior resultado possivel,
    # porque parece verde. Medir a lente e' medir TAMBEM se ela e' chamada.
    # ⛔ HIERARQUIA DO MECANISMO — diretriz do operador, 2026-08-06 (§31).
    # So dispara quando a cena 2 mostra preparo em quadro.
    sc.lint_hierarquia_mecanismo(spec, blocos, ach)

    sc.lint_take_vs_image(blocos, ach)

    return ach


def resumo_pt(spec):
    fam = ("ela aponta, nada se mexe" if spec["familia"]["id"] == "aponta"
           else "ela despeja %s na cena 1 e a cena 2 e' so' o copo pronto"
                % spec["despejo"][0])
    if spec["sexo"] == "homem":
        fam = fam.replace("ela ", "ele ")
    return ("%s de %d anos, de scrub %s, num %s. Na bancada: %s. %s. Duas "
            "cenas de 8s, gelatina em cubos na última."
            % ("Homem" if spec["sexo"] == "homem" else "Mulher",
               spec["ref"]["idade"], spec["scrub"],
               spec["cenario"]["id"].replace("_", " "),
               ", ".join(spec["bancada"]), fam.capitalize()))


def nova_fala(spec, i, rng):
    """Re-sorteia a copy de UMA cena, ja' formatada com os slots deste video.

    ⚠️ A cena 2 e' COMPOSTA (item + virada + CTA + gate) e cada peca depende do
    espaco que as outras deixam — re-sortear so' um pedaco estouraria o teto
    sem ninguem ver. Por isso ela e' remontada inteira pelo mesmo
    `_montar_take2` do sorteio, com o item que JA' esta' na bancada (CL20)."""
    o = spec["orgaos"]
    if i == 0:
        return rng.choice([h for h in HOOKS if "{o}" in h]).format(o=o[0])
    return _montar_take2(spec["item_a"], o[1], rng)


EIXOS_QUE_MEXEM_NA_COPY = {}

# ⚠️ `despejo` nao tem pool fixo (o par sai do CL14/CL20 e varia por video),
# entao o teto e' arbitrario: 8 pares antes de zerar. Sem teto proprio a lista
# so' cresceria e o anti-repeticao pararia de rejeitar qualquer coisa.
TETO_LEDGER = {"familia": len(FAMILIAS), "cenario": len(CENARIOS), "despejo": 8}



# ---------------------------------------------------------------------------
# ⭐⭐ AUTOTESTE — o aceite deste motor deixa de ser RELATO e vira MEDICAO
# ---------------------------------------------------------------------------
# ⚠️ ESTE MOTOR NASCEU SEM `--autoteste` e ficou assim ate' 2026-08-13, quando os
# CENARIOS foram de 6 para 18 e os CORPOS_H de 9 para 18 por ordem do operador
# (*"melhore a aparencia e shape desses homens"* / *"aumente o pool de opcoes
# substancialmente, tambem dos ambientes"*). Pool grande sem sonda e' pior que
# pool pequeno: o vicio volta calado.
# ⛔ `0 ERRO` num lote grande e' SUSPEITA, nao aprovacao: pode ser motor limpo ou
# regra morta. Por isso cada trava tem um sabotador, e o sabotador tem de CHEGAR
# onde a regra olha (licoes §16) — e' por isso que `_medir_pools` recebe as
# listas por ARGUMENTO em vez de ler o global.
_DETERIORACAO = (
    "scar", "broken nose", "chipped tooth", "missing tooth", "gap between",
    "sun damage", "sun-weathered", "weathered", "ruddy", "thin skin",
    "loose skin", "age spot", "sunken", "gaunt", "bony", "hollow", "leathery",
    "deeply lined", "deep lines", "crease between", "hooded eyelid",
)
# ⛔ Palavra de aprovacao SO' E' PROIBIDA NO POOL MASCULINO. No feminino ela e'
# obrigatoria por contrato — o CL26 tem assert de carga exigindo `beautiful` em
# toda linha do CORPOS_M, porque ali a beleza mora na FRASE e nao no cast. Uma
# sonda que ignorasse essa assimetria reprovaria justamente a regra que o
# operador mandou escrever.
_APROVACAO_H = ("handsome", "chiseled", "rugged", "strong jaw", "square jaw",
                "piercing eyes", "good-looking", "not a celebrity",
                "not famous", "not a model")


def _medir_pools(cenarios, refs_m, refs_h, corpos_h, corpos_m):
    """As travas de POOL deste motor, medidas — nunca declaradas.

    ⛔ As cinco listas entram por ARGUMENTO de proposito: e' o que deixa o
    sabotador plantar uma entrada suja sem encostar no motor de verdade. Trava
    que so' sabe olhar o global nao pode ser testada, e trava nao testada e'
    decoracao.
    """
    achados = []
    for nome, pool, piso in (("CENARIOS", cenarios, 18), ("REFS_M", refs_m, 17),
                             ("REFS_H", refs_h, 17), ("CORPOS_H", corpos_h, 18),
                             ("CORPOS_M", corpos_m, 5)):
        if len(pool) < piso:
            achados.append("pool %s com %d entradas (piso %d)"
                           % (nome, len(pool), piso))
        txt = [str(x) for x in pool]
        for x in sorted({t for t in txt if txt.count(t) > 1}):
            achados.append("pool %s tem entrada REPETIDA: %s" % (nome, x[:70]))

    # ⛔ DETERIORACAO em qualquer pool de gente. E' a regra mais cara do repo:
    # o operador reprovou um lote inteiro no PLACA 16 com *"esses caras tao
    # parecendo mendigo"*, e este motor carregava onze marcas de dano ate'
    # 2026-08-13 (cicatriz, pele castigada, vinco, nariz quebrado, palpebra).
    for nome, pool in (("REFS_M", refs_m), ("REFS_H", refs_h),
                       ("CORPOS_H", corpos_h), ("CORPOS_M", corpos_m)):
        for x in pool:
            baixo = str(x).lower()
            for t in _DETERIORACAO:
                if t in baixo:
                    achados.append("pool %s: ancora DETERIORADA %r em %s"
                                   % (nome, t, str(x)[:60]))
    for nome, pool in (("REFS_H", refs_h), ("CORPOS_H", corpos_h)):
        for x in pool:
            baixo = str(x).lower()
            for t in _APROVACAO_H:
                if t in baixo:
                    achados.append("pool %s: palavra de aprovacao/negacao %r em "
                                   "%s" % (nome, t, str(x)[:60]))

    # ⛔ CENARIOS: UM unico `%s` por entrada, que e' o pronome objeto da
    # montagem. Dois viram TypeError na mao do operador; zero apaga a pessoa.
    ids = [c["id"] for c in cenarios]
    for c in cenarios:
        if c["desc"].count("%s") != 1:
            achados.append("CENARIO %s com %d `%%s` (tem de ser exatamente 1)"
                           % (c["id"], c["desc"].count("%s")))
        if ids.count(c["id"]) > 1:
            achados.append("CENARIO com id repetido: %s" % c["id"])
    return achados


def autoteste(n=600):
    """Os pools e as invariantes deste motor, medidos num lote de verdade."""
    falhas = list(_medir_pools(CENARIOS, REFS_M, REFS_H, CORPOS_H, CORPOS_M))
    vistos = collections.defaultdict(set)
    sexos = collections.Counter()

    for seed in range(n):
        spec = sortear("joe", random.Random(seed), {}, {})
        blocos = montar(spec)
        for tipo, msg in lint(spec, blocos):
            if tipo == "ERRO":
                falhas.append("seed %d (%s): %s"
                              % (seed, spec["cenario"]["id"], msg))
        vistos["cenario"].add(spec["cenario"]["id"])
        vistos["corpo"].add(spec["corpo"])
        vistos["ref"].add(spec["ref"]["marca"])
        sexos[spec["sexo"]] += 1

    if len(vistos["cenario"]) != len(CENARIOS):
        falhas.append("cenario: %d de %d nunca sorteados em %d videos"
                      % (len(CENARIOS) - len(vistos["cenario"]),
                         len(CENARIOS), n))
    # ⚠️ CORPO e REF sao sorteados DEPOIS do sexo, entao a cobertura tem de
    # somar os dois lados — cobrar so' um deles esconde metade do pool.
    if len(vistos["corpo"]) != len(CORPOS_H) + len(CORPOS_M):
        falhas.append("corpo: %d de %d nunca sorteados em %d videos"
                      % (len(CORPOS_H) + len(CORPOS_M) - len(vistos["corpo"]),
                         len(CORPOS_H) + len(CORPOS_M), n))
    if len(vistos["ref"]) != len(REFS_M) + len(REFS_H):
        falhas.append("ref: %d de %d nunca sorteados em %d videos"
                      % (len(REFS_M) + len(REFS_H) - len(vistos["ref"]),
                         len(REFS_M) + len(REFS_H), n))
    for s, q in sexos.items():
        if not 0.35 <= q / float(n) <= 0.65:
            falhas.append("sexo %s em %.1f%% do lote (faixa 35-65%%)"
                          % (s, 100.0 * q / n))

    # ---- CONTROLES POSITIVOS: cada trava SABE reprovar? --------------------
    ctrl = []
    _sujo = dict(REFS_H[0])
    _sujo["marca"] = "a pale crescent scar on his left cheekbone"
    if not any("DETERIORADA" in m for m in
               _medir_pools(CENARIOS, REFS_M, REFS_H + [_sujo], CORPOS_H, CORPOS_M)):
        ctrl.append("a sonda de aparencia NAO acusa `scar` plantado no REFS_H")
    _pele = dict(REFS_M[0])
    _pele["marca"] = "sun-weathered skin and full lips"
    if not any("DETERIORADA" in m for m in
               _medir_pools(CENARIOS, REFS_M + [_pele], REFS_H, CORPOS_H, CORPOS_M)):
        ctrl.append("a sonda de aparencia NAO alcanca o pool FEMININO")
    _elogio = dict(REFS_H[0])
    _elogio["marca"] = "a heavy square jaw and dark brows"
    if not any("aprovacao" in m for m in
               _medir_pools(CENARIOS, REFS_M, REFS_H + [_elogio], CORPOS_H, CORPOS_M)):
        ctrl.append("a sonda NAO acusa palavra de aprovacao no pool masculino")
    # ⛔ E o contrario, que e' metade do par: a sonda de aprovacao NAO pode
    # encostar no CORPOS_M, onde `beautiful` e' exigido pelo assert do CL26.
    if any("CORPOS_M" in m and "aprovacao" in m for m in
           _medir_pools(CENARIOS, REFS_M, REFS_H, CORPOS_H, CORPOS_M)):
        ctrl.append("a sonda de aprovacao esta' reprovando o CORPOS_M, onde a "
                    "beleza facial e' CONTRATO (CL26)")
    _cen = {"id": "sabotador", "desc": "a bright room behind %s with %s"}
    if not any("`%s`" in m for m in
               _medir_pools(CENARIOS + [_cen], REFS_M, REFS_H, CORPOS_H, CORPOS_M)):
        ctrl.append("a sonda NAO acusa cenario com dois `%s`")
    if not any("REPETIDA" in m for m in
               _medir_pools(CENARIOS, REFS_M, REFS_H, CORPOS_H + [CORPOS_H[0]],
                            CORPOS_M)):
        ctrl.append("a sonda NAO acusa entrada REPETIDA no pool")
    # ⚠️ O controle NEGATIVO, que fecha o par: o pool limpo nao pode ser
    # acusado. Regra que reprova tudo nunca foi testada.
    if _medir_pools(CENARIOS, REFS_M, REFS_H, CORPOS_H, CORPOS_M):
        ctrl.append("o pool limpo esta' sendo reprovado pela propria sonda")

    # ⛔⛔ O CONTRATO DO `rotulo` — o texto que o menu suspenso do painel
    # desenha (2026-08-13, ordem do operador: *"implemente esse mecanismo e
    # menu drop down para todos os demais agentes 16"*).
    # ⚠️ AQUI OS DOIS POOLS DIVIDEM UM MENU SO'. O eixo `ref` sai de REFS_H ou
    # de REFS_M conforme o SEXO sorteado, entao o operador ve' as 34 pessoas na
    # mesma lista — e a unicidade tem de valer no CONJUNTO, nao pool a pool.
    # Duas mulheres com rotulos iguais seria colisao dentro do mesmo pool; uma
    # mulher e um homem com o mesmo rotulo e' colisao entre pools, e o
    # `ui_agente._barra_dropdowns` monta o mapa com `if txt not in mapa` — o
    # SEGUNDO some do menu em silencio, sem erro e sem log.
    # ⚠️ O TETO DE 42 e' a largura do combobox (`width=38` + folga): rotulo
    # maior sai cortado, e rotulo cortado volta a ser ilegivel — que e'
    # exatamente o problema que ele veio resolver.
    _refs = REFS_M + REFS_H
    _rot = [x.get("rotulo") or "" for x in _refs]
    _sem = [x["cabeca"][:32] for x in _refs if not x.get("rotulo")]
    if _sem:
        falhas.append("ROTULO: %d REF(s) sem rotulo — o dropdown cai no `id` e "
                      "o operador le' %r" % (len(_sem), _sem[0]))
    _rep = sorted({r for r in _rot if _rot.count(r) > 1})
    if _rep:
        falhas.append("ROTULO: %d rotulo(s) repetido(s) (%r) — a segunda REF "
                      "some do dropdown sem erro nenhum" % (len(_rep), _rep[0]))
    _longos = [r for r in _rot if len(r) > 42]
    if _longos:
        falhas.append("ROTULO: %d rotulo(s) acima de 42 chars (%r, %d) — "
                      "estoura a largura do menu"
                      % (len(_longos), _longos[0], len(_longos[0])))
    # ⛔ E o rotulo e' PORTUGUES: se vazar para um bloco, o Veo desenha o texto.
    # A lente e' de AUSENCIA e varre o pool inteiro — um sorteio so' mediria a
    # sorte da seed.
    _junto = " ".join(" ".join(montar(sortear("joe", random.Random(700 + k),
                                              {}, {})).values())
                      for k in range(12))
    _vaza = [r for r in _rot if r and r in _junto]
    if _vaza:
        falhas.append("ROTULO: o texto de painel %r vazou para um bloco do "
                      "prompt — ele e' portugues e o Veo desenha texto"
                      % _vaza[0])

    # ⛔⛔ E A TRAVA QUE GUARDA O BURACO. `DROPDOWNS_UI` NAO E' DECLARADO neste
    # motor, e o motivo esta' medido: o `ui_agente` monta o mapa do menu com
    # `mapa[texto] = e.get("id")`, e NENHUMA entrada de REFS_M/REFS_H tem `id`
    # — elas sao {idade, cabeca, marca}. Declarar hoje renderiza um menu de 17
    # opcoes em que TODO valor vira `None`, o `travas()` descarta, e a REF
    # continua sorteando: menu que promete e nao entrega, que e' pior do que
    # menu ausente. (Medido em 2026-08-13: 8 sorteios com a opcao escolhida
    # devolveram 6 rostos diferentes.)
    # ⚠️ Entao esta lente fica ARMADA e DORMENTE: no dia em que alguem declarar
    # o `DROPDOWNS_UI`, ela cobra as duas coisas que faltam — `id` em toda
    # entrada e um `sortear` que FIXA por esse id. Sem ela, o buraco reabre
    # calado e so' aparece no lote.
    for _ch, _lbl, _pool_nome, _campo in list(globals().get("DROPDOWNS_UI") or []):
        _p = globals().get(_pool_nome)
        if not isinstance(_p, list) or not _p:
            falhas.append("DROPDOWNS_UI: o pool %r nao existe no motor — o "
                          "menu nasce vazio" % _pool_nome)
            continue
        _faltam = [x for x in _p if not str(x.get(_campo) or "")]
        if _faltam:
            falhas.append("DROPDOWNS_UI: %d entrada(s) de %s sem o campo %r"
                          % (len(_faltam), _pool_nome, _campo))
        _sem_id = [x for x in _p if not x.get("id")]
        if _sem_id:
            falhas.append("DROPDOWNS_UI: %d entrada(s) de %s sem `id` — o "
                          "ui_agente mapeia o menu para None e o eixo continua "
                          "sorteando" % (len(_sem_id), _pool_nome))
            continue
        _alvo = _p[0]["id"]
        _v = {sortear("joe", random.Random(800 + k), {},
                      {_ch: _alvo})[_ch].get("id") for k in range(8)}
        if _v != {_alvo}:
            falhas.append("DROPDOWNS_UI: travar %r em %r devolveu %r — o menu "
                          "promete e o sorteio ignora" % (_ch, _alvo, sorted(_v)))

    # ⭐⭐ CONTROLES NEGATIVOS DAS TRAVAS DE ROTULO. Lente que nunca acusou e'
    # lente que ninguem sabe se funciona. ⚠️ Sabotagem em COPIA: mexer no pool
    # global deixaria o motor sujo se o autoteste morresse no meio.
    def _falhas_rot(pool):
        r = [x.get("rotulo") or "" for x in pool]
        return ([x for x in pool if not x.get("rotulo")]
                or [t for t in r if r.count(t) > 1]
                or [t for t in r if len(t) > 42])

    for _nome, _sujo in (
            ("rotulo vazio", [dict(_refs[0], rotulo="")] + _refs[1:]),
            ("rotulo repetido entre os pools",
             [dict(_refs[0], rotulo=REFS_H[0]["rotulo"])] + _refs[1:]),
            ("rotulo de 43 chars", [dict(_refs[0], rotulo="x" * 43)] + _refs[1:])):
        if not _falhas_rot(_sujo):
            ctrl.append("a trava de rotulo NAO acusou o pool sabotado (%s)"
                        % _nome)
    if _falhas_rot(_refs):
        ctrl.append("a trava de rotulo esta' acusando o pool de verdade")

    print("CENARIOS %d | REFS_M %d | REFS_H %d | CORPOS_H %d | CORPOS_M %d | "
          "%d videos" % (len(CENARIOS), len(REFS_M), len(REFS_H),
                         len(CORPOS_H), len(CORPOS_M), n))
    print("vistos: cenarios %d/%d | corpos %d/%d | refs %d/%d"
          % (len(vistos["cenario"]), len(CENARIOS),
             len(vistos["corpo"]), len(CORPOS_H) + len(CORPOS_M),
             len(vistos["ref"]), len(REFS_M) + len(REFS_H)))
    print("sexo: homem %.1f%% | mulher %.1f%%"
          % (100.0 * sexos["homem"] / n, 100.0 * sexos["mulher"] / n))

    if ctrl:
        # ⛔ ASCII de proposito: o console do Windows e' cp1252 e o `⛔` levanta
        # UnicodeEncodeError — justamente na hora em que o relatorio importa.
        print("\n>> O AUTOTESTE ESTA' CEGO:")
        for c in ctrl:
            print("   %s" % c)
    if falhas:
        print("\n>> %d FALHA(S):" % len(falhas))
        for f in falhas[:20]:
            print("   %s" % f)
    if not falhas and not ctrl:
        print("\nAUTOTESTE OK - e os controles reprovam quando devem.")
    return 1 if (falhas or ctrl) else 0

def main():
    ap = argparse.ArgumentParser(description="Randomizador do agente CLEAN")
    ap.add_argument("--autoteste", action="store_true",
                    help="mede os pools e as invariantes do motor (com controles)")
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
        print("SPEC — pagina %s | %s | familia %s | bancada: %s"
              % (a.pagina, spec["sexo"], spec["familia"]["id"],
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
                              ("cenario", spec["cenario"]["id"]),
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
