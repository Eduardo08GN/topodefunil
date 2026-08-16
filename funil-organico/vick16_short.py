# -*- coding: utf-8 -*-
"""VICK 16 — a pomada azul. RECONSTRUIDO PEQUENO E FIEL em 2026-08-15.

    python funil-organico/vick16_short.py --autoteste
    python funil-organico/vick16_short.py --pagina joe

===============================================================================
 ⛔⛔ POR QUE ESTE ARQUIVO FOI REESCRITO DO ZERO NO MESMO DIA EM QUE NASCEU
===============================================================================
A primeira versao tinha 7.153 linhas, pools de 100 entradas por eixo e media
**0 ERRO em 600 sorteios**. O operador reprovou olhando o video:

    *"deu muito ruim essa arquitetura. As cenas ficaram com muito elemento
    visual sem nexo e as copys completamente em drifting copy."*

Ele estava certo, e as duas causas sao a mesma: **eu media DISTINCAO e chamava
de qualidade**.

 1. **SETE EIXOS SORTEADOS E EMPILHADOS** — cena, acao, regua, rotulo,
    vasilhame, pessoa, camera. Cada PAR passava numa lente de compatibilidade;
    o QUADRO INTEIRO nunca foi verificado. Cem elementos distintos viraram cem
    elementos SOLTOS.
    ⭐ A fonte varia praticamente UM: a superficie. Todo o resto dela e'
    constante — e e' exatamente por isso que os 15 videos parecem a mesma
    pagina em vez de quinze colagens.

 2. **PROIBIR O MECANISMO NA FALA ESVAZIOU A COPY.** A lente VI1 da v1 proibia
    nomear a pomada e a gelatina, para forcar o comentario. Sem o concreto,
    sobrava `it sweeps the plaque out of the way` — ninguem sabe o que e' a
    placa nem o que e' o ritual. Drifting puro, e por DESENHO meu.
    ⛔ E o pior: **a fonte JA' E' CONCRETA e eu joguei fora**. O v11 diz
    *"15 seconds in the shower, one ingredient you already walked past at the
    supermarket. 21 days later, I was 4 inches bigger."* Segundos, lugar,
    prazo, numero. Eu tinha isso na mao e mandei onze agentes inventarem por
    cima.

===============================================================================
 O QUE ESTA VERSAO FAZ DIFERENTE
===============================================================================
⭐ **UM EIXO FORTE VARIA: A SUPERFICIE.** Sao as 15 superficies REAIS lidas nos
15 videos, uma por video, zero repeticao e nenhuma inventada. Tudo o que a
fonte mantem constante fica CONSTANTE aqui: o pote azul, o sache, a regua de
madeira, a placa `growth hack`, o gesto, o ponto de vista e as maos.
⛔ A lista `PROPS`/`MAOS`/`CAMERA`/`GESTO_*` mais abaixo E' o conserto. Na v1
cada uma delas era um pool sorteado.

⭐⭐ **TODA FALA E' VERBATIM DA FONTE.** Nao ha uma linha de copy escrita por
mim nem por agente: cada beat carrega o `v` do video de onde saiu, a lente VI1
cobra isso a cada sorteio, e o autoteste conta quantos beats chegaram sem
origem (tem de ser zero). Recombinar o que o campo ja' aprovou e' barato;
inventar por cima foi o que custou a v1.

⛔ E O CONCRETO VOLTA A SER DITO. `fifteen seconds`, `four inches`,
`twenty-one days`, `supermarket`, `blue pills`, `no pharmacy` — a fonte diz
tudo isso e converte. A trava de nao nomear ingrediente (CT5) vale para os
motores cuja moeda e' a RECEITA; aqui a moeda e' o PASSO A PASSO: o video diz
o QUE, a DM diz o COMO. Excecao declarada em `medir_copy16.DESLIGADAS`.

===============================================================================
 A FONTE
===============================================================================
15 reels em `C:/Users/edlut/Music/OKC-Likes-Viewer-master/vick`, 300s, lidos a
2 quadros/s (566 quadros) e transcritos com `faster-whisper small.en`. Mapa em
[`concorrentes/vick-mapa-visual.md`](../concorrentes/vick-mapa-visual.md).
⛔ E' a mesma fonte dos tres BANHO; o que separa e' o VICKS, em 13 dos 15.
⛔ A frase do rodeio (v03) NAO entra: ela e' exclusiva do `banho16_v2`.
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

APP = TITULO = "AGENTE VICK 16"
SUBTITULO = ("2 takes de 8s · a pomada azul no banheiro · UM eixo varia (o "
             "lugar) e toda fala e' verbatim dos 15 videos da fonte")
SLUG = "vick-16"
SEXOS = ("homem",)
CENAS_UI = ["1 · O HOOK", "2 · O MECANISMO + CTA"]
LEDGER = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      ".vick-16-ledger.json")

KEYWORD_UI = True
KEYWORD_NATIVA = "recipe"

TETO_FALA = {1: 25, 2: 25}
PISO_FALA = {1: 8, 2: 10}

# ⛔ Os apelidos que a FONTE usa. Excecao ao CT4b, declarada.
NUCLEO = ("baseball bat", "small bat", "shrinking bat", "pipes")

BANIDOS_CTA = {"book": "quebra a automacao de DM",
               "yes": "quebra a automacao de DM"}
BANIDOS_IMAGE = {}
BANIDOS_TAKE = {}
BANIDOS_BLOCO = {}

ETNIA = {"joe": "white American", "marcus": "Black American",
         "ray": "white American", "chuck": "white American",
         "matt": "white American"}


# ===========================================================================
# ⭐ O UNICO EIXO QUE VARIA — as 15 superficies REAIS
# ===========================================================================
# Uma por video da fonte, zero repeticao, nenhuma inventada. Cada entrada leva
# o ambiente e o AUDIO juntos, porque um sem o outro e' meio quadro. Camera e
# luz NAO entram aqui: elas sao constantes, e e' isso que faz os quinze
# parecerem a mesma pagina.
SUPERFICIES = [
    {"id": "borda_banheira", "v": "v01", "curto": "borda branca da banheira",
     "amb": "a small older bathroom, the white alcove tub filling behind, "
            "white square tile with dark grout",
     "sup": "the flat white capping ledge on top of the tub surround",
     "audio": "tap water running into the filling tub, small tiled echo"},
    {"id": "bancada_pia", "v": "v02", "curto": "tampo branco da pia",
     "amb": "a bright clean bathroom with daylight from a window, a frameless "
            "mirror on the wall behind",
     "sup": "the white cultured-marble vanity top, on the flat wing to the "
            "left of the basin",
     "audio": "quiet room tone, a spoon clinking against glass"},
    {"id": "deck_ceramica", "v": "v03", "curto": "deck de ceramica bege",
     "amb": "a large built-in tub filled with pale mint water, warm beige walls",
     "sup": "the wide beige ceramic tub deck, grout lines crossing it",
     "audio": "still bath water lapping faintly"},
    {"id": "caddy_inox", "v": "v04", "curto": "caddy de inox no box",
     "amb": "a closed shower stall, two cream tiled walls meeting at a corner, "
            "the shower head running",
     "sup": "a brushed stainless corner caddy clamped to the riser pole",
     "audio": "the shower running steady on tile"},
    {"id": "banquinho_madeira", "v": "v05", "curto": "banquinho de madeira",
     "amb": "a domestic bathroom, a white tub half full of still water, a "
            "coiled hand-shower hose hanging on the wall",
     "sup": "the pale wooden seat of a low solid-wood stool pushed against "
            "the side of the tub",
     "audio": "still bath water shifting, a small room echo"},
    {"id": "nicho_embutido", "v": "v06", "curto": "piso do nicho embutido",
     "amb": "a shower walled in grey reclaimed barn wood, a rain head pouring "
            "a straight curtain of water",
     "sup": "the smooth white plaster floor of a square niche cut into the "
            "wood wall",
     "audio": "the rain head drumming on the shower floor"},
    {"id": "caddy_arame", "v": "v07", "curto": "caddy de arame cromado",
     "amb": "a plain tiled shower with the head running and steam on the far "
            "wall, the shower pipe crossing above",
     "sup": "the upper tray of a two-tier chrome wire caddy hanging from the "
            "shower pipe",
     "audio": "water pattering through the wire tray"},
    {"id": "tabua_acougueiro", "v": "v08", "curto": "tabua de acougueiro",
     "amb": "a home kitchen with a window over the sink behind and a kettle "
            "on the hob",
     "sup": "a pale butcher-block counter, its vertical glue joints visible",
     "audio": "kitchen room tone, a spoon tapping wood"},
    {"id": "marmore_pia", "v": "v09", "curto": "marmore da pia",
     "amb": "a warm bathroom with a wide mirror and a folded towel on the rail "
            "behind",
     "sup": "the marble vanity top in the foreground, grey veining on white",
     "audio": "quiet room tone, a lid unscrewing"},
    {"id": "prateleira_vidro", "v": "v10", "curto": "prateleira de vidro",
     "amb": "a compact bathroom with a mirrored cabinet standing open",
     "sup": "a glass shelf inside the open cabinet, lit from above",
     "audio": "a cabinet door swinging, quiet room tone"},
    {"id": "prateleira_macica", "v": "v11", "curto": "prateleira de madeira macica",
     "amb": "a shower stall with the water running the whole time and dark "
            "tiled walls",
     "sup": "a thick varnished solid-wood corner shelf, water beading on it",
     "audio": "the shower running steadily, water on wood"},
    {"id": "tampa_vaso", "v": "v12", "curto": "tampa do vaso sanitario",
     "amb": "a small bathroom at night, the only light coming from above the "
            "mirror",
     "sup": "the closed white toilet lid, used flat as a work surface",
     "audio": "a very quiet house, a plastic sachet tearing"},
    {"id": "tampo_direita_cuba", "v": "v13", "curto": "tampo a direita da cuba",
     "amb": "a plain white bathroom with a chrome mixer tap behind",
     "sup": "the flat white counter to the right of the basin, with nothing "
            "inside the bowl",
     "audio": "a tap dripping once, tiled room tone"},
    {"id": "granito_bege", "v": "v14", "curto": "granito bege do box",
     "amb": "a shower stall with running water and mottled beige stone walls",
     "sup": "a built-in quarter-circle corner shelf in mottled beige granite",
     "audio": "the shower running on stone"},
    {"id": "prateleira_espelho", "v": "v15", "curto": "prateleira sob o espelho",
     "amb": "a bathroom seen past the edge of a wall mirror, a towel on a hook",
     "sup": "a narrow shelf mounted under the mirror",
     "audio": "quiet room tone, a jar set down on the shelf"},
]


# ===========================================================================
# ⛔⛔ O QUE NAO VARIA — e ESTA LISTA E' O CONSERTO
# ===========================================================================
# Na versao reprovada cada um destes era um pool sorteado, e a soma deles foi o
# "muito elemento visual sem nexo". Aqui sao STRINGS TRAVADAS, porque e' assim
# que a fonte faz: os 15 videos tem o mesmo pote, o mesmo sache, a mesma regua,
# a mesma placa, o mesmo gesto e o mesmo ponto de vista. O que muda entre eles
# e' ONDE isso acontece — e so'.
PROPS = ("an open cobalt-blue jar of vapour rub with its turquoise lid lying "
         "beside it, a torn foil gelatin sachet, a plain yellow wooden ruler "
         "lying flat and untouched, and a brown cardboard sign with `growth "
         "hack` written on it in black marker leaning against the wall behind")

# ⚠️ A forma CURTA existe so' para o take 2 nao repetir a lista inteira: o
# repeat com a lista completa produzia `The same an open cobalt-blue jar...`.
PROPS_CURTO = ("the same blue jar, the torn sachet, the wooden ruler and the "
               "cardboard sign")

MAOS = ("the weathered hands of an older man, thick knuckles and sun spots "
        "across the backs, no face and no body in frame")

CAMERA = ("POV of a man standing over the surface with the phone in his free "
          "hand, looking down at about forty-five degrees, slight handheld "
          "drift")

LUZ = "plain domestic bathroom light, no colour cast"

GESTO_IMG = ("his index finger is pressing into the pale powder heaped on the "
             "surface of the blue rub, lifting a small ridge of it clear of "
             "the rim")

GESTO_TAKE = ("He presses one finger into the jar and stirs the powder into "
              "the blue rub once, and the mixture rises into a pale foam that "
              "climbs to the rim")

PAYOFF_IMG = ("the mixture in the jar has risen into a pale foam of large "
              "bubbles that reaches the rim, untouched, with no hand near it")

CAUDA = ("Shot on an iPhone held in one hand, slight natural sway, soft sensor "
         "grain. No on-screen text, no subtitles, no captions, no watermark.")


# ===========================================================================
# ⭐⭐ A COPY — VERBATIM, e cada beat diz de que video saiu
# ===========================================================================
# ⛔ NENHUMA linha aqui foi escrita por mim nem por agente. Sao as falas dos 15
# videos, cortadas nos beats, com a idade parametrizada apenas onde a fonte JA'
# a variava (66/67/72/74 sao quatro videos com a mesma frase e idade diferente).
# ⭐ E' o oposto do que a v1 fez: la' eu gerei 224 falas e o resultado foi vago
# com metrica boa.
HOOKS = [
    {"v": "v01", "txt": "I am {idade} and this is the shower hack I use every "
     "night to look bigger and last longer."},
    {"v": "v02", "txt": "If you are single, do not try this. If you are "
     "married, try it in moderation."},
    {"v": "v03", "txt": "If you are a man over 50 and you are not doing this "
     "trick yet, you are already falling behind."},
    {"v": "v05", "txt": "Struggling to stay hard, or with your small size? "
     "That is not about getting older."},
    {"v": "v06", "txt": "I am {idade} and I fixed my small bat with a shower "
     "habit."},
    {"v": "v08", "txt": "Over 60 and tired of going soft or feeling small? "
     "This kitchen hack makes you hard."},
    {"v": "v09", "txt": "At {idade} I wake up bigger than I did in my twenties "
     "with this trick."},
    {"v": "v10", "txt": "Why accept a shrinking bat and going soft? At {idade} "
     "I stopped accepting it."},
    {"v": "v11", "txt": "My wife almost cheated on me. She said to my face "
     "that I was not enough for her anymore."},
    {"v": "v12", "txt": "Is going soft ruining the mood? A bizarre nighttime "
     "trick saved my marriage."},
    {"v": "v13", "txt": "Over 50 and tired of going soft or feeling small? "
     "This shower hack brings your size back."},
    {"v": "v15", "txt": "Stop accepting a shrinking bat. I am {idade} and a "
     "bizarre nighttime habit restored my size."},
]

# ⛔ O MECANISMO VOLTA A SER DITO. Sao as frases da fonte, e elas nomeiam o que
# esta' acontecendo — o contrario do `it sweeps the plaque out of the way` que
# o operador reprovou.
MECANISMOS = [
    {"v": "v06", "txt": "It simply unclogs the toxic build-up stopping your "
     "blood flow."},
    {"v": "v09", "txt": "It melts the invisible blockage choking your blood "
     "supply while you sleep."},
    {"v": "v12", "txt": "It flushes the hidden blockages trapping your blood."},
    {"v": "v05", "txt": "This morning trick flushes out the toxins clogging "
     "your blood vessels."},
    {"v": "v08", "txt": "It flushes the build-up choking your blood flow and "
     "brings back your real size."},
    {"v": "v01", "txt": "This recipe removes the toxic build-up sitting in "
     "your arteries."},
    {"v": "v10", "txt": "It flushes the plaque choking your vessels and forces "
     "the blood back down."},
]

# ⭐ O CONCRETO — o beat que a v1 nao tinha, e o que faz a fala parar de
# flutuar. Numeros, lugares e prazos que a FONTE diz.
PROVAS = [
    {"v": "v11", "txt": "Fifteen seconds in the shower, one ingredient you "
     "already walked past at the supermarket."},
    {"v": "v11", "txt": "Twenty-one days later I was four inches bigger."},
    {"v": "v03", "txt": "I use zero blue pills."},
    {"v": "v05", "txt": "Men are having brutal results in forty-eight hours."},
    {"v": "v01", "txt": "No side effects, no pharmacy."},
    {"v": "v10", "txt": "No blue pills, no pharmacy."},
    {"v": "v06", "txt": "Once the pipes are clear you get maximum size."},
]

CTAS = [
    {"v": "v11", "txt": "Comment recipe, and I will send it to you right now."},
    {"v": "v03", "txt": "Comment recipe, for the step-by-step video."},
    {"v": "v08", "txt": "Comment recipe, and I will send you the step-by-step."},
    {"v": "v01", "txt": "Comment recipe, and I will send you the full video."},
]

IDADES = (64, 65, 66, 67, 72, 74)   # as seis que a fonte diz


# ===========================================================================
# SORTEIO
# ===========================================================================
EIXOS_LEDGER = ("superficie", "hook", "mecanismo", "prova", "cta")


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
    """Uma entrada evitando as ultimas usadas — e CEDE quando nada sobra."""
    livres = [x for x in pool if _chave(x) not in usados]
    return rng.choice(livres or pool)


def _por_id(pool, valor, chave="id"):
    """Aceita o ID OU a entrada ja' resolvida (o painel manda o dicionario)."""
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
    f = dict(enumerate(spec.get("falas", ["", ""])))
    if 0 in quais:
        f[0] = spec["hook"]["txt"].replace("{idade}", str(spec["idade"]))
    if 1 in quais:
        # ⛔⛔ A PROVA ESCOLHE PRIMEIRO, e essa ordem E' O CONSERTO DA v1.
        # Ela e' o beat CONCRETO — `fifteen seconds`, `four inches`,
        # `twenty-one days`, `no pharmacy` — e e' exatamente o que faltava na
        # versao que o operador reprovou por drifting. Medido: com o mecanismo
        # escolhendo primeiro, a prova so' cabia em 26% dos videos, ou seja o
        # antidoto entrava em um a cada quatro.
        # ⭐ Agora o motor sorteia o TRIO INTEIRO entre as combinacoes que
        # cabem nos 25, em vez de escolher em cascata. Quem cede e' o
        # mecanismo, que tem sete redacoes do mesmo sentido; a prova e o CTA
        # nao tem substituto.
        # ⛔ E o trio nao pode trazer um apelido que brigue com o do hook (CT4).
        do_hook = _orgaos(f.get(0) or spec.get("falas", [""])[0])
        trios = [(p, m, c) for p in PROVAS for m in MECANISMOS for c in CTAS
                 if _palavras(p["txt"]) + _palavras(m["txt"])
                 + _palavras(c["txt"]) <= TETO_FALA[2]
                 and len(do_hook | _orgaos(p["txt"]) | _orgaos(m["txt"])
                         | _orgaos(c["txt"])) <= 1]
        if trios:
            p, m, c = rng.choice(trios)
            spec["prova"], spec["mecanismo"], spec["cta"] = p, m, c
            f[1] = " ".join((m["txt"], p["txt"], c["txt"]))
        else:
            # ⚠️ so' acontece se alguem alongar os pools; o video sai sem a
            # prova em vez de sair cortado no render.
            m, c = spec["mecanismo"], spec["cta"]
            spec["prova"] = None
            f[1] = " ".join((m["txt"], c["txt"]))
    return f


def sortear(pagina, rng, ledger, travas=None):
    travas = travas or {}
    hist = (ledger or {}).get(pagina, {})
    spec = {
        "pagina": pagina,
        "etnia": ETNIA.get(pagina, "white American"),
        "idade": rng.choice(IDADES),
        "superficie": (_por_id(SUPERFICIES, travas["superficie"])
                       if travas.get("superficie")
                       else _fresco(SUPERFICIES,
                                    hist.get("superficie", [])[-6:], rng)),
        "hook": (_por_id(HOOKS, travas["hook"], "v") if travas.get("hook")
                 else _fresco(HOOKS, hist.get("hook", [])[-5:], rng)),
        "mecanismo": _fresco(MECANISMOS, hist.get("mecanismo", [])[-3:], rng),
        "cta": _fresco(CTAS, hist.get("cta", [])[-2:], rng),
    }
    spec["falas"] = [v for _, v in sorted(_falas(spec, rng).items())]
    return spec


# ⛔⛔ O APELIDO SE RESOLVE NA ESCOLHA, NUNCA NA REESCRITA.
# O CT4 quer UM apelido do orgao por video. A tentacao e' normalizar o texto
# depois de montado — e eu tentei: **quebrou o verbatim**, que e' a unica
# guarda desta versao contra o drifting que reprovou a v1. Medido: 5 beats
# deixaram de casar com a fonte no mesmo instante.
# ⭐ Entao quem cede e' o SORTEIO: o motor so' combina beats cujos apelidos ja'
# concordam. Custa candidatos, nao custa uma palavra da fonte.
_RX_ORGAO = re.compile(
    r"\b(%s)\b" % "|".join(re.escape(n) for n in sorted(NUCLEO, key=len,
                                                        reverse=True)), re.I)


def _orgaos(txt):
    return {m.group(0).lower() for m in _RX_ORGAO.finditer(txt or "")}


def nova_fala(spec, i, rng):
    if i == 0:
        spec["hook"] = _fresco(HOOKS, [spec["hook"]["v"]], rng)
    else:
        spec["mecanismo"] = _fresco(MECANISMOS, [spec["mecanismo"]["v"]], rng)
        spec["cta"] = _fresco(CTAS, [spec["cta"]["v"]], rng)
    return _falas(spec, rng, quais=(i,))[i]


# ===========================================================================
# MONTAGEM
# ===========================================================================
def montar(spec):
    s = spec["superficie"]
    b = {}
    b["BLOCO 0 (REF)"] = (
        "REF 01: Photo of a real person's hands, %s. Plain neutral gray "
        "background, soft even frontal light, no objects. Slight sensor grain, "
        "raw iPhone photo aesthetic. No subtitles, no captions, no burned-in "
        "text, no watermark." % MAOS)

    # ⚠️ A ORDEM DAS FRASES E' GRAMATICA, nao estilo. A primeira montagem
    # colava `Resting on {sup} are {PROPS}` — e como varias superficies terminam
    # numa oracao subordinada (`..., grout lines crossing it`), o verbo caia
    # depois dela e a frase virava lixo. Aqui os PROPS vem primeiro e a
    # superficie entra por `on`, que aceita qualquer cauda.
    b["IMAGE 01/02"] = (
        "IMAGE 01/02: Inside %s. On %s stand %s. %s. In frame are %s. %s. "
        "%s. %s"
        % (s["amb"], s["sup"], PROPS, _cap(GESTO_IMG), MAOS, CAMERA,
           _cap(LUZ), CAUDA))

    # ⭐ O take 2 e' o MESMO quadro com a substancia transformada. Nada mais
    # muda — e' o payoff da fonte, e e' a coisa mais barata de manter coerente.
    # ⚠️ Aqui o repeat usa `PROPS_CURTO`: repetir a lista inteira produzia
    # `The same an open cobalt-blue jar...`, com artigo dobrado.
    b["IMAGE 02/02"] = (
        "IMAGE 02/02: Inside %s, the same place in the same framing. On %s, "
        "%s. %s are still in frame beside it. In frame are %s. %s. %s. %s"
        % (s["amb"], s["sup"], PAYOFF_IMG, _cap(PROPS_CURTO), MAOS, CAMERA,
           _cap(LUZ), CAUDA))

    b["TAKE 01/02"] = (
        "TAKE 01/02: Animate the provided image exactly. %s. The camera does "
        "not move and there are no cuts. %s. Audio: %s. Only he speaks.\n"
        'Dialogue: "%s"' % (CAMERA, GESTO_TAKE, s["audio"], spec["falas"][0]))

    b["TAKE 02/02"] = (
        "TAKE 02/02: Animate the provided image exactly. %s. The camera does "
        "not move and there are no cuts. The foam settles very slightly and no "
        "hand enters the frame. Audio: %s. Only he speaks.\n"
        'Dialogue: "%s"' % (CAMERA, s["audio"], spec["falas"][1]))

    return sc.selar_takes(sc.selar_tags(b))


# ===========================================================================
# AS LENTES — cinco, e cada uma guarda um dos defeitos que reprovaram a v1
# ===========================================================================
def _vi1_copy_com_origem(spec, blocos, ach):
    """⛔⛔ TODA FALA TEM DE SER VERBATIM DA FONTE.

    E' a lente central desta reconstrucao. Na v1 eu gerei 224 falas e o
    operador reprovou por drifting; aqui cada beat carrega o `v` do video de
    onde saiu e esta lente confere que o que chegou a fala sao mesmo os beats
    do pool. Copy nova sem origem acusa aqui, no sorteio, e nao no render.
    """
    origem = {h["txt"].replace("{idade}", str(spec["idade"])) for h in HOOKS}
    if spec["falas"][0] not in origem:
        ach.append(("ERRO", "VI1: a fala 1 nao e' verbatim de nenhum video da "
                            "fonte — copy sem origem foi o que reprovou a v1"))
    for beat in (spec["mecanismo"], spec.get("prova"), spec["cta"]):
        if beat and beat["txt"] not in spec["falas"][1]:
            ach.append(("ERRO", "VI1: o beat %s nao chegou a fala 2" % beat["v"]))


def _vi2_um_eixo(spec, blocos, ach):
    """⛔ A SUPERFICIE E' O UNICO EIXO VISUAL, e os props sao CONSTANTES.

    Se um quadro sair sem a superficie sorteada ou sem os props travados, o
    motor voltou a ser o da v1: elementos soltos e nenhum lugar.
    """
    # ⚠️ O take 2 e' cobrado pela forma CURTA: repetir a lista inteira ali
    # produzia artigo dobrado (`The same an open cobalt-blue jar...`). A lente
    # acompanha o texto que existe, e nao o que eu gostaria que existisse.
    # ⚠️ `_cap` maiusculiza a inicial no bloco, entao a lente compara a forma
    # CAPITALIZADA. Comparar a crua reprovava 600 de 600 — lente que acusa o
    # proprio formato de saida e' ruido, e ruido treina o operador a ignorar.
    for k, esperado in (("IMAGE 01/02", PROPS),
                        ("IMAGE 02/02", _cap(PROPS_CURTO))):
        if spec["superficie"]["sup"] not in blocos[k]:
            ach.append(("ERRO", "VI2: %s sem a superficie sorteada" % k))
        if esperado not in blocos[k]:
            ach.append(("ERRO", "VI2: %s sem os props travados — na fonte eles "
                                "sao CONSTANTES, nao opcionais" % k))


def _vi3_continuidade(spec, blocos, ach):
    """Sem rosto, as MAOS e o LUGAR sao a unica ancora entre os dois takes."""
    for k in ("IMAGE 01/02", "IMAGE 02/02"):
        if MAOS not in blocos[k]:
            ach.append(("ERRO", "VI3: %s sem a ancora das maos" % k))
    if spec["superficie"]["amb"] not in blocos["IMAGE 02/02"]:
        ach.append(("ERRO", "VI3: o take 2 nao acontece no mesmo lugar"))


def _vi4_orcamento(spec, blocos, ach):
    for i, fala in enumerate(spec["falas"], 1):
        n = _palavras(fala)
        if n > TETO_FALA[i]:
            ach.append(("ERRO", "VI4: cena %d com %d palavras (teto %d) — a "
                                "fala volta cortada do render"
                        % (i, n, TETO_FALA[i])))
        if n < PISO_FALA[i]:
            ach.append(("AVISO", "VI4: cena %d com so' %d palavras" % (i, n)))


def _vi5_fala_no_take(spec, blocos, ach):
    """A fala chega VERBATIM a linha Dialogue: — copy nao se reescreve no meio."""
    for i, k in enumerate(("TAKE 01/02", "TAKE 02/02")):
        if ('Dialogue: "%s"' % spec["falas"][i]) not in blocos[k]:
            ach.append(("ERRO", "VI5: a fala %d nao chega verbatim ao %s"
                        % (i + 1, k)))


def _ct16(spec, blocos, ach):
    """O contrato 16s, com as duas excecoes deste angulo.

    ⛔ CT4b desligado: os apelidos sao os da FONTE (`baseball bat`, `pipes`).
    ⛔ CT5 desligado, e essa e' a licao da v1: aqui a moeda do comentario e' o
    PASSO A PASSO, nao a receita. O video diz o QUE, a DM diz o COMO — e a
    fonte converte assim. Foi PROIBIR o concreto que produziu o drifting.
    """
    fora = []
    sc.lint_copy16(sys.modules[__name__], spec, fora)
    ach.extend(x for x in fora if not x[1].startswith(("CT4b:", "CT5:")))


def _anticeleb(spec, blocos, ach):
    sc.lint_anticeleb(blocos, ach)


def _painel(spec, blocos, ach):
    sc.lint_painel_honesto(sys.modules[__name__], spec, blocos, ach)


def lint(spec, blocos):
    return sc.lint_curto(
        sys.modules[__name__], spec, blocos, (1, 2), TETO_FALA,
        literais=("recipe",), cota_min=0,
        extras=(_ct16, _anticeleb, _painel, _vi1_copy_com_origem, _vi2_um_eixo,
                _vi3_continuidade, _vi4_orcamento, _vi5_fala_no_take))


# ===========================================================================
# RESUMO E PAINEL
# ===========================================================================
def resumo_pt(spec):
    s = spec["superficie"]
    return ("16s, DOIS takes, POV sem rosto. O LUGAR: %s (%s da fonte). "
            "Take 1 — o dedo mistura o po da gelatina dentro do pote de pomada "
            "azul, com a regua e a placa `growth hack` parados ao lado. "
            "Take 2 — o MESMO quadro com a mistura virada ESPUMA na borda. "
            "Homem de %d anos, %s. Beats: hook %s · mecanismo %s · prova %s · "
            "CTA %s, todos verbatim da fonte. Fecha em `recipe`."
            % (s["curto"], s["v"], spec["idade"], spec["etnia"],
               spec["hook"]["v"], spec["mecanismo"]["v"],
               spec["prova"]["v"] if spec.get("prova") else "—",
               spec["cta"]["v"]))


EIXOS_UI = [
    ("superficie", "O LUGAR", "SUPERFICIES", "curto"),
    ("hook", "O HOOK", "HOOKS", "v"),
]
EIXOS_TRAVAVEIS = ["superficie", "hook"]
DROPDOWNS_UI = [("superficie", "O LUGAR", "SUPERFICIES", "curto")]
IGNORA_PAINEL = ("hook",)


# ===========================================================================
# AUTOTESTE
# ===========================================================================
def _autoteste(n=400, seed=20260815):
    rng = random.Random(seed)
    led, erros = {}, collections.Counter()
    vistos = collections.Counter()
    falas = {1: set(), 2: set()}
    pal = {1: [], 2: []}
    sem_origem = 0
    com_prova = 0
    for _ in range(n):
        sp = sortear("joe", rng, led)
        _anotar(led, sp)
        bl = montar(sp)
        for nivel, txt in lint(sp, bl):
            if nivel == "ERRO":
                erros[txt.split(":")[0]] += 1
        vistos[sp["superficie"]["id"]] += 1
        com_prova += bool(sp.get("prova"))
        for i in (1, 2):
            falas[i].add(sp["falas"][i - 1])
            pal[i].append(_palavras(sp["falas"][i - 1]))
        # ⭐ O CONTROLE QUE A v1 NAO TINHA: 100% do texto falado tem origem.
        beats = [sp["hook"], sp["mecanismo"], sp["cta"]]
        if sp.get("prova"):
            beats.append(sp["prova"])
        junto = " ".join(sp["falas"])
        for b in beats:
            if b["txt"].replace("{idade}", str(sp["idade"])) not in junto:
                sem_origem += 1

    print("%s — %d sorteios (seed %d)" % (APP, n, seed))
    print("  lugares: %d de %d alcancados · min %dx · max %dx"
          % (len(vistos), len(SUPERFICIES), min(vistos.values()),
             max(vistos.values())))
    for i in (1, 2):
        print("  cena %d: %3d falas distintas · palavras %d/%d/%d"
              % (i, len(falas[i]), min(pal[i]), sum(pal[i]) // len(pal[i]),
                 max(pal[i])))
    print("  o beat CONCRETO (prova) entra em %d%% dos videos"
          % (100 * com_prova // n))
    print("  beats sem origem na fonte: %d  %s"
          % (sem_origem, "(toda fala e' verbatim)" if not sem_origem
             else "<-- FALHA"))
    print("  pools: %d lugares · %d hooks · %d mecanismos · %d provas · %d CTAs"
          % (len(SUPERFICIES), len(HOOKS), len(MECANISMOS), len(PROVAS),
             len(CTAS)))
    print("  linter: %d ERRO" % sum(erros.values()))
    for k, v in erros.most_common(8):
        print("     %4dx %s" % (v, k))
    return sum(erros.values()) + sem_origem


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
