#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE RESSURREICAO SHORT — 3 cenas de 8 segundos (24s), SHORT NATIVO.

Doutrina: AGENTE_ED_RESSURREICAO_V1.md (regras R1-R8 + §A VARIANTE SHORT)
Fonte:    concorrentes/sofia-maren-pouring-mapa-visual.md — 52 frames abertos um
          a um, medicao em pixels no MP4 (extracao extra a 10 e 20 fps na janela
          do morph), camera provada fixa, transcricao confrontada palavra a
          palavra. 2026-08-02.

⭐ POR QUE ESTE MOTOR E NAO UM AGENTE NOVO
------------------------------------------
A decomposicao do reel garimpado deu NOVE pecas e nenhuma orfa: a peca central
— despejo sobre prop na bancada, e o prop cresce na tela — e' literalmente a
"Pouring de mao (H7)" do RESSURREICAO, escrita naquelas palavras ANTES do
garimpo. O RESSURREICAO era o unico angulo com bit visual validado que nunca
virou ferramenta (`ressurreicao_*.py` nao existia no disco). Entao, em vez do
vigesimo agente, o decimo segundo motor — decisao do operador em 2026-08-02.

⛔ SHORT NATIVO — NAO DERIVA DE MOTOR LONGO
Nao existe e nao deve existir um `ressurreicao_lucas.py`: o angulo cabe inteiro
em tres batidas. Como o `troca_short.py` e o `escandalo_short.py`, este arquivo
e' motor completo (pools proprios) mas usa a maquinaria compartilhada do
`short_comum.py` (`lint_curto`, `selar_takes`, `lint_isca_cta`,
`lint_cta_literal`) passando A SI MESMO como `base`.

AS TRES EMENDAS QUE O GARIMPO PAGOU — e elas sao o coracao do motor
-------------------------------------------------------------------
[R2-emenda] ⭐⭐ A ESCALA E' DIFERENCIAL. Medido frame a frame no arquivo:
     altura 149->345px = 2,31x, largura 73->105px = 1,44x, razao 2,04 -> 3,29
     (+61%). O prop ALONGA, nao incha — termina 61% mais esguio. A R2 antiga so'
     mandava "dobrar de comprimento" e CALAVA sobre grossura, e o silencio e'
     autorizacao: sem dizer o contrario o Veo escala o objeto inteiro, e escala
     uniforme le' como INCHACO — que e' o vocabulario de tumescencia (`swell`,
     `pulse`) que ja' derrubou video nosso. RS_ESCALA_DIFERENCIAL diz as DUAS
     coisas. ⚠️ Selo 🟡: e' medicao da FONTE, nao render nosso.
[R7]        ⭐⭐ O CRESCIMENTO MORA NO APAGAO DE LEGENDA. A legenda da fonte
     esta' na tela em 0,0-3,9 / 4,7-6,9 / 7,0-15,7 / 15,8-39,5: o UNICO apagao
     real dos 40 segundos e' 3,9-4,7s = 0,8 segundo, exatamente em cima do morph
     de 0,6s. Todos os outros vaos sao de 0,1s. Nao e' acaso, e' DIRECAO — nada
     compete com a imagem no instante em que a imagem e' o argumento.
[R8]        ⭐ O JATO E' MASCARA, NAO SO' CABO. Engrossa 0,3s ANTES do morph e
     para 0,05s DEPOIS; entre 3,6 e 4,0s o prop SOME dentro da coluna de po', e
     e' la' dentro que a escala vira. Sem a cortina o Veo tem de resolver a
     transformacao em campo aberto — que e' a parte cara, e e' onde ele inventa
     (bicho se levantando, segundo prop, anatomia impossivel).

⭐ O ACHADO ④ — A PLATEIA COLAPSADA NO ROSTO DELA (ES1, segunda geometria)
Nos dois reels anteriores da pagina havia 1-2 figurantes mudos de boca aberta
(foi dali que saiu o ESCANDALO). Aqui NAO HA' NINGUEM: a funcao foi colapsada no
rosto da narradora, no mesmo plano focal do prop. E' estruturalmente melhor para
nos — custa um personagem a menos, elimina a composicao de corpo passivo em
quadro (a familia das 4 recusas deterministicas de 2026-07-30) e resolve de graca
a tensao 🔴 aberta na ES1 sobre onde por o figurante: com plateia interna nao
existe figurante para posicionar. E cumpre a R3 (alguem reage ENQUANTO cresce:
sem reacao le' como glitch de IA; com reacao le' como milagre).

O FLAG `--credibilidade` — E O DEFAULT E' CONFIRMA
--------------------------------------------------
`confirma` e' a forma VALIDADA deste agente: o crescimento como PROVA, a promessa
numerica virando imagem, a fala confirmando e transferindo. `desmente` e' o TR8
do TROCA, variante DESMENTE, literal — o crescimento vira GAG.
⚠️ O default e' CONFIRMA e o motivo e' um numero, nao um gosto: o reel que
desmente fez 3.872 views, o irmao da mesma pagina fez 32.900, e os 9 reels SEM
crescimento das duas paginas garimpadas fizeram 11K-33K. Nao ha' evidencia
nenhuma de que desmentir ajude. ⚠️ E n=1 tambem nao prova o contrario — por isso
o `desmente` nao e' banido: fica como variante, e roda-lo e' decisao do Ed.
Mesma mecanica do `--degrau` do ESCANDALO: variante de risco e' FLAG, nunca
redesenho — assim uma recusa custa uma flag e nao um lote.

⛔ SE A CENA 1 CRESCE, NADA CRESCE NAS CENAS 2 E 3 (achado ⑧)
Em 24 segundos a regra do arco longo ("nunca PICO2 da familia crescimento") fica
mais dura: nas cenas 2 e 3 o prop e' OBJETO ESTATICO DECLARADO. Dois choques
iguais em 24 segundos somam a um. E' verificavel por regex, entao e' LINTER
(RS6), nao comentario.

⚠️ DIVERGENCIAS DA SPEC DE CONSTRUCAO — declaradas, com o motivo
----------------------------------------------------------------
1) ⭐ OS TETOS SAO OS DA DOUTRINA, NAO OS DA SPEC. A spec pedia
   TETO_FALA={1:28,2:34,3:34} / PISO_FALA={1:20,2:26,3:24}; o
   `AGENTE_ED_RESSURREICAO_V1.md` ja' esta' emendado e diz, com a conta escrita,
   `TETO_FALA = {1: 27, 2: 34, 3: 30}` e `PISO_FALA = {1: 16, 2: 26, 3: 20}`,
   declarando esses numeros "o CONTRATO do motor". Motor que contradiz a
   doutrina manda o operador ler a regra errada (licoes-de-construcao §3), entao
   valem os da doutrina. ⚠️ A diferenca e' ALCADA DO ED e esta' registrada: com
   27/34/30 a soma dos tetos e' 91 (a faixa 82-96 volta a ser alcancavel); com
   28/34/34 seria 96 (a borda de cima exata). Trocar e' editar duas linhas.
2) A REACAO SAI DO IMAGE E VAI PARA O TAKE. A spec punha a REACAO sorteada
   dentro de RS_PLATEIA_INTERNA_IMAGE **e** dentro de RS_PLATEIA_INTERNA_TAKE
   ("her face changes once and stops: %s"). Se o primeiro frame ja' mostra a
   cara de choque, mandar a cara "mudar uma vez e parar" NAQUELE choque obriga o
   modelo a sair dele primeiro — prompt que se contradiz o modelo resolve como
   quiser. E a R3 exige a reacao DURANTE o crescimento, nao antes. Entao o IMAGE
   fica com a metade que carrega peso (unica pessoa em quadro, mesmo plano
   focal, mesmo foco) e a analogia de genero (`the way a studio audience reacts
   to a punchline`, alavanca 3 — e' o que segura o escandalo SEM `mouth open`)
   desceu para o TAKE, colada a expressao que ela qualifica.
3) O terceiro slot de RS_JATO_MASCARA recebe o NOME FALADO da substancia, nao o
   `jato`: "the column of a steady column of fine white powder" nao e' ingles. A
   travada nao mudou uma virgula — mudou o que se poe no slot.
4) A BANCADA-RECIBO entra SO' no IMAGE 02/03. O rotulo da spec dizia "so' no
   IMAGE 02/03" e a linha seguinte dizia "fora do IMAGE 03"; vale a segunda, que
   e' o precedente TR7/F12c — o IMAGE 03 e' o bloco mais arriscado do lote e
   densidade e' superficie de bloqueio.
5) ⭐ O JATO NAO PARA — e esta divergencia era MUDA ate' 2026-08-02. O titulo da
   R8 diz que o jato "engrossa 0,3s ANTES do morph e PARA 0,05s DEPOIS", e a
   frase travada da doutrina termina em `and the pour stops in the same instant`.
   O motor escreve `The column thins again the instant it stops` e os 12 TAKEs
   de DESPEJOS mandam o contrario explicito (`does not lower it`). ⚠️ E esta'
   CERTO assim, mas o motivo tem de estar escrito: o MONTE na mesa e' o
   CRONOMETRO deste motor ([6]) e ele cresce `the whole time` — parar o despejo
   aos ~5s mata o cronometro, e sem tempo passado o crescimento nao tem por que
   ter acontecido. Na fonte o jato podia parar porque o reel continua por mais
   35 segundos; aqui o take acaba em 8. ⛔ Quem "corrigir" o motor copiando a
   travada da doutrina quebra o cronometro — por isso a doutrina tambem foi
   emendada, e nao so' este comentario.
6) ⭐ A REACAO E' NO RECONHECIMENTO, NAO NO ALONGAMENTO. A R3 pede reacao
   DURANTE o crescimento; o RS_PLATEIA_INTERNA_TAKE poe `At the moment it comes
   back out of the column`, que e' o instante do RECONHECIMENTO. E' consequencia
   direta da R8: dentro da oclusao o prop nao esta' visivel, entao nao ha' o que
   reagir — reacao a uma coluna de po' opaca nao le' como milagre, le' como
   nada. Declarado aqui porque divergencia calada e' a §3 do
   licoes-de-construcao com outra roupa.
7) ⛔ O MORPH CAI EM 3-5s, E A R2 PEDE ~3s. ⚠️ ESTA NAO FOI CORRIGIDA — e' copy
   e cena, alcada do Ed (CLAUDE.md §Regra de alcada). A R2 diz "Comeca e termina
   nos primeiros ~3s" citando o P17 ("o feed da' 2 segundos"), e o
   RS_CRESCIMENTO_TAKE manda `0 to 3 seconds: ... does not change. 3 to 5
   seconds: it gets longer`. O bit visual inteiro do agente acontece DEPOIS da
   janela que a propria regra chama de decisiva: o timing veio da fonte (morph
   em 3,6-4,2s de um reel de 40s) e foi copiado para um take de 8s sem
   reescalar. Nenhuma RS cobra a janela. Reportado ao operador em 2026-08-02.

Uso:
    python funil-organico/ressurreicao_short.py --pagina joe --n 2
    python funil-organico/ressurreicao_short.py --pagina marcus --n 3 --seed 42
    python funil-organico/ressurreicao_short.py --pagina ray --n 1 --dry-run
    python funil-organico/ressurreicao_short.py --pagina joe --n 5 --credibilidade desmente
    python funil-organico/ressurreicao_short.py --pagina joe --n 5 --degrau 4
    python funil-organico/ressurreicao_short.py --pagina joe --n 5 --analogia pressao
    python funil-organico/ressurreicao_short.py --stats
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
LEDGER = os.path.join(AQUI, ".ressurreicao-short-ledger.json")

TITULO = "AGENTE RESSURREICAO SHORT"
SUBTITULO = ("o despejo que ressuscita — o prop murcho que alonga na tela, "
             "dentro da coluna de po' · 3 cenas")
SLUG = "ressurreicao-short"

CENAS_UI = ["1 · O DESPEJO E O CRESCIMENTO", "2 · A RECEITA INCOMPLETA",
            "3 · A PROVA + CTA"]

# ---------------------------------------------------------------------------
# ORCAMENTO — piso E teto, e os dois sao mecanicos
# ---------------------------------------------------------------------------
# ⚠️ NUMEROS DA DOUTRINA, caractere por caractere (§Os tetos — medidos, nao
# conservadores). De onde vem cada um:
#   cena 1 — 8s MENOS os 0,8s de silencio obrigatorio da R7 = 7,2s. O teto
#            medido de uma cena cheia de 8s e' 30 (ESCANDALO, capacidade real
#            27-32 na nossa taxa de 3,4-4,0 p/s); 30 x 0,9 = 27.
#   cena 2 — identico ao ESCANDALO. ⛔ ZERO folga: 34 em 8s ja' pede 4,25 p/s,
#            ACIMA da taxa mediana da propria fonte (3,61). Bullet aqui e'
#            atropelo garantido — e' por isso que a cena 2 e' uma fala so'.
#   cena 3 — capacidade medida 29-35; a cena abre com PROVA e comporta UM bullet
#            de barreira depois dela.
# ⚠️ Teto conservador vira espaco morto, e espaco morto vira enchimento
# (licoes-de-construcao §5): no ESCANDALO o teto era 22, a capacidade real 27-32
# e as falas mediam 18,4 — o slot que sobrava virou "Give me eight seconds".
TETO_FALA = {1: 27, 2: 34, 3: 30}
PISO_FALA = {1: 16, 2: 26, 3: 20}

# ⚠️ A borda de CIMA da faixa 82-96 da doutrina. ⛔ Nao usar a soma dos tetos
# (91): o AVISO por video dispararia abaixo do numero que a faixa exige.
TETO_TOTAL = 96

# Congruencia inviolavel: etnia do CORPO-PROVA = etnia do avatar da pagina.
# ⛔ A narradora NAO usa este dict — ela e' solta (ver NARRADORAS), e o motor
# nunca escreve adjetivo de etnia junto dela.
ETNIA = {"joe": "white American", "ray": "white American", "matt": "white American",
         "marcus": "Black American", "chuck": "Black American"}

NUCLEO = ["Johnson", "soldier", "pecker", "manhood", "wiener", "tool", "old boy"]

# ⛔ PISO DE IDADE 28 — herdado do organicwave_short (`IDADE_MINIMA_MULHER`) com
# o motivo escrito: "ja' pagamos para descobrir que idade em cena com conteudo de
# ED e' zona sensivel". Pesa mais aqui porque a cena 3 pareia a narradora com um
# homem de ate' 70 numa composicao de proxy falico.
IDADE_MINIMA_NARRADORA = 28

# ⛔ ES11 — a politica de MENORES e' a determinista (nao cede a regerar) e e'
# sensivel a GEOMETRIA DE INTIMIDADE + DIFERENCA DE IDADE, nao a idade absoluta.
# Sem teto, o sorteio livre pareava narradora de 28 com homem de 70 na F12b. O
# risco vinha do SORTEIO, e sorteio se conserta por filtro.
TETO_DIF_IDADE = 30

# ⭐ O FLAG DA CREDIBILIDADE. Default CONFIRMA — ver docstring.
CREDIBILIDADES = ("confirma", "desmente")
CREDIBILIDADE_PADRAO = "confirma"

# ⭐ A escada de moderacao do hook (§8 do mapa). O degrau 1 (o literal da fonte,
# `Pour baking soda on your John-son and watch it swell up overnight`) NAO ESTA'
# NO POOL: ele soma `your <nucleo>` + PRAZO no mesmo take de 8s, que e' a
# composicao exata que derrubou o video do NECROSE — a fala da fonte e' reprovada
# pelo NOSSO PROPRIO linter (RS10) antes de chegar ao Veo.
#   2 🔴 assertiva sem prazo — ⚠️ ver a nota abaixo: o 🔴 e' da FONTE, nao nosso
#   3 🟡 condicional
#   4 🟢 a ATRIBUICAO (`they say`) — o achado de moderacao deste angulo
#   5 🟢 plana
#
# ⭐⭐ DEFAULT 2 — ORDEM DO OPERADOR, 2026-08-02, e o motivo e' COPY, nao risco.
# O default era 3, e o degrau 3 e' o UNICO dos quatro cujos hooks NAO nomeiam a
# substancia: medido, 0 de 400 videos diziam o nome dela na cena 1. A fonte diz
# na palavra 3 (`Pour baking soda on your Johnson...`). Sem o nome da coisa, os
# beats seguintes viravam anafora sem antecedente — `the mechanism`, `that's not
# on you`, `explained it`, tres definidos apontando para nada. O operador leu o
# take renderizado e cravou: "quem ve o video nem entende do que se trata".
#
# ⚠️ E O 🔴 DO DEGRAU 2 NAO TRANSFERE PARA O NOSSO POOL. O selo foi dado a'
# formulacao LITERAL DA FONTE, que tem dois gatilhos que nenhuma das nossas tem:
#   fonte:  `Pour baking soda ON YOUR JOHN-SON and watch it SWELL UP.`
#   nossa:  `Pour {s} ON IT and watch what your {o} could do.`
# A nossa despeja no PROXY, nao no corpo, e nao tem verbo de inchaco. Medido nas
# tres entradas do degrau 2: zero aplicacao no corpo, zero vocabulario de
# inchaco.
# ⚠️ Residual honesto: `watch what your {o} could do` nao e' condicional de
# forma (nao abre com `if`), embora `could` seja modalidade condicional. Das 3
# entradas do degrau 2, so' essa nomeia o orgao; as outras duas nao o citam.
# ⭐ BONUS MEDIDO: no degrau 3 os SEIS hooks nomeavam o orgao, e a regra de
# nomea-lo uma vez por cena deixava a cena 1 com apenas TRES bullets sorteaveis.
# No degrau 2 so' um dos tres nomeia — o pool de bullets volta a abrir.
DEGRAUS = (2, 3, 4, 5)
DEGRAU_PADRAO = 2

# ⭐ A familia da analogia fisica. `extensao` (uma ponta fixa, a outra viaja,
# espessura constante) e' o default POR FORCA DA R2-EMENDA. `pressao` descreve
# INFLACAO — que e' exatamente o que a emenda proibe —, e fica sob flag porque a
# unica analogia com selo 🟢 EM RENDER (`fire hose`, Joe/geoduck) e' dela.
# ⚠️ Nenhuma das 10 de extensao passou por render. Selo 🟡 ate' o primeiro take.
FAMILIAS_ANALOGIA = ("extensao", "pressao")
ANALOGIA_PADRAO = "extensao"


# ---------------------------------------------------------------------------
# STRINGS TRAVADAS — ⛔ constantes, nunca redigitadas
# ---------------------------------------------------------------------------
# ⚠️ Os `%s` sao SLOTS DO MOTOR, nao texto a reescrever. Comprimir uma travada
# "com as minhas palavras" ja' entregou esqueleto 3D no lugar da placa em corte
# (RUNBOOK-app-offline §Por que portar). Descricao livre encolhe; bloco validado
# se copia caractere por caractere.

CAUDA = "Shot on iPhone, natural grain. No on-screen text, no watermark."

# P12. ⚠️ ESCRITA NA AFIRMATIVA de proposito: "Nothing carries a readable label,
# logo or brand" injeta `label`, `logo` e `brand` num prompt cuja tese e' que nao
# ha' nenhum — a mesma mecanica de `fully clothed`.
# ⭐ E aqui ela pesa mais que nos outros agentes: na fonte a marca da caixa fica
# legivel O HOOK INTEIRO e em varios frames e' o objeto mais nitido do quadro,
# porque tem CARGA FUNCIONAL (o rotulo laranja faz "bicarbonato" ser lido em 0,2s
# sem uma palavra). Tirar a marca custa alguma coisa, e o custo e' real.
FRASE_SEM_MARCA = "Every container in the frame is plain and unlabelled."

# ---------------------------------------------------------------------------
# ⭐⭐ [1] R2-EMENDA — A ESCALA DIFERENCIAL. Medida em pixels: altura 2,31x,
# largura 1,44x, razao 2,04 -> 3,29. E' esta frase que impede o Veo de escalar
# tudo junto — e escala uniforme le' como INCHACO.
# ---------------------------------------------------------------------------
RS_ESCALA_DIFERENCIAL = (
    "its length roughly doubles while its width barely changes, so it finishes "
    "noticeably slimmer in proportion than it started"
)

# ---------------------------------------------------------------------------
# ⭐⭐ [2] R8 — O JATO E' MASCARA. O jato faz DOIS trabalhos: e' o CABO que liga
# causa a efeito e e' a CORTINA que esconde a transicao. Sem ela o Veo resolve a
# transformacao em campo aberto, que e' a parte cara.
# Slots: jato da substancia · nome do prop · NOME FALADO da substancia · topo.
# ⚠️ O terceiro slot e' o nome falado (ver divergencia 3 da docstring).
# ---------------------------------------------------------------------------
RS_JATO_MASCARA = (
    "A third of a second before it changes, %s thickens into a wide column and "
    "the %s is hidden inside it and cannot be seen. It comes back out of the "
    "column of %s already at its new length, %s first. The column thins again "
    "the instant it stops."
)

# ---------------------------------------------------------------------------
# ⭐⭐ [3] R7 — O APAGAO. A regra mais barata do lote: custa uma linha e vale
# para todo take de crescimento que ja' temos.
# ⚠️ PENDENCIA EXPLICITA, e ela NAO e' minha de resolver: a regra tem tres
# camadas e so' duas estao no motor — (1) a direcao no TAKE, aqui; (2) a legenda
# por cima, que nasce no Veo Editor a partir do Whisper e e' ponteiro no
# `adbatch-prompts-editor.md`; (3) o campo `Dialogue:` propriamente dito, que e'
# UMA string so' e nao tem como declarar uma pausa de 0,8s sem inventar um
# contrato de parser. ⛔ Nao inventei: mexer no parser do AdBatch por conta
# propria e' a mesma familia de erro de "mudar a cena para destravar".
#
# ⛔⛔ CORRECAO DE 2026-08-02 — O APAGAO E' DE 0,8s, NAO DE 2s, E E' ANCORADO NO
# MORPH. A versao anterior dizia "between three and five seconds" (uma janela de
# DOIS segundos) e na frase seguinte "through that whole second": contradizia a
# si mesma dentro da propria string, que e' exatamente o argumento que a
# divergencia 2 desta docstring usa para tirar a reacao do IMAGE. E o numero
# estava errado nos dois sentidos:
#   · a R7 mede 0,8s (3,9->4,7s na fonte), e o mapa e' explicito: "reservar 0,8
#     segundo ... capacidade cai para 7,2s -> 26 a 31 palavras";
#   · o TETO_FALA[1]=27 da doutrina E' 30 x 0,9, e o 0,9 e' 7,2/8. Com 2s de
#     silencio o fator seria 6/8 = 0,75 e o teto teria de cair para ~22. Medido
#     em 400 sorteios: a cena 1 sai com 26,8 palavras de media — 3,72 p/s em
#     7,2s (dentro da capacidade) mas 4,46 p/s em 6,0s, ACIMA do pico da propria
#     fonte (4,4). O motor pedia uma fala que nao cabia no take que ele mesmo
#     escrevia.
# ⚠️ E a ancora deixou de ser o relogio absoluto: `around the moment it changes`
# nao colide com as batidas 0-3 / 3-5 / 5-8 do RS_CRESCIMENTO_TAKE, que era a
# segunda contradicao da versao anterior.
# ---------------------------------------------------------------------------
RS_APAGAO = (
    "Her mouth is closed and still for eight tenths of a second around the "
    "moment it changes, and no word is spoken over that beat."
)

# ---------------------------------------------------------------------------
# [4] R4 — A MAO SEGURA A BASE. ⛔⛔ REVOGA A "R4-EMENDA (ancora sem mao)" DE
# 2026-08-02, QUE DUROU MENOS DE UM DIA E FOI REPROVADA NO PRIMEIRO RENDER.
#
# O QUE A EMENDA DIZIA: o prop fica solto, em pe', no eixo central da bancada,
# sem nenhuma mao tocando — "mao em quadro daria escala e denunciaria o efeito".
# A ancora era `the base of it stays pinned to the same spot on the <bancada>
# and never moves, never tips, never slides; it only grows upward`.
#
# ⛔ POR QUE QUEBROU, e o defeito e' de LOGICA, nao de sorte: `base cravada no
# mesmo ponto` + `so' cresce para cima` sao duas ordens que o modelo NAO tem
# como satisfazer juntas quando o corpo alonga. Ele resolve a conta pelo unico
# jeito que sobra — ENFIANDO A BASE DENTRO DA MESA. Render de 2026-08-02: a
# banana afunda no tampo e o po' forma uma cratera em volta do buraco.
# ⛔ E o frame 0 ja' nascia implausivel: fruta em pe' no proprio eixo maior, sem
# nada segurando, nao para em pe' no mundo real — o gerador entrega equilibrio
# impossivel, e implausibilidade no primeiro frame contamina o take inteiro.
#
# ⭐ ORDEM DO OPERADOR (2026-08-02, lendo o render): a REF segura a base do prop
# em pe' com UMA mao e despeja com a OUTRA. E' o retorno a' R4 original
# (`never leaving his hands, never set down`) — a emenda e' que era o desvio.
# A mao que segura vira a ANCORA FISICA de verdade: ela da' ao modelo um motivo
# visivel para a base nao se mover, em vez de uma proibicao abstrata.
# ⚠️ O medo de "mao em quadro da' escala" se inverte aqui e joga a favor: com o
# punho fechado na base, o que cresce e' explicitamente o TRECHO ACIMA DO PUNHO,
# e a mao vira a regua que TORNA o crescimento legivel.
# Slots: bancada.
# ---------------------------------------------------------------------------
# ⚠️ "her other hand" e nao "her left hand": os DESPEJOS nomeiam a mao que
# despeja (quase todos a direita, um a esquerda), e travar a mao que segura em
# um lado fixo brigaria com esse pool. Generico casa com os dois.
RS_BASE_NA_MAO = (
    "her other hand is closed around the base of it and holds it standing "
    "upright on the %s the whole time; that hand never lets go, never lifts and "
    "never changes position, and only the part above her fist gets longer"
)

# ⛔ A TRAVA CONTRA O AFUNDAMENTO. Nao basta tirar a ordem contraditoria: o
# modelo ja' aprendeu esse atalho e precisa ouvir o contrario em afirmativa.
# ⚠️ AFIRMATIVA, nunca negacao pura: `the surface is solid and unbroken` guia,
# `does not sink` so' planta a palavra (mesma logica da FRASE_SEM_MARCA).
# Slots: bancada · bancada.
RS_SUPERFICIE_SOLIDA = (
    "The top of the %s is solid and unbroken all the way across, and the bottom "
    "end of it rests on that surface inside her fist the entire time; it stays "
    "on top of the %s and no part of it ever goes below the surface."
)

# ⚠️ A amarracao continua DUPLA (R4): a mao e' o primeiro fio, este e' o segundo.
RS_SEM_FLUTUAR = "No floating objects."

# ---------------------------------------------------------------------------
# [5] R2b — A COREOGRAFIA POR BATIDAS. ⚠️ A NUMERACAO E' A DA DOUTRINA, e ela
# esta' registrada na R8 justamente para ninguem "corrigir" depois:
#   1 ancora fixa · 2 analogia fisica · 3 propagacao · 4 estado final travado ·
#   5 articulacao e arco (+5b orientacao da base) · 6 teto de comprimento ·
#   7 trava de identidade · 8 OCLUSAO
# — OITO elementos, e a ESCALA DIFERENCIAL nao e' um deles: ela e' propriedade
# do ESTADO FINAL (elemento 4), e por isso entrou como EMENDA DA R2, nao como
# batida nova. ⛔ Este comentario dizia "os nove elementos" e listava DEZ nomes,
# promovendo a escala diferencial e a orientacao da base a elementos proprios —
# uma terceira numeracao, num repo que ja' tinha duas (o mapa da fonte propos
# escala=8 e oclusao=9; a doutrina fechou em oclusao=8). Corrigido 2026-08-02.
# A lista completa e numerada mora no `prop-metaforas.md` §Coreografia de
# crescimento — uma regra, um lugar.
# ⚠️ Batidas com SEGUNDOS EXPLICITOS: o Veo respeita marcacao temporal muito
# melhor que adverbio, e isso satisfaz o P17 (crescimento em ~3s) sem usar
# `slowly`.
# ⚠️ Estoura o orcamento de 80-150 palavras do TAKE — e' EXCECAO AUTORIZADA pela
# R2b (prop de armadilha documentada paga essa conta).
# Slots, nesta ordem: prop · bancada · bancada(RS_BASE_NA_MAO) · analogia ·
#                     topo · prop · bancada · prop · prop ·
#                     bancada · bancada (RS_SUPERFICIE_SOLIDA)
# ---------------------------------------------------------------------------
RS_CRESCIMENTO_TAKE = (
    "0 to 3 seconds: the %s stands on the %s exactly as it appears in the first "
    "frame and does not change. "
    + RS_BASE_NA_MAO[0].upper() + RS_BASE_NA_MAO[1:] + ". "
    "3 to 5 seconds: it gets longer %s. The growth travels up out of her fist "
    "toward the free tip, and " + RS_ESCALA_DIFERENCIAL + ". %s comes "
    "back into view at the new height and is the smallest part of it now. "
    "5 to 8 seconds: it does not move again. It stays at exactly that length "
    "for the rest of the shot, and never grows past the length of her forearm. "
    "There is only ONE %s in this shot, the same one already standing on the "
    "%s in the first frame. That exact same %s is the one that gets longer. No "
    "second %s appears at any point and nothing new grows beside it. "
    + RS_SUPERFICIE_SOLIDA
)

# O ESTADO FINAL declarado com a escala inteira. ⛔ A declaracao de escala tem de
# ser IDENTICA nas tres cenas a menos do pronome (RS8): escala diferente entre as
# cenas le' como um SEGUNDO crescimento fora do take que o coreografa.
# Slot: prop["depois"].
RS_ESTADO_FINAL_TAKE = (
    "From five seconds to the end of the shot it is %s, and it does not change "
    "again."
)

# ---------------------------------------------------------------------------
# [6] O CRONOMETRO — o monte de po' na mesa. Cresce o take INTEIRO, independente
# do prop. Sem ele nao ha' "passou tempo", e sem tempo passado o crescimento nao
# tem por que ter acontecido. Slots: bancada, monte.
# ---------------------------------------------------------------------------
RS_CRONOMETRO = (
    "On the %s under it, %s the whole time, wider at the end of the shot than "
    "at the start."
)

# O anel de po' JA' FORMADO no frame 0 — na fonte nao existe frame de "antes": o
# video abre com o pouring ja' em andamento (a mesma economia do TR4). Slots:
# anel derivado do monte, bancada.
RS_ANEL_IMAGE = "%s already lies around its base on the %s."

# ---------------------------------------------------------------------------
# [7] ⭐ A PLATEIA INTERNA (achado ④). ⚠️ `the way a studio audience reacts to a
# punchline` e' a alavanca 3 (nomear o genero da imagem) e e' o que mantem a cara
# de escandalo SEM `mouth open`. ⛔ zero `mouth open` / `lips parted` /
# `open-mouthed` / `tongue`: a reacao entra por sobrancelha, olho e gesto parado.
# ⚠️ A reacao mora no TAKE, nao no IMAGE — ver divergencia 2 da docstring.
# Slot IMAGE: prop. Slot TAKE: reacao.
# ---------------------------------------------------------------------------
RS_PLATEIA_INTERNA_IMAGE = (
    "She is the only person in the frame, in the same focal plane as the %s and "
    "just as sharply in focus. She is watching it, her eyes on it and her face "
    "still."
)
RS_PLATEIA_INTERNA_TAKE = (
    "At the moment it comes back out of the column her face changes once and "
    "stops: %s, the way a studio audience reacts to a punchline. She holds that "
    "expression without change until the end of the shot."
)

# ---------------------------------------------------------------------------
# [8] ⭐ A F12b — TERCEIRA FORMULACAO. COPIADA CARACTERE POR CARACTERE do
# TROCA §TR10 -> ESCANDALO §ES4 (ordem do Ed de 2026-08-01, olhando oito
# renders). ⛔ NAO reescrever: `beside the lap` -> `centred against the front`
# custou oito renders lidos, e `level with his groin` custou uma recusa.
# ⛔ ZERO `groin`/`pubic`/`crotch`: a coordenada vem da PECA DE ROUPA.
# Slots IMAGE: peca da calca (NUA) · prop ancorado NELE · relacao NOMEADA.
# Slot TAKE: nome do prop.
# ---------------------------------------------------------------------------
RS_F12B_IMAGE = (
    "Centred against the front of his %s, in both his own fists one stacked "
    "above the other, he holds %s — the base of it resting on the fabric, the "
    "tip pointing straight up. Standing beside him, %s points one finger down "
    "at it without touching him, talking straight to camera."
)

RS_F12B_TAKE = (
    "Her pointing finger stays close but never touches him. He keeps his eyes "
    "on the lens and never speaks; both his own fists stay where they are. The "
    "%s in his own fists stays exactly as it appears in the first frame — "
    "completely motionless for the entire shot."
)

# ---------------------------------------------------------------------------
# [9] A TRAVADA DE IMOBILIDADE (prop-metaforas §Regra dos dois lados), copiada
# NUA e com o objeto NOMEADO. ⛔ E' o que cobre o achado ⑧ nas cenas 2 e 3.
# ⛔ Sem `changes size, shape or state` — negacao que injeta `size` e `state` num
# prompt cuja tese e' que nada muda. Slot: nome do prop.
# ---------------------------------------------------------------------------
RS_IMOVEL_TAKE = (
    "The %s stays exactly as it appears in the first frame — completely "
    "motionless for the entire shot."
)

# ---------------------------------------------------------------------------
# [10] ES9 — O OBJETO DA KEYWORD NA MAO NO FRAME DA KEYWORD.
# ⚠️ `held level`, NUNCA `held flat to the lens` (correcao de 2026-08-02):
# `flat to the lens` nasceu para o donut e manda INCLINAR uma tigela rasa de
# cubos — contradicao fisica dentro do proprio IMAGE.
# ⚠️ A mao livre e' a ESQUERDA porque a F12b ja' comprometeu a direita com o dedo
# que aponta. Slot: mecanismo["curto"].
# ---------------------------------------------------------------------------
RS_KEYWORD_NA_MAO_IMAGE = (
    "In her own free left hand, raised to the height of her chest and held "
    "level, she holds %s."
)

RS_KEYWORD_NA_MAO_TAKE = (
    "What she holds in her own free left hand stays at that same height and "
    "does not move for the entire shot."
)

# ---------------------------------------------------------------------------
# [11] A BANCADA-RECIBO (TROCA §TR7 = ESCANDALO §ES8). ⚠️ SO' NO IMAGE 02/03.
# ⛔ Fora do IMAGE 01 (que ja' carrega ela + o prop + o jato + o monte + o anel)
# e fora do IMAGE 03 (o bloco mais arriscado do lote): densidade e' superficie de
# bloqueio. Slots: bancada, itens.
# ---------------------------------------------------------------------------
RS_BANCADA_RECIBO = (
    "Laid out on the %s beside her, never touched and never mentioned: %s. "
    + FRASE_SEM_MARCA
)

# ---------------------------------------------------------------------------
# [12] TR1/ES9 — o detalhe forense POR MECANISMO. A peca do mecanismo ja' estava
# plantada desde o frame 1: o reveal nao apresenta nada novo. Objeto que entra de
# fora do quadro nao e' premio, e' corte disfarcado.
# ⚠️ O detalhe e' POR MECANISMO: mandar desenhar "its lid lying face-up" numa
# TIGELA e' contradicao dentro do proprio IMAGE.
# Slots: mecanismo["curto"] SEM artigo, bancada, mecanismo["pousado"].
# ---------------------------------------------------------------------------
RS_PLANTADO_IMAGE = "The %s has been standing on the %s since the first frame, %s."

# ---------------------------------------------------------------------------
# [13] ES5/prop-metaforas §Coreografia — A RECEITA EXECUTADA, em batidas com
# segundos. Copiada literal do ES_RECEITA_TAKE do escandalo_short.
# ⛔ ZERO medida, ZERO duracao, ZERO horario: forma e gesto.
# Slots: receita["gesto"], receita["fisica"], mecanismo["curto"].
# ---------------------------------------------------------------------------
RS_RECEITA_TAKE = (
    "0 to 3 seconds: %s. 3 to 5 seconds: her left hand turns a wooden spoon "
    "through it twice and lifts the spoon clear of the rim. 5 to 8 seconds: %s, "
    "and her right hand comes to rest on the board beside %s and stays there. "
    "She talks straight into the lens the whole time."
)


# ---------------------------------------------------------------------------
# ELENCO
# ---------------------------------------------------------------------------
# ⭐⭐ A LICAO QUE ESTE MOTOR NASCE CUMPRINDO (licoes-de-construcao §15).
# O operador mediu os 21 pools de personagem do repo e TODOS tinham eixo
# descritivo zerado — oculos = 0 em 20 de 21, barba = 0 em varios, porte quase
# ausente. Dez pessoas descritas so' por cabelo sao a MESMA pessoa dez vezes, e o
# gerador devolve o mesmo rosto. Queixa literal: "seu repertorio de personagens
# esta fraquissimo".
# ⛔ Portanto CADA entrada difere das outras em pelo menos TRES eixos, e os eixos
# sao CAMPOS SEPARADOS — cabelo (cor+corte+linha) · oculos · porte · rosto (a
# marca P6, permanente) · idade · roupa. Assim a diversidade e' AUDITAVEL por
# enumeracao (`medir_personagens.py`) em vez de aferida a olho.
# ⚠️ E o corolario do §6: a chave de contagem do medidor de entropia e' O OBJETO
# INTEIRO, nunca um subconjunto de campos escolhido a olho.
#
# ⭐ A NARRADORA E' SOLTA NA ETNIA — precedente [D2] do TROCA/ESCANDALO: o REF
# nao e' o avatar; o avatar e' o corpo-prova da cena 3. O cabelo e' o descritor
# mais etnico que existe e o pool tem afro, box braids, ruivo, platinado, loiro,
# tapered e crespo: o render varia sozinho. ⛔ Zero adjetivo de etnia aqui.
# ⚠️ Solta na etnia, NAO na idade: piso de 28 (IDADE_MINIMA_NARRADORA).
NARRADORAS = [
    {"id": "ruiva_sardas", "idade": 29,
     "cabelo": "long copper-red hair parted low on one side",
     "oculos": "",
     "porte": "small and narrow through the shoulders",
     "rosto": "a heavy dusting of freckles across her nose and cheeks",
     "roupa": "a cropped dark-green ribbed tank top and black leggings"},
    {"id": "oculos_redondos", "idade": 37,
     "cabelo": "wavy caramel-blonde hair pushed back off a high forehead",
     "oculos": "thin round gold-rimmed glasses",
     "porte": "tall and long-limbed",
     "rosto": "a small dark mole beside her left nostril",
     "roupa": "a cropped charcoal ribbed tank top and high-waisted black leggings"},
    {"id": "afro_curto", "idade": 34,
     "cabelo": "a short natural afro shaved close at the sides",
     "oculos": "",
     "porte": "broad-shouldered and squarely built",
     "rosto": "a small dark beauty mark high on her left cheekbone",
     "roupa": "a cropped mustard knit top and a thin gold chain"},
    {"id": "loira_raiz", "idade": 41,
     "cabelo": "long honey-blonde hair with grown-out roots",
     "oculos": "",
     "porte": "heavy-set and full through the arms",
     "rosto": "sun-freckled skin and a deep dimple in her right cheek",
     "roupa": "a fitted black t-shirt tucked into high-waisted jeans"},
    {"id": "rabo_alto", "idade": 30,
     "cabelo": "jet-black hair pulled into a high slicked-back ponytail",
     "oculos": "",
     "porte": "compact and thick through the shoulders",
     "rosto": "a wide gap between her front teeth",
     "roupa": "a cropped grey sweatshirt cut off above the waist"},
    {"id": "tranca_caixa", "idade": 31,
     "cabelo": "waist-length box braids gathered over one shoulder",
     "oculos": "",
     "porte": "tall and heavy-boned",
     "rosto": "a small raised scar at the point of her chin",
     "roupa": "a cropped burgundy tank top and stacked gold bangles"},
    {"id": "grisalha_meia_lua", "idade": 47,
     "cabelo": "silver-streaked dark hair in a loose low bun",
     "oculos": "half-moon reading glasses pushed up onto her head",
     "porte": "short and square through the middle",
     "rosto": "weathered skin and deep laugh lines at the outer corners of her eyes",
     "roupa": "a denim shirt knotted at the waist over a plain vest"},
    {"id": "bob_platinado", "idade": 28,
     "cabelo": "a bleached-platinum bob cut sharp at the jaw",
     "oculos": "",
     "porte": "very slight and narrow-framed",
     "rosto": "a small hoop through her left nostril",
     "roupa": "a cropped lilac zip-up and gold rings on three fingers"},
    {"id": "franja_reta", "idade": 33,
     "cabelo": "long chestnut hair with a blunt fringe cut straight across",
     # ⚠️ `glasses`, nao `frames`: o gate de personagem casa o eixo por palavra,
     # e `frames` nao conta como oculos. Mesma imagem, medicao honesta.
     "oculos": "heavy black rectangular glasses",
     "porte": "average height and softly built",
     "rosto": "a small crescent birthmark at her right temple",
     "roupa": "a rust-orange long-sleeve top pushed up to the elbows"},
    {"id": "cachos_bronze", "idade": 39,
     "cabelo": "tight auburn-dyed curls worn wide",
     "oculos": "",
     "porte": "tall and rangy",
     "rosto": "a thin pale scar along her left jawline",
     "roupa": "a cropped emerald wrap top and long gold drop earrings"},
    {"id": "tapered_macas", "idade": 43,
     "cabelo": "a close tapered cut faded high at the sides",
     "oculos": "thin wire-framed oval glasses low on her nose",
     "porte": "lean and flat-shouldered",
     "rosto": "a beauty mark under her right eye",
     "roupa": "a charcoal turtleneck and heavy gold hoops"},
    {"id": "tranca_unica", "idade": 30,
     "cabelo": "long jet-black hair in a single braid over one shoulder",
     "oculos": "",
     "porte": "short and round-shouldered",
     "rosto": "a small dark tattoo of three stars behind her right ear",
     "roupa": "a cropped white crochet top and gold bangles"},
    {"id": "coque_bagunca", "idade": 36,
     "cabelo": "sandy-blonde hair twisted into a messy topknot",
     "oculos": "",
     "porte": "broad and strong through the back",
     "rosto": "faintly freckled skin and pale grey-green eyes under heavy dark brows",
     "roupa": "a sage-green tank top and a slim gold watch"},
    {"id": "morango_gatinho", "idade": 45,
     "cabelo": "long wavy strawberry-blonde hair",
     "oculos": "tortoiseshell cat-eye glasses",
     "porte": "small and fine-boned",
     "rosto": "lightly freckled skin and a beauty mark just above her upper lip",
     "roupa": "a cropped pale-blue knit top and a thin gold chain bracelet"},
    {"id": "crespo_solto", "idade": 32,
     "cabelo": "a big loose curl-out worn wide off the face",
     "oculos": "",
     "porte": "tall and broad through the chest",
     "rosto": "a small vertical scar through her left eyebrow",
     "roupa": "a cropped terracotta rib tank and a flat gold collar"},
    {"id": "grisalha_curta", "idade": 52,
     "cabelo": "close-cropped steel-grey hair worn natural",
     "oculos": "square gold-rimmed reading glasses",
     "porte": "stocky and thick through the forearms",
     "rosto": "deeply lined skin and a deep vertical line between her brows",
     "roupa": "a plain navy work shirt with the sleeves rolled"},
]

# ⭐ O CORPO-PROVA — o homem da cena 3 (F12b/TR10/ES4). TRAVADO na etnia da
# pagina via homens_de(); a etnia e' injetada pelo dict ETNIA, ⛔ nunca escrita
# na descricao. 55-70 anos: e' o CORPO com que o espectador se identifica.
# ⚠️ `calca` nasce NUA (sem oracao subordinada) porque entra na travada da F12b —
# cada palavra a mais no IMAGE 03 e' superficie de bloqueio no bloco mais
# arriscado do lote.
CORPOS_PROVA_CLARA = [
    {"id": "prata_pintinha", "idade": 58,
     "cabelo": "thick silver hair swept straight back", "barba": "clean-shaven",
     "oculos": "", "porte": "tall and still square through the shoulders",
     "rosto": "a large dark mole high on his left cheekbone",
     "roupa": "a plain navy short-sleeve work shirt", "calca": "khaki work pants"},
    {"id": "barba_branca", "idade": 62,
     "cabelo": "thinning grey hair cut short",
     "barba": "a full white beard trimmed close",
     "oculos": "heavy black rectangular glasses",
     "porte": "heavy-set and thick through the chest",
     "rosto": "deep-set pale grey eyes under heavy brows",
     "roupa": "a heather-grey pocket tee", "calca": "faded blue jeans"},
    {"id": "covinha_tempora", "idade": 56,
     "cabelo": "dark hair greying hard at the temples", "barba": "clean-shaven",
     "oculos": "", "porte": "lean and long-armed",
     "rosto": "sun-weathered skin and a deep vertical dimple in his left cheek",
     "roupa": "an olive canvas shirt with the sleeves rolled to the elbow",
     "calca": "brown corduroy trousers"},
    {"id": "palpebra_pesada", "idade": 64,
     "cabelo": "a bald crown with close-cropped white hair at the sides",
     "barba": "a grey moustache trimmed to the lip", "oculos": "",
     "porte": "short and barrel-chested", "rosto": "heavy hooded eyelids",
     "roupa": "a light blue short-sleeve button-down",
     "calca": "grey twill work pants"},
    {"id": "queixo_fendido", "idade": 55,
     "cabelo": "sandy blond hair going grey at the sides", "barba": "clean-shaven",
     "oculos": "gold-rimmed aviator readers", "porte": "broad and thick-necked",
     "rosto": "a strong cleft chin",
     "roupa": "a charcoal henley with the sleeves pushed up",
     "calca": "dark denim jeans"},
    {"id": "aco_sardas", "idade": 60,
     "cabelo": "wavy steel-grey hair worn a little long", "barba": "clean-shaven",
     "oculos": "", "porte": "small and wiry",
     "rosto": "heavy freckling across his nose and cheeks",
     "roupa": "a faded red flannel shirt", "calca": "tan chinos"},
    {"id": "bigode_guidao", "idade": 57,
     "cabelo": "a shaved head", "barba": "a thick grey handlebar moustache",
     "oculos": "", "porte": "tall and rangy",
     "rosto": "leathery skin and a nose broadened flat at the bridge",
     "roupa": "a mustard-yellow snap-button shirt", "calca": "black work trousers"},
    {"id": "dentes_falha", "idade": 66,
     "cabelo": "white hair combed straight back", "barba": "clean-shaven",
     "oculos": "wire bifocals low on his nose",
     "porte": "stooped and narrow through the shoulders",
     "rosto": "a wide gap between his front teeth",
     "roupa": "a cream short-sleeve camp shirt", "calca": "olive cargo pants"},
    {"id": "sinal_olho", "idade": 59,
     "cabelo": "short auburn hair fading to grey",
     "barba": "two days of grey stubble", "oculos": "",
     "porte": "average height and softly built",
     "rosto": "a raised mole at the outer corner of his right eye",
     "roupa": "a slate-blue polo shirt", "calca": "stone-coloured chinos"},
    {"id": "flat_top", "idade": 61,
     "cabelo": "a flat-top cut gone completely white", "barba": "clean-shaven",
     "oculos": "", "porte": "big-framed and heavy through the middle",
     "rosto": "deeply lined skin and very thick greying eyebrows",
     "roupa": "a forest-green fishing shirt with two chest pockets",
     "calca": "khaki shorts"},
    {"id": "mecha_branca", "idade": 63,
     "cabelo": "thick chestnut hair with a bright white streak at the left temple",
     "barba": "a short grey goatee", "oculos": "",
     "porte": "lean and slightly stooped",
     "rosto": "a long jaw and a deep cleft under the lower lip",
     "roupa": "a rust-red pocket tee", "calca": "grey sweatpants"},
    {"id": "corte_sobrancelha", "idade": 65,
     "cabelo": "a close silver crew cut", "barba": "clean-shaven",
     "oculos": "safety glasses pushed up on his forehead",
     "porte": "square and thick-armed",
     "rosto": "a long-healed nick through his right eyebrow",
     "roupa": "a blue-and-white plaid short-sleeve shirt",
     "calca": "brown canvas work pants"},
    {"id": "costeleta_larga", "idade": 68,
     "cabelo": "white hair parted at the side",
     "barba": "wide old-fashioned sideburns down to the jaw", "oculos": "",
     "porte": "tall and very thin", "rosto": "weathered skin, sunken cheeks and a high forehead",
     "roupa": "a tan corduroy shirt buttoned to the collar",
     "calca": "dark brown slacks"},
    {"id": "nariz_torto", "idade": 70,
     "cabelo": "thin white hair combed forward",
     "barba": "a white chinstrap beard", "oculos": "thin wire-framed oval glasses",
     "porte": "short and round through the shoulders",
     "rosto": "heavily creased skin and a nose broken and set crooked years ago",
     "roupa": "a pale grey flannel shirt", "calca": "navy work trousers"},
]

# ⚠️ POOL ESPELHADO por INDICE: mesma idade, mesmos oculos, mesmo porte, mesma
# roupa e mesma calca. So' cabelo/barba/rosto mudam, que e' onde a etnia se le'.
# Espelhar mantem honesta a comparacao entre paginas: a unica variavel que muda
# entre joe e marcus e' a etnia, nunca o figurino.
CORPOS_PROVA_ESCURA = [
    {"id": "prata_barba", "idade": 58,
     "cabelo": "close-cropped silver hair",
     "barba": "a neat white beard along the jaw", "oculos": "",
     "porte": "tall and still square through the shoulders",
     "rosto": "a large dark mole high on his left cheekbone",
     "roupa": "a plain navy short-sleeve work shirt", "calca": "khaki work pants"},
    {"id": "locs_ambar", "idade": 62,
     "cabelo": "salt-and-pepper locs gathered back",
     "barba": "a full white beard trimmed close",
     "oculos": "heavy black rectangular glasses",
     "porte": "heavy-set and thick through the chest",
     "rosto": "deep-set amber eyes under heavy brows",
     "roupa": "a heather-grey pocket tee", "calca": "faded blue jeans"},
    {"id": "fade_covinha", "idade": 56,
     "cabelo": "a close grey fade", "barba": "clean-shaven", "oculos": "",
     "porte": "lean and long-armed",
     "rosto": "sun-weathered skin and a deep vertical dimple in his left cheek",
     "roupa": "an olive canvas shirt with the sleeves rolled to the elbow",
     "calca": "brown corduroy trousers"},
    {"id": "cavanhaque", "idade": 64,
     "cabelo": "a smooth shaved head", "barba": "a neat silver goatee",
     "oculos": "", "porte": "short and barrel-chested",
     "rosto": "heavy hooded eyelids",
     "roupa": "a light blue short-sleeve button-down",
     "calca": "grey twill work pants"},
    {"id": "twists_queixo", "idade": 55,
     "cabelo": "short black twists just starting to grey", "barba": "clean-shaven",
     "oculos": "gold-rimmed aviator readers", "porte": "broad and thick-necked",
     "rosto": "a strong cleft chin",
     "roupa": "a charcoal henley with the sleeves pushed up",
     "calca": "dark denim jeans"},
    {"id": "afro_sardas", "idade": 60,
     "cabelo": "a silver-flecked afro worn low", "barba": "clean-shaven",
     "oculos": "", "porte": "small and wiry",
     "rosto": "heavy freckling across his nose and cheeks",
     "roupa": "a faded red flannel shirt", "calca": "tan chinos"},
    {"id": "careca_bigode", "idade": 57,
     "cabelo": "a bald head", "barba": "a thick grey moustache", "oculos": "",
     "porte": "tall and rangy", "rosto": "leathery skin and a nose broadened flat at the bridge",
     "roupa": "a mustard-yellow snap-button shirt", "calca": "black work trousers"},
    {"id": "branco_falha", "idade": 66,
     "cabelo": "short white hair worn close", "barba": "clean-shaven",
     "oculos": "wire bifocals low on his nose",
     "porte": "stooped and narrow through the shoulders",
     "rosto": "a wide gap between his front teeth",
     "roupa": "a cream short-sleeve camp shirt", "calca": "olive cargo pants"},
    {"id": "hightop_sinal", "idade": 59,
     "cabelo": "a grey high-top fade", "barba": "two days of grey stubble",
     "oculos": "", "porte": "average height and softly built",
     "rosto": "a raised mole at the outer corner of his right eye",
     "roupa": "a slate-blue polo shirt", "calca": "stone-coloured chinos"},
    {"id": "afro_curto_grisalho", "idade": 61,
     "cabelo": "a short grey afro", "barba": "clean-shaven", "oculos": "",
     "porte": "big-framed and heavy through the middle",
     "rosto": "deeply lined skin and very thick greying eyebrows",
     "roupa": "a forest-green fishing shirt with two chest pockets",
     "calca": "khaki shorts"},
    {"id": "mecha_tempora", "idade": 63,
     "cabelo": "a close grey afro with a bright white patch above the left temple",
     "barba": "a short grey goatee", "oculos": "",
     "porte": "lean and slightly stooped",
     "rosto": "a long jaw and a deep cleft under the lower lip",
     "roupa": "a rust-red pocket tee", "calca": "grey sweatpants"},
    {"id": "barba_corte", "idade": 65,
     "cabelo": "a close grey crew cut", "barba": "a neat grey beard",
     "oculos": "safety glasses pushed up on his forehead",
     "porte": "square and thick-armed",
     "rosto": "a long-healed nick through his right eyebrow",
     "roupa": "a blue-and-white plaid short-sleeve shirt",
     "calca": "brown canvas work pants"},
    {"id": "costeleta_grisalha", "idade": 68,
     "cabelo": "close white hair parted at the side",
     "barba": "wide old-fashioned sideburns down to the jaw", "oculos": "",
     "porte": "tall and very thin", "rosto": "weathered skin, sunken cheeks and a high forehead",
     "roupa": "a tan corduroy shirt buttoned to the collar",
     "calca": "dark brown slacks"},
    {"id": "nariz_torto_escuro", "idade": 70,
     "cabelo": "thin white hair worn close", "barba": "a white chinstrap beard",
     "oculos": "thin wire-framed oval glasses",
     "porte": "short and round through the shoulders",
     "rosto": "heavily creased skin and a nose broken and set crooked years ago",
     "roupa": "a pale grey flannel shirt", "calca": "navy work trousers"},
]


def homens_de(pagina):
    """O CORPO-PROVA casa com o avatar da pagina. Congruencia inviolavel."""
    return CORPOS_PROVA_CLARA if "white" in ETNIA[pagina] else CORPOS_PROVA_ESCURA


def mulheres_de(pagina):
    """A narradora e' SOLTA: pool unico, a pagina nao filtra nada.

    Existe para deixar a excecao explicita em codigo: e' a UNICA vez que "etnia
    do REF = etnia do avatar" nao vale, e vale porque neste angulo o REF nao e'
    o avatar — o avatar e' o homem que segura a prova na cena 3.
    """
    return NARRADORAS


# ---------------------------------------------------------------------------
# EIXOS VISUAIS
# ---------------------------------------------------------------------------
# ⭐ O EIXO DO AGENTE — O PROP QUE RESSUSCITA.
# R1: o IMAGE e' o primeiro frame = estado ANTES. Todos comecam PEQUENOS e EM
# PE', base SEGURA NA MAO dela sobre a superficie (R4). Prop ja' grande nao tem
# pra onde crescer.
# ⛔ PENDENCIA ABERTA, ALCADA DO ED (2026-08-02): as 14 entradas abaixo foram
# escritas sob a "R4-emenda" que mandava o prop se equilibrar SOZINHO — 14 de 14
# dizem `standing on its cut end`. A emenda foi REVOGADA no primeiro render (o
# prop crescia para dentro da mesa), e agora a mao dela sustenta. As entradas
# continuam funcionando, mas o pool inteiro esta' deixando de usar o estado
# MURCHO que a R1 pede e que voltou a ser possivel. Trocar isso e' cena/copy.
# ⚠️ A ESCALA DIFERENCIAL esta' embutida nos dois estados, com regua no quadro:
#   `antes`  = no longer than her palm and as thick as her wrist   (razao ~2,0)
#   `depois` = as long as her forearm and still no thicker than her wrist
# comprimento ~2,3x, largura CONSTANTE. ⛔ A largura NUNCA se redeclara maior.
# `topo` e' a peca que reaparece la' em cima no frame do reconhecimento
# (f121-123 da fonte) e que cresce MENOS — e' essa desproporcao que vende
# "alongou" em vez de "inflou".
# `tom` pareia por CONTRASTE com a substancia (RS15): o po' tem de virar ESTRIA
# visivel, que e' a explicacao fisica do morph que a imagem entrega sozinha.
# ⛔ Geoduck e marisco FORA (R5 + prior dominante: queimou 5 tentativas seguidas;
# contra prior dominante negacao verbal nao vence).
# ⛔ `comically large` (R6) so' vale para prop que NASCE grande, nunca como
# resultado; `absurdly oversized` e' selo 🔴 sempre.
PROPS_MURCHOS = [
    {"id": "berinjela", "nome": "eggplant", "tom": "escuro",
     "topo": "its green star-shaped crown", "negacao": "",
     "antes": "a small dark-purple eggplant standing upright on its own base with the crown pointing up, no longer than her palm and as thick as her wrist",
     "depois": "as long as her forearm and still no thicker than her wrist, its sides running almost parallel",
     "dele": "a deep-purple eggplant as long as his forearm and no thicker than his wrist, the crown still pointing up"},
    {"id": "pepino", "nome": "cucumber", "tom": "escuro",
     "topo": "its pale blunt end",
     "negacao": "No snake, no worm, no eel, nothing alive, nothing with a face.",
     "antes": "a short stubby pickling cucumber standing on its cut end, dark green and dull, no longer than her palm and as thick as her wrist",
     "depois": "as long as her forearm and still no thicker than her wrist, its sides running almost parallel",
     "dele": "a long smooth dark-green cucumber as long as his forearm and no thicker than his wrist"},
    {"id": "cenoura", "nome": "carrot", "tom": "escuro",
     "topo": "its cut green stem-top", "negacao": "",
     "antes": "a short fat carrot standing on its wide cut top with the tip in the air, the skin still rough, no longer than her palm and as thick as her wrist",
     "depois": "as long as her forearm and still no thicker than her wrist, tapering evenly to the tip",
     "dele": "a large raw carrot as long as his forearm and no thicker than his wrist, the skin still rough"},
    {"id": "daikon", "nome": "daikon", "tom": "claro",
     "topo": "its trimmed leaf stub",
     "negacao": "No snake, no worm, no tentacle, nothing alive, nothing with a face.",
     "antes": "a short white daikon radish standing on its cut crown with the tapered end pointing up, no longer than her palm and as thick as her wrist",
     "depois": "as long as her forearm and still no thicker than her wrist, straight from base to tip",
     "dele": "a pale daikon radish as long as his forearm and no thicker than his wrist, the tapered end pointing up"},
    {"id": "pastinaga", "nome": "parsnip", "tom": "claro",
     "topo": "its wide flat crown", "negacao": "",
     "antes": "a short cream-coloured parsnip standing on its wide crown with the tapered end up, no longer than her palm and as thick as her wrist",
     "depois": "as long as her forearm and still no thicker than her wrist, the taper stretched out long",
     "dele": "a thick cream-coloured parsnip as long as his forearm and no thicker than his wrist"},
    {"id": "linguica", "nome": "sausage", "tom": "escuro",
     "topo": "its twisted tied end",
     "negacao": "No snake, no worm, no eel, no tentacle, nothing alive, nothing with a face.",
     "antes": "a short thick smoked sausage link standing on one cut end, the casing taut and dark, no longer than her palm and as thick as her wrist",
     "depois": "as long as her forearm and still no thicker than her wrist, the casing smooth down its whole length",
     "dele": "a thick smoked sausage link as long as his forearm and no thicker than his wrist"},
    {"id": "milho", "nome": "corn", "tom": "claro",
     "topo": "its tapered silk end", "negacao": "",
     "antes": "a stubby ear of sweet corn stripped clean of its husk, standing on its cut stalk end, kernels tight and glossy, no longer than her palm and as thick as her wrist",
     "depois": "as long as her forearm and still no thicker than her wrist, the rows of kernels running unbroken to the tip",
     "dele": "an ear of sweet corn stripped clean of its husk, as long as his forearm and no thicker than his wrist"},
    {"id": "abobrinha", "nome": "zucchini", "tom": "escuro",
     "topo": "its cut stem end", "negacao": "",
     "antes": "a short round-ended zucchini standing on its cut stem end, dark green and matte, no longer than her palm and as thick as her wrist",
     "depois": "as long as her forearm and still no thicker than her wrist, its sides running almost parallel",
     "dele": "a long dark-green zucchini as long as his forearm and no thicker than his wrist"},
    {"id": "batata_doce", "nome": "sweet potato", "tom": "escuro",
     "topo": "its tapered root tip", "negacao": "",
     "antes": "a short round sweet potato standing on its flat cut end with the tapered tip up, deep copper skin, no longer than her palm and as thick as her wrist",
     "depois": "as long as her forearm and still no thicker than her wrist, the taper drawn out long",
     "dele": "a long sweet potato as long as his forearm and no thicker than his wrist, the tapered end pointing up"},
    {"id": "calabaza", "nome": "squash", "tom": "claro",
     "topo": "its cut stem crown", "negacao": "",
     "antes": "the short solid neck of a butternut squash standing upright on its cut base, pale tan and matte, no longer than her palm and as thick as her wrist",
     "depois": "as long as her forearm and still no thicker than her wrist, straight and even the whole way",
     "dele": "the long solid neck of a butternut squash, as long as his forearm and no thicker than his wrist"},
    {"id": "banana", "nome": "banana", "tom": "claro",
     "topo": "its dark stem tip", "negacao": "",
     "antes": "a short stubby banana standing on its cut end with the stem tip up, the skin yellow and lightly spotted, no longer than her palm and as thick as her wrist",
     "depois": "as long as her forearm and still no thicker than her wrist, the curve pulled almost straight",
     "dele": "a ripe banana as long as his forearm and no thicker than his wrist, the skin yellow and lightly spotted"},
    {"id": "mandioca", "nome": "cassava", "tom": "escuro",
     "topo": "its cut pale end", "negacao": "",
     "antes": "a short length of cassava root standing on one cut end, the brown bark rough and dry, no longer than her palm and as thick as her wrist",
     "depois": "as long as her forearm and still no thicker than her wrist, the bark unbroken to the top",
     "dele": "a length of cassava root as long as his forearm and no thicker than his wrist, the brown bark rough and dry"},
    {"id": "aspargo", "nome": "asparagus", "tom": "escuro",
     "topo": "its tight scaled head", "negacao": "",
     "antes": "a single jumbo asparagus spear standing on its trimmed base with the head up, deep green, no longer than her palm and as thick as two of her fingers",
     "depois": "as long as her forearm and still no thicker than two of her fingers, straight from base to head",
     "dele": "a jumbo asparagus spear as long as his forearm and no thicker than two of his fingers"},
    {"id": "alho_poro", "nome": "leek", "tom": "claro",
     "topo": "its dark green leaf top", "negacao": "",
     "antes": "a short trimmed leek standing on its cut root end, the white shaft banded pale green, no longer than her palm and as thick as her wrist",
     "depois": "as long as her forearm and still no thicker than her wrist, the white shaft drawn out long",
     "dele": "a trimmed leek as long as his forearm and no thicker than his wrist, the white shaft banded pale green"},
]

# A SUBSTANCIA DESPEJADA — o que cai por cima.
# ⚠️ TODAS sao SECAS e granulosas, e nao por gosto: as tres mecanicas medidas
# dependem disso — o jato-mascara (R8) precisa de coluna OPACA, o MONTE na mesa
# e' o CRONOMETRO, e a ESTRIA vertical no prop crescido e' a explicacao fisica do
# morph (a mesma quantidade de po' numa area 2,3x maior vira listra em vez de
# capa).
# ⛔ P12: recipiente por FORMA, virado de boca pra baixo, zero marca. A caixa
# laranja de bicarbonato da fonte fica legivel o hook inteiro e e' o pior caso do
# garimpo.
# ⚠️ `fala` tem no maximo 2 palavras — o pior caso do teto da cena 1 depende
# disso. `tom` pareia por CONTRASTE com o prop (RS15).
SUBSTANCIAS = [
    {"id": "bicarbonato", "fala": "baking soda", "tom": "claro",
     "caixa": "a plain pale cardboard carton of fine white powder, turned mouth-down in her raised hand",
     "jato": "a steady column of fine white powder",
     "monte": "a ring of white powder spreading into a wide flat mound",
     "capa": "its whole surface gone chalk-white",
     "estria": "white streaks running down from its shoulders over two thirds of its length"},
    {"id": "farinha", "fala": "flour", "tom": "claro",
     "caixa": "a plain paper sack of soft white flour, the top rolled back and turned mouth-down in her raised hand",
     "jato": "a soft column of white flour",
     "monte": "a ring of flour spreading into a wide flat mound",
     "capa": "its whole surface floured over matte white",
     "estria": "soft white streaks running down from its shoulders over two thirds of its length"},
    {"id": "amido", "fala": "cornstarch", "tom": "claro",
     "caixa": "a plain white cardboard box of very fine bright-white powder, turned mouth-down in her raised hand",
     "jato": "a dense column of very fine bright-white powder",
     "monte": "a ring of bright-white powder spreading into a wide flat mound",
     "capa": "its whole surface packed bright white",
     "estria": "bright white streaks running down from its shoulders over two thirds of its length"},
    {"id": "sal", "fala": "sea salt", "tom": "claro",
     "caixa": "a plain cardboard cylinder of coarse white crystals, turned mouth-down in her raised hand",
     "jato": "a rattling column of coarse white crystals",
     "monte": "a ring of coarse crystals spreading into a wide flat mound",
     "capa": "its whole surface crusted over in coarse white grains",
     "estria": "lines of coarse white grains running down from its shoulders over two thirds of its length"},
    {"id": "acucar", "fala": "sugar", "tom": "claro",
     "caixa": "a plain glass canister of white granulated sugar, turned mouth-down in her raised hand",
     "jato": "a bright column of granulated sugar",
     "monte": "a ring of sugar spreading into a wide flat mound",
     "capa": "its whole surface sugared over in a solid white coat",
     "estria": "glittering white streaks running down from its shoulders over two thirds of its length"},
    {"id": "leite_po", "fala": "powdered milk", "tom": "claro",
     "caixa": "a plain unlabelled tin of chalk-white powder, turned mouth-down in her raised hand",
     "jato": "a thick column of chalk-white powder",
     "monte": "a ring of chalk-white powder spreading into a wide flat mound",
     "capa": "its whole surface gone flat chalk-white",
     "estria": "chalk-white streaks running down from its shoulders over two thirds of its length"},
    {"id": "fuba", "fala": "cornmeal", "tom": "claro",
     "caixa": "a plain cloth sack of pale yellow meal, turned mouth-down in her raised hand",
     "jato": "a grainy column of pale yellow meal",
     "monte": "a ring of pale yellow meal spreading into a wide flat mound",
     "capa": "its whole surface covered in pale yellow meal",
     "estria": "pale yellow streaks running down from its shoulders over two thirds of its length"},
    {"id": "aveia", "fala": "oat flour", "tom": "claro",
     "caixa": "a plain kraft-paper bag of pale oat flour, turned mouth-down in her raised hand",
     "jato": "a soft column of pale oat flour",
     "monte": "a ring of oat flour spreading into a wide flat mound",
     "capa": "its whole surface dusted over pale oatmeal grey",
     "estria": "pale oatmeal streaks running down from its shoulders over two thirds of its length"},
    {"id": "gergelim", "fala": "sesame seed", "tom": "claro",
     "caixa": "a plain glass jar of pale sesame seed, turned mouth-down in her raised hand",
     "jato": "a hissing column of pale sesame seed",
     "monte": "a ring of pale seed spreading into a wide flat mound",
     "capa": "its whole surface stuck over with pale seed",
     "estria": "lines of pale seed running down from its shoulders over two thirds of its length"},
    {"id": "canela", "fala": "cinnamon", "tom": "escuro",
     "caixa": "a plain unlabelled tin of red-brown ground cinnamon, turned mouth-down in her raised hand",
     "jato": "a fine column of red-brown ground cinnamon",
     "monte": "a ring of red-brown powder spreading into a wide flat mound",
     "capa": "its whole surface gone flat red-brown",
     "estria": "red-brown streaks running down from its shoulders over two thirds of its length"},
    {"id": "cacau", "fala": "cocoa", "tom": "escuro",
     "caixa": "a plain unlabelled tin of dark unsweetened cocoa powder, turned mouth-down in her raised hand",
     "jato": "a dark column of unsweetened cocoa powder",
     "monte": "a ring of dark powder spreading into a wide flat mound",
     "capa": "its whole surface gone matte dark brown",
     "estria": "dark brown streaks running down from its shoulders over two thirds of its length"},
    {"id": "cafe", "fala": "ground coffee", "tom": "escuro",
     "caixa": "a plain kraft-paper bag of dark ground coffee, turned mouth-down in her raised hand",
     "jato": "a coarse column of dark ground coffee",
     "monte": "a ring of dark grounds spreading into a wide flat mound",
     "capa": "its whole surface packed over in dark grounds",
     "estria": "dark coffee streaks running down from its shoulders over two thirds of its length"},
    {"id": "papoula", "fala": "poppy seed", "tom": "escuro",
     "caixa": "a plain glass jar of tiny blue-black poppy seed, turned mouth-down in her raised hand",
     "jato": "a hissing column of tiny blue-black seed",
     "monte": "a ring of blue-black seed spreading into a wide flat mound",
     "capa": "its whole surface stuck over with blue-black seed",
     "estria": "lines of blue-black seed running down from its shoulders over two thirds of its length"},
    {"id": "paprica", "fala": "paprika", "tom": "escuro",
     "caixa": "a plain unlabelled tin of deep red paprika, turned mouth-down in her raised hand",
     "jato": "a fine column of deep red paprika",
     "monte": "a ring of deep red powder spreading into a wide flat mound",
     "capa": "its whole surface gone deep matte red",
     "estria": "deep red streaks running down from its shoulders over two thirds of its length"},
]

# O GESTO DO DESPEJO.
# ⚠️ O video ABRE COM O DESPEJO JA' EM ANDAMENTO: nao existe frame de "antes" —
# o espectador entra sem contrato (a mesma economia do TR4).
# ⚠️ O prop NAO esta' em mao nenhuma: esta' solto na superficie, e e' isso que
# torna o crescimento possivel (mao em quadro daria escala e denunciaria o
# efeito). E' o que faz deste o quadro de MENOR risco de composicao de todo o
# garimpo: elenco 1, ela ativa, sem plateia, sem corpo passivo, sem mao de
# terceiro em corpo alheio, sem virilha humana em quadro.
# Slots img: %s = pote da substancia · %s = nome do prop.
DESPEJOS = [
    {"id": "alto_direita", "mao_livre": True,
     "img": "Her right hand holds %s high above the %s, already pouring; her left forearm rests flat on the surface.",
     "take": "Her right hand keeps the carton tipped at the same height and does not lower it."},
    {"id": "duas_maos",
     "img": "Both her hands are on %s, tipped over the %s and already pouring, her elbows braced on the surface.",
     "take": "Both her hands keep the carton tipped at the same height and do not lower it."},
    {"id": "punho_esquerdo",
     "img": "Her left hand holds %s tipped mouth-down over the %s, already pouring; her right hand is flat on the surface beside it.",
     "take": "Her left hand keeps the carton tipped at the same height and does not lower it."},
    {"id": "bem_baixo",
     "img": "Her right hand holds %s barely a hand's width above the %s, already pouring in a short tight stream.",
     "take": "Her right hand keeps the carton at that same low height and does not lift it."},
    {"id": "braco_esticado",
     "img": "Her right arm is stretched out straight, %s tipped mouth-down well above the %s and already pouring.",
     "take": "Her arm stays stretched out at the same height and does not bend."},
    {"id": "ombro_alto",
     "img": "Her right hand holds %s up level with her own shoulder, tipped over the %s and already pouring.",
     "take": "Her hand stays level with her shoulder and does not drop."},
    {"id": "batendo", "mao_livre": True,
     "img": "Her right hand holds %s over the %s, already pouring, while her left hand taps the side of it to keep it running.",
     "take": "Her left hand keeps tapping the same spot and her right hand does not lower the carton."},
    {"id": "cotovelo_apoiado",
     "img": "Her right elbow is planted on the surface and her hand holds %s tipped over the %s, already pouring.",
     "take": "Her elbow stays planted and her hand does not lower the carton."},
    {"id": "colher_livre", "mao_livre": True,
     "img": "Her right hand holds %s tipped over the %s, already pouring; a wooden spoon is held idle in her left hand.",
     "take": "Her right hand keeps the carton tipped at the same height and the spoon in her left hand never moves."},
    {"id": "peito",
     "img": "Her right hand holds %s at the height of her own chest, tipped over the %s and already pouring.",
     "take": "Her hand stays at chest height and does not drop."},
    {"id": "circulo",
     "img": "Her right hand holds %s tipped over the %s, already pouring, moving in a slow small circle above it.",
     "take": "Her hand keeps making the same small circle at the same height for the whole shot."},
    {"id": "mao_em_concha", "mao_livre": True,
     "img": "Her right hand holds %s tipped over the %s, already pouring, while her cupped left hand catches what misses.",
     "take": "Her cupped left hand stays where it is and her right hand does not lower the carton."},
]

# ⭐ A PLATEIA COLAPSADA NO ROSTO DELA (achado ④). Encaixa no slot de
# RS_PLATEIA_INTERNA_TAKE, logo antes de `, the way a studio audience reacts to a
# punchline`. Cumpre a R3: sem reacao le' como glitch de IA; com reacao le' como
# milagre.
# ⛔ zero `mouth open` / `lips parted` / `open-mouthed` / `tongue`: a reacao entra
# por sobrancelha, olho arregalado e gesto parado.
# ⛔⛔ E DESDE 2026-08-02 A REACAO E' DE ROSTO E TRONCO, NUNCA DE MAO. Com a R4
# restaurada as DUAS maos estao ocupadas — uma segura a base do prop, a outra
# despeja — entao `one hand goes flat on her own chest` manda o modelo largar o
# prop no meio do crescimento, que e' o unico jeito de ele obedecer. Foi
# exatamente o que o render de 2026-08-02 fez: a mao subiu ao peito, o pote
# sumiu e a banana ficou equilibrada sozinha.
# ⚠️ As entradas de mao NAO foram apagadas — string validada e' constante, e
# elas voltam a valer em qualquer variante sem prop na mao. Sao FILTRADAS no
# sorteio pelo campo `maos`.
REACOES = [
    {"id": "sobrancelhas_altas",
     "desc": "her eyebrows shoot up and stop there and her eyes stretch wide"},
    {"id": "queixo_recuado",
     "desc": "her chin pulls back into her neck, her eyebrows up, her eyes wide and fixed"},
    {"id": "olhos_na_lente",
     "desc": "her eyes stretch wide and turn straight to the lens, eyebrows high"},
    {"id": "testa_franzida",
     "desc": "her forehead pulls into deep horizontal lines under raised brows, her eyes wide"},
    {"id": "mao_no_rosto", "maos": True,
     "desc": "one hand stops halfway to her own face, fingers spread, her eyes wide"},
    {"id": "sobrancelha_unica",
     "desc": "one eyebrow drives far higher than the other and both her eyes go wide"},
    {"id": "riso_preso",
     "desc": "her cheeks push up and her eyes crease shut at the corners, caught mid-laugh"},
    {"id": "mao_no_peito", "maos": True,
     "desc": "one hand goes flat on her own chest, her eyebrows high and her eyes wide"},
    {"id": "cabeca_inclinada",
     "desc": "her head tips to one side, eyebrows up, eyes wide and unblinking"},
    {"id": "punho_no_queixo", "maos": True,
     "desc": "one fist stops just under her chin, knuckles up, her eyes wide above it"},
    {"id": "ombros_altos",
     "desc": "her shoulders come up around her ears, eyebrows high, eyes wide and staring"},
    {"id": "dedo_parado", "maos": True,
     "desc": "one index finger stops mid-point at nothing, her eyes wide and her brows high"},
    {"id": "sobrancelhas_juntas",
     "desc": "both eyebrows drive up and pinch together, her eyes wide, caught mid-word"},
    {"id": "recuo_tronco", "maos": True,
     "desc": "she rocks back a hand's width from the surface, eyebrows high, eyes wide and locked"},
]

# ⭐ A ANALOGIA FISICA — elemento 2 da coreografia ("o Veo executa processo
# conhecido muito melhor que adjetivo").
# ⚠️ E ela e' a TENSAO MAIS DURA DO PROJETO, registrada e nao escondida: a unica
# analogia 🟢 VALIDADA EM RENDER (`fire hose being filled with water pressure`,
# Joe/geoduck) descreve INFLACAO — que e' exatamente o que a R2-emenda proibe,
# porque escala uniforme le' como inchaco. As 10 da familia EXTENSAO (uma ponta
# fixa, a outra viaja, espessura constante) sao o default por forca da emenda; as
# 4 de PRESSAO ficam sob `--analogia pressao` porque a primeira delas e' a unica
# com selo verde em render. ⚠️ Nenhuma das 10 novas passou por render: 🟡.
# ⚠️ A analogia aponta para FORA da cena (licao do TROCA: analogia circular nao
# desambigua nada) — nenhuma das 14 e' de cozinha.
ANALOGIAS = [
    {"id": "trena", "familia": "extensao",
     "desc": "the way a carpenter's tape runs up out of its case when the blade is pushed out"},
    {"id": "antena", "familia": "extensao",
     "desc": "the way a telescoping radio antenna draws up out of its own base"},
    {"id": "tripe", "familia": "extensao",
     "desc": "the way a tripod leg is drawn out to full length from a fixed foot"},
    {"id": "vara_pesca", "familia": "extensao",
     "desc": "the way a fishing rod slides up out of its own handle"},
    {"id": "bomba_pneu", "familia": "extensao",
     "desc": "the way a bicycle pump handle draws up out of its barrel"},
    {"id": "antena_carro", "familia": "extensao",
     "desc": "the way a car aerial rises out of the wing without getting any thicker"},
    {"id": "cabo_piscina", "familia": "extensao",
     "desc": "the way a telescopic pool pole is pushed out to reach the far end"},
    {"id": "cabo_rolo", "familia": "extensao",
     "desc": "the way a paint roller extension pole runs out one section at a time"},
    {"id": "estante_partitura", "familia": "extensao",
     "desc": "the way a music stand is raised on its own column"},
    {"id": "pedestal_microfone", "familia": "extensao",
     "desc": "the way a boom microphone stand is run up to full height"},
    {"id": "mangueira_incendio", "familia": "pressao",
     "desc": "the way a flat fire hose fills with water pressure"},
    {"id": "boneco_inflavel", "familia": "pressao",
     "desc": "the way an inflatable air dancer at a car lot fills from the fan below"},
    {"id": "balao_longo", "familia": "pressao",
     "desc": "the way a long balloon fills from the neck outward"},
    {"id": "camara_ar", "familia": "pressao",
     "desc": "the way a flat inner tube fills from the valve"},
]

# CENARIOS — 14 CLASSES diferentes, nao decoracao trocada.
# ⛔ ES13: o alibi de autoridade se faz por FORMA, nunca por TEXTO — os dois
# diplomas da fonte ficam legiveis o video inteiro e sao DOIS problemas
# (superficie de bloqueio P12 + credencial DECLARADA, a primeira linha da cerca
# do ELA_DIAGNOSTICA). Entram como `two framed documents in dark wood frames with
# gold foil seals`: mesma imagem, zero texto.
# ⛔ `hardback spines`, NUNCA `hardback books` (RS14).
# ⛔ Nunca escrever que o texto e' ilegivel — negacao e' municao.
# ✅ Bandeira dos EUA em todos, em forma diferente cada vez (esta' no catalogo,
# nao e' marca). ⛔ Banidos: planta, carpete, caixa triangular de bandeira
# dobrada, ima decorativo.
# ⚠️ `re_ancora` existe porque a entropia COLAPSA entre o spec e o prompt: sem
# ela metade do lote diria so' "in the same kitchen" nas cenas 2 e 3 e a bandeira
# sumiria do quadro.
CENARIOS = [
    {"id": "escritorio_diplomas", "bancada": "desk", "curto": "office",
     "set": "a home office with a full wall of dark hardback spines with gold detailing, two framed documents in dark wood frames with gold foil seals and a US flag on a floor stand in the corner",
     "re_ancora": "the same home office, the wall of dark hardback spines and the two framed documents behind her and the US flag on its floor stand",
     "luz": "warm lamp light with soft daylight from a window frame-left."},
    {"id": "escritorio_painel", "bancada": "desk", "curto": "study",
     "set": "a wood-panelled home study with a shelf of dark hardback spines, a green glass desk lamp and a small US flag on a short pole in a brass stand",
     "re_ancora": "the same wood-panelled study, the shelf of dark hardback spines behind her and the small US flag in its brass stand",
     "luz": "warm pooled lamp light with dim daylight from behind her."},
    {"id": "sala_estante", "bancada": "side table", "curto": "den",
     "set": "a den with floor-to-ceiling shelves of dark hardback spines, a worn leather wing chair and a US flag on a floor stand beside the doorway",
     "re_ancora": "the same den, the floor-to-ceiling shelves of dark hardback spines behind her and the US flag on its floor stand by the doorway",
     "luz": "low warm lamp light and one shaft of daylight from frame-right."},
    {"id": "cozinha_modesta", "bancada": "counter", "curto": "kitchen",
     "set": "a small older American kitchen with laminate counters and a window over the sink, a small US flag standing in a jar on the sill",
     "re_ancora": "the same small older kitchen, the small US flag still standing in its jar on the sill",
     "luz": "flat grey daylight from the window over the sink."},
    {"id": "cozinha_ilha", "bancada": "island", "curto": "kitchen",
     "set": "an open-plan American kitchen with a white marble island, a living room out of focus behind her and a small US flag on a stand at the end of the island",
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
    {"id": "alpendre", "bancada": "table", "curto": "porch",
     "set": "a screened American back porch with a heavy wooden table and a US flag hanging from a bracket on the post",
     "re_ancora": "the same screened back porch, the heavy wooden table and the US flag still hanging from its bracket on the post",
     "luz": "bright shaded daylight coming through the screens."},
    {"id": "garagem", "bancada": "workbench", "curto": "garage",
     "set": "a home garage workbench with a pegboard of tools behind, a rolling chest and a US flag hung flat on the pegboard",
     "re_ancora": "the same home garage, the pegboard of tools behind her and the US flag still hung flat on it",
     "luz": "cool fluorescent strip light overhead."},
    {"id": "porao_oficina", "bancada": "bench top", "curto": "basement shop",
     "set": "a basement workshop with a heavy scarred bench top, a vice bolted to one end, a rack of clamps on the wall and a US flag hung flat above the rack",
     "re_ancora": "the same basement workshop, the vice at the end of the bench and the US flag still hung flat above the rack of clamps",
     "luz": "a single caged bulb overhead and no daylight."},
    {"id": "copa_igreja", "bancada": "counter", "curto": "hall",
     "set": "a plain community hall kitchen with a stainless counter, a stack of folding chairs behind and a small US flag on the pass-through window",
     "re_ancora": "the same community hall kitchen, the stack of folding chairs behind her and the small US flag still on the pass-through window",
     "luz": "even overhead fluorescent light."},
    {"id": "rv", "bancada": "counter", "curto": "galley",
     "set": "the galley of a parked American RV, wood-veneer cabinets, a small sink and a US flag decal beside the window",
     "re_ancora": "the same RV galley, wood-veneer cabinets and the US flag decal still beside the window",
     "luz": "warm afternoon light through the RV window frame-right."},
]

# A BANCADA-RECIBO (TR7/ES8): a boca cita 1 ingrediente, a imagem mostra 3-4,
# nunca tocados e nunca mencionados. E' o LASTRO do `full recipe` — prometiamos a
# receita completa sem nunca provar em imagem que existe uma.
# ⚠️ `cabecas` faz o sorteio EVITAR POR CONSTRUCAO a colisao com DOIS eixos: a
# receita `{r}` E a substancia `{s}`. Com substancia=canela, uma bancada de canela
# poria na imagem justamente o que a fala ja' citou — e recibo que repete a boca
# deixa de ser recibo.
# ⛔ Zero marca legivel, e a ausencia declarada pela AFIRMATIVA (`plain`), nunca
# `with no label`.
BANCADAS = [
    {"id": "po_gengibre", "cabecas": ("ginger",),
     "itens": "a plain glass jar of fine white powder, a knob of fresh ginger root and a wooden spoon"},
    {"id": "limao_sal", "cabecas": ("lemon", "salt"),
     "itens": "a rustic ceramic bowl, a halved lemon face-up and a small dish of coarse salt"},
    {"id": "canela_ambar", "cabecas": ("cinnamon",),
     "itens": "an unlabelled amber bottle, three cinnamon sticks tied with twine and a shallow saucer"},
    {"id": "melaco_sementes", "cabecas": ("syrup", "molasses", "seed"),
     "itens": "a stoneware crock of dark syrup with the lid tipped beside it, a paring knife and a scatter of black seeds"},
    {"id": "nozes_nozmoscada", "cabecas": ("walnut", "nutmeg"),
     "itens": "a small white bowl of shelled walnuts, a whole nutmeg on a wooden board and a folded cloth"},
    {"id": "folhas_coador", "cabecas": (),
     "itens": "a wide-mouth jar of dried leaves, a metal strainer and a chipped enamel mug"},
    {"id": "pilao_beterraba", "cabecas": ("beet", "beetroot"),
     "itens": "a wooden mortar and pestle with something ground pale inside, a cut beetroot and a folded paper packet"},
    {"id": "jarra_alho", "cabecas": ("garlic",),
     "itens": "a glass measuring jug half full of clear liquid, a whole head of garlic and a long-handled spoon"},
    {"id": "figos_lata", "cabecas": ("fig",),
     "itens": "a saucer of dried figs, a squat unlabelled tin with the lid resting on it and a wooden scoop"},
    {"id": "salsa_conta_gotas", "cabecas": ("parsley",),
     "itens": "a bundle of fresh parsley tied at the stems, a small brown bottle with a dropper and a china teacup"},
    {"id": "aveia_casca", "cabecas": ("oat", "cinnamon"),
     "itens": "a shallow bowl of raw oats, a stick of cinnamon bark and a slotted metal spoon"},
    {"id": "roma_pilao", "cabecas": ("pomegranate",),
     "itens": "a halved pomegranate face-up on a board, a small stone pestle and a folded linen cloth"},
    {"id": "cacau_mel", "cabecas": ("cacao", "cocoa", "honey"),
     "itens": "a plain tin of dark powder, a squat jar of thick amber syrup and a bone-handled spoon"},
    {"id": "pimenta_almofariz", "cabecas": ("cayenne", "pepper", "paprika"),
     "itens": "a saucer of coarse orange grains, a small stone mortar and a stack of three unlabelled tins"},
]

# A RECEITA da cena 2 — o `{r}`, o ingrediente que a boca cita.
# ⚠️ EIXO SEPARADO da SUBSTANCIA de proposito: a substancia do hook e' a ISCA
# despejada no PROXY; a receita e' o PREPARO que vai no copo.
# ⭐⭐ E aqui mora o achado mais duro do mapa: a receita da fonte e' TOPICA SOBRE
# O CORPO (`apply it directly and leave it on for ten minutes before bed`, com
# caiena). Capsaicina em mucosa genital por dez minutos e' queimadura quimica —
# ⛔ isso nao e' risco de render, e' risco de DANO REAL: nao se resolve
# regerando, nao se resolve trocando a forma de dizer, e nao e' materia de alcada
# de copy, e' materia de NAO FAZER (RS9). A nossa topica toca o PROXY (TR5); esta
# aqui e' da familia PREPARO/BEBER, que e' o que os dois outros reels da mesma
# pagina fazem.
# ⛔ ZERO medida, ZERO duracao, ZERO horario: forma e gesto.
# ⚠️ `fisica` vem ACOPLADA a receita — correcao do bug do ESCANDALO, onde fisica
# sorteada independente entregava "a flat opaque gold" sobre po' vermelho e "the
# powder goes under" sobre dois paus de canela.
RECEITAS = [
    {"id": "beterraba", "fala": "beet powder", "cabecas": ("beet", "beetroot"),
     "img": "a tall glass of warm water with a shallow dish of deep red beet powder beside it",
     "gesto": "her right hand tips the shallow dish of deep red powder into the glass",
     "fisica": "the water turns from clear to magenta to an opaque blood red in the space of two seconds"},
    {"id": "roma", "fala": "pomegranate", "cabecas": ("pomegranate",),
     "img": "a tall glass of warm water with a small glass jug of dark pomegranate juice beside it",
     "gesto": "her right hand pours a thread of dark juice down the inside of the glass",
     "fisica": "a dark spiral winds down through the clear water and holds its shape without breaking"},
    {"id": "mel", "fala": "raw honey", "cabecas": ("honey",),
     "img": "a wide mug of warm water and an open jar of raw honey with a wooden dipper across the rim",
     "gesto": "her right hand lifts the dipper and lets a slow ribbon of honey fall into the mug",
     "fisica": "a slow ribbon sinks whole to the bottom and lies there in a loose coil"},
    {"id": "caiena", "fala": "cayenne", "cabecas": ("cayenne", "pepper"),
     "img": "a tall glass of warm water with a small saucer of coarse orange cayenne beside it",
     "gesto": "her right hand taps the saucer so a fall of coarse orange grains lands on the surface",
     "fisica": "coarse grains float in a raft on the surface and refuse to go under"},
    {"id": "gengibre", "fala": "ginger", "cabecas": ("ginger",),
     "img": "a squat glass of warm water and a knob of fresh ginger root grated into a small dish",
     "gesto": "her right hand scrapes the grated ginger off the dish into the glass with her thumb",
     "fisica": "a fine pale foam climbs the inside of the glass and stays banked against it"},
    {"id": "curcuma", "fala": "turmeric", "cabecas": ("turmeric",),
     "img": "a heavy glass of warm water and a rustic ceramic bowl of deep yellow turmeric paste with a spoon standing in it",
     "gesto": "her right hand lifts the standing spoon of yellow paste and turns it into the water",
     "fisica": "the water goes from clear to a flat opaque gold in one pass of the spoon"},
    {"id": "melaco", "fala": "molasses", "cabecas": ("molasses", "syrup"),
     "img": "a tall glass of warm water and a stoneware crock of dark molasses with a wooden spoon in it",
     "gesto": "her right hand draws the spoon up out of the crock and lets the dark syrup fall in a thread",
     "fisica": "a slow ribbon sinks whole to the bottom and lies there in a loose coil"},
    {"id": "canela", "fala": "cinnamon", "cabecas": ("cinnamon",),
     "img": "a wide mug of warm water and three cinnamon sticks tied with twine lying on the board",
     "gesto": "her right hand snaps a cinnamon stick in half and drops both pieces into the mug",
     "fisica": "a slow brown cloud unwinds from each broken end and sinks through the water"},
    {"id": "limao", "fala": "lemon", "cabecas": ("lemon",),
     "img": "a tall glass of warm water and a lemon halved face-up on the board",
     "gesto": "her right hand squeezes one lemon half over the glass, the pulp collapsing between her fingers",
     "fisica": "small tight bubbles climb the inside of the glass and cling there in lines"},
    {"id": "vinagre", "fala": "cider vinegar", "cabecas": ("vinegar",),
     "img": "a tall glass of warm water and an unlabelled amber bottle tipped against a small dish of cloudy vinegar",
     "gesto": "her right hand tips the amber bottle and lets a pour of cloudy vinegar run down the inside of the glass",
     "fisica": "the liquid separates into two clean bands with a sharp line between them, then folds together"},
    {"id": "melancia", "fala": "watermelon", "cabecas": ("watermelon",),
     "img": "a tall glass of warm water and a wedge of watermelon on the board with the juice pooling under it",
     "gesto": "her right hand presses the wedge against a metal strainer over the glass until the juice runs through",
     "fisica": "the water turns from clear to magenta to an opaque blood red in the space of two seconds"},
    {"id": "alho", "fala": "garlic", "cabecas": ("garlic",),
     "img": "a squat glass of warm water and a whole head of garlic with two cloves already crushed flat beside it",
     "gesto": "her right hand slides the two crushed cloves off the flat of the knife into the glass",
     "fisica": "a fine pale sediment drops out of the liquid and gathers in a ring at the bottom"},
    {"id": "salsa", "fala": "parsley", "cabecas": ("parsley",),
     "img": "a wide mug of warm water and a bundle of fresh parsley tied at the stems",
     "gesto": "her right hand tears a handful of parsley off the bundle and pushes it under the surface",
     # ⛔ `floats back up`, nunca `rises`: `rises` e' da familia de crescimento
     # que a RS6 bane fora do TAKE 01 — e a fisica da receita mora no TAKE 02.
     "fisica": "the green floats back up and holds in a slow turning cloud just under the surface"},
    {"id": "cacau", "fala": "raw cacao", "cabecas": ("cacao", "cocoa"),
     "img": "a heavy glass of warm water and a shallow tin of dark unsweetened cacao powder",
     "gesto": "her right hand shakes the tin so a fall of dark powder lands on the water",
     "fisica": "a slow brown cloud sinks from the surface to the bottom of the glass and settles there"},
]

# COMO A GELATINA APARECE.
# `plantado` = na bancada da cena 2 desde o frame 1 (o reveal nao apresenta nada
# novo: objeto que entra de fora do quadro nao e' premio, e' corte disfarcado);
# `curto` = a referencia de continuidade que volta NA MAO LIVRE dela na cena 3,
# no frame em que a boca diz `gelatin,`; `pousado` = o detalhe forense POR
# MECANISMO.
# ⚠️ O mecanismo NAO e' eixo sorteavel de substancia: e' GELATINA nas doze
# variantes — congruencia inviolavel, o mecanismo do criativo e' o que a VSL
# vende.
# ⛔ E por isso as DOZE nomeiam `gelatin` no `plantado` E no `curto`: com po'
# anonimo o espectador ve' um sache generico no frame da keyword e a coincidencia
# palavra<->objeto desaparece.
# ⛔ Nunca mandar desenhar tampa em tigela: contradicao dentro do proprio IMAGE.
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
     "plantado": "a plain white sachet of pale gelatin powder torn open at the top, standing upright",
     "curto": "the torn-open white sachet of pale gelatin powder",
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
     "plantado": "a torn white sachet of gelatin powder lying flat beside a tumbler of cold water",
     "curto": "the torn white sachet of gelatin powder",
     "pousado": "already poured, the wet spoon lying on the board beside it"},
    {"id": "forma_cubos",
     "plantado": "a shallow metal tray of set amber gelatin scored right through into squares",
     "curto": "the metal tray of amber gelatin squares",
     "pousado": "uncovered, the scoring knife lying on the board beside it"},
    {"id": "tigela_madeira",
     "plantado": "a turned wooden bowl of firm amber gelatin cubes piled above the rim",
     "curto": "the wooden bowl of amber gelatin cubes",
     "pousado": "uncovered, the emptied glass measure standing on the board beside it"},
]


# ---------------------------------------------------------------------------
# COPY — CENA 1: o hook, a leitura do crescimento e o bullet
# ---------------------------------------------------------------------------
# ⭐ CADA hook declara o seu `degrau` da escada de moderacao, e existe
# `--degrau N`: assim uma recusa custa UMA FLAG, nao um redesenho.
# ⛔ O DEGRAU 1 (o literal da fonte, `Pour baking soda on your John-son and watch
# it swell up overnight`) NAO ESTA' NO POOL: ele soma `your <nucleo>` + PRAZO no
# mesmo take de 8s, que e' a composicao exata que derrubou o video do NECROSE por
# "politicas contra a geracao de conteudo nocivo". Ou seja: a fala da fonte, como
# esta', e' reprovada pelo NOSSO PROPRIO linter (RS10) antes de chegar ao Veo.
# ⭐⭐ O DEGRAU 4 E' A ATRIBUICAO, e e' o achado de moderacao proprio deste
# angulo: porque o video vai demolir ou provar a crendice meio segundo depois,
# ela pode ser posta na boca de OUTRA PESSOA — some o imperativo, some a 2a
# pessoa no claim, some a posse da promessa, e nao custa um frame.
# ⛔ Nenhuma com prazo. ⚠️ Numeros por extenso: o Veo soletra algarismo.
HOOKS = [
    {"degrau": 3, "txt": "If you want your {o} doing what that just did, hear me out."},
    {"degrau": 3, "txt": "If you want your {o} to do that, watch this whole thing."},
    {"degrau": 3, "txt": "Want your {o} doing what you just watched? Then stay right here."},
    {"degrau": 3, "txt": "If your {o} still quits on you, this is the one to watch."},
    {"degrau": 3, "txt": "If you want your {o} answering like that, this is where it starts."},
    {"degrau": 3, "txt": "If your {o} has gone quiet on you, watch this all the way."},
    {"degrau": 4, "txt": "They say {s} does this. Watch it happen."},
    {"degrau": 4, "txt": "Every man on this app swears by {s}. Here's why."},
    {"degrau": 4, "txt": "They've been saying {s} for years. Now watch."},
    {"degrau": 4, "txt": "Half the internet swears by {s}. This is what they mean."},
    {"degrau": 4, "txt": "My grandfather swore by {s}. I laughed at him too."},
    {"degrau": 4, "txt": "That one about {s} has been going around forever. Watch."},
    {"degrau": 2, "txt": "Pour {s} on it and watch what your {o} could do."},
    # ⛔ estas duas SAIRAM do degrau 2 em 2026-08-03 e foram para o 5. Elas
    # nomeiam a substancia e o gesto, mas NUNCA dizem que aquilo e' o corpo
    # dele — o espectador tinha de inferir a transferencia. Medido no lote que
    # o operador reprovou: 2 de 8 sorteios fechavam a cena 1 sem uma unica
    # mencao ao orgao. O degrau 2 agora e' 100% transferencia.
    {"degrau": 5, "txt": "{s} on it. That's the whole thing. Watch."},
    {"degrau": 5, "txt": "Two handfuls of {s}, poured straight on. Watch it."},
    # ⭐⭐ A FAMILIA DIRETA — ordem do operador em 2026-08-03, com o take
    # renderizado na mao: "para de fazer copy que nao diz nada com nada".
    # A fonte que ele mandou junto e' brutal e nao pede licenca:
    #     `pour raw honey on your Johnson every night`
    #     `and it will grow 5 inches in one week`
    # ⛔ NAO copiamos aquilo: `every night` e `in one week` sao marcador de
    # PRAZO, e `5 inches` e' promessa de MEDIDA — as duas coisas que derrubaram
    # o video do NECROSE. O que se copia e' a ESTRUTURA: a demo transfere para o
    # corpo dele numa frase so', sem rodeio e sem deixis.
    # ⚠️ E ela e' AFIRMATIVA, nao condicional. A regra antiga so' admitia `your
    # {o}` em condicional ou pergunta; o operador mandou ser direto e a decisao
    # e' dele. O prazo continua BANIDO — e' o prazo que derruba, nao a
    # afirmativa (RS10 cobra a SOMA das duas).
    {"degrau": 2, "txt": "This is what {s} does to your {o}."},
    {"degrau": 2, "txt": "{s} on it. This is what it does to your {o}."},
    {"degrau": 2, "txt": "Watch {s} hit it. Your {o} does the same thing."},
    {"degrau": 2, "txt": "That's {s}, and that's your {o} on it."},
    {"degrau": 2, "txt": "{s} does this. To that, and to your {o}."},
    {"degrau": 5, "txt": "{s}. Every guy has heard of it. Almost nobody knows why."},
    {"degrau": 5, "txt": "Nobody explains what {s} actually does. I will."},
    {"degrau": 5, "txt": "There's a reason men keep {s} in the cupboard."},
    {"degrau": 5, "txt": "{s}. Two dollars a box. Watch what it does."},
]

# ⭐ MODO DEFAULT (`--credibilidade confirma`): colado no crescimento, a fala
# CONFIRMA e TRANSFERE — o crescimento como PROVA, a promessa numerica virando
# imagem. E' a forma validada deste agente (R1-R6 + o arco das 5 cenas).
# ⛔ ZERO afirmacao sobre o corpo do espectador com prazo na mesma cena.
# ⛔ ZERO palavra tecnica: a cena 2 reserva EXATAMENTE UMA, e gastar uma aqui faz
# duas no video.
# ⛔⛔ REESCRITO EM 2026-08-02 POR ORDEM DO OPERADOR — "copy vaga, quem ve o
# video nem entende do que se trata". Medido antes: 10 das 14 entradas NAO
# tinham um unico substantivo concreto. `You just watched the mechanism work.`
# e' meta-fala: declara que houve um mecanismo em vez de dizer QUAL. A fonte, no
# mesmo slot, diz `the cayenne forces your blood vessels to open up`.
# ⭐ A REGRA NOVA: toda entrada nomeia SANGUE, VASO ou PRESSAO. Nenhuma
# sobrevive so' de `that` / `it` / `the mechanism`.
# ⛔ E o vocabulario e' de PROPOSITO o mais chao possivel — `blood`, `vessels`,
# `pressure`, `flow`. `circulation`, `oxygen`, `collagen`, `nitric oxide` e
# `vasodilator` sao as palavras tecnicas da CENA 2, e gastar uma aqui faz duas
# no video.
# ⛔ Zero afirmacao sobre o corpo do espectador com prazo (RS10).
# ⛔⛔ REESCRITO EM 2026-08-03 — SEGUNDA ORDEM DO OPERADOR SOBRE O MESMO SLOT.
# A primeira passada trocou meta-fala (`You just watched the mechanism work`) por
# fisiologia (`Outside it's visible. Inside it's the same blood.`). Ele leu o
# take renderizado e reprovou de novo: fisiologia ainda e' CONVERSA. O molde que
# ele deu e' outro, e e' o de direct response classico:
#     [o que a substancia faz no {o} DELE] -> [o que ELA sente] -> [consequencia]
#     "...when she feels what woke her up at 3:00am... she will never let you
#      stop taking this."
# ⭐ A REGRA NOVA DESTE SLOT: quem sente e' A MULHER, e o que ela sente e'
# SENSORIAL E ESPECIFICO — hora da noite, gesto, silencio, a cara dela. Nao e'
# "ela vai gostar": e' um momento que da' para ver.
# ⛔ Zero fisiologia aqui: `blood`, `pressure`, `vessels` viraram a cena 2 junto
# com a palavra tecnica. Cena 1 e' o corpo dele e a reacao dela, nada mais.
# ⛔ Zero PRAZO (RS10) — `every night`, `in one week`, `overnight` sao o que
# derrubou o NECROSE. Hora da noite em NARRATIVA (`at three in the morning`) nao
# e' posologia: e' quando ela acordou, nao quando ele toma.
CONFIRMACOES = [
    "Then she feels it at three in the morning.",
    "She's going to wake up and find that.",
    "The first time she feels it, she goes quiet.",
    "She'll roll over at two and stop talking.",
    "Watch her face the night she finds out.",
    "She wakes up, feels that, and says nothing.",
    "Her hand lands on it and she freezes.",
    "She finds that in the dark and stares.",
    "She'll feel it before you say one word.",
    "That's what she reaches for at three in the morning.",
    "She won't ask. She'll just look at you.",
    "The night she feels that, she stops sleeping.",
    "She'll notice before you do. They always do.",
    "One night she reaches over and goes still.",
]

# MODO `--credibilidade desmente`: o TR8 do TROCA, variante DESMENTE, literal.
# ⭐ O que este angulo acrescenta a' TR8 e' o OBJETO do desmentido: no TROCA a
# isca desmentida e' VERBAL (8/8 sem crescimento, a promessa e' 100% falada);
# aqui a isca desmentida e' uma ANIMACAO QUE A TELA ENTREGOU. Em uma frase: o
# TROCA desmente uma PROMESSA, este desmente uma PROVA.
# ⚠️ E' isso que licencia o degrau 4 do hook (a atribuicao).
# ⛔ CONSEQUENCIA MECANICA, cobrada por linter (RS17): rodando este pool o video
# fica SEM EVIDENCIA nenhuma ate' a cena 3 — entao a cena 3 e' obrigatoriamente o
# corpo-prova (F12b), nunca a tigela sozinha.
DESMENTIDOS = [
    "You do not actually believe that works, right?",
    "Of course it doesn't. Nothing does that.",
    "You know that's nonsense. So do I.",
    "It doesn't work. It never has.",
    "Look at your own face. Exactly that.",
    "Nope. Never worked on anybody, ever.",
    "Sounds insane, because it is.",
    "Right? Complete garbage, every single word.",
    "You already knew better than that.",
    "That one's been going around for years.",
    "It doesn't. Not one bit of it.",
    "Nobody actually believes that. Not one man.",
    "And it does absolutely nothing. Zero.",
]

# ⭐ O BULLET DA CENA 1 — tipo OBJECAO #11 / NAO-E-SUA-CULPA (Benson §3: culpar
# o sistema e a informacao errada, NUNCA o prospecto). No modo desmente o beat
# anterior e' a unica frase do video que chama o espectador de ingenuo, e um
# bullet de 7 palavras converte a piada em ALIANCA em vez de deixa-la como
# cutucada.
# ⛔ Bullet de CURIOSIDADE nao cabe aqui: o beat 2 ja' abriu o loop, e dois loops
# abertos na mesma respiracao e nenhum fecha.
# ⚠️ 10 das 13 trazem `{o}` — foi a queixa literal do operador no ESCANDALO (0
# dos 9 hooks nomeavam o orgao; a cena 1 nunca dizia o nome da coisa). As 3 sem
# `{o}` existem para quando o HOOK ja' nomeia (ver `_uma_vez_so`).
# ⚠️ E preferem `the {o}` a `your {o}`: a frase fala do VILAO e o orgao aparece
# como OBJETO DO INTERESSE DELE, nunca como diagnostico do corpo de quem assiste.
# ⛔ ZERO marcador de prazo.
#
# ⛔⛔ O CAMPO `cred` — CORRECAO DE 2026-08-02, e e' a mesma mecanica que as
# FUNDIDAS ja' tinham. Sem ele o bullet nao sabia em que modo estava rodando, e
# DUAS entradas emolduram o crescimento como BOATO DE INTERNET — que e'
# exatamente o que o modo `confirma` existe para negar. Sorteio real, seed 42,
# modo default:
#     "...hear me out. You just watched the mechanism work.
#      Half the internet still says it works."
# A cena declara que a prova e' mecanismo e o bullet seguinte a devolve para
# "dizem por ai". Medido antes do conserto: 168 de 400 sorteios no modo padrao
# (42,0%) fechavam a cena 1 desmentindo a propria prova.
# ⚠️ ⛔ NENHUMA entrada foi reescrita, cortada ou renumerada: as 17 continuam
# caractere por caractere como estavam. O que mudou e' EM QUE MODO cada uma pode
# ser sorteada — filtro, como o `voz` das PROVAS e o `cabecas` das BANCADAS.
# ⚠️ `They sold you the age excuse instead.` continua `ambas` de proposito: ela
# e' Benson §3 (culpar o sistema), nao moldura de boato — nao contradiz nada.
# ⛔⛔ REESCRITO EM 2026-08-02, MESMA ORDEM DAS CONFIRMACOES. O bullet tinha
# vilao concreto (medico, corredor de farmacia, propaganda) mas AFIRMAVA QUE
# ALGO FOI SONEGADO SEM NUNCA DIZER O QUE. `Not your fault. Nobody explains the
# {o}.` — explica O QUE sobre ele? `That's not on you. Nobody ever explained
# it.` — "it" nao tem antecedente nenhum, e foi a frase que o operador citou:
# "wtf is she talking about???".
# ⭐ A REGRA NOVA: o bullet nomeia O QUE FOI SONEGADO, nao so' que houve
# sonegacao. `what shuts it down`, `what opens it`, `the cause` — o objeto do
# verbo passa a existir.
# ⛔ E evita `blood`, que e' a palavra do beat anterior: bullet ecoando o beat
# gasta duas das ~16 palavras que sobram na cena e o `_repete` derruba o par.
# ⚠️ Benson §3 preservado em todas: culpa-se o SISTEMA e a informacao errada,
# nunca o prospecto.
BULLETS = [
    # ⭐⭐ A FAMILIA DA CONSEQUENCIA — ordem do operador, 2026-08-03. O molde e'
    # literal dele: "she will never let you stop taking this". O bullet deixa de
    # ser queixa contra o sistema e passa a ser O QUE ACONTECE DEPOIS, na voz
    # dela. E' o fecho do arco que o beat anterior abriu: ela sentiu, e agora e'
    # ela quem nao deixa parar.
    # ⛔ Zero prazo (RS10). Zero medida. Zero fisiologia (e' da cena 2).
    {"cred": "ambas", "txt": "She will never let you stop doing this."},
    {"cred": "ambas", "txt": "She'll be the one hiding the jar."},
    {"cred": "ambas", "txt": "After that, she's the one asking."},
    {"cred": "ambas", "txt": "She'll want to know what changed. Don't tell her."},
    {"cred": "ambas", "txt": "You won't be the one bringing it up anymore."},
    {"cred": "ambas", "txt": "She'll start going to bed early."},
    {"cred": "ambas", "txt": "That's the night she stops rolling away."},
    {"cred": "ambas", "txt": "She'll never let that jar leave the house."},
    # a familia do VILAO (Benson §3) fica, em minoria: ela cabe quando o beat
    # anterior ja' pagou a consequencia e sobra folga de palavra.
    {"cred": "ambas", "txt": "Nobody makes a dime when the {o} works."},
    {"cred": "ambas", "txt": "Your doctor treats the pill, never the {o}."},
    {"cred": "ambas", "txt": "That aisle sells pills, never what opens the {o}."},
    # ⛔⛔ FRASE ORFA — CONSERTO DE 2026-08-03, mesma ordem do operador ("arrume
    # isso em todos os agentes que estao com esse vicio"). `They sold you the
    # age excuse instead.` nomeia a CAUSA (a desculpa da idade) e nao diz
    # desculpa PARA O QUE — o espectador ouve a queixa e nao sabe do que se
    # trata. Agora o alvo entra NA MESMA FRASE.
    # ⚠️ ⛔ O ALVO NAO PODE SER `{o}`: este bullet mora na familia SEM `{o}`, que
    # e' a que o `_montar_falas` sorteia quando o hook JA' nomeou o orgao (a
    # cena 1 nomeia exatamente uma vez — duas em 8 segundos e' bordao). Por
    # isso o alvo e' `going soft`, que diz o que a desculpa encobre sem repetir
    # o substantivo. Custo: 9 palavras contra 7 — cabe no TETO_FALA[1] = 27.
    {"cred": "ambas", "txt": "They sold you the age excuse for going soft."},
    # ⛔ as duas de moldura de BOATO: so' rodam quando a fala ja' desmentiu.
    {"cred": "desmente", "txt": "Half the internet still says it works."},
    {"cred": "desmente", "txt": "That one has been going around for years."},
    # + medido depois do primeiro lote: no degrau 3 os seis hooks nomeiam o
    # orgao, entao a regra de nomea-lo UMA vez por cena deixava a cena 1 com
    # apenas TRES bullets — 182/180/38 em 400 sorteios. Tres opcoes ficam abaixo
    # da barra do operador ("nada menos que os demais agentes SHORT"), e o
    # conserto e' pool, nao regra: mais quatro da mesma familia, todas SEM `{o}`.
    # ⚠️ No degrau 2 (default desde 2026-08-02) so' um dos tres hooks nomeia o
    # orgao, entao as onze de cima voltam a entrar no sorteio padrao.
    {"cred": "ambas", "txt": "She'll ask. Say nothing and do it again."},
    {"cred": "ambas", "txt": "She won't let that stop. Not now."},
    {"cred": "ambas", "txt": "Your doctor was never taught what closes it."},
    {"cred": "ambas", "txt": "Nobody makes a dime telling you what opens it."},
]

# ---------------------------------------------------------------------------
# COPY — CENA 2: a fundida (RECEITA + MECANISMO + VIRADA num folego so')
# ---------------------------------------------------------------------------
# ⛔ TODA entrada carrega o literal minusculo `gelatin trick` — ele mora em cenas
# diferentes em cada agente e TODAS caem no colapso de 5 para 3; sem ele o
# criativo deixa de ser congruente com o que a VSL vende.
# ⛔ TODA entrada carrega `{o}`: com o hook do degrau 4 ou 5 a cena 1 nao nomeia
# o nucleo pela boca do hook, e as cenas 2 e 3 sustentam a cota.
# ⛔ EXATAMENTE UMA palavra tecnica (vasodilator / nitric oxide / circulation /
# collagen / oxygen): zero perde o verniz que compra a virada de piada-de-legume
# para clinica em 8 segundos, duas viram aula.
# ⛔ ZERO medida, ZERO duracao, ZERO horario — forma e gesto (`a spoon of`, `a
# pour of`, `two fingers of`).
# ⭐ As tres propriedades do V6 do VAZAMENTO, e as tres sao obrigatorias: a
# NEGACAO vem ANTES da solucao, o ORGAO e' nomeado na mesma frase, e usa o SIM
# que ele ja' deu.
# ⚠️ `cred` filtra por modo: `ambas` roda nos dois.
FUNDIDAS = [
    {"cred": "ambas", "txt": "A spoon of {r}, a pour of warm water, stirred down. Real vasodilators. But without the gelatin trick that glass does nothing at all for his {o}."},
    {"cred": "desmente", "txt": "Forget the powder. {r} in warm water, stirred until it turns. That's nitric oxide. And without the gelatin trick his {o} never feels one drop of it."},
    {"cred": "confirma", "txt": "Outside, that took four seconds. Inside, it takes {r} and warm water. Circulation. But the gelatin trick is the half nobody hands you, and his {o} needed it."},
    {"cred": "ambas", "txt": "Here's the half they give away: {r}, warm water, one turn of the spoon. Collagen. Here's the half they don't: the gelatin trick, and his {o} felt that one."},
    {"cred": "ambas", "txt": "Two fingers of {r} into warm water. Good for oxygen. But nobody hands you the gelatin trick, and that is the half his {o} was missing."},
    # ⛔⛔ FRASE ORFA — CONSERTO DE 2026-08-03, E A ENTRADA E' A QUE O OPERADOR
    # CITOU. Ele leu o take renderizado ("It isn't age. The blood flow got
    # choked off. Parsley and warm water open it. Real vasodilators. And the
    # gelatin trick is what keeps his old boy open.") e cravou: "deveria ser it
    # isn't age QUE ESTA CAUSANDO O SEU JOHN-SON NAO FUNCIONAR MAIS. Voce tem
    # que contextualizar mais as coisas. Ta' deixando o viewer sem entender o
    # contexto e do que se trata."
    # ⭐ A REGRA NOVA: toda frase que nomeia uma CAUSA carrega, NA MESMA FRASE, o
    # que ela quebra. Aqui DUAS nomeavam causa e nenhuma dizia sobre o que ela
    # age — `It isn't age.` (idade causando o que?) e `The blood flow got choked
    # off.` (estrangulado onde?). O orgao so' chegava na ULTIMA frase, e o
    # operador reprovou exatamente essa cena: nao vale "aparece em algum lugar".
    # ⭐ O conserto FUNDE as duas numa frase so' e poe o alvo dentro dela — assim
    # ele cabe no teto em vez de estoura-lo: 31 palavras contra 27, e 33 no pior
    # par {r}/{o} (TETO_FALA[2] = 34). ⛔ Subir o teto nao era opcao.
    # ⚠️ `he went soft`, nao `you`: o que se cobra e' REFERENTE, nao pessoa — a
    # fundida ja' conta a historia do homem (`his {o}` na frase do gelatin
    # trick) e trocar a pessoa no meio quebraria o arco.
    # ⛔ Zero prazo e zero medida na frase nova (RS10 / a linha do NECROSE).
    {"cred": "ambas", "txt": "It isn't age — the blood flow got choked off and he went soft. {r} and warm water open it. Real vasodilators. And the gelatin trick is what keeps his {o} open."},
    {"cred": "ambas", "txt": "My aunt gave me this one: {r}, warm water, stir it clear. Oxygen. On its own it did nothing — the gelatin trick is what finished it for his {o}."},
    {"cred": "desmente", "txt": "That powder never did a thing. This does: {r}, warm water, one stir. Vasodilators. And the gelatin trick, without which his {o} stays exactly where it is."},
    {"cred": "ambas", "txt": "Nobody hands you the whole thing. {r}, warm water, stirred down — real collagen. And the gelatin trick, the half his {o} was waiting on."},
    {"cred": "ambas", "txt": "Watch. {r} goes in, warm water over it, stir it down. That's nitric oxide. Skip the gelatin trick and his {o} feels none of it."},
    {"cred": "confirma", "txt": "You saw what that does on a bench. In a glass it's {r} and warm water. Circulation. And the gelatin trick, which is the part his {o} needed."},
    {"cred": "ambas", "txt": "A pour of {r}, warm water, stirred until the colour turns. Vasodilators, plain and simple. But without the gelatin trick his {o} gets none of it."},
    {"cred": "ambas", "txt": "Spoon of {r}. Warm water. Stir. That's the oxygen half. The other half is the gelatin trick, and his {o} answered inside three weeks."},
    {"cred": "ambas", "txt": "Here's the part they leave out. {r} on its own is half a recipe — without the gelatin trick the collagen never reaches his {o} at all."},
    {"cred": "ambas", "txt": "{r} and warm water, stirred with a wooden spoon. That's the vasodilator half. The gelatin trick is the other half, and his {o} needed both."},
    {"cred": "confirma", "txt": "That was four seconds on a bench. This is the inside version: {r}, warm water, stirred down. Nitric oxide. Plus the gelatin trick his {o} needed."},
]

# ---------------------------------------------------------------------------
# COPY — CENA 3: prova -> barreira -> CTA -> gate, nesta ordem
# ---------------------------------------------------------------------------
# ⭐ ORDEM DO ED (2026-08-01, lendo os takes 3 renderizados): a cena 3 ABRE COM
# PROVA, nunca com barreira — "esta' muito fazendo rodeios, beating about the
# bush... ta' muito drifting essa copy". O take onde o homem finalmente aparece
# segurando a evidencia gastava a primeira frase falando de preco e de prateleira
# de supermercado.
# ⚠️ E a segunda ordem, que e' o que fecha: "faltou referenciar o falico" — ⛔
# TODAS trazem `{o}`, sem ele a prova nao tem referente: diz que algo mudou e nao
# diz o que.
# ⭐ E aqui a prova pesa MAIS do que nos dois agentes anteriores: se o lote rodar
# em `--credibilidade desmente`, a copy DESTRUIU a evidencia do take 1, e esta e'
# a ultima chance de a promessa aterrissar num corpo humano.
# ⛔ Zero deixis a pessoa (`Look at him`, `That's him`): a relacao ja' esta'
# NOMEADA no IMAGE 03 e deixis reprova o teste do radio.
# ⚠️ `voz`: `intima` exige relacao de parceria; `terceiro` roda com qualquer uma.
# O motor FILTRA — nao se reescreve pool.
PROVAS = [
    {"voz": "intima", "txt": "Now his {o} won't let me sleep."},
    {"voz": "intima", "txt": "His {o} wakes up before he does."},
    {"voz": "intima", "txt": "I beg his {o} for mercy now."},
    {"voz": "intima", "txt": "His {o} gives me no quiet nights."},
    {"voz": "intima", "txt": "Done by ten before. His {o} isn't."},
    {"voz": "intima", "txt": "I stopped asking. His {o} started answering."},
    {"voz": "terceiro", "txt": "His {o} doesn't take no anymore."},
    {"voz": "terceiro", "txt": "His {o} gave the whole thing away."},
    {"voz": "intima", "txt": "Three weeks in, his {o} outlasts me."},
    {"voz": "terceiro", "txt": "My sister asked what changed. His {o}."},
    {"voz": "terceiro", "txt": "His {o} quit waiting on him."},
    {"voz": "terceiro", "txt": "His {o} stopped apologizing. So did he."},
    {"voz": "terceiro", "txt": "Nineteen days later his {o} doesn't quit."},
    {"voz": "intima", "txt": "His {o} turns the lamp back on."},
    {"voz": "intima", "txt": "His {o} runs the schedule now."},
    {"voz": "terceiro", "txt": "Sixty-two, and his {o} acts thirty."},
    {"voz": "intima", "txt": "I said goodnight. His {o} disagreed."},
    {"voz": "terceiro", "txt": "Ask what his {o} does at midnight."},
]

# ⭐ AS BARREIRAS, e este e' o lugar delas: DEPOIS da prova e NUNCA antes dela. A
# TR14 registra que elas "nao foram apagadas — sao copy validada e continuam no
# motor, PARADAS", e que traze-las de volta seria beat de OUTRA cena.
# Tratam as objecoes de Benson que cabem em 24 segundos: #9 (nao tenho dinheiro),
# #3 (nao funciona pra mim), #7 (ninguem pode saber).
# ⛔ ARMADILHA REGISTRADA DE PROPOSITO, para que ninguem a reintroduza:
# `Ten seconds, once, before bed.` esta' DESCARTADA — `before bed` e' marcador de
# PRAZO e a cena 3 tem `{o}` na prova; e' a mesma soma que derrubou o NECROSE. A
# reescrita sem prazo (`One glass. That is the whole thing.`) esta' no pool.
BARREIRAS = [
    "Two dollars at any store.",
    "Nobody in your house knows.",
    "No prescription, no doctor, no waiting.",
    "It's in the baking aisle.",
    "You already own the glass.",
    "No pills, no appointment, no questions.",
    "Cheaper than one refill.",
    "He never knew I started it.",
    "Bottom shelf, about four dollars.",
    "Nothing to swallow but water.",
    "No one has to know.",
    "One glass. That is the whole thing.",
    "Sixty-eight years old. Same result.",
    "Four dollars in the baking aisle.",
]

# ⛔⛔ TODAS carregam o LITERAL `Comment gelatin,` — minusculo e com virgula
# (`sc.lint_cta_literal`, regra do operador de 2026-08-02 para TODO SHORT). A
# legenda do nosso video nasce no Veo Editor, do Whisper, EM CIMA DO AUDIO
# GERADO: ela nao e' escrita por nos, e' a transcricao do que o modelo FALOU.
# Comando variavel (`Type gelatin`, `Say gelatin`, `One word: gelatin`) e' margem
# para o modelo parafrasear a keyword, e parafrasear quebra a automacao de DM.
# ⛔ TODAS passam no `lint_isca_cta`: dizem O QUE a pessoa recebe. Medido no dia
# da ordem: 22 CTAs em 7 agentes pediam o comentario sem dizer o que chega — o
# espectador era convidado a pagar sem saber o que compra.
# ⛔ `book`, `yes` e `link` proibidos (`book` quebra a automacao e e' literalmente
# a palavra do reel de 82K — terceira vez que aquela pagina a usa).
# ⚠️ ENTROPIA DE FORMA, nao so' de contagem: 5 das 16 levam a keyword FORA da
# posicao inicial, senao o --stats conta 16 e a variacao percebida e' 3.
CTAS = [
    "Comment gelatin, and I'll send you the whole recipe tonight.",
    "Comment gelatin, and the recipe's on your phone tonight.",
    "Comment gelatin, and I'll send you both halves.",
    "Comment gelatin, and I'll tell you exactly what to buy.",
    "Comment gelatin, one word, and the recipe is yours.",
    "Comment gelatin, and I'll send the other half.",
    "Comment gelatin, and the recipe goes out tonight.",
    "Comment gelatin, and I'll send the missing half.",
    "Want it? Comment gelatin, and I'll send the recipe tonight.",
    "Comment gelatin, and I'll send you the measurements.",
    "Comment gelatin, and I'll send it before you scroll.",
    "Comment gelatin, and I'll send all four ingredients.",
    "It's four lines. Comment gelatin, and I'll send it.",
    "Comment gelatin, and I'll send you where to get it.",
    "Comment gelatin, nothing else, and I'll send the recipe.",
    "Comment gelatin, and I'll send the part nobody posts.",
]

# ⭐ O follow-gate que ja' usamos JA' E' o "porque" de Langer (1978): pedido +
# motivo leva a aceitacao de 60% para 93%. E' 2/2 na fonte e literal no nosso
# `espinha-fixa`. ⛔ NAO MEXER — registrado aqui so' para que ninguem "melhore" a
# linha sem saber por que ela funciona.
# ⛔ REGRA DE POOL medida pelo operador no TROCA: "brother" caia em 31-73% dos
# videos. EXATAMENTE DUAS entradas com `brother`, tres com vocativo no total, 11
# de 14 sem vocativo nenhum.
# ⚠️ E o que varia nao e' so' o vocativo: varia o MOTIVO do gate (a plataforma
# bloqueia · a fila de comentarios · o feed some amanha · o algoritmo esconde).
# ⛔ Zero nome de plataforma na `Dialogue:` — nomear a plataforma e' P12 e nao
# custa nada evitar.
GATES = [
    "Follow first, or nothing lands.",
    "No follow, no message.",
    "I only message people who follow.",
    "Followers get answered first.",
    "One tap on follow. That's it.",
    "Follow me, brother. Then it sends.",
    "No follow, my inbox stays shut.",
    "Three hundred comments tonight. Followers first.",
    "Follow tonight. Tomorrow this is gone.",
    "Follow, my friend. Then I answer.",
    "The algorithm hides me from non-followers.",
    "Follow first. That opens my inbox.",
    "I answer followers. Everyone else waits.",
    "Follow me, brother. That's the gate.",
]

VOCATIVOS = ("brother", "my friend", "guys", "buddy", "man", "girls")


# ---------------------------------------------------------------------------
# TABELAS DE TOKEN BANIDO (o linter compartilhado le' estas)
# ---------------------------------------------------------------------------
# ⚠️ Direcao de cena, nunca fala.
# ⚠️ ATENCAO — A DIFERENCA DESTE MOTOR PARA OS OUTROS SHORT: aqui o TAKE 01 TEM
# de mandar o prop crescer. Entao a familia `grows/lengthens/expands/...` NAO
# entra nestas tabelas (que valem para todos os blocos); ela e' cobrada pela RS6,
# que a permite SO' no TAKE 01. O que fica aqui e' o que nao pode aparecer em
# bloco NENHUM — o vocabulario de tumescencia e o de efeito grafico.
BANIDOS_TAKE = {
    "engorged": "adjetivo de estado — vocabulario de tumescencia",
    "tumescent": "idem",
    "throbbing": "idem",
    "veiny": "detalhe anatomico no prop",
    "veins": "idem",
}
BANIDOS_IMAGE = dict(BANIDOS_TAKE)

# ⛔ substring, em qualquer bloco.
# ⚠️ A oclusao e' de PO', nunca de corte: a deteccao de cena na fonte confirma que
# NAO ha' corte dentro do crescimento — e' morph em plano continuo. Zero `cut`,
# zero `transition`, zero efeito grafico: sem particula, sem glow, sem whoosh,
# sem flash, sem trilha. O crescimento e' puramente geometrico, e a cor do prop
# nao muda.
BANIDOS_GLOBAL = {
    "morph": "o crescimento e' geometrico, nunca efeito — e' nome de tecnica",
    "time-lapse": "idem", "before and after": "idem",
    "transforms": "idem", "vfx": "idem",
    # ⛔⛔ CORRECAO DE 2026-08-02. A ⛔ list da R8 proibia `cut`, `transition`,
    # particula, glow, whoosh, flash e trilha — e a tabela nao implementava
    # NENHUM dos que um editor de pool realmente escreveria. Regra que so' mora
    # no comentario nao e' regra: e' intencao. Medido em 200 sorteios, zero dos
    # tokens abaixo aparece hoje, entao entram sem falso positivo.
    # ⚠️ ⛔ `cut` NU esta' FORA de proposito: a tabela casa por SUBSTRING e o
    # pool inteiro de props fala em `cut end`, `cut crown`, `cut stalk`. Banir a
    # palavra solta reprovaria 100% dos lotes — que e' o modo de falha da §2 do
    # licoes-de-construcao. Entram as FORMAS DE CORTE, que nao colidem com nada.
    "jump cut": "a oclusao e' de PO', nunca de corte — morph em plano continuo",
    "quick cut": "idem", "smash cut": "idem", "match cut": "idem",
    "cross-fade": "idem", "crossfade": "idem", "dissolve to": "idem",
    "transition": "idem — zero corte dentro do crescimento",
    "whoosh": "efeito grafico/sonoro — o crescimento e' puramente geometrico",
    "glow": "idem", "lens flare": "idem", "particle": "idem",
    "sparkle": "idem", "shimmer": "idem", "flash": "idem",
    "the victim": "rotulo que significa dano — descrever a pessoa",
    "the narrator": "idem — ou nomear a relacao",
}
BANIDOS_CTA = {
    "book": "quebra a automacao Comentario->DM (e e' a palavra do reel de 82K)",
    "yes": "idem",
    "link": "CTA e' comentario, nao link",
}

# ⛔ o guardrail de figurino: zero vocabulario de desejo. A roupa entra como PECA
# descrita, nunca como adjetivo de desejo.
BANIDOS_DESEJO = {
    "sexy": "vocabulario de desejo — a roupa entra como PECA descrita",
    "seductive": "idem", "sultry": "idem", "curvy": "idem",
    "revealing": "idem", "cleavage": "idem", "lingerie": "idem",
    "provocative": "idem", "alluring": "idem", "flirty": "idem",
}


# ---------------------------------------------------------------------------
# HELPERS
# ---------------------------------------------------------------------------

def _palavras(txt):
    """Contrato do linter compartilhado: palavra e' letra, apostrofo e hifen."""
    return len(re.findall(r"[A-Za-z'\-]+", txt))


_CACHE_W = {}


def _w(txt):
    """`_palavras` memoizado — o sorteio da cena 3 pesa milhares de combinacoes
    por video, e recompilar regex em cada uma custa segundos no self-test."""
    n = _CACHE_W.get(txt)
    if n is None:
        n = _CACHE_W[txt] = _palavras(txt)
    return n


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


def _maiuscula(txt):
    return txt[0].upper() + txt[1:] if txt else txt


# ⛔ O SLOT QUE CAI NO INICIO DA FRASE. Os pools nascem em minuscula porque na
# maioria das entradas o `{s}` e o `{r}` caem no meio da oracao — mas em sete
# hooks e tres fundidas eles ABREM a frase, e sem isto a copy sai
# "cinnamon on its own is half a recipe" e "sea salt. Every guy has heard of it".
# ⚠️ Nao e' cosmetico: a legenda do video nasce do Whisper sobre o audio, mas a
# `Dialogue:` e' o que o operador LE para aprovar o lote — e frase em minuscula
# le' como erro de motor, que e' exatamente o que era.
_RX_FRASE = re.compile(r"(^|[.!?]\s+)([a-z])")


def _pontuar(fala):
    return _RX_FRASE.sub(lambda m: m.group(1) + m.group(2).upper(), fala)


def _sem_artigo(txt):
    """Tira o artigo inicial de um item de pool.

    A travada diz "The %s has been standing on the %s..." e os itens do pool
    nascem com artigo proprio. O motor ajusta o SLOT; ⛔ a travada nao se
    reescreve.
    """
    for art in ("the ", "a ", "an "):
        if txt.lower().startswith(art):
            return txt[len(art):]
    return txt


def _peca(calca):
    """A peca de roupa NUA, sem oracao subordinada.

    As 14 calcas ja' nascem nuas, entao isto e' GUARDA, nao transformacao: se
    alguem acrescentar "khaki shorts with a deep side pocket" a um pool, a
    travada da F12b nao sai como "against the front of his khaki shorts with a
    deep side pocket".
    """
    return calca.split(" with ")[0]


# ⚠️ Os recipientes do pool SUBSTANCIAS sao caixa, saco, lata, pote, vidro e
# cilindro — e os TAKEs do pool DESPEJOS foram escritos com "the carton". Mandar
# "the carton" num take cuja imagem tem um saco de pano e' contradicao dentro do
# proprio bloco. O motor resolve o SLOT; ⛔ nenhum dos dois pools se reescreve.
_RECIPIENTES = ("carton", "cylinder", "canister", "sack", "box", "tin", "bag",
                "jar")


def _recipiente(caixa):
    for r in _RECIPIENTES:
        if re.search(r"\b%s\b" % r, caixa):
            return r
    return "container"


def _pote(caixa):
    """O recipiente sem o "in her raised hand" — quem declara a mao e' o DESPEJO.

    Sem isto o IMAGE 01 diz duas vezes de que mao se trata, e as duas podem nao
    ser a mesma (o despejo `punho_esquerdo` com um pote "in her raised hand").
    ⚠️ Duas formas no pool (`, turned mouth-down` e `and turned mouth-down`):
    cortar so' a primeira deixava a farinha com a mao errada em quadro, e o
    self-test cobra o contrato dos dois lados.
    """
    return re.split(r",? and turned mouth-down|, turned mouth-down",
                    caixa)[0].rstrip(", ")


def _anel(sub):
    """O anel de po' ja' formado no frame 0, derivado do MONTE (que e' a versao
    que cresce, do TAKE). Uma fonte da verdade por substancia, nao duas."""
    return _maiuscula(sub["monte"].split(" spreading")[0])


def _monte_verbo(sub):
    """O monte com VERBO FINITO, para o slot do RS_CRONOMETRO.

    ⛔ Bug medido em 2026-08-02, presente em 100% dos TAKE 01: a travada e'
    "On the %s under it, %s the whole time, wider at the end..." e espera uma
    ORACAO no slot; o pool entrega um SINTAGMA NOMINAL (`a ring of dark powder
    spreading into a wide flat mound`). O TAKE saia sem verbo finito:
    "On the bench top under it, a ring of dark powder spreading into a wide flat
    mound the whole time, wider at the end of the shot than at the start."

    ⚠️ O conserto e' do SLOT, nunca da travada nem do pool — os dois continuam
    caractere por caractere como estavam. O ` spreading` ja' e' contrato cobrado
    pelo `_contrato_dos_pools`, entao a derivacao nao pode falhar calada.
    """
    return sub["monte"].replace(" spreading into", " spreads into", 1)


# ⛔ RS8 — a declaracao de escala tem de ser a MESMA nas tres cenas a menos do
# pronome. Escala diferente entre as cenas le' como um SEGUNDO crescimento fora
# do take que o coreografa. E a regua e' o antebraco de QUEM SEGURA: dela na cena
# 1, dele na cena 3.
_RX_ESCALA = re.compile(
    r"as long as (?:her|his) forearm and (?:still )?no thicker than "
    r"((?:two of )?(?:her|his) \w+)", re.I)


def _escala(txt, pron):
    """O nucleo invariante da escala, com o pronome de quem segura."""
    m = _RX_ESCALA.search(txt)
    if not m:
        return ""
    cauda = re.sub(r"\b(her|his)\b", pron, m.group(1))
    return "as long as %s forearm and no thicker than %s" % (pron, cauda)


def _escala_bloco(txt):
    """A escala como o LINTER a le': normalizada no masculino, para comparar
    blocos diferentes sem tropecar no pronome."""
    return _escala(txt, "his")


# ---------------------------------------------------------------------------
# A RELACAO NOMEADA (alavanca 2 do protocolo de recusa)
# ---------------------------------------------------------------------------
# ⛔ `the victim`/`the narrator` sao proibidos: descreve-se a pessoa ou nomeia-se
# o vinculo. ⚠️ E a relacao tem de ser FISICAMENTE POSSIVEL com as idades
# sorteadas — com narradora de 28 e corpo-prova de 58, trinta e um anos de
# casamento nao fecham. Entao o numero se calcula (uniao a partir dos 20 anos do
# mais novo), e quando nem isso fecha cai-se em vinculo SEM numero.
# ⛔ Omitir a relacao nao e' opcao.
RELACOES_SEM_NUMERO = [
    "the woman who cooks for him",
    "the woman from the house next door",
    "the woman who does his shopping",
]

# a familia de voz que cada relacao autoriza nas PROVAS da cena 3: so' a parceira
# pode dizer "I beg his {o} for mercy now".
VOZES_INTIMAS = ("his wife of", "his partner of")


def voz_da_relacao(relacao):
    return "intima" if relacao.startswith(VOZES_INTIMAS) else "terceiro"


def _relacao(rng, idade_m, idade_h):
    anos = min(idade_m, idade_h) - 20
    op = list(RELACOES_SEM_NUMERO)
    if anos >= 15:
        # peso 2 na esposa: e' a formulacao do operador e e' a que carrega mais
        # vinculo — e vinculo nomeado e' o que desarma a leitura de intimidade
        # gratuita na composicao da F12b.
        op += ["his wife of %s years" % _por_extenso(anos)] * 2
        op.append("his partner of %s years" % _por_extenso(anos))
    elif anos >= 8:
        op.append("his partner of %s years" % _por_extenso(anos))
    return rng.choice(op)


# ---------------------------------------------------------------------------
# LEDGER — anti-repeticao por pagina
# ---------------------------------------------------------------------------
EIXOS_LEDGER = ("narradora", "corpo_prova", "cenario", "prop", "substancia",
                "despejo", "reacao", "analogia", "receita", "mecanismo",
                "bancada")


def _carregar_ledger():
    if os.path.exists(LEDGER):
        with open(LEDGER, encoding="utf-8-sig") as f:
            return json.load(f)
    return {}


def _anotar(ledger, spec):
    """Anota o sorteio no ledger EM MEMORIA, sem tocar no arquivo.

    ⚠️ Existe separado do `_gravar_ledger` por causa do `--dry-run`: sem isto os
    N videos de um mesmo lote sao sorteados todos contra o mesmo historico e o
    `_evitando()` nao ve' o irmao que acabou de sair. O ensaio nao grava, mas tem
    de se lembrar de si.
    """
    p = ledger.setdefault(spec["pagina"], {})
    for eixo in EIXOS_LEDGER:
        p.setdefault(eixo, []).append(spec[eixo]["id"])
        p[eixo] = p[eixo][-12:]


def _gravar_ledger(ledger, spec):
    _anotar(ledger, spec)
    with open(LEDGER, "w", encoding="utf-8") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)


def _evitando(rng, pool, recentes):
    livres = [x for x in pool if (x.get("id") if isinstance(x, dict) else x)
              not in recentes]
    return rng.choice(livres if livres else pool)


def _cita(corpo, cabeca):
    """A palavra-cabeca de um item de bancada aparece na copy? (singular ou
    plural — 'fig' tem de pegar 'figs')."""
    return re.search(r"\b%ss?\b" % re.escape(cabeca), corpo, re.I) is not None


def _bancada_livre(rng, falas, recentes, receita=None, sub=None):
    """RS16 — O RECIBO E' MUDO, por construcao em vez de checado depois.

    Tres colisoes, nao uma: com a FALA (o que a boca cita), com o `{r}` da
    receita e com o `{s}` da substancia. O "full recipe" so' tem lastro se a boca
    citar UM e a imagem mostrar TRES — se a boca cita o que a imagem devia
    esconder, o recibo deixa de ser recibo.
    """
    corpo = " ".join(falas)
    if receita:
        corpo += " " + receita["fala"]
    if sub:
        corpo += " " + sub["fala"]
    livres = [b for b in BANCADAS
              if not any(_cita(corpo, c) for c in b["cabecas"])]
    return _evitando(rng, livres if livres else BANCADAS, recentes)


# ecos de FATO dentro do mesmo video ("two dollars" ditos duas vezes em 24s).
ECOS = ("two dollars", "four dollars", "three weeks", "nineteen days",
        "sixty-two", "sixty-eight", "baking aisle")


def _eco(*partes):
    corpo = " ".join(partes).lower()
    return any(corpo.count(e) > 1 for e in ECOS)


def _tri(txt):
    """Os trigramas de uma frase, para achar eco que a tupla ECOS nao lista."""
    p = re.findall(r"[a-z']+", (txt or "").lower())
    return {tuple(p[i:i + 3]) for i in range(len(p) - 2)}


def _repete(hook, bullet):
    """O bullet repete uma expressao que o HOOK acabou de dizer?

    ⛔ Medido em 2026-08-02: no degrau 4 o hook "That one about {s} has been
    going around forever. Watch." podia ser seguido do bullet "That one has been
    going around for years." — a mesma frase duas vezes em oito segundos. A
    tupla ECOS nao pega isto porque ela lista FATOS (precos, prazos), e aqui o
    eco e' de FORMULA. Trigrama pega os dois casos sem lista para manter.
    ⚠️ Guarda de entropia, nao de doutrina: entra como filtro com fallback, e
    nenhuma entrada de pool foi tocada.
    """
    return bool(_tri(hook) & _tri(bullet))


# ⛔ RS10 — PRAZO + `your <nucleo>` no mesmo take de 8s: a composicao literal que
# derrubou o video do NECROSE por "politicas contra a geracao de conteudo
# nocivo". ⚠️ O `tonight` dos CTAs nao dispara: o CTA nao nomeia o orgao.
# ⛔⛔ CORRECAO DE 2026-08-02 — `inside three weeks` ESCAPAVA. O `\bin \w+
# (days|weeks|months)\b` antigo so' casava a preposicao `in`, e o pool FUNDIDAS
# tem `his {o} answered inside three weeks`; `within` e `after` tambem passavam,
# e `in <numero> days` com numero por extenso composto (`twenty-one days`) idem.
# ⚠️ Isto e' MODERACAO, nao estetica: a soma `your <nucleo>` + PRAZO no mesmo
# take de 8s e' a composicao literal que derrubou o video do NECROSE por
# "politicas contra a geracao de conteudo nocivo". Uma regra que nao ve' metade
# das formas do prazo nao esta' cobrindo a composicao — esta' fingindo cobrir.
# ⛔⛔ BURACO TAPADO EM 2026-08-02. A v1 listava so' `days|weeks|months` e por
# isso deixava passar `That happened in four seconds.` — medido, 33 em 400
# videos casavam `your {o}` no hook com esse bullet na cena 1, e a regra
# reportava 0 ERRO. Regra escrita nao e' regra que pega: o `_rs10_prazo` existia
# desde o primeiro dia e nunca disparou uma vez.
# ⚠️ E' o bullet que fala da duracao DO QUE A TELA MOSTROU, nao do corpo de quem
# assiste. Vale a trava assim mesmo: o classificador julga TOKEN e GEOMETRIA,
# nunca intencao (CLAUDE.md §a licao que generaliza).
RS10_PRAZO = re.compile(
    r"\b(overnight|by next|by the|before bed|every (morning|night)|tonight|"
    r"by morning|by tomorrow|"
    r"(in|inside|within|after)\s+[\w-]+\s+"
    r"(seconds?|minutes?|hours?|days?|weeks?|months?))\b", re.I)
RS10_CORPO_2A = re.compile(
    r"\byour\s+(?:\w+\s+){0,2}(%s)\b" % "|".join(NUCLEO), re.I)

# ⛔ RS9 — RECEITA TOPICA SOBRE O CORPO. Nao e' risco de render, e' risco de DANO
# REAL: capsaicina em mucosa por dez minutos e' queimadura quimica, e uma
# instrucao dessas saindo de uma pagina nossa e' o gatilho de denuncia mais forte
# que existe em plataforma. A nossa substancia toca o PROXY e as maos, NUNCA
# corpo humano (TR5).
RS9_TOPICA = re.compile(
    r"\b(apply|rub|smear|spread|put)\b.{0,40}\b(on|onto|into)\s+"
    r"(your|his|her)\b", re.I)

# ⛔ RS6/achado ⑧ — se a cena 1 cresce, as cenas 2 e 3 nao crescem, nao incham e
# nao mudam de tamanho. Dois choques iguais em 24 segundos somam a um.
# ⚠️ O REGEX MUDOU DE CASA em 2026-08-02: mora em `short_comum.CRESCIMENTO`,
# porque a doutrina sempre disse que ele moraria la'. Este alias existe para que
# ninguem reescreva a lista aqui — uma regra, um lugar (P9).
RS6_CRESCIMENTO = sc.CRESCIMENTO

# ⛔ RS7 — `slowly`/`gradually` sao P17 (crescimento lento e' invisivel e o feed
# da' 2 segundos); `comically large` so' vale para prop que NASCE grande (R6),
# nunca como resultado; `absurdly oversized` e' selo 🔴 sempre.
RS7_TAKE1 = re.compile(r"\b(slowly|gradually|absurdly oversized|"
                       r"comically large)\b", re.I)

RS11_TOKENS = ("the victim", "the narrator", "groin", "pubic", "crotch",
               "mouth open", "lips parted", "open-mouthed", "tongue")

RS12_CONFORMIDADE = ("not a celebrity", "fully clothed", "they are adults",
                     "no nudity", "no minors")

RS13_NEGACAO = ("no label", "without a label", "not a brand", "readable label",
                "no logo")

RS14_BANIDOS = ("potted plant", "carpet", "rug")


# ---------------------------------------------------------------------------
# SORTEIO
# ---------------------------------------------------------------------------

def _montar_falas(rng, sub, rec, orgaos, relacao, credibilidade, degrau):
    """As tres falas.

    cena 1 = hook + leitura do crescimento + bullet
    cena 2 = a fundida, sozinha (⛔ zero folga: 34 palavras em 8s ja' pedem 4,25
             p/s, ACIMA da taxa mediana da propria fonte — bullet aqui e'
             atropelo garantido)
    cena 3 = prova -> barreira -> CTA -> gate, nesta ordem

    Filtros POR CONSTRUCAO, todos com fallback medido no self-test:
    · `degrau`        — a escada da moderacao do hook e' escolha do Ed
    · `credibilidade` — confirma (default) x desmente, nos dois pools que mudam
    · ⭐ A CENA 1 NOMEIA O ORGAO EXATAMENTE UMA VEZ. Se o hook ja' o nomeia
      (degrau 2/3), o bullet vem dos tres que nao nomeiam; se o hook nao nomeia
      (degrau 4/5), o bullet nomeia. Duas mencoes do mesmo substantivo em 8
      segundos e' bordao, e nenhuma deixa a cena 1 sem dizer o nome da coisa —
      que foi a queixa literal do operador no ESCANDALO.
    · voz da PROVA x relacao nomeada da cena 3
    · teto e piso POR CENA, e o eco de fato medido no VIDEO INTEIRO
    """
    # ----- cena 1 ----------------------------------------------------------
    hooks = [h for h in HOOKS if h["degrau"] == degrau] or HOOKS
    hk = rng.choice(hooks)
    hook = hk["txt"].format(s=sub["fala"], o=orgaos[0])
    hook_nomeia = "{o}" in hk["txt"]

    beat2 = CONFIRMACOES if credibilidade == "confirma" else DESMENTIDOS
    # ⛔⛔ RS10 NO SORTEIO, nao so' no linter (ordem do operador, 2026-08-02).
    # Se o hook trouxe `your {o}`, nada que entra na MESMA fala de 8s pode
    # trazer marcador de prazo — e' a composicao que derrubou o NECROSE.
    # ⚠️ Ate' hoje isto era so' ERRO de lint: o motor MONTAVA o video proibido e
    # reclamava depois. Agora ele nao monta. O linter fica como rede.
    # ⛔ NENHUMA DAS DUAS COPIES FOI ALTERADA — copy e' alcada do operador. O que
    # muda e' o SORTEIO: elas continuam nos pools e so' deixam de sair juntas.
    prazo_proibido = bool(RS10_CORPO_2A.search(hook))

    def _sem_prazo(itens):
        """⚠️ `or itens` e' rede, nao gambiarra: pool vazio deixaria a cena 1
        abaixo do PISO_FALA. Medido em 400 sorteios: nunca e' acionada."""
        if not prazo_proibido:
            return itens
        return [x for x in itens if not RS10_PRAZO.search(x)] or itens

    beat2 = _sem_prazo(beat2)
    # ⛔ o bullet obedece ao MODO (ver o campo `cred` do pool): duas entradas
    # emolduram o crescimento como boato e so' podem rodar depois do desmentido.
    elegiveis = _sem_prazo([b["txt"] for b in BULLETS
                            if b["cred"] in ("ambas", credibilidade)])
    pref = [b for b in elegiveis if ("{o}" in b) != hook_nomeia]
    resto = [b for b in elegiveis if ("{o}" in b) == hook_nomeia]

    def _c1(b2, bl):
        txt = "%s %s" % (hook, b2)
        return txt + " " + bl.format(o=orgaos[0]) if bl else txt

    # ⚠️ O eco e' cobrado contra os DOIS beats, nao so' contra o bullet: medido,
    # a colisao real do degrau 4 era hook x DESMENTIDO ("That one about {s} has
    # been going around forever. Watch." + "That one's been going around for
    # years."), e uma guarda que so' olhasse o bullet nao veria nada.
    def _validos(bullets, sem_eco=True):
        return [(b2, bl) for b2 in beat2 for bl in bullets
                if PISO_FALA[1] <= _w(_c1(b2, bl)) <= TETO_FALA[1]
                and not (sem_eco and (_repete(hook, bl) or _repete(hook, b2)
                                      or _repete(b2, bl)))]

    op = (_validos(pref) or _validos(resto)
          or _validos(pref, sem_eco=False) or _validos(resto, sem_eco=False)
          or _validos([None]))
    if op:
        c1 = _c1(*rng.choice(op))
    else:                                   # nao acontece: medido no self-test
        c1 = _c1(min(beat2, key=_w), min(pref or elegiveis, key=_w))

    # ----- cena 2 ----------------------------------------------------------
    fund = [f for f in FUNDIDAS if f["cred"] in ("ambas", credibilidade)]
    cand = [f["txt"].format(r=rec["fala"], o=orgaos[1]) for f in fund or FUNDIDAS]
    ok = [c for c in cand if PISO_FALA[2] <= _w(c) <= TETO_FALA[2]]
    c2 = rng.choice(ok or cand)

    # ----- cena 3 ----------------------------------------------------------
    voz = voz_da_relacao(relacao)
    provas = [p for p in PROVAS if voz == "intima" or p["voz"] == "terceiro"]
    prova = rng.choice(provas)["txt"].format(o=orgaos[2])
    cta = rng.choice(CTAS)
    gate = rng.choice([g for g in GATES
                       if _w(prova) + _w(cta) + _w(g) + _MIN_BARREIRA
                       <= TETO_FALA[3]] or GATES)
    usado = _w(prova) + _w(cta) + _w(gate)
    # ⛔ FALLBACK EM DOIS ESTAGIOS — correcao de 2026-08-02. O fallback antigo
    # (`or BARREIRAS`) desligava a guarda de eco junto com o piso: bastava nao
    # haver barreira dentro do piso para o fato repetido embarcar sem aviso.
    # Agora relaxa-se o PISO primeiro e a guarda de eco por ultimo — a ordem
    # importa porque piso curto e' AVISO (RS20) e fato repetido em 24 segundos e'
    # o vicio que o operador ja' mediu.
    def _barr(piso, sem_eco):
        return [b for b in BARREIRAS
                if (usado + _w(b) >= PISO_FALA[3] if piso else True)
                and usado + _w(b) <= TETO_FALA[3]
                and not (sem_eco and _eco(c1, c2, prova, cta, gate, b))]

    barr = (_barr(True, True) or _barr(False, True)
            or _barr(True, False) or _barr(False, False) or BARREIRAS)
    c3 = "%s %s %s %s" % (prova, rng.choice(barr), cta, gate)
    return [_pontuar(c1), _pontuar(c2), _pontuar(c3)]


_MIN_BARREIRA = min(_w(b) for b in BARREIRAS)


def sortear(pagina, rng, ledger, credibilidade=None, degrau=None, analogia=None):
    """Anti-repeticao por ledger, por pagina.

    Os dois eixos de ROSTO evitam os 3 ultimos (rosto repetido e' o que o
    operador ve primeiro no lote); os eixos de cenario e objeto evitam os 2
    ultimos.

    ⚠️ A ORDEM IMPORTA e cada dependencia esta' escrita:
    · a SUBSTANCIA depende do PROP (RS15: `tom` por contraste — sem contraste o
      po' nao vira ESTRIA e a explicacao fisica do morph some do quadro);
    · a ANALOGIA depende da flag (RS18: analogia de INFLACAO contradiz a
      R2-emenda dentro do mesmo TAKE, e prompt que se contradiz o modelo resolve
      como quiser);
    · o HOMEM depende da idade dela (RS19/ES11);
    · a RELACAO e' sorteada ANTES das falas, porque ela manda na VOZ da prova;
    · a BANCADA e' sorteada DEPOIS das falas, porque o recibo tem de ser mudo.
    """
    cred = credibilidade or CREDIBILIDADE_PADRAO
    deg = degrau or DEGRAU_PADRAO
    fam = analogia or ANALOGIA_PADRAO

    hist = ledger.get(pagina, {})
    elegiveis = [n for n in NARRADORAS if n["idade"] >= IDADE_MINIMA_NARRADORA]
    nar = _evitando(rng, elegiveis, hist.get("narradora", [])[-3:])
    pares = [h for h in homens_de(pagina)
             if abs(h["idade"] - nar["idade"]) <= TETO_DIF_IDADE]
    hom = _evitando(rng, pares or homens_de(pagina),
                    hist.get("corpo_prova", [])[-3:])
    cen = _evitando(rng, CENARIOS, hist.get("cenario", [])[-2:])
    prop = _evitando(rng, PROPS_MURCHOS, hist.get("prop", [])[-2:])
    sub = _evitando(rng, [s for s in SUBSTANCIAS if s["tom"] != prop["tom"]],
                    hist.get("substancia", [])[-2:])
    # ⛔ R4 (2026-08-02): uma mao segura a base do prop, a outra despeja — entao
    # as DUAS estao ocupadas o take inteiro. Sai do sorteio todo despejo que
    # ocupa a mao livre com outra coisa (apoiar o antebraco, bater na caixa,
    # segurar colher, aparar o que cai) e toda reacao de mao/punho/dedo, mais a
    # que exige recuar do balcao. Deixar entrar manda o modelo LARGAR o prop no
    # meio do crescimento — foi o que o render fez antes desta trava.
    desp = _evitando(rng, [d for d in DESPEJOS if not d.get("mao_livre")],
                     hist.get("despejo", [])[-2:])
    rea = _evitando(rng, [r for r in REACOES if not r.get("maos")],
                    hist.get("reacao", [])[-2:])
    ana = _evitando(rng, [a for a in ANALOGIAS if a["familia"] == fam],
                    hist.get("analogia", [])[-2:])
    rec = _evitando(rng, RECEITAS, hist.get("receita", [])[-2:])
    mec = _evitando(rng, MECANISMOS_PROP, hist.get("mecanismo", [])[-2:])

    relacao = _relacao(rng, nar["idade"], hom["idade"])
    # tres substantivos DISTINTOS de uma vez: um por cena. Rotacao e' do VIDEO,
    # nao da fala.
    orgaos = rng.sample(NUCLEO, 3)
    falas = _montar_falas(rng, sub, rec, orgaos, relacao, cred, deg)
    ban = _bancada_livre(rng, falas, hist.get("bancada", [])[-2:], rec, sub)

    return {"pagina": pagina, "narradora": nar, "corpo_prova": hom,
            "cenario": cen, "prop": prop, "substancia": sub, "despejo": desp,
            "reacao": rea, "analogia": ana, "receita": rec, "mecanismo": mec,
            "bancada": ban, "relacao": relacao, "credibilidade": cred,
            "degrau": deg, "analogia_flag": analogia, "falas": falas}


# ---------------------------------------------------------------------------
# GERADOR
# ---------------------------------------------------------------------------
# Formato de entrega, sempre: BLOCO 0 (REF) -> os 3 IMAGE agrupados -> os 3 TAKE
# agrupados. ⛔ Nunca intercalar. Numeracao x/03. Destino: AdBatch Vertical 3.

def _descricao(p):
    """A pessoa em UMA oracao, com os eixos que a fazem ser OUTRA pessoa.

    ⚠️ Dez pessoas descritas so' por cabelo sao a MESMA pessoa dez vezes, e o
    gerador devolve o mesmo rosto (licoes-de-construcao §15). Por isso o porte
    entra sempre, e os oculos e o pelo facial entram quando existem.
    ⛔ Zero adjetivo de etnia aqui: quem injeta e' o motor, por pagina.
    """
    partes = [p["cabelo"]]
    if p.get("barba"):
        partes.append(p["barba"])
    if p.get("oculos"):
        partes.append(p["oculos"])
    partes.append(p["rosto"])
    marca = ", ".join(partes[:-1]) + " and " + partes[-1]
    return "%s, with %s" % (p["porte"], marca)


def montar(spec):
    et = ETNIA[spec["pagina"]]
    nar, hom, cen = spec["narradora"], spec["corpo_prova"], spec["cenario"]
    prop, sub, desp = spec["prop"], spec["substancia"], spec["despejo"]
    rea, ana, rec = spec["reacao"], spec["analogia"], spec["receita"]
    mec, ban, falas = spec["mecanismo"], spec["bancada"], spec["falas"]
    bnc = cen["bancada"]
    luz = _maiuscula(cen["luz"])

    # ⚠️ A ANCORA DE CONTINUIDADE E' A NARRADORA — ela esta' nas tres cenas, e a
    # descricao volta INTEIRA, com a marca facial. Ancora curta ("same hair")
    # carrega a roupa e PERDE O ROSTO: foi assim que o VAZAMENTO devolveu um
    # senhor de oculos e bigode no lugar do corpo-prova, e como o TAKE diz "only
    # she speaks", o estranho falava a fala do REF.
    # ⛔ E ela nunca leva adjetivo de etnia: e' sorteada livre.
    ela = ("a %d-year-old woman, %s, wearing %s"
           % (nar["idade"], _descricao(nar), nar["roupa"]))
    mesma = ("The same %d-year-old woman, %s, wearing %s"
             % (nar["idade"], _descricao(nar), nar["roupa"]))
    recibo = RS_BANCADA_RECIBO % (bnc, ban["itens"])
    # a escala do prop crescido, com a regua de quem esta' em quadro (RS8)
    escala_dela = _escala(prop["depois"], "her")

    b = {}

    b["BLOCO 0 (REF)"] = (
        "REF 01: Photo of a real person, a %d-year-old woman, chest up, facing "
        "the camera directly, calm steady expression. %s. Wearing %s. Plain "
        "neutral gray background, soft even frontal light. No subtitles, no "
        "captions, no burned-in text, no watermark."
        % (nar["idade"], _maiuscula(_descricao(nar)), nar["roupa"])
    )

    # --- IMAGE 01/03 — O DESPEJO JA' EM ANDAMENTO ---------------------------
    # R1: o IMAGE e' o primeiro frame = estado ANTES. O prop pequeno, EM PE',
    # com a MAO ESQUERDA DELA FECHADA NA BASE (R4) e a direita despejando.
    # ⛔ Ate' 2026-08-02 este bloco punha o prop "solto, sem nenhuma mao tocando"
    # pela R4-emenda, com o argumento de que mao em quadro daria escala e
    # denunciaria o efeito. O render provou o contrario duas vezes: fruta em pe'
    # no proprio eixo maior sem apoio ja' nasce implausivel no frame 0, e a base
    # sem ancora fisica faz o modelo resolver o alongamento AFUNDANDO o prop na
    # mesa. A mao nao denuncia o efeito — ela e' a regua que o torna legivel.
    # ⚠️ Nao existe frame de "antes" do POURING: o video abre com o despejo ja'
    # correndo, e o anel de po' ja' formado (a mesma economia do TR4).
    # ⛔ SEM bancada-recibo: este bloco ja' carrega ela + o prop + o pote + o
    # jato + o anel, e densidade e' superficie de bloqueio.
    b["IMAGE 01/03"] = (
        "IMAGE 01/03: Medium shot in %s, camera low and close to the top of the "
        "%s. Standing behind the %s is %s. %s Standing upright on the %s in "
        "front of her, held at its base in her closed fist that rests on "
        "the %s: %s. %s runs "
        "from her other hand down onto it in one unbroken column. %s %s %s %s %s"
        % (cen["set"], bnc, bnc, ela,
           desp["img"] % (_pote(sub["caixa"]), prop["nome"]),
           bnc, bnc, prop["antes"], _maiuscula(sub["jato"]),
           RS_ANEL_IMAGE % (_anel(sub), bnc),
           RS_PLATEIA_INTERNA_IMAGE % prop["nome"],
           FRASE_SEM_MARCA, luz, CAUDA)
    )

    # --- IMAGE 02/03 — A RECEITA INCOMPLETA ---------------------------------
    # ⚠️ `re_ancora` no lugar de "in the same kitchen": sem ele metade do lote
    # perdia o cenario E a bandeira dos EUA a partir da cena 2.
    # ⚠️ O prop CRESCIDO fica em quadro, com a MESMA declaracao de escala da cena
    # 1 (RS8) — e' o recibo mudo do que acabou de acontecer.
    # ⚠️ O mecanismo ja' estava plantado desde o frame 1 (TR1/ES9): o reveal nao
    # apresenta nada novo.
    b["IMAGE 02/03"] = (
        "IMAGE 02/03: Medium shot at the same %s in %s, same light. %s, stands "
        "behind it talking straight to camera. On the %s in front of her, on a "
        "wooden board: %s. %s Still standing on its own base at the far end of "
        "the %s, the %s, now %s. %s %s %s"
        % (bnc, cen["re_ancora"], mesma, bnc, rec["img"],
           RS_PLANTADO_IMAGE % (_sem_artigo(mec["plantado"]), bnc,
                                mec["pousado"]),
           bnc, prop["nome"], escala_dela, recibo, luz, CAUDA)
    )

    # --- IMAGE 03/03 — O CORPO-PROVA ----------------------------------------
    # ⭐ A F12b. Ele DE PE, mudo, o prop na PROPRIA mao; ela aponta SEM ENCOSTAR.
    # O que bloqueia nao e' o prop, e' a AGENCIA — e a agencia se declara tambem
    # pelo OLHAR DELE NA LENTE, nao so' pelo punho.
    # ⚠️ A relacao e' nomeada UMA vez (dentro da travada) e a etnia dele e' a da
    # pagina; a dela continua sem adjetivo nenhum.
    # ⚠️ A ancora de escala e' NO CORPO DELE: quem segura e' ele.
    # ⛔ Zero plateia e SEM bancada-recibo (F12c): este e' o bloco mais arriscado
    # do lote, e o lastro do "full recipe" ja' foi provado na cena 2.
    b["IMAGE 03/03"] = (
        "IMAGE 03/03: Medium shot in %s, same light. %s, stands frame-left. A "
        "%d-year-old %s man, %s, in %s and %s, stands beside her, upright, chin "
        "level, his eyes on the lens, saying nothing. %s %s They are the only "
        "two people in the frame. %s %s"
        % (cen["re_ancora"], mesma, hom["idade"], et, _descricao(hom),
           hom["roupa"], hom["calca"],
           RS_F12B_IMAGE % (_peca(hom["calca"]), prop["dele"], spec["relacao"]),
           RS_KEYWORD_NA_MAO_IMAGE % mec["curto"], luz, CAUDA)
    )

    # --- TAKE 01/03 — ⭐⭐ O AGENTE INTEIRO ESTA' AQUI ----------------------
    # A coreografia por batidas com segundos (R2b) e' 🟢 validada em producao
    # (Joe/geoduck, saiu de primeira depois de duas falhas). Verbo de crescimento
    # descreve o QUE; o Veo precisa do COMO, senao preenche o vazio com o
    # movimento que ele ja' conhece pra aquela forma — bicho se levantando.
    # ⚠️ Estoura o orcamento de 80-150 palavras do TAKE: EXCECAO AUTORIZADA pela
    # R2b, que e' a conta que prop de armadilha documentada paga.
    # ⛔ Zero corte dentro do crescimento (e' morph em plano continuo na fonte),
    # zero efeito grafico, e a cor do prop nao muda.
    # ⛔⛔ A ORDEM DOS BLOCOS E' CRONOLOGICA, e ela foi CORRIGIDA em 2026-08-02.
    # Antes o RS_JATO_MASCARA (a oclusao) era emitido DEPOIS do
    # RS_ESTADO_FINAL_TAKE — ou seja, o prompt mandava ver o estado final e so'
    # entao contava que a mudanca tinha acontecido escondida. Pior: o
    # RS_CRESCIMENTO_TAKE ja' diz `%s comes back into view at the new height`, e
    # "volta a aparecer" so' tem referente se a oclusao tiver sido declarada
    # ANTES. O bloco chegava depois, e prompt que se contradiz o modelo resolve
    # como quiser — que e' justamente o que a R8 existe para impedir.
    # ⚠️ Nenhuma travada mudou um caractere: mudou a ORDEM em que sao emitidas.
    #   batidas (0-3 / 3-5 / 5-8 + trava de identidade)
    #   -> a cortina que cobre a batida de 3-5
    #   -> o estado final, que fecha
    b["TAKE 01/03"] = (
        "TAKE 01/03: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway, no cuts, and the camera does not move. %s "
        "%s %s %s %s %s %s %s%s\n"
        "Dialogue: \"%s\"\n"
        "Audio: dry powder hissing onto wood, quiet room tone in the %s. No "
        "music."
        % (desp["take"].replace("carton", _recipiente(sub["caixa"])),
           RS_CRESCIMENTO_TAKE % (prop["nome"], bnc, bnc, ana["desc"],
                                  _maiuscula(prop["topo"]), prop["nome"], bnc,
                                  prop["nome"], prop["nome"], bnc, bnc),
           RS_JATO_MASCARA % (sub["jato"], prop["nome"], sub["fala"],
                              prop["topo"]),
           RS_ESTADO_FINAL_TAKE % prop["depois"],
           RS_CRONOMETRO % (bnc, _monte_verbo(sub)),
           "By the end of the shot the surface of it shows %s." % sub["estria"],
           RS_PLATEIA_INTERNA_TAKE % rea["desc"],
           RS_APAGAO,
           (" " + prop["negacao"] if prop["negacao"] else "")
           + " " + RS_SEM_FLUTUAR + " She is the only person in the shot.",
           sonorizar(falas[0]), cen["curto"])
    )

    # --- TAKE 02/03 — A RECEITA EXECUTADA -----------------------------------
    # ⛔ Se a cena 1 cresce, NADA cresce aqui (achado ⑧): o prop e' objeto
    # estatico DECLARADO, com a travada nua e o objeto nomeado.
    b["TAKE 02/03"] = (
        "TAKE 02/03: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway. The camera does not move and there is no cut "
        "at any point in this shot. %s %s\n"
        "Dialogue: \"%s\"\n"
        "Audio: a spoon against glass, quiet room tone in the %s. No music."
        % (RS_RECEITA_TAKE % (rec["gesto"], rec["fisica"], mec["curto"]),
           RS_IMOVEL_TAKE % prop["nome"], sonorizar(falas[1]), cen["curto"])
    )

    # --- TAKE 03/03 ----------------------------------------------------------
    # ⛔ So' ela tem Dialogue. Ele e' mudo — o dialogo do Veo e' monofonico na
    # pratica e duas vozes saem tortas.
    b["TAKE 03/03"] = (
        "TAKE 03/03: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway, no cuts, and the camera does not move. %s %s "
        "She speaks straight into the lens, calm and even, no rush. Only she "
        "speaks.\nDialogue: \"%s\"\nAudio: quiet room tone in the %s. No music."
        % (RS_F12B_TAKE % prop["nome"], RS_KEYWORD_NA_MAO_TAKE,
           sonorizar(falas[2]), cen["curto"])
    )

    # ⛔ a trava de texto queimado em todo TAKE. Zero de 18 TAKEs a tinham quando
    # o buraco foi achado, e texto vindo do gerador entra por cima da nossa
    # legenda (que nasce depois, no Editor, do Whisper) e nao sai.
    return sc.selar_takes(b)


# ---------------------------------------------------------------------------
# LINTER — as regras RS
# ---------------------------------------------------------------------------
# ⚠️ A NUMERACAO. As regras de DOUTRINA sao R1-R8 do
# `AGENTE_ED_RESSURREICAO_V1.md`; `RS<n>` e' o identificador do LINTER, e toda
# mensagem de erro cita a regra da doutrina que ela cobra. Sem isso o operador e'
# mandado ler a regra errada — foi o que aconteceu no TROCA, cujo motor citava
# TR15-TR21 quando a doutrina ia ate' a TR14 (licoes-de-construcao §3).
#
#   RS1  R2-emenda  escala diferencial     RS11 §travas  tokens proibidos
#   RS2  R8         o jato-mascara         RS12 §travas  conformidade
#   RS3  R4         mao na base+superficie RS13 §travas  ausencia por negacao
#   RS4  R7         o apagao               RS14 ES13/ES14 texto e objeto banido
#   RS5  R2b/el.7   trava de identidade    RS15 §prop    contraste de tom
#   RS6  achado ⑧   nada cresce nas 2 e 3  RS16 TR7/ES8  recibo mudo
#   RS7  R2/R6      adverbio e `comically` RS17 §cred    modo x fundida x cena 3
#   RS8  R2-emenda  escala igual nas 3     RS18 R2-emenda familia da analogia
#   RS9  V5/TR5     receita topica         RS19 ES11     casting
#   RS10 §travas    prazo + nucleo         RS20 §tetos   piso (AVISO)
#   RS21 R3         a reacao durante       RS23 §travas  figurino sem desejo
#   RS22 ES9        keyword na mao livre
#
# ⚠️ RS21-RS23 nasceram numerados em 2026-08-02. Antes eram `RS_plateia`,
# `RS_keyword` e `RS_figurino` — identificadores sem linha na tabela da
# doutrina, que e' a falha do TROCA repetida (licoes-de-construcao §3). Toda
# adicao futura entra AQUI e na tabela do .md no mesmo commit.
#
# ⚠️ TODA comparacao com travada e' contra o MIOLO INVARIANTE (o trecho entre os
# `%s`), NUNCA contra o template cru: `TRAVADA not in bloco` da' 100% de falso
# positivo quando a travada chega formatada, e regra que reprova tudo nunca foi
# testada (licoes-de-construcao §2).

M_ESCALA_DIF = ("width barely changes", "slimmer in proportion")
M_JATO = "is hidden inside it and cannot be seen"
# ⛔ MIOLO INVARIANTE, nunca a constante inteira (§2 das licoes): a constante tem
# slot e a comparacao daria 100% de falso positivo.
M_BASE = "never lets go, never lifts and never changes position"
M_SUPERFICIE = "no part of it ever goes below the surface"
# ⛔ a formulacao da R4-emenda revogada. Se voltar, o prop volta a afundar.
M_BASE_REVOGADA = "not held by anyone"
M_APAGAO = "for eight tenths of a second around the moment it changes"
M_IDENTIDADE = ("There is only ONE", "No second")
M_F12B = ("in both his own fists one stacked above the other",
          "points one finger down at it without touching him")
M_IMOVEL = "completely motionless for the entire shot"
M_RECIBO = " beside her, never touched and never mentioned: "
M_KEYWORD = ("In her own free left hand, raised to the height of her chest "
             "and held level")
M_PLATEIA = "the way a studio audience reacts to a punchline"


def _direcao(txt):
    """So' a direcao de cena — a fala nunca entra na varredura de token."""
    return txt.split("\nDialogue:")[0]


def _faltam(txt, tokens):
    return [t for t in tokens if t not in txt]


def _achar(txt, tokens):
    """Os tokens de uma tabela que aparecem no texto (palavra inteira)."""
    return [t for t in tokens if re.search(r"\b%s\b" % re.escape(t), txt, re.I)]


def _rs1_escala(spec, blocos, achados):
    """R2-emenda: sem isto o Veo escala o objeto INTEIRO, e escala uniforme le'
    como INCHACO — o vocabulario de tumescencia que ja' derrubou video nosso."""
    falta = _faltam(blocos["TAKE 01/03"], M_ESCALA_DIF)
    if falta:
        achados.append(("ERRO", "RS1 (R2-emenda): TAKE 01/03 sem o miolo da "
                                "escala diferencial %s — sem ele o Veo escala "
                                "tudo junto e a leitura vira inchaco" % falta))


def _rs2_jato(spec, blocos, achados):
    """R8: sem a cortina o Veo tem de resolver a transformacao em campo aberto,
    que e' a parte cara e e' onde ele inventa."""
    if M_JATO not in blocos["TAKE 01/03"]:
        achados.append(("ERRO", "RS2 (R8): TAKE 01/03 sem a oclusao pelo jato — "
                                "a transformacao fica em campo aberto"))


def _rs3_base(spec, blocos, achados):
    """R4: a ancora e' a MAO fechada na base, e a bancada e' solida.

    ⛔ Ate' 2026-08-02 esta regra cobrava a "base cravada na bancada" da
    R4-emenda. `base cravada` + `so' cresce para cima` sao ordens que o modelo
    nao consegue satisfazer juntas, e ele resolvia enfiando o prop na mesa. A
    emenda foi revogada no primeiro render."""
    if M_BASE not in blocos["TAKE 01/03"]:
        achados.append(("ERRO", "RS3 (R4): TAKE 01/03 sem a mao fechada na "
                                "base — sem ancora fisica o prop afunda na "
                                "bancada ou o take le' como TROCA DE OBJETO"))
    if M_SUPERFICIE not in blocos["TAKE 01/03"]:
        achados.append(("ERRO", "RS3 (R4): TAKE 01/03 sem a trava de superficie "
                                "solida — e' o que impede o prop de crescer "
                                "PARA DENTRO da bancada"))
    if RS_SEM_FLUTUAR not in blocos["TAKE 01/03"]:
        achados.append(("ERRO", "RS3 (R4): a amarracao e' DUPLA — falta "
                                "'No floating objects.' no TAKE 01/03"))
    for nome in ("IMAGE 01/03", "TAKE 01/03"):
        if M_BASE_REVOGADA in blocos[nome]:
            achados.append(("ERRO", "RS3 (R4): %s traz %r — e' a R4-emenda "
                                    "REVOGADA, e ela poe o prop em pe' sem "
                                    "apoio no frame 0"
                            % (nome, M_BASE_REVOGADA)))


def _rs25_transferencia(spec, blocos, achados):
    """⭐ A CENA 1 DIZ QUE AQUILO E' O CORPO DELE. Ordem do operador em
    2026-08-03, com dois takes renderizados na mao.

    O vicio que ela mata: a cena mostra o despejo, nomeia a substancia, descreve
    o que acontece na tela — e NUNCA fecha o circuito com o espectador. Sem a
    transferencia explicita o video vira demonstracao de cozinha, e a queixa
    literal foi "quem ve o video nem entende do que se trata".

    ⛔ Regra de FUNCAO, nao de forma: nao basta o orgao aparecer no video (o
    `cota_min` do lint_curto ja' cobra isso e passava). Ele tem de aparecer na
    CENA 1, em segunda pessoa, colado ao que a substancia faz."""
    fala = spec["falas"][0]
    if not RS10_CORPO_2A.search(fala):
        achados.append(("ERRO", "RS25: a cena 1 nunca diz `your <nucleo>` — o "
                                "espectador tem de INFERIR que a demo e' o "
                                "corpo dele, e e' onde a copy vira vaga"))


def _rs4_apagao(spec, blocos, achados):
    """R7: com fala ou legenda por cima o espectador LE em vez de VER, e a
    mecanica morre. O silencio nao e' economia de palavra — e' o palco."""
    if M_APAGAO not in blocos["TAKE 01/03"]:
        achados.append(("ERRO", "RS4 (R7): TAKE 01/03 sem o apagao de 0,8s em "
                                "cima do morph"))


def _rs5_identidade(spec, blocos, achados):
    """R2b elemento 7: o gerador ADICIONA quando voce descreve um estado novo sem
    dizer que ele pertence ao objeto que ja' existe. Transformar e' caro,
    instanciar e' barato — ja' custou 5 tentativas de geoduck."""
    falta = _faltam(blocos["TAKE 01/03"], M_IDENTIDADE)
    if falta:
        achados.append(("ERRO", "RS5 (R2b/elemento 7): TAKE 01/03 sem a trava de "
                                "identidade %s — o Veo cria um SEGUNDO prop e "
                                "deixa o murcho ao lado" % falta))


def _rs6_nada_cresce(spec, blocos, achados):
    """⭐ Achado ⑧, e e' o coracao do agente: se a cena 1 cresce, as cenas 2 e 3
    nao crescem, nao incham e nao mudam de tamanho. Dois choques iguais em 24
    segundos somam a um.

    ⚠️ A MAQUINARIA MORA NO `short_comum.py` desde 2026-08-02, porque e' o que a
    doutrina sempre declarou ("vira LINTER no short_comum.py e vale para todo
    SHORT que vier") e nao era verdade — a regra vivia so' aqui. Aqui fica o que
    e' DESTE agente: qual bloco tem licenca para crescer.
    """
    sc.lint_nada_cresce(blocos, achados, excecao=("TAKE 01/03",),
                        rotulo="RS6 (achado 8)")


def _rs7_adverbio(spec, blocos, achados):
    """R2/R6: `slowly` e `gradually` sao P17 — crescimento lento e' invisivel e o
    feed da' 2 segundos. `comically large` so' vale para prop que NASCE grande."""
    achado = sorted(set(m.group(0).lower()
                        for m in RS7_TAKE1.finditer(_direcao(blocos["TAKE 01/03"]))))
    if achado:
        achados.append(("ERRO", "RS7 (R2/R6): TAKE 01/03 usa %s" % achado))


def _rs8_escala_igual(spec, blocos, achados):
    """R2-emenda: escala diferente entre as cenas le' como um SEGUNDO crescimento
    fora do take que o coreografa. E a regua e' o antebraco de QUEM SEGURA."""
    lidas = {}
    for nome in ("TAKE 01/03", "IMAGE 02/03", "IMAGE 03/03"):
        lidas[nome] = _escala_bloco(blocos[nome])
    vazios = [k for k, v in lidas.items() if not v]
    if vazios:
        achados.append(("ERRO", "RS8 (R2-emenda): sem declaracao de escala em %s"
                        % sorted(vazios)))
        return
    if len(set(lidas.values())) > 1:
        achados.append(("ERRO", "RS8 (R2-emenda): a escala do prop muda entre as "
                                "cenas: %s" % sorted(set(lidas.values()))))


def _rs9_topica(spec, blocos, achados):
    """V5/TR5: a nossa topica toca o PROXY e as maos, NUNCA corpo humano. ⛔ Nao
    e' risco de render, e' risco de DANO REAL — nao se resolve regerando nem
    trocando a forma de dizer."""
    for i, fala in enumerate(spec["falas"], 1):
        m = RS9_TOPICA.search(fala)
        if m and not any(p["nome"] in fala for p in PROPS_MURCHOS):
            achados.append(("ERRO", "RS9 (V5/TR5): a cena %d manda aplicar no "
                                    "CORPO ('%s') — a substancia so' toca o "
                                    "proxy" % (i, m.group(0))))


def _rs10_prazo(spec, blocos, achados):
    """A composicao literal que derrubou o video do NECROSE por conteudo nocivo:
    `your <nucleo>` + marcador de PRAZO no mesmo take de 8s."""
    for i, fala in enumerate(spec["falas"], 1):
        p = RS10_PRAZO.search(fala)
        if p and RS10_CORPO_2A.search(fala):
            achados.append(("ERRO", "RS10: cena %d soma 'your <nucleo>' e o prazo "
                                    "'%s' no mesmo take — e' a linha do NECROSE"
                            % (i, p.group(0))))


def _rs11_tokens(spec, blocos, achados):
    for nome, txt in sorted(blocos.items()):
        achado = [t for t in RS11_TOKENS if t in txt.lower()]
        if achado:
            achados.append(("ERRO", "RS11: %s contem %s" % (nome, achado)))


def _rs12_conformidade(spec, blocos, achados):
    """Silencio vence negacao: declaracao nao desarma classificador, so' entrega
    municao — `not a celebrity` nomeia a categoria que ele policia."""
    for nome, txt in sorted(blocos.items()):
        achado = [t for t in RS12_CONFORMIDADE if t in txt.lower()]
        if achado:
            achados.append(("ERRO", "RS12: %s declara conformidade %s"
                            % (nome, achado)))


def _rs13_negacao(spec, blocos, achados):
    """A ausencia de rotulo se declara pela AFIRMATIVA. `Nothing carries a
    readable label, logo or brand` injeta os tres tokens num prompt cuja tese e'
    que nao ha' nenhum — a mesma mecanica de `fully clothed`."""
    for nome, txt in sorted(blocos.items()):
        achado = [t for t in RS13_NEGACAO if t in txt.lower()]
        if achado:
            achados.append(("ERRO", "RS13: %s declara a ausencia pela negacao %s "
                                    "— so' a FRASE_SEM_MARCA afirmativa entrega "
                                    "isso" % (nome, achado)))
    for nome in ("IMAGE 01/03", "IMAGE 02/03"):
        if FRASE_SEM_MARCA not in blocos[nome]:
            achados.append(("ERRO", "RS13 (P12): %s sem a FRASE_SEM_MARCA — na "
                                    "fonte a marca da caixa fica legivel o hook "
                                    "inteiro" % nome))


def _rs14_texto_e_objeto(spec, blocos, achados):
    """ES13: credencial DECLARADA em imagem e' a primeira linha da cerca, e texto
    legivel e' superficie de bloqueio. ES14: objeto sem funcao de leitura."""
    for nome, txt in sorted(blocos.items()):
        if re.search(r"\bbooks?\b", txt, re.I):
            achados.append(("ERRO", "RS14 (ES13): %s diz 'book' — o cenario diz "
                                    "'hardback spines'" % nome))
        achado = [t for t in RS14_BANIDOS if t in txt.lower()]
        if achado:
            achados.append(("ERRO", "RS14 (ES14): %s tem objeto banido %s"
                            % (nome, achado)))


def _rs15_contraste(spec, blocos, achados):
    """Sem contraste o po' nao vira ESTRIA, e a estria e' a explicacao fisica do
    morph que a imagem entrega sozinha (a mesma quantidade de po' numa area 2,3x
    maior vira listra em vez de capa)."""
    if spec["prop"]["tom"] == spec["substancia"]["tom"]:
        achados.append(("ERRO", "RS15: prop (%s) e substancia (%s) no mesmo tom "
                                "'%s' — o po' nao vira estria"
                        % (spec["prop"]["id"], spec["substancia"]["id"],
                           spec["prop"]["tom"])))


def _rs16_recibo(spec, blocos, achados):
    """TR7/ES8: a boca cita 1, a imagem mostra 3-4. Se a boca cita o que a imagem
    devia esconder, o recibo deixa de ser recibo."""
    corpo = " ".join(spec["falas"]) + " " + spec["receita"]["fala"] + " " + \
        spec["substancia"]["fala"]
    citadas = [c for c in spec["bancada"]["cabecas"] if _cita(corpo, c)]
    if citadas:
        achados.append(("ERRO", "RS16 (TR7/ES8): a bancada-recibo %s colide com "
                                "a copy/receita/substancia em %s"
                        % (spec["bancada"]["id"], citadas)))
    if M_RECIBO not in blocos["IMAGE 02/03"]:
        achados.append(("ERRO", "RS16: IMAGE 02/03 sem a bancada-recibo — o "
                                "'full recipe' fica sem lastro em imagem"))
    for nome in ("IMAGE 01/03", "IMAGE 03/03"):
        if M_RECIBO in blocos[nome]:
            achados.append(("ERRO", "RS16 (F12c): %s com bancada-recibo — "
                                    "densidade e' superficie de bloqueio" % nome))


def _rs17_credibilidade(spec, blocos, achados):
    """A fundida tem `cred`, e o modo do lote manda. E se o lote roda em
    `desmente`, a copy DESTRUIU a evidencia do take 1: a cena 3 passa de
    recomendavel a OBRIGATORIAMENTE o corpo-prova."""
    cred = spec["credibilidade"]
    if cred not in CREDIBILIDADES:
        achados.append(("ERRO", "RS17: credibilidade '%s' desconhecida" % cred))
    alvo = [_pontuar(f["txt"].format(r=spec["receita"]["fala"], o=o))
            for f in FUNDIDAS if f["cred"] in ("ambas", cred)
            for o in NUCLEO]
    if spec["falas"][1] not in alvo:
        achados.append(("ERRO", "RS17: a fundida da cena 2 nao pertence ao modo "
                                "'%s'" % cred))
    falta = _faltam(blocos["IMAGE 03/03"], M_F12B)
    if falta:
        achados.append(("ERRO", "RS17 (F12b/TR10/ES4): IMAGE 03/03 nao e' o "
                                "corpo-prova (%s) — no modo '%s' o video ficaria "
                                "sem evidencia nenhuma" % (falta, cred)))


def _rs18_analogia(spec, blocos, achados):
    """A familia PRESSAO descreve INFLACAO, que contradiz a escala diferencial
    DENTRO do mesmo TAKE — e prompt que se contradiz o modelo resolve como
    quiser. Entra so' por flag explicita."""
    if spec["analogia"]["familia"] == "pressao" and \
            spec.get("analogia_flag") != "pressao":
        achados.append(("ERRO", "RS18 (R2-emenda): analogia '%s' e' da familia "
                                "pressao sem a flag --analogia pressao"
                        % spec["analogia"]["id"]))
    if spec["analogia"]["desc"] not in blocos["TAKE 01/03"]:
        achados.append(("ERRO", "RS18 (R2b/elemento 2): TAKE 01/03 sem a analogia "
                                "fisica — verbo de crescimento descreve o QUE, e "
                                "o Veo precisa do COMO"))


def _rs19_casting(spec, blocos, achados):
    """ES11: a politica de MENORES e' a determinista (nao cede a regerar) e e'
    sensivel a GEOMETRIA DE INTIMIDADE + DIFERENCA DE IDADE, nao a idade real."""
    if spec["narradora"]["idade"] < IDADE_MINIMA_NARRADORA:
        achados.append(("ERRO", "RS19 (ES11): narradora com %d anos (piso %d)"
                        % (spec["narradora"]["idade"], IDADE_MINIMA_NARRADORA)))
    dif = abs(spec["corpo_prova"]["idade"] - spec["narradora"]["idade"])
    if dif > TETO_DIF_IDADE:
        achados.append(("ERRO", "RS19 (ES11): %d anos de diferenca no par da cena "
                                "3 (teto %d)" % (dif, TETO_DIF_IDADE)))
    et = ETNIA[spec["pagina"]]
    if spec["corpo_prova"] not in homens_de(spec["pagina"]):
        achados.append(("ERRO", "RS19: corpo-prova fora do pool de %s" % et))


def _rs20_piso(spec, blocos, achados):
    """⚠️ O piso NAO se cumpre com enchimento: cumpre-se com mais FATO. Bullet que
    nao carrega fato novo e' o 'Give me eight seconds' do ESCANDALO com outro
    nome."""
    for i, fala in enumerate(spec["falas"], 1):
        n = _palavras(fala)
        if n < PISO_FALA[i]:
            achados.append(("AVISO", "RS20: cena %d com %d palavras (piso %d) — "
                                     "cumprir com mais FATO, nunca com "
                                     "enchimento" % (i, n, PISO_FALA[i])))


def _rs_travadas(spec, blocos, achados):
    """RS21-RS23 + a segunda metade da RS6: travadas cujo sumico e' MUDO.

    ⛔⛔ CORRECAO DE 2026-08-02 — ESTAS QUATRO NAO TINHAM NUMERO. O motor emitia
    `RS_plateia`, `RS_imovel`, `RS_keyword` e `RS_figurino`, e a tabela da
    doutrina ia de RS1 a RS20: quatro identificadores que o operador nao tem
    como procurar em lugar nenhum. E' LITERALMENTE a falha do TROCA que a §As
    regras do motor diz estar evitando (o motor citava TR15-TR21 e a doutrina ia
    ate' a TR14 — licoes-de-construcao §3), cometida de novo com outra grafia.
    ⚠️ Pior no caso da plateia: a mensagem citava "achado 4/ES1", um achado do
    mapa e uma regra do ESCANDALO. A regra DESTE agente que ela cobra e' a R3
    (ALGUEM REAGE ENQUANTO CRESCE), e a R3 nao aparecia na mensagem — o operador
    era mandado para o arquivo errado.
    """
    if M_PLATEIA not in blocos["TAKE 01/03"]:
        achados.append(("ERRO", "RS21 (R3): TAKE 01/03 sem a analogia de genero "
                                "da reacao — e' ela que mantem a cara de "
                                "escandalo sem 'mouth open'"))
    if M_IMOVEL not in blocos["TAKE 02/03"]:
        achados.append(("ERRO", "RS6 (achado 8): TAKE 02/03 sem a travada de "
                                "imobilidade com o prop nomeado"))
    if M_KEYWORD not in blocos["IMAGE 03/03"]:
        achados.append(("ERRO", "RS22 (ES9): IMAGE 03/03 sem o objeto da "
                                "keyword na mao livre dela"))
    for nome, tab in (("IMAGE", BANIDOS_DESEJO),):
        for chave, txt in sorted(blocos.items()):
            if not chave.startswith(nome):
                continue
            achado = _achar(txt, tab)
            if achado:
                achados.append(("ERRO", "RS23 (§travas): %s tem vocabulario de "
                                        "desejo %s — a roupa entra como PECA "
                                        "descrita" % (chave, achado)))


def lint(spec, blocos):
    # ⚠️ `teto_total` explicito: o padrao do `lint_curto` e' a soma dos tetos
    # (91), que aqui e' MENOR que a borda de cima da faixa da doutrina (96) — o
    # AVISO dispararia abaixo do numero que a propria faixa permite.
    return sc.lint_curto(
        sys.modules[__name__], spec, blocos, (1, 2, 3), TETO_FALA,
        literais=("gelatin trick",), teto_total=TETO_TOTAL,
        extras=(_rs1_escala, _rs2_jato, _rs3_base, _rs4_apagao, _rs5_identidade,
                _rs6_nada_cresce, _rs7_adverbio, _rs8_escala_igual, _rs9_topica,
                _rs10_prazo, _rs11_tokens, _rs12_conformidade, _rs13_negacao,
                _rs14_texto_e_objeto, _rs15_contraste, _rs16_recibo,
                _rs17_credibilidade, _rs18_analogia, _rs19_casting, _rs20_piso,
                _rs25_transferencia, _rs_travadas))


# ---------------------------------------------------------------------------
# UI — contrato do ui_agente.py compartilhado
# ---------------------------------------------------------------------------
# ⚠️ "homens_de" e' FUNCAO da pagina, nao lista — a UI resolve isso desde
# 2026-07-31. "NARRADORAS" e' lista simples porque a narradora e' solta.
EIXOS_UI = [
    ("narradora", "A NARRADORA", "NARRADORAS", "rosto"),
    ("corpo_prova", "O CORPO-PROVA (cena 3)", "homens_de", "rosto"),
    ("cenario", "O CENARIO", "CENARIOS", "id"),
    ("prop", "O PROP QUE CRESCE", "PROPS_MURCHOS", "nome"),
    ("substancia", "A SUBSTANCIA DESPEJADA", "SUBSTANCIAS", "fala"),
    ("despejo", "O GESTO DO DESPEJO", "DESPEJOS", "id"),
    ("reacao", "A REACAO DELA", "REACOES", "id"),
    ("analogia", "A ANALOGIA FISICA", "ANALOGIAS", "id"),
    ("receita", "A RECEITA (cena 2)", "RECEITAS", "fala"),
    ("mecanismo", "O MECANISMO PLANTADO", "MECANISMOS_PROP", "curto"),
    ("bancada", "A BANCADA-RECIBO", "BANCADAS", "itens"),
]

PT_CENARIO = {
    "escritorio_diplomas": "No escritório com estante e dois diplomas",
    "escritorio_painel": "No escritório de madeira, com abajur verde",
    "sala_estante": "Na sala com estante do chão ao teto",
    "cozinha_modesta": "Na cozinha modesta de laminado",
    "cozinha_ilha": "Na cozinha aberta com ilha de mármore",
    "cozinha_fazenda": "Na cozinha de fazenda com pia de louça",
    "cozinha_cabana": "Na cozinha de cabana de pinho",
    "cozinha_retro": "Na cozinha anos setenta de parede de madeira",
    "trailer": "Na cozinha corredor do trailer",
    "alpendre": "No alpendre telado dos fundos",
    "garagem": "Na bancada de garagem",
    "porao_oficina": "Na oficina do porão",
    "copa_igreja": "Na copa do salão comunitário",
    "rv": "Na cozinha do motorhome",
}

PT_CRED = {"confirma": "a fala CONFIRMA e transfere (o crescimento é PROVA)",
           "desmente": "a fala DESMENTE meio segundo depois (o crescimento vira GAG)"}


def resumo_pt(spec):
    """A frase que permite aprovar ou re-sortear em dois segundos."""
    et = "branca" if "white" in ETNIA[spec["pagina"]] else "negra"
    return (
        "%s, uma narradora de %d anos despeja %s por cima de %s pequeno que está "
        "SOLTO EM PÉ na bancada — e ele alonga na tela, escondido dentro da "
        "coluna de pó, enquanto a cara dela reage no lugar do espectador. Depois "
        "do crescimento, %s. Na cena 2 ela prepara %s com água morna e declara a "
        "receita incompleta sem o gelatin trick; o prop já crescido fica parado "
        "em quadro. Na cena 3 um homem de %d anos, de pele %s, segura o prop nas "
        "próprias mãos contra a frente da calça, olhando na lente, enquanto ela "
        "aponta sem encostar e chama o comentário. Três cenas de 8s; só a cena 1 "
        "cresce."
        % (PT_CENARIO.get(spec["cenario"]["id"], "Na cozinha"),
           spec["narradora"]["idade"], spec["substancia"]["fala"],
           spec["prop"]["nome"], PT_CRED[spec["credibilidade"]],
           spec["receita"]["fala"], spec["corpo_prova"]["idade"], et)
    )


def _refazer_falas(spec, rng):
    """Reescreve as tres falas com os eixos atuais do spec e re-checa o recibo.

    ⚠️ Os substantivos do nucleo sao PRESERVADOS quando ja' estao em cena — a
    rotacao e' do VIDEO, nao da fala.
    """
    o1 = sc.orgao_de(sys.modules[__name__], spec["falas"][0], NUCLEO[0])
    o2 = sc.orgao_de(sys.modules[__name__], spec["falas"][1], NUCLEO[1])
    o3 = sc.orgao_de(sys.modules[__name__], spec["falas"][2], NUCLEO[2])
    spec["falas"] = _montar_falas(rng, spec["substancia"], spec["receita"],
                                  [o1, o2, o3], spec["relacao"],
                                  spec["credibilidade"], spec["degrau"])
    spec["bancada"] = _bancada_livre(rng, spec["falas"], [], spec["receita"],
                                     spec["substancia"])


def _trocar_prop(spec, rng):
    """O prop nao entra em fala nenhuma — mas manda no CONTRASTE DE TOM (RS15).

    Trocar o prop sem re-sortear a substancia entregava po' claro sobre prop
    claro, e sem contraste a estria (a explicacao fisica do morph) some do
    quadro. O operador nao teria como consertar isso pela interface.
    """
    if spec["substancia"]["tom"] == spec["prop"]["tom"]:
        spec["substancia"] = rng.choice([s for s in SUBSTANCIAS
                                         if s["tom"] != spec["prop"]["tom"]])
        _refazer_falas(spec, rng)


def _trocar_substancia(spec, rng):
    """A substancia entra na cena 1 pelo `{s}` dos hooks dos degraus 2, 4 e 5 —
    trocar o eixo sem reescrever deixaria 'cornstarch' no pote e 'cinnamon' na
    boca. E ela tambem obedece ao contraste de tom (RS15)."""
    if spec["substancia"]["tom"] == spec["prop"]["tom"]:
        spec["prop"] = rng.choice([p for p in PROPS_MURCHOS
                                   if p["tom"] != spec["substancia"]["tom"]])
    _refazer_falas(spec, rng)


def _trocar_receita(spec, rng):
    """A receita e' o `{r}` da cena 2 — e o recibo tem de continuar mudo."""
    _refazer_falas(spec, rng)


def _par_dentro_do_teto(spec, rng):
    """⛔ ES11 — o teto de 30 anos vale TAMBEM quando o operador troca o eixo na
    mao, e nao valia.

    Medido no caminho da UI: trocar a narradora ou o corpo-prova pelo botao
    entregava pares de ate' 42 anos de diferenca na composicao da F12b, porque a
    guarda de idade morava so' no `sortear`. Regra que vale no sorteio e nao vale
    no clique nao e' regra — e' sorte. Quem se ajusta e' o corpo-prova: a peca
    que o operador acabou de escolher fica.
    """
    if abs(spec["corpo_prova"]["idade"] - spec["narradora"]["idade"]) \
            <= TETO_DIF_IDADE:
        return
    pool = [h for h in homens_de(spec["pagina"])
            if abs(h["idade"] - spec["narradora"]["idade"]) <= TETO_DIF_IDADE]
    if pool:
        spec["corpo_prova"] = rng.choice(pool)


def _trocar_narradora(spec, rng):
    """A idade dela e' metade da conta da relacao nomeada da cena 3, e a relacao
    manda na VOZ das provas: trocar a narradora recalcula as duas — e re-checa o
    teto de diferenca de idade do par (ES11)."""
    _par_dentro_do_teto(spec, rng)
    spec["relacao"] = _relacao(rng, spec["narradora"]["idade"],
                               spec["corpo_prova"]["idade"])
    _refazer_falas(spec, rng)


def _trocar_corpo_prova(spec, rng):
    """O corpo-prova nao mexe em fala nenhuma, mas mexe na RELACAO — que e'
    aritmetica de idade — e a relacao manda na voz da prova da cena 3."""
    _par_dentro_do_teto(spec, rng)
    spec["relacao"] = _relacao(rng, spec["narradora"]["idade"],
                               spec["corpo_prova"]["idade"])
    if voz_da_relacao(spec["relacao"]) == "terceiro":
        _refazer_falas(spec, rng)


def _trocar_analogia(spec, rng):
    """⛔ O botao `trocar` da UI sorteia do pool INTEIRO, e o pool tem a familia
    PRESSAO — que so' entra por ordem explicita (RS18).

    Medido: sem esta guarda, 4 de 14 cliques no eixo entregavam uma analogia de
    INFLACAO num TAKE cuja tese e' a escala diferencial, e o lote saia reprovado
    pelo proprio linter com o operador sem saber por que. A flag e' ORDEM; o
    clique nao e'. Nao mexe em fala nenhuma.
    """
    fam = spec.get("analogia_flag") or ANALOGIA_PADRAO
    if spec["analogia"]["familia"] != fam:
        spec["analogia"] = rng.choice([a for a in ANALOGIAS
                                       if a["familia"] == fam])


def _trocar_bancada(spec, rng):
    """⛔ O recibo tem de continuar MUDO depois do clique.

    Medido no caminho da UI: o botao sorteia do pool inteiro, e 60 de 3600
    cliques punham na imagem justamente o ingrediente que a boca ja' cita — o
    recibo que existe para dar lastro ao "full recipe" passava a repetir a fala.
    A guarda morava so' no `sortear`.
    """
    corpo = " ".join(spec["falas"]) + " " + spec["receita"]["fala"] + " " + \
        spec["substancia"]["fala"]
    if any(_cita(corpo, c) for c in spec["bancada"]["cabecas"]):
        spec["bancada"] = _bancada_livre(rng, spec["falas"],
                                         [spec["bancada"]["id"]],
                                         spec["receita"], spec["substancia"])


EIXOS_QUE_MEXEM_NA_COPY = {
    "analogia": _trocar_analogia,
    "bancada": _trocar_bancada,
    "prop": _trocar_prop,
    "substancia": _trocar_substancia,
    "receita": _trocar_receita,
    "narradora": _trocar_narradora,
    "corpo_prova": _trocar_corpo_prova,
}


def nova_fala(spec, i, rng):
    """Re-sorteia a fala da cena i (0-2) preservando o orgao que ja' esta' nela —
    a rotacao do substantivo e' do VIDEO, nao da fala."""
    o = sc.orgao_de(sys.modules[__name__], spec["falas"][i])
    return _montar_falas(rng, spec["substancia"], spec["receita"], [o, o, o],
                         spec["relacao"], spec["credibilidade"],
                         spec["degrau"])[i]


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def imprimir(spec, blocos, achados):
    print("=" * 72)
    print("SPEC — pagina %s | narradora %s (%d) | corpo-prova %s (%d) | "
          "cenario %s" % (spec["pagina"], spec["narradora"]["id"],
                          spec["narradora"]["idade"], spec["corpo_prova"]["id"],
                          spec["corpo_prova"]["idade"], spec["cenario"]["id"]))
    print("       prop %s | substancia %s | despejo %s | reacao %s | "
          "analogia %s" % (spec["prop"]["id"], spec["substancia"]["id"],
                           spec["despejo"]["id"], spec["reacao"]["id"],
                           spec["analogia"]["id"]))
    print("       receita %s | mecanismo %s | bancada %s | credibilidade %s | "
          "degrau %s" % (spec["receita"]["id"], spec["mecanismo"]["id"],
                         spec["bancada"]["id"], spec["credibilidade"],
                         spec["degrau"]))
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
    total = 0
    for i, fala in enumerate(spec["falas"], 1):
        n = _palavras(fala)
        total += n
        print("cena %d: %d palavras (piso %d, teto %d)"
              % (i, n, PISO_FALA[i], TETO_FALA[i]))
    print("video: %d palavras (faixa 82-%d)" % (total, TETO_TOTAL))
    if not achados:
        print("LINTER: OK — nenhuma violacao mecanica.")
    else:
        for nivel, msg in achados:
            print("[%s] %s" % (nivel, msg))
        n_erros = sum(1 for a in achados if a[0] == "ERRO")
        print("%d erro(s), %d aviso(s)." % (n_erros, len(achados) - n_erros))


# ---------------------------------------------------------------------------
# SELF-TEST DE ENTROPIA — a barra e' ordem permanente do operador:
# "nada menos que os demais agentes SHORT".
# ---------------------------------------------------------------------------
EIXOS_VISUAIS = ("narradora", "corpo_prova", "cenario", "prop", "substancia",
                 "despejo", "reacao", "analogia", "receita", "mecanismo",
                 "bancada")
MIN_OPCOES = 9          # piso por eixo visual
TETO_FREQ = 0.17        # nenhum item pode concentrar mais que isso
MIN_COPY = {"HOOKS": 16, "FUNDIDAS": 13, "CTAS": 14, "GATES": 11}


def _contrato_dos_pools(falhas):
    """⛔ Os pools tem contratos que o motor DERIVA — e derivacao muda que nao e'
    cobrada e' derivacao que quebra calada.

    Cada um destes ja' seria um bug silencioso: um `monte` sem " spreading" faria
    o anel do IMAGE 01 sair com a frase inteira do cronometro; uma `caixa` sem
    recipiente conhecido poria "the container" no TAKE; um `depois`/`dele` fora do
    padrao de escala mataria a RS8 por falso positivo.
    """
    for s in SUBSTANCIAS:
        if " spreading" not in s["monte"]:
            falhas.append("SUBSTANCIAS[%s].monte sem ' spreading' — o anel do "
                          "IMAGE 01 sai errado" % s["id"])
        if "turned mouth-down" not in s["caixa"] or \
                "in her raised hand" in _pote(s["caixa"]):
            falhas.append("SUBSTANCIAS[%s].caixa nao corta em 'turned "
                          "mouth-down' — o IMAGE 01 sai com duas maos" % s["id"])
        if _recipiente(s["caixa"]) == "container":
            falhas.append("SUBSTANCIAS[%s].caixa sem recipiente conhecido"
                          % s["id"])
        if _palavras(s["fala"]) > 2:
            falhas.append("SUBSTANCIAS[%s].fala com mais de 2 palavras — o pior "
                          "caso do teto da cena 1 depende disso" % s["id"])
    for p in PROPS_MURCHOS:
        if not _escala(p["depois"], "her") or not _escala(p["dele"], "his"):
            falhas.append("PROPS_MURCHOS[%s] sem declaracao de escala legivel"
                          % p["id"])
        elif _escala_bloco(p["depois"]) != _escala_bloco(p["dele"]):
            falhas.append("PROPS_MURCHOS[%s]: `depois` e `dele` declaram escalas "
                          "diferentes (RS8)" % p["id"])
        if "no longer than her palm" not in p["antes"]:
            falhas.append("PROPS_MURCHOS[%s].antes sem a regua do estado ANTES "
                          "(R1)" % p["id"])
    for m in MECANISMOS_PROP:
        if "gelatin" not in m["plantado"] or "gelatin" not in m["curto"]:
            falhas.append("MECANISMOS_PROP[%s] sem nomear gelatin" % m["id"])
    for f in FUNDIDAS:
        if "gelatin trick" not in f["txt"] or "{o}" not in f["txt"]:
            falhas.append("FUNDIDAS sem 'gelatin trick' ou sem {o}: %r"
                          % f["txt"][:40])
    for p in PROVAS:
        if "{o}" not in p["txt"]:
            falhas.append("PROVAS sem {o} — a prova fica sem referente: %r"
                          % p["txt"])
    # ⛔ o campo `cred` do BULLETS e' filtro de MODO: sem ele o bullet nao sabe
    # em que video esta' e o modo `confirma` fecha a cena 1 desmentindo a
    # propria prova (medido: 42,0% antes do conserto).
    for b in BULLETS:
        if b["cred"] not in ("ambas",) + CREDIBILIDADES:
            falhas.append("BULLETS com cred '%s' desconhecido: %r"
                          % (b["cred"], b["txt"][:40]))
        if RS10_PRAZO.search(b["txt"]):
            falhas.append("BULLETS com marcador de prazo: %r" % b["txt"])
    for cred in CREDIBILIDADES:
        eleg = [b["txt"] for b in BULLETS if b["cred"] in ("ambas", cred)]
        for nomeia in (True, False):
            n = len([b for b in eleg if ("{o}" in b) != nomeia])
            if n < 3:
                falhas.append("modo '%s' com so' %d bullet(s) para hook que %s "
                              "nomeia o orgao" % (cred, n,
                                                  "" if nomeia else "nao"))
    for c in CTAS:
        if sc.CTA_LITERAL not in c:
            falhas.append("CTAS sem o literal %r: %r" % (sc.CTA_LITERAL, c))
        if not sc.ISCA_CTA.search(c):
            falhas.append("CTAS sem isca (nao diz o que chega): %r" % c)
    # RS15 — o contraste de tom tem de ser possivel dos DOIS lados
    for tom in ("claro", "escuro"):
        if not [s for s in SUBSTANCIAS if s["tom"] != tom]:
            falhas.append("nao ha' substancia que contraste com prop '%s'" % tom)
    # RS18 — a familia default tem de encher o eixo sozinha
    ext = [a for a in ANALOGIAS if a["familia"] == "extensao"]
    if len(ext) < MIN_OPCOES:
        falhas.append("familia 'extensao' com %d analogias (minimo %d) — e' a "
                      "unica que roda sem flag" % (len(ext), MIN_OPCOES))


def autoteste(n_por_pagina=80, seed=7, credibilidade=None, degrau=None,
              analogia=None):
    falhas = []
    _contrato_dos_pools(falhas)

    tamanhos = {"NARRADORAS": len(NARRADORAS),
                "CORPOS_PROVA_CLARA": len(CORPOS_PROVA_CLARA),
                "CORPOS_PROVA_ESCURA": len(CORPOS_PROVA_ESCURA),
                "PROPS_MURCHOS": len(PROPS_MURCHOS),
                "SUBSTANCIAS": len(SUBSTANCIAS), "DESPEJOS": len(DESPEJOS),
                "REACOES": len(REACOES), "ANALOGIAS": len(ANALOGIAS),
                "CENARIOS": len(CENARIOS), "BANCADAS": len(BANCADAS),
                "RECEITAS": len(RECEITAS),
                "MECANISMOS_PROP": len(MECANISMOS_PROP)}
    for nome, n in sorted(tamanhos.items()):
        if n < MIN_OPCOES:
            falhas.append("eixo visual %s com %d opcoes (minimo %d)"
                          % (nome, n, MIN_OPCOES))
    copy = {"HOOKS": len(HOOKS), "CONFIRMACOES": len(CONFIRMACOES),
            "DESMENTIDOS": len(DESMENTIDOS), "BULLETS": len(BULLETS),
            "FUNDIDAS": len(FUNDIDAS), "PROVAS": len(PROVAS),
            "BARREIRAS": len(BARREIRAS), "CTAS": len(CTAS), "GATES": len(GATES)}
    for nome, piso in sorted(MIN_COPY.items()):
        if copy[nome] < piso:
            falhas.append("pool de copy %s com %d entradas (minimo %d)"
                          % (nome, copy[nome], piso))

    # --- regra de POOL dos gates -------------------------------------------
    # ⚠️ O vocativo so' pode existir nos GATES; se escorregar para BARREIRAS ou
    # CTAS, a cena 3 passa a ter dois num video so' e o vicio que o operador
    # mediu (31-73%) volta.
    n_brother = sum(1 for g in GATES if "brother" in g.lower())
    n_voc = sum(1 for g in GATES if _achar(g, VOCATIVOS))
    if n_brother > 2:
        falhas.append("GATES: %d com 'brother' (maximo 2)" % n_brother)
    if n_voc >= len(GATES) / 2.0:
        falhas.append("GATES: %d de %d com vocativo — a maioria tem de vir sem "
                      "nenhum" % (n_voc, len(GATES)))
    for nome, pool in (("BARREIRAS", BARREIRAS), ("CTAS", CTAS)):
        sujos = [x for x in pool if _achar(x, VOCATIVOS)]
        if sujos:
            falhas.append("%d entrada(s) de %s com vocativo — o vocativo so' "
                          "mora nos GATES" % (len(sujos), nome))

    # --- piso de idade ------------------------------------------------------
    novas = [x["id"] for x in NARRADORAS if x["idade"] < IDADE_MINIMA_NARRADORA]
    if novas:
        falhas.append("RS19: narradora(s) abaixo do piso de %d anos: %s"
                      % (IDADE_MINIMA_NARRADORA, ", ".join(novas)))

    # --- o orcamento e' ALCANCAVEL? -----------------------------------------
    # ⚠️ Enumeracao exaustiva do pior e do melhor caso de cada cena. Foi assim
    # que se descobriu, no TROCA, que o teto de nenhuma cena era alcancavel
    # (AVISO virava codigo morto) e que a cena 2 ficava abaixo do piso em 48%
    # dos sorteios. As duas bordas sao MEDIDAS, nao estimadas.
    ex_s = max(_w(s["fala"]) for s in SUBSTANCIAS) - 1
    ex_o = max(_w(o) for o in NUCLEO) - 1
    for deg in DEGRAUS:
        hs = [h for h in HOOKS if h["degrau"] == deg]
        for cred in CREDIBILIDADES:
            b2 = CONFIRMACOES if cred == "confirma" else DESMENTIDOS
            # ⛔ o pool de bullet ENCOLHE por modo desde 2026-08-02 (campo
            # `cred`): a enumeracao tem de enxergar o mesmo pool que o sorteio,
            # senao ela prova a viabilidade de um pool que nao roda.
            eleg = [b["txt"] for b in BULLETS if b["cred"] in ("ambas", cred)]
            viavel = 0
            for h in hs:
                nomeia = "{o}" in h["txt"]
                base = _w(h["txt"]) + (ex_o if nomeia else 0) + \
                    (ex_s if "{s}" in h["txt"] else 0)
                bl = [b for b in eleg if ("{o}" in b) != nomeia]
                combos = [(x, y) for x in b2 for y in bl
                          if PISO_FALA[1] <= base + _w(x) + _w(y)
                          + (ex_o if "{o}" in y else 0) <= TETO_FALA[1]
                          and not (_repete(h["txt"], y)
                                   or _repete(h["txt"], x) or _repete(x, y))]
                viavel += len(combos)
                if not combos:
                    falhas.append("cena 1 sem combinacao valida no degrau %d / "
                                  "%s para o hook %r" % (deg, cred,
                                                         h["txt"][:34]))
            print("  cena 1 · degrau %d · %-8s  %4d combinacoes validas"
                  % (deg, cred, viavel))
    # ⚠️ A cena 2 e' UMA fala so', e o motor escolhe entre as que CABEM. Entao o
    # que se cobra nao e' "a pior entrada cabe" e sim "para toda combinacao de
    # receita, orgao e modo sobra pelo menos uma fundida dentro da faixa" — que
    # e' a condicao real de nunca haver fallback.
    pior = None
    for cred in CREDIBILIDADES:
        pool = [f for f in FUNDIDAS if f["cred"] in ("ambas", cred)]
        for r in RECEITAS:
            for o in NUCLEO:
                cabem = [f for f in pool
                         if PISO_FALA[2] <= _w(f["txt"].format(r=r["fala"], o=o))
                         <= TETO_FALA[2]]
                if pior is None or len(cabem) < pior[0]:
                    pior = (len(cabem), cred, r["id"], o)
    print("  cena 2 · pior caso: %d fundidas dentro da faixa (%s / %s / %s)"
          % pior)
    if pior[0] == 0:
        falhas.append("cena 2 sem fundida na faixa %d-%d para %s"
                      % (PISO_FALA[2], TETO_FALA[2], pior[1:]))
    piso3 = (min(_w(p["txt"]) for p in PROVAS) + min(_w(x) for x in BARREIRAS)
             + min(_w(x) for x in CTAS) + min(_w(x) for x in GATES))
    if piso3 < PISO_FALA[3]:
        falhas.append("cena 3 pode sair com %d palavras (piso %d)"
                      % (piso3, PISO_FALA[3]))

    # --- os sorteios --------------------------------------------------------
    rng = random.Random(seed)
    freq, total_eixo, erros, avisos, n = {}, {}, 0, 0, 0
    palavras = {1: [], 2: [], 3: []}
    for pag in sorted(ETNIA):
        ledger = {}
        for _ in range(n_por_pagina):
            spec = sortear(pag, rng, ledger, credibilidade, degrau, analogia)
            blocos = montar(spec)
            for nivel, msg in lint(spec, blocos):
                if nivel == "ERRO":
                    erros += 1
                    if erros <= 5:
                        print("  ERRO (%s): %s" % (pag, msg))
                else:
                    avisos += 1
                    if avisos <= 3:
                        print("  AVISO (%s): %s" % (pag, msg))
            # o corpo-prova e' pool POR ETNIA: medir junto com as outras paginas
            # diluiria a concentracao e mentiria a favor.
            for eixo in EIXOS_VISUAIS:
                chave = (eixo + ":" + ETNIA[pag]) if eixo == "corpo_prova" else eixo
                freq.setdefault(chave, {})
                freq[chave][spec[eixo]["id"]] = freq[chave].get(spec[eixo]["id"], 0) + 1
                total_eixo[chave] = total_eixo.get(chave, 0) + 1
            for i, fala in enumerate(spec["falas"], 1):
                palavras[i].append(_palavras(fala))
            _anotar(ledger, spec)
            n += 1

    # ⚠️ O TETO DE CONCENTRACAO E' AJUSTADO QUANDO UMA FLAG ENCOLHE O POOL, e
    # so' nesse caso. Com `--analogia pressao` sobram 4 opcoes, e 4 opcoes tem
    # 25% de concentracao MINIMA por aritmetica: reprovar ali seria reprovar o
    # que esta' certo, que e' o modo de falha do proprio medidor
    # (licoes-de-construcao §16). ⛔ Sem flag, o teto continua sendo 17%.
    teto_eixo = {}
    if analogia:
        n_fam = len([a for a in ANALOGIAS if a["familia"] == analogia])
        teto_eixo["analogia"] = max(TETO_FREQ, 1.35 / n_fam)

    print("\nENTROPIA — %d sorteios (%d por pagina)" % (n, n_por_pagina))
    print("-" * 72)
    for chave in sorted(freq):
        c = freq[chave]
        teto = teto_eixo.get(chave, TETO_FREQ)
        topo, qtd = max(c.items(), key=lambda kv: kv[1])
        pc = qtd / float(total_eixo[chave])
        marca = "OK " if pc <= teto else "X  "
        print("  %s %-28s %2d opcoes | mais sorteado %-22s %4.1f%% (teto %.0f%%)"
              % (marca, chave, len(c), topo, pc * 100, teto * 100))
        if pc > teto:
            falhas.append("eixo %s concentra %.1f%% em '%s' (teto %.0f%%)"
                          % (chave, pc * 100, topo, teto * 100))

    print("\nUSO DO ORCAMENTO — medido contra a CAPACIDADE REAL, nao contra o teto")
    print("-" * 72)
    # capacidade real por cena, pelas taxas da propria fonte (3,61-4,4 p/s); a
    # cena 1 desconta os 0,8s de silencio obrigatorio da R7 -> 7,2s.
    capacidade = {1: (26, 31), 2: (29, 35), 3: (29, 35)}
    tot = 0.0
    for i in (1, 2, 3):
        v = palavras[i]
        media = sum(v) / float(len(v))
        tot += media
        print("  cena %d: min %2d · media %4.1f · max %2d | piso %d teto %d | "
              "capacidade real %d-%d (%.0f%%)"
              % (i, min(v), media, max(v), PISO_FALA[i], TETO_FALA[i],
                 capacidade[i][0], capacidade[i][1],
                 100.0 * media / capacidade[i][1]))
    print("  video: media %.1f palavras (faixa da doutrina 82-%d)"
          % (tot, TETO_TOTAL))

    print("\nPOOLS DE COPY")
    print("-" * 72)
    for nome in sorted(copy):
        print("  %-14s %d" % (nome, copy[nome]))
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


def stats(credibilidade=None, degrau=None, analogia=None):
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
    return autoteste(credibilidade=credibilidade, degrau=degrau,
                     analogia=analogia)


def main():
    ap = argparse.ArgumentParser(
        description="Randomizador do agente RESSURREICAO SHORT")
    ap.add_argument("--pagina", choices=sorted(ETNIA))
    ap.add_argument("--n", type=int, default=1)
    ap.add_argument("--seed", type=int, help="reproduzivel")
    ap.add_argument("--dry-run", action="store_true", help="nao grava ledger")
    # ⭐ A leitura do crescimento e' ALCADA DO ED. Default `confirma`, que e' a
    # forma validada deste agente; `desmente` e' o TR8 do TROCA e fica como
    # variante, nao como padrao.
    ap.add_argument("--credibilidade", choices=CREDIBILIDADES,
                    help="o que a fala faz DEPOIS do crescimento — "
                         "confirma (default, o crescimento e' PROVA) | "
                         "desmente (o crescimento vira GAG)")
    ap.add_argument("--degrau", type=int, choices=DEGRAUS,
                    help="trava a escada de moderacao do hook — 2 assertiva | "
                         "3 condicional (default, a unica validada) | "
                         "4 atribuicao | 5 plana")
    ap.add_argument("--analogia", choices=FAMILIAS_ANALOGIA,
                    help="familia da analogia fisica — extensao (default, por "
                         "forca da R2-emenda) | pressao (inflacao: contradiz a "
                         "escala diferencial, so' por ordem explicita)")
    ap.add_argument("--stats", action="store_true",
                    help="uso dos pools + self-test de entropia")
    a = ap.parse_args()

    if a.stats:
        return stats(a.credibilidade, a.degrau, a.analogia)

    if not a.pagina:
        ap.error("informe --pagina <joe|ray|matt|marcus|chuck> (ou --stats)")

    rng = random.Random(a.seed)
    ledger = _carregar_ledger()
    saida = 0
    for i in range(a.n):
        spec = sortear(a.pagina, rng, ledger, a.credibilidade, a.degrau,
                       a.analogia)
        blocos = montar(spec)
        achados = lint(spec, blocos)
        if a.n > 1:
            print("\n\n########## VIDEO %d/%d ##########\n" % (i + 1, a.n))
        imprimir(spec, blocos, achados)
        if any(x[0] == "ERRO" for x in achados):
            saida = 1
        # o lote inteiro se lembra de si mesmo; so' a GRAVACAO respeita o
        # --dry-run (mesma logica do botao "marcar como usado" do app)
        _anotar(ledger, spec) if a.dry_run else _gravar_ledger(ledger, spec)
    return saida


if __name__ == "__main__":
    sys.exit(main())
