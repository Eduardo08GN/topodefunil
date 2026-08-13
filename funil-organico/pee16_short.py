#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE PEE SHORT — 3 cenas de 8 segundos.

⭐ MOTOR AUTOSSUFICIENTE desde 2026-08-03. Ate' esta data este arquivo fazia
`import pee_lucas as base` e lia de la' as strings travadas, os pools e as
tabelas do linter. Os `*_lucas` sao de terceiro e saem do repo de trabalho,
entao tudo o que era herdado foi copiado para ca', caractere por caractere.
**Este arquivo passa a ser a FONTE DA VERDADE do angulo PEE.**

O colapso das 5 cenas do arco longo em 3:

    arco longo 1 · A MANCHA + O VINCULO  ->  SHORT 1 · A MANCHA
    arco longo 4 · REDENCAO              ->  SHORT 2 · O TRUQUE + A VIRADA (funde 2, 3 e 4)
    arco longo 5 · CTA                   ->  SHORT 3 · CTA

⛔ O QUE O COLAPSO AMEACAVA
Duas coisas, e as duas sao espinha do angulo:
  · o literal `gelatin trick`, que morava nos RITUAIS (cena 3);
  · o **mecanismo da prostata** (PE7), que morava nos MECANISMOS (cena 2). No
    PEE o mecanismo nao e' `blood flow` generico: e' a prostata inchada
    apertando o cano, e e' isso que amarra a mancha ao orgao. Sem ele o hook
    faz uma afirmacao que o video nunca sustenta.
Os dois entram na copy fundida, e o linter trava nos dois.
"""

import argparse
import collections
import os
import random
import re
import sys
from types import SimpleNamespace

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import short_comum as sc                                        # noqa: E402

from nucleo_sonoro import sonorizar                             # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
# ⛔ Ledger proprio: 16s e 24s nao gastam o historico um do outro.
LEDGER = os.path.join(AQUI, ".pee-16-ledger.json")

TITULO = "AGENTE PEE 16"
SUBTITULO = ("2 takes de 8s = 16 segundos · a mancha pública, e a bancada "
             "com o rosto no mesmo quadro")
SLUG = "pee-16"


# ===========================================================================
# ⭐ DOUTRINA DO ANGULO — INLINEADA EM 2026-08-03
# ===========================================================================
# Daqui ate' a marca "FIM DA DOUTRINA INLINEADA" esta' tudo o que este motor
# lia do `pee_lucas.py`. Os `*_lucas` sao de terceiro e saem do repo de
# trabalho: cada nome herdado foi COPIADO LITERALMENTE, com o comentario que
# explica por que ele existe. Nada foi reescrito, renomeado, comprimido nem
# reordenado — sao strings validadas em campo, e mexer nelas muda o video que
# sai do gerador.
#
# ⚠️ As tres funcoes e o teto do ARCO LONGO de 5 cenas ganharam sufixo para nao
# colidir com o contrato de 3 cenas deste modulo:
#     sortear    -> _sortear_longo
#     montar     -> _montar_longo
#     nova_fala  -> _nova_fala_longa
#     TETO_FALA  -> TETO_FALA_LONGO   (⛔ NAO e' o TETO_FALA deste arquivo, que
#                                      tem 3 cenas; sao dois dicionarios)
# O `short_comum` recebe as tres pelo objeto `_LONGO`, montado no fim do bloco.

# ---------------------------------------------------------------------------
# STRINGS TRAVADAS — copia literal da doutrina. NAO REESCREVER, NAO COMPRIMIR.
# ---------------------------------------------------------------------------

# PE2 — o choro nao e' opcional: e' o que transforma a mancha de piada em ruina
CHORO_IMAGE = (
    "head bowed, chin toward his chest, looking down at himself, crying hard — "
    "tears running down both cheeks, eyes red and squeezed shut, mouth twisted "
    "down, shoulders shaking. Both hands fidgeting with the hem of his t-shirt."
)
CHORO_TAKE = (
    "he keeps crying, his shoulders shaking once with a sob, tears still on his "
    "cheeks, and he does not look up. He never speaks and never looks at the camera."
)

# PE3 — o dedo aponta a MANCHA NA ROUPA, nunca a virilha. Roupa e' ancora segura,
# e ninguem encosta nele — e' a construcao que o F12b do FLAGRANTE tomou como
# precedente depois das 4 recusas por agencia.
NARRADOR_IMAGE = (
    "crouched on one knee beside him, right arm extended, index finger pointing "
    "directly at the stain on the fabric, not touching him, face turned toward "
    "the camera, mouth open mid-word"
)
NARRADOR_TAKE = (
    "The crouching man speaks calmly to camera, his pointing finger stays on the "
    "stain on the fabric and never touches the other man. Neither man changes position."
)

# PE4 — plateia ri E aponta (ordem do operador). Sem isso vira acidente triste.
#
# ⛔⛔ O SUBSTANTIVO VIROU PARAMETRO EM 2026-08-10, E ISSO E' CONSERTO DE
# CONTRADICAO, NAO REESCRITA DA STRING.
# A string dizia `four blurred SHOPPERS` cravado, em todo sorteio — enquanto o
# TAKE 01, dez linhas abaixo, ja' dizia `the blurred %s keep laughing` com o
# `loc["plateia"]` do local sorteado. Ou seja: o mesmo prompt descrevia
# `shoppers` na IMAGE e `customers` / `bowlers` / `players` no TAKE, para a
# MESMA gente no MESMO quadro.
# ⚠️ Ja' estava errado antes desta ampliacao (feira, loja de racao e loja de
# pesca nao tem "shoppers" no TAKE), mas passava despercebido porque os seis
# primeiros locais eram todos varejo. Com boliche, aeroporto, arquibancada e
# salao de bingo no pool, a IMAGE passaria a pedir COMPRADORES DE SUPERMERCADO
# num portao de embarque.
# ⛔ E contradicao DENTRO do prompt e' a familia de defeito mais cara deste
# repo: o gerador nao escolhe um dos dois, ele inventa um terceiro. E' o mesmo
# mecanismo das DUAS COLHERES que o operador pegou no render em 2026-08-10.
# ⭐ A ordem do operador (plateia RI e APONTA, quatro figurantes desfocados)
# esta' intacta caractere por caractere — o que mudou foi de onde vem o
# substantivo, e ele passou a vir de onde ja' vinha no TAKE.
PLATEIA_IMAGE = (
    "four blurred %s standing behind them, hands over their mouths "
    "mid-laugh, two of them pointing at him, clearly mocking him"
)

# D1 — o modelo anatomico da cena 2 (mesma string do FLAGRANTE F16)
D1_IMAGE = (
    "In his left hand he holds up toward the camera a hand-sized medical "
    "teaching model of the male pelvis in median sagittal section — a "
    "flat-backed slab of molded plastic, painted in pink, salmon and pale "
    "blue, the interior structures exposed in lengthwise profile the way a "
    "urology office display shows them, the whole model turned so its cut "
    "face is squared to the lens. His right index finger points at the model."
)
D1_TAKE = (
    "He holds the plastic anatomy model steady in his left hand and taps its "
    "cut face twice with his right index finger as he explains. The model "
    "stays squared to the camera and does not turn or tilt."
)

IMOBILIDADE = ("same position, same angle, same shape — completely motionless "
               "for the entire shot.")
NEGACAO_AVE = (" No bird, no goose, no duck, no swan, no snake, no feathers, "
               "no beak, no eyes, no head, nothing alive.")
CAUDA = "iPhone shot, natural grain, no text, no watermark."

# ⛔⛔ LAPIDE — `ANTICELEB` MORREU EM 2026-08-10, E O REPO PRECISA SABER DISSO.
# ---------------------------------------------------------------------------
# A constante era `"Ordinary relatable face, not a celebrity."` e entrava em
# DOIS lugares: no BLOCO 0 (REF) e na IMAGE da mancha.
#
# ⛔ ORDEM DO OPERADOR, com o lote na mao: *"nao falar de celebridade nem usar a
# palavra famoso, celebridade no prompt, muito menos dizer burramente no prompt
# 'not morgan freeman', 'not celebrity', 'not famous people'"*.
#
# ⭐ E ELE ESTA' CERTO PELA DOUTRINA QUE O PROPRIO REPO JA' TINHA ESCRITO
# (licoes-producao-veo §"E' pior que inutil: e' municao", 2026-07-31):
#     *"a declaracao nao e' neutra. Ela coloca o token no campo: escrever
#      `not a celebrity` injeta `celebrity`. O classificador casa TOKEN, nao
#      intencao — e' a mesma mecanica da grafia homofona, virada contra nos."*
# A regra existia ha' dez dias e nunca tinha sido aplicada a este arquivo. O
# resultado foi um pool que dizia `not a celebrity` em todo sorteio E entregava
# a celebridade mesmo assim — o pior dos dois mundos, porque a clausula dava a
# impressao de que o problema estava tratado.
#
# ⛔ NAO SE SUBSTITUI POR OUTRA NEGACAO. `not a model`, `not an actor`, `not
# resembling any famous person` sao a MESMA municao com outra roupa. Contra o
# classificador e contra o atrator, o silencio vence a negacao.
# ⭐ QUEM FAZ O TRABALHO AGORA E' A GEOMETRIA DO POOL `REFS` — cada entrada
# descreve formato de rosto, testa, nariz, maxilar e malar. Rosto especifico
# nao tem para onde derivar; rosto generico deriva para a media do treino, e a
# media tem nome.
# ⚠️ ESTA LAPIDE FICA. Regra que some sem explicacao volta no proximo agente
# nascido por copia — e foi exatamente assim que a clausula chegou aqui.
# ⚠️ E o `short_comum` AINDA tem `ANTICELEB_BELA` e `ANTICELEB_FORTE` com a
# mesma negacao dentro, usados por outros motores. Este arquivo NAO os le'
# (o MODO FORTE daqui montava a clausula local), mas a divida esta' registrada.

# ⭐ QUEM NARRA — o sexo de quem fala com a lente (2026-08-06).
# Ordem do operador: *"uma marcacao dentro dos agentes python, de todos, pra
# saber se aquele agente gera roteiros com personagem homens e mulheres como
# narrador/apresentador ou se so' gera com um dos dois"*.
# ⛔ MEDIDO, nao lido: 120 sorteios por agente, olhando o BLOCO 0 do prompt.
# Declarar de cabeca aqui seria a mesma FORMA-sem-FUNCAO que ja' custou o
# botao de pele morto em tres motores.
# ⚠️ Com DOIS sexos a UI desenha a trava homem/mulher; com um so', nao desenha
# botao nenhum — botao que nao trava nada e' pior que botao nenhum.
SEXOS = ("homem",)

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
# POOLS SORTEAVEIS
# ---------------------------------------------------------------------------

# PE5 — sempre lugar publico movimentado, zero marca legivel (P12).
# ⚠️ Nao existe versao privada da mancha: sem plateia nao ha' flagrante.
# ⛔⛔ RISADA NAO ENTRA NO AUDIO — 2026-08-10. O operador pegou isto no
# FLAGRANTE 16 com o render na mao (*"o homem que deveria estar extremamente
# triste da' risada junto com todo mundo"*), e aqui o caso e' PIOR: a vitima
# deste angulo esta' CHORANDO na IMAGE, e o campo `Audio:` cueava `laughter`.
# O Veo sincroniza ROSTO com AUDIO — som de riso faz toda cara em quadro rir,
# inclusive a que o texto manda estar em lagrimas.
# ⭐ Nao faz falta: a plateia continua rindo NA IMAGEM. Sai a pista sonora que
# arrastava o rosto errado junto.
# ⚠️ Estendi do FLAGRANTE para ca' por ser o mesmo defeito na mesma cena — o
# operador reportou um so'.
LOCAIS = [
    {"id": "mercado", "selo": "V",
     "cenario": "a busy big-box supermarket aisle",
     "detalhe": "full shelves on both sides, a shopping cart beside him, "
                "an out-of-focus aisle sign with no readable text",
     "plateia": "shoppers", "plateia_evento": "that store",
     "eco": "the same aisle",
     "luz": "Hard fluorescent overhead light.",
     "audio": "store ambience, a cart rolling."},
    {"id": "farmacia", "selo": "N",
     "cenario": "a pharmacy aisle",
     "detalhe": "shelves of unlabeled boxes, a counter out of focus behind them",
     "plateia": "customers", "plateia_evento": "that pharmacy",
     "eco": "the same pharmacy counter",
     "luz": "Flat white pharmacy light.",
     "audio": "quiet store ambience, a scanner beeping."},
    {"id": "fila_caixa", "selo": "V",
     "cenario": "a supermarket checkout line",
     "detalhe": "a conveyor belt with groceries, a register out of focus, "
                "no readable brand names",
     "plateia": "people in line", "plateia_evento": "that checkout line",
     "eco": "the same checkout line",
     "luz": "Hard fluorescent overhead light.",
     "audio": "checkout beeps, bags rustling."},
    {"id": "ferragens", "selo": "N",
     "cenario": "a hardware store aisle",
     "detalhe": "racks of tools and paint cans, a flatbed cart beside him, "
                "no readable brand names",
     "plateia": "customers", "plateia_evento": "that hardware store",
     "eco": "the same tool aisle",
     "luz": "Cool warehouse overhead light.",
     "audio": "warehouse ambience, a cart squeaking."},
    {"id": "hortifruti", "selo": "N",
     "cenario": "the produce section of a supermarket",
     "detalhe": "crates of fruit and vegetables, a misting sprayer above them",
     "plateia": "shoppers", "plateia_evento": "that produce aisle",
     "eco": "the same produce aisle",
     "luz": "Bright white produce light.",
     "audio": "store ambience, the mist sprayer hissing."},
    {"id": "conveniencia", "selo": "N",
     "cenario": "a gas station convenience store",
     "detalhe": "a coffee counter and snack racks, a glass door out of focus, "
                "no readable brand names",
     "plateia": "customers", "plateia_evento": "that gas station",
     "eco": "the same store counter",
     "luz": "Harsh white overhead light.",
     "audio": "store ambience, a door chime."},
    # + 2026-08-01: o operador mediu vicio — os mesmos cenarios voltando no
    # lote. Pool ampliado com tres lugares publicos fora do varejo de rua.
    {"id": "feira", "selo": "N",
     "cenario": "a crowded farmers market walkway",
     "detalhe": "folding tables of produce under canvas canopies, a stack of "
                "crates beside him, no readable signs",
     "plateia": "shoppers", "plateia_evento": "that farmers market",
     "eco": "the same market row",
     "luz": "Open midday sunlight.",
     "audio": "market chatter, a vendor calling out."},
    {"id": "racao", "selo": "N",
     "cenario": "a farm and feed store aisle",
     "detalhe": "stacked sacks of feed on wooden pallets, a hand truck beside "
                "him, no readable labels",
     "plateia": "customers", "plateia_evento": "that feed store",
     "eco": "the same feed aisle",
     "luz": "Dusty daylight from high windows.",
     "audio": "warehouse ambience, a pallet jack rattling."},
    {"id": "pesca", "selo": "N",
     "cenario": "a crowded bait and tackle shop",
     "detalhe": "walls of fishing rods and bins of tackle, a live bait tank "
                "bubbling beside them, no readable labels",
     "plateia": "customers", "plateia_evento": "that tackle shop",
     "eco": "the same tackle shop",
     "luz": "Warm overhead shop light.",
     "audio": "shop ambience, the bait tank bubbling."},
    # ======================================================================
    # + 2026-08-10: SEGUNDA AMPLIACAO, e desta vez o operador mediu com o LOTE
    # RENDERIZADO na mao — quatro roteiros seguidos e o corredor de varejo em
    # todos os quatro. *"esta repetindo com muita frequencia os mesmos
    # personagems / Variar tb o ambiente do take 1"*.
    #
    # ⛔ O DIAGNOSTICO NAO E' O TAMANHO DO POOL, sao DUAS COISAS somadas:
    #   1. as nove entradas acima eram SEIS VEZES A MESMA COISA — corredor de
    #      loja com prateleiras dos dois lados. Mercado, farmacia, ferragens,
    #      hortifruti, conveniencia e racao mudam o ROTULO e nao mudam o QUADRO:
    #      mesma profundidade, mesma altura de camera, mesma luz de teto, mesma
    #      plateia de "customers". Nove entradas, tres imagens.
    #   2. o `_evitando` guardava so' os 3 ultimos — com 9 entradas isso e' 1
    #      em 6 de repetir na quarta vez. Subiu para 6 no `_sortear_longo`.
    #
    # ⭐ AS DOZE NOVAS MUDAM A GEOMETRIA DO QUADRO, nao a placa da porta:
    # arquibancada ao ar livre, salao de mesas compridas, fila com corda,
    # sala de espera com cadeiras de plastico, piso de showroom. E cada uma
    # traz uma PLATEIA que a cena 1 exige (PE5: sem plateia nao ha' flagrante)
    # e um som proprio — o audio e' o que separa boliche de banco no escuro.
    # ⛔ Todas continuam publicas, movimentadas e SEM MARCA LEGIVEL (P12).
    # ⚠️ `plateia_evento` entra na FALA pelo `{evento}` e passa pelo `_aqui`,
    # entao TEM de comecar com `that ` e ler bem depois de `in ` / `out of `.
    # O autoteste cobra as duas coisas.
    # ⚠️ `plateia` entra em `the blurred %s keep laughing` — e' substantivo
    # plural NU, sem artigo. `the regulars` ali sairia como "the blurred the
    # regulars", e foi por isso que o campo virou controle no autoteste.
    # ======================================================================
    {"id": "boliche", "selo": "N",
     "cenario": "a busy bowling alley concourse",
     "detalhe": "racks of house balls and lit lanes stretching away behind "
                "them, a scoring monitor out of focus, no readable text",
     "plateia": "bowlers", "plateia_evento": "that bowling alley",
     "eco": "the same bowling alley",
     "luz": "Low overhead light with bright lane glare behind them.",
     "audio": "pins crashing, a ball rolling down the lane."},
    {"id": "lavanderia", "selo": "N",
     "cenario": "a crowded laundromat",
     "detalhe": "a wall of front-load washers and a long folding table, a "
                "rolling laundry cart beside him, no readable labels",
     "plateia": "customers", "plateia_evento": "that laundromat",
     "eco": "the same laundromat",
     "luz": "Flat white fluorescent light.",
     "audio": "machines tumbling, a dryer buzzer."},
    {"id": "legiao", "selo": "N",
     "cenario": "the main room of a veterans hall",
     "detalhe": "long folding tables and stacked chairs, a wood-paneled wall "
                "and a dartboard behind them, no readable signs",
     "plateia": "regulars", "plateia_evento": "that veterans hall",
     "eco": "the same veterans hall",
     "luz": "Warm dim light from hanging fixtures.",
     "audio": "room chatter, a chair scraping the floor."},
    {"id": "bingo", "selo": "N",
     "cenario": "a packed bingo hall",
     "detalhe": "long tables covered in paper cards and daubers, a number "
                "board out of focus, no readable text",
     "plateia": "players", "plateia_evento": "that bingo hall",
     "eco": "the same bingo hall",
     "luz": "Flat overhead hall light.",
     "audio": "hall chatter, a caller's microphone."},
    {"id": "lanchonete", "selo": "N",
     "cenario": "the aisle of a busy diner",
     "detalhe": "vinyl booths down both sides, a counter with stools out of "
                "focus, no readable menus",
     "plateia": "diners", "plateia_evento": "that diner",
     "eco": "the same diner",
     "luz": "Warm light from window blinds and overhead globes.",
     "audio": "diner chatter, plates clattering."},
    {"id": "borracharia", "selo": "N",
     "cenario": "the waiting room of a tire shop",
     "detalhe": "rows of plastic chairs and a stack of tires through the "
                "glass, a coffee machine beside him, no readable labels",
     "plateia": "customers", "plateia_evento": "that tire shop",
     "eco": "the same waiting room",
     "luz": "Hard fluorescent light through a glass partition.",
     "audio": "an impact wrench in the bay, a phone ringing."},
    {"id": "concessionaria", "selo": "N",
     "cenario": "a car dealership showroom floor",
     "detalhe": "a polished sedan on the tile behind them, glass walls and "
                "desks out of focus, no readable badges",
     "plateia": "shoppers", "plateia_evento": "that showroom",
     "eco": "the same showroom floor",
     "luz": "Bright even showroom light.",
     "audio": "showroom chatter, a phone ringing at a desk."},
    {"id": "correio", "selo": "N",
     "cenario": "a post office lobby line",
     "detalhe": "a rope line and a service counter out of focus, a wall of "
                "small brass boxes beside them, no readable signs",
     "plateia": "people in line", "plateia_evento": "that post office",
     "eco": "the same post office line",
     "luz": "Flat white overhead light.",
     "audio": "lobby murmur, a stamp thudding on the counter."},
    {"id": "banco", "selo": "N",
     "cenario": "a bank lobby line",
     "detalhe": "a velvet rope and teller windows out of focus, a polished "
                "stone floor under them, no readable signs",
     "plateia": "people in line", "plateia_evento": "that bank lobby",
     "eco": "the same bank lobby",
     "luz": "Cool even lobby light.",
     "audio": "quiet lobby murmur, a printer running."},
    {"id": "viveiro", "selo": "N",
     "cenario": "the aisle of a garden center",
     "detalhe": "benches of potted plants under a translucent roof, bags of "
                "soil stacked beside him, no readable labels",
     "plateia": "shoppers", "plateia_evento": "that garden center",
     "eco": "the same garden aisle",
     "luz": "Diffused daylight through a translucent roof.",
     "audio": "a sprinkler ticking, quiet chatter."},
    # ⛔⛔ `little league` SAIU ANTES DE CHEGAR AO GERADOR — 2026-08-10.
    # A primeira versao desta entrada dizia `at a little league ballpark` com
    # plateia `parents`. Isso poe CRIANCAS implicitas no mesmo quadro em que um
    # homem esta' com uma mancha de urina na virilha e um dedo apontando para
    # ela. A politica de menores e' a que mais recusou neste repo (quatro
    # recusas seguidas no FLAGRANTE), e ha' um hook no pool que diz `in front
    # of his grandson` — os dois juntos dobrariam a aposta.
    # ⭐ Softball adulto entrega a MESMA geometria (arquibancada de metal ao ar
    # livre, plateia colada, luz de fim de tarde) sem a adjacencia. Nao se
    # trocou a cena: trocou-se a liga.
    {"id": "arquibancada", "selo": "N",
     "cenario": "the front row of metal bleachers at an adult softball field",
     "detalhe": "a chain-link backstop and a dirt infield behind them, a "
                "cooler at his feet, no readable banners",
     "plateia": "spectators", "plateia_evento": "that ballpark",
     "eco": "the same bleachers",
     "luz": "Late afternoon sun from frame-right.",
     "audio": "a bat crack, scattered clapping."},
    {"id": "aeroporto", "selo": "N",
     "cenario": "a crowded airport gate area",
     "detalhe": "rows of seats and a jet bridge window behind them, a roller "
                "bag beside him, no readable signs",
     "plateia": "travelers", "plateia_evento": "that airport",
     "eco": "the same gate area",
     "luz": "Flat terminal overhead light.",
     "audio": "terminal murmur, a boarding chime."},
    # ======================================================================
    # + 2026-08-13: TERCEIRA AMPLIACAO, 21 -> 27. Ordem do operador:
    # *"aumente o pool de opcoes substancialmente, tambem dos ambientes"*.
    # ⭐ MESMO CRITERIO DA SEGUNDA (2026-08-10), que e' o unico que funcionou:
    # o que separa uma entrada da outra e' a GEOMETRIA DO QUADRO, nao a placa
    # da porta. Entram um salao de espelhos (barbearia), um piso de peso livre
    # (academia), uma arquibancada de madeira em anel voltada para baixo
    # (leilao de gado), uma plataforma coberta com linha amarela no chao
    # (estacao), um salao de mesas redondas com pista no meio (casamento) e um
    # salao de mesas compridas de potluck (centro comunitario).
    # ⛔ Todas continuam PUBLICAS e MOVIMENTADAS (PE5: sem plateia nao ha'
    # flagrante) e SEM MARCA LEGIVEL (P12).
    # ⛔ RISADA CONTINUA FORA DO `audio` — a vitima esta' chorando na IMAGE e o
    # Veo sincroniza rosto com som (correcao de 2026-08-10). A plateia ri NA
    # IMAGEM.
    # ⚠️ `plateia_evento` comeca com `that ` (o `_aqui` troca por `this `) e foi
    # LIDO dentro do hook antes de entrar: os HOOKS dizem `in {evento}` e
    # `out of {evento}`, entao `that pier` (que sairia "in this pier") foi
    # descartado na mesa em favor de lugares que leem com `in`.
    # ⚠️ `plateia` e' substantivo plural NU, sem artigo — o TAKE monta
    # `the blurred %s keep laughing`.
    # ======================================================================
    {"id": "barbearia", "selo": "N",
     "cenario": "a busy barbershop",
     "detalhe": "three chairs facing a mirrored wall behind them, a row of "
                "waiting chairs beside him, no readable signs",
     "plateia": "waiting customers", "plateia_evento": "that barbershop",
     "eco": "the same barbershop",
     "luz": "Warm even light bouncing off the mirrors.",
     "audio": "clippers buzzing, room chatter."},
    {"id": "academia", "selo": "N",
     "cenario": "the free-weight area of a busy gym",
     "detalhe": "racks of dumbbells and a mirrored wall behind them, a flat "
                "bench beside him, no readable logos",
     "plateia": "gym members", "plateia_evento": "that gym",
     "eco": "the same gym floor",
     "luz": "Bright even overhead gym light.",
     "audio": "weights clanking, a treadmill running."},
    {"id": "leilao", "selo": "N",
     "cenario": "a packed livestock auction barn",
     "detalhe": "tiered wooden benches around a sawdust ring, a raised "
                "auctioneer's box behind it, a rolled paper program in his "
                "hand, no readable signs",
     "plateia": "bidders", "plateia_evento": "that auction barn",
     "eco": "the same auction barn",
     "luz": "Dusty overhead barn light with daylight from a side door.",
     "audio": "the auctioneer's chant, cattle moving in the ring."},
    {"id": "estacao", "selo": "N",
     "cenario": "a crowded commuter train station",
     "detalhe": "a yellow line painted along the platform edge and a steel "
                "canopy overhead, a bench and a rolling bag beside him, no "
                "readable signs",
     "plateia": "commuters", "plateia_evento": "that train station",
     "eco": "the same platform",
     "luz": "Flat daylight under the platform canopy.",
     "audio": "a train braking, platform announcements."},
    {"id": "casamento", "selo": "N",
     "cenario": "a wedding reception hall",
     "detalhe": "round tables under white cloths and an empty dance floor "
                "behind them, a chair pushed back beside him, no readable "
                "banners",
     "plateia": "guests", "plateia_evento": "that wedding hall",
     "eco": "the same reception hall",
     "luz": "Warm low light from strings of bulbs overhead.",
     "audio": "a band playing, room chatter."},
    {"id": "centro_comunitario", "selo": "N",
     "cenario": "the main hall of a community center at a potluck",
     "detalhe": "long tables of covered dishes and stacked folding chairs "
                "behind them, a paper plate in his hand, no readable signs",
     "plateia": "neighbors", "plateia_evento": "that community center",
     "eco": "the same community hall",
     "luz": "Flat warm light from ceiling panels.",
     "audio": "hall chatter, a chair scraping the floor."},
]

# PE1 — a mancha vive do CONTRASTE. Roupa de baixo sempre CLARA.
# ⛔ Calca escura mata o hook: a mancha some e o video perde a evidencia.
ROUPAS = [
    {"id": "khaki_shorts", "peca": "light khaki cargo shorts"},
    {"id": "moletom_cinza", "peca": "light gray sweatpants"},
    {"id": "chino_bege", "peca": "beige chinos"},
    {"id": "linho_creme", "peca": "cream linen trousers"},
    {"id": "calca_areia", "peca": "pale tan work pants"},
    # + 2026-08-01: o operador mediu vicio — a mesma calca clara voltando no
    # lote. Pool dobrado, todas claras (a mancha continua vivendo do contraste).
    {"id": "bermuda_golfe", "peca": "white golf shorts"},
    {"id": "jeans_claro", "peca": "light stone-washed jeans"},
    {"id": "pintor", "peca": "off-white painter's pants"},
    {"id": "veludo_bege", "peca": "light tan corduroy trousers"},
    {"id": "jogger_aveia", "peca": "oatmeal fleece joggers"},
]

# Fila de reformulacao do selo 🟡 — se a formulacao 1 recusar, tentar a 2 etc.
MANCHA = [
    "a large dark wet stain spreading across the front of his {peca}",
    "a large dark patch of wet fabric across the front of his {peca}",
    "his {peca} are soaked dark down the front",
]

# Set das cenas 2/3/5 (PE8 — cenas 2-5 sao o FLAGRANTE, luz travada nas 4)
AMBIENTES = [
    {"id": "cozinha", "set": "a plain kitchen, cabinets and a window behind him",
     "bancada": "counter", "curto": "kitchen", "luz": "warm lamp light."},
    {"id": "cozinha_aberta",
     "set": "an open-plan kitchen with an island, a living room out of focus behind him",
     "bancada": "island", "curto": "kitchen",
     "luz": "warm even light from a window frame-left."},
    {"id": "churrasqueira",
     "set": "an outdoor grill station in a backyard, a wooden fence behind him",
     "bancada": "grill counter", "curto": "grill station",
     "luz": "late afternoon sunlight from frame-left."},
    {"id": "varanda",
     "set": "a covered back porch, a screen door and potted plants behind him",
     "bancada": "porch table", "curto": "back porch", "luz": "soft shaded daylight."},
    {"id": "garagem",
     "set": "a clean home garage workshop, pegboard tools on the wall behind him",
     "bancada": "workbench", "curto": "garage workshop",
     "luz": "cool overhead shop light."},
    # + 2026-08-01: o operador mediu vicio — o mesmo set interno voltando no
    # lote. Pool dobrado.
    {"id": "sala_jantar",
     "set": "a small dining room, a hutch of dishes against the wall behind him",
     "bancada": "dining table", "curto": "dining room",
     "luz": "warm light from a hanging fixture overhead."},
    {"id": "galpao",
     "set": "a backyard tool shed with a rough plank wall behind him",
     "bancada": "work table", "curto": "tool shed",
     "luz": "daylight through an open shed door frame-right."},
    {"id": "alpendre",
     "set": "a screened front porch, a painted railing and a quiet street out of focus behind him",
     "bancada": "side table", "curto": "front porch",
     "luz": "low golden evening light."},
    {"id": "trailer",
     "set": "the kitchenette of a camper trailer, narrow cabinets and a small window behind him",
     "bancada": "galley counter", "curto": "camper kitchenette",
     "luz": "flat light from a small window frame-right."},
    {"id": "porao_bar",
     "set": "a finished basement with a home bar and shelves of glasses behind him",
     "bancada": "bar top", "curto": "basement bar",
     "luz": "warm light from two hanging bulbs."},
    # ======================================================================
    # + 2026-08-13: 10 -> 20. Ordem do operador: *"aumente o pool de opcoes
    # substancialmente, tambem dos ambientes"*.
    # ⛔ AS QUATRO CHAVES SAO OBRIGATORIAS E CADA UMA CAI NUM LUGAR DIFERENTE
    # DO PROMPT — entrada nova que erre uma delas quebra a frase montada, nao o
    # sorteio, e por isso o defeito so' apareceria no render:
    #   · `set`     -> "Medium close-up in %s." — le' depois de `in `.
    #   · `bancada` -> "stands behind the %s" — substantivo NU, sem artigo, e
    #                  ele volta em "same %s" na IMAGE 03 (o insert das maos).
    #                  Tem de ser uma superficie onde caiba preparar o sache.
    #   · `curto`   -> "Close-up in the same %s" — o nome curto do lugar.
    #   · `luz`     -> entra minusculo depois de virgula E capitalizado no
    #                  comeco de frase; por isso comeca minusculo e termina em
    #                  ponto. As dez antigas ja' seguiam isso.
    # ⭐ E o criterio das dez novas e' o mesmo dos LOCAIS: muda a GEOMETRIA
    # (bancada estreita de corredor, tampa de caminhonete ao ar livre, mesa de
    # piquenique, bancada de vaso no quintal, escrivaninha), nao so' o rotulo
    # do comodo. Cinco delas sao ao ar livre ou semiabertas, o que o pool tinha
    # em 3 de 10.
    # ⛔ PE8: a luz e' travada nas cenas 2-5 pelo motor, entao ela tem de ser
    # uma so' frase que sirva a TRES quadros do mesmo lugar — nada de luz que
    # so' exista num horario ("the last ten minutes of sunset").
    # ======================================================================
    {"id": "cozinha_rustica",
     "set": "a farmhouse kitchen with open shelves and a deep enamel sink behind him",
     "bancada": "wooden counter", "curto": "farmhouse kitchen",
     "luz": "steady morning light from a window frame-right."},
    {"id": "cozinha_corredor",
     "set": "a narrow galley kitchen with white tile behind him and a window over the sink",
     "bancada": "counter", "curto": "galley kitchen",
     "luz": "cool daylight coming in over the sink."},
    {"id": "deck",
     "set": "a wooden deck off the back of the house, a plain railing and tall trees behind him",
     "bancada": "deck table", "curto": "back deck",
     "luz": "dappled afternoon light through the trees."},
    {"id": "sala_estar",
     "set": "a plain living room, a sofa and a framed picture on the wall behind him",
     "bancada": "coffee table", "curto": "living room",
     "luz": "warm lamp light with daylight from a window frame-left."},
    {"id": "escritorio",
     "set": "a small home office, a bookshelf and a closed window blind behind him",
     "bancada": "desk", "curto": "home office",
     "luz": "warm light from a desk lamp frame-right."},
    {"id": "caminhonete",
     "set": "the open tailgate of a pickup truck parked on a gravel drive, tall grass and a treeline behind him",
     "bancada": "tailgate", "curto": "truck tailgate",
     "luz": "bright open daylight, high and even."},
    {"id": "acampamento",
     "set": "a campsite picnic table beside a canvas tent, pine woods behind him",
     "bancada": "picnic table", "curto": "campsite table",
     "luz": "soft morning light filtered through the pines."},
    {"id": "celeiro_bancada",
     "set": "a work bench inside a small barn, hand tools hanging on the plank wall behind him",
     "bancada": "bench top", "curto": "barn workshop",
     "luz": "daylight through an open barn door frame-left."},
    # ⚠️ `lavanderia_casa`, nao `lavanderia`: o pool LOCAIS ja' tem uma
    # `lavanderia` (a publica, de maquinas de fila). Os dois ids vivem em
    # eixos diferentes do ledger e nao colidem em codigo — colidem na cabeca de
    # quem le' o painel, que e' onde o erro sai caro.
    {"id": "lavanderia_casa",
     "set": "a home laundry room, a washer and dryer and a shelf of bottles behind him",
     "bancada": "folding counter", "curto": "laundry room",
     "luz": "flat white light from a ceiling fixture."},
    {"id": "horta",
     "set": "a raised garden bed at the back of the yard, tomato cages and a wooden fence behind him",
     "bancada": "potting bench", "curto": "garden bench",
     "luz": "bright open afternoon light."},
]

# PE9 — contraste ≥3 eixos garantido por CONSTRUCAO: o narrador sempre tem
# cabeleira farta, e' barbeado e nao usa oculos; a vitima e' sempre careca,
# de bigode e de oculos. Nenhuma verificacao necessaria (F4b).
#
# ===========================================================================
# ⭐⭐ POOL REESCRITO E DOBRADO EM 2026-08-10 — "O REF ESTA' PARECENDO O
# MORGAN FREEMAN" (relato de campo do operador, com quatro lotes na mao)
# ===========================================================================
# ⛔⛔ O QUE ELE ORDENOU, LITERAL: *"mude tb o pool de opcoes de ref (veja no
# print que o ref ta parecendo o morgan freeman), nao falar de celebridade nem
# usar a palavra famoso, celebridade no prompt, muito menos dizer burramente no
# prompt 'not morgan freeman', 'not celebrity', 'not famous people'"*.
#
# ⭐ POR QUE SAIA SEMPRE O MESMO HOMEM — e nao era o tamanho do pool.
# As treze entradas antigas descreviam o narrador por CABELO + UMA ANCORA. Doze
# das treze diziam `full/thick <silver|gray|white|snow-white> hair`. Junte isso
# ao resto do BLOCO 0, que era travado e identico em todo sorteio — `a wide warm
# natural smile`, `chest up, facing camera`, `plain gray background, soft light`
# — e o prompt inteiro descreve um retrato de estudio de um senhor grisalho de
# sorriso largo. Esse e' o CENTRO EXATO do atrator; o modelo preenche o rosto
# com a media do treino, e a media tem nome.
# ⛔ E a clausula `not a celebrity` PIORAVA: ela injeta o token `celebrity` no
# campo, que e' municao (licoes-producao-veo §Declaracao e' municao). Saiu do
# arquivo inteiro neste commit — ver a lapide onde ela morava.
#
# ⭐⭐ O CONSERTO E' GEOMETRIA, NAO NEGACAO. A doutrina do repo ja' dizia como
# (espinha-fixa §Construir o REF contra a celebridade): *"a defesa nao e' negar
# celebridade; e' descrever um rosto que nenhuma celebridade tem. Rosto
# interessante-mas-generico deriva; rosto especifico nao tem para onde derivar."*
# Entao toda entrada daqui carrega TRES coisas, nesta ordem:
#     <cabelo: cor + CORTE + nascimento do cabelo>  ·  <ARQUITETURA DO ROSTO:
#     formato, testa/arcada, nariz, maxilar, malar, olhos>  ·  <ancora>
# A do meio e' a nova, e e' ela que faz o trabalho. Um `broad flat-planed face,
# high cheekbones, a broad flat-bridged nose` nao tem para onde derivar.
#
# ⛔ CINCO DAS 24 NAO SAO GRISALHAS (castanho com grisalho so' na tempora,
# preto entremeado, preto denso, cachos escuros, castanho-avermelhado). Um pool
# 100% prateado e' um pool de um homem so', por mais ancoras que ele tenha.
#
# ⛔ O QUE CONTINUA PROIBIDO AQUI, e cada um por um motivo pago:
#   · OCULOS, PELO FACIAL e CALVICIE — os tres eixos da VITIMA (PE9/F4b). Sao o
#     contraste de 3 eixos a' distancia, e nascem por construcao. As duas
#     isencoes no `medir_personagens.py` sao exatamente estas.
#   · ANCORA DE DENTE (`gold crown`, `wide gap between his front teeth`) — as
#     duas entradas antigas que a usavam SAIRAM, e nao por gosto: desde a CL25
#     (2026-08-10) o BLOCO 0 declara `the front teeth even, white and complete`.
#     Coroa e falha CONTRADIZEM a string travada dentro do mesmo prompt, e
#     contradicao dentro do prompt e' onde o gerador inventa (mesma familia do
#     defeito das duas colheres).
#   · DETERIORACAO — `gaunt`, `bony`, `leathery`, `weather-beaten`, palpebra
#     caida, nariz quebrado, dente lascado. Vira mendigo e mata a credibilidade
#     do narrador, que e' a autoridade da cena.
#   · APROVACAO — `handsome`, `chiseled`, `distinguished`, `strong jaw`,
#     `piercing eyes`. Sao os adjetivos que empurram PARA a celebridade.
#   · `big` cru e `huge` — o `BANIDOS_IMAGE` deste motor pega os dois.
#   · ETNIA — zero mencao: quem injeta e' o `ETNIA[pagina]`, e o cabelo por isso
#     e' descrito por COR/CORTE/COMPRIMENTO, nunca por textura de uma etnia so'.
# ⚠️ Repetir nunca mais foi so' questao de pool: o `_sortear_longo` passou a
# levar o `ref` no ledger (evita as 8 ultimas) — antes era `rng.choice` puro,
# sem memoria nenhuma, e era isso que trazia a mesma cara duas vezes no lote.
# ===========================================================================
# ⛔⛔ ONZE ENTRADAS DESTE POOL FORAM SANEADAS EM 2026-08-13 — ordem do
# operador: *"melhore a aparencia e shape desses homens"*.
# ===========================================================================
# ⭐ O pool foi reescrito em 10/08 contra a CELEBRIDADE e ganhou a arquitetura
# facial que o separa. O que ele NAO tinha era o outro lado da tabela: das 24
# entradas, ONZE descreviam o narrador por DETERIORACAO — cinco cicatrizes,
# `hollow cheeks`, `a face tanned deep from years outdoors`, `a dark age spot`,
# `sun-spotted skin`, `a ruddy face`, `skin deeply lined`, `a torn right
# earlobe`. Some as onze marcas de dano; ficam as onze ARQUITETURAS, que sao o
# que faz o trabalho contra o atrator.
# ⚠️ E NENHUMA entrada perdeu ancora: cicatriz saiu e entrou pinta, covinha,
# queixo partido, mancha clara, sarda, argola/pino. A ancora e' o que faz o
# rosto VOLTAR IGUAL no segundo take (P6) — tirar sem repor seria trocar um
# defeito por outro pior.
# ⚠️ A PELE tambem continua acionada, so' que do lado saudavel: lightly
# tanned, freckled, smooth-skinned, laugh lines. O eixo `pele` do
# medir_personagens casa com os quatro.
# ⛔ O narrador deste angulo e' a AUTORIDADE da cena — quem chora e se humilha
# e' a vitima, ao lado dele, no mesmo quadro. Narrador com cara de castigo faz
# o video virar desgraca alheia, e desgraca alheia nao vende receita nenhuma.
REFS = [
    {"id": "risca_lateral", "idade": 62,
     "marca": "dark brown hair going gray only at the temples, combed into a "
              "low side part, a broad square face with a heavy flat brow and a "
              "wide mouth, lightly tanned skin, and a deep "
              "vertical cleft in his chin",
     "cabelo": "dark brown", "roupa": "Plain navy crew-neck tee shirt.",
     "roupa_curta": "navy tee shirt"},
    {"id": "topete_ferro", "idade": 66,
     "marca": "thick iron-gray hair standing up from a high square hairline, a "
              "short broad face with full cheeks and a blunt upturned nose, and "
              "a dark mole high on his left cheekbone",
     "cabelo": "iron-gray", "roupa": "Plain olive crew-neck tee shirt.",
     "roupa_curta": "olive tee shirt"},
    {"id": "bico_de_viuva", "idade": 59,
     "marca": "black hair shot through with gray, dropping to a low widow's "
              "peak at the center of his forehead, deep-set eyes under a heavy "
              "brow ridge and a long chin, and a raised dark mole in the "
              "middle of his right cheek",
     "cabelo": "black and gray", "roupa": "Plain charcoal crew-neck tee shirt.",
     "roupa_curta": "charcoal tee shirt"},
    {"id": "corte_rente", "idade": 64,
     "marca": "hair cropped close to the scalp all over, gray at the sides and "
              "darker on top, a wide flat-planed face with high cheekbones and "
              "a broad flat-bridged nose, and a small notch missing from the "
              "top of his left ear",
     "cabelo": "gray", "roupa": "Plain slate blue crew-neck tee shirt.",
     "roupa_curta": "slate blue tee shirt"},
    {"id": "cachos_colarinho", "idade": 61,
     "marca": "ash-gray hair worn long enough to curl over his collar, a narrow "
              "face with a high forehead and a thin straight nose, laugh lines "
              "fanning from the corners of his eyes, and a gold stud in his "
              "right earlobe",
     "cabelo": "ash-gray", "roupa": "Plain faded red crew-neck tee shirt.",
     "roupa_curta": "faded red tee shirt"},
    {"id": "flat_top", "idade": 73,
     "marca": "a thick pewter flat-top cut squared off across the top, a long "
              "jaw and flat cheeks under high cheekbones, lightly tanned skin, "
              "and a dark mole at the outer corner of his left eye",
     "cabelo": "pewter", "roupa": "Plain heather gray crew-neck tee shirt.",
     "roupa_curta": "heather gray tee shirt"},
    {"id": "juba_para_tras", "idade": 71,
     "marca": "a heavy snow-white mane brushed straight back over his ears, a "
              "long narrow face on a tall rangy frame, and a small dark beauty "
              "mark on his right temple",
     "cabelo": "snow-white", "roupa": "Plain tan crew-neck tee shirt.",
     "roupa_curta": "tan tee shirt"},
    {"id": "franja_frente", "idade": 69,
     "marca": "a heavy gray-brown mop combed forward over his forehead, a round "
              "face with full cheeks, a short blunt nose and thick eyebrows "
              "that meet in a single line, and a raised mole beside his left "
              "nostril",
     "cabelo": "gray-brown", "roupa": "Plain dusty blue crew-neck tee shirt.",
     "roupa_curta": "dusty blue tee shirt"},
    {"id": "mecha_branca", "idade": 64,
     "marca": "gray hair parted on the side with a bright white streak at his "
              "left temple, a soft oval face with a rounded chin and wide-set "
              "eyes, and a deep dimple in his chin",
     "cabelo": "gray", "roupa": "Plain teal crew-neck tee shirt.",
     "roupa_curta": "teal tee shirt"},
    {"id": "cabelo_grosso", "idade": 67,
     "marca": "thick coarse silver hair cut short at the sides, a heavy-set "
              "square frame and a broad face with a short forehead, and a "
              "coin-sized dark birthmark on the side of his jaw",
     "cabelo": "silver", "roupa": "Plain black crew-neck tee shirt.",
     "roupa_curta": "black tee shirt"},
    {"id": "cabelo_fino", "idade": 58,
     "marca": "fine sandy hair gone gray at the crown and combed flat, a lean "
              "face with a sharp chin and a long straight nose, and a small "
              "silver hoop in his left ear",
     "cabelo": "sandy gray", "roupa": "Plain forest green crew-neck tee shirt.",
     "roupa_curta": "forest green tee shirt"},
    {"id": "cabeca_quadrada", "idade": 70,
     "marca": "white hair cut in a short even taper, a wide square face with a "
              "low hairline and a jaw that squares off at the corners, "
              "smooth-skinned across the forehead, and a pale patch of white "
              "skin the length of a thumbnail along his left jaw",
     "cabelo": "white", "roupa": "Plain brown crew-neck tee shirt.",
     "roupa_curta": "brown tee shirt"},
    {"id": "sardento", "idade": 63,
     "marca": "thick salt-and-pepper hair with a stubborn cowlick at the crown, "
              "a round face and a blunt nose, a spray of dark freckles across "
              "his nose and both cheekbones, and a deep dimple in his left cheek",
     "cabelo": "salt-and-pepper",
     "roupa": "Plain rust orange crew-neck tee shirt.",
     "roupa_curta": "rust orange tee shirt"},
    {"id": "olhos_diferentes", "idade": 65,
     "marca": "steel-gray hair combed straight back, one eye pale ice-blue and "
              "the other dark brown, a narrow face with a high-bridged nose and "
              "a short upper lip",
     "cabelo": "steel-gray", "roupa": "Plain burgundy crew-neck tee shirt.",
     "roupa_curta": "burgundy tee shirt"},
    {"id": "preto_denso", "idade": 60,
     "marca": "hair still mostly black, cut short and dense, gray only in front "
              "of the ears, a broad face with a heavy jaw and a short forehead, "
              "and a raised mole under his right eye",
     "cabelo": "black", "roupa": "Plain stone gray crew-neck tee shirt.",
     "roupa_curta": "stone gray tee shirt"},
    {"id": "cabelo_alto", "idade": 68,
     "marca": "thick white hair standing high off a deep hairline, a long face "
              "with a narrow chin and a prominent bump in the bridge of his "
              "nose, laugh lines at the corners of his mouth, and a dark "
              "beauty mark just under his lower lip",
     "cabelo": "white", "roupa": "Plain denim blue crew-neck tee shirt.",
     "roupa_curta": "denim blue tee shirt"},
    {"id": "barril", "idade": 66,
     "marca": "short pewter hair with a hard part cut into the left side, a "
              "barrel-chested build and a wide round face, and a dark birthmark "
              "the size of a dime above his right eyebrow",
     "cabelo": "pewter", "roupa": "Plain mustard crew-neck tee shirt.",
     "roupa_curta": "mustard tee shirt"},
    {"id": "compacto", "idade": 74,
     "marca": "thin white hair combed back off a high forehead, a long narrow "
              "face with sharp cheekbones on a compact frame, and two small "
              "dark moles in a line on his right temple",
     "cabelo": "white", "roupa": "Plain plum crew-neck tee shirt.",
     "roupa_curta": "plum tee shirt"},
    {"id": "ruivo_desbotado", "idade": 61,
     "marca": "rust-red hair faded to sandy gray, cut short and combed to one "
              "side, a freckled face with laugh lines bracketing his mouth and "
              "a square chin, and a deep dimple in each cheek",
     "cabelo": "rust-red and gray",
     "roupa": "Plain hunter green crew-neck tee shirt.",
     "roupa_curta": "hunter green tee shirt"},
    {"id": "cachos_escuros", "idade": 59,
     "marca": "dense dark curls cut close at the sides and gray at the temples, "
              "a broad-shouldered build and a wide open face with a heavy "
              "level brow, and a small dark mole above his left eyebrow",
     "cabelo": "dark", "roupa": "Plain cream crew-neck tee shirt.",
     "roupa_curta": "cream tee shirt"},
    {"id": "risca_no_meio", "idade": 72,
     "marca": "fine ash-white hair parted down the middle and tucked behind his "
              "ears, a long jaw and a wide mouth, lightly tanned skin across "
              "the forehead, and a heavy silver ring in his right earlobe",
     "cabelo": "ash-white", "roupa": "Plain sky blue crew-neck tee shirt.",
     "roupa_curta": "sky blue tee shirt"},
    {"id": "escovinha", "idade": 63,
     "marca": "iron-gray hair buzzed to an even short brush all over, a square "
              "heavy-set frame with a flat brow and small close-set eyes, and a "
              "birthmark shaped like a comma on his left cheek",
     "cabelo": "iron-gray", "roupa": "Plain maroon crew-neck tee shirt.",
     "roupa_curta": "maroon tee shirt"},
    {"id": "castanho_alto", "idade": 57,
     "marca": "thick chestnut hair, gray above the ears, worn long on top and "
              "short at the sides, a heart-shaped face with a pointed chin and "
              "laugh lines around the eyes, and a small dark beauty mark "
              "beside his left nostril",
     "cabelo": "chestnut", "roupa": "Plain slate crew-neck tee shirt.",
     "roupa_curta": "slate tee shirt"},
    {"id": "ondas_baixas", "idade": 65,
     "marca": "heavy gray waves worn low across the forehead, a wide flat face "
              "with a broad nose and a heavy under-jaw, and a pale patch of "
              "white skin the size of a coin on his right jaw",
     "cabelo": "gray", "roupa": "Plain indigo crew-neck tee shirt.",
     "roupa_curta": "indigo tee shirt"},
]

VITIMAS = [
    # ⛔⛔ SETE ENTRADAS SANEADAS EM 2026-08-13 — mesma passada dos REFS, mesma
    # ordem do operador (*"melhore a aparencia e shape desses homens"*), e aqui
    # o motivo e' ainda mais direto: a VITIMA e' quem o espectador tem de
    # RECONHECER COMO ELE MESMO. Se ela chora, se humilha E AINDA parece
    # castigada, o video vira desgraca alheia e o homem do outro lado da tela
    # se distancia em vez de se reconhecer. Sairam `a deeply lined forehead`,
    # `a sun-spotted scalp`, `a shallow scar`, `a ruddy face` (x2),
    # `liver-spotted temples`, `skin creased deep` e `sun-spotted temples`.
    # ⚠️ Nenhuma perdeu ancora nem perdeu o eixo `pele`: entrou sarda, pele
    # lisa, pele levemente bronzeada e linhas de riso — que e' o mesmo eixo
    # medido, do lado saudavel da tabela.
    # ⛔ CARECA + BIGODE + OCULOS continua travado nas 20 (PE9/F4b) e o
    # autoteste cobra os tres em cada entrada.
    # ⚠️ 2026-08-10 — as nove primeiras GANHARAM PELE E ANCORA FACIAL, e o
    # bigode/oculos/camisa de cada uma ficou INTACTO. Motivo medido: o pool
    # marcava `pele` em 3/20 e `ancora` em 2/20 — e a ancora e' justamente o
    # que faz o rosto VOLTAR IGUAL entre os dois takes (P6). Sem ela o Veo
    # redesenha a vitima na cena 2 e o espectador ve' outro homem.
    # ⛔ Nenhuma ancora aqui repete ancora do pool REFS deste arquivo (nem a
    # marca nem o LUGAR dela): ancora igual entre narrador e vitima remenda o
    # morphing que o PE9 existe para impedir, e os dois dividem o IMAGE 01.
    {"id": "cinza_preto", "idade": 63,
     "marca": "bald man with a thick gray mustache, a wide freckled forehead, "
              "black-framed glasses and a small dark mole in the middle of his "
              "forehead",
     "camisa": "a pale blue t-shirt"},
    {"id": "ruivo_arame", "idade": 62,
     "marca": "bald man with a red mustache, wire-rimmed glasses and a pale "
              "birthmark shaped like a teardrop under his right ear",
     "camisa": "a white polo shirt"},
    {"id": "branco_quadrado", "idade": 65,
     "marca": "bald man with a white mustache, a smooth-skinned scalp, thick "
              "square glasses and a deep cleft in the point of his chin",
     "camisa": "a light gray t-shirt"},
    {"id": "curto_redondo", "idade": 61,
     "marca": "bald man with a short gray mustache, round wire glasses and a "
              "dark beauty mark at the corner of his mouth",
     "camisa": "a pale yellow polo shirt"},
    # + 2026-08-01: o operador mediu vicio — a mesma vitima voltando no lote.
    # Pool ampliado; careca + bigode + oculos continua travado.
    {"id": "aviador", "idade": 64,
     "marca": "bald man with a bushy salt-and-pepper mustache, a lightly tanned face and gold aviator glasses",
     "camisa": "a faded sage green t-shirt"},
    {"id": "sem_aro", "idade": 60,
     "marca": "bald man with a thin white mustache, rimless glasses and a "
              "small mole on the bridge of his nose",
     "camisa": "a cream henley shirt"},
    {"id": "tartaruga", "idade": 66,
     "marca": "bald man with a drooping gray mustache, laugh lines around his mouth and heavy tortoiseshell glasses",
     "camisa": "a pale pink polo shirt"},
    {"id": "meia_armacao", "idade": 63,
     "marca": "bald man with a gray horseshoe fringe, a wide silver mustache and half-rim reading glasses",
     "camisa": "a light peach t-shirt"},
    {"id": "oval_marrom", "idade": 67,
     "marca": "bald man with a close-trimmed sandy mustache, oval brown-framed "
              "glasses and a birthmark like a coffee stain on the back of his "
              "scalp",
     "camisa": "a soft mint green polo shirt"},
    # + 2026-08-02: o operador mediu o pool inteiro e viu A MESMA VITIMA
    # voltando — as nove acima variam bigode e oculos e mais nada, entao o
    # gerador recebia quase a mesma frase e devolvia quase o mesmo rosto. As
    # tres novas trazem os eixos que este pool nao acionava: PORTE
    # (compleicao), PELE (textura de idade) e uma ANCORA FACIAL permanente
    # (P6), que e' o que faz o rosto voltar igual entre as cenas.
    #   · careca + bigode + oculos continua TRAVADO nas tres (PE9/F4b: sao os
    #     3 eixos que separam a vitima do narrador a' distancia).
    #   · a ancora e' sempre do lado ✅ de licoes-producao-veo §REF —
    #     DISTINTIVO, NUNCA DETERIORADO (pinta, covinha, feicao de nariz).
    #     ⛔ dente lascado, bigode manchado de nicotina e oculos remendados
    #     com fita ficaram de fora: viram mendigo e matam a credibilidade.
    #   · nenhuma repete ancora dos REFS deste arquivo — mancha senil na
    #     tempora, lobulo rasgado, cicatriz no labio, sobrancelhas unidas,
    #     covinha no queixo. Ancora identica entre narrador e vitima remenda o
    #     morphing que o PE9 existe para impedir, e os dois aparecem juntos no
    #     mesmo IMAGE 01/05.
    #   · zero mencao a etnia: o motor injeta ETNIA[pagina] antes da marca.
    {"id": "morsa", "idade": 69,
     "marca": "bald man with a heavy build and jowls, a full snow-white walrus mustache, small half-moon glasses low on his nose and a raised mole beside one nostril",
     "camisa": "a washed-out lavender bowling shirt"},
    {"id": "vermelho_grosso", "idade": 68,
     "marca": "bald man with a soft middle and smooth-skinned temples, a thin mustache dyed too dark for his age, chunky red plastic glasses and a deep dimple in his left cheek",
     "camisa": "a washed tan plaid flannel shirt"},
    {"id": "clipe_solar", "idade": 56,
     "marca": "bald man with a tall rangy frame and a prominent Adam's apple, a thick charcoal mustache gray only at the tips, plain metal glasses with clip-on sun lenses flipped up and a bump in the bridge of his nose",
     "camisa": "a loose seafoam green fishing shirt"},
    # ======================================================================
    # + 2026-08-10: TERCEIRA AMPLIACAO, no mesmo lote em que os REFS foram
    # reescritos. O operador leu quatro roteiros e viu a MESMA DUPLA nos
    # quatro — e a vitima repete pelo mesmo motivo que o narrador repetia:
    # `rng.choice` puro, sem ledger, e doze entradas que variavam BIGODE e
    # OCULOS e mais nada. Bigode e oculos sao os dois acessorios; nenhum dos
    # dois e' a CABECA. Careca com bigode grisalho e oculos e' um homem so'.
    #
    # ⭐ AS OITO NOVAS ABREM O QUE FALTAVA: o FORMATO DO CRANIO (que num
    # careca e' o rosto inteiro — domo largo, achatado atras, quadrado, ovo
    # alto, estreito e inclinado), o MAXILAR e a TESTA. O bigode e os oculos
    # continuam ali, mas agora sao o acabamento, nao a descricao.
    # ⛔ CARECA + BIGODE + OCULOS CONTINUA TRAVADO nas oito, e o autoteste
    # cobra os tres em CADA entrada: sao o contraste de 3 eixos a' distancia
    # contra o narrador (PE9/F4b), e ele nasce por construcao ou nao nasce.
    # ⛔ A ancora e' sempre do lado ✅ de licoes-producao-veo §REF —
    # DISTINTIVO, NUNCA DETERIORADO. A vitima chora e se humilha em quadro;
    # se ela AINDA parecer maltratada, o video vira desgraca alheia e nao
    # espelho, e o espectador nao se reconhece.
    # ⚠️ zero mencao a etnia: o motor injeta ETNIA[pagina] antes da marca.
    # ======================================================================
    {"id": "cranio_estreito", "idade": 58,
     "marca": "bald man with a compact wiry frame, a narrow skull and ears "
              "that stand out, a pencil-thin gray mustache and thin steel "
              "rectangular glasses",
     "camisa": "a striped blue and white oxford shirt"},
    {"id": "domo_largo", "idade": 70,
     "marca": "bald man with a broad domed skull over a short thick body, a "
              "lightly tanned scalp, a wide brush mustache gone entirely white and "
              "heavy black plastic glasses",
     "camisa": "a burgundy short-sleeve button-down"},
    {"id": "nuca_reta", "idade": 62,
     "marca": "bald man with a long flat-backed skull, laugh lines at the "
              "corners of his eyes, a chevron mustache still dark under the "
              "nose and thin gold wire glasses",
     "camisa": "a pale gray polo shirt"},
    {"id": "cabeca_redonda", "idade": 65,
     "marca": "bald man with a round head, full cheeks and a freckled scalp, "
              "a drooping sandy mustache and blue plastic reading glasses low "
              "on his nose",
     "camisa": "a light denim work shirt"},
    {"id": "cranio_quadrado", "idade": 59,
     "marca": "bald man with a square blocky skull and a heavy jaw, a clipped "
              "charcoal mustache, matte black rectangular glasses and a dark "
              "mole on the tip of his chin",
     "camisa": "a heather gray henley"},
    {"id": "cranio_inclinado", "idade": 68,
     "marca": "bald man with a narrow sloping skull and freckled temples, "
              "a thin silver mustache and oversized square tortoiseshell "
              "glasses",
     "camisa": "a faded olive polo shirt"},
    {"id": "testa_baixa", "idade": 61,
     "marca": "bald man with a wide low forehead on a stocky barrel build, a "
              "bushy iron-gray mustache, round gold-rimmed glasses and a "
              "birthmark shaped like a leaf on his left temple",
     "camisa": "a pale blue camp shirt"},
    {"id": "cabeca_ovo", "idade": 66,
     "marca": "bald man with a tall egg-shaped skull and a long thin body, a "
              "neat white horseshoe mustache and half-rim glasses hanging "
              "from a black cord",
     "camisa": "a soft cream polo shirt"},
]

MULHERES = [
    {"idade": 58, "payoff": "with chin-length wavy hair, in a red dress"},
    {"idade": 59, "payoff": "with long straight hair, in a navy wrap dress"},
    {"idade": 57, "payoff": "with short curly hair, in an emerald dress"},
    {"idade": 60, "payoff": "with shoulder-length hair, in a burgundy dress"},
    # + 2026-08-01: o operador mediu vicio — a mesma mulher no payoff, lote
    # atras de lote. Pool ampliado.
    {"idade": 61, "payoff": "with a short silver bob, in a teal blouse and skirt"},
    {"idade": 56, "payoff": "with her hair pinned up in a bun, in a mustard yellow dress"},
    {"idade": 62, "payoff": "with a long gray braid over one shoulder, in a plum dress"},
    {"idade": 55, "payoff": "with cropped white hair, in a coral sundress"},
    {"idade": 59, "payoff": "with loose gray waves, in a forest green dress"},
    {"idade": 58, "payoff": "with a low ponytail, in a cream blouse and a charcoal skirt"},
    # + 2026-08-02: mesma medicao que gerou o bloco das VITIMAS logo acima, so'
    # que do lado da mulher do payoff — o operador viu SEMPRE O MESMO ROSTO. As
    # dez acima dizem CABELO + VESTIDO e mais nada: dez mulheres descritas so'
    # por cabelo sao a mesma mulher dez vezes, e o gerador devolvia quase a
    # mesma cara. As seis novas abrem os tres eixos ZERADOS deste pool:
    #   · PORTE — slight, broad-shouldered, short-round, heavy-set,
    #     tall-narrow, wiry. Nenhuma das dez acima menciona compleicao.
    #   · OCULOS — correntinha de micangas, meia-lua, armacao vermelha grossa,
    #     oculos de sol na cabeca. Eram 0/10 aqui.
    #   · PELE — deeply lined, sun-weathered, freckles, laugh lines.
    #   · e uma ANCORA FACIAL permanente em cada (P6), sempre do lado ✅ da
    #     tabela de licoes-producao-veo §REF — DISTINTIVO, NUNCA DETERIORADO
    #     (pinta, cicatriz limpa, sarda, dente separado). ⛔ dente lascado
    #     ficou de fora: vira mendigo e mata a credibilidade.
    #   · ⛔ zero `big`/`huge`: o payoff aterrissa na IMAGE 04/05 e o
    #     BANIDOS_IMAGE deste motor pega `big(?!-box)`.
    #   · zero mencao a etnia: o motor injeta ETNIA[pagina] antes do payoff.
    # ⚠️ REESCRITA EM 2026-08-13: era `a deeply lined face`. A lente nova
    # do autoteste pegou — pele castigada esta' na lista de PROIBIDO, e as
    # linhas de riso dizem a mesma idade sem dizer o mesmo castigo.
    {"idade": 66,
     "payoff": "with a small, slight frame and laugh lines around her eyes, "
               "thin white hair set in tight permed curls, reading glasses on "
               "a beaded chain and a dark mole beside her right nostril, in a "
               "printed housedress under a soft blue cardigan"},
    # ⚠️ REESCRITA EM 2026-08-13: eram DUAS violacoes na mesma entrada —
    # `sun-weathered skin` e `a thin scar`. Entraram pele levemente bronzeada
    # (mesmo eixo `pele`, lado saudavel) e a mecha branca na sobrancelha, que
    # ancora o rosto igual e nao e' ferida.
    {"idade": 57,
     "payoff": "with broad shoulders and lightly tanned skin, her hair in a "
               "high messy topknot and a bright white streak through her "
               "right eyebrow, in a moss green shirt dress with the sleeves "
               "rolled up"},
    {"idade": 63,
     "payoff": "with a short, round frame, hair dyed flat dark brown under a "
               "blunt fringe, half-moon reading glasses low on her nose and "
               "a raised mole on her chin, in a camel knit twinset and a "
               "single strand of pearls"},
    # ⚠️ REESCRITA EM 2026-08-13: a ancora era `a wide gap between her front
    # teeth`. Falha entre os dentes esta' na lista de PROIBIDO do operador
    # (*"melhore a aparencia e shape desses homens"* vale para o casal inteiro
    # do payoff — e' o quadro do FINAL FELIZ, o unico do video em que alguem
    # sorri). Entrou a covinha, que ancora igual e nao deteriora. ⛔ E ela era
    # a UNICA entrada do pool que casava com o `_DENTE` — se um dia este pool
    # entrar na varredura de dente do autoteste, ele ja' passa limpo.
    {"idade": 64,
     "payoff": "with a heavy-set frame, a shaggy shoulder-length "
               "gray-and-black cut, sunglasses pushed up on her head and a "
               "deep dimple in her right cheek, in an orange tunic top and "
               "white capri pants"},
    {"idade": 65,
     "payoff": "with a tall, narrow build, a long face and thick freckles "
               "across her nose, fine silver hair swept back into a "
               "tortoiseshell comb and a chunky amber ring, in a gray "
               "sweater and a long denim skirt"},
    {"idade": 53,
     "payoff": "with a wiry, broad-shouldered build and deep laugh lines "
               "around her mouth, short spiky ash-blond hair growing out at "
               "the roots, thick red-framed glasses and a beauty mark at the "
               "corner of her mouth, in a checked blue-and-white blouse and "
               "dark jeans"},
    # ======================================================================
    # + 2026-08-13: 16 -> 24. Ordem do operador: *"melhore a aparencia e shape
    # desses homens"* / *"aumente o pool de opcoes substancialmente"*.
    # ⭐ ESTA E' A MULHER DO PAYOFF — o unico quadro do video em que alguem
    # esta' feliz. Por isso as oito novas empurram para o lado SAUDAVEL da
    # tabela (§REF, DISTINTIVO NUNCA DETERIORADO): sarda, covinha, pinta,
    # mecha branca, argola, pele lisa, linhas de riso. ⛔ Zero cicatriz, zero
    # falha de dente, zero `sun-weathered`/`deeply lined`/`liver-spotted` —
    # a mulher que ri no colo dele nao pode parecer castigada, senao o payoff
    # vira consolo em vez de premio.
    # ⭐ Os eixos que giram aqui, e cada nova aciona pelo menos tres: PORTE
    # (`\w+ frame`/`\w+ build`), CABELO, OCULOS (3 das 8 — o pool fica em 7/24,
    # ~29%), PELE saudavel (freckled, smooth-skinned, lightly tanned, laugh
    # lines) e ANCORA facial permanente (P6), sempre em ponto diferente.
    # ⛔ Zero `big`/`huge`: o payoff aterrissa na IMAGE 04 e o BANIDOS_IMAGE
    # deste motor pega `big(?!-box)`.
    # ⛔ Zero mencao a etnia: o motor injeta ETNIA[pagina] antes do payoff.
    # ⚠️ O `payoff` entra em "A %d-year-old %s woman %s sits sideways on his
    # knee" — comeca em `with ` e termina no traje, como as dezesseis acima.
    # ======================================================================
    {"idade": 54,
     "payoff": "with a trim build and smooth-skinned cheeks, dark hair in a "
               "blunt shoulder-length cut with a bright silver streak at the "
               "left temple, and a small mole above her right eyebrow, in a "
               "sleeveless navy shift dress"},
    {"idade": 60,
     "payoff": "with a soft round frame and a light spray of freckles across "
               "her nose, copper hair set in loose curls, and gold hoop "
               "earrings, in a butter yellow blouse and a long floral skirt"},
    {"idade": 57,
     "payoff": "with broad shoulders and a long neck, thick black hair "
               "twisted up and pinned with a wooden clip, thin gold-rimmed "
               "glasses and a beauty mark beside her left eye, in a teal wrap "
               "dress"},
    {"idade": 62,
     "payoff": "with a small, slight build and laugh lines at the corners of "
               "her eyes, fine silver hair cut in a soft pixie, and a pearl "
               "stud in each earlobe, in a rose linen blouse and cream "
               "trousers"},
    {"idade": 55,
     "payoff": "with a tall, narrow build and lightly tanned skin, "
               "honey-brown hair falling loose to her shoulders, and a deep "
               "dimple in her left cheek, in a sage green sundress"},
    {"idade": 65,
     "payoff": "with a stout frame and a wide open face, white hair in a "
               "short permed set, oval reading glasses on a thin gold chain "
               "and a raised mole on her right jaw, in a lilac cardigan over "
               "a white blouse"},
    {"idade": 58,
     "payoff": "with a compact build and freckled forearms, auburn hair in a "
               "low ponytail with gray coming in at the part, and a shallow "
               "cleft in her chin, in a denim shirt dress and a leather belt"},
    {"idade": 63,
     "payoff": "with a full-figured frame and smooth-skinned hands, "
               "salt-and-pepper hair in a chin-length bob, thick "
               "tortoiseshell glasses pushed up on her head and a dark beauty "
               "mark under her left eye, in a burgundy knit top and black "
               "trousers"},
]

# prop do payoff (cena 4) — F15: ja' ereto no IMAGE, dimensionado por escala
PROPS = [
    {"id": "banana", "marisco": False,
     "ereto": "a banana upright at shoulder height, held stiff and straight, "
              "as long as her forearm and as thick as her wrist"},
    {"id": "geoduck", "marisco": True,
     "ereto": "a geoduck clam upright by its shell at shoulder height, its siphon "
              "held stiff and straight, as long as her forearm and as thick as her wrist"},
    {"id": "pepino", "marisco": False,
     "ereto": "a cucumber upright at shoulder height, held stiff and straight, "
              "as long as her forearm and as thick as her wrist"},
    {"id": "daikon", "marisco": False,
     "ereto": "a daikon radish upright at shoulder height, held stiff and straight, "
              "as long as her forearm and as thick as her wrist"},
    # + 2026-08-01: o operador mediu vicio — o mesmo prop no payoff em todo
    # lote. Mais dois, mesma escala.
    {"id": "baguete", "marisco": False,
     "ereto": "a French baguette upright at shoulder height, held stiff and "
              "straight, as long as her forearm and as thick as her wrist"},
    {"id": "salame", "marisco": False,
     "ereto": "a whole dry-cured salami upright at shoulder height, held stiff "
              "and straight, as long as her forearm and as thick as her wrist"},
]

# ---------------------------------------------------------------------------
# POOLS DE COPY
# ---------------------------------------------------------------------------

# ⭐⭐ 2026-08-10 — CONTRATO DE COPY 16s, CT4. O apelido do orgao e' UM SO' por
# video e volta nos DOIS takes; a variacao mora ENTRE videos, que e' onde ela
# nunca custou nada. Duas consequencias nesta lista:
#   · ⛔ `soldier` APOSENTADO. Em boca americana de 50-70 anos `soldier` para o
#     orgao soa a filme de guerra — britanismo. Entraram no lugar `manhood` e
#     `equipment`, que o ouvido do avatar reconhece e que o `medir_deiticos` /
#     `medir_contexto_copy` ja' listam no regex ORGAO (apelido fora daquele
#     regex viraria falso positivo de "cena orfa" nos dois medidores).
#   · ⛔ TODA ENTRADA TEM UMA PALAVRA SO'. O take 2 fecha em 25 palavras com
#     quatro batidas (9+5+3+8); um apelido de duas palavras (`old boy`)
#     estouraria o teto e mataria por filtro as entradas mais longas de cada
#     pool — a armadilha de orcamento do §4 do contrato.
# Pool de 5 -> 6 entradas: nenhuma perda de entropia na troca.
NUCLEO = ["Johnson", "pecker", "wiener", "tool", "manhood", "equipment"]

# PE6 ⭐ — a regra mais importante do agente. O hook LIGA o mijo ao orgao NA
# MESMA FALA. Hook so' de mijo REPROVA: o homem com ED nao se reconhece, acha
# que o assunto e' bexiga e rola. Estrutura obrigatoria:
#   fato do mijo + aparte + orgao nomeado + VINCULO afirmado
VINCULOS = ["same thing", "same reason", "and that's why"]

# ⭐⭐ POOL REESCRITO EM 2026-08-10 — CT2 do CONTRATO DE COPY 16s.
# Medido antes: 31% dos sorteios nao tinham NENHUMA sentenca dizendo o que o
# corpo dele faz de errado. `took his {o}`, `does nothing`, `stopped answering`
# e `shut his {o} down` (com o objeto no meio) descrevem dano nenhum que o
# espectador reconheca como o SEU — e sem auto-reconhecimento nao ha'
# comentario: ele nao comenta porque a copy e' boa, comenta porque se viu.
#
# ⛔ O MOLDE, e agora ele e' o mesmo nas 22 entradas:
#     <mijo em {evento}> · <dano social curto> · <VINCULO> · his {o} + FALHA + NUMERO
# A melhor linha ja' medida do parque inteiro e' a entrada 1 deste pool,
# `hasn't worked in two years` — cinco palavras, um numero, um dano.
#
# ⛔ AS DUAS ENTRADAS EM PRIMEIRA PESSOA FORAM APOSENTADAS (`That was me in
# 2019`, `I did the same in 2019`) e substituidas por duas de terceira pessoa.
# Motivo: o take 2 agora prova no HOMEM DA CENA 1 (`That man's {o} answered
# her.`), e com um hook em primeira pessoa esse `that man` passava a apontar
# para o proprio narrador — deitico com dois donos. Entropia preservada: o pool
# saiu de 20 para 22 entradas.
#
# ⚠️ Tamanhos parelhos DE PROPOSITO (18-23 palavras, teto 24): entrada curta
# demais num pool de teto apertado e' entrada que domina o lote (§4).
HOOKS = [
    # ⛔ `He lost it right there` -> `He wet himself right there` (2026-08-10,
    # conferencia da reforma). Mesma contagem de palavras, e nada mais mudou.
    # Motivo: em boca americana `he lost it` significa PRIMEIRO perder a cabeca
    # / desabar em choro, e a IMAGEM DESTE ANGULO RATIFICA JUSTAMENTE ESSA
    # leitura errada — o CHORO_IMAGE obriga o homem a estar chorando muito,
    # lagrimas nas duas bochechas, ombros tremendo. E' a colisao "ouvido B" que
    # este mesmo arquivo ja' documenta no `_hook_sem_colisao`: nao e' um absurdo
    # que o ouvido descarta em 200ms, e' uma SEGUNDA HISTORIA COMPLETA (o homem
    # desabou chorando na loja). ⚠️ O `_pe6_hook` aceitava `lost it` como "o
    # hook diz o mijo" — passe FALSO: o token esta' na lista, mas a sentenca
    # nao diz mijo nenhum para quem ouve uma vez so'.
    "He wet himself right there in {evento}. Poor guy... and that's why his {o} hasn't worked in two years.",
    "He wet his pants in {evento} and everybody saw. Same reason his {o} quit on him two years ago.",
    "He soaked right through in {evento}. Same thing that made him leak stopped his {o} cold two years back.",
    "He peed himself in {evento} because he couldn't hold it. Same thing killed his {o} two years ago.",
    "He wet his pants in {evento}. His wife wasn't surprised. Same reason his {o} stopped working two years back.",
    "He peed his pants in {evento}. His brother in law still tells it. Same reason his {o} quit two years ago.",
    "He soaked his pants in {evento}. His wife quit reaching for him. Same reason his {o} went out two years ago.",
    # ⛔ `She said it was fine` -> `His wife called it fine` (2026-08-10). Mesma
    # contagem de palavras (5 por 5), e a segunda frase (`She says that in bed
    # too.`) fica intacta — ela e' a melhor linha do pool e agora tem dono.
    # Motivo: esta era a UNICA entrada do pool que ABRIA o video inteiro num
    # pronome sem referente. As outras 21 abrem em `He` / `A grown man` / `They`,
    # e ali o referente esta' NO QUADRO — o homem de calca molhada. Uma mulher
    # nao esta': o `MAPA` deste 16s e' `(1, 3)` e nenhum dos dois quadros tem
    # mulher. `She said it was fine` era `she` sem dono nem em fala nem em
    # imagem, na primeira meia-segunda do video (lei `pronome-generico-e-drifting`).
    "His wife called it fine when he peed in {evento}. She says that in bed too. Same reason his {o} quit.",
    "He leaked down his leg in {evento}. Hasn't asked anybody out since. Same reason his {o} gave out two years ago.",
    "He started leaking in {evento}. His wife already told her friends. Same reason his {o} hasn't worked in two years.",
    # + 2026-08-01: o operador mediu vicio — os mesmos hooks voltando no lote.
    # Pool ampliado; todos mantem mijo + orgao + vinculo na mesma fala (PE6).
    "Everybody laughed when he leaked through his pants in {evento}. Same reason his {o} quit on him two years ago.",
    "A grown man peed himself in {evento} on a Tuesday. Same reason his {o} stopped two years ago.",
    "Know why a man peed himself in {evento}? Same reason his {o} hasn't worked in two years.",
    "His wife walked him out of {evento} soaked. Same reason his {o} quit on her two years ago.",
    "His doctor blamed the coffee when he peed in {evento}. Same thing had already stopped his {o} cold.",
    "They still talk about the man who soaked his pants in {evento}. Same reason his {o} quit two years back.",
    # ⛔ mesma troca de `lost it` da entrada 1 deste pool, mesmo motivo, mesma
    # contagem. ⭐ Esta e' a unica entrada de SENTENCA UNICA do pool — e' ela
    # que o registro do `medir_abertura` (mais abaixo) aponta como o caminho se
    # o operador quiser abertura com referente nomeado.
    "He wet himself standing in {evento}, and that's why his {o} has been dead two years.",
    "He won't be the last man soaked in {evento}. Same thing that stopped his {o} two years ago.",
    "He wet himself in {evento} in front of his grandson. Same reason his {o} gave out two years ago.",
    "He soaked his pants in {evento} and walked out fast. Same reason his {o} quit on him years ago.",
    # + 2026-08-10: as duas que entram no lugar das de primeira pessoa.
    "Two women in {evento} laughed at his wet pants. Same reason his {o} quit two years ago.",
    "He peed through his pants in {evento} at sixty three. Same reason his {o} gave out first.",
]

# PE7 — a cena 2 EXPLICA o vinculo que o hook afirmou. Uma causa, dois sintomas.
MECANISMOS = [
    "It's his prostate squeezing the pipe shut. Same pressure keeps the blood out of your {o}.",
    "His prostate is clamping down on the pipe. That same pressure is what starves your {o}.",
    "It's the prostate choking the line. The same squeeze is why your {o} can't fill anymore.",
    # ⭐ 2026-08-03 — FRASE ORFA. O operador leu um take pronto e reprovou:
    # "It isn't age. The blood flow got choked off." -> "deveria ser it isn't
    # age QUE ESTA' CAUSANDO seu John-son nao funcionar mais. Voce tem que
    # contextualizar mais as coisas. Ta' deixando o viewer sem entender o
    # contexto e do que se trata."
    # REGRA NOVA: toda frase que nomeia uma CAUSA carrega, NA MESMA FRASE, o
    # que ela quebra. Nao vale o orgao aparecer "em algum lugar da cena" — a
    # cena reprovada tinha o orgao na ultima frase. Aqui "It's not his age."
    # era a unica frase orfa do motor inteiro (medido: 14 de 14 renderizacoes
    # orfas vinham desta entrada). O alvo entrou NELA, em TERCEIRA PESSOA,
    # porque a frase fala do homem da historia — a pessoa que a frase ja' usa
    # e' a que se mantem (`his {o}` aqui, `your {o}` na frase de fechamento).
    # ⛔ Teto da cena 2 = 26 palavras. O objeto engordou a entrada em 5, entao
    # a ultima frase foi comprimida na mesma entrada ("is why no blood gets to
    # your {o}" -> "starves your {o} of blood"): 24 palavras com nucleo de uma
    # palavra, 26 no pior caso ("old boy", que conta 2). Nada de subir o teto.
    "It's not his age that shut his {o} down. His prostate swelled up and pinched the pipe. Same pinch starves your {o} of blood.",
    "Pills don't touch this. It's his prostate pressing the line flat, and that same press is why your {o} can't fill.",
    "They never told him why, because a fixed man buys nothing. His prostate is sitting on that pipe and shutting your {o} down.",
    "Picture a boot standing on a garden hose. That's his prostate on the line, and it's why your {o} won't fill.",
    "The dripping came first. That's his prostate closing the pipe, and it closes on your {o} a year or two later.",
    "His doctor treated the bladder and never mentioned the rest. Same prostate pressing the same pipe is what took your {o} down.",
    "Blood doesn't reach your {o} anymore. It's the same prostate pinching the same line that sends him to the bathroom all night.",
    "They'll call it two different problems. It's one. His prostate is on the pipe, and that's why your {o} stays down.",
    "I know this one. My prostate grew over the line and closed it. I leaked. Then my {o} went half. Then nothing.",
    "Us guys all have the same prostate leaning on the same line. That's why we drip, and that's why our {o} sleeps through it.",
    # + 2026-08-01: o operador mediu vicio — a mesma explicacao da cena 2 em
    # todo lote. Pool ampliado; uma causa, dois sintomas continua de pe (PE7).
    "Every man's prostate grows after fifty. It closes the pipe first and your {o} second.",
    "If you get up twice a night, your prostate is already on the line and your {o} knows it.",
    "One gland, two failures. His prostate shut the pipe, and that left your {o} with nothing.",
    "The night trips to the bathroom and the dead {o} are the same problem. His prostate on the pipe.",
]

RITUAIS = [
    "That's when his brother gave him the gelatin trick. He stirred it into a glass that same night. Give your {o} one week.",
    "That's when a buddy handed him the gelatin trick. He drank it that same night. Stir it, drink it, and watch your {o} wake up.",
    "That's when his son-in-law gave him the gelatin trick. He mixed it into a glass that night. Do it before your {o} quits for good.",
    "A guy at the barbershop gave him the gelatin trick. He stirred a spoonful into cold water before bed. Do it tonight and your {o} answers by Friday.",
    "An old army buddy called him that night with the gelatin trick. One spoon, warm water, stirred slow. Do the same tonight and give your {o} nine days.",
    "His fishing partner gave him the gelatin trick. He mixed it in the kitchen that same night. Give your {o} two weeks and stop saying sorry in the dark.",
    "His nephew texted him the gelatin trick. He mixed a spoonful into his morning drink. Do the same and your {o} wakes up before you do.",
    "I found the gelatin trick in 2019, brother. I stirred one spoon into cold water that night. Nine days later my {o} answered.",
    "The gelatin trick is what we do at home now. A spoonful in half a glass of cold water. Your {o} shows up before the weekend.",
    # + 2026-08-01: o operador mediu vicio — o mesmo ritual em todo lote. Pool
    # ampliado; o literal `gelatin trick` continua obrigatorio em cada item.
    "The pharmacist's husband told him about the gelatin trick. He stirred it into a mug before bed. Give your {o} ten days.",
    "His neighbor slid him a note with the gelatin trick on it. One spoon in cold water, every night. Your {o} answers by the weekend.",
    "Nobody at the clinic told him. A retired trucker did, with the gelatin trick, one spoon, cold water. Start tonight for your {o}.",
    "He laughed at the gelatin trick when his cousin sent it. He stirred a spoonful in anyway. Nine days for your {o}.",
]

BARREIRAS = [
    "Nobody has to know but her.",
    "No doctor, no pharmacy counter.",
    "You do it in your own kitchen, in about a minute.",
    "Costs less than a cup of coffee.",
    "You never say the words out loud to anybody.",
    # + 2026-08-01: o operador mediu vicio — a mesma barreira fechando a cena 4.
    # Pool ampliado.
    "One spoon, one glass, one minute.",
    "You can do it before she wakes up.",
    "No appointment, no waiting room, no forms.",
    "She finds out when it works, not before.",
]

# F1 — o eco deste angulo: ele volta ao mesmo lugar SECO e de cabeca erguida
REDENCOES = [
    "Nineteen days later he walked back into {eco} dry, head up. Now she's the one bragging about his {o}. {barreira}",
    "Nineteen days later he was back in {eco}, dry and standing tall. Now she won't stop talking about his {o}. {barreira}",
    "Twenty six days later he was back in {eco} dry, head high. She says his {o} wakes up before the alarm. {barreira}",
    "Sixteen days later he walked into {eco} dry, head up. His {o} left her needing a minute to catch her breath. {barreira}",
    "Eighteen days later he was back in {eco} dry, chin up. She reaches for him first now. His {o} never quits. {barreira}",
    "Twenty four days later he walked into {eco} dry, head up. Now she asks for a night off from his {o}. {barreira}",
    # + 2026-08-01: o operador mediu vicio — a mesma redencao em todo lote. Pool
    # ampliado; o eco (ele de volta ao mesmo lugar, seco) continua travado (F1).
    "He goes back to {eco} every week now, dry. She brags about his {o} to her sister. {barreira}",
    "Three weeks. He stood in {eco} dry, and she couldn't keep her hands off his {o}. {barreira}",
    "The same people who laughed at him in {eco} watched him walk out dry. His {o} is back. {barreira}",
    "Now he walks into {eco} alone and dry. His wife says his {o} never quits. {barreira}",
]

GATES = [
    "Follow me first, brother.",
    "Follow me first or I can't find your comment.",
    "Hit follow first, or Facebook won't deliver it.",
    # + 2026-08-01: o operador mediu vicio — "brother" saia em todo CTA do lote.
    # ⛔ REGRA NOVA: no maximo 2 entradas com o vocativo "brother" no pool
    # inteiro, e a MAIORIA das entradas sem vocativo nenhum. Quando adicionar
    # gate novo, conferir a contagem antes.
    "Follow first. I can't message a stranger.",
    "Hit follow, or this never reaches you again.",
    "Follow first. Those comments get answered first.",
    "Two hundred comments a day, man. Follow first.",
    "Tap follow, then comment. Otherwise it gets buried.",
    "Follow me before you comment, my friend.",
    "Follow first, or my inbox stays shut.",
    "Follow me first, buddy. Takes one second.",
]

CTAS = [
    # ⭐ Alternativa pedida pelo operador em 2026-07-31, vista em campo:
    # a promessa e' A RECEITA, nao "o que eu uso" nem "onde eu compro".
    # E' a mais direta do pool e a unica que casa com a keyword RECIPE
    # que o Veo Editor ja' destaca na legenda.
    "Comment gelatin, and I'll send you the recipe tonight. {gate}",
    "Comment gelatin, and I'll send you the only one I trust tonight. {gate}",
    "Comment gelatin, and I'll send you that exact one today. {gate}",
    "Comment gelatin, and I'll send you where to get the right one. {gate}",
    "Comment gelatin, and thank me Friday night. I'll send it over today. {gate}",
    "Comment gelatin, and tonight — somebody always reports this. I'll send the recipe before it goes down. {gate}",
    "One word. Comment gelatin, and it's in your inbox tonight. {gate}",
    "Comment gelatin, and I'll send you the source. I can't name it here. {gate}",
    "Comment gelatin, and I'll send the same one he used. {gate}",
    "Comment gelatin, and I'll send you the real one. The store stuff did nothing for you. {gate}",
    "Comment gelatin, and I'll send you the one we use at home. {gate}",
    # + 2026-08-01: o operador mediu vicio — o mesmo CTA repetindo no lote.
    # Pool ampliado; a keyword GELATIN continua travada em todas.
    "Comment gelatin, and I'll send it before I turn in tonight. {gate}",
    "Comment gelatin, and I'll send the recipe. Your wife never has to know you asked. {gate}",
    "You already know. Comment gelatin, and the recipe is in your messages tonight. {gate}",
    "Don't overthink it. Comment gelatin, and I'll send you the recipe. {gate}",
]

# ---------------------------------------------------------------------------
# LINTER
# ---------------------------------------------------------------------------

BANIDOS_TAKE = {
    "stiff": "adjetivo de estado em prompt de movimento derruba o video",
    "limp": "idem", "sags": "idem",
    "pulse": "tumescencia — IMAGE passa e o VIDEO e' recusado",
    "throb": "idem", "swelling": "idem",
    "engorged": "vocabulario anatomico — recusa",
    "geoduck": "so' no IMAGE; no TAKE usar 'the clam'",
    "neck": "no geoduck e' 'siphon', nunca 'neck'",
}
BANIDOS_IMAGE = {
    # 'big(?!-box)': o banimento e' de DIMENSAO de prop. Sem o lookahead, o
    # cenario 'big-box supermarket' era acusado em todo sorteio do local mercado.
    "big(?!-box)": "adjetivo nao dimensiona — o Veo normaliza",
    "huge": "idem", "engorged": "vocabulario anatomico — recusa", "veins": "idem",
}

BANIDOS_GLOBAL = {
    "the victim": "rotulo que significa dano — municao pro classificador",
    "the narrator": "trocar por relacao nomeada",
}
BANIDOS_CTA = {"BOOK": "quebra a automacao DM", "YES": "quebra a automacao DM"}

# roupa escura mata o hook (PE1) — o pool ja' impede, o linter e' rede
ROUPA_ESCURA = ["dark jeans", "black pants", "navy trousers", "dark trousers",
                "black shorts", "dark slacks"]

# ⚠️ 2026-08-03: chamava-se `TETO_FALA` no `pee_lucas.py`. Renomeado ao ser
# inlineado porque este modulo ja' tem um `TETO_FALA` proprio, de 3 cenas. Este
# aqui e' o do ARCO LONGO de 5 cenas, e serve para as PONTAS do SHORT herdarem
# o teto das cenas 1 e 5 (ver o `TETO_FALA` deste arquivo, mais abaixo).
TETO_FALA_LONGO = {1: 24, 2: 26, 3: 30, 4: 36, 5: 24}


def _palavras(txt):
    return len(re.findall(r"[A-Za-z']+", txt))


def _evitando(rng, pool, recentes):
    livres = [x for x in pool if x.get("id") not in recentes]
    return rng.choice(livres if livres else pool)


# 3 dos 20 hooks matam o orgao com verbo literal (`killed his {o}`, `has been
# dead two years`, `plays dead`). Dois dos 7 substantivos do NUCLEO sao ANIMADOS
# (`old boy`, `soldier`) — e o cruzamento dos dois nao produz um absurdo que o
# ouvido descarta em 200ms, produz UMA SEGUNDA HISTORIA COMPLETA:
#
#   ouvido A (certo) : ele se mijou, e por isso o orgao esta' morto ha' 2 anos
#   ouvido B (errado): ele desabou em prantos na loja porque o FILHO / o CACHORRO
#                      morreu ha' dois anos
#
# E a leitura B e' a que a IMAGEM ratifica: a cena 1 OBRIGA o homem a estar
# chorando muito, lagrimas nas duas bochechas, ombros tremendo (CHORO_IMAGE /
# PE2). Nas outras entradas a imagem paga a conta; nestas ela paga a conta
# errada. Achado na auditoria de drifting de 2026-08-01.
#
# ⛔ Corrigido no SORTEIO, nao no pool: os 3 hooks e os 7 substantivos sao copy
# validada e nenhum foi redigitado. Resolve as tres entradas de uma vez.
# ⛔ APOSENTADA NA PRATICA EM 2026-08-10, e a aposentadoria e' declarada. O
# unico membro VIVO desta tupla era `soldier`, e ele saiu do NUCLEO na reforma
# do CONTRATO DE COPY 16s (britanismo — ver a nota do NUCLEO). Com o pool atual
# (`Johnson`, `pecker`, `wiener`, `tool`, `manhood`, `equipment`) nenhum
# substantivo e' ANIMADO, entao a colisao "ouvido B" (o filho/o cachorro morreu)
# nao tem mais como nascer e o guarda abaixo passa direto em todo sorteio.
# ⚠️ A funcao NAO foi apagada: ela e' a rede do dia em que alguem devolver um
# apelido animado ao pool (`old boy` e' o candidato obvio). Regra que some sem
# explicacao o repo trata como divida.
NUCLEO_ANIMADO = ("old boy", "soldier")
_MORTE = ("killed", "dead", "plays dead")


def _hook_sem_colisao(rng, orgaos, tentativas=12):
    """Um hook que nao mate um substantivo animado do nucleo."""
    for _ in range(tentativas):
        h = rng.choice(HOOKS)
        if not (orgaos[0] in NUCLEO_ANIMADO
                and any(m in h for m in _MORTE)):
            return h
    # fallback: com o sorteio travado, prefere-se hook sem verbo de morte
    livres = [h for h in HOOKS if not any(m in h for m in _MORTE)]
    return rng.choice(livres or HOOKS)


def _sortear_longo(pagina, rng, ledger, travas=None):
    # ⛔ A REF DESTE AGENTE SAI AQUI, no motor longo embutido — nao no
    # `sortear` de tres argumentos la' de baixo. Por isso a trava atravessa
    # `sc.sortear_curto` ate' aqui: sem isso o toggle acenderia e nao mudaria
    # nada, que e' o botao que mente.
    # ⛔⛔ A JANELA DO LEDGER SUBIU EM 2026-08-10, e o numero nao e' gosto: e' a
    # metade MECANICA da queixa *"esta repetindo com muita frequencia os mesmos
    # personagens"*. Com 21 locais e janela 3, a chance de o mesmo lugar voltar
    # dentro de quatro videos era de 1 em 6; com janela 6 ela e' zero por
    # construcao — o `_evitando` simplesmente nao pode sortear o que esta' la'.
    # ⚠️ A janela nunca pode encostar no tamanho do pool: com `livres` vazio o
    # `_evitando` cai no pool inteiro e a memoria vira enfeite. As tres janelas
    # abaixo estao em ~1/3 do respectivo pool, e o autoteste cobra essa folga.
    hist = ledger.get(pagina, {})
    local = _evitando(rng, LOCAIS, hist.get("local", [])[-6:])
    roupa = _evitando(rng, ROUPAS, hist.get("roupa", [])[-3:])
    amb = _evitando(rng, AMBIENTES, hist.get("ambiente", [])[-3:])
    prop = _evitando(rng, PROPS, hist.get("prop", [])[-2:])
    # ⭐ MODOS DE REF: a REF e' o narrador (homem) e a MULHER e' quem aparece
    # no payoff. Cada um leva o seu modo.
    _tv = travas or {}
    # ⛔⛔ O NARRADOR E A VITIMA ENTRARAM NO LEDGER EM 2026-08-10. Ate' hoje as
    # duas linhas eram `rng.choice(...)` CRU — os dois unicos rostos do video
    # eram os dois unicos eixos SEM MEMORIA NENHUMA no motor inteiro, enquanto
    # local, roupa, ambiente e prop tinham. Por isso o operador via a mesma
    # dupla em lotes seguidos mesmo depois de duas ampliacoes de pool: o
    # problema nunca foi so' quantas entradas existiam, era que o sorteio nao
    # lembrava de nada. Pool grande com sorteio sem memoria repete igual.
    # ⚠️ O MODO FORTE continua passando por fora — ele nao sai do `REFS`, entao
    # nao ha' historico a evitar. O `_gravar_ledger` grava o `id` que vier
    # (`forte_<idade>`), e ele nunca colide com um id do pool.
    ref = (sc.ref_forte(REFS[0], rng) if _tv.get("forte")
           else _evitando(rng, REFS, hist.get("ref", [])[-8:]))
    vit = _evitando(rng, VITIMAS, hist.get("vitima", [])[-6:])
    mul = (sc.ref_bela(MULHERES[0], rng) if _tv.get("bela")
           else rng.choice(MULHERES))

    # ⛔⛔ CT4b (2026-08-10) — SO' TRES APELIDOS SAO SORTEAVEIS.
    # Ordem do operador: *"quero que vc use weiner e john-son pra se referir ao
    # orgao tb, nao apenas pec-ker"*. `soldier` soa filme de guerra para ouvido
    # americano e `tool` e' ambiguo em giria dos EUA; os dois seguem no NUCLEO
    # porque as LENTES os usam para DETECTAR o orgao — o que muda e' que nao
    # sao mais sorteaveis. O CT4 trava UM apelido por video; sem isto aqui, um
    # apelido por video vira o MESMO apelido no lote inteiro.
    _o1 = rng.choice(sc.APELIDOS_16)
    orgaos = [_o1] * 4
    hook = _hook_sem_colisao(rng, orgaos)
    falas = [
        hook.format(evento=_aqui(local["plateia_evento"]), o=orgaos[0]),
        rng.choice(MECANISMOS).format(o=orgaos[1]),
        rng.choice(RITUAIS).format(o=orgaos[2]),
        rng.choice(REDENCOES).format(eco=local["eco"], o=orgaos[3],
                                     barreira=rng.choice(BARREIRAS)),
        rng.choice(CTAS).format(gate=rng.choice(GATES)),
    ]
    return {"pagina": pagina, "local": local, "roupa": roupa, "ambiente": amb,
            "prop": prop, "ref": ref, "vitima": vit, "mulher": mul,
            "mancha": MANCHA[0], "falas": falas}


def _montar_longo(spec):
    et = ETNIA[spec["pagina"]]
    ref, vit, mul = spec["ref"], spec["vitima"], spec["mulher"]
    prop, loc, amb, roupa = spec["prop"], spec["local"], spec["ambiente"], spec["roupa"]
    falas = spec["falas"]
    luz = amb["luz"]
    neg = NEGACAO_AVE if prop["marisco"] else ""
    mancha = spec["mancha"].format(peca=roupa["peca"])

    b = {}

    # O cabecalho REF faz parte do bloco, igual ao "IMAGE 01/05:" dos outros.
    # E o que o parser do AdBatch usa para mandar este bloco para o painel
    # Consistencia Visual em vez de tentar encaixa-lo num slot da grade.
    # ⛔ Nao remover: sem ele a referencia e descartada em silencio.
    b["BLOCO 0 (REF)"] = (
        # ⛔⛔ 2026-08-10 — `Lean muscular build` ENTREGAVA MAGRO. Relato de
        # campo do operador com o render na mao: o narrador saia franzino, sem
        # o porte que o angulo pede. O Veo le' `lean` primeiro e o resto vira
        # detalhe — mesma licao do CL25 com os dentes e do EX9 com `beautiful`:
        # adjetivo generico perde para a palavra concreta que vem antes.
        # ⭐ Agora e' o padrao do CLEAN V1, que ele pediu nominalmente: nada de
        # `lean`, e o corpo e' descrito pelo QUE ELE FAZ (`a man who lifts`),
        # nao por um adjetivo de forma.
                # ⛔⛔ CL25 — O REF SORRI MOSTRANDO OS DENTES. Relato de campo do
        # operador, 2026-08-10: *"os dentes do narrador estao pessimos, parece
        # que estao podres ou que estao prestes a cair"*.
        # A REF dizia so' `calm expression` — boca fechada. Sem dentes na
        # imagem de identidade o Veo INVENTA a dentadura quando a boca abre no
        # take, e inventa mal. E' a mesma licao que o CLEAN pagou em
        # 2026-08-04 e resolveu com esta linha; aqui ela faltava.
        # ⚠️ A ancora e' POSITIVA e vai na REF, nao no TAKE: o take herda o
        # rosto do primeiro frame, entao e' o frame que precisa ter a boca
        # certa. Descrever dente no TAKE chega tarde.
        # ⛔⛔ 2026-08-10 — `a wide warm natural smile` VIROU `a natural smile`.
        # Nao e' economia de palavra: `wide warm smile` + `senhor grisalho` +
        # `plain gray background` e' a receita literal do retrato de estudio
        # que o operador reconheceu no lote. Os TRES literais que a lente CL25
        # cobra continuam intactos (`natural smile`, `clean white teeth`,
        # `even, white and complete`) — o que saiu foram os dois adjetivos que
        # nao descrevem geometria nenhuma e so' empurram para o atrator.
        # ⛔ E a clausula `not a celebrity` saiu daqui — ver a lapide do
        # `ANTICELEB` no topo do arquivo. Quem separa este rosto de todos os
        # outros agora e' a arquitetura facial que vem no `marca`.
        "REF 01: Photo of a real person, a %d-year-old %s man, chest up, facing camera, "
        "a natural smile with the lips parted, showing a full row of clean white teeth, the front teeth even, white and complete. The dense build of a man who lifts, thick through the "
        "chest and shoulders, forearms corded, skin taut and even. %s. "
        "%s Plain gray background, soft light. No text, no watermark."
        % (ref["idade"], et, ref["marca"].capitalize(), ref["roupa"])
    )

    b["IMAGE 01/05"] = (
        "IMAGE 01/05: Medium shot in %s, %s. Standing in the middle is a "
        "%d-year-old %s %s, wearing %s, with %s. He stands there, %s "
        "Beside him is a %d-year-old %s man with %s, %s, and %s. "
        "%s %s"
        % (loc["cenario"], loc["detalhe"], vit["idade"], et, vit["marca"],
           vit["camisa"], mancha, CHORO_IMAGE,
           ref["idade"], et, ref["marca"], NARRADOR_IMAGE,
           PLATEIA_IMAGE % loc["plateia"], loc["luz"], CAUDA)
    )

    b["IMAGE 02/05"] = (
        "IMAGE 02/05: Medium close-up in %s. The same %d-year-old %s man, %s, "
        "%s, stands behind the %s, leaning slightly toward the camera, mouth "
        "open mid-word. %s He is alone in frame. %s %s"
        % (amb["set"], ref["idade"], et, ref["marca"], ref["roupa_curta"],
           amb["bancada"], D1_IMAGE, luz.capitalize(), CAUDA)
    )

    b["IMAGE 03/05"] = (
        "IMAGE 03/05: Close insert shot, same %s, %s A pair of hands tears open "
        "a small white sachet and pours powder into a glass of water, a spoon "
        "beside it. No face in frame. %s" % (amb["bancada"], luz, CAUDA)
    )

    b["IMAGE 04/05"] = (
        "IMAGE 04/05: Medium shot in a plain living room, %s The same "
        "%d-year-old %s %s, now in a clean white shirt and dry trousers, sits in "
        "an armchair grinning, head up, a total reversal of his bowed posture in "
        "the store. A %d-year-old %s woman %s sits sideways on his knee, the way "
        "a newlywed poses for a photograph, arm around him, laughing. In her free "
        "hand she holds %s.%s %s"
        % (luz, vit["idade"], et, vit["marca"], mul["idade"], et,
           mul["payoff"], prop["ereto"], neg, CAUDA)
    )

    b["IMAGE 05/05"] = (
        "IMAGE 05/05: Close-up in the same %s, %s The same %d-year-old %s man, "
        "%s, alone, looking at camera with a confident half-smile, finger "
        "pointing at the lens. %s"
        % (amb["curto"], luz, ref["idade"], et, ref["marca"], CAUDA)
    )

    b["TAKE 01/05"] = (
        "TAKE 01/05: Animate the image exactly. Handheld iPhone, slight sway, no "
        "cuts. %s The standing man does not move from where he is — %s Behind "
        "them the blurred %s keep laughing, two still pointing. Only the "
        "crouching man speaks.\nDialogue: \"%s\"\nAudio: %s No music."
        % (NARRADOR_TAKE, CHORO_TAKE, loc["plateia"], sonorizar(falas[0]), loc["audio"])
    )

    b["TAKE 02/05"] = (
        "TAKE 02/05: Animate the image exactly. Handheld iPhone, slight sway, no "
        "cuts. %s He is alone in frame, speaking with conviction.\n"
        "Dialogue: \"%s\"\nAudio: quiet room tone. No music." % (D1_TAKE, sonorizar(falas[1]))
    )

    b["TAKE 03/05"] = (
        "TAKE 03/05: Animate the image exactly. Handheld iPhone, slight sway, no "
        "cuts. Hands finish pouring the sachet, stir the glass in slow circles. "
        "No face enters frame.\nDialogue: \"%s\"\n"
        "Audio: spoon clinking glass, quiet room tone. No music." % sonorizar(falas[2])
    )

    b["TAKE 04/05"] = (
        "TAKE 04/05: Animate the image exactly. Handheld iPhone, slight sway, no "
        "cuts. The man laughs silently, head tipping back. The woman laughs, "
        "tightens her arm around him; her other hand stays exactly where it is, "
        "holding it motionless the entire shot. Neither changes position. A man's "
        "voice speaks over the scene; the couple stays silent.\n"
        "Dialogue: \"%s\"\nAudio: quiet room tone, soft laughter. No music." % sonorizar(falas[3])
    )

    b["TAKE 05/05"] = (
        "TAKE 05/05: Animate the image exactly. Handheld iPhone, slight sway, no "
        "cuts. He looks at camera, calm, points his finger, speaks evenly.\n"
        "Dialogue: \"%s\"\nAudio: quiet room tone. No music." % sonorizar(falas[4])
    )

    return b


def _nova_fala_longa(spec, i, rng):
    """Re-sorteia a fala da cena i (0-4) mantendo o substantivo-nucleo daquela cena."""
    o = next((n for n in NUCLEO if n.lower() in spec["falas"][i].lower()), "Johnson")
    loc = spec["local"]
    if i == 0:
        return rng.choice(HOOKS).format(evento=_aqui(loc["plateia_evento"]),
                                    o=o)
    if i == 1:
        return rng.choice(MECANISMOS).format(o=o)
    if i == 2:
        return rng.choice(RITUAIS).format(o=o)
    if i == 3:
        return rng.choice(REDENCOES).format(eco=loc["eco"], o=o,
                                            barreira=rng.choice(BARREIRAS))
    return rng.choice(CTAS).format(gate=rng.choice(GATES))


EIXOS_UI = [
    ("local", "LOCAL", "LOCAIS", "id"),
    ("roupa", "ROUPA", "ROUPAS", "peca"),
    ("ambiente", "AMBIENTE", "AMBIENTES", "id"),
    ("prop", "PROP CENA 4", "PROPS", "id"),
    # ⛔ O ROTULO DOS DOIS ROSTOS PASSOU DE `marca` PARA `id` EM 2026-08-10, e
    # e' consequencia direta da reforma dos pools: o `marca` era `full silver
    # hair and a notched left ear` (8 palavras) e virou a arquitetura facial
    # inteira (~30 palavras). O painel desenha esse texto numa LINHA, ao lado
    # do rotulo do eixo — com a marca nova a linha do NARRADOR sozinha
    # empurraria os outros seis eixos para fora da tela.
    # ⭐ O `id` foi escrito para ser lido pelo operador (`juba_para_tras`,
    # `cranio_quadrado`), e o painel ja' antepoe a idade: `66y · flat_top`.
    # E' a mesma forma que o FIGHT 16 usa (`50y · sal_pimenta`).
    ("ref", "NARRADOR", "REFS", "id"),
    ("vitima", "VÍTIMA", "VITIMAS", "id"),
    ("mulher", "MULHER", "MULHERES", "payoff"),
]

PT_LOCAL = {
    "mercado": "No corredor do mercado", "farmacia": "No corredor da farmácia",
    "fila_caixa": "Na fila do caixa", "ferragens": "Na loja de ferragens",
    "hortifruti": "No hortifrúti", "conveniencia": "Na loja de conveniência",
    # + 2026-08-01: rotulos dos locais novos do lote desta data.
    "feira": "Na feira livre", "racao": "Na loja de ração",
    "pesca": "Na loja de pesca",
    # + 2026-08-10: os doze locais da segunda ampliacao. ⚠️ O `.get` tem
    # fallback ("No local"), entao esquecer um rotulo aqui NAO quebra o app —
    # so' faz o resumo da janela mentir em silencio, que e' pior. O autoteste
    # cobra rotulo para todo id de LOCAIS.
    "boliche": "No boliche", "lavanderia": "Na lavanderia",
    "legiao": "No salão dos veteranos", "bingo": "No salão de bingo",
    "lanchonete": "Na lanchonete", "borracharia": "Na sala de espera da borracharia",
    "concessionaria": "No showroom da concessionária",
    "correio": "Na fila do correio", "banco": "Na fila do banco",
    "viveiro": "No viveiro de plantas",
    "arquibancada": "Na arquibancada do campo",
    "aeroporto": "No portão do aeroporto",
    # + 2026-08-13: os seis locais da terceira ampliacao.
    "barbearia": "Na barbearia", "academia": "Na academia",
    "leilao": "No leilão de gado", "estacao": "Na plataforma do trem",
    "casamento": "No salão de festas", "centro_comunitario": "No centro comunitário",
}


# ---------------------------------------------------------------------------
# ⭐ O "MOTOR BASE" QUE O short_comum ESPERA
# ---------------------------------------------------------------------------
# O `short_comum` recebe o motor de 5 cenas como ARGUMENTO e le' dele `montar`,
# `sortear`, `nova_fala`, `ETNIA`, `CAUDA`, `NEGACAO_AVE`, `sonorizar`,
# `NUCLEO`, `_palavras` e as tabelas `BANIDOS_*`. Ate' 2026-08-03 esse
# argumento era o modulo `pee_lucas`; agora e' este pacote de nomes locais.
#
# ⛔ `montar`/`sortear`/`nova_fala` apontam para as funcoes do ARCO LONGO.
# Aponta-las para as deste modulo — que sao as de 3 cenas — seria recursao
# infinita.
# ⚠️ Entram aqui somente os nomes que o `pee_lucas` expunha: `BANIDOS_GLOBAL`
# sim, `BANIDOS_CATEGORIA`/`BANIDOS_ANIMAL`/`BANIDOS_VAZAMENTO`/`BANIDOS_FONTE`
# nao — o `lint_curto` varre essa lista com `hasattr`, e o motor do PEE nunca
# teve as outras quatro. Inventar uma aqui ligaria uma regra que este angulo
# nunca teve.
_LONGO = SimpleNamespace(
    ETNIA=ETNIA, NUCLEO=NUCLEO, CAUDA=CAUDA, NEGACAO_AVE=NEGACAO_AVE,
    sonorizar=sonorizar, _palavras=_palavras,
    BANIDOS_TAKE=BANIDOS_TAKE, BANIDOS_IMAGE=BANIDOS_IMAGE,
    BANIDOS_GLOBAL=BANIDOS_GLOBAL, BANIDOS_CTA=BANIDOS_CTA,
    montar=_montar_longo, sortear=_sortear_longo, nova_fala=_nova_fala_longa,
)


# ===========================================================================
# FIM DA DOUTRINA INLINEADA
# ===========================================================================

# ⭐ MAPA e' de onde vem a IMAGEM; MAPA_COPY e' de onde vem a FALA. A cena 3
# junta as duas coisas: a fala do CTA (base 5) por cima da cena do ritual.
#
# ⚠️ Ordem do operador, 2026-07-31: "estamos deixando espaco valioso nesses 22
# segundos apertados no lixo". A cena 3 era o close do CTA — um terco do video
# num talking head, zero informacao visual. Agora o espectador OUVE o pedido e
# VE o gelatin trick nos mesmos 8 segundos.

# ⚠️ E aqui a cena 3 nao vem pronta do base: a do ritual dele e' insert de
# maos, e o operador pediu "rosto aparente enquanto prepara". A recombinacao
# (set da cena 2 + acao da cena 3 + rosto) mora em short_comum.bancada_com_rosto
# — nenhum fragmento novo, e o motor longo fica intacto.
# ⚠️ DOIS, nao tres. Sai a cena 4 do base (a redencao): ela e' a que o
# colapso temporal come. Fica a 1 (a mancha, o hook) e a 3 (a bancada, o
# payoff com rosto).
MAPA = (1, 3)
MAPA_COPY = (1, None)             # None = a fundida
# ⛔⛔ DUAS CENAS. A do meio (a redencao) morre como QUADRO; a fundida
# herda o quadro da CTA — a bancada com o rosto dele — e leva o truque
# para dentro da fala.
CENAS_UI = ["1 · A MANCHA", "2 · O TRUQUE + CTA"]

# As pontas herdam o teto do ARCO LONGO — os pools sao os mesmos, e no PEE eles
# estao bem calibrados (0% de estouro em 300 sorteios medidos). So' a cena 2
# tem teto proprio, porque a copy dela e' propria.
# ⛔ 34 estava ACIMA DO FISICO (32 = 8s a 4,0 palavras/s, licoes §5).
# Nao estourava por sorte do pool — o maximo GERADO medido em 600
# sorteios era 31. Mas teto declarado acima da capacidade e' bomba
# armada: o lint compara com ESTE numero, entao aprovaria a primeira
# entrada longa que alguem acrescentasse, e a fala sairia cortada no
# render sem ninguem ver (licoes §27). Baixado em 2026-08-04.
# ⛔⛔ TETO 25 — ordem permanente do operador, 2026-08-05: *"sempre meca. Nao
# pode haver cortes de fala."* O numero vem de RENDER, nao de conta: 32
# cortou e 28 cortou. Os exemplos que ele escreve a mao vivem em 16-25
# palavras (2,0-3,1 p/s). Ver licoes-de-construcao §28.
# ⭐⭐ MODOS DE REF — contrato compartilhado (short_comum),
# 2026-08-05. ⛔ Desligados, o prompt volta IDENTICO ao de antes
# do recurso — provado caractere por caractere.
MODO_BELA = True

# ⛔⛔ MODO FORTE DESLIGADO EM 2026-08-10, E O MOTIVO E' MEDIDO, NAO ESTETICO.
# ---------------------------------------------------------------------------
# Achado ao LER um roteiro com o toggle ligado, na conferencia da reforma dos
# pools de rosto. Com `--forte` este motor entregava:
#
#   "Photo of a real person, a 29-YEAR-OLD Black American man ... Clear
#    steel-blue eyes, A STRONG SQUARE JAW and A SHORT BEARD."
#
# Tres coisas quebram de uma vez, e nenhuma e' opiniao:
#   1. ⛔ A BARBA VIOLA O PE9/F4b. O narrador ser BARBEADO e' um dos tres eixos
#      que o separam da vitima (careca + bigode + oculos) a' distancia, num
#      plano medio em que os dois dividem o quadro. O `sc.REFS_FORTES` tem
#      SETE das dezesseis entradas com pelo facial — 44% dos sorteios do modo
#      apagariam o contraste que este agente inteiro depende.
#   2. ⛔ A IDADE. O pool compartilhado vai de 26 a 38 anos. Aqui o narrador
#      se agacha ao lado de um PAR de 56-70 e explica a prostata dele. Um
#      rapaz de 29 nao tem autoridade nenhuma sobre esse assunto, e o
#      `idade_min` do `ref_forte` nao resolve: ele CEDE quando nada cabe na
#      faixa, entao devolveria 38 no melhor caso.
#   3. ⛔ `a strong square jaw` esta' na lista de adjetivos que empurram PARA a
#      celebridade — que e' exatamente o defeito que o operador mandou matar.
#
# ⭐ E O MODO NAO FAZ FALTA: o musculo que ele existe para adicionar JA' ESTA'
# na string travada do BLOCO 0 deste motor (`The dense build of a man who
# lifts, thick through the chest and shoulders, forearms corded`). O toggle
# nao acrescentava porte — trocava um narrador certo por um errado.
#
# ⚠️ O RAMO `sc.ref_forte` NO `_sortear_longo` FICA. Religar e' UMA linha aqui,
# e o autoteste ja' guarda a condicao: com `MODO_FORTE = True` ele passa a
# EXIGIR que a REF forte respeite o PE9, e reprova enquanto o pool
# compartilhado tiver barba. Regra que some sem explicacao vira divida.
MODO_FORTE = False

# ⛔⛔ DUAS CENAS no teto FISICO de 25.
# ⚠️ A fundida NAO herda os pools do motor de 24s: a menor FUNDIDA de la'
# tem 23 palavras e o menor CTA 10 — 33 contra teto 25. Foi reconstruida
# em eixos que cabem por construcao.
TETO_FALA = {1: TETO_FALA_LONGO[1], 2: 25}


# ---------------------------------------------------------------------------
# A COPY FUNDIDA — cena 2
# ---------------------------------------------------------------------------
# ⚠️ CURADORIA DO OPERADOR. Copy nova, montada dos fragmentos ja' validados dos
# MECANISMOS, RITUAIS e REDENCOES do motor base.
#
# Todo item carrega, na mesma respiracao:
#   1. o mecanismo -> a `prostate` apertando o cano (PE7)
#   2. o ritual    -> a string literal `gelatin trick`
#   3. a virada    -> ele seco, dezenove dias depois, e ela
# ⛔ Sem {barreira}: tres beats ja' enchem os 8 segundos.
# ⚠️ Todo item precisa de `{o}` — o CTA nao nomeia o orgao.
#
# ⭐ 2026-08-03 — VERBO DE ENCANAMENTO NO LUGAR DO RESULTADO. O operador leu as
# falas no proprio app e reprovou o verbo `open`:
#     "Nobody makes a dime telling you what opens it." -> "Opens o QUE? Com
#      tanto verbo que voce poderia usar de forma mais obvia pra dizer que DEIXA
#      O PINTO MELHOR, voce usa 'opens'?"
# REGRA NOVA: o que o gelatin trick FAZ e' dito com VERBO DE RESULTADO, no
# registro em que um homem diria — `gets him hard again`, `wakes your {o} back
# up`, `got his {o} working again`, `brought his {o} back hard`. O mecanismo
# (a prostata no cano) continua na fala, porque e' o PE7 e o linter cobra o
# literal `prostate`; o que sai e' o verbo do cano ocupando o lugar do
# beneficio. Sete entradas foram reescritas (1, 4, 5, 6, 8, 11 e 13, na ordem
# deste pool): seis usavam `open*` como acao do truque, e a 11 usava a metafora
# `moved the thumb` no mesmo lugar, deixando o homem DEDUZIR o resultado.
# ⛔ O criterio nao e' o regex: e' a pergunta "um homem ouvindo isso entende que
# o negocio deixa o pinto dele funcionando?". `da' pra deduzir` reprova.
# ⛔ NAO se troca `open` por outro eufemismo de encanamento (`unblocks`,
# `restores flow`, `frees it up`): trocar metafora por metafora nao conserta
# nada — e' o §17 das licoes ("trocar uma abstracao por outra e chamar de
# conserto").
# ⛔ Teto da cena 2 = 34 palavras e nao subiu: onde o verbo de resultado ficou
# mais longo que `opened it`, o corte saiu da MESMA entrada (a marcacao de
# tempo virou o fragmento `Nineteen days.`, forma que ja' rodava aqui).
#
# ⛔⛔⛔ POOL MORTO — NAO E' LIDO POR NINGUEM DESDE 2026-08-09, quando o
# `_fundir` passou a montar a cena 2 dos quatro eixos (`MECANISMOS16`,
# `PROVAS16`, `GATES16`, `CTAS16`). Fica no arquivo como HISTORICO das licoes
# que estao escritas nos comentarios acima (o verbo de resultado no lugar do
# verbo de encanamento, o prazo que derrubou o video do NECROSE).
# ⚠️ E FICA CONDENADO: nenhuma destas 14 entradas passa no CONTRATO DE COPY 16s
# de 2026-08-10 — todas estouram o teto de 25, nenhuma tem CTA, e varias trazem
# `hard`/`came back` colado no orgao (CT7) e prazo junto de `your {o}`.
# ⛔ Religar este pool sem reescreve-lo devolve os cinco defeitos medidos.
FUNDIDAS = [
    "It's the prostate pressing the line flat — the same squeeze that starves "
    "your {o}. His brother gave him the gelatin trick. Nineteen days later he "
    "was dry, head up.",

    # 2026-08-03: `opened both` -> `got him hard again`. "Abriu os dois" o QUE?
    "His prostate clamped the pipe shut, and that same pressure shut his {o} "
    "down. The gelatin trick got him hard again. Nineteen days later she "
    "reaches for him first.",

    "It's his prostate choking the line — the same squeeze is why your {o} "
    "can't fill. One spoon of the gelatin trick, and nineteen days later he "
    "was dry.",

    "The prostate sits on that pipe and shuts your {o} down. His brother handed "
    "him the gelatin trick. Nineteen days later he walked in dry, head high.",

    # 2026-08-03: `opened it` -> `got his {o} hard again` (o alvo entra no verbo).
    "Pills don't touch this — it's the prostate pressing the line flat. The "
    "gelatin trick got his {o} hard again, and nineteen days later he still "
    "hasn't quit.",

    # + 2026-08-01: o operador mediu vicio — a mesma fundida em todo lote SHORT.
    # Pool ampliado; cada item continua carregando o literal `gelatin trick`,
    # a prostata no cano e o {o}, porque as cenas que os traziam sao as que caem.
    # 2026-08-03: `It opens the line...` gastava a frase no cano. A prostata
    # continua nomeada (PE7), mas o verbo do truque agora e' o resultado.
    # ⛔ CONSERTO 2026-08-03, no mesmo dia: a versao acima terminava em
    # `wakes your {o} back up. Nineteen days.` — e isso e' `your <orgao>` +
    # PRAZO no mesmo take de 8s, a composicao EXATA que derrubou o video do
    # NECROSE por conteudo nocivo. Passou pelo RS10 porque o regex so' via
    # `in nineteen days` e a frase entregava o prazo como FRAGMENTO SOLTO.
    # ⚠️ E o fragmento tambem era o vicio [F] que este mesmo lote veio matar.
    # O prazo sai; o resultado fica.
    "A man at the barbershop handed him the gelatin trick. The prostate was "
    "pinching the line shut — this wakes your {o} back up.",

    # 2026-08-03: `got the pipe open` gastava o verbo do truque no cano e
    # deixava o orgao de carona (`came back with it`). Agora o truque age
    # direto no orgao: `brought his {o} back hard`.
    "Nineteen days is all it took. His prostate quit squeezing the line, and "
    "the gelatin trick brought his {o} back hard. She noticed first.",

    "Same prostate, two failures — the wet pants and the dead {o}. One spoon "
    "of the gelatin trick, and nineteen days later he was dry and she wasn't "
    "sleeping.",

    # 2026-08-03: `opened his in nineteen days` — abriu o QUE dele? Virou
    # `got him standing again`.
    # ⛔ CONSERTO no mesmo dia: o prazo tinha virado o FRAGMENTO `Nineteen
    # days.` — sintagma nominal sem verbo, que e' o vicio [F] deste lote, e
    # ainda por cima somava PRAZO a `your {o}` da primeira frase (RS10, a linha
    # do NECROSE). Prazo fora.
    "If you get up twice a night, that's the prostate on the line, and your "
    "{o} is next. The gelatin trick got him standing again.",

    "A retired trucker told him about the gelatin trick. It gets under the "
    "prostate that's squeezing the pipe, and nineteen days later his {o} "
    "answered.",

    "Doctors treat the bladder and leave the rest. It's one prostate on one "
    "pipe. He stirred the gelatin trick into cold water and got his {o} back.",

    # 2026-08-03: `moved the thumb` era o verbo do truque, e o payoff so' dizia
    # `dry and grinning` — o homem tinha de DEDUZIR o resultado no corpo dele.
    # A metafora do polegar fica (e' o mecanismo); o resultado agora e' dito.
    "Think of a thumb over a hose end — that's his prostate, and your {o} "
    "gets nothing. The gelatin trick moved the thumb. Nineteen days later he "
    "was dry and hard again.",

    "He laughed at the gelatin trick too. Then his prostate stopped sitting "
    "on that pipe, and three weeks later she was the one bragging about his {o}.",

    # 2026-08-03: `opened both for him` -> `put him back to work`. A frase 1 ja'
    # nomeia `your {o}`, entao o pronome no verbo nao fica sem referente.
    "The prostate closes the pipe first and your {o} second. Nobody tells you "
    "that. The gelatin trick put him back to work, and she noticed inside three "
    "weeks.",
]


# ---------------------------------------------------------------------------
# ⭐⭐ A FALA DA CENA FUNDIDA — EIXOS COMPOSTOS
# ⭐⭐ REESCRITA TOTAL EM 2026-08-10 — CONTRATO DE COPY 16s
# ---------------------------------------------------------------------------
#     {MECANISMO} {PROVA} {GATE} {CTA}          <- o CTA e' o FIM do video
#
# ⛔⛔ A ORDEM MUDOU, e essa e' a correcao mais cara do lote (CT1). Antes o
# gate vinha DEPOIS do `Comment gelatin,` e a ultima coisa no ouvido — colada
# no unico pedido que gera receita — era `Follow, then comment.` / `Followers
# only.`: um segundo CTA nu, ou uma condicional na recompensa. Medido: 26% dos
# sorteios deste motor. A posicao final e' a que fica, e ela tem de ser o
# pedido. ⭐ O follow continua existindo — ele so' passou para ANTES.
#
# ⛔ Ordens do operador que continuam governando estes pools:
#   · *"nao use pronome, seja taxativo e claro"* — o homem da prova e' NOMEADO.
#   · *"seja mais taxativo: I'll send recipe"* — toda entrada de CTAS16 nomeia
#     `recipe`. Os CTAs de 24s prometem `that exact one` — de QUE, o espectador
#     nao sabe.
#   · *"faltou gravitar pro centro, que e' o john-son dele voltar a
#     funcionar"* — a prova e' o ORGAO, nunca o vazamento parando.
#
# ⭐⭐ O ORCAMENTO E' FECHADO E TODA ENTRADA TEM O MESMO TAMANHO:
#         mecanismo 9  +  prova 5  +  gate 3  +  CTA 8  =  25  = TETO_FALA[2]
# ⛔ POR QUE TAMANHO FIXO, e nao "8-11 palavras" como antes: com quatro batidas
# somando num teto apertado, pool de tamanho variavel nao e' pool — e' um pool
# pequeno com enfeites. O solver so' pode sortear o que CABE, entao a entrada
# longa nunca sai e morre viva dentro do arquivo. Com os quatro tamanhos
# travados, TODA combinacao cabe por construcao: 12 x 12 x 8 x 10 = 11.520
# falas, e o [ALCANCE] medido e' 100% dos itens de todos os quatro pools.
# ⚠️ Quem mexer nestes pools tem de respeitar a soma. O solver abaixo tem rede,
# mas rede que dispara e' entrada morta.

# ⚠️ 9 palavras exatas. O mecanismo do PEE e' a PROSTATA apertando a linha — e'
# o que separa este angulo dos outros dezoito, e some se a fala nao o disser.
# ⛔ CT3 — `gelatin trick` NUNCA aparece como rotulo nu. Cada entrada carrega,
# na MESMA sentenca, um VERBO DE EFEITO e um ALVO (o orgao ou o sangue).
# Medido antes: 84% dos sorteios traziam `The gelatin trick opens it.` ou
# `...takes the prostate off your {o}.` — o primeiro sem alvo, o segundo com um
# verbo que nao diz efeito nenhum. Nome de mecanismo sem razao ao lado nao vira
# crenca: vira ruido de marca.
# ⚠️ Os verbos saem da lista `short_comum.VERBOS_EFEITO_16`, que e' a mesma que
# a lente cobra — `unpinches`, `frees`, `releases` e `takes` sairam por nao
# estarem la' (e por nao dizerem, em boca americana, o que o negocio FAZ).
# ⛔ `choked`, `blood flow` e `shut down` ficam FORA de proposito: sao os
# tokens que o `medir_contexto_copy` conta como fisiologia solta.
#
# ⛔⛔ TODA ENTRADA NOMEIA O ORGAO, e isso e' decisao MEDIDA, nao gosto. A
# primeira versao desta reforma tinha quatro entradas em que o alvo era so' o
# sangue (`...pushes blood past that swollen prostate.`). Elas passavam no CT3
# — `blood` e' alvo valido — e o `medir_abertura` as pegou: a PRIMEIRA sentenca
# do take 2 nao dizia o que estava quebrado, e ela chega ao ouvido logo DEPOIS
# DO CORTE. E' a mesma premissa do CT4: o corte zera a memoria de trabalho, e o
# que o take 1 disse ha' oito segundos nao esta' mais na cabeca de quem ouve.
# Medido: 40% das aberturas do take 2 orfas com as quatro entradas de sangue,
# 0% depois de tira-las.
# ⚠️ O molde e' unico de proposito — `<verbo de efeito> the prostate
# <participio> your {o}` — porque em nove palavras cabem exatamente as quatro
# coisas obrigatorias: o literal `gelatin trick`, o literal `prostate`, o verbo
# de efeito e o orgao. A variacao mora no par verbo x participio (6 x 7), nao
# na sintaxe. Pool de 8 -> 12 entradas.
MECANISMOS16 = [
    "The gelatin trick loosens the prostate choking your {o}.",
    "The gelatin trick loosens the prostate strangling your {o}.",
    "The gelatin trick loosens the prostate crushing your {o}.",
    "The gelatin trick stops the prostate starving your {o}.",
    "The gelatin trick stops the prostate squeezing your {o}.",
    "The gelatin trick stops the prostate pinching your {o}.",
    "The gelatin trick fixes the prostate clamping your {o}.",
    "The gelatin trick fixes the prostate choking your {o}.",
    "The gelatin trick fixes the prostate starving your {o}.",
    "The gelatin trick moves the prostate off your {o}.",
    "The gelatin trick clears the prostate off your {o}.",
    "The gelatin trick keeps the prostate off your {o}.",
]

# ⚠️ 5 palavras exatas.
#
# ⛔⛔ `the husband` FOI APOSENTADO EM 2026-08-10. Ele nasceu de uma ordem certa
# — *"nao use pronome"* — com uma execucao errada: artigo definido sem dono. No
# angulo PEE nao ha' esposa nomeada em cena nenhuma, entao `the husband` chega
# ao ouvido como marido DE QUEM, e ainda por cima empilhava o apelido do orgao
# duas vezes na mesma respiracao (`That's how the husband's Johnson came back`).
# ⭐ NO LUGAR, UM DEITICO COM REFERENTE EM QUADRO: `that man` / `that fella` /
# `that guy`. O espectador acabou de passar oito segundos olhando exatamente um
# homem — o da calca molhada. E' a designacao mais concreta que este video tem,
# e ela nao depende de nenhuma sentenca anterior para se sustentar.
#
# ⛔ CT7 — NENHUM VERBO DE ERECCAO COLADO NO ORGAO. Medido antes: 54% dos
# sorteios diziam `came back`, `works again` ou `got hard again` grudado no
# apelido, e essa e' a licao paga em campo no COLO 16 (~95% de recusa do
# gerador). O que voltou continua sendo dito — com `answered`, `never quits`,
# `never fails`, `quit hiding`, que sao o idioma da casa e passam no render.
# ⛔⛔ `answered her` FOI DERRUBADO EM 2026-08-10, na conferencia da reforma, e
# a razao e' MEDIDA: 16,5% dos 400 sorteios entregavam `That fella's manhood
# answered her.` sem UMA mulher no video inteiro. E nao e' descuido do pool —
# e' estrutural deste 16s: o `MAPA` e' `(1, 3)`, e a cena do payoff (a mulher
# no colo dele, cena 4 do arco longo) e' justamente a que o colapso temporal
# come. Sobram dois quadros — a loja e a bancada — e em nenhum dos dois existe
# uma mulher. Nos 400 sorteios, 66 nao tinham sequer a palavra `wife` no take 1:
# o `her` chegava ao ouvido sem dono nem em fala nem em imagem.
# ⭐ E' a lei `pronome-generico-e-drifting` do repo, na letra: *"`she`/`it` sem
# dono nao compra; decompor em pool de designacoes concretas, NAO escrever
# frase melhor"*. Por isso o conserto nao inventa uma mulher nomeada (isso
# seria CENA nova, alcada do operador) — ele tira o pronome e devolve a prova
# ao ORGAO, que e' onde a ordem do operador ja' mandava ela gravitar
# (*"faltou gravitar pro centro, que e' o john-son dele voltar a funcionar"*).
# ⚠️ `works nights` e nao `works again`: `works again` esta' dentro do
# `ERECAO_16` e reprovaria no CT7 (a licao paga no COLO 16). A metafora de
# turno de trabalho e' a mesma familia de `never quits` / `never fails`, que
# sao as formulas que ja' passam no render.
# ⚠️ 5 palavras exatas, e o pool continua com 12 entradas (3 designacoes x 4
# predicados): nenhuma entropia perdida na troca.
PROVAS16 = [
    "That man's {o} works nights.",
    "That man's {o} never quits.",
    "That man's {o} never fails.",
    "That man's {o} quit hiding.",
    "That fella's {o} works nights.",
    "That fella's {o} never quits.",
    "That fella's {o} never fails.",
    "That fella's {o} quit hiding.",
    "That guy's {o} works nights.",
    "That guy's {o} never quits.",
    "That guy's {o} never fails.",
    "That guy's {o} quit hiding.",
]

# ⚠️ 3 palavras exatas, FRASE SEPARADA — nunca colada no `Comment gelatin,`.
# ⛔ A automacao de DM casa palavra EXATA: follow encostado na keyword faz o
# comentario sair com duas palavras e a automacao nao dispara.
# ⛔ CT1 — o gate agora entra ANTES do CTA. E por isso `Follow, then comment.`
# saiu: encostado no `Comment gelatin,` que vem em seguida, ele mandava
# comentar duas vezes.
# ⚠️ No maximo 2 entradas com vocativo no pool inteiro (regra de 2026-08-01,
# nascida do `brother` saindo em todo CTA do lote). Aqui sao 2: brother e buddy.
# ⛔⛔ POOL APOSENTADO EM 2026-08-10 — ELE NAO CHEGA MAIS AO VIDEO.
# Ordem do operador: *"nao acho que deva ter follow me no cta, a mensagem e'
# enviada independente de seguirem ou nao"* (CT8 do CONTRATO-COPY-16S).
# O gate existia no repo inteiro por uma PREMISSA ERRADA sobre a automacao de
# DM, e quem opera a automacao corrigiu a premissa.
# ⚠️ POR QUE NAO FOI APAGADO: o autoteste e os contratos deste motor ainda o
# validam (contagem minima, vocativo, tamanho), e apagar exigiria mexer neles
# no mesmo commit em que a copy inteira mudou — duas cirurgias de uma vez e'
# como se perde o rastro do que quebrou o que.
# ⛔ ENTAO FICA ESTE AVISO: melhorar as entradas abaixo NAO muda um unico
# video. Se o follow voltar um dia, ele volta ANTES do CTA (CT1) e por decisao
# do operador, nao por alguem reativar a variavel.
GATES16 = [
    "Tap follow first.",
    "Hit follow first.",
    "Follow me first.",
    "Tap follow now.",
    "Hit follow now.",
    "Follow first, please.",
    "Follow me, brother.",
    "Follow me, buddy.",
]

# ⚠️ 8 palavras exatas, TODAS nomeando `recipe` e TODAS dizendo ONDE ela chega.
# ⛔ CT6 — a clausula de entrega nao e' enfeite, e' o que paga a cobertura
# social. O KPI deste funil e' uma CONFISSAO PUBLICA: o comentario leva nome e
# foto e cai no feed da esposa. Medido antes: 100% dos sorteios pediam o
# comentario sem uma palavra baixando esse custo.
# ⭐ E a clausula e' DE GRACA: `and I'll send the recipe tonight` custa as
# mesmas palavras que `and the recipe hits your messages`, e a segunda entrega
# o endereco, a privacidade e o fato de que nao e' na tela publica.
# ⛔ `Comment gelatin,` e' LITERAL (short_comum.CTA_LITERAL) e a virgula depois
# da keyword nao e' opcional: sem a micro-pausa o Veo emenda e narra "gelatine".
# ⚠️ 2026-08-10 — CONECTOR OBRIGATORIO DEPOIS DA KEYWORD. Medido: 81% dos
# CTAs deste motor saiam como `Comment gelatin, your inbox gets...` — emenda
# de virgula na unica frase do video que gera receita. Sem conector as duas
# oracoes colidem no ouvido e o imperativo (`Comment gelatin`) deixa de soar
# como comando. Custa UMA palavra e havia 3 de folga no teto.
CTAS16 = [
    "Comment gelatin, and the recipe hits your messages.",
    "Comment gelatin, and the recipe hits your inbox.",
    "Comment gelatin, and the recipe reaches your messages.",
    "Comment gelatin, and the recipe reaches your inbox.",
    "Comment gelatin, and your messages get the recipe.",
    "Comment gelatin, and your inbox gets the recipe.",
    "Comment gelatin, and the recipe goes to your messages.",
    "Comment gelatin, and the recipe lands in your inbox.",
    "Comment gelatin, and the recipe waits in your messages.",
    "Comment gelatin, and nobody else sees the recipe.",
]


def _fundir(spec, rng):
    """`MECANISMO + PROVA + GATE + CTA`, tudo dentro do teto da cena 2.

    ⛔⛔ RELIGADO EM 2026-08-09. Esta funcao devolvia so' uma `FUNDIDAS` — o
    video inteiro saia SEM `Comment gelatin`, e o linter reprovava 400 de 400
    sorteios. E reprovava certo: video de funil sem CTA e' pior que video que
    nao gera, porque o defeito e' silencioso.
    ⭐ 12 x 12 x 8 x 10 = 11.520 falas, contra as 14 `FUNDIDAS` fixas de antes.

    ⛔⛔ O ORGAO VEM DO HOOK — CT4, 2026-08-10. Ate' hoje esta linha lia
    `spec["falas_base"][3]`, que e' a fala da REDENCAO do arco longo e usa
    `orgaos[3]`, um substantivo DIFERENTE do `orgaos[0]` do hook. Resultado
    medido: o apelido do orgao mudava no corte em 98% dos videos. Em 24s e
    cinco cenas o bordao e' o risco; em 16s e duas cenas o risco e' o oposto —
    o corte zera a memoria de trabalho, e trocar `tool` por `Johnson` no
    segundo 9 obriga o espectador a remapear justamente quando ele ja' esta'
    com um pe' fora.
    ⚠️ `spec["falas"][0]` e nao `falas_base[0]`: os dois sao o hook no sorteio,
    mas quando o operador re-sorteia a cena 1 na janela (ou troca o LOCAL, que
    reescreve o hook) so' o primeiro esta' atualizado. Ler o `falas_base` ali
    devolveria o apelido velho e a fala 2 sairia falando de outro orgao.

    ⛔ A ORDEM DE MONTAGEM NAO E' ARBITRARIA — e' a mesma licao do CLEAN
    16seg: sorteia-se entre os que CABEM, nunca solto para testar depois.
    Sorteando solto, so' a combinacao mais curta sobrevive e o pool inteiro
    colapsa em duas ou tres falas. Quem escolhe PRIMEIRO e' a batida com MENOS
    SUBSTITUTOS (o mecanismo: ele carrega o literal `gelatin trick`, o literal
    `prostate`, o verbo de efeito e o alvo, tudo na mesma sentenca); o CTA
    escolhe por ULTIMO e absorve a sobra.
    ⚠️ Hoje a rede nunca dispara: os quatro pools tem tamanho FIXO e somam 25
    exatos, entao toda combinacao cabe. Ela fica de pe' para o dia em que
    alguem acrescentar uma entrada fora da conta — sem ela, a entrada nova
    sairia silenciosamente do sorteio (ou estouraria o teto no render, que e'
    pior).
    """
    o = sc.orgao_de(_LONGO, spec["falas"][0])
    fmt = lambda t: t.format(o=o)                              # noqa: E731
    teto = TETO_FALA[2]

    def menor(pool):
        return min(_palavras(fmt(t)) for t in pool)

    def escolher(pool, gasto, reserva):
        cabem = [t for t in pool if gasto + _palavras(fmt(t)) + reserva <= teto]
        if not cabem:
            # ⛔ rede sem invencao: a entrada mais curta que existe no pool.
            # Nunca `or pool` cru, que e' o que estourava o teto antes.
            return min(pool, key=lambda t: _palavras(fmt(t)))
        return rng.choice(cabem)

    x = escolher(MECANISMOS16, 0,
                 menor(PROVAS16) + menor(GATES16) + menor(CTAS16))
    gasto = _palavras(fmt(x))
    p = escolher(PROVAS16, gasto, menor(GATES16) + menor(CTAS16))
    gasto += _palavras(fmt(p))
    # ⛔⛔ CT8 (2026-08-10) — O BEAT DO FOLLOW SAIU DA FALA.
    # Ordem do operador: *"nao acho que deva ter follow me no cta, a
    # mensagem e' enviada independente de seguirem ou nao"*. O gate
    # existia no repo inteiro por uma PREMISSA ERRADA sobre a automacao
    # de DM, e quem opera a automacao corrigiu. As palavras liberadas
    # vao para o mecanismo e a prova.
    c = escolher(CTAS16, gasto, 0)
    return "%s %s %s" % (fmt(x), fmt(p), c)


# ---------------------------------------------------------------------------
# CONTRATO DO MOTOR
# ---------------------------------------------------------------------------

def _carregar_ledger():
    import json
    if os.path.exists(LEDGER):
        with open(LEDGER, encoding="utf-8-sig") as f:
            return json.load(f)
    return {}


def _anotar(ledger, spec):
    """Anota o sorteio no ledger EM MEMORIA — sem tocar em disco.

    ⛔ Separado do `_gravar_ledger` em 2026-08-10 por um motivo so': o
    autoteste precisa medir a ANTI-REPETICAO, e medir isso exige rodar
    centenas de sorteios COM a memoria ligada. Chamando o `_gravar_ledger`
    ele escreveria o `.pee-16-ledger.json` de verdade a cada sorteio — o
    teste envenenaria o ledger do operador e ainda mediria com I/O no meio.
    ⚠️ E a alternativa (reescrever a logica de append dentro do teste) e' pior:
    o teste passaria a medir a COPIA, e a copia nao drifta junto com o
    original. Aqui os dois caminhos leem a mesma funcao.
    """
    p = ledger.setdefault(spec["pagina"], {})
    # ⛔ `ref` e `vitima` entraram em 2026-08-10 — sem gravar aqui, a janela
    # nova do `_sortear_longo` leria uma lista sempre vazia e o eixo voltaria
    # a sortear sem memoria. Ledger tem DOIS lados, e ja' se perdeu um dia
    # ligando so' um deles.
    # ⚠️ `.get("id")` e nao `["id"]`: no MODO FORTE o dicionario vem do
    # `sc.ref_forte`, e um `KeyError` aqui derrubaria a gravacao DEPOIS de o
    # roteiro ja' ter sido montado e mostrado.
    for eixo, val in (("local", spec["local"]["id"]),
                      ("roupa", spec["roupa"]["id"]),
                      ("ambiente", spec["ambiente"]["id"]),
                      ("prop", spec["prop"]["id"]),
                      ("ref", spec["ref"].get("id")),
                      ("vitima", spec["vitima"].get("id"))):
        if val is None:
            continue
        p.setdefault(eixo, []).append(val)
        # ⚠️ 12 e' a cauda guardada; a JANELA LIDA no `_sortear_longo` e' menor
        # (6 para o local, 8 para o narrador). Guardar mais do que se le' e' de
        # proposito: da' folga para subir uma janela sem perder historico.
        p[eixo] = p[eixo][-12:]


def _gravar_ledger(ledger, spec):
    """Anota E escreve. E' o que a UI e a linha de comando chamam."""
    import json
    _anotar(ledger, spec)
    with open(LEDGER, "w", encoding="utf-8") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)


def sortear(pagina, rng, ledger, travas=None):
    return sc.sortear_curto(_LONGO, pagina, rng, ledger, MAPA, _fundir,
                            MAPA_COPY, travas)


# ⛔⛔ O DEITICO DO HOOK — 2026-08-10, relato de campo do operador.
# Os 20 hooks dizem `in {evento}`, e os 14 eventos sao todos DISTAIS: `that
# store`, `that pharmacy`, `that produce aisle`. Mas na cena 1 o narrador esta'
# DENTRO do lugar, agachado ao lado do homem — e apontava para "aquela loja"
# estando nela.
# ⚠️ Nao e' o tempo verbal: passado sobre cena ao vivo passaria ("acabou de
# acontecer"). O que quebra e' o DEDO apontando para fora de onde ele ja' esta'.
# Mesma familia do defeito do NECROSE 16, que o operador pegou lendo a copy.
# ⛔ A troca acontece SO' AQUI, no 16s. O arco de 5 cenas tem cenas em outro
# lugar, e la' o `that` esta' certo — mexer no pool quebraria o motor longo.
def _aqui(evento):
    """`that store` -> `this store`: o narrador esta' dentro do lugar."""
    return evento[5:] and "this " + evento[5:] if evento.startswith("that ")         else evento


def montar(spec):
    b = sc.montar_curto(_LONGO, spec, MAPA)
    # ⛔⛔ CONSERTADO EM 2026-08-09. O agente NAO ABRIA: montava as cenas 2 e 3
    # do formato de 3 cenas (`spec["falas"][2]`) enquanto o `sortear_curto` ja'
    # entregava DUAS falas — `IndexError: list index out of range` no primeiro
    # sorteio, antes da janela subir. E ainda gravava com as tags `02/03` e
    # `03/03`, que o `montar_curto` ja' tinha parado de emitir.
    # ⚠️ Sobrou do colapso: o `montar_curto` foi generalizado em 18aa6dd e o
    # `sortear_curto` em 70228dd, mas o override daqui ficou para tras. Terceira
    # peca da mesma familia.
    #
    # ⭐ QUAL DAS DUAS CENAS ESPECIAIS SOBREVIVE — as duas nasceram de ordem do
    # operador em 2026-07-31 e, com dois takes, so' uma cabe:
    #   `redencao_com_ref`   punha o NARRADOR de volta em quadro, porque em 3
    #                        cenas ele sumia no terco do meio;
    #   `bancada_com_rosto`  poe o ROSTO no ritual, porque a cena do CTA sem
    #                        cara nao converte (*"pedido sem cara"*).
    # Fica a SEGUNDA. O motivo da primeira era o meio do video, e em 2 cenas
    # nao existe meio — o narrador ja' esta' na cena 1. O motivo da segunda
    # continua inteiro: a cena 2 e' onde mora o `Comment gelatin`.
    # ⚠️ Para inverter a escolha e' UMA linha: trocar `bancada_com_rosto` por
    # `redencao_com_ref` abaixo. As duas tem a mesma assinatura.
    # ⭐ 2026-08-10 — `sache_erguido`, o mesmo modo que o FLAGRANTE 16 recebeu
    # horas antes, pelo relato IDENTICO do operador: *"copo de agua transparente
    # mexendo com uma colher, e o saco da gelatina sem nome nenhum"*.
    # O copo ja' nasce cheio de `vivid purple`, sem colher em quadro, e ele
    # ergue o sache rotulado GELATIN HORSE TRICK para a lente enquanto fala.
    # ⛔ Nao ha' despejo: acao em dois estados e' o que faz o modelo duplicar
    # objeto. Duas evidencias PARADAS — o roxo (resultado) e o sache (causa).
    i2, t2 = sc.bancada_com_rosto(_LONGO, spec, spec["falas"][1], n=2, total=2,
                                  modo="sache_erguido")
    b["IMAGE 02/02"], b["TAKE 02/02"] = i2, t2
    # ⛔ trava de texto queimado em todo TAKE — o watermark que o
    # operador viu vazando nos reels da concorrente (2026-08-01).
    return sc.selar_takes(b)


def nova_fala(spec, i, rng):
    return sc.nova_fala_curta(_LONGO, spec, i, rng, MAPA, _fundir, MAPA_COPY)


def _recopiar_local(spec, rng):
    """O local entra no hook — trocar exige reescreve-lo."""
    spec["falas"][0] = _nova_fala_longa(sc.espelho(spec, MAPA), 0, rng)


EIXOS_QUE_MEXEM_NA_COPY = {"local": _recopiar_local}


# ---------------------------------------------------------------------------
# LINTER
# ---------------------------------------------------------------------------

def _pe6_hook(spec, blocos, achados):
    """O hook diz o mijo, nomeia o orgao e AFIRMA o vinculo entre os dois."""
    h = spec["falas"][0].lower()
    if not any(t in h for t in ("peed", "wet", "soaked", "leak", "lost it")):
        achados.append(("ERRO", "PE6: o hook nao diz o mijo"))
    if not any(n.lower() in h for n in NUCLEO):
        achados.append(("ERRO", "PE6: o hook nao nomeia o orgao — hook so' de "
                                "mancha nao vende nada"))
    if not any(t in h for t in ("same thing", "same reason", "that's why",
                                "and that's why")):
        achados.append(("ERRO", "PE6: falta o VINCULO afirmado no hook "
                                "(a mancha e o orgao tem a MESMA causa)"))


def _pe1_roupa_clara(spec, blocos, achados):
    i1 = sc.bloco_base(blocos, MAPA, "IMAGE", 1).lower()
    for escura in ROUPA_ESCURA:
        if escura in i1:
            achados.append(("ERRO", "PE1: roupa escura ('%s') mata o contraste "
                                    "da mancha" % escura))


def _blocos_travados(spec, blocos, achados):
    i1 = sc.bloco_base(blocos, MAPA, "IMAGE", 1)
    # ⚠️ A plateia entra FORMATADA com o substantivo do local (2026-08-10) —
    # comparar com o template cru (`four blurred %s ...`) reprovaria 100% dos
    # sorteios, que e' a lente contra o proprio template (licoes §16).
    for s, rot in ((CHORO_IMAGE, "choro PE2"),
                   (NARRADOR_IMAGE, "narrador PE3"),
                   (PLATEIA_IMAGE % spec["local"]["plateia"], "plateia PE4")):
        if s not in i1:
            achados.append(("ERRO", "a cena da mancha sem a string travada: %s" % rot))
    # ⛔⛔ 2026-08-09 — A REGRA SO' VALE SE A CENA DO PAYOFF ESTIVER NO VIDEO.
    # Ela guarda a cena 4 do arco longo: o casal com o prop, que tem de ficar
    # IMOVEL. O MAPA deste 16s e' `(1, 3)` — a cena 4 nao entra, e o video nao
    # tem prop nenhum para ficar imovel.
    # ⚠️ Duas versoes erradas antes desta, e as duas por nao ler o que a regra
    # guarda: `4` cravado estourava `ValueError` no `.index`; apontar para
    # `MAPA[-1]` fazia ela cobrar imobilidade da cena da BANCADA, onde as maos
    # mexem a colher de proposito — reprovava 400 de 400 e teria ensinado o
    # operador a ignorar o linter.
    # ⛔ Regra que nao se aplica se DESLIGA, nao se afrouxa.
    if 4 not in MAPA:
        return
    if "motionless" not in sc.bloco_base(blocos, MAPA, "TAKE", 4).lower():
        achados.append(("ERRO", "o TAKE do payoff sem declaracao de imobilidade "
                                "do prop"))


# ⭐⭐ A LENTE DO CONTRATO DE COPY 16s (short_comum.lint_copy16), ligada em
# 2026-08-10. As sete travas moram la' e sao cobradas de fora pelo
# `medir_copy16.py` — aqui elas passam a reprovar tambem no app, na hora, antes
# de o roteiro ir para o AdBatch.
# ⚠️ `isca_absurda=False`: o PEE nao tem promessa falsa no take 1. A mancha e' o
# fato, nao a isca — entao o CT7 (verbo de ereccao colado no orgao) vale nos
# DOIS takes, e nao so' no do CTA.
def _ct16(spec, blocos, achados):
    sc.lint_copy16(sys.modules[__name__], spec, achados, isca_absurda=False)


# ⛔⛔ LENTE APOSENTADA — "substantivo repetido no video" (short_comum.lint_curto)
# ---------------------------------------------------------------------------
# Ela e' um AVISO generico do `lint_curto`: acusa quando o mesmo apelido do
# orgao aparece em mais de uma cena. Nasceu para os motores de 3 e 5 cenas, onde
# "duas mencoes iguais viram bordao" — e o CT4 do CONTRATO DE COPY 16s REVERTE
# essa regra para a familia de dois takes, com a reversao declarada:
#
#     em 24s o risco e' o bordao; em 16s o risco e' o oposto — o corte zera a
#     memoria de trabalho, e trocar o apelido no segundo 9 obriga o espectador
#     a remapear justamente quando ele ja' esta' com um pe' fora.
#
# Medido: o apelido mudava no corte em 98% dos videos deste motor. Agora ele e'
# UM SO' por video de proposito, entao o aviso acusaria 100% dos sorteios — e
# lente que reprova o que esta' certo ensina o operador a ignorar o linter
# (licoes-de-construcao §16). ⛔ Nao se apaga a regra no `short_comum`: ela
# continua valendo para os dezenove motores de 3 cenas. Desliga-se AQUI, no
# motor onde o contrato a substituiu, e com o motivo escrito.
_APOSENTADA_CT4 = "substantivo repetido no video"


def _cl25_dentes(spec, blocos, achados):
    """⛔ O REF tem de sorrir mostrando os dentes — CL25, 2026-08-10.

    Sem esta ancora na imagem de identidade o Veo inventa a dentadura quando a
    boca abre no take, e inventa podre. Foi relato de campo com render na mao.
    ⚠️ A lente olha o REF, nao o TAKE: o take herda o rosto do primeiro frame.
    """
    ref = blocos.get("BLOCO 0 (REF)", "")
    for pedaco in ("natural smile", "clean white teeth", "even, white and complete"):
        if pedaco not in ref:
            achados.append(("ERRO", "CL25: o REF nao declara %r — sem dentes na "
                                    "imagem de identidade o Veo inventa banguelo"
                                    % pedaco))


def lint(spec, blocos):
    achados = sc.lint_curto(
        _LONGO, spec, blocos, MAPA, TETO_FALA,
        literais=("gelatin trick", "prostate"),
        extras=(_pe6_hook, _pe1_roupa_clara, _blocos_travados,
                _ct16, _cl25_dentes))
    return [a for a in achados if not a[1].startswith(_APOSENTADA_CT4)]


# ---------------------------------------------------------------------------
# RESUMO
# ---------------------------------------------------------------------------

def resumo_pt(spec):
    et = "branca" if "white" in ETNIA[spec["pagina"]] else "negra"
    # ⛔ CONSERTADO EM 2026-08-10. Este texto dizia *"Na cena 2 vem o truque e a
    # virada, e na 3 o CTA. Três cenas"* — herdado do formato de 3 cenas e
    # MENTIROSO num motor de 2 takes: o operador le' este resumo na janela do
    # app, e ele descrevia uma cena 3 que nao existe e omitia que o CTA fecha o
    # take 2. Nao e' copy falada nem cena (nao muda um caractere do prompt), e'
    # rotulo de UI — e rotulo de UI que mente e' a mesma familia do botao que
    # nao trava nada.
    return ("%s, a mancha escura na calça dele com a plateia em volta. No take "
            "2 vem o mecanismo da próstata, a prova e o CTA. Dois takes de 8s, "
            "elenco de pele %s."
            % (PT_LOCAL.get(spec["local"]["id"], "No local"), et))


# ---------------------------------------------------------------------------
# ⭐⭐ AUTOTESTE — NASCEU EM 2026-08-10, e a ausencia dele era a divida mais
# cara deste arquivo
# ---------------------------------------------------------------------------
# ⛔ Este motor era um dos POUCOS 16s SEM `__main__` e sem autoteste. Consequencia
# pratica: nao havia UM comando que provasse que ele funciona. Toda alteracao de
# pool era aceita por LEITURA, e a lei do repo e' o contrario — *aceite e'
# MEDICAO, nunca RELATO*. As duas ampliacoes de pool anteriores (01/08 e 02/08)
# entraram sem nenhuma medida, e o defeito que o operador reportou hoje sobreviveu
# as duas.
#
# ⛔ O QUE ESTE AUTOTESTE GUARDA, e por que cada controle existe:
#   · CONTRASTE DE 3 EIXOS (PE9/F4b) — narrador sem oculos, sem pelo facial e
#     com cabelo; vitima careca, de bigode E de oculos, sempre. E' o que separa
#     os dois no plano medio, e nasce por construcao ou nao nasce. ⚠️ Os dois
#     primeiros tambem sao as duas ISENCOES declaradas no `medir_personagens.py`:
#     um `clean-shaven` distraido no pool dos REFS transformaria a isencao em
#     "excecao declarada que nao esta' mais zerada" e reprovaria o gate de la'.
#   · SILENCIO CONTRA A CELEBRIDADE — nenhum bloco montado pode conter
#     `celebrity`, `famous`, `not a model`, `not an actor` nem nome proprio de
#     gente. E' a ordem do operador de 2026-08-10 e a doutrina de 2026-07-31,
#     e ela so' vale se estiver em codigo: ja' voltou uma vez por copia.
#   · ANCORA DE DENTE — proibida enquanto o BLOCO 0 declarar `the front teeth
#     even, white and complete`. Duas entradas antigas do pool a tinham e
#     CONTRADIZIAM a string travada dentro do mesmo prompt.
#   · A FALA — teto por cena, e o `{evento}` do hook tem de sair legivel em
#     TODOS os locais (e' texto falado, e local novo entra na copy sem pedir
#     licenca).
#   · A ANTI-REPETICAO, MEDIDA — nao "o pool cresceu", e sim: em 60 sorteios
#     seguidos da mesma pagina, com o ledger ligado, quantas vezes o mesmo
#     rosto/lugar volta dentro da janela? A resposta tem de ser ZERO, e e' esse
#     numero que responde a queixa do operador, nao a contagem de entradas.
# ---------------------------------------------------------------------------

# tokens que pertencem a' VITIMA e nao podem vazar para o pool do narrador
_OCULOS = re.compile(r"\b(glasses|spectacles|bifocal\w*|readers|shades|lenses|"
                     r"rimless|half-?rim|half-?moon|wire-?rimmed|wire-?frame\w*|"
                     r"sunglasses|clip-?on)\b", re.I)
_PELO = re.compile(r"\b(beard\w*|mustache\w*|moustache\w*|goatee|stubble|"
                   r"sideburns|muttonchop\w*|clean-?shaven|whiskers|"
                   r"chin.?strap|chevron|walrus)\b", re.I)
_CALVO = re.compile(r"\b(bald\w*|shaved head|balding)\b", re.I)

# ⛔ o silencio contra a celebridade, em regex. `not a celebrity` e irmaos.
_CELEB = re.compile(r"\b(celebrity|celebrities|famous|movie star|"
                    r"look-?alike|resembl\w+ any)\b|\bnot an? (model|actor)\b",
                    re.I)
# ⛔ empurram PARA a celebridade (adjetivo de aprovacao no lugar de geometria)
_APROVACAO = ("handsome", "chiseled", "distinguished", "piercing eyes",
              "strong jaw", "rugged good-looking")
# ⛔ empurram para MENDIGO — matam a credibilidade do narrador
# ⛔⛔ A LISTA DOBROU EM 2026-08-13, e nao por capricho: a versao curta
# aprovava ONZE entradas dos REFS e SETE das VITIMAS que descreviam gente por
# DANO (cicatriz, mancha senil, pele castigada de sol, face avermelhada, testa
# vincada fundo, lobulo rasgado, falha entre os dentes). O gate media
# `gaunt|bony|leathery` — palavras que ninguem escreve — e ficava verde
# enquanto o pool inteiro envelhecia. ⚠️ Lente que so' pega o que ninguem faz
# e' pior que lente nenhuma: ela CERTIFICA o defeito.
# ⭐ A lista abaixo e' a ordem do operador de 2026-08-13, palavra por palavra
# (*"melhore a aparencia e shape desses homens"*, com o pool na mao). Os termos
# saudaveis que substituem cada um estao no cabecalho de REFS e de VITIMAS.
# ⚠️ `notch`/`torn` ficam de FORA da lista: entalhe de orelha e' feicao, nao
# ferida — e nenhum sobrou nos dois pools de qualquer forma.
_MENDIGO = ("gaunt", "bony", "leathery", "weather-beaten", "chipped tooth",
            "drooping eyelid", "broken capillaries", "frayed", "patchy",
            "toothless", "unkempt",
            # + 2026-08-13
            "scar", "sun damage", "sun-damaged", "weathered", "ruddy",
            "thin skin", "loose skin", "age spot", "sun-spotted",
            "liver-spotted", "sunken", "hollow cheek", "deeply lined",
            "deep lines", "creased", "worn-out", "careworn", "torn ",
            "missing tooth")
# ⚠️ `worn` CRU FOI TESTADO E CAIU NA MESMA RODADA: reprovou tres entradas
# CERTAS (`hair worn long enough to curl over his collar`, `worn long on top`,
# `heavy gray waves worn low across the forehead`) — ali `worn` e' o verbo
# VESTIR, nao o adjetivo de gasto. Quem cede e' a lente, nao o pool
# (licoes §16). Ficaram `worn-out` e `careworn`, que so' existem no sentido
# proibido.
# ⛔ contradizem a string travada do BLOCO 0 (`front teeth even, white and
# complete`) — CL25. Contradicao dentro do prompt e' onde o gerador inventa.
_DENTE = ("crown on one", "gold crown", "gap between his front teeth",
          "gap between her front teeth", "missing tooth")


def autoteste(n=400):
    falhas = []

    # -- 1. IDENTIDADE DOS POOLS ------------------------------------------
    for nome, pool in (("LOCAIS", LOCAIS), ("ROUPAS", ROUPAS),
                       ("AMBIENTES", AMBIENTES), ("PROPS", PROPS),
                       ("REFS", REFS), ("VITIMAS", VITIMAS)):
        ids = [e.get("id") for e in pool]
        if any(i is None for i in ids):
            falhas.append("%s: entrada sem `id` — o `_evitando` compara por id, "
                          "e entrada sem id nunca e' evitada" % nome)
        if len(set(ids)) != len(ids):
            dup = [i for i, c in collections.Counter(ids).items() if c > 1]
            falhas.append("%s: id repetido %s — o ledger passa a evitar duas "
                          "entradas de uma vez" % (nome, dup))

    # -- 2. A JANELA DO LEDGER TEM DE CABER NO POOL ------------------------
    # ⛔ janela >= pool deixa `livres` vazio, o `_evitando` cai no pool inteiro
    # e a memoria vira enfeite silencioso. E' o modo de falha mais traicoeiro
    # daqui: nada quebra, so' volta a repetir.
    for nome, pool, janela in (("LOCAIS", LOCAIS, 6), ("ROUPAS", ROUPAS, 3),
                               ("AMBIENTES", AMBIENTES, 3), ("PROPS", PROPS, 2),
                               ("REFS", REFS, 8), ("VITIMAS", VITIMAS, 6)):
        if janela >= len(pool):
            falhas.append("%s: janela %d >= pool %d — o `_evitando` cai no pool "
                          "inteiro e a memoria nao serve para nada"
                          % (nome, janela, len(pool)))
        elif janela > len(pool) // 2:
            falhas.append("%s: janela %d e' mais da metade do pool (%d) — sobra "
                          "pouca escolha e o sorteio vira rodizio"
                          % (nome, janela, len(pool)))

    # -- 3. PE9/F4b — O CONTRASTE DE 3 EIXOS, POR CONSTRUCAO ---------------
    for r in REFS:
        t = " ".join(str(v) for v in r.values())
        if _OCULOS.search(t):
            falhas.append("REFS %s: oculos no narrador — e' um dos 3 eixos da "
                          "VITIMA (PE9/F4b) e derruba a isencao declarada no "
                          "medir_personagens" % r["id"])
        if _PELO.search(t):
            falhas.append("REFS %s: pelo facial no narrador — idem PE9/F4b"
                          % r["id"])
        if _CALVO.search(t):
            falhas.append("REFS %s: calvicie no narrador — idem PE9/F4b"
                          % r["id"])
        # ⚠️ A LISTA E' LARGA DE PROPOSITO, e nasceu larga porque a versao
        # estreita (`hair|curls|mane|flat-top`) reprovou duas entradas CERTAS
        # na primeira rodada: `a heavy gray-brown mop combed forward` e `heavy
        # gray waves worn low across the forehead` descrevem cabelo sem dizer a
        # palavra. Lente que reprova o que esta' certo ensina a ignorar a lente
        # (licoes §16) — quem cede e' a lente, nao o pool.
        # ⛔ E' a mesma familia de tokens do eixo `cabelo` do medir_personagens.
        if not re.search(r"\b(hair|curls?|mane|mop|waves|locks|flat-top|"
                         r"taper|buzz\w*|topknot|fringe|hairline|"
                         r"widow's peak|cowlick)\b", t, re.I):
            falhas.append("REFS %s: o narrador tem de ter CABELO descrito — e' "
                          "metade do contraste contra a vitima careca" % r["id"])
    for v in VITIMAS:
        t = " ".join(str(x) for x in v.values())
        for rx, rot in ((_CALVO, "careca"), (_PELO, "bigode"),
                        (_OCULOS, "oculos")):
            if not rx.search(t):
                falhas.append("VITIMAS %s: sem %s — os TRES sao travados "
                              "(PE9/F4b)" % (v["id"], rot))

    # -- 4. AS PALAVRAS PROIBIDAS NOS DOIS POOLS DE ROSTO ------------------
    for nome, pool in (("REFS", REFS), ("VITIMAS", VITIMAS)):
        for e in pool:
            t = " ".join(str(x) for x in e.values()).lower()
            for p in _APROVACAO:
                if p in t:
                    falhas.append("%s %s: %r empurra PARA a celebridade — o "
                                  "lugar dele e' geometria, nao aprovacao"
                                  % (nome, e["id"], p))
            for p in _MENDIGO:
                if p in t:
                    falhas.append("%s %s: %r vira mendigo e mata a "
                                  "credibilidade" % (nome, e["id"], p))
            for p in _DENTE:
                if p in t:
                    falhas.append("%s %s: ancora de dente (%r) contradiz o "
                                  "`front teeth even, white and complete` do "
                                  "BLOCO 0 — CL25" % (nome, e["id"], p))
            if re.search(r"\b(white|black|hispanic|latino|asian) (american )?"
                         r"(man|men|male)\b", t):
                falhas.append("%s %s: etnia dentro do pool — quem injeta e' o "
                              "ETNIA[pagina] (congruencia com o avatar)"
                              % (nome, e["id"]))
    # + 2026-08-13 — O POOL `MULHERES` ENTROU NA VARREDURA. Ele descreve GENTE
    # (a mulher do payoff, o unico rosto FELIZ do video) e estava de fora desta
    # lente desde sempre. ⚠️ So' se descobriu porque o irmao `pee_short` ganhou
    # autoteste nesta data e pegou la' duas entradas com `deeply lined`,
    # `sun-weathered` e `a thin scar` que ESTE gate deixava passar — as mesmas
    # entradas, nos dois arquivos. Lente que cobre um pool e nao o vizinho e'
    # como nao ter lente no vizinho.
    # ⚠️ `MULHERES` nao tem `id` (o pool nasceu assim e renomear chave nao e'
    # assunto desta passada), entao o rotulo e' o indice + a idade.
    for i, e in enumerate(MULHERES):
        rot = "#%d (%d anos)" % (i, e["idade"])
        t = " ".join(str(x) for x in e.values()).lower()
        for p in _MENDIGO + _APROVACAO + _DENTE:
            if p in t:
                falhas.append("MULHERES %s: %r — DISTINTIVO, NUNCA "
                              "DETERIORADO / geometria, nunca aprovacao"
                              % (rot, p))

    # -- 5. LOCAIS — CAMPOS, E OS DOIS QUE ENTRAM EM TEXTO MONTADO ---------
    for l in LOCAIS:
        for k in ("cenario", "detalhe", "plateia", "plateia_evento", "eco",
                  "luz", "audio"):
            if not l.get(k):
                falhas.append("LOCAIS %s: sem %r" % (l["id"], k))
        if not l["plateia_evento"].startswith("that "):
            falhas.append("LOCAIS %s: `plateia_evento` tem de comecar com "
                          "`that ` — o `_aqui` troca por `this ` e sem o "
                          "prefixo a fala sai com o deitico errado" % l["id"])
        # `the blurred %s keep laughing` — substantivo plural NU
        if re.match(r"(the|a|an) ", l["plateia"]):
            falhas.append("LOCAIS %s: `plateia` com artigo — o TAKE 01 monta "
                          "`the blurred %%s keep laughing` e sairia `the "
                          "blurred the ...`" % l["id"])
        if l["id"] not in PT_LOCAL:
            falhas.append("LOCAIS %s: sem rotulo em PT_LOCAL — o resumo da "
                          "janela cai no fallback e mente em silencio" % l["id"])

    # -- 6. OS SORTEIOS -----------------------------------------------------
    rng = random.Random(20260810)
    erros = collections.Counter()
    estouros = []
    celebs = []
    for i in range(n):
        pag = sorted(ETNIA)[i % len(ETNIA)]
        travas = {}
        # ⛔⛔ O MODO FORTE SO' E' EXERCITADO SE ESTIVER DECLARADO LIGADO — e,
        # se estiver, ele passa a ser COBRADO pelo PE9 como qualquer outro
        # narrador. E' o guarda que sustenta a decisao de 2026-08-10 de
        # desliga-lo: no dia em que alguem trocar o `MODO_FORTE` para True, o
        # autoteste reprova enquanto o `sc.REFS_FORTES` tiver barba e 26-38
        # anos, em vez de deixar o defeito voltar em silencio.
        if MODO_FORTE and i % 4 == 1:
            travas["forte"] = True
        if i % 4 == 2:
            travas["bela"] = True
        spec = sortear(pag, rng, {}, travas)
        blocos = montar(spec)
        # ⛔ O PE9 VALE PARA O NARRADOR QUE ENTRAR EM QUADRO, venha ele do pool
        # deste arquivo ou do pool compartilhado do MODO FORTE. A lente olha o
        # `marca` MONTADO, e nao o pool — foi por olhar so' o pool que a barba
        # do `sc.REFS_FORTES` chegou ao roteiro sem ninguem ver.
        _m = str(spec["ref"].get("marca", ""))
        if _PELO.search(_m) or _OCULOS.search(_m) or _CALVO.search(_m):
            falhas.append("narrador sorteado viola o PE9 (%s): %r"
                          % ("MODO FORTE" if travas.get("forte") else "pool",
                             _m[:60]))
        for nivel, msg in lint(spec, blocos):
            if nivel == "ERRO":
                erros[msg[:70]] += 1
        for j, fala in enumerate(spec["falas"], 1):
            if _palavras(fala) > TETO_FALA[j]:
                estouros.append((j, _palavras(fala), fala))
        for k, txt in blocos.items():
            m = _CELEB.search(txt)
            if m and len(celebs) < 3:
                celebs.append((k, m.group(0)))
        # ⛔⛔ A PLATEIA TEM DE SER A MESMA GENTE NA IMAGE E NO TAKE.
        # Este controle nasceu do defeito real: a `PLATEIA_IMAGE` tinha
        # `shoppers` cravado e o TAKE lia `loc["plateia"]`, entao o prompt
        # descrevia duas plateias diferentes para o mesmo quadro. Contradicao
        # dentro do prompt e' onde o gerador inventa um terceiro (as duas
        # colheres). ⚠️ O controle olha os BLOCOS MONTADOS, nao os pools —
        # o defeito morava na montagem, e um teste de pool nao o veria.
        p = spec["local"]["plateia"]
        if ("four blurred %s standing" % p) not in blocos["IMAGE 01/02"]:
            falhas.append("IMAGE 01/02 nao traz a plateia %r do local %s"
                          % (p, spec["local"]["id"]))
        if ("the blurred %s keep laughing" % p) not in blocos["TAKE 01/02"]:
            falhas.append("TAKE 01/02 nao traz a plateia %r do local %s"
                          % (p, spec["local"]["id"]))
    for msg, c in erros.most_common():
        falhas.append("linter reprovou %d/%d sorteios: %s" % (c, n, msg))
    for j, w, f in estouros[:3]:
        falhas.append("cena %d com %d palavras (teto %d): %s"
                      % (j, w, TETO_FALA[j], f[:70]))
    for k, tok in celebs:
        falhas.append("bloco %s diz %r — o silencio vence a negacao, e o "
                      "operador proibiu o token nominalmente" % (k, tok))

    # -- 7. O HOOK COM CADA LOCAL, PALAVRA POR PALAVRA ---------------------
    # ⛔ Local novo entra na FALA pelo `{evento}` sem pedir licenca. Um
    # `plateia_evento` que leia mal (`in this gate`) so' apareceria no render.
    for l in LOCAIS:
        ev = _aqui(l["plateia_evento"])
        if not ev.startswith("this "):
            falhas.append("LOCAIS %s: o `_aqui` nao converteu (%r)"
                          % (l["id"], ev))
        for h in HOOKS:
            fala = h.format(evento=ev, o="Johnson")
            if _palavras(fala) > TETO_FALA[1]:
                falhas.append("LOCAIS %s + hook de %d palavras estoura o teto "
                              "%d: %s" % (l["id"], _palavras(fala),
                                          TETO_FALA[1], fala[:70]))
                break

    # -- 8. A ANTI-REPETICAO, MEDIDA -----------------------------------------
    # ⭐ E' ESTE o numero que responde a queixa do operador. Nao "o pool
    # dobrou": 60 sorteios seguidos da MESMA pagina, ledger ligado, e a
    # pergunta e' quantas vezes o mesmo rosto ou o mesmo lugar reaparece
    # dentro da janela que deveria proteger.
    rng2 = random.Random(4242)
    led = {}
    vistos = {"local": [], "ref": [], "vitima": []}
    janelas = {"local": 6, "ref": 8, "vitima": 6}
    for _ in range(60):
        s = sortear("joe", rng2, led)
        for eixo, chave in (("local", "local"), ("ref", "ref"),
                            ("vitima", "vitima")):
            novo = s[chave]["id"]
            if novo in vistos[eixo][-janelas[eixo]:]:
                falhas.append("%s %r repetiu dentro da janela de %d — o "
                              "ledger nao esta' protegendo o eixo"
                              % (eixo, novo, janelas[eixo]))
            vistos[eixo].append(novo)
        _anotar(led, s)
    for eixo, seq in sorted(vistos.items()):
        print("  %-8s 60 sorteios, %d rostos/lugares distintos, o mais "
              "frequente saiu %dx"
              % (eixo, len(set(seq)), collections.Counter(seq).most_common(1)[0][1]))

    if falhas:
        print("\nSELF-TEST REPROVADO (%d falha(s)):" % len(falhas))
        for f in falhas:
            print("   " + f)
        return 1
    print("\nAUTOTESTE OK — %d sorteios, %d locais, %d narradores, %d vitimas."
          % (n, len(LOCAIS), len(REFS), len(VITIMAS)))
    return 0


def main():
    ap = argparse.ArgumentParser(description=TITULO)
    ap.add_argument("--pagina", choices=sorted(ETNIA), default="joe")
    ap.add_argument("--n", type=int, default=1)
    ap.add_argument("--seed", type=int)
    ap.add_argument("--forte", action="store_true", help="MODO FORTE ligado")
    ap.add_argument("--bela", action="store_true", help="MODO BELA ligado")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--autoteste", action="store_true")
    a = ap.parse_args()

    if a.autoteste:
        return autoteste()

    led = _carregar_ledger()
    rng = random.Random(a.seed)
    travas = {}
    if a.forte:
        travas["forte"] = True
    if a.bela:
        travas["bela"] = True
    for _ in range(a.n):
        s = sortear(a.pagina, rng, led, travas)
        b = montar(s)
        print("=" * 70)
        print(resumo_pt(s))
        print("=" * 70)
        for k in sorted(b):
            print("\n%s\n" % b[k])
        for nivel, msg in lint(s, b):
            print("[%s] %s" % (nivel, msg))
        if not a.dry_run:
            _gravar_ledger(led, s)
    return 0


if __name__ == "__main__":
    sys.exit(main())
