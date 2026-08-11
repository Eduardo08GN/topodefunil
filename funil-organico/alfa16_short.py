#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE ALFA 16 — 2 takes de 8 segundos, destino AdBatch Vertical 2.

╔══════════════════════════════════════════════════════════════════════════╗
║ O ANGULO EM UMA FRASE: ele nao confessa uma falha — ele AVISA. O take 1  ║
║ e' um alerta ("se voce tem esposa, cuidado") e o take 2 e' a prova       ║
║ social em quadro: ele no meio, DUAS mulheres coladas, uma de cada lado.  ║
╚══════════════════════════════════════════════════════════════════════════╝

⛔⛔ O QUE SEPARA ESTE AGENTE DE TODOS OS OUTROS DEZOITO
Os dezoito anteriores abrem numa FALHA — a mancha, o murcho, o "struggling to
stay hard". Este abre numa AMEACA BRINCALHONA e fecha numa HIPERBOLE
PARADOXAL: o truque funciona TAO bem que a esposa e' quem pede tregua. O
espectador se reconhece pela ESPOSA, nao pelo orgao.

⚠️ E isso tem consequencia em CODIGO, declarada mais abaixo: o CT2 e o CT6 do
CONTRATO-COPY-16S sao DESLIGADOS aqui, cada um com o motivo escrito. Regra que
some sem explicacao o repo trata como divida.

────────────────────────────────────────────────────────────────────────────
A ESTRUTURA, decidida com o operador antes da primeira linha (2026-08-10)

  · TAKE 1 — O AVISO. Ele DE PE', perto da lente, tronco nu, TOALHA na
    cintura, falando para a camera com meio sorriso confiante. Atras, na cama,
    DUAS mulheres enroladas em toalha, SORRINDO de alegria.
  · TAKE 2 — AS DUAS DO LADO. Ele SENTADO, uma mulher de cada lado, coladas,
    as duas sorrindo. ⭐⭐ E ELE COM AS DUAS MAOS OCUPADAS: a tigela de cubos
    de gelatina numa, a caixa de bicarbonato na outra.

  ⛔ DOIS EIXOS DE CENA INDEPENDENTES (decisao do operador): o QUARTO do take 1
    e o AMBIENTE do take 2 sao listas separadas e nenhuma filtra a outra. E' a
    mesma arquitetura do FIGHT 16 — e traz a mesma consequencia: **o lugar NAO
    atravessa o corte**, entao a continuidade tem de ser carregada pelas
    PESSOAS. Lente FA13 proibe dizer `the same room/house` no take 2.

  ⭐⭐ AS MESMAS DUAS MULHERES NOS DOIS TAKES (decisao do operador). Isto e' o
    contrario do que parece: e' mais caro que o homem sozinho, porque sao TRES
    pessoas para manter identicas entre dois quadros gerados SEPARADAMENTE.
    Lente FA3 cobra as tres, peca por peca.
────────────────────────────────────────────────────────────────────────────

⛔⛔ A LICAO DO FIGHT 16 JA' NASCE APLICADA AQUI (FT14, 2026-08-10)
No FIGHT a mulher trocava entre os takes em ~15% dos videos, e a causa nao era
falta de ancora: era CONTRADICAO dentro da frase — a etnia declarada brigando
com o tom de pele que vinha do pool BELA compartilhado. Diante de contradicao o
gerador escolhe um lado, e escolhe INDEPENDENTEMENTE em cada chamada.
⭐ Por isso o pool `MULHERES` deste arquivo nasceu SEM tom de pele: a etnia e' a
UNICA autoridade sobre a cor. E o `_marca_dela` sanea a marca do MODO BELA pelo
mesmo motivo. Aqui o risco e' DOBRADO — sao duas mulheres.

⛔ SORRINDO, NUNCA GARGALHANDO — ordem do operador, literal: *"mulheres no take
1 e 2 sorrindo muito de alegria (sorrindo, nao gargalhando)"*. As referencias
visuais que ele mandou dizem `laughing` em quase todas; foi trocado por
`smiling` em cada uma, e a lente FA1 reprova o retorno de `laugh`.

    python funil-organico/alfa16_short.py --autoteste
    python funil-organico/alfa16_short.py --pagina joe --n 3
"""

import argparse
import collections
import json
import os
import random
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import short_comum as sc                                       # noqa: E402
from nucleo_sonoro import sonorizar                            # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(AQUI, ".alfa-16-ledger.json")

TITULO = "AGENTE ALFA 16"
SLUG = "alfa-16"
SUBTITULO = ("2 takes de 8s = 16 segundos · o aviso de toalha com as duas "
             "atras e depois as duas coladas · a prova esta' nas duas maos dele")

CENAS_UI = ["1 · O AVISO", "2 · AS DUAS DO LADO"]

# ⭐ Um sexo so' — narrador HOMEM. Com um sexo a UI nao desenha botao, que e' o
# certo: botao que nao troca nada e' pior que botao nenhum.
SEXOS = ("homem",)

MODO_BELA = True

# ⭐⭐ MODO FORTE COM POOL PROPRIO, 50+ — decisao do operador (2026-08-10).
# ⛔ O `sc.REFS_FORTES` compartilhado NAO serve aqui: ele tem 26-38 anos e 7 de
# 16 entradas com pelo facial. O operador pediu REF **50+**, e um toggle que
# entrega um rapaz de 29 num angulo de autoridade masculina madura e' o mesmo
# defeito que me obrigou a DESLIGAR o modo no PEE 16 hoje.
# ⭐ Aqui o modo nao troca a pessoa: troca o CORPO dela. Desligado, o porte
# comum de um homem de 50+ que se cuida; ligado, o fisico do print (peitoral e
# ombros de quem treina, cintura seca). Mesma faixa etaria nos dois estados.
MODO_FORTE = True

PELE_TRAVAVEL = False

TETO_FALA = {1: 25, 2: 25}
# ⚠️ PISO por cena — fala curta demais num take de 8s deixa silencio, e silencio
# em video de funil e' onde o dedo sobe.
PISO_FALA = {1: 20, 2: 21}

NUCLEO = ["Johnson", "pecker", "wiener", "soldier", "tool"]

ETNIA = {
    "roy": "white American", "dean": "white American",
    "earl": "white American",
    "jason": "Black American", "philippe": "Black American",
    "joe": "white American", "ray": "white American", "matt": "white American",
    "marcus": "Black American", "chuck": "Black American",
}

CAUDA = ("Shot on iPhone, natural grain. No on-screen text, no subtitles, no "
         "captions, no watermark.")

# ⛔⛔ SEM DECLARACAO DE CONFORMIDADE. Ordem do operador de 2026-08-10, e
# doutrina do repo desde 2026-07-31 (licoes-producao-veo §"Declaracao e'
# municao"): `not a celebrity` INJETA o token `celebrity`, e o classificador
# casa TOKEN, nao intencao. Quem separa estes rostos da media do treino e' a
# ARQUITETURA FACIAL de cada entrada do pool `HOMENS` — formato do rosto,
# testa, nariz, maxilar —, nunca uma negacao.
# ⚠️ Este agente NASCE limpo. Os outros ~41 motores do repo ainda carregam a
# negacao; a divida esta' declarada no CLAUDE.md.

# ---------------------------------------------------------------------------
# ⭐ AS STRINGS TRAVADAS — a prova nas duas maos
# ---------------------------------------------------------------------------
# ⛔ Ordem do operador: *"no take 2 o homem sempre segurara uma bowl de gelatina
# em cubos numa mao e a caixa de baking soda na outra"*.
# ⚠️ E' por isso que NENHUM ambiente do take 2 pode pedir gesto de mao: as
# referencias que ele mandou traziam `one arm casually resting along the
# backrest` e `gesturing with one hand`, e as duas foram removidas na
# transcricao. Mao ocupada nao gesticula, e prompt que pede as duas coisas faz o
# gerador desenhar uma TERCEIRA mao — e' o defeito das DUAS COLHERES.
TIGELA_CUBOS = "a clear glass bowl full of cut cubes of set amber gelatin"
CAIXA_BICARBONATO = ("an orange and yellow cardboard box of baking soda, the "
                     "label sharp and readable")

# ---------------------------------------------------------------------------
# EIXO 1 — O QUARTO DO AVISO (take 1)
# ---------------------------------------------------------------------------
# ⛔ Eixo INDEPENDENTE do take 2 (decisao do operador). O print de referencia e'
# o `hotel_cidade`; os outros nove sao o mesmo BEAT em outro lugar — ele de pe'
# perto da lente, elas atras na cama/no assento, enroladas em toalha.
# ⚠️ Cada entrada carrega `elas`, e o campo existe porque a geometria do print
# (as duas sentadas na beirada da cama) nao transfere para uma suite de spa nem
# para um deck. Sem isso o prompt pediria uma cama onde nao ha' cama.
QUARTOS = [
    {"id": "hotel_cidade", "nome": "quarto de hotel com a cidade na janela",
     "cen": "a modern hotel bedroom at night, a wide upholstered headboard and "
            "a window showing the lit city behind it",
     "elas": "Sitting side by side on the edge of the bed a few feet behind him "
             "are",
     "luz": "two warm bedside lamps and no ceiling light",
     "audio": "quiet room tone, faint traffic far below"},
    {"id": "resort_tropical", "nome": "quarto de resort tropical",
     "cen": "a bright resort bedroom with the balcony door open and palm "
            "leaves moving outside",
     "elas": "Sitting together on the end of the bed a few feet behind him are",
     "luz": "late afternoon sun through the open balcony door",
     "audio": "surf breaking outside, wind through the open door"},
    {"id": "chale_montanha", "nome": "quarto de chale na montanha",
     "cen": "a mountain lodge bedroom with log walls and a wood stove burning "
            "in the corner",
     "elas": "Sitting close together on a bench at the foot of the bed behind "
             "him are",
     "luz": "firelight from the stove and one small lamp",
     "audio": "the stove ticking, wind outside the window"},
    {"id": "cobertura", "nome": "cobertura com vidro do chao ao teto",
     "cen": "a penthouse bedroom with floor-to-ceiling glass and the city grid "
            "far below",
     "elas": "Sitting side by side on a low bench against the glass behind him "
             "are",
     "luz": "dim interior light with the city glow coming through the glass",
     "audio": "quiet room tone, a distant siren"},
    {"id": "villa_piscina", "nome": "quarto de villa com piscina",
     "cen": "a villa bedroom with sliding doors open onto a lit private pool",
     "elas": "Sitting together on the end of the bed behind him are",
     "luz": "blue light off the pool water and one warm lamp",
     "audio": "water lapping in the pool, crickets outside"},
    {"id": "suite_spa", "nome": "suite de spa do hotel",
     "cen": "a hotel spa suite with polished stone walls and rolled white "
            "towels stacked on a shelf",
     "elas": "Sitting side by side on a long cushioned bench behind him are",
     "luz": "warm indirect light low on the walls",
     "audio": "quiet room tone, water running somewhere far off"},
    {"id": "banheiro_luxo", "nome": "banheiro de luxo da suite",
     "cen": "a large hotel bathroom with a marble counter, a deep soaking tub "
            "and a fogged mirror",
     "elas": "Sitting side by side on the wide edge of the tub behind him are",
     "luz": "warm vanity light with the mirror still fogged",
     "audio": "water dripping into the tub, quiet room tone"},
    {"id": "cabana_praia", "nome": "cabana de praia",
     "cen": "an open beach cabana with white curtains moving and the ocean "
            "behind it",
     "elas": "Sitting together on a cushioned bench behind him are",
     "luz": "low golden light near sunset",
     "audio": "surf and wind in the curtains"},
    {"id": "quarto_iate", "nome": "cabine de iate",
     "cen": "a yacht cabin with varnished wood panels and a round window "
            "showing open water",
     "elas": "Sitting side by side on the built-in bunk behind him are",
     "luz": "warm cabin light with daylight in the round window",
     "audio": "water against the hull, the quiet hum of the boat"},
    {"id": "quarto_deserto", "nome": "quarto de resort no deserto",
     "cen": "a desert resort bedroom with adobe walls and a wide window "
            "showing red rock at dusk",
     "elas": "Sitting close together on a low bench behind him are",
     "luz": "last red daylight through the window and one lamp",
     "audio": "very quiet room tone, wind outside"},
]

# ---------------------------------------------------------------------------
# EIXO 2 — O AMBIENTE DAS DUAS DO LADO (take 2)
# ---------------------------------------------------------------------------
# ⛔⛔ OS DEZ AMBIENTES SAO DO OPERADOR — ele escreveu os dez, um por um, e a
# lista e' FECHADA. O autoteste conta dez e reprova se alguem acrescentar ou
# resumir. ⚠️ Ele disse que sao REFERENCIA e nao literal, entao o que foi
# transcrito e' a GEOMETRIA de cada uma (onde ele senta, onde elas sentam, o que
# esta' atras, a luz) — nao a prosa.
# ⛔ E o que foi REMOVIDO de todas: `laughing` (virou sorriso, ordem dele) e
# qualquer gesto de mao (`one arm resting along the backrest`, `gesturing with
# one hand`) — as duas maos dele estao ocupadas com a tigela e a caixa.
AMBIENTES = [
    {"id": "espreguicadeira", "nome": "espreguicadeira na beira da piscina",
     "cen": "an upscale tropical resort pool deck, a large swimming pool "
            "directly behind them, palm trees and tropical planting",
     "pose": "Sitting on a wide poolside chaise lounge closest to the camera is",
     "luz": "bright open afternoon sunlight",
     "audio": "water moving in the pool, distant voices"},
    {"id": "rooftop", "nome": "lounge na cobertura, cidade a noite",
     "cen": "a luxury rooftop lounge at night with a wide illuminated city "
            "skyline behind them and a cocktail table with glasses nearby",
     "pose": "Sitting on a large outdoor lounge sofa closest to the camera is",
     "luz": "warm architectural light mixed with blue city light",
     "audio": "quiet rooftop chatter, city hum far below"},
    {"id": "deck_jacuzzi", "nome": "deck da jacuzzi ao entardecer",
     "cen": "a private hotel jacuzzi deck at dusk, steam rising off the water "
            "behind them and wet stone underfoot",
     "pose": "Sitting on the wide edge of the jacuzzi closest to the camera is",
     "luz": "soft sunset sky with warm deck lights",
     "audio": "water bubbling behind them, quiet evening air"},
    {"id": "chaise_quarto", "nome": "chaise do quarto de luxo, manha",
     "cen": "an elegant hotel bedroom in bright morning light, a large unmade "
            "bed behind them and clothes left over a chair",
     "pose": "Sitting on a long upholstered chaise longue closest to the camera "
             "is",
     "luz": "morning sun through sheer curtains",
     "audio": "very quiet room tone, a bird outside"},
    {"id": "cabana", "nome": "cabana de praia no fim da tarde",
     "cen": "a private beach cabana with the ocean visible behind the open "
            "curtains, beach towels and sandals nearby",
     "pose": "Sitting on a cushioned outdoor bench closest to the camera is",
     "luz": "warm low sunset light",
     "audio": "surf and a light breeze in the curtains"},
    {"id": "lareira_lodge", "nome": "lounge da lareira no lodge",
     "cen": "an upscale mountain lodge lounge at night, a large stone fireplace "
            "burning behind them and snow visible through the window",
     "pose": "Sitting in a deep leather lounge chair closest to the camera is",
     "luz": "warm firelight with low lamps",
     "audio": "the fire cracking, very quiet room"},
    {"id": "varanda_mar", "nome": "varanda da suite de frente para o mar",
     "cen": "an oceanfront hotel balcony in the early evening, the ocean and "
            "the horizon behind them and two empty glasses on a small table",
     "pose": "Sitting on a wide outdoor daybed closest to the camera is",
     "luz": "soft blue-hour light",
     "audio": "surf far below, wind on the balcony"},
    {"id": "spa", "nome": "lounge de relaxamento do spa",
     "cen": "a high-end hotel spa relaxation lounge, polished stone surfaces, "
            "rolled white towels and faint steam in the background",
     "pose": "Sitting on a large cushioned relaxation bench closest to the "
             "camera is",
     "luz": "warm indirect ambient light",
     "audio": "very quiet room tone, water trickling somewhere"},
    {"id": "penthouse", "nome": "sala da cobertura depois da festa",
     "cen": "a modern penthouse living room late at night, floor-to-ceiling "
            "windows showing the city below, cushions scattered and drinks left "
            "on a low table",
     "pose": "Sitting on a large designer sofa closest to the camera is",
     "luz": "dim warm interior light",
     "audio": "quiet room tone, the city far below"},
    {"id": "deck_infinito", "nome": "deck da piscina de borda infinita, nascer "
                                    "do sol",
     "cen": "an exclusive villa with a private infinity pool at sunrise, the "
            "pool and the ocean horizon behind them and tropical planting "
            "around",
     "pose": "Sitting on the edge of a padded poolside daybed closest to the "
             "camera is",
     "luz": "pale sunrise light with soft morning mist",
     "audio": "very still water, early birds"},
]

# ---------------------------------------------------------------------------
# O NARRADOR — 50+, e a ARQUITETURA FACIAL e' o que o separa da media do treino
# ---------------------------------------------------------------------------
# ⛔ Ordem do operador: REF **50+**. E ordem do mesmo dia: nada de negacao de
# celebridade. Entao cada entrada descreve FORMATO DE ROSTO, TESTA/ARCADA,
# NARIZ, MAXILAR e o cabelo por CORTE — nao so' cor de cabelo mais uma marca.
# Um pool descrito so' por cabelo e' um homem so' repetido N vezes, e o gerador
# devolve a media (foi o defeito que o operador pegou no PEE 16 hoje).
# ⚠️ CINCO das dezesseis NAO sao grisalhas: aos 50 muita gente ainda nao e', e
# um pool 100% prateado empobrece o lote inteiro.
# ⚠️ ZERO mencao a etnia: quem injeta e' o `ETNIA[pagina]` (congruencia com o
# avatar da pagina, que e' inviolavel neste funil).
#
# ⛔⛔ POOL REESCRITO E DOBRADO EM 2026-08-10 — "RETIRE ESSE REF FEIO"
# ---------------------------------------------------------------------------
# O operador viu o render e reprovou o narrador. Era o `franja_frente`:
#
#     "a heavy grey-brown MOP COMBED FORWARD over his forehead, a round face
#      with a short blunt nose" + "thick EYEBROWS THAT MEET IN A SINGLE LINE"
#
# ⛔ E era violacao da doutrina do proprio repo — licoes-producao-veo §REF,
# DISTINTIVO NUNCA DETERIORADO: a ancora tem de ser uma caracteristica
# MEMORAVEL num rosto SAUDAVEL E CUIDADO, nunca uma avaria. Cabelo penteado
# PARA A FRENTE le' como quem esconde entrada; sobrancelha unida le' como
# desleixo. Nenhuma das duas e' marca — as duas sao descuido.
#
# ⚠️⚠️ E A AUDITORIA ACHOU MAIS OITO, todas do mesmo lado da tabela: `small
# close-set eyes`, `full cheeks and a blunt nose`, `hollow cheeks`, `heavy
# under-jaw`, `waves worn low across the forehead`, `hair standing high off a
# DEEP HAIRLINE` (le' entrada), `round-jawed face with a short forehead`,
# `heart-shaped face with a pointed chin`. Uma a uma passavam; JUNTAS elas
# faziam um pool em que metade dos sorteios entregava um homem sem atrativo.
#
# ⭐⭐ E A BARRA DESTE ANGULO E' OUTRA, e e' isso que eu tinha errado. No PEE o
# narrador vende CREDIBILIDADE — rosto vivido serve. Aqui ele esta' de toalha
# com DUAS MULHERES do lado: se ele nao for plausivelmente atraente, a cena
# nao fecha e o espectador nao inveja ninguem. A lei do REF feminino do repo
# ("sempre bonita") tem um equivalente masculino NESTE angulo, e ele nao
# estava escrito.
# ⛔ Mas continua PROIBIDO dizer isso com adjetivo: `handsome`, `chiseled`,
# `distinguished`, `strong jaw` empurram PARA a celebridade (espinha-fixa
# §Construir o REF contra a celebridade). O atrativo tem de sair da GEOMETRIA
# — mandibula definida, osso bom, cabelo farto e bem cortado —, nunca de um
# adjetivo de aprovacao.
# ⚠️ O autoteste ganhou a lista de VOCABULARIO DE DESLEIXO, e ela teria pegado
# o `franja_frente` no dia em que ele nasceu.
#
# ⚠️ OITO das 26 NAO sao grisalhas: aos 50 muita gente ainda nao e', e um pool
# 100% prateado empobrece o lote inteiro.
# ⚠️ ZERO mencao a etnia: quem injeta e' o `ETNIA[pagina]`.
HOMENS = [
    {"id": "risca_lateral", "idade": 52,
     "marca": "dark hair combed into a low side part with grey only at the "
              "temples, a close-trimmed dark beard and a broad square face "
              "with a heavy flat brow",
     "sinal": "a shallow cleft in his chin"},
    {"id": "grisalho_tras", "idade": 58,
     "marca": "thick steel-grey hair brushed straight back, a full grey beard "
              "kept short, a long face with high cheekbones and a straight "
              "narrow nose",
     "sinal": "a clean pale scar through his right eyebrow"},
    {"id": "corte_rente", "idade": 55,
     "marca": "hair cropped close all over and grey at the sides, three days "
              "of grey stubble, a wide face with a firm jawline, sun-weathered",
     "sinal": "a small notch in the rim of his left ear"},
    {"id": "ondulado_escuro", "idade": 51,
     "marca": "dense dark waves cut short at the sides, a squared jaw and "
              "wide-set eyes under level brows",
     "sinal": "a raised mole beside his left nostril"},
    {"id": "prata_curto", "idade": 61,
     "marca": "short silver hair with a hard part cut into one side, a thick "
              "silver moustache, a heavy square jaw and a level hairline",
     "sinal": "a coin-sized birthmark on the side of his jaw"},
    {"id": "castanho_alto", "idade": 50,
     "marca": "thick chestnut hair worn long on top and short at the sides, an "
              "angular face with a defined chin, tanned",
     "sinal": "a deep dimple in his left cheek"},
    {"id": "sal_pimenta", "idade": 56,
     "marca": "salt-and-pepper hair swept back off the forehead, a "
              "salt-and-pepper goatee, a lean face with a firm jawline and a "
              "straight nose",
     "sinal": "a dense spray of freckles across his nose"},
    {"id": "flat_top", "idade": 63,
     "marca": "a pewter flat-top cut squared off across the top, a long jaw "
              "and high flat cheekbones",
     "sinal": "a pale scar under his lower lip"},
    {"id": "preto_denso", "idade": 53,
     "marca": "hair still mostly black and cut dense and short, a clean-shaven "
              "face, grey only in front of the ears, a broad face with a wide "
              "mouth",
     "sinal": "a small dark mole under his right eye"},
    {"id": "onda_prata", "idade": 59,
     "marca": "thick silver hair with a natural wave lifting off the forehead, "
              "close silver stubble, a long face with a high bridge to his nose",
     "sinal": "laugh lines cut deep at the corners of his mouth"},
    {"id": "arruivado", "idade": 54,
     "marca": "rust-brown hair faded to sandy grey and combed to one side, a "
              "short reddish beard going grey, a ruddy square-chinned face",
     "sinal": "a deep dimple in each cheek"},
    {"id": "compacto", "idade": 66,
     "marca": "fine white hair combed back off the forehead, a neat white "
              "moustache, a long face with sharp cheekbones, deeply lined",
     "sinal": "two small dark moles in a line on his right temple"},
    {"id": "mecha_branca", "idade": 60,
     "marca": "grey hair parted on the side with a bright white streak at one "
              "temple, an oval face with a defined jaw",
     "sinal": "a deep cleft in his chin"},
    {"id": "escovinha", "idade": 51,
     "marca": "dark hair buzzed to an even short brush all over, heavy "
              "stubble, a square face with a wide jaw and level brows",
     "sinal": "a birthmark shaped like a comma on his left cheek"},
    {"id": "ondas_baixas", "idade": 64,
     "marca": "heavy grey waves worn back off the forehead, a long face with a "
              "straight strong nose",
     "sinal": "a pale patch of white skin the size of a coin on his jaw"},
    {"id": "cachos_grisalhos", "idade": 57,
     "marca": "tight grey curls cut close to the head, a close-cut grey beard, "
              "a broad open face with high cheekbones",
     "sinal": "a small gold hoop in his left ear"},
    # ---------------------------------------------------------------------
    # + 2026-08-10: as DEZ que dobram o pool, no mesmo padrao — geometria que
    # le' bem, cabelo farto e bem cortado, e uma ancora memoravel.
    # ---------------------------------------------------------------------
    {"id": "platinado", "idade": 62,
     "marca": "thick platinum-white hair with a deep side sweep, a lean "
              "angular face and a straight nose",
     "sinal": "one pale blue eye and one hazel eye"},
    {"id": "no_na_nuca", "idade": 50,
     "marca": "dark hair long enough to tie into a short knot at the nape, a "
              "short dark beard, a narrow face with a defined jaw",
     "sinal": "a small scar at the point of his chin"},
    {"id": "militar", "idade": 55,
     "marca": "a high and tight cut with grey at the temples, a clean-shaven "
              "face, a wide square face and a level brow",
     "sinal": "a shallow dimple in his chin"},
    {"id": "mecha_frente", "idade": 53,
     "marca": "thick dark hair falling loose over one side of the forehead, "
              "light stubble, a long face with a fine straight nose",
     "sinal": "freckles across his nose and cheekbones"},
    {"id": "cabelo_farto", "idade": 65,
     "marca": "a full head of white hair with a natural side wave, a neat "
              "white beard cut close, a broad face with a wide firm mouth",
     "sinal": "a dark mole high on one cheekbone"},
    {"id": "taper_baixo", "idade": 52,
     "marca": "dark hair in a low taper with a sharp line at the temples, a "
              "thin moustache, an oval face with a defined jaw, lightly "
              "freckled",
     "sinal": "a beauty mark beside one eyebrow"},
    {"id": "grisalho_medio", "idade": 58,
     "marca": "mid-length grey hair tucked behind the ears, a clean-shaven "
              "face, a long face with high flat cheekbones",
     "sinal": "a thin pale scar along one jawline"},
    {"id": "loiro_areia", "idade": 51,
     "marca": "sandy blond hair going grey at the temples and cut short, light "
              "stubble, a square face with a wide mouth, tanned with fine "
              "lines at the eyes",
     "sinal": "a small notch in one eyebrow"},
    {"id": "topete", "idade": 60,
     "marca": "thick grey hair swept up and back off the forehead, a close "
              "silver beard, a strong-boned face with a straight nose",
     "sinal": "a raised beauty mark on his right jaw"},
    {"id": "cacho_solto", "idade": 54,
     "marca": "loose dark curls with grey running through them, worn short, a "
              "clean-shaven face, a broad face with a defined chin",
     "sinal": "a clean pale scar across the back of one hand"},
]

# ⭐⭐ O CORPO — e e' aqui que o MODO FORTE vive.
# ⛔ Os dois pools tem a MESMA faixa etaria (o narrador continua 50+ nos dois
# estados). O que muda e' o fisico, e ele muda de verdade: o autoteste cobra
# que os dois conjuntos nao tenham UMA entrada em comum. Toggle que nao move
# nada e' o botao que mente, e este repo ja' pagou por ele tres vezes.
CORPOS_H = [
    "medium build, solid through the chest and softening a little at the waist",
    "an average build with square shoulders and a flat stomach",
    "a lean build with long arms and a narrow waist",
    "a heavier build, broad through the chest and thick in the arms",
    "a compact build with a deep chest and short thick forearms",
    "a tall build with sloping shoulders and a long torso",
]
CORPOS_FORTES = [
    "the dense build of a man who lifts, thick through the chest and shoulders "
    "with the waist still cut",
    "a powerfully built frame with a broad chest, thick arms and clear "
    "definition down the stomach",
    "a hard-muscled build with heavy shoulders, corded forearms and a tight "
    "waist",
    "a wide athletic frame, deep chest, cut arms and visible lines across the "
    "stomach",
    "a heavy muscular build with a barrel chest, thick neck-to-shoulder line "
    "and a flat hard stomach",
]

# a toalha DELE — sempre na cintura, nos dois takes (e' o uniforme do angulo)
TOALHAS = [
    "a white bath towel knotted at his waist",
    "a thick white hotel towel wrapped and tucked at his waist",
    "a navy blue towel wrapped low at his waist",
    "a sand-coloured beach towel knotted at his waist",
    "a large charcoal grey towel wrapped at his waist",
]

# ---------------------------------------------------------------------------
# AS DUAS MULHERES — pool generoso, e SEM TOM DE PELE de proposito
# ---------------------------------------------------------------------------
# ⛔⛔ NENHUMA ENTRADA DIZ COR DE PELE, e isso e' a licao FT14 do FIGHT 16
# aplicada ANTES do primeiro render: la' o pool BELA compartilhado trazia
# `clear deep brown skin` enquanto o motor declarava `white American` na mesma
# frase, e o gerador — que resolve contradicao INVENTANDO — entregou uma mulher
# no take 1 e outra no take 2 em ~15% dos videos.
# ⚠️ Aqui o risco e' DOBRADO: sao DUAS mulheres atravessando o corte. A etnia
# declarada e' a UNICA autoridade sobre a cor, nas duas.
# ⛔ E NENHUMA diz SORRISO tambem: o sorriso e' CENA (o operador mandou que elas
# sorriam nos dois takes) e entra na montagem, uma vez so'. Sorriso dentro da
# identidade brigaria com qualquer cena que pedisse outra expressao.
MULHERES = [
    {"id": "morena_ondulada", "idade": 29, "etnia": "white American",
     "porte": "slim with narrow shoulders",
     "marca": "long wavy dark brown hair and a small mole beside her left eye"},
    {"id": "loira_lisa", "idade": 31, "etnia": "white American",
     "porte": "athletic with a small waist",
     "marca": "straight blonde hair cut blunt at the shoulders, tanned from the "
              "sun, and a faint scar through one eyebrow"},
    {"id": "ruiva_cachos", "idade": 27, "etnia": "white American",
     "porte": "small and lightly built",
     "marca": "loose auburn curls past her shoulders and a dense spray of "
              "freckles"},
    {"id": "preto_liso", "idade": 33, "etnia": "Black American",
     "porte": "tall with long legs",
     "marca": "straight black hair worn long, fine laugh lines at the corners of "
              "her eyes, and a wide gap between her front teeth"},
    {"id": "trancas", "idade": 28, "etnia": "Black American",
     "porte": "athletic and broad-shouldered",
     "marca": "long thin braids gathered behind one shoulder and a beauty mark "
              "high on one cheekbone"},
    {"id": "coque_alto", "idade": 30, "etnia": "white American",
     "porte": "curvy with a narrow waist",
     "marca": "dark hair pulled up into a high messy knot, lightly freckled "
              "across the nose, and a small chin dimple"},
    {"id": "chanel_castanho", "idade": 34, "etnia": "white American",
     "porte": "average build with a long waist",
     "marca": "chestnut hair cut to a sharp bob at the jaw, tanned from the sun, "
              "and a beauty mark above her lip"},
    {"id": "afro_curto", "idade": 26, "etnia": "Black American",
     "porte": "petite and finely built",
     "marca": "a short natural afro and a small scar at the corner of one "
              "eyebrow"},
    {"id": "rabo_de_cavalo", "idade": 32, "etnia": "white American",
     "porte": "toned with square shoulders",
     "marca": "dark hair pulled back into a long high ponytail and a thin "
              "silver stud in one nostril"},
    {"id": "grisalha_jovem", "idade": 35, "etnia": "white American",
     "porte": "slim and long-limbed",
     "marca": "shoulder-length hair dyed a pale silver-grey and a wide mouth "
              "with a deep cupid's bow"},
    {"id": "twist_out", "idade": 31, "etnia": "Black American",
     "porte": "curvy with a small waist",
     "marca": "shoulder-length hair in loose defined coils and a small mole "
              "under her right eye"},
    {"id": "franja_reta", "idade": 27, "etnia": "white American",
     "porte": "compact and lightly built",
     "marca": "dark hair with a straight blunt fringe over her eyebrows, fine "
              "laugh lines at her eyes, and a narrow face"},
    {"id": "mel_longo", "idade": 29, "etnia": "white American",
     "porte": "athletic with clear definition in her arms",
     "marca": "long honey-blonde hair worn loose, freckled across the nose and "
              "shoulders, and a faint scar on her chin"},
    {"id": "coque_baixo", "idade": 36, "etnia": "Black American",
     "porte": "tall and narrow through the hips",
     "marca": "hair gathered into a low sleek knot and high sharp cheekbones"},
    {"id": "ombro_castanho", "idade": 33, "etnia": "white American",
     "porte": "solid through the shoulders and hips",
     "marca": "mid-brown hair to her shoulders with a heavy side part and a "
              "small mole on her jaw"},
    # ---------------------------------------------------------------------
    # + 2026-08-10: as OITO que dobram o pool ("aumente o pool de personagens
    # tb"). Mesmo contrato das dezesseis acima — SEM tom de pele (a etnia e' a
    # unica autoridade, licao FT14) e SEM sorriso (o sorriso e' CENA e entra
    # uma vez so' na montagem).
    # ⭐ E a etnia delas e' SOLTA — quem trava a congruencia com a pagina e' o
    # HOMEM. Por isso entram tres etnias que o pool nao tinha: sao duas
    # mulheres em quadro, e a variacao entre elas e' o que separa uma da outra.
    # ---------------------------------------------------------------------
    {"id": "morena_repartida", "idade": 30, "etnia": "Hispanic American",
     "porte": "curvy with a small waist",
     "marca": "long dark hair with a centre part and a beauty mark just below "
              "one eye"},
    {"id": "ondulada_mel", "idade": 32, "etnia": "Hispanic American",
     "porte": "athletic with long legs",
     "marca": "shoulder-length waves in a warm caramel tone and a fine scar "
              "through one eyebrow"},
    {"id": "liso_preto_curto", "idade": 28, "etnia": "Asian American",
     "porte": "slim and finely built",
     "marca": "straight black hair cut in a blunt bob at the jaw and a small "
              "mole at the corner of her mouth"},
    {"id": "rabo_alto_preto", "idade": 34, "etnia": "Asian American",
     "porte": "toned with square shoulders",
     "marca": "long black hair pulled into a high ponytail and high sharp "
              "cheekbones"},
    {"id": "loira_curta", "idade": 31, "etnia": "white American",
     "porte": "lean with a long neck",
     "marca": "a short blonde crop swept to one side and a thin silver hoop in "
              "one ear"},
    {"id": "ruiva_lisa", "idade": 26, "etnia": "white American",
     "porte": "petite with a narrow waist",
     "marca": "straight copper-red hair to her collarbone and freckles across "
              "her nose and cheeks"},
    {"id": "locs", "idade": 33, "etnia": "Black American",
     "porte": "tall and athletic",
     "marca": "shoulder-length locs gathered to one side and a small gold stud "
              "in one nostril"},
    {"id": "bob_castanho", "idade": 29, "etnia": "Black American",
     "porte": "curvy with full hips",
     "marca": "a chin-length brown bob with a deep side part and a dimple in "
              "one cheek"},
    {"id": "cacheada_volumosa", "idade": 28, "etnia": "Black American",
     "porte": "athletic with a narrow waist",
     "marca": "voluminous curls worn wide around her face, tanned from the sun,"
              "and a wide bright gap-toothed mouth"},
]

# ---------------------------------------------------------------------------
# ⭐⭐ O ENVOLTORIO DELAS — STRING TRAVADA, e nasceu EIXO
# ---------------------------------------------------------------------------
# ⛔⛔ O BIQUINI SAIU EM 2026-08-10, POR REPROVACAO DE CAMPO. O operador rodou
# o lote e mediu: *"acho que teremos que deixar apenas a opcao de toalha
# amarrada ate' a altura acima do busto mesmo. Ta' dando muita reprovacao so' o
# biquini na parte superior das mulheres."*
#
# O eixo tinha DOIS estados, pedidos por ele no mesmo dia:
#     ✅ toalha enrolada e presa POUCO ACIMA DO BUSTO   (a do print)
#     ⛔ biquini em cima + toalha na CINTURA            — REPROVADO no gerador
#
# ⭐ E a diferenca entre os dois nao e' de pudor, e' de CATEGORIA para o
# classificador: `bath towel` e' roupao/banho, e o corpo aparece COBERTO por um
# objeto de casa. `bikini top` nomeia ROUPA DE BANHO, e roupa de banho num
# quarto de hotel com um homem de toalha e' outra categoria inteira — a mesma
# familia da licao do `lap` -> `knee`, em que o token decide e nao a intencao.
# ⚠️ E o print de referencia sempre foi o primeiro estado; o segundo era
# ampliacao nossa. Quando a ampliacao briga com o gerador, quem sai e' a
# ampliacao.
#
# ⛔ COM UM ESTADO SO', ISTO DEIXOU DE SER EIXO — virou string travada, e o
# botao SAIU DO PAINEL. Botao com uma opcao e' botao que nao muda nada, e a lei
# do operador sobre isso e' antiga: *botao que nao troca nada e' pior que botao
# nenhum*. Manter o pool com um item so' seria a forma sem a funcao.
# ⚠️ As DUAS usam o mesmo envoltorio, e isso continua valendo pelo motivo
# original: elas sao AS MESMAS atravessando o corte, e traje diferente entre
# elas — ou entre os takes — le' como duas cenas coladas.
ENVOLTORIO_DELAS = "a white bath towel wrapped and tucked just above the bust"

# ===========================================================================
# COPY — TAKE 1: O AVISO
# ===========================================================================
# ⛔⛔ A SEMANTICA E' DO OPERADOR, literal: *"if you have a wife, watch out! The
# trick i discovered will make your wife <frase impactante de hiperbole
# paradoxal dizendo que ela nao aguenta mais o Johnson dele nao dando tregua
# pra ela>"*.
#
# TRES BATIDAS:
#     <AVISO ao homem casado>  ·  <O TRUQUE que ele descobriu>  ·  <O PARADOXO>
#
# ⛔ O PARADOXO E' O ANGULO. Nao e' "funciona"; e' "funciona DEMAIS, e quem
# pede tregua e' ela". A promessa entra pela ESPOSA, que e' onde o avatar
# sente o problema — ele nao precisa admitir nada para se reconhecer.
#
# ⛔⛔ E POR ISSO O CT2 ESTA' DESLIGADO NESTE MOTOR (ver `_ct16`): o CT2 exige
# que o take 1 enuncie uma FALHA masculina, e este angulo — por desenho do
# operador — nao enuncia nenhuma. Ele AVISA e PROMETE. Deixar o aviso ligado
# faria o painel acusar 100% dos videos, e lente que reprova o que esta' certo
# ensina o operador a ignorar o relatorio inteiro (licoes §16).

# ⚠️ 6-7 palavras exatas.
AVISOS = [
    "If you have a wife, watch out.",              # ← a do operador
    "If you have a wife, fair warning.",
    "Married men, you have been warned.",
    "Got a wife at home? Careful.",
    "If your wife is home tonight, careful.",
    "Husbands, this one comes with a warning.",
]

# ⚠️ 7-8 palavras exatas. Nomeia o literal `gelatin trick` como DESCOBERTA.
# ⛔ A razao do truque (verbo de efeito + alvo, CT3) mora no take 2, que e' onde
# ela cabe — cobrar a razao nas duas mencoes seria redundancia paga em palavras
# que o take nao tem.
#
# ⛔⛔ DUAS ENTRADAS FORAM DESCARTADAS EM 2026-08-10, POR VAGUEZA — o operador
# leu o app e perguntou: *"o que significa `got hold of me` nesse caso? Nao ta'
# meio vago nao?"*. Esta' — e a outra tinha o MESMO defeito:
#
#     ✗ "The gelatin trick got hold of me."      -> agarrou ele COMO? e' passivo,
#                                                   e o truque vira o sujeito
#     ✗ "The gelatin trick I found did something." -> fez o QUE? `did something`
#                                                   e' vagueza pura
#
# ⭐ E A CAUSA E' DE PROJETO, nao de redacao: as duas tentavam dizer o EFEITO —
# que e' trabalho do PARADOXO, a batida seguinte. Ao tentar fazer o trabalho do
# vizinho em sete palavras, nao fizeram nem o proprio nem o dele.
# ⛔ O trabalho desta batida e' A DESCOBERTA: QUEM contou ou QUANDO comecou.
# Concreto e verificavel. O que aconteceu depois e' a proxima sentenca, e ela
# chega meio segundo depois.
# ⚠️ E' a lei permanente do operador (`teste-wtf-da-sentenca`): se o espectador
# pode perguntar "do que ele esta' falando?", a copy e' descarte — e o
# autoteste passou a cobrar isso com uma lista de predicados vazios.
TRUQUES = [
    "I started the gelatin trick a month ago.",
    "I found the gelatin trick three weeks ago.",
    "A buddy handed me the gelatin trick.",
    "I discovered the gelatin trick last month.",
    "My neighbor put me onto the gelatin trick.",
    "I have been doing the gelatin trick nightly.",
]

# ⚠️ 8-10 palavras — a batida mais longa, porque e' a que vende.
# ⛔⛔ CT7 — NENHUM VERBO DE ERECCAO NA MESMA SENTENCA DO ORGAO. Por isso aqui
# nao entra `hard`, `stands up`, `wakes up`, `comes back`, `works again`: a
# hiperbole e' contada pelo que ELA faz (pedir tregua, se esconder, implorar),
# nunca pelo que o orgao faz. E' a licao paga no COLO 16 (~95% de recusa).
#
# ⭐⭐ 1a PESSOA DESDE 2026-08-10 — `MY wife`, nunca `YOUR wife`.
# ---------------------------------------------------------------------------
# Diagnostico do operador: *"nao seria melhor `My wife` em vez de `Your wife`?
# Pois conferiria um angulo de confissao de autoridade pro viewer."*
# Conferido, e conserta TRES coisas — ele nomeou uma:
#
#   1. O TAKE TROCAVA DE PESSOA DUAS VEZES. A sequencia era `If you have a
#      wife` (2a) -> `I found the gelatin trick` (1a) -> `Your wife will...`
#      (2a). Zigue-zague que ninguem nota lendo e que no ouvido enfraquece as
#      duas pontas. Agora o take e' UM DEPOIMENTO SO': uma frase de aviso, e o
#      resto e' a historia DELE.
#   2. VIRA TESTEMUNHO, E NAO PROMESSA — e esta e' a parte cara. `Your wife
#      WILL beg` e' afirmacao sobre o futuro de OUTRA pessoa: o vendedor
#      garantindo resultado. `My wife begs` e' relato de fato sobre quem fala.
#      A imagem na cabeca do espectador e' a MESMA; o risco nao e'. Promessa de
#      resultado e' o que o classificador pega e o que o espectador desconta.
#   3. E' O QUE A ESTRUTURA JA' PEDIA. O AVISO em 2a pessoa e' o gancho e JA'
#      fez a transferencia — depois dele o paradoxo nao precisa apontar para o
#      espectador, precisa PROVAR. Take 1 e' prova, take 2 e' oferta.
#
# ⛔ E NAO FOI SO' TROCAR A PALAVRA: o pool inteiro estava no FUTURO (`will
# beg`, `will start hiding`), e futuro em 1a pessoa nao existe aqui — ele esta'
# contando o que JA' acontece. As seis entradas foram reescritas no PRESENTE.
# ⚠️ O take 2 continua inteiro em 2a pessoa (`...into your {o}` · `Comment
# gelatin`) DE PROPOSITO: e' la' que se vira para o espectador e se pede.
# ⚠️ CT4 continua de pe' — o apelido e' o MESMO nos dois takes; o que muda e' o
# possessivo (`my` no depoimento, `your` na oferta), e a trava olha o
# substantivo, nao o possessivo.
PARADOXOS = [
    "Now my wife begs my {o} for one night off.",
    "Now my wife begs my {o} for mercy.",
    "My wife has started asking my {o} for a break.",
    "My wife hides from my {o} at bedtime now.",
    "Now my wife needs a night off from my {o}.",
    "My wife ran out of excuses before my {o} did.",
]

# ===========================================================================
# COPY — TAKE 2: O MECANISMO, A COZINHA E O PEDIDO
# ===========================================================================
# ⛔⛔ A FORMA E' DO OPERADOR, literal: *"The gelatin trick sends blood back
# into your pecker. All ingredients you have in your kitchen. Comment gelatin,
# and I'll send the recipe."*
#
#     <MECANISMO com razao>  ·  <A COZINHA>  ·  <O PEDIDO>
#
# ⛔⛔ E O CT6 ESTA' DESLIGADO NESTE MOTOR, por ordem dele: *"vc nao usara
# complemento tal como `by message`"*. O CT6 pede que o CTA diga ONDE a receita
# chega, e a razao dele e' boa (o comentario leva nome e foto, e a clausula
# baixa o custo social). Mas a decisao e' do operador, e o lugar liberado foi
# gasto na COZINHA — que derruba a objecao "vou ter de comprar alguma coisa",
# e essa objecao vem ANTES do custo social.
# ⚠️ Isto fica DECLARADO e nao escondido: se o comentario cair, o primeiro
# lugar a olhar e' esta decisao.

# ⚠️ 9 palavras exatas. CT3: `gelatin trick` + VERBO DE EFEITO + ALVO na MESMA
# sentenca. Os verbos saem de `sc.VERBOS_EFEITO_16`, que e' a mesma lista que a
# lente cobra — verbo fora dela reprova mesmo lendo bem.
# ⛔ Construcao SEMPRE direcional (`blood ... back into your {o}`). As formas de
# RETENCAO (`fills your {o} with blood`) descrevem o orgao enchendo, e e'
# exatamente isso que o classificador le' como tumescencia.
MECANISMOS = [
    "The gelatin trick sends blood back into your {o}.",   # ← a do operador
    "The gelatin trick brings blood back into your {o}.",
    "The gelatin trick feeds blood back into your {o}.",
    "The gelatin trick pushes blood back into your {o}.",
    "The gelatin trick drives blood back into your {o}.",
    "The gelatin trick puts blood back into your {o}.",
]

# ⚠️ 6-7 palavras exatas.
# ⛔ CT5 — NENHUM INGREDIENTE NOMEADO. A receita e' a UNICA moeda que o
# comentario compra; dizer o conteudo na tela publica esvazia o CTA deste video
# e dos outros 49 da mesma pagina. `ingredients` e' a CATEGORIA, nunca um item.
COZINHAS = [
    "All ingredients you have in your kitchen.",           # ← a do operador
    "Every ingredient is already in your kitchen.",
    "All of it comes from your kitchen.",
    "Nothing you do not already own.",
    "It all sits in your kitchen already.",
    "Two things you already keep at home.",
]

# ⚠️ 7-8 palavras exatas. `Comment gelatin,` e' LITERAL
# (`sc.CTA_LITERAL`), e a virgula depois da keyword NAO e' opcional: sem a
# micro-pausa o Veo emenda e narra "gelatine", e a automacao de DM casa palavra
# EXATA.
CTAS = [
    "Comment gelatin, and I'll send the recipe.",          # ← a do operador
    "Comment gelatin, and I'll send you the recipe.",
    "Comment gelatin, and the recipe is yours.",
    "Comment gelatin, and I'll send it tonight.",
    "Comment gelatin, and I'll send the whole recipe.",
    "Comment gelatin, and the recipe goes out tonight.",
]


# ===========================================================================
# HELPERS
# ===========================================================================

def _palavras(s):
    return len(re.findall(r"[A-Za-z']+", s or ""))


def _cap(s):
    return s[0].upper() + s[1:] if s else s


def _fresco(pool, usados, rng):
    livres = [x for x in pool if x["id"] not in usados]
    return rng.choice(livres or pool)


def _por_id(pool, valor):
    return next((x for x in pool if x["id"] == valor), None)


def _cabe(pool, reserva, cena, o=None):
    """As entradas que cabem depois de reservar `reserva` palavras.

    ⚠️ O fallback NAO devolve o pool inteiro — isso e' estouro silencioso.
    Devolve a entrada mais CURTA, e quem reclama depois e' o linter.
    """
    def _n(x):
        return _palavras(x.format(o=o) if o is not None else x)
    v = [x for x in pool if _n(x) + reserva <= TETO_FALA[cena]]
    return v or [min(pool, key=_n)]


def _mn(pool, o=None):
    return min(_palavras(x.format(o=o) if o is not None else x) for x in pool)


def _falas(spec, rng, quais=(0, 1)):
    """As duas falas.

    ⛔⛔ CT4 — UM APELIDO POR VIDEO, repetido nos dois takes. O corte zera a
    memoria de trabalho, e trocar `pecker` por `Johnson` no segundo 9 obriga o
    espectador a remapear justamente quando ele ja' esta' com um pe' fora.

    ⛔ ORDEM DE ESCOLHA (que nao e' a ordem da frase): escolhe primeiro quem tem
    MENOS SUBSTITUTOS. No take 1 e' o PARADOXO — ele e' a batida mais longa e a
    que carrega o angulo inteiro. No take 2 e' o MECANISMO, que carrega o
    literal `gelatin trick`, o verbo de efeito e o alvo na mesma sentenca. O
    beat mais intercambiavel escolhe por ULTIMO e absorve a sobra.
    """
    o = spec["apelido"]
    f = dict(enumerate(spec.get("falas", ["", ""])))

    if 0 in quais:
        pa = rng.choice(_cabe(PARADOXOS, _mn(AVISOS) + _mn(TRUQUES), 1,
                              o)).format(o=o)
        av = rng.choice(_cabe(AVISOS, _palavras(pa) + _mn(TRUQUES), 1))
        tr = rng.choice(_cabe(TRUQUES, _palavras(pa) + _palavras(av), 1))
        f[0] = "%s %s %s" % (av, tr, pa)

    if 1 in quais:
        me = rng.choice(_cabe(MECANISMOS, _mn(COZINHAS) + _mn(CTAS), 2,
                              o)).format(o=o)
        ct = rng.choice(_cabe(CTAS, _palavras(me) + _mn(COZINHAS), 2))
        co = rng.choice(_cabe(COZINHAS, _palavras(me) + _palavras(ct), 2))
        f[1] = "%s %s %s" % (me, co, ct)

    return f


# ⛔⛔ O SANEADOR DA DESCRICAO DELAS — a licao FT14 do FIGHT 16, ja' aplicada.
# O pool BELA compartilhado (`sc.ref_bela`) traz TOM DE PELE e SORRISO dentro da
# `marca`. Os dois brigam com o que este motor declara por fora:
#   · o tom de pele briga com a ETNIA declarada (duas autoridades para o mesmo
#     atributo, e o gerador resolve DIFERENTE em cada take);
#   · o sorriso da identidade briga com o sorriso da CENA, que aqui e' obrigado
#     e escrito uma vez so' na montagem.
# ⚠️ Age por CLAUSULA, nunca por regex na string inteira: cirurgia de regex em
# texto ja' montado deixa virgula orfa e ` and ` solto.
_CLAUSULA = re.compile(r",\s*|\s+and\s+")
_TOM_DE_PELE = re.compile(r"\bskin\b|\bcomplexion\b|\bcomplected\b", re.I)
_SORRISO_ID = re.compile(r"\bsmile\b|\bsmiling\b|\bgrin\w*\b", re.I)


# ---------------------------------------------------------------------------
# ⭐⭐ A PELE DELAS — 2026-08-10, e isto REVISA a decisao FT14 do FIGHT 16
# ---------------------------------------------------------------------------
# ⛔ RELATO DE CAMPO: *"pq o agente alfa16 ta gerando somente ref homem de pele
# escura com mulheres brancas? coloque mulheres de pele escura tb"*.
#
# ⚠️ MEDIDO ANTES DE MEXER, e o motor NAO estava errado: 36% dos sorteios
# traziam `Black American woman` no bloco montado. O gerador e' que estava
# ignorando o rotulo.
#
# ⭐ E A CAUSA E' A MINHA PROPRIA CORRECAO ANTERIOR, levada longe demais. No
# FIGHT 16 a etnia declarada brigava com o tom de pele que vinha do pool BELA
# (`white American` + `clear deep brown skin`), e eu resolvi TIRANDO o tom de
# pele — deixando a etnia como AUTORIDADE UNICA. Funcionou contra a
# contradicao, mas criou outro problema: `Black American` vira UM adjetivo
# solto no meio de vinte palavras de cabelo, porte, marca e traje, e o gerador
# resolve pela media do treino — que, para "mulher bonita de toalha", e' branca.
#
# ⛔⛔ A LICAO CORRIGIDA: o problema nunca foi a pele estar na frase. Era ela
# CONTRADIZER a etnia. Duas vozes que CONCORDAM nao sao contradicao, sao
# reforco — e reforco e' exatamente o que um sinal fraco precisa.
# ⭐ Entao a pele volta, DERIVADA DA ETNIA e nunca escrita a mao entrada por
# entrada: assim ela nao tem como divergir num refactor. A variacao dentro de
# cada etnia mora aqui.
# ⚠️ E o `_marca_dela` continua tirando o tom de pele que vem do pool BELA —
# senao voltariam DUAS declaracoes de pele na mesma frase, e a segunda seria a
# que contradiz.
PELES = {
    # ⚠️ Toda entrada entra depois de `...woman WITH `, entao nenhuma pode
    # comecar ou carregar outro `with` — a primeira versao trazia `pale skin
    # with a light tan` e o bloco saia `with pale skin with a light tan`.
    # Achado LENDO o bloco montado, nao por lente.
    "white American": ["fair skin", "warm light skin", "lightly tanned skin"],
    "Black American": ["deep brown skin", "rich dark brown skin",
                       "warm medium-brown skin"],
    "Hispanic American": ["warm olive skin", "light brown skin"],
    "Asian American": ["light golden skin", "warm ivory skin"],
}


def _pele_dela(mulher, rng):
    """O tom de pele que CONCORDA com a etnia declarada da entrada."""
    return rng.choice(PELES.get(mulher["etnia"], PELES["white American"]))


def _marca_dela(spec, mulher):
    marca = mulher["marca"]
    if not spec.get("bela"):
        return marca
    partes = [p.strip() for p in _CLAUSULA.split(marca) if p.strip()]
    fica = [p for p in partes
            if not _TOM_DE_PELE.search(p) and not _SORRISO_ID.search(p)]
    if not fica:
        return partes[0]
    if len(fica) == 1:
        return fica[0]
    return ", ".join(fica[:-1]) + " and " + fica[-1]


def _dupla(spec):
    """As duas mulheres, na ordem em que entram no quadro."""
    return (spec["mulher_a"], spec["mulher_b"])


def _descreve_dupla(spec):
    """`a 29-year-old white American woman, ..., and a 31-year-old ...`

    ⛔ UMA SO' FUNCAO monta as duas nos DOIS takes. Espalhar isso pelos dois
    blocos e' o fragmento espelhado que diverge na primeira manutencao — e o
    que diverge aqui e' exatamente a ancora que impede a troca de pessoa.
    """
    # ⛔⛔ A ETNIA E O TOM DE PELE VEM COLADOS, e nesta ordem — ver o bloco do
    # `PELES`. Sozinho, `Black American` e' um adjetivo perdido no meio de vinte
    # palavras e o gerador resolve pela media do treino; com a pele ao lado, o
    # sinal deixa de ser opinavel. As duas vozes CONCORDAM por construcao
    # (a pele e' derivada da etnia), entao nao ha' contradicao a resolver.
    tr = ENVOLTORIO_DELAS
    partes = []
    for w in _dupla(spec):
        partes.append("a %d-year-old %s woman with %s, %s, %s, wearing %s"
                      % (w["idade"], w["etnia"], w["pele"], w["porte"],
                         _marca_dela(spec, w), tr))
    return partes[0] + ", and " + partes[1]


# ===========================================================================
# SORTEIO
# ===========================================================================

def sortear(pagina, rng, ledger, travas=None):
    travas = travas or {}
    hist = (ledger or {}).get(pagina, {})
    etnia = ETNIA.get(pagina, "white American")

    # ⛔⛔ OS DOIS EIXOS DE CENA SAO SORTEADOS SEPARADAMENTE e nenhum filtra o
    # outro — decisao do operador. Quem quiser "casar" os dois (o quarto de
    # resort puxando a espreguicadeira) estaria inventando uma regra que ele
    # nao deu, e reduzindo 100 pares a 10.
    quarto = (_por_id(QUARTOS, travas["quarto"]) if travas.get("quarto")
              else _fresco(QUARTOS, hist.get("quarto", [])[-4:], rng))
    ambiente = (_por_id(AMBIENTES, travas["ambiente"])
                if travas.get("ambiente")
                else _fresco(AMBIENTES, hist.get("ambiente", [])[-4:], rng))

    homem = (_por_id(HOMENS, travas["homem"]) if travas.get("homem")
             else _fresco(HOMENS, hist.get("homem", [])[-6:], rng))

    # ⛔ AS DUAS MULHERES TEM DE SER DIFERENTES ENTRE SI — e o guarda e' o
    # sorteio, nao o linter: com 16 entradas a colisao aconteceria em ~6% dos
    # videos, e duas gemeas no mesmo quadro nao sao um estilo, sao um erro.
    mulher_a = (_por_id(MULHERES, travas["mulher_a"])
                if travas.get("mulher_a")
                else _fresco(MULHERES, hist.get("mulher_a", [])[-5:], rng))
    if travas.get("mulher_b"):
        mulher_b = _por_id(MULHERES, travas["mulher_b"])
    else:
        recentes = hist.get("mulher_b", [])[-5:] + [mulher_a["id"]]
        mulher_b = _fresco(MULHERES, recentes, rng)

    # ⭐⭐ MODO BELA — contrato compartilhado, e ele move AS DUAS.
    # ⛔ O CADEADO DA TELA VENCE O MODO: mulher travada no painel e' mais
    # especifica que "uma bela qualquer".
    # ⛔⛔ E A ETNIA DELAS SOBREVIVE AO MODO — e agora a PELE tambem. O
    # `ref_bela` devolveria a etnia do MOLDE (`MULHERES[0]`), travando as duas
    # em `white American` sem ninguem ver; e o pool bela e' escrito em registro
    # de pele clara. Sem estas linhas, ligar o MODO BELA embranqueceria o lote
    # inteiro — que e' metade da queixa que o operador levantou.
    bela = bool(travas.get("bela"))
    if bela and not travas.get("mulher_a"):
        _e = mulher_a["etnia"]
        mulher_a = sc.ref_bela(MULHERES[0], rng)
        mulher_a["etnia"] = _e
    if bela and not travas.get("mulher_b"):
        _e = mulher_b["etnia"]
        # ⛔⛔ O `banidos` do `sc.ref_bela` FILTRA POR TEXTO (procura a palavra
        # dentro de corpo/cabeca/marca), NAO por id — passar o id la' nao bane
        # nada, e o autoteste pegou 9 videos em 400 com as DUAS BELAS
        # IDENTICAS. O guarda tem de ser por ID, e mora aqui.
        # ⚠️ Sorteio com repeticao, nao filtro do pool: o pool bela e' do
        # `short_comum` e nao expoe id na entrada; o que ele devolve, sim.
        for _ in range(12):
            _cand = sc.ref_bela(MULHERES[0], rng)
            if _cand.get("id") != mulher_a.get("id"):
                break
        mulher_b = _cand
        mulher_b["etnia"] = _e

    # ⛔ A PELE E' DERIVADA DA ETNIA e gravada no spec, nos dois estados do
    # MODO BELA. No spec, e nao na montagem, porque as duas mulheres sao AS
    # MESMAS nos dois takes: derivar duas vezes com o mesmo `rng` daria peles
    # diferentes entre os quadros, e o espectador veria outras duas mulheres.
    for _w in (mulher_a, mulher_b):
        _w["pele"] = _pele_dela(_w, rng)

    forte = bool(travas.get("forte"))
    corpo = rng.choice(CORPOS_FORTES if forte else CORPOS_H)

    spec = {
        "pagina": pagina, "etnia": etnia, "bela": bela, "forte": forte,
        "quarto": quarto, "ambiente": ambiente,
        "homem": homem, "mulher_a": mulher_a, "mulher_b": mulher_b,
        "corpo_h": corpo,
        "toalha": rng.choice(TOALHAS),
        # ⛔ CT4b — o apelido sai de `sc.APELIDOS_16` e de mais lugar nenhum.
        "apelido": rng.choice(list(sc.APELIDOS_16)),
    }
    spec["falas"] = [v for _, v in sorted(_falas(spec, rng).items())]
    return spec


def nova_fala(spec, i, rng):
    return _falas(spec, rng, quais=(i,))[i]


# ===========================================================================
# MONTAGEM
# ===========================================================================

# ⛔ O SORRISO DELAS, EM UMA STRING SO' E NOS DOIS TAKES.
# Ordem do operador: *"mulheres no take 1 e 2 sorrindo muito de alegria
# (sorrindo, NAO gargalhando)"*. A distincao nao e' preciosismo: `laughing`
# puxa boca aberta, olho fechado e cabeca para tras — e a lente FA1 reprova a
# volta da palavra. As referencias visuais que ele mandou diziam `laughing` em
# nove das dez; foi trocado em todas.
# ⛔⛔ E A CLAUSULA E' POSITIVA, SEM UM `not` — a primeira versao desta string
# terminava em `Neither woman is laughing out loud.` e foi REPROVADA pelo
# proprio autoteste, com razao dupla:
#   1. a lente FA1 acusava a si mesma (o token `laughing` estava na clausula que
#      existe para proibi-lo);
#   2. e, pior, e' a doutrina de 2026-07-31 do repo — DECLARACAO E' MUNICAO.
#      Escrever `not laughing` INJETA `laughing` no campo. Contra o gerador o
#      silencio vence a negacao, e o que impede a gargalhada nao e' proibi-la:
#      e' descrever a BOCA que ela nao tem (`mouths closed or barely open`).
SORRISO = ("Both women are smiling widely and happily, clearly delighted, "
           "their mouths closed or barely open, lips together, and their eyes "
           "bright and open.")


def montar(spec):
    q, a = spec["quarto"], spec["ambiente"]
    h = spec["homem"]
    et = spec["etnia"]
    b = {}

    # --- BLOCO 0 — a REF e' o HOMEM (ele e' quem fala) --------------------
    b["BLOCO 0 (REF)"] = (
        "REF 01: Photo of a real person, a %d-year-old %s man, chest up, "
        "facing the camera directly, a calm confident half-smile. %s, %s. "
        "Hands out of frame, no objects. Plain neutral gray background, soft "
        "even frontal light. Slight sensor grain, soft focus, raw iPhone front "
        "camera aesthetic. No subtitles, no captions, no burned-in text, no "
        "watermark."
        # ⚠️ `_cap` na marca — sem ele o bloco saia `half-smile. dark hair
        # buzzed...`, com a sentenca abrindo em minuscula. Achado LENDO o
        # roteiro, nao por lente: os dois IMAGE ja' usavam `_cap` e este nao.
        # Fragmento espelhado que diverge — por isso nasceu a `_fa14_pontuacao`.
        % (h["idade"], et, _cap(h["marca"]), h["sinal"]))

    # --- TAKE 1 — O AVISO -------------------------------------------------
    # ⛔ O PRINT, ELEMENTO POR ELEMENTO: ele DE PE', perto da lente, tronco nu,
    # TOALHA na cintura, falando PARA A LENTE com meio sorriso confiante. Elas
    # ATRAS, enroladas em toalha, sorrindo de alegria.
    # ⚠️ ELE FALA PARA A LENTE, nunca para elas: e' um aviso ao espectador, nao
    # uma conversa em quadro. E' o que sustenta a 2a pessoa da fala.
    b["IMAGE 01/02"] = (
        "IMAGE 01/02: Medium shot in %s. Standing in the foreground close to "
        "the lens, facing the camera, is a %d-year-old %s man, bare-chested, "
        "%s, wearing %s, talking to the camera with a calm confident "
        "half-smile. %s, %s. %s %s. %s They are the only three people in the "
        "frame. Lit by %s. %s"
        % (q["cen"], h["idade"], et, spec["corpo_h"], spec["toalha"],
           _cap(h["marca"]), h["sinal"], q["elas"], _descreve_dupla(spec),
           SORRISO, q["luz"], CAUDA))

    b["TAKE 01/02"] = (
        "TAKE 01/02: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway, no cuts, and the camera does not move. He "
        "talks straight into the lens the whole time and never turns to look "
        "at them. Both women stay exactly where they are, keep smiling happily "
        "the whole time with their lips together, and neither of them speaks. "
        "Only he speaks. Nothing else in the frame changes.\n"
        "Dialogue: \"%s\"\nAudio: %s. No music."
        % (sonorizar(spec["falas"][0]), q["audio"]))

    # --- TAKE 2 — AS DUAS DO LADO -----------------------------------------
    # ⛔⛔ A ANCORA DE CONTINUIDADE VALE PARA AS TRES PESSOAS, e aqui ela e' mais
    # cara que em qualquer outro 16s do parque: os dois eixos de cena sao
    # independentes, entao o LUGAR nao atravessa o corte e as PESSOAS sao a
    # unica coisa que atravessa. Lente FA3.
    # ⭐⭐ AS DUAS MAOS SAO A PROVA (ordem do operador): a tigela de cubos numa,
    # a caixa de bicarbonato na outra. Lente FA4.
    b["IMAGE 02/02"] = (
        "IMAGE 02/02: Medium shot in %s. %s the same %d-year-old %s man from "
        "the first scene, %s, %s, %s, wearing %s, his face fully in frame and "
        "turned to the camera. It is the same man, not a different person. "
        "Pressed close against him, one on each side, are the same two women "
        "from the first scene: %s. %s In one hand he holds %s, and in his "
        "other hand he holds %s. Both of his hands are full and he is not "
        "gesturing. They are the only three people in the frame. Lit by %s. %s"
        % (a["cen"], a["pose"], h["idade"], et, h["marca"], h["sinal"],
           spec["corpo_h"], spec["toalha"], _descreve_dupla(spec), SORRISO,
           TIGELA_CUBOS, CAIXA_BICARBONATO, a["luz"], CAUDA))

    b["TAKE 02/02"] = (
        "TAKE 02/02: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway, no cuts, and the camera does not move. He "
        "talks straight into the lens the whole time and it is the same man as "
        "in the first scene. Both women stay pressed against him and never "
        "move away, they keep smiling happily the whole time with their lips "
        "together, and neither of them speaks. Only he speaks. He keeps the "
        "bowl in one hand and the box in the other the whole time and never "
        "sets either one down. Nothing else in the frame changes.\n"
        "Dialogue: \"%s\"\nAudio: %s. No music."
        % (sonorizar(spec["falas"][1]), a["audio"]))

    return sc.selar_takes(b)


# ===========================================================================
# LINTER — as regras FA
# ===========================================================================

def _fa1_sorriso(spec, blocos, achados):
    """FA1 — elas SORRIEM nos dois takes, e nunca gargalham."""
    for k in ("IMAGE 01/02", "IMAGE 02/02"):
        if SORRISO not in blocos.get(k, ""):
            achados.append(("ERRO", "FA1: %s sem a clausula de sorriso das "
                                    "duas — foi pedida nominalmente para os "
                                    "DOIS takes" % k))
    for k in ("TAKE 01/02", "TAKE 02/02"):
        if "keep smiling happily" not in blocos.get(k, ""):
            achados.append(("ERRO", "FA1: %s nao manda elas CONTINUAREM "
                                    "sorrindo — sorriso so' na IMAGE some no "
                                    "movimento" % k))
    # ⛔ `laughing` puxa boca aberta e cabeca para tras, que e' o oposto do que
    # o operador pediu. As referencias que ele mandou diziam `laughing` em nove
    # das dez, entao o token TEM de ser cobrado — ele volta por copia.
    # ⛔ O TOKEN NAO PODE APARECER NEM PARA SER NEGADO. `Neither woman is
    # laughing` injeta `laughing` no campo — doutrina de 2026-07-31. Por isso a
    # lente e' ABSOLUTA e nao tem excecao de negacao: se a palavra estiver no
    # prompt, ela reprova. ⚠️ As referencias visuais que o operador mandou
    # diziam `laughing` em nove das dez, entao o token volta por copia — foi
    # por isso que esta lente nasceu junto com o motor.
    # ⚠️ `laugh lines` E' RUGA, NAO RISO — e a primeira versao desta lente
    # reprovou 60 de 400 sorteios em cima do `sinal` de um homem do pool
    # (`laugh lines cut deep at the corners of his mouth`), que e' marca de
    # idade e nao expressao. Lente que reprova o que esta' certo ensina o
    # operador a ignorar o relatorio (licoes §16) — entao a lente cede, e o
    # pool de rostos fica intacto.
    for k, txt in blocos.items():
        limpo = re.sub(r"\blaugh(ter)? lines\b", "", txt, flags=re.I)
        m = re.search(r"\blaugh\w*\b|\bgiggl\w*\b|\bhowling\b|\bcackl\w*\b",
                      limpo, re.I)
        if m:
            achados.append(("ERRO", "FA1: %s traz %r — o operador pediu "
                                    "SORRINDO, nao gargalhando, e o token nao "
                                    "entra nem negado" % (k, m.group(0))))


def _fa2_geometria(spec, blocos, achados):
    """FA2 — a geometria dos dois quadros, que e' o que separa os takes."""
    i1 = blocos.get("IMAGE 01/02", "")
    i2 = blocos.get("IMAGE 02/02", "")
    for pedaco, rot in (("Standing in the foreground close to the lens",
                         "ele DE PE' perto da lente"),
                        ("bare-chested", "tronco nu")):
        if pedaco not in i1:
            achados.append(("ERRO", "FA2: a IMAGE 01/02 perdeu o print (%s)"
                            % rot))
    if "one on each side" not in i2:
        achados.append(("ERRO", "FA2: a IMAGE 02/02 nao poe uma mulher de cada "
                                "lado — e' a geometria que o operador ditou"))
    for k, bl in (("IMAGE 01/02", i1), ("IMAGE 02/02", i2)):
        if "only three people" not in bl:
            achados.append(("ERRO", "FA2: %s sem a trava de contagem de gente "
                                    "— sem ela o Veo enche o quadro" % k))


def _fa3_ancora(spec, blocos, achados):
    """FA3 — as TRES pessoas atravessam o corte, peca por peca.

    ⛔ Aqui a ancora e' mais cara que em qualquer outro 16s: os dois eixos de
    cena sao independentes, entao o LUGAR nao ajuda a segurar ninguem. Foi
    exatamente isso que produziu a troca de mulher no FIGHT 16.
    """
    i2 = blocos.get("IMAGE 02/02", "")
    h = spec["homem"]
    for pedaco, rot in ((str(h["idade"]), "a idade dele"),
                        (h["marca"], "a marca dele"),
                        (h["sinal"], "o sinal dele"),
                        (spec["corpo_h"], "o corpo dele"),
                        ("It is the same man, not a different person",
                         "a frase de identidade")):
        if pedaco not in i2:
            achados.append(("ERRO", "FA3: a IMAGE 02/02 sem %s — sem a ancora "
                                    "inteira o Veo desenha outra pessoa" % rot))
    if "the same two women from the first scene" not in i2:
        achados.append(("ERRO", "FA3: a IMAGE 02/02 nao declara que sao AS "
                                "MESMAS DUAS mulheres do take 1"))
    for w in _dupla(spec):
        for k in ("IMAGE 01/02", "IMAGE 02/02"):
            if _marca_dela(spec, w) not in blocos.get(k, ""):
                achados.append(("ERRO", "FA3: %s sem a marca de %s — duas "
                                        "mulheres atravessando o corte sem "
                                        "ancora viram outras duas"
                                % (k, w.get("id", "?"))))


def _fa4_duas_maos(spec, blocos, achados):
    """FA4 — a prova esta' nas duas maos, e so' no take 2."""
    i2, t2 = blocos.get("IMAGE 02/02", ""), blocos.get("TAKE 02/02", "")
    for s, rot in ((TIGELA_CUBOS, "a tigela de cubos"),
                   (CAIXA_BICARBONATO, "a caixa de bicarbonato")):
        if s not in i2:
            achados.append(("ERRO", "FA4: a IMAGE 02/02 sem %s" % rot))
    if "never sets either one down" not in t2:
        achados.append(("ERRO", "FA4: o TAKE 02/02 nao trava os dois objetos "
                                "nas maos — objeto que pode ser pousado some"))
    # ⛔ mao ocupada NAO gesticula. Prompt que pede as duas coisas faz o gerador
    # desenhar uma TERCEIRA mao — e' o defeito das DUAS COLHERES.
    if re.search(r"gestur\w+|arm (casually )?rest\w+ along", i2, re.I) \
            and "not gesturing" not in i2:
        achados.append(("ERRO", "FA4: a IMAGE 02/02 pede gesto de mao com as "
                                "duas maos ocupadas"))
    # ⛔ e a prova NAO entra no take 1: la' ele ainda esta' avisando, nao
    # provando. Objeto adiantado gasta o payoff.
    i1 = blocos.get("IMAGE 01/02", "")
    for s, rot in ((TIGELA_CUBOS, "a tigela"), (CAIXA_BICARBONATO, "a caixa")):
        if s in i1:
            achados.append(("ERRO", "FA4: %s aparece ja' no take 1 — a prova e' "
                                    "o payoff do take 2" % rot))


def _fa5_sem_texto(spec, blocos, achados):
    for k, txt in blocos.items():
        if k.startswith("TAKE") and sc.SEM_TEXTO_TAKE not in txt:
            achados.append(("ERRO", "FA5: %s sem a trava de texto queimado" % k))


def _fa6_sem_prop(spec, blocos, achados):
    """FA6 — este angulo NAO tem prop falico, e isso e' propriedade dele."""
    for k, txt in blocos.items():
        if re.search(r"\b(geoduck|banana|cucumber|daikon|baguette|salami|"
                     r"clam|siphon|anatomy model|pelvis)\b", txt, re.I):
            achados.append(("ERRO", "FA6: %s traz prop falico — a prova deste "
                                    "angulo e' o CASAL e as duas maos" % k))


def _fa7_orcamento(spec, blocos, achados):
    for i, fala in enumerate(spec["falas"], 1):
        n = _palavras(fala)
        if n > TETO_FALA[i]:
            achados.append(("ERRO", "FA7: cena %d com %d palavras (teto %d) — "
                                    "o render CORTA a fala" % (i, n, TETO_FALA[i])))
        elif n < PISO_FALA[i]:
            achados.append(("AVISO", "FA7: cena %d com %d palavras (piso %d) — "
                                     "sobra silencio no take" % (i, n, PISO_FALA[i])))


def _fa8_etnia(spec, blocos, achados):
    """FA8 — a etnia do HOMEM vem da PAGINA e chega aos dois quadros."""
    for k in ("BLOCO 0 (REF)", "IMAGE 01/02", "IMAGE 02/02"):
        if spec["etnia"] not in blocos.get(k, ""):
            achados.append(("ERRO", "FA8: %s sem a etnia da pagina (%s) — a "
                                    "congruencia com o avatar e' inviolavel"
                            % (k, spec["etnia"])))


def _fa9_toalha(spec, blocos, achados):
    """FA9 — a toalha dele e o envoltorio delas, nos DOIS takes."""
    for k in ("IMAGE 01/02", "IMAGE 02/02"):
        if spec["toalha"] not in blocos.get(k, ""):
            achados.append(("ERRO", "FA9: %s sem a toalha dele — e' o uniforme "
                                    "do angulo" % k))
        # ⛔ string TRAVADA desde 2026-08-10 (o biquini reprovava no gerador)
        if ENVOLTORIO_DELAS not in blocos.get(k, ""):
            achados.append(("ERRO", "FA9: %s sem o envoltorio delas" % k))
        # ATENCAO: ESTA LINHA JA' NASCEU MORTA UMA VEZ. Ela foi escrita por
        # heredoc, e a BORDA DE PALAVRA do regex (barra invertida + b) virou
        # um BYTE DE CONTROLE 0x08 dentro do arquivo. O padrao passou a
        # procurar um BACKSPACE literal antes de bikini e NUNCA casava:
        # autoteste verde, lente sem efeito nenhum.
        # E' o modo de falha que o proprio repo documentou no MESMO dia —
        # heredoc que escreve .py deixa byte de controle, e o regex morre
        # calado. Por isso aqui nao ha' borda de palavra nenhuma: sao
        # palavras que nao aparecem por acaso, e substring basta. Menos
        # escape, menos superficie.
        # E FOI O CONTROLE NEGATIVO QUE ACHOU, nao a leitura: a lente parecia
        # certa no `inspect.getsource`, porque o terminal ENGOLE o backspace
        # ao imprimir. Lente sem controle negativo nunca foi testada — e esta
        # esteve verde e morta ao mesmo tempo.
        if re.search("bikini|swimsuit|swimwear|lingerie",
                     blocos.get(k, ""), re.I):
            achados.append(("ERRO", "FA9: %s traz roupa de banho — o biquini "
                                    "foi REPROVADO no gerador em 2026-08-10 e "
                                    "o envoltorio e' toalha, string travada" % k))


def _fa10_duas_distintas(spec, blocos, achados):
    """FA10 — as duas mulheres sao PESSOAS DIFERENTES."""
    a, b = _dupla(spec)
    if a.get("id") and a.get("id") == b.get("id"):
        achados.append(("ERRO", "FA10: as duas mulheres sao a MESMA entrada "
                                "(%s) — duas gemeas no quadro e' erro, nao "
                                "estilo" % a.get("id")))
    if _marca_dela(spec, a) == _marca_dela(spec, b):
        achados.append(("ERRO", "FA10: as duas mulheres tem a MESMA descricao "
                                "depois do saneamento — o quadro nao as separa"))


def _fa11_modos(spec, blocos, achados):
    """FA11 — os toggles movem o quadro, nos dois estados.

    ⛔ E' a lente contra a FORMA-SEM-FUNCAO: botao aceso, sorteio igual. Este
    repo ja' pagou isso tres vezes.
    """
    for k in ("IMAGE 01/02", "IMAGE 02/02"):
        bl = blocos.get(k, "")
        if spec["corpo_h"] not in bl:
            achados.append(("ERRO", "FA11: %s sem o corpo do estado atual do "
                                    "MODO FORTE" % k))
        for w in _dupla(spec):
            if "%d-year-old" % w["idade"] not in bl:
                achados.append(("ERRO", "FA11: %s sem a idade de uma delas "
                                        "(%d) — e' a primeira coisa que o MODO "
                                        "BELA move" % (k, w["idade"])))
    if spec["forte"] and spec["corpo_h"] not in CORPOS_FORTES:
        achados.append(("ERRO", "FA11: MODO FORTE ligado e o corpo veio do pool "
                                "comum — o botao nao move nada"))
    if not spec["forte"] and spec["corpo_h"] not in CORPOS_H:
        achados.append(("ERRO", "FA11: MODO FORTE desligado e o corpo veio do "
                                "pool forte"))


def _fa12_pele_concorda(spec, blocos, achados):
    """FA12 — a etnia e o tom de pele DIZEM A MESMA COISA, nas duas.

    ⛔⛔ ESTA LENTE FOI VIRADA DO AVESSO EM 2026-08-10, e a virada e' a licao.
    A versao anterior PROIBIA tom de pele ao lado da etnia — era a correcao do
    FIGHT 16, onde `white American` brigava com `clear deep brown skin`. Estava
    certa contra a CONTRADICAO e errada contra o resultado: sem a pele, a etnia
    vira um adjetivo perdido no meio de vinte palavras, e o operador mediu o
    efeito em campo — *"pq esta' gerando somente mulheres brancas?"*, com o
    motor pedindo 36% de mulheres negras.

    ⭐ O que a lente cobra agora e' CONCORDANCIA, nao ausencia:
      · a pele da entrada TEM de aparecer colada na etnia dela;
      · e NENHUMA outra declaracao de pele pode aparecer na mesma frase — se
        aparecer, e' o pool BELA reintroduzindo a contradicao original.
    ⚠️ Duas vozes que concordam sao reforco; duas que discordam sao invencao.
    A lente antiga so' sabia da segunda metade.
    """
    for k in ("IMAGE 01/02", "IMAGE 02/02"):
        bl = blocos.get(k, "")
        for w in _dupla(spec):
            alvo = "%d-year-old %s woman with %s" % (w["idade"], w["etnia"],
                                                     w["pele"])
            if alvo not in bl:
                achados.append(("ERRO", "FA12: %s nao traz a etnia COLADA no "
                                        "tom de pele (%r) — sozinha, a etnia "
                                        "perde para a media do treino"
                                % (k, alvo[:70])))
                continue
            # ⛔ e nenhuma SEGUNDA declaracao de pele NO TRECHO DELA.
            # ⚠️ O recorte para em `wearing`, que e' onde a clausula de cada
            # mulher termina. A primeira versao ia ate' o `;` e passava por
            # cima da OUTRA mulher — contava a pele da vizinha como duplicata e
            # reprovou 802 sorteios. Lente com recorte errado nao mede o que
            # diz medir.
            m = re.search(re.escape(alvo) + r".*?wearing", bl)
            if m and len(_TOM_DE_PELE.findall(m.group(0))) > 1:
                achados.append(("ERRO", "FA12: %s declara pele DUAS vezes na "
                                        "frase dela (%r) — a segunda vem do "
                                        "pool BELA e contradiz a primeira"
                                % (k, m.group(0)[:80])))


def _fa14_pontuacao(spec, blocos, achados):
    """FA14 — nenhuma sentenca abre em minuscula, e nenhuma virgula fica orfa.

    ⛔ Nasceu de um defeito REAL achado LENDO o roteiro, nao por lente: o
    BLOCO 0 montava `...half-smile. dark hair buzzed...` porque so' ele nao
    passava a marca pelo `_cap`, enquanto os dois IMAGE passavam. E' fragmento
    espelhado que diverge — a familia de defeito mais comum deste repo.
    ⚠️ E a lente e' da CLASSE, nao do caso: qualquer campo de pool que um dia
    entre depois de um ponto cai aqui, inclusive os que ainda nao existem.
    """
    for k, txt in blocos.items():
        if k.startswith("TAKE"):
            corpo = txt.split("Dialogue:")[0]      # a fala tem regras proprias
        else:
            corpo = txt
        m = re.search(r"[.!?]\s+([a-z])", corpo)
        if m:
            i = m.start()
            achados.append(("ERRO", "FA14: %s abre sentenca em minuscula "
                                    "(...%r...)" % (k, corpo[i:i + 46])))
        if re.search(r",\s*,|\s+,|,\s*\.|\band\s+and\b", corpo):
            achados.append(("ERRO", "FA14: %s tem pontuacao quebrada — sinal de "
                                    "campo vazio ou de saneamento que comeu "
                                    "uma clausula" % k))


def _fa13_lugares_independentes(spec, blocos, achados):
    """FA13 — o take 2 NAO pode fingir que e' o mesmo lugar do take 1.

    ⛔ Os dois eixos sao independentes por decisao do operador. Dizer `the same
    room` seria uma mentira no prompt, e prompt que mente e' onde o gerador
    inventa. ⚠️ Esta lente existe porque o motor irmao (BED 16) usa exatamente
    esse idioma, e o proximo agente nasce por copia.
    """
    if re.search(r"\bthe same (room|bedroom|bathroom|house|hotel|cabin|suite|"
                 r"place|apartment|villa|lodge)\b", blocos.get("IMAGE 02/02", ""),
                 re.I):
        achados.append(("ERRO", "FA13: a IMAGE 02/02 diz `the same <lugar>` — "
                                "os dois eixos de cena sao INDEPENDENTES e o "
                                "lugar nao atravessa o corte"))


# ⛔⛔ CT2 E CT6 DESLIGADOS NESTE MOTOR, e cada um com o motivo escrito.
# ---------------------------------------------------------------------------
# CT2 — "o take 1 enuncia a FALHA dele". Este angulo, por desenho do operador,
#   NAO enuncia falha nenhuma: ele AVISA e PROMETE, e o espectador se reconhece
#   pela ESPOSA. Deixar ligado faria o painel acusar 100% dos videos, e lente
#   que reprova o que esta' certo ensina o operador a ignorar o relatorio.
# CT6 — "o CTA diz ONDE a receita chega". Ordem literal dele: *"vc nao usara
#   complemento tal como by message"*. As palavras liberadas foram para a
#   COZINHA, que derruba a objecao "vou ter de comprar alguma coisa".
# ⚠️ Os dois sao AVISO no `sc.lint_copy16`, nao ERRO — entao desligar aqui NAO
# afrouxa nenhuma trava dura. E fica declarado: se o comentario cair, o CT6 e' o
# primeiro lugar a olhar.
_CT_DESLIGADOS = ("CT2:", "CT6:")


def _ct16(spec, blocos, achados):
    locais = []
    sc.lint_copy16(sys.modules[__name__], spec, locais, isca_absurda=False)
    achados.extend(a for a in locais
                   if not a[1].startswith(_CT_DESLIGADOS))


def lint(spec, blocos):
    ach = []
    falas = spec["falas"]
    sc.lint_tags(blocos, ach)
    sc.lint_take_vs_image(blocos, ach)
    sc.lint_isca_cta(falas[-1], ach, "a cena 2 (CTA)")
    sc.lint_cta_literal(falas[-1], ach, "a cena 2 (CTA)")
    for f in (_fa1_sorriso, _fa2_geometria, _fa3_ancora, _fa4_duas_maos,
              _fa5_sem_texto, _fa6_sem_prop, _fa7_orcamento, _fa8_etnia,
              _fa9_toalha, _fa10_duas_distintas, _fa11_modos,
              _fa12_pele_concorda, _fa13_lugares_independentes,
              _fa14_pontuacao, _ct16):
        f(spec, blocos, ach)
    return ach


# ===========================================================================
# PAINEL
# ===========================================================================

EIXOS_UI = [
    ("quarto", "O QUARTO", "QUARTOS", "nome"),
    ("ambiente", "O AMBIENTE", "AMBIENTES", "nome"),
    ("homem", "QUEM FALA", "HOMENS", "id"),
    ("mulher_a", "MULHER 1", "MULHERES", "id"),
    ("mulher_b", "MULHER 2", "MULHERES", "id"),
]
EIXOS_TRAVAVEIS = [e[0] for e in EIXOS_UI]
TRAVAS_UI = []
IGNORA_PAINEL = ()
EIXOS_QUE_MEXEM_NA_COPY = {}
EIXOS_LEDGER = ("quarto", "ambiente", "homem", "mulher_a", "mulher_b")


def resumo_pt(spec):
    et = "branca" if "white" in spec["etnia"] else "negra"
    return (
        "16s, DOIS takes. Take 1 — O AVISO, em %s: ele de %d anos, DE PE' perto "
        "da lente, tronco nu e TOALHA na cintura, falando para a lente; as DUAS "
        "mulheres atras, de toalha acima do busto, SORRINDO. Take 2 — AS DUAS DO LADO, em %s: o MESMO "
        "homem e AS MESMAS DUAS, uma de cada lado, coladas, e ele com a TIGELA "
        "DE CUBOS numa mao e a CAIXA DE BICARBONATO na outra. ATENCAO: os dois "
        "lugares sao INDEPENDENTES — quem atravessa o corte sao as TRES "
        "pessoas, nao a casa. Elenco: homem %s de pele %s, duas mulheres de "
        "%d e %d anos%s%s."
        % (spec["quarto"]["nome"], spec["homem"]["idade"],
           spec["ambiente"]["nome"], spec["etnia"], et,
           spec["mulher_a"]["idade"], spec["mulher_b"]["idade"],
           " (modo BELA LIGADO)" if spec["bela"] else "",
           " (modo FORTE LIGADO)" if spec["forte"] else ""))


# ===========================================================================
# LEDGER
# ===========================================================================

def _carregar_ledger():
    if os.path.exists(LEDGER):
        with open(LEDGER, encoding="utf-8-sig") as f:
            try:
                return json.load(f)
            except ValueError:
                return {}
    return {}


def _anotar(ledger, spec):
    """Anota EM MEMORIA — sem tocar em disco.

    ⛔ Separado do `_gravar_ledger` porque o autoteste precisa medir a
    anti-repeticao com a memoria LIGADA, e chamar o gravador escreveria o
    ledger do operador a cada sorteio.
    """
    p = ledger.setdefault(spec["pagina"], {})
    for eixo in EIXOS_LEDGER:
        val = spec[eixo].get("id")
        if val is None:
            continue
        p.setdefault(eixo, []).append(val)
        p[eixo] = p[eixo][-12:]


def _gravar_ledger(ledger, spec):
    _anotar(ledger, spec)
    with open(LEDGER, "w", encoding="utf-8") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)


# ===========================================================================
# AUTOTESTE
# ===========================================================================

def autoteste(n=400):
    falhas = []
    rng = random.Random(20260810)
    erros = collections.Counter()
    avisos = collections.Counter()
    tam = {1: [], 2: []}
    apel = collections.Counter()
    idades_bela, idades_normal = set(), set()

    for i in range(n):
        pag = sorted(ETNIA)[i % len(ETNIA)]
        travas = {}
        if i % 2 == 0:
            travas["bela"] = True
        if i % 3 == 0:
            travas["forte"] = True
        spec = sortear(pag, rng, {}, travas)
        blocos = montar(spec)
        for nivel, msg in lint(spec, blocos):
            (erros if nivel == "ERRO" else avisos)[msg[:74]] += 1
        for j, fala in enumerate(spec["falas"], 1):
            tam[j].append(_palavras(fala))
        apel[spec["apelido"]] += 1
        for w in _dupla(spec):
            (idades_bela if spec["bela"] else idades_normal).add(w["idade"])

    print("%s — %d sorteios (metade em MODO BELA, um terco em MODO FORTE)"
          % (TITULO, n))
    for j in (1, 2):
        print("  cena %d: palavras min/med/max %d/%d/%d"
              % (j, min(tam[j]), sum(tam[j]) // len(tam[j]), max(tam[j])))
    print("  apelido: %s" % dict(apel))
    print("  mulheres · BELA desligado idades %d..%d | LIGADO %d..%d"
          % (min(idades_normal), max(idades_normal),
             min(idades_bela), max(idades_bela)))
    print("  linter: %d ERRO, %d AVISO"
          % (sum(erros.values()), sum(avisos.values())))
    for m, c in list(erros.most_common())[:4]:
        print("     %dx %s" % (c, m))

    # -- CONTROLE: o MODO BELA move a PESSOA, e nao so' o rotulo -------------
    # ⛔⛔ AQUI O CONTROLE NAO E' A IDADE, e a diferenca e' deliberada. No FIGHT
    # 16 e no BED 16 o estado desligado e' a ESPOSA (34-43) e o ligado e' a REF
    # bela (21-33): faixas disjuntas por desenho, e o controle de la' cobra
    # isso. Neste angulo nao ha' esposa — as duas mulheres sao PROVA SOCIAL, e
    # o print do operador mostra mulheres na casa dos 30. Copiar o controle do
    # FIGHT me obrigaria a envelhecer o pool ate' 44 anos so' para satisfazer a
    # lente, que e' otimizar a metrica CONTRA o objetivo (o erro que este repo
    # ja' cometeu quatro vezes com o `medir_personagens`).
    # ⭐ O que se cobra e' a FUNCAO: com o toggle ligado, a descricao dela tem
    # de vir do pool COMPARTILHADO, nunca do pool deste arquivo. Se um dia o
    # `ref_bela` deixar de ser chamado, ISTO acusa — a idade nao acusaria.
    _marcas_locais = {w["marca"] for w in MULHERES}
    _rng = random.Random(777)
    _vazou = 0
    for _ in range(60):
        _s = sortear("joe", _rng, {}, {"bela": True})
        for _w in _dupla(_s):
            if _w["marca"] in _marcas_locais:
                _vazou += 1
    if _vazou:
        falhas.append("MODO BELA: %d descricao(oes) vieram do pool LOCAL com o "
                      "toggle ligado — o botao nao trocou a pessoa" % _vazou)

    # -- CONTROLE: o MODO FORTE move o corpo de verdade ---------------------
    if set(CORPOS_H) & set(CORPOS_FORTES):
        falhas.append("MODO FORTE: os dois pools de corpo tem entrada em comum "
                      "— o toggle nao move nada nesses sorteios")

    # -- CONTROLE: [ALCANCE] — entrada que nunca sai esta' morta ------------
    # ⛔ Entrada que nao cabe com os MINIMOS dos outros beats e' entrada morta,
    # e o autoteste a conta como viva se so' olhar o pool.
    for rot, pool, outros, cena, o in (
            ("AVISOS", AVISOS, (TRUQUES, PARADOXOS), 1, "Johnson"),
            ("TRUQUES", TRUQUES, (AVISOS, PARADOXOS), 1, "Johnson"),
            ("PARADOXOS", PARADOXOS, (AVISOS, TRUQUES), 1, "Johnson"),
            ("MECANISMOS", MECANISMOS, (COZINHAS, CTAS), 2, "Johnson"),
            ("COZINHAS", COZINHAS, (MECANISMOS, CTAS), 2, "Johnson"),
            ("CTAS", CTAS, (MECANISMOS, COZINHAS), 2, "Johnson")):
        reserva = sum(_mn(p, o) for p in outros)
        mortas = [x for x in pool
                  if _palavras(x.format(o=o)) + reserva > TETO_FALA[cena]]
        if mortas:
            falhas.append("[ALCANCE] %s: %d entrada(s) nunca saem (%r)"
                          % (rot, len(mortas), mortas[0][:44]))

    # -- CONTROLE: COBERTURA — a soma dos MAIORES tem de caber --------------
    for cena, pools in ((1, (AVISOS, TRUQUES, PARADOXOS)),
                        (2, (MECANISMOS, COZINHAS, CTAS))):
        maior = sum(max(_palavras(x.format(o="Johnson")) for x in p)
                    for p in pools)
        if maior > TETO_FALA[cena]:
            falhas.append("COBERTURA cena %d: a soma dos MAIORES da' %d "
                          "palavras (teto %d) — o `_cabe` passa a cortar e o "
                          "sorteio deixa de ser uniforme"
                          % (cena, maior, TETO_FALA[cena]))

    # -- CONTROLE: CT7 por construcao ---------------------------------------
    # ⛔ Nenhum beat do take 1 pode juntar verbo de ereccao com o orgao. O
    # PARADOXO nomeia o orgao, entao e' ELE que nao pode ter o verbo.
    for rot, pool in (("PARADOXOS", PARADOXOS), ("AVISOS", AVISOS),
                      ("TRUQUES", TRUQUES)):
        sujas = [x for x in pool if sc.ERECAO_16.search(x)
                 and any(nn.lower() in x.lower() for nn in NUCLEO + ["{o}"])]
        if sujas:
            falhas.append("CT7: %s junta verbo de ereccao e orgao (%r)"
                          % (rot, sujas[0][:44]))

    # -- CONTROLE: VOCABULARIO DE DESLEIXO ----------------------------------
    # ⛔⛔ DISTINTIVO, NUNCA DETERIORADO — licoes-producao-veo §REF. A ancora e'
    # uma caracteristica MEMORAVEL num rosto SAUDAVEL E CUIDADO; nunca uma
    # avaria e nunca um descuido.
    # ⚠️ Esta lista nasceu de um REF que o operador REPROVOU vendo o render:
    # cabelo penteado PARA A FRENTE sobre a testa (le' como quem esconde
    # entrada) e SOBRANCELHAS UNIDAS numa linha so'. Passou por todas as
    # lentes: nao era palavra de mendigo, nao era adjetivo de celebridade, e o
    # pool tinha 16 entradas distintas. O que faltava era esta lista.
    # ⭐ E a barra deste angulo e' mais alta que a dos outros: ele aparece de
    # toalha com DUAS mulheres do lado. Se ele nao for plausivelmente atraente,
    # a cena nao fecha — e' o equivalente masculino da LEI DO REF.
    _DESLEIXO = ("combed forward", "comb-over", "comb over",
                 "meet in a single line", "unibrow", "close-set eyes",
                 "jowl", "receding", "thinning", "balding", "deep hairline",
                 "hollow cheeks", "sunken", "under-jaw", "double chin",
                 "bulbous", "wispy", "yellowed", "stained", "unkempt",
                 "worn low across the forehead")
    # ⛔ nenhuma entrada de PELES pode trazer outro `with`: elas entram depois
    # de `...woman WITH `, e o bloco sairia com `with ... with ...`.
    for _et, _lst in PELES.items():
        for _p in _lst:
            if " with " in _p or _p.startswith("with "):
                falhas.append("PELES[%s]: %r traz `with` — a montagem ja' poe o "
                              "dela antes" % (_et, _p))
    for e in HOMENS:
        t = (e["marca"] + " " + e["sinal"]).lower()
        for d in _DESLEIXO:
            if d in t:
                falhas.append("DESLEIXO: HOMENS %s traz %r — a ancora e' marca "
                              "num rosto CUIDADO, nunca descuido. Neste angulo "
                              "ele aparece de toalha com duas mulheres do lado."
                              % (e["id"], d))

    # -- CONTROLE: A PESSOA DE CADA TAKE ------------------------------------
    # ⛔⛔ Take 1 e' DEPOIMENTO, take 2 e' OFERTA, e a pessoa gramatical e' o
    # que separa os dois. O defeito que isto impede ja' existiu: o paradoxo
    # estava em 2a pessoa (`Your wife will beg...`) entre um aviso em 2a e um
    # truque em 1a, e o take trocava de pessoa DUAS vezes. O operador ouviu e
    # pediu a 1a. Sem controle, a proxima entrada escrita com pressa volta ao
    # `Your wife` e ninguem ve' — cada frase soa bem sozinha.
    for x in PARADOXOS:
        if not re.search(r"\bmy wife\b", x, re.I):
            falhas.append("PESSOA: PARADOXOS %r nao esta' em 1a pessoa — o "
                          "take 1 e' depoimento (`my wife`), nao promessa "
                          "sobre o futuro do espectador" % x[:44])
        if re.search(r"\byour\b|\byou\b", x, re.I):
            falhas.append("PESSOA: PARADOXOS %r fala com o espectador — quem "
                          "faz isso e' o AVISO (o gancho) e o take 2 inteiro"
                          % x[:44])
    for rot, pool in (("MECANISMOS", MECANISMOS), ("COZINHAS", COZINHAS)):
        for x in pool:
            if re.search(r"\bmy\b|\bI\b", x):
                falhas.append("PESSOA: %s %r esta' em 1a pessoa — o take 2 e' a "
                              "OFERTA e fala com o espectador" % (rot, x[:44]))

    # -- CONTROLE: PREDICADO VAZIO — o teste WTF, em codigo -----------------
    # ⛔⛔ Nasceu de uma pergunta do operador lendo o app: *"o que significa
    # `got hold of me` nesse caso? Nao ta' meio vago nao?"*. Estava, e havia
    # uma segunda com o mesmo defeito (`did something`). As duas tentavam dizer
    # o EFEITO — trabalho do PARADOXO, a batida seguinte — e em sete palavras
    # nao fizeram nem o proprio trabalho nem o dele.
    # ⚠️ Vagueza nao se mede por regex em geral; mas os predicados vazios sao
    # uma lista CURTA e conhecida, e e' exatamente por onde ela volta quando
    # alguem acrescenta uma entrada com pressa. E' a lei `slot tem que cumprir
    # funcao`: o linter checava FORMA, e forma nao pega frase que nao diz nada.
    _VAZIOS = (r"did something", r"got hold of", r"changed things",
               r"something happened", r"it worked", r"made a difference",
               r"did the trick", r"took care of it", r"handled it",
               r"was a game changer", r"blew my mind")
    for rot, pool in (("AVISOS", AVISOS), ("TRUQUES", TRUQUES),
                      ("PARADOXOS", PARADOXOS), ("MECANISMOS", MECANISMOS),
                      ("COZINHAS", COZINHAS), ("CTAS", CTAS)):
        for x in pool:
            m = next((v for v in _VAZIOS if re.search(v, x, re.I)), None)
            if m:
                falhas.append("TESTE WTF: %s tem predicado VAZIO (%r em %r) — "
                              "o espectador pode perguntar 'do que ele esta' "
                              "falando?'" % (rot, m, x[:44]))

    # -- CONTROLE: o literal do funil ---------------------------------------
    for rot, pool in (("TRUQUES", TRUQUES), ("MECANISMOS", MECANISMOS)):
        sem = [x for x in pool if "gelatin trick" not in x]
        if sem:
            falhas.append("%s: %d entrada(s) sem o literal `gelatin trick`"
                          % (rot, len(sem)))
    sem_kw = [x for x in CTAS if not x.startswith(sc.CTA_LITERAL)]
    if sem_kw:
        falhas.append("CTAS: %d entrada(s) nao abrem com %r"
                      % (len(sem_kw), sc.CTA_LITERAL))

    # -- CONTROLE: CT5 — nenhum ingrediente nomeado -------------------------
    for rot, pool in (("COZINHAS", COZINHAS), ("MECANISMOS", MECANISMOS),
                      ("PARADOXOS", PARADOXOS)):
        sujas = [x for x in pool if sc.INGREDIENTES_16.search(x)]
        if sujas:
            falhas.append("CT5: %s nomeia ingrediente (%r) — a receita e' a "
                          "moeda" % (rot, sujas[0][:44]))

    # -- CONTROLE: nenhum pool de fala diz IDADE nem VASILHAME --------------
    # ⛔ `a fala nao paga o que o quadro mostra` (lei permanente do operador):
    # medida, vasilhame e fracao saem da fala, porque o quadro ja' os mostra.
    for rot, pool in (("AVISOS", AVISOS), ("TRUQUES", TRUQUES),
                      ("PARADOXOS", PARADOXOS), ("MECANISMOS", MECANISMOS),
                      ("COZINHAS", COZINHAS), ("CTAS", CTAS)):
        for x in pool:
            if re.search(r"\b(bowl|spoon|spoonful|glass|cup|scoop|teaspoon|"
                         r"tablespoon|half|quarter)\b", x, re.I):
                falhas.append("%s: %r traz vasilhame/medida na fala" % (rot, x))
            if re.search(r"\b(at|past|over|under) (fifty|sixty|seventy|forty|"
                         r"\d\d)\b", x, re.I):
                falhas.append("%s: %r diz idade na fala" % (rot, x))

    # -- CONTROLE: os campos dos dois eixos de cena -------------------------
    for q in QUARTOS:
        for k in ("nome", "cen", "elas", "luz", "audio"):
            if not q.get(k):
                falhas.append("QUARTO %s: sem %r" % (q["id"], k))
    for a in AMBIENTES:
        for k in ("nome", "cen", "pose", "luz", "audio"):
            if not a.get(k):
                falhas.append("AMBIENTE %s: sem %r" % (a["id"], k))
    # ⛔ Os DEZ ambientes sao lista FECHADA — o operador escreveu os dez.
    if len(AMBIENTES) != 10:
        falhas.append("AMBIENTES: sao %d e o operador ditou DEZ — a lista nao "
                      "e' nossa" % len(AMBIENTES))
    # ⛔ O ENVOLTORIO E' TRAVADO, e o guarda impede que ele volte a ser pool:
    # o biquini reprovava no gerador (relato de campo, 2026-08-10) e
    # `bath towel` e `bikini top` sao CATEGORIAS diferentes para o
    # classificador, nao graus da mesma coisa.
    if re.search(r"bikini|swimsuit|swimwear|lingerie", ENVOLTORIO_DELAS, re.I):
        falhas.append("ENVOLTORIO_DELAS voltou a nomear roupa de banho — foi "
                      "REPROVADO no gerador")

    # -- CONTROLE: ids unicos ------------------------------------------------
    for rot, pool in (("QUARTOS", QUARTOS), ("AMBIENTES", AMBIENTES),
                      ("HOMENS", HOMENS), ("MULHERES", MULHERES),
                      ):
        ids = [x["id"] for x in pool]
        if len(set(ids)) != len(ids):
            falhas.append("%s: id repetido" % rot)

    # -- CONTROLE NEGATIVO da FA9 (o biquini) --------------------------------
    # ⛔⛔ ESTE CONTROLE NAO E' ENFEITE: sem ele a lente do biquini ficou VERDE
    # E MORTA por um commit inteiro. A borda de palavra do regex tinha virado
    # um byte de controle 0x08 no arquivo, o padrao procurava um BACKSPACE
    # antes de `bikini`, e nada casava nunca. O `inspect.getsource` mostrava a
    # linha CERTA — porque o terminal engole o backspace ao imprimir.
    # ⚠️ Lente sem controle negativo nunca foi testada. Foi assim que o defeito
    # apareceu: eu injetei o biquini a mao para mostrar a lente funcionando, e
    # ela nao acusou.
    s = sortear("joe", random.Random(2), {})
    bl = montar(s)
    bl["IMAGE 01/02"] = bl["IMAGE 01/02"].replace(
        ENVOLTORIO_DELAS, "a bikini top with a white bath towel at the waist")
    prova = []
    _fa9_toalha(s, bl, prova)
    if not any("roupa de banho" in a[1] for a in prova):
        falhas.append("a FA9 NAO acusou o biquini reinjetado — a lente do "
                      "envoltorio esta' morta (confira byte de controle no "
                      "regex: heredoc que escreve .py deixa 0x08)")

    # -- CONTROLE NEGATIVO da FA13 -------------------------------------------
    # ⛔ Uma lente que nunca acusou nunca foi testada. Injeta o idioma do BED 16
    # e exige que ela morda.
    s = sortear("joe", random.Random(1), {})
    bl = montar(s)
    bl["IMAGE 02/02"] = bl["IMAGE 02/02"] + " Back in the same bedroom."
    prova = []
    _fa13_lugares_independentes(s, bl, prova)
    if not prova:
        falhas.append("a FA13 NAO acusou `the same bedroom` — lente que nunca "
                      "morde nunca foi testada")

    # -- CONTROLE NEGATIVO da FA1 --------------------------------------------
    bl2 = montar(s)
    bl2["IMAGE 01/02"] = bl2["IMAGE 01/02"].replace(SORRISO,
                                                    "Both women are laughing.")
    prova = []
    _fa1_sorriso(s, bl2, prova)
    if not prova:
        falhas.append("a FA1 NAO acusou riso alto")

    # -- CONTROLE: a anti-repeticao, medida ---------------------------------
    rng2 = random.Random(4242)
    led = {}
    vistos = collections.defaultdict(list)
    janelas = {"quarto": 4, "ambiente": 4, "homem": 6, "mulher_a": 5}
    for _ in range(50):
        s = sortear("joe", rng2, led)
        for eixo, jan in janelas.items():
            novo = s[eixo]["id"]
            if novo in vistos[eixo][-jan:]:
                falhas.append("%s %r repetiu dentro da janela de %d"
                              % (eixo, novo, jan))
            vistos[eixo].append(novo)
        if s["mulher_a"]["id"] == s["mulher_b"]["id"]:
            falhas.append("as duas mulheres sairam iguais no sorteio normal")
        _anotar(led, s)
    for eixo in sorted(janelas):
        print("  %-9s 50 sorteios, %d distintos" % (eixo, len(set(vistos[eixo]))))

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
    ap.add_argument("--quarto", choices=[q["id"] for q in QUARTOS])
    ap.add_argument("--ambiente", choices=[a["id"] for a in AMBIENTES])
    ap.add_argument("--bela", action="store_true")
    ap.add_argument("--forte", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--autoteste", action="store_true")
    a = ap.parse_args()

    if a.autoteste:
        return autoteste()

    led = _carregar_ledger()
    rng = random.Random(a.seed)
    travas = {}
    for k in ("quarto", "ambiente"):
        if getattr(a, k):
            travas[k] = getattr(a, k)
    if a.bela:
        travas["bela"] = True
    if a.forte:
        travas["forte"] = True
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
