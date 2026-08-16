# -*- coding: utf-8 -*-
"""gelaHORSE 16 — a caixa de HORSE GELATIN na cozinha, e a receita em copo.

    python funil-organico/gelahorse16_short.py --autoteste
    python funil-organico/gelahorse16_short.py --pagina joe

===============================================================================
 A FONTE — Healthy Men's Guide
===============================================================================
13 reels de `facebook.com/HealthyMensGuide/reels/`, enumerados pelo
`garimpo_apify.py` e BAIXADOS pelas URLs `.mp4` do proprio payload — sem a
sessao pessoal do operador em nenhum momento. Quadros a 2/s (490 no total) e
transcricao `faster-whisper small.en`.

⚠️ E' a mesma pagina do `horse16`, que nasceu de UM reel dela (1038123865853645,
69K). Este agente CONVIVE com ele, por ordem do operador — o `horse16` e' o bar
de garagem com o casal; este e' a COZINHA com a caixa.

⭐⭐ A PAGINA E' UMA MAQUINA DE REPETICAO. Os 13 reels contam a MESMA historia
com variacao minima: *"minha mulher ia me deixar"* -> *"horse gelatin, meio
limao e uma colher de canela"* -> *"fiquei tres vezes maior"* -> CTA. E' o
oposto do que eu fiz no VICK: la' eu inventei 100 cenas; aqui a fonte prova que
o caminho e' repetir o que funciona.
    melhor: 96.377 views · 19,7 c/mil     mediana da pagina: ~24K
    o mais eficiente: v05 com 21,7 c/mil  (acima do campeao do BANHO 16 3T)

===============================================================================
 ⛔ AS DECISOES DO OPERADOR (2026-08-16)
===============================================================================
1. **TAKE 1 E TAKE 2 SORTEADOS SEPARADOS, opcao (b)**: o AMBIENTE vem do take
   1 e so' o GESTO do take 2 vem da pool propria. ⭐ Isso da' 6x4 combinacoes
   sem quebrar a continuidade — se o take 2 trouxesse o ambiente dele, o
   segundo quadro mudaria de cozinha no meio do video, que e' o defeito que a
   ancora do `IMAGE 02` existe para impedir.
2. **CONVIVE com o `horse16`.**
3. **Keyword `gelatin`.** ⛔ E ISSO E' CONSERTO, NAO COPIA: dos 13 CTAs da
   fonte, SETE pedem `yes` e TRES pedem `horse` — as duas palavras estao
   BANIDAS na automacao de DM dele. So' tres pedem `gelatin`. Publicar o CTA
   verbatim faria o comentario entrar e a mensagem nao sair.
4. **A copy sai da FALA**, nao da legenda: 11 dos 13 posts tem `text` vazio.
5. **SEM CAVALO VIVO em cena.** ⚠️ O cavalo do ROTULO fica — ele e' o produto,
   e e' o que sustenta o nome quando o animal nao aparece. Mesma excecao ao P12
   ja' declarada no `horse16`.

===============================================================================
 ⚠️ DIVIDA DECLARADA: 6 dos 13 tem leitura otica; 7 nao
===============================================================================
As entradas de cena saem dos videos que eu li QUADRO A QUADRO: v01, v02, v06,
v09, v11 e v13. Os outros sete tem a FALA transcrita (e ela esta' nos pools de
copy, completa), mas a cena deles ainda nao foi lida. ⛔ Nao inventei cena para
completar numero — foi exatamente isso que reprovou o VICK 16.
"""
import argparse
import collections
import json
import os
import random
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import short_comum as sc  # noqa: E402

APP = TITULO = "AGENTE gelaHORSE 16"
SUBTITULO = ("2 takes de 8s · a caixa de HORSE GELATIN na cozinha · take 1 e "
             "take 2 sorteados separados, com o ambiente vindo do take 1")
SLUG = "gelahorse-16"
SEXOS = ("homem",)
CENAS_UI = ["1 · O HOOK + A RECEITA", "2 · O RESULTADO + CTA"]
LEDGER = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      ".gelahorse-16-ledger.json")

KEYWORD_UI = True
KEYWORD_NATIVA = "gelatin"

TETO_FALA = {1: 25, 2: 25}
PISO_FALA = {1: 10, 2: 10}

# ⛔ `Johnson` E' DO CONTRATO E DA FONTE ao mesmo tempo — v06 e v13 usam. E' o
# unico motor do parque em que o CT4b nao precisa de excecao.
NUCLEO = ("Johnson",)

# ⛔ `horse` NAO entra aqui, e a medicao explica: o `lint_curto` varre a fala
# INTEIRA do CTA, e ela carrega `horse gelatin` (o ingrediente) e `big like a
# horse` (a comparacao da fonte). Banir o token acusava 38 de 400 videos por
# copy que esta' certa — o §16 das licoes. O que precisa ser garantido e' que o
# COMANDO seja `Comment gelatin,`, e disso cuida o `lint_cta_literal`.
BANIDOS_CTA = {"book": "quebra a automacao de DM",
               "yes": "quebra a automacao de DM — a FONTE pede `yes` em 7 dos "
                      "13, e e' por isso que este motor troca o CTA"}
BANIDOS_IMAGE = {}
BANIDOS_TAKE = {}
BANIDOS_BLOCO = {}

ETNIA = {"joe": "white American", "marcus": "Black American",
         "ray": "white American", "chuck": "white American",
         "matt": "white American"}


# ===========================================================================
# ⭐ AS CENAS DO TAKE 1 — seis, todas LIDAS quadro a quadro
# ===========================================================================
# Cada entrada leva ambiente + superficie + angulo + o gesto de apresentar a
# caixa. ⛔ O ambiente daqui vale para os DOIS takes (decisao (b) do operador).
CENAS_T1 = [
    {"id": "v01_quartzo_rosa", "v": "v01", "curto": "caixa rosa no quartzo branco",
     "amb": "a bright modern kitchen with grey cabinets blurred behind",
     "sup": "a white quartz counter",
     "cam": "Shot from just above the counter at chest height, close on his "
            "hands, his body cropped at the shoulders",
     "gesto": "his heavily veined, sun-spotted hands are opening the top of a "
              "magenta HORSE GELATIN box standing on the counter, a brown "
              "horse printed on it in a golden field",
     "roupa": "a plain black shirt"},

    {"id": "v02_caixa_erguida", "v": "v02", "curto": "caixa branca erguida",
     "amb": "a kitchen with soft daylight, the room falling out of focus behind",
     "sup": "a marble counter",
     "cam": "Frontal from chest height, he is in frame from the neck down and "
            "his face is never in the shot",
     "gesto": "he is holding a cream-white HORSE GELATIN box up toward the "
              "viewer with both hands, a brown horse printed on the front",
     "roupa": "a yellow cotton t-shirt"},

    {"id": "v06_tabua_magenta", "v": "v06", "curto": "caixa magenta na tábua",
     "amb": "a white kitchen with the far side out of focus",
     "sup": "an end-grain butcher block resting on a marble counter",
     "cam": "Straight on at chest height, close on the block, his torso "
            "cropped above the shoulders",
     "gesto": "his hands are steadying a tall magenta HORSE GELATIN box with a "
              "black horse printed on it, an empty glass bowl waiting beside it",
     "roupa": "a black knit shirt"},

    {"id": "v09_mesa_janela", "v": "v09", "curto": "mesa de madeira na janela",
     "amb": "a warm kitchen corner with a window and a potted plant in a "
            "woven basket behind",
     "sup": "a wooden board on a solid wood table",
     "cam": "Slightly above the table looking down, warm window light raking "
            "across it, only his hands and forearms in frame",
     "gesto": "his hand is setting a pink HORSE GELATIN box upright beside a "
              "glass bowl, a whole lemon and a cut lemon half on the board",
     "roupa": "a dark long-sleeved shirt"},

    {"id": "v11_granito_copo", "v": "v11", "curto": "copo no granito malhado",
     "amb": "a kitchen with white cabinets and a window letting in flat daylight",
     "sup": "a speckled granite counter",
     "cam": "Close at counter height, his torso filling the background, his "
            "face out of frame",
     "gesto": "his hands are set either side of a heavy glass tumbler on the "
              "counter, the HORSE GELATIN box standing just behind it",
     "roupa": "a black shirt"},

    {"id": "v13_bandeira", "v": "v13", "curto": "bandeira dos EUA, sem mãos",
     "amb": "a homely kitchen with a potted plant and a small United States "
            "flag on a stand behind",
     "sup": "an end-grain wooden table",
     "cam": "Straight on at table height, a still establishing shot with "
            "nobody in frame",
     "gesto": "a pink HORSE GELATIN box stands behind an empty glass bowl, and "
              "a turquoise sticky note with `HARD AS ROCK` handwritten on it "
              "lies in front",
     "roupa": None},
]


# ===========================================================================
# ⭐ OS GESTOS DO TAKE 2 — pool PROPRIA, sorteada a parte
# ===========================================================================
# ⛔ Decisao (b): estes trazem o GESTO e o vasilhame, nunca o ambiente. O lugar
# continua sendo o do take 1 — e' o que da' 24 combinacoes sem que a cozinha
# mude no meio do video.
ACOES_T2 = [
    {"id": "espremer_limao", "v": "v01", "curto": "espreme meio limão",
     "gesto": "his hands are squeezing a lemon half over a glass bowl of "
              "bright red gelatin liquid, a thin stream running down into it"},
    {"id": "canela_frasco", "v": "v09", "curto": "polvilha canela do frasco",
     "gesto": "he is tipping a small glass shaker of cinnamon over the bowl of "
              "red liquid, the dark specks settling on the surface"},
    {"id": "mexer_copo", "v": "v11", "curto": "mexe o copo com a colher",
     "gesto": "he is stirring a tall glass of bright pink liquid with a spoon, "
              "one hand steadying the glass on the counter"},
    {"id": "erguer_copo", "v": "v13", "curto": "ergue o copo pronto",
     "gesto": "he is lifting the finished glass of deep red liquid to chest "
              "height, the empty box standing behind it"},
]


# ===========================================================================
# A COPY — VERBATIM DA FALA DOS 13 REELS
# ===========================================================================
# ⚠️ `half a lemon` da fonte virou `lemon`: a fala nao paga o que o quadro
# mostra — e' a mesma correcao ja' aplicada no `horse16`, e a regra do repo
# (sem medida nem fracao na copy falada).
HOOKS = [
    {"v": "v01", "txt": "I thought my wife was about to end everything."},
    {"v": "v02", "txt": "Is it getting smaller and softer every day? Not "
     "anymore, my friend."},
    {"v": "v03", "txt": "My wife was about to leave me because of my "
     "performance."},
    {"v": "v04", "txt": "I thought my wife was going to leave me."},
    {"v": "v06", "txt": "If you see an older man with a younger woman, it is "
     "because he is using horse gelatin."},
    {"v": "v07", "txt": "I was losing my marriage because of my performance."},
    {"v": "v09", "txt": "Feeling like you are not as hard and firm as you used "
     "to be? I was feeling the same way."},
    {"v": "v10", "txt": "I was sure my wife was going to leave me."},
    {"v": "v11", "txt": "My wife was about to leave me. I felt weak, small and "
     "completely useless."},
    {"v": "v13", "txt": "If you see an older guy with a much younger woman, "
     "you can bet he is using horse gelatin."},
]

RECEITAS = [
    {"v": "v01", "txt": "Horse gelatin, lemon and a spoonful of cinnamon "
     "before bed."},
    {"v": "v05", "txt": "Horse gelatin, lemon and a spoonful of cinnamon every "
     "night."},
    {"v": "v03", "txt": "Everything changed with a simple mixture. Horse "
     "gelatin, lemon and cinnamon."},
    {"v": "v04", "txt": "It started with three ingredients. Horse gelatin, "
     "lemon and a spoon of cinnamon."},
    {"v": "v11", "txt": "Then I discovered this raw combination. Horse "
     "gelatin, lemon and cinnamon."},
]

RESULTADOS = [
    {"v": "v01", "txt": "My performance lasted for hours and it grew three "
     "times bigger."},
    {"v": "v02", "txt": "It got bigger and rock hard for hours."},
    {"v": "v03", "txt": "I got three times bigger and hard as iron."},
    {"v": "v06", "txt": "My Johnson got ridiculously bigger. It stayed "
     "firm for hours."},
    {"v": "v10", "txt": "My size increased fast and I was lasting a lot longer."},
    {"v": "v11", "txt": "It gave me back control. I got bigger and lasted "
     "way longer."},
    {"v": "v13", "txt": "My Johnson got big like a horse. It went hard as "
     "a horseshoe."},
]

# ⛔⛔ OS TRES CTAs QUE A FONTE JA' FAZ COM `gelatin`. Os outros dez pedem `yes`
# ou `horse` — palavras BANIDAS na automacao de DM do operador. Nao sao copy
# ruim: sao copy de OUTRA automacao, e publicar verbatim faria o comentario
# entrar e a mensagem nao sair.
CTAS = [
    {"v": "v02", "txt": "Comment gelatin, and I will send you the full "
     "explanation right now."},
    {"v": "v05", "txt": "Comment gelatin, and I will send the step-by-step "
     "straight to your inbox."},
    {"v": "v10", "txt": "Comment gelatin, and I will send you the full step by "
     "step."},
]

IDADES = (62, 65, 67, 69, 71, 74)


# ===========================================================================
# SORTEIO
# ===========================================================================
EIXOS_LEDGER = ("cena", "acao", "hook", "receita", "resultado", "cta")


def _chave(x):
    return x.get("id") or x.get("v")


def _carregar_ledger():
    try:
        with open(LEDGER, "r", encoding="utf-8") as f:
            return json.load(f)
    except (IOError, ValueError):
        return {}


def _anotar(ledger, spec):
    hist = ledger.setdefault(spec["pagina"], {})
    for eixo in EIXOS_LEDGER:
        val = spec.get(eixo)
        if isinstance(val, dict):
            hist.setdefault(eixo, []).append(_chave(val))


def _gravar_ledger(ledger, spec=None):
    if spec is not None:
        _anotar(ledger, spec)
    try:
        with open(LEDGER, "w", encoding="utf-8") as f:
            json.dump(ledger, f, ensure_ascii=False, indent=1)
    except IOError:
        pass


def _fresco(pool, usados, rng):
    livres = [x for x in pool if _chave(x) not in usados]
    return rng.choice(livres or pool)


def _por_id(pool, valor, chave="id"):
    if isinstance(valor, dict):
        return valor
    for x in pool:
        if x.get(chave) == valor:
            return x
    return None


def _palavras(s):
    return len(re.findall(r"[A-Za-z']+", s or ""))


def _cap(s):
    return s[0].upper() + s[1:] if s else s


def _falas(spec, rng, quais=(0, 1)):
    """As duas falas, cada uma um PAR que cabe nos 25.

    ⛔ O par inteiro e' sorteado entre as combinacoes viaveis, nunca em
    cascata: escolher o primeiro beat e depois procurar um que caiba colapsa a
    variancia — medido no VICK, onde o take 2 saiu com UMA fala em 400 videos.
    """
    f = dict(enumerate(spec.get("falas", ["", ""])))
    if 0 in quais:
        pares = [(h, r) for h in HOOKS for r in RECEITAS
                 if _palavras(h["txt"]) + _palavras(r["txt"]) <= TETO_FALA[1]]
        h, r = rng.choice(pares)
        spec["hook"], spec["receita"] = h, r
        f[0] = "%s %s" % (h["txt"], r["txt"])
    if 1 in quais:
        pares = [(x, c) for x in RESULTADOS for c in CTAS
                 if _palavras(x["txt"]) + _palavras(c["txt"]) <= TETO_FALA[2]]
        x, c = rng.choice(pares)
        spec["resultado"], spec["cta"] = x, c
        f[1] = "%s %s" % (x["txt"], c["txt"])
    return f


def sortear(pagina, rng, ledger, travas=None):
    travas = travas or {}
    hist = (ledger or {}).get(pagina, {})
    spec = {
        "pagina": pagina,
        "etnia": ETNIA.get(pagina, "white American"),
        "idade": rng.choice(IDADES),
        "cena": (_por_id(CENAS_T1, travas["cena"]) if travas.get("cena")
                 else _fresco(CENAS_T1, hist.get("cena", [])[-3:], rng)),
        # ⭐ Sorteada A PARTE, como o operador pediu — mas so' o GESTO viaja; o
        # lugar continua sendo o do take 1.
        "acao": (_por_id(ACOES_T2, travas["acao"]) if travas.get("acao")
                 else _fresco(ACOES_T2, hist.get("acao", [])[-2:], rng)),
    }
    spec["falas"] = [v for _, v in sorted(_falas(spec, rng).items())]
    return spec


def nova_fala(spec, i, rng):
    return _falas(spec, rng, quais=(i,))[i]


# ===========================================================================
# MONTAGEM
# ===========================================================================
def _quem(spec):
    c = spec["cena"]
    base = ("a %d-year-old %s man with heavy weathered hands, thick knuckles "
            "and sun spots across the backs" % (spec["idade"], spec["etnia"]))
    return base + (", wearing %s" % c["roupa"] if c["roupa"] else "")


def montar(spec):
    c, a = spec["cena"], spec["acao"]
    h = _quem(spec)
    b = {}

    b["BLOCO 0 (REF)"] = (
        "REF 01: Photo of a real person, %s, chest up, facing forward, calm "
        "steady expression. Plain neutral gray background, soft even frontal "
        "light, hands out of frame. Slight sensor grain, raw amateur photo "
        "look. No subtitles, no captions, no burned-in text, no watermark." % h)

    b["IMAGE 01/02"] = (
        "IMAGE 01/02: Inside %s. On %s, %s. In frame is %s. %s. Everyday "
        "amateur snapshot look, slight natural sway, soft sensor grain. No "
        "on-screen text, no subtitles, no captions, no watermark."
        % (c["amb"], c["sup"], c["gesto"], h, c["cam"]))

    # ⭐ O AMBIENTE E' O MESMO — decisao (b). So' o gesto muda, e a ancora de
    # continuidade vai por extenso para o Veo nao trocar de pessoa.
    b["IMAGE 02/02"] = (
        "IMAGE 02/02: Inside %s, the same place in the same framing. On %s, "
        "%s. It is the same %d-year-old %s man from the first scene, not a "
        "different person. %s. Everyday amateur snapshot look, slight natural "
        "sway, soft sensor grain. No on-screen text, no subtitles, no "
        "captions, no watermark."
        % (c["amb"], c["sup"], a["gesto"], spec["idade"], spec["etnia"],
           c["cam"]))

    b["TAKE 01/02"] = (
        "TAKE 01/02: Animate the provided image exactly. %s and there are no "
        "cuts. He does the movement once, slowly, and stops. Audio: a quiet "
        "kitchen, a box being set down. Only he speaks.\nDialogue: \"%s\""
        % (c["cam"], spec["falas"][0]))

    b["TAKE 02/02"] = (
        "TAKE 02/02: Animate the provided image exactly. %s and there are no "
        "cuts. He finishes the movement and stops; nothing else in the frame "
        "changes. Audio: a quiet kitchen, a spoon against glass. Only he "
        "speaks.\nDialogue: \"%s\"" % (c["cam"], spec["falas"][1]))

    return sc.selar_takes(sc.selar_tags(b))


# ===========================================================================
# AS LENTES
# ===========================================================================
_RX_APARELHO = re.compile(
    r"\b(phone|iphone|smartphone|camera|lens|filming|filmed|tripod)\b", re.I)
_RX_CAVALO_VIVO = re.compile(
    r"\b(a|the|live|real) (horse|mare|stallion|pony)\b(?! gelatin)", re.I)


def _gh1_sem_aparelho(spec, blocos, ach):
    """⛔ Aparelho escrito no prompt vira aparelho DESENHADO — licao do VICK."""
    for k, v in blocos.items():
        if k.startswith("BLOCO"):
            continue
        m = _RX_APARELHO.search(v)
        if m:
            ach.append(("ERRO", "GH1: %s nomeia %r" % (k, m.group(0))))


def _sem_dialogo(txt):
    """O bloco sem a linha `Dialogue:`.

    ⛔ Lente de CENA nunca le' a FALA. `big like a horse` e `hard as a
    horseshoe` sao comparacoes que a fonte diz, e acusa-las como cavalo em cena
    reprova copy validada — o mesmo motivo pelo qual a lente do anticeleb le' a
    direcao e nunca o dialogo.
    """
    return re.split(r"\nDialogue:", txt or "")[0]


def _gh2_sem_cavalo_vivo(spec, blocos, ach):
    """⛔ Ordem do operador: SEM CAVALO. O do ROTULO fica — ele e' o produto e e'
    o que sustenta o nome quando o animal nao aparece (excecao ao P12 ja'
    declarada no `horse16`). Esta lente separa os dois: `a horse printed on it`
    passa, `a horse grazing behind` nao."""
    for k, bruto in blocos.items():
        v = _sem_dialogo(bruto)
        for m in _RX_CAVALO_VIVO.finditer(v):
            trecho = v[max(0, m.start() - 60):m.end() + 40]
            if re.search(r"printed|label|box|on the front|illustration",
                         trecho, re.I):
                continue
            ach.append(("ERRO", "GH2: %s poe um cavalo VIVO em cena (%r) — o "
                                "cavalo so' existe no rotulo"
                        % (k, m.group(0))))


def _gh3_caixa_no_quadro(spec, blocos, ach):
    """A caixa E' o mecanismo: sem ela em quadro o video nao diz o que vender."""
    if "HORSE GELATIN" not in blocos["IMAGE 01/02"]:
        ach.append(("ERRO", "GH3: a IMAGE 01 sem a caixa de HORSE GELATIN"))


def _gh4_continuidade(spec, blocos, ach):
    c = spec["cena"]
    for k in ("IMAGE 01/02", "IMAGE 02/02"):
        if c["amb"] not in blocos[k] or c["sup"] not in blocos[k]:
            ach.append(("ERRO", "GH4: %s nao acontece no mesmo lugar — o "
                                "ambiente vem do take 1 nos DOIS quadros" % k))


def _gh5_copy_com_origem(spec, blocos, ach):
    """Toda fala e' verbatim da fala dos 13 reels."""
    for beat, i in ((spec["hook"], 0), (spec["receita"], 0),
                    (spec["resultado"], 1), (spec["cta"], 1)):
        if beat["txt"] not in spec["falas"][i]:
            ach.append(("ERRO", "GH5: o beat %s nao chegou a fala %d"
                        % (beat["v"], i + 1)))


def _gh6_orcamento(spec, blocos, ach):
    for i, fala in enumerate(spec["falas"], 1):
        n = _palavras(fala)
        if n > TETO_FALA[i]:
            ach.append(("ERRO", "GH6: cena %d com %d palavras (teto %d)"
                        % (i, n, TETO_FALA[i])))
        if n < PISO_FALA[i]:
            ach.append(("AVISO", "GH6: cena %d com so' %d palavras" % (i, n)))


def _gh7_fala_no_take(spec, blocos, ach):
    for i, k in enumerate(("TAKE 01/02", "TAKE 02/02")):
        if ('Dialogue: "%s"' % spec["falas"][i]) not in blocos[k]:
            ach.append(("ERRO", "GH7: a fala %d nao chega verbatim ao %s"
                        % (i + 1, k)))


def _ct16(spec, blocos, ach):
    """⛔ CT5 desligado: a FONTE nomeia a receita na fala em 13 de 13, e e' o
    par de hipotese que o PRATO 16 e o MEL 16 ja' testam. Aqui ela vem de graca,
    porque e' assim que a pagina de 96 mil views fala."""
    fora = []
    sc.lint_copy16(sys.modules[__name__], spec, fora)
    ach.extend(x for x in fora if not x[1].startswith("CT5:"))


def _anticeleb(spec, blocos, ach):
    sc.lint_anticeleb(blocos, ach)


def _painel(spec, blocos, ach):
    sc.lint_painel_honesto(sys.modules[__name__], spec, blocos, ach)


def lint(spec, blocos):
    return sc.lint_curto(
        sys.modules[__name__], spec, blocos, (1, 2), TETO_FALA,
        literais=("gelatin",), cota_min=0,
        extras=(_ct16, _anticeleb, _painel, _gh1_sem_aparelho,
                _gh2_sem_cavalo_vivo, _gh3_caixa_no_quadro, _gh4_continuidade,
                _gh5_copy_com_origem, _gh6_orcamento, _gh7_fala_no_take))


# ===========================================================================
# RESUMO E PAINEL
# ===========================================================================
def resumo_pt(spec):
    c, a = spec["cena"], spec["acao"]
    return ("16s, DOIS takes, cozinha. TAKE 1 (%s da fonte): %s — %s. "
            "TAKE 2 (%s da fonte): %s, NO MESMO lugar. Homem de %d anos, %s. "
            "Beats: hook %s · receita %s · resultado %s · CTA %s, todos "
            "verbatim da fala. Fecha em `gelatin` (a fonte pede `yes`/`horse`, "
            "que quebram a automacao). SEM cavalo vivo."
            % (c["v"], c["curto"], c["sup"], a["v"], a["curto"], spec["idade"],
               spec["etnia"], spec["hook"]["v"], spec["receita"]["v"],
               spec["resultado"]["v"], spec["cta"]["v"]))


EIXOS_UI = [
    ("cena", "A CENA (take 1)", "CENAS_T1", "curto"),
    ("acao", "O GESTO (take 2)", "ACOES_T2", "curto"),
]
EIXOS_TRAVAVEIS = ["cena", "acao"]
DROPDOWNS_UI = [("cena", "A CENA", "CENAS_T1", "curto")]
IGNORA_PAINEL = ()


# ===========================================================================
# AUTOTESTE
# ===========================================================================
def _autoteste(n=400, seed=20260816):
    rng = random.Random(seed)
    led, erros = {}, collections.Counter()
    vc, va = collections.Counter(), collections.Counter()
    pares_vistos = set()
    falas = {1: set(), 2: set()}
    pal = {1: [], 2: []}
    for _ in range(n):
        sp = sortear("joe", rng, led)
        _anotar(led, sp)
        bl = montar(sp)
        for nivel, txt in lint(sp, bl):
            if nivel == "ERRO":
                erros[txt.split(":")[0]] += 1
        vc[sp["cena"]["id"]] += 1
        va[sp["acao"]["id"]] += 1
        pares_vistos.add((sp["cena"]["id"], sp["acao"]["id"]))
        for i in (1, 2):
            falas[i].add(sp["falas"][i - 1])
            pal[i].append(_palavras(sp["falas"][i - 1]))

    print("%s — %d sorteios (seed %d)" % (APP, n, seed))
    print("  cenas do take 1: %d de %d · gestos do take 2: %d de %d"
          % (len(vc), len(CENAS_T1), len(va), len(ACOES_T2)))
    print("  combinacoes cena x gesto vistas: %d de %d possiveis"
          % (len(pares_vistos), len(CENAS_T1) * len(ACOES_T2)))
    for i in (1, 2):
        print("  cena %d: %3d falas distintas · palavras %d/%d/%d"
              % (i, len(falas[i]), min(pal[i]), sum(pal[i]) // len(pal[i]),
                 max(pal[i])))
    print("  pools: %d cenas · %d gestos · %d hooks · %d receitas · "
          "%d resultados · %d CTAs"
          % (len(CENAS_T1), len(ACOES_T2), len(HOOKS), len(RECEITAS),
             len(RESULTADOS), len(CTAS)))
    print("  linter: %d ERRO" % sum(erros.values()))
    for k, v in erros.most_common(8):
        print("     %4dx %s" % (v, k))
    return sum(erros.values())


def main():
    ap = argparse.ArgumentParser(description=APP)
    ap.add_argument("--pagina", default="joe")
    ap.add_argument("--seed", type=int)
    ap.add_argument("--autoteste", action="store_true")
    ap.add_argument("--n", type=int, default=400)
    a = ap.parse_args()
    if a.autoteste:
        raise SystemExit(1 if _autoteste(a.n) else 0)
    rng = random.Random(a.seed)
    sp = sortear(a.pagina, rng, _carregar_ledger())
    bl = montar(sp)
    print(resumo_pt(sp), "\n")
    for k in ("BLOCO 0 (REF)", "IMAGE 01/02", "IMAGE 02/02",
              "TAKE 01/02", "TAKE 02/02"):
        print("=" * 70)
        print(bl[k], "\n")
    for nivel, txt in lint(sp, bl):
        print("[%s] %s" % (nivel, txt))


if __name__ == "__main__":
    main()
