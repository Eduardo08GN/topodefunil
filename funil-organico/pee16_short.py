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
PLATEIA_IMAGE = (
    "four blurred shoppers standing behind them, hands over their mouths "
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
ANTICELEB = "Ordinary relatable face, not a celebrity."
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
]

# PE9 — contraste ≥3 eixos garantido por CONSTRUCAO: o narrador sempre tem
# cabeleira farta, e' barbeado e nao usa oculos; a vitima e' sempre careca,
# de bigode e de oculos. Nenhuma verificacao necessaria (F4b).
REFS = [
    {"idade": 66, "marca": "full silver hair and a notched left ear",
     "cabelo": "silver", "roupa": "Plain navy crew-neck tee shirt.",
     "roupa_curta": "navy tee shirt"},
    {"idade": 64, "marca": "full gray hair and a clean pale scar through his left eyebrow",
     "cabelo": "gray", "roupa": "Plain olive crew-neck tee shirt.",
     "roupa_curta": "olive tee shirt"},
    {"idade": 68, "marca": "thick white hair and a deep cleft in his chin",
     "cabelo": "white", "roupa": "Plain charcoal crew-neck tee shirt.",
     "roupa_curta": "charcoal tee shirt"},
    {"idade": 65, "marca": "full salt-and-pepper hair and a gold crown on one front tooth",
     "cabelo": "salt-and-pepper", "roupa": "Plain slate blue crew-neck tee shirt.",
     "roupa_curta": "slate blue tee shirt"},
    {"idade": 67, "marca": "thick silver hair and a prominent dark mole on his left cheekbone",
     "cabelo": "silver", "roupa": "Plain black crew-neck tee shirt.",
     "roupa_curta": "black tee shirt"},
    # + 2026-08-01: o operador mediu vicio — o mesmo rosto voltando no lote.
    # Pool ampliado; o contraste de 3 eixos com a VITIMA continua por construcao.
    {"idade": 63, "marca": "a full head of wavy iron-gray hair and a wide gap between his front teeth",
     "cabelo": "iron-gray", "roupa": "Plain forest green crew-neck tee shirt.",
     "roupa_curta": "forest green tee shirt"},
    {"idade": 62, "marca": "thick gray hair swept straight back and a birthmark the size of a dime above his right eyebrow",
     "cabelo": "gray", "roupa": "Plain rust orange crew-neck tee shirt.",
     "roupa_curta": "rust orange tee shirt"},
    {"idade": 66, "marca": "thick salt-and-pepper hair parted on the side and a thin pale scar along his jawline",
     "cabelo": "salt-and-pepper", "roupa": "Plain brown crew-neck tee shirt.",
     "roupa_curta": "brown tee shirt"},
    {"idade": 64, "marca": "a full head of gray hair with a bright white streak at his left temple and a deep dimple in his chin",
     "cabelo": "gray", "roupa": "Plain teal crew-neck tee shirt.",
     "roupa_curta": "teal tee shirt"},
    # + 2026-08-02: o operador mediu o pool inteiro e viu SEMPRE O MESMO ROSTO.
    # As nove acima descrevem o narrador so' por CABELO mais uma ancora — nove
    # homens descritos so' por cabelo sao o mesmo homem nove vezes, e o gerador
    # devolvia quase a mesma cara. As quatro novas trazem os eixos rasos daqui:
    #   · 71 — PORTE de rosto (longo e estreito) mais PELE de idade (mancha
    #     senil na tempora).
    #   · 61 — PELE (rugas fundas em leque no canto dos olhos) mais ancora de
    #     lobulo rasgado, mesma familia da orelha entalhada ja' usada aqui.
    #   · 73 — PORTE de rosto (olhos fundos sob arcada pesada) mais ancora de
    #     cicatriz limpa no labio.
    #   · 69 — PORTE de corpo (armacao longa e esgalgada) mais ancora de
    #     sobrancelhas unidas numa linha so'.
    #   · a ancora e' sempre do lado ✅ de licoes-producao-veo §REF —
    #     DISTINTIVO, NUNCA DETERIORADO. ⛔ dente lascado, palpebra caida e
    #     nariz quebrado ficaram de fora: viram mendigo e matam a credibilidade.
    #   · OCULOS, PELO FACIAL e CALVICIE continuam ZERADOS aqui DE PROPOSITO
    #     (PE9/F4b): sao os tres eixos que pertencem a' VITIMA. Enche-los no
    #     narrador destrui o contraste de 3 eixos que nasce por construcao.
    #   · zero mencao a etnia: o motor injeta ETNIA[pagina] antes da marca.
    {"idade": 71, "marca": "a thick snow-white mane brushed back over his ears, a long narrow face, and a dark age spot the size of a nickel on his right temple",
     "cabelo": "snow-white", "roupa": "Plain tan crew-neck tee shirt.",
     "roupa_curta": "tan tee shirt"},
    {"idade": 61, "marca": "a full head of ash-gray hair long enough to curl at his collar, deep lines fanning from the corners of his eyes, and a torn right earlobe",
     "cabelo": "ash-gray", "roupa": "Plain faded red crew-neck tee shirt.",
     "roupa_curta": "faded red tee shirt"},
    {"idade": 73, "marca": "a thick pewter flat-top cut, deep-set eyes under a heavy brow, and a pale scar splitting his upper lip",
     "cabelo": "pewter", "roupa": "Plain heather gray crew-neck tee shirt.",
     "roupa_curta": "heather gray tee shirt"},
    {"idade": 69, "marca": "a heavy gray-brown mop combed forward over his forehead, a long rangy frame, and thick eyebrows that meet in a single line above his nose",
     "cabelo": "gray-brown", "roupa": "Plain dusty blue crew-neck tee shirt.",
     "roupa_curta": "dusty blue tee shirt"},
]

VITIMAS = [
    {"idade": 63, "marca": "bald man with a thick gray mustache and black-framed glasses",
     "camisa": "a pale blue t-shirt"},
    {"idade": 62, "marca": "bald man with a red mustache and wire-rimmed glasses",
     "camisa": "a white polo shirt"},
    {"idade": 65, "marca": "bald man with a white mustache and thick square glasses",
     "camisa": "a light gray t-shirt"},
    {"idade": 61, "marca": "bald man with a short gray mustache and round wire glasses",
     "camisa": "a pale yellow polo shirt"},
    # + 2026-08-01: o operador mediu vicio — a mesma vitima voltando no lote.
    # Pool ampliado; careca + bigode + oculos continua travado.
    {"idade": 64, "marca": "bald man with a bushy salt-and-pepper mustache and gold aviator glasses",
     "camisa": "a faded sage green t-shirt"},
    {"idade": 60, "marca": "bald man with a thin white mustache and rimless glasses",
     "camisa": "a cream henley shirt"},
    {"idade": 66, "marca": "bald man with a drooping gray mustache and heavy tortoiseshell glasses",
     "camisa": "a pale pink polo shirt"},
    {"idade": 63, "marca": "bald man with a gray horseshoe fringe, a wide silver mustache and half-rim reading glasses",
     "camisa": "a light peach t-shirt"},
    {"idade": 67, "marca": "bald man with a close-trimmed sandy mustache and oval brown-framed glasses",
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
    {"idade": 69, "marca": "bald man with a heavy build and jowls, a full snow-white walrus mustache, small half-moon glasses low on his nose and a raised mole beside one nostril",
     "camisa": "a washed-out lavender bowling shirt"},
    {"idade": 68, "marca": "bald man with a soft middle and liver-spotted temples, a thin mustache dyed too dark for his age, chunky red plastic glasses and a deep dimple in his left cheek",
     "camisa": "a washed tan plaid flannel shirt"},
    {"idade": 56, "marca": "bald man with a tall rangy frame and a prominent Adam's apple, a thick charcoal mustache gray only at the tips, plain metal glasses with clip-on sun lenses flipped up and a bump in the bridge of his nose",
     "camisa": "a loose seafoam green fishing shirt"},
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
    {"idade": 66,
     "payoff": "with a small, slight frame and a deeply lined face, thin "
               "white hair set in tight permed curls, reading glasses on a "
               "beaded chain and a dark mole beside her right nostril, in a "
               "printed housedress under a soft blue cardigan"},
    {"idade": 57,
     "payoff": "with broad shoulders and sun-weathered skin, her hair in a "
               "high messy topknot and a thin scar through her right "
               "eyebrow, in a moss green shirt dress with the sleeves "
               "rolled up"},
    {"idade": 63,
     "payoff": "with a short, round frame, hair dyed flat dark brown under a "
               "blunt fringe, half-moon reading glasses low on her nose and "
               "a raised mole on her chin, in a camel knit twinset and a "
               "single strand of pearls"},
    {"idade": 64,
     "payoff": "with a heavy-set frame, a shaggy shoulder-length "
               "gray-and-black cut, sunglasses pushed up on her head and a "
               "wide gap between her front teeth, in an orange tunic top and "
               "white capri pants"},
    {"idade": 65,
     "payoff": "with a tall, narrow build, a long face and thick freckles "
               "across her nose, fine silver hair swept back into a "
               "tortoiseshell comb and a chunky amber ring, in a gray "
               "sweater and a long denim skirt"},
    {"idade": 53,
     "payoff": "with a wiry, broad-shouldered build and deep laugh lines "
               "around her mouth, short spiky ash-blond hair growing out at "
               "the roots, thick red-framed glasses and a small scar at the "
               "corner of her mouth, in a checked blue-and-white blouse and "
               "dark jeans"},
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
        "REF 01: Photo of a real person, a %d-year-old %s man, chest up, facing camera, "
        "a wide warm natural smile with the lips parted, showing a full row of clean white teeth, the front teeth even, white and complete. The dense build of a man who lifts, thick through the "
        "chest and shoulders, forearms corded, skin taut and even. %s. "
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
           ref["idade"], et, ref["marca"], NARRADOR_IMAGE, PLATEIA_IMAGE,
           ANTICELEB, loc["luz"], CAUDA)
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
MODO_FORTE = True

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
    i2, t2 = sc.bancada_com_rosto(_LONGO, spec, spec["falas"][1], n=2, total=2)
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
    for s, rot in ((CHORO_IMAGE, "choro PE2"),
                   (NARRADOR_IMAGE, "narrador PE3"),
                   (PLATEIA_IMAGE, "plateia PE4")):
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
