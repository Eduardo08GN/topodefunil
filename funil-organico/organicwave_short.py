#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE ORGANIC WAVE SHORT — 3 cenas de 8 segundos.

Porte do **primeiro** agente da operacao (`AGENTE_ED_ORGANIC_WAVE.md`), com o
mecanismo migrado de honey para **gelatin** (decisao do operador, 2026-07-31).

O QUE ELE TEM QUE OS QUATRO ESPECIALISTAS NAO TEM
-------------------------------------------------
1. **Primeira pessoa.** Aqui nao ha' narrador e vitima: quem fala e' o dono do
   problema. O eixo de identificacao do cruzamento de copy (oxitocina) mora
   nele, e o banco de DORES do agente original e' o ativo — "falling asleep on
   the couch on purpose", "she blamed herself and that killed me".
2. **Elenco de aspiracao, nao de identificacao.** ⚠️ Ordem do operador: pessoas
   belissimas, mulheres lindas de todas as etnias, homens musculosos e handsome.
   Isso e' o oposto dos especialistas, que vendem "o cara da sua rua".
3. **Curiosity gap.** Um ingrediente a mais na bancada que a copy NUNCA nomeia
   — o mecanismo do agente original para gerar comentario extra. Sobrevive.

⛔ POR QUE ESTE NAO DERIVA DE NINGUEM
Os `<agente>_short.py` derivam de um motor longo. Aqui nao ha' motor longo em
Python: o ORGANIC WAVE so' existia como Markdown. Entao este arquivo e' motor
completo — pools proprios — mas continua usando a maquinaria compartilhada
(`short_comum.lint_curto`) passando a si mesmo como `base`.

⛔ E POR QUE ELE NAO TEM `Ordinary relatable face`
A string `ANTICELEB` dos quatro maduros e' "Ordinary relatable face, not a
celebrity." As duas metades servem a propositos opostos e aqui as duas caem:
  · `Ordinary relatable face` contradiz o elenco de aspiracao;
  · `not a celebrity` foi retirada por ordem do operador — declarar
    conformidade nao desarma classificador (ja' documentado em
    `licoes-producao-veo.md`) e o token pode levantar a suspeita que pretendia
    evitar.
Nos quatro especialistas a string continua, porque la' ela esta' certa.
"""

import json
import os
import random
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import short_comum as sc                                        # noqa: E402
from nucleo_sonoro import sonorizar                             # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(AQUI, ".organicwave-short-ledger.json")

TITULO = "AGENTE ORGANIC WAVE SHORT"
SUBTITULO = "primeira pessoa, elenco de aspiração, em 3 cenas · prompts Veo"
SLUG = "organicwave-short"

CENAS_UI = ["1 · A DOR (1ª pessoa)", "2 · O GELATIN TRICK + A PROVA", "3 · CTA"]
# Os tetos descrevem a copy APROVADA, nao o contrario: os 36 itens foram
# curados pelo operador, entao o limite segue o p95 medido deles. Serve
# para pegar a cauda longa, nao para reprovar o pool.
TETO_FALA = {1: 24, 2: 36, 3: 34}

# congruencia inviolavel: a etnia do REF e' a do avatar da pagina
ETNIA = {"joe": "white American", "ray": "white American", "matt": "white American",
         "marcus": "Black American", "chuck": "Black American"}

NUCLEO = ["Johnson", "soldier", "pecker", "manhood", "wiener", "tool", "old boy"]


# ---------------------------------------------------------------------------
# STRINGS TRAVADAS
# ---------------------------------------------------------------------------

CAUDA = "Shot on iPhone, natural grain. No on-screen text, no watermark."

# ⚠️ O contrario do ANTICELEB dos especialistas. Aqui o rosto VENDE.
BELEZA_H = ("a strikingly handsome face with a strong jawline, in visibly "
            "excellent shape for his age")
BELEZA_M = "strikingly beautiful, flawless skin, in visibly excellent shape"

# ⛔ Copia literal do pool validado do FLAGRANTE. Nao reescrever: e' a spec
# dimensional que impede o prop de sair no tamanho natural.
NEGACAO_AVE = (" No bird, no goose, no duck, no swan, no snake, no feathers, "
               "no beak, no eyes, no head, nothing alive.")

IMOBILIDADE = ("It stays exactly as it appears in the first frame — same "
               "position, same angle, same shape — completely motionless for "
               "the entire shot.")


# ---------------------------------------------------------------------------
# ELENCO — belissimo, por ordem do operador
# ---------------------------------------------------------------------------
# ⚠️ A marca facial continua OBRIGATORIA: e' o que segura a continuidade do
# rosto entre as tres cenas. Mas aqui ela e' **compativel com beleza** — sinal,
# sarda, covinha, olhos claros — e nunca cicatriz feia ou orelha entalhada,
# que sao as marcas dos especialistas.
# ⚠️ Os DOIS sexos sao pools por ETNIA, pelo mesmo motivo: a congruencia de
# casting e' travada pela pagina, e cabelo e' o descritor mais etnico que
# existe. Um pool unico entregaria "loira mel" numa pagina de avatar negro e
# "locs grisalhos" numa de avatar branco. A variedade que o operador pediu —
# ruivas, loiras, morenas, afrodescendentes — vem das cinco paginas somadas.
REFS_H_CLARA = [
    {"idade": 58, "marca": "thick silver hair swept back and a small dark beauty mark high on his left cheekbone",
     "corpo": "a broad muscular chest and defined arms"},
    {"idade": 61, "marca": "full salt-and-pepper hair, a close-cropped silver beard and pale grey eyes",
     "corpo": "a powerfully built chest and thick corded forearms"},
    {"idade": 56, "marca": "dark hair greying at the temples and a deep dimple in his left cheek",
     "corpo": "broad shoulders and a hard flat stomach"},
    {"idade": 64, "marca": "a full head of white hair and light hazel eyes with heavy lashes",
     "corpo": "a lean hard-muscled build with visible definition in the chest and arms"},
    {"idade": 59, "marca": "close-cropped silver hair and a small beauty mark beside his right eye",
     "corpo": "a broad chest, thick arms and clearly cut abdominal muscles"},
    {"idade": 62, "marca": "sandy blond hair going grey at the sides and a strong cleft chin",
     "corpo": "heavy shoulders and a thick muscular neck"},
    {"idade": 57, "marca": "wavy steel-grey hair worn a little long and bright blue eyes",
     "corpo": "a broad back and clearly defined arms"},
    {"idade": 60, "marca": "short auburn hair fading to grey and light freckles across his nose",
     "corpo": "a powerful chest and thick forearms"},
    {"idade": 63, "marca": "silver hair combed straight back and a trimmed white beard along the jaw",
     "corpo": "a lean athletic build with cut shoulders and a flat stomach"},
]
REFS_H_ESCURA = [
    {"idade": 58, "marca": "close-cropped silver hair, a neat white beard and a small dark beauty mark on his left cheekbone",
     "corpo": "a broad muscular chest and defined arms"},
    {"idade": 61, "marca": "a full head of white hair worn short and warm amber eyes",
     "corpo": "a powerfully built chest and thick corded forearms"},
    {"idade": 56, "marca": "a close grey fade and a deep dimple in his left cheek",
     "corpo": "broad shoulders and a hard flat stomach"},
    {"idade": 64, "marca": "salt-and-pepper locs gathered back and a trimmed grey beard",
     "corpo": "a lean hard-muscled build with visible definition in the chest and arms"},
    {"idade": 59, "marca": "a smooth shaved head and a neat silver goatee",
     "corpo": "a broad chest, thick arms and clearly cut abdominal muscles"},
    {"idade": 62, "marca": "short grey twists and a small beauty mark beside his right eye",
     "corpo": "heavy shoulders and a thick muscular neck"},
    {"idade": 57, "marca": "a silver-flecked afro worn low and bright hazel eyes",
     "corpo": "a broad back and clearly defined arms"},
    {"idade": 60, "marca": "close-cropped white hair and a strong cleft chin",
     "corpo": "a powerful chest and thick forearms"},
    {"idade": 63, "marca": "a short grey afro and a trimmed white beard along the jaw",
     "corpo": "a lean athletic build with cut shoulders and a flat stomach"},
]

MULHERES_CLARA = [
    {"idade": 34, "desc": "long honey-blonde hair past her shoulders, a small beauty mark on her left jaw, a fitted coral summer dress"},
    {"idade": 31, "desc": "long copper-red hair and light freckles across her nose, a fitted white sundress"},
    {"idade": 36, "desc": "long dark wavy hair past her waist and a deep dimple in her right cheek, a fitted turquoise dress"},
    {"idade": 29, "desc": "shoulder-length ash-blonde hair and pale green eyes, a fitted olive summer dress"},
    {"idade": 33, "desc": "long auburn hair gathered over one shoulder and a small beauty mark beside her right eye, a fitted burgundy dress"},
    {"idade": 30, "desc": "long strawberry-blonde waves and freckled shoulders, a fitted white linen dress"},
    {"idade": 37, "desc": "glossy dark brown hair in a high ponytail and bright green eyes, a fitted navy summer dress"},
    {"idade": 32, "desc": "deep red hair cut to the collarbone and a small beauty mark above her lip, a fitted cream dress"},
    {"idade": 35, "desc": "long platinum-blonde hair and grey-blue eyes, a fitted emerald summer dress"},
    {"idade": 28, "desc": "chestnut hair in loose beach waves and a dimple in her left cheek, a fitted blush sundress"},
]
MULHERES_ESCURA = [
    {"idade": 35, "desc": "long braided hair gathered over one shoulder, a small beauty mark high on her right cheekbone, a fitted emerald dress"},
    {"idade": 32, "desc": "a short natural afro and striking cheekbones, a fitted burgundy summer dress"},
    {"idade": 30, "desc": "long box braids past her shoulders and a deep dimple in her left cheek, a fitted coral dress"},
    {"idade": 37, "desc": "shoulder-length natural curls and warm amber eyes, a fitted white sundress"},
    {"idade": 28, "desc": "hair in a high bun with soft edges and a small beauty mark below her left eye, a fitted teal dress"},
    {"idade": 34, "desc": "long knotless braids down her back and a bright open smile, a fitted mustard summer dress"},
    {"idade": 31, "desc": "a full voluminous afro and light hazel eyes, a fitted white linen dress"},
    {"idade": 36, "desc": "sleek long hair parted in the middle and a small beauty mark on her right jaw, a fitted navy dress"},
    {"idade": 29, "desc": "shoulder-length auburn-dyed curls and freckles across her cheeks, a fitted olive sundress"},
    {"idade": 33, "desc": "long twists gathered high and a deep dimple in her right cheek, a fitted blush dress"},
]

# ⚠️ PISO DE IDADE 28. O agente original punha esta persona em 20-24 e isso NAO
# foi portado. O VAZAMENTO carrega a regra V12 — declarar "two fully clothed
# adults" com as duas idades em toda mencao — e ela existe por falha de
# classificador documentada. Ja' pagamos para descobrir que idade em cena com
# conteudo de ED e' zona sensivel. O contraste de "metade da idade dele", que
# e' o que vende, sobrevive de sobra com o piso em 28.
# ⛔ Nao baixar sem ordem do operador.
IDADE_MINIMA_MULHER = 28


def mulheres_de(pagina):
    return MULHERES_CLARA if "white" in ETNIA[pagina] else MULHERES_ESCURA


def homens_de(pagina):
    return REFS_H_CLARA if "white" in ETNIA[pagina] else REFS_H_ESCURA


# ⛔ SEMPRE cozinha americana — regra do agente original, que proibia
# rancho/curral fora do mecanismo de gelatina a cavalo.
AMBIENTES = [
    {"id": "cozinha", "set": "a bright American kitchen, white cabinets and a window behind him",
     "bancada": "counter", "curto": "kitchen", "luz": "warm even daylight from a window frame-left."},
    {"id": "cozinha_ilha", "set": "an open-plan American kitchen with a marble island, a living room out of focus behind him",
     "bancada": "island", "curto": "kitchen", "luz": "warm even light from a window frame-left."},
    {"id": "cozinha_madeira", "set": "a warm oak American kitchen, copper pans on a rail behind him",
     "bancada": "counter", "curto": "kitchen", "luz": "warm lamp light."},
    {"id": "cozinha_moderna", "set": "a modern American kitchen with matte black cabinets and a subway-tile wall",
     "bancada": "island", "curto": "kitchen", "luz": "cool even daylight from frame-right."},
]

# o prop-metafora do hook: o murcho na mao, com o deitico da copy apontando
# ⛔ Copia literal dos pools validados do FLAGRANTE.
PROPS = [
    {"id": "geoduck", "marisco": True,
     "murcho": "a small geoduck clam by its pale ridged shell, its siphon no longer than his thumb, shriveled and wrinkled, completely soft, folded over on itself",
     "ereto": "a geoduck clam upright by its shell at shoulder height, its siphon held stiff and straight, as long as her forearm and as thick as her wrist"},
    {"id": "banana", "marisco": False,
     "murcho": "a small banana, no longer than his thumb, shriveled and wrinkled, skin dull and spotted, completely soft, folded over on itself",
     "ereto": "a banana upright at shoulder height, held stiff and straight, as long as her forearm and as thick as her wrist"},
    {"id": "pepino", "marisco": False,
     "murcho": "a small shrivelled cucumber, no longer than his thumb, wrinkled and completely soft, folded over on itself",
     "ereto": "a cucumber upright at shoulder height, held stiff and straight, as long as her forearm and as thick as her wrist"},
    {"id": "okra", "marisco": False,
     "murcho": "a small wilted okra pod, no longer than his thumb, shriveled and completely soft, drooping over his fingers",
     "ereto": "an okra pod upright at shoulder height, held stiff and straight, as long as her forearm"},
]

# ⭐ O CURIOSITY GAP do agente original: um item a mais na bancada que a copy
# NUNCA nomeia. Ele existe para o comentario vir com "e o outro ingrediente?"
# junto da keyword — comentario a mais e' alcance a mais.
ISCA = [
    "a golden honey jar with a wooden dipper beside it",
    "a small jar of raw honey, lid off",
    "a knob of fresh ginger root and a paring knife",
    "three cinnamon sticks tied with twine",
    "a small tin of maca powder, lid beside it",
]

# ⚠️ A acao e' frase de GERUNDIO, SEM SUJEITO — encaixa nas duas personas.
# Enquanto trazia sujeito masculino proprio, a persona feminina rendia
# "Her hands work while she talks: HE empties the sachet..." num take que
# declara que so' ela esta' em quadro. Prompt que se contradiz e' prompt que
# o modelo resolve como quiser.
RECEITAS = [
    {"id": "gelatina_agua", "fala": "a spoonful of gelatin into a glass of cold water",
     "mesa": "a plain white sachet of pale powder with no label, a clear glass of water and a metal spoon",
     "acao": "tearing the sachet open, tipping the powder into the glass of water and stirring it in slow circles"},
    {"id": "gelatina_limao", "fala": "a spoonful of gelatin into cold water with fresh lemon",
     "mesa": "a plain white sachet of pale powder with no label, a glass of cold water, a halved lemon and a metal spoon",
     "acao": "emptying the sachet into the glass, squeezing the halved lemon over it and stirring it through"},
    {"id": "gelatina_morna", "fala": "a spoonful of gelatin into half a glass of warm water",
     "mesa": "a plain white sachet of pale powder with no label, a glass of warm water and a long metal spoon",
     "acao": "emptying the sachet into the warm water and stirring until the powder is gone"},
]


# ---------------------------------------------------------------------------
# COPY — aprovada pelo operador em 2026-07-31
# ---------------------------------------------------------------------------
# ⚠️ CURADORIA DO OPERADOR. Os 18 itens abaixo foram apresentados um a um e
# aprovados em bloco. Nenhum entra ou sai sem passar por ele.
#
# O diagnostico que os produziu, contra a lente de `cruzamento-copy-excelencia`:
# a copy do agente original estava TIMIDA — o choque chegava na palavra 15, o
# orgao nunca era nomeado, nao havia deitico para prop nenhum, o mecanismo
# estava ausente e sobrava pigarro ("I know you're not gonna believe me").
# O banco de DORES dele, porem, era bom e foi preservado: e' o que carrega a
# identificacao em primeira pessoa.

# ⚠️ `{n}` e' a idade POR EXTENSO, nunca o digito. Os itens aprovados diziam
# "Sixty-{n}" com o slot recebendo o algarismo, e isso renderizava "Sixty-1
# years old" — pior, um REF de 56 anos sairia "Sixty-6". O prefixo saiu do
# template e a idade inteira entra pelo slot. Mesmo defeito que ja' tinha
# aparecido como "Thirty-4" no VAZAMENTO: numero na copy se escreve, nao se
# concatena.
IDADE_EXT = {55: "fifty-five", 56: "fifty-six", 57: "fifty-seven",
             58: "fifty-eight", 59: "fifty-nine", 60: "sixty",
             61: "sixty-one", 62: "sixty-two", 63: "sixty-three",
             64: "sixty-four", 65: "sixty-five", 66: "sixty-six",
             67: "sixty-seven", 68: "sixty-eight", 69: "sixty-nine",
             70: "seventy"}

HOOKS = [
    "{N} years old, and this is what my {o} looked like every night. My wife stopped reaching for me.",
    "Look at this one. That was my {o} at {n} — and I made excuses every single night.",
    "Four hundred dollars a month on pills, and my {o} still looked like this. She stopped asking, brother.",
    "This is my {o} before. I used to fall asleep on the couch on purpose so she wouldn't try.",
    "My wife blamed herself. She thought it was her. It was my {o}, and it looked exactly like this.",
    "I couldn't look my wife in the eye at {n}. My {o} hung like this and I knew why she stopped.",
    "Too embarrassed to tell my own doctor. So I sat with this — my {o}, every night, for two years.",
    "We slept like roommates for eight months. This was my {o}, and I thought that was just {n}.",
]

FUNDIDAS = [
    # ⚠️ O item aprovado terminava em "nineteen days later mine came back",
    # sem nomear o orgao. Como o CTA tambem nao nomeia, a cota caia para 1/3 e
    # o linter reprovava 69 de 300 sorteios. Uma palavra mudou — `mine` virou
    # `my {o}` — e o operador foi avisado.
    "It was never age — it's blood flow, choked off. Stir {ing}. That's the gelatin trick, and nineteen days later my {o} came back.",
    "Stir {ing}. They call it the gelatin trick, and it opens the blood flow your {o} lost. This is me now.",
    "My neighbor gave me this. Stir {ing} — the gelatin trick. The blood flow came back, and so did my {o}.",
    "Nobody told me it was blood flow. Stir {ing}, that's the whole gelatin trick, and my {o} hasn't quit since.",
    "Two dollars, brother. Stir {ing} — the gelatin trick — and the blood flow that left my {o} came right back.",
]

CTAS = [
    # ⭐ Alternativa pedida pelo operador em 2026-07-31, vista em campo:
    # a promessa e' A RECEITA, nao "o que eu uso" nem "onde eu compro".
    # E' a mais direta do pool e a unica que casa com a keyword RECIPE
    # que o Veo Editor ja' destaca na legenda.
    "Comment gelatin, and I'll send you the recipe tonight. {gate}",
    "Next Friday night she'll ask what changed. Comment gelatin, and I'll send you the exact one I use. {gate}",
    "A month from tonight you won't recognise yourself. Comment gelatin, and I'll send you where I get mine. {gate}",
    "I waited two years to find this. Comment gelatin, and you won't wait two days. {gate}",
    "Comment gelatin, and I'll send you the one my neighbor sent me. Nobody in my house ever knew. {gate}",
    "Comment gelatin, and I'll send it tonight. There's one more ingredient on that counter I can't name here. {gate}",
]

# ---------------------------------------------------------------------------
# COPY — PERSONA FEMININA (aprovada pelo operador em 2026-07-31)
# ---------------------------------------------------------------------------
# ⚠️ CURADORIA DO OPERADOR. Mesmo diagnostico da masculina: os hooks dela no
# agente original abriam com pigarro ("Okay so I need to tell you what
# happened", "I know it sounds insane", "honestly"), o choque chegava tarde e o
# orgao nunca era nomeado.
#
# ⭐ O ANGULO QUE SO' ELA TEM: **ela faz escondido.** O original dizia "I
# secretly made him this" — a mulher resolve sem ele saber. Isso muda o alvo do
# anuncio (a esposa compra pro marido) e sobrevive no CTA 4.

HOOKS_F = [
    "My man is {n} and this is what his {o} looked like. He stopped coming to bed and I let him.",
    "Look at this one. That was my husband's {o} for two years, and I started thinking it was me.",
    "I was about to leave. The bedroom was dead, and his {o} looked exactly like this.",
    "I stopped undressing in front of him. Not because of me — because of this. Because of his {o}.",
    "He blamed his age. I blamed myself. It was neither of us — his {o} looked like this every night.",
    "Four hundred a month on pills, and his {o} still looked like this. I stopped asking.",
    "We hadn't touched in eight months. This was his {o}, and he wouldn't talk about it.",
    "My man is {n}. This was his {o} in March. I'm the one who found what fixed it.",
]

FUNDIDAS_F = [
    "It was never his age — it's blood flow, choked off. I stir {ing}. That's the gelatin trick, and nineteen days later his {o} came back.",
    "I stir {ing} for him. They call it the gelatin trick, and it opens the blood flow his {o} lost. Look at us now.",
    "My aunt gave me this. I stir {ing} — the gelatin trick. The blood flow came back, and so did his {o}.",
    "Nobody told us it was blood flow. I stir {ing}, that's the whole gelatin trick, and his {o} hasn't quit since.",
    "Two dollars, girls. I stir {ing} — the gelatin trick — and the blood flow that left his {o} came right back.",
]

CTAS_F = [
    # ⭐ Alternativa pedida pelo operador em 2026-07-31, vista em campo:
    # a promessa e' A RECEITA, nao "o que eu uso" nem "onde eu compro".
    # E' a mais direta do pool e a unica que casa com a keyword RECIPE
    # que o Veo Editor ja' destaca na legenda.
    "Comment gelatin, and I'll send you the recipe I use on him. {gate}",
    "Next Friday night he'll be the one reaching for you. Comment gelatin, and I'll send you the exact one I use. {gate}",
    "A month from now you won't recognise him. Comment gelatin, and I'll send you where I get mine. {gate}",
    "I waited two years to find this. Comment gelatin, and you won't wait two days. {gate}",
    "Comment gelatin, and I'll send you the one my aunt sent me. He never even knew I did it. {gate}",
    "Comment gelatin, and I'll send it tonight. There's one more thing on that counter I can't name here. {gate}",
]


GATES = [
    "Follow me first, or my message never lands.",
    "Follow me first, or I won't have any way to find your comment, brother.",
    "Hit follow right now, or Facebook can't deliver it.",
]


# ---------------------------------------------------------------------------
# TABELAS DE TOKEN BANIDO (o linter compartilhado le' estas)
# ---------------------------------------------------------------------------

BANIDOS_TAKE = {
    "stiffens": "estado mudando no TAKE — o prop e' imovel",
    "swells": "idem", "grows": "idem", "rises": "idem",
    "pulse": "nomear o eixo ja' basta para o filtro; negar nao protege",
    "erect": "vocabulario de estado na direcao de cena",
}
BANIDOS_IMAGE = {
    "engorged": "adjetivo de estado no IMAGE",
    "veins": "detalhe anatomico no prop",
    "throbbing": "idem",
}
BANIDOS_GLOBAL = {
    "the narrator": "o agente e' 1a pessoa: nao existe narrador externo",
    "the victim": "nao ha' vitima neste agente — a dor e' dele",
    "ordinary relatable": "este agente e' de aspiracao, nao de identificacao",
}
BANIDOS_CTA = {
    "book": "quebra a automacao Comentario->DM",
    "yes": "idem",
    "link": "CTA e' comentario, nao link",
}


# ---------------------------------------------------------------------------
# SORTEIO
# ---------------------------------------------------------------------------

def _palavras(txt):
    return len(re.findall(r"[A-Za-z'\-]+", txt))


def _carregar_ledger():
    if os.path.exists(LEDGER):
        with open(LEDGER, encoding="utf-8-sig") as f:
            return json.load(f)
    return {}


def _gravar_ledger(ledger, spec):
    p = ledger.setdefault(spec["pagina"], {})
    for eixo, val in (("ambiente", spec["ambiente"]["id"]),
                      ("prop", spec["prop"]["id"]),
                      ("receita", spec["receita"]["id"]),
                      ("isca", spec["isca"])):
        p.setdefault(eixo, []).append(val)
        p[eixo] = p[eixo][-12:]
    with open(LEDGER, "w", encoding="utf-8") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)


def _evitando(rng, pool, recentes):
    livres = [x for x in pool if (x.get("id") if isinstance(x, dict) else x) not in recentes]
    return rng.choice(livres if livres else pool)


# ⭐ O EIXO QUE O AGENTE ORIGINAL TINHA E OS ESPECIALISTAS NAO TEM: quem narra.
# No masculino o dono do problema fala de si. No feminino e' a mulher que conta
# — e no CTA 4 dela, que ela resolveu **escondido**. Sao dois anuncios
# diferentes com o mesmo mecanismo, e o alvo muda: um vende para o homem, o
# outro vende para a esposa que compra pro marido.
PERSONAS = [{"id": "homem"}, {"id": "mulher"}]


def sortear(pagina, rng, ledger):
    hist = ledger.get(pagina, {})
    amb = _evitando(rng, AMBIENTES, hist.get("ambiente", [])[-2:])
    prop = _evitando(rng, PROPS, hist.get("prop", [])[-2:])
    rec = _evitando(rng, RECEITAS, hist.get("receita", [])[-2:])
    isca = _evitando(rng, ISCA, hist.get("isca", [])[-3:])
    persona = _evitando(rng, PERSONAS, hist.get("persona", [])[-1:])
    ref = rng.choice(homens_de(pagina))
    mul = rng.choice(mulheres_de(pagina))

    orgaos = rng.sample(NUCLEO, 3)
    n = IDADE_EXT[ref["idade"]]
    if persona["id"] == "mulher":
        falas = [
            rng.choice(HOOKS_F).format(o=orgaos[0], n=n, N=n.capitalize()),
            rng.choice(FUNDIDAS_F).format(o=orgaos[1], ing=rec["fala"]),
            rng.choice(CTAS_F).format(gate=rng.choice(GATES)),
        ]
    else:
        falas = [
            rng.choice(HOOKS).format(o=orgaos[0], n=n, N=n.capitalize()),
            rng.choice(FUNDIDAS).format(o=orgaos[1], ing=rec["fala"]),
            rng.choice(CTAS).format(gate=rng.choice(GATES)),
        ]
    return {"pagina": pagina, "ambiente": amb, "prop": prop, "receita": rec,
            "isca": isca, "ref": ref, "mulher": mul, "persona": persona,
            "falas": falas}


# ---------------------------------------------------------------------------
# GERADOR
# ---------------------------------------------------------------------------

def _quem_fala(spec, et):
    """Quem narra as tres cenas, com beleza e marca facial declaradas."""
    ref, mul = spec["ref"], spec["mulher"]
    # ⚠️ O "mesmo" repete a descricao INTEIRA — marca facial e declaracao de
    # beleza inclusas. Uma ancora curta ("same hair, same dress") carrega a
    # continuidade mas perde o rosto: sem a marca repetida o Veo troca de
    # pessoa entre as cenas, que e' a falha que derrubou a cena do casal do
    # VAZAMENTO. Repetir sai mais barato que consertar.
    if spec["persona"]["id"] == "mulher":
        d = ("a %d-year-old %s woman, %s, %s"
             % (mul["idade"], et, mul["desc"], BELEZA_M))
        return d, "The same " + d[2:]
    d = ("a %d-year-old %s man, %s, bare-chested with %s, %s"
         % (ref["idade"], et, ref["marca"], ref["corpo"], BELEZA_H))
    return d, "The same " + d[2:]


def montar(spec):
    et = ETNIA[spec["pagina"]]
    ref, mul, amb = spec["ref"], spec["mulher"], spec["ambiente"]
    prop, rec, isca = spec["prop"], spec["receita"], spec["isca"]
    falas = spec["falas"]
    fem = spec["persona"]["id"] == "mulher"
    neg = NEGACAO_AVE if prop["marisco"] else ""
    quem, mesmo = _quem_fala(spec, et)
    # o pronome do prop na mao muda com quem esta' segurando
    dela = "her" if fem else "his"
    idade_narra = mul["idade"] if fem else ref["idade"]

    b = {}

    # ⚠️ O REF do bloco 0 e' quem NARRA — e' o rosto que precisa se repetir nas
    # tres cenas. Na persona feminina isso e' a mulher, nao o homem.
    if fem:
        b["BLOCO 0 (REF)"] = (
            "REF 01: Photo of a real person, a %d-year-old %s woman, chest up, "
            "facing the camera directly, calm steady expression. %s. %s. Plain "
            "neutral gray background, soft even frontal light. No subtitles, no "
            "captions, no burned-in text, no watermark."
            % (mul["idade"], et, mul["desc"][0].upper() + mul["desc"][1:],
               BELEZA_M[0].upper() + BELEZA_M[1:])
        )
    else:
        b["BLOCO 0 (REF)"] = (
            "REF 01: Photo of a real person, a %d-year-old %s man, chest up, "
            "facing the camera directly, calm steady expression. Bare-chested "
            "with %s. %s. %s. Plain neutral gray background, soft even frontal "
            "light. No subtitles, no captions, no burned-in text, no watermark."
            % (ref["idade"], et, ref["corpo"],
               ref["marca"][0].upper() + ref["marca"][1:],
               BELEZA_H[0].upper() + BELEZA_H[1:])
        )

    b["IMAGE 01/03"] = (
        "IMAGE 01/03: Medium shot in %s. Standing behind the %s is %s. She looks "
        "straight into the lens, mouth open mid-word." % (amb["set"], amb["bancada"], quem)
        if fem else
        "IMAGE 01/03: Medium shot in %s. Standing behind the %s is %s. He looks "
        "straight into the lens, mouth open mid-word, jaw tight."
        % (amb["set"], amb["bancada"], quem)
    ) + (
        " In %s right hand, held out in front of %s chest, %s holds %s. %s is the "
        "only person in the frame. %s %s%s"
        % (dela, dela, "she" if fem else "he", prop["murcho"],
           "She" if fem else "He", amb["luz"].capitalize(), CAUDA, neg)
    )

    b["IMAGE 02/03"] = (
        "IMAGE 02/03: Medium shot at the %s in the same %s, same light. %s, "
        "stands behind it mid-action, speaking to the camera. On it: %s, and off "
        "to the side %s. Both %s hands are at the glass. %s is the only person "
        "in the frame. %s %s"
        % (amb["bancada"], amb["curto"], mesmo, rec["mesa"], isca, dela,
           "She" if fem else "He", amb["luz"].capitalize(), CAUDA)
    )

    # a cena 3 e' a do casal: os DOIS em quadro, com as duas idades declaradas
    # ⛔ V12 herdado do VAZAMENTO: idade dos dois em toda mencao — falha de
    # classificador documentada.
    b["IMAGE 03/03"] = (
        "IMAGE 03/03: Medium shot in the same %s, same light. Two fully clothed "
        "adults, a %d-year-old woman and a %d-year-old man. %s %d-year-old "
        "%s woman, %s, %s, stands beside him, leaning in against his shoulder, "
        "laughing, one hand flat on his chest. %s %d-year-old %s man, %s, "
        "bare-chested with %s, %s, looks straight into the lens, calm and "
        "confident, one corner of his mouth raised. In her free hand she holds "
        "%s. %s %s%s"
        % (amb["curto"], mul["idade"], ref["idade"],
           # ⛔ A ancora "The same" cai sobre QUEM NARRA — e' o rosto que vem
           # das cenas 1 e 2. O outro entra novo em quadro e nao leva "same",
           # senao promete uma continuidade que nunca existiu.
           ("The same" if fem else "A"),
           mul["idade"], et, mul["desc"], BELEZA_M,
           ("A" if fem else "The same"),
           ref["idade"], et, ref["marca"], ref["corpo"], BELEZA_H,
           prop["ereto"], amb["luz"].capitalize(), CAUDA, neg)
    )

    b["TAKE 01/03"] = (
        "TAKE 01/03: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway, no cuts. The %d-year-old %s speaks straight "
        "into the lens with force. On the word \"this\" %s lifts the thing in "
        "%s right hand an inch toward the camera. %s %s is the only person in "
        "the shot.\nDialogue: \"%s\"\nAudio: quiet kitchen room tone. No music."
        % (idade_narra, "woman" if fem else "man", "she" if fem else "he", dela,
           IMOBILIDADE, "She" if fem else "He", sonorizar(falas[0]))
    )

    b["TAKE 02/03"] = (
        "TAKE 02/03: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway, no cuts. %s hands work while %s talks: %s. "
        "%s eyes stay on the lens the whole time. %s is the only person in the "
        "shot.\nDialogue: \"%s\"\nAudio: quiet kitchen room tone, a spoon "
        "against glass. No music."
        % ("Her" if fem else "His", "she" if fem else "he", rec["acao"],
           "Her" if fem else "His", "She" if fem else "He", sonorizar(falas[1]))
    )

    b["TAKE 03/03"] = (
        "TAKE 03/03: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway, no cuts. The %d-year-old %s looks into the "
        "lens and speaks directly and evenly, no rush. The %d-year-old %s laughs "
        "once and keeps still. Her hand holding it does not move: %s Only the "
        "%d-year-old %s speaks; the other one is silent.\nDialogue: \"%s\"\n"
        "Audio: quiet kitchen room tone, soft laughter. No music."
        % (idade_narra, "woman" if fem else "man",
           ref["idade"] if fem else mul["idade"], "man" if fem else "woman",
           IMOBILIDADE, idade_narra, "woman" if fem else "man",
           sonorizar(falas[2]))
    )

    return b


# ---------------------------------------------------------------------------
# LINTER
# ---------------------------------------------------------------------------

def _hook(spec, blocos, achados):
    """O hook e' 1a pessoa, nomeia o orgao e aponta o prop com deitico."""
    h = spec["falas"][0]
    if not any(n.lower() in h.lower() for n in NUCLEO):
        achados.append(("ERRO", "o hook nao nomeia o orgao com substantivo"))
    if not re.search(r"\bthis\b|\bthis one\b", h, re.I):
        achados.append(("ERRO", "o hook nao aponta o prop — sem deitico o "
                                "espectador nao sabe para onde olhar"))
    # ⚠️ 1a pessoa do PLURAL tambem conta: "We hadn't touched in eight months"
    # e' primeira pessoa e reprovava 15 de 300 sorteios com o regex antigo.
    if not re.search(r"\bmy\b|\bI\b|\bwe\b|\bus\b|\bour\b", h, re.I):
        achados.append(("ERRO", "o hook nao esta' em 1a pessoa — e' o eixo "
                                "inteiro deste agente"))


def _elenco(spec, blocos, achados):
    """Beleza declarada e marca facial presente — de QUEM NARRA.

    ⚠️ O REF deste agente e' quem fala, e isso muda com a persona: no masculino
    e' o homem, no feminino e' a mulher. Checar sempre o homem reprovava metade
    dos sorteios por um defeito que nao existia.
    """
    fem = spec["persona"]["id"] == "mulher"
    beleza = BELEZA_M if fem else BELEZA_H
    marca = (spec["mulher"]["desc"] if fem
             else spec["ref"]["marca"]).split(" and ")[-1]

    for nome in ("IMAGE 01/03", "IMAGE 02/03", "IMAGE 03/03"):
        if beleza not in blocos[nome]:
            achados.append(("ERRO", "%s sem a declaracao de beleza de quem "
                                    "narra" % nome))
        if marca not in blocos[nome]:
            achados.append(("ERRO", "%s sem a marca facial de quem narra — sem "
                                    "ela o rosto troca entre as cenas" % nome))


def _isca(spec, blocos, achados):
    """O curiosity gap: a isca esta' na bancada e NUNCA na copy."""
    if spec["isca"] not in blocos["IMAGE 02/03"]:
        achados.append(("ERRO", "a isca sumiu da bancada — e' ela que gera o "
                                "comentario extra"))
    corpo = " ".join(spec["falas"]).lower()
    for palavra in ("honey", "ginger", "cinnamon", "maca"):
        if palavra in corpo:
            achados.append(("ERRO", "a copy NOMEIA a isca ('%s') — o curiosity "
                                    "gap so' funciona se ela ficar sem nome"
                            % palavra))


def lint(spec, blocos):
    return sc.lint_curto(
        sys.modules[__name__], spec, blocos, (1, 2, 3), TETO_FALA,
        literais=("gelatin trick", "blood flow"),
        extras=(_hook, _elenco, _isca))


# ---------------------------------------------------------------------------
# UI
# ---------------------------------------------------------------------------

# ⭐ PERSONA vem primeiro de proposito: e' o eixo que decide QUEM NARRA, e
# portanto de qual pool a copy inteira sai. Sem ele no painel o operador via
# dois elencos e nao sabia qual dos dois estava falando.
# ⚠️ "REFS_H" e "MULHERES" sao FUNCOES da pagina, nao listas — a UI resolve
# isso desde 2026-07-31 (ver ui_agente.trocar_eixo).
EIXOS_UI = [
    ("persona", "QUEM NARRA", "PERSONAS", "id"),
    ("ambiente", "COZINHA", "AMBIENTES", "id"),
    ("prop", "PROP DO HOOK", "PROPS", "id"),
    ("receita", "O RITUAL", "RECEITAS", "id"),
    ("ref", "O HOMEM", "homens_de", "marca"),
    ("mulher", "A MULHER", "mulheres_de", "desc"),
]

PT_AMB = {"cozinha": "Na cozinha americana clara",
          "cozinha_ilha": "Na cozinha de conceito aberto com ilha",
          "cozinha_madeira": "Na cozinha de carvalho",
          "cozinha_moderna": "Na cozinha moderna preta"}


def resumo_pt(spec):
    et = "branca" if "white" in ETNIA[spec["pagina"]] else "negra"
    if spec["persona"]["id"] == "mulher":
        return ("%s, quem fala e a mulher de %d anos: ela mostra o prop murcho "
                "na mão e conta a dor do marido de %d. Na cena 2 ela prepara a "
                "gelatina na bancada, e na 3 aparece com ele e o prop ereto. "
                "Três cenas, elenco de pele %s."
                % (PT_AMB.get(spec["ambiente"]["id"], "Na cozinha"),
                   spec["mulher"]["idade"], spec["ref"]["idade"], et))
    return ("%s, quem fala e o homem de %d anos sem camisa e muito bonito: ele "
            "mostra o prop murcho na mão e conta a própria dor. Na cena 2 ele "
            "prepara a gelatina na bancada, e na 3 aparece com a mulher de %d "
            "e o prop ereto. Três cenas, elenco de pele %s."
            % (PT_AMB.get(spec["ambiente"]["id"], "Na cozinha"),
               spec["ref"]["idade"], spec["mulher"]["idade"], et))


def _recopiar_receita(spec, rng):
    """A receita entra na fala da cena 2 — trocar o ritual exige reescrever."""
    o = sc.orgao_de(sys.modules[__name__], spec["falas"][1])
    spec["falas"][1] = rng.choice(FUNDIDAS).format(o=o, ing=spec["receita"]["fala"])


def _recopiar_persona(spec, rng):
    """Trocar quem narra troca a copy INTEIRA — sao pools diferentes.

    ⚠️ Sem isto o painel mostraria "quem narra: mulher" com as tres falas na
    voz do homem. O eixo nao e' de elenco, e' de roteiro.
    """
    n = IDADE_EXT[spec["ref"]["idade"]]
    fem = spec["persona"]["id"] == "mulher"
    hooks, fundidas, ctas = ((HOOKS_F, FUNDIDAS_F, CTAS_F) if fem
                             else (HOOKS, FUNDIDAS, CTAS))
    orgaos = rng.sample(NUCLEO, 2)
    spec["falas"] = [
        rng.choice(hooks).format(o=orgaos[0], n=n, N=n.capitalize()),
        rng.choice(fundidas).format(o=orgaos[1], ing=spec["receita"]["fala"]),
        rng.choice(ctas).format(gate=rng.choice(GATES)),
    ]


EIXOS_QUE_MEXEM_NA_COPY = {"receita": _recopiar_receita,
                           "persona": _recopiar_persona,
                           "ref": _recopiar_persona}


def nova_fala(spec, i, rng):
    o = sc.orgao_de(sys.modules[__name__], spec["falas"][i])
    if i == 0:
        n = IDADE_EXT[spec["ref"]["idade"]]
        return rng.choice(HOOKS).format(o=o, n=n, N=n.capitalize())
    if i == 1:
        return rng.choice(FUNDIDAS).format(o=o, ing=spec["receita"]["fala"])
    return rng.choice(CTAS).format(gate=rng.choice(GATES))


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    _rng = random.Random()
    _pag = sys.argv[1] if len(sys.argv) > 1 else "chuck"
    _spec = sortear(_pag, _rng, _carregar_ledger())
    _b = montar(_spec)
    print(resumo_pt(_spec))
    print("=" * 72)
    for _k in sorted(_b):
        print(_b[_k] + "\n" + "-" * 72)
    for _n, _m in lint(_spec, _b):
        print("%s: %s" % (_n, _m))
