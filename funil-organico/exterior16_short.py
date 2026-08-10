#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE EXTERIOR SHORT — 3 cenas de 8 segundos (24s), SHORT NATIVO.

Doutrina: AGENTE_ED_EXTERIOR_V1.md (regras EX1-EX17)
Fonte:    concorrentes/angela-brooks-mapa-visual.md — reel 1338568635113668,
          30,30s, 1080x1920, UM corte so' (em 5,30s). Transcript integral
          Whisper large-v3 + frames do hook a 3 fps. 2026-08-03.
          519 curtidas · 779 comentarios · razao comentario/curtida 1,50, a mais
          alta do garimpo. ⚠️ n=1, sem views: o que justifica o agente nao e' o
          numero, e' o DISPOSITIVO (a REGRA, EX2, e o gesto de dois, EX4).

O nome e' duplo e os dois sentidos valem: o argumento e' sobre o EXTERIOR (o que
se joga por cima) e a cena inteira acontece num EXTERIOR (a varanda).

⛔⛔ A LEI DESTE AGENTE (EX1) — leia antes de qualquer outra linha
----------------------------------------------------------------
Ordem literal do operador, 2026-08-03:

    "A copy do video que te passei e' a FONTE DA VERDADE e voce ira usa-la
     trazendo-a para nosso agente. PARE DE CRUZAR OS DADOS com o que a regra de
     moderacao determina para o build desse agente. So' alinhe o que tange ao
     nosso mecanismo: gelatin trick e comment gelatin."

Sem ambiguidade:
  1. ⭐ A fala da fonte (§3 do mapa) entra COMO ELA E'. Verbatim.
  2. ⛔ A copy DESTE agente nao e' filtrada pela nossa doutrina de moderacao.
     Nao se suaviza, nao se troca palavra por eufemismo, nao se "melhora".
  3. ⭐ O UNICO alinhamento e' o MECANISMO: onde a fonte diz `one ingredient`,
     entra `gelatin trick`; e o CTA carrega `Comment gelatin,`.
  4. ⛔ E nao se inventa copy. A variancia sai de RECOMBINAR e REORDENAR dentro
     do vocabulario da fonte, nunca de escrever claim novo.
  5. ⚠️ A UNICA edicao autorizada na fala da fonte e' a saida de `overnight` da
     primeira frase. Fica `Pour baking soda on your {o} and watch it swell up.`

⚠️ E o que a EX1 NAO revoga: `gelatin trick` e `Comment gelatin,` nao sao
moderacao, sao a automacao de DM — a legenda nasce no Veo Editor, do Whisper,
EM CIMA DO AUDIO GERADO, e keyword variavel faz o modelo parafrasear. Sao linter
no `short_comum.py` e continuam valendo. Idem a trava de texto queimado (EX17):
e' PIPELINE, nao moderacao.

⛔⛔ EMENDA DA EX1 PARA A FAMILIA 16s — 2026-08-10, ORDEM DIRETA DO OPERADOR
---------------------------------------------------------------------------
    *"agentes troca16, ressurreicao16, exterior16, flagrante16, pee16,
     escandalo16, colo16 precisam de reformulacao TOTAL de suas copys"*

A EX1 travava a fala no VERBATIM da Angela Brooks. Essa trava **nao vale mais
para o motor de 16s** — e a revogacao e' dele, nao minha. O que a substitui e'
o CONTRATO DE COPY 16s (`funil-organico/CONTRATO-COPY-16S.md`, sete travas
CT1-CT7 em `short_comum.lint_copy16`), nascido de uma revisao adversarial de 6
lentes sobre tres lotes renderizados.

⚠️ E ESTE MOTOR ERA O PIOR DOS SETE, medido em 200 sorteios ANTES da reforma:
    CT1 (frase depois do CTA) ........ 100%
    CT2 (take 1 sem falha enunciada) . 100%
    CT3 (`gelatin trick` rotulo nu) .. 100%
    CT4 (apelido muda no corte) ...... 100%
    CT6 (CTA sem endereco de entrega)  100%
⛔ Nenhum desses defeitos aparece relendo o pool: todos vivem na COMBINACAO. E'
por isso que o contrato e' CODIGO (`_ct16` no `lint`), nao paragrafo.

⚠️ O que a emenda NAO revoga, e continua sendo a lei deste angulo:
  · A REGRA (EX2) — o argumento do de-fora-contra-o-de-dentro. Ele desceu para
    a batida do DESMENTIDO da cena 1, que e' onde ele e' CONCRETO (`powder on
    the outside does nothing`), e o herdeiro funcional dele na cena 2 continua
    sendo o MECANISMO (sangue + pressao + orgao), cobrado em ERRO por
    `_ex2_regra`. E' a unica peca que nenhum outro agente do parque tem.
  · A ISCA ABSURDA do bicarbonato (EX8: nada cresce em CENA, so' na fala).
  · `gelatin trick`, `Comment gelatin,` e a trava de texto queimado.
⛔ O que a emenda revoga: o verbatim. As sete travas ganham da fonte quando as
duas brigam, porque a ordem de 2026-08-10 e' posterior e nominal a este motor.

⛔ SHORT NATIVO — NAO DERIVA DE MOTOR LONGO
Nao existe e nao deve existir um motor longo de 5 cenas deste angulo, e ⛔ nao
existe arquivo com label `lucas` — os `*_lucas` sao de terceiro, moram em
`agentes-de-terceiros/` e nao se le', nao se mede e nao se cita. Como o
`troca_short.py`, o `escandalo_short.py` e o `ressurreicao_short.py`, este
arquivo e' motor completo (pools proprios) e passa A SI MESMO como `base` para a
maquinaria compartilhada do `short_comum.py` (`lint_curto`, `selar_takes`,
`lint_isca_cta`, `lint_cta_literal`, `lint_nada_cresce`).

O QUE ESTE AGENTE TEM E NENHUM OUTRO NOSSO TEM
-----------------------------------------------
[EX2] ⭐⭐ A REGRA — `Nothing you pour on the outside changes what's happening on
      the inside.` Ela faz TRES trabalhos de uma vez: mata o truque caseiro que a
      cena 1 acabou de executar na tela (a demo vira prova contra si mesma),
      converte a objecao do cetico em alianca (Benson §3, `and you're right not
      to`) e estabelece a categoria do produto sem nomea-lo — se o de fora nao
      resolve, o que resolve e' de dentro, e o ingrediente entra ja' ganhando.
      ⛔ Sem ela o agente nao existe: o que sobra e' uma isca absurda que o
      RESSURREICAO e o TROCA ja' fazem melhor. E' LINTER (EX2), nao comentario.
[EX4] ⭐ O GESTO DE DOIS, travado elemento por elemento no frame 0 da fonte: ela
      pela esquerda com a caixa de boca para baixo a ~45°, o geoduck vertical com
      o sifao para cima, ele pela direita CORTADO NO PEITO com as duas maos na
      concha, uma acima da outra.
[EX5] ⭐ O HOMEM SEM ROSTO e' ECONOMIA, nao descuido: um rosto a menos para
      manter identico entre tres blocos de 8s gerados separadamente — o problema
      que mais custa nos nossos lotes (a ancora `the same N-year-old` do
      `lint_curto` nasceu de um render que devolveu um senhor de oculos e bigode
      no lugar do corpo-prova). ⛔ NUNCA por o rosto dele em quadro.
[EX8] ⛔⛔ NESTE AGENTE NADA CRESCE. Nao existe morph, nao existe escala, nao
      existe antes/depois. O `swell up` mora SO' na isca falada, e a isca e'
      demolida meio segundo depois: a promessa de inchaco e' DO VILAO. Se o prop
      crescer na tela, A REGRA passa a contradizer a imagem e o agente desaba.
      `lint_nada_cresce(..., excecao=())` — e este e' o primeiro motor do repo
      que pode chamar assim, porque nenhuma cena tem licenca para crescer.

⛔⛔ CONFERENCIA DA REFORMA — 2026-08-10, LEITURA EM VOZ ALTA
-------------------------------------------------------------
A reforma do CONTRATO DE COPY 16s zerou os sete CTs, e as sete travas
continuam zeradas. ⚠️ MAS AS TRAVAS SAO ESTRUTURAIS, e nenhuma delas pergunta
se um americano de 50-70 anos ENTENDE a frase ouvindo uma vez. Seis entradas
passavam nos sete CTs e falhavam nessa leitura:

    DESMENTIDOS   ✗ The outside was never the problem.      `outside` sem dono
    DESMENTIDOS   ✗ The outside does nothing for you.       idem
    FALHAS16      ✗ You still lose it before she does.      `does` = verbo proxy
    DISCLOSURES16 ✗ ... gave {par} pressure back.           `pressure` = hipertensao
    DISCLOSURES16 ✗ ... works on {par}'s blood.             rotulo nu disfarcado
    FOLLOWS16     ✗ Followers only.                         condicao, nao pedido

⭐ CADA UMA VIROU LENTE no `_contrato_dos_pools` — julgamento que nao vira
cobranca volta no proximo pool (licoes §36). ⛔ E NENHUM POOL ENCOLHEU: as seis
foram repostas por entradas do mesmo beat, marcadas uma a uma no fim de cada
lista, porque a ordem permanente do operador proibe regressao de entropia. As
reposicoes sao COPY escrita pela conferencia — se o Ed nao gostar da forma, o
lugar de trocar esta' assinalado.
⚠️ O cabecalho dos DESMENTIDOS foi pego MENTINDO sobre o proprio pool
(afirmava "6 das 10 opoem fora/dentro"; era UMA). Os numeros de cabecalho deste
arquivo passaram a ser contados, nao afirmados.

⚠️⚠️ DIVERGENCIAS DECLARADAS — cada uma com o motivo e o numero
---------------------------------------------------------------
Divergencia calada e' a §3 do licoes-de-construcao com outra roupa. As quatro:

1) ⭐ PISO_FALA[2] = 24 — ⚠️ E ISTO JA' NAO E' DIVERGENCIA: a EX12 da doutrina foi
   emendada em 2026-08-03 e ja' escreve `{1: 22, 2: 24, 3: 30}`. Motor e doutrina
   dizem o MESMO numero. ⛔ O texto que ficava aqui ("E A DOUTRINA DIZ 28")
   sobreviveu a' emenda e mandava o operador procurar um conflito que nao existe,
   que e' a §3 das licoes pelo avesso. Fica o REGISTRO da conta, que continua
   valendo, e ⛔ reverter para 28 e' alcada do Ed.
   A CONTA, medida por enumeracao exaustiva das 90 combinacoes de cena 2
   (REGRAS 9 x MECANISMOS_FALA 10), faixa real 21-30 palavras:
       piso 28 ->  6 de 90 combinacoes, e SO' 2 das 10 entradas de
                   MECANISMOS_FALA ficam sorteaveis
       piso 26 -> 27 de 90, 7 de 10 entradas, a mais sorteada concentra 33,3%
       piso 24 -> 66 de 90, 10 de 10 entradas, a mais sorteada concentra 13,6%
   (marginal, enumeracao exaustiva; MEDIDO em 400 sorteios com piso 24: 11,5%)
   O piso da doutrina veio das 30 palavras da FONTE nesses tres beats, e o
   motivo escrito dele e' "cena abaixo do piso = beat da fonte perdido". Aqui
   esse motivo esta' satisfeito POR CONSTRUCAO e nao por contagem: ⛔ TODA
   entrada de REGRAS carrega A REGRA e ⛔ TODA entrada de MECANISMOS_FALA carrega
   circulacao E pressao — e desde 2026-08-03 as duas coisas sao COBRADAS no
   `_contrato_dos_pools`, porque enquanto eram so' comentario uma entrada ficou
   sem `circulation` e 8,2% dos videos perdiam o beat que a conta promete.
   Nenhum beat cai. Com 28 o piso deixaria de proteger beat e passaria a destruir
   a entropia que o operador exigiu como ordem permanente ("nada menos que os
   demais agentes SHORT").
   ⚠️ O teto NAO foi tocado: 32 e' o da doutrina, e teto estourado e' atropelo.
   ⚠️ E O OUTRO LADO DO MESMO FILTRO, que a tabela da doutrina nao trazia: o piso
   nao move so' a concentracao de MECANISMOS_FALA, move a de REGRAS junto —
   marginal 33,3% com piso 28, 25,9% com 26 e 15,2% com 24. O 24 continua sendo o
   melhor dos tres NOS DOIS LADOS; o que faltava era publicar o lado que sobra.

2) ⭐ A CENA 3 USA UM POOL FUNDIDO (`FUNDIDAS`), e' a saida (a) da EX12, e as
   duas pontas da spec de construcao (`PROBLEMAS` e `OPEN_LOOPS` separados)
   foram fundidas nele. A conta que obriga: com os dois pools separados a cena 3
   sai com 33-43 palavras contra um teto de 34 — sobrariam ~5 das 81
   combinacoes, todas forcadas ao CTA mais curto e ao gate mais curto, o que
   mataria a entropia de CTAS e GATES junto. A propria doutrina ja' prescreve a
   fusao ("e' o que o motor faz por default, e sai 31-33 palavras"). Medido com
   o pool fundido: 308 das 648 combinacoes ficam na faixa 30-34.
   ⚠️ ERAM 401 ate' 2026-08-03, e o custo esta' declarado: as FUNDIDAS passaram a
   carregar OBRIGATORIAMENTE a oracao da consequencia (`the body can't keep up`),
   entao a mais curta subiu de 13 para 14 palavras e sobrou menos espaco para o
   CTA e o gate. Medido em 400 sorteios, a concentracao do CTA mais sorteado foi
   de 19,5% para 24,2% e a do gate de 24,2% para 26,8%. ⛔ Foi troca CONSCIENTE:
   67% dos videos diziam a causa sem dizer o que ela quebra (§17), e beat da fonte
   perdido custa mais que 5 pontos de concentracao num pool de copy — que a EX15
   manda RELATAR, nao zerar.

3) ⭐ A VARANDA E' A MESMA NAS TRES CENAS (EX11), e por isso ⛔ NAO EXISTE o eixo
   `AMBIENTES_B` (a sunroom) que a spec de construcao propunha para as cenas 2 e
   3. A fonte corta para talking-head puro em 5,30s; a doutrina diz, com o
   motivo escrito, que esse e' um dos dois unicos elementos da fonte que NAO
   copiamos (o outro e' a legenda queimada, EX17): talking-head solo e' pobreza
   de bit visual, e cenario unico da' continuidade de graca entre tres blocos
   gerados separadamente. A entropia que a sunroom carregava foi para o eixo
   MESAS (a superficie da varanda onde a gelatina fica plantada desde o frame 1
   da cena 2) — 12 opcoes, sem perder contagem de eixo.
   ⚠️ E ATE' 2026-08-03 ESSA COMPENSACAO ERA NOMINAL: o campo `mesa` (a descricao
   inteira: "a wooden crate stood on end as a table") NAO era emitido em bloco
   nenhum — 0 de 400 videos —, so' o rotulo curto saia, e o IMAGE 02/03 abria com
   `stands behind the crate`, artigo definido para um objeto que o prompt nunca
   apresentava. ⛔ A CONTAGEM de eixo estava preservada e a CARGA VISUAL nao
   chegava ao prompt, que e' otimizar contra a metrica em vez de contra o objetivo
   (licoes §15/§16). Agora a primeira mencao e' a descricao e as seguintes sao o
   rotulo curto.

4) ⭐ OS DESCRITORES DE CABELO E DE PELE SAO NEUTROS DE ETNIA (EX10), e por isso
   `a full soft afro`, `waist-length box braids` e `a long twist-out` — que
   estavam na spec de construcao — NAO entraram, e nem `pale forearms`,
   `freckled forearms` ou cor de olho clara. ⛔ Nao e' preciosismo: o modelo de
   etnia deste agente e' o do NECROSE — UM pool so' de cada personagem, ZERO
   etnia nas entradas, `ETNIA[pagina]` injetada na montagem —, e descritor
   etnico por dentro do cabelo quebra a injecao em duas das cinco paginas. Uma
   entrada tem de servir pagina branca E pagina negra; a textura sai da
   injecao. A propria spec de construcao pedia "ZERO mencao a etnia nas
   entradas" e depois escrevia entradas que a mencionam — vale a regra.
   ⚠️ Custo declarado: o pool perdeu cor de cabelo e cor de olho como eixos de
   distincao, e a diferenca passa a vir de CORTE, COMPRIMENTO, PORTE, OCULOS DE
   SOL e ANCORA FACIAL. Medido no `medir_personagens.py`: nenhum eixo zerado.

Uso:
    python funil-organico/exterior_short.py --pagina joe --n 2
    python funil-organico/exterior_short.py --pagina marcus --n 3 --seed 42
    python funil-organico/exterior_short.py --pagina ray --n 1 --dry-run
    python funil-organico/exterior_short.py --stats
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
# ⛔ LEDGER PROPRIO. O de 24s e o de 16s nao se falam: sao formatos
# diferentes, e um lote de 16s nao pode gastar o historico do outro.
LEDGER = os.path.join(AQUI, ".exterior-16-ledger.json")

TITULO = "AGENTE EXTERIOR 16"
SUBTITULO = ("2 takes de 8s = 16 segundos · o despejo na varanda, e a regra "
             "com o corpo-prova no mesmo quadro · nada do que voce joga por "
             "fora muda o que acontece por dentro")
SLUG = "exterior-16"

# ⛔⛔ DUAS CENAS, e a segunda e a FUSAO das cenas 2 e 3 do motor de 24s.
# As duas ja' aconteciam no MESMO deck — o que muda entre elas e' quem
# esta' em quadro (a 2 e' ela sozinha atras da mesa de ferro; a 3 traz o
# corpo-prova cortado no peito) e ONDE esta' o geoduck (na mesa / nas maos
# dele). A fusao fica com o quadro da 3, que e' o payoff, e leva a REGRA e
# o MECANISMO para dentro da fala.
CENAS_UI = ["1 · A ISCA E O DESMENTIDO", "2 · A REGRA + PROVA + CTA"]


# ---------------------------------------------------------------------------
# ORCAMENTO — EX12. Piso E teto, e os dois sao mecanicos.
# ---------------------------------------------------------------------------
# A conta da doutrina, passo a passo:
#   fonte ......... 111 palavras / 30,30s ............. = 3,66 p/s
#   nosso video ... 3 x 8s ............................ = 24,0 s
#   a 3,66 p/s (a taxa da PROPRIA fonte), 24s comportam = 88 palavras
#   logo o arco cabe com CORTE DE 21% .................. (111 -> 88)
# ⚠️ E a nossa entrega MEDIDA e' 2,96 p/s (TROCA, 400 sorteios) = 71 palavras em
# 24s. Se este motor entregar na nossa taxa habitual, 17 palavras do arco caem —
# e as que caem sao as DO MEIO, porque as pontas sao literais travados. Por isso
# o PISO pesa tanto quanto o teto aqui: cena abaixo do piso = beat da fonte
# perdido, e o arco da fonte e' a lei (EX1).
#
# 🔴 TENSAO ARITMETICA ABERTA, e ela e' da doutrina: a capacidade medida de um
# take cheio de 8s e' 27-32 palavras (3,4-4,0 p/s, medido no ESCANDALO). A cena 3
# NO TETO pede 4,25 p/s — acima da banda e acima da propria fonte. A causa e'
# estrutural: a cena 3 tem QUATRO beats onde as outras tem tres, e 15-19 dessas
# palavras sao literais fixos (CTA + gate). ⛔ O motor nao escolhe: cobra piso e
# teto por cena e avisa. A decisao e' do Ed.
#
# ⚠️ PISO_FALA[2] = 24 e' DIVERGENCIA DECLARADA da doutrina (28) — a conta inteira
# esta' na divergencia 1 da docstring. ⛔ Alcada do Ed: trocar e' editar uma linha.
# ⛔⛔ TETO 25 — ordem permanente do operador, 2026-08-05: *"sempre meca. Nao
# pode haver cortes de fala."* O numero vem de render, nao de conta: 32
# cortou, 28 cortou. Os exemplos que ele escreve a mao vivem em 16-25
# palavras (2,0-3,1 palavras/s).
# ⚠️ cena 1 cortava em 1,0%. `_op1` ja' peneira contra o teto.
#
# ⛔⛔ HISTORICO DA CENA 2, E ELE TEM DUAS TENTATIVAS — a segunda pegou.
#
# 2026-08-05: baixei o teto da cena 2 de 32 para 25 e o motor passou a levantar
# `IndexError: Cannot choose from an empty sequence`. Voltou para 32 e ficou
# escrito aqui que era DELIBERADO e para NAO TOCAR. A leitura estava errada: o
# IndexError nao provava que a copy nao cabia — provava que a ESCADA de
# degradacao do `_op2` nao tinha fundo. Os quatro degraus dela exigem todos
# `<= TETO_FALA[2]`, entao com o teto no fisico um mecanismo longo zerava os
# quatro e o `rng.choice([])` derrubava o sorteio. O sintoma era da escada, nao
# do pool.
#
# 2026-08-08: desceu para 25 e FICOU, porque duas coisas mudaram junto:
#   · a escada ganhou fundo garantido (`or [min(REGRAS, ...)]`) — antes de
#     quebrar, cede o teto e deixa o linter reclamar, que e' quem tem de falar;
#   · o MECANISMO passou a ser escolhido dentro do orcamento, em vez de solto.
# ⚠️ MEDIDO depois: 0 ERRO e 0 AVISO em 400 sorteios, maximo 25 palavras, e a
# cena 2 saiu da lista das que cortam fala (era 34,2% dos sorteios acima do
# teto fisico — ou seja, fala CORTADA no render).
# ⚠️ CUSTO ASSUMIDO, tambem medido: 164 -> 112 falas distintas na cena 2, e UM
# dos dez `MECANISMOS_FALA` (o VERBATIM de 18 palavras) nao deixa espaco para
# regra nenhuma e sai do sorteio. Ele so' produzia fala que o take cortava.
# ⛔ Recuperar essas 52 e' encurtar copy — alcada do operador.
#
# ⛔⛔ A CENA 3 FICA EM 34 DE PROPOSITO e continua na lista das que cortam: la' o
# MENOR par possivel ja' da' 32 palavras, entao baixar o teto so' trocaria fala
# cortada por sorteio impossivel. Aquilo e' copy, e copy e' alcada do operador.
#
# ⛔⛔ SEM MODO BELA NESTE MOTOR (2026-08-05). Tres lentes batem de uma
# vez: EX7 (`neck`, a regra do geoduck, paga em recusa), EX9
# (vocabulario banido) e EX10 (a narradora tem de existir numa tabela
# propria). O modo reprovava 65 de 200.
# ⛔⛔ DUAS CENAS, as duas no teto FISICO de 25 palavras (8s a ~3,1 p/s).
# ⚠️ O motor de 24s declarava 34 na cena 3 e por isso vivia na lista dos
# que cortam fala: o MENOR par FUNDIDA+CTA+GATE de la' ja' da' 32 palavras.
# Aqui a cena fundida NAO herda aqueles beats — ela e' reconstruida em
# eixos compostos que cabem no teto por construcao, e o [ALCANCE] do
# autoteste reprova qualquer entrada que nao caiba com os minimos das
# outras. E' a licao §36: entrada que nao alcanca nao e' rara, e' morta.
# ⚠️ PISO da cena 2 em 20: com quatro beats curtos o piso de 30 do motor
# de 24s seria inalcancavel, e alarme que nao pode ser satisfeito nao e'
# alarme — e' ruido, e ruido ensina a ignorar o self-test inteiro.
# ⛔⛔ ORCAMENTO REFEITO EM 2026-08-10 (CONTRATO DE COPY 16s), E ELE AGORA FECHA
# POR CONSTRUCAO — nao por filtro. A licao §36 (`entrada que nao alcanca nao e'
# rara, e' morta`) custou caro duas vezes esta semana, e a defesa mais forte
# contra ela nao e' um solver melhor: e' um pool cujo MAIOR caso ja' cabe.
#
#   cena 1 = ISCAS(10) + DESMENTIDOS(4-7) + FALHAS16(6-7)  -> 20-24
#   cena 2 = MECANISMOS16(6) + DISCLOSURES16(8)
#            + FOLLOWS16(2) + CTAS(8-9)                    -> 24-25
#
# ⚠️ Com isso NENHUMA combinacao e' descartada por orcamento, e o [ALCANCE] do
# autoteste sai 100% em todos os pools de fala — medido, nao afirmado.
# ⛔ TETO 25 continua vindo de RENDER, nao de conta (ordem permanente do
# operador, 2026-08-05: *"sempre meca. Nao pode haver cortes de fala."*). 32
# cortou, 28 cortou. ⛔ Nao subir para 26 "porque falta uma palavra": foi o que
# se pensou em fazer aqui e a saida certa foi ENCURTAR o beat, nao o teto.
TETO_FALA = {1: 25, 2: 25}
# ⚠️ PISOS REBAIXADOS COM A CONTA JUNTO (eram 22 e 20). O piso existe para
# acusar BEAT PERDIDO, e os beats deste motor agora sao garantidos por
# CONSTRUCAO (tres pools obrigatorios na cena 1, quatro na cena 2): o piso passa
# a ser so' a borda de baixo da faixa real. Piso acima do minimo alcancavel e'
# alarme que ninguem pode satisfazer — ruido que ensina a ignorar o self-test.
#   cena 1: minimo real 20 (10+4+6) -> piso 20
#   cena 2: minimo real 24 (6+8+2+8) -> piso 22, com folga de 2
PISO_FALA = {1: 20, 2: 22}

# ⚠️ A borda de CIMA da faixa 82-96 da doutrina. ⛔ Nao usar a soma dos tetos
# (94): a faixa da doutrina permite 96, e o AVISO dispararia abaixo do numero que
# ela mesma autoriza. Na pratica os tetos POR CENA e' que travam — o que e' o
# desenho certo, porque atropelo acontece dentro de um take, nao no video.
# ⚠️ Dois takes de 25 = 50. O total nao trava nada aqui (os tetos POR CENA
# e' que travam, porque atropelo acontece dentro de um take), mas existe
# para o relatorio nao mentir sobre o tamanho do video.
TETO_TOTAL = 50

# ---------------------------------------------------------------------------
# EX10 — ETNIA PELO MODELO DO NECROSE, E VALE PARA OS DOIS PERSONAGENS
# ---------------------------------------------------------------------------
# Congruencia inviolavel: etnia do REF = etnia do avatar da pagina.
# ⛔ Zero adjetivo de etnia dentro dos pools; quem injeta e' a montagem, por
# pagina. Uma entrada serve pagina branca E pagina negra — e' o que faz a
# congruencia custar ZERO duplicacao de pool (no TROCA e no RESSURREICAO isso
# custava dois pools espelhados por indice).
# ⚠️ DIVERGE do TR11/[D2] do TROCA, onde a narradora e' solta na etnia:
# ordem do operador, 2026-08-03, neste angulo o casting inteiro casa com a pagina.
# ⭐ QUEM NARRA — o sexo de quem fala com a lente (2026-08-06).
# Ordem do operador: *"uma marcacao dentro dos agentes python, de todos, pra
# saber se aquele agente gera roteiros com personagem homens e mulheres como
# narrador/apresentador ou se so' gera com um dos dois"*.
# ⛔ MEDIDO, nao lido: 120 sorteios por agente, olhando o BLOCO 0 do prompt.
# Declarar de cabeca aqui seria a mesma FORMA-sem-FUNCAO que ja' custou o
# botao de pele morto em tres motores.
# ⚠️ Com DOIS sexos a UI desenha a trava homem/mulher; com um so', nao desenha
# botao nenhum — botao que nao trava nada e' pior que botao nenhum.
SEXOS = ("mulher",)

ETNIA = {
    # ⭐ As 5 paginas do lote de 2026-08-05. Split 3 brancos / 2 negros —
    # a razao (volume absoluto x prevalencia) esta' escrita no
    # `bridge-pages-deploy.md`.
    "roy": "white American", "dean": "white American",
    "earl": "white American",
    "jason": "Black American", "philippe": "Black American",
    "joe": "white American", "ray": "white American", "matt": "white American",
         "marcus": "Black American", "chuck": "Black American"}

# EX14 — o nucleo deste repo desde 2026-08-03.
NUCLEO = ["Johnson", "pecker", "wiener", "tool", "soldier"]
# ⚠️ `soldier` FICA NA TABELA E NAO CHEGA MAIS AO VIDEO — desde a reforma de
# 2026-08-10 so' o `NUCLEO_DIRETO` alimenta a fala, e o terceiro substantivo
# (o unico lugar por onde `tool`/`soldier` entravam) nao e' mais emitido. E'
# de proposito: em ingles americano `soldier` para o orgao soa a filme de
# guerra, e o contrato manda escrever como gente fala. A tabela continua
# inteira porque ela e' o LEXICO das lentes (CT3/CT4 do `lint_copy16`, cota do
# orgao do `lint_curto`, `_ex2_regra`) — apagar entrada de lexico cega o
# linter contra copy que alguem escreva amanha.
# ⭐ OS DIRETOS — os tres que NOMEIAM o orgao. `tool` e `soldier` sao apelido
# afetivo e suavizam; entram em minoria, nunca nas duas cenas que a fonte nomeia.
# ⚠️ DIVERGENCIA MINIMA E DECLARADA da letra da EX14, que escreve
# `sc.orgaos_sorteaveis(rng, 2)`: aqui e' `rng.sample(NUCLEO_DIRETO, 2)`. O motivo e' a
# ordem do operador de 2026-08-03 que trocou o pool dos nove motores ("use
# palavras alusivas mais diretas ao penis, tal como wiener, peck-er, john-son, do
# que manhood"), e a fonte diz `Johnson` nas DUAS cenas em que nomeia. Sortear os
# dois entre os cinco deixaria `tool`/`soldier` nas duas cenas centrais em 30% dos
# videos. O terceiro substantivo (cena 3, so' quando a fundida traz `{o}`) sai do
# resto — e' onde os afetivos entram.
NUCLEO_DIRETO = ["Johnson", "pecker", "wiener"]

# ---------------------------------------------------------------------------
# EX9 — A LEI DA REF: LINDA E JOVEM, POR DESCRICAO FISICA CONCRETA
# ---------------------------------------------------------------------------
# ⛔ Piso de 28 herdado do `organicwave_short` (`IDADE_MINIMA_MULHER`) com o
# motivo escrito: "ja' pagamos para descobrir que idade em cena com conteudo de
# ED e' zona sensivel". ⛔ Nao baixar sem ordem dele.
# ⚠️ E teto de 34, que e' a outra metade da lei: 28-34, nao "adulta".
IDADE_MINIMA_NARRADORA = 28
IDADE_MAXIMA_NARRADORA = 34

# ⛔ SEM filtro de diferenca de idade, e o registro existe para ninguem
# "consertar" achando que faltou a ES11. Os homens ficam em 40-58 contra
# narradoras de 28-34: gap maximo 30, exatamente o TETO_DIF_IDADE dos outros
# motores, ou seja ja' dentro da guarda. E a geometria NAO e' de intimidade —
# ela despeja, ele segura um molusco, ela nao encosta nele e ele nao tem rosto.
TETO_DIF_IDADE = 30


# ---------------------------------------------------------------------------
# STRINGS TRAVADAS — ⛔ constantes, nunca redigitadas
# ---------------------------------------------------------------------------
# ⚠️ Os `%s` sao SLOTS DO MOTOR, nao texto a reescrever. Comprimir uma travada
# "com as minhas palavras" ja' entregou esqueleto 3D no lugar da placa em corte
# (RUNBOOK-app-offline §Por que portar). Descricao livre encolhe; bloco validado
# se copia caractere por caractere.

# ---------------------------------------------------------------------------
# [EX4] ⭐⭐ A GEOMETRIA DO IMAGE 01 — ordem do operador, frame 0 do §2 do mapa,
# elemento por elemento. ⛔ NUNCA por o rosto dele em quadro.
# ⛔ `groin`/`pubic`/`crotch` ficam fora: a coordenada nao precisa deles — o prop
# esta' NAS MAOS DELE, no eixo do corpo dele, e o enquadramento corta no peito.
# ⚠️ As duas maos, uma acima da outra, sao a mesma alavanca da F12b/TR10: trazem
# o objeto para o eixo do corpo e nao deixam o Veo escolher o lado. E a AGENCIA e'
# dele (maos dele, no corpo dele), que e' o que separa esta composicao das 4
# recusas deterministicas de 2026-07-30.
# Slots, nesta ordem: ela (descricao inteira) · caixa["caixa"] ·
#                     despejo["img"] · homem (descricao inteira)
# ---------------------------------------------------------------------------
# ⛔⛔ A ORDEM DAS ORACOES E' PARTE DA TRAVADA, e ela foi corrigida em 2026-08-03
# por tres defeitos que estavam TODOS no mesmo periodo — e no bloco do HOOK, que e'
# a peca que justifica o decimo agente:
#   (a) `holding it level` contradizia `standing upright with the siphon pointing
#       straight up` no mesmo objeto. Pior: `held level` e' o termo que este repo
#       usa para TIGELA NA HORIZONTAL (ver EX_KEYWORD_NA_MAO_IMAGE). O IMAGE 03/03
#       ja' dizia a coisa certa (`holding it upright`) — a versao limpa estava no
#       bloco do CTA e a ambigua no hook.
#   (b) `the shell` aparecia DUAS VEZES antes de o geoduck ser introduzido —
#       deitico sem referente, o mesmo defeito que a EX11 aponta na tabua de
#       madeira. O Veo resolve deitico solto inventando o objeto.
#   (c) `Between the two of them, standing upright` vinha DEPOIS de "nas maos
#       dele" e competia com ela — podia plantar o molusco de pe' no deck.
# ⛔ O conserto foi so' de ORDEM e de UMA oracao: o geoduck entra ANTES das maos,
# e `holding it level` saiu. Nenhum elemento do frame 0 foi removido.
EX_GEOMETRIA_IMAGE = (
    "Standing frame-left, turned three-quarters towards the middle of the "
    "frame, is %s. In her left hand, raised to the height of her own chest and "
    "tipped mouth-down at about forty-five degrees, she holds %s, and a "
    "diagonal stream of white powder falls from its open mouth. %s Between the "
    "two of them, standing upright with the siphon pointing straight up and "
    "the shell below it, is a whole geoduck clam, and white powder has already "
    "settled over the top third of the siphon. Standing frame-right, cropped "
    "at the chest so that no face is in the frame, is %s; both of his hands "
    "are closed around the shell, one above the other."
)

# ---------------------------------------------------------------------------
# [EX4] A VARANDA TRAVADA — os quatro elementos do frame 0 que nao variam.
# ⛔ Fora do eixo VARANDAS de proposito: eixo que carrega elemento travado acaba
# perdendo o elemento em metade do lote. Sem slot.
# ---------------------------------------------------------------------------
EX_VARANDA_TRAVADA = (
    "White rocking chairs stand on the boards behind them, the porch rail is "
    "painted white, a United States flag hangs from the post at frame-right, "
    "and the deck under them is bare wood."
)

# ---------------------------------------------------------------------------
# [EX7] ⛔ A BLINDAGEM DE FORMA DO GEODUCK.
# ⚠️ ISTO NAO E' MODERACAO: e' o modo de falha documentado do geoduck, que vira
# PATO no TAKE — pago em render, registrado no `licoes-producao-veo` e na V1 do
# VAZAMENTO. Negacao de FORMA nao e' declaracao de IMOBILIDADE, e e' so' a
# segunda que saiu por ordem do operador. Sem slot.
# ⛔ ARMADILHA REGISTRADA: NAO banir os tokens `duck`/`goose`/`bird` em tabela de
# substring — esta travada os contem literalmente, e um `\bduck\b` reprovaria
# 100% dos lotes (licoes-de-construcao §2: linter que reprova tudo nunca foi
# testado).
# ---------------------------------------------------------------------------
EX_BLINDAGEM_FORMA = (
    "No bird, no goose, no duck, no swan, no snake, no worm, no tentacle, no "
    "feathers, no beak, no eyes, no head, nothing alive, nothing with a face."
)

# ---------------------------------------------------------------------------
# [EX5] ⭐ O HOMEM SEM ROSTO NO TAKE — a decisao de projeto sustentada no
# MOVIMENTO. Sem isto o Veo panoramiza para cima e o rosto entra em quadro no
# segundo 3, que e' exatamente o rosto que nao queremos ter de manter identico
# entre blocos. Sem slot.
# ---------------------------------------------------------------------------
EX_SEM_ROSTO_TAKE = (
    "He stays cropped at the chest for the whole shot: the camera never tilts "
    "up to his face and he never leans down into frame. Only his chest, his "
    "arms and his hands are in the picture, and both of his hands stay closed "
    "around the shell where they are. Only she speaks."
)

# ---------------------------------------------------------------------------
# [EX6] ⛔ A MARCA LEGIVEL — decisao do operador, 2026-08-03, CONTRA a P12.
# ⭐ O que a marca compra: o rotulo laranja faz "bicarbonato" ser lido em 0,2s
# sem uma palavra. E' carga funcional, nao enfeite.
# ⚠️ O risco declarado a ele e registrado: nao e' so' politica de plataforma, e'
# ASSOCIACAO INDEVIDA — embalagem de terceiro num video de alegacao de saude
# sexual sugere endosso da marca. Ele leu e decidiu manter.
# ⚠️ Escrita na AFIRMATIVA: `readable` guia, `not blurred` so' plantaria a
# palavra (a mesma mecanica da FRASE_SEM_MARCA dos outros motores, invertida de
# proposito). ⛔ A P12 continua valendo integralmente nos outros nove agentes:
# isto e' excecao nominal e datada.
# ⛔⛔ O SLOT E' `caixa["recipiente"]`, E ELE NASCEU DE UMA MEDICAO: a travada dizia
# `the box` fixo, e 7 das 12 CAIXAS NAO sao caixa (`carton`, `pouch`, `shaker`,
# `bag`, `package`, `tin`). Resultado medido: 235 de 400 videos (58,8%) mandavam
# desenhar "a caixa" com uma lata ou um saco em quadro — contradicao dentro do
# proprio bloco, que o Veo resolve inventando. ⚠️ O motor JA' tinha resolvido isso
# para o jorro (`the mouth of the %s` no TAKE 01) e o mesmo raciocinio nao tinha
# sido aplicado nem aqui nem nos DESPEJOS. Uma regra, um lugar.
# ---------------------------------------------------------------------------
EX_MARCA_LEGIVEL = (
    "The lettering on the %s is sharp and readable for the whole shot."
)

# ⛔ O MIOLO INVARIANTE da travada acima — e' com ele que o linter compara, nunca
# com o template cru, que agora tem slot (licoes-de-construcao §2: comparar com a
# constante que tem slot da' 100% de falso positivo).
M_MARCA = "is sharp and readable for the whole shot"

# ⛔ A frase que NAO pode aparecer em bloco nenhum deste agente — ela e' a P12 dos
# outros nove e contradiz a EX6 frontalmente. Fica aqui NOMEADA para o linter
# poder cobrar a ausencia dela; ⛔ nunca e' emitida.
FRASE_SEM_MARCA_PROIBIDA = "Every container in the frame is plain and unlabelled."

# ---------------------------------------------------------------------------
# [EX7] ⛔ AS QUATRO DECLARACOES DE ESTADO DE MOVIMENTO QUE ESTAO PROIBIDAS AQUI.
# Os outros nove motores DECLARAM o prop imovel (`RS_IMOVEL_TAKE`,
# `completely motionless for the entire shot`); neste agente isso saiu por ordem
# do operador. ⛔ Sem este linter, a primeira pessoa que "consertar" o motor
# copiando a travada de imobilidade do RESSURREICAO quebra a ordem em silencio.
# ---------------------------------------------------------------------------
EX_MOVIMENTO_PROIBIDO = ("motionless", "does not move", "doesn't move",
                         "stays exactly as it appears", "completely still")

# ---------------------------------------------------------------------------
# [EX11/TR1/ES9] O MECANISMO PLANTADO DESDE O FRAME 1 e O OBJETO DA KEYWORD NA
# MAO. ⚠️ As duas travadas sao COPIA LITERAL do `ressurreicao_short.py`
# (`RS_PLANTADO_IMAGE` e `RS_KEYWORD_NA_MAO_IMAGE`) — string validada e'
# constante, nunca redigitada.
# ⭐ Por que ES9: o objeto da keyword esta' NA MAO LIVRE dela no frame em que a
# boca diz `gelatin,`, e esta' PLANTADO na mesa desde o frame 1 da cena 2 —
# objeto que entra de fora do quadro nao e' premio, e' corte disfarcado.
# ⚠️ `held level`, NUNCA `held flat to the lens`: `flat to the lens` nasceu para o
# donut e manda INCLINAR uma tigela rasa de cubos.
# ⚠️ A mao livre e' a ESQUERDA porque e' a mao que segurava a caixa na cena 1 e
# esta' vazia na cena 3.
# Slots EX_PLANTADO: mecanismo["plantado"] SEM artigo · mesa · mecanismo["pousado"]
# Slot EX_KEYWORD_IMAGE: mecanismo["curto"]
# ---------------------------------------------------------------------------
EX_PLANTADO_IMAGE = "The %s has been standing on the %s since the first frame, %s."

EX_KEYWORD_NA_MAO_IMAGE = (
    "In her own free left hand, raised to the height of her chest and held "
    "level, she holds %s."
)

# ⛔ O par do RESSURREICAO termina em `and does not move for the entire shot`, e
# esse literal esta' PROIBIDO aqui (EX7). Reescrito para dizer a MESMA coisa pela
# posicao, que e' o que o Veo obedece, sem declarar estado de movimento.
# ⚠️ Divergencia de UMA oracao, declarada: o resto e' o mesmo contrato.
EX_KEYWORD_NA_MAO_TAKE = (
    "What she holds in her own free left hand stays at that same height in "
    "front of her for the entire shot."
)

# ---------------------------------------------------------------------------
# [EX17] A CAUDA — identica a' dos nove motores. ⛔ Nao reescrever.
# ⚠️ A fonte tem texto queimado palavra a palavra (`YOUR`, `FIRM?`) e esse e' o
# unico elemento visual dela que nao se copia: a NOSSA legenda nasce depois, no
# Veo Editor, a partir do Whisper, e texto vindo do gerador entra por cima e nao
# sai. Isto e' PIPELINE, e a EX1 nao o revoga.
# ---------------------------------------------------------------------------
CAUDA = "Shot on iPhone, natural grain. No on-screen text, no watermark."


# ---------------------------------------------------------------------------
# ELENCO — EX9, EX10, EX15
# ---------------------------------------------------------------------------
# ⭐⭐ A LICAO QUE ESTE MOTOR NASCE CUMPRINDO (licoes-de-construcao §15). O
# operador mediu os 21 pools de personagem do repo e TODOS tinham eixo descritivo
# zerado. Dez pessoas descritas so' por cabelo sao a MESMA pessoa dez vezes, e o
# gerador devolve o mesmo rosto. Queixa literal: "seu repertorio de personagens
# esta fraquissimo".
# ⛔ Portanto CADA entrada difere das outras em pelo menos TRES eixos, e os eixos
# sao CAMPOS SEPARADOS — cabelo · oculos · porte · rosto (a ancora P6,
# permanente) · idade · roupa. A diversidade e' AUDITAVEL por enumeracao
# (`medir_personagens.py --gate`), nunca aferida a olho.
#
# ⛔⛔ ZERO ETNIA (EX10), E ISSO INCLUI O QUE ENTRA POR DENTRO DO CABELO E DA PELE.
# `a full soft afro`, `waist-length box braids` e `a long twist-out` CARREGAM
# etnia; `pale forearms` e cor de olho clara tambem. Num pool unico eles
# quebrariam a injecao em duas das cinco paginas. Os descritores aqui sao de
# CORTE, COMPRIMENTO e ESTILO (`worn loose past the shoulders`, `in a high sleek
# ponytail`, `cut sharp at the jaw`) — a textura sai da injecao. ⛔ Nao e'
# detalhe: e' o que faz o modelo de etnia funcionar.
# ⚠️ Custo declarado (divergencia 4 da docstring): cor de cabelo e cor de olho
# deixam de ser eixos de distincao. A diferenca vem de corte, comprimento, porte,
# oculos de sol e ancora facial.
#
# ⚠️ OCULOS DE SOL, NUNCA DE LEITURA: a lei da REF (linda e jovem) briga de
# frente com oculos de leitura — foi o erro registrado na EXCECAO do
# `ressurreicao_short` (otimizar para o medidor entregou narradoras de 47 e 52
# anos, grisalhas e de oculos de leitura, num agente de nutra sexual). Oculos de
# sol na cabeca sao figurino de varanda e nao brigam com nada.
# ⛔ Zero `sexy`/`curvy`/`beautiful` (BANIDOS_DESEJO): a atratividade entra por
# DESCRICAO FISICA CONCRETA. ⛔ Zero `baby tee`: o token `baby` entra de graca.
# ⛔ E o REF nao e' copia da Angela Brooks — do reel-fonte extrai-se o
# DISPOSITIVO, nunca a APARENCIA (ED12). Por isso ⛔ nada de blazer de autoridade:
# o operador trocou o registro de proposito.
NARRADORAS = [
    {"id": "solto_longo", "idade": 30,
     "cabelo": "long hair worn loose and falling well past her shoulders",
     "oculos": "",
     "porte": "a gym-fit hourglass figure, a full bust, a flat toned stomach, firm round glutes and long lean legs",
     "rosto": "a light spray of freckles across her nose and a small dark mole "
              "at her jawline",
     "roupa": "a fitted white tank top and denim cut-offs"},
    {"id": "rabo_alto", "idade": 29,
     "cabelo": "hair pulled back into a high sleek ponytail",
     "oculos": "",
     "porte": "a tall athletic build, a full high bust, a tight defined midsection, firm glutes and long toned legs",
     "rosto": "large dark eyes and a shallow dimple in her left cheek",
     "roupa": "a pale-blue button-front shirt tied at the waist"},
    {"id": "tranca_unica", "idade": 28,
     "cabelo": "very long hair gathered over one shoulder in a single thick "
               "braid",
     "oculos": "",
     "porte": "a sculpted gym body, a full bust, visible abs, a small waist and firm rounded glutes",
     "rosto": "a full mouth, a beauty mark at the corner of her right eye and "
              "gold hoop earrings",
     "roupa": "a rust ribbed tank top"},
    {"id": "bob_platina", "idade": 31,
     "cabelo": "a bleached-platinum bob cut sharp at the jaw",
     "oculos": "",
     "porte": "a compact fitness figure, a full bust, a hard flat stomach, a narrow waist and firm glutes",
     "rosto": "a faint scar through her right eyebrow and a straight nose",
     "roupa": "a black cropped tee and high-waisted white shorts"},
    {"id": "volume_solto", "idade": 29,
     "cabelo": "thick hair worn big and loose, standing out wide around her "
               "face",
     "oculos": "",
     "porte": "an athletic figure with a deep waist-to-hip line, a generous bust, a toned flat stomach, firm glutes and strong smooth legs",
     "rosto": "high cheekbones and a small mole on her right cheekbone",
     "roupa": "a mustard knit tank top and a thin gold chain"},
    {"id": "coque_bagunca", "idade": 32,
     "cabelo": "hair twisted up into a loose messy bun",
     "oculos": "mirrored aviator sunglasses pushed up into her hair",
     "porte": "a lean gym-built figure, a full bust, sharply defined abs, a tiny waist and firm high glutes",
     "rosto": "wide-set eyes, a light spray of freckles and a shallow dimple "
              "in her chin",
     "roupa": "a pale-blue tank top and white shorts"},
    {"id": "cachos_medios", "idade": 30,
     "cabelo": "shoulder-length hair worn in loose curls",
     "oculos": "",
     "porte": "a full-figured fitness body, a full bust, a toned stomach, wide firm hips and round glutes",
     "rosto": "a full mouth and a small crescent birthmark at her right temple",
     "roupa": "a rust-orange top with the sleeves pushed up"},
    # ⚠️ `crop of hair` e `a small silver hoop in each ear` NAO sao enfeite: a
    # versao anterior dizia `a short tousled crop` e `small silver hoops`, e
    # ZERAVA os eixos `cabelo` e `ancora` desta entrada no
    # `medir_personagens.py` — `crop` nao esta' no regex de cabelo e `\bhoop\b`
    # nao casa o plural `hoops`. Descricao que o medidor nao ve' e' descricao
    # que ninguem audita.
    {"id": "crop_curto", "idade": 29,
     "cabelo": "a short tousled crop of hair swept hard to one side",
     "oculos": "round sunglasses pushed up on her forehead",
     "porte": "a trained slender figure, a full bust, a flat sculpted stomach, a narrow waist and firm glutes",
     "rosto": "freckles scattered over her collarbones and a small silver hoop "
              "in each ear",
     "roupa": "a black cropped tank top and light denim shorts"},
    {"id": "volume_alto", "idade": 34,
     "cabelo": "hair worn big and swept up off her face",
     "oculos": "",
     "porte": "a tall strong fitness build, a full bust, a toned midsection, firm glutes and powerful smooth legs",
     "rosto": "a wide bright smile and a small mole above her left brow",
     "roupa": "an emerald cropped knit top and thin gold hoops"},
    {"id": "franja_cortina", "idade": 28,
     "cabelo": "long hair with a soft curtain fringe framing her face",
     "oculos": "narrow black sunglasses pushed up on her head",
     "porte": "a strongly shaped athletic figure, a full round bust, a flat toned belly, a small waist and firm glutes",
     "rosto": "a heart-shaped face and a dark mole under her left eye",
     "roupa": "a cream ribbed top and pale denim shorts"},
    {"id": "liso_glossy", "idade": 33,
     "cabelo": "long jet-black hair worn straight and glossy",
     "oculos": "",
     "porte": "a long-limbed gym figure, a full bust, visible abs, a cinched waist and firm lifted glutes",
     "rosto": "sharp cheekbones and a small gold stud in her left nostril",
     "roupa": "a burgundy wrap top and dark jeans"},
    {"id": "meio_preso", "idade": 31,
     "cabelo": "hair pinned back on one side and left down on the other",
     "oculos": "tortoiseshell sunglasses hooked into the front of her top",
     "porte": "a petite hard-trained figure, a full bust, a flat stomach and firm round glutes",
     "rosto": "a tiny freckle on her left eyelid and a faint pale scar on her "
              "left cheekbone",
     "roupa": "a white cropped tee and high-waisted jeans"},
    {"id": "ondas_soltas", "idade": 29,
     "cabelo": "long hair worn in loose waves pushed back off her face",
     "oculos": "folding sunglasses hooked at her collar",
     "porte": "a tall toned figure, a full bust, a lean defined waist, firm glutes and long tanned legs",
     "rosto": "skin tanned from the sun and a small dark beauty mark just "
              "above her lip",
     "roupa": "a white ribbed tank top and khaki shorts"},
    {"id": "coque_baixo", "idade": 32,
     "cabelo": "hair pulled into a low twisted knot at the nape",
     "oculos": "",
     "porte": "a full hourglass gym figure, a generous bust, a flat trained stomach, wide hips and firm glutes",
     "rosto": "smooth-skinned, with a deep dimple that only shows on the left",
     "roupa": "a sage-green scoop top and dark jeans"},
]

# ⭐ EX5 — O HOMEM DA CENA 1 E DA CENA 3, CORTADO NO PEITO, SEM ROSTO EM QUADRO.
# ⛔ Zero cabelo, zero pelo facial, zero oculos: ele nao tem cabeca em quadro, e
# encher esses eixos e' desenhar exatamente o que a decisao de projeto tirou do
# enquadramento. Os tres eixos que sobram estao cheios de proposito e sao os
# UNICOS que o espectador ve': PORTE, PELE (antebracos e maos) e ANCORA (cicatriz,
# pinta, mancha de nascenca no braco ou na mao).
# ⚠️ Os tres zeros estao DECLARADOS no `medir_personagens.py` (EXCECOES), pelo
# precedente FLAGRANTE/NECROSE, com o motivo escrito. ⛔ A alternativa preguicosa
# era batizar o pool de `TORSOS`, que o regex `NOMES_DE_POOL` nao casa e some do
# relatorio — isso e' otimizar contra a metrica em vez de contra o objetivo
# (licoes-de-construcao §15/§16), e nao foi feito.
# ⛔ Zero etnia aqui tambem (EX10): a pele entra por TEXTURA (curtida, marcada de
# sol, gretada), nunca por TOM.
HOMENS_SEM_ROSTO = [
    {"id": "camiseta_marinho", "idade": 48,
     "porte": "heavy through the chest and thick-armed",
     "roupa": "a plain navy cotton t-shirt",
     "pele": "heavy forearms tanned to a hard line at the elbow",
     "marca": "a pale old scar across the back of his right hand"},
    {"id": "flanela_xadrez", "idade": 44,
     "porte": "lean and long-armed",
     "roupa": "a red-and-black plaid flannel shirt with the sleeves rolled to "
              "the elbow",
     "pele": "forearms lined and sun-weathered",
     "marca": "a raised mole on his left wrist"},
    {"id": "polo_cinza", "idade": 56,
     "porte": "heavy-set and round through the middle",
     "roupa": "a heather-grey polo shirt",
     "pele": "sun-spotted skin along the top of his forearms",
     "marca": "a thin white scar along his right thumb"},
    {"id": "regata_branca", "idade": 52,
     "porte": "wiry and narrow-shouldered",
     "roupa": "a white ribbed sleeveless undershirt",
     "pele": "leathery weathered forearms",
     "marca": "a coin-sized dark birthmark above his left wrist"},
    {"id": "camisa_trabalho", "idade": 50,
     "porte": "solid and square through the shoulders",
     "roupa": "a light-blue short-sleeve work shirt with a chest pocket",
     "pele": "forearms tanned to a hard line where the sleeve ends",
     "marca": "a long healed scar across his right forearm"},
    {"id": "moletom_cortado", "idade": 46,
     "porte": "tall and rangy",
     "roupa": "a grey sweatshirt with the sleeves cut off at the shoulder",
     "pele": "deeply lined skin on the backs of his hands",
     "marca": "a dark mole below his right elbow"},
    {"id": "camisa_jeans", "idade": 54,
     "porte": "compact and solid",
     "roupa": "a faded denim shirt buttoned to the second button",
     "pele": "forearms creased and sun-spotted",
     "marca": "a birthmark low on his right forearm"},
    {"id": "henley_carvao", "idade": 42,
     "porte": "broad-shouldered and heavy through the chest",
     "roupa": "a charcoal henley with the sleeves pushed up",
     "pele": "thick creased skin over the knuckles",
     "marca": "two moles close together on his left forearm"},
    {"id": "camiseta_bolso", "idade": 58,
     "porte": "thin and slight",
     "roupa": "a cream pocket tee",
     "pele": "forearms lightly lined and dry",
     "marca": "a faint scar ringing his right wrist"},
    {"id": "camisa_pesca", "idade": 55,
     "porte": "big-framed and stout",
     "roupa": "a forest-green fishing shirt with two chest pockets",
     "pele": "heavily tanned forearms",
     "marca": "a dark mole at the base of his left thumb"},
    {"id": "camiseta_lisa", "idade": 40,
     "porte": "trim and flat through the middle",
     "roupa": "a plain black t-shirt",
     "pele": "smooth-skinned forearms with a sharp tan line",
     "marca": "a small scar on the back of his left hand"},
    {"id": "camisa_listrada", "idade": 51,
     "porte": "stocky and short-armed",
     "roupa": "a blue-and-white striped short-sleeve shirt",
     "pele": "weathered, deeply creased skin",
     "marca": "a liver-spotted patch and a mole at his right wrist bone"},
    # + 2026-08-04: ampliacao por ordem do operador — *"aumente o pool de
    # personagens... faca isso para pelo menos outros 5 agentes shorts"*.
    # ⛔ Cada entrada difere das outras em >= 3 eixos fisicos (licoes §15):
    # contar entradas nao basta, o que conta e' quantos eixos elas acionam.
    {"id": "polo_vinho", "idade": 55,
     "porte": "broad and barrel-chested, thick through the middle",
     "roupa": "a deep wine-red polo shirt",
     "pele": "forearms heavily freckled and hard at the elbow",
     "marca": "a wide steel watch loose on his left wrist"},
    {"id": "regata_cinza", "idade": 44,
     "porte": "lean and wiry, with corded forearms",
     "roupa": "a heather-grey sleeveless vest",
     "pele": "a scatter of dark moles across the shoulder",
     "marca": "a faded green tattoo band around his left forearm"},
    {"id": "flanela_verde", "idade": 51,
     "porte": "heavy-boned with a long back and wide hands",
     "roupa": "a forest-green flannel shirt with the sleeves cut off",
     "pele": "weathered skin cracked across the knuckles",
     "marca": "a thick silver ring on his left index finger"},
    {"id": "henley_areia", "idade": 47,
     "porte": "compact and solid, shoulders square",
     "roupa": "a sand-coloured henley with the sleeves pushed up",
     "pele": "forearms with a raised keloid line above the wrist",
     "marca": "a woven leather cord knotted at his left wrist"},
    {"id": "camisa_xadrez_azul", "idade": 58,
     "porte": "tall and rangy, narrow through the hips",
     "roupa": "a blue-and-white checked work shirt",
     "pele": "thin skin drawn tight over the tendons of the forearm",
     "marca": "a white band of untanned skin where a ring used to be"},
    {"id": "camiseta_preta", "idade": 42,
     "porte": "thick-armed and heavy-shouldered",
     "roupa": "a plain black cotton t-shirt",
     "pele": "forearms dark and thickly covered to the wrist",
     "marca": "a thumbnail ridged and darkened from an old injury"},
]


# ---------------------------------------------------------------------------
# CENARIO — EX11: A VARANDA E' A MESMA NAS TRES CENAS
# ---------------------------------------------------------------------------
# ⚠️ Os quatro elementos travados da geometria (cadeiras de balanco brancas,
# guarda-corpo branco, bandeira dos EUA, deck de madeira) NAO moram aqui: moram
# na EX_VARANDA_TRAVADA. Este eixo varia a CLASSE e a arquitetura em volta.
# ⛔ E nao existe eixo de "ambiente B": a fonte corta para uma sunroom em 5,30s e
# esse e' um dos dois unicos elementos visuais dela que nao copiamos (divergencia
# 3 da docstring). Talking-head solo e' pobreza de bit visual, e cenario unico
# da' continuidade de graca entre tres blocos gerados separadamente.
VARANDAS = [
    {"id": "fazenda_meio_oeste",
     "set": "a deep wraparound porch on an old Midwest farmhouse, white "
            "clapboard wall behind, flat corn fields to the horizon",
     "re_ancora": "the same wraparound farmhouse porch",
     "curto": "the porch",
     "luz": "flat even morning light"},
    {"id": "rancho_suburbano",
     "set": "the narrow front porch of a suburban ranch house, vinyl siding, a "
            "mown lawn and a driveway behind",
     "re_ancora": "the same narrow front porch of the ranch house",
     "curto": "the porch",
     "luz": "bright overcast daylight"},
    {"id": "cabana_montanha",
     "set": "the front deck of a log cabin, pines crowding close behind the rail",
     "re_ancora": "the same log cabin deck",
     "curto": "the cabin deck",
     "luz": "green-tinged light filtered through the pines"},
    {"id": "casa_praia",
     "set": "the raised porch of a grey-shingled coastal cottage, dune grass "
            "and a strip of ocean behind",
     "re_ancora": "the same raised porch of the coastal cottage",
     "curto": "the porch",
     "luz": "hard bright sea light from frame-left"},
    {"id": "colonial_colunas",
     "set": "the columned front porch of a white colonial house, brick steps "
            "down to a clipped hedge",
     "re_ancora": "the same columned colonial porch",
     "curto": "the porch",
     "luz": "warm late-afternoon light raking from frame-right"},
    {"id": "bangalo_craftsman",
     "set": "the low porch of a Craftsman bungalow, tapered posts on stone "
            "piers and a maple in the yard",
     "re_ancora": "the same low bungalow porch",
     "curto": "the porch",
     "luz": "dappled shade moving on the boards"},
    {"id": "casa_movel",
     "set": "the built-on porch of a mobile home under a metal awning, a "
            "gravel lot behind",
     "re_ancora": "the same built-on porch under the awning",
     "curto": "the porch",
     "luz": "flat shaded daylight under the awning"},
    {"id": "lago_deck",
     "set": "the lakeside deck of a summer house, the water flat and bright "
            "behind the rail",
     "re_ancora": "the same lakeside deck",
     "curto": "the deck",
     "luz": "bright light bouncing up off the water"},
    {"id": "vitoriana",
     "set": "the gingerbread-trimmed porch of a Victorian house, scrolled "
            "brackets and a painted floor",
     "re_ancora": "the same gingerbread-trimmed Victorian porch",
     "curto": "the porch",
     "luz": "soft high-cloud daylight"},
    {"id": "deserto_adobe",
     "set": "the shaded porch of an adobe house in the desert, red rock and "
            "dry brush behind",
     "re_ancora": "the same shaded adobe porch",
     "curto": "the porch",
     "luz": "hard sun outside and deep open shade on the porch"},
    {"id": "varanda_telada",
     "set": "a screened porch on a Florida house, palm shadows falling across "
            "the screens",
     "re_ancora": "the same screened Florida porch",
     "curto": "the screened porch",
     "luz": "bright shaded daylight coming through the screens"},
    {"id": "fazenda_sul",
     "set": "the long front porch of a Southern farmhouse, a porch swing at "
            "the far end and a pasture fence behind",
     "re_ancora": "the same long Southern farmhouse porch",
     "curto": "the porch",
     "luz": "warm low light late in the day"},
    {"id": "celeiro_convertido",
     "set": "the deck of a converted barn, a red board-and-batten wall behind",
     "re_ancora": "the same converted barn deck",
     "curto": "the deck",
     "luz": "flat grey daylight"},
    {"id": "apalaches",
     "set": "a plank porch on an Appalachian hillside house, ridgelines "
            "stacked in the haze behind",
     "re_ancora": "the same plank hillside porch",
     "curto": "the porch",
     "luz": "cool hazy light with the ridges soft behind"},
]

# ⭐ A MESA DA VARANDA — a superficie onde a gelatina fica PLANTADA desde o frame
# 1 da cena 2 (ES9) e onde o geoduck e a caixa ficam pousados na cena 2.
# ⚠️ Este eixo existe porque a sunroom da fonte NAO entra (divergencia 3): a
# entropia que ela carregava mudou de endereco, nao sumiu.
MESAS = [
    {"id": "vime_redonda", "mesa": "a round wicker table on the boards",
     "curto": "the wicker table"},
    {"id": "madeira_pintada", "mesa": "a small painted wooden table",
     "curto": "the painted table"},
    {"id": "banquinho_pinho", "mesa": "a low pine stool used as a side table",
     "curto": "the pine stool"},
    {"id": "carrinho_esmalte",
     "mesa": "an enamel-topped serving cart pushed against the rail",
     "curto": "the serving cart"},
    {"id": "tabua_cavalete",
     "mesa": "a plank laid across two trestles as a work table",
     "curto": "the plank table"},
    {"id": "ferro_jardim", "mesa": "a small wrought-iron garden table",
     "curto": "the iron table"},
    {"id": "engradado", "mesa": "a wooden crate stood on end as a table",
     "curto": "the crate"},
    {"id": "dobravel_metal",
     "mesa": "a folding metal card table opened out on the boards",
     "curto": "the card table"},
    {"id": "carretel_cabo", "mesa": "an old cable spool used as a low table",
     "curto": "the spool table"},
    {"id": "bancada_rail",
     "mesa": "a narrow shelf board fixed along the inside of the rail",
     "curto": "the shelf board"},
    {"id": "cadeira_lateral",
     "mesa": "a square side table between two of the rocking chairs",
     "curto": "the side table"},
    {"id": "tronco_cortado", "mesa": "a cut log section standing on end",
     "curto": "the log table"},
]

# ⛔ EX6 — TODAS de bicarbonato de sodio, porque a fala esta' travada em `baking
# soda` e imagem que contradiz a boca queima o take. ⛔ Zero embalagem lisa ou
# generica: a marca real e legivel e' ordem do operador. ARM & HAMMER e' a da
# fonte; as outras sao SKUs e marcas reais de bicarbonato do varejo US.
# ⛔⛔ SO' CAIXA DE PAPELAO — ORDEM DO OPERADOR, 2026-08-03, DEPOIS DE VER O
# RENDER. Ele recebeu um video com um POTE CILINDRICO na mao da narradora e
# escreveu: *"nao havia te pedido para mudar a marca da caixa de baking soda pra
# esse formato cilindrico: seja rigoroso e fiel a' forma de apresentacao da
# marca: aquela embalagem box classica"*.
#
# O pool tinha SEIS entradas que NAO sao caixa, e que estavam la' por minha
# conta, nao por pedido dele — `ah_shaker` (frasco cilindrico de tampa
# flip-top), `clabber` (lata cilindrica), `ah_pouch`, `ah_saco_grande` e
# `milliard` (sacos) e `bobs` (pacote plastico). Metade do pool podia sair
# cilindrica ou mole, e a caixa laranja e' justamente o que faz "bicarbonato"
# ser lido em 0,2s sem uma palavra. As seis sairam.
# `ah_familia` era `carton` e virou `box`: e' a mesma embalagem, e a palavra
# `carton` convida o gerador a variar a forma.
# ⚠️ E A FORMA NAO FICA SO' NA PALAVRA `box` — `box` sozinho ja' devolveu
# cilindro. A geometria vai ESCRITA, em EX_CAIXA_FORMA.
CAIXAS = [
    {"id": "ah_classica", "recipiente": "box",
     "caixa": "the classic one-pound orange Arm & Hammer baking soda box, the "
              "brand name large and sharp across the front"},
    {"id": "ah_familia", "recipiente": "box",
     "caixa": "a large family-size Arm & Hammer baking soda box, the orange "
              "front panel square to the lens"},
    {"id": "ah_rasgada", "recipiente": "box",
     "caixa": "an Arm & Hammer baking soda box with the top corner torn open "
              "along the perforation"},
    {"id": "great_value", "recipiente": "box",
     "caixa": "a Great Value baking soda box from Walmart"},
    {"id": "kroger", "recipiente": "box",
     "caixa": "a Kroger-brand baking soda box"},
    {"id": "whole_foods", "recipiente": "box",
     "caixa": "a 365 by Whole Foods Market baking soda box"},
    # ⚠️ O corte para 6 furava o piso do proprio motor (`MIN_OPCOES = 9` por
    # eixo visual, cobrado no autoteste). ⛔ Baixar o piso seria resolver a
    # ordem dele afrouxando a regra que segura TODOS os eixos — as quatro
    # abaixo repoem a entropia DENTRO da caixa classica, variando TAMANHO e
    # ESTADO da embalagem, que e' o que a fonte mostra. Nenhuma forma nova.
    {"id": "ah_bico", "recipiente": "box",
     "caixa": "an Arm & Hammer baking soda box with the pour spout tab folded "
              "open at the top corner"},
    {"id": "ah_pequena", "recipiente": "box",
     "caixa": "a small eight-ounce Arm & Hammer baking soda box, the orange "
              "front panel facing the lens"},
    {"id": "ah_amassada", "recipiente": "box",
     "caixa": "a well-used Arm & Hammer baking soda box, one bottom corner "
              "dented from the cupboard, the orange front still square to the "
              "lens"},
    {"id": "signature", "recipiente": "box",
     "caixa": "a Signature Select baking soda box"},
]

# ⛔⛔ A BLINDAGEM DE FORMA DA CAIXA — irma da EX_BLINDAGEM_FORMA do geoduck.
# ⚠️ Por que a NEGACAO entra aqui, se o repo prega que silencio vence negacao: a
# regra de nao-negar e' de DECLARACAO DE CONFORMIDADE (nunca escrever "not a
# celebrity", "fully clothed") — la' negar planta a palavra no classificador de
# moderacao. Isto e' outra coisa: e' desambiguacao de FORMA, e o precedente e' a
# blindagem do geoduck DESTE MESMO agente, que so' parou de virar pato quando a
# lista de negacao entrou. Prop que o gerador troca de forma se descreve pelos
# dois lados.
EX_CAIXA_FORMA = (
    "The baking soda package is a rectangular cardboard box with flat faces "
    "and square corners, taller than it is wide and shallow from front to "
    "back, with a flat top and a perforated pour spout at one top corner. It "
    "is not a cylinder, not a canister, not a tub, not a tin, not a jar, not a "
    "bottle, not a pouch, not a bag and not a shaker."
)

# ⛔ O miolo invariante, para o linter cobrar sem depender da frase inteira
# (licoes §2 — comparar com o template cru e' falso positivo garantido no dia em
# que a string ganhar slot).
M_CAIXA_FORMA = "rectangular cardboard box with flat faces"

# ⛔ A geometria travada NAO se abre: a caixa esta' sempre na MAO ESQUERDA, a'
# altura do peito, de boca para baixo, inclinada ~45°, jorro em diagonal (EX4).
# O que varia e' a MAO LIVRE (direita), o olhar e a micro-acao da mao que despeja.
# ⛔ Zero `does not move` nas entradas: e' literal proibido neste agente (EX7), e
# a mesma ordem se diz pela POSICAO (`stays where it is`), que e' o que o Veo
# obedece de fato.
# ⛔⛔ O `%s` DE CADA ENTRADA E' `caixa["recipiente"]`, PELO MESMO MOTIVO DA
# EX_MARCA_LEGIVEL: `the box` fixo contradizia a imagem em 7 das 12 CAIXAS. ⚠️ Uma
# entrada que NAO nomeia o recipiente nao leva `%s` — nao se poe slot por simetria.
DESPEJOS = [
    {"id": "mao_no_corrimao",
     "img": "Her free right hand rests flat on the white rail beside her.",
     "take": "Her free right hand stays flat on the rail and the %s stays at "
             "the same height."},
    {"id": "batendo_lateral",
     "img": "Her free right hand is against the side of the %s, mid-tap.",
     "take": "Her free right hand keeps tapping the same spot and the %s "
             "stays at the same height."},
    {"id": "dedo_apontando",
     "img": "Her free right hand points down at the falling powder without "
            "touching anything.",
     "take": "Her pointing hand stays where it is and the %s stays at the "
             "same height."},
    {"id": "mao_no_quadril",
     "img": "Her free right hand is planted on her own hip.",
     "take": "Her free hand stays on her hip and the %s stays at the same "
             "height."},
    # ⚠️ ERA `the torn-off lid flap of the box`, e a aba de tampa NAO EXISTE em
    # `pouch`, `bag`, `tin` nem `shaker` — 4 dos 12 recipientes tornavam o gesto
    # impossivel. `strip of packaging` diz o mesmo gesto (papel rasgado na mao
    # livre, na horizontal) sem prometer uma peca que a embalagem sorteada pode
    # nao ter. ⛔ Por isso esta entrada nao leva slot: o objeto ficou generico de
    # proposito.
    {"id": "aba_na_mao",
     "img": "Her free right hand holds a torn-off strip of packaging, held "
            "level.",
     "take": "What she holds in her free right hand stays level and the %s "
             "stays at the same height."},
    {"id": "polegar_no_bolso",
     "img": "Her free right thumb is hooked in the pocket of her shorts.",
     "take": "Her free hand stays hooked where it is and the %s stays at the "
             "same height."},
    {"id": "concha",
     "img": "Her free right hand is cupped under the fall, catching what "
            "misses.",
     "take": "Her cupped hand stays where it is and the %s stays at the same "
             "height."},
    {"id": "mao_na_cadeira",
     "img": "Her free right hand rests on the back of the white rocking chair "
            "beside her.",
     "take": "Her free hand stays on the chair back and the %s stays at the "
             "same height."},
    {"id": "antebraco_no_corrimao",
     "img": "Her free right forearm lies along the top of the rail, the hand "
            "hanging over the far side.",
     "take": "Her forearm stays on the rail and the %s stays at the same "
             "height."},
    {"id": "circulo_lento",
     "img": "Her pouring hand is caught mid-way through a small slow circle at "
            "the same height.",
     "take": "Her pouring hand keeps tracing the same small circle at the same "
             "height."},
    {"id": "chacoalho_curto",
     "img": "Her pouring hand is caught mid-shake, the stream breaking into a "
            "broader fall.",
     "take": "Her pouring hand keeps giving the %s the same small shake at "
             "the same height."},
    {"id": "xicara_na_mao",
     "img": "Her free right hand holds a mug at waist height.",
     "take": "The mug in her free right hand stays at that height and the %s "
             "stays at the same height."},
    {"id": "olhos_no_po",
     "img": "Her free right hand hangs loose at her side and her eyes are down "
            "on the powder.",
     "take": "Her free hand stays at her side and the %s stays at the same "
             "height."},
]

# ⚠️ AQUI A REACAO NAO E' CHOQUE: nada cresce (EX8). E' o registro com que ela
# EXECUTA a isca e a DEMOLE meio segundo depois — deadpan, ironia, ceticismo.
# ⛔ Zero `mouth open` / `lips parted` / `open-mouthed` / `tongue`: a expressao
# entra por sobrancelha, olho e queixo.
# ⛔ E zero verbo de crescimento (`rises`, `swells`): o `lint_nada_cresce` varre a
# direcao de cena e reprovaria o lote inteiro.
REACOES = [
    {"id": "deadpan",
     "desc": "her face stays completely flat, no expression at all, her eyes "
             "on the lens"},
    {"id": "sobrancelha_unica",
     "desc": "one eyebrow lifts higher than the other and stays lifted"},
    {"id": "meio_sorriso",
     "desc": "one corner of her mouth pulls back in a small dry smile and holds"},
    # ⚠️ ERA `her chin tucks back into her neckline`. `neckline` NAO casava nem o
    # `"neck "` (com espaco) do BANIDOS_GLOBAL nem o `\bneck\b` do `_ex7_lexico`,
    # e escapava por tecnicalidade de substring — para dentro da DIRECAO do TAKE
    # 01/03, que e' exatamente o bloco onde o geoduck vira pato. A tabela do EX7
    # ja' dizia "por isso nenhuma roupa do elenco diz `crew-neck` nem
    # `scoop-neck`": a regra tinha sido respeitada no figurino e furada numa
    # reacao. ⛔ O contrato dos pools agora cobra a substring, nao a palavra.
    {"id": "queixo_recuado",
     "desc": "her chin tucks back towards her collarbones, her eyebrows up"},
    {"id": "olhar_de_lado",
     "desc": "her eyes go down to the powder, come back to the lens and stay "
             "there"},
    {"id": "cabeca_inclinada",
     "desc": "her head tips slowly to one side and stays there"},
    {"id": "piscada_lenta",
     "desc": "she blinks once, slowly, without changing anything else"},
    {"id": "sobrancelhas_juntas",
     "desc": "both eyebrows pinch together and her eyes narrow"},
    {"id": "negativa_curta",
     "desc": "she gives one small shake of the head and stops"},
    {"id": "ombro_unico", "desc": "one shoulder lifts and drops once"},
    {"id": "olhos_largos",
     "desc": "her eyes widen once, her brows high, and settle there"},
    {"id": "riso_preso",
     "desc": "her cheeks push up once, her eyes creasing at the corners, and "
             "settle"},
]

# ⚠️ CADA ENTRADA E' COPIA LITERAL de `MECANISMOS_PROP` do `ressurreicao_short.py`
# — string validada e' constante, nunca redigitada. ⛔ O detalhe do `pousado` e'
# POR MECANISMO: mandar desenhar "its lid lying face-up" numa TIGELA e'
# contradicao dentro do proprio IMAGE.
MECANISMOS = [
    {"id": "tigela_cubos",
     "plantado": "a shallow white bowl of firm vivid purple gelatin cut into cubes, "
                 "each cube wobbling slightly",
     "curto": "the shallow white bowl of vivid purple gelatin cubes",
     "pousado": "uncovered, its serving spoon lying on the board beside it"},
    {"id": "pote_firme",
     "plantado": "a clear glass jar of gelatin already set firm and vivid purple",
     "curto": "the glass jar of set vivid purple gelatin",
     "pousado": "already open, its lid lying face-up on the board beside it"},
    {"id": "sache_aberto",
     "plantado": "a plain white sachet of pale gelatin powder torn open at the "
                 "top, standing upright",
     "curto": "the torn-open white sachet of pale gelatin powder",
     "pousado": "already torn, its foil top lying flat on the board beside it"},
    {"id": "mason_po",
     "plantado": "a wide-mouth mason jar half full of pale gelatin powder",
     "curto": "the mason jar of pale gelatin powder",
     "pousado": "already open, its lid lying face-up on the board beside it"},
    {"id": "copo_mexido",
     "plantado": "a glass tumbler of cold water with the gelatin already "
                 "stirred through it, still turning",
     "curto": "the glass tumbler of cold water with the gelatin stirred "
              "through it",
     "pousado": "already stirred, the wet spoon lying on the board beside it"},
    {"id": "panela_morna",
     "plantado": "a small enamel saucepan of warm vivid purple gelatin with a spoon "
                 "standing in it",
     "curto": "the enamel saucepan of warm vivid purple gelatin",
     "pousado": "already open, its lid lying face-up on the board beside it"},
    {"id": "pires_cubos",
     "plantado": "three firm vivid purple gelatin cubes stacked on a small white "
                 "saucer",
     "curto": "the saucer of stacked vivid purple gelatin cubes",
     "pousado": "uncovered, the emptied mould lying on the board beside it"},
    {"id": "tigela_lisa",
     "plantado": "a plain glass bowl of gelatin set firm, the surface catching "
                 "the light in one flat sheet",
     "curto": "the glass bowl of firm-set gelatin",
     "pousado": "uncovered, the mixing spoon lying on the board beside it"},
    {"id": "granulos",
     "plantado": "a squat unlabelled jar of pale gelatin granules with a "
                 "wooden scoop lying beside it",
     "curto": "the unlabelled jar of pale gelatin granules",
     "pousado": "already open, its lid lying face-up on the board beside it"},
    {"id": "copo_sache",
     "plantado": "a torn white sachet of gelatin powder lying flat beside a "
                 "tumbler of cold water",
     "curto": "the torn white sachet of gelatin powder",
     "pousado": "already poured, the wet spoon lying on the board beside it"},
    {"id": "forma_cubos",
     "plantado": "a shallow metal tray of set vivid purple gelatin scored right "
                 "through into squares",
     "curto": "the metal tray of vivid purple gelatin squares",
     "pousado": "uncovered, the scoring knife lying on the board beside it"},
    {"id": "tigela_madeira",
     "plantado": "a turned wooden bowl of firm vivid purple gelatin cubes piled above "
                 "the rim",
     "curto": "the wooden bowl of vivid purple gelatin cubes",
     "pousado": "uncovered, the emptied glass measure standing on the board "
                "beside it"},
]


# ###########################################################################
# POOLS DE COPY — ⛔⛔ A FONTE DA VERDADE E' A FALA DA ANGELA BROOKS (EX1)
# ###########################################################################
# TRES SELOS, e todo comentario de pool cita o seu:
#   [1] VERBATIM      — a fala da fonte como ela e' (§3 do mapa), com a UNICA
#                       edicao autorizada: `overnight` fora da primeira frase.
#   [2] RECOMBINACAO  — so' palavras ja' presentes na fala da fonte, reordenadas,
#                       segmentadas ou reconjugadas. ⛔ Nenhum claim novo. As
#                       unicas adicoes sao funcionais (`and`, `so`, `that's`,
#                       `otherwise`).
#   [3] COSTURA DO MECANISMO — frase da fonte com o NOSSO mecanismo no lugar do
#                       dela (`one ingredient` -> `the gelatin trick`, `Yes,` ->
#                       `Comment gelatin,`). E' o UNICO alinhamento autorizado.
#   [4] POOL VALIDADO DE OUTRO AGENTE SHORT — a costura do mecanismo MAIS um
#                       payload de CTA que ja' roda em outro motor nosso. ⛔ Toda
#                       entrada [4] cita `arquivo:linha` de origem.
#
# ⛔⛔ O SELO [4] NASCEU DE UMA REPROVACAO, e o registro fica porque o defeito era
# do SELO, nao da copy: quatro CTAs traziam palavra que a fonte nao tem (`use`,
# `where`/`get`, `recipe`, `whole`) e estavam marcadas `# [3]` — ou seja, a
# legenda declarava "frase da fonte" para frase que nao e' da fonte. Selo falso
# faz o proximo revisor concluir "tudo derivado da fonte" sem abrir o pool, e o
# selo E' o mecanismo de auditoria da EX1. As quatro sao a taxonomia [3] DA ORDEM
# DO OPERADOR ("pool ja' validado de outro agente SHORT"), que este arquivo tinha
# gasto no nome da costura — por isso a classe ganhou numero proprio em vez de a
# copy ser trocada (copy e' alcada do Ed).
# ⚠️ E o que uma [4] custa esta' declarado: `the recipe` e `where to get it`
# prometem na DM uma formula ou um ponto de venda, e a fonte promete a IDENTIDADE
# de um ingrediente. ⛔ Se o Ed quiser as nove CTAs 100% da fonte, o conserto e'
# trocar essas quatro por recombinacao pura — uma linha cada.
#
# ⛔ ENTRADA QUE NAO CAIBA EM NENHUM DOS QUATRO E' INVENCAO, e invencao viola a EX1.
# ⚠️ E QUANDO A FONTE NAO DA' MATERIAL, O POOL FICA MENOR E O NUMERO E' RELATADO
# (EX15). Tres ficam abaixo de 9 — ALIANCAS (5), GATES (6) e DESMENTIDOS (7) — e o
# motivo e' o mesmo nos tres: a fonte da' UMA frase curta de cada e nao ha'
# vocabulario nela para chegar a 14 sem escrever claim que ela nao fez.
# ⛔ Nao foi inventado nada para bater meta. A variancia da FALA compensa por
# COMBINACAO: cena 1 = 8x7x5 = 280, cena 2 = 9x10 = 90, cena 3 = 12x9x6 = 648.

# --- cena 1, batida 1 -------------------------------------------------------
# A isca absurda, com a UNICA edicao autorizada (`overnight` fora).
# ⛔ Todas trazem `{o}` e o literal `baking soda`; todas terminam no verbo de
# inchaco, que e' o motor da isca que a batida seguinte demole.
# ⚠️ `swell up` aqui e' a promessa DO VILAO: o video e' CONTRA o truque caseiro,
# e a demolicao vem meio segundo depois. ⛔ Isto nao autoriza crescimento em
# imagem nenhuma (EX8) — o linter varre a direcao de cena, nunca a fala.
# ⛔⛔ POOL REESCRITO EM 2026-08-10 (emenda da EX1). ERAM 8 ENTRADAS, SAO 10.
# ⚠️ O que saiu e POR QUE, entrada por entrada:
#   · `Baking soda. On your {o}. Watch it swell up.` — abertura de UMA
#     sentenca de duas palavras. O `medir_abertura` acusava exatamente ela:
#     6,7% das cenas 1 abriam em `Baking soda.`, sem referente. O teste WTF
#     nao perdoa: o espectador chega no meio do scroll e ouve `Baking soda.`
#     sozinho. Agora toda entrada e' UMA sentenca que ja' traz `your {o}`.
#   · `swell up` virou `swell`/`makes it swell` — em ingles americano
#     `swell up` e' PICADA DE ABELHA (inchaco de alergia), e a promessa da
#     isca e' de TAMANHO contra uma VSL de ereccao. A isca continua sendo a
#     promessa DO VILAO; ela so' parou de soar a pronto-socorro.
# ⛔ TODAS com exatamente 10 palavras (o `{o}` e' sempre 1 palavra): e' o que
# faz o teto de 25 fechar com o pior DESMENTIDO (7) e a pior FALHA (7).
# ⭐ CT7 permite o verbo de tumescencia AQUI: no take 1 de angulo de ISCA
# ABSURDA a promessa e' justamente a que o video desmente meio segundo depois
# (`isca_absurda=True` no `_ct16`). ⛔ Isto nao autoriza crescimento em imagem
# nenhuma (EX8) — o linter varre a direcao de cena, nunca a fala.
ISCAS = [
    "Pour baking soda on your {o} and watch it swell.",
    "Dump baking soda on your {o} and watch it swell.",
    "Pour baking soda over your {o} and watch it swell.",
    "Shake baking soda on your {o} and watch it swell.",
    "Sprinkle baking soda on your {o} and watch it swell.",
    "Cover your {o} in baking soda and watch it swell.",
    "They swear baking soda on your {o} makes it swell.",
    "Everybody swears baking soda on your {o} makes it swell.",
    "Baking soda on your {o}, and you watch it swell.",
    "Pour baking soda straight onto your {o}, watch it swell.",
]

# --- cena 1, batida 2 -------------------------------------------------------
# ⛔⛔ POOL REESCRITO EM 2026-08-10. ERAM 7 ENTRADAS, VIRARAM 10, A
# CONFERENCIA DO MESMO DIA DERRUBOU DUAS E REPOS DUAS: SAO 10.
# ⚠️ O DEFEITO QUE SAIU: as sete diziam a MESMA coisa — `you don't actually
# think that works, right?`. Tres problemas de uma vez:
#   (a) PERGUNTA RETORICA com `that` apontando para tras. Ouvida sozinha, no
#       meio do scroll, `that` nao tem dono.
#   (b) juntas com a ALIANCA, fechavam o take 1 em NEGACAO TRIPLA no frame
#       exato do corte, que e' onde a plataforma mede retencao.
#   (c) nenhuma DIZIA POR QUE nao funciona.
# ⭐ AGORA E' AQUI QUE A REGRA (EX2) SOBREVIVE, e ela sobrevive CONCRETA: o
# operador ja' tinha reprovado a forma abstrata em 2026-08-08 (*"The outside
# changes nothing" — "Outside de quE?"*). Na cena 1 o de-fora tem nome — e' o
# PO' que a tela esta' despejando naquele segundo.
#
# ⛔⛔ CONFERENCIA 2026-08-10 — DUAS ENTRADAS DERRUBADAS NA LEITURA EM VOZ ALTA,
# e o cabecalho antigo MENTIA sobre o proprio pool.
# ---------------------------------------------------------------------------
# O cabecalho afirmava *"6 das 10 entradas opoem fora/dentro"*. Contado no
# pool: UMA entrada tinha as duas palavras (`Nothing on the outside gets
# inside.`). Afirmacao de comentario que ninguem conta e' afirmacao que
# envelhece — o numero saiu e no lugar entrou uma LENTE (ver
# `_contrato_dos_pools`).
# ⛔ AS DUAS QUE CAIRAM eram `outside` NU, sem objeto e sem par `inside`:
#
#     ✗ The outside was never the problem.
#     ✗ The outside does nothing for you.
#
# E' a forma EXATA que o operador ja' reprovou em 2026-08-08 (*"Outside de
# quE?"*). Ouvida uma vez por um americano de 50-70 anos, `the outside` sozinho
# nao tem dono: pode ser a parte de fora da casa. As oito que ficaram nomeiam o
# PO' (`powder`) ou o GESTO (`what you pour on`), e agora isso e' cobrado.
# ⚠️ O POOL NAO ENCOLHEU: caiu para 8 e voltou a 10 com duas reposicoes de
# piso (marcadas no fim da lista). A ordem permanente do operador — *"nao
# sacrifique... perda de entropia"* — nao deixa entregar pool menor, e o
# `MIN_COPY` cobra isso. ⛔ As duas entradas novas sao COPY escrita pela
# conferencia: estao marcadas uma a uma para o Ed poder trocar a forma sem
# ter de descobrir quais sao.
# ⛔ Nenhuma entrada repete `baking soda`: a guarda de eco (`_repete`) casa
# bigrama de conteudo, e `baking soda` na batida 2 mataria a entrada contra
# TODAS as ISCAS de uma vez — entrada morta por eco e' entrada morta.
# ⛔ 4-7 palavras.
DESMENTIDOS = [
    "The powder does nothing.",
    "White powder fixes nothing.",
    "The powder never gets inside.",
    "No powder reaches the inside.",
    "Powder on the outside does nothing.",
    "Nothing on the outside gets inside.",
    "What you pour on does nothing.",
    "The powder sits there and does nothing.",
    # ⚠️ AS DUAS ULTIMAS SAO REPOSICAO DE PISO, escritas em 2026-08-10 pela
    # conferencia para o pool nao ENCOLHER (ordem permanente do operador:
    # *"nao sacrifique... perda de entropia"*). Sao recombinacao do mesmo beat
    # das outras seis — o `outside` aqui tem dono (`that powder`), e o
    # `inside` tem destinatario (`you`). ⛔ Copy nova: se o Ed nao gostar da
    # forma, o lugar de trocar e' aqui, e o pool continua com dez.
    "That powder stays on the outside.",
    "The powder can't get inside you.",
]

# --- cena 1, batida 3 -------------------------------------------------------
# ⭐⭐ A FALHA DELE — CT2 do CONTRATO DE COPY 16s, e o buraco mais caro que este
# motor tinha: NENHUM homem falhava em segundo algum, CT2 em 100% dos sorteios.
#
# ⛔ Sem auto-reconhecimento nao ha' comentario. Ele nao comenta porque a copy
# e' boa — comenta porque SE VIU. A linha modelo do parque inteiro e' de cinco
# palavras, um numero e um dano: `He'd lose it ten minutes in.`
# ⚠️ Aqui ela vai em SEGUNDA PESSOA, porque a cena 1 deste angulo ja' fala com
# o corpo do espectador (`your {o}`, EX14) e trocar para terceira no meio da
# mesma fala obriga a remapear quem e' quem em 8 segundos.
# ⭐ E ela fica na POSICAO FINAL do take 1 — a que o espectador leva para o
# corte. Antes essa posicao era da ALIANCA (`And you're right not to.`), que e'
# a terceira negacao seguida e nao entrega diagnostico nenhum.
# ⛔ 6-7 palavras. 8 das 12 trazem NUMERO — CONTADO, nao afirmado, depois de o
# cabecalho dos DESMENTIDOS ter sido pego mentindo sobre o proprio pool
# (`ten minutes`, `five minutes`,
# `two minutes`, `nine nights`), que e' o que transforma "as vezes falha" em
# um relogio que ele reconhece.
# ⛔ CONFERENCIA 2026-08-10 — UMA ENTRADA DERRUBADA NA LEITURA EM VOZ ALTA:
#
#     ✗ You still lose it before she does.
#
# `does` e' VERBO PROXY: para entender a frase o espectador tem de recuperar
# `lose it` da oracao anterior E aplica-lo a ELA — e `she loses it` nao quer
# dizer nada em ingles americano. Ouvida uma vez, a frase pergunta em vez de
# diagnosticar, e o beat de auto-reconhecimento (CT2) e' justamente o que nao
# pode custar processamento. As doze que ficaram dizem o dano com o verbo do
# dano. Agora e' lente (`_contrato_dos_pools`), nao gosto — e o piso foi
# reposto na ultima entrada: 12 -> 11 -> 12.
FALHAS16 = [
    "You still lose it ten minutes in.",
    "You still quit ten minutes in.",
    "Ten minutes in, you lose it anyway.",
    "You still go soft by minute ten.",
    "Five minutes in, you're soft again.",
    "You still go soft halfway through.",
    "Two minutes in, you already went soft.",
    "Nine nights out of ten, you quit.",
    "You still can't finish what you start.",
    "She waits, and you go soft anyway.",
    "You lost it again last Saturday night.",
    # ⚠️ REPOSICAO DE PISO (2026-08-10) — mesma batida, com numero e sem verbo
    # proxy, no lugar da que a conferencia derrubou.
    "You go soft four minutes in.",
]

# ⛔⛔ POOL APOSENTADO EM 2026-08-10 — NAO ALIMENTA MAIS A FALA.
# ---------------------------------------------------------------------------
# A ALIANCA (Benson §3: o ceticismo vira cumplicidade) era a batida 3 da cena 1
# e perdeu o lugar para as FALHAS16, por CT2 do contrato. ⛔ E nao foi troca de
# gosto, foi de ORCAMENTO MEDIDO: com a isca em 10 e o desmentido em 4-7, sobram
# 8 palavras ate' o teto de 25. Cabe UMA batida, e o contrato diz qual — o take
# 1 tem de terminar enunciando a falha, com dano concreto.
# ⚠️ O trabalho que a alianca fazia nao evaporou: quem converte o cetico agora e'
# o proprio DESMENTIDO, que deixou de ser pergunta retorica e passou a AFIRMAR
# o motivo (`powder on the outside does nothing`) — concordar com o cetico
# dizendo a razao dele em voz alta e' a mesma alavanca, mais barata.
# ⛔ Fica escrito em vez de apagado: pool que some sem explicacao vira divida, e
# reverter e' alcada do Ed (basta reabrir a batida 3 e cortar 3 palavras da
# isca).
ALIANCAS = [
    "And you're right not to.",                                     # [1]
    "You're right not to.",                                         # [2]
    "And you're right.",                                            # [2]
    "Right not to.",                                                # [2]
    "And you're right not to think that.",                          # [2]
]

# --- cena 2, batida 1 -------------------------------------------------------
# ⭐⭐ A REGRA (EX2) — o coracao do agente e a unica peca que nenhum outro agente
# nosso tem. ⛔ TODA entrada carrega alguma forma dela, e o linter cobra o par
# `outside`/`inside` (ou a recombinacao equivalente `pour on` + `what's
# happening`) na fala da cena 2.
# ⚠️ A spec de construcao trazia uma decima entrada — `Nothing you pour on your
# {o} changes what's happening inside.` — e ela SAIU do pool: ⛔ TODA entrada de
# MECANISMOS_FALA ja' carrega `{o}`, e as duas juntas nomeariam o orgao DUAS
# VEZES na mesma fala de 8 segundos, que e' bordao. ⛔ Entrada morta no pool e'
# pior que entrada ausente: quem edita depois nao sabe por que ela nunca sai.
REGRAS = [
    "Nothing you pour on the outside changes what's happening on the inside.",  # [1]
    "Nothing you pour on the outside changes what's happening inside.",         # [2]
    "What you pour on the outside changes nothing on the inside.",              # [2]
    "Nothing on the outside changes what's happening on the inside.",           # [2]
    "Nothing you pour on it changes what's happening inside.",                  # [2]
    "What's happening is on the inside. Nothing you pour changes that.",        # [2]
    "The outside doesn't change what's happening on the inside.",               # [2]
    "Outside changes nothing. What's happening is on the inside.",              # [2]
    "Pour it on the outside; the inside doesn't change.",                       # [2]
]

# --- cena 2, batidas 2 e 3 fundidas (circulacao + pressao) ------------------
# ⛔ TODA entrada carrega `{o}`, e isso e' MECANICO, nao estetico: e' ela que
# cumpre a cota do orgao da cena 2 E que satisfaz o gate `medir_contexto_copy` —
# a palavra `circulation` dispara o detector [B] de MECANISMO, e sem o ALVO NA
# MESMA FALA a cena e' reprovada como orfa (§17, "ta' deixando o viewer sem
# entender do que se trata").
# ⛔ E TODA entrada carrega `circulation` E `pressure` — e' o contrato que sustenta
# a EMENDA do PISO_FALA[2] (divergencia 1 da docstring), e desde 2026-08-03 e'
# cobrado no `_contrato_dos_pools` em vez de afirmado em comentario.
# ⚠️ COBERTURA DECLARADA: `firm` (a palavra de payoff mais concreta da fonte,
# `Getting firm is blood coming in with pressure`) esta' em 8 das 10 — as entradas
# [2] e [7] largam `firm` porque a fonte tambem tem a forma sem ele
# (`What makes your {o} actually respond is one thing, circulation`) e as duas sao
# recombinacao dessa metade. ⛔ Numero relatado, nao escondido (EX15).
MECANISMOS_FALA = [
    # [1] as duas falas da fonte (10,66-13,38 e 13,90-16,06) em sequencia
    "What makes your {o} actually respond is one thing, circulation. Getting "
    "firm is blood coming in with pressure.",
    "What makes your {o} respond is circulation. Getting firm is blood coming "
    "in with pressure.",                                                    # [2]
    "What makes your {o} actually respond is circulation, blood coming in "
    "with pressure.",                                                       # [2]
    "One thing makes your {o} respond: circulation. Getting firm is blood "
    "coming in with pressure.",                                             # [2]
    "Getting your {o} firm is blood coming in with pressure. That's "
    "circulation.",                                                         # [2]
    "Your {o} responds to one thing, circulation. Getting firm is blood "
    "coming in with pressure.",                                             # [2]
    # ⚠️ ESTA ENTRADA GANHOU `Circulation` DEPOIS DE MEDIDA: sem ela, 33 de 400
    # videos (8,2%) saiam com a cena 2 sem a palavra — e a justificativa escrita
    # da EMENDA do PISO_FALA[2] afirma "toda entrada de MECANISMOS_FALA carrega
    # circulacao E pressao. Nenhum beat cai". A afirmacao era prosa; agora e'
    # contrato (`_contrato_dos_pools`).
    "Getting firm is blood coming in with pressure. Circulation is what makes "
    "your {o} respond.",                                                    # [2]
    "Blood coming in with pressure is what makes your {o} actually respond. "
    "Circulation.",                                                         # [2]
    "What makes your {o} firm is one thing, circulation. Blood coming in with "
    "pressure.",                                                            # [2]
    "Circulation. That's what makes your {o} actually respond. Getting firm "
    "is blood coming in with pressure.",                                    # [2]
]

# --- cena 3, batidas 1 e 2 FUNDIDAS ----------------------------------------
# ⭐ AQUI MORA A UNICA COSTURA NOSSA: onde a fonte diz `one ingredient`, entra
# `gelatin trick`. ⛔ TODAS carregam o literal MINUSCULO `gelatin trick` — e' o
# que o `lint_curto(literais=("gelatin trick",))` cobra, e sem ele o criativo
# deixa de ser congruente com o que a VSL vende.
#
# ⭐ EX3 — O BATISMO MORA NA CENA 3, E ESSA E' UMA DIVERGENCIA DECLARADA DO
# PADRAO SHORT. O CLAUDE.md e o short_comum.py dizem que a copy fundida da CENA 2
# carrega o literal. Aqui nao, por duas razoes de ARCO: (1) a cena 2 ja' tem dono,
# e' A REGRA (EX2); (2) na fonte o ingrediente so' aparece em 21s de 30 — no
# ultimo terco, DEPOIS do problema. Subir o batismo gasta a curiosidade 8 segundos
# cedo e deixa a cena 3 com nada alem do CTA. ⚠️ O linter continua satisfeito: ele
# varre o CORPO DAS TRES FALAS JUNTAS, nao a cena 2 especificamente.
#
# ⚠️ ESTE POOL E' A FUSAO das duas pontas da spec de construcao (`PROBLEMAS` e
# `OPEN_LOOPS`), e e' a saida (a) que a propria doutrina prescreve na EX12: com os
# dois pools separados a cena 3 sairia com 33-43 palavras contra um teto de 34,
# sobrando ~5 das 81 combinacoes, todas forcadas ao CTA e ao gate mais curtos.
# ⚠️ A cauda `no matter how many tricks you try` da fala 16,36-20,46 nao cabe em
# 8s; `no trick you try works` e' ela reaproveitada curta.
#
# ⛔⛔ TODA ENTRADA DIZ O QUE A PRESSAO FRACA QUEBRA, e isto e' CONTRATO cobrado no
# `_contrato_dos_pools`, nao estilo. A fonte diz a causa E a consequencia na mesma
# oracao — `When the pressure is weak, THE BODY CAN'T KEEP UP` (16,36-20,46) — e a
# primeira versao deste pool tinha 8 de 12 entradas que diziam so' a causa. ⛔ Isso
# NAO era eufemismo nem moderacao: era a oracao da consequencia APAGADA, o motor
# ficando MENOS explicito que a fonte. Medido: 268 de 400 videos (67,0%) saiam com
# a cena 3 sem nome de orgao E sem `can't keep up` — que e' o §17 das licoes em
# estado puro ("frase que nomeia causa sem dizer o que ela quebra"), e o
# `medir_contexto_copy` nao pegava porque `weak` nao esta' no lexico dele.
#
# ⚠️ COBERTURA DAS BATIDAS DA FONTE, MEDIDA E DECLARADA (o que a EX15 manda relatar
# em vez de esconder). 12 entradas, faixa 17-19 palavras, 308 das 648 combinacoes
# de cena 3 na banda 30-34:
#     consequencia  `the body/your {o} can't keep up` .......... 12/12
#     mecanismo     `gelatin trick` ............................ 12/12
#     open loop A   `at the root` ...............................  4/12
#     open loop B   `(real) force again` .........................  2/12
#     cauda         `no trick you try works` / `nothing you try`.  2/12
#     orgao         `{o}` .......................................  4/12
# ⚠️ `at the root` caiu de 7/12 para 4/12 e o motivo e' aritmetico, nao editorial:
# `the body can't keep up` custa 5 palavras e `at the root` custa 3, e as duas
# juntas com o batismo nao cabem em 19 numa cena cujo teto e' 34 com CTA+gate de
# 15-19. ⛔ A troca foi consequencia (4->12) por open loop A (7->4), e o beat que
# ganhou e' o que o espectador precisa para entender do que se trata.
FUNDIDAS = [
    # [3] o corte do proprio operador + 16,36-20,46 (causa E consequencia) +
    #     21,00-23,36 com `one ingredient` -> `the gelatin trick`
    "Weak pressure. Your {o} can't keep up. The gelatin trick takes care of "
    "that at the root.",
    "When the pressure is weak, your {o} can't keep up. The gelatin trick "
    "takes care of that.",                                                  # [3]
    "Weak pressure, and the body can't keep up. The gelatin trick takes care "
    "of that at the root.",                                                 # [3]
    "Weak pressure, the body can't keep up, and the gelatin trick takes care "
    "of that at the root.",                                                 # [3]
    "The body can't keep up with weak pressure. One thing takes care of "
    "that: the gelatin trick.",                                             # [3]
    "Weak pressure, the body can't keep up, no trick you try works. The "
    "gelatin trick takes care of it.",                                      # [3]
    # [3] 23,58-25,78 `getting the blood to show up with real force again`
    #     com o sujeito nomeado
    "Weak pressure, the body can't keep up. The gelatin trick gets the blood "
    "showing up with force again.",
    "Weak pressure, the body can't keep up. The gelatin trick gets the blood "
    "showing up with real force.",                                          # [3]
    "Weak pressure, the body can't keep up. That's what the gelatin trick "
    "takes care of, at the root.",                                          # [3]
    "When the pressure is weak, your {o} can't keep up. The gelatin trick is "
    "the one thing for that.",                                              # [3]
    "The pressure is weak, so your {o} can't keep up. The gelatin trick "
    "takes care of it.",                                                    # [3]
    "Weak pressure, the body can't keep up. Nothing you try works. The "
    "gelatin trick takes care of it.",                                      # [3]
]

# --- cena 3, batida 3 -------------------------------------------------------
# ⛔ TODAS carregam o literal `Comment gelatin,` (minusculo, com virgula). A
# frase-base e' a da fonte (`and I'll send you exactly what it is`) com a nossa
# keyword na frente no lugar do `Yes,`.
# ⭐ E a fonte ja' passa no `lint_isca_cta` sem uma virgula de mudanca: ela DIZ O
# QUE A PESSOA RECEBE. E' mais um motivo para a copy dela ser lei aqui.
# ⛔ `BOOK` e `YES` proibidos (quebram a automacao DM); ⛔ keyword em CAIXA ALTA
# faz o Veo soletrar. ⛔ Zero vocativo aqui — vocativo so' nos GATES (TR15).
# ⚠️ CINCO SAO [3] e QUATRO SAO [4] — o payload das quatro nao esta' na fonte e o
# selo diz de onde ele veio. ⛔ Nao remarcar como [3] "para ficar uniforme".
# ⛔⛔ POOL REESCRITO EM 2026-08-10 — CT6 DO CONTRATO, QUE ESTAVA EM 100%.
# ---------------------------------------------------------------------------
# ⭐⭐ A DESCOBERTA QUE FAZ A CONTA FECHAR: a COBERTURA SOCIAL nao cabe como
# batida propria em 25 palavras. Ela mora DENTRO da sentenca do CTA.
#
#     antes:  Comment gelatin, and I'll send you the recipe.        (9 pal.)
#     depois: Comment gelatin, and the recipe goes to your messages. (9 pal.)
#
# MESMO CUSTO, e entrega de graca (a) o endereco da entrega, (b) a privacidade
# e (c) o fato de que nao e' na tela publica.
# ⚠️ POR QUE ISTO NAO E' ENFEITE: o KPI deste funil e' uma CONFISSAO PUBLICA —
# o comentario leva nome e foto e vai para o feed. Quanto melhor o diagnostico
# em 2a pessoa (e o take 1 agora tem um), MAIS CARO fica comentar. Em 48
# segundos de copy dos tres lotes revisados nao havia UMA palavra baixando esse
# custo.
# ⛔ 8-9 palavras, todas com o literal `Comment gelatin,`, todas dizendo O QUE
# chega (`recipe`, cobrado pelo `lint_isca_cta`) e ONDE (`your messages` /
# `your inbox`, cobrado pelo CT6). ⛔ Zero `I'll send you` sozinho: mandar sem
# dizer para onde e' exatamente o que a lente acusava.
# ⚠️ Eram 9 entradas; sao 10. A conferencia de 2026-08-10 leu as dez em voz
# alta e nao derrubou nenhuma.
# ⚠️ 2026-08-10 — CONECTOR OBRIGATORIO DEPOIS DA KEYWORD. Medido: 81% dos
# CTAs deste motor saiam como `Comment gelatin, your inbox gets...` — emenda
# de virgula na unica frase do video que gera receita. Sem conector as duas
# oracoes colidem no ouvido e o imperativo (`Comment gelatin`) deixa de soar
# como comando. Custa UMA palavra e havia 3 de folga no teto.
CTAS = [
    "Comment gelatin, and the recipe goes to your messages.",
    "Comment gelatin, and the recipe lands in your messages.",
    "Comment gelatin, and the recipe hits your messages.",
    "Comment gelatin, and the recipe comes to your messages.",
    "Comment gelatin, and the recipe arrives in your messages.",
    "Comment gelatin, and the recipe waits in your messages.",
    "Comment gelatin, and the whole recipe hits your messages.",
    "Comment gelatin, and the recipe goes to your inbox.",
    "Comment gelatin, and the recipe lands in your inbox.",
    "Comment gelatin, and the recipe goes straight to your messages.",
]

# --- cena 3, batida 4 -------------------------------------------------------
# ⚠️ POOL PEQUENO E DECLARADO: a fonte da' UM gate. Seis entradas, todas
# recombinacao do mesmo `follow me first / I can't reach you`.
# ⛔ Nao mexer no MOTIVO do gate — pedido + porque e' Langer (1978), e e' literal
# na `espinha-fixa`.
GATES = [
    "Follow me first or I can't reach you.",                        # [1]
    "Follow first, or I can't reach you.",                          # [2]
    "I can't reach you unless you follow me first.",                # [2]
    "Follow me, or I can't reach you.",                             # [2]
    "No follow, and I can't reach you.",                            # [2]
    "Follow me first. Otherwise I can't reach you.",                # [2]
]

VOCATIVOS = ("brother", "my friend", "guys", "buddy", "girls")


# ---------------------------------------------------------------------------
# TABELAS DE TOKEN BANIDO (o linter compartilhado le' estas)
# ---------------------------------------------------------------------------
# ⚠️ Direcao de cena, NUNCA fala. E' por isso que `swell up` (EX1/ISCAS) nao e'
# tocado por nada disto.
# ⛔ E' aqui que mora a ARMADILHA DO GEODUCK: `duck`, `goose` e `bird` NAO podem
# entrar em tabela nenhuma, porque a EX_BLINDAGEM_FORMA os contem literalmente e
# um `\bduck\b` reprovaria 100% dos lotes.
BANIDOS_TAKE = {
    "engorged": "adjetivo de estado — vocabulario de tumescencia",
    "tumescent": "idem",
    "throbbing": "idem",
    "veiny": "detalhe anatomico no prop",
    "veins": "idem",
    # EX7 — `geoduck` so' no IMAGE. No TAKE o nome da especie faz o modelo buscar
    # o BICHO no treino, e o bicho vem com cabeca. No movimento ele diz `the clam`
    # ou `the pale tan shellfish`.
    "geoduck": "EX7 — no TAKE o prop e' 'the clam', nunca a especie nomeada",
}
BANIDOS_IMAGE = {
    "engorged": "adjetivo de estado — vocabulario de tumescencia",
    "tumescent": "idem",
    "throbbing": "idem",
    "veiny": "detalhe anatomico no prop",
    "veins": "idem",
}

# ⛔ substring, em qualquer bloco.
BANIDOS_GLOBAL = {
    # EX8 — nada cresce, entao nao ha' o que chamar de tecnica de transformacao
    "morph": "EX8 — neste agente nada cresce; nome de tecnica so' convida o efeito",
    "time-lapse": "idem", "before and after": "idem",
    "transforms": "idem", "vfx": "idem",
    "jump cut": "EX11 — a varanda e' a mesma nas tres cenas, sem corte interno",
    "quick cut": "idem", "smash cut": "idem", "match cut": "idem",
    "cross-fade": "idem", "crossfade": "idem", "dissolve to": "idem",
    "transition": "idem",
    "whoosh": "efeito grafico/sonoro — nao ha' efeito nenhum neste agente",
    "glow": "idem", "lens flare": "idem", "particle": "idem",
    "sparkle": "idem", "shimmer": "idem", "flash": "idem",
    # EX7 — `neck` no prop e' o token que puxa o pescoco de ave; a peca do
    # geoduck e' o SIFAO. ⚠️ Por isso nenhuma roupa do elenco diz `crew-neck` nem
    # `scoop-neck`: seria falso positivo garantido nesta tabela.
    "neck ": "EX7 — a peca do geoduck e' o 'siphon', nunca 'neck'",
    "the victim": "rotulo que significa dano — descrever a pessoa",
    "the narrator": "idem — ou nomear a relacao",
}

BANIDOS_CTA = {
    "book": "quebra a automacao Comentario->DM (e e' a palavra do reel de 82K)",
    "yes": "idem",
    "link": "CTA e' comentario, nao link",
}

# ⛔ EX9 — o guardrail de figurino: zero vocabulario de desejo. A roupa entra como
# PECA descrita, nunca como adjetivo de desejo.
BANIDOS_DESEJO = {
    "sexy": "vocabulario de desejo — a roupa entra como PECA descrita",
    "seductive": "idem", "sultry": "idem", "curvy": "idem",
    "revealing": "idem", "cleavage": "idem", "lingerie": "idem",
    "provocative": "idem", "alluring": "idem", "flirty": "idem",
    "attractive": "idem", "beautiful": "idem",
    "baby tee": "o token `baby` entra de graca num video de conteudo adulto",
}


# ---------------------------------------------------------------------------
# HELPERS
# ---------------------------------------------------------------------------

def _palavras(txt):
    """Contrato do linter compartilhado: palavra e' letra, apostrofo e hifen."""
    return len(re.findall(r"[A-Za-z'\-]+", txt))


_CACHE_W = {}


def _w(txt):
    """`_palavras` memoizado — o sorteio pesa centenas de combinacoes por video,
    e recompilar regex em cada uma custa segundos no self-test."""
    n = _CACHE_W.get(txt)
    if n is None:
        n = _CACHE_W[txt] = _palavras(txt)
    return n


def _maiuscula(txt):
    return txt[0].upper() + txt[1:] if txt else txt


# ⛔ O SLOT QUE CAI NO INICIO DA FRASE. Guarda barata: se um dia um `{o}` abrir
# uma oracao, a copy sairia em minuscula e leria como erro de motor para quem
# aprova o lote.
_RX_FRASE = re.compile(r"(^|[.!?]\s+)([a-z])")


def _pontuar(fala):
    return _RX_FRASE.sub(lambda m: m.group(1) + m.group(2).upper(), fala)


def _slot(txt, val):
    """Preenche o `%s` de uma entrada de pool — e devolve o texto intacto quando
    a entrada nao tem slot.

    ⛔ Existe porque `"sem slot" % val` NAO e' no-op em Python: levanta
    `TypeError: not all arguments converted`. Nem toda entrada de DESPEJOS nomeia
    o recipiente (a mao livre pode estar no quadril, no bolso ou no corrimao), e
    ⛔ nao se poe slot por simetria so' para o `%` nao quebrar.
    """
    return txt % val if "%s" in txt else txt


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


def _tri(txt):
    """Os trigramas de uma frase, para achar eco de FORMULA (nao de fato)."""
    p = re.findall(r"[a-z']+", (txt or "").lower())
    return {tuple(p[i:i + 3]) for i in range(len(p) - 2)}


# ⛔ PALAVRAS FUNCIONAIS — o que NAO conta como eco quando se repete sozinho.
# Os pools saem todos do mesmo paragrafo de 111 palavras: `you`, `the`, `that` e
# `is` se repetem por construcao e banir isso mataria o motor. O que incomoda o
# ouvido em 8 segundos e' a palavra de CONTEUDO voltando.
PALAVRAS_FUNCIONAIS = frozenset((
    "a", "an", "and", "are", "as", "at", "be", "but", "by", "can't", "do",
    "does", "doesn't", "don't", "for", "from", "he", "her", "his", "i", "i'll",
    "if", "in", "is", "it", "its", "me", "my", "no", "not", "of", "on", "one",
    "or", "otherwise", "our", "out", "own", "she", "so", "that", "that's",
    "the", "their", "them", "then", "there", "there's", "they", "this", "to",
    "unless", "up", "was", "we", "what", "what's", "when", "with", "you",
    "you're", "your",
))


def _bi_conteudo(txt):
    """Os bigramas com ao menos UMA palavra de conteudo.

    ⛔⛔ ISTO EXISTE PORQUE O TRIGRAMA MEDIU 41% DE ECO E NAO ACUSOU NENHUM. A
    colisao real deste agente atravessa a FRONTEIRA DE FRASE: os DESMENTIDOS
    terminam em `...think that works, right?` e uma das ALIANCAS e' `And you're
    right not to think that.` — as duas trazem `think that`, e nao ha' UM trigrama
    em comum entre elas, entao o guarda passava. Medido em 400 sorteios: 164
    videos (41,0%) diziam `think that` duas vezes na mesma fala de 8 segundos, o
    pior indice do repo (o segundo pior e' 12,0% no organicwave).
    ⚠️ A docstring do `_repete` afirmava que "trigrama pega o eco de formula sem
    lista para manter — que e' o caso real aqui". Medido, nao pegava: era exatamente
    a afirmacao de comentario que ninguem tinha cobrado.
    """
    p = [w for w in re.findall(r"[a-z']+", (txt or "").lower())]
    return {tuple(p[i:i + 2]) for i in range(len(p) - 1)
            if not (p[i] in PALAVRAS_FUNCIONAIS
                    and p[i + 1] in PALAVRAS_FUNCIONAIS)}


def _repete(a, b):
    """Duas batidas da mesma cena repetem uma expressao inteira?

    ⚠️ Guarda de ENTROPIA, nao de doutrina: entra como filtro com fallback, e ⛔
    nenhuma entrada de pool foi tocada por causa dela — o conserto do eco de 41%
    mora AQUI, no guarda, e nao numa reescrita de copy (que e' alcada do Ed).
    ⛔ Sao DUAS peneiras e elas pegam coisas diferentes: o trigrama pega a formula
    inteira repetida; o bigrama de conteudo pega o par de palavras que volta
    atravessando a fronteira de frase, que era o buraco real.
    """
    return bool((_tri(a) & _tri(b)) or (_bi_conteudo(a) & _bi_conteudo(b)))


def _achar(txt, tokens):
    """Os tokens de uma tabela que aparecem no texto (palavra inteira)."""
    return [t for t in tokens if re.search(r"\b%s\b" % re.escape(t), txt, re.I)]


def _faltam(txt, tokens):
    return [t for t in tokens if t not in txt]


# ---------------------------------------------------------------------------
# LEDGER — EX16
# ---------------------------------------------------------------------------
# Os eixos de ROSTO evitam as 3 ultimas saidas (rosto repetido e' o que o operador
# ve' primeiro no lote); os demais evitam as 2 ultimas. Sem isso um lote de 20
# videos repete rosto e cenario mesmo com pool grande.
EIXOS_LEDGER = ("narradora", "homem", "varanda", "mesa", "caixa", "despejo",
                "reacao", "mecanismo")


def _carregar_ledger():
    if os.path.exists(LEDGER):
        with open(LEDGER, encoding="utf-8-sig") as f:
            return json.load(f)
    return {}


def _anotar(ledger, spec):
    """Anota o sorteio no ledger EM MEMORIA, sem tocar no arquivo.

    ⚠️ Existe separado do `_gravar_ledger` por causa do `--dry-run`: sem isto os
    N videos de um mesmo lote sao sorteados todos contra o mesmo historico e o
    `_evitando()` nao ve' o irmao que acabou de sair.
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


# ---------------------------------------------------------------------------
# ⭐⭐ A FALA DA CENA FUNDIDA — EIXOS COMPOSTOS (2026-08-08)
# ---------------------------------------------------------------------------
# ⛔ Os pools da cena 3 do motor de 24s NAO servem aqui: o menor par
# FUNDIDA+CTA+GATE de la' da' 32 palavras contra o teto fisico de 25. A cena
# fundida foi RECONSTRUIDA, e o operador aprovou a forma (lote 1, 2026-08-08):
#
#     {MECANISMO} {PROVA} {CTA} {FOLLOW}
#
# ⛔⛔ DUAS ORDENS DELE, E AS DUAS VIRARAM LENTE:
#   1. *"nao use pronome, seja taxativo e claro"* — reprovou `That's what he's
#      holding.`: `he` sem dono e `that` sem referente. Nenhuma entrada abaixo
#      abre com pronome, e o DISCLOSURE nomeia o vinculo (`my husband`), que e'
#      quem esta' no quadro segurando o prop limpo. ⚠️ Ate' 2026-08-09 esse
#      beat era a PROVA (`the man beside me`) — o operador trocou por
#      disclosure em primeira pessoa; ver o cabecalho de DISCLOSURES16.
#   2. *"muito vaga e ocupando tempo precioso"* — reprovou `The outside changes
#      nothing.`: o de fora DE QUE, muda O QUE. Todo beat aqui nomeia coisa
#      concreta: sangue, pressao, o orgao, o homem, o gelatin trick.
# ⭐ E' por isso que sao EIXOS e nao uma frase: frase unica em pool de um
# entrega o mesmo video sempre, e o operador ja' me devolveu isso uma vez
# (`she feels it first` no TRIO 16). A variacao mora na COMBINACAO.

# ⚠️ Cada entrada nomeia SANGUE, PRESSAO e o ORGAO — sem os tres a frase vira
# "algo melhora la' dentro", que e' o drifting que o operador reprovou em
# 2026-08-08. ⛔ Nenhuma abre com pronome (*"nao use pronome, seja taxativo e
# claro"*).
# ⭐ ESTE E' O BEAT QUE NENHUM OUTRO AGENTE DO PARQUE TEM, e a reforma de
# 2026-08-10 NAO o tocou no conteudo — ele so' passou a ter DONO e ALVO fixos.
# ⛔⛔ TODAS COM EXATAMENTE 6 PALAVRAS, e isso e' orcamento medido, nao gosto:
# 6 + 8 (disclosure) + 2 (follow) + 9 (o CTA mais caro) = 25, o teto no fio.
# Uma entrada de 7 mataria os CTAs de 9 palavras por [ALCANCE] — que e' a
# armadilha §36 exata (`pool que vai de 6 a 14 num teto de 25 nao e' pool de
# 12, e' pool de 4 com oito enfeites`). Cobrado no `_contrato_dos_pools`.
# ⚠️ Eram 10 entradas; sao 11. As formas longas que sairam (`What firms your
# {o} is blood with pressure.`, 8 palavras) diziam o MESMO que as curtas —
# este e' o beat INTERCAMBIAVEL do take 2, e num teto apertado o beat
# intercambiavel e' quem tem de encolher.
# ⛔ Zero `blood pressure` COLADO: em ingles americano isso e' hipertensao, e o
# video passaria a falar de outra doenca. Cobrado por regex no contrato.
# ⛔ Zero verbo de ereccao (CT7): `firms`/`fills`/`carries` passam no gerador,
# `hard`/`stands up`/`comes back` reprovam ~95% quando colados no orgao.
MECANISMOS16 = [
    "Blood with pressure firms your {o}.",
    "Blood under pressure firms your {o}.",
    "Blood with pressure fills your {o}.",
    "Your {o} needs blood under pressure.",
    "Pressure drives blood into your {o}.",
    "Pressure carries blood into your {o}.",
    "Pressure pushes blood through your {o}.",
    "Pressure moves blood into your {o}.",
    "Pressure holds blood inside your {o}.",
    "Pressure keeps blood in your {o}.",
    "Pressure feeds blood to your {o}.",
]

# ⭐⭐ O DISCLOSURE — ordem do operador, 2026-08-09, e ela e' de ARCO.
# ---------------------------------------------------------------------------
# Ele leu um lote e escreveu:
#
#     *"Acho que uma copy melhor para o take 2 seria um DISCLOSURE do take 1:
#      what really worked for my husband or fiancee (por conta do pool) was the
#      gelatin trick I've discovered."*
#
# ⭐ E ele esta' certo sobre o buraco. A cena 1 termina em `And you're right` —
# ela ACABA DE DEMOLIR a isca e deixa a pergunta aberta *"entao o que funciona?"*.
# A PROVA antiga (`The man beside me used the gelatin trick.`) respondia de
# lado: um terceiro anonimo fez uma coisa. Disclosure responde de frente, e em
# primeira pessoa — quem fala e' a mulher que viu funcionar em casa.
#
# ⚠️ MAS A VERSAO LITERAL DELE NAO CABE, e o motivo esta' medido, nao suposto.
# A dele tem 23 palavras somando CTA e follow e SO' cabe porque larga o
# MECANISMO — e o mecanismo e' o herdeiro funcional de A REGRA (EX2), a unica
# peca que nenhum outro agente do parque tem, cobrada em ERRO por `_ex2_regra`.
# Sem `blood` + `pressure` + orgao, o EXTERIOR 16 vira "isca absurda + gelatin
# trick", que qualquer um dos outros vinte ja' e'. Entao o disclosure entra NO
# LUGAR DA PROVA, no mesmo orcamento de 6-9 palavras, e o mecanismo fica.
# ⛔ Se ele quiser a versao literal mesmo assim, e' decisao dele — mas custa
# aposentar a `_ex2_regra` e deixar a cena 2 sem nomear o orgao (cota 1/2).
#
# ⛔⛔ POOL REESCRITO EM 2026-08-10 — CT3 DO CONTRATO, QUE ESTAVA EM 100%.
# ---------------------------------------------------------------------------
# ⭐ O DEFEITO ERA ESTRUTURAL, nao de estilo: `The gelatin trick is what fixed
# my man.` nomeia o mecanismo e NAO DIZ O QUE ELE FAZ. Nome de mecanismo sem
# razao ao lado nao vira crenca — vira ruido de marca, e o espectador nao tem
# no que acreditar quando o CTA pede o comentario meio segundo depois.
#
#     RUIM: The gelatin trick is what fixed my man.
#     BOM : The gelatin trick fixed my husband's blood flow.
#
# ⛔ CONTRATO DE CADA ENTRADA (cobrado no `_contrato_dos_pools`, nao afirmado):
#     · o literal `gelatin trick`
#     · `{par}` — o VINCULO nomeado (ordem do operador, 2026-08-09: disclosure
#       em primeira pessoa, nao prova de terceiro anonimo)
#     · um VERBO DE EFEITO da lista `sc.VERBOS_EFEITO_16` na MESMA sentenca
#     · um ALVO (`blood` / `pressure`) na MESMA sentenca
#     · exatamente 8 palavras
# ⚠️ A LISTA DE VERBOS E' LITERAL E EM REGEX DE PALAVRA INTEIRA: `opens` esta'
# nela, `opened` NAO. Escrever `opened` aqui deixaria a lente cega e a entrada
# passaria como rotulo nu. So' entram passados que a lista tem: `fixed`,
# `changed`, `started`, `made`, `gave`, `turned`, `worked`.
# ⚠️ Eram 9 entradas, viraram 10, a conferencia do mesmo dia derrubou duas e
# repos duas: sao 10 (ver o bloco logo acima do pool).
# ⭐ POR QUE O DISCLOSURE E' TAMBEM A PROVA: ele responde de frente a pergunta
# que a cena 1 deixa aberta (*"entao o que funciona?"*), em primeira pessoa, e
# a pessoa que responde e' a que esta' no quadro ao lado do corpo-prova.
# ⛔⛔ CONFERENCIA 2026-08-10 — DUAS ENTRADAS DERRUBADAS NA LEITURA EM VOZ ALTA.
# ---------------------------------------------------------------------------
#     ✗ The gelatin trick gave {par} pressure back.
# `pressure` SOZINHO, sem `blood` na mesma sentenca. Para um americano de 50-70
# anos `pressure` nu e' PRESSAO ARTERIAL — e "deu a pressao dele de volta" e'
# uma coisa RUIM na cabeca dessa faixa etaria, que toma remedio para baixa-la.
# ⚠️ E' a mesma armadilha que o proprio motor ja' cobra em `MECANISMOS16`
# (`blood pressure` colado = hipertensao), so' que pela outra ponta: la' o
# defeito e' juntar demais, aqui e' soltar o `pressure` do `blood`.
#
#     ✗ The gelatin trick works on {par}'s blood.
# `works on ... blood` e' o ROTULO NU do CT3 disfarcado de razao: `works` passa
# na lista de verbos mas nao diz EFEITO nenhum — "funciona" e' a afirmacao que
# a sentenca deveria estar provando. E em ingles americano `work on his blood`
# puxa exame de sangue, nao ereccao.
# ⚠️ 10 -> 8 -> 10: as duas que cairam foram REPOSTAS por entradas do mesmo
# beat (marcadas no fim da lista), porque pool nao pode encolher. Todas as dez
# trazem `blood` E um verbo que diz o que acontece com ele (`fixed`, `moves`,
# `unblocks`, `holds`, `opens`...). Os dois criterios viraram lente no
# `_contrato_dos_pools`.
DISCLOSURES16 = [
    "The gelatin trick fixed {par}'s blood flow.",
    "The gelatin trick changed {par}'s blood flow.",
    "The gelatin trick started {par}'s blood moving.",
    "The gelatin trick keeps {par}'s blood coming.",
    "The gelatin trick moves {par}'s blood again.",
    "The gelatin trick unblocks {par}'s blood flow.",
    "The gelatin trick brings {par}'s blood back.",
    "The gelatin trick holds {par}'s blood in.",
    # ⚠️ AS DUAS ULTIMAS SAO REPOSICAO DE PISO (2026-08-10). As duas dizem o
    # EFEITO com o verbo do efeito e trazem `blood` — os dois criterios que
    # derrubaram as anteriores. ⭐ `opens ... blood vessels` e' a formulacao
    # mais legivel do pool inteiro para 50-70 anos: e' a frase que o
    # cardiologista deles ja' usou.
    "The gelatin trick opens {par}'s blood vessels.",
    "The gelatin trick made {par}'s blood move.",
]

# ⛔⛔ TODAS COM DUAS PALAVRAS, e isso e' orcamento, nao gosto: uma entrada de
# tres empurraria os disclosures de 9 para fora da banda e mataria dois deles em
# silencio. Cobrado no `_contrato_dos_pools`.
# ⚠️ `fiance`, nao `fiancee`: no ingles dos EUA a forma com dois `e` e' a
# MULHER noiva. Quem esta' no quadro e' ele.
# ⭐ O homem continua NOMEADO — o que muda e' que ele deixa de ser um terceiro
# anonimo (`the man beside me`) e passa a ser o dela. Ele esta' cortado no peito
# e sem rosto, entao o espectador nao julga a idade: o vinculo e' o que a fala
# disser.
# ⛔ `my partner` SAIU EM 2026-08-10. Ele DESIDENTIFICA a unica prova social do
# video: `partner` em ingles americano e' o termo neutro de quem nao quer dizer
# o genero, e o quadro mostra um HOMEM cortado no peito. O espectador de 50-70
# anos que a pagina persegue nao chama a mulher dele de `my partner`.
# ⚠️ No lugar entrou `my guy` — duas palavras, coloquial e inequivocamente
# masculino. ⚠️ `fiance`, nao `fiancee`: no ingles dos EUA a forma com dois `e`
# e' a MULHER noiva. Quem esta' no quadro e' ele.
PARES16 = ("my husband", "my man", "my fiance", "my guy")

# ⛔⛔ O FOLLOW MUDOU DE LUGAR EM 2026-08-10 — CT1 DO CONTRATO, QUE ESTAVA EM
# 100% DOS SORTEIOS.
# ---------------------------------------------------------------------------
# Ele vinha DEPOIS do `Comment gelatin,` e era a ultima coisa no ouvido: um
# segundo CTA nu colado no unico pedido que gera receita. A posicao final e' a
# que fica, e ela tem de ser o pedido. ⭐ O follow continua existindo — vai
# ANTES. Ordem nova da cena 2: MECANISMO -> DISCLOSURE -> FOLLOW -> CTA.
# ⛔⛔ E CONTINUA SENDO FRASE SEPARADA, nunca colada no `Comment gelatin,`: a
# automacao de DM casa a palavra EXATA, e follow encostado na keyword faz o
# comentario sair com duas palavras e a automacao nao dispara (lente T16-2).
# ⛔ TODAS COM DUAS PALAVRAS — o contrato orca 3 para o follow, e aqui ele custa
# 2 porque o CTA com cobertura social custa 9. Cobrado no `_contrato_dos_pools`.
# ⚠️ CUSTO DECLARADO: o MOTIVO do gate (`or I can't reach you`, Langer 1978)
# nao cabe mais em 2 palavras e caiu. Recuperar e' encurtar o CTA — e o CTA e'
# quem paga a cobertura social, que o contrato nao deixa negociar. Alcada do Ed.
# ⚠️ Eram 6 entradas, viraram 7, e a conferencia do mesmo dia derrubou
# `Followers only.` e repos `Hit follow.`: sao 7.
# ⛔ CONFERENCIA 2026-08-10 — UMA ENTRADA DERRUBADA:
#
#     ✗ Followers only.
#
# Nao e' um PEDIDO, e' uma CONDICAO — e a condicao que ela impoe e' sobre a
# recompensa que o CTA vai oferecer meio segundo depois. E' o defeito que o CT1
# nomeia (*condicional na recompensa*) reentrando pela porta da frente: ele so'
# nao e' acusado porque mudou de POSICAO, e o CT1 mede posicao. Ouvida uma vez,
# `Followers only.` deixa o espectador decidindo se ele se qualifica, no exato
# segundo em que o video precisa que ele digite. As sete sao verbo no
# imperativo. 7 -> 6 -> 7, e a forma-substantivo virou lente.
FOLLOWS16 = [
    "Follow first.",
    "Follow me.",
    "Follow now.",
    "Follow today.",
    "Just follow.",
    "Follow, please.",
    # ⚠️ REPOSICAO DE PISO (2026-08-10) — verbo no imperativo, duas palavras, e
    # e' como a plataforma fala.
    "Hit follow.",
]


# ---------------------------------------------------------------------------
# SORTEIO
# ---------------------------------------------------------------------------

def _montar_falas(rng, orgaos):
    """As DUAS falas do video, na estrutura travada do CONTRATO DE COPY 16s.

    take 1 = ISCA absurda + DESMENTIDO (A REGRA concreta) + A FALHA DELE
    take 2 = MECANISMO + DISCLOSURE (com `gelatin trick` e razao) + FOLLOW + CTA

    ⛔⛔ A ORDEM DO TAKE 2 MUDOU EM 2026-08-10 e a mudanca e' o CT1: o FOLLOW
    vem ANTES do CTA. Antes ele vinha depois, e a ultima coisa no ouvido —
    colada no unico pedido que gera receita — era um segundo CTA nu. Medido:
    100% dos sorteios.

    ⚠️ O FILTRO E' DE ORCAMENTO, e ele e' de DUAS PONTAS: teto porque estourar e'
    atropelo, piso porque cena curta perde beat. Cada estagio tem fallback MEDIDO
    no self-test, na ordem certa: relaxa-se a guarda de ECO primeiro e o PISO por
    ultimo, porque eco repetido em 8 segundos e' vicio audivel e piso curto e'
    so' AVISO.
    ⭐ Depois da reforma o filtro de orcamento NAO DESCARTA NADA nas duas cenas
    (os pools ja' cabem no pior caso — ver o cabecalho de TETO_FALA). Ele fica
    como rede: quem mexer num pool amanha' descobre pelo [ALCANCE], nao pelo
    render.
    """
    # ----- cena 1 ----------------------------------------------------------
    # ⚠️ `orgaos[0]` e `orgaos[1]` sao O MESMO APELIDO desde a reforma (CT4).
    isca = rng.choice(ISCAS).format(o=orgaos[0])

    def _c1(d, a):
        return "%s %s %s" % (isca, d, a)

    # ⛔ `FALHAS16` no lugar de `ALIANCAS` — CT2. O pool antigo continua no
    # arquivo, aposentado e com o motivo escrito.
    def _op1(piso, sem_eco):
        return [(d, a) for d in DESMENTIDOS for a in FALHAS16
                if (PISO_FALA[1] <= _w(_c1(d, a)) if piso else True)
                and _w(_c1(d, a)) <= TETO_FALA[1]
                and not (sem_eco and (_repete(isca, d) or _repete(isca, a)
                                      or _repete(d, a)))]

    op = (_op1(True, True) or _op1(True, False) or _op1(False, True)
          or _op1(False, False))
    c1 = _c1(*rng.choice(op))

    # ----- cena 2 — ⭐⭐ A FUNDIDA -------------------------------------------
    # Forma aprovada pelo operador (lote 1, 2026-08-08):
    #     {MECANISMO} {DISCLOSURE, com o VINCULO nomeado} {CTA} {FOLLOW}
    # ⚠️ era `{PROVA, com o homem NOMEADO}` ate' 2026-08-09.
    #
    # ⛔⛔ CADA BEAT ORCA CONTRA O MINIMO DOS OUTROS, e o beat sem restricao
    # propria e' escolhido DENTRO do orcamento — nunca antes dele. E' a licao
    # §36, paga tres vezes no mesmo dia (receita 12->55 falas distintas;
    # escandalo e exterior saindo da lista dos que cortam fala).
    # ⚠️ E o contra-exemplo do COLO tambem esta' medido: quando o orcamento e'
    # apertadissimo, esta ordem CONCENTRA o sorteio em vez de espalhar. Por isso
    # o [ALCANCE] do autoteste manda aqui — ele diz quantas entradas de cada
    # eixo NUNCA saem, que e' exatamente o que "cabe no teto" esconde.
    # ⛔ A reserva e' NUMERICA, sem texto de enchimento: comparar contagem de
    # palavras e' o que a regra de fato quer dizer, e string-molde de mentira
    # ja' me fez medir a coisa errada oito vezes hoje.
    def _cabe16(pool, reserva):
        """As entradas que cabem no teto DEPOIS de reservar `reserva` palavras.

        ⚠️ O fallback nao devolve o pool inteiro (isso e' estouro silencioso):
        devolve a entrada mais CURTA, e quem reclama e' o linter.
        """
        def _n(x):
            return _w(x.format(o=orgaos[1]))
        v = [x for x in pool if _n(x) + reserva <= TETO_FALA[2]]
        return v or [min(pool, key=_n)]

    # ⚠️ O `{par}` e' resolvido ANTES de medir: todas as entradas de PARES16 tem
    # duas palavras (contrato), mas medir o molde com `{par}` cru contaria 1 e o
    # orcamento sairia otimista em uma palavra — exatamente o erro de medir a
    # string-molde em vez da string final.
    par = rng.choice(PARES16)
    _disc = [d.format(par=par) for d in DISCLOSURES16]
    _mn_m = min(_w(x.format(o=orgaos[1])) for x in MECANISMOS16)
    _mn_c = min(_w(x) for x in CTAS)
    _mn_f = min(_w(x) for x in FOLLOWS16)

    # ⛔⛔ O DISCLOSURE ESCOLHE PRIMEIRO, E ISSO FOI MEDIDO — nao e' preferencia.
    # Com o MECANISMO na frente (a ordem de 2026-08-08, quando o beat 2 era a
    # PROVA), o [ALCANCE] do sorteio real deu 7 de 9 disclosures vivos, um deles
    # em 0,7% e o mais frequente em 31,8%: os mecanismos vao de 6 a 8 palavras e
    # so' DOIS tem 6, entao disclosure de 9 so' cabia em ~2% dos sorteios.
    # ⭐ O criterio e' o mesmo do FLAGRANTE 16: escolhe primeiro QUEM TEM MENOS
    # SUBSTITUTOS. Os dez mecanismos dizem a MESMA coisa (sangue + pressao +
    # orgao) de dez jeitos; os nove disclosures dizem coisas diferentes (o que
    # funcionou / eu dei / eu achei / consertou). Quem e' intercambiavel absorve
    # a sobra — aqui, o mecanismo.
    # ⚠️ DEPOIS DA REFORMA A ORDEM NAO MUDA MAIS NADA, e isso e' o objetivo: com
    # MECANISMO=6, DISCLOSURE=8, FOLLOW=2 e CTA=8-9, o pior caso soma 25 = teto.
    # Nenhum `_cabe16` descarta entrada nenhuma, e o [ALCANCE] sai 100% nos
    # quatro pools. ⛔ A ordem fica como esta' porque ela e' a correta se alguem
    # alargar um pool amanha': primeiro quem tem MENOS SUBSTITUTOS (o
    # disclosure, que diz coisas diferentes), por ultimo o INTERCAMBIAVEL (o
    # mecanismo, que diz a mesma coisa de onze jeitos).
    disc = rng.choice(_cabe16(_disc, _mn_m + _mn_c + _mn_f))
    mecan = rng.choice(_cabe16(MECANISMOS16, _w(disc) + _mn_c + _mn_f))
    mecan = mecan.format(o=orgaos[1])
    # ⛔⛔ CT1 — O FOLLOW ENTRA ANTES DO CTA. A ultima sentenca do video e' o
    # pedido, sempre. Trocar estas duas linhas de lugar reabre o defeito que
    # estava em 100% dos sorteios.
    # ⛔⛔ CT8 (2026-08-10) — O BEAT DO FOLLOW SAIU DA FALA.
    # Ordem do operador: *"nao acho que deva ter follow me no cta, a
    # mensagem e' enviada independente de seguirem ou nao"*. O gate
    # existia no repo inteiro por uma PREMISSA ERRADA sobre a automacao
    # de DM, e quem opera a automacao corrigiu. As palavras liberadas
    # vao para o mecanismo e a prova.
    cta = rng.choice(_cabe16(CTAS, _w(mecan) + _w(disc)))
    c2 = "%s %s %s" % (mecan, disc, cta)

    return [_pontuar(c1), _pontuar(c2)]


def _orgaos(rng):
    """O apelido do orgao do video — EX14 + CT4.

    ⛔⛔ REVERSAO DECLARADA, 2026-08-10. Ate' aqui esta funcao sorteava DOIS
    apelidos DISTINTOS (`rng.sample(NUCLEO_DIRETO, 2)`) porque "duas mencoes
    iguais em 16 segundos sao bordao". Medido, o efeito era o oposto do
    pretendido: o apelido MUDAVA NO CORTE em 100% dos videos.

    Em 24s e cinco cenas o bordao e' o risco. Em 16s e DUAS cenas o risco e' o
    contrario — o corte zera a memoria de trabalho, e trocar `pecker` por
    `wiener` no segundo 9 obriga o espectador a remapear justamente quando ele
    ja' esta' com um pe' fora. ⭐ A variacao continua existindo ENTRE videos,
    que e' onde ela nunca custou nada: sao 3 apelidos por lote, nao 1.

    ⚠️ O terceiro item continua existindo na tupla e NAO E' EMITIDO em fala
    nenhuma (a cena que o usava caiu na fusao para 16s). Fica porque `sortear`
    e o `resumo_pt` leem a tupla inteira, e porque encurta-la para dois seria
    mudar o contrato de spec de um motor que o app ja' consome.
    """
    um = rng.choice(NUCLEO_DIRETO)
    resto = [n for n in NUCLEO if n != um]
    return [um, um, rng.choice(resto)]


def sortear(pagina, rng, ledger, travas=None):
    """Anti-repeticao por ledger, por pagina.

    ⚠️ Nenhum eixo visual depende de outro neste agente, e isso e' consequencia
    direta da EX11: a varanda e' a mesma nas tres cenas, entao nao ha' o par
    cenario-A/cenario-B para casar; a caixa e' sempre de bicarbonato, entao nao
    ha' contraste de tom para resolver; e nada cresce (EX8), entao nao ha'
    analogia fisica para escolher. Sorteio plano e' o desenho certo aqui — ⛔ nao
    e' esquecimento.
    """
    hist = ledger.get(pagina, {})
    elegiveis = [n for n in NARRADORAS
                 if IDADE_MINIMA_NARRADORA <= n["idade"] <= IDADE_MAXIMA_NARRADORA]
    nar = _evitando(rng, elegiveis, hist.get("narradora", [])[-3:])
    hom = _evitando(rng, HOMENS_SEM_ROSTO, hist.get("homem", [])[-3:])
    var = _evitando(rng, VARANDAS, hist.get("varanda", [])[-2:])
    cx = _evitando(rng, CAIXAS, hist.get("caixa", [])[-2:])
    desp = _evitando(rng, DESPEJOS, hist.get("despejo", [])[-2:])
    rea = _evitando(rng, REACOES, hist.get("reacao", [])[-2:])
    mec = _evitando(rng, MECANISMOS, hist.get("mecanismo", [])[-2:])

    mesa = _evitando(rng, MESAS, hist.get("mesa", [])[-2:])
    orgaos = _orgaos(rng)
    falas = _montar_falas(rng, orgaos)

    return {"pagina": pagina, "narradora": nar, "homem": hom, "varanda": var,
            "mesa": mesa, "caixa": cx, "despejo": desp, "reacao": rea,
            "mecanismo": mec, "orgaos": orgaos, "falas": falas}


# ---------------------------------------------------------------------------
# GERADOR
# ---------------------------------------------------------------------------
# EX17 — formato de entrega, sempre: BLOCO 0 (REF) -> os 3 IMAGE agrupados -> os
# 3 TAKE agrupados. ⛔ Nunca intercalar. Numeracao x/03. Destino: AdBatch
# Vertical 3.

# ⭐⭐ EX14 — A NARRADORA E' SEMPRE LINDA E DE CORPO FITNESS (ordem do
# operador, 2026-08-06): *"o agente exterior short deve gerar somente mulheres
# extremamente lindas e sensuais, com corpos fitness de academia, barriga
# sarada, seios e gluteos duros"*.
# ⚠️ O pool anterior dizia `slim`, `petite`, `lightly toned` — magra, que nao e'
# a mesma coisa que treinada. Os 14 portes foram reescritos com a mesma
# anatomia de frase: SILHUETA -> busto -> abdomen -> gluteo -> pernas.
# ⛔ A ordem das clausulas nao e' estetica: e' o que deixa o filtro do REF
# cortar exatamente o que esta' fora de quadro, sem perder o resto.
# ⛔⛔ NAO EXISTE FRASE DE BELEZA AQUI, E E' DE PROPOSITO. A primeira versao
# desta regra injetava "a strikingly beautiful and sensual woman" no REF — e o
# proprio linter reprovou 420 vezes, porque `beautiful` esta' no
# BANIDOS_DESEJO. Ao ler o EX9 inteiro, a razao fica clara: a regra se chama
# "A LEI DA REF: LINDA E JOVEM" e quer o MESMO resultado que o operador pediu.
# Ela so' diz COMO — *"a atratividade entra por DESCRICAO FISICA CONCRETA"*.
# Os 14 portes fitness SAO essa descricao concreta. O adjetivo seria a versao
# preguicosa da mesma ordem, e a que este agente ja' provou que o gerador
# recusa. ⛔ Nao reintroduzir: mexer aqui e' reabrir 420 reprovacoes.

# ⛔ FORA DE QUADRO NAO SE DESCREVE. O REF e' `chest up`: pedir abdomen,
# cintura, gluteo ou perna numa foto cortada no peito e' ordem contraditoria, e
# o gerador "resolve" contradicao do jeito errado. E' a mesma licao do CL24 do
# CLEAN, que custou uma rodada de REFs erradas para ser aprendida.
_FORA_DO_PEITO = ("stomach", "abs", "belly", "waist", "midsection",
                  "glute", "hip", "leg")


def _porte_ref(porte):
    """O porte SEM o que o `chest up` nao mostra. Silhueta e busto ficam."""
    return ", ".join(c for c in porte.split(", ")
                     if not any(t in c.lower() for t in _FORA_DO_PEITO))


def _descricao_dela(p, so_peito=False):
    """A narradora em UMA oracao, com os eixos que a fazem ser OUTRA pessoa.

    ⚠️ Dez pessoas descritas so' por cabelo sao a MESMA pessoa dez vezes, e o
    gerador devolve o mesmo rosto (licoes-de-construcao §15). Por isso o porte
    entra sempre, e os oculos entram quando existem.
    ⛔ Zero adjetivo de etnia aqui: quem injeta e' a montagem, por pagina (EX10).
    """
    partes = [p["cabelo"]]
    if p.get("oculos"):
        partes.append(p["oculos"])
    partes.append(p["rosto"])
    marca = ", ".join(partes[:-1]) + " and " + partes[-1]
    # ⭐ EX14: no REF entra so' o que cabe no `chest up` (ver _porte_ref)
    porte = _porte_ref(p["porte"]) if so_peito else p["porte"]
    return "%s, with %s" % (porte, marca)


def _descricao_dele(p):
    """O homem SEM ROSTO em uma oracao — EX5.

    ⛔ Zero cabelo, zero pelo facial, zero oculos: nada disso esta' em quadro. O
    que o espectador ve' e' porte, camiseta, antebraco e a marca da pele.
    """
    return "%s, in %s, with %s and %s" % (p["porte"], p["roupa"], p["pele"],
                                          p["marca"])


def montar(spec):
    et = ETNIA[spec["pagina"]]
    nar, hom, var = spec["narradora"], spec["homem"], spec["varanda"]
    # ⚠️  NAO e desempacotada aqui: a mesa de ferro so aparecia na
    # IMAGE 02/03 do motor de 24s, que e o quadro que caiu na fusao. O eixo
    # continua SORTEADO e no ledger (o painel o trava, e ele governa o
    # cenario da varanda), mas nenhum bloco o imprime.
    cx, desp = spec["caixa"], spec["despejo"]
    rea, mec, falas = spec["reacao"], spec["mecanismo"], spec["falas"]
    # ⚠️ O PONTO FINAL E' DO MOTOR, nao do pool: as entradas de `luz` nascem sem
    # pontuacao (elas tambem entram no meio de oracao), e sem isto a cauda
    # colava na luz — "flat shaded daylight under the awning Shot on iPhone".
    luz = _maiuscula(var["luz"]) + "."
    # ⛔ O RECIPIENTE E' SLOT EM TRES LUGARES (marca legivel, gesto do despejo no
    # IMAGE e no TAKE) porque 7 das 12 CAIXAS nao sao caixa. ⚠️ `%` sobre string
    # sem `%s` e' no-op, entao as entradas de DESPEJOS que nao nomeiam o
    # recipiente passam intactas — ⛔ nao se poe slot por simetria.
    rec = cx["recipiente"]
    marca = EX_MARCA_LEGIVEL % rec
    desp_img, desp_take = _slot(desp["img"], rec), _slot(desp["take"], rec)
    # ⚠️ A travada do PLANTADO ja' traz o artigo ("standing on the %s"), entao o
    # slot entra NU — senao sai "on the the side table".

    # ⚠️ A ANCORA DE CONTINUIDADE E' INVERTIDA (EX11/TR18): quem repete rosto e'
    # ELA, e a descricao volta INTEIRA, com a marca facial, nunca em ancora curta.
    # `same hair` carrega a roupa e PERDE O ROSTO — foi assim que o VAZAMENTO
    # devolveu um senhor de oculos e bigode no lugar do corpo-prova, e como o TAKE
    # dizia "only he speaks", o estranho falava a fala do REF.
    # ⚠️ Ele nao pede ancora de rosto porque nao tem rosto: o que se re-ancora
    # dele e' a roupa, o porte e o corte no peito.
    ela = ("a %d-year-old %s woman, %s, wearing %s"
           % (nar["idade"], et, _descricao_dela(nar), nar["roupa"]))
    mesma = ("The same %d-year-old %s woman, %s, wearing %s"
             % (nar["idade"], et, _descricao_dela(nar), nar["roupa"]))
    ele = "a %d-year-old %s man, %s" % (hom["idade"], et, _descricao_dele(hom))
    mesmo = ("the same %d-year-old %s man, %s"
             % (hom["idade"], et, _descricao_dele(hom)))

    b = {}

    # --- BLOCO 0 (REF) ------------------------------------------------------
    # ⭐ UMA foto so', a dela. Ele nao tem rosto, logo nao tem REF — e' a economia
    # inteira do angulo virando uma linha de prompt A MENOS (EX5).
    b["BLOCO 0 (REF)"] = (
        "REF 01: Photo of a real person, a %d-year-old %s woman, chest up, "
        "facing the camera directly, calm steady expression. %s. Wearing %s. "
        "Plain neutral gray background, soft even frontal light. No subtitles, "
        "no captions, no burned-in text, no watermark."
        % (nar["idade"], et, _maiuscula(_descricao_dela(nar, so_peito=True)),
           nar["roupa"])
    )

    # --- IMAGE 01/03 — ⭐⭐ A GEOMETRIA TRAVADA (EX4) ------------------------
    # ⛔ O po' JA' ESTA' no prop no frame 0 — a mesma economia do TR4/TROCA: nao
    # ha' frame de "antes", o video abre com o despejo em andamento.
    # ⛔ Zero plateia (EX11): plateia e' ESCANDALO/FLAGRANTE, e e' um dos quatro
    # ingredientes da composicao que produziu as recusas deterministicas de
    # 2026-07-30.
    # ⛔ EX_CAIXA_FORMA entra logo depois da geometria, onde a caixa acabou de
    # ser nomeada: e' o bloco em que ela esta' NA MAO e despejando, o mesmo em
    # que o operador viu o cilindro.
    b["IMAGE 01/02"] = (
        "IMAGE 01/02: Medium shot on %s. %s %s %s %s She is looking down at the "
        "powder, not at the lens. They are the only two people in the frame. "
        "%s %s %s"
        % (var["set"],
           EX_GEOMETRIA_IMAGE % (ela, cx["caixa"], desp_img, ele),
           EX_CAIXA_FORMA,
           EX_VARANDA_TRAVADA, EX_BLINDAGEM_FORMA, marca,
           luz, CAUDA)
    )

    # --- IMAGE 02/03 — A REGRA, ELA SOZINHA ---------------------------------
    # ⚠️ `re_ancora` no lugar de "on the same porch": sem ele metade do lote perde
    # o cenario E a bandeira dos EUA a partir da cena 2.
    # ⭐ A PROVA DO TRUQUE FICA NO QUADRO enquanto a fala o demole: o geoduck
    # empoeirado e a caixa continuam a' vista, na mesa, e ela nao os toca. E' o
    # recibo mudo da cena que acabou de passar.
    # ⚠️ E o mecanismo ja' esta' PLANTADO aqui, no frame 1 (TR1/ES9): o reveal da
    # cena 3 nao apresenta nada novo.
    # ⚠️ A TABUA DE MADEIRA NAO E' ENFEITE: as travadas do `pousado` (copia
    # literal do RESSURREICAO) dizem "lying on the board beside it", e sem uma
    # tabua em quadro esse "the board" nao tem referente — o Veo resolve
    # inventando. E' o mesmo motivo pelo qual o RESSURREICAO poe o mecanismo
    # "on a wooden board" na bancada. ⛔ Quem tirar a tabua quebra as 12 entradas
    # de MECANISMOS de uma vez.
    # ⚠️ A PRIMEIRA MENCAO DA MESA E' A DESCRICAO INTEIRA (`mesa["mesa"]`), as
    # seguintes sao o rotulo curto. ⛔ O campo `mesa` era CAMPO MORTO — 0 de 400
    # videos o emitiam, e o bloco abria com `stands behind the crate` / `the
    # spool table` / `the shelf board`, artigo definido para um objeto que o
    # prompt nunca introduzia (o Veo inventa a forma). E a divergencia 3 da
    # docstring justifica a ausencia do eixo `AMBIENTES_B` dizendo que a entropia
    # "foi para o eixo MESAS": a CONTAGEM estava preservada, a CARGA VISUAL nao
    # chegava ao prompt (licoes-de-construcao §15/§16 — otimizar contra a metrica).
    # --- IMAGE 02/02 — ⭐⭐ A CENA FUNDIDA -----------------------------------
    # ⛔⛔ ESTE QUADRO E' O DA CENA 3 DO MOTOR DE 24s, SEM UMA ALTERACAO.
    # A cena 2 de la' (ela sozinha atras da mesa de ferro, com o geoduck e a
    # caixa deitados lado a lado) nao entra aqui como IMAGEM — o geoduck
    # esta' na mesa la' e nas MAOS DELE aqui, e juntar poe dois geoducks no
    # mesmo quadro. E' o defeito que a T16-1 do TRIO 16 existe para pegar.
    # ⚠️ E a outra metade da licao, tambem paga no TRIO 16: quadro entulhado
    # o Veo resolve APAGANDO alguem, e quem ele apaga e' o corpo-prova.
    # ⭐ A REGRA da cena 2 sobrevive na FALA, nao no quadro — e' a regra da
    # familia 16s: a copy fundida carrega obrigatoriamente o mecanismo do
    # angulo e o literal `gelatin trick`, porque as cenas que os traziam sao
    # justamente as que caem.
    # ⛔ Ele volta pelo MESMO corte no peito (EX5): coerencia de continuidade, e
    # um rosto a menos para manter identico.
    # ⭐ ES9: o objeto da keyword esta' na mao livre dela no frame em que a boca
    # diz `gelatin,` — e ele estava plantado na mesa desde o frame 1 da cena 2.
    # ⛔ SEM a caixa em quadro: o bloco do CTA e' o mais arriscado do lote e
    # densidade e' superficie de bloqueio (F12c). O geoduck volta LIMPO.
    b["IMAGE 02/02"] = (
        "IMAGE 02/02: Medium shot on %s, same light. %s, stands frame-left, "
        "talking straight to camera. Standing frame-right, cropped at the "
        "chest so that no face is in the frame, is %s; both of his hands are "
        "closed around the shell of the same whole geoduck clam, one above the "
        "other, holding it upright with the siphon pointing straight up, and "
        "the powder is gone from it now. %s They are the only two people in "
        "the frame. %s %s %s"
        % (var["re_ancora"], mesma, mesmo,
           EX_KEYWORD_NA_MAO_IMAGE % mec["curto"],
           EX_BLINDAGEM_FORMA, luz, CAUDA)
    )

    # --- TAKE 01/03 — O DESPEJO EM ANDAMENTO --------------------------------
    # ⛔ Nada cresce (EX8): nao ha' uma unica batida de transformacao neste bloco,
    # e e' isso que separa este agente do RESSURREICAO. La' o crescimento e' o bit
    # visual; aqui A AUSENCIA DELE E' O ARGUMENTO.
    # ⛔ E zero declaracao de estado de movimento (EX7): o prop nao e' declarado
    # imovel, por ordem do operador. O que segura a leitura e' a BLINDAGEM DE
    # FORMA, que e' negacao de forma e nao de movimento.
    b["TAKE 01/02"] = (
        "TAKE 01/02: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway, no cuts, and the camera does not tilt or "
        "pan. The pour runs the whole shot: the stream of white powder keeps "
        "falling in the same diagonal from the mouth of the %s onto the "
        "siphon of the pale tan shellfish, and the powder on it spreads a "
        "little wider on the shell below. %s %s She starts with her eyes down "
        "on the powder and brings them up to the lens as she talks, and %s. "
        "%s %s\n"
        "Dialogue: \"%s\"\n"
        "Audio: dry powder hissing onto shell and boards, a screen door "
        "settling somewhere behind, quiet outdoor room tone on %s. No music."
        # ⚠️ `recipiente` e nao "box": a caixa pode ser lata, saco ou pouch, e
        # mandar despejar "da boca da caixa" numa imagem que tem uma lata e'
        # contradicao dentro do proprio bloco.
        % (rec, desp_take, EX_SEM_ROSTO_TAKE, rea["desc"],
           EX_BLINDAGEM_FORMA, marca, sonorizar(falas[0]),
           var["curto"])
    )

    # --- TAKE 02/03 — ⭐⭐ A REGRA -------------------------------------------
    # ⛔ Ela sozinha, e SO' ELA TEM Dialogue nas tres cenas (EX11): o dialogo do
    # Veo e' monofonico na pratica e duas vozes saem tortas.
    # --- TAKE 02/02 — A REGRA, A PROVA E O CTA ------------------------------
    # ⛔ Ele e' MUDO e continua sem rosto (EX5). Ela pede o comentario olhando na
    # lente — `follow me first` e' um pedido, e pedido sem cara nao converte.
    b["TAKE 02/02"] = (
        "TAKE 02/02: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway, no cuts, and the camera does not tilt or "
        "pan. %s %s She speaks straight into the lens, calm and even, no rush. "
        "%s\n"
        "Dialogue: \"%s\"\n"
        "Audio: quiet outdoor room tone on %s, a little wind in the trees. No "
        "music."
        # ⚠️ `falas[1]`, a SEGUNDA e ultima. Com duas cenas o indice 2 nao
        # existe mais — e um IndexError aqui so' apareceria no lote.
        % (EX_SEM_ROSTO_TAKE, EX_KEYWORD_NA_MAO_TAKE, EX_BLINDAGEM_FORMA,
           sonorizar(falas[1]), var["curto"])
    )

    # ⛔ EX17 — a trava de texto queimado em todo TAKE. Zero de 18 TAKEs a tinham
    # quando o buraco foi achado, e texto vindo do gerador entra por cima da nossa
    # legenda (que nasce depois, no Editor, do Whisper) e nao sai.
    return sc.selar_takes(b)


# ---------------------------------------------------------------------------
# LINTER — as regras EX
# ---------------------------------------------------------------------------
# ⚠️ A NUMERACAO E' A MESMA DA DOUTRINA, caractere por caractere: as regras deste
# agente sao EX1-EX17 no `AGENTE_ED_EXTERIOR_V1.md`, e toda mensagem de erro cita
# a EX que ela cobra. Regra citada em codigo e ausente da doutrina manda o
# operador ler a regra errada (licoes-de-construcao §3) — foi o que aconteceu no
# TROCA, cujo motor citava TR15-TR21 quando a doutrina ia ate' a TR14.
#
#   EX2  A REGRA na cena 2          EX10 zero etnia no pool + injecao na montagem
#   EX3  o batismo na cena 3        EX11 elenco 2/1/2, varanda unica E o
#   EX4  a geometria travada             mecanismo plantado desde o frame 1 (ES9)
#   EX5  o homem sem rosto          EX12 piso por cena (AVISO)
#   EX6  a marca legivel            EX13 CTA/gate literais (delegado — ver `lint`)
#   EX7  blindagem/movimento/lexico EX14 `your <nucleo>` e substantivos distintos
#   EX8  nada cresce                EX17 a cauda dos IMAGE
#   EX9  figurino sem desejo + faixa de idade
#
# ⚠️ TODA comparacao com travada e' contra o MIOLO INVARIANTE (o trecho entre os
# `%s`), NUNCA contra o template cru: `TRAVADA not in bloco` da' 100% de falso
# positivo quando a travada chega formatada, e regra que reprova tudo nunca foi
# testada (licoes-de-construcao §2).

# ---------------------------------------------------------------------------
# ⭐⭐ A REGRA (EX2), verificavel por regex.
# ---------------------------------------------------------------------------
# O invariante e' `inside` MAIS um dos dois eixos que a fonte opoe a ele: o
# LUGAR (`outside`) ou o GESTO (`pour`). Nas 9 entradas do pool, as duas formas
# aparecem — sete opoem lugar, e a que parte a frase em duas
# (`What's happening is on the inside. Nothing you pour changes that.`) opoe o
# gesto.
# ⛔⛔ A PRIMEIRA VERSAO EXIGIA `pour ... on` NA FORMA ALTERNATIVA e reprovou 59
# de 400 sorteios: nessa entrada o `pour` nao rege preposicao nenhuma. Regra que
# reprova a copy CERTA e' o mesmo defeito da §2 das licoes visto do outro lado —
# nao adianta o linter existir se ele cobra uma forma de dizer em vez do
# argumento.
_RX_INSIDE = re.compile(r"\binside\b", re.I)
_RX_OPOSTO = re.compile(r"\boutside\b|\bpour\w*\b", re.I)

# ⭐ CONTROLES: a esquerda TEM de passar, a direita TEM de ser acusada.
CONTROLE_REGRA = (
    [u"Nothing you pour on the outside changes what's happening on the inside.",
     u"What's happening is on the inside. Nothing you pour changes that.",
     u"Nothing you pour on it changes what's happening inside.",
     u"Outside changes nothing. What's happening is on the inside."],
    [u"Getting firm is blood coming in with pressure.",
     u"What makes your Johnson actually respond is one thing, circulation.",
     u"Comment gelatin, and I'll send you exactly what it is."],
)


def _tem_regra(txt):
    """A fala carrega A REGRA? `inside` + (o lugar `outside` OU o gesto `pour`)."""
    return bool(_RX_INSIDE.search(txt) and _RX_OPOSTO.search(txt))

# ⛔ MIOLOS INVARIANTES, nunca a constante inteira.
# ⛔⛔ SAO SETE, UM POR ELEMENTO DA TABELA DO §2 DO MAPA, e eram TRES ate'
# 2026-08-03. Os quatro que faltavam foram sabotados um a um e TODOS passaram em
# silencio: trocar `frame-left` por `frame-right` nela, `left hand` por `right
# hand` na caixa, `frame-right` por `frame-left` nele e apagar o po' ja' acumulado
# no sifao. ⛔ Esquerda e direita sao justamente os dois elementos que o mapa
# grifa em negrito e que o checklist da doutrina chama de "a geometria do hook
# esta' inteira" — linter que cobra 3 de 7 nao cobra a geometria, cobra um pedaco
# dela (licoes-de-construcao §15: verificar a FORMA e nao a FUNCAO).
M_GEOMETRIA = ("Standing frame-left, turned three-quarters towards the middle",
               "In her left hand, raised to the height of her own chest",
               "tipped mouth-down at about forty-five degrees",
               "standing upright with the siphon pointing straight up",
               "white powder has already settled over the top third of the "
               "siphon",
               "Standing frame-right, cropped at the chest",
               "both of his hands are closed around the shell, one above the "
               "other")
M_VARANDA = "a United States flag hangs from the post at frame-right"
M_SEM_ROSTO_IMAGE = "cropped at the chest so that no face is in the frame"
M_SEM_ROSTO_TAKE = "the camera never tilts up to his face"
M_KEYWORD = ("In her own free left hand, raised to the height of her chest "
             "and held level")
M_PLANTADO = "has been standing on the"

# ---------------------------------------------------------------------------
# EX10 — O QUE NAO PODE EXISTIR DENTRO DE UM POOL DE PESSOA
# ---------------------------------------------------------------------------
# ⚠️ Cobra-se o POOL, nao o bloco montado: no bloco a etnia esta' la' de
# proposito, injetada por pagina.
#
# ⛔⛔ A PRIMEIRA VERSAO DESTE LINTER ERA UMA MAQUINA DE FALSO POSITIVO, e o
# registro fica porque o modo de falha e' o §16 das licoes em estado puro: ela
# casava os tokens NUS `white` e `black`, e reprovou 418 de 400 sorteios em cima
# de `a white ribbed tank top`, `a plain black t-shirt` e `long jet-black hair`.
# COR DE ROUPA NAO E' ETNIA — e' exatamente por isso que `olive` e `fair` sairam
# do eixo `pele` do `medir_personagens.py`. Linter que reprova o que esta' certo
# nunca foi testado (licoes-de-construcao §2).
#
# Sao DUAS familias, e elas falham de jeitos diferentes:
#   EXPLICITA — a etnia dita com todas as letras. Regex, porque ela so' e' etnia
#               quando qualifica UMA PESSOA ou a PELE (`Black American woman`,
#               `pale-skinned`), nunca quando qualifica um tecido.
#   IMPLICITA — a etnia que entra POR DENTRO do cabelo, da pele ou do olho.
#               `a full soft afro`, `waist-length box braids`, `a long
#               twist-out`, `honey-blonde`, `green eyes`, `pale forearms` nao
#               dizem a palavra e mesmo assim travam a entrada numa etnia so'.
#               ⛔ E' esta familia que quebra o modelo do NECROSE em silencio:
#               num pool unico, uma entrada tem de servir pagina branca E negra.
ETNIA_EXPLICITA = re.compile(
    r"\b(white|black|pale|fair|dark|olive|brown|light)[- ]skinned\b"
    r"|\b(white|black|asian|hispanic|latina|latino|caucasian|african|"
    r"american|ebony|mixed-race)\s+"
    r"(american|woman|women|man|men|skin|guy|male|female|features)\b"
    r"|\b(asian|hispanic|latina|latino|caucasian|afro-american|"
    r"african-american)\b", re.I)

ETNIA_IMPLICITA = ("afro", "box braid", "twist-out", "twist out", "cornrow",
                   "dreadlock", "locs", "kinky", "blonde", "blond", "auburn",
                   "ginger", "redhead", "copper-red", "blue eyes",
                   "green eyes", "grey eyes", "gray eyes", "hazel eyes",
                   "pale forearms", "pale skin", "freckled forearms")

# ⭐ CONTROLES DO PROPRIO LINTER (o medidor tambem mente — §16). Cada frase da
# esquerda TEM de ser acusada; cada frase da direita NAO pode ser. As negativas
# sao os falsos positivos REAIS que este linter ja' produziu.
CONTROLE_ETNIA = (
    [u"a 30-year-old Black American woman", u"pale-skinned forearms",
     u"a full soft afro worn wide and loose", u"waist-length box braids",
     u"long honey-blonde waves", u"clear blue eyes", u"a long twist-out",
     u"pale forearms with sun-spotted skin"],
    [u"a white ribbed tank top", u"a plain black t-shirt",
     u"long jet-black hair worn straight and glossy",
     u"a blue-and-white striped short-sleeve shirt",
     u"a red-and-black plaid flannel shirt", u"large dark eyes",
     u"smooth-skinned forearms with a sharp tan line",
     u"a bleached-platinum bob cut sharp at the jaw"],
)


def _etnia_no_pool(txt):
    """Os achados de etnia num texto de POOL — as duas familias juntas."""
    achado = [m.group(0) for m in ETNIA_EXPLICITA.finditer(txt)]
    baixo = txt.lower()
    achado += [t for t in ETNIA_IMPLICITA if t in baixo]
    return sorted(set(achado))


def _direcao(txt):
    """So' a direcao de cena — a fala nunca entra na varredura de token.

    ⛔ E' aqui que `swell up` sobrevive: ele mora na fala da cena 1 (EX1) e e'
    legitimo. Varrer o bloco inteiro reprovaria 100% dos lotes pela EX8.
    """
    return txt.split("\nDialogue:")[0]


def _ex2_regra(spec, blocos, achados):
    """⭐⭐ EX2 no formato de 16s — o MECANISMO no lugar da REGRA literal.

    ⛔⛔ A REGRA LITERAL (`inside` oposto a `outside`/`pour`) NAO ESTA' MAIS NA
    FALA, e isso e' decisao do operador, nao minha. Ele leu os tres lotes de
    copy da cena fundida em 2026-08-08 e reprovou justamente a forma que a
    trazia:

        *"The outside changes nothing"* — **"Outside de quÊ?"**
        *"Essa frase esta' muito vaga e ocupando tempo precioso"*

    Num take de 25 palavras, quatro delas gastas numa abstracao que nao nomeia
    nada e' o desperdicio que ele apontou. A REGRA sobrevive onde ela ja' era
    concreta: na CENA 1, onde a isca nomeia `baking soda` e o desmentido a
    demole.

    ⭐ MAS A LENTE NAO MORRE — ela passa a cobrar o HERDEIRO FUNCIONAL. O que a
    REGRA existia para entregar era *"o que resolve nao esta' do lado de fora"*,
    e quem diz isso agora e' o MECANISMO: sangue chegando com pressao, DENTRO do
    orgao nomeado. Lente que perde o alvo tem de mudar de pergunta ou morrer —
    o que ela nao pode e' continuar cobrando um endereco vazio.
    """
    fala = spec["falas"][1]
    if not re.search(r"\bblood\b", fala, re.I) or \
            not re.search(r"\bpressure\b", fala, re.I):
        achados.append(("ERRO", "EX2/16: a cena fundida nao carrega o MECANISMO "
                                "— sem `blood` E `pressure` na mesma fala, o "
                                "agente perde a unica peca que nenhum outro "
                                "nosso tem e vira isca absurda generica"))
    if not any(n in fala for n in NUCLEO):
        achados.append(("ERRO", "EX2/16: a cena fundida nao nomeia o orgao — "
                                "mecanismo sem destino e' `algo melhora la' "
                                "dentro`, que e' o drifting que o operador "
                                "reprovou em 2026-08-08"))


def _ex3_batismo(spec, blocos, achados):
    """EX3 — o batismo do `gelatin trick` mora na CENA 3, e a divergencia do
    padrao SHORT e' declarada.

    Na fonte o ingrediente so' aparece em 21s de 30 — no ultimo terco, DEPOIS do
    problema. Subir o batismo para a cena 2 gasta a curiosidade 8 segundos cedo,
    deixa a cena 3 com nada alem do CTA e ainda empilha duas coisas grandes nas
    32 palavras que ja' sao da REGRA.
    """
    # ⚠️ INDICE 1, a ULTIMA das duas. O batismo continua no ULTIMO terco do
    # video, que e' o que a fonte faz — o que mudou foi o numero de tercos.
    if "gelatin trick" not in spec["falas"][1]:
        achados.append(("ERRO", "EX3: a cena fundida nao batiza o `gelatin "
                                "trick` — na fonte o ingrediente e' nomeado no "
                                "ultimo terco, depois do problema"))
    if "gelatin trick" in spec["falas"][0]:
        achados.append(("ERRO", "EX3: o `gelatin trick` subiu para a cena 2, "
                                "que ja' tem dono (A REGRA, EX2) — e gasta a "
                                "curiosidade 8 segundos cedo"))


def _ex4_geometria(spec, blocos, achados):
    """⛔⛔ EX4 — a geometria do hook e' travada elemento por elemento. E' o gesto
    de dois que justifica o decimo agente."""
    falta = _faltam(blocos["IMAGE 01/02"], M_GEOMETRIA)
    if falta:
        achados.append(("ERRO", "EX4: IMAGE 01/03 sem elemento(s) travado(s) da "
                                "geometria do frame 0: %s" % falta))
    if M_VARANDA not in blocos["IMAGE 01/02"]:
        achados.append(("ERRO", "EX4: IMAGE 01/03 sem a varanda travada — "
                                "cadeiras de balanco, guarda-corpo branco, "
                                "bandeira dos EUA e deck de madeira"))


def _ex5_sem_rosto(spec, blocos, achados):
    """⭐ EX5 — um rosto a menos para manter identico entre tres blocos de 8s
    gerados separadamente. ⛔ NUNCA por o rosto dele em quadro, nem na cena 3."""
    for nome in ("IMAGE 01/02", "IMAGE 02/02"):
        if M_SEM_ROSTO_IMAGE not in blocos[nome]:
            achados.append(("ERRO", "EX5: %s desenha o homem sem o corte no "
                                    "peito — o rosto dele entra em quadro e "
                                    "passa a ter de ser mantido identico entre "
                                    "os blocos" % nome))
    for nome in ("TAKE 01/02", "TAKE 02/02"):
        if M_SEM_ROSTO_TAKE not in blocos[nome]:
            achados.append(("ERRO", "EX5: %s sem a trava de camera — sem ela o "
                                    "Veo panoramiza para cima e o rosto entra "
                                    "no segundo 3" % nome))


def _ex6_marca(spec, blocos, achados):
    """⛔ EX6 — a marca e' real e legivel, e a P12 esta' revogada NESTE agente.

    ⚠️ A cobranca e' dos DOIS lados: a travada tem de estar onde a caixa aparece,
    e a frase da P12 nao pode aparecer em lugar nenhum. So' o primeiro lado
    deixaria alguem escrever as duas e o prompt se contradizer sozinho.
    """
    # ⛔ M_MARCA, nao EX_MARCA_LEGIVEL: a travada ganhou slot em 2026-08-03 e
    # comparar com o template cru daria 100% de falso positivo (licoes §2).
    for nome in ("IMAGE 01/02", "TAKE 01/02"):
        if M_MARCA not in blocos[nome]:
            achados.append(("ERRO", "EX6: %s sem a trava de marca legivel — o "
                                    "rotulo laranja e' o que faz 'bicarbonato' "
                                    "ser lido em 0,2s sem uma palavra" % nome))
    for nome in sorted(blocos):
        if FRASE_SEM_MARCA_PROIBIDA in blocos[nome]:
            achados.append(("ERRO", "EX6: %s traz a frase da P12 (%r) — ela "
                                    "contradiz frontalmente a ordem do operador "
                                    "de manter a marca real"
                            % (nome, FRASE_SEM_MARCA_PROIBIDA)))
    if "baking soda" not in blocos["IMAGE 01/02"]:
        achados.append(("ERRO", "EX6: IMAGE 01/03 nao nomeia o bicarbonato na "
                                "embalagem — a boca diz `baking soda` e imagem "
                                "que contradiz a boca queima o take"))

    # ⛔⛔ EX6b — A EMBALAGEM E' CAIXA DE PAPELAO, SEMPRE (ordem do operador,
    # 2026-08-03, depois de receber um render com pote cilindrico).
    # Cobrado nos DOIS lados, como o resto do EX6: a blindagem de forma tem de
    # estar onde a caixa aparece, e nenhum bloco pode nomear uma forma que nao
    # e' caixa. So' o primeiro lado deixaria alguem reabrir o pool amanha' com
    # uma lata e o linter continuaria verde.
    # ⛔ SO' A CENA 1. No motor de 24s a caixa aparecia tambem na cena 2
    # (deitada na mesa de ferro); aqui a cena fundida herdou o quadro da
    # cena 3, que e' DELIBERADAMENTE sem a caixa — o bloco do CTA e' o mais
    # arriscado do lote e densidade e' superficie de bloqueio (F12c).
    # ⚠️ Cobrar a blindagem num bloco que nao tem a caixa reprovaria 100%
    # dos lotes por uma regra que nao se aplica.
    for nome in ("IMAGE 01/02",):
        if M_CAIXA_FORMA not in blocos[nome]:
            achados.append(("ERRO", "EX6b: %s sem a blindagem de forma da caixa "
                                    "— `box` sozinho ja' devolveu cilindro no "
                                    "render" % nome))
    # ⚠️ Varre o texto da CAIXA, nao o bloco inteiro: a propria EX_CAIXA_FORMA
    # diz `not a cylinder, not a tin...`, e varrer o bloco acusaria a blindagem
    # de ser o defeito que ela conserta (licoes §2 — o linter que se
    # auto-reprova). O `recipiente` entra junto porque e' ele que vira `the %s`
    # no jorro do TAKE 01.
    proibidas = ("cylinder", "cylindrical", "canister", "tub", "tin", "jar",
                 "bottle", "pouch", "bag", "shaker", "carton", "package")
    txt_caixa = spec["caixa"]["caixa"].lower()
    for forma in proibidas:
        if re.search(r"\b%s\b" % forma, txt_caixa):
            achados.append(("ERRO", "EX6b: a CAIXA %s e' `%s` — a embalagem tem "
                                    "de ser a caixa de papelao classica"
                            % (spec["caixa"]["id"], forma)))
    if spec["caixa"]["recipiente"] != "box":
        achados.append(("ERRO", "EX6b: o `recipiente` da CAIXA %s e' %r — o "
                                "slot vira `the %s` no jorro do TAKE 01 e "
                                "contradiria a imagem"
                        % (spec["caixa"]["id"], spec["caixa"]["recipiente"],
                           spec["caixa"]["recipiente"])))


def _ex7_blindagem(spec, blocos, achados):
    """⛔ EX7 — a blindagem de FORMA em todo bloco que desenha o prop.

    ⚠️ Isto NAO e' moderacao: e' o modo de falha documentado do geoduck, que vira
    PATO no TAKE. Pago em render, registrado no `licoes-producao-veo`.
    """
    for nome in sorted(blocos):
        if nome.startswith("BLOCO"):
            continue
        if EX_BLINDAGEM_FORMA not in blocos[nome]:
            achados.append(("ERRO", "EX7: %s sem a blindagem de forma do "
                                    "geoduck — sem ela o prop vira pato no "
                                    "TAKE" % nome))


def _ex7_movimento(spec, blocos, achados):
    """⛔ EX7 — ZERO declaracao de estado de movimento, por ordem do operador.

    Os outros nove motores declaram o prop imovel (`completely motionless for
    the entire shot`). Aqui isso saiu. ⛔ Sem este linter, a primeira pessoa que
    "consertar" o motor copiando a travada de imobilidade do RESSURREICAO quebra
    a ordem em silencio — e o silencio e' o problema, nao o texto.
    """
    for nome in sorted(blocos):
        direcao = _direcao(blocos[nome]).lower()
        achado = [t for t in EX_MOVIMENTO_PROIBIDO if t in direcao]
        if achado:
            achados.append(("ERRO", "EX7: %s declara estado de movimento %s — "
                                    "proibido neste agente por ordem do "
                                    "operador (2026-08-03); a blindagem de "
                                    "FORMA fica, a de MOVIMENTO nao"
                            % (nome, achado)))


def _ex7_lexico(spec, blocos, achados):
    """EX7 — `geoduck` so' no IMAGE; no TAKE, `the clam`/`the pale tan
    shellfish`. ⛔ E `neck` nunca: a peca e' o `siphon`.

    ⚠️ A metade do `geoduck` e' redundante com a BANIDOS_TAKE de proposito: a
    tabela pega o token e esta funcao explica POR QUE, com o nome da regra. Uma
    mensagem de tabela diz "contem X"; esta diz o que quebra.
    """
    for nome in sorted(blocos):
        if not nome.startswith("TAKE"):
            continue
        if re.search(r"\bgeoduck\b", _direcao(blocos[nome]), re.I):
            achados.append(("ERRO", "EX7: %s nomeia a especie — no TAKE o "
                                    "modelo busca o BICHO no treino, e o bicho "
                                    "vem com cabeca" % nome))
    for nome in sorted(blocos):
        if re.search(r"\bneck\b", _direcao(blocos[nome]), re.I):
            achados.append(("ERRO", "EX7: %s diz `neck` — a peca do geoduck e' "
                                    "o `siphon`, e `neck` puxa pescoco de ave"
                            % nome))


def _ex8_nada_cresce(spec, blocos, achados):
    """⛔⛔ EX8 — neste agente NADA cresce, e este e' o primeiro motor do repo que
    pode chamar `lint_nada_cresce` com `excecao=()`.

    Se o prop crescer na tela, A REGRA (EX2) passa a contradizer a imagem e o
    agente inteiro desaba: ela nao vende o bicarbonato, ela vende o argumento que
    o destroi. ⚠️ A varredura e' so' da DIRECAO de cena — `swell up` mora na fala
    da cena 1 e e' legitimo (EX1).
    """
    sc.lint_nada_cresce(blocos, achados, excecao=(), rotulo="EX8")


def _ex9_ref(spec, blocos, achados):
    """⭐ EX9 — a lei da REF: 28-34, atratividade por DESCRICAO FISICA CONCRETA.

    ⛔ Zero adjetivo de desejo no prompt: o que se escreve e' cabelo, porte,
    traco. Declaracao de desejo nao desarma nada e ainda planta a palavra.
    """
    idade = spec["narradora"]["idade"]
    if not IDADE_MINIMA_NARRADORA <= idade <= IDADE_MAXIMA_NARRADORA:
        achados.append(("ERRO", "EX9: narradora com %d anos, fora da faixa "
                                "%d-%d da lei da REF"
                        % (idade, IDADE_MINIMA_NARRADORA,
                           IDADE_MAXIMA_NARRADORA)))
    for nome in sorted(blocos):
        achado = _achar(blocos[nome], BANIDOS_DESEJO)
        if achado:
            achados.append(("ERRO", "EX9: %s tem vocabulario de desejo %s — a "
                                    "roupa entra como PECA descrita"
                            % (nome, achado)))


def _ex10_etnia(spec, blocos, achados):
    """⭐ EX10 — pool unico, zero etnia nas entradas, injecao na montagem.

    ⚠️ A cobranca e' NOS DOIS SENTIDOS, e as duas metades tem motivos diferentes:
    · no POOL a etnia nao pode existir, senao uma entrada deixa de servir as duas
      paginas e a injecao passa a se contradizer;
    · no BLOCO ela TEM de existir, senao a congruencia inviolavel (etnia do REF =
      etnia do avatar da pagina) sai do video sem ninguem ver.
    """
    et = ETNIA[spec["pagina"]]
    for rot, p in (("narradora", spec["narradora"]), ("homem", spec["homem"])):
        txt = " ".join(v for v in p.values() if isinstance(v, str))
        achado = _etnia_no_pool(txt)
        if achado:
            achados.append(("ERRO", "EX10: a entrada %s[%s] carrega etnia %s — "
                                    "num pool unico ela deixa de servir as duas "
                                    "paginas e briga com a injecao"
                            % (rot, p["id"], achado)))
    for nome in ("BLOCO 0 (REF)", "IMAGE 01/02", "IMAGE 02/02"):
        if et not in blocos[nome]:
            achados.append(("ERRO", "EX10: %s sem a etnia da pagina (%r) — a "
                                    "congruencia com o avatar sai do video sem "
                                    "ninguem ver" % (nome, et)))


def _ex11_elenco(spec, blocos, achados):
    """EX11 — elenco 2/1/2, uma voz so', e a varanda e' a mesma nas tres cenas.

    ⛔ Zero plateia: plateia e' ESCANDALO/FLAGRANTE e e' um dos quatro
    ingredientes da composicao que produziu as recusas deterministicas de
    2026-07-30.
    ⛔ Cena 2 e' ela SOZINHA: e' a cena da REGRA, e um segundo corpo em quadro
    rouba o unico argumento que o agente tem.
    """
    # ⛔⛔ A LENTE DE `She is alone in the frame.` MORREU AQUI, e o motivo
    # tem de ficar escrito: ela cobrava a CENA 2 DO MOTOR DE 24s, que era ela
    # sozinha atras da mesa de ferro. Essa cena nao existe mais — a fundida
    # herdou o quadro da cena 3, que tem DOIS corpos por construcao (ela e o
    # corpo-prova cortado no peito).
    # ⚠️ Repontar a lente para o bloco novo seria pior que remove-la: ela
    # reprovaria 100% dos lotes por exigir o oposto do que a cena pede. Foi
    # exatamente isso que a substituicao em bloco `/03`->`/02` fez no PLACA, no
    # BOTICA e no COLO hoje.
    # ⭐ NO LUGAR DELA, a garantia SIMETRICA: a fundida tem de declarar que sao
    # DOIS e so' dois. Sem isso o Veo preenche o quadro com figurante, e o
    # agente inteiro depende de nao haver plateia.
    if "They are the only two people in the frame." not in blocos["IMAGE 02/02"]:
        achados.append(("ERRO", "EX11: IMAGE 02/02 nao fecha a contagem de "
                                "gente — a cena fundida e' ela e o corpo-prova, "
                                "e um terceiro corpo em quadro rouba o "
                                "argumento"))
    if "Only she speaks." not in blocos["TAKE 01/02"] or \
            "Only she speaks." not in blocos["TAKE 02/02"]:
        achados.append(("ERRO", "EX11: falta `Only she speaks.` num dos takes "
                                "com dois em quadro — sem isso o homem dubla a "
                                "fala dela e o dialogo do Veo sai torto"))
    re_ancora = spec["varanda"]["re_ancora"]
    # ⚠️ So' a fundida: com dois blocos, a re-ancora existe para o segundo
    # nao perder a varanda e a bandeira.
    for nome in ("IMAGE 02/02",):
        if re_ancora not in blocos[nome]:
            achados.append(("ERRO", "EX11: %s sem a re-ancora da varanda — "
                                    "metade do lote perde o cenario e a "
                                    "bandeira a partir da cena 2" % nome))


def _ex11_plantado(spec, blocos, achados):
    """EX11/ES9 — a gelatina esta' PLANTADA na mesa desde o frame 1 da cena 2, e o
    objeto da keyword esta' NA MAO LIVRE dela no frame em que a boca diz
    `gelatin,`.

    ⛔⛔ ISTO NAO TINHA LINTER ATE' 2026-08-03, e os dois miolos (`M_PLANTADO` e
    `M_KEYWORD`) existiam no arquivo com UMA ocorrencia cada — a definicao. Eram
    constantes mortas sob um cabecalho que dizia `MIOLOS INVARIANTES`, e o
    `pyflakes` nao pega nome de modulo nao usado, entao a saida vazia nao provava
    nada. Sabotagem medida: apagar a gelatina plantada e tirar a keyword da mao
    dela passavam as duas EM SILENCIO.
    ⭐ O que a regra compra: objeto que entra de fora do quadro nao e' premio, e'
    corte disfarcado. O reveal da cena 3 nao apresenta nada novo — ele PAGA o que
    ja' estava na mesa desde o primeiro frame da cena 2.
    """
    # ⛔⛔ A COBRANCA DO PLANTIO MORREU, e o motivo importa. Ela exigia que o
    # mecanismo estivesse na mesa desde o frame 1 da CENA 2 do motor de 24s,
    # para que o reveal da cena 3 nao apresentasse objeto novo (ES9: objeto que
    # entra de fora do quadro nao e' premio, e' corte disfarcado). A cena que
    # fazia o plantio e' justamente a que caiu.
    # ⭐ Com DOIS takes o principio se cumpre dentro do proprio take: o objeto
    # da keyword esta' na mao dela no PRIMEIRO FRAME da fundida e fica ate' o
    # fim — nao entra de fora do quadro em momento nenhum. E' a mesma leitura do
    # TRIO 16.
    # ⚠️ Nao repontei para a cena 1: por o gelatin na mao dela durante o despejo
    # seria mudar a CENA, e cena e' alcada do operador.
    if M_KEYWORD not in blocos["IMAGE 02/02"]:
        achados.append(("ERRO", "EX11/ES9: IMAGE 02/02 nao poe o objeto da "
                                "keyword na mao livre dela — a boca diz "
                                "`gelatin,` e a mao nao mostra o que a palavra "
                                "compra"))
    # ⚠️ Continua valendo como regra de FUNCAO: a constante pode estar
    # presente e ainda apontar para outro objeto se alguem sortear o mecanismo
    # duas vezes. O que mudou e' o endereco, nao a pergunta.
    if mec_curto_fora(spec, blocos):
        achados.append(("ERRO", "EX11/ES9: o objeto da keyword na mao dela nao "
                                "e' o mecanismo sorteado deste video"))


def mec_curto_fora(spec, blocos):
    """O objeto da mao na cena 3 e' o MESMO que foi plantado na cena 2?

    ⛔ Regra de FUNCAO: as duas travadas podem estar presentes e ainda assim
    apontar para objetos diferentes se alguem sortear o mecanismo duas vezes.
    """
    return spec["mecanismo"]["curto"] not in blocos["IMAGE 02/02"]


def _ex12_piso(spec, blocos, achados):
    """EX12 — o piso e' AVISO, e o motivo esta' escrito: cena abaixo do piso e'
    beat da fonte perdido, e o arco da fonte e' a lei (EX1).

    ⚠️ Piso nao se cumpre com enchimento (licoes-de-construcao §5) — cumpre-se com
    o beat da fonte que estava faltando.
    """
    for i, fala in enumerate(spec["falas"], 1):
        n = _palavras(fala)
        if n < PISO_FALA[i]:
            achados.append(("AVISO", "EX12: cena %d com %d palavras (piso %d) — "
                                     "beat da fonte perdido, nao enchimento"
                            % (i, n, PISO_FALA[i])))


def _ex14_orgao(spec, blocos, achados):
    """EX14 — `your {o}`, o corpo do ESPECTADOR, e substantivos DISTINTOS.

    ⭐ E' o que transfere o prop para quem assiste, e e' o que faz o porteiro
    passar de graca neste agente: o espectador sabe do que se trata em 2,9
    segundos, na palavra 6 da primeira frase.
    ⛔ Regra de FUNCAO, nao de forma: nao basta o orgao aparecer no video (o
    `cota_min` do `lint_curto` ja' cobra isso e passaria). Ele tem de aparecer na
    CENA 1, em SEGUNDA PESSOA.
    """
    rx = re.compile(r"\byour\s+(%s)\b" % "|".join(NUCLEO), re.I)
    if not rx.search(spec["falas"][0]):
        achados.append(("ERRO", "EX14: a cena 1 nunca diz `your <nucleo>` — o "
                                "espectador tem de INFERIR que a demo e' o "
                                "corpo dele, e e' onde a copy vira vaga"))
    for i in (0, 1):
        if re.search(r"\b(his|their)\s+(%s)\b" % "|".join(NUCLEO),
                     spec["falas"][i], re.I):
            achados.append(("ERRO", "EX14: a cena %d fala do orgao em terceira "
                                    "pessoa — nas cenas 1 e 2 e' sempre `your`"
                            % (i + 1)))
    # ⛔⛔ LENTE APOSENTADA EM 2026-08-10 — E A REVERSAO E' O CT4 DO CONTRATO.
    # Aqui morava:
    #     if spec["orgaos"][0] == spec["orgaos"][1]:
    #         ERRO "as cenas 1 e 2 usam o mesmo substantivo — duas mencoes
    #               iguais em 16 segundos sao bordao"
    # ⚠️ A lente EXIGIA exatamente o defeito que o contrato mede: o apelido do
    # orgao mudando no corte, medido em 100% dos sorteios deste motor. Em 16s o
    # corte zera a memoria de trabalho e a troca de nome obriga o espectador a
    # remapear no segundo 9. ⛔ A pergunta oposta agora e' feita pelo
    # `sc.lint_copy16` (CT4), que cobra o MESMO apelido nos dois takes; manter
    # as duas seria reprovar 100% dos lotes com as duas pontas ao mesmo tempo.
    # ⭐ O que sobra da EX14 continua de pe' e e' o que ela tinha de mais forte:
    # `your <nucleo>` na cena 1 e ZERO terceira pessoa. So' a exigencia de
    # substantivos DIFERENTES caiu.


def _ex17_cauda(spec, blocos, achados):
    """EX17 — a cauda em todo IMAGE. A metade dos TAKE ja' e' cobrada pelo
    `lint_sem_texto` dentro do `lint_curto`; esta e' a outra metade."""
    for nome in sorted(blocos):
        if nome.startswith("IMAGE") and CAUDA not in blocos[nome]:
            achados.append(("ERRO", "EX17: %s sem a cauda — sem ela o Veo pode "
                                    "desenhar legenda ou marca, e a nossa "
                                    "legenda nasce depois, no Editor" % nome))


def _ct16(spec, blocos, achados):
    """⭐⭐ AS SETE TRAVAS DO CONTRATO DE COPY 16s, ligadas neste motor.

    Doutrina: `funil-organico/CONTRATO-COPY-16S.md`.
    Codigo:   `short_comum.lint_copy16` — uma regra, um lugar.

    ⭐ `isca_absurda=True` porque o take 1 deste angulo E' uma promessa falsa
    que o proprio video desmente meio segundo depois (bicarbonato + `swell`).
    So' o CT7 muda com esse flag: ali o verbo de tumescencia e' a ISCA, nao um
    claim nosso, e proibi-lo mataria o angulo. ⛔ No take 2 ele continua
    proibido colado no orgao — a licao paga no COLO 16, ~95% de recusa.
    """
    sc.lint_copy16(sys.modules[__name__], spec, achados, isca_absurda=True)


# ⛔⛔ O AVISO QUE O CT4 TORNOU FALSO — e por que ele e' filtrado AQUI.
# ---------------------------------------------------------------------------
# O `sc.lint_curto` emite `substantivo repetido no video: [...]` sempre que o
# mesmo apelido do orgao aparece nas duas falas. Isso era a regra ate'
# 2026-08-10 e passou a ser a EXIGENCIA (CT4): um apelido por video, repetido
# nos dois takes. Com a reforma o aviso dispara em 100% dos sorteios,
# acusando exatamente a copy correta.
# ⛔ O conserto certo seria no `short_comum.py` — mas ele e' compartilhado por
# 23 motores e OUTROS AGENTES ESTAO TRABALHANDO NELE EM PARALELO neste mesmo
# momento; editar arquivo de outro dono e' como se perde um dia de trabalho
# alheio. Entao o filtro mora aqui, NOMEADO e com o motivo escrito, ate' que o
# dono do `short_comum` inverta a lente la' dentro.
# ⚠️ O filtro e' de PREFIXO EXATO e so' pega esta mensagem: aviso novo que
# apareca amanha' continua chegando ao operador.
_AVISO_REVOGADO_CT4 = "substantivo repetido no video"


def lint(spec, blocos):
    # ⭐ EX13 (CTA e gate literais da fonte com a nossa keyword na frente) NAO tem
    # funcao propria aqui de proposito: ela e' cobrada pelo `lint_cta_literal` e
    # pelo `lint_isca_cta` de dentro do `lint_curto`, que e' o unico lugar do repo
    # onde essa regra mora. ⛔ O registro existe porque a EX13 era a UNICA regra da
    # doutrina que o motor nunca citava — quem rastreasse `EX13` no codigo nao
    # achava nada e concluiria que a regra ficou sem cobranca.
    # ⚠️ `teto_total` explicito: o padrao do `lint_curto` e' a soma dos tetos
    # (94), e a faixa da doutrina permite 96 — o AVISO dispararia abaixo do
    # numero que ela mesma autoriza.
    achados = sc.lint_curto(
        sys.modules[__name__], spec, blocos, (1, 2, 3), TETO_FALA,
        literais=("gelatin trick",), teto_total=TETO_TOTAL, cota_min=2,
        extras=(_ex2_regra, _ex3_batismo, _ex4_geometria, _ex5_sem_rosto,
                _ex6_marca, _ex7_blindagem, _ex7_movimento, _ex7_lexico,
                _ex8_nada_cresce, _ex9_ref, _ex10_etnia, _ex11_elenco,
                _ex11_plantado, _ex12_piso, _ex14_orgao, _ex17_cauda,
                # ⭐⭐ o CONTRATO DE COPY 16s, ligado em 2026-08-10
                _ct16))
    return [a for a in achados
            if not a[1].startswith(_AVISO_REVOGADO_CT4)]


# ---------------------------------------------------------------------------
# UI — contrato do ui_agente.py compartilhado
# ---------------------------------------------------------------------------
EIXOS_UI = [
    ("narradora", "A NARRADORA", "NARRADORAS", "rosto"),
    ("homem", "O HOMEM SEM ROSTO", "HOMENS_SEM_ROSTO", "roupa"),
    ("varanda", "A VARANDA (as 3 cenas)", "VARANDAS", "id"),
    ("mesa", "A MESA DA VARANDA", "MESAS", "curto"),
    ("caixa", "A CAIXA DE BICARBONATO", "CAIXAS", "id"),
    ("despejo", "O GESTO DO DESPEJO", "DESPEJOS", "id"),
    ("reacao", "A REACAO DELA", "REACOES", "id"),
    ("mecanismo", "O MECANISMO PLANTADO", "MECANISMOS", "curto"),
]

# ⭐ VAZIO, E ISSO E' UMA PROPRIEDADE DO AGENTE, NAO UM ESQUECIMENTO.
# Nos outros motores trocar o prop, a substancia ou a receita OBRIGA a reescrever
# a fala, porque a fala os nomeia. Aqui a copy e' a da fonte (EX1) e nao nomeia
# eixo visual nenhum: a caixa e' sempre `baking soda`, o mecanismo e' sempre o
# `gelatin trick`, e nem a varanda nem o gesto entram na boca. Entao clicar em
# qualquer eixo da UI nao pode mexer na copy — e mexer seria justamente violar a
# EX1. ⛔ Quem adicionar um eixo que ENTRE na fala tem de adicionar a funcao aqui.
EIXOS_QUE_MEXEM_NA_COPY = {}

PT_VARANDA = {
    "fazenda_meio_oeste": "Na varanda de uma casa de fazenda do Meio-Oeste",
    "rancho_suburbano": "Na varanda estreita de uma casa de subúrbio",
    "cabana_montanha": "No deck de uma cabana de tora",
    "casa_praia": "Na varanda alta de uma casa de praia",
    "colonial_colunas": "Na varanda de colunas de uma casa colonial branca",
    "bangalo_craftsman": "Na varanda baixa de um bangalô Craftsman",
    "casa_movel": "Na varanda anexa de uma casa móvel",
    "lago_deck": "No deck de uma casa de veraneio à beira do lago",
    "vitoriana": "Na varanda rendilhada de uma casa vitoriana",
    "deserto_adobe": "Na varanda sombreada de uma casa de adobe no deserto",
    "varanda_telada": "Numa varanda telada de uma casa da Flórida",
    "fazenda_sul": "Na varanda comprida de uma casa de fazenda do Sul",
    "celeiro_convertido": "No deck de um celeiro convertido",
    "apalaches": "Numa varanda de tábuas nos Apalaches",
}


def resumo_pt(spec):
    """A frase que permite aprovar ou re-sortear em dois segundos."""
    et = "branca" if "white" in ETNIA[spec["pagina"]] else "negra"
    return (
        # ⚠️ TEXTO CORRIGIDO EM 2026-08-10. Ele descrevia TRES cenas e a cena 2
        # do motor de 24s (ela sozinha atrás da mesa) — um quadro que não existe
        # aqui desde a fusão. Resumo que descreve vídeo que o motor não gera é
        # o pior tipo de mentira: o operador aprova ou re-sorteia lendo ISTO.
        "%s, uma narradora de %d anos, de pele %s, despeja bicarbonato sobre "
        "um geoduck em pé que um homem de %d anos segura com as duas mãos — "
        "ele entra "
        "CORTADO NO PEITO, sem rosto em quadro. No TAKE 1 ela manda jogar "
        "bicarbonato no %s e ver inchar, demole a própria isca (o pó fica do "
        "lado de fora) e fecha dizendo A FALHA DELE, com relógio. No TAKE 2, "
        "na MESMA varanda (a mesa sorteada é %s), ela diz o MECANISMO — sangue "
        "com pressão, no órgão —, entrega o gelatin trick como o que resolveu "
        "para o homem dela, pede o follow e SÓ ENTÃO chama o comentário, com "
        "%s na mão livre. "
        # ⛔⛔ SO' cp1252 AQUI. O console do Windows deste repo roda em cp1252, e
        # `resumo_pt` e' a UNICA string do motor que passa pelo `print` do CLI:
        # um `⛔` (U+26D4) nesta linha derrubava `--pagina joe` com
        # UnicodeEncodeError em 100% das execucoes — e o `--stats` nao pegava,
        # porque o self-test nunca chama `resumo_pt`. Os outros nove motores sao
        # cp1252-safe aqui; este era o unico fora. ⛔ Nada de emoji nesta funcao.
        "Dois takes de 8s; nada cresce em cena nenhuma."
        % (PT_VARANDA.get(spec["varanda"]["id"], "Na varanda"),
           spec["narradora"]["idade"], et, spec["homem"]["idade"],
           spec["orgaos"][0], spec["mesa"]["curto"],
           spec["mecanismo"]["curto"])
    )


def nova_fala(spec, i, rng):
    """Re-sorteia a fala da cena i (0-2) preservando o orgao que ja' esta' nela —
    a rotacao do substantivo e' do VIDEO, nao da fala."""
    return _montar_falas(rng, spec["orgaos"])[i]


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def imprimir(spec, blocos, achados):
    print("=" * 72)
    print("SPEC — pagina %s | narradora %s (%d) | homem %s (%d) | varanda %s"
          % (spec["pagina"], spec["narradora"]["id"], spec["narradora"]["idade"],
             spec["homem"]["id"], spec["homem"]["idade"], spec["varanda"]["id"]))
    print("       mesa %s | caixa %s | despejo %s | reacao %s | mecanismo %s"
          % (spec["mesa"]["id"], spec["caixa"]["id"], spec["despejo"]["id"],
             spec["reacao"]["id"], spec["mecanismo"]["id"]))
    print("       orgaos %s" % ", ".join(spec["orgaos"]))
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
    # ⚠️ ERA `faixa 82-%d`, herdado do arco de 24s: com dois takes de 8s o
    # video tem 16 segundos e teto 50. Imprimir uma faixa que comeca ACIMA do
    # proprio teto e' pedir para o operador procurar um problema inexistente.
    print("video: %d palavras (teto %d, 2 takes de 8s)" % (total, TETO_TOTAL))
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
EIXOS_VISUAIS = ("narradora", "homem", "varanda", "mesa", "caixa", "despejo",
                 "reacao", "mecanismo")
MIN_OPCOES = 9          # piso por eixo visual
TETO_FREQ = 0.17        # nenhum item pode concentrar mais que isso

# ⚠️ ATE' 2026-08-10 TRES POOLS FICAVAM ABAIXO DE 9 (ALIANCAS 5, GATES 6,
# DESMENTIDOS 7) e o motivo escrito era a EX1: a fonte da' UMA frase curta de
# cada e nao havia vocabulario nela para chegar a 14 sem inventar claim.
# ⭐ Com a EMENDA DA EX1 (o verbatim caiu para a familia 16s) essa restricao
# deixou de existir, e os pools que continuavam vivos foram TODOS ampliados.
# `GATES` continua em 6 porque esta' aposentado — quem faz o gate e' FOLLOWS16.
# ⛔⛔ PISOS ATUALIZADOS EM 2026-08-10 — E NENHUM DELES DESCEU.
# Ordem permanente do operador: *"nao sacrifique, dimira ou faca quaisquer
# regressao no agente que ocasione perda de entropia"*. A reforma de copy
# reescreveu seis pools de fala e TODOS sairam maiores ou iguais:
#     ISCAS           8 -> 10      DISCLOSURES16   9 -> 10
#     DESMENTIDOS     7 -> 10      FOLLOWS16       6 ->  7
#     MECANISMOS16   10 -> 11      CTAS            9 -> 10
#     ALIANCAS (5) aposentada -> FALHAS16 (12), batida nova
# ⚠️ `ALIANCAS` sai do piso porque saiu do sorteio (pool aposentado, ver o
# cabecalho dele). ⛔ Piso cobrado sobre pool que ninguem usa e' piso que da'
# a impressao de que alguem olhou.
MIN_COPY = {"ISCAS": 10, "DESMENTIDOS": 10, "FALHAS16": 12, "REGRAS": 9,
            "MECANISMOS_FALA": 10, "FUNDIDAS": 12, "CTAS": 10, "GATES": 6,
            "MECANISMOS16": 11, "DISCLOSURES16": 10, "FOLLOWS16": 7}


def _contrato_dos_pools(falhas):
    """⛔ Os pools tem contratos que o motor DERIVA — e derivacao muda que nao e'
    cobrada e' derivacao que quebra calada.

    Cada um destes ja' seria um bug silencioso: uma isca sem `{o}` deixaria a
    cena 1 sem segunda pessoa e furaria a EX14 no sorteio (nao so' no linter); um
    mecanismo sem `{o}` reprovaria no `medir_contexto_copy` como cena orfa; uma
    regra sem o par outside/inside passaria pelo `_ex2_regra` so' por acaso; e
    uma caixa cujo `recipiente` nao aparece no proprio texto poria a palavra
    errada no resumo em portugues.
    """
    for i, t in enumerate(ISCAS):
        if "{o}" not in t or "baking soda" not in t.lower():
            falhas.append("ISCAS[%d] sem `{o}` ou sem `baking soda` — a cena 1 "
                          "perde a segunda pessoa ou contradiz a imagem" % i)
        # ⛔ EX14 por CONSTRUCAO: a lente cobra `your <nucleo>` na cena 1 depois
        # do sorteio; aqui o pool ja' nasce cumprindo, senao o defeito so'
        # apareceria em alguns sorteios.
        if "your {o}" not in t:
            falhas.append("ISCAS[%d] nao diz `your {o}` — a cena 1 tem de por o "
                          "prop no corpo de QUEM ASSISTE (EX14)" % i)
        # ⛔ TETO POR CONSTRUCAO: 10 + pior DESMENTIDO (7) + pior FALHA (7) = 24.
        # Uma isca de 11 estouraria o teto de 25 com o pior par, e o motor
        # esconderia isso escolhendo outro par — entrada meio-viva.
        if _w(t) != 10:
            falhas.append("ISCAS[%d] tem %d palavras (contrato: 10) — o "
                          "orcamento da cena 1 fecha por construcao e uma "
                          "entrada fora de tamanho mata combinacao por "
                          "[ALCANCE]" % (i, _w(t)))
        # ⛔⛔ ANTI-ECO NO PROPRIO POOL: `_repete` casa bigrama de conteudo, e
        # `baking soda` na batida 2 ou 3 mataria a entrada contra TODAS as
        # ISCAS. Aqui o guarda e' do lado oposto — nenhuma isca pode carregar
        # vocabulario que as outras batidas precisam.
    for i, t in enumerate(DESMENTIDOS):
        if not 4 <= _w(t) <= 7:
            falhas.append("DESMENTIDOS[%d] tem %d palavras (contrato: 4-7) — "
                          "fora da banda o teto da cena 1 deixa de fechar por "
                          "construcao" % (i, _w(t)))
        if "baking soda" in t.lower():
            falhas.append("DESMENTIDOS[%d] repete `baking soda` — a guarda de "
                          "eco casa o bigrama contra TODAS as ISCAS e a entrada "
                          "nasce morta" % i)
        if "{o}" in t:
            falhas.append("DESMENTIDOS[%d] traz `{o}` — a cena 1 ja' nomeia o "
                          "orgao na isca, e duas vezes em 8 segundos e' bordao"
                          % i)
        # ⛔⛔ O DE-FORA TEM DE TER NOME (conferencia 2026-08-10). O operador
        # reprovou `The outside changes nothing` em 2026-08-08 com quatro
        # palavras — *"Outside de quE?"* — e duas entradas com a mesma forma
        # nua sobreviveram a' reforma porque o cabecalho AFIRMAVA o criterio em
        # vez de o motor COBRAR. Toda entrada nomeia o PO' (`powder`) ou o
        # GESTO (`pour`), ou opoe explicitamente `outside`/`inside`.
        baixo_d = t.lower()
        if not ("powder" in baixo_d or "pour" in baixo_d
                or ("outside" in baixo_d and "inside" in baixo_d)):
            falhas.append("DESMENTIDOS[%d] nega uma abstracao (%r) — sem "
                          "`powder`, sem `pour` e sem o par outside/inside o "
                          "espectador nao sabe do que se fala em uma audicao"
                          % (i, t))
    # ⭐⭐ CT2 — TODA FALHA TEM DE SER RECONHECIVEL PELA LENTE DO CONTRATO.
    # ⛔ Nao basta a frase "falar de falha": o `lint_copy16` procura um LEXICO
    # fechado, e frase que descreve o dano com palavra fora dele passa pelo
    # revisor humano e reprova no medidor.
    # ⛔⛔ POR ISSO A PERGUNTA E' FEITA A' PROPRIA LENTE, com uma spec-sonda, em
    # vez de a um regex COPIADO para ca'. Copia de regex envelhece sozinha: no
    # dia em que o `short_comum` ganhar um verbo novo, a copia continua velha e
    # o contrato passa a mentir nos dois sentidos. Uma regra, um lugar.
    # ⚠️ A sonda so' olha o CT2 — o resto dos achados dela e' lixo esperado
    # (fala 2 de mentira).
    for i, t in enumerate(FALHAS16):
        _sonda, _ach = {"falas": [t, "Comment gelatin."]}, []
        sc.lint_copy16(sys.modules[__name__], _sonda, _ach, isca_absurda=True)
        if any(m.startswith("CT2") for _, m in _ach):
            falhas.append("FALHAS16[%d] nao enuncia FALHA no lexico do CT2 (%r) "
                          "— sem dano concreto o espectador nao se reconhece e "
                          "nao comenta" % (i, t))
        if not 6 <= _w(t) <= 7:
            falhas.append("FALHAS16[%d] tem %d palavras (contrato: 6-7) — o "
                          "teto da cena 1 e' 10+7+7=24 e uma entrada de 8 "
                          "estoura com o pior desmentido" % (i, _w(t)))
        if "{o}" in t:
            falhas.append("FALHAS16[%d] traz `{o}` — o orgao ja' esta' na isca "
                          "da mesma fala" % i)
        # ⛔ VERBO PROXY (conferencia 2026-08-10). `You still lose it before she
        # does.` obriga o espectador a recuperar `lose it` da oracao anterior e
        # aplica-lo a OUTRA pessoa, em 8 segundos e ouvindo uma vez — e `she
        # loses it` nao significa nada em ingles americano. O dano tem de ser
        # dito com o verbo do dano; `does`/`did` no lugar dele e' o drifting de
        # pronome/verbo generico.
        if re.search(r"\b(does|did|do)\b\s*[.!?]?$", t, re.I):
            falhas.append("FALHAS16[%d] fecha em verbo proxy (%r) — o dano tem "
                          "de ser dito, nao substituido por `does`" % (i, t))
    for i, t in enumerate(MECANISMOS_FALA):
        if "{o}" not in t:
            falhas.append("MECANISMOS_FALA[%d] sem `{o}` — `circulation` dispara "
                          "o detector do medir_contexto_copy e sem o ALVO na "
                          "MESMA fala a cena 2 e' reprovada como orfa" % i)
        # ⛔ A EMENDA do PISO_FALA[2] (28 -> 24) e' justificada POR CONSTRUCAO:
        # "toda entrada carrega circulacao E pressao, nenhum beat cai". Enquanto
        # isso era so' prosa, uma entrada ficou sem `circulation` e 8,2% dos
        # videos perdiam o beat — a conta que sustenta a emenda ficava falsa em
        # 1 de cada 12 videos. ⛔ Afirmacao de comentario que o motor nao cobra e'
        # afirmacao que quebra calada.
        for beat in ("circulation", "pressure"):
            if beat not in t.lower():
                falhas.append("MECANISMOS_FALA[%d] sem `%s` — a EMENDA do "
                              "PISO_FALA[2] se apoia em `nenhum beat cai`, e "
                              "esta entrada derruba um" % (i, beat))
    # ⛔ §17 — a fonte diz a causa E o que ela quebra na MESMA oracao. Entrada que
    # diz so' `weak pressure` deixa o espectador sem saber do que se trata, e o
    # `medir_contexto_copy` nao pega porque `weak` nao esta' no lexico dele.
    for i, t in enumerate(FUNDIDAS):
        if "can't keep up" not in t:
            falhas.append("FUNDIDAS[%d] nomeia a causa (pressao fraca) sem dizer "
                          "o que ela quebra — falta `can't keep up`, que e' a "
                          "oracao da propria fonte (16,36-20,46)" % i)
    for i, t in enumerate(REGRAS):
        if "{o}" in t:
            falhas.append("REGRAS[%d] traz `{o}` — junto com o mecanismo isso "
                          "nomeia o orgao duas vezes na mesma fala" % i)
        if not _tem_regra(t):
            falhas.append("REGRAS[%d] nao carrega A REGRA (EX2)" % i)
    # ⚠️ O CONTROLE DO LINTER DA REGRA RODA ANTES DO POOL: ele ja' mentiu uma vez
    # (59 reprovacoes em cima da entrada que opoe o GESTO em vez do LUGAR).
    devem_r, nao_devem_r = CONTROLE_REGRA
    for frase in devem_r:
        if not _tem_regra(frase):
            falhas.append("CONTROLE do linter da REGRA: %r deveria passar"
                          % frase)
    for frase in nao_devem_r:
        if _tem_regra(frase):
            falhas.append("CONTROLE do linter da REGRA: %r deveria ser acusada"
                          % frase)
    for i, t in enumerate(FUNDIDAS):
        if "gelatin trick" not in t:
            falhas.append("FUNDIDAS[%d] sem o literal `gelatin trick` — o "
                          "criativo deixa de ser congruente com a VSL" % i)
    # ⛔ O DISCLOSURE (2026-08-09) — dois contratos, os dois ja' teriam quebrado
    # calados: entrada sem `{par}` volta a ser o terceiro anonimo que o operador
    # trocou, e entrada sem `gelatin trick` fura a EX3 so' em alguns sorteios.
    # ⛔ MECANISMOS16 — o beat que nenhum outro agente tem. Contrato em quatro
    # linhas, e as quatro ja' quebraram calado em algum motor do parque.
    for i, t in enumerate(MECANISMOS16):
        for beat in ("blood", "pressure"):
            if beat not in t.lower():
                falhas.append("MECANISMOS16[%d] sem `%s` — o `_ex2_regra` cobra "
                              "os dois na mesma fala, e sem eles o EXTERIOR 16 "
                              "vira isca absurda generica" % (i, beat))
        if "{o}" not in t:
            falhas.append("MECANISMOS16[%d] sem `{o}` — mecanismo sem destino e' "
                          "`algo melhora la' dentro`, o drifting que o operador "
                          "reprovou em 2026-08-08" % i)
        # ⛔ `blood pressure` colado = HIPERTENSAO em ingles americano. O video
        # passaria a falar de outra doenca no beat mais importante que ele tem.
        if re.search(r"\bblood\s+pressure\b", t, re.I):
            falhas.append("MECANISMOS16[%d] diz `blood pressure` colado — em "
                          "ingles americano isso e' hipertensao, nao ereccao"
                          % i)
        if _w(t.format(o="Johnson")) != 6:
            falhas.append("MECANISMOS16[%d] tem %d palavras (contrato: 6) — 6+8+"
                          "2+9 = 25 e' o teto no fio, e uma de 7 mata os CTAs de "
                          "9 palavras por [ALCANCE]"
                          % (i, _w(t.format(o="Johnson"))))
    # ⛔ DISCLOSURES16 — o beat do CT3. Sem verbo de efeito E alvo na MESMA
    # sentenca, `gelatin trick` e' rotulo nu e nao vira crenca.
    _alvos = tuple(sc.ALVOS_16) + tuple(n.lower() for n in NUCLEO)
    for i, t in enumerate(DISCLOSURES16):
        if "{par}" not in t:
            falhas.append("DISCLOSURES16[%d] sem `{par}` — sem o vinculo a fala "
                          "volta a ser prova de terceiro anonimo" % i)
        if "gelatin trick" not in t:
            falhas.append("DISCLOSURES16[%d] sem o literal `gelatin trick` — a "
                          "EX3 batiza na cena fundida e esta entrada nao batiza"
                          % i)
        baixo = t.lower()
        if not any(re.search(r"\b%s\b" % v, baixo) for v in sc.VERBOS_EFEITO_16):
            falhas.append("DISCLOSURES16[%d] sem VERBO DE EFEITO da lista do "
                          "`sc.VERBOS_EFEITO_16` (%r) — CT3: o nome do mecanismo "
                          "sem razao ao lado e' ruido de marca" % (i, t))
        if not any(a in baixo for a in _alvos):
            falhas.append("DISCLOSURES16[%d] sem ALVO na mesma sentenca (%r) — "
                          "CT3: o mecanismo tem de dizer sobre O QUE ele age"
                          % (i, t))
        # ⛔⛔ O ALVO TEM DE SER `blood` (conferencia 2026-08-10). `sc.ALVOS_16`
        # aceita `pressure` sozinho, e com ele passou `The gelatin trick gave
        # {par} pressure back.` — para o homem de 50-70 anos que esta pagina
        # persegue, `pressure` NU e' pressao arterial, a coisa que ele toma
        # remedio para BAIXAR. E' a irma da guarda que os MECANISMOS16 ja' tem
        # contra `blood pressure` colado, pela ponta oposta.
        if "blood" not in baixo:
            falhas.append("DISCLOSURES16[%d] tem alvo sem `blood` (%r) — "
                          "`pressure` sozinho e' hipertensao no ouvido de 50-70 "
                          "anos, nao ereccao" % (i, t))
        # ⛔ `works` E' ROTULO NU DISFARCADO. Ele esta' na lista de verbos de
        # efeito, mas nao declara efeito nenhum: "funciona" e' exatamente a
        # afirmacao que a sentenca do CT3 deveria estar PROVANDO. E `work on his
        # blood` em ingles americano puxa exame de sangue.
        if re.search(r"\bworks?\b", baixo):
            falhas.append("DISCLOSURES16[%d] usa `work(s)` (%r) — CT3 pede o "
                          "EFEITO, e `funciona` e' a afirmacao que a razao "
                          "deveria sustentar" % (i, t))
        if _w(t.format(par="my husband")) != 8:
            falhas.append("DISCLOSURES16[%d] tem %d palavras com o `{par}` "
                          "resolvido (contrato: 8) — fora disso o teto da cena 2 "
                          "deixa de fechar por construcao"
                          % (i, _w(t.format(par="my husband"))))
    # ⛔ Duas palavras cada: uma de tres empurra os disclosures para fora
    # da banda e mata dois deles em silencio (ver comentario do pool).
    for p in PARES16:
        if _w(p) != 2:
            falhas.append("PARES16 %r nao tem duas palavras — muda o orcamento "
                          "da cena 2 e mata disclosure por [ALCANCE]" % p)
        # ⛔ 2026-08-10: `my partner` desidentifica a prova social. O contrato
        # cobra a ausencia para ninguem reabrir o pool com o termo neutro.
        if "partner" in p:
            falhas.append("PARES16 %r usa `partner` — termo neutro de genero "
                          "num quadro que mostra um HOMEM; desidentifica a "
                          "unica prova social do video" % p)
    # ⛔ FOLLOWS16 — CT1 poe o follow ANTES do CTA, e o orcamento so' fecha com
    # duas palavras.
    for i, t in enumerate(FOLLOWS16):
        if _w(t) != 2:
            falhas.append("FOLLOWS16[%d] tem %d palavras (contrato: 2) — com 3 "
                          "o CTA de 9 palavras deixa de caber e a cobertura "
                          "social do CT6 morre por [ALCANCE]" % (i, _w(t)))
        if "gelatin" in t.lower():
            falhas.append("FOLLOWS16[%d] encosta na keyword — a automacao de DM "
                          "casa a palavra EXATA (lente T16-2)" % i)
        # ⛔ O FOLLOW E' PEDIDO, NUNCA CONDICAO (conferencia 2026-08-10).
        # `Followers only.` e' o defeito do CT1 (condicional na recompensa)
        # reentrando pela porta da frente: ele so' nao era acusado porque o CT1
        # mede POSICAO, e este beat mudou de lugar. O follow tem de ser verbo no
        # imperativo — a forma-substantivo poe o espectador decidindo se ele se
        # qualifica no segundo em que o video precisa que ele digite.
        if re.search(r"\bfollowers\b", t, re.I):
            falhas.append("FOLLOWS16[%d] e' condicao, nao pedido (%r) — a "
                          "forma-substantivo reimporta a condicional na "
                          "recompensa que o CT1 derrubou" % (i, t))
    for i, t in enumerate(CTAS):
        if sc.CTA_LITERAL not in t:
            falhas.append("CTAS[%d] sem o literal %r" % (i, sc.CTA_LITERAL))
        if "GELATIN" in t:
            falhas.append("CTAS[%d] com a keyword em CAIXA ALTA — o Veo "
                          "soletra" % i)
        # ⛔⛔ CT6 — a sentenca do CTA diz ONDE a receita chega. Era 100% dos
        # sorteios antes da reforma: o comentario leva nome e foto para o feed,
        # e sem a cobertura o custo social de comentar fica maior que a
        # curiosidade. A clausula e' de graca (mesmo custo em palavras).
        if not sc.ENTREGA_16.search(t):
            falhas.append("CTAS[%d] nao diz ONDE a receita chega (%r) — CT6"
                          % (i, t))
        # ⛔ CT5 — nenhum ingrediente na fala. A receita e' a UNICA moeda que o
        # comentario compra, e entregue uma vez esta' gasta para os outros 49
        # videos da pagina. ⚠️ `gelatin` NAO conta: e' a keyword.
        m_ing = sc.INGREDIENTES_16.search(t)
        if m_ing:
            falhas.append("CTAS[%d] entrega o ingrediente %r — CT5"
                          % (i, m_ing.group(0)))
        # ⛔ CT7 — verbo de ereccao na fala do CTA e' claim NOSSO. ~95% de
        # recusa medida no COLO 16 quando colado no orgao.
        if sc.ERECAO_16.search(t):
            falhas.append("CTAS[%d] traz verbo de ereccao (%r) — CT7"
                          % (i, sc.ERECAO_16.search(t).group(0)))
        if not 8 <= _w(t) <= 9:
            falhas.append("CTAS[%d] tem %d palavras (contrato: 8-9) — o teto da "
                          "cena 2 e' 6+8+2+9 = 25" % (i, _w(t)))
        # ⛔ `lint_isca_cta`: o CTA tem de dizer O QUE a pessoa recebe. Cobrado
        # no pool, nao so' no sorteio — pool que nasce sujo produz o defeito em
        # 1 de cada N videos, que e' o pior de todos os regimes.
        if not sc.ISCA_CTA.search(t):
            falhas.append("CTAS[%d] pede o comentario e nao diz o que chega (%r)"
                          % (i, t))
    for c in CAIXAS:
        if c["recipiente"] not in c["caixa"].lower():
            falhas.append("CAIXAS[%s]: o `recipiente` (%s) nao aparece no texto "
                          "da propria caixa" % (c["id"], c["recipiente"]))
        if "baking soda" not in c["caixa"].lower():
            falhas.append("CAIXAS[%s] nao e' de bicarbonato — a boca diz "
                          "`baking soda` e imagem que contradiz a boca queima o "
                          "take" % c["id"])
    # ⛔ o vocativo so' pode existir nos GATES (TR15). Se escorregar para os CTAS,
    # a cena 3 passa a ter dois num video so'.
    for nome, pool in (("CTAS", CTAS), ("FUNDIDAS", FUNDIDAS)):
        sujos = [x for x in pool if _achar(x, VOCATIVOS)]
        if sujos:
            falhas.append("%d entrada(s) de %s com vocativo — o vocativo so' "
                          "mora nos GATES" % (len(sujos), nome))
    n_voc = sum(1 for g in GATES if _achar(g, VOCATIVOS))
    if n_voc >= len(GATES) / 2.0:
        falhas.append("GATES: %d de %d com vocativo — a maioria tem de vir sem "
                      "nenhum" % (n_voc, len(GATES)))
    # ⛔ EX7 — nenhuma entrada de pool pode trazer declaracao de movimento: as
    # travadas nao sao o unico caminho para ela entrar no bloco.
    for nome, pool, campos in (("DESPEJOS", DESPEJOS, ("img", "take")),
                               ("REACOES", REACOES, ("desc",)),
                               ("MECANISMOS", MECANISMOS,
                                ("plantado", "curto", "pousado"))):
        for it in pool:
            txt = " ".join(it[c] for c in campos).lower()
            achado = [t for t in EX_MOVIMENTO_PROIBIDO if t in txt]
            if achado:
                falhas.append("%s[%s] declara estado de movimento %s (EX7)"
                              % (nome, it["id"], achado))
            # ⛔ EX7 — `neck` por SUBSTRING, nao por palavra inteira. `neckline`
            # passava pelos dois guardas do bloco montado (`"neck "` com espaco e
            # `\bneck\b`) e caia na direcao do TAKE 01/03, que e' o bloco em que o
            # geoduck vira pato. ⚠️ Aqui a substring e' segura porque estes tres
            # pools nao descrevem roupa — `crew-neck`/`scoop-neck` moram no
            # figurino do elenco, que este laco nao varre.
            if "neck" in txt:
                falhas.append("%s[%s] contem `neck` — a peca do geoduck e' o "
                              "`siphon`, e o token puxa pescoco de ave para "
                              "dentro do TAKE (EX7)" % (nome, it["id"]))
    # ⛔ EX10 — zero etnia dentro dos pools de pessoa. ⚠️ O CONTROLE DO LINTER
    # RODA ANTES: este regex ja' mentiu uma vez (418 reprovacoes em cima de cor
    # de roupa), e medidor quebrado produz um "passou" mentiroso.
    devem, nao_devem = CONTROLE_ETNIA
    for frase in devem:
        if not _etnia_no_pool(frase):
            falhas.append("CONTROLE do linter de etnia: %r deveria ser acusada"
                          % frase)
    for frase in nao_devem:
        achado = _etnia_no_pool(frase)
        if achado:
            falhas.append("CONTROLE do linter de etnia: %r nao podia ser "
                          "acusada (casou %s)" % (frase, achado))
    for nome, pool in (("NARRADORAS", NARRADORAS),
                       ("HOMENS_SEM_ROSTO", HOMENS_SEM_ROSTO)):
        for p in pool:
            txt = " ".join(v for v in p.values() if isinstance(v, str))
            achado = _etnia_no_pool(txt)
            if achado:
                falhas.append("%s[%s] carrega etnia %s (EX10)"
                              % (nome, p["id"], achado))
    # ⛔ EX9 — a faixa de idade da lei da REF
    fora = [n["id"] for n in NARRADORAS
            if not IDADE_MINIMA_NARRADORA <= n["idade"] <= IDADE_MAXIMA_NARRADORA]
    if fora:
        falhas.append("EX9: narradora(s) fora da faixa %d-%d: %s"
                      % (IDADE_MINIMA_NARRADORA, IDADE_MAXIMA_NARRADORA,
                         ", ".join(fora)))
    # ⚠️ o gap de idade do par, so' para REGISTRO: a guarda dos outros motores e'
    # 30, e este pool ja' nasce dentro dela. Se alguem ampliar HOMENS_SEM_ROSTO
    # para cima, isto acusa antes de virar composicao de intimidade.
    gap = max(h["idade"] for h in HOMENS_SEM_ROSTO) \
        - min(n["idade"] for n in NARRADORAS)
    if gap > TETO_DIF_IDADE:
        falhas.append("o par pode sair com %d anos de diferenca (teto %d) — "
                      "ES11" % (gap, TETO_DIF_IDADE))


def _viabilidade(falhas):
    """⛔ O ORCAMENTO E' ALCANCAVEL? Enumeracao EXAUSTIVA do pior e do melhor caso
    de cada cena, nao estimativa.

    Foi assim que se descobriu, no TROCA, que o teto de nenhuma cena era
    alcancavel (o AVISO virava codigo morto) e que a cena 2 ficava abaixo do piso
    em 48% dos sorteios. As duas bordas sao MEDIDAS.
    """
    # ⛔⛔ O MOLDE NAO SE MEDE, MEDE-SE A STRING FINAL — e isto acabou de custar
    # um relatorio errado (2026-08-10). A conta antiga era
    # `_w(molde) + _w(par) - 1`, que supoe que `{par}` vale UM token no molde
    # cru. Com o disclosure novo o slot aparece como `{par}'s`, e o
    # `[A-Za-z'\-]+` conta `par` E `'s` — dois tokens. A enumeracao saia UMA
    # palavra pessimista por combinacao e acusou 24.948 de 30.800 combinacoes
    # "fora da banda" num orcamento que o sorteio real fecha em 24-25.
    # ⚠️ E' o mesmo erro que o proprio `_montar_falas` ja' evitava resolvendo o
    # `{par}` ANTES de medir. Duas contas do mesmo orcamento, uma certa e uma
    # errada, e quem imprimia numero era a errada (licoes §16).
    o_caro = max(NUCLEO, key=_w)                   # o `{o}` mais caro
    print("\nVIABILIDADE DO ORCAMENTO — enumeracao exaustiva")
    print("-" * 72)

    # ⚠️ `ALIANCAS` saiu daqui em 2026-08-10 junto com a batida: quem fecha a
    # cena 1 agora e' `FALHAS16` (CT2). Enumerar o pool aposentado mediria uma
    # cena que o motor nao produz mais — o modo de falha §16 na forma mais cara.
    c1 = [_w(i.format(o=o_caro)) + _w(d) + _w(a)
          for i in ISCAS for d in DESMENTIDOS for a in FALHAS16]
    ok1 = [x for x in c1 if PISO_FALA[1] <= x <= TETO_FALA[1]]
    print("  cena 1: faixa real %d-%d | %d de %d combinacoes na banda %d-%d"
          % (min(c1), max(c1), len(ok1), len(c1), PISO_FALA[1], TETO_FALA[1]))
    if len(ok1) != len(c1):
        falhas.append("cena 1: %d de %d combinacoes FORA da banda %d-%d — o "
                      "orcamento tinha de fechar por construcao"
                      % (len(c1) - len(ok1), len(c1),
                         PISO_FALA[1], TETO_FALA[1]))
    for nome, pool in (("isca", ISCAS), ("desmentido", DESMENTIDOS),
                       ("falha", FALHAS16)):
        for x in pool:
            if not [1 for i in ISCAS for d in DESMENTIDOS for a in FALHAS16
                    if x in (i, d, a)
                    and PISO_FALA[1] <= _w(i.format(o=o_caro)) + _w(d) + _w(a)
                    <= TETO_FALA[1]]:
                falhas.append("cena 1 sem combinacao na banda para o %s %r"
                              % (nome, x[:34]))

    # ⛔⛔ ESTE BLOCO MEDIA O MOTOR ERRADO, e por isso o autoteste inteiro nunca
    # rodou ate' o fim neste agente. Herdado do porte de 24s, ele enumerava
    # REGRAS x MECANISMOS_FALA (cena 2 de la') e FUNDIDAS x CTAS x GATES (cena 3
    # de la') — e estourava `KeyError: 3` em `PISO_FALA[3]`, que num motor de
    # DUAS cenas nao existe. Resultado: `python -c "autoteste()"` morria antes
    # dos sorteios, e o numero que ele imprimia antes de morrer era sobre pools
    # que a cena 2 do 16s NAO USA.
    # ⚠️ E' o modo de falha §16 na forma mais cara: lente que roda, imprime
    # numero e mede outra coisa. Agora enumera a cadeia REAL do `_montar_falas`.
    # ⚠️ REGRAS / MECANISMOS_FALA / FUNDIDAS / GATES continuam no arquivo: o
    # `_ex2_regra` e o `CONTROLE_REGRA` ainda os usam como controle da lente.
    # Eles nao alimentam mais a fala — quem alimenta e' a familia `*16`.
    # ⚠️ A tupla carrega os QUATRO beats agora, nao dois: depois da reforma o
    # CTA e o FOLLOW tambem tem contrato de tamanho, e "quantos mecanismos
    # cabem" nunca foi a pergunta inteira. ⛔ Entrada que nunca cabe nao e'
    # rara, e' morta (licoes §36) — e isso vale para os quatro pools.
    c2 = [(_w(m.format(o=o_caro)) + _w(d.format(par=p)) + _w(c) + _w(f),
           m, d, c, f)
          for m in MECANISMOS16 for d in DISCLOSURES16 for p in PARES16
          for c in CTAS for f in FOLLOWS16]
    ok2 = [x for x in c2 if PISO_FALA[2] <= x[0] <= TETO_FALA[2]]
    print("  cena 2: faixa real %d-%d | %d de %d na banda %d-%d"
          % (min(x[0] for x in c2), max(x[0] for x in c2), len(ok2), len(c2),
             PISO_FALA[2], TETO_FALA[2]))
    print("          %d/%d mecanismos · %d/%d disclosures · %d/%d CTAs · "
          "%d/%d follows alcancaveis"
          % (len({x[1] for x in ok2}), len(MECANISMOS16),
             len({x[2] for x in ok2}), len(DISCLOSURES16),
             len({x[3] for x in ok2}), len(CTAS),
             len({x[4] for x in ok2}), len(FOLLOWS16)))
    if len(ok2) != len(c2):
        falhas.append("cena 2: %d de %d combinacoes FORA da banda %d-%d — o "
                      "orcamento tinha de fechar por construcao"
                      % (len(c2) - len(ok2), len(c2),
                         PISO_FALA[2], TETO_FALA[2]))
    for rot, idx, pool in (("mecanismo", 1, MECANISMOS16),
                           ("disclosure", 2, DISCLOSURES16),
                           ("CTA", 3, CTAS), ("follow", 4, FOLLOWS16)):
        for x in pool:
            if not [1 for y in ok2 if y[idx] == x]:
                falhas.append("cena 2: o %s %r nunca cabe na banda"
                              % (rot, x[:34]))


def autoteste(n_por_pagina=80, seed=7):
    falhas = []
    _contrato_dos_pools(falhas)

    tamanhos = {"NARRADORAS": len(NARRADORAS),
                "HOMENS_SEM_ROSTO": len(HOMENS_SEM_ROSTO),
                "VARANDAS": len(VARANDAS), "MESAS": len(MESAS),
                "CAIXAS": len(CAIXAS), "DESPEJOS": len(DESPEJOS),
                "REACOES": len(REACOES), "MECANISMOS": len(MECANISMOS)}
    for nome, n in sorted(tamanhos.items()):
        if n < MIN_OPCOES:
            falhas.append("eixo visual %s com %d opcoes (minimo %d)"
                          % (nome, n, MIN_OPCOES))
    copy = {"ISCAS": len(ISCAS), "DESMENTIDOS": len(DESMENTIDOS),
            "FALHAS16": len(FALHAS16), "REGRAS": len(REGRAS),
            "MECANISMOS_FALA": len(MECANISMOS_FALA), "FUNDIDAS": len(FUNDIDAS),
            "CTAS": len(CTAS), "GATES": len(GATES),
            # ⭐ os pools que de fato alimentam a cena 2 do 16s. Sem eles o
            # relatorio listava oito pools e nenhum deles era o que sai no
            # video — relatorio que nao cita quem fala nao serve de inventario.
            "MECANISMOS16": len(MECANISMOS16),
            "DISCLOSURES16": len(DISCLOSURES16), "PARES16": len(PARES16),
            "FOLLOWS16": len(FOLLOWS16)}
    for nome, piso in sorted(MIN_COPY.items()):
        if copy[nome] < piso:
            falhas.append("pool de copy %s com %d entradas (minimo %d)"
                          % (nome, copy[nome], piso))

    _viabilidade(falhas)

    # --- os sorteios --------------------------------------------------------
    rng = random.Random(seed)
    freq, total_eixo, erros, avisos, n = {}, {}, 0, 0, 0
    palavras = {1: [], 2: [], 3: []}
    estouros = 0
    for pag in sorted(ETNIA):
        ledger = {}
        for _ in range(n_por_pagina):
            spec = sortear(pag, rng, ledger)
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
            for eixo in EIXOS_VISUAIS:
                freq.setdefault(eixo, {})
                freq[eixo][spec[eixo]["id"]] = freq[eixo].get(spec[eixo]["id"], 0) + 1
                total_eixo[eixo] = total_eixo.get(eixo, 0) + 1
            for i, fala in enumerate(spec["falas"], 1):
                w = _palavras(fala)
                palavras[i].append(w)
                if w > TETO_FALA[i]:
                    estouros += 1
            _anotar(ledger, spec)
            n += 1

    print("\nENTROPIA — %d sorteios (%d por pagina)" % (n, n_por_pagina))
    print("-" * 72)
    for chave in sorted(freq):
        c = freq[chave]
        topo, qtd = max(c.items(), key=lambda kv: kv[1])
        pc = qtd / float(total_eixo[chave])
        marca = "OK " if pc <= TETO_FREQ else "X  "
        print("  %s %-20s %2d opcoes | mais sorteado %-22s %4.1f%% (teto %.0f%%)"
              % (marca, chave, len(c), topo, pc * 100, TETO_FREQ * 100))
        if pc > TETO_FREQ:
            falhas.append("eixo %s concentra %.1f%% em '%s' (teto %.0f%%)"
                          % (chave, pc * 100, topo, TETO_FREQ * 100))

    print("\nUSO DO ORCAMENTO — medido contra a CAPACIDADE REAL, nao contra o teto")
    print("-" * 72)
    # capacidade real de um take cheio de 8s: 27-32 palavras (3,4-4,0 p/s, medido
    # no ESCANDALO). ⚠️ A cena 3 no teto da doutrina pede 4,25 p/s — a tensao 🔴
    # aberta da EX12, decisao do Ed.
    # ⛔ O SEGUNDO RESQUICIO DA CENA 3, e ele derrubava o autoteste na ultima
    # linha: `palavras[3]` existe como lista VAZIA e `sum([])/0` estoura. O
    # laco agora sai do proprio TETO_FALA, que e' quem sabe quantas cenas o
    # motor tem — numero de cenas cravado a mao envelhece a cada porte.
    capacidade = {1: (27, 32), 2: (27, 32)}
    tot = 0.0
    for i in sorted(TETO_FALA):
        v = palavras[i]
        media = sum(v) / float(len(v))
        tot += media
        print("  cena %d: min %2d · media %4.1f · max %2d | piso %d teto %d | "
              "capacidade real %d-%d (%.0f%% · %.2f p/s na media)"
              % (i, min(v), media, max(v), PISO_FALA[i], TETO_FALA[i],
                 capacidade[i][0], capacidade[i][1],
                 100.0 * media / capacidade[i][1], media / 8.0))
    # ⚠️ ERA `faixa da doutrina 82-%d` e `tot / 24.0` — as duas mentiam desde o
    # porte. Este motor tem DOIS takes de 8s: o video dura 16 segundos e o teto
    # e' 50 palavras, nao a faixa 82-96 do arco de 24s. Dividir por 24 imprimia
    # 1,96 p/s onde a taxa real e' 2,94 — e taxa e' justamente o numero que
    # decide se a fala e' cortada no render.
    print("  video: media %.1f palavras (teto %d) · %.2f p/s em 16s"
          % (tot, TETO_TOTAL, tot / 16.0))
    print("  ESTOURO DE TETO em %d sorteios: %d cena(s)" % (n, estouros))
    if estouros:
        falhas.append("%d cena(s) acima do TETO_FALA em %d sorteios"
                      % (estouros, n))

    print("\nPOOLS DE COPY")
    print("-" * 72)
    for nome in sorted(copy):
        print("  %-16s %d" % (nome, copy[nome]))

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


def stats():
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
    return autoteste()


def main():
    ap = argparse.ArgumentParser(
        description="Randomizador do agente EXTERIOR SHORT")
    ap.add_argument("--pagina", choices=sorted(ETNIA))
    ap.add_argument("--n", type=int, default=1)
    ap.add_argument("--seed", type=int, help="reproduzivel")
    ap.add_argument("--dry-run", action="store_true", help="nao grava ledger")
    ap.add_argument("--stats", action="store_true",
                    help="uso dos pools + self-test de entropia")
    a = ap.parse_args()

    if a.stats:
        return stats()

    if not a.pagina:
        ap.error("informe --pagina <joe|ray|matt|marcus|chuck> (ou --stats)")

    rng = random.Random(a.seed)
    ledger = _carregar_ledger()
    saida = 0
    for i in range(a.n):
        spec = sortear(a.pagina, rng, ledger)
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
