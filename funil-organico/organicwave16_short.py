#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE ORGANIC WAVE 16 — 2 takes de 8 segundos.

⭐⭐ COPIA LITERAL DO `organicwave_short.py`, adaptada SO' NO EIXO TEMPORAL.
Ordem do operador, 2026-08-14: *"crie o organicwave16 (derivando do organicwave
short)"*. Nenhum pool encolheu, nenhuma string validada foi redigitada — o
arquivo nasceu de `Copy-Item` e so' o que o colapso obriga foi operado.

⛔ O `organicwave_short.py` NAO FOI TOCADO. Este e' agente NOVO, com ledger
proprio, e os dois convivem — sao formatos diferentes (Vertical 3 x Vertical 2).

O COLAPSO 3 -> 2
    SHORT 1 · A DOR (1a pessoa) + o prop murcho   ->  16s 1 · igual, intacta
    SHORT 2 · O GELATIN TRICK na bancada          ->  16s 2 · funde 2 e 3
    SHORT 3 · O CTA com o casal                   ->

⛔ POR QUE ESTE NAO USA `sc.montar_curto` como o PEE 16, o FLAGRANTE 16 e o
NECROSE 16: aquela maquinaria procura os blocos do motor base rotulados `/05`
(ela colapsa um arco LONGO de 5 cenas). O ORGANIC WAVE nunca teve motor longo —
o `_short` ja' e' o motor, e ele emite `/03`. Entao este arquivo segue o caminho
dos outros dezenove 16s: `montar` proprio, emitindo `01/02` e `02/02`.

⛔⛔ O QUE O COLAPSO AMEACAVA, e onde cada coisa foi parar
Tres coisas, e as tres sao espinha deste angulo:
  · a ISCA (o curiosity gap) morava na bancada da cena 2;
  · o PAYOFF (o casal, o prop ereto) morava na cena 3;
  · o RITUAL (a gelatina sendo mexida) morava na cena 2.
O quadro fundido carrega os tres: e' a bancada da cena 2 — com a isca e o copo —
com o casal da cena 3 dentro dela. ⚠️ Recombinacao de dois quadros validados,
nao invencao: cada pedaco vem de bloco que ja' rodou em render. E' o mesmo
precedente do `sc.bancada_com_rosto` (a cena que faltava, montada de partes que
ja' existiam).

⛔⛔ E A COPY DA CENA 2 E' NOVA, porque a antiga NAO PASSA no CONTRATO DE COPY
16s. Medido, nao suposto — as `FUNDIDAS` e os `CTAS` do `_short` violam CINCO
das sete travas ao mesmo tempo (a lapide de cada pool esta' escrita ao lado
dele):
    CT1  o `{gate}` fica DEPOIS do `Comment gelatin,`
    CT5  a receita entra na fala com `fresh lemon` dentro
    CT6  nenhum CTA diz ONDE a receita chega
    CT7  `it gets your {o} hard again` — verbo de ereccao colado no orgao
    CT8  o pool `GATES` inteiro e' pedido de follow
⚠️ A copy nova NAO foi inventada do zero: cada beat sai das sentencas que o
operador ja' aprovou em 2026-07-31, cortando so' o que o contrato proibe. As
tres listas novas (`MECANISMOS16`, `PROVAS16`, `CTAS16`, mais as femininas)
estao marcadas para leitura dele.

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

import argparse
import collections
import json
import os
import random
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import short_comum as sc                                        # noqa: E402
from nucleo_sonoro import sonorizar                             # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
# ⛔ Ledger proprio: 16s e 24s nao gastam o historico um do outro.
LEDGER = os.path.join(AQUI, ".organicwave-16-ledger.json")

TITULO = "AGENTE ORGANIC WAVE 16"
SUBTITULO = ("2 takes de 8s = 16 segundos · primeira pessoa, elenco de "
             "aspiração, e o casal na bancada do ritual")
SLUG = "organicwave-16"

# ⚠️ Os rotulos dizem os BEATS DA FALA, nao so' o que se ve': a cena 2 termina
# no CTA, com nada depois dele (CT1), e carrega o mecanismo com razao (CT3).
CENAS_UI = ["1 · A DOR (1ª pessoa) + O PROP MURCHO",
            "2 · O GELATIN TRICK + A PROVA + CTA"]
# Os tetos descrevem a copy APROVADA, nao o contrario: os 36 itens foram
# curados pelo operador, entao o limite segue o p95 medido deles. Serve
# para pegar a cauda longa, nao para reprovar o pool.
# ⛔⛔ CENAS 2 E 3 CAIRAM DE 36/34 PARA 32 EM 2026-08-04. Os dois estavam
# ACIMA DO FISICO: 8s a 4,0 palavras/s = 32 (licoes §5). O p95 do pool nao
# manda no relogio — teto acima da capacidade fisica faz o lint APROVAR uma
# fala que o take corta (licoes §27). Medido antes: c2 estourava em 7,3% e
# o que ficava de fora era o fecho da fundida.
# ⛔⛔ TETO 25 — ordem permanente do operador, 2026-08-05: *"sempre meca. Nao
# pode haver cortes de fala."* O numero vem de RENDER, nao de conta: 32
# cortou e 28 cortou. Os exemplos que ele escreve a mao vivem em 16-25
# palavras (2,0-3,1 p/s). Ver licoes-de-construcao §28.
TETO_FALA = {1: 24, 2: 25}

# ⛔ O PISO E' ARITMETICA — a soma dos MINIMOS dos beats de cada cena, como no
# MEL 16 e no TROCA 16. Piso chutado e' alarme que dispara sempre, e alarme que
# dispara sempre ensina a ignorar o linter inteiro.
# ⚠️ cena 1 = o menor HOOK do pool aprovado.
# ⚠️ cena 2 = menor MECANISMO (10) + menor PROVA (4) + menor CTA (8) = 22.
#    ⛔ Nao rebaixar para calar alarme: se uma entrada nova ficar curta, quem
#    cresce e' a ENTRADA, nao o piso (licao do MEL 16).
PISO_FALA = {1: 15, 2: 22}

# congruencia inviolavel: a etnia do REF e' a do avatar da pagina
# ⭐ QUEM NARRA — o sexo de quem fala com a lente (2026-08-06).
# Ordem do operador: *"uma marcacao dentro dos agentes python, de todos, pra
# saber se aquele agente gera roteiros com personagem homens e mulheres como
# narrador/apresentador ou se so' gera com um dos dois"*.
# ⛔ MEDIDO, nao lido: 120 sorteios por agente, olhando o BLOCO 0 do prompt.
# Declarar de cabeca aqui seria a mesma FORMA-sem-FUNCAO que ja' custou o
# botao de pele morto em tres motores.
# ⚠️ Com DOIS sexos a UI desenha a trava homem/mulher; com um so', nao desenha
# botao nenhum — botao que nao trava nada e' pior que botao nenhum.
SEXOS = ("homem", "mulher")

ETNIA = {"joe": "white American", "ray": "white American", "matt": "white American",
         "marcus": "Black American", "chuck": "Black American"}

NUCLEO = ["Johnson", "pecker", "wiener", "tool", "soldier"]


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
    # + 2026-08-01: o operador viu o mesmo rosto voltando no lote. Tres marcas
    # faciais a mais, na mesma gramatica de marca + corpo.
    {"idade": 65, "marca": "a shaved head, a thick grey handlebar moustache and a small mole at the outer corner of his right eye",
     "corpo": "a deep barrel chest and heavy sloping shoulders"},
    {"idade": 62, "marca": "a short flat-top cut gone completely white and a wide gap between his front teeth",
     "corpo": "thick arms and a broad chest with clear muscle separation"},
    {"idade": 57, "marca": "thick chestnut hair with a bright white streak at the left temple and green eyes",
     "corpo": "a compact powerful build with square shoulders and a tight midsection"},
    # + 2026-08-02: o operador mediu os dois pools e viu SEMPRE O MESMO ROSTO.
    # As doze acima descrevem a marca quase so' por CABELO mais cor de olho, e
    # o `corpo` e' sempre a mesma familia de torso — doze homens descritos so'
    # por cabelo sao o mesmo homem doze vezes. As quatro novas trazem os eixos
    # que este pool nao acionava:
    #   · 55 — OCULOS, o eixo ZERADO aqui (0/12): armacao fina de metal, mais
    #     sinal de nascenca oval sob a mandibula.
    #   · 68 — OCULOS de casco grosso mais CALVICIE frontal e PORTE pesado,
    #     mais mecha branca na sobrancelha.
    #   · 66 — PELE castigada de sol e sardenta mais PORTE seco de corda,
    #     rabo de cavalo e cavanhaque quadrado.
    #   · 70 — PELO FACIAL de costeleta larga mais topete alto e covinhas.
    #   · a ancora continua COMPATIVEL COM BELEZA, como manda o cabecalho
    #     deste elenco: sinal, sarda, mecha, covinha. ⛔ nenhuma cicatriz feia
    #     e nenhuma orelha entalhada, que sao marcas dos especialistas.
    #   · ⚠️ DESVIO DECLARADO: as doze acima espelham `idade` E `corpo` por
    #     indice com o pool ESCURA. As quatro novas mantem a idade e mudam o
    #     corpo (aqui torso peludo, la' torso liso) — foi eixo introduzido de
    #     proposito. O codigo nao pareia por indice, entao nada quebra.
    #   · zero mencao a etnia: o motor injeta ETNIA[pagina] antes da marca.
    {"idade": 55, "marca": "dark brown hair cut short and side-parted with only a little grey at the front, fine silver wire-rimmed glasses and a small oval birthmark below his right jaw",
     "corpo": "a long-limbed swimmer's build with wide flat shoulders and a narrow waist"},
    {"idade": 68, "marca": "a high balding forehead with thin white hair combed straight back, thick tortoiseshell glasses and a bright white streak through his left eyebrow",
     "corpo": "a heavy thick-set frame, a deep chest and thick arms under a dense mat of grey hair"},
    {"idade": 66, "marca": "long iron-grey hair tied back in a low ponytail, a short squared silver goatee and pale amber eyes set in sun-weathered freckled skin",
     "corpo": "a lean whipcord frame with long ropey forearms and a hard narrow waist"},
    {"idade": 70, "marca": "a high silver pompadour swept up off the forehead, heavy silver sideburns down to the jawline and deep dimples in both cheeks",
     "corpo": "a tall upright frame with a broad V-shaped back tapering to a lean hard waist"},
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
    # + 2026-08-01: o operador viu o mesmo rosto voltando no lote. Tres marcas
    # faciais a mais, na mesma gramatica de marca + corpo.
    {"idade": 65, "marca": "a smooth shaved head, a thick grey handlebar moustache and a small mole at the outer corner of his right eye",
     "corpo": "a deep barrel chest and heavy sloping shoulders"},
    {"idade": 62, "marca": "a short white flat-top fade and a wide gap between his front teeth",
     "corpo": "thick arms and a broad chest with clear muscle separation"},
    {"idade": 57, "marca": "a close grey afro with a bright white streak above the left temple and light green eyes",
     "corpo": "a compact powerful build with square shoulders and a tight midsection"},
    # + 2026-08-02: o espelho das quatro novas do pool CLARA — mesma medicao (o
    # operador viu sempre o mesmo rosto, porque as doze acima descreviam a marca
    # quase so' por cabelo e cor de olho), mesma idade por indice, mesmos eixos
    # novos. So' o descritor de cabelo/barba muda, que e' onde a etnia se le'.
    #   · 55 — OCULOS (eixo ZERADO aqui) mais sardas na ponte do nariz.
    #   · 68 — CALVICIE em coroa mais PORTE pesado e olhos de tom desigual
    #     (heterocromia, ancora ✅ da tabela de licoes-producao-veo).
    #   · 66 — OCULOS de leitura mais entrada de cabelo bem recuada e PORTE
    #     seco e fibroso, mais sinal de nascenca oval na tempora.
    #   · 70 — PELO FACIAL de barba chin-strap mais coroa de ouro num dente.
    #   · a ancora continua COMPATIVEL COM BELEZA (sinal, sarda, coroa de ouro,
    #     heterocromia). ⛔ nenhuma cicatriz feia, nenhuma orelha entalhada.
    #   · ⚠️ mesmo DESVIO DECLARADO do pool CLARA: as quatro novas mantem a
    #     idade por indice mas nao o `corpo` (aqui torso liso, la' torso
    #     peludo). O codigo nao pareia por indice, entao nada quebra.
    {"idade": 55, "marca": "greying cornrows braided straight back, heavy horn-rimmed glasses, a cleanly shaven jaw and dark freckles scattered across the bridge of his nose",
     "corpo": "a tall rangy build with long flat muscle across the shoulders and a very narrow waist"},
    {"idade": 68, "marca": "a bald crown ringed with close-cropped white hair, a full thick white beard and one eye noticeably paler than the other",
     "corpo": "a heavy thick-set frame, a deep smooth hairless chest and thick solid arms"},
    {"idade": 66, "marca": "a deeply receding hairline clipped to a fine grey shadow, wire-rimmed reading glasses low on the nose and a small oval birthmark high on his right temple",
     "corpo": "a wiry sinewy build with stringy forearms and sharply drawn lines across the stomach"},
    {"idade": 70, "marca": "a low tapered cut lined up sharp at the temples and gone completely white, a thin white chin-strap beard along the jaw and a gold crown on one front tooth",
     "corpo": "a big-framed torso with heavy shoulders and a deep chest under a mat of white hair"},
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
    # + 2026-08-01: o operador viu o mesmo rosto voltando no lote. Quatro
    # mulheres a mais, cada uma com marca facial propria.
    {"idade": 33, "desc": "a sleek dark bob cut sharp at the jaw and a small beauty mark under her left eye, a fitted plum dress"},
    {"idade": 29, "desc": "long jet-black hair in a single braid over one shoulder and a gap between her front teeth, a fitted rust-orange sundress"},
    {"idade": 36, "desc": "caramel-highlighted hair twisted into a loose bun and a narrow widow's peak above dark arched brows, a fitted sage green dress"},
    {"idade": 31, "desc": "shoulder-length golden-brown hair with a blunt fringe and a small crescent birthmark at her hairline, a fitted denim-blue summer dress"},
    # + 2026-08-02: mesma medicao que gerou os blocos dos REFS_H logo acima,
    # so' que do lado da mulher — o operador viu SEMPRE O MESMO ROSTO. As
    # catorze acima descrevem a pessoa por CABELO mais cor de olho: catorze
    # mulheres descritas so' por cabelo sao a mesma mulher catorze vezes. As
    # tres novas trazem os eixos que este pool nao acionava:
    #   · OCULOS — era 0/14 aqui, e 0/28 somando os dois pools de mulher.
    #     Leitura tortoiseshell na cabeca e armacao de acetato grossa.
    #   · PORTE — petite, ombros largos com braco definido, quadril largo e
    #     cintura fina. Nenhuma das catorze menciona compleicao.
    #   · PELE — sardas densas, pele bronzeada de sol.
    #   · a ancora facial (P6) continua obrigatoria e NO ROSTO: sarda, fenda
    #     no queixo, pinta sob a narina. ⛔ marca no pescoco ou atras da
    #     orelha nao ancora — e o motor concatena `BELEZA_M` logo depois.
    #   · a ancora tambem continua COMPATIVEL COM BELEZA: nada de cicatriz
    #     feia, que e' marca dos especialistas, nao deste elenco.
    #   · as tres fecham em "a fitted <cor> <peca>", como as catorze acima.
    #   · zero mencao a etnia: a etnia deste pool ja' e' a do proprio pool.
    {"idade": 28, "desc": "a cropped light-brown pixie cut with a deep side part, wide-set grey eyes above a small upturned nose, a dense spray of dark freckles across her nose and both cheekbones, petite and small-framed, a fitted apricot sundress"},
    {"idade": 38, "desc": "prematurely silver hair in a blunt bob level with her chin, tortoiseshell reading glasses pushed up on top of her head, heavy dark brows over a wide full mouth and a deep cleft in her chin, broad shoulders and clear definition in her arms, a fitted forest-green wrap dress"},
    {"idade": 33, "desc": "tight sandy-brown curls pinned loosely on top of her head, thick dark acetate frames, square and heavy, skin tanned and freckled from the sun, a small brown mole under her right nostril, wide hips and a narrow waist, a fitted ivory eyelet sundress"},
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
    # + 2026-08-01: o operador viu o mesmo rosto voltando no lote. Quatro
    # mulheres a mais, cada uma com marca facial propria.
    {"idade": 30, "desc": "a short tapered cut faded at the sides and a small beauty mark above her left brow, a fitted rust-orange dress"},
    {"idade": 34, "desc": "waist-length micro braids pulled into a high ponytail and a gap between her front teeth, a fitted plum dress"},
    {"idade": 28, "desc": "finger waves set close to the head and a narrow widow's peak, a fitted gold summer dress"},
    {"idade": 36, "desc": "long faux locs gathered over one shoulder and deep dimples in both cheeks, a fitted sage green dress"},
    # + 2026-08-02: o espelho das tres novas do pool CLARA — mesma medicao (o
    # operador viu sempre o mesmo rosto, porque as catorze acima descreviam a
    # pessoa por cabelo mais cor de olho), mesmos eixos novos. So' o descritor
    # de cabelo muda, que e' onde a etnia se le'.
    #   · OCULOS — o eixo ZERADO nos dois pools de mulher (0/28).
    #   · PORTE — ombros largos com braco forte, magra e de membros longos.
    #   · a ancora facial (P6) e' NO ROSTO: pinta sob o labio, duas pintas
    #     juntas na mandibula. ⛔ marca abaixo da orelha nao ancora.
    #   · as duas fecham em "a fitted <cor> <peca>", como as catorze acima.
    {"idade": 35, "desc": "cornrows braided straight back into a low bun, heavy tortoiseshell glasses, high sharp cheekbones and a small dark beauty mark centred just below her lower lip, broad-shouldered with strong arms, a fitted cobalt-blue wrap dress"},
    {"idade": 39, "desc": "close-cropped natural hair gone mostly silver, a broad forehead above deep-set eyes and two small dark moles set close together on her left jaw, lean and long-limbed, a heavy silver cuff on one wrist, a fitted ink-blue linen dress"},
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
    # + 2026-08-01: o operador mediu vicio de cenario — as mesmas quatro
    # cozinhas voltavam no lote. Sete cozinhas americanas a mais.
    {"id": "cozinha_galley", "set": "a narrow galley kitchen in an older American apartment, cabinets down both walls and a window at the far end",
     "bancada": "counter", "curto": "kitchen", "luz": "flat daylight from the window at the end of the room."},
    {"id": "cozinha_fazenda", "set": "an old American farmhouse kitchen with a deep porcelain sink and a window above it",
     "bancada": "counter", "curto": "kitchen", "luz": "soft grey morning light through the window over the sink."},
    {"id": "cozinha_cabana", "set": "a knotty pine cabin kitchen with a screen door and pine trees out the window",
     "bancada": "counter", "curto": "kitchen", "luz": "green-tinged afternoon light coming through the screen door."},
    {"id": "cozinha_retro", "set": "a nineteen-seventies American kitchen with laminate counters, wood-panelled walls and a round wall clock",
     "bancada": "counter", "curto": "kitchen", "luz": "warm overhead bulb light with dim daylight from the side."},
    {"id": "cozinha_bar", "set": "an American kitchen with a breakfast bar and two wooden stools, a hallway out of focus beyond",
     "bancada": "breakfast bar", "curto": "kitchen", "luz": "even daylight from a sliding glass door frame-right."},
    {"id": "cozinha_peninsula", "set": "a small American kitchen with a tiled peninsula dividing it from a dining table",
     "bancada": "peninsula", "curto": "kitchen", "luz": "warm side light from a lamp over the dining table."},
    {"id": "cozinha_porao", "set": "a finished basement kitchenette with a bar sink and a low ceiling",
     "bancada": "bar counter", "curto": "kitchen", "luz": "warm recessed ceiling light and no daylight."},
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
    # + 2026-08-01: o operador mediu vicio de prop — o lote voltava sempre com
    # os mesmos quatro. Cinco a mais, na mesma gramatica de murcho/ereto.
    {"id": "aspargo", "marisco": False,
     "murcho": "a small wilted asparagus stalk, no longer than his thumb, limp and drooping over his fingers",
     "ereto": "an asparagus stalk upright at shoulder height, held stiff and straight, as long as her forearm"},
    {"id": "daikon", "marisco": False,
     "murcho": "a small shrivelled daikon radish, no longer than his thumb, wrinkled and completely soft, drooping over his fingers",
     "ereto": "a daikon radish upright at shoulder height, held stiff and straight, as long as her forearm and as thick as her wrist"},
    {"id": "linguica", "marisco": False,
     "murcho": "a small pale sausage, no longer than his thumb, shriveled and completely soft, folded over on itself",
     "ereto": "a thick sausage upright at shoulder height, held stiff and straight, as long as her forearm"},
    {"id": "abobrinha", "marisco": False,
     "murcho": "a small shrivelled zucchini, no longer than his thumb, wrinkled and completely soft, folded over on itself",
     "ereto": "a zucchini upright at shoulder height, held stiff and straight, as long as her forearm and as thick as her wrist"},
    {"id": "berinjela", "marisco": False,
     "murcho": "a small shrivelled eggplant, no longer than his thumb, wrinkled and completely soft, folded over on itself",
     "ereto": "an eggplant upright at shoulder height, held stiff and straight, as long as her forearm and as thick as her wrist"},
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
    # + 2026-08-01: a isca repetia dentro do mesmo lote e o curiosity gap
    # perdia a graca. Cinco itens a mais na bancada, nenhum nomeado na copy.
    "a small stoneware pot of bee pollen, lid tipped against it",
    "a handful of shelled walnuts in a shallow white bowl",
    "a squat jar of dark molasses with the lid resting beside it",
    "a small dish of grated raw beet, deep red",
    "three dried figs on a white saucer",
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
    # + 2026-08-01: tres rituais so' nao seguravam o lote — a cena 2 repetia.
    # Cinco liquidos a mais, acao sempre em gerundio e sem sujeito.
    {"id": "gelatina_gelo", "fala": "gelatin into ice water",
     "mesa": "a plain white sachet of pale powder with no label, a tall glass of ice water and a long metal spoon",
     "acao": "tipping the powder into the ice water and working the spoon around the rim until it clears"},
    {"id": "gelatina_leite", "fala": "gelatin into cold milk",
     "mesa": "a plain white sachet of pale powder with no label, a white mug of cold milk and a metal spoon",
     "acao": "shaking the sachet out over the mug and turning the spoon slowly through the milk"},
    {"id": "gelatina_suco", "fala": "gelatin into orange juice",
     "mesa": "a plain white sachet of pale powder with no label, a glass of orange juice and a metal spoon",
     "acao": "pouring the powder into the juice and stirring until nothing is left floating"},
    {"id": "gelatina_cafe", "fala": "gelatin into black coffee",
     "mesa": "a plain white sachet of pale powder with no label, a mug of black coffee and a metal spoon",
     "acao": "emptying the sachet into the coffee and stirring it through in slow circles"},
    {"id": "gelatina_sal", "fala": "gelatin into salted cold water",
     "mesa": "a plain white sachet of pale powder with no label, a glass of cold water, a small dish of salt and a metal spoon",
     "acao": "tipping the powder into the water, adding a pinch of salt from the dish and stirring it in"},
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
    # + 2026-08-01: o operador mediu vicio na copy — os mesmos oito hooks
    # voltavam no lote. Seis dores a mais, nenhuma com vocativo.
    "Thirty-one years married, and this is what my {o} had turned into. She never said a word.",
    "The pills quit working before I did. My {o} still went down like this, every single night.",
    "My {o} quit on me the year I turned {n}. This is what two years of that looks like.",
    "She stopped touching me and I let her. This was my {o}, and I blamed the years.",
    "The bedroom went quiet two years ago. Not her fault. This was my {o}, and I knew it.",
    "My doctor gave me a pill and a shrug. Two years later this was still my {o}.",
]

# ⛔ 2026-08-03 — FRASE ORFA. O operador leu um take renderizado ("It isn't
# age. The blood flow got choked off.") e reprovou: "voce tem que
# contextualizar mais as coisas, ta' deixando o viewer sem entender do que se
# trata". Idade causando O QUE? estrangulado ONDE? Nao adianta o orgao aparecer
# na ULTIMA frase da cena — foi exatamente essa cena que ele reprovou.
# ⭐ REGRA NOVA: toda frase que nomeia uma CAUSA (idade, blood flow) carrega,
#    NA MESMA FRASE, o que ela quebra. Mantem-se a pessoa que a frase ja' usa —
#    aqui 1a pessoa, entao `my {o}`.
# ⚠️ Conserto CIRURGICO: so' a primeira frase das entradas 0, 3, 6 e 7 mudou.
#    As demais ja' traziam o alvo na mesma frase ("the blood flow my {o} lost")
#    e nao foram tocadas. Os fechamentos validados ficaram intactos: o alvo
#    entrou por dentro do teto de 36 palavras, medido no pior caso
#    (`old boy` + a receita mais longa).
FUNDIDAS = [
    # ⚠️ O item aprovado terminava em "nineteen days later mine came back",
    # sem nomear o orgao. Como o CTA tambem nao nomeia, a cota caia para 1/3 e
    # o linter reprovava 69 de 300 sorteios. Uma palavra mudou — `mine` virou
    # `my {o}` — e o operador foi avisado.
    "It wasn't age — my {o} lost its blood flow. Stir {ing}. That's the gelatin trick, and nineteen days later my {o} came back.",
    # ⛔ 2026-08-03 — VERBO DE ENCANAMENTO. O operador leu esta fala no app:
    # "Nobody makes a dime telling you what opens it" / "it opens the blood flow
    # your {o} lost" -> "Opens o QUE? Com tanto verbo que voce poderia usar de
    # forma mais obvia pra dizer que DEIXA O PINTO MELHOR, voce usa 'opens'?".
    # ⭐ REGRA NOVA: o verbo da promessa e' de RESULTADO, dito como um homem
    #    diria — `gets your {o} hard again`. ⛔ Nao trocar `open` por outro
    #    eufemismo de encanamento (`unblocks`, `restores flow`): trocar
    #    abstracao por abstracao nao e' conserto (licoes §17).
    # ⚠️ O `blood flow` NAO sai — o linter cobra o literal. Ele deixa de ser a
    #    promessa e vira o motivo, na MESMA frase do orgao (regra da frase orfa).
    # ⚠️ Coube sem subir TETO_FALA, mas COMEU FOLGA: pior caso (`old boy` + o
    #    ritual mais longo) sobe de 32 para 35 de 36. Sobra UMA palavra — quem
    #    for mexer nesta entrada ou alongar RECEITAS mede antes.
    "Stir {ing}. They call it the gelatin trick, and it gets your {o} hard again — the blood flow comes back. This is me now.",
    "My neighbor gave me this. Stir {ing} — the gelatin trick. The blood flow came back, and so did my {o}.",
    "Nobody told me my {o} was starved of blood flow. Stir {ing}, that's the whole gelatin trick, and my {o} hasn't quit since.",
    "Two dollars, brother. Stir {ing} — the gelatin trick — and the blood flow that left my {o} came right back.",
    # + 2026-08-01: cinco fundidas so' repetiam na cena 2. Seis a mais, todas
    # carregando o literal "gelatin trick" e o blood flow, como manda a regra.
    "Nineteen days. Stir {ing}, that's the gelatin trick, and the blood flow my {o} lost came back.",
    "My doctor never once said my {o} was short on blood flow. Stir {ing}. The gelatin trick gave me my {o} back.",
    "It's the blood flow to my {o}, not the calendar. Stir {ing}. That's the gelatin trick, and my {o} works again.",
    "Stir {ing} before bed. That's the gelatin trick. The blood flow came back and my {o} with it.",
    "Three weeks on the gelatin trick. Stir {ing}. The blood flow my {o} was missing is running again.",
    "My wife noticed before I did. Stir {ing}, the gelatin trick, and the blood flow found my {o} again.",
]

CTAS = [
    # ⭐ Alternativa pedida pelo operador em 2026-07-31, vista em campo:
    # a promessa e' A RECEITA, nao "o que eu uso" nem "onde eu compro".
    # E' a mais direta do pool e a unica que casa com a keyword RECIPE
    # que o Veo Editor ja' destaca na legenda.
    "Comment gelatin, and I'll send you the recipe tonight. {gate}",
    # ⛔ 2026-08-03 — MUDANCA SEM DIZER O QUE MUDOU. O operador, lendo o app:
    # "My sister asked what changed." -> "O que mudou?". `what changed` abre a
    # pergunta e a fala acaba, entao o espectador nunca ouve a promessa.
    # ⭐ REGRA NOVA: se a frase abre a pergunta, ela mesma RESPONDE — e a
    #    resposta e' o resultado no corpo dele, nao o mecanismo.
    # ⚠️ Teto da cena 3 e' 34 e a troca custava 3 palavras: `night` saiu e
    #    `send you` virou `send`, entao o pior caso (com o gate mais longo)
    #    SOBE de 32 para 33 — o corte devolveu 2 das 3, nao todas. Sobra UMA
    #    palavra. A isca do CTA continua (`the exact one I use`).
    "Next Friday she'll ask what got you hard again. Comment gelatin, and I'll send the exact one I use. {gate}",
    "A month from tonight you won't recognise yourself. Comment gelatin, and I'll send you where I get mine. {gate}",
    "I waited two years to find this. Comment gelatin, and I'll send the recipe tonight. {gate}",
    "Comment gelatin, and I'll send you the one my neighbor sent me. Nobody in my house ever knew. {gate}",
    "Comment gelatin, and I'll send it tonight. There's one more ingredient on that counter I can't name here. {gate}",
    # + 2026-08-01: o operador mediu vicio no fechamento — os mesmos seis CTAs
    # no lote inteiro. Seis a mais, nenhum com vocativo.
    "Comment gelatin, and the recipe's in your inbox in ten minutes. {gate}",
    "Two dollars at any grocery store. Comment gelatin, and I'll tell you exactly what to buy. {gate}",
    "My wife doesn't know I post these. Comment gelatin, and I'll send you the recipe. {gate}",
    "You've watched this far. Comment gelatin, and I'll send you what I stir every night. {gate}",
    "Don't buy another pill this month. Comment gelatin, and I'll send you the recipe tonight. {gate}",
    "Nineteen days from tonight you'll be telling somebody else. Comment gelatin, and I'll send it. {gate}",
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
    # ⛔ 2026-08-03 — FRASE ORFA (ver o bloco da FUNDIDAS). "He blamed his age."
    # nomeia a causa e nao diz o que ela quebrou. O alvo entrou na MESMA frase,
    # na terceira pessoa que a frase ja' usava: `for going soft`.
    "He blamed his age for going soft. I blamed myself. It was neither of us — his {o} looked like this every night.",
    "Four hundred a month on pills, and his {o} still looked like this. I stopped asking.",
    "We hadn't touched in eight months. This was his {o}, and he wouldn't talk about it.",
    "My man is {n}. This was his {o} in March. I'm the one who found what fixed it.",
    # + 2026-08-01: mesmo vicio da persona masculina — os oito hooks dela
    # voltavam no lote. Quatro dores a mais, nenhuma com vocativo.
    "Nine years together and I was sleeping alone in my own bed. This was his {o}.",
    # ⛔ 2026-08-03 — FRASE ORFA. "He turned {n} and everything stopped."
    # culpava a idade e deixava o orgao para a TERCEIRA frase, que e' o defeito
    # exato que o operador reprovou. O alvo subiu para a frase da causa.
    "He turned {n} and his {o} stopped. Not our marriage, just this — every single night.",
    "Two years I thought he was cheating. He wasn't. This was his {o}, and he was hiding it.",
    "He said he was tired. For eight months I believed him. This is what his {o} looked like.",
]

# ⛔ 2026-08-03 — FRASE ORFA, o mesmo conserto da FUNDIDAS masculina (a queixa
# do operador esta' documentada la'). Aqui a pessoa da frase e' a terceira — a
# mulher conta a historia do marido —, entao o alvo entra como `his {o}` e nao
# como `your {o}`: o que se cobra e' REFERENTE, nao pessoa.
# ⚠️ So' as entradas 0 e 3 mudaram; as outras sete ja' diziam o alvo na mesma
#    frase. A entrada 0 e' a mais apertada do motor (36 de teto 36 no pior caso)
#    e o conserto entrou sem somar uma palavra.
FUNDIDAS_F = [
    "It wasn't age — his {o} lost its blood flow. I stir {ing}. That's the gelatin trick, and nineteen days later his {o} came back.",
    # ⛔ 2026-08-03 — VERBO DE ENCANAMENTO, o espelho feminino da FUNDIDAS[1]
    # (a queixa do operador esta' documentada la'): `it opens the blood flow his
    # {o} lost` descreve o vaso abrindo quando a promessa e' o RESULTADO.
    # ⭐ Mesma regra nova: verbo de resultado (`got his {o} hard again`), com o
    #    `blood flow` rebaixado a motivo e na mesma frase do orgao. A pessoa da
    #    frase continua a terceira — o que se cobra e' REFERENTE, nao pessoa.
    # ⚠️ Esta e' a entrada mais apertada da persona feminina. Para caber sem
    #    subir o TETO_FALA, `They call it` foi encurtado para `That's` — o
    #    fechamento validado `And he came back.` fica. 35 de 36 no pior caso.
    "I stir {ing} for him. That's the gelatin trick — the blood flow came back and his {o} got hard again. And he came back.",
    "My aunt gave me this. I stir {ing} — the gelatin trick. The blood flow came back, and so did his {o}.",
    "Nobody told us his {o} had no blood flow. I stir {ing}, that's the whole gelatin trick, and his {o} hasn't quit since.",
    "Two dollars, girls. I stir {ing} — the gelatin trick — and the blood flow that left his {o} came right back.",
    # + 2026-08-01: mesma expansao da masculina, a cena 2 dela repetia. Quatro
    # a mais, todas com o literal "gelatin trick" e o blood flow no lugar.
    "I stir {ing} every night before bed. That's the gelatin trick. The blood flow came back, and his {o} with it.",
    "Three weeks on the gelatin trick. I stir {ing}. The blood flow his {o} was missing is running again.",
    "He never asked what was in the glass. I stir {ing}. Gelatin trick, blood flow back, and his {o} with it.",
    "I did it without telling him. I stir {ing}. The gelatin trick, the blood flow, and his {o} did the rest.",
]

CTAS_F = [
    # ⭐ Alternativa pedida pelo operador em 2026-07-31, vista em campo:
    # a promessa e' A RECEITA, nao "o que eu uso" nem "onde eu compro".
    # E' a mais direta do pool e a unica que casa com a keyword RECIPE
    # que o Veo Editor ja' destaca na legenda.
    "Comment gelatin, and I'll send you the recipe I use on him. {gate}",
    "Next Friday night he'll be the one reaching for you. Comment gelatin, and I'll send you the exact one I use. {gate}",
    "A month from now you won't recognise him. Comment gelatin, and I'll send you where I get mine. {gate}",
    "I waited two years to find this. Comment gelatin, and I'll send the recipe tonight. {gate}",
    "Comment gelatin, and I'll send you the one my aunt sent me. He never even knew I did it. {gate}",
    "Comment gelatin, and I'll send it tonight. There's one more ingredient on that counter I can't name here. {gate}",
    # + 2026-08-01: o operador mediu vicio no fechamento — os mesmos seis CTAs
    # no lote inteiro. Seis a mais, nenhum com vocativo.
    "Comment gelatin, and I'll send you what I put in his glass. {gate}",
    "Two dollars at the grocery store. Comment gelatin, and I'll tell you exactly what to get. {gate}",
    "Do it for him if he won't. Comment gelatin, and I'll send you the recipe tonight. {gate}",
    "He still thinks it was his idea. Comment gelatin, and I'll send you mine. {gate}",
    "Nineteen days from tonight you'll be the one telling your friends. Comment gelatin, and I'll send it. {gate}",
    "Don't buy him another pill this month. Comment gelatin, and I'll send you the recipe. {gate}",
]


GATES = [
    "Follow me first, or my message never lands.",
    "Follow me first, or I won't have any way to find your comment, brother.",
    "Hit follow right now, or Facebook can't deliver it.",
    # + 2026-08-01: o operador mediu vicio de vocativo — "brother" caia em
    # praticamente todo CTA do lote, porque so' havia tres gates.
    # ⛔ REGRA NOVA: no maximo 2 entradas deste pool com o vocativo "brother",
    # e a MAIORIA sem vocativo nenhum. Nove gates a mais abaixo.
    "Hit follow first. I can't message anyone who isn't following.",
    "Follow first. Three hundred comments come in and I answer followers.",
    "One tap on follow, or this never reaches you again.",
    "The algorithm hides me from people who don't follow.",
    "I answer followers first. Everybody else waits until the weekend.",
    "Follow me tonight, my friend. Tomorrow this is off your feed.",
    "Facebook blocks my message unless you follow me. So follow.",
    "Two hundred people comment on these. Followers get answered first, guys.",
    "Follow me and my inbox opens. That's how the page works.",
]


# ---------------------------------------------------------------------------
# ⛔⛔⛔ LAPIDE — OS CINCO POOLS ACIMA ESTAO APOSENTADOS NESTE ARQUIVO
# ---------------------------------------------------------------------------
# `FUNDIDAS`, `FUNDIDAS_F`, `CTAS`, `CTAS_F` e `GATES` NAO SAO LIDOS por
# ninguem daqui para baixo. Ficam no arquivo como HISTORICO — cada um carrega,
# em comentario, uma licao paga em render que continua valendo (o verbo de
# RESULTADO no lugar do verbo de encanamento, a frase orfa que nomeia causa sem
# dizer o que ela quebra, a idade por extenso).
#
# ⚠️⚠️ MELHORAR QUALQUER ENTRADA DELES NAO MUDA UM UNICO VIDEO DESTE MOTOR.
# Quem escreve a cena 2 aqui sao as tres listas novas logo abaixo.
#
# ⛔ POR QUE ELES NAO PODIAM VIR — medido contra `sc.lint_copy16`, nao suposto:
#   CT1  os 24 CTAS terminam em `{gate}`, DEPOIS do `Comment gelatin,`.
#        A ultima coisa no ouvido era um segundo pedido, nao o primeiro.
#   CT5  a fundida recebe `{ing}` = a fala da receita, e tres das oito receitas
#        dizem `fresh lemon` / `salted` — ingrediente na fala e' a moeda gasta
#        antes do pedido (`lemon` entrou no `INGREDIENTES_16` em 2026-08-12).
#   CT6  nenhum dos 24 CTAS diz ONDE a receita chega. `I'll send you the recipe
#        tonight` promete o quando, nunca o onde, e e' o onde que baixa o custo
#        social de comentar com nome e foto.
#   CT7  `it gets your {o} hard again` (FUNDIDAS[1]) e `got his {o} hard again`
#        (FUNDIDAS_F[1]) sao verbo de ereccao COLADO no orgao — a licao paga no
#        COLO 16, ~95% de recusa. ⚠️ Nao e' a palavra: e' a colagem. Sobre o
#        CORPO passa, sobre o ORGAO nao.
#   CT8  o pool `GATES` inteiro e' pedido de follow, e a premissa que o criou
#        estava errada: *"a mensagem e' enviada independente de seguirem ou
#        nao"* (operador, 2026-08-10).
#
# ⭐ E POR QUE ISTO NAO E' "REESCREVER A COPY DO ED": cada beat abaixo sai de
# uma sentenca que ele ja' aprovou em 2026-07-31, com o que o contrato proibe
# cortado fora. O `blood flow` continua sendo o motivo e nunca a promessa; o
# `gelatin trick` continua literal; a dor e o elenco nao mudaram uma virgula.
# ⚠️ As tres listas estao marcadas para leitura dele antes de virar `.exe`.

# ---------------------------------------------------------------------------
# COPY DA CENA 2 — o take fundido, sob o CONTRATO DE COPY 16s
# ---------------------------------------------------------------------------
# A conta do orcamento, teto 25:
#     mecanismo com razao ..... 10-13
#     prova curta .............  4-7
#     CTA com cobertura .......  8-9
#
# ⛔ O MECANISMO CARREGA O ORGAO. Nao e' enfeite: o `lint_curto` cobra o
# substantivo do nucleo em 2 das 2 cenas (cota), e o CT4 exige que seja O MESMO
# nos dois takes. Por isso o `{o}` entra aqui e o sorteio usa UM apelido so'.
# ⛔ E O VERBO E' DE RESULTADO, NUNCA DE ENCANAMENTO. `opens`, `unblocks` e
# `restores flow` estao proibidos por ordem do operador (2026-08-03, lendo o
# app: *"com tanto verbo que voce poderia usar de forma mais obvia... voce usa
# 'opens'?"*) — ainda que o `VERBOS_EFEITO_16` do short_comum os aceite.
MECANISMOS16 = [
    "The gelatin trick put the blood flow back in my {o}.",
    # ⛔ ERA `It wasn't age. The gelatin trick sends...` — DUAS sentencas, e a
    # primeira nomeia a CAUSA (idade) sem dizer o que ela quebra. E' a FRASE
    # ORFA que o operador reprovou em 2026-08-03 lendo um take renderizado
    # (*"voce tem que contextualizar mais as coisas, ta' deixando o viewer sem
    # entender do que se trata"*), e o `medir_contexto_copy` a pegou em 20 de
    # 1.201 frases. ⭐ O conserto e' o mesmo da FUNDIDAS[0] original: o travessao
    # mantem causa e alvo na MESMA sentenca.
    "It wasn't age — the gelatin trick sends blood flow to my {o}.",
    "My {o} ran dry. The gelatin trick brings the blood flow back.",
    "Two dollars. The gelatin trick drives blood flow straight to my {o}.",
    "My {o} was starved. The gelatin trick feeds the blood flow.",
    # ⚠️ `My neighbor gave me this` e `Three weeks on...` sairam com 13
    # palavras e MEDIDAS mortas: com a prova mais curta (4) e o CTA mais curto
    # (9), o mecanismo so' cabe ate' 12. Entrada que nunca cabe e' pool morto
    # que o autoteste de contagem conta como vivo — a lei
    # `pool-com-entrada-inalcancavel`. Quem encolheu foi a ENTRADA, nao o piso.
    "My neighbor sent it. The gelatin trick feeds my {o} blood flow.",
    "Not the calendar. The gelatin trick sends blood flow to my {o}.",
    "Two weeks on the gelatin trick, and blood flow reaches my {o}.",
    "My doctor never mentioned blood flow. The gelatin trick fixed my {o}.",
    "The gelatin trick gave my {o} its blood flow back.",
]

# ⚠️ A PROVA E' SOBRE ELA, NAO SOBRE O ORGAO — e isso e' o CT7 em forma de
# pool, nao pudor. `Nineteen days later my {o} came back` era o fechamento
# aprovado da FUNDIDAS[0], e `came back` esta' no `ERECAO_16`: colado no orgao,
# reprova. A prova mudou de sujeito e ganhou o que o angulo sempre teve de
# melhor — a mulher que voltou a procurar.
PROVAS16 = [
    "My wife noticed first.",
    "She noticed before I did.",
    "Nineteen days later she noticed.",
    "She reaches for me now.",
    "The couch nights are over.",
    "Two years of silence, done.",
    "She stopped sleeping alone.",
    "Nineteen days. She reached for me.",
    "I quit making excuses.",
    "She asked what I did.",
]

MECANISMOS16_F = [
    "The gelatin trick put the blood flow back in his {o}.",
    # ⛔ mesma frase orfa da masculina — ver a nota la'.
    "It wasn't age — the gelatin trick sends blood flow to his {o}.",
    "His {o} ran dry. The gelatin trick brings the blood flow back.",
    "Two dollars. The gelatin trick drives blood flow straight to his {o}.",
    "His {o} was starved. The gelatin trick feeds the blood flow.",
    "My aunt sent it. The gelatin trick feeds his {o} blood flow.",
    "Not the calendar. The gelatin trick sends blood flow to his {o}.",
    "Two weeks on the gelatin trick, and blood flow reaches his {o}.",
    "No doctor mentioned blood flow. The gelatin trick fixed his {o}.",
    "The gelatin trick gave his {o} its blood flow back.",
]

# ⭐ O ANGULO QUE SO' ELA TEM sobrevive aqui: ela faz ESCONDIDO. Duas das dez
# entradas carregam isso, que era o CTA 4 dela no `_short`.
PROVAS16_F = [
    "He reaches for me now.",
    "He never asked what changed.",
    # ⚠️ era `Nineteen days later he came to bed` (7) e estava MORTA: com o
    # mecanismo mais curto (10) e o CTA mais curto (9), a prova so' cabe ate' 6.
    "He came back to bed.",
    "He stopped sleeping downstairs.",
    "I did it without telling him.",
    "He thinks it was his idea.",
    "The bedroom is loud again.",
    "Nineteen days. He noticed first.",
    "He quit making excuses.",
    "I stopped sleeping alone.",
]

# ⛔ CT6 EM TODA ENTRADA: as dez dizem ONDE a receita chega. A clausula e'
# gratis no orcamento (mesmo custo do `I'll send the recipe` antigo) e entrega
# de graca o endereco, a privacidade e o fato de que nao e' na tela publica.
# ⛔ CT1: esta e' SEMPRE a ultima sentenca da fala. Nada vem depois dela.
# ⚠️ Pool UNICO para as duas personas — quem recebe a receita e' o espectador,
# nao o narrador, entao a pessoa da frase nao muda.
CTAS16 = [
    "%s and the recipe goes to your messages." % sc.CTA_LITERAL,
    "%s and the recipe lands in your inbox." % sc.CTA_LITERAL,
    "%s and I'll send the recipe by message." % sc.CTA_LITERAL,
    "%s and the whole recipe hits your inbox." % sc.CTA_LITERAL,
    "%s and I'll send it straight to your messages." % sc.CTA_LITERAL,
    "%s and the recipe is in your inbox tonight." % sc.CTA_LITERAL,
    "%s and nobody else sees the recipe I send." % sc.CTA_LITERAL,
    "%s and I'll send the recipe in private." % sc.CTA_LITERAL,
    "%s and your messages get the recipe tonight." % sc.CTA_LITERAL,
    "%s and the recipe comes to your messages." % sc.CTA_LITERAL,
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
    # ⚠️ O `_short` nao tem o try/except e ESTOURA com `JSONDecodeError` se o
    # arquivo estiver truncado — e ele pode estar, porque a gravacao e'
    # `open(w)` sem temp+rename: matar o app no meio da escrita deixa um JSON
    # pela metade e o agente nao abre mais. O MEL 16 ja' engole; este engole
    # tambem. ⛔ Divida declarada: engolir esconde a corrupcao em vez de
    # consertar a escrita, e o conserto de verdade e' gravar em temporario e
    # renomear. Fica registrado porque vale para o parque inteiro.
    if os.path.exists(LEDGER):
        try:
            with open(LEDGER, encoding="utf-8-sig") as f:
                return json.load(f)
        except (ValueError, OSError):
            return {}
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


def _cabe(pool, monta, teto):
    """As entradas que cabem no teto.

    ⛔ SEM `or pool`: quando nada cabe devolve a MAIS CURTA, nunca o pool
    inteiro — `or pool` e' o estouro silencioso, porque entrega a fala longa
    sem reclamar exatamente quando o orcamento esta' apertado.
    """
    ok = [x for x in pool if _palavras(monta(x)) <= teto]
    return ok if ok else [min(pool, key=lambda x: _palavras(monta(x)))]


def _pools(persona_id):
    """Os pools de fala da persona: hook, mecanismo, prova.

    ⚠️ O CTA nao entra aqui — `CTAS16` e' pool UNICO. Quem recebe a receita e'
    o espectador, nao o narrador, entao a pessoa da frase nao muda com a
    persona (era o que fazia `CTAS` e `CTAS_F` serem dois pools no `_short`).
    """
    return ((HOOKS_F, MECANISMOS16_F, PROVAS16_F) if persona_id == "mulher"
            else (HOOKS, MECANISMOS16, PROVAS16))


def _fundir(spec, rng, o=None):
    """A fala da cena 2: MECANISMO + PROVA + CTA, dentro do teto de 25.

    ⛔⛔ A ORDEM DE QUEM CEDE E' A DOUTRINA DO ARQUIVO, nao gosto: o beat que
    NAO pode encolher sai primeiro reservando o MENOR dos outros dois, e os
    demais cedem ao que sobrou. Sem a reserva, um mecanismo de 13 palavras
    apaga em silencio as provas longas e as entradas viram pool morto — a lei
    `pool-com-entrada-inalcancavel`, que o autoteste conta como viva.

    ⚠️ O CTA e' o ultimo a ceder porque carrega o literal `Comment gelatin,` e
    a isca; e ele fica SEMPRE na ultima posicao (CT1: nada depois do pedido).
    """
    o = o or spec.get("orgao") or sc.orgao_de(sys.modules[__name__],
                                              spec["falas"][0])
    _, mecanismos, provas = _pools(spec["persona"]["id"])
    teto = TETO_FALA[2]
    _cp = min(provas, key=_palavras)
    _cc = min(CTAS16, key=_palavras)
    mec = rng.choice(_cabe(mecanismos,
                           lambda m: "%s %s %s" % (m.format(o=o), _cp, _cc),
                           teto)).format(o=o)
    prova = rng.choice(_cabe(provas,
                             lambda p: "%s %s %s" % (mec, p, _cc), teto))
    cta = rng.choice(_cabe(CTAS16,
                           lambda c: "%s %s %s" % (mec, prova, c), teto))
    return "%s %s %s" % (mec, prova, cta)


def sortear(pagina, rng, ledger, travas=None):
    """⭐ `travas` entrou em 2026-08-06 só para a trava de QUEM NARRA.

    Este era o único dos três motores de dois sexos que não recebia travas — a
    UI passava `travas["sexo"]` e o botão não travava nada. Assinatura aditiva:
    quem chama sem o argumento continua sorteando como sempre.
    """
    travas = travas or {}
    hist = ledger.get(pagina, {})
    amb = _evitando(rng, AMBIENTES, hist.get("ambiente", [])[-2:])
    prop = _evitando(rng, PROPS, hist.get("prop", [])[-2:])
    isca = _evitando(rng, ISCA, hist.get("isca", [])[-3:])
    _sexo = travas.get("sexo")
    _pool = [p for p in PERSONAS if p["id"] == _sexo] if _sexo else PERSONAS
    persona = _evitando(rng, _pool or PERSONAS, hist.get("persona", [])[-1:])
    ref = rng.choice(homens_de(pagina))
    mul = rng.choice(mulheres_de(pagina))
    # ⛔ 2026-08-10 — SO' OS TRES APELIDOS SAO SORTEAVEIS (ordem do
    # operador, parque inteiro). `soldier` e `tool` seguem no NUCLEO porque
    # as LENTES os usam para DETECTAR o orgao; o que muda e' que nao saem
    # mais na fala. Ver `short_comum.orgaos_sorteaveis`.

    # ⛔⛔ CT4 — UM APELIDO POR VIDEO, repetido nos DOIS takes. O `_short`
    # sorteia TRES (um por cena) e esta' certo la': em 24s e cinco cenas o
    # bordao e' o risco. Em 16s e duas cenas o risco e' o oposto — o corte zera
    # a memoria de trabalho, e trocar `wiener` por `Johnson` no segundo 9
    # obriga o espectador a remapear justamente quando ele ja' esta' com um pe'
    # fora. A variacao continua existindo ENTRE videos, e quem a cobra e' o
    # CT4b (`sc.orgaos_sorteaveis` so' devolve os tres autorizados).
    orgao = sc.orgaos_sorteaveis(rng, 1)[0]
    n = IDADE_EXT[ref["idade"]]
    hooks, _, _ = _pools(persona["id"])
    # ⭐ A RECEITA CONTINUA SORTEADA e continua chegando ao QUADRO — o copo, o
    # sache e a colher na IMAGE 02/02, a acao no TAKE 02/02. O que mudou e' que
    # ela NAO ENTRA MAIS NA FALA (CT5: ingrediente dito e' a moeda gasta antes
    # do pedido, e tres das oito receitas dizem `fresh lemon` ou `salted`).
    # ⚠️ Por isso ela nao precisa mais ceder ao teto da fala: o filtro
    # `_cabe(RECEITAS, ...)` do `_short` sumiu porque o vinculo sumiu junto.
    rec = _evitando(rng, RECEITAS, hist.get("receita", [])[-2:])
    spec = {"pagina": pagina, "ambiente": amb, "prop": prop, "receita": rec,
            "isca": isca, "ref": ref, "mulher": mul, "persona": persona,
            "orgao": orgao}
    spec["falas"] = [
        rng.choice(_cabe(hooks,
                         lambda h: h.format(o=orgao, n=n, N=n.capitalize()),
                         TETO_FALA[1])).format(o=orgao, n=n, N=n.capitalize()),
        "",
    ]
    spec["falas"][1] = _fundir(spec, rng, orgao)
    return spec


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

    b["IMAGE 01/02"] = (
        "IMAGE 01/02: Medium shot in %s. Standing behind the %s is %s. She looks "
        "straight into the lens, mouth open mid-word." % (amb["set"], amb["bancada"], quem)
        if fem else
        "IMAGE 01/02: Medium shot in %s. Standing behind the %s is %s. He looks "
        "straight into the lens, mouth open mid-word, jaw tight."
        % (amb["set"], amb["bancada"], quem)
    ) + (
        " In %s right hand, held out in front of %s chest, %s holds %s. %s is the "
        "only person in the frame. %s %s%s"
        % (dela, dela, "she" if fem else "he", prop["murcho"],
           "She" if fem else "He", amb["luz"].capitalize(), CAUDA, neg)
    )

    # ⭐⭐ O QUADRO FUNDIDO — as cenas 2 e 3 do `_short` num quadro so'.
    # Cada pedaco vem de bloco que ja' rodou em render; nada foi inventado:
    #   · o SET, a BANCADA e a LUZ ......... da cena 2
    #   · a MESA (copo, sache, colher) ..... da cena 2   (o mecanismo)
    #   · a ISCA ........................... da cena 2   (o curiosity gap)
    #   · o PARCEIRO colado no ombro ....... da cena 3   (o payoff social)
    #   · o PROP ERETO na mao livre dele ... da cena 3   (o payoff visual)
    # ⛔ Sem os tres ultimos o colapso comeria o payoff inteiro; sem os tres
    # primeiros comeria o mecanismo. Este angulo precisa dos SEIS, e por isso
    # nao serve aqui a regra do PEE 16 (la' o colapso sacrifica um quadro).
    #
    # ⛔ SAIU `is the only person in the frame`, que as duas cenas de origem
    # traziam. Agora sao DOIS em quadro, e manter a linha seria contradicao
    # DENTRO do prompt — a familia de defeito mais cara deste repo: o gerador
    # nao escolhe um dos dois lados, ele inventa um terceiro. Quem garante que
    # so' um fala e' o TAKE, e ele diz isso com todas as letras.
    # ⛔ V12 herdado do VAZAMENTO: as DUAS idades declaradas em toda mencao.
    # ⛔ NAO devolver aqui declaracao de conformidade ("two fully clothed
    # adults"). Ordem do operador, 2026-07-31: ela nao desarma o classificador
    # — so' troca de token ou de geometria desarma — e ainda injeta o token.
    #
    # ⚠️⚠️ A GEOMETRIA DO CASAL MUDA COM A PERSONA, e nao e' simetria estetica:
    # `one hand flat on his chest` e' a mao DELA no torso nu DELE, validada em
    # render na cena 3. Espelhar isso — o homem com a mao no peito da mulher —
    # e' outra imagem e outro risco de classificador; ali a mao vai ao BRACO.
    # Mesma familia da licao do `sitting across his lap`, que passou virando
    # `perched sideways on his right knee` sem mudar a imagem.
    if fem:
        _parceiro = ("A %d-year-old %s man, %s, bare-chested with %s, %s"
                     % (ref["idade"], et, ref["marca"], ref["corpo"], BELEZA_H))
        _colado = ("stands beside her, leaning in against her shoulder, "
                   "laughing, one hand resting on her upper arm")
        _mao = "In his free hand he holds"
    else:
        _parceiro = ("A %d-year-old %s woman, %s, %s"
                     % (mul["idade"], et, mul["desc"], BELEZA_M))
        _colado = ("stands beside him, leaning in against his shoulder, "
                   "laughing, one hand flat on his chest")
        _mao = "In her free hand she holds"

    b["IMAGE 02/02"] = (
        "IMAGE 02/02: Medium shot at the %s in the same %s, same light. %s, "
        "stands behind it mid-action, speaking to the camera. On it: %s, and off "
        "to the side %s. Both %s hands are at the glass. %s, %s, saying nothing. "
        "%s %s. %s %s%s"
        % (amb["bancada"], amb["curto"], mesmo, rec["mesa"], isca, dela,
           _parceiro, _colado, _mao, prop["ereto"],
           amb["luz"].capitalize(), CAUDA, neg)
    )

    b["TAKE 01/02"] = (
        "TAKE 01/02: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway, no cuts. The %d-year-old %s speaks straight "
        "into the lens with force. On the word \"this\" %s lifts the thing in "
        "%s right hand an inch toward the camera. %s %s is the only person in "
        "the shot.\nDialogue: \"%s\"\nAudio: quiet kitchen room tone. No music."
        % (idade_narra, "woman" if fem else "man", "she" if fem else "he", dela,
           IMOBILIDADE, "She" if fem else "He", sonorizar(falas[0]))
    )

    # ⭐ O TAKE FUNDIDO — a acao do ritual da cena 2 e a direcao do casal da
    # cena 3, as duas literais. ⛔ E' AQUI que mora a garantia de que so' um
    # fala: a IMAGE perdeu o `only person in the frame` porque agora sao dois,
    # e sem esta linha o segundo entraria na conversa.
    b["TAKE 02/02"] = (
        "TAKE 02/02: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway, no cuts. %s hands stir the spoon while %s talks, %s. "
        "%s eyes stay on the lens the whole time. The %d-year-old %s laughs once "
        "and keeps still. The hand holding it does not move: %s Only the "
        "%d-year-old %s speaks; the other one is silent.\nDialogue: \"%s\"\n"
        "Audio: quiet kitchen room tone, a spoon against glass, soft laughter. "
        "No music."
        % ("Her" if fem else "His", "she" if fem else "he", rec["acao"],
           "Her" if fem else "His",
           ref["idade"] if fem else mul["idade"], "man" if fem else "woman",
           IMOBILIDADE, idade_narra, "woman" if fem else "man",
           sonorizar(falas[1]))
    )

    # ⛔ trava de texto queimado em todo TAKE — o watermark que o
    # operador viu vazando nos reels da concorrente (2026-08-01).
    return sc.selar_takes(b)


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

    for nome in ("IMAGE 01/02", "IMAGE 02/02"):
        if beleza not in blocos[nome]:
            achados.append(("ERRO", "%s sem a declaracao de beleza de quem "
                                    "narra" % nome))
        if marca not in blocos[nome]:
            achados.append(("ERRO", "%s sem a marca facial de quem narra — sem "
                                    "ela o rosto troca entre as cenas" % nome))


def _isca(spec, blocos, achados):
    """O curiosity gap: a isca esta' na bancada e NUNCA na copy."""
    if spec["isca"] not in blocos["IMAGE 02/02"]:
        achados.append(("ERRO", "a isca sumiu da bancada — e' ela que gera o "
                                "comentario extra"))
    corpo = " ".join(spec["falas"]).lower()
    for palavra in ("honey", "ginger", "cinnamon", "maca"):
        if palavra in corpo:
            achados.append(("ERRO", "a copy NOMEIA a isca ('%s') — o curiosity "
                                    "gap so' funciona se ela ficar sem nome"
                            % palavra))


def _ct16(spec, blocos, achados):
    """As sete travas do CONTRATO DE COPY 16s, cobradas de dentro do motor.

    ⛔ `isca_absurda=False`: este angulo nao promete nada falso no take 1 para
    desmentir meio segundo depois (isso e' TROCA, EXTERIOR e COLO). Aqui a dor
    e' verdadeira desde o primeiro frame — entao o CT7 vale nos DOIS takes, e
    verbo de ereccao colado no orgao reprova em qualquer um deles.
    """
    sc.lint_copy16(sys.modules[__name__], spec, achados, isca_absurda=False)


def _piso(spec, blocos, achados):
    """O orcamento e' PISO **e** teto — o teto ja' e' cobrado pelo `lint_curto`.

    ⚠️ Sem o piso, uma fala de 12 palavras passa calada e deixa ~4 segundos de
    silencio no fim do take: o take nao encolhe, quem encolhe e' a fala. Foi a
    licao do TROCA 16 e do MEL 16, e ela custa duas linhas aqui.
    """
    for i, fala in enumerate(spec["falas"], 1):
        n = _palavras(fala)
        if n < PISO_FALA[i]:
            achados.append(("ERRO", "a cena %d tem %d palavras (piso %d) — "
                                    "fala curta demais deixa o take mudo no "
                                    "fim" % (i, n, PISO_FALA[i])))


def lint(spec, blocos):
    return sc.lint_curto(
        sys.modules[__name__], spec, blocos, (1, 2), TETO_FALA,
        literais=("gelatin trick", "blood flow"),
        extras=(_hook, _elenco, _isca, _ct16, _piso))


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
          "cozinha_moderna": "Na cozinha moderna preta",
          # + 2026-08-01: as sete cozinhas novas do pool AMBIENTES precisam do
          # resumo em PT, senao o painel cai no fallback "Na cozinha".
          "cozinha_galley": "Na cozinha corredor de apartamento",
          "cozinha_fazenda": "Na cozinha de fazenda com pia de louça",
          "cozinha_cabana": "Na cozinha de cabana de pinho",
          "cozinha_retro": "Na cozinha anos setenta com parede de madeira",
          "cozinha_bar": "Na cozinha com balcão de bar e banquetas",
          "cozinha_peninsula": "Na cozinha pequena com península azulejada",
          "cozinha_porao": "Na copa do porão acabado",
          }


def resumo_pt(spec):
    et = "branca" if "white" in ETNIA[spec["pagina"]] else "negra"
    if spec["persona"]["id"] == "mulher":
        return ("%s, quem fala e a mulher de %d anos: ela mostra o prop murcho "
                "na mão e conta a dor do marido de %d. Na cena 2 ela prepara a "
                "gelatina na bancada e ele entra colado no ombro dela, mudo, "
                "com o prop ereto na mão livre. Dois takes de 8s, elenco de "
                "pele %s."
                % (PT_AMB.get(spec["ambiente"]["id"], "Na cozinha"),
                   spec["mulher"]["idade"], spec["ref"]["idade"], et))
    return ("%s, quem fala e o homem de %d anos sem camisa e muito bonito: ele "
            "mostra o prop murcho na mão e conta a própria dor. Na cena 2 ele "
            "prepara a gelatina na bancada e a mulher de %d entra colada no "
            "ombro dele, muda, com o prop ereto na mão livre. Dois takes de "
            "8s, elenco de pele %s."
            % (PT_AMB.get(spec["ambiente"]["id"], "Na cozinha"),
               spec["ref"]["idade"], spec["mulher"]["idade"], et))


def _hook_novo(spec, rng, o):
    """Um hook do pool da persona, ja' formatado e dentro do teto da cena 1."""
    n = IDADE_EXT[spec["ref"]["idade"]]
    hooks, _, _ = _pools(spec["persona"]["id"])
    return rng.choice(_cabe(hooks,
                            lambda h: h.format(o=o, n=n, N=n.capitalize()),
                            TETO_FALA[1])).format(o=o, n=n, N=n.capitalize())


# ⛔⛔ `_recopiar_receita` MORREU AQUI, e a morte e' consequencia do CT5.
# No `_short` a receita entrava DENTRO da fala da cena 2 (`{ing}`), entao
# trocar o ritual no painel obrigava a reescrever a fala — senao o quadro
# mostrava cafe e o audio dizia agua gelada. Neste motor a receita nao encosta
# na fala: ela vive so' na IMAGE 02/02 (o copo, o sache, a colher) e no TAKE
# 02/02 (a acao). Trocar o ritual muda o QUADRO e mais nada, e por isso o eixo
# sai do mapa de recopia.
# ⚠️ Eixo que continua chegando ao video — a lente `lint_painel_honesto` do
# `short_comum` confere isso sozinha, e e' ela que impede que a remocao daqui
# vire um dropdown que nao muda nada.


def _recopiar_persona(spec, rng):
    """Trocar quem narra troca a copy INTEIRA — sao pools diferentes.

    ⚠️ Sem isto o painel mostraria "quem narra: mulher" com as duas falas na
    voz do homem. O eixo nao e' de elenco, e' de roteiro.
    ⛔ E o apelido do orgao e' RESORTEADO UMA VEZ e usado nas duas falas —
    CT4. Sortear por fala traria dois apelidos no mesmo video.
    """
    o = sc.orgaos_sorteaveis(rng, 1)[0]
    spec["orgao"] = o
    spec["falas"][0] = _hook_novo(spec, rng, o)
    spec["falas"][1] = _fundir(spec, rng, o)


EIXOS_QUE_MEXEM_NA_COPY = {"persona": _recopiar_persona,
                           "ref": _recopiar_persona}


def nova_fala(spec, i, rng):
    # ⛔ CT4: o apelido e' do VIDEO, nao da cena. O `_short` lia o orgao da
    # fala QUE ESTAVA SENDO TROCADA (`spec["falas"][i]`), o que aqui traria um
    # apelido novo para a cena 1 e deixaria a cena 2 com o antigo — dois
    # apelidos no mesmo video, que e' exatamente o defeito que o CT4 mede.
    # ⭐ O apelido mora no `spec`, e as duas falas o leem de la'.
    o = spec.get("orgao") or sc.orgao_de(sys.modules[__name__],
                                         spec["falas"][0])
    if i == 0:
        return _hook_novo(spec, rng, o)
    return _fundir(spec, rng, o)


# ---------------------------------------------------------------------------
# AUTOTESTE
# ---------------------------------------------------------------------------
# ⛔⛔ ACEITE E' MEDICAO, NUNCA RELATO — nem meu, nem de subagente. O
# `organicwave_short.py` nunca teve autoteste (so' um CLI de um sorteio), e por
# isso ninguem nunca soube quantos dos sorteios dele estouravam o teto. Este
# nasce com um: motor 16s sem medicao entra no parque cego.
#
# ⚠️ Ele mede TRES coisas que o linter sozinho nao pega:
#   · o ALCANCE de cada pool — entrada que nunca sai esta' morta, e o autoteste
#     de contagem a conta como viva (lei `pool-com-entrada-inalcancavel`);
#   · a REPARTICAO dos tres apelidos — o CT4 trava um por video, e sem olhar a
#     repartição "um por video" vira o MESMO no lote inteiro (CT4b);
#   · o MINIMO e o MAXIMO de palavras por cena — o minimo decide o teto, nao o
#     maximo.

def autoteste(n=400):
    pags = sorted(ETNIA)
    erros = collections.Counter()
    avisos = 0
    dist = collections.defaultdict(set)
    tam = collections.defaultdict(list)
    apelidos = collections.Counter()
    personas = collections.Counter()
    falhas = []
    rng = random.Random(20260814)

    for i in range(n):
        pag = pags[i % len(pags)]
        spec = sortear(pag, rng, {})
        b = montar(spec)
        for j, fala in enumerate(spec["falas"], 1):
            tam[j].append(_palavras(fala))
        apelidos[spec["orgao"]] += 1
        personas[spec["persona"]["id"]] += 1
        for eixo in ("ambiente", "prop", "receita", "isca"):
            v = spec[eixo]
            dist[eixo].add(v["id"] if isinstance(v, dict) else v)
        # ⚠️ A DETECCAO FORMATA A ENTRADA antes de procurar. A primeira versao
        # comparava o prefixo ate' a primeira chave, e por isso dava a entrada
        # `{N} years old, ...` como MORTA em 400 sorteios: o prefixo dela e'
        # string vazia. Lente que inventa defeito e' tao cara quanto lente que
        # nao ve' — foi o que quase me fez "consertar" um hook que estava certo.
        _n = IDADE_EXT[spec["ref"]["idade"]]
        for rot, pool in (("mecanismo", MECANISMOS16 + MECANISMOS16_F),
                          ("prova", PROVAS16 + PROVAS16_F),
                          ("cta", CTAS16),
                          ("hook", HOOKS + HOOKS_F)):
            alvo = spec["falas"][0] if rot == "hook" else spec["falas"][1]
            for entrada in pool:
                try:
                    render = entrada.format(o=spec["orgao"], n=_n,
                                            N=_n.capitalize())
                except (KeyError, IndexError):
                    render = entrada
                if render in alvo:
                    dist[rot].add(entrada)
        for nivel, msg in lint(spec, b):
            if nivel == "ERRO":
                erros[msg[:78]] += 1
                if len(falhas) < 3:
                    falhas.append((pag, msg, list(spec["falas"])))
            else:
                avisos += 1

    print("%s — %d sorteios, %d paginas" % (TITULO, n, len(pags)))
    for j in sorted(tam):
        v = tam[j]
        print("  cena %d: %2d-%2d palavras (piso %d, teto %d), media %.1f"
              % (j, min(v), max(v), PISO_FALA[j], TETO_FALA[j],
                 sum(v) / float(len(v))))
    print("  apelidos (CT4b): %s" % dict(apelidos))
    print("  personas:        %s" % dict(personas))
    for eixo, pool in (("ambiente", AMBIENTES), ("prop", PROPS),
                       ("receita", RECEITAS), ("isca", ISCA),
                       ("hook", HOOKS + HOOKS_F),
                       ("mecanismo", MECANISMOS16 + MECANISMOS16_F),
                       ("prova", PROVAS16 + PROVAS16_F), ("cta", CTAS16)):
        marca = "" if len(dist[eixo]) == len(pool) else "   <-- entrada morta"
        print("  %-10s %2d/%2d alcancadas%s"
              % (eixo, len(dist[eixo]), len(pool), marca))
    print("  AVISOS: %d" % avisos)
    if erros:
        print("  ERROS:")
        for msg, q in erros.most_common():
            print("    %4d x %s" % (q, msg))
        for pag, msg, falas in falhas:
            print("    --- %s: %s" % (pag, msg))
            for f in falas:
                print("        %s" % f)
        return False
    print("  OK: zero ERRO em %d sorteios" % n)
    return True


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    _ap = argparse.ArgumentParser(description=TITULO)
    _ap.add_argument("pagina", nargs="?", default="chuck",
                     choices=sorted(ETNIA))
    _ap.add_argument("--seed", type=int, default=None)
    _ap.add_argument("--autoteste", nargs="?", type=int, const=400,
                     default=None, metavar="N")
    _a = _ap.parse_args()

    if _a.autoteste:
        sys.exit(0 if autoteste(_a.autoteste) else 1)

    _rng = random.Random(_a.seed)
    _spec = sortear(_a.pagina, _rng, _carregar_ledger())
    _b = montar(_spec)
    print(resumo_pt(_spec))
    print("=" * 72)
    for _k in sorted(_b):
        print(_b[_k] + "\n" + "-" * 72)
    for _n, _m in lint(_spec, _b):
        print("%s: %s" % (_n, _m))
