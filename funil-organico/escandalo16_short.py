#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AGENTE ESCANDALO SHORT — 3 cenas de 8 segundos (24s), SHORT NATIVO.

Doutrina: AGENTE_ED_ESCANDALO_V1.md (regras ES1-ES22)
Fonte:    concorrentes/sofia-maren-mapa-visual.md — leitura otica de 2 reels da
          pagina Sofia Maren, 92 frames (2 fps nos primeiros 4s), 2026-08-01.

⭐ O QUE DA' NOME AO AGENTE — O ESCANDALO ALHEIO
-----------------------------------------------
Um ou dois figurantes MUDOS, no MESMO plano focal da narradora, flanqueando a
cabeca dela, de olhos arregalados e sobrancelhas em pe', CONGELADOS assim pelos
8 segundos do hook — e a fala NAO os menciona uma unica vez. Eles encenam o
escandalo NO LUGAR do espectador, o que o autoriza a achar graca em vez de
sentir vergonha. Invariante 2/2 da fonte, e o unico elemento do lote com ZERO
existencia verbal em 42 segundos.

⛔ POR QUE NAO EXISTE NO REPERTORIO: o FLAGRANTE tem plateia, mas 3-5
desfocadas ao fundo, "textura, nao personagem", e com uma VITIMA. Aqui os
rostos estao EM FOCO, no primeiro plano, a altura da cabeca dela, e ninguem e'
humilhado — e' reacao a uma piada. E' laugh track feito de rostos.

⛔ POR QUE ESTE NAO DERIVA DE NINGUEM
------------------------------------
Os `<agente>_short.py` de flagrante/pee/vazamento/necrose colapsam um motor
longo de 5 cenas. Aqui nao ha' motor longo: o angulo nasce em tres cenas, igual
ao TROCA. Nao existe — e nao deve existir — um `escandalo_lucas.py`. Entao este
arquivo e' motor completo (pools proprios), mas continua usando a maquinaria
compartilhada (`short_comum.lint_curto`, `sc.selar_takes`) passando a si mesmo
como `base`, exatamente como o `troca_short.py`.

AS CINCO DECISOES DO OPERADOR (2026-08-01) — nao sao negociaveis
---------------------------------------------------------------
[D1] O TAKE 3 E' A PROVA NA MAO DELE — a F12b/TR10. Ele DE PE, mudo, queixo
     firme, olhos na lente, com o proxy nas DUAS MAOS dele, uma acima da outra,
     CENTRADAS CONTRA A FRENTE da peca de roupa, base no tecido e ponta pra
     cima. Ela ao lado, apontando um dedo pra baixo SEM ENCOSTAR, falando o CTA
     direto na lente. A F12b e' "a licao mais cara da operacao ate' hoje":
     quatro IMG 01 recusadas em sequencia, deterministicamente. O que bloqueia
     nao e' o prop, e' a AGENCIA — quem segura o objeto na virilha tem de ser o
     dono dela, e tem de estar ATIVO.
     ⛔ `groin`/`pubic`/`crotch` continuam fora: a coordenada vem da PECA DE
     ROUPA. Trocou-se a geometria, nunca o termo.
[D2] ⭐ O HOMEM QUE REAGE NO HOOK E' O MESMO QUE SEGURA A PROVA NO TAKE 3.
     Na fonte os figurantes somem aos 7s e NAO voltam — e' por isso que o lote
     marcou 2,5 de 4 no criterio do PIPELINE (sem vitima, sem arco). Trazendo o
     mesmo homem de volta na cena 3, ele deixa de ser figurante e vira ARCO:
     reage ao escandalo, e no fim e' ele quem segura a prova. Mesma pessoa,
     descricao INTEIRA nas duas cenas (marca facial + roupa + calca) — ancora
     curta ("the same man", "same hair") carrega a roupa e PERDE O ROSTO, que
     foi como o VAZAMENTO devolveu um senhor de oculos e bigode no lugar do
     corpo-prova.
[D3] O HOOK RODA NO DEGRAU 1, o literal da fonte, ciente de que e' o degrau 🔴:
     `If you wanna put your banana in your partner's donut five nights a week`.
     Ele empilha quatro gatilhos e viola a nossa propria regra de nunca nomear o
     proxy na `Dialogue:`. ⛔ ALCADA DO OPERADOR E ESTA' DECIDIDO — nao
     suavizar, nao trocar por conta propria. A escada INTEIRA entra como eixo
     sorteavel (`--degrau N`, default 1): assim uma recusa custa uma FLAG, nao
     um redesenho.
[D4] CASTING: o HOMEM e' travado na etnia da pagina (e' o corpo com que o
     espectador de 50-65 se identifica); a NARRADORA e' sorteada livre entre
     todos os arquetipos, e o motor NUNCA escreve adjetivo de etnia junto dela.
     ⚠️ SOLTA na etnia, nao na idade: piso de 28 anos (IDADE_MINIMA_NARRADORA).
[D5] ⛔ O LIVRO NAO E' ABSORVIDO. Nem o objeto, nem o beat do upsell (36% do
     video deles), nem a palavra `book` — que alem de tudo e' PROIBIDA na nossa
     automacao de DM. O CTA e' travado no literal `gelatin`.

⚠️ A COMPRESSAO E' DE BEAT, NAO DE FALA (ES16)
A fonte tem 139-150 palavras em 42s (3,3-3,6 p/s); o nosso SHORT tem 82-96 em
24s (3,4-4,0 p/s). A TAXA E' A MESMA — nao existe compressao de fala a fazer.
Eles tem 4 beats e nos temos 3 slots, e um TEM de ser o CTA: entao tres beats
deles cabem em dois takes. E' a opcao A da §4 do mapa (fundir o meio); B e C
foram descartadas pelo operador.

⚠️ TENSAO ARITMETICA ABERTA, PARA O ED DECIDIR (ES16)
A soma dos tetos por cena (22+34+26) e' 82, que e' exatamente o PISO do
orcamento total da doutrina (82-96). Logo o video so' entraria na faixa com as
tres cenas no teto exato, e nunca passaria de 82. O motor cobra o que da' para
cobrar — piso e teto POR CENA, medidos por enumeracao exaustiva no self-test —
e entrega hoje 62-77 palavras. Para chegar a 82-96 de verdade, ou os tetos por
cena sobem, ou a faixa total desce. E' decisao de copy: alcada.

⚠️ TRES PONTOS DE ALCADA QUE ESTE MOTOR IMPLEMENTA E QUE PRECISAM DO AVAL DO ED
1) O ORIFICIO NAO VOLTA NA CENA 3 (so' o eixo, `e_img_dele`). Motivo: eixo +
   orificio composto contra o corpo de um homem e' penetracao consumada sobre
   corpo humano — a familia exata das 4 recusas deterministicas de 2026-07-30.
   Ja' esta' escrito na ES4 da doutrina.
2) AS RELACOES SAO PARCEIRA-ONLY (`his wife of N years`, `his partner of N
   years`, `the woman he has been with for N years`). Motivo: 9 das 16 PROVAS
   da cena 3 sao carnais e em primeira pessoa (`Now his {o} won't let me
   sleep`) e contradiriam `the woman who does his shopping` — e relacao
   contradita na fala e' relacao ANULADA, que e' perder a alavanca 2 do
   protocolo de recusa. ⚠️ A doutrina (ES4) ainda lista `his neighbour of N
   years` e `the man she cooks for`: as PROVAS ja' carregam o campo `voz`
   (intima/terceiro) para o dia em que o Ed reabrir o pool — o motor FILTRA,
   nao se reescreve pool.
3) A TIGELA SOBE NA MAO LIVRE DELA na cena 3 (ES9 travada
   ES_KEYWORD_NA_MAO_IMAGE). A doutrina ES9 registra isso como TENSAO ABERTA e
   diz que, enquanto o Ed nao decide, vale a cena ordenada (tigela na bancada).
   Este motor implementa a forma FORTE do achado ③ por ordem explicita da spec
   de construcao. ⚠️ Se o Ed disser o contrario, e' trocar a travada de lugar —
   nao mexe em regra nenhuma.

⚠️ CORRECOES DE 2026-08-02 (revisao adversarial de tres lentes)
--------------------------------------------------------------
MODERACAO
· TETO_DIF_IDADE=30 no sorteio do homem. 14% do lote pareava narradora e
  corpo-prova com >= 35 anos de diferenca (pior caso 28 x 70) na composicao da
  F12b — e a ES11 ja' dizia que a politica de MENORES e' sensivel a geometria
  de intimidade + diferenca de idade. O risco vinha do SORTEIO, nao da cena.
· ES5 ganhou as duas travas que a doutrina anunciava e o codigo nao tinha:
  `your <nucleo>` + PRAZO no mesmo take (a linha do NECROSE) e `your <nucleo>`
  em forma AFIRMATIVA em vez de condicional/pergunta (precedente do
  `necrose_lucas.py`). ⛔ Nenhuma das duas toca o degrau 1: os hooks de la'
  nomeiam os props e nunca dizem `your <nucleo>`. Quem elas pegam e' o ESCAPE —
  duas das cinco entradas do degrau 2 tinham derivado para a afirmativa, e
  descer um degrau caia nelas em 40% das vezes.
· IMAGE 03/03 (o bloco mais arriscado do lote, e o unico sem guarda) perdeu 21
  palavras de REDUNDANCIA PURA: a relacao dita duas vezes e a FRASE_SEM_MARCA
  num bloco sem bancada-recibo. ⛔ A travada da F12b nao encolheu uma virgula.
· ES9: `held flat to the lens` -> `held level` SO' no objeto da keyword (mandar
  inclinar uma tigela rasa de cubos para a lente e' contradicao fisica); e as
  12 variantes do mecanismo passaram a nomear `gelatin` — duas diziam so' "pale
  powder", e po' anonimo no frame de `comment gelatin,` mata o achado ③.
· ES14 ganhou tabela de objeto banido e TETO DE PALAVRAS por bloco.
DOUTRINA
· ES5: a fisica do liquido passou a ser sorteada DENTRO do que a receita
  consegue produzir (`exige`). Sorteadas soltas, saiam "**the powder** goes
  under" com canela em pau e "opaque **gold**" com po' vermelho.
· Numeracao/regras devolvidas ao .md: elemento 6️⃣ do hook, ES1.4, ES4/TAKE,
  ES9 (forma forte), ES10/ES16 (cota 2/3), ES13 (`hardback spines` + o eixo
  CENARIO), ES14 (as excecoes de figurino e da bandeira-ima).
ENTROPIA
· o self-test cobra `MIN_OPCOES` sobre o MEDIDO (antes `len(c)` era impresso e
  descartado), mede os SETE modos (antes so' o default) e mede tambem os eixos
  por STRING e por COPY — `id` diferente com a mesma string nao e' variacao.
· P22 por cena entrou no --stats. ⛔ O AVISO por video NAO foi calado: calar o
  medidor nao e' cobrar a regra.

⭐⭐ REFORMA DA COPY FALADA — CONTRATO DE COPY 16s, 2026-08-10
-------------------------------------------------------------
Ordem do operador depois de uma revisao adversarial de 6 lentes independentes
sobre lotes renderizados. Doutrina: `funil-organico/CONTRATO-COPY-16S.md`;
lente: `short_comum.lint_copy16`; medidor: `medir_copy16.py`.
⛔ SO' A FALA MUDOU. Nenhum bloco IMAGE/TAKE, nenhum pool de cena, nenhuma
travada — o quadro e' alcada do operador.

    ANTES (medido, 200 sorteios)      DEPOIS (medido, 200 sorteios)
    CT1 100%  CT2 94%  CT3 100%       CT1..CT7 todos 0%
    CT4 100%  CT5 100% CT6 100%

A estrutura passou a ser:
    TAKE 1   hook (degrau sorteavel) + A FALHA DELE, com dano concreto
    TAKE 2   mecanismo COM RAZAO -> prova curta -> follow -> CTA   <- FIM

O que saiu de cada slot, e por que:
  · o VILAO OCULTO deu lugar a FALHA. Ele dizia de quem e' a culpa e nunca do
    QUE; e o operador ja' mandara tirar a farmacia da boca ("polui a copy e
    gera drifting"). Pool PARADO em VILOES, nao apagado.
  · a RECEITA FALADA (`{r}` + `collagen`) saiu inteira: entregava DOIS
    ingredientes de graca antes do pedido, e a receita e' a UNICA moeda que o
    comentario compra — gasta uma vez, esta' gasta para os outros 49 videos da
    pagina. Pools PARADOS em ABERTURAS16 e RECEITAS16.
  · o GATE deixou de fechar o video. Ele era a ULTIMA coisa no ouvido, colada
    no unico pedido que gera receita, e era ameaca. Virou FOLLOW de tres
    palavras ANTES do CTA. Pool PARADO em GATES.
  · o CTA passou a dizer ONDE a receita chega — mesma contagem de palavras,
    e paga a cobertura social do comentario, que leva nome e foto no feed.
  · o apelido do orgao passou a ser UM por video, repetido nos dois takes. ⛔
    E' uma REVERSAO declarada da regra de 24s, e o AVISO antigo do
    `lint_curto` esta' aposentado no `lint()` deste motor, com o motivo
    escrito ali.

Uso:
    python funil-organico/escandalo_short.py --pagina joe --n 2
    python funil-organico/escandalo_short.py --pagina marcus --n 3 --seed 42
    python funil-organico/escandalo_short.py --pagina ray --n 1 --dry-run
    python funil-organico/escandalo_short.py --pagina joe --n 10 --degrau 3
    python funil-organico/escandalo_short.py --pagina joe --n 5 --geometria montados
    python funil-organico/escandalo_short.py --pagina joe --n 5 --figurantes 2
    python funil-organico/escandalo_short.py --stats
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
# ⛔ Ledger proprio: 16s e 24s sao formatos diferentes e nao gastam o
# historico um do outro.
LEDGER = os.path.join(AQUI, ".escandalo-16-ledger.json")

TITULO = "AGENTE ESCANDALO 16"
SUBTITULO = ("2 takes de 8s = 16 segundos · o escandalo alheio, e a receita "
             "com o corpo-prova no mesmo quadro")
SLUG = "escandalo-16"

# ⛔⛔ DUAS CENAS. A 2 (a receita executada na bancada) morre como QUADRO e
# sobrevive como FALA; a fundida herda o quadro da 3, que e o payoff.
CENAS_UI = ["1 · O ESCANDALO + A FALHA", "2 · MECANISMO + PROVA + FOLLOW + CTA"]

# ES16. ⚠️ O ORCAMENTO E' PISO **E** TETO. Tratar o piso como "julgamento que
# mora na doutrina" foi o que deixou 48% das cenas 2 do TROCA abaixo dele: piso
# nao cobrado e' piso que nao existe. Os dois sao mecanicos e moram aqui.
# ⚠️ O teto da cena 1 subiu de 22 para 30 em 2026-08-02, e o numero e' medido,
# nao chutado: 8 segundos na nossa taxa de fala (3,4-4,0 palavras/s) comportam
# 27-32, e as falas mediam 18,4. Teto folgado nao e' seguranca — e' frase morta
# esperando para nascer, e foi assim que o slot virou enchimento.
# ⛔ O hook do degrau 1 fica limitado a 14 palavras: com o vilao de 14 no lugar
# do fecho, hook de 16 dava 30 exatos, folga ZERO (3,75 palavras/s).
# ⛔ 34 estava ACIMA DO FISICO (32 = 8s a 4,0 palavras/s, licoes §5).
# Nao estourava por sorte do pool — o maximo GERADO medido em 600
# sorteios era 31. Mas teto declarado acima da capacidade e' bomba
# armada: o lint compara com ESTE numero, entao aprovaria a primeira
# entrada longa que alguem acrescentasse, e a fala sairia cortada no
# render sem ninguem ver (licoes §27). Baixado em 2026-08-04.
# ⛔⛔ TETO 25 — ordem permanente do operador, 2026-08-05: *"sempre meca. Nao
# pode haver cortes de fala."* O numero vem de render, nao de conta: 32
# cortou, 28 cortou. Os exemplos que ele escreve a mao vivem em 16-25
# palavras (2,0-3,1 palavras/s).
# ⚠️ cena 3 cortava em 0,5%. Enumeracao exaustiva: 99,1% das 5.610 combinacoes ja'
# cabiam em 25, e sobrevivem 22/22 PROVAS, 17/17 CTAS e 15/15 GATES.
# ⭐⭐ MODOS DE REF — contrato compartilhado (short_comum), 2026-08-05.
# Toggles de `ref bela` (super model, corpo escultural, pouca roupa,
# olhos fora do comum) e `ref forte` (homem musculoso e atraente).
# ⛔ Desligados, o prompt volta IDENTICO ao de antes do recurso.
MODO_BELA = True

# ⛔⛔ DUAS CENAS, as duas no teto FISICO de 25 palavras.
# ⚠️ O motor de 24s declarava 32 na cena 2 com PISO 26 — par impossivel em
# que todo sorteio viola um dos dois, e por isso ele vivia na lista dos que
# cortam fala (o menor par FUNDIDA+SELO ja da 25).
# ⭐ Aqui a fundida e reconstruida em eixos que cabem por construcao, e o
# [ALCANCE] do autoteste reprova entrada que nao alcanca.
TETO_FALA = {1: 25, 2: 25}
PISO_FALA = {1: 16, 2: 18}

# ⚠️ A borda de CIMA da faixa da doutrina. ⛔ Nao usar a soma dos tetos (82):
# 82 e' o PISO do orcamento total, e o AVISO dispararia acima do numero que a
# ES16 exige como MINIMO.
TETO_TOTAL = 96

# [D4] congruencia: so' o HOMEM casa com o avatar da pagina. A narradora NAO usa
# este dict — ela e' sorteada livre, e o motor nunca escreve adjetivo de etnia
# junto dela (ES11).
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

# ⛔ PISO DE IDADE 28 — herdado do organicwave_short (`IDADE_MINIMA_MULHER`),
# com o motivo escrito: "ja' pagamos para descobrir que idade em cena com
# conteudo de ED e' zona sensivel". Pesa MAIS aqui: a cena 3 pareia a narradora
# com um homem de ate' 70 numa composicao de proxy falico, e a politica de
# MENORES e' a determinista (nao cede a regerar) e e' sensivel a geometria de
# intimidade + diferenca de idade, nao a idade real.
IDADE_MINIMA_NARRADORA = 28

# ⛔ ES11 — TETO DE DIFERENCA DE IDADE DO PAR DA CENA 3 (2026-08-02).
# O piso de 28 nao cobre o que a propria ES11 nomeia como gatilho: a politica de
# MENORES e' sensivel a GEOMETRIA DE INTIMIDADE + DIFERENCA DE IDADE, nao a
# idade absoluta. Sem teto, o sorteio livre pareava narradora de 28 com homem de
# 70 (42 anos de diferenca) na composicao da F12b — medido: 14% do lote com >= 35
# anos de diferenca, 25,8% entre 25 e 29. O risco nao vinha da cena, vinha do
# SORTEIO, e sorteio se conserta por filtro.
# ⚠️ 30 e' o maior valor que mata a cauda medida sem esvaziar o pool: com
# narradora de 28 sobram 4 homens (55-58), e o `_evitando` cuida do resto.
TETO_DIF_IDADE = 30

# ES10/[D3] — a escada de moderacao do hook. ⛔ O DEFAULT E' 1 por ordem
# explicita do operador, ciente de que e' o degrau 🔴.
DEGRAUS = (1, 2, 3, 4)
DEGRAU_PADRAO = 1

# ES2 — a geometria do par. `separados` e' o reel A, o unico de que temos numero
# (32,9K), e e' o degrau mais barato do risco nº2 da §9 do mapa.
GEOMETRIAS = ("separados", "montados")
GEOMETRIA_PADRAO = "separados"

# ES1 — quantos rostos congelados flanqueiam a cabeca dela. Default 1: e' o
# reel A e e' o unico compativel com [D2] sem carga extra (o segundo homem NAO
# volta na cena 3 e por isso nao vira arco).
# ⚠️ Faltam as views do reel B — sem elas nao da' para dizer se a plateia de
# dois performa melhor. Lacuna registrada, nao resolvida por opiniao.
FIGURANTES = (1, 2)
FIGURANTES_PADRAO = 1


# ---------------------------------------------------------------------------
# STRINGS TRAVADAS — ⛔ constantes, nunca redigitadas
# ---------------------------------------------------------------------------
# ⚠️ Os `%s` sao SLOTS do motor, nao texto a reescrever. Comprimir uma travada
# "com as minhas palavras" ja' entregou esqueleto 3D no lugar da placa em corte
# (RUNBOOK-app-offline §Por que portar). ES14: descricao livre encolhe, string
# validada e' INTOCAVEL.

CAUDA = "Shot on iPhone, natural grain. No on-screen text, no watermark."

# ES8/P12. ⚠️ ESCRITA NA AFIRMATIVA de proposito: "Nothing carries a readable
# label, logo or brand" injeta `label`, `logo` e `brand` num prompt cuja tese e'
# que nao ha' nenhum — a mesma mecanica de `fully clothed`
# (licoes-producao-veo §Declaracao e' municao). Quando da' para dizer o mesmo
# pela positiva, diz-se pela positiva.
FRASE_SEM_MARCA = "Every container in the frame is plain and unlabelled."

# ---------------------------------------------------------------------------
# ⭐⭐ ES1 — A PLATEIA CONGELADA. E' o agente inteiro.
# Slots: idade, etnia (ETNIA[pagina]), marca facial, roupa, calca, REACAO.
# ⚠️ Descricao INTEIRA (marca + roupa + calca), porque este mesmo rosto volta na
# cena 3 [D2] — ancora curta perde o rosto.
# ⚠️ `the way a studio audience reacts to a punchline` e' a alavanca 3 (nomear o
# genero da imagem) e e' o que mantem a cara de escandalo SEM `mouth open`.
# ⛔ zero `mouth open` / `lips parted` / `tongue` / `open-mouthed`: o banimento
# nasceu de um caso em que a boca era DELA, a centimetros da haste; aqui as
# bocas estao a altura da cabeca, longe do prop, em outras pessoas — e mesmo
# assim a reacao entra por sobrancelha, olho e gesto parado.
#
# 🔴 DECISAO ABERTA — ALCADA DO ED (levantada na revisao de 2026-08-02, NAO
# corrigida aqui porque e' CENA).
# Existem HOJE DUAS formulacoes desta travada, e elas divergem:
#   · a da doutrina (ES1): "Standing at either side of her head, at the same
#     distance from the camera as her face and just as sharply in focus, ..."
#   · a deste motor: "One step behind her right shoulder, level with her head
#     and in the same focal plane and the same sharp focus as her face, ..."
# A do motor importa `one step behind her right shoulder` do RISCO Nº3 da §9 do
# mapa (a saida para nao descrever a sobreposicao prop x corpo) e, ao junta-lo
# com `in the same focal plane`, diz a mesma coordenada de dois jeitos OPOSTOS:
# um passo atras e' outra distancia de camera. Prompt que se contradiz o modelo
# resolve como quiser, e o desfecho provavel e' a plateia DESFOCADA AO FUNDO —
# que e' exatamente o FLAGRANTE, do qual a ES1 propriedade 2 manda separar.
# ⚠️ E a do motor nao e' capricho: com UM figurante, `at either side of her
# head` (plural, escrita para dois) nao serve.
# ⛔ Escolher entre as duas e' CENA. Ate' a decisao do Ed vale esta, que e' a
# que o linter cobra (M_PLATEIA_IMG). Mesma situacao na ES2 (grau 1 e grau 2).
# ---------------------------------------------------------------------------
ES_PLATEIA_IMAGE = (
    "One step behind her right shoulder, level with her head and in the same "
    "focal plane and the same sharp focus as her face, stands a %d-year-old %s "
    "man with %s, in %s and %s. %s, the way a studio audience reacts to a "
    "punchline. He does not speak."
)

ES_PLATEIA_TAKE = (
    "His face stays exactly as it appears in the first frame — the same "
    "expression, held without change for the entire shot. He does not move, "
    "does not speak and does not look away. Only she speaks."
)

# ⚠️ A travada e' UMA so'. Para o SEGUNDO figurante o motor ESPELHA o ombro e
# passa a frase para o plural — sao as unicas palavras que mudam, e espelhar por
# `replace` mantem UMA fonte da verdade em vez de duas strings que envelhecem
# separadas (P9). ⛔ O conteudo da travada nao muda: mesma coordenada, mesmo
# plano focal, mesma analogia de genero, mesma imobilidade.
ES_PLATEIA_IMAGE_2 = ES_PLATEIA_IMAGE.replace("her right shoulder",
                                              "her left shoulder")

ES_PLATEIA_TAKE_2 = (
    ES_PLATEIA_TAKE
    .replace("His face stays", "The face of each man beside her stays")
    .replace("He does not move, does not speak and does not look away.",
             "Neither of them moves, speaks or looks away.")
)

# P13/F4b — dois personagens do mesmo sexo e da mesma faixa etaria FUNDEM se o
# contraste nao estiver ESCRITO. O pool ja' garante >= 3 eixos visiveis
# distintos (idade, marca facial, roupa); esta frase e' a quarta exigencia.
ES_CONTRASTE_FIGURANTES = (
    "The two men beside her are plainly different people: different ages, "
    "different faces and different clothes."
)

# ---------------------------------------------------------------------------
# ⭐ ES2 — O PAR. Dois graus, escolhidos pelo modo `--geometria`.
# Slots: eixo (e_img), orificio (f_img).
# ⚠️ `the way a grocer holds up two things to compare them` e `the way a cook
# holds up a skewer before it goes on the grill` sao a alavanca 3 do risco nº2
# da §9 do mapa, copiadas de la'.
# ⛔ Nao tirar um dos dois objetos, nao afastar o prop do corpo, nao cortar
# figurante: esgotadas as formulacoes, PARAR E REPORTAR ao Ed.
# ⛔ E a SOBREPOSICAO nunca e' descrita — ela e' fato de camera, nao instrucao.
# Zero `over his body` / `in front of his hips` / `at his waist`.
#
# 🔴 DECISAO ABERTA — ALCADA DO ED (2026-08-02, NAO corrigida aqui: e' CENA).
# Como na ES1, a doutrina carrega OUTRA formulacao, e a diferenca e' de leitura:
#   · grau 1, doutrina: "... and the two never touch: [o eixo] STANDING UPRIGHT
#     in her left fist WITH THE TIP POINTING AT THE CEILING, and [o orificio]
#     held flat to the lens in her right hand."
#     grau 1, motor: "... both at the height of her own chest and HELD FLAT TO
#     THE LENS ..." — deitar OS DOIS no plano da lente tira a verticalidade do
#     eixo, que e' o que o faz ler como eixo e nao como fruta.
#   · grau 2, doutrina: "[o eixo] RUN THROUGH THE MIDDLE OF [o orificio], which
#     sits partway along its length."
#     grau 2, motor: "... together as a single piece ..." — que diz que os dois
#     estao juntos na mao, nao que um ATRAVESSA o outro. O modo 🔴 pode nao
#     entregar a penetracao consumada que o rotulo 🔴 promete.
# ⚠️ E `the way a grocer holds up two things to compare them` nao existe no mapa
# nem na doutrina — e' analogia de genero criada aqui (a §9 so' traz a do
# cozinheiro/espeto). Funciona como alavanca 3, mas e' invencao do motor.
# ⛔ Ate' a decisao do Ed vale esta, que e' a que o linter cobra.
# ---------------------------------------------------------------------------
ES_PAR_SEPARADOS_IMAGE = (
    "She holds %s up in her left hand and %s up in her right, one on each side, "
    "both at the height of her own chest and held flat to the lens, the way a "
    "grocer holds up two things to compare them. The two objects do not touch "
    "each other."
)

ES_PAR_MONTADOS_IMAGE = (
    "In one raised fist, at the height of her own chest and held flat to the "
    "lens, she holds %s and %s together as a single piece, the way a cook holds "
    "up a skewer before it goes on the grill."
)

# vale para os dois graus. E' a alavanca 4 (congelar a geometria).
# ⛔ Travada NUA e objeto NOMEADO: nada de `changes size, shape or state`, que
# injeta `size` e `state` num prompt cuja tese e' que nada muda.
ES_PAR_TAKE = (
    "Neither object moves at any point in the shot; they stay exactly as they "
    "appear in the first frame — completely motionless for the entire shot. Her "
    "hands do not move either."
)

# ---------------------------------------------------------------------------
# ⭐ ES4/[D1] — A F12b. COPIADA CARACTERE POR CARACTERE do TROCA §TR10
# (troca_short.py, TR_MAO_PROPRIA_IMAGE / TR_MAO_PROPRIA_TAKE), formulacao de
# 2026-08-01. ⛔ NAO reescrever: `beside the lap` -> `centred against the front`
# custou oito renders lidos, e `level with his groin` custou uma recusa.
# Slots IMAGE: peca da calca (NUA, sem oracao subordinada), proxy ancorado NELE
# (e_img_dele), relacao NOMEADA.  Slot TAKE: nome do eixo.
# ⛔ ZERO `groin` / `pubic` / `crotch`: a coordenada vem da PECA DE ROUPA.
# ⛔ ZERO `the victim` / `the narrator`: `victim` e' palavra que SIGNIFICA dano.
# ⚠️ SO' O EIXO volta na cena 3. O orificio NAO volta — eixo + orificio + corpo
# dele reproduz a penetracao consumada sobre um corpo humano, que e' a familia
# de composicao das 4 recusas deterministicas de 2026-07-30.
# ---------------------------------------------------------------------------
ES_F12B_IMAGE = (
    "Centred against the front of his %s, in both his own fists one stacked "
    "above the other, he holds %s — the base of it resting on the fabric, the "
    "tip pointing straight up. Standing beside him, %s points one finger down "
    "at it without touching him, talking straight to camera."
)

ES_F12B_TAKE = (
    "Her pointing finger stays close but never touches him. He keeps his eyes "
    "on the lens and never speaks; both his own fists stay where they are. The "
    "%s in his own fists stays exactly as it appears in the first frame — "
    "completely motionless for the entire shot."
)

# ---------------------------------------------------------------------------
# ⭐ ES9 — O OBJETO DA KEYWORD NA MAO NO FRAME DA KEYWORD (achado ③ do mapa).
# Entra no IMAGE 03/03 NO LUGAR de "Behind them on the counter: [mecanismo]" —
# custo zero de densidade no bloco mais arriscado do lote (F12c/ES14), e a cena
# que diz `comment gelatin,` passa a ter gelatina numa mao.
# A mao livre e' a ESQUERDA porque a travada da F12b ja' comprometeu a direita
# com o dedo que aponta. Slot: mecanismo["curto"].
# 🔴 Esta e' a forma FORTE do achado; a doutrina ES9 registra a escolha como
# tensao aberta (ver docstring, ponto 3 de alcada).
# ---------------------------------------------------------------------------
# ⚠️ `held level` e NAO `held flat to the lens` (correcao de 2026-08-02).
# `held flat to the lens` e' a formulacao do mapa §9 e nasceu para o DONUT — um
# anel, cuja face inteira e' a leitura. Estendida ao objeto da keyword, ela manda
# INCLINAR para a camera uma tigela rasa de cubos, uma bandeja e uma panela: e'
# contradicao fisica dentro do proprio IMAGE, e prompt que se contradiz o modelo
# resolve como quiser. `held level` mantem o objeto na mao, na altura do peito e
# em quadro no frame da keyword — que e' tudo o que a ES9 pede — sem mandar
# derramar. ⛔ A travada do PAR (ES2) nao muda: la' o `flat to the lens` e' certo.
ES_KEYWORD_NA_MAO_IMAGE = (
    "In her own free left hand, raised to the height of her chest and held "
    "level, she holds %s."
)

ES_KEYWORD_NA_MAO_TAKE = (
    "What she holds in her own free left hand stays at that same height and "
    "does not move for the entire shot."
)

# ---------------------------------------------------------------------------
# ES8 — A BANCADA-RECIBO (TROCA §TR7). ⚠️ SO' NO IMAGE 02/03.
# ⛔ Fora do IMAGE 01 (que ja' carrega ela + o homem + os dois props) e fora do
# IMAGE 03 (o bloco mais arriscado do lote): densidade e' superficie de bloqueio
# (ES14) e o lastro do `full recipe` ja' foi provado na cena 2.
# Slots: bancada do cenario, itens do recibo.
# ---------------------------------------------------------------------------
ES_BANCADA_RECIBO = (
    "Laid out on the %s beside her, never touched and never mentioned: %s. "
    + FRASE_SEM_MARCA
)

# ---------------------------------------------------------------------------
# ES5 — A RECEITA EXECUTADA, em batidas com segundos (metodo 🟢 de
# prop-metaforas §Coreografia: "verbo sozinho nao e' instrucao — o Veo precisa
# do COMO"). ⛔ ZERO medida, ZERO horario: forma e gesto.
# Slots: receita["gesto"], fisica["desc"], mecanismo["curto"].
# ---------------------------------------------------------------------------
ES_RECEITA_TAKE = (
    "0 to 3 seconds: %s. 3 to 5 seconds: her left hand turns a wooden spoon "
    "through it twice and lifts the spoon clear of the rim. 5 to 8 seconds: %s, "
    "and her right hand comes to rest on the board beside %s and stays there. "
    "She talks straight into the lens the whole time."
)

# ES9, detalhe forense (TR1): a peca do mecanismo ja' estava plantada desde o
# frame 1 — o reveal nao apresenta nada novo. Objeto que entra de fora do quadro
# nao e' premio, e' corte disfarcado.
# Slots: mecanismo["curto"] SEM artigo, bancada, mecanismo["pousado"].
# ⚠️ O detalhe forense e' POR MECANISMO: mandar desenhar "its lid lying face-up"
# numa TIGELA e' contradicao dentro do proprio IMAGE, e prompt que se contradiz
# o modelo resolve como quiser.
ES_PLANTADO_IMAGE = "The %s has been standing on the %s since the first frame, %s."


# ---------------------------------------------------------------------------
# ELENCO
# ---------------------------------------------------------------------------
# ⭐ [D4]/ES11 A NARRADORA E' SOLTA — pool unico, sem etnia declarada em lugar
# nenhum. O cabelo e' o descritor mais etnico que existe e o pool tem afro, box
# braids, ruivo, platinado, loiro e tapered: o render varia sozinho. Se o
# operador quiser garantir proporcao, isso e' filtro por pagina no sortear() e
# e' ORDEM DELE — nao se decide aqui.
# ⚠️ Marca facial obrigatoria (P6): e' o que segura a continuidade do rosto
# entre as tres cenas. Sem ela o Veo troca de pessoa.
# ⚠️ FIGURINO: o pool segue a fonte (cropped, joias de ouro), com 4 entradas
# cobertas para o operador poder rodar um lote coberto. 🟡 Divergencia
# deliberada do UN1 do UNCAO, que continua valendo integralmente la'.
# ⛔ Zero `baby tee`: o token `baby` entra de graca num prompt que ja' pareia
# mulher com homem de 55-70 e objeto falico. `ringer tee` e' a mesma peca.
# ⛔⛔ LEI DO REF — A NARRADORA E' SEMPRE SUPER FIT E LINDA.
# Ordem do operador, 2026-08-04, olhando o lote gerado por este agente:
# *"mulheres sempre super fit e lindas nos videos gerados pelo agente short
# escandalo"*. Vale como lei permanente, nao como ajuste de lote.
#
# ⚠️⚠️ ESTE POOL FOI REESCRITO PORQUE ERA A **QUARTA** OCORRENCIA DO MESMO ERRO
# MEU — depois do RESSURREICAO, do CLEAN e do COLO, e pela mesma causa exata:
# eu escrevi as cinco ultimas entradas (2026-08-02) para PREENCHER OS EIXOS QUE
# O `medir_personagens.py` PREMIA — `oculos`, `pele`, `porte` — e ele me
# devolveu narradoras de 44, 47, 50 e 52 anos, grisalhas, de oculos de leitura,
# com `sun-weathered skin`, `deep laugh lines` e `a notched scar in her upper
# lip`. Num agente em que ela e' quem vende para homem.
#
# ⛔ E A CAUSA RAIZ NAO ERA O POOL, ERA O MEDIDOR: os outros tres agentes tem
# excecao declarada para `oculos`; o ESCANDALO nao tinha. Sem a excecao, o gate
# reprovava o pool certo e o proximo agente o enchia de oculos de novo.
# A excecao foi adicionada junto com esta reescrita — consertar so' o pool
# deixaria o defeito voltar sozinho (licoes-de-construcao §18).
#
# AS TRAVAS DESTE POOL, e nenhuma e' negociavel:
#   · IDADE 28-35 — o piso e' o `IDADE_MINIMA_NARRADORA` (moderacao, ja' pago em
#     campo) e o teto e' a lei do REF. ⛔ Nada acima de 35.
#   · PORTE em 100% das entradas, e sempre ATLETICO: e' o eixo que muda a
#     silhueta no plano medio, onde ela vive nas tres cenas.
#   · ⛔ ZERO oculos, ZERO grisalho, ZERO pele castigada, ZERO ruga de expressao.
#   · ANCORA FACIAL (P6) obrigatoria e sempre SINAL DE BELEZA — sarda, covinha,
#     pinta, olho de cor incomum, falha entre os dentes, malar alto, argola no
#     nariz. ⛔ Nunca cicatriz feia, palpebra caida, dente lascado.
#   · ⛔ nenhuma diz POSTURA: `stooped` colidiria com a travada da ES4, que ja'
#     escreve `upright, chin level`. Ombro e' FORMA, nao pose.
#   · zero mencao a etnia [D4]/ES11 — a variacao mora no CABELO.
NARRADORAS = [
    {"id": "ruiva_sardas", "idade": 29,
     "marca": "a lean toned build with a flat midriff, long copper-red hair and a heavy dusting of freckles across her nose and cheeks",
     "roupa": "a cropped dark-green ribbed tank top and black leggings"},
    {"id": "caramelo_pinta", "idade": 31,
     "marca": "a slim athletic build with defined shoulders, wavy caramel-blonde hair and a small dark mole beside her left nostril",
     "roupa": "a cropped charcoal ribbed tank top and high-waisted black leggings"},
    {"id": "afro_curto", "idade": 34,
     "marca": "a compact tightly muscled build, a short natural afro and a small dark beauty mark high on her left cheekbone",
     "roupa": "a cropped mustard knit top and a thin gold chain"},
    {"id": "loira_covinha", "idade": 33,
     "marca": "a trim athletic build with a defined waist, long honey-blonde hair and a deep dimple in her right cheek",
     "roupa": "a fitted black t-shirt tucked into high-waisted jeans"},
    {"id": "rabo_alto", "idade": 30,
     "marca": "a lean dancer's build with long limbs, jet-black hair in a high slicked-back ponytail and a wide gap between her front teeth",
     "roupa": "a cropped grey sweatshirt cut off above the waist"},
    {"id": "tranca_caixa", "idade": 31,
     "marca": "a toned swimmer's build with square shoulders, waist-length box braids and full lips over a strong even smile",
     "roupa": "a cropped burgundy tank top and stacked gold bangles"},
    {"id": "cacho_alto", "idade": 28,
     "marca": "a slim strong build with a narrow waist, thick dark curls gathered high off her neck and a small heart-shaped birthmark below her right ear",
     "roupa": "a denim shirt knotted at the waist over a plain vest"},
    {"id": "bob_platinado", "idade": 28,
     "marca": "a wiry athletic build with slim hips, a bleached-platinum bob cut sharp at the jaw and a small hoop through her left nostril",
     "roupa": "a cropped lilac zip-up and gold rings on three fingers"},
    {"id": "franja_reta", "idade": 33,
     "marca": "a slender long-limbed build, long chestnut hair with a blunt fringe and a small crescent birthmark at her right temple",
     "roupa": "a rust-orange long-sleeve top pushed up to the elbows"},
    {"id": "cachos_bronze", "idade": 32,
     "marca": "a firm athletic build with toned arms, tight auburn curls worn loose and high sharp cheekbones over a wide bright smile",
     "roupa": "a cropped emerald wrap top and long gold drop earrings"},
    {"id": "tapered_macas", "idade": 34,
     "marca": "a lean muscular build with a long neck, a close tapered cut faded at the sides and a beauty mark under her right eye",
     "roupa": "a charcoal turtleneck and heavy gold hoops"},
    {"id": "tranca_unica", "idade": 30,
     "marca": "a tall lean build with fine collarbones, long jet-black hair in a single braid over one shoulder and a small dark tattoo of three stars behind her right ear",
     "roupa": "a cropped white crochet top and gold bangles"},
    {"id": "coque_bagunca", "idade": 32,
     "marca": "a slim toned build with a flat stomach, sandy-blonde hair in a messy topknot and pale grey-green eyes under dark brows",
     "roupa": "a sage-green tank top and a slim gold watch"},
    {"id": "morango_lente", "idade": 35,
     "marca": "a fit toned build with a small waist, long wavy strawberry-blonde hair and a beauty mark just above her upper lip",
     "roupa": "a cropped pale-blue knit top and a thin gold chain bracelet"},
    {"id": "crespo_solto", "idade": 32,
     "marca": "a strong compact build with toned shoulders, a big loose curl-out worn wide and arched brows over dark almond eyes",
     "roupa": "a cropped terracotta rib tank and a flat gold collar"},
    # + 2026-08-04: as cinco que substituem as cinco velhas (44-52 anos,
    # grisalhas e de oculos). Elas trazem os MESMOS eixos que aquelas traziam —
    # PORTE variado e ancora facial forte — sem nada que brigue com a lei do
    # REF. O porte agora esta' em 20/20, nao em 5/20.
    {"id": "ombro_largo", "idade": 29,
     "marca": "a broad-shouldered athletic build with a narrow waist, blunt-cut glossy black hair at the collarbone and striking pale green eyes",
     "roupa": "a cropped oatmeal rib tank and gold studs"},
    {"id": "alta_bronzeada", "idade": 33,
     "marca": "a tall lean frame with long legs, smooth sun-kissed skin, ash-brown hair knotted low and a small mole on her jawline",
     "roupa": "a cropped khaki tank and a thin leather cord at her wrist"},
    {"id": "cintura_curta", "idade": 30,
     "marca": "a short-waisted powerful build with visible shoulder definition, close-cropped dark hair and eyes of two different colours, one green and one brown",
     "roupa": "a chambray shirt tied off above the waist, cuffs turned back"},
    {"id": "raspado_lateral", "idade": 31,
     "marca": "a compact hard-trained build, black hair shaved close on one side and a straight fine nose over a wide full mouth",
     "roupa": "a cropped olive tank and short black-painted nails"},
    {"id": "cornrows_forte", "idade": 35,
     "marca": "a solidly athletic build with cut arms, cornrows running to the nape and smooth clear skin over high round cheekbones",
     "roupa": "a cropped scarlet knit top and a gold cuff"},
]

# ⭐ [D2]/[D4] O HOMEM — o que REAGE no hook e SEGURA A PROVA na cena 3. Dois
# pools espelhados (mesma idade, mesma roupa, mesma calca por indice) — o que
# muda e' so' o descritor de cabelo/barba, que e' onde a etnia se le'. Espelhar
# em vez de escrever dois pools independentes mantem a comparacao entre paginas
# honesta: a unica variavel que muda entre joe e marcus e' a etnia.
# ⚠️ 55-70 anos: e' o CORPO com que o espectador se identifica.
# ⚠️ A `calca` existe para a ancora de roupa da F12b (ES4) e nasce NUA, sem
# oracao subordinada — cada palavra a mais no IMAGE 03 e' superficie de bloqueio
# no bloco mais arriscado do lote (ES14).
HOMENS_CLARA = [
    {"id": "prata_pintinha", "idade": 58,
     "marca": "thick silver hair swept straight back and a large dark mole high on his left cheekbone",
     "roupa": "a plain navy short-sleeve work shirt", "calca": "khaki work pants"},
    {"id": "barba_branca", "idade": 62,
     "marca": "a full white beard trimmed close and deep-set pale grey eyes under heavy brows",
     "roupa": "a heather-grey pocket tee", "calca": "faded blue jeans"},
    {"id": "covinha_tempora", "idade": 56,
     "marca": "dark hair greying hard at the temples and a deep vertical dimple in his left cheek",
     "roupa": "an olive canvas shirt with the sleeves rolled to the elbow",
     "calca": "brown corduroy trousers"},
    {"id": "palpebra_pesada", "idade": 64,
     "marca": "a bald crown with close-cropped white hair at the sides and heavy hooded eyelids",
     "roupa": "a light blue short-sleeve button-down", "calca": "grey twill work pants"},
    {"id": "queixo_fendido", "idade": 55,
     "marca": "sandy blond hair going grey at the sides and a strong cleft chin",
     "roupa": "a charcoal henley with the sleeves pushed up", "calca": "dark denim jeans"},
    {"id": "aco_sardas", "idade": 60,
     "marca": "wavy steel-grey hair worn a little long and heavy freckling across his nose and cheeks",
     "roupa": "a faded red flannel shirt", "calca": "tan chinos"},
    {"id": "bigode_guidao", "idade": 57,
     "marca": "a shaved head and a thick grey handlebar moustache",
     "roupa": "a mustard-yellow snap-button shirt", "calca": "black work trousers"},
    {"id": "dentes_falha", "idade": 65,
     "marca": "white hair combed straight back and a wide gap between his front teeth",
     "roupa": "a cream short-sleeve camp shirt", "calca": "olive cargo pants"},
    {"id": "sinal_olho", "idade": 59,
     "marca": "short auburn hair fading to grey and a raised mole at the outer corner of his right eye",
     "roupa": "a slate-blue polo shirt", "calca": "stone-coloured chinos"},
    {"id": "flat_top", "idade": 61,
     "marca": "a flat-top cut gone completely white and very thick greying eyebrows",
     "roupa": "a forest-green fishing shirt with two chest pockets", "calca": "khaki shorts"},
    {"id": "mecha_branca", "idade": 63,
     "marca": "thick chestnut hair with a bright white streak at the left temple",
     "roupa": "a rust-red pocket tee", "calca": "grey sweatpants"},
    {"id": "corte_sobrancelha", "idade": 65,
     "marca": "a close silver crew cut and a long-healed nick through his right eyebrow",
     "roupa": "a blue-and-white plaid short-sleeve shirt", "calca": "brown canvas work pants"},
    {"id": "costeleta_larga", "idade": 64,
     "marca": "white hair parted at the side and wide old-fashioned sideburns down to the jaw",
     "roupa": "a tan corduroy shirt buttoned to the collar", "calca": "dark brown slacks"},
    {"id": "nariz_torto", "idade": 63,
     "marca": "thin white hair combed forward and a nose broken and set crooked years ago",
     "roupa": "a pale grey flannel shirt", "calca": "navy work trousers"},
    # + 2026-08-02: o operador mediu os dois pools e viu SEMPRE O MESMO ROSTO.
    # As catorze acima descrevem o homem quase so' por CABELO mais uma ancora —
    # catorze homens descritos so' por cabelo sao o mesmo homem catorze vezes, e
    # o gerador devolvia quase a mesma cara. As quatro novas trazem os eixos
    # que este pool nao acionava:
    #   · 56 — OCULOS, o eixo ZERADO aqui (0/14): armacao preta grossa, mais
    #     PORTE barrigudo.
    #   · 58 — PORTE seco e nervoso mais PELE castigada de sol, mais bigode
    #     chevron e dente de ouro (ancora ✅, a mesma coroa de ouro que ja'
    #     roda em quatro motores).
    #   · 67 — OCULOS de leitura meia-lua mais PORTE de ombros estreitos e
    #     caidos, barba curta aparada e orelha entalhada.
    #   · 69 — PORTE de pescoco grosso mais rosto barbeado e sinal de
    #     nascenca vinho na tempora.
    #   · a ancora e' sempre do lado ✅ de licoes-producao-veo §REF —
    #     DISTINTIVO, NUNCA DETERIORADO (cicatriz limpa, dente de ouro,
    #     orelha entalhada, sinal de nascenca).
    #   · ⛔ ombro caido e' FORMA do ombro, nao postura: `stooped`/`curvado`
    #     colidiria com a travada da ES4, que escreve `upright, chin level`.
    #   · o espelho por indice com o pool ESCURA (mesma idade, mesma roupa,
    #     mesma calca) esta' mantido nas quatro.
    #   · zero mencao a etnia: o motor injeta ETNIA[pagina] antes da marca.
    {"id": "oculos_barriga", "idade": 56,
     "marca": "a round-bellied build, sandy-grey hair over a receding hairline, thick black-framed glasses and a pitted scar on his right jaw",
     "roupa": "a grey bowling shirt", "calca": "black work jeans"},
    {"id": "chevron_ouro", "idade": 58,
     "marca": "a lean wiry build, sun-creased skin, close iron-grey hair, a thick chevron moustache and a gold front tooth",
     "roupa": "a faded chambray work shirt", "calca": "dark green work trousers"},
    {"id": "leitura_orelha", "idade": 62,
     "marca": "narrow sloping shoulders, white hair, a short boxed beard, half-moon reading glasses down his nose and a notched left ear",
     "roupa": "a burgundy cardigan", "calca": "pleated beige trousers"},
    {"id": "pescoco_mancha", "idade": 61,
     "marca": "a broad thick-necked build, straight white hair cut short, a clean-shaven face and a port-wine birthmark on his right temple",
     "roupa": "a maroon zip-up fleece", "calca": "washed indigo carpenter jeans"},
    # + 2026-08-04: DEZ pares novos, por ordem do operador — *"aumente o pool
    # de personagens para o escandalo short, esta muito repetitivo"*. 18 -> 28.
    # ⚠️ Todos 55-65: acima disso a entrada e' PESO MORTO, porque a narradora
    # vai ate' 35 (lei do REF) e o TETO_DIF_IDADE=30 poe o teto real em 65.
    # Cinco entradas antigas (66-70) nunca eram sorteadas e foram trazidas
    # para a banda no mesmo commit — 13 sorteaveis viraram 28.
    # ⛔ FIGURINO TODO NOVO: nenhuma roupa e nenhuma calca repete as 18
    # anteriores. Num plano medio o olho le' a ROUPA antes do rosto, e dez
    # homens novos na mesma camisa verde seriam o mesmo homem de novo.
    {"id": "bigode_aviador", "idade": 57,
     "marca": "a thick sandy-grey moustache, wire-rimmed aviator glasses and a heavy square jaw",
     "roupa": "a dark teal short-sleeve work shirt", "calca": "dark olive work trousers"},
    {"id": "careca_barbudo", "idade": 61,
     "marca": "a shaved head, a full salt-and-pepper beard and a deep scar through his upper lip",
     "roupa": "a sand-coloured linen shirt open at the collar", "calca": "faded black jeans"},
    {"id": "onda_longa", "idade": 63,
     "marca": "wavy white hair worn long over the ears, clean-shaven, and very pale blue eyes",
     "roupa": "a black quilted vest over a white tee", "calca": "light grey cargo trousers"},
    {"id": "costeleta_nariz", "idade": 59,
     "marca": "a short grey crew cut, thick mutton-chop sideburns and a bulbous reddened nose",
     "roupa": "a mustard waffle-knit long-sleeve", "calca": "rust corduroy trousers"},
    {"id": "ruivo_sardento", "idade": 56,
     "marca": "thinning ginger-grey hair, a freckled scalp and pale lashes",
     "roupa": "a washed denim western shirt with pearl snaps", "calca": "stonewashed blue jeans"},
    {"id": "bico_viuva", "idade": 64,
     "marca": "a widow's peak gone white, heavy black-rimmed glasses and a cleft in his chin",
     "roupa": "a deep purple polo shirt", "calca": "navy chinos"},
    {"id": "dente_ouro", "idade": 60,
     "marca": "close-cropped iron-grey hair, a neat pencil moustache and a gold tooth that shows when he grins",
     "roupa": "an oatmeal fisherman's sweater", "calca": "brown duck canvas trousers"},
    {"id": "sobrancelha_farta", "idade": 62,
     "marca": "a full head of white hair swept sideways, bushy untamed eyebrows and a long thin face",
     "roupa": "a brick-red short-sleeve button-down", "calca": "charcoal jogging bottoms"},
    {"id": "cavanhaque_claro", "idade": 58,
     "marca": "a bald crown ringed with grey, a heavy grey soul patch and deep laugh lines",
     "roupa": "a hunter-green thermal henley", "calca": "tan work trousers"},
    {"id": "franja_prata", "idade": 55,
     "marca": "short silver hair combed forward, clean-shaven, and a broad flat nose with an old bump",
     "roupa": "a pale yellow guayabera shirt", "calca": "dark green corduroys"},
]

HOMENS_ESCURA = [
    {"id": "prata_barba", "idade": 58,
     "marca": "close-cropped silver hair, a neat white beard along the jaw and a large dark mole high on his left cheekbone",
     "roupa": "a plain navy short-sleeve work shirt", "calca": "khaki work pants"},
    {"id": "locs_ambar", "idade": 62,
     "marca": "salt-and-pepper locs gathered back and deep-set amber eyes under heavy brows",
     "roupa": "a heather-grey pocket tee", "calca": "faded blue jeans"},
    {"id": "fade_covinha", "idade": 56,
     "marca": "a close grey fade and a deep vertical dimple in his left cheek",
     "roupa": "an olive canvas shirt with the sleeves rolled to the elbow",
     "calca": "brown corduroy trousers"},
    {"id": "cavanhaque", "idade": 64,
     "marca": "a smooth shaved head, a neat silver goatee and heavy hooded eyelids",
     "roupa": "a light blue short-sleeve button-down", "calca": "grey twill work pants"},
    {"id": "twists_queixo", "idade": 55,
     "marca": "short black twists just starting to grey and a strong cleft chin",
     "roupa": "a charcoal henley with the sleeves pushed up", "calca": "dark denim jeans"},
    {"id": "afro_sardas", "idade": 60,
     "marca": "a silver-flecked afro worn low and heavy freckling across his nose and cheeks",
     "roupa": "a faded red flannel shirt", "calca": "tan chinos"},
    {"id": "careca_bigode", "idade": 57,
     "marca": "a bald head and a thick grey moustache",
     "roupa": "a mustard-yellow snap-button shirt", "calca": "black work trousers"},
    {"id": "branco_falha", "idade": 65,
     "marca": "short white hair and a wide gap between his front teeth",
     "roupa": "a cream short-sleeve camp shirt", "calca": "olive cargo pants"},
    {"id": "hightop_sinal", "idade": 59,
     "marca": "a grey high-top fade and a raised mole at the outer corner of his right eye",
     "roupa": "a slate-blue polo shirt", "calca": "stone-coloured chinos"},
    {"id": "afro_curto_grisalho", "idade": 61,
     "marca": "a short grey afro and very thick greying eyebrows",
     "roupa": "a forest-green fishing shirt with two chest pockets", "calca": "khaki shorts"},
    {"id": "mecha_tempora", "idade": 63,
     "marca": "a close grey afro with a bright white patch above the left temple",
     "roupa": "a rust-red pocket tee", "calca": "grey sweatpants"},
    {"id": "barba_corte", "idade": 65,
     "marca": "a neat grey beard and a long-healed nick through his right eyebrow",
     "roupa": "a blue-and-white plaid short-sleeve shirt", "calca": "brown canvas work pants"},
    {"id": "costeleta_grisalha", "idade": 64,
     "marca": "close white hair and wide old-fashioned sideburns down to the jaw",
     "roupa": "a tan corduroy shirt buttoned to the collar", "calca": "dark brown slacks"},
    {"id": "nariz_torto_escuro", "idade": 63,
     "marca": "thin white hair worn close and a nose broken and set crooked years ago",
     "roupa": "a pale grey flannel shirt", "calca": "navy work trousers"},
    # + 2026-08-02: o espelho das quatro novas do pool CLARA — mesma medicao (o
    # operador viu sempre o mesmo rosto, porque as catorze acima descreviam a
    # pessoa quase so' por cabelo), mesmos eixos novos, mesma idade, mesma
    # roupa e mesma calca por indice. So' o descritor de cabelo/barba muda,
    # que e' onde a etnia se le' [D2]/[D4].
    #   · 56 — OCULOS (eixo ZERADO aqui) mais PORTE barrigudo.
    #   · 58 — PORTE seco e nervoso mais PELE castigada de sol, bigode chevron
    #     e dente de ouro.
    #   · 67 — OCULOS de leitura meia-lua mais ombros estreitos e caidos.
    #   · 69 — PORTE de pescoco grosso mais sinal de nascenca vinho na tempora.
    {"id": "oculos_recuado", "idade": 56,
     "marca": "a round-bellied build, grey stubble over a receding hairline, thick black-framed glasses and a pitted scar on his right jaw",
     "roupa": "a grey bowling shirt", "calca": "black work jeans"},
    {"id": "chevron_raspado", "idade": 58,
     "marca": "a lean wiry build, sun-creased skin, a grey buzz cut, a thick chevron moustache and a gold front tooth",
     "roupa": "a faded chambray work shirt", "calca": "dark green work trousers"},
    {"id": "leitura_coils", "idade": 62,
     "marca": "narrow sloping shoulders, close white coils, a short boxed beard, half-moon reading glasses down his nose and a notched left ear",
     "roupa": "a burgundy cardigan", "calca": "pleated beige trousers"},
    {"id": "pescoco_cachos", "idade": 61,
     "marca": "a broad thick-necked build, tight white curls cut short, a clean-shaven face and a port-wine birthmark on his right temple",
     "roupa": "a maroon zip-up fleece", "calca": "washed indigo carpenter jeans"},
    # + 2026-08-04: DEZ pares novos, por ordem do operador — *"aumente o pool
    # de personagens para o escandalo short, esta muito repetitivo"*. 18 -> 28.
    # ⚠️ Todos 55-65: acima disso a entrada e' PESO MORTO, porque a narradora
    # vai ate' 35 (lei do REF) e o TETO_DIF_IDADE=30 poe o teto real em 65.
    # Cinco entradas antigas (66-70) nunca eram sorteadas e foram trazidas
    # para a banda no mesmo commit — 13 sorteaveis viraram 28.
    # ⛔ FIGURINO TODO NOVO: nenhuma roupa e nenhuma calca repete as 18
    # anteriores. Num plano medio o olho le' a ROUPA antes do rosto, e dez
    # homens novos na mesma camisa verde seriam o mesmo homem de novo.
    {"id": "bigode_aviador_escuro", "idade": 57,
     "marca": "a thick greying moustache, wire-rimmed aviator glasses and a heavy square jaw",
     "roupa": "a dark teal short-sleeve work shirt", "calca": "dark olive work trousers"},
    {"id": "careca_barbudo_escuro", "idade": 61,
     "marca": "a shaved head, a full grey-flecked beard and a deep scar through his upper lip",
     "roupa": "a sand-coloured linen shirt open at the collar", "calca": "faded black jeans"},
    {"id": "twists_longos", "idade": 63,
     "marca": "silver twists worn long to the shoulders, clean-shaven, and deep-set dark eyes",
     "roupa": "a black quilted vest over a white tee", "calca": "light grey cargo trousers"},
    {"id": "costeleta_fade", "idade": 59,
     "marca": "a short grey fade, thick greying sideburns and a broad flat nose",
     "roupa": "a mustard waffle-knit long-sleeve", "calca": "rust corduroy trousers"},
    {"id": "sardas_escuras", "idade": 56,
     "marca": "thinning grey hair with a receding line and a scatter of dark freckles across his cheeks",
     "roupa": "a washed denim western shirt with pearl snaps", "calca": "stonewashed blue jeans"},
    {"id": "testa_alta", "idade": 64,
     "marca": "a high grey hairline, heavy black-rimmed glasses and a cleft in his chin",
     "roupa": "a deep purple polo shirt", "calca": "navy chinos"},
    {"id": "dente_ouro_escuro", "idade": 60,
     "marca": "close-cropped grey coils, a neat pencil moustache and a gold tooth that shows when he grins",
     "roupa": "an oatmeal fisherman's sweater", "calca": "brown duck canvas trousers"},
    {"id": "afro_largo", "idade": 62,
     "marca": "a full grey afro worn wide, bushy untamed eyebrows and a long narrow face",
     "roupa": "a brick-red short-sleeve button-down", "calca": "charcoal jogging bottoms"},
    {"id": "cavanhaque_escuro", "idade": 58,
     "marca": "a bald crown ringed with grey, a heavy grey soul patch and deep laugh lines",
     "roupa": "a hunter-green thermal henley", "calca": "tan work trousers"},
    {"id": "ondas_prata", "idade": 55,
     "marca": "short silver waves brushed forward, clean-shaven, and high broad cheekbones",
     "roupa": "a pale yellow guayabera shirt", "calca": "dark green corduroys"},
]


def homens_de(pagina):
    """[D4]/ES11 — o HOMEM casa com o avatar da pagina. Congruencia inviolavel."""
    return HOMENS_CLARA if "white" in ETNIA[pagina] else HOMENS_ESCURA


def mulheres_de(pagina):
    """[D4]/ES11 — a narradora e' SOLTA: pool unico, a pagina nao filtra nada.

    Existe para deixar a excecao explicita em codigo: e' a UNICA vez que "etnia
    do REF = etnia do avatar" nao vale, e vale porque neste angulo o REF nao e'
    o avatar — o avatar e' o homem que reage e segura a prova.
    """
    return NARRADORAS


# ---------------------------------------------------------------------------
# EIXOS VISUAIS
# ---------------------------------------------------------------------------
# ⭐⭐ ES1 — O ESCANDALO CONGELADO. Encaixa no slot final da travada
# ES_PLATEIA_IMAGE, logo antes de `, the way a studio audience reacts to a
# punchline`.
# ⛔ zero `mouth open` / `lips parted` / `tongue` / `open-mouthed`: a reacao
# entra por sobrancelha, olho arregalado, gesto parado e `caught mid-word`.
REACOES = [
    {"id": "sobrancelhas_altas",
     "desc": "his eyebrows have shot up and stopped there and his eyes are stretched wide"},
    {"id": "queixo_solto",
     "desc": "his lower jaw has dropped and stopped, his eyes wide, caught mid-word"},
    {"id": "olhos_na_lente",
     "desc": "his eyes are stretched wide and turned straight to the lens, eyebrows high"},
    {"id": "testa_franzida",
     "desc": "his forehead is pulled into deep horizontal lines under raised brows, his eyes wide"},
    {"id": "mao_no_rosto",
     "desc": "one hand has stopped halfway to his own face, fingers spread, his eyes wide"},
    {"id": "recuo_queixo",
     "desc": "his chin is pulled back into his neck, eyebrows up, eyes wide and fixed"},
    {"id": "sobrancelha_unica",
     "desc": "one eyebrow is driven far higher than the other and both his eyes are wide"},
    {"id": "riso_preso",
     "desc": "his cheeks are pushed up and his eyes creased shut at the corners, caught mid-laugh"},
    {"id": "mao_no_peito",
     "desc": "one hand is flat on his own chest, his eyebrows high and his eyes wide"},
    {"id": "cabeca_inclinada",
     "desc": "his head is tipped to one side, eyebrows up, eyes wide and unblinking"},
    {"id": "punho_no_queixo",
     "desc": "one fist has stopped just under his chin, knuckles up, his eyes wide above it"},
    {"id": "ombros_altos",
     "desc": "his shoulders are up around his ears, eyebrows high, eyes wide and staring"},
    {"id": "dedo_parado",
     "desc": "one index finger is stopped mid-point at nothing, his eyes wide and his brows high"},
    {"id": "sobrancelhas_juntas",
     "desc": "both eyebrows are driven up and pinched together, his eyes wide, caught mid-word"},
]

# ⭐ ES2 — O PAR: o eixo + o orificio. E' a primeira geometria de PENETRACAO do
# garimpo inteiro; todos os nossos props eram objeto solo.
# ⚠️ `fala_e`/`fala_f` sao SEMPRE uma palavra so' — o pior caso do teto da cena
# 1 depende disso.
# ⚠️ Os 4 ultimos tem `fala_f: None` e por construcao ficam FORA do degrau 1: o
# hook literal precisa nomear o orificio, e `onion ring` nao cabe em uma
# palavra.
# ⚠️ `e_img_dele` e' A MESMA ESCALA com a ancora no corpo DELE — a declaracao de
# tamanho tem de ser identica nas cenas 1 e 3, senao le' como crescimento. E a
# regua e' o antebraco de QUEM SEGURA (ES4).
PARES = [
    {"id": "banana_glace", "e_nome": "banana", "f_nome": "doughnut",
     "fala_e": "banana", "fala_f": "donut",
     "e_img": "a ripe banana at its natural size, the skin yellow and lightly spotted",
     "e_img_dele": "a ripe banana at its natural size, the skin yellow and lightly spotted",
     "f_img": "a glazed ring doughnut, the glaze still glossy and unbroken"},
    {"id": "banana_granulado", "e_nome": "banana", "f_nome": "doughnut",
     "fala_e": "banana", "fala_f": "donut",
     "e_img": "a ripe banana at its natural size, the skin yellow and lightly spotted",
     "e_img_dele": "a ripe banana at its natural size, the skin yellow and lightly spotted",
     "f_img": "a white-frosted ring doughnut covered in coloured sprinkles"},
    {"id": "banana_bagel", "e_nome": "banana", "f_nome": "bagel",
     "fala_e": "banana", "fala_f": "bagel",
     "e_img": "a ripe banana at its natural size, the skin yellow and lightly spotted",
     "e_img_dele": "a ripe banana at its natural size, the skin yellow and lightly spotted",
     "f_img": "a sesame bagel, the crust glossy and the hole cut wide"},
    {"id": "pepino_bagel_papoula", "e_nome": "cucumber", "f_nome": "bagel",
     "fala_e": "cucumber", "fala_f": "bagel",
     "e_img": "a long smooth English cucumber, as long as her forearm and as thick as her wrist",
     "e_img_dele": "a long smooth English cucumber, as long as his forearm and as thick as his wrist",
     "f_img": "a poppy-seed bagel, the hole cut wide and the crust matte"},
    {"id": "pepino_chocolate", "e_nome": "cucumber", "f_nome": "doughnut",
     "fala_e": "cucumber", "fala_f": "donut",
     "e_img": "a long smooth English cucumber, as long as her forearm and as thick as her wrist",
     "e_img_dele": "a long smooth English cucumber, as long as his forearm and as thick as his wrist",
     "f_img": "a chocolate-glazed ring doughnut, the glaze set matte and cracked at one edge"},
    {"id": "cenoura_glace", "e_nome": "carrot", "f_nome": "doughnut",
     "fala_e": "carrot", "fala_f": "donut",
     "e_img": "a large raw carrot, the skin still rough, as long as her forearm and as thick as her wrist",
     "e_img_dele": "a large raw carrot, the skin still rough, as long as his forearm and as thick as his wrist",
     "f_img": "a glazed ring doughnut, the glaze still glossy and unbroken"},
    {"id": "cenoura_bagel_tudo", "e_nome": "carrot", "f_nome": "bagel",
     "fala_e": "carrot", "fala_f": "bagel",
     "e_img": "a large raw carrot, the skin still rough, as long as her forearm and as thick as her wrist",
     "e_img_dele": "a large raw carrot, the skin still rough, as long as his forearm and as thick as his wrist",
     "f_img": "an everything bagel crusted with seeds and coarse salt flakes"},
    {"id": "linguica_bagel_liso", "e_nome": "sausage", "f_nome": "bagel",
     "fala_e": "sausage", "fala_f": "bagel",
     "e_img": "a thick smoked sausage link, as long as her forearm",
     "e_img_dele": "a thick smoked sausage link, as long as his forearm",
     "f_img": "a plain bagel, pale and dusted with flour"},
    {"id": "linguica_acucar", "e_nome": "sausage", "f_nome": "doughnut",
     "fala_e": "sausage", "fala_f": "donut",
     "e_img": "a thick smoked sausage link, as long as her forearm",
     "e_img_dele": "a thick smoked sausage link, as long as his forearm",
     "f_img": "a ring doughnut heavily dusted with white sugar"},
    {"id": "milho_glace", "e_nome": "corn", "f_nome": "doughnut",
     "fala_e": "corn", "fala_f": "donut",
     "e_img": "an ear of sweet corn stripped clean of its husk, kernels tight and glossy, as long as her hand",
     "e_img_dele": "an ear of sweet corn stripped clean of its husk, kernels tight and glossy, as long as his hand",
     "f_img": "a glazed ring doughnut, the glaze still glossy and unbroken"},
    {"id": "pastinaga_bagel_canela", "e_nome": "parsnip", "f_nome": "bagel",
     "fala_e": "parsnip", "fala_f": "bagel",
     "e_img": "a thick cream-coloured parsnip, as long as her forearm",
     "e_img_dele": "a thick cream-coloured parsnip, as long as his forearm",
     "f_img": "a cinnamon-raisin bagel, dark specks through the crumb"},
    {"id": "abobrinha_granulado", "e_nome": "zucchini", "f_nome": "doughnut",
     "fala_e": "zucchini", "fala_f": "donut",
     "e_img": "a long dark-green zucchini, as long as her forearm and as thick as her wrist",
     "e_img_dele": "a long dark-green zucchini, as long as his forearm and as thick as his wrist",
     "f_img": "a white-frosted ring doughnut covered in coloured sprinkles"},
    {"id": "banana_anel_cebola", "e_nome": "banana", "f_nome": "onion ring",
     "fala_e": "banana", "fala_f": None,
     "e_img": "a ripe banana at its natural size, the skin yellow and lightly spotted",
     "e_img_dele": "a ripe banana at its natural size, the skin yellow and lightly spotted",
     "f_img": "a thick battered onion ring, deep golden and crisp at the edge"},
    {"id": "pepino_anel_abacaxi", "e_nome": "cucumber", "f_nome": "pineapple ring",
     "fala_e": "cucumber", "fala_f": None,
     "e_img": "a long smooth English cucumber, as long as her forearm and as thick as her wrist",
     "e_img_dele": "a long smooth English cucumber, as long as his forearm and as thick as his wrist",
     "f_img": "a thick ring cut from a fresh pineapple, the core punched out and the flesh wet"},
    {"id": "cenoura_anel_pimentao", "e_nome": "carrot", "f_nome": "pepper ring",
     "fala_e": "carrot", "fala_f": None,
     "e_img": "a large raw carrot, the skin still rough, as long as her forearm and as thick as her wrist",
     "e_img_dele": "a large raw carrot, the skin still rough, as long as his forearm and as thick as his wrist",
     "f_img": "a thick ring cut across a red bell pepper, the wall glossy and the seeds cleaned out"},
    {"id": "daikon_anel_cebola", "e_nome": "daikon", "f_nome": "onion ring",
     "fala_e": "daikon", "fala_f": None,
     "e_img": "a pale daikon radish with the tapered end pointing up, as long as her forearm",
     "e_img_dele": "a pale daikon radish with the tapered end pointing up, as long as his forearm",
     "f_img": "a thick battered onion ring, deep golden and crisp at the edge"},
]

# ES5 — o preparo EXECUTADO pelas MAOS na cena 2. ⛔ ZERO medida e ZERO horario
# (V5 do VAZAMENTO): forma e gesto. `fala` e' o UNICO ingrediente que a boca
# cita (slot {r}); os outros 3 do recibo vem da BANCADA e nunca sao ditos (ES8).
# ⚠️ `cabecas` existe para o sorteio EVITAR por construcao a colisao entre o que
# a boca diz e o que a bancada mostra.
RECEITAS = [
    {"id": "beterraba", "fala": "beet powder", "cabecas": ("beet", "beetroot"),
     "img": "a tall glass of warm water with a shallow dish of deep red beet powder beside it",
     "gesto": "her right hand tips the shallow dish of deep red powder into the glass"},
    {"id": "roma", "fala": "pomegranate", "cabecas": ("pomegranate",),
     "img": "a tall glass of warm water with a small glass jug of dark pomegranate juice beside it",
     "gesto": "her right hand pours a thread of dark juice down the inside of the glass"},
    {"id": "mel", "fala": "raw honey", "cabecas": ("honey",),
     "img": "a wide mug of warm water and an open jar of raw honey with a wooden dipper across the rim",
     "gesto": "her right hand lifts the dipper and lets a slow ribbon of honey fall into the mug"},
    {"id": "caiena", "fala": "cayenne", "cabecas": ("cayenne", "pepper"),
     "img": "a tall glass of warm water with a small saucer of coarse orange cayenne beside it",
     "gesto": "her right hand taps the saucer so a fall of coarse orange grains lands on the surface"},
    {"id": "gengibre", "fala": "ginger", "cabecas": ("ginger",),
     "img": "a squat glass of warm water and a knob of fresh ginger root grated into a small dish",
     "gesto": "her right hand scrapes the grated ginger off the dish into the glass with her thumb"},
    {"id": "curcuma", "fala": "turmeric", "cabecas": ("turmeric",),
     "img": "a heavy glass of warm water and a rustic ceramic bowl of deep yellow turmeric paste with a spoon standing in it",
     "gesto": "her right hand lifts the standing spoon of yellow paste and turns it into the water"},
    {"id": "melaco", "fala": "molasses", "cabecas": ("molasses", "syrup"),
     "img": "a tall glass of warm water and a stoneware crock of dark molasses with a wooden spoon in it",
     "gesto": "her right hand draws the spoon up out of the crock and lets the dark syrup fall in a thread"},
    {"id": "canela", "fala": "cinnamon", "cabecas": ("cinnamon",),
     "img": "a wide mug of warm water and three cinnamon sticks tied with twine lying on the board",
     "gesto": "her right hand snaps a cinnamon stick in half and drops both pieces into the mug"},
    {"id": "limao", "fala": "lemon", "cabecas": ("lemon",),
     "img": "a tall glass of warm water and a lemon halved face-up on the board",
     "gesto": "her right hand squeezes one lemon half over the glass, the pulp collapsing between her fingers"},
    {"id": "vinagre", "fala": "cider vinegar", "cabecas": ("vinegar",),
     "img": "a tall glass of warm water and an unlabelled amber bottle tipped against a small dish of cloudy vinegar",
     "gesto": "her right hand tips the amber bottle and lets a pour of cloudy vinegar run down the inside of the glass"},
    {"id": "melancia", "fala": "watermelon", "cabecas": ("watermelon",),
     "img": "a tall glass of warm water and a wedge of watermelon on the board with the juice pooling under it",
     "gesto": "her right hand presses the wedge against a metal strainer over the glass until the juice runs through"},
    {"id": "alho", "fala": "garlic", "cabecas": ("garlic",),
     "img": "a squat glass of warm water and a whole head of garlic with two cloves already crushed flat beside it",
     "gesto": "her right hand slides the two crushed cloves off the flat of the knife into the glass"},
    {"id": "salsa", "fala": "parsley", "cabecas": ("parsley",),
     "img": "a wide mug of warm water and a bundle of fresh parsley tied at the stems",
     "gesto": "her right hand tears a handful of parsley off the bundle and pushes it under the surface"},
    {"id": "bordo", "fala": "maple syrup", "cabecas": ("maple", "syrup"),
     "img": "a tall glass of warm water and a small unlabelled jug of dark maple syrup",
     "gesto": "her right hand pours a slow thread of dark syrup into the glass without stopping"},
    {"id": "cacau", "fala": "raw cacao", "cabecas": ("cacao", "cocoa"),
     "img": "a heavy glass of warm water and a shallow tin of dark unsweetened cacao powder",
     "gesto": "her right hand shakes the tin so a fall of dark powder lands on the water"},
    {"id": "semente_abobora", "fala": "pumpkin seed", "cabecas": ("pumpkin", "seed"),
     "img": "a tall glass of warm water and a small dish of hulled pumpkin seeds ground to a coarse green meal",
     "gesto": "her right hand pushes the coarse green meal off the dish into the glass with the back of a spoon"},
]

# ⭐ Eixo PROPRIO, mas NAO INDEPENDENTE da receita (correcao de 2026-08-02).
# A fisica do liquido e' a carga que a FALA NAO PAGA — e por isso ela nao pode
# contradizer o gesto que a mao acabou de executar DENTRO DA MESMA TRAVADA
# (ES_RECEITA_TAKE poe as duas na mesma frase). Sorteadas independentes, saiam:
#   · `canela` (dois paus quebrados no copo) + `dissolucao` ("**the powder**
#     goes under") — artigo definido apontando para um po' que ninguem pos;
#   · `beterraba` (po' VERMELHO) + `turvo` ("a flat opaque **gold**");
#   · `estratificado` ("a yellow slick floats up ... a raft of orange grains")
#     descreve OLEO + caiena, e nenhuma das 16 receitas poe oleo — a entrada
#     reintroduzia por descricao de fisica o ingrediente-fantasma que a ES6
#     bane (`bone marrow oil`).
# ⚠️ `exige`: None = compativel com qualquer receita; tupla = so' com essas.
# ⛔ `estratificado` fica com `exige` VAZIO — nao e' apagada, e' PARADA: a copy
# e' do operador, e o dia em que ele decidir se quer uma receita de gordura no
# pool ela volta com uma linha. Ate' la' nao e' sorteada.
# ⚠️ LIMITE HONESTO desta correcao: as seis entradas com `exige: None` ainda
# nomeiam COR (`a dark spiral`, `a slow brown cloud`, `fine dark sediment`,
# `dark below and pale above`) e continuam podendo cair sobre uma receita clara.
# Apertar tambem essas leva a concentracao do eixo `fisica` de 15% para 30% —
# acima da barra da ES22. Fechar isso de verdade pede mais entradas de FISICAS
# ou redacao neutra de cor, e as duas coisas sao COPY: alcada do Ed.
FISICAS = [
    {"id": "cor_sangue", "exige": ("beterraba", "roma", "melancia"),
     "desc": "the water turns from clear to magenta to an opaque blood red in the space of two seconds"},
    {"id": "estratificado", "exige": (),
     "desc": "a yellow slick floats up and holds on top while a raft of orange grains sits on it without dissolving"},
    {"id": "redemoinho", "exige": None,
     "desc": "a dark spiral winds down through the clear water and holds its shape without breaking"},
    {"id": "nuvem", "exige": None,
     "desc": "a slow brown cloud sinks from the surface to the bottom of the glass and settles there"},
    {"id": "espuma", "exige": None,
     "desc": "a fine pale foam climbs the inside of the glass and stays banked against it"},
    {"id": "sedimento", "exige": None,
     "desc": "a fine dark sediment drops out of the liquid and gathers in a ring at the bottom"},
    {"id": "fio_afunda", "exige": ("mel", "melaco", "bordo"),
     "desc": "a slow ribbon sinks whole to the bottom and lies there in a loose coil"},
    {"id": "turvo", "exige": ("mel", "curcuma", "vinagre"),
     "desc": "the water goes from clear to a flat opaque gold in one pass of the spoon"},
    {"id": "graos_boiando", "exige": ("caiena", "semente_abobora"),
     "desc": "coarse grains float in a raft on the surface and refuse to go under"},
    {"id": "dissolucao", "exige": ("beterraba",),
     "desc": "the powder goes under and vanishes completely, leaving the water a clear deep red"},
    {"id": "dois_tons", "exige": None,
     "desc": "the liquid separates into two clean bands, dark below and pale above, with a sharp line between them"},
    {"id": "bolhas", "exige": None,
     "desc": "small tight bubbles climb the inside of the glass and cling there in lines"},
    # + 2026-08-04: SEIS fisicas universais novas. ⚠️ Nao e' capricho — e'
    # aritmetica do `--stats`: as `exige: None` sao as unicas disponiveis para
    # TODA receita, e eram 6. Com seis opcoes o teto de concentracao de 17% e'
    # inalcancavel por construcao (1/6 = 16,7%, e qualquer desvio do sorteio
    # estoura). O self-test reprovou em 17,5% no `espuma`.
    # ⛔ A correcao e' POOL, nunca teto: afrouxar a barra seria maquiar o painel.
    # Doze universais poem o piso teorico em 8,3%.
    {"id": "neblina", "exige": None,
     "desc": "a milky haze spreads out from the spoon and fills the glass evenly"},
    {"id": "anel_superficie", "exige": None,
     "desc": "a thin bright ring forms where the liquid meets the glass and stays there"},
    {"id": "grumos", "exige": None,
     "desc": "small soft lumps form and hang suspended halfway down the glass"},
    {"id": "fios_descendo", "exige": None,
     "desc": "fine threads trail down from the surface like roots and reach the bottom"},
    {"id": "clareia", "exige": None,
     "desc": "the liquid clouds over completely and then clears again from the top down"},
    {"id": "borda_escura", "exige": None,
     "desc": "a darker rim gathers at the edge of the surface while the centre stays pale"},
]


def fisicas_de(receita):
    """ES5 — as fisicas que a receita sorteada consegue produzir."""
    return [f for f in FISICAS
            if f["exige"] is None or receita["id"] in f["exige"]]

# ES13 — o alibi de autoridade se faz por FORMA, nunca por TEXTO.
# ⛔ ZERO texto legivel na parede: a fonte compra 10 segundos de credibilidade
# com dois diplomas de texto legivel, e sao DOIS problemas — (1) texto legivel e'
# superficie de bloqueio (P12/ES14) e (2) e' credencial DECLARADA em imagem, que
# e' a primeira linha da cerca do ELA_DIAGNOSTICA ("ficamos com o teatro,
# largamos a credencial").
# ⛔ E nunca escrever que o texto e' ilegivel: negacao e' municao.
# ✅ A bandeira dos EUA se copia — nao e' marca, esta' no catalogo, custa uma
# linha, e e' 2/2 na fonte.
# ⚠️ `re_ancora` existe porque a entropia COLAPSA entre o spec e o prompt: sem
# ela metade do lote diria so' "in the same kitchen" nas cenas 2 e 3 e a
# bandeira sumiria do quadro a partir da cena 2.
CENARIOS = [
    {"id": "escritorio_diplomas", "bancada": "desk", "curto": "office",
     "set": "a home office with a full wall of dark hardback spines with gold detailing, two framed documents in dark wood frames with gold foil seals and a US flag on a floor stand in the corner",
     "re_ancora": "the same home office, the wall of dark hardback spines and the two framed documents behind her and the US flag on its floor stand",
     "luz": "warm lamp light with soft daylight from a window frame-left."},
    {"id": "escritorio_painel", "bancada": "desk", "curto": "study",
     "set": "a wood-panelled home study with a shelf of dark hardbacks, a green glass desk lamp and a small US flag on a short pole in a brass stand",
     "re_ancora": "the same wood-panelled study, the shelf of dark hardbacks behind her and the small US flag in its brass stand",
     "luz": "warm pooled lamp light with dim daylight from behind her."},
    {"id": "sala_estante", "bancada": "side table", "curto": "den",
     "set": "a den with floor-to-ceiling shelves of dark hardback spines, a worn leather wing chair and a US flag on a floor stand beside the doorway",
     "re_ancora": "the same den, the floor-to-ceiling shelves of dark hardbacks behind her and the US flag on its floor stand by the doorway",
     "luz": "low warm lamp light and one shaft of daylight from frame-right."},
    {"id": "cozinha_modesta", "bancada": "counter", "curto": "kitchen",
     "set": "a small older American kitchen with laminate counters and a window over the sink, a US flag magnet on the fridge door",
     "re_ancora": "the same small older kitchen, the US flag magnet still on the fridge door",
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
    # ⛔ `potted plants` saiu (2026-08-02): a ES14 bane planta por NOME — e'
    # superficie de bloqueio sem funcao de leitura —, e a entrada as carregava
    # no `set` E no `re_ancora`, ou seja, nas tres cenas.
    {"id": "varanda_sol", "bancada": "wicker table", "curto": "sunroom",
     "set": "a bright sunroom with wicker furniture and a US flag on a short pole by the sliding door",
     "re_ancora": "the same bright sunroom, the wicker furniture and the US flag on its short pole by the sliding door",
     "luz": "flooding daylight from three glass walls."},
    {"id": "rv", "bancada": "counter", "curto": "galley",
     "set": "the galley of a parked American RV, wood-veneer cabinets, a small sink and a US flag decal beside the window",
     "re_ancora": "the same RV galley, wood-veneer cabinets and the US flag decal still beside the window",
     "luz": "warm afternoon light through the RV window frame-right."},
    {"id": "cozinha_moderna", "bancada": "island", "curto": "kitchen",
     "set": "a modern American kitchen with matte black cabinets and a subway-tile wall, a small US flag in a pen cup beside the toaster",
     "re_ancora": "the same matte black kitchen with the subway-tile wall, the small US flag still in the pen cup beside the toaster",
     "luz": "cool even daylight from frame-right."},
]

# ES8 — o RECIBO de 3-4 itens: a boca cita 1 (o {r} da RECEITA), a imagem mostra
# 3-4. Nunca tocados, nunca mencionados. E' o que da' lastro ao `full recipe` —
# nos prometiamos a receita completa sem nunca provar em imagem que existe uma.
# ⛔ Zero marca legivel: FORMA no lugar de rotulo.
# ⚠️ `cabecas` existe para o sorteio EVITAR por construcao a colisao com o {r} e
# com as falas.
# ⚠️ Duas entradas diziam "with no label" (herdadas do TROCA). Isso e' a AUSENCIA
# declarada pela NEGACAO, que injeta `label` num prompt cuja tese e' que nao ha'
# rotulo nenhum — a mesma mecanica de `fully clothed`, e e' literalmente o ⛔ da
# ES8/ES13. Trocado por `plain`: mesmo objeto, mesma imagem, sem o token.
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
    {"id": "raiz_graos", "cabecas": ("ginger",),
     "itens": "a whole ginger root, a plain jar of coarse dark grains and a wooden butter knife"},
    {"id": "roma_pilao", "cabecas": ("pomegranate",),
     "itens": "a halved pomegranate face-up on a board, a small stone pestle and a folded linen cloth"},
    {"id": "cacau_mel", "cabecas": ("cacao", "cocoa", "honey"),
     "itens": "a plain tin of dark powder, a squat jar of thick amber syrup and a bone-handled spoon"},
    {"id": "pimenta_almofariz", "cabecas": ("cayenne", "pepper"),
     "itens": "a saucer of coarse orange grains, a small stone mortar and a stack of three unlabelled tins"},
]

# ⭐ ES9 — como a GELATINA aparece. `plantado` = na bancada da cena 2 desde o
# frame 1 (a peca plantada); `curto` = a referencia de continuidade que volta NA
# MAO LIVRE DELA na cena 3, no frame em que a keyword `gelatin,` e' dita;
# `pousado` = o detalhe forense POR MECANISMO.
# ⚠️ O mecanismo NAO e' eixo sorteavel de substancia: e' GELATINA nas doze
# variantes. Congruencia inviolavel — o mecanismo do criativo e' o que a VSL
# vende. Eles trocam entre livro, oleo e mel; nos nao.
# ⛔ E por isso as DOZE nomeiam `gelatin` no `plantado` E no `curto` (cobrado por
# enumeracao no self-test, 2026-08-02). Duas entradas diziam so' "pale powder" /
# "torn white sachet": no frame em que a boca diz `comment gelatin,` o
# espectador via um sache branco generico, que le' como fermento. O achado ③
# inteiro depende de COMANDO E PREMIO SEREM A MESMA IMAGEM — com po' anonimo
# nao ha' coincidencia palavra<->objeto, e a ES9 fica sem o seu unico argumento.
# ⛔ Nunca mandar desenhar tampa em tigela: contradicao dentro do mesmo IMAGE.
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
# COPY — cena 1: O ESCANDALO (hook + fecho)
# ---------------------------------------------------------------------------
# ⭐ ES10/[D3] — A ESCADA DO HOOK E' EIXO SORTEAVEL, E O DEFAULT E' O DEGRAU 1.
# Cada entrada carrega o seu `degrau`; o motor aceita `--degrau N`; sem a flag
# sai o 1. Assim uma recusa custa UMA FLAG, nao um redesenho.
#   1 🔴 o literal da fonte: verbo de penetracao + os dois objetos nomeados +
#        2a pessoa + frequencia. 9 hooks. ⚠️ Filtra PARES para os que tem
#        `fala_f` — o hook literal precisa nomear o orificio.
#   2 🟡 sai o verbo e saem os dois substantivos; entra o nucleo com grafia
#        homofona. `this` e' deixis, paga pelo quadro. 5 hooks.
#   3 🟢 na forma — condicional pura, a unica validada em producao contra a
#        politica de conteudo nocivo. 6 hooks.
#   4 🟢 o innuendo fica 100% na tela, a fala vira beneficio puro. Perde o
#        trocadilho, que e' o que faz rir. 5 hooks.
# ⛔ Os hooks de degrau 1 NOMEIAM o proxy na `Dialogue:`, o que viola a nossa
# propria regra. Isso e' [D3], alcada do operador, e esta' DECIDIDO — nao
# suavizar, nao trocar por conta propria. Registrado, nao corrigido.
# ⚠️ Numeros por extenso: o Veo soletra algarismo.
# ⛔ Nenhuma com PRAZO somado a `your <nucleo>` — e' a composicao que derrubou o
# video do NECROSE ("politicas contra a geracao de conteudo nocivo").
# Placeholders: {e} eixo do par, {f} orificio, {o} orgao.
HOOKS = [
    {"degrau": 1, "txt": "If you wanna put your {e} in your partner's {f} five nights a week..."},
    {"degrau": 1, "txt": "If you want your {e} still fitting your wife's {f} every night, this is for you."},
    {"degrau": 1, "txt": "Guys still putting the {e} in the {f} at seventy do one thing first."},
    {"degrau": 1, "txt": "You want your {e} going in that {f} five nights a week? Start here."},
    {"degrau": 1, "txt": "The {e} in the {f} four nights a week at sixty-two. That's the goal."},
    {"degrau": 1, "txt": "If you wanna be putting your {e} in her {f} at seventy, pay attention."},
    {"degrau": 1, "txt": "Married thirty years and still putting the {e} in the {f}? Not luck."},
    {"degrau": 1, "txt": "Your {e}, her {f}, five nights a week at sixty-five. That's the target."},
    {"degrau": 1, "txt": "Nobody puts the {e} in the {f} at sixty-eight by accident. One thing."},
    {"degrau": 2, "txt": "If you want your {o} doing this five nights a week..."},
    {"degrau": 2, "txt": "Your {o} doing this four nights a week at sixty. That's the thing."},
    {"degrau": 2, "txt": "Want your {o} still doing this every night after sixty-five?"},
    {"degrau": 2, "txt": "Men who get their {o} doing this at seventy all did one thing."},
    {"degrau": 2, "txt": "Your {o} doing this on a Tuesday, not just a Saturday."},
    {"degrau": 3, "txt": "If you want your {o} still working at eleven at night..."},
    {"degrau": 3, "txt": "If you want your {o} answering on a Tuesday, not just a Saturday..."},
    {"degrau": 3, "txt": "If you want your {o} outlasting the ball game, there's one thing first."},
    {"degrau": 3, "txt": "If you want your {o} up before the coffee is, this is it."},
    {"degrau": 3, "txt": "If you want your {o} keeping her up past midnight, start here."},
    {"degrau": 3, "txt": "If you want your {o} still on the clock at sixty-eight, start here."},
    {"degrau": 4, "txt": "Five nights a week, brother. That's what this does for a man of sixty."},
    {"degrau": 4, "txt": "Four nights a week at sixty-eight. That's what this does for a man."},
    {"degrau": 4, "txt": "Every night this week. That's what this does for a man of sixty-four."},
    {"degrau": 4, "txt": "Sixty-one years old and it doesn't quit. That's what this does."},
    {"degrau": 4, "txt": "Twice on a Sunday at sixty-six. That's what this does for a man."},
    # + 2026-08-02: ampliacao de variancia por ordem do operador.
    # Verificacao adversarial reprovou 32 de 54 propostas; estas
    # sobreviveram e foram medidas em 2800 sorteios.
    # ⛔ ERA "Three things stop the {e} going in the {f} after sixty. Only one
    # matters." — prometia uma LISTA de tres bloqueios e ainda prometia eleger
    # o unico que importa, e o video nao nomeia nenhum dos tres nem o eleito.
    # ⚠️ Um laco aberto que a cena 2 paga ("the gelatin trick") e' legitimo e
    # continua nos outros hooks; uma ENUMERACAO anunciada e nunca dita, nao.
    {"degrau": 1, "txt": "One thing decides if the {e} still goes in the {f} at sixty."},
    {"degrau": 1, "txt": "Your wife wants the {e} in the {f} tonight. Not next Christmas."},
    {"degrau": 1, "txt": "Could you put the {e} in the {f} tonight and again tomorrow?"},
]

# ---------------------------------------------------------------------------
# ⭐ ES23 — O VILAO OCULTO, o segundo beat da cena 1
# ---------------------------------------------------------------------------
# Ordem do operador, 2026-08-02, lendo os takes renderizados: "no take 1 desse
# agente escandalo, ha espaco de tempo pra incluir mais um bullet de copy, no
# angulo de vilao oculto". E, na mesma mensagem: "faltou palavras de alusoes ao
# falico mais diretas tb, tipo John-son, peck-er, wiener".
#
# Ele estava certo nos dois, e os dois eram mediveis:
#   · o teto da cena 1 era 22 palavras, mas 8 segundos na nossa taxa de fala
#     (3,4-4,0 p/s) comportam 27-32 — as falas mediam 18,4. O teto subiu para 30.
#   · 0 dos 9 hooks do degrau 1 nomeavam o orgao: a cena 1 nunca dizia o nome da
#     coisa. Medido depois do bullet: 1000 de 1000.
#
# ⛔ O VILAO SUBSTITUI O FECHO, nao se soma a ele. Os FECHOS eram enchimento
# ("Give me eight seconds", "Stay with me here") — exatamente o drifting que o
# operador mandou eliminar do repo inteiro. Trocar mantem o orcamento e ganha
# conteudo.
#
# ⚠️ A ARMADILHA QUE ESTE POOL DESVIA. Frase que AFIRMA o estado do corpo do
# espectador e' a familia que derrubou o video do NECROSE com "politicas contra
# conteudo nocivo". A saida e' o proprio angulo: a frase fala do VILAO, e o
# orgao aparece como OBJETO DO INTERESSE DELE, nunca como diagnostico.
#     ⛔ "Your {o} stopped working and they know why."   (diagnostico)
#     ✅ "Nobody makes a dime if your {o} starts working" (fala do vilao)
# As 10 entradas passaram pelo `_afirma_no_corpo()` com as 7 palavras do NUCLEO:
# zero disparos. Oito delas dizem `the {o}`, nao `your {o}`.
#
# ⭐ FRASE ORFA — CORRECAO DE 2026-08-03 (ordem do operador, lendo um take
# renderizado: "voce tem que contextualizar mais as coisas, ta' deixando o viewer
# sem entender o contexto e do que se trata").
# A REGRA NOVA: toda frase que nomeia uma CAUSA carrega, NA MESMA FRASE, o que
# ela quebra. Nao vale o orgao "aparecer em algum lugar da cena" — o operador
# reprovou exatamente uma cena em que o orgao estava la', na ULTIMA frase.
#     ⛔ "They sold you the age excuse."  -> desculpa para O QUE?
#     ✅ "They sold you the age excuse, and your {o} paid for it."
# Aqui a causa (a desculpa da idade) e o alvo (o orgao) ficam na mesma oracao.
# ⚠️ MESMA CONTAGEM DE PALAVRAS da entrada antiga (12 com `Johnson`, 13 com `old
# boy`): o alvo nao foi SOMADO ao teto da cena 1 — o segundo beat ("Sixty was
# never the {o}'s problem") foi absorvido pelo primeiro. Teto nao se sobe.
# ⚠️ Continua `the {o}`, nunca `your {o}`: em forma afirmativa o `_afirma_no_corpo`
# reprovaria (ES5), e nunca `his {o}`, que a ES1_MENCAO proibe na cena 1.
# ⛔⛔ POOL PARADO EM 2026-08-10 — O VILAO SAIU DO SLOT, A FALHA ENTROU.
# Duas ordens do operador convergiram no mesmo slot:
#   1. *"o vilao (a farmacia) polui a copy e gera drifting"* — e a entrada
#      "Who gets paid if your {o} never changes? The pharmacy does." e' a
#      farmacia nomeada na boca, alem de "never changes" nao descrever NADA
#      (muda como? de que para que?);
#   2. o CONTRATO DE COPY 16s, CT2 — MEDIDO em 200 sorteios: 94% dos videos
#      deste motor nao tinham UMA sentenca dizendo o que o corpo dele faz de
#      errado. Sem auto-reconhecimento nao ha' comentario: ele nao comenta
#      porque a copy e' boa, comenta porque SE VIU.
# ⛔ Em 8 segundos ha' lugar para hook + UM beat. Vilao e falha disputavam o
# mesmo slot, e a falha ganha porque e' ela que o KPI paga.
# ⚠️ PARADO, NAO APAGADO: e' copy validada e trazer de volta e' alcada do Ed.
VILOES = [
    "Nobody makes a dime if your {o} starts working on its own.",
    "That aisle has your money and nothing in it for the {o}.",
    "You've watched that ad a hundred times. It never once mentioned the {o}.",
    "Your grandfather knew this. Then somebody put a prescription on the {o}.",
    "Nobody told you, and that silence cost the {o} ten good years.",
    "They sold you the age excuse, and the {o} paid for it.",
    "Your doctor won't say this. There's no billing code for the {o}.",
    "Who gets paid if your {o} never changes? The pharmacy does.",
    "Add up what you've spent. None of it was meant for the {o}.",
    "They'll sell you a monthly plan before they'll sell the {o} an answer.",
]

# ---------------------------------------------------------------------------
# ⭐⭐ CT2 — A FALHA DELE, O SEGUNDO BEAT DA CENA 1 (2026-08-10)
# ---------------------------------------------------------------------------
# Contrato de copy 16s, CT2: *"o take 1 enuncia a FALHA, com dano concreto e de
# preferencia um numero"*. A melhor linha medida do parque inteiro e' de cinco
# palavras — `He'd lose it ten minutes in.` — um numero, um dano, nenhuma
# metafora. Este pool e' essa linha em dezoito formas.
#
# ⛔⛔ AS QUATRO CERCAS DESTE POOL, e nenhuma e' negociavel:
#   · ES1 — ZERO `he`/`him`/`his`. E' a trava que da' nome ao agente: o
#     figurante congelado existe 100% na imagem e 0% na fala. A falha aqui e'
#     do ESPECTADOR, nao de um terceiro — e' por isso que ela morde.
#   · ES5 — nunca `your <nucleo>` em forma AFIRMATIVA. Ou a frase diz
#     `the {o}` (a forma que 14 das 18 usam), ou ela e' PERGUNTA e termina em
#     `?`. Afirmar o estado do corpo de quem assiste e' a composicao que
#     derrubou o video do NECROSE por conteudo nocivo.
#   · CT7 — nenhum verbo de ereccao colado no orgao. Aqui o movimento e' o
#     inverso (quita, amolece, apaga), entao a cerca nao aperta — mas
#     `works again`/`comes back`/`hard` ficam fora por construcao.
#   · ES5/PRAZO — ZERO `in three months` / `three weeks later`: somado ao
#     `your {o}` que os hooks dos degraus 2 e 3 ja' trazem, e' a linha do
#     NECROSE de novo. Os numeros deste pool sao de RELOGIO e de IDADE, nunca
#     de prazo de tratamento.
# ⚠️ TAMANHOS PARECIDOS de proposito (7-10 palavras): pool que vai de 5 a 14
# num teto de 25 nao e' pool de 18, e' pool de 4 com catorze enfeites — o
# orcamento mata as entradas longas e quatro delas levam o lote inteiro.
# ⚠️ Todas nomeiam o `{o}`: no degrau 1 o hook nao carrega nucleo nenhum, e a
# cota do orgao (2 de 2) e o CT4 dependem desta frase.
# ⚠️ TREZE DAS DEZESSETE FALAM EM 2a PESSOA, e o numero e' MEDIDO, nao
# estetico: no degrau 4 nenhum dos cinco hooks aterrissa (a P22 do checklist da
# doutrina pede 2a pessoa ou imperativo por cena), entao a FALHA aterrissa
# sozinha — e o pool efetivo daquele degrau e' so' o que carrega `you`/`your`.
# ⭐ MEDIDO em 400 sorteios por degrau (conferencia de 2026-08-10, 2.800
# videos): 17/17 vivas nos degraus 1, 2 e 3, montados, dois figurantes e
# d2+montados+2fig; 13/17 no degrau 4, e as QUATRO que faltam sao exatamente as
# de 3a pessoa — nao e' entrada morta por aritmetica de orcamento, e' a P22
# cobrando o que tem de cobrar. ⛔ Zerar essa diferenca so' seria possivel
# escrevendo as dezessete em 2a pessoa, e ai' o pool vira uma frase so'
# repetida dezessete vezes.
# ⛔ DERRUBADA NA LEITURA EM VOZ ALTA (conferencia 2026-08-10):
#   · `One night in six, and the {o} failed you.` — a FRACAO nao resolve numa
#     audicao so'. "Uma noite em seis" e' a noite BOA ou a noite RUIM? As duas
#     leituras cabem, e elas dizem o contrario uma da outra. `Two of three
#     nights your {o} won't work?` diz a mesma coisa e nao vira charada, porque
#     o verbo (`won't work`) carrega o sinal junto com a fracao.
FALHAS = [
    "Ten minutes in, the {o} quits on you.",
    "Twenty minutes in, the {o} goes soft on you.",
    "Halfway through, the {o} quits and you're done.",
    "Two minutes of trying and your {o} won't hold?",
    "By eleven the {o} quits and your wife rolls over.",
    "Four years, and your {o} hasn't worked once?",
    "Every Saturday the {o} quits before you finish.",
    "Sixty years old and the {o} gave out on you.",
    "Fifteen minutes, and the {o} shut down on you.",
    "Twice this week the {o} quit on you.",
    "Nine at night and your {o} has already quit?",
    "Married thirty years, and the {o} stopped showing up.",
    "Ten minutes in and your {o} quits on you?",
    "Soft by eleven, and the {o} has quit again.",
    "Fifty-eight years old and the {o} went out early.",
    "Two of three nights your {o} won't work?",
    "Ten minutes is all, and then the {o} quits.",
]

# ⚠️ PARADO, NAO APAGADO. O FECHO saiu do slot da cena 1 pela ordem acima —
# tratava de atencao, e o que faltava ali era MOTIVO. Continua aqui porque e'
# copy validada e a decisao de traze-lo de volta e' do operador (alcada); se
# voltar, e' como beat de outra cena, nunca empurrando o vilao.
# ⛔ NENHUM contem `he`/`him`/`his`: a fala nunca menciona o figurante (ES1). E'
# o que da' nome ao agente; se a fala o menciona, ele deixa de encenar no lugar
# do espectador e vira personagem comentado.
FECHOS = [
    "You need to hear this.",
    "Do not skip this one.",
    "Give me eight seconds.",
    "Stay with me here.",
    "This is the part nobody says.",
    "Listen close. It's one thing.",
    "Watch what my hands do.",
    "Eight seconds. That's all.",
    "Nobody told you this part.",
    "Here's what actually does it.",
    "Keep watching. It's one thing.",
    "One thing. That's the whole secret.",
]

# ---------------------------------------------------------------------------
# COPY — cena 2: A RECEITA INCOMPLETA (fundida + selo)
# ---------------------------------------------------------------------------
# ⛔ ES6 — TODA fundida carrega o literal minusculo `gelatin trick`. Ele mora em
# cenas diferentes em cada agente e TODAS caem no colapso de 5 para 3; sem ele o
# criativo deixa de ser congruente com o que a VSL vende, que e' regra
# inviolavel e nao preferencia. O linter trava nisso duas vezes: no corpo das
# tres falas (lint_curto, parametro `literais`) e na CENA 2 especificamente.
#
# ⛔ ES6, as tres propriedades do V6 do VAZAMENTO, e as tres sao obrigatorias:
#   (1) a NEGACAO vem ANTES da solucao — o espectador sente a falta antes de
#       saber do que;
#   (2) o ORGAO e' nomeado na mesma frase, nunca pronome;
#   (3) usa o SIM que ele ja' deu — ele aceitou a receita, e agora descobre que
#       esta' a um ingrediente de completa-la.
#
# ⛔ ES7 — EXATAMENTE UMA palavra tecnica (vasodilator / nitric oxide /
# circulation / collagen / oxygen). Zero perde o verniz que compra a virada de
# piada de fruta para clinica em 8 segundos; duas viram aula, e aula nao cabe
# num take que ja' carrega a receita e a virada.
#
# ⛔ ES5 — ZERO medida e ZERO horario. A fonte diz "one teaspoon ... every
# morning on an empty stomach": isso e' DOSE, e o V5 do VAZAMENTO proibe. A
# saida e' FORMA e GESTO (`a spoon of`, `a pour of`, `two fingers of`).
#
# ⚠️ TODO template precisa do slot `{o}`: no degrau 1 a cena 1 nao nomeia o
# nucleo, entao as cenas 2 e 3 sao as unicas que sustentam a cota de 2/3. Um
# unico item sem `{o}` derrubaria o lote inteiro.
# ⛔⛔ POOL REESCRITO EM 2026-08-04 — A CENA 2 DEIXA DE ENSAIAR A RECEITA.
#
# Ordem do operador, lendo o TAKE 02 renderizado (`{r} into the glass, warm
# water over it, stir. Vasodilators. Without the gelatin trick it stays a warm
# drink and his {o} never knows. That's it. Both halves.`):
#
#     "a ref 'ensaia uma receita' e o take acaba: isso nao agrega nada em termos
#      de persuasao e nao cabe aqui no contexto de um take de poucos segundos.
#      Aqui poderia haver uma copy falada mais estrategica, com funcao pratica
#      mais eficaz, tal como: 'depois de tanto pesquisar, procurar, descobri um
#      truque chamado gelatin trick com ingredientes baratos que fez o peck-er
#      do meu parceiro mudar da agua pro vinho'."
#
# ⛔ O DIAGNOSTICO, e ele e' o vicio §4: o slot passava no linter e nao cumpria a
# funcao. `{r} in, warm water, stir` e' INSTRUCAO — e a instrucao ja' esta' sendo
# EXECUTADA pelas maos dela no mesmo quadro. Gastar 8 segundos de boca narrando o
# que o olho ja' ve' e' pagar duas vezes pelo mesmo beat e nao comprar nada.
#
# ⭐ A ESTRUTURA NOVA, quatro beats, e ela e' obrigatoria em toda entrada:
#     1. A BUSCA ......... o que ela tentou e falhou (e' aqui que mora a negacao)
#     2. A DESCOBERTA .... o mecanismo BATIZADO: `gelatin trick`
#     3. O BARATO ........ o `{r}` entra como PROVA DE PRECO, nao como passo
#     4. O RESULTADO ..... o que aconteceu com o `{o}` DELE, nomeado
#
# ⭐⭐ POR QUE A ESTRUTURA SALVA AS TRAVAS EM VEZ DE BRIGAR COM ELAS: a ES6 exige
# um marcador de NEGACAO antes do batismo, e a busca fracassada e' o lugar mais
# natural do video para ele — `two years of pills and nothing` faz o espectador
# SENTIR A FALTA antes de saber do que. A regra continua inteira e a copy ficou
# melhor. ⛔ ES7 continua valendo: UMA palavra tecnica por entrada, nunca duas.
#
# ⛔ E O VICIO DE DRIFTING FICA DE FORA POR CONSTRUCAO: o beat 4 de TODA entrada
# nomeia o `{o}` e diz o que ele passou a FAZER. Nenhuma termina em reacao vaga
# — `she noticed` sem objeto e' exatamente o que o operador reprovou no mesmo
# dia (licoes-de-construcao §20).
#
# ⚠️ 22 ENTRADAS, e a variacao e' nos QUATRO beats de forma independente: seis
# buscas diferentes, sete fontes de descoberta (ela mesma, comentario, cunhada,
# enfermeira, forum, colega dele, farmaceutico), cinco formas de dizer o preco e
# dez resultados distintos. ⛔ A imagem do operador (`da agua pro vinho`) entra
# UMA vez, nao vinte: repetir o exemplo dado e' o que ele chamou de maritaca.
# ⛔⛔ REESCRITO EM 2026-08-04 — A PRIMEIRA SENTENCA PASSA A CARREGAR O ORGAO.
#
# O operador leu o TAKE 02 renderizado e parou tudo:
#
#     "I read every forum there is and found nothing"
#     telespectador: "read WHAT? WTF? What the hell is she talking about?"
#
# ⛔ O DEFEITO: a fala abria com uma BUSCA sem OBJETO. O espectador chega no
# meio do scroll, ouve a primeira sentenca antes de qualquer outra, e ela nao
# dizia procurando O QUE. O orgao so' aparecia na TERCEIRA sentenca — tarde
# demais para quem decide em dois segundos se fica.
#
# ⚠️⚠️ E A MEDICAO DESMENTIU A MINHA PROPRIA DESCULPA. A hipotese era encaixe
# matematico — copy curta para caber nos 8s. Medido no parque: 64,2% das
# primeiras sentencas do ESCANDALO eram orfas, e a folga media nessas falas era
# de **+3,1 palavras**. O espaco existia. Nao foi o teto que me obrigou.
# Detalhe da causa raiz em `licoes-de-construcao.md` §21.
#
# ⭐ A REGRA QUE FICA: a PRIMEIRA sentenca da cena 2 nomeia o orgao. Cobrada
# pelo linter (ES22), com o caso do operador como controle.
FUNDIDAS = [
    "I went looking for anything that would fix his {o} and found nothing. The gelatin trick did it — {r}, real collagen, pennies.",
    "Two years of pills and nothing moved his {o}. Then the gelatin trick — {r}, vasodilators, four dollars — and he was back.",
    "Every doctor we saw had nothing for his {o}. The gelatin trick was {r} and honest collagen, and it worked inside a week.",
    "I read every forum there is looking for something for his {o} and found nothing. Then the gelatin trick: {r}, oxygen, pennies.",
    "Nobody could tell us what was wrong with his {o}. A nurse named the gelatin trick — {r}, vasodilators, four dollars — and it changed.",
    "The pharmacy had a shelf for his {o} and nothing on it that worked. The gelatin trick is {r} and cheap collagen.",
    "We spent a fortune and never got his {o} back. The gelatin trick did it for {r} and small change — real circulation.",
    "Three specialists, never a straight answer about his {o}. A woman in a comment section gave me the gelatin trick — {r}, real circulation.",
    "The pills did nothing for his {o} and neither did the patches. The gelatin trick is {r}, straight collagen, next to free.",
    "I looked for two years for something that would wake his {o} up. Nothing did. Then the gelatin trick — {r}, oxygen, pennies.",
    "His doctor had nothing left to offer for his {o}. My sister-in-law handed me the gelatin trick — {r}, pure collagen, small change.",
    "He would never talk to a doctor about his {o}. A man at his shop gave him the gelatin trick — {r}, oxygen, a few dollars.",
    "Months of looking and nothing changed for his {o}. Then the gelatin trick: cheap {r}, plain collagen, and it came back.",
    "I never thought a kitchen would do anything for his {o}. The gelatin trick did — {r} for pocket change, real circulation.",
    "We had stopped trying anything for his {o}. Nothing we bought did a thing. The gelatin trick is {r}, vasodilators, four dollars.",
    "He had given up on his {o}. I didn't. I found the gelatin trick — {r}, nitric oxide, the cheapest thing in the house.",
    "Nothing on that pharmacy shelf did a thing for his {o}. The gelatin trick is {r} and honest collagen, and it brought him back.",
    "Every website sold him something for his {o}. Nobody sells the gelatin trick — it is {r}, circulation, and a few dollars.",
    "The expensive things did nothing for his {o}. The cheap one worked: the gelatin trick, {r}, vasodilators, less than a coffee.",
    "Two hundred dollars a month and his {o} never moved. The gelatin trick is {r} and collagen and small change, and it did.",
    "I did not find this in a clinic and nobody made a cent off his {o}. The gelatin trick, {r}, nitric oxide, and it works.",
    "The famous ones did nothing for his {o}. The gelatin trick is not famous — {r}, cheap collagen — and it got him standing again.",
]

# O selo curto que fecha a fundida e cobra o PISO de 26 da cena 2.
# ⚠️ O motor re-sorteia se o selo ecoar um FATO ja' dito na fundida (`two
# dollars`, `three weeks`): 24 segundos nao comportam pagar o mesmo fato duas
# vezes (ES20).
SELOS = [
    "Two dollars a box.",
    "Same glass, every time.",
    "There is one step I left out.",
    "No pills anywhere near it.",
    "The amounts are the whole trick.",
    "I did not say the amounts.",
    "One glass, last thing at night.",
    "I watched him do it.",
    "He didn't believe it either.",
    "Cheapest thing in the kitchen.",
    "No filter on this one.",
    "That's the whole difference.",
    # + 2026-08-02: ampliacao de variancia por ordem do operador.
    # Verificacao adversarial reprovou 32 de 54 propostas; estas
    # sobreviveram e foram medidas em 2800 sorteios.
    "I stopped buying anything else.",
]

# ---------------------------------------------------------------------------
# COPY — cena 3: A PROVA + CTA (prova + cta + gate)
# ---------------------------------------------------------------------------
# ⭐ ORDEM DO ED, 2026-08-01: a cena 3 abre com PROVA, nao com barreira. "O take
# onde o homem finalmente aparece segurando a evidencia gastava a primeira frase
# falando de preco e de prateleira de supermercado."
# ⚠️ E a segunda ordem, que e' o que fecha: "faltou referenciar o falico". ⛔
# TODAS as provas trazem `{o}` — sem ele a prova nao tem referente: ela diz que
# algo mudou e nao diz o que.
# ⛔ Zero deixis a pessoa (`Look at him`, `That's him`): a relacao ja' esta'
# NOMEADA no IMAGE 03, e deixis reprova o teste do radio.
# ⚠️ `voz`: `intima` exige relacao de parceria (que e' o default deste agente);
# `terceiro` roda com qualquer relacao, e e' o que sobra se o Ed reabrir o pool
# de RELACOES. O motor FILTRA — nao se reescreve pool.
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
    # 2026-08-03 — QUEIXA DO OPERADOR lendo o app: "My sister asked what
    # changed. His old boy." -> "His old boy o QUE?" / "O que mudou?". Duas
    # doencas na mesma entrada: [C] a frase abria a pergunta e a fala acabava
    # sem responder, e [F] `His {o}.` e' sintagma nominal solto, sem verbo
    # finito. REGRA NOVA: se a frase abre a pergunta, a proxima RESPONDE, e
    # responde com VERBO DE RESULTADO dito como um homem diria (`gets it hard
    # again`), nunca com verbo de encanamento. ⛔ Toda frase precisa de verbo
    # finito. E `what changed` sai INTEIRO da fala: manter a pergunta e
    # responder logo depois ainda gasta 2 palavras para adiar o beneficio — o
    # que ele quer ouvir e' o resultado, nao a pergunta sobre ele.
    # Custo: 7 -> 10 palavras, dentro do teto 26 da cena 3.
    {"voz": "terceiro", "txt": "My sister asked. I said his {o} gets hard again."},
    {"voz": "terceiro", "txt": "His {o} quit waiting on him."},
    {"voz": "terceiro", "txt": "His {o} stopped apologizing. So did he."},
    {"voz": "terceiro", "txt": "Nineteen days later his {o} doesn't quit."},
    {"voz": "intima", "txt": "His {o} turns the lamp back on."},
    {"voz": "intima", "txt": "His {o} runs the schedule now."},
    {"voz": "terceiro", "txt": "Sixty-two, and his {o} acts thirty."},
    # + 2026-08-02: ampliacao de variancia por ordem do operador.
    # Verificacao adversarial reprovou 32 de 54 propostas; estas
    # sobreviveram e foram medidas em 2800 sorteios.
    {"voz": "intima", "txt": "I said goodnight. His {o} disagreed."},
    {"voz": "terceiro", "txt": "His {o} works harder than the truck."},
    # 2026-08-03 — mesma queixa, mesma familia [F]: `His {o}.` sozinho nao diz
    # o que o orgao TEM nem o que ele FAZ. O predicado entra com verbo de
    # resultado do registro da casa (`gets him standing again`), e a piada do
    # filme fica de pe' sozinha: o filme nao acaba porque ele levanta antes.
    # ⛔ NAO se troca `open` por outro eufemismo de encanamento — trocar
    # metafora por metafora nao conserta nada (§17 das licoes).
    # Custo: 7 -> 10 palavras, dentro do teto 26 da cena 3.
    {"voz": "intima", "txt": "I don't finish movies anymore. His {o} stands up first."},
    {"voz": "intima", "txt": "Two in the morning. His {o} again."},
    {"voz": "terceiro", "txt": "The whole street knows about his {o} now."},
    {"voz": "terceiro", "txt": "At midnight his {o} is the one still awake."},
]

# ⛔ ES12 — keyword travada em `gelatin`, MINUSCULA e SEGUIDA DE VIRGULA dentro
# do Dialogue: duas falhas pagas — `GLATN` (caixa alta faz o Veo soletrar) e
# `gelatine` (sem a micro-pausa o TTS emenda).
# ⛔ `book`, `yes`, `link` proibidos: `book` quebra a automacao Comentario->DM e
# e' literalmente a palavra do reel de 82K [D5].
# ⚠️ ENTROPIA DE FORMA, nao so' de contagem: 5 das 16 (#5, #7, #9, #13, #15)
# levam a keyword FORA da posicao inicial, senao o --stats conta 16 e a variacao
# percebida e' 3. (O comentario dizia 6; medido, sao 5 — 2026-08-02.)
CTAS = [
    "Comment gelatin, and I'll send you the whole recipe.",
    "Comment gelatin, and the recipe's on your phone tonight.",
    "Comment gelatin, and I'll send you the amounts.",
    "Comment gelatin, and I'll tell you how much of each.",
    "Comment gelatin, one word, and the recipe is yours.",
    "Comment gelatin, and I'll send the recipe step I left out.",
    "Comment gelatin, and the recipe goes out tonight.",
    "Comment gelatin, and I'll send the amounts for the recipe.",
    "Comment gelatin, and I'll send the recipe tonight.",
    # ⛔ AQUI HAVIA UMA SEGUNDA COPIA de "and the recipe goes out tonight."
    # (2026-08-08). Ela ja' esta' quatro linhas acima. Duplicata nao quebra
    # nada — por isso e' cara: dobra a chance daquela entrada e ocupa um slot
    # que devia ser repertorio novo. O sintoma so' aparece no LOTE.
    "Comment gelatin, and I'll send the recipe before you scroll.",
    "Comment gelatin, and I'll send the amounts written out.",
    "Comment gelatin, and I'll send the recipe written out.",
    "Comment gelatin, and I'll send where to buy the collagen.",
    "Comment gelatin, nothing else, and I'll send the recipe.",
    "Comment gelatin, and the whole recipe comes to you.",
    # + 2026-08-02: ampliacao de variancia por ordem do operador.
    # Verificacao adversarial reprovou 32 de 54 propostas; estas
    # sobreviveram e foram medidas em 2800 sorteios.
    "Comment gelatin, and I'll send the recipe nobody posts.",
]

# ⛔ ES19 — REGRA DE POOL, medida pelo operador no TROCA: "brother" caia em
# 31-73% dos videos. EXATAMENTE DUAS entradas com "brother", tres com vocativo
# no total, e 12 de 15 sem vocativo nenhum.
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
    "Tap follow, or it gets eaten.",
    "Follow me, brother. That's the gate.",
]

VOCATIVOS = ("brother", "my friend", "guys", "buddy", "man", "girls")

# ⚠️ POOL PARADO, NAO APAGADO (precedente do TROCA). Copy validada de tratamento
# de objecao. NAO entra na montagem default: a cena 3 tem 26 palavras e a ordem
# do Ed de 2026-08-01 foi trocar a barreira de abertura por PROVA. Fica aqui
# porque a decisao de traze-la de volta e' dele (alcada) — se voltar, e' como
# quarto beat de outra cena, nunca empurrando a prova.
BARREIRAS = [
    "Two dollars at any store.",
    "Nobody in your house knows.",
    "No prescription, no doctor, no waiting.",
    "It's in the baking aisle.",
    "Thirty seconds at the sink.",
    "You already own the glass.",
    "No pills, no appointment, no questions.",
    "Cheaper than one refill.",
    "He never knew I started it.",
    "Bottom shelf, about four dollars.",
    "Nothing to swallow but water.",
    "No one has to know.",
]


# ---------------------------------------------------------------------------
# TABELAS DE TOKEN BANIDO (o linter compartilhado le' estas)
# ---------------------------------------------------------------------------
# ⚠️ Direcao de cena, nunca fala. A fala DIZ a promessa, e a promessa e' o
# produto. O que nao pode e' a DIRECAO mandar o prop crescer: neste angulo nada
# cresce em quadro (ES2), e quem entrega a promessa sao as CARAS (ES1).
# ⚠️ `stiff`, `limp`, `sags` e `swelling` entraram em 2026-08-02: a ES2 os lista
# NOMINALMENTE ("zero `stiff`/`limp`/`sags`/`grows`/`pulse`/`swelling`") e a
# tabela so' cobria as formas conjugadas. Regra escrita na doutrina e ausente da
# tabela e' regra que a proxima edicao de pool quebra em silencio.
BANIDOS_TAKE = {
    "stiffens": "estado mudando no TAKE — ES2: nada cresce neste angulo",
    "swells": "idem", "grows": "idem", "rises": "idem",
    "expands": "idem", "doubles": "idem", "lengthens": "idem",
    "stiff": "adjetivo de estado — ES2 lista nominalmente",
    "limp": "idem", "sags": "idem", "swelling": "idem",
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
    "morph": "ES2: nada se transforma em quadro",
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

# ⛔ O guardrail de figurino: a divergencia do UN1 e' de PECA DESCRITA, nunca de
# vocabulario de desejo. Os pools estao limpos hoje; a tabela existe para a
# proxima edicao de pool.
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


_UNI = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen"]
_DEZ = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty",
        7: "seventy", 8: "eighty", 9: "ninety"}


def _por_extenso(n):
    """Numero escrito, nunca concatenado.

    ⚠️ Ja' saiu "Sixty-1 years old" e "Thirty-4" em producao por concatenar
    prefixo com algarismo. Numero na copy se ESCREVE (ES10).
    """
    if n < 20:
        return _UNI[n]
    d, u = divmod(n, 10)
    return _DEZ[d] + ("-" + _UNI[u] if u else "")


def _sem_artigo(txt):
    """Tira o artigo inicial de um item de pool.

    A travada diz "The %s has been standing on the ..." e os itens do pool
    nascem com artigo proprio. O motor ajusta o SLOT; ⛔ a travada nao se
    reescreve.
    """
    for art in ("the ", "a ", "an "):
        if txt.lower().startswith(art):
            return txt[len(art):]
    return txt


def _maiuscula(txt):
    return txt[0].upper() + txt[1:] if txt else txt


def _inicio_de_frase(txt):
    """Caixa alta no comeco da fala e depois de cada ponto final.

    ⚠️ Existe por causa do slot `{r}`: 8 das 16 FUNDIDAS o poem no comeco de uma
    frase, e a `Dialogue:` saia `"Watch. ginger in, warm water on top..."` e
    `"cinnamon, warm water, stirred..."` — texto que o TTS le' igual, mas que o
    operador le' como descuido no bloco que ele revisa antes de gerar.
    ⛔ So' na CENA 2. A keyword `gelatin,` da cena 3 e' minuscula por regra paga
    (ES12) e nunca cai depois de ponto nos pools de hoje — mas nao se roda uma
    normalizacao de caixa por cima dela sem necessidade.
    """
    return re.sub(r"(^|[.!?]\s+)([a-z])",
                  lambda m: m.group(1) + m.group(2).upper(), txt)


def _peca(calca):
    """A peca de roupa NUA, sem oracao subordinada.

    Hoje as 28 calcas ja' nascem nuas, entao isto e' GUARDA, nao transformacao:
    se alguem acrescentar 'khaki shorts with a deep side pocket' a um pool, a
    travada da F12b nao sai como 'centred against the front of his khaki shorts
    with a deep side pocket'. ⛔ A coordenada e' a FRENTE da peca, e nao se troca
    por bolso — bolso joga o prop no quadril e AMPUTA a cena (ES4).
    """
    return calca.split(" with ")[0]


# ES4 — a relacao NOMEADA e' a alavanca 2 do protocolo de recusa, e e'
# obrigatoria aqui. ⛔ Omitir nao e' opcao; `the victim`/`the narrator` sao
# proibidos.
# ⚠️ O numero se CALCULA (uniao a partir dos 20 anos do mais novo): com
# narradora >= 28 e homem >= 55 a conta sempre fecha em >= 8 anos, entao nao
# existe o ramo "sem numero" que o TROCA precisava.
# ⚠️ POOL PARCEIRA-ONLY por construcao — ver docstring, ponto 2 de alcada.
# ⛔ `his daughter-in-law` esta' fora: injeta leitura sexual intrafamiliar
# exatamente na geometria que ja' custou 4 recusas deterministicas.
def _relacao(rng, idade_m, idade_h):
    anos = min(idade_m, idade_h) - 20
    # peso 2 na esposa: e' a formulacao do operador e e' a que carrega mais
    # vinculo — que e' precisamente o que a alavanca 2 compra.
    op = ["his wife of %s years" % _por_extenso(anos)] * 2
    op.append("his partner of %s years" % _por_extenso(anos))
    op.append("the woman he has been with for %s years" % _por_extenso(anos))
    return rng.choice(op)


# a familia de voz que cada relacao autoriza nas PROVAS da cena 3.
VOZES_INTIMAS = ("his wife of", "his partner of", "the woman he has been with")


def voz_da_relacao(relacao):
    return "intima" if relacao.startswith(VOZES_INTIMAS) else "terceiro"


def _carregar_ledger():
    if os.path.exists(LEDGER):
        with open(LEDGER, encoding="utf-8-sig") as f:
            return json.load(f)
    return {}


# ES21 — os eixos que o ledger rotaciona. ROSTO evita os 3 ultimos (rosto
# repetido e' o que o operador ve' primeiro no lote); os demais evitam os 2.
EIXOS_LEDGER = ("narradora", "homem", "reacao", "par", "receita", "fisica",
                "cenario", "bancada", "mecanismo")


def _anotar(ledger, spec):
    """Anota o sorteio no ledger EM MEMORIA, sem tocar no arquivo.

    ⚠️ Existe separado do `_gravar_ledger` por causa do `--dry-run`: sem isto os
    N videos de um mesmo lote sao sorteados todos contra o mesmo historico e o
    `_evitando()` nao ve' o irmao que acabou de sair — `--n 2` devolvia a mesma
    narradora nos dois. O ensaio nao grava, mas tem de se lembrar de si.
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
    livres = [x for x in pool
              if (x.get("id") if isinstance(x, dict) else x) not in recentes]
    return rng.choice(livres if livres else pool)


def _cita(corpo, cabeca):
    """A palavra-cabeca aparece na copy? (singular ou plural — 'fig' tem de
    pegar 'figs')."""
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

    Serve para dizer se dois itens de cenario desenham O MESMO OBJETO — recibo
    que repete o pote da receita mostra dois ingredientes, nao quatro (ES8).
    """
    p = [w for w in _PALAVRA_CHEIA.findall(txt.lower()) if w not in _VAZIAS]
    return set(zip(p, p[1:]))


def _bancada_livre(rng, falas, recentes, receita=None):
    """ES8 — O RECIBO E' MUDO **E NAO REPETE A RECEITA**, por construcao em vez
    de checado depois.

    Tres colisoes, nao uma:
    · com a FALA — com receita=ginger a boca diz "ginger" na cena 2, e as duas
      bancadas de gengibre poriam na imagem justamente o que a fala ja' citou. O
      "full recipe" so' tem lastro se a boca citar UM e a imagem mostrar TRES.
    · com as CABECAS da receita — mesma coisa, medida pelo campo em vez do texto.
    · com a IMAGEM da receita — recibo que desenha o mesmo objeto do copo mostra
      dois ingredientes, nao quatro.
    """
    corpo = " ".join(falas)
    livres = [b for b in BANCADAS
              if not any(_cita(corpo, c) for c in b["cabecas"])]
    if receita:
        cab_r = set(receita["cabecas"])
        livres = [b for b in livres if not (set(b["cabecas"]) & cab_r)] or livres
        img = _pares(receita["img"])
        sem_eco = [b for b in livres if not (_pares(b["itens"]) & img)]
        livres = sem_eco or livres
    return _evitando(rng, livres if livres else BANCADAS, recentes)


# ES20 — ecos de FATO dentro do mesmo VIDEO (nao so' dentro da cena): a fundida
# que diz "three weeks" e a prova "Three weeks in, ..." estao em cenas
# diferentes e mesmo assim pagam o mesmo fato duas vezes em 24 segundos.
ECOS = ("two dollars", "nineteen days", "three weeks", "four dollars")


def _eco(*partes):
    corpo = " ".join(partes).lower()
    return any(corpo.count(e) > 1 for e in ECOS)


# ⛔ ES20b — DOIS PRECOS DIFERENTES NA MESMA RESPIRACAO (2026-08-04).
# O `_eco` acima so' pega o MESMO fato repetido. As FUNDIDAS novas trazem preco
# dentro da propria fala (`a dollar of {r}`, `four dollars`, `pennies`) e o pool
# de SELOS tem `Two dollars a box.` — o sorteio solto devolvia
# *"...a dollar of garlic... Two dollars a box."*, dois precos diferentes para a
# mesma coisa em oito segundos. Achado LENDO a saida renderizada (§19), nao pelo
# linter: nenhum fato se REPETIA, entao o `_eco` passava limpo.
# ⚠️ So' AMOUNT conta. Varrer `cheap`/`cheapest` esvaziaria o pool de selos e
# reprovaria copy que esta' certa — a regra e' sobre CIFRA, nao sobre barateza.
_PRECO = re.compile(
    r"\b(?:a|one|two|three|four|five|six|ten|twenty|fifty|a few|"
    r"two hundred|a couple of)\s+(?:hundred\s+)?dollars?\b"
    r"|\bpennies\b|\b(?:pocket|small)\s+change\b|\bnext to free\b"
    r"|\bless than a coffee\b", re.I)


def _precos(*partes):
    """As cifras distintas ditas nas partes."""
    return {m.group(0).lower() for m in _PRECO.finditer(" ".join(partes))}


def _preco_novo(fund, selo):
    """O SELO acrescenta uma cifra que a fundida ja' nao tinha?

    ⛔⛔ A REGRA E' SOBRE O SELO, NUNCA SOBRE A FUNDIDA — e a primeira versao
    errou exatamente isso, do jeito da §16 ("regra larga demais"). Ela contava
    as cifras da fala inteira e reprovava
    *"Two hundred dollars a month and nothing to show... small change"* — que
    tem duas cifras DE PROPOSITO: o contraste caro/barato e' o argumento da
    entrada, nao um descuido. Quem escreveu a fundida escolheu suas cifras; o
    que o sorteio nao pode e' colar uma TERCEIRA por cima.
    """
    return bool(_precos(fund)) and bool(_precos(selo) - _precos(fund))


# P22 — "cada cena aterrissa em 2a pessoa OU IMPERATIVO" (checklist da
# doutrina). O imperativo conta: `Watch what my hands do.` fala com o espectador
# tanto quanto `your {o}`.
P22_2A = re.compile(r"\b(you|your|you're|you'll|yours)\b", re.I)
# ⛔ So' VERBOS. Uma versao anterior desta lista tinha "one", "no" e "spoon"
# dentro dela para calar o AVISO da P22 em algumas combinacoes — isso nao e'
# cobrar a regra, e' fraudar o medidor. Se a cena nao aterrissa, o operador tem
# de ver.
IMPERATIVOS = ("watch", "listen", "keep", "give", "stay", "do", "start", "put",
               "want", "look", "hit", "tap", "follow", "comment", "type", "say",
               "skip", "grab", "take", "stop", "stir", "forget", "drop")


def _aterrissa(fala):
    if P22_2A.search(fala):
        return True
    for frase in re.split(r"[.!?:]\s*|\s+—\s+", fala):
        p = re.findall(r"[A-Za-z']+", frase)
        if p and p[0].lower() in IMPERATIVOS:
            return True
    return False


def _escolher(rng, pool, ok, tentativas=12):
    """Sorteia do pool ate' `ok(item)`; se nao achar por sorteio, VARRE.

    ⚠️ A varredura no fim e' a diferenca em relacao ao helper do TROCA, e ela
    existe por causa do PISO: as bordas do orcamento sao estreitas (a cena 3
    fecha em 20 palavras exatas em parte das combinacoes), e devolver "o ultimo
    sorteado" nessas bordas e' o mesmo que nao cobrar o piso. Se existe solucao,
    esta funcao a encontra; se nao existe, devolve o ultimo e o linter acusa.
    """
    esc = rng.choice(pool)
    for _ in range(tentativas):
        if ok(esc):
            return esc
        esc = rng.choice(pool)
    livres = [x for x in pool if ok(x)]
    return rng.choice(livres) if livres else esc


# ---------------------------------------------------------------------------
# SORTEIO
# ---------------------------------------------------------------------------

# ⛔⛔ O DRIFTING MAIS CARO DESTE AGENTE, medido em 1.200 sorteios: 100% dos
# videos. A cena 1 fala em SEGUNDA pessoa — "your {o}", "guys", "you" — e a
# cena 2 abre em TERCEIRA sobre um homem especifico: "He would never talk to a
# doctor", "His doctor had nothing left", "We spent a fortune and never got his
# {o} back". Quem entra no video pelo scroll ouve "he" e nao tem em quem
# pendurar: as 22 FUNDIDAS e as 22 PROVAS falam de um homem que o AUDIO nunca
# apresenta.
#
# ⚠️ E o motor JA' SABIA quem ele e': a `relacao` ("his wife of thirty years")
# e' sorteada e entra no IMAGE, onde e' a alavanca 2 do protocolo de recusa. Ou
# seja — o GERADOR sabia de quem se falava; o ESPECTADOR nunca.
#
# A correcao nomeia o homem UMA vez, na primeira mencao da cena 2, com o termo
# que a relacao ja' autoriza. Depois dela, todo "he/his/we" tem dono.
# ⛔ Nao inventa relacao nova: le' a que foi sorteada. Contradizer a relacao na
# fala e' ANULA-LA, e a relacao anulada custa a alavanca de moderacao (ES4).
_TRATAMENTO = (
    ("his wife of", "my husband"),
    ("his partner of", "my partner"),
    ("the woman he has been with", "my man"),
)

# ⛔⛔ FRONTEIRA DE PALAVRA, e a constante mora AQUI de proposito: este `\b`
# ja' virou BACKSPACE (0x08) ao passar por um heredoc, a regex ficou muda, a
# nomeacao parou de acontecer EM SILENCIO e so' o gate de contexto viu.
# ⚠️ Sem a fronteira, `find("his ")` casava dentro de "this " e cuspia
# *"I did not find tmy husband's in a clinic"* em 9 de 1.200 sorteios.
_PRIMEIRO_MASC = re.compile(r"\b(his|him)\b")


def _nomeia_o_homem(txt, relacao):
    """Troca a PRIMEIRA mencao masculina da cena 2 pelo termo da relacao."""
    termo = next((t for pref, t in _TRATAMENTO if relacao.startswith(pref)),
                 "my husband")
    if txt.startswith("He "):
        return termo[0].upper() + termo[1:] + txt[2:]
    m = _PRIMEIRO_MASC.search(txt)
    if not m:
        return txt
    # `him something` -> `my husband something` (objeto, sem genitivo)
    if m.group(1).lower() == "him":
        return txt[:m.start(1)] + termo + txt[m.end(1):]
    # `his {o}` -> `my husband's {o}`; `his doctor` -> `my husband's doctor`
    return txt[:m.start(1)] + termo + "'s" + txt[m.end(1):]


# ---------------------------------------------------------------------------
# ⭐⭐ A FALA DA CENA FUNDIDA — EIXOS COMPOSTOS (2026-08-08)
# ---------------------------------------------------------------------------
# Forma A, aprovada pelo operador:
#     {RECEITA com o gelatin trick} {PROVA no marido} {CTA} {GATE}
#
# ⛔ Os pools de 24s nao serviam: FUNDIDA (21-25) + SELO (4-7) da' 25 no MINIMO
# contra teto fisico 25, e somado a cena 3 da' 39. O motor de 24s vivia na lista
# dos que cortam fala por isso, com PISO 26 declarado acima do proprio teto.
#
# ⛔⛔ AS ORDENS DO OPERADOR QUE GOVERNAM ESTES POOLS, todas de 2026-08-08:
#   1. *"nao use pronome, seja taxativo e claro"* — as 22 entradas de PROVAS do
#      motor de 24s abrem com `His {o}`: o orgao esta' nomeado, o DONO nao. Aqui
#      e' `My husband's {o}` — a narradora fala em primeira pessoa nas duas
#      cenas, entao ela diz de quem.
#   2. *"seja mais taxativo: I'll send recipe ou I'll send the complete
#      recipe"* — TODA entrada de CTAS16 nomeia `recipe`. Quatro das dezesseis
#      CTAs de 24s prometiam `the amounts` / `how much of each`, e `amounts` de
#      QUE e' a mesma duvida que ele reprovou no FALTA 16.
#   3. *"muito vaga e ocupando tempo precioso"* — nenhum beat abstrato. Cada um
#      nomeia coisa: o ingrediente sorteado, o colageno, o marido, o orgao.

# ⚠️ 5-8 palavras. `{r}` e' o ingrediente SORTEADO (pool RECEITAS, 16 entradas
# de 1-2 palavras), entao a variacao real e' 8 x 16.
# ⛔ O literal `gelatin trick` mora AQUI e e' obrigatorio: era a cena 2 que o
# trazia, e ela e' justamente a que caiu.
# ⚠️ 5-8 palavras, e ela e' a PRIMEIRA sentenca do take — a que decide se o
# espectador fica. Tem de cumprir DUAS lentes do angulo de uma vez:
#   · ES22 — nomear o ORGAO na abertura (o teste WTF, licoes §21);
#   · ES6  — trazer o marcador de NEGACAO antes do batismo do mecanismo.
# ⛔ E cumpre a ordem do operador: `my husband's`, nunca `his` solto.
# ⭐ E' o arco da propria fonte, comprimido: *"Months of looking and nothing
# changed for my husband's Johnson. Then the gelatin trick..."*
# ⛔⛔ POOLS PARADOS EM 2026-08-10 — os dois beats fundiram em MECANISMOS16.
# Motivo MEDIDO, 200 sorteios, contrato de copy 16s:
#   · CT5 em 100% — as oito RECEITAS16 entregam DOIS ingredientes de graca
#     (`{r}` sorteado + `collagen`) ANTES do pedido. E o dano nao e' de um
#     video: a receita e' a UNICA moeda que o comentario compra, e entregue
#     uma vez na pagina ela esta' gasta para os outros 49 que pedem a mesma
#     palavra pela mesma receita.
#   · CT3 em 100% — `The gelatin trick: {r} and collagen.` e' ROTULO NU. Diz o
#     nome do mecanismo e nao diz o que ele FAZ, entao nao ha' no que
#     acreditar: vira ruido de marca.
# ⚠️ PARADOS, NAO APAGADOS. Se o Ed decidir um dia que a pagina pode gastar a
# moeda, eles voltam com uma linha.
ABERTURAS16 = [
    "Nothing worked on my husband's {o}.",
    "Nothing worked for my husband's {o}.",
    "Nothing moved my husband's {o}.",
    "Nothing touched my husband's {o} for years.",
    "Nobody had an answer for my husband's {o}.",
    "Nothing helped my husband's {o} in years.",
    "Nothing reached my husband's {o}.",
    "Nobody fixed my husband's {o}.",
]

RECEITAS16 = [
    "The gelatin trick: {r} and collagen.",
    "The gelatin trick is {r} and plain collagen.",
    "The gelatin trick: {r}, collagen, warm water.",
    "The gelatin trick is {r} with plain collagen.",
    "The gelatin trick: cheap {r} and collagen.",
    "The gelatin trick adds {r} to plain collagen.",
    "The gelatin trick: plain collagen and {r}.",
    "The gelatin trick is collagen and {r}, nothing else.",
]


# ---------------------------------------------------------------------------
# ⭐⭐ CT3 — O MECANISMO COM RAZAO, a primeira sentenca do take 2 (2026-08-10)
# ---------------------------------------------------------------------------
# UMA sentenca que carrega, de uma vez, as cinco coisas que este slot deve:
#   1. o literal `gelatin trick` (ES6, congruencia com a VSL — inviolavel);
#   2. um VERBO DE EFEITO (CT3) — `feeds`, `puts`, `keeps`, `fills`, `carries`;
#   3. o ALVO (CT3) — o orgao, nomeado, nunca `blood flow` solto (§17: causa
#      nomeada sem dizer o que ela quebra);
#   4. o DONO (ordem do operador 2026-08-08, *"nao use pronome, seja taxativo"*)
#      — `{d}` e' `my husband's` / `my partner's` / `my man's`, DERIVADO da
#      relacao sorteada. ⛔ Nao e' mais cravado em `my husband's`: a relacao
#      nomeada no IMAGE 02 e' a alavanca 2 do protocolo de recusa, e a fala
#      dizer `my husband` sobre um IMAGE que diz `his partner of thirty years`
#      ANULA a relacao — que e' perder a alavanca (ES4);
#   5. EXATAMENTE UMA palavra tecnica (ES7) — e ⛔ `collagen` esta' fora por
#      construcao, porque o CT5 a bane como ingrediente; `vasodilators` saiu na
#      2a conferencia por nao sobreviver a uma audicao (motivo logo abaixo).
#      Sobram `circulation`, `oxygen` e `nitric oxide`, que sao FISIOLOGIA, nao
#      lista de compras: nao ha' como comprar `circulation` no mercado.
#
# ⛔ CT7 — nenhum verbo de ereccao encostado no orgao. `puts circulation back
# in {d} {o}` passa; `gets {d} {o} hard` reprova no gerador (~95% medido em
# campo no COLO 16). O que a frase promete e' CIRCULACAO, e o espectador faz a
# conta sozinho.
# ⚠️ 8-10 palavras, banda estreita de proposito. Em 25 palavras com quatro
# beats a folga total e' de 2 palavras: entrada de 12 nunca sairia, e pool com
# entrada morta e' pool que mente no --stats.
#
# ⛔ DERRUBADA NA LEITURA EM VOZ ALTA (2a conferencia, 2026-08-10):
#   · `The gelatin trick works like vasodilators on {d} {o}.` — `vasodilators`
#     e' a unica palavra do motor inteiro que um americano de 60 anos nao
#     decodifica DENTRO da sentenca: ela chega em ~1,2s, no meio do primeiro
#     beat do take 2, que e' onde ele decide se fica. Quem conhece a palavra a
#     conhece do FOLHETO DE UM REMEDIO, e ai' ela nao ajuda — encosta o
#     mecanismo caseiro na farmacia, que e' o vilao que este funil vende
#     contra. ⚠️ Ela passava as sete travas: nenhuma lente a acusa, e por isso
#     so' a audicao a pegou (§19). ⛔ `vasodilator` FICA em ES7_TECNICAS: a
#     lista e' de DETECCAO, e se alguem a reintroduzir eu quero as duas lentes
#     acusando. Sobram `circulation`, `oxygen` e `nitric oxide` — as tres sao
#     fisiologia que o proprio nicho ja' fala em anuncio, nao bula.
MECANISMOS16 = [
    "The gelatin trick feeds {d} {o} oxygen.",
    "The gelatin trick gives {d} {o} circulation.",
    "The gelatin trick fills {d} {o} with oxygen.",
    "The gelatin trick put circulation into {d} {o}.",
    "The gelatin trick pushes oxygen into {d} {o}.",
    "The gelatin trick carries oxygen to {d} {o}.",
    "The gelatin trick keeps circulation in {d} {o}.",
    "The gelatin trick restores circulation to {d} {o}.",
    "The gelatin trick holds oxygen in {d} {o}.",
    "The gelatin trick brings circulation back to {d} {o}.",
    "The gelatin trick moves oxygen back into {d} {o}.",
    "The gelatin trick feeds nitric oxide to {d} {o}.",
    "The gelatin trick fixed the circulation to {d} {o}.",
    "The gelatin trick clears the circulation to {d} {o}.",
    "The gelatin trick started circulation in {d} {o} again.",
    "Nothing but the gelatin trick feeds {d} {o} oxygen.",
    "Nothing but the gelatin trick gives {d} {o} circulation.",
]


# ---------------------------------------------------------------------------
# ⭐ A PROVA CURTA — o segundo beat do take 2 (2026-08-10)
# ---------------------------------------------------------------------------
# 4-5 palavras. E' a unica batida do video em que a mulher diz o que MUDOU na
# casa, e ela fala do HOMEM, nunca do orgao — de proposito:
# ⛔ CT7 — a prova e' o lugar natural do `stays hard` / `wakes up` / `comes
# back`, e e' exatamente onde eles reprovam. Sem o orgao na sentenca a lente
# nem precisa apertar: o dano ja' esta' fora por construcao.
# ⭐⭐ E ELA CARREGA A NEGACAO DA ES6, todas as 18. A ES6 exige o marcador de
# falta em volta do batismo do mecanismo, e no formato 16s a FALTA de verdade
# mora no take 1 (o CT2, a falha dele) — do outro lado do corte. O marcador
# dentro do take fica aqui, colado no mecanismo, sem gastar palavra propria.
# ⚠️ `he` aqui TEM dono: a sentenca anterior acabou de dizer `{d} {o}`. E' a
# diferenca entre anafora e drifting.
# ⚠️ TAMANHOS EQUILIBRADOS de proposito. Medido no pool de 2026-08-09 (3 de 4
# palavras contra 15 de 5): as tres curtas levavam 25% do lote, porque a prova
# e' o TERCEIRO beat a escolher e herda a sobra do mecanismo e do CTA — quando
# os dois saem longos, so' as curtas cabem. Pool torto no beat que escolhe por
# ultimo nao e' pool de 18, e' pool de 3 com quinze enfeites.
#
# ⛔⛔ CINCO ENTRADAS DERRUBADAS NA LEITURA EM VOZ ALTA (conferencia
# 2026-08-10). O criterio nao foi estilo: foi *o que um americano de 50-70 anos
# entende OUVINDO UMA VEZ*, e a prova e' a batida que tem 1,3 segundo para
# entrar. Nenhuma delas era acusada por lente nenhuma — todas passavam o
# contrato inteiro, e e' por isso que so' a leitura as pegou (§19).
#   · `I don't sleep anymore.` — a leitura literal e' INSONIA, e insonia e'
#     queixa, nao prova. A intencao (a casa passou a virar a noite) exige uma
#     inferencia que o ouvido nao faz em 1,3s, e ela poe a NARRADORA no lugar
#     do deficit. ⚠️ `Nobody sleeps in this house.` fica: o sujeito plural e a
#     casa entregam o casal, nao um sintoma de uma pessoa so'.
#   · `Nothing gets done before midnight.` — sem sujeito humano nenhum, a
#     primeira leitura e' TAREFA DE CASA / procrastinacao. Nao diz nada sobre
#     ele, e prova que nao fala do homem nao e' prova.
#   · `I never win that argument.` — `that argument` e' DEITICO SEM DONO: nao
#     ha' discussao nenhuma em lugar nenhum do video para o `that` apontar. E'
#     o modo de falha do pronome generico, com determinante no lugar do
#     pronome — o medidor de deiticos nao o pega porque a lista dele e' de
#     pronomes.
#   · `Nobody gets an early night.` — `an early night` e' britanismo; o
#     americano de 60 anos diz `turn in early`. E carrega a mesma ambiguidade
#     de insonia da primeira.
#   · `My husband doesn't quit now.` — ⛔ CONTRADIZ A RELACAO SORTEADA. Era a
#     UNICA entrada do pool que renomeia o dono, e ela o renomeia CRAVADO:
#     medido em 2.000 sorteios, 20 videos (1,0%) diziam
#     *"...circulation to my partner's soldier. My husband doesn't quit now."*
#     na mesma respiracao. Anular a relacao nomeada e' perder a alavanca 2 do
#     protocolo de recusa (ES4) — o mesmo defeito que o `_dono()` acabou de
#     consertar do outro lado. As doze entradas em `he`/`him` ja' cobrem o
#     slot, e nelas o dono vem da sentenca anterior, que e' anafora legitima.
#
# ⛔⛔ MAIS DUAS DERRUBADAS NA 2a CONFERENCIA (2026-08-10). O criterio aqui nao
# e' "vago" — e' AMBIGUO PARA O LADO ERRADO: as duas admitem uma leitura em que
# o homem esta' PIOR, e prova que pode ser lida como queixa nao e' prova.
#   · `He doesn't ask twice.` — a leitura pretendida e' *nao precisa pedir duas
#     vezes* (ela diz sim de primeira). A leitura literal e' *pede uma vez e
#     desiste* — que e' exatamente a FALHA do take 1 sobrevivendo ao gelatin
#     trick. Duas leituras opostas na mesma sentenca, e a errada e' a mais
#     curta de alcancar. ⚠️ `I don't refuse him anymore.` diz a leitura boa sem
#     charada e fica.
#   · `He never runs out.` — `run out` em ingles pede complemento (`run out OF
#     something`). Nua, a primeira leitura de um ouvido americano e' `run out
#     [the door]`, ou seja o homem SAINDO. `Nothing tires him out.` e `Nothing
#     wears him down anymore.` cobrem o mesmo sentido com o verbo completo.
# ⚠️ Pool de 11, contra piso 11 do MIN_COPY — este slot esta' NO limite, e a
# proxima derrubada exige reposicao pelo Ed. Registrado, nao contornado.
PROVAS16 = [
    "He doesn't quit anymore.",
    "Nothing stops him now.",
    "Nobody sleeps in this house.",
    "He doesn't wait now.",
    "Nothing tires him out.",
    "I don't refuse him anymore.",
    "He doesn't stop at midnight.",
    "Never a quiet night.",
    "He doesn't slow down.",
    "Nothing wears him down anymore.",
    "He doesn't need convincing now.",
]


# ---------------------------------------------------------------------------
# ⭐ O FOLLOW — terceiro beat, e ele vem ANTES do CTA (CT1, 2026-08-10)
# ---------------------------------------------------------------------------
# ⛔⛔ A INVERSAO E' O CONSERTO MAIS CARO DO CONTRATO: 100% dos sorteios deste
# motor terminavam o video num GATE (`The algorithm hides me from
# non-followers.`, `Followers get answered first.`, `No follow, no message.`)
# — ou seja, a ULTIMA coisa no ouvido, colada no unico pedido que gera receita,
# era uma EXPECTATIVA NEGATIVA sobre a entrega ou uma CONDICIONAL na
# recompensa. A posicao final e' a que fica, e ela tem de ser o pedido.
# ⭐ O follow nao morreu — mudou de lugar. E mudando de lugar ele tambem mudou
# de forma: la' no fim precisava ser AMEACA para segurar o ouvido; aqui, antes
# do pedido, basta ser INSTRUCAO. Tres palavras, imperativo, zero ameaca.
# ⚠️ TODAS com 3 palavras exatas — e' o beat mais intercambiavel do take, entao
# e' ele quem absorve a sobra do orcamento. Banda de tamanho zero significa que
# nenhuma entrada morre por aritmetica: as 16 alcancam.
# ⚠️ DUAS com vocativo (ES19: o operador mediu `brother` em 31-73% dos videos
# do TROCA e mandou variar — 2 de 16 mantem a textura sem virar bordao).
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
FOLLOWS16 = [
    "Follow me first.",
    "Tap follow first.",
    "Hit follow first.",
    "Follow, then comment.",
    "Follow me now.",
    "Tap follow now.",
    "Hit follow now.",
    "Follow me, brother.",
    "Follow first, brother.",
    "Follow me here.",
    "Follow me today.",
    "Follow me tonight.",
    "Follow before commenting.",
    "Tap follow here.",
    "Hit follow today.",
    "Follow this page.",
]


# ---------------------------------------------------------------------------
# ⭐⭐ O CTA — a ULTIMA sentenca do video, e ela diz ONDE a receita chega (CT6)
# ---------------------------------------------------------------------------
# ⛔⛔ A CONTA QUE FAZ A COBERTURA SOCIAL CABER. Ela nao cabe como batida
# propria em 25 palavras; mora DENTRO da sentenca do CTA, de graca:
#     antes:  Comment gelatin, and I'll send the recipe.            (9 palavras)
#     depois: Comment gelatin, and the recipe goes to your messages. (9 palavras)
# Mesmo custo, e entrega tres coisas que o pool antigo nao entregava: (a) o
# ENDERECO da entrega, (b) a PRIVACIDADE e (c) o fato de que nao e' na tela
# publica. O KPI deste funil e' uma CONFISSAO PUBLICA — o comentario leva nome
# e foto e vai para o feed da mulher dele —, e quanto melhor o diagnostico em
# 2a pessoa, MAIS CARO fica comentar. Em 48 segundos de copy revisada nao havia
# UMA palavra baixando esse custo.
# ⛔ O literal `Comment gelatin,` e' intocavel (a legenda do video nasce do
# Whisper em cima do audio gerado, e a automacao de DM casa palavra exata).
# ⛔ TODA entrada nomeia `recipe`: prometer `the amounts` sem dizer de que e' a
# duvida que o operador reprovou no FALTA 16.
# ⚠️ 8-9 palavras, metade em cada tamanho: quando o mecanismo sai com 10, so'
# as de 8 cabem — pool torto aqui viraria oito entradas mortas.
CTAS16 = [
    "Comment gelatin, and the recipe hits your inbox.",
    "Comment gelatin, and the recipe comes in private.",
    "Comment gelatin, and nobody else sees the recipe.",
    "Comment gelatin, and your inbox gets the recipe.",
    "Comment gelatin, and the recipe reaches your messages.",
    "Comment gelatin, and the recipe lands in private.",
    "Comment gelatin, and the recipe goes in private.",
    "Comment gelatin, and your messages get the recipe.",
    "Comment gelatin, and the recipe goes to your messages.",
    "Comment gelatin, and the recipe lands in your inbox.",
    "Comment gelatin, and the recipe waits in your messages.",
    "Comment gelatin, and I'll send the recipe in private.",
    "Comment gelatin, and the whole recipe reaches your inbox.",
    "Comment gelatin, and the recipe arrives in your messages.",
    "Comment gelatin, and I'll send the recipe by message.",
    "Comment gelatin, and the recipe sits in your inbox.",
]


# ⛔ O DONO DO ORGAO — derivado da RELACAO sorteada, nunca cravado.
# `his wife of N years` -> `my husband's`; `his partner of N years` ->
# `my partner's`; `the woman he has been with` -> `my man's`.
# ⚠️ As tres custam DUAS palavras exatas, entao a escolha nao mexe no orcamento
# do take — se custassem diferente, a relacao sorteada estaria decidindo em
# silencio quais mecanismos cabem.
def _abre(frase):
    """A primeira palavra da sentenca, em minusculas e sem pontuacao.

    ⚠️ Existe para o guarda de gagueira do take 2 (mecanismo -> prova). Nao
    reaproveita o `_eco`, que varre FATO repetido: aqui o que repete e' a
    PALAVRA DE ABERTURA, e ela nao e' fato nenhum.
    """
    m = re.search(r"[A-Za-z'\-]+", frase or "")
    return m.group(0).lower() if m else ""


def _dono(relacao):
    termo = next((t for pref, t in _TRATAMENTO if relacao.startswith(pref)),
                 "my husband")
    return termo + "'s"


def _montar_falas(rng, par, receita, orgaos, relacao, degrau):
    """As DUAS falas do 16s, montadas pelo contrato de copy (2026-08-10).

        TAKE 1   hook (degrau sorteavel) + A FALHA DELE, com dano concreto
        TAKE 2   mecanismo COM RAZAO -> prova curta -> follow -> CTA   <- FIM

    ⚠️ ES16: a compressao aqui e' de BEAT, nao de fala — a taxa de palavras da
    fonte e a nossa sao a MESMA (3,3-3,6 vs 3,4-4,0 p/s). Uma frase por cena
    deixaria ar num take de 8s, e ar vira pausa morta.

    Filtros por construcao, todos com varredura de fallback:
    · o DEGRAU do hook e' escolha do Ed (ES10), nao do sorteio
    · o PISO e o TETO por cena (ES16) — piso nao cobrado e' piso que nao existe
    · a P22 (2a pessoa ou imperativo) em cada cena
    · CT4 — UM apelido do orgao por video, o MESMO nos dois takes

    ⚠️ `receita` continua na assinatura e nao entra mais em fala nenhuma: o CT5
    tirou o ingrediente da boca. O eixo segue vivo na IMAGE/TAKE e no ledger —
    quem foi embora foi a MENCAO FALADA, nao o eixo.
    """

    hook_pool = [h for h in HOOKS if h["degrau"] == degrau] or HOOKS
    # ⛔ ES5 — o ESCAPE tem de ser mais seguro que o degrau de que se escapa.
    # Duas das cinco entradas do degrau 2 derivaram para a forma AFIRMATIVA
    # sobre o corpo do espectador ("Your {o} doing this four nights a week at
    # sixty."), que e' a familia do NECROSE — descer um degrau caia nelas em 40%
    # das vezes. O motor deixa de sortea-las e o linter reprova; a REESCRITA da
    # copy e' alcada do Ed, e ate' la' o pool efetivo do degrau 2 e' de 3.
    # ⛔ Zero efeito no degrau 1: os hooks de la' nomeiam os props, nunca dizem
    # `your <nucleo>`. A ordem [D3] passa intacta.
    seguros = [h for h in hook_pool
               if _afirma_no_corpo(h["txt"].format(e=par["fala_e"],
                                                   f=par["fala_f"],
                                                   o=orgaos[0])) is None]
    hook_pool = seguros or hook_pool

    # ⛔⛔ O HOOK ERA SORTEADO SEM ORCAMENTO NENHUM, e o VILAO tinha de absorver
    # sozinho o que sobrasse. Quando o hook saia longo, nenhum vilao satisfazia
    # o predicado abaixo e o `_escolher` caia no fallback — devolvia um vilao
    # qualquer e a cena 1 ia a 29 palavras, contra teto 25.
    # ⚠️ MEDIDO em 2026-08-08 pelo `medir_teto_fala --curva`: 7,2% dos sorteios
    # acima do teto fisico, ou seja FALA CORTADA no render, com o piso do motor
    # em 23 — o pool sabia falar curto, a cadeia e' que nao pedia.
    # ⭐ Mesmo conserto que tirou o TROCA da lista dos que cortam fala: o beat
    # sem restricao propria passa a ser escolhido DENTRO do orcamento, e o
    # criterio nao e' "o menor vilao cabe" e sim "existe vilao que satisfaz o
    # predicado INTEIRO" — piso, teto e a P22 do `_aterrissa`.
    # ⛔ NENHUMA PALAVRA MUDA: muda quais hooks entram no sorteio.
    # ⭐ 2026-08-10: o beat que absorve deixou de ser o VILAO e passou a ser a
    # FALHA (CT2). A mecanica de orcamento e' a mesma, caractere por caractere.
    def _tem_falha(h):
        t = h["txt"].format(e=par["fala_e"], f=par["fala_f"], o=orgaos[0])
        return any(PISO_FALA[1]
                   <= _palavras("%s %s" % (t, x.format(o=orgaos[0])))
                   <= TETO_FALA[1]
                   and (_aterrissa(t) or _aterrissa(x))
                   for x in FALHAS)

    # ⚠️ `or hook_pool` porque lista vazia nao pode existir: antes de derrubar o
    # sorteio, o teto cede e quem reclama e' o linter — e' ele que tem de
    # aparecer, nao um IndexError.
    hook_pool = [h for h in hook_pool if _tem_falha(h)] or hook_pool
    hook = rng.choice(hook_pool)["txt"].format(e=par["fala_e"],
                                               f=par["fala_f"], o=orgaos[0])
    # ⭐⭐ CT2 — o segundo beat da cena 1 e' A FALHA DELE, com dano concreto.
    # Foi o FECHO ("Give me eight seconds" — atencao, sem motivo), depois o
    # VILAO OCULTO (motivo, sem dano), e agora e' o DANO. A escada e' a mesma
    # pergunta tres vezes: o que esta' faltando neste slot?
    #   · fecho ..... nao dizia nada sobre ele
    #   · vilao ..... dizia de quem e' a culpa, e nunca do que
    #   · falha ..... diz o que o corpo dele FAZ de errado, e um numero
    # MEDIDO antes da troca: 94% dos videos sem UMA sentenca de falha.
    # ⚠️ A falha carrega `{o}`: e' por ela que a cena 1 nomeia o orgao em 100%
    # dos sorteios, inclusive no degrau 1, cujos hooks nomeiam os PROPS.
    falha = _escolher(
        rng, FALHAS,
        lambda x: (PISO_FALA[1]
                   <= _palavras("%s %s" % (hook, x.format(o=orgaos[0])))
                   <= TETO_FALA[1]
                   and (_aterrissa(hook) or _aterrissa(x))))
    c1 = "%s %s" % (hook, falha.format(o=orgaos[0]))

    # ----- cena 2 — ⭐⭐ A FUNDIDA -------------------------------------------
    # ⛔⛔ CADA BEAT ORCA CONTRA O MINIMO DOS OUTROS, e o beat sem restricao
    # propria e' escolhido DENTRO do orcamento. Licao §36.
    # ⚠️ E o guarda de ECO continua: com quatro beats em oito segundos, repetir
    # substantivo le' como gagueira, nao como retomada.
    def _cabe16(pool, reserva, fmt):
        def _n(x):
            return _palavras(fmt(x))
        v = [x for x in pool if _n(x) + reserva <= TETO_FALA[2]]
        return v or [min(pool, key=_n)]

    # ⭐ O DONO sai da RELACAO sorteada — duas palavras, sempre, seja qual for.
    _d = _dono(relacao)
    # ⛔⛔ CT4 — O MESMO APELIDO NOS DOIS TAKES, e isto REVERTE a regra antiga.
    # Ate' 2026-08-09 o take 1 usava `orgaos[0]` e o take 2 usava `orgaos[1]`,
    # cumprindo o AVISO de "substantivo repetido no video" do `lint_curto`. O
    # resultado MEDIDO foi o apelido mudando no corte em 100% dos videos.
    # Em 24s e cinco cenas o bordao e' o risco; em 16s e DUAS cenas o risco e'
    # o oposto — o corte zera a memoria de trabalho, e trocar `soldier` por
    # `Johnson` no segundo 9 obriga o espectador a remapear no instante em que
    # ele ja' esta' com um pe' fora. A variacao continua existindo ENTRE
    # videos (`orgaos` sai de `rng.sample`), que e' onde ela nunca custou nada.
    _o = orgaos[0]
    _fm = lambda x: x.format(d=_d, o=_o)

    # ⛔⛔ A ORDEM DE ESCOLHA E' POR NUMERO DE SUBSTITUTOS, NAO PELA ORDEM EM
    # QUE AS FRASES SAEM DA BOCA. Quem escolhe primeiro e' quem tem menos
    # substitutos; o beat intercambiavel escolhe por ULTIMO e absorve a sobra.
    #   1º MECANISMO — carrega cinco exigencias de uma vez (literal, verbo,
    #      alvo, dono e a palavra tecnica da ES7). Nao ha' substituto.
    #   2º CTA ....... literal travado + isca + endereco de entrega (CT6).
    #   3º PROVA ..... 4-5 palavras, ampla.
    #   4º FOLLOW .... tres palavras, dezesseis formas de dizer a mesma coisa.
    #      E' ele quem absorve, e por isso todas as entradas tem o MESMO
    #      tamanho: banda zero significa que nenhuma morre por aritmetica.
    # ⚠️ Cada um reserva o MINIMO dos que ainda faltam — com folga total de 2
    # palavras em 25, reservar a mediana (a regra do pool anterior, onde a
    # folga era de 6) mataria as entradas longas do mecanismo e do CTA.
    _mn_m = min(_palavras(_fm(x)) for x in MECANISMOS16)
    _mn_p = min(_palavras(_fm(x)) for x in PROVAS16)
    _mn_f = min(_palavras(x) for x in FOLLOWS16)
    _mn_c = min(_palavras(x) for x in CTAS16)

    mec16 = _fm(rng.choice(_cabe16(MECANISMOS16, _mn_c + _mn_p + _mn_f, _fm)))
    cta16 = rng.choice(_cabe16(
        CTAS16, _palavras(mec16) + _mn_p + _mn_f, lambda x: x))
    # ⛔⛔ GAGUEIRA DE ABERTURA — achada LENDO a saida, nao por lente (§19).
    # Duas das dezoito MECANISMOS16 abrem em `Nothing but the gelatin trick...`
    # e cinco das PROVAS16 abrem em `Nothing`/`Nobody`. Sorteadas soltas, as
    # duas primeiras sentencas do take 2 saiam com a MESMA palavra de abertura
    # colada — *"Nothing but the gelatin trick gives my partner's soldier
    # circulation. Nothing tires him out."* — em 56 de 2.000 videos (2,8%).
    # Ouvido uma vez isso nao le' como paralelismo, le' como travada de fala,
    # e acontece nos 1,5s em que o espectador decide se o take 2 vale.
    # ⚠️ O `_eco` nao pega: ele varre FATO repetido, e `Nothing` nao e' fato.
    # ⚠️ E' filtro por CONSTRUCAO com fallback (`or`), como todos os outros
    # deste motor: se o orcamento apertar a ponto de so' sobrar prova com a
    # mesma abertura, o sorteio nao cai — quem reclama e' o linter.
    # ⛔ So' o par mecanismo->prova precisa do guarda: o FOLLOW abre em
    # `Follow`/`Tap`/`Hit` e o CTA abre em `Comment`, sempre, por construcao.
    _cab_p = _cabe16(PROVAS16, _palavras(mec16) + _palavras(cta16) + _mn_f, _fm)
    _cab_p = [x for x in _cab_p if _abre(_fm(x)) != _abre(mec16)] or _cab_p
    pro16 = _fm(rng.choice(_cab_p))
    _usado = _palavras(mec16) + _palavras(cta16) + _palavras(pro16)
    # ⛔⛔ CT8 (2026-08-10) — O BEAT DO FOLLOW SAIU DA FALA.
    # Ordem do operador: *"nao acho que deva ter follow me no cta, a
    # mensagem e' enviada independente de seguirem ou nao"*. O gate
    # existia no repo inteiro por uma PREMISSA ERRADA sobre a automacao
    # de DM, e quem opera a automacao corrigiu. As palavras liberadas
    # vao para o mecanismo e a prova.
    # ⛔⛔ CT1 — O CTA E' A ULTIMA COISA DO VIDEO. Nada depois dele, nunca.
    # A ordem falada e' mecanismo -> prova -> follow -> CTA, mesmo tendo o CTA
    # sido ESCOLHIDO em segundo: escolher e falar sao duas ordens diferentes.
    c2 = "%s %s %s" % (mec16, pro16, cta16)
    return [c1, c2]


def sortear(pagina, rng, ledger, travas=None, geometria=None,
            figurantes=None):
    """ES21 — anti-repeticao por ledger, por pagina.

    ⚠️ A assinatura tem de aceitar `sortear(pagina, rng, ledger)` com tres
    posicionais: e' assim que o `ui_agente.py` chama. Os tres modos caem no
    default ([D3]: degrau 1; ES2: separados; ES1: um figurante).

    ⚠️ A RELACAO E' SORTEADA ANTES DAS FALAS: a voz da PROVA da cena 3 depende
    dela, e a relacao nomeada e' a alavanca 2 do protocolo de recusa —
    contradize-la na fala a ANULA.
    """
    # ⛔⛔ O 4o POSICIONAL E' `travas`. A ui_agente passa o dicionario de
    # travas ali sempre que o motor declara contrato, e com a assinatura
    # antiga ele cairia dentro de `degrau` virando estado invalido EM
    # SILENCIO. O parametro antigo viaja DENTRO das travas — mesmo
    # conserto do TROCA. ⚠️ Desempacotar aqui, na PRIMEIRA linha do corpo:
    # a primeira versao fazia isso la' embaixo, no site da REF, e `degrau`
    # e' usado antes — UnboundLocalError em 100%% dos sorteios.
    travas = travas if isinstance(travas, dict) else (
        {"degrau": travas} if travas else {})
    degrau = travas.get("degrau")
    degrau = DEGRAU_PADRAO if degrau is None else degrau
    geometria = GEOMETRIA_PADRAO if geometria is None else geometria
    figurantes = FIGURANTES_PADRAO if figurantes is None else figurantes

    hist = ledger.get(pagina, {})
    pool_h = homens_de(pagina)

    # ⚠️ 28 e' o piso da ES11 — ela fala do marido.
    nar = (sc.ref_bela(NARRADORAS[0], rng,
                       idade_min=IDADE_MINIMA_NARRADORA)
           if travas.get("bela")
           else _evitando(rng, NARRADORAS, hist.get("narradora", [])[-3:]))
    # ⛔ ES11/TETO_DIF_IDADE: o homem sai do pool JA' FILTRADO pela diferenca de
    # idade. A cena 3 poe os dois num quadro de proxy falico, e a politica de
    # menores e' a determinista — nao cede a regerar. Filtro por construcao, com
    # fallback: se nenhum homem couber, `_evitando` volta ao pool inteiro e o
    # AVISO da ES11 acusa.
    pool_ok = [h for h in pool_h
               if h["idade"] - nar["idade"] <= TETO_DIF_IDADE] or pool_h
    # ⛔ SEM MODO_FORTE AQUI. Este slot e' o FIGURANTE CONGELADO, e a ES11
    # exige 55-70 anos: ele e' a plateia muda que encena o constrangimento, nao
    # o corpo-prova. Homem musculoso de 26-38 nao e' o que a cena pede, e
    # forcar o modo reprovava 200 de 200.
    hom = _evitando(rng, pool_ok, hist.get("homem", [])[-3:])
    rea = _evitando(rng, REACOES, hist.get("reacao", [])[-2:])

    # ⚠️ ES10/ES2: no degrau 1 o hook NOMEIA o orificio, entao o par sorteado tem
    # de ter `fala_f`. O filtro e' por CONSTRUCAO — deixar o `.format` resolver
    # um `None` escreveria a palavra "None" na Dialogue.
    pares = [p for p in PARES if p["fala_f"]] if degrau == 1 else PARES
    par = _evitando(rng, pares, hist.get("par", [])[-2:])

    rec = _evitando(rng, RECEITAS, hist.get("receita", [])[-2:])
    # ⚠️ ES5: a fisica sai do subconjunto que a RECEITA consegue produzir — as
    # duas caem na mesma travada do TAKE 02, e prompt que se contradiz o modelo
    # resolve como quiser.
    fis = _evitando(rng, fisicas_de(rec), hist.get("fisica", [])[-2:])
    cen = _evitando(rng, CENARIOS, hist.get("cenario", [])[-2:])
    # ⚠️ ES9/ES8: o mecanismo PLANTADO nao pode desenhar o mesmo objeto que a
    # imagem da receita ja' desenha no MESMO IMAGE 02 — com `copo_sache` o bloco
    # saia com dois copos altos (o morno da receita na tabua e o frio na
    # bancada). Mesma mecanica de colisao por construcao do `_bancada_livre`.
    img_r = _pares(rec["img"])
    mec_pool = [m for m in MECANISMOS_PROP
                if not (_pares(m["plantado"]) & img_r)] or MECANISMOS_PROP
    mec = _evitando(rng, mec_pool, hist.get("mecanismo", [])[-2:])

    # ES1 — com dois figurantes o segundo sai do MESMO pool de etnia, com id
    # diferente e com uma REACAO diferente: dois rostos com a mesma cara fundem
    # em um so' (P13/F4b), e ai' o gag perde metade da plateia.
    # ⚠️ So' o PRIMEIRO volta na cena 3 [D2] — o segundo nao vira arco.
    hom2 = rea2 = None
    if figurantes == 2:
        hom2 = rng.choice([h for h in pool_h if h["id"] != hom["id"]])
        rea2 = rng.choice([r for r in REACOES if r["id"] != rea["id"]])

    relacao = _relacao(rng, nar["idade"], hom["idade"])

    # ES16/cota do orgao: tres substantivos DISTINTOS sorteados de uma vez. No
    # degrau 1 (e no 4) o primeiro nao entra em fala nenhuma — fica de reserva
    # para o `nova_fala()` da UI nao repetir o que ja' esta' em cena.
    # ⛔⛔ CT4b (2026-08-10) — SO' TRES APELIDOS SAO SORTEAVEIS.
    # Ordem do operador: *"quero que vc use weiner e john-son pra se referir ao
    # orgao tb, nao apenas pec-ker"*. `soldier` soa filme de guerra para ouvido
    # americano e `tool` e' ambiguo em giria dos EUA; os dois seguem no NUCLEO
    # porque as LENTES os usam para DETECTAR o orgao — o que muda e' que nao
    # sao mais sorteaveis. O CT4 trava UM apelido por video; sem isto aqui, um
    # apelido por video vira o MESMO apelido no lote inteiro.
    _o1 = rng.choice(sc.APELIDOS_16)
    orgaos = [_o1] * 3
    falas = _montar_falas(rng, par, rec, orgaos, relacao, degrau)
    ban = _bancada_livre(rng, falas, hist.get("bancada", [])[-2:], rec)

    return {"pagina": pagina, "narradora": nar, "homem": hom, "reacao": rea,
            "homem2": hom2, "reacao2": rea2, "par": par, "receita": rec,
            "fisica": fis, "cenario": cen, "bancada": ban, "mecanismo": mec,
            "degrau": degrau, "geometria": geometria, "figurantes": figurantes,
            "relacao": relacao, "falas": falas,
            # ⭐ 50/50, ordem do operador 2026-08-04. ⚠️ Sorteado com `rng`, nunca
            # derivado do cenario: amarrar a bandeira ao set faria dela mais um
            # atributo fixo, que e' exatamente o estado que ele mandou quebrar.
            "bandeira": rng.random() < 0.5}


# ---------------------------------------------------------------------------
# GERADOR
# ---------------------------------------------------------------------------
# Formato de entrega, sempre: BLOCO 0 (REF) -> os 3 IMAGE agrupados -> os 3
# TAKE agrupados. ⛔ Nunca intercalar. Destino: AdBatch Vertical 3.

def montar(spec):
    et = ETNIA[spec["pagina"]]
    nar, hom, cen = spec["narradora"], spec["homem"], spec["cenario"]
    # ⚠️ `rec`, `fis`, `ban` e `recibo` NAO sao desempacotados: os quatro so'
    # alimentavam a IMAGE/TAKE 02/03, o bloco da bancada, que caiu na fusao. Os
    # eixos continuam SORTEADOS e no ledger (o painel os trava, e a receita
    # entra na FALA da fundida), mas nenhum bloco os imprime.
    par, rea = spec["par"], spec["reacao"]
    mec = spec["mecanismo"]
    falas = spec["falas"]
    luz = _maiuscula(cen["luz"])

    # ⭐⭐ A BANDEIRA E' 50/50 (ordem do operador, 2026-08-04). Ela estava escrita
    # DENTRO da string de cada cenario, entao aparecia em 100% dos videos — e o
    # proprio autoteste a exigia em 15/15. Aqui ela sai por remocao exata quando
    # o sorteio diz que nao, e o `lint_bandeira` confere no TEXTO MONTADO.
    # ⛔ Nao se reescreve o pool: as 15 strings de cenario sao copy validada.
    com_bandeira = spec.get("bandeira", True)
    cen_set = cen["set"] if com_bandeira else sc.tirar_bandeira(cen["set"])
    cen_anc = (cen["re_ancora"] if com_bandeira
               else sc.tirar_bandeira(cen["re_ancora"]))

    # ⚠️ ES3/ES11 — A ANCORA DE CONTINUIDADE VOLTA INTEIRA, com a marca facial,
    # tanto na narradora (que esta' nas tres cenas) quanto no homem (que volta na
    # cena 3). Ancora curta ("same hair") carrega a roupa e PERDE O ROSTO — foi
    # assim que o VAZAMENTO devolveu um senhor de oculos e bigode no lugar do
    # corpo-prova.
    # ⛔ E ela nunca leva adjetivo de etnia [D4]: e' sorteada livre.
    ela = ("a %d-year-old woman with %s, wearing %s"
           % (nar["idade"], nar["marca"], nar["roupa"]))
    mesma = ("The same %d-year-old woman, with %s, wearing %s"
             % (nar["idade"], nar["marca"], nar["roupa"]))

    par_img = (ES_PAR_MONTADOS_IMAGE if spec["geometria"] == "montados"
               else ES_PAR_SEPARADOS_IMAGE) % (par["e_img"], par["f_img"])

    plateia_img = ES_PLATEIA_IMAGE % (hom["idade"], et, hom["marca"],
                                      hom["roupa"], hom["calca"],
                                      _maiuscula(rea["desc"]))
    plateia_take = ES_PLATEIA_TAKE
    if spec["figurantes"] == 2:
        h2, r2 = spec["homem2"], spec["reacao2"]
        plateia_img = "%s %s %s" % (
            plateia_img,
            ES_PLATEIA_IMAGE_2 % (h2["idade"], et, h2["marca"], h2["roupa"],
                                  h2["calca"], _maiuscula(r2["desc"])),
            ES_CONTRASTE_FIGURANTES)
        plateia_take = ES_PLATEIA_TAKE_2


    b = {}

    # O REF e' a NARRADORA: e' o rosto que precisa se repetir nas tres cenas. O
    # homem entra na cena 1 dentro da travada da plateia e volta na 3 pela
    # ancora inteira — ele nao tem REF proprio.
    b["BLOCO 0 (REF)"] = (
        "REF 01: Photo of a real person, a %d-year-old woman, chest up, facing "
        "the camera directly, calm steady expression. %s. Wearing %s. Plain "
        "neutral gray background, soft even frontal light. No subtitles, no "
        "captions, no burned-in text, no watermark."
        % (nar["idade"], _maiuscula(nar["marca"]), nar["roupa"])
    )

    # --- IMAGE 01/03 — O ESCANDALO -------------------------------------------
    # Os elementos obrigatorios do hook, todos 2/2 na fonte: ela com o olhar na
    # lente · o PAR (eixo + orificio) na altura do peito · as caras congeladas no
    # mesmo plano focal · o alibi de autoridade por FORMA.
    # ⛔ SEM bancada-recibo, SEM mecanismo, SEM receita (ES14/F12c): este quadro
    # ja' carrega 2-3 pessoas e 2 props, e densidade e' superficie de bloqueio.
    # O lastro do `full recipe` e' pago na cena 2, onde a cena e' de 1 pessoa.
    # ⛔ E a SOBREPOSICAO prop x corpo nunca e' descrita: e' fato de camera. A
    # travada fala do BRACO dela e de ONDE ele esta', e a perspectiva faz o resto.
    b["IMAGE 01/02"] = (
        "IMAGE 01/02: Medium shot in %s. Standing in the middle of the frame is "
        "%s. She looks straight into the lens. %s %s %s %s"
        % (cen_set, ela, par_img, plateia_img, luz, CAUDA)
    )

    # --- IMAGE 02/03 — A RECEITA INCOMPLETA ----------------------------------
    # ES15: o corte seco aos 8s descarta o hook INTEIRO — os figurantes e os dois
    # props somem e nao voltam (invariante 2/2 da fonte). Ela fica sozinha.
    # ES9: a peca do mecanismo ja' estava plantada desde o frame 1; o reveal da
    # cena 3 nao apresenta nada novo, puxa pro primeiro plano o que ja' estava.
    # ⚠️ `at the %s` e nao `at the same %s`: a bancada NUNCA foi estabelecida no
    # IMAGE 01 (por ES14 o quadro do hook nao tem bancada nenhuma), entao "the
    # same counter" era referencia pendurada. A continuidade quem carrega e' o
    # `re_ancora`, que ja' diz "the same kitchen".
    # --- IMAGE 02/02 — ⭐⭐ A CENA FUNDIDA -----------------------------------
    # ⛔⛔ QUADRO DA CENA 3 DO MOTOR DE 24s, INTACTO. A cena 2 de la (a receita
    # executada na bancada) NAO entra como imagem: ela tem o copo, a tigela e o
    # po sobre a tabua, e a 3 tem o corpo-prova ao lado dela. Juntar as duas
    # empilha bancada + dois corpos + o par de props em 8 segundos, e quadro
    # entulhado o Veo resolve APAGANDO alguem — normalmente o corpo-prova, que e
    # o payoff. Licao paga no TRIO 16.
    # ⭐⭐ E SOME JUNTO O DEFEITO DA COLHER. O template ES_RECEITA_TAKE manda
    # "her left hand turns a wooden spoon" nas DEZESSEIS receitas, e apenas
    # DUAS delas declaram colher na IMAGE — 162 de 400 videos do motor de 24s
    # saem com o TAKE mandando animar um objeto que a imagem nao tem. Ele era
    # usado SO no TAKE 02/03, que e' o bloco que morre aqui: os ~44% de
    # contradicao TAKE x IMAGE nao passam para este motor.
    # ⚠️ O de 24s continua com o defeito — conserta-lo mexe em CENA, e cena e'
    # alcada do operador.
    # ⭐ A receita sobrevive na FALA, que e a regra da familia 16s.
    b["IMAGE 02/02"] = (
        "IMAGE 02/02: Medium shot in %s, same light. %s, stands frame-left. The "
        "same %d-year-old %s man with %s, in %s and %s, stands beside her, "
        "upright, chin level, his eyes on the lens, saying nothing. %s %s "
        "They are the only two people in the frame. %s %s"
        % (cen_anc, mesma, hom["idade"], et,
           hom["marca"], hom["roupa"], hom["calca"],
           ES_F12B_IMAGE % (_peca(hom["calca"]), par["e_img_dele"],
                            spec["relacao"]),
           ES_KEYWORD_NA_MAO_IMAGE % mec["curto"], luz, CAUDA)
    )

    # --- TAKE 01/03 -----------------------------------------------------------
    # ⭐ ES1/ES2 — nada se move. O hook e' um quadro parado que fala: os props
    # nao mudam de estado e as caras nao evoluem, a expressao do ultimo frame e'
    # a do primeiro. Toda a energia vem de prop, rosto e legenda.
    b["TAKE 01/02"] = (
        "TAKE 01/02: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway, no cuts, and the camera does not move. She "
        "talks straight into the lens the whole time. %s %s\nDialogue: \"%s\"\n"
        "Audio: quiet room tone in the %s. No music."
        % (ES_PAR_TAKE, plateia_take, sonorizar(falas[0]), cen["curto"])
    )

    # --- TAKE 02/03 — A RECEITA EXECUTADA ------------------------------------
    # ⚠️ ES5: a receita e' EXECUTADA pelas maos na tela, com o liquido mudando de
    # estado. Objeto parado na mao enquanto ela fala e' cena morta (P20).
    # ⚠️ Coreografia EM BATIDAS COM SEGUNDOS: verbo sozinho nao e' instrucao — o
    # Veo precisa do COMO.
    # ⭐ A fisica do liquido e' EIXO PROPRIO, independente do ingrediente: e' a
    # carga que a FALA NAO PAGA.
    b["TAKE 02/02"] = (
        "TAKE 02/02: Animate the provided image exactly. Handheld iPhone shot, "
        "very slight natural sway, no cuts, and the camera does not move. %s %s "
        "She speaks straight into the lens, calm and even, no rush. Only she "
        "speaks.\nDialogue: \"%s\"\nAudio: quiet room tone in the %s. No music."
        % (ES_F12B_TAKE % par["e_nome"], ES_KEYWORD_NA_MAO_TAKE,
           # ⚠️ , a SEGUNDA e ULTIMA. Com duas cenas o indice 2
           # nao existe — e um IndexError aqui so aparece no lote.
           sonorizar(falas[1]), cen["curto"])
    )

    # ⛔ ES18 — trava de texto queimado em todo TAKE. A fonte assina
    # `genaicontent` em 46/46 frames e faz 33K/82K: e' DADO de que o publico nao
    # pune, nao permissao. Nos continuamos limpando.
    return sc.selar_takes(b)


# ---------------------------------------------------------------------------
# LINTER — as regras ES
# ---------------------------------------------------------------------------
# ⚠️ A NUMERACAO E' A DA DOUTRINA, caractere por caractere (P9: uma regra, um
# lugar). O TROCA ja' pagou por nao fazer isso: o linter dele dizia "TR9: IMAGE
# 03/03 sem a ancora de bolso" e a TR9 da doutrina era o `gelatin trick` — dez
# numeros significavam coisas diferentes dos dois lados, e o operador nao tinha
# como auditar cobertura. A doutrina do ESCANDALO foi estendida ate' a ES22 para
# as regras que este motor legitimamente criou.
#
#   ES1  a plateia congelada       ES12  o livro nao e' absorvido / keyword
#   ES2  o par + imobilidade       ES13  alibi por FORMA / zero texto legivel
#   ES3  o arco (o mesmo homem)    ES14  densidade
#   ES4  a F12b / a agencia        ES15  elenco 2-3/1/2 e uma voz so'
#   ES5  receita sem dose          ES16  orcamento (piso E teto) + cota
#   ES6  receita incompleta        ES17  ⛔ declaracao de conformidade  (novo)
#   ES7  uma palavra tecnica       ES18  ⛔ texto queimado                (novo)
#   ES8  a bancada-recibo          ES19  gates: regra de POOL do vocativo (novo)
#   ES9  o objeto da keyword       ES20  eco de FATO                      (novo)
#   ES10 a escada do hook          ES21  ledger / anti-repeticao          (novo)
#   ES11 casting e congruencia     ES22  self-test de entropia            (novo)
#
# Toda ES e' ERRO, salvo os AVISOs explicitos (orcamento acima do teto, eco de
# fato, P22, figurino).
#
# ⛔ REGRA DE ESCRITA DE LINTER, paga na construcao do TROCA: NUNCA comparar com
# uma constante que tem SLOT (`ES_X not in bloco` da' 100% de falso positivo
# quando ES_X chega formatada). Compara-se o MIOLO INVARIANTE — o trecho entre
# os %s, que sobrevive a qualquer preenchimento. E se um linter reprova 100%, a
# suspeita e' DELE, nao da cena.

# --- miolos invariantes das travadas ---------------------------------------
M_PLATEIA_IMG = ", the way a studio audience reacts to a punchline. He does not speak."
M_PLATEIA_TAKE = "held without change for the entire shot"
M_PAR_SEPARADOS = "the way a grocer holds up two things to compare them"
M_PAR_MONTADOS = "the way a cook holds up a skewer before it goes on the grill"
M_F12B_IMG_A = "Centred against the front of his "
M_F12B_IMG_B = "in both his own fists one stacked above the other, he holds"
M_F12B_IMG_C = "points one finger down at it without touching him, talking straight to camera."
M_F12B_TAKE_A = "Her pointing finger stays close but never touches him."
M_F12B_TAKE_B = "in his own fists stays exactly as it appears in the first frame"
M_KEYWORD_IMG = ("In her own free left hand, raised to the height of her chest "
                 "and held level, she holds ")
M_RECIBO = " beside her, never touched and never mentioned: "
M_PLANTADO = " has been standing on the "
M_RECEITA_TAKE = ("her left hand turns a wooden spoon through it twice and "
                  "lifts the spoon clear of the rim")


def _achar(txt, tokens):
    """Os tokens de uma tabela que aparecem no texto (palavra inteira)."""
    return [t for t in tokens if re.search(r"\b%s\b" % re.escape(t), txt, re.I)]


def _direcao(txt):
    """So' a direcao de cena — o `Dialogue:` fica de fora.

    A fala e' o produto: ela DIZ a promessa, nomeia o proxy no degrau 1 e usa
    `his {o}`. As varreduras de token de IMAGEM nao podem cair sobre ela.
    """
    return txt.split("\nDialogue:")[0]


# ES1 — ⛔ ZERO EXISTENCIA VERBAL. E' o que da' nome ao agente: se a fala o
# menciona, ele deixa de encenar no lugar do espectador e vira personagem
# comentado. Invariante 2/2 da fonte em 42 segundos.
ES1_MENCAO = re.compile(r"\b(he|him|his|these guys|my husband|my man)\b", re.I)
# ⛔ risco nº4 da §9 do mapa. O banimento nasceu de um caso em que a boca era
# DELA, a centimetros da haste; continua valendo sem excecao.
ES1_BOCA = re.compile(r"mouth open|open-mouthed|lips parted|tongue|mouth agape",
                      re.I)

# ES4 — tokens que ja' custaram recusa, e os dois rotulos proibidos por ordem do
# operador.
ES4_TOKENS = ("groin", "pubic", "crotch", "genital", "the victim",
              "the narrator")
# ⛔ o vocabulario do homem ABATIDO E PASSIVO: foi a composicao das 4 recusas
# deterministicas de 2026-07-30. O que bloqueia nao e' o prop, e' a agencia.
ES4_PASSIVO = ("seated", "slumped", "head down", "head bowed", "defeated",
               "ashamed", "stands still", "steady at his side")

# ES5 — ⛔ ZERO MEDIDA, ZERO HORARIO (V5 do VAZAMENTO). A receita-isca e' TOPICA
# ou de PREPARO, nunca dose medica.
# ⚠️ E o motivo esta' escrito: dose + `your {o}` no mesmo take reproduz a
# composicao claim-sobre-o-corpo + prazo que derrubou o video do NECROSE.
ES5_MEDIDA = re.compile(
    r"\b(teaspoons?|tablespoons?|tbsp|tsp|cups?|ounces?|oz|grams?|milligrams?|"
    r"mg|ml|millilitres?|drops?|scoops?|doses?|servings?)\b", re.I)
# ⚠️ `scoop` SAI da varredura da DIRECAO porque nos pools ele e' UTENSILIO ("a
# wooden scoop lying beside it"), nao unidade — reprovaria 100% dos IMAGE 02 com
# o mecanismo `granulos` ou a bancada `figos_lata`. Linter que reprova sempre e'
# linter errado.
#   servings? -> "its serving spoon lying on the board beside it"
#   cups?     -> mobilia ("a small US flag in a pen cup beside the toaster")
#   drops?    -> VERBO ("her right hand ... drops both pieces into the mug",
#                "a fine dark sediment drops out of the liquid")
# O que sobra sao unidades que nao tem como ser outra coisa. E a trava que
# importa continua INTEIRA: a lista completa roda sobre a FALA, que e' onde a
# receita viraria bula.
ES5_MEDIDA_CENA = re.compile(
    r"\b(teaspoons?|tablespoons?|tbsp|tsp|ounces?|oz|grams?|milligrams?|"
    r"mg|ml|millilitres?|doses?)\b", re.I)
ES5_HORARIO = re.compile(
    r"\b(every morning|each morning|empty stomach|twice a day|"
    r"three times a day|before bed|at bedtime|every day|first thing)\b", re.I)

# ⛔ ES5 — MARCADOR DE PRAZO. A doutrina anunciava esta trava ("o linter reprova
# a soma `your <nucleo>` + marcador de prazo dentro do mesmo take de 8s") e ela
# NAO existia no codigo — regra anunciada e nao escrita e' regra que a proxima
# edicao de pool quebra em silencio. E' a composicao exata (claim sobre o corpo
# do espectador + prazo) que derrubou o video do NECROSE.
ES5_PRAZO = re.compile(
    r"\b(inside|within|in|after)\s+\w+\s+(weeks?|days?|months?)\b"
    r"|\b\w+\s+(weeks?|days?|months?)\s+(later|in)\b"
    r"|\bby\s+(sunday|monday|tuesday|friday|saturday|christmas)\b", re.I)

# ⛔ ES5 — `your <nucleo>` SO' EM FORMA CONDICIONAL OU PERGUNTA.
# Precedente pago e ja' virado linter no NECROSE (`necrose_lucas.py`: "o hook
# precisa de `if` ou terminar em `?`"), com o diagnostico escrito em
# licoes-producao-veo: *"o hook nasceu da linha condicional da fonte e foi
# derivando para a forma assertiva ao longo do pool, sem que ninguem notasse"*.
# A condicional VENDE EXATAMENTE O MESMO DESEJO; o que ela nao faz e' ATESTAR o
# estado do corpo de quem assiste.
# ⛔ E ela NAO toca no degrau 1: os hooks do degrau 1 nomeiam os dois props e
# nunca dizem `your <nucleo>`, entao a ordem do operador [D3] passa intacta por
# esta regra. Quem ela pega e' o ESCAPE (degraus 2 e 3) — um escape que nao e'
# mais seguro que o degrau recusado nao escapa de nada.
ES5_2A_NUCLEO = re.compile(
    r"\byour\s+(%s)\b" % "|".join(re.escape(o) for o in NUCLEO), re.I)


def _afirma_no_corpo(fala):
    """A frase que diz `your <nucleo>` sem `if` e sem `?` — ou None.

    ⚠️ Mora aqui, ao lado da tabela da ES5, e nao na secao HELPERS, para que a
    regra e a sua varredura envelhecam juntas. E' chamada tanto pelo linter
    quanto pelo `_montar_falas` (Python resolve no momento da chamada).
    """
    for frase in re.findall(r"[^.!?]+[.!?]*", fala):
        if not ES5_2A_NUCLEO.search(frase):
            continue
        if re.search(r"\bif\b", frase, re.I) or frase.rstrip().endswith("?"):
            continue
        return frase.strip()
    return None

# ES6 — a negacao vem ANTES da solucao, ou na mesma frase que ela.
# ⚠️ `don't` esta' na lista porque uma das fundidas escreve a negacao assim
# ("Here's the half they don't: the gelatin trick"). O marcador e' a NEGACAO,
# nao uma palavra preferida.
ES6_NEGACAO = ("without", "skip", "alone", "never", "none of it", "nothing",
               "half a recipe", "the other half", "leave out", "nobody",
               "don't", "doesn't", "didn't")

# ES7 — UMA palavra tecnica, uma so'. Zero perde o verniz; duas viram aula.
ES7_TECNICAS = ("vasodilator", "nitric oxide", "circulation", "collagen",
                "oxygen")

# ES11 — ⛔ a narradora nunca leva adjetivo de etnia [D4].
# ⚠️ O padrao e' PRECISO de proposito: varrer `white` solto reprovaria "a cropped
# white crochet top", que e' cor de roupa. O que se proibe e' o adjetivo
# QUALIFICANDO a mulher.
ES11_ETNIA_DELA = re.compile(
    r"\b(white|black|african|hispanic|latina|asian|caucasian)\s+"
    r"(american\s+)?woman\b", re.I)

# ES13 — ⛔ ZERO TEXTO LEGIVEL e ZERO CREDENCIAL DECLARADA (P12 + a cerca do
# ELA_DIAGNOSTICA). A fonte compra credibilidade com dois diplomas de texto
# legivel; sao DOIS problemas, nao um.
ES13_TEXTO = ("diploma", "certificate", "degree", "licence", "license", "label",
              "logo", "brand", "title", "poster", "sign", "written", "reads",
              "lettering", "inscription")
# ⛔ e nunca escrever que o texto e' ilegivel: negacao e' municao, pela mesma
# mecanica de `fully clothed`.
ES13_NEGACAO = ("illegible", "unreadable", "blurred text")

# ES14 — ⛔ OS OBJETOS QUE A DOUTRINA BANE POR NOME: "planta, carpete, caixa
# triangular de bandeira, joia, tatuagem e ima de geladeira nao entram: sao
# superficie de bloqueio sem funcao de leitura."
# ⚠️ DUAS EXCECOES REGISTRADAS na ES14 da doutrina em 2026-08-02, e por isso
# fora desta tabela:
#   · JOIA e TATUAGEM no FIGURINO DA NARRADORA — divergencia deliberada do UN1,
#     o pool segue a fonte (cropped + joias de ouro). E' peca de roupa descrita,
#     que a ES17 separa de vocabulario de desejo;
#   · o ima de geladeira do `cozinha_modesta` — ali ele E' a bandeira dos EUA,
#     que a ES13 manda copiar. O que a ES14 bane e' o ima DECORATIVO.
# ⛔ O que sobra e' banido sem excecao, e a tabela existe para a proxima edicao
# de pool: hoje ela nao dispara (o `potted plants` do `varanda_sol` saiu junto).
ES14_BANIDOS = ("carpet", "rug", "potted plant", "houseplant", "pot plant",
                "flag case", "folded flag", "triangular case")

# ⚠️ GUARDA DE DENSIDADE POR BLOCO (F12c: "quanto mais info voce da' pro Veo,
# mais municao voce da' pra ele flagrar algo"). O IMAGE 03/03 e' o bloco mais
# arriscado do lote e era o UNICO sem guarda — o `_es14_densidade` so' olhava o
# IMAGE 01. O teto e' AVISO e esta' logo acima do maximo medido depois da poda
# de 2026-08-02: e' regressao que ele pega, nao o lote de hoje.
# Medido em 2026-08-02 depois da poda (media / maximo, 200 sorteios):
#   1 figurante  — IMAGE 01 244/266 · IMAGE 02 203/218 · IMAGE 03 225/244
#   2 figurantes — IMAGE 01 342/366 (a segunda travada de plateia + a frase de
#                  contraste da P13), os outros dois iguais
# (o IMAGE 03 vinha de 246 de media antes da poda da relacao repetida e da
# FRASE_SEM_MARCA — 21 palavras a menos no bloco mais arriscado do lote.)
# ⚠️ A entrada de `IMAGE 02/03` saiu junto com o bloco. O teto da fundida
# e' o da antiga cena 3, porque o QUADRO e' o dela, sem uma alteracao.
ES14_TETO_BLOCO = {"IMAGE 01/02": 275, "IMAGE 02/02": 255}
ES14_EXTRA_FIGURANTE = 110

# ES17 — ⛔ ZERO DECLARACAO DE CONFORMIDADE. Declarar entrega ao classificador a
# categoria que ele deve procurar. Silencio vence negacao.
ES17_CONFORMIDADE = ("not a celebrity", "fully clothed", "they are adults",
                     "no nudity", "consensual", "age-appropriate",
                     "non-sexual", "consenting", "nothing sexual")


def _es1_plateia(spec, blocos, achados):
    """ES1 — ⭐⭐ A PLATEIA CONGELADA QUE A FALA NUNCA MENCIONA **NA CENA 1**.

    ⚠️ A varredura de mencao roda so' sobre `falas[0]`, e isso esta' CERTO: a
    [D2]/ES3 transforma o figurante em ARCO, e as 16 FUNDIDAS e as 16 PROVAS
    dizem `his {o}` — sem esse `his` a prova da cena 3 nao teria dono. A ES1.4
    da doutrina dizia "em nenhuma das 3 cenas" e foi corrigida em 2026-08-02
    para o que a cena de fato exige: o silencio verbal e' o da CENA 1.
    """
    img, take = blocos["IMAGE 01/02"], blocos["TAKE 01/02"]
    if M_PLATEIA_IMG not in img:
        achados.append(("ERRO", "ES1: IMAGE 01/03 sem a travada da plateia — e' "
                                "o agente inteiro, e a analogia de genero e' o "
                                "que mantem a cara de escandalo sem 'mouth open'"))
    if M_PLATEIA_TAKE not in take:
        achados.append(("ERRO", "ES1: TAKE 01/03 sem a travada de congelamento — "
                                "a expressao do ultimo frame tem de ser a do "
                                "primeiro"))
    hit = ES1_MENCAO.search(spec["falas"][0])
    if hit:
        achados.append(("ERRO", "ES1: a cena 1 menciona o figurante ('%s') — ele "
                                "encena o escandalo NO LUGAR do espectador, e "
                                "existe 100%% na imagem e 0%% na fala"
                        % hit.group(0)))
    for nome, txt in sorted(blocos.items()):
        h = ES1_BOCA.search(txt)
        if h:
            achados.append(("ERRO", "ES1: %s usa '%s' como descritor de reacao "
                                    "perto de prop falico — a reacao entra por "
                                    "sobrancelha e olho" % (nome, h.group(0))))
    if spec["figurantes"] == 2:
        if spec["homem2"] is None or spec["reacao2"] is None:
            achados.append(("ERRO", "ES1: --figurantes 2 sem o segundo figurante "
                                    "sorteado"))
        elif spec["homem2"]["id"] == spec["homem"]["id"] or \
                spec["reacao2"]["id"] == spec["reacao"]["id"]:
            achados.append(("ERRO", "ES1: os dois figurantes tem o mesmo rosto ou "
                                    "a mesma cara — dois personagens do mesmo "
                                    "sexo e faixa FUNDEM sem >= 3 eixos visiveis"))
        elif ES_CONTRASTE_FIGURANTES not in blocos["IMAGE 01/02"]:
            achados.append(("ERRO", "ES1: dois figurantes sem a frase de "
                                    "contraste escrita (P13/F4b)"))


def _es2_par(spec, blocos, achados):
    """ES2 — ⭐ O PAR: eixo + orificio no mesmo quadro. Sem os dois nao ha'
    metafora: o eixo sozinho e' fruta, o orificio sozinho e' cafe da manha."""
    img, take = blocos["IMAGE 01/02"], blocos["TAKE 01/02"]
    presentes = [m for m in (M_PAR_SEPARADOS, M_PAR_MONTADOS) if m in img]
    if len(presentes) != 1:
        achados.append(("ERRO", "ES2: IMAGE 01/03 com %d travadas de geometria "
                                "(tem de ser exatamente uma)" % len(presentes)))
    esperada = (M_PAR_MONTADOS if spec["geometria"] == "montados"
                else M_PAR_SEPARADOS)
    if esperada not in img:
        achados.append(("ERRO", "ES2: IMAGE 01/03 nao carrega a geometria "
                                "sorteada ('%s')" % spec["geometria"]))
    for campo in ("e_img", "f_img"):
        if spec["par"][campo] not in img:
            achados.append(("ERRO", "ES2: IMAGE 01/03 sem o %s do par — sem os "
                                    "DOIS objetos nao ha' metafora" % campo))
    if ES_PAR_TAKE not in take:
        achados.append(("ERRO", "ES2: TAKE 01/03 sem a travada de imobilidade do "
                                "par — nada cresce neste angulo, e quem entrega "
                                "a promessa sao as caras"))
    if spec["degrau"] == 1 and not spec["par"]["fala_f"]:
        achados.append(("ERRO", "ES2/ES10: degrau 1 com um par sem nome falavel "
                                "para o orificio — o hook literal nomeia os dois"))


def _es3_arco(spec, blocos, achados):
    """ES3 — ⭐⭐ O HOMEM DO HOOK VOLTA COMO CORPO-PROVA NA CENA 3. E' o ARCO.

    Na fonte os figurantes somem aos 7s e nao voltam — e' por isso que o lote
    marcou 2,5 de 4. Trazendo o mesmo homem de volta, ele deixa de ser figurante.
    ⚠️ Descricao INTEIRA nas duas cenas: ancora curta carrega a roupa e perde o
    rosto.
    """
    hom = spec["homem"]
    et = ETNIA[spec["pagina"]]
    for nome in ("IMAGE 01/02", "IMAGE 02/02"):
        txt = blocos[nome]
        for campo in ("marca", "roupa", "calca"):
            if hom[campo] not in txt:
                achados.append(("ERRO", "ES3: %s sem o campo '%s' do homem — a "
                                        "ancora de continuidade e' INTEIRA, com "
                                        "marca facial" % (nome, campo)))
        if "%d-year-old %s man" % (hom["idade"], et) not in txt:
            achados.append(("ERRO", "ES3: %s sem 'the %d-year-old %s man' — idade "
                                    "em toda mencao" % (nome, hom["idade"], et)))
    if "The same %d-year-old %s man" % (hom["idade"], et) not in blocos["IMAGE 02/02"]:
        achados.append(("ERRO", "ES3: IMAGE 03/03 sem a ancora 'The same ... "
                                "man' — sem ela o Veo desenha OUTRA pessoa e o "
                                "arco morre"))


def _es4_agencia(spec, blocos, achados):
    """ES4 — ⭐ A F12b: ele segura na PROPRIA mao, ela aponta sem encostar.

    "A licao mais cara da operacao ate' hoje": quatro IMG 01 recusadas em
    sequencia, deterministicamente. Nada aqui e' decorativo.
    """
    img, take = blocos["IMAGE 02/02"], blocos["TAKE 02/02"]
    for lit, motivo in (
            (M_F12B_IMG_A, "a coordenada vem da PECA DE ROUPA, e `beside` "
                           "empurrava o prop para o quadril"),
            (M_F12B_IMG_B, "as DUAS maos: uma mao so' deixa o Veo escolher o "
                           "lado e o prop sai do eixo do corpo"),
            (M_F12B_IMG_C, "ela aponta SEM ENCOSTAR — e' o que separa do "
                           "ELA_DIAGNOSTICA, onde o dedo crava no corpo dele")):
        if lit not in img:
            achados.append(("ERRO", "ES4: IMAGE 03/03 sem o literal '%s' — %s"
                            % (lit.strip(), motivo)))
    for lit in (M_F12B_TAKE_A, M_F12B_TAKE_B):
        if lit not in take:
            achados.append(("ERRO", "ES4: TAKE 03/03 sem o literal '%s' — a "
                                    "agencia tem de continuar no movimento" % lit))
    if "his eyes on the lens" not in img:
        achados.append(("ERRO", "ES4: IMAGE 03/03 sem o olhar dele na lente — sem "
                                "isso ele e' corpo passivo, e passividade e' o "
                                "que a F12b diz que bloqueia"))
    if _peca(spec["homem"]["calca"]) not in img:
        achados.append(("ERRO", "ES4: IMAGE 03/03 sem a peca de roupa sorteada — "
                                "a ancora precisa existir na imagem"))
    if spec["relacao"] not in img:
        achados.append(("ERRO", "ES4: IMAGE 03/03 sem a relacao NOMEADA ('%s') — "
                                "e' a alavanca 2 do protocolo de recusa, e "
                                "omitir nao e' opcao" % spec["relacao"]))
    if spec["par"]["e_img_dele"] not in img:
        achados.append(("ERRO", "ES4: IMAGE 03/03 sem a ancora de escala no corpo "
                                "DELE — na cena 3 quem segura e' ele"))
    # ⛔ O ORIFICIO NAO VOLTA. Eixo + orificio composto contra o corpo de um homem
    # e' penetracao consumada sobre corpo humano: a familia exata das 4 recusas.
    for nome in ("IMAGE 02/02", "TAKE 02/02"):
        alvo = _direcao(blocos[nome])
        if spec["par"]["f_img"] in alvo or _achar(alvo, (spec["par"]["f_nome"],)):
            achados.append(("ERRO", "ES4: %s traz o orificio de volta — a "
                                    "combinacao com a F12b e' PROIBIDA, nao e' "
                                    "fila de fallback" % nome))
        for hit in [t for t in ES4_PASSIVO if t in alvo.lower()]:
            achados.append(("ERRO", "ES4: %s usa vocabulario de corpo passivo "
                                    "('%s') — foi a composicao das 4 recusas "
                                    "deterministicas" % (nome, hit)))


def _es5_sem_dose(spec, blocos, achados):
    """ES5 — ⛔ A RECEITA NAO LEVA MEDIDA NEM HORARIO (V5 do VAZAMENTO)."""
    fala = spec["falas"][1]
    for rx, rotulo in ((ES5_MEDIDA, "medida"), (ES5_HORARIO, "horario")):
        h = rx.search(fala)
        if h:
            achados.append(("ERRO", "ES5: a cena 2 traz %s ('%s') — a receita-"
                                    "isca e' de PREPARO, por forma e gesto; dose "
                                    "+ 'your <nucleo>' e' a linha que derrubou o "
                                    "video do NECROSE" % (rotulo, h.group(0))))
    for nome in ("IMAGE 02/02", "TAKE 02/02"):
        alvo = _direcao(blocos[nome])
        for rx, rotulo in ((ES5_MEDIDA_CENA, "medida"), (ES5_HORARIO, "horario")):
            h = rx.search(alvo)
            if h:
                achados.append(("ERRO", "ES5: %s traz %s ('%s') na direcao de "
                                        "cena" % (nome, rotulo, h.group(0))))
    # ⛔ A trava que a doutrina anunciava e o codigo nao tinha: `your <nucleo>`
    # somado a marcador de PRAZO no mesmo take de 8s. E' a composicao exata que
    # derrubou o video do NECROSE ("politicas contra a geracao de conteudo
    # nocivo"). Hoje e' inalcancavel por sorte — os hooks com `your <nucleo>`
    # nao tem prazo e os prazos moram em falas de 3a pessoa. Fica como guarda
    # para a proxima edicao de pool.
    for i, f in enumerate(spec["falas"], 1):
        hit = ES5_PRAZO.search(f)
        if hit and ES5_2A_NUCLEO.search(f):
            achados.append(("ERRO", "ES5: a cena %d soma 'your <nucleo>' e prazo "
                                    "('%s') no mesmo take de 8s — e' a "
                                    "composicao que derrubou o video do NECROSE"
                            % (i, hit.group(0).strip())))
        frase = _afirma_no_corpo(f)
        if frase:
            achados.append(("ERRO", "ES5: a cena %d AFIRMA sobre o corpo do "
                                    "espectador em vez de condicionar ('%s') — a "
                                    "forma valida e' condicional ('if...') ou "
                                    "pergunta; a condicional vende o mesmo desejo "
                                    "sem ATESTAR o corpo de quem assiste"
                            % (i, frase)))
    # ⚠️ AVISO: prazo SOZINHO na cena 2 (3a pessoa). Nao e' a linha do NECROSE —
    # e' 3a pessoa, que e' a forma que o mapa recomenda —, mas e' a mesma
    # familia empilhada com receita + mecanismo num take de 8s, e o operador tem
    # de ver antes de gerar.
    hit = ES5_PRAZO.search(spec["falas"][1])
    if hit:
        achados.append(("AVISO", "ES5: a cena 2 empilha receita, mecanismo e "
                                 "prazo ('%s') no mesmo take de 8s"
                        % hit.group(0).strip()))
    # ⚠️ a fisica x a receita. O `sortear()` ja' filtra por construcao; isto pega
    # o caminho da UI, em que o operador troca um dos dois na mao — e ai' o
    # TAKE 02 pode voltar a mandar "the powder goes under" com dois paus de
    # canela no copo.
    if spec["fisica"] not in fisicas_de(spec["receita"]):
        achados.append(("ERRO", "ES5: a fisica '%s' nao e' produzivel pela "
                                "receita '%s' — as duas caem na mesma travada do "
                                "TAKE 02, e prompt que se contradiz o modelo "
                                "resolve como quiser"
                        % (spec["fisica"]["id"], spec["receita"]["id"])))


def _es6_incompleta(spec, blocos, achados):
    """ES6 — ⭐⭐ A RECEITA E' DADA E DECLARADA INCOMPLETA, e a cena 2 carrega o
    literal `gelatin trick`.

    As tres propriedades do V6 do VAZAMENTO: a negacao vem ANTES da solucao, o
    orgao e' nomeado na mesma frase, e usa-se o SIM que ele ja' deu.
    """
    fala = spec["falas"][1].lower()
    pos = fala.find("gelatin trick")
    if pos < 0:
        achados.append(("ERRO", "ES6: o literal 'gelatin trick' nao esta' na cena "
                                "2 — o mecanismo perde o nome no ponto em que a "
                                "receita e' declarada incompleta"))
        return
    # a negacao antes do batismo, ou na MESMA frase que ele
    inicio = max(fala.rfind(".", 0, pos), fala.rfind(";", 0, pos)) + 1
    janela = fala[:pos] if any(n in fala[:pos] for n in ES6_NEGACAO) \
        else fala[inicio:]
    if not any(n in janela for n in ES6_NEGACAO):
        achados.append(("ERRO", "ES6: a cena 2 batiza o mecanismo sem marcador de "
                                "NEGACAO antes dele nem na mesma frase — o "
                                "espectador tem de sentir a falta antes de saber "
                                "do que"))
    if not any(o.lower() in fala for o in NUCLEO):
        achados.append(("ERRO", "ES6: a cena 2 nao nomeia o orgao — o V6 exige o "
                                "orgao NA MESMA FRASE da negacao, nunca pronome"))


def _es7_tecnica(spec, blocos, achados):
    """ES7 — UMA palavra tecnica, uma so'. E' o verniz que compra a virada de
    piada de fruta para clinica em 8 segundos."""
    fala = spec["falas"][1].lower()
    n = sum(fala.count(t) for t in ES7_TECNICAS)
    if n != 1:
        achados.append(("ERRO", "ES7: a cena 2 tem %d palavras tecnicas (tem de "
                                "ter exatamente 1) — zero perde o verniz, duas "
                                "viram aula" % n))


def _es8_recibo(spec, blocos, achados):
    """ES8 — A BANCADA-RECIBO: a boca cita 1, a imagem mostra 3-4.

    ⚠️ SO' no IMAGE 02/03. Fora do 01 (que ja' carrega duas pessoas e dois props)
    e fora do 03 (o bloco mais arriscado do lote): densidade e' superficie de
    bloqueio, e o lastro do `full recipe` ja' foi pago na cena 2.
    """
    # ⛔⛔ LENTE MORTA. O RECIBO — os itens pousados na bancada, `never
    # touched and never mentioned` — existia na IMAGE 02/03, a cena da
    # receita executada. Essa cena caiu: a fundida herdou o quadro da 3, que
    # nao tem bancada. Repontar cobraria de um bloco que nao tem onde por os
    # itens, e reprovaria 100% dos lotes.
    if False:
        achados.append(("ERRO", "ES8: IMAGE 02/03 sem a bancada-recibo — e' o "
                                "lastro do 'full recipe'"))
    for nome in ("IMAGE 01/02", "IMAGE 02/02"):
        if M_RECIBO in blocos[nome]:
            achados.append(("ERRO", "ES8: %s carrega a bancada-recibo — ela mora "
                                    "so' no IMAGE 02/03 (ES14)" % nome))
    corpo = " ".join(spec["falas"])
    for cab in spec["bancada"]["cabecas"]:
        if _cita(corpo, cab):
            achados.append(("ERRO", "ES8: a copy cita '%s', que e' item da "
                                    "bancada — o recibo so' tem lastro se a boca "
                                    "citar UM e a imagem mostrar TRES" % cab))
    colisao = set(spec["bancada"]["cabecas"]) & set(spec["receita"]["cabecas"])
    if colisao:
        achados.append(("ERRO", "ES8: a bancada repete o ingrediente da receita "
                                "(%s) — recibo que repete mostra dois, nao quatro"
                        % ", ".join(sorted(colisao))))
    if _pares(spec["bancada"]["itens"]) & _pares(spec["receita"]["img"]):
        achados.append(("AVISO", "ES8: a bancada-recibo desenha um objeto que a "
                                 "imagem da receita ja' desenha"))
    # ⚠️ SO' no IMAGE 02/03, que e' onde moram os recipientes (o copo da receita,
    # os 3 itens do recibo, o pote do mecanismo). Exigi-la tambem no IMAGE 03/03
    # — que tem UM recipiente, ja' descrito por forma — injetava `container`,
    # `plain` e `unlabelled` de graca no bloco mais arriscado do lote.
    # ⛔ Idem: a frase `every container is plain and unlabelled` protegia a
    # bancada de marcas legiveis, e nao ha' mais bancada.
    if False:
        achados.append(("ERRO", "ES8: IMAGE 02/03 sem a frase de ausencia de "
                                "rotulo, que e' escrita pela AFIRMATIVA"))


def _es9_keyword(spec, blocos, achados):
    """ES9 — ⭐ O OBJETO DA KEYWORD EM QUADRO NO FRAME EM QUE A KEYWORD E' DITA.

    Achado ③ do mapa, 2/2: e' o que faz o CTA deles funcionar sem seta, sem badge
    e sem realce de legenda. Nossa keyword e' `gelatin` e nosso objeto e' a
    gelatina — a coincidencia palavra<->objeto que eles tem de graca, nos tambem.
    """
    img3, take3 = blocos["IMAGE 02/02"], blocos["TAKE 02/02"]
    if M_KEYWORD_IMG not in img3 or spec["mecanismo"]["curto"] not in img3:
        achados.append(("ERRO", "ES9: IMAGE 03/03 sem o mecanismo na mao livre "
                                "dela — a cena que diz 'comment gelatin' tem de "
                                "mostrar gelatina"))
    if ES_KEYWORD_NA_MAO_TAKE not in take3:
        achados.append(("ERRO", "ES9: TAKE 03/03 sem a travada de imobilidade do "
                                "objeto da keyword"))
    # ⛔ dois lugares para a mesma peca dentro do MESMO bloco e' contradicao, e
    # prompt que se contradiz o modelo resolve como quiser.
    if img3.count(spec["mecanismo"]["curto"]) > 1:
        achados.append(("ERRO", "ES9: IMAGE 03/03 poe o mecanismo em dois lugares "
                                "no mesmo bloco"))
    # ⛔⛔ LENTE MORTA — a mesma do EXTERIOR 16. O plantio exigia o mecanismo
    # na bancada desde o frame 1 da cena 2, para que o reveal da cena 3 nao
    # apresentasse objeto novo (ES9). Quem plantava e' a cena que caiu.
    # ⭐ Com DOIS takes o principio se cumpre dentro do proprio take: o
    # objeto da keyword esta' na mao dela no PRIMEIRO frame da fundida e
    # fica ate' o fim — nao entra de fora do quadro em momento nenhum.
    if False:
        achados.append(("ERRO", "ES9: IMAGE 02/03 sem a travada da peca PLANTADA "
                                "— objeto que entra de fora do quadro nao e' "
                                "premio, e' corte disfarcado"))
    # ⚠️ o mecanismo plantado e a imagem da receita dividem o IMAGE 02: se os
    # dois desenham o mesmo objeto, o bloco pede dois copos altos e o Veo
    # desenha dois. O `sortear()` ja' evita por construcao; isto pega o caminho
    # da UI, em que o operador troca um dos dois na mao.
    if _pares(spec["mecanismo"]["plantado"]) & _pares(spec["receita"]["img"]):
        achados.append(("AVISO", "ES9: o mecanismo plantado desenha um objeto que "
                                 "a imagem da receita ja' desenha no mesmo "
                                 "IMAGE 02/03"))


def _es10_degrau(spec, blocos, achados):
    """ES10 — a escada do hook, e o casamento fala x imagem no degrau 1.

    ⚠️ No degrau 1 os dois substantivos da fala sao os DOIS PROPS SORTEADOS. ⛔
    Nunca deixar a travada com `banana`/`donut` fixos quando o sorteio deu outro
    par — fala e imagem tem de casar.
    """
    if spec["degrau"] not in DEGRAUS:
        achados.append(("ERRO", "ES10: degrau %r fora da escada" % spec["degrau"]))
    if spec["degrau"] != 1:
        return
    fala = spec["falas"][0].lower()
    for campo in ("fala_e", "fala_f"):
        alvo = spec["par"][campo]
        if alvo and not re.search(r"\b%s\b" % re.escape(alvo), fala):
            achados.append(("ERRO", "ES10: o hook do degrau 1 nao nomeia o '%s' "
                                    "do par sorteado — fala e imagem tem de "
                                    "casar" % alvo))
    if re.search(r"\d", spec["falas"][0]):
        achados.append(("ERRO", "ES10: algarismo na cena 1 — o Veo soletra "
                                "numero; escreve-se por extenso"))


def _es11_casting(spec, blocos, achados):
    """ES11/[D4] — a etnia do HOMEM e' a da pagina; a dela nunca e' escrita."""
    et = ETNIA[spec["pagina"]]
    for nome in ("IMAGE 01/02", "IMAGE 02/02"):
        if "%s man" % et not in blocos[nome]:
            achados.append(("ERRO", "ES11: %s sem a etnia '%s' no homem — "
                                    "congruencia inviolavel com o avatar da "
                                    "pagina" % (nome, et)))
    for nome, txt in sorted(blocos.items()):
        h = ES11_ETNIA_DELA.search(txt)
        if h:
            achados.append(("ERRO", "ES11: %s declara etnia da narradora ('%s') — "
                                    "ela e' sorteada livre [D4] e o motor nunca "
                                    "escreve a etnia dela" % (nome, h.group(0))))
    if spec["narradora"]["idade"] < IDADE_MINIMA_NARRADORA:
        achados.append(("ERRO", "ES11: narradora com %d anos (piso %d) — idade em "
                                "cena com conteudo de ED e' zona sensivel, e a "
                                "politica de menores e' a determinista"
                        % (spec["narradora"]["idade"], IDADE_MINIMA_NARRADORA)))
    for quem in (spec["homem"], spec["homem2"]):
        if quem and not 55 <= quem["idade"] <= 70:
            achados.append(("ERRO", "ES11: figurante com %d anos — a faixa e' "
                                    "55-70, o corpo com que o espectador de 50-65 "
                                    "se identifica" % quem["idade"]))
    # ⚠️ AVISO, nao ERRO: o `sortear()` ja' filtra por construcao, entao isto so'
    # dispara quando o operador FORCA o par pela interface — e ai' a escolha e'
    # dele, mas ele tem de ver o numero. So' o homem da CENA 3 conta: e' o unico
    # que entra na geometria de intimidade da F12b.
    dif = spec["homem"]["idade"] - spec["narradora"]["idade"]
    if dif > TETO_DIF_IDADE:
        achados.append(("AVISO", "ES11: %d anos de diferenca entre a narradora "
                                 "(%d) e o corpo-prova (%d), teto %d — a politica "
                                 "de menores e' sensivel a geometria de intimidade "
                                 "+ diferenca de idade, e e' a determinista"
                        % (dif, spec["narradora"]["idade"],
                           spec["homem"]["idade"], TETO_DIF_IDADE)))


def _es12_livro(spec, blocos, achados):
    """ES12/[D5] — ⛔ O LIVRO NAO E' ABSORVIDO: nem o objeto, nem a palavra.

    O grosso do CTA e' herdado do `lint_curto` (keyword, caixa, virgula,
    BANIDOS_CTA); aqui se cobra o que e' proprio: `book` fora de QUALQUER bloco,
    inclusive da direcao de cena, porque um livro em quadro convida o espectador
    a digitar a palavra que quebra a automacao de DM.
    """
    for nome, txt in sorted(blocos.items()):
        if re.search(r"\bbooks?\b", txt, re.I):
            achados.append(("ERRO", "ES12: %s contem 'book' — [D5] o livro nao e' "
                                    "absorvido, e a palavra quebra a automacao "
                                    "Comentario->DM" % nome))
    if not BANIDOS_CTA:
        achados.append(("ERRO", "ES12: BANIDOS_CTA vazio — o CTA ficaria sem a "
                                "trava de BOOK/YES/LINK"))


def _es13_texto(spec, blocos, achados):
    """ES13 — ⛔ ZERO TEXTO LEGIVEL, ZERO CREDENCIAL DECLARADA.

    ⚠️ A varredura tira antes a frase de ausencia de rotulo: ela e' afirmativa e
    nao se denunciaria hoje, mas o `replace` fica como guarda caso ela volte a
    citar `label`.
    """
    for nome, txt in sorted(blocos.items()):
        limpo = _direcao(txt).replace(FRASE_SEM_MARCA, "")
        for hit in _achar(limpo, ES13_TEXTO):
            achados.append(("ERRO", "ES13: %s contem '%s' — o alibi de autoridade "
                                    "se faz por FORMA (estante, selo dourado, "
                                    "bandeira), nunca por texto" % (nome, hit)))
        for hit in [t for t in ES13_NEGACAO if t in limpo.lower()]:
            achados.append(("ERRO", "ES13: %s declara que o texto e' ilegivel "
                                    "('%s') — negacao e' municao" % (nome, hit)))


def _es14_densidade(spec, blocos, achados):
    """ES14 — DENSIDADE: o quadro do hook e' o mais denso do repertorio.

    F12c: "quanto mais info voce da' pro Veo, mais municao voce da' pra ele
    flagrar algo." ⛔ Cortar o par, a plateia ou o recibo para "aliviar" e'
    amputar regra, nao densidade — o que se corta e' descricao livre.
    """
    img1 = blocos["IMAGE 01/02"]
    if spec["mecanismo"]["curto"] in img1 or spec["mecanismo"]["plantado"] in img1:
        achados.append(("ERRO", "ES14: IMAGE 01/03 carrega o mecanismo — o quadro "
                                "do hook ja' tem 2-3 pessoas e 2 props"))
    if spec["receita"]["img"] in img1:
        achados.append(("ERRO", "ES14: IMAGE 01/03 carrega a receita — ela e' da "
                                "cena 2, onde o elenco e' 1"))
    # ⛔ os objetos que a doutrina bane por nome, em qualquer bloco
    for nome, txt in sorted(blocos.items()):
        for hit in [t for t in ES14_BANIDOS if t in txt.lower()]:
            achados.append(("ERRO", "ES14: %s carrega '%s' — superficie de "
                                    "bloqueio sem funcao de leitura" % (nome, hit)))
    # ⚠️ a guarda que faltava: o teto de palavras POR BLOCO
    for nome, teto in sorted(ES14_TETO_BLOCO.items()):
        # ⚠️ o segundo figurante e' MODO declarado (o reel B), nao inchaco: ele
        # traz a segunda travada de plateia e a frase de contraste da P13, e as
        # duas sao regra. O teto acompanha o modo em vez de acusar 100% do lote.
        if nome == "IMAGE 01/02" and spec["figurantes"] == 2:
            teto += ES14_EXTRA_FIGURANTE
        n = _palavras(blocos[nome])
        if n > teto:
            achados.append(("AVISO", "ES14: %s com %d palavras (teto %d) — o que "
                                     "encolhe e' DESCRICAO LIVRE; string validada "
                                     "e' intocavel, e cortar o par, a plateia ou o "
                                     "recibo e' amputar regra" % (nome, n, teto)))


def _es15_elenco(spec, blocos, achados):
    """ES15 — ELENCO 2-3 / 1 / 2, E UMA VOZ SO': A DELA.

    O corte seco aos 8s descarta o hook inteiro — os figurantes e os dois props
    somem e nao voltam (invariante 2/2 da fonte).
    """
    # ⛔⛔ LENTE MORTA, e repontar seria PIOR que remove-la: ela exige que
    # ela esteja SOZINHA, e a fundida tem DOIS corpos por construcao (ela e
    # o corpo-prova). A checagem logo abaixo, que cobra `They are the only
    # two people`, e' a que vale aqui — e ela ja' existia.
    # ⚠️ Foi exatamente esse tipo de repontamento cego que inverteu lentes
    # no PLACA, no BOTICA e no COLO em 2026-08-08.
    if False:
        achados.append(("ERRO", "ES15: IMAGE 02/03 nao declara elenco 1 — o corte "
                                "seco descarta o hook inteiro"))
    if "They are the only two people in the frame." not in blocos["IMAGE 02/02"]:
        achados.append(("ERRO", "ES15: IMAGE 02/02 nao declara elenco 2"))
    for nome in ("TAKE 01/02", "TAKE 02/02"):
        if "Only she speaks." not in blocos[nome]:
            achados.append(("ERRO", "ES15: %s sem 'Only she speaks.' — o dialogo "
                                    "do Veo e' monofonico e duas vozes saem "
                                    "tortas" % nome))
    # ⛔⛔ LENTE MORTA — E EU A MATEI DEPOIS DE TE-LA REPONTADO ERRADO.
    # Ela varria `IMAGE 02/03` e `TAKE 02/03` — e SO' esses — cobrando que os
    # props do hook nao reaparecessem na cena da bancada. Repontei para a
    # fundida por reflexo, e a fundida e' a antiga cena 3, que NUNCA foi alvo
    # dela: ali o corpo-prova segura o par por construcao. Medido: 84 ERROs em
    # 400 sorteios acusando quadro CERTO.
    # ⚠️ E' o mesmo erro que inverteu lentes no PLACA, no BOTICA e no COLO em
    # 2026-08-08 — cometido tres linhas abaixo do comentario em que eu avisava
    # sobre ele. Renomear e' seguro para CHAVE; para REGRA, pergunta-se QUAL
    # bloco ela vigiava e por que.
    # ⭐ O bloco que ela vigiava nao existe mais, entao ela morre.


def _es16_orcamento(spec, blocos, achados):
    """ES16 — O ORCAMENTO E' PISO **E** TETO.

    Piso nao cobrado e' piso que nao existe: enquanto era "julgamento que mora na
    doutrina", 48% das cenas 2 do TROCA saiam abaixo dele. Teto continua sendo
    teto: cena estourada corta UMA frase (a que explica), nunca se reescreve mais
    curta e mais vaga; e o piso nao se cumpre com enchimento, cumpre-se com FATO.
    """
    for i, fala in enumerate(spec["falas"], 1):
        n = _palavras(fala)
        if n < PISO_FALA[i]:
            achados.append(("ERRO", "ES16: cena %d com %d palavras (piso %d) — o "
                                    "piso se cumpre com mais FATO, nao com "
                                    "enchimento" % (i, n, PISO_FALA[i])))
    # ⚠️ P22, item do checklist da doutrina: cada cena aterrissa em 2a pessoa ou
    # imperativo. AVISO, nao ERRO — e' pool de COPY, que e' alcada do Ed.
    for i, fala in enumerate(spec["falas"], 1):
        if not _aterrissa(fala):
            achados.append(("AVISO", "P22: cena %d nao aterrissa em 2a pessoa nem "
                                     "em imperativo" % i))


def _es17_conformidade(spec, blocos, achados):
    """ES17 — ⛔ ZERO DECLARACAO DE CONFORMIDADE, e os dois rotulos proibidos.

    Declarar entrega ao classificador a categoria que ele deve procurar: `not a
    celebrity` e `fully clothed` NOMEIAM o que policiam. Silencio vence negacao.
    """
    for nome, txt in sorted(blocos.items()):
        baixo = txt.lower()
        for hit in [t for t in ES17_CONFORMIDADE if t in baixo]:
            achados.append(("ERRO", "ES17: %s declara conformidade ('%s') — a "
                                    "declaracao e' municao de graca" % (nome, hit)))
        for hit in _achar(txt, ES4_TOKENS):
            achados.append(("ERRO", "ES17/ES4: %s contem '%s' — token proibido "
                                    "(recusa paga ou ordem do operador)"
                            % (nome, hit)))
        for hit in _achar(txt, tuple(BANIDOS_DESEJO)):
            achados.append(("ERRO", "ES17: %s usa vocabulario de desejo ('%s') — "
                                    "a divergencia de figurino e' de PECA "
                                    "DESCRITA, nunca de vocabulario"
                            % (nome, hit)))


def _es19_gates(spec, blocos, achados):
    """ES19 — GUARDA de vocativo na cena 3 (regra de POOL medida pelo operador).

    ⚠️ Hoje esta regra nao dispara, e isso e' correto: so' os GATES carregam
    vocativo (3 de 15) e so' um gate entra por video. Ela existe para a proxima
    edicao de pool — se alguem puser 'brother' num CTA, a cena 3 passa a ter dois
    e o vicio que o operador mediu (31-73%) volta. A trava VIVA e' a do
    self-test, que exige CTAS e BARREIRAS sem vocativo nenhum.
    """
    # ⚠️ indice 1: o CTA e o follow vivem na cena FUNDIDA, a ultima das duas.
    # ⛔⛔ SO' VOCATIVO DE VERDADE — correcao de 2026-08-10, e ela e' o modo de
    # falha §16 (lente que reprova o que esta' certo). Com o `{d}` derivado da
    # relacao, a fala passou a poder dizer `my man's {o}`, e o `\bman\b` do
    # `_achar` casava DENTRO do possessivo: 25 de 800 videos acusados de "dois
    # vocativos" por uma frase que nao tem nenhum. Vocativo e' quem esta'
    # DESTACADO POR VIRGULA (`Follow first, brother.`); `my man's tool` e'
    # sintagma possessivo e nao chama ninguem.
    hits = [v for v in VOCATIVOS
            if re.search(r",\s*%s\b(?!')" % re.escape(v),
                         spec["falas"][1], re.I)]
    if len(hits) > 1:
        achados.append(("AVISO", "ES19: dois vocativos na cena 3 (%s) — o "
                                 "operador mediu vicio de 'brother' e mandou "
                                 "variar" % ", ".join(hits)))


def _es20_eco(spec, blocos, achados):
    """ES20 — o mesmo FATO dito duas vezes em 24 segundos.

    'three weeks' na fundida e na prova: o orcamento e' curto demais para pagar
    a mesma informacao duas vezes, e o espectador ouve repeticao, nao reforco.
    """
    corpo = " ".join(spec["falas"]).lower()
    for e in ECOS:
        if corpo.count(e) > 1:
            achados.append(("AVISO", "ES20: '%s' aparece %d vezes no mesmo video"
                            % (e, corpo.count(e))))


def _es21_bandeira(spec, blocos, achados):
    """ES21 — ⭐ A BANDEIRA E' 50/50, e some INTEIRA quando o sorteio diz que nao.

    ⛔ Ordem do operador, 2026-08-04: *"todos os takes estao possuindo bandeiras
    dos EUA, quero algo 50%/50%"*. Ate' aqui ela estava escrita DENTRO da string
    de cada cenario, e o proprio `--stats` a exigia em 15/15 — nao havia eixo
    para sortear, havia texto.

    ⚠️ A lente varre o TEXTO MONTADO e cobra os dois lados: sorteou sem e sobrou
    bandeira = a remocao nao pegou; sorteou com e nenhum bloco a mostra = o eixo
    nao chegou ao prompt. E cobra a PROSA (virgula dupla, `and` orfao), porque
    remocao por regex em prosa erra em silencio.
    """
    sc.lint_bandeira(spec, blocos, achados, rotulo="ES21")


def _es22_abertura(spec, blocos, achados):
    """ES22 — ⭐⭐ A PRIMEIRA SENTENCA DA CENA 2 NOMEIA O ORGAO.

    ⛔ Ordem do operador, 2026-08-04, lendo o take renderizado:
    *"'I read every forum there is and found nothing' — telespectador: 'read
    WHAT? WTF? What the hell is she talking about?'"*

    ⚠️ POR QUE A UNIDADE E' A PRIMEIRA SENTENCA E NAO A FALA: a cota do orgao
    ja' cobrava a CENA, e passava — o orgao aparecia, so' que na terceira
    sentenca. Quem chega no scroll ouve a primeira antes de qualquer outra, e
    decide ali se fica. Cobrar a cena e' cobrar o lugar errado.

    ⚠️ E a desculpa do orcamento foi MEDIDA e caiu: 64,2% das aberturas eram
    orfas com folga media de +3,1 palavras. Havia espaco (licoes §21).
    """
    prim = _sentencas_es(spec["falas"][1])
    if prim and not any(o.lower() in prim[0].lower() for o in NUCLEO):
        achados.append(("ERRO", "ES22: a abertura da cena 2 nao nomeia o orgao "
                                "— %r deixa o espectador perguntando "
                                "'procurando o QUE?' no segundo em que ele "
                                "decide se fica" % prim[0]))
    # ⭐ 2026-08-10: a enumeracao mudou de pool junto com a copy. Quem abre a
    # cena 2 agora e' o MECANISMO (CT3), e ele nomeia o orgao dentro da mesma
    # sentenca em que batiza o `gelatin trick` — a ES22 e o CT3 passaram a ser
    # a mesma frase, e nao mais duas frases disputando os 8 segundos.
    # ⛔ A enumeracao sobre FUNDIDAS/ABERTURAS16 saiu porque os dois pools estao
    # PARADOS (o CT5 tirou o ingrediente da boca). Cobrar pool que nao chega ao
    # video e' lente que reprova o que nao existe — e cobrar SO' ele seria pior:
    # o pool vivo ficaria sem guarda nenhuma.
    for linha in MECANISMOS16:
        p0 = _sentencas_es(linha)
        if p0 and "{o}" not in p0[0]:
            achados.append(("ERRO", "ES22: entrada do pool MECANISMOS16 abre sem "
                                    "`{o}` — %r" % p0[0]))


def _sentencas_es(fala):
    import re as _re
    return [s.strip() for s in _re.split(r"(?<=[.!?])\s+", fala or "") if s.strip()]


# ⭐⭐ A LENTE DO CONTRATO DE COPY 16s (2026-08-10).
# ⛔ `isca_absurda=False`: este angulo NAO promete nada que ele desminta meio
# segundo depois. A isca absurda e' do TROCA, do EXTERIOR e do COLO — la' o
# verbo de ereccao no take 1 E' o gancho. Aqui a promessa do hook e' literal, e
# o CT7 vale nos DOIS takes.
def _ct16(spec, blocos, achados):
    sc.lint_copy16(sys.modules[__name__], spec, achados, isca_absurda=False)


# ⛔⛔ LENTE APOSENTADA — "substantivo repetido no video" (AVISO do lint_curto).
# Ela nasceu para os motores de 24s e CINCO cenas, onde duas mencoes iguais sao
# bordao. O CT4 do contrato de copy 16s REVERTE a regra para a familia de dois
# takes, e a reversao e' declarada: em 16 segundos o corte zera a memoria de
# trabalho, e trocar o apelido no segundo 9 obriga o espectador a remapear
# justamente quando ele ja' esta' com um pe' fora. Medido: o apelido mudava no
# corte em 100% dos videos deste motor.
# ⚠️ O AVISO mora no `short_comum`, que e' compartilhado com os 24s — la' ele
# continua CERTO e nao se toca. Quem tem de calar e' o motor de 16s, e cala
# AQUI, nomeando o que caiu e por que. ⛔ Filtro por prefixo exato: calar por
# substring larga apagaria acusacao futura em silencio, que e' o oposto do que
# uma aposentadoria declarada deve fazer.
_APOSENTADO_24S = "substantivo repetido no video"


def lint(spec, blocos):
    # ⚠️ `teto_total` explicito: o padrao do `lint_curto` e' a soma dos tetos
    # (82), que aqui e' o PISO do orcamento da doutrina — o AVISO dispararia
    # acima do numero que a ES16 exige como MINIMO. A borda de cima e' 96.
    # ⚠️ `cota_min=2`: as DUAS falas carregam o nucleo (a FALHA na cena 1, o
    # MECANISMO na cena 2), inclusive no degrau 1, cujos hooks nomeiam os props.
    achados = sc.lint_curto(
        sys.modules[__name__], spec, blocos, (1, 2, 3), TETO_FALA,
        literais=("gelatin trick",), cota_min=2, teto_total=TETO_TOTAL,
        extras=(_es1_plateia, _es2_par, _es3_arco, _es4_agencia, _es5_sem_dose,
                _es6_incompleta, _es7_tecnica, _es8_recibo, _es9_keyword,
                _es10_degrau, _es11_casting, _es12_livro, _es13_texto,
                _es14_densidade, _es15_elenco, _es16_orcamento,
                _es17_conformidade, _es19_gates, _es20_eco, _es21_bandeira,
                _es22_abertura, _ct16))
    return [(n, m) for n, m in achados if not m.startswith(_APOSENTADO_24S)]


# ---------------------------------------------------------------------------
# UI — contrato do ui_agente.py compartilhado
# ---------------------------------------------------------------------------
# ⚠️ "homens_de" e' FUNCAO da pagina, nao lista — a UI resolve isso desde
# 2026-07-31 (ui_agente._pool). "NARRADORAS" e' lista simples porque a narradora
# e' solta [D4].
EIXOS_UI = [
    ("narradora", "A NARRADORA", "NARRADORAS", "marca"),
    ("homem", "O HOMEM (hook + prova)", "homens_de", "marca"),
    ("reacao", "A CARA DE ESCANDALO", "REACOES", "id"),
    ("par", "O PAR (eixo + orificio)", "PARES", "id"),
    ("receita", "A RECEITA", "RECEITAS", "fala"),
    ("fisica", "A FISICA DO LIQUIDO", "FISICAS", "id"),
    ("cenario", "O CENARIO", "CENARIOS", "id"),
    ("bancada", "A BANCADA-RECIBO", "BANCADAS", "itens"),
    ("mecanismo", "O MECANISMO PLANTADO", "MECANISMOS_PROP", "curto"),
]

PT_CENARIO = {
    "escritorio_diplomas": "No escritório de autoridade, com estante e documentos com selo",
    "escritorio_painel": "No escritório de madeira, com estante e bandeira",
    "sala_estante": "Na sala com estante do chão ao teto",
    "cozinha_modesta": "Na cozinha modesta de laminado",
    "cozinha_ilha": "Na cozinha aberta com ilha de mármore",
    "cozinha_fazenda": "Na cozinha de fazenda com pia de louça",
    "cozinha_cabana": "Na cozinha de cabana de pinho",
    "cozinha_retro": "Na cozinha anos setenta de parede de madeira",
    "trailer": "Na cozinha corredor do trailer",
    "alpendre": "No alpendre telado dos fundos",
    "garagem": "Na bancada de garagem",
    "copa_igreja": "Na copa do salão comunitário",
    "varanda_sol": "No jardim de inverno",
    "rv": "Na cozinha do motorhome",
    "cozinha_moderna": "Na cozinha moderna preta",
}


def resumo_pt(spec):
    """A frase que permite aprovar ou re-sortear em dois segundos."""
    et = "branca" if "white" in ETNIA[spec["pagina"]] else "negra"
    quantos = ("um homem" if spec["figurantes"] == 1 else "dois homens")
    return (
        "%s, uma narradora de %d anos ergue o par (%s + %s) %s à altura do "
        "peito enquanto %s de pele %s, ao lado da cabeça dela e no mesmo foco, "
        "%s congelado%s — e a fala nunca os menciona. Na cena 2 ela está "
        "sozinha, prepara %s em água morna, e a FALA diz o que o gelatin trick "
        "faz com o órgão dele. Na cena 3 o MESMO homem de %d anos segura o eixo nas "
        "duas mãos dele, contra a frente da peça de baixo (%s), olhando na "
        "lente, enquanto ela "
        "aponta sem encostar com %s na mão livre. Três cenas de 8s, degrau %d "
        "do hook, nada cresce em quadro."
        % (PT_CENARIO.get(spec["cenario"]["id"], "No cenário"),
           spec["narradora"]["idade"], spec["par"]["e_nome"],
           spec["par"]["f_nome"], spec["geometria"], quantos, et,
           "fica" if spec["figurantes"] == 1 else "ficam",
           "" if spec["figurantes"] == 1 else "s",
           spec["receita"]["fala"], spec["homem"]["idade"],
           _peca(spec["homem"]["calca"]), spec["mecanismo"]["curto"],
           spec["degrau"])
    )


def _orgaos_de(spec):
    """Os tres substantivos que ja' estao no video, para nao rotacionar sozinho.

    ⚠️ No degrau 1 a cena 1 nao carrega nucleo nenhum — o `padrao` cobre isso
    sem inventar um quarto substantivo.
    """
    return [sc.orgao_de(sys.modules[__name__], spec["falas"][0]),
            # ⚠️ DOIS orgaos, nao tres: a fundida usa o segundo, e o terceiro
            # pertencia a cena que caiu. Manter tres deixaria um orgao
            # sorteado que nunca aparece no video.
            sc.orgao_de(sys.modules[__name__], spec["falas"][1],
                        padrao="soldier")]


def _recopiar_hook(spec, rng):
    """O PAR entra na fala 1 pelos slots {e}/{f} do degrau 1 — trocar o eixo sem
    reescrever o hook deixaria 'banana' na boca e pepino na mao.

    ⚠️ E se o par novo nao tiver nome falavel para o orificio, ele NAO pode rodar
    no degrau 1: o motor troca o par por um que tenha, em vez de escrever a
    palavra 'None' na Dialogue. O operador nao teria como consertar isso pela
    interface.
    """
    if spec["degrau"] == 1 and not spec["par"]["fala_f"]:
        spec["par"] = rng.choice([p for p in PARES if p["fala_f"]])
    novas = _montar_falas(rng, spec["par"], spec["receita"], _orgaos_de(spec),
                          spec["relacao"], spec["degrau"])
    spec["falas"][0] = novas[0]


def _recopiar_fundida(spec, rng):
    """A RECEITA entra na fala 2 pelo slot {r} — e re-sorteia a bancada se o
    ingrediente novo colidir com o recibo (ES8) e a FISICA se o liquido novo nao
    conseguir produzi-la (ES5).

    ⚠️ A fisica anda junto porque as duas caem na MESMA travada do TAKE 02: sem
    isto, trocar `beterraba` por `canela` pela interface deixava o take mandando
    "**the powder** goes under" com dois paus de canela no copo.
    """
    novas = _montar_falas(rng, spec["par"], spec["receita"], _orgaos_de(spec),
                          spec["relacao"], spec["degrau"])
    spec["falas"][1] = novas[1]
    if spec["fisica"] not in fisicas_de(spec["receita"]):
        spec["fisica"] = rng.choice(fisicas_de(spec["receita"]))
    if any(_cita(" ".join(spec["falas"]), c)
           for c in spec["bancada"]["cabecas"]) or \
            set(spec["bancada"]["cabecas"]) & set(spec["receita"]["cabecas"]):
        spec["bancada"] = _bancada_livre(rng, spec["falas"], [], spec["receita"])


def _recopiar_tudo(spec, rng):
    """Trocar a narradora reescreve as tres falas E a relacao.

    Nao e' capricho: a idade dela e' metade da conta da relacao nomeada da cena 3
    (ES4) — trocar uma narradora de 45 por uma de 28 mudaria `his wife of
    thirty-five years` para um numero que nao fecha. E a relacao manda na VOZ da
    PROVA, entao ela e' recalculada ANTES das falas.
    """
    spec["relacao"] = _relacao(rng, spec["narradora"]["idade"],
                               spec["homem"]["idade"])
    spec["falas"] = _montar_falas(rng, spec["par"], spec["receita"],
                                  rng.sample(NUCLEO, 3), spec["relacao"],
                                  spec["degrau"])
    if any(_cita(" ".join(spec["falas"]), c) for c in spec["bancada"]["cabecas"]):
        spec["bancada"] = _bancada_livre(rng, spec["falas"], [], spec["receita"])


def _trocar_homem(spec, rng):
    """O homem nao mexe em fala nenhuma diretamente, mas mexe na RELACAO — que e'
    aritmetica de idade — e a relacao manda na VOZ da PROVA da cena 3 (ES4). Se a
    relacao nova deixar de autorizar a voz intima, a cena 3 se refaz.

    ⚠️ E com dois figurantes o segundo tem de continuar sendo OUTRA pessoa: dois
    rostos iguais fundem em um so' (P13/F4b).
    """
    spec["relacao"] = _relacao(rng, spec["narradora"]["idade"],
                               spec["homem"]["idade"])
    if spec["figurantes"] == 2 and spec["homem2"]["id"] == spec["homem"]["id"]:
        pool = homens_de(spec["pagina"])
        spec["homem2"] = rng.choice([h for h in pool
                                     if h["id"] != spec["homem"]["id"]])
    if voz_da_relacao(spec["relacao"]) != "intima":
        spec["falas"][1] = nova_fala(spec, 1, rng)


def _trocar_reacao(spec, rng):
    """Com dois figurantes as duas caras tem de ser DIFERENTES — duas caras
    iguais fazem os dois rostos lerem como o mesmo personagem (ES1/P13)."""
    if spec["figurantes"] == 2 and spec["reacao2"]["id"] == spec["reacao"]["id"]:
        spec["reacao2"] = rng.choice([r for r in REACOES
                                      if r["id"] != spec["reacao"]["id"]])


EIXOS_QUE_MEXEM_NA_COPY = {
    "par": _recopiar_hook,
    "receita": _recopiar_fundida,
    "narradora": _recopiar_tudo,
    "homem": _trocar_homem,
    "reacao": _trocar_reacao,
}


def nova_fala(spec, i, rng):
    """Re-sorteia a fala da cena i (0-2) preservando o orgao que ja' esta' nela —
    a rotacao do substantivo e' do VIDEO, nao da fala."""
    o = sc.orgao_de(sys.modules[__name__], spec["falas"][i])
    return _montar_falas(rng, spec["par"], spec["receita"], [o, o, o],
                         spec["relacao"], spec["degrau"])[i]


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def imprimir(spec, blocos, achados):
    print("=" * 72)
    print("SPEC — pagina %s | narradora %s (%d) | homem %s (%d) | cenario %s"
          % (spec["pagina"], spec["narradora"]["id"], spec["narradora"]["idade"],
             spec["homem"]["id"], spec["homem"]["idade"], spec["cenario"]["id"]))
    print("       par %s | receita %s | fisica %s | mecanismo %s | bancada %s"
          % (spec["par"]["id"], spec["receita"]["id"], spec["fisica"]["id"],
             spec["mecanismo"]["id"], spec["bancada"]["id"]))
    print("       MODOS — degrau %d | geometria %s | figurantes %d | reacao %s%s"
          % (spec["degrau"], spec["geometria"], spec["figurantes"],
             spec["reacao"]["id"],
             "" if spec["figurantes"] == 1
             else " + %s (%s)" % (spec["reacao2"]["id"], spec["homem2"]["id"])))
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
        print("cena %d: %d palavras (piso %d, teto %d)"
              % (i, _palavras(fala), PISO_FALA[i], TETO_FALA[i]))
    print("video: %d palavras" % sum(_palavras(f) for f in spec["falas"]))
    if not achados:
        print("LINTER: OK — nenhuma violacao mecanica.")
    else:
        for nivel, msg in achados:
            print("[%s] %s" % (nivel, msg))
        n_erros = sum(1 for a in achados if a[0] == "ERRO")
        print("%d erro(s), %d aviso(s)." % (n_erros, len(achados) - n_erros))


# ES22 — SELF-TEST DE ENTROPIA. A barra e' ordem explicita do operador: "no
# minimo o mesmo nivel de entropia dos demais agentes shorts". Medida em 400
# sorteios (80 por pagina) com ledger VIVO — a anti-repeticao faz parte do
# comportamento real — e repetida por degrau, por geometria e por nº de
# figurantes, porque um defeito que so' aparece em parte dos sorteios e' o que o
# `--n 2 --dry-run` nao pega.
EIXOS_VISUAIS = ("narradora", "homem", "reacao", "par", "receita", "fisica",
                 "cenario", "bancada", "mecanismo")
MIN_OPCOES = 9          # piso por eixo visual
TETO_FREQ = 0.17        # nenhum item pode concentrar mais que isso
# ⚠️ FECHOS/SELOS/PROVAS/BARREIRAS entraram em 2026-08-02: o dict `copy` ja' os
# enumerava e nenhum deles tinha piso. FECHOS e' justamente o que cai de 12 para
# 8 no degrau 4 (nenhum dos 5 hooks de la' aterrissa na P22, entao o fecho tem
# de aterrissar sozinho).
MIN_COPY = {"HOOKS": 16, "FUNDIDAS": 13, "CTAS": 14, "GATES": 11,
            "FECHOS": 11, "SELOS": 11, "PROVAS": 14, "BARREIRAS": 11,
            # + 2026-08-10, os cinco pools do contrato de copy 16s. Os pisos
            # sao o tamanho DE HOJE menos dois: piso igual ao tamanho atual e'
            # piso que so' serve para impedir crescimento, e piso muito abaixo
            # nao cobra nada. ⛔ Os quatro pools do take 2 substituem
            # ABERTURAS16 (8) + RECEITAS16 (8) + GATES (15): a entropia falada
            # subiu de 8x8x8x15 = 7.680 para 17x11x16x16 = 47.872 combinacoes.
            # ⚠️ FALHAS, MECANISMOS16 e PROVAS16 RE-DERIVADAS em 2026-08-10,
            # nas DUAS conferencias que leram a saida em voz alta: os pools
            # encolheram de 18 para 17, de 18 para 17 e de 18 para 11 porque
            # uma, uma e SETE entradas foram derrubadas por nao sobreviverem a
            # uma unica audicao (o motivo de cada uma esta' escrito em cima do
            # proprio pool). O piso segue a
            # MESMA regra dos outros — tamanho de hoje menos dois — e nao a
            # regra "nunca abaixa": piso que trava um pool no tamanho que ele
            # tinha quando a copy era ruim obriga a repor lixo para passar no
            # self-test. ⛔ O que nao pode acontecer em silencio e' o
            # encolhimento; por isso os cinco textos ficam NOMEADOS no
            # comentario do pool, e nenhum piso desce abaixo de MIN_OPCOES (9).
            "FALHAS": 15, "MECANISMOS16": 16, "PROVAS16": 11,
            "FOLLOWS16": 14, "CTAS16": 14}
MIN_HOOKS_D1 = 6        # o degrau 1 e' o default: precisa de pool proprio

# ⭐ ES22, correcao de 2026-08-02 — A ENTROPIA POR `id` NAO E' A ENTROPIA QUE O
# ESPECTADOR VE'. Varios `id` diferentes entregam a MESMA STRING: 4 entradas de
# PARES repetem a descricao da banana, 7 dos 15 CENARIOS dizem `kitchen` na
# linha `Audio:` e 7 dizem `counter`. O self-test dizia "par 12 opcoes | OK"
# enquanto um em cada quatro videos carregava a mesma frase de banana.
# ⚠️ Estas chaves sao MEDIDAS E IMPRESSAS, e a barra e' cobrada como AVISO, nao
# como falha: fecha-las e' editar POOL (dar `e_img` proprio a cada entrada de
# PARES, diversificar `curto`/`bancada`), e pool e' COPY/CENA — alcada do Ed.
# ⛔ Medir e calar seria pior que nao medir: o numero fica na saida do --stats.
EIXOS_STRING = (
    ("str:par.e_img", ("par", "e_img")),
    ("str:par.f_img", ("par", "f_img")),
    ("str:par.fala_e", ("par", "fala_e")),
    ("str:par.fala_f", ("par", "fala_f")),
    ("str:cenario.curto", ("cenario", "curto")),
    ("str:cenario.bancada", ("cenario", "bancada")),
    ("str:mecanismo.curto", ("mecanismo", "curto")),
)


def _nova_medida():
    """O acumulador de uma rodada. Um por MODO — antes so' o default media."""
    return {"freq": {}, "total": {}, "vicio": 0, "p22": {1: 0, 2: 0, 3: 0},
            "n": 0}


def _id_hook(fala, degrau):
    """De volta ao template de HOOKS que produziu esta fala.

    ⚠️ Existe porque o hook nao e' campo do spec e, sem ele, o AVISO de degrau
    usava a ESPERANCA UNIFORME (100/nº de hooks) em vez do medido — e para o
    degrau 3 a esperanca da' 16,7% (abaixo da barra) enquanto o medido e' 19,2%,
    porque o filtro do orcamento e da P22 nao trata os hooks por igual.
    """
    for i, h in enumerate(HOOKS):
        if h["degrau"] != degrau:
            continue
        pat = "^" + ".+?".join(re.escape(p)
                               for p in re.split(r"\{[efo]\}", h["txt"]))
        if re.match(pat, fala):
            return "h%02d" % (i + 1)
    return "?"


# ⭐⭐ [ALCANCE] — de volta ao TEMPLATE que produziu a frase (2026-08-10).
# ⛔ Existe porque contar `len(pool)` nao e' medir entropia: o orcamento de 25
# palavras pode deixar metade das entradas INALCANCAVEIS, e o `--stats`
# continuaria imprimindo o tamanho do pool como se todas saissem. Entrada que
# nunca chega ao video esta' morta, e pool com entrada morta mente.
# ⚠️ A comparacao e' em MINUSCULAS: o motor capitaliza o inicio da frase, e uma
# busca case-sensitive ja' declarou entrada viva como morta em outro motor.
_RX_SLOT = re.compile(r"\{[a-z]\}")


def _id_beat(pool, fala):
    baixo = fala.lower()
    melhor = "?"
    for i, tpl in enumerate(pool):
        partes = [p for p in _RX_SLOT.split(tpl.lower()) if p.strip()]
        if all(p in baixo for p in partes):
            # o template mais LONGO que casa: "Follow me first." e "Follow me
            # now." dividem prefixo, e o primeiro a casar nao e' o certo.
            if melhor == "?" or len(tpl) > len(pool[int(melhor[1:]) - 1]):
                melhor = "b%02d" % (i + 1)
    return melhor


def _rodada(n_por_pagina, rng, degrau, geometria, figurantes, m=None):
    """Uma passada completa por todas as paginas. Devolve (erros, avisos, n)."""
    erros = avisos = n = 0
    mostrados = []
    for pag in sorted(ETNIA):
        ledger = {}
        for _ in range(n_por_pagina):
            spec = sortear(pag, rng, ledger, {"degrau": degrau},
                           geometria, figurantes)
            blocos = montar(spec)
            for nivel, msg in lint(spec, blocos):
                if nivel == "ERRO":
                    erros += 1
                    if len(mostrados) < 5:
                        mostrados.append("  ERRO (%s): %s" % (pag, msg))
                else:
                    avisos += 1
            if m is not None:
                if "brother" in spec["falas"][1].lower():
                    m["vicio"] += 1
                for i, fala in enumerate(spec["falas"], 1):
                    if not _aterrissa(fala):
                        m["p22"][i] += 1
                eixos = list(EIXOS_VISUAIS)
                if figurantes == 2:
                    eixos += ["homem2", "reacao2"]
                for eixo in eixos:
                    chave = (eixo + ":" + ETNIA[pag]) \
                        if eixo.startswith("homem") else eixo
                    _contar(m, chave, spec[eixo]["id"])
                for chave, (eixo, campo) in EIXOS_STRING:
                    _contar(m, chave, spec[eixo][campo])
                _contar(m, "copy:hook", _id_hook(spec["falas"][0], degrau))
                # ⛔ ERA `for i in (2, 3)` — herdado do motor de 24s, e
                # `falas[2]` nao existe na familia de DOIS takes: o --stats
                # inteiro morria de IndexError na primeira rodada, ou seja o
                # self-test de entropia deste motor nunca rodou uma vez.
                # ⚠️ Com o CT4 as duas contagens sao a MESMA distribuicao de
                # proposito (um apelido por video, repetido nos dois takes) —
                # medir as duas e' o que prova que o CT4 esta' de pe'.
                for i in (1, 2):
                    _contar(m, "copy:nucleo c%d" % i,
                            sc.orgao_de(sys.modules[__name__],
                                        spec["falas"][i - 1]))
                for nome, pool, fala in (
                        ("copy:falha", FALHAS, spec["falas"][0]),
                        ("copy:mecanismo16", MECANISMOS16, spec["falas"][1]),
                        ("copy:prova16", PROVAS16, spec["falas"][1]),
                        ("copy:follow16", FOLLOWS16, spec["falas"][1]),
                        ("copy:cta16", CTAS16, spec["falas"][1])):
                    _contar(m, nome, _id_beat(pool, fala))
                m["n"] += 1
            _anotar(ledger, spec)
            n += 1
    for linha in mostrados:
        print(linha)
    return erros, avisos, n


def _contar(m, chave, valor):
    m["freq"].setdefault(chave, {})
    m["freq"][chave][valor] = m["freq"][chave].get(valor, 0) + 1
    m["total"][chave] = m["total"].get(chave, 0) + 1


def _imprimir_entropia(m, rotulo, falhas, completo=True):
    """Imprime e COBRA a barra. Devolve as linhas soft (AVISO) da rodada.

    ⛔ Duas correcoes de 2026-08-02:
    1. `len(c)` era impresso e DESCARTADO — um eixo com 7 opcoes perfeitamente
       uniformes da' 14,3% e saia marcado OK. O piso de 9 so' era cobrado sobre
       `len(POOL)`, nunca sobre o que o sorteio de fato produziu.
    2. a entropia era medida SO' NO MODO DEFAULT: os outros seis modos rodavam
       cegos, e `--figurantes 2` nunca mediu `homem2`/`reacao2`.

    ⚠️ `completo=False` nos modos extras: so' as linhas que falham. A tabela
    inteira sete vezes vira parede de texto, e parede de texto nao se le'.
    """
    soft = []
    print("\nENTROPIA — %s (%d sorteios)%s"
          % (rotulo, m["n"], "" if completo else "  [so' o que falha]"))
    print("-" * 72)
    limpo = True
    for chave in sorted(m["freq"]):
        c = m["freq"][chave]
        topo, qtd = max(c.items(), key=lambda kv: kv[1])
        pc = qtd / float(m["total"][chave])
        duro = not chave.startswith(("str:", "copy:"))
        ruim = pc > TETO_FREQ or len(c) < MIN_OPCOES
        if ruim:
            limpo = False
        if completo or ruim:
            print("  %s %-26s %2d opcoes | mais sorteado %-40.40s %4.1f%%"
                  % ("OK " if not ruim else ("X  " if duro else "!  "),
                     chave, len(c), topo, pc * 100))
        if not ruim:
            continue
        queixa = ("%s [%s]: %d opcoes, %.1f%% em '%.40s' (piso %d opcoes, "
                  "teto %.0f%%)" % (chave, rotulo, len(c), pc * 100, topo,
                                    MIN_OPCOES, TETO_FREQ * 100))
        (falhas if duro else soft).append(queixa)
    if limpo and not completo:
        print("  (nenhum eixo fora da barra)")
    return soft


def autoteste(n_por_pagina=80, seed=7):
    falhas = []

    # --- tamanho de pool ---------------------------------------------------
    tamanhos = {"NARRADORAS": len(NARRADORAS), "HOMENS_CLARA": len(HOMENS_CLARA),
                "HOMENS_ESCURA": len(HOMENS_ESCURA), "REACOES": len(REACOES),
                "PARES": len(PARES), "RECEITAS": len(RECEITAS),
                "FISICAS": len(FISICAS), "CENARIOS": len(CENARIOS),
                "BANCADAS": len(BANCADAS),
                "MECANISMOS_PROP": len(MECANISMOS_PROP)}
    for nome, n in sorted(tamanhos.items()):
        if n < MIN_OPCOES:
            falhas.append("eixo visual %s com %d opcoes (minimo %d)"
                          % (nome, n, MIN_OPCOES))
    pares_falantes = [p for p in PARES if p["fala_f"]]
    if len(pares_falantes) < MIN_OPCOES:
        falhas.append("PARES com nome falavel para o orificio: %d (minimo %d) — "
                      "e' o pool efetivo do degrau 1, que e' o default"
                      % (len(pares_falantes), MIN_OPCOES))

    copy = {"HOOKS": len(HOOKS), "FECHOS": len(FECHOS), "FUNDIDAS": len(FUNDIDAS),
            "SELOS": len(SELOS), "PROVAS": len(PROVAS), "CTAS": len(CTAS),
            "GATES": len(GATES), "BARREIRAS": len(BARREIRAS),
            "FALHAS": len(FALHAS), "MECANISMOS16": len(MECANISMOS16),
            "PROVAS16": len(PROVAS16), "FOLLOWS16": len(FOLLOWS16),
            "CTAS16": len(CTAS16)}
    for nome, piso in sorted(MIN_COPY.items()):
        if copy[nome] < piso:
            falhas.append("pool de copy %s com %d entradas (minimo %d)"
                          % (nome, copy[nome], piso))
    por_degrau = {d: sum(1 for h in HOOKS if h["degrau"] == d) for d in DEGRAUS}
    if por_degrau[1] < MIN_HOOKS_D1:
        falhas.append("HOOKS do degrau 1 (o default): %d (minimo %d)"
                      % (por_degrau[1], MIN_HOOKS_D1))

    # --- ES19, regra de POOL dos gates -------------------------------------
    n_brother = sum(1 for g in GATES if "brother" in g.lower())
    n_voc = sum(1 for g in GATES if _achar(g, VOCATIVOS))
    if n_brother != 2:
        falhas.append("ES19: %d gates com 'brother' (a regra e' exatamente 2)"
                      % n_brother)
    if n_voc > 3:
        falhas.append("ES19: %d gates com vocativo (maximo 3)" % n_voc)
    if n_voc >= len(GATES) / 2.0:
        falhas.append("ES19: %d de %d gates com vocativo — a maioria tem de vir "
                      "sem nenhum" % (n_voc, len(GATES)))
    for nome, pool in (("CTAS", CTAS), ("BARREIRAS", BARREIRAS),
                       ("PROVAS", [p["txt"] for p in PROVAS])):
        sujos = [x for x in pool if _achar(x, VOCATIVOS)]
        if sujos:
            falhas.append("ES19: %d entrada(s) de %s com vocativo — o vocativo "
                          "so' mora nos GATES" % (len(sujos), nome))
    # ⭐ 2026-08-10 — a mesma regra de POOL, repontada para o beat que hoje
    # carrega o vocativo. O GATE saiu do video (CT1) e o FOLLOW tomou o lugar
    # dele: se a guarda ficasse so' nos GATES, o vicio de 'brother' que o
    # operador mediu no TROCA (31-73% dos videos) voltaria pela porta nova.
    n_voc16 = sum(1 for f in FOLLOWS16 if _achar(f, VOCATIVOS))
    if n_voc16 > 3:
        falhas.append("ES19: %d follows com vocativo (maximo 3)" % n_voc16)
    for nome, pool in (("CTAS16", CTAS16), ("MECANISMOS16", MECANISMOS16),
                       ("PROVAS16", PROVAS16), ("FALHAS", FALHAS)):
        sujos = [x for x in pool if _achar(x, VOCATIVOS)]
        if sujos:
            falhas.append("ES19: %d entrada(s) de %s com vocativo — no take 2 o "
                          "vocativo so' mora no FOLLOW" % (len(sujos), nome))

    # --- ES1, o pool de FECHOS nao pode mencionar o figurante ---------------
    sujos = [f for f in FECHOS if ES1_MENCAO.search(f)]
    if sujos:
        falhas.append("ES1: %d fecho(s) mencionam o figurante: %s"
                      % (len(sujos), sujos))
    # ⛔⛔ E A MESMA CERCA NO POOL QUE HOJE OCUPA O SLOT. A FALHA fala do que o
    # corpo faz de errado, e a tentacao de escrever "his {o} quits" e' enorme —
    # so' que na cena 1 nao existe `he`: o figurante congelado encena o
    # escandalo NO LUGAR do espectador, e mencionar o figurante o transforma em
    # personagem comentado. E' o agente inteiro que se perde.
    sujos = [f for f in FALHAS if ES1_MENCAO.search(f)]
    if sujos:
        falhas.append("ES1: %d falha(s) mencionam o figurante: %s"
                      % (len(sujos), sujos))
    # ⛔ CT2 — toda entrada de FALHAS tem de ENUNCIAR a falha. Pool que passa no
    # linter porque UMA entrada carrega o token e as outras nao e' pool que
    # reprova 17 videos em 18 sem ninguem ver: a lente olha o video sorteado, o
    # self-test olha o repertorio (licao §19).
    for i, f in enumerate(FALHAS, 1):
        if "{o}" not in f:
            falhas.append("CT4/cota: FALHAS[%d] sem `{o}` — no degrau 1 e' a "
                          "unica frase da cena 1 que nomeia o orgao" % i)
        prova = {"falas": [f.format(o="pecker"), ""]}
        ct2 = []
        sc.lint_copy16(sys.modules[__name__], prova, ct2, isca_absurda=False)
        if any("CT2" in msg for _n, msg in ct2):
            falhas.append("CT2: FALHAS[%d] nao enuncia falha nenhuma — %r" % (i, f))
        if _afirma_no_corpo(f.format(o="Johnson")):
            falhas.append("ES5: FALHAS[%d] afirma sobre o corpo do espectador "
                          "('your <nucleo>' fora de condicional/pergunta)" % i)
        if ES5_PRAZO.search(f):
            falhas.append("ES5: FALHAS[%d] traz marcador de PRAZO — somado ao "
                          "'your <nucleo>' dos hooks dos degraus 2 e 3 e' a "
                          "composicao que derrubou o video do NECROSE" % i)

    # --- ES11, piso de idade -----------------------------------------------
    novas = [x["id"] for x in NARRADORAS if x["idade"] < IDADE_MINIMA_NARRADORA]
    if novas:
        falhas.append("ES11: narradora(s) abaixo do piso de %d anos: %s"
                      % (IDADE_MINIMA_NARRADORA, ", ".join(novas)))
    fora = [h["id"] for h in HOMENS_CLARA + HOMENS_ESCURA
            if not 55 <= h["idade"] <= 70]
    if fora:
        falhas.append("ES11: homem(ns) fora da faixa 55-70: %s" % ", ".join(fora))

    # --- ES16, o orcamento e' alcancavel? (enumeracao exaustiva) ------------
    # ⚠️ Enumeracao, nao amostragem. Foi assim que se descobriu no TROCA que o
    # teto de nenhuma cena era alcancavel (o AVISO de teto virava codigo morto) e
    # que a cena 2 ficava abaixo do piso em 48% dos sorteios.
    extra_o = max(_palavras(o) for o in NUCLEO) - 1
    for d in DEGRAUS:
        hk = [_palavras(h["txt"]) for h in HOOKS if h["degrau"] == d]
        fa = [_palavras(f) for f in FALHAS]
        # a FALHA sempre carrega {o}; o hook so' nos degraus 2 e 3
        ex = extra_o * (2 if d in (2, 3) else 1)
        if min(hk) + max(fa) < PISO_FALA[1]:
            falhas.append("ES16: cena 1 no degrau %d nao alcanca o piso (%d < %d)"
                          % (d, min(hk) + max(fa), PISO_FALA[1]))
        # ⚠️ `min(fa)` e nao `max(fa)`: a FALHA e' escolhida DENTRO do
        # orcamento (`_escolher` com predicado de piso e teto), entao o que
        # tem de caber e' a combinacao mais curta possivel com o hook mais
        # longo. Cobrar `max + max` reprovaria um pool saudavel — e' a §16,
        # lente que reprova o que esta' certo.
        if max(hk) + min(fa) + ex > TETO_FALA[1]:
            falhas.append("ES16: cena 1 no degrau %d pode estourar (%d > %d)"
                          % (d, max(hk) + min(fa) + ex, TETO_FALA[1]))

    # ⭐⭐ O TAKE 2 EM QUATRO BEATS — o piso e o teto por ENUMERACAO.
    # ⛔ A conta do contrato (8 mecanismo + 5 prova + 3 follow + 9 CTA = 25) e'
    # o ALVO; o que se cobra aqui e' a ARITMETICA REAL do pool, porque foi
    # exatamente uma conta de cabeca que deixou o motor de 24s com PISO 26
    # declarado acima do proprio TETO de 25 — par impossivel em que todo
    # sorteio viola um dos dois.
    # ⚠️ `extra_o` uma vez so': o mecanismo carrega UM `{o}`, os outros tres
    # beats nao carregam nenhum. O `{d}` custa 2 palavras nas tres formas
    # (`my husband's` / `my partner's` / `my man's`), entao ele nao tem extra.
    me = [_palavras(x.format(d="my husband's", o="Johnson"))
          for x in MECANISMOS16]
    p16 = [_palavras(x) for x in PROVAS16]
    f16 = [_palavras(x) for x in FOLLOWS16]
    c16 = [_palavras(x) for x in CTAS16]
    if max(me) + max(p16) + max(f16) + max(c16) < PISO_FALA[2]:
        falhas.append("ES16: cena 2 nao alcanca o piso (%d < %d)"
                      % (max(me) + max(p16) + max(f16) + max(c16),
                         PISO_FALA[2]))
    # ⭐ O teto NAO e' "a soma dos maximos" — o solver escolhe dentro do
    # orcamento. O que tem de caber e' a COMBINACAO MINIMA: se nem ela couber,
    # nao existe video legal e o fallback do `_cabe16` estoura em silencio.
    if min(me) + min(p16) + min(f16) + min(c16) > TETO_FALA[2]:
        falhas.append("ES16: cena 2 nao cabe nem na combinacao mais curta "
                      "(%d > %d) — o fallback do solver estoura o teto fisico"
                      % (min(me) + min(p16) + min(f16) + min(c16),
                         TETO_FALA[2]))

    # --- CT3/CT5/ES6/ES7, cobertura por ENUMERACAO dos pools do take 2 ------
    # ⛔⛔ A enumeracao saiu de FUNDIDAS (pool PARADO) e foi para MECANISMOS16,
    # que e' quem chega ao video. Lente apontada para pool morto e' lente que
    # imprime "OK" sobre o nada.
    for i, f in enumerate(MECANISMOS16, 1):
        baixo = f.lower()
        if "gelatin trick" not in baixo:
            falhas.append("ES6: MECANISMOS16[%d] sem o literal 'gelatin trick'" % i)
        if "{o}" not in f or "{d}" not in f:
            falhas.append("ES6: MECANISMOS16[%d] sem slot {o} ou {d}" % i)
        n_tec = sum(baixo.count(t) for t in ES7_TECNICAS)
        if n_tec != 1:
            falhas.append("ES7: MECANISMOS16[%d] com %d palavras tecnicas"
                          % (i, n_tec))
        # CT3 pela lente compartilhada, entrada por entrada — verbo de efeito e
        # ALVO na mesma sentenca do batismo. ⛔ Rotulo nu nao passa.
        prova = {"falas": ["", f.format(d="my husband's", o="pecker")
                           + " Comment gelatin, and the recipe goes to your "
                             "messages."]}
        ct3 = []
        sc.lint_copy16(sys.modules[__name__], prova, ct3, isca_absurda=False)
        for _n, msg in ct3:
            if msg.startswith(("CT3", "CT5", "CT7")):
                falhas.append("MECANISMOS16[%d]: %s" % (i, msg))
    # ⛔⛔ ES6 — O MARCADOR DE NEGACAO MORA NO POOL DE PROVAS16, TODAS AS 18.
    # No formato 16s a FALTA de verdade e' o CT2, do outro lado do corte; o
    # marcador dentro do take fica na prova, colado no mecanismo, sem gastar
    # palavra propria. Se alguem escrever uma prova sem negacao, a ES6 reprova
    # o video inteiro — e reprovaria por sorteio, um em dezoito, que e' o pior
    # jeito de descobrir.
    for i, p in enumerate(PROVAS16, 1):
        if not any(n in p.lower() for n in ES6_NEGACAO):
            falhas.append("ES6: PROVAS16[%d] sem marcador de negacao (%r) — e' "
                          "ela que sustenta a falta dentro do take" % (i, p))
    # ⛔ CT5 e CT6 no pool inteiro de CTAs: ingrediente na boca e CTA sem
    # endereco de entrega sao os dois defeitos que estavam em 100% do lote.
    for i, c in enumerate(CTAS16, 1):
        if sc.INGREDIENTES_16.search(c):
            falhas.append("CT5: CTAS16[%d] nomeia ingrediente — %r" % (i, c))
        if not sc.ENTREGA_16.search(c):
            falhas.append("CT6: CTAS16[%d] nao diz ONDE a receita chega — %r"
                          % (i, c))
        if sc.CTA_LITERAL not in c:
            falhas.append("ES12: CTAS16[%d] sem o literal %r"
                          % (i, sc.CTA_LITERAL))
    # ⛔ CT1 — o follow e' a penultima batida, nunca a ultima. Se uma entrada
    # de FOLLOWS16 trouxer um segundo pedido, o video passa a ter duas
    # chamadas e a ultima deixa de ser a que paga.
    for i, f in enumerate(FOLLOWS16, 1):
        if "comment gelatin" in f.lower():
            falhas.append("CT1: FOLLOWS16[%d] carrega o CTA — o pedido e' a "
                          "ULTIMA coisa do video, e mora so' no CTAS16" % i)
    for i, p in enumerate(PROVAS, 1):
        if "{o}" not in p["txt"]:
            falhas.append("ES16: PROVAS[%d] sem {o} — a prova ficaria sem "
                          "referente" % i)

    # --- ES9, o objeto da keyword tem de LER como gelatina ------------------
    # ⛔ O achado ③ e' a coincidencia palavra<->objeto. Um sache branco de po'
    # anonimo no frame de `comment gelatin,` le' como fermento, e ai' comando e
    # premio deixam de ser a mesma imagem.
    for m_ in MECANISMOS_PROP:
        for campo in ("plantado", "curto"):
            if "gelatin" not in m_[campo].lower():
                falhas.append("ES9: MECANISMOS_PROP['%s'].%s nao nomeia gelatina"
                              % (m_["id"], campo))

    # --- ES13, o marcador de autoridade/americanidade por FORMA -------------
    # ⚠️ A bandeira e' 2/2 na fonte e e' o UNICO marcador presente em 15/15 dos
    # nossos cenarios. O kit completo (estante + documentos com selo) so' existe
    # nos cenarios de escritorio — registrado na ES13 da doutrina em 2026-08-02,
    # que antes declarava o alibi como obrigatorio em todos.
    sem_bandeira = [c["id"] for c in CENARIOS if "US flag" not in c["set"]
                    or "US flag" not in c["re_ancora"]]
    if sem_bandeira:
        falhas.append("ES13: cenario(s) sem a bandeira dos EUA no set ou na "
                      "ancora: %s" % ", ".join(sem_bandeira))

    # --- ES5, a fisica tem de ser possivel com a receita --------------------
    magras = [r["id"] for r in RECEITAS if len(fisicas_de(r)) < 4]
    if magras:
        falhas.append("ES5: receita(s) com menos de 4 fisicas compativeis: %s"
                      % ", ".join(magras))

    # --- ES5, o ESCAPE tem de ser condicional ou pergunta -------------------
    # ⛔ Nao toca no degrau 1 (os hooks de la' nao dizem `your <nucleo>`): a
    # ordem [D3] do operador passa intacta. O que se cobra e' o ESCAPE.
    afirmativos = {}
    for d in DEGRAUS:
        pool_d = [h for h in HOOKS if h["degrau"] == d]
        maus = [h["txt"] for h in pool_d
                if _afirma_no_corpo(h["txt"].format(e="banana", f="donut",
                                                    o="Johnson"))]
        afirmativos[d] = maus
        if len(maus) == len(pool_d):
            falhas.append("ES5: TODOS os %d hooks do degrau %d afirmam sobre o "
                          "corpo do espectador — o degrau deixa de ser escape"
                          % (len(pool_d), d))

    # --- P22, quantos FECHOS aterrissam sozinhos ---------------------------
    # ⚠️ No degrau 4 nenhum dos hooks aterrissa, entao o pool efetivo de FECHOS
    # e' so' o que aterrissa. Medido por enumeracao para nao virar surpresa.
    fechos_p22 = [f for f in FECHOS if _aterrissa(f)]
    if len(fechos_p22) < 6:
        falhas.append("P22: so' %d de %d FECHOS aterrissam — no degrau 4 esse e' "
                      "o pool efetivo inteiro" % (len(fechos_p22), len(FECHOS)))

    # --- as 400 x N passadas ------------------------------------------------
    # --- as 400 x N passadas, TODAS medidas ---------------------------------
    # ⛔ Correcao de 2026-08-02: antes so' o modo default passava `freq`, e os
    # seis modos extras rodavam cegos — inclusive `--figurantes 2`, cujo segundo
    # rosto (`homem2`/`reacao2`) nunca foi medido por ninguem.
    rng = random.Random(seed)
    modos = ([(1, "separados", 1, "default (d1, separados, 1 figurante)")]
             + [(d, "separados", 1, "degrau %d" % d) for d in DEGRAUS if d != 1]
             + [(1, "montados", 1, "geometria montados"),
                (1, "separados", 2, "dois figurantes"),
                (2, "montados", 2, "degrau 2 + montados + dois figurantes")])
    medidas, soft = [], []
    print("SORTEIOS")
    for d, g, f, rotulo in modos:
        m = _nova_medida()
        e2, a2, n2 = _rodada(n_por_pagina, rng, d, g, f, m)
        print("  %-42s %d sorteios: %d ERRO, %d AVISO" % (rotulo, n2, e2, a2))
        if e2:
            falhas.append("%d ERRO de linter em %d sorteios (%s)"
                          % (e2, n2, rotulo))
        medidas.append((rotulo, m))
    for i, (rotulo, m) in enumerate(medidas):
        linhas = _imprimir_entropia(m, rotulo, falhas, completo=(i == 0))
        # ⚠️ o resumo soft leva o default INTEIRO e, dos modos extras, so' o que
        # e' PROPRIO deles (o hook do degrau de escape). Repetir sete vezes que
        # `counter` concentra 46% e' ruido, e ruido apaga sinal.
        soft += [x for x in linhas if i == 0 or x.startswith("copy:hook")]

    print("\nPOOLS DE COPY")
    print("-" * 72)
    for nome in sorted(copy):
        print("  %-12s %d" % (nome, copy[nome]))
    print("  HOOKS por degrau: %s"
          % ", ".join("d%d:%d" % (d, por_degrau[d]) for d in DEGRAUS))
    print("  HOOKS afirmativos sobre o corpo (ES5, fora do sorteio): %s"
          % ", ".join("d%d:%d" % (d, len(afirmativos[d])) for d in DEGRAUS))
    print("  FECHOS que aterrissam sozinhos (P22): %d de %d — e' o pool efetivo "
          "do degrau 4" % (len(fechos_p22), len(FECHOS)))
    print("  FISICAS compativeis por receita: %d-%d de %d"
          % (min(len(fisicas_de(r)) for r in RECEITAS),
             max(len(fisicas_de(r)) for r in RECEITAS), len(FISICAS)))
    print("  gates com 'brother': %d | gates com vocativo: %d de %d"
          % (n_brother, n_voc, len(GATES)))
    # ⚠️ ES19, medido em vez de suposto: a esperanca uniforme e' 2/15 = 13,3%, e
    # o filtro da P22 na cena 3 empurra para cima (dos 7 gates que aterrissam em
    # imperativo, 2 levam 'brother'). Registrado como AVISO, nao escondido: o
    # vicio que o operador mediu era de 31-73%.
    mdef = medidas[0][1]
    pc_b = 100.0 * mdef["vicio"] / mdef["n"]
    print("  'brother' na cena 3, medido: %d de %d = %.1f%%"
          % (mdef["vicio"], mdef["n"], pc_b))
    if pc_b > 15.0:
        print("  AVISO ES19: 'brother' acima de 15%% (%.1f%%) — o filtro da P22 "
              "favorece os gates imperativos, e 2 dos 7 levam o vocativo" % pc_b)

    # ⚠️ P22 MEDIDA POR CENA (2026-08-02). O AVISO por video existe e continua
    # existindo — ⛔ calar o medidor nao e' cobrar a regra —, mas ele saia em
    # ~68% do lote e um aviso que sai em dois tercos treina o operador a ignorar
    # TODO aviso, e ai' os avisos raros (ES8, ES9, ES20) morrem junto. A saida
    # honesta e' MEDIR: 11 das 16 FUNDIDAS e 0 dos 12 SELOS aterrissam em 2a
    # pessoa ou imperativo, entao a cena 2 nao tem como cumprir a P22 com o pool
    # de hoje. Fechar isso e' reescrever SELOS/FUNDIDAS = COPY = alcada do Ed.
    print("\nP22 — CENAS QUE NAO ATERRISSAM (2a pessoa ou imperativo)")
    print("-" * 72)
    for rotulo, m in medidas:
        print("  %-42s c1 %4.1f%% | c2 %4.1f%% | c3 %4.1f%%"
              % (rotulo, 100.0 * m["p22"][1] / m["n"],
                 100.0 * m["p22"][2] / m["n"], 100.0 * m["p22"][3] / m["n"]))
    print("  pools: %d de %d FUNDIDAS e %d de %d SELOS aterrissam"
          % (sum(1 for f in FUNDIDAS if _aterrissa(f)), len(FUNDIDAS),
             sum(1 for s in SELOS if _aterrissa(s)), len(SELOS)))

    # ⚠️ Registrado, nao escondido, e agora MEDIDO em vez de suposto. O calculo
    # antigo usava a esperanca uniforme (100/nº de hooks): para o degrau 3 dava
    # 16,7% e o AVISO nunca disparava, enquanto o medido e' 19,2%.
    if soft:
        print("\nAVISO ES22 — BARRA NAO CUMPRIDA EM EIXO DE STRING/COPY")
        print("-" * 72)
        for linha in soft:
            print("  ! %s" % linha)
        print("  Correcao = EDICAO DE POOL: `e_img` proprio por entrada de "
              "PARES, `curto`/")
        print("  `bancada` menos repetidos, NUCLEO de 7 para 9+, mais hooks nos "
              "degraus de")
        print("  escape. Copy e cena sao ALCADA DO ED — medido e registrado, "
              "nao corrigido.")

    print("\n" + "=" * 72)
    if falhas:
        for f in falhas:
            print("FALHA: %s" % f)
        print("SELF-TEST REPROVADO (%d falha(s))." % len(falhas))
        return 1
    print("SELF-TEST OK — a barra de entropia foi cumprida nos eixos por `id`;"
          " os eixos por STRING vao acima como AVISO.")
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
        description="Randomizador do agente ESCANDALO SHORT")
    ap.add_argument("--pagina", choices=sorted(ETNIA))
    ap.add_argument("--n", type=int, default=1)
    ap.add_argument("--seed", type=int, help="reproduzivel")
    ap.add_argument("--dry-run", action="store_true", help="nao grava ledger")
    # ⚠️ ES10/[D3]: a escolha do degrau e' ALCADA DO ED, e o DEFAULT E' 1 por
    # ordem explicita dele. Uma recusa custa esta flag, nao um redesenho.
    ap.add_argument("--degrau", type=int, choices=DEGRAUS,
                    default=DEGRAU_PADRAO,
                    help="a escada de moderacao do hook (ES10) — 1 🔴 o literal "
                         "da fonte (DEFAULT) | 2 🟡 | 3 🟢 na forma | 4 🟢")
    ap.add_argument("--geometria", choices=GEOMETRIAS, default=GEOMETRIA_PADRAO,
                    help="ES2 — separados (DEFAULT, o reel de 32,9K) | montados "
                         "(🔴, penetracao consumada no frame 1)")
    ap.add_argument("--figurantes", type=int, choices=FIGURANTES,
                    default=FIGURANTES_PADRAO,
                    help="ES1 — 1 (DEFAULT, o reel A) | 2 (o reel B; so' o "
                         "primeiro volta na cena 3)")
    ap.add_argument("--stats", action="store_true",
                    help="uso dos pools + self-test de entropia (ES22)")
    a = ap.parse_args()

    if a.stats:
        return stats()

    if not a.pagina:
        ap.error("informe --pagina <joe|ray|matt|marcus|chuck> (ou --stats)")

    rng = random.Random(a.seed)
    ledger = _carregar_ledger()
    saida = 0
    for i in range(a.n):
        spec = sortear(a.pagina, rng, ledger, {"degrau": a.degrau},
                       a.geometria,
                       a.figurantes)
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
