#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE GOOD 16 — o casal na agua · 2 takes de 8s = 16 segundos.

⭐⭐ O PRIMEIRO ANGULO EM QUE O HOMEM FALA E A MULHER E' MUDA. Os outros vinte
tem narradora. Aqui a inversao e' o ativo: quem promete e' o corpo que ja'
entregou, e a prova social esta' encostada nele, sem dizer palavra.

Doutrina completa em `../AGENTE_ED_GOOD_V1.md`, destilada da leitura otica a
1 fps de CINCO reels (2026-08-09): `agenteGOOD.mp4`, `agenteGOOD2.mp4`,
`prep1.mp4`, `prep2.mp4`, `prep3.mp4`.

⭐ TOGGLE DE ENQUADRAMENTO — os cinco reels tem A MESMA COPY, palavra por
palavra. O que muda e' so' o quadro, e por isso e' toggle e nao agente novo:

    casal na agua   ele + ela na jacuzzi, corpo inteiro, ele fala na lente
    so as maos      macro na bancada do banheiro, NENHUM rosto, nenhuma mulher

⛔ REGRAS QUE NASCEM COM O AGENTE
  · o CTA e' `gelatin`, nunca `recipe` (a fonte pede recipe; a automacao de DM
    casa palavra EXATA e o funil inteiro roda em gelatin)
  · o `follow` vem em FRASE SEPARADA, nunca colado na keyword
  · a fala e' sobre o CORPO (`harder and stronger`), nunca sobre o orgao —
    verbo de ereccao e' lido como tumescencia e reprova (licao paga em campo
    no COLO 16, 2026-08-09)

    python funil-organico/good16_short_app.py
"""

import argparse
import json
import os
import random
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
if AQUI not in sys.path:
    sys.path.insert(0, AQUI)

import short_comum as sc                                        # noqa: E402
from nucleo_sonoro import sonorizar                             # noqa: E402

# ⛔ Os apelidos do orgao. Este agente NAO os usa na fala (ver GO1) — a lista
# existe para a lente conseguir PROIBI-LOS.
NUCLEO = ["Johnson", "pecker", "wiener", "soldier", "tool"]

LEDGER = os.path.join(AQUI, ".good-16-ledger.json")

TITULO = "AGENTE GOOD 16"
SLUG = "good-16"
SUBTITULO = ("2 takes de 8s = 16 segundos · o casal na agua · o homem fala e "
             "ela e' muda · toggle: casal na agua / so as maos")

CENAS_UI = ["1 · O AVISO", "2 · O CORPO + CTA"]

# ⛔⛔ DUAS CENAS no teto FISICO de 25 palavras (8s a ~3,1 p/s).
# ⚠️ A fonte e' um PLANO UNICO de 13-20s. O corte em dois takes de 8s nao
# existe nela — e' a nossa adaptacao ao AdBatch Vertical 2. Os dois takes
# acontecem no MESMO quadro: o que muda entre eles e' o sache subindo.
TETO_FALA = {1: 25, 2: 25}
PISO_FALA = {1: 16, 2: 18}

# ⛔ Congruencia inviolavel: a etnia do REF casa com a etnia do avatar da
# pagina. ⭐ Neste angulo o REF que fala e' o HOMEM — entao a pagina governa
# ELE, e a mulher fica solta (ordem do operador, 2026-08-09).
ETNIA = {
    "roy": "white American", "dean": "white American",
    "earl": "white American",
    "jason": "Black American", "philippe": "Black American",
    "joe": "white American", "ray": "white American", "matt": "white American",
    "marcus": "Black American", "chuck": "Black American",
}

# ⭐ QUEM NARRA — este e' o unico agente do parque com narrador HOMEM.
SEXOS = ("homem",)

# ⛔ SEM MODO BELA aqui: o modo dela nao existe porque ela nao fala e nao
# conduz. O que existe e' o MODO MUSCULOSO, que e' dele — ver §5 da doutrina.
MODO_BELA = False
MODO_MUSCULOSO = True


# ===========================================================================
# ⭐⭐ MUNDOS — arquetipos AQUATICOS por regiao dos EUA
# ===========================================================================
# ⛔ Ordem do operador, 2026-08-09: *"sempre voltado pra piscina, jacuzzi, por
# favor, nicho de verao"*. Nao ha' mundo seco neste agente.
# ⭐ Cada entrada arrasta CENARIO + LUZ + AUDIO + TRAJE DELA, nunca so' o
# fundo — e' a mecanica de `variar etnia = arrastar o mundo`, aqui aplicada ao
# corpo dele: e' a agua que autoriza o tronco nu.
MUNDOS = [
    {"id": "georgia_deck", "regiao": "georgia",
     "cen": "a cedar-plank deck behind a Georgia ranch house, tall pines "
            "crowding the far edge of the yard",
     "agua": "a round wooden hot tub set into the deck, the water moving",
     "luz": "late afternoon sun coming in low and warm through the pines",
     "audio": "cicadas, water moving in the tub, a distant lawnmower",
     "dela": "a white bikini top"},
    {"id": "texas_quintal", "regiao": "texas",
     "cen": "a Texas backyard with a plank fence and dry St. Augustine grass",
     "agua": "a rectangular concrete pool with a tiled lip",
     "luz": "high midday sun, hard light and short shadows",
     "audio": "a window unit humming, water lapping the tile, far traffic",
     "dela": "a coral bikini top"},
    {"id": "florida_borda", "regiao": "florida",
     "cen": "a Florida patio with screened lanai posts and palms behind",
     "agua": "an infinity-edge pool with water spilling over the near lip",
     "luz": "bright overcast, soft even light off the water",
     "audio": "water spilling over the edge, a mockingbird, a pool pump",
     "dela": "a turquoise bikini top"},
    {"id": "arizona_adobe", "regiao": "arizona",
     "cen": "an Arizona yard with ochre adobe walls and a saguaro past the wall",
     "agua": "a small plunge pool with dark plaster and a stone coping",
     "luz": "flat desert glare, the light bouncing white off the wall",
     "audio": "dry wind, water moving, a dove somewhere",
     "dela": "a black bikini top"},
    {"id": "michigan_cabana", "regiao": "michigan",
     "cen": "a Michigan cabin porch with a rail of peeled logs, birch behind",
     "agua": "a square hot tub on the porch boards, steam off the surface",
     "luz": "cool overcast morning light, steam catching it",
     "audio": "steam and jets, wind in the birches, a loon far off",
     "dela": "a navy bikini top"},
    {"id": "california_bungalow", "regiao": "california",
     "cen": "a Southern California yard with a low stucco wall and a lemon tree",
     "agua": "a kidney-shaped pool with pale blue plaster",
     "luz": "golden hour, long warm light across the water",
     "audio": "water moving, a distant freeway, a wind chime",
     "dela": "a white halter bikini top"},
    {"id": "carolina_lago", "regiao": "carolinas",
     "cen": "a Carolina lake dock of grey weathered boards, water past it",
     "agua": "a hot tub set at the end of the dock, the lake behind it",
     "luz": "hazy afternoon light off the lake",
     "audio": "water against the dock posts, crickets, a far outboard motor",
     "dela": "a red bikini top"},
    {"id": "vegas_quintal", "regiao": "vegas",
     "cen": "a Nevada backyard with crushed-rock landscaping and a block wall",
     "agua": "a small rectangular pool with a raised spa spilling into it",
     "luz": "hard low sun late in the day, the wall glowing warm",
     "audio": "the spa spillover, dry air, a distant highway",
     "dela": "a lime bikini top"},
]

# ===========================================================================
# O HOMEM — quem fala. ⛔ etnia TRAVADA na pagina.
# ===========================================================================
# ⛔⛔ O CORPO E' O ARGUMENTO. Sem os bracos e as veias a fala vira promessa
# vazia — invariante medida 2/2 na fonte. E a ALIANCA importa: a fala e' *"se
# voce tem esposa"*.
HOMENS = [
    {"id": "grisalho_curto",
     "marca": "close-cropped grey hair and a full grey beard"},
    {"id": "careca_cavanhaque",
     "marca": "a clean-shaven scalp and a short grey goatee"},
    {"id": "grisalho_tempos",
     "marca": "short salt-and-pepper hair and a trimmed grey beard"},
    {"id": "barba_cheia",
     "marca": "grey hair receding at the temples and a full white beard"},
    {"id": "bigode_grisalho",
     "marca": "close-cropped grey hair and a thick grey moustache"},
    {"id": "grisalho_ondulado",
     "marca": "short wavy grey hair and a close grey beard"},
]

CORPOS_H = [
    "heavy through the shoulders, thick arms with the veins standing out on "
    "the forearms",
    "broad-chested and thick-armed, the veins showing along both forearms",
    "solid through the chest and shoulders, forearms corded and veined",
    "wide-shouldered with heavy upper arms and visible forearm veins",
    "thick through the neck and shoulders, heavy veined forearms",
    "densely built through the chest, the veins standing up on his arms",
]

# ===========================================================================
# A MULHER — ⭐ etnia SOLTA (ordem do operador). Ela e' MUDA.
# ===========================================================================
# ⛔ A LEI DO REF vale para ela: 25-35, sempre bonita, zero oculos, zero
# grisalho, zero pele castigada.
# ⛔ E ela e' MUDA. Invariante 2/2 na fonte, nao estilo.
MULHERES = [
    {"id": "loira_longa", "etnia": "white American",
     "marca": "long blonde hair, wet at the ends, and a small beauty spot "
              "above her lip"},
    {"id": "ruiva_ondulada", "etnia": "white American",
     "marca": "wavy auburn hair pushed back wet and a dense spray of freckles"},
    {"id": "morena_lisa", "etnia": "white American",
     "marca": "dark brown hair slicked back wet and a small scar through one "
              "eyebrow"},
    {"id": "tranca_lateral", "etnia": "Black American",
     "marca": "long box braids gathered over one shoulder and high cheekbones"},
    {"id": "cacheada_curta", "etnia": "Black American",
     "marca": "a short wet curly afro and a small gold nose stud"},
    {"id": "tranca_longa", "etnia": "Black American",
     "marca": "waist-length braids wet to the ends and a beauty spot on her "
              "cheek"},
    {"id": "latina_ondulada", "etnia": "Latina American",
     "marca": "long wavy black hair wet at the ends and a small mole by her eye"},
    {"id": "asiatica_lisa", "etnia": "Asian American",
     "marca": "straight black hair slicked back wet and a faint scar on her chin"},
]

# ===========================================================================
# O SACHE e o POST-IT
# ===========================================================================
# ⛔ Ordem do operador: *"seja fiel ao video original: aparecendo gelatin
# legivel e escrito"*. No mundo aquatico o sache e' laminado, que e' o que
# sobrevive a' agua sem contradizer a cena.
# ⚠️ EXCECAO DECLARADA na trava `No on-screen text`: a palavra esta' no
# OBJETO, nao queimada na tela pelo gerador. A trava segue valendo para
# legenda, marca d'agua e texto de interface.
SACHE = ("a small foil sachet with the word GELATIN printed across the front "
         "in plain black letters, held between his thumb and fingers")

# ⭐ O POST-IT so' existe no enquadramento `so as maos` — e' o unico elemento
# do quadro que nomeia o assunto sem a fala.
# ⛔ Rotulos SUGESTIVOS, nunca explicitos: palavra anatomica num post-it
# legivel e' superficie de bloqueio sem funcao.
POSTITS = [
    "GROWTH TRICK",
    "HARD AGAIN",
    "FIRM TRICK",
    "BLOOD FLOW",
    "THE FIX",
    "NIGHT FIX",
]

# ⭐ A bancada do banheiro — o mundo do enquadramento `so as maos`.
BANCADAS = [
    {"id": "azulejo_branco",
     "cen": "a home bathroom counter of pale laminate, small white square "
            "tiles on the wall behind"},
    {"id": "granito_cinza",
     "cen": "a home bathroom counter of speckled grey granite, a mirror edge "
            "showing at the top of the frame"},
    {"id": "marmore_creme",
     "cen": "a home bathroom counter of cream marble, a cabinet door with a "
            "brushed handle below"},
    {"id": "laminado_bege",
     "cen": "a plain beige laminate bathroom counter with a rounded front edge"},
]

# ⚠️ Sempre GENERICO e sem marca legivel — a fonte mostra `Colgate` e aqui
# sai, pela regra de embalagem sem marca (BOTICA).
CLUTTER = [
    "a plain toothpaste tube, an unlabelled pump bottle of hand soap and a "
    "toothbrush in a cup",
    "two unlabelled tubes lying on their sides and a pump bottle of soap",
    "an unlabelled soap dispenser, a folded hand towel and a toothbrush cup",
    "a plain white tube, a small unlabelled jar and a toothbrush in a holder",
]


# ===========================================================================
# ⭐⭐ A COPY — o arco medido nos CINCO reels, quase palavra por palavra
# ===========================================================================
# ⛔⛔ A FALA E' SOBRE O CORPO, NUNCA SOBRE O ORGAO. A fonte diz `your body
# harder and stronger` — e essa e' a razao pela qual este angulo e' mais
# seguro que os outros na moderacao. Verbo que descreve o orgao voltando a
# funcionar e' lido como tumescencia; o COLO 16 pagou ~95% de recusa por isso
# em 2026-08-09.
# ⛔ Nao introduzir `{o}` nesta copy. Nao e' esquecimento, e' a defesa.

# cena 1 = AVISO + A ESPOSA + ELA NAO AGUENTA
AVISOS = [
    "If you are single, stay away from this.",
    "If you are single, do not try this.",
    "If you are single, this is not for you.",
    "If you are single, do not touch this.",
    "If you are single, skip this one.",
    "Single men, this is not for you.",
]

ESPOSAS = [
    "And if you have a wife, be very careful.",
    "If you are married, be very careful with this.",
    "If you are married, use it carefully.",
    "If you are married, thank me later.",
    "If you have a wife, go easy with it.",
    "Married men, use this with caution.",
]

# ⛔ E' o beat que faz o video existir: a promessa vem da MULHER nao dar conta,
# nao de uma afirmacao sobre o corpo do espectador.
AGUENTAM = [
    "She will not handle you.",
    "She will not be able to keep up.",
    "She will not keep up with you.",
    "Your wife will not keep up.",
    "She is not going to keep up.",
]

# cena 2 = O CORPO + PRECO + CTA + FOLLOW
# ⛔⛔ O ORCAMENTO DA CENA 2 E' DE 25 PALAVRAS E ELE MANDA. A primeira versao
# destes pools somava 31 no MINIMO — zero combinacoes validas, e o [ALCANCE] do
# autoteste acusou QUATRO pools 100% mortos. E' a licao §36 do repo, cometida
# por mim de novo na estreia do agente.
# ⚠️ Quem encolheu foi o PRECO: e' o beat mais dispensavel dos quatro (a fonte
# so' o traz em dois dos cinco reels) e o unico que nao carrega promessa nem
# comando.
CORPOS_FALA = [
    "This leaves your body harder and stronger than in years.",
    "This makes your body harder and stronger than in years.",
    "This leaves your body harder than it has felt in decades.",
    "This has your body harder and stronger than in years.",
    "This mixture leaves your body harder and stronger.",
    "This leaves your body stronger than it has felt in years.",
]

PRECOS = [
    "Costs almost nothing.",
    "Costs next to nothing.",
    "And it costs almost nothing.",
    "The price is almost nothing.",
]

# ⛔⛔ A fonte pede `recipe`. NAO COPIAMOS: a automacao de DM casa palavra
# EXATA e o funil inteiro roda em `gelatin`.
CTAS = [
    "%s and I'll send you the recipe." % sc.CTA_LITERAL,
    "%s and I'll send the recipe tonight." % sc.CTA_LITERAL,
    "%s and I'll send you the full recipe." % sc.CTA_LITERAL,
    "%s and I'll send the whole recipe." % sc.CTA_LITERAL,
    "%s and I'll send you the recipe tonight." % sc.CTA_LITERAL,
]

# ⛔ FRASE SEPARADA, sempre. Colado na keyword, o comentario do espectador sai
# com duas palavras e a automacao nao dispara.
# ⚠️ 2-6 palavras, e o teto REAL deste beat e' 6 — o [ALCANCE] do autoteste
# mediu. `Follow me so I can reach you` tem 7 e nunca era sorteado: nao era
# raro, era MORTO, e o pool contava como opcao viva.
FOLLOWS = [
    "Follow me first.",
    "Follow me so it reaches you.",
    "Follow me, then comment.",
    "Follow first.",
    "Follow me, or nothing sends.",
    "Follow me or it won't send.",
]


# ===========================================================================
# HELPERS
# ===========================================================================

def _palavras(s):
    return len(re.findall(r"[A-Za-z']+", s or ""))


def _carregar_ledger():
    if os.path.exists(LEDGER):
        with open(LEDGER, encoding="utf-8-sig") as f:
            return json.load(f)
    return {}


EIXOS_LEDGER = ("mundo", "homem", "mulher", "bancada")


def _anotar(ledger, spec):
    p = ledger.setdefault(spec["pagina"], {})
    for eixo in EIXOS_LEDGER:
        if spec.get(eixo):
            p.setdefault(eixo, []).append(spec[eixo]["id"])
            p[eixo] = p[eixo][-12:]


def _gravar_ledger(ledger, spec):
    _anotar(ledger, spec)
    with open(LEDGER, "w", encoding="utf-8") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)


def _fresco(pool, usados, rng):
    livres = [x for x in pool if x["id"] not in usados]
    return rng.choice(livres or pool)


def _por_id(pool, valor):
    return next((x for x in pool if x["id"] == valor), None)


def _cabe(pool, reserva, cena):
    """As entradas que cabem depois de reservar `reserva` palavras.

    ⚠️ O fallback nao devolve o pool inteiro — isso e' estouro silencioso.
    Devolve a entrada mais CURTA, e quem reclama e' o linter.
    """
    v = [x for x in pool if _palavras(x) + reserva <= TETO_FALA[cena]]
    return v or [min(pool, key=_palavras)]


def _rsv(vals):
    v = sorted(vals)
    return v[len(v) // 2]


# ===========================================================================
# SORTEIO
# ===========================================================================

ENQUADRAMENTOS = ("casal na agua", "so as maos")


def _falas(spec, rng, quais=(0, 1)):
    """As duas falas.

    ⛔⛔ QUEM ESCOLHE PRIMEIRO RESERVA O MINIMO; QUEM ESCOLHE NO MEIO RESERVA A
    MEDIANA. Regra medida no ESCANDALO 16, dos dois defeitos opostos: com o
    minimo em todos o ULTIMO beat fica preso; com a mediana em todos o
    PRIMEIRO fica preso.
    """
    f = dict(enumerate(spec.get("falas", ["", ""])))

    if 0 in quais:
        _mn_e = min(_palavras(x) for x in ESPOSAS)
        _mn_a = min(_palavras(x) for x in AGUENTAM)
        av = rng.choice(_cabe(AVISOS, _mn_e + _mn_a, 1))
        es = rng.choice(_cabe(ESPOSAS,
                              _palavras(av)
                              + _rsv([_palavras(x) for x in AGUENTAM]), 1))
        ag = rng.choice(_cabe(AGUENTAM, _palavras(av) + _palavras(es), 1))
        f[0] = "%s %s %s" % (av, es, ag)

    if 1 in quais:
        _mn_p = min(_palavras(x) for x in PRECOS)
        _mn_c = min(_palavras(x) for x in CTAS)
        _mn_f = min(_palavras(x) for x in FOLLOWS)
        co = rng.choice(_cabe(CORPOS_FALA, _mn_p + _mn_c + _mn_f, 2))
        pr = rng.choice(_cabe(PRECOS,
                              _palavras(co) + _mn_c
                              + _rsv([_palavras(x) for x in FOLLOWS]), 2))
        ct = rng.choice(_cabe(CTAS,
                              _palavras(co) + _palavras(pr)
                              + _rsv([_palavras(x) for x in FOLLOWS]), 2))
        fo = rng.choice(_cabe(FOLLOWS,
                              _palavras(co) + _palavras(pr) + _palavras(ct), 2))
        f[1] = "%s %s %s %s" % (co, pr, ct, fo)

    return f


def sortear(pagina, rng, ledger, travas=None):
    travas = travas or {}
    hist = (ledger or {}).get(pagina, {})
    etnia = ETNIA.get(pagina, "white American")

    enq = travas.get("enquadramento") or rng.choice(ENQUADRAMENTOS)

    mundo = (_por_id(MUNDOS, travas["mundo"]) if travas.get("mundo")
             else _fresco(MUNDOS, hist.get("mundo", [])[-4:], rng))
    homem = (_por_id(HOMENS, travas["homem"]) if travas.get("homem")
             else _fresco(HOMENS, hist.get("homem", [])[-3:], rng))
    # ⭐ a mulher tem etnia SOLTA — ela nao e' o REF de congruencia
    mulher = (_por_id(MULHERES, travas["mulher"]) if travas.get("mulher")
              else _fresco(MULHERES, hist.get("mulher", [])[-4:], rng))
    bancada = (_por_id(BANCADAS, travas["bancada"]) if travas.get("bancada")
               else _fresco(BANCADAS, hist.get("bancada", [])[-2:], rng))

    spec = {
        "pagina": pagina, "etnia": etnia, "enquadramento": enq,
        "mundo": mundo, "homem": homem, "mulher": mulher, "bancada": bancada,
        "corpo_h": rng.choice(CORPOS_H),
        "postit": rng.choice(POSTITS),
        "clutter": rng.choice(CLUTTER),
    }
    spec["falas"] = [v for _, v in sorted(_falas(spec, rng).items())]
    return spec


def nova_fala(spec, i, rng):
    return _falas(spec, rng, quais=(i,))[i]


# ===========================================================================
# MONTAGEM
# ===========================================================================

CAUDA = ("Shot on iPhone, natural grain. No on-screen text, no subtitles, no "
         "captions, no watermark.")

# ⛔ ANTICELEB — nunca declarar conformidade ("not a celebrity" e' municao).
# ⚠️ Aqui a frase existe porque o BLOCO 0 do repo inteiro a carrega e o
# gerador a espera; o que se proibe e' INVENTAR declaracao nova.
ANTICELEB = ("An ordinary everyday relatable person with a plain unremarkable "
             "face, not a celebrity, not a model, not an actor.")


def montar(spec):
    m, h, w = spec["mundo"], spec["homem"], spec["mulher"]
    et, enq = spec["etnia"], spec["enquadramento"]
    b = {}

    # --- BLOCO 0 — a REF e' o HOMEM (ele e' quem fala) ---------------------
    # ⛔ Neste angulo a congruencia de etnia governa ELE, nao ela.
    b["BLOCO 0 (REF)"] = (
        "REF 01: Photo of a real person, a 58-year-old %s man, chest up, "
        "facing the camera directly, calm steady expression. %s, %s, wearing "
        "a gold wedding band. %s Hands out of frame, no objects. Plain neutral "
        "gray background, soft even frontal light. Slight sensor grain, soft "
        "focus, raw iPhone front camera aesthetic. No subtitles, no captions, "
        "no burned-in text, no watermark."
        % (et, h["marca"], spec["corpo_h"], ANTICELEB))

    if enq == "casal na agua":
        # ⭐ Os DOIS takes acontecem no MESMO quadro. A fonte e' plano unico;
        # o que muda entre eles e' o sache subindo na cena 2.
        cena = (
            "Medium shot at %s. %s, sitting in %s with the water at his chest, "
            "shoulders and arms out of the water, %s, %s, a gold wedding band "
            "on his hand, talking straight to camera. Beside him, leaning in "
            "against his shoulder with the water at her chest, is a 30-year-old "
            "%s woman, %s, wearing %s; she looks at the lens and says nothing. "
            "They are the only two people in the frame. %s"
            % (m["cen"], "The same 58-year-old %s man" % et, m["agua"],
               h["marca"], spec["corpo_h"], w["etnia"], w["marca"], m["dela"],
               _cap(m["luz"]) + "."))

        b["IMAGE 01/02"] = "IMAGE 01/02: %s His hands are empty and rest on the "\
            "edge in front of him. %s" % (cena, CAUDA)
        b["IMAGE 02/02"] = "IMAGE 02/02: %s In one hand, raised to the height "\
            "of his own chest and clear of the water, he holds %s. %s" \
            % (cena, SACHE, CAUDA)

        mov = ("She stays exactly where she is, leaning against his shoulder, "
               "and she never speaks. Only he speaks. The water keeps moving "
               "the way water moves and nothing else in the frame changes.")
        b["TAKE 01/02"] = (
            "TAKE 01/02: Animate the provided image exactly. Handheld iPhone "
            "shot, very slight natural sway, no cuts, and the camera does not "
            "move. He talks straight into the lens the whole time and his "
            "hands stay where they are. %s\n"
            "Dialogue: \"%s\"\nAudio: %s. No music."
            % (mov, sonorizar(spec["falas"][0]), m["audio"]))
        b["TAKE 02/02"] = (
            "TAKE 02/02: Animate the provided image exactly. Handheld iPhone "
            "shot, very slight natural sway, no cuts, and the camera does not "
            "move. He keeps the sachet at exactly the same height and the same "
            "angle for the whole shot, and the lettering on it stays sharp and "
            "readable. %s\n"
            "Dialogue: \"%s\"\nAudio: %s. No music."
            % (mov, sonorizar(spec["falas"][1]), m["audio"]))
    else:
        # ⭐⭐ SO AS MAOS — nenhum rosto, nenhuma mulher, em nenhum frame.
        # ⛔ Ordem do operador: *"so maos, sem mulher"*.
        bc = spec["bancada"]
        cena = (
            "Overhead medium close shot looking down at %s. In frame are the "
            "hands of a 58-year-old %s man, the skin weathered, a gold wedding "
            "band on one finger; his head and body are out of shot and no face "
            "is in the frame at any point. On the counter, in shot from the "
            "first frame: a clear glass of water with a metal spoon resting "
            "against the rim%s, and a square yellow sticky note lying flat "
            "in the foreground with %s hand-written across it in blue pen. "
            "Further back on the counter: %s. He is the only person in the "
            "frame and no other person appears. %s"
            % (bc["cen"], et, "%s", spec["postit"], spec["clutter"],
               "Flat even bathroom light."))

        b["IMAGE 01/02"] = "IMAGE 01/02: %s His hands rest flat on the counter "\
            "beside the glass. %s" % (cena % "", CAUDA)
        # ⛔⛔ O SACHE SO' ENTRA NA CENA 2 — na primeira versao ele morava
        # na string COMPARTILHADA dos dois IMAGE e vazava para a cena 1. A
        # lente GO4 acusou 191 de 400. Ele e' a UNICA mudanca de estado do
        # plano, e e' isso que da' a batida que a fonte tem.
        b["IMAGE 02/02"] = "IMAGE 02/02: %s One hand is closed around the "\
            "sachet and lifts it slightly clear of the counter. %s" \
            % (cena % (", " + SACHE), CAUDA)

        mov = ("No face enters the frame at any point and no other person "
               "appears. Nothing on the counter is picked up or moved except "
               "what his hands already hold. Only his hands move.")
        for k, i in (("TAKE 01/02", 0), ("TAKE 02/02", 1)):
            b[k] = (
                "%s: Animate the provided image exactly. Handheld iPhone shot, "
                "very slight natural sway, no cuts, and the camera does not "
                "move. %s\nDialogue: \"%s\"\nAudio: a quiet bathroom room "
                "tone, a tap dripping once. No music."
                % (k, mov,
                   sonorizar(spec["falas"][i])))

    return sc.selar_takes(b)


def _cap(s):
    return s[0].upper() + s[1:] if s else s


# ===========================================================================
# LINTER — as regras GO
# ===========================================================================

def _go1_corpo_nao_orgao(spec, blocos, achados):
    """⭐⭐ GO1 — A FALA E' SOBRE O CORPO, NUNCA SOBRE O ORGAO.

    ⛔ E' a defesa central deste angulo. O COLO 16 mediu ~95% de recusa no Veo
    em 2026-08-09 porque a fala nomeava o orgao junto de um verbo de ereccao —
    o classificador le' isso como tumescencia. A fonte deste angulo fala de
    `your body harder and stronger`, e e' por isso que ela passa.
    ⚠️ A lente existe para impedir que alguem "melhore" a copy no futuro
    trazendo o orgao para ca.
    """
    corpo = " ".join(spec["falas"]).lower()
    for n in NUCLEO:
        if n.lower() in corpo:
            achados.append((
                "ERRO",
                "GO1: a fala nomeia o orgao (%r) — este angulo fala do CORPO "
                "(`harder and stronger`), e e' isso que o faz passar na "
                "moderacao onde os outros reprovam" % n))


def _go2_ela_muda(spec, blocos, achados):
    """GO2 — ela nunca fala, e o take tem de DIZER isso.

    ⚠️ Omitir nao basta: o Veo poe as duas bocas a mexer se ninguem proibir, e
    o dialogo dele sai monofonico e torto.
    """
    if spec["enquadramento"] != "casal na agua":
        return
    for k in ("TAKE 01/02", "TAKE 02/02"):
        if "Only he speaks" not in blocos[k]:
            achados.append(("ERRO", "GO2: %s sem `Only he speaks` — sem isso "
                                    "o Veo mexe a boca dela tambem" % k))


def _go3_sem_rosto(spec, blocos, achados):
    """GO3 — no enquadramento `so as maos`, ZERO rosto e ZERO mulher."""
    if spec["enquadramento"] != "so as maos":
        return
    for k in ("IMAGE 01/02", "IMAGE 02/02"):
        if "no face is in the frame" not in blocos[k]:
            achados.append(("ERRO", "GO3: %s nao proibe o rosto — o angulo "
                                    "inteiro depende de nao haver rosto" % k))
    for k in blocos:
        if k.startswith("BLOCO"):
            continue
        if re.search(r"\bwoman\b", blocos[k], re.I):
            achados.append(("ERRO", "GO3: %s traz uma mulher no enquadramento "
                                    "`so as maos` — ordem do operador: so' "
                                    "maos, sem mulher" % k))


def _go4_sache(spec, blocos, achados):
    """GO4 — o sache com GELATIN legivel aparece na cena 2, nunca na 1.

    ⛔ E' a unica mudanca de estado do plano. Se ele ja' estiver na cena 1, o
    video perde a batida que a fonte tem.
    """
    if "GELATIN" in blocos["IMAGE 01/02"]:
        achados.append(("ERRO", "GO4: o sache ja' aparece na cena 1 — ele e' a "
                                "unica mudanca de estado do plano e entra na 2"))
    if "GELATIN" not in blocos["IMAGE 02/02"]:
        achados.append(("ERRO", "GO4: a cena 2 nao tem o sache com GELATIN "
                                "legivel — ordem do operador, fiel a' fonte"))


def _go5_orcamento(spec, blocos, achados):
    for i, fala in enumerate(spec["falas"], 1):
        n = _palavras(fala)
        if n > TETO_FALA[i]:
            achados.append(("ERRO", "GO5: cena %d com %d palavras (teto %d) — "
                                    "a fala e' cortada no render" % (i, n,
                                                                     TETO_FALA[i])))
        if n < PISO_FALA[i]:
            achados.append(("AVISO", "GO5: cena %d com %d palavras (piso %d) — "
                                     "sobra ar morto no take" % (i, n,
                                                                 PISO_FALA[i])))


def _go6_etnia(spec, blocos, achados):
    """GO6 — a congruencia governa O HOMEM, que e' quem fala."""
    et = spec["etnia"]
    for k in ("BLOCO 0 (REF)", "IMAGE 01/02", "IMAGE 02/02"):
        if et not in blocos[k]:
            achados.append(("ERRO", "GO6: %s sem a etnia da pagina (%r) — a "
                                    "congruencia com o avatar sai do video "
                                    "sem ninguem ver" % (k, et)))


def lint(spec, blocos):
    """⚠️ Lint PROPRIO, nao `sc.lint_curto`. Aquele e' da maquinaria de
    colapso 5->3 e pede `base` e `mapa`, que este motor nao tem: ele nao
    deriva de motor longo nenhum."""
    ach = []
    falas = spec["falas"]
    sc.lint_tags(blocos, ach)
    sc.lint_sem_texto(blocos, ach)
    sc.lint_isca_cta(falas[1], ach, "a cena 2 (CTA)")
    sc.lint_cta_literal(falas[1], ach, "a cena 2 (CTA)")
    sc.lint_take_vs_image(blocos, ach)
    for f in (_go1_corpo_nao_orgao, _go2_ela_muda, _go3_sem_rosto,
              _go4_sache, _go5_orcamento, _go6_etnia):
        f(spec, blocos, ach)
    return ach


# ===========================================================================
# PAINEL
# ===========================================================================

EIXOS_UI = [
    ("mundo", "A AGUA", "MUNDOS", "id"),
    ("homem", "QUEM FALA", "HOMENS", "id"),
    ("mulher", "A MULHER", "MULHERES", "id"),
    ("bancada", "A BANCADA", "BANCADAS", "id"),
]

EIXOS_TRAVAVEIS = ["mundo", "homem", "mulher", "bancada", "enquadramento"]

TRAVAS_UI = [("enquadramento", "enquadramento",
              ["livre"] + list(ENQUADRAMENTOS))]


def resumo_pt(spec):
    if spec["enquadramento"] == "casal na agua":
        return ("Homem %s de 58 anos, %s, em %s. Cena 1: maos vazias, ele fala. "
                "Cena 2: ergue o sache GELATIN. Ao lado, mulher %s, muda. "
                "Dois takes de 8s = 16s."
                % (spec["etnia"], spec["homem"]["marca"],
                   spec["mundo"]["regiao"], spec["mulher"]["etnia"]))
    return ("So as maos de um homem %s de 58 anos, sobre %s. Post-it: %s. "
            "Cena 1: maos na bancada. Cena 2: ergue o sache GELATIN. Sem rosto, "
            "sem mulher. Dois takes de 8s = 16s."
            % (spec["etnia"], spec["bancada"]["id"], spec["postit"]))


# ===========================================================================
# AUTOTESTE
# ===========================================================================

def autoteste(n=400):
    import collections
    pags = sorted(ETNIA)
    erros = collections.Counter()
    dist = collections.defaultdict(set)
    enq = collections.Counter()
    falhas, avisos = [], 0

    for i in range(n):
        s = sortear(pags[i % len(pags)], random.Random(i), {})
        enq[s["enquadramento"]] += 1
        for c, f in enumerate(s["falas"], 1):
            dist[c].add(f)
        for nivel, msg in lint(s, montar(s)):
            if nivel == "ERRO":
                erros[msg[:70]] += 1
            else:
                avisos += 1

    print("GOOD 16 — %d sorteios" % n)
    print("  enquadramento: %s" % dict(enq))
    for c in sorted(dist):
        print("  cena %d: %d falas distintas" % (c, len(dist[c])))
    print("  linter: %d ERRO, %d AVISO" % (sum(erros.values()), avisos))
    for k, v in erros.most_common(5):
        print("     %3dx %s" % (v, k))

    # ⭐ [ALCANCE] — entrada que nao cabe com os minimos dos outros beats nunca
    # e' sorteada. Nao e' rara: e' morta, e o autoteste a contava como viva.
    for rot, pool, cena, outros in (
            ("AVISOS", AVISOS, 1, [ESPOSAS, AGUENTAM]),
            ("ESPOSAS", ESPOSAS, 1, [AVISOS, AGUENTAM]),
            ("AGUENTAM", AGUENTAM, 1, [AVISOS, ESPOSAS]),
            ("CORPOS_FALA", CORPOS_FALA, 2, [PRECOS, CTAS, FOLLOWS]),
            ("PRECOS", PRECOS, 2, [CORPOS_FALA, CTAS, FOLLOWS]),
            ("CTAS", CTAS, 2, [CORPOS_FALA, PRECOS, FOLLOWS]),
            ("FOLLOWS", FOLLOWS, 2, [CORPOS_FALA, PRECOS, CTAS])):
        reserva = sum(min(_palavras(x) for x in p) for p in outros)
        mortas = [x for x in pool
                  if _palavras(x) + reserva > TETO_FALA[cena]]
        if mortas:
            falhas.append("[ALCANCE] %s: %d de %d nunca sao sorteadas "
                          "(teto real %d palavras)"
                          % (rot, len(mortas), len(pool),
                             TETO_FALA[cena] - reserva))

    if sum(erros.values()):
        falhas.append("%d ERRO de linter" % sum(erros.values()))
    if falhas:
        print("\nSELF-TEST REPROVADO (%d falha(s)):" % len(falhas))
        for f in falhas:
            print("   " + f)
        return 1
    print("\nAUTOTESTE OK.")
    return 0


def main():
    ap = argparse.ArgumentParser(description=TITULO)
    ap.add_argument("--pagina", choices=sorted(ETNIA), default="joe")
    ap.add_argument("--n", type=int, default=1)
    ap.add_argument("--seed", type=int)
    ap.add_argument("--enquadramento", choices=ENQUADRAMENTOS)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--autoteste", action="store_true")
    a = ap.parse_args()

    if a.autoteste:
        return autoteste()

    led = _carregar_ledger()
    rng = random.Random(a.seed)
    travas = {"enquadramento": a.enquadramento} if a.enquadramento else {}
    for _ in range(a.n):
        s = sortear(a.pagina, rng, led, travas)
        b = montar(s)
        print("=" * 70)
        print(resumo_pt(s))
        print("=" * 70)
        for k in sorted(b):
            print("\n%s\n" % b[k])
        for nivel, msg in lint(s, b):
            print("[%s] %s" % (nivel, msg))
        if not a.dry_run:
            _gravar_ledger(led, s)
    return 0


if __name__ == "__main__":
    sys.exit(main())
