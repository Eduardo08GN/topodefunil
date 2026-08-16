# -*- coding: utf-8 -*-
"""VICK 16 — a pomada azul, e o mecanismo que a fala nunca diz.

    python funil-organico/vick16_short.py --autoteste
    python funil-organico/vick16_short.py --pagina joe

===============================================================================
 A FONTE
===============================================================================
15 reels em `C:\\Users\\edlut\\Music\\OKC-Likes-Viewer-master\\vick`, 300s no
total, lidos a **2 quadros por segundo** (566 quadros, um a um) e transcritos
com `faster-whisper small.en`. O mapa completo esta' em
[`concorrentes/vick-mapa-visual.md`](../concorrentes/vick-mapa-visual.md) — 101 KB
de leitura otica, e nenhuma linha dele e' suposicao.

⭐⭐ O MECANISMO, E ELE SO' EXISTE NA IMAGEM. O homem abre um pote de VapoRub,
rasga um sache de gelatina Knox, despeja o po DENTRO do pote, mistura com o
dedo, as vezes acrescenta mel — e a mistura EFERVESCE ate' virar espuma que
sobe na borda. A FALA NUNCA NOMEIA NADA DISSO: ela diz `toxic buildup`,
`flushes the plaque`, `melts the invisible blockage`.
⛔ Essa assimetria E' O ANGULO: a imagem entrega a receita, a fala cobra o
comentario por ela. Quem "consertar" isso nomeando o Vicks na fala destroi o
motivo de alguem comentar.

⛔⛔ E' A MESMA FONTE DOS TRES `banho`. O v03 traz *"falling like a lame horse
in the middle of a rodeo"* verbatim, frase ja' registrada no `banho16_v2`; o
CTA e' `Comment recipe`, o mesmo do `banho16`. O que separa este motor dos
irmaos e' **o VICKS**, presente em 13 dos 15 e ausente do parque inteiro.
⭐ Por isso o `vick16` CONVIVE com os tres, como o `mel16` convive com o
`prato16`: dois irmaos existem para isolar UMA variavel, e aqui ela e' a pomada.
⛔ E a frase do rodeio NAO entra aqui, de proposito — ela fica exclusiva do
`banho16_v2`. Repetir a mesma frase em dois motores faz o lote soar como um.

===============================================================================
 AS DECISOES DO OPERADOR (2026-08-15)
===============================================================================
1. **A pessoa e' EIXO SORTEAVEL** — o motor decide entre so' as maos, mao e
   antebraco, tronco, ou corpo inteiro. A fonte faz os quatro.
2. **O Vicks e' MECANISMO**, nao prop.
3. **2 takes de 8s** (AdBatch Vertical 2).
4. **O pool de nomes do ritual cresce**: os 5 lidos mais gelatin/rub x
   hack/trick/habit/ritual.
5. **O CT1 e' APLICADO** — o follow vem ANTES do CTA. ⚠️ A fonte faz o
   CONTRARIO nos 15 (`Follow me so I can reach you` no fim); esta e' uma
   divergencia deliberada da fonte, por ordem dele, nao um descuido.
6. **O v11 virou um SEGUNDO EIXO DE HOOK** — a familia HISTORIA (perda concreta
   na relacao + um terceiro que contou o segredo + dias + resultado) contra a
   familia MECANISMO (idade ou condicao + o nome do ritual). As duas nunca se
   misturam no mesmo video.

⛔ EXCECAO AO CT4b, DECLARADA: os apelidos do orgao sao os DA FONTE —
`baseball bat`, `small bat`, `shrinking bat`, `shrinking baton`, `buddy`,
`pipes` — e nao os `pecker`/`wiener`/`Johnson` do contrato. Precedente: o
`banho16` ja' desligou o CT4b por ordem do operador.

===============================================================================
 ⛔⛔ A CENA E' A UNIDADE ATOMICA — e isso resolve um defeito antes dele nascer
===============================================================================
O operador pediu pool de ambientes >= 100 E um pool de cenas com variancia
absurda. Os dois separados cruzariam `prateleira de canto do box` com
`espreguicadeira de praia` — e' o defeito que o commit dfb5d88 documenta (*"o
painel nao respeitava o acoplamento entre eixos"*) e a licao GO21 do GOOD 16.

Por isso **ambiente + superficie + camera + enquadramento + luz + audio viajam
JUNTOS** num objeto so: um deles falso derruba os outros cinco. O pool de CENAS
**e'** o pool de ambientes. A ACAO fica em eixo proprio e declara em que
familia cabe (`cabe_em`), e a cena declara se comporta regua (`regua_cabe`) —
regua de madeira numa sauna de madeira some no fundo, e isso so' apareceria no
render.

MEDIDO no pool: **100 superficies distintas em 100 entradas**, 12 familias,
61 cenas que comportam regua contra 39 que nao, 40 molhadas contra 60 secas.

===============================================================================
 ⚠️ LIDO x CONSTRUIDO — a divida declarada deste motor
===============================================================================
A fonte tem 15 videos; o operador pediu 100+ por pool. Logo a maioria e'
EXTRAPOLACAO, e isso contraria a regra do HORSE 16 (*"entrada nova sai de
leitura de video, nunca de invencao"*). A regra nao foi ignorada — foi
TORNADA VISIVEL: **cada entrada carrega `fonte`**, e o autoteste conta os dois
grupos. Assim o campo sabe a que atribuir resultado.

    cenas   22 lidos · 78 construidos
    acoes   47 lidos · 53 construidos
    homens  18 lidos · 82 construidos
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

APP = "AGENTE VICK 16"
# O painel compartilhado le' estes por nome. Sem `TITULO` o `ui_agente`
# estoura no construtor, e o .exe sobe com "Unhandled exception in script" —
# que foi exatamente o que o smoke test do executavel pegou.
TITULO = "AGENTE VICK 16"
SUBTITULO = ("2 takes de 8s = 16 segundos · a pomada azul · ele mistura o po no pote e a espuma sobe; a fala NUNCA nomeia o ingrediente")
SEXOS = ("homem",)

# A ETNIA por pagina — a congruencia inviolavel do funil: a etnia do REF casa
# com a do avatar da pagina. Copiada do parque, nao reinventada aqui: uma
# segunda tabela divergiria da primeira no dia em que uma pagina mudasse.
ETNIA = {'roy': 'white American', 'dean': 'white American', 'earl': 'white American', 'jason': 'Black American', 'philippe': 'Black American', 'joe': 'white American', 'ray': 'white American', 'matt': 'white American', 'marcus': 'Black American', 'chuck': 'Black American'}

# Os rotulos das duas caixas de copy no painel.
CENAS_UI = ["1 · O HOOK", "2 · O MECANISMO + CTA"]
SLUG = "vick-16"
LEDGER = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      ".vick-16-ledger.json")

# ⭐ A palavra do CTA e' campo no painel desde 2026-08-15; `KEYWORD_NATIVA` e' a
# que os pools ja' trazem escrita — a ancora da substituicao, nao um gosto.
KEYWORD_UI = True
KEYWORD_NATIVA = "recipe"

# ⛔ 2 takes de 8s. O teto de 25 palavras e' o mesmo da familia 16s.
TETO_FALA = {1: 25, 2: 25}
PISO_FALA = {1: 10, 2: 11}

CAUDA = ("Shot on an iPhone held in one hand, slight natural sway, soft sensor "
         "grain. No on-screen text, no subtitles, no captions, no watermark.")

# ⛔ EXCECAO AO CT4b DECLARADA — sao os apelidos DA FONTE, medidos nos 15.
# `buddy` SAIU do NUCLEO: na familia HISTORIA ele e' o AMIGO que contou o
# segredo ("then a buddy told me"), nao o orgao. Duas leituras para a mesma
# palavra faziam o normalizador do CT4 trocar o amigo por `shrinking bat`.
NUCLEO = ("baseball bat", "small bat", "shrinking bat", "shrinking baton",
          "pipes")

BANIDOS_CTA = {
    "book": "quebra a automacao de DM",
    "yes": "quebra a automacao de DM",
}

# ⛔ As tabelas que o `lint_curto` compartilhado le' por nome. Vazias aqui NAO
# significa "sem guarda": as recusas deste angulo sao geometricas (o gesto no
# orgao) e nao lexicais, e quem as cobra e' a lente VI7. Declarar as tabelas
# vazias e' o contrato — sem elas o `lint_curto` estoura em AttributeError, e
# um motor que nao roda o linter e' pior que um motor sem linter.
BANIDOS_IMAGE = {}
BANIDOS_TAKE = {}
BANIDOS_BLOCO = {}

# ⭐⭐ AS CENAS — a unidade atomica. 100 entradas, 100 superficies
# DISTINTAS (medido). Cada uma leva ambiente + superficie + camera +
# enquadramento + luz + audio, porque um deles falso derruba os outros.
CENAS = [{'id': 'borda_branca_banheira_enchendo',
  'curto': 'Borda branca da banheira enchendo',
  'fonte': 'lido',
  'familia': 'banheira',
  'ambiente': 'Small old lower-middle-class bathroom. White alcove tub '
              'filling: chrome spout pouring a continuous stream, murky '
              'olive-green water with white foam floating. White square '
              'tile, dark stained grout, chrome overflow plate, with the jar '
              'visible in frame.',
  'superficie': 'The flat white tub ledge — the horizontal capping strip on '
                'top of the tub surround, between the tub rim and the tiled '
                'wall. Every object rests directly on that white band, which '
                'runs diagonally across the frame; a yellowed caulk line '
                'shows where it meets the tile.',
  'camera': 'POV of a man standing over the tub, phone in one hand, looking '
            'down at forty to fifty degrees. Handheld with constant drift '
            'and micro-tremor, descending slowly toward the mouth of the '
            'jar.',
  'enquadramento': 'Vertical 9:16, medium-wide. In: the chrome spout with '
                   'its running stream, the green water, the whole white '
                   'ledge on a diagonal, the cardboard sign leaning on the '
                   'tile, the floor and toilet base in the corner. Cropped: '
                   'ceiling, any person.',
  'luz': 'Cold flat ceiling light, no window, hard sheen on wet white '
         'enamel.',
  'audio': 'Continuous tap water hitting the filling tub, faint echo of a '
           'small tiled room, cardboard flap tearing.',
  'aceita': ['po', 'pote', 'sache', 'creme', 'espuma'],
  'regua_cabe': True,
  'molhado': True},
 {'id': 'bancada_pia_branca_camera_travada',
  'curto': 'Bancada branca da pia, camera travada',
  'fonte': 'lido',
  'familia': 'pia',
  'ambiente': 'Clean bright middle-class bathroom with daylight from a '
              'window, frameless mirror reflecting a grey-and-white striped '
              'shower curtain, white tile and a white-sash window, cream '
              'wall, dark wood cabinet below, with the glass visible in '
              'frame.',
  'superficie': 'The one-piece white cultured-marble sink countertop with an '
                'integral oval basin; the props stand on the flat wing to '
                'the LEFT of the basin, and the sticky note lies flat on the '
                'deck in front of the bowl. Nothing is inside the basin.',
  'camera': 'Locked-off tripod shot at chest height, angled twenty-five to '
            'thirty degrees down onto the vanity. Zero drift, zero zoom: the '
            'frame never changes, only the hands enter and leave it.',
  'enquadramento': 'Vertical 9:16, one immutable medium shot. Glass in the '
                   'left third, basin and faucet in the right third, note at '
                   'the base, mirror in the top third. Hands enter from the '
                   'upper right. Cropped: floor, any face.',
  'luz': 'Soft cool daylight from the window, even and shadowless, bright '
         'bounce off the white countertop.',
  'audio': 'Quiet closed-bathroom room tone, a spoon clinking on glass, '
           'faint street hum through the window.',
  'aceita': ['po', 'cubos', 'pote', 'sache', 'creme', 'liquido'],
  'regua_cabe': True,
  'molhado': False},
 {'id': 'deck_ceramica_bege_banheira',
  'curto': 'Deck de ceramica bege da banheira',
  'fonte': 'lido',
  'familia': 'banheira',
  'ambiente': 'Large built-in tub filled with pale mint-green water, chrome '
              'spout and chrome overflow plate, wide beige-tan ceramic '
              'surround with visible grout, steam rising near the end, warm '
              'beige walls.',
  'superficie': 'The wide beige-tan twelve-inch ceramic tub deck — the broad '
                'tiled shelf capping the built-in tub, grout lines crossing '
                'it. Box, jar, loose lid and measuring tape lie side by side '
                'on that warm tile with room to spare.',
  'camera': 'Handheld high three-quarter angle looking down onto the tub '
            'deck, then descending and closing in steps to a near-plumb '
            'macro over the mouth of the jar. Breathing and micro-tremor '
            'throughout.',
  'enquadramento': 'Vertical 9:16. Opens wide on the deck: spout, mint '
                   'water, box, jar, lid and the whole measuring tape from '
                   'two to fourteen inches. Then a detail of both hands. '
                   'Cropped: ceiling, floor, any face.',
  'luz': 'Warm domestic bathroom light, soft and diffuse, mild specular on '
         'the mint water.',
  'audio': 'Still bath water lapping faintly, cardboard flap tearing, a '
           'spoon tapping the rim of the jar.',
  'aceita': ['po', 'cubos', 'pote', 'sache', 'creme', 'espuma', 'liquido'],
  'regua_cabe': True,
  'molhado': True},
 {'id': 'caddy_inox_escovado_na_haste',
  'curto': 'Caddy de inox escovado na haste',
  'fonte': 'lido',
  'familia': 'chuveiro',
  'ambiente': 'Closed shower enclosure, two beige-cream large-format tiled '
              'walls meeting at a corner, dark gunmetal shower head running '
              'continuously, a fan of water crossing in front of the '
              'products, light steam and runnels on the tile, with the pan '
              'visible in frame.',
  'superficie': 'A brushed stainless corner caddy clamped to the dark '
                'vertical riser pole in the middle of frame; fan-shaped '
                'drain grooves scored into its top, rounded lip, beaded with '
                'fat drops and dripping filaments off its front edge. All '
                'three products stand on that one tray.',
  'camera': 'POV of a man standing inside the enclosure, phone at chest and '
            'shoulder height, tilted slightly down at the corner caddy with '
            'the shower head at the top of frame. Near-static, minimal '
            'handheld drift.',
  'enquadramento': 'Vertical 9:16, medium-tight. In: the shower rose at the '
                   'top, the tiled corner at the sides, the caddy and its '
                   'products in the lower third. Cropped: ceiling, floor '
                   'pan, the enclosure as a whole, any person.',
  'luz': 'Cool diffuse bathroom light, no hard shadow, wet highlights along '
         'the stainless lip.',
  'audio': 'Shower running steady on tile, water pattering on the caddy and '
           'on the floor pan, cardboard tearing.',
  'aceita': ['po', 'pote', 'sache', 'creme', 'espuma'],
  'regua_cabe': True,
  'molhado': True},
 {'id': 'banquinho_madeira_ao_lado_banheira',
  'curto': 'Banquinho de madeira ao lado da banheira',
  'fonte': 'lido',
  'familia': 'banheira',
  'ambiente': 'Domestic bathroom, white alcove tub half full of still pale '
              'blue-green water, chrome tub spout, chrome lever mixer high '
              'on the wall, coiled hand-shower hose hanging, smooth white '
              'drywall, dark laminate floor behind, with the jar visible in '
              'frame.',
  'superficie': 'A low solid-wood stool with visible legs and a stretcher, '
                'pushed against the outer skirt of the tub; every prop '
                'stands on its dry pale wooden seat, which fills the lower '
                'right third of frame. The high white tub rim works as a '
                'second ledge and splits the frame.',
  'camera': 'POV of a man standing beside the tub, phone in hand at waist '
            'and hip height, looking down about forty-five degrees; diagonal '
            'composition, closing in progressively to a near-vertical macro '
            'over the jar.',
  'enquadramento': 'Vertical 9:16. Wide: the wall mixer, the hose, the '
                   'spout, the tub rim and its water, the whole cardboard '
                   'sign, the stool with its props. Cropped: ceiling, most '
                   'of the floor, any person.',
  'luz': 'Soft domestic daylight, no steam, gentle shadows under the legs of '
         'the stool.',
  'audio': 'Still bath water shifting, small room echo, a plastic sachet '
           'tearing.',
  'aceita': ['po', 'cubos', 'pote', 'sache', 'creme', 'espuma', 'liquido'],
  'regua_cabe': True,
  'molhado': False},
 {'id': 'piso_nicho_madeira_demolicao',
  'curto': 'Piso do nicho na parede de demolicao',
  'fonte': 'lido',
  'familia': 'nicho',
  'ambiente': 'Shower stall walled in grey reclaimed barn wood, horizontal '
              'weathered boards with heavy knots and grain, a square '
              'white-cream niche cut into it, a dark rain head pouring a '
              'straight curtain of water.',
  'superficie': 'The floor of the built-in square niche — a smooth '
                'white-cream plaster shelf recessed into the wood wall, the '
                "niche's own side walls framing the still life. The products "
                'stand in a row on that recessed floor, inside the opening.',
  'camera': 'Frontal and almost perpendicular to the wall, chest height, the '
            'niche centred and symmetrical in frame like a vitrine. Static, '
            'minimal drift, then closing to a medium over the hands.',
  'enquadramento': 'Vertical 9:16. The niche holds the centre third, rustic '
                   'wood above, below and at both sides. In: the cropped '
                   'rain head, the sheet of falling water, the whole niche '
                   'with its objects. Cropped: ceiling, floor, any body.',
  'luz': 'Cool even shower light, high contrast between the grey wood and '
         'the white niche, wet sheen on the boards.',
  'audio': 'Rain head drumming on the shower floor, water hissing past the '
           'mouth of the niche, damp tiled reverb.',
  'aceita': ['po', 'pote', 'sache', 'creme', 'espuma'],
  'regua_cabe': True,
  'molhado': True},
 {'id': 'caddy_arame_cromado_dois_niveis',
  'curto': 'Caddy de arame cromado de dois niveis',
  'fonte': 'lido',
  'familia': 'chuveiro',
  'ambiente': 'Small closed shower stall, large square beige-cream tile with '
              'dark grey grout, shower running continuously with a diagonal '
              'jet falling behind the objects, droplets on the lens, a '
              'chrome grab bar on the tile.',
  'superficie': 'A two-tier chrome wire caddy hung on the shower pipe and '
                'wedged into the corner at chest height; every object sits '
                'on the open grid of the UPPER basket, the gaps between the '
                'wires and the water dripping through them plainly visible. '
                'The lower basket stays empty.',
  'camera': 'POV with the phone at chest height, aimed slightly down into '
            'the corner of the stall; handheld with micro-tremor and abrupt '
            'reframes, dropping in three steps until it sits almost level '
            'with the caddy in a slight low angle.',
  'enquadramento': 'Vertical 9:16. Shower rose in the top third, caddy and '
                   'products in the lower third, ruler tight against the '
                   'right edge. Cropped: ceiling, floor pan, the room as a '
                   'whole, any person.',
  'luz': 'Warm flat bathroom light, no hard shadow, wet gleam along the '
         'chrome wire.',
  'audio': 'Shower hissing on tile the entire time, droplets ticking through '
           'the wire basket, cardboard tearing.',
  'aceita': ['po', 'pote', 'sache', 'creme', 'espuma'],
  'regua_cabe': True,
  'molhado': True},
 {'id': 'tabua_acougueiro_cozinha_rustica',
  'curto': 'Tabua de acougueiro da cozinha rustica',
  'fonte': 'lido',
  'familia': 'cozinha',
  'ambiente': 'Rustic rural American kitchen, hard morning sun through a '
              'wooden window in the upper right striping the counter, dark '
              'green slate-look tile backsplash, white outlet with a black '
              'cord hanging, honey-toned wood sill, with the bowl and glass '
              'visible in frame.',
  'superficie': 'A pale butcher-block counter with visible vertical glue '
                'joints, knife scars and dark oil and water stains; every '
                'object rests directly on the wood and the front edge of the '
                'slab closes the bottom of frame. The wooden window sill '
                'behind holds the note.',
  'camera': 'Over-the-shoulder POV of someone cooking: about forty-five '
            'degrees down, phone above and behind the hands, pointed at the '
            'bowl on the counter, at the eye height of a man standing at the '
            'block. Light drift, no strong tremor.',
  'enquadramento': 'Vertical 9:16, medium-tight on the counter: window in '
                   'the upper right, note, mug in the upper left, '
                   'paper-towel roll on the right, bowl centred in the '
                   'middle third, hands in the lower third. Cropped: face, '
                   'torso, floor.',
  'luz': 'Hard golden morning sunlight from the side, warm, with a defined '
         'diagonal shadow across the wood.',
  'audio': 'Quiet country kitchen tone, birds far outside the window, a '
           'spoon ringing on glass, a sachet tearing.',
  'aceita': ['po', 'cubos', 'pote', 'sache', 'creme', 'liquido', 'espuma'],
  'regua_cabe': True,
  'molhado': False},
 {'id': 'deck_marmore_banheira_led_azul',
  'curto': 'Deck de marmore da banheira com LED azul',
  'fonte': 'lido',
  'familia': 'banheira',
  'ambiente': 'Upper-middle-class bathroom in veined white marble, wall and '
              'deck both stone, a lit blue LED strip along the tub edge and '
              'wall, chrome towel bar with a striped towel, white '
              'wall-mounted soap dish, with the jar visible in frame.',
  'superficie': 'The veined white marble tub deck — a high, pale polished '
                'stone ledge capping the built-in tub, marble tile behind '
                'it, the lit blue LED line running along its outer edge. '
                'Every prop stands on that cold stone; nothing touches wood.',
  'camera': 'Handheld high-angle POV over the tub deck, phone held above the '
            "man's own working hands, then a second setup low and frontal "
            'almost level with the mouth of the jar. Hard cut between the '
            'two, near-static in each.',
  'enquadramento': 'Vertical 9:16. Tight on both hands, spoon and jar with '
                   'the tub and the handwritten card thrown out of focus '
                   'behind; the last framing is a close-up of the jar with '
                   'the blue LED streaking the background. Cropped: face, '
                   'floor, ceiling.',
  'luz': 'Warm ceiling light against the cold blue LED line, glossy '
         'reflections on polished marble.',
  'audio': 'Quiet high-end bathroom room tone, a thick drizzle of honey off '
           'a spoon, a distant extractor fan.',
  'aceita': ['po', 'cubos', 'pote', 'sache', 'creme', 'espuma', 'liquido'],
  'regua_cabe': True,
  'molhado': False},
 {'id': 'parapeito_azulejado_banheira_habitada',
  'curto': 'Parapeito azulejado da banheira habitada',
  'fonte': 'lido',
  'familia': 'banheira',
  'ambiente': 'Old lived-in American bathroom: checkerboard beige tile to '
              'mid-height, cream paint above, hammered obscure-glass window '
              'on the right with late-afternoon orange haze, stained sink '
              'counter, alcove tub with turquoise water.',
  'superficie': 'The tiled tub ledge — a checkerboard beige tile capping '
                'strip about three tiles wide on top of the tub surround, '
                'its grout darkened with age; the props stand on that tile '
                'with the tub and its turquoise water below to the right.',
  'camera': 'Camera high and tilted down about forty-five degrees, POV of a '
            'man standing at the tub watching his own hands work; both hands '
            'enter from the sides and are cut at the forearm.',
  'enquadramento': 'Vertical 9:16, medium-tight on the ledge. In: both '
                   'hands, jar, sachet, spoon, the white tape running along '
                   'the ledge and turning the corner, the tub water in the '
                   'lower right. Cropped: ceiling, face, the far wall.',
  'luz': 'Warm late-afternoon daylight diffused through obscure glass, '
         'orange halo, soft shadows.',
  'audio': 'Faint water settling in the tub, an old extractor rattling, a '
           'paper sachet tearing.',
  'aceita': ['po', 'cubos', 'pote', 'sache', 'creme', 'espuma'],
  'regua_cabe': False,
  'molhado': True},
 {'id': 'prateleira_canto_madeira_macica',
  'curto': 'Prateleira de canto de madeira macica',
  'fonte': 'lido',
  'familia': 'chuveiro',
  'ambiente': 'Closed shower stall, large square beige off-white tile with '
              'pale grout, two walls meeting at a corner, a dark grey '
              'ceiling rain head running from the first frame to the last, '
              'no window.',
  'superficie': 'A thick solid-wood corner shelf — roughly four centimetres '
                'of honey-oak varnished board wedged into the corner of the '
                'stall, soaked through, water sheeting across its face and '
                'dripping off its front edge. It is the only surface in the '
                'scene.',
  'camera': 'POV of the operator standing inside the stall, phone at chest '
            'height looking down into the corner. The position never moves '
            'but the distance does: it alternates between a wide of the '
            'whole shelf and a macro glued to the hands.',
  'enquadramento': 'Vertical 9:16. Wide: rain head at the top, corner shelf '
                   'in the middle, stall base below, all three objects '
                   'whole. Tight: hands and jar fill half the frame, box and '
                   "ruler soft behind. Cropped: the man's head, always above "
                   'the top edge.',
  'luz': 'Flat cool bathroom light, no window, even across the wet tile.',
  'audio': 'Rain head running continuously, water drumming on the stall '
           'floor, drips ticking off the wooden edge.',
  'aceita': ['po', 'pote', 'sache', 'creme', 'espuma'],
  'regua_cabe': True,
  'molhado': True},
 {'id': 'tampa_do_vaso_sanitario',
  'curto': 'Tampa fechada do vaso sanitario',
  'fonte': 'lido',
  'familia': 'vaso',
  'ambiente': 'Clean modern middle-class bathroom: large-format beige tile '
              'with a trim band high on the wall, white two-piece toilet '
              'centred, white tub on the right with chrome valve and '
              'diverter, beige ceramic floor, with the bottle and glass '
              'visible in frame.',
  'superficie': 'The closed toilet lid — a lowered white seat cover used as '
                'a work bench; every object stands on that oval moulded '
                'surface, and the tank behind acts as the back wall where '
                'the yellow note is stuck.',
  'camera': 'Gentle high angle, standing in front of the toilet, phone at '
            'chest height looking down thirty to forty degrees. Essentially '
            'locked at first, then two tighter framings, the last with a '
            'sachet held right against the lens.',
  'enquadramento': 'Vertical 9:16. Tank and note in the top third, lid with '
                   'its objects in the middle, the front of the seat closing '
                   'the bottom third, the tub filling the right band. '
                   'Cropped: ceiling, floor, any person.',
  'luz': 'Flat slightly warm bathroom light, no hard shadow, the brightest '
         'frame of the batch from all the white ceramic.',
  'audio': 'Dry closed-bathroom room tone, a spoon clinking against a glass, '
           'a plastic cap popping off a bottle.',
  'aceita': ['cubos', 'pote', 'sache', 'liquido'],
  'regua_cabe': False,
  'molhado': False},
 {'id': 'tampo_direita_da_cuba_pastilha',
  'curto': 'Tampo a direita da cuba, pastilha de vidro',
  'fonte': 'lido',
  'familia': 'pia',
  'ambiente': 'Home bathroom vanity: white basin dropped into a one-piece '
              'cultured-marble top, cheap two-handle chrome faucet, a strip '
              'of beige-brown-sage glass mosaic on the wall behind, pale oak '
              'cabinet doors below.',
  'superficie': 'The dry white countertop to the RIGHT of the drop-in basin '
                '— flat, glossy cultured stone with the ceiling fixture '
                'mirrored in it; the glass bowl sits on that dry top beside '
                'the basin, never inside it. No board, no cloth under it.',
  'camera': 'POV of a man standing at the sink with the phone in one hand, '
            'steep top-down angle of forty-five to sixty degrees at chest '
            'and shoulder height, handheld with light drift, zooming in '
            'progressively from wide to macro with no visible cut.',
  'enquadramento': 'Vertical 9:16. Opening: faucet upper left, basin left, '
                   'bowl centre, box lower left, ruler right, cabinet cut at '
                   'the base. Then the bowl grows until only the hand and '
                   'its payoff remain. Cropped: face, torso, ceiling.',
  'luz': 'Warm vanity light from above, a soft specular pool on the glossy '
         'white top, no daylight.',
  'audio': 'Dry bathroom room tone, a knife tapping the counter, a spoon '
           'stirring inside a glass bowl.',
  'aceita': ['po', 'cubos', 'pote', 'sache', 'creme', 'liquido', 'espuma'],
  'regua_cabe': True,
  'molhado': False},
 {'id': 'prateleira_canto_granito_bege',
  'curto': 'Prateleira de canto de granito bege',
  'fonte': 'lido',
  'familia': 'chuveiro',
  'ambiente': 'Inside a running shower, water curtains and spray crossing '
              'the frame constantly, large beige-cream tile with faintly '
              'marbled texture and visible grout on two walls, no window, '
              'warm humid air, with the jar and pan visible in frame.',
  'superficie': 'A built-in quarter-round corner shelf of mottled beige '
                'granite, cantilevered into the tiled corner; water sheets '
                'over it and drips off the front lip in five or six visible '
                'filaments. Every prop stands on that soaked speckled stone.',
  'camera': 'Eye level or slightly below, aimed straight at the corner of '
            'the stall — not a high angle. Handheld with micro-drift, '
            'zooming in progressively from the whole shelf to a macro on the '
            'mouth of the jar.',
  'enquadramento': 'Vertical 9:16. The shelf holds the lower third; the '
                   'upper two thirds are plain tile and falling water, '
                   'deliberately kept empty of objects. The ruler climbs the '
                   'right edge. Cropped: ceiling, floor, any body.',
  'luz': 'Warm bathroom light through steam, soft, wet highlights on the '
         'granite and on the jar.',
  'audio': 'Shower running the entire time, water breaking over the stone '
           'lip, filaments dripping onto the pan below.',
  'aceita': ['po', 'pote', 'sache', 'creme', 'espuma'],
  'regua_cabe': True,
  'molhado': True},
 {'id': 'degrau_acrilico_cabeceira_banheira',
  'curto': 'Degrau de acrilico na cabeceira da banheira',
  'fonte': 'lido',
  'familia': 'banheira',
  'ambiente': 'Bathroom at night: white built-in tub with a lit blue LED '
              'strip along its skirt, grey porcelain floor, a blue bath mat, '
              'a door on the right, a shampoo bottle on the far tub rim.',
  'superficie': 'The flat white acrylic step at the head of the built-in tub '
                '— the dry moulded deck where the tub meets the wall; box, '
                'jar, loose turquoise lid and ruler stand right in the '
                'corner where that deck meets the rounded rim of the bath.',
  'camera': 'Top-down POV at fifty to sixty degrees, phone in one hand '
            'looking onto the tub deck, then pushing into macro and almost '
            'straight down at the end. Light handheld float.',
  'enquadramento': 'Vertical 9:16. Starts medium-wide with the tub, the LED '
                   'line and the whole deck of props plus the full ruler, '
                   'and ends in extreme macro on the mouth of the jar with '
                   'the blue LED soft behind. Cropped: face, ceiling.',
  'luz': 'Cool night bathroom light with the electric blue LED as the '
         'signature, cold whites, no daylight.',
  'audio': 'Empty bathroom room tone, a paper sachet tearing, a spoon '
           'knocking the rim of the jar, a far-off pipe hum.',
  'aceita': ['po', 'cubos', 'pote', 'sache', 'creme', 'espuma'],
  'regua_cabe': True,
  'molhado': False},
 {'id': 'vidro_fume_canto_box_frameless',
  'curto': 'Prateleira de vidro fume, box frameless',
  'fonte': 'construido',
  'familia': 'chuveiro',
  'ambiente': 'Frameless glass shower enclosure with white large-format '
              'porcelain walls, a chrome thermostatic bar valve and hand '
              'shower running, water beading and sliding down the clear '
              'glass panel, with the tray visible in frame.',
  'superficie': 'A smoked tempered-glass corner shelf, eight millimetres '
                'thick, held by two polished chrome brackets in the tiled '
                'corner; the props stand on the dark translucent glass and '
                'their bases read through it from below, water pooling '
                'around each one.',
  'camera': 'Phone held low, almost level with the shelf itself, tilted very '
            'slightly up so the underside of the glass reads; handheld, '
            'small drift, one slow push-in.',
  'enquadramento': 'Vertical 9:16. In: the corner joint, the shelf nearly '
                   'edge-on with the objects on it, the wet glass panel at '
                   'the left, the bar valve cut at the top. Cropped: shower '
                   'head, floor, any face.',
  'luz': 'Cool white LED downlight, hard specular streaks on the wet glass, '
         'sharp edge highlights along the shelf.',
  'audio': 'Hand shower hissing off-frame, water running down the glass '
           'panel, drips landing on the shower tray.',
  'aceita': ['pote', 'sache', 'creme', 'espuma'],
  'regua_cabe': True,
  'molhado': True},
 {'id': 'mureta_ardosia_wetroom',
  'curto': 'Cap de ardosia da meia-parede do wet room',
  'fonte': 'construido',
  'familia': 'chuveiro',
  'ambiente': 'Open walk-in wet room with no door: micro-cement floor '
              'sloping to a linear drain, matte charcoal wall tile, a '
              'ceiling rain head running steadily, steam gathering at the '
              'top of frame.',
  'superficie': 'The honed black slate cap of the half-height pony wall that '
                'divides the wet room — a flat twenty-centimetre stone '
                'coping, matte and streaked with running water; every object '
                'stands on that dark stone band.',
  'camera': 'Chest height, straight on and perpendicular to the pony wall, '
            'phone in one hand, almost no tilt; handheld with a slow '
            'breathing drift.',
  'enquadramento': 'Vertical 9:16. In: the slate coping across the middle '
                   'third with the objects on it, dark tile above, the wet '
                   'sloped floor and drain below. Cropped: ceiling, rain '
                   'head, any body.',
  'luz': 'Cool grey daylight from a high slot window, low contrast, the '
         'matte black stone swallowing the light.',
  'audio': 'Rain head drumming on micro-cement, water gurgling into the '
           'linear drain, wide room echo.',
  'aceita': ['po', 'cubos', 'pote', 'sache', 'creme', 'espuma'],
  'regua_cabe': True,
  'molhado': True},
 {'id': 'banco_teca_ripado_box',
  'curto': 'Banco ripado de teca dentro do box',
  'fonte': 'construido',
  'familia': 'chuveiro',
  'ambiente': 'Tiled shower enclosure in warm grey stone-look porcelain, a '
              'hand shower running on the far wall, steam thick in the air, '
              'water pooling under a slatted teak bench.',
  'superficie': 'The slatted dark teak shower bench seat — five oiled '
                'hardwood slats with one-centimetre gaps between them, '
                'soaked almost black; the jar and the box stand across two '
                'slats, straddling a gap, tilted a little by the ribs.',
  'camera': 'Phone held high, above the head, pointed almost straight down '
            'at the bench in a near-plumb top-down; handheld, slight sway.',
  'enquadramento': 'Vertical 9:16, top-down. In: the whole bench seat '
                   'filling the frame, the gaps between slats, the wet floor '
                   'showing under the bench at the edges. Cropped: walls, '
                   'shower head, the person entirely.',
  'luz': 'Warm recessed ceiling light through steam, soft, wet sheen running '
         'along each slat.',
  'audio': 'Shower running against tile, water dripping through the bench '
           'slats onto the floor below.',
  'aceita': ['pote', 'sache', 'creme', 'espuma'],
  'regua_cabe': False,
  'molhado': True},
 {'id': 'prateleira_aco_preto_no_trilho',
  'curto': 'Prateleira de aco preto fosco no trilho',
  'fonte': 'construido',
  'familia': 'chuveiro',
  'ambiente': 'Narrow modern shower stall, glossy white metro tile with '
              'black grout, a matte black rail system on the wall, black '
              'rain head running, water streaking the dark grout lines.',
  'superficie': 'A matte black powder-coated steel shelf clipped onto the '
                'vertical wall rail — a flat perforated tray with a raised '
                'lip, water beading in every perforation; all the objects '
                'stand on that black tray, high above the floor.',
  'camera': 'Shoulder height, tilted down about thirty degrees onto the '
            'shelf, phone in one hand; handheld with visible micro-tremor '
            'and one reframe.',
  'enquadramento': 'Vertical 9:16. In: the black rail climbing the frame, '
                   'the shelf with its objects in the lower middle, white '
                   'tile and black grout behind. Cropped: ceiling, floor, '
                   'any person.',
  'luz': 'Hard cool spotlight from above, strong contrast between the white '
         'tile and the black hardware.',
  'audio': 'Rain head running hard on tile, water ticking down through the '
           'perforated tray.',
  'aceita': ['po', 'pote', 'sache', 'creme', 'espuma'],
  'regua_cabe': True,
  'molhado': True},
 {'id': 'ventosa_plastica_sobre_banheira',
  'curto': 'Suporte plastico de ventosa sobre a banheira',
  'fonte': 'construido',
  'familia': 'banheira',
  'ambiente': 'Rented apartment bathroom: white subway tile with grey grout '
              'over a steel alcove tub filling behind a half-open striped '
              'curtain, cheap chrome spout, worn silicone at the joint.',
  'superficie': 'A small white plastic suction-cup shower caddy stuck flat '
                'on the subway tile above the tub — a shallow moulded tray '
                'with drain slots and two suction discs visible behind it; '
                'the jar sits alone on that flexing plastic tray.',
  'camera': 'Phone held at waist height and tilted UP at the caddy in a '
            'clear low angle, so the tile wall runs away above; handheld, '
            'unstable, one correction mid-shot.',
  'enquadramento': 'Vertical 9:16, low angle. In: the plastic tray with the '
                   'jar seen from below, the suction discs, the tile grid, '
                   'the curtain edge at the left. Cropped: the tub water, '
                   'the ceiling, any face.',
  'luz': 'Flat fluorescent ceiling light with a greenish cast, no daylight, '
         'dull plastic sheen.',
  'audio': 'Tub filling loudly off-frame, plastic curtain rustling, tinny '
           'echo of a small bathroom.',
  'aceita': ['pote', 'sache', 'creme'],
  'regua_cabe': False,
  'molhado': True},
 {'id': 'nicho_mosaico_hexagonal_marmore',
  'curto': 'Nicho de mosaico hexagonal de marmore',
  'fonte': 'construido',
  'familia': 'nicho',
  'ambiente': 'Shower walled in white subway tile with a recessed niche '
              'lined in white hexagonal marble mosaic, a chrome rain head '
              'running and throwing a curtain of water across the mouth of '
              'the niche.',
  'superficie': 'The floor of the recessed niche, paved in small white '
                'hexagonal marble mosaic with pale grout and sloped slightly '
                'to drain; the objects stand on that faceted stone floor, '
                'framed by the niche opening.',
  'camera': 'Eye level, perpendicular to the wall, the niche centred and '
            'symmetrical like a display case; locked framing with only a '
            'breathing drift, then one push-in.',
  'enquadramento': 'Vertical 9:16. The niche opening holds the centre of the '
                   'frame, subway tile all around it, the falling water '
                   'crossing in front of it. Cropped: rain head, floor, any '
                   'body.',
  'luz': 'Cool even shower light, the white mosaic bouncing it back, low '
         'contrast, damp sheen on every facet.',
  'audio': 'Rain head running past the niche, drips ticking inside the '
           'recess, tiled reverb.',
  'aceita': ['po', 'pote', 'sache', 'creme', 'espuma'],
  'regua_cabe': True,
  'molhado': True},
 {'id': 'bandeja_bambu_banheira_de_pes',
  'curto': 'Bandeja de bambu sobre a banheira de pes',
  'fonte': 'construido',
  'familia': 'banheira',
  'ambiente': 'Period bathroom with a white cast-iron clawfoot tub full of '
              'still hot water, steam rising, pale green wainscot panelling, '
              'a chrome telephone mixer hooked over the rolled rim.',
  'superficie': 'The flat bamboo bath caddy tray bridging the clawfoot tub '
                'from rim to rim — a dry slatted board with a raised lip and '
                'a fold-out book rest; every object stands on the pale '
                'bamboo with the steaming water directly beneath it.',
  'camera': 'Phone held high over the tub at about sixty degrees down, '
            'looking onto the tray; handheld, slow drift, no cut.',
  'enquadramento': 'Vertical 9:16. In: the whole tray across the frame, both '
                   'rolled tub rims, the steaming water at the edges below, '
                   'one clawfoot cut at the bottom. Cropped: the walls '
                   'above, any face.',
  'luz': 'Warm tungsten wall sconce through steam, soft haze, gentle golden '
         'falloff toward the water.',
  'audio': 'Still hot water shifting in a cast-iron tub, steam hiss, a spoon '
           'set down on bamboo.',
  'aceita': ['po', 'cubos', 'pote', 'sache', 'creme', 'liquido', 'espuma'],
  'regua_cabe': False,
  'molhado': False},
 {'id': 'saboneteira_moldada_fibra_de_vidro',
  'curto': 'Saboneteira moldada do encaixe de fibra',
  'fonte': 'construido',
  'familia': 'banheira',
  'ambiente': 'Builder-grade one-piece fiberglass tub and shower surround in '
              'almond white, faint mould in the seams, chrome sliding doors '
              'on a track, shower off and everything dry.',
  'superficie': 'The integral moulded soap ledge stamped into the fiberglass '
                'surround — a shallow oval recess with a raised rim at chest '
                'height, its bottom scoured chalky by years of cleaning; the '
                'jar sits inside that recess, wedged.',
  'camera': 'Chest height, angled slightly down and pressed close to the '
            'corner of the surround, phone in one hand; nearly static, small '
            'tremor.',
  'enquadramento': 'Vertical 9:16, tight. In: the moulded recess with the '
                   'jar, the seam of the surround, a sliver of the sliding '
                   'door track. Cropped: shower head, tub floor, any person.',
  'luz': 'Flat warm bulb light behind a plastic diffuser, low contrast, dull '
         'plastic reflection.',
  'audio': 'Dry bathroom room tone, an extractor fan humming, a sliding door '
           'rolling on its track.',
  'aceita': ['pote', 'sache', 'creme'],
  'regua_cabe': False,
  'molhado': False},
 {'id': 'banco_terrazzo_wetroom',
  'curto': 'Banco de terrazzo do wet room',
  'fonte': 'construido',
  'familia': 'chuveiro',
  'ambiente': 'Large walk-in shower lined in pale terrazzo with dark chips, '
              'a glass screen on one side, a ceiling rain head running '
              'behind, water sheeting across the sloped floor.',
  'superficie': 'The cantilevered terrazzo bench seat built into the shower '
                'wall — a thick pale slab flecked with black and rust chips, '
                'its front edge rounded and wet; the objects stand near that '
                'edge, close enough that the foam would run off it.',
  'camera': 'Phone held low, at knee height, almost level with the top of '
            'the bench and tilted a few degrees up; handheld, slow lateral '
            'drift.',
  'enquadramento': 'Vertical 9:16, low. In: the bench slab nearly edge-on '
                   'with the objects on it, the wet terrazzo wall behind, '
                   'the sloped floor at the bottom. Cropped: rain head, '
                   'ceiling, any body.',
  'luz': 'Neutral daylight through a frosted clerestory, soft, the terrazzo '
         'chips catching small glints.',
  'audio': 'Rain head falling behind the bench, water running down terrazzo, '
           'a wide tiled echo.',
  'aceita': ['po', 'cubos', 'pote', 'sache', 'creme', 'espuma'],
  'regua_cabe': True,
  'molhado': True},
 {'id': 'prateleira_pedra_sabao_verde',
  'curto': 'Prateleira de pedra-sabao esverdeada',
  'fonte': 'construido',
  'familia': 'chuveiro',
  'ambiente': 'Compact shower stall clad in split-face grey stone, a black '
              'exposed valve and rain head running, water darkening the '
              'stone and steam curling near the ceiling.',
  'superficie': 'A honed green-black soapstone shelf bolted into the stone '
                'wall — a dense matte slab with faint white veining and a '
                'chamfered front edge, water beading and slipping straight '
                'off it; the props stand on that dark stone.',
  'camera': 'Shoulder height, straight on to the shelf with only a slight '
            'downward tilt, phone in one hand; handheld, minimal drift.',
  'enquadramento': 'Vertical 9:16. In: the shelf across the middle third '
                   'with its objects, split-face stone above and below, '
                   'water falling at the right edge. Cropped: rain head, '
                   'floor, any face.',
  'luz': 'Moody low-key shower light, a single warm source high left, deep '
         'shadow inside the stone texture.',
  'audio': 'Rain head splashing on stone, water running off the shelf edge, '
           'a low tiled rumble.',
  'aceita': ['po', 'pote', 'sache', 'creme', 'espuma'],
  'regua_cabe': True,
  'molhado': True},
 {'id': 'inserto_inox_dentro_do_nicho',
  'curto': 'Inserto de inox dividindo o nicho',
  'fonte': 'construido',
  'familia': 'nicho',
  'ambiente': 'Shower niche cut into a wall of glossy dark green tile, a '
              'brushed stainless plate splitting it into two levels, a '
              'chrome shower arm running just outside the recess, with the '
              'jar visible in frame.',
  'superficie': 'The brushed stainless insert shelf that divides the niche '
                'in two — a flat metal plate set into the recess, its '
                'brushed grain running left to right, water standing on it '
                'in flat beads; the objects stand on that upper plate.',
  'camera': 'Eye level, perpendicular into the mouth of the niche, phone in '
            'one hand, static frame, then a slow push in to a macro on the '
            'jar.',
  'enquadramento': 'Vertical 9:16. In: the whole niche opening, the '
                   'stainless plate with its objects, the empty lower level, '
                   'dark green tile all around. Cropped: shower head, floor, '
                   'any body.',
  'luz': 'Cool downlight raking the brushed grain, a bright metal streak '
         'against the dark green tile.',
  'audio': 'Shower running just outside frame, water pinging on the metal '
           'plate, damp echo.',
  'aceita': ['po', 'pote', 'sache', 'creme', 'espuma'],
  'regua_cabe': True,
  'molhado': True},
 {'id': 'piso_de_seixos_do_box',
  'curto': 'Piso de seixos do box',
  'fonte': 'construido',
  'familia': 'chuveiro',
  'ambiente': 'Spa-style shower with walls of vertical cedar and a floor of '
              'river pebble mosaic, rain head running, water finding its way '
              'between the stones toward a hidden drain.',
  'superficie': 'The pebble mosaic shower floor itself — rounded grey and '
                'brown river stones set in dark grout, uneven and running '
                'with water; the jar and the box stand directly on the wet '
                'stones and are tilted off-square by them.',
  'camera': 'Phone held very low at knee height, angled down about seventy '
            'degrees at the floor; handheld, unsteady, one small correction.',
  'enquadramento': 'Vertical 9:16, steep and low. In: the pebble floor '
                   'filling the frame with the objects on it, the base of '
                   'the cedar wall at the top, water running between stones. '
                   'Cropped: everything above knee height.',
  'luz': 'Warm cedar-bounced light from a ceiling fixture, gold-brown cast, '
         'wet stones glinting.',
  'audio': 'Rain head hitting stone, water trickling between pebbles, a '
           'hollow drain gurgle.',
  'aceita': ['pote', 'sache', 'creme', 'espuma'],
  'regua_cabe': False,
  'molhado': True},
 {'id': 'peitoril_da_janela_do_box',
  'curto': 'Peitoril azulejado da janela do box',
  'fonte': 'construido',
  'familia': 'chuveiro',
  'ambiente': 'Tub-shower with an old frosted-glass window inside the wet '
              'zone, cream tile framing it, the shower running to the left, '
              'condensation running down the pane in long trails.',
  'superficie': 'The tiled window sill inside the shower — a narrow cream '
                'bullnose ledge sloping slightly inward, its grout darkened, '
                'standing water in the low corner; the props are lined up on '
                'that sill, backed against the frosted pane.',
  'camera': 'Eye level, straight at the window, phone in one hand at head '
            'height with no tilt; handheld, gentle sway, one slow step '
            'closer.',
  'enquadramento': 'Vertical 9:16. In: the frosted pane with its '
                   'condensation, the whole sill with its objects, tile on '
                   'both sides. Cropped: the shower head, the tub below, any '
                   'person.',
  'luz': 'Diffused daylight coming through the frosted glass, milky and '
         'even, backlighting the steam.',
  'audio': 'Shower running off to the left, condensation dripping off the '
           'sill, muffled traffic behind the glass.',
  'aceita': ['po', 'pote', 'sache', 'creme', 'espuma'],
  'regua_cabe': True,
  'molhado': True},
 {'id': 'mureta_porcelanato_curva_quadrante',
  'curto': 'Topo da mureta curva do box quadrante',
  'fonte': 'construido',
  'familia': 'chuveiro',
  'ambiente': 'Quadrant corner shower with a curved low wall instead of a '
              'door, beige porcelain tile, a chrome riser and hand shower '
              'running, water tracking around the curve.',
  'superficie': 'The flat capped top of the curved pony wall — a continuous '
                'strip of bullnose porcelain following the arc, about '
                'fifteen centimetres wide and wet; the objects stand along '
                'the curve, the box sitting off-square because of it.',
  'camera': 'Chest height, tilted down about thirty-five degrees along the '
            'arc of the wall, phone in one hand; handheld with drift that '
            'follows the curve.',
  'enquadramento': 'Vertical 9:16. In: the arc of the capped wall running '
                   'from lower left to upper right with the objects on it, '
                   'the enclosure behind, the bathroom floor outside at the '
                   'edge. Cropped: ceiling, any face.',
  'luz': 'Warm domestic light mixed with a cool bounce from outside the '
         'enclosure, wet gleam along the bullnose.',
  'audio': 'Hand shower running inside the enclosure, water running around '
           'the tiled curve, a slow drip outside.',
  'aceita': ['po', 'pote', 'sache', 'creme', 'espuma'],
  'regua_cabe': True,
  'molhado': True},
 {'id': 'prateleira_concreto_wetroom_industrial',
  'curto': 'Prateleira de concreto do wet room industrial',
  'fonte': 'construido',
  'familia': 'chuveiro',
  'ambiente': 'Industrial wet room: grey micro-cement walls and floor, '
              'exposed black plumbing, an oversized square rain head '
              'running, steam hanging in a shaft of daylight.',
  'superficie': 'A cast concrete shelf poured straight out of the '
                'micro-cement wall — a raw grey slab with visible aggregate '
                'and a chipped front edge, darkened where the water has '
                'soaked in; the props stand on that rough concrete.',
  'camera': 'Phone held below the shelf line, at hip height, tilted up so '
            'the underside of the slab reads; handheld, slight sway, one '
            'slow rise.',
  'enquadramento': 'Vertical 9:16, low angle. In: the underside and front '
                   'edge of the slab, the objects seen from just below, a '
                   'black pipe crossing the top. Cropped: rain head, floor, '
                   'any body.',
  'luz': 'Hard daylight shaft from a high window cutting through steam, '
         'strong contrast on the raw grey concrete.',
  'audio': 'Big rain head roaring on cement, water running off the slab '
           'edge, deep concrete reverb.',
  'aceita': ['po', 'cubos', 'pote', 'sache', 'creme', 'espuma'],
  'regua_cabe': True,
  'molhado': True},
 {'id': 'grade_cromada_sobre_banheira',
  'curto': 'Grade cromada atravessando a banheira',
  'fonte': 'construido',
  'familia': 'banheira',
  'ambiente': 'Hotel-style bathroom with a deep white tub full of hot water, '
              'steam rolling off the surface, white marble-look tile, a '
              'chrome hand shower coiled on the rim.',
  'superficie': 'The chrome wire tub rack straddling the bath from rim to '
                'rim — two parallel bars with a mesh centre, beaded with '
                'condensation; the jar and the box stand on that mesh with '
                'the steaming water directly under them, visible through the '
                'grid.',
  'camera': 'Phone held high over the tub at about forty-five degrees down, '
            'looking onto the rack; handheld, slow drift, steam crossing the '
            'lens.',
  'enquadramento': 'Vertical 9:16. In: the rack across the frame with its '
                   'objects, both tub rims, steaming water seen through the '
                   'mesh below. Cropped: the walls above, any person.',
  'luz': 'Warm ceiling downlight through heavy steam, hazy, soft chrome '
         'highlights.',
  'audio': 'Hot still water in a deep tub, steam hiss, the chrome rack '
           'ticking as weight shifts on it.',
  'aceita': ['pote', 'sache', 'creme', 'espuma'],
  'regua_cabe': False,
  'molhado': True},
 {'id': 'degrau_penny_tile_da_banheira',
  'curto': 'Degrau de penny tile da banheira embutida',
  'fonte': 'construido',
  'familia': 'banheira',
  'ambiente': 'Renovated bathroom with a drop-in tub set into a tiled '
              'platform, matte grey penny-round tile on the step and skirt, '
              'the tub still empty, the chrome filler standing dry, with the '
              'glass and jar visible in frame.',
  'superficie': 'The tiled masonry step in front of the drop-in tub — a '
                'broad platform paved in matte grey penny-round mosaic with '
                'pale grout, dry and slightly gritty underfoot; every object '
                'stands directly on that round-tiled step.',
  'camera': 'Phone held low, near the height of the step, tilted down about '
            'thirty degrees; handheld, small tremor, one slow crawl forward.',
  'enquadramento': 'Vertical 9:16, low. In: the penny-tile step filling the '
                   'lower two thirds with the objects on it, the tub skirt '
                   'rising behind, the filler cut at the top. Cropped: '
                   'ceiling, any face.',
  'luz': 'Even neutral daylight from a window off-frame, flat, a tiny shadow '
         'inside every grout ring.',
  'audio': 'Dry bathroom room tone, a distant pipe knock, a glass jar set '
           'down on tile.',
  'aceita': ['po', 'cubos', 'pote', 'sache', 'creme', 'liquido', 'espuma'],
  'regua_cabe': True,
  'molhado': False},
 {'id': 'estrado_de_ipe_no_box',
  'curto': 'Estrado de ipe no piso do box',
  'fonte': 'construido',
  'familia': 'chuveiro',
  'ambiente': 'Shower stall floored with a dark ipe duckboard over the '
              'drain, walls of charcoal ceramic, a chrome rain head running, '
              'water flooding between the boards and draining beneath them.',
  'superficie': 'The dark ipe duckboard grate on the shower floor — oiled '
                'hardwood slats gone almost black with water, two-centimetre '
                'gaps between them and water rushing underneath; the jar '
                'stands across two slats, over a gap.',
  'camera': 'Phone held above the head, pointed almost straight down at the '
            'duckboard; handheld with noticeable sway, descending slowly '
            'toward the jar.',
  'enquadramento': 'Vertical 9:16, near-plumb top-down. In: the duckboard '
                   'filling the frame, the objects standing on it, water '
                   'moving under the slats. Cropped: walls, rain head, the '
                   'person entirely.',
  'luz': 'Cool overhead light on near-black wet wood, bright specular '
         'ribbons running along each slat.',
  'audio': 'Rain head hammering wood, water rushing under the boards into '
           'the drain.',
  'aceita': ['pote', 'sache', 'creme', 'espuma'],
  'regua_cabe': False,
  'molhado': True},
 {'id': 'prateleira_latao_azulejo_verde',
  'curto': 'Prateleira de latao no azulejo verde',
  'fonte': 'construido',
  'familia': 'chuveiro',
  'ambiente': 'Small shower clad in glossy dark green tile with brass '
              'fittings, an unlacquered brass shower head running warm '
              'water, patina streaks and hard-water spots across the metal, '
              'with the jar visible in frame.',
  'superficie': 'An unlacquered aged brass corner shelf with a lipped edge '
                'and a patina of green and brown spotting, screwed into the '
                'tiled corner; the props stand on that warm dull metal with '
                'water standing in the lip around them.',
  'camera': 'Chest height, tilted down about twenty-five degrees into the '
            'corner, phone in one hand; handheld, steady, one slow push-in '
            'on the jar.',
  'enquadramento': 'Vertical 9:16. In: the brass shelf with its objects, the '
                   'green tile corner joint, the brass shower arm cut at the '
                   'top. Cropped: ceiling, floor, any body.',
  'luz': 'Warm amber light, the brass glowing against the cold green tile, '
         'moderate contrast.',
  'audio': 'Shower running on glazed tile, water pinging on brass, a small '
           'metallic drip.',
  'aceita': ['po', 'pote', 'sache', 'creme', 'espuma'],
  'regua_cabe': True,
  'molhado': True},
 {'id': 'pia_marmore_cultivado',
  'curto': 'Bancada de pia de marmore cultivado',
  'fonte': 'lido',
  'familia': 'pia',
  'ambiente': 'Clean middle-class family bathroom, cream painted walls, '
              'frameless mirror reflecting a grey-and-white striped shower '
              'curtain and a white-framed window with daylight; a dark brown '
              'wood cabinet below the vanity, with the glass visible in '
              'frame.',
  'superficie': 'The flat white cultured-marble vanity top, on the dry wing '
                'to the LEFT of the oval integrated basin: one moulded '
                'seamless piece, glossy, objects resting directly on the '
                'stone at about thirty-two inches off the floor.',
  'camera': 'Chest height, tripod-still, angled down about twenty-five to '
            'thirty degrees at the vanity; the phone is clamped to a shelf '
            'across the room so both hands stay free and only they enter '
            'frame.',
  'enquadramento': 'Vertical 9:16, one unchanging medium shot: basin and '
                   'chrome faucet on the right third, the dry left wing at '
                   'centre, mirror across the top third. Floor, ceiling and '
                   'any body are cut.',
  'luz': 'Flat daylight from the window at camera left, cool and even, no '
         'hard shadow; the mirror bounces a second soft fill onto the stone.',
  'audio': 'Room tone only, no music: a faint tap drip into the basin, '
           'muffled street traffic through the window glass, the odd creak '
           'of the house.',
  'aceita': ['po', 'cubos', 'pote', 'sache', 'creme', 'liquido', 'espuma'],
  'regua_cabe': True,
  'molhado': False},
 {'id': 'pia_direita_pastilha_vidro',
  'curto': 'Tampo branco a direita da cuba, com pastilha de vidro',
  'fonte': 'lido',
  'familia': 'pia',
  'ambiente': 'Warm domestic bathroom, chrome two-handle faucet, a glass '
              'mosaic strip in beige, brown and sage behind the basin, light '
              'oak cabinet doors below, taps shut and the whole counter dry.',
  'superficie': 'The flat white cultured-marble counter on the DRY RIGHT '
                'side of the recessed oval basin: glossy, seamless, the '
                'ceiling fixture reflected in it; everything sits on that '
                'right-hand plateau, never inside the bowl.',
  'camera': 'Phone in one raised hand, chest-to-shoulder height, tilted '
            'steeply down forty-five to sixty degrees over the counter; '
            'slight handheld drift, the free hand working below the lens.',
  'enquadramento': 'Vertical 9:16. Faucet top-left, basin at the left edge, '
                   'the dry right counter at centre, the oak cabinet door '
                   'clipped along the bottom. Ceiling, floor and any torso '
                   'stay out.',
  'luz': 'Warm tungsten from a single vanity fixture above the mirror, a '
         'soft highlight streak along the glossy counter, gentle shadow '
         'under every object.',
  'audio': 'Room tone only, no music: extractor fan humming steadily, '
           'distant water knocking in the wall pipes, hands sliding on '
           'stone.',
  'aceita': ['po', 'cubos', 'pote', 'sache', 'creme', 'liquido', 'espuma'],
  'regua_cabe': True,
  'molhado': False},
 {'id': 'bancada_marmore_led_azul',
  'curto': 'Tampo de marmore veiado com fita de LED azul',
  'fonte': 'lido',
  'familia': 'pia',
  'ambiente': 'Upper-middle-class bathroom in veined white marble, chrome '
              'towel bar holding a red-white-and-blue striped towel, wall '
              'soap dish; a blue LED strip glows along the wall behind, the '
              'marble dry, with the glass visible in frame.',
  'superficie': 'The polished white marble vanity slab with grey veining, on '
                'the flat run in FRONT of the built-in basin, the basin lip '
                'clipped at the bottom of frame; all objects lined up on '
                'that cold dry stone.',
  'camera': 'Low, almost at counter level, frontal with a slight upward '
            'tilt; the phone is propped against the mirror splashback so the '
            'frame never moves and only hands cross it.',
  'enquadramento': 'Vertical 9:16, near-macro product framing: the marble '
                   'run fills the lower half, the LED strip streaks the '
                   'background out of focus, towel bar soft at the top. '
                   'Everything above chest is cut.',
  'luz': 'Warm ceiling light on the objects against a cold blue LED wash '
         'behind, two colour temperatures in one frame, hard highlights on '
         'the polished stone.',
  'audio': 'Room tone only, no music: a low ventilation hiss, one distant '
           'door closing elsewhere in the house, glass and metal set down on '
           'stone.',
  'aceita': ['po', 'cubos', 'pote', 'sache', 'creme', 'liquido', 'espuma'],
  'regua_cabe': True,
  'molhado': False},
 {'id': 'bancada_concreto_moldado',
  'curto': 'Bancada de concreto moldado cinza',
  'fonte': 'construido',
  'familia': 'pia',
  'ambiente': 'Renovated loft-style bathroom: a poured concrete vanity slab, '
              'matte dark grey with tiny air pockets, matte black wall '
              'faucet, exposed brick painted white behind, everything dry '
              'and cold.',
  'superficie': 'The two-inch-thick poured concrete vanity slab, matte dark '
                'grey and slightly porous, on the flat span to the RIGHT of '
                'the round vessel bowl; objects sit straight on the raw '
                'concrete, no mat, no tray.',
  'camera': 'Standing beside the slab, phone held one-handed at waist '
            'height, looking down about forty-five degrees; small handheld '
            'breathing, no zoom through the take.',
  'enquadramento': 'Vertical 9:16. The concrete slab fills the lower two '
                   'thirds on a diagonal, black faucet top-right, painted '
                   'brick behind. Mirror, ceiling and any body are outside '
                   'the frame.',
  'luz': 'Hard directional light from a single black pendant at frame left, '
         'long dark shadows raking across the concrete, deep contrast.',
  'audio': 'Room tone only, no music: a heavy vent motor two rooms away, an '
           'object grating faintly on concrete, no running water at all.',
  'aceita': ['po', 'cubos', 'pote', 'sache', 'creme', 'liquido', 'espuma'],
  'regua_cabe': True,
  'molhado': False},
 {'id': 'bancada_teca_borda_viva',
  'curto': 'Prancha de teca de borda viva com cuba de apoio',
  'fonte': 'construido',
  'familia': 'pia',
  'ambiente': 'Spa-like home bathroom: a thick live-edge teak slab as '
              'vanity, oiled honey grain, a white ceramic vessel bowl on '
              'top, pale plaster wall, folded linen towel, the wood dry and '
              'warm.',
  'superficie': 'The oiled live-edge teak slab, its bark-shaped front edge '
                'visible, on the wide flat area LEFT of the white vessel '
                'bowl; objects stand on bare warm wood with the grain '
                'running lengthwise beneath them.',
  'camera': 'Phone in the left hand at hip height, angled down about fifty '
            'degrees over the slab; slow handheld drift closing in across '
            'the length of the take.',
  'enquadramento': 'Vertical 9:16. The teak slab runs corner to corner, '
                   'vessel bowl at the right edge, plaster wall filling the '
                   'top third. Floor, mirror and any person are cut.',
  'luz': 'Low warm side light from a paper-shaded sconce, the grain raking '
         'and shadowed, the wood glowing amber.',
  'audio': 'Room tone only, no music: a quiet house hum, birds faint behind '
           'a closed window, wood creaking under weight.',
  'aceita': ['po', 'cubos', 'pote', 'sache', 'creme', 'liquido', 'espuma'],
  'regua_cabe': False,
  'molhado': False},
 {'id': 'bancada_azulejo_rosa_1950',
  'curto': 'Bancada azulejada rosa dos anos 50',
  'fonte': 'construido',
  'familia': 'pia',
  'ambiente': 'Untouched 1950s American bathroom: a counter tiled in glossy '
              'pink four-inch squares with darkened grout, chrome edge trim, '
              'pink wall tile to shoulder height, worn but dry and lived-in.',
  'superficie': 'The pink four-inch-square glazed tile counter top beside '
                'the basin, grout lines forming a visible grid under the '
                'objects and a chrome bullnose strip along the front edge; '
                'each object straddles two or three tiles.',
  'camera': 'Phone braced against the wall mirror at chest height, angled '
            'down thirty-five degrees; almost no drift, the frame steady '
            'while hands come in from the right.',
  'enquadramento': 'Vertical 9:16. The tile grid fills the lower half, pink '
                   'wall tile and a chrome soap holder above, the basin edge '
                   'clipped at left. Ceiling and any torso are cut.',
  'luz': 'Two frosted bulbs over the mirror, warm and slightly green, '
         'specular dots on every glazed tile.',
  'audio': 'Room tone only, no music: an old exhaust fan rattling, water '
           'hammer in the wall, a clock ticking beyond the door.',
  'aceita': ['po', 'cubos', 'pote', 'sache', 'creme', 'liquido', 'espuma'],
  'regua_cabe': True,
  'molhado': False},
 {'id': 'borda_pia_pedestal',
  'curto': 'Aro estreito da pia de coluna',
  'fonte': 'construido',
  'familia': 'pia',
  'ambiente': 'Small old guest bathroom with a white porcelain pedestal sink '
              'standing free against beadboard panelling painted grey-green; '
              'cracked hex floor tile, the basin dry, a thin sliver of soap '
              'on the rim.',
  'superficie': 'The narrow oval porcelain rim of the pedestal sink itself, '
                'only about three inches of flat glaze between the bowl and '
                'the outer edge; objects are crowded onto that shallow lip, '
                'one nearly touching the next.',
  'camera': 'Phone held high in one hand near eye level, aimed almost '
            'straight down onto the small rim, the operator standing over '
            'the basin; visible handheld sway.',
  'enquadramento': 'Vertical 9:16, tight: the oval rim and the dark bowl '
                   'fill the frame, chrome taps at the top edge, a strip of '
                   'beadboard behind. The pedestal column and floor are cut.',
  'luz': 'A single bare bulb overhead, a hot pool of light on the white '
         'porcelain, the edges falling into shadow.',
  'audio': 'Room tone only, no music: a slow drip into the dry basin, '
           'floorboards creaking, wind pressing on an old window.',
  'aceita': ['po', 'pote', 'sache', 'creme', 'espuma'],
  'regua_cabe': False,
  'molhado': False},
 {'id': 'prateleira_vidro_armario_espelho',
  'curto': 'Prateleira de vidro do armario-espelho aberto',
  'fonte': 'construido',
  'familia': 'pia',
  'ambiente': 'A mirrored medicine cabinet standing open above a sink, three '
              'tempered glass shelves on chrome clips, the interior painted '
              'white, a toothbrush glass and a razor pushed aside, dry and '
              'slightly dusty.',
  'superficie': 'The middle tempered-glass shelf inside the open mirror '
                'cabinet, five inches deep with polished edges and the white '
                'cabinet back right behind it; objects sit on clear glass at '
                'eye level, the shelf edge cutting a bright line.',
  'camera': "Phone at eye height held straight out at arm's length, level "
            'with the shelf and perpendicular to it, no tilt; the mirrored '
            'door is angled away so the lens is not doubled.',
  'enquadramento': 'Vertical 9:16. The open cabinet interior fills the '
                   'frame, the middle shelf across the centre, the shelf '
                   'above clipping the top. Sink, wall and any body are '
                   'outside.',
  'luz': 'Cool white LED strip under the top shelf, light falling straight '
         'down, thin bright lines along every glass edge.',
  'audio': 'Room tone only, no music: a ballast tick from the light, glass '
           'shelf ringing faintly when touched, muffled voices downstairs.',
  'aceita': ['po', 'cubos', 'pote', 'sache', 'creme'],
  'regua_cabe': False,
  'molhado': False},
 {'id': 'tampa_vaso_fechada',
  'curto': 'Tampa fechada do vaso sanitario',
  'fonte': 'lido',
  'familia': 'vaso',
  'ambiente': 'Clean modern middle-class bathroom: large beige wall tile '
              'with a border strip, a white two-piece toilet centred, a '
              'white tub with chrome valves at right, beige floor tile, no '
              'window.',
  'superficie': 'The closed white toilet seat lid, lowered flat and used as '
                'a work bench: a hard glossy oval at knee-to-thigh height '
                'with the hinges visible at the back, objects standing '
                'directly on the plastic lid.',
  'camera': 'Standing in front of the toilet, phone in one hand at chest '
            'height, tilted down thirty to forty degrees onto the lid; the '
            'frame holds still a long while before creeping closer.',
  'enquadramento': 'Vertical 9:16. Cistern and its flat top fill the upper '
                   "third, the lid with the objects the middle, the seat's "
                   'front edge closes the bottom; the tub enters the right '
                   'strip. Floor and body are cut.',
  'luz': 'Flat warm ceiling light, no hard shadow, the whole frame bright '
         'and ceramic-white.',
  'audio': 'Room tone only, no music: a cistern refilling faintly then '
           'stopping, a hard plastic lid creaking under weight, shoes '
           'shifting on tile.',
  'aceita': ['po', 'cubos', 'pote', 'sache', 'creme', 'liquido', 'espuma'],
  'regua_cabe': True,
  'molhado': False},
 {'id': 'caixa_acoplada_porcelana',
  'curto': 'Tampo da caixa acoplada do vaso',
  'fonte': 'construido',
  'familia': 'vaso',
  'ambiente': 'Narrow apartment bathroom tiled to the ceiling in white '
              "subway tile with grey grout; the toilet's ceramic cistern "
              'stands against the wall, its lid dusty at the corners, a '
              'spare roll on top.',
  'superficie': 'The flat porcelain lid of the toilet cistern: a hard white '
                'rectangle about seven inches deep at waist-to-chest height, '
                'its rounded edge and the small flush-button hole visible; '
                'objects line up along that depth.',
  'camera': 'Phone held low in one hand at roughly waist level, tilted '
            'slightly UP so the cistern lid sits on the horizon line; the '
            'operator stands close, one shoulder near the wall.',
  'enquadramento': 'Vertical 9:16. The cistern lid runs across the lower '
                   'third as a shelf, white subway tile fills everything '
                   'above, the bowl and floor stay out of frame.',
  'luz': 'Cold ceiling LED panel, even and shadowless, grout lines reading '
         'grey against bright tile.',
  'audio': "Room tone only, no music: neighbours' plumbing rushing behind "
           'the wall, a ceramic lid clinking, a lift motor somewhere in the '
           'building.',
  'aceita': ['po', 'cubos', 'pote', 'sache', 'creme', 'liquido', 'espuma'],
  'regua_cabe': True,
  'molhado': False},
 {'id': 'peitoril_azulejo_vidro_martelado',
  'curto': 'Peitoril azulejado da janela de vidro martelado',
  'fonte': 'lido',
  'familia': 'outro',
  'ambiente': 'Old lived-in American bathroom: chequered beige wall tile to '
              'mid-height, cream paint above, a hammered frosted glass '
              'window at right throwing a late-afternoon orange halo across '
              'the room.',
  'superficie': 'The narrow tiled window sill pressed against the frosted '
                'glass: a strip of pale beige tile barely wider than a hand, '
                'grout darkened at the joints, objects crowded in a single '
                'row along it.',
  'camera': 'Phone held low, almost level with the sill and slightly below '
            'it looking up; the operator crouches at the window, one hand on '
            'the phone, the other reaching in from the right.',
  'enquadramento': 'Vertical 9:16. The sill runs across the lower third, the '
                   'frosted pane fills the upper two thirds as a glowing '
                   'screen, the window frame clipped both sides. Floor and '
                   'any body are cut.',
  'luz': 'Late afternoon sun through hammered glass: a warm orange bloom '
         'behind the objects rimming their edges, their front faces in soft '
         'shade.',
  'audio': 'Room tone only, no music: sparrows and a distant lawnmower '
           'outside the closed window, glass rattling gently in its frame.',
  'aceita': ['po', 'pote', 'sache', 'creme', 'espuma'],
  'regua_cabe': True,
  'molhado': False},
 {'id': 'peitoril_marmore_basculante',
  'curto': 'Peitoril fundo de marmore sob janela basculante',
  'fonte': 'construido',
  'familia': 'outro',
  'ambiente': 'Bathroom of an old brick house: a deep white marble window '
              'sill under a top-hinged awning window cranked half open, '
              'peeling white paint on the frame, a dry potted fern pushed to '
              'one corner.',
  'superficie': 'The deep white marble window sill, ten inches front to back '
                'with a rounded drip edge and a faint grey vein, cool and '
                'dry; objects stand in the middle of that slab with room to '
                'spare around them.',
  'camera': "Phone braced on the opposite wall's towel bar at chest height, "
            'looking straight across at the sill with a mild downward tilt '
            'of twenty degrees; fixed frame, hands entering from the left.',
  'enquadramento': 'Vertical 9:16. The marble sill crosses the lower half, '
                   'the open awning pane and a slice of green garden fill '
                   'the top, the wall closes both sides. Ceiling, floor and '
                   'body are cut.',
  'luz': 'Overcast north daylight, soft and shadowless, cool on the marble '
         'with a faint green cast from the garden outside.',
  'audio': 'Room tone only, no music: light wind through the open pane, '
           'leaves moving, a dog barking two yards away.',
  'aceita': ['po', 'cubos', 'pote', 'sache', 'creme', 'liquido', 'espuma'],
  'regua_cabe': True,
  'molhado': False},
 {'id': 'banquinho_madeira_macica',
  'curto': 'Banquinho baixo de madeira macica',
  'fonte': 'lido',
  'familia': 'banheira',
  'ambiente': 'Domestic bathroom with a white built-in alcove tub half full '
              'of still pale blue-green water, chrome lever mixer and a '
              'coiled hand-shower hose on smooth white drywall, dark '
              'laminate floor beyond.',
  'superficie': 'The solid light-wood top of a low sauna-style stool '
                'standing against the outside of the tub: a honey plank seat '
                'with visible legs and a cross rail at knee height, every '
                'object sitting on that small tabletop.',
  'camera': 'Standing beside the tub, phone in one hand at hip height '
            'looking down about forty-five degrees; the composition runs on '
            'the diagonal and closes in slowly through the take.',
  'enquadramento': 'Vertical 9:16. Tub edge and still water at left, white '
                   'wall top right, the stool with its objects in the lower '
                   'right corner. Ceiling, most of the floor and any person '
                   'are cut.',
  'luz': 'Soft domestic ceiling light, no steam, a gentle sheen on the still '
         'water bouncing pale blue onto the white wall.',
  'audio': 'Room tone only, no music: still water settling with tiny plips, '
           'a hose swinging against tile, a television muffled beyond the '
           'door.',
  'aceita': ['po', 'cubos', 'pote', 'sache', 'creme', 'liquido', 'espuma'],
  'regua_cabe': True,
  'molhado': False},
 {'id': 'borda_banheira_seca_hospede',
  'curto': 'Borda seca da banheira de hospedes',
  'fonte': 'construido',
  'familia': 'banheira',
  'ambiente': 'Unused guest bathroom kept spotless: a bone-dry white alcove '
              'tub with taps shut and a clean towel folded over the rim, '
              'white subway tile, the shower curtain pushed all the way to '
              'one end.',
  'superficie': 'The flat white acrylic tub rim at the head of the bath, the '
                'wide dry ledge where the tub meets the tiled wall, spotless '
                'and free of water marks; objects stand in a row on that '
                'ledge with the bowl dropping away behind.',
  'camera': 'Kneeling at the side of the tub, phone in one hand just above '
            'the rim, angled down fifty-five degrees; small breathing drift, '
            'the free hand entering at the bottom edge.',
  'enquadramento': 'Vertical 9:16. The dry rim runs diagonally through the '
                   'lower half, the empty tub floor out of focus behind, '
                   'tile and the folded towel closing the top. Ceiling and '
                   'body are cut.',
  'luz': 'Bright neutral ceiling light, everything white on white, only the '
         'objects carrying colour.',
  'audio': 'Room tone only, no music: a dead-quiet room, one hollow knock '
           'when something touches the acrylic, faint traffic far off.',
  'aceita': ['po', 'cubos', 'pote', 'sache', 'creme', 'liquido', 'espuma'],
  'regua_cabe': True,
  'molhado': False},
 {'id': 'tabua_acougueiro_cozinha',
  'curto': 'Bancada de tabua de acougueiro na cozinha',
  'fonte': 'lido',
  'familia': 'cozinha',
  'ambiente': 'Rustic rural American kitchen at breakfast time: a light '
              'butcher-block counter with visible glue joints, knife scars '
              'and dark oil stains, slate-green tile backsplash, a white '
              'outlet with a black cord hanging, with the glass visible in '
              'frame.',
  'superficie': 'The light butcher-block counter top itself, end-jointed '
                'maple strips running vertically with knife marks and water '
                'stains in the grain, the front edge of the counter closing '
                'the bottom of frame; everything rests directly on the wood.',
  'camera': 'Over-the-shoulder POV of somebody working the counter: phone '
            'held above and behind the hands at about forty-five degrees, '
            'standing height, small reframing drift, no cuts.',
  'enquadramento': 'Vertical 9:16. A window corner top right with its wooden '
                   'sill behind, a paper-towel roll at right, the bowl '
                   'centred in the middle third, hands filling the lower '
                   'third. Ceiling and any face are cut.',
  'luz': 'Hard morning sun through the wooden window, a bright diagonal bar '
         'across the counter, deep warm shadow on the opposite side.',
  'audio': 'Room tone only, no music: a refrigerator compressor, birds '
           'outside, a spoon knocking glass, footsteps on a wooden floor.',
  'aceita': ['po', 'cubos', 'pote', 'sache', 'creme', 'liquido', 'espuma'],
  'regua_cabe': False,
  'molhado': False},
 {'id': 'assento_chuveiro_teca_seco',
  'curto': 'Assento dobravel de teca, chuveiro desligado',
  'fonte': 'construido',
  'familia': 'chuveiro',
  'ambiente': 'Walk-in shower standing completely dry, taps shut and the '
              'glass door swung open: large grey porcelain wall tile, a '
              'fixed teak folding seat down against the wall, a towel on the '
              'outside hook.',
  'superficie': 'The slatted teak folding shower seat, lowered and locked '
                'horizontal: five oiled slats with narrow gaps between them '
                'at knee height on brushed-steel brackets; objects straddle '
                'two slats each and stand dry.',
  'camera': 'Crouching inside the open shower, phone held one-handed just '
            "above the seat, tilted down sixty degrees; the operator's knee "
            'near the tile, mild handheld sway.',
  'enquadramento': 'Vertical 9:16. The teak seat crosses the lower half with '
                   'its gaps visible, grey tile fills the top, the open '
                   'glass door edge at right. Drain, ceiling and any body '
                   'are cut.',
  'luz': 'Cool recessed downlight in the shower ceiling, a single soft pool '
         'on the teak, the tile falling grey and even.',
  'audio': 'Room tone only, no music: the hollow tiled echo of every small '
           'sound, a drain sighing, a bathroom door hinge far away.',
  'aceita': ['po', 'cubos', 'pote', 'sache', 'creme', 'espuma'],
  'regua_cabe': False,
  'molhado': False},
 {'id': 'tampo_maquina_lavar',
  'curto': 'Tampo esmaltado da maquina de lavar',
  'fonte': 'construido',
  'familia': 'outro',
  'ambiente': 'Laundry nook inside a family bathroom: a white front-loading '
              'washing machine under a shelf of detergent bottles, its '
              'enamel top scuffed, a wicker basket of towels shoved against '
              'it, all dry.',
  'superficie': 'The flat white enamel top of the front-loading washing '
                'machine: a hard hip-height rectangle with the control panel '
                'raised at the back and two shallow dents near the edge; '
                'objects sit on the bare enamel, slightly off centre.',
  'camera': 'Standing at the machine, phone in one hand at chest height '
            'tilted down forty degrees; the machine is running, so the whole '
            'frame carries a fine constant vibration.',
  'enquadramento': 'Vertical 9:16. The enamel top fills the lower two '
                   'thirds, control panel and detergent shelf across the '
                   'top, the door porthole clipped at the bottom. Ceiling '
                   'and body are cut.',
  'luz': 'Cold overhead fluorescent tube, flat and slightly blue, a hard '
         'bright reflection running the length of the enamel.',
  'audio': 'Room tone only, no music: a washing machine drum spinning up and '
           'holding, objects buzzing lightly against enamel, water draining '
           'inside the machine.',
  'aceita': ['po', 'cubos', 'pote', 'sache', 'creme', 'liquido', 'espuma'],
  'regua_cabe': True,
  'molhado': False},
 {'id': 'tampa_cesto_vime',
  'curto': 'Tampa do cesto de roupa de vime',
  'fonte': 'construido',
  'familia': 'outro',
  'ambiente': 'Corner of a lived-in family bathroom: a tall seagrass laundry '
              'hamper with its flat woven lid shut, a sock caught under the '
              'rim, painted wainscot behind, a bath mat rolled at its base.',
  'superficie': 'The flat woven lid of the closed laundry hamper: a round '
                'basketwork disc at thigh height with a raised braided rim '
                'and a clear weave pattern, springing slightly under weight; '
                'objects stand mid-weave.',
  'camera': 'Squatting beside the hamper, phone in one hand at about the '
            'height of the lid, tilted down thirty-five degrees; noticeable '
            "handheld sway as the operator's weight shifts.",
  'enquadramento': 'Vertical 9:16. The round lid fills the lower two thirds '
                   'as a woven field, wainscot and a hanging towel behind, '
                   'the hamper body clipped at the bottom. Ceiling and body '
                   'are cut.',
  'luz': 'Warm low sidelight from a floor-level plug-in nightlight and the '
         'open door, the weave raking into strong texture.',
  'audio': 'Room tone only, no music: wicker creaking under weight, the '
           'house settling, someone walking past in the hallway.',
  'aceita': ['po', 'cubos', 'pote', 'sache', 'creme'],
  'regua_cabe': False,
  'molhado': False},
 {'id': 'radiador_ferro_fundido',
  'curto': 'Topo do radiador de ferro fundido',
  'fonte': 'construido',
  'familia': 'outro',
  'ambiente': 'Old East Coast bathroom in winter: a cast-iron column '
              'radiator painted thick cream stands under the window, cold '
              'and switched off, paint chipped at the valve, a towel over '
              'the top rail.',
  'superficie': 'The flat cast-iron top rail of the column radiator: a '
                'narrow painted ledge at hip height with the ribs of each '
                'column showing as slots underneath; objects balance on the '
                'solid strip along its front edge.',
  'camera': 'Standing at the radiator, phone in one hand at waist height '
            'tilted down fifty degrees; the operator leans in so the top '
            'rail reads as a shelf, small drift throughout.',
  'enquadramento': 'Vertical 9:16. The painted top rail crosses the lower '
                   'third, the column fins fall away below it, the window '
                   'and its shutter fill the upper half. Floor and body are '
                   'cut.',
  'luz': 'Grey winter daylight from the window behind, the objects half in '
         'silhouette, the cream paint reading almost white along the top '
         'edge.',
  'audio': 'Room tone only, no music: iron ticking as the heating cools, '
           'wind in the window frame, a metal cap tapping the radiator.',
  'aceita': ['po', 'pote', 'sache', 'creme', 'espuma'],
  'regua_cabe': False,
  'molhado': False},
 {'id': 'radiador_painel_branco',
  'curto': 'Aba superior do radiador de painel',
  'fonte': 'construido',
  'familia': 'outro',
  'ambiente': 'Modern rented flat bathroom: a flat white steel panel '
              'radiator on the wall, switched off and cold, grey vinyl '
              'floor, a chrome towel ring beside it, a plain roller blind '
              'half down.',
  'superficie': 'The narrow flat top ledge of the white panel radiator: '
                'about two inches of painted steel with a slotted grille '
                'running along it at chest height; objects sit on the solid '
                'stretch between two slots, wall right behind them.',
  'camera': 'Phone held at chest height in one hand, level with the ledge '
            'and nearly straight on, only a slight downward tilt; the '
            'operator stands square to the wall, one step back.',
  'enquadramento': "Vertical 9:16. The radiator's top ledge cuts across the "
                   'middle of the frame, the ribbed panel below, plain '
                   'painted wall above. Floor, ceiling and any body are cut.',
  'luz': 'Neutral daylight through the half-drawn blind, flat and soft, a '
         'thin highlight along the painted steel edge.',
  'audio': 'Room tone only, no music: building ventilation, a lift somewhere '
           'in the block, metal ringing faintly when something is set down.',
  'aceita': ['po', 'pote', 'sache', 'creme'],
  'regua_cabe': False,
  'molhado': False},
 {'id': 'toalha_dobrada_toalheiro',
  'curto': 'Toalha dobrada sobre o toalheiro',
  'fonte': 'construido',
  'familia': 'outro',
  'ambiente': 'Guest bathroom set up like a small hotel: a chrome ladder '
              'towel rail on the wall, a thick white waffle towel folded in '
              'three over the middle bar, grey-green paint, a framed print '
              'beside it.',
  'superficie': 'The thick white waffle towel folded in three over the '
                'middle bar of the chrome ladder rail: a soft padded shelf '
                'at chest height that dips under each object, the chrome bar '
                'visible at both ends of the fold.',
  'camera': 'Phone held at chest height in one hand, almost level with the '
            'towel and tilted down twenty degrees; the operator stands close '
            'to the wall, small breathing movement.',
  'enquadramento': 'Vertical 9:16. The folded towel runs across the middle '
                   'of the frame like a shelf, empty rails above and below, '
                   'painted wall filling the rest. Floor, ceiling and any '
                   'body are cut.',
  'luz': 'Soft warm sconce light from the left, the waffle weave picking up '
         'texture, a gentle shadow pooling under each object.',
  'audio': 'Room tone only, no music: an almost silent room, cloth '
           'compressing under weight, the chrome rail humming faintly when '
           'knocked.',
  'aceita': ['po', 'pote', 'sache', 'creme'],
  'regua_cabe': False,
  'molhado': False},
 {'id': 'prateleira_flutuante_carvalho',
  'curto': 'Prateleira flutuante de carvalho sobre o vaso',
  'fonte': 'construido',
  'familia': 'outro',
  'ambiente': 'Small bathroom with a thick oak floating shelf mounted above '
              'the toilet, no visible brackets, matte navy wall, a trailing '
              'plant in a clay pot at one end, everything dry.',
  'superficie': 'The thick oak floating shelf above the toilet: a two-inch '
                'solid plank with no brackets at chest height, grain running '
                'left to right; objects stand in the clear middle stretch, '
                'the plant pot pushed to the far end.',
  'camera': 'Phone held in one hand slightly below the shelf at chest '
            'height, tilted UP about fifteen degrees so the plank reads as a '
            'stage; the operator stands a pace back from the wall.',
  'enquadramento': 'Vertical 9:16. The shelf runs across the lower middle, '
                   'navy wall fills the top, the toilet cistern clipped in '
                   'the bottom corner. Ceiling, floor and any body are cut.',
  'luz': 'Warm directional light from a wall sconce at frame right, the oak '
         'glowing, a soft shadow of every object thrown left along the '
         'plank.',
  'audio': 'Room tone only, no music: a very quiet room, leaves brushing the '
           'wall, the wooden shelf knocking softly.',
  'aceita': ['po', 'cubos', 'pote', 'sache', 'creme', 'liquido', 'espuma'],
  'regua_cabe': False,
  'molhado': False},
 {'id': 'carrinho_aco_rodinhas',
  'curto': 'Carrinho auxiliar de aco com rodinhas',
  'fonte': 'construido',
  'familia': 'outro',
  'ambiente': 'Bathroom of a converted garage flat: a mint-green '
              'powder-coated steel utility trolley on castors parked beside '
              'the basin, three tiers of towels and bottles, bare concrete '
              'floor, dry.',
  'superficie': 'The top tier of the mint-green powder-coated steel trolley: '
                'a shallow tray with a raised lip all around and a chipped '
                'rolled edge at hip height; objects sit inside the tray with '
                'that lip in front of them.',
  'camera': 'Standing over the trolley, phone in one hand at chest height '
            'tilted down fifty degrees; the trolley rolls a fraction when '
            'touched, so the frame shifts once during the take.',
  'enquadramento': 'Vertical 9:16. The mint tray fills the lower two thirds '
                   'with its lip in front, the second tier peeking below, '
                   'tiled wall behind. Castors, floor and body are cut.',
  'luz': 'Cool bright ceiling light, the mint reading saturated, small hard '
         'reflections skidding across the powder-coated steel.',
  'audio': 'Room tone only, no music: castors rolling half an inch on '
           'concrete, the metal tray ringing, a fan running somewhere.',
  'aceita': ['po', 'cubos', 'pote', 'sache', 'creme', 'liquido', 'espuma'],
  'regua_cabe': True,
  'molhado': False},
 {'id': 'carrinho_rattan_tres_niveis',
  'curto': 'Carrinho de rattan de tres niveis',
  'fonte': 'construido',
  'familia': 'outro',
  'ambiente': 'Sunny bohemian bathroom: a three-tier rattan and bamboo '
              'trolley beside the tub loaded with rolled towels and amber '
              'bottles, terracotta floor tile, a macrame hanger on the wall, '
              'all dry.',
  'superficie': 'The middle tier of the rattan trolley: a woven cane '
                'platform inside a bamboo frame at waist height, giving very '
                'slightly under weight; objects rest on the flat woven panel '
                'with rolled towels stacked on the tier below.',
  'camera': 'Phone in one hand at hip height tilted down forty-five degrees, '
            'the operator standing close so the tier fills the frame; loose '
            'handheld with a slow sway.',
  'enquadramento': 'Vertical 9:16. The woven tier and its bamboo rim take '
                   'the lower two thirds, the top tier clipped at the very '
                   'top, terracotta floor showing in one corner. Ceiling and '
                   'body are cut.',
  'luz': 'Warm late morning sun through a bamboo blind, striped shadows '
         'falling across the weave and over the objects.',
  'audio': 'Room tone only, no music: cane creaking, the blind tapping the '
           'window, birds outside.',
  'aceita': ['po', 'cubos', 'pote', 'sache', 'creme', 'espuma'],
  'regua_cabe': False,
  'molhado': False},
 {'id': 'banco_teca_ripado',
  'curto': 'Banco ripado de teca',
  'fonte': 'construido',
  'familia': 'outro',
  'ambiente': 'Home spa bathroom kept dry: a long slatted teak bench along '
              'the wall, rolled towels underneath, pebble-mosaic floor, a '
              'closed steam room door with fogged glass at the far end.',
  'superficie': 'The slatted teak bench top: seven oiled slats with '
                'finger-wide gaps between them at knee height, screwed onto '
                'a dark frame; objects stand across two slats each and the '
                'gaps read black beneath them.',
  'camera': 'Crouching by the bench, phone in one hand almost at bench '
            'height tilted down forty degrees; slow handheld drift '
            'travelling along the length of the slats.',
  'enquadramento': 'Vertical 9:16. The slats run diagonally through the '
                   'lower half with the gaps clear, wall and rolled towels '
                   'behind, the far door soft at the top. Floor and body are '
                   'cut.',
  'luz': 'Warm indirect light from a cove above the wall, the teak glowing '
         'amber, black bars of shadow in every gap.',
  'audio': 'Room tone only, no music: dry warm-room silence, wood ticking, a '
           'distant extractor turning over.',
  'aceita': ['po', 'cubos', 'pote', 'sache', 'creme', 'espuma'],
  'regua_cabe': False,
  'molhado': False},
 {'id': 'banqueta_dobravel_plastico',
  'curto': 'Banquinho plastico dobravel, altura do chao',
  'fonte': 'construido',
  'familia': 'outro',
  'ambiente': "Plain family bathroom: a child's white folding plastic step "
              'stool opened on the floor next to the tub, non-slip ridges on '
              'the tread, a bath mat beside it, floor tile grouted and dry.',
  'superficie': 'The top tread of the white folding plastic step stool: a '
                'small ribbed rectangle barely a foot across, six inches off '
                'the floor, non-slip ridges running side to side; objects '
                'are crowded onto it edge to edge.',
  'camera': 'Kneeling on the tile, phone held very low in one hand near '
            'floor level, tilted down only twenty-five degrees so the stool '
            'reads big against the room; heavy handheld presence.',
  'enquadramento': 'Vertical 9:16. The ribbed tread fills the lower half '
                   "from this low angle, the tub's white skirt and floor "
                   'tile behind, the ceiling out of frame. Any body is cut.',
  'luz': 'Bright flat ceiling light from far above, the plastic reading '
         'clinical white, small hard shadows caught in the ribs.',
  'audio': 'Room tone only, no music: plastic flexing and clicking, knees '
           'shifting on tile, a tap dripping out of frame.',
  'aceita': ['po', 'pote', 'sache', 'creme'],
  'regua_cabe': False,
  'molhado': False},
 {'id': 'caixote_madeira_virado',
  'curto': 'Caixote de madeira virado como mesinha',
  'fonte': 'construido',
  'familia': 'outro',
  'ambiente': 'Cabin bathroom with plank walls: an old wooden crate turned '
              'on its end as a side table by the tub, stencilled letters '
              'faded on its side, a candle stub and folded flannel on top, '
              'dry.',
  'superficie': 'The upturned base of the old wooden crate serving as a '
                'tabletop: rough pine boards with a gap between two of them '
                'and a nail head standing proud, at knee height; objects sit '
                'on the raw boards, one crate leg visible below.',
  'camera': 'Sitting on the tub edge, phone in one hand at chest height '
            'looking down fifty-five degrees onto the crate; the frame '
            'breathes with the operator, no zoom.',
  'enquadramento': 'Vertical 9:16. The crate top fills the middle of the '
                   "frame with the plank wall behind, the tub's white edge "
                   'at left. Floor, ceiling and any body are cut.',
  'luz': 'A single warm bulb on a cord above, strong falloff, the plank wall '
         'dropping into deep brown shadow.',
  'audio': 'Room tone only, no music: crickets and wind outside the cabin, '
           'wood knocking, a floorboard settling.',
  'aceita': ['po', 'cubos', 'pote', 'sache', 'creme', 'espuma'],
  'regua_cabe': False,
  'molhado': False},
 {'id': 'comoda_nogueira_vintage',
  'curto': 'Comoda de nogueira usada como movel de banheiro',
  'fonte': 'construido',
  'familia': 'outro',
  'ambiente': 'Bathroom of an old house furnished with an antique dark '
              'walnut dresser instead of a vanity: brass drop pulls, a lamp '
              'beside it, a runner cloth, the wood polished and dry.',
  'superficie': 'The polished dark walnut dresser top: a deep, near-black '
                'timber surface with a faint water ring and a brass keyhole '
                'plate at the front edge, hip height; objects stand on the '
                'bare polished wood, clear of the runner cloth.',
  'camera': 'Phone propped against the dresser mirror at chest height, '
            'angled down thirty degrees; a locked-off frame with hands '
            'entering from the right and never a reframe.',
  'enquadramento': 'Vertical 9:16. The dark dresser top fills the lower two '
                   'thirds, a brass pull and the drawer front clipped at the '
                   'bottom, wall and mirror edge above. Ceiling and body are '
                   'cut.',
  'luz': 'Warm table lamp at frame left, light pooled on the walnut, the '
         'corners of the frame dropping into brown darkness.',
  'audio': 'Room tone only, no music: a heavy drawer sliding once, an old '
           'clock in the hall, rain against a distant window.',
  'aceita': ['po', 'cubos', 'pote', 'sache', 'creme', 'liquido', 'espuma'],
  'regua_cabe': True,
  'molhado': False},
 {'id': 'mesa_lateral_vidro_ferro',
  'curto': 'Mesinha de vidro com base de ferro',
  'fonte': 'construido',
  'familia': 'outro',
  'ambiente': 'Bathroom in a modern flat: a small round side table with a '
              'clear glass top on a thin black iron frame, standing on pale '
              'herringbone floor beside a freestanding tub, dry and '
              'uncluttered.',
  'superficie': 'The clear glass top of the small round iron side table: a '
                'polished disc with a bevelled edge at waist height, the '
                'black iron ring frame and the floor visible straight '
                'through it; objects sit on glass and throw their shadows '
                'onto the floor below.',
  'camera': 'Phone held one-handed at chest height, tilted down forty-five '
            'degrees onto the glass; the operator circles a few inches '
            'during the take so the reflection slides across the top.',
  'enquadramento': 'Vertical 9:16. The glass disc fills the middle of the '
                   'frame with herringbone floor showing through it, the '
                   "tub's curve in the top corner. Ceiling and body are cut.",
  'luz': 'Bright diffuse daylight from a skylight overhead, clean '
         'reflections in the glass and sharp doubled shadows on the floor '
         'beneath.',
  'audio': 'Room tone only, no music: glass ringing crisply when touched, '
           'the iron frame creaking, rain on the skylight.',
  'aceita': ['po', 'cubos', 'pote', 'sache', 'creme', 'liquido', 'espuma'],
  'regua_cabe': True,
  'molhado': False},
 {'id': 'bancada_inox_lavanderia',
  'curto': 'Bancada de aco inox do canto de lavanderia',
  'fonte': 'construido',
  'familia': 'outro',
  'ambiente': 'Utility corner off the bathroom: a brushed stainless steel '
              'counter over a deep laundry sink, taps shut and the steel '
              'dry, a mop hanging, painted breeze-block wall, harsh and '
              'functional.',
  'superficie': 'The brushed stainless steel counter to the LEFT of the deep '
                'laundry sink: a dry span of grained metal with a raised '
                'rolled edge in front and fine scratches in the brushing, '
                'hip height; objects sit straight on the steel.',
  'camera': 'Standing at the counter, phone in one hand at chest height '
            'tilted down forty-five degrees; the steel throws the working '
            'hand back as a soft reflection, small handheld drift.',
  'enquadramento': 'Vertical 9:16. The steel span fills the lower two thirds '
                   "with its rolled edge in front, the sink's dark opening "
                   'at right, block wall above. Floor and body are cut.',
  'luz': 'Cold overhead fluorescent, long linear reflections streaking along '
         'the brushed grain, unforgiving and flat.',
  'audio': 'Room tone only, no music: a fluorescent ballast buzzing, metal '
           'knocking on steel, water gurgling in the drain trap.',
  'aceita': ['po', 'cubos', 'pote', 'sache', 'creme', 'liquido', 'espuma'],
  'regua_cabe': True,
  'molhado': False},
 {'id': 'tabua_acougueiro_carrinho',
  'curto': 'Carrinho com tampo de tabua de acougueiro',
  'fonte': 'construido',
  'familia': 'outro',
  'ambiente': 'Wide bathroom with a rolling kitchen island parked in it as '
              'storage: a thick maple butcher-block top over a painted steel '
              'frame, towels on the lower rack, castors locked, floor dry, '
              'with the glass visible in frame.',
  'superficie': 'The thick end-grain maple butcher-block top of the rolling '
                'island: a chequerboard of oiled end-grain blocks with a '
                'shallow juice groove routed around it at hip height; '
                "objects stand inside that groove's border on bare block.",
  'camera': 'Phone in one hand at chest height tilted down forty-five '
            'degrees, the operator standing at one corner so the groove runs '
            'diagonally through the frame; slow handheld push-in.',
  'enquadramento': 'Vertical 9:16. The end-grain chequerboard and the routed '
                   'groove fill the lower two thirds, the painted frame edge '
                   'below, bathroom wall and a mirror behind. Ceiling and '
                   'body are cut.',
  'luz': 'Warm pendant directly above, a bright oval on the block and heavy '
         'shadow at the corners of the frame.',
  'audio': 'Room tone only, no music: the solid dull knock of glass on thick '
           'wood, a castor easing, house pipes ticking.',
  'aceita': ['po', 'cubos', 'pote', 'sache', 'creme', 'liquido', 'espuma'],
  'regua_cabe': False,
  'molhado': False},
 {'id': 'banquinho_metal_ordenha',
  'curto': 'Banquinho de metal de tres pernas',
  'fonte': 'construido',
  'familia': 'outro',
  'ambiente': 'Half-renovated farmhouse bathroom: a three-legged galvanised '
              'metal milking stool standing on bare plywood subfloor, a '
              'claw-foot tub behind with taps shut, plaster torn back to the '
              'lath on one wall.',
  'superficie': 'The round galvanised metal seat of the three-legged milking '
                'stool: a dished disc about a foot across with a rolled rim '
                'and a scuffed grey sheen, low at shin height; objects are '
                'grouped in the dish with the rim curling up around them.',
  'camera': 'Kneeling on the plywood, phone in one hand held just above the '
            'stool, tilted down sixty degrees; the operator steadies an '
            'elbow on one knee, so the drift is slow and heavy.',
  'enquadramento': 'Vertical 9:16. The dished metal disc fills the centre of '
                   'the frame, one leg and the plywood grain below, the '
                   'claw-foot tub soft behind. Ceiling and any body are cut.',
  'luz': 'A raw work light on a stand at frame left, hard and white, the '
         'galvanised dish flaring at one edge while the torn plaster stays '
         'deep in shadow.',
  'audio': 'Room tone only, no music: metal ringing hollow under every '
           'touch, plywood creaking, a power drill running two rooms away.',
  'aceita': ['po', 'pote', 'sache', 'creme', 'espuma'],
  'regua_cabe': False,
  'molhado': False},
 {'id': 'console_base_maquina_costura',
  'curto': 'Console feito de base de maquina de costura',
  'fonte': 'construido',
  'familia': 'outro',
  'ambiente': 'Bathroom of a restored townhouse: an old cast-iron '
              'sewing-machine treadle base fitted with a stained oak top and '
              'used as a console, ornate ironwork below, dark green wall, '
              'dry and tidy.',
  'superficie': 'The stained dark-oak top screwed onto the cast-iron '
                'sewing-machine base: a narrow rectangular plank at hip '
                "height with the machine's two old screw holes still open "
                'near the back; objects stand between those holes on the '
                'flat oak.',
  'camera': 'Phone braced against the wall at chest height, tilted down '
            'thirty-five degrees and fixed; the ironwork stays sharp below '
            'and the hands enter the frame from the left.',
  'enquadramento': 'Vertical 9:16. The oak plank crosses the middle third, '
                   'the iron treadle scrollwork visible underneath, dark '
                   'green wall filling the top. Floor and any body are cut.',
  'luz': 'Warm picture light on the wall above throwing a narrow beam down '
         'the plank, the ironwork below reading almost black.',
  'audio': 'Room tone only, no music: an old house creaking, iron ringing '
           'dully when knocked, muffled street noise through closed '
           'shutters.',
  'aceita': ['po', 'cubos', 'pote', 'sache', 'creme', 'liquido', 'espuma'],
  'regua_cabe': True,
  'molhado': False},
 {'id': 'sauna_banco_baixo_cedro',
  'curto': 'banco baixo de cedro na sauna',
  'fonte': 'construido',
  'familia': 'sauna',
  'ambiente': 'Small cedar sauna, horizontal slat walls darkened by heat, a '
              'squat iron stove in the corner holding a mound of grey '
              'stones, heat shimmer rising off them.',
  'superficie': 'the second slat of the lower cedar bench — a single '
                'four-inch board with the grain running left to right and a '
                'dark sweat stain where it meets the wall',
  'camera': 'POV of a man seated on the upper bench, phone held low in his '
            'left hand between his own knees, looking down past his shin at '
            'the bench below',
  'enquadramento': 'Vertical 9:16. The lower bench runs diagonally across '
                   'the bottom half; the stove stones sit blurred in the top '
                   'right. Cropped: ceiling, door, any face.',
  'luz': 'One shielded amber lamp behind the backrest, warm and low '
         'contrast, long soft shadows falling down the slats',
  'audio': 'Stones ticking as they cool, a slow exhale, timber creaking. No '
           'music.',
  'aceita': ['pote', 'creme', 'sache', 'po', 'espuma'],
  'regua_cabe': False,
  'molhado': False},
 {'id': 'sauna_prateleira_pedra_sabao',
  'curto': 'prateleira de pedra-sabao atras do banco alto',
  'fonte': 'construido',
  'familia': 'sauna',
  'ambiente': 'Hotel sauna lined in dark slate on three sides, a long cedar '
              'upper bench, a wooden bucket and ladle on the floor, no '
              'window, the stove out of frame.',
  'superficie': 'the soapstone ledge running along the wall behind the upper '
                'bench — a six-inch shelf of matte grey-green stone at '
                'shoulder height, cool to the touch, one pale ring where a '
                'cup has stood',
  'camera': 'POV of a man standing in the middle of the room, phone in his '
            'right hand at chest height, aimed level at the stone ledge '
            'rather than tilted down',
  'enquadramento': 'Vertical 9:16. The ledge cuts across the frame at the '
                   'two-thirds line, dark slate above it, empty bench below. '
                   'Cropped: the stove, the floor, the door.',
  'luz': 'A narrow strip of cold daylight through smoked glass near the '
         'ceiling set against the warm cedar below — two colour temperatures '
         'in one frame',
  'audio': 'Dead heavy room tone, one drip into the wooden bucket, plumbing '
           'knocking inside the wall. No music.',
  'aceita': ['pote', 'creme', 'sache', 'po', 'espuma'],
  'regua_cabe': True,
  'molhado': False},
 {'id': 'sauna_barril_tampa_balde',
  'curto': 'tampa do balde na sauna barril',
  'fonte': 'construido',
  'familia': 'sauna',
  'ambiente': 'Barrel sauna in a snowed-in backyard, curved cedar staves '
              'arcing overhead, a porthole window fogged solid white, a '
              'black rubber mat on the curved floor.',
  'superficie': 'the upturned flat lid of the cedar water bucket set on the '
                'bench as a small round table — a ten-inch disc of pale wood '
                'banded in black iron, still beaded with water',
  'camera': 'POV of a man sitting cross-legged on the low bench, phone '
            'propped against his own thigh, angled steeply down at the '
            'bucket lid a foot in front of him',
  'enquadramento': 'Vertical 9:16. The round lid fills the centre third, '
                   'staves arc across the top of the frame, the porthole '
                   'glows white upper left. Cropped: his body, the door, the '
                   'stove.',
  'luz': 'Flat white bounce off the snow coming through the porthole, no '
         'lamp lit, the edges of the frame going slightly blue',
  'audio': 'Wood creaking as it expands, muffled snow-silence outside, a '
           'faint hiss off the stove. No music.',
  'aceita': ['pote', 'creme', 'sache', 'po'],
  'regua_cabe': False,
  'molhado': True},
 {'id': 'jacuzzi_nicho_acrilico',
  'curto': 'nicho moldado do acrilico da jacuzzi',
  'fonte': 'construido',
  'familia': 'jacuzzi',
  'ambiente': 'Indoor hot tub room, a five-seat acrylic spa sunk into a '
              'tiled platform, jets running hard, the water pale turquoise '
              'and churning, condensation running down the window.',
  'superficie': 'the moulded drink recess pressed into the acrylic shell rim '
                '— a flat oval pad the size of a dinner plate, set between '
                'two headrests, dry and above the waterline',
  'camera': 'POV of a man sitting in the tub with his back against the wall, '
            'phone held just clear of the water in his right hand, angled up '
            'slightly at the rim beside his shoulder',
  'enquadramento': 'Vertical 9:16. The moulded recess sits centre-frame in '
                   'the lower third, churning water at the bottom edge, the '
                   'fogged window across the top. Cropped: his chest, the '
                   'far side of the tub.',
  'luz': 'Underwater LED throwing moving turquoise ripples up onto the rim '
         'and the wall, one warm downlight from the ceiling above',
  'audio': 'Jets churning, water slapping acrylic, the pump humming under '
           'the floor. No music.',
  'aceita': ['pote', 'creme', 'sache', 'po', 'espuma'],
  'regua_cabe': False,
  'molhado': True},
 {'id': 'jacuzzi_coroa_staves_cedro',
  'curto': 'coroa de cedro do ofuro no deck da montanha',
  'fonte': 'construido',
  'familia': 'jacuzzi',
  'ambiente': 'Round cedar hot tub on a mountain deck at dusk, steam pouring '
              'off the surface, pine trunks crowding in behind, packed snow '
              'still banked against the staves.',
  'superficie': 'the flat crown board that caps the cedar staves — a '
                'five-inch band of weathered grey wood circling the whole '
                'tub, worn smooth and darkened where hands have gripped it',
  'camera': 'POV of a man standing in the tub with water at his waist, phone '
            'in his left hand held out past the crown board, looking down at '
            'it at about sixty degrees',
  'enquadramento': 'Vertical 9:16. The crown board curves across the frame '
                   'as a shallow arc at mid height, steam and dark water '
                   'below, pine trunks and dusk sky above. Cropped: his '
                   'torso, the deck.',
  'luz': 'Last blue daylight overhead plus a single warm bulb on the deck '
         'post cutting a hard yellow edge along the near side of the wood',
  'audio': 'Water lapping the staves, wind through pine needles, a dog '
           'barking far downhill. No music.',
  'aceita': ['pote', 'creme', 'sache', 'espuma'],
  'regua_cabe': False,
  'molhado': True},
 {'id': 'jacuzzi_bandeja_bambu',
  'curto': 'bandeja de bambu atravessada na spa',
  'fonte': 'construido',
  'familia': 'jacuzzi',
  'ambiente': 'Small plug-in backyard spa on a concrete pad, the vinyl cover '
              'folded back over the far half, water still and clear, '
              'chain-link fence and a garage wall behind it.',
  'superficie': 'a slatted bamboo bath caddy bridging the spa from rim to '
                'rim — a tray a foot wide with a raised lip on each side, '
                'sitting dead level over the water in front of him',
  'camera': 'POV of a man sitting in the spa, phone braced against the far '
            'rim so both of his hands stay free, framing the tray head-on at '
            'chest height',
  'enquadramento': 'Vertical 9:16. The tray runs edge to edge across the '
                   'middle of the frame, still water beneath it, folded '
                   'vinyl cover and fence above. Cropped: him entirely, the '
                   'yard, the sky.',
  'luz': 'Flat overcast afternoon with no shadows at all, a faint green cast '
         'bouncing off the fence and the garage paint',
  'audio': 'A low filter hum, water settling, traffic two streets over. No '
           'music.',
  'aceita': ['pote', 'creme', 'sache', 'po', 'cubos', 'liquido', 'espuma'],
  'regua_cabe': False,
  'molhado': False},
 {'id': 'praia_braco_espreguicadeira',
  'curto': 'braco de teca da espreguicadeira',
  'fonte': 'construido',
  'familia': 'praia',
  'ambiente': 'Private beach at mid morning, two teak loungers standing on '
              'packed wet sand near the tideline, a rolled white towel at '
              'the foot of one, the sea flat and glassy.',
  'superficie': 'the wide slatted teak armrest of the lounger — three '
                'parallel boards forming a flat pad eight inches across, '
                'salt-bleached grey, sand grains caught in the gaps between '
                'them',
  'camera': 'POV of a man lying back on the lounger, phone in his right hand '
            'held above his own lap, angled down and sideways at the armrest '
            'beside his hip',
  'enquadramento': 'Vertical 9:16. The armrest runs down the right third in '
                   'perspective, wet sand and flat sea filling the left. '
                   'Cropped: his legs, his face, the second lounger.',
  'luz': 'Hard high sun, short black shadows under every object, glare '
         'kicking back off the wet sand',
  'audio': 'Small waves collapsing, gulls, a rope tapping against a pole. No '
           'music.',
  'aceita': ['pote', 'creme', 'sache', 'espuma'],
  'regua_cabe': False,
  'molhado': False},
 {'id': 'praia_mesinha_dobravel_areia',
  'curto': 'mesinha dobravel fincada na areia',
  'fonte': 'construido',
  'familia': 'praia',
  'ambiente': 'Wide empty beach late in the day, dry pale sand ridged by '
              'wind, a striped windbreak staked at an angle, an aluminium '
              'folding side table sunk unevenly into the sand.',
  'superficie': 'the perforated aluminium top of the folding side table — a '
                'fourteen-inch square of white-painted metal punched with a '
                'grid of drain holes, one leg sunk lower so the top tilts',
  'camera': 'POV of a man kneeling in the sand beside the table, phone in '
            'his left hand at knee height, looking down at the tabletop at '
            'about fifty degrees',
  'enquadramento': 'Vertical 9:16. The tilted square sits in the middle of '
                   'the frame with sand all around it, windbreak stripes '
                   'crossing the top edge. Cropped: the sea, the sky, his '
                   'knees.',
  'luz': 'Low golden sun raking in from the left, every ridge of sand '
         'throwing a long shadow, the painted metal blowing slightly white',
  'audio': 'Wind buffeting fabric, distant surf, sand hissing across the '
           'metal. No music.',
  'aceita': ['pote', 'creme', 'sache', 'cubos', 'espuma'],
  'regua_cabe': True,
  'molhado': False},
 {'id': 'praia_tampa_cooler',
  'curto': 'tampa do cooler ao lado da cadeira de lona',
  'fonte': 'construido',
  'familia': 'praia',
  'ambiente': 'Sheltered cove in the shade of a rock overhang, a battered '
              'blue-and-white cooler standing beside a folding canvas chair, '
              'damp pebbles instead of sand, kelp along the waterline.',
  'superficie': 'the closed lid of the hard cooler used flat as a table — a '
                'scuffed white moulded plastic rectangle with a raised rim '
                'and two recessed cup wells, condensation beaded all over it',
  'camera': 'POV of a man sitting in the canvas chair, phone in his right '
            'hand resting on the chair arm, pointed sideways and slightly '
            'down at the cooler lid',
  'enquadramento': 'Vertical 9:16. The lid occupies the lower two thirds in '
                   'strong perspective, wet pebbles and dark rock overhang '
                   'above. Cropped: his legs, the chair back, the open sea.',
  'luz': 'Deep open shade under the rock with a hot bright strip of sunlit '
         'water burning across the top of the frame',
  'audio': 'Water sucking back through pebbles, an echo off the rock face, a '
           'boat engine far out. No music.',
  'aceita': ['pote', 'creme', 'sache', 'po', 'cubos', 'liquido', 'espuma'],
  'regua_cabe': True,
  'molhado': True},
 {'id': 'rio_laje_granito',
  'curto': 'laje de granito seca na margem',
  'fonte': 'construido',
  'familia': 'ar_livre',
  'ambiente': 'Wide shallow river in late summer, water low, a field of pale '
              'rounded granite exposed on the near bank, dry grass and alder '
              'scrub behind, no path in sight.',
  'superficie': 'a flat table-sized slab of dry pale granite lying level '
                'among the rounded stones — pitted and speckled black on '
                'white, with a hairline crack running corner to corner',
  'camera': 'POV of a man crouched on his heels on the bank, phone in his '
            'right hand at hip height, tilted down at the slab a foot in '
            'front of his boots',
  'enquadramento': 'Vertical 9:16. The slab fills the lower half edge to '
                   'edge, the river runs bright across the middle band, the '
                   'far bank blurs at the top. Cropped: his body, the sky.',
  'luz': 'High overcast, soft and even, the water reading silver-white and '
         'the rock almost colourless',
  'audio': 'River running over stones, one insect close to the mic, wind '
           'through alder. No music.',
  'aceita': ['pote', 'creme', 'sache', 'po', 'cubos', 'espuma'],
  'regua_cabe': True,
  'molhado': False},
 {'id': 'rio_tronco_deriva',
  'curto': 'tronco de deriva encaixado nas pedras',
  'fonte': 'construido',
  'familia': 'ar_livre',
  'ambiente': 'Narrow fast stretch of river in a gorge, a sun-bleached '
              'driftwood log jammed between two boulders above the current, '
              'moss on the shaded faces, spray drifting through.',
  'superficie': 'the sawn end-face of the driftwood log — a pale silver disc '
                'two feet across tipped up toward the sky, the growth rings '
                'raised proud, the wood dry and fibrous under the fingers',
  'camera': 'POV of a man standing on the boulder beside the log, phone in '
            'his left hand at waist height, looking almost straight down at '
            'the cut face',
  'enquadramento': 'Vertical 9:16. The pale disc sits centre-frame ringed by '
                   'dark wet rock, a white ribbon of rapid crossing the '
                   'bottom corner. Cropped: his feet, the gorge walls, the '
                   'horizon.',
  'luz': 'Shafts of direct sun coming through the gorge, hard-edged patches '
         'sliding across the wood, the surrounding rock in deep shade',
  'audio': 'A loud rapid close by, spray hitting stone, one bird call '
           'cutting through. No music.',
  'aceita': ['pote', 'creme', 'sache'],
  'regua_cabe': False,
  'molhado': True},
 {'id': 'rio_patamar_xisto_molhado',
  'curto': 'degrau de xisto molhado rente a agua',
  'fonte': 'construido',
  'familia': 'ar_livre',
  'ambiente': 'Slow bend of a brown river under willows, layered dark shale '
              "stepping down into the water, the top ledge a hand's width "
              'above the surface and constantly rewetted.',
  'superficie': 'the wet shale ledge just above the waterline — a black '
                'shelf two feet wide and as flat as a plank, glossy with '
                'river water and edged with a bright green algae line',
  'camera': 'POV of a man sitting on the shale step above it, phone in his '
            'right hand between his knees, angled down at the wet ledge '
            'below his boots',
  'enquadramento': 'Vertical 9:16. The black ledge crosses the lower third, '
                   'brown water fills the middle, willow leaves hang into '
                   'the top of the frame. Cropped: his legs, the far bank.',
  'luz': 'Dappled green light through willow leaves, moving constantly, the '
         'wet shale throwing back a hard mirror highlight',
  'audio': 'Water slapping the shale, willow leaves moving, a fish rising. '
           'No music.',
  'aceita': ['pote', 'creme', 'sache', 'po', 'espuma'],
  'regua_cabe': True,
  'molhado': True},
 {'id': 'ofuro_borda_cedro',
  'curto': 'borda larga do ofuro de cedro',
  'fonte': 'construido',
  'familia': 'banheira',
  'ambiente': 'Japanese-style cedar soaking tub on a small deck screened by '
              'bamboo, filled to the brim with clear steaming water, a '
              'folded indigo cloth hanging on the screen.',
  'superficie': 'the wide flat cedar rim of the soaking tub — a seven-inch '
                'band of blond wood running all the way round, damp and dark '
                'along the inner edge, dry and pale on the outer',
  'camera': 'POV of a man standing in the tub with water at his hips, phone '
            'in his right hand held out past the rim, looking down at it at '
            'about forty-five degrees',
  'enquadramento': 'Vertical 9:16. The rim runs as a broad diagonal from '
                   'bottom left to right, steaming water beneath, bamboo '
                   'screen filling the top. Cropped: his torso, the deck '
                   'boards.',
  'luz': 'Early morning sun striped by the bamboo screen, alternating hot '
         'bars and cool shade laid across the rim',
  'audio': 'Water settling, bamboo knocking in the wind, birds waking up. No '
           'music.',
  'aceita': ['pote', 'creme', 'sache', 'po', 'espuma'],
  'regua_cabe': False,
  'molhado': True},
 {'id': 'ofuro_banquinho_degrau_cobre',
  'curto': 'banquinho-degrau ao lado da tina de cobre',
  'fonte': 'construido',
  'familia': 'banheira',
  'ambiente': 'Copper soaking tub standing free on gravel in a walled '
              'garden, the metal gone brown-green with patina, the water '
              'steaming, ivy swallowing the brick wall behind.',
  'superficie': 'the upper tread of the two-step wooden stool set against '
                'the tub — a slab of oiled oak a foot square, scuffed pale '
                'in the middle where feet have climbed it, one corner '
                'rounded off',
  'camera': 'POV of a man standing on the gravel beside the tub, phone in '
            'his left hand at chest height, looking steeply down at the '
            'stool tread by his knee',
  'enquadramento': 'Vertical 9:16. The tread sits low centre, the curved '
                   'copper flank fills the right third, gravel and ivy '
                   'across the top. Cropped: his body, the tub rim, the wall '
                   'top.',
  'luz': 'Bright overcast, the copper glowing a dull orange as the only warm '
         'thing in an otherwise grey-green frame',
  'audio': 'Steam hissing off hot metal, gravel shifting underfoot, a wood '
           'pigeon. No music.',
  'aceita': ['pote', 'creme', 'sache', 'po', 'cubos', 'espuma'],
  'regua_cabe': False,
  'molhado': False},
 {'id': 'ofuro_bancada_ardosia_deserto',
  'curto': 'bancada de ardosia atras da tina de pedra',
  'fonte': 'construido',
  'familia': 'banheira',
  'ambiente': 'Soaking basin carved from a single granite block on the '
              'terrace of a desert house, a service counter built into the '
              'wall behind it, agaves standing in gravel beyond.',
  'superficie': 'the honed slate service counter built along the wall behind '
                'the basin — a matte blue-black slab at hip height, eighteen '
                'inches deep, with a shallow drip channel cut along its '
                'front edge',
  'camera': 'POV of a man standing at the counter with the basin behind him, '
            'phone in his right hand held high and angled down at the slate, '
            'his own shadow falling across it',
  'enquadramento': 'Vertical 9:16. The slate counter fills the lower two '
                   'thirds as a flat dark field, the wall and one agave '
                   'blade at the top. Cropped: the basin, his arms above the '
                   'elbow.',
  'luz': 'Hard late-afternoon desert sun from the left, one crisp shadow '
         'edge cutting the slate on the diagonal',
  'audio': 'Dry wind, one cicada, water trickling into the basin behind him. '
           'No music.',
  'aceita': ['pote', 'creme', 'sache', 'po', 'cubos', 'liquido', 'espuma'],
  'regua_cabe': True,
  'molhado': False},
 {'id': 'piscina_pedra_coping',
  'curto': 'pedra de borda da piscina',
  'fonte': 'construido',
  'familia': 'ar_livre',
  'ambiente': 'Rectangular lap pool in a fenced suburban yard, the water '
              'very still and blue, travertine coping set around the edge, a '
              'skimmer lid and a coiled vacuum hose nearby.',
  'superficie': 'one travertine coping stone at the pool edge — a cream '
                'limestone block twelve by twenty-four inches with a rounded '
                'bullnose lip, pitted with natural holes, dry on top and '
                'dark along the water side',
  'camera': 'POV of a man sitting on the coping with his feet in the water, '
            'phone in his right hand beside his thigh, angled down at the '
            'stone next to him',
  'enquadramento': 'Vertical 9:16. The coping stone runs across the lower '
                   'half, pool water fills the upper half, the fence line '
                   'just enters the top. Cropped: his legs, the far end, the '
                   'house.',
  'luz': 'Mid-morning sun with caustic ripple patterns thrown up from the '
         'water onto the stone, moving without stopping',
  'audio': 'The skimmer sucking, the pump humming, a lawnmower two yards '
           'over. No music.',
  'aceita': ['pote', 'creme', 'sache', 'po', 'cubos', 'liquido', 'espuma'],
  'regua_cabe': True,
  'molhado': False},
 {'id': 'piscina_mureta_floreira_motel',
  'curto': 'topo da mureta de concreto da floreira',
  'fonte': 'construido',
  'familia': 'ar_livre',
  'ambiente': 'Motel pool deck at night, a kidney-shaped pool lit from '
              'inside, a low poured-concrete planter wall along one side, '
              'dusty palms and a chain-link gate beyond it.',
  'superficie': 'the flat cap of the concrete planter wall — a ten-inch-wide '
                'band of rough grey poured concrete at waist height, chipped '
                'along one edge, dry soil spilled across it from the '
                'planting',
  'camera': 'POV of a man standing at the wall with the pool at his back, '
            'phone in his left hand at chest height, aimed level along the '
            'cap so it runs away in perspective',
  'enquadramento': 'Vertical 9:16. The wall cap runs from the bottom of the '
                   'frame into the distance up the centre, pool glow along '
                   'the left edge, palms black at the top. Cropped: his '
                   'body, the rooms.',
  'luz': 'Only the underwater pool light and one sodium lamp on a pole — '
         'turquoise from below, orange from above, deep black in between',
  'audio': 'The pool filter, moths hitting the lamp, a highway a mile off. '
           'No music.',
  'aceita': ['pote', 'creme', 'sache', 'po', 'cubos', 'espuma'],
  'regua_cabe': True,
  'molhado': False},
 {'id': 'academia_banco_corredor',
  'curto': 'banco de ripas no corredor de armarios',
  'fonte': 'construido',
  'familia': 'academia',
  'ambiente': 'Gym locker aisle, two rows of dented grey steel lockers '
              'facing each other, a slatted bench bolted between them, '
              'rubber floor tiles, an open gym bag three lockers down.',
  'superficie': 'the slatted hardwood bench between the locker rows — four '
                'varnished maple boards with finger-wide gaps between them, '
                'bolted to a steel frame and worn shiny down the middle',
  'camera': 'POV of a man sitting on the bench, phone in his right hand held '
            'out over his own knee, looking straight down at the boards '
            'beside his hip',
  'enquadramento': 'Vertical 9:16. The bench boards run up the frame in '
                   'perspective, locker doors closing in on both sides, '
                   'rubber floor at the bottom. Cropped: his body, the '
                   'ceiling, the aisle end.',
  'luz': 'A fluorescent strip directly overhead, hard top light, everything '
         'faintly green, black shadows dropping through the bench gaps',
  'audio': 'A locker door slamming, a hand dryer starting up, weights '
           'clanging through the wall. No music.',
  'aceita': ['pote', 'creme', 'sache', 'po', 'cubos', 'liquido', 'espuma'],
  'regua_cabe': False,
  'molhado': False},
 {'id': 'academia_bancada_pias',
  'curto': 'bancada molhada das pias do vestiario',
  'fonte': 'construido',
  'familia': 'academia',
  'ambiente': 'Gym washroom, four rectangular basins set in one continuous '
              'counter, a long mirror above with a hand dryer between, white '
              'subway tile, a folded wet-floor sign in the corner.',
  'superficie': 'the counter top to the right of the last basin — a slab of '
                'speckled grey solid-surface material with standing water '
                'pooled where it dips, a paper towel gone translucent stuck '
                'near the edge',
  'camera': 'POV of a man standing at the counter, phone in his left hand at '
            'chest height, tilted down about forty degrees so the mirror '
            'stays out of the shot',
  'enquadramento': 'Vertical 9:16. The wet counter fills the lower two '
                   'thirds, the chrome tap and the bottom edge of the mirror '
                   'frame the top. Cropped: his reflection, his torso, the '
                   'other basins.',
  'luz': 'Cool white downlights over the mirror, the wet counter throwing a '
         'broad specular sheet straight back at the lens',
  'audio': 'A tap dripping, the hand dryer roaring then cutting out, '
           'everything echoing off tile. No music.',
  'aceita': ['pote', 'creme', 'sache', 'po', 'liquido', 'espuma'],
  'regua_cabe': True,
  'molhado': True},
 {'id': 'academia_assento_box_chuveiro',
  'curto': 'assento embutido do chuveiro da academia',
  'fonte': 'construido',
  'familia': 'academia',
  'ambiente': 'Gym shower stall, waist-high tiled divider walls, an '
              'institutional push-button head running, cheap white tile with '
              'dark grout, a plastic curtain drawn halfway across.',
  'superficie': 'the built-in tiled shower seat in the corner of the stall — '
                'a bench-shaped ledge of the same white tile, fifteen inches '
                'square, sloped a couple of degrees to drain and running '
                'with water',
  'camera': 'POV of a man standing under the running head, phone in his '
            'right hand held down at hip height, angled steeply at the tiled '
            'seat in the corner',
  'enquadramento': 'Vertical 9:16. The tiled seat occupies the lower right, '
                   'the divider wall and the running head cross the upper '
                   'left. Cropped: his body, the curtain rail, the drain.',
  'luz': 'Flat wet-room ceiling light coming through steam, no shadow '
         'anywhere, the whole frame slightly blown out',
  'audio': 'Shower hitting tile, water gulping in the drain, a voice echoing '
           'from another stall. No music.',
  'aceita': ['pote', 'creme', 'sache', 'espuma'],
  'regua_cabe': True,
  'molhado': True},
 {'id': 'trailer_mesa_dinete',
  'curto': 'mesa da dinete do trailer',
  'fonte': 'construido',
  'familia': 'outro',
  'ambiente': 'Inside a vintage aluminium travel trailer parked in scrub, '
              'curved riveted walls, a dinette of two facing benches in '
              'brown vinyl, the window crank open a few turns.',
  'superficie': 'the fold-down dinette table — a rectangle of pale grey '
                'laminate edged in aluminium T-trim with a brown burn ring '
                'near one corner, carried on a single chrome pedestal',
  'camera': 'POV of a man sitting on one dinette bench, phone in his right '
            'hand held above the table, looking down at it at about '
            'fifty-five degrees',
  'enquadramento': 'Vertical 9:16. The laminate top fills the middle of the '
                   'frame, the curved riveted wall and window running up the '
                   'right side. Cropped: the opposite bench, the floor, his '
                   'lap.',
  'luz': 'Desert daylight through the small window at a low angle, one hot '
         'rectangle of sun laid on the laminate, everything else in dim '
         'interior shadow',
  'audio': 'Wind pushing on aluminium, a loose cabinet latch ticking, a fly '
           'working the window. No music.',
  'aceita': ['pote', 'creme', 'sache', 'po', 'cubos', 'liquido', 'espuma'],
  'regua_cabe': True,
  'molhado': False},
 {'id': 'trailer_escorredor_pia_inox',
  'curto': 'escorredor da pia de inox do motorhome',
  'fonte': 'construido',
  'familia': 'pia',
  'ambiente': 'Galley of a small camper van, a two-burner hob under a glass '
              'lid, a tiny stainless sink with a folding tap, the water pump '
              'switch showing a red light, thin plywood cabinetry.',
  'superficie': 'the pressed stainless drainboard beside the camper sink — a '
                'ribbed panel eight by ten inches stamped with drain '
                'channels running toward the bowl, water still standing in '
                'the grooves',
  'camera': "POV of a man standing in the van's narrow aisle, phone in his "
            'left hand at chest height, tilted down at the drainboard a foot '
            'below him',
  'enquadramento': 'Vertical 9:16. The ribbed steel fills the lower half, '
                   'the folded tap and the hob lid crossing the top. '
                   'Cropped: the cabinets, his body, the van door.',
  'luz': 'One warm LED strip under the overhead locker, close and '
         'directional, the ribs of the drainboard casting parallel shadow '
         'lines',
  'audio': 'The water pump kicking in and shutting off, rain on the van '
           'roof, a fridge cycling. No music.',
  'aceita': ['pote', 'creme', 'sache', 'po', 'liquido', 'espuma'],
  'regua_cabe': True,
  'molhado': True},
 {'id': 'trailer_prateleira_box_fibra',
  'curto': 'prateleira moldada do chuveirinho do trailer',
  'fonte': 'construido',
  'familia': 'chuveiro',
  'ambiente': 'Cramped RV wet bath, moulded cream fibreglass on all four '
              'sides, a handheld shower on a slide bar, a plastic skylight '
              'overhead, a folding door that never quite shuts.',
  'superficie': 'the moulded corner shelf pressed into the fibreglass shower '
                'wall — a small triangular ledge with a raised lip and two '
                'drain slots, at chest height, streaked with dried water '
                'spots',
  'camera': 'POV of a man standing in the wet bath, phone held close to his '
            'chest in his right hand because there is no room to pull back, '
            'aimed almost level at the corner shelf',
  'enquadramento': 'Vertical 9:16. The triangular shelf sits centre right, '
                   'cream fibreglass filling everything else, the skylight '
                   'glowing at the very top. Cropped: his body, the door, '
                   'the floor.',
  'luz': 'Grey-white daylight coming straight down through the plastic '
         'skylight, shadowless and faintly yellow on the cream walls',
  'audio': 'The handheld shower dribbling, the flexible hose knocking the '
           'wall, rain on the skylight. No music.',
  'aceita': ['pote', 'creme', 'sache', 'espuma'],
  'regua_cabe': False,
  'molhado': True},
 {'id': 'barco_amurada_teca',
  'curto': 'borda de teca envernizada da amurada',
  'fonte': 'construido',
  'familia': 'outro',
  'ambiente': 'Small varnished sailing boat at anchor in a flat calm bay, '
              'sails furled, a coiled line on deck, the mast shadow lying '
              'across the cockpit, other moorings far off.',
  'superficie': 'the varnished teak cap along the cockpit coaming — a '
                'four-inch band of honey-coloured wood under many coats of '
                'gloss, the seams black with old caulk, hot from the sun',
  'camera': 'POV of a man sitting in the cockpit, phone in his left hand '
            'resting on his thigh, angled up slightly at the wooden cap '
            'beside his shoulder',
  'enquadramento': 'Vertical 9:16. The cap runs as a bright diagonal from '
                   'lower left to upper right, flat bay water beyond it, the '
                   'boom crossing the top corner. Cropped: his body, the '
                   'mast.',
  'luz': 'Full midday sun, the varnish throwing a long white specular '
         'streak, reflected light bouncing up off the water underneath',
  'audio': 'Halyards tapping the mast, water slapping the hull, one gull. No '
           'music.',
  'aceita': ['pote', 'creme', 'sache'],
  'regua_cabe': False,
  'molhado': False},
 {'id': 'barco_mesa_cartas_cabine',
  'curto': 'mesa de cartas na cabine abaixo do convés',
  'fonte': 'construido',
  'familia': 'outro',
  'ambiente': 'Below deck in a small cabin cruiser, dark mahogany joinery '
              'everywhere, a folded paper chart and brass dividers, a '
              'portlight throwing moving waterline light on the ceiling.',
  'superficie': 'the hinged chart table — a rectangle of dark varnished '
                'mahogany with a raised fiddle rail on three sides to stop '
                'things sliding, a long brass hinge along the back edge',
  'camera': 'POV of a man sitting at the chart table, phone in his right '
            'hand held above it, looking straight down at the wood with his '
            'own shadow at the edge of frame',
  'enquadramento': 'Vertical 9:16. The fiddle-railed table fills nearly the '
                   'whole frame, the portlight glowing white in the top '
                   'corner. Cropped: the bunk, the companionway steps, his '
                   'body.',
  'luz': 'Dim cabin interior with reflected water-light rippling over the '
         'ceiling and spilling onto the varnish — moving, unstable, greenish',
  'audio': 'Hull creaking, water working against the planking, a fender '
           'squeaking on the dock. No music.',
  'aceita': ['pote', 'creme', 'sache', 'po', 'cubos', 'espuma'],
  'regua_cabe': True,
  'molhado': False},
 {'id': 'barco_tampa_motor_popa',
  'curto': 'tampa da caixa do motor na popa',
  'fonte': 'construido',
  'familia': 'outro',
  'ambiente': 'Aluminium centre-console fishing boat drifting on a lake at '
              'dawn, mist sitting on the water, rod holders empty, a landing '
              'net hooked over the rail, the outboard tilted up.',
  'superficie': 'the flat vinyl-covered engine box lid at the stern used as '
                'a seat — a padded grey rectangle, the vinyl split along one '
                'seam and mended with gaffer tape, a dried fish scale near '
                'the edge',
  'camera': 'POV of a man sitting on the thwart facing aft, phone in his '
            'right hand at chest height, aimed down at the engine box lid '
            'two feet away',
  'enquadramento': 'Vertical 9:16. The grey lid fills the lower two thirds, '
                   'the tilted outboard and the mist-white lake fill the '
                   'top. Cropped: his legs, the console, the far shore.',
  'luz': 'Flat cold dawn light through mist with no sun disc yet, everything '
         'grey-blue and very low contrast',
  'audio': 'Water knocking the aluminium hull, a loon calling, an outboard '
           'starting far across the lake. No music.',
  'aceita': ['pote', 'creme', 'sache', 'cubos', 'espuma'],
  'regua_cabe': True,
  'molhado': True},
 {'id': 'termal_terraco_travertino',
  'curto': 'lingua de travertino da fonte termal',
  'fonte': 'construido',
  'familia': 'ar_livre',
  'ambiente': 'Natural hot spring in high desert, terraces of orange and '
              'cream mineral crust stepping down the slope, steam pulling '
              'sideways in the wind, sagebrush and a dirt track above.',
  'superficie': 'a dry travertine shelf at the lip of the upper pool — a low '
                'mineral terrace like stacked poured wax, cream-white on top '
                'and rust-orange at the edge, warm and slightly rough',
  'camera': 'POV of a man sitting in the pool with his back against the '
            'terrace, phone in his right hand reaching back over his own '
            'shoulder, angled down at the shelf beside his ear',
  'enquadramento': 'Vertical 9:16. The cream shelf runs across the middle '
                   'band, steaming water at the bottom, sage and open sky at '
                   'the top. Cropped: his body, the lower pools, the track.',
  'luz': 'Hard low sun burning through the steam, hot rim light along every '
         'mineral ridge, the water reading almost black against it',
  'audio': 'Water trickling from terrace to terrace, wind across sage, a '
           'raven. No music.',
  'aceita': ['pote', 'creme', 'sache', 'espuma'],
  'regua_cabe': True,
  'molhado': False},
 {'id': 'termal_estrado_onsen',
  'curto': 'estrado de cipreste do onsen',
  'fonte': 'construido',
  'familia': 'ar_livre',
  'ambiente': 'Outdoor onsen bath at a mountain inn, boulders set around a '
              'steaming pool, a low wooden duckboard along the near edge, '
              'maples turning red on the slope, snow on the far peak.',
  'superficie': "one plank of the wooden duckboard at the pool's edge — a "
                'dark wet cypress board six inches wide with a shallow '
                'groove worn across it, water sheeting slowly over the '
                'surface',
  'camera': 'POV of a man kneeling on the duckboard, phone in his left hand '
            'at waist height, looking down along the plank so it runs away '
            'from him into the distance',
  'enquadramento': 'Vertical 9:16. The plank runs from the bottom of the '
                   'frame into depth, steaming water on one side, wet rock '
                   'on the other, red maple at the top. Cropped: his knees, '
                   'the sky.',
  'luz': 'Grey mountain overcast, very soft, steam diffusing everything, the '
         'red maples the only saturated colour in the frame',
  'audio': 'Water spilling from a bamboo spout, steam, snow melting off a '
           'roof edge. No music.',
  'aceita': ['pote', 'creme', 'sache', 'espuma'],
  'regua_cabe': False,
  'molhado': True},
 {'id': 'quintal_prateleira_ripas_cedro',
  'curto': 'prateleira de ripas do chuveiro de quintal',
  'fonte': 'construido',
  'familia': 'chuveiro',
  'ambiente': 'Outdoor shower stall built against a shingled beach house, '
              'three cedar walls open to the sky, a brass head gone green '
              'with salt, a wooden pallet floor laid over sand.',
  'superficie': 'the slatted cedar corner shelf screwed to the stall wall — '
                'two weather-silvered boards with a finger gap between them '
                'at chest height, a bar of soap gone soft in one corner of '
                'it',
  'camera': 'POV of a man standing in the stall with the water off, phone in '
            'his right hand at chest height, aimed level at the corner shelf',
  'enquadramento': 'Vertical 9:16. The shelf sits centre-frame, cedar boards '
                   'and open sky above it, the pallet floor cropped away '
                   'below. Cropped: his body, the shower head, the house.',
  'luz': 'Open sky straight overhead, bright bounce off the pale cedar, a '
         'hard-edged patch of sun drifting across as clouds move',
  'audio': 'Wind in beach grass, a screen door, gulls, the head still '
           'dripping. No music.',
  'aceita': ['pote', 'creme', 'sache', 'espuma'],
  'regua_cabe': False,
  'molhado': True},
 {'id': 'quintal_bloco_concreto',
  'curto': 'topo dos blocos de concreto empilhados',
  'fonte': 'construido',
  'familia': 'chuveiro',
  'ambiente': 'A garden hose rigged to a fence post as a shower in a bare '
              'backyard, a square of poured concrete for a floor, grey '
              'cinder blocks stacked as a step, dandelions in the cracks.',
  'superficie': 'the top of the stacked cinder blocks — the upper block '
                'turned web-face up so its two rectangular voids open like '
                'wells, grey and gritty, chipped along one corner',
  'camera': 'POV of a man crouching beside the blocks, phone in his right '
            'hand at knee height, looking down at the block face at about '
            'sixty degrees',
  'enquadramento': 'Vertical 9:16. The block face and its two open voids '
                   'fill the centre, wet concrete floor all round it, the '
                   'fence and the hose at the top. Cropped: his body, the '
                   'sky.',
  'luz': 'Flat late-afternoon overcast, cold grey on grey, the only warmth '
         'coming from the dandelions at the frame edge',
  'audio': 'Hose water spattering concrete, a sprinkler next door, a dog '
           'chain dragging. No music.',
  'aceita': ['pote', 'creme', 'sache', 'po', 'espuma'],
  'regua_cabe': True,
  'molhado': True},
 {'id': 'quintal_tanque_galvanizado',
  'curto': 'fundo do tanque galvanizado virado',
  'fonte': 'construido',
  'familia': 'chuveiro',
  'ambiente': 'A farm wash-up point beside a barn, a hose head wired to a '
              'rafter, a galvanised stock tank upturned as a stand, straw '
              'and mud on the concrete apron, a blanket over the rail.',
  'superficie': 'the upturned bottom of the galvanised stock tank — a broad '
                'dull-silver disc of ribbed sheet metal, dented in the '
                'middle and ringed by a raised rim, standing at waist height',
  'camera': 'POV of a man standing at the tank, phone in his left hand held '
            'out over it, looking almost straight down at the metal disc',
  'enquadramento': 'Vertical 9:16. The ribbed silver disc fills nearly the '
                   'whole frame, the concrete apron showing in one corner. '
                   'Cropped: his body, the barn wall, the shower head.',
  'luz': 'Low sun coming in flat under the barn roof, raking hard across the '
         'ribs of the metal, dust hanging visible in the beam',
  'audio': 'A horse shifting in a stall, water dripping, corrugated iron '
           'ticking as it cools. No music.',
  'aceita': ['pote', 'creme', 'sache', 'po', 'cubos', 'espuma'],
  'regua_cabe': True,
  'molhado': False},
 {'id': 'caminhoneiro_prateleira_inox',
  'curto': 'prateleira de inox do box do posto',
  'fonte': 'construido',
  'familia': 'chuveiro',
  'ambiente': 'Paid shower room at a truck stop, beige fibreglass panels on '
              'every side, an institutional head on a chrome ball joint, a '
              'used towel hanging on a plastic hook.',
  'superficie': 'the perforated stainless shelf bolted to the shower wall — '
                'a shallow tray six by fourteen inches with turned-up edges '
                'and a grid of drain holes, at shoulder height, water '
                'standing in the low corner',
  'camera': 'POV of a man standing in the stall, phone in his right hand at '
            'chest height, angled slightly up at the steel shelf on the wall',
  'enquadramento': 'Vertical 9:16. The steel tray sits across the upper '
                   'middle of the frame, beige fibreglass filling the rest, '
                   'the head cropped at the very top. Cropped: his body, the '
                   'door, the floor.',
  'luz': 'One recessed ceiling can behind steam, a single bright hotspot '
         'burning on the wet steel and flat beige everywhere else',
  'audio': 'Shower running, an engine brake outside, the extractor fan '
           'rattling in its housing. No music.',
  'aceita': ['pote', 'creme', 'sache', 'espuma'],
  'regua_cabe': True,
  'molhado': True},
 {'id': 'caminhoneiro_bancada_lascada',
  'curto': 'bancada lascada das pias do posto',
  'fonte': 'construido',
  'familia': 'pia',
  'ambiente': 'Truck stop washroom at night, four sinks in a run, a long '
              'mirror with one corner missing, cracked beige floor tile, an '
              'overflowing paper bin, the door propped by a mop bucket.',
  'superficie': 'the chipped laminate counter to the left of the first sink '
                '— a mustard-coloured particleboard top with the plastic '
                'edge strip peeling away and the swollen board showing '
                'through where water got in',
  'camera': 'POV of a man standing at the far sink, phone in his left hand '
            'at chest height, angled down at the counter beside him so the '
            'mirror stays out of the shot',
  'enquadramento': 'Vertical 9:16. The mustard counter runs diagonally '
                   'across the lower two thirds, the sink lip and one tap '
                   'crossing the top. Cropped: the mirror, his face, the '
                   'other sinks.',
  'luz': 'A buzzing fluorescent tube overhead, green-white and slightly '
         'unsteady, a hard shadow under every object',
  'audio': 'Fluorescent buzz, a hand dryer, air brakes hissing outside, a PA '
           'calling a shower number. No music.',
  'aceita': ['pote', 'creme', 'sache', 'po', 'cubos', 'liquido', 'espuma'],
  'regua_cabe': True,
  'molhado': False}]

# ⭐ OS GESTOS — 100 entradas, eixo proprio. `cabe_em` declara em que
# familia de cena cada um faz sentido: e' o acoplamento em codigo.
ACOES = [{'id': 'tampa_desrosqueada',
  'curto': 'desrosqueia a tampa turquesa do pote',
  'fonte': 'lido',
  'cabe_em': ['chuveiro',
              'banheira',
              'pia',
              'cozinha',
              'vaso',
              'sauna',
              'jacuzzi'],
  'vasilhame': 'a squat cobalt-blue ointment jar standing on the surface, '
               'teal screw lid still seated on it',
  't1_img': 'his thumb and two fingers are closed around the teal lid '
            'mid-turn, a pale line of white salve already showing under the '
            'loosened rim',
  't1_take': 'He turns the teal lid off the jar in one slow twist.',
  'substancia': 'white-blue translucent salve, thick and waxy, showing under '
                'the loosened rim',
  'usa_vicks': True},
 {'id': 'aponta_a_caixa',
  'curto': 'aponta o indicador para a caixa de gelatina',
  'fonte': 'lido',
  'cabe_em': ['chuveiro',
              'banheira',
              'pia',
              'cozinha',
              'vaso',
              'sauna',
              'jacuzzi'],
  'vasilhame': 'an orange and white Knox gelatin box standing upright, label '
               'square to the lens',
  't1_img': 'his index finger stops half an inch from the front of the '
            'standing gelatin box, the other fingers curled back into the '
            'palm',
  't1_take': 'He points one finger at the gelatin box and holds it there.',
  'substancia': 'dry sealed carton, matte orange and white, nothing spilled '
                'yet',
  'usa_vicks': False},
 {'id': 'pote_girado_pra_lente',
  'curto': 'gira o pote aberto apresentando a boca',
  'fonte': 'lido',
  'cabe_em': ['chuveiro',
              'banheira',
              'pia',
              'cozinha',
              'vaso',
              'sauna',
              'jacuzzi'],
  'vasilhame': 'an open cobalt-blue ointment jar cradled in one hand, no lid '
               'in frame',
  't1_img': 'the open jar is turned mouth-first toward the lens in his palm, '
            'the white salve inside catching the light flat and unbroken',
  't1_take': 'He rotates the open jar in his palm until the mouth faces the '
             'lens.',
  'substancia': 'smooth white salve, unbroken surface, faint green-blue cast',
  'usa_vicks': True},
 {'id': 'pote_erguido_na_lente',
  'curto': 'ergue o pote aberto ate a altura da lente',
  'fonte': 'lido',
  'cabe_em': ['chuveiro',
              'banheira',
              'pia',
              'cozinha',
              'vaso',
              'sauna',
              'jacuzzi'],
  'vasilhame': 'an open cobalt-blue ointment jar balanced on his flat palm',
  't1_img': 'the open jar is raised close to the lens on his flat palm, the '
            'surface of the white cream filling most of the frame with one '
            'shallow dent in it',
  't1_take': 'He lifts the open jar up toward the lens and stops.',
  'substancia': 'white cream with a shallow dent where a fingertip already '
                'pressed',
  'usa_vicks': True},
 {'id': 'palmas_abertas_sobre_os_props',
  'curto': 'abre as duas palmas sobre os produtos, gesto de olha isso',
  'fonte': 'lido',
  'cabe_em': ['chuveiro', 'banheira', 'pia', 'cozinha', 'vaso'],
  'vasilhame': 'the gelatin box and the open blue ointment jar standing side '
               'by side on the surface',
  't1_img': 'both hands are open palms up above the two products, fingers '
            'spread wide, touching nothing at all',
  't1_take': 'He opens both palms above the products and holds them there.',
  'substancia': 'nothing poured yet, dry orange carton beside untouched '
                'white salve',
  'usa_vicks': True},
 {'id': 'caixa_erguida_pra_lente',
  'curto': 'ergue a caixa de gelatina ate a lente, rotulo virado',
  'fonte': 'lido',
  'cabe_em': ['chuveiro',
              'banheira',
              'pia',
              'cozinha',
              'vaso',
              'sauna',
              'jacuzzi'],
  'vasilhame': 'a sealed orange and white gelatin box held in both hands',
  't1_img': 'both hands hold the gelatin box up close to the lens with the '
            'label square on, the tiled corner blurred out behind it',
  't1_take': 'He raises the gelatin box to the lens and turns the label '
             'square.',
  'substancia': 'sealed orange carton, dry and still full, corners sharp',
  'usa_vicks': False},
 {'id': 'aba_da_caixa_rasgada',
  'curto': 'rasga a aba de cima da caixa',
  'fonte': 'lido',
  'cabe_em': ['chuveiro',
              'banheira',
              'pia',
              'cozinha',
              'vaso',
              'sauna',
              'jacuzzi'],
  'vasilhame': 'a gelatin box held upright in one hand, top flap half torn',
  't1_img': 'his thumb has torn the top flap of the gelatin box halfway open '
            'and the pale sachet inside is showing through the split',
  't1_take': 'He tears the top flap of the gelatin box open with his thumb.',
  'substancia': 'torn cardboard fibres along the split, the pale sachet '
                'showing through',
  'usa_vicks': False},
 {'id': 'sache_puxado_de_dentro',
  'curto': 'puxa o sache de dentro da caixa',
  'fonte': 'lido',
  'cabe_em': ['chuveiro',
              'banheira',
              'pia',
              'cozinha',
              'vaso',
              'sauna',
              'jacuzzi'],
  'vasilhame': 'an opened gelatin box in the left hand with a paper sachet '
               'coming out of the top',
  't1_img': 'two fingers have the paper sachet pinched and drawn halfway '
            'clear of the open box, the box tipped back to let it out',
  't1_take': 'He draws the paper sachet up out of the open box.',
  'substancia': 'kraft-paper sachet, taut and full of fine powder',
  'usa_vicks': False},
 {'id': 'sache_rasgado',
  'curto': 'rasga o topo do sache',
  'fonte': 'lido',
  'cabe_em': ['chuveiro',
              'banheira',
              'pia',
              'cozinha',
              'vaso',
              'sauna',
              'jacuzzi',
              'praia'],
  'vasilhame': 'a full paper gelatin sachet held between both hands',
  't1_img': 'both hands hold the sachet at chest height with the torn top '
            'strip hanging off it and the open mouth tipped slightly down',
  't1_take': 'He tears the top strip off the sachet.',
  'substancia': 'fine pale straw-coloured powder banked at the torn mouth',
  'usa_vicks': False},
 {'id': 'sache_erguido_rasgado',
  'curto': 'ergue o sache ja rasgado colado na lente',
  'fonte': 'lido',
  'cabe_em': ['chuveiro', 'banheira', 'pia', 'cozinha', 'vaso'],
  'vasilhame': 'a torn gelatin sachet held flat in the right hand',
  't1_img': 'the torn sachet is held up flat against the lens filling half '
            'the frame, the ragged tear running across its whole top edge',
  't1_take': 'He holds the torn sachet up to the lens and keeps it still.',
  'substancia': 'white powder banked inside the torn sachet, a dusting of it '
                'along the seam',
  'usa_vicks': False},
 {'id': 'po_despejado_no_pote',
  'curto': 'despeja o po do sache dentro do pote aberto',
  'fonte': 'lido',
  'cabe_em': ['chuveiro',
              'banheira',
              'pia',
              'cozinha',
              'vaso',
              'sauna',
              'jacuzzi'],
  'vasilhame': 'a torn gelatin sachet tipped over an open cobalt-blue '
               'ointment jar',
  't1_img': 'a continuous thread of pale powder falls from the tilted sachet '
            'into the open blue jar and has already built a small cone on '
            'the white salve',
  't1_take': 'He tips the sachet and lets the powder run into the open jar.',
  'substancia': 'fine cream-coloured powder falling onto thick white salve',
  'usa_vicks': True},
 {'id': 'po_da_caixa_no_pote',
  'curto': 'despeja o po direto da caixa dentro do pote',
  'fonte': 'lido',
  'cabe_em': ['chuveiro', 'banheira', 'pia', 'cozinha', 'vaso', 'sauna'],
  'vasilhame': 'an opened gelatin box tipped over an open cobalt-blue '
               'ointment jar held in the other hand',
  't1_img': 'the box is tilted steeply and a wide fall of pale powder is '
            'dropping into the jar, a dust haze hanging around the rim',
  't1_take': 'He tips the whole box and the powder falls into the jar.',
  'substancia': 'dry pale powder in a broad fall, dust hazing the air at the '
                'rim',
  'usa_vicks': True},
 {'id': 'po_no_liquido_ambar',
  'curto': 'despeja o po sobre o liquido ambar do copo',
  'fonte': 'lido',
  'cabe_em': ['pia', 'cozinha', 'vaso', 'banheira'],
  'vasilhame': 'a tall plain drinking glass of amber liquid, a torn sachet '
               'held above it',
  't1_img': 'the powder has landed on the surface of the amber liquid and '
            'sits there as a white island that has not sunk yet',
  't1_take': 'He shakes the sachet once over the glass and the powder '
             'settles on the surface.',
  'substancia': 'white powder floating as a raft on translucent amber liquid',
  'usa_vicks': False},
 {'id': 'po_azul_na_agua',
  'curto': 'despeja o po azul na tigela com agua',
  'fonte': 'lido',
  'cabe_em': ['pia', 'cozinha', 'vaso'],
  'vasilhame': 'a shallow clear glass bowl of still water on the counter',
  't1_img': 'a heap of blue powder has just hit the water and is blooming '
            'outward in a cloud from the point where it landed',
  't1_take': 'He tips the sachet and the blue powder drops into the water.',
  'substancia': 'royal-blue powder clouding out into clear still water',
  'usa_vicks': False},
 {'id': 'sache_verte_tinta_azul',
  'curto': 'despeja o sache e o conteudo cai como tinta azul',
  'fonte': 'lido',
  'cabe_em': ['cozinha', 'pia'],
  'vasilhame': 'a wide shallow glass bowl, empty, on a butcher block '
               'counter, the torn sachet held above it in both hands',
  't1_img': 'what leaves the sachet is not powder but a rope of vivid blue '
            'liquid, already pooling and spreading across the bottom of the '
            'bowl',
  't1_take': 'He squeezes the sachet and the blue liquid runs out into the '
             'bowl.',
  'substancia': 'vivid cyan liquid, ink-like, glossy where it pools',
  'usa_vicks': False},
 {'id': 'dedo_afunda_no_pote',
  'curto': 'enfia o indicador no pote e mexe',
  'fonte': 'lido',
  'cabe_em': ['chuveiro',
              'banheira',
              'pia',
              'cozinha',
              'vaso',
              'sauna',
              'jacuzzi'],
  'vasilhame': 'an open cobalt-blue ointment jar steadied on the surface by '
               'the other hand',
  't1_img': 'his index finger is buried to the first knuckle in the jar and '
            'has dragged one spiral through the powder into the salve '
            'underneath',
  't1_take': 'He pushes one finger into the jar and stirs once.',
  'substancia': 'white powder folding into blue-white salve, grey-blue '
                'streaks turning up',
  'usa_vicks': True},
 {'id': 'dedo_comprime_o_po',
  'curto': 'comprime o po contra o creme com a polpa do dedo',
  'fonte': 'lido',
  'cabe_em': ['chuveiro', 'banheira', 'pia', 'cozinha', 'vaso', 'sauna'],
  'vasilhame': 'an open cobalt-blue ointment jar held level in the other '
               'hand',
  't1_img': 'the pad of his index finger is pressing the powder flat down '
            'against the salve and a shallow print stays where he pushed',
  't1_take': 'He presses the powder down into the salve with the pad of his '
             'finger.',
  'substancia': 'dry powder compacting into waxy salve, the fingerprint '
                'holding its shape',
  'usa_vicks': True},
 {'id': 'dedo_erguido_com_bolota',
  'curto': 'ergue o dedo com uma bolota de creme na ponta',
  'fonte': 'lido',
  'cabe_em': ['chuveiro',
              'banheira',
              'pia',
              'cozinha',
              'vaso',
              'sauna',
              'jacuzzi'],
  'vasilhame': 'an open cobalt-blue ointment jar held low in the other hand',
  't1_img': 'his index finger is raised in the centre of the frame with a '
            'fat blob of white cream sitting on the tip, blue-green flecks '
            'running through it',
  't1_take': 'He lifts his finger clear of the jar with the blob of cream on '
             'the tip.',
  'substancia': 'white cream with blue-green flecks, holding a soft peak on '
                'the fingertip',
  'usa_vicks': True},
 {'id': 'dedo_com_fio_escorrendo',
  'curto': 'ergue o dedo e um fio pegajoso escorre ate o pote',
  'fonte': 'lido',
  'cabe_em': ['chuveiro', 'banheira', 'pia', 'cozinha', 'vaso', 'sauna'],
  'vasilhame': 'an open cobalt-blue ointment jar directly below the raised '
               'hand',
  't1_img': 'a single sticky thread stretches from his lifted fingertip back '
            'down to the surface in the jar, thin in the middle and about to '
            'break',
  't1_take': 'He raises his finger until the sticky thread from the jar '
             'stretches thin.',
  'substancia': 'sticky white cream drawing itself into one long thread',
  'usa_vicks': True},
 {'id': 'dois_dedos_pegam_creme',
  'curto': 'pega o creme do pote com dois dedos',
  'fonte': 'lido',
  'cabe_em': ['chuveiro', 'banheira', 'pia', 'sauna', 'jacuzzi'],
  'vasilhame': 'a small open blue ointment jar cradled in the left hand',
  't1_img': 'two fingers come out of the jar with a scoop of white cream '
            'held between them, the jar still cradled in the other hand',
  't1_take': 'He scoops cream out of the jar with two fingers.',
  'substancia': 'opaque white cream, dense, holding the shape of the two '
                'fingertips',
  'usa_vicks': True},
 {'id': 'recarrega_o_dedo',
  'curto': 'volta ao pote e recarrega a ponta do dedo',
  'fonte': 'lido',
  'cabe_em': ['chuveiro', 'banheira', 'pia', 'sauna', 'jacuzzi'],
  'vasilhame': 'an open blue ointment jar held at chest height in the other '
               'hand',
  't1_img': 'his fingertip is coming out of the jar loaded a second time '
            'while the first smear is still drying matte on the back of the '
            'same hand',
  't1_take': 'He dips back into the jar and loads his fingertip again.',
  'substancia': 'white cream, a fresh load on the fingertip, the earlier '
                'smear gone matte',
  'usa_vicks': True},
 {'id': 'mel_da_colher',
  'curto': 'inclina a colher e derrama o mel sobre o po',
  'fonte': 'lido',
  'cabe_em': ['chuveiro', 'banheira', 'pia', 'cozinha', 'vaso', 'sauna'],
  'vasilhame': 'a plain steel tablespoon of honey tilted over the open blue '
               'jar',
  't1_img': 'the spoon is tipped and a thick ribbon of amber honey is '
            'falling onto the white powder, already pooling in the centre of '
            'the jar',
  't1_take': 'He tips the spoon and the honey runs onto the powder.',
  'substancia': 'amber honey, thick and slow, pooling on white powder',
  'usa_vicks': True},
 {'id': 'mel_do_alto',
  'curto': 'ergue a colher bem alto e o fio de mel atravessa o quadro',
  'fonte': 'lido',
  'cabe_em': ['chuveiro', 'banheira', 'pia', 'cozinha', 'vaso'],
  'vasilhame': 'a steel spoon of dark honey held high above the open blue '
               'jar',
  't1_img': 'the spoon is held high above the jar and one unbroken amber '
            'thread runs the full height of the frame down into it',
  't1_take': 'He raises the spoon high and lets the honey fall in one long '
             'thread.',
  'substancia': 'dark amber honey in a single unbroken thread, glassy where '
                'the light hits',
  'usa_vicks': True},
 {'id': 'mel_suspenso_pingando',
  'curto': 'mantem a colher de mel suspensa, pingando',
  'fonte': 'lido',
  'cabe_em': ['chuveiro', 'banheira', 'pia', 'cozinha', 'vaso'],
  'vasilhame': 'a steel spoon of honey held still above the open blue jar',
  't1_img': 'the spoon hangs motionless above the jar with a heavy drop of '
            'honey gathering on its lip and not yet falling',
  't1_take': 'He holds the honey spoon still above the jar and lets a drop '
             'gather.',
  'substancia': 'dark amber honey gathering into one heavy drop on the spoon '
                'lip',
  'usa_vicks': True},
 {'id': 'colher_mexe_no_copo',
  'curto': 'mexe com a colher dentro do copo',
  'fonte': 'lido',
  'cabe_em': ['pia', 'cozinha', 'vaso', 'banheira'],
  'vasilhame': 'a tall glass of amber liquid with a long steel spoon '
               'standing in it',
  't1_img': 'the long spoon is mid-turn inside the glass and the amber '
            'liquid has gone cloudy beige with white grains suspended in the '
            'swirl',
  't1_take': 'He turns the spoon once around the inside of the glass.',
  'substancia': 'amber liquid gone cloudy beige, white grains turning '
                'through it',
  'usa_vicks': False},
 {'id': 'colher_ergue_fios',
  'curto': 'ergue a colher e o liquido desce em babas grossas',
  'fonte': 'lido',
  'cabe_em': ['pia', 'cozinha', 'vaso', 'banheira'],
  'vasilhame': 'a tall glass of thickened beige liquid, the steel spoon '
               'lifted clear of it',
  't1_img': 'the spoon is held clear of the glass and the liquid is coming '
            'off it in thick opaque ropes instead of drops',
  't1_take': 'He lifts the spoon out of the glass and the liquid falls off '
             'it in ropes.',
  'substancia': 'thick beige liquid falling in slow elastic ropes, like raw '
                'egg white',
  'usa_vicks': False},
 {'id': 'colher_espetada',
  'curto': 'deixa a colher em pe no copo e afasta a mao',
  'fonte': 'lido',
  'cabe_em': ['pia', 'cozinha', 'vaso', 'banheira'],
  'vasilhame': 'a tall glass of thickened beige mixture with the spoon '
               'standing upright in it',
  't1_img': 'the spoon is standing on its own in the thickened liquid and '
            'his hand is drawing back with the fingers opening away from it',
  't1_take': 'He lets go of the spoon and it stands up in the glass on its '
             'own.',
  'substancia': 'thickened beige mixture, stiff enough to hold the spoon '
                'upright',
  'usa_vicks': False},
 {'id': 'colher_mexe_ate_dourar',
  'curto': 'mexe com a colher ate o conteudo virar dourado',
  'fonte': 'lido',
  'cabe_em': ['chuveiro', 'banheira', 'pia', 'cozinha', 'vaso'],
  'vasilhame': 'an open cobalt-blue ointment jar held steady on the shelf, a '
               'long steel spoon inside it',
  't1_img': 'the spoon is turning inside the jar and the paste has gone from '
            'white to warm gold along the whole track it has cut',
  't1_take': 'He turns the spoon through the jar until the paste goes gold.',
  'substancia': 'white paste turning warm gold along the spoon track, glossy '
                'at the edges',
  'usa_vicks': True},
 {'id': 'colher_mergulha_bloco_branco',
  'curto': 'mergulha a colher com o bloco branco na taca azul',
  'fonte': 'lido',
  'cabe_em': ['pia', 'cozinha', 'vaso'],
  'vasilhame': 'a stemless wine glass of electric-blue liquid with a white '
               'head on top',
  't1_img': 'the spoon is pushing a white block down under the surface of '
            'the blue liquid and white clouds are trailing off it as it '
            'sinks',
  't1_take': 'He pushes the white block under the blue liquid with the '
             'spoon.',
  'substancia': 'opaque white block dissolving in clouds through '
                'electric-blue liquid',
  'usa_vicks': False},
 {'id': 'fio_ambar_em_espiral',
  'curto': 'despeja o fio ambar que desce em espiral no azul',
  'fonte': 'lido',
  'cabe_em': ['pia', 'cozinha', 'vaso'],
  'vasilhame': 'a stemless wine glass of electric-blue liquid, a steel spoon '
               'pouring above it',
  't1_img': 'a thick amber thread is falling into the blue drink and '
            'spiralling down without mixing, a gold layer already sitting on '
            'the bottom',
  't1_take': 'He pours the amber thread into the blue drink and it spirals '
             'to the bottom.',
  'substancia': 'amber syrup spiralling through electric-blue liquid, '
                'settling gold at the base',
  'usa_vicks': False},
 {'id': 'agua_do_copo_no_pote',
  'curto': 'despeja agua de um copo dentro do pote',
  'fonte': 'lido',
  'cabe_em': ['chuveiro', 'banheira', 'pia', 'cozinha'],
  'vasilhame': 'a clear drinking glass of water tipped over the open blue '
               'ointment jar',
  't1_img': 'the glass is tipped in at the top edge of frame and a thin fall '
            'of water is landing in the jar on the powder and honey, '
            'darkening the surface where it hits',
  't1_take': 'He tips the glass and pours water into the jar.',
  'substancia': 'clear water landing on white powder and amber honey, '
                'darkening it on contact',
  'usa_vicks': True},
 {'id': 'chia_despejada',
  'curto': 'despeja as sementes de um copinho sobre o gel',
  'fonte': 'lido',
  'cabe_em': ['pia', 'cozinha', 'vaso'],
  'vasilhame': 'a small clear measuring cup of dark seeds held over the '
               'glass bowl',
  't1_img': 'the seeds are landing on the blue gel and spreading into a dark '
            'drift across the middle of it',
  't1_take': 'He tips the little cup and the seeds scatter across the gel.',
  'substancia': 'small grey-black seeds drifting across royal-blue gel',
  'usa_vicks': False},
 {'id': 'espuma_sobe_ate_a_borda',
  'curto': 'a mistura efervesce e a espuma sobe ate a borda',
  'fonte': 'lido',
  'cabe_em': ['chuveiro', 'banheira', 'pia', 'cozinha', 'vaso', 'sauna'],
  'vasilhame': 'the open cobalt-blue ointment jar alone on the surface, no '
               'hands in frame',
  't1_img': 'the jar is full to the thread with white foam of big uneven '
            'bubbles, risen level with the rim and stopped there',
  't1_take': 'The mixture fizzes and the foam rises to the rim of the jar.',
  'substancia': 'white foam of large uneven bubbles, matte, filling the jar '
                'to the thread',
  'usa_vicks': True},
 {'id': 'espuma_transborda_pelo_rotulo',
  'curto': 'a espuma transborda e escorre pela lateral do pote',
  'fonte': 'lido',
  'cabe_em': ['chuveiro', 'banheira', 'pia', 'cozinha', 'vaso'],
  'vasilhame': 'the open cobalt-blue ointment jar on the surface with foam '
               'over its mouth',
  't1_img': 'the foam has broken over the rim and two heavy runs of it are '
            'sliding down the blue label to the surface below',
  't1_take': 'The foam breaks over the rim and runs down the side of the '
             'jar.',
  'substancia': 'white foam overflowing, running in heavy streaks down '
                'cobalt-blue',
  'usa_vicks': True},
 {'id': 'espuma_em_cupula',
  'curto': 'a espuma sobe em cupula acima da boca do pote',
  'fonte': 'lido',
  'cabe_em': ['chuveiro', 'banheira', 'pia', 'cozinha', 'vaso', 'sauna'],
  'vasilhame': 'the open cobalt-blue ointment jar standing alone, foam '
               'crowning it',
  't1_img': 'the foam stands in a firm dome a full inch above the mouth of '
            'the jar, bubbles fine and tight, none of it running over',
  't1_take': 'The foam swells into a dome above the mouth of the jar and '
             'holds.',
  'substancia': 'dense white foam, fine tight bubbles, holding a clean dome',
  'usa_vicks': True},
 {'id': 'faca_corta_o_gel',
  'curto': 'corta o gel firme em cubos com a faca',
  'fonte': 'lido',
  'cabe_em': ['cozinha', 'pia'],
  'vasilhame': 'a clear glass bowl of set blue gel on the counter',
  't1_img': 'the black-handled chef knife has cut two clean lines through '
            'the set gel and is standing in the third cut',
  't1_take': 'He draws the knife once through the set gel.',
  'substancia': 'firm translucent blue gel, the cut faces glossy and square',
  'usa_vicks': False},
 {'id': 'cubo_pescado_na_tigela',
  'curto': 'mergulha a mao e pesca um cubo da tigela',
  'fonte': 'lido',
  'cabe_em': ['cozinha', 'pia', 'banheira'],
  'vasilhame': 'a clear glass bowl of cut blue cubes under a little water',
  't1_img': 'his fingers are closing on one cube below the surface and the '
            'cube beside it is tipping into the gap it leaves',
  't1_take': 'He reaches into the bowl and picks one cube out.',
  'substancia': 'wet blue cubes, wobbling, water running off the edges',
  'usa_vicks': False},
 {'id': 'cubo_erguido_na_lente',
  'curto': 'ergue um cubo ate a lente',
  'fonte': 'lido',
  'cabe_em': ['cozinha', 'pia', 'banheira', 'chuveiro', 'jacuzzi'],
  'vasilhame': 'a clear glass bowl of cubes below, one cube held up between '
               'finger and thumb',
  't1_img': 'one large blue cube is held close to the lens between finger '
            'and thumb, its internal layers and silver flecks lit through '
            'from behind',
  't1_take': 'He raises the cube up to the lens and stops.',
  'substancia': 'translucent blue gel cube, layered inside, wet and shining',
  'usa_vicks': False},
 {'id': 'fatia_girada_na_lente',
  'curto': 'ergue a fatia e gira mostrando as duas faces',
  'fonte': 'lido',
  'cabe_em': ['cozinha', 'pia'],
  'vasilhame': 'a wide glass bowl of set blue gel with one thick slice '
               'lifted out of it',
  't1_img': 'a thick rectangular slice of blue gel is held up to the lens '
            'edge-on, gel running off the bottom corner back down into the '
            'bowl',
  't1_take': 'He turns the slice of gel over in front of the lens.',
  'substancia': 'thick blue gel slice with pale seeds suspended in it, '
                'dripping at the corner',
  'usa_vicks': False},
 {'id': 'cubos_na_palma_aberta',
  'curto': 'segura os cubos na palma aberta',
  'fonte': 'construido',
  'cabe_em': ['chuveiro', 'banheira', 'pia', 'cozinha', 'jacuzzi', 'praia'],
  'vasilhame': 'a shallow glass bowl of set cubes just below the open hand',
  't1_img': 'three cubes sit flat on his open palm still trembling from '
            'being set down, water beading on the skin under them',
  't1_take': 'He settles three cubes onto his open palm and keeps his '
             'fingers flat.',
  'substancia': 'wet amber-blue cubes, trembling, beading water on the palm',
  'usa_vicks': False},
 {'id': 'creme_na_nuca',
  'curto': 'passa o creme na propria nuca',
  'fonte': 'lido',
  'cabe_em': ['chuveiro', 'banheira', 'pia', 'sauna', 'jacuzzi'],
  'vasilhame': 'an open blue ointment jar held low in his other hand',
  't1_img': 'seen from behind, his hand is flat on the back of his own neck '
            'with a white smear already spread from the hairline down',
  't1_take': 'He rubs the cream into the back of his own neck.',
  'substancia': 'opaque white cream, finger tracks visible across the skin',
  'usa_vicks': True},
 {'id': 'creme_no_peito',
  'curto': 'esfrega o creme no proprio peito em circulos',
  'fonte': 'lido',
  'cabe_em': ['banheira', 'pia', 'chuveiro', 'sauna', 'jacuzzi', 'praia'],
  'vasilhame': 'an open blue ointment jar and its teal lid held together in '
               'his left hand',
  't1_img': 'his open palm is flat on his own bare chest with the white '
            'cream spread in a wide circle over grey chest hair, his face '
            'cropped away above the frame',
  't1_take': 'He rubs the cream into his own chest in one slow circle.',
  'substancia': 'thick white cream shining wet across grey chest hair',
  'usa_vicks': True},
 {'id': 'creme_no_antebraco',
  'curto': 'espalha o creme no proprio antebraco',
  'fonte': 'construido',
  'cabe_em': ['chuveiro',
              'banheira',
              'pia',
              'cozinha',
              'sauna',
              'jacuzzi',
              'praia'],
  'vasilhame': 'an open blue ointment jar standing on the surface beside his '
               'elbow',
  't1_img': 'a broad white smear runs along the inside of his own forearm '
            'and his other hand is still flat on it at the end of the stroke',
  't1_take': 'He spreads the cream along the inside of his own forearm.',
  'substancia': 'white cream thinning to a shine over the forearm hair',
  'usa_vicks': True},
 {'id': 'creme_na_regua',
  'curto': 'esfrega o creme descendo pela face da regua',
  'fonte': 'lido',
  'cabe_em': ['chuveiro', 'banheira', 'pia', 'cozinha'],
  'vasilhame': 'a dark wooden ruler standing upright against the tiled '
               'corner',
  't1_img': 'his fingers are drawn halfway down the face of the standing '
            'ruler leaving a white streak straight across the printed '
            'numbers',
  't1_take': 'He drags the cream down the face of the ruler with two '
             'fingers.',
  'substancia': 'white cream smeared over dark varnished wood and printed '
                'numbers',
  'usa_vicks': True},
 {'id': 'pote_suspenso_sob_o_jato',
  'curto': 'segura o pote suspenso sob o jato do chuveiro',
  'fonte': 'lido',
  'cabe_em': ['chuveiro'],
  'vasilhame': 'the open blue ointment jar held up in mid-air with no '
               'surface under it',
  't1_img': 'the open jar is held out into the falling water with nothing '
            'under it, the stream breaking white across his knuckles and the '
            'rim',
  't1_take': 'He holds the open jar out into the falling water.',
  'substancia': 'white salve in the jar, water breaking white over the hand '
                'around it',
  'usa_vicks': True},
 {'id': 'palma_passa_na_prateleira',
  'curto': 'passa a palma aberta sobre a prateleira molhada',
  'fonte': 'lido',
  'cabe_em': ['chuveiro', 'banheira'],
  'vasilhame': 'a soaked solid wood corner shelf with the jar and the box '
               'standing on it',
  't1_img': 'his open palm is sweeping across the wet shelf and pushing a '
            'sheet of water ahead of it toward the front edge',
  't1_take': 'He sweeps his open palm across the wet shelf.',
  'substancia': 'standing water and foam residue skimming off dark soaked '
                'wood',
  'usa_vicks': False},
 {'id': 'mao_pousa_o_pote',
  'curto': 'pousa o pote na superficie e retira a mao',
  'fonte': 'lido',
  'cabe_em': ['chuveiro', 'banheira', 'pia', 'cozinha', 'vaso', 'sauna'],
  'vasilhame': 'the open cobalt-blue ointment jar just set down on the '
               'surface, foam level in it',
  't1_img': 'the jar has just been set down and his fingers are already '
            'lifting off it, one still curled near the rim',
  't1_take': 'He sets the jar down and takes his hand away.',
  'substancia': 'white foam settled level in the jar, the surface still '
                'moving slightly',
  'usa_vicks': True},
 {'id': 'vk-c01',
  'curto': 'Peneirar o po numa peneirinha de cha sobre o pote',
  'fonte': 'construido',
  'cabe_em': ['borda_banheira',
              'bancada_pia',
              'cozinha',
              'banquinho_madeira'],
  'vasilhame': 'Small stainless mesh sieve held over the open cobalt-blue '
               'VapoRub jar, the orange-and-white Knox gelatin box standing '
               'behind it.',
  't1_img': 'Frozen macro from above: a small stainless mesh sieve hovers '
            'two inches over the open cobalt VapoRub jar, its bowl heaped '
            'with cream-white gelatin powder, and a thin veil of powder '
            'hangs suspended mid-fall over the pale salve. Weathered older '
            'hand, veined and freckled, gripping the sieve handle. No face.',
  't1_take': 'The weathered hand taps the rim of the small stainless sieve '
             'held over the open cobalt VapoRub jar, and fine cream-white '
             'gelatin powder sifts down through the mesh in a slow drifting '
             'veil that settles across the pale salve.',
  'substancia': 'Fine cream-white gelatin powder, dry and floury, drifting '
                'in a soft veil onto dense white salve with faint blue-grey '
                'streaks.',
  'usa_vicks': True},
 {'id': 'vk-c02',
  'curto': 'Bater a mistura com garfo dentro do pote',
  'fonte': 'construido',
  'cabe_em': ['bancada_pia', 'borda_banheira', 'cozinha', 'tampa_vaso'],
  'vasilhame': 'Open cobalt-blue VapoRub jar held low in one hand, plain '
               'stainless dinner fork in the other.',
  't1_img': 'Frozen macro: a stainless dinner fork stands buried tines-down '
            'in the white paste inside the open cobalt VapoRub jar, a ridge '
            'of whipped cream-white peaks risen around the tines, one bead '
            'of paste clinging to the fork handle. Old veined hands, no '
            'face, no torso.',
  't1_take': 'The hand whisks the stainless dinner fork in fast tight '
             'circles inside the open cobalt VapoRub jar, and the white '
             'paste climbs the tines and stiffens into aerated peaks that '
             'hold their shape.',
  'substancia': 'Dense white salve whipped pale and airy, stiff peaks, shot '
                'through with grey-blue flecks and dry powder pockets.',
  'usa_vicks': True},
 {'id': 'vk-c03',
  'curto': 'Amassar os grumos com as costas do garfo',
  'fonte': 'construido',
  'cabe_em': ['cozinha', 'bancada_pia', 'peitoril_janela'],
  'vasilhame': 'Shallow clear glass Pyrex bowl on the counter, torn gelatin '
               'sachet lying beside it.',
  't1_img': 'Frozen top-down: the back of a stainless fork presses flat '
            'against a lump of pale gelatin paste in a shallow clear glass '
            'bowl, the lump crushed into a fan of ridged tine marks, dry '
            'powder still visible at the edges. Old hands with liver spots, '
            'no face.',
  't1_take': 'The hand presses the back of the stainless fork down onto the '
             'lumps of pale paste in the clear glass bowl, dragging once, '
             'and the lumps flatten into a smooth ridged smear that spreads '
             'across the glass.',
  'substancia': 'Pale cream lumps crushing into a smooth ridged paste, matte '
                'and slightly tacky, with dry white powder still unmixed at '
                'the rim.',
  'usa_vicks': False},
 {'id': 'vk-c04',
  'curto': 'Aquecer o pote na agua quente da banheira',
  'fonte': 'construido',
  'cabe_em': ['borda_banheira', 'banquinho_madeira'],
  'vasilhame': 'Closed cobalt-blue VapoRub jar with its turquoise screw cap '
               'on, held half-submerged in the bath water.',
  't1_img': 'Frozen: the closed cobalt VapoRub jar sits half-sunk in '
            'steaming olive-green bath water, held between an old thumb and '
            'two fingers, a ring of ripples frozen around the label and '
            'condensation beading on the blue lid. Steam hangs above the '
            'water. Hand and forearm only, no face.',
  't1_take': 'The old hand rocks the closed cobalt VapoRub jar slowly back '
             'and forth in the steaming bath water, ripples spreading out '
             'from the label in slow rings as the jar warms.',
  'substancia': 'Turbid olive-green bath water, steam rising, the cobalt jar '
                'glossy and beaded with condensation, salve softening unseen '
                'inside.',
  'usa_vicks': True},
 {'id': 'vk-c05',
  'curto': 'Aquecer o pote dentro de uma caneca de agua quente',
  'fonte': 'construido',
  'cabe_em': ['cozinha', 'bancada_pia', 'peitoril_janela'],
  'vasilhame': 'Beige ceramic mug of steaming water with the closed cobalt '
               'VapoRub jar standing inside it.',
  't1_img': 'Frozen: the closed cobalt VapoRub jar stands upright inside a '
            'beige ceramic mug filled with steaming water, water line '
            'halfway up the label, an old hand cupping the mug from the '
            'side, steam curling past the turquoise cap. Kitchen light '
            'raking across. No face.',
  't1_take': 'The old hand lowers the closed cobalt VapoRub jar down into '
             'the mug of steaming water until the water climbs to the middle '
             'of the label and settles, steam curling around the turquoise '
             'cap.',
  'substancia': 'Clear hot water clouding faintly, steam curling, the cobalt '
                'jar darkening with wet as it sinks.',
  'usa_vicks': True},
 {'id': 'vk-c06',
  'curto': 'Pote aberto embaixo do jato do chuveiro',
  'fonte': 'construido',
  'cabe_em': ['sob_o_jato', 'prateleira_box', 'nicho_box'],
  'vasilhame': 'Open cobalt-blue VapoRub jar, no cap in frame, held out flat '
               'on the palm under the running shower.',
  't1_img': 'Frozen: the open cobalt VapoRub jar sits flat on an old open '
            'palm directly under the falling shower, a hard rope of water '
            'striking the white salve and blowing a small crater in it, '
            'droplets exploding off the rim. Wet weathered hand, water '
            'running down the wrist. No face.',
  't1_take': 'The old hand holds the open cobalt VapoRub jar out flat on the '
             'palm under the falling shower, and the water drills a slow '
             'crater into the white salve as the jar fills and overflows '
             'down the sides.',
  'substancia': 'White salve pitted and glossy under a hard rope of clear '
                'water, the surface turning slick and translucent at the '
                'crater edge.',
  'usa_vicks': True},
 {'id': 'vk-c08',
  'curto': 'Espalhar a pasta ao longo de uma espatula de silicone',
  'fonte': 'construido',
  'cabe_em': ['cozinha', 'bancada_pia', 'tampa_vaso'],
  'vasilhame': 'Black silicone spatula blade held flat, open cobalt VapoRub '
               'jar resting on the surface beneath it.',
  't1_img': 'Frozen macro: a thick even layer of pale gelatin paste is '
            'smeared the full length of a black silicone spatula blade, held '
            'horizontal in an old hand, the ridge of paste catching the '
            'light along the blade edge. The open cobalt jar sits below on '
            'the surface. No face.',
  't1_take': 'The old hand drags the loaded black silicone spatula slowly '
             'across the frame, spreading the pale paste out into one long '
             'even ribbon along the blade until it reaches the tip.',
  'substancia': 'Pale cream paste, thick and satiny, laid in one even ribbon '
                'on black silicone, edges standing up in a soft ridge.',
  'usa_vicks': True},
 {'id': 'vk-c09',
  'curto': 'Raspar a parede interna do pote com a espatula',
  'fonte': 'construido',
  'cabe_em': ['bancada_pia', 'cozinha', 'prateleira_box'],
  'vasilhame': 'Open cobalt-blue VapoRub jar tilted toward the lens, small '
               'black silicone spatula inside it.',
  't1_img': 'Frozen macro straight down: the small black silicone spatula is '
            'pressed flat against the inner wall of the tilted open cobalt '
            'jar, a clean scraped stripe of blue glass showing where it '
            'passed, a curl of white paste rolled up on the blade. Old hand '
            'gripping the jar. No face.',
  't1_take': 'The old hand runs the small black silicone spatula once around '
             'the inner wall of the tilted cobalt jar, peeling a clean '
             'stripe down to the blue glass and rolling the paste into a '
             'curl on the blade.',
  'substancia': 'Sticky white salve peeling off blue glass in a soft curl, a '
                'clean wet stripe left behind on the jar wall.',
  'usa_vicks': True},
 {'id': 'vk-c10',
  'curto': 'Enrolar a pasta num quadrado de gaze',
  'fonte': 'construido',
  'cabe_em': ['bancada_pia', 'borda_banheira', 'cozinha'],
  'vasilhame': 'Square of white cotton gauze opened flat on the counter, a '
               'spoonful of pale paste in its centre.',
  't1_img': 'Frozen: an open square of white cotton gauze lies flat on the '
            'counter with a mound of pale gelatin paste in its centre, two '
            'old hands frozen mid-fold lifting two opposite corners of the '
            'gauze up toward each other. The cobalt jar sits out of focus '
            'behind. No face.',
  't1_take': 'The two old hands fold the four corners of the white gauze '
             'square up over the mound of pale paste and gather them into a '
             'small bundle, the cloth going translucent where the paste '
             'presses through.',
  'substancia': 'Pale cream paste bleeding grease-translucent through '
                'open-weave white cotton, the gauze darkening in a wet ring.',
  'usa_vicks': True},
 {'id': 'vk-c11',
  'curto': 'Amarrar a trouxinha de gaze com barbante',
  'fonte': 'construido',
  'cabe_em': ['cozinha', 'bancada_pia', 'peitoril_janela'],
  'vasilhame': 'Gathered white gauze bundle loaded with pale paste, a length '
               'of natural kitchen twine wrapped at its neck.',
  't1_img': 'Frozen macro: natural kitchen twine is cinched tight around the '
            'neck of a white gauze bundle swollen with pale paste, the knot '
            'half-pulled and the loose ends splayed, the cloth translucent '
            'and shining where the paste presses through. Two old hands '
            'holding the ends taut. No face.',
  't1_take': 'The two old hands pull the natural twine tight around the neck '
             'of the swollen gauze bundle, the cloth puckering into deep '
             'folds as the knot cinches down.',
  'substancia': 'White gauze puckering into wet translucent folds, pale '
                'grease-slick paste bulging inside the bundle.',
  'usa_vicks': True},
 {'id': 'vk-c12',
  'curto': 'Espremer a trouxinha de gaze sobre o pote',
  'fonte': 'construido',
  'cabe_em': ['borda_banheira', 'bancada_pia', 'prateleira_box'],
  'vasilhame': 'Wet white gauze bundle held over the open cobalt VapoRub '
               'jar, drips landing in the salve.',
  't1_img': 'Frozen macro: a wet white gauze bundle is squeezed in an old '
            'fist directly over the open cobalt VapoRub jar, milky liquid '
            'bulging through the weave and one thick drop frozen mid-fall '
            'above the white salve. Knuckles blanched with pressure. No '
            'face, no torso.',
  't1_take': 'The old fist squeezes the wet gauze bundle held over the open '
             'cobalt jar, and milky liquid presses out through the weave and '
             'runs down in slow threads into the white salve below.',
  'substancia': 'Milky translucent liquid bleeding through white weave and '
                'falling in slow ropey threads onto dense white salve.',
  'usa_vicks': True},
 {'id': 'vk-c13',
  'curto': 'Encher uma seringa culinaria sem agulha',
  'fonte': 'construido',
  'cabe_em': ['cozinha', 'bancada_pia', 'tampa_vaso'],
  'vasilhame': 'Clear plastic culinary syringe, no needle, wide blunt '
               'nozzle, dipped into a shallow glass bowl of pale slurry.',
  't1_img': 'Frozen macro: the blunt wide nozzle of a clear plastic culinary '
            'syringe sits submerged in a shallow glass bowl of pale slurry, '
            'the plunger drawn halfway back and the barrel half-filled with '
            'cloudy cream liquid, a bubble trapped at the top. Old hand on '
            'the plunger. No face.',
  't1_take': 'The old hand draws the plunger of the clear culinary syringe '
             'steadily back, and cloudy cream slurry climbs up the barrel in '
             'one smooth column with a single bubble riding at the top.',
  'substancia': 'Cloudy cream-coloured slurry, slightly viscous, climbing a '
                'clear barrel with one trapped bubble.',
  'usa_vicks': False},
 {'id': 'vk-c14',
  'curto': 'Extrudar a pasta da seringa em espiral no pote',
  'fonte': 'construido',
  'cabe_em': ['bancada_pia', 'cozinha', 'borda_banheira'],
  'vasilhame': 'Clear plastic culinary syringe held nozzle-down over the '
               'open cobalt VapoRub jar.',
  't1_img': 'Frozen macro: a clear plastic culinary syringe hangs '
            'nozzle-down over the open cobalt VapoRub jar, extruding a thick '
            'pale rope of paste that has already coiled into two glossy '
            'spiral rings on top of the white salve. Old hand pressing the '
            'plunger. No face.',
  't1_take': 'The old hand presses the syringe plunger down over the open '
             'cobalt jar, laying one continuous pale rope of paste in a '
             'widening spiral across the surface of the white salve.',
  'substancia': 'Thick glossy pale rope of paste coiling in even spirals '
                'over matte white salve, holding its shape without slumping.',
  'usa_vicks': True},
 {'id': 'vk-c15',
  'curto': 'Prensar a mistura numa forma de gelo de silicone',
  'fonte': 'construido',
  'cabe_em': ['cozinha', 'bancada_pia', 'peitoril_janela'],
  'vasilhame': 'Blue silicone ice cube tray, several wells already filled '
               'with pale paste, one being pressed.',
  't1_img': 'Frozen macro: an old thumb presses down into one well of a blue '
            'silicone ice cube tray packed with pale gelatin paste, the '
            'paste swelling up around the thumb pad, three neighbouring '
            'wells already filled flat and glossy. Torn sachet lying beside '
            'the tray. No face.',
  't1_take': 'The old thumb presses down hard into one well of the blue '
             'silicone ice tray, packing the pale paste flush to the rim so '
             'it bulges up around the thumb and settles glossy.',
  'substancia': 'Pale dense paste packed into square wells, glossy on top, '
                'bulging around the thumb pad and holding the print.',
  'usa_vicks': False},
 {'id': 'vk-c16',
  'curto': 'Prensar a pasta numa latinha de pomada de aluminio',
  'fonte': 'construido',
  'cabe_em': ['bancada_pia', 'borda_banheira', 'prateleira_box'],
  'vasilhame': 'Small round unlabelled aluminium salve tin, lid off beside '
               'it, being packed with pale paste.',
  't1_img': 'Frozen macro: two old fingers press a mound of pale paste flat '
            'into a small round aluminium salve tin, the surface '
            'half-smoothed and half-lumpy, the bare tin lid lying face-up '
            'beside it catching a hard glint of light. No face, no torso.',
  't1_take': 'The two old fingers press and smear the pale paste flat into '
             'the small aluminium salve tin, turning the mound into an even '
             "glossy disc that reaches the tin's edge.",
  'substancia': 'Pale paste packed into bare aluminium, half matte and '
                'lumpy, half smoothed to a wet glossy disc.',
  'usa_vicks': False},
 {'id': 'vk-c17',
  'curto': 'Raspar o po pra dentro do pote com um cartao plastico',
  'fonte': 'construido',
  'cabe_em': ['bancada_pia', 'cozinha', 'tampa_vaso'],
  'vasilhame': 'Blank white plastic card used as a scraper, open cobalt '
               'VapoRub jar sitting at the edge of the counter.',
  't1_img': 'Frozen macro: a blank white plastic card is held on edge '
            'against the wet counter, pushing a low drift of cream-white '
            'gelatin powder toward the lip of the open cobalt VapoRub jar, a '
            'first pinch of powder already tipping over the rim. Old hand on '
            'the card. No face.',
  't1_take': 'The old hand sweeps the blank white plastic card along the '
             'counter in one straight push, driving the drift of cream-white '
             'powder over the edge and into the open cobalt jar below.',
  'substancia': 'Cream-white gelatin powder in a low dune, dry and clumping '
                'at the card edge, spilling in a fine cascade.',
  'usa_vicks': True},
 {'id': 'vk-c18',
  'curto': 'Juntar o po derramado na bancada com o cartao',
  'fonte': 'construido',
  'cabe_em': ['cozinha', 'bancada_pia', 'peitoril_janela'],
  'vasilhame': 'Blank white plastic card scraping a spill of powder across '
               'the butcher-block counter, torn sachet lying flat nearby.',
  't1_img': 'Frozen top-down: a blank white plastic card is dragged across '
            'the scarred butcher-block counter, corralling a scattered spill '
            'of cream-white powder into a tight crescent ridge, clean '
            'streaked wood behind the card. Old veined hand, ring on one '
            'finger. No face.',
  't1_take': 'The old hand drags the blank white plastic card across the '
             'scarred wood counter, gathering the scattered white powder '
             'into one tight crescent ridge and leaving a clean streaked '
             'path behind it.',
  'substancia': 'Scattered cream-white powder swept into a tight crescent '
                'ridge on scarred pale wood, fine dust still hanging low.',
  'usa_vicks': False},
 {'id': 'vk-c19',
  'curto': 'Pincelar a pasta com pincel de silicone',
  'fonte': 'construido',
  'cabe_em': ['cozinha', 'bancada_pia', 'borda_banheira'],
  'vasilhame': 'Red-handled silicone pastry brush loaded with pale paste, '
               'open cobalt VapoRub jar below it.',
  't1_img': 'Frozen macro: a red-handled silicone pastry brush is loaded '
            'with pale glossy paste and held just above the open cobalt '
            'VapoRub jar, the bristles splayed and heavy with the paste, one '
            'thread of it stretching back down to the surface. Old hand on '
            'the handle. No face.',
  't1_take': 'The old hand sweeps the loaded silicone pastry brush back and '
             'forth across the mouth of the open cobalt jar, painting the '
             'pale paste into a flat glossy skin over the salve.',
  'substancia': 'Pale glossy paste combed into fine brush-stripes over white '
                'salve, wet and light-catching along every ridge.',
  'usa_vicks': True},
 {'id': 'vk-c20',
  'curto': 'Pincelar a pasta no proprio antebraco',
  'fonte': 'construido',
  'cabe_em': ['bancada_pia', 'borda_banheira', 'banquinho_madeira'],
  'vasilhame': 'Silicone pastry brush in one hand, open cobalt VapoRub jar '
               'standing on the surface behind the forearm.',
  't1_img': 'Frozen: a silicone pastry brush is pressed against the inner '
            'forearm of an older man, painting a wide wet stripe of pale '
            'paste along the skin over the veins, hair flattened under the '
            'stroke. Forearm and hands only, cropped at the elbow and the '
            'wrist. No face, no torso.',
  't1_take': 'The hand drags the loaded silicone brush in one long stroke up '
             'the inner forearm, laying a wide wet stripe of pale paste '
             'along the skin that beads and shines as it goes.',
  'substancia': 'Pale paste laid in a wide wet stripe on weathered skin, '
                'shining, flattening the arm hair under the stroke.',
  'usa_vicks': True},
 {'id': 'vk-c21',
  'curto': 'Mergulhar o pote fechado na agua da banheira',
  'fonte': 'construido',
  'cabe_em': ['borda_banheira', 'banquinho_madeira'],
  'vasilhame': 'Closed cobalt-blue VapoRub jar with turquoise cap, sinking '
               'below the surface of the bath water.',
  't1_img': 'Frozen underwater-line shot: the closed cobalt VapoRub jar is '
            'being pushed under the olive-green bath water by an old flat '
            'palm, a collar of silver bubbles frozen streaming off the '
            'turquoise cap, the surface caved in around the wrist. No face, '
            'no torso.',
  't1_take': 'The old flat palm pushes the closed cobalt jar down under the '
             'bath water and holds it there, a collar of silver bubbles '
             'streaming off the turquoise cap as the surface closes over the '
             'label.',
  'substancia': 'Turbid olive-green water swallowing a cobalt jar, silver '
                'bubble collar streaming up, white foam scum drifting at the '
                'surface.',
  'usa_vicks': True},
 {'id': 'vk-c22',
  'curto': 'Esfregar a mistura entre as duas palmas',
  'fonte': 'construido',
  'cabe_em': ['sob_o_jato',
              'bancada_pia',
              'borda_banheira',
              'prateleira_box'],
  'vasilhame': 'Open cobalt VapoRub jar set down on the surface below, its '
               'turquoise cap face-up beside it.',
  't1_img': 'Frozen: two old palms are pressed flat together and slid apart '
            'at an angle, a thick film of pale paste smeared between them, '
            'strands of it stretching in thin threads across the gap, powder '
            'still visible in the creases of the fingers. Hands only, no '
            'face, no torso.',
  't1_take': 'The two old palms press flat together and grind slowly against '
             'each other, working the pale paste into a thin warm film that '
             'stretches into fine threads as the hands part.',
  'substancia': 'Pale paste thinning into a warm translucent film between '
                'palms, drawing fine stretched threads, powder still caught '
                'in the skin creases.',
  'usa_vicks': True},
 {'id': 'vk-c23',
  'curto': 'Apertar o squeeze de mel sobre o pote',
  'fonte': 'construido',
  'cabe_em': ['cozinha', 'bancada_pia', 'borda_banheira', 'tampa_vaso'],
  'vasilhame': 'Clear plastic honey squeeze bottle with a pointed cap, held '
               'over the open cobalt VapoRub jar.',
  't1_img': 'Frozen macro: an old fist squeezes a clear plastic honey bottle '
            'held over the open cobalt VapoRub jar, the bottle walls dented '
            'in under the fingers and a thick unbroken amber thread frozen '
            'mid-fall onto the white powder below. No face, no torso.',
  't1_take': 'The old fist squeezes the clear plastic honey bottle over the '
             'open cobalt jar, and a thick amber thread runs down in one '
             'unbroken line and pools in a bright coil on top of the white '
             'powder.',
  'substancia': 'Thick golden amber honey in one unbroken thread, coiling '
                'bright and glassy over dull cream-white powder.',
  'usa_vicks': True},
 {'id': 'vk-c24',
  'curto': 'Apertar um squeeze de gel de babosa no pote',
  'fonte': 'construido',
  'cabe_em': ['bancada_pia', 'prateleira_box', 'cozinha'],
  'vasilhame': 'Green-tinted plastic squeeze bottle of clear aloe gel, '
               'nozzle down over the open cobalt VapoRub jar.',
  't1_img': 'Frozen macro: a green-tinted plastic squeeze bottle is inverted '
            'over the open cobalt VapoRub jar, a fat clear blob of aloe gel '
            'frozen halfway out of the nozzle and a glassy dome of it '
            'already sitting on the white salve. Old hand crushing the '
            'bottle. No face.',
  't1_take': 'The old hand crushes the green plastic bottle over the open '
             'cobalt jar, pushing out a fat clear blob of aloe gel that '
             'lands and spreads into a glassy dome across the white salve.',
  'substancia': 'Clear colourless aloe gel, glassy and jelly-firm, doming on '
                'matte white salve without sinking in.',
  'usa_vicks': True},
 {'id': 'vk-c25',
  'curto': 'Virar o pote de cabeca pra baixo sobre a palma',
  'fonte': 'construido',
  'cabe_em': ['bancada_pia', 'cozinha', 'borda_banheira', 'peitoril_janela'],
  'vasilhame': 'Open cobalt-blue VapoRub jar turned fully upside down above '
               'an open flat palm.',
  't1_img': 'Frozen: the open cobalt VapoRub jar is held fully upside down '
            'above an old open palm, the packed white salve hanging in the '
            'mouth of the jar and just beginning to sag out of it in a '
            'single lobe. Label reading upside down. No face, no torso.',
  't1_take': 'The old hand turns the open cobalt jar fully upside down over '
             'the flat palm and holds it there, the packed white salve '
             'sagging slowly out of the mouth in one heavy lobe.',
  'substancia': 'Packed white salve hanging inverted in the jar mouth, '
                'sagging in one heavy lobe, blue-grey flecks visible in the '
                'break.',
  'usa_vicks': True},
 {'id': 'vk-c26',
  'curto': 'Bater no fundo do pote invertido pra soltar a massa',
  'fonte': 'construido',
  'cabe_em': ['cozinha', 'bancada_pia', 'tampa_vaso'],
  'vasilhame': 'Inverted open cobalt VapoRub jar over a shallow clear glass '
               "bowl, the jar's base being struck.",
  't1_img': 'Frozen macro: an old palm strikes the flat base of the inverted '
            'cobalt VapoRub jar held over a shallow clear glass bowl, and '
            'the packed white plug of salve is frozen dropping free in '
            'mid-air between jar and bowl. Motion blur on the striking hand. '
            'No face.',
  't1_take': 'The old palm slaps the flat base of the inverted cobalt jar '
             'held over the glass bowl, and the packed white plug of salve '
             'breaks loose and drops out whole into the bowl.',
  'substancia': 'A whole packed plug of white salve, edges scored by the jar '
                'wall, dropping free and flattening on impact.',
  'usa_vicks': True},
 {'id': 'vk-c27',
  'curto': 'Medir o po com colher dosadora de metal',
  'fonte': 'construido',
  'cabe_em': ['cozinha', 'bancada_pia', 'peitoril_janela', 'tampa_vaso'],
  'vasilhame': 'Small stainless measuring spoon on a ring of nested spoons, '
               'heaped with cream-white powder.',
  't1_img': 'Frozen macro: a small stainless measuring spoon on a ring of '
            'nested spoons is held heaped and overflowing with cream-white '
            'gelatin powder, loose grains spilling off both sides, the torn '
            'sachet lying open below. Old veined hand on the ring. No face.',
  't1_take': 'The old hand dips the small stainless measuring spoon into the '
             'torn sachet and lifts it out heaped and overflowing, loose '
             'cream-white grains spilling off both sides as it rises.',
  'substancia': 'Cream-white gelatin powder heaped over a bright steel bowl, '
                'dry and free-running, grains shedding off the edges.',
  'usa_vicks': False},
 {'id': 'vk-c28',
  'curto': 'Nivelar a colher dosadora com a borda de um cartao',
  'fonte': 'construido',
  'cabe_em': ['cozinha', 'bancada_pia', 'tampa_vaso'],
  'vasilhame': 'Heaped stainless measuring spoon being struck level by the '
               'edge of a blank white plastic card.',
  't1_img': 'Frozen macro: the straight edge of a blank white plastic card '
            'is drawn across the rim of a heaped stainless measuring spoon, '
            'half the mound already shaved off flat and a small avalanche of '
            'cream-white powder frozen falling away. Two old hands. No face.',
  't1_take': 'The old hand draws the edge of the blank white card straight '
             'across the rim of the heaped measuring spoon, shaving the '
             'mound level and sending the excess powder falling away in a '
             'small avalanche.',
  'substancia': 'Cream-white powder shaved dead level at a steel rim, the '
                'shaved excess falling in a fine dry sheet.',
  'usa_vicks': False},
 {'id': 'vk-c29',
  'curto': 'Despejar de um copinho dosador de xarope',
  'fonte': 'construido',
  'cabe_em': ['bancada_pia', 'tampa_vaso', 'borda_banheira'],
  'vasilhame': 'Small ribbed clear plastic dosing cup from a syrup bottle, '
               'tipped over the open cobalt VapoRub jar.',
  't1_img': 'Frozen macro: a small ribbed clear plastic dosing cup is tipped '
            'almost vertical over the open cobalt VapoRub jar, a slug of '
            'cloudy pale liquid frozen leaving its lip and a bright meniscus '
            'still clinging inside the cup. Old fingers pinching the cup. No '
            'face.',
  't1_take': 'The old fingers tip the small ribbed dosing cup over the open '
             'cobalt jar, and the cloudy pale liquid slides out over the lip '
             'in one slug and sinks into the white salve.',
  'substancia': 'Cloudy pale liquid, slightly thick, sliding out of ribbed '
                'plastic and darkening a crater in the white salve.',
  'usa_vicks': True},
 {'id': 'vk-c30',
  'curto': 'Moer o po num almofariz de pedra',
  'fonte': 'construido',
  'cabe_em': ['cozinha', 'peitoril_janela', 'bancada_pia'],
  'vasilhame': 'Heavy grey stone mortar with a stubby pestle, cream-white '
               'powder banked in its bowl.',
  't1_img': 'Frozen macro: a stubby grey stone pestle is pressed into the '
            'bank of cream-white powder inside a heavy stone mortar, a '
            'smeared crescent of crushed powder pushed up the bowl wall, '
            'dust hanging in the raking window light. Old hand gripping the '
            'pestle. No face.',
  't1_take': 'The old hand grinds the stone pestle in slow heavy circles '
             'around the mortar bowl, crushing the cream-white powder finer '
             'and pushing a smeared crescent of it up the stone wall.',
  'substancia': 'Cream-white powder crushed finer against rough grey stone, '
                'a pale dust haze rising in the raking light.',
  'usa_vicks': False},
 {'id': 'vk-c31',
  'curto': 'Empurrar o po por um coador de cha com a colher',
  'fonte': 'construido',
  'cabe_em': ['cozinha', 'bancada_pia', 'peitoril_janela'],
  'vasilhame': 'Round chrome tea strainer resting on the mouth of a tall '
               'clear glass, spoon pressing powder through the mesh.',
  't1_img': 'Frozen macro: the back of a stainless spoon is pressed hard '
            'into a mound of pale paste sitting in a round chrome tea '
            'strainer balanced on the mouth of a tall clear glass, fine '
            'worms of paste extruding through the mesh underneath. Old hand '
            'on the spoon. No face.',
  't1_take': 'The old hand presses the back of the stainless spoon down into '
             'the mound of pale paste in the chrome tea strainer, forcing it '
             'through the mesh in fine worms that drop into the glass below.',
  'substancia': 'Pale paste extruded through fine chrome mesh into short '
                'pale worms that drop and coil in the glass.',
  'usa_vicks': False},
 {'id': 'vk-c32',
  'curto': 'Tampar a boca do pote com a palma e chacoalhar',
  'fonte': 'construido',
  'cabe_em': ['sob_o_jato', 'prateleira_box', 'borda_banheira', 'nicho_box'],
  'vasilhame': 'Open cobalt-blue VapoRub jar sealed by a bare palm clamped '
               'over its mouth.',
  't1_img': 'Frozen: an old bare palm is clamped hard over the mouth of the '
            'open cobalt VapoRub jar, the other hand gripping the base, the '
            'whole jar tilted mid-shake with a puff of white powder escaping '
            'around the edge of the palm. Wrists only, no face, no torso.',
  't1_take': 'The old palm clamps down over the mouth of the open cobalt jar '
             'and both hands shake it hard up and down, puffs of white '
             'powder escaping around the edge of the palm on each stroke.',
  'substancia': 'Cream-white powder blooming in puffs around a sealing palm, '
                'packed white salve slamming loose inside the jar.',
  'usa_vicks': True},
 {'id': 'vk-c33',
  'curto': 'Cortar o sache com tesourinha',
  'fonte': 'construido',
  'cabe_em': ['bancada_pia', 'cozinha', 'tampa_vaso', 'peitoril_janela'],
  'vasilhame': 'Sealed foil gelatin sachet held taut, small stainless '
               'scissors biting into its top edge.',
  't1_img': 'Frozen macro: small stainless scissors are closed halfway '
            'across the top edge of a taut foil gelatin sachet, a clean '
            'straight cut already opened for an inch and a curl of foil '
            'peeling back, the cobalt jar waiting below out of focus. Two '
            'old hands. No face.',
  't1_take': 'The two old hands close the small stainless scissors across '
             'the top of the taut foil sachet in one long cut, the severed '
             'strip of foil curling away and the cut edge springing open.',
  'substancia': 'Matte silver foil parting in a clean straight cut, a first '
                'spill of cream-white powder catching in the crease.',
  'usa_vicks': True},
 {'id': 'vk-c34',
  'curto': 'Bater o fundo do pote na bancada pra assentar o po',
  'fonte': 'construido',
  'cabe_em': ['bancada_pia', 'cozinha', 'tampa_vaso', 'peitoril_janela'],
  'vasilhame': 'Open cobalt-blue VapoRub jar being knocked down onto the '
               'hard counter, powder mounded inside it.',
  't1_img': 'Frozen: the open cobalt VapoRub jar is struck flat down on the '
            'hard counter by an old hand, a ring of cream-white powder '
            'frozen jumping off the mound inside and hanging in the air just '
            'above the rim. Slight motion blur on the jar. No face.',
  't1_take': 'The old hand knocks the open cobalt jar flat down on the '
             'counter three times, the mounded powder inside jumping and '
             'settling flatter with every strike.',
  'substancia': 'Mounded cream-white powder jumping loose and levelling '
                'flat, a fine dust ring hanging over the jar rim.',
  'usa_vicks': True},
 {'id': 'vk-c35',
  'curto': 'Girar o pote em circulos sobre a bancada molhada',
  'fonte': 'construido',
  'cabe_em': ['bancada_pia',
              'borda_banheira',
              'tampa_vaso',
              'prateleira_box'],
  'vasilhame': 'Open cobalt-blue VapoRub jar swirled flat on a wet white '
               'counter, wet rings trailing behind it.',
  't1_img': 'Frozen top-down: the open cobalt VapoRub jar is swirled flat '
            'across the wet white counter, two overlapping wet rings smeared '
            'behind it and the pale slurry inside tilted up one wall in a '
            'frozen wave. Old hand loosely cupping the jar. No face.',
  't1_take': 'The old hand swirls the open cobalt jar in flat circles on the '
             'wet counter, the pale slurry inside riding up one wall in a '
             'slow wave and smearing wet rings across the surface behind it.',
  'substancia': 'Pale slurry riding up the jar wall in a slow wave, wet '
                'smeared rings glossing the white counter beneath.',
  'usa_vicks': True},
 {'id': 'vk-c36',
  'curto': 'Selar a boca do pote com filme plastico',
  'fonte': 'construido',
  'cabe_em': ['cozinha', 'bancada_pia', 'peitoril_janela'],
  'vasilhame': 'Open cobalt-blue VapoRub jar with a sheet of clear cling '
               'film stretched taut over its mouth.',
  't1_img': 'Frozen macro: a sheet of clear cling film is stretched '
            'drum-tight over the mouth of the open cobalt VapoRub jar, two '
            'old thumbs pressing it down around the threads, condensation '
            'already fogging the film and the pale mixture distorted '
            'underneath. No face.',
  't1_take': 'The two old thumbs press the sheet of clear cling film down '
             'over the mouth of the cobalt jar and drag it tight around the '
             'threads until the film pulls drum-flat and fogs from below.',
  'substancia': 'Clear film pulled drum-tight and fogging with condensation, '
                'the pale mixture blurred and swelling underneath.',
  'usa_vicks': True},
 {'id': 'vk-c37',
  'curto': 'Borrifar agua no po com um borrifador',
  'fonte': 'construido',
  'cabe_em': ['prateleira_box', 'nicho_box', 'bancada_pia', 'cozinha'],
  'vasilhame': 'Small clear plastic trigger spray bottle aimed down into the '
               'open cobalt VapoRub jar.',
  't1_img': 'Frozen macro: a small clear plastic trigger spray bottle is '
            'aimed down into the open cobalt VapoRub jar, a cone of fine '
            'mist frozen in the air and the cream-white powder already '
            'pocked with dark wet freckles where the first droplets landed. '
            'Old finger on the trigger. No face.',
  't1_take': 'The old finger pumps the trigger of the small spray bottle '
             'over the open cobalt jar, and a fine cone of mist falls until '
             'the cream-white powder darkens into a freckled damp crust.',
  'substancia': 'Cream-white powder pocked with dark wet freckles under a '
                'fine mist, crusting damp and glossy where the droplets '
                'land.',
  'usa_vicks': True},
 {'id': 'vk-c38',
  'curto': 'Pingar agua no po com um conta-gotas',
  'fonte': 'construido',
  'cabe_em': ['bancada_pia', 'cozinha', 'tampa_vaso', 'peitoril_janela'],
  'vasilhame': 'Amber glass dropper bottle with a rubber bulb, held above '
               'the open cobalt VapoRub jar.',
  't1_img': 'Frozen macro: an amber glass dropper is held above the open '
            'cobalt VapoRub jar with one fat clear drop frozen hanging off '
            'the tip and two dark craters already punched into the '
            'cream-white powder below. Old fingers squeezing the rubber '
            'bulb. No face.',
  't1_take': 'The old fingers squeeze the rubber bulb of the amber glass '
             'dropper over the open cobalt jar, releasing single fat drops '
             'that punch dark wet craters one by one into the cream-white '
             'powder.',
  'substancia': 'Single fat clear drops punching dark wet craters into dry '
                'cream-white powder, each crater rimmed with a swollen ring.',
  'usa_vicks': True},
 {'id': 'vk-c39',
  'curto': 'Mexer com o cabo da colher em vez da concha',
  'fonte': 'construido',
  'cabe_em': ['bancada_pia',
              'borda_banheira',
              'tampa_vaso',
              'prateleira_box'],
  'vasilhame': 'Stainless tablespoon held backwards, its narrow handle sunk '
               'into the open cobalt VapoRub jar.',
  't1_img': 'Frozen macro: a stainless tablespoon is held backwards with its '
            'narrow handle sunk deep into the open cobalt VapoRub jar, the '
            'bowl of the spoon pointing up and out of frame, a tight swirl '
            'carved into the pale mixture around the handle. Old hand '
            'gripping the bowl. No face.',
  't1_take': 'The old hand grips the bowl of the tablespoon and stirs with '
             'the narrow handle end sunk into the cobalt jar, cutting a '
             'tight deep swirl through the pale mixture.',
  'substancia': 'Pale mixture cut into a tight deep swirl by a thin steel '
                'handle, ridges standing sharp and wet.',
  'usa_vicks': True},
 {'id': 'vk-c40',
  'curto': 'Desenhar uma espiral com um palito de churrasco',
  'fonte': 'construido',
  'cabe_em': ['cozinha', 'bancada_pia', 'peitoril_janela', 'tampa_vaso'],
  'vasilhame': 'Bare wooden skewer drawn through pale slurry in a shallow '
               'clear glass bowl.',
  't1_img': 'Frozen top-down macro: a bare wooden skewer is dragged through '
            'pale slurry in a shallow clear glass bowl, trailing one clean '
            'spiral groove from the centre outward, an amber thread pulled '
            'into a feathered marble along the line. Old hand pinching the '
            'skewer. No face.',
  't1_take': 'The old hand drags the bare wooden skewer slowly outward '
             'through the pale slurry in one continuous spiral, feathering '
             'an amber thread into a marbled ribbon behind the tip.',
  'substancia': 'Pale slurry marbled with a feathered amber thread, one '
                'clean spiral groove holding its shape on the surface.',
  'usa_vicks': False},
 {'id': 'vk-c41',
  'curto': 'Mexer com o cabo de uma escova de dentes',
  'fonte': 'construido',
  'cabe_em': ['bancada_pia',
              'borda_banheira',
              'tampa_vaso',
              'prateleira_box'],
  'vasilhame': 'White-and-blue toothbrush held bristles-up, its handle end '
               'stirring the open cobalt VapoRub jar.',
  't1_img': 'Frozen macro: a white-and-blue toothbrush is held bristles-up '
            'with its flat handle end plunged into the open cobalt VapoRub '
            'jar, pale paste climbing an inch up the plastic and a deep '
            'furrow ploughed through the surface. Old hand gripping the '
            'brush head. No face.',
  't1_take': 'The old hand grips the toothbrush by its head and ploughs the '
             'flat handle end back and forth through the pale mixture in the '
             'cobalt jar, turning up a deep glossy furrow.',
  'substancia': 'Pale mixture ploughed into a deep glossy furrow, climbing '
                'an inch up white-and-blue plastic and hanging there.',
  'usa_vicks': True},
 {'id': 'vk-c42',
  'curto': 'Alisar a superficie com as costas da colher',
  'fonte': 'construido',
  'cabe_em': ['bancada_pia', 'cozinha', 'borda_banheira', 'nicho_box'],
  'vasilhame': 'Stainless tablespoon laid back-down across the surface of '
               'the open cobalt VapoRub jar.',
  't1_img': 'Frozen macro straight down: the back of a stainless tablespoon '
            'is pressed flat across the pale mixture in the open cobalt '
            'VapoRub jar, half the surface already burnished mirror-smooth '
            'and the other half still ridged and lumpy. Old hand on the '
            'handle. No face.',
  't1_take': 'The old hand presses the back of the stainless tablespoon flat '
             'onto the pale mixture in the cobalt jar and sweeps it in one '
             'slow arc, burnishing the ridged surface to a mirror-smooth '
             'skin.',
  'substancia': 'Pale mixture burnished from ridged and matte into a '
                'mirror-smooth wet skin that holds the light in one flat '
                'sheet.',
  'usa_vicks': True},
 {'id': 'vk-c43',
  'curto': 'Prensar o po com o fundo de um copo de vidro',
  'fonte': 'construido',
  'cabe_em': ['cozinha', 'bancada_pia', 'peitoril_janela'],
  'vasilhame': 'Heavy clear glass tumbler pressed base-down into powder '
               'banked in a shallow glass bowl.',
  't1_img': 'Frozen macro: the heavy base of a clear glass tumbler is '
            'pressed down into cream-white powder banked in a shallow glass '
            'bowl, the powder compacted into a flat pale disc under the '
            'glass and a fine collar of loose dust puffed out around the '
            'rim. Old hand on top. No face.',
  't1_take': 'The old hand pushes the heavy glass tumbler base-down into the '
             'banked cream-white powder and leans on it, compacting the '
             'powder into a flat pale disc and puffing a collar of dust out '
             'around the rim.',
  'substancia': 'Cream-white powder compacted into a flat chalky disc under '
                'thick glass, a fine dust collar puffed out at the rim.',
  'usa_vicks': False},
 {'id': 'vk-c44',
  'curto': 'Furar um poco no centro da massa com o polegar',
  'fonte': 'construido',
  'cabe_em': ['bancada_pia', 'borda_banheira', 'prateleira_box', 'nicho_box'],
  'vasilhame': 'Open cobalt-blue VapoRub jar held up close to the lens, its '
               'turquoise cap face-up beside it.',
  't1_img': 'Frozen macro: an old thumb is pressed deep into the centre of '
            'the packed white salve in the open cobalt VapoRub jar, a clean '
            'round well sunk to the bottom of the jar and the displaced '
            'salve pushed up into a raised collar around it. No face, no '
            'torso.',
  't1_take': 'The old thumb presses straight down into the centre of the '
             'packed white salve in the cobalt jar and screws once, sinking '
             'a clean round well to the bottom and raising a collar of salve '
             'around it.',
  'substancia': 'Packed white salve sunk into a clean round well down to '
                'blue glass, a raised collar of displaced salve standing '
                'around the hole.',
  'usa_vicks': True},
 {'id': 'vk-c45',
  'curto': 'Correr o dedo pela borda interna do pote',
  'fonte': 'construido',
  'cabe_em': ['bancada_pia',
              'prateleira_box',
              'borda_banheira',
              'sob_o_jato'],
  'vasilhame': 'Open cobalt-blue VapoRub jar tilted toward the lens, index '
               'finger tracing its inner rim.',
  't1_img': 'Frozen macro: an old index finger is dragged around the inner '
            'rim of the tilted open cobalt VapoRub jar, gathering a thick '
            'ridge of pale paste ahead of the fingertip and leaving a clean '
            'glossy stripe of blue glass behind it. No face, no torso.',
  't1_take': 'The old index finger runs slowly all the way around the inner '
             'rim of the tilted cobalt jar, pushing a growing ridge of pale '
             'paste ahead of it and leaving a clean glossy stripe of blue '
             'glass behind.',
  'substancia': 'Pale paste rolled into a growing ridge ahead of a '
                'fingertip, bare blue glass left glossy and streaked behind '
                'it.',
  'usa_vicks': True},
 {'id': 'vk-c46',
  'curto': 'Extrudar a pasta num espremedor de alho',
  'fonte': 'construido',
  'cabe_em': ['cozinha', 'bancada_pia', 'peitoril_janela'],
  'vasilhame': 'Heavy chrome garlic press squeezed over a shallow clear '
               'glass bowl, pale strands falling into it.',
  't1_img': 'Frozen macro: a heavy chrome garlic press is clamped shut over '
            'a shallow clear glass bowl and pale paste is frozen extruding '
            'through the holes in a dozen short worms, several already '
            'dropped and coiled in the bowl below. Old fist white-knuckled '
            'on the handles. No face.',
  't1_take': 'The old fist clamps the heavy chrome garlic press shut over '
             'the glass bowl, and pale paste squeezes out through the holes '
             'in a dozen short worms that break off and coil in the bowl.',
  'substancia': 'Pale paste extruded through chrome holes into short pale '
                'worms, wet and glossy, coiling loose as they drop.',
  'usa_vicks': False},
 {'id': 'vk-c47',
  'curto': 'Bater a mistura com um mini fouet',
  'fonte': 'construido',
  'cabe_em': ['cozinha', 'bancada_pia', 'tampa_vaso', 'borda_banheira'],
  'vasilhame': 'Small stainless balloon whisk worked inside a heavy beige '
               'ceramic mug of pale slurry.',
  't1_img': 'Frozen macro: a small stainless balloon whisk is lifted half '
            'out of a heavy beige ceramic mug, its wires webbed with pale '
            'foam and dragging a thin curtain of it back down into the '
            'slurry, a ring of froth risen at the mug wall. Old hand on the '
            'handle. No face.',
  't1_take': 'The old hand beats the small stainless whisk fast inside the '
             'beige ceramic mug, and the pale slurry lightens and climbs '
             'into a froth that rings the inside of the mug.',
  'substancia': 'Pale slurry beaten light and frothing, fine bubbles webbing '
                'steel wires and a froth ring climbing the mug wall.',
  'usa_vicks': False},
 {'id': 'vk-c49',
  'curto': 'Rolar a mistura numa bolinha entre os dedos',
  'fonte': 'construido',
  'cabe_em': ['bancada_pia',
              'cozinha',
              'borda_banheira',
              'banquinho_madeira'],
  'vasilhame': 'Open cobalt-blue VapoRub jar sitting below, a small pale '
               'ball rolled between thumb and two fingers.',
  't1_img': 'Frozen macro: a small pale ball of paste sits pinched between '
            'an old thumb and two fingers held up to the lens, its surface '
            'tacky and slightly ridged with fingerprints, a faint powder '
            'bloom still dusting one side. The open cobalt jar waits out of '
            'focus below. No face.',
  't1_take': 'The old thumb and two fingers roll the lump of pale paste in '
             'tight circles until it firms into a small smooth ball, the '
             'fingerprints polishing out and a faint powder bloom lifting '
             'off it.',
  'substancia': 'Pale paste rolled firm and tacky into a small smooth ball, '
                'faint powder bloom on one side, fingerprints polishing '
                'away.',
  'usa_vicks': True},
 {'id': 'vk-c50',
  'curto': 'Raspar o resto de creme da tampa turquesa com a colher',
  'fonte': 'construido',
  'cabe_em': ['borda_banheira', 'bancada_pia', 'prateleira_box', 'nicho_box'],
  'vasilhame': 'Turquoise VapoRub screw cap lying face-up with salve pooled '
               'inside it, stainless spoon scraping it out.',
  't1_img': 'Frozen macro: the edge of a stainless spoon is dragged across '
            'the inside of the turquoise VapoRub screw cap lying face-up, '
            'lifting the pooled white salve into a thick curl on the spoon '
            'and leaving a clean arc of bare turquoise plastic behind. Old '
            'hand steadying the cap. No face.',
  't1_take': 'The old hand drags the edge of the stainless spoon across the '
             'inside of the face-up turquoise cap, lifting the pooled white '
             'salve into one thick curl and leaving a clean arc of bare '
             'plastic behind.',
  'substancia': 'White salve pooled in a turquoise cap, lifting off in one '
                'thick glossy curl and leaving bare shining plastic behind.',
  'usa_vicks': True}]

# ⭐ AS PESSOAS — 100 entradas. O operador tornou a PRESENCA sorteavel:
# so' as maos, maos e antebraco, tronco, ou corpo inteiro.
HOMENS = [{'id': 'maos_v01_pelos_escuros',
  'curto': 'mãos mais jovens do v01, antebraço peludo sem manchas',
  'fonte': 'lido',
  'presenca': 'maos_antebraco',
  'idade': 52,
  'etnia': 'branco',
  'desc': 'Hands and right forearm of a white man in his early fifties, '
          'notably younger than the other hands in this world. Fair skin '
          'with no liver spots at all. Dark brown body hair covers the '
          'forearm from below the elbow down to the wrist bone, thinning '
          'where it meets the back of the hand. Two cord-like veins run '
          'diagonally across the back of the hand and swell when he grips. '
          'Knuckles are pronounced and slightly reddened. Square-cut short '
          'nails, clean, one thumbnail with a faint horizontal dent. Bare '
          'ring finger, no band and no pale mark where one would sit.',
  'roupa': 'No sleeve enters frame: the forearm is bare to just below the '
           'elbow.'},
 {'id': 'maos_v02_manchas_senis',
  'curto': 'mãos velhas manchadas do v02, pele finíssima',
  'fonte': 'lido',
  'presenca': 'maos',
  'idade': 71,
  'etnia': 'branco',
  'desc': 'Hands of an elderly white man, skin thin as paper and deeply '
          'crumpled over the back of the hand. Tendons and veins stand up in '
          'raised ridges under the skin, so the shape of every bone reads '
          'through. Brown liver spots of uneven size are scattered across '
          'the backs of both hands, the largest one the size of a dime just '
          'behind the index knuckle. Fingertips slightly flattened, nails '
          'ridged lengthwise and cut very short. No ring, no watch.',
  'roupa': ''},
 {'id': 'costas_v03_camisa_jeans',
  'curto': 'grisalho de camiseta jeans, de costas, passando creme na nuca',
  'fonte': 'lido',
  'presenca': 'tronco',
  'idade': 58,
  'etnia': 'branco',
  'desc': 'White man photographed from behind and three-quarters, never '
          'facing the lens. Short salt-and-pepper hair, cropped close at the '
          'neck, with a white stubble line running down the nape. His face '
          'reads only as a partial profile: a heavy jaw with white stubble, '
          'a straight nose seen edge-on, one ear with a thick attached lobe. '
          'Broad back, slightly rounded shoulders, forearms with dark hair. '
          'The white smear of ointment stays visible on the back of his '
          'neck.',
  'roupa': 'Faded denim-blue cotton t-shirt, worn soft, with the back hem '
           'rolled and pushed up so the small of his back and the black '
           'elastic waistband beneath show.'},
 {'id': 'maos_v03_alianca_direita',
  'curto': 'mãos enrugadas com aliança dourada no anelar DIREITO',
  'fonte': 'lido',
  'presenca': 'maos',
  'idade': 73,
  'etnia': 'branco',
  'desc': 'Hands of an old white man, very heavily wrinkled, with large '
          'brown liver spots across both backs of hand and a cluster of '
          'smaller ones on the thumb web. A plain yellow gold wedding band '
          'sits on the ring finger of the RIGHT hand, worn thin and slightly '
          'oval from decades of use, with a dull scratched face. Knuckles '
          'are broad, the middle finger sits a little crooked. Nails thick '
          'and yellowish, trimmed straight across.',
  'roupa': ''},
 {'id': 'maos_v04_unhas_limpas',
  'curto': 'mãos idosas de articulações grossas e unhas curtas limpas',
  'fonte': 'lido',
  'presenca': 'maos',
  'idade': 70,
  'etnia': 'branco',
  'desc': 'Hands of an elderly white man with thick, enlarged finger joints, '
          'each knuckle noticeably wider than the finger above and below it. '
          'Deep dorsal veins branch in a Y behind the wrist. Scattered brown '
          'age spots, more on the left hand than the right. Nails cut very '
          'short and scrupulously clean, the cuticles pushed back and '
          'slightly dry. Palms callused at the base of the fingers. No '
          'jewellery of any kind.',
  'roupa': ''},
 {'id': 'maos_v05_fio_creme',
  'curto': 'mãos de pele fina, rugas profundas, dedo com fio pegajoso',
  'fonte': 'lido',
  'presenca': 'maos',
  'idade': 68,
  'etnia': 'branco',
  'desc': 'Hands of an elderly white man with paper-thin skin and deep '
          'parallel wrinkles across the back of the hand, folding when he '
          'closes his fist. Thick veins run over the tendons and are visible '
          'even at rest. Brown age spots, freckle-sized, concentrated toward '
          'the wrist. The index finger is the working finger: its pad is '
          'slightly wider and the nail on it is shorter than the others. A '
          'small hard callus sits on the side of the middle finger where a '
          'pen rests.',
  'roupa': ''},
 {'id': 'maos_v06_dedos_grossos',
  'curto': 'mãos que entram por baixo do quadro, dedos grossos e unhas '
           'curtas',
  'fonte': 'lido',
  'presenca': 'maos',
  'idade': 75,
  'etnia': 'branco',
  'desc': 'Hands of a white man in his mid-seventies, entering from the '
          'bottom edge of frame. Backs of the hands are deeply wrinkled with '
          'a crosshatch of fine lines; veins are raised and blue-grey. '
          'Fingers are thick and blunt-tipped, with wide flat nails cut '
          'short and one thumbnail that is markedly thicker and slightly '
          'yellowed than the rest. Brown liver spots across both hands. A '
          'pale narrow groove at the base of the left ring finger where a '
          'ring used to sit, but no ring now.',
  'roupa': ''},
 {'id': 'maos_v07_molhadas',
  'curto': 'mãos molhadas e brilhantes sob o chuveiro, sem aliança',
  'fonte': 'lido',
  'presenca': 'maos',
  'idade': 66,
  'etnia': 'branco',
  'desc': 'Hands of an elderly white man, wet and shining, with droplets '
          'beading on the back of the hand and running down the wrist. Skin '
          'very wrinkled, the wet folds catching the light. Large knuckles, '
          'prominent dorsal veins, brown age spots visible through the '
          'water. Nails short, clean, with water sitting in the nail folds. '
          'Nothing on the wrists at all: no watch, no band, no bracelet. '
          'Only the hands and, at most, the wrist bone enter frame.',
  'roupa': ''},
 {'id': 'maos_v08_relogio_preto',
  'curto': 'mãos negras com aliança dourada e relógio preto de pulseira '
           'larga',
  'fonte': 'lido',
  'presenca': 'maos_antebraco',
  'idade': 72,
  'etnia': 'negro',
  'desc': 'Hands and forearms of an elderly African-American man. Deep brown '
          'skin, heavily wrinkled over the knuckles, which read lighter than '
          'the surrounding skin. Veins stand out in a raised network across '
          'the back of the hand. Thick blunt fingers, short clean nails with '
          'pale half-moons. A yellow gold wedding band on the left ring '
          'finger. On the left wrist a black watch on a wide leather strap, '
          'the strap softened and cracked at the fold. The right forearm '
          'shows almost to the elbow, with sparse grey hair.',
  'roupa': 'Sleeves out of frame; forearms bare, a rolled dark cuff just '
           'visible at the very edge on the right.'},
 {'id': 'tronco_v09_peito_nu',
  'curto': 'homem negro de tronco nu com pelos grisalhos, rosto cortado no '
           'queixo',
  'fonte': 'lido',
  'presenca': 'tronco',
  'idade': 63,
  'etnia': 'negro',
  'desc': 'Bare torso of an African-American man in his early sixties. Chest '
          'hair is thick and mostly grey, spreading across both pectorals '
          'and thinning down the middle of a soft, rounded belly. Shoulders '
          'and upper arms are heavy and thick. The frame cuts the head above '
          'the mouth: only the chin and lower lip show, with grey stubble '
          'over a broad, square jaw and a deep crease running from the '
          'corner of the mouth. Yellow gold wedding band on the left hand. A '
          'shine of white ointment sits smeared across the chest.',
  'roupa': 'Navy fleece sweatpants sitting low on the hips; no shirt.'},
 {'id': 'costas_v10_camiseta_azul',
  'curto': 'narrador negro de cabelo raspado grisalho, camiseta azul '
           'desbotada',
  'fonte': 'lido',
  'presenca': 'tronco',
  'idade': 68,
  'etnia': 'negro',
  'desc': 'African-American man shot from behind and three-quarters, head '
          'lowered. Hair shaved down very short and gone white-grey across '
          'the crown, with the hairline receding in two soft points at the '
          'temples. White stubble on the chin and along the jaw, visible in '
          'the sliver of profile. Thick neck, broad sloping shoulders, ears '
          'set close to the skull. Yellow gold wedding band on the left ring '
          'finger. His right hand is up at the back of his own neck.',
  'roupa': 'Faded blue-grey short-sleeve cotton t-shirt, collar stretched '
           'out of shape, one shoulder seam slightly frayed.'},
 {'id': 'maos_v10_escuras_manchadas',
  'curto': 'mãos negras muito enrugadas com manchas claras',
  'fonte': 'lido',
  'presenca': 'maos',
  'idade': 70,
  'etnia': 'negro',
  'desc': 'Hands of an elderly African-American man. Very deep wrinkles '
          'across the back of the hand, the skin loose enough to lift. Pale, '
          'lighter-toned age spots scattered over the darker skin, '
          'especially behind the middle and ring knuckles. Veins raised and '
          'clearly drawn under the skin. The palms and fingertips are '
          'notably lighter than the backs. Nails short, thick, with '
          'pronounced pale lunulae. Yellow gold wedding band on the left '
          'ring finger.',
  'roupa': ''},
 {'id': 'maos_v11_nos_enrugados',
  'curto': 'mãos brancas de 67 com manchas marrons e dedos grossos',
  'fonte': 'lido',
  'presenca': 'maos',
  'idade': 67,
  'etnia': 'branco',
  'desc': 'Hands of a white man of sixty-seven. Fair skin with brown liver '
          'spots across the back of both hands, one of them long and '
          'irregular, running behind the ring knuckle. Veins clearly raised. '
          'Fingers thick with wrinkled skin gathered over each knuckle like '
          'a small cuff. Nails cut short and clean, filed square, one index '
          'nail slightly torn at the corner. Fine white hairs on the first '
          'segment of each finger. No ring, no watch.',
  'roupa': ''},
 {'id': 'maos_v12_dedos_longos',
  'curto': 'mãos de dedos longos com anel no dedo mínimo',
  'fonte': 'lido',
  'presenca': 'maos',
  'idade': 69,
  'etnia': 'branco',
  'desc': 'Hands of an elderly white man with unusually long, narrow '
          'fingers. Skin thin and pale with brown liver spots and a '
          'purple-grey bruise the size of a thumbprint on the back of the '
          'left hand. Veins extremely prominent, standing proud of the skin '
          'all the way to the knuckles. A small worn silver ring sits on the '
          'little finger of the left hand, too loose, turned slightly to one '
          'side. Nails narrow, long-bedded, trimmed close.',
  'roupa': ''},
 {'id': 'maos_v13_segura_cubo',
  'curto': 'mãos de rugas profundas erguendo o cubo até a lente',
  'fonte': 'lido',
  'presenca': 'maos',
  'idade': 74,
  'etnia': 'branco',
  'desc': 'Hand of a white man in his mid-seventies raised close to the '
          'lens, filling half the frame. Skin thin, with deep folds running '
          'across the back of the hand and gathering into loose crepe over '
          'the wrist. Veins very prominent and slightly winding. Knuckles '
          'marked and reddened, with a small dry crack in the skin over the '
          'index knuckle. Brown liver spots. Nails short with pronounced '
          'vertical ridging, one thumbnail slightly split at the free edge.',
  'roupa': ''},
 {'id': 'maos_v14_molhadas_nos',
  'curto': 'mãos molhadas de veias grossas, nós marcados',
  'fonte': 'lido',
  'presenca': 'maos',
  'idade': 72,
  'etnia': 'branco',
  'desc': 'Wet hands of an elderly white man, water clinging in fat droplets '
          'along the tendons. Skin wrinkled and reddened by heat, the '
          'fingertips slightly pruned. Thick blue veins run in a raised fork '
          'over the back of the hand. Knuckles heavy and roughened, the skin '
          'over them darker and dry. Brown liver spots visible under the wet '
          'sheen. Nails cut short and blunt, water sitting under the tip of '
          'the thumbnail.',
  'roupa': ''},
 {'id': 'costas_v15_camiseta_marinho',
  'curto': 'grisalho de camiseta azul-marinho, barra levantada, só perfil no '
           'espelho',
  'fonte': 'lido',
  'presenca': 'tronco',
  'idade': 60,
  'etnia': 'branco',
  'desc': 'White man shot from behind, his face reaching the lens only as a '
          'partial reflection in the mirror: a long profile, straight nose, '
          'grey stubble along a lean jaw, and a deep vertical crease in the '
          'cheek. Short salt-and-pepper hair, thinning at the crown, cut '
          'high above the ears. Forearms noticeably hairy with dark hair '
          'going grey. Shoulders narrow for his height, a slight forward '
          'stoop.',
  'roupa': 'Navy cotton t-shirt with the back hem lifted and bunched, '
           'exposing the lower back.'},
 {'id': 'maos_v15_bem_velhas',
  'curto': 'mãos bem mais velhas que os antebraços do plano A',
  'fonte': 'lido',
  'presenca': 'maos',
  'idade': 77,
  'etnia': 'branco',
  'desc': 'Hands of a white man near eighty, markedly older than the smooth '
          'forearms seen earlier in the same world. Skin translucent and '
          'slack, deeply wrinkled across every joint, with brown liver spots '
          'crowded on the backs of both hands. Veins thick, blue and '
          'winding, standing well proud of the skin. The little finger of '
          'the right hand curves inward at the last joint. Nails thickened '
          'and slightly opaque, cut short.',
  'roupa': ''},
 {'id': 'maos_artrite_indicador_torto',
  'curto': 'mãos artríticas com o indicador travado torto',
  'fonte': 'construido',
  'presenca': 'maos',
  'idade': 76,
  'etnia': 'branco',
  'desc': 'Hands of a white man of seventy-six with clear arthritic change. '
          'The end joint of the right index finger is permanently bent to '
          'one side and thickened by a hard bony knob; the same knob, '
          'smaller, sits on the middle finger. Skin thin and dry, with fine '
          'flaking over the knuckles. Brown liver spots across both hands. '
          'Veins raised. His grip is careful and slightly clumsy because of '
          'that finger. Nails short and slightly domed.',
  'roupa': ''},
 {'id': 'maos_marceneiro_unha_quebrada',
  'curto': 'mãos de marceneiro, calos secos e meia unha do mindinho',
  'fonte': 'construido',
  'presenca': 'maos',
  'idade': 64,
  'etnia': 'branco',
  'desc': 'Working hands of a white man of sixty-four. Broad palms with a '
          'hard yellow callus ridge running across the base of all four '
          'fingers, dry and slightly cracked. The nail of the left little '
          'finger is missing its outer half, the old bed grown smooth and '
          'shiny. Thumbnail thick and flat with a deep vertical ridge down '
          'the middle. Fine sawdust sits in the knuckle creases. A few brown '
          'spots on the backs of the hands, fewer than his age would '
          'suggest.',
  'roupa': ''},
 {'id': 'maos_vitiligo_dorso',
  'curto': 'mãos negras com mancha de vitiligo no dorso direito',
  'fonte': 'construido',
  'presenca': 'maos',
  'idade': 70,
  'etnia': 'negro',
  'desc': 'Hands of an elderly African-American man. A pale, sharply '
          'outlined vitiligo patch the size of a walnut sits on the back of '
          'the right hand between the thumb and index knuckle, with two '
          'smaller pale islands beside it. The rest of the skin is deep '
          'brown, wrinkled, with raised veins. Fingers thick, joints '
          'slightly swollen. Nails short and clean with wide pale '
          'half-moons. No ring on either hand.',
  'roupa': ''},
 {'id': 'maos_dedos_nicotina_anel',
  'curto': 'dedos com mancha de nicotina e anel de brasão largo',
  'fonte': 'construido',
  'presenca': 'maos',
  'idade': 61,
  'etnia': 'latino',
  'desc': 'Hands of a Latino man of sixty-one, olive-toned and weathered. '
          'The index and middle fingertips of the right hand carry an old '
          'yellow-brown nicotine stain on the skin and on the nail. A heavy '
          'silver signet ring, its flat face rubbed featureless, sits on the '
          'right ring finger. Black hair on the back of the fingers going '
          'grey. Knuckles broad, veins visible but not extreme. Nails cut '
          'with a clipper, corners left square.',
  'roupa': ''},
 {'id': 'maos_cicatriz_palma',
  'curto': 'mãos lisas com cicatriz queloide na base da palma',
  'fonte': 'construido',
  'presenca': 'maos',
  'idade': 66,
  'etnia': 'asiatico',
  'desc': 'Hands of an East Asian man of sixty-six. Skin smooth-textured and '
          'almost hairless, the fine wrinkling appearing mainly over the '
          'knuckles rather than across the whole hand. A raised, pale keloid '
          'scar about two inches long crosses the heel of the left palm and '
          'shows whenever the palm turns to the lens. Veins moderately '
          'visible, running straight. Fingers even in length, nails short '
          'and neatly filed with clean edges. Very few age spots.',
  'roupa': ''},
 {'id': 'maos_tremor_hematoma',
  'curto': 'mãos de 79 com tremor leve e hematoma roxo no dorso',
  'fonte': 'construido',
  'presenca': 'maos',
  'idade': 79,
  'etnia': 'branco',
  'desc': 'Hands of a white man of seventy-nine, unsteady with a fine '
          'constant tremor that shows whenever he holds something still. '
          'Skin nearly translucent, with a large flat purple bruise spread '
          'across the back of the left hand and a smaller one at the wrist. '
          'Veins thick and dark, clearly visible through the skin. Liver '
          'spots crowd both hands. Nails thickened and slightly yellow, cut '
          'unevenly.',
  'roupa': ''},
 {'id': 'antebraco_tatuagem_ancora',
  'curto': 'antebraço negro com tatuagem de âncora esverdeada',
  'fonte': 'construido',
  'presenca': 'maos_antebraco',
  'idade': 57,
  'etnia': 'negro',
  'desc': 'Hands and left forearm of an African-American man of fifty-seven. '
          'On the inner forearm an old anchor tattoo has blurred into a soft '
          'grey-green shape, its outline gone fuzzy and the lettering '
          'beneath it no longer readable. Skin deep brown and firm, with '
          'sparse hair. Veins visible along the forearm and swelling at the '
          'wrist. Knuckles slightly lighter than the surrounding skin. '
          'Yellow gold wedding band on the left ring finger, bright and '
          'unscratched.',
  'roupa': 'Short grey t-shirt sleeve visible at the top edge of frame, '
           'pushed above the elbow.'},
 {'id': 'antebraco_marca_de_sol',
  'curto': 'antebraço com linha de bronzeado de lavrador',
  'fonte': 'construido',
  'presenca': 'maos_antebraco',
  'idade': 68,
  'etnia': 'branco',
  'desc': 'Hands and right forearm of a white man of sixty-eight, with a '
          'hard sun line at mid-forearm: leathery red-brown skin below it, '
          'pale untanned skin above. The tanned half is freckled and its '
          'fine hair is bleached almost white. Brown liver spots on the back '
          'of the hand. Knuckles thick and dry with small cracks. Nails '
          'short, one thumbnail carrying a black line of old bruising '
          'growing out.',
  'roupa': 'Rolled chambray shirt sleeve stopping just above the tan line at '
           'the elbow.'},
 {'id': 'antebraco_pulseira_cobre',
  'curto': 'antebraço peludo com pulseira de cobre no punho',
  'fonte': 'construido',
  'presenca': 'maos_antebraco',
  'idade': 54,
  'etnia': 'latino',
  'desc': 'Hands and forearms of a Latino man of fifty-four, olive skin with '
          'thick black hair covering the forearms down to the wrist. An open '
          'copper bangle worn for joint pain sits on the right wrist, its '
          'inner face polished bright while the outside has gone dark green '
          'in the grooves. Veins strong on the forearm, less so on the hand. '
          'Broad palms, short fingers, nails cut square with a hard rim of '
          'dry skin around each.',
  'roupa': 'Dark polo sleeve cut off at the top of frame; forearms bare.'},
 {'id': 'antebraco_queimadura_punho',
  'curto': 'antebraço com queimadura antiga e brilhante no punho',
  'fonte': 'construido',
  'presenca': 'maos_antebraco',
  'idade': 73,
  'etnia': 'branco',
  'desc': 'Hands and left forearm of a white man of seventy-three. On the '
          'inner wrist an old burn scar the size of a coin sits shiny, '
          'hairless and slightly puckered, paler than the skin around it. '
          'Elsewhere the skin is thin and spotted brown, the forearm hair '
          'sparse and white. Veins prominent along the forearm and looping '
          'over the back of the hand. Finger joints slightly swollen, nails '
          'ridged and short.',
  'roupa': 'Faded plaid flannel cuff unbuttoned and pushed back, visible at '
           'the elbow edge of frame.'},
 {'id': 'antebraco_relogio_por_dentro',
  'curto': 'mãos negras ressecadas, relógio virado por dentro do punho',
  'fonte': 'construido',
  'presenca': 'maos_antebraco',
  'idade': 65,
  'etnia': 'negro',
  'desc': 'Hands and forearms of an African-American man of sixty-five. The '
          'knuckles are dry and ashy, a pale grey against the deep brown '
          'skin, and the same dryness runs along the outer edge of each '
          'hand. A steel watch on a wide worn leather strap is turned so the '
          'face rides on the inside of the left wrist. Veins raised on the '
          'forearm. Thick fingers, short nails, a small dark scar on the web '
          'between thumb and index.',
  'roupa': 'Sleeve of a heather-grey henley pushed up in a thick roll below '
           'the elbow.'},
 {'id': 'antebraco_sardas_no_quebrado',
  'curto': 'antebraço sardento ruivo-grisalho, um nó achatado',
  'fonte': 'construido',
  'presenca': 'maos_antebraco',
  'idade': 62,
  'etnia': 'branco',
  'desc': 'Hands and right forearm of a white man of sixty-two, very fair '
          'and heavily freckled from wrist to elbow, the freckles running '
          'together into patches. Forearm hair is faded ginger going grey. '
          'The middle knuckle of the right hand is flattened and sits lower '
          'than the others from an old break, and the finger above it angles '
          'slightly outward. Veins visible, thin and straight. Nails pale '
          'and short, cuticles dry.',
  'roupa': 'Sleeve of a white cotton undershirt visible high at the shoulder '
           'edge of frame.'},
 {'id': 'antebraco_cicatriz_mordida',
  'curto': 'antebraço com cicatriz em crescente de mordida antiga',
  'fonte': 'construido',
  'presenca': 'maos_antebraco',
  'idade': 70,
  'etnia': 'branco',
  'desc': 'Hands and left forearm of a white man of seventy. A crescent of '
          'small white scars, an old dog bite, curves across the outer '
          'forearm halfway to the elbow, the skin there smooth and hairless '
          'where the hair never came back. The rest of the forearm is '
          'spotted brown and wrinkled at the wrist. Veins thick and blue. '
          'Wide flat fingernails, cut short, with pronounced lengthwise '
          'ridges. No ring.',
  'roupa': 'Rolled cuff of a soft green flannel shirt at the top edge of '
           'frame.'},
 {'id': 'antebraco_cicatriz_polegar',
  'curto': 'mãos de pouca pelagem com cicatriz cirúrgica na base do polegar',
  'fonte': 'construido',
  'presenca': 'maos_antebraco',
  'idade': 71,
  'etnia': 'asiatico',
  'desc': 'Hands and forearms of an East Asian man of seventy-one. A thin '
          'white surgical scar about an inch long runs across the base of '
          'the right thumb into the wrist crease, the line flat and slightly '
          'shiny. Skin smooth with sparse hair, wrinkling mainly at the '
          'knuckles and the wrist. A few small flat brown spots on the backs '
          'of the hands. Fingers slender, nails short with clean straight '
          'edges. No jewellery.',
  'roupa': 'Cuff of a pale blue button-down shirt, rolled twice, visible at '
           'the left wrist.'},
 {'id': 'antebraco_unha_martelada',
  'curto': 'antebraço grosso com unha do polegar preta crescendo',
  'fonte': 'construido',
  'presenca': 'maos_antebraco',
  'idade': 59,
  'etnia': 'branco',
  'desc': 'Thick hands and forearms of a white man of fifty-nine. The right '
          'thumbnail is dark purple-black from an old hammer strike, with a '
          'clean half-moon of new pink nail growing out at the base. '
          'Forearms heavy, hair dark going grey, a wide flat vein crossing '
          'toward the elbow. Knuckles broad and scuffed. Dried paint '
          'speckles sit on the back of the left hand and in the wrist hair. '
          'Nails cut with a knife, edges irregular.',
  'roupa': 'Sleeve of a paint-spattered grey work shirt, rolled thick above '
           'the elbow.'},
 {'id': 'antebraco_corrente_fina',
  'curto': 'antebraço latino com pulseira de elos finos e unhas sulcadas',
  'fonte': 'construido',
  'presenca': 'maos_antebraco',
  'idade': 76,
  'etnia': 'latino',
  'desc': 'Hands and forearms of a Latino man of seventy-six, skin gone thin '
          'and olive-grey, with brown spots crowded on the backs of the '
          'hands. A fine gold link bracelet, thin as a chain, sits loose on '
          'the right wrist and slides when he moves. Every fingernail '
          'carries deep lengthwise furrows and a slight yellowing at the '
          'tip. Veins very prominent, standing up over the tendons. Knuckles '
          'wide, the skin over them loose.',
  'roupa': 'Cuff of a short-sleeve guayabera visible high in frame; forearm '
           'bare below.'},
 {'id': 'antebraco_alianca_gasta',
  'curto': 'aliança gasta e oval no anelar, nós mais escuros',
  'fonte': 'construido',
  'presenca': 'maos_antebraco',
  'idade': 74,
  'etnia': 'negro',
  'desc': 'Hands and forearms of an African-American man of seventy-four. A '
          'yellow gold wedding band on the left ring finger has worn thin '
          'and gone oval, biting slightly into the finger. The knuckles read '
          'distinctly darker than the skin around them. Skin heavily lined, '
          'with pale age spots. Veins raised in a network across the '
          'forearm. Fingers thick, nails short and slightly domed, with a '
          'small ridge on the right index.',
  'roupa': 'Sleeve of a maroon short-sleeve polo at the top edge of frame.'},
 {'id': 'antebraco_mecanico_graxa',
  'curto': 'mãos de mecânico com graxa nas linhas dos nós',
  'fonte': 'construido',
  'presenca': 'maos_antebraco',
  'idade': 55,
  'etnia': 'branco',
  'desc': 'Hands and forearms of a white man of fifty-five who works on '
          'engines. Fine black grease is worked permanently into the creases '
          'of the knuckles and under the free edge of every nail, while the '
          'skin around it is scrubbed clean and slightly raw. A long thin '
          'white scar runs from the base of the left thumb up the inside of '
          'the forearm. Forearms thick with dark hair. Veins strong. Nails '
          'short, one index nail chipped at the corner.',
  'roupa': 'Sleeve of a navy work shirt rolled twice above the elbow, cuff '
           'stained dark.'},
 {'id': 'tronco_barril_cicatriz_baixa',
  'curto': 'tronco de barril com pelo grisalho e cicatriz baixa no abdômen',
  'fonte': 'construido',
  'presenca': 'tronco',
  'idade': 66,
  'etnia': 'branco',
  'desc': 'Barrel-chested white man of sixty-six. Chest hair thick and '
          'almost entirely grey, spreading wide across the chest and running '
          'down the centre of a rounded belly. A short pale surgical scar '
          'sits low on the right side of the abdomen. The frame cuts the '
          'head above the upper lip: only jaw, chin and mouth show, with a '
          'heavy square jaw, grey stubble and a deep vertical crease down '
          'the centre of the chin. Thick neck with two horizontal folds.',
  'roupa': 'White cotton undershirt pulled up and bunched under the chest; '
           'grey drawstring sweatpants at the hips.'},
 {'id': 'tronco_magro_queloide_ombro',
  'curto': 'tronco negro enxuto com queloide no ombro',
  'fonte': 'construido',
  'presenca': 'tronco',
  'idade': 61,
  'etnia': 'negro',
  'desc': 'Lean torso of an African-American man of sixty-one, still '
          'carrying muscle in the shoulders and upper arms with the '
          'definition softened. A raised keloid scar the width of a finger '
          'sits on the front of the left shoulder. Chest hair sparse and '
          'grey. The frame cuts the head at the mouth: a narrow chin with a '
          'close-trimmed white goatee, and a jaw with a visible tendon line '
          'running down the neck.',
  'roupa': 'Black cotton tank top, hem loose over the waistband of grey '
           'shorts.'},
 {'id': 'tronco_camisa_xadrez_aberta',
  'curto': 'barriga mole e camisa xadrez aberta, tatuagem desbotada no ombro',
  'fonte': 'construido',
  'presenca': 'tronco',
  'idade': 69,
  'etnia': 'latino',
  'desc': 'Torso of a Latino man of sixty-nine, soft belly resting over the '
          'waistband, chest hair grey and thinning at the centre. On the '
          'right shoulder an old tattoo has faded to a soft blue-grey blur '
          'with no readable edge. Olive skin with sun damage across the '
          'shoulders. Head cut at the mouth: a wide chin, a thick grey '
          'moustache dropping past the lip corners, and stubble along a full '
          'jaw.',
  'roupa': 'Red plaid flannel shirt worn open over the bare chest, sleeves '
           'rolled to the forearm.'},
 {'id': 'tronco_magro_cicatriz_clavicula',
  'curto': 'tronco magro com costelas à mostra e cicatriz sob a clavícula',
  'fonte': 'construido',
  'presenca': 'tronco',
  'idade': 72,
  'etnia': 'branco',
  'desc': 'Thin torso of a white man of seventy-two, ribs faintly visible '
          'beneath the skin, chest almost hairless with a few white hairs at '
          'the sternum. A pale surgical scar four inches long runs under the '
          'left collarbone. His face is in frame: a long narrow skull, '
          'hollow cheeks, a high thin nose with a slight bump at the bridge, '
          'deep-set pale eyes under sparse white brows, and a receded '
          'hairline with fine white hair combed flat.',
  'roupa': 'Terry towel wrapped and tucked at the waist; no shirt.'},
 {'id': 'tronco_roupao_ombros_largos',
  'curto': 'ombros largos, roupão aberto, mandíbula quadrada',
  'fonte': 'construido',
  'presenca': 'tronco',
  'idade': 57,
  'etnia': 'branco',
  'desc': 'White man of fifty-seven, broad through the shoulders with a '
          'thick chest and a belly that has begun to soften. Chest hair dark '
          'going grey, dense at the sternum. His face is in frame: a wide '
          'square jaw with a heavy chewing muscle at the corner, a blunt '
          'nose, a brow bone that shades the eyes, deep lines from nose to '
          'mouth corners, and short dark hair going grey at the temples with '
          'a cowlick at the front.',
  'roupa': 'Navy waffle-weave robe worn open over the bare chest, belt '
           'hanging loose.'},
 {'id': 'tronco_pijama_listrado',
  'curto': 'ombros curvados de 78, pijama listrado abotoado até o meio',
  'fonte': 'construido',
  'presenca': 'tronco',
  'idade': 78,
  'etnia': 'negro',
  'desc': 'African-American man of seventy-eight, shoulders stooped forward, '
          'chest narrow with loose skin and white chest hair showing at the '
          'open collar. Forearms thin, veins standing up like cord. His face '
          'is in frame: a long narrow head, a high forehead carrying three '
          'deep horizontal creases, a flat wide nose, hollow cheeks, '
          'close-cropped white hair receding at both temples, and a short '
          'white beard along the jaw only.',
  'roupa': 'Blue-and-white striped cotton pyjama top, buttoned from the '
           'middle down, collar open.'},
 {'id': 'corpo_nariz_torto',
  'curto': 'corpo inteiro, nariz quebrado torto e sobrancelhas prateadas',
  'fonte': 'construido',
  'presenca': 'corpo_inteiro',
  'idade': 64,
  'etnia': 'branco',
  'desc': 'White man of sixty-four, medium height, wiry with sloping '
          'shoulders. Long narrow head, high flat cheekbones, and a nose '
          'broken once and healed with a visible deviation to the left. '
          'Silver eyebrows grown coarse and slightly wild. Deep nasolabial '
          "folds bracket a thin-lipped mouth. Hairline receded to a widow's "
          'peak, hair grey and combed back. His hands hang at his sides with '
          'prominent knuckles and a plain steel band on the left ring '
          'finger.',
  'roupa': 'Grey crew-neck t-shirt tucked into dark work trousers, brown '
           'leather belt with a worn buckle.'},
 {'id': 'corpo_barba_branca_gap',
  'curto': 'corpo inteiro, malares largos e barba branca rente',
  'fonte': 'construido',
  'presenca': 'corpo_inteiro',
  'idade': 70,
  'etnia': 'negro',
  'desc': 'African-American man of seventy, tall with a slight forward lean. '
          'Broad flat cheekbones, deep-set eyes under a strong brow, a wide '
          'nose with rounded nostrils, and a full mouth with a visible gap '
          'between the upper front teeth when he speaks. Close-cropped white '
          'beard following the jawline with a matching white moustache; hair '
          'shaved to the scalp and gone white at the sides. Ears with long '
          'attached lobes. Yellow gold band on the left hand.',
  'roupa': 'Olive-green button-down shirt worn open over a white undershirt, '
           'dark jeans, canvas sneakers.'},
 {'id': 'corpo_bigode_grisalho',
  'curto': 'corpo inteiro, mandíbula quadrada e bigode preto grisalhando',
  'fonte': 'construido',
  'presenca': 'corpo_inteiro',
  'idade': 58,
  'etnia': 'latino',
  'desc': 'Latino man of fifty-eight, stocky and thick through the chest. '
          'Square jaw with a heavy chin, a prominent brow ridge shading dark '
          'eyes, a wide-based nose, and a thick black moustache greying at '
          'the outer ends that covers the upper lip. Olive skin with sun '
          'lines fanning from the eye corners. Black hair, greying at the '
          'temples, combed back and still thick on top. A small dark mole '
          'below the right eye.',
  'roupa': 'Short-sleeve grey work shirt with a chest pocket, tucked in, '
           'dark denim jeans.'},
 {'id': 'corpo_nariz_bulboso',
  'curto': 'corpo inteiro, papada e nariz bulboso com capilares',
  'fonte': 'construido',
  'presenca': 'corpo_inteiro',
  'idade': 75,
  'etnia': 'branco',
  'desc': 'White man of seventy-five, heavy-set and short, standing with his '
          'weight on one hip. Round skull, jowls sagging past the jawline, '
          'and a bulbous nose with fine red capillaries across the bridge '
          'and wings. Thick white eyebrows growing long over pale watery '
          'eyes, with deep pouches beneath them. Thin white hair combed '
          'sideways over the crown, ears large with hair at the tragus. '
          'Brown spots on the forehead and on the backs of the hands.',
  'roupa': 'Beige short-sleeve button shirt untucked over dark slacks, house '
           'slippers.'},
 {'id': 'corpo_queixo_fendido',
  'curto': 'corpo inteiro, queixo fendido e óculos de armação fina',
  'fonte': 'construido',
  'presenca': 'corpo_inteiro',
  'idade': 52,
  'etnia': 'branco',
  'desc': 'White man of fifty-two, tall and lean with square shoulders. '
          'Angular face: flat cheek planes, a straight nose, and a distinct '
          'vertical cleft in the chin. Dark brown hair going grey only at '
          'the temples, cut short and parted on the left. Thin wire-frame '
          'glasses sit low on the nose, the lenses catching a small '
          'reflection. A faint vertical scar cuts through the left eyebrow. '
          'Clean-shaven, with a blue shadow along the jaw.',
  'roupa': 'Navy quarter-zip pullover over a white collared shirt, khaki '
           'chinos.'},
 {'id': 'corpo_testa_alta_cavanhaque',
  'curto': 'corpo inteiro, testa alta com três vincos e cavanhaque '
           'sal-e-pimenta',
  'fonte': 'construido',
  'presenca': 'corpo_inteiro',
  'idade': 66,
  'etnia': 'negro',
  'desc': 'African-American man of sixty-six, medium build, standing '
          'straight. Narrow face with a high forehead carrying three '
          'horizontal creases, angular cheekbones, and a straight narrow '
          'nose. Salt-and-pepper goatee framing the mouth, the upper lip '
          'hair heavier than the chin. Hair cut low with a sharp lined-up '
          'hairline squared at the corners. A small pale scar on the left '
          'cheekbone. Reading glasses hooked into his shirt collar.',
  'roupa': 'Charcoal cardigan over a light blue polo, dark trousers, brown '
           'loafers.'},
 {'id': 'corpo_malares_altos_cabelo_penteado',
  'curto': 'corpo inteiro, malares altos e cabelo ralo penteado pra trás',
  'fonte': 'construido',
  'presenca': 'corpo_inteiro',
  'idade': 68,
  'etnia': 'branco',
  'desc': 'White man of sixty-eight, broad-framed and slightly '
          'barrel-chested. High wide cheekbones with a flat plane beneath '
          'them, pale blue eyes set under a low brow, a short straight nose, '
          'and a wide mouth with thin lips. Thinning grey hair combed '
          'straight back from a high forehead, leaving the temples bare. '
          'Long earlobes. Skin ruddy across the cheekbones with broken '
          'capillaries. A shaving nick healing at the corner of the jaw.',
  'roupa': 'Green flannel shirt buttoned to the second button, sleeves '
           'rolled, dark work jeans.'},
 {'id': 'corpo_pes_de_galinha_cabelo_branco',
  'curto': 'corpo inteiro, cabelo branco farto e óculos de leitura na gola',
  'fonte': 'construido',
  'presenca': 'corpo_inteiro',
  'idade': 73,
  'etnia': 'latino',
  'desc': 'Latino man of seventy-three, medium height with a slight paunch. '
          "Deep crow's feet fanning from dark brown eyes, heavy lower lids, "
          'a wide nose with a rounded tip, and full lips framed by deep '
          'smile lines. Thick white hair brushed straight back off the '
          'forehead, still dense at the crown. Clean-shaven, with white '
          'stubble showing at the sideburns. A dark raised mole on the left '
          'side of the neck.',
  'roupa': 'Cream short-sleeve guayabera with vertical pintucks, dark brown '
           'trousers, gold-rimmed reading glasses hanging from the open '
           'collar.'},
 {'id': 'h51',
  'curto': 'Mãos de mineiro do leste do Kentucky, mindinho cortado',
  'fonte': 'construido',
  'presenca': 'maos',
  'idade': 71,
  'etnia': 'white',
  'desc': 'Two hands of a 71-year-old white man from eastern Kentucky, '
          'resting on the tub rim. Broad flat nail beds, knuckles swollen '
          'into knobs by arthritis, and a permanent grey-blue line of coal '
          'dust set under the left thumbnail that no scrubbing has ever '
          'lifted. The tip of the left little finger is gone above the first '
          'joint, the stump rounded and pale. Skin dry and cracked across '
          'the knuckles, a thick blue vein running from the wrist to the '
          'base of the index finger. No ring, but a bare white band of skin '
          'where one sat for forty years.',
  'roupa': ''},
 {'id': 'h52',
  'curto': 'Mãos e antebraço de metalúrgico de Detroit, queimadura de prensa',
  'fonte': 'construido',
  'presenca': 'maos_antebraco',
  'idade': 66,
  'etnia': 'Black',
  'desc': 'Right hand and forearm of a 66-year-old Black man from Detroit, '
          'entering frame from the lower edge. Deep brown skin with lighter '
          'mottling across the back of the hand, tendons standing like '
          'cords, nails short and squared. A shiny raised keloid stripe '
          'about four inches long runs along the inside of the forearm from '
          'an old press-brake burn, the skin there paler and smooth. A thin '
          'gold wedding band worn down to an oval on the ring finger, and a '
          'plain steel watch with a cracked crystal on the wrist.',
  'roupa': 'Faded navy work shirt with the sleeve rolled twice above the '
           'elbow'},
 {'id': 'h53',
  'curto': 'Homem inteiro do Vale do Rio Grande, nariz quebrado e guayabera',
  'fonte': 'construido',
  'presenca': 'corpo_inteiro',
  'idade': 58,
  'etnia': 'Hispanic',
  'desc': 'A 58-year-old Hispanic man from the Rio Grande Valley in Texas, '
          'standing full length beside the tub. Compact and thick through '
          'the chest, a heavy belly, short bowed legs. Face: wide square '
          'jaw, broad flat nose bridge with a bump halfway down where it was '
          'broken, deep-set dark eyes under a low straight brow, a heavy '
          'grey moustache covering the upper lip, deep vertical creases from '
          'nose to mouth corners, black hair still dark on top and white '
          'only at the temples. A dark mole the size of a pencil eraser sits '
          'high on the left cheekbone. His hands are wide with short blunt '
          'fingers and a hairline scar across the right palm.',
  'roupa': 'Untucked short-sleeve guayabera in pale cream over dark work '
           'trousers, brown leather belt, socks and rubber sandals'},
 {'id': 'h54',
  'curto': 'Mãos finas de Honolulu, anel de jade lascado',
  'fonte': 'construido',
  'presenca': 'maos',
  'idade': 74,
  'etnia': 'Asian American',
  'desc': 'Hands of a 74-year-old Japanese American man in Honolulu. Slim '
          'hands, long fingers, skin thin enough to show every tendon, and a '
          'flat brown sun spot the size of a nickel over the second knuckle '
          'of the left hand. The right index fingernail is thickened and '
          'ridged, yellowed at the tip, from a hammer strike decades ago. A '
          'worn jade ring, deep green and chipped at one edge, sits loose on '
          'the right little finger. The fingertips are smooth and slightly '
          'shiny.',
  'roupa': ''},
 {'id': 'h55',
  'curto': 'Tronco do Panhandle da Flórida, cicatriz sob a clavícula',
  'fonte': 'construido',
  'presenca': 'tronco',
  'idade': 62,
  'etnia': 'white',
  'desc': 'Bare torso of a 62-year-old white man on the Florida Panhandle, '
          'framed from the collarbones down to the waist, the face cropped '
          'away above the mouth. Sunburnt neck and forearms against a pale '
          'chest, with a hard tan line across the biceps. Grey chest hair, a '
          'soft belly, a slack chest. A four-inch surgical scar, silvered '
          'and flat, runs under the right collarbone. The right hand holds '
          'the jar; its knuckles are red and chapped, and the wedding band '
          'has gone brassy from pool chemicals.',
  'roupa': 'Bare chest, a faded blue beach towel knotted at the waist'},
 {'id': 'h56',
  'curto': 'Mãos diné de Window Rock, prata com turquesa',
  'fonte': 'construido',
  'presenca': 'maos_antebraco',
  'idade': 69,
  'etnia': 'Native American',
  'desc': 'Both hands and forearms of a 69-year-old Diné man from Window '
          'Rock, Arizona. Warm brown skin sun-darkened to a sharp line at '
          'the wrist, broad palms, thick fingers with wide flat nails cut '
          'straight across. The back of the left hand carries a pale zigzag '
          'scar from barbed wire. A heavy silver band inlaid with a single '
          'turquoise stone sits on the right ring finger, the silver dulled '
          'and scratched. Coarse black-and-grey hair on the forearms, and a '
          'faint white stripe at the wrist where a watch strap used to sit.',
  'roupa': 'Pearl-snap western shirt in faded red plaid, cuffs undone and '
           'pushed to the forearm'},
 {'id': 'h57',
  'curto': 'Mãos de pescador do Maine, cicatriz de anzol',
  'fonte': 'construido',
  'presenca': 'maos',
  'idade': 77,
  'etnia': 'white',
  'desc': 'Hands of a 77-year-old white lobsterman from Down East Maine. '
          'Enormous knuckles, fingers permanently curved as if still closed '
          'around a rope, palms thick and yellow with callus, nails short '
          'and split. A white hook scar curls through the web between the '
          'right thumb and index finger. The skin is chapped scarlet across '
          'the backs, cracked at the knuckle folds, with brown age spots '
          'crowding the wrists. The left little finger sits crooked, healed '
          'off-line from an old break nobody set.',
  'roupa': ''},
 {'id': 'h58',
  'curto': 'Mãos do Lowcountry, vitiligo em volta da aliança',
  'fonte': 'construido',
  'presenca': 'maos',
  'idade': 72,
  'etnia': 'Black',
  'desc': 'Hands of a 72-year-old Black man from the South Carolina '
          'Lowcountry. Very dark skin on the backs, much paler on the palms, '
          'deeply lined, the palm creases pale and sharp. Fingers long and '
          'tapering, nails filed smooth and pink at the beds. Two pale flat '
          'patches of vitiligo spread across the back of the left hand '
          'around the ring finger. A thick gold wedding band, wide and '
          'slightly domed, on the left. A ridge of callus runs along the '
          'outside edge of the right hand.',
  'roupa': ''},
 {'id': 'h59',
  'curto': 'Mão e antebraço de Fresno, unha do polegar rachada ao meio',
  'fonte': 'construido',
  'presenca': 'maos_antebraco',
  'idade': 64,
  'etnia': 'Hispanic',
  'desc': 'Right hand and forearm of a 64-year-old Mexican American man from '
          'Fresno, California. Deeply tanned to the elbow, then a hard line '
          'where the sleeve ended and the skin turns pale. A wide working '
          'hand, thick pads at the base of the fingers, dirt still dark in '
          'the creases and under two nails. The right thumbnail is split '
          'lengthwise and has grown back in two halves. A faded green tattoo '
          'of three small dots sits in the web of the thumb, blurred to a '
          'smudge by fifty years. The hair on the forearm is sun-bleached to '
          'copper.',
  'roupa': 'Grey cotton T-shirt, the short sleeve tight around the upper '
           'arm'},
 {'id': 'h60',
  'curto': 'Tronco do Iron Range, âncora borrada no ombro',
  'fonte': 'construido',
  'presenca': 'tronco',
  'idade': 68,
  'etnia': 'white',
  'desc': 'Torso of a 68-year-old white man from Hibbing, Minnesota, framed '
          'from the shoulders to the hips, the face cut off by the top of '
          'frame so only a grey stubbled chin shows. Big-framed and gone '
          'soft, a heavy round belly straining the undershirt, sloping '
          'shoulders, white hair on the forearms. A dark blue tattoo on the '
          'left shoulder has blurred past reading and shows only the outline '
          'of an anchor. Both hands are wide and pink, the left ring finger '
          'swollen around a wedding band that has not come off in thirty '
          'years.',
  'roupa': 'White ribbed sleeveless undershirt, worn thin and yellowed at '
           'the neckline, over dark green work trousers'},
 {'id': 'h61',
  'curto': 'Mãos pequenas do Queens, corte de estilete no indicador',
  'fonte': 'construido',
  'presenca': 'maos',
  'idade': 70,
  'etnia': 'Asian American',
  'desc': 'Hands of a 70-year-old Korean American man in Queens, New York. '
          'Small, neat hands with square fingertips, nails trimmed very '
          'short and clean. The skin is sallow and thin, showing a network '
          'of fine wrinkles at every knuckle; two dark brown age spots sit '
          'on the back of the right hand and one on the wrist. The left '
          'index finger has a shiny flat scar across the pad from a box '
          'cutter, the fingerprint pattern interrupted by it. No ring, but a '
          'thin frayed red thread bracelet around the left wrist.',
  'roupa': ''},
 {'id': 'h62',
  'curto': 'Homem inteiro de Atlanta, quelóide na orelha e óculos na testa',
  'fonte': 'construido',
  'presenca': 'corpo_inteiro',
  'idade': 61,
  'etnia': 'Black',
  'desc': 'A 61-year-old Black man from Atlanta, standing full length in the '
          'bathroom doorway. Tall and lean with wide shoulders and long '
          'arms, a slight stoop. Face: long narrow jaw with a short white '
          'beard trimmed close, broad nose with wide nostrils, high rounded '
          'forehead, hairline receded to the crown with the remaining hair '
          'cut to grey stubble, deep-set eyes with heavy lower lids, and a '
          'small raised keloid bump on the left earlobe from an old '
          'piercing. Reading glasses pushed up on the forehead. His hands '
          'are long-fingered, with a plain gold band on the left.',
  'roupa': 'Open short-sleeve button-down in pale blue over a white '
           'undershirt, dark grey sweatpants, house slippers'},
 {'id': 'h63',
  'curto': 'Mãos de Pittsburgh, unha roxa e sardas de solda',
  'fonte': 'construido',
  'presenca': 'maos_antebraco',
  'idade': 59,
  'etnia': 'white',
  'desc': 'Both hands and forearms of a 59-year-old white man in Pittsburgh, '
          'the arm hair still mostly dark brown with grey at the wrists. The '
          'hands are broad and heavy, the nails wide, and the right index '
          'nail is blackened dark purple under the plate from a recent hit '
          'and is growing out. A cluster of small pale spark-burn scars, '
          'each the size of a pinhead, freckles the left forearm from '
          'welding. Veins stand out along the back of both hands. A '
          'tarnished silver claddagh ring sits on the right ring finger.',
  'roupa': 'Grey hooded sweatshirt with the sleeves shoved up to the elbows'},
 {'id': 'h64',
  'curto': 'Mãos manchadas de Albuquerque, polegar liso de tanto enrolar',
  'fonte': 'construido',
  'presenca': 'maos',
  'idade': 76,
  'etnia': 'Hispanic',
  'desc': 'Hands of a 76-year-old Hispanic man from Albuquerque, New Mexico. '
          'Weathered brown skin, loose over the backs of the hands, mapped '
          'with sun damage — a dozen flat coffee-coloured spots between the '
          'wrist and the knuckles. Long fingers, enlarged knuckles, both '
          'little fingers bending inward. The nails are thick and ridged, '
          'one of them yellowed. A stamped silver ring worn smooth sits on '
          'the left middle finger. The pad of the right thumb is polished '
          'shiny and hairless from decades of rolling.',
  'roupa': ''},
 {'id': 'h65',
  'curto': 'Tronco lakota de Pine Ridge, trança sobre o peito',
  'fonte': 'construido',
  'presenca': 'tronco',
  'idade': 65,
  'etnia': 'Native American',
  'desc': 'Torso of a 65-year-old Lakota man from Pine Ridge, South Dakota, '
          'framed from the collarbones to the belt, the chin and mouth just '
          'visible at the top of frame with grey stubble. A broad barrel '
          'chest with almost no chest hair, a thick middle, heavy rounded '
          'shoulders. Warm brown skin with a paler band across the upper '
          'arms where sleeves usually sit. A long thin surgical scar runs '
          'down the centre of the chest, silvered and slightly puckered. A '
          'braid of black-and-grey hair falls forward over the right '
          'shoulder onto the chest.',
  'roupa': 'Bare chest, a dark grey towel over the left shoulder, faded '
           'jeans low on the hips'},
 {'id': 'h66',
  'curto': 'Mãos mais novas de Boise, unha do médio que nunca voltou',
  'fonte': 'construido',
  'presenca': 'maos',
  'idade': 55,
  'etnia': 'white',
  'desc': 'Hands of a 55-year-old white man in Boise, Idaho — the '
          'youngest-looking hands in the pool. The skin is still firm across '
          'the backs, with only the beginnings of crepe at the wrist and no '
          'liver spots. Sandy hair grows on the fingers between the '
          'knuckles. The left hand is missing the fingernail on the middle '
          'finger, the bed smooth and shiny where it never grew back. A '
          'brushed titanium wedding band, dark grey and wide, sits low on '
          'the left ring finger, and a blue ballpoint mark streaks the side '
          'of the right index finger.',
  'roupa': ''},
 {'id': 'h67',
  'curto': 'Mão e antebraço do South Side, relógio folgado escorregando',
  'fonte': 'construido',
  'presenca': 'maos_antebraco',
  'idade': 73,
  'etnia': 'Black',
  'desc': 'Left hand and forearm of a 73-year-old Black man on the South '
          'Side of Chicago. The skin is dark and dry, ashy grey at the '
          'knuckles, with deep parallel wrinkles across the back of the '
          'hand. The forearm is thin, the muscle gone, a raised vein snaking '
          'from wrist to elbow. A four-inch white scar crosses the inside of '
          'the wrist. The nails are thick and slightly curved with pale '
          'half-moons. A gold-tone watch on a stretch band hangs loose and '
          'slides down toward the hand every time he lifts it.',
  'roupa': 'Maroon terry bathrobe, the sleeve falling back off the forearm'},
 {'id': 'h68',
  'curto': 'Mãos de 79 anos em Sarasota, tremor fino e anel de brasão',
  'fonte': 'construido',
  'presenca': 'maos',
  'idade': 79,
  'etnia': 'white',
  'desc': 'Hands of a 79-year-old white man in Sarasota, Florida, the oldest '
          'hands in the pool. The skin is translucent and papery, with '
          'purple bruises blooming on the backs where the vessels gave way '
          'and veins standing ropy and high. Liver spots crowd from the '
          'knuckles up over the wrists. The nails are long, thickened and '
          'faintly yellow. The right hand carries a fine constant tremor, '
          'visible whenever it holds the lid. A gold signet ring with a worn '
          'flat face sits on the left little finger.',
  'roupa': ''},
 {'id': 'h69',
  'curto': 'Homem inteiro de Las Vegas, bigode branco e corrente no '
           'colarinho',
  'fonte': 'construido',
  'presenca': 'corpo_inteiro',
  'idade': 67,
  'etnia': 'Hispanic',
  'desc': 'A 67-year-old Cuban American man in Las Vegas, standing in full '
          'frame at the bathroom door. Short and broad, thick-necked, with a '
          'hard round belly and arms still heavy from work. Face: round with '
          'full jowls, a broad flat nose, a thick white moustache that hides '
          'the upper lip entirely, heavy dark eyebrows still black against '
          'white hair combed straight back, deep smile creases at the eyes, '
          'and a small pitted scar on the right cheek from childhood. The '
          'skin is an even olive. A gold chain shows at the open collar.',
  'roupa': 'Cream short-sleeve linen shirt buttoned halfway over a white '
           'undershirt, dark shorts, leather sandals'},
 {'id': 'h70',
  'curto': 'Tronco magro de Seattle, timão desbotado no braço',
  'fonte': 'construido',
  'presenca': 'tronco',
  'idade': 63,
  'etnia': 'Asian American',
  'desc': 'Torso of a 63-year-old Filipino American man in Seattle, framed '
          'from the base of the throat to the waist, the face cropped above '
          'the mouth. Lean and wiry, the ribs faintly visible, a small soft '
          'belly, an almost hairless chest. Warm brown skin with a raised '
          'mole the size of a pea below the left nipple. A faded blue tattoo '
          "of a ship's wheel sits on the outside of the right upper arm, the "
          'linework blurred and gone green with age. The hands are slim, and '
          'the left ring finger carries a plain worn band.',
  'roupa': 'Bare chest, a white towel over one shoulder, dark blue pyjama '
           'trousers'},
 {'id': 'h71',
  'curto': 'Mãos de Nashville, quatro calos de corda nas pontas',
  'fonte': 'construido',
  'presenca': 'maos',
  'idade': 60,
  'etnia': 'white',
  'desc': 'Hands of a 60-year-old white man in Nashville. Long, bony '
          'fingers, with four hard flattened calluses on the fingertips of '
          'the left hand from guitar strings, each one shiny and pale. The '
          'nails on the right hand are grown longer than those on the left. '
          'Freckles scatter across both backs and thicken into sun spots at '
          'the wrists. A dark, well-worn leather cord bracelet sits on the '
          'right wrist. Fine reddish-grey hair grows between the knuckles.',
  'roupa': ''},
 {'id': 'h72',
  'curto': 'Mãos cherokee de Tulsa, nó rachado e bracelete de prata',
  'fonte': 'construido',
  'presenca': 'maos_antebraco',
  'idade': 58,
  'etnia': 'Native American',
  'desc': 'Both hands and forearms of a 58-year-old Cherokee man in Tulsa, '
          'Oklahoma. Broad hands, thick through the palm, brown skin with a '
          'red undertone, forearms heavy and still muscled. The back of the '
          'right hand carries a fresh split across the middle knuckle, '
          'scabbed dark. The forearm hair is black, straight and coarse, '
          'with grey coming in near the wrists. A wide hammered silver cuff '
          'sits on the left wrist. The thumbnails are broad and ridged, and '
          'the left one has a deep white line across it.',
  'roupa': 'Black T-shirt with short sleeves, a faded canvas jacket sleeve '
           'shoved back on the left arm'},
 {'id': 'h73',
  'curto': 'Mãos de Baton Rouge, indicador cortado na junta',
  'fonte': 'construido',
  'presenca': 'maos',
  'idade': 68,
  'etnia': 'Black',
  'desc': 'Hands of a 68-year-old Black man in Baton Rouge, Louisiana. Wide '
          'palms, short thick fingers, dark skin gone dusty at the knuckles. '
          'The last joint of the right index finger is missing, taken clean '
          'at the joint, the end rounded and smooth — and the hand still '
          'points with that finger. The nails are broad and short, one '
          'growing back over a dark bruise. A gold wedding band has sunk '
          'deep into the finger with the flesh risen over it on both sides. '
          'At the wrist sits a raised scar shaped like a small horseshoe.',
  'roupa': ''},
 {'id': 'h74',
  'curto': 'Tronco de Cheyenne, clavícula soldada torta',
  'fonte': 'construido',
  'presenca': 'tronco',
  'idade': 71,
  'etnia': 'white',
  'desc': 'Torso of a 71-year-old white man in Cheyenne, Wyoming, framed '
          'from the shoulders down, the face cut by the top of frame so only '
          'a white-stubbled chin shows. Broad-shouldered and once heavy, now '
          'thinner, the skin loose across the chest. A deep leathered tan '
          'covers the neck, forearms and the V of the throat; the rest of '
          'the torso is pale as paper. The chest hair is white. A hard '
          'raised lump sits over the left collarbone where an old break '
          'knitted crooked. His right hand is thick and cracked, and the '
          'left carries a battered gold band.',
  'roupa': 'Bare chest, faded blue jeans with a large oval belt buckle, a '
           'white towel hanging from the left hand'},
 {'id': 'h75',
  'curto': 'Mão de San Antonio, medalha escorregada até o dorso',
  'fonte': 'construido',
  'presenca': 'maos_antebraco',
  'idade': 62,
  'etnia': 'Hispanic',
  'desc': 'Right hand and forearm of a 62-year-old Tejano man in San '
          'Antonio, entering from the right of frame. A thick forearm under '
          'a heavy layer of black-and-grey hair, the skin olive-brown. The '
          'hand is wide, the palm calloused into a solid pad, the nails '
          'short and clean. A raised pink scar crosses the back of the hand '
          "between thumb and index from a table saw. A saint's medal on a "
          'thin chain has slipped down the wrist and hangs against the back '
          'of the hand as he reaches. His wedding band is worn on that '
          'chain, not on the finger.',
  'roupa': "Grey mechanic's shirt with a name patch on the chest, sleeve "
           'rolled to the elbow'},
 {'id': 'h76',
  'curto': 'Mãos de Toledo, dedos amarelados de nicotina',
  'fonte': 'construido',
  'presenca': 'maos',
  'idade': 66,
  'etnia': 'white',
  'desc': 'Hands of a 66-year-old white man in Toledo, Ohio. Big square '
          'hands, the knuckles broad and reddened, fingers short and thick '
          'with wide flat nails. Nicotine has stained the inside of the '
          'right index and middle fingers a permanent amber. Age spots begin '
          'at the wrists and thin out over the backs. The left thumb still '
          'shows the dark line of an old blood blister growing out of the '
          'nail. Coarse grey hair on the fingers, and a wide silver ring '
          'with a raised eagle on the right middle finger.',
  'roupa': ''},
 {'id': 'h77',
  'curto': 'Homem inteiro de San Jose, pinta com um fio ao lado do nariz',
  'fonte': 'construido',
  'presenca': 'corpo_inteiro',
  'idade': 72,
  'etnia': 'Asian American',
  'desc': 'A 72-year-old Chinese American man in San Jose, California, '
          'standing in full frame with a slight forward stoop. Slight build, '
          'narrow shoulders, thin arms, a small round belly. Face: oval with '
          'high flat cheekbones, a broad low nose bridge, deeply hooded '
          'eyelids, a long philtrum, thin lips, and skin drawn tight over '
          'the jaw with two deep folds at the mouth. The hair is still black '
          'and thick on top, white only at the sideburns, combed flat. A '
          'small brown mole with a single long hair grows beside the right '
          'nostril. Wire-frame glasses.',
  'roupa': 'Loose light-grey polo shirt tucked into elastic-waist trousers, '
           'canvas house shoes'},
 {'id': 'h78',
  'curto': 'Mãos de Memphis, cicatriz reta no dorso e anel de formatura',
  'fonte': 'construido',
  'presenca': 'maos',
  'idade': 57,
  'etnia': 'Black',
  'desc': 'Hands of a 57-year-old Black man in Memphis. Strong hands, medium '
          'brown, the palms much lighter, the fingers long with prominent '
          'knuckles gone slightly grey and dry. The nails are cut square, '
          'one thumbnail thickened and ribbed. A straight raised scar four '
          'inches long runs across the back of the left hand from the wrist '
          'toward the little finger, healed pale. A thin gold band sits on '
          'the left ring finger, and a wider class ring with a dark red '
          'stone on the right.',
  'roupa': ''},
 {'id': 'h79',
  'curto': 'Mãos pálidas de Vermont, hematomas de pele fina',
  'fonte': 'construido',
  'presenca': 'maos_antebraco',
  'idade': 74,
  'etnia': 'white',
  'desc': 'Both hands and forearms of a 74-year-old white man in Vermont. '
          'The skin is very pale, almost blue at the wrist, mapped with fine '
          'broken capillaries; the forearms are thin, the muscle wasted, the '
          'hair on them gone white and sparse. Large purple-brown patches of '
          'thin-skin bruising cover the backs of both hands. The nails are '
          'pale and ridged lengthwise. A dark tan wool sleeve keeps sliding '
          'down over the left wrist. A gold band worn thin as wire sits on '
          'the left ring finger.',
  'roupa': 'Heavy oatmeal wool cardigan over a checked flannel shirt, both '
           'sleeves pushed up'},
 {'id': 'h80',
  'curto': 'Tronco de Denver, nome tatuado ilegível no antebraço',
  'fonte': 'construido',
  'presenca': 'tronco',
  'idade': 60,
  'etnia': 'Hispanic',
  'desc': 'Torso of a 60-year-old Mexican American man in Denver, framed '
          'from the collarbones to the waistband, the chin and mouth in the '
          'top of frame with a black-and-grey moustache. A thick chest and '
          'shoulders built by years of concrete work, a solid belly, dark '
          'chest hair going white at the sternum. A hard tan line cuts '
          'across the biceps. On the left pectoral sits a small round scar '
          'the size of a dime. The right forearm carries a faded green '
          'tattoo of a name in cursive, now unreadable.',
  'roupa': 'Bare chest, grey sweatpants, a white towel around the neck'},
 {'id': 'h81',
  'curto': 'Mãos blackfeet de Browning, dois dedos que não abrem mais',
  'fonte': 'construido',
  'presenca': 'maos',
  'idade': 75,
  'etnia': 'Native American',
  'desc': 'Hands of a 75-year-old Blackfeet man in Browning, Montana. '
          'Big-boned hands, the skin brown and deeply weathered, cracked '
          'across the knuckles from cold and wind, the backs covered in fine '
          'white scratch-scars. The fingers are thick, the nails broad, one '
          'thumbnail split. The tendons stand out like wires. On the right '
          'hand the ring finger and little finger stay slightly curled — '
          'they no longer straighten. A worn leather thong is tied around '
          'the left wrist, its knot flattened by years.',
  'roupa': ''},
 {'id': 'h82',
  'curto': 'Mão de Wichita, calo de caneta no indicador',
  'fonte': 'construido',
  'presenca': 'maos_antebraco',
  'idade': 69,
  'etnia': 'white',
  'desc': 'Left hand and forearm of a 69-year-old white man in Wichita, '
          'Kansas. A long, sun-freckled forearm, the hair on it faded from '
          'red to white. The hand is narrow with long fingers and oval '
          'nails, and a hard yellow callus sits on the first joint of the '
          'index finger where a pen has rested for fifty years. Two flat '
          'brown sun spots mark the back of the hand, the larger one with an '
          'uneven edge. He wears a plain steel wristwatch on a leather strap '
          'gone soft and dark, buckled at the last hole.',
  'roupa': 'Short-sleeve plaid cotton shirt with the top button open'},
 {'id': 'h83',
  'curto': 'Homem inteiro de Oakland, sobrancelha partida por cicatriz',
  'fonte': 'construido',
  'presenca': 'corpo_inteiro',
  'idade': 64,
  'etnia': 'Black',
  'desc': 'A 64-year-old Black man in Oakland, California, in full frame at '
          'the edge of the tub. Medium height, heavy through the chest and '
          'stomach, thick arms. Face: square with a broad jaw, a wide flat '
          'nose, full lips, a close-cropped white beard along the jawline '
          'only, a shaved head with a faint grey shadow, deep horizontal '
          'lines across the forehead, and one eyebrow interrupted by a small '
          'old scar. The skin is dark and even, with a raised dark spot at '
          'the temple. His hands are large, with a gold band and a scar '
          'across the left palm.',
  'roupa': 'Sleeveless white undershirt, black basketball shorts, socks '
           'pushed down'},
 {'id': 'h84',
  'curto': 'Mãos de Portland, indicador torto de artrite e mancha de tinta',
  'fonte': 'construido',
  'presenca': 'maos',
  'idade': 73,
  'etnia': 'white',
  'desc': 'Hands of a 73-year-old white man in Portland, Oregon. Pale hands, '
          'thin skin, the veins standing high and blue-green over the backs, '
          'the tendons visible whenever the fingers move. Small brown spots '
          'dot the backs and thicken toward the wrist. The nails are trimmed '
          'short and clean, with a white ridge across the right middle nail. '
          'The left index knuckle is enlarged and reddened by arthritis, the '
          'finger deviating slightly outward. A permanent dark green ink '
          'stain sits in the crease of the right thumb.',
  'roupa': ''},
 {'id': 'h85',
  'curto': 'Tronco seco de Tucson, cicatriz sob as costelas',
  'fonte': 'construido',
  'presenca': 'tronco',
  'idade': 70,
  'etnia': 'Hispanic',
  'desc': 'Torso of a 70-year-old Hispanic man in Tucson, framed from the '
          'shoulders to the hips, the face cropped above the mouth so only a '
          'white moustache and chin remain. Thin and dried out by desert '
          'sun, the ribs showing at the sides, the skin brown and loose '
          'across the chest with sparse white hair. A long pale scar curves '
          'under the right ribs from an old surgery. Both forearms are '
          'darker than the chest, with a hard sleeve line at the biceps. His '
          'hands look too big for the arms, with wide flat nails.',
  'roupa': 'Bare chest, a tan towel folded over the shoulder, brown corduroy '
           'trousers'},
 {'id': 'h86',
  'curto': 'Mãos de Sacramento, mindinho torto de fratura mal curada',
  'fonte': 'construido',
  'presenca': 'maos_antebraco',
  'idade': 68,
  'etnia': 'Asian American',
  'desc': 'Both hands and forearms of a 68-year-old Vietnamese American man '
          'in Sacramento. Slim, almost hairless forearms, the skin a light '
          'golden brown scattered with small dark spots. The hands are '
          'narrow with long fingers and short trimmed nails; the left little '
          'finger bends sharply at the last joint from a break that healed '
          'on its own. A band of paler skin circles the right wrist where a '
          'watch normally sits. An oval, shiny burn scar marks the inside of '
          'the right forearm.',
  'roupa': 'Pale blue short-sleeve button-down, worn soft, hem untucked'},
 {'id': 'h87',
  'curto': 'Mãos de Buffalo, sardas fundidas em manchas e bracelete de cobre',
  'fonte': 'construido',
  'presenca': 'maos',
  'idade': 65,
  'etnia': 'white',
  'desc': 'Hands of a 65-year-old white man in Buffalo, New York. Heavy, '
          'meaty hands, the backs red and chapped from cold, the knuckles '
          'cracked and dry. The fingers are short and thick, the nails broad '
          'and cut with clippers, and the nail on the right middle finger is '
          'thickened and pale from an old crush. A dense field of freckles '
          'runs from the wrists over the backs, merging into sun spots. He '
          'wears a plain wide gold wedding band and, on the right wrist, a '
          'copper bracelet gone green underneath.',
  'roupa': ''},
 {'id': 'h88',
  'curto': 'Mãos lumbee de Pembroke, polegar achatado de trabalho',
  'fonte': 'construido',
  'presenca': 'maos',
  'idade': 71,
  'etnia': 'Native American',
  'desc': 'Hands of a 71-year-old Lumbee man from Pembroke, North Carolina. '
          'Wide hands, warm brown skin with a reddish cast, the backs '
          'covered in fine crosshatched wrinkles and a few flat dark spots. '
          'The palms are thickly calloused along the base of the fingers '
          'from tobacco and timber work. The right thumb is flattened and '
          'widened at the tip, the nail growing broad over it. A plain '
          'silver band, dented on one side, sits on the left ring finger. '
          'Short black-and-grey hair grows on the back of each finger.',
  'roupa': ''},
 {'id': 'h89',
  'curto': 'Mão de Jackson, quelóide redondo de vacina antiga',
  'fonte': 'construido',
  'presenca': 'maos_antebraco',
  'idade': 76,
  'etnia': 'Black',
  'desc': 'Right hand and forearm of a 76-year-old Black man in Jackson, '
          'Mississippi. The forearm is thin and dark, the skin loose and '
          'shining at the elbow, the hair almost entirely gone. Lighter '
          'mottled patches spread over the back of the hand where pigment '
          'has thinned with age. The knuckles are large and pale on top, the '
          'fingers long and slightly bent. A keloid as round as a coin sits '
          'on the forearm from an old vaccination. His nails are thick and '
          'ivory-coloured, cut square, with deep lengthwise ridges.',
  'roupa': 'White undershirt with a stretched collar, thin cotton, no sleeve '
           'past the shoulder'},
 {'id': 'h90',
  'curto': 'Tronco de Manchester, cicatriz de hérnia com marcas de ponto',
  'fonte': 'construido',
  'presenca': 'tronco',
  'idade': 59,
  'etnia': 'white',
  'desc': 'Torso of a 59-year-old white man in Manchester, New Hampshire, '
          'framed from the collarbones to the waist, the face cropped above '
          'the mouth leaving a dark stubbled chin with grey coming through '
          'it. A soft body, round shoulders, a heavy low belly, pale skin '
          'with dark chest hair going grey down the sternum. A four-inch '
          'scar with visible cross-marks runs low on the right abdomen from '
          'a hernia repair. A small cluster of red moles sits above the left '
          'nipple. The hands are broad and pink, a thick gold band cutting '
          'into the ring finger.',
  'roupa': 'Bare chest, navy flannel pyjama trousers, a grey towel bunched '
           'in the left hand'},
 {'id': 'h91',
  'curto': 'Mãos de Miami, ônix preto no anelar direito',
  'fonte': 'construido',
  'presenca': 'maos',
  'idade': 78,
  'etnia': 'Hispanic',
  'desc': 'Hands of a 78-year-old Cuban American man in Miami. The skin is '
          'thin and speckled, the tendons standing sharply, the backs mapped '
          'with purple-brown bruise patches. The fingers are long, the nails '
          'thick and slightly curved, trimmed carefully and buffed to a '
          'shine. He wears a heavy gold ring with a flat black onyx stone on '
          'the right ring finger, and a thin bracelet chain that has '
          'flattened the hair on the left wrist. The pads of the fingers are '
          'smooth and glossy.',
  'roupa': ''},
 {'id': 'h92',
  'curto': 'Homem inteiro de Salt Lake City, mancha rosa na têmpora',
  'fonte': 'construido',
  'presenca': 'corpo_inteiro',
  'idade': 66,
  'etnia': 'white',
  'desc': 'A 66-year-old white man in Salt Lake City, standing full length '
          'beside the tub with a slight lean to one side. Tall, narrow '
          'through the shoulders, long arms, a paunch pushing the shirt out. '
          'Face: long and rectangular with a heavy square chin, a straight '
          'thin nose, pale grey-blue eyes set deep under a shelf of brow, '
          'thin lips, and a deep vertical crease down each cheek. White hair '
          'thinning at the crown and worn a little long over the ears; heavy '
          'white eyebrows with one hair grown out long. A rough patch of '
          'pink skin sits on the left temple where a sun spot was frozen '
          'off.',
  'roupa': 'Faded green fishing shirt with two chest pockets, sleeves '
           'buttoned at the wrist, khaki trousers, leather slippers'},
 {'id': 'h93',
  'curto': 'Mão de Edison, cicatriz de porta de vidro na base do polegar',
  'fonte': 'construido',
  'presenca': 'maos_antebraco',
  'idade': 61,
  'etnia': 'Asian American',
  'desc': 'Left hand and forearm of a 61-year-old Indian American man in '
          'Edison, New Jersey. Medium brown skin, the forearm covered in '
          'fine dark hair with grey scattered through it. The hand is '
          'broad-palmed with short fingers and square nails, the cuticles '
          'dark and the nail beds slightly purple. A thick pale scar crosses '
          'the base of the thumb where a glass door caught him. A gold ring '
          'with a small red stone sits tight on the little finger, and a '
          'black thread is knotted around the wrist beside a plain steel '
          'watch.',
  'roupa': 'Olive short-sleeve knit polo, collar open, sleeve ending high on '
           'the arm'},
 {'id': 'h94',
  'curto': 'Mãos de Baltimore, queimadura brilhante no dorso',
  'fonte': 'construido',
  'presenca': 'maos',
  'idade': 70,
  'etnia': 'Black',
  'desc': 'Hands of a 70-year-old Black man in Baltimore, Maryland. '
          'Long-fingered, elegant hands with prominent knuckles and dark '
          'skin that goes grey and dry across the joints. The nails are '
          'longish and oval, one cracked vertically at the free edge. A '
          'large flat scald scar covers the back of the right hand, shiny '
          'and lighter than the surrounding skin. Two rings on the left: a '
          'plain gold band and, above it, a thinner band with a milled edge. '
          'Fine white hair grows on the back of each finger.',
  'roupa': ''},
 {'id': 'h95',
  'curto': 'Tronco do Arkansas, peixe desbotado no antebraço',
  'fonte': 'construido',
  'presenca': 'tronco',
  'idade': 63,
  'etnia': 'white',
  'desc': 'Torso of a 63-year-old white man in Arkansas, framed from the '
          'base of the neck to the belt, the face cropped above the mouth '
          'with a grey moustache showing. A long torso, sloping shoulders, a '
          'hard round belly, skin pale except for a deep red-brown neck and '
          'forearms. Grey chest hair thick down the middle. A long faded '
          'tattoo runs down the left forearm — a fish whose outline has '
          'blurred to green. The right hand holds the jar; its nails are '
          'broad and the index finger is stained yellow along the side.',
  'roupa': 'Bare chest, a white towel tucked at the waist over dark work '
           'trousers'},
 {'id': 'h96',
  'curto': 'Mãos de Milwaukee, coquí azulado no antebraço',
  'fonte': 'construido',
  'presenca': 'maos_antebraco',
  'idade': 56,
  'etnia': 'Hispanic',
  'desc': 'Both hands and forearms of a 56-year-old Puerto Rican man in '
          'Milwaukee, Wisconsin. The forearms are thick and still strong, '
          'covered in dark hair, the skin a light olive brown flushed red at '
          'the wrists. The hands are wide, the palms hard, the fingers short '
          'with broad nails cut down to the quick. A crescent-shaped scar '
          'sits at the base of the left thumb from a box knife. On the right '
          'forearm, a small faded tattoo of a coquí frog in blue-black ink '
          'has softened at the edges. His steel wedding band is scratched '
          'all over.',
  'roupa': 'Black T-shirt with a stretched neck, sleeves pushed up over the '
           'shoulders'},
 {'id': 'h97',
  'curto': 'Homem inteiro lummi, cabelo preso e pinta sob o olho',
  'fonte': 'construido',
  'presenca': 'corpo_inteiro',
  'idade': 62,
  'etnia': 'Native American',
  'desc': 'A 62-year-old Lummi man near Bellingham, Washington, standing in '
          'full frame in the bathroom doorway. Solid and broad, with a heavy '
          'chest and stomach and short thick legs. Face: wide and round with '
          'high broad cheekbones, a strong flat nose with a rounded tip, '
          'deep folds from nose to mouth, dark eyes set under straight heavy '
          'brows, and a wide mouth with a thin upper lip. Black hair, grey '
          'at the temples, pulled back and tied at the neck. A small dark '
          'mole sits under the left eye. His hands are broad, the nails wide '
          'and short.',
  'roupa': 'Dark red hooded sweatshirt with the sleeves pushed up, loose '
           'grey sweatpants, rubber shower sandals'},
 {'id': 'h98',
  'curto': 'Mãos de fazendeiro de Iowa, indicador levado pela rosca',
  'fonte': 'construido',
  'presenca': 'maos',
  'idade': 68,
  'etnia': 'white',
  'desc': 'Hands of a 68-year-old white farmer in eastern Iowa. Very large '
          'hands with thick fingers and deep-set nails, the skin on the '
          'backs weathered dark to the wrist and dead white above it. The '
          'knuckles are permanently swollen and the fingers no longer fully '
          'straighten. Dirt is worked into every crease of the right palm. '
          'The left index finger is short — the last joint taken by an auger '
          '— and the end is blunt and pink. A gold band, worn until its '
          'edges have gone to wire, sits below the swollen knuckle.',
  'roupa': ''},
 {'id': 'h99',
  'curto': 'Mão de Houston, queimadura de respingo e pulseira de contas',
  'fonte': 'construido',
  'presenca': 'maos_antebraco',
  'idade': 59,
  'etnia': 'Black',
  'desc': 'Right hand and forearm of a 59-year-old Black man in Houston. The '
          'forearm is thick and dark, with a raised vein running along the '
          'top and short black hair still without much grey. The hand is '
          'broad, the palm calloused into a hard ridge, the knuckles '
          'slightly ashy. A small round scar, purple-dark, sits on the back '
          'of the hand from a spatter burn. The nails are short and neat '
          'with wide white half-moons. A broad gold-tone watch sits high on '
          'the wrist, with a leather-and-bead bracelet below it.',
  'roupa': 'Charcoal athletic T-shirt, the short sleeve tight around the '
           'arm'},
 {'id': 'h100',
  'curto': 'Tronco de Providence, marca-passo saliente sob a clavícula',
  'fonte': 'construido',
  'presenca': 'tronco',
  'idade': 74,
  'etnia': 'white',
  'desc': 'Torso of a 74-year-old white man in Providence, Rhode Island, '
          'framed from the shoulders to the waist, the face cut off above '
          'the mouth leaving a slack chin with white stubble. Thin now, the '
          'chest fallen in, the skin loose and pleated across the sternum '
          'with sparse white hair. A pacemaker shows as a hard rectangular '
          'bulge under the skin below the left collarbone, the scar over it '
          'a thin white line. Age spots scatter across the shoulders. The '
          'hands are bony with huge knuckles, and the wedding band is held '
          'on only by the swollen joint.',
  'roupa': 'Bare chest under an open cotton bathrobe in faded burgundy, '
           'striped pyjama trousers'}]

# A familia MECANISMO do hook: idade ou condicao + o nome do ritual.
HOOKS_MECANISMO = [{'id': 'hm01',
  'fonte': 'lido',
  'txt': 'I am 67 and this is the shower hack that I use every time I go to '
         'bed to look bigger and last longer.',
  'palavras': 24},
 {'id': 'hm02',
  'fonte': 'lido',
  'txt': 'If you are single, do not try this, and if you are married, try '
         "this in moderation because ladies won't be able to keep up.",
  'palavras': 25},
 {'id': 'hm03',
  'fonte': 'lido',
  'txt': "Struggling to stay hard or with your small size? That's not about "
         'getting older. This morning trick flushes out the toxins.',
  'palavras': 21},
 {'id': 'hm04',
  'fonte': 'lido',
  'txt': "I'm 64 and fix my small bat with a shower habit.",
  'palavras': 11},
 {'id': 'hm05',
  'fonte': 'lido',
  'txt': 'Over 50 and tired of going soft or feeling small, this shower hack '
         'flushes clogs stopping your blood flow.',
  'palavras': 19},
 {'id': 'hm06',
  'fonte': 'lido',
  'txt': 'At 65, I wake up bigger than I did in my 20s with this trick.',
  'palavras': 15},
 {'id': 'hm07',
  'fonte': 'lido',
  'txt': 'Why accept a shrinking baton going soft? At 65, I stopped '
         'accepting it. This shower hack flushes the plaque choking your '
         'vessels.',
  'palavras': 22},
 {'id': 'hm08',
  'fonte': 'lido',
  'txt': 'Is going soft ruining the mood? A bizarre nighttime trick saved my '
         'marriage.',
  'palavras': 13},
 {'id': 'hm09',
  'fonte': 'lido',
  'txt': "Stop accepting a shrinking bat. I'm 65 and a bizarre nighttime "
         'habit restored my size down there.',
  'palavras': 17},
 {'id': 'hm10',
  'fonte': 'construido',
  'txt': 'If you are over 58 and still going soft, this shower ritual clears '
         'what is blocking you.',
  'palavras': 17},
 {'id': 'hm11',
  'fonte': 'construido',
  'txt': 'At 61 nobody warned me my pipes could clog. A bedtime rub opened '
         'them again.',
  'palavras': 15},
 {'id': 'hm12',
  'fonte': 'construido',
  'txt': 'My doctor blamed my age. I am 74, and this rub trick proved him '
         'wrong in three weeks.',
  'palavras': 18},
 {'id': 'hm13',
  'fonte': 'construido',
  'txt': 'I am 70 and I have not touched a blue pill since I learned this '
         'jar trick.',
  'palavras': 17},
 {'id': 'hm14',
  'fonte': 'construido',
  'txt': 'It is not your age. It is the buildup. At 63, this kitchen hack '
         'cleared mine out.',
  'palavras': 17},
 {'id': 'hm15',
  'fonte': 'construido',
  'txt': 'Every man past 65 should hear this once. A bizarre nighttime habit '
         'is why I still last all night.',
  'palavras': 19},
 {'id': 'hm16',
  'fonte': 'construido',
  'txt': 'I hid this shower hack from my wife for a year. I am 68, and she '
         'found out the fun way.',
  'palavras': 21},
 {'id': 'hm17',
  'fonte': 'construido',
  'txt': 'Over 70 and watching your bat shrink every year? This rub hack put '
         'the inches back.',
  'palavras': 16},
 {'id': 'hm18',
  'fonte': 'construido',
  'txt': 'The pharmacy on my corner wanted four hundred dollars a month. I '
         'am 66 and this jar trick costs me nothing.',
  'palavras': 21},
 {'id': 'hm19',
  'fonte': 'construido',
  'txt': 'At 59 I stopped believing my size was gone forever. One shower '
         'ritual, eight seconds, every night.',
  'palavras': 17},
 {'id': 'hm20',
  'fonte': 'construido',
  'txt': 'Are you 60 or older and quietly avoiding your wife at night? This '
         'bedtime rub ended that for me.',
  'palavras': 19},
 {'id': 'hm21',
  'fonte': 'construido',
  'txt': 'Do not tell your friends about this morning trick until you are '
         'over 55 and ready for what happens.',
  'palavras': 19},
 {'id': 'hm22',
  'fonte': 'construido',
  'txt': 'A retired trucker showed me this shower hack at 64. I have not '
         'gone soft since.',
  'palavras': 16},
 {'id': 'hm23',
  'fonte': 'construido',
  'txt': 'Ever wonder why 70 year old men give up? Their pipes are clogged. '
         'This rub trick unclogs them.',
  'palavras': 18},
 {'id': 'hm24',
  'fonte': 'construido',
  'txt': 'I was 67 and measuring smaller every year. Then a jar trick under '
         'my sink changed the number.',
  'palavras': 18},
 {'id': 'hm25',
  'fonte': 'construido',
  'txt': 'Two weeks after I turned 69, this bedtime rub gave me back what I '
         'thought retirement took.',
  'palavras': 17},
 {'id': 'hm26',
  'fonte': 'construido',
  'txt': 'I am 76 and I still surprise her. It took one bizarre nighttime '
         'habit and eight seconds a day.',
  'palavras': 19},
 {'id': 'hm27',
  'fonte': 'construido',
  'txt': 'Men at 62 accept a small bat like it is a law. This shower hack '
         'broke that law for me.',
  'palavras': 20},
 {'id': 'hm28',
  'fonte': 'construido',
  'txt': 'You are not finished at 71. You are blocked. One morning trick '
         'opens what your arteries closed.',
  'palavras': 17},
 {'id': 'hm30',
  'fonte': 'construido',
  'txt': 'They keep telling men over 65 that nothing can be done. This rub '
         'hack was built in my bathroom.',
  'palavras': 19},
 {'id': 'hm31',
  'fonte': 'construido',
  'txt': 'I am 60 and my wife thinks I found a doctor. I found a jar trick '
         'in my medicine cabinet.',
  'palavras': 20},
 {'id': 'hm32',
  'fonte': 'construido',
  'txt': 'Half the men at my class reunion were going soft. I was 68 and I '
         'had this shower hack.',
  'palavras': 19},
 {'id': 'hm33',
  'fonte': 'construido',
  'txt': 'If you are 73 and think the good nights are behind you, this '
         'bizarre nighttime trick says otherwise.',
  'palavras': 18},
 {'id': 'hm34',
  'fonte': 'construido',
  'txt': 'At 54 I was already the smallest I had ever been. A bedtime rub '
         'reversed it in a month.',
  'palavras': 19},
 {'id': 'hm36',
  'fonte': 'construido',
  'txt': 'Warning for men over 58: this shower ritual works fast, and your '
         'wife will notice before you do.',
  'palavras': 18},
 {'id': 'hm37',
  'fonte': 'construido',
  'txt': 'I spent 20 years blaming stress. At 64 I learned it was buildup, '
         'and one kitchen hack ended the excuses.',
  'palavras': 20},
 {'id': 'hm38',
  'fonte': 'construido',
  'txt': 'Do this jar trick if you are over 62 and you are tired of watching '
         'her pretend it is fine.',
  'palavras': 20},
 {'id': 'hm39',
  'fonte': 'construido',
  'txt': 'I was 63 and out of options. Then a jar trick from a supermarket '
         'aisle did what the clinic could not.',
  'palavras': 21},
 {'id': 'hm40',
  'fonte': 'construido',
  'txt': 'There is a reason I am 75 and never worry about the lights being '
         'on. It is a morning trick.',
  'palavras': 20},
 {'id': 'hm41',
  'fonte': 'construido',
  'txt': 'Does your bat look smaller in the mirror at 57? That is buildup, '
         'and this shower hack flushes it.',
  'palavras': 19},
 {'id': 'hm42',
  'fonte': 'construido',
  'txt': 'My wife stopped reaching for me when I hit 66. A bizarre nighttime '
         'habit changed that in eleven days.',
  'palavras': 19},
 {'id': 'hm43',
  'fonte': 'construido',
  'txt': 'The blockage builds for 30 years and hits you around 60. One '
         'bedtime rub melts it while you sleep.',
  'palavras': 19},
 {'id': 'hm44',
  'fonte': 'construido',
  'txt': 'Retired at 65, shrinking at 66, back to normal at 67. The '
         'difference was one morning trick.',
  'palavras': 17},
 {'id': 'hm45',
  'fonte': 'construido',
  'txt': 'Nobody at the pharmacy will tell a 70 year old man about this jar '
         'trick. It costs them money.',
  'palavras': 19},
 {'id': 'hm46',
  'fonte': 'construido',
  'txt': 'I am 62 and I did this bizarre nighttime trick out of desperation. '
         'Eight days later my wife asked questions.',
  'palavras': 20},
 {'id': 'hm48',
  'fonte': 'construido',
  'txt': 'Go ahead and blame 74 for going soft. I did too, until this shower '
         'hack proved the pipes were the problem.',
  'palavras': 21},
 {'id': 'hm49',
  'fonte': 'construido',
  'txt': 'I stopped counting on my body at 73. Then a shower ritual gave me '
         'back the only part that mattered.',
  'palavras': 20}]

# ⭐ A familia HISTORIA — o v11 virou eixo por ordem do operador.
HOOKS_HISTORIA = [{'id': 'hh01',
  'fonte': 'lido',
  'txt': "My wife almost cheated on me. She said to my face that I wasn't "
         'enough for her anymore. Then a buddy told me.',
  'palavras': 23},
 {'id': 'hh02',
  'fonte': 'construido',
  'txt': 'She took her pillow to the couch and stayed there nine nights. My '
         'neighbor saw the light on and told me about this.',
  'palavras': 23},
 {'id': 'hh03',
  'fonte': 'construido',
  'txt': 'Eleven years she reached for me first. Then she stopped, and never '
         'said why. My brother handed me this recipe at Thanksgiving.',
  'palavras': 22},
 {'id': 'hh04',
  'fonte': 'construido',
  'txt': 'Dinner went quiet for a whole year. Not one fight, just quiet. A '
         'guy behind me at the hardware store fixed that.',
  'palavras': 22},
 {'id': 'hh05',
  'fonte': 'construido',
  'txt': 'My wife laughed at me. Not cruel, which was worse. An Army vet in '
         'the VA waiting room told me what to do.',
  'palavras': 23},
 {'id': 'hh06',
  'fonte': 'construido',
  'txt': 'The doctor shrugged and blamed my age for the shrinking bat. The '
         'farrier at the county stable gave me a real answer instead.',
  'palavras': 23},
 {'id': 'hh07',
  'fonte': 'construido',
  'txt': 'Our fortieth anniversary and she booked two hotel rooms. A trucker '
         'at a Kentucky rest stop told me about this shower trick.',
  'palavras': 22},
 {'id': 'hh08',
  'fonte': 'construido',
  'txt': 'I found the divorce papers half filled out in her sock drawer. My '
         'barber saw my face and told me what he uses.',
  'palavras': 23},
 {'id': 'hh09',
  'fonte': 'construido',
  'txt': 'I heard her tell her sister I was a roommate now. A retired '
         'plumber on my street told me about this recipe.',
  'palavras': 22},
 {'id': 'hh10',
  'fonte': 'construido',
  'txt': 'I put my hand on her hip and she flinched. That is a thing you '
         "don't forget. My fishing partner told me this.",
  'palavras': 23},
 {'id': 'hh11',
  'fonte': 'construido',
  'txt': 'The lamp is off before I reach the stairs now. She used to wait '
         'up. A horse trainer told me what changed for him.',
  'palavras': 24},
 {'id': 'hh12',
  'fonte': 'construido',
  'txt': 'Eight years of saving for that cruise, and my wife cancelled it '
         'with no reason given. The man who mows my lawn told me.',
  'palavras': 24},
 {'id': 'hh13',
  'fonte': 'construido',
  'txt': 'It scared me worse than fighting when my wife stopped complaining. '
         'A seventy-year-old at my gym told me how his own year ended.',
  'palavras': 23},
 {'id': 'hh14',
  'fonte': 'construido',
  'txt': "We're too old for that now, she said, and rolled over. A rancher I "
         'buy hay from told me she was wrong.',
  'palavras': 22},
 {'id': 'hh15',
  'fonte': 'construido',
  'txt': 'Twenty inches of cold mattress between us every night for a year. '
         'My own father-in-law pulled me aside and told me this.',
  'palavras': 22},
 {'id': 'hh16',
  'fonte': 'construido',
  'txt': 'Jeans and a sweatshirt to bed, every night, for a year. That is a '
         "message. A night-shift nurse told me it wasn't age.",
  'palavras': 23},
 {'id': 'hh17',
  'fonte': 'construido',
  'txt': 'Thirty-one years of a kiss at the door. Then nothing, for six '
         'months. An old Navy chief told me about this shower habit.',
  'palavras': 23},
 {'id': 'hh18',
  'fonte': 'construido',
  'txt': "The recliner became my bed. She blamed my snoring, but it wasn't "
         'snoring. A guy at the VFW hall told me about this.',
  'palavras': 23},
 {'id': 'hh19',
  'fonte': 'construido',
  'txt': 'The pharmacist slid me a counseling pamphlet with the blue pills. '
         'The man behind me said my pipes were clogged, not my age.',
  'palavras': 23},
 {'id': 'hh20',
  'fonte': 'construido',
  'txt': 'Her ring came off to wash dishes in March and never went back on. '
         'My cousin told me about this recipe in April.',
  'palavras': 23},
 {'id': 'hh21',
  'fonte': 'construido',
  'txt': 'Two Christmases running, my wife signed the cards from both of us '
         'without asking. My mechanic told me about this shower trick.',
  'palavras': 22},
 {'id': 'hh22',
  'fonte': 'construido',
  'txt': "Don't worry about it. She said that three times in one week. A "
         'widower down the street heard me repeat it and told me.',
  'palavras': 24},
 {'id': 'hh23',
  'fonte': 'construido',
  'txt': 'Eleven at night, my wife smiling at her phone, and I knew. A '
         'beekeeper at the farmers market told me what to do.',
  'palavras': 23},
 {'id': 'hh24',
  'fonte': 'construido',
  'txt': 'She stopped using my name. Eight months of hey and you. A man at '
         'the dog park told me what shrinks the baton.',
  'palavras': 23},
 {'id': 'hh25',
  'fonte': 'construido',
  'txt': "You tried, that's what counts. I would rather she yelled at me. My "
         'golf partner told me about this the next morning.',
  'palavras': 22},
 {'id': 'hh26',
  'fonte': 'construido',
  'txt': 'There is a lock on my own guest room door now, and my wife put it '
         'there. My tile man told me this.',
  'palavras': 23},
 {'id': 'hh27',
  'fonte': 'construido',
  'txt': "A man's name came out of her mouth at dinner. Not mine. An old "
         'Marine at the barbershop told me what to mix.',
  'palavras': 23},
 {'id': 'hh28',
  'fonte': 'construido',
  'txt': 'My grown son asked me why his mother cries in the garage. I knew '
         'why. A bartender told me how to end it.',
  'palavras': 23},
 {'id': 'hh29',
  'fonte': 'construido',
  'txt': 'Our anniversary dinner got deleted from the kitchen calendar and '
         'book club written over it. A night guard at my building told me.',
  'palavras': 23},
 {'id': 'hh30',
  'fonte': 'construido',
  'txt': 'Twenty-two months without her hand on me. Not once. A rodeo hand '
         'at the fairgrounds told me the baseball bat is not the problem.',
  'palavras': 24},
 {'id': 'hh31',
  'fonte': 'construido',
  'txt': "Three girls' trips in one year, and she never once asked if I "
         'minded. A retired firefighter next door told me about this.',
  'palavras': 23},
 {'id': 'hh32',
  'fonte': 'construido',
  'txt': 'I love you like family, my wife said. Thirty years, and a small '
         'bat did that. A man at the range told me this.',
  'palavras': 24},
 {'id': 'hh33',
  'fonte': 'construido',
  'txt': 'Calm as a Sunday, my wife asked whether I would mind if she found '
         'company elsewhere. A cattle hauler told me about this.',
  'palavras': 23},
 {'id': 'hh34',
  'fonte': 'construido',
  'txt': "There was a therapist's card on my nightstand and she never said a "
         'word about it. My roofer told me about this recipe.',
  'palavras': 23},
 {'id': 'hh35',
  'fonte': 'construido',
  'txt': 'My wife asked me to move my things to the basement. More room, she '
         'said. An old cowboy at the feed store told me.',
  'palavras': 24},
 {'id': 'hh36',
  'fonte': 'construido',
  'txt': 'The perfume stopped. Small thing, but it meant my wife had quit on '
         'me. A poker friend told me about this trick.',
  'palavras': 22},
 {'id': 'hh37',
  'fonte': 'construido',
  'txt': 'Sixteen months, separate blankets, separate sides, separate lives. '
         'The stock clerk at my supermarket told me the fix was on aisle '
         'four.',
  'palavras': 22},
 {'id': 'hh38',
  'fonte': 'construido',
  'txt': "At my nephew's wedding she introduced me as her friend. My buddy "
         'had quit on me years before. A bowling teammate told me.',
  'palavras': 23},
 {'id': 'hh39',
  'fonte': 'construido',
  'txt': 'In front of the whole congregation, my wife prayed out loud for '
         'patience with me. A deacon caught me after and told me.',
  'palavras': 23},
 {'id': 'hh40',
  'fonte': 'construido',
  'txt': 'Four hundred days of fine and nothing else. That was my marriage. '
         'A man I served with called and told me about this.',
  'palavras': 23},
 {'id': 'hh41',
  'fonte': 'construido',
  'txt': 'A locksmith swapped our bedroom handle for one that locks. My wife '
         'ordered it. He looked at me and told me about this.',
  'palavras': 23},
 {'id': 'hh42',
  'fonte': 'construido',
  'txt': 'Her mother told me my wife calls us just friends now. Her uncle, '
         'of all people, told me what to do about it.',
  'palavras': 23},
 {'id': 'hh43',
  'fonte': 'construido',
  'txt': 'I quit sleeping. Sat in the kitchen at four every morning so she '
         "wouldn't have to lie next to me. A diner cook told me.",
  'palavras': 25},
 {'id': 'hh44',
  'fonte': 'construido',
  'txt': "Every evening my wife swam at the neighbor's pool and came home "
         'glowing. Not for me. Their pool man told me about this.',
  'palavras': 23},
 {'id': 'hh45',
  'fonte': 'construido',
  'txt': 'The television stays on all night now so we never have to talk. An '
         "auctioneer I've known thirty years told me about this.",
  'palavras': 23},
 {'id': 'hh46',
  'fonte': 'construido',
  'txt': 'The urologist wrote age-related on my chart and sent me home. A '
         'man in the waiting room told me that word is a lie.',
  'palavras': 24},
 {'id': 'hh47',
  'fonte': 'construido',
  'txt': 'The anniversary gift she opened was one she bought herself and '
         'signed from me. The man who delivers my propane told me this.',
  'palavras': 23},
 {'id': 'hh48',
  'fonte': 'construido',
  'txt': 'The porch light stopped coming on for me. Small thing. Felt like a '
         'door closing. A man at deer camp told me this.',
  'palavras': 23},
 {'id': 'hh49',
  'fonte': 'construido',
  'txt': 'At sixty-nine, my wife wanted a bigger house so we could each have '
         'our own bedroom. A man at the swap meet told me.',
  'palavras': 24},
 {'id': 'hh50',
  'fonte': 'construido',
  'txt': 'Just stop trying, please. My wife said it in the dark with her '
         'back to me. My mail carrier told me about this trick.',
  'palavras': 24}]

# ⛔ NENHUMA destas frases nomeia ingrediente. A lente VI1 cobra.
MECANISMOS = [{'id': 'mec_curto_01',
  'fonte': 'construido',
  'txt': 'It melts the invisible blockage choking your blood supply.',
  'palavras': 9},
 {'id': 'mec_curto_02',
  'fonte': 'construido',
  'txt': 'It flushes the build-up choking your blood flow.',
  'palavras': 8},
 {'id': 'mec_curto_03',
  'fonte': 'construido',
  'txt': 'It unclogs the toxic build-up stopping your blood flow.',
  'palavras': 9},
 {'id': 'mec_curto_04',
  'fonte': 'construido',
  'txt': 'It flushes the plaque choking your lower vessels.',
  'palavras': 8},
 {'id': 'mec_curto_05',
  'fonte': 'construido',
  'txt': 'It flushes the hidden blockages trapping your blood.',
  'palavras': 8},
 {'id': 'mec_curto_06',
  'fonte': 'construido',
  'txt': 'It clears the toxic buildup sitting in your arteries.',
  'palavras': 9},
 {'id': 'mec_curto_07',
  'fonte': 'construido',
  'txt': 'It melts what has been choking your blood supply.',
  'palavras': 9},
 {'id': 'mec_curto_08',
  'fonte': 'construido',
  'txt': 'It strips the plaque off your lower vessels.',
  'palavras': 8},
 {'id': 'mec_curto_09',
  'fonte': 'construido',
  'txt': 'It opens the pipes that stopped carrying blood.',
  'palavras': 8},
 {'id': 'mec_curto_10',
  'fonte': 'construido',
  'txt': 'It washes out what has been blocking you.',
  'palavras': 8},
 {'id': 'mec_curto_11',
  'fonte': 'construido',
  'txt': 'It dissolves the buildup strangling your blood flow.',
  'palavras': 8},
 {'id': 'mec_curto_12',
  'fonte': 'construido',
  'txt': 'It clears the clog and the blood comes back.',
  'palavras': 9},
 {'id': 'mec_curto_13',
  'fonte': 'construido',
  'txt': 'It flushes the toxins clogging your blood vessels.',
  'palavras': 8},
 {'id': 'mec_curto_14',
  'fonte': 'construido',
  'txt': 'It breaks up the plaque holding your blood back.',
  'palavras': 9},
 {'id': 'mec_curto_15',
  'fonte': 'construido',
  'txt': 'It empties the vessels that stopped filling.',
  'palavras': 7},
 {'id': 'mec_curto_16',
  'fonte': 'construido',
  'txt': 'It melts the blockage and blood flows on its own.',
  'palavras': 10},
 {'id': 'mec_curto_17',
  'fonte': 'construido',
  'txt': 'It scrubs the buildup out of your arteries.',
  'palavras': 8},
 {'id': 'mec_curto_18',
  'fonte': 'construido',
  'txt': 'It frees the blood your body stopped sending down.',
  'palavras': 9},
 {'id': 'mec_curto_19',
  'fonte': 'construido',
  'txt': 'It clears what age quietly packed into your vessels.',
  'palavras': 9},
 {'id': 'mec_curto_20',
  'fonte': 'construido',
  'txt': 'It drains the sludge choking your circulation.',
  'palavras': 7},
 {'id': 'mec_curto_21',
  'fonte': 'construido',
  'txt': 'It reopens the channel that closed on you.',
  'palavras': 8},
 {'id': 'mec_curto_22',
  'fonte': 'construido',
  'txt': 'It lifts the film blocking your blood supply.',
  'palavras': 8},
 {'id': 'mec_curto_23',
  'fonte': 'construido',
  'txt': 'It flushes decades of buildup in one night.',
  'palavras': 8},
 {'id': 'mec_curto_24',
  'fonte': 'construido',
  'txt': 'It loosens the plaque and the pressure returns.',
  'palavras': 8},
 {'id': 'mec_curto_25',
  'fonte': 'construido',
  'txt': 'It clears the passage your blood forgot.',
  'palavras': 7},
 {'id': 'mec_curto_26',
  'fonte': 'construido',
  'txt': 'It melts the clog while you sleep.',
  'palavras': 7},
 {'id': 'mec_curto_27',
  'fonte': 'construido',
  'txt': 'It pushes the blood back where it belongs.',
  'palavras': 8},
 {'id': 'mec_curto_28',
  'fonte': 'construido',
  'txt': 'It cleans out the vessels feeding you down there.',
  'palavras': 9},
 {'id': 'mec_curto_29',
  'fonte': 'construido',
  'txt': 'It removes the buildup no pill ever touched.',
  'palavras': 8},
 {'id': 'mec_curto_30',
  'fonte': 'construido',
  'txt': 'It unblocks what the pharmacy never fixed.',
  'palavras': 7},
 {'id': 'mec_curto_31',
  'fonte': 'construido',
  'txt': 'It flushes the gunk starving your blood flow.',
  'palavras': 8},
 {'id': 'mec_curto_32',
  'fonte': 'construido',
  'txt': 'It clears the toxins and the size comes back.',
  'palavras': 9},
 {'id': 'mec_curto_33',
  'fonte': 'construido',
  'txt': 'It thaws the blockage sitting in your arteries.',
  'palavras': 8},
 {'id': 'mec_curto_34',
  'fonte': 'construido',
  'txt': 'It sweeps the plaque out of the way.',
  'palavras': 8},
 {'id': 'mec_curto_35',
  'fonte': 'construido',
  'txt': 'It restores the flow that quietly stopped.',
  'palavras': 7},
 {'id': 'mec_curto_36',
  'fonte': 'construido',
  'txt': 'It opens what closed and the blood returns.',
  'palavras': 8},
 {'id': 'mec_curto_37',
  'fonte': 'construido',
  'txt': 'It dissolves what has been choking you for years.',
  'palavras': 9},
 {'id': 'mec_curto_38',
  'fonte': 'construido',
  'txt': 'It clears the line and the pressure comes back.',
  'palavras': 9},
 {'id': 'mec_curto_39',
  'fonte': 'construido',
  'txt': 'It flushes the buildup your doctor never mentioned.',
  'palavras': 8},
 {'id': 'mec_curto_40',
  'fonte': 'construido',
  'txt': 'It melts the blockage that shrank you.',
  'palavras': 7}]

# ⛔ Todas carregam o literal `Comment recipe,`. CT1 aplicado: o follow
# vem ANTES do CTA — divergencia deliberada da fonte, ordem do operador.
CTAS = [{'id': 'cta_01',
  'fonte': 'construido',
  'txt': 'Comment recipe, and I will send you the full video with the step '
         'by step, straight to your messages.',
  'palavras': 19},
 {'id': 'cta_03',
  'fonte': 'construido',
  'txt': 'Want the whole method? Comment recipe, and it arrives in your '
         'private messages within minutes.',
  'palavras': 15},
 {'id': 'cta_04',
  'fonte': 'construido',
  'txt': 'One word costs you nothing. Comment recipe, and the entire '
         'step-by-step shows up in your DMs.',
  'palavras': 16},
 {'id': 'cta_05',
  'fonte': 'construido',
  'txt': 'Do not ask me here. Comment recipe, and the full video goes '
         'straight to your inbox.',
  'palavras': 16},
 {'id': 'cta_06',
  'fonte': 'construido',
  'txt': 'No pharmacy, no blue pills. Comment recipe, and the whole method '
         'lands in your messages.',
  'palavras': 15},
 {'id': 'cta_07',
  'fonte': 'construido',
  'txt': 'Comment recipe, open your messages, and copy what you just '
         'watched.',
  'palavras': 11},
 {'id': 'cta_09',
  'fonte': 'construido',
  'txt': 'Still stuck with a shrinking bat? Comment recipe, and the full '
         'method hits your messages right away.',
  'palavras': 17},
 {'id': 'cta_10',
  'fonte': 'construido',
  'txt': 'Do not screenshot this. Comment recipe, and the clean full video '
         'goes straight to your inbox.',
  'palavras': 16},
 {'id': 'cta_11',
  'fonte': 'construido',
  'txt': 'Every man with a small baseball bat asked me the same thing. '
         'Comment recipe, and the answer reaches your messages.',
  'palavras': 20},
 {'id': 'cta_13',
  'fonte': 'construido',
  'txt': 'Your buddy has waited long enough. Comment recipe, and the full '
         'video arrives in your private messages.',
  'palavras': 17},
 {'id': 'cta_14',
  'fonte': 'construido',
  'txt': 'The word is recipe, nothing else. Comment recipe, and the '
         'step-by-step video appears in your inbox.',
  'palavras': 16},
 {'id': 'cta_15',
  'fonte': 'construido',
  'txt': 'Comment recipe, and the full method is in your messages before you '
         'finish this video.',
  'palavras': 15},
 {'id': 'cta_16',
  'fonte': 'construido',
  'txt': 'Over fifty and tired of hiding it? Comment recipe, and the full '
         'step-by-step goes to your messages.',
  'palavras': 17},
 {'id': 'cta_17',
  'fonte': 'construido',
  'txt': 'Two seconds of typing. Comment recipe, and my full video is '
         'sitting in your inbox.',
  'palavras': 15},
 {'id': 'cta_19',
  'fonte': 'construido',
  'txt': 'Comment recipe, and I send you the same video I sent my neighbor, '
         'straight to your inbox.',
  'palavras': 17},
 {'id': 'cta_20',
  'fonte': 'construido',
  'txt': 'Nothing exotic, nothing you cannot pronounce. Comment recipe, and '
         'the steps land in your messages.',
  'palavras': 15},
 {'id': 'cta_21',
  'fonte': 'construido',
  'txt': 'Another year like this one is a choice. Comment recipe, and the '
         'full method lands in your inbox.',
  'palavras': 18},
 {'id': 'cta_22',
  'fonte': 'construido',
  'txt': 'Comment recipe, and check your messages, because that is where the '
         'full video is going.',
  'palavras': 15},
 {'id': 'cta_23',
  'fonte': 'construido',
  'txt': 'It does not fit in a comment. Comment recipe, and the whole method '
         'reaches your messages instead.',
  'palavras': 17},
 {'id': 'cta_25',
  'fonte': 'construido',
  'txt': 'Men fixed their small bat with this. Comment recipe, and the full '
         'video goes to your messages.',
  'palavras': 17},
 {'id': 'cta_26',
  'fonte': 'construido',
  'txt': 'Comment recipe, and the step-by-step reaches your private messages '
         'without you asking twice.',
  'palavras': 13},
 {'id': 'cta_27',
  'fonte': 'construido',
  'txt': 'Read this before you swipe. Comment recipe, and the full method is '
         'delivered to your inbox.',
  'palavras': 16},
 {'id': 'cta_28',
  'fonte': 'construido',
  'txt': 'Comment recipe, and everything I just did here shows up in your '
         'messages, in order.',
  'palavras': 15},
 {'id': 'cta_29',
  'fonte': 'construido',
  'txt': 'Do it now, before you forget. Comment recipe, and the full video '
         'waits for you in your DMs.',
  'palavras': 18},
 {'id': 'cta_31',
  'fonte': 'construido',
  'txt': 'I will not repeat this on camera. Comment recipe, and the full '
         'method goes to your private messages.',
  'palavras': 18},
 {'id': 'cta_32',
  'fonte': 'construido',
  'txt': 'Your pipes can be clear by next week. Comment recipe, and the '
         'steps arrive in your messages.',
  'palavras': 17},
 {'id': 'cta_33',
  'fonte': 'construido',
  'txt': 'Comment recipe, and I will put the full video in your messages '
         'myself, one by one.',
  'palavras': 16},
 {'id': 'cta_34',
  'fonte': 'construido',
  'txt': 'Stop accepting a shrinking baton. Comment recipe, and the full '
         'step-by-step hits your inbox.',
  'palavras': 14},
 {'id': 'cta_36',
  'fonte': 'construido',
  'txt': 'Comment recipe, and the part I left out of this video goes into '
         'your messages.',
  'palavras': 15},
 {'id': 'cta_37',
  'fonte': 'construido',
  'txt': 'This took me twenty-one days. Comment recipe, and the full '
         'step-by-step reaches your inbox in seconds.',
  'palavras': 16},
 {'id': 'cta_38',
  'fonte': 'construido',
  'txt': 'My son thought this was nonsense until he tried it. Comment '
         'recipe, and the whole video is waiting in your messages.',
  'palavras': 21},
 {'id': 'cta_39',
  'fonte': 'construido',
  'txt': 'Comment recipe, and nobody else sees the answer, the full video '
         'goes quietly to your inbox.',
  'palavras': 16}]

# O instrumento de medida — eixo, e ele
# so' aparece onde a cena declarou `regua_cabe`.
REGUAS = [{'id': 'madeira_escolar',
  'curto': 'regua escolar de madeira',
  'fonte': 'lido',
  'img': 'A yellowed wooden school ruler lies flat beside them, untouched.'},
 {'id': 'madeira_em_pe',
  'curto': 'regua de madeira em pe',
  'fonte': 'lido',
  'img': 'A wooden ruler stands upright against the wall behind them, '
         'untouched.'},
 {'id': 'fita_metrica',
  'curto': 'fita metrica estendida',
  'fonte': 'lido',
  'img': 'A yellow tape measure lies extended beside them, untouched.'},
 {'id': 'madeira_escura',
  'curto': 'regua de nogueira',
  'fonte': 'lido',
  'img': 'A dark walnut ruler lies flat beside them, untouched.'},
 {'id': 'metal_dobravel',
  'curto': 'regua metalica dobravel',
  'fonte': 'construido',
  'img': 'A folding steel rule lies half-open beside them, untouched.'}]

# O rotulo fisico `growth hack`.
ROTULOS = [{'id': 'papelao',
  'curto': 'placa de papelao',
  'fonte': 'lido',
  'img': 'A brown corrugated cardboard sign with `growth hack` written on it '
         'in thick black marker leans against the wall behind.'},
 {'id': 'postit',
  'curto': 'post-it amarelo',
  'fonte': 'lido',
  'img': 'A yellow sticky note with `growth hack` written on it in blue pen '
         'lies flat in front.'},
 {'id': 'fita_crepe',
  'curto': 'fita crepe escrita',
  'fonte': 'construido',
  'img': 'A strip of masking tape with `growth hack` written on it in marker '
         'is stuck to the wall behind.'}]

# Os nomes do ritual — 5 lidos + 9
# construidos, por ordem do operador de aumentar o pool.
RITUAIS = ['shower hack',
 'kitchen hack',
 'morning trick',
 'bizarre nighttime trick',
 'bizarre nighttime habit',
 'gelatin hack',
 'rub hack',
 'gelatin trick',
 'rub trick',
 'shower ritual',
 'bedtime rub',
 'jar trick',
 'two-minute rub',
 'bathroom trick']


# ===========================================================================
# SORTEIO
# ===========================================================================
EIXOS_LEDGER = ("cena", "acao", "homem", "hook", "mecanismo", "cta")


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
            hist.setdefault(eixo, []).append(val.get("id"))


def _gravar_ledger(ledger, spec=None):
    if spec is not None:
        _anotar(ledger, spec)
    try:
        with open(LEDGER, "w", encoding="utf-8") as f:
            json.dump(ledger, f, ensure_ascii=False, indent=1)
    except IOError:
        pass


def _fresco(pool, usados, rng):
    """Uma entrada evitando as ultimas usadas — e CEDE quando nada sobra.

    ⛔ Pool grande com sorteio SEM memoria repete igual: licao do PEE 16. Com
    100 entradas por eixo a memoria pesa MAIS, nao menos — sem ela o operador
    veria a mesma cena duas vezes num lote de 30 e concluiria que o pool e'
    pequeno.
    """
    livres = [x for x in pool if x.get("id") not in usados]
    return rng.choice(livres or pool)


def _por_id(pool, valor, chave="id"):
    """Aceita o ID (string) OU a entrada ja' resolvida (o painel manda o dict)."""
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


# ⛔⛔ O MAPA DE VIZINHANCA — e ele existe porque a MEDICAO achou o buraco.
# Os pools de CENA e de ACAO foram escritos por agentes diferentes, e eles nao
# usaram o mesmo vocabulario de familia: `academia`, `ar_livre`, `nicho` e
# `outro` sairam com **zero acoes compativeis** — 36 das 100 cenas. O `_compat`
# cedia em silencio e a lente VI4 acusava em 73 de 200 sorteios.
# ⭐ A saida NAO foi reescrever 100 acoes: foi declarar de quem cada familia
# orfa toma emprestado. `nicho` E' um chuveiro; as 23 cenas de `outro` sao
# superficies secas domesticas (peitoril, radiador, carrinho, banquinho), que e'
# exatamente o que `pia` ja' cobre.
_FAM_VIZINHA = {
    "nicho": ("chuveiro",),
    "outro": ("pia", "cozinha"),
    "academia": ("pia", "chuveiro"),
    "ar_livre": ("pia", "praia", "jacuzzi"),
    "praia": ("jacuzzi", "ar_livre"),
}


def _familias_de(cena):
    """A familia da cena mais as de quem ela pode tomar gesto emprestado."""
    f = cena["familia"]
    return (f,) + _FAM_VIZINHA.get(f, ())


def _compat(cena, acoes):
    """As acoes que cabem NESTA cena.

    ⛔ E' aqui que o acoplamento vira codigo. `cabe_em` e' declarado na acao;
    `aceita` e' declarado na cena. Sem os dois, o sorteio monta um homem
    peneirando po numa espreguicadeira de praia.
    ⚠️ CEDE para a lista inteira se o cruzamento zerar — cena nova sem acao
    declarada nao pode derrubar o sorteio. Quem reclama e' o autoteste.
    """
    fams = _familias_de(cena)
    ok = [a for a in acoes
          if set(fams) & set(a["cabe_em"]) and _subst(a) in cena["aceita"]]
    return ok or [a for a in acoes if set(fams) & set(a["cabe_em"])] or list(acoes)


def _subst(acao):
    """A familia de substancia de uma acao, para casar com `aceita` da cena."""
    t = (acao.get("substancia") or "").lower()
    if "powder" in t:
        return "po"
    if "cube" in t:
        return "cubos"
    if "foam" in t or "froth" in t:
        return "espuma"
    if "liquid" in t or "syrup" in t or "honey" in t:
        return "liquido"
    return "creme"


def _falas(spec, rng, quais=(0, 1)):
    """As duas falas.

    ⛔⛔ QUEM ESCOLHE PRIMEIRO RESERVA O MINIMO. Regra medida no ESCANDALO 16:
    o beat que escolhe sem reservar prende o vizinho no teto.
    """
    f = dict(enumerate(spec.get("falas", ["", ""])))
    hooks = HOOKS_HISTORIA if spec.get("historia") else HOOKS_MECANISMO
    if 0 in quais:
        cands = [h for h in hooks
                 if _palavras(_fmt(h["txt"], spec)) <= TETO_FALA[1]
                 and _palavras(_fmt(h["txt"], spec)) >= PISO_FALA[1]]
        f[0] = _fmt(rng.choice(cands or hooks)["txt"], spec)
    if 1 in quais:
        # ⛔ O take 2 carrega MECANISMO + CTA na mesma fala, e o teto e' 25.
        # O CTA escolhe primeiro porque ele e' o beat que NAO pode encolher.
        # ⛔⛔ O PAR TEM DE CABER NOS 25, e escolher os dois soltos NAO cabia:
        # medido, o take 2 saia com 23/29/33 palavras e a lente VI9 acusava em
        # 197 de 200. Mecanismo (min 12) + CTA (min 11) so' fecha se os dois
        # forem escolhidos JUNTOS. Aqui o CTA e' sorteado e, se o par estourar,
        # ele encolhe ate' caber — o CTA e' o beat que nao pode sumir, o
        # mecanismo e' o que pode ser dito mais curto.
        # ⛔⛔ TODOS OS PARES QUE CABEM, e depois um sorteio entre eles — nao o
        # PRIMEIRO que cabe. A versao anterior ordenava por tamanho e pegava o
        # primeiro: medido, o take 2 saiu com **1 fala distinta em 200
        # sorteios**. Consertar o teto matando a variancia e' trocar um defeito
        # visivel por um invisivel, e o invisivel custa mais — 200 videos
        # dizendo a mesma frase e' o lote inteiro parecendo um so'.
        pares = [(c, m) for c in CTAS for m in MECANISMOS
                 # ⚠️ FOLGA DE 2: o `_um_apelido` roda DEPOIS e pode
                 # alongar a fala (`pipes` -> `shrinking baton` custa uma
                 # palavra). Medido: sem a folga, 13 de 400 estouravam o teto.
                 if _palavras(c["txt"]) + _palavras(m["txt"]) <= TETO_FALA[2] - 2]
        if pares:
            cta, m = rng.choice(pares)
        else:
            cta = min(CTAS, key=lambda x: _palavras(x["txt"]))
            m = min(MECANISMOS, key=lambda x: _palavras(x["txt"]))
        spec["cta"], spec["mecanismo"] = cta, m
        f[1] = "%s %s" % (m["txt"], cta["txt"])
    return f


def _fmt(txt, spec):
    return (txt.replace("{idade}", str(spec["homem"]["idade"]))
               .replace("{mecanismo}", spec["ritual"])
               .replace("{o}", spec["orgao"]))


def sortear(pagina, rng, ledger, travas=None):
    travas = travas or {}
    hist = (ledger or {}).get(pagina, {})

    cena = (_por_id(CENAS, travas["cena"]) if travas.get("cena")
            else _fresco(CENAS, hist.get("cena", [])[-12:], rng))
    acao = (_por_id(ACOES, travas["acao"]) if travas.get("acao")
            else _fresco(_compat(cena, ACOES), hist.get("acao", [])[-12:], rng))
    homem = (_por_id(HOMENS, travas["homem"]) if travas.get("homem")
             else _fresco(HOMENS, hist.get("homem", [])[-12:], rng))

    spec = {
        "pagina": pagina,
        "cena": cena, "acao": acao, "homem": homem,
        "ritual": rng.choice(RITUAIS),
        "orgao": rng.choice(NUCLEO),
        # ⭐ O segundo eixo de hook, por ordem do operador: 50/50 entre a
        # familia MECANISMO e a familia HISTORIA. E' eixo medido, nao gosto.
        "historia": (travas["historia"] if "historia" in travas
                     else rng.random() < 0.5),
        # ⛔ A regua e' eixo, e ela SO' aparece onde cabe. `regua_cabe` da cena
        # manda: regua de madeira numa sauna de madeira some no fundo.
        "regua": (rng.choice(REGUAS) if cena["regua_cabe"] and rng.random() < 0.6
                  else None),
        "rotulo": rng.choice(ROTULOS) if rng.random() < 0.75 else None,
    }
    spec["falas"] = [v for _, v in sorted(_falas(spec, rng).items())]
    spec["falas"] = _um_apelido(spec["falas"], spec["orgao"])
    return spec


def _um_apelido(falas, alvo):
    """⛔ UM apelido do orgao por video, nos DOIS takes — e' o CT4.

    Os hooks e os CTAs vem com o apelido JA' ESCRITO, e cada pool escolheu o
    seu: medido, o take 1 dizia `shrinking bat` e o take 2 `small bat` no mesmo
    video. Em 16s o corte zera a memoria de trabalho e o espectador remapeia.
    ⭐ Normalizar na saida e' mais barato e mais seguro que peneirar os pools:
    peneirar mataria copy boa por causa de UMA palavra que da' para trocar.
    """
    # ORDENADO DO MAIOR PARA O MENOR, e isso custou uma medicao inteira. A
    # alternacao do `re` e' PRIMEIRA-QUE-CASA, nao a mais longa: com
    # `shrinking bat` antes de `shrinking baton`, a troca comia so' o prefixo
    # e devolvia `shrinking bat` + `on` = `shrinking baton` de novo. O CT4
    # seguia acusando, e a causa estava AQUI e nao no pool de copy.
    termos = sorted(NUCLEO, key=len, reverse=True)
    rx = re.compile(r"\b(%s)\b" % "|".join(re.escape(n) for n in termos), re.I)
    return [rx.sub(alvo, f) for f in falas]


def nova_fala(spec, i, rng):
    return _falas(spec, rng, quais=(i,))[i]


# ===========================================================================
# MONTAGEM
# ===========================================================================
def _quem(h):
    """A frase de presenca — o eixo que o operador tornou sorteavel."""
    return {
        "maos": "Only his hands are in frame, no face and no body",
        "maos_antebraco": "Only his hands and one forearm are in frame, no face",
        "tronco": "He is in frame from the chest up, seen from behind or in "
                  "profile, his face never squared to the lens",
        "corpo_inteiro": "He is in frame standing, seen from behind",
    }[h["presenca"]]


def _corpo(h):
    if h["presenca"] == "maos":
        return h["desc"]
    return "%s, a %d-year-old %s man%s" % (
        h["desc"], h["idade"], h["etnia"],
        (", wearing %s" % h["roupa"]) if h.get("roupa") else "")


def montar(spec):
    c, a, h = spec["cena"], spec["acao"], spec["homem"]
    b = {}
    extras = []
    if spec["regua"]:
        extras.append(spec["regua"]["img"])
    if spec["rotulo"]:
        extras.append(spec["rotulo"]["img"])
    extra = (" " + " ".join(extras)) if extras else ""

    # ⛔ BLOCO 0 — a ancora de continuidade. Sem rosto na maioria dos videos, o
    # que atravessa o corte sao as MAOS: elas sao a identidade deste angulo.
    b["BLOCO 0 (REF)"] = (
        "REF 01: Photo of a real person's hands, %s. Plain neutral gray "
        "background, soft even frontal light, no objects, nothing else in "
        "frame. Slight sensor grain, raw iPhone photo aesthetic. No subtitles, "
        "no captions, no burned-in text, no watermark."
        % h["desc"])

    b["IMAGE 01/02"] = (
        "IMAGE 01/02: %s %s %s %s %s %s%s %s %s"
        % (c["ambiente"] + ".", "Resting on " + c["superficie"] + " is "
           + a["vasilhame"] + ".", a["t1_img"] + ".", _corpo(h) + ".",
           _quem(h) + ".", c["camera"] + ".", extra, c["luz"] + ".", CAUDA))

    # ⭐ O TAKE 2 e' o MESMO enquadramento com a substancia TRANSFORMADA. E' o
    # payoff da fonte: a mistura efervesce e a espuma sobe na borda.
    b["IMAGE 02/02"] = (
        # ⛔ A ANCORA VAI POR EXTENSO — `the same N-year-old E man`. Sem ela o
        # Veo desenha OUTRA pessoa no segundo quadro e o estranho fala a fala do
        # REF; foi medido em 161 de 200 antes desta linha existir.
        "IMAGE 02/02: %s Standing at the same %s is the same %d-year-old %s "
        "man from the first scene, %s. The same %s in the same framing, but "
        "the mixture has risen into a pale foam of large bubbles that reaches "
        "the rim. It is the same man and the same surface, not a different "
        "place. %s %s%s %s %s"
        % (c["ambiente"] + ".", c["superficie"], h["idade"], h["etnia"],
           h["desc"], a["vasilhame"], _quem(h) + ".", c["camera"] + ".",
           extra, c["luz"] + ".", CAUDA))

    b["TAKE 01/02"] = (
        "TAKE 01/02: Animate the provided image exactly. %s The camera does "
        "not move and there are no cuts. %s He does this once and stops. "
        "Audio: %s Only he speaks.\n"
        'Dialogue: "%s"'
        % (c["camera"] + ".", a["t1_take"] + ".", c["audio"] + ".",
           spec["falas"][0]))

    b["TAKE 02/02"] = (
        "TAKE 02/02: Animate the provided image exactly. %s The camera does "
        "not move and there are no cuts. The foam settles and moves very "
        "slightly; nothing else in the frame changes and no hand enters. "
        "Audio: %s Only he speaks.\n"
        'Dialogue: "%s"'
        % (c["camera"] + ".", c["audio"] + ".", spec["falas"][1]))

    return sc.selar_takes(sc.selar_tags(b))


# ===========================================================================
# AS LENTES
# ===========================================================================
def _vi1_mecanismo_mudo(spec, blocos, ach):
    """⛔⛔ A LENTE MAIS IMPORTANTE DESTE MOTOR.

    A fala NUNCA pode nomear o Vicks, a gelatina, o mel nem qualquer
    ingrediente — e' o CT5, e aqui ele e' o angulo inteiro: a imagem entrega a
    receita e a fala cobra o comentario por ela. Quem nomear na fala mata o
    motivo de comentar.
    """
    rx = re.compile(r"\b(vicks|vaporub|vapor rub|gelatin|gelatine|knox|honey|"
                    r"jell-?o|baking soda|vinegar|aloe|menthol|camphor)\b", re.I)
    for i, f in enumerate(spec["falas"], 1):
        m = rx.search(f)
        if m:
            ach.append(("ERRO", "VI1: a fala %d nomeia o ingrediente %r — a "
                                "imagem entrega a receita, a fala cobra o "
                                "comentario POR ela" % (i, m.group(0))))


def _vi2_mecanismo_no_quadro(spec, blocos, ach):
    """⭐ E o contrario tambem: o pote TEM de estar na imagem."""
    for k in ("IMAGE 01/02", "IMAGE 02/02"):
        if spec["acao"]["vasilhame"] not in blocos[k]:
            ach.append(("ERRO", "VI2: %s sem o vasilhame do mecanismo" % k))


def _vi3_continuidade(spec, blocos, ach):
    """As maos e a superficie sao a ancora entre os dois takes."""
    for k in ("IMAGE 01/02", "IMAGE 02/02"):
        if spec["homem"]["desc"] not in blocos[k]:
            ach.append(("ERRO", "VI3: %s sem a descricao das maos — sem rosto, "
                                "elas sao a unica ancora do corte" % k))
        if spec["cena"]["superficie"] not in blocos[k]:
            ach.append(("ERRO", "VI3: %s sem a superficie da cena" % k))


def _vi4_acoplamento(spec, blocos, ach):
    """⛔ A acao tem de caber na familia da cena. E' o defeito que a arquitetura
    existe para impedir — se ele aparecer aqui, o `_compat` cedeu."""
    if not set(_familias_de(spec["cena"])) & set(spec["acao"]["cabe_em"]):
        ach.append(("ERRO", "VI4: a acao %r nao cabe na familia %r — o cruzamento "
                            "cedeu e o quadro vai sair incoerente"
                    % (spec["acao"]["id"], spec["cena"]["familia"])))


def _vi5_regua(spec, blocos, ach):
    """A regua so' existe onde a cena disse que cabe."""
    if spec["regua"] and not spec["cena"]["regua_cabe"]:
        ach.append(("ERRO", "VI5: regua numa cena que declarou regua_cabe=False"))
    if spec["regua"] and spec["regua"]["img"] not in blocos["IMAGE 01/02"]:
        ach.append(("ERRO", "VI5: a regua sorteada nao chega ao quadro"))


def _vi6_uma_acao(spec, blocos, ach):
    """⛔ UMA acao por take. Duas e' o CT7 — o gerador escolhe uma e ignora a
    outra, e quem descobre e' o render."""
    t = spec["acao"]["t1_take"]
    if re.search(r"\b(and then|then he|after that|next he)\b", t, re.I):
        ach.append(("ERRO", "VI6: a acao %r encadeia dois gestos" % spec["acao"]["id"]))


def _vi7_orgao_solto(spec, blocos, ach):
    """⛔ O gesto nunca encosta no orgao — nem na imagem, nem no take."""
    rx = re.compile(r"\b(groin|genital|penis|crotch|manhood)\b", re.I)
    for k, v in blocos.items():
        if rx.search(v):
            ach.append(("ERRO", "VI7: %s poe o gesto no orgao — recusa certa "
                                "do gerador" % k))


def _vi8_hook_puro(spec, blocos, ach):
    """As duas familias de hook NUNCA se misturam no mesmo video."""
    f1 = spec["falas"][0].lower()
    tem_hist = bool(re.search(r"\b(wife|marriage|buddy|neighbou?r|brother|she)\b", f1))
    if spec["historia"] and not tem_hist:
        ach.append(("AVISO", "VI8: modo HISTORIA ligado e o hook nao conta uma"))
    if not spec["historia"] and tem_hist:
        ach.append(("AVISO", "VI8: modo MECANISMO e o hook conta uma historia"))


def _vi9_orcamento(spec, blocos, ach):
    for i, fala in enumerate(spec["falas"], 1):
        n = _palavras(fala)
        if n > TETO_FALA[i]:
            ach.append(("ERRO", "VI9: cena %d com %d palavras (teto %d) — a "
                                "fala e' cortada no render" % (i, n, TETO_FALA[i])))
        if n < PISO_FALA[i]:
            ach.append(("AVISO", "VI9: cena %d com so' %d palavras" % (i, n)))


def _vi10_fala_no_take(spec, blocos, ach):
    """⛔ A fala chega VERBATIM a linha Dialogue:. Copy aprovada nao se reescreve
    no caminho — e' a lente BA9 do BANHO 16 3T."""
    for i, k in enumerate(("TAKE 01/02", "TAKE 02/02")):
        if ('Dialogue: "%s"' % spec["falas"][i]) not in blocos[k]:
            ach.append(("ERRO", "VI10: a fala %d nao chega verbatim ao %s" % (i + 1, k)))


def _ct16(spec, blocos, ach):
    """O contrato de copy da familia 16s, com a excecao declarada.

    ⛔ O CT4b fica DESLIGADO neste motor: os apelidos do orgao sao os DA FONTE
    (`baseball bat`, `pipes`...), medidos nos 15 videos, e nao os
    `pecker`/`wiener`/`Johnson` do contrato. Precedente: o `banho16` desligou o
    mesmo CT4b por ordem do operador (*"somente jonhson e manhood"*).
    ⚠️ Os dois numeros continuam MEDIDOS pelo `medir_copy16` — o que muda e' que
    a decisao aparece rotulada, em vez de o gate acusar copy que esta' certa.
    """
    fora = []
    sc.lint_copy16(sys.modules[__name__], spec, fora)
    ach.extend(x for x in fora if not x[1].startswith("CT4b:"))


def _anticeleb(spec, blocos, ach):
    sc.lint_anticeleb(blocos, ach)


def _painel(spec, blocos, ach):
    sc.lint_painel_honesto(sys.modules[__name__], spec, blocos, ach)


def lint(spec, blocos):
    # ⚠️ As lentes proprias entram por `extras=`, que e' o idioma do repo — nao
    # numa lista paralela. Assim `lint_curto` continua sendo o unico ponto que
    # decide a ordem, e uma lente nova nao pode ficar orfa de chamada.
    return sc.lint_curto(
        sys.modules[__name__], spec, blocos, (1, 2), TETO_FALA,
        literais=("recipe",), cota_min=0,
        extras=(_ct16, _anticeleb, _painel,
                _vi1_mecanismo_mudo, _vi2_mecanismo_no_quadro, _vi3_continuidade,
                _vi4_acoplamento, _vi5_regua, _vi6_uma_acao, _vi7_orgao_solto,
                _vi8_hook_puro, _vi9_orcamento, _vi10_fala_no_take))


# ===========================================================================
# RESUMO E PAINEL
# ===========================================================================
def resumo_pt(spec):
    c, a, h = spec["cena"], spec["acao"], spec["homem"]
    return ("16s, DOIS takes. CENA: %s (%s). O GESTO: %s. QUEM: %s, %d anos, "
            "%s%s. O ritual chama-se %r e o apelido do orgao e' %r. Hook da "
            "familia %s. %s%s Take 2 — a MESMA cena com a mistura virada "
            "ESPUMA na borda. Fecha no CTA (`recipe`), e a fala NUNCA nomeia "
            "o ingrediente."
            % (c["curto"], c["familia"], a["curto"], h["curto"], h["idade"],
               {"maos": "so as maos", "maos_antebraco": "maos e antebraco",
                "tronco": "tronco", "corpo_inteiro": "corpo inteiro"}[h["presenca"]],
               "" if h["fonte"] == "lido" else " [construido]",
               spec["ritual"], spec["orgao"],
               "HISTORIA" if spec["historia"] else "MECANISMO",
               ("Regua: %s. " % spec["regua"]["curto"]) if spec["regua"] else "Sem regua. ",
               ("Rotulo: %s. " % spec["rotulo"]["curto"]) if spec["rotulo"] else ""))


EIXOS_UI = [
    ("cena", "A CENA", "CENAS", "curto"),
    ("acao", "O GESTO", "ACOES", "curto"),
    ("homem", "QUEM", "HOMENS", "curto"),
]
EIXOS_TRAVAVEIS = ["cena", "acao", "homem"]
TRAVAS_UI = [("historia", "hook", ["livre", "mecanismo", "historia"])]
DROPDOWNS_UI = [("cena", "A CENA", "CENAS", "curto"),
                ("homem", "QUEM", "HOMENS", "curto")]
IGNORA_PAINEL = ("historia",)


# ===========================================================================
# AUTOTESTE
# ===========================================================================
def _autoteste(n=400, seed=20260815):
    rng = random.Random(seed)
    led = {}
    erros = collections.Counter()
    vistos = {k: collections.Counter() for k in ("cena", "acao", "homem")}
    fam = collections.Counter()
    pres = collections.Counter()
    falas = {1: set(), 2: set()}
    pal = {1: [], 2: []}
    hist = 0
    for _ in range(n):
        sp = sortear("joe", rng, led)
        _anotar(led, sp)
        bl = montar(sp)
        for nivel, txt in lint(sp, bl):
            if nivel == "ERRO":
                erros[txt.split(":")[0]] += 1
        for k in vistos:
            vistos[k][sp[k]["id"]] += 1
        fam[sp["cena"]["familia"]] += 1
        pres[sp["homem"]["presenca"]] += 1
        hist += bool(sp["historia"])
        for i in (1, 2):
            falas[i].add(sp["falas"][i - 1])
            pal[i].append(_palavras(sp["falas"][i - 1]))

    print("%s — %d sorteios (seed %d)" % (APP, n, seed))
    for k, alvo in (("cena", CENAS), ("acao", ACOES), ("homem", HOMENS)):
        print("  %-6s %3d/%3d alcancados · min %2dx · max %2dx"
              % (k, len(vistos[k]), len(alvo),
                 min(vistos[k].values()), max(vistos[k].values())))
    print("  familias de cena: %d de %d" % (len(fam), len({c["familia"] for c in CENAS})))
    print("  presenca: %s" % dict(pres))
    print("  hook HISTORIA em %d%% dos videos" % (100 * hist // n))
    for i in (1, 2):
        print("  cena %d: %3d falas distintas · palavras %d/%d/%d"
              % (i, len(falas[i]), min(pal[i]), sum(pal[i]) // len(pal[i]), max(pal[i])))
    print("  lidos x construidos: cenas %d/%d · acoes %d/%d · homens %d/%d"
          % (sum(1 for x in CENAS if x["fonte"] == "lido"), len(CENAS),
             sum(1 for x in ACOES if x["fonte"] == "lido"), len(ACOES),
             sum(1 for x in HOMENS if x["fonte"] == "lido"), len(HOMENS)))
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
    led = _carregar_ledger()
    sp = sortear(a.pagina, rng, led)
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
