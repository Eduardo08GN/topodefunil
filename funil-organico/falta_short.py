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
import argparse
import json
import os
import random
import re
import sys

import short_comum as sc

AQUI = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(AQUI, ".falta-short-ledger.json")

TITULO = "AGENTE FALTA SHORT"
SLUG = "falta-short"
SUBTITULO = ("a receita aparece incompleta · a parte que falta é o mecanismo · "
             "gerador offline de prompts Veo")

# ⚠️ A etnia aqui NAO vem da pagina — vem do MUNDO (doutrina "etnia arrasta o
# mundo inteiro"). A tabela existe so' para a UI listar as paginas.
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
     "coz": "an Appalachian farmhouse kitchen with painted board walls and a "
            "deep porcelain sink",
     "coz_c": "the same Appalachian farmhouse kitchen",
     "sup_a": "a worn pine counter", "sup": "pine counter",
     "luz": "flat grey daylight through a single window",
     "luz_c": "the same flat grey daylight",
     "etnias": ["white American"]},
    {"id": "sulista", "familia": "sulista",
     "coz": "a Southern kitchen with pale yellow beadboard walls and a screen "
            "door standing open",
     "coz_c": "the same Southern kitchen",
     "sup_a": "a scrubbed wooden table", "sup": "wooden table",
     "luz": "warm afternoon light through the screen door",
     "luz_c": "the same warm afternoon light",
     "etnias": ["Black American"]},
    {"id": "texas", "familia": "texas",
     "coz": "a Texas ranch kitchen with saltillo tile and a heavy iron range",
     "coz_c": "the same Texas ranch kitchen",
     "sup_a": "a thick butcher block", "sup": "butcher block",
     "luz": "hard midday sun through a wide window",
     "luz_c": "the same hard midday sun",
     "etnias": ["white American"]},
    {"id": "meio_oeste", "familia": "meio_oeste",
     "coz": "a Midwestern kitchen with laminate cabinets and a wall clock",
     "coz_c": "the same Midwestern kitchen",
     "sup_a": "a speckled formica counter", "sup": "formica counter",
     "luz": "even overcast light through a curtained window",
     "luz_c": "the same even overcast light",
     "etnias": ["white American"]},
    {"id": "nova_inglaterra", "familia": "nova_inglaterra",
     "coz": "a New England kitchen with white shaker cabinets and a soapstone "
            "sink",
     "coz_c": "the same New England kitchen",
     "sup_a": "a soapstone counter", "sup": "soapstone counter",
     "luz": "cool north light through small panes",
     "luz_c": "the same cool north light",
     "etnias": ["white American"]},
    {"id": "harlem", "familia": "harlem",
     "coz": "a Harlem brownstone kitchen with pressed tin ceiling and tall "
            "narrow windows",
     "coz_c": "the same brownstone kitchen",
     "sup_a": "a marble slab counter", "sup": "marble counter",
     "luz": "warm city light coming in high",
     "luz_c": "the same warm city light",
     "etnias": ["Black American"]},
    {"id": "atlanta", "familia": "atlanta",
     "coz": "an Atlanta kitchen with dark wood cabinets and a wide island",
     "coz_c": "the same Atlanta kitchen",
     "sup_a": "a granite island", "sup": "granite island",
     "luz": "bright filtered daylight from a back door",
     "luz_c": "the same bright filtered daylight",
     "etnias": ["Black American"]},
    {"id": "delta", "familia": "delta",
     "coz": "a Mississippi Delta kitchen with a chipped enamel stove and a "
            "hanging bare bulb",
     "coz_c": "the same Delta kitchen",
     "sup_a": "an oilcloth-covered table", "sup": "covered table",
     "luz": "low warm lamplight",
     "luz_c": "the same low warm lamplight",
     "etnias": ["Black American"]},
    {"id": "gullah", "familia": "gullah",
     "coz": "a Lowcountry kitchen with blue-washed boards and a window onto "
            "marsh grass",
     "coz_c": "the same Lowcountry kitchen",
     "sup_a": "a scrubbed plank counter", "sup": "plank counter",
     "luz": "soft coastal light off the water",
     "luz_c": "the same soft coastal light",
     "etnias": ["Black American"]},
    {"id": "noroeste", "familia": "noroeste",
     "coz": "a Pacific Northwest kitchen with cedar shelving and a window onto "
            "wet firs",
     "coz_c": "the same Northwest kitchen",
     "sup_a": "a slab fir counter", "sup": "fir counter",
     "luz": "dim green light through rain on the glass",
     "luz_c": "the same dim green light",
     "etnias": ["white American"]},
    {"id": "grandes_lagos", "familia": "grandes_lagos",
     "coz": "a Great Lakes kitchen with knotty pine panelling and a chest "
            "freezer humming",
     "coz_c": "the same Great Lakes kitchen",
     "sup_a": "a pine countertop", "sup": "pine countertop",
     "luz": "pale winter light off snow",
     "luz_c": "the same pale winter light",
     "etnias": ["white American"]},
    {"id": "creole", "familia": "creole",
     "coz": "a New Orleans kitchen with a tall shuttered window and a cast "
            "iron pot on the range",
     "coz_c": "the same New Orleans kitchen",
     "sup_a": "a worn zinc counter", "sup": "zinc counter",
     "luz": "heavy humid light through the shutters",
     "luz_c": "the same heavy humid light",
     "etnias": ["Black American"]},
    {"id": "amish", "familia": "amish",
     "coz": "a plain country kitchen with no appliances on the walls and a "
            "hand pump at the sink",
     "coz_c": "the same plain country kitchen",
     "sup_a": "a bare oak table", "sup": "oak table",
     "luz": "daylight only, no electric light",
     "luz_c": "the same daylight, no electric light",
     "etnias": ["white American"]},
    {"id": "italo_americana", "familia": "italo_americana",
     "coz": "an Italian-American kitchen with a tiled backsplash and braided "
            "garlic on a hook",
     "coz_c": "the same Italian-American kitchen",
     "sup_a": "a stainless counter", "sup": "stainless counter",
     "luz": "warm bulb light over the range",
     "luz_c": "the same warm bulb light",
     "etnias": ["white American"]},
    {"id": "americana", "familia": "americana",
     "coz": "a plain suburban American kitchen with oak cabinets and a fridge "
            "covered in magnets",
     "coz_c": "the same suburban kitchen",
     "sup_a": "a laminate counter", "sup": "laminate counter",
     "luz": "flat kitchen ceiling light",
     "luz_c": "the same flat ceiling light",
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
    {"id": "geoduck", "tipo": "molusco",
     "nome": "geoduck",
     "img": "a large geoduck clam, its long siphon neck hanging slack and "
            "folded down over her fingers",
     "antes": "the long siphon neck, hanging slack and folded down",
     "depois": "the same siphon neck has drawn up long and straight, standing "
               "clear of her hand, no thicker than before",
     "curto": "geoduck"},
    {"id": "peca", "tipo": "anatomia",
     "nome": "peça anatômica",
     "img": "a life-size anatomical cross-section model of the male pelvis in "
            "moulded plastic, the shaft lying folded down against the base",
     "antes": "the moulded shaft, lying folded down against the base",
     "depois": "the same moulded shaft has risen and extended straight out "
               "from the base, the same thickness as before",
     # ⛔⛔ ESTE CAMPO ENTRA NO TAKE EM INGLES — era "peça anatômica" e o
     # prompt saia com *"pours a thin steady stream over the peça anatômica"*.
     # O campo `nome` (que e' PT) serve ao painel e ao resumo; o `curto` serve
     # ao PROMPT, e sao coisas diferentes.
     "curto": "anatomical model"},
]

# ⚠️ A cena 3 pede o par GRANDE do prop — é o payoff, e ele tem de ser
# visivelmente maior que o do hook, na mesma espécie.
PROPS_GRANDES = {
    "geoduck": "a very large geoduck clam, its siphon neck drawn up long and "
               "straight above her fist",
    "peca": "the same anatomical cross-section model, the moulded shaft risen "
            "and extended straight out from the base",
}

# ⭐ A ALTERNATIVA, PRONTA PARA TROCA DE UMA LINHA. O operador escolheu o morph
# VISÍVEL ciente do risco; se o gerador recusar, esta constante põe a mudança
# escondida dentro do jato, que é a forma que passou no RESSURREICAO.
# ⛔ A VIRGULA DEPOIS DE %(antes)s NAO E' ENFEITE. O campo era uma ORACAO com
# verbo finito ("the moulded shaft LIES folded down...") encaixada num slot de
# sintagma nominal, e o prompt saia com dois verbos brigando: *"the moulded
# shaft lies folded down against the base changes on camera"*. Agora o campo
# `antes` e' sintagma nominal + participio, entre virgulas.
MORPH_VISIVEL = ("As the liquid runs over it, %(antes)s, changes on camera: "
                 "%(depois)s. The change happens in one continuous take, with "
                 "no cut.")
MORPH_OCULTO = ("The falling liquid covers it completely for a moment. When "
                "the stream moves on, %(depois)s. The change is never seen "
                "happening.")
MORPH = MORPH_VISIVEL


# ---------------------------------------------------------------------------
# ⭐⭐ A ISCA DESMENTIDA — o que ela despeja no prop
# ---------------------------------------------------------------------------
# ⚠️ Na fonte é vinagre de maçã. O pool mantém a forma: líquido de despensa que
# a internet promete e que o vídeo desmente na mesma respiração.
SUBSTANCIAS = [
    {"id": "vinagre", "nome": "apple cider vinegar", "fala": "apple cider vinegar"},
    {"id": "azeite", "nome": "olive oil", "fala": "olive oil"},
    {"id": "mel", "nome": "raw honey", "fala": "raw honey"},
    {"id": "limao", "nome": "lemon juice", "fala": "lemon juice"},
    {"id": "castor", "nome": "castor oil", "fala": "castor oil"},
    {"id": "alcool", "nome": "rubbing alcohol", "fala": "rubbing alcohol"},
    {"id": "coco", "nome": "coconut oil", "fala": "coconut oil"},
    {"id": "salmoura", "nome": "pickle brine", "fala": "pickle brine"},
]

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
    {"id": "liquidificador", "vaso": "a blender jug on its base",
     "acao": "drops the pieces into the blender jug", "curto": "blender"},
    {"id": "tigela_fouet", "vaso": "a wide ceramic bowl with a wire whisk in it",
     "acao": "whisks it in the ceramic bowl", "curto": "ceramic bowl"},
    {"id": "pilao", "vaso": "a heavy stone mortar with the pestle standing in it",
     "acao": "grinds it down in the stone mortar", "curto": "stone mortar"},
    {"id": "panela", "vaso": "a small enamel pan on a low flame",
     "acao": "stirs it in the enamel pan", "curto": "enamel pan"},
    {"id": "jarra", "vaso": "a stoneware pitcher with a long wooden spoon",
     "acao": "stirs it through the stoneware pitcher", "curto": "pitcher"},
    {"id": "peneira", "vaso": "a fine metal sieve resting over a steel bowl",
     "acao": "presses it through the sieve", "curto": "sieve"},
    {"id": "moedor", "vaso": "a hand-crank grinder clamped to the edge",
     "acao": "cranks it through the grinder", "curto": "grinder"},
    {"id": "coador", "vaso": "a wide crock with a square of cloth tied over it",
     "acao": "strains it through the cloth", "curto": "cloth strainer"},
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
    {"id": "cachos_longos", "idade": 27,
     "cabeca": "long dark curls falling past the shoulders",
     "marca": "a small dark mole just under her left eye",
     "corpo": "tall with a narrow waist"},
    {"id": "liso_platinado", "idade": 24,
     "cabeca": "sleek platinum hair cut blunt at the jaw",
     "marca": "a faint scar through one of her eyebrows",
     "corpo": "slim and long-limbed"},
    {"id": "rabo_alto", "idade": 26,
     "cabeca": "black hair pulled into a high sleek ponytail",
     "marca": "a small gap between her front teeth",
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
     "marca": "a thin scar at her hairline",
     "corpo": "long-legged and slight"},
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
ANTICELEB = ("not resembling any famous person, not a celebrity")

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
    # ⛔⛔ A VIRADA TERMINA NO ORGAO, e isso e' correcao de drifting.
    # O operador ditou "but combined with the secret I discovered will" e a
    # construcao dele esta preservada literalmente. Mas terminar ali reprova no
    # `medir_deiticos` familia C: nome ABSTRATO ("the secret") sem DESTINO —
    # sozinha no scroll, "it will" o QUE? Ele mesmo acabou de dizer que nao
    # aceita mais drifting, entao a frase ganha o destino que faltava sem
    # perder uma palavra da construcao dele.
    "Pouring {s} on your {o} won't bring it back overnight. "
    "But combined with the secret I found, your {o} comes back.",
    "Rubbing {s} on your {o} won't wake it up overnight. "
    "But combined with the secret I found, your {o} wakes up.",
    "{S} alone won't bring your {o} back overnight. "
    "But combined with the secret I found, your {o} answers again.",
    "Dripping {s} on your {o} does nothing overnight. "
    "But combined with the secret I found, your {o} comes back.",
    # ⛔ ERA "It won't." — reprovado na revisao adversarial de 2026-08-06. E' a
    # MESMA forma que ele reprovou no TROCA ("and I'll send it" — *enviar o
    # QUE??*): verbo elidido, objeto nenhum. Pior: o antecedente mais proximo
    # de "It" nao e' a substancia, e' o proprio orgao — dito uma palavra antes.
    # "That's a lie" fecha a sentenca sozinha e aponta para a CRENDICE.
    "They swear {s} fixes your {o} overnight. That's a lie. "
    "Combined with the secret I found, your {o} comes back.",
    "{S} on your {o} won't work overnight. "
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
    # ⛔ O literal e' "Comment gelatin," COM VIRGULA — ordem do operador de
    # 2026-08-02, depois de ver renders com a legenda "COMMENT HONEY": a
    # legenda do video sai do audio, e comando variavel faz o modelo
    # parafrasear a keyword. O `lint_cta_literal` cobra isso nos 18.
    # ⛔⛔ QUEM OMITE E' O MUNDO, NUNCA ELA — correcao da revisao adversarial de
    # 2026-08-06. Duas entradas diziam *"I'll send the piece I left out"*, e a
    # cena 2 diz, em 5 dos 6 templates, que quem deixa de fora e'
    # everyone/nobody/they. Eram 2.016 pares em que ela acusava o mundo de
    # omitir e uma respiracao depois assumia a omissao. A tensao nao vem de ela
    # ter escondido: vem de A RECEITA DO MUNDO estar furada e ela ter a peca.
    # ⚠️ E' tambem o enquadramento que o operador ditou — *"missing part da
    # receita sera entregue ao comentar gelatin"*: a peca falta NA RECEITA.
    "Comment gelatin, and I'll send you the missing part.",
    "Comment gelatin, and I'll send you what's missing.",
    "Comment gelatin, one word, and I'll send the missing part.",
    "Comment gelatin, and I'll send you the part nobody includes.",
    "Comment gelatin, and I'll send the missing piece tonight.",
    # ⛔ Era "the rest of the recipe" — isca válida, mas não nomeia A PARTE QUE
    # FALTA, que é o ângulo inteiro. O CTA tem de prometer exatamente o que a
    # cena 2 disse que ficou de fora, senão o vídeo abre um buraco e entrega
    # outra coisa.
    "Comment gelatin, and I'll send you the missing step.",
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
EIXOS_TRAVAVEIS = ["mundo", "etnia", "ref", "amiga", "prop", "substancia",
                   "metodo", "comum", "raro"]
EIXOS_UI = [
    ("mundo", "A REGIAO", "MUNDOS", "id"),
    ("etnia", "ETNIA", "etnias_do_mundo", None),
    ("ref", "QUEM FALA", "REFS", "cabeca"),
    ("amiga", "A AMIGA", "REFS", "cabeca"),
    ("prop", "O PROP", "PROPS", "nome"),
    ("substancia", "A ISCA", "SUBSTANCIAS", "nome"),
    ("metodo", "O PREPARO", "METODOS", "curto"),
    ("comum", "O COMUM", "COMUNS", "nome"),
    ("raro", "O RARO", "RAROS", "nome"),
]
CENAS_UI = ["1 · a isca desmentida", "2 · a receita com o buraco",
            "3 · o copo + CTA"]

TETO_LEDGER = {"familia_mundo": len(FAMILIAS_MUNDO), "prop": len(PROPS),
               "substancia": len(SUBSTANCIAS), "metodo": len(METODOS),
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

    prop = _por_id(PROPS, travas["prop"]) if travas.get("prop") else \
        _fresco(PROPS, usados.get("prop", []), rng, "id")
    sub = _fresco(SUBSTANCIAS, usados.get("substancia", []), rng, "id")
    met = _fresco(METODOS, usados.get("metodo", []), rng, "id")
    com = _fresco(COMUNS, usados.get("comum", []), rng, "id")
    raro = _fresco(RAROS, usados.get("raro", []), rng, "id")
    reacao = rng.choice(REACOES_AMIGA)
    if travas.get("bela"):
        tpl, _curto = sc.traje_bela(rng)
        traje = tpl % rng.choice(sc.CORES_BELAS) if "%s" in tpl else tpl
    else:
        traje = rng.choice(TRAJES_PADRAO)
    orgao = rng.choice(NUCLEO)

    falas = _montar_falas(rng, sub, orgao, com, raro)

    return {
        "pagina": pagina, "mundo": mundo, "etnia": et, "ref": ref,
        "amiga": amiga, "prop": prop, "substancia": sub, "metodo": met,
        "comum": com, "raro": raro, "reacao": reacao, "orgao": orgao,
        "bela": bool(travas.get("bela")), "falas": falas, "traje": traje,
        "bandeira": rng.random() < 0.5,
    }


def _montar_falas(rng, sub, orgao, com, raro):
    """As tres falas, cada uma cedendo ao teto ANTES de ser escolhida."""
    c1 = _escolher(
        rng, DESMENTIDOS,
        lambda t: _palavras(t.format(s=sub["fala"], S=sub["fala"].capitalize(),
                                     o=orgao)) <= TETO_FALA[1],
        tamanho=lambda t: _palavras(t.format(s=sub["fala"],
                                             S=sub["fala"].capitalize(),
                                             o=orgao))
    ).format(s=sub["fala"], S=sub["fala"].capitalize(), o=orgao)

    # ⛔ O RARO ENTRA EM MINUSCULA. Ele abria a frase e por isso era
    # capitalizado; desde que os templates ganharam verbo de preparo
    # ("Add {R}."), capitalizar produzia *"Add Maca root, that Andean root
    # from Peru."* — e a legenda queimada sai do audio, entao a maiuscula no
    # meio da frase vira erro visivel no video.
    c2 = _escolher(
        rng, RECEITAS,
        lambda t: (_palavras(t.format(R=raro["fala"], o=orgao)) <= TETO_FALA[2]
                   and not _colide(c1, t.format(R=raro["fala"], o=orgao), orgao)),
        tamanho=lambda t: _palavras(t.format(R=raro["fala"], o=orgao))
    ).format(R=raro["fala"], o=orgao)

    # ⛔⛔ O GUARDA DE ECO ENTRE CENAS — revisao adversarial de 2026-08-06.
    # As tres falas eram sorteadas cegas umas das outras, e em 17% dos pares a
    # cena 2 repetia literalmente o fecho da cena 1: *"your peck-er comes
    # back"* e depois *"the blood comes back to your peck-er"*; ou
    # "answers again" duas vezes em 24 segundos. O payoff perde forca quando
    # a segunda vez chega — e o CTA "the piece I left out" ecoava o "always
    # left out" da cena 2 na mesma respiracao.
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
    m, ref, prop = spec["mundo"], spec["ref"], spec["prop"]
    sub, met, com, raro = (spec["substancia"], spec["metodo"], spec["comum"],
                           spec["raro"])
    band = BANDEIRA if spec.get("bandeira") else ""

    v = {
        "coz": m["coz"], "coz_c": m["coz_c"], "sup_a": m["sup_a"],
        "sup": m["sup"], "luz": m["luz"], "luz_c": m["luz_c"],
        "pessoa": _pessoa(spec), "ancora": _ancora(spec),
        "amiga": _amiga(spec), "reacao": spec["reacao"],
        "traje": _traje(spec), "prop_img": prop["img"],
        "prop_grande": PROPS_GRANDES[prop["id"]], "prop_curto": prop["curto"],
        "sub": sub["nome"], "vaso": met["vaso"], "acao": met["acao"],
        "com_img": com["img"], "raro_img": raro["img"],
        # ⚠️ `.rstrip(".")` — os quatro blocos escrevem "%(anti)s." e o
        # ANTICELEB_BELA (compartilhado) ja' termina em ponto: saia
        # *"not resembling any famous person.."* nos quatro. Normalizar aqui e'
        # melhor que tirar o ponto do template, que os outros agentes usam sem
        # ponto proprio.
        "anti": (sc.ANTICELEB_BELA if spec.get("bela")
                 else ANTICELEB).rstrip("."),
        "cauda": CAUDA, "band": band,
        "morph": MORPH % {"antes": prop["antes"], "depois": prop["depois"]},
        "idade": ref["idade"], "etnia": spec["etnia"], "marca": ref["marca"],
        "cabeca": ref["cabeca"],
    }
    v["nao_toca"] = NAO_TOCA % m["sup"]

    b = {}
    b["BLOCO 0 (REF)"] = (
        "REF 01: Photo of a real person, a %(idade)d-year-old %(etnia)s woman, "
        "chest up, facing the camera directly, neutral steady expression with "
        "her mouth closed. %(cabeca)s and %(marca)s. Wearing %(traje)s. "
        "%(anti)s. Hands out of frame, no objects. Plain neutral gray "
        "background, soft even frontal light. %(cauda)s" % v)

    # --- CENA 1 — A ISCA DESMENTIDA -----------------------------------------
    # ⛔ O prop nasce MURCHO e muda em cena. O despejo cai SOBRE ele, nunca no
    # copo: e' o objeto que desmente a crendice, e por isso ele tem de estar
    # na lente, na altura do peito, antes de qualquer coisa acontecer.
    b["IMAGE 01/03"] = (
        "IMAGE 01/03: Medium shot in %(coz)s, %(luz)s. Standing behind "
        "%(sup_a)s is %(pessoa)s, wearing %(traje)s. She looks straight into "
        "the lens. Held out towards the camera in her left hand, at chest "
        "height: %(prop_img)s. In her right hand, tipped over it, a plain "
        "unlabelled bottle of %(sub)s. Beside her stands %(amiga)s, wearing "
        "%(traje)s, %(reacao)s — she never looks at the lens. They are the "
        "only two people in the frame. %(nao_toca)s%(band)s %(anti)s. "
        "%(cauda)s" % v)

    b["TAKE 01/03"] = (
        "TAKE 01/03: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway. The camera does not move and there is no "
        "cut. She keeps talking to the lens and never lowers her left hand. "
        "The bottle in her right hand pours a thin steady stream over the "
        "%(prop_curto)s the whole time. %(morph)s The second woman does not "
        "speak, does not move her feet, and keeps her eyes on the "
        "%(prop_curto)s. Only she speaks. No on-screen text, no subtitles, no "
        "captions, no watermark." % v)

    # --- CENA 2 — A RECEITA COM O BURACO ------------------------------------
    # ⛔ O RARO E O COMUM ESTAO EM QUADRO, mas o gelatin trick NAO. E' o
    # angulo inteiro: a bancada mostra a receita, e a peca que falta so'
    # existe na fala. Mostrar gelatina aqui entregaria de graca o que o CTA
    # vende.
    b["IMAGE 02/03"] = (
        "IMAGE 02/03: Medium shot in %(coz_c)s, %(luz_c)s. %(Ancora)s, wearing "
        # ⛔ ERA "never touched and never mentioned". A segunda metade
        # CONTRADIZ A FALA: a cena 2 nomeia o raro em voz alta, por ordem do
        # operador — e' o eixo dele. A primeira metade era redundante: o
        # %(nao_toca)s logo abaixo ja' cobre a bancada inteira. Achado da
        # revisao adversarial de 2026-08-06.
        "%(traje)s, stands at %(sup_a)s with %(vaso)s in front of her. Laid "
        "out on the surface beside it: "
        "%(com_img)s and %(raro_img)s. She is the only person in the frame. "
        "Shot from chest height, straight on. %(nao_toca)s%(band)s %(anti)s. "
        "%(cauda)s" % dict(v, Ancora=_ancora(spec)[0].upper() + _ancora(spec)[1:]))

    b["TAKE 02/03"] = (
        "TAKE 02/03: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway, no cuts, and the camera does not move. She "
        "talks straight into the lens while she %(acao)s, one continuous "
        "movement, and never stops looking at the camera. Nothing else on the "
        "surface is picked up. She is the only person who appears. No "
        "on-screen text, no subtitles, no captions, no watermark." % v)

    # --- CENA 3 — AS DUAS, O PROP GRANDE E O COPO ---------------------------
    # ⛔ ORDEM DO OPERADOR: uma segura o prop GRANDE, ja' ereto; a outra segura
    # o copo. E' o payoff em dois objetos, e o contraste com o prop murcho da
    # cena 1 e' a prova visual do mecanismo.
    b["IMAGE 03/03"] = (
        "IMAGE 03/03: Closer medium shot in %(coz_c)s, %(luz_c)s, framed from "
        "the waist up. %(Ancora)s, wearing %(traje)s, stands frame-right "
        "holding a tall glass filled to the top with a thick pale drink, a "
        "single paper straw standing in it. Frame-left, %(amiga)s, wearing "
        "%(traje)s, holds %(prop_grande)s upright in both fists at chest "
        "height. They are the only two people in the frame.%(band)s %(anti)s. "
        "%(cauda)s" % dict(v, Ancora=_ancora(spec)[0].upper() + _ancora(spec)[1:]))

    b["TAKE 03/03"] = (
        "TAKE 03/03: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway, no cuts, and the camera does not move. She "
        "holds the glass steady at chest height the whole time and never sets "
        "it down. The second woman holds the %(prop_curto)s completely still, "
        "keeps her eyes on it, and never speaks. Only she speaks, straight "
        "into the lens. No on-screen text, no subtitles, no captions, no "
        "watermark." % v)

    return b


# ---------------------------------------------------------------------------
# LINTER — as regras deste ângulo
# ---------------------------------------------------------------------------
_HOMEM = re.compile(r"\b(a|the|his|one)\s+(?:\w+\s+){0,3}(man|men|husband|"
                    r"boyfriend|guy)\b", re.I)


def _fa_sem_homem(spec, blocos, achados):
    """FA1 — ⛔ NENHUM HOMEM EM CENA. Ordem do operador na entrevista: a fonte
    tem um homem cozinhando ao fundo e ele SAI. São as duas mulheres nas três
    cenas, e um terceiro corpo em quadro muda a leitura do vídeo inteiro."""
    for nome, txt in sorted(blocos.items()):
        if _HOMEM.search(txt):
            achados.append(("ERRO", "FA1: %s traz um homem em cena — este "
                                    "ângulo é só as duas mulheres" % nome))


def _fa_prop(spec, blocos, achados):
    """FA2 — o prop SORTEADO está na cena 1, e a versão grande na cena 3.

    ⚠️ Mede o prop do `spec`, nunca uma constante: quando o prop virou eixo, um
    linter que olhasse string fixa acusaria metade dos sorteios. Foi o que
    aconteceu com o copo do BOTICA no mesmo dia."""
    if spec["prop"]["img"] not in blocos["IMAGE 01/03"]:
        achados.append(("ERRO", "FA2: IMAGE 01/03 sem o prop sorteado (%s)"
                        % spec["prop"]["id"]))
    if PROPS_GRANDES[spec["prop"]["id"]] not in blocos["IMAGE 03/03"]:
        achados.append(("ERRO", "FA2: IMAGE 03/03 sem a versão grande do prop "
                                "— o contraste com o murcho é a prova visual"))


def _fa_morph(spec, blocos, achados):
    """FA3 — a mudança do prop está no TAKE 01, e ela ALONGA sem engrossar.

    ⛔⛔ A escala é DIFERENCIAL. Medido em pixels na fonte do RESSURREICAO:
    altura 2,31× contra largura 1,44×. Se a descrição disser que o objeto fica
    MAIOR, lê como tumescência e o gerador recusa — foi assim que caiu um
    vídeo nosso na política de conteúdo nocivo."""
    t1 = blocos["TAKE 01/03"]
    if spec["prop"]["depois"] not in t1:
        achados.append(("ERRO", "FA3: TAKE 01/03 sem a mudança do prop — o "
                                "despejo sem morph é só um líquido caindo"))
    # ⛔ NEGAÇÃO NÃO CONTA. A primeira versão acusava `no thicker than before` —
    # a frase que EXISTE justamente para impedir o inchaço. A lente reprovava o
    # texto que CUMPRE a regra, em 418 de 800 sorteios. Suspeitar da lente antes
    # do código é a lição que mais se repetiu esta semana.
    _cresce = re.sub(r"\b(no|not|never|same)\s+\w+", " ", t1, flags=re.I)
    if re.search(r"\b(bigger|larger|swell\w*|thicker|grows|expands)\b",
                 _cresce, re.I):
        achados.append(("ERRO", "FA3: TAKE 01/03 descreve o prop ficando MAIOR "
                                "— a escala é diferencial (alonga, não incha); "
                                "'maior' lê como tumescência e derruba o vídeo"))


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
    if not re.search(r"\bmissing\b|\bpiece\b|\bpart\b", f3, re.I):
        achados.append(("ERRO", "FA4: o CTA não nomeia a parte que falta — é "
                                "exatamente o que ele promete entregar"))


def _fa_raro(spec, blocos, achados):
    """FA5 — o raro entra na fala com nome popular + aposto, nunca científico."""
    if spec["raro"]["fala"] not in spec["falas"][1]:
        achados.append(("ERRO", "FA5: a cena 2 não traz o raro sorteado com o "
                                "aposto (%s)" % spec["raro"]["id"]))


def _fa_duas(spec, blocos, achados):
    """FA6 — duas mulheres nas cenas 1 e 3, UMA na cena 2.

    ⚠️ A cena 2 é o preparo e ela está sozinha: a amiga voltando ali tiraria o
    foco da bancada, que é onde a receita se prova."""
    for nome in ("IMAGE 01/03", "IMAGE 03/03"):
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


def _fa_morph_gramatical(spec, blocos, achados):
    """FA10 — o morph e' a cena inteira; e o estado ANTES e' SINTAGMA NOMINAL.

    ⛔⛔ ESTA LENTE JA' NASCEU CEGA UMA VEZ, na mesma hora em que foi escrita.
    A primeira versao checava se a string montada continha
    `"%s, changes on camera" % antes` — ou seja, checava a VIRGULA. Reinjetei o
    defeito original (`antes` = "the moulded shaft lies folded down") e ela
    PASSOU, porque a virgula continuava no lugar: o prompt saia agramatical e a
    lente dizia limpo. Ela media a FORMA do encaixe, nunca a NATUREZA do que
    encaixou. Agora mede o campo."""
    antes, depois = spec["prop"]["antes"], spec["prop"]["depois"]
    m = _VERBO_FINITO.search(antes)
    if m:
        achados.append(("ERRO", "FA10: o estado ANTES do prop %r conjuga "
                                "(%r) — ele entra como SUJEITO de 'changes on "
                                "camera' e o prompt fica com dois verbos"
                        % (spec["prop"]["id"], m.group(0))))
    t = blocos["TAKE 01/03"]
    if MORPH is MORPH_VISIVEL:
        if ("%s, changes on camera" % antes) not in t:
            achados.append(("ERRO", "FA10: o morph nao encaixa o estado ANTES "
                                    "entre virgulas"))
        if depois not in t.split("changes on camera:", 1)[-1]:
            achados.append(("ERRO", "FA10: o estado DEPOIS nao vem apos os "
                                    "dois-pontos do morph"))
    elif depois not in t:
        achados.append(("ERRO", "FA10: morph oculto sem o estado DEPOIS"))


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
    orgaos = [o.lower() for o in NUCLEO]
    alvos = [(1, orgaos), (3, orgaos + ["gelatin", "missing", "piece", "part"])]
    for i, termos in alvos:
        sents = _sentencas(falas[i - 1])
        if not sents:
            continue
        if not any(t in sents[0].lower() for t in termos):
            ach.append(("ERRO", "FA9: a abertura da cena %d nao nomeia o "
                                "referente — %r deixa o espectador perguntando "
                                "do que se trata" % (i, sents[0][:46])))

    for extra in (_fa_sem_homem, _fa_prop, _fa_morph, _fa_buraco, _fa_raro,
                  _fa_duas, _fa_bloco_limpo, _fa_morph_gramatical):
        extra(spec, blocos, ach)
    return ach


def resumo_pt(spec):
    m, r, p = spec["mundo"], spec["ref"], spec["prop"]
    return ("Mulher %s de %d anos, em %s. Cena 1: despeja %s sobre %s na lente, "
            "com uma amiga ao lado, e ele muda em cena. Cena 2: %s com %s e %s, "
            "e a peça que falta só é dita. Cena 3: as duas — uma com %s grande "
            "e ereto, a outra com o copo. Três cenas de 8s."
            % (spec["etnia"], r["idade"], m["familia"], spec["substancia"]["nome"],
               # o resumo e' PT: usa "nome". O campo "curto" agora e' o termo
               # INGLES que vai para o prompt, e aqui ele nao pode aparecer.
               p["nome"], spec["metodo"]["curto"], spec["comum"]["nome"],
               spec["raro"]["nome"], p["nome"]))


def nova_fala(spec, cena, rng):
    """Re-sorteia UMA fala sem mexer nas outras — o botão `trocar` da copy."""
    novas = _montar_falas(rng, spec["substancia"], spec["orgao"],
                          spec["comum"], spec["raro"])
    return novas[cena - 1]
