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

⭐⭐ REFORMA DE COPY 16s — 2026-08-10 (CONTRATO-COPY-16S.md)
-----------------------------------------------------------
Ordem do operador: *"agentes troca16 ... precisam de reformulacao total de suas
copys"*. A copy FALADA foi reescrita inteira (pools + solver); a CENA nao foi
tocada — nenhum bloco IMAGE/TAKE e nenhum pool visual mudou uma virgula.
O que a reforma trocou, e o numero medido antes dela em 200 sorteios:

    CT1 (100%)  o follow deixou de ser a ULTIMA coisa no ouvido e passou a vir
                ANTES do CTA; o video termina no pedido.
    CT2  (78%)  o desmentido passou a carregar a FALHA com dano concreto e
                numero, em 2a pessoa (`You lose it ten minutes in.`).
    CT3  (55%)  `gelatin trick` deixou de ser rotulo nu: toda entrada leva
                verbo de efeito + alvo (o sangue/a pressao chegando ao orgao).
    CT4 (100%)  UM apelido do orgao por video, repetido nos dois takes —
                reverte a rotacao herdada do motor de 24s.
    CT6  (95%)  o CTA diz ONDE a receita chega (`to your messages`).
    CT7   (0%)  verbo de ereccao colado no orgao saiu do take 2 (claim nosso);
                no take 1 ele fica, porque ali E' a isca que o video desmente.

E duas correcoes de fundo que vieram junto: a promessa da isca deixou de ser
TAMANHO e passou a ser DURACAO (a VSL vende recuperacao de ereccao, nao
aumento), e `soldier` saiu do NUCLEO por ser britanismo em ouvido americano.

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
# ⛔ LEDGER PROPRIO: 24s e 16s sao lotes diferentes.
LEDGER = os.path.join(AQUI, ".troca-16-ledger.json")

TITULO = "AGENTE TROCA 16"
SUBTITULO = "o proxy sai, o mecanismo entra no mesmo ponto do quadro · 3 cenas"
SLUG = "troca-16"

# ⚠️ Os rotulos dizem os BEATS DA FALA, nao so' o que se ve': depois da reforma
# de copy 16s (2026-08-10) a cena 1 nao e' so' a crendice — ela desmente e
# ENUNCIA A FALHA (CT2); e a cena 2 termina no CTA, com o follow ANTES (CT1).
CENAS_UI = ["1 · A CRENDICE + O DESMENTIDO COM A FALHA",
            "2 · O CORPO-PROVA + A TROCA NA FALA + FOLLOW + CTA"]

# TR14. ⚠️ O ORCAMENTO E' PISO **E** TETO — ordem do operador. Tratar o piso
# como "julgamento que mora na doutrina" foi o que deixou 48% das cenas 2
# abaixo dele: piso nao cobrado e' piso que nao existe. Os dois sao mecanicos e
# moram aqui.
# ⛔ 34 estava ACIMA DO FISICO (32 = 8s a 4,0 palavras/s, licoes §5).
# Nao estourava por sorte do pool — o maximo GERADO medido em 600
# sorteios era 32. Mas teto declarado acima da capacidade e' bomba
# armada: o lint compara com ESTE numero, entao aprovaria a primeira
# entrada longa que alguem acrescentasse, e a fala sairia cortada no
# render sem ninguem ver (licoes §27). Baixado em 2026-08-04.
# ⛔⛔ TETO 25 — ordem permanente do operador, 2026-08-05: *"sempre meca. Nao
# pode haver cortes de fala."* O numero vem de RENDER, nao de conta: 32
# cortou e 28 cortou. Os exemplos que ele escreve a mao vivem em 16-25
# palavras (2,0-3,1 p/s). Ver licoes-de-construcao §28.
# ⭐⭐ MODOS DE REF — contrato compartilhado (short_comum), 2026-08-05.
# Toggles de `ref bela` (super model, corpo escultural, pouca roupa,
# olhos fora do comum) e `ref forte` (homem musculoso e atraente).
# ⛔ Desligados, o prompt volta IDENTICO ao de antes do recurso.
MODO_BELA = True
MODO_FORTE = True

# ⭐ DUAS CENAS. O teto vem da fisica (8s x 3,1 p/s).
# ⛔⛔ E O PISO DA CENA 2 ERA 26 COM TETO 25 no motor de 24s — par
# impossivel, em que todo sorteio viola um dos dois. Testei se era ele que
# congelava a cena (15 falas distintas em 300) e NAO era: com piso 18, 20,
# 22 ou 25 o numero nao muda. A causa e' outra e esta' registrada no
# `_montar_falas`. Mas o par continua sendo declaracao contraditoria, e
# aqui ele nasce coerente.
TETO_FALA = {1: 22, 2: 25}
# ⚠️⚠️ O PISO DA CENA 2 CAIU DE 20 PARA 18 EM 2026-08-10, e a queda e'
# CONSEQUENCIA MEDIDA, nao afrouxamento: com o beat do follow fora da fala
# (CT8), a cena 2 perdeu 3-4 palavras e passou a bater no piso antigo em
# 130 de 400 sorteios. Piso calibrado com um beat que nao existe mais e'
# alarme que sempre dispara, e alarme que sempre dispara ensina a ignorar
# o linter inteiro. 18 palavras em 8s dao 2,25 p/s — dentro da faixa em
# que o operador escreve a mao (16-25).
PISO_FALA = {1: 16, 2: 18}

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

# ###########################################################################
# ⭐⭐⭐ REFORMA DE COPY 16s — 2026-08-10 (CONTRATO-COPY-16S.md)
# ###########################################################################
# ⛔ ORDEM DO OPERADOR: *"agentes troca16 ... precisam de reformulacao total de
# suas copys"*. A copy antiga deste motor foi MEDIDA em 200 sorteios e violava
# cinco das sete travas:
#
#     CT1 sentenca depois do CTA ........ 100%   (o gate fechava o video)
#     CT2 take 1 sem falha enunciada .....  78%
#     CT3 `gelatin trick` sem razao ......  55%
#     CT4 apelido do orgao muda no corte . 100%
#     CT6 CTA sem endereco de entrega ....  95%
#
# ⭐ O QUE MUDOU, beat a beat:
#
#   cena 1 = CRENDICE (a isca absurda) + DESMENTIDO **COM A FALHA DELE**
#            A promessa da isca deixou de ser TAMANHO (`ten times bigger`,
#            `grow a full inch`) e passou a ser DURACAO/ERECCAO — a VSL vende
#            recuperacao, nao aumento, e hook que promete o que a VSL nao
#            entrega queima a pagina. E o desmentido, que era so' desmentido,
#            passa a carregar o DANO CONCRETO em 2a pessoa (`You lose it ten
#            minutes in.`), que e' o CT2.
#            ⚠️ A falha e' do ESPECTADOR, nao de um `he`: nas cenas 1 e 2 o
#            elenco e' 1 (TR13) e um `He'd lose it` ali e' pronome sem dono —
#            a lente T16-5b reprova, e com razao.
#
#   cena 2 = TROCA (gesto + mecanismo COM RAZAO) -> FOLLOW -> CTA   <- FIM
#            A ordem inverteu: o `gate` (follow) era a ULTIMA coisa no ouvido,
#            colada no unico pedido que gera receita. Agora ele vem ANTES, e o
#            video termina no pedido (CT1).
#
# ⚠️ O ORCAMENTO E' O QUE MANDA NO TAMANHO DAS ENTRADAS (teto 25):
#            troca 10-11 | follow 3-5 | CTA 8-9   ->  pior caso 25, melhor 21
#     Pool cujas entradas variam de 6 a 14 palavras num teto de 25 nao e' pool
#     de 12, e' pool de 4 com oito enfeites: as longas nunca sao sorteadas. Por
#     isso cada pool aqui nasce com FAIXA ESTREITA, e o [ALCANCE] mede.
# ###########################################################################

# ---------------------------------------------------------------------------
# ⭐⭐ A TROCA, AGORA NA FALA — o pool que substitui FUNDIDAS no formato 16s
# ---------------------------------------------------------------------------
# ⛔⛔ DECISAO DO OPERADOR, 2026-08-08, com as duas opcoes medidas na mesa.
# Este e' o UNICO dos cinco portes em que as cenas 2 e 3 NAO FUNDEM, e por duas
# razoes que estao escritas no proprio motor de 24s:
#
#   1. A cena 3 e' o BLOCO MAIS ARRISCADO DO LOTE — a regra de que ela deriva
#      custou QUATRO recusas deterministicas, e o recibo de 42 palavras foi
#      removido dela porque *"densidade e' superficie de bloqueio"*. Trazer a
#      bancada da cena 2 para la' e' recriar o que ja' foi pago em recusa.
#   2. AS DUAS DISPUTAM QUEM SEGURA O PROXY. Na cena 2 ele esta' no punho DELA
#      — ela precisa largar para a troca acontecer no mesmo ponto do quadro. Na
#      cena 3 esta' na mao DELE, e isso e' a F12b: a agencia tem de ser dele.
#      Nao ha' frame que comporte as duas coisas.
#
# ⭐ O operador escolheu o CORPO-PROVA. A troca deixa de acontecer na tela e
# passa a existir aqui, na fala — este pool E' essa mudanca.
#
# ⛔ TODA ENTRADA FAZ TRES COISAS, e as tres sao cobradas por lente:
#   · o GESTO de largar (`Drop that`, `Wrong jar`, `Set that down`) — e' o que
#     resta do bit visual, e sem ele a cena 2 vira um mecanismo qualquer;
#   · o literal `gelatin trick`;
#   · o ORGAO, que o TESTEMUNHO carregava e que morreu no orcamento.
#
# ⚠️ DEZ A ONZE PALAVRAS, e o numero e' ARITMETICA: o CTA com cobertura custa
# 8-9 e o follow 3-5, entao sobram 11. A primeira versao tinha 9-12 palavras e
# matou VINTE E QUATRO entradas dos tres pools — 2% de cobertura.
#
# ⭐⭐ CT3 — O ROTULO NU MORREU. As entradas antigas eram `The gelatin trick
# wakes your {o}` / `... is your {o}'s way back`: nome de mecanismo sem RAZAO
# ao lado nao vira crenca, vira ruido de marca (55% dos sorteios reprovavam).
# Agora toda entrada carrega VERBO DE EFEITO + ALVO na MESMA sentenca do
# literal, e o alvo e' o sangue/a pressao chegando ao orgao — que e' o que a
# VSL vende.
#
# ⛔⛔ CT7 — VERBO DE ERECCAO COLADO NO ORGAO SAIU DAQUI. `wakes`, `hardens`,
# `straightens`, `is your {o}'s way back` descrevem o ORGAO voltando a
# funcionar, e essa e' a licao paga em campo no COLO 16: ~95% de recusa do
# gerador. Sobre o CORPO e o SANGUE passa; sobre o ORGAO nao. A excecao da isca
# absurda vale so' para o TAKE 1 (a promessa que o video desmente), nunca aqui,
# onde o claim e' NOSSO.
#
# ⛔ `his {o}` saiu das duas entradas que o traziam: na cena 2 nao ha' homem em
# quadro (elenco 1, TR13) e `his` ali e' pronome sem dono.
#
# ⛔ TODA ENTRADA CONTINUA FAZENDO TRES COISAS, cobradas por lente:
#   · o GESTO de largar (`Drop that`, `Wrong jar`, `Leave it`) — e' o que resta
#     do bit visual, e sem ele a cena 2 vira um mecanismo qualquer;
#   · o literal `gelatin trick`;
#   · o ORGAO, que o TESTEMUNHO carregava e que morreu no orcamento.
TROCAS16 = [
    "Drop that. The gelatin trick puts blood back in your {o}",
    "Forget that. The gelatin trick opens blood flow to your {o}",
    "Put that down. The gelatin trick fills your {o} with blood",
    "Not that. The gelatin trick holds blood inside your {o}",
    # ⚠️ `Wrong jar.` MORREU NO OUVIDO, 2026-08-10 — e o frame prova: no IMAGE
    # 02/02 montado nao ha' pote nenhum, o que existe em quadro e' o PROXY com
    # a substancia por cima, nas maos dele. `Wrong jar` aponta para um objeto
    # que o video nao mostra, e o gesto so' funciona se o espectador achar o
    # que largar. `Wrong stuff` aponta para a substancia, que esta' la'.
    "Wrong stuff. The gelatin trick feeds blood to your {o}",
    # ⚠️ `clears the path to your {o}` MORREU NO TESTE WTF, 2026-08-10: caminho
    # de QUE? Todas as outras treze entradas nomeiam o sangue; esta nomeava um
    # caminho vazio e passava na CT3 so' porque `clears` esta' na lista de
    # verbos e o orgao conta como alvo. Lente que aprova a forma sem cobrar a
    # funcao e' o modo de falha da casa.
    "Leave that. The gelatin trick carries blood down to your {o}",
    "Skip that. The gelatin trick keeps blood in your {o} longer",
    "That failed. The gelatin trick restores pressure to your {o}",
    "Set that down. The gelatin trick brings blood into your {o}",
    # ⚠️ `unblocks blood to your {o}` nao e' ingles falado — desbloqueia-se o
    # CAMINHO, nao o sangue. Trocado por `unblocks the flow to your {o}`:
    # mesmo verbo (continua na VERBOS_EFEITO_16), `flow` e' ALVO_16, e o custo
    # sobe de 10 para 11, dentro da faixa.
    "Drop it. The gelatin trick unblocks the flow to your {o}",
    "Forget it. The gelatin trick pushes blood into your {o}",
    "That did nothing. The gelatin trick fixes your {o}'s blood supply",
    "Not that one. The gelatin trick moves blood into your {o}",
    "Leave it. The gelatin trick gives your {o} its blood back",
]

# ⛔⛔ `soldier` FOI APOSENTADO — 2026-08-10, reforma de copy 16s.
# Nao e' gosto: `soldier` para o orgao e' britanismo, e num ouvido americano de
# 50-70 anos ele soa a filme de guerra, nao a apelido de banheiro. Entrou no
# lugar `manhood`, que ja' tem grafia sonora validada no `nucleo_sonoro`
# (`man-hood`) — ou seja, a troca nao cria termo sem cobertura de TTS.
# ⚠️ O TAMANHO DO POOL NAO CAIU: cinco antes, cinco depois.
NUCLEO = ["Johnson", "pecker", "wiener", "tool", "manhood"]


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
# ⭐ TERCEIRA FORMULACAO — ORDEM DO ED, 2026-08-01, olhando os renders.
# A tensao acima ("homem de pe' nao tem colo") saiu do papel: `beside the lap`
# e' coordenada de homem SENTADO, e num homem DE PE o Veo resolvia o `beside`
# ao pe' da letra — o legume saia na altura do quadril, deslocado para o lado,
# numa mao so'. Lido em oito renders: nao le' como prolongamento, le' como
# sujeito segurando uma compra.
#
# O que o operador pediu, e por que cada pedaco esta' aqui:
#   · DUAS MAOS, uma acima da outra — e' o que traz o objeto para o eixo do
#     corpo e o mantem la'. Uma mao so' deixa o Veo escolher o lado.
#   · `centred against the front of` no lugar de `beside` — `beside` empurra
#     para fora, `centred against` e' coordenada, nao vizinhanca.
#   · base encostada no tecido + ponta para cima — e' o que faz ler como
#     PROLONGAMENTO em vez de objeto carregado.
# ⛔ Continua sem `groin`/`pubic`/`crotch`: a coordenada e' dada pela PECA DE
# ROUPA (`the front of his khaki work pants`), que e' a mesma alavanca que fez
# `beside the lap of his khaki shorts` passar onde `level with his groin` foi
# recusado. Trocou-se a geometria, nunca o termo.
# ⚠️ A AGENCIA da F12b fica INTEIRA e ate' reforcada: duas maos dele, no corpo
# dele, e ela segue apontando sem encostar. O que derrubou as 4 recusas de
# 2026-07-30 foi mao de TERCEIRO em corpo passivo — nao e' o caso.
# Slots: peca da calca, proxy (ancorado NELE), relacao.
TR_MAO_PROPRIA_IMAGE = (
    # ⚠️ ORDEM DA FRASE: os punhos vem ANTES do proxy. A descricao do proxy e'
    # longa (cor, escala, substancia) e, posta entre `he holds` e `in both his
    # own fists`, saia "the mustard still on it in both his own fists" — a
    # substancia lida como estando nas maos. Verbo, maos, objeto, geometria.
    # ⚠️ E o `upright` saiu: `the tip pointing straight up` ja' o diz, e ele
    # aterrissava colado no fim da descricao do proxy ("the mustard still on it
    # upright"). Travessao separa a descricao longa da geometria (F12c: uma
    # palavra a menos neste bloco e' superficie de bloqueio a menos).
    "Centred against the front of his %s, in both his own fists one stacked "
    "above the other, he holds %s — the base of it resting on the fabric, the "
    "tip pointing straight up. Standing beside him, %s points one finger down "
    "at it without touching him, talking straight to camera."
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
    "on the lens and never speaks; both his own fists stay where they are. The "
    "%s in his own fists stays exactly as it appears in the first frame — completely "
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
     "rotulo": "29y · ruiva longa + sardas no rosto",
     "marca": "a heavy dusting of freckles across her nose and cheeks and long copper-red hair",
     "roupa": "a cropped white ribbed tank top and high-waisted jeans"},
    {"id": "afro_curto", "idade": 34,
     "rotulo": "34y · afro curto + pinta no malar",
     "marca": "a short natural afro and a small dark beauty mark high on her left cheekbone",
     "roupa": "a cropped mustard knit top and a thin gold chain"},
    {"id": "loira_raiz", "idade": 41,
     "rotulo": "41y · loira com raiz + covinha funda",
     "marca": "long honey-blonde hair with grown-out roots and a deep dimple in her right cheek",
     "roupa": "a cropped black t-shirt and large gold hoop earrings"},
    # ⚠️ 2026-08-13: a FALHA ENTRE OS DENTES saiu — mesma familia do dente
    # lascado que fez o operador reprovar o lote do PLACA 16 (*"esses caras
    # tao parecendo mendigo"*). A ancora facial continua obrigatoria, so' que
    # do lado bonito.
    {"id": "rabo_alto", "idade": 30,
     "rotulo": "30y · rabo preto alto + pinta no olho",
     "marca": "jet-black hair in a high slicked-back ponytail and a small beauty mark at the outer corner of her left eye",
     "roupa": "a cropped grey sweatshirt cut off above the waist"},
    {"id": "oculos_especialista", "idade": 37,
     "rotulo": "37y · escura media + oculos dourados",
     "marca": "shoulder-length dark hair, thin gold-rimmed glasses and a narrow widow's peak",
     "roupa": "a cropped olive button-up shirt knotted at the front"},
    {"id": "tranca_caixa", "idade": 31,
     "rotulo": "31y · box braids longas + batom ameixa",
     "marca": "waist-length box braids and dark plum lipstick",
     "roupa": "a cropped burgundy tank top and stacked gold bangles"},
    {"id": "grisalha_coque", "idade": 45,
     "rotulo": "45y · coque grisalho + linhas de riso",
     "marca": "silver-streaked dark hair in a loose bun and deep laugh lines at the outer corners of her eyes",
     "roupa": "a cropped denim shirt knotted at the waist"},
    {"id": "bob_platinado", "idade": 28,
     "rotulo": "28y · bob platinado + argola no nariz",
     "marca": "a bleached-platinum bob cut sharp at the jaw and a small hoop in her left nostril",
     "roupa": "a cropped lilac zip-up and gold rings on three fingers"},
    {"id": "franja_reta", "idade": 33,
     "rotulo": "33y · castanha com franja + marca na testa",
     "marca": "long chestnut hair with a blunt fringe and a small crescent birthmark at her right temple",
     "roupa": "a cropped rust-orange top and a heavy gold pendant"},
    {"id": "cachos_bronze", "idade": 39,
     "rotulo": "39y · cachos acaju + sombra bronze",
     "marca": "tight auburn-dyed curls and metallic bronze eyeshadow",
     "roupa": "a cropped emerald wrap top and long gold drop earrings"},
    # ⛔ `baby tee` saiu: e' o token `baby` entrando de graca num prompt que ja'
    # pareia mulher jovem com homem de 51-65 e objeto falico — mesma mecanica de
    # `clothed`/`celebrity`. `ringer tee` e' a mesma peca.
    {"id": "morango_jovem", "idade": 28,
     "rotulo": "28y · loira morango + pinta no labio",
     "marca": "long wavy strawberry-blonde hair and a beauty mark just above her upper lip",
     "roupa": "a cropped pale-blue knit top and a thin gold chain bracelet"},
    {"id": "tapered_macas", "idade": 43,
     "rotulo": "43y · corte tapered + malar alto",
     "marca": "a close tapered cut faded at the sides and high sharp cheekbones",
     "roupa": "a cropped charcoal turtleneck and heavy gold hoops"},
    {"id": "tranca_unica", "idade": 30,
     "rotulo": "30y · tranca unica + tatuagem de estrelas",
     "marca": "long jet-black hair in a single braid over one shoulder and a small dark tattoo of three stars behind her right ear",
     "roupa": "a cropped white crochet top and gold bangles"},
    {"id": "coque_bagunca", "idade": 36,
     "rotulo": "36y · coque desfeito + olhos verde-cinza",
     "marca": "sandy-blonde hair in a messy topknot and pale grey-green eyes under heavy dark brows",
     "roupa": "a cropped sage-green tank top and a slim gold watch"},
    # + 2026-08-02: mesma medicao que gerou o bloco dos CORPOS_PROVA logo
    # abaixo, so' que do lado da narradora — o operador viu SEMPRE O MESMO
    # ROSTO. As catorze acima descrevem a pessoa por CABELO mais uma ancora:
    # catorze mulheres descritas so' por cabelo sao a mesma mulher catorze
    # vezes, e o gerador devolvia quase a mesma cara. As cinco novas trazem os
    # eixos que este pool nao acionava:
    #   · PORTE — era 0/14 aqui. heavy-set, tall lean, short compact, full
    #     rounded, small wiry. E' o eixo que muda a silhueta no plano medio,
    #     que e' onde a narradora vive nas tres cenas.
    #   · OCULOS — armacao preta grossa e oculos de sol no cabelo (o pool so'
    #     tinha um fio de ouro em catorze).
    #   · PELE — sun-weathered, manchas de sol nas macas do rosto.
    #   · a ancora facial (P6) continua obrigatoria e sempre do lado ✅ de
    #     licoes-producao-veo §REF — DISTINTIVO, NUNCA DETERIORADO (cicatriz
    #     limpa, fenda no queixo, pinta). ⛔ dente lascado ficou de fora.
    #   · [D3] `cropped` no inicio da roupa nas cinco, como manda o pool.
    #   · zero mencao a etnia: a narradora do TROCA e' solta e nao recebe
    #     injecao de etnia nenhuma — a variacao mora no cabelo.
    # ⚠️⚠️ 2026-08-13, TRES REESCRITAS NESTE BLOCO. O comentario acima manda a
    # ancora vir "sempre do lado ✅ DISTINTIVO, NUNCA DETERIORADO" e depois
    # escreve `raised pale scar`, `sun-weathered skin`, `dark sun spots` e
    # `short vertical scar` — a regra estava no comentario e o contrario no
    # dado. E' exatamente o pool que o operador reprovou no PLACA 16 (*"esses
    # caras tao parecendo mendigo"*).
    # ⛔ Saem: cicatriz, pele castigada de sol e mancha de idade.
    # ✅ Entram no lugar: pinta, sarda e bronzeado leve — os MESMOS eixos
    # (`pele` e `ancora` do `medir_personagens`) continuam preenchidos, so'
    # que sem deterioracao. Trocar a palavra sem trocar o eixo e' o ponto:
    # zerar o eixo para "limpar" e' o outro modo de errar.
    {"id": "oculos_grossos_lenco", "idade": 47,
     "rotulo": "47y · bandana no cabelo + oculos grossos",
     "marca": "a heavy-set build, a faded bandana folded back over thick greying hair, thick black-framed glasses and a small dark mole at the outer end of her left eyebrow",
     "roupa": "a cropped rust-brown corduroy overshirt and one wide gold cuff on her right wrist"},
    {"id": "locs_alta_seca", "idade": 52,
     "rotulo": "52y · alta + locs presas + fenda no queixo",
     "marca": "a tall lean frame with narrow sloping shoulders, shoulder-length locs pulled back off her face, lightly tanned smooth skin and a deep cleft in her chin",
     "roupa": "a cropped sand-coloured linen shirt tied at the ribs and thin gold hoops"},
    {"id": "oculos_sol_baixinha", "idade": 35,
     "rotulo": "35y · baixinha + ondas claras + oculos sol",
     "marca": "a short compact build, dark sunglasses pushed up into thick sun-bleached waves, a wide flat nose and a dark mole under her right eye",
     "roupa": "a cropped faded-red sleeveless top and a chunky gold curb chain"},
    {"id": "cornrows_cheia", "idade": 44,
     "rotulo": "44y · porte cheio + cornrows + sardas",
     "marca": "a full rounded build, tight cornrows gathered into a low bun, freckles scattered across her cheekbones and a small beauty mark at the corner of her mouth",
     "roupa": "a cropped teal wrap top and two gold studs in her left ear"},
    {"id": "raspado_lateral", "idade": 49,
     "rotulo": "49y · lateral raspada + porte miudo",
     "marca": "a small wiry frame, dark hair worn long on one side and shaved close over the other ear, wide-set eyes and a dark mole low on her right jawline",
     "roupa": "a cropped oatmeal cable-knit sweater and thin gold rings on four fingers"},
    # -----------------------------------------------------------------------
    # + 2026-08-13: NOVE narradoras novas (19 -> 28). Ordem do operador:
    # *"melhore a aparencia e shape desses homens"* e *"aumente o pool de
    # opcoes substancialmente, tambem dos ambientes"*.
    # ⚠️ Dezenove entradas com um sorteio que so' evita as 3 ultimas devolvem
    # a mesma cara a cada quatro videos, e quem ve o lote inteiro de uma vez
    # e' o operador.
    # ⛔ DISTINTIVO, NUNCA DETERIORADO — zero `scar`, zero `gap between
    # teeth`, zero `sun spots`, zero `weathered`, zero `sunken`. As ancoras
    # sao pinta, covinha, mecha, argola, fenda no queixo, sarda.
    # ⛔ Zero palavra de aprovacao (`handsome`, `chiseled`, `rugged`): elogio
    # no prompt puxa o rosto para a media do banco de imagem, mesma mecanica
    # de `not a celebrity` invocar a celebridade. Descreve-se FEICAO.
    # ⛔ Zero cor de pele: a narradora do TROCA e' SOLTA na etnia [D2] e a
    # variacao mora no cabelo — cor aqui poe duas vozes no mesmo sintagma.
    # ⚠️ TRES DAS NOVE TEM OCULOS, de proposito. Este e' o unico dos tres
    # motores do grupo cujo pool feminino NAO tem excecao declarada em
    # `medir_personagens.EXCECOES`, entao o eixo `oculos` e' cobrado aqui: com
    # 3 em 19 ele estava em 16%, e as tres novas o levam a 6 em 28. E' armacao
    # de moda (clear-frame, cat-eye, espelhado no cabelo), nunca oculos de
    # leitura de meia-lua — a diferenca entre estilo e envelhecimento.
    # ⚠️ [D3] `cropped` no inicio da roupa, como manda o pool.
    # -----------------------------------------------------------------------
    {"id": "mecha_platina", "idade": 30,
     "rotulo": "30y · escura com mecha platinada",
     "marca": "a lean athletic build with cut shoulders, smooth-skinned, long dark hair with one bleached-platinum streak swept back from her left temple",
     "roupa": "a cropped ink-blue rib tank and a fine gold chain"},
    {"id": "pixie_cobre", "idade": 29,
     "rotulo": "29y · pixie cobre + sardas no rosto",
     "marca": "a compact strong build with a narrow waist, a short copper pixie cut swept off the forehead and a light dusting of freckles over her cheekbones",
     "roupa": "a cropped stone-grey tank top and small gold studs"},
    {"id": "oculos_finos_bob", "idade": 34,
     "rotulo": "34y · bob mel + oculos de aro fino",
     "marca": "a slim toned build, a blunt honey-blonde bob cut level at the jaw and thin clear-framed glasses over wide green eyes",
     "roupa": "a cropped sand-coloured linen shirt tied at the ribs and thin gold hoops"},
    {"id": "bantu_knots", "idade": 31,
     "rotulo": "31y · bantu knots + argola no nariz",
     "marca": "a firm compact build with toned shoulders, lightly tanned, dark hair set in bantu knots in even rows and a small gold hoop through her left nostril",
     "roupa": "a cropped ivory rib tank and a flat gold collar"},
    {"id": "oculos_gatinho", "idade": 37,
     "rotulo": "37y · alta + oculos gatinho + covinha",
     "marca": "a tall long-limbed frame, mid-length dark hair tucked behind one ear and tortoiseshell cat-eye glasses over a deep dimple in her right cheek",
     "roupa": "a cropped rust rib tank and a slim gold watch"},
    {"id": "rabo_trancado", "idade": 28,
     "rotulo": "28y · rabo trancado + ombros largos",
     "marca": "a strong build with square shoulders, a long braided ponytail pulled high and a beauty mark just below her right eye",
     "roupa": "a cropped plum knit top and gold drop earrings"},
    {"id": "oculos_sol_locs", "idade": 40,
     "rotulo": "40y · locs longas + oculos espelhados",
     "marca": "a full rounded build, smooth-skinned, long slim locs gathered back off her face and mirrored sunglasses pushed up on her head",
     "roupa": "a cropped teal wrap top and stacked gold bangles"},
    {"id": "loira_manteiga", "idade": 35,
     "rotulo": "35y · loira manteiga + oculos dourados",
     "marca": "a broad-shouldered athletic build with a flat midriff, freckled across the nose, butter-blonde hair cut blunt at the shoulder, slim gold wire-frame glasses and a small mole above her left brow",
     "roupa": "a cropped white ribbed tank top and high-waisted jeans"},
    {"id": "coils_puff", "idade": 33,
     "rotulo": "33y · coils em puff + oculos pretos",
     "marca": "a short powerful build with defined arms, dark hair in tight coils gathered back into a low puff, square black-framed glasses and a small cleft in her chin",
     "roupa": "a cropped scarlet knit top and a gold cuff"},
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
    # + 2026-08-02: o operador mediu os dois pools e viu SEMPRE O MESMO ROSTO.
    # As doze acima descrevem o corpo-prova quase so' por CABELO mais uma
    # ancora — doze homens descritos so' por cabelo sao o mesmo homem doze
    # vezes, e o gerador devolvia quase a mesma cara. As tres novas trazem os
    # eixos que este pool nao acionava:
    #   · 52 — OCULOS, o eixo ZERADO aqui (0/12): oculos de leitura baixos no
    #     nariz, mais entrada de cabelo recuada e orelha entalhada.
    #   · 54 — PORTE (ombros caidos) mais PELO FACIAL de costeleta.
    #   · 62 — PORTE de rosto (mandibula larga e quadrada) mais PELE castigada
    #     de sol e barba por fazer.
    #   · a ancora e' sempre do lado ✅ de licoes-producao-veo §REF —
    #     DISTINTIVO, NUNCA DETERIORADO (cicatriz limpa, orelha entalhada).
    #   · ⛔ nenhuma diz postura: `stooped`/`curvado` colide com a travada da
    #     F12b, que ja' escreve `upright, chin level` na mesma sentenca do
    #     IMAGE 03. Ombro caido e' FORMA do ombro, nao postura.
    #   · o espelho por indice com o pool ESCURA (mesma idade, mesma roupa,
    #     mesma calca) esta' mantido nas tres.
    #   · zero mencao a etnia: o motor injeta ETNIA[pagina] antes da marca.
    {"id": "leitura_orelha", "idade": 52,
     "marca": "a receding sandy hairline, reading glasses low on his nose and a notched left ear",
     "roupa": "a short-sleeve grey chambray shirt buttoned to the collar",
     "calca": "dark green work trousers"},
    {"id": "costeleta_cicatriz", "idade": 54,
     "marca": "sloping shoulders, thick rust-red sideburns and a raised scar along his left jaw",
     "roupa": "a washed-out teal work shirt with the top button open",
     "calca": "sand-coloured duck trousers"},
    {"id": "mandibula_sol", "idade": 62,
     "marca": "a broad square jaw under close grey stubble, sun-weathered skin and a horseshoe scar at his hairline",
     "roupa": "a dark brown short-sleeve utility shirt",
     "calca": "faded grey denim jeans"},
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
    # + 2026-08-02: o espelho das tres novas do pool CLARA — mesma medicao (o
    # operador viu sempre o mesmo rosto, porque as doze acima descreviam a
    # pessoa quase so' por cabelo), mesmos eixos novos, mesma idade, mesma
    # roupa e mesma calca por indice. So' o descritor de cabelo/barba muda,
    # que e' onde a etnia se le' [D2].
    #   · 52 — OCULOS (eixo ZERADO aqui) mais entrada recuada e orelha entalhada.
    #   · 54 — PORTE (ombros caidos) mais PELO FACIAL de costeleta.
    #   · 62 — PORTE de rosto (mandibula larga) mais barba por fazer.
    {"id": "taper_leitura", "idade": 52,
     "marca": "a receding grey taper, reading glasses low on his nose and a notched left ear",
     "roupa": "a short-sleeve grey chambray shirt buttoned to the collar",
     "calca": "dark green work trousers"},
    {"id": "costeletas_grisalhas", "idade": 54,
     "marca": "sloping shoulders, thick grey muttonchop sideburns and a raised scar along his left jaw",
     "roupa": "a washed-out teal work shirt with the top button open",
     "calca": "sand-coloured duck trousers"},
    {"id": "ondas_mandibula", "idade": 62,
     "marca": "a broad square jaw under grey stubble, short grey waves and a horseshoe scar at his hairline",
     "roupa": "a dark brown short-sleeve utility shirt",
     "calca": "faded grey denim jeans"},
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
    # ⭐ O GEODUCK — ordem do operador, 2026-08-05: *"esta faltando um big
    # geoduck de proxy no agente troca"*. E' o proxy de maior semelhanca
    # anatomica do repertorio, e por isso o de maior risco de moderacao.
    # ⛔ DUAS TRAVAS DE FORMA, herdadas do EXTERIOR (regras EX7, pagas em
    # recusa): a peca e' o `siphon`, NUNCA `neck`; e no TAKE ele e' `the clam`,
    # nunca a especie nomeada. Quem editar esta entrada tem de manter as duas.
    {"id": "geoduck", "nome": "clam", "analogia": "squash",
     "img": "a very large whole geoduck clam, its thick siphon extending well past the shell, as long as her forearm",
     "img_dele": "a very large whole geoduck clam, its thick siphon extending well past the shell, as long as his forearm"},
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
    # -----------------------------------------------------------------------
    # + 2026-08-13: DEZ ambientes novos (14 -> 24). Ordem do operador:
    # *"aumente o pool de opcoes substancialmente, tambem dos ambientes"*.
    # ⚠️ Com 14 entradas e um sorteio que evita as 2 ultimas, o cenario voltava
    # a cada tres videos — e sete das catorze ja' diziam `kitchen` no `curto`,
    # que e' o unico traco do cenario que entra no Audio dos TAKE.
    # ⚠️ CLASSES DIFERENTES DE VERDADE, nao decoracao trocada: despensa, sala
    # de jantar, bar de porao, cozinha de rancho, cozinha de praia, varanda de
    # verao, bancada de acougueiro, galeria de apartamento, cozinha de
    # azulejo, cozinha de avo. ⚠️ Cinco delas sao as MESMAS do
    # `escandalo16_short` (bloco ES19), copiadas com as chaves DESTE pool.
    # ⚠️ CADA UMA TRAZ O AMBIENTE INTEIRO no nivel das vizinhas: superficie +
    # dois objetos de leitura + a BANDEIRA no `set`, `re_ancora` que
    # reestabelece o cenario na cena seguinte (sem ela metade do lote diz so'
    # "in the same kitchen" e a bandeira some), e `luz` propria.
    # ✅ Bandeira dos EUA em todas, em FORMA diferente cada vez — esta' no
    # catalogo, nao e' marca.
    # ⛔ `clay jugs` e nao `clay pots` no rancho: `pot` puxa `pot plant`, que e'
    # superficie de bloqueio sem funcao de leitura.
    # -----------------------------------------------------------------------
    {"id": "cozinha_azulejo", "bancada": "counter", "curto": "kitchen",
     "set": "an American kitchen with white square tile running up the wall behind the counter, a dish rack by the sink and a US flag decal on the window glass",
     "re_ancora": "the same tiled kitchen, the dish rack by the sink and the US flag decal still on the window glass",
     "luz": "bright flat daylight through the window over the counter."},
    {"id": "bancada_acougue", "bancada": "butcher block", "curto": "kitchen",
     "set": "a country American kitchen built around a heavy butcher block table, cast iron pans hanging on the wall and a US flag in a glass case on the shelf",
     "re_ancora": "the same butcher block kitchen, the cast iron pans on the wall and the US flag still in its case",
     "luz": "warm low daylight from a single window frame-left."},
    {"id": "cozinha_verao", "bancada": "prep counter", "curto": "cook porch",
     "set": "a screened summer cook porch with a long prep counter, jars of preserves on an open shelf and a US flag hanging from a bracket by the screen door",
     "re_ancora": "the same screened cook porch, the jars of preserves on the shelf and the US flag still on its bracket",
     "luz": "soft shaded daylight coming through the screens."},
    {"id": "porao_bar", "bancada": "bar top", "curto": "basement bar",
     "set": "a finished American basement with a home bar, a row of stools and shelves of glasses, a US flag pinned flat on the panelled wall",
     "re_ancora": "the same basement bar with the shelves of glasses, the US flag still pinned flat on the panelled wall",
     "luz": "warm light from two hanging bulbs over the bar."},
    {"id": "cozinha_apartamento", "bancada": "galley counter", "curto": "kitchen",
     "set": "a narrow apartment galley kitchen with pale cabinets on both sides and a city window at the end, a US flag magnet on the fridge",
     "re_ancora": "the same narrow galley kitchen with the city window at the end, the US flag magnet still on the fridge",
     "luz": "flat daylight from the window at the end of the galley."},
    {"id": "despensa", "bancada": "prep counter", "curto": "pantry",
     "set": "a walk-in pantry off an American kitchen with deep open shelves of glass jars, a narrow prep counter down one side and a US flag pinned to the edge of a shelf",
     "re_ancora": "the same pantry off the kitchen, the deep shelves of glass jars behind her and the US flag still pinned to the shelf edge",
     "luz": "warm overhead light with daylight spilling in from the kitchen door."},
    {"id": "cozinha_praia", "bancada": "counter", "curto": "kitchen",
     "set": "a bright coastal American kitchen with white beadboard cabinets, a window onto a wooden deck and a US flag on a short pole by the door",
     "re_ancora": "the same coastal kitchen, the wooden deck through the window and the US flag still on its short pole by the door",
     "luz": "high clean daylight bouncing off the white cabinets."},
    {"id": "sala_jantar", "bancada": "dining table", "curto": "dining room",
     "set": "an American dining room with a long oak table, a sideboard of stacked plates against the wall and a US flag on a short pole in the corner",
     "re_ancora": "the same dining room, the sideboard of stacked plates behind her and the US flag still on its short pole in the corner",
     "luz": "warm daylight from a tall window frame-left."},
    {"id": "cozinha_rancho", "bancada": "tiled counter", "curto": "kitchen",
     "set": "a southwestern American ranch kitchen with a hand-painted tiled counter, a row of clay jugs on the shelf above and a US flag hung flat above the door",
     "re_ancora": "the same ranch kitchen, the row of clay jugs on the shelf and the US flag still hung flat above the door",
     "luz": "hot dry daylight through a deep-set window frame-right."},
    {"id": "cozinha_avo", "bancada": "enamel-top table", "curto": "kitchen",
     "set": "an old-fashioned American kitchen built around an enamel-top table, a tall wooden pie safe against the wall and a US flag pinned above the doorway",
     "re_ancora": "the same old-fashioned kitchen, the tall wooden pie safe behind her and the US flag still pinned above the doorway",
     "luz": "soft late daylight through a lace-curtained window frame-left."},
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
    # -----------------------------------------------------------------------
    # + 2026-08-13: DEZ recibos novos (12 -> 22). Ordem do operador:
    # *"aumente o pool de opcoes substancialmente"*.
    # ⚠️ O pool efetivo NAO e' o tamanho da lista: o `_bancada_livre` corta
    # tudo que colide com a fala e com o `pote` da substancia, e so' entao
    # evita as recentes. Com doze entradas o que sobrava depois do filtro era
    # meia duzia, e o mesmo recibo voltava — ampliar aqui e' ampliar o que
    # sobra DEPOIS do filtro, que e' o numero que importa.
    # ⛔ `cabecas` declara o que a imagem deixa NOMEAVEL: e' o campo que faz o
    # sorteio evitar POR CONSTRUCAO que a boca cite o que a imagem tinha de
    # esconder. Recibo que repete a boca mostra dois ingredientes, nao tres.
    # ⛔ Zero marca legivel — FORMA no lugar de rotulo, e a ausencia declarada
    # pela AFIRMATIVA (`plain`), nunca por `with no label`.
    # -----------------------------------------------------------------------
    {"id": "mel_favo", "cabecas": ("honey",),
     "itens": "a squat jar of thick honey with a piece of comb in it, a wooden dipper and a folded linen cloth"},
    {"id": "curcuma_ralador", "cabecas": ("turmeric",),
     "itens": "a saucer of bright yellow powder, a fresh turmeric root on a wooden board and a small metal grater"},
    {"id": "melancia_faca", "cabecas": ("watermelon",),
     "itens": "a thick wedge of watermelon face-up on a board, a plain glass jar of pale grains and a bone-handled knife"},
    {"id": "abobora_sementes", "cabecas": ("pumpkin", "seed"),
     "itens": "a shallow dish of pumpkin seeds, a squat plain tin with the lid resting on it and a wooden scoop"},
    {"id": "bordo_lata", "cabecas": ("maple", "syrup"),
     "itens": "a plain tin jug of dark amber syrup, two stacked unlabelled tins and a long-handled spoon"},
    {"id": "alecrim_almofariz", "cabecas": ("rosemary",),
     "itens": "a bundle of fresh rosemary tied at the stems, a small stone mortar and a plain white saucer"},
    {"id": "linhaca_pote", "cabecas": ("flax", "seed"),
     "itens": "a wide-mouth jar of small brown seeds, a folded paper packet and a slotted wooden spoon"},
    {"id": "cravo_pires", "cabecas": ("clove",),
     "itens": "a saucer of dried cloves, a plain glass jar of coarse pale powder and a short wooden pestle"},
    {"id": "hortela_caneca", "cabecas": ("mint",),
     "itens": "a bunch of fresh mint standing in a glass of water, a plain tin of pale powder and a china teacup"},
    {"id": "damasco_tabua", "cabecas": ("apricot",),
     "itens": "a row of dried apricots on a wooden board, a plain amber jar of clear liquid and a wooden butter knife"},
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
     "plantado": "a shallow white bowl of firm vivid purple gelatin cut into cubes, each cube wobbling slightly",
     "curto": "the shallow white bowl of vivid purple gelatin cubes",
     "pousado": "uncovered, its serving spoon lying on the board beside it"},
    {"id": "pote_firme",
     "plantado": "a clear glass jar of gelatin already set firm and vivid purple",
     "curto": "the glass jar of set vivid purple gelatin",
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
     "plantado": "a small enamel saucepan of warm vivid purple gelatin with a spoon standing in it",
     "curto": "the enamel saucepan of warm vivid purple gelatin",
     "pousado": "already open, its lid lying face-up on the board beside it"},
    {"id": "pires_cubos",
     "plantado": "three firm vivid purple gelatin cubes stacked on a small white saucer",
     "curto": "the saucer of stacked vivid purple gelatin cubes",
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
#
# ⛔⛔ A PROMESSA MUDOU DE EIXO — 2026-08-10, reforma de copy 16s.
# TODAS as dezoito entradas antigas prometiam TAMANHO (`ten times bigger`,
# `grow a full inch`, `worth three inches`, `double the size`). A VSL vende
# RECUPERACAO DE ERECCAO, nao aumento: a isca absurda tem de mentir sobre a
# MESMA coisa que o mecanismo entrega, senao o desmentido nao abre buraco
# nenhum — ele troca de assunto, e o espectador que veio pelo `+3 inches`
# recebe uma receita para outra queixa.
# ⚠️ O TRAVAMENTO DELIBERADO da fonte (`ten times bigger` em 7 de 8 reels)
# CAI JUNTO, e a razao esta' escrita: ele so' valia enquanto a promessa era de
# tamanho. A concentracao agora e' em DURACAO (`all night`, `an hour`), que e'
# o que a nossa oferta paga.
# ⭐ CT7 permite verbo de ereccao AQUI, e so' aqui: no take 1 dos angulos de
# isca absurda a promessa e' justamente a que o video desmente meio segundo
# depois. Na cena 2 (claim NOSSO) continua proibido.
# ⛔ Nenhuma com PRAZO (`days`/`weeks`/`months`) — foi o token que derrubou o
# NECROSE. `minutes`, `hour` e `night` nao sao prazo, sao duracao do ato.
# ⚠️ FAIXA ESTREITA, 11-12 palavras: o teto da cena 1 e' 22 e o desmentido
# custa 7-8. Entrada de 14 palavras aqui seria entrada morta.
CRENDICES = [
    {"degrau": "assertiva",
     "txt": "Rub {s} on your {o} and it stays up all night."},
    {"degrau": "assertiva",
     "txt": "Put {s} on your {o} tonight and it holds for hours."},
    {"degrau": "assertiva",
     "txt": "One spoon of {s} on your {o} and you last all night."},
    {"degrau": "assertiva",
     "txt": "The whole internet says {s} on your {o} works every single time."},
    {"degrau": "assertiva",
     "txt": "Two fingers of {s} straight onto your {o}, and it lasts hours."},
    # ⚠️ OUVIDO NATIVO, 2026-08-10: era `and that's you all night`. `that's
    # you ...` como predicado de resultado e' construcao britanica (`that's
    # you sorted`); num ouvido americano de 50-70 anos, ouvida UMA vez, ela
    # nao fecha a promessa — o espectador entende as palavras e nao entende a
    # frase. `you're good all night` diz o mesmo, no mesmo custo (11).
    {"degrau": "assertiva",
     "txt": "A little {s} on your {o} and you're good all night."},
    {"degrau": "assertiva",
     "txt": "Rub {s} on your {o} tonight — two solid hours, they claim."},
    {"degrau": "condicional",
     "txt": "Want your {o} lasting all night? Rub {s} on it tonight."},
    # ⚠️ DUAS DAS QUATRO CONDICIONAIS PERDERAM O VERBO `rub` — 2026-08-10. As
    # quatro o tinham, e com o degrau TRAVADO na UI/CLI o guarda de colisao do
    # `_montar_falas` nao tinha para onde fugir: `Then rub menthol rub straight
    # on it` sobrava em 5,7% dos sorteios travados. Com duas saidas limpas o
    # residuo cai para (2/4)^12, que e' zero na pratica. Os verbos novos
    # (`coat`, `work`) ja' viviam no pool `resistencia` — nao e' vocabulario
    # novo, e' vocabulario redistribuido.
    {"degrau": "condicional",
     "txt": "Want your {o} going all night? Then coat it in {s}."},
    {"degrau": "condicional",
     "txt": "If you want your {o} lasting an hour, rub {s} on it."},
    {"degrau": "condicional",
     "txt": "If your {o} keeps quitting, work {s} into it nightly."},
    # ⚠️ DEITICO SEM REFERENTE, 2026-08-10: era `Every guy here swears`. O
    # elenco da cena 1 e' UM (TR13) — nao ha' `here` nenhum em quadro, e
    # `every guy here` manda o ouvido procurar uma plateia que o frame nao
    # tem. O `medir_deiticos` nao pega porque `here` sozinho nao esta' na
    # lista de tokens dele; pegou o ouvido. `I know` custa 1 palavra e o pior
    # caso da cena 1 nao muda (12, empatado com `The whole internet says`).
    {"degrau": "testemunho",
     "txt": "Every guy I know swears {s} on your {o} works every time."},
    {"degrau": "testemunho",
     "txt": "My cousin swears {s} on your {o} buys you a whole hour."},
    {"degrau": "testemunho",
     "txt": "Guys everywhere swear {s} on your {o} is worth two solid hours."},
    {"degrau": "testemunho",
     "txt": "Everybody says the same thing: {s} on your {o}, all night."},
    {"degrau": "testemunho",
     "txt": "Half this country swears {s} on your {o} lasts you an hour."},
    {"degrau": "resistencia",
     "txt": "Rub {s} into your {o} nightly and it never quits on you."},
    {"degrau": "resistencia",
     "txt": "Coat your {o} in {s} and it stops quitting on you."},
    {"degrau": "resistencia",
     "txt": "Rubbing {s} on your {o} beats every pill on the shelf."},
    {"degrau": "resistencia",
     "txt": "Work {s} into your {o} and it never lets you down."},
]

DEGRAUS = ("assertiva", "condicional", "testemunho", "resistencia")

# O desmentido e' BEAT PROPRIO (TR8), curto, colado na crendice. E' ele que
# transforma o comando absurdo em pergunta — e a pergunta e' o buraco onde a
# cena 2 encaixa o batismo.
#
# ⭐⭐ CT2 — E AGORA ELE CARREGA A FALHA, COM DANO CONCRETO.
# Medido: 78% dos sorteios antigos nao tinham UMA sentenca dizendo o que o
# corpo faz de errado. `Nobody actually believes that one.` desmente a isca e
# nao diagnostica nada — e sem auto-reconhecimento nao ha' comentario: ele nao
# comenta porque a copy e' boa, comenta porque SE VIU.
# A melhor linha ja' medida do parque tem cinco palavras, um numero e um dano
# (`He'd lose it ten minutes in.`) — aqui ela vem em 2a PESSOA, porque nas
# cenas 1 e 2 o elenco e' 1 (TR13) e um `he` sem homem em quadro e' pronome sem
# dono (lente T16-5b).
# ⚠️ FAIXA ESTREITA, 7-8 palavras: crendice (11-12) + desmentido (7-8) + 1 de
# folga da substancia de duas palavras = 20 no pior caso, teto 22, piso 16.
# ⛔ Zero `days`/`weeks`/`months`: a cena ja' diz `your {o}` e 2a pessoa somada
# a PRAZO e' a composicao que derrubou o video do NECROSE.
DESMENTIDOS = [
    "Nonsense. You lose it ten minutes in.",
    "Doesn't work. You go soft in five minutes.",
    "Course not. You quit twenty minutes in.",
    "You know better. You lost it last night.",
    "Garbage, every word. You still can't finish.",
    "Nope. You gave out again on Saturday.",
    "That's a lie. You go soft too early.",
    "Right? Total nonsense. And you still quit.",
    "Lies. You've been quitting early for years.",
    "Sounds insane because it is. You quit anyway.",
    "Zero chance. You went soft again last night.",
    "You already know. You lose it early.",
    "Never worked for anybody. You still go soft.",
    "Not one bit. You quit ten minutes in.",
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
# ⛔⛔ O CTA TEM DE NOMEAR O QUE E ENVIADO — ordem do Ed, 2026-08-06, lendo o
# take 3 renderizado: *"'and I'll send it.' — enviar o QUE?? a isca tinha que
# estar expressa: 'que eu envio a receita', e nao 'que eu envio ela'"*.
# A fala que ele leu era `It's four lines long. Comment gelatin, and I'll send
# it.` — dois pronomes sem dono numa frase so: o que tem quatro linhas, e o
# que sera enviado. O espectador comenta sem saber o que vai receber, e o CTA
# e' o unico ponto do video onde ele age.
# ⚠️ 14 das 18 entradas ja nomeavam ("the recipe", "the measurements", "all
# four ingredients"). As 5 trocadas mantiveram a MESMA contagem de palavras: a
# cena 3 ja esta 12,8% acima do teto e um CTA mais longo vira corte de fala.
# ⛔ O `_tr_isca_nomeada` cobra isso a cada sorteio.
#
# ⭐⭐ CT6 — O CTA PASSA A DIZER **ONDE A RECEITA CHEGA**. Medido: 95% dos
# sorteios antigos nao diziam. O KPI e' uma CONFISSAO PUBLICA — o comentario
# leva nome e foto e vai para o feed de quem conhece o sujeito — e em 48
# segundos de copy nao havia uma palavra baixando esse custo. A clausula e'
# gratis: `and I'll send the recipe` (9 palavras) vira `and the recipe goes to
# your messages` (9 palavras), mesmo custo, e entrega o endereco, a privacidade
# e o fato de que nao e' na tela publica.
#
# ⚠️ A ENTROPIA DE FORMA DO INICIO FOI TROCADA DE PROPOSITO. A nota antiga
# registrava que sete entradas levavam a keyword em outra posicao para o pool
# nao abrir sempre igual. Isso morreu: CT1 exige que a sentenca do CTA seja a
# ULTIMA do video e o orcamento nao paga lead-in. A variacao mudou de lugar —
# ela agora mora no ENDERECO DA ENTREGA (`your messages` · `your inbox` · `by
# message` · `in private` · `nobody else sees`) e no verbo de chegada (goes ·
# lands · arrives · waits · hits · shows · drops · stays · reaches), que e' a
# parte que o espectador precisa ouvir.
# ⛔ A forma da keyword nao muda: `gelatin` minusculo, seguido de virgula.
# ⚠️ FAIXA ESTREITA, 8-9 palavras: troca (10-11) + follow (3-5) + CTA (8-9) da'
# 21-25 num teto de 25.
CTAS = [
    "Comment gelatin, and the recipe goes to your messages.",
    "Comment gelatin, and the recipe lands in your inbox.",
    "Comment gelatin, and the recipe arrives in your messages.",
    "Comment gelatin, and the recipe waits in your inbox.",
    "Comment gelatin, and the whole recipe hits your inbox.",
    "Comment gelatin, and the recipe comes by message tonight.",
    "Comment gelatin, and I'll send the recipe in private.",
    "Comment gelatin, and the measurements go to your messages.",
    "Comment gelatin, and the recipe appears in your inbox.",
    "Comment gelatin, and nobody else sees the recipe.",
    "Comment gelatin, and the recipe stays in your messages.",
    "Comment gelatin, and the four ingredients reach your inbox.",
    "Comment gelatin, and the recipe reaches you in private.",
    "Comment gelatin, and the recipe reaches your inbox tonight.",
    # ⚠️ ENTRADA MAIS FRACA DO POOL, E FICA — registrado em 2026-08-10 depois
    # de tentar troca-la. `what to buy` e' oracao livre como SUJEITO de `hits`,
    # a unica assim no pool: falada, `and what to buy...` abre como pergunta e
    # o ouvido volta atras no meio da unica sentenca que gera receita. A troca
    # por `the shopping list` foi ESCRITA E MEDIDA — 25 ERRO em 400 sorteios:
    # o `lint_isca_cta` do short_comum (compartilhado, fora da minha alcada)
    # so' reconhece recipe/measurements/ingredients/link/source/protocol e as
    # formas `I'll send` / `in|to your inbox` — `hits your inbox` nao casa.
    # As saidas que casam custam 10 palavras e gastariam a ULTIMA folga do
    # teto de render (24 -> 25 no pior caso), que nao vale um ajuste de
    # sintaxe. Fica como esta'; a decisao de reescrever a sentenca do CTA e'
    # do operador.
    "Comment gelatin, and what to buy hits your inbox.",
    "Comment gelatin, and the recipe drops into your inbox.",
    "Comment gelatin, and the recipe is in your messages.",
    "Comment gelatin, and I'll send the recipe by message.",
]

# ⛔ TR5 — REGRA DE POOL, medida pelo operador: "brother" caia em 31-73% dos
# videos. No maximo DUAS entradas com "brother", e a MAIORIA sem vocativo
# nenhum. O self-test do --stats reprova se a proporcao escorregar.
# ⛔ Zero nome de plataforma na `Dialogue:` — P12.
#
# ⭐⭐ CT1 — O FOLLOW MUDOU DE LUGAR E DE TAMANHO, 2026-08-10.
# DE LUGAR: era a ULTIMA sentenca do video, colada no unico pedido que gera
# receita — 100% dos sorteios. A ultima coisa no ouvido era `The algorithm
# hides me from non-followers` (expectativa negativa), `Followers get answered
# first. Everyone else waits.` (condicional na recompensa) ou `Follow me,
# brother, or this never arrives.` (segundo CTA nu). A posicao final e' a que
# fica; ela tem de ser o pedido. Agora o follow vem ANTES do CTA.
# DE TAMANHO: 6-8 palavras -> 3-5. O orcamento do take 2 reserva TRES palavras
# para este beat, e o que sobrava vinha do CTA, que e' onde o dinheiro esta'.
# ⛔ O QUE SE PERDEU, e e' honesto dizer: o MOTIVO do gate (a plataforma
# bloqueia · a fila de comentarios · o feed some amanha) nao cabe mais em 3-5
# palavras na maioria das entradas. TRES entradas ainda o carregam (`I answer
# followers only`, `Followers get answered first`, `No follow, no message`); as
# outras onze sao comando puro. A troca foi deliberada: motivo de gate na
# posicao final custava o CT1 inteiro.
# ⛔⛔ POOL APOSENTADO EM 2026-08-10 — ELE NAO CHEGA MAIS AO VIDEO.
# Ordem do operador: *"nao acho que deva ter follow me no cta, a mensagem e'
# enviada independente de seguirem ou nao"* (CT8 do CONTRATO-COPY-16S).
# O gate existia no repo inteiro por uma PREMISSA ERRADA sobre a automacao de
# DM, e quem opera a automacao corrigiu a premissa.
# ⚠️ POR QUE NAO FOI APAGADO: o autoteste e os contratos deste motor ainda o
# validam (contagem minima, vocativo, tamanho), e apagar exigiria mexer neles
# no mesmo commit em que a copy inteira mudou — duas cirurgias de uma vez e'
# como se perde o rastro do que quebrou o que.
# ⛔ ENTAO FICA ESTE AVISO: melhorar as entradas abaixo NAO muda um unico
# video. Se o follow voltar um dia, ele volta ANTES do CTA (CT1) e por decisao
# do operador, nao por alguem reativar a variavel.
GATES = [
    "Follow me first.",
    "Hit follow first.",
    "Tap follow first.",
    "Follow me right now.",
    "Give me a follow.",
    "One tap: follow me.",
    "Follow me, then comment.",
    "Follow me tonight.",
    "Follow me, brother.",
    "Follow me, my friend.",
    "Follow me, guys.",
    "I answer followers only.",
    "Followers get answered first.",
    "No follow, no message.",
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


def _narradora_por_id(valor):
    """A entrada de NARRADORAS que o dropdown `A NARRADORA` escolheu.

    ⭐ O `ui_agente` desenha o `rotulo` e devolve o `id` — este helper e' a
    ponta que converte um no outro.
    ⛔ CEDE PARA O POOL INTEIRO SO' SE O ID NAO EXISTIR, e isso e' rede contra
    ledger velho, nunca contra erro de digitacao vivo: o `--stats` cobra que
    todo id do pool seja resolvivel, entao um `None` aqui em producao ja'
    teria reprovado o self-test.
    ⚠ Aceita o DICIONARIO tambem — o cadeado da coluna trava o eixo com a
    entrada que esta' na tela, nao com o id dela.
    """
    if isinstance(valor, dict):
        return valor
    for n in NARRADORAS:
        if n["id"] == valor:
            return n
    return NARRADORAS[0]


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

# ⛔⛔ ESTA DEFINICAO DE `TR8_NUMERO` ERA CODIGO MORTO E FOI REMOVIDA
# (2026-08-10). Havia DUAS no arquivo — esta e a de baixo, na secao do linter —
# e a de baixo, por ser a ultima a ser executada no import, sobrescrevia esta.
# Ou seja: a lista de numerais acima nunca mediu nada. Fica o comentario porque
# regra que some sem explicacao vira divida; a definicao VIVA e' a unica que
# existe agora, e ela mudou de familia junto com a promessa (tamanho ->
# duracao) na reforma de copy 16s.

TR8_PRAZO = re.compile(r"\b(\w+\s+(?:days?|weeks?|months?))\b|\bsince\s+[A-Z]",
                       re.I)

# ⛔⛔ TR16 — PRONOME SEM DONO (Ed, 2026-08-06, no mesmo take que trouxe o
# drifting da fundida). A prova `He'll tell you if you ask him.` caiu numa fala
# cuja fundida nunca apresentou homem nenhum, e o espectador pergunta "quem?".
#
# ⚠️ O comentario do pool de PROVAS ja' dizia "ZERO DEIXIS A PESSOA" e listava
# cinco entradas removidas por isso — e QUATRO com o mesmo defeito continuaram
# la'. Foi correcao declarada pronta com o vicio ainda dentro: o mesmo modo de
# falha das licoes §29-§32. Medido: 24 dos 180 pares (13%) deixavam o pronome
# orfao.
#
# ⛔ A correcao NAO e' apagar as quatro provas. Elas sao boas quando a fundida
# fala de um homem ("his {o}", "my husband's {o}") — apagar encolheria o pool
# em 33% para resolver 13% dos casos. O que se cobra e' o PAR: a prova com
# pronome so' entra se a fundida tiver apresentado alguem, exatamente como a
# prova com prazo ja' se re-sorteia diante de 2a pessoa.
TR16_PRONOME = re.compile(r"^\s*(he|him|his|the same man|same man|that man)\b",
                          re.I)
TR16_ANTECEDENTE = re.compile(
    r"\b(his|him|husband|husband's|a man i know|my man)\b", re.I)
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


# ⭐ TR1 — O GESTO DA TROCA, agora na fala. A lista e' a dos verbos que o pool
# `TROCAS16` usa para largar o que nao presta; ampliar o pool exige ampliar
# aqui, e e' de proposito: lente que aceita qualquer coisa nao prova nada.
# ⚠️ `leave it` entrou junto com a entrada nova do pool (2026-08-10): sem ela a
# lente reprovaria uma entrada que E' o gesto.
# ⚠️ `wrong jar` -> `wrong stuff` junto com a entrada do pool (2026-08-10):
# nao ha' pote no frame montado, e a lente nao pode ser a unica sobrevivente
# de um gesto que o video nao mostra. `wrong jar` sai da lente porque saiu do
# pool — lente que aceita forma morta esconde pool morto.
TR1_GESTO = re.compile(
    r"\b(drop|forget|put that down|set that down|leave that|leave it|"
    r"not that|wrong stuff|skip that|that failed|that did nothing)\b", re.I)


def _so_crendice(fala1):
    """A crendice sozinha, sem o desmentido colado no fim.

    ⚠️ EXISTE POR CAUSA DA REFORMA DE COPY 16s. O desmentido agora carrega a
    FALHA com numero (`You lose it ten minutes in.`, CT2), e duas lentes
    perguntam da cena 1 "onde esta' a PROMESSA?": o `_tr_crendice` (TR8) e o
    `_gatilho_reacao`, que decide se a cara dela sincroniza `On the number` ou
    `On the promise`. Medindo a fala INTEIRA, o numero do DANO passaria por
    numero da PROMESSA e a reacao facial sincronizaria no beat errado — no
    frame em que ela diz que o espectador amolece, nao no frame do exagero.
    """
    for d in DESMENTIDOS:
        if fala1.endswith(d):
            return fala1[:-len(d)].strip()
    return fala1


def _montar_falas(rng, subst, orgaos, relacao, degrau=None):
    """As DUAS falas do formato 16s.

    cena 1 = crendice (isca absurda) + desmentido COM A FALHA DELE   (CT2)
    cena 2 = A TROCA (mecanismo com razao) -> FOLLOW -> CTA          (CT1)

    ⛔⛔ O QUE MORREU, e e' honesto dizer: `FUNDIDAS`, `PROVAS`, `BARREIRAS` e
    `TESTEMUNHOS`. Os quatro eram beats das cenas 2 e 3 do motor de 24s.
    ⭐ O que sobreviveu como EIXO (o conteudo foi reescrito na reforma de
    2026-08-10): `CRENDICES` (18 -> 20), `DESMENTIDOS` (12 -> 14), `TROCAS16`
    (12 -> 14), `CTAS` (18 -> 18) e `GATES` (14 -> 14). Nenhum pool encolheu.

    ⚠️ E o TESTEMUNHO nao saiu de graca: era ele que nomeava o orgao na cena 3.
    Por isso TODA entrada de `TROCAS16` carrega o `{o}` — a cota nao caiu, ela
    mudou de dono.

    ⭐⭐ A ORDEM DE ESCOLHA E' A DO ORCAMENTO, e ela inverteu: quem escolhe
    PRIMEIRO e' o beat com MENOS SUBSTITUTOS, e quem escolhe por ULTIMO absorve
    a sobra. A TROCA e' a voz do angulo (e a mais cara, 10-11 palavras), o
    FOLLOW e' o beat de 3-5, e o CTA e' o intercambiavel — 18 entradas todas em
    8-9 palavras. Antes o CTA escolhia no meio e o gate no fim, que e'
    exatamente o inverso.
    """
    cren_pool = [c for c in CRENDICES if degrau in (None, c["degrau"])] or CRENDICES

    # ⚠️⚠️ COLISAO DE VERBO COM SUBSTANCIA — 3,4% dos sorteios, medido em 1.000
    # em 2026-08-10: `Rub menthol rub on your manhood`, `Rubbing menthol rub on
    # your pecker`. Oito das vinte crendices carregam o verbo `rub` e uma das
    # catorze substancias E' um rub — o gaguejo cai nas CINCO PRIMEIRAS
    # palavras do video, que e' exatamente onde o polegar decide.
    # ⛔ NAO SE CONSERTA NA SUBSTANCIA: `menthol rub` e' pool VISUAL (entra no
    # IMAGE como a pelicula sobre o proxy) e reescreve-la e' mexer na CENA —
    # alcada do operador.
    # ⚠️ E NAO MATA ENTRADA NENHUMA: a crendice barrada continua sorteavel com
    # as outras treze substancias, e o [ALCANCE] segue 20/20. No degrau
    # `condicional` as quatro entradas tem `rub`; ali o `_escolher` cai no
    # fallback e o gaguejo volta — que e' o estado de hoje, nao uma regressao.
    _e_rub = "rub" in subst["fala"].lower()
    cren = _escolher(rng, cren_pool,
                     lambda c: not (_e_rub
                                    and re.search(r"\brub(bing)?\b",
                                                  c["txt"], re.I)))

    c1 = "%s %s" % (cren["txt"].format(s=subst["fala"], o=orgaos[0]),
                    rng.choice(DESMENTIDOS))

    # ⚠️ o menor de cada eixo, para reservar o espaco desde o primeiro sorteio.
    # Sem isto a troca e' escolhida contra o teto cheio, o CTA entra por cima e
    # a cena estoura — foi exatamente o que aconteceu na cena 2 do motor de 24s,
    # onde 14 das 15 FUNDIDAS nunca cabem nem com a menor PROVA.
    c_cta = min(CTAS, key=_palavras)

    # ⛔⛔ A ORDEM DOS ARGUMENTOS E' A ORDEM NO OUVIDO, e ela E' o CT1:
    # troca -> follow -> CTA. O video termina no pedido; nada depois dele.
    # ⛔⛔ CT8 (2026-08-10) — O BEAT DO FOLLOW SAIU DA FALA.
    # Ordem do operador: *"nao acho que deva ter follow me no cta, a
    # mensagem e' enviada independente de seguirem ou nao"*. O gate
    # existia no repo inteiro por uma PREMISSA ERRADA sobre a automacao
    # de DM, e quem opera a automacao corrigiu. As palavras liberadas
    # vao para o mecanismo e a prova.
    def _c2(tr, cta):
        return "%s. %s" % (
            tr.format(s=subst["fala"], o=orgaos[1]).rstrip(". "), cta)

    _tc = [x for x in TROCAS16
           if _palavras(_c2(x, c_cta)) <= TETO_FALA[2]]
    troca = rng.choice(_tc or [min(TROCAS16, key=_palavras)])
    _cc = [x for x in CTAS
           if _palavras(_c2(troca, x)) <= TETO_FALA[2]
           and not _eco(c1, _c2(troca, x))]
    _cc = _cc or [x for x in CTAS
                  if _palavras(_c2(troca, x)) <= TETO_FALA[2]]
    cta = rng.choice(_cc or [min(CTAS, key=_palavras)])

    return [c1, _c2(troca, cta)]

def sortear(pagina, rng, ledger, travas=None):
    """TR20 — anti-repeticao por ledger, por pagina.

    Os dois eixos de ROSTO evitam os 3 ultimos (rosto repetido e' o que o
    operador ve primeiro no lote); os eixos de cenario e objeto evitam os 2
    ultimos. Combo repetido em videos consecutivos da mesma pagina e' proibido.

    ⚠️ A RELACAO E' SORTEADA ANTES DAS FALAS. Antes as duas saiam independentes
    e 13% dos lotes diziam `my husband's {o}` num IMAGE 03 que nomeava a
    narradora como a vizinha — e a relacao nomeada e' a alavanca 2 do protocolo
    de recusa: contradize-la na fala a anula.
    """
    # ⛔⛔ O 4o POSICIONAL E' `travas`, NAO `degrau`. A ui_agente chama
    # `sortear(pag, rng, led, travas_dict)` sempre que o motor declara
    # EIXOS_TRAVAVEIS — e com a assinatura antiga o dicionario caia dentro de
    # `degrau` e virava estado invalido em silencio. O `degrau` do CLI passa a
    # viajar DENTRO das travas, que e' o unico canal que a UI conhece.
    travas = travas or {}
    degrau = travas.get("degrau")
    hist = ledger.get(pagina, {})
    # ⭐ MODOS DE REF — a narradora e o corpo-prova, cada um com o seu.
    # ⚠️ 28 e' o piso do TR11 — ver a nota em `sc.ref_bela`.
    # ⭐⭐ O DROPDOWN `A NARRADORA` entra AQUI — e' a "UMA linha no `sortear`"
    # que a nota do `EIXOS_TRAVAVEIS` la' embaixo exige. Sem ela o
    # `DROPDOWNS_UI` desenharia o menu e nao travaria nada.
    # ⛔ E ELE VEM ANTES DO `bela`: escolha explicita e' mais especifica que
    # modo grosso, mesma ordem que a `ui_agente` ja' usa (dropdown antes do
    # cadeado, pele por ultimo). Com o menu em `livre` o sorteio e' bit a bit
    # o de antes.
    nar = (_narradora_por_id(travas["narradora"]) if travas.get("narradora")
           else sc.ref_bela(NARRADORAS[0], rng,
                            idade_min=IDADE_MINIMA_NARRADORA)
           if travas.get("bela")
           else _evitando(rng, NARRADORAS, hist.get("narradora", [])[-3:]))
    _hpool = homens_de(pagina)
    hom = (sc.ref_forte(_hpool[0], rng) if travas.get("forte")
           else _evitando(rng, _hpool, hist.get("corpo_prova", [])[-3:]))
    cen = _evitando(rng, CENARIOS, hist.get("cenario", [])[-2:])
    # ⭐ CADEADO DO PROXY — ordem do operador, 2026-08-05: *"coloca um botao de
    # trava no proxy tb"*. A UI devolve o DICIONARIO que esta' na tela (nao um
    # id), entao ele entra direto: quem remonta o video em volta dele e' daqui
    # para baixo.
    prox = travas.get("proxy") or _evitando(rng, PROXIES,
                                            hist.get("proxy", [])[-2:])
    sub = _evitando(rng, SUBSTANCIAS, hist.get("substancia", [])[-2:])
    texturas = TEXTURAS if sub.get("fluida", True) else         [x for x in TEXTURAS if not x.get("fluida", True)]
    tex = _evitando(rng, texturas, hist.get("textura", [])[-2:])
    mec = _evitando(rng, MECANISMOS_PROP, hist.get("mecanismo", [])[-2:])

    relacao = _relacao(rng, nar["idade"], hom["idade"])

    # ⛔⛔ CT4 — UM APELIDO DO ORGAO POR VIDEO, REPETIDO NOS DOIS TAKES.
    # ISTO REVERTE a regra que estava aqui (`sc.orgaos_sorteaveis(rng, 3)`, tres
    # substantivos DISTINTOS por sorteio), e a reversao e' declarada:
    #   · em 24s e cinco cenas o risco e' o BORDAO — duas mencoes iguais viram
    #     tique, e por isso o motor de 24s rotaciona;
    #   · em 16s e DUAS cenas o risco e' o oposto. Medido: o apelido mudava no
    #     corte em 100% dos videos deste motor. O corte zera a memoria de
    #     trabalho, e trocar `tool` por `Johnson` no segundo 9 obriga o
    #     espectador a remapear justamente quando ele ja' esta' com um pe' fora.
    # ⭐ A variacao NAO acabou: ela continua existindo ENTRE videos (cinco
    # apelidos sorteados por lote), que e' onde ela nunca custou nada.
    # ⚠️ A lista de tres fica, porque `_montar_falas` e `nova_fala` a esperam —
    # e' o MESMO termo nas tres posicoes.
    # ⛔⛔ CT4b (2026-08-10) — SO' TRES APELIDOS SAO SORTEAVEIS.
    # Ordem do operador: *"quero que vc use weiner e john-son pra se referir ao
    # orgao tb, nao apenas pec-ker"*. `soldier` soa filme de guerra para ouvido
    # americano e `tool` e' ambiguo em giria dos EUA; os dois seguem no NUCLEO
    # porque as LENTES os usam para DETECTAR o orgao — o que muda e' que nao
    # sao mais sorteaveis. O CT4 trava UM apelido por video; sem isto aqui, um
    # apelido por video vira o MESMO apelido no lote inteiro.
    _o = rng.choice(sc.APELIDOS_16)
    orgaos = [_o, _o, _o]
    falas = _montar_falas(rng, sub, orgaos, relacao, degrau)
    ban = _bancada_livre(rng, falas, hist.get("bancada", [])[-2:], sub)

    return {"pagina": pagina,
            # 50/50, ordem do operador 2026-08-04
            "bandeira": rng.random() < 0.5, "narradora": nar, "corpo_prova": hom,
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
    you`, `beats every pill on the shelf` — 20% do pool) manda o Veo
    sincronizar com um numeral que a fala nao tem, e ele escolhe sozinho onde.

    ⛔ MEDE SO' A CRENDICE, nunca a fala inteira (ver `_so_crendice`): desde a
    reforma de copy 16s o desmentido carrega o DANO com numero (`ten minutes
    in`), e casar ali sincronizaria a cara de espanto dela com a frase em que
    ela diz que o espectador amolece.
    """
    return (GATILHO_NUMERO if TR8_NUMERO.search(_so_crendice(fala1))
            else GATILHO_PROMESSA)


def montar(spec):
    et = ETNIA[spec["pagina"]]
    nar, hom, cen = spec["narradora"], spec["corpo_prova"], spec["cenario"]
    prox, sub, tex = spec["proxy"], spec["substancia"], spec["textura"]
    mec, ban = spec["mecanismo"], spec["bancada"]
    falas = spec["falas"]
    bnc = cen["bancada"]

    # ⭐⭐ A BANDEIRA E' 50/50 (ordem do operador, 2026-08-04). Ela estava escrita
    # DENTRO da string de cada cenario, entao saia em 100% dos videos. Aqui ela
    # sai por remocao EXATA quando o sorteio diz que nao, e o `lint_bandeira`
    # confere no TEXTO MONTADO — inclusive a prosa (virgula dupla, `and` orfao).
    # ⛔ O pool nao e' reescrito: as strings de cenario sao copy validada.
    com_bandeira = spec.get("bandeira", True)
    cen_set = cen["set"] if com_bandeira else sc.tirar_bandeira(cen["set"])
    cen_anc = (cen["re_ancora"] if com_bandeira
               else sc.tirar_bandeira(cen["re_ancora"]))
    luz = cen["luz"][0].upper() + cen["luz"][1:]

    # ⚠️ TR18 — A ANCORA DE CONTINUIDADE AQUI E' INVERTIDA em relacao aos
    # outros agentes: quem repete rosto e' a NARRADORA (ela esta' nas tres
    # cenas), e a descricao volta INTEIRA, com a marca facial. Ancora curta
    # ("same hair") carrega a roupa e perde o rosto — foi assim que o
    # VAZAMENTO devolveu um senhor de oculos e bigode no lugar do corpo-prova.
    # ⛔⛔ A NARRADORA PASSA A LEVAR A ETNIA DA PAGINA — ORDEM DO ED, 2026-08-06.
    # Ele setou `pele escura` na UI e recebeu narradora branca ao lado de um
    # corpo-prova negro: *"se eu setei pele escura, as refs tem que ter pele
    # escura ue"*.
    #
    # ⚠️ ISTO REVERTE O [D2], que era decisao dele e esta escrita no topo do
    # arquivo: "o espectador de 50+ se identifica com o CORPO, nao com quem
    # narra — entao a congruencia vale onde ela vende". So o HOMEM casava com o
    # avatar. O proprio comentario do pool ja antecipava a virada: *"Se o
    # operador quiser garantir proporcao, isso e' ORDEM DELE — nao se decide
    # aqui."* E' esta a ordem.
    #
    # ⚠️ O QUE SE PERDE, para ficar registrado: a narradora era o maior eixo de
    # variacao visual do lote (8 arquetipos, cabelo afro/box braids/ruivo/
    # platinado). Amarrada a pagina, esse eixo encolhe pela metade — cada
    # pagina passa a sortear so dentro da propria etnia. O ganho e a
    # congruencia que o CLAUDE.md chama de inviolavel e que o video quebrava.
    ela = ("a %d-year-old %s woman with %s, wearing %s"
           % (nar["idade"], et, nar["marca"], nar["roupa"]))
    mesma = ("The same %d-year-old %s woman, with %s, wearing %s"
             % (nar["idade"], et, nar["marca"], nar["roupa"]))
    recibo = TR_BANCADA_RECIBO % (bnc, ban["itens"])
    analogia = ANALOGIAS[prox["analogia"]]
    gatilho = _gatilho_reacao(falas[0])

    b = {}

    # O REF e' a NARRADORA: e' o rosto que precisa se repetir nas tres cenas.
    # O corpo-prova entra novo na cena 3 e nao tem REF — por isso ele leva
    # artigo indefinido la' (TR17).
    b["BLOCO 0 (REF)"] = (
        "REF 01: Photo of a real person, a %d-year-old %s woman, chest up, "
        "facing the camera directly, calm steady expression. %s. Wearing %s. "
        "Plain neutral gray background, soft even frontal light. No subtitles, "
        "no captions, no burned-in text, no watermark."
        % (nar["idade"], et, nar["marca"][0].upper() + nar["marca"][1:],
           nar["roupa"])
    )

    # --- IMAGE 01/03 — A CRENDICE -------------------------------------------
    # Os 6 elementos obrigatorios do hook, todos 8/8 na fonte: ela sozinha com
    # o olhar na lente · o proxy vertical na altura do rosto · a substancia JA'
    # no prop (TR4: a aplicacao nunca e' mostrada, e a procedencia se prova
    # pelo pote aberto com a tampa deitada) · o recibo · o alibi domestico com
    # a bandeira.
    b["IMAGE 01/02"] = (
        "IMAGE 01/02: Medium shot in %s. Standing behind the %s is %s. She "
        "looks straight into the lens. In her left hand: %s, and %s. %s %s A "
        "wooden board lies on the %s in front of her. Standing on the %s since "
        "before the shot began: %s. Also on the %s, open since the first frame: "
        "%s. %s She is the only person in the frame. %s %s"
        % (cen_set, bnc, ela, prox["img"], tex["desc"] % sub["fala"],
           TR_PROXY_NA_MAO, TR_MAO_LIVRE % sub["fala"],
           bnc, bnc, sub["pote"], bnc, mec["plantado"], recibo, luz, CAUDA)
    )

    # ⛔⛔ A IMAGE DA TROCA FOI APAGADA — decisao do operador, 2026-08-08.
    # Ela era a cena 2 do motor de 24s: ela sozinha atras da bancada, o proxy
    # lambuzado no punho, o mecanismo plantado e a bancada-recibo. E' o bit que
    # da' nome ao angulo, e cai porque as cenas 2 e 3 deste motor NAO FUNDEM:
    #   · a cena 3 e' o bloco mais arriscado do lote (a regra de que ela deriva
    #     custou QUATRO recusas deterministicas) e o recibo de 42 palavras foi
    #     removido dela porque densidade e' superficie de bloqueio. Trazer a
    #     bancada de volta e' recriar o que ja' foi pago;
    #   · e as duas disputam QUEM SEGURA O PROXY — no punho dela para a troca
    #     acontecer, na mao dele pela F12b. Nao ha' frame que comporte as duas.
    # ⭐ A troca nao sumiu do video: ela desceu para a FALA, no pool `TROCAS16`.
    # ⛔ APAGADA, nao comentada: bloco morto e' bomba com pino — basta alguem
    # religar por copia e o lote sai com tres cenas num motor de duas.

    # --- IMAGE 02/02 — O CORPO-PROVA ----------------------------------------
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
    b["IMAGE 02/02"] = (
        "IMAGE 02/02: Medium shot in %s, same light. %s, stands frame-left; "
        "she is %s. A %d-year-old %s man with %s, in %s and %s, stands beside "
        "her, upright, chin level, his eyes on the lens, saying nothing. %s "
        "Behind them on the %s, still where it was: %s. They are the only two "
        "people in the frame. %s %s %s"
        % (cen_anc, mesma, spec["relacao"], hom["idade"], et,
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
    b["TAKE 01/02"] = (
        "TAKE 01/02: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway, no cuts, and the camera does not move. She "
        "talks straight into the lens the whole time. %s %s She is the only "
        "person in the shot.\nDialogue: \"%s\"\nAudio: quiet room tone in the "
        "%s. No music."
        % (TR_VAIVEM % analogia, TR_SEM_CRESCIMENTO % (prox["nome"], gatilho),
           sonorizar(falas[0]), cen["curto"])
    )

    # --- TAKE 02/02 ----------------------------------------------------------
    # ⛔ TR13: so' ela tem Dialogue. Ele e' mudo — o dialogo do Veo e'
    # monofonico na pratica e duas vozes saem tortas.
    b["TAKE 02/02"] = (
        "TAKE 02/02: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway, no cuts, and the camera does not move. %s "
        "She speaks straight into the lens, calm and even, no rush. Only she "
        "speaks.\nDialogue: \"%s\"\nAudio: quiet room tone in the %s. No music."
        % (TR_MAO_PROPRIA_TAKE % prox["nome"], sonorizar(falas[1]),
           cen["curto"])
    )

    # ⛔ trava de texto queimado em todo TAKE — o watermark que o
    # operador viu vazando nos reels da concorrente (2026-08-01).
    return sc.selar_takes(b)


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
#
# ⛔⛔ AS DUAS FORAM REESCRITAS NA REFORMA DE COPY 16s (2026-08-10), e a razao
# nao e' estilo: a familia numerica media TAMANHO (`ten`, `inch`, `bigger`,
# `size`, `doubles`), que e' exatamente a promessa que saiu do pool de
# CRENDICES porque a VSL vende recuperacao de ereccao, nao aumento. Regex que
# continua procurando a promessa antiga passa a medir zero de vinte e reprova
# copy certa — o modo de falha §16.
# ⚠️ A familia numerica agora e' de DURACAO (`all night`, `an hour`, `hours`,
# `every time`) e a de resistencia e' de PERSISTENCIA (`never quits`, `stops
# quitting`, `beats every`, `never lets you down`, `every night`).
# ⛔ `minutes` NAO entra: `ten minutes in` e' o DANO do desmentido (CT2), nao a
# promessa da crendice — e as duas frases vivem na mesma cena.
TR8_NUMERO = re.compile(
    r"\b(hours?|all night|every time|every single time|twice|ten times)\b", re.I)
TR8_RESISTENCIA = re.compile(
    r"(never quits|never lets you down|stops quitting|keeps quitting|"
    r"every night|nightly|a different animal|beats every)", re.I)

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
    # ⛔ A PROMESSA E' COBRADA DA CRENDICE, nao da fala inteira: o desmentido
    # agora carrega a FALHA com numero (CT2), e medir a fala inteira deixaria a
    # crendice passar de graca com o numero do DANO. Lente que aceita o avesso
    # do que cobra nao e' lente.
    if not (TR8_NUMERO.search(_so_crendice(h))
            or TR8_RESISTENCIA.search(_so_crendice(h))):
        achados.append(("ERRO", "TR8: a crendice nao carrega promessa "
                                "(de duracao ou de resistencia) — sem o segundo "
                                "choque o comando e' so' esquisito"))


def _tr_pronome_orfao(spec, blocos, achados):
    """TR16 — ⛔ PRONOME SEM DONO na fala.

    Ed, 2026-08-06, lendo o take 2 renderizado: a fala fechava em `He'll tell
    you if you ask him.` e nenhuma frase anterior apresentara homem nenhum. O
    espectador pergunta "he quem?" e o take inteiro se perde.

    ⚠️ A cobranca e' de REFERENTE, nao de pessoa. `his {o}` logo antes resolve
    o pronome; o que reprova e' o pronome que abre uma frase sem que a PROPRIA
    fala tenha apresentado alguem.

    ⛔ SO' A CENA 2. Na primeira versao eu cobrei as tres e o linter acusou 245
    de 400 sorteios — todos na cena 3, onde o testemunho abre com `He reaches
    first now...` e o homem ESTA' EM QUADRO: ele e' o corpo-prova, o referente
    e' visual e a fala nao precisa reapresenta-lo. A cena 2 e' o caso oposto,
    e e' por isso que o defeito nasce la': o IMAGE 02 declara que ela e' a
    unica pessoa no quadro, entao um `He` ali nao tem dono em lugar nenhum.
    """
    for i, fala in enumerate(spec["falas"], 1):
        if i != 2:
            continue
        frases = [f.strip() for f in re.split(r"(?<=[.!?])\s+", fala) if f.strip()]
        vistos = ""
        for f in frases:
            if TR16_PRONOME.match(f) and not TR16_ANTECEDENTE.search(vistos):
                achados.append((
                    "ERRO",
                    "TR16: cena %d abre uma frase com pronome sem dono (%r) — "
                    "nada antes na fala apresentou esse homem" % (i, f[:44])))
                break
            vistos += " " + f


# a frase que carrega o literal do mecanismo tem de dizer o que ele DEVOLVE
# ⛔⛔ A LISTA FOI AMPLIADA — 2026-08-08, e e' a TERCEIRA vez neste repo que
# uma regex de sinonimos mede outra coisa por conhecer meia familia (as duas
# anteriores: `leaves out` x `left out` no FALTA, e a lista de rotulos de
# hierarquia no `short_comum`).
# ⚠️ O QUE A LENTE EXISTE PARA PEGAR continua sendo o caso do operador:
# `Gelatin does what honey never could — the gelatin trick.` — mecanismo
# anunciado SEM verbo de efeito nenhum, nada em que agir.
# ⭐ O que ela NAO pode reprovar e' `The gelatin trick fills your {o}`: o
# verbo de efeito esta' la' e o destino e' o orgao. Faltavam na lista
# justamente os verbos de efeito diretos — fills, opens, wakes, hardens,
# feeds, straightens, loads, fixed. Sem eles a lente reprovava 800 de 800.
# ⛔ A ampliacao e' de VERBOS DE EFEITO, nao de qualquer verbo: continuam de
# fora `does`, `is`, `has` e companhia, que sao os que produzem o caso ruim.
# ⚠️ AMPLIADA DE NOVO NA REFORMA DE COPY 16s (2026-08-10) — e e' a QUARTA vez
# que esta regex mede outra coisa por conhecer meia familia. Os verbos de
# efeito do pool novo (`puts`, `brings`, `pushes`, `unblocks`, `clears`,
# `restores`, `moves`, `gives`, `holds`, `keeps`) nao estavam aqui, e a lente
# reprovou 372 de 800 sorteios de copy CORRETA no primeiro autoteste depois da
# troca. Entram tambem os ALVOS (`blood`, `flow`, `pressure`, `supply`,
# `path`): a lente pergunta "o que ele devolve?", e sangue/pressao E' a
# resposta.
# ⛔ Continuam de fora `does`, `is`, `has` e companhia — sao os que produzem o
# caso ruim que a lente existe para pegar.
TR17_DESTINO = re.compile(
    r"\b(back|again|answers?|answered|remembers?|running|hard|returns?|"
    r"alive|life|awake|up|bigger|stopped quitting|has not quit|had not quit|"
    r"not quit|works?|working|"
    r"fills?|filled|opens?|opened|wakes?|woke|hardens?|hardened|feeds?|fed|"
    r"straightens?|straightened|loads?|loaded|fixes?|fixed|thick|stiff|"
    r"puts?|brings?|pushes|push|unblocks?|clears?|restores?|moves?|gives?|"
    r"holds?|keeps?|blood|flow|pressure|supply|path)\b",
    re.I)


def _tr_mecanismo_sem_destino(spec, blocos, achados):
    """TR17 — ⛔ O MECANISMO ANUNCIADO SEM DIZER O QUE ELE DEVOLVE.

    Ed, 2026-08-06: `Gelatin does what honey never could — the gelatin trick.`
    COMPARA o mecanismo com a isca e nao entrega nada em que agir. E' irma da
    regra da FRASE ORFA (§17, causa sem dizer o que ela quebra): la' a causa
    precisa nomear o que quebrou, aqui o mecanismo precisa nomear o que volta.

    A janela e' a frase do literal MAIS a seguinte — varias fundidas boas poem
    o destino logo depois (`The gelatin trick. His {o} has not quit since
    March.`), e cobrar tudo numa frase so' reprovaria copy que funciona.
    """
    for i, fala in enumerate(spec["falas"], 1):
        frases = [f.strip() for f in re.split(r"(?<=[.!?])\s+", fala) if f.strip()]
        for j, f in enumerate(frases):
            if "gelatin trick" not in f.lower():
                continue
            janela = " ".join(frases[j:j + 2])
            if not TR17_DESTINO.search(janela):
                achados.append((
                    "ERRO",
                    "TR17: cena %d nomeia o gelatin trick e nao diz o que ele "
                    "devolve (%r)" % (i, janela[:56])))
            break


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
    VIVA e' a do self-test, que exige os CTAS sem vocativo nenhum.
    """
    cena3 = spec["falas"][-1]
    hits = _achar(cena3, VOCATIVOS)
    if len(hits) > 1:
        achados.append(("AVISO", "TR15: dois vocativos na cena 3 (%s) — o "
                                 "operador mediu vicio de 'brother' e mandou "
                                 "variar" % ", ".join(hits)))


def _tr_troca(spec, blocos, achados):
    """TR1 — ⭐ A TROCA. Sem estes literais o Veo corta, e o argumento inteiro
    do agente morre: a leitura de SUBSTITUICAO depende de mesma mao, mesmo
    ponto, mesma altura, take unico."""
    # ⛔⛔ TR1 MUDOU DE ALVO, NAO FOI APAGADA — 2026-08-08.
    # Ela vigiava o TAKE 02/03: a descida do proxy, a subida da gelatina e o
    # ponto, em batidas com segundos. Esse TAKE morreu quando o operador
    # escolheu preservar o corpo-prova, e a troca desceu para a FALA.
    # ⭐ Uma regra que perde o objeto nao vira lixo: ela vira a lente do objeto
    # NOVO. A troca agora e' um GESTO DITO, e sem o gesto a cena 2 e' um
    # mecanismo qualquer — o angulo se chama TROCA por causa dele.
    # ⛔ Apagar a TR1 aqui seria perder a unica prova de que o bit sobreviveu a'
    # mudanca de midia.
    f2 = (spec["falas"][1] if len(spec.get("falas", [])) > 1 else "")
    if not TR1_GESTO.search(f2):
        achados.append(("ERRO", "TR1: a cena 2 nao tem o GESTO da troca "
                                "(`drop`/`forget`/`put down`/`wrong jar`...) — "
                                "sem ele o angulo vira um mecanismo qualquer, e "
                                "e' o gesto que da' nome ao agente (%r)"
                        % f2[:50]))
    if "gelatin trick" not in f2.lower():
        achados.append(("ERRO", "TR1: a cena 2 sem o literal `gelatin trick` — "
                                "e' o que amarra o criativo a' VSL"))
    if not any(o.lower() in f2.lower() for o in NUCLEO):
        achados.append(("ERRO", "TR1: a cena 2 nao nomeia o orgao. No motor de "
                                "24s quem o nomeava era o TESTEMUNHO, que "
                                "morreu no orcamento — a cota mudou de dono, "
                                "nao caiu"))

def _tr_sem_crescimento(spec, blocos, achados):
    """TR2 — [D4]: o prop nao cresce, e a promessa e' paga pela cara dela.

    ⚠️ Procura-se o MIOLO INVARIANTE, nunca o template. `TR_SEM_CRESCIMENTO`
    tem dois slots (%s do proxy e %s do gatilho) e chega ao bloco ja'
    formatado — comparar com o template cru da' 100% de falso positivo, que foi
    exatamente o que aconteceu em 400 de 400 sorteios. O trecho abaixo mora
    entre os dois slots e sobrevive a qualquer preenchimento.
    """
    if TR2_MIOLO not in blocos["TAKE 01/02"]:
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
    img, take = blocos["IMAGE 02/02"], blocos["TAKE 02/02"]
    calca = spec["corpo_prova"]["calca"]
    if "his own fist" not in img:
        achados.append(("ERRO", "TR10: IMAGE 02/02 sem 'his own fist' — a "
                                "agencia nao esta' declarada"))
    # ⭐ ancora nova (Ed, 2026-08-01): `centred against the front of his ...`
    # substituiu `beside the lap of his ...` porque o homem esta' DE PE e o
    # `beside` mandava o prop para o quadril. A alavanca e' a mesma — a peca
    # de roupa dando a coordenada sem o termo anatomico.
    # ⚠️ minusculas: a travada ABRE a frase, entao chega com "C" maiusculo.
    if "centred against the front of his " not in img.lower():
        achados.append(("ERRO", "TR10: IMAGE 02/02 sem a ancora de roupa "
                                "travada ('centred against the front of his "
                                "...') — sem ela o prop volta para o quadril"))
    if "both his own fists" not in img.lower():
        achados.append(("ERRO", "TR10: IMAGE 02/02 sem as DUAS maos — uma mao "
                                "so' deixa o Veo escolher o lado e o prop sai "
                                "fora do eixo do corpo (ordem do Ed)"))
    if calca not in img:
        achados.append(("ERRO", "TR10: IMAGE 02/02 sem a peca de roupa sorteada "
                                "— a ancora precisa existir na imagem"))
    if "his eyes on the lens" not in img:
        achados.append(("ERRO", "TR10: IMAGE 02/02 sem o olhar dele na lente — "
                                "sem isso ele e' corpo passivo, e passividade e' "
                                "o que a F12b diz que bloqueia"))
    if "without touching him" not in img:
        achados.append(("ERRO", "TR10: IMAGE 02/02 sem 'without touching him'"))
    if "never touches him" not in take:
        achados.append(("ERRO", "TR10: TAKE 02/02 sem 'never touches him' — e' "
                                "o que separa a TROCA do ELA_DIAGNOSTICA, onde "
                                "o dedo crava no corpo dele"))
    if "keeps his eyes on the lens" not in take:
        achados.append(("ERRO", "TR10: TAKE 02/02 sem o olhar dele na lente — "
                                "a agencia tem de continuar no movimento"))
    for nome in ("IMAGE 02/02", "TAKE 02/02"):
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

    ⚠️ A 02/02 esta' FORA da varredura de proposito, e nao por esquecimento: e'
    o bloco de maior risco do lote (duas pessoas + proxy no colo dele) e a F12c
    manda encolher tudo que for descricao livre ali — "quanto mais info vc da'
    pro Veo, mais municao vc da' pra ele flagrar algo". O recibo ja' cumpriu o
    lastro do 'full recipe' nas duas cenas anteriores; repeti-lo na terceira
    paga superficie de bloqueio sem comprar nada. A versao anterior desta
    funcao exigia o recibo nas tres e reprovava 400 de 400 sorteios contra o
    comentario do proprio montar().
    """
    itens = spec["bancada"]["itens"]
    for nome in ("IMAGE 01/02",):
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
    # ⚠️ A ancora carrega a ETNIA desde 2026-08-06. Quando a narradora passou a
    # nomear a etnia, esta string deixou de casar e o TR18 acusou 1600 de 1600
    # sorteios — o linter da continuidade caiu junto com a mudanca do casting.
    # Ela tem de descrever a narradora COMO ELA E' ESCRITA, senao mede outra.
    ancora = "the same %d-year-old %s woman" % (spec["narradora"]["idade"], et)
    for nome in ("IMAGE 02/02",):
        if ancora.lower() not in blocos[nome].lower():
            achados.append(("ERRO", "TR18: %s sem a ancora '%s' — sem o rosto "
                                    "repetido o Veo troca de pessoa entre as "
                                    "cenas" % (nome, ancora)))
        if spec["narradora"]["marca"] not in blocos[nome]:
            achados.append(("ERRO", "TR18: %s sem a marca facial da narradora "
                                    "por inteiro" % nome))
    img3 = blocos["IMAGE 02/02"]
    if not re.search(r"A %d-year-old %s man" % (spec["corpo_prova"]["idade"], et),
                     img3):
        achados.append(("ERRO", "TR18: IMAGE 02/02 sem o corpo-prova em artigo "
                                "indefinido — ele entra novo na cena 3"))
    if re.search(r"the same \d+-year-old %s man" % et, img3, re.I):
        achados.append(("ERRO", "TR18: IMAGE 02/02 marca o corpo-prova como "
                                "'the same' — promete uma continuidade que "
                                "nunca existiu"))
    # ⚠️ o mesmo objeto, a regua no corpo de QUEM SEGURA: 83% dos lotes saiam
    # com "in his own fist ... as long as HER forearm", contra a letra da TR10.
    if spec["proxy"]["img_dele"] not in img3:
        achados.append(("ERRO", "TR18: IMAGE 02/02 sem a ancora de escala no "
                                "corpo DELE — na cena 3 quem segura e' ele"))


# a isca: o que o espectador RECEBE ao comentar. Sem um destes, o CTA manda
# agir sem dizer em troca de que.
TR19_ISCA = re.compile(
    r"\b(recipe|measurements|ingredients|dose|what to buy|where to buy)\b",
    re.I)


def _tr_isca_nomeada(spec, blocos, achados):
    """TR19 - o CTA nomeia O QUE sera enviado.

    Ed, 2026-08-06, lendo o take 3: "and I'll send it" - enviar o QUE? A isca
    tem de estar expressa. E o unico ponto do video onde se pede uma acao, e
    pedir sem dizer a troca desperdica o take inteiro.

    ⛔⛔ ESTA LENTE ESTAVA MORTA E NINGUEM VIU. A condicao era
    `spec["falas"][-1] if len(spec["falas"]) > 2 else ""` — herdada do motor de
    24s, onde ha' TRES falas. Neste motor ha' DUAS, entao o `else ""` disparava
    sempre e a funcao saia no `return` de cima em 100% dos sorteios. Lente que
    nunca acusa nao e' lente que aprova: e' lente que nunca olhou (licoes §29).
    A cena do CTA e' `falas[-1]` tenha o motor 2 ou 3 falas, que e' o idioma
    que o proprio `short_comum` ja' usa.
    """
    fala = spec["falas"][-1]
    if "comment gelatin" not in fala.lower():
        return
    if not TR19_ISCA.search(fala):
        achados.append((
            "ERRO",
            "TR19: cena 3 pede o comentario e nao diz o que envia (%r)"
            % fala[-58:]))


def _tr_congruencia(spec, blocos, achados):
    """TR11 — a etnia dos DOIS e' a da pagina.

    ⛔⛔ ESTE LINTER FOI INVERTIDO (Ed, 2026-08-06). Ele PROIBIA a etnia da
    narradora — cobrava que ela nunca aparecesse, por causa do [D2]. Era ele
    que garantia o defeito que o operador leu na tela: `pele escura` na UI,
    corpo-prova negro, narradora branca ao lado.

    Agora cobra o contrario: a REF e as tres IMAGE nomeiam a etnia dela, e ela
    e' a mesma da pagina. Congruencia de casting e' inviolavel no CLAUDE.md, e
    quem media estava medindo o avesso.
    """
    et = ETNIA[spec["pagina"]]
    if "%s man" % et not in blocos["IMAGE 02/02"]:
        achados.append(("ERRO", "TR11: IMAGE 02/02 sem a etnia '%s' no "
                                "corpo-prova — congruencia inviolavel com o "
                                "avatar da pagina" % et))
    # ela: cobrada onde ela e' apresentada — o REF e as duas primeiras cenas
    for nome in ("BLOCO 0 (REF)", "IMAGE 01/02"):
        txt = blocos.get(nome, "")
        if "%s woman" % et not in txt:
            achados.append(("ERRO", "TR11: %s sem a etnia '%s' na narradora — "
                                    "e' o defeito que entregava mulher branca "
                                    "com corpo-prova negro" % (nome, et)))
    # e nenhuma outra etnia pode escapar em lugar nenhum
    outra = "Black American" if "white" in et else "white American"
    for nome, txt in sorted(blocos.items()):
        if re.search(r"%s\s+(woman|man)" % re.escape(outra), txt, re.I):
            achados.append(("ERRO", "TR11: %s traz '%s' numa pagina de avatar "
                                    "'%s' — casting cruzado" % (nome, outra, et)))
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
    for nome in ("IMAGE 01/02", "IMAGE 02/02"):
        if "cropped" not in blocos[nome]:
            achados.append(("AVISO", "TR12: %s sem o figurino da fonte "
                                     "('cropped') — 🟡 divergencia do UN1, "
                                     "decisao [D3]" % nome))



def _bandeira_5050(spec, blocos, achados):
    """⭐ A BANDEIRA E' 50/50, e some INTEIRA quando o sorteio diz que nao.

    ⛔ Ordem do operador, 2026-08-04: *"todos os takes estao possuindo bandeiras
    dos EUA, quero algo 50%/50%"*. Ate' aqui ela estava escrita DENTRO da string
    de cada cenario — nao havia eixo para sortear, havia texto.
    ⚠️ A lente varre o TEXTO MONTADO e cobra os dois lados, mais a PROSA: remocao
    por regex em prosa erra em silencio, e silencio e' o que nao pode acontecer.
    """
    sc.lint_bandeira(spec, blocos, achados, rotulo="bandeira 50/50")



# ---------------------------------------------------------------------------
# ⛔⛔ T16-5b — O PRONOME SEM DONO, EM TODAS AS CENAS
# ---------------------------------------------------------------------------
# Ordem do operador, 2026-08-08, lendo o painel do PLACA 16:
#     "...why the gelatin trick exists before she stops asking."
#     -> *"She who??? stopping asking about what????"*
#
# ⚠️ A lente T16-5 original olhava SO' A CENA DO CTA. O defeito estava na cena
# 1, que vem dos pools herdados do motor de 24s. Lente que cobre uma cena de
# duas nao e' lente, e' amostra.
#
# ⛔⛔ E ELA NAO ADIVINHA. Cada motor DECLARA abaixo os pronomes cujo referente
# esta' EM QUADRO. Foi isso que impediu o conserto errado: varrendo por
# CONTAGEM, o TRIO e o DUPLA apareciam com mais de 50% da cena 1 "defeituosa" —
# e ali o `she` de `the one she holds` aponta para a mulher VISIVEL segurando o
# prop gigante, que e' regra do proprio operador ("o segundo prop tem dono
# nomeado: she / her hand / my friend"). Ler as frases custou dez minutos e
# salvou dois motores certos.
#
# ⭐ Quem acrescentar entrada de pool com pronome nu tem de vir aqui declarar
# por que ele tem dono. Declaracao explicita e' o oposto de adivinhacao.
PRONOME_VISUAL = ("his",)

_PRON_NU = re.compile(r"\b(she|her|he|his)\b", re.I)
_TEM_DONO = re.compile(
    r"\b(wife|girlfriend|woman|girl|friend|husband|boyfriend|man|men|guy|"
    r"marriage)\b", re.I)
# ⛔ Verbos que pedem objeto e ficam pendurados sem ele: `stops asking` —
# parando de perguntar O QUE? E' a mesma familia do pronome sem dono, e o
# operador reprovou exatamente esta forma.
_PENDURADO = re.compile(
    r"\b(stops?|starts?|keeps?|quits?)\s+(asking|telling|talking|wondering|"
    r"complaining|noticing|checking)\b"
    r"(?!\s+(what|about|for|the|her|his|you|it|at|to))", re.I)


def _t16_5b(spec, blocos, achados):
    for _i, _fala in enumerate(spec.get("falas") or [], 1):
        if (_PRON_NU.search(_fala) and not _TEM_DONO.search(_fala)
                and not any(_v in _fala.lower() for _v in PRONOME_VISUAL)):
            achados.append((
                "ERRO",
                "T16-5b: cena %d usa pronome NU sem dizer de quem se trata e "
                "sem referente em quadro declarado — o espectador gasta o "
                "segundo dele perguntando `quem?` (%r)" % (_i, _fala[:64])))
        _p = _PENDURADO.search(_fala)
        if _p:
            achados.append((
                "ERRO",
                "T16-5b: cena %d tem `%s` sem objeto — parando de perguntar O "
                "QUE? Verbo pendurado e' a mesma familia do pronome sem dono"
                % (_i, _p.group(0))))

# ---------------------------------------------------------------------------
# ⭐⭐⭐ CT1..CT7 — O CONTRATO DE COPY 16s, LIGADO
# ---------------------------------------------------------------------------
# A lente mora no `short_comum` (uma regra, um lugar) e o motor so' a chama.
# ⭐ `isca_absurda=True`: este angulo E' uma promessa falsa que ele proprio
# desmente meio segundo depois, entao o CT7 nao cobra verbo de ereccao no take
# 1 — proibi-lo ali mataria o angulo. No take 2, que e' claim NOSSO, ele
# continua cobrado.
def _ct16(spec, blocos, achados):
    sc.lint_copy16(sys.modules[__name__], spec, achados, isca_absurda=True)


# ⛔⛔ LENTE APOSENTADA — "substantivo repetido no video" (AVISO do `lint_curto`)
# -----------------------------------------------------------------------------
# O `lint_curto` avisa quando o mesmo substantivo do NUCLEO aparece em mais de
# uma cena. Essa regra nasceu no formato de 24s/5 cenas, onde repetir e' bordao.
# O **CT4 do contrato 16s a REVERTE**: em duas cenas o corte zera a memoria de
# trabalho e o apelido TEM de ser o mesmo nos dois takes. Manter o AVISO seria
# ter, no mesmo `lint()`, uma lente exigindo o que a outra reprova — e o
# operador aprenderia a ignorar o relatorio.
# ⛔ Nao se apaga a regra no `short_comum` (ela e' certa nos motores de 3 cenas,
# e o arquivo e' compartilhado): filtra-se AQUI, no unico motor que declara a
# reversao. Fonte: CONTRATO-COPY-16S.md §CT4.
_AVISO_APOSENTADO = "substantivo repetido no video"


def lint(spec, blocos):
    # ⚠️ `teto_total` explicito: o padrao do `lint_curto` e' a soma dos tetos
    # (82), que aqui e' o PISO do orcamento da doutrina — o AVISO dispararia
    # acima do numero que a TR14 exige como MINIMO. A borda de cima e' 96.
    achados = sc.lint_curto(
        sys.modules[__name__], spec, blocos, (1, 2), TETO_FALA,
        literais=("gelatin trick",), teto_total=TETO_TOTAL,
        extras=(_ct16, _t16_5b, _tr_crendice, _tr_claim_prazo,
                _tr_segunda_pessoa,
                _tr_pronome_orfao, _tr_mecanismo_sem_destino, _tr_isca_nomeada,
                _tr_proxy_mudo, _tr_eco, _tr_orcamento, _tr_batismo, _tr_cta,
                _tr_gates, _tr_troca, _tr_sem_crescimento, _tr_agencia,
                _tr_tokens, _tr_marca, _tr_verbos, _tr_recibo, _tr_ancoras,
                _tr_congruencia, _tr_voz, _tr_figurino,
                _bandeira_5050))
    return [a for a in achados if not a[1].startswith(_AVISO_APOSENTADO)]


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

# ⭐ O CADEADO. So' o PROXY por ora — e' o que o operador pediu. Acrescentar
# outro eixo aqui e' UMA linha no `sortear` (`travas.get("x") or ...`) mais o
# nome nesta lista; sem a linha no sortear o botao aparece e nao trava nada.
EIXOS_TRAVAVEIS = ["proxy"]


# ⭐⭐ O DROPDOWN DA NARRADORA — e' ELE que da' FUNCAO ao campo `rotulo`.
# ⛔ Sem esta linha o rotulo seria comentario caro: 28 textos escritos, medidos
# e travados, e nenhum olho humano os veria. Forma sem funcao e' o defeito que
# este repo mais paga (licoes-de-construcao §41), e um label que nao aparece na
# tela e' a versao mais barata dele.
# ⛔ POR QUE DROPDOWN E NAO `TRAVAS_UI`: a barra de travas desenha UM BOTAO POR
# OPCAO, lado a lado. Com 28 REFs ela estoura a largura da janela. Contrato
# aditivo da `ui_agente` (2026-08-13).
# ⚠ O campo exibido e' `rotulo`, NAO `id`: a `ui_agente` monta o mapa
# texto -> id, entao o operador escolhe '29y · ruiva longa + sardas no rosto' e o motor recebe 'ruiva_sardas'. Um menu de ids
# obrigaria a abrir o codigo para saber o que se escolheu.
# ⚠ E o rotulo da tela e' o MESMO texto do `EIXOS_UI` acima (`A NARRADORA`):
# dois nomes para o mesmo eixo confundem quem opera.
DROPDOWNS_UI = [("narradora", "A NARRADORA", "NARRADORAS", "rotulo")]

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
    # ⛔ CT4: o apelido do video e' UM so'. Antes esta funcao lia um termo da
    # cena 1 e outro da cena 2 (com `padrao="soldier"`, que nem existe mais no
    # NUCLEO) — ou seja, ela REINTRODUZIA pela interface o defeito que o
    # sorteio acabou de corrigir. Le-se o da cena 1 e ele vale para as duas.
    _o = sc.orgao_de(sys.modules[__name__], spec["falas"][0])
    orgaos = [_o, _o, _o]
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
    # ⛔ CT4: um apelido por video (ver a nota no `sortear`).
    _o = rng.choice(sc.APELIDOS_16)
    orgaos = [_o, _o, _o]
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
# ⛔ FUNDIDAS saiu: o beat morreu na fusao. Entra TROCAS16, que o substitui
# e cujo piso e' 10 (doze entradas escritas em 7-9 palavras).
# ⚠️ 2026-08-10: os pisos SOBEM junto com a reforma de copy. Ordem permanente do
# operador — *"nao sacrifique, dimira ou faca quaisquer regressao no agente que
# ocasione perda de entropia"* — e piso que fica para tras autoriza a proxima
# edicao a encolher o pool de volta.
MIN_COPY = {"CRENDICES": 20, "DESMENTIDOS": 14, "TROCAS16": 14, "CTAS": 18,
            "GATES": 14}


def autoteste(n_por_pagina=80, seed=7, degrau=None):
    falhas = []

    # ⛔⛔ O CONTRATO DO `rotulo` — as quatro coisas que o dropdown exige.
    # ⚠ A UNICIDADE nao e' capricho: a `ui_agente._barra_dropdowns` monta o
    # mapa com `if txt and txt not in mapa`, entao dois rotulos iguais fazem a
    # SEGUNDA narradora desaparecer do menu — em silencio, sem erro, sem log.
    # Pool de 28 que o operador so' consegue alcancar em 27 e' a mesma
    # familia do botao que mente, so' que por colisao de texto.
    # ⚠ O TETO DE 42 e' a largura do combobox (`width=38` + folga): rotulo
    # maior fica cortado na tela, e rotulo cortado volta a ser ilegivel, que e'
    # exatamente o problema que ele veio resolver.
    _sem = [x["id"] for x in NARRADORAS if not x.get("rotulo")]
    if _sem:
        falhas.append("ROTULO: %d entrada(s) de NARRADORAS sem rotulo — o "
                      "dropdown cai no `id` e o operador le' %r"
                      % (len(_sem), _sem[0]))
    _rot = [x.get("rotulo") or "" for x in NARRADORAS]
    _rep = sorted({r for r in _rot if _rot.count(r) > 1})
    if _rep:
        falhas.append("ROTULO: %d rotulo(s) repetido(s) (%r) — a segunda "
                      "narradora some do dropdown sem erro nenhum"
                      % (len(_rep), _rep[0]))
    _longos = [r for r in _rot if len(r) > 42]
    if _longos:
        falhas.append("ROTULO: %d rotulo(s) acima de 42 chars (%r, %d) — "
                      "estoura a largura do menu"
                      % (len(_longos), _longos[0], len(_longos[0])))

    # ⛔⛔ E O `DROPDOWNS_UI` TEM DE APONTAR PARA COISA QUE EXISTE. A
    # `ui_agente` le' o pool por `getattr(motor, nome, [])` e o campo por
    # `e.get(campo) or e.get("id")`: um nome de pool errado devolve lista vazia
    # e desenha um menu VAZIO, e um campo errado cai no `id` — nos dois casos
    # sem uma linha de erro. Falha silenciosa de UI e' a que chega ao operador.
    for _ch, _tela, _pool_nome, _campo in DROPDOWNS_UI:
        _pool = globals().get(_pool_nome)
        if not _pool:
            falhas.append("DROPDOWNS_UI: o pool %r nao existe (ou esta' vazio) "
                          "— o menu %r sai vazio na tela"
                          % (_pool_nome, _tela))
            continue
        _faltam = [e.get("id") for e in _pool if not e.get(_campo)]
        if _faltam:
            falhas.append("DROPDOWNS_UI: %d entrada(s) de %s sem o campo %r "
                          "— o menu cai no `id` em %r"
                          % (len(_faltam), _pool_nome, _campo, _faltam[0]))
        if _tela not in [u[1] for u in EIXOS_UI if u[0] == _ch]:
            falhas.append("DROPDOWNS_UI: o eixo %r se chama %r no dropdown e "
                          "outra coisa no EIXOS_UI — dois nomes para o mesmo "
                          "eixo confundem quem opera" % (_ch, _tela))

    # ⛔⛔ E O MENU TEM DE FIXAR DE VERDADE (licoes-de-construcao §41:
    # verificar a FORMA e declarar pronto sem verificar a FUNCAO). As tres
    # lentes acima olham o TEXTO; esta olha o EFEITO. Sem ela, alguem mexe no
    # `sortear`, o menu continua desenhado e bonito, e passa a devolver outra
    # mulher — que e' exatamente o botao que mente.
    _alvo = NARRADORAS[len(NARRADORAS) // 2]["id"]
    _pag = sorted(ETNIA)[0]
    _fix = {sortear(_pag, random.Random(9000 + i), {},
                    {"narradora": _alvo})["narradora"]["id"] for i in range(8)}
    if _fix != {_alvo}:
        falhas.append("DROPDOWNS_UI: escolher %r no menu devolveu %r — o "
                      "`sortear` nao le' `travas['narradora']` e o dropdown "
                      "virou botao que mente" % (_alvo, sorted(_fix)))

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
            "TROCAS16": len(TROCAS16),
            "CTAS": len(CTAS), "GATES": len(GATES),
            }
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
    # ⚠️ BARREIRAS saiu da varredura junto com o pool. A trava de vocativo
    # continua VIVA nos CTAS, que e' onde ela importa: o vocativo so' pode
    # morar nos GATES.
    for nome, pool in (("CTAS", CTAS),):
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
    # ⛔ A cena 1 continua sendo crendice + desmentido. A cena 2 mudou de pools
    # inteiros: era fundida + prova, agora e' troca + CTA + gate.
    faixas = {
        1: ([_palavras(c["txt"]) for c in CRENDICES],
            [_palavras(d) for d in DESMENTIDOS], extra + extra_o),
    }
    for i, (a_, b_, ex) in sorted(faixas.items()):
        if min(a_) + min(b_) < PISO_FALA[i]:
            falhas.append("TR14: cena %d pode sair com %d palavras (piso %d) — "
                          "o pool nao alcanca o piso do operador"
                          % (i, min(a_) + min(b_), PISO_FALA[i]))
        if max(a_) + max(b_) + ex > TETO_FALA[i]:
            falhas.append("TR14: cena %d pode estourar (%d, teto %d)"
                          % (i, max(a_) + max(b_) + ex, TETO_FALA[i]))

    # ⭐ A CENA 2 TAMBEM E' ENUMERADA — 2026-08-10. Ela ficava de fora porque o
    # solver "resolvia" o teto filtrando entradas, e filtrar e' justamente o que
    # MATA entrada de pool em silencio: o lote sai dentro do teto e ninguem ve'
    # que metade do pool nunca foi ao ar. Aqui as duas bordas sao medidas.
    _t2 = [_palavras(x.format(s="x", o="x")) for x in TROCAS16]
    _g2 = [_palavras(x) for x in GATES]
    _c2w = [_palavras(x) for x in CTAS]
    if min(_t2) + min(_g2) + min(_c2w) < PISO_FALA[2]:
        falhas.append("TR14: cena 2 pode sair com %d palavras (piso %d)"
                      % (min(_t2) + min(_g2) + min(_c2w), PISO_FALA[2]))
    if max(_t2) + max(_g2) + max(_c2w) > TETO_FALA[2]:
        falhas.append("TR14: cena 2 pode estourar (%d, teto %d) — com o pior "
                      "caso acima do teto o solver comeca a FILTRAR entradas, "
                      "e entrada filtrada e' entrada morta"
                      % (max(_t2) + max(_g2) + max(_c2w), TETO_FALA[2]))

    # ⭐⭐ [ALCANCE] TODA ENTRADA DE POOL TEM DE SER SORTEAVEL — e este motor e'
    # a razao mais forte para a trava existir. MEDIDO no `troca_short.py` de
    # 24s, antes de portar:
    #
    #     FUNDIDAS (15) x PROVAS (12) = 180 combinacoes
    #     cabem no teto de 25:  TRES  (2%)
    #     FUNDIDAS que nao cabem nem com a menor PROVA:  14 de 15
    #     PROVAS que nao cabem nem com a menor FUNDIDA:   9 de 12
    #
    # A cena 2 de la' entrega 15 falas distintas em 300 videos porque o pool
    # nao cabe no proprio teto — 14 das 15 FUNDIDAS aprovadas nunca vao ao ar.
    # ⚠️ E NAO E' O PISO: testei piso 18, 20, 22, 25 e 26 e o numero nao muda.
    # A causa e' o comprimento das entradas, nao a faixa declarada.
    # ⛔ Aqui a mesma cena da' 52% de cobertura com ZERO entrada inalcancavel, e
    # esta trava garante que continue assim.
    _mT = min(_palavras(x.format(s="x", o="x")) for x in TROCAS16)
    _mC = min(_palavras(x) for x in CTAS)
    _mG = min(_palavras(x) for x in GATES)
    for _nome, _pool, _outros in (
            # ⚠️ o `o=` tem de ser um termo VIVO do NUCLEO: era `soldier`, que
            # foi aposentado na reforma de 2026-08-10 (britanismo).
            ("TROCAS16", [x.format(s="crushed cinnamon", o="pecker")
                          for x in TROCAS16], _mC + _mG),
            ("CTAS", CTAS, _mT + _mG),
            ("GATES", GATES, _mT + _mC)):
        _teto = TETO_FALA[2] - _outros
        _mortas = [x for x in _pool if _palavras(x) > _teto]
        if _mortas:
            falhas.append("[ALCANCE] %d entrada(s) de %s nunca sao sorteadas "
                          "(teto real do eixo: %d palavras): %s"
                          % (len(_mortas), _nome, _teto, _mortas[:2]))

    # ⭐ TR1 no nivel do POOL: o gesto da troca, o literal e o orgao em TODAS as
    # entradas. Sem isso a lente de fala passaria por sorte, nao por garantia.
    for _x in TROCAS16:
        if not TR1_GESTO.search(_x):
            falhas.append("TR1: entrada de TROCAS16 sem o GESTO: %r" % _x)
        if "gelatin trick" not in _x.lower():
            falhas.append("TR1: entrada de TROCAS16 sem o literal: %r" % _x)
        if "{o}" not in _x:
            falhas.append("TR1: entrada de TROCAS16 sem o orgao: %r" % _x)

    # --- 400 sorteios -------------------------------------------------------
    rng = random.Random(seed)
    freq, total_eixo, erros, avisos, n = {}, {}, 0, 0, 0
    for pag in sorted(ETNIA):
        ledger = {}
        for _ in range(n_por_pagina):
            spec = sortear(pag, rng, ledger, {"degrau": degrau})
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
        spec = sortear(a.pagina, rng, ledger, {"degrau": a.degrau})
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
