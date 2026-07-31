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
TETO_FALA = {1: 24, 2: 34, 3: 32}

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
REFS_H = [
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
]

# ⚠️ "mulheres lindas de TODAS as etnias" (loiras, ruivas, afro-descendentes):
# a variedade mora aqui, mas a **etnia da mulher acompanha a da pagina**, igual
# a do REF — a congruencia de casting e' regra inviolavel do funil.
MULHERES = [
    {"idade": 34, "desc": "long honey-blonde hair past her shoulders, a small beauty mark on her left jaw, a fitted coral summer dress"},
    {"idade": 32, "desc": "long copper-red hair and light freckles across her nose, a fitted white sundress"},
    {"idade": 35, "desc": "long braided hair gathered over one shoulder, a small beauty mark high on her right cheekbone, a fitted emerald dress"},
    {"idade": 33, "desc": "a short natural afro and striking cheekbones, a fitted burgundy summer dress"},
    {"idade": 36, "desc": "long dark wavy hair past her waist and a deep dimple in her right cheek, a fitted turquoise dress"},
]

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

RECEITAS = [
    {"id": "gelatina_agua", "fala": "a spoonful of gelatin into a glass of cold water",
     "mesa": "a plain white sachet of pale powder with no label, a clear glass of water and a metal spoon",
     "acao": "he tears the sachet open, tips the powder into the glass of water and stirs it in slow circles"},
    {"id": "gelatina_limao", "fala": "a spoonful of gelatin into cold water with fresh lemon",
     "mesa": "a plain white sachet of pale powder with no label, a glass of cold water, a halved lemon and a metal spoon",
     "acao": "he empties the sachet into the glass, squeezes the halved lemon over it and stirs it through"},
    {"id": "gelatina_morna", "fala": "a spoonful of gelatin into half a glass of warm water",
     "mesa": "a plain white sachet of pale powder with no label, a glass of warm water and a long metal spoon",
     "acao": "he empties the sachet into the warm water and stirs until the powder is gone"},
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
    "Next Friday night she'll ask what changed. Comment gelatin, and I'll send you the exact one I use. {gate}",
    "A month from tonight you won't recognise yourself. Comment gelatin, and I'll send you where I get mine. {gate}",
    "I waited two years to find this. Comment gelatin, and you won't wait two days. {gate}",
    "Comment gelatin, and I'll send you the one my neighbor sent me. Nobody in my house ever knew. {gate}",
    "Comment gelatin, and I'll send it tonight. There's one more ingredient on that counter I can't name here. {gate}",
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


def sortear(pagina, rng, ledger):
    hist = ledger.get(pagina, {})
    amb = _evitando(rng, AMBIENTES, hist.get("ambiente", [])[-2:])
    prop = _evitando(rng, PROPS, hist.get("prop", [])[-2:])
    rec = _evitando(rng, RECEITAS, hist.get("receita", [])[-2:])
    isca = _evitando(rng, ISCA, hist.get("isca", [])[-3:])
    ref = rng.choice(REFS_H)
    mul = rng.choice(MULHERES)

    orgaos = rng.sample(NUCLEO, 3)
    n = IDADE_EXT[ref["idade"]]
    falas = [
        rng.choice(HOOKS).format(o=orgaos[0], n=n, N=n.capitalize()),
        rng.choice(FUNDIDAS).format(o=orgaos[1], ing=rec["fala"]),
        rng.choice(CTAS).format(gate=rng.choice(GATES)),
    ]
    return {"pagina": pagina, "ambiente": amb, "prop": prop, "receita": rec,
            "isca": isca, "ref": ref, "mulher": mul, "falas": falas}


# ---------------------------------------------------------------------------
# GERADOR
# ---------------------------------------------------------------------------

def montar(spec):
    et = ETNIA[spec["pagina"]]
    ref, mul, amb = spec["ref"], spec["mulher"], spec["ambiente"]
    prop, rec, isca = spec["prop"], spec["receita"], spec["isca"]
    falas = spec["falas"]
    neg = NEGACAO_AVE if prop["marisco"] else ""

    quem = ("a %d-year-old %s man, %s, bare-chested with %s, %s"
            % (ref["idade"], et, ref["marca"], ref["corpo"], BELEZA_H))
    mesmo = ("The same %d-year-old %s man, same hair, same %s, same build"
             % (ref["idade"], et, ref["marca"].split(" and ")[-1]))

    b = {}

    b["BLOCO 0 (REF)"] = (
        "REF 01: Photo of a real person, a %d-year-old %s man, chest up, facing "
        "the camera directly, calm steady expression. Bare-chested with %s. %s. "
        "%s. Plain neutral gray background, soft even frontal light. No "
        "subtitles, no captions, no burned-in text, no watermark."
        % (ref["idade"], et, ref["corpo"],
           ref["marca"][0].upper() + ref["marca"][1:],
           BELEZA_H[0].upper() + BELEZA_H[1:])
    )

    b["IMAGE 01/03"] = (
        "IMAGE 01/03: Medium shot in %s. Standing behind the %s is %s. He looks "
        "straight into the lens, mouth open mid-word, jaw tight. In his right "
        "hand, held out in front of his chest, he holds %s. He is the only "
        "person in the frame. %s %s%s"
        % (amb["set"], amb["bancada"], quem, prop["murcho"],
           amb["luz"].capitalize(), CAUDA, neg)
    )

    b["IMAGE 02/03"] = (
        "IMAGE 02/03: Medium shot at the %s in the same %s, same light. %s, "
        "bare-chested, stands behind it mid-action, speaking to the camera. On "
        "it: %s, and off to the side %s. Both his hands are at the glass. He is "
        "the only person in the frame. %s %s"
        % (amb["bancada"], amb["curto"], mesmo, rec["mesa"], isca,
           amb["luz"].capitalize(), CAUDA)
    )

    b["IMAGE 03/03"] = (
        "IMAGE 03/03: Medium shot in the same %s, same light. %s, bare-chested, "
        "stands at the %s looking straight into the lens, calm and confident, "
        "one corner of his mouth raised. Beside him a %d-year-old %s woman, %s, "
        "%s, leans in against his shoulder, laughing, one hand flat on his "
        "chest. In her free hand she holds %s. %s %s%s"
        % (amb["curto"], mesmo, amb["bancada"], mul["idade"], et, mul["desc"],
           BELEZA_M, prop["ereto"], amb["luz"].capitalize(), CAUDA, neg)
    )

    b["TAKE 01/03"] = (
        "TAKE 01/03: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway, no cuts. The %d-year-old man speaks straight "
        "into the lens with force. On the word \"this\" he lifts the thing in "
        "his right hand an inch toward the camera. %s He is the only person in "
        "the shot.\nDialogue: \"%s\"\nAudio: quiet kitchen room tone. No music."
        % (ref["idade"], IMOBILIDADE, sonorizar(falas[0]))
    )

    b["TAKE 02/03"] = (
        "TAKE 02/03: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway, no cuts. His hands work while he talks: %s. "
        "His eyes stay on the lens the whole time. He is the only person in the "
        "shot.\nDialogue: \"%s\"\nAudio: quiet kitchen room tone, a spoon "
        "against glass. No music."
        % (rec["acao"], sonorizar(falas[1]))
    )

    b["TAKE 03/03"] = (
        "TAKE 03/03: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway, no cuts. The %d-year-old man looks into the "
        "lens and speaks directly and evenly, no rush. The %d-year-old woman "
        "laughs once against his shoulder and keeps her hand where it is. Her "
        "other hand does not move: %s Only he speaks; she is silent and "
        "laughing.\nDialogue: \"%s\"\nAudio: quiet kitchen room tone, soft "
        "laughter. No music."
        % (ref["idade"], mul["idade"], IMOBILIDADE, sonorizar(falas[2]))
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
    if not re.search(r"\bmy\b|\bI\b", h):
        achados.append(("ERRO", "o hook nao esta' em 1a pessoa — e' o eixo "
                                "inteiro deste agente"))


def _elenco(spec, blocos, achados):
    """Beleza declarada nas tres cenas, e a marca facial presente."""
    for nome in sorted(k for k in blocos if k.startswith("IMAGE")):
        if "IMAGE 01" in nome and BELEZA_H not in blocos[nome]:
            achados.append(("ERRO", "%s sem a declaracao de beleza do REF" % nome))
    if BELEZA_M not in blocos["IMAGE 03/03"]:
        achados.append(("ERRO", "IMAGE 03 sem a declaracao de beleza da mulher"))
    marca_curta = spec["ref"]["marca"].split(" and ")[-1]
    for nome in ("IMAGE 02/03", "IMAGE 03/03"):
        if marca_curta not in blocos[nome]:
            achados.append(("ERRO", "%s sem a marca facial do REF — sem ela o "
                                    "rosto troca entre as cenas" % nome))


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

EIXOS_UI = [
    ("ambiente", "COZINHA", "AMBIENTES", "id"),
    ("prop", "PROP DO HOOK", "PROPS", "id"),
    ("receita", "O RITUAL", "RECEITAS", "id"),
    ("ref", "O HOMEM", "REFS_H", "marca"),
    ("mulher", "A MULHER", "MULHERES", "desc"),
]

PT_AMB = {"cozinha": "Na cozinha americana clara",
          "cozinha_ilha": "Na cozinha de conceito aberto com ilha",
          "cozinha_madeira": "Na cozinha de carvalho",
          "cozinha_moderna": "Na cozinha moderna preta"}


def resumo_pt(spec):
    et = "branca" if "white" in ETNIA[spec["pagina"]] else "negra"
    return ("%s, o homem de %d anos sem camisa e muito bonito mostra o prop "
            "murcho na mão e conta a própria dor. Na cena 2 ele prepara a "
            "gelatina na bancada, e na 3 aparece com a mulher e o prop ereto. "
            "Três cenas, elenco de pele %s."
            % (PT_AMB.get(spec["ambiente"]["id"], "Na cozinha"),
               spec["ref"]["idade"], et))


def _recopiar_receita(spec, rng):
    """A receita entra na fala da cena 2 — trocar o ritual exige reescrever."""
    o = sc.orgao_de(sys.modules[__name__], spec["falas"][1])
    spec["falas"][1] = rng.choice(FUNDIDAS).format(o=o, ing=spec["receita"]["fala"])


EIXOS_QUE_MEXEM_NA_COPY = {"receita": _recopiar_receita}


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
