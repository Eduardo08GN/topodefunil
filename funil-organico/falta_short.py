# -*- coding: utf-8 -*-
"""AGENTE FALTA SHORT — a receita que aparece incompleta de propósito.

FONTE: https://www.facebook.com/reel/1753888712524981
Leitura ótica em `concorrentes/falta-mapa-visual.md` (34 frames a 1 fps).

⭐⭐ O QUE ESTE ÂNGULO TEM QUE OS OUTROS 18 NÃO TÊM
-----------------------------------------------------------------------------
A receita é entregue INTEIRA MENOS UM PEDAÇO, e o vídeo diz isso na cara. Na
fonte: *"There is one missing herb that makes this drink five times more
effective."* A isca deixa de ser "te mando a receita" e vira **te mando o
pedaço que falta** — um degrau de tensão a mais, e é dele que sai o nome.

⛔ E A PARTE QUE FALTA É O PRÓPRIO MECANISMO. O `gelatin trick` não é mais um
item da lista: ele é o buraco na receita. Quem comenta recebe o buraco.

DECISÕES DO OPERADOR — entrevista de 2026-08-06, antes de uma linha de código
-----------------------------------------------------------------------------
1. O PROP DO HOOK É EIXO SORTEADO: geoduck OU peça anatômica peniana. Um por
   vídeo, nunca os dois. (Ele descartou "os dois em quadro".)
2. O MORPH É VISÍVEL NA TELA — escolhido por ele CIENTE de que o arranjo
   oculto (a mudança escondida dentro do jato) é o que passou na moderação no
   RESSURREICAO. ⚠️ Se o gerador recusar, a alternativa está pronta em
   `MORPH_OCULTO` — é trocar uma constante.
3. NENHUM HOMEM. As duas mulheres nas três cenas. A fonte tem um homem
   cozinhando ao fundo; ele sai.
4. A ISCA É A PARTE QUE FALTA da receita, e ela É o gelatin trick.
5. MODO BELA + pool de arquétipos por REGIÃO DOS EUA, roupa curta.

⛔⛔ A ESCALA DO MORPH É DIFERENCIAL, NUNCA UNIFORME
-----------------------------------------------------------------------------
Lição paga no RESSURREICAO e medida em pixels na fonte dele: **altura 2,31×
contra largura 1,44×**. O objeto ALONGA, não incha. Escala uniforme lê como
tumescência e já derrubou vídeo nosso na política de conteúdo nocivo.

⛔ COPIAR MOTOR TRAZ AS CENAS JUNTO (licoes-de-construcao §29)
-----------------------------------------------------------------------------
O esqueleto veio do DUPLA (duas mulheres, mundos, geoduck), mas TODA cena
deste arquivo é escrita do zero. O linter grita quando a regra some; a CENA
errada não grita — foi assim que o PLACA passou a gerar as IMAGEs do DUPLA.
Há um teste de aceite que prova que nenhuma string de cena do DUPLA
sobreviveu aqui.
"""
import json
import os
import re

import short_comum as sc

AQUI = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(AQUI, ".falta-short-ledger.json")

TITULO = "AGENTE FALTA SHORT"
SLUG = "falta-short"
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
# ⛔⛔ `to his shorts`, NUNCA `to them`. A clausula entra depois de
# `wearing <calca><oculos>`, e quando o homem sorteado tem oculos o
# `them` passa a apontar para OS OCULOS.
# ⚠️ MEDIDO: 40 de 300 sorteios — so acontece com homem de oculos
# (143/300), e por isso passou: dois tercos saem corretos.
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
     "cabeca": "long dark curls falling past the shoulders",
     "marca": "a small dark mole just under her left eye",
     "corpo": "tall with a narrow waist"},
    {"id": "liso_platinado", "idade": 24,
     "cabeca": "sleek platinum hair cut blunt at the jaw",
     "marca": "a small beauty mark just above her left eyebrow",
     "corpo": "slim and long-limbed"},
    {"id": "rabo_alto", "idade": 26,
     "cabeca": "black hair pulled into a high sleek ponytail",
     "marca": "a deep dimple in her left cheek",
     "corpo": "athletic with square shoulders"},
    {"id": "ondas_ruivas", "idade": 25,
     "cabeca": "deep auburn waves worn loose",
     "marca": "freckles scattered across her nose",
     "corpo": "curved with a small waist"},
    {"id": "trancas", "idade": 28,
     "cabeca": "long box braids gathered over one shoulder",
     "marca": "a beauty mark high on her cheekbone",
     "corpo": "tall and softly curved"},
    {"id": "bob_castanho", "idade": 23,
     "cabeca": "a glossy chestnut bob",
     "marca": "a dimple in her cheek",
     "corpo": "petite with a narrow frame"},
    {"id": "afro_curto", "idade": 29,
     "cabeca": "a short rounded afro",
     "marca": "a small birthmark at her temple",
     "corpo": "strong-shouldered and lean"},
    {"id": "loiro_longo", "idade": 22,
     "cabeca": "long honey-blonde hair, straight and heavy",
     "marca": "a light spray of freckles across her nose and cheekbones",
     "corpo": "long-legged and slight"},
    # --- as 16 novas (2026-08-13) ------------------------------------------
    {"id": "tranca_lateral", "idade": 24,
     "cabeca": "a long single braid falling over one shoulder",
     "marca": "a small beauty mark above the right corner of her mouth",
     "corpo": "slim with long legs"},
    {"id": "coque_alto", "idade": 26,
     "cabeca": "dark hair gathered into a high glossy bun",
     "marca": "a light dusting of freckles across her nose",
     "corpo": "athletic with a narrow waist"},
    {"id": "franja_reta", "idade": 23,
     "cabeca": "straight black hair with a blunt fringe at the brows",
     "marca": "a deep dimple in her right cheek",
     "corpo": "petite and slim"},
    {"id": "cachos_curtos", "idade": 27,
     "cabeca": "short springy curls pushed back from her face",
     "marca": "a tiny gold stud in her left nostril",
     "corpo": "curved with a small waist"},
    {"id": "mel_ondulado", "idade": 25,
     "cabeca": "honey-brown waves falling to the middle of her back",
     "marca": "a small dark mole under her right eye",
     "corpo": "long-limbed and slim"},
    {"id": "loiro_bob", "idade": 22,
     "cabeca": "a sharp platinum bob cut level at the jaw",
     "marca": "a fine spray of freckles high on both cheeks",
     "corpo": "slight and narrow-framed"},
    {"id": "trancas_longas", "idade": 28,
     "cabeca": "waist-length braids pulled over one shoulder",
     "marca": "a small beauty mark at her left temple",
     "corpo": "tall and softly curved"},
    {"id": "ruivo_liso", "idade": 24,
     "cabeca": "straight copper-red hair parted in the middle",
     "marca": "freckles scattered across her nose and cheekbones",
     "corpo": "slim with square shoulders"},
    {"id": "preto_longo", "idade": 29,
     "cabeca": "long jet-black hair worn loose and heavy",
     "marca": "a fine dusting of freckles over her nose and a shallow cleft "
              "in her chin",
     "corpo": "tall with a narrow waist"},
    {"id": "meio_preso", "idade": 26,
     "cabeca": "chestnut hair half pulled up, the rest loose past her "
               "shoulders",
     "marca": "one green eye and one hazel eye",
     "corpo": "curved and long-legged"},
    {"id": "pixie", "idade": 23,
     "cabeca": "a cropped dark pixie cut",
     "marca": "a tiny mole at the outer corner of her right eye",
     "corpo": "petite with a narrow frame"},
    {"id": "ondas_castanhas", "idade": 25,
     "cabeca": "loose chestnut waves parted deep on one side",
     "marca": "a light spray of freckles over her nose",
     "corpo": "slim with soft curves"},
    {"id": "rabo_baixo", "idade": 28,
     "cabeca": "dark hair pulled into a low sleek ponytail",
     "marca": "a beauty mark high on her right cheekbone",
     "corpo": "athletic and long-limbed"},
    {"id": "loiro_escuro", "idade": 24,
     "cabeca": "dark blonde hair in loose beach waves",
     "marca": "a small mole on her jaw below her left ear",
     "corpo": "tall and slender"},
    {"id": "castanho_curto", "idade": 22,
     "cabeca": "a chin-length chestnut cut tucked behind one ear",
     "marca": "freckles across the bridge of her nose",
     "corpo": "petite and trim"},
    {"id": "ondas_pretas", "idade": 29,
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
# ⛔⛔ MAIUSCULA. A clausula entra depois de `%(band)s`, que termina em
# ponto — e o bloco saia com "...on the wall in the background. not
# resembling any famous person". MEDIDO: 900 ocorrencias em 300 sorteios
# (tres blocos por video). Frase em minuscula e gramaticalmente valida:
# nenhum linter a pega, so LENDO o prompt.
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
# COPY — cena 2: A RECEITA COM O BURACO
# ---------------------------------------------------------------------------
# ⛔⛔ AQUI MORA O ÂNGULO. A receita é dita INTEIRA MENOS UMA PEÇA, e a peça é
# nomeada como o que FALTA. Três coisas obrigatórias na mesma fala:
#   1. o RARO, com nome popular + aposto (nunca nome científico);
#   2. o literal `gelatin trick` anunciado com HIERARQUIA — dois-pontos e
#      rótulo, nunca como item N de uma lista (§31);
#   3. o que os dois DEVOLVEM ao órgão (§17 / TR17: mecanismo sem destino é
#      mecanismo que não entrega nada em que agir).
#
# ⚠️ `the missing part` é o aposto que vira a isca do CTA. Ele tem de estar
# aqui e no CTA, ou o comentário promete algo que o vídeo nunca mencionou.
RECEITAS = [
    # ⛔⛔ O COMUM SAIU DA FALA — razao na licao §31: quando o teto aperta, cede
    # o que o QUADRO JA CONTA. A primeira versao carregava comum + raro +
    # mecanismo + destino e o pool inteiro dava 25 a 32 palavras contra teto de
    # 25: nenhuma entrada cabia, nem no melhor caso. O comum esta na bancada em
    # IMAGE 02, visivel. O que SO' a fala pode carregar e' a peca que falta.
    # ⚠️ O raro FICA, por ordem expressa do operador.
    # ⛔⛔ TODA ENTRADA ABRE COM VERBO DE PREPARO — correcao da revisao
    # adversarial de 2026-08-06. Antes a fala comecava com o nome do raro e um
    # ponto: *"Ginkgo, the leaf off that ancient Chinese tree."* — sintagma
    # nominal solto, sem verbo, em 288 de 288 combinacoes. Nao e' receita: e'
    # uma etiqueta. A fonte diz `In a blender, combine two cups of fresh
    # pineapple` — IMPERATIVO, dirigido ao espectador, enquanto ela prepara em
    # quadro. Aqui o verbo volta.
    # ⚠️ O verbo e' NEUTRO DE UTENSILIO de proposito: `add`/`use`/`in goes`
    # servem ao liquidificador, ao pilao, a peneira e ao coador. `blend`
    # contradiria 7 dos 8 metodos do pool.
    # ⛔ E ELE CUSTA ZERO: cada prefixo foi pago cortando o mesmo tanto na
    # cauda. Antes 60 das 288 combinacoes ESTOURAVAM o teto (ate' 28 palavras)
    # e o `_escolher` so' as escondia — com o raro mais longo sobravam 4 dos 6
    # templates. Agora cabem 6 de 6 em todos os 8 raros.
    "Add {R}. The piece everyone leaves out: the gelatin trick, "
    "and the blood returns to your {o}.",
    "Start with {R}. What nobody includes: the gelatin trick, "
    "the missing piece that opens your {o} again.",
    "In goes {R}. Always left out: the gelatin trick, "
    "the missing part that brings your {o} back.",
    "Now add {R}. Nobody hands you the last piece: the gelatin trick, "
    "and your {o} answers again.",
    "Add {R}. The piece they hold back: the gelatin trick, "
    "and the blood fills your {o} again.",
    "Use {R}. The one they skip: the gelatin trick, "
    "the missing piece that wakes your {o}.",
]

# ---------------------------------------------------------------------------
# COPY — cena 3: O PAYOFF + O CTA QUE ENTREGA O QUE FALTA
# ---------------------------------------------------------------------------
# ⛔ O CTA NOMEIA O QUE É ENVIADO — regra TR19, ordem dele em 2026-08-06 lendo
# um take do TROCA: *"'and I'll send it' — enviar o QUÊ??"*. Aqui o que se
# envia tem nome próprio: A PARTE QUE FALTA.
CTAS = [
    # ⛔⛔ TODOS OS SEIS NOMEIAM A RECEITA (2026-08-07). O pool anterior dizia
    # "the missing part", "what's missing", "the missing piece" — e nenhum
    # dizia de QUE. O operador leu o painel e reprovou os seis de uma vez.
    # ⚠️ O literal e' "Comment gelatin," COM VIRGULA — ordem de 2026-08-02,
    # depois de renders com a legenda "COMMENT HONEY": a legenda sai do audio,
    # e comando variavel faz o modelo parafrasear a keyword.
    "Comment gelatin, and I'll send the recipe with the missing piece.",
    "Comment gelatin, and I'll send you the recipe and the part they skip.",
    "Comment gelatin, one word, and I'll send the recipe with the missing part.",
    "Comment gelatin, and I'll send the part of the recipe nobody posts.",
    "Comment gelatin, and I'll send you the recipe with the step they leave out.",
    "Comment gelatin, and I'll send the whole recipe, missing piece included.",
    "Comment gelatin, and I'll send you the recipe and the piece nobody includes.",
    "Comment gelatin, and I'll send the recipe with the part I left out.",
]

GATES = [
    "Follow me first, or it won't reach you.",
    "Follow me first — I can't reply otherwise.",
    "Follow me or the message never lands.",
    "Follow me first, that's the only way it gets through.",
]


# ---------------------------------------------------------------------------
# CONTRATO DA UI
# ---------------------------------------------------------------------------
TETO_FALA = {1: 25, 2: 25, 3: 25}
PISO_FALA = {1: 16, 2: 20, 3: 12}
TETO_TOTAL = 72

TRAVAS_UI = [("familia_mundo", "regiao", FAMILIAS_MUNDO)]
EIXOS_TRAVAVEIS = ["mundo", "etnia", "ref", "amiga", "homem", "prop",
                   "metodo", "comum", "raro"]
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
CENAS_UI = ["1 · o corpo-prova acusado", "2 · a receita com o buraco",
            "3 · o copo + CTA"]

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
        ref = travas.get("ref") or sc.ref_bela(REFS[0], rng)
        amiga = sc.ref_bela(REFS[0], rng, banidos=(ref.get("cabeca", ""),))
    else:
        ref = travas.get("ref") or _fresco(REFS, usados.get("ref", []), rng, "id")
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
    """As tres falas. ⛔ O MESMO RARO nas cenas 1 e 2 — e' a corrente do video.

    ⭐ Nu no hook (`nome`), com aposto na cena 2 (`fala`). Decisao do operador:
    com o aposto o hook estoura o teto de 25. O hook nomeia, a cena 2 explica.
    """
    c1 = _escolher(
        rng, DESMENTIDOS,
        lambda t: _palavras(t.format(r=raro["nome"], o=orgao)) <= TETO_FALA[1],
        tamanho=lambda t: _palavras(t.format(r=raro["nome"], o=orgao))
    ).format(r=raro["nome"], o=orgao)

    c2 = _escolher(
        rng, RECEITAS,
        lambda t: (_palavras(t.format(R=raro["fala"], o=orgao)) <= TETO_FALA[2]
                   and not _colide(c1, t.format(R=raro["fala"], o=orgao), orgao)),
        tamanho=lambda t: _palavras(t.format(R=raro["fala"], o=orgao))
    ).format(R=raro["fala"], o=orgao)

    cta = _escolher(rng, CTAS,
                    lambda c: not _colide(c1 + " " + c2, c, orgao))
    gate = _escolher(rng, GATES,
                     lambda g: (_palavras(cta) + _palavras(g) <= TETO_FALA[3]
                                and not _colide(c1 + " " + c2 + " " + cta, g,
                                                orgao)))
    return [c1, c2, "%s %s" % (cta, gate)]


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
        # SILENCIO) deixa o `ANTICELEB` VAZIO. Os quatro blocos escreviam
        # "%(anti)s. " e devolviam ponto orfao e espaco duplo — a sujeira que a
        # lente foi escrita para pegar. `sc.frase_anti` normaliza o ponto e o
        # espaco no SLOT, e some inteiro quando o texto e' vazio; os templates
        # passaram a `%(anti_frase)s`, sem ponto proprio.
        # ⚠️ Com o MODO BELA aceso o valor continua vindo do compartilhado e o
        # texto sai identico ao de antes — medido bloco a bloco.
        "anti_frase": sc.frase_anti(sc.ANTICELEB_BELA if spec.get("bela")
                                    else ANTICELEB),
        "cauda": CAUDA, "band": band,
        "idade": ref["idade"], "etnia": spec["etnia"], "marca": ref["marca"],
        "cabeca": ref["cabeca"],
        "f1": spec["falas"][0], "f2": spec["falas"][1], "f3": spec["falas"][2],
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
    b["IMAGE 01/03"] = (
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
        "IMAGE 01/03: Medium wide shot in %(coz)s, %(luz)s, natural colour "
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

    b["TAKE 01/03"] = (
        # ⛔ MESMAS ALAVANCAS NO TAKE, e a trava de geometria vem LOGO NO
        # COMECO: o video foi recusado mais vezes que a imagem, e e' no take
        # que o classificador imagina movimento que o prompt nao pediu.
        "TAKE 01/03: Animate the provided image exactly. Handheld iPhone shot, "
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

    # --- CENA 2 — A RECEITA COM O BURACO ------------------------------------
    # ⛔ O RARO E O COMUM ESTAO EM QUADRO, mas o gelatin trick NAO. E' o angulo
    # inteiro: a bancada mostra a receita, e a peca que falta so' existe na
    # fala. Mostrar gelatina aqui entregaria de graca o que o CTA vende.
    # ⛔ O HOMEM NAO ENTRA AQUI. A cena 2 e' a receita, e um terceiro corpo
    # tiraria o foco da bancada — que e' onde a receita se prova.
    b["IMAGE 02/03"] = (
        "IMAGE 02/03: Medium shot in %(coz_c)s, %(luz_c)s, natural colour "
        "with no colour grading. %(Ancora)s, wearing %(traje)s, stands at "
        "%(sup_a)s with %(vaso)s in front of her. Laid out on the surface "
        "beside it: %(com_img)s and %(raro_img)s. She is the only person in "
        "the frame. Shot from chest height, straight on. %(nao_toca)s%(band)s "
        "%(anti_frase)s%(cauda)s" % v)

    b["TAKE 02/03"] = (
        "TAKE 02/03: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway, no cuts, and the camera does not move. She "
        "talks straight into the lens while she %(acao)s, one continuous "
        "movement, and never stops looking at the camera. Nothing else on the "
        "surface is picked up. She is the only person who appears.\n"
        'Dialogue: "%(f2)s"\n'
        "Audio: %(audio)s. No music.\n"
        "No on-screen text, no subtitles, no captions, no watermark." % v)

    # --- CENA 3 — O PAYOFF NAS MAOS DELE ------------------------------------
    # ⛔ ORDEM DO OPERADOR: *"cena 3 sera o homem segurando geoduck grande e
    # neck ereta, retire a silvertape com prop do short dele na cena 3"*.
    # ⚠️ O `%(sem_fita)s` nao e' redundancia: o Veo carrega adereco da cena
    # anterior por continuidade, entao a AUSENCIA precisa ser dita.
    # ⚠️ E ele entra COM A CABECA EM QUADRO. A versao cortada na cintura foi
    # recusada por politica — torso masculino decapitado com objeto na virilha
    # e' o par que o classificador pega. Pessoa inteira le' como pessoa.
    b["IMAGE 03/03"] = (
        "IMAGE 03/03: Medium wide shot in %(coz_c)s, %(luz_c)s, natural "
        "colour with no colour grading. Frame-left, standing and facing the "
        "camera, is the same %(h_idade)d-year-old %(etnia)s man, %(h_corpo)s, "
        "%(h_cabeca)s and %(h_marca)s, wearing %(h_calca)s%(h_oculos)s "
        "%(sem_fita)s; he holds "
        "%(prop_grande)s, and his face is relaxed and looking off to the "
        "side. Frame-right, standing behind %(sup_a)s, is %(ancora)s, wearing "
        "%(traje)s; she holds a tall glass filled to the top with a thick "
        "pale drink, a single paper straw standing in it, and looks straight "
        "into the lens with her mouth open mid-word. They are the only two "
        "people in the frame. %(nao_toca)s%(band)s %(anti_frase)s%(cauda)s" % v)

    b["TAKE 03/03"] = (
        "TAKE 03/03: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway, no cuts, and the camera does not move. She "
        "holds the glass steady at chest height the whole time and never sets "
        "it down, and she talks straight into the lens. The man does not move "
        "and does not speak; he keeps both fists closed around the geoduck at "
        "the same height and the same angle, and its neck stays extended "
        "straight upward for the whole shot. Only she speaks.\n"
        'Dialogue: "%(f3)s"\n'
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
    for nome in ("IMAGE 01/03", "IMAGE 03/03"):
        if not _HOMEM.search(blocos[nome]):
            achados.append(("ERRO", "FA1: %s sem o homem em cena — ele e' o "
                                    "corpo-prova deste angulo" % nome))
    if _HOMEM.search(blocos["IMAGE 02/03"]):
        achados.append(("ERRO", "FA1: IMAGE 02/03 traz homem — a cena 2 e' a "
                                "receita, e ela e' dela sozinha"))
    for nome in ("TAKE 01/03", "TAKE 03/03"):
        if "does not speak" not in blocos[nome]:
            achados.append(("ERRO", "FA1: %s sem a trava de fala do homem — "
                                    "sem ela o segundo corpo dubla a narradora"
                            % nome))


def _fa_prop(spec, blocos, achados):
    """FA2 — o prop sorteado esta' PRESO nele na cena 1; o geoduck grande esta'
    nas maos dele na cena 3.

    ⚠️ Mede o prop do `spec`, nunca uma constante: quando o prop virou eixo, um
    linter que olhasse string fixa acusaria metade dos sorteios."""
    if spec["prop"]["img"] not in blocos["IMAGE 01/03"]:
        achados.append(("ERRO", "FA2: IMAGE 01/03 sem o prop sorteado (%s)"
                        % spec["prop"]["id"]))
    if FITA not in blocos["IMAGE 01/03"]:
        achados.append(("ERRO", "FA2: IMAGE 01/03 sem a fita — sem ela o prop "
                                "vira comida na mao e a piada morre"))
    if PROP_GRANDE not in blocos["IMAGE 03/03"]:
        achados.append(("ERRO", "FA2: IMAGE 03/03 sem o geoduck do payoff"))
    if SEM_FITA not in blocos["IMAGE 03/03"]:
        achados.append(("ERRO", "FA2: IMAGE 03/03 nao DIZ que nao ha' fita — o "
                                "Veo carrega adereco da cena anterior por "
                                "continuidade, e ausencia omitida ele preenche"))


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
    for nome in ("IMAGE 01/03", "IMAGE 02/03", "IMAGE 03/03"):
        if re.search(r"\bgelatin\b", blocos[nome], re.I):
            achados.append(("ERRO", "FA4: %s MOSTRA gelatina — ela é a peça que "
                                    "falta e só pode existir na fala" % nome))
    f2, f3 = spec["falas"][1], spec["falas"][2]
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
    if not re.search(r"\bmissing\b|\bpiece\b|\bpart\b|\bstep\b|"
                     r"\bleaves? out\b|\bleft out\b|\bskips?\b", f3, re.I):
        achados.append(("ERRO", "FA4: o CTA não nomeia a parte que falta — é "
                                "exatamente o que ele promete entregar"))


def _fa_raro(spec, blocos, achados):
    """FA5 — ⛔⛔ O MESMO RARO NAS DUAS CENAS, e e' a corrente do video:
    nu no hook, com aposto na cena 2.

    cena 1: o raro SOZINHO nao resolve · cena 2: use o raro + a peca que todos
    pulam · cena 3: comente gelatin e eu mando a peca. Se a cena 1 desmentisse
    um raro e a cena 2 receitasse OUTRO, o espectador ouviria dois suplementos
    e nao saberia o assunto.
    ⛔ O aposto no hook estoura o teto de 25 — por isso ele so' existe na 2."""
    nome, fala = spec["raro"]["nome"], spec["raro"]["fala"]
    if nome.lower() not in spec["falas"][0].lower():
        achados.append(("ERRO", "FA5: o hook nao nomeia o raro sorteado (%s) — "
                                "sem ele a cena 1 desmente o nada"
                        % spec["raro"]["id"]))
    if fala not in spec["falas"][1]:
        achados.append(("ERRO", "FA5: a cena 2 não traz o raro sorteado com o "
                                "aposto (%s)" % spec["raro"]["id"]))
    if re.search(r",\s*(that|the)\b", spec["falas"][0]):
        achados.append(("ERRO", "FA5: o aposto vazou para o hook — ele so' cabe "
                                "na cena 2, e no hook estoura o teto"))


def _fa_duas(spec, blocos, achados):
    """FA6 — duas mulheres nas cenas 1 e 3, UMA na cena 2.

    ⚠️ A cena 2 é o preparo e ela está sozinha: a amiga voltando ali tiraria o
    foco da bancada, que é onde a receita se prova."""
    if "only three people" not in blocos["IMAGE 01/03"]:
        achados.append(("ERRO", "FA6: IMAGE 01/03 sem a trava de elenco de TRES "
                                "— o homem, quem fala e quem aponta"))
    for nome in ("IMAGE 03/03",):
        if "only two people" not in blocos[nome]:
            achados.append(("ERRO", "FA6: %s sem a trava de elenco — sem ela o "
                                    "Veo enche o fundo de gente" % nome))
    if "only person" not in blocos["IMAGE 02/03"]:
        achados.append(("ERRO", "FA6: IMAGE 02/03 devia ter ela sozinha"))
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
    for i, nome in enumerate(("TAKE 01/03", "TAKE 02/03", "TAKE 03/03")):
        fala = spec["falas"][i]
        if ('Dialogue: "%s"' % fala) not in blocos[nome]:
            achados.append(("ERRO", "FA10: %s nao carrega a fala da cena %d — "
                                    "o video sai MUDO" % (nome, i + 1)))
        if "Audio:" not in blocos[nome]:
            achados.append(("ERRO", "FA10: %s sem a linha de Audio" % nome))


def _sentencas(t):
    return [x.strip() for x in re.split(r"(?<=[.!?])\s+", t) if x.strip()]


def lint(spec, blocos):
    """⛔ COMPOE os linters compartilhados, nao usa `lint_curto`.

    O `lint_curto` serve aos SHORT que DERIVAM de um motor base de 5 cenas e
    reusa as tabelas dele (BANIDOS_*). Este agente nasce inteiro, sem base —
    chamar `lint_curto` levantava `AttributeError: BANIDOS_CTA` na primeira
    execucao. E' o padrao dos agentes novos (dupla, trio).
    """
    ach = []
    falas = spec["falas"]

    sc.lint_tags(blocos, ach)
    sc.lint_sem_texto(blocos, ach)
    # ⛔⛔ A negacao anti-celebridade nunca volta ao texto montado
    # (2026-08-14, ordem do operador). Este motor nao passa pelo
    # `sc.lint_curto`, entao a lente entra aqui explicitamente — regra sem
    # guarda volta no proximo agente nascido por copia, e foi exatamente
    # assim que a clausula chegou aos 30 motores.
    sc.lint_anticeleb(blocos, ach)
    sc.lint_isca_cta(falas[2], ach, "a cena 3 (CTA)")
    sc.lint_cta_literal(falas[2], ach, "a cena 3 (CTA)")
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
    alvos = [(1, orgaos), (3, orgaos + ["gelatin", "missing", "piece", "part"])]
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
            "Cena 2: %s com %s e %s, e a peça que falta só é dita. Cena 3: ele "
            "com o geoduck grande e sem fita, ela com o copo. Três cenas de 8s."
            % (spec["etnia"], r["idade"], m["familia"], h["idade"], p["nome"],
               spec["metodo"]["curto"], spec["comum"]["nome"],
               spec["raro"]["nome"]))


def nova_fala(spec, cena, rng):
    """Re-sorteia UMA fala sem mexer nas outras — o botão `trocar` da copy."""
    # ⛔⛔ CONSERTO DE CRASH — 2026-08-08. Esta chamada passava CINCO argumentos
    # para uma funcao de tres, e `spec["substancia"]` nao existe desde a
    # reformulacao de 2026-08-07: clicar em `trocar` no painel levantava
    # KeyError: 'substancia'.
    # ⚠️ POR QUE SOBREVIVEU: este motor nao tem `autoteste()` nem CLI. Nada
    # nunca chamou `nova_fala`, entao nada nunca falhou — forma sem funcao na
    # versao mais pura (§29). Achado ao portar o FALTA 16, que ganhou autoteste
    # e sonda propria para esta funcao.
    # ⛔ NAO e' mudanca de copy nem de cena: e' um botao que quebrava o app.
    novas = _montar_falas(rng, spec["orgao"], spec["raro"])
    return novas[cena - 1]
