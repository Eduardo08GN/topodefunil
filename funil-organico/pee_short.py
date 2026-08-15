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

import os
import re
import sys
from types import SimpleNamespace

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import short_comum as sc                                        # noqa: E402

from nucleo_sonoro import sonorizar                             # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(AQUI, ".pee-short-ledger.json")

TITULO = "AGENTE PEE SHORT"
SUBTITULO = "a mancha pública, em 3 cenas · gerador offline de prompts Veo"
SLUG = "pee-short"


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
# ⛔⛔ O SUBSTANTIVO DA PLATEIA VIROU `%s` EM 2026-08-13 — era `shoppers`
# cravado, e o TAKE 01 sempre leu `loc["plateia"]`. Ou seja: o mesmo quadro era
# descrito com DUAS plateias diferentes dentro do mesmo prompt (`four blurred
# shoppers` na IMAGE, `the blurred bidders keep laughing` no TAKE). Contradicao
# dentro do prompt e' exatamente onde o gerador inventa um terceiro — e' o
# mecanismo das DUAS COLHERES que o operador pegou no render em 2026-08-10.
# ⚠️ O defeito era invisivel enquanto quase todo local tinha plateia
# `shoppers`/`customers`; com os 27 locais desta data (bidders, commuters,
# guests, neighbors, bowlers) ele apareceria em quase todo video. Ampliar pool
# sem consertar isto teria PIORADO o motor.
# ⭐ O irmao `pee16_short.py` ja' fez esta correcao em 2026-08-10; aqui ela
# chegou junto com os pools. A ordem do operador (plateia RI e APONTA, quatro
# figurantes desfocados) esta' intacta caractere por caractere — o que mudou
# foi de ONDE vem o substantivo, e ele passou a vir de onde ja' vinha no TAKE.
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
# ⛔ A negacao anti-celebridade saiu daqui em 2026-08-14, por ordem do operador
# (*"tire not a celebrity do prompt"*): declaracao INJETA o token que ela nega.
# A metade positiva ficou. Ver CLAUDE.md §"CONTRA A CELEBRIDADE, SILENCIO".
ANTICELEB = "Ordinary relatable face."
CAUDA = "iPhone shot, natural grain, no text, no watermark."

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
# ⭐⭐ 2026-08-13 — OS CINCO POOLS ABAIXO (LOCAIS, AMBIENTES, REFS, VITIMAS,
# MULHERES) SAO COPIA LITERAL DO IRMAO `pee16_short.py`, comentarios inclusive.
# ===========================================================================
# ⛔ MOTIVO: os dois motores nasceram por copia literal e tinham DIVERGIDO —
# o 16s recebeu duas ampliacoes (2026-08-10) e a reforma anti-celebridade do
# pool REFS, e este aqui ficou onde estava: 9 locais contra 21, 13 narradores
# de UMA linha de cabelo contra 24 com arquitetura facial, 12 vitimas contra
# 20. Dois arquivos com o mesmo nome de pool e conteudo diferente e' pior que
# um pool pequeno: ninguem sabe qual e' a fonte da verdade. Ordem do operador
# nesta data: *"melhore a aparencia e shape desses homens"* / *"aumente o pool
# de opcoes substancialmente, tambem dos ambientes"* — e a forma de cumprir nos
# dois sem criar uma terceira versao e' nivelar POR CIMA.
#
# ⚠️ DUAS COISAS QUE OS COMENTARIOS COPIADOS DIZEM E QUE AQUI SAO DIFERENTES —
# esta' escrito aqui para ninguem "consertar" o codigo pelo comentario:
#   1. o comentario de LOCAIS fala do `_aqui` (`that store` -> `this store`).
#      Esse helper e' do 16s, onde o narrador esta' DENTRO do lugar. Este motor
#      passa o `plateia_evento` DIRETO para o hook (`... in that store`), o que
#      torna o prefixo `that ` ainda mais obrigatorio, nao menos.
#   2. o comentario de REFS diz que o narrador e a vitima entraram no ledger.
#      Isso e' verdade no 16s; aqui os dois continuam em `rng.choice` puro. E'
#      divida conhecida e NAO foi mexida nesta passada — sorteio e' maquinaria,
#      e a ordem do dia era pool.
# ⚠️ Onde o comentario copiado fala em "autoteste", vale o desta data: este
# arquivo ganhou o seu proprio no fim do arquivo (`--autoteste`).
# ===========================================================================

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

NUCLEO = ["Johnson", "pecker", "wiener", "tool", "soldier"]

# PE6 ⭐ — a regra mais importante do agente. O hook LIGA o mijo ao orgao NA
# MESMA FALA. Hook so' de mijo REPROVA: o homem com ED nao se reconhece, acha
# que o assunto e' bexiga e rola. Estrutura obrigatoria:
#   fato do mijo + aparte + orgao nomeado + VINCULO afirmado
VINCULOS = ["same thing", "same reason", "and that's why"]

HOOKS = [
    "He peed himself in {evento} because he couldn't hold it in. Poor guy... same thing killed his {o} two years ago.",
    "He wet his pants in {evento} and everybody saw. Poor guy... same reason his {o} quit on him.",
    "He soaked right through in {evento}. Poor guy... same thing that made him leak is why his {o} doesn't work.",
    "He lost it right there in {evento}. Poor guy... and that's why his {o} hasn't worked in two years.",
    "He wet his pants in {evento}. His wife wasn't even surprised. Same reason his {o} stopped working two years back.",
    "He peed his pants in {evento}. His brother in law still tells that story. Same thing shut his {o} down.",
    "He soaked his pants in {evento}. His wife stopped reaching for him two years ago. Same reason his {o} plays dead.",
    "She said it was fine when he peed in {evento}. She says that in bed too. Same reason his {o} quit.",
    "He leaked down his leg in {evento}. Hasn't asked a woman out since the divorce. Same reason his {o} stays down.",
    "He started leaking in {evento}. His wife already told her friends about it. Same reason his {o} does nothing.",
    "He peed right there in {evento}. That was me in 2019. Same reason my {o} went out that year.",
    "He peed in {evento} today. I did the same in 2019. Every man I know has. Same thing took our {o}.",
    # + 2026-08-01: o operador mediu vicio — os mesmos hooks voltando no lote.
    # Pool ampliado; todos mantem mijo + orgao + vinculo na mesma fala (PE6).
    "Everybody laughed when he leaked through his pants in {evento}. Same reason his {o} quit.",
    "A grown man peed himself in {evento} on a Tuesday. Same thing that took his {o}.",
    "Know why a man peed himself in {evento}? Same reason his {o} hasn't worked since.",
    "His wife walked him out of {evento} soaked. Same reason she stopped touching his {o}.",
    "His doctor blamed the coffee when he peed in {evento}. Same thing had already taken his {o}.",
    "They still talk about the man who soaked his pants in {evento}. Same reason his {o} stopped answering.",
    "He lost it standing in {evento}, and that's why his {o} has been dead two years.",
    "He won't be the last man to get soaked in {evento}. Same thing that shut his {o} down.",
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
    "Comment gelatin, tonight — somebody always reports this. I'll send the recipe before it goes down. {gate}",
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
    hist = ledger.get(pagina, {})
    local = _evitando(rng, LOCAIS, hist.get("local", [])[-3:])
    roupa = _evitando(rng, ROUPAS, hist.get("roupa", [])[-2:])
    amb = _evitando(rng, AMBIENTES, hist.get("ambiente", [])[-2:])
    prop = _evitando(rng, PROPS, hist.get("prop", [])[-2:])
    # ⭐ MODOS DE REF: a REF e' o narrador (homem) e a MULHER e' quem aparece
    # no payoff. Cada um leva o seu modo.
    _tv = travas or {}
    ref = (sc.ref_forte(REFS[0], rng) if _tv.get("forte") else rng.choice(REFS))
    vit = rng.choice(VITIMAS)
    mul = (sc.ref_bela(MULHERES[0], rng) if _tv.get("bela")
           else rng.choice(MULHERES))
    # ⛔ 2026-08-10 — SO' OS TRES APELIDOS SAO SORTEAVEIS (ordem do
    # operador, parque inteiro). `soldier` e `tool` seguem no NUCLEO porque
    # as LENTES os usam para DETECTAR o orgao; o que muda e' que nao saem
    # mais na fala. Ver `short_comum.orgaos_sorteaveis`.

    orgaos = sc.orgaos_sorteaveis(rng, 4)
    hook = _hook_sem_colisao(rng, orgaos)
    falas = [
        hook.format(evento=local["plateia_evento"], o=orgaos[0]),
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
        "REF 01: Photo of a real person, a %d-year-old %s man, chest up, facing camera, "
        "calm expression. Lean muscular build, chest and shoulders visible. %s. "
        "%s %s Plain gray background, soft light. No text, no watermark."
        % (ref["idade"], et, ref["marca"].capitalize(), ref["roupa"], ANTICELEB)
    )

    b["IMAGE 01/05"] = (
        "IMAGE 01/05: Medium shot in %s, %s. Standing in the middle is a "
        "%d-year-old %s %s, wearing %s, with %s. He stands there, %s "
        "Beside him is a %d-year-old %s man with %s, %s, and %s. "
        "%s %s %s"
        % (loc["cenario"], loc["detalhe"], vit["idade"], et, vit["marca"],
           vit["camisa"], mancha, CHORO_IMAGE,
           ref["idade"], et, ref["marca"], NARRADOR_IMAGE,
           PLATEIA_IMAGE % loc["plateia"], ANTICELEB, loc["luz"], CAUDA)
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
        return rng.choice(HOOKS).format(evento=loc["plateia_evento"], o=o)
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
    ("ref", "NARRADOR", "REFS", "marca"),
    ("vitima", "VÍTIMA", "VITIMAS", "marca"),
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
MAPA = (1, 4, 3)
MAPA_COPY = (1, None, 5)          # None = a fundida
CENAS_UI = ["1 · A MANCHA", "2 · O TRUQUE + A VIRADA", "3 · CTA PREPARANDO"]

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
MODO_FORTE = True

TETO_FALA = {1: TETO_FALA_LONGO[1], 2: 25, 3: TETO_FALA_LONGO[5]}


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


def _fundir(spec, rng):
    o = sc.orgao_de(_LONGO, spec["falas_base"][3])
    # ⛔ 2026-08-05 — a fundida cede ao teto. Era `rng.choice(FUNDIDAS)`
    # cru e 73% dos sorteios da cena 2 passavam de 25 palavras.
    # ⚠️ Fallback na entrada mais CURTA, nunca `or FUNDIDAS`.
    cabem = [x for x in FUNDIDAS if _palavras(x.format(o=o)) <= TETO_FALA[2]]
    esc = (rng.choice(cabem) if cabem
           else min(FUNDIDAS, key=lambda x: _palavras(x.format(o=o))))
    return esc.format(o=o)


# ---------------------------------------------------------------------------
# CONTRATO DO MOTOR
# ---------------------------------------------------------------------------

def _carregar_ledger():
    import json
    if os.path.exists(LEDGER):
        with open(LEDGER, encoding="utf-8-sig") as f:
            return json.load(f)
    return {}


def _gravar_ledger(ledger, spec):
    import json
    p = ledger.setdefault(spec["pagina"], {})
    for eixo, val in (("local", spec["local"]["id"]),
                      ("roupa", spec["roupa"]["id"]),
                      ("ambiente", spec["ambiente"]["id"]),
                      ("prop", spec["prop"]["id"])):
        p.setdefault(eixo, []).append(val)
        p[eixo] = p[eixo][-12:]
    with open(LEDGER, "w", encoding="utf-8") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)


def sortear(pagina, rng, ledger, travas=None):
    return sc.sortear_curto(_LONGO, pagina, rng, ledger, MAPA, _fundir,
                            MAPA_COPY, travas)


def montar(spec):
    b = sc.montar_curto(_LONGO, spec, MAPA)
    # a cena 3 e' a unica que nao vem pronta do base — ver o comentario
    # do MAPA e a docstring de short_comum.bancada_com_rosto
    # ⚠️ DUAS cenas nao vem prontas do base, e as duas por ordem do
    # operador: a 2, para o narrador nao sumir no terco do meio; e a 3,
    # para o rosto aparecer enquanto prepara. As duas recombinam blocos
    # validados — ver as docstrings em short_comum.
    i2, t2 = sc.redencao_com_ref(_LONGO, spec, spec["falas"][1])
    b["IMAGE 02/03"], b["TAKE 02/03"] = i2, t2
    i3, t3 = sc.bancada_com_rosto(_LONGO, spec, spec["falas"][2])
    b["IMAGE 03/03"], b["TAKE 03/03"] = i3, t3
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
    # ⚠️ a plateia entra FORMATADA (`PLATEIA_IMAGE % ...`): comparar com o
    # template cru (`four blurred %s ...`) reprovaria 100% dos sorteios, que e'
    # a lente contra o proprio template (licoes §16).
    for s, rot in ((CHORO_IMAGE, "choro PE2"),
                   (NARRADOR_IMAGE, "narrador PE3"),
                   (PLATEIA_IMAGE % spec["local"]["plateia"], "plateia PE4")):
        if s not in i1:
            achados.append(("ERRO", "a cena da mancha sem a string travada: %s" % rot))
    # a cena do payoff virou a 2 do SHORT, mas a trava do prop e' a mesma
    if "motionless" not in sc.bloco_base(blocos, MAPA, "TAKE", 4).lower():
        achados.append(("ERRO", "o TAKE do payoff sem declaracao de imobilidade "
                                "do prop"))


def lint(spec, blocos):
    return sc.lint_curto(
        _LONGO, spec, blocos, MAPA, TETO_FALA,
        literais=("gelatin trick", "prostate"),
        extras=(_pe6_hook, _pe1_roupa_clara, _blocos_travados))


# ---------------------------------------------------------------------------
# RESUMO
# ---------------------------------------------------------------------------

def resumo_pt(spec):
    et = "branca" if "white" in ETNIA[spec["pagina"]] else "negra"
    return ("%s, a mancha escura na calça dele com a plateia em volta. Na cena "
            "2 vem o truque e a virada, e na 3 o CTA. Três cenas, elenco de "
            "pele %s."
            % (PT_LOCAL.get(spec["local"]["id"], "No local"), et))


# ---------------------------------------------------------------------------
# AUTOTESTE — 2026-08-13
# ---------------------------------------------------------------------------
# ⛔⛔ ESTE MOTOR NAO TINHA NENHUM. Nem `__main__`, nem `--autoteste`: ele so'
# existia por dentro do app. Consequencia pratica — a ampliacao de pool desta
# data (9 locais -> 27, 13 narradores -> 24, 12 vitimas -> 20, 16 mulheres ->
# 24, 10 ambientes -> 20) NAO TERIA COMO SER MEDIDA, e aceite e' MEDICAO, nunca
# relato (licoes-de-construcao, corolario do §1). Pool novo que quebra a
# montagem so' apareceria no dia em que alguem abrisse o app e sorteasse por
# acaso o local errado.
#
# ⭐ O QUE ELE COBRA, e cada item existe por um defeito ja' pago neste repo:
#   1. id unico por pool ................. o `_evitando` compara por id
#   2. janela do ledger cabe no pool ..... janela >= pool zera a memoria em
#                                          silencio: nada quebra, so' repete
#   3. PE9/F4b por CONSTRUCAO ............ narrador com cabelo e sem oculos/
#                                          pelo/calvicie; vitima com os tres
#   4. rosto DISTINTIVO, NUNCA DETERIORADO  a lista de 2026-08-13 do operador
#   5. aprovacao e celebridade no pool ... as duas empurram PARA a celebridade
#   6. campos de LOCAIS e AMBIENTES ...... cada chave cai num ponto diferente
#                                          da frase montada
#   7. 400 sorteios: linter sem ERRO, teto de fala, plateia coerente entre
#      IMAGE e TAKE, e o hook lido com CADA `plateia_evento`
#   8. anti-repeticao MEDIDA em 60 sorteios seguidos da mesma pagina
#
# ⚠️ O QUE ELE **NAO** COBRA, e esta' escrito para nao virar falso verde:
#   · a clausula `not a celebrity` do `ANTICELEB` continua nos blocos montados
#     deste motor. E' divida DECLARADA do repo (CLAUDE.md: ~41 motores ainda a
#     carregam) e tira-la muda o prompt de todo video — alcada do operador, nao
#     minha. Por isso a varredura de celebridade aqui olha os POOLS, que sao o
#     que esta passada mexeu, e nao os blocos.
#   · o ledger deste motor nao guarda `ref` nem `vitima` (o irmao 16s guarda).
#     E' maquinaria de sorteio e ficou intacta.
# ---------------------------------------------------------------------------

# tokens que pertencem a' VITIMA e nao podem vazar para o pool do narrador
_OCULOS = re.compile(r"\b(glasses|spectacles|bifocal\w*|readers|shades|lenses|"
                     r"rimless|half-?rim|half-?moon|wire-?rimmed|wire-?frame\w*|"
                     r"sunglasses|clip-?on)\b", re.I)
_PELO = re.compile(r"\b(beard\w*|mustache\w*|moustache\w*|goatee|stubble|"
                   r"sideburns|muttonchop\w*|clean-?shaven|whiskers|"
                   r"chin.?strap|chevron|walrus)\b", re.I)
_CALVO = re.compile(r"\b(bald\w*|shaved head|balding)\b", re.I)


def _pelo_no_narrador(txt):
    """`_PELO` menos `clean-shaven` — a AUSENCIA de barba nao e' barba.

    ⚠️ O `_PELO` serve a DOIS usos opostos: na VITIMA ele cobra PRESENCA de
    bigode, e ali `clean-?shaven` tem de casar (uma vitima "clean-shaven"
    estaria errada e o token acusa). No NARRADOR ele cobra AUSENCIA — e a
    palavra `clean-shaven` descreve exatamente o estado CERTO. Sem esta
    peneira a lente reprova o narrador por estar barbeado, que e' o cumulo da
    lente contra o proprio contrato (licoes §16).
    """
    return _PELO.search(re.sub(r"clean-?shaven", "", txt, flags=re.I))


# ⛔ empurram PARA a celebridade (adjetivo de aprovacao no lugar de geometria)
_APROVACAO = ("handsome", "chiseled", "distinguished", "piercing eyes",
              "strong jaw", "rugged good-looking")
# ⛔ negacao de conformidade DENTRO DO POOL — declaracao e' municao
_CELEB_POOL = re.compile(r"\b(celebrity|celebrities|famous|movie star|"
                         r"look-?alike)\b", re.I)
# ⛔ DISTINTIVO, NUNCA DETERIORADO — lista do operador, 2026-08-13:
# *"melhore a aparencia e shape desses homens"*. ⚠️ `worn` cru NAO entra: ali
# ele e' o verbo VESTIR (`hair worn long on top`) e reprovaria entrada certa —
# lente que reprova o que esta' certo ensina a ignorar a lente (licoes §16).
_MENDIGO = ("gaunt", "bony", "leathery", "weather-beaten", "chipped tooth",
            "drooping eyelid", "broken capillaries", "frayed", "patchy",
            "toothless", "unkempt", "scar", "sun damage", "sun-damaged",
            "weathered", "ruddy", "thin skin", "loose skin", "age spot",
            "sun-spotted", "liver-spotted", "sunken", "hollow cheek",
            "deeply lined", "deep lines", "creased", "worn-out", "careworn",
            "torn ", "missing tooth", "gap between")


def _anotar(ledger, spec):
    """O `_gravar_ledger` sem tocar em disco — o autoteste nao suja o ledger."""
    p = ledger.setdefault(spec["pagina"], {})
    for eixo, val in (("local", spec["local"]["id"]),
                      ("roupa", spec["roupa"]["id"]),
                      ("ambiente", spec["ambiente"]["id"]),
                      ("prop", spec["prop"]["id"])):
        p.setdefault(eixo, []).append(val)
        p[eixo] = p[eixo][-12:]


def autoteste(n=400):
    import collections
    import random
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
            falhas.append("%s: id repetido %s" % (nome, dup))

    # -- 2. A JANELA DO LEDGER TEM DE CABER NO POOL ------------------------
    # ⚠️ as janelas sao as do `_sortear_longo` DESTE motor (3/2/2/2), que sao
    # menores que as do irmao 16s. Numero copiado de la' mentiria.
    for nome, pool, janela in (("LOCAIS", LOCAIS, 3), ("ROUPAS", ROUPAS, 2),
                               ("AMBIENTES", AMBIENTES, 2), ("PROPS", PROPS, 2)):
        if janela >= len(pool):
            falhas.append("%s: janela %d >= pool %d — o `_evitando` cai no pool "
                          "inteiro e a memoria nao serve para nada"
                          % (nome, janela, len(pool)))

    # -- 3. PE9/F4b — O CONTRASTE DE 3 EIXOS, POR CONSTRUCAO ---------------
    for r in REFS:
        t = " ".join(str(v) for v in r.values())
        if _OCULOS.search(t):
            falhas.append("REFS %s: oculos no narrador — e' um dos 3 eixos da "
                          "VITIMA (PE9/F4b)" % r["id"])
        if _pelo_no_narrador(t):
            falhas.append("REFS %s: pelo facial no narrador — idem" % r["id"])
        if _CALVO.search(t):
            falhas.append("REFS %s: calvicie no narrador — idem" % r["id"])
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

    # -- 4. AS PALAVRAS PROIBIDAS NOS TRES POOLS DE GENTE ------------------
    for nome, pool in (("REFS", REFS), ("VITIMAS", VITIMAS),
                       ("MULHERES", MULHERES)):
        for i, e in enumerate(pool):
            rot = e.get("id", "#%d" % i)
            t = " ".join(str(x) for x in e.values()).lower()
            for p in _APROVACAO:
                if p in t:
                    falhas.append("%s %s: %r empurra PARA a celebridade — o "
                                  "lugar dele e' geometria, nao aprovacao"
                                  % (nome, rot, p))
            for p in _MENDIGO:
                if p in t:
                    falhas.append("%s %s: %r vira mendigo e mata a "
                                  "credibilidade (DISTINTIVO, NUNCA "
                                  "DETERIORADO)" % (nome, rot, p))
            if _CELEB_POOL.search(t):
                falhas.append("%s %s: fala de celebridade dentro do pool — o "
                              "silencio vence a negacao" % (nome, rot))
            if re.search(r"\b(white|black|hispanic|latino|asian) (american )?"
                         r"(man|men|male|woman|women)\b", t):
                falhas.append("%s %s: etnia dentro do pool — quem injeta e' o "
                              "ETNIA[pagina] (congruencia com o avatar)"
                              % (nome, rot))

    # -- 5. OS CAMPOS QUE CAEM DENTRO DE TEXTO MONTADO ---------------------
    for l in LOCAIS:
        for k in ("cenario", "detalhe", "plateia", "plateia_evento", "eco",
                  "luz", "audio"):
            if not l.get(k):
                falhas.append("LOCAIS %s: sem %r" % (l["id"], k))
        if not l["plateia_evento"].startswith("that "):
            falhas.append("LOCAIS %s: `plateia_evento` tem de comecar com "
                          "`that ` — o hook monta `... in {evento}`" % l["id"])
        if not l["eco"].startswith("the same "):
            falhas.append("LOCAIS %s: `eco` tem de comecar com `the same ` — a "
                          "REDENCAO monta `walked back into {eco}`" % l["id"])
        # `the blurred %s keep laughing` — substantivo plural NU
        if re.match(r"(the|a|an) ", l["plateia"]):
            falhas.append("LOCAIS %s: `plateia` com artigo — o TAKE 01 sairia "
                          "`the blurred the ...`" % l["id"])
        if l["id"] not in PT_LOCAL:
            falhas.append("LOCAIS %s: sem rotulo em PT_LOCAL — o resumo cai no "
                          "fallback e mente em silencio" % l["id"])
    for a in AMBIENTES:
        for k in ("set", "bancada", "curto", "luz"):
            if not a.get(k):
                falhas.append("AMBIENTES %s: sem %r" % (a["id"], k))
        if not a["luz"].endswith("."):
            falhas.append("AMBIENTES %s: `luz` sem ponto final — ela entra "
                          "capitalizada como frase inteira na IMAGE 02"
                          % a["id"])
        if a["luz"][:1].isupper():
            falhas.append("AMBIENTES %s: `luz` comecando em maiuscula — ela "
                          "tambem entra minuscula depois de virgula na IMAGE "
                          "03/04" % a["id"])
        if re.match(r"(the|a|an) ", a["bancada"]):
            falhas.append("AMBIENTES %s: `bancada` com artigo — a IMAGE 02 "
                          "monta `stands behind the <bancada>`" % a["id"])

    # -- 6. OS SORTEIOS -----------------------------------------------------
    rng = random.Random(20260813)
    erros = collections.Counter()
    estouros = []
    pend_forte = []
    pend_teto = collections.Counter()
    for i in range(n):
        pag = sorted(ETNIA)[i % len(ETNIA)]
        travas = {}
        if MODO_FORTE and i % 4 == 1:
            travas["forte"] = True
        if MODO_BELA and i % 4 == 2:
            travas["bela"] = True
        spec = sortear(pag, rng, {}, travas)
        blocos = montar(spec)
        # ⛔ O PE9 vale para o narrador QUE ENTRA EM QUADRO, venha ele do pool
        # deste arquivo ou do pool compartilhado do MODO FORTE. A lente olha o
        # `marca` MONTADO, e nao o pool — foi por olhar so' o pool que a barba
        # do `sc.REFS_FORTES` chegou ao roteiro de outro motor sem ninguem ver.
        _m = str(spec["ref"].get("marca", ""))
        if _pelo_no_narrador(_m) or _OCULOS.search(_m) or _CALVO.search(_m):
            if travas.get("forte"):
                pend_forte.append(_m[:60])   # PENDENCIA B — ver o rodape
            else:
                falhas.append("narrador sorteado viola o PE9 (pool): %r"
                              % _m[:60])
        for nivel, msg in lint(spec, blocos):
            if nivel == "ERRO":
                erros[msg[:70]] += 1
        for j, fala in enumerate(spec["falas"], 1):
            if _palavras(fala) > TETO_FALA[j]:
                if j == 3:
                    pend_teto[fala] += 1     # PENDENCIA A — ver o rodape
                else:
                    estouros.append((j, _palavras(fala), fala))
        # ⛔⛔ A PLATEIA TEM DE SER A MESMA GENTE NA IMAGE E NO TAKE — foi o
        # defeito consertado nesta data (o `shoppers` cravado no
        # PLATEIA_IMAGE). O controle olha os BLOCOS MONTADOS, nao os pools: o
        # defeito morava na montagem e um teste de pool nao o veria.
        p = spec["local"]["plateia"]
        i1 = sc.bloco_base(blocos, MAPA, "IMAGE", 1)
        t1 = sc.bloco_base(blocos, MAPA, "TAKE", 1)
        if ("four blurred %s standing" % p) not in i1:
            falhas.append("IMAGE da mancha nao traz a plateia %r do local %s"
                          % (p, spec["local"]["id"]))
        if ("the blurred %s keep laughing" % p) not in t1:
            falhas.append("TAKE da mancha nao traz a plateia %r do local %s"
                          % (p, spec["local"]["id"]))
    for msg, c in erros.most_common():
        falhas.append("linter reprovou %d/%d sorteios: %s" % (c, n, msg))
    for j, w, f in estouros[:3]:
        falhas.append("cena %d com %d palavras (teto %d): %s"
                      % (j, w, TETO_FALA[j], f[:70]))

    # -- 7. O HOOK COM CADA LOCAL, PALAVRA POR PALAVRA ---------------------
    # ⛔ Local novo entra na FALA pelo `{evento}` sem pedir licenca. Um evento
    # comprido so' apareceria como fala cortada no render.
    for l in LOCAIS:
        for h in HOOKS:
            fala = h.format(evento=l["plateia_evento"], o="Johnson")
            if _palavras(fala) > TETO_FALA[1]:
                falhas.append("LOCAIS %s + hook de %d palavras estoura o teto "
                              "%d: %s" % (l["id"], _palavras(fala),
                                          TETO_FALA[1], fala[:70]))
                break

    # -- 8. A ANTI-REPETICAO, MEDIDA ----------------------------------------
    # ⭐ E' este numero que responde "o pool aumentou?" — nao a contagem de
    # entradas. 60 sorteios seguidos da mesma pagina, com o ledger ligado.
    rng2 = random.Random(4242)
    led = {}
    vistos = {"local": [], "ambiente": []}
    janelas = {"local": 3, "ambiente": 2}
    for _ in range(60):
        s = sortear("joe", rng2, led)
        for eixo in vistos:
            novo = s[eixo]["id"]
            if novo in vistos[eixo][-janelas[eixo]:]:
                falhas.append("%s %r repetiu dentro da janela de %d — o ledger "
                              "nao esta' protegendo o eixo"
                              % (eixo, novo, janelas[eixo]))
            vistos[eixo].append(novo)
        _anotar(led, s)
    for eixo, seq in sorted(vistos.items()):
        print("  %-10s 60 sorteios, %d distintos, o mais frequente saiu %dx"
              % (eixo, len(set(seq)),
                 collections.Counter(seq).most_common(1)[0][1]))
    # ⚠️ ref e vitima entram SEM ledger neste motor (divida declarada, ver o
    # cabecalho) — o numero e' impresso mesmo assim, porque o que nao se mede
    # volta.
    rng3 = random.Random(99)
    caras = [sortear("joe", rng3, {})["ref"]["id"] for _ in range(60)]
    print("  %-10s 60 sorteios, %d distintos, o mais frequente saiu %dx  "
          "(sem ledger — divida declarada)"
          % ("ref", len(set(caras)),
             collections.Counter(caras).most_common(1)[0][1]))

    # -- 9. AS DUAS PENDENCIAS DECLARADAS -----------------------------------
    # ⛔⛔ AS DUAS SAO ANTERIORES A ESTA PASSADA e as duas caem em ALCADA DO
    # OPERADOR — por isso sao MEDIDAS E IMPRESSAS, e nao reprovam. Gate que
    # reprova o que quem roda nao pode consertar ensina a ignorar o gate
    # (licoes §16); defeito que ninguem imprime volta calado, que e' pior.
    # ⚠️ Nenhuma das duas foi criada nem agravada pela ampliacao de pools de
    # 2026-08-13: a A vive nos pools CTAS/GATES e a B no pool COMPARTILHADO do
    # short_comum, e nenhum dos tres foi tocado.
    #
    # PENDENCIA A — CTA acima do teto da cena 3.
    #   O teto da cena 3 e' o TETO_FALA_LONGO[5] = 24, e ha' combinacao de
    #   CTA + gate que fecha em 25. Ordem permanente do operador: *"sempre
    #   meca. Nao pode haver cortes de fala."* ⛔ O conserto e' CORTAR COPY, e
    #   copy e' alcada dele (nunca alterar por conta propria). O irmao 16s nao
    #   tem o problema porque la' o CTA divide a cena fundida, com teto 25.
    #
    # PENDENCIA B — MODO FORTE entrega narrador com BARBA.
    #   `sc.ref_forte` sai do pool COMPARTILHADO (`sc.REFS_FORTES`), que tem
    #   barba/cavanhaque e `a strong square jaw`. Barba no narrador quebra o
    #   PE9/F4b (e' um dos TRES eixos da vitima) e `strong jaw` esta' na lista
    #   de adjetivos que empurram PARA a celebridade. ⭐ O irmao `pee16` ja'
    #   resolveu isto em 2026-08-10 DESLIGANDO o toggle (`MODO_FORTE = False`,
    #   com a lapide escrita no arquivo dele). Aqui ele continua LIGADO, e
    #   desligar um recurso do app do operador nao e' decisao minha.
    #   ⚠️ No dia em que o toggle for desligado — ou em que o pool
    #   compartilhado ganhar entradas sem pelo facial — esta pendencia zera
    #   sozinha e a lente volta a reprovar de verdade.
    if pend_teto:
        tot = sum(pend_teto.values())
        print("\n  PENDENCIA A (declarada, nao reprova): %d/%d sorteios com a "
              "cena 3 acima do teto %d — %d CTA(s) distintos."
              % (tot, n, TETO_FALA[3], len(pend_teto)))
        for f, c in pend_teto.most_common(2):
            print("      %dx (%d palavras) %s" % (c, _palavras(f), f[:66]))
    if pend_forte:
        print("\n  PENDENCIA B (declarada, nao reprova): %d/%d sorteios com o "
              "MODO FORTE ligado entregaram narrador que viola o PE9."
              % (len(pend_forte), n))
        print("      ex.: %s" % pend_forte[0])

    if falhas:
        print("\nSELF-TEST REPROVADO (%d falha(s)):" % len(falhas))
        for f in falhas:
            print("   " + f)
        return 1
    print("\nAUTOTESTE OK — %d sorteios, %d locais, %d ambientes, %d "
          "narradores, %d vitimas, %d mulheres."
          % (n, len(LOCAIS), len(AMBIENTES), len(REFS), len(VITIMAS),
             len(MULHERES)))
    return 0


def main():
    import argparse
    import random
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
        spec = sortear(a.pagina, rng, led, travas)
        blocos = montar(spec)
        print("=" * 70)
        print(resumo_pt(spec))
        print("=" * 70)
        for k in sorted(blocos, key=lambda x: (not x.startswith("BLOCO"), x)):
            print("\n" + blocos[k])
        for nivel, msg in lint(spec, blocos):
            print("[%s] %s" % (nivel, msg))
        if not a.dry_run:
            _gravar_ledger(led, spec)
    return 0


if __name__ == "__main__":
    sys.exit(main())
