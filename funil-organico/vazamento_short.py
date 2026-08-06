#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE VAZAMENTO SHORT — 3 cenas de 8 segundos.

Motor AUTOSSUFICIENTE (2026-08-03): tudo que ele precisa mora neste arquivo.
O arco de 5 cenas continua existindo aqui dentro, como maquinaria, porque o
colapso e' construido em cima dele:

    base 1 · O VAZAMENTO        ->  SHORT 1 · O VAZAMENTO
    base 4 · MECANISMO + PROVA  ->  SHORT 2 · A RECEITA INCOMPLETA + A PROVA
    base 5 · CTA                ->  SHORT 3 · CTA

⛔ ESTE FOI O COLAPSO MAIS DELICADO DOS QUATRO
O angulo do VAZAMENTO **e'** a receita incompleta: a cena 2 dava metade da
receita (o bicarbonato) e a cena 3 revelava que sem o gelatin trick aquela
metade nao faz nada. As duas caem — ou seja, cai a isca E cai a virada, que
juntas sao o mecanismo inteiro do agente.

A copy fundida resolve as duas numa frase so': ela **introduz e revela na mesma
respiracao** ("baking soda alone does nothing without the gelatin trick"). Fica
mais apertado e, honestamente, mais direto — mas quem quiser a isca de verdade,
com o espectador anotando a receita antes da virada, usa a versao longa.

O linter trava na negacao literal `without the gelatin trick` (V6), que e' o
que impede a fundida de virar so' mais uma promessa.
"""

import os
import re
import sys
import types

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import short_comum as sc                                         # noqa: E402

from nucleo_sonoro import sonorizar                              # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(AQUI, ".vazamento-short-ledger.json")

TITULO = "AGENTE VAZAMENTO SHORT"
SUBTITULO = "o corpo-prova e a receita incompleta, em 3 cenas · prompts Veo"
SLUG = "vazamento-short"


# ===========================================================================
# ⭐ BLOCO INLINEADO DO MOTOR LONGO — 2026-08-03
# ---------------------------------------------------------------------------
# Ate' hoje este arquivo fazia `import vazamento_lucas as base` e herdava de la'
# strings travadas, pools, tabelas de banido e as tres funcoes do arco de 5
# cenas. Os `*_lucas` sao de terceiro e saem do repo de trabalho, entao o motor
# virou AUTOSSUFICIENTE: tudo que ele consumia foi copiado LITERALMENTE para
# ca', com os comentarios originais junto — eles sao a memoria de por que cada
# regra existe.
#
# ⛔ A PARTIR DE AGORA ESTE ARQUIVO E' A FONTE DA VERDADE DO ANGULO VAZAMENTO.
# Nao ha' mais motor longo para corrigir: correcao de string travada, de pool
# de copy ou de tabela de banido entra aqui.
#
# ⚠️ O QUE MUDOU DE NOME — e so' isso mudou:
#   · `TETO_FALA` do longo -> `TETO_FALA_LONGO` (5 cenas). O `TETO_FALA` deste
#     arquivo continua sendo o do SHORT (3 cenas). Sao DOIS dicionarios
#     diferentes e confundi-los troca o teto de palavra do agente inteiro.
#   · `sortear`/`montar`/`nova_fala` do longo -> `*_longo`, porque o SHORT ja'
#     tem funcoes com esses nomes. O `short_comum` recebe as tres pelo
#     `_MOTOR_LONGO` no fim deste bloco, no lugar onde recebia o modulo base.
# Nenhum texto de prompt, pool de copy, pool de personagem ou string travada
# foi tocado.
# ===========================================================================

# ---------------------------------------------------------------------------
# STRINGS TRAVADAS — copia literal da doutrina. NAO REESCREVER, NAO COMPRIMIR.
# ---------------------------------------------------------------------------

# V1 — o geoduck e' GIGANTE, MOLE e seguro com AS DUAS MAOS (ordem do operador).
# Dimensao por ESCALA CORPORAL, nunca por adjetivo (large/big sao normalizados).
GEODUCK_IMAGE = (
    "He holds a very large geoduck clam with both hands against his bare chest, "
    "gripping the pale ridged shell. Its siphon hangs straight down over his lap, "
    "completely soft and slack, as long as his forearm and as thick as his wrist, "
    "drooping under its own weight with a rounded blunt tip, pale tan, its surface "
    "dull and slightly wrinkled. No bird, no goose, no duck, no swan, no snake, no "
    "feathers, no beak, no eyes, no head, nothing alive."
)

# V1 no TAKE — o estado vive no IMAGE; vocabulario firme<->murcho em prompt de
# movimento derruba o video (regra dos dois lados). ⛔ nunca 'geoduck', nunca 'neck'.
GEODUCK_TAKE = (
    "The clam stays exactly as it appears in the first frame — same position, same "
    "angle, same shape — completely motionless for the entire shot. It is a still "
    "object and nothing about it changes. No bird, no goose, no duck, no swan, no "
    "snake, no worm, no tentacle, no feathers, no beak, no eyes, no head, nothing "
    "alive, nothing with a face."
)

# V2 ⭐ — o vazamento e' a assinatura, e se descreve como SALMOURA DE MARISCO.
# As 4 pecas que ancoram em peixaria e nao em corpo: clear briny liquid, brine,
# fresh clam, fishmonger's counter. ⛔ leaking / white / milky / fluido corporal.
VAZAMENTO_IMAGE = (
    "A thin trickle of clear briny liquid runs from the tip of the siphon and pools "
    "in a small puddle on the wooden table below, the way brine drains from a fresh "
    "clam on a fishmonger's counter."
)
VAZAMENTO_TAKE = "The puddle on the table slowly widens; the clam itself never moves."

ANTICELEB = "Ordinary relatable face, not a celebrity."
CAUDA = "iPhone shot, natural grain, no text, no watermark."

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
# POOLS SORTEAVEIS
# ---------------------------------------------------------------------------

# V9 — dois settings, troca na cena 2. Cena 1 INTERIOR, cenas 2-5 EXTERIOR.
# V10 — a bandeira dos EUA aparece nos DOIS settings.
COZINHAS = [
    {"id": "cozinha_branca",
     "set": "a modest American kitchen, white cabinets, a stainless steel "
            "refrigerator, a small American flag on a stand on the counter",
     "luz": "Cool white overhead kitchen light, flat and even."},
    {"id": "cozinha_carvalho",
     "set": "a modest American kitchen, oak cabinets, a hanging bunch of dried "
            "herbs, a small American flag on a stand beside the bread box",
     "luz": "Warm overhead kitchen light, slight shadow under the chin."},
    {"id": "cozinha_creme",
     "set": "a modest American kitchen, cream-painted cabinets, a bowl of lemons, "
            "a small American flag on a stand by the window",
     "luz": "Cool white overhead kitchen light, flat and even."},
    # + 2026-08-01: o operador mediu vicio de cenario — a mesma cozinha voltando
    # no lote. Pool de 3 para 12.
    {"id": "cozinha_azulejo",
     "set": "a modest American kitchen, pale blue tile backsplash, a wall clock "
            "over the doorway, a small American flag on a stand next to the toaster",
     "luz": "Cool white overhead kitchen light, flat and even."},
    {"id": "cozinha_laminado",
     "set": "a modest American kitchen, worn laminate countertops, a percolator "
            "beside the stove, a small American flag on a stand beside the sink",
     "luz": "Neutral daylight through the window over the sink, soft and even."},
    {"id": "cozinha_fazenda",
     "set": "a modest American farmhouse kitchen, a deep enamel sink, checkered "
            "curtains over the window, a small American flag on a stand on the sill",
     "luz": "Warm overhead kitchen light, slight shadow under the chin."},
    {"id": "cozinha_corredor",
     "set": "a narrow galley kitchen in a modest American home, cabinets on both "
            "walls, a row of coffee mugs on hooks, a small American flag on a stand "
            "by the range",
     "luz": "Cool white overhead kitchen light, flat and even."},
    {"id": "cozinha_nogueira",
     "set": "a modest American kitchen, dark walnut cabinets, a cast-iron skillet "
            "hanging on the wall, a small American flag on a stand above the stove",
     "luz": "Warm light from a single fixture over the table, soft shadow under the chin."},
    {"id": "cozinha_tijolo",
     "set": "a modest American kitchen, exposed brick behind the stove, a wooden "
            "knife block, a small American flag on a stand on the windowsill",
     "luz": "Cool white overhead kitchen light, flat and even."},
    {"id": "cozinha_despensa",
     "set": "a modest American kitchen, open pantry shelves stacked with cans, a "
            "bowl of apples on the counter, a small American flag on a stand by the door",
     "luz": "Neutral overhead kitchen light, even and shadowless."},
    {"id": "cozinha_reboque",
     "set": "a compact kitchen in a modest American mobile home, wood-paneled "
            "walls, a chest freezer in the corner, a small American flag on a stand "
            "over the sink",
     "luz": "Cool white overhead kitchen light, flat and even."},
    {"id": "cozinha_verde",
     "set": "a modest American kitchen, sage green cabinets, a hanging spider "
            "plant, a small American flag on a stand next to the cookie jar",
     "luz": "Warm overhead kitchen light, slight shadow under the chin."},
]

QUINTAIS = [
    {"id": "cerca_madeira",
     "set": "the backyard of a modest American home, a wooden privacy fence, mowed "
            "grass, a small American flag mounted by the back door, potted flowers",
     "luz": "late afternoon golden sunlight from frame-left, long soft shadows."},
    {"id": "churrasqueira",
     "set": "the backyard of a modest American home, a chain-link fence with hedges, "
            "a covered charcoal grill, a small American flag by the back door",
     "luz": "late afternoon golden sunlight from frame-right, long soft shadows."},
    {"id": "lenha",
     "set": "the backyard of a modest American home, a low wooden fence, a stack of "
            "firewood against the wall, a small American flag by the back door",
     "luz": "late afternoon golden sunlight from frame-left, long soft shadows."},
    {"id": "varanda_quintal",
     "set": "the backyard of a modest American home, a wicker sofa with cushions, "
            "dry golden grass, a small American flag mounted by the back door",
     "luz": "late afternoon golden sunlight from frame-right, warm and directional."},
    # + 2026-08-01: mesmo vicio medido na cozinha — o lote inteiro caia no mesmo
    # quintal. Pool de 4 para 12.
    {"id": "horta",
     "set": "the backyard of a modest American home, a wooden fence, tomato plants "
            "staked in a small garden bed, a small American flag mounted by the back door",
     "luz": "late afternoon golden sunlight from frame-left, long soft shadows."},
    {"id": "varal",
     "set": "the backyard of a modest American home, a clothesline strung between "
            "two posts, a chain-link fence, a small American flag by the back door",
     "luz": "late afternoon golden sunlight from frame-right, long soft shadows."},
    {"id": "galpao",
     "set": "the backyard of a modest American home, a small metal tool shed with "
            "the door ajar, patchy grass, a small American flag by the back door",
     "luz": "late afternoon golden sunlight from frame-left, warm and directional."},
    {"id": "carvalho",
     "set": "the backyard of a modest American home, a broad oak tree shading the "
            "fence line, a low picket fence, a small American flag mounted by the back door",
     "luz": "late afternoon golden sunlight from frame-right, warm and directional."},
    {"id": "piscina",
     "set": "the backyard of a modest American home, an above-ground pool with a "
            "folded cover, a wooden fence, a small American flag by the back door",
     "luz": "late afternoon golden sunlight from frame-left, long soft shadows."},
    {"id": "caminhonete",
     "set": "the backyard of a modest American home, an old pickup truck parked "
            "beside the gravel drive, a wooden fence, a small American flag mounted "
            "by the back door",
     "luz": "late afternoon golden sunlight from frame-right, warm and directional."},
    {"id": "ferradura",
     "set": "the backyard of a modest American home, a horseshoe pit dug in the "
            "dirt, a hedge along the property line, a small American flag by the back door",
     "luz": "late afternoon golden sunlight from frame-left, warm and directional."},
    {"id": "carrinho",
     "set": "the backyard of a modest American home, a white picket fence, a "
            "wheelbarrow and a stack of clay pots against the wall, a small American "
            "flag mounted by the back door",
     "luz": "late afternoon golden sunlight from frame-right, long soft shadows."},
]

# V3 ⭐ — o REF e' o corpo-prova: tronco NU, musculatura por GRUPO NOMEADO
# (`muscular` sozinho nao renderiza). ⛔ sem barriga proeminente: aqui ele e' o
# DEPOIS ambulante. Marca facial obrigatoria, num rosto saudavel (nunca avaria).
REFS = [
    {"idade": 69, "musculo": "a lean hard-muscled build with visible definition in "
                             "the chest, shoulders and arms",
     "marca": "short silver hair swept back and a clean pale scar through his left eyebrow",
     "roupa2": "a faded olive linen shirt unbuttoned halfway, sleeves rolled to the elbows"},
    {"idade": 71, "musculo": "a powerfully built muscular frame with a broad chest "
                             "and thick arms",
     "marca": "thick silver-white hair parted on the side and a prominent dark mole "
              "on his right cheekbone",
     "roupa2": "a light blue short-sleeve work shirt, open at the collar"},
    {"idade": 68, "musculo": "a heavy-set powerful build, barrel chest and thick "
                             "muscular forearms",
     "marca": "close-cropped hair with a bold white streak on the left side and a "
              "gold crown on his upper right front tooth",
     "roupa2": "a mustard-yellow short-sleeve button-down shirt"},
    {"idade": 70, "musculo": "a tall broad-shouldered muscular build with a wide "
                             "back and strong neck",
     "marca": "thick gray hair and a deep vertical cleft in his chin",
     "roupa2": "a rust-red short-sleeve snap-button shirt, open at the collar"},
    {"idade": 67, "musculo": "a lean hard-muscled build with visible definition in "
                             "the chest, shoulders and arms",
     "marca": "full silver hair and a small notch missing from the top of his left ear",
     "roupa2": "a faded denim shirt with the sleeves cut off"},
    # + 2026-08-01: o operador viu o mesmo rosto voltando no lote. Pool de 5 para 9.
    {"idade": 66, "musculo": "a wiry hard-muscled build with a deep chest and "
                             "corded forearms",
     "marca": "a shaved head with a close fringe of white hair above the ears and "
              "a small crescent scar under his right eye",
     "roupa2": "a charcoal-gray short-sleeve henley, sleeves pushed up"},
    {"idade": 72, "musculo": "a thick-set powerful build with heavy shoulders and "
                             "a broad chest",
     "marca": "salt-and-pepper hair cut short and neat and a deep dimple in his "
              "left cheek",
     "roupa2": "an olive-drab short-sleeve fishing shirt with two chest pockets"},
    {"idade": 64, "musculo": "a compact powerful build with dense shoulders and "
                             "thick arms",
     "marca": "wiry gray hair cut short at the temples and a dark birthmark the "
              "size of a dime on his left jaw",
     "roupa2": "a heather-gray short-sleeve pocket tee"},
    {"idade": 74, "musculo": "a long-limbed muscular build with a flat stomach and "
                             "strong shoulders",
     "marca": "a bald crown with cropped gray hair at the sides and a thin pale "
              "scar along his jawline",
     "roupa2": "a navy blue short-sleeve camp shirt"},
    # + 2026-08-02: o operador mediu o pool inteiro e viu SEMPRE O MESMO ROSTO.
    # As nove acima descrevem a pessoa quase so' por CABELO — nove homens
    # descritos so' por cabelo sao o mesmo homem nove vezes, e o gerador
    # devolvia quase a mesma cara. As quatro novas entram cada uma por um eixo
    # que estava zerado ou raso aqui:
    #   · 60 — PORTE de lutador (pescoco grosso, ombros pesados) e ancora de
    #     cicatriz limpa no labio.
    #   · 75 — PORTE seco e ossudo mais PELE de idade (manchas senis).
    #   · 73 — OCULOS, o eixo ZERADO deste pool (0/9), mais calvicie total.
    #   · 65 — OCULOS de leitura mais entrada de cabelo em V, cabelo ralo.
    #   · a ancora e' sempre do lado ✅ de licoes-producao-veo §REF —
    #     DISTINTIVO, NUNCA DETERIORADO (cicatriz limpa, mancha, mecha).
    #   · PELO FACIAL continua fora de proposito: o BLOCO 0 deste motor ja'
    #     renderiza `clean-shaven` em string travada, e barba aqui poria o
    #     motor a se contradizer dentro do mesmo bloco.
    #   · zero mencao a etnia: o motor injeta ETNIA[pagina] antes da marca.
    {"idade": 60, "musculo": "a broad thick-necked wrestler's build with heavy "
                             "shoulders, a deep chest and a hard flat stomach",
     "marca": "jet-black hair going gray only at the temples, cut in a short "
              "flat-top, and a thick white scar running down through his upper lip",
     "roupa2": "a white ribbed sleeveless undershirt"},
    {"idade": 75, "musculo": "a rangy hard-muscled build with wide bony shoulders, "
                             "stringy sinewy arms and a lean ridged stomach",
     "marca": "a full head of snow-white hair long enough to touch his collar and "
              "a cluster of dark age spots across his right temple",
     "roupa2": "a sand-colored short-sleeve safari shirt with buttoned epaulets"},
    {"idade": 73, "musculo": "a blocky powerlifter's build with a heavy chest, wide "
                             "back muscles and a thick hard midsection",
     "marca": "a completely bald smooth scalp with no hair left at the sides, thin "
              "gold wire-rimmed glasses, and a deep pitted scar high on his right "
              "cheekbone",
     "roupa2": "a teal short-sleeve bowling shirt with cream side panels"},
    {"idade": 65, "musculo": "a build that tapers hard from wide flaring back "
                             "muscles to a narrow waist, with square chest muscles "
                             "and thick round shoulders",
     "marca": "a sharp widow's peak in thinning ash-gray hair, square silver-rimmed "
              "reading glasses low on the tip of his nose, and a wide pale scar "
              "across his forehead above the left eyebrow",
     # ⚠️ 2026-08-02: esta entrada nascia com "an oval name patch on the chest"
     # e foi corrigida no mesmo dia, antes de ir ao ar. Cracha/etiqueta com
     # nome PEDE TEXTO NA CENA, e a cauda travada do IMAGE deste motor fecha
     # com "no text, no watermark" — o prompt se contradizia sozinho. Trocado
     # so' o pedaco do cracha; a camisa de mecanico fica.
     "roupa2": "a khaki short-sleeve mechanic's shirt with a buttoned flap "
               "pocket on the chest"},
]

# V12 ⭐ — a mulher de 30-35 na cena 4, SEMPRE. Linda, abracada em pe, muda, rindo.
# A idade dos DOIS vai escrita em toda mencao (falha documentada: classificador
# barra por menores sem isso). ⛔ nunca colo, nunca joelho neste agente.
MULHERES = [
    {"idade": 33, "desc": "long chestnut-brown wavy hair past her shoulders, a small "
                          "beauty mark on her left jaw, a fitted coral summer dress"},
    {"idade": 34, "desc": "long dark blonde hair past her shoulders, a small notch in "
                          "her right eyebrow, a fitted white tank top and blue jeans"},
    {"idade": 32, "desc": "long braided hair gathered over one shoulder, a small beauty "
                          "mark high on her right cheekbone, a fitted emerald summer dress"},
    {"idade": 35, "desc": "long straight black hair past her waist, a small dark beauty "
                          "mark below her left eye, a fitted turquoise summer dress"},
    # + 2026-08-01: a mesma moca aparecia em metade do lote. Pool de 4 para 8.
    {"idade": 31, "desc": "long auburn hair pulled back in a high ponytail, a small "
                          "beauty mark above her upper lip, a fitted navy blue summer dress"},
    {"idade": 35, "desc": "dark curls gathered on top of her head in a loose bun, a "
                          "small mole at the corner of her mouth, a fitted olive green "
                          "sundress"},
    {"idade": 32, "desc": "long dark hair worn loose and straight with a center part, "
                          "a thin pale scar through her right eyebrow, a fitted burgundy "
                          "wrap dress"},
    {"idade": 33, "desc": "long dark hair with sun-lightened ends falling past her "
                          "shoulders, a small crescent scar on her left temple, a fitted "
                          "red sleeveless sundress"},
    # + 2026-08-02: mesma medicao que gerou o bloco dos REFS logo acima, so'
    # que do lado da mulher da cena 4 — o operador viu SEMPRE O MESMO ROSTO. E
    # aqui o vicio era literal: as OITO acima abrem TODAS em "long ... hair".
    # Oito mulheres descritas so' por cabelo comprido sao a mesma mulher oito
    # vezes. As seis novas quebram isso por construcao e trazem os eixos que o
    # pool nao acionava:
    #   · CABELO que nao e' comprido — bob reto, corte abaixo da orelha, twist
    #     baixo, pixie, raspado lateral, coque com oculos de sol em cima.
    #   · OCULOS — tortoiseshell grosso, fio de ouro. Eram 0/8 aqui.
    #   · PORTE — long-limbed, ombros de nadadora, encorpada, ombros
    #     quadrados. Nenhuma das oito menciona compleicao.
    #   · PELE — sardas, marca de sol nos ombros.
    #   · a ancora facial (P6) continua obrigatoria em cada uma e sempre do
    #     lado ✅ de licoes-producao-veo §REF — DISTINTIVO, NUNCA DETERIORADO
    #     (pinta, sarda, cicatriz limpa, dente separado). ⛔ dente lascado
    #     ficou de fora: colide com o `strikingly beautiful` que o motor
    #     concatena logo depois.
    #   · o literal `fitted` e a peca fechada estao nas seis: e' o que a V12
    #     cobra, e a idade dos dois vai escrita em toda mencao.
    #   · ⛔ nenhuma entrada de 30 anos: `IDADE_EXT[30]` e' ("thirty",
    #     "thirty") e cinco moldes de CORPO escrevem "Thirty-{n} years old" —
    #     sairia "Thirty-thirty years old", a reincidencia exata do bug
    #     "Thirty-4" documentado mais abaixo neste arquivo.
    {"idade": 34, "desc": "a blunt dark bob cut level with her jaw, thick "
                          "tortoiseshell glasses, tall and long-limbed, a small dark "
                          "mole on the point of her chin, a fitted denim shirtdress"},
    {"idade": 31, "desc": "wavy copper-red hair cropped just below her ears, broad "
                          "swimmer's shoulders, a heavy dusting of freckles across "
                          "her nose and cheekbones, a narrow gap between her front "
                          "teeth, a fitted white sundress"},
    {"idade": 35, "desc": "dark hair in a low twist with one silver streak at the "
                          "temple, solidly built, sun-freckled shoulders, a fine pale "
                          "scar across the bridge of her nose, a fitted "
                          "mustard-yellow tank dress"},
    {"idade": 32, "desc": "a cropped platinum pixie cut, thin gold wire-rimmed "
                          "glasses, high sharp cheekbones, a dark beauty mark at the "
                          "outer corner of her right eye, a fitted black polka-dot "
                          "sundress"},
    {"idade": 34, "desc": "dark hair shaved close on one side, falling in waves on "
                          "the other, long-legged, a faint tan line across her "
                          "shoulders, a thin white scar through her upper lip, a "
                          "fitted olive tank top and khaki shorts"},
    {"idade": 33, "desc": "hair twisted up in a knot with sunglasses pushed up on "
                          "top of her head, tall with square shoulders, heavy dark "
                          "eyebrows, a small raised scar under her right eye, a "
                          "fitted rust-orange linen jumpsuit"},
]

# Prop do payoff (cena 4) — F15: JA' ereto no IMAGE, dimensionado por escala
# corporal. ⛔ nunca `engorged`/`veins`/`a third thicker` (recusa documentada).
PROPS_PAYOFF = [
    {"id": "daikon", "desc": "a very large daikon radish as long as his forearm and "
                             "as thick as his wrist, stiff and straight, its surface "
                             "taut and pale, reaching above his shoulder"},
    {"id": "pepino", "desc": "a very large cucumber as long as his forearm and as "
                             "thick as his wrist, stiff and straight, its surface taut "
                             "and glossy, reaching above his shoulder"},
    {"id": "banana", "desc": "a very large banana as long as his forearm and as thick "
                             "as his wrist, stiff and straight, its surface taut, "
                             "reaching above his shoulder"},
    {"id": "mandioca", "desc": "a very large cassava root as long as his forearm and "
                               "as thick as his wrist, stiff and straight, its surface "
                               "taut and pale, reaching above his shoulder"},
    # + 2026-08-01: o mesmo prop repetindo no lote. Pool de 4 para 8, mesma escala.
    {"id": "abobrinha", "desc": "a very large zucchini as long as his forearm and "
                                "as thick as his wrist, stiff and straight, its surface "
                                "taut and dark green, reaching above his shoulder"},
    {"id": "plantain", "desc": "a very large green plantain as long as his forearm "
                               "and as thick as his wrist, stiff and straight, its "
                               "surface taut and ridged, reaching above his shoulder"},
    {"id": "cenoura", "desc": "a very large carrot as long as his forearm and as "
                              "thick as his wrist, stiff and straight, its surface "
                              "taut and bright, reaching above his shoulder"},
    {"id": "paozao", "desc": "a crusty French bread loaf as long as his forearm and "
                             "as thick as his wrist, stiff and straight, its crust firm "
                             "and golden, reaching above his shoulder"},
]

# ---------------------------------------------------------------------------
# POOLS DE COPY
# ---------------------------------------------------------------------------

NUCLEO = ["Johnson", "pecker", "wiener", "tool", "soldier"]

# O hook herda a ECONOMIA da fonte: orgao nomeado + mecanismo + comando, em <=8s
# ⛔ 2026-08-03 — FRASE ORFA. O operador leu um take e reprovou: "it isn't age"
# deveria ser "it isn't age THAT'S CAUSING YOUR JOHN-SON NOT WORKING ANYMORE...
# ta' deixando o viewer sem entender o contexto e do que se trata".
# REGRA NOVA: toda frase que nomeia uma CAUSA carrega, NA MESMA FRASE, o que ela
# quebra. Nao vale o orgao aparecer "em algum lugar da cena" — a cena reprovada
# tinha o orgao na ULTIMA frase. Aqui isso derrubou 4 entradas: as duas com
# "That's blood flow choked off." solta, o fragmento "Blood flow." e o
# "It's blood flow, not you." — em todas o orgao passou para dentro da propria
# frase da causa. Teto da cena 1 (20) respeitado no pior caso, {o} = "old boy".
HOOKS = [
    "This is what happens to your {o} when American men ignore blood flow too long. Do this tonight.",
    "Your {o} stopped showing up because the blood flow to it choked off. Do this before it's too late.",
    "This is what ignoring blood flow does to your {o}. Fix yours tonight, brother.",
    "American men let the blood flow to their {o} get choked off. Do this before it's too late.",
    "Your wife stopped reaching for you. Nobody told you your {o} lost blood flow. Fix it tonight.",
    "Doctors billed you for twenty years and never once checked the blood flow to your {o}. Do this tonight.",
    "She already knows your {o} won't work tonight — that's blood flow, choked off. Fix it before Friday.",
    "You apologized in the dark again last night. Blood flow quit reaching your {o}. Do this tonight.",
    "She said it's okay, honey, and rolled over. It's blood flow, not you — fix your {o} tonight.",
    # ⛔ CONSERTO 2026-08-03 (2a passada, achado da revisao) — VERBO DE
    # ENCANAMENTO (familia [V]). Queixa do operador lendo o app: "Opens o QUE?
    # Com tanto verbo que voce poderia usar pra dizer que DEIXA O PINTO MELHOR,
    # voce usa 'opens'?". Este era o unico HOOK que usava `open` como promessa:
    # `a pill that never OPENED the blood flow to your {o}` descreve o vaso, nao
    # o homem. ⭐ REGRA NOVA: verbo de RESULTADO (`got your {o} hard`), e o
    # mecanismo `blood flow` continua NA MESMA FRASE — trocar `open` por outro
    # eufemismo de encanamento (`unblocks`, `restores flow`) nao e' conserto.
    # ⚠️ TETO cena 1 (20) MELHORA: 21 -> 20 palavras no pior caso ({o} = "old
    # boy"). ⚠️ RS10: caiu o `Do this tonight instead`, entao esta entrada deixou
    # de somar `your {o}` + marcador de prazo na mesma fala de 8s.
    "You plan your nights around a pill that never got your {o} hard — that's blood flow, not your age.",
    "Nobody in my house buys those pills anymore. Blood flow quit your {o}, brother. Stop paying them.",
    "I went four years without finishing once, brother. Blood flow quit my {o}. Give me sixty seconds.",
    "For four years I told my wife I was just tired. Blood flow quit my {o}. Don't lie to her.",
    "I lost my confidence. I stopped touching my wife. Blood flow quit my {o}. Your turn's coming.",
]

# V5 — a receita e' gelatin + baking soda, PREPARADA NA TELA pelas maos dele.
# ⚠️ topica ou de preparo, nunca dose medica: sem miligramas, sem cura.
RECEITAS = [
    "Men, stir a spoonful of gelatin into baking soda for one minute. Do it before your {o} quits for good.",
    "Men, mix a spoonful of gelatin with baking soda in a jar. Stir it. Your {o} is about to wake back up.",
    "Men, stir gelatin into baking soda, one full minute. That's the first half of getting your {o} back.",
    "Men, stir gelatin and baking soda in a coffee mug while she's asleep. She doesn't need to know why your {o} came back.",
    "Men, pour the baking soda over the gelatin and stir it one full minute. She's still asking. Your {o} still isn't answering.",
    "Men, mix gelatin into baking soda and stir until it's smooth. Do it tonight and check your {o} in the morning.",
    "Men, one spoon of gelatin, one spoon of baking soda, stir. Takes a minute. Your {o} took twenty years to quit.",
    "Men, mix gelatin with baking soda and stir. Costs a dollar. The pill people charged you thirty a month for your {o}.",
    "Men, mix gelatin with baking soda in a glass and stir. Do it before Saturday, before she finds out your {o} doesn't work.",
    "Men, stir gelatin into baking soda right on the counter. Your {o} worked fine at thirty. Get it back.",
    "Every man in my family keeps gelatin and baking soda on the counter. Mix them, stir a minute. Your {o} needs both.",
    "Us guys don't order anything. Gelatin, baking soda, a spoon. Stir one minute. Nobody has to know your {o} needs it.",
    "We keep gelatin next to the coffee in this house. Stir a spoonful into baking soda. Your {o} gets one minute of your day.",
    # + 2026-08-01: o operador mediu vicio de abertura — quase todo item comecava
    # em "Men,". Cinco entradas novas sem esse vocativo.
    "Grab the gelatin and the baking soda off your own shelf. Stir them one minute. Your {o} has waited long enough.",
    "Before you go to bed tonight, stir a spoonful of gelatin into baking soda. That's step one for your {o}.",
    "Nobody at the pharmacy sells this. Gelatin, baking soda, one minute of stirring. Your {o} starts there.",
    "My father-in-law handed me this recipe. Gelatin, baking soda, stir a minute. Do it tonight for your {o}.",
    "Two things off the shelf: gelatin and baking soda. Stir one minute. That's where your {o} comes back.",
]

# V6 ⭐⭐ — a regra central: a receita que ele acabou de dar e' INCOMPLETA.
# (1) a negacao vem antes da solucao, (2) o orgao e' nomeado na mesma frase,
# (3) usa o sim que o espectador ja' deu. ⛔ nunca `not just any gelatin`.
# ⛔ 2026-08-03 — FRASE ORFA (a mesma queixa que reescreveu os HOOKS acima). O
# operador leu "It isn't age. The blood flow got choked off." e cobrou:
# "voce tem que contextualizar mais as coisas, ta' deixando o viewer sem
# entender o contexto e do que se trata". REGRA NOVA: a frase que nomeia a
# causa carrega o alvo NA MESMA FRASE. Aqui o vicio estava em 15 das 16
# entradas — a emenda do MUP virava duas frases de fisiologia solta
# ("It's not age." / "Your blood flow got choked off.") e o orgao ficava
# so' na frase anterior. Todas ganharam o orgao dentro da frase da causa.
# ⚠️ O que NAO mudou: o literal `without the gelatin trick`, a negacao antes
# da solucao, o `for your {o}` na frase da negacao (V6.2) e o `blood flow`
# que o linter cobra. Onde o alvo nao coube, encurtei OUTRA coisa da propria
# entrada — o teto de 34 da cena 3 e' medido no pior caso, {o} = "old boy".
# A entrada 9 nao tinha o vicio (o orgao ja' vinha na frase) e nao foi tocada.
VIRADAS = [
    "But here's what most guys never find out. Without the gelatin trick, baking soda alone does nothing for your {o} — it's not age, brother, it's blood flow, choked off.",
    "But here's the thing most guys never realize. Without the gelatin trick, baking soda does nothing for your {o}. It's not age — the blood flow to your {o} got choked off.",
    "You didn't fail, brother. Nobody gave you the other half. Without the gelatin trick, baking soda does nothing for your {o}, and the blood flow to it stays choked off.",
    "Stop right there. Without the gelatin trick, that baking soda is half a recipe and your {o} stays down. It's not age — it's the blood flow to your {o}, squeezed shut.",
    "I gave you half on purpose. Without the gelatin trick, that recipe does nothing for your {o}. It's not age — the blood flow to your {o} got pinched off decades ago.",
    "Now don't go telling the guys yet. Without the gelatin trick, baking soda does nothing for your {o}. It's not age, brother — the blood flow to your {o} got shut down.",
    "You're one ingredient short, brother. Without the gelatin trick, baking soda does nothing for your {o}. It's not age — the blood flow to your {o} got choked off while you waited.",
    "She's waited two years already. Without the gelatin trick, baking soda does nothing for your {o}, and she waits two more. It's not age — your {o} got its blood flow choked off.",
    "I mixed that same spoon for a year and nothing moved. Without the gelatin trick, baking soda does nothing for your {o}. It's not age — your {o} lost its blood flow.",
    "I did this wrong first. I quit for a month. I told my wife it was over. Without the gelatin trick, baking soda does nothing for your {o} — your blood flow stays shut.",
    "Every man I gave this to called me back angry. Without the gelatin trick, baking soda does nothing for your {o}. It's not age — your {o} got its blood flow sealed off.",
    # + 2026-08-01: o operador mediu vicio de vocativo — "brother" em quase toda
    # virada. Cinco entradas novas, nenhuma com vocativo.
    "Go ahead and try it without me. Without the gelatin trick, baking soda does nothing for your {o}. It's not age — the blood flow to your {o} got pinched shut.",
    "You've already lost ten years to this. Without the gelatin trick, baking soda does nothing for your {o}. It's not age — the blood flow to your {o} got clamped off.",
    "Your doctor won't tell you this part. Without the gelatin trick, baking soda does nothing for your {o}. It's not age — the blood flow to your {o} got cut off.",
    "My neighbor mixed it wrong all summer and gave up. Without the gelatin trick, baking soda does nothing for your {o}. It's not age — your {o} got its blood flow sealed shut.",
    "Now you know what the pill people never sold you. Without the gelatin trick, baking soda does nothing for your {o}. Your {o} got its blood flow choked off — that's not age.",
]

# V12 — a copy da cena 4 e' DIRETA sobre ela, com o substantivo-nucleo.
# ⛔ reacao generica (`life is good again`) nao conta.
PROVAS = [
    "She's half my age and she can't keep her hands off my {o}. Thirty-{n} years old and she calls me every night. {barreira}",
    "She's {n_ext} and she can't keep her hands off my {o}. Half my age, and she's the one who won't wait. {barreira}",
    "Thirty-{n} years old and she told her girlfriends about my {o}. Half my age, and I'm what she brags about. {barreira}",
    "She's {n_ext}. Half my age, and she asked me for a break. My {o} doesn't tap out first anymore. {barreira}",
    "Thirty-{n} years old and she reaches for me first now. Half my age, and my {o} is why she stays. {barreira}",
    "She's {n_ext} and she drives an hour over on a Tuesday night. Half my age, and my {o} is why. {barreira}",
    "She's {n_ext}, half my age, and she needed a minute to catch her breath. My {o} did that. {barreira}",
    "Us guys pass this around now. My {o} works and she's {n_ext}. She couldn't sit still the next day. Thirty-{n} years old. {barreira}",
    # + 2026-08-01: o operador mediu vicio de abertura — a prova sempre comecava
    # pela idade dela. Cinco entradas novas entrando por outro lugar.
    "My {o} works, and she noticed before I said a word. She's {n_ext}, half my age. {barreira}",
    "Her friends ask what she sees in me. She's {n_ext}, and my {o} is the answer. {barreira}",
    "She was quiet the first night. Thirty-{n} years old, and now she won't let my {o} rest. {barreira}",
    "Twenty years I couldn't. Now she's {n_ext}, half my age, and my {o} keeps up with her. {barreira}",
    "I stopped apologizing in the dark. She's {n_ext}, half my age, and my {o} doesn't quit early. {barreira}",
]

BARREIRAS = [
    "A trick you can do from the comfort of your own home.",
    "No doctor, no pharmacy counter, nobody has to know.",
    "You do it in your own kitchen, in about a minute.",
    "Costs less than a cup of coffee and nobody sees you buy it.",
    "Nothing to fill, nothing to explain to anybody.",
    # + 2026-08-01: pool curto demais, a mesma barreira caia no lote inteiro.
    "Everything you need is already in your cupboard.",
    "Any grocery store in town has both, for pocket change.",
    "You do it once, alone, and it stays your business.",
]

# ⛔ CONSERTO 2026-08-03 — MUDANCA SEM DIZER O QUE MUDOU (familia [C]).
# O operador leu no proprio app "My sister asked what changed." e cobrou: "o que
# mudou?". Aqui o vicio era o mesmo em tres entradas deste pool — a fala abria a
# pergunta ("she asks what changed", "she'll ask what got into you") e ACABAVA,
# entao o CTA inteiro passava sem nunca dizer o que o negocio faz pelo homem.
# ⭐ REGRA NOVA: se a frase abre a pergunta, ela mesma RESPONDE, e responde com
# VERBO DE RESULTADO ("got you hard again", "you're hard again"), nunca com
# verbo de encanamento nem com outra abstracao — trocar metafora por metafora
# nao e' conserto (§17 de licoes-de-construcao.md).
# ⚠️ TETO_FALA da cena 3 (40) intacto: cada entrada reescrita tem MENOS ou o
# MESMO numero de palavras da que substituiu (12->12, 11->11, 10->9), e o gasto
# do verbo obvio foi pago DENTRO da propria entrada (caiu "Next"/"video" na
# primeira, "You'll remember this" virou "Remember this" na segunda).
# ⚠️ RS10: nenhuma delas escreve `your <orgao>`, entao o marcador de prazo
# ("Friday night", "tonight") continua sozinho na fala. Zero medida de resultado.
PACING = [
    "Friday night, when she asks what got you hard again, remember this.",
    # ⚠️ 2026-08-03, 2a passada: a 1a versao deste conserto escreveu "Next Friday
    # night she'll find out you're hard again. Remember this." — 11 palavras
    # contra as 10 da entrada que substituiu, e o pior CTA renderizado subiu de
    # 44 para 45 palavras (teto 40). Regra [1]: se o verbo obvio nao couber,
    # ENCURTE OUTRA COISA na mesma entrada — nunca suba o TETO_FALA. Caiu "Next".
    "Friday night she'll find out you're hard again. Remember this.",
    # + 2026-08-01: so' havia duas entradas, ambas em "next Friday night" — todo
    # CTA do lote marcava a mesma sexta. Quatro janelas novas.
    "Saturday morning, when she's still smiling, you'll think back to this.",
    "The next time she reaches over in bed, you'll remember tonight.",
    "Two weeks from now you'll wonder why nobody told you sooner.",
    "One month from tonight, she'll know you're hard again.",
]

GATES = [
    "Make sure you're following me first, or I won't have any way to find your comment, brother.",
    "Follow me first, or Facebook can't deliver it, brother.",
    "Hit follow right now, or my message never lands.",
    # + 2026-08-01: o operador mediu "brother" em praticamente todo CTA do lote.
    # ⚠️ REGRA: no maximo 2 entradas deste pool com o vocativo "brother", e a
    # maioria sem vocativo nenhum. As duas de cima ja' gastam a cota.
    "Follow me first — Facebook won't let me message a stranger.",
    "Tap follow before you comment, or your name gets buried.",
    "Follow me first, man. I go through the followers first.",
    "Hit follow, otherwise the algorithm never shows you my reply.",
    "Follow me before you scroll on, or this never reaches you again.",
    "Give me a follow first. My inbox is closed to strangers.",
    "Follow first, fellas. Half the comments I get, I never find again.",
    "Follow me first — I only get a day or two here.",
    "You'll want to follow first — that's the only way it goes through.",
]

CTAS = [
    # ⭐ Alternativa pedida pelo operador em 2026-07-31, vista em campo:
    # a promessa e' A RECEITA, nao "o que eu uso" nem "onde eu compro".
    # E' a mais direta do pool e a unica que casa com a keyword RECIPE
    # que o Veo Editor ja' destaca na legenda.
    "{pacing} Comment gelatin, and I'll send you the recipe today. {gate}",
    "{pacing} Comment gelatin, and I'll send you the only one I trust today. {gate}",
    "{pacing} Comment gelatin, and I'll send you the exact one I use, tonight. {gate}",
    "{pacing} Comment gelatin, and I'll send you where I get mine. {gate}",
    "{pacing} Comment gelatin, and I'll send you the full video today. {gate}",
    "{pacing} Comment gelatin, and I'll send you what to buy and where. {gate}",
    "{pacing} Comment gelatin, and I'll send the whole thing over before this comes down. {gate}",
    "{pacing} Comment gelatin, and I'll send you the gelatin trick tonight. {gate}",
    "{pacing} Comment gelatin, and I'll send you the other half of that recipe. {gate}",
    "{pacing} Comment gelatin, and I'll send you the same one I sent my brother. {gate}",
    "{pacing} Comment gelatin, and I'll send you the one we use at my house. I can't name it here. {gate}",
    "{pacing} I waited four years to find this. Comment gelatin, and I'll send you the missing half tonight. {gate}",
    "{pacing} Comment gelatin, and I'll send you what my own wife went looking for. She found it before I did. {gate}",
    # + 2026-08-01: o operador mediu vicio de promessa — quase todo item prometia
    # "o que eu uso"/"onde eu compro". Quatro entradas novas, sem vocativo.
    "{pacing} Comment gelatin, and the recipe is in your inbox tonight. {gate}",
    "{pacing} Comment gelatin, and I'll walk you through the missing half. {gate}",
    "{pacing} Comment gelatin, and I'll send the brand my wife buys. {gate}",
    "{pacing} Comment gelatin, and I'll send you the rest tonight. {gate}",
]

# ---------------------------------------------------------------------------
# TABELAS DE TOKEN BANIDO — consumidas pelo `short_comum.lint_curto`
# ---------------------------------------------------------------------------

BANIDOS_TAKE = {
    "geoduck": "so' no IMAGE; no TAKE usar 'the clam' (V1)",
    "neck": "no geoduck e' 'siphon', nunca 'neck' (V1)",
    "stiff": "adjetivo de estado em prompt de movimento derruba o video",
    "limp": "idem", "sags": "idem", "pulse": "tumescencia — o VIDEO e' recusado",
    "throb": "idem", "swelling": "idem",
}
BANIDOS_IMAGE = {
    "big": "adjetivo nao dimensiona — o Veo normaliza (V1)",
    "huge": "idem", "engorged": "vocabulario anatomico — recusa", "veins": "idem",
}
# V2 — o vazamento nunca sai do dominio da peixaria
BANIDOS_VAZAMENTO = {
    "leaking": "verbo do prop — usar o vocabulario de salmoura (V2)",
    "milky": "a cor faz a leitura virar outra coisa (V2)",
    "cloudy": "idem (V2)",
    "dripping fluid": "sem qualificar — ancorar em peixaria (V2)",
}
# V7 — zero ingrediente-fantasma importado da fonte
BANIDOS_FONTE = {
    "horse gelatin": "ingrediente-fantasma do Kofi — nosso mecanismo e' o gelatin trick (V7)",
    "equine collagen": "idem (V7)",
}
BANIDOS_GLOBAL = {"the victim": "rotulo que significa dano",
                  "the narrator": "trocar por relacao nomeada"}
BANIDOS_CTA = {"BOOK": "quebra a automacao DM", "YES": "quebra a automacao DM"}

# ⚠️⚠️ ESTE E' O TETO DO ARCO DE 5 CENAS — nao e' o teto do SHORT.
# O `TETO_FALA` deste arquivo (logo abaixo, na secao do SHORT) tem 3 cenas e e'
# o que o app e o linter cobram. Este aqui existe so' para as PONTAS herdarem a
# mesma regua do motor longo: cena 1 (20) vira a 1 do SHORT e cena 5 (40) vira
# a 3. Trocar um pelo outro muda o teto de palavra do agente inteiro.
#
# cena 5 com teto folgado (40): future pacing + GELATIN + follow-gate sao
# TRES obrigatorios e nao cabem nas 16-20 palavras do arsenal.
TETO_FALA_LONGO = {1: 20, 2: 24, 3: 34, 4: 32, 5: 40}


def _palavras(txt):
    return len(re.findall(r"[A-Za-z']+", txt))


# A idade dela entra na fala de duas formas: {n_ext} e' o numero inteiro por
# extenso ("thirty-four") e {n} e' so' a UNIDADE em palavra ("four"), para os
# moldes que escrevem "Thirty-{n} years old".
# ⚠️ Passar o digito cru (idade - 30) entregava "Thirty-4" na fala — bug visto
# no painel em 2026-07-30. O REF fala o que esta' escrito.
IDADE_EXT = {
    30: ("thirty", "thirty"), 31: ("thirty-one", "one"),
    32: ("thirty-two", "two"), 33: ("thirty-three", "three"),
    34: ("thirty-four", "four"), 35: ("thirty-five", "five"),
}


def _idade_slots(idade):
    ext, unidade = IDADE_EXT[idade]
    return {"n_ext": ext, "n": unidade}


def _evitando(rng, pool, recentes):
    livres = [x for x in pool if x.get("id") not in recentes]
    return rng.choice(livres if livres else pool)


def sortear_longo(pagina, rng, ledger, travas=None):
    # ⛔ A REF e a MULHER saem AQUI, no motor longo embutido. A trava
    # atravessa `sc.sortear_curto` ate' este ponto — sem isso o toggle
    # acenderia e nao mudaria nada.
    hist = ledger.get(pagina, {})
    coz = _evitando(rng, COZINHAS, hist.get("cozinha", [])[-2:])
    qui = _evitando(rng, QUINTAIS, hist.get("quintal", [])[-2:])
    prop = _evitando(rng, PROPS_PAYOFF, hist.get("prop", [])[-2:])
    ref, mul = rng.choice(REFS), rng.choice(MULHERES)

    orgaos = rng.sample(NUCLEO, 4)
    falas = [
        rng.choice(HOOKS).format(o=orgaos[0]),
        rng.choice(RECEITAS).format(o=orgaos[1]),
        rng.choice(VIRADAS).format(o=orgaos[2]),
        rng.choice(PROVAS).format(o=orgaos[3], barreira=rng.choice(BARREIRAS),
                                  **_idade_slots(mul["idade"])),
        _cta_montado(rng),
    ]
    return {"pagina": pagina, "cozinha": coz, "quintal": qui, "prop": prop,
            "ref": ref, "mulher": mul, "falas": falas,
            # 50/50, ordem do operador 2026-08-04
            "bandeira": rng.random() < 0.5}


# ---------------------------------------------------------------------------
# GERADOR DO ARCO DE 5 CENAS — o `short_comum.montar_curto` chama este e fica
# so' com as cenas do MAPA
# ---------------------------------------------------------------------------

def montar_longo(spec):
    et = ETNIA[spec["pagina"]]
    ref, mul, prop = spec["ref"], spec["mulher"], spec["prop"]
    coz, qui, falas = spec["cozinha"], spec["quintal"], spec["falas"]
    luz_ext = qui["luz"]

    roupa_s = re.sub(r"^an? ", "", ref["roupa2"])   # sem artigo, para "the same ..."
    corpo = ("bare-chested, %s, skin with a light sheen of sweat. %s."
             % (ref["musculo"], ref["marca"].capitalize()))


    # ⭐⭐ A BANDEIRA E' 50/50 (ordem do operador, 2026-08-04). Ela estava escrita
    # DENTRO das strings de COZINHAS e QUINTAIS, entao saia em 100% dos videos.
    # Aqui ela sai por remocao EXATA quando o sorteio diz que nao, e o
    # `lint_bandeira` confere no TEXTO MONTADO — inclusive a prosa.
    # ⛔ O pool nao e' reescrito: as strings de set sao copy validada.
    com_bandeira = spec.get("bandeira", True)
    coz_set = coz["set"] if com_bandeira else sc.tirar_bandeira(coz["set"])
    qui_set = qui["set"] if com_bandeira else sc.tirar_bandeira(qui["set"])
    b = {}

    # O cabecalho REF faz parte do bloco, igual ao "IMAGE 01/05:" dos outros.
    # E o que o parser do AdBatch usa para mandar este bloco para o painel
    # Consistencia Visual em vez de tentar encaixa-lo num slot da grade.
    # ⛔ Nao remover: sem ele a referencia e descartada em silencio.
    b["BLOCO 0 (REF)"] = (
        "REF 01: Photo of a real person, a %d-year-old %s man, chest up, facing the camera "
        "directly, jaw tight, brow furrowed, mouth open mid-shout. %s. Heavy crow's "
        "feet, clean-shaven, tanned skin with visible pores. %s No text, no watermark."
        % (ref["idade"], et, corpo.rstrip("."), ANTICELEB)
    )

    b["IMAGE 01/05"] = (
        "IMAGE 01/05: Medium shot inside %s. Seated behind a wooden kitchen table is "
        "a %d-year-old %s man, %s Jaw tight, brow furrowed, eyes locked on the lens, "
        "mouth open mid-shout. %s %s He is alone in the frame. %s %s %s"
        % (coz_set, ref["idade"], et, corpo, GEODUCK_IMAGE, VAZAMENTO_IMAGE,
           ANTICELEB, coz["luz"], CAUDA)
    )

    b["IMAGE 02/05"] = (
        "IMAGE 02/05: Medium shot in %s. Standing behind a weathered wooden table is "
        "the same %d-year-old %s man, %s, now wearing %s, thick forearms bare. He is "
        "mid-action: his right hand tilts an open box of baking soda, pouring white "
        "powder into a glass jar of gelatin on the table. His left hand holds a wooden "
        "stirring stick above the jar. He is speaking, looking directly at the camera. "
        "He is alone in the frame. %s The scene is lit by %s %s"
        % (qui_set, ref["idade"], et, ref["marca"], ref["roupa2"], ANTICELEB,
           luz_ext, CAUDA)
    )

    b["IMAGE 03/05"] = (
        "IMAGE 03/05: Medium close-up, same backyard, same table with the open jar and "
        "the box of baking soda. The same %d-year-old %s man, %s, same %s. He leans "
        "toward the camera, his right index finger pointing directly at the lens, his "
        "left hand flat on the table. Expression hard and urgent, brow furrowed, mouth "
        "open mid-word. He is alone in the frame. %s Late afternoon %s %s"
        % (ref["idade"], et, ref["marca"], roupa_s, ANTICELEB, luz_ext, CAUDA)
    )

    b["IMAGE 04/05"] = (
        "IMAGE 04/05: Medium shot, same backyard, same fence and flag. Two fully "
        # ⛔ "The SAME %d-year-old man, SAME %s" — a ancora de continuidade tem
        # de cair sobre o HOMEM, nao sobre a camisa. Enquanto dizia so' "The
        # 69-year-old man ... wearing the same shirt", o Veo lia "a mesma
        # camisa" e se sentia livre para desenhar outra pessoa dentro dela:
        # saiu um senhor de oculos e bigode, sem musculatura, no lugar do
        # corpo-prova. E como o TAKE diz "Only he speaks", quem falava a fala
        # do REF era esse estranho. Falha relatada em producao, 2026-07-31.
        "clothed adults, a %d-year-old woman and a %d-year-old man. The same "
        "%d-year-old %s man, same %s, wearing the same %s, stands tall, chin "
        "lifted, grinning broadly. In his right "
        "hand, held upright at shoulder height, he grips %s. A %d-year-old %s woman, "
        "strikingly beautiful, %s, visibly toned arms. She has both arms wrapped around "
        "his shoulders from the side, leaning her head against him, laughing openly. "
        "Both are ordinary everyday relatable people with plain unremarkable faces, "
        "not celebrities, not models, not actors. The scene is lit by %s %s"
        % (mul["idade"], ref["idade"], ref["idade"], et, ref["marca"], roupa_s,
           prop["desc"], mul["idade"], et, mul["desc"], luz_ext, CAUDA)
    )

    b["IMAGE 05/05"] = (
        "IMAGE 05/05: Close-up, same backyard. The same %d-year-old %s man, %s, wearing "
        "the same %s. He is alone in the frame. He looks straight into the lens, calm and "
        "confident, one corner of his mouth raised in a half-smile. His right index "
        "finger points directly at the camera. %s The scene is lit by %s %s"
        % (ref["idade"], et, ref["marca"], roupa_s, ANTICELEB, luz_ext, CAUDA)
    )

    b["TAKE 01/05"] = (
        "TAKE 01/05: Animate the provided image exactly. Handheld iPhone shot, very "
        "slight natural sway, no cuts. The %d-year-old man stares into the lens with "
        "fury, brow furrowed, jaw tight, and speaks with force, leaning forward once "
        "mid-sentence. His hands grip the shell and do not move. %s %s He is the only "
        "person in the shot.\nDialogue: \"%s\"\n"
        "Audio: quiet kitchen hum, faint refrigerator buzz. No music."
        % (ref["idade"], GEODUCK_TAKE, VAZAMENTO_TAKE, sonorizar(falas[0]))
    )

    b["TAKE 02/05"] = (
        "TAKE 02/05: Animate the provided image exactly. Handheld iPhone shot, very "
        "slight natural sway, no cuts. The %d-year-old man speaks to the camera while "
        "his hands stir the jar: finishing the baking soda, setting the box down, "
        "picking up the wooden stick and stirring the mixture inside the jar in "
        "slow circles. His "
        "eyes stay on the lens the whole time. He is the only person in the shot and no "
        "one else enters frame.\nDialogue: \"%s\"\n"
        "Audio: outdoor ambient — distant birds, faint breeze. No music."
        % (ref["idade"], sonorizar(falas[1]))
    )

    b["TAKE 03/05"] = (
        "TAKE 03/05: Animate the provided image exactly. Handheld iPhone shot, very "
        "slight natural sway, no cuts. The %d-year-old man leans toward the camera, "
        "pointing his right index finger at the lens, expression dead serious. His left "
        "hand presses flat on the table once for emphasis. He slows down on the last "
        "sentence. He is the only person in the shot.\nDialogue: \"%s\"\n"
        "Audio: outdoor ambient — same birds, faint breeze. No music."
        % (ref["idade"], sonorizar(falas[2]))
    )

    b["TAKE 04/05"] = (
        "TAKE 04/05: Animate the provided image exactly. Handheld iPhone shot, very "
        "slight natural sway, no cuts. The %d-year-old man grins wide and laughs once "
        "at his own line, his head tipping back briefly. His right arm stays exactly "
        "where it is, holding it upright at shoulder height the entire take — it stays "
        "exactly as it appears in the first frame, same position, same angle, same "
        "shape, completely motionless for the entire shot. The %d-year-old woman laughs "
        "openly, her head tipping against his shoulder, both arms wrapped around him, "
        "swaying slightly with her laughter. Only he speaks; she is silent and "
        "laughing.\nDialogue: \"%s\"\n"
        "Audio: outdoor ambient — birds, her laughter warm and audible. No music."
        % (ref["idade"], mul["idade"], sonorizar(falas[3]))
    )

    b["TAKE 05/05"] = (
        "TAKE 05/05: Animate the provided image exactly. Handheld iPhone shot, very "
        "slight natural sway, no cuts. The %d-year-old man looks into the lens, calm "
        "and confident, and points his right index finger at the camera. He speaks "
        "directly and evenly, no rush.\nDialogue: \"%s\"\n"
        "Audio: outdoor ambient, faint breeze. No music." % (ref["idade"], sonorizar(falas[4]))
    )

    return b


def nova_fala_longo(spec, i, rng):
    """Re-sorteia a fala da cena i (0-4) mantendo o substantivo-nucleo daquela cena."""
    o = next((n for n in NUCLEO if n.lower() in spec["falas"][i].lower()), "Johnson")
    mul = spec["mulher"]
    if i == 0:
        return rng.choice(HOOKS).format(o=o)
    if i == 1:
        return rng.choice(RECEITAS).format(o=o)
    if i == 2:
        return rng.choice(VIRADAS).format(o=o)
    if i == 3:
        return rng.choice(PROVAS).format(o=o, barreira=rng.choice(BARREIRAS),
                                         **_idade_slots(mul["idade"]))
    return _cta_montado(rng)


# ---------------------------------------------------------------------------
# INTERFACE (consumido por ui_agente.py)
# ---------------------------------------------------------------------------

EIXOS_UI = [
    ("cozinha", "COZINHA", "COZINHAS", "id"),
    ("quintal", "QUINTAL", "QUINTAIS", "id"),
    ("prop", "PROP CENA 4", "PROPS_PAYOFF", "id"),
    ("ref", "REF (corpo-prova)", "REFS", "marca"),
    ("mulher", "MULHER", "MULHERES", "desc"),
]

PT_COZ = {"cozinha_branca": "cozinha branca", "cozinha_carvalho": "cozinha de carvalho",
          "cozinha_creme": "cozinha creme"}
PT_QUI = {"cerca_madeira": "no quintal de cerca de madeira",
          "churrasqueira": "no quintal com churrasqueira",
          "lenha": "no quintal com a pilha de lenha",
          "varanda_quintal": "no quintal com sofá de vime"}


# ---------------------------------------------------------------------------
# ⭐ A FACHADA DO MOTOR LONGO — o que o `short_comum` recebia como modulo base
# ---------------------------------------------------------------------------
# O `short_comum` foi escrito para receber o MODULO do motor longo e ler dele
# `montar`, `sortear`, `nova_fala`, `NUCLEO`, `_palavras` e as tabelas
# `BANIDOS_*`. Como agora tudo mora neste arquivo, e os nomes `montar`,
# `sortear` e `nova_fala` daqui sao os do SHORT, a fachada empacota as versoes
# `*_longo` sob os nomes que ele espera.
#
# ⚠️ O `lint_curto` faz `hasattr(base, "BANIDOS_CATEGORIA"/"BANIDOS_ANIMAL")` —
# este agente nunca teve essas duas tabelas, e a fachada tambem nao as tem. Nao
# inventar: a varredura tem de continuar sendo exatamente a mesma.
_MOTOR_LONGO = types.SimpleNamespace(
    montar=montar_longo,
    sortear=sortear_longo,
    nova_fala=nova_fala_longo,
    NUCLEO=NUCLEO,
    _palavras=_palavras,
    ETNIA=ETNIA,
    CAUDA=CAUDA,
    sonorizar=sonorizar,
    BANIDOS_TAKE=BANIDOS_TAKE,
    BANIDOS_IMAGE=BANIDOS_IMAGE,
    BANIDOS_CTA=BANIDOS_CTA,
    BANIDOS_GLOBAL=BANIDOS_GLOBAL,
    BANIDOS_VAZAMENTO=BANIDOS_VAZAMENTO,
    BANIDOS_FONTE=BANIDOS_FONTE,
)

# ===========================================================================
# FIM DO BLOCO INLINEADO — daqui para baixo e' o SHORT propriamente dito
# ===========================================================================

# ⭐ MAPA e' de onde vem a IMAGEM; MAPA_COPY e' de onde vem a FALA. A cena 3
# junta as duas coisas: a fala do CTA (base 5) por cima da cena do ritual.
#
# ⚠️ Ordem do operador, 2026-07-31: "estamos deixando espaco valioso nesses 22
# segundos apertados no lixo". A cena 3 era o close do CTA — um terco do video
# num talking head, zero informacao visual. Agora o espectador OUVE o pedido e
# VE o gelatin trick nos mesmos 8 segundos.
#
# No VAZAMENTO a cena que ja' tem rosto E maos trabalhando e' a 2 (a
# receita-isca: ele despeja o bicarbonato e mexe, falando com a camera). Ela
# fecha o arco em vez de brigar com ele — a fundida diz que bicarbonato sozinho
# nao faz nada, e o CTA por cima da imagem dele mexendo o bicarbonato oferece
# justamente a outra metade da receita.
MAPA = (1, 4, 2)
MAPA_COPY = (1, None, 5)          # None = a fundida
CENAS_UI = ["1 · O VAZAMENTO", "2 · A RECEITA INCOMPLETA + A PROVA",
            "3 · CTA PREPARANDO"]

# ⛔⛔ AS CENAS 2 E 3 NAO HERDAM MAIS O TETO DO LONGO — corrigido 2026-08-04.
# O comentario antigo dizia "mesmos pools, mesma regua" e a regua estava
# ERRADA: na versao longa o CTA tinha uma cena inteira so' para ele; aqui
# ele divide os mesmos 8 segundos com o pacing e o gate. Herdar 40 dali fez
# este motor virar o pior do repo — medido, a cena 3 gerava ate' 48 palavras
# (6,0 p/s) e 53,5% dos videos tinham fala cortada. O que ficava de fora era
# o GATE DE FOLLOW INTEIRO: nao o hook, nao o `Comment gelatin,` — a
# maquina de conversao morrendo no ar, em metade do lote.
# ⚠️ 8s a 4,0 palavras/s = 32 (licoes-de-construcao §5 e §27).
# ⛔⛔ SEM MODOS DE REF NESTE MOTOR (2026-08-05). Ele tem `IDADE_EXT`,
# uma tabela indexada POR IDADE que traduz o numero para a expressao
# falada, e o pool compartilhado tem idades que ela nao conhece — o
# sorteio morre com KeyError. Ligar exige reconstruir a tabela, e isso
# mudaria o comportamento NORMAL, que hoje esta' provado identico.

TETO_FALA = {1: TETO_FALA_LONGO[1], 2: 32, 3: 32}


# ---------------------------------------------------------------------------
# A COPY FUNDIDA — cena 2
# ---------------------------------------------------------------------------
# ⚠️ CURADORIA DO OPERADOR. Copy nova, montada dos fragmentos ja' validados das
# VIRADAS e PROVAS do motor longo.
#
# Todo item carrega, na mesma respiracao:
#   1. a isca + a virada -> `without the gelatin trick` + o bicarbonato inutil
#   2. o mecanismo       -> `blood flow`
#   3. a prova           -> a moca, metade da idade dele
# ⛔ Sem {barreira}: tres beats ja' enchem os 8 segundos.
# ⚠️ Todo item precisa de `{o}` — o CTA nao nomeia o orgao.
FUNDIDAS = [
    "Without the gelatin trick, baking soda alone does nothing for your {o} — "
    "that's blood flow, choked off. She's {n_ext}, half my age, and she can't "
    "keep her hands off mine.",

    "Baking soda is half a recipe: without the gelatin trick your {o} stays "
    "down, because the blood flow is choked off. She's {n_ext} and she reaches "
    "for me first now.",

    "Without the gelatin trick that baking soda does nothing for your {o} — "
    "your blood flow got squeezed shut, not your age. Thirty-{n} years old, "
    "and she won't wait.",

    "Nobody gave you the other half, brother. Without the gelatin trick the "
    "baking soda leaves your {o} down and the blood flow shut. She's {n_ext} "
    "and she needed a minute.",

    "Without the gelatin trick, baking soda is half a recipe and the blood flow "
    "never reaches your {o}. She's {n_ext}, half my age, and she calls me every "
    "night.",

    # + 2026-08-01: o operador mediu vicio — cinco itens so', e "brother" voltando
    # no lote. Pool de 5 para 13; as oito novas nao tem vocativo.
    "Without the gelatin trick, that baking soda leaves your {o} right where "
    "it is — the blood flow stays choked off. She's {n_ext}, half my age, and "
    "she told her girlfriends about mine.",

    "Your blood flow got choked off, not your years — and without the gelatin "
    "trick, baking soda does nothing for your {o}. She's {n_ext} and she "
    "couldn't sit still the next day.",

    "You didn't fail. Without the gelatin trick, baking soda does nothing for "
    "your {o} — the blood flow got pinched shut years ago. She's {n_ext} and "
    "she noticed before I said anything.",

    "I stirred baking soda for a year and nothing moved. Without the gelatin trick, baking soda "
    "does nothing for your {o} — the blood flow stays clamped off. She's "
    "{n_ext} and she asked for a break.",

    "You're one ingredient short. Without the gelatin trick, baking soda does "
    "nothing for your {o} and the blood flow stays shut. Thirty-{n} years old, "
    "and she brags about mine.",

    # ⛔ CONSERTO 2026-08-03 — FRASE ORFA. `That's blood flow, choked off
    # decades back.` nao dizia choked off ONDE: o orgao estava na frase
    # ANTERIOR, e o espectador ouve a causa solta. Queixa literal do operador
    # sobre o mesmo vicio em outro agente: "ta' deixando o viewer sem entender
    # o contexto e do que se trata".
    # ⭐ A regra: a frase que nomeia a CAUSA carrega, NA MESMA FRASE, o que ela
    # quebra. ⚠️ O gasto foi pago dentro da propria entrada — TETO_FALA da cena
    # 2 (36) intacto.
    "Without the gelatin trick, baking soda does nothing. That's the blood flow "
    "to your {o}, choked off decades back. She's {n_ext}, half my age, and she "
    "found out what mine does.",

    "Stop before you tell the guys. Without the gelatin trick, that baking "
    "soda does nothing for your {o} — your blood flow got squeezed shut. "
    "She's {n_ext} and she won't leave me alone.",

    # ⛔ CONSERTO 2026-08-03 (2a passada, achado da revisao) — VERBO DE
    # ENCANAMENTO (familia [V]). Era a unica FUNDIDA com `open`: `the blood flow
    # never OPENS for your {o}` entrega o vaso abrindo quando o homem quer saber
    # se fica duro. ⭐ REGRA NOVA: verbo de RESULTADO (`never gets your {o}
    # hard`) com o mecanismo `blood flow` de sujeito, na mesma frase.
    # ⚠️ TETO cena 2 (36) intacto: mesma contagem de palavras da entrada que
    # substituiu (`never opens for your {o}` = `never gets your {o} hard`).
    # ⚠️ RS10: sem marcador de prazo nesta fala, o `your {o}` segue sozinho.
    "Without the gelatin trick, the baking soda is half the job and the blood "
    "flow never gets your {o} hard. She's {n_ext}, half my age, and she's the "
    "one keeping me up.",
]


def _cta_montado(rng, teto=None):
    """PACING + corpo do CTA + GATE somam num take so', e ninguem olhava.

    ⛔ ORDEM DELIBERADA: o corpo do CTA sai primeiro (carrega a isca e o
    literal `Comment gelatin,`, intocavel pela automacao de DM), o pacing
    depois, e o GATE por ULTIMO — o gate e' o beat intercambiavel do trio,
    entao e' ele que absorve a sobra em vez de ser cortado pelo fim do take.
    ⚠️ Fallback = a entrada mais CURTA, NUNCA `or pool`.
    """
    teto = TETO_FALA[3] if teto is None else teto
    corpo = lambda c: c.replace("{pacing}", "").replace("{gate}", "").strip()
    min_p = min(_palavras(x) for x in PACING)
    min_g = min(_palavras(x) for x in GATES)
    vc = [c for c in CTAS if _palavras(corpo(c)) + min_p + min_g <= teto]
    cta = rng.choice(vc or [min(CTAS, key=lambda c: _palavras(corpo(c)))])
    n_c = _palavras(corpo(cta))
    vp = [p for p in PACING if n_c + _palavras(p) + min_g <= teto]
    pac = rng.choice(vp or [min(PACING, key=_palavras)])
    vg = [g for g in GATES
          if n_c + _palavras(pac) + _palavras(g) <= teto]
    gate = rng.choice(vg or [min(GATES, key=_palavras)])
    return cta.format(pacing=pac, gate=gate)


def _fundir(spec, rng):
    o = sc.orgao_de(_MOTOR_LONGO, spec["falas_base"][3])
    idade = _idade_slots(spec["mulher"]["idade"])
    # ⚠️ sem `or FUNDIDAS`: lista vazia e' resposta legitima e quem decide e'
    # o chamador. `or pool` devolveria tudo e reintroduziria o estouro.
    cabem = [f for f in FUNDIDAS
             if _palavras(f.format(o=o, **idade)) <= TETO_FALA[2]]
    esc = (rng.choice(cabem) if cabem
           else min(FUNDIDAS, key=lambda f: _palavras(f.format(o=o, **idade))))
    return esc.format(o=o, **idade)


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
    for eixo, val in (("cozinha", spec["cozinha"]["id"]),
                      ("quintal", spec["quintal"]["id"]),
                      ("prop", spec["prop"]["id"])):
        p.setdefault(eixo, []).append(val)
        p[eixo] = p[eixo][-12:]
    with open(LEDGER, "w", encoding="utf-8") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)


def sortear(pagina, rng, ledger, travas=None):
    return sc.sortear_curto(_MOTOR_LONGO, pagina, rng, ledger, MAPA,
                            _fundir, MAPA_COPY, travas)


def montar(spec):
    # ⛔ trava de texto queimado em todo TAKE — o watermark que o
    # operador viu vazando nos reels da concorrente (2026-08-01).
    return sc.selar_takes(sc.montar_curto(_MOTOR_LONGO, spec, MAPA))


def nova_fala(spec, i, rng):
    return sc.nova_fala_curta(_MOTOR_LONGO, spec, i, rng, MAPA, _fundir, MAPA_COPY)


EIXOS_QUE_MEXEM_NA_COPY = {}


# ---------------------------------------------------------------------------
# LINTER
# ---------------------------------------------------------------------------

def _hook(spec, blocos, achados):
    h = spec["falas"][0].lower()
    if not any(n.lower() in h for n in NUCLEO):
        achados.append(("ERRO", "o hook nao nomeia o orgao com substantivo"))
    if "blood flow" not in h:
        achados.append(("ERRO", "o hook nao nomeia o mecanismo (blood flow)"))


def _v6_negacao(spec, blocos, achados):
    """A virada virou a cena 2 do SHORT, mas a negacao continua obrigatoria."""
    f2 = spec["falas"][1].lower()
    if not any(n.lower() in f2 for n in NUCLEO):
        achados.append(("ERRO", "V6: a virada nao nomeia o orgao na mesma frase"))
    if "blood flow" not in f2:
        achados.append(("ERRO", "V6: falta o MUP emendado (o fluxo estrangulado)"))


def _blocos_travados(spec, blocos, achados):
    i1 = sc.bloco_base(blocos, MAPA, "IMAGE", 1)
    t1 = sc.bloco_base(blocos, MAPA, "TAKE", 1)
    for txt, s, rot in ((i1, GEODUCK_IMAGE, "geoduck V1"),
                        (i1, VAZAMENTO_IMAGE, "vazamento V2"),
                        (t1, GEODUCK_TAKE, "imobilidade V1"),
                        (t1, VAZAMENTO_TAKE, "poca V2")):
        if s not in txt:
            achados.append(("ERRO", "a cena do vazamento sem a string travada: %s" % rot))

    # V12 — a cena do casal virou a 2 do SHORT; a declaracao de idade dos DOIS
    # continua sendo o que segura o classificador
    i4 = sc.bloco_base(blocos, MAPA, "IMAGE", 4)
    if "fully clothed adults" not in i4:
        achados.append(("ERRO", "V12: a cena do casal sem a linha de abertura "
                                "declarando 'two fully clothed adults' com as "
                                "duas idades"))
    if i4.count("-year-old") < 2:
        achados.append(("ERRO", "V12: idade dos dois precisa estar em TODA mencao "
                                "na cena do casal (falha de classificador "
                                "documentada)"))

    # V10 — os DOIS sets sobrevivem agora que a cena 3 e' a bancada externa
    if "American flag" not in i1:
        achados.append(("AVISO", "V10: sem bandeira dos EUA no set interno"))
    if "American flag" not in sc.bloco_base(blocos, MAPA, "IMAGE", 2):
        achados.append(("AVISO", "V10: sem bandeira dos EUA no set externo"))

    # V8 — as cenas solo que sobraram
    for cena in (1, 2):
        nome = "IMAGE %02d/03" % (MAPA.index(cena) + 1)
        if "alone in the frame" not in blocos[nome]:
            achados.append(("AVISO", "V8: %s nao declara que ele esta sozinho" % nome))


def _bandeira_5050(spec, blocos, achados):
    """⭐ A BANDEIRA E' 50/50, e some INTEIRA quando o sorteio diz que nao.

    ⛔ Ordem do operador, 2026-08-04. Ate' aqui ela estava escrita DENTRO das
    strings de COZINHAS e QUINTAIS — nao havia eixo, havia texto.
    ⚠️ Varre o TEXTO MONTADO e cobra os dois lados, mais a prosa: remocao por
    regex em prosa erra em silencio.
    """
    sc.lint_bandeira(spec, blocos, achados, rotulo="bandeira 50/50")


def lint(spec, blocos):
    return sc.lint_curto(
        _MOTOR_LONGO, spec, blocos, MAPA, TETO_FALA,
        literais=("gelatin trick", "without the gelatin trick", "blood flow"),
        extras=(_hook, _v6_negacao, _blocos_travados,
                _bandeira_5050))


# ---------------------------------------------------------------------------
# RESUMO
# ---------------------------------------------------------------------------

def resumo_pt(spec):
    et = "branca" if "white" in ETNIA[spec["pagina"]] else "negra"
    return ("Na %s, o corpo-prova de %d anos segura o geoduck que vaza. Na cena "
            "2 vem a receita incompleta e a prova com a moça, e na 3 o CTA. "
            "Três cenas, elenco de pele %s."
            % (PT_COZ.get(spec["cozinha"]["id"], "cozinha"),
               spec["ref"]["idade"], et))
