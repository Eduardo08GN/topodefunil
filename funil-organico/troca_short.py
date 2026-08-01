#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE TROCA SHORT — 3 cenas de 8 segundos (24s), SHORT NATIVO.

Doutrina: AGENTE_ED_TROCA_V1.md (regras TR1-TR21)
Fonte:    concorrentes/julie-evans-mapa-visual.md — leitura otica de 8 reels
          (7 da pagina Julie Evans, 1 da Sofia Maren), 142 frames, 2026-08-01.

⭐ O QUE DA' NOME AO AGENTE — A TROCA
------------------------------------
O proxy desce e o mecanismo sobe **no mesmo ponto do quadro, mesma mao, mesma
altura, sem corte**. O cerebro le SUBSTITUICAO ("isso nao funciona, ISTO
funciona") sem uma palavra. Invariante 8/8 da fonte, e o unico elemento do lote
que carrega o video inteiro e que nao existe no nosso repertorio: nos nossos
angulos o pivo mora numa CENA NOVA, com outro enquadramento e outro beat;
aqui ele custa zero segundos e zero renders.

⛔ POR QUE ESTE NAO DERIVA DE NINGUEM
------------------------------------
Os outros `<agente>_short.py` colapsam um motor longo de 5 cenas. Aqui nao ha'
motor longo: a fonte tem 12-14s de take unico e o angulo nasce em tres cenas.
Nao existe — e nao deve existir — um `troca_lucas.py`. Entao este arquivo e'
motor completo (pools proprios), mas continua usando a maquinaria compartilhada
(`short_comum.lint_curto`) passando a si mesmo como `base`, exatamente como o
`organicwave_short.py`.

AS QUATRO DECISOES DO OPERADOR (2026-08-01) — nao sao negociaveis
----------------------------------------------------------------
[D1] A CENA 3 E' A F12b ADAPTADA. O homem — o corpo-prova — segura o proxy na
     PROPRIA mao e ela aponta SEM ENCOSTAR. A F12b e' "a licao mais cara da
     operacao ate' hoje": quatro IMG 01 recusadas em sequencia,
     deterministicamente. O que bloqueia nao e' o prop, e' a AGENCIA — quem
     segura o objeto na virilha tem de ser o dono dela, e tem de estar ATIVO.
     ⚠️ Delta de registro em relacao ao FLAGRANTE: la' ele esta' sentado, cabeca
     baixa, prop minusculo e murcho — e' HUMILHACAO. Aqui ele esta' DE PE,
     neutro, com o prop GRANDE: nao e' vergonha, e' CONSTATACAO. Isso e'
     tambem o que separa do ELA_DIAGNOSTICA, onde o dedo CRAVA no abdomen dele
     e ele esta' deitado e passivo; aqui ela nao encosta (TR10).
     ⛔ `groin`/`pubic` custaram recusa (`level with his groin`) — a ancora e'
     de ROUPA e a string e' TRAVADA: `beside the lap of his khaki shorts`. So'
     a PECA varia; `lap` e' a coordenada e nao se troca por `pocket`, que joga
     o prop no quadril e amputa a cena.
[D2] CASTING: corpo-prova TRAVADO na etnia da pagina, narradora SOLTA. Razao do
     operador: o espectador de 50+ se identifica com o CORPO, nao com quem
     narra — entao a congruencia vale onde ela vende, e o maior eixo de
     variacao visual do lote (8 arquetipos femininos observados) fica livre.
     ⚠️ SOLTA na etnia, nao na idade: o piso de 28 anos do organicwave_short
     continua valendo (ver `IDADE_MINIMA_NARRADORA`).
⚠️ A MAO: por UN4, via TR1.2 da doutrina, o proxy nasce no punho ESQUERDO — e'
     o esquerdo que desce e sobe na troca, e a DIREITA e' a mao livre que
     trabalha a substancia (invariante 4/28, o VERBO do formato).
[D3] FIGURINO: seguir os videos-fonte (cropped, joias de ouro). 🟡 Divergencia
     DELIBERADA do UN1 do UNCAO, que manda roupa coberta e continua valendo
     integralmente la'. Por isso TR19 e' AVISO, nunca ERRO: o operador pode
     querer rodar um lote coberto sem que o linter reprove.
[D4] O PROP NAO CRESCE. Achado ① da fonte: 8/8 sem crescimento, VFX, morph ou
     antes/depois — e convertem 25-30K. A promessa numerica e' 100% VERBAL e
     quem a entrega e' a REACAO FACIAL dela, no frame exato do numero. 🟡
     Divergencia deliberada do P17/P20 do PRISMA. Economia medida: queimamos 5
     tentativas de geoduck e uma coreografia de 7 elementos para conseguir
     crescimento na tela; o concorrente faz 25-30K com o prop parado.

⚠️ ADAPTAR AQUI E' EXPANDIR, NAO COMPRIMIR (TR14, ordem do operador)
A fonte fala ~35-40 palavras em 13s. Nosso orcamento e' 82-96 palavras em 24s.
Copiar os 4 beats deles deixa ar sobrando, e ar num take de 8s vira pausa
morta. Por isso cada cena e' composta de DOIS pools (crendice+desmentido,
fundida+prova, barreira+cta+gate) em vez de uma frase so' — e o PISO e' cobrado
pelo linter, nao so' o teto.

⚠️ TENSAO ARITMETICA ABERTA, PARA O ED DECIDIR
A soma dos tetos por cena (22+34+26) e' 82, que e' exatamente o PISO do
orcamento total da doutrina (82-96). Logo o video so' entraria na faixa com as
tres cenas no teto exato, e nunca passaria de 82. O motor cobra o que da' para
cobrar — piso e teto POR CENA, medidos por enumeracao exaustiva no self-test —
e entrega hoje 66-78 palavras (media ~71). Para chegar a 82-96 de verdade, ou
os tetos por cena sobem, ou a faixa total desce. E' decisao de copy: alcada.

Uso:
    python funil-organico/troca_short.py --pagina joe --n 2
    python funil-organico/troca_short.py --pagina marcus --n 3 --seed 42
    python funil-organico/troca_short.py --pagina ray --n 1 --dry-run
    python funil-organico/troca_short.py --pagina joe --n 10 --degrau condicional
    python funil-organico/troca_short.py --stats
"""

import argparse
import json
import os
import random
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import short_comum as sc                                        # noqa: E402
from nucleo_sonoro import sonorizar                             # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(AQUI, ".troca-short-ledger.json")

TITULO = "AGENTE TROCA SHORT"
SUBTITULO = "o proxy sai, o mecanismo entra no mesmo ponto do quadro · 3 cenas"
SLUG = "troca-short"

CENAS_UI = ["1 · A CRENDICE", "2 · A TROCA + O BATISMO", "3 · O CORPO-PROVA + CTA"]

# TR14. ⚠️ O ORCAMENTO E' PISO **E** TETO — ordem do operador. Tratar o piso
# como "julgamento que mora na doutrina" foi o que deixou 48% das cenas 2
# abaixo dele: piso nao cobrado e' piso que nao existe. Os dois sao mecanicos e
# moram aqui.
TETO_FALA = {1: 22, 2: 34, 3: 26}
PISO_FALA = {1: 16, 2: 26, 3: 20}

# ⚠️ TENSAO ARITMETICA REGISTRADA (nao resolvida — e' alcada do Ed):
# a soma dos tetos e' 22+34+26 = 82, que e' exatamente o PISO do orcamento
# total da doutrina (82-96 palavras). Ou seja: o video so' entra na faixa com
# as TRES cenas no teto exato, e nunca passa de 82. Ou os tetos por cena sobem,
# ou a faixa total desce. Enquanto isso o motor cobra o que da' para cobrar —
# piso e teto POR CENA — e o AVISO de total dispara acima de 96 (a borda de
# cima da faixa), nunca acima de 82, que e' a borda de BAIXO.
TETO_TOTAL = 96

# congruencia [D2]: so' o CORPO-PROVA casa com o avatar da pagina.
# A narradora NAO usa este dict — ela e' sorteada livre, e o motor nunca
# escreve adjetivo de etnia junto dela (TR18).
ETNIA = {"joe": "white American", "ray": "white American", "matt": "white American",
         "marcus": "Black American", "chuck": "Black American"}

NUCLEO = ["Johnson", "soldier", "pecker", "manhood", "wiener", "tool", "old boy"]


# ---------------------------------------------------------------------------
# STRINGS TRAVADAS — ⛔ constantes, nunca redigitadas
# ---------------------------------------------------------------------------
# ⚠️ Os `%s` sao SLOTS do motor, nao texto a reescrever. Comprimir uma travada
# "com as minhas palavras" ja' entregou esqueleto 3D no lugar da placa em corte
# (RUNBOOK-app-offline §Por que portar).

CAUDA = "Shot on iPhone, natural grain. No on-screen text, no watermark."

# P12. Fecha todo IMAGE. Os reels tem pote de Vicks e caixa Arm & Hammer em
# 8/8 — nos substituimos por FORMA, nunca por marca.
# ⚠️ ESCRITA NA AFIRMATIVA de proposito. A versao anterior dizia "Nothing in the
# frame carries a readable label, logo or brand" e injetava `label`, `logo` e
# `brand` num prompt cuja tese e' que nao ha' nenhum — a mesma mecanica de
# `fully clothed` (licoes-producao-veo §Declaracao e' municao). Quando da' para
# dizer o mesmo pela positiva, diz-se pela positiva.
FRASE_SEM_MARCA = "Every container in the frame is plain and unlabelled."

# ⭐ TR10/[D1] — a F12b adaptada. Slots: peca da calca, proxy (ancorado NELE),
# relacao.
# ⛔ `lap` E' A COORDENADA E E' STRING TRAVADA. `beside the lap of his khaki
# shorts` foi o que substituiu `level with his groin` depois de uma recusa paga
# (prop-metaforas §Recusa do gerador; F12b: "`lap` + peca de roupa entrega a
# mesma coordenada de `groin` sem o termo anatomico"). Uma versao anterior deste
# motor trocou `lap` por `front pocket`/`side pocket` "para acompanhar a calca
# sorteada": isso e' (a) reescrever string validada sem ordem do operador e
# (b) mover o prop da virilha para o quadril, que e' AMPUTAR A CENA para
# destravar — o reflexo que o CLAUDE.md §Alcada proibe. So' a PECA varia.
# ⚠️ Tensao real, reportada e nao resolvida aqui: o homem esta' DE PE (TR10) e
# homem de pe' nao tem colo. Ou a postura cede, ou a ancora, ou nasce uma
# terceira formulacao — decisao do Ed.
TR_MAO_PROPRIA_IMAGE = (
    "In his own fist, held down beside the lap of his %s, he holds %s. Standing "
    "beside him, %s points one finger down at it without touching him, talking "
    "straight to camera."
)

# a mesma regra no movimento. `never touches him` e' o que o TR10 cobra.
# ⚠️ A AGENCIA e' o que a F12b cobra, e ela e' declarada por DUAS coisas: o
# olhar dele na lente e o punho onde estava. A versao anterior escrevia "He
# stands still and says nothing, his own fist steady at his side" — que e'
# exatamente o vocabulario do homem ABATIDO E PASSIVO das 4 recusas
# deterministicas, e ainda tirava o punho do colo.
# ⛔ E o objeto e' NOMEADO (a doutrina so' proibe nomear na `Dialogue:`; na
# direcao de cena o legume se nomeia normalmente). "The thing in his fist ...
# same length" era eufemismo somado a injecao de `length`.
TR_MAO_PROPRIA_TAKE = (
    "Her pointing finger stays close but never touches him. He keeps his eyes "
    "on the lens and never speaks; his own fist stays where it is. The %s in "
    "his own fist stays exactly as it appears in the first frame — completely "
    "motionless for the entire shot."
)

# TR1 achado ②, detalhe forense do v01 e do v03: o pote ja' estava ABERTO na
# bancada desde o frame 1 e a TAMPA continua la' depois que ele sobe pra mao.
# O "reveal" nao apresenta nada novo — puxa pro primeiro plano o que estava
# plantado. ⛔ Objeto que entra de fora do quadro nao e' troca, e' corte
# disfarcado.
# ⚠️ O detalhe forense e' POR MECANISMO (campo `pousado`): 7 dos 10 mecanismos
# nao tem tampa (tigela, pires, sache, copo, panela). Mandar desenhar "its lid
# lying face-up" numa tigela e' contradicao dentro do proprio IMAGE — e prompt
# que se contradiz o modelo resolve como quiser.
TR_TROCA_IMAGE = (
    "The %s has been standing on the %s since the first frame, %s."
)

# ⭐⭐ A TROCA. E' o agente inteiro. ⛔ Nunca `swap`/`switch`/`replaces` — com o
# resultado nomeado o Veo troca o objeto CORTANDO; descreve-se descida, subida
# e ponto.
# ⚠️ COREOGRAFIA EM BATIDAS COM SEGUNDOS, como a TR1 da doutrina prescreve pelo
# metodo 🟢 de prop-metaforas §Coreografia: "verbo sozinho nao e' instrucao — o
# Veo precisa do COMO". A versao anterior tinha comprimido as tres batidas numa
# frase so' e ainda descia o proxy `onto the workbench` enquanto a frase
# seguinte dizia que ele ficava `on the wooden board`: duas superficies para a
# mesma acao, no take que E' o agente.
# ⚠️ MAO ESQUERDA (UN4, via TR1.2 da doutrina): o proxy nasce no punho esquerdo,
# entao e' o esquerdo que desce e sobe; a direita continua sendo a que trabalha
# a substancia. Slots: proxy, proxy, mecanismo.
TR_TROCA_TAKE = (
    "0 to 2 seconds: she keeps talking to the lens while her left hand lowers "
    "the %s straight down onto the wooden board in front of her and lets go of "
    "it. The %s stays lying on that board, still in frame, for the rest of the "
    "shot. 2 to 4 seconds: the same left hand comes straight back up to the "
    "same spot in the frame, at the same height beside her face, now holding "
    "%s — same point in the frame, same hand, same height, one continuous take. "
    "4 to 8 seconds: her hand does not move again and what it holds stays at "
    "that same height beside her face until the end of the shot."
)

# TR7 achado ③: a boca cita 1 ingrediente, a imagem mostra 3-4. E' o lastro do
# "full recipe" — nos prometiamos a receita completa sem nunca provar em imagem
# que existe uma.
TR_BANCADA_RECIBO = (
    "Laid out on the %s beside her, never touched and never mentioned: %s. "
    + FRASE_SEM_MARCA
)

# [D4] a promessa e' entregue pela CARA dela, no frame do numero.
# ⚠️ A travada de imobilidade e' a de prop-metaforas §Regra dos dois lados,
# copiada NUA. A versao anterior a prefixava com "Nothing in her hand changes
# size, shape or state at any point" e a infixava com "same position, same
# angle, same length": negacao que injeta `size`, `state` e `length` num prompt
# cuja tese e' justamente que nada muda de tamanho — municao de graca pela
# mecanica ja' documentada de `fully clothed`. E ainda inchava a travada 3x
# (F12c: string validada e' intocavel, descricao livre e' que encolhe).
# ⛔ zero `mouth open`/`tongue`/`lips parted` (risco 4 da §6 do mapa) — a reacao
# entra por outro traco: sobrancelha, olho, `caught mid-word`.
# Slots: nome do proxy, gatilho de sincronia da reacao.
TR_SEM_CRESCIMENTO = (
    "The %s in her fist stays exactly as it appears in the first frame — "
    "completely motionless for the entire shot. %s her eyes go wide and her "
    "eyebrows lift, caught mid-word, eyes locked on the lens."
)

# ⚠️ O gatilho de sincronia segue a FAMILIA da promessa sorteada: "On the
# number" numa crendice sem numeral (25% delas sao da familia de resistencia)
# manda o Veo sincronizar com algo que a fala nao tem, e ele inventa onde.
GATILHO_NUMERO = "On the number,"
GATILHO_PROMESSA = "On the promise,"

# geometria da fonte (invariantes 2, 3 e 5 do mapa). O prop e' a UNICA regua de
# escala do quadro: baixar pra bancada mata a relacao corpo-prop e a cena vira
# demonstracao culinaria. ⚠️ `held beside her cheek at eye level` no lugar de
# `pressed against her face`, que e' o risco 5 ja' desarmado.
# ⚠️ PUNHO ESQUERDO, por UN4 (via TR1.2 da doutrina). A versao anterior deste
# motor inverteu para a direita por decisao propria, alegando coerencia entre as
# travadas — o argumento era falso (a TR_VAIVEM nao nomeava mao nenhuma) e a
# escolha e' de CENA, ou seja, alcada do Ed. Doutrina manda.
TR_PROXY_NA_MAO = (
    "She holds it upright in her left fist, tip pointing up, held beside her "
    "cheek at eye level, in the same focal plane as her face."
)

# ⭐ invariante 4/28 — A MAO LIVRE E' O VERBO. Mao parada segurando = foto de
# produto. Ela precisa estar declarada no IMAGE: sem isso o TAKE manda trabalhar
# "along the length of it" sobre uma imagem em que a unica mao declarada e' a
# que segura o prop de pe' ao lado da bochecha — e prompt que se contradiz o
# modelo resolve como quiser. Slot: a substancia (invariante 5: ela ja' esta'
# nas maos no frame 1).
TR_MAO_LIVRE = ("Her free right hand is on it as well, fingers spread along its "
                "length, %s on her fingertips.")

# risco 1 da §6: `slides her hand up and down`, `strokes`, `pumps`, `grips` sao
# recusa provavel. Alavanca 4 + alavanca 3 — o verbo troca e o GENERO DA IMAGEM
# e' nomeado. Nomear o genero e' obrigatorio, nao opcional.
# ⚠️ A analogia tem de apontar para FORA da cena: rodar "the way a cook rubs
# marinade into a squash" com uma abobrinha (zucchini = squash) ou com o pescoco
# de uma butternut squash na mao e' analogia circular, e circular nao desambigua
# nada. Cada proxy declara a sua familia (campo `analogia`).
TR_VAIVEM = "Her free right hand works it along the length of it, %s."

ANALOGIAS = {
    "squash": "the way a cook rubs marinade into a squash before roasting",
    "ribs": "the way a cook works a dry rub into a rack of ribs",
}

# risco 2 da §6, o ponto mais arriscado do quadro. ⛔ Nao amputar o fio:
# redirecionar o DESTINO (a tabua, nunca o corpo dela) e nomear o genero.
# E' o destino-corpo que carrega a leitura de ejaculacao, nao o fio.
# ⚠️ A SUBSTANCIA E' NOMEADA. A formulacao validada da §6.2 e' `a slow thread of
# honey runs off...`; uma versao anterior trocou o substantivo por `it`, e como
# nenhuma textura nomeava a substancia, o referente mais proximo de `it` passava
# a ser O PROXY — ou seja, um fio saindo da ponta de baixo de um objeto falico,
# com a substancia anonima e a analogia do dipper pendurada sem antecedente.
# Era remover a unica salvaguarda do ponto mais arriscado do quadro.
TR_FIO = ("a slow thread of the %s runs off the bottom end and down onto the "
          "wooden board, the way honey runs off a dipper")


# ---------------------------------------------------------------------------
# ELENCO
# ---------------------------------------------------------------------------
# ⭐ [D2] A NARRADORA E' SOLTA — pool unico, sem etnia declarada em lugar nenhum.
# O cabelo e' o descritor mais etnico que existe e o pool tem afro, box braids,
# ruivo, platinado, loiro e tapered: o render varia sozinho. Se o operador
# quiser garantir proporcao (ex.: metade do lote com narradora negra), isso e'
# filtro por pagina no sortear() e e' ORDEM DELE — nao se decide aqui.
# ⚠️ Marca facial obrigatoria (P6): e' o que segura a continuidade do rosto
# entre as tres cenas. Sem ela o Veo troca de pessoa — falha que ja' derrubou a
# cena do casal do VAZAMENTO.
# ⚠️ [D3] `cropped` em todas: divergencia deliberada do UN1, com selo 🟡.
# ⛔ PISO DE IDADE 28 — herdado do organicwave_short (`IDADE_MINIMA_MULHER`), que
# o carrega com o motivo escrito: "ja' pagamos para descobrir que idade em cena
# com conteudo de ED e' zona sensivel", e com o aviso de nao baixar sem ordem do
# operador. Este motor tinha baixado para 24 sem ordem registrada em lugar
# nenhum — reversao silenciosa de uma regra que existe por falha de
# classificador documentada. Pesa mais aqui do que la': a cena 3 pareia a
# narradora com um corpo-prova de ate' 65 numa composicao de proxy falico, e a
# politica de MENORES e' a determinista (nao cede a regerar) e e' sensivel a
# geometria de intimidade + diferenca de idade, nao a idade real.
IDADE_MINIMA_NARRADORA = 28

NARRADORAS = [
    {"id": "ruiva_sardas", "idade": 29,
     "marca": "a heavy dusting of freckles across her nose and cheeks and long copper-red hair",
     "roupa": "a cropped white ribbed tank top and high-waisted jeans"},
    {"id": "afro_curto", "idade": 34,
     "marca": "a short natural afro and a small dark beauty mark high on her left cheekbone",
     "roupa": "a cropped mustard knit top and a thin gold chain"},
    {"id": "loira_raiz", "idade": 41,
     "marca": "long honey-blonde hair with grown-out roots and a deep dimple in her right cheek",
     "roupa": "a cropped black t-shirt and large gold hoop earrings"},
    {"id": "rabo_alto", "idade": 30,
     "marca": "jet-black hair in a high slicked-back ponytail and a wide gap between her front teeth",
     "roupa": "a cropped grey sweatshirt cut off above the waist"},
    {"id": "oculos_especialista", "idade": 37,
     "marca": "shoulder-length dark hair, thin gold-rimmed glasses and a narrow widow's peak",
     "roupa": "a cropped olive button-up shirt knotted at the front"},
    {"id": "tranca_caixa", "idade": 31,
     "marca": "waist-length box braids and dark plum lipstick",
     "roupa": "a cropped burgundy tank top and stacked gold bangles"},
    {"id": "grisalha_coque", "idade": 45,
     "marca": "silver-streaked dark hair in a loose bun and deep laugh lines at the outer corners of her eyes",
     "roupa": "a cropped denim shirt knotted at the waist"},
    {"id": "bob_platinado", "idade": 28,
     "marca": "a bleached-platinum bob cut sharp at the jaw and a small hoop in her left nostril",
     "roupa": "a cropped lilac zip-up and gold rings on three fingers"},
    {"id": "franja_reta", "idade": 33,
     "marca": "long chestnut hair with a blunt fringe and a small crescent birthmark at her right temple",
     "roupa": "a cropped rust-orange top and a heavy gold pendant"},
    {"id": "cachos_bronze", "idade": 39,
     "marca": "tight auburn-dyed curls and metallic bronze eyeshadow",
     "roupa": "a cropped emerald wrap top and long gold drop earrings"},
    # ⛔ `baby tee` saiu: e' o token `baby` entrando de graca num prompt que ja'
    # pareia mulher jovem com homem de 51-65 e objeto falico — mesma mecanica de
    # `clothed`/`celebrity`. `ringer tee` e' a mesma peca.
    {"id": "morango_jovem", "idade": 28,
     "marca": "long wavy strawberry-blonde hair and a beauty mark just above her upper lip",
     "roupa": "a cropped pale-blue knit top and a thin gold chain bracelet"},
    {"id": "tapered_macas", "idade": 43,
     "marca": "a close tapered cut faded at the sides and high sharp cheekbones",
     "roupa": "a cropped charcoal turtleneck and heavy gold hoops"},
    {"id": "tranca_unica", "idade": 30,
     "marca": "long jet-black hair in a single braid over one shoulder and a small dark tattoo of three stars behind her right ear",
     "roupa": "a cropped white crochet top and gold bangles"},
    {"id": "coque_bagunca", "idade": 36,
     "marca": "sandy-blonde hair in a messy topknot and pale grey-green eyes under heavy dark brows",
     "roupa": "a cropped sage-green tank top and a slim gold watch"},
]

# ⭐ [D2] O CORPO-PROVA E' TRAVADO pela etnia da pagina. Dois pools espelhados
# (mesma idade, mesma roupa, mesma calca por indice) — o que muda e' so' o
# descritor de cabelo/barba, que e' onde a etnia se le'. Espelhar em vez de
# escrever dois pools independentes mantem a comparacao entre paginas honesta:
# a unica variavel que muda entre joe e marcus e' a etnia, nunca o figurino.
# ⚠️ 51-65 anos: e' o CORPO com que o espectador se identifica [D2].
# ⚠️ A `calca` existe para a ancora de roupa da F12b (TR10): `beside the lap of
# his khaki shorts`. ⛔ Nada de oracao de bolso aqui — ela so' existia para a
# ancora reescrita (`front pocket`), que era o desvio, e cada palavra a mais
# no IMAGE 03 e' superficie de bloqueio no bloco mais arriscado do lote (F12c).
CORPOS_PROVA_CLARA = [
    {"id": "prata_pintinha", "idade": 58,
     "marca": "thick silver hair swept back and a small dark beauty mark high on his left cheekbone",
     "roupa": "a plain navy short-sleeve work shirt",
     "calca": "khaki work pants"},
    {"id": "barba_branca", "idade": 62,
     "marca": "a full white beard trimmed close and deep-set pale grey eyes",
     "roupa": "a heather-grey pocket tee",
     "calca": "faded blue jeans"},
    {"id": "covinha_tempora", "idade": 55,
     "marca": "dark hair greying at the temples and a deep vertical dimple in his left cheek",
     "roupa": "an olive canvas shirt with the sleeves rolled to the elbow",
     "calca": "brown corduroy trousers"},
    {"id": "palpebra_pesada", "idade": 64,
     "marca": "a bald crown with close-cropped white hair at the sides and heavy hooded eyelids",
     "roupa": "a light blue short-sleeve button-down",
     "calca": "grey twill work pants"},
    {"id": "queixo_fendido", "idade": 51,
     "marca": "sandy blond hair going grey at the sides and a strong cleft chin",
     "roupa": "a charcoal henley with the sleeves pushed up",
     "calca": "dark denim jeans"},
    {"id": "aco_sardas", "idade": 60,
     "marca": "wavy steel-grey hair worn a little long and light freckles across his nose",
     "roupa": "a faded red flannel shirt",
     "calca": "tan chinos"},
    {"id": "bigode_guidao", "idade": 57,
     "marca": "a shaved head and a thick grey handlebar moustache",
     "roupa": "a mustard-yellow snap-button shirt",
     "calca": "black work trousers"},
    {"id": "dentes_falha", "idade": 65,
     "marca": "white hair combed straight back and a wide gap between his front teeth",
     "roupa": "a cream short-sleeve camp shirt",
     "calca": "olive cargo pants"},
    {"id": "sinal_olho", "idade": 53,
     "marca": "short auburn hair fading to grey and a small mole at the outer corner of his right eye",
     "roupa": "a slate-blue polo shirt",
     "calca": "stone-coloured chinos"},
    {"id": "flat_top", "idade": 61,
     "marca": "a flat-top cut gone completely white and thick greying eyebrows",
     "roupa": "a forest-green fishing shirt with two chest pockets",
     "calca": "khaki shorts"},
    {"id": "mecha_branca", "idade": 56,
     "marca": "thick chestnut hair with a bright white streak at the left temple",
     "roupa": "a rust-red pocket tee",
     "calca": "grey sweatpants"},
    {"id": "corte_sobrancelha", "idade": 63,
     "marca": "a close silver crew cut and a long-healed nick through his right eyebrow",
     "roupa": "a blue-and-white plaid short-sleeve shirt",
     "calca": "brown canvas work pants"},
]
CORPOS_PROVA_ESCURA = [
    {"id": "prata_barba", "idade": 58,
     "marca": "close-cropped silver hair and a neat white beard along the jaw",
     "roupa": "a plain navy short-sleeve work shirt",
     "calca": "khaki work pants"},
    {"id": "locs_ambar", "idade": 62,
     "marca": "salt-and-pepper locs gathered back and warm amber eyes",
     "roupa": "a heather-grey pocket tee",
     "calca": "faded blue jeans"},
    {"id": "fade_covinha", "idade": 55,
     "marca": "a close grey fade and a deep vertical dimple in his left cheek",
     "roupa": "an olive canvas shirt with the sleeves rolled to the elbow",
     "calca": "brown corduroy trousers"},
    {"id": "cavanhaque", "idade": 64,
     "marca": "a smooth shaved head and a neat silver goatee",
     "roupa": "a light blue short-sleeve button-down",
     "calca": "grey twill work pants"},
    {"id": "twists_queixo", "idade": 51,
     "marca": "short black twists just starting to grey and a strong cleft chin",
     "roupa": "a charcoal henley with the sleeves pushed up",
     "calca": "dark denim jeans"},
    {"id": "afro_sardas", "idade": 60,
     "marca": "a silver-flecked afro worn low and light freckles across his nose",
     "roupa": "a faded red flannel shirt",
     "calca": "tan chinos"},
    {"id": "careca_bigode", "idade": 57,
     "marca": "a bald head and a thick grey moustache",
     "roupa": "a mustard-yellow snap-button shirt",
     "calca": "black work trousers"},
    {"id": "branco_falha", "idade": 65,
     "marca": "short white hair and a wide gap between his front teeth",
     "roupa": "a cream short-sleeve camp shirt",
     "calca": "olive cargo pants"},
    {"id": "hightop_sinal", "idade": 53,
     "marca": "a grey high-top fade and a small mole at the outer corner of his right eye",
     "roupa": "a slate-blue polo shirt",
     "calca": "stone-coloured chinos"},
    {"id": "afro_curto_grisalho", "idade": 61,
     "marca": "a short grey afro and thick greying eyebrows",
     "roupa": "a forest-green fishing shirt with two chest pockets",
     "calca": "khaki shorts"},
    {"id": "mecha_tempora", "idade": 56,
     "marca": "a close grey afro with a bright white streak above the left temple",
     "roupa": "a rust-red pocket tee",
     "calca": "grey sweatpants"},
    {"id": "barba_corte", "idade": 63,
     "marca": "a neat grey beard and a long-healed nick through his right eyebrow",
     "roupa": "a blue-and-white plaid short-sleeve shirt",
     "calca": "brown canvas work pants"},
]


def homens_de(pagina):
    """[D2] O corpo-prova casa com o avatar da pagina — congruencia inviolavel."""
    return CORPOS_PROVA_CLARA if "white" in ETNIA[pagina] else CORPOS_PROVA_ESCURA


def mulheres_de(pagina):
    """[D2] A narradora e' SOLTA: pool unico, a pagina nao filtra nada.

    A funcao existe por contrato da UI (ui_agente resolve o eixo por nome) e
    para deixar a excecao explicita em codigo: e' a UNICA vez que "etnia do REF
    = etnia do avatar" nao vale, e vale porque neste angulo o REF nao e' o
    avatar — o avatar e' o corpo-prova da cena 3.
    """
    return NARRADORAS


# ---------------------------------------------------------------------------
# EIXOS VISUAIS
# ---------------------------------------------------------------------------
# ⚠️ Escala absurda NAO prediz performance (medido na fonte): os dois reels de
# banana em tamanho natural fizeram 25,5K e 25,9K; a abobrinha de 45-50cm fez
# 5,6K. Por isso a banana entra no pool no tamanho natural, sem ancora de
# antebraco — e' o unico item assim, de proposito.
# O campo `nome` serve ao linter TR3 (varrer as falas) E a direcao de cena: a
# doutrina so' proibe nomear o proxy na `Dialogue:` — "✅ na direcao de cena o
# legume e' nomeado normalmente, e' la' que ele precisa ser desenhado". Chamar o
# objeto de `the thing in his fist` era eufemismo desnecessario.
# ⚠️ `img` e `img_dele` sao O MESMO OBJETO com a ancora no corpo certo: a regua
# e' o antebraco de quem esta' segurando. Na cena 3 quem segura e' ELE — 83% dos
# lotes saiam com "in his own fist ... as long as HER forearm", contra a letra
# da TR10 da doutrina (`as long as his forearm and as thick as his wrist`).
# ⚠️ A BANANA continua em tamanho natural nos dois, de proposito: escala absurda
# NAO prediz performance (os dois reels de banana natural fizeram 25,5K e 25,9K;
# a abobrinha de 45-50cm fez 5,6K), e "at its natural size" ja' e' declaracao de
# escala — a mesma na cena 1 e na 3, que e' o que o corolario da TR2 cobra.
# ⚠️ `analogia` escolhe o dominio culinario do TR_VAIVEM: ele tem de ser
# DIFERENTE do proxy em quadro, senao a alavanca 3 (nomear o genero da imagem)
# aponta para dentro da propria cena e nao desambigua nada.
PROXIES = [
    {"id": "cenoura", "nome": "carrot", "analogia": "squash",
     "img": "a large raw carrot, the skin still rough, as long as her forearm and as thick as her wrist",
     "img_dele": "a large raw carrot, the skin still rough, as long as his forearm and as thick as his wrist"},
    {"id": "abobrinha", "nome": "zucchini", "analogia": "ribs",
     "img": "a long dark-green zucchini, as long as her forearm and as thick as her wrist",
     "img_dele": "a long dark-green zucchini, as long as his forearm and as thick as his wrist"},
    {"id": "banana", "nome": "banana", "analogia": "squash",
     "img": "a ripe banana at its natural size, the skin yellow and lightly spotted",
     "img_dele": "a ripe banana at its natural size, the skin yellow and lightly spotted"},
    {"id": "pepino", "nome": "cucumber", "analogia": "ribs",
     "img": "a long smooth English cucumber, as long as her forearm and as thick as her wrist",
     "img_dele": "a long smooth English cucumber, as long as his forearm and as thick as his wrist"},
    {"id": "daikon", "nome": "daikon", "analogia": "squash",
     "img": "a pale daikon radish with the tapered end pointing up, as long as her forearm",
     "img_dele": "a pale daikon radish with the tapered end pointing up, as long as his forearm"},
    {"id": "berinjela", "nome": "eggplant", "analogia": "squash",
     "img": "a deep purple eggplant held by the stem end, as thick as her wrist",
     "img_dele": "a deep purple eggplant held by the stem end, as thick as his wrist"},
    {"id": "pastinaga", "nome": "parsnip", "analogia": "squash",
     "img": "a thick cream-coloured parsnip, as long as her forearm",
     "img_dele": "a thick cream-coloured parsnip, as long as his forearm"},
    {"id": "milho", "nome": "corn", "analogia": "ribs",
     "img": "an ear of sweet corn stripped clean of its husk, kernels tight and glossy, as long as her hand",
     "img_dele": "an ear of sweet corn stripped clean of its husk, kernels tight and glossy, as long as his hand"},
    {"id": "calabaza", "nome": "squash", "analogia": "ribs",
     "img": "the long solid neck of a butternut squash, as thick as her wrist",
     "img_dele": "the long solid neck of a butternut squash, as thick as his wrist"},
    {"id": "linguica", "nome": "sausage", "analogia": "squash",
     "img": "a thick smoked sausage link, as long as her forearm",
     "img_dele": "a thick smoked sausage link, as long as his forearm"},
    {"id": "batata_doce", "nome": "sweet potato", "analogia": "squash",
     "img": "a long sweet potato with the tapered end pointing up, as long as her forearm",
     "img_dele": "a long sweet potato with the tapered end pointing up, as long as his forearm"},
]

# A substancia do hook: domestica e reconhecivel em meio segundo (gramatica do
# SUBSTANCIA_ABSURDA). ⛔ P12: o `pote` e' descrito por FORMA, nunca por marca —
# `Vicks` virou `menthol rub` na fala e um pote azul baixo de pomada na imagem;
# a caixa laranja de bicarbonato virou pote de vidro liso com po branco.
# ⚠️ `fala` cabe em 2 palavras no maximo ("apple cider vinegar" foi cortado
# para "cider vinegar") — o pior caso do teto da cena 1 depende disso.
SUBSTANCIAS = [
    {"id": "mel", "fala": "honey",
     "pote": "an open glass jar of raw honey with a wooden dipper resting across the rim"},
    {"id": "curcuma", "fala": "turmeric",
     "pote": "a rustic ceramic bowl of deep yellow turmeric paste with a spoon standing in it"},
    {"id": "oleo_coco", "fala": "coconut oil",
     "pote": "an open glass jar of white coconut oil softened at the surface, the lid tipped against it"},
    # ⚠️ Pote BRANCO DE CERAMICA, nao azul de vidro: pote azul baixo de pomada e'
    # a silhueta e a cor da Vicks — trade dress reconhecivel sem rotulo, e P12
    # manda substituir por FORMA, nao reproduzir a forma da marca.
    {"id": "mentol", "fala": "menthol rub",
     "pote": "a squat white ceramic jar of pale ointment, the lid lying face-up beside it"},
    {"id": "azeite", "fala": "olive oil",
     "pote": "a dark unlabelled glass bottle tipped against a shallow white saucer of green oil"},
    {"id": "mostarda", "fala": "mustard",
     "pote": "a small stoneware crock of coarse yellow mustard with a wooden spoon in it"},
    {"id": "iogurte", "fala": "yogurt",
     "pote": "a plain white bowl of thick yogurt with a spoon laid across it"},
    {"id": "amendoim", "fala": "peanut butter",
     "pote": "an open glass jar of peanut butter with a knife standing upright in it"},
    {"id": "clara_ovo", "fala": "egg white",
     "pote": "two cracked eggshells on a saucer beside a glass bowl of clear egg white"},
    # ⚠️ unica substancia em PO do pool: `fluida: False` impede que ela caia
    # numa textura de escorrimento ("a slow thread of the baking soda") — a
    # textura e' eixo independente (TR6), mas independente nao e' impossivel, e
    # prompt fisicamente impossivel e' licenca de alucinacao.
    {"id": "bicarbonato", "fala": "baking soda", "fluida": False,
     "pote": "a plain glass jar of fine white powder with a wooden spoon beside it"},
    {"id": "aloe", "fala": "aloe",
     "pote": "a cut aloe leaf on a wooden board, clear gel beading along the open edge"},
    {"id": "banha", "fala": "bacon grease",
     "pote": "a white enamel tin of pale rendered fat with a spoon resting in it"},
    {"id": "vinagre", "fala": "cider vinegar",
     "pote": "an unlabelled amber glass bottle beside a small dish of cloudy vinegar"},
    {"id": "gengibre", "fala": "ginger",
     "pote": "a knob of fresh ginger root grated into a small dish beside a rustic ceramic bowl"},
]

# ⭐ TR6, achado ④: a fisica da substancia e' EIXO PROPRIO, independente da
# substancia. E' a carga que a fala nao paga — no v02 o gel escorre em filetes
# opacos e a leitura e' inequivoca com zero palavras.
# ⛔ NENHUMA textura termina no corpo dela. Os dois itens de fio redirecionam
# para a TABUA e nomeiam o genero da imagem ("the way honey runs off a
# dipper" / "the way batter runs off a whisk"): e' o destino que carrega a
# leitura de ejaculacao, nao o fio (risco 2 da §6).
# ⚠️ TODA textura NOMEIA a substancia (`%s`). Antes todas diziam `it`, e como o
# `it` mais proximo no prompt era o PROXY, a textura descrevia o proxio objeto
# falico em vez do que estava passado nele — no item do fio isso removia a unica
# salvaguarda do ponto mais arriscado do quadro (ver TR_FIO).
# ⚠️ `curta` e' a mesma textura em uma oracao, para as cenas 2 e 3: sem ela o
# proxy saia LIMPO nos IMAGE 02 e 03, o que contradiz o invariante 26/28 e o
# proprio checklist da doutrina ("o proxy lambuzado FICA em quadro").
TEXTURAS = [
    {"id": "verniz", "fluida": True,
     "desc": "the whole surface of it is coated in a thin wet varnish of the %s, catching one hard specular highlight down its length, nothing running",
     "curta": "still wet with %s"},
    {"id": "gel_placas", "fluida": True,
     "desc": "thick opaque plates of the %s sit on it with clean gaps between them, holding every ridge they were laid down in",
     "curta": "still plated with %s"},
    {"id": "fio_tabua", "fluida": True, "desc": TR_FIO,
     "curta": "%s still running off its lower end onto the board"},
    {"id": "pasta_seca", "fluida": False,
     "desc": "a dull dry paste of the %s covers it in fingerprint smears and small dry lumps, none of it running",
     "curta": "still smeared with dry %s"},
    {"id": "grumos", "fluida": True,
     "desc": "the %s is beaded over it in small round glossy drops that hold their shape and do not move",
     "curta": "still beaded with %s"},
    {"id": "pelicula_fosca", "fluida": False,
     "desc": "a matte film of the %s has dried unevenly over it, cracked into fine plates where it set",
     "curta": "still filmed over with dried %s"},
    {"id": "camada_espessa", "fluida": True,
     "desc": "a heavy even coat of the %s, thick enough to hold the ridge marks her fingers left behind",
     "curta": "still thick with %s"},
    {"id": "pingo_tabua", "fluida": True,
     "desc": "a single slow drip of the %s has run down the length of it and gathered in a ring on the wooden board below, the way batter runs off a whisk",
     "curta": "still ringed where the %s ran down onto the board"},
    {"id": "teias_dedos", "fluida": True,
     "desc": "fine glossy strands of the %s stretch between her thumb and forefinger each time they lift away from it",
     "curta": "still stringy with %s"},
    {"id": "brilho_seco", "fluida": False,
     "desc": "only a faint dry sheen of the %s sits on it, no thickness at all, just a change in how the light comes back off it",
     "curta": "still faintly sheened with %s"},
]

# O alibi domestico (invariante 16/8-8): em estudio ou fundo neutro a MESMA
# acao muda de genero — e de politica de plataforma. O `escritorio` e' o alibi
# de AUTORIDADE do v08, o de 82K, que troca cozinha por estante e diplomas.
# ⚠️ Classes DIFERENTES de verdade (laminado, marmore, fazenda, cabana, anos
# 70, trailer, RV, lavanderia, salao comunitario), nao decoracao trocada.
# ✅ Bandeira dos EUA em todos, em FORMA diferente cada vez — 8/8 na fonte, e
# nao e' marca: esta' no nosso catalogo (prop-metaforas §Props de autoridade).
# ⚠️ `re_ancora` existe porque a entropia COLAPSAVA entre o spec e o prompt: o
# `set` rico (14 valores) entrava so' no IMAGE 01, e os outros seis blocos
# recebiam apenas `curto`+`bancada` — 8 e 7 valores, com "kitchen" em 50% e
# "counter" em 51%. Metade do lote dizia literalmente "in the same kitchen, same
# light" e mais nada, e a bandeira dos EUA (invariante 15/28, obrigatoria em
# quadro) sumia das cenas 2 e 3. O `re_ancora` reestabelece o cenario pelo traco
# mais reconhecivel + a bandeira, em uma oracao.
CENARIOS = [
    {"id": "cozinha_modesta", "bancada": "counter", "curto": "kitchen",
     "set": "a small older American kitchen with laminate counters and a window over the sink, a US flag magnet on the fridge door",
     "re_ancora": "the same small older kitchen, the US flag magnet still on the fridge door",
     "luz": "flat grey daylight from the window over the sink."},
    {"id": "cozinha_ilha", "bancada": "island", "curto": "kitchen",
     "set": "an open-plan American kitchen with a white marble island, a living room out of focus behind her, a small US flag on a stand at the end of the island",
     "re_ancora": "the same open-plan kitchen, the living room out of focus behind her and the small US flag on its stand",
     "luz": "warm even daylight from tall windows frame-left."},
    {"id": "cozinha_fazenda", "bancada": "counter", "curto": "kitchen",
     "set": "an old American farmhouse kitchen with a deep porcelain sink, open shelves and a US flag pinned above the doorway",
     "re_ancora": "the same farmhouse kitchen with the deep porcelain sink and open shelves, the US flag still pinned above the doorway",
     "luz": "soft morning light through the window over the sink."},
    {"id": "cozinha_cabana", "bancada": "counter", "curto": "kitchen",
     "set": "a knotty pine cabin kitchen with a screen door, pine trees outside and a small US flag tacked to the door frame",
     "re_ancora": "the same knotty pine cabin kitchen, pine trees still visible through the screen door and the small US flag tacked to the frame",
     "luz": "green-tinged afternoon light coming through the screen door."},
    {"id": "cozinha_retro", "bancada": "counter", "curto": "kitchen",
     "set": "a nineteen-seventies American kitchen with wood-panelled walls, a round wall clock and a US flag decal on the cabinet door",
     "re_ancora": "the same wood-panelled seventies kitchen, the round wall clock and the US flag decal still on the cabinet door",
     "luz": "warm overhead bulb light with dim daylight from the side."},
    {"id": "trailer", "bancada": "counter", "curto": "kitchen",
     "set": "the narrow galley kitchen of an American mobile home, gingham curtains at a small window and a US flag pinned to the panelling",
     "re_ancora": "the same narrow mobile-home kitchen, gingham curtains at the small window and the US flag still pinned to the panelling",
     "luz": "hard daylight through the small window frame-right."},
    {"id": "escritorio", "bancada": "desk", "curto": "office",
     "set": "a home office with a full wall of books, two framed certificates and a US flag on a floor stand in the corner",
     "re_ancora": "the same home office, the wall of books and the two framed certificates behind her and the US flag on its floor stand in the corner",
     "luz": "warm lamp light with soft daylight from a window frame-left."},
    {"id": "alpendre", "bancada": "table", "curto": "porch",
     "set": "a screened American back porch with a wooden table, a ceiling fan and a US flag hanging from a bracket on the post",
     "re_ancora": "the same screened back porch, the ceiling fan overhead and the US flag still hanging from its bracket on the post",
     "luz": "bright shaded daylight coming through the screens."},
    {"id": "garagem", "bancada": "workbench", "curto": "garage",
     "set": "a home garage workbench with a pegboard of tools behind, a rolling chest and a US flag hung flat on the pegboard",
     "re_ancora": "the same home garage, the pegboard of tools behind her and the US flag still hung flat on it",
     "luz": "cool fluorescent strip light overhead."},
    {"id": "copa_igreja", "bancada": "counter", "curto": "hall",
     "set": "a plain community hall kitchen with a stainless counter, a stack of folding chairs behind and a small US flag on the pass-through window",
     "re_ancora": "the same community hall kitchen, the stack of folding chairs behind her and the small US flag still on the pass-through window",
     "luz": "even overhead fluorescent light."},
    {"id": "varanda_sol", "bancada": "wicker table", "curto": "sunroom",
     "set": "a bright sunroom with wicker furniture, potted plants and a US flag on a short pole by the sliding door",
     "re_ancora": "the same bright sunroom, the potted plants and the US flag on its short pole by the sliding door",
     "luz": "flooding daylight from three glass walls."},
    {"id": "lavanderia", "bancada": "folding counter", "curto": "laundry room",
     "set": "an American laundry room with a folding counter over the machines, a wire rack of towels and a US flag sticker on the dryer",
     "re_ancora": "the same laundry room, the wire rack of towels behind her and the US flag sticker still on the dryer",
     "luz": "warm ceiling light and no daylight."},
    {"id": "rv", "bancada": "counter", "curto": "galley",
     "set": "the galley of a parked American RV, wood-veneer cabinets, a small sink and a US flag decal beside the window",
     "re_ancora": "the same RV galley, wood-veneer cabinets and the US flag decal still beside the window",
     "luz": "warm afternoon light through the RV window frame-right."},
    {"id": "cozinha_moderna", "bancada": "island", "curto": "kitchen",
     "set": "a modern American kitchen with matte black cabinets and a subway-tile wall, a small US flag in a pen cup beside the toaster",
     "re_ancora": "the same matte black kitchen with the subway-tile wall, the small US flag still in the pen cup beside the toaster",
     "luz": "cool even daylight from frame-right."},
]

# TR7/TR16 — o RECIBO. Tres itens, nunca citados na fala: e' o que da' lastro ao
# "full recipe". O campo `cabecas` existe para o linter varrer a copy e para o
# sorteio EVITAR a colisao por construcao (ver `_bancada_livre`): com
# substancia=ginger, uma bancada de gengibre poria na boca o que a imagem tinha
# de esconder. ⛔ Zero marca legivel — forma no lugar de rotulo.
BANCADAS = [
    {"id": "po_gengibre", "cabecas": ("ginger",),
     "itens": "a plain glass jar of fine white powder, a knob of fresh ginger root and a wooden spoon"},
    {"id": "limao_sal", "cabecas": ("lemon", "salt"),
     "itens": "a rustic ceramic bowl, a halved lemon face-up and a small dish of coarse salt"},
    {"id": "canela_ambar", "cabecas": ("cinnamon",),
     "itens": "an unlabelled amber bottle, three cinnamon sticks tied with twine and a shallow saucer"},
    {"id": "melaco_sementes", "cabecas": ("syrup", "molasses"),
     "itens": "a stoneware crock of dark syrup with the lid tipped beside it, a paring knife and a scatter of black seeds"},
    {"id": "nozes_nozmoscada", "cabecas": ("walnut", "nutmeg"),
     "itens": "a small white bowl of shelled walnuts, a whole nutmeg on a wooden board and a folded cloth"},
    {"id": "folhas_coador", "cabecas": (),
     "itens": "a wide-mouth jar of dried leaves, a metal strainer and a chipped enamel mug"},
    {"id": "pilao_beterraba", "cabecas": ("beetroot",),
     "itens": "a wooden mortar and pestle with something ground pale inside, a cut beetroot and a folded paper packet"},
    {"id": "jarra_alho", "cabecas": ("garlic",),
     "itens": "a glass measuring jug half full of clear liquid, a whole head of garlic and a long-handled spoon"},
    {"id": "figos_lata", "cabecas": ("fig",),
     "itens": "a saucer of dried figs, a squat unlabelled tin with the lid resting on it and a wooden scoop"},
    {"id": "salsa_conta_gotas", "cabecas": ("parsley",),
     "itens": "a bundle of fresh parsley tied at the stems, a small brown bottle with a dropper and a china teacup"},
    {"id": "aveia_casca", "cabecas": ("oat", "cinnamon"),
     "itens": "a shallow bowl of raw oats, a stick of cinnamon bark and a slotted metal spoon"},
    {"id": "raiz_graos", "cabecas": ("ginger",),
     "itens": "a whole ginger root, a jar of coarse dark grains with no label and a wooden butter knife"},
]

# ⭐ TR1 — a peca que SOBE na troca. Ela ja' estava plantada na bancada desde o
# frame 1; o "reveal" nao apresenta nada novo. `plantado` e' a aparencia
# (o que o gerador desenha), `curto` e' a referencia de continuidade (o que
# volta na mao, e o que entra na travada TR_TROCA_*).
# ⚠️ O mecanismo NAO e' eixo sorteavel de substancia: e' gelatina nas dez
# variantes. Congruencia inviolavel — o mecanismo do criativo e' o que a VSL
# vende. Eles trocam entre Vicks, mel e azeite; nos nao.
# ⚠️ `pousado` e' o detalhe forense POR MECANISMO. A travada nasceu do v01/v03,
# onde o mecanismo era pote COM TAMPA — e o motor a aplicava aos dez, mandando
# desenhar "its lid lying face-up" em tigela, pires, sache, copo e panela (7 dos
# 10, 48% dos IMAGE 02). Contradicao dentro do mesmo bloco, e a tampa e'
# justamente a prova de que a peca estava plantada.
MECANISMOS_PROP = [
    {"id": "tigela_cubos",
     "plantado": "a shallow white bowl of firm amber gelatin cut into cubes, each cube wobbling slightly",
     "curto": "the shallow white bowl of amber gelatin cubes",
     "pousado": "uncovered, its serving spoon lying on the board beside it"},
    {"id": "pote_firme",
     "plantado": "a clear glass jar of gelatin already set firm and amber",
     "curto": "the glass jar of set amber gelatin",
     "pousado": "already open, its lid lying face-up on the board beside it"},
    {"id": "sache_aberto",
     "plantado": "a plain white sachet of pale powder torn open at the top, standing upright",
     "curto": "the torn-open white sachet of pale powder",
     "pousado": "already torn, its foil top lying flat on the board beside it"},
    {"id": "mason_po",
     "plantado": "a wide-mouth mason jar half full of pale gelatin powder",
     "curto": "the mason jar of pale gelatin powder",
     "pousado": "already open, its lid lying face-up on the board beside it"},
    {"id": "copo_mexido",
     "plantado": "a glass tumbler of cold water with the gelatin already stirred through it, still turning",
     "curto": "the glass tumbler of cold water with the gelatin stirred through it",
     "pousado": "already stirred, the wet spoon lying on the board beside it"},
    {"id": "panela_morna",
     "plantado": "a small enamel saucepan of warm amber gelatin with a spoon standing in it",
     "curto": "the enamel saucepan of warm amber gelatin",
     "pousado": "already open, its lid lying face-up on the board beside it"},
    {"id": "pires_cubos",
     "plantado": "three firm amber gelatin cubes stacked on a small white saucer",
     "curto": "the saucer of stacked amber gelatin cubes",
     "pousado": "uncovered, the emptied mould lying on the board beside it"},
    {"id": "tigela_lisa",
     "plantado": "a plain glass bowl of gelatin set firm, the surface catching the light in one flat sheet",
     "curto": "the glass bowl of firm-set gelatin",
     "pousado": "uncovered, the mixing spoon lying on the board beside it"},
    {"id": "granulos",
     "plantado": "a squat unlabelled jar of pale gelatin granules with a wooden scoop lying beside it",
     "curto": "the unlabelled jar of pale gelatin granules",
     "pousado": "already open, its lid lying face-up on the board beside it"},
    {"id": "copo_sache",
     "plantado": "a tall glass of cold water with a torn white sachet lying flat beside it",
     "curto": "the tall glass of cold water with the torn white sachet beside it",
     "pousado": "already poured, the wet spoon lying on the board beside it"},
]


# ---------------------------------------------------------------------------
# COPY — cena 1: A CRENDICE (crendice + desmentido)
# ---------------------------------------------------------------------------
# TR8. O agente roda a variante DESMENTE, e por razao ESTRUTURAL, nao por
# numero: as duas variantes da fonte convertem na mesma faixa (11K-30K), mas
# (a) DESMENTE e' exatamente o arco do SUBSTANCIA_ABSURDA — o absurdo e' a
# porta, o mecanismo real e' a chave — e (b) em 3 cenas e' o desmentido que
# ABRE BURACO para a cena 2 ter o que batizar. Sem ele a TROCA nao tem contra
# o que acontecer.
#
# ⚠️ A ESCADA DA PROMESSA E' DECISAO DO ED (§5c do mapa, TR8: "a escolha do
# degrau e' do Ed — alcada"). O pool vem MISTURADO por padrao, mas agora cada
# entrada declara o seu `degrau` e existe o filtro `--degrau` — antes o motor
# sorteava por conta propria o que a doutrina reservou ao operador, e o operador
# nao tinha como exercer a escolha sem editar codigo.
#   · assertiva ..... degrau 1, risco 🟡 (a forma da fonte, 7/8)
#   · condicional ... degrau 2, a UNICA validada em producao
#   · testemunho .... prova social de terceiro
#   · resistencia ... a familia do v01 ("last all night long"), sem numero
# ⛔ Nenhuma com PRAZO — foi o token que derrubou o NECROSE ("by next month").
# ⛔ Nenhuma com `from this to this`: e' deitico, e neste formato o prop nao
#    cresce (TR2), entao a imagem nao entrega os dois estados.
# ⚠️ TODAS falam do corpo do ESPECTADOR (`your {o}`). Cinco entradas usavam
# `his {o}`/`their {o}` — 29% dos lotes — e sem o `your` a promessa deixa de ser
# enderecada e o hook vira fofoca sobre terceiros. `your Johnson` e' justamente
# o que transfere o proxy para o corpo do espectador (invariante 8/28, 8/8 na
# fonte), e a TR3 cobra isso com todas as letras.
# ⚠️ Numeros por extenso: o Veo soletra algarismo.
# ⚠️ `ten times bigger` concentra 7 das 18 entradas. E' TRAVAMENTO DELIBERADO:
# a fonte usa a mesma promessa em 7 dos 8 reels. Diluir seria escolher copy no
# lugar do Ed — se ele quiser diluir, e' entrada de pool, nao regra.
CRENDICES = [
    {"degrau": "assertiva",
     "txt": "Rub {s} on your {o} and it's gonna get ten times bigger."},
    {"degrau": "condicional",
     "txt": "If you want your {o} ten times bigger, rub {s} on it tonight."},
    {"degrau": "testemunho",
     "txt": "They all say {s} on your {o} makes it twice the size."},
    {"degrau": "testemunho",
     "txt": "Every man on this app swears {s} on your {o} is worth three inches."},
    {"degrau": "assertiva",
     "txt": "Put {s} on your {o} tonight and it doubles. The internet swears by it."},
    {"degrau": "assertiva",
     "txt": "One spoon of {s} on your {o} and you grow a full inch."},
    {"degrau": "testemunho",
     "txt": "My cousin swears {s} on your {o} takes you from four to eight."},
    {"degrau": "resistencia",
     "txt": "Rub {s} into your {o} every night and it never quits on you."},
    {"degrau": "assertiva",
     "txt": "The whole internet says {s} on your {o} makes it ten times bigger."},
    {"degrau": "resistencia",
     "txt": "Coat your {o} in {s} and it comes out a different animal."},
    {"degrau": "assertiva",
     "txt": "Two fingers of {s}, straight onto your {o}, and it grows ten times."},
    {"degrau": "testemunho",
     "txt": "Guys everywhere swear {s} on your {o} adds a couple of inches."},
    {"degrau": "condicional",
     "txt": "Want your {o} ten times bigger? Then rub {s} straight on it tonight."},
    {"degrau": "resistencia",
     "txt": "A spoonful of {s} on your {o} beats every pill on the shelf."},
    {"degrau": "assertiva",
     "txt": "A little {s} on your {o}. That's the whole thing. Ten times bigger."},
    {"degrau": "testemunho",
     "txt": "Everybody says the same thing: {s} on your {o}, double the size."},
    {"degrau": "assertiva",
     "txt": "Rub {s} on your {o} — ten times bigger, that's the claim they make."},
    {"degrau": "testemunho",
     "txt": "Half this country swears {s} on your {o} is worth two whole inches."},
]

DEGRAUS = ("assertiva", "condicional", "testemunho", "resistencia")

# O desmentido e' BEAT PROPRIO (TR8), curto, colado na crendice. E' ele que
# transforma o comando absurdo em pergunta — e a pergunta e' o buraco onde a
# cena 2 encaixa o batismo.
# ⚠️ Piso de 5 palavras em cada um: com desmentidos de 3 palavras a cena 1 caia
# abaixo do piso de 16 da TR14.
DESMENTIDOS = [
    "You don't believe that works, right?",
    "Yeah. Nobody actually believes that one.",
    "Course it doesn't work. Never did.",
    "You know that's nonsense, right?",
    "Look at your face. Exactly that.",
    "It doesn't. Not one bit.",
    "You're not buying that. Good.",
    "Nope. Never worked for anybody, ever.",
    "And you already know better.",
    "Sounds insane, because it is.",
    "Right? Total garbage, every word.",
    "Doesn't work. You know it.",
]

# ---------------------------------------------------------------------------
# COPY — cena 2: A TROCA (fundida + prova)
# ---------------------------------------------------------------------------
# ⛔ TR9 — TODA fundida carrega o literal minusculo `gelatin trick`. Ele mora
# em cenas diferentes em cada agente e TODAS caem no colapso de 5 para 3; sem
# ele o criativo deixa de ser congruente com o que a VSL vende, que e' regra
# inviolavel e nao preferencia. O linter trava nisso duas vezes: no corpo das
# tres falas (lint_curto, parametro `literais`) e na CENA 2 especificamente
# (TR3), porque e' no ponto da troca que o pivo precisa ganhar nome.
#
# ⚠️ TODO template precisa do slot `{o}`: o CTA nao nomeia o orgao, entao a
# cena 2 e' a unica companhia da cena 1 na cota 2/3. Um unico item sem `{o}`
# derrubou 48 de 300 sorteios no port anterior (RUNBOOK §As travas do SHORT).
# ⚠️ A entrada 3 chegou do operador SEM o slot — terminava em "and the blood
# flow comes back". Duas palavras entraram ("to your {o}") pelo mesmo motivo e
# com o mesmo precedente do organicwave_short ("mine" -> "my {o}"), e o
# operador foi avisado na entrega. Nada mais no pool foi tocado.
# ⚠️ CLAIM SOBRE O CORPO DO ESPECTADOR: CONDICIONA, NAO AFIRMA.
# Quatro entradas diziam `it puts the blood back in your {o}` / `the blood flow
# reaches your {o} again` / `it's the blood flow your {o} is missing` — isso e'
# DIAGNOSTICO do corpo de quem assiste, que somado a uma prova com PRAZO na
# mesma cena reproduz exatamente a linha que derrubou o video do NECROSE
# ("Your manhood looks like this right now. It can look like this by next
# month" — politicas contra geracao de conteudo nocivo). A tabela da propria
# licao manda condicionar ou passar para a terceira pessoa; a condicional vende
# o mesmo desejo sem ATESTAR o estado do corpo do espectador.
# O `_tr_claim_prazo` cobra isso, e o `_montar_falas` re-sorteia a prova para
# nunca empilhar 2a pessoa + prazo no mesmo take de 8s.
#
# ⚠️ `voz` casa a fala com a RELACAO sorteada na cena 3. Antes as duas eram
# sorteadas independentes e 13% dos lotes diziam `my husband's {o}` num IMAGE 03
# que nomeava a narradora como a vizinha ou a mulher que faz as compras — e a
# relacao nomeada e' a alavanca 2 do protocolo de recusa: contradize-la na fala
# a anula.
FUNDIDAS = [
    {"voz": "neutra",
     "txt": "Forget that. This is what actually works — gelatin. That's the gelatin trick, and if you want the blood back in your {o}, that's the one."},
    {"voz": "neutra",
     "txt": "Drop that. Pick this up. Gelatin in cold water, every single night — they call it the gelatin trick, and your {o} remembers."},
    {"voz": "neutra",
     "txt": "That never worked on anybody. This did. A spoon of gelatin, stirred cold — the gelatin trick — and the blood flow came back to his {o}."},
    {"voz": "conjugal",
     "txt": "It was never {s}. It's blood flow, choked off, and gelatin opens it. That's the gelatin trick, and my husband's {o} came back."},
    {"voz": "neutra",
     "txt": "Set that down. This one's real: gelatin, stirred into cold water. The gelatin trick. Nineteen days and his {o} was back for good."},
    {"voz": "neutra",
     "txt": "Nobody's {o} ever got bigger from {s}. They got bigger from gelatin. That's the gelatin trick, and it costs two dollars a box."},
    {"voz": "neutra",
     "txt": "Put that down. Gelatin. Cold water, one spoon, before bed — the gelatin trick — and if blood flow is what your {o} lost, that's the one."},
    {"voz": "neutra",
     "txt": "My aunt handed me this instead. Gelatin, stirred cold. The gelatin trick. Three weeks later his {o} had not quit once."},
    {"voz": "neutra",
     "txt": "Wrong jar. This one. Gelatin in warm water, stirred until it's gone. They call it the gelatin trick, and his {o} answers now."},
    {"voz": "neutra",
     "txt": "That jar goes down. This one comes up. Gelatin — the gelatin trick — and the blood flow his {o} lost is running again."},
    {"voz": "neutra",
     "txt": "Doctors never say blood flow. Gelatin does the job {s} never could. That's the gelatin trick, and his {o} proved it in weeks."},
    {"voz": "conjugal",
     "txt": "Trade it. One spoon of gelatin, cold water, nightly. The gelatin trick, and his {o} stopped quitting on us months ago."},
    {"voz": "neutra",
     "txt": "Off the counter, into the trash. Gelatin is the one — the gelatin trick — and if blood flow is what your {o} is missing, start there."},
    {"voz": "neutra",
     "txt": "Same hand, different jar. Gelatin, stirred into cold water before bed. The gelatin trick. His {o} has not quit since March."},
    {"voz": "neutra",
     "txt": "This goes down, this comes up. Gelatin. Cold water, one spoon — the gelatin trick — and if your {o} needs the blood flow, that's it."},
]

# ⛔ ZERO DEIXIS A PESSOA. Cinco provas eram `He's standing right here.` / `Look
# at him.` / `That's him. Not a photo.` / `Ask him yourself.` / `Right there.
# That's the proof.` — 40% dos lotes mandavam olhar para um homem que o proprio
# IMAGE 02 declara ausente (`She is the only person in the frame`, elenco 1/1/2
# da TR13). Deixis e' a 4a forma de vago que a TR3 bane, e reprova o teste do
# radio do checklist.
PROVAS = [
    "Nineteen days, start to finish.",
    "Nineteen days on a man I know.",
    "He'll tell you if you ask him.",
    "Two dollars a box, that's all.",
    "He'll tell you the same thing.",
    "Three weeks, every single night.",
    "I watched the whole thing happen.",
    "No photo, no filter, no story.",
    "No pills, nothing else, just that.",
    "Same man, nineteen days later.",
    "He didn't believe it either. You won't.",
    "Not a story. You can check it.",
]

# ---------------------------------------------------------------------------
# COPY — cena 3: O CORPO-PROVA + CTA (barreira + cta + gate)
# ---------------------------------------------------------------------------
# ⚠️ Piso de 5 palavras: com barreiras de 4 a cena 3 caia abaixo do piso de 20
# da TR14.
BARREIRAS = [
    "Two dollars at any store.",
    "Nobody in your house knows.",
    "No prescription, no doctor, no waiting.",
    "It's in the baking aisle.",
    "Takes thirty seconds a night.",
    "You already have the glass.",
    "No pills, no appointment, no questions.",
    "Cheaper than a single refill.",
    "He never knew I did it.",
    "Grocery store, bottom shelf, about four dollars.",
    "Nothing to swallow but water.",
    "No one has to know.",
]

# ⛔ Keyword travada em `gelatin`, minuscula e SEGUIDA DE VIRGULA dentro do
# Dialogue — duas falhas pagas: `GLATN` (caixa alta faz o Veo soletrar) e
# `gelatine` (sem a micro-pausa o TTS emenda).
# ⛔ `BOOK` e `YES` proibidos: quebram a automacao Comentario->DM. ⚠️ O reel de
# 82K usa literalmente `book` — copiar a ARQUITETURA, nunca a palavra.
# ⭐ A fonte prova de fora que a keyword mais forte e' o NOME DO MECANISMO, e o
# nosso `gelatin trick` ja' e' isso: a adaptacao e' 1:1 e custa zero.
# ⚠️ ENTROPIA DE FORMA, nao so' de contagem: 16 das 18 entradas abriam com o
# mesmo prefixo de 4 palavras (`Comment gelatin, and I'll`) e 13 com o de 5 —
# o --stats contava 18 e a variacao percebida era 3. Sete entradas passaram a
# levar a keyword em outra posicao. ⛔ A forma da keyword nao muda: `gelatin`
# minusculo, seguido de virgula.
CTAS = [
    "Comment gelatin, and I'll send you the whole recipe tonight.",
    "Comment gelatin, and it's in your inbox in ten minutes.",
    "Comment gelatin, and I'll send you exactly what to buy.",
    "The recipe's yours — comment gelatin, and it goes out tonight.",
    "Comment gelatin, and I'll tell you how much and when.",
    "Comment gelatin, and I'll send you the full recipe.",
    "One word in the comments: gelatin, and it's yours tonight.",
    "Comment gelatin, and you'll have it before he gets home.",
    "Type gelatin, in the comments and I'll send the measurements.",
    "Comment gelatin, and I'll send the whole thing, free.",
    "Say the word — gelatin, in the comments — and it's sent.",
    "Comment gelatin, and I'll send the recipe my aunt sent me.",
    "Comment gelatin, and I'll send you all four ingredients.",
    "Want it? Comment gelatin, and I'll message you tonight.",
    "Comment gelatin, and I'll send it before you scroll away.",
    "It's four lines long. Comment gelatin, and I'll send it.",
    "Comment gelatin, and I'll send you where to get it.",
    "Just the word gelatin, in the comments. That's the whole ask.",
]

# ⛔ TR5 — REGRA DE POOL, medida pelo operador: "brother" caia em 31-73% dos
# videos. No maximo DUAS entradas com "brother", e a MAIORIA sem vocativo
# nenhum. E o que varia nao e' so' o vocativo: varia o MOTIVO do gate (a
# plataforma bloqueia · a fila de comentarios · o feed some amanha · o
# algoritmo esconde). O self-test do --stats reprova se a proporcao escorregar.
# ⛔ Zero nome de plataforma na `Dialogue:` — a ultima entrada dizia "or Facebook
# eats the message", e a variante limpa ja' existia duas linhas acima. Nomear a
# plataforma e' P12 e nao custa nada evitar.
GATES = [
    "Follow first, or my message never lands.",
    "Hit follow, or the app blocks me.",
    "I can only message people who follow.",
    "Followers get answered first. Everyone else waits.",
    "One tap on follow. That's the whole gate.",
    "Follow me, brother, or this never arrives.",
    "Without the follow my inbox stays shut.",
    "Three hundred comments tonight. Followers go first.",
    "Follow tonight — tomorrow this leaves your feed.",
    "Follow me, my friend. Then I can answer.",
    "The algorithm hides me from non-followers.",
    "Follow first. That's how my inbox opens.",
    "I answer followers. Everyone else has to wait.",
    "Tap follow, or the app eats the message.",
]

VOCATIVOS = ("brother", "my friend", "guys", "buddy", "man", "girls")


# ---------------------------------------------------------------------------
# TABELAS DE TOKEN BANIDO (o linter compartilhado le' estas)
# ---------------------------------------------------------------------------
# ⚠️ Direcao de cena, nunca fala. A crendice DIZ "it doubles" e "ten times
# bigger" — a promessa verbal e' o produto. O que nao pode e' a DIRECAO mandar
# o prop crescer, porque [D4] diz que nada muda em quadro.
BANIDOS_TAKE = {
    "stiffens": "estado mudando no TAKE — [D4] o prop e' imovel",
    "swells": "idem", "grows": "idem", "rises": "idem",
    "expands": "idem", "doubles": "idem", "lengthens": "idem",
    "erect": "vocabulario de estado na direcao de cena",
    "pulse": "nomear o eixo ja' basta para o filtro; negar nao protege",
}
BANIDOS_IMAGE = {
    "engorged": "adjetivo de estado no IMAGE",
    "veins": "detalhe anatomico no prop",
    "throbbing": "idem",
}
# ⛔ substring, em qualquer bloco. `the victim`/`the narrator` sao ordem do
# operador: `victim` e' palavra que SIGNIFICA dano — rotular a cena assim
# entrega municao de graca. Descrever a pessoa, ou nomear a relacao.
BANIDOS_GLOBAL = {
    "morph": "[D4] nada se transforma em quadro",
    "time-lapse": "idem", "before and after": "idem",
    "transforms": "idem", "vfx": "idem",
    "the victim": "rotulo que significa dano — descrever a pessoa",
    "the narrator": "idem — ou nomear a relacao",
}
BANIDOS_CTA = {
    "book": "quebra a automacao Comentario->DM (e e' a palavra do reel de 82K)",
    "yes": "idem",
    "link": "CTA e' comentario, nao link",
}

# ⛔ TR12 — o unico ⛔ da doutrina que nao tinha tabela no motor. A divergencia
# de figurino [D3] e' 🟡 e deliberada, mas o guardrail que sobrou dela (zero
# vocabulario de desejo) estava valendo so' na honra: os pools estao limpos hoje
# e nada impedia a proxima edicao de pool de sujar.
BANIDOS_DESEJO = {
    "sexy": "vocabulario de desejo — a roupa entra como PECA descrita",
    "seductive": "idem", "sultry": "idem", "curvy": "idem",
    "revealing": "idem", "cleavage": "idem", "lingerie": "idem",
    "provocative": "idem", "alluring": "idem", "flirty": "idem",
}


# ---------------------------------------------------------------------------
# SORTEIO
# ---------------------------------------------------------------------------

def _palavras(txt):
    """Contrato do linter compartilhado: palavra e' letra, apostrofo e hifen."""
    return len(re.findall(r"[A-Za-z'\-]+", txt))


_UNI = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen"]
_DEZ = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty",
        7: "seventy", 8: "eighty", 9: "ninety"}


def _por_extenso(n):
    """Numero escrito, nunca concatenado.

    ⚠️ Ja' saiu "Sixty-1 years old" e "Thirty-4" em producao por concatenar
    prefixo com algarismo. Numero na copy se ESCREVE.
    """
    if n < 20:
        return _UNI[n]
    d, u = divmod(n, 10)
    return _DEZ[d] + ("-" + _UNI[u] if u else "")


def _sem_artigo(txt):
    """Tira o artigo inicial de um item de pool.

    A travada diz "The %s has been standing open..." e os itens do pool nascem
    com artigo proprio. O motor ajusta o SLOT; ⛔ a travada nao se reescreve.
    """
    for art in ("the ", "a ", "an "):
        if txt.lower().startswith(art):
            return txt[len(art):]
    return txt


def _peca(calca):
    """A peca de roupa nua, sem oracao subordinada.

    Hoje as 24 calcas ja' nascem nuas (a oracao do bolso saiu junto com a
    ancora reescrita), entao isto e' GUARDA, nao transformacao: se alguem
    acrescentar 'khaki shorts with a deep side pocket' a um pool, a travada da
    F12b nao sai como 'beside the lap of his khaki shorts with a deep side
    pocket'. ⛔ O substantivo da ancora e' `lap`, nunca `pocket`.
    """
    return calca.split(" with ")[0]


# TR10 — a relacao NOMEADA e' a alavanca 2 do protocolo de recusa, e ela e'
# obrigatoria aqui. ⛔ `the victim`/`the narrator` sao proibidos: descrever a
# pessoa ou nomear o vinculo.
# ⚠️ E a relacao tem de ser FISICAMENTE POSSIVEL com as idades sorteadas — o
# exemplo do operador e' `his wife of thirty-one years`, mas com narradora de
# 28 e corpo-prova de 60 trinta e um anos de casamento nao fecham. Entao o
# numero se calcula (uniao a partir dos 20 anos do mais novo), e quando nem
# isso fecha cai-se em vinculo SEM numero. ⛔ Omitir a relacao nao e' opcao.
# ⛔ `his daughter-in-law` FOI REMOVIDA. Nao esta' em lugar nenhum da doutrina
# (que nomeia `his wife of thirty-one years`, `her neighbor of twenty-six
# years` e `the man she cooks for`): o motor inventou o vinculo, e inventou
# justamente o pior possivel para esta composicao — leitura sexual
# intrafamiliar em cima da geometria que ja' custou 4 recusas deterministicas.
# Se o Ed quiser a nora, e' ordem dele e volta como entrada de pool.
RELACOES_SEM_NUMERO = [
    "the woman who cooks for him",
    "the woman from the house next door",
    "the woman who does his shopping",
]

# a familia de voz que cada relacao autoriza na fala da cena 2 (ver FUNDIDAS):
# so' a esposa pode dizer `my husband's {o}` / `stopped quitting on us`.
VOZES_CONJUGAIS = ("his wife of",)


def voz_da_relacao(relacao):
    return "conjugal" if relacao.startswith(VOZES_CONJUGAIS) else "terceiro"


def _relacao(rng, idade_m, idade_h):
    # uniao a partir dos 20 anos do mais novo dos dois — e' o piso que faz a
    # aritmetica fechar em qualquer combinacao sorteada
    anos = min(idade_m, idade_h) - 20
    op = list(RELACOES_SEM_NUMERO)
    if anos >= 15:
        # peso 2 na esposa: e' a formulacao do operador (`his wife of
        # thirty-one years`), e e' a que carrega mais vinculo
        op += ["his wife of %s years" % _por_extenso(anos)] * 2
        op.append("his neighbor of %s years" % _por_extenso(anos))
    elif anos >= 8:
        op.append("his neighbor of %s years" % _por_extenso(anos))
    return rng.choice(op)


def _carregar_ledger():
    if os.path.exists(LEDGER):
        with open(LEDGER, encoding="utf-8-sig") as f:
            return json.load(f)
    return {}


def _anotar(ledger, spec):
    """Anota o sorteio no ledger EM MEMORIA, sem tocar no arquivo.

    ⚠️ Existe separado do `_gravar_ledger` por causa do `--dry-run`: sem isto,
    os N videos de um mesmo lote sao sorteados todos contra o mesmo historico
    e o `_evitando()` nao ve' o irmao que acabou de sair — `--n 2` devolvia a
    mesma narradora nos dois. O ensaio nao grava, mas tem de se lembrar de si.
    """
    p = ledger.setdefault(spec["pagina"], {})
    for eixo in ("narradora", "corpo_prova", "cenario", "proxy", "substancia",
                 "textura", "mecanismo", "bancada"):
        p.setdefault(eixo, []).append(spec[eixo]["id"])
        p[eixo] = p[eixo][-12:]


def _gravar_ledger(ledger, spec):
    _anotar(ledger, spec)
    with open(LEDGER, "w", encoding="utf-8") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)


def _evitando(rng, pool, recentes):
    livres = [x for x in pool if (x.get("id") if isinstance(x, dict) else x) not in recentes]
    return rng.choice(livres if livres else pool)


def _cita(corpo, cabeca):
    """A palavra-cabeca de um item de bancada aparece na copy? (singular ou
    plural — 'fig' tem de pegar 'figs')."""
    return re.search(r"\b%ss?\b" % re.escape(cabeca), corpo, re.I) is not None


_PALAVRA_CHEIA = re.compile(r"[a-z]{3,}")
_VAZIAS = frozenset((
    "the", "and", "with", "for", "its", "beside", "half", "into", "full",
    "resting", "lying", "standing", "across", "rim", "top", "open", "small",
    "large", "long", "wide", "deep", "plain", "whole", "three", "two", "one",
    "something", "inside", "there", "them", "that", "this", "from", "under",
))


def _pares(txt):
    """Pares de palavras de conteudo adjacentes ('rustic ceramic', 'glass jar').

    Serve para dizer se dois itens de cenario desenham O MESMO OBJETO.
    """
    p = [w for w in _PALAVRA_CHEIA.findall(txt.lower()) if w not in _VAZIAS]
    return set(zip(p, p[1:]))


def _bancada_livre(rng, falas, recentes, sub=None):
    """TR19 — O RECIBO E' MUDO **E NAO REPETE O POTE**, por construcao em vez de
    checado depois (RUNBOOK §Regra de contraste).

    Duas colisoes, nao uma:
    · com a FALA — com substancia=ginger a boca diz "ginger" na cena 1, e as
      duas bancadas de gengibre poriam na imagem justamente o que a fala ja'
      citou. O "full recipe" so' tem lastro se a boca citar UM e a imagem
      mostrar TRES.
    · com o POTE da substancia — 11 dos 168 pares desenhavam o mesmo objeto
      duas vezes no mesmo quadro ("a plain glass jar of fine white powder" no
      pote E na bancada; "a rustic ceramic bowl" nos dois). Recibo que repete o
      pote nao mostra tres ingredientes, mostra dois.
    """
    corpo = " ".join(falas)
    livres = [b for b in BANCADAS
              if not any(_cita(corpo, c) for c in b["cabecas"])]
    if sub:
        pote = _pares(sub["pote"])
        sem_eco = [b for b in livres if not (_pares(b["itens"]) & pote)]
        livres = sem_eco or livres
    return _evitando(rng, livres if livres else BANCADAS, recentes)


# ⚠️ TR8/licoes-producao-veo: 2a pessoa + PRAZO no mesmo take de 8s e' a
# composicao que derrubou o video do NECROSE. A fundida ja' esta' condicionada,
# mas a prova pode trazer o prazo — entao a prova se re-sorteia, por construcao.
# ⚠️ Decide a familia da promessa da cena 1 (ver _gatilho_reacao). Precisa casar
# tanto o numeral quanto a promessa de MULTIPLO escrita sem numero — "it
# doubles" e "twice the size" sao numericas para o espectador, e a reacao dela
# tem de cair ali. Sem "double|twice", uma crendice de multiplo receberia o
# gatilho de resistencia e a cara dela sincronizaria no lugar errado.
# o pedaco de TR_SEM_CRESCIMENTO que nao depende de slot — e' por ele que o
# linter confere a imobilidade (ver _tr_sem_crescimento).
TR2_MIOLO = "completely motionless for the entire shot"

TR8_NUMERO = re.compile(
    r"\d|\b(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|"
    r"twenty|thirty|forty|fifty|sixty|double|doubles|doubled|twice|half|"
    r"inch|inches)\b", re.I)

TR8_PRAZO = re.compile(r"\b(\w+\s+(?:days?|weeks?|months?))\b|\bsince\s+[A-Z]",
                       re.I)
TR8_CORPO_2A = re.compile(
    r"\byour\s+(?:\w+\s+){0,2}(%s)\b" % "|".join(NUCLEO), re.I)

# ecos de FATO dentro do mesmo video ("two dollars" ditos duas vezes em 24s).
ECOS = ("two dollars", "nineteen days", "three weeks", "four dollars")

# P22 — "cada cena aterrissa em 2a pessoa OU IMPERATIVO" (checklist da
# doutrina). O imperativo conta: `Set that down.` fala com o espectador tanto
# quanto `your {o}`. Sem esta lista a regra reprovaria metade das fundidas por
# um criterio que a propria doutrina nao usa.
P22_2A = re.compile(r"\b(you|your|you're|you'll|yours)\b", re.I)
IMPERATIVOS = ("forget", "drop", "pick", "set", "put", "trade", "rub", "coat",
               "want", "look", "hit", "tap", "follow", "comment", "type", "say",
               "off", "grab", "take", "stop", "keep", "just")


def _aterrissa(fala):
    if P22_2A.search(fala):
        return True
    for frase in re.split(r"[.!?:]\s*|\s+—\s+", fala):
        p = re.findall(r"[A-Za-z']+", frase)
        if p and p[0].lower() in IMPERATIVOS:
            return True
    return False


def _eco(*partes):
    corpo = " ".join(partes).lower()
    return any(corpo.count(e) > 1 for e in ECOS)


def _escolher(rng, pool, ok, tentativas=12):
    """Sorteia do pool ate' `ok(item)` — e devolve o ultimo se nao houver saida.

    Nao filtra a lista inteira de proposito: o custo e' o mesmo e o fallback
    mantem o motor sempre entregando um lote, como o `_evitando`.
    """
    esc = rng.choice(pool)
    for _ in range(tentativas):
        if ok(esc):
            return esc
        esc = rng.choice(pool)
    return esc


def _montar_falas(rng, subst, orgaos, relacao, degrau=None):
    """As tres falas, cada uma somando dois ou tres pools.

    ⚠️ TR14: adaptar a fonte aqui e' EXPANDIR ~2,3x, nao comprimir. Uma frase
    por cena — que e' o que os reels de 13s tem — deixaria ar num take de 8s, e
    ar vira pausa morta. Por isso cena 1 = crendice + desmentido, cena 2 =
    fundida + prova, cena 3 = barreira + CTA + gate.

    Tres filtros por construcao, todos com fallback:
    · `degrau` — a escada da promessa e' escolha do Ed (TR8), nao do sorteio
    · voz da fundida × relacao nomeada da cena 3 (TR10)
    · 2a pessoa + prazo na mesma cena 2, e eco de fato dentro do video
    """
    voz = voz_da_relacao(relacao)
    cren_pool = [c for c in CRENDICES if degrau in (None, c["degrau"])] or CRENDICES
    fund_pool = [f for f in FUNDIDAS if f["voz"] in ("neutra", voz)] or FUNDIDAS

    c1 = "%s %s" % (rng.choice(cren_pool)["txt"].format(s=subst["fala"],
                                                        o=orgaos[0]),
                    rng.choice(DESMENTIDOS))

    fund = rng.choice(fund_pool)["txt"].format(s=subst["fala"], o=orgaos[1])
    tem_2a = bool(TR8_CORPO_2A.search(fund))
    falta_p22 = not _aterrissa(fund)
    prova = _escolher(rng, PROVAS,
                      lambda p: not (tem_2a and TR8_PRAZO.search(p))
                      and not _eco(fund, p)
                      and not (falta_p22 and not P22_2A.search(p)))
    c2 = "%s %s" % (fund, prova)

    # ⚠️ o eco e' medido contra o VIDEO INTEIRO, nao so' dentro da cena: a
    # fundida que diz "two dollars a box" e a barreira "Two dollars at any
    # store." estao em cenas diferentes e mesmo assim pagam o mesmo fato duas
    # vezes em 24 segundos.
    barreira = _escolher(rng, BARREIRAS, lambda b: not _eco(c1, c2, b))
    cta = rng.choice(CTAS)
    gate = _escolher(rng, GATES, lambda g: not _eco(c1, c2, barreira, cta, g))
    c3 = "%s %s %s" % (barreira, cta, gate)
    return [c1, c2, c3]


def sortear(pagina, rng, ledger, degrau=None):
    """TR20 — anti-repeticao por ledger, por pagina.

    Os dois eixos de ROSTO evitam os 3 ultimos (rosto repetido e' o que o
    operador ve primeiro no lote); os eixos de cenario e objeto evitam os 2
    ultimos. Combo repetido em videos consecutivos da mesma pagina e' proibido.

    ⚠️ A RELACAO E' SORTEADA ANTES DAS FALAS. Antes as duas saiam independentes
    e 13% dos lotes diziam `my husband's {o}` num IMAGE 03 que nomeava a
    narradora como a vizinha — e a relacao nomeada e' a alavanca 2 do protocolo
    de recusa: contradize-la na fala a anula.
    """
    hist = ledger.get(pagina, {})
    nar = _evitando(rng, NARRADORAS, hist.get("narradora", [])[-3:])
    hom = _evitando(rng, homens_de(pagina), hist.get("corpo_prova", [])[-3:])
    cen = _evitando(rng, CENARIOS, hist.get("cenario", [])[-2:])
    prox = _evitando(rng, PROXIES, hist.get("proxy", [])[-2:])
    sub = _evitando(rng, SUBSTANCIAS, hist.get("substancia", [])[-2:])
    texturas = TEXTURAS if sub.get("fluida", True) else         [x for x in TEXTURAS if not x.get("fluida", True)]
    tex = _evitando(rng, texturas, hist.get("textura", [])[-2:])
    mec = _evitando(rng, MECANISMOS_PROP, hist.get("mecanismo", [])[-2:])

    relacao = _relacao(rng, nar["idade"], hom["idade"])

    # TR6/cota do orgao: tres substantivos DISTINTOS sorteados de uma vez. So'
    # dois entram em fala (o CTA nao nomeia o orgao) — o terceiro fica de
    # reserva para o `nova_fala()` da UI nao repetir o que ja' esta' em cena.
    orgaos = rng.sample(NUCLEO, 3)
    falas = _montar_falas(rng, sub, orgaos, relacao, degrau)
    ban = _bancada_livre(rng, falas, hist.get("bancada", [])[-2:], sub)

    return {"pagina": pagina, "narradora": nar, "corpo_prova": hom,
            "cenario": cen, "proxy": prox, "substancia": sub, "textura": tex,
            "mecanismo": mec, "bancada": ban, "degrau": degrau,
            "relacao": relacao, "falas": falas}


# ---------------------------------------------------------------------------
# GERADOR
# ---------------------------------------------------------------------------
# Formato de entrega, sempre: BLOCO 0 (REF) -> os 3 IMAGE agrupados -> os 3
# TAKE agrupados. ⛔ Nunca intercalar. Destino: AdBatch Vertical 3.

def _gatilho_reacao(fala1):
    """Onde a reacao facial sincroniza — segue a FAMILIA da promessa.

    "On the number" numa crendice da familia de RESISTENCIA (`it never quits on
    you`, `a different animal`, `beats every pill on the shelf` — 25% do pool)
    manda o Veo sincronizar com um numeral que a fala nao tem, e ele escolhe
    sozinho onde.
    """
    return GATILHO_NUMERO if TR8_NUMERO.search(fala1) else GATILHO_PROMESSA


def montar(spec):
    et = ETNIA[spec["pagina"]]
    nar, hom, cen = spec["narradora"], spec["corpo_prova"], spec["cenario"]
    prox, sub, tex = spec["proxy"], spec["substancia"], spec["textura"]
    mec, ban = spec["mecanismo"], spec["bancada"]
    falas = spec["falas"]
    bnc = cen["bancada"]
    luz = cen["luz"][0].upper() + cen["luz"][1:]

    # ⚠️ TR18 — A ANCORA DE CONTINUIDADE AQUI E' INVERTIDA em relacao aos
    # outros agentes: quem repete rosto e' a NARRADORA (ela esta' nas tres
    # cenas), e a descricao volta INTEIRA, com a marca facial. Ancora curta
    # ("same hair") carrega a roupa e perde o rosto — foi assim que o
    # VAZAMENTO devolveu um senhor de oculos e bigode no lugar do corpo-prova.
    # ⛔ E ela nunca leva adjetivo de etnia (TR11/[D2]): ela e' sorteada livre.
    ela = ("a %d-year-old woman with %s, wearing %s"
           % (nar["idade"], nar["marca"], nar["roupa"]))
    mesma = ("The same %d-year-old woman, with %s, wearing %s"
             % (nar["idade"], nar["marca"], nar["roupa"]))
    recibo = TR_BANCADA_RECIBO % (bnc, ban["itens"])
    analogia = ANALOGIAS[prox["analogia"]]
    gatilho = _gatilho_reacao(falas[0])

    b = {}

    # O REF e' a NARRADORA: e' o rosto que precisa se repetir nas tres cenas.
    # O corpo-prova entra novo na cena 3 e nao tem REF — por isso ele leva
    # artigo indefinido la' (TR17).
    b["BLOCO 0 (REF)"] = (
        "REF 01: Photo of a real person, a %d-year-old woman, chest up, facing "
        "the camera directly, calm steady expression. %s. Wearing %s. Plain "
        "neutral gray background, soft even frontal light. No subtitles, no "
        "captions, no burned-in text, no watermark."
        % (nar["idade"], nar["marca"][0].upper() + nar["marca"][1:], nar["roupa"])
    )

    # --- IMAGE 01/03 — A CRENDICE -------------------------------------------
    # Os 6 elementos obrigatorios do hook, todos 8/8 na fonte: ela sozinha com
    # o olhar na lente · o proxy vertical na altura do rosto · a substancia JA'
    # no prop (TR4: a aplicacao nunca e' mostrada, e a procedencia se prova
    # pelo pote aberto com a tampa deitada) · o recibo · o alibi domestico com
    # a bandeira.
    b["IMAGE 01/03"] = (
        "IMAGE 01/03: Medium shot in %s. Standing behind the %s is %s. She "
        "looks straight into the lens. In her left hand: %s, and %s. %s %s A "
        "wooden board lies on the %s in front of her. Standing on the %s since "
        "before the shot began: %s. Also on the %s, open since the first frame: "
        "%s. %s She is the only person in the frame. %s %s"
        % (cen["set"], bnc, ela, prox["img"], tex["desc"] % sub["fala"],
           TR_PROXY_NA_MAO, TR_MAO_LIVRE % sub["fala"],
           bnc, bnc, sub["pote"], bnc, mec["plantado"], recibo, luz, CAUDA)
    )

    # --- IMAGE 02/03 — A TROCA ----------------------------------------------
    # A peca do mecanismo JA' ESTAVA plantada: o reveal nao apresenta nada
    # novo, puxa pro primeiro plano o que estava no cenario (detalhe forense do
    # v01 e do v03 — a tampa continua na bancada depois que o pote sobe).
    # ⚠️ `re_ancora` no lugar de "in the same kitchen": sem ele metade do lote
    # perdia o cenario E a bandeira dos EUA a partir da cena 2.
    # ⚠️ O proxy volta LAMBUZADO (`tex["curta"]`) — invariante 26/28 e item do
    # checklist da doutrina ("o proxy lambuzado FICA em quadro"); antes ele
    # saia limpo de todos os IMAGE depois do primeiro.
    # ⚠️ O mecanismo e' descrito UMA vez (a TR_TROCA_IMAGE ja' o nomeia): a
    # versao anterior punha `mec["plantado"]` e a travada no mesmo bloco.
    b["IMAGE 02/03"] = (
        "IMAGE 02/03: Medium shot at the same %s in %s, same light. %s, stands "
        "behind it talking straight to camera. %s, %s, is still upright in her "
        "left fist beside her cheek. On the %s in front of her, on a wooden "
        "board: %s. %s %s She is the only person in the frame. %s %s"
        % (bnc, cen["re_ancora"], mesma,
           prox["img"][0].upper() + prox["img"][1:], tex["curta"] % sub["fala"],
           bnc, mec["plantado"],
           TR_TROCA_IMAGE % (_sem_artigo(mec["curto"]), bnc, mec["pousado"]),
           recibo, luz, CAUDA)
    )

    # --- IMAGE 03/03 — O CORPO-PROVA ----------------------------------------
    # ⭐ [D1]/TR10 — a F12b. Ele DE PE, neutro, prop grande, na PROPRIA mao;
    # ela aponta SEM ENCOSTAR. O que bloqueia nao e' o prop, e' a agencia — e a
    # agencia se declara tambem pelo OLHAR DELE NA LENTE, nao so' pelo punho.
    # ⚠️ A relacao e' nomeada e a etnia dele e' a da pagina (TR11); a dela
    # continua sem adjetivo nenhum.
    # ⚠️ A ancora de escala e' NO CORPO DELE (`img_dele`): quem segura e' ele.
    # ⛔ Zero plateia: plateia e' FLAGRANTE, e e' um dos quatro ingredientes da
    # composicao que produziu as recusas deterministicas de 2026-07-30.
    # ⚠️ SEM A BANCADA-RECIBO (F12c). Este e' o bloco mais arriscado do lote — a
    # regra de que ele deriva custou 4 recusas deterministicas — e era tambem o
    # mais gordo do repo (230 palavras, 2,3x o IMAGE 01 do proprio FLAGRANTE).
    # 42 dessas palavras eram um recibo que nao serve a beat nenhum da cena 3:
    # o lastro do "full recipe" ja' foi provado nas cenas 1 e 2. Densidade e'
    # superficie de bloqueio, e o que encolhe e' descricao livre, nunca travada.
    # No lugar entra o MECANISMO em uma oracao — a cena que diz "comment
    # gelatin" passa a mostrar gelatina em quadro.
    b["IMAGE 03/03"] = (
        "IMAGE 03/03: Medium shot in %s, same light. %s, stands frame-left; "
        "she is %s. A %d-year-old %s man with %s, in %s and %s, stands beside "
        "her, upright, chin level, his eyes on the lens, saying nothing. %s "
        "Behind them on the %s, still where it was: %s. They are the only two "
        "people in the frame. %s %s %s"
        % (cen["re_ancora"], mesma, spec["relacao"], hom["idade"], et,
           hom["marca"], hom["roupa"], hom["calca"],
           TR_MAO_PROPRIA_IMAGE % (_peca(hom["calca"]),
                                   "%s, the %s still on it"
                                   % (prox["img_dele"], sub["fala"]),
                                   spec["relacao"]),
           bnc, mec["curto"], FRASE_SEM_MARCA, luz, CAUDA)
    )

    # --- TAKE 01/03 ----------------------------------------------------------
    # ⚠️ TR17: o vai-e-vem entra pela travada TR_VAIVEM, que troca o verbo e
    # NOMEIA O GENERO DA IMAGEM — e o genero tem de ser um dominio culinario
    # DIFERENTE do proxy em quadro (campo `analogia`), senao a analogia aponta
    # para dentro da propria cena e nao desambigua nada.
    # ⛔ `strokes`/`pumps`/`grips`/`slides her hand up and down` sao recusa.
    # [D4]: nada cresce; quem paga a promessa e' a cara dela, no frame do
    # numero — e a reacao entra por sobrancelha e olho, nunca por boca ou
    # lingua (risco 4 da §6). O GATILHO segue a familia da promessa sorteada.
    b["TAKE 01/03"] = (
        "TAKE 01/03: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway, no cuts, and the camera does not move. She "
        "talks straight into the lens the whole time. %s %s She is the only "
        "person in the shot.\nDialogue: \"%s\"\nAudio: quiet room tone in the "
        "%s. No music."
        % (TR_VAIVEM % analogia, TR_SEM_CRESCIMENTO % (prox["nome"], gatilho),
           sonorizar(falas[0]), cen["curto"])
    )

    # --- TAKE 02/03 — ⭐⭐ A TROCA -------------------------------------------
    # O agente inteiro esta' aqui. ⛔ Nunca `swap`/`switch`/`replaces`: com o
    # RESULTADO nomeado o Veo troca o objeto cortando. Descreve-se descida,
    # subida e ponto, EM BATIDAS COM SEGUNDOS (TR1) — e o proxy lambuzado FICA
    # em quadro depois de largado, que e' a evidencia residual do resto do take.
    b["TAKE 02/03"] = (
        "TAKE 02/03: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway. The camera does not move and there is no cut "
        "at any point in this shot. %s\nDialogue: \"%s\"\nAudio: quiet room "
        "tone in the %s, one soft knock as something is set down on wood. No "
        "music."
        % (TR_TROCA_TAKE % (prox["nome"], prox["nome"], mec["curto"]),
           sonorizar(falas[1]), cen["curto"])
    )

    # --- TAKE 03/03 ----------------------------------------------------------
    # ⛔ TR13: so' ela tem Dialogue. Ele e' mudo — o dialogo do Veo e'
    # monofonico na pratica e duas vozes saem tortas.
    b["TAKE 03/03"] = (
        "TAKE 03/03: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway, no cuts, and the camera does not move. %s "
        "She speaks straight into the lens, calm and even, no rush. Only she "
        "speaks.\nDialogue: \"%s\"\nAudio: quiet room tone in the %s. No music."
        % (TR_MAO_PROPRIA_TAKE % prox["nome"], sonorizar(falas[2]),
           cen["curto"])
    )

    return b


# ---------------------------------------------------------------------------
# LINTER — as regras TR
# ---------------------------------------------------------------------------
# ⚠️ A NUMERACAO E' A DA DOUTRINA, caractere por caractere (P9: uma regra, um
# lugar). A versao anterior tinha numeracao PROPRIA: o linter dizia "TR9: IMAGE
# 03/03 sem a ancora de bolso" e a TR9 da doutrina e' o `gelatin trick`. Dez
# numeros significavam coisas diferentes dos dois lados, e sete (TR15-TR21) nao
# existiam na doutrina — o operador nao tinha como auditar cobertura, e toda
# mensagem de erro o mandava ler a regra errada. A doutrina foi estendida ate' a
# TR21 para as regras que o motor legitimamente criou.
#
#   TR1  a TROCA                TR8   desmentido + escada da promessa
#   TR2  o prop nao cresce      TR9   batismo `gelatin trick` + keyword do CTA
#   TR3  proxy mudo / deixis    TR10  a F12b (agencia) + tokens proibidos
#   TR4  aplicacao elidida      TR11  casting / congruencia
#   TR5  substancia so' no prop TR12  figurino 🟡
#   TR6  fisica da substancia   TR13  elenco 1/1/2, uma voz
#   TR7  bancada-recibo + P12   TR14  orcamento (piso E teto) + cota do orgao
#   TR15 follow-gate            TR16  ⛔ declaracao de conformidade
#   TR17 os verbos da §6        TR18  ancora de continuidade invertida
#   TR19 recibo mudo            TR20  ledger        TR21  self-test
#
# Toda TR e' ERRO, salvo a TR12 (figurino), que e' AVISO por decisao [D3], e os
# AVISOs de orcamento e de eco.

def _achar(txt, tokens):
    """Os tokens de uma tabela que aparecem no texto (palavra inteira)."""
    return [t for t in tokens if re.search(r"\b%s\b" % re.escape(t), txt, re.I)]


# TR8 — DUAS FAMILIAS DE PROMESSA, as duas observadas na fonte: a numerica
# (7/8, `ten times bigger`) e a de RESISTENCIA (v01, `last all night long`).
# Sem promessa o comando e' so' esquisito (invariante 10/28), e e' por isso que
# a regra existe — nao pelo numero em si.
TR8_NUMERO = re.compile(
    r"\b(ten|twice|doubles?|two|three|four|eight|inch|inches|bigger|size)\b", re.I)
TR8_RESISTENCIA = re.compile(
    r"(never quits|all night|every time|a different animal|beats every)", re.I)

# TR3 — o `nome` de cada proxy mais as variantes que o espectador diria.
TR3_VARIANTES = ("carrots", "zucchinis", "bananas", "cucumbers", "radish",
                 "aubergine", "parsnips", "corn cob", "butternut", "sausages",
                 "yam")

# TR3 — deixis a PESSOA. Nas cenas 1 e 2 o elenco e' 1 (TR13): mandar olhar
# para um homem que o proprio IMAGE declara ausente reprova o teste do radio.
TR3_DEIXIS = ("look at him", "right here", "standing here", "that's him",
              "ask him yourself", "right there", "over there", "next to me")

TR10_TOKENS = ("groin", "pubic", "crotch", "genital", "the victim",
               "the narrator")

TR10_CONTATO = ("her hand on his", "she holds his", "grips his", "touches his",
                "reaches for his")

TR1_CORTES = ("cut to", "we cut", "then we see", "camera moves", "new shot",
              "reverse angle")

# P12. ⚠️ Nome de plataforma entra aqui: `Facebook` saia na `Dialogue:` em 7%
# dos lotes pela ultima entrada dos GATES.
TR7_MARCAS = ("Vicks", "VapoRub", "Arm & Hammer", "Jell-O", "Knox", "Vaseline",
              "label reading", "logo", "brand name", "readable label",
              "Facebook", "Instagram", "TikTok", "YouTube")

TR16_CONFORMIDADE = ("not a celebrity", "fully clothed", "no nudity",
                     "they are adults", "consenting", "nothing sexual")

TR17_VERBOS = ("strokes", "pumps", "grips", "slides her hand up and down",
               "up and down", "shaft", "mouth open", "lips parted", "tongue",
               "onto her chest", "onto her skin", "on her breasts",
               "pressed against her face",
               # conjugacoes: as travadas sao constantes, entao hoje nao ha'
               # vetor — o guarda vale para a proxima edicao de pool
               "stroking", "pumping", "gripping", "sliding up and down",
               "milks", "tugs", "tugging")


def _tr_crendice(spec, blocos, achados):
    """TR8 — a crendice nomeia o orgao DO ESPECTADOR e fecha com uma promessa.

    ⚠️ O `your` nao e' estilo: `your Johnson` e' o que TRANSFERE o proxy para o
    corpo de quem assiste (invariante 8/28, 8/8 na fonte). Sem ele a promessa
    deixa de ser enderecada e o hook vira fofoca sobre terceiros.
    """
    h = spec["falas"][0]
    if not any(n.lower() in h.lower() for n in NUCLEO):
        achados.append(("ERRO", "TR8: a crendice nao nomeia o orgao com "
                                "substantivo do nucleo"))
    elif not TR8_CORPO_2A.search(h):
        achados.append(("ERRO", "TR8: a crendice nomeia o orgao mas nao e' o do "
                                "ESPECTADOR ('your ...') — sem isso a promessa "
                                "nao e' enderecada"))
    if not (TR8_NUMERO.search(h) or TR8_RESISTENCIA.search(h)):
        achados.append(("ERRO", "TR8: a crendice nao carrega promessa "
                                "(numerica ou de resistencia) — sem o segundo "
                                "choque o comando e' so' esquisito"))


def _tr_claim_prazo(spec, blocos, achados):
    """TR8 — ⛔ CLAIM SOBRE O CORPO DO ESPECTADOR + PRAZO NA MESMA CENA.

    E' a composicao exata que derrubou o video do NECROSE com "politicas contra
    a geracao de conteudo nocivo": diagnostico do corpo de quem assiste somado a
    promessa com prazo. A forma que passa e' a da fonte — condicionar, nunca
    afirmar (licoes-producao-veo §Quando so' o video cai, olhe a FALA).
    """
    for i, fala in enumerate(spec["falas"], 1):
        if TR8_CORPO_2A.search(fala) and TR8_PRAZO.search(fala):
            achados.append(("ERRO", "TR8: cena %d empilha corpo do espectador "
                                    "('your ...') e PRAZO no mesmo take de 8s — "
                                    "condicionar, nunca afirmar" % i))


def _tr_segunda_pessoa(spec, blocos, achados):
    """P22 — cada cena aterrissa em 2a pessoa ou imperativo.

    Item do checklist da doutrina que nao tinha regra nenhuma: 16% das cenas 1
    e 32% das cenas 2 saiam em pura 3a/1a pessoa.
    """
    for i, fala in enumerate(spec["falas"], 1):
        if not _aterrissa(fala):
            achados.append(("AVISO", "P22: cena %d nao aterrissa em 2a pessoa "
                                     "nem em imperativo" % i))


def _tr_proxy_mudo(spec, blocos, achados):
    """TR3 — ⭐ O PROXY NUNCA E' NOMEADO NA FALA. E' o truque inteiro.

    O classificador e o algoritmo ouvem `gelatin` e `John-son`, nunca o objeto.
    A substituicao e' feita pelo espectador. ✅ Na direcao de cena o legume e'
    nomeado normalmente — e' la' que ele precisa ser desenhado.
    E o proxy tambem nao e' apontado por DEIXIS (4a forma de vago): neste
    formato e' pior ainda, porque a imagem nao entrega os dois estados (TR2) e
    porque nas cenas 1 e 2 o elenco e' 1.
    """
    corpo = " ".join(spec["falas"])
    nomes = tuple(p["nome"] for p in PROXIES) + TR3_VARIANTES
    for hit in _achar(corpo, nomes):
        achados.append(("ERRO", "TR3: a fala NOMEIA o proxy ('%s') — a "
                                "substituicao tem de ser feita pelo "
                                "espectador" % hit))
    for i in (1, 2):
        baixo = spec["falas"][i - 1].lower()
        for hit in [d for d in TR3_DEIXIS if d in baixo]:
            achados.append(("ERRO", "TR3: cena %d aponta por deixis ('%s') num "
                                    "quadro de elenco 1 — reprova o teste do "
                                    "radio" % (i, hit)))


def _tr_eco(spec, blocos, achados):
    """TR14 — o mesmo FATO dito duas vezes em 24 segundos.

    "two dollars" na cena 2 e na 3, "nineteen days" na fundida e na prova: o
    orcamento e' curto demais para pagar a mesma informacao duas vezes.
    """
    corpo = " ".join(spec["falas"]).lower()
    for e in ECOS:
        if corpo.count(e) > 1:
            achados.append(("AVISO", "TR14: '%s' aparece %d vezes no mesmo "
                                     "video — o orcamento nao paga o mesmo fato "
                                     "duas vezes" % (e, corpo.count(e))))


def _tr_orcamento(spec, blocos, achados):
    """TR14 — o orcamento e' PISO **E** TETO (ordem do operador).

    O `lint_curto` cobra o teto por cena; o PISO nao era cobrado por ninguem, e
    metade dos lotes saia com a cena 2 curta demais — exatamente o defeito que a
    regra existe para impedir ("adaptar aqui e' EXPANDIR ~2,3x").
    """
    for i, fala in enumerate(spec["falas"], 1):
        n = _palavras(fala)
        if n < PISO_FALA[i]:
            achados.append(("AVISO", "TR14: cena %d com %d palavras (piso %d) — "
                                     "o piso nao se cumpre com enchimento, e sim "
                                     "com mais FATO" % (i, n, PISO_FALA[i])))


def _tr_batismo(spec, blocos, achados):
    """TR9 — o batismo acontece na CENA 2, onde a troca acontece.

    O `lint_curto` ja' cobra o literal no corpo das tres falas; esta regra
    cobra o LUGAR. Se o nome do mecanismo escorrega para outra cena, o pivo
    perde o nome exatamente no ponto em que o objeto e' substituido.
    """
    if "gelatin trick" not in spec["falas"][1].lower():
        achados.append(("ERRO", "TR9: o literal 'gelatin trick' nao esta' na "
                                "cena 2 — o pivo perde o nome no ponto da troca"))


def _tr_cta(spec, blocos, achados):
    """TR9 — reafirma a tabela do CTA neste motor.

    O grosso e' herdado do `lint_curto` (keyword, caixa, virgula, BANIDOS_CTA);
    aqui so' se garante que a tabela EXISTE e esta' povoada — motor sem
    BANIDOS_CTA passaria em silencio pela checagem herdada.
    """
    if not BANIDOS_CTA:
        achados.append(("ERRO", "TR9: BANIDOS_CTA vazio — o CTA ficaria sem a "
                                "trava de BOOK/YES/LINK"))


def _tr_gates(spec, blocos, achados):
    """TR15 — GUARDA de vocativo na cena 3.

    ⚠️ Hoje esta regra nao dispara, e isso e' correto: so' os GATES carregam
    vocativo (2 de 14) e so' um gate entra por video. Ela existe para a proxima
    edicao de pool — se alguem puser 'brother' num CTA ou numa barreira, a cena
    3 passa a ter dois e o vicio que o operador mediu (31-73%) volta. A trava
    VIVA e' a do self-test, que exige BARREIRAS e CTAS sem vocativo nenhum.
    """
    cena3 = spec["falas"][2]
    hits = _achar(cena3, VOCATIVOS)
    if len(hits) > 1:
        achados.append(("AVISO", "TR15: dois vocativos na cena 3 (%s) — o "
                                 "operador mediu vicio de 'brother' e mandou "
                                 "variar" % ", ".join(hits)))


def _tr_troca(spec, blocos, achados):
    """TR1 — ⭐ A TROCA. Sem estes literais o Veo corta, e o argumento inteiro
    do agente morre: a leitura de SUBSTITUICAO depende de mesma mao, mesmo
    ponto, mesma altura, take unico."""
    t = blocos["TAKE 02/03"]
    for lit in ("same point in the frame, same hand, same height",
                "one continuous take"):
        if lit not in t:
            achados.append(("ERRO", "TR1: TAKE 02/03 sem o literal '%s' — sem "
                                    "ele o Veo corta e a troca vira corte "
                                    "disfarcado" % lit))
    for hit in _achar(t, TR1_CORTES):
        achados.append(("ERRO", "TR1: TAKE 02/03 contem '%s' — a troca e' em "
                                "take unico, camera parada" % hit))
    # ⚠️ UMA superficie so'. A versao anterior descia o proxy `onto the
    # workbench` e a frase seguinte dizia que ele ficava `on the wooden board`:
    # duas superficies para a mesma acao, no take que E' o agente.
    if "onto the wooden board" not in t:
        achados.append(("ERRO", "TR1: TAKE 02/03 nao desce o proxy 'onto the "
                                "wooden board' — a coreografia da TR1 usa UMA "
                                "superficie, e prompt que se contradiz o "
                                "modelo resolve como quiser"))
    # as batidas com segundos sao o metodo 🟢 de prop-metaforas §Coreografia:
    # verbo sozinho nao e' instrucao, o Veo precisa do COMO
    for batida in ("0 to 2 seconds", "2 to 4 seconds", "4 to 8 seconds"):
        if batida not in t:
            achados.append(("ERRO", "TR1: TAKE 02/03 sem a batida '%s' — a "
                                    "coreografia da TR1 e' em segundos"
                            % batida))


def _tr_sem_crescimento(spec, blocos, achados):
    """TR2 — [D4]: o prop nao cresce, e a promessa e' paga pela cara dela.

    ⚠️ Procura-se o MIOLO INVARIANTE, nunca o template. `TR_SEM_CRESCIMENTO`
    tem dois slots (%s do proxy e %s do gatilho) e chega ao bloco ja'
    formatado — comparar com o template cru da' 100% de falso positivo, que foi
    exatamente o que aconteceu em 400 de 400 sorteios. O trecho abaixo mora
    entre os dois slots e sobrevive a qualquer preenchimento.
    """
    if TR2_MIOLO not in blocos["TAKE 01/03"]:
        achados.append(("ERRO", "TR2: TAKE 01/03 sem a string travada de "
                                "imobilidade — [D4] cai e a promessa fica sem "
                                "quem a entregue"))


def _tr_agencia(spec, blocos, achados):
    """TR10 — ⭐ a F12b: ele segura na PROPRIA mao, ela aponta sem encostar.

    Esta e' a composicao que produziu as 4 recusas deterministicas de
    2026-07-30 quando estava errada. Nada aqui e' decorativo: sem `his own
    fist` a agencia nao esta' declarada; sem `beside the lap of his ...` a
    coordenada volta ao territorio de `groin`, que ja' custou recusa; e sem o
    olhar dele na lente sobra o homem passivo, que e' o que bloqueia.
    """
    img, take = blocos["IMAGE 03/03"], blocos["TAKE 03/03"]
    calca = spec["corpo_prova"]["calca"]
    if "his own fist" not in img:
        achados.append(("ERRO", "TR10: IMAGE 03/03 sem 'his own fist' — a "
                                "agencia nao esta' declarada"))
    if "beside the lap of his " not in img:
        achados.append(("ERRO", "TR10: IMAGE 03/03 sem a ancora de roupa "
                                "travada ('beside the lap of his ...') — e' a "
                                "formulacao que substituiu 'level with his "
                                "groin' depois de recusa paga"))
    if calca not in img:
        achados.append(("ERRO", "TR10: IMAGE 03/03 sem a peca de roupa sorteada "
                                "— a ancora precisa existir na imagem"))
    if "his eyes on the lens" not in img:
        achados.append(("ERRO", "TR10: IMAGE 03/03 sem o olhar dele na lente — "
                                "sem isso ele e' corpo passivo, e passividade e' "
                                "o que a F12b diz que bloqueia"))
    if "without touching him" not in img:
        achados.append(("ERRO", "TR10: IMAGE 03/03 sem 'without touching him'"))
    if "never touches him" not in take:
        achados.append(("ERRO", "TR10: TAKE 03/03 sem 'never touches him' — e' "
                                "o que separa a TROCA do ELA_DIAGNOSTICA, onde "
                                "o dedo crava no corpo dele"))
    if "keeps his eyes on the lens" not in take:
        achados.append(("ERRO", "TR10: TAKE 03/03 sem o olhar dele na lente — "
                                "a agencia tem de continuar no movimento"))
    for nome in ("IMAGE 03/03", "TAKE 03/03"):
        for hit in [t for t in TR10_CONTATO if t in blocos[nome].lower()]:
            achados.append(("ERRO", "TR10: %s contem contato dela nele ('%s')"
                            % (nome, hit)))


def _tr_tokens(spec, blocos, achados):
    """TR10, TR16 e TR12 — em QUALQUER bloco, fala inclusa."""
    for nome, txt in sorted(blocos.items()):
        for hit in _achar(txt, TR10_TOKENS):
            achados.append(("ERRO", "TR10: %s contem '%s' — token proibido "
                                    "(recusa paga ou ordem do operador)"
                            % (nome, hit)))
        for hit in [t for t in TR16_CONFORMIDADE if t in txt.lower()]:
            achados.append(("ERRO", "TR16: %s declara conformidade ('%s') — "
                                    "silencio vence negacao, e a declaracao e' "
                                    "municao de graca" % (nome, hit)))
        for hit in _achar(txt, tuple(BANIDOS_DESEJO)):
            achados.append(("ERRO", "TR12: %s usa vocabulario de desejo ('%s') "
                                    "— a divergencia [D3] e' de FIGURINO, nunca "
                                    "de vocabulario" % (nome, hit)))


def _tr_marca(spec, blocos, achados):
    """TR7 — P12: nenhuma marca legivel. ✅ `US flag` e' explicitamente
    permitido: nao e' marca, esta' no catalogo, e e' 8/8 na fonte.

    ⚠️ A varredura tira antes a propria frase de direcao de arte — hoje ela e'
    afirmativa e nao se denunciaria, mas o `replace` fica como guarda caso ela
    volte a citar `label`/`logo`.
    """
    for nome, txt in sorted(blocos.items()):
        limpo = txt.replace(FRASE_SEM_MARCA, "")
        for hit in _achar(limpo, TR7_MARCAS):
            achados.append(("ERRO", "TR7: %s contem marca/rotulo legivel "
                                    "('%s') — substituir por FORMA, nunca por "
                                    "marca" % (nome, hit)))
        if nome.startswith("IMAGE") and FRASE_SEM_MARCA not in txt:
            achados.append(("ERRO", "TR7: %s sem a frase de ausencia de "
                                    "rotulo" % nome))


def _tr_verbos(spec, blocos, achados):
    """TR17 — os verbos da §6 do mapa. A cena fica INTACTA; troca-se a forma de
    dizer pelas travadas TR_VAIVEM, TR_FIO e TR_PROXY_NA_MAO."""
    for nome, txt in sorted(blocos.items()):
        if not (nome.startswith("IMAGE") or nome.startswith("TAKE")):
            continue
        baixo = txt.lower()
        for hit in [t for t in TR17_VERBOS if t in baixo]:
            achados.append(("ERRO", "TR17: %s contem '%s' — usar a formulacao "
                                    "travada da §6; ⛔ nunca amputar a cena"
                            % (nome, hit)))


def _tr_recibo(spec, blocos, achados):
    """TR7/TR19 — o recibo aparece nos IMAGE 01 e 02, e NUNCA na copy.

    ⚠️ A 03/03 esta' FORA da varredura de proposito, e nao por esquecimento: e'
    o bloco de maior risco do lote (duas pessoas + proxy no colo dele) e a F12c
    manda encolher tudo que for descricao livre ali — "quanto mais info vc da'
    pro Veo, mais municao vc da' pra ele flagrar algo". O recibo ja' cumpriu o
    lastro do 'full recipe' nas duas cenas anteriores; repeti-lo na terceira
    paga superficie de bloqueio sem comprar nada. A versao anterior desta
    funcao exigia o recibo nas tres e reprovava 400 de 400 sorteios contra o
    comentario do proprio montar().
    """
    itens = spec["bancada"]["itens"]
    for nome in ("IMAGE 01/03", "IMAGE 02/03"):
        if itens not in blocos[nome]:
            achados.append(("ERRO", "TR7: %s sem a bancada-recibo — e' o lastro "
                                    "do 'full recipe'" % nome))
    corpo = " ".join(spec["falas"])
    for cab in spec["bancada"]["cabecas"]:
        if _cita(corpo, cab):
            achados.append(("ERRO", "TR19: a copy cita '%s', que e' item da "
                                    "bancada — o recibo so' tem lastro se a "
                                    "boca citar um e a imagem mostrar tres"
                            % cab))
    if _pares(spec["bancada"]["itens"]) & _pares(spec["substancia"]["pote"]):
        achados.append(("AVISO", "TR19: a bancada-recibo desenha um objeto que "
                                 "o pote da substancia ja' desenha — recibo que "
                                 "repete o pote mostra dois ingredientes, nao "
                                 "tres"))


def _tr_ancoras(spec, blocos, achados):
    """TR18 — a ancora de continuidade INVERTIDA, e o artigo do corpo-prova.

    Quem repete rosto aqui e' a narradora. O corpo-prova entra NOVO na cena 3:
    escrever 'the same' nele prometeria uma continuidade que nunca existiu, e o
    Veo tentaria casar com um rosto que nenhuma cena anterior mostrou.
    """
    et = ETNIA[spec["pagina"]]
    ancora = "the same %d-year-old woman" % spec["narradora"]["idade"]
    for nome in ("IMAGE 02/03", "IMAGE 03/03"):
        if ancora.lower() not in blocos[nome].lower():
            achados.append(("ERRO", "TR18: %s sem a ancora '%s' — sem o rosto "
                                    "repetido o Veo troca de pessoa entre as "
                                    "cenas" % (nome, ancora)))
        if spec["narradora"]["marca"] not in blocos[nome]:
            achados.append(("ERRO", "TR18: %s sem a marca facial da narradora "
                                    "por inteiro" % nome))
    img3 = blocos["IMAGE 03/03"]
    if not re.search(r"A %d-year-old %s man" % (spec["corpo_prova"]["idade"], et),
                     img3):
        achados.append(("ERRO", "TR18: IMAGE 03/03 sem o corpo-prova em artigo "
                                "indefinido — ele entra novo na cena 3"))
    if re.search(r"the same \d+-year-old %s man" % et, img3, re.I):
        achados.append(("ERRO", "TR18: IMAGE 03/03 marca o corpo-prova como "
                                "'the same' — promete uma continuidade que "
                                "nunca existiu"))
    # ⚠️ o mesmo objeto, a regua no corpo de QUEM SEGURA: 83% dos lotes saiam
    # com "in his own fist ... as long as HER forearm", contra a letra da TR10.
    if spec["proxy"]["img_dele"] not in img3:
        achados.append(("ERRO", "TR18: IMAGE 03/03 sem a ancora de escala no "
                                "corpo DELE — na cena 3 quem segura e' ele"))


def _tr_congruencia(spec, blocos, achados):
    """TR11 — [D2]: a etnia do HOMEM e' a da pagina; a dela nunca e' escrita."""
    et = ETNIA[spec["pagina"]]
    if "%s man" % et not in blocos["IMAGE 03/03"]:
        achados.append(("ERRO", "TR11: IMAGE 03/03 sem a etnia '%s' no "
                                "corpo-prova — congruencia inviolavel com o "
                                "avatar da pagina" % et))
    for nome, txt in sorted(blocos.items()):
        if re.search(r"(white|black) American\s+woman", txt, re.I):
            achados.append(("ERRO", "TR11: %s declara etnia da narradora — ela "
                                    "e' sorteada livre [D2] e o motor nunca "
                                    "escreve a etnia dela" % nome))
    if spec["narradora"]["idade"] < IDADE_MINIMA_NARRADORA:
        achados.append(("ERRO", "TR11: narradora com %d anos (piso %d) — idade "
                                "em cena com conteudo de ED e' zona sensivel, e "
                                "o piso nao se baixa sem ordem do operador"
                        % (spec["narradora"]["idade"], IDADE_MINIMA_NARRADORA)))


def _tr_voz(spec, blocos, achados):
    """TR10 — a voz da cena 2 casa com a RELACAO nomeada na cena 3.

    A relacao nomeada e' a alavanca 2 do protocolo de recusa; contradize-la na
    fala a anula. `my husband's {o}` num IMAGE 03 que diz "she is the woman from
    the house next door" e' o prompt discordando de si mesmo — 13% dos lotes.
    """
    if voz_da_relacao(spec["relacao"]) == "conjugal":
        return
    baixo = spec["falas"][1].lower()
    for marca in ("my husband", "quitting on us"):
        if marca in baixo:
            achados.append(("ERRO", "TR10: a cena 2 fala em voz conjugal ('%s') "
                                    "e a relacao nomeada e' '%s'"
                            % (marca, spec["relacao"])))


def _tr_figurino(spec, blocos, achados):
    """TR12 🟡 — [D3]: figurino da fonte. AVISO, nunca ERRO.

    Os 8 concorrentes usam cropped e passam na moderacao com 11K-30K views, e o
    operador decidiu seguir a fonte. Mas isto e' divergencia deliberada do UN1
    do UNCAO (que continua valendo la' integralmente), com selo amarelo ate' o
    nosso A/B — entao o linter sinaliza e nao reprova.
    """
    for nome in ("IMAGE 01/03", "IMAGE 02/03", "IMAGE 03/03"):
        if "cropped" not in blocos[nome]:
            achados.append(("AVISO", "TR12: %s sem o figurino da fonte "
                                     "('cropped') — 🟡 divergencia do UN1, "
                                     "decisao [D3]" % nome))


def lint(spec, blocos):
    # ⚠️ `teto_total` explicito: o padrao do `lint_curto` e' a soma dos tetos
    # (82), que aqui e' o PISO do orcamento da doutrina — o AVISO dispararia
    # acima do numero que a TR14 exige como MINIMO. A borda de cima e' 96.
    return sc.lint_curto(
        sys.modules[__name__], spec, blocos, (1, 2, 3), TETO_FALA,
        literais=("gelatin trick",), teto_total=TETO_TOTAL,
        extras=(_tr_crendice, _tr_claim_prazo, _tr_segunda_pessoa,
                _tr_proxy_mudo, _tr_eco, _tr_orcamento, _tr_batismo, _tr_cta,
                _tr_gates, _tr_troca, _tr_sem_crescimento, _tr_agencia,
                _tr_tokens, _tr_marca, _tr_verbos, _tr_recibo, _tr_ancoras,
                _tr_congruencia, _tr_voz, _tr_figurino))


# ---------------------------------------------------------------------------
# UI — contrato do ui_agente.py compartilhado
# ---------------------------------------------------------------------------
# ⚠️ "homens_de" e' FUNCAO da pagina, nao lista — a UI resolve isso desde
# 2026-07-31 (ui_agente.trocar_eixo). "NARRADORAS" e' lista simples porque a
# narradora e' solta [D2].
EIXOS_UI = [
    ("narradora", "A NARRADORA", "NARRADORAS", "marca"),
    ("corpo_prova", "O CORPO-PROVA (cena 3)", "homens_de", "marca"),
    ("cenario", "O CENARIO", "CENARIOS", "id"),
    ("proxy", "O PROXY", "PROXIES", "nome"),
    ("substancia", "A SUBSTANCIA DO HOOK", "SUBSTANCIAS", "fala"),
    ("textura", "A FISICA DA SUBSTANCIA", "TEXTURAS", "id"),
    ("mecanismo", "O MECANISMO PLANTADO", "MECANISMOS_PROP", "curto"),
    ("bancada", "A BANCADA-RECIBO", "BANCADAS", "itens"),
]

PT_CENARIO = {
    "cozinha_modesta": "Na cozinha modesta de laminado",
    "cozinha_ilha": "Na cozinha aberta com ilha de mármore",
    "cozinha_fazenda": "Na cozinha de fazenda com pia de louça",
    "cozinha_cabana": "Na cozinha de cabana de pinho",
    "cozinha_retro": "Na cozinha anos setenta de parede de madeira",
    "trailer": "Na cozinha corredor do trailer",
    "escritorio": "No escritório de autoridade, com estante e diplomas",
    "alpendre": "No alpendre telado dos fundos",
    "garagem": "Na bancada de garagem",
    "copa_igreja": "Na copa do salão comunitário",
    "varanda_sol": "No jardim de inverno",
    "lavanderia": "Na lavanderia",
    "rv": "Na cozinha do motorhome",
    "cozinha_moderna": "Na cozinha moderna preta",
}


def resumo_pt(spec):
    """A frase que permite aprovar ou re-sortear em dois segundos."""
    et = "branca" if "white" in ETNIA[spec["pagina"]] else "negra"
    return (
        "%s, uma narradora de %d anos segura o proxy (%s) no punho ESQUERDO, ao "
        "lado do rosto, com a direita trabalhando a substância, e manda esfregar "
        "%s no órgão. Na cena 2 o proxy desce na tábua e %s sobe no mesmo ponto "
        "do quadro, mesma mão, sem corte. Na cena 3 um homem de %d anos, de pele "
        "%s, segura o proxy na própria mão, ao lado do colo, olhando na lente, "
        "enquanto ela aponta sem encostar. Três cenas de 8s, nada cresce em "
        "quadro."
        % (PT_CENARIO.get(spec["cenario"]["id"], "Na cozinha"),
           spec["narradora"]["idade"], spec["proxy"]["id"],
           spec["substancia"]["fala"], spec["mecanismo"]["curto"],
           spec["corpo_prova"]["idade"], et)
    )


def _recopiar_crendice(spec, rng):
    """A substancia entra na cena 1 e em tres fundidas — trocar o eixo obriga a
    reescrever as duas primeiras falas, senao o painel mostra 'turmeric' no
    pote e 'honey' na boca.

    ⚠️ E re-sorteia a bancada se a substancia nova colidir com o recibo (TR19):
    o operador nao teria como consertar isso pela interface.
    """
    orgaos = [sc.orgao_de(sys.modules[__name__], spec["falas"][0]),
              sc.orgao_de(sys.modules[__name__], spec["falas"][1],
                          padrao="soldier"), NUCLEO[0]]
    novas = _montar_falas(rng, spec["substancia"], orgaos, spec["relacao"],
                          spec.get("degrau"))
    spec["falas"][0], spec["falas"][1] = novas[0], novas[1]
    if any(_cita(" ".join(spec["falas"]), c) for c in spec["bancada"]["cabecas"]):
        spec["bancada"] = _bancada_livre(rng, spec["falas"], [],
                                         spec["substancia"])


def _recopiar_tudo(spec, rng):
    """Trocar a narradora reescreve as tres falas E a relacao.

    Nao e' capricho: a idade dela e' metade da conta da relacao nomeada da cena
    3 (TR10) — trocar uma narradora de 45 por uma de 28 deixaria 'his wife of
    twenty-five years' num rosto que nao fecha a aritmetica. E a voz da copy
    (esposa, vizinha, a mulher que cozinha) acompanha: a relacao e' recalculada
    ANTES das falas, para que o filtro de voz da cena 2 valha.
    """
    orgaos = rng.sample(NUCLEO, 3)
    spec["relacao"] = _relacao(rng, spec["narradora"]["idade"],
                               spec["corpo_prova"]["idade"])
    spec["falas"] = _montar_falas(rng, spec["substancia"], orgaos,
                                  spec["relacao"], spec.get("degrau"))
    if any(_cita(" ".join(spec["falas"]), c) for c in spec["bancada"]["cabecas"]):
        spec["bancada"] = _bancada_livre(rng, spec["falas"], [],
                                         spec["substancia"])


def _trocar_corpo_prova(spec, rng):
    """O corpo-prova nao mexe em fala nenhuma, mas mexe na RELACAO — que e'
    aritmetica de idade (31 anos de casamento nao cabem num homem de 51 com uma
    narradora de 28) — e a relacao manda na VOZ da cena 2 (TR10). Se a relacao
    nova deixar de autorizar a voz conjugal, a cena 2 se refaz."""
    spec["relacao"] = _relacao(rng, spec["narradora"]["idade"],
                               spec["corpo_prova"]["idade"])
    if voz_da_relacao(spec["relacao"]) != "conjugal":
        baixo = spec["falas"][1].lower()
        if "my husband" in baixo or "quitting on us" in baixo:
            spec["falas"][1] = nova_fala(spec, 1, rng)


EIXOS_QUE_MEXEM_NA_COPY = {
    "substancia": _recopiar_crendice,
    "narradora": _recopiar_tudo,
    "corpo_prova": _trocar_corpo_prova,
}


def nova_fala(spec, i, rng):
    """Re-sorteia a fala da cena i (0-2) preservando o orgao que ja' esta' nela
    — a rotacao do substantivo e' do VIDEO, nao da fala."""
    o = sc.orgao_de(sys.modules[__name__], spec["falas"][i])
    orgaos = [o, o, o]
    return _montar_falas(rng, spec["substancia"], orgaos, spec["relacao"],
                         spec.get("degrau"))[i]


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def imprimir(spec, blocos, achados):
    print("=" * 72)
    print("SPEC — pagina %s | narradora %s (%d) | corpo-prova %s (%d) | "
          "cenario %s" % (spec["pagina"], spec["narradora"]["id"],
                          spec["narradora"]["idade"], spec["corpo_prova"]["id"],
                          spec["corpo_prova"]["idade"], spec["cenario"]["id"]))
    print("       proxy %s | substancia %s | textura %s | mecanismo %s | "
          "bancada %s" % (spec["proxy"]["id"], spec["substancia"]["id"],
                          spec["textura"]["id"], spec["mecanismo"]["id"],
                          spec["bancada"]["id"]))
    print("=" * 72)
    print(resumo_pt(spec))
    print("=" * 72)
    print(blocos["BLOCO 0 (REF)"] + "\n")
    for k in sorted(k for k in blocos if k.startswith("IMAGE")):
        print("-" * 72)
        print(blocos[k] + "\n")
    for k in sorted(k for k in blocos if k.startswith("TAKE")):
        print("-" * 72)
        print(blocos[k] + "\n")
    print("=" * 72)
    for i, fala in enumerate(spec["falas"], 1):
        print("cena %d: %d/%d palavras" % (i, _palavras(fala), TETO_FALA[i]))
    if not achados:
        print("LINTER: OK — nenhuma violacao mecanica.")
    else:
        for nivel, msg in achados:
            print("[%s] %s" % (nivel, msg))
        n_erros = sum(1 for a in achados if a[0] == "ERRO")
        print("%d erro(s), %d aviso(s)." % (n_erros, len(achados) - n_erros))


# TR21 — SELF-TEST DE ENTROPIA. A barra e' ordem explicita do operador: "no
# minimo o mesmo nivel de entropia dos demais agentes shorts". Medida em 400
# sorteios, 80 por pagina, com ledger vivo (a anti-repeticao faz parte do
# comportamento real).
EIXOS_VISUAIS = ("narradora", "corpo_prova", "cenario", "proxy", "substancia",
                 "textura", "mecanismo", "bancada")
MIN_OPCOES = 9          # piso por eixo visual
TETO_FREQ = 0.17        # nenhum item pode concentrar mais que isso
MIN_COPY = {"CRENDICES": 16, "FUNDIDAS": 13, "CTAS": 14, "GATES": 11}


def autoteste(n_por_pagina=80, seed=7, degrau=None):
    falhas = []

    # --- tamanho de pool ---------------------------------------------------
    tamanhos = {"NARRADORAS": len(NARRADORAS),
                "CORPOS_PROVA_CLARA": len(CORPOS_PROVA_CLARA),
                "CORPOS_PROVA_ESCURA": len(CORPOS_PROVA_ESCURA),
                "PROXIES": len(PROXIES), "SUBSTANCIAS": len(SUBSTANCIAS),
                "TEXTURAS": len(TEXTURAS), "CENARIOS": len(CENARIOS),
                "BANCADAS": len(BANCADAS),
                "MECANISMOS_PROP": len(MECANISMOS_PROP)}
    for nome, n in sorted(tamanhos.items()):
        if n < MIN_OPCOES:
            falhas.append("eixo visual %s com %d opcoes (minimo %d)"
                          % (nome, n, MIN_OPCOES))
    copy = {"CRENDICES": len(CRENDICES), "DESMENTIDOS": len(DESMENTIDOS),
            "FUNDIDAS": len(FUNDIDAS), "PROVAS": len(PROVAS),
            "CTAS": len(CTAS), "GATES": len(GATES),
            "BARREIRAS": len(BARREIRAS)}
    for nome, piso in sorted(MIN_COPY.items()):
        if copy[nome] < piso:
            falhas.append("pool de copy %s com %d entradas (minimo %d)"
                          % (nome, copy[nome], piso))

    # --- TR15, regra de POOL dos gates -------------------------------------
    # ⚠️ A checagem de BARREIRAS/CTAS e' a trava VIVA: `n_voc` media exatamente o
    # mesmo conjunto que `n_brother` (2 e 2), entao a linha da "maioria" nao
    # testava nada independente. O vocativo so' pode existir nos GATES; se
    # escorregar para os outros dois pools, a cena 3 passa a ter dois num video
    # so' e o vicio que o operador mediu (31-73%) volta.
    n_brother = sum(1 for g in GATES if "brother" in g.lower())
    n_voc = sum(1 for g in GATES if _achar(g, VOCATIVOS))
    if n_brother > 2:
        falhas.append("TR15: %d gates com 'brother' (maximo 2)" % n_brother)
    if n_voc >= len(GATES) / 2.0:
        falhas.append("TR15: %d de %d gates com vocativo — a maioria tem de "
                      "vir sem nenhum" % (n_voc, len(GATES)))
    for nome, pool in (("BARREIRAS", BARREIRAS), ("CTAS", CTAS)):
        sujos = [x for x in pool if _achar(x, VOCATIVOS)]
        if sujos:
            falhas.append("TR15: %d entrada(s) de %s com vocativo — o vocativo "
                          "so' mora nos GATES" % (len(sujos), nome))

    # --- TR11, piso de idade da narradora ----------------------------------
    novas = [x["id"] for x in NARRADORAS
             if x["idade"] < IDADE_MINIMA_NARRADORA]
    if novas:
        falhas.append("TR11: narradora(s) abaixo do piso de %d anos: %s"
                      % (IDADE_MINIMA_NARRADORA, ", ".join(novas)))

    # --- TR14, o orcamento e' alcancavel? ----------------------------------
    # ⚠️ Enumeracao exaustiva do pior e do melhor caso de cada cena. Foi assim
    # que se descobriu que o teto de nenhuma cena era alcancavel (AVISO de teto
    # virava codigo morto) e que a cena 2 ficava abaixo do piso em 48% dos
    # sorteios. Agora as duas bordas sao medidas, nao estimadas.
    extra = max(_palavras(s["fala"]) for s in SUBSTANCIAS) - 1
    extra_o = max(_palavras(o) for o in NUCLEO) - 1
    faixas = {
        1: ([_palavras(c["txt"]) for c in CRENDICES],
            [_palavras(d) for d in DESMENTIDOS], extra + extra_o),
        2: ([_palavras(f["txt"]) for f in FUNDIDAS],
            [_palavras(p) for p in PROVAS], extra + extra_o),
    }
    for i, (a_, b_, ex) in sorted(faixas.items()):
        if min(a_) + min(b_) < PISO_FALA[i]:
            falhas.append("TR14: cena %d pode sair com %d palavras (piso %d) — "
                          "o pool nao alcanca o piso do operador"
                          % (i, min(a_) + min(b_), PISO_FALA[i]))
        if max(a_) + max(b_) + ex > TETO_FALA[i]:
            falhas.append("TR14: cena %d pode estourar (%d, teto %d)"
                          % (i, max(a_) + max(b_) + ex, TETO_FALA[i]))
    piso3 = min(_palavras(x) for x in BARREIRAS) + \
        min(_palavras(x) for x in CTAS) + min(_palavras(x) for x in GATES)
    teto3 = max(_palavras(x) for x in BARREIRAS) + \
        max(_palavras(x) for x in CTAS) + max(_palavras(x) for x in GATES)
    if piso3 < PISO_FALA[3]:
        falhas.append("TR14: cena 3 pode sair com %d palavras (piso %d)"
                      % (piso3, PISO_FALA[3]))
    if teto3 > TETO_FALA[3]:
        falhas.append("TR14: cena 3 pode estourar (%d, teto %d)"
                      % (teto3, TETO_FALA[3]))

    # --- 400 sorteios -------------------------------------------------------
    rng = random.Random(seed)
    freq, total_eixo, erros, avisos, n = {}, {}, 0, 0, 0
    for pag in sorted(ETNIA):
        ledger = {}
        for _ in range(n_por_pagina):
            spec = sortear(pag, rng, ledger, degrau)
            blocos = montar(spec)
            for nivel, msg in lint(spec, blocos):
                if nivel == "ERRO":
                    erros += 1
                    if erros <= 5:
                        print("  ERRO (%s): %s" % (pag, msg))
                else:
                    avisos += 1
            # o corpo-prova e' pool POR ETNIA: medir junto com as outras
            # paginas diluiria a concentracao e mentiria a favor.
            for eixo in EIXOS_VISUAIS:
                chave = (eixo + ":" + ETNIA[pag]) if eixo == "corpo_prova" else eixo
                freq.setdefault(chave, {})
                freq[chave][spec[eixo]["id"]] = freq[chave].get(spec[eixo]["id"], 0) + 1
                total_eixo[chave] = total_eixo.get(chave, 0) + 1
            _anotar(ledger, spec)
            n += 1

    print("\nENTROPIA — %d sorteios (%d por pagina)" % (n, n_por_pagina))
    print("-" * 72)
    for chave in sorted(freq):
        c = freq[chave]
        topo, qtd = max(c.items(), key=lambda kv: kv[1])
        pc = qtd / float(total_eixo[chave])
        marca = "OK " if pc <= TETO_FREQ else "X  "
        print("  %s %-28s %2d opcoes | mais sorteado %-22s %4.1f%%"
              % (marca, chave, len(c), topo, pc * 100))
        if pc > TETO_FREQ:
            falhas.append("eixo %s concentra %.1f%% em '%s' (teto %.0f%%)"
                          % (chave, pc * 100, topo, TETO_FREQ * 100))

    print("\nPOOLS DE COPY")
    print("-" * 72)
    for nome in sorted(copy):
        print("  %-12s %d" % (nome, copy[nome]))
    print("  gates com 'brother': %d | gates com vocativo: %d de %d"
          % (n_brother, n_voc, len(GATES)))

    print("\nLINTER em %d sorteios: %d ERRO, %d AVISO" % (n, erros, avisos))
    if erros:
        falhas.append("%d ERRO de linter em %d sorteios" % (erros, n))

    print("\n" + "=" * 72)
    if falhas:
        for f in falhas:
            print("FALHA: %s" % f)
        print("SELF-TEST REPROVADO (%d falha(s))." % len(falhas))
        return 1
    print("SELF-TEST OK — a barra de entropia foi cumprida.")
    return 0


def stats(degrau=None):
    ledger = _carregar_ledger()
    if ledger:
        print("LEDGER — uso recente por pagina")
        print("-" * 72)
        for pag, eixos in sorted(ledger.items()):
            print("\n%s" % pag.upper())
            for eixo, vals in sorted(eixos.items()):
                cont = {}
                for v in vals:
                    cont[v] = cont.get(v, 0) + 1
                print("  %-12s %s" % (eixo, ", ".join("%s:%d" % kv
                                                      for kv in sorted(cont.items()))))
        print("")
    else:
        print("ledger vazio — nenhum video sorteado ainda.\n")
    return autoteste(degrau=degrau)


def main():
    ap = argparse.ArgumentParser(description="Randomizador do agente TROCA SHORT")
    ap.add_argument("--pagina", choices=sorted(ETNIA))
    ap.add_argument("--n", type=int, default=1)
    ap.add_argument("--seed", type=int, help="reproduzivel")
    ap.add_argument("--dry-run", action="store_true", help="nao grava ledger")
    # ⚠️ TR8: a escolha do degrau da promessa e' ALCADA DO ED. O pool sai
    # misturado por padrao (comportamento antigo); com esta flag ele roda o lote
    # inteiro num degrau so'. Antes o motor decidia por sorteio o que a doutrina
    # reservava ao operador — e o operador nao tinha como escolher sem editar
    # codigo.
    ap.add_argument("--degrau", choices=DEGRAUS,
                    help="trava a escada da promessa da cena 1 (TR8) — "
                         "assertiva 🟡 | condicional (a unica validada) | "
                         "testemunho | resistencia")
    ap.add_argument("--stats", action="store_true",
                    help="uso dos pools + self-test de entropia (TR21)")
    a = ap.parse_args()

    if a.stats:
        return stats(a.degrau)

    if not a.pagina:
        ap.error("informe --pagina <joe|ray|matt|marcus|chuck> (ou --stats)")

    rng = random.Random(a.seed)
    ledger = _carregar_ledger()
    saida = 0
    for i in range(a.n):
        spec = sortear(a.pagina, rng, ledger, a.degrau)
        blocos = montar(spec)
        achados = lint(spec, blocos)
        if a.n > 1:
            print("\n\n########## VIDEO %d/%d ##########\n" % (i + 1, a.n))
        imprimir(spec, blocos, achados)
        if any(x[0] == "ERRO" for x in achados):
            saida = 1
        # o lote inteiro se lembra de si mesmo; so' a GRAVACAO respeita o
        # --dry-run (mesma logica do botao "marcar como usado" do app, que le'
        # o ledger sempre e escreve so' quando o lote foi de fato usado)
        _anotar(ledger, spec) if a.dry_run else _gravar_ledger(ledger, spec)
    return saida


if __name__ == "__main__":
    sys.exit(main())
