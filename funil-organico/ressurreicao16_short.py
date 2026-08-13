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

⭐⭐ REFORMA TOTAL DA COPY FALADA — 2026-08-10 (CONTRATO DE COPY 16s)
--------------------------------------------------------------------
Ordem do operador: *"agentes troca16, ressurreicao16, exterior16, flagrante16,
pee16, escandalo16, colo16 precisam de reformulacao total de suas copys"*.
Doutrina: `CONTRATO-COPY-16S.md` · lente: `short_comum.lint_copy16` ·
medidor: `python funil-organico/medir_copy16.py --motor ressurreicao16`.

Medido ANTES, 200 sorteios: CT1 100% · CT2 30% · CT3 100% · CT4 100% · CT5 78%
· CT6 100%. DEPOIS: 0% nas sete. O que mudou, e SO' isto — nenhum bloco
IMAGE/TAKE e nenhum pool de cena foi tocado:

  · a estrutura do take 2 passa a ser mecanismo COM RAZAO -> prova -> follow ->
    CTA, e o CTA e' a ULTIMA sentenca do video (CT1). O gate saiu de depois do
    pedido, onde estava em 100% dos sorteios;
  · o pool METADES16 morreu inteiro (CT5): ele punha `cayenne`/`pomegranate` na
    boca a um segundo da keyword, numa automacao que casa palavra exata. O eixo
    `receita` continua vivo — so' nao sai mais pela boca;
  · UM apelido do orgao por video, repetido nos dois takes (CT4). ⛔ ISTO
    REVERTE a regra antiga "tres substantivos distintos, um por cena" deste
    motor, e a lente `substantivo repetido no video` do `lint_curto` foi
    APOSENTADA aqui, com o motivo escrito no `lint`;
  · todo hook enuncia a FALHA dele com dano concreto (CT2), inclusive nos
    degraus 3/4/5 — e o degrau 3, declarado em DEGRAUS desde sempre, ganhou
    pool (a flag caia no `or HOOKS` e mentia);
  · os quatro beats do take 2 tem tamanho UNICO (8/5/3/9 = 25) e o bullet do
    take 1 tem cinco: com tamanho livre o solver sorteia PARES e a entrada
    curta leva o lote (medido 16 para 1). [ALCANCE] 14/14 em todos os pools.

⛔ Dois defeitos de CAMINHO DE CLIQUE que so' existiam na JANELA foram
corrigidos junto, porque a reforma passava por eles: `_refazer_falas` lia
`falas[2]` (IndexError em todo botao de copy da UI) e o `autoteste` dividia por
zero na "cena 3". Nenhum medidor via — todos olham o `sortear`.

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
# ⛔ Ledger proprio: 16s e 24s nao gastam o historico um do outro.
LEDGER = os.path.join(AQUI, ".ressurreicao-16-ledger.json")

TITULO = "AGENTE RESSURREICAO 16"
SUBTITULO = ("o despejo que ressuscita — o prop murcho que alonga na tela, "
             "dentro da coluna de po' · 3 cenas")
SLUG = "ressurreicao-16"

# ⛔⛔ DUAS CENAS. A 2 (a receita na bancada) morre como QUADRO e sobrevive
# como FALA; a fundida herda o quadro da 3, que e' o payoff.
# ⚠️ ESTE CAMPO FICOU PARA TRAS NO PORTE e o app QUEBRAVA ao abrir:
# `IndexError` em `_preencher_copy`, porque a UI monta uma caixa de texto
# por rotulo de CENAS_UI e pedia a fala[2], que nao existe mais. Nenhum
# medidor pegou — todos olham o motor, e este defeito so' existe na JANELA.
CENAS_UI = ["1 · O DESPEJO E O CRESCIMENTO", "2 · A RECEITA + PROVA + CTA"]

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
# ⛔ 34 estava ACIMA DO FISICO (32 = 8s a 4,0 palavras/s, licoes §5).
# Nao estourava por sorte do pool — o maximo GERADO medido em 600
# sorteios era 30. Mas teto declarado acima da capacidade e' bomba
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

# ⭐⭐ MODO BELA — com o filtro de banidos do proprio motor (RS23).
MODO_BELA = True

# ⛔⛔ DUAS CENAS no teto FISICO de 25 palavras. O motor de 24s declarava
# 32 na cena 2 com PISO 26 — par impossivel em que todo sorteio viola um
# dos dois, e por isso ele vivia na lista dos que cortam fala: a menor
# FUNDIDA de la' tem 22 palavras e o menor par com o resto da' 26.
# ⭐ Aqui a fundida e' reconstruida em eixos que cabem por construcao, e o
# [ALCANCE] do autoteste reprova entrada que nao alcanca.
TETO_FALA = {1: 25, 2: 25}
PISO_FALA = {1: 16, 2: 18}

# ⚠️ A borda de CIMA da faixa 82-96 da doutrina. ⛔ Nao usar a soma dos tetos
# (91): o AVISO por video dispararia abaixo do numero que a faixa exige.
TETO_TOTAL = 96

# Congruencia inviolavel: etnia do CORPO-PROVA = etnia do avatar da pagina.
# ⛔ A narradora NAO usa este dict — ela e' solta (ver NARRADORAS), e o motor
# nunca escreve adjetivo de etnia junto dela.
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

NUCLEO = ["Johnson", "pecker", "wiener", "tool", "soldier"]
# ⭐ OS DIRETOS — os tres que NOMEIAM o orgao. `tool`, `soldier` e
# `old boy` sao apelido afetivo e suavizam; entram em minoria.
NUCLEO_DIRETO = ["Johnson", "pecker", "wiener"]


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
# ⛔ REESCRITA EM 2026-08-03, com a substancia virando LIQUIDA. A versao de po'
# dizia `thickens into a wide column and the <prop> is hidden INSIDE it`: volume
# opaco engolindo o objeto. Liquido nao tem volume — tem LAMINA. Entao a oclusao
# passa de "dentro da coluna" para "atras da cortina": o jato ALARGA numa folha
# que corre pela frente do prop, e o reconhecimento vem quando a ponta reaparece
# na altura nova. Mesma funcao (o morph acontece oculto, o Veo nao precisa
# resolver mudanca de forma em campo aberto), fisica outra.
# ⚠️ SELO 🟡 — a versao de po' tinha medicao de fonte; esta e' traducao de
# mecanica, sem render nosso ainda. Sobe a 🟢 no primeiro take que sair.
RS_JATO_MASCARA = (
    "A third of a second before it changes, %s widens into a broad falling "
    "sheet that runs down the whole front of the %s, and it is hidden behind "
    "that sheet and cannot be seen. It comes back out of the running %s already "
    "at its new length, %s first. The sheet narrows to a thread again the "
    "instant it stops."
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

    # ⛔ LEI DO REF (2026-08-03): linda, jovem, sex appeal alto.
    # A ancora facial (P6) continua obrigatoria, mas vem do lado bonito.
    {"id": "ruiva_sardas", "idade": 30,
     "cabelo": "long copper-red hair falling loose past her shoulders",
     "oculos": "",
     "porte": "slim with a narrow waist",
     "rosto": "a light dusting of freckles across her nose and green eyes",
     "roupa": "a cropped dark-green ribbed tank top and black leggings"},
    {"id": "loira_ondas", "idade": 29,
     "cabelo": "long honey-blonde waves pushed back off her face",
     "oculos": "",
     "porte": "tall and long-legged",
     "rosto": "a small dark beauty mark just above her lip",
     "roupa": "a cropped white ribbed tank top and high-waisted black leggings"},
    {"id": "afro_solto", "idade": 29,
     "cabelo": "a full soft afro worn wide and loose",
     "oculos": "",
     "porte": "slim and lightly toned through the arms",
     "rosto": "high cheekbones and a small mole on her right cheekbone",
     "roupa": "a cropped mustard knit top and a thin gold chain"},
    {"id": "morena_rabo", "idade": 31,
     "cabelo": "glossy dark-brown hair in a high sleek ponytail",
     "oculos": "",
     "porte": "slim through the waist with full hips",
     "rosto": "large dark eyes and a shallow dimple in her left cheek",
     "roupa": "a fitted black scoop-neck top and dark jeans"},
    {"id": "tranca_longa", "idade": 28,
     "cabelo": "waist-length box braids gathered over one shoulder",
     "oculos": "",
     "porte": "tall and slim-hipped",
     "rosto": "full lips and a tiny beauty spot at the corner of her right eye",
     "roupa": "a cropped terracotta rib tank and gold hoop earrings"},
    # ⚠️ 2026-08-13: a CICATRIZ saiu do `rosto`. O cabecalho manda a ancora
    # vir "do lado bonito" e a entrada escrevia `faint scar` — regra no
    # comentario, contrario no dado. E' o pool que o operador reprovou no
    # PLACA 16 (*"esses caras tao parecendo mendigo"*). A ancora continua
    # (pinta no fim da sobrancelha), o eixo `ancora` do medidor segue
    # preenchido, e nada de deterioracao entra no prompt.
    {"id": "platinada_bob", "idade": 28,
     "cabelo": "a bleached-platinum bob cut sharp at the jaw",
     "oculos": "",
     "porte": "petite and fine-boned",
     "rosto": "pale grey eyes and a small dark mole at the end of her right eyebrow",
     "roupa": "a cropped light-grey tank top and black leggings"},
    {"id": "castanha_franja", "idade": 28,
     "cabelo": "long chestnut hair with a soft curtain fringe",
     "oculos": "",
     "porte": "slim and softly built",
     "rosto": "a heart-shaped face and a small dark mole under her left eye",
     "roupa": "a fitted cream ribbed top and pale denim shorts"},
    {"id": "cachos_ruivos", "idade": 30,
     "cabelo": "loose auburn curls worn long and wide",
     "oculos": "",
     "porte": "slender with strong shoulders",
     "rosto": "freckled cheeks and one dimple that only shows on the left",
     "roupa": "a cropped olive tank top and black leggings"},
    {"id": "preta_lisa", "idade": 33,
     "cabelo": "long jet-black hair worn straight and glossy",
     "oculos": "",
     "porte": "tall and athletic through the legs",
     "rosto": "sharp cheekbones and a small gold stud in her left nostril",
     "roupa": "a fitted burgundy wrap top and dark jeans"},
    {"id": "coque_bagunca", "idade": 30,
     "cabelo": "sandy-blonde hair twisted into a loose messy bun",
     "oculos": "",
     "porte": "slim with a flat stomach",
     "rosto": "blue eyes set wide apart and a light spray of freckles",
     "roupa": "a cropped pale-blue tank top and white shorts"},
    {"id": "cacheada_media", "idade": 32,
     "cabelo": "shoulder-length dark curls with warm highlights",
     "oculos": "",
     "porte": "narrow-waisted and lightly toned",
     "rosto": "a full mouth and a small crescent birthmark at her right temple",
     "roupa": "a fitted rust-orange top with the sleeves pushed up"},
    {"id": "morena_solta", "idade": 29,
     "cabelo": "long dark-brown hair loose and slightly wavy",
     "oculos": "",
     "porte": "tall and slim through the waist",
     "rosto": "wide hazel eyes and a small dimple in her chin",
     "roupa": "a cropped charcoal ribbed tank top and black leggings"},
    {"id": "loira_trancinha", "idade": 31,
     "cabelo": "pale blonde hair in a single loose side braid",
     "oculos": "",
     "porte": "petite and lightly muscled",
     "rosto": "clear blue eyes and a tiny freckle on her left eyelid",
     "roupa": "a fitted white cropped tee and high-waisted jeans"},
    {"id": "crespa_alta", "idade": 34,
     "cabelo": "a long twist-out worn big and off the face",
     "oculos": "",
     "porte": "tall and strong-shouldered",
     "rosto": "a wide bright smile and a small mole above her left brow",
     "roupa": "a cropped emerald knit top and thin gold hoops"},
    {"id": "ruiva_curta", "idade": 29,
     "cabelo": "a short tousled copper crop swept to one side",
     "oculos": "",
     "porte": "slim and narrow-shouldered",
     "rosto": "grey-green eyes and freckles scattered over her collarbones",
     "roupa": "a cropped black tank top and light denim shorts"},
    {"id": "castanha_alta", "idade": 31,
     "cabelo": "long light-brown hair with sun-lightened ends",
     "oculos": "",
     "porte": "tall and long-limbed",
     "rosto": "a straight nose and a small dark mole beside her mouth",
     "roupa": "a fitted sand-coloured rib top and dark leggings"},
    # -----------------------------------------------------------------------
    # + 2026-08-13: DOZE narradoras novas (16 -> 28). Ordem do operador:
    # *"melhore a aparencia e shape desses homens"* e *"aumente o pool de
    # opcoes substancialmente, tambem dos ambientes"*.
    # ⚠️ Dezesseis era o menor pool feminino dos tres motores deste grupo, e
    # com o sorteio evitando so' as recentes a mesma cara voltava a cada tres
    # videos. Quem ve o lote inteiro de uma vez e' o operador.
    # ⛔ AS TRAVAS DE CIMA VALEM SEM EXCECAO: piso de idade 28
    # (IDADE_MINIMA_NARRADORA), LEI DO REF (linda, jovem), ancora facial (P6)
    # obrigatoria e sempre do lado BONITO, e cada entrada difere das outras em
    # pelo menos TRES eixos — que aqui sao CAMPOS SEPARADOS, e' por isso que a
    # diversidade e' auditavel por enumeracao em vez de aferida a olho.
    # ⛔ Zero `scar`, `gap between teeth`, `sun spots`, `weathered`, `sunken`,
    # `gaunt`: e' a lista que ja' custou lote no PLACA 16.
    # ⛔ Zero cor de pele — a narradora e' SOLTA na etnia e o cabelo e' o
    # descritor mais etnico que existe; cor escrita aqui poe duas vozes no
    # mesmo sintagma e o gerador resolve inventando.
    # ⛔ `oculos` nasce VAZIO nas doze, e isso e' decisao declarada, nao
    # esquecimento: a excecao ("ressurreicao16_short.py", "NARRADORAS",
    # "oculos") existe em `medir_personagens.EXCECOES` por ordem — oculos de
    # leitura brigam frontalmente com a LEI DO REF. O eixo fica zerado de
    # proposito e o gate sabe disso.
    # -----------------------------------------------------------------------
    {"id": "mecha_prata", "idade": 32,
     "cabelo": "long dark hair with one bleached-platinum streak at the front",
     "oculos": "",
     "porte": "lean and strong through the shoulders",
     "rosto": "smooth-skinned with a small mole at the corner of her right eye",
     "roupa": "a cropped ink-blue rib tank and black leggings"},
    {"id": "bantu_knots", "idade": 30,
     "cabelo": "dark hair set in bantu knots in even rows",
     "oculos": "",
     "porte": "compact and narrow-waisted",
     "rosto": "full lips and a small gold hoop through her left nostril",
     "roupa": "a cropped ivory rib tank and a flat gold collar"},
    {"id": "pixie_cobre", "idade": 29,
     "cabelo": "a short copper pixie cut swept off the forehead",
     "oculos": "",
     "porte": "petite and lightly muscled",
     "rosto": "freckles across her nose and a single dimple on the left",
     "roupa": "a cropped stone-grey tank top and small gold studs"},
    {"id": "ondas_mel", "idade": 31,
     "cabelo": "honey-brown hair falling in loose waves past her shoulders",
     "oculos": "",
     "porte": "tall and long-limbed",
     "rosto": "wide green eyes and a beauty mark under her left cheekbone",
     "roupa": "a fitted cream wrap top and dark jeans"},
    {"id": "rabo_trancado", "idade": 28,
     "cabelo": "a long braided ponytail pulled high off the neck",
     "oculos": "",
     "porte": "a strong build with square shoulders",
     "rosto": "lightly tanned with a small cleft in her chin",
     "roupa": "a cropped plum knit top and gold drop earrings"},
    {"id": "crespo_tapered", "idade": 33,
     "cabelo": "a short tapered natural cut faded at the sides",
     "oculos": "",
     "porte": "slim with a long neck",
     "rosto": "high cheekbones and a small beauty mark above her lip",
     "roupa": "a cropped mustard knit top and thin gold hoops"},
    {"id": "bob_mel", "idade": 29,
     "cabelo": "a blunt honey-blonde bob cut level at the jaw",
     "oculos": "",
     "porte": "small-framed and lightly toned",
     "rosto": "clear blue eyes and a shallow dimple in her chin",
     "roupa": "a fitted white cropped tee and pale denim shorts"},
    {"id": "locs_longas", "idade": 34,
     "cabelo": "long slim locs gathered back off her face",
     "oculos": "",
     "porte": "long-limbed and narrow through the waist",
     "rosto": "a wide bright smile and a small dark mole on her jawline",
     "roupa": "a cropped emerald rib tank and stacked gold bangles"},
    {"id": "castanha_meio", "idade": 32,
     "cabelo": "mid-length dark-brown hair tucked behind one ear",
     "oculos": "",
     "porte": "slim and broad-shouldered",
     "rosto": "a light spray of freckles and a small gold stud high in her right ear",
     "roupa": "a cropped charcoal tank top and high-waisted jeans"},
    {"id": "ruiva_longa", "idade": 30,
     "cabelo": "long dark-red hair worn straight and glossy",
     "oculos": "",
     "porte": "full-figured with a narrow waist",
     "rosto": "green eyes and a beauty mark at the corner of her mouth",
     "roupa": "a fitted burgundy scoop-neck top and dark leggings"},
    {"id": "trancas_finas", "idade": 31,
     "cabelo": "waist-length micro braids swept over one shoulder",
     "oculos": "",
     "porte": "lean and long-legged",
     "rosto": "smooth-skinned with a small dimple in her left cheek",
     "roupa": "a cropped terracotta rib tank and gold hoop earrings"},
    {"id": "topete_alto", "idade": 35,
     "cabelo": "thick dark hair pulled up into a high topknot",
     "oculos": "",
     "porte": "compact and lightly muscled",
     "rosto": "lightly tanned with a small mole above her right brow",
     "roupa": "a cropped sage-green tank top and a slim gold watch"},
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
     "antes": "a whole baby eggplant, uncut, with its green star crown still on it and the smooth end below, dark purple and glossy, no longer than her palm and as thick as her wrist",
     "depois": "as long as her forearm and still no thicker than her wrist, its sides running almost parallel",
     "dele": "a deep-purple eggplant as long as his forearm and no thicker than his wrist, the crown still pointing up"},
    {"id": "pepino", "nome": "cucumber", "tom": "escuro",
     "topo": "its blunt blossom end",
     "negacao": "No snake, no worm, no eel, nothing alive, nothing with a face.",
     "antes": "a whole squat pickling cucumber, uncut, both blunt ends still on it, dark green and dull, no longer than her palm and as thick as her wrist",
     "depois": "as long as her forearm and still no thicker than her wrist, its sides running almost parallel",
     "dele": "a long smooth dark-green cucumber as long as his forearm and no thicker than his wrist"},
    {"id": "cenoura", "nome": "carrot", "tom": "escuro",
     "topo": "its green leaf-tops", "negacao": "",
     "antes": "a whole stubby carrot, uncut, its green leaf-tops still attached and its root tip still tapering, the skin rough, no longer than her palm and as thick as her wrist",
     "depois": "as long as her forearm and still no thicker than her wrist, tapering evenly to the tip",
     "dele": "a large raw carrot as long as his forearm and no thicker than his wrist, the skin still rough"},
    {"id": "daikon", "nome": "daikon", "tom": "claro",
     "topo": "its leafy green top",
     "negacao": "No snake, no worm, no tentacle, nothing alive, nothing with a face.",
     "antes": "a whole young daikon radish, uncut, its leafy green top still on it and its root tail still tapering, white and smooth, no longer than her palm and as thick as her wrist",
     "depois": "as long as her forearm and still no thicker than her wrist, straight from base to tip",
     "dele": "a pale daikon radish as long as his forearm and no thicker than his wrist, the tapered end pointing up"},
    {"id": "pastinaga", "nome": "parsnip", "tom": "claro",
     "topo": "its tapering root tip", "negacao": "",
     "antes": "a whole young parsnip, uncut, its rounded crown and tapering root tip both still on it, cream-coloured, no longer than her palm and as thick as her wrist",
     "depois": "as long as her forearm and still no thicker than her wrist, the taper stretched out long",
     "dele": "a thick cream-coloured parsnip as long as his forearm and no thicker than his wrist"},
    {"id": "linguica", "nome": "sausage", "tom": "escuro",
     "topo": "its twisted tied end",
     "negacao": "No snake, no worm, no eel, no tentacle, nothing alive, nothing with a face.",
     "antes": "a whole short smoked sausage link, uncut, twisted and tied closed at both ends, the casing taut and dark, no longer than her palm and as thick as her wrist",
     "depois": "as long as her forearm and still no thicker than her wrist, the casing smooth down its whole length",
     "dele": "a thick smoked sausage link as long as his forearm and no thicker than his wrist"},
    {"id": "milho", "nome": "corn", "tom": "claro",
     "topo": "its tuft of pale silk", "negacao": "",
     "antes": "a whole short ear of sweet corn in its husk, uncut, the silk still coming out of the top, no longer than her palm and as thick as her wrist",
     "depois": "as long as her forearm and still no thicker than her wrist, the rows of kernels running unbroken to the tip",
     "dele": "an ear of sweet corn stripped clean of its husk, as long as his forearm and no thicker than his wrist"},
    {"id": "abobrinha", "nome": "zucchini", "tom": "escuro",
     "topo": "its dried blossom tip", "negacao": "",
     "antes": "a whole baby zucchini, uncut, its dried blossom still on the tip and its stem still on the other end, dark green and matte, no longer than her palm and as thick as her wrist",
     "depois": "as long as her forearm and still no thicker than her wrist, its sides running almost parallel",
     "dele": "a long dark-green zucchini as long as his forearm and no thicker than his wrist"},
    {"id": "batata_doce", "nome": "sweet potato", "tom": "escuro",
     "topo": "its tapered root tip", "negacao": "",
     "antes": "a whole small sweet potato, uncut, both ends tapering to their own points, deep copper skin, no longer than her palm and as thick as her wrist",
     "depois": "as long as her forearm and still no thicker than her wrist, the taper drawn out long",
     "dele": "a long sweet potato as long as his forearm and no thicker than his wrist, the tapered end pointing up"},
    {"id": "calabaza", "nome": "squash", "tom": "claro",
     "topo": "its curved stem neck", "negacao": "",
     "antes": "a whole small crookneck squash, uncut, its curved neck and stem still on it, pale tan and matte, no longer than her palm and as thick as her wrist",
     "depois": "as long as her forearm and still no thicker than her wrist, straight and even the whole way",
     "dele": "the long solid neck of a butternut squash, as long as his forearm and no thicker than his wrist"},
    {"id": "banana", "nome": "banana", "tom": "claro",
     "topo": "its dark stem tip", "negacao": "",
     "antes": "a whole baby banana, uncut, its dark stem still attached and its blossom tip still closed, the skin yellow and lightly freckled, no longer than her palm and as thick as her wrist",
     "depois": "as long as her forearm and still no thicker than her wrist, the curve pulled almost straight",
     "dele": "a ripe banana as long as his forearm and no thicker than his wrist, the skin yellow and lightly spotted"},
    {"id": "mandioca", "nome": "cassava", "tom": "escuro",
     "topo": "its tapered pale tip", "negacao": "",
     "antes": "a whole young cassava root, uncut, tapering naturally at both ends, the brown bark rough and dry, no longer than her palm and as thick as her wrist",
     "depois": "as long as her forearm and still no thicker than her wrist, the bark unbroken to the top",
     "dele": "a length of cassava root as long as his forearm and no thicker than his wrist, the brown bark rough and dry"},
    {"id": "aspargo", "nome": "asparagus", "tom": "escuro",
     "topo": "its tight scaled head", "negacao": "",
     "antes": "a whole thick asparagus spear, uncut, its tight scaled head on top and its pale woody foot below, deep green, no longer than her palm and as thick as her wrist",
     "depois": "as long as her forearm and still no thicker than two of her fingers, straight from base to head",
     "dele": "a jumbo asparagus spear as long as his forearm and no thicker than two of his fingers"},
    {"id": "alho_poro", "nome": "leek", "tom": "claro",
     "topo": "its dark green leaf top", "negacao": "",
     "antes": "a whole baby leek, uncut, its dark green leaves still on top and its hairy white root still on the bottom, the shaft banded pale green, no longer than her palm and as thick as her wrist",
     "depois": "as long as her forearm and still no thicker than her wrist, the white shaft drawn out long",
     "dele": "a trimmed leek as long as his forearm and no thicker than his wrist, the white shaft banded pale green"},
]

# A SUBSTANCIA DESPEJADA — o que cai por cima.
# ⛔⛔ TODAS SAO LIQUIDAS, e isso e' ORDEM DO OPERADOR (2026-08-03), com a fonte
# na mao: "substancia sempre sera liquido e ocorrendo pouring, nunca powders
# como esta atualmente". O reel de referencia despeja OLEO de uma garrafa ambar
# sobre o proxy, e a legenda diz `this is what black seed oil`.
#
# ⚠️ O QUE ISSO CUSTOU, E O CONSERTO DE CADA UM. As tres mecanicas medidas
# dependiam de po' SECO, e nenhuma delas foi abandonada — foram traduzidas:
#   · JATO-MASCARA (R8) — precisava de coluna OPACA. Fio de liquido nao esconde
#     nada, entao o jato passa a ALARGAR NUMA CORTINA que corre pela frente do
#     prop: a oclusao deixa de ser volume de po' e passa a ser lamina de
#     liquido. Mesma funcao, fisica outra.
#   · MONTE na mesa = CRONOMETRO. Po' vira monte, liquido vira POCA — e poca
#     espalha melhor: e' ainda mais legivel que "passou tempo".
#   · ESTRIA vertical = explicacao fisica do morph. No po' era "a mesma
#     quantidade numa area 2,3x maior vira listra". No liquido e' melhor ainda:
#     ele ESCORRE, entao a listra e' o comportamento natural, nao um efeito que
#     o modelo precisa inventar. ⭐ E o brilho ganha: superficie molhada pega a
#     luz e o alongamento fica mais legivel do que em fosco.
# ⛔ Cada `capa`/`estria` diz que o prop fica MOLHADO e BRILHANTE — sem isso o
#   Veo entrega a fruta seca com o liquido caindo ao lado.
#
# ⛔ P12: recipiente por FORMA, inclinado, zero marca. A caixa laranja de
# bicarbonato da fonte fica legivel o hook inteiro e e' o pior caso do garimpo.
# ⚠️ `fala` tem no maximo 2 palavras — o pior caso do teto da cena 1 depende
# disso. `tom` pareia por CONTRASTE com o prop (RS15).
# ⚠️ CONTRATO DE FORMATO, cobrado pelo self-test: `caixa` termina em
# `, tipped mouth-down in her raised hand` (o `_pote` corta ai') e `monte`
# contem ` spreading into` (o `_anel` e o `_monte_verbo` cortam ai').
SUBSTANCIAS = [
    {"id": "oleo_negro", "fala": "black seed oil", "tom": "escuro",
     "caixa": "a plain amber glass bottle of dark oil, tipped mouth-down in her raised hand",
     "jato": "a steady thread of near-black oil",
     "monte": "a ring of dark oil spreading into a wide glossy pool",
     "capa": "its whole surface wet and shining near-black",
     "estria": "dark oil running down in bands from its shoulders over two thirds of its length"},
    {"id": "mel", "fala": "raw honey", "tom": "claro",
     "caixa": "a plain clear glass jar of thick golden honey, tipped mouth-down in her raised hand",
     "jato": "a slow rope of thick golden honey",
     "monte": "a ring of honey spreading into a wide glossy pool",
     "capa": "its whole surface glazed wet and golden",
     "estria": "golden honey sliding down in slow bands from its shoulders over two thirds of its length"},
    {"id": "azeite", "fala": "olive oil", "tom": "claro",
     "caixa": "a plain green glass cruet of pale green oil, tipped mouth-down in her raised hand",
     "jato": "a steady thread of pale green oil",
     "monte": "a ring of pale oil spreading into a wide glossy pool",
     "capa": "its whole surface wet and shining pale green",
     "estria": "pale green oil running down from its shoulders over two thirds of its length"},
    {"id": "melaco", "fala": "molasses", "tom": "escuro",
     "caixa": "a plain heavy glass jug of near-black syrup, tipped mouth-down in her raised hand",
     "jato": "a slow rope of near-black syrup",
     "monte": "a ring of dark syrup spreading into a wide glossy pool",
     "capa": "its whole surface coated wet and near-black",
     "estria": "near-black syrup crawling down from its shoulders over two thirds of its length"},
    {"id": "ricino", "fala": "castor oil", "tom": "claro",
     "caixa": "a plain clear glass bottle of colourless oil, tipped mouth-down in her raised hand",
     "jato": "a steady thread of clear colourless oil",
     "monte": "a ring of clear oil spreading into a wide glossy pool",
     "capa": "its whole surface wet and glassy with clear oil",
     "estria": "clear oil running down in bright lines from its shoulders over two thirds of its length"},
    {"id": "beterraba", "fala": "beet juice", "tom": "escuro",
     "caixa": "a plain clear glass bottle of deep red juice, tipped mouth-down in her raised hand",
     "jato": "a steady thread of deep red juice",
     "monte": "a ring of red juice spreading into a wide glossy pool",
     "capa": "its whole surface wet and stained deep red",
     "estria": "deep red juice running down from its shoulders over two thirds of its length"},
    {"id": "coco", "fala": "coconut oil", "tom": "claro",
     "caixa": "a plain wide-mouthed glass jar of melted coconut oil, tipped mouth-down in her raised hand",
     "jato": "a steady thread of warm melted coconut oil",
     "monte": "a ring of clear oil spreading into a wide glossy pool",
     "capa": "its whole surface wet and gleaming with clear oil",
     "estria": "clear oil running down in bright lines from its shoulders over two thirds of its length"},
    {"id": "cafe_frio", "fala": "cold brew", "tom": "escuro",
     "caixa": "a plain brown glass flask of near-black coffee, tipped mouth-down in her raised hand",
     "jato": "a steady thread of near-black coffee",
     "monte": "a ring of dark coffee spreading into a wide glossy pool",
     "capa": "its whole surface wet and shining dark brown",
     "estria": "dark coffee running down from its shoulders over two thirds of its length"},
    {"id": "vinagre", "fala": "cider vinegar", "tom": "claro",
     "caixa": "a plain clear glass bottle of pale amber vinegar, tipped mouth-down in her raised hand",
     "jato": "a steady thread of pale amber vinegar",
     "monte": "a ring of pale vinegar spreading into a wide glossy pool",
     "capa": "its whole surface wet and shining pale amber",
     "estria": "pale amber vinegar running down from its shoulders over two thirds of its length"},
    {"id": "bordo", "fala": "maple syrup", "tom": "escuro",
     "caixa": "a plain glass decanter of dark brown syrup, tipped mouth-down in her raised hand",
     "jato": "a slow rope of dark brown syrup",
     "monte": "a ring of dark syrup spreading into a wide glossy pool",
     "capa": "its whole surface glazed wet and dark brown",
     "estria": "dark syrup sliding down in slow bands from its shoulders over two thirds of its length"},
    {"id": "aloe", "fala": "aloe juice", "tom": "claro",
     "caixa": "a plain clear glass bottle of thick pale juice, tipped mouth-down in her raised hand",
     "jato": "a thick thread of pale cloudy juice",
     "monte": "a ring of pale juice spreading into a wide glossy pool",
     "capa": "its whole surface wet and slick with pale juice",
     "estria": "pale juice running down from its shoulders over two thirds of its length"},
    {"id": "roma", "fala": "pomegranate", "tom": "escuro",
     "caixa": "a plain clear glass bottle of dark red juice, tipped mouth-down in her raised hand",
     "jato": "a steady thread of dark red juice",
     "monte": "a ring of dark red juice spreading into a wide glossy pool",
     "capa": "its whole surface wet and stained dark red",
     "estria": "dark red juice running down from its shoulders over two thirds of its length"},
    {"id": "glicerina", "fala": "glycerin", "tom": "claro",
     "caixa": "a plain small clear glass flask of clear syrup, tipped mouth-down in her raised hand",
     "jato": "a slow thread of clear heavy syrup",
     "monte": "a ring of clear syrup spreading into a wide glossy pool",
     "capa": "its whole surface wet and glassy with clear syrup",
     "estria": "clear syrup crawling down in bright lines from its shoulders over two thirds of its length"},
    {"id": "cha_preto", "fala": "black tea", "tom": "escuro",
     "caixa": "a plain brown glass bottle of strong dark tea, tipped mouth-down in her raised hand",
     "jato": "a steady thread of strong dark tea",
     "monte": "a ring of dark tea spreading into a wide glossy pool",
     "capa": "its whole surface wet and shining dark",
     "estria": "dark tea running down from its shoulders over two thirds of its length"},
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
    # -----------------------------------------------------------------------
    # + 2026-08-13: DEZ ambientes novos (14 -> 24). Ordem do operador:
    # *"aumente o pool de opcoes substancialmente, tambem dos ambientes"*.
    # ⚠️ Com 14 entradas e um sorteio que evita as 2 ultimas, o cenario voltava
    # a cada tres videos — e seis das catorze ja' diziam `kitchen` no `curto`,
    # que e' o traco do cenario que entra no Audio dos TAKE.
    # ⚠️ CLASSES DIFERENTES DE VERDADE, nao decoracao trocada: despensa, sala
    # de jantar, bar de porao, cozinha de rancho, cozinha de praia, varanda de
    # verao, bancada de acougueiro, galeria de apartamento, cozinha de
    # azulejo, cozinha de avo. ⚠️ Cinco delas sao as MESMAS do
    # `escandalo16_short` (bloco ES19), copiadas com as chaves DESTE pool.
    # ⚠️ CADA UMA TRAZ O AMBIENTE INTEIRO no nivel das vizinhas: superficie +
    # dois objetos de leitura + a BANDEIRA no `set`, `re_ancora` que
    # reestabelece o cenario na cena seguinte (sem ela metade do lote diz
    # so' "in the same kitchen" e a bandeira some do quadro), e `luz` propria.
    # ✅ Bandeira dos EUA em todas, em FORMA diferente cada vez.
    # ⛔ RS14: zero planta, zero carpete — por isso `clay jugs` e nao `clay
    # pots` no rancho, que `pot` puxa `pot plant`.
    # ⛔ ES13/RS: zero texto legivel — o alibi de autoridade e' FORMA.
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
    # -----------------------------------------------------------------------
    # + 2026-08-13: OITO recibos novos (14 -> 22). Ordem do operador:
    # *"aumente o pool de opcoes substancialmente"*.
    # ⚠️ O pool efetivo NAO e' o tamanho da lista: o `_bancada_livre` corta
    # tudo que colide com a fala, com a receita `{r}` E com a substancia `{s}`
    # — sao DOIS eixos de colisao neste motor —, e so' entao evita as
    # recentes. Ampliar aqui e' ampliar o que sobra DEPOIS do filtro, que e' o
    # numero que importa.
    # ⛔ `cabecas` declara o que a imagem deixa NOMEAVEL: se a boca cita o que
    # a imagem tinha de esconder, o recibo deixa de ser recibo.
    # ⛔ Zero marca legivel — FORMA no lugar de rotulo, e a ausencia declarada
    # pela AFIRMATIVA (`plain`), nunca por `with no label` (RS13).
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
     "plantado": "a shallow white bowl of firm vivid purple gelatin cut into cubes, each cube wobbling slightly",
     "curto": "the shallow white bowl of vivid purple gelatin cubes",
     "pousado": "uncovered, its serving spoon lying on the board beside it"},
    {"id": "pote_firme",
     "plantado": "a clear glass jar of gelatin already set firm and vivid purple",
     "curto": "the glass jar of set vivid purple gelatin",
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
     "plantado": "a torn white sachet of gelatin powder lying flat beside a tumbler of cold water",
     "curto": "the torn white sachet of gelatin powder",
     "pousado": "already poured, the wet spoon lying on the board beside it"},
    {"id": "forma_cubos",
     "plantado": "a shallow metal tray of set vivid purple gelatin scored right through into squares",
     "curto": "the metal tray of vivid purple gelatin squares",
     "pousado": "uncovered, the scoring knife lying on the board beside it"},
    {"id": "tigela_madeira",
     "plantado": "a turned wooden bowl of firm vivid purple gelatin cubes piled above the rim",
     "curto": "the wooden bowl of vivid purple gelatin cubes",
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
# ⛔⛔ REESCRITO EM 2026-08-10 — CONTRATO DE COPY 16s, trava CT2.
# Medido antes (200 sorteios, `medir_copy16.py`): 30% dos take 1 NAO enunciavam
# falha nenhuma. O buraco tinha nome e endereco — tres dos oito hooks do degrau
# 2 (`hadn't been hard in two years`, `nothing worked for him`, `was done in
# bed`) e TODOS os quatro dos degraus 4 e 5, que abriam pela crendice
# (`They say {s} does this.`) e nunca diziam o que o corpo dele faz de errado.
# ⭐ A REGRA NOVA E' UMA SO': A PRIMEIRA SENTENCA DE TODO HOOK E' A FALHA DELE,
# com dano concreto e de preferencia um numero. A escada de moderacao (o
# `degrau`) passa a viver na SEGUNDA sentenca, que e' onde ela sempre pertenceu:
# o degrau qualifica o CLAIM SOBRE A SUBSTANCIA, e a falha do marido nao e'
# claim sobre substancia nenhuma.
#     2 assertiva sem prazo, sem {s} — a ponte em 2a pessoa com o orgao
#     3 condicional (`If {s} works, ...`)
#     4 atribuicao (`They say {s} ...`) — o achado de moderacao deste angulo
#     5 plana (o nome da substancia, nu)
# ⭐ O DEGRAU 3 GANHOU POOL. `DEGRAUS` declarava (2,3,4,5) desde o primeiro dia e
# o pool nao tinha UMA entrada de degrau 3: `--degrau 3` caia no `or HOOKS` e
# rodava os doze, ou seja, a flag mentia. Quatro entradas novas fecham o buraco.
# ⭐ 12 -> 18 entradas: nenhuma familia foi perdida e o `MIN_COPY["HOOKS"]=16`
# do autoteste (que reprovava com 12) volta a ser cumprido.
# ⚠️ `He'd lose it ten minutes in` e' A MELHOR LINHA MEDIDA DO PARQUE (cinco
# palavras, um numero, um dano) e aparece em quatro degraus de proposito — e' o
# padrao que o contrato manda copiar, nao um eco.
# ⛔ Nenhuma com prazo (RS10). ⚠️ Numeros por extenso: o Veo soletra algarismo.
# ⛔ CT7 — `hard` so' aparece em sentenca SEM o orgao (`couldn't stay hard past
# sixty` e' o corpo dele, nao o orgao): verbo de ereccao colado no orgao e' ~95%
# de recusa medida no COLO 16.
HOOKS = [

    # --- degrau 2: falha + ponte em 2a pessoa. ⛔ Estes carregam o `your {o}`
    # que a RS25 cobra da cena 1; nos degraus 3/4/5 quem carrega e' o bullet.
    {"degrau": 2, "txt": "My husband couldn't stay hard past sixty. If that's your {o}, watch this."},
    {"degrau": 2, "txt": "Sixty-one, and my man quit on me in bed. Sound like your {o}?"},
    {"degrau": 2, "txt": "My husband went soft every time. If your {o} does that, stay here."},
    {"degrau": 2, "txt": "He stopped even trying at fifty-eight. If that's your {o}, watch."},
    # ⚠️ era `My husband hadn't been hard in two years.` — nenhum verbo de falha
    # que a CT2 reconheca, e `hadn't been hard` e' estado, nao dano.
    {"degrau": 2, "txt": "My husband quit trying after two years. If that's your {o}, watch this."},
    {"degrau": 2, "txt": "He'd lose it ten minutes in. If your {o} quits like that, watch."},
    # ⚠️ era `Sixty-three and nothing worked for him.` — "nada funcionou" nao diz
    # o que parou de funcionar.
    {"degrau": 2, "txt": "Sixty-three, and everything quit on him. If your {o} did too, watch."},
    # ⚠️ era `My man was done in bed at sixty.` — `was done` e' resumo, nao dano.
    {"degrau": 2, "txt": "My man stopped finishing at sixty. If that's your {o}, stay with me."},

    # --- degrau 3: falha + a substancia em CONDICIONAL (pool que nao existia)
    {"degrau": 3, "txt": "My husband went soft every time. If {s} works, watch."},
    {"degrau": 3, "txt": "He'd lose it ten minutes in. If {s} helps, stay."},
    {"degrau": 3, "txt": "He stopped trying at fifty-eight. If {s} is real, watch."},
    {"degrau": 3, "txt": "My man quit at sixty. If {s} does this, stay."},

    # --- degrau 4: falha + ATRIBUICAO (o achado de moderacao do angulo)
    {"degrau": 4, "txt": "My husband went soft at sixty. They say {s} fixes that."},
    {"degrau": 4, "txt": "He'd lose it ten minutes in. They all swear by {s}."},
    {"degrau": 4, "txt": "He quit at fifty-eight. The neighbors swear by {s}."},

    # --- degrau 5: falha + o nome da substancia, plano
    {"degrau": 5, "txt": "My husband went soft every time. {s}. Watch."},
    {"degrau": 5, "txt": "He'd lose it ten minutes in. {s} on it. Watch."},
    {"degrau": 5, "txt": "He quit on me at sixty. {s}. Watch."},
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
# ⛔⛔ REESCRITO EM 2026-08-10 — o `this` sem dono, e ele custava o beat inteiro.
# Queixa medida na revisao adversarial: *"So I started making him this"* — o
# UNICO referente na tela e' liquido sendo despejado EM CIMA do prop, entao
# `this` le' como topico (a substancia absurda) quando o que se quer dizer e'
# BEBIDA. Nove das catorze entradas terminavam num demonstrativo nu (`this`,
# `it`, `the thing`), e demonstrativo sem referente e' descarte (§teste WTF).
# ⭐ A REGRA NOVA: toda entrada NOMEIA o que ela achou — `recipe`, `drink` ou
# `glass`. Sao as tres palavras que o CTA vai cobrar de volta, entao nomea-las
# aqui e' plantar a moeda, nao gastar palavra.
# ⛔ ZERO nome de ingrediente (CT5): a receita e' a UNICA moeda que o comentario
# compra, e uma vez dita na tela publica esta' gasta para os outros 49 videos.
# ⚠️ ORCAMENTO: 6-7 palavras, TODAS. Entrada de 9 palavras num teto de 25 nao
# concorre com uma de 6 — ela empurra o hook e o bullet para fora e o pool vira
# enfeite. Tamanho parecido e' o que faz o [ALCANCE] fechar em 14 de 14.
CONFIRMACOES = [
    "Then his brother handed me a recipe.",
    "So I started making him this drink.",
    "My salon lady had the recipe.",
    "Then I found the recipe at home.",
    "A neighbor gave me the recipe.",
    "So I made him one glass.",
    "Then my aunt handed over her recipe.",
    "A nurse gave me the recipe.",
    "So I made the drink, not pills.",
    "Then I found the recipe nobody sells.",
    # ⚠️ era `His shop buddy swore by the drink.` — `by the` casa o RS10_PRAZO
    # (`by the` esta' na familia `by next`/`by morning`), e com o hook do degrau
    # 3/4/5 quem traz o `your <nucleo>` e' o BULLET, entao o filtro de prazo do
    # sorteio (que so' olhava o hook) nao via a soma. Medido: 18 ERRO em 200
    # sorteios no degrau 3. A entrada estava tambem MORTA no degrau 2, onde o
    # filtro a barrava sempre.
    "His shop buddy knew the recipe.",
    "I dropped his pills for the drink.",
    "Then his army buddy shared the recipe.",
    # ⛔⛔ DERRUBADA NA CONFERENCIA DE 2026-08-10, mesma leitura em voz alta.
    # Era `So the drink went into his glass.` e o defeito e' PRIMEIRA MENCAO
    # DEFINIDA SEM AGENTE. Sorteio real, degrau 5:
    #     "He'd lose it ten minutes in. Olive oil on it. Watch.
    #      So the drink went into his glass."
    # Ate' aqui o video nao falou em bebida nenhuma; o unico liquido dito e' a
    # substancia absurda. `THE drink` entao se resolve no que acabou de ser
    # nomeado, e o take passa a dizer que ele bebeu o oleo — o mesmo erro de
    # `That is what he drank.` nos BULLETS, e nos degraus 3/4/5 os dois podiam
    # cair no MESMO take 1. E a frase e' agentless: as outras treze entradas
    # tem sempre alguem que da', acha, faz ou serve; esta e' direcao de cena.
    # ⚠️ Substituta: 6 palavras (teto 7), agente na primeira palavra, nomeia
    # `drink` como as outras, zero prazo, zero ingrediente.
    "So I poured him the drink.",
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
# ⚠️ 2026-08-10: as treze entradas ficam CARACTERE POR CARACTERE como estavam,
# menos a primeira — ela tinha 8 palavras contra 5-7 das outras doze, e num teto
# de 25 a mais longa do pool e' a que rouba a folga do hook. `do not` -> `don't`
# resolve sem tocar no sentido.
DESMENTIDOS = [
    "You don't actually believe that works, right?",
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
# ⛔⛔ REESCRITO EM 2026-08-10, e sao TRES defeitos medidos de uma vez:
#
# [1] O PROP DE PLASTICO CHAMADO DE `him`. `Look at that. That's him now.` /
#     `Keep your eyes on it. That's him.` — o unico corpo em quadro na cena 1 e'
#     uma banana num punho. Dizer que ELE e' o marido nao e' metafora: e' a
#     frase mais literal do take apontando para a coisa errada. Sete das doze
#     entradas faziam isso.
# [2] A DEIXIS SEM DONO. `What it does to that, it did to him.` sao TRES
#     ponteiros numa sentenca de nove palavras, e nenhum tem antecedente falado.
# [3] ⛔⛔ A RS25 SO' PASSAVA POR SORTE DO DEFAULT. A regra exige `your <nucleo>`
#     na cena 1; as tres entradas com `{o}` diziam `his {o}` / `the {o}`, que
#     NAO casam. Com o degrau 2 (default) o hook trazia o `your {o}` e a lente
#     ficava verde; em `--degrau 4` ou `--degrau 5`, onde o hook nao nomeia o
#     orgao, o bullet era a UNICA chance e ele nao a cumpria. Flag que quebra
#     regra e' flag que ninguem pode rodar.
#
# ⭐ AS DUAS REGRAS NOVAS DO POOL:
#   · quem carrega `{o}` carrega `your {o}` — 2a pessoa, RS25 e CT4 no mesmo
#     token;
#   · a transferencia e' dita pelo NOME (`my husband`), nunca por `him` colado
#     no prop. O que a tela mostra e a copy compara — nao identifica.
# ⛔ ZERO marcador de prazo (RS10 mata `your {o}` + prazo no mesmo take de 8s).
# ⚠️ ORCAMENTO: 5-7 palavras, todas.
#
# ⛔ O CAMPO `cred` VOLTOU A TER FUNCAO. As doze antigas eram todas `ambas`, e
# no modo `desmente` o beat anterior diz *"Of course it doesn't. Nothing does
# that."* e o bullet seguinte respondia *"That's what it did to him"* — a cena
# fechava desmentindo a si mesma. Agora a leitura do crescimento como PROVA e'
# `confirma`, e as seis neutras (que falam do que faltava, nao do que a tela
# entregou) sao `ambas`. ⚠️ Tres com `{o}` e tres sem em CADA modo: e' o piso
# que o autoteste cobra para o hook que nomeia e para o que nao nomeia.
# ⚠️⚠️ CINCO PALAVRAS, TODAS — e o numero nao e' estetico, e' o que faz o pool
# existir. O take 1 e' hook (ate' 13) + descoberta (ate' 7) + bullet, e o teto
# e' 25: com bullets de 5 a 7 palavras, o solver descarta as longas sempre que
# o hook e' comprido, e como ele sorteia PARES a entrada curta aparece em muito
# mais pares. MEDIDO em 1.200 sorteios com o pool de tamanho livre: `That
# happened to my husband.` (5) saia 449 vezes e `What fixed my husband was a
# glass.` (7) saia 28 — 16 para 1 num pool que o `--stats` conta como sete.
# ⭐ Com 13 + 7 + 5 = 25 exatas no pior caso, TODA combinacao cabe: nenhuma
# entrada e' descartada por orcamento e a distribuicao fica plana por
# construcao. E' a mesma solucao do take 2 (8/5/3/9), aplicada ao take 1.
BULLETS = [
    # --- neutras: rodam nos dois modos -------------------------------------
    {"cred": "ambas", "txt": "Your {o} needs a recipe."},
    {"cred": "ambas", "txt": "Your {o} is missing something."},
    {"cred": "ambas", "txt": "Your {o} needs one thing."},
    {"cred": "ambas", "txt": "A glass fixed my husband."},
    {"cred": "ambas", "txt": "One recipe changed my husband."},
    {"cred": "ambas", "txt": "My husband needed something else."},
    # --- a leitura do crescimento como PROVA: so' no modo confirma ---------
    {"cred": "confirma", "txt": "Your {o} can do that."},
    # ⚠️ era `Your {o} goes that way.` — lido em serie depois do beat da
    # descoberta, `goes that way` nao diz para onde. `Same thing for your {o}.`
    # aponta para o que a tela acabou de fazer, no mesmo tamanho.
    {"cred": "confirma", "txt": "Same thing for your {o}."},
    {"cred": "confirma", "txt": "That happens to your {o}."},
    {"cred": "confirma", "txt": "Your {o} does exactly that."},
    {"cred": "confirma", "txt": "That happened to my husband."},
    # ⛔⛔ DUAS ENTRADAS DERRUBADAS NA CONFERENCIA DE 2026-08-10 (leitura em voz
    # alta, ouvido de americano de 50-70 anos, uma passada so'). Ambas nasceram
    # NESTA reforma — nao sao copy validada em campo, sao linha do assistente:
    #
    # [1] `My husband went that way.` — dois defeitos somados. (a) `went that
    #     way` e' idiomatico nos EUA para "virou gay" / "definhou", e e' a
    #     leitura que chega primeiro num homem de 60 anos ouvindo uma vez;
    #     (b) o `that` nao tem antecedente FALADO — e este pool ja' tinha
    #     matado `Your {o} goes that way.` por essa razao exata ("goes that way
    #     nao diz para onde"). A mesma formula sobreviveu so' porque o sujeito
    #     mudou. Trocada por uma que ESPELHA a falha nomeada no hook, que e' o
    #     que fecha o loop do take 1: se o hook diz `went soft every time`, o
    #     bullet diz que o marido parou de fazer isso.
    # [2] `That is what he drank.` — o `That` aponta para a UNICA coisa liquida
    #     em quadro, que e' a substancia absurda sendo despejada no prop (olive
    #     oil, black seed oil, molasses). Ouvido uma vez, o video diz que o
    #     marido BEBEU o oleo. Nao e' vago: e' errado. E o registro sem
    #     contracao (`That is`) nao e' fala de ninguem — seria `That's`.
    # ⚠️ Ambas as substitutas mantem as CINCO palavras exatas, o `cred`
    # confirma, zero `{o}` (o contrato dos pools cobra 3 com e 3 sem por modo) e
    # zero marcador de prazo. Zero deixis: o sujeito e' NOMEADO nas duas.
    {"cred": "confirma", "txt": "My husband stopped going soft."},
    {"cred": "confirma", "txt": "My husband holds up now."},
    {"cred": "confirma", "txt": "My husband changed like that."},
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
    # ⛔⛔ REESCRITO EM 2026-08-03 — ordem do operador: "reescreva toda a
    # copy do agente para satisfazer a todas as pontuacoes criticas".
    # A hierarquia agora e' CONTEXTO -> DESCOBERTA -> RECEITA -> OPEN LOOP ->
    # GELATINA -> PROVA -> CTA. O espectador sabe do que se trata na
    # PRIMEIRA frase; esconde-se o COMO, nunca o SOBRE O QUE.
    {"cred": "ambas", "txt": "It starts with {r} and warm water, stirred down. That part everybody knows. The part they leave out is the gelatin trick, and that's the half his {o} needed."},
    {"cred": "ambas", "txt": "The base is easy: {r}, warm water, one stir. Nobody hides that. What they hide is the gelatin trick, and without it his {o} stayed down."},
    {"cred": "ambas", "txt": "Half of it is {r} and warm water. That half does nothing alone. The gelatin trick is the other half, and it's the one that got his {o} hard."},
    {"cred": "ambas", "txt": "You start with {r} and warm water. Everyone stops there. I didn't, because the gelatin trick is what got his {o} hard."},
    {"cred": "ambas", "txt": "It's {r}, warm water, stirred until it turns. Simple. But there's one more step, the gelatin trick, and that step is what woke his {o} up."},
    {"cred": "ambas", "txt": "{r} and warm water is where it starts. That's the part they'll tell you. The gelatin trick is the part they won't, and his {o} needed it."},
    {"cred": "ambas", "txt": "First {r}, then warm water, stirred clear. That's two of three. The third is the gelatin trick, and it got his {o} standing again."},
    {"cred": "ambas", "txt": "Anyone can do the {r} and warm water. Almost nobody does the gelatin trick after it, and that's the step that got his {o} hard again."},
    {"cred": "ambas", "txt": "{r} in warm water, one turn of the spoon. That much is free. The gelatin trick is what I paid to learn, and his {o} came back on it."},
    {"cred": "ambas", "txt": "The drink is {r} and warm water. Alone it did nothing. Then I added the gelatin trick and his {o} came back hard."},
    {"cred": "ambas", "txt": "It's {r} and warm water to start. Every recipe online stops right there. Mine doesn't — the gelatin trick got his {o} working."},
    {"cred": "ambas", "txt": "Two things in the glass: {r} and warm water. A third thing goes in after, the gelatin trick, and that's the one that got his {o} back."},
    {"cred": "ambas", "txt": "{r}, warm water, stir. That's the part I can say out loud. The gelatin trick is the rest of it, and it's what got him hard again."},
    {"cred": "ambas", "txt": "Start with {r} and warm water. Good on its own, useless for this. The gelatin trick is what made it work on his {o}."},
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
    # ⛔⛔ REESCRITO EM 2026-08-03 — ordem do operador: "reescreva toda a
    # copy do agente para satisfazer a todas as pontuacoes criticas".
    # A hierarquia agora e' CONTEXTO -> DESCOBERTA -> RECEITA -> OPEN LOOP ->
    # GELATINA -> PROVA -> CTA. O espectador sabe do que se trata na
    # PRIMEIRA frase; esconde-se o COMO, nunca o SOBRE O QUE.
    {"voz": "terceiro", "txt": "His {o} hasn't gone soft since."},
    {"voz": "intima", "txt": "That's him. His {o} never quits now."},
    {"voz": "intima", "txt": "Two years of a dead {o}, and now this."},
    {"voz": "terceiro", "txt": "His {o} is harder now than at forty."},
    {"voz": "terceiro", "txt": "Same man whose {o} had given up."},
    {"voz": "intima", "txt": "His {o} stands like that now."},
    {"voz": "terceiro", "txt": "Same man, same age. His {o} doesn't quit."},
    {"voz": "terceiro", "txt": "His {o} hasn't needed a pill since."},
    {"voz": "intima", "txt": "That's what his {o} does now."},
    {"voz": "intima", "txt": "His {o} is what wakes me up now."},
    {"voz": "terceiro", "txt": "His {o} went from dead to this."},
    {"voz": "intima", "txt": "His {o} hasn't gone soft on me since."},
    {"voz": "terceiro", "txt": "His {o} had stopped answering. Look at it."},
    {"voz": "intima", "txt": "His {o} is harder than the day we met."},
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
    # ⛔⛔ REESCRITO EM 2026-08-03 — ordem do operador: "reescreva toda a
    # copy do agente para satisfazer a todas as pontuacoes criticas".
    # A hierarquia agora e' CONTEXTO -> DESCOBERTA -> RECEITA -> OPEN LOOP ->
    # GELATINA -> PROVA -> CTA. O espectador sabe do que se trata na
    # PRIMEIRA frase; esconde-se o COMO, nunca o SOBRE O QUE.
    "Comment gelatin, and I'll send the recipe.",
    "Comment gelatin, and the full recipe goes to you.",
    "Comment gelatin, and I'll send the missing recipe step.",
    "Comment gelatin, and I'll send you all three steps.",
    # ⚠️ era `and you get what I used` — encurtei e a ISCA foi junto: o linter
    # exige que o CTA diga O QUE CHEGA, e "o que eu usei" nao nomeia entrega.
    "Comment gelatin, and you get the recipe I used.",
    "Comment gelatin, and I'll write out the glass.",
    "Comment gelatin, and I'll send the recipe step everyone skips.",
    "Comment gelatin, and I'll send you the whole thing.",
    "Comment gelatin, and the recipe is yours.",
    "Comment gelatin, and I'll send what to buy.",
    "Comment gelatin, and I'll send you the exact recipe.",
    "Comment gelatin, and I'll send the third ingredient.",
    "Comment gelatin, and I'll send it my way.",
    "Comment gelatin, and I'll send his recipe.",
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
# ⛔⛔ REESCRITO EM 2026-08-10 — O GATE MUDOU DE LUGAR E DE TAMANHO (CT1 + CT6).
#
# [posicao] Medido: 100% dos take 2 terminavam DEPOIS do pedido, e a ultima
#   coisa no ouvido era `The algorithm hides me from non-followers.` /
#   `Three hundred comments tonight. Followers first.` — expectativa negativa
#   sobre a entrega ou condicional na recompensa, colada no unico beat que gera
#   receita. A posicao final e' a que fica; ela tem de ser o pedido.
#   ⭐ O follow NAO foi cortado — ele vai ANTES do CTA. O pool continua vivo,
#   continua sorteado, continua no video.
#
# [tamanho] O orcamento fechado do take 2 da' TRES palavras ao follow
#   (8 mecanismo + 5 prova + 3 follow + 9 CTA = 25). As entradas antigas tinham
#   4 a 7 e nao havia como caber quatro beats. Entao o motivo do gate deixa de
#   ser uma oracao e vira a propria forma verbal.
#
# ⛔ `Three hundred comments tonight.` MORREU e nao volta: e' claim que o proprio
# video derruba (o espectador ve o contador de comentarios na tela) e ainda soma
# `tonight`, marcador de prazo.
# ⚠️ A REGRA DE POOL DO VOCATIVO CONTINUA VALENDO e continua cobrada pelo
# autoteste: no maximo DUAS com `brother`, e a maioria sem vocativo nenhum —
# medido pelo operador no TROCA, `brother` caia em 31-73% dos videos.
# ⚠️ TRES palavras, TODAS. O teto de 25 nao tem folga: uma entrada de quatro
# estoura o take inteiro, e take estourado corta a keyword, que e' a ultima
# coisa dita.
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
    "Tap follow first.",
    "Follow, then comment.",
    "I answer followers.",
    "Followers get answered.",
    "Follow me, brother.",
    "Follow before commenting.",
    "Non-followers get skipped.",
    "Follow me, guys.",
    "Hit follow first.",
    "Followers hear back.",
    "Follow me now.",
    "Follow me, man.",
    "I message followers.",
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
# ⛔ 2026-08-03: os de po' (carton, sack, box, bag, canister...) ficaram so' para
# o caso de alguem reintroduzir um solido — a SUBSTANCIA deste agente e' LIQUIDA
# por ordem do operador, e liquido sai de garrafa, nao de saco.
_RECIPIENTES = ("bottle", "flask", "jug", "cruet", "decanter", "jar", "tin",
                "carton", "cylinder", "canister", "sack", "box", "bag")


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
    # ⚠️ `tipped` entrou em 2026-08-03 com as substancias liquidas: garrafa se
    # INCLINA, nao se vira de boca para baixo. As formas de po' ficam no regex
    # para nao quebrar quem copiar uma travada antiga.
    return re.split(r",? and (?:turned|tipped) mouth-down"
                    r"|, (?:turned|tipped) mouth-down", caixa)[0].rstrip(", ")


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
# ⛔⛔ SEGUNDO BURACO TAPADO, 2026-08-03. O primeiro era `seconds`; este e' o
# PRAZO SOLTO. Num conserto de copy do PEE a travada virou
# `wakes your {o} back up. Nineteen days.` — prazo entregue como FRAGMENTO, sem
# preposicao, e o regex so' via `in nineteen days`. E' a linha do NECROSE
# passando por baixo da regra que existe para barra-la.
# ⚠️ E o oposto tambem foi medido: `nineteen days later he walked in` e `one
# night she reaches over` sao NARRATIVA sobre o terceiro, nao promessa ao
# espectador. Cobrar isso reprovava 200/200 do FLAGRANTE, que conta historia dos
# outros por construcao. A negativa e' tao importante quanto a positiva.
RS10_PRAZO = re.compile(
    r"\b(overnight|by next|by the|before bed|every (morning|night)|tonight|"
    r"by morning|by tomorrow)\b"
    r"|\b(in|inside|within|after)\s+[\w-]+\s+"
    r"(seconds?|minutes?|hours?|days?|weeks?|months?)\b"
    # o prazo SOLTO, como sentenca inteira
    r"|(?:^|[.!?]\s*)(one|two|three|four|five|six|seven|eight|nine|ten|"
    r"eleven|twelve|fifteen|nineteen|twenty|thirty|\d+)\s+"
    r"(seconds?|minutes?|hours?|days?|weeks?|months?|nights?)\s*[.!?]", re.I)

# ⛔ NARRATIVA NAO E' PROMESSA — descontado antes de aplicar o RS10_PRAZO.
RS10_NARRATIVA = re.compile(
    r"\b[\w-]+\s+(seconds?|minutes?|hours?|days?|weeks?|months?|nights?)\s+"
    r"later\b|\bnights? a week\b", re.I)
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

# ⛔ CT2 no POOL, nao so' no video montado. O `lint_copy16` cobra a falha na
# fala inteira; aqui se cobra de CADA HOOK, porque a falha e' o trabalho do
# hook e nao um efeito colateral do beat seguinte. ⚠️ O vocabulario e' um
# SUBCONJUNTO do da lente compartilhada — quem passa aqui passa la'.
CT2_FALHA = re.compile(r"\b(quit|quits|quitting|soft|stopped|stops|couldn't|"
                       r"lose it|lost it|loses it|failed|fails|gave out)\b",
                       re.I)


# ---------------------------------------------------------------------------
# SORTEIO
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# ⭐⭐ A FALA DO TAKE 2 — QUATRO BEATS, ORCAMENTO FECHADO (reforma 2026-08-10)
# ---------------------------------------------------------------------------
#     {MECANISMO 8} {PROVA 5} {FOLLOW 3} {CTA 9}  =  25, o teto fisico
#
# ⛔⛔ A ESTRUTURA VEM DO CONTRATO DE COPY 16s, nao de gosto:
#     TAKE 2   mecanismo COM RAZAO -> prova curta -> follow -> CTA   <- FIM
# Doutrina e a conta inteira: funil-organico/CONTRATO-COPY-16S.md.
#
# ⛔ O QUE MORREU AQUI, e por que — as METADES16 (2026-08-08 - 2026-08-10):
#   `My husband's {o} ignored {r}.` era a pior familia de sentenca do lote de
#   sete motores, e por tres motivos somados numa frase de seis palavras:
#     1. ORGAO PERSONIFICADO — um penis nao "ignora" nada. `ignored cayenne`
#        e' o mesmo vicio de `his soldier ignored parsley`, que a revisao de
#        ouvido nativo derrubou.
#     2. INGREDIENTE ENTREGUE DE GRACA (CT5) — medido em 78% dos sorteios. O
#        `{r}` punha `cayenne`, `pomegranate`, `garlic` na fala. A receita e' a
#        UNICA moeda que o comentario compra: dita uma vez na tela publica, ela
#        esta' gasta para os outros 49 videos da mesma pagina.
#     3. UM SUBSTANTIVO COMESTIVEL DE UMA PALAVRA A UM SEGUNDO DA KEYWORD, numa
#        automacao de DM que casa PALAVRA EXATA. `Comment gelatin` competindo
#        com `cayenne` no mesmo folego e' pedir para a pessoa comentar errado.
#   ⭐ O EIXO `receita` NAO FOI PERDIDO: ele continua sorteado, continua no
#   ledger, no painel e no ledger de entropia — ele so' deixou de sair pela
#   BOCA. Ele mora onde sempre pesou mais, que e' o IMAGE/TAKE 02 (a receita
#   sendo executada em quadro) e a bancada-recibo. Ver a divergencia registrada
#   em `_trocar_receita`.
#
# ⭐⭐ A CONTA, E POR QUE ELA E' FECHADA E NAO FOLGADA. O teto de 25 vem de
# RENDER (32 cortou, 28 cortou) e o take 2 tem de caber QUATRO beats. Com pools
# de tamanho livre, quem tem 6 palavras rouba a folga de quem tem 10 e o pool
# vira "quatro entradas com oito enfeites" — medido em outro motor, quatro
# entradas levavam 67% do lote. Aqui cada pool tem TAMANHO UNICO:
#     mecanismo 8 · prova 5 · follow 3 · CTA 9 = 25 exatas, sempre.
# Consequencia direta e medida: [ALCANCE] 14/14 em CADA um dos quatro pools, e
# nenhum sorteio precisa do fallback. O contrato de tamanho e' cobrado pelo
# `_contrato_dos_pools` — pool sem lente e' pool que envelhece mentindo.

# ⭐ O MECANISMO COM RAZAO (CT3). ⛔ Rotulo nu e' proibido: `The gelatin trick
# is the half that works.` nao diz o que a gelatina FAZ, e nome de mecanismo sem
# razao ao lado nao vira crenca — vira ruido de marca. Toda entrada carrega
# VERBO DE EFEITO + ALVO (o sangue, a pressao, o fluxo, o corpo) na MESMA
# sentenca, que e' o que a lente cobra.
# ⛔ O ALVO E' O SANGUE E NUNCA O ORGAO, e isso e' CT7: verbo de efeito colado no
# orgao ("the gelatin trick gets your {o} hard") e' ~95% de recusa do gerador,
# licao paga em campo no COLO 16. Sobre o corpo passa; sobre o orgao nao.
# ⛔ ZERO ingrediente (CT5) e ZERO `blood flow ... choked/blocked/cut off`, que
# e' a forma que o `medir_contexto_copy` cobra como causa orfa.
# ⚠️ As catorze abrem com `The gelatin trick` de proposito: o nome do mecanismo
# e' o centro de gravidade do funil e repeti-lo na mesma posicao e' o que faz o
# espectador sair do video sabendo pronuncia-lo. A entropia mora na razao, que
# e' a metade que muda. ⚠️ `The` e' o unico qualificador que a allowlist do
# `_adjetivo_do_mecanismo` aceita junto de artigo/numeral.
#
# ⛔⛔ E TODAS NOMEIAM O DONO — correcao de 2026-08-10, MEDIDA. A primeira versao
# era impessoal (`The gelatin trick pushes blood where it belongs.`), que e' a
# forma canonica do contrato, e o `medir_abertura.py` saltou de 21,2% para
# 71,2% de aberturas orfas: a PRIMEIRA sentenca do take 2 passou a nao ter
# referente nenhum, e ela e' a que chega sozinha depois do corte. Os +50 pontos
# eram exatamente as 120 aberturas de cena 2 do lote.
# ⭐ Nomear o dono custa ZERO palavra (continua 8) e ainda cumpre a ordem do
# operador de 2026-08-08 para este slot: *"nao use pronome, seja taxativo e
# claro"*, com o dono NOMEADO. E' o que licencia o `His {o}` da PROVA seguinte:
# o antecedente passa a estar na sentenca anterior DO MESMO TAKE.
MECANISMOS16 = [
    "The gelatin trick holds my husband's blood in.",
    "The gelatin trick brings my husband's blood back.",
    "The gelatin trick opens my husband's blood flow.",
    "The gelatin trick feeds my husband's body again.",
    "The gelatin trick keeps my husband's pressure up.",
    "The gelatin trick restores my husband's blood flow.",
    "The gelatin trick moves my husband's blood again.",
    "The gelatin trick worked on my husband's blood.",
    "The gelatin trick clears my husband's blocked flow.",
    "The gelatin trick pushes blood through my husband.",
    "The gelatin trick brings my husband's pressure back.",
    "The gelatin trick unblocks my husband's blood flow.",
    "The gelatin trick changed my husband's whole body.",
    "The gelatin trick started my husband's blood moving.",
]

# ⭐ A PROVA CURTA — e e' ela que carrega o apelido do orgao no take 2 (CT4).
# ⛔⛔ CT4 REVERTE A REGRA ANTIGA deste motor ("tres substantivos DISTINTOS de
# uma vez: um por cena"). Em 24s e cinco cenas o bordao era o risco; em 16s e
# dois takes o risco e' o oposto — o CORTE ZERA A MEMORIA DE TRABALHO, e trocar
# `soldier` por `Johnson` no segundo 9 obriga o espectador a remapear justamente
# quando ele ja' esta' com um pe' fora. Medido: o apelido mudava no corte em
# 100% dos videos. A variacao continua existindo ENTRE videos, que e' onde ela
# nunca custou nada. Ver `sortear` e a lente aposentada no `lint`.
# ⛔ O DONO NUNCA FICA IMPLICITO. ⚠️ Nove entradas abrem com `His {o}` e isso NAO
# e' pronome nu: o beat ANTERIOR do mesmo take (o mecanismo) diz `my husband` em
# todas as catorze entradas, entao o antecedente esta' a uma sentenca de
# distancia e dentro do mesmo take — anafora, nao deixis. As outras cinco dizem
# `My man's {o}` para o ouvido nao levar `my husband's ... my husband's` colado.
# ⛔ Se algum dia uma entrada de MECANISMOS16 deixar de nomear o dono, estas
# nove viram pronome orfao — por isso o contrato dos pools cobra o dono la'.
# ⛔ CT7 — ZERO verbo de ereccao na sentenca do orgao (`hard`, `stands up`,
# `works again`, `comes back`, `swells`). A prova e' a NEGACAO DA FALHA
# (`never quits`, `stopped failing`), que diz a mesma coisa e passa no gerador.
# ⚠️ CINCO palavras, todas.
# ⚠️ CINCO palavras CONTADAS COM O `{o}` JA' SUBSTITUIDO — e' a conta que a
# primeira versao errou. `My husband's {o} holds out now.` parece cinco e sao
# SEIS (`My`+`husband's`+`Johnson`+`holds`+`out`+`now`); com 6 a soma da' 26
# contra teto 25 e o solver descarta a entrada em 100% dos sorteios. Medido no
# [ALCANCE]: cinco entradas nasceram mortas e o autoteste as contava como vivas.
# ⛔ Por isso `_contrato_dos_pools` passou a cobrar o tamanho de cada entrada
# com o pior `{o}` do NUCLEO — contrato que so' vive no comentario e' intencao.
PROVAS16 = [
    "His {o} has not quit.",
    "His {o} never quits now.",
    "His {o} never fails now.",
    "His {o} does not quit.",
    "His {o} stopped failing me.",
    "His {o} still holds now.",
    "His {o} outlasts me now.",
    "His {o} answers every time.",
    "His {o} lasts all night.",
    "My man's {o} never quits.",
    "My man's {o} never fails.",
    "My man's {o} doesn't quit.",
    "My man's {o} stopped failing.",
    "My man's {o} still holds.",
]

# ⭐ O CTA COM COBERTURA SOCIAL (CT6) — e a descoberta que faz a conta fechar:
# a cobertura NAO cabe como beat proprio em 25 palavras, entao ela mora DENTRO
# da sentenca do pedido.
#     antes:  Comment gelatin, and I'll send the recipe.            (9 palavras)
#     depois: Comment gelatin, and the recipe goes to your messages. (9 palavras)
# Mesmo custo, e paga de graca (a) o endereco da entrega, (b) a privacidade e
# (c) o fato de que nao e' na tela publica. O KPI e' uma confissao publica num
# feed onde o comentario leva nome e foto: sem a clausula, quanto melhor o
# diagnostico em 2a pessoa, MAIS CARO fica comentar.
# ⛔ TODAS carregam o literal `Comment gelatin,` (minusculo, com virgula) e todas
# nomeiam `recipe` — sem isca o espectador e' convidado a pagar sem saber o que
# compra. ⛔ `book`, `yes` e `link` proibidos.
# ⛔ ESTA E' A ULTIMA SENTENCA DO VIDEO, SEMPRE (CT1). Nada vem depois dela.
# ⚠️ NOVE palavras, todas.
CTAS16 = [
    "Comment gelatin, and the recipe goes to your messages.",
    "Comment gelatin, and the recipe lands in your inbox.",
    "Comment gelatin, and I'll send the recipe by message.",
    "Comment gelatin, and the whole recipe hits your inbox.",
    "Comment gelatin, and the recipe comes to your messages.",
    "Comment gelatin, and the full recipe goes by message.",
    "Comment gelatin, and the recipe arrives in your inbox.",
    "Comment gelatin, and the recipe waits in your messages.",
    "Comment gelatin, and I'll drop the recipe in private.",
    "Comment gelatin, and I'll put the recipe in private.",
    "Comment gelatin, and the recipe goes straight by message.",
    "Comment gelatin, and the recipe sits in your messages.",
    "Comment gelatin, and I'll send the recipe in private.",
    "Comment gelatin, and the recipe goes to your inbox.",
]


def _montar_falas(rng, sub, rec, orgao, relacao, credibilidade, degrau):
    """As DUAS falas do 16s.

    take 1 = hook (A FALHA DELE, com dano concreto) + descoberta + bullet
    take 2 = mecanismo COM RAZAO -> prova curta -> follow -> CTA   <- FIM

    ⛔⛔ `orgao` E' UMA STRING, NAO MAIS UMA LISTA DE TRES (CT4, 2026-08-10).
    O motor sorteava tres apelidos distintos e gastava um por cena; medido, o
    apelido MUDAVA NO CORTE em 100% dos videos. Em 16s e dois takes o corte zera
    a memoria de trabalho do espectador, e trocar `soldier` por `Johnson` no
    segundo 9 obriga-o a remapear justamente quando ele ja' esta' com um pe'
    fora. UM apelido por video, repetido nos dois takes; a variacao continua
    existindo ENTRE videos, que e' onde ela nunca custou nada.
    ⚠️ Compatibilidade: se vier lista (chamada antiga), usa-se a primeira.

    ⚠️ `rec` (a receita) NAO ENTRA MAIS EM FALA NENHUMA — CT5. Ela continua
    sorteada, no ledger e no painel, e continua mandando no IMAGE/TAKE 02 e na
    bancada-recibo. O parametro fica na assinatura porque a bancada e o painel
    o consomem pelo spec; tira-lo daqui e' refactor de chamada, nao de copy.

    Filtros POR CONSTRUCAO, todos com fallback medido no self-test:
    · `degrau`        — a escada da moderacao do hook e' escolha do Ed
    · `credibilidade` — confirma (default) x desmente, nos dois pools que mudam
    · ⭐ A CENA 1 NOMEIA O ORGAO EXATAMENTE UMA VEZ, e sempre em 2a pessoa
      (`your <nucleo>`, RS25). Se o hook ja' o nomeia (degrau 2), o bullet vem
      dos que nao nomeiam; se o hook nao nomeia (degrau 3/4/5), o bullet nomeia.
    · teto e piso POR CENA, e o eco de fato medido no VIDEO INTEIRO
    """
    if not isinstance(orgao, str):           # chamada antiga: lista de tres
        orgao = orgao[0]
    # ----- cena 1 ----------------------------------------------------------
    hooks = [h for h in HOOKS if h["degrau"] == degrau] or HOOKS
    hk = rng.choice(hooks)
    hook = hk["txt"].format(s=sub["fala"], o=orgao)
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
        return txt + " " + bl.format(o=orgao) if bl else txt

    # ⚠️ O eco e' cobrado contra os DOIS beats, nao so' contra o bullet: medido,
    # a colisao real do degrau 4 era hook x DESMENTIDO ("That one about {s} has
    # been going around forever. Watch." + "That one's been going around for
    # years."), e uma guarda que so' olhasse o bullet nao veria nada.
    # ⛔⛔ O RS10 PASSOU A SER COBRADO NA FALA MONTADA, 2026-08-10. O filtro
    # `_sem_prazo` acima olha so' o HOOK, e ate' hoje isso bastava porque o
    # `your <nucleo>` sempre vinha dele. Com os degraus 3/4/5 quem carrega o
    # `your <nucleo>` e' o BULLET — entao a soma proibida (`your <nucleo>` +
    # PRAZO no mesmo take de 8s, a composicao literal que derrubou o video do
    # NECROSE) nascia DEPOIS da decisao do filtro e so' aparecia como ERRO de
    # lint. Medido antes do conserto: 18 ERRO em 200 sorteios no degrau 3 e 9
    # em 200 no degrau 4. Agora o motor nao monta o par; o linter fica de rede.
    # ⚠️ Desconta a NARRATIVA antes de procurar o prazo, exatamente como o
    # `_rs10_prazo` faz — `nineteen days later he walked in` conta a historia do
    # terceiro e nao promete nada a quem assiste.
    def _rs10_ok(txt):
        limpa = RS10_NARRATIVA.sub(" ", txt)
        return not (RS10_CORPO_2A.search(limpa) and RS10_PRAZO.search(limpa))

    def _validos(bullets, sem_eco=True):
        return [(b2, bl) for b2 in beat2 for bl in bullets
                if PISO_FALA[1] <= _w(_c1(b2, bl)) <= TETO_FALA[1]
                and _rs10_ok(_c1(b2, bl))
                and not (sem_eco and (_repete(hook, bl) or _repete(hook, b2)
                                      or _repete(b2, bl)))]

    # ⛔⛔ A ORDEM DOS FALLBACKS MUDOU EM 2026-08-10, e nao e' cosmetica.
    # Era `pref -> resto -> pref sem eco -> resto sem eco`: ou seja, bastava o
    # guarda de eco esvaziar `pref` para o motor cair no `resto` — e `resto`,
    # quando o hook NAO nomeia o orgao, e' justamente o conjunto de bullets SEM
    # `{o}`. Resultado: cena 1 sem `your <nucleo>` nenhum, que e' ERRO de RS25 e
    # falha de CT4 (o apelido sumia do take 1 e so' aparecia no take 2).
    # ⭐ Agora o eco cede ANTES da regra: `pref -> pref sem eco -> resto -> ...`.
    # Eco de trigrama e' desconforto; cena 1 sem o orgao e' o video nao dizer
    # do que se trata.
    op = (_validos(pref) or _validos(pref, sem_eco=False)
          or _validos(resto) or _validos(resto, sem_eco=False)
          or _validos([None]))
    # ⛔⛔ SORTEIO EM DOIS ESTAGIOS, 2026-08-10 — e a razao e' um numero.
    # `rng.choice(op)` sorteia PARES, e o numero de pares em que uma entrada
    # aparece e' inversamente proporcional ao tamanho dela: num teto de 25 uma
    # entrada de 5 palavras cabe com todas as outras e uma de 7 quase nao cabe.
    # Medido em 1.200 sorteios com o pool novo: o bullet `That happened to my
    # husband.` (5 palavras) saia 449 vezes e `What fixed my husband was a
    # glass.` (7) saia 28 — 16 para 1, num pool que o `--stats` conta como sete.
    # Pool assim nao e' pool de sete, e' pool de dois com cinco enfeites.
    # ⭐ Sorteando primeiro o BULLET entre os que tem ao menos um parceiro, e so'
    # depois o beat da descoberta entre os parceiros DELE, a probabilidade passa
    # a ser por ENTRADA e nao por PAR. ⚠️ O bullet escolhe primeiro por ser o
    # pool menor (6-7 elegiveis contra 13-14) e o mais espremido — e' a mesma
    # regra do orcamento do take 2: quem tem menos substitutos escolhe antes.
    if op:
        porb = {}
        for _b2, _bl in op:
            porb.setdefault(_bl, []).append(_b2)
        bl = rng.choice(sorted(porb, key=lambda x: (x is None, x or "")))
        c1 = _c1(rng.choice(porb[bl]), bl)
    else:                                   # nao acontece: medido no self-test
        c1 = _c1(min(beat2, key=_w), min(pref or elegiveis, key=_w))

    # ----- cena 2 — ⭐⭐ O TAKE DO MECANISMO + PROVA + FOLLOW + CTA ----------
    # ⛔⛔ A ORDEM DA STRING E' A DO CONTRATO, E O CTA E' O FIM (CT1):
    #     mecanismo (8) · prova (5) · follow (3) · CTA com cobertura (9) = 25
    # Ate' 2026-08-10 o gate vinha DEPOIS do pedido em 100% dos sorteios, e a
    # ultima coisa no ouvido era `The algorithm hides me from non-followers.`
    # A posicao final e' a que fica; ela tem de ser o pedido.
    #
    # ⭐ QUEM ESCOLHE PRIMEIRO E' QUEM TEM MENOS SUBSTITUTOS. A regra saiu MEDIDA
    # do ESCANDALO 16 e dos dois defeitos opostos (reservando o minimo em todos,
    # o ULTIMO beat fica preso; reservando a mediana em todos, o PRIMEIRO fica
    # preso). Aqui o beat espremido e' o MECANISMO — e' ele que carrega o literal
    # `gelatin trick` e a razao que a CT3 cobra —, e o beat intercambiavel e' o
    # FOLLOW, que escolhe por ultimo e absorve a sobra.
    #
    # ⚠️ ⛔ E COM OS QUATRO POOLS DE TAMANHO UNICO (8/5/3/9) ESTE SOLVER NUNCA
    # BINDA: toda combinacao da' exatamente 25. Ele fica como REDE, nao como
    # enfeite — no dia em que alguem acrescentar uma entrada fora do tamanho, e'
    # ele que impede o estouro silencioso, e o `_contrato_dos_pools` e' que
    # reprova a entrada. Rede sem lente e' rede que ninguem sabe que rompeu.
    def _rsv(vals):
        v = sorted(vals)
        return v[len(v) // 2]

    def _cabe16(pool, reserva, fmt):
        """⚠️ O fallback nao devolve o pool inteiro — isso e' estouro
        silencioso. Devolve a entrada mais CURTA, e quem reclama e' o linter."""
        v = [x for x in pool if _w(fmt(x)) + reserva <= TETO_FALA[2]]
        return v or [min(pool, key=lambda x: _w(fmt(x)))]

    _id = lambda x: x
    _fp = lambda x: x.format(o=orgao)
    _mn_p = min(_w(_fp(x)) for x in PROVAS16)
    _mn_g = min(_w(g) for g in GATES)
    _mn_c = min(_w(x) for x in CTAS16)
    mec16 = rng.choice(_cabe16(MECANISMOS16, _mn_p + _mn_c, _id))
    prova16 = _fp(rng.choice(_cabe16(
        PROVAS16, _w(mec16) + _rsv([_w(x) for x in CTAS16]), _fp)))
    cta16 = rng.choice(_cabe16(
        CTAS16, _w(mec16) + _w(prova16), _id))
    # ⛔⛔ CT8 (2026-08-10) — O BEAT DO FOLLOW SAIU DA FALA.
    # Ordem do operador: *"nao acho que deva ter follow me no cta, a
    # mensagem e' enviada independente de seguirem ou nao"*. O gate
    # existia no repo inteiro por uma PREMISSA ERRADA sobre a automacao
    # de DM, e quem opera a automacao corrigiu. As palavras liberadas
    # vao para o mecanismo e a prova.
    c2 = "%s %s %s" % (mec16, prova16, cta16)
    return [_pontuar(c1), _pontuar(c2)]


_MIN_BARREIRA = min(_w(b) for b in BARREIRAS)


def sortear(pagina, rng, ledger, travas=None, degrau=None,
            analogia=None):
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
    # ⛔⛔ O 4o POSICIONAL E' `travas`. A ui_agente passa o dicionario de
    # travas ali sempre que o motor declara contrato, e com a assinatura
    # antiga ele cairia dentro de `credibilidade` virando estado invalido EM
    # SILENCIO. O parametro antigo viaja DENTRO das travas — mesmo
    # conserto do TROCA. ⚠️ Desempacotar aqui, na PRIMEIRA linha do corpo:
    # a primeira versao fazia isso la' embaixo, no site da REF, e `credibilidade`
    # e' usado antes — UnboundLocalError em 100%% dos sorteios.
    travas = travas if isinstance(travas, dict) else (
        {"credibilidade": travas} if travas else {})
    credibilidade = travas.get("credibilidade")
    cred = credibilidade or CREDIBILIDADE_PADRAO
    deg = degrau or DEGRAU_PADRAO
    fam = analogia or ANALOGIA_PADRAO

    hist = ledger.get(pagina, {})
    elegiveis = [n for n in NARRADORAS if n["idade"] >= IDADE_MINIMA_NARRADORA]
    # ⚠️ 28 e' o piso da RS19 — ela fala do marido.
    # ⭐ MODO BELA — o operador decidiu inclui-lo aqui depois de eu reportar
    # o conflito com a RS23. **A RS23 NAO FOI FURADA**: o helper recebe a
    # lista de banidos do proprio motor (`BANIDOS_DESEJO`) e so' sorteia
    # entradas que ja' a respeitam. A regra continua valendo e o modo entra
    # POR BAIXO dela — furar seria reintroduzir vocabulario que ja' custou
    # recusa em render.
    nar = (sc.ref_bela(elegiveis[0], rng,
                       idade_min=IDADE_MINIMA_NARRADORA,
                       banidos=tuple(BANIDOS_DESEJO))
           if (travas or {}).get("bela")
           else _evitando(rng, elegiveis, hist.get("narradora", [])[-3:]))
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
    # ⛔⛔ PELO MENOS DUAS DAS TRES CENAS USAM PALAVRA DIRETA (2026-08-03).
    # Ordem do operador, lendo o app: "use palavras alusivas mais diretas ao
    # penis, tal como wiener, peck-er, john-son, do que manhood".
    # `manhood` fala de MASCULINIDADE, nao do orgao — e' abstracao, o mesmo
    # vicio da copy num nivel abaixo. Saiu do pool dos 9 motores.
    # `soldier`, `old boy` e `tool` sao apelido afetivo: suavizam. Ficam, porque
    # tres motores os usam como fallback e porque variedade tambem conta — mas
    # entram em MINORIA, nunca em duas cenas do mesmo video.
    # ⛔⛔ CT4b (2026-08-10) — SO' TRES APELIDOS SAO SORTEAVEIS, e o
    # video usa UM so' nos dois takes (CT4). Antes: dois de NUCLEO_DIRETO
    # mais um do RESTO (`tool`, `soldier`) — e era o resto que aparecia em
    # 22% dos videos. Ordem do operador: `weiner` e `john-son` tambem, nao
    # so' `pec-ker`. `soldier` soa filme de guerra para ouvido americano e
    # `tool` e' ambiguo em giria dos EUA; os dois seguem no NUCLEO porque as
    # LENTES os usam para DETECTAR o orgao.
    _o1 = rng.choice(sc.APELIDOS_16)
    orgaos = [_o1] * 3
    rng.shuffle(orgaos)
    falas = _montar_falas(rng, sub, rec, orgaos, relacao, cred, deg)
    ban = _bancada_livre(rng, falas, hist.get("bancada", [])[-2:], rec, sub)

    return {"pagina": pagina,
            # 50/50, ordem do operador 2026-08-04
            "bandeira": rng.random() < 0.5, "narradora": nar, "corpo_prova": hom,
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
    # ⚠️ `rec` e `ban` nao sao desempacotados aqui: os dois so' alimentavam a
    # IMAGE/TAKE 02/03, o bloco da bancada, que caiu na fusao. Os eixos seguem
    # SORTEADOS, no ledger e no painel — e a receita entra na FALA da fundida,
    # via `{r}` — mas nenhum bloco os imprime.
    rea, ana = spec["reacao"], spec["analogia"]
    mec, falas = spec["mecanismo"], spec["falas"]
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
    # a escala do prop crescido, com a regua de quem esta' em quadro (RS8)

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
    b["IMAGE 01/02"] = (
        "IMAGE 01/02: Medium shot in %s, camera low and close to the top of the "
        "%s. Standing behind the %s is %s. %s Standing upright on the %s in "
        "front of her, held at its base in her closed fist that rests on "
        "the %s: %s. %s runs "
        "from her other hand down onto it in one unbroken column. %s %s %s %s %s"
        % (cen_set, bnc, bnc, ela,
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
    b["IMAGE 02/02"] = (
        "IMAGE 02/02: Medium shot in %s, same light. %s, stands frame-left. A "
        "%d-year-old %s man, %s, in %s and %s, stands beside her, upright, chin "
        "level, his eyes on the lens, saying nothing. %s %s They are the only "
        "two people in the frame. %s %s"
        % (cen_anc, mesma, hom["idade"], et, _descricao(hom),
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
    b["TAKE 01/02"] = (
        "TAKE 01/02: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway, no cuts, and the camera does not move. %s "
        "%s %s %s %s %s %s %s%s\n"
        "Dialogue: \"%s\"\n"
        # ⛔ 2026-08-03: era `dry powder hissing onto wood` e sobreviveu a' troca
        # do pool porque estava numa TRAVADA, nao no pool. Som de po' seco com
        # oleo caindo na imagem e' contradicao que o Veo resolve inventando —
        # e ele resolve pela TRILHA, nao pela imagem. Achado por medicao: o
        # literal saia em 120 de 120 takes depois da troca.
        "Audio: liquid pouring in a steady stream and running over the surface, "
        "quiet room tone in the %s. No music."
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
    b["TAKE 02/02"] = (
        "TAKE 02/02: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway, no cuts, and the camera does not move. %s %s "
        "She speaks straight into the lens, calm and even, no rush. Only she "
        "speaks.\nDialogue: \"%s\"\nAudio: quiet room tone in the %s. No music."
        % (RS_F12B_TAKE % prop["nome"], RS_KEYWORD_NA_MAO_TAKE,
           sonorizar(falas[1]), cen["curto"])
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
# ⛔ 2026-08-03: era `is hidden inside it and cannot be seen`, do tempo do po'.
# Com a substancia liquida a oclusao virou LAMINA e nao volume — o miolo mudou
# junto com a travada, senao o linter reprova 100% dos sorteios.
M_JATO = "hidden behind that sheet and cannot be seen"
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
    falta = _faltam(blocos["TAKE 01/02"], M_ESCALA_DIF)
    if falta:
        achados.append(("ERRO", "RS1 (R2-emenda): TAKE 01/03 sem o miolo da "
                                "escala diferencial %s — sem ele o Veo escala "
                                "tudo junto e a leitura vira inchaco" % falta))


def _rs2_jato(spec, blocos, achados):
    """R8: sem a cortina o Veo tem de resolver a transformacao em campo aberto,
    que e' a parte cara e e' onde ele inventa."""
    if M_JATO not in blocos["TAKE 01/02"]:
        achados.append(("ERRO", "RS2 (R8): TAKE 01/03 sem a oclusao pelo jato — "
                                "a transformacao fica em campo aberto"))


def _rs3_base(spec, blocos, achados):
    """R4: a ancora e' a MAO fechada na base, e a bancada e' solida.

    ⛔ Ate' 2026-08-02 esta regra cobrava a "base cravada na bancada" da
    R4-emenda. `base cravada` + `so' cresce para cima` sao ordens que o modelo
    nao consegue satisfazer juntas, e ele resolvia enfiando o prop na mesa. A
    emenda foi revogada no primeiro render."""
    if M_BASE not in blocos["TAKE 01/02"]:
        achados.append(("ERRO", "RS3 (R4): TAKE 01/03 sem a mao fechada na "
                                "base — sem ancora fisica o prop afunda na "
                                "bancada ou o take le' como TROCA DE OBJETO"))
    if M_SUPERFICIE not in blocos["TAKE 01/02"]:
        achados.append(("ERRO", "RS3 (R4): TAKE 01/03 sem a trava de superficie "
                                "solida — e' o que impede o prop de crescer "
                                "PARA DENTRO da bancada"))
    if RS_SEM_FLUTUAR not in blocos["TAKE 01/02"]:
        achados.append(("ERRO", "RS3 (R4): a amarracao e' DUPLA — falta "
                                "'No floating objects.' no TAKE 01/03"))
    for nome in ("IMAGE 01/02", "TAKE 01/02"):
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
    if M_APAGAO not in blocos["TAKE 01/02"]:
        achados.append(("ERRO", "RS4 (R7): TAKE 01/03 sem o apagao de 0,8s em "
                                "cima do morph"))


def _rs5_identidade(spec, blocos, achados):
    """R2b elemento 7: o gerador ADICIONA quando voce descreve um estado novo sem
    dizer que ele pertence ao objeto que ja' existe. Transformar e' caro,
    instanciar e' barato — ja' custou 5 tentativas de geoduck."""
    falta = _faltam(blocos["TAKE 01/02"], M_IDENTIDADE)
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
    sc.lint_nada_cresce(blocos, achados, excecao=("TAKE 01/02",),
                        rotulo="RS6 (achado 8)")


def _rs7_adverbio(spec, blocos, achados):
    """R2/R6: `slowly` e `gradually` sao P17 — crescimento lento e' invisivel e o
    feed da' 2 segundos. `comically large` so' vale para prop que NASCE grande."""
    achado = sorted(set(m.group(0).lower()
                        for m in RS7_TAKE1.finditer(_direcao(blocos["TAKE 01/02"]))))
    if achado:
        achados.append(("ERRO", "RS7 (R2/R6): TAKE 01/03 usa %s" % achado))


def _rs8_escala_igual(spec, blocos, achados):
    """R2-emenda: escala diferente entre as cenas le' como um SEGUNDO crescimento
    fora do take que o coreografa. E a regua e' o antebraco de QUEM SEGURA."""
    lidas = {}
    # ⚠️ `IMAGE 02/03` saiu da lista: o bloco nao existe mais. Os dois que
    # ficam sao os mesmos de antes, so' com o rotulo novo.
    for nome in ("TAKE 01/02", "IMAGE 02/02"):
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
        # ⛔ desconta a narrativa ANTES de procurar o prazo: `nineteen days later
        # he walked in` fala do homem da historia, nao promete nada a quem ve.
        limpa = RS10_NARRATIVA.sub(" ", fala)
        p = RS10_PRAZO.search(limpa)
        if p and RS10_CORPO_2A.search(limpa):
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
    # ⚠️ So' a cena 1: o segundo bloco da lista era o da bancada, que caiu.
    # ⛔ NAO repontei para `IMAGE 02/02` — a fundida e' a antiga cena 3, que
    # nunca foi alvo desta regra. Repontar por reflexo e' o erro que ja'
    # acusou quadro CERTO em quatro motores hoje.
    for nome in ("IMAGE 01/02",):
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
    # ⛔⛔ LENTE MORTA. O RECIBO — os itens pousados na bancada, `never
    # touched and never mentioned` — existia na IMAGE 02/03, a cena da
    # receita. Essa cena caiu, e a fundida herdou o quadro da 3, que nao tem
    # bancada. Repontar cobraria de um bloco que nao tem onde por os itens.
    if False:
        achados.append(("ERRO", "RS16: IMAGE 02/03 sem a bancada-recibo — o "
                                "'full recipe' fica sem lastro em imagem"))
    for nome in ("IMAGE 01/02", "IMAGE 02/02"):
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
    # A METADE DA LENTE QUE CONFERIA PERTENCIMENTO MORREU, e a conta que
    # justifica esta' medida: as CATORZE entradas de FUNDIDAS sao `cred:
    # "ambas"`, entao o filtro `f["cred"] in ("ambas", cred)` devolvia SEMPRE as
    # catorze, nos dois modos. Ela nunca separou confirma de desmente — era uma
    # checagem de pertencimento a um pool, e esse pool nao alimenta mais a cena
    # fundida (que e' composta de METADES16 + OUTRAS16 + CTA + GATE).
    # O CONTROLADOR CONTINUA VIVO: `--credibilidade` segue sorteado, no
    # ledger, no painel e governando a cena 1 e a obrigatoriedade do
    # corpo-prova. O que caiu foi so' a checagem que ja' nao checava nada.
    if False:
        achados.append(("ERRO", "RS17: a fundida da cena 2 nao pertence ao modo "
                                "'%s'" % cred))
    falta = _faltam(blocos["IMAGE 02/02"], M_F12B)
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
    if spec["analogia"]["desc"] not in blocos["TAKE 01/02"]:
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
    if M_PLATEIA not in blocos["TAKE 01/02"]:
        achados.append(("ERRO", "RS21 (R3): TAKE 01/03 sem a analogia de genero "
                                "da reacao — e' ela que mantem a cara de "
                                "escandalo sem 'mouth open'"))
    # ⛔⛔ LENTE MORTA. A trava de IMOBILIDADE existia porque a cena 2 vinha
    # DEPOIS do crescimento: o prop tinha de ser declarado parado ali, senao
    # o Veo continuava o morph no take seguinte. Com dois takes, o take que
    # seguia o crescimento e' a fundida, e ela ja' carrega a propria trava
    # no bloco que herdou da cena 3.
    if False:
        achados.append(("ERRO", "RS6 (achado 8): TAKE 02/03 sem a travada de "
                                "imobilidade com o prop nomeado"))
    if M_KEYWORD not in blocos["IMAGE 02/02"]:
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
# ⭐⭐ CT16 — AS SETE TRAVAS DO CONTRATO DE COPY 16s
# ---------------------------------------------------------------------------
# Doutrina: funil-organico/CONTRATO-COPY-16S.md · codigo: short_comum.lint_copy16
# ⚠️ `isca_absurda=False`: este angulo NAO promete nada que ele desminta meio
# segundo depois (isso e' TROCA/EXTERIOR/COLO). Logo o CT7 vale nos DOIS takes —
# verbo de ereccao colado no orgao reprova aqui tambem, nao so' no take do CTA.
# ⚠️ A lente entra por `extras` porque o motor usa `sc.lint_curto`, que nao a
# chama sozinha.
def _ct16(spec, blocos, achados):
    sc.lint_copy16(sys.modules[__name__], spec, achados, isca_absurda=False)


# ⛔⛔ LENTE APOSENTADA — "substantivo repetido no video" (do `lint_curto`).
# Ela dizia: duas cenas usando o MESMO apelido do orgao e' bordao. A CT4 do
# contrato de copy 16s REVERTE essa regra, e a reversao e' medida: com apelidos
# distintos por cena, o nome do orgao mudava no corte em 100% dos videos deste
# motor. Em 24s e cinco cenas o bordao era o risco; em 16s e dois takes o corte
# zera a memoria de trabalho e a troca custa mais que a repeticao.
# ⚠️ A lente NAO foi apagada — ela mora no `short_comum.py`, que e' compartilhado
# com os motores de 3 cenas, onde ela continua certa. O que este motor faz e'
# DECLARAR que ela nao se aplica a ele, e dizer qual regra a substituiu. Filtro
# explicito e' melhor que silencio: quem ler o `lint` ve' as duas regras e a
# razao da troca.
_AVISO_APOSENTADO = "substantivo repetido no video"


def lint(spec, blocos):
    # ⚠️ `teto_total` explicito: o padrao do `lint_curto` e' a soma dos tetos
    # (91), que aqui e' MENOR que a borda de cima da faixa da doutrina (96) — o
    # AVISO dispararia abaixo do numero que a propria faixa permite.
    achados = sc.lint_curto(
        sys.modules[__name__], spec, blocos, (1, 2, 3), TETO_FALA,
        literais=("gelatin trick",), teto_total=TETO_TOTAL,
        extras=(_rs1_escala, _rs2_jato, _rs3_base, _rs4_apagao, _rs5_identidade,
                _rs6_nada_cresce, _rs7_adverbio, _rs8_escala_igual, _rs9_topica,
                _rs10_prazo, _rs11_tokens, _rs12_conformidade, _rs13_negacao,
                _rs14_texto_e_objeto, _rs15_contraste, _rs16_recibo,
                _rs17_credibilidade, _rs18_analogia, _rs19_casting, _rs20_piso,
                _rs25_transferencia, _rs_travadas, _bandeira_5050, _ct16))
    return [(n, m) for n, m in achados if _AVISO_APOSENTADO not in m]


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
    """Reescreve as DUAS falas com os eixos atuais do spec e re-checa o recibo.

    ⛔⛔ CORRIGIDO EM 2026-08-10 — ESTA FUNCAO ESTOURAVA `IndexError` E NENHUM
    MEDIDOR VIA. Ela lia `spec["falas"][2]`, que existia no motor de 24s e nao
    existe aqui: o 16s tem DUAS falas. Todo botao da UI que mexe em copy
    (`substancia`, `narradora`, `corpo_prova`, `receita`, `prop`) passa por
    aqui, entao o app quebrava no primeiro clique. E' o mesmo modo de falha que
    ja' derrubou o `CENAS_UI` deste arquivo: defeito que so' existe na JANELA,
    porque os medidores olham o `sortear` e nunca o caminho do clique.

    ⚠️ O apelido do orgao e' PRESERVADO — e agora e' UM SO' (CT4), lido da fala
    que ja' esta' em cena. Re-sortear aqui trocaria o nome do orgao a cada
    clique em um eixo que nada tem a ver com ele.
    """
    orgao = sc.orgao_de(sys.modules[__name__], spec["falas"][0], NUCLEO[0])
    spec["falas"] = _montar_falas(rng, spec["substancia"], spec["receita"],
                                  orgao, spec["relacao"],
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
    """⛔⛔ MUDOU EM 2026-08-10: a receita NAO ENTRA MAIS EM FALA NENHUMA (CT5).

    Ela era o `{r}` das METADES16 (`My husband's {o} ignored cayenne.`) e por
    isso trocar o eixo obrigava a reescrever a fala. Com o ingrediente fora da
    boca, o eixo mexe so' no IMAGE/TAKE 02 e no recibo — entao re-sortear as
    falas aqui seria trocar hook e CTA do operador por um clique que ele deu em
    outro lugar. O que continua obrigatorio e' o recibo permanecer MUDO em
    relacao a' receita nova.
    """
    _trocar_bancada(spec, rng)


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
    """Re-sorteia a fala do take i (0-1) preservando o apelido do orgao.

    ⚠️ O apelido sai da fala 0 e nao da fala `i` — CT4: e' UM por video, e o
    take 2 tem de repetir exatamente o que o take 1 disse. Ler de `falas[i]`
    deixaria o clique no take 2 trocar o nome so' de um lado do corte, que e'
    exatamente o defeito que a reforma de 2026-08-10 fechou."""
    o = sc.orgao_de(sys.modules[__name__], spec["falas"][0])
    return _montar_falas(rng, spec["substancia"], spec["receita"], o,
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

    # ⭐⭐ O CONTRATO DE TAMANHO DOS POOLS DE FALA — reforma de 2026-08-10.
    # ⛔ POR QUE ISTO E' LENTE E NAO COMENTARIO: a copy dos dois takes so' cabe
    # porque cada pool tem tamanho FIXO ou TETO fixo, e a primeira versao errou
    # a conta em duas entradas de PROVAS16 sem que nada reclamasse — cinco
    # entradas nasceram mortas (6 palavras num slot de 5) e o autoteste as
    # contava como vivas. Contrato que so' vive no comentario e' intencao.
    #     take 1 = hook (<=13) + descoberta (<=7) + bullet (==5)   -> <=25
    #     take 2 = mecanismo (8) + prova (5) + follow (3) + CTA (9) == 25
    # ⚠️ O tamanho e' medido com o PIOR `{o}` e o PIOR `{s}` ja' substituidos:
    # `My husband's {o} holds out now.` parece cinco palavras e sao seis.
    _pior_o = max(NUCLEO, key=_w)
    _pior_s = max((s["fala"] for s in SUBSTANCIAS), key=_w)

    def _tam(txt):
        return _palavras(txt.format(o=_pior_o, s=_pior_s, r=""))

    for rotulo, pool, alvo, exato in (
            ("HOOKS", [h["txt"] for h in HOOKS], 13, False),
            ("CONFIRMACOES", CONFIRMACOES, 7, False),
            ("DESMENTIDOS", DESMENTIDOS, 7, False),
            ("BULLETS", [b["txt"] for b in BULLETS], 5, True),
            ("MECANISMOS16", MECANISMOS16, 8, True),
            ("PROVAS16", PROVAS16, 5, True),
            ("GATES", GATES, 3, True),
            ("CTAS16", CTAS16, 9, True)):
        for x in pool:
            n = _tam(x)
            if (n != alvo) if exato else (n > alvo):
                falhas.append(
                    "%s: %r tem %d palavras (%s %d) — o orcamento do take nao "
                    "fecha e a entrada sai do sorteio em silencio"
                    % (rotulo, x[:44], n, "exigido" if exato else "teto", alvo))
    # ⛔ e o orcamento fechado do take 2, conferido pela soma e nao pela fe'
    _t2 = 8 + 5 + 3 + 9
    if _t2 != TETO_FALA[2]:
        falhas.append("take 2: mecanismo+prova+follow+CTA = %d contra teto %d"
                      % (_t2, TETO_FALA[2]))
    # ⛔ CT3 — todo mecanismo carrega o literal E a razao (verbo + alvo)
    for x in MECANISMOS16:
        baixo = x.lower()
        if "gelatin trick" not in baixo:
            falhas.append("MECANISMOS16 sem o literal 'gelatin trick': %r" % x)
        if not any(re.search(r"\b%s\b" % v, baixo)
                   for v in sc.VERBOS_EFEITO_16):
            falhas.append("MECANISMOS16 sem VERBO de efeito (CT3): %r" % x)
        if not any(a in baixo for a in sc.ALVOS_16):
            falhas.append("MECANISMOS16 sem ALVO (CT3): %r" % x)
        if sc.ERECAO_16.search(x):
            falhas.append("MECANISMOS16 com verbo de ereccao (CT7): %r" % x)
        # ⛔ o DONO na abertura do take 2 — duas regras dependem disto:
        # o `medir_abertura` (a primeira sentenca do take tem referente) e as
        # nove PROVAS16 que abrem com `His {o}` e tomam o antecedente daqui.
        if "my husband" not in baixo:
            falhas.append("MECANISMOS16 sem o dono nomeado: a abertura do take "
                          "2 fica sem referente e o `His {o}` da PROVA vira "
                          "pronome orfao: %r" % x)
    # ⛔ CT4/CT7 — a prova carrega o orgao e NUNCA um verbo de ereccao com ele
    for x in PROVAS16:
        if "{o}" not in x:
            falhas.append("PROVAS16 sem {o} — o take 2 perde o apelido do "
                          "orgao e o CT4 quebra: %r" % x)
        if sc.ERECAO_16.search(x):
            falhas.append("PROVAS16 com verbo de ereccao colado no orgao "
                          "(CT7, ~95%% de recusa medida no COLO 16): %r" % x)
    # ⛔ CT1/CT5/CT6 — o CTA e' a ultima sentenca, diz onde chega e nao entrega
    # ingrediente
    for x in CTAS16:
        if sc.CTA_LITERAL not in x:
            falhas.append("CTAS16 sem o literal %r: %r" % (sc.CTA_LITERAL, x))
        if not sc.ISCA_CTA.search(x):
            falhas.append("CTAS16 sem isca (nao diz o que chega): %r" % x)
        if not sc.ENTREGA_16.search(x):
            falhas.append("CTAS16 sem a cobertura social (CT6: onde a receita "
                          "chega): %r" % x)
        if sc.INGREDIENTES_16.search(x):
            falhas.append("CTAS16 entrega ingrediente (CT5): %r" % x)
    # ⛔ CT2 — todo hook enuncia a FALHA dele, com dano concreto. Medido antes
    # da reforma: 30% dos take 1 nao diziam UMA palavra sobre o que o corpo dele
    # faz de errado, e sem auto-reconhecimento nao ha' comentario.
    for h in HOOKS:
        if not CT2_FALHA.search(h["txt"]):
            falhas.append("HOOKS sem falha enunciada (CT2): %r" % h["txt"])
    # ⛔ o degrau declarado tem de ter pool — `--degrau 3` rodava os DOZE hooks
    # pelo `or HOOKS` e a flag mentia.
    for d in DEGRAUS:
        if not [h for h in HOOKS if h["degrau"] == d]:
            falhas.append("degrau %d declarado em DEGRAUS e sem um hook no "
                          "pool — a flag cai no `or HOOKS` e mente" % d)

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
    # ⛔⛔ ENUMERACAO EXAUSTIVA DO TAKE 2 — reescrita em 2026-08-10.
    # Ela media a antiga cena 2 (o pool FUNDIDAS x cada RECEITA x cada orgao),
    # e desde o colapso para dois takes as FUNDIDAS nao alimentam fala nenhuma:
    # a enumeracao provava a viabilidade de um pool que nao roda, que e' o
    # oposto de medir. ⚠️ E a antiga cobranca de "cena 3" indexava PISO_FALA[2]
    # com o nome errado — nao existe cena 3 num motor de dois takes.
    # ⭐ Agora ela conta as combinacoes REAIS dos quatro beats do take 2 e
    # reprova a entrada que nao chega a NENHUMA — a definicao operacional de
    # entrada morta.
    combos2 = 0
    inalcancavel = {"MECANISMOS16": set(MECANISMOS16),
                    "PROVAS16": set(PROVAS16), "GATES": set(GATES),
                    "CTAS16": set(CTAS16)}
    for o in NUCLEO:
        for me in MECANISMOS16:
            for pr in PROVAS16:
                for g in GATES:
                    for c in CTAS16:
                        soma = (_w(me) + _w(pr.format(o=o)) + _w(g) + _w(c))
                        if not PISO_FALA[2] <= soma <= TETO_FALA[2]:
                            continue
                        combos2 += 1
                        inalcancavel["MECANISMOS16"].discard(me)
                        inalcancavel["PROVAS16"].discard(pr)
                        inalcancavel["GATES"].discard(g)
                        inalcancavel["CTAS16"].discard(c)
    print("  take 2 · %d combinacoes dentro da faixa %d-%d"
          % (combos2, PISO_FALA[2], TETO_FALA[2]))
    for nome, mortas in sorted(inalcancavel.items()):
        if mortas:
            falhas.append("%s: %d entrada(s) que nao cabem em combinacao "
                          "nenhuma do take 2 — pool morto: %s"
                          % (nome, len(mortas), sorted(mortas)[:2]))

    # --- os sorteios --------------------------------------------------------
    rng = random.Random(seed)
    freq, total_eixo, erros, avisos, n = {}, {}, 0, 0, 0
    # ⛔ era `{1: [], 2: [], 3: []}` e o relatorio fazia `min()` de lista vazia
    # na cena 3: o self-test estourava `ValueError` num motor de DOIS takes.
    palavras = {1: [], 2: []}
    for pag in sorted(ETNIA):
        ledger = {}
        for _ in range(n_por_pagina):
            spec = sortear(pag, rng, ledger, {"credibilidade": credibilidade},
                           degrau, analogia)
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
    # ⛔⛔ A CAPACIDADE E' A DO RENDER, NAO A DA FONTE — corrigido 2026-08-10.
    # A tabela dizia 26-31 e 29-35 (as taxas de 3,61-4,4 p/s da Sofia Maren) e o
    # relatorio imprimia "uso do orcamento" contra um numero que o proprio motor
    # ja' tinha declarado impossivel: o TETO_FALA e' 25 por ORDEM PERMANENTE do
    # operador, medido em render (*"sempre meca. Nao pode haver cortes de
    # fala"* — 32 cortou, 28 cortou, 25 nao). Medir contra 35 fazia o take cheio
    # aparecer como "71% do orcamento" quando ele esta' no limite fisico.
    # ⚠️ E era `{1:..,2:..,3:..}` num motor de DOIS takes.
    capacidade = {1: (20, 25), 2: (20, 25)}
    tot = 0.0
    for i in (1, 2):
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
