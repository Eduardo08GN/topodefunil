# -*- coding: utf-8 -*-
"""OCTOPUS 5 — a fantasia de polvo, 5 takes de 4s (20s), AdBatch Vertical 5.

⛔⛔ ESTE AGENTE NAO TEM FALA, E ISSO NAO E' ESQUECIMENTO.
   Os dez reels lidos da fonte nao tem uma palavra falada: sao musica mais UMA
   legenda queimada que nao muda do primeiro ao ultimo frame. Por isso aqui
   nao existe pool de dialogo, teto de palavras, transcricao nem karaoke — o
   `captions.transcrever` nao tem o que transcrever. E' a primeira rota do
   parque construida assim, e a diferenca e' da FONTE, nao preferencia.
   ⭐ O ganho: o orcamento inteiro de palavras do prompt vai para camera,
   cena e luz, em vez de dividir com a locucao.

⭐⭐ A FONTE JA' OPERA EM POOL, e foi a leitura otica que provou.
   A cena da manta rosa puxada no quarto aparece IDENTICA, quadro por quadro,
   em pelo menos dois reels (65K e 27K), com legendas diferentes. Nao e'
   enquadramento parecido: e' o mesmo arquivo reaproveitado. Eles recombinam
   um acervo de takes e trocam a legenda. Este motor faz o mesmo, por sorteio.

⛔ NICHO NOVO — NADA DO CONTRATO DE ED VALE AQUI.
   Sem gelatina, sem keyword de DM, sem prop falico, sem CONTRATO-COPY-16S.
   O `lint_copy16` nao roda neste arquivo e nao deve rodar: as sete travas de
   la' falam de orgao, mecanismo e CTA de DM, e nenhuma existe neste angulo.
   O destino do clique e' `nestlingpicks.shop`, pela bio.

FONTE (leitura otica de 2026-09-01)
   Pagina 61593789450554, 10 reels baixados e lidos em folha de contato de 8
   quadros. Duracao de 11,4s a 15,7s. Construcao identica nos dez: 6 a 8
   vinhetas curtas, uma legenda unica segurada o video inteiro, sem fala.
   ⏳ DIVIDA DECLARADA: a grade mostra 17 reels e o DOM so' entregou 10. As
   pools abaixo saem dos dez lidos. Entrada nova sai de LEITURA, nunca de
   invencao.

⚠️ DOIS ACHADOS QUE CONTRARIAM A DECISAO DO OPERADOR, registrados porque sao
   da fonte e nao opiniao:
   1. A fantasia AZUL aparece em metade dos videos, e um take mostra roxa,
      azul e rosa enfileiradas. O operador travou em ROSA (ordem de
      2026-09-01) e e' o que este motor faz. Se um dia a cor virar eixo, a
      leitura ja' esta' feita.
   2. Existe uma cena de PRATEIRA DE LOJA cheia de caixas do produto, com a
      marca deles impressa. E' credibilidade fabricada, nao varejo real. Nao
      foi reproduzida aqui de proposito.

Uso:
    python funil-organico/octopus5.py --n 10
    python funil-organico/octopus5.py --n 5 --seed 42 --dry-run
    python funil-organico/octopus5.py --autoteste
"""

import argparse
import io
import json
import os
import random
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(AQUI, ".octopus-5-ledger.json")
TITULO = "OCTOPUS 5 — 5 takes de 4s, sem fala"

N_TAKES = 5
SEG_POR_TAKE = 4

# ---------------------------------------------------------------------------
# A STRING TRAVADA DO PRODUTO
# ---------------------------------------------------------------------------
# ⛔ NAO REESCREVER. E' a unica continuidade entre cinco quadros gerados em
# sessoes separadas: sem ela a cor muda, o numero de tentaculos muda, e o
# espectador percebe antes de saber o que percebeu. Vai LETRA POR LETRA nos
# cinco IMAGE, e e' a mesma string dos lotes manuais de 31/08.
PRODUTO = ("a pale pink plush octopus costume with eight long soft tentacles "
           "edged in deeper rose pink, a rounded hood with a deep pink lining")

# ⚠️ Ausente de proposito: nome de marca, texto em quadro e qualquer aparelho.
# `shot on a phone` e' descricao de ESTILO; escrever `holding a phone` faz o
# gerador DESENHAR o aparelho — licao paga com um lote inteiro no VICK 16.
ESTILO = "Shot on a phone, natural home photography, slight grain."
ANTI_TEXTO = "No text, no captions, no watermark."
ANTI_TEXTO_TAKE = ("No subtitles, no captions, no burned-in text, "
                   "no on-screen text.")
# ⛔ O negativo dos dez dedos e' o padrao vigente do parque (V4, anti-glitch).
# So' entra em cena com mao humana em quadro — em cena sem gente ele gastaria
# orcamento de palavra a toa.
DEDOS = ("Exactly ten fingers total visible, no extra hands, no extra limbs, "
         "only two arms visible.")


def _cena(ident, cenario, luz, movimento, audio, maos=False):
    return {"id": ident, "cenario": cenario.strip(), "luz": luz.strip(),
            "movimento": movimento.strip(), "audio": audio.strip(),
            "maos": maos}


# ---------------------------------------------------------------------------
# TAKE 1 — A REVELACAO. O gancho: o produto aparece, ainda sem o bebe.
# ---------------------------------------------------------------------------
# ⭐ Todas saem de aberturas reais dos dez reels. A da manta e' a que a fonte
# mais repete, e e' justamente a que ela reaproveita entre videos diferentes.
TAKE1 = [
    _cena(
        "manta_no_quarto",
        "Vertical 9:16 photo of a nursery floor with a pale pink rug. A large "
        "soft mound sits under a pink floral blanket, its shape lumpy and "
        "unreadable. A woman's hand enters from the right and pinches one "
        "corner of the blanket, lifting it a few inches so a single tentacle "
        "of " + PRODUTO + " is just visible underneath. A white crib and a "
        "cream armchair stand behind.",
        "Soft daylight from a window on the left, warm and diffused.",
        "The hand lifts the blanket up and away in one smooth pull, the fabric "
        "sliding off and the costume underneath coming into view. One single "
        "pull, no second gesture.",
        "quiet room tone, soft fabric slide.", maos=True),
    _cena(
        "erguida_no_berco",
        "Vertical 9:16 photo in a nursery, camera low. A woman stands beside a "
        "white crib holding up by the hood " + PRODUTO + ", arms raised so the "
        "tentacles hang and spread wide across the upper half of the frame. "
        "Her face is cropped above the top edge; only her body from the chin "
        "down is visible. A changing table and a stuffed bear sit behind.",
        "Soft daylight from a window on the left, warm and diffused.",
        "She lowers the costume slowly toward the lens, the tentacles swinging "
        "and settling as it comes down.",
        "quiet room tone, faint fabric rustle.", maos=True),
    _cena(
        "pov_sofa",
        "Vertical 9:16 photo from a low reclined angle, as if lying back on a "
        "sofa. In the foreground a woman's legs in dark leggings rest across a "
        "cream sectional. Standing beyond her feet, a man in a plain white "
        "t-shirt holds up toward the lens " + PRODUTO + ", gripping it by the "
        "hood with both hands, tentacles spread across the upper frame. A low "
        "wooden media console and a potted olive tree behind him.",
        "Soft daylight from a large window on the right, warm and diffused.",
        "He lowers the costume toward the lens in one smooth motion, the "
        "tentacles swinging and settling as it comes down.",
        "quiet room tone, faint fabric rustle.", maos=True),
    _cena(
        "caixa_no_chao",
        "Vertical 9:16 photo looking down at a living room floor of pale wood. "
        "An open cardboard shipping box sits slightly off centre, flaps folded "
        "back, torn tape hanging. Spilling out over the near edge and across "
        "the floor toward the lens are two tentacles of " + PRODUTO + ", the "
        "rest still bunched inside the box. A woman's bare knees and one hand "
        "rest at the bottom edge, the hand gripping one tentacle.",
        "Soft daylight from a window on the left, warm and diffused.",
        "Her hand pulls the tentacle toward the lens in one steady motion, "
        "dragging more of the costume out over the cardboard edge.",
        "quiet room tone, cardboard scuff, fabric rustle.", maos=True),
    _cena(
        "corredor_altura",
        "Vertical 9:16 photo in a bright hallway. A woman stands in a plain "
        "white t-shirt and grey sweatpants, arms stretched high above her "
        "head, holding up by the hood " + PRODUTO + ". The costume hangs at "
        "full length in front of her, tentacles trailing past her knees to the "
        "floor, so it reads far larger than expected. Her face is cropped "
        "above the top edge. A white doorframe and a runner rug behind.",
        "Bright even daylight from a window at the end of the hall.",
        "She lowers her arms slowly, letting the costume drop until the "
        "tentacle tips pool on the floor, then holds still.",
        "quiet room tone, faint fabric rustle.", maos=True),
]

# ---------------------------------------------------------------------------
# TAKE 2 — O ABSURDO. O produto sozinho, sem ninguem dentro nem por perto.
# ---------------------------------------------------------------------------
# ⭐ E' o beat que a fonte usa para o scroll parar: um objeto grande, macio e
# vazio num lugar cotidiano. Nenhuma destas cenas tem gente em quadro.
TAKE2 = [
    _cena(
        "geladeira",
        "Vertical 9:16 photo, camera at knee height in a kitchen. Standing "
        "upright and completely empty on the wooden floor, balanced on its own "
        "splayed tentacles, is " + PRODUTO + ", hood facing away from the lens, "
        "directly in front of a wide open refrigerator. The "
        "refrigerator interior is lit and full: jars, bottles, produce "
        "drawers. Dark cabinetry on the left. No people in frame.",
        "The only light is the cold white glow from inside the refrigerator, "
        "spilling onto the floor and rimming the plush.",
        "The costume stands completely still. One tentacle tip settles a few "
        "millimetres against the floor. The refrigerator door holds open.",
        "refrigerator hum, quiet kitchen room tone."),
    _cena(
        "corredor_mercado",
        "Vertical 9:16 photo down the centre of a long supermarket aisle, "
        "camera at knee height. Standing upright and completely empty on the "
        "polished floor, small in the middle of the frame, is " + PRODUTO + ", "
        "tentacles splayed. Shelves of colourful packaging recede "
        "to a vanishing point on both sides. No people in frame.",
        "Flat overhead fluorescent light, even and slightly cold.",
        "The costume stands completely still. Nothing moves anywhere in the "
        "aisle.",
        "distant store hum, faint air conditioning."),
    _cena(
        "armario_cesto",
        "Vertical 9:16 photo of a bathroom vanity, camera at floor height. Two "
        "cabinet doors stand open. Inside, sitting in a woven basket between "
        "stacked towels and bottles, is " + PRODUTO + ", empty, hood facing "
        "the lens, tentacles spilling out over the cabinet lip onto the tiled "
        "floor. A hand rests on one door handle.",
        "Warm bathroom light from above, soft and yellow.",
        "The hand pulls the door a few inches wider and stops. Nothing else "
        "moves.",
        "quiet room tone, cabinet hinge.", maos=True),
    _cena(
        "cadeira_jantar",
        "Vertical 9:16 photo of a set dining table, camera at table height. "
        "Sitting upright and completely empty in a wooden dining chair is " +
        PRODUTO + ", hood facing the lens, tentacles draped over the seat edge "
        "and spread across the table toward a plate. A white dinner "
        "plate, cutlery set properly, a glass of water. The other chairs are "
        "empty. No people in frame.",
        "Warm pendant light hanging low over the table, soft and yellow.",
        "Nothing moves except one tentacle tip settling a few millimetres "
        "against the tablecloth.",
        "quiet room tone, a distant clock."),
    _cena(
        "garagem",
        "Vertical 9:16 photo of an open garage doorway seen from inside, "
        "camera at knee height. Standing upright and completely empty on the "
        "concrete floor is " + PRODUTO + ", silhouetted against the bright "
        "driveway beyond. Tool shelves and a folded stroller line the "
        "left wall. No people in frame.",
        "Hard daylight flooding in from the open garage door ahead, the "
        "interior falling into shadow.",
        "The costume stands completely still. A tentacle tip lifts a fraction "
        "in a draught and settles.",
        "quiet outdoor room tone, distant birds."),
]

# ---------------------------------------------------------------------------
# TAKE 3 — O BEBE REVELADO. Primeira vez que ha' alguem dentro.
# ---------------------------------------------------------------------------
# ⚠️ E' aqui que a moderacao bate. Se recusar, NAO MUDE A CENA: troque
# `a baby around ten months old` por `a small child in a plush hooded costume`
# e `baby laugh` por `soft child voice`. Esgote tres formulacoes antes de
# pedir ajuda — regra de alcada, o operador decide corte de cena.
TAKE3 = [
    _cena(
        "chao_do_quarto",
        "Vertical 9:16 photo in a nursery, camera at floor level. A baby "
        "around ten months old sits upright on a pale pink rug wearing " +
        PRODUTO + ". The hood frames the face, sitting back off the forehead "
        "so the whole face is visible, cheeks full, mouth open in a wide "
        "smile. The tentacles spread flat across the rug all around. A white "
        "crib and a cream armchair behind.",
        "Soft daylight from a window on the left, warm and diffused.",
        "The baby rocks once from side to side and the smile widens. The "
        "tentacles stay flat on the rug.",
        "quiet room tone, a soft baby coo."),
    _cena(
        "cama_de_costas",
        "Vertical 9:16 photo looking straight down at a white bed. A baby "
        "around ten months old lies on its back wearing " + PRODUTO + ", arms "
        "and legs relaxed, the eight tentacles fanned out symmetrically across "
        "the white bedding like a star. The hood cradles the head and the "
        "whole face is visible, eyes open, mouth open in a laugh.",
        "Bright soft daylight from a window to the right, even and clean.",
        "The baby kicks once and the tentacles shift a fraction on the "
        "bedding. Nothing else moves.",
        "quiet room tone, a soft baby laugh."),
    _cena(
        "janela_rua",
        "Vertical 9:16 photo at floor level beside a large window. A baby "
        "around ten months old sits upright wearing " + PRODUTO + ", the hood "
        "framing the face and sitting back off the forehead. The tentacles "
        "spread flat across the pale wooden floor. Beyond the window a "
        "suburban street with parked cars and trees, soft and out of focus.",
        "Bright overcast daylight from the window, soft and even, no harsh "
        "shadow.",
        "The baby turns its head slowly toward the lens and breaks into a wide "
        "open mouthed smile, then looks away again.",
        "quiet room tone, a soft baby coo, distant birds."),
    _cena(
        "berco_rindo",
        "Vertical 9:16 photo looking down into a white crib. A baby around ten "
        "months old lies on its back wearing " + PRODUTO + ", the hood around "
        "the head, tentacles spread over the crib sheet. Mouth wide open in a "
        "laugh, eyes squeezed shut. A folded muslin and a small stuffed bear "
        "at the edges of the frame.",
        "Warm soft daylight from a window behind the crib, gentle and hazy.",
        "The baby laughs and one arm lifts, then drops back onto the sheet. "
        "The tentacles barely move.",
        "quiet room tone, a soft baby laugh."),
    _cena(
        "colo_pernas",
        "Vertical 9:16 photo from a low reclined angle on a sofa. A woman's "
        "legs in dark leggings fill the lower half of the frame, and sitting "
        "upright on her shins facing the lens is a baby around ten months old "
        "wearing " + PRODUTO + ". The hood frames the face; the tentacles hang "
        "down over her legs on both sides. A pale wall and a doorway behind.",
        "Soft daylight from a large window on the right, warm and diffused.",
        "The baby bounces once on her shins and smiles toward the lens. Her "
        "legs stay still.",
        "quiet room tone, a soft baby coo."),
]

# ---------------------------------------------------------------------------
# TAKE 4 — O MOVIMENTO. O produto sai de casa ou ganha velocidade.
# ---------------------------------------------------------------------------
TAKE4 = [
    _cena(
        "corredor_correndo",
        "Vertical 9:16 photo down a bright hallway, camera at knee height. A "
        "toddler runs toward the lens wearing " + PRODUTO + ", tentacles "
        "swinging out to both sides and dragging behind. The hood sits back "
        "off the forehead so the whole face is visible, mouth open in a "
        "delighted shout. An open doorway and a bright room at the far end.",
        "Bright daylight spilling from the room at the end of the hall, soft "
        "and even.",
        "The toddler runs two more paces toward the lens and slows, the "
        "tentacles swinging forward and settling.",
        "quiet room tone, small running footsteps, a child laugh."),
    _cena(
        "grama_de_costas",
        "Vertical 9:16 photo on a green lawn, camera at knee height behind a "
        "toddler standing with its back to the lens, wearing " + PRODUTO + ". "
        "The eight tentacles hang down and out, several resting on the grass. "
        "Beyond, a garden fence, a tree and a patch of sky.",
        "Bright overcast daylight, soft and even, no harsh shadow.",
        "The toddler takes one step forward and the tentacles sway and settle. "
        "The head turns a fraction to one side.",
        "quiet outdoor room tone, breeze, distant birds."),
    _cena(
        "balanco",
        "Vertical 9:16 photo at a playground, camera at seat height. A baby "
        "around ten months old sits in a green bucket swing wearing " +
        PRODUTO + ", the hood framing the face, tentacles draped over the "
        "front bar and hanging down. An adult hand rests on the swing chain at "
        "the edge of the frame. Grass and trees behind, soft and out of focus.",
        "Bright dappled daylight through the trees, warm and moving.",
        "The swing drifts forward a few inches and back, the tentacles "
        "swaying under it. The baby smiles toward the lens.",
        "quiet outdoor room tone, swing chain creak, a soft baby laugh.",
        maos=True),
    _cena(
        "escorregador",
        "Vertical 9:16 photo at the bottom of a small metal slide, camera at "
        "ground level. A toddler sits at the foot of the slide wearing " +
        PRODUTO + ", legs out in front, tentacles spread across the slide and "
        "onto the woodchip ground. Mouth wide open in a laugh. A playground "
        "frame and trees behind.",
        "Bright overcast daylight, soft and even.",
        "The toddler slides the last few inches to the ground and stops, the "
        "tentacles sliding after and settling.",
        "quiet outdoor room tone, metal slide scuff, a child laugh."),
    _cena(
        "calcada_adultos",
        "Vertical 9:16 photo on a suburban pavement, camera behind two adults "
        "walking away from the lens, cropped at the shoulders so no faces are "
        "visible. Each carries on their back " + PRODUTO + ", hoods over their "
        "own shoulders and tentacles hanging down their backs and swinging at "
        "their sides. Front lawns, parked cars and autumn trees ahead.",
        "Low warm afternoon daylight from ahead, long soft shadows behind them.",
        "They take two more steps away from the lens and the tentacles swing "
        "with the stride. Neither turns around.",
        "quiet outdoor room tone, footsteps on pavement, distant traffic."),
]

# ---------------------------------------------------------------------------
# TAKE 5 — A TERNURA. O payoff, sempre parado e sempre quente.
# ---------------------------------------------------------------------------
# ⭐ A fonte fecha em calma nos dez videos. E' o beat que faz salvar e enviar,
# e por isso nenhuma cena aqui tem movimento grande.
TAKE5 = [
    _cena(
        "sofa_dormindo",
        "Vertical 9:16 photo looking down from standing height. A sleeping "
        "baby lies on a dark charcoal sofa wearing " + PRODUTO + ". The hood "
        "cradles the head, eyes closed, face peaceful and turned slightly to "
        "one side. The eight tentacles fall away across the dark cushions in a "
        "loose star. A folded cream blanket at the edge of the frame.",
        "Warm low lamplight from the upper left, dim and cosy, deep shadow in "
        "the sofa fabric.",
        "The sleeping baby breathes, the chest rising and falling once, twice. "
        "A single tentacle shifts a fraction against the cushion.",
        "quiet room tone, very soft breathing."),
    _cena(
        "colo_no_sofa",
        "Vertical 9:16 photo on a cream sofa, camera slightly above eye level. "
        "A woman sits holding a baby upright against her chest. The baby wears "
        + PRODUTO + " and the tentacles hang down over the woman's arms and "
        "lap. The baby faces the lens, calm and wide eyed. The woman's face is "
        "cropped above the top edge; only her shoulders, arms and hands show.",
        "Warm low lamplight from the upper right, cosy, deep shadow in the "
        "corners.",
        "The baby turns its head slightly and breaks into a smile toward the "
        "lens. The woman's arms stay still, holding.",
        "quiet room tone, very soft baby coo.", maos=True),
    _cena(
        "berco_dormindo",
        "Vertical 9:16 photo looking down into a white crib in a dim room. A "
        "sleeping baby lies on its back wearing " + PRODUTO + ", the hood "
        "around the head, eyes closed, one cheek squashed against the hood "
        "lining. The tentacles fan out across the crib sheet. A muslin folded "
        "at the foot of the crib.",
        "Warm low nightlight from the lower left, dim and orange, the rest of "
        "the room in shadow.",
        "The sleeping baby breathes, the chest rising and falling once. "
        "Nothing else moves.",
        "quiet room tone, very soft breathing."),
    _cena(
        "manta_e_bebe",
        "Vertical 9:16 photo of a nursery floor. A baby around ten months old "
        "sits wearing " + PRODUTO + ", half tucked under the edge of a pink "
        "floral blanket that is folded back around it, the tentacles emerging "
        "from beneath the fabric across the rug. The face is calm, eyes on the "
        "lens. A white crib behind.",
        "Warm low lamplight from the upper left, cosy, soft shadow.",
        "The baby blinks slowly and one tentacle shifts under the blanket "
        "edge. Nothing else moves.",
        "quiet room tone, very soft baby breath."),
    _cena(
        "janela_noite",
        "Vertical 9:16 photo beside a window at dusk, camera at floor level. A "
        "baby around ten months old sits upright wearing " + PRODUTO + ", "
        "looking out through the glass. The tentacles spread flat on the pale "
        "wooden floor. Beyond the window the street is dark blue with a warm "
        "porch light in the distance.",
        "Cool blue light from the window and a warm lamp behind the baby, the "
        "two colours meeting on the hood.",
        "The baby leans a fraction closer to the glass and stills. One "
        "tentacle shifts on the floor.",
        "quiet room tone, very soft baby breath."),
]

POOLS = [TAKE1, TAKE2, TAKE3, TAKE4, TAKE5]
NOMES_TAKE = ["revelacao", "absurdo", "bebe", "movimento", "ternura"]

# ---------------------------------------------------------------------------
# A LEGENDA UNICA
# ---------------------------------------------------------------------------
# ⛔ UMA por video, segurada do primeiro ao ultimo frame. NAO e' copy por cena.
# A forma sai da fonte e e' rigida: primeira linha e' a PROIBICAO DE OUTRA
# PESSOA, entre aspas ou com o sujeito nomeado; segunda linha e' so' `Me:`
# mais o emoji. Sem verbo, sem explicacao. O emoji e' a unica cor do quadro e
# carrega o tom sozinho.
# ⚠️ Escritas NOVAS, na forma da fonte. Copiar a copy dela seria copiar a peca,
# nao o metodo — e a marca deles esta' registrada.
LEGENDAS = [
    'HIM: we do NOT need another baby thing\nMe:',
    'HIM: what did you order now\nMe:',
    'HIM: babe the package is HUGE\nMe:',
    'HIM: please tell me that was cheap\nMe:',
    'HIM: whatever it is, SEND IT BACK\nMe:',
    'HIM: we are on a BUDGET this month\nMe:',
    'He asked what was in the box\nMe:',
    'He said the nursery is FULL\nMe:',
    'Told him I would stop buying baby stuff\nAlso me:',
    'POV: he checks the card statement\nMe:',
    '"Kids are impossible to shop for"\nMe:',
    '"You already have everything for the baby"\nMe:',
    'My husband: no more. I mean it.\nMe:',
    'HIM: that better not be another box\nMe:',
    'Everyone: babies do not need much\nMe:',
]

# ⛔ MONOCROMATICO ATE' O RENDERIZADOR DE PNG ENTRAR. Medido em 31/08: o
# ffmpeg queima legenda pelo libass, e o libass le so' a camada de CONTORNO
# das fontes de emoji coloridas. Estes saem em branco no video, e o colorido
# depende do `veo-editor-cta-fixo/legenda_png.py`, que existe e ainda nao esta'
# ligado ao pipeline.
EMOJIS = ["\U0001F937", "\U0001F926", "\U0001F644", "\U0001F60D",
          "\U0001F62D", "\U0001F631", "❤", "\U0001F6D2"]

CTA_FINAL = [
    "Link in bio, and I am not sorry",
    "nestlingpicks.shop before he sees this",
    "Worth every dollar. Link in bio.",
    "He gets it now. Link in bio.",
    "Tag a mom who needs this",
    "Yes it is real. Yes I bought it. Link in bio.",
]


# ---------------------------------------------------------------------------
# LEDGER
# ---------------------------------------------------------------------------
def _carregar_ledger():
    if not os.path.isfile(LEDGER):
        return {}
    try:
        with io.open(LEDGER, encoding="utf-8") as f:
            return json.load(f)
    except (ValueError, IOError):
        return {}


def _salvar_ledger(led):
    try:
        with io.open(LEDGER, "w", encoding="utf-8") as f:
            f.write(json.dumps(led, ensure_ascii=False, indent=1))
    except IOError as e:
        print("[ledger] nao gravou: %s" % e, file=sys.stderr)


def _sortear(rng, pool, chave, led, campo="id"):
    """Sorteia evitando o que saiu mais recente. ⛔ O ledger guarda os ULTIMOS
    usados, nao todos: pool pequena com memoria infinita trava depois de N
    videos e o motor passa a devolver ERRO em vez de video."""
    usados = led.get(chave, [])
    frescos = [x for x in pool if x[campo] not in usados] or list(pool)
    escolha = rng.choice(frescos)
    usados = ([escolha[campo]] + usados)[:max(1, len(pool) - 1)]
    led[chave] = usados
    return escolha


# ---------------------------------------------------------------------------
# MONTAGEM
# ---------------------------------------------------------------------------
def montar(rng, led):
    cenas = [_sortear(rng, POOLS[i], "take%d" % (i + 1), led)
             for i in range(N_TAKES)]
    leg = _sortear(rng, [{"id": t} for t in LEGENDAS], "legenda", led)["id"]
    emo = rng.choice(EMOJIS)
    cta = _sortear(rng, [{"id": c} for c in CTA_FINAL], "cta", led)["id"]
    return {"cenas": cenas, "legenda": leg + emo, "cta": cta}


def _uma_linha(*partes):
    """Junta em UMA linha corrida. ⛔ O formato da casa nao quebra prompt: o
    operador cola um de cada vez na AdBatch, e quebra de linha no meio o faz
    caçar onde a entrada termina."""
    return " ".join(" ".join(p.split()) for p in partes if p)


def _bloco_image(i, c):
    extra = ("Anatomically correct hands, clean finger separation."
             if c["maos"] else "")
    return "IMAGE %02d/%02d: %s" % (
        i + 1, N_TAKES,
        _uma_linha(c["cenario"], c["luz"], ESTILO, extra, ANTI_TEXTO))


def _bloco_take(i, c):
    # ⛔ NO I2V O TAKE NAO REDESCREVE NADA. A imagem E' o primeiro quadro;
    # redescrever convida o modelo a REGERAR o rosto e a cor, que e' a causa
    # real do morphing entre cenas. Doutrina Veo 3.1, secao 5.
    extra = DEDOS if c["maos"] else ""
    corpo = _uma_linha(
        "Animate the provided image exactly. Maintain the subject from the "
        "first frame. The camera does not move, no cuts.",
        c["movimento"],
        "Light unchanged: %s" % c["luz"],
        extra, ANTI_TEXTO_TAKE)
    # ⚠️ sem linha `Dialogue:` — este agente nao tem fala, e linha vazia seria
    # pior que linha ausente: o operador leria como copy esquecida.
    return "TAKE %02d/%02d: %s\nAudio: %s" % (i + 1, N_TAKES, corpo, c["audio"])


def render(v, n):
    """Formato da casa: uma linha de spec entre reguas, depois um prompt por
    entrada, em linha corrida, separados por linha em branco."""
    spec = _uma_linha(
        "%ds, CINCO takes de %ds, SEM FALA (musica e legenda queimada)." % (
            N_TAKES * SEG_POR_TAKE, SEG_POR_TAKE),
        "Cenas: " + " / ".join("%d %s" % (i + 1, c["id"])
                               for i, c in enumerate(v["cenas"])) + ".",
        "LEGENDA FIXA, segurada nos %ds inteiros, no campo CTA fixo do editor:"
        % (N_TAKES * SEG_POR_TAKE),
        # ⚠️ o repr() mostrava o `\n` LITERAL na linha de spec. A legenda tem
        # duas linhas de propósito (a proibicao e o `Me:`), entao aqui ela vira
        # uma barra — no editor ela e' colada com a quebra de verdade.
        v["legenda"].replace("\n", " / "),
        "CTA da descricao do post: " + v["cta"] + ".",
        "Destino: AdBatch Vertical %d." % N_TAKES)
    out = ["=" * 70, "VIDEO %02d  |  %s" % (n, spec), "=" * 70, ""]
    for i, c in enumerate(v["cenas"]):
        out.append(_bloco_image(i, c))
        out.append("")
        out.append("")
    for i, c in enumerate(v["cenas"]):
        out.append(_bloco_take(i, c))
        out.append("")
        out.append("")
    return "\n".join(out)


# ---------------------------------------------------------------------------
# LENTE
# ---------------------------------------------------------------------------
# ⛔ Cada regra aqui nasceu de um defeito pago em campo por outro agente.
# Lente que nao acusa nada e' lente que nao esta' olhando.
_RE_APARELHO = re.compile(r"\b(holding|with) (a |the )?(phone|smartphone|"
                          r"camera|iphone)\b", re.I)
_RE_TRANSFORMA = re.compile(r"PRODUTO\.(capitalize|title|upper|lower)\(")
_RE_CELEB = re.compile(r"not (a )?(celebrity|famous|celebrities)", re.I)
_RE_MARCA = re.compile(r"\b(octocuddles|nestling ?picks|amazon)\b", re.I)


def lint_fonte():
    """⛔ VARRE O PROPRIO ARQUIVO atras do modo de falha que quebrou a OC1 no
    primeiro autoteste: transformar a constante do produto com um metodo de
    caixa (para a frase comecar com maiuscula) troca o `a` inicial por `A`, e
    a string travada deixa de existir literal. A cena continua parecendo
    certa, e a continuidade do produto morre dentro dela.
    ⭐ A OC1 pega o sintoma depois de montado; esta pega a CAUSA no fonte."""
    import inspect
    try:
        fonte = inspect.getsource(sys.modules[__name__])
    except (OSError, TypeError):
        return []
    # ⛔ SO' CODIGO. A primeira versao varria o arquivo inteiro e acusava a
    # PROPRIA docstring, que precisa citar o padrao para explica-lo. Falso
    # positivo permanente treina o operador a ignorar o gate.
    linhas = [ln for ln in fonte.splitlines()
              if not ln.lstrip().startswith("#")
              and "_RE_TRANSFORMA" not in ln]
    achados = _RE_TRANSFORMA.findall("\n".join(linhas))
    return (["OC0 a string travada e transformada no fonte (%s) — "
             "a OC1 vai falhar em silencio" % ", ".join(sorted(set(achados)))]
            if achados else [])


def lint(v):
    p = []
    texto_img = " ".join(c["cenario"] for c in v["cenas"])
    texto_take = " ".join(c["movimento"] for c in v["cenas"])
    tudo = texto_img + " " + texto_take

    # OC1 — a string do produto, letra por letra, nas cinco imagens
    faltam = [c["id"] for c in v["cenas"] if PRODUTO not in c["cenario"]]
    if faltam:
        p.append("OC1 produto sem a string travada: %s" % ", ".join(faltam))

    # OC2 — aparelho DESENHADO. Licao do VICK 16: nomear o aparelho faz o
    # gerador desenha-lo, e um lote inteiro saiu com telefone na mao.
    if _RE_APARELHO.search(tudo):
        p.append("OC2 aparelho nomeado no prompt")

    # OC3 — a negacao de celebridade injeta o token que ela teme (ordem de
    # 2026-08-10, e 30 arquivos ja' foram varridos por isto)
    if _RE_CELEB.search(tudo):
        p.append("OC3 negacao de celebridade no prompt")

    # OC4 — marca em quadro: o gerador escreve texto embaralhado e o P12 do
    # parque proibe marca, salvo excecao declarada. Aqui nao ha' excecao.
    if _RE_MARCA.search(tudo):
        p.append("OC4 marca nomeada no prompt")

    # OC5 — o negativo de legenda nas DUAS pontas. O Veo transcreve fala e
    # queima texto por conta propria; a legenda de verdade e' queimada depois,
    # pelo editor, e duas legendas no mesmo quadro e' lote perdido.
    if any(ANTI_TEXTO not in _bloco_image(i, c)
           for i, c in enumerate(v["cenas"])):
        p.append("OC5 falta o anti-texto em algum IMAGE")
    if any(ANTI_TEXTO_TAKE not in _bloco_take(i, c)
           for i, c in enumerate(v["cenas"])):
        p.append("OC5 falta o anti-texto em algum TAKE")

    # OC6 — dez dedos onde ha' mao humana em quadro
    for i, c in enumerate(v["cenas"]):
        if c["maos"] and DEDOS not in _bloco_take(i, c):
            p.append("OC6 mao em quadro sem o negativo dos dedos: %s" % c["id"])

    # OC7 — a legenda tem que ter as DUAS linhas da forma da fonte
    if "\n" not in v["legenda"]:
        p.append("OC7 legenda sem a segunda linha (o `Me:`)")

    # OC8 — cinco cenas DISTINTAS. Sem isto o sorteio pode repetir a mesma
    # cena em dois slots e o video sai com dois quadros iguais.
    ids = [c["id"] for c in v["cenas"]]
    if len(set(ids)) != N_TAKES:
        p.append("OC8 cena repetida no mesmo video: %s" % ", ".join(ids))

    # OC9 — o TAKE nao pode redescrever o cenario (morphing no I2V)
    for i, c in enumerate(v["cenas"]):
        if PRODUTO in c["movimento"]:
            p.append("OC9 o TAKE %d redescreve o produto" % (i + 1))
    return p


# ---------------------------------------------------------------------------
# AUTOTESTE
# ---------------------------------------------------------------------------
def autoteste(n=400):
    rng = random.Random(20260901)
    led = {}
    erros = 0
    # ⛔ o guarda de FONTE roda antes de qualquer sorteio: se a string travada
    # foi transformada no codigo, todo video do lote nasce errado.
    for msg in lint_fonte():
        print("  %s" % msg)
        erros += 1
    vistos = [set() for _ in range(N_TAKES)]
    legendas = set()
    for _ in range(n):
        v = montar(rng, led)
        for i, c in enumerate(v["cenas"]):
            vistos[i].add(c["id"])
        legendas.add(v["legenda"].split("\n")[0])
        p = lint(v)
        if p:
            erros += 1
            if erros <= 3:
                print("  ERRO: %s" % "; ".join(p))
    print("=" * 62)
    print("AUTOTESTE OCTOPUS 5 — %d sorteios" % n)
    print("=" * 62)
    print("  videos com ERRO de lente : %d" % erros)
    for i in range(N_TAKES):
        print("  take %d (%-10s) alcancadas: %d de %d"
              % (i + 1, NOMES_TAKE[i], len(vistos[i]), len(POOLS[i])))
    print("  legendas alcancadas      : %d de %d" % (len(legendas), len(LEGENDAS)))
    total = 1
    for pl in POOLS:
        total *= len(pl)
    print("  combinacoes de cena      : %d" % total)
    print("  com legenda e emoji      : %d" % (total * len(LEGENDAS) * len(EMOJIS)))
    ok = (erros == 0
          and all(len(vistos[i]) == len(POOLS[i]) for i in range(N_TAKES))
          and len(legendas) == len(LEGENDAS))
    print("  RESULTADO                : %s" % ("APROVADO" if ok else "REPROVADO"))
    return 0 if ok else 1


def main():
    # ⛔ O CONSOLE DO WINDOWS MATA O EMOJI. O terminal nasce em cp1252 e o
    # `print` levanta UnicodeEncodeError na legenda — o motor gera certo e
    # morre na saida. O app tkinter nunca viu isto, entao o defeito so'
    # existia no caminho CLI, que e' justamente o que o operador roda para
    # conferir antes de gerar lote.
    for fluxo in (sys.stdout, sys.stderr):
        try:
            fluxo.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass
    ap = argparse.ArgumentParser(description=TITULO)
    ap.add_argument("--n", type=int, default=1, help="quantos videos")
    ap.add_argument("--seed", type=int, default=None)
    ap.add_argument("--dry-run", action="store_true",
                    help="nao grava o ledger")
    ap.add_argument("--autoteste", nargs="?", type=int, const=400, default=None)
    a = ap.parse_args()

    if a.autoteste is not None:
        return autoteste(a.autoteste)

    rng = random.Random(a.seed)
    led = _carregar_ledger()
    saiu = 0
    for k in range(a.n):
        v = montar(rng, led)
        p = lint(v)
        if p:
            print("REPROVADO pela lente: %s" % "; ".join(p), file=sys.stderr)
            continue
        print(render(v, k + 1))
        saiu += 1
    if not a.dry_run and saiu:
        _salvar_ledger(led)
    return 0 if saiu == a.n else 1


if __name__ == "__main__":
    sys.exit(main())
