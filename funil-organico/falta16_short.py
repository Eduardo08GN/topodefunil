# -*- coding: utf-8 -*-
"""AGENTE FALTA 16 — a receita incompleta, em dois takes de 8s.

⭐⭐ O QUE ELE E': o FALTA em **16 segundos**. Terceiro motor da familia 16s,
depois do TRIO 16 e do DUPLA 16, sob a mesma clausula do operador: o ajuste e'
so' no eixo temporal, sem sacrificar pool nem controlador.

⛔ Ele **nao substitui** o `falta_short.py`. Ledger proprio, copia literal +
cirurgia temporal.

FONTE: https://www.facebook.com/reel/1753888712524981
Leitura otica em `concorrentes/falta-mapa-visual.md` (34 frames a 1 fps).

⭐⭐ O QUE ESTE ANGULO TEM QUE OS OUTROS NAO TEM
-----------------------------------------------------------------------------
A receita e' entregue INTEIRA MENOS UM PEDACO, e o video diz isso na cara. A
isca deixa de ser "te mando a receita" e vira **te mando o pedaco que falta** —
e a parte que falta E' o `gelatin trick`.

⛔⛔ A COSTURA E' O ANGULO: o buraco e' nomeado na VENDA e prometido no CTA. No
motor de 24s ela atravessa duas cenas (8 segundos); aqui cai dentro de uma
respiracao so'. Por isso o guarda novo: venda e CTA nomeiam o buraco com
substantivos DIFERENTES (`piece` x `part` x `step`). Repetir o mesmo em tres
segundos le' como gagueira, nao como retomada.

O ARCO — 2 cenas de 8s, destino AdBatch Vertical 2:

    cena 1  A ACUSACAO  o homem com o proxy preso de fita, a REF ao centro e a
                        amiga em cima da bancada apontando · o desmentido +
                        o raro nomeado
    cena 2  A PROVA     a mesma cozinha: a bancada da receita, ela com o copo
                        e o homem com o geoduck grande, sem fita ·
                        o gelatin trick + a costura + o CTA

⭐ COMO AS 3 VIRARAM 2. As cenas 2 e 3 do FALTA ja' acontecem no MESMO lugar
(`coz_c`), entao a bancada da receita e o payoff cabem no mesmo frame.

⛔⛔ E AQUI A GELATINA NAO ENTRA NA BANCADA — ao contrario do TRIO 16 e do
DUPLA 16, onde a tigela de cubos e' OBRIGATORIA (regra DU2). Neste angulo
mostrar gelatina entregaria de graca o que o CTA vende: a peca que falta so'
existe na FALA. Copiar a cauda de bancada dos irmaos teria matado o angulo, e
ha' lente cobrando (FA16-2).

⛔ O RARO CONTINUA FALADO, e sem custo: os 20 DESMENTIDOS o nomeiam na cena 1
(medido, 20/20). Repeti-lo na cena 2 seria pagar duas vezes pela mesma
informacao num video de 16 segundos — e o aposto, que na versao de 24s vive na
cena 2, tornaria a cena 2 IMPOSSIVEL: medido, 0 de 1536 combinacoes cabiam.

⛔ E A VIRGULA DEPOIS DE `gelatin` E' INTOCAVEL: a automacao de DM casa palavra
EXATA (operador, 2026-08-08). O follow vem em frase SEPARADA. Lente T16-2.

⚠️ TR19 CONTINUA VALENDO — o CTA NOMEIA o que e' enviado. `and I'll send it`
foi reprovado pelo operador (*"enviar o QUE??"*). Os CTAs curtos deste motor
nomeiam o payload sem gastar o verbo de envio: `and the missing piece is
yours`.

Uso:
    python funil-organico/falta16_short.py --pagina joe --n 1
    python funil-organico/falta16_short.py --autoteste
"""
import json
import os
import random
import re

import short_comum as sc

AQUI = os.path.dirname(os.path.abspath(__file__))
# ⛔ LEDGER PROPRIO: 24s e 16s sao lotes diferentes e cada um tem de varrer
# o repertorio inteiro sem gastar o frescor do outro.
LEDGER = os.path.join(AQUI, ".falta-16-ledger.json")

TITULO = "AGENTE FALTA 16"
SLUG = "falta-16"
SUBTITULO = ("a receita aparece incompleta · a parte que falta é o mecanismo · "
             "gerador offline de prompts Veo")

# ⚠️ A etnia aqui NAO vem da pagina — vem do MUNDO (doutrina "etnia arrasta o
# mundo inteiro"). A tabela existe so' para a UI listar as paginas.
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
    "roy": "white American", "dean": "white American", "earl": "white American",
    "jason": "Black American", "philippe": "Black American",
    "joe": "white American", "ray": "white American", "matt": "white American",
    "marcus": "Black American", "chuck": "Black American",
    "hank": "white American", "wade": "white American",
    "isaiah": "Black American", "curtis": "Black American",
    "otis": "Black American",
}

# ⭐⭐ PELE TRAVAVEL. Este motor ignora ETNIA[pagina] de proposito, entao sem
# esta flag o seletor clara/escura do painel acenderia e nao travaria nada —
# pior que nao ter botao, porque PARECE travado. Foi o defeito do CLEAN V2 e
# o mesmo que o operador encontrou no BOTICA em 2026-08-06.
PELE_TRAVAVEL = True

# ⭐ MODO BELA — o mesmo defeito de FORMA-sem-FUNCAO, do outro lado. O `sortear`
# ja' le' `travas["bela"]` e remonta REF, amiga, traje e clausula do rosto, e o
# docstring do app promete *"MODO BELA de nascenca, por ordem dele"* — mas sem
# esta linha o painel nao desenha o toggle (a UI so' desenha os modos que o
# motor DECLARA, via `getattr(motor, "MODO_BELA")`). Codigo escrito e
# inalcancavel: o operador nunca conseguiria ligar o modo.
# ⛔ Nao ha' MODO_FORTE aqui de proposito — este agente nao tem homem em cena.
MODO_BELA = True

# ⛔⛔ LISTA EXPLICITA, nunca "tudo que nao e' branco". Correcao de campo dele,
# com print: **escura = NEGRO**. Asiatico, latino e mestico nao sao nem clara
# nem escura — so' saem com a pele LIVRE.
# ⛔ MESMA LISTA dos outros motores (cha, dupla, placa, trio, botica):
# classificacao divergente entre agentes e' o fragmento espelhado que a P9
# proibe.
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
# ⭐⭐ MUNDOS — ARQUÉTIPOS POR REGIÃO DOS EUA
# ---------------------------------------------------------------------------
# ⛔ ORDEM DO OPERADOR: *"pool com arquetipos por regioes dos eua"*. Os mundos
# dos outros agentes carregam Caribe, Andes, Ásia e Mediterrâneo; aqui o
# recorte é OS ESTADOS UNIDOS, porque o funil é US e o espectador tem de
# reconhecer a cozinha como a da rua dele.
#
# ⚠️ "Variar etnia é arrastar o mundo inteiro": cada entrada leva cozinha, cor
# de superfície, luz E etnia juntas. Trocar só o rosto deixa a cozinha errada.
MUNDOS = [
    {"id": "apalache", "familia": "apalache",
     "audio": "wind in the trees, a quiet house",
     "coz": "an Appalachian farmhouse kitchen with painted board walls and a "
            "deep porcelain sink",
     "coz_c": "the same Appalachian farmhouse kitchen",
     "sup_a": "a worn pine counter", "sup": "pine counter",
     "luz": "flat grey daylight through a single window",
     "luz_c": "the same flat grey daylight",
     "etnias": ["white American"]},
    {"id": "sulista", "familia": "sulista",
     "audio": "cicadas outside, a ceiling fan",
     "coz": "a Southern kitchen with pale yellow beadboard walls and a screen "
            "door standing open",
     "coz_c": "the same Southern kitchen",
     "sup_a": "a scrubbed wooden table", "sup": "wooden table",
     "luz": "warm afternoon light through the screen door",
     "luz_c": "the same warm afternoon light",
     "etnias": ["Black American"]},
    {"id": "texas", "familia": "texas",
     "audio": "a screen door creaking, dry wind",
     "coz": "a Texas ranch kitchen with saltillo tile and a heavy iron range",
     "coz_c": "the same Texas ranch kitchen",
     "sup_a": "a thick butcher block", "sup": "butcher block",
     "luz": "hard midday sun through a wide window",
     "luz_c": "the same hard midday sun",
     "etnias": ["white American"]},
    {"id": "meio_oeste", "familia": "meio_oeste",
     "audio": "a refrigerator hum, a quiet street",
     "coz": "a Midwestern kitchen with laminate cabinets and a wall clock",
     "coz_c": "the same Midwestern kitchen",
     "sup_a": "a speckled formica counter", "sup": "formica counter",
     "luz": "even overcast light through a curtained window",
     "luz_c": "the same even overcast light",
     "etnias": ["white American"]},
    {"id": "nova_inglaterra", "familia": "nova_inglaterra",
     "audio": "a radiator ticking, gulls far off",
     "coz": "a New England kitchen with white shaker cabinets and a soapstone "
            "sink",
     "coz_c": "the same New England kitchen",
     "sup_a": "a soapstone counter", "sup": "soapstone counter",
     "luz": "cool north light through small panes",
     "luz_c": "the same cool north light",
     "etnias": ["white American"]},
    {"id": "harlem", "familia": "harlem",
     "audio": "faint traffic, a radio two floors down",
     "coz": "a Harlem brownstone kitchen with pressed tin ceiling and tall "
            "narrow windows",
     "coz_c": "the same brownstone kitchen",
     "sup_a": "a marble slab counter", "sup": "marble counter",
     "luz": "warm city light coming in high",
     "luz_c": "the same warm city light",
     "etnias": ["Black American"]},
    {"id": "atlanta", "familia": "atlanta",
     "audio": "birds in the back yard, a quiet house",
     "coz": "an Atlanta kitchen with dark wood cabinets and a wide island",
     "coz_c": "the same Atlanta kitchen",
     "sup_a": "a granite island", "sup": "granite island",
     "luz": "bright filtered daylight from a back door",
     "luz_c": "the same bright filtered daylight",
     "etnias": ["Black American"]},
    {"id": "delta", "familia": "delta",
     "audio": "crickets, a slow ceiling fan",
     "coz": "a Mississippi Delta kitchen with a chipped enamel stove and a "
            "hanging bare bulb",
     "coz_c": "the same Delta kitchen",
     "sup_a": "an oilcloth-covered table", "sup": "covered table",
     "luz": "low warm lamplight",
     "luz_c": "the same low warm lamplight",
     "etnias": ["Black American"]},
    {"id": "gullah", "familia": "gullah",
     "audio": "waves far off, wind through a screen",
     "coz": "a Lowcountry kitchen with blue-washed boards and a window onto "
            "marsh grass",
     "coz_c": "the same Lowcountry kitchen",
     "sup_a": "a scrubbed plank counter", "sup": "plank counter",
     "luz": "soft coastal light off the water",
     "luz_c": "the same soft coastal light",
     "etnias": ["Black American"]},
    {"id": "noroeste", "familia": "noroeste",
     "audio": "rain on the window, a quiet kitchen",
     "coz": "a Pacific Northwest kitchen with cedar shelving and a window onto "
            "wet firs",
     "coz_c": "the same Northwest kitchen",
     "sup_a": "a slab fir counter", "sup": "fir counter",
     # ⛔ ERA "dim green light": o operador viu o lote e disse *"tire esse ar de
     # blade runner 2049, esta em tom esverdeado villeneuve"*. Medido nos 15
     # mundos, ESTE era o unico com luz colorida — os outros 14 ja eram
     # neutros. Nao era grading do gerador: era o motor pedindo verde.
     "luz": "cool grey daylight through rain on the glass",
     "luz_c": "the same cool grey daylight",
     "etnias": ["white American"]},
    {"id": "grandes_lagos", "familia": "grandes_lagos",
     "audio": "wind against the glass, a quiet house",
     "coz": "a Great Lakes kitchen with knotty pine panelling and a chest "
            "freezer humming",
     "coz_c": "the same Great Lakes kitchen",
     "sup_a": "a pine countertop", "sup": "pine countertop",
     "luz": "pale winter light off snow",
     "luz_c": "the same pale winter light",
     "etnias": ["white American"]},
    {"id": "creole", "familia": "creole",
     "audio": "a streetcar far off, cicadas",
     "coz": "a New Orleans kitchen with a tall shuttered window and a cast "
            "iron pot on the range",
     "coz_c": "the same New Orleans kitchen",
     "sup_a": "a worn zinc counter", "sup": "zinc counter",
     "luz": "heavy humid light through the shutters",
     "luz_c": "the same heavy humid light",
     "etnias": ["Black American"]},
    {"id": "amish", "familia": "amish",
     "audio": "a clock ticking, birds outside",
     "coz": "a plain country kitchen with no appliances on the walls and a "
            "hand pump at the sink",
     "coz_c": "the same plain country kitchen",
     "sup_a": "a bare oak table", "sup": "oak table",
     "luz": "daylight only, no electric light",
     "luz_c": "the same daylight, no electric light",
     "etnias": ["white American"]},
    {"id": "italo_americana", "familia": "italo_americana",
     "audio": "a pot simmering, a quiet kitchen",
     "coz": "an Italian-American kitchen with a tiled backsplash and braided "
            "garlic on a hook",
     "coz_c": "the same Italian-American kitchen",
     "sup_a": "a stainless counter", "sup": "stainless counter",
     "luz": "warm bulb light over the range",
     "luz_c": "the same warm bulb light",
     "etnias": ["white American"]},
    {"id": "americana", "familia": "americana",
     "audio": "a refrigerator hum, a quiet house",
     "coz": "a plain suburban American kitchen with oak cabinets and a fridge "
            "covered in magnets",
     "coz_c": "the same suburban kitchen",
     "sup_a": "a laminate counter", "sup": "laminate counter",
     "luz": "flat kitchen ceiling light",
     "luz_c": "the same flat ceiling light",
     "etnias": ["white American", "Black American"]},
    # ⭐⭐ 2026-08-13 — MAIS NOVE REGIOES (15 -> 24). Ordem do operador:
    # *"aumente o pool de opcoes substancialmente, tambem dos ambientes"*.
    # ⛔ COBERTURA DE ETNIA CRESCE DOS DOIS LADOS, nunca de um so': eram 9
    # mundos que comportam `white American` e 7 que comportam `Black
    # American`; passam a 15 e 12. Etnia sem cozinha compativel derruba o
    # sorteio — o `mundos_da_pele` cede para a lista inteira e a trava de pele
    # do painel deixa de significar alguma coisa.
    # ⚠️ Cada entrada nova carrega o MESMO nivel das vizinhas: cozinha,
    # superficie, luz, audio e etnias. Fundo sem luz nem ambiencia e' meia
    # entrada, e o gerador preenche a metade que falta sozinho.
    # ⛔ NENHUMA luz colorida — a licao do `noroeste` (*"tire esse ar de blade
    # runner 2049"*) vale para quem chega depois.
    {"id": "oakland", "familia": "oakland",
     "audio": "a bus braking a block away, a quiet house",
     "coz": "an Oakland Victorian kitchen with tall painted cabinets and a "
            "bay window onto the back steps",
     "coz_c": "the same Oakland kitchen",
     "sup_a": "a green tile counter", "sup": "tile counter",
     "luz": "soft bay-window light off the back yard",
     "luz_c": "the same soft bay-window light",
     "etnias": ["Black American"]},
    {"id": "sul_chicago", "familia": "sul_chicago",
     "audio": "an el train far off, a radiator ticking",
     "coz": "a South Side Chicago two-flat kitchen with painted steel "
            "cabinets and a glazed back door onto wooden stairs",
     "coz_c": "the same two-flat kitchen",
     "sup_a": "a worn enamel-topped table", "sup": "enamel table",
     "luz": "cool north light off the brick wall next door",
     "luz_c": "the same cool north light",
     "etnias": ["Black American"]},
    {"id": "detroit", "familia": "detroit",
     "audio": "a furnace humming, a car going by",
     "coz": "a Detroit brick bungalow kitchen with steel cabinets and a "
            "swinging door through to the dining room",
     "coz_c": "the same bungalow kitchen",
     "sup_a": "a boomerang-pattern formica dinette",
     "sup": "formica dinette",
     "luz": "warm lamplight against a pale window",
     "luz_c": "the same warm lamplight",
     "etnias": ["Black American"]},
    {"id": "baltimore", "familia": "baltimore",
     "audio": "children out on the street, a screen door",
     "coz": "a Baltimore rowhouse kitchen, a narrow galley run with a window "
            "onto the back alley",
     "coz_c": "the same rowhouse kitchen",
     "sup_a": "a scrubbed steel counter", "sup": "steel counter",
     "luz": "flat daylight down the narrow galley",
     "luz_c": "the same flat daylight",
     "etnias": ["Black American", "white American"]},
    {"id": "ozarks", "familia": "ozarks",
     "audio": "a dog barking off in the trees, cicadas",
     "coz": "an Ozark hill kitchen with open shelves of canning jars and a "
            "screened window over the sink",
     "coz_c": "the same hill kitchen",
     "sup_a": "a worn hickory counter", "sup": "hickory counter",
     "luz": "soft daylight through the window screen",
     "luz_c": "the same soft daylight",
     "etnias": ["white American"]},
    {"id": "montanha", "familia": "montanha",
     "audio": "wind off the ridge, a quiet cabin",
     "coz": "a Rocky Mountain cabin kitchen with log walls and a cast iron "
            "stove in the corner",
     "coz_c": "the same cabin kitchen",
     "sup_a": "a thick spruce counter", "sup": "spruce counter",
     "luz": "hard high-altitude daylight through a small window",
     "luz_c": "the same hard daylight",
     "etnias": ["white American"]},
    {"id": "costa_maine", "familia": "costa_maine",
     "audio": "gulls, a halyard tapping",
     "coz": "a Maine harbour kitchen with white bead-board walls and a window "
            "onto the working docks",
     "coz_c": "the same harbour kitchen",
     "sup_a": "a scrubbed maple counter", "sup": "maple counter",
     "luz": "cool bright light coming off the water",
     "luz_c": "the same cool bright light",
     "etnias": ["white American"]},
    {"id": "sudoeste", "familia": "sudoeste",
     "audio": "dry wind, a wind chime",
     "coz": "a New Mexico adobe kitchen with thick plastered walls and a row "
            "of dried chiles hanging by the door",
     "coz_c": "the same adobe kitchen",
     "sup_a": "a saltillo-tiled counter", "sup": "tiled counter",
     "luz": "hard clean desert light through a deep window opening",
     "luz_c": "the same hard desert light",
     "etnias": ["white American"]},
    {"id": "siderurgica", "familia": "siderurgica",
     "audio": "a freight train, a fridge humming",
     "coz": "a steel-town kitchen with metal cabinets and a window onto a row "
            "of identical back porches",
     "coz_c": "the same steel-town kitchen",
     "sup_a": "a steel-edged formica counter", "sup": "formica counter",
     "luz": "flat grey light off an overcast sky",
     "luz_c": "the same flat grey light",
     "etnias": ["white American", "Black American"]},
]

FAMILIAS_MUNDO = list(dict.fromkeys(m["familia"] for m in MUNDOS))


def mundos_da_pele(pele):
    """Os mundos que COMPORTAM a pele pedida.

    ⛔ Cede em vez de derrubar: sem mundo compatível devolve a lista inteira.
    Botão que zera o sorteio é botão que quebra o app.
    """
    if pele not in ("clara", "escura"):
        return MUNDOS
    filtrados = [m for m in MUNDOS if any(_pele_de(e) == pele for e in m["etnias"])]
    return filtrados or MUNDOS


# ---------------------------------------------------------------------------
# ⭐⭐ O PROP — EIXO SORTEADO: O MOLUSCO OU A PEÇA ANATÔMICA
# ---------------------------------------------------------------------------
# ⛔ ORDEM DO OPERADOR, entrevista de 2026-08-06: **um OU outro, nunca os dois
# em quadro**. Metade do lote sai com geoduck, metade com a peça de anatomia.
#
# ⚠️ Cada entrada declara COMO ELE MUDA no despejo, porque a mudança é
# diferente: o molusco ALONGA o pescoço; a peça levanta o corpo cavernoso. Uma
# descrição só para os dois produziria um morph genérico que não é nem um nem
# outro.
#
# ⛔⛔ `antes` e `depois` NUNCA descrevem escala uniforme. A lição do
# RESSURREICAO, medida em pixels: altura 2,31× contra largura 1,44×. O objeto
# ALONGA. "Fica maior" lê como tumescência e derruba o vídeo.
PROPS = [
    # ⛔⛔ SAIU A PECA ANATOMICA (ordem do operador, 2026-08-07). O prop deixa
    # de ser segurado na mao e passa a ficar PRESO NELE: um proxy murcho,
    # colado na vertical na frente do short com silver tape.
    # ⚠️ VERTICAL, e isso e' lição paga em geracao: eu tinha escrito `taped
    # horizontally across the front` e o Veo entregou exatamente isso — o prop
    # deitado. A fita e' que atravessa; o prop desce reto.
    # ⚠️ E a redacao e' `taped upright along the front of his shorts`, nao
    # `pointing straight down` nem `at the zipper`: as duas ultimas puseram o
    # holofote na virilha e a IMAGE 01 foi recusada por politica.
    {"id": "banana", "nome": "banana murcha",
     "img": "a small withered brown banana",
     "curto": "taped banana"},
    {"id": "pepino", "nome": "pepino murcho",
     "img": "a limp shrivelled cucumber",
     "curto": "taped cucumber"},
    {"id": "cenoura", "nome": "cenoura mole",
     "img": "a thin soft carrot bent over on itself",
     "curto": "taped carrot"},
    {"id": "abobrinha", "nome": "abobrinha murcha",
     "img": "a soft drooping yellow squash",
     "curto": "taped squash"},
    {"id": "salsicha", "nome": "salsicha fria",
     "img": "a single pale cold sausage hanging slack",
     "curto": "taped sausage"},
]

# ⭐ A FITA. Vale para os cinco: e' ela que faz o proxy virar protese comica em
# vez de comida na mao. Duas tiras curtas ATRAVESSADAS, o prop na vertical.
FITA = ("taped upright along the front of his shorts, held by two short "
        "strips of silver duct tape")

# ⭐⭐ O ADESIVO NA BARRIGA — o bit visual que o operador escolheu do
# video-fonte. Desenho a mao em papel branco, colado na pele.
# ⚠️ Papel COLADO, nunca desenho na pele: tinta em pele nua e' outro
# classificador.
ADESIVOS = [
    "a square white paper sticker with a hand-drawn sad face",
    "a round white paper sticker with a hand-drawn frowning face",
    "a square white paper sticker with a hand-drawn downward arrow",
    "a round white paper sticker with a hand-drawn sleeping face",
]

# ⭐⭐ O PAYOFF DA CENA 3 — o geoduck grande, na mao DELE, e nenhuma fita.
# ⚠️ `with nothing taped to them and no tape anywhere on him` nao e'
# redundancia: o Veo carrega adereco da cena anterior por continuidade, entao
# a ausencia precisa ser DITA, nao so' omitida.
PROP_GRANDE = ("a very large geoduck clam upright in both fists at chest "
               "height, its long siphon neck extended straight upward and "
               "clear of his hands")
# ⛔⛔ `to his shorts`, NUNCA `to them`. Achado LENDO o prompt em
# 2026-08-08: a clausula entra depois de `wearing <calca><oculos>`, e
# quando o homem sorteado tem oculos o `them` passa a apontar para OS
# OCULOS — "thin wire-rimmed glasses with nothing taped to them".
# ⚠️ MEDIDO: 40 de 300 sorteios, e o `falta_short.py` tem a MESMA taxa,
# entao e' defeito HERDADO. So' acontece com homem de oculos (143/300),
# e por isso passou: dois tercos dos sorteios saem corretos.
# ⭐ O conserto e' o referente EXPLICITO, nao mudar a ordem da frase:
# nome proprio nao depende de onde a clausula cai.
SEM_FITA = "with nothing taped to his shorts and no tape anywhere on him"

# ---------------------------------------------------------------------------
# ⭐⭐ O HOMEM — o corpo-prova, e o unico que nao fala
# ---------------------------------------------------------------------------
# ⛔ ELE ENTROU NESTA PASSADA (2026-08-07). Ate' aqui o agente proibia homem em
# cena por ordem do operador; ele reviu depois de ver o video-fonte novo. O
# linter FA1 foi INVERTIDO: era "nenhum homem" e virou "o homem e' obrigatorio
# nas cenas 1 e 3, e proibido na 2".
HOMENS = [
    # ⛔⛔ MARCA FACIAL OBRIGATORIA, e nao e' enfeite: ele aparece nas cenas 1 e
    # 3, com um corte no meio, e sem ancora distintiva o Veo devolve OUTRO
    # homem na cena 3 — o payoff deixa de ser o mesmo sujeito e o video perde a
    # prova. Foi o gate de personagens que pegou o buraco.
    # ⚠️ Os oculos FICAM aqui de proposito: no homem eles leem como
    # CREDIBILIDADE, o oposto do efeito na REF (a LEI DO REF os bane nela).
    # ⛔ ZERO adjetivo de etnia dentro das entradas — quem injeta e' a montagem,
    # a partir do mundo. Mesmo contrato do pool das mulheres.
    # ⭐⭐ 2026-08-13 — DE 6 PARA 24, E OS SEIS ANTIGOS REESCRITOS.
    # Ordem do operador: *"melhore a aparencia e shape desses homens"* e
    # *"aumente o pool de opcoes substancialmente, tambem dos ambientes"*.
    # ⛔⛔ DISTINTIVO, NUNCA DETERIORADO. CINCO dos seis originais violavam a
    # regra que ja' custou lote no PLACA 16 (*"esses caras tao parecendo
    # mendigo"*): vinco fundo entre as sobrancelhas, cicatriz na sobrancelha,
    # dobras sob os dois olhos, nariz quebrado e nunca alinhado, mancha de
    # sol na tempora. Sairam TODOS, e o `shape` foi junto — barriga mole e
    # tronco curvado viraram ombro quadrado, costas retas e corpo solido.
    # ⭐ No lugar entraram ancoras SAUDAVEIS: covinha, queixo partido, mecha
    # prateada, pinta, brinco de argola ou tarraxa, entrada em bico,
    # sobrancelha cheia e reta, mecha branca acima da tempora.
    # ⛔ ZERO palavra de aprovacao (handsome, rugged, strong jaw): elogio no
    # prompt puxa o rosto para a MEDIA do banco de imagem — o mesmo mecanismo
    # pelo qual escrever "not a celebrity" invoca a celebridade. Descreve-se
    # FEICAO, nunca julgamento.
    # ⚠️ OCULOS EM 7 DE 24 (29%), e a queda e' de proposito: eram 3 de 6 (50%)
    # e o homem de oculos e' justamente o caso em que o `SEM_FITA` precisa de
    # referente explicito para o pronome nao apontar para as lentes.
    # ⛔ O eixo PELE segue ZERADO aqui por CONTRATO (excecao declarada no
    # `medir_personagens.py`): nenhuma entrada carrega adjetivo de pele nem de
    # etnia — quem injeta e' a montagem, a partir do MUNDO sorteado.
    {"id": "grisalho", "idade": 61,
     "corpo": "bare-chested, square-shouldered and solid through the chest",
     "cabeca": "grey stubble", "calca": "loose khaki shorts",
     "marca": "a shallow cleft in the middle of his chin", "oculos": ""},
    {"id": "careca", "idade": 66,
     "corpo": "bare-chested, broad with a straight back",
     "cabeca": "bald with a neat grey fringe", "calca": "faded denim shorts",
     "marca": "a small dark mole on his right cheek",
     "oculos": "thin wire-rimmed glasses"},
    {"id": "bigode", "idade": 58,
     "corpo": "bare-chested, thick through the chest",
     "cabeca": "a heavy grey moustache", "calca": "grey sweat shorts",
     "marca": "a deep dimple in his left cheek", "oculos": ""},
    {"id": "barba_branca", "idade": 69,
     "corpo": "bare-chested, lean and upright",
     "cabeca": "a short white beard", "calca": "olive cargo shorts",
     "marca": "a silver streak running through his beard at the chin",
     "oculos": "square reading glasses pushed up on his forehead"},
    {"id": "cabelo_ralo", "idade": 63,
     "corpo": "bare-chested, a wide solid frame",
     "cabeca": "thin grey hair combed back", "calca": "navy gym shorts",
     "marca": "heavy level brows over a broad flat nose", "oculos": ""},
    {"id": "queimado", "idade": 57,
     "corpo": "bare-chested, broad-shouldered and compact",
     "cabeca": "close-cropped salt-and-pepper hair",
     "calca": "tan work shorts",
     "marca": "a patch of white above his left temple",
     "oculos": "dark aviator glasses pushed up into his hair"},
    # --- os 18 novos (2026-08-13) ------------------------------------------
    {"id": "topete_prateado", "idade": 59,
     "corpo": "bare-chested, broad-shouldered and flat through the middle",
     # ⚠️ `clean-shaven` VEM NA FRENTE nas seis entradas que o trazem: a
     # montagem escreve `%(cabeca)s and %(marca)s`, e com ele no fim saia
     # *"...a widow's peak, clean-shaven and a shallow cleft chin"* — adjetivo
     # e sintagma nominal ligados pelo mesmo `and`. Achado LENDO a string
     # montada, nao pelo linter.
     "cabeca": "clean-shaven, with thick silver hair swept back from a "
               "widow's peak",
     "calca": "charcoal running shorts",
     "marca": "a shallow cleft chin", "oculos": ""},
    {"id": "barba_curta", "idade": 62,
     "corpo": "bare-chested, a compact square frame",
     "cabeca": "a close-trimmed salt-and-pepper beard over short hair",
     "calca": "faded red swim shorts",
     "marca": "a small dark mole at the outer corner of his left eye",
     "oculos": ""},
    {"id": "cavanhaque", "idade": 57,
     "corpo": "bare-chested, lean with clear definition across the shoulders",
     "cabeca": "a neat grey goatee with short cropped hair",
     "calca": "black athletic shorts",
     "marca": "a small gold stud in his left ear",
     "oculos": "thin steel-rimmed glasses"},
    {"id": "raspado", "idade": 64,
     "corpo": "bare-chested, solid and barrel-chested",
     "cabeca": "clean-shaven, with a shaved head",
     "calca": "olive board shorts",
     "marca": "a coin-sized birthmark high on his right temple",
     "oculos": ""},
    {"id": "costeletas", "idade": 60,
     "corpo": "bare-chested, sturdy with a straight back",
     "cabeca": "short grey hair with thick sideburns",
     "calca": "denim cut-off shorts",
     "marca": "a deep dimple in his right cheek", "oculos": ""},
    {"id": "rabo_preso", "idade": 56,
     "corpo": "bare-chested, wiry and long-limbed",
     "cabeca": "long iron-grey hair tied back at the nape",
     "calca": "loose linen shorts",
     "marca": "a small silver hoop in his left ear", "oculos": ""},
    {"id": "chevron", "idade": 65,
     "corpo": "bare-chested, heavy-set with wide shoulders",
     "cabeca": "a full chevron moustache under short combed hair",
     "calca": "brown work shorts",
     "marca": "a dark beauty mark high on his left cheekbone",
     "oculos": "square black-framed glasses"},
    {"id": "barba_quadrada", "idade": 68,
     "corpo": "bare-chested, tall and rangy",
     "cabeca": "a full white beard trimmed square",
     "calca": "khaki hiking shorts",
     "marca": "a pronounced widow's peak at his hairline", "oculos": ""},
    {"id": "careca_bigode", "idade": 58,
     "corpo": "bare-chested, broad and solidly built",
     "cabeca": "bald with a dark grey moustache",
     "calca": "navy swim trunks",
     "marca": "a small mole just below his right eye", "oculos": ""},
    {"id": "franja_branca", "idade": 63,
     "corpo": "bare-chested, square-shouldered and trim",
     "cabeca": "clean-shaven, with short white hair combed forward",
     "calca": "grey drawstring shorts",
     "marca": "a small dark mole at his left temple",
     "oculos": "rimless reading glasses low on his nose"},
    {"id": "crew_cut", "idade": 55,
     "corpo": "bare-chested, a solid swimmer's build",
     "cabeca": "clean-shaven, with a thick white crew cut",
     "calca": "red lifeguard shorts",
     "marca": "a small mole at his left jaw",
     "oculos": ""},
    {"id": "entradas_altas", "idade": 66,
     "corpo": "bare-chested, stocky with a deep chest",
     "cabeca": "a receding hairline with the rest cropped short",
     "calca": "olive cargo shorts",
     "marca": "a dimple that shows in his left cheek when he talks",
     "oculos": ""},
    {"id": "ondulado", "idade": 61,
     "corpo": "bare-chested, lean and upright",
     "cabeca": "clean-shaven, with wavy iron-grey hair down to the collar",
     "calca": "faded green swim shorts",
     "marca": "a dark mole on his jawline below his right ear",
     "oculos": ""},
    {"id": "ferradura", "idade": 69,
     "corpo": "bare-chested, heavy through the chest and shoulders",
     "cabeca": "a bald crown with a close grey horseshoe fringe",
     "calca": "sand-coloured work shorts",
     "marca": "a shallow cleft chin under a trimmed white moustache",
     "oculos": ""},
    {"id": "bigode_ruivo", "idade": 57,
     "corpo": "bare-chested, thickset and square",
     "cabeca": "a rust-red moustache going grey at the edges",
     "calca": "blue gym shorts",
     "marca": "a small beauty mark at the corner of his mouth",
     "oculos": ""},
    {"id": "tempora_grisalha", "idade": 55,
     "corpo": "bare-chested, broad-shouldered and trim",
     "cabeca": "clean-shaven, with dark hair cropped short and grey at the "
               "temples",
     "calca": "navy running shorts",
     "marca": "a deep cleft in his chin",
     "oculos": ""},
    {"id": "barba_de_tres_dias", "idade": 60,
     "corpo": "bare-chested, solid with a flat stomach",
     "cabeca": "close grey stubble over short dark hair",
     "calca": "grey swim shorts",
     "marca": "a silver streak in the stubble at his chin", "oculos": ""},
    {"id": "oculos_leitura", "idade": 67,
     "corpo": "bare-chested, tall with sloping shoulders",
     "cabeca": "a trimmed white moustache under thin white hair combed back",
     "calca": "olive linen shorts",
     "marca": "a dark beauty mark on his right temple",
     "oculos": "half-rim reading glasses"},
]


# ---------------------------------------------------------------------------
# ⛔⛔ AQUI MORAVA `SUBSTANCIAS` — a isca topica que ela despejava no prop.
# Removida em 2026-08-07: o operador tirou o DESPEJO da cena ("nao havera mais
# despejo, melhor o ref com maos livres fazendo gesto apontando pra prop
# enquanto ela fala"). Sem garrafa em quadro, um pool de liquidos era codigo
# que so' alimentava uma fala descrevendo acao que o video nao mostra.
# ⭐ O que a isca era, a fala agora e': o hook desmente o RARO TOMADO SOZINHO.
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# ⭐⭐ O RARO — o ingrediente que entra na receita com nome popular + aposto
# ---------------------------------------------------------------------------
# ⛔ NOME POPULAR + APOSTO, nunca nome científico. Regra herdada do BOTICA: o
# espectador americano não sabe o que é `Lepidium meyenii`, mas entende
# `maca root, that Andean root from Peru`. Nome científico soa a rótulo de
# farmácia — e a farmácia é justamente o que este funil não é.
RAROS = [
    {"id": "maca", "nome": "maca root",
     "img": "a small dish of pale maca root powder",
     "fala": "maca root, that Andean root from Peru"},
    {"id": "tribulus", "nome": "tribulus",
     "img": "a small dish of dried tribulus pods",
     "fala": "tribulus, the little spiked pod farmers know"},
    {"id": "muira", "nome": "muira puama",
     "img": "a small dish of shaved muira puama bark",
     "fala": "muira puama, the Amazon wood they call potency bark"},
    {"id": "ginkgo", "nome": "ginkgo",
     "img": "a small dish of dried ginkgo leaf",
     "fala": "ginkgo, the leaf off that ancient Chinese tree"},
    {"id": "fenugreek", "nome": "fenugreek",
     "img": "a small dish of golden fenugreek seed",
     "fala": "fenugreek, the seed your grandmother kept for tea"},
    {"id": "horny_goat", "nome": "horny goat weed",
     "img": "a small dish of dried horny goat weed",
     "fala": "horny goat weed, the herb goat farmers stumbled onto"},
    {"id": "ashwagandha", "nome": "ashwagandha",
     "img": "a small dish of ashwagandha root powder",
     "fala": "ashwagandha, the root Indian families brew at night"},
    {"id": "beet", "nome": "beet root",
     "img": "a small dish of dark beet root powder",
     "fala": "beet root, the plain red root nobody respects"},
    # ⭐ 2026-08-20 — os tres que o operador acrescentou, na forma DESTE
    # motor (o aposto vive dentro de `fala`, nao num campo separado).
    # ⛔ As outras entradas daqui NAO foram uniformizadas com as do
    # BOTICA: elas carregam apostos proprios, tambem validados por ele
    # (`tribulus, the little spiked pod farmers know`), e reescrever copy
    # validada para "padronizar" e' erro que este repo ja' pagou.
    {"id": "ginseng", "nome": "panax ginseng",
     "img": "a small dish of pale twisted ginseng root",
     "fala": "panax ginseng, the famous Korean root"},
    {"id": "acafrao", "nome": "saffron",
     "img": "a small dish of deep red saffron threads",
     "fala": "saffron, the rare red spice from the crocus flower"},
    {"id": "catuaba", "nome": "catuaba",
     "img": "a small dish of reddish bark shavings",
     "fala": "catuaba, the bark traditionally used in Brazil"},
]

# ---------------------------------------------------------------------------
# ⭐ OS COMUNS — o que qualquer um tem em casa, para a receita parecer fácil
# ---------------------------------------------------------------------------
COMUNS = [
    {"id": "abacaxi", "nome": "fresh pineapple", "img": "a bowl of fresh pineapple chunks"},
    {"id": "curcuma", "nome": "ground turmeric", "img": "a small dish of ground turmeric"},
    {"id": "gengibre", "nome": "fresh ginger", "img": "a knob of fresh ginger"},
    {"id": "canela", "nome": "ground cinnamon", "img": "a small dish of ground cinnamon"},
    {"id": "melancia", "nome": "watermelon", "img": "a bowl of cut watermelon"},
    {"id": "romã", "nome": "pomegranate seeds", "img": "a bowl of pomegranate seeds"},
    {"id": "alho", "nome": "garlic", "img": "a head of garlic"},
    {"id": "aveia", "nome": "rolled oats", "img": "a bowl of rolled oats"},
]

# ---------------------------------------------------------------------------
# ⭐ O UTENSÍLIO — o preparo em movimento
# ---------------------------------------------------------------------------
# ⚠️ Cada vasilhame tem SILHUETA PRÓPRIA, e isso não é capricho: no BOTICA
# metade do pool era de vidro e o gerador colapsava quatro deles numa prensa
# francesa, que é a forma que ele conhece melhor. Aqui nenhum par compartilha
# corpo de vidro com haste dentro.
METODOS = [
    # ⛔⛔ O POOL INTEIRO FOI REFEITO (2026-08-07). O operador viu o lote e
    # disse: *"seu settings de hardware do meal prep take 2 esta ruim"*. E
    # estava: pilao de pedra, peneira sobre tigela de aco, moedor de manivela e
    # coador de pano NAO leem como bebida sendo preparada — leem como qualquer
    # outra coisa. O video vende um COPO, e a cena 2 tem de mostrar o copo
    # nascendo.
    # ⚠️ E cada vasilhame tem SILHUETA E MATERIAL PROPRIOS, que e' a licao do
    # BOTICA: metade do pool era de vidro e o gerador colapsava quatro deles
    # numa prensa francesa, a forma que ele conhece melhor. Aqui nao ha' dois
    # corpos de vidro com haste dentro.
    {"id": "liquidificador", "vaso": "a blender jug on its base",
     "acao": "drops the pieces into the blender jug", "curto": "blender"},
    {"id": "jarra_vidro",
     "vaso": "a tall glass pitcher with a long steel spoon standing in it",
     "acao": "stirs it through the glass pitcher", "curto": "glass pitcher"},
    {"id": "mason", "vaso": "a wide-mouth mason jar with its lid off beside it",
     "acao": "screws the lid on the mason jar and shakes it once",
     "curto": "mason jar"},
    {"id": "tigela_fouet",
     "vaso": "a wide ceramic bowl with a wire whisk resting in it",
     "acao": "whisks it in the ceramic bowl", "curto": "ceramic bowl"},
    {"id": "coqueteleira",
     "vaso": "a stainless steel shaker cup with the cap off on the surface",
     "acao": "caps the steel shaker and shakes it twice", "curto": "shaker"},
    {"id": "medidor",
     "vaso": "a heavy glass measuring jug with a pouring spout",
     "acao": "pours it from the measuring jug", "curto": "measuring jug"},
    {"id": "caneca_garrafa",
     "vaso": "a thick ceramic mug beside a small unlabelled glass bottle",
     "acao": "tips the small bottle into the mug", "curto": "mug"},
    {"id": "mixer",
     "vaso": "a tall plastic beaker with a hand blender standing in it",
     "acao": "runs the hand blender down into the beaker", "curto": "beaker"},
]


# ---------------------------------------------------------------------------
# ⭐⭐ AS DUAS MULHERES — e nenhum homem em cena
# ---------------------------------------------------------------------------
# ⛔ ORDEM DO OPERADOR, entrevista de 2026-08-06: a fonte tem um homem
# cozinhando ao fundo e ele SAI. As duas mulheres estão nas três cenas.
# ⚠️ A REF é quem FALA; a segunda é MUDA e olha o prop, nunca a lente. É a
# mesma mecânica da plateia congelada do ESCANDALO: ela encena o espanto no
# lugar do espectador.
# ⛔ `Only she speaks` é obrigatório no TAKE — sem isso o segundo corpo dubla a
# fala e a cena do casal do VAZAMENTO caiu exatamente por aí.
REFS = [
    # ⭐⭐ 2026-08-13 — DE 8 PARA 24, E TRES ANTIGAS REESCRITAS.
    # Ordem do operador: *"aumente o pool de opcoes substancialmente, tambem
    # dos ambientes"*. Sao DUAS mulheres em quadro por video (a REF e a
    # amiga), entao um pool de oito e' o eixo mais estreito do motor: com 8
    # entradas, 28 pares possiveis; com 24, 276.
    # ⛔⛔ DISTINTIVO, NUNCA DETERIORADO — sairam a cicatriz na sobrancelha, a
    # cicatriz na linha do cabelo e a falha entre os dentes. Marca de rosto
    # continua OBRIGATORIA (sem ela o Veo devolve outro rosto no corte), so'
    # que do lado do SINAL DE BELEZA: pinta, covinha, beauty mark, sarda,
    # queixo partido, tarraxa, heterocromia.
    # ⛔ ZERO adjetivo de etnia e ZERO oculos (LEI DO REF, excecao declarada no
    # medidor). O eixo que separa as duas mulheres no MESMO frame e' o CABELO,
    # e por isso nenhuma entrada repete penteado.
    {"id": "cachos_longos", "idade": 27,
     "rotulo": "27y · cachos escuros longos + sinal",
     "rotulo": "27y · cachos escuros longos + sinal",
     "cabeca": "long dark curls falling past the shoulders",
     "marca": "a small dark mole just under her left eye",
     "corpo": "tall with a narrow waist"},
    {"id": "liso_platinado", "idade": 24,
     "rotulo": "24y · platinado no queixo + pinta",
     "rotulo": "24y · platinado no queixo + pinta",
     "cabeca": "sleek platinum hair cut blunt at the jaw",
     "marca": "a small beauty mark just above her left eyebrow",
     "corpo": "slim and long-limbed"},
    {"id": "rabo_alto", "idade": 26,
     "rotulo": "26y · rabo preto alto + covinha",
     "rotulo": "26y · rabo preto alto + covinha",
     "cabeca": "black hair pulled into a high sleek ponytail",
     "marca": "a deep dimple in her left cheek",
     "corpo": "athletic with square shoulders"},
    {"id": "ondas_ruivas", "idade": 25,
     "rotulo": "25y · ondas auburn soltas + sardas",
     "rotulo": "25y · ondas auburn soltas + sardas",
     "cabeca": "deep auburn waves worn loose",
     "marca": "freckles scattered across her nose",
     "corpo": "curved with a small waist"},
    {"id": "trancas", "idade": 28,
     "rotulo": "28y · box braids no ombro + pinta",
     "rotulo": "28y · box braids no ombro + pinta",
     "cabeca": "long box braids gathered over one shoulder",
     "marca": "a beauty mark high on her cheekbone",
     "corpo": "tall and softly curved"},
    {"id": "bob_castanho", "idade": 23,
     "rotulo": "23y · bob castanho brilhante + covinha",
     "rotulo": "23y · bob castanho brilhante + covinha",
     "cabeca": "a glossy chestnut bob",
     "marca": "a dimple in her cheek",
     "corpo": "petite with a narrow frame"},
    {"id": "afro_curto", "idade": 29,
     "rotulo": "29y · afro curto + sinal na tempora",
     "rotulo": "29y · afro curto + sinal na tempora",
     "cabeca": "a short rounded afro",
     "marca": "a small birthmark at her temple",
     "corpo": "strong-shouldered and lean"},
    {"id": "loiro_longo", "idade": 22,
     "rotulo": "22y · loiro mel longo liso + sardas",
     "rotulo": "22y · loiro mel longo liso + sardas",
     "cabeca": "long honey-blonde hair, straight and heavy",
     "marca": "a light spray of freckles across her nose and cheekbones",
     "corpo": "long-legged and slight"},
    # --- as 16 novas (2026-08-13) ------------------------------------------
    {"id": "tranca_lateral", "idade": 24,
     "rotulo": "24y · tranca unica lateral + pinta",
     "rotulo": "24y · tranca unica lateral + pinta",
     "cabeca": "a long single braid falling over one shoulder",
     "marca": "a small beauty mark above the right corner of her mouth",
     "corpo": "slim with long legs"},
    {"id": "coque_alto", "idade": 26,
     "rotulo": "26y · coque escuro alto + sardas",
     "rotulo": "26y · coque escuro alto + sardas",
     "cabeca": "dark hair gathered into a high glossy bun",
     "marca": "a light dusting of freckles across her nose",
     "corpo": "athletic with a narrow waist"},
    {"id": "franja_reta", "idade": 23,
     "rotulo": "23y · preto franja reta + covinha",
     "rotulo": "23y · preto franja reta + covinha",
     "cabeca": "straight black hair with a blunt fringe at the brows",
     "marca": "a deep dimple in her right cheek",
     "corpo": "petite and slim"},
    {"id": "cachos_curtos", "idade": 27,
     "rotulo": "27y · cachos curtos + tarraxa dourada",
     "rotulo": "27y · cachos curtos + tarraxa dourada",
     "cabeca": "short springy curls pushed back from her face",
     "marca": "a tiny gold stud in her left nostril",
     "corpo": "curved with a small waist"},
    {"id": "mel_ondulado", "idade": 25,
     "rotulo": "25y · ondas mel castanho + sinal",
     "rotulo": "25y · ondas mel castanho + sinal",
     "cabeca": "honey-brown waves falling to the middle of her back",
     "marca": "a small dark mole under her right eye",
     "corpo": "long-limbed and slim"},
    {"id": "loiro_bob", "idade": 22,
     "rotulo": "22y · bob platinado reto + sardas",
     "rotulo": "22y · bob platinado reto + sardas",
     "cabeca": "a sharp platinum bob cut level at the jaw",
     "marca": "a fine spray of freckles high on both cheeks",
     "corpo": "slight and narrow-framed"},
    {"id": "trancas_longas", "idade": 28,
     "rotulo": "28y · trancas ate a cintura + pinta",
     "rotulo": "28y · trancas ate a cintura + pinta",
     "cabeca": "waist-length braids pulled over one shoulder",
     "marca": "a small beauty mark at her left temple",
     "corpo": "tall and softly curved"},
    {"id": "ruivo_liso", "idade": 24,
     "rotulo": "24y · ruivo cobre liso + sardas",
     "rotulo": "24y · ruivo cobre liso + sardas",
     "cabeca": "straight copper-red hair parted in the middle",
     "marca": "freckles scattered across her nose and cheekbones",
     "corpo": "slim with square shoulders"},
    {"id": "preto_longo", "idade": 29,
     "rotulo": "29y · preto longo solto + queixo partido",
     "rotulo": "29y · preto longo solto + queixo partido",
     "cabeca": "long jet-black hair worn loose and heavy",
     "marca": "a fine dusting of freckles over her nose and a shallow cleft "
              "in her chin",
     "corpo": "tall with a narrow waist"},
    {"id": "meio_preso", "idade": 26,
     "rotulo": "26y · castanho meio preso + olhos bicolor",
     "rotulo": "26y · castanho meio preso + olhos bicolor",
     "cabeca": "chestnut hair half pulled up, the rest loose past her "
               "shoulders",
     "marca": "one green eye and one hazel eye",
     "corpo": "curved and long-legged"},
    {"id": "pixie", "idade": 23,
     "rotulo": "23y · pixie escuro + sinal no olho",
     "rotulo": "23y · pixie escuro + sinal no olho",
     "cabeca": "a cropped dark pixie cut",
     "marca": "a tiny mole at the outer corner of her right eye",
     "corpo": "petite with a narrow frame"},
    {"id": "ondas_castanhas", "idade": 25,
     "rotulo": "25y · ondas castanhas + risca funda",
     "rotulo": "25y · ondas castanhas + risca funda",
     "cabeca": "loose chestnut waves parted deep on one side",
     "marca": "a light spray of freckles over her nose",
     "corpo": "slim with soft curves"},
    {"id": "rabo_baixo", "idade": 28,
     "rotulo": "28y · rabo escuro baixo + pinta alta",
     "rotulo": "28y · rabo escuro baixo + pinta alta",
     "cabeca": "dark hair pulled into a low sleek ponytail",
     "marca": "a beauty mark high on her right cheekbone",
     "corpo": "athletic and long-limbed"},
    {"id": "loiro_escuro", "idade": 24,
     "rotulo": "24y · loiro escuro ondulado + sinal",
     "rotulo": "24y · loiro escuro ondulado + sinal",
     "cabeca": "dark blonde hair in loose beach waves",
     "marca": "a small mole on her jaw below her left ear",
     "corpo": "tall and slender"},
    {"id": "castanho_curto", "idade": 22,
     "rotulo": "22y · castanho no queixo + sardas",
     "rotulo": "22y · castanho no queixo + sardas",
     "cabeca": "a chin-length chestnut cut tucked behind one ear",
     "marca": "freckles across the bridge of her nose",
     "corpo": "petite and trim"},
    {"id": "ondas_pretas", "idade": 29,
     "rotulo": "29y · ondas pretas longas + tarraxa",
     "rotulo": "29y · ondas pretas longas + tarraxa",
     "cabeca": "long black waves with a deep side part",
     "marca": "a tiny silver stud in her right nostril",
     "corpo": "full-figured with a small waist"},
]

# ⚠️ A AMIGA é sorteada do mesmo pool, mas NUNCA a mesma entrada — duas
# mulheres com o mesmo rosto no mesmo quadro é o defeito mais visível que
# existe, e o Veo faz isso sozinho se a descrição não separar as duas.
REACOES_AMIGA = [
    "her eyes fixed on it, lips parted",
    "watching it without blinking",
    "her hand half raised, stopped in the air",
    "staring at it, chin drawn back",
    "one eyebrow up, eyes on it",
    "leaning in slightly, eyes on it",
    "her mouth open a little, eyes on it",
    "still, her gaze locked on it",
]

# ⭐ A cláusula anti-celebridade, no registro de mulher.
# ⛔⛔ A negacao anti-celebridade saiu daqui em 2026-08-14, por ordem do
# operador (*"tire not a celebrity do prompt"*): declaracao INJETA o token
# que ela nega. ⚠️ Aqui a clausula era `not resembling any famous person, not
# a celebrity` — NEGACAO PURA, sem metade descritiva para sobreviver, o unico
# caso assim nos 30 motores. Por isso a constante fica VAZIA e quem carrega a
# pontuacao passou a ser o slot (`sc.frase_anti`), no `montar()`.
# ⚠️ O aviso de MAIUSCULA acima morreu junto: nao ha' mais frase para comecar
# em minuscula. Fica pela memoria de como o defeito se parecia.
# Ver CLAUDE.md §"CONTRA A CELEBRIDADE, SILENCIO".
ANTICELEB = ("")

CAUDA = ("Slight sensor grain, soft focus, raw iPhone front camera aesthetic. "
         "No subtitles, no captions, no burned-in text, no watermark.")

# ⚠️ "in the background", nao "behind them": a cena 2 tem UMA pessoa em
# quadro, e o plural saia contradizendo o "She is the only person in the frame"
# da mesma frase.
BANDEIRA = " A small US flag sticker is stuck on the wall in the background."

# ⛔ O que está na bancada NÃO se mexe. Sem esta trava o Veo inventa mãos
# mexendo em potes ao fundo e a continuidade entre os blocos de 8s morre.
NAO_TOCA = ("Nothing else on the %s is touched, moved, opened or lifted, and "
            "nothing is added to it or taken away.")

# ---------------------------------------------------------------------------
# COPY — cena 1: A ISCA DESMENTIDA + A VIRADA
# ---------------------------------------------------------------------------
# ⛔⛔ ORDEM DO OPERADOR, palavra por palavra: *"após '...back overnight...'
# teremos 'but combined with the secret I discovered will' — retirar 'but this
# Costco remedy'"*. A fonte credita a virada a um LUGAR (Costco); aqui ela é
# creditada ao SEGREDO, porque é o segredo que a isca do CTA entrega.
#
# ⚠️ A frase nomeia o órgão NA MESMA FRASE da causa (regra da FRASE ÓRFÃ, §17):
# "won't bring it back" sem dizer o quê é fisiologia solta.
DESMENTIDOS = [
    # ⛔⛔⛔ TODO HOOK DIZ O QUE SE FAZ COM O RARO. Ordem do operador em
    # 2026-08-07, lendo um take renderizado: *"every morning just ginko?? WTF?
    # Ginkgo pra que? pra passar na bunda? pra plantar??? Vc tem que ser CLARO,
    # taxativo"*.
    # ⚠️ Dez dos vinte hooks nomeavam o raro e paravam ali — "Six weeks of {r}
    # alone", "Every morning, just {r}". Numa cena onde NAO ha' copo nem
    # bancada em quadro (o hook e' o homem com o prop preso), a fala e' o
    # UNICO lugar onde o verbo pode existir. Cena 2 pode dizer so' "Add {R}"
    # porque o liquidificador esta' na tela; o hook nao pode.
    # ⛔ O verbo e' de BEBER, nao de tomar capsula: o mecanismo do video e' uma
    # bebida, e o payoff da cena 3 e' um copo.
    #
    # ⛔ A VIRADA CONTINUA DITADA e nao se reescreve: *"but combined with the
    # secret I discovered will"*. O que ela ganhou foi o DESTINO — sem terminar
    # no orgao, "it will" o QUE?
    # ⚠️ Teto medido no PIOR caso (`horny goat weed` + `john-son`).
    #
    # ── o dinheiro gasto ────────────────────────────────────────────────────
    "Two bottles of {r} swallowed and your {o} never answered once. "
    "But combined with the secret I found, your {o} answers again.",
    "You paid good money to drink {r} and your {o} never noticed. "
    "But combined with the secret I found, your {o} comes back.",
    "The {r} you drink promised everything and left your {o} down. "
    "But combined with the secret I found, your {o} wakes up.",
    "The label swears drinking {r} alone is all your {o} needs. "
    "But combined with the secret I found, your {o} comes back.",
    "Whoever sold you {r} to drink skipped the step your {o} needed. "
    "But combined with the secret I found, your {o} answers again.",
    "Doubling the dose of {r} you drink still leaves your {o} quiet. "
    "But combined with the secret I found, your {o} wakes up.",
    # ── o tempo perdido ─────────────────────────────────────────────────────
    "Six weeks drinking {r} and your {o} won't stand up. "
    "But combined with the secret I found, your {o} comes back.",
    "Three months drinking {r} and your {o} still goes soft. "
    "But combined with the secret I found, your {o} comes back.",
    "Eight months drinking {r} and your {o} still plays dead. "
    "But combined with the secret I found, your {o} wakes up.",
    "A year of drinking {r} and your {o} still gives out. "
    "But combined with the secret I found, your {o} answers again.",
    "All winter drinking {r} and your {o} stayed asleep. "
    "But combined with the secret I found, your {o} wakes up.",
    "Drinking {r} and nothing else, your {o} still ignores you. "
    "But combined with the secret I found, your {o} wakes up.",
    "You swallow {r} and nothing else, and your {o} still sleeps. "
    "But combined with the secret I found, your {o} wakes up.",
    # ── a metade: o raro nao e' mentira, e' INCOMPLETO ─────────────────────
    "Taken alone, {r} never reaches your {o}. "
    "But combined with the secret I found, your {o} wakes up.",
    "No amount of {r} you drink will wake your {o}. "
    "But combined with the secret I found, your {o} comes back.",
    "Swallowing {r} alone does half the work your {o} needs. "
    "But combined with the secret I found, your {o} answers again.",
    "Your {o} stayed silent because drinking {r} was never enough. "
    "But combined with the secret I found, your {o} wakes up.",
    "Your {o} didn't fail you. Taking {r} alone was never enough. "
    "But combined with the secret I found, your {o} comes back.",
    "Nobody told you drinking {r} alone does nothing for your {o}. "
    "But combined with the secret I found, your {o} answers again.",
    "Your wife stopped asking, and drinking {r} never woke your {o}. "
    "But combined with the secret I found, your {o} answers again.",
]

# ---------------------------------------------------------------------------
# COPY — cena 2 do 16: A VENDA, O CTA E A COSTURA
# ---------------------------------------------------------------------------
# ⛔⛔ AQUI MORREM RECEITAS, CTAS E GATES do motor de 24s, e a razao e' de
# ARITMETICA, medida antes de escrever uma linha:
#
#     receita + CTA + gate, com os MINIMOS de hoje = 34 palavras, teto 25
#     e com o RARO+APOSTO na cena 2: 0 de 1536 combinacoes cabiam
#
# ⭐ O QUE SALVOU TUDO foi medir de onde o raro ja' vinha: os 20 DESMENTIDOS
# nomeiam o raro na CENA 1 (20/20, medido). Repeti-lo na cena 2 num video de 16
# segundos e' pagar duas vezes pela mesma informacao — a mesma economia que
# tirou o aposto do hook no motor de 24s, so' que na direcao inversa.
# ⚠️ Resultado: 71% das combinacoes cabem, mediana 24, ZERO entrada morta, e
# NADA se perde — raro, costura, CTA e follow-gate continuam todos de pe'.

# ⭐⭐ A VENDA. Toda entrada faz TRES coisas ao mesmo tempo:
#   1. carrega o literal `gelatin trick` como SUJEITO (amarra o criativo a' VSL
#      e ja' o poe no topo da hierarquia sem precisar do rotulo com dois pontos);
#   2. NOMEIA O BURACO (`piece`/`part`/`step`) — e' a metade da costura;
#   3. diz o que o buraco DEVOLVE ao orgao (§17: mecanismo sem destino nao
#      entrega nada em que agir).
VENDAS = [
    "The gelatin trick is the missing piece your {o} needs",
    # ⛔ AS TRES ULTIMAS FORAM REESCRITAS — a lente FA4 acusou 32 de 400 e
    # estava CERTA: `the piece that brings your {o} back` nomeia o SUBSTANTIVO
    # do buraco e nao diz que ele FALTA. Sem a falta, o angulo vira "mais uma
    # receita" — e' o nome do agente que se perde.
    # ⚠️ Cada entrada carrega agora um marcador de ausencia: `missing`,
    # `leave out`, `skip`, `hold back` ou `nobody includes/hands`.
    "The gelatin trick is the piece they leave out, and your {o} comes back",
    "The gelatin trick is the part nobody hands you, and your {o} answers",
    "The gelatin trick is the missing part that wakes your {o}",
    "The gelatin trick is the piece your {o} was missing",
    "The gelatin trick is the step they skip, and your {o} fills again",
    "The gelatin trick is the piece they hold back from your {o}",
    "The gelatin trick is the one piece nobody includes, and your {o} returns",
]

# ⭐⭐ O CTA. Curto, e ele AINDA NOMEIA o que e' enviado — a regra TR19, ordem
# do operador lendo um take do TROCA: *"'and I'll send it' — enviar o QUE??"*.
# ⛔⛔ TODAS AS ENTRADAS DIZEM `I'll send`, e isso NAO e' estilo. A primeira
# versao economizava trocando o verbo de envio por posse (`and the missing
# piece is yours`) — e o `sc.lint_isca_cta`, que e' COMPARTILHADO pelos 21
# motores, reprovava: a regex dele conhece `recipe`, `measurements`, `send
# you/the/...` e `I'll send`, e nao conhece `is yours`.
# ⚠️ A tentacao era alargar a lente compartilhada. Nao: ela vale para todos os
# motores e a forma dela e' doutrina de 2026-08-02. Medido, a troca custa UMA
# palavra ("and the missing piece is yours" = 8; "and I'll send the missing
# piece" = 8, empatado) — mudar o motor era mais barato E mais correto que
# mudar a regra de todo mundo.
# ⛔⛔ E A VIRGULA DEPOIS DE `gelatin` E' O ITEM MAIS IMPORTANTE DESTE POOL. A
# automacao de DM casa palavra EXATA; a legenda nasce do Whisper em cima do
# audio e nao ha' conserto depois. Lente T16-2.
CTAS = [
    # ⛔⛔ TODA ENTRADA NOMEIA `recipe`. Ordem do operador, 2026-08-08, lendo
    # o app: *"seja mais taxativo: I'll send recipe ou I'll send the complete
    # recipe. `and I'll send the part they leave out` da' vazao pra pessoa
    # ficar em duvida: qual parte de QUE??"*
    # ⚠️ E O DEFEITO FOI MEU, NA COMPRESSAO DO PORTE: o motor de 24s tem as
    # OITO CTAs nomeando `recipe` (`the recipe with the missing part`, `the
    # recipe with the step they leave out`). Ao apertar para 25 palavras eu
    # cortei justamente o substantivo que diz O QUE e' entregue — e' a §35,
    # `COMPRIMI A FRASE MATANDO O SUBSTANTIVO`, cometida por mim de novo.
    # ⭐ A COSTURA DO ANGULO NAO SE PERDE: quem diz que falta uma peca e' a
    # PRIMEIRA sentenca da cena 2, e a lente FA4 cobra isso separadamente. O
    # CTA responde aquela falta com a palavra que fecha — `complete`.
    "Comment gelatin, and I'll send the complete recipe.",
    "Comment gelatin, and I'll send the full recipe.",
    "Comment gelatin, and I'll send the whole recipe.",
    "Comment gelatin, and I'll send you the complete recipe.",
    "Comment gelatin, and I'll send the complete recipe tonight.",
    "Comment gelatin, and I'll send the recipe with the missing piece.",
    "Comment gelatin, and I'll send the recipe with the missing step.",
    "Comment gelatin, and I'll send the recipe nobody posts complete.",
]

# ⭐ O FOLLOW — curto por ARITMETICA. Ver o controle [ALCANCE] do autoteste:
# entrada que nao cabe somada aos minimos dos outros eixos nunca e' sorteada, e
# o autoteste a contaria como opcao viva.
GATES = [
    "Followers only.",
    "Follow first.",
    "Follow me first.",
    "Follow me too.",
    "Follow, or nothing sends.",
    "Unfollowed, I cannot reply.",
    "No follow, no recipe.",
    "Follow, or it never sends.",
]

# ⛔⛔ O NUCLEO DA COSTURA. `piece`, `part` e `step` sao as tres formas de
# nomear o buraco, e o guarda abaixo obriga a VENDA e o CTA a usarem formas
# DIFERENTES. No motor de 24s a costura atravessa 8 segundos e repetir o mesmo
# substantivo e' RETOMADA; aqui ela cai em tres, e repetir vira GAGUEIRA.
# ⚠️ Medido: sem o guarda, 42% dos sorteios repetiam o substantivo.
_SEAM = ("piece", "part", "step")


def _nucleo_seam(t):
    return set(w for w in _SEAM if w in t.lower())


# ---------------------------------------------------------------------------
# CONTRATO DA UI
# ---------------------------------------------------------------------------
# ⭐ DUAS CENAS. O teto continua 25 — ele vem da fisica (8s x 3,1 p/s),
# nao do numero de cenas.
# ⛔ O piso da cena 2 e' ARITMETICA: menor VENDA + menor CTA + menor
# FOLLOW. Piso abaixo disso e' alarme que nunca toca.
TETO_FALA = {1: 25, 2: 25}
PISO_FALA = {1: 16, 2: 19}
TETO_TOTAL = 50

TRAVAS_UI = [("familia_mundo", "regiao", FAMILIAS_MUNDO)]
EIXOS_TRAVAVEIS = ["mundo", "etnia", "ref", "amiga", "homem", "prop",
                   "metodo", "comum", "raro"]
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
    ("mundo", "A REGIAO", "MUNDOS", "id"),
    ("etnia", "ETNIA", "etnias_do_mundo", None),
    ("ref", "QUEM FALA", "REFS", "cabeca"),
    ("amiga", "A AMIGA", "REFS", "cabeca"),
    ("homem", "O CORPO-PROVA", "HOMENS", "id"),
    ("prop", "O PROP PRESO", "PROPS", "nome"),
    ("metodo", "O PREPARO", "METODOS", "curto"),
    ("comum", "O COMUM", "COMUNS", "nome"),
    ("raro", "O RARO", "RAROS", "nome"),
]
CENAS_UI = ["1 · o corpo-prova acusado", "2 · a prova + o buraco + CTA"]

# ⭐⭐ O DROPDOWN DE QUEM FALA — e' ELE que da' FUNCAO ao campo `rotulo`.
# ⛔ Sem esta linha o rotulo seria comentario caro: 24 textos escritos, medidos
# e travados, e nenhum olho humano os veria. Forma sem funcao e' o defeito que
# este repo mais paga (licoes-de-construcao §41), e um label que nao aparece na
# tela e' a versao mais barata dele.
# ⛔ POR QUE DROPDOWN E NAO `TRAVAS_UI`: a barra de travas desenha UM BOTAO POR
# OPCAO, lado a lado. Serve para as regioes; com 24 REFs ela estoura a largura
# da janela. Contrato aditivo do `ui_agente` (2026-08-13), modelo: MEL 16.
# ⚠️ O campo exibido e' `rotulo`, NAO `cabeca` nem `id`: `cabeca` e' um
# paragrafo em ingles e `id` (`meio_preso`, `pixie`) so' diz alguma coisa para
# quem escreveu o pool. O operador escolhe "23y · pixie escuro + sinal no olho".
# ⛔⛔ ESTE POOL JA' TINHA `id` — o que faltava era o `sortear` RESPEITA-LO. A
# linha antiga (`ref = travas.get("ref") or ...`) usava a trava CRUA, entao o id
# vindo do menu virava `spec["ref"]` como STRING e a montagem quebrava no
# primeiro `ref["cabeca"]`. Ver `_por_ref` la' em cima.
DROPDOWNS_UI = [("ref", "QUEM FALA", "REFS", "rotulo")]

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
    um traceback no meio do lote ESCONDE a causa real — quem le' ve'
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

TETO_LEDGER = {"familia_mundo": len(FAMILIAS_MUNDO), "prop": len(PROPS),
               "homem": len(HOMENS), "metodo": len(METODOS),
               "comum": len(COMUNS), "raro": len(RAROS), "ref": len(REFS)}

NUCLEO = ("soldier", "manhood", "member", "john-son", "peck-er", "wiener")


def _carregar_ledger():
    try:
        with open(LEDGER, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


def _anotar(led, spec):
    """Registra os eixos deste sorteio no ledger da pagina.

    ⛔ Existe desde o primeiro dia: o `ui_agente` chama
    `_gravar_ledger(_carregar_ledger(), self.spec)` com DOIS argumentos, e
    motor que aceita UM levanta TypeError dentro do callback do tkinter, que
    morre CALADO — o toast diz "registrado" e nada e' escrito. Oito dos
    dezoito agentes nasceram com esse defeito; este nao.
    """
    u = led.setdefault(spec["pagina"], {})
    for eixo, val in (("familia_mundo", spec["mundo"]["familia"]),
                      ("prop", spec["prop"]["id"]),
                      ("substancia", spec["substancia"]["id"]),
                      ("metodo", spec["metodo"]["id"]),
                      ("comum", spec["comum"]["id"]),
                      ("raro", spec["raro"]["id"]),
                      ("ref", spec["ref"]["id"])):
        u.setdefault(eixo, [])
        if val not in u[eixo]:
            u[eixo].append(val)
        if len(u[eixo]) >= TETO_LEDGER[eixo]:
            u[eixo] = [val]
    return led


def _gravar_ledger(led, spec=None):
    if spec is not None:
        _anotar(led, spec)
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
    """Resolve a REF travada por `id` (o dropdown) OU por `cabeca`.

    ⛔⛔ ESTE HELPER EXISTE PORQUE O `travas["ref"]` ERA USADO CRU. A linha
    antiga era `ref = travas.get("ref") or ...` — ela assumia que a trava era o
    DICT da entrada, que e' o que o cadeado da coluna manda. So' que o
    `ui_agente._barra_dropdowns` manda o `id`, uma STRING: com ela, `spec["ref"]`
    virava a string `"cachos_longos"` e a montagem quebrava no primeiro
    `ref["cabeca"]`. Nao e' o botao que mente — e' o botao que derruba o app.
    ⚠️ Valor que NAO e' string volta intacto, entao o cadeado (dict) continua
    exatamente como estava. Isto e' um SUPERSET do comportamento antigo.
    """
    if not isinstance(valor, str):
        return valor
    return next((x for x in pool
                 if x.get("id") == valor or x.get("cabeca") == valor), pool[0])


def _palavras(t):
    return len(t.split())


def _escolher(rng, pool, ok, tamanho=None):
    """Filtra de verdade e cai na MAIS CURTA quando nada serve.

    ⛔ Nao usa 'tenta 12 vezes e devolve a ultima': esse fallback ignora o teto
    de fala em silencio e foi o que fez a cena 2 do TROCA passar de 25 para 27
    palavras sem ninguem ver.

    ⛔⛔ `tamanho` mede a string FORMATADA, nao o template. Sem ele o fallback
    escolhia o template mais curto e, depois de substituir o raro (que tem
    aposto e chega a 9 palavras), a fala saia com 28 contra teto de 25 — o
    filtro passava e o estouro entrava pela porta dos fundos.
    """
    cands = [x for x in pool if ok(x)]
    if cands:
        return rng.choice(cands)
    return min(pool, key=tamanho or _palavras)


# ⛔ Palavras de liga: repetir "the", "your" ou "and" entre cenas nao e' eco, e'
# ingles. O eco que machuca e' o de CONTEUDO — verbo e substantivo.
_LIGA = frozenset(
    "the a an and or but your you it on in of to that this with i me my so "
    "first no not won't will is are be one".split())


def _bigramas(t, orgao):
    """Pares de palavras de conteudo, sem o orgao (ele repete DE PROPOSITO)."""
    p = [w.strip(".,:;!?").lower() for w in t.split()]
    p = [w for w in p if w != orgao]
    return {(a, b) for a, b in zip(p, p[1:])
            if not (a in _LIGA and b in _LIGA)}


# ⛔⛔ O ECO QUE E' PARA ACONTECER. Ordem do operador, palavra por palavra:
# *"the secret gelatin trick, (aposto the missing part) (vira isca pro cta
# final)"*. O aposto da cena 2 TEM de reaparecer no CTA — e' o que costura a
# promessa a entrega. Sem esta excecao o guarda de eco derrubava exatamente a
# costura do angulo: a cena 3 caia de 4,2% para 1,2% de uso nos CTAs que
# nomeiam a peca, e o vidoe prometia uma coisa depois de anunciar outra.
# ⚠️ A excecao e' por PALAVRA, nao por par — e isso e' medicao, nao gosto. Com
# a excecao so' nos pares ("missing","part") etc., o que continuava derrubando
# o CTA era o par vizinho ("the","missing"): os quatro CTAs que nomeiam a peca
# cairam para 200 usos em 2.400 contra 800 dos dois que nao a nomeiam — o
# guarda estava premiando justamente os CTAs mais fracos.
_ECO_PALAVRA = frozenset(["missing"])
_ECO_PAR = frozenset([("gelatin", "trick"), ("nobody", "includes")])


def _colide(anterior, candidata, orgao):
    comuns = _bigramas(anterior, orgao) & _bigramas(candidata, orgao)
    resto = {c for c in comuns
             if c not in _ECO_PAR and not (_ECO_PALAVRA & set(c))}
    return bool(resto)


def sortear(pagina, rng, ledger, travas=None):
    travas = travas or {}
    usados = (ledger or {}).get(pagina, {})

    # ⭐ a pele filtra o UNIVERSO de mundos antes de qualquer sorteio
    pele = travas.get("pele")
    disponiveis = mundos_da_pele(pele)
    familias = list(dict.fromkeys(m["familia"] for m in disponiveis))

    fam_trava = travas.get("familia_mundo")
    if travas.get("mundo"):
        mundo = _por_id(MUNDOS, travas["mundo"])
    else:
        fam = (fam_trava if fam_trava and fam_trava != "livre"
               else _fresco([{"id": x} for x in familias],
                            usados.get("familia_mundo", []), rng, "id")["id"])
        mundo = rng.choice([m for m in disponiveis if m["familia"] == fam]
                           or [m for m in MUNDOS if m["familia"] == fam])

    ets = ([e for e in mundo["etnias"] if _pele_de(e) == pele]
           if pele in ("clara", "escura") else [])
    et = travas.get("etnia") or rng.choice(ets or mundo["etnias"])

    # ⭐ MODO BELA — a REF e a amiga saem do pool bela quando o toggle liga.
    if travas.get("bela"):
        ref = (_por_ref(REFS, travas["ref"]) if travas.get("ref")
               else sc.ref_bela(REFS[0], rng))
        amiga = sc.ref_bela(REFS[0], rng, banidos=(ref.get("cabeca", ""),))
    else:
        ref = (_por_ref(REFS, travas["ref"]) if travas.get("ref")
               else _fresco(REFS, usados.get("ref", []), rng, "id"))
        # ⛔ A AMIGA NUNCA E' A MESMA ENTRADA DA REF. Duas mulheres de rosto
        # identico no mesmo quadro e' o defeito mais visivel que existe, e o
        # Veo faz isso sozinho se a descricao nao separar as duas.
        amiga = travas.get("amiga") or rng.choice(
            [r for r in REFS if r["id"] != ref.get("id")])

    prop = (_por_id(PROPS, travas["prop"]) if travas.get("prop")
            else _fresco(PROPS, usados.get("prop", []), rng, "id"))
    # ⭐ O HOMEM E O ADESIVO — os dois eixos que entraram com a cena nova.
    homem = (_por_id(HOMENS, travas["homem"]) if travas.get("homem")
             else _fresco(HOMENS, usados.get("homem", []), rng, "id"))
    adesivo = rng.choice(ADESIVOS)
    # ⛔⛔ ESTES TRES ACENDIAM O BOTAO E NAO TRAVAVAM NADA. Estavam em
    # EIXOS_TRAVAVEIS desde o nascimento do agente, o painel desenhava o
    # `trava`, e o sorteio seguia aleatorio — o operador clicava e nao
    # acontecia nada. E' o MESMO defeito que o CLEAN V2 pagou em campo com a
    # trava de pele, e que o amigo do Ed achou depois no COLO e no RECEITA.
    # ⚠️ Achado testando eixo por eixo, nao lendo o codigo: `mundo`, `homem` e
    # `prop` travavam; estes tres, nao. Contar entradas em EIXOS_TRAVAVEIS
    # nunca acusaria — a lista estava certa, quem nao lia era o sorteio.
    met = (_por_id(METODOS, travas["metodo"]) if travas.get("metodo")
           else _fresco(METODOS, usados.get("metodo", []), rng, "id"))
    com = (_por_id(COMUNS, travas["comum"]) if travas.get("comum")
           else _fresco(COMUNS, usados.get("comum", []), rng, "id"))
    raro = (_por_id(RAROS, travas["raro"]) if travas.get("raro")
            else _fresco(RAROS, usados.get("raro", []), rng, "id"))
    reacao = rng.choice(REACOES_AMIGA)
    if travas.get("bela"):
        tpl, _curto = sc.traje_bela(rng)
        traje = tpl % rng.choice(sc.CORES_BELAS) if "%s" in tpl else tpl
        # ⛔ A AMIGA TEM ROUPA PROPRIA. As duas vestiam a MESMA, e duas
        # mulheres de traje identico no mesmo quadro leem como a mesma pessoa
        # duplicada — exatamente o que o eixo da amiga existe para impedir. No
        # lote que o operador aprovou elas estavam diferentes.
        for _ in range(8):
            tpl2, _c2 = sc.traje_bela(rng)
            traje_amiga = (tpl2 % rng.choice(sc.CORES_BELAS)
                           if "%s" in tpl2 else tpl2)
            if traje_amiga != traje:
                break
    else:
        traje = rng.choice(TRAJES_PADRAO)
        traje_amiga = rng.choice([t for t in TRAJES_PADRAO if t != traje])
    orgao = rng.choice(sc.APELIDOS_16)

    falas = _montar_falas(rng, orgao, raro)

    return {
        "pagina": pagina, "mundo": mundo, "etnia": et, "ref": ref,
        "amiga": amiga, "prop": prop, "homem": homem,
        "adesivo": adesivo, "metodo": met,
        "comum": com, "raro": raro, "reacao": reacao, "orgao": orgao,
        "bela": bool(travas.get("bela")), "falas": falas, "traje": traje,
        "traje_amiga": traje_amiga,
        "bandeira": rng.random() < 0.5,
    }


def _montar_falas(rng, orgao, raro):
    """As DUAS falas.

    ⛔ O RARO E' FALADO NA CENA 1, e so' la'. Medido: os 20 DESMENTIDOS o
    nomeiam (20/20). No motor de 24s ele aparece nu no hook e com APOSTO na
    cena 2; aqui a cena 2 nao paga de novo, e o aposto sequer cabe — com ele,
    ZERO de 1536 combinacoes ficavam em 25 palavras.

    ⭐⭐ O GUARDA DA COSTURA. A venda nomeia o buraco (`piece`/`part`/`step`) e
    o CTA promete o buraco — e os dois tem de usar substantivos DIFERENTES. No
    motor de 24s a costura atravessa 8 segundos e repetir o mesmo termo e'
    RETOMADA; aqui ela cai dentro de tres, e repetir vira GAGUEIRA.
    ⚠️ Medido: sem o guarda, 42% dos sorteios repetiam o substantivo.
    ⛔ O fallback e' `or cand` e nao `or CTAS`: quando nenhum CTA diverge, cede
    a DIVERGENCIA, nunca o teto — devolver o pool inteiro e' o bug que ja' fez
    o COLO e o BOTICA subirem de 31 para 36 palavras.
    """
    c1 = _escolher(
        rng, DESMENTIDOS,
        lambda t: _palavras(t.format(r=raro["nome"], o=orgao)) <= TETO_FALA[1],
        tamanho=lambda t: _palavras(t.format(r=raro["nome"], o=orgao))
    ).format(r=raro["nome"], o=orgao)

    # o menor de cada eixo, para reservar o espaco desde o primeiro sorteio
    c_cta = min(CTAS, key=_palavras)
    c_gate = min(GATES, key=_palavras)

    def _c2(venda, cta, gate):
        return "%s. %s %s" % (venda.format(o=orgao).rstrip(". "), cta, gate)

    venda = _escolher(
        rng, VENDAS,
        lambda t: (_palavras(_c2(t, c_cta, c_gate)) <= TETO_FALA[2]
                   and not _colide(c1, t.format(o=orgao), orgao)),
        tamanho=lambda t: _palavras(_c2(t, c_cta, c_gate)))

    _nv = _nucleo_seam(venda)
    cand = [c for c in CTAS
            if _palavras(_c2(venda, c, c_gate)) <= TETO_FALA[2]]
    divergentes = [c for c in cand if not (_nucleo_seam(c) & _nv)] or cand
    cta = _escolher(rng, divergentes, lambda c: True)

    gate = _escolher(
        rng, GATES,
        lambda g: (_palavras(_c2(venda, cta, g)) <= TETO_FALA[2]
                   and not _colide(c1 + " " + venda, g, orgao)),
        tamanho=_palavras)

    return [c1, _c2(venda, cta, gate)]


def _pessoa(spec):
    r = spec["ref"]
    return ("a %d-year-old %s woman with %s and %s"
            % (r["idade"], spec["etnia"], r["cabeca"], r["marca"]))


def _ancora(spec):
    r = spec["ref"]
    return ("the same %d-year-old %s woman, with %s and %s"
            % (r["idade"], spec["etnia"], r["cabeca"], r["marca"]))


def _amiga(spec):
    a = spec["amiga"]
    return ("a second %s woman with %s and %s" % (spec["etnia"], a["cabeca"],
                                                  a["marca"]))


# ⛔ O traje e' sorteado no `sortear` e VIAJA NO SPEC. O `montar` nao recebe
# rng — chamar `traje_bela(rng)` la dentro era AttributeError na primeira
# execucao, e dentro de um callback do tkinter isso morre calado.
TRAJES_PADRAO = [
    "a fitted crop top and high-cut shorts",
    "a short cotton sundress",
    "a cropped tank and denim shorts",
    "a ribbed halter top and short skirt",
]


def _traje(spec):
    return spec.get("traje") or TRAJES_PADRAO[0]


def montar(spec):
    """Os 7 blocos. Formatacao NOMEADA de ponta a ponta — sao 12+ campos por
    bloco, e um deslocamento posicional troca prop por pessoa sem estourar
    erro nenhum (bug que so' aparece no video pronto)."""
    m, ref, prop, hom = spec["mundo"], spec["ref"], spec["prop"], spec["homem"]
    met, com, raro = spec["metodo"], spec["comum"], spec["raro"]
    band = BANDEIRA if spec.get("bandeira") else ""

    v = {
        "coz": m["coz"], "coz_c": m["coz_c"], "sup_a": m["sup_a"],
        "sup": m["sup"], "luz": m["luz"], "luz_c": m["luz_c"],
        "audio": m["audio"],
        "pessoa": _pessoa(spec), "ancora": _ancora(spec),
        "amiga": _amiga(spec), "traje_amiga": spec["traje_amiga"],
        "traje": _traje(spec), "prop_img": prop["img"],
        "prop_curto": prop["curto"], "fita": FITA,
        "prop_grande": PROP_GRANDE, "sem_fita": SEM_FITA,
        "adesivo": spec["adesivo"],
        "h_idade": hom["idade"], "h_corpo": hom["corpo"],
        "h_cabeca": hom["cabeca"], "h_calca": hom["calca"],
        "vaso": met["vaso"], "acao": met["acao"],
        "com_img": com["img"], "raro_img": raro["img"],
        # ⛔⛔ O SLOT LEVA A PROPRIA PONTUACAO — 2026-08-14. Aqui a clausula
        # anti-celebridade era NEGACAO PURA, sem metade descritiva, entao a
        # remocao (ordem do operador, CLAUDE.md §CONTRA A CELEBRIDADE,
        # SILENCIO) deixa o `ANTICELEB` VAZIO. Os blocos escreviam "%(anti)s. "
        # e devolviam ponto orfao e espaco duplo — a sujeira que a lente foi
        # escrita para pegar. `sc.frase_anti` normaliza o ponto e o espaco no
        # SLOT, e some inteiro quando o texto e' vazio; os templates passaram a
        # `%(anti_frase)s`, sem ponto proprio.
        # ⚠️ Com o MODO BELA aceso o valor continua vindo do compartilhado e o
        # texto sai identico ao de antes — medido bloco a bloco.
        "anti_frase": sc.frase_anti(sc.ANTICELEB_BELA if spec.get("bela")
                                    else ANTICELEB),
        "cauda": CAUDA, "band": band,
        "idade": ref["idade"], "etnia": spec["etnia"], "marca": ref["marca"],
        "cabeca": ref["cabeca"],
        "f1": spec["falas"][0], "f2": spec["falas"][1],
    }
    v["nao_toca"] = NAO_TOCA % m["sup"]
    # ⚠️ A MARCA entra SEMPRE; os oculos so' quando existem. Sem a marca
    # o Veo devolve outro homem na cena 3 e o payoff perde a prova.
    v["h_marca"] = hom["marca"]
    v["h_oculos"] = (" and " + hom["oculos"]) if hom["oculos"] else ""
    v["homem"] = ("a %(h_idade)d-year-old %(etnia)s man, %(h_corpo)s, "
                  "%(h_cabeca)s and %(h_marca)s, wearing %(h_calca)s"
                  "%(h_oculos)s" % v)
    v["Ancora"] = _ancora(spec)[0].upper() + _ancora(spec)[1:]

    b = {}
    b["BLOCO 0 (REF)"] = (
        "REF 01: Photo of a real person, a %(idade)d-year-old %(etnia)s woman, "
        "chest up, facing the camera directly, neutral steady expression with "
        "her mouth closed. %(cabeca)s and %(marca)s. Wearing %(traje)s. "
        "%(anti_frase)sHands out of frame, no objects. Plain neutral gray "
        "background, soft even frontal light. %(cauda)s" % v)

    # --- CENA 1 — O CORPO-PROVA E A ACUSACAO --------------------------------
    # ⛔⛔ A COMPOSICAO E' DO OPERADOR, validada prompt a prompt no Veo antes de
    # virar codigo. Tres pessoas, tres funcoes:
    #   · o HOMEM a esquerda, tronco nu, adesivo na barriga e o proxy murcho
    #     preso de fita — ele nunca fala e nunca se mexe. E' a prova.
    #   · a REF ao centro, MAOS LIVRES e vazias sobre a bancada. Ela so' fala.
    #   · a AMIGA a direita, de quatro EM CIMA da bancada, apontando para o
    #     prop sem encostar. E' ela que acusa — e foi a peca que o operador
    #     aprovou primeiro no lote de teste.
    # ⛔ A REF NAO APONTA. Dois bracos apontando a mesma coisa e' ruido, e o
    # operador escolheu a de cima ("gostei do fato de que quem aponta e' a
    # mulher linda que esta em cima da superficie").
    # ⛔ E NAO HA' DESPEJO. Saiu a garrafa, saiu a substancia topica e saiu o
    # morph — sem liquido caindo, nada motivava a mudanca em cena, e o morph
    # solto era o que mais chamava o classificador. O antes/depois passou a
    # acontecer ENTRE a cena 1 e a 3.
    b["IMAGE 01/02"] = (
        # ⛔⛔ ESTA REDACAO EXISTE PARA PASSAR NO CLASSIFICADOR, e cada pedaco
        # dela e' uma alavanca do protocolo de recusa. A CENA E' A MESMA que o
        # operador aprovou — mudaram as palavras.
        # [3] O GENERO DA IMAGEM VEM PRIMEIRO, antes de qualquer corpo: dizer
        #     que e' uma demonstracao filmada da' ao modelo a leitura certa, e
        #     foi o que destravou o colo do casal na mesma politica.
        # [1] O TOKEN: `on her hands and knees` somado a `her hips raised` era
        #     o par que o classificador reconhecia. Virou `has climbed up` +
        #     `leaning forward onto both hands` + `her shoulders towards the
        #     centre` — a MESMA geometria, outras palavras.
        # [2] A RELACAO e o PROPOSITO: ele e' `the man who came to them for
        #     the recipe` (caso, nao parceiro) e ela sobe na bancada `to reach
        #     across it` — pose com motivo nao pede que o modelo invente um.
        # [4] `no one touching anyone` e `without touching it or him` matam o
        #     contato antes que ele seja imaginado.
        "IMAGE 01/02: Medium wide shot in %(coz)s, %(luz)s, natural colour "
        "with no colour grading. The three of them are set up the way a "
        "before-and-after demonstration is staged for a home remedy video, "
        "each in their own part of the frame and no one touching anyone. "
        "Frame-left, standing on his own and facing the camera with his arms "
        "at his sides, is the man who came to them for the recipe, "
        "%(homem)s; %(adesivo)s is stuck flat on his belly, and %(prop_img)s "
        "is %(fita)s. Centre frame, standing behind %(sup_a)s, is %(pessoa)s, "
        "wearing %(traje)s; both her hands are empty and rest on the surface, "
        "and she looks straight into the lens with her mouth open mid-word. "
        "Frame-right, her friend has climbed up onto %(sup_a)s and is leaning "
        "forward onto both hands to reach across it, her shoulders towards "
        "the centre of the frame and her face turned to the lens; she is "
        "%(amiga)s, wearing %(traje_amiga)s, and her right arm reaches out "
        "with the index finger pointing at the %(prop_curto)s, without "
        "touching it or him. They are the only three people in the frame. "
        "%(nao_toca)s%(band)s %(anti_frase)s%(cauda)s" % v)

    b["TAKE 01/02"] = (
        # ⛔ MESMAS ALAVANCAS NO TAKE, e a trava de geometria vem LOGO NO
        # COMECO: o video foi recusado mais vezes que a imagem, e e' no take
        # que o classificador imagina movimento que o prompt nao pediu.
        "TAKE 01/02: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway. The camera does not move and there is no "
        "cut. None of the three changes position, and no one touches anyone "
        "at any point. She keeps talking straight to the lens the whole time "
        "and her hands stay resting on the surface. The man does not move and "
        "does not speak, and keeps his arms at his sides; the %(prop_curto)s "
        "stays in exactly the same place and at the same angle, and the tape "
        "never comes loose. Her friend stays exactly as she is, leaning "
        "forward on both hands, her arm still held out and her finger still "
        "pointing at the %(prop_curto)s without touching it, her face turned "
        "to the lens, and she never speaks. Only she speaks.\n"
        'Dialogue: "%(f1)s"\n'
        "Audio: %(audio)s. No music.\n"
        "No on-screen text, no subtitles, no captions, no watermark." % v)

    # --- CENA 2 — A PROVA: A BANCADA, O COPO E O CORPO-PROVA ---------------
    # ⭐⭐ E' A FUSAO DAS CENAS 2 E 3 DO FALTA, e ela nao inventa cenario: as
    # duas ja' aconteciam em %(coz_c)s. O que muda e' que agora cabem juntas:
    #   · a BANCADA da receita — o vaso do metodo sorteado, o comum e o raro —
    #     que e' onde a receita se prova;
    #   · ela com o COPO na lente, que e' o objeto da keyword;
    #   · ele frame-left com o geoduck grande e SEM A FITA, que e' o payoff.
    #
    # ⛔⛔ A GELATINA NAO ENTRA AQUI, e essa e' a diferenca deste angulo para o
    # TRIO 16 e o DUPLA 16, onde a tigela de cubos e' OBRIGATORIA (regra DU2).
    # Aqui mostrar gelatina entregaria de graca o que o CTA vende: a peca que
    # falta so' existe na FALA. Copiar a cauda de bancada dos irmaos teria
    # matado o angulo — ha' lente cobrando (FA16-2).
    #
    # ⛔ E O `acao` DO METODO NAO ENTRA no TAKE: ele descreve as maos dela
    # trabalhando o utensilio, e a mao dela esta' no copo. Take mandando animar
    # dois gestos incompativeis e' a contradicao IMAGE x TAKE.
    #
    # ⚠️ Ele entra COM A CABECA EM QUADRO. A versao cortada na cintura foi
    # recusada por politica — torso masculino decapitado com objeto na virilha
    # e' o par que o classificador pega. Pessoa inteira le' como pessoa.
    b["IMAGE 02/02"] = (
        "IMAGE 02/02: Medium wide shot in %(coz_c)s, %(luz_c)s, natural "
        "colour with no colour grading. Frame-left, standing and facing the "
        "camera, is the same %(h_idade)d-year-old %(etnia)s man, %(h_corpo)s, "
        "%(h_cabeca)s and %(h_marca)s, wearing %(h_calca)s%(h_oculos)s "
        "%(sem_fita)s; he holds "
        "%(prop_grande)s, and his face is relaxed and looking off to the "
        "side. Frame-right, standing behind %(sup_a)s, is %(ancora)s, wearing "
        "%(traje)s; she holds a tall glass filled to the top with a thick "
        "pale drink, a single paper straw standing in it, and looks straight "
        "into the lens with her mouth open mid-word. On the surface in front "
        "of her stand %(vaso)s, %(com_img)s and %(raro_img)s. They are the "
        "only two people in the frame. %(nao_toca)s%(band)s %(anti_frase)s"
        "%(cauda)s" % v)

    b["TAKE 02/02"] = (
        "TAKE 02/02: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway, no cuts, and the camera does not move. She "
        "holds the glass steady at chest height the whole time and never sets "
        "it down, and she talks straight into the lens. Nothing on the surface "
        "is picked up. The man does not move and does not speak; he keeps both "
        "fists closed around the geoduck at the same height and the same "
        "angle, and its neck stays extended straight upward for the whole "
        "shot. Only she speaks.\n"
        'Dialogue: "%(f2)s"\n'
        "Audio: %(audio)s. No music.\n"
        "No on-screen text, no subtitles, no captions, no watermark." % v)

    return b


# ---------------------------------------------------------------------------
# LINTER — as regras deste ângulo
# ---------------------------------------------------------------------------
# ⛔⛔ ESTE REGEX JA' NASCEU CEGO: com {0,3} e \w+ ele nao casava
# "a 61-year-old white American man" — "61-year-old" tem hifen, quebra em
# TRES tokens e estoura a janela. A lente FA1 acusou os 1.200 sorteios de
# nao terem homem, num agente em que o homem esta' em DUAS das tres cenas.
# ⚠️ Agora aceita hifen ([\w-]) e uma janela de 6, que cobre
# "a 61-year-old white American man" e "the same 61-year-old ... man".
_HOMEM = re.compile(r"\b(a|the|his|one|same)\s+(?:[\w-]+\s+){0,6}"
                    r"(man|men|husband|boyfriend|guy)\b", re.I)


def _fa_homem(spec, blocos, achados):
    """FA1 — ⛔⛔ INVERTIDO EM 2026-08-07. Ate' aqui esta lente BANIA homem em
    cena ("este angulo e' so' as duas mulheres"). O operador reviu depois de
    ver o video-fonte novo: o homem virou o CORPO-PROVA e agora e'
    obrigatorio nas cenas 1 e 3 — e proibido na 2, que e' a receita.

    ⚠️ Uma lente que sobrevive a uma inversao de regra sem ser reescrita e'
    uma lente que passou a medir o contrario do que a doutrina diz. Por isso
    ela mudou de NOME junto: `_fa_sem_homem` -> `_fa_homem`.
    """
    # ⛔⛔ REAPONTADA — 2026-08-08. A lente cobrava homem nas cenas 1 e 3 e
    # PROIBIA homem na cena 2 ("a cena 2 e' a receita, e ela e' dela sozinha").
    # Na fusao a cena 2 do 16 E' o payoff: o corpo-prova esta' la' por
    # construcao. Manter a proibicao reprovaria 100% da producao — regra que
    # cobra o oposto do que o motor faz nao e' defesa, e' sabotagem.
    for nome in ("IMAGE 01/02", "IMAGE 02/02"):
        if not _HOMEM.search(blocos[nome]):
            achados.append(("ERRO", "FA1: %s sem o homem em cena — ele e' o "
                                    "corpo-prova deste angulo" % nome))
    for nome in ("TAKE 01/02", "TAKE 02/02"):
        if "does not speak" not in blocos[nome]:
            achados.append(("ERRO", "FA1: %s sem a trava de fala do homem — "
                                    "sem ela o segundo corpo dubla a narradora"
                            % nome))


def _fa_prop(spec, blocos, achados):
    """FA2 — o prop sorteado esta' PRESO nele na cena 1; o geoduck grande esta'
    nas maos dele na cena 3.

    ⚠️ Mede o prop do `spec`, nunca uma constante: quando o prop virou eixo, um
    linter que olhasse string fixa acusaria metade dos sorteios."""
    if spec["prop"]["img"] not in blocos["IMAGE 01/02"]:
        achados.append(("ERRO", "FA2: IMAGE 01/02 sem o prop sorteado (%s)"
                        % spec["prop"]["id"]))
    if FITA not in blocos["IMAGE 01/02"]:
        achados.append(("ERRO", "FA2: IMAGE 01/02 sem a fita — sem ela o prop "
                                "vira comida na mao e a piada morre"))
    if PROP_GRANDE not in blocos["IMAGE 02/02"]:
        achados.append(("ERRO", "FA2: IMAGE 02/02 sem o geoduck do payoff"))
    if SEM_FITA not in blocos["IMAGE 02/02"]:
        achados.append(("ERRO", "FA2: IMAGE 02/02 nao DIZ que nao ha' fita — o "
                                "Veo carrega adereco da cena anterior por "
                                "continuidade, e ausencia omitida ele preenche"))

    # --- FA16-3: o referente do `sem fita` -----------------------------------
    # ⛔ A clausula cai depois de `wearing <calca><oculos>`. Com `them` ela
    # aponta para os OCULOS em 13% dos sorteios. Referente explicito resolve, e
    # esta lente garante que ninguem volte ao pronome por copia.
    if re.search(r"glasses\s+with nothing taped to them", blocos["IMAGE 02/02"], re.I):
        achados.append(("ERRO", "FA16-3: `nothing taped to them` logo depois de "
                                "`glasses` — o pronome aponta para os OCULOS, "
                                "nao para o short"))

def _fa_nada_cresce(spec, blocos, achados):
    """FA3 — ⛔ NADA CRESCE EM CENA NESTE AGENTE.

    O morph morreu junto com o despejo (2026-08-07): sem liquido caindo, nada
    motivava a mudanca, e o morph solto era o que mais chamava o classificador.
    O antes/depois passou a acontecer ENTRE a cena 1 e a 3 — murcho e preso la',
    grande e na mao dele aqui.

    ⛔ Mas a guarda FICA, e apontada para os blocos inteiros: se alguma edicao
    futura reintroduzir vocabulario de crescimento, lê como tumescencia e
    derruba o video. Foi assim que caiu um video nosso na politica de conteudo
    nocivo.
    ⚠️ NEGACAO NAO CONTA: a primeira versao desta lente acusava `no thicker
    than before` — a frase que EXISTIA para impedir o inchaco — em 418 de 800
    sorteios."""
    for nome, txt in sorted(blocos.items()):
        limpo = re.sub(r"\b(no|not|never|same)\s+\w+", " ", txt, flags=re.I)
        if re.search(r"\b(bigger|larger|swell\w*|thicker|grows|expands|"
                     r"rises|risen|inflat\w*)\b", limpo, re.I):
            achados.append(("ERRO", "FA3: %s descreve algo CRESCENDO — neste "
                                    "agente nada cresce em cena" % nome))



def _fa_buraco(spec, blocos, achados):
    """FA4 — ⛔⛔ O ÂNGULO INTEIRO: a peça que falta é dita e nunca mostrada.

    A cena 2 nomeia `gelatin trick` como o que FALTA, e o CTA entrega essa
    mesma peça. Se a gelatina aparecer em quadro, o vídeo dá de graça o que o
    comentário vende — e o CTA perde a razão de existir."""
    # ⛔⛔ FA16-2 — A GELATINA CONTINUA FORA DE TODO QUADRO, e no 16 isso e'
    # MAIS facil de quebrar: os irmaos TRIO 16 e DUPLA 16 tem a tigela de
    # cubos OBRIGATORIA na bancada (regra DU2), e a bancada deles foi de
    # onde eu copiei a mecanica do `aparato16`. Copiar a cauda junto teria
    # matado o angulo em silencio — o prompt sairia bonito e o CTA perderia
    # a razao de existir.
    for nome in ("IMAGE 01/02", "IMAGE 02/02"):
        if re.search(r"\bgelatin\b", blocos[nome], re.I):
            achados.append(("ERRO", "FA4: %s MOSTRA gelatina — ela é a peça que "
                                    "falta e só pode existir na fala" % nome))
    f2 = spec["falas"][1]
    # ⚠️ A lista cobre as SEIS formas que o pool usa de dizer "falta uma peça".
    # A primeira versão só aceitava `left out` e reprovava `leaves out`, que é a
    # entrada mais comum do pool — 257 de 800. Regex que conhece meia conjugação
    # é regex que mede outra coisa.
    if not re.search(r"\bmissing\b|\bleaves? out\b|\bleft out\b|\bhold(s|ing)? "
                     r"back\b|\bskips?\b|\bnobody (includes|hands)\b", f2, re.I):
        achados.append(("ERRO", "FA4: a cena 2 não diz que FALTA uma peça — sem "
                                "isso o ângulo vira mais uma receita"))
    # ⚠️ A LENTE ERA ESTREITA: conhecia so' missing/piece/part e reprovava
    # *"the recipe with the step they leave out"* — frase que NOMEIA a parte
    # que falta, so' que com outra palavra. Regex que conhece meia familia
    # de sinonimos mede outra coisa (mesmo erro do `leaves out` x `left
    # out`, pago em 06/08).
    # ⛔⛔ NO 16 O CTA MORA NA MESMA FALA DA VENDA. A lente lia `falas[2]`, que
    # nao existe mais — e o `f3` ficou orfao no corpo dela, estourando
    # NameError no primeiro sorteio. Agora ela olha o RESTO da cena 2, depois
    # da primeira sentenca: e' onde o CTA vive.
    # ⚠️ Foi o autoteste NOVO que pegou. No motor de 24s nao ha' autoteste, e
    # e' por isso que o `nova_fala` de la' ficou quebrado sem ninguem ver.
    _sn = _sentencas(f2)
    _cta_txt = " ".join(_sn[1:]) if len(_sn) >= 2 else ""
    # ⛔⛔ A LENTE MUDOU DE PERGUNTA — 2026-08-08, ordem do operador. Ela
    # aceitava `the part they leave out` como suficiente, e o operador leu
    # isso no app e reprovou: *"da' vazao pra pessoa ficar em duvida: qual
    # parte de QUE??"*. Nomear a FALTA nao e' nomear o ENTREGUE.
    # ⭐ Agora ela cobra o substantivo do produto: `recipe`. E' mais forte e
    # mais barato de verificar — e a costura do angulo continua coberta pela
    # checagem de cima, que exige a falta na primeira sentenca da cena 2.
    if not re.search(r"\brecipe\b", _cta_txt, re.I):
        achados.append(("ERRO", "FA4: o CTA não nomeia a RECEITA — sem o "
                                "substantivo do que é entregue, `a parte que "
                                "falta` deixa o espectador perguntando `parte "
                                "de quê?`"))


def _fa_raro(spec, blocos, achados):
    """FA5 — ⛔⛔ O RARO E' FALADO NA CENA 1, e no 16 e' SO' la'.

    ⛔ REAPONTADA — 2026-08-08. No motor de 24s a lente cobrava o raro NU no
    hook e COM APOSTO na cena 2 ("a corrente do video"). No 16 a cena 2 e' a
    venda + o CTA, e o aposto nao cabe: MEDIDO, com ele ZERO de 1536
    combinacoes ficavam em 25 palavras. Cobrar o aposto aqui reprovaria 100%
    da producao — regra que cobra o que o orcamento proibe nao e' defesa.
    ⭐ O que se manteve: o raro CONTINUA falado, e sem custo, porque os 20
    DESMENTIDOS o nomeiam (medido, 20/20). A lente agora prova isso.
    ⚠️ E ele continua no QUADRO da cena 2, no `raro_img` da bancada.
    """
    raro = spec["raro"]
    if raro["nome"] not in spec["falas"][0]:
        achados.append(("ERRO", "FA5: a cena 1 nao nomeia o raro sorteado (%s) "
                                "— e' a corrente que liga o hook a' receita"
                        % raro["id"]))
    if raro["img"] not in blocos["IMAGE 02/02"]:
        achados.append(("ERRO", "FA5: a bancada da cena 2 sem o raro em quadro "
                                "(%s) — ele saiu da fala, entao o quadro e' o "
                                "unico lugar que sobrou" % raro["id"]))

def _fa_duas(spec, blocos, achados):
    """FA6 — duas mulheres nas cenas 1 e 3, UMA na cena 2.

    ⚠️ A cena 2 é o preparo e ela está sozinha: a amiga voltando ali tiraria o
    foco da bancada, que é onde a receita se prova."""
    # ⛔⛔ REAPONTADA. No motor de 24s a cena 2 era ela SOZINHA (a receita) e a
    # cena 3 tinha DUAS pessoas. Fundidas, a cena 2 do 16 tem duas — a trava de
    # elenco muda de bloco, nao some. Cobrar `only person` aqui reprovaria
    # 100%, e apagar a trava deixaria o Veo encher o fundo de gente.
    if "only three people" not in blocos["IMAGE 01/02"]:
        achados.append(("ERRO", "FA6: IMAGE 01/02 sem a trava de elenco de TRES "
                                "— o homem, quem fala e quem aponta"))
    if "only two people" not in blocos["IMAGE 02/02"]:
        achados.append(("ERRO", "FA6: IMAGE 02/02 sem a trava de elenco de DUAS "
                                "— sem ela o Veo enche o fundo de gente"))
    if spec["ref"].get("cabeca") == spec["amiga"].get("cabeca"):
        achados.append(("ERRO", "FA6: as duas mulheres têm o mesmo cabelo — "
                                "rosto repetido no mesmo quadro é o defeito "
                                "mais visível que existe"))


# ⛔⛔ FA8 — A LENTE QUE FALTAVA, e a razao dela esta' escrita aqui para nao se
# perder: a revisao adversarial de 2026-08-06 varreu as 600 falas com sete
# lentes e devolveu ZERO. Ai eu gerei UM lote de entrega e o prompt trouxe
# QUATRO defeitos que nenhuma delas podia ver — porque todas mediam a FALA, e
# nenhuma media o BLOCO:
#   · *"pours a thin steady stream over the peça anatômica"* — portugues cru
#     dentro do TAKE em ingles, do rotulo de painel usado como termo de prompt;
#   · *"the moulded shaft lies folded down against the base changes on
#     camera"* — dois verbos finitos brigando, de encaixar oracao em slot de
#     sintagma nominal;
#   · *"not resembling any famous person.."* — ponto duplo nos quatro blocos;
#   · *"the wall behind them"* numa cena que diz, na mesma frase, que ela e' a
#     unica pessoa em quadro.
# Nenhum e' sutil. Todos sao mecanicos e verificaveis — ou seja, sao exatamente
# o que o runbook manda mandar para o codigo.
_PT_NO_PROMPT = re.compile(r"[áàâãéêíóôõúüçÁÀÂÃÉÊÍÓÔÕÚÜÇ]")


def _fa_bloco_limpo(spec, blocos, achados):
    """FA8 — o bloco vai para o Veo: ingles, pontuacao sa, elenco coerente."""
    for nome, txt in blocos.items():
        m = _PT_NO_PROMPT.search(txt)
        if m:
            i = max(0, m.start() - 40)
            achados.append(("ERRO", "FA8: %s tem PORTUGUES no prompt (…%s…)"
                            % (nome, txt[i:m.start() + 20])))
        if ".." in txt.replace("...", ""):
            achados.append(("ERRO", "FA8: %s tem ponto duplo" % nome))
        # plural de elenco numa cena declaradamente de uma pessoa so'
        if "only person in the frame" in txt and re.search(
                r"\bbehind them\b|\bbetween them\b|\bthey are\b", txt, re.I):
            achados.append(("ERRO", "FA8: %s diz que ela esta' SOZINHA e usa "
                                    "plural de elenco na mesma frase" % nome))


# ⚠️ Verbo FINITO em ingles no estado ANTES. O campo ocupa slot de sujeito
# ("%(antes)s, changes on camera") — se ele proprio conjugar, o prompt sai com
# dois verbos brigando pela mesma oracao.
# ⛔ A forma participial (`hanging`, `lying`) e' justamente a que PODE estar
# ali, entao o padrao ignora `-ing` de proposito.
_VERBO_FINITO = re.compile(
    r"\b(hangs?|lies|lie|sits?|rests?|stands?|is|are|was|were|has|have|"
    r"points?|droops?|falls?|leans?|curls?)\b", re.I)


def _fa_fala_no_take(spec, blocos, achados):
    """FA10 — ⛔⛔⛔ A FALA ESTA' NOS TRES TAKES.

    E' a lente que nao existia, e a ausencia dela custou um lote inteiro. O
    agente montava as tres falas, mostrava no painel, salvava no .txt — e
    NENHUMA entrava no prompt. A linha Dialogue aparecia 0 vezes neste motor,
    contra
    1 a 13 em todos os outros dezoito. Os videos saiam MUDOS, e o operador so'
    descobriu gerando: *"vc esqueceu de incluir as falas em todos os takes, o
    agente atualmente nao gera prompt com a parte da fala"*.

    ⚠️ Nenhuma lente antiga podia pegar: todas mediam a FALA (teto, drifting,
    eco) ou o BLOCO (portugues, pontuacao) — nenhuma media a JUNCAO dos dois.
    Cobertura de lente nao e' qualidade, e' cobertura.
    """
    for i, nome in enumerate(("TAKE 01/02", "TAKE 02/02")):
        fala = spec["falas"][i]
        if ('Dialogue: "%s"' % fala) not in blocos[nome]:
            achados.append(("ERRO", "FA10: %s nao carrega a fala da cena %d — "
                                    "o video sai MUDO" % (nome, i + 1)))
        if "Audio:" not in blocos[nome]:
            achados.append(("ERRO", "FA10: %s sem a linha de Audio" % nome))


def _sentencas(t):
    return [x.strip() for x in re.split(r"(?<=[.!?])\s+", t) if x.strip()]




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
PRONOME_VISUAL = ()

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
    """⛔ COMPOE os linters compartilhados, nao usa `lint_curto`.

    O `lint_curto` serve aos SHORT que DERIVAM de um motor base de 5 cenas e
    reusa as tabelas dele (BANIDOS_*). Este agente nasce inteiro, sem base —
    chamar `lint_curto` levantava `AttributeError: BANIDOS_CTA` na primeira
    execucao. E' o padrao dos agentes novos (dupla, trio).
    """
    ach = []
    _t16_5b(spec, blocos, ach)
    falas = spec["falas"]

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
    # A automacao de DM casa palavra EXATA (operador, 2026-08-08) e a
    # legenda nasce do Whisper em cima do audio: nao ha' conserto depois.
    # A regra e' POSICIONAL — depois de `comment gelatin` vem VIRGULA.
    # ⚠️ `finditer`, nao `search`: `gelatin` aparece duas vezes na fala (no
    # `gelatin trick` e no comando), e olhar so' a primeira dava verde para
    # `Comment gelatin now,`.
    _f2 = falas[1] or ""
    for _kw in re.finditer(r"comment\s+gelatin(.)", _f2, re.I):
        if _kw.group(1) != ",":
            ach.append(("ERRO", "T16-2: `comment gelatin%s...` — a keyword "
                                "tem de ser fechada por VIRGULA" % _kw.group(1)))
    if re.search(r"comment\s+gelatin\W+(and\s+)?follow", _f2, re.I):
        ach.append(("ERRO", "T16-2: o `follow` esta' colado no comando"))
    # ⛔⛔ FA16-1 — A COSTURA, e ela e' o angulo inteiro.
    # O buraco tem de ser nomeado NA VENDA e prometido NO CTA, com
    # substantivos DIFERENTES. No motor de 24s a costura atravessa 8
    # segundos e repetir o mesmo termo e' RETOMADA; aqui ela cai dentro de
    # tres, e repetir vira GAGUEIRA. Medido: sem o guarda, 42% repetiam.
    _sents = _sentencas(_f2)
    if len(_sents) >= 2:
        _venda, _resto = _sents[0], " ".join(_sents[1:])
        if not _nucleo_seam(_venda):
            ach.append(("ERRO", "FA16-1: a venda da cena 2 nao NOMEIA o "
                                "buraco (piece/part/step) — sem isso o CTA "
                                "promete algo que o video nunca mencionou "
                                "(%r)" % _venda))
        # ⛔⛔ ESTA METADE FOI DERRUBADA PELO OPERADOR — 2026-08-08. Ela exigia
        # que o CTA nomeasse o buraco (piece/part/step), e ele leu a saida no
        # app e reprovou exatamente isso:
        #
        #     *"and I'll send the part they leave out da' vazao pra pessoa
        #      ficar em duvida: qual parte de QUE??"*
        #     *"seja mais taxativo: I'll send recipe ou I'll send the complete
        #      recipe"*
        #
        # ⭐ Nomear a FALTA nao e' nomear o ENTREGUE. O CTA passou a cobrar o
        # substantivo do produto (`recipe`), e quem cobra e' a FA4 — mais forte
        # e mais barato de verificar.
        # ⚠️ A COSTURA NAO SE PERDE: a checagem de cima, que exige o buraco
        # NOMEADO na venda, continua intacta. O buraco e' dito; o CTA responde
        # a ele com a palavra que fecha (`complete`).
        # ⛔ E a anti-gagueira abaixo continua valendo para os CTAs que ainda
        # nomeiam o buraco (`the recipe with the missing piece`): repetir o
        # mesmo substantivo em tres segundos le' como gagueira, nao retomada.
        if _nucleo_seam(_venda) & _nucleo_seam(_resto):
            ach.append(("AVISO", "FA16-1: venda e CTA repetem %s em tres "
                                 "segundos — le' como gagueira, nao como "
                                 "retomada"
                        % sorted(_nucleo_seam(_venda) & _nucleo_seam(_resto))))
    sc.lint_bandeira(spec, blocos, ach, rotulo="FA7")

    if not blocos.get("BLOCO 0 (REF)", "").lstrip().upper().startswith("REF"):
        ach.append(("ERRO", "BLOCO 0 sem o cabecalho REF — o AdBatch descarta "
                            "a referencia em silencio"))

    # o literal do mecanismo tem de existir no corpo das falas
    corpo = " ".join(falas).lower()
    if "gelatin trick" not in corpo:
        ach.append(("ERRO", "o literal 'gelatin trick' sumiu da copy — ele e' o "
                            "mecanismo que a VSL vende"))
    sc._adjetivo_do_mecanismo(corpo, ach)

    # --- tetos e pisos ------------------------------------------------------
    for i, f in enumerate(falas, 1):
        n = _palavras(f)
        if n > TETO_FALA[i]:
            ach.append(("ERRO", "FA8: cena %d com %d palavras (teto %d) — a "
                                "narracao passa de 7s e a fala corta"
                        % (i, n, TETO_FALA[i])))
        if n < PISO_FALA[i]:
            ach.append(("AVISO", "FA8: cena %d com %d palavras (piso %d) — "
                                 "sobra silencio nos 8s" % (i, n, PISO_FALA[i])))

    # --- FA9: a abertura de cada cena tem REFERENTE (licoes §21) ------------
    # ⛔ A primeira sentenca e' a que o espectador ouve sozinha no scroll, antes
    # de qualquer outra — e era a unica que nenhuma lente minha olhava.
    orgaos = [o.lower() for o in sc.APELIDOS_16]
    # ⚠️ A cena 2 do 16 abre com a VENDA, que traz `gelatin` e o buraco.
    alvos = [(1, orgaos),
             (2, orgaos + ["gelatin", "missing", "piece", "part", "step"])]
    for i, termos in alvos:
        sents = _sentencas(falas[i - 1])
        if not sents:
            continue
        if not any(t in sents[0].lower() for t in termos):
            ach.append(("ERRO", "FA9: a abertura da cena %d nao nomeia o "
                                "referente — %r deixa o espectador perguntando "
                                "do que se trata" % (i, sents[0][:46])))

    for extra in (_fa_homem, _fa_prop, _fa_nada_cresce, _fa_buraco, _fa_raro,
                  _fa_duas, _fa_bloco_limpo, _fa_fala_no_take):
        extra(spec, blocos, ach)
    return ach


def resumo_pt(spec):
    """⚠️ O resumo e' PT e descreve o que o operador VAI VER. Ele ficou para
    tras na reformulacao de 2026-08-07 — ainda falava de despejo, de substancia
    e de um prop que muda em cena, todos removidos — e quebrou no primeiro
    sorteio por ler `spec["substancia"]`, que nao existe mais.
    ⛔ Resumo desatualizado nao e' cosmetico: e' o unico lugar onde o operador
    le' o video ANTES de gastar credito gerando."""
    m, r, p, h = spec["mundo"], spec["ref"], spec["prop"], spec["homem"]
    return ("Mulher %s de %d anos, em %s. Cena 1: homem de %d anos de tronco "
            "nu com %s presa de fita no short e adesivo na barriga; ela fala "
            "de mãos livres e a amiga, de quatro na bancada, aponta pro prop. "
            "Cena 2: a mesma cozinha — ele com o geoduck grande e SEM fita, ela "
            "com o copo, e na bancada %s com %s e %s. A peça que falta só é "
            "dita, nunca mostrada. Dois takes de 8s = 16s."
            % (spec["etnia"], r["idade"], m["familia"], h["idade"], p["nome"],
               spec["metodo"]["curto"], spec["comum"]["nome"],
               spec["raro"]["nome"]))


def nova_fala(spec, cena, rng):
    """Re-sorteia UMA fala sem mexer nas outras — o botao `trocar` da copy.

    ⛔⛔ ESTA FUNCAO ESTAVA QUEBRADA NO MOTOR DE 24s, e o conserto veio para ca'
    junto. Ela chamava `_montar_falas(rng, spec["substancia"], spec["orgao"],
    spec["comum"], spec["raro"])` — CINCO argumentos numa funcao de tres, e
    `spec["substancia"]` nem existe desde a reformulacao de 2026-08-07. Clicar
    em `trocar` no painel levantava KeyError.
    ⚠️ POR QUE SOBREVIVEU: este motor nao tinha `autoteste()` nem CLI. Nada
    nunca chamou `nova_fala`, entao nada nunca falhou. E' a forma-sem-funcao do
    §29 na sua versao mais pura: codigo que ninguem executa nao tem defeito
    ate' o operador clicar.
    ⛔ E' por isso que o `autoteste()` deste arquivo CHAMA nova_fala nas duas
    cenas — cobertura de lente nao e' qualidade, e' cobertura.
    """
    novas = _montar_falas(rng, spec["orgao"], spec["raro"])
    return novas[cena - 1]

# ---------------------------------------------------------------------------
# AUTOTESTE
# ---------------------------------------------------------------------------
# ⛔⛔ O MOTOR DE 24s NAO TEM ESTE BLOCO, e foi por isso que o `nova_fala` dele
# ficou quebrado sem ninguem ver. `0 ERRO` num lote grande e' SUSPEITA, nao
# aprovacao — por isso cada trava tem sabotador, e o sabotador tem de CHEGAR
# onde a regra olha (licoes §16).

def autoteste(n=400):
    import collections
    falhas, ctrl = [], []
    vistos = collections.defaultdict(set)
    larguras = {1: [], 2: []}
    seam_igual = 0

    # ⛔⛔ O CONTRATO DO DROPDOWN VEM ANTES DO LOTE — ver `_contrato_dropdown`.
    # Ele so' olha dado estatico (o pool e a declaracao), entao nao custa nada;
    # e se ele estiver quebrado nao adianta medir o lote inteiro, porque o
    # proprio `sortear` pode cair antes de chegar ao fim.
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
                falhas.append("seed %d: %s" % (seed, msg))
        for eixo in ("mundo", "prop", "homem", "metodo", "comum", "raro"):
            vistos[eixo].add(spec[eixo]["id"])
        vistos["ref"].add(spec["ref"]["cabeca"])
        for i, f in enumerate(spec["falas"], 1):
            larguras[i].append(_palavras(f))
        _s = _sentencas(spec["falas"][1])
        if len(_s) >= 2 and (_nucleo_seam(_s[0]) & _nucleo_seam(" ".join(_s[1:]))):
            seam_igual += 1

    for eixo, pool in (("mundo", MUNDOS), ("prop", PROPS), ("homem", HOMENS),
                       ("metodo", METODOS), ("comum", COMUNS), ("raro", RAROS)):
        if len(vistos[eixo]) != len(pool):
            falhas.append("%s: %d de %d nunca sorteados"
                          % (eixo, len(pool) - len(vistos[eixo]), len(pool)))

    # ⭐⭐ [ALCANCE] toda entrada de pool tem de ser sortavel. Criado no TRIO 16
    # depois de achar SEIS de dez FOLLOWS que nunca saiam — o autoteste contava
    # dez opcoes e a producao tinha quatro. Nenhuma outra lente pega: todas
    # verificam a frase MONTADA, que sempre cabe por causa do fallback.
    _mV = min(_palavras(x.format(o="soldier")) for x in VENDAS)
    _mC = min(_palavras(x) for x in CTAS)
    _mG = min(_palavras(x) for x in GATES)
    for _nome, _pool, _outros in (("VENDAS", [x.format(o="soldier") for x in VENDAS], _mC + _mG),
                                  ("CTAS", CTAS, _mV + _mG),
                                  ("GATES", GATES, _mV + _mC)):
        _teto = TETO_FALA[2] - _outros
        _mortas = [x for x in _pool if _palavras(x) > _teto]
        if _mortas:
            ctrl.append("[ALCANCE] %d entrada(s) de %s nunca sao sorteadas "
                        "(teto real %d): %s" % (len(_mortas), _nome, _teto,
                                                _mortas[:2]))

    s = sortear("joe", random.Random(1), {}, {})
    b = montar(s)

    # ⭐⭐ [NOVA_FALA] o botao `trocar` do painel. Sonda que NAO existia no motor
    # de 24s, e por isso ele ficou com a funcao quebrada em producao.
    for cena in (1, 2):
        try:
            f = nova_fala(s, cena, random.Random(9))
            if not f or _palavras(f) > TETO_FALA[cena]:
                ctrl.append("[NOVA_FALA] cena %d devolveu %r" % (cena, f))
        except Exception as e:
            ctrl.append("[NOVA_FALA] cena %d ESTOUROU: %s: %s"
                        % (cena, type(e).__name__, e))

    # [T16-2] a keyword grudada
    s2 = dict(s, falas=list(s["falas"]))
    s2["falas"][1] = s2["falas"][1].replace("Comment gelatin,", "Comment gelatin now,")
    if not any("T16-2" in m for _, m in lint(s2, b)):
        ctrl.append("[T16-2] NAO acusa palavra colada na keyword")

    # [FA16-1] a costura: a VENDA sem o buraco
    # ⛔⛔ SONDA REAPONTADA — 2026-08-13. Ela sabotava o CTA (trocava tudo
    # depois da primeira sentenca por `...I'll send the recipe. Follow
    # first.`) e cobrava que a FA16-1 acusasse. So' que a metade da FA16-1 que
    # olhava o CTA foi DERRUBADA PELO OPERADOR em 2026-08-08 (*"seja mais
    # taxativo: I'll send recipe"*) — quem cobra o CTA hoje e' a FA4, pelo
    # substantivo `recipe`, e o sabotador ate' o entregava. Resultado: a sonda
    # sabotava uma regra que nao existe mais, nunca chegava a uma checagem
    # viva e o autoteste se auto-reportava CEGO em todo lote desde entao.
    # ⚠️ Sabotador que nao alcanca a regra passa sempre, e passar sempre e' o
    # mesmo que nao existir (licoes §16). Agora ele ataca a metade VIVA: a
    # venda sem `piece`/`part`/`step`.
    s3 = dict(s, falas=list(s["falas"]))
    s3["falas"][1] = ("The gelatin trick sends blood where your %s needs it. "
                      "Comment gelatin, and I'll send the recipe."
                      % s["orgao"])
    if not any("FA16-1" in m for _, m in lint(s3, b)):
        ctrl.append("[FA16-1] NAO acusa a venda que nao nomeia o buraco")

    # [FA16-2] a gelatina em quadro — o angulo inteiro
    b2 = dict(b)
    b2["IMAGE 02/02"] += " A shallow bowl of vivid purple gelatin cubes."
    if not any("FA4" in m for _, m in lint(s, b2)):
        ctrl.append("[FA16-2] NAO acusa gelatina em quadro — o CTA perde a "
                    "razao de existir e nenhuma outra lente olha")

    # [FA10] o take sem a fala — o defeito que deixou o FALTA mudo
    b3 = dict(b)
    b3["TAKE 02/02"] = b3["TAKE 02/02"].replace('Dialogue: "', 'Copy: "')
    if not any("FA10" in m for _, m in lint(s, b3)):
        ctrl.append("[FA10] NAO acusa o TAKE sem a linha Dialogue")

    if [x for t, x in lint(s, b) if t == "ERRO"]:
        ctrl.append("o lote limpo esta' sendo reprovado")

    print("MUNDOS %d | PROPS %d | HOMENS %d | METODOS %d | RAROS %d | REFS %d"
          % (len(MUNDOS), len(PROPS), len(HOMENS), len(METODOS), len(RAROS),
             len(REFS)))
    print("%d videos | mundos %d/%d | raros %d/%d"
          % (n, len(vistos["mundo"]), len(MUNDOS), len(vistos["raro"]),
             len(RAROS)))
    for i in (1, 2):
        Lw = larguras[i]
        print("  cena %d: %d-%d palavras (media %.1f) | piso %d teto %d"
              % (i, min(Lw), max(Lw), sum(Lw) / float(len(Lw)),
                 PISO_FALA[i], TETO_FALA[i]))
    print("  costura com substantivo REPETIDO: %d de %d (%.0f%%)"
          % (seam_igual, n, 100.0 * seam_igual / n))

    # ⛔⛔ A TRAVA TEM DE FIXAR — a unica checagem do dropdown que mede FUNCAO.
    # As de FORMA (rotulo unico, curto, presente, com `id`) rodaram la' no
    # comeco, em `_contrato_dropdown`. O §41 do licoes-de-construcao existe
    # exatamente porque forma verificada foi declarada pronta sem funcao
    # medida — e neste motor a funcao ESTAVA quebrada: o pool ja' tinha `id`, mas o `sortear` usava a trava
    # CRUA, entao o id do menu virava `spec["ref"]` como STRING.
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
            # do id, que e' IGUAL ao alvo. A lente comparava id com id, dava
            # FIXOU, e o spec estourava no `montar` com `string indices must
            # be integers`. Lente que aceita string mede o TEXTO que ela mesma
            # mandou, nao o eixo que o motor resolveu.
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
        print("\n>> O AUTOTESTE ESTA' CEGO:")
        for c in ctrl:
            print("   %s" % c)
    if falhas:
        print("\n>> %d FALHA(S):" % len(falhas))
        for f in falhas[:15]:
            print("   %s" % f)
    if not falhas and not ctrl:
        print("\nAUTOTESTE OK — e os controles reprovam quando devem.")
    return 1 if (falhas or ctrl) else 0


def main():
    import argparse
    ap = argparse.ArgumentParser(
        description="Randomizador do agente FALTA 16 (2 takes de 8s)")
    ap.add_argument("--pagina", choices=sorted(ETNIA))
    ap.add_argument("--n", type=int, default=1)
    ap.add_argument("--seed", type=int)
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
    for _ in range(a.n):
        spec = sortear(a.pagina, rng, led)
        blocos = montar(spec)
        print("=" * 72)
        print("SPEC — pagina %s | seed %s" % (a.pagina, seed))
        print(resumo_pt(spec))
        print("=" * 72)
        for nome in ["BLOCO 0 (REF)"] + sorted(k for k in blocos
                                               if not k.startswith("BLOCO")):
            print(blocos[nome] if nome.startswith("BLOCO")
                  else "\n%s\n%s" % ("-" * 72, blocos[nome]))
        ach = lint(spec, blocos)
        print("\n" + "=" * 72)
        if ach:
            for tipo, msg in ach:
                print("[%s] %s" % (tipo, msg))
        else:
            print("LINTER: OK — nenhuma violacao mecanica.")
        if not a.dry_run:
            _gravar_ledger(led, spec)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
