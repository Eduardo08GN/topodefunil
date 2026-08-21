#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ruth16_short.py — randomizador + gerador + linter do **RUTH 16**.

⭐⭐ O QUE ELE E': a **humilhacao publica** de uma pessoa obesa no take 1, o
**reencontro com a Ruth** no take 2 e a **receita + CTA** no take 3. TRES takes
de 8s (24s), destino AdBatch **Vertical 3**.

⛔⛔ ELE NAO E' IRMAO DOS 32 DE GELATINA. Rota propria, oferta propria:
**emagrecimento**, `KEYWORD_NATIVA = "recipe"`, e **nada de gelatina neste
motor** (ordem do operador). Quem publicar isto apontando para a VSL de
gelatina quebra a congruencia de proposito. Mesmo desenho do RARO 16.

FONTE: `facebook.com/profile.php?id=61589307140516` ("Ruth Yoder"), 60 posts
garimpados. ⭐ **A mediana da pagina inteira e' 48,5 comentarios por mil
views** — o melhor reel-fonte que este repo ja' modelou (o campeao dos sete do
BANHO 16 3T) fez 20,5, e era o TOPO, nao a mediana. O topo daqui faz 95,7.
Proposta e corte dos 15 em [`PROPOSTA-ruth16.md`](PROPOSTA-ruth16.md).

⛔ O CORTE E' LITERAL, e por isso da' para separar sem olhar: os videos de
humilhacao abrem em `This was <NOME> before, <o desastre>, <as testemunhas>.
Pure shame.` Os outros 44 sao receita, barriga em close ou pergunta-resposta.

===============================================================================
 ⭐⭐ O QUE A LEITURA OTICA DOS 15 PROVOU — e ela desmentiu a fonte
===============================================================================
Quinze reels lidos quadro a quadro, com folha de contato e transcricao. O
achado que mais vale nao e' sobre o que a fonte faz bem:

  1. ⛔⛔ **EM 7 DOS 15 NAO HA' TERCEIRO NENHUM EM QUADRO** — v24 (so' uma
     sombra na calcada), v39 (estacionamento vazio), v49 (so' o marido, que e'
     VITIMA), v40, v45, v47 e v59 (so' bombeiros e EMS, todos TRABALHANDO).
     E a fala promete `getting filmed and laughed at by the people around
     her` em SEIS deles. ⭐ Sem terceiro olhando, isto e' **acidente privado,
     nao vergonha publica** — o beat mais caro da formula existe so' no audio.
     ⛔ Por isso **toda entrada de `DESASTRES` aqui carrega TESTEMUNHA EM
     QUADRO por construcao**, e a lente `RU1` cobra isso por video. E' a
     correcao mais valiosa que a leitura produziu.
  2. ⛔⛔ **NINGUEM ESTA' FILMANDO em nenhum dos quinze.** A fala diz `filmed`
     e o quadro nunca tem um aparelho. ⭐ Aqui a palavra **`filmed` SAI da
     copy**: as testemunhas olham, viram a cabeca, apontam e riem — o que a
     imagem paga. E `phone`/`camera`/`filming` ficam **banidos da direcao de
     cena** (lente `RU5`), porque aparelho escrito vira aparelho DESENHADO —
     licao paga com um lote inteiro no VICK 16.
  3. ⭐⭐ **A ANCORA DE IDENTIDADE E' A PECA DE ROUPA, NAO O ROSTO** — e este
     e' o achado mais aproveitavel dos quinze. No v46 a mesma blusa floral
     atravessa os dois atos: apertada no corpo obeso, **caindo solta** no
     corpo magro. Ela e' ancora de continuidade E prova de emagrecimento no
     mesmo objeto. ⛔ Onde a fonte NAO tem ancora de roupa, ela troca de
     pessoa escancaradamente: v27 (loira de 35 vira grisalha de 55), v45 (o
     homem branco de barba curta vira hispanico), v28, v38.
  4. ⚠️ **E o rosto oculto no ato 1 nao e' regra: e' METADE.** Escondido em 6
     de 15 (v09, v15, v28, v38, v49, v51), totalmente visivel nos outros 9 —
     inclusive no v46, que e' o unico com testemunha de verdade em foco.
     ⛔ Variavel confundida vira EIXO, nunca palpite: `rosto_ato1` e' sorteado
     50/50 e pre-selecionavel no painel, para o campo responder o que a fonte
     nao responde. Mesma mecanica do `mecanismo` do BANHO 16 3T.
  5. ⚠️ **A Ruth perde os oculos no v49** e os tem no v46 e no v47 — mesma
     personagem fixa com acessorio inconstante. Por isso os oculos entram na
     **string travada** `RUTH`, e a lente `RU2` os cobra nos dois quadros do
     reencontro.

===============================================================================
 O QUE O OPERADOR DECIDIU
===============================================================================
  D1 TRES takes de 8s (24s), AdBatch **Vertical 3**, blocos `01/03`..`03/03`.
  D2 ⛔ `TETO_FALA = 25` por take — **8,0s x 3,1 palavras/s, os dois MEDIDOS**.
     Nao e' 14: o 14 do `banho16_3t` saiu de uma suposicao de take de 5s que a
     medicao desmentiu, e o proprio arquivo dele ja' registra a correcao.
  D3 Os tres atos: **1 A HUMILHACAO · 2 O REENCONTRO com a Ruth · 3 A RECEITA
     + CTA**. E' o corte que a fonte faz sozinha: em 12 dos 15 reels o
     `reencontro` e o `cta` ja' sao dois beats de fala distintos dentro do
     mesmo plano da varanda.
  D4 Agressao **IGUAL A' FONTE**: o guindaste, os bombeiros, o EMS, a cadeira
     do salao. Nada disso e' suavizado.
  D5 Rota de EMAGRECIMENTO. `KEYWORD_NATIVA = "recipe"`, `KEYWORD_UI = True`.
     ⛔ `yes` e `book` banidos (quebram a automacao de DM) — e a fonte pede
     `yes` em praticamente todos os 60. ⛔ E **nada de gelatina** (lente RU10).

===============================================================================
 OS EIXOS
===============================================================================
  DESASTRES  59 · o lugar + as testemunhas + o enquadramento JUNTOS numa
                  entrada so'. ⛔ Separar em quatro eixos daria mais
                  combinacao e MENOS nexo — e' a licao do VICK 16.
  PESSOAS    14 · nome + sexo + idade. ⭐ A fonte troca **so' o nome** e
                  republica o mesmo roteiro (Betsy/Betty na mesma cadeira,
                  Marjorie/Marilyn na mesma rampa) — e' o eixo mais barato que
                  existe, e o nome atravessa os tres takes.
  REENCONTROS 8 · o lugar do ato 2 (varanda, deck, botica, gramado).
  ROUPAS     10 · ⭐⭐ a PECA ANCORA, apertada no take 1 e solta no take 2.
  ROSTOS     14 · a arquitetura facial do BLOCO 0 (REF).
  PARCEIROS   4 · o marido, so' quando o desastre e' de casal.
  A COPY        · ABERTURAS (5 formas) · BEATS_TESTEMUNHA (6 formas) · PROVAS (5
                  formas), cada beat marcado com `forma` e a distribuicao
                  MEDIDA no autoteste.

⛔⛔ **POOL DE UMA FORMA SO' NAO E' POOL** — licao do RARO 16, onde eu escrevi
oito hooks e os oito eram pergunta, e quem viu foi o operador, na tela. ⚠️ Aqui
o risco e' maior, porque a assinatura da fonte E' uma forma so' (`This was X
before` em 11 de 15). Por isso as outras quatro formas de abertura **nao sao
invencao**: sao sentencas que a propria fonte diz DENTRO dos mesmos videos,
promovidas a' posicao de abertura (`This was Janet's everyday reality` do v24,
`unable to move because of her size` do v59, `this is what she faced every
single day` do v09, `getting out of the car was already a struggle` do v24).

⭐ E o sorteio **escolhe a FORMA antes do resultado** (RARO 16): num sorteio
filtrado por orcamento, entrada CURTA e' entrada favorecida, e a forma vira
peso sem ninguem ter pedido. Se o eixo que importa e' a forma, e' a forma que
se sorteia.

===============================================================================
 ⛔⛔ O CUSTO CENTRAL: A MESMA PESSOA, OBESA E DEPOIS MAGRA
===============================================================================
E' a continuidade mais cara que este parque ja' pediu — mais cara que as tres
pessoas do ALFA 16, porque aqui o corpo **muda de proposito** e so' a
identidade tem de permanecer. Tres defesas, todas em codigo:

  1. **BLOCO 0 (REF) = o ROSTO**, e os tres IMAGE repetem a ancora por extenso
     (lente `RU4`).
  2. ⛔⛔ **A ANCORA SO' CITA TRACO QUE O PESO NAO MOVE** — olhos (formato e
     distancia), sobrancelha, ponte do nariz, orelha, sinal permanente,
     corte de cabelo. **Maxilar, bochecha, papada e queixo ficam DE FORA**:
     eles mudam com o peso, e uma ancora que os cita obriga o gerador a
     escolher entre a ancora e a magreza — e ele escolhe contra nos.
  3. ⭐⭐ **A PECA DE ROUPA**, o achado do v46: a mesma peca nos tres quadros,
     esticada no primeiro e **pendurada solta** nos outros dois (lente `RU3`).

⛔ E NENHUMA COR DE PELE, DE OLHO OU DE CABELO nos pools: a etnia vem da
PAGINA (congruencia inviolavel), e duas vozes decidindo o mesmo sintagma o Veo
resolve inventando — defeito FT14 do FIGHT 16.

===============================================================================
 ⛔⛔ O LOTE REPROVADO DE 2026-08-21 — a lente que media a FORMA e matou a FUNCAO
===============================================================================
O operador gerou um lote, olhou o mp4 e reprovou: *"nao esta' gerando
personagens obesos, inclusive alguns parecem ate' magros"* e *"as cenas de
humilhacao nao estao fazendo sentido logico visual nenhum [...] esta' com
drifting logico: quem ve' fica WTF???"*.

⛔ O bloco que produziu aquilo gastava **CATORZE PALAVRAS** no corpo, e todas
adjetivo: *"a very heavy 39-year-old white American woman [...] and with her a
very heavy husband in a black t-shirt. They are both wide through the
middle."* **O gerador nao desenha adjetivo** — ele desenha FORMA, AREA DE
QUADRO e COMPARACAO. Sem as tres ele volta para a media do treino, que e' uma
pessoa comum. Foi exatamente o que voltou.

⚠️⚠️ **E A CAUSA IMEDIATA FOI UM CONSERTO MEU, NA MANHA DO MESMO DIA.** A
varredura adversarial achou `very heavy` repetido de duas a quatro vezes por
bloco, eu **enxuguei os catorze `porte`** para matar a repeticao, medi
*"1200 -> 0"* e dei por consertado. Matei a repeticao e matei a obesidade
junto. **§41 das licoes de construcao na forma mais cara: verificar a FORMA e
destruir a FUNCAO.** A `RU14` contava o ADJETIVO, entao a saida mais barata
para passar nela era tirar peso da descricao — lente mal desenhada empurra o
conserto para o lado errado.

⭐⭐ **O QUE ENTROU:** a ARQUITETURA DO CORPO em SEIS ELEMENTOS (bloco
`PESSOAS`), ~180 palavras no take 1 e so' nele; a `RU20`, que cobra NA SAIDA
MONTADA um numero de peso, uma clausula de POSICAO NO QUADRO e uma de
COMPARACAO; e a `RU14` reescrita para contar SINTAGMA DE PESSOA e nao
adjetivo, com controle negativo dos dois lados (descricao longa do MESMO corpo
passa; `the very heavy customer` acusa).

⛔ **E A CADEIRA DE RODAS VAZIA SAIU DO `escada_varanda`:** era o maior objeto
do canto inferior do quadro e contava OUTRA historia (deficiente que caiu da
cadeira), roubando do corpo a explicacao da queda.

===============================================================================
 ⭐⭐ A VARREDURA ADVERSARIAL DE 2026-08-21 — o que ela achou e o que ela custou
===============================================================================
Tres verificadores mediram este motor com lentes diferentes um dia depois de ele
nascer. **Vinte e um achados, todos reproduzidos rodando o comando da
evidencia** — e o que eles tem em comum vale mais que qualquer um deles:

  ⛔⛔ **NENHUM defeito apareceu como ERRO de lente.** O `--autoteste` imprimia
  `0 ERRO, 0 AVISO` sobre 400 videos em que 100% dos blocos nomeavam o corpo
  duas a quatro vezes, 46% tinham a direcao de cena no genero errado, 32%
  pediam `both figures` num quadro de tres pessoas e 21% punham o casal em dois
  lugares ao mesmo tempo. ⭐ **Treze lentes, e o que elas cobravam era a
  PRESENCA das pecas certas — nunca a CONSISTENCIA do bloco montado.**

O que entrou por causa disso:

  · **Cinco lentes novas** — `RU14` (um corpo, um sintagma), `RU15` (geometria
    do casal), `RU16` (silencio na fala exige silencio no quadro), `RU17` (a
    direcao de cena concorda com o elenco) e `RU18` (o CT5 nas TRES falas).
    ⭐ E uma sexta em 21/08, da varredura de moderacao: `RU19` (a peca-ancora
    e' a UNICA no corpo de quem o video apresenta).
  · **`RU3`, `RU4` e `RU5` cresceram**: peca fantasma, rosto no `porte` com a
    camera de costas, e o bloco INTEIRO em vez de dois tercos dele.
    ⚠️ A `RU4` cresceu de novo em 21/08 (fim do dia): ela varria o campo
    `porte` sozinho, e a arquitetura nova tem SEIS campos de corpo — hoje ela
    le' o BLOCO DE CORPO MONTADO, do elemento 1 ao 6.
  · **O sorteio mudou de regra** (`_sortear_plano`): a entrada e' sorteada
    ANTES do orcamento, e o prazo virou exclusivo por fala.
  · **O painel virou medicao**: cadeado e botao `trocar` contados eixo por eixo
    no autoteste, mais uma varredura sob as travas de `sexo` e `rosto_ato1`.
  · **O motor entrou nos medidores** de que estava fora (quatro dos sete).
  · **`main()` nao imprime mais video reprovado**: re-sorteia ate' 12 vezes.

===============================================================================
 ⭐⭐ A VARREDURA DE MODERACAO DE 2026-08-21 — o pool `DESASTRES`, com 3 lentes
===============================================================================
Tres lentes (classificador de conteudo · gerabilidade no Veo · verdade da cena)
sobre as 59 entradas. **Sete cortadas** (cada uma com lapide no lugar) e **25
achados TIER 1 aplicados** sobre as 52 que ficaram — e, no mesmo dia, **dez
entradas de reposicao**, que levam o pool a **62** (bloco proprio mais abaixo).

  ⛔⛔ **A ANCORA DE ROUPA QUEBRAVA EM UMA ENTRADA, E ERA A PECA MAIS CARA DO
  MOTOR.** A `avental_costas` punha a pessoa de avental de papel, e o MESMO
  paragrafo ja' dizia `wearing a cream blouse [...] stretched tight across the
  back`. O gerador escolhe UMA; se escolhe o avental, o take 2 (`the same cream
  blouse, now hanging loose`) fica sem referente e a continuidade do angulo
  morre naquele video. ⭐ Entrou a lente **`RU19`** — e o caro nela nao e'
  acusar, e' SEPARAR TRES DONOS: roupa no corpo dela (ERRO), roupa em terceiro
  (`six patients in paper gowns`, `tomografo_estreito`) e roupa em movel (`a
  chrome return rack hung with dresses and jeans`, `provador_loja`). ⚠️ As duas
  ultimas foram ACUSADAS por um revisor humano e as duas estao CERTAS: sao os
  controles positivos da lente. Medido: 55 pares (desastre x peca) no bloco
  montado, 1 defeito, 52 de 52 desastres varridos e 0 acusados — e **62 de 62**
  depois das dez entradas de reposicao, tambem com 0 acusados.

  ⛔ **O CLUSTER B CULPAVA UM VILAO EXTERNO em 8 das 11 entradas** (gelo, oleo,
  piso molhado, azulejo, faixa pintada, pente da escada rolante). Quem cai no
  gelo e' qualquer um — o video deixava de ser *This was <NOME> before* e virava
  acidente com reu. Nas nove LIDAS nenhuma nomeia perigo. ⚠️ E o vilao saiu do
  `cen`, do `cam`, da `luz` e do `audio` junto: bloco que tira a causa e mantem
  o gelo na trilha e' o defeito do VICK 16.

  ⛔ **O CLUSTER E TINHA UM DEFEITO DE LOTE:** 11 de 11 entradas abriam o `mov`
  no mesmo gesto — um uniformizado de braco ou palma estendidos. Onze videos com
  o mesmo movimento no mesmo segundo nao sao onze videos. O funcionario fica em
  quadro; o primeiro beat e' do PUBLICO.

  ⚠️ **TIER 2 (11 colapsos de par) NAO foi aplicado**: e' curadoria de pool, nao
  defeito de video, e a decisao e' do operador.

⭐⭐ **AS DEZ ENTRADAS DE REPOSICAO (2026-08-21, no mesmo dia).** As sete
cortadas voltaram como **dez**, e o pool foi de 52 a **62**: B 10->12, C 6->9,
D 8->10, E 7->10 (o A fica em 12 e as nove LIDAS em 9). ⛔ Nenhuma repete o
defeito de classe que derrubou as sete: a causa e' sempre o CORPO (nao ha' gelo,
oleo nem piso molhado em `acao` nenhum), o `mov` abre sempre num CIVIL e a
maquina, quando existe, tem operador identificado nos comandos.

  ⛔⛔ **UMA REGRA DE CLUSTER MUDOU, e esta escrita no lugar onde a proxima
  entrada vai nascer.** O cluster C proibia `impotencia` no bloco inteiro, com
  razao: *and nobody there could lift them* sobre um guincho erguendo em quadro
  e' a fala desmentindo o quadro. ⭐ Mas ela NAO desmente quando o `test` mostra
  os civis que **tentaram primeiro e desistiram** (os quatro homens de mangas
  arregacadas do `carregadeira_feira`, o homem de fleece do `bolsa_ar_calcada`):
  ai' a maquina e' a CONSEQUENCIA da impotencia. ⛔ Sem esse beat de tentativa
  fracassada no `test`, a forma continua proibida no cluster.

  ⚠️ **E UMA LENTE ENCOLHEU DE PROPOSITO, por FALSO POSITIVO MEDIDO.** O
  contador de existencia por eixo rodava nas 400 seeds fixas. Com 62 desastres a
  media por entrada e' 6,5 e a chance de UMA das 62 nao sair por puro acaso e'
  ~9%: o autoteste acusou `balanco_varanda` de estar MORTA (§35) sobre uma
  entrada que sai **22 vezes em 2.000 sorteios**. So' o eixo `desastre` passou a
  ser medido nos 2.000 — os mesmos que o ALCANCE POR DESASTRE ja' fazia, entao o
  custo e' zero. As 400 seeds continuam sendo a regressao de todo o resto.

  ⏳⏳ **E O NUMERO QUE A EXPANSAO NAO CONSERTOU, dito em vez de escondido.**
  Medido em 2.000 sorteios (amostra com poder, nao as 400): o alcance MINIMO de
  `BEATS_TESTEMUNHA` era **de3=25 (0,24x da media)** no commit 5a76d76, caiu a
  **21 (0,20x)** com os sete cortes e voltou a **25 (0,24x)** com as dez novas.
  ⛔ As dez **repuseram** o que os cortes tiraram e **nao melhoraram** o piso. A
  causa e' ACOPLAMENTO e esta' medida: `de3` e' a forma `dedo`, que exige
  VIZINHO em quadro (os tres beats dizem `neighbour` / `across the street`), e
  so' UMA das dez — a `talha_garagem`, numa garagem de suburbio com nove
  vizinhos na calcada — comporta a forma. `dedo` foi de 11/59 para **12/62** do
  pool, que e' o mesmo 19%. ⛔ Nao forcei `dedo` nas outras nove: parque de
  exposicoes, calcada de centro, feira e enfermaria nao tem vizinho, e rotulo
  que o quadro nao paga e' o que a RU6 existe para impedir. **Subir esse piso
  pede CENA DE VIZINHANCA nova, e cena e' alcada do operador.**
  ⭐ O que subiu: a razao max/min da abertura foi de 2,5x para **2,1x** e a da
  testemunha de 11,4x (pos-corte) para **9,4x**.

⏳⏳ **O QUE FICOU ABERTO — ALCADA DO OPERADOR, com o numero medido ao lado.**
Nada disto e' esquecimento: sao decisoes de COPY e de CENA, e a regra do repo e'
sugerir, nunca trocar.

  A. ⏳ **O ATO 3 NAO TEM RECEITA EM QUADRO.** Medido: o IMAGE 03 difere do
     IMAGE 02 em UMA sentenca — a palma erguida e a cabeca virada. Nenhuma
     tigela, caneca, jarro ou papel na mao de ninguem, em 300 de 300 sorteios.
     O `D3` chama o ato 3 de *"A RECEITA + CTA"* e visualmente ele e' o ato 2
     com um gesto novo. ⭐ Um objeto so' — o copo pronto na mao da Ruth, o
     papel dobrado — separaria os dois quadros, e e' o unico beat que o CT5
     permite MOSTRAR sem nomear ingrediente.
  B. ⏳ **A RUTH NAO TEM ARQUITETURA FACIAL NEM ETNIA ESCRITA.** Medido: a
     constante `RUTH` tem UM traco de rosto (`a deeply lined face`) contra os
     cinco de cada entrada de `ROSTOS` (olho, sobrancelha, nariz, orelha,
     sinal). O cabecalho diz *"ela aparece identica nos 15 reels"* e *"sortear
     a Ruth seria trocar a marca"* — hoje quem sorteia a Ruth e' o gerador, a
     cada video. ⛔ Nao inventei o rosto dela: inventar a marca e' exatamente o
     que a frase acima proibe. A `RU2` cobra tres pecas de ROUPA e passa a
     cobrar os tracos no dia em que eles existirem.
  C. ⭐⭐ **AS ENTRADAS LONGAS DE COPY CABIAM EM POUCOS DESASTRES — E E' ISSO
     QUE A EXPANSAO DE 2026-08-21 EXISTE PARA CONSERTAR.** O conserto do
     sorteio tinha nivelado o que dava (a `vi7` foi de 6 para 31 em 400, a
     `im2` de 4 para 10) e o resto era aritmetica: com um beat de desastre de
     13 palavras, o orcamento de abertura+testemunha e' **10**, e a menor
     abertura (4) com a menor testemunha (5) ja' gasta 9. A saida era de COPY
     — encurtar um lado ou o outro — e o operador escolheu a terceira: **dar
     ao motor CINQUENTA beats de desastre novos**, a maioria de 6 a 8
     palavras, para as entradas longas passarem a caber.
     ⭐ MEDIDO nas mesmas 400 seeds, antes e depois:
         ABERTURAS         min 2 (`di3`) -> **10**, e a propria `di3` foi a 17
         BEATS_TESTEMUNHA  min 4 (`de3`) ->  **5**, e a propria `de3` foi a 7
     A abertura funcionou; a testemunha quase nao se moveu, e a causa esta'
     medida na alinea F — o que trava `de3` deixou de ser orcamento e passou a
     ser ACOPLAMENTO. O autoteste imprime os quatro numeros lado a lado e
     REPROVA o motor se o minimo nao subir.
  D. ⏳ **4 DAS 14 PESSOAS SAO ANONIMAS E ABREM EM PRONOME** (122 de 400
     videos): *"This was her before"*, *"Nothing was simple for them"*. E'
     desenho declarado e verbatim do v28 — e e' tambem o unico lugar do motor
     onde o take 1 nao tem referente proprio. Vale a pena o operador olhar um
     desses videos na tela antes de o lote sair.
  E. ⏳ **AS CINQUENTA CENAS NOVAS NAO TEM LEITURA OTICA POR TRAS.** Elas saem
     do GRAFO que o operador desenhou (ver o cabecalho de `DESASTRES`), e a
     excecao a' regra *"pool so' cresce de video lido"* esta' declarada la'. As
     NOVE primeiras seguem sendo as unicas com `v` de reel. ⛔ Se o campo
     reprovar uma cena nova, ela nao tem reel para defende-la.
  F. ⏳ **`dedo` E' AGORA A FORMA MAIS ESCASSA — 12 de 59 desastres (20%), 6%
     dos videos.** Os tres beats dela dizem literalmente `neighbour(s)`, e a
     varredura de coerencia a tirou de QUATRO cenas do cluster A onde o
     publico e' cliente de balcao, convidado de festa em salao alugado ou
     PARENTE no proprio deck — *"and the neighbours pointed at her"* sobre a
     familia dela e' o teste WTF reprovando. ⭐ Decisao certa e ela custa
     alcance: e' por isso que o minimo de `BEATS_TESTEMUNHA` (a `de3`) quase
     nao subiu com a expansao. ⛔ Saidas, as duas de CENA e portanto do
     operador: escrever cenas de VIZINHANCA no proximo lote, ou aceitar que a
     forma fique nos 6%. O autoteste imprime `desastres por forma` justamente
     para essa divida ter numero em vez de impressao.

⚠️ E **o que a varredura NAO conseguiu me fazer consertar sozinho** esta' escrito
onde acontece: a `cctv_calcada` e a `rampa_medico` prometiam na FALA coisas que
o quadro nao pagava (uma crianca, as pernas cedendo). ⭐ Consertei pelo lado da
CENA, nao da copy — a crianca entrou no carrinho, as pernas entraram no `acao` —
porque a fala e' o que converte e a imagem e' o que se ajusta a ela.

===============================================================================
 ⚠️ RISCOS DITOS UMA VEZ
===============================================================================
**Moderacao.** Isto e' humilhacao explicita de pessoa obesa, com terceiros
rindo em quadro. O operador autorizou *"igual a' fonte"*, e a fonte roda — mas
ela tambem declara `#syntheticperformer` e carimba `genaicontent` no video.
**Fidelidade.** A fonte e' gerada por IA e os quinze videos tem defeito de
continuidade grosseiro (a cadeira que se conserta sozinha, o cabo que nunca
arrebenta, o relogio do CCTV congelado). Nada disso e' modelo: o que se copia
e' o ARCO, nunca o artefato.

Uso:
    python funil-organico/ruth16_short.py --pagina joe --n 1
    python funil-organico/ruth16_short.py --autoteste
"""

import argparse
import collections
import io
import json
import os
import random
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
if AQUI not in sys.path:
    sys.path.insert(0, AQUI)

import short_comum as sc                                        # noqa: E402
from nucleo_sonoro import sonorizar                             # noqa: E402

TITULO = "AGENTE RUTH 16"
SLUG = "ruth-16"
SUBTITULO = ("3 takes de 8s = 24 segundos · a humilhacao publica, o reencontro "
             "com a Ruth e a receita · rota de EMAGRECIMENTO, sem gelatina")

LEDGER = os.path.join(AQUI, ".ruth-16-ledger.json")

CENAS_UI = ["1 · A HUMILHACAO", "2 · O REENCONTRO", "3 · A RECEITA + CTA"]

# ⛔⛔ OS NOMES DOS BLOCOS SAO CONSTANTES, e isso e' conserto de um defeito real
# do BANHO 16 3T: as lentes herdadas varriam a tupla literal `("IMAGE 01/02",
# "IMAGE 02/02")` e, depois da cirurgia temporal, acusaram 7 ERROS num video
# CERTO. Lente que varre nome literal apodrece na primeira mudanca de formato.
IMAGENS = ("IMAGE 01/03", "IMAGE 02/03", "IMAGE 03/03")
TAKES = ("TAKE 01/03", "TAKE 02/03", "TAKE 03/03")

# ⛔⛔ O TETO E' DERIVADO, NAO DECLARADO (D2). `SEGUNDOS_TAKE x TAXA_MEDIA`:
# quando o relogio mudar, o teto muda junto. Numero escrito na mao nao
# sobrevive a' proxima cirurgia temporal — foi o que aconteceu com o 14 do
# `banho16_3t`, que saiu de uma suposicao de take de 5s.
SEGUNDOS_TAKE = 8.0
TAXA_MEDIA = 3.1
TETO = int(round(SEGUNDOS_TAKE * TAXA_MEDIA))        # 25
TETO_FALA = {1: TETO, 2: TETO, 3: TETO}

# ⭐ PISO = o MINIMO REAL que os pools deste motor produzem, medido e nao
# chutado. Piso calibrado no chute vira alarme que sempre dispara, e alarme que
# sempre dispara ensina o operador a ignorar o linter inteiro.
PISO_FALA = {1: 15, 2: 16, 3: 14}


def segundos_de(fala, taxa=TAXA_MEDIA):
    """Quanto tempo esta fala ocupa, na taxa pedida."""
    return len([p for p in str(fala).split() if p]) / float(taxa)


# ⛔ A etnia vem da PAGINA, nunca do sorteio: congruencia inviolavel do funil.
ETNIA = {
    "joe": "white American", "ray": "white American", "matt": "white American",
    "marcus": "Black American", "chuck": "Black American",
}

PELE_TRAVAVEL = False
MODOS_DEFAULT = ()

# ⛔ Este angulo NAO nomeia orgao nenhum: a falha e' o PESO, e o corpo em
# quadro e' a prova. `NUCLEO` vazio desliga a cota do orgao e o CT4/CT4b por
# construcao, em vez de por excecao — mesmo desenho do RARO 16.
NUCLEO = ()

BANIDOS_CTA = {"book": "quebra a automacao de DM",
               "yes": "quebra a automacao de DM — e e' a palavra que a fonte "
                      "pede em praticamente todos os 60 posts",
               "gelatin": "esta rota e' de emagrecimento e nao usa gelatina"}
BANIDOS_IMAGE = {}
BANIDOS_TAKE = {}
BANIDOS_BLOCO = {}

CTA_LITERAL_BASE = "Comment recipe,"
KEYWORD_UI = True
KEYWORD_NATIVA = "recipe"


# ===========================================================================
# ⛔⛔ A RUTH — CONSTANTE, NAO EIXO
# ===========================================================================
# Ela e' a assinatura da pagina: aparece identica nos 15 reels e e' a unica
# pessoa que atravessa a pagina inteira. Sortear a Ruth seria trocar a marca.
# ⚠️ OS OCULOS ESTAO NA STRING POR MEDICAO: o v49 a mostra SEM oculos nos dois
# quadros de fechamento, enquanto o v46 e o v47 a mostram com aro dourado. A
# leitura otica registrou isso como defeito e pediu literalmente que, se o
# angulo virasse motor, os oculos entrassem na string travada do REF.
RUTH = ("an Amish woman in her eighties with a deeply lined face, round "
        "wire-rimmed glasses, a white organdy prayer cap tied over grey hair, "
        "a cream long-sleeved blouse buttoned at the collar with the cuffs "
        "rolled back, a grey linen pinafore apron dress down to the ankle "
        "with two patch pockets, and black leather lace-up oxford shoes")

# ⛔ A prova de que a lente RU2 procura, e ela e' de FUNCAO e nao de literal:
# tres pecas que so' existem nela. Lente colada na string inteira acusa a si
# mesma na primeira reescrita — foi o que a BA1 do BANHO 3T pagou.
RUTH_PROVAS = ("prayer cap", "pinafore apron", "wire-rimmed glasses")


# ===========================================================================
# ⭐⭐ OS SESSENTA E DOIS DESASTRES — o eixo principal
# ===========================================================================
# ⛔⛔ DUAS PROCEDENCIAS, E ELAS NAO SE MISTURAM. As NOVE PRIMEIRAS saem de
# LEITURA OTICA dos 15 reels de humilhacao publica da "Ruth Yoder" e carregam
# o `v` do reel de origem (`v28/v40/v45`, `v46/v50`, ...). As CINQUENTA E
# TRES seguintes, agrupadas por cluster logo abaixo, saem do GRAFO CONCEITUAL que o
# operador desenhou em 2026-08-21 — cinco nos (falencia estrutural ·
# vulnerabilidade fisica · espetacularizacao da ajuda · rota medica ·
# nao-encaixe) ligados por tres arestas (gravidade · olhar do outro ·
# desumanizacao) — e carregam `v` no formato `grafo-<CLUSTER>` mais o campo
# `cluster`. Carimbo de proveniencia de GRAFO nunca vira carimbo de reel.
#
# ⚠️⚠️ E ISSO E' UMA EXCECAO DECLARADA A' REGRA *"pool so' cresce de video
# lido"*. A regra vale para FALA VERBATIM — a copy que converteu em campo nao
# se inventa, e nenhuma das 50 traz fala nova de abertura, de testemunha, de
# virada ou de CTA: elas trazem CENA, e o beat de desastre que a acompanha e' a
# mesma forma sem sujeito conjugado das nove lidas. Quem gerou as cenas foi o
# OPERADOR, dando a regra generativa (os cinco nos e as tres arestas); eu
# executei a regra dele. ⭐ Precedente do parque: o `bed16`, cujos pools de
# fala sao construcao nossa sob contrato porque o reel-fonte nao baixa — la' a
# divida esta' declarada no cabecalho e aqui tambem.
# ⏳ DIVIDA DECLARADA: nenhuma das 50 tem leitura otica por tras. Se o campo
# reprovar uma cena, ela nao tem reel para defende-la.
#
# ⛔ CADA ENTRADA ARRASTA O LUGAR + AS BEATS_TESTEMUNHA + O ENQUADRAMENTO
# JUNTOS.
# Separar em quatro eixos daria mais combinacao e menos nexo: e' a licao do
# VICK 16, onde sete eixos empilhados deram 0 ERRO em 600 sorteios e um video
# que o operador reprovou olhando (*"elementos visuais sem nexo"*).
#
# ⛔⛔ TODAS TEM TESTEMUNHA EM QUADRO, E EM SETE DAS NOVE ISSO E' CORRECAO DA
# FONTE, NAO COPIA DELA. A leitura otica achou o mesmo buraco em v24, v39,
# v49, v40, v45, v47 e v59: a fala promete plateia e o quadro entrega
# socorrista trabalhando, ou ninguem. Bombeiro e' testemunha de AUTORIDADE (o
# desastre e' grave o bastante para chamar o 911), nao testemunha de VERGONHA
# — sao dois papeis, e a fonte confunde os dois. Aqui o terceiro que OLHA
# existe sempre, e a lente RU1 o cobra.
#
# ⛔ `cam` descreve ANGULO e ALTURA, nunca aparelho e nunca por negacao.
# ⚠️ `fala` e' o beat do desastre no take 1 e e' escrito SEM SUJEITO
# CONJUGADO (o evento e' o sujeito, ou o verbo e' modal/passado): o mesmo pool
# serve `she`, `he` e `they` sem quebrar concordancia. `acao` segue a mesma
# regra, e por isso nenhuma das nove precisa de variante de numero.
# ⛔⛔ A CENA MUDA (`test_q` / `mov_q` / `audio_q`) — DEFEITO MEDIDO EM
# 2026-08-21, e ele desmentia o cabecalho deste proprio pool.
# O beat `silencio` (*"and nobody said a word"*, *"and the people there watched
# in total silence"*) so' existe em DOIS desastres — `cadeira_salao` e
# `reabilitacao` — e os DOIS tem riso escrito no `test`, no `mov` e, num deles,
# no `audio`. Medido em 400 sorteios: **21 de 21** videos com a forma
# `silencio` saiam sobre uma imagem que RI. Fala que desmente o proprio quadro
# e' exatamente o defeito que a leitura otica achou em seis dos quinze reels da
# fonte, invertido — e o comentario acima ja' declarava esse conserto feito.
# ⭐ A saida NAO foi matar a forma (`silencio` e' verbatim do v46/v50 e o
# autoteste reprovaria o pool com uma forma que nunca sai): foi dar aos dois
# desastres uma variante MUDA do mesmo quadro. Mesmo lugar, mesmo elenco,
# mesma contagem de pessoas — muda o GESTO (a mao sobre a boca no lugar do
# riso) e o audio. ⚠️ Quando os campos `_q` faltam, a lente `RU16` reprova a
# combinacao antes de ela chegar ao operador.
#
# ⚠️ `formas` declara quais formas de TESTEMUNHA cabem naquele quadro —
# `plateia` (todo mundo virou a cabeca) so' existe onde ha' sala cheia, e
# `dedo` so' onde ha' vizinho. Par que nao existe no mundo nao e' variedade,
# e' ruido; a lente RU6 cobra o par e o autoteste planta o proibido.
DESASTRES = [
    {"id": "guindaste_parede", "curto": "o guindaste arranca pela parede",
     "v": "v28/v40/v45", "sexos": ("mulher", "homem"),
     "formas": ("riso", "dedo", "juizo", "impotencia"),
     "interior": False,
     "cen": "the side wall of a two-storey American house on a bright summer "
            "day, cream lap siding with a rough rectangular hole torn open "
            "through the upper floor, splintered raw framing and loose boards "
            "hanging down over the siding, a black articulated hydraulic crane "
            "arm crossing the top of the frame with a red hook block on a "
            "chain, a red fire engine at the kerb, a wooden privacy fence and "
            "a mowed lawn below",
     "acao": "the yellow nylon sling has torn through at the hook block and "
             "the body has just come down into the grass still wrapped in "
             "the webbing, one fist still closed on the strap, the frayed "
             "end swinging back up toward the torn opening and boards "
             "dropping out of the hole behind it",
     "test": "on the lawn, four neighbours have come across from the next "
             "house and stand in a loose ring a few paces back, close enough "
             "to read: two men in green work shirts openly laughing with "
             "their heads tipped together, an older woman in a lilac "
             "cardigan with a flat hand over her mouth, and a man in a red "
             "ball cap with his arm out pointing straight down at the "
             "webbing",
     "mov": "As the line begins one fist hauls down on the yellow strap and "
            "an elbow drives into the grass to lift the shoulders. Halfway "
            "through the line the webbing slides through the fingers and the "
            "shoulders go back down into the sling. As the line ends the two "
            "men in green work shirts laugh out loud and the man in the red "
            "ball cap swings his pointing arm further out",
     "cam": "The shot is taken from the lawn at hip height, angled about "
            "thirty degrees upward along the wall so the torn opening, the "
            "crane arm and the body on the grass all sit in the same vertical "
            "frame",
     "luz": "Hard high summer sun from the upper left, crisp shadows thrown "
            "flat across the pale siding, cloudless sky.",
     "audio": "an idling diesel engine, a hydraulic whine, boots on grass and "
              "several people laughing and talking over each other"},

    {"id": "guindaste_sala", "curto": "o guindaste de oficina na sala",
     "v": "v27/v47", "sexos": ("mulher", "homem"),
     "formas": ("riso", "plateia", "juizo", "impotencia"),
     "interior": True,
     "cen": "the cluttered living room of an old single-wide farmhouse in "
            "winter, a cream popcorn ceiling, a brass ceiling fan with dusty "
            "blades, tan wood-panel walls, a brown leather sofa, a floral area "
            "rug over speckled linoleum, a lace-curtained window with flat "
            "grey daylight, and a polished steel shop hoist with an orange "
            "hydraulic ram standing in the middle of the floor",
     "acao": "the orange hydraulic ram has just taken the whole load and "
             "both feet have come up off the floral rug, the black nylon "
             "straps drawn bar-tight under the arms with both hands clamped "
             "onto them, the polished steel mast leaning as two firefighters "
             "in tan bunker gear brace it",
     "test": "crowded into the doorway behind the hoist stand four "
             "neighbours who came in off the street and never left: two men "
             "in quilted flannel jackets laughing with their shoulders "
             "shaking, a teenager in a grey hoodie grinning wide, and an "
             "older man in a brown cardigan with both hands on the door "
             "frame staring straight at the sling",
     "mov": "As the line begins both hands haul down on the black straps and "
            "a knee comes up hunting the mast to push off. Halfway through "
            "the line the grip slides down the nylon and the whole load "
            "swings back into the straps with the feet still off the rug. As "
            "the line ends the two men in quilted flannel jackets laugh out "
            "loud and the teenager in the grey hoodie leans further into the "
            "doorway",
     "cam": "The shot is taken from across the living room at waist height, "
            "straight on and level, wide enough to hold the whole hoist, the "
            "hanging body and the crowded doorway behind it",
     "luz": "Flat cold overcast daylight pushing in from the lace-curtained "
            "window, a weak warm bulb overhead, grey shadowless fill.",
     "audio": "nylon straps creaking, a steel chain clinking, low radio "
              "chatter and a room full of people talking and laughing"},

    {"id": "cadeira_salao", "curto": "a cadeira do salao racha",
     "v": "v46/v50", "sexos": ("mulher",),
     "formas": ("plateia", "silencio", "riso", "juizo"),
     "interior": True,
     "cen": "the inside of a small American nail salon, sage-green walls, a "
            "carved wooden sign high on the wall, racks of nail polish bottles "
            "in tight rainbow rows, a white drop ceiling with long fluorescent "
            "panels, three glass pendant lamps, beige tile floor and a long "
            "receding row of tan leather pedicure thrones with glass foot "
            "basins and rolled white towels",
     "acao": "the carved wooden armrest has just split apart in her hand and "
             "the leather seat is dropping off its pedestal with her still "
             "on it, one wet bare foot skidding off the rim of the glass "
             "basin as the basin goes over and water sheets out across the "
             "beige tile",
     "test": "the six women seated along the pedicure row have all twisted "
             "round in their chairs to look, two of them in white salon "
             "robes seated mid-row laughing behind their hands, and two nail "
             "technicians in black work polos and white latex gloves stand "
             "over her",
     "mov": "As the line begins she gets both palms flat on the tile and "
            "pushes to bring a knee under her. Halfway through the line the "
            "wet foot slides out from under her and the shoulder drops back "
            "against the tipped basin. As the line ends the two women in "
            "white salon robes laugh behind their hands and the technicians "
            "in black polos step back from the tipped basin",
     "cam": "The shot is taken from the salon aisle at waist height, angled "
            "slightly down, wide enough to hold the broken throne, the body on "
            "the tile and the whole receding row of chairs behind it",
     "luz": "Flat cool white fluorescent ceiling light, almost shadowless, a "
            "faint green bounce off the walls.",
     "audio": "the sharp crack of splitting wood, a collective gasp, a chair "
              "caster rolling and then a room gone quiet",
     # ⛔⛔ A VARIANTE MUDA (ver o bloco `A CENA MUDA` abaixo): o mesmo quadro
     # sem o riso, para o beat `silencio` nao desmentir a propria imagem.
     "test_q": "the six women seated along the pedicure row have all twisted "
               "round in their chairs to look, two of them with a flat hand "
               "over the mouth and nobody saying anything, and two nail "
               "technicians in black work polos and white latex gloves stand "
               "over her without moving",
     "mov_q": "As the line begins the last two heads in the row turn round. "
              "Halfway through the line two of the seated women put a hand "
              "over the mouth and not one of them speaks. As the line ends "
              "the whole room is still watching and nobody moves"},

    {"id": "rampa_medico", "curto": "a rampa do medico",
     "v": "v09/v15/v51", "sexos": ("casal",),
     # ⚠️ SEM `plateia`: as tres entradas dessa forma dizem `room`, e isto e'
     # uma rampa ao ar livre. Achado lendo a fala montada — *"every head in
     # the room turned"* sobre uma calcada e' o teste WTF reprovando.
     # ⚠️ E SEM `silencio`: duas das testemunhas desta imagem estao RINDO.
     "formas": ("impotencia", "riso", "juizo"),
     "interior": False,
     "cen": "an outdoor concrete wheelchair ramp climbing to the glass main "
            "entrance of a large city hospital on a bright morning, a pale "
            "limestone facade with dark tinted window bands, a dark canopy "
            "over the automatic sliding doors, grey steel pipe handrails down "
            "both sides of the ramp, a black planter with a clipped shrub and "
            "a parked SUV at street level behind the railing",
     "acao": "halfway up the ramp the knees of the one pushing have folded "
             "on the slope and the wheelchair has gone over sideways with "
             "them, tipping the other out onto the concrete in the same "
             "movement, four hands out flat on the ramp and one slip-on shoe "
             "skidding away down the incline",
     "test": "six people who were waiting outside the entrance have stopped "
             "on the steps to watch: two women in matching navy windbreakers "
             "laughing with their heads together, a young man in a brown "
             "delivery uniform standing still with his mouth open, and an "
             "older couple in raincoats who reach a hand halfway out and "
             "then pull it back",
     "mov": "As the line begins one of them grabs the grey steel handrail "
            "with both hands and hauls to get a knee up onto the ramp. "
            "Halfway through the line the hand slides down the pipe and the "
            "knee drops back onto the concrete as the wheelchair rocks over "
            "further. As the line ends the two women in navy windbreakers on "
            "the steps laugh into each other and the young man in the brown "
            "delivery uniform turns to watch them",
     "cam": "The shot is taken from a few feet behind the group at hip height, "
            "tilted up along the slope of the ramp so the fallen bodies sit low "
            "in the frame and the entrance sits high in it",
     "luz": "Flat overcast midday daylight, soft shadowless light on pale "
            "concrete, cool neutral white balance.",
     "audio": "shoes scuffing concrete, a palm slapping the steel handrail, "
              "the metallic clatter of the wheelchair frame on the concrete "
              "and two people laughing near the doors"},

    {"id": "escada_varanda", "curto": "a escada da varanda cede",
     "v": "v49", "sexos": ("casal",),
     "formas": ("impotencia", "riso", "dedo", "juizo"),
     "interior": False,
     "cen": "the front of a modest American house with pale grey clapboard "
            "siding, a weathered wooden porch with a square post and a slatted "
            "rail, a white-framed window and a black wall lantern beside the "
            "door, a run of thick weathered wooden steps down to a gravel "
            "driveway, and low green shrubs planted along the front of the "
            "porch",
     "acao": "one thick wooden tread has split through under them and both "
             "of them are dropping into the gap together, one hand still "
             "clamped on the slatted rail with the arm pulled straight, the "
             "broken half of the plank still in the air beside a knee and "
             "splinters flying out over the gravel",
     "test": "three neighbours have come out onto the sidewalk at the end of "
             "the driveway and stand there watching: a man in a blue polo "
             "with his arms folded laughing openly, a woman in a green "
             "sundress beside him standing still and simply staring, and a "
             "third in a red ball cap with one arm out pointing at the "
             "broken steps",
     "mov": "As the line begins one of them hauls down on the slatted rail "
            "with both hands and jams an elbow onto the step above. Halfway "
            "through the line the slat cracks out of the post and the "
            "shoulders drop back into the broken flight. As the line ends "
            "the man in the blue polo on the sidewalk laughs and says "
            "something and the neighbour in the red ball cap swings a "
            "pointing arm out at the steps",
     "cam": "The shot is taken from driveway height a few paces back, angled "
            "up the flight so both fallen bodies and the neighbours on the "
            "sidewalk sit in the same vertical frame",
     "luz": "Hard midday summer sun from the left, bleached wood, deep shadow "
            "under the porch roof, bright sky.",
     "audio": "a loud splintering crack, wood shards skittering on gravel, a "
              "boot scraping hard on the broken tread and laughter carrying "
              "from the sidewalk"},

    {"id": "carro_cafe", "curto": "a queda do carro com o cafe' derramado",
     "v": "v24", "sexos": ("mulher", "homem"),
     "formas": ("riso", "dedo", "juizo", "impotencia"),
     "interior": False,
     "cen": "a residential driveway paved in stamped brick-pattern concrete in "
            "warm terracotta and sand tones in the late afternoon, a white "
            "minivan filling one side of the frame with its side sliding door "
            "rolled fully open onto dark grey captain's chairs, a red painted "
            "kerb line along the far edge and a mowed lawn beyond",
     "acao": "coming down out of the open sliding door the leading knee has "
             "folded under and the takeaway cup has just left the hand, "
             "still in the air with its lid gone and a fan of coffee flying "
             "out ahead of it, one palm slapping flat onto the brick pavers "
             "as the hip drops",
     "test": "three neighbours are on the sidewalk right at the end of the "
             "driveway, close enough to read: two teenagers in basketball "
             "jerseys openly laughing with their heads tipped back and a "
             "woman in a yellow raincoat with a dog lead in one hand and her "
             "free hand flat over her mouth, all three stopped and watching",
     "mov": "As the line begins one hand grabs the sill of the open sliding "
            "door and pulls to drag a knee up under the hip. Halfway through "
            "the line the fingers slide off the sill and the shoulder drops "
            "back onto the pavers as the coffee spreads. As the line ends "
            "the two teenagers in basketball jerseys on the sidewalk laugh "
            "out loud and the woman in the yellow raincoat lifts her free "
            "hand to her mouth",
     "cam": "The shot is taken from beside the open sliding door at chest "
            "height, angled down about thirty degrees onto the pavers, wide "
            "enough to hold the fallen body, the spilled coffee and the group "
            "on the sidewalk",
     "luz": "Hard low late-afternoon sun from the right, strong warm key, long "
            "dark shadows raked across the brick pavers, high contrast.",
     "audio": "a plastic lid clattering on brick, a hand slapping flat on "
              "the pavers, a dog barking once and two young voices laughing"},

    {"id": "cctv_calcada", "curto": "a queda na propria garagem",
     "v": "v38", "sexos": ("casal",),
     # ⚠️ SEM `plateia` pela mesma razao (garagem ao ar livre), e sem
     # `silencio` porque a imagem tem um vizinho GRITANDO — a fala nao pode
     # dizer que ninguem falou nada.
     "formas": ("dedo", "riso", "juizo", "impotencia"),
     "interior": False,
     "cen": "the wide concrete driveway of a new-build suburban development at "
            "midday, grey vinyl-sided two-storey houses with stone-front "
            "gables and dark garage doors across the street, mowed green "
            "lawns, a young maple in a mulch bed, a clean asphalt street, a "
            "dark navy SUV parked at one side and a black coach lantern on the "
            "garage wall",
     "acao": "one of them has gone down on the concrete and taken the other "
             "over in the same movement, so both of them are landing tangled "
             "in one heap with four hands flat on the driveway, while the "
             "black three-wheel stroller with a small child in it rolls "
             "loose down the slope",
     "test": "four neighbours have closed into a ring around them on the "
             "concrete: a bearded man in a ball cap with his arms crossed "
             "laughing, a blonde woman in a pink hoodie beside him laughing "
             "too, a man in a yellow polo jabbing a pointed finger down at "
             "them and shouting, and an elderly woman in a floral housecoat "
             "against the garage with one hand over her mouth",
     "mov": "As the line begins one of them plants both palms on the "
            "concrete and drives an elbow down to get a hip off the ground. "
            "Halfway through the line the arm folds under and both of them "
            "settle back into the heap while the stroller rolls further down "
            "the slope. As the line ends the man in the yellow polo jabs his "
            "finger down at them and shouts and the bearded man in the ball "
            "cap laughs into the shoulder of the woman in the pink hoodie",
     "cam": "The shot is taken from under the garage eave about three metres "
            "up, looking down the driveway at roughly thirty degrees, wide "
            "enough to hold both bodies, the rolling stroller and the "
            "whole ring of neighbours",
     "luz": "Flat bright overcast midday daylight, no hard shadows, slightly "
            "desaturated and low contrast.",
     "audio": "one man shouting, two people laughing, stroller wheels on "
              "concrete and a street otherwise silent"},

    {"id": "reabilitacao", "curto": "reaprendendo a andar na clinica",
     "v": "v39", "sexos": ("mulher", "homem"),
     "formas": ("plateia", "silencio", "juizo", "impotencia", "riso"),
     "interior": True,
     "cen": "the physical-therapy room of a small American medical clinic, "
            "beige painted walls, black-framed anatomical charts of the "
            "muscular and skeletal systems, a wall-mounted ultrasound cart "
            "with a white monitor, a white drop ceiling with recessed "
            "fluorescent panels, wide plank wood-look vinyl flooring and a "
            "pale oak practice staircase with a varnished handrail",
     "acao": "three treads up the pale oak practice staircase both grey "
             "forearm crutches are planted on the step above with the whole "
             "body hanging off the grips, the left crutch tip skidding "
             "sideways off the varnished nosing and an empty black folding "
             "wheelchair waiting at the foot",
     "test": "six other patients waiting on the bench along the far wall "
             "have all stopped to watch: two of them in grey sweatshirts "
             "leaning together laughing quietly, a young man in a blue "
             "tracksuit openly staring, and an older woman in a red cardigan "
             "who looks away and then back again",
     "mov": "As the line begins both hands press down on the crutch grips "
            "and the trailing knee drives up toward the next tread. Halfway "
            "through the line the left crutch tip skids off the nosing and "
            "the foot comes back down onto the tread it started from. As the "
            "line ends the two patients in grey sweatshirts on the bench "
            "lean together laughing and the young man in the blue tracksuit "
            "stares openly",
     "cam": "The shot is taken from the top of the practice staircase at chest "
            "height, angled slightly down along the treads so the climb fills "
            "the lower frame and the waiting bench sits behind it",
     "luz": "Flat cool overhead fluorescent light, no shadow direction, a "
            "faint greenish institutional cast.",
     "audio": "rubber crutch tips knocking on wood, a crutch tip skidding on "
              "varnish, a low clinic hum and two people laughing quietly",
     # ⛔⛔ A VARIANTE MUDA — mesmo quadro, mesmo elenco, sem o riso.
     "test_q": "six other patients waiting on the bench along the far wall "
               "have all stopped to watch: two of them leaning together and "
               "watching without a word, one young man openly staring, and an "
               "older woman who looks away and then back again",
     "mov_q": "As the line begins one crutch tip skids on the tread and the "
              "whole bench of patients looks up. Halfway through the line two "
              "of them lean together and neither says anything. As the line "
              "ends the climb stalls one step from the top and the room stays "
              "silent",
     "audio_q": "rubber crutch tips knocking on wood, laboured breathing and "
                "a low clinic hum in a room with no voices in it"},

    {"id": "sofa_bombeiros", "curto": "os bombeiros erguem do sofa'",
     "v": "v59", "sexos": ("mulher", "homem"),
     "formas": ("riso", "juizo", "dedo", "impotencia"),
     "interior": True,
     "cen": "the living room of an ordinary suburban house, plain white-grey "
            "walls, a tall window with white venetian blinds letting in flat "
            "daylight, a beige fabric sectional sofa with loose cushions, a "
            "rectangular glass-top coffee table on a thin dark metal frame in "
            "the foreground and a grey geometric-pattern area rug beneath it",
     "acao": "both palms are jammed down into the sagging sofa cushions and "
             "the hips have come two inches clear of the seat, the whole "
             "beige sectional dragged forward off its feet with the "
             "movement, while two firefighters in tan bunker gear take a "
             "forearm each and pull",
     "test": "the front door stands open behind the sofa and five neighbours "
             "have crowded into the doorway to watch: three of them in work "
             "jackets laughing with their heads together, a teenager in a "
             "striped rugby shirt leaning in over the others to stare, and a "
             "woman in a green apron with both hands at her mouth",
     "mov": "As the line begins both palms drive down into the cushions and "
            "the hips push higher off the seat. Halfway through the line the "
            "near hand sinks through the cushion and the hips drop back into "
            "the sofa with the firefighters still holding the forearms. As "
            "the line ends the three in work jackets in the doorway laugh "
            "out loud and the teenager in the striped rugby shirt leans in "
            "further over their shoulders",
     "cam": "The shot is taken from across the coffee table at seated chest "
            "height, level and straight on, wide enough to hold the sofa, both "
            "firefighters and the crowded doorway behind them",
     "luz": "Cool flat daylight from the window at one side, grey and "
            "shadowless, a faint blue cast on the room.",
     "audio": "gear rustling, boots scuffing the rug, sofa springs creaking "
              "and several people laughing in the doorway"},

    # -----------------------------------------------------------------------
    # ⭐ CLUSTER A — FALENCIA ESTRUTURAL: o movel, a tabua ou o parafuso
    #    cede sob o corpo. A aresta do grafo e' GRAVIDADE + OLHAR DO OUTRO —
    #    o objeto publico quebra e a plateia que ja' estava ali vira
    #    testemunha sem precisar chegar de lugar nenhum. (12 entradas)
    # -----------------------------------------------------------------------
    {"id": "banco_igreja", "curto": "o banco da igreja racha",
     "v": "grafo-A", "cluster": "A",
     "sexos": ("mulher", "homem"),
     "formas": ("plateia", "silencio", "juizo"),
     "interior": True,
     "cen": "the inside of a small white country church on a Sunday morning, "
            "plain whitewashed board walls, tall arched windows with clear "
            "glass and dark wooden frames, a stained wooden pulpit on a low "
            "platform, a black hymn board with white number cards on the "
            "front wall, long rows of varnished oak pews with worn red "
            "cushions, and a narrow red carpet runner down the centre aisle",
     "acao": "the front pew has just snapped at the leg and the bench is "
             "tipping end-down into the aisle, the body sliding off the "
             "dropping seat with one hand still clamped on the pew back, the "
             "split half of the leg standing up out of the boards and "
             "hymnals coming off the tilt",
     "test": "the congregation has turned in the rows behind: two women in "
             "flowered dresses one pew back with a flat hand over the mouth, "
             "an usher in a grey suit stopped at the end of the front pew "
             "holding his hymnbook against his chest, a teenage boy in a "
             "clip-on tie half out of his seat staring, and nobody in the "
             "church saying anything",
     "mov": "As the line begins the body braces an elbow on the tilted bench "
            "and pushes to rise. Halfway through the line the split board "
            "drops another inch under that elbow and the hand slides off the "
            "varnished pew back, so the whole weight goes straight back "
            "down. As the line ends the two women in flowered dresses in the "
            "pew behind press a flat hand over the mouth, the usher in the "
            "grey suit lifts his hymnbook against his chest and the rows "
            "nearest the aisle draw back into their pews",
     "cam": "The shot is taken from the centre aisle at seated shoulder "
            "height, angled slightly down along the pews, wide enough to hold "
            "the broken bench, the body on the runner and four rows of turned "
            "faces behind it",
     "luz": "Warm morning sun coming through the tall arched windows in long "
            "bars across the pews, soft shadows on the whitewashed walls.",
     "audio": "a sharp crack of splitting wood, hymnals slapping the floor, "
              "one organ note trailing off and a church gone completely "
              "quiet"},

    {"id": "banqueta_lanchonete", "curto": "a banqueta da lanchonete cede",
     "v": "grafo-A", "cluster": "A",
     "sexos": ("mulher", "homem"),
     "formas": ("riso", "plateia", "juizo"),
     "interior": True,
     "cen": "the inside of an American roadside diner at lunchtime, a long "
            "formica counter in speckled cream with a chrome edge strip, a "
            "row of chrome pedestal stools with red vinyl tops bolted to a "
            "checkerboard tile floor, a stainless pass window behind the "
            "counter with paper tickets clipped above it, red vinyl booths "
            "along the window wall and a glass pie case at one end",
     "acao": "the chrome pedestal has just sheared off its floor plate under "
             "the second counter stool and the red vinyl top is rolling away "
             "across the tile, the body dropping onto the checkerboard floor "
             "with one hand hooked over the counter edge and a plate tipping "
             "off behind it",
     "test": "the counter is full and not one person has come off it: two men "
             "in work shirts on the next stools laughing with their heads "
             "tipped back, a waitress in a mint uniform stopped mid-pour with "
             "the coffee pot still up, and a man in a window booth half "
             "standing with his arm out, pointing down at the floor",
     "mov": "As the line begins the body hauls on the chrome counter edge "
            "and gets one shoulder up off the tile. Halfway through the line "
            "that arm folds under the load and the hand comes off the lip, "
            "so the body settles back onto the checkerboard. As the line "
            "ends the two men in work shirts on the next stools tip their "
            "heads back laughing, the waitress in the mint uniform behind "
            "the counter holds the coffee pot up mid-pour and the man in the "
            "window booth stabs his pointing arm out across the counter",
     "cam": "The shot is taken from the far end of the counter at seated "
            "chest height, angled slightly down along the row of stools, wide "
            "enough to hold the sheared pedestal, the body on the tile and "
            "the whole counter of watching faces",
     "luz": "Flat white fluorescent light from the ceiling panels with hard "
            "warm daylight coming in from the window wall at one side.",
     "audio": "a metallic bang, a plate breaking on tile, a stool top "
              "rolling and two men laughing out loud over the counter"},

    {"id": "cadeira_churrasco", "curto": "a cadeira de plastico no churrasco",
     "v": "grafo-A", "cluster": "A",
     "sexos": ("mulher", "homem"),
     "formas": ("riso", "impotencia", "juizo"),
     "interior": False,
     "cen": "a suburban back yard during a block cookout on a summer "
            "afternoon, a rectangular folding table under a blue pop-up "
            "canopy with paper plates and foil trays on it, a black kettle "
            "grill smoking at one side, white plastic stacking chairs set in "
            "a loose circle on cut grass, a wooden privacy fence with string "
            "lights along the top and open coolers in the shade",
     "acao": "all four legs of the white plastic chair have just splayed out "
             "at once and the seat is cracking through the middle, the body "
             "dropping inside the collapsing frame onto the cut grass with "
             "the paper plate already upturned in the air and food spreading "
             "over the lawn",
     "test": "the circle of chairs has not broken up: two men in shorts and "
             "ball caps laughing openly with their beers still in hand, a "
             "woman in an apron who has taken hold under one arm and is "
             "heaving with no result, and a second woman beside her who pulls "
             "at the other arm twice and lets go",
     "mov": "As the line begins the body rolls onto one hip and drives both "
            "palms into the grass to get a knee under. Halfway through the "
            "line the cracked seat shifts away under that knee and the arms "
            "fold, so the body comes back down inside the broken frame. As "
            "the line ends the two men in shorts and ball caps across the "
            "circle laugh out loud with their beers still up, the woman in "
            "the apron heaves under one arm and gets nowhere and the second "
            "woman lets go of the other wrist and steps back",
     "cam": "The shot is taken from inside the circle of chairs at seated hip "
            "height, angled slightly down across the grass, wide enough to "
            "hold the split chair, the body inside it and the whole ring of "
            "guests around it",
     "luz": "Hard afternoon summer sun through the blue canopy, warm bounce "
            "off the grass, sharp shadows under the table.",
     "audio": "plastic cracking and skidding on grass, foil trays rattling, "
              "a grill hissing and several people laughing at once"},

    {"id": "arquibancada_escola", "curto": "a tabua da arquibancada quebra",
     "v": "grafo-A", "cluster": "A",
     "sexos": ("mulher", "homem"),
     "formas": ("riso", "plateia", "juizo"),
     "interior": True,
     "cen": "the gymnasium of a small-town American community centre during "
            "an evening adult league game, a glossy varnished maple court "
            "with a painted blue key and centre circle, pale cinderblock "
            "walls painted cream, a black scoreboard high on the end wall, a "
            "folded blue wrestling mat against the wall, and a bank of "
            "pull-out wooden bleachers along one side packed with people",
     "acao": "one wooden bleacher plank has just cracked through in the "
             "third row and dropped a foot, the body going down between the "
             "boards with one leg through the gap to the thigh, both arms "
             "flung back onto the plank behind and a bag of popcorn still "
             "spilling down the rows below",
     "test": "the rows around the gap have all turned inward and stayed "
             "there: four adults on the row above laughing with their heads "
             "together, two teenagers beside them grinning, a woman in a "
             "league sweatshirt frozen halfway out of her seat, and a man two "
             "rows down twisted round with his mouth open, staring straight "
             "up at the broken plank",
     "mov": "As the line begins the body presses both palms onto the plank "
            "behind and pushes to lift the trapped leg out of the gap. "
            "Halfway through the line the cracked board sags further under "
            "those hands and the leg wedges tighter, so the push gets "
            "nothing. As the line ends the four adults on the row above "
            "break into open laughter, the two teenagers beside them grin "
            "and lean in over the boards and the woman in the league "
            "sweatshirt rises halfway out of her seat two rows up",
     "cam": "The shot is taken from the court floor at standing head height, "
            "angled about thirty degrees upward into the bleachers, wide "
            "enough to hold the broken plank, the trapped body and six rows "
            "of turned faces above it",
     "luz": "Hard white gymnasium high-bay light straight down, hot "
            "highlights on the varnished floor, short shadows under the "
            "bleachers.",
     "audio": "a loud wooden crack, popcorn scattering over the boards, a "
              "whistle stopping short and a row of people laughing"},

    {"id": "cadeira_dobravel_festa", "curto": "a cadeira dobravel na festa",
     "v": "grafo-A", "cluster": "A",
     "sexos": ("mulher", "homem"),
     "formas": ("riso", "plateia", "juizo"),
     "interior": True,
     "cen": "the rented hall of a small American community centre set for an "
            "anniversary party, cream painted cinderblock walls, a low white "
            "drop ceiling with square fluorescent panels, round tables in "
            "white cloths with gold paper centrepieces, silver foil letters "
            "strung across the far wall, a long buffet table with warming "
            "trays at one side and a scuffed wood-look vinyl floor",
     "acao": "the folding chair has just scissored shut under the body and "
             "is going over sideways, the body dropping onto the vinyl floor "
             "inside the closing steel frame with one hand dragging the "
             "white tablecloth off the table above it and a punch glass "
             "tipping over the edge",
     "test": "the party has stopped at every table: three guests in dress "
             "shirts at the next table laughing with their napkins still in "
             "hand, an older woman in a corsage standing across the room "
             "with both palms pressed to her cheeks, and a man in a green "
             "sweater at the buffet with a serving spoon in one hand and the "
             "other arm out, pointing across the room at the floor",
     "mov": "As the line begins the body takes hold of a leg of the round "
            "table and pulls to get the shoulders up off the vinyl. Halfway "
            "through the line the table skids toward the body instead of "
            "holding, the cloth comes off it and the pull gets nothing. As "
            "the line ends the three guests in dress shirts at the next "
            "table laugh out loud with their napkins still up, the older "
            "woman in the corsage across the room presses both palms to her "
            "cheeks and the man in the green sweater at the buffet points "
            "his serving spoon at the floor",
     "cam": "The shot is taken from beside the buffet table at standing chest "
            "height, angled down about thirty degrees across the room, wide "
            "enough to hold the folded chair, the body on the vinyl and four "
            "full tables behind it",
     "luz": "Flat cool fluorescent ceiling light across the whole room, a "
            "weak warm bounce off the gold centrepieces, no shadow direction.",
     "audio": "steel folding legs snapping shut, a glass rolling on vinyl, "
              "a table scraping and a whole table of guests laughing"},

    {"id": "cadeira_guiche", "curto": "a cadeira do guiche estoura",
     "v": "grafo-A", "cluster": "A",
     "sexos": ("mulher", "homem"),
     "formas": ("plateia", "silencio", "juizo"),
     "interior": True,
     "cen": "the public service floor of a county office building, grey-blue "
            "carpet tiles, a long counter of numbered service windows in pale "
            "laminate with clear screens above them, a red digital number "
            "display over the far window, rows of grey stacking chairs facing "
            "the counter, a ticket dispenser on a post and cream painted "
            "walls with a framed county seal",
     "acao": "the gas cylinder of the wheeled chair at the service window "
             "has just blown through its whole travel and the seat is going "
             "over backwards, the body tipping off it toward the carpet "
             "tiles with one hand still on the counter lip and loose "
             "paperwork lifting off the ledge",
     "test": "the whole waiting floor has turned and stayed turned: two women "
             "in the front row of chairs with a flat hand over the mouth, a "
             "man in a delivery jacket standing up out of his seat and openly "
             "staring, a clerk behind the screen half risen with both palms "
             "flat on the counter, and not one voice in the room",
     "mov": "As the line begins the body pulls hard on the laminate counter "
            "lip and gets one elbow up onto it. Halfway through the line the "
            "elbow slides back off the counter and the five-castor base "
            "rolls out from under, so the body settles onto the carpet "
            "tiles. As the line ends the two women in the front row of "
            "chairs raise a flat hand over the mouth, the man in the "
            "delivery jacket in the waiting rows comes up out of his seat "
            "staring and the clerk behind the screen leans over the counter "
            "on both palms",
     "cam": "The shot is taken from beside the service window at standing "
            "chest height, angled about twenty degrees down, wide enough to "
            "hold the dropped chair, the body on the carpet tiles and the "
            "full rows of seated people facing it",
     "luz": "Flat cool fluorescent ceiling light across the whole floor, a "
            "faint green cast on the carpet tiles, almost no shadow.",
     "audio": "a sharp pneumatic bang, castors clattering over carpet, "
              "loose paper sliding and a service floor gone completely "
              "quiet"},

    {"id": "rede_quintal", "curto": "o poste da rede arranca",
     "v": "grafo-A", "cluster": "A",
     "sexos": ("mulher", "homem"),
     "formas": ("riso", "juizo"),
     "interior": False,
     "cen": "the back yard of an ordinary American house on a summer "
            "afternoon, a striped canvas hammock slung between a wooden deck "
            "post and a leaning steel stand on cut grass, a raised wooden "
            "deck with a rail behind it, a folding side table with cans on "
            "it, a chain link fence with honeysuckle grown through it and "
            "garden beds along the far edge",
     "acao": "the wooden deck post has just torn out of the boards at its "
             "base and is coming down with the hammock, the body swinging to "
             "the grass rolled up in the striped canvas with the split post "
             "still in the air over the legs and the side table going flat "
             "beside it",
     "test": "four relatives who were up on the deck have come to the rail "
             "instead of the steps: two men in ball caps laughing hard with "
             "their hands on the rail, a woman beside them with a serving "
             "bowl still against her hip and her mouth open, and a boy in "
             "his teens leaning over the rail with one arm out, pointing "
             "straight down at the tangled canvas",
     "mov": "As the line begins the body grabs two fistfuls of the striped "
            "canvas and pulls to swing a leg out of it. Halfway through the "
            "line the canvas cinches tighter around the hips with that pull "
            "and the leg stays inside, so the body rolls back flat on the "
            "grass. As the line ends the two men in ball caps at the deck "
            "rail laugh hard with both hands on the rail, the woman with the "
            "serving bowl against her hip opens her mouth and the teenage "
            "boy leans further over the rail and points straight down",
     "cam": "The shot is taken from the grass a few paces off at hip height, "
            "angled about twenty degrees upward toward the deck so the "
            "tangled hammock sits low in the frame and the four at the rail "
            "sit high in it",
     "luz": "Hard high summer sun from the left, sharp shadows across the cut "
            "grass, bright sky over the fence.",
     "audio": "wood splitting and screws tearing out, a table clattering on "
              "grass, cans rolling and two men laughing up on the deck"},

    {"id": "tabua_pier", "curto": "a tabua do pier cede",
     "v": "grafo-A", "cluster": "A",
     "sexos": ("casal",),
     "formas": ("riso", "impotencia", "juizo"),
     "interior": False,
     "cen": "a public wooden fishing pier on a lake on a bright morning, "
            "weathered grey planking with wide gaps between the boards, a "
            "paint-flaked steel pipe rail down both sides, a life ring on a "
            "white post, a fish cleaning station with a hose coiled under it, "
            "rowboats tied along one side and a dark tree line across flat "
            "green water",
     "acao": "one weathered plank has just snapped through under both of "
             "them and the two broken halves are still swinging down toward "
             "the water, so both are dropping into the gap together, one leg "
             "of each through the decking to the knee and their hands "
             "clamped on the same pipe rail",
     "test": "seven people fishing along the rail have reeled in and come a "
             "few steps closer without touching anything: two men in camo "
             "ball caps laughing with their rods still up, a man in chest "
             "waders who takes a wrist and hauls and gets nowhere, and an "
             "older woman in a yellow rain slicker who reaches for the other "
             "arm, pulls twice and steps back",
     "mov": "As the line begins both of them haul on the pipe rail together "
            "and try to lift a knee clear of the gap. Halfway through the "
            "line the rail flexes out on its brackets and their hands slide "
            "down it, so both legs drop back through the boards. As the line "
            "ends the two men in camo ball caps along the rail laugh out "
            "loud with their rods still up, the man in chest waders takes a "
            "wrist, hauls and gets nowhere and the older woman in the yellow "
            "rain slicker pulls twice at the other arm and steps back",
     "cam": "The shot is taken from further down the pier at hip height, "
            "straight along the walkway and level, wide enough to hold the "
            "broken plank, both bodies on the decking and the whole line of "
            "people at the rail",
     "luz": "Hard morning sun low across the water, bright glints on the "
            "lake, warm light along the grey planking.",
     "audio": "a hard wooden snap, water slapping the pilings, a rod "
              "clattering on the deck and two people laughing along the "
              "rail"},

    {"id": "degrau_trailer", "curto": "o degrau do trailer arranca",
     "v": "grafo-A", "cluster": "A",
     "sexos": ("mulher", "homem"),
     "formas": ("riso", "dedo", "juizo"),
     "interior": False,
     "cen": "the pitch of a busy American campground in the morning, a white "
            "travel trailer with a striped awning rolled halfway out, a "
            "folding aluminium step unit at its door, a picnic table with a "
            "checked cloth, a stone fire ring full of cold ash, a green nylon "
            "tent two pitches over and gravel roads between the sites under "
            "tall pines",
     "acao": "the top tread of the aluminium step unit has just folded under "
             "and torn off its hinge, the body dropping off the trailer "
             "doorway onto the gravel with one hand still hooked on the door "
             "frame, the bent tread turning in the air and a coffee mug "
             "thrown clear",
     "test": "the neighbouring pitches have come to the edge of their sites "
             "and stopped there: a couple in matching windbreakers laughing "
             "with their coffee still in hand, a man in a fishing hat "
             "standing with one arm out pointing at the bent step, and two "
             "teenagers stopped on their bicycles at the gravel road staring",
     "mov": "As the line begins the body pulls on the trailer door frame and "
            "gets a foot onto the bottom tread. Halfway through the line "
            "that tread folds under the foot as well and the hands come off "
            "the frame, so the body sits back down on the gravel. As the "
            "line ends the couple in matching windbreakers laugh at the edge "
            "of their site with their coffee still up, the man in the "
            "fishing hat at the next pitch pushes his pointing arm further "
            "out and the two teenagers on bicycles put a foot down on the "
            "gravel road",
     "cam": "The shot is taken from the gravel road at hip height, angled "
            "about twenty degrees up toward the trailer door, wide enough to "
            "hold the torn step, the body on the gravel and the watching "
            "neighbours at their sites",
     "luz": "Cool early morning sun raking through the pines, long soft "
            "shadows across the gravel, pale sky above the trees.",
     "audio": "metal tearing and clanging on gravel, a mug rolling, a camp "
              "chair collapsing and a couple laughing two sites over"},

    {"id": "balanco_varanda", "curto": "o balanco da varanda despenca",
     "v": "grafo-A", "cluster": "A",
     "sexos": ("casal",),
     "formas": ("riso", "dedo", "juizo"),
     "interior": False,
     "cen": "the covered front porch of an American clapboard house in the "
            "late afternoon, pale yellow siding, a white painted porch "
            "ceiling with two heavy eye bolts screwed into the beam, a wooden "
            "porch swing on chains hanging under them, a white rail with "
            "turned balusters, a hanging basket of ferns at the corner and a "
            "paved sidewalk with parked cars beyond the steps",
     "acao": "one eye bolt has just ripped out of the porch beam and the "
             "swing is dropping on that side with both of them still on the "
             "seat, both sliding down the tilted boards toward the rail with "
             "the loose chain whipping across their knees and paint chips "
             "still in the air",
     "test": "five neighbours out on the sidewalk have stopped in front of "
             "the house and stayed there: two men in ball caps laughing "
             "openly at the foot of the steps, a woman with a stroller "
             "stopped dead with a hand at her mouth, a man in a work vest "
             "with his arm out pointing up at the empty bolt hole, and a "
             "teenager halfway up the walk",
     "mov": "As the line begins both of them grab the swing chain over their "
            "heads and pull to get off the tilting seat. Halfway through the "
            "line the second bolt turns in the beam and the seat drops "
            "another foot, so both slide down the boards instead. As the "
            "line ends the two men in ball caps at the foot of the steps "
            "break out laughing, the woman with the stroller claps a hand "
            "over her mouth and the man in the work vest on the sidewalk "
            "jabs his pointing arm up at the empty bolt hole",
     "cam": "The shot is taken from the sidewalk at chest height, angled "
            "about twenty degrees up onto the porch, wide enough to hold the "
            "fallen swing, both bodies on the boards and the group standing "
            "in the foreground",
     "luz": "Warm low late-afternoon sun from the side, long shadows across "
            "the porch boards, deep shade under the roof.",
     "audio": "a bolt tearing out of wood, chain links hitting the boards, "
              "a hanging basket swinging and two men laughing on the "
              "sidewalk"},

    {"id": "corrimao_biblioteca", "curto": "o corrimao da biblioteca arranca",
     "v": "grafo-A", "cluster": "A",
     "sexos": ("mulher", "homem"),
     "formas": ("plateia", "silencio", "juizo"),
     "interior": True,
     "cen": "the open stairwell inside a small public library, a wide "
            "staircase of pale terrazzo steps with black rubber nosing, a "
            "brushed steel handrail on brackets along the cream plaster wall, "
            "a mezzanine of oak shelving above behind a chest-high glass "
            "balustrade, framed reading posters on the wall and a long study "
            "table with green shaded lamps at the foot of the stairs",
     "acao": "the steel handrail has just torn off the wall at three "
             "brackets and is swinging down across the plaster with the body "
             "still holding on to it, the body dropping backwards over the "
             "terrazzo steps as the wall anchors pull free and plaster dust "
             "comes off the wall in a line",
     "test": "the study table and the mezzanine above have both turned to the "
             "stairwell: three students up from the long table with a hand "
             "over the mouth, an older man at the mezzanine glass looking "
             "straight down over the rail, and a librarian in a cardigan "
             "stopped at the foot of the stairs with an armful of books and "
             "no voice in the room",
     "mov": "As the line begins the body pulls up on the loose handrail and "
            "gets one foot back onto a step. Halfway through the line a "
            "fourth bracket tears out of the plaster under that pull and the "
            "rail drops another foot, so the body goes back down over the "
            "steps. As the line ends the three students at the long table "
            "come up out of their chairs with a hand over the mouth, the "
            "older man at the mezzanine glass leans further over the "
            "balustrade and the librarian in the cardigan stops short at the "
            "foot of the stairs with her books",
     "cam": "The shot is taken from the foot of the staircase at standing "
            "chest height, angled about thirty degrees up along the steps, "
            "wide enough to hold the torn rail, the body on the terrazzo and "
            "the faces at the mezzanine glass above",
     "luz": "Cool even daylight from a high clerestory window with a weak "
            "warm fill from the table lamps, soft shadows on the plaster.",
     "audio": "steel brackets tearing out of plaster, a handrail ringing "
              "against the wall, books hitting the floor and a room with no "
              "voices in it"},

    {"id": "banco_restaurante", "curto": "o banco do restaurante solta",
     "v": "grafo-A", "cluster": "A",
     "sexos": ("mulher", "homem"),
     "formas": ("riso", "plateia", "juizo"),
     "interior": True,
     "cen": "the dining room of a family restaurant in the evening, dark "
            "stained wood-panel wainscot, deep red vinyl booths in a row "
            "along the window wall with brass rail dividers, tables in dark "
            "laminate with paper placemats and squat glass tumblers, a brass "
            "wall lamp over each booth, a patterned red carpet and a service "
            "station with water jugs at the end of the row",
     "acao": "the bench of the corner booth has just torn off its wall bolts "
             "at one end and is dropping to the carpet, the body sliding "
             "down into the gap between the bench and the table with both "
             "hands on the table edge, the table pushed off square and a "
             "tumbler going over across the placemats",
     "test": "the whole dining room has turned toward the corner booth and "
             "stayed turned: a party of four at the next table laughing with "
             "their forks still up, a waiter stopped in the aisle with a "
             "tray on one hand, and a man in a plaid shirt at the service "
             "station with his arm straight out, pointing across the room at "
             "the dropped bench",
     "mov": "As the line begins the body pulls on the table edge with both "
            "hands and tries to lift clear of the gap. Halfway through the "
            "line the table slides toward the body over the carpet and the "
            "bench end drops further, so the pull only takes the body deeper "
            "into the gap. As the line ends the party of four at the next "
            "table laugh out loud with their forks still up, the waiter with "
            "the tray on one hand turns in the aisle and the man in the "
            "plaid shirt at the service station stabs his arm out across the "
            "room",
     "cam": "The shot is taken from the aisle at seated chest height, angled "
            "slightly down into the booth, wide enough to hold the torn "
            "bench, the body wedged at the table and the full row of watching "
            "tables behind it",
     "luz": "Warm low tungsten light from the brass wall lamps over the "
            "booths, deep shadow in the corners, cool blue window light at "
            "the edge.",
     "audio": "bolts tearing out of a wall, a bench end dropping onto "
              "carpet, a glass tipping over and a table of guests laughing"},

    # -----------------------------------------------------------------------
    # ⭐ CLUSTER B — VULNERABILIDADE FISICA: o chao vence o corpo e o que
    #    ele carregava se espalha em quadro. A aresta e' GRAVIDADE: a queda
    #    so' abre o quadro, quem humilha e' quem escolheu parar e olhar em
    #    vez de ajudar. (12 entradas)
    # ⛔⛔ E A CAUSA E' SEMPRE O CORPO OU O DEGRAU, NUNCA UM VILAO EXTERNO
    #    NOMEADO — conserto de 2026-08-21. Oito entradas punham a culpa fora
    #    (gelo, oleo, piso molhado, azulejo solto, faixa pintada, pente da
    #    escada rolante): quem cai no gelo e' qualquer um, e o video deixa de
    #    ser *This was <NOME> before* para virar acidente com reu. Nas nove
    #    LIDAS nenhuma nomeia perigo — o v24 escorrega DESCENDO da van e o v38
    #    fecha em `unable to push themselves up`. ⚠️ Quando o vilao saiu do
    #    `acao` ele teve de sair junto do `cen`, do `cam`, da `luz` e do
    #    `audio`: bloco que remove a causa e mantem o gelo na trilha sonora e'
    #    o defeito do VICK 16 — cada campo passa e o quadro inteiro mente.
    # -----------------------------------------------------------------------
    {"id": "mercado_faixa", "curto": "as compras espalhadas no estacionamento",
     "v": "grafo-B", "cluster": "B",
     "sexos": ("mulher", "homem"),
     "formas": ("riso", "juizo"),
     "interior": False,
     "cen": "the painted pedestrian crossing across the entrance lane of a "
            "large American supermarket parking lot in the late afternoon, "
            "wide white stripes on grey asphalt, a low kerb with a mulch "
            "strip and clipped shrubs, a long glass storefront with automatic "
            "doors behind it, a nested train of steel shopping carts against "
            "the wall and rows of parked cars filling the background",
     "acao": "the leading knee is folding stepping down off the kerb onto "
             "the crossing and the body is going over sideways onto one hip "
             "with one hand thrown flat on the asphalt, while the paper sack "
             "splits open in the air and oranges and a cracked egg carton "
             "spill across the white stripes",
     "test": "three shoppers have stopped their carts a few steps away: two "
             "of them in grey fleece jackets laughing with their heads "
             "tipped together, a man in a green store apron gripping a cart "
             "handle and staring down at the crossing, and a woman in a "
             "yellow sun visor with one arm out pointing at the scattered "
             "groceries",
     "mov": "As the line begins the body plants both hands on the asphalt "
            "beside the split sack and drives up onto one knee. Halfway "
            "through the line the planted hand skids forward over the loose "
            "oranges and the shoulder drops back onto the white stripes. As "
            "the line ends the two shoppers in grey fleece jackets laugh "
            "harder behind their carts and the man in the green store apron "
            "takes both hands off his cart handle and steps back from the "
            "kerb",
     "cam": "The shot is taken from the parking row at chest height, angled "
            "down about twenty degrees across the crossing, wide enough to "
            "hold the fallen body, the spread of groceries and the shoppers "
            "standing behind their carts",
     "luz": "Hard low late-afternoon sun from the left, long shadows raked "
            "across the white stripes, warm high-contrast key.",
     "audio": "cans rolling on asphalt, a paper sack tearing open, cart "
              "wheels stopping and two people laughing close by"},

    {"id": "onibus_degrau", "curto": "o degrau do onibus e a roupa suja",
     "v": "grafo-B", "cluster": "B",
     "sexos": ("mulher", "homem"),
     "formas": ("riso", "juizo", "impotencia"),
     "interior": False,
     "cen": "a city bus stop on a wide commercial street at mid-morning, a "
            "glass and steel shelter with a slatted metal bench, a printed "
            "timetable panel behind scratched plexiglass, a full-size transit "
            "bus pulled in at the kerb with its front door folded open onto a "
            "high first step, a litter bin, a bare street tree in a metal "
            "grate and low brick storefronts across the road",
     "acao": "the leading knee has buckled on the long drop off the high "
             "first step and the body is going over onto the pavement with "
             "one hand still hooked on the folded door, while the mesh "
             "laundry bag splits against the kerb and throws damp towels, "
             "sheets and single socks out into the gutter",
     "test": "six passengers waiting to board are backed up along the "
             "shelter: two young women in denim jackets laughing openly, an "
             "older man in a brown work jacket crouched at the kerb with a "
             "forearm in both hands, and a teenager in a red hooded top "
             "leaning out over the kerb toward the laundry in the gutter",
     "mov": "As the line begins the body pulls on the edge of the folded "
            "door with both hands and drags one knee up onto the bottom "
            "step. Halfway through the line the hand slides down the smooth "
            "painted edge and the knee comes back off the step into the "
            "gutter. As the line ends the two young women in denim jackets "
            "at the shelter laugh out loud and the older man in the brown "
            "work jacket takes a forearm in both hands, hauls once and opens "
            "his hands again",
     "cam": "The shot is taken from the kerb a few paces back at hip height, "
            "angled about twenty degrees up toward the open bus door so the "
            "fallen body, the spilled laundry and the whole waiting queue sit "
            "in one frame",
     "luz": "Flat bright overcast morning light, soft shadowless fill on wet "
            "concrete, cool neutral white balance.",
     "audio": "an idling bus engine, air brakes hissing, wet fabric "
              "dragging on concrete and two women laughing at the shelter"},

    {"id": "gelo_correios", "curto": "o gelo na calcada dos correios",
     "v": "grafo-B", "cluster": "B",
     "sexos": ("mulher", "homem"),
     "formas": ("silencio", "juizo", "impotencia"),
     "interior": False,
     "cen": "the sidewalk outside a small-town post office on a grey winter "
            "morning, a squat brick building with a wide stone step and a "
            "glazed door set in a deep frame, plain concrete slabs running to "
            "the kerb, a black cast-iron mailbox stand at the kerb, a snow "
            "bank pushed up against a bare hedge and parked cars ridged with "
            "old snow along the street",
     "acao": "the leading knee has stalled halfway up the single wide stone "
             "step and the body is going back off it onto the concrete slabs "
             "below, one arm still hooked round a cardboard box that is "
             "tearing open along its seam and shedding padded envelopes "
             "across the pavement",
     "test": "four people waiting to get in are stopped on the step above: "
             "two women in long winter coats with a flat hand over the mouth "
             "and saying nothing, a man in a grey wool cap crouched at the "
             "foot of the step with a grip under one arm, and a woman in a "
             "red headscarf watching from the door beside the sliding "
             "envelopes",
     "mov": "As the line begins the body gets one elbow up onto the stone "
            "step and pushes to bring the other knee under it. Halfway "
            "through the line the elbow slides off the rounded edge of the "
            "step and the shoulder comes back down onto the concrete slabs. "
            "As the line ends the man in the grey wool cap hauls once on the "
            "arm he is holding and opens his hands again, and the two women "
            "in long winter coats on the step above raise a flat hand to the "
            "mouth",
     "cam": "The shot is taken from the kerb at knee height, angled slightly "
            "up along the concrete slabs so the body lies low and wide in the "
            "frame with the post office step and the watching group behind it",
     "luz": "Flat cold winter overcast, blue-grey light with no shadow "
            "direction, a pale glare coming off the bare concrete slabs.",
     "audio": "a stack of parcels going down on concrete, cardboard scraping "
              "the slabs, a shoe scuffing the stone step and a street with "
              "no voices on it"},

    {"id": "praca_bandeja", "curto": "a bandeja voa na praca de alimentacao",
     "v": "grafo-B", "cluster": "B",
     "sexos": ("mulher", "homem"),
     "formas": ("riso", "plateia", "juizo"),
     "interior": True,
     "cen": "the food court of an American shopping mall at lunch time, a "
            "high white coffered ceiling with round downlights, a glass "
            "barrel skylight over the middle, a grid of fixed laminate tables "
            "with attached seats, tiled counters and back-lit menu boards "
            "along the far wall, and a bank of steel bins with tray shelves "
            "on the polished tile",
     "acao": "the hips have jammed on the post of the fixed seat and the "
             "last shove has torn the body out of it sideways into the "
             "aisle, the loaded tray leaving both hands in the air with "
             "burgers, a bucket of fries and a burst soda cup fanning out "
             "across the tiles",
     "test": "the two nearest tables have emptied and eight people are "
             "standing around the aisle: three teenagers in basketball "
             "jerseys laughing out loud with a fourth grinning behind them, "
             "a woman in a food-court polo holding a mop handle in both "
             "hands, and an older man in a green windbreaker staring down at "
             "the spilled soda",
     "mov": "As the line begins the body gets one hand onto the edge of the "
            "laminate table and one knee up off the tile to climb back into "
            "the seat. Halfway through the line the hand slips off the wet "
            "laminate where the soda ran and the knee goes back down into "
            "the spill. As the line ends the three teenagers in basketball "
            "jerseys at the next table laugh out loud and the woman in the "
            "food-court polo props both hands on her mop handle and looks "
            "away toward the counters",
     "cam": "The shot is taken from the aisle at chest height, angled down "
            "about twenty-five degrees onto the tile, wide enough to hold the "
            "fallen body, the scattered food and the emptied tables standing "
            "behind it",
     "luz": "Bright flat mall lighting from overhead downlights with cool "
            "skylight fill, almost shadowless, faintly green on the tile.",
     "audio": "a tray clattering on tile, ice cubes skidding away, chairs "
              "scraping back and a crowd of young voices laughing"},

    {"id": "posto_latas", "curto": "as latas rolando no posto",
     "v": "grafo-B", "cluster": "B",
     "sexos": ("mulher", "homem"),
     "formas": ("riso", "juizo"),
     "interior": False,
     "cen": "the forecourt of a highway gas station at midday, a wide steel "
            "canopy on white columns over two fuel islands, black and yellow "
            "pump housings with printed price panels, an oil-stained concrete "
            "apron, a rack of windshield squeegee buckets, a glass-fronted "
            "service shop with an ice chest outside the door and a flat scrub "
            "field beyond the entrance",
     "acao": "the knees have folded halfway back to the car and the body is "
             "going down against the pump base with both hands flying out "
             "flat on the concrete, while the plastic carrier tears open "
             "from its handle and a dozen soda cans burst out and roll under "
             "the parked cars, two of them foaming",
     "test": "two drivers have left their own pumps and stand a few steps "
             "off: one in a blue polo laughing with the fuel nozzle still up "
             "in his hand and one in an orange work shirt doubled over "
             "grinning, a woman in a straw hat at the next island has one "
             "arm out pointing at the rolling cans, and the shop clerk holds "
             "the glass door open and watches from the step",
     "mov": "As the line begins the body gets both hands onto the pump base "
            "and pushes up against it to bring one foot flat on the "
            "concrete. Halfway through the line the hand slides down the "
            "smooth pump housing and the shoulder comes back against the "
            "base. As the line ends the driver in the blue polo laughs with "
            "the fuel nozzle still up in his hand, the driver in the orange "
            "work shirt doubles over grinning, and the woman in the straw "
            "hat at the next island pushes her pointing arm further out",
     "cam": "The shot is taken from under the canopy at chest height, angled "
            "down about thirty degrees along the pump island so the fallen "
            "body, the rolling cans and both watching drivers sit in the same "
            "frame",
     "luz": "Hard midday sun outside the canopy with deep flat shade "
            "underneath, blown bright highlights on the concrete apron "
            "beyond.",
     "audio": "aluminium cans rolling on concrete, soda hissing out of a "
              "split can, a pump nozzle clicking and two men laughing"},

    {"id": "escada_rolante", "curto": "a escada rolante e as sacolas",
     "v": "grafo-B", "cluster": "B",
     "sexos": ("casal",),
     "formas": ("riso", "plateia", "juizo", "impotencia"),
     "interior": True,
     "cen": "the ground floor of a department store at the foot of a moving "
            "staircase, brushed steel side panels and a black rubber handrail "
            "running down into a stainless comb plate, polished cream stone "
            "flooring, a glass balustrade along the upper landing, chrome "
            "clothing racks and lit display counters spreading out across the "
            "sales floor behind",
     "acao": "the last moving step is dropping away under the leading foot "
             "at the comb plate and the balance is going backwards, one of "
             "them catching the other on the way down, so both are landing "
             "on the stone with shoe boxes, folded shirts and a burst paper "
             "bag flung out around them",
     "test": "the shoppers carried down behind them are backing up two deep "
             "on the moving steps: two women in wool coats near the front "
             "laughing with their heads together, a man in a charcoal suit "
             "who steps over an outstretched leg onto the stone without "
             "stopping, a woman in a tan raincoat just behind him with an "
             "elbow in both hands, and a boy at the balustrade above leaning "
             "over toward the spilled boxes",
     "mov": "As the line begins one of them gets a hand onto the steel side "
            "panel and drives up onto one knee while the other pushes at the "
            "stone with both palms. Halfway through the line the hand skids "
            "off the smooth panel and both come back down onto the stone "
            "among the spilled boxes. As the line ends the two women in wool "
            "coats near the front of the steps laugh with their heads "
            "together and the woman in the tan raincoat hauls twice on the "
            "elbow she is holding and opens her hands",
     "cam": "The shot is taken from the sales floor at hip height, angled "
            "about twenty degrees up toward the comb plate so both bodies, "
            "the spilled boxes and the stacked shoppers on the steps read in "
            "one frame",
     "luz": "Bright even retail lighting from overhead spots, cool white with "
            "soft speculars on the steel panels.",
     "audio": "the escalator drive humming, cardboard boxes sliding on "
              "stone, hangers rattling and two women laughing on the steps"},

    # ⛔ LAPIDE 2026-08-21 — `lavanderia_cesto` CORTADO: colapsa com
    #    `onibus_degrau`, que ja' e' dono de "roupa suja espalhada em publico" e cuja
    #    causa ja' e' do corpo (o primeiro degrau alto do onibus). Aqui a causa era o
    #    azulejo levantado — vilao externo, o defeito do cluster B.


    {"id": "porta_giratoria", "curto": "a porta giratoria do saguao",
     "v": "grafo-B", "cluster": "B",
     "sexos": ("mulher", "homem"),
     "formas": ("silencio", "juizo", "impotencia"),
     "interior": True,
     "cen": "the lobby of a downtown office building on a weekday morning, a "
            "four-wing revolving door in a polished brass drum set into a "
            "full-height glass wall, veined grey marble flooring, a long "
            "stone reception counter with a house plant at each end, a bank "
            "of brushed steel lift doors down one side and a rope-and-post "
            "queue line laid out across the floor",
     "acao": "the trailing hip has jammed against the leading edge of the "
             "door wing and stopped the whole drum dead halfway round, so "
             "the body is going down inside the glass against the curved "
             "wall with the cardboard drink tray crushing underneath and "
             "four coffees running out under the seal",
     "test": "eleven people are held up on both sides of the stuck drum and "
             "nobody there makes a sound: two office workers in blue "
             "lanyards with their hands on a shoulder through the open wing, "
             "a woman in a camel coat by the reception counter pressing a "
             "flat hand over her mouth, and the rest along the rope line "
             "watching",
     "mov": "As the line begins the body gets both palms flat on the curved "
            "glass and pushes to bring one knee up off the marble. Halfway "
            "through the line the palm skids down the glass through the "
            "spilled coffee and the knee goes back down. As the line ends "
            "the two office workers in blue lanyards haul once on the "
            "shoulder they have hold of through the open wing and let go, "
            "and the woman in the camel coat at the reception counter "
            "presses a flat hand over her mouth",
     "cam": "The shot is taken from inside the lobby at chest height, about "
            "thirty degrees off the axis of the brass drum and square to the "
            "open wing so the line of sight goes through the opening instead "
            "of through the curved glass, wide enough to hold the wedged "
            "body, the spreading coffee and the held-up people on both sides "
            "of it",
     "luz": "Cool morning daylight flooding through the glass wall with soft "
            "overhead fill, low contrast and slightly blue on the marble.",
     "audio": "a revolving door mechanism grinding to a stop, a paper cup "
              "crushing, coffee running across stone and a lobby with no "
              "voices in it"},

    {"id": "corredor_lixo", "curto": "o saco de lixo rasga no corredor",
     "v": "grafo-B", "cluster": "B",
     "sexos": ("mulher", "homem"),
     "formas": ("riso", "dedo", "juizo"),
     "interior": False,
     "cen": "the open exterior walkway of a two-storey American apartment "
            "block in the morning, a painted steel guard rail running the "
            "length of it, numbered doors with worn mats and a plastic chair "
            "outside one of them, a concrete stair with a metal nosing at the "
            "far end, a row of dented dumpsters in the lot below and parked "
            "cars behind them",
     "acao": "the leading knee has folded on the top step with the trash bag "
             "swung out over the rail, and the body is coming down across "
             "the concrete nosing on one hip and both forearms while the bag "
             "splits open from top to bottom and spills grounds, tins and "
             "food waste down four steps",
     "test": "four neighbours have come out along the walkway above: two of "
             "them in grey sweatshirts laughing over the rail with their "
             "doors standing open, a man in an orange work vest with one arm "
             "out pointing down at the split bag, and a woman in the lot "
             "below who stops with her keys in her hand and stares up",
     "mov": "As the line begins the body gets both forearms onto the stair "
            "nosing and pushes to lift one hip clear of the steps. Halfway "
            "through the line the forearm slides off the metal nosing "
            "through the wet grounds and the hip drops back onto the "
            "concrete. As the line ends the two neighbours in grey "
            "sweatshirts lean further over the walkway rail laughing and the "
            "man in the orange work vest pushes his pointing arm out over "
            "the rail and calls something down",
     "cam": "The shot is taken from the lot at the foot of the stair at chest "
            "height, angled about thirty degrees up so the body on the steps, "
            "the split bag and the neighbours along the walkway all sit in "
            "one vertical frame",
     "luz": "Flat bright overcast morning light, soft shadowless fill on grey "
            "concrete, cool neutral balance.",
     "audio": "a plastic bag tearing, tins and bottles rolling down "
              "concrete steps, a screen door banging and two people "
              "laughing above"},

    {"id": "rampa_tinta", "curto": "a lata de tinta na rampa",
     "v": "grafo-B", "cluster": "B",
     "sexos": ("casal",),
     "formas": ("riso", "juizo", "impotencia"),
     "interior": False,
     "cen": "the sloped exit ramp of a multi-storey public parking garage, "
            "bare grey concrete with a painted yellow edge line, rough "
            "board-formed walls marked with black tyre scuffs, galvanised "
            "pipe railings along the low side, square columns with numbered "
            "bays behind them, a fluorescent strip fitting overhead and a "
            "bright doorway of daylight at the bottom of the slope",
     "acao": "the knees have folded together on the slope on the way down to "
             "the car and both are going over at once, one of them catching "
             "the railing and the other coming down flat on the concrete, "
             "while the paint can bursts open and sends a wide white flood "
             "running down past a stopped car",
     "test": "three drivers have got out of the stopped cars behind them and "
             "stand at the top of the slope: two of them in windbreakers "
             "laughing with their car doors hanging open, and a woman in a "
             "tan work jacket crouched on the slope below them with a wrist "
             "in both hands",
     "mov": "As the line begins one of them hauls on the pipe railing with "
            "both hands while the other gets a palm onto the concrete and "
            "pushes up onto one knee. Halfway through the line the palm "
            "slides forward through the white flood and the knee comes back "
            "down on the slope. As the line ends the two drivers in "
            "windbreakers at the top of the slope laugh with their car doors "
            "hanging open and the woman in the tan work jacket hauls twice "
            "on the wrist and opens her hands again",
     "cam": "The shot is taken from the foot of the ramp at knee height, "
            "angled about twenty-five degrees up the slope so both bodies, "
            "the running paint and the drivers at the top sit in the same "
            "vertical frame",
     "luz": "Hard fluorescent strip light overhead against a blown-out "
            "doorway of daylight at the bottom, high contrast on the wet "
            "concrete.",
     "audio": "a steel paint can rolling on concrete, an idling engine, car "
              "doors standing open and two people laughing up the slope"},

    {"id": "festa_rua", "curto": "a travessa na festa de rua",
     "v": "grafo-B", "cluster": "B",
     "sexos": ("mulher", "homem"),
     "formas": ("riso", "dedo", "juizo", "impotencia"),
     "interior": False,
     "cen": "a residential street closed off for a block party in the late "
            "afternoon, ranch houses with mown front lawns and driveways down "
            "both sides, orange cones and a sawhorse across the corner, "
            "folding tables set end to end along the kerb under paper cloths, "
            "a charcoal grill smoking on a driveway apron, coolers on the "
            "tarmac and bunting strung between two mailboxes",
     "acao": "the ankle has rolled off the kerb edge with the foil tray "
             "carried out in both hands and the body is coming down half on "
             "the lawn and half on the tarmac, the tray turning over in the "
             "air and throwing potato salad, paper plates and plastic forks "
             "in a wide arc across the street",
     "test": "the two nearest tables have emptied onto the tarmac and eight "
             "neighbours are standing over it: two men in polo shirts "
             "laughing with paper cups still in their hands, a woman in a "
             "wide sun hat with one arm out pointing down at the upturned "
             "tray, and a couple in matching red aprons crouched at either "
             "side with an arm each in their hands",
     "mov": "As the line begins the body gets both hands into the grass at "
            "the kerb and drives up onto one knee. Halfway through the line "
            "the knee skids out sideways in the spilled potato salad and the "
            "shoulder comes back down on the tarmac. As the line ends the "
            "two men in polo shirts laugh with their paper cups still up, "
            "the woman in the wide sun hat pushes her pointing arm further "
            "out, and the couple in matching red aprons take an arm each, "
            "pull twice and let go",
     "cam": "The shot is taken from the middle of the closed street at hip "
            "height, angled down about twenty degrees toward the kerb so the "
            "fallen body, the thrown food and the whole ring of neighbours "
            "sit in one frame",
     "luz": "Warm low late-afternoon sun down the length of the street, long "
            "shadows across the tarmac, high contrast on the paper cloths.",
     "audio": "an aluminium tray clanging on tarmac, plastic forks "
              "skittering, a grill hissing and several people laughing at "
              "once"},

    # ⛔ A CAUSA E' O CORPO: o joelho dobra ao SUBIR o meio-fio. Nao ha'
    # gelo, oleo nem piso molhado — o que voa da mao (o caixote, os
    # pessegos) e' CONSEQUENCIA, nunca reu. A vergonha sao os dois homens
    # da fila do cafe, que nao largam o copo e riem de pe' em cima dela; a
    # feirante de sessenta puxa o pulso duas vezes, desiste e volta para
    # tras da mesa (a `impotencia`). ⚠️ O avental esta' NA FEIRANTE (RU19).
    {"id": "feira_caixote", "curto": "o joelho cede no meio-fio da feira",
     "v": "grafo-B", "cluster": "B",
     "sexos": ("mulher", "homem"),
     "formas": ("riso", "juizo", "impotencia"),
     "interior": False,
     "cen": "a small-town farmers market on a closed main street on a "
            "Saturday morning, white pop-up canopies down both sides, trestle "
            "tables under them heaped with produce in wooden crates, a high "
            "granite kerb between the stalls and the roadway, a bucket of cut "
            "sunflowers on the ground, a coffee stand with a queue at it, and "
            "brick storefronts behind the canopies",
     "acao": "the knee has folded coming up off the roadway onto the high "
             "granite kerb and the body is going down onto one hip against "
             "the kerb stone, the wooden crate tipping out of both arms and "
             "peaches and tomatoes rolling out under the trestle tables",
     "test": "the queue at the coffee stand has broken up and stands over "
             "it: two men in their forties in polo shirts laughing with cups "
             "still in their hands, a woman of about sixty in a stall apron "
             "crouched at the kerb with a wrist in both hands, and a "
             "teenager in a grey t-shirt who stops with a bag on his "
             "shoulder and stares",
     "mov": "As the line begins the body gets one hand onto the granite kerb "
            "and pushes to bring the trailing knee up onto it. Halfway "
            "through the line the hand rolls off the kerb edge on a loose "
            "peach and the knee comes back down into the roadway. As the "
            "line ends the two men in polo shirts from the coffee queue "
            "laugh with their cups still up and the woman in the stall apron "
            "pulls twice on the wrist she is holding and opens her hands "
            "again",
     "cam": "The shot is taken from the roadway at knee height a couple of "
            "paces off the kerb, angled about twenty degrees up so the body "
            "down against the kerb stone, the burst crate and the standing "
            "queue behind it sit in one frame",
     "luz": "Bright clear morning sun from the left, hard shadows under the "
            "canopies and blown highlights on the white cloth.",
     "audio": "a wooden crate cracking on stone, fruit rolling over asphalt, "
              "a coffee grinder running under a canopy and two men laughing "
              "close by"},

    # ⛔ A CAUSA E' O CORPO: as pernas cedem AO LEVANTAR da cadeira; o cafe
    # derramado e as cartelas sao consequencia. A vergonha e' o velho de
    # oitenta duas cadeiras adiante, que poe as duas maos em cima das
    # cartelas e vira o corpo inteiro para olhar, e a mulher de sessenta
    # que se levanta pela metade para enxergar por cima da fila. ⭐ Sessenta
    # pessoas SENTADAS num salao fechado e ninguem diz nada: e' por isso que
    # `plateia` e `silencio` cabem juntas aqui, com zero riso nos tres
    # campos — e as duas sao as formas mais escassas do pool.
    {"id": "bingo_salao", "curto": "as pernas cedem no bingo do salao",
     "v": "grafo-B", "cluster": "B",
     "sexos": ("mulher", "homem"),
     "formas": ("plateia", "silencio", "juizo"),
     "interior": True,
     "cen": "the hall of a volunteer fire company rented out for bingo night, "
            "a low acoustic tile ceiling with strip lights, long folding "
            "tables in rows filling the floor, moulded plastic chairs pushed "
            "in tight at them, paper cards and daubers spread over the "
            "tables, a raised platform with a wire ball cage at one end, and "
            "a serving hatch through to a kitchen at the back",
     "acao": "the legs have given out standing up from the chair halfway "
             "down a row and the body is coming down between two tables with "
             "one arm hooked over a table edge and dragging it, a paper cup "
             "going over on its side and cards and daubers sliding across "
             "the tiles",
     "test": "sixty players sit at the tables and every one of them has "
             "turned round without a word: a man of about eighty in a plaid "
             "shirt two seats along with both hands flat on his cards, a "
             "woman in her sixties in a lilac cardigan who half stands to "
             "see over the row, a couple at the next table who look at each "
             "other and back, and the caller on the platform who has stopped",
     "mov": "As the line begins the body pulls down on the edge of the "
            "folding table with the hooked arm and drives up onto one knee. "
            "Halfway through the line the folding table tips up on two legs "
            "and the arm slides off the laminate edge, and the knee goes "
            "back down on the tile. As the line ends the man in the plaid "
            "shirt two seats along turns right round with both hands flat on "
            "his cards, the woman in the lilac cardigan half stands to see "
            "over the row, and not one of them says anything",
     "cam": "The shot is taken from the end of the row at chest height, level "
            "and straight on down the gap between the tables, close enough to "
            "hold the body on the tiles and wide enough to keep the rows of "
            "turned faces behind it",
     "luz": "Flat cool strip lighting overhead with a faint green cast on the "
            "tiles and almost no shadow direction.",
     "audio": "a plastic chair skidding back over tile, a paper cup emptying "
              "under a table, a ball cage turning once on the platform and a "
              "hall that has gone quiet"},

    # -----------------------------------------------------------------------
    # ⭐ CLUSTER C — ESPETACULARIZACAO DA AJUDA: a maquina de CARGA resolve
    #    o corpo. A aresta e' DESUMANIZACAO — palete, guincho, elevador de
    #    mudanca, balanca de frete: o resgate acontece e e' ele que humilha, na
    #    frente de civis. ⛔⛔ `impotencia` SO' CABE AQUI QUANDO O BEAT E'
    #    ANTERIOR A' MAQUINA — regra reescrita em 2026-08-21, quando as tres
    #    entradas de reposicao entraram. A versao antiga proibia a forma no
    #    cluster inteiro, e o motivo era certo: *and nobody there could lift
    #    them* sobre um guincho erguendo em quadro e' a fala desmentindo o
    #    quadro. ⭐ Mas ela nao desmente quando o `test` mostra os CIVIS QUE
    #    TENTARAM PRIMEIRO e desistiram (quatro homens de mangas arregacadas,
    #    o homem de fleece que soltou o braco): ai' a maquina e' a
    #    CONSEQUENCIA da impotencia, nao a contradicao dela. ⛔ Sem esse beat
    #    de tentativa fracassada escrito no `test`, a forma continua proibida
    #    — as seis entradas antigas nao a declaram e nao devem passar a
    #    declarar. ⚠️ E ela custa alcance: `impotencia` era a terceira forma
    #    mais escassa do pool.
    #    (9 entradas)
    # ⛔⛔ MAQUINA QUE ERGUE GENTE TEM OPERADOR OU SERVICO NO MESMO QUADRO —
    #    conserto de 2026-08-21. Sem ninguem nos comandos o gerador ou INVENTA
    #    um motorista (e o elenco muda sozinho entre a IMAGE e o TAKE) ou deixa
    #    a maquina parada e o beat de abertura morre; e maquina erguendo pessoa
    #    sem servico identificado le' como trote, nao como resgate. O carro de
    #    bombeiros do `guindaste_parede` (v28/v40/v45, LIDO e renderizado) e' a
    #    forma validada disso.
    # -----------------------------------------------------------------------
    {"id": "empilhadeira_galpao",
     "curto": "a empilhadeira e o palete no galpao",
     "v": "grafo-C", "cluster": "C",
     "sexos": ("mulher", "homem"),
     "formas": ("riso", "juizo"),
     "interior": False,
     "cen": "the loading dock of a plain commercial warehouse in the late "
            "afternoon, bare concrete floor with yellow painted lane "
            "markings, grey steel racking stacked with shrink-wrapped boxes, "
            "a raised dock platform with black rubber bumpers, one roller "
            "shutter rolled all the way up onto a paved yard with a white box "
            "truck backed in, and a battered orange forklift with tall black "
            "mast rails",
     "acao": "the forks have just lifted and the loaded pallet is swinging a "
             "foot clear of the concrete with its boards bowing in the "
             "middle, and the body has caught the front slats with both "
             "hands as it tips, while a warehouse worker in a hi-vis vest "
             "holds the levers in the cab",
     "test": "at the open shutter stand four people who have no work here: "
             "two delivery drivers in polos laughing with their heads tipped "
             "together, a woman from the front counter with a flat hand over "
             "her mouth, and an older man in a windbreaker who came in off "
             "the yard and simply stares",
     "mov": "As the line begins the body flattens both palms on the pallet "
            "boards and pushes to get up off them. Halfway through the line "
            "the boards flex under the push and one hand skids off the slat, "
            "so the arm folds and the weight comes straight back down. As "
            "the line ends the two drivers in polos at the open shutter "
            "laugh out loud and the older man in the windbreaker only "
            "watches",
     "cam": "The shot is taken from the dock floor at knee height a few paces "
            "in front of the forks, angled about twenty degrees upward so the "
            "loaded pallet sits high in the frame and the group at the open "
            "shutter sits behind it",
     "luz": "Low warm late-afternoon sun flooding in through the open shutter "
            "from behind, long shadows raked across the concrete.",
     "audio": "a diesel forklift idling, hydraulics whining, pallet boards "
              "creaking and two men laughing near the shutter"},

    {"id": "porta_arrancada", "curto": "a porta arrancada da dobradica",
     "v": "grafo-C", "cluster": "C",
     "sexos": ("mulher", "homem"),
     "formas": ("riso", "dedo", "juizo"),
     "interior": False,
     "cen": "the front of a small American ranch house on a grey morning, "
            "white vinyl siding, a concrete stoop with two steps and a black "
            "iron rail, an empty doorway with the door and its frame lifted "
            "clean out and leaning against the siding, bare studs and torn "
            "paint around the opening, a white ambulance at the kerb with its "
            "rear doors open, a mowed lawn and a chain-link fence",
     "acao": "the door and its frame are out of the wall and tipping back "
             "against the siding, and the wide orange rescue board has "
             "jammed crosswise in the raw opening with the body sitting up "
             "on it, one shoulder hard against the bare stud, while two "
             "paramedics take the ends of the board",
     "test": "eleven neighbours have gathered on the lawn and the sidewalk "
             "and not one of them is leaving: two men in work jackets "
             "laughing openly, a woman in a green raincoat with a coffee mug "
             "pointing at the door leaning against the siding, and three "
             "more standing shoulder to shoulder at the fence line watching "
             "the board come through",
     "mov": "As the line begins the body hooks one hand on the raw stud of "
            "the opening and hauls to swing the shoulder clear. Halfway "
            "through the line the hand slides down the bare wood and the "
            "board drops back against the jamb. As the line ends the two men "
            "in work jackets on the lawn laugh out loud and the woman in the "
            "green raincoat pushes her pointing arm further out",
     "cam": "The shot is taken from above the lawn about three metres up, "
            "looking toward the stoop at roughly twenty-five degrees down, "
            "wide enough to hold the empty doorway, the door and frame "
            "leaning against the siding, the strapped board coming out over "
            "the stoop and the whole crowd of neighbours on the grass below "
            "it",
     "luz": "Flat cool overcast morning light with no shadow direction, a "
            "pale grey wash over the siding.",
     "audio": "ratchet straps clicking, boots on concrete, a radio squelch "
              "and several neighbours laughing and talking at once"},

    {"id": "elevador_mudanca", "curto": "o elevador de mudanca ate' a varanda",
     "v": "grafo-C", "cluster": "C",
     "sexos": ("mulher", "homem"),
     "formas": ("riso", "dedo", "juizo"),
     "interior": False,
     "cen": "the front of a three-storey red brick apartment block on a "
            "bright day, white-framed sash windows, black fire escape "
            "railings, small concrete balconies with wrought iron rails, a "
            "narrow strip of grass, and a flatbed truck at the kerb carrying "
            "an aluminium ladder hoist that runs at a steep angle from the "
            "truck bed up to an open third-floor balcony door",
     "acao": "the hoist platform has stalled two floors up with the "
             "aluminium track bowed under it and the nose tipped down, and "
             "the body is sliding forward against the orange webbing with "
             "both hands locked on the corner posts, while a uniformed mover "
             "works the hoist controls at the truck",
     "test": "the whole sidewalk has stopped to look up: two young men in "
             "team jerseys on bicycles laughing with their feet down on the "
             "kerb, a woman with grocery bags standing with her mouth open, "
             "a man in a grey hoodie in the doorway pointing straight up at "
             "the platform, and four residents leaning out of the "
             "second-floor windows",
     "mov": "As the line begins the body pulls hand over hand on the corner "
            "post to drag itself back up the tilted platform. Halfway "
            "through the line the webbing stretches out under the pull and "
            "the hand slips down the post, so the body slides forward again. "
            "As the line ends the two young men in team jerseys on the kerb "
            "laugh out loud and the man in the grey hoodie in the doorway "
            "points higher",
     "cam": "The shot is taken from the open third-floor balcony doorway at "
            "chest height, looking down along the aluminium ladder track so "
            "the loaded platform and the body on it fill the near frame, with "
            "the truck, the strip of grass and the people on the sidewalk "
            "reading small below",
     "luz": "Hard mid-morning sun from the left, sharp shadows across the "
            "brick, clear blue sky.",
     "audio": "an electric winch motor grinding, aluminium rails rattling, "
              "bicycle brakes and two men laughing on the sidewalk"},

    {"id": "balanca_carga", "curto": "a balanca de carga da loja de racao",
     "v": "grafo-C", "cluster": "C",
     "sexos": ("mulher", "homem"),
     "formas": ("plateia", "silencio", "juizo"),
     "interior": True,
     "cen": "the inside of a rural farm and feed store, tall grey steel "
            "shelving stacked with sacks and coils of rope, a scuffed "
            "concrete floor with a painted yellow border, hand-lettered "
            "cardboard price cards, a wooden service counter under a row of "
            "caged bulbs, a wide sliding barn door open onto a gravel yard, "
            "and a heavy freight platform scale of black steel with a big "
            "round white dial on a post",
     "acao": "the body has just stepped up onto the steel deck of the "
             "freight scale with both arms held out from the sides, and the "
             "deck has dropped hard on its springs while the long black "
             "pointer swings all the way round past the last mark on the "
             "white dial and knocks against its stop",
     "test": "the six customers waiting at the counter have all turned round "
             "to watch: a young woman in a denim jacket with a flat hand "
             "over her mouth, two men in caps who look at each other and "
             "then away, an older woman gripping her purse and staring, and "
             "a clerk in a canvas apron behind the counter",
     "mov": "As the line begins the body puts a hand on the dial post and "
            "lifts one foot to step back down off the deck. Halfway through "
            "the line the deck rocks under the shift, the foot comes "
            "straight back down and the pointer swings out past the last "
            "mark again. As the line ends every head at the counter has "
            "turned and the young woman in the denim jacket keeps a flat "
            "hand over her mouth",
     "cam": "The shot is taken from the aisle beside the scale at chest "
            "height, level and straight on, with the big white dial on its "
            "post close in the near frame so the black pointer reads large, "
            "and wide enough behind it to hold the steel deck and the whole "
            "line of customers at the counter",
     "luz": "Warm caged bulbs overhead mixed with cold daylight from the open "
            "barn door, soft directional light, dust in the air.",
     "audio": "the steel deck creaking under load, a dial pointer knocking "
              "against its stop, a ceiling fan turning and a store with no "
              "voices in it"},

    {"id": "guincho_piscina", "curto": "o guincho da piscina publica",
     "v": "grafo-C", "cluster": "C",
     "sexos": ("mulher", "homem"),
     "formas": ("riso", "juizo"),
     "interior": True,
     "cen": "the inside of a municipal indoor swimming pool, a high white "
            "steel roof with rows of hanging lamps, pale blue tiled walls, a "
            "six-lane pool with black lane lines and blue and white lane "
            "ropes, wet grey non-slip tiling around the edge, a stack of red "
            "rescue tubes, tiered bench seating along the far wall, and a "
            "white pool hoist bolted to the deck with a mesh sling seat on "
            "its arm",
     "acao": "the hoist arm has stalled bent over the water with the mesh "
             "sling seat swinging half clear of it, and the body sits in the "
             "seat with both hands clamped on the arm and the legs still "
             "down in the lane, water sheeting off the mesh, while a "
             "lifeguard holds the post",
     "test": "the swimmers have stopped in the lanes and hung on the rope to "
             "look, three of them in bright swim caps laughing with their "
             "goggles pushed up, and on the benches along the wall six "
             "people in street clothes have stood up, with a man in a red "
             "jacket among them shouting across the water while a lifeguard "
             "stands by the hoist post",
     "mov": "As the line begins the body hauls on the hoist arm and swings "
            "one leg toward the tiled edge. Halfway through the line the wet "
            "arm slides through both hands and the seat turns back out over "
            "the water with the leg dropping again. As the line ends the "
            "three swimmers in bright caps on the lane rope laugh out loud "
            "and the man in the red jacket on the bench shouts across the "
            "lanes",
     "cam": "The shot is taken from the pool deck at seated chest height, "
            "level with the sling seat and angled slightly down toward the "
            "water, wide enough to hold the hoist arm, the swimmers on the "
            "lane rope and the benches behind them",
     "luz": "Cold white overhead lamps with hard reflections dancing off the "
            "water onto the tiled walls.",
     "audio": "water sheeting off the sling, an electric hoist motor, "
              "echoing voices under a high roof and three swimmers laughing"},

    {"id": "guincho_reboque", "curto": "o guincho do reboque na valeta",
     "v": "grafo-C", "cluster": "C",
     "sexos": ("mulher", "homem"),
     "formas": ("riso", "juizo", "impotencia"),
     "interior": False,
     "cen": "the gravel shoulder of a two-lane country road in the early "
            "evening, a shallow grass ditch dropping away from the shoulder, "
            "a wire fence and a mowed field behind it, a white flatbed tow "
            "truck angled onto the shoulder with its amber beacon turning and "
            "its steel winch cable paid out down the slope, orange cones set "
            "out on the asphalt and a line of stopped cars behind them",
     "acao": "the winch cable has just snapped tight and the yellow recovery "
             "strap has cinched under the arms, and the body has come a foot "
             "up the wet grass on its back with both heels ploughing dark "
             "lines, while the tow truck above it squats down onto its rear "
             "springs",
     "test": "nine drivers have got out of the stopped cars and lined the "
             "shoulder above the ditch: two of them in ball caps laughing "
             "with their arms folded, a man in a hi-vis vest who came down "
             "two steps, put a hand out and went back up, and four more "
             "standing shoulder to shoulder at the cones looking down the "
             "slope",
     "mov": "As the line begins the body rolls onto one hip and drives an "
            "elbow down into the wet grass to help the cable. Halfway "
            "through the line the elbow sinks through the grass and the "
            "shoulder goes flat again while the strap slips a few inches "
            "back down the slope. As the line ends the two drivers in ball "
            "caps on the shoulder laugh out loud and the man in the hi-vis "
            "vest folds his arms",
     "cam": "The shot is taken from the road shoulder about three metres up, "
            "looking down the grass slope at roughly forty degrees over the "
            "heads of the line of drivers, so the yellow recovery strap and "
            "the body on the wet grass read clear and low in the frame with "
            "the standing drivers ranged across the top of it",
     "luz": "Low golden evening sun raking across the field from the right, "
            "long shadows down the ditch, warm sky.",
     "audio": "a winch drum ratcheting, cable creaking under load, an "
              "idling diesel engine and two men laughing at the roadside"},

    # ⭐ A VERGONHA E' A MULHER DE UNS CINQUENTA de vestido de verao: ela
    # baixa a mao da boca e comenta com os dois rapazes que riem. A
    # `impotencia` aqui e' LEGITIMA e vem ANTES da maquina — os quatro
    # homens de mangas arregacadas tentaram carregar e desistiram na frente
    # de todo mundo, e a concha e' a consequencia disso, nao a contradicao.
    # Quem dirige o trator e' bombeiro voluntario: SERVICO identificado.
    {"id": "carregadeira_feira",
     "curto": "a concha da carregadeira no parque de exposicoes",
     "v": "grafo-C", "cluster": "C",
     "sexos": ("mulher", "homem"),
     "formas": ("riso", "juizo", "impotencia"),
     "interior": False,
     "cen": "the main fairway of a county fairground on a hot afternoon, "
            "trampled dry grass between rows of white livestock tents, a red "
            "and white striped concession trailer with its awning propped up, "
            "hay bales stacked as seating along the lane, a wooden judging "
            "ring with pipe rails beyond, and a green farm tractor with a "
            "wide steel front loader bucket stopped across the lane",
     "acao": "the loader bucket has just come up two feet off the grass with "
             "the body sitting in it on a folded blanket, both hands "
             "gripping the front lip and one leg hanging over the edge, and "
             "the tractor has lifted light on its rear wheels while a "
             "volunteer firefighter works the levers",
     "test": "the fairway has stopped moving: two young men in feed-store "
             "caps laughing with their heads tipped together, a woman of "
             "about fifty in a sun dress with a flat hand over her mouth, and "
             "four older men in shirtsleeves who took an arm each a minute "
             "ago, pulled twice and let go",
     "mov": "As the line begins the body pushes down on the front lip of the "
            "bucket and tries to swing the hanging leg back in. Halfway "
            "through the line the bucket rocks on the hydraulics and the leg "
            "falls back over the edge, so both hands grab the lip again. As "
            "the line ends the two young men in feed-store caps laugh out "
            "loud and the woman in the sun dress lowers her hand and says "
            "something across to them",
     "cam": "The shot is taken from the fairway at chest height a few paces "
            "in front of the bucket, angled about twenty-five degrees upward "
            "so the raised bucket and the body in it fill the middle of the "
            "frame with the stopped fairway behind",
     "luz": "Hard high afternoon sun almost straight overhead, short black "
            "shadows on the trampled grass, bleached bright sky.",
     "audio": "a diesel tractor idling, hydraulics whining under the bucket, "
              "a livestock announcer echoing off the tents and two young men "
              "laughing close by"},

    # ⭐ A VERGONHA E' A VIZINHA DE UNS SESSENTA de cardiga: braco esticado
    # apontando para dentro da garagem e a voz chamando os dois rapazes que
    # riem sobre o capo. Sao VIZINHOS de verdade em quadro, que e' o que os
    # tres beats de `dedo` exigem (`neighbour`, `across the street`) — e
    # essa forma e' a mais escassa do pool. A talha e' operada por dois
    # bombeiros voluntarios; o adolescente so' espia, nao propaga a piada.
    {"id": "talha_garagem", "curto": "a talha de corrente na viga da garagem",
     "v": "grafo-C", "cluster": "C",
     "sexos": ("mulher", "homem"),
     "formas": ("riso", "dedo", "juizo"),
     "interior": False,
     "cen": "an attached suburban garage with the sectional door rolled all "
            "the way up onto a concrete driveway, an exposed timber ceiling "
            "beam, pegboard walls hung with tools, a chest freezer and "
            "stacked paint tins along one side, an oil-stained slab floor, a "
            "lawn tractor pushed back into the corner, and a red chain hoist "
            "shackled to the beam over the middle of the floor",
     "acao": "the chain hoist has taken up hard and the timber beam above it "
             "is bending visibly, and the body is a hand's width off the "
             "slab in the webbing sling with the toes still dragging on the "
             "concrete, while two volunteer firefighters haul the chain hand "
             "over hand",
     "test": "out on the driveway nine neighbours have come across and not "
             "one of them leaves: two men in their thirties in work jackets "
             "laughing over the hood of a parked car, a woman of about sixty "
             "in a cardigan with one arm out pointing straight into the "
             "garage, and a teenager leaning in past the door track to see "
             "the sling",
     "mov": "As the line begins the body grabs the taut chain above the hook "
            "with both hands and hauls to get the toes off the slab. Halfway "
            "through the line the chain bites into the fingers and both "
            "hands come off it, so the sling takes the whole load again and "
            "swings. As the line ends the two men in work jackets on the "
            "driveway laugh over the hood of the car and the woman in the "
            "cardigan points further into the garage",
     "cam": "The shot is taken from the driveway at hip height just outside "
            "the door track, angled about twenty degrees upward into the "
            "garage so the sling, the taut chain and the beam sit in one "
            "vertical frame with the neighbours in the near foreground",
     "luz": "Flat overcast daylight flooding in through the open door against "
            "the dim interior, weak shadows on the oil-stained slab.",
     "audio": "a chain hoist clicking link by link, webbing creaking under "
              "load, a car door left open chiming and two men laughing on the "
              "driveway"},

    # ⭐ A VERGONHA E' O HOMEM DE UNS QUARENTA de fleece: ele solta o braco
    # que segurava, se levanta e BALANCA A CABECA para a mesa atras dele —
    # desistir na frente de uma plateia sentada. A `impotencia` de novo vem
    # ANTES da maquina, e por isso a forma cabe num cluster onde o resgate
    # acontece em quadro. A equipe de resgate esta' uniformizada e so'
    # trabalha.
    {"id": "bolsa_ar_calcada",
     "curto": "as bolsas de ar erguendo na calcada do cafe",
     "v": "grafo-C", "cluster": "C",
     "sexos": ("mulher", "homem"),
     "formas": ("riso", "juizo", "impotencia"),
     "interior": False,
     "cen": "a downtown sidewalk outside a corner coffee house on a bright "
            "weekday morning, wide grey paving slabs, a low iron rail penning "
            "in a patio of small round tables under a green awning, a bicycle "
            "rack and a parking meter at the kerb, a shopfront window full of "
            "hanging plants, and a white fire department response truck "
            "stopped at the kerb with its rear doors open",
     "acao": "the orange lifting bladders underneath have just taken another "
             "stage of air and the body has come a hand's width up off the "
             "paving, both arms braced out on the slabs and one shoe left "
             "behind at the kerb, while two firefighters crouch at the air "
             "control panel",
     "test": "the whole patio has turned its chairs round and stays in them: "
             "two women in their twenties in denim jackets laughing into "
             "their cups, a man of about forty in a fleece who got down and "
             "took an arm before the crew came, pulled twice and stood back "
             "up, and four more at the rail leaning out over their tables to "
             "watch the bags fill",
     "mov": "As the line begins the body drives both braced arms down "
            "against the paving slabs to come up with the bags. Halfway "
            "through the line the elbows buckle outward and the shoulders go "
            "straight back down onto the slabs. As the line ends the two "
            "women in denim jackets at the patio tables laugh into their "
            "cups and the man in the fleece lets go of the arm he was "
            "holding and shakes his head",
     "cam": "The shot is taken from the kerb at knee height a couple of paces "
            "away, angled about fifteen degrees down along the paving so the "
            "inflating bags and the body sit low and close in the frame with "
            "the patio rail and the watching tables behind",
     "luz": "Hard low morning sun coming down the street from the left, long "
            "shadows across the paving, bright glare off the shopfront glass.",
     "audio": "compressed air hissing into the bladders, plastic creaking as "
              "they fill, a cup set down hard on a metal table and two women "
              "laughing behind the rail"},

    # ⛔ LAPIDE 2026-08-21 — `elevador_aeroporto` CORTADO: o ambilift e' SERVICO
    #    PADRAO de aeroporto (nao ha' vergonha num procedimento, ha' servico), e a
    #    camera punha o rosto a trinta passageiros de distancia. O `cinto_aviao` ja'
    #    e' dono do aviao e a vergonha dele e' real.


    # ⛔ LAPIDE 2026-08-21 — `tabua_igreja` CORTADO: colapsa com `banco_igreja`
    #    (a mesma igreja branca de tabua, a mesma congregacao muda em duas alas) e o
    #    prior treinado devolve CAIXAO — seis homens de terno carregando uma tabua a
    #    altura do ombro com um corpo deitado em cima.


    # ⛔ LAPIDE 2026-08-21 — `carrinho_carga` CORTADO: o julgamento cai nos DOIS
    #    HOMENS que empurram, nao no corpo — e ninguem transporta gente de pe' num
    #    carrinho de geladeira. A forma verdadeira dessa cena ja' e' o `maca_transferencia`.


    # -----------------------------------------------------------------------
    # ⭐ CLUSTER D — ROTA MEDICA: o equipamento de saude nao serve, nao
    #    fecha ou pede reforco. A aresta e' o OLHAR DO OUTRO num lugar onde a
    #    cortina aberta, o corredor ou a fila poem publico civil dentro de um
    #    exame — o funcionario e' AUTORIDADE e nao paga a vergonha sozinho.
    #    (10 entradas)
    # -----------------------------------------------------------------------
    {"id": "balanca_recepcao", "curto": "a balanca da recepcao trava",
     "v": "grafo-D", "cluster": "D",
     "sexos": ("mulher", "homem"),
     "formas": ("riso", "juizo"),
     "interior": True,
     "cen": "the front reception of a small American medical clinic on a "
            "weekday morning, a laminate counter with a sliding glass window "
            "and a queue rope on chrome posts, pale grey walls, a white drop "
            "ceiling with recessed fluorescent panels, a round wall clock, a "
            "rack of folded pamphlets, speckled vinyl flooring, and a low "
            "steel platform scale with a hinged upright column standing in "
            "the open beside the counter",
     "acao": "the second foot has just come down onto the steel plate and "
             "the platform has bottomed out hard against the vinyl, the "
             "heels hanging off the back edge and both hands clamped on the "
             "upright column, while the display window in the column has "
             "gone dark and blank",
     "test": "the receptionist leans out of the sliding window and calls "
             "something across the room, and the eight patients waiting in "
             "the row of chairs all look up: two young women in denim "
             "jackets in the front row laughing behind a folded pamphlet, a "
             "man in work boots staring openly with his elbows on his knees, "
             "and an older woman half turned in her seat",
     "mov": "As the line begins both hands haul down on the upright column "
            "and one heel drags back onto the plate to find the middle of "
            "it. Halfway through the line the heel slides straight off the "
            "rear edge again and the platform bottoms out under the sole "
            "with the display still dark. As the line ends the two young "
            "women in denim jackets in the front row of chairs laugh behind "
            "the folded pamphlet and the man in work boots on the waiting "
            "row leans further in over his knees",
     "cam": "The shot is taken from the far side of the waiting room at "
            "seated chest height, level and straight on, wide enough to hold "
            "the scale, the body on the platform and the whole row of waiting "
            "chairs behind it",
     "luz": "Flat cool fluorescent ceiling light with a faint green cast, "
            "almost shadowless, a weak window bounce from the left.",
     "audio": "the platform creaking under the soles, a printer chattering "
              "behind the counter, one voice calling across the room and "
              "two young women laughing"},

    {"id": "manguito_pressao", "curto": "o manguito que nao fecha",
     "v": "grafo-D", "cluster": "D",
     "sexos": ("mulher", "homem"),
     "formas": ("silencio", "juizo"),
     "interior": True,
     "cen": "an open triage bay in an American clinic, a half-drawn beige "
            "curtain on a ceiling track, a blue vinyl vitals chair with a "
            "padded armrest board, a rolling stand carrying a grey monitor "
            "and a coiled hose, a wall rail of sanitiser bottles and glove "
            "boxes, cream painted block walls, a white drop ceiling, and a "
            "waiting bench of moulded plastic chairs visible past the open "
            "curtain",
     "acao": "the upper arm has just been pressed flat down onto the padded "
             "board and rolled inward to bring the cuff together, and the "
             "two ends of the grey cuff have sprung a full hand apart across "
             "it, with the nurse's fingers still hooked in the loose end",
     "test": "past the open curtain, five patients on the waiting bench have "
             "all stopped to look: a man in a windbreaker holding a folded "
             "coat and staring straight in, a woman in a red raincoat who "
             "glances up from her lap and back down and up again, and two "
             "others leaning sideways to see round the curtain, the bay "
             "quiet enough to hear the hose swing",
     "mov": "As the line begins the arm rolls further inward on the padded "
            "board and the free hand pulls the loose end of the cuff across "
            "toward the other. Halfway through the line the two ends spring "
            "apart a full hand short and the free hand drops back onto the "
            "armrest board. As the line ends the man in the windbreaker on "
            "the waiting bench stares straight in through the open curtain "
            "and the woman in the red raincoat beside him looks up from her "
            "lap and down again",
     "cam": "The shot is taken from the foot of the vitals chair at chest "
            "height, angled about twenty degrees so the arm on the board sits "
            "low in the frame and the open curtain with the waiting bench "
            "sits behind it",
     "luz": "Even cool overhead fluorescent light with a faint blue cast, "
            "soft shadows falling under the armrest board.",
     "audio": "the rasp of the fastening pulling apart, a coiled hose "
              "swinging against the stand, shoes on vinyl and a bay gone "
              "quiet"},

    {"id": "cadeira_rodas_estreita",
     "curto": "a cadeira de rodas estreita demais",
     "v": "grafo-D", "cluster": "D",
     "sexos": ("casal",),
     "formas": ("impotencia", "riso", "juizo"),
     "interior": True,
     "cen": "the main lobby of a city hospital at midday, a polished terrazzo "
            "floor, a long wooden reception desk with a queue of people at "
            "it, tall glass entrance doors with a dark canopy beyond, potted "
            "ficus trees in square planters, rows of linked steel-frame "
            "waiting chairs, a wall of framed pastel prints and a bank of "
            "lifts with brushed steel doors",
     "acao": "one of them has just come down into the hospital wheelchair "
             "and stopped dead with the hips caught hard between the two "
             "padded armrests, while the other hauls back on the push "
             "handles until both front castors lift clear of the terrazzo",
     "test": "the queue at the reception desk has broken up to watch: a man "
             "in a suit with a document wallet under his arm laughing "
             "openly, a woman in a mustard coat beside him laughing too, an "
             "elderly couple who take a step forward and stop with their "
             "hands half raised, and a teenager up on the lift landing to "
             "see over the heads",
     "mov": "As the line begins both palms push down hard on the two padded "
            "armrests and the shoulders drive upward to lift clear of the "
            "seat. Halfway through the line the palms skid off the vinyl "
            "armrests, the weight drops back between them and the other "
            "keeps hauling on the push handles. As the line ends the man in "
            "the suit with the document wallet at the reception desk laughs "
            "out loud to the woman in the mustard coat beside him and the "
            "elderly couple by the lifts lower their half-raised hands",
     "cam": "The shot is taken from beside the reception desk at hip height, "
            "angled about twenty degrees down onto the wheelchair, wide "
            "enough to hold both of them, the tipping frame and the broken "
            "queue behind",
     "luz": "Bright even daylight flooding through the glass entrance and "
            "mixing with cool ceiling light, soft double shadows on terrazzo.",
     "audio": "the wheelchair frame knocking on stone, hard breathing, a "
              "lift chime and two people laughing near the desk"},

    {"id": "maca_transferencia", "curto": "quatro pessoas para mover na maca",
     "v": "grafo-D", "cluster": "D",
     "sexos": ("mulher", "homem"),
     "formas": ("silencio", "juizo"),
     "interior": True,
     "cen": "a corridor of a small American hospital, glossy pale green walls "
            "with a dented stainless bumper rail, a speckled grey vinyl "
            "floor, an open door to a treatment room, a linen cart and a "
            "hand-sanitiser dispenser against one wall, a row of moulded "
            "plastic chairs under a window at the far end, and a chrome "
            "transfer trolley with a thin blue mattress standing sideways in "
            "the corridor",
     "acao": "the near elbow has just driven down into the blue plastic "
             "slide board to shift the hips across onto the trolley, and the "
             "board has skidded out sideways over the mattress instead, with "
             "four orderlies in navy scrubs braced on a draw sheet gone "
             "bar-taut",
     "test": "the row of chairs at the far end of the corridor is full and "
             "every one of them has turned to look: a man with a walking "
             "stick between his knees leaning forward, a mother in a grey "
             "fleece holding a small girl still by the shoulder, and two "
             "older women side by side who watch the whole thing without a "
             "word",
     "mov": "As the line begins the near elbow drives down into the blue "
            "slide board and the far shoulder turns to push the hips across "
            "onto the trolley. Halfway through the line the elbow slides off "
            "the board, the draw sheet snaps taut in the four pairs of hands "
            "and the hips settle back where they started. As the line ends "
            "the man with the walking stick in the row of chairs leans "
            "further forward and the mother in the grey fleece in the same "
            "row holds the small girl still by the shoulder",
     "cam": "The shot is taken from the far end of the corridor at chest "
            "height, level and straight on, wide enough to hold the trolley, "
            "the stalled move and the full row of chairs in the same frame",
     "luz": "Flat cool corridor fluorescent light with a green cast, a bright "
            "daylight window burning out at the far end.",
     "audio": "the draw sheet creaking, trolley wheels shifting on vinyl, "
              "four people breathing hard and a corridor with no voices in "
              "it"},

    {"id": "avental_costas", "curto": "o avental que nao amarra atras",
     "v": "grafo-D", "cluster": "D",
     "sexos": ("mulher", "homem"),
     "formas": ("riso", "juizo"),
     "interior": True,
     "cen": "the changing alcove of an American imaging department, three "
            "curtained cubicles with striped fabric curtains on chrome "
            "tracks, a wall of narrow blue lockers with round key tags, a "
            "long wooden bench, a mirror in a chipped frame, pale beige "
            "walls, grey speckled flooring, and a corridor of waiting chairs "
            "opening straight off the alcove",
     "acao": "the body has stepped out of the cubicle still in its own "
             "street clothes and both fists have just dragged the two back "
             "ties of a pale blue paper gown together across the front, "
             "where they have fetched up a full hand short of each other",
     "test": "four people waiting on the bench and in the corridor chairs are "
             "all looking: two women in street clothes laughing quietly with "
             "their heads together, a man in a matching paper gown who grins "
             "and drops his eyes to the floor, and an older woman who watches "
             "the whole thing without blinking",
     "mov": "As the line begins both fists drag the two back ties around "
            "toward each other across the front of the held-up gown. Halfway "
            "through the line the ties fetch up a full hand short, the paper "
            "splits at one shoulder seam and both fists come down. As the "
            "line ends the two women in street clothes on the bench laugh "
            "into their hands and the man in the matching paper gown on the "
            "corridor chairs grins down at the floor",
     "cam": "The shot is taken from the corridor end of the alcove at chest "
            "height, angled slightly down, wide enough to hold the open "
            "cubicle curtain, the gown held up in one fist and the people "
            "watching from the bench",
     "luz": "Soft cool overhead light with one warm bulb over the mirror, "
            "gentle shadows across the beige walls.",
     "audio": "paper rustling in one fist, shoes on vinyl, a curtain ring "
              "sliding on its track and two women laughing quietly"},

    {"id": "mesa_exame_papel", "curto": "a mesa de exame cede",
     "v": "grafo-D", "cluster": "D",
     "sexos": ("mulher", "homem"),
     "formas": ("riso", "juizo"),
     "interior": True,
     "cen": "the open fast-track treatment area of an American urgent care "
            "clinic, four bays down one wall divided by half-drawn curtains "
            "on ceiling tracks with a nurses' station on castors in the "
            "middle of the floor, cream vinyl exam tables with white paper "
            "rolls at the head end in each bay, a wall chart of the human "
            "skeleton, a stainless sink with a paper-towel dispenser, a "
            "rolling stool, cream painted walls, a white drop ceiling with "
            "fluorescent panels, and a companion chair at the foot of every "
            "table",
     "acao": "the weight has just come down onto the near exam table and the "
             "base has folded under one end, so the cream vinyl top is "
             "dropping into a hard slant with the white paper roll tearing "
             "open along it in one long ragged split",
     "test": "the far exam table and the companion chairs are occupied and "
             "everyone in the bay has turned: a teenager in a red hoodie on "
             "the far table laughing out loud with a hand over his eyes, his "
             "mother beside him laughing as well, and an older man on a "
             "companion chair leaning round the pushed-back curtain to see",
     "mov": "As the line begins both hands go back onto the dropping table "
            "top and the arms lock to push the hips up off it. Halfway "
            "through the line the vinyl slides out from under both palms, "
            "the torn paper roll goes with them and the hips slide further "
            "down the slant. As the line ends the teenager in the red hoodie "
            "on the far exam table laughs out loud behind a hand and his "
            "mother in the companion chair beside him laughs with him",
     "cam": "The shot is taken from the sink side of the bay at standing "
            "chest height, angled about twenty degrees down onto the dropped "
            "table, wide enough to hold the torn paper and the occupied far "
            "table behind it",
     "luz": "Flat cool fluorescent ceiling light, almost shadowless, with a "
            "faint green institutional cast on the cream vinyl.",
     "audio": "a table base buckling under the weight, paper tearing in one "
              "long rip, a stool caster rolling and a boy laughing"},

    {"id": "tomografo_estreito", "curto": "o tomografo nao aceita",
     "v": "grafo-D", "cluster": "D",
     "sexos": ("mulher", "homem"),
     "formas": ("silencio", "juizo"),
     "interior": True,
     "cen": "the corridor outside an imaging suite in an American hospital, a "
            "wide doorway standing open onto a bright scanner room where the "
            "white ring of the machine and its narrow motorised table fill "
            "the middle of the floor, pale grey walls with a yellow and black "
            "warning band round the door frame, a run of moulded chairs along "
            "the corridor, and a fire door with a small window at the end",
     "acao": "both hands have just pressed flat into the narrow scanner "
             "mattress to swing the hips up off the step stool, and the near "
             "shoulder has caught hard against the white ring of the "
             "machine, the shoulders standing a hand wider than the table on "
             "each side",
     "test": "six patients in paper gowns are waiting on the corridor chairs "
             "and every one of them can see straight through the open door: "
             "a man with his arms folded watching without moving, a woman "
             "with a coat folded on her knees who looks down at her lap and "
             "back up twice, and a couple who lean together and say nothing",
     "mov": "As the line begins both palms press down into the narrow "
            "mattress and the hips lift a few inches off the step stool. "
            "Halfway through the line the near shoulder catches on the white "
            "ring of the machine and the hips come straight back down onto "
            "the stool. As the line ends the man with his arms folded on the "
            "corridor chairs watches through the open doorway and the woman "
            "with the coat folded on her knees beside him looks down at her "
            "lap and up again",
     "cam": "The shot is taken from inside the scanner room at seated chest "
            "height, a little to the side of the narrow table so the body on "
            "the edge of it and the shoulders standing a hand wider than the "
            "mattress on each side fill the near frame, with the technologist "
            "in the doorway and the corridor of waiting patients reading "
            "through the open door behind",
     "luz": "Cool even fluorescent corridor light against a brighter clinical "
            "white spilling out of the scanner room.",
     "audio": "a low mechanical hum from the scanner room, a step stool "
              "shifting on the floor, quiet talk in the doorway and a "
              "corridor with no other voices"},

    {"id": "andador_farmacia", "curto": "o andador dobra na fila da farmacia",
     "v": "grafo-D", "cluster": "D",
     "sexos": ("casal",),
     "formas": ("plateia", "riso", "juizo"),
     "interior": True,
     "cen": "the prescription counter at the back of an American drug store, "
            "a laminate counter with a raised divider and a pick-up bell, "
            "shelves of white paper bags in alphabetical bays behind it, an "
            "aisle of shampoo and vitamins running back toward the front of "
            "the store, waxed cream tile flooring, bright white ceiling "
            "panels, and a roped waiting line with a painted privacy stripe "
            "on the floor",
     "acao": "both of them have their hands on the same folding walking "
             "frame and it has just scissored shut sideways under the push, "
             "so the two of them are going down together onto the waxed tile "
             "with the folded aluminium frame across the shins of both",
     "test": "the whole line behind the privacy stripe turns at once: a "
             "woman with a basket on her arm laughing out loud, a man in a "
             "ball cap behind her laughing as well, an older customer who "
             "steps back into the vitamin aisle to keep watching, and a "
             "clerk who stands at the counter with a paper bag in each hand",
     "mov": "As the line begins one hand clamps the near upright of the "
            "folded frame and both of them haul on it to drag it open again "
            "underneath them. Halfway through the line the aluminium joint "
            "slams shut a second time and the frame skids flat across the "
            "tile out of reach of both. As the line ends the woman with the "
            "basket on her arm in the waiting line laughs out loud and the "
            "man in the ball cap behind her laughs with her",
     "cam": "The shot is taken from the pharmacy counter at hip height, "
            "angled about twenty degrees down onto the tile, wide enough to "
            "hold the folded frame, both of them and the whole waiting line "
            "behind the stripe",
     "luz": "Hard even white retail ceiling light, bright and shadowless, "
            "with a cool cast on the waxed tile.",
     "audio": "aluminium tubing clattering on tile, a basket handle "
              "rattling, several people laughing and a pick-up bell ringing "
              "once"},

    # ⭐ A VERGONHA E' A MULHER DE UNS QUARENTA que para no meio de
    # descascar a laranja e fica com ela nas duas maos, sem desviar o
    # olhar. A prova e' POSICAO e nunca numero: duas camas no mesmo chao,
    # uma visivelmente mais larga. ⛔ Ela fica DE PE', com a propria roupa e
    # uma bolsa de lona — nada de avental no corpo dela (RU19). Zero riso
    # em `test`/`mov`/`audio`, entao `silencio` nao desmente o quadro.
    {"id": "cama_ala",
     "curto": "a cama da enfermaria trocada por uma mais larga",
     "v": "grafo-D", "cluster": "D",
     "sexos": ("mulher", "homem"),
     "formas": ("silencio", "juizo"),
     "interior": True,
     "cen": "a four-bed ward in a small American hospital in the middle of "
            "the day, pale blue curtains bunched on ceiling tracks between "
            "the bays, a speckled vinyl floor, a window with horizontal "
            "blinds at the far end, a wheeled overbed table and a vinyl "
            "visitor chair beside each bed, a sanitiser dispenser by the "
            "door, and one bay standing empty with its bed pushed out into "
            "the middle of the floor",
     "acao": "one hand and the canvas bag have just come down on the edge of "
             "the ordinary bed to sit, and the two porters in navy tunics "
             "are rolling that bed out from under the hand toward the door "
             "while a much broader one comes in over the same floor marks",
     "test": "the other three beds have visitors and every one of them "
             "watches without a word: a man of about seventy sitting up "
             "against his pillows who folds his newspaper down onto his lap, "
             "a woman in her forties who stops halfway through peeling an "
             "orange, and a young couple in the far bay who look at each "
             "other and then back",
     "mov": "As the line begins one hand and the canvas bag press down on "
            "the edge of the ordinary bed and the hips start to lower toward "
            "it. Halfway through the line the bed rolls out from under the "
            "hand, the bag swings back up into both arms and the hips come "
            "up to standing again. As the line ends the man with the folded "
            "newspaper in the far bed lowers it onto his lap and the woman "
            "with the orange in the visitor chair stops peeling and holds it "
            "in both hands",
     "cam": "The shot is taken from the door of the ward at chest height, "
            "level and straight on down the middle of the floor, close enough "
            "to hold the waiting body and the incoming bed together with the "
            "three occupied beds ranked behind them",
     "luz": "Flat cool ceiling fluorescent light with a hard band of daylight "
            "coming through the blinds at the far end.",
     "audio": "bed castors rumbling over vinyl, a bag handle creaking in two "
              "hands, a monitor beeping somewhere down the corridor and a "
              "ward with no voices in it"},

    # ⭐ A VERGONHA E' O HOMEM DE UNS TRINTA na cadeira ao lado, que RI ALTO
    # com o babador de papel ainda preso no pescoco — PACIENTE igual a ela,
    # nao funcionario. A auxiliar so' afasta a bandeja: ela nao abre o `mov`
    # e nao e' a vergonha. O menino de dez ri atras do braco da mae e nao
    # propaga nada. A prova e' POSICAO (o encosto parado no meio do curso, a
    # base no fim do batente), nunca um mostrador.
    {"id": "cadeira_dentista",
     "curto": "a cadeira do dentista para no meio do curso",
     "v": "grafo-D", "cluster": "D",
     "sexos": ("mulher", "homem"),
     "formas": ("riso", "juizo"),
     "interior": True,
     "cen": "an open-plan dental surgery in an American strip-mall clinic, "
            "three treatment bays side by side with no doors between them, "
            "mint green walls, a white drop ceiling, an articulated lamp arm "
            "swung over each chair, rolling stools and instrument trays on "
            "swing arms, a corner sink with a paper towel dispenser, and a "
            "glass door standing open onto a waiting area of moulded chairs",
     "acao": "the shoulders have just gone back into the treatment chair and "
             "the post has dropped straight through its travel to the bottom "
             "of the stroke, leaving the backrest stalled halfway down and "
             "both feet flat on the floor as the assistant swings the tray "
             "clear",
     "test": "everyone in the next bay and the open waiting area is watching: "
             "a man of about thirty in the next chair laughing out loud with "
             "the paper bib still clipped at his neck, a boy of about ten "
             "laughing behind his mother's arm, and a woman in a work jacket "
             "who lowers her magazine and stares in through the open door",
     "mov": "As the line begins both hands push down on the armrests and the "
            "shoulders drive back to carry the backrest the rest of the way "
            "down. Halfway through the line the backrest stops dead where it "
            "is, the post sinks the last inch under the push and both feet "
            "come down flat on the floor again. As the line ends the man in "
            "the next bay with the paper bib still clipped at his neck "
            "laughs out loud and the woman in the work jacket in the waiting "
            "area lowers her magazine and stares in",
     "cam": "The shot is taken from the foot of the treatment chair at seated "
            "chest height, angled about fifteen degrees down onto the dropped "
            "chair, close enough to hold the body in it and wide enough to "
            "keep the next bay and the open door in the same frame",
     "luz": "Cold white overhead panels with the treatment lamp arm throwing "
            "a small hard pool of light across the chair.",
     "audio": "a hydraulic post sighing down under the chair, an instrument "
              "tray swinging on its arm, a suction line running dry and a man "
              "laughing one bay over"},

    # -----------------------------------------------------------------------
    # ⭐ CLUSTER E — NAO-ENCAIXE: o vao padrao recusa o corpo e nada
    #    quebra. A aresta e' DESUMANIZACAO pela MEDIDA: catraca, trava de
    #    seguranca, cinto, poltrona, provador — o mundo diz nao e uma fila
    #    parada atras assiste. (10 entradas)
    # ⛔⛔ O FUNCIONARIO PODE FICAR EM QUADRO; O PRIMEIRO BEAT DO `mov` NUNCA E'
    #    ELE, E A VERGONHA NUNCA E' ELE — conserto de 2026-08-21, e era o maior
    #    defeito de LOTE da varredura. Onze de onze entradas deste cluster
    #    tinham um uniformizado com o braco ou a palma estendidos no mesmo
    #    lugar do quadro, e ONZE DE ONZE abriam o `mov` nesse gesto: onze
    #    videos com o mesmo movimento no mesmo segundo nao sao onze videos.
    #    ⭐ Nas nove LIDAS quem humilha e' sempre CIVIL — o bombeiro e a
    #    manicure aparecem trabalhando, nunca julgando. O `mov` abre no
    #    PUBLICO; o funcionario, quando age, age no meio ou no fim.
    # -----------------------------------------------------------------------
    {"id": "catraca_metro", "curto": "a catraca do metro nao passa",
     "v": "grafo-E", "cluster": "E",
     "sexos": ("mulher", "homem"),
     "formas": ("silencio", "juizo"),
     "interior": True,
     "cen": "the fare hall of a big-city subway station, white tiled walls "
            "with a wide grout grid, a scuffed grey terrazzo floor, a long "
            "row of waist-high stainless steel fare gates with clear glass "
            "barrier panels, a lit glass attendant booth to one side, steel "
            "columns painted dark green and a staircase down to the platform "
            "behind",
     "acao": "the glass barrier panels are folded right back into the "
             "stainless housings with the lane standing open, and the "
             "leading foot has just carried the step into it, so the hips "
             "have jammed against both stainless posts at once with one hand "
             "flat on each",
     "test": "a station attendant in a navy uniform vest has stepped out of "
             "the booth and stands back with one flat palm raised, talking "
             "with the free hand down at his side, and the queue behind the "
             "gates has stopped: a man in a work coat staring ahead, two "
             "women with shopping bags turned fully sideways to look, and a "
             "teenager who looks down and back up",
     "mov": "As the line begins both hands push off the stainless posts and "
            "the leading shoulder drives forward to carry the hips through "
            "the open lane. Halfway through the line the palms slide down "
            "the posts, the hips stay wedged between them and the trailing "
            "foot comes back down behind the gate. As the line ends the man "
            "in the work coat at the head of the queue stares straight ahead "
            "and the two women with shopping bags behind him turn fully "
            "sideways to look",
     "cam": "The shot is taken from the platform side of the gates at chest "
            "height, level and straight on, wide enough to hold the open "
            "barrier panels, the stopped body, the attendant and the whole "
            "queue behind",
     "luz": "Flat cool fluorescent light from overhead panels, almost no "
            "shadow direction, a faint green cast on the white tile.",
     "audio": "a fare gate chime repeating, shoes shifting on terrazzo, a "
              "distant train rumble and a hall with no voices in it"},

    {"id": "trava_brinquedo", "curto": "a trava do brinquedo nao fecha",
     "v": "grafo-E", "cluster": "E",
     "sexos": ("mulher", "homem"),
     "formas": ("riso", "juizo"),
     "interior": False,
     "cen": "the loading platform of a small amusement park ride on a hot "
            "afternoon, a steel and fibreglass car painted red and yellow "
            "parked at the gate, a chequer-plate steel deck, a chain-link "
            "queue rail zigzagging back under a striped canvas awning, "
            "painted safety posts and a green treeline beyond the ride track",
     "acao": "both hands have just hauled the padded black over-the-shoulder "
             "harness down onto the chest and it has stopped short and swung "
             "straight back up, so it stands wide open above the seat with "
             "the body still down in the car and both hands back on the grab "
             "bar",
     "test": "the ride operator, a young man in a red polo, stands at the "
             "side of the car with both hands off the harness and one arm out "
             "flat, shaking his head, and the queue at the rail has stopped: "
             "two teenage girls laughing behind their hands, a father with a "
             "small boy on his shoulders staring, and an older man leaning on "
             "the rail",
     "mov": "As the line begins both hands take the padded harness and haul "
            "it down onto the chest with the shoulders pushed back into the "
            "seat. Halfway through the line the harness stops a hand short "
            "of the latch and swings straight back up wide open again over "
            "the seat. As the line ends the two teenage girls at the "
            "chain-link queue rail laugh behind their hands and the father "
            "with the small boy on his shoulders stares from the rail",
     "cam": "The shot is taken from the platform beside the car at seated "
            "chest height, angled about twenty degrees down onto the open "
            "harness, wide enough to hold the car, the operator and the queue "
            "at the rail behind",
     "luz": "Hard high afternoon sun from the upper right, crisp shadows on "
            "the steel deck, bright hazy sky.",
     "audio": "a ride motor idling, a safety buzzer sounding twice, girls "
              "laughing near the rail and a crowd murmuring"},

    {"id": "cinto_aviao", "curto": "o cinto do aviao nao alcanca",
     "v": "grafo-E", "cluster": "E",
     "sexos": ("mulher", "homem"),
     "formas": ("silencio", "juizo"),
     "interior": True,
     "cen": "the coach cabin of a narrow-body airliner during boarding, tan "
            "moulded plastic sidewalls, three-abreast rows of navy blue seat "
            "covers with worn grey headrest cloths, a low curved ceiling with "
            "open overhead bins, a narrow aisle in patterned carpet, small "
            "oval windows full of bright apron light and a galley curtain at "
            "the front",
     "acao": "both hands have just dragged the two ends of the seat belt "
             "toward each other across the lap and the buckle tongue has "
             "stopped several inches short of the socket, with the long grey "
             "extender strap held out over the armrest beside them",
     "test": "a flight attendant in a navy uniform stands in the aisle "
             "holding the extender strap out, speaking with her weight back, "
             "while the boarding queue behind has stopped moving: a man with "
             "a bag on his shoulder looking down the row, two women in the "
             "opposite seats turned fully around, and a teenager who stares "
             "and then looks away",
     "mov": "As the line begins both hands pull the two belt ends in toward "
            "each other across the lap and the shoulders press back into the "
            "seat. Halfway through the line the buckle tongue stops short of "
            "the socket, the webbing runs out of slack and both hands come "
            "back down onto the armrests. As the line ends the man with the "
            "bag on his shoulder in the stalled aisle looks down the row and "
            "the two women in the opposite seats turn fully around",
     "cam": "The shot is taken from the aisle right beside the row at seated "
            "chest height, turned in toward the seats so the two open belt "
            "ends across the lap and the grey extender strap in the "
            "attendant's hand read large in the near frame, with the stalled "
            "boarding queue running back down the aisle behind",
     "luz": "Cold overhead cabin light with hard white apron daylight "
            "flooding in through the oval windows, high contrast on the seat "
            "backs.",
     "audio": "a cabin ventilation hiss, a seat belt buckle tongue clicking "
              "against the socket, bags shifting in the aisle and no "
              "talking"},

    {"id": "poltrona_cinema", "curto": "a poltrona do cinema com braco fixo",
     "v": "grafo-E", "cluster": "E",
     "sexos": ("casal",),
     "formas": ("plateia", "silencio", "juizo"),
     "interior": True,
     "cen": "the front of a small cinema auditorium with the house lights up, "
            "rows of dark red fold-down seats with worn fabric and fixed dark "
            "wooden armrests, a black rubber-matted aisle with low step "
            "lights, plain grey acoustic wall panels, a blank white screen "
            "behind a bunched black curtain and a projection window high on "
            "the rear wall",
     "acao": "the two of them have just gone down together into the two "
             "seats either side of one fixed wooden armrest and both have "
             "stopped hard against it, the hips of each pressed to that "
             "armrest and the two folded seat pans still empty underneath",
     "test": "an usher in a maroon waistcoat stands at the end of the row "
             "with one flat palm raised, speaking across the seats from the "
             "aisle end, and the whole audience has turned round to look: a "
             "couple in matching windbreakers two rows back staring over the "
             "seat backs, a woman with a paper cup frozen at her mouth, and "
             "a man who looks and then looks at the floor",
     "mov": "As the line begins both of them grip the seat backs in front "
            "and lower together toward the two seat pans either side of the "
            "shared armrest. Halfway through the line the hips of each stop "
            "hard against that one armrest, the two seat pans stay empty and "
            "the two of them come back up onto their feet. As the line ends "
            "the couple in matching windbreakers two rows back stare over "
            "the seat backs and the woman with the paper cup in the aisle "
            "row holds it frozen at her mouth",
     "cam": "The shot is taken from the row in front at seated head height, "
            "turned back along the row so the empty folded seat, both fixed "
            "wooden armrests and the hands on them read large in the near "
            "frame, with the usher at the aisle end and the turned faces of "
            "the audience behind",
     "luz": "Warm house lights up at half strength, soft pools from the "
            "ceiling fittings, deep shadow under the seats.",
     "audio": "seat springs creaking, a paper cup set down on an armrest, "
              "feet shifting on rubber matting and an auditorium gone quiet"},

    {"id": "provador_loja", "curto": "a cortina do provador nao fecha",
     "v": "grafo-E", "cluster": "E",
     "sexos": ("mulher",),
     "formas": ("plateia", "riso", "juizo"),
     "interior": True,
     "cen": "the fitting room corridor of an ordinary American clothing "
            "store, four narrow cubicles with slatted white doors and heavy "
            "grey fabric curtains on chrome rails, a beige carpet strip down "
            "the middle, a chrome return rack hung with dresses and jeans, "
            "warm ceiling spots and the bright shop floor with round clothing "
            "racks beyond",
     "acao": "one hand has just dragged the grey curtain the whole way along "
             "its chrome rail and it has fetched up a foot short of the "
             "frame, leaving the cubicle standing open to the corridor, with "
             "a dress on its hanger held up against the front in the other "
             "hand",
     "test": "the customers waiting in line with clothes on their arms have "
             "all stopped where they stand: two young women laughing behind a "
             "folded jacket, an older woman staring straight into the open "
             "gap, and a man at the return rack who turns round, looks, and "
             "turns back to the rack",
     "mov": "As the line begins one hand hauls the grey curtain along the "
            "chrome rail toward the frame with the whole arm behind it. "
            "Halfway through the line the curtain runs out at the same foot "
            "short of the frame, the rings jam on the rail and the arm comes "
            "down. As the line ends the two young women behind the folded "
            "jacket in the waiting line laugh out loud and the older woman "
            "behind them in the line stares straight into the open gap",
     "cam": "The shot is taken from the far end of the fitting room corridor "
            "at chest height, level and straight on, wide enough to hold the "
            "open gap in the curtain and the whole waiting line",
     "luz": "Warm ceiling spots down the corridor with cooler flat light off "
            "the shop floor behind, soft shadows on the carpet.",
     "audio": "hangers scraping on a chrome rail, a curtain ring dragging, "
              "two women laughing and shop floor chatter behind"},

    # ⭐ A VERGONHA SAO OS DOIS HOMENS DE UNS QUARENTA na caminhonete da
    # fila ao lado: eles giram o corpo inteiro para a porta aberta e riem
    # um para o outro. O vendedor da' a volta no carro e fica girando a
    # chave — ele NAO abre o `mov` e nao e' a humilhacao, so' o cenario
    # dela. ⛔ Entrada de CASAL: quem coloca os dois no espaco e' o `acao`
    # (um preso na soleira, o outro no para-lama), nunca a frase de elenco.
    # ⚠️ A fala e' `neither of them` e nao `%(suj)s`: com o slot ela saia
    # *"This was Marjorie before, Marjorie and her husband could not..."* —
    # o nome duas vezes na mesma respiracao e quatro palavras de orcamento
    # gastas para repeti-lo.
    {"id": "carro_concessionaria",
     "curto": "o banco do carro na concessionaria",
     "v": "grafo-E", "cluster": "E",
     "sexos": ("casal",),
     "formas": ("riso", "juizo"),
     "interior": False,
     "cen": "the front row of a small used car lot on a bright weekday "
            "morning, rows of sedans and pickups parked nose out on fresh "
            "black asphalt, triangular pennant lines strung on wires "
            "overhead, a low glass sales office with a clipped shrub either "
            "side of the door, a flagpole at the kerb, and one compact silver "
            "sedan pulled out of the row with its driver's door standing wide "
            "open",
     "acao": "one of them has just dropped down into the driver's seat and "
             "stopped half in the doorway with the hips wedged between the "
             "seat bolster and the wheel, while the other has both hands on "
             "the top of the open door and is hauling it wider on its hinge",
     "test": "the salesman has walked round to the far side of the car and "
             "stands there turning a key fob over, and the customers out on "
             "the lot have stopped where they are: two men in work shirts "
             "looking over a truck bed laughing at each other, and a woman "
             "of about thirty holding a toddler by the hand who watches and "
             "does not move on",
     "mov": "As the line begins the hands on the wheel rim haul the chest in "
            "toward the column while the other pushes both palms against the "
            "shoulder from the doorway. Halfway through the line the hips "
            "stay wedged at the bolster, the near foot slides back off the "
            "sill and the door hinge creaks wider. As the line ends the two "
            "men in work shirts at the truck bed in the next row laugh and "
            "turn right round toward the open door",
     "cam": "The shot is taken from the lane between the rows at hip height a "
            "few paces off the open door, angled about ten degrees up so the "
            "open door, the body wedged at the sill and the two watching men "
            "beyond the truck bed sit in one frame",
     "luz": "Hard clear morning sun from the right, sharp shadows under the "
            "parked cars, strong glare off the windscreens.",
     "audio": "a car door hinge creaking under load, a key fob chirping once, "
              "pennant lines snapping in the wind and two men laughing across "
              "the lot"},

    # ⭐ A VERGONHA SAO OS DOIS HOMENS DE CHAPEU DE PALHA, cinquentoes, JA'
    # MONTADOS: eles riem um para o outro POR CIMA da cabeca dela, de cima
    # para baixo, que e' a geometria da humilhacao inteira. Os outros dois
    # desceram, tentaram empurrar pela bota e voltaram para a sela sem
    # dizer nada — e' o que sustenta `impotencia` sem maquina nenhuma. O
    # tratador so' leva o animal: funcionario trabalhando, nunca a vergonha.
    {"id": "cavalo_trilha", "curto": "o cavalo da trilha levado embora",
     "v": "grafo-E", "cluster": "E",
     "sexos": ("mulher", "homem"),
     "formas": ("riso", "juizo", "impotencia"),
     "interior": False,
     "cen": "the yard of a trail riding stable on a clear morning, a red "
            "timber barn with its sliding door pushed back, a dirt turning "
            "circle churned up by hooves, a paddock fence of split rails with "
            "saddles laid over the top rail, a wooden mounting block of three "
            "steps set out in the open, a water trough on a stand, and six "
            "saddled horses held in a loose line by their reins",
     "acao": "one boot has just swung up toward a stirrup hanging level with "
             "the waist and both hands have taken the saddle to pull, and "
             "the wrangler has already walked the horse a stride clear of "
             "the mounting block, so the raised boot is out over bare dirt",
     "test": "the five riders already up in their saddles have turned their "
             "horses to watch: two men in their fifties in straw hats "
             "laughing across at each other, a woman of about twenty-five who "
             "covers her mouth with the hand holding the rein, and two more "
             "who got down a minute ago, took a boot each to push and climbed "
             "back up without a word",
     "mov": "As the line begins both hands haul down on the saddle and the "
            "raised boot reaches again for the stirrup hanging level with "
            "the waist. Halfway through the line the saddle leather slides "
            "through both hands, the boot comes back down onto the top step "
            "and the mounting block rocks under it. As the line ends the two "
            "men in straw hats up in their saddles laugh across at each "
            "other over the block and the young woman on the near horse "
            "covers her mouth with the hand holding the rein",
     "cam": "The shot is taken from the yard at chest height a few paces from "
            "the block, angled about ten degrees up so the empty stirrup, the "
            "body on the top step and the mounted riders behind all sit in "
            "one frame",
     "luz": "Clear low morning sun from the side, long shadows raked across "
            "the dirt, pale blue sky over the barn roof.",
     "audio": "hooves shifting on packed dirt, a stirrup leather creaking, "
              "bits and reins jingling and two men laughing from the saddle"},

    # ⭐ A VERGONHA E' O HOMEM DE UNS SESSENTA dois degraus abaixo: mao no
    # corrimao, cabeca erguida, olhando para cima sem desviar um segundo —
    # e a mulher de corta-vento que estica o pescoco de lado para ver por
    # cima dele. Doze pessoas presas atras dela numa escada onde ninguem
    # passa e ninguem fala: e' a forma `silencio` com o quadro pagando o
    # que a fala promete (zero riso em `test`/`mov`/`audio`).
    {"id": "escada_farol",
     "curto": "a escada em caracol do farol estreita demais",
     "v": "grafo-E", "cluster": "E",
     "sexos": ("mulher", "homem"),
     "formas": ("silencio", "juizo"),
     "interior": True,
     "cen": "the inside of a coastal lighthouse tower open to visitors, a "
            "whitewashed brick shaft curving away overhead, a black cast-iron "
            "spiral stair bolted to the wall and winding up out of the frame, "
            "worn treads in a pierced pattern, a thin iron handrail on the "
            "outer edge, a small arched window letting in one shaft of "
            "daylight, and a rope barrier at the foot of the stair",
     "acao": "the leading foot has just gone up onto the tread where the "
             "shaft narrows and the hips have wedged between the thin iron "
             "handrail and the whitewashed brick, one shoulder pressed flat "
             "to the wall and both hands locked on the rail",
     "test": "the tour group is backed up on the treads underneath and "
             "nobody speaks: a man of about sixty in a fleece vest two steps "
             "down with his hand on the rail looking straight up, a woman in "
             "a windbreaker who turns her head sideways to see past him, a "
             "girl of about twelve who says nothing, and four more waiting "
             "at the rope barrier below",
     "mov": "As the line begins both hands pull hard on the thin iron "
            "handrail and the leading knee drives up onto the next tread. "
            "Halfway through the line the hips stay wedged between the rail "
            "and the brick, the leading foot comes back down a tread and the "
            "water bottle tips over on the step below. As the line ends the "
            "man in the fleece vest two steps down keeps his hand on the "
            "rail and looks straight up, and the woman in the windbreaker "
            "behind him turns her head sideways to see past him",
     "cam": "The shot is taken from four treads below at chest height, angled "
            "about thirty degrees upward around the curve of the stair so the "
            "narrowing shaft, the body wedged between the rail and the wall "
            "and the heads of the group underneath sit in one frame",
     "luz": "One shaft of hard daylight from the arched window crossing the "
            "whitewash, deep shade above it and below it.",
     "audio": "shoe soles scuffing on iron treads, a handrail ringing under a "
              "grip, wind moaning down the shaft and a stairwell with no "
              "voices in it"},

    # ⛔ LAPIDE 2026-08-21 — `mesa_restaurante` CORTADO: terceiro salao identico
    #    do lote (com `banco_restaurante` e `festa_rua`) e o mais vazio dos tres — mesmo
    #    com o conserto do achado 33 continua sendo "um casal esperando mesa".
    #    O `banco_restaurante` fica: o banco que solta e' imagem propria.


    # ⛔ LAPIDE 2026-08-21 — `bote_passeio` CORTADO: quarta tira que nao fecha do
    #    lote (com `cinto_aviao`, `manguito_pressao` e o que ja' saiu) e o cenario de
    #    menor aposta dos quatro — ninguem e' obrigado a fazer passeio de barco.


    {"id": "bicicleta_academia", "curto": "a bicicleta da academia nao serve",
     "v": "grafo-E", "cluster": "E",
     "sexos": ("mulher", "homem"),
     "formas": ("riso", "juizo"),
     "interior": True,
     "cen": "the cardio floor of an ordinary American gym, a long row of "
            "black upright exercise bikes with red flywheel guards and thin "
            "padded saddles, rubber-tile flooring in dark speckled grey, "
            "mirrored wall panels down one side, a rack of coloured dumbbells "
            "behind, black exposed ceiling ductwork and tall windows with "
            "flat daylight",
     "acao": "the near foot has just driven down on the caged pedal to swing "
             "the hips up onto the saddle, and the raised knee has come up "
             "hard under the handlebar stem and stopped dead against it, the "
             "thin saddle behind it still empty and the toe strap swinging",
     "test": "a trainer in a grey staff shirt stands beside the bike with one "
             "hand on the saddle rail and the other open, talking across the "
             "bike, and the members waiting for the machines have stopped: "
             "two men with towels round their necks laughing, a woman on the "
             "next bike who stops pedalling to stare, and one more watching "
             "in the mirror",
     "mov": "As the line begins both hands lock on the handlebars and the "
            "near foot drives down on the caged pedal to bring the hips up "
            "over the saddle. Halfway through the line the raised knee jams "
            "under the handlebar stem, the pedal spins away underfoot and "
            "the standing leg takes the weight again. As the line ends the "
            "two men with towels round their necks at the machines laugh out "
            "loud and the woman on the next bike stops pedalling to stare",
     "cam": "The shot is taken from the cardio floor beside the bike at "
            "seated chest height, angled slightly down, wide enough to hold "
            "the loose toe strap, the empty saddle, the trainer and the "
            "members waiting behind",
     "luz": "Flat cool daylight from the tall windows mixed with overhead "
            "strip light, low contrast, hard reflections on the mirrored "
            "panels.",
     "audio": "a flywheel spinning down, a dumbbell set on a rack, "
              "treadmill belts running and two men laughing nearby"},

    {"id": "elevador_lobby", "curto": "as portas do elevador que nao fecham",
     "v": "grafo-E", "cluster": "E",
     "sexos": ("mulher", "homem"),
     "formas": ("silencio", "juizo"),
     "interior": True,
     "cen": "the ground-floor lift lobby of an older office building, two "
            "brushed steel lift doors in a marble surround, a polished beige "
            "stone floor with dark inlay bands, a wood-panelled wall with a "
            "long padded bench, a brass call panel between the doors, a glass "
            "entrance wall with the street beyond and a small potted fig in "
            "the corner",
     "acao": "the last step has just carried the body in against the back "
             "wall of a car already holding seven office workers, and the "
             "two steel doors have driven halfway shut across the opening "
             "and bounced wide open again off the black rubber safety edge",
     "test": "the office workers waiting in the lobby have all stopped and "
             "none of them steps toward the car: a man with a coffee tray "
             "staring at the seven already inside, two women in office coats "
             "who look and say nothing to each other, and one more who steps "
             "back against the bench, while a building attendant in a grey "
             "blazer stays well back at the doorway with both hands down",
     "mov": "As the line begins both hands press flat to the back wall and "
            "the shoulders turn sideways to pull clear of the door line. "
            "Halfway through the line the steel doors come across, strike "
            "the shoulder and bounce wide open off the rubber edge again, "
            "and the seven in the car turn their faces to the wall. As the "
            "line ends the man with the coffee tray in the lobby stares at "
            "the crowded car and the two women in office coats by the bench "
            "look at each other and say nothing",
     "cam": "The shot is taken from the middle of the lobby at chest height, "
            "level and straight on, wide enough to hold the open lift doors, "
            "the crowded car, the body against its back wall and the waiting "
            "office workers",
     "luz": "Soft warm downlights on marble mixed with cool daylight from the "
            "glass entrance wall, gentle reflections on the polished floor.",
     "audio": "steel lift doors driving shut and bouncing open off a rubber "
              "edge over and over, shoes on stone and a lobby with no voices"},

    # ⛔ LAPIDE 2026-08-21 — `teleferico_colete` CORTADO: colapso quase verbatim
    #    com `trava_brinquedo` (trava que nao fecha + operador negando de braco estendido
    #    + fila nos corrimaos rindo, e os dois `mov` abrindo igual), e esquiar esta' fora
    #    do avatar do nicho enquanto o parque de diversoes e' universal.

]


# ===========================================================================
# ⭐ A PESSOA — nome + sexo + idade
# ===========================================================================
# ⭐ E' o eixo mais barato que existe, e a fonte prova: ela troca SO' O NOME e
# republica o mesmo roteiro. Betsy (v46) e Betty (v50) caem na MESMA cadeira de
# salao; Marjorie (v09/v15) e Marilyn (v51) caem na MESMA rampa. Isso nao e'
# descuido deles — e' o eixo que custa uma palavra e muda o video inteiro para
# quem assiste.
#
# ⛔⛔ OS CAMPOS GRAMATICAIS EXISTEM PARA UM POOL DE COPY SO'. `suj`, `obj`,
# `ref`, `poss` e `poss_nome` permitem que as MESMAS entradas de abertura, de
# testemunha e de CTA sirvam mulher, homem e casal sem duplicar o pool. ⚠️ E
# TODA a copy deste motor esta' no PASSADO ou em modal, de proposito: assim
# nenhuma frase precisa concordar em numero, e o defeito `they looks` deixa de
# ser possivel em vez de ser proibido.
#   ref        quem o video APRESENTA  ...... "Marjorie" · "her" · "them"
#   suj        sujeito da frase ............. "Marjorie" · "she"  · "they"
#   obj        objeto / alvo do remedio ..... "Marjorie" · "her"  · "them"
#   poss       possessivo ................... "her" · "his" · "their"
#   poss_nome  possessivo com nome .......... "Marjorie's" · "her" · "their"
#
# ⛔ NO CASAL O NOME E' DA MULHER E `obj` E' `them` — e' exatamente o que a
# fonte faz: *"This was Marjorie before [...] after I gave THEM one simple
# remedy"*. O marido nunca e' nomeado em nenhum dos quinze reels.
#
# ⏳ DIVIDA DECLARADA: o pool MASCULINO tem duas entradas e as duas sao
# ANONIMAS, porque a fonte nunca nomeia um homem — os dois unicos reels
# masculinos (v40 e v45) dizem `him`. Pool cresce de VIDEO LIDO, com o `v`
# carimbado; nome masculino entra no dia em que um reel disser um. Inventar
# quatro nomes aqui daria numero de pool e nao daria repertorio (§15).
#
# ⛔⛔ A ARQUITETURA DO CORPO — SEIS ELEMENTOS, E ELA NASCEU DE UM LOTE
# REPROVADO COM O VIDEO NA MAO (2026-08-21). O operador gerou, olhou e disse:
# *"nao esta' gerando personagens obesos, inclusive alguns parecem ate'
# magros"*. Estava certo, e a causa era minha.
#
# ⛔ O QUE O MOTOR ESCREVIA ERAM CATORZE PALAVRAS, TODAS ADJETIVO:
#     *"a very heavy 39-year-old white American woman [...] and with her a very
#       heavy husband in a black t-shirt. They are both wide through the
#       middle."*
# O gerador nao desenha ADJETIVO. Ele desenha FORMA, AREA DE QUADRO e
# COMPARACAO — e sem as tres ele volta para a media do treino, que e' uma
# pessoa comum. Foi exatamente o que voltou: um homem forte de porte comum e
# uma mulher plus size comum.
#
# ⚠️⚠️ E A CAUSA IMEDIATA FOI UM CONSERTO MEU, no mesmo dia, de manha: a
# varredura adversarial achou `very heavy` repetido de duas a quatro vezes por
# bloco (RU14), ENXUGOU os catorze `porte` para matar a repeticao, mediu
# *"1200 -> 0"* e deu por consertado. Matou a repeticao e matou a obesidade
# junto. E' a §41 das licoes de construcao na forma mais cara: **verificar a
# FORMA e destruir a FUNCAO**. ⛔ O conserto novo nao pode ressuscitar a
# repeticao — UMA descricao longa e continua NAO e' quatro reintroducoes com
# sintagma definido novo, e a `RU14` foi reescrita para saber a diferenca.
#
# ⭐⭐ OS SEIS ELEMENTOS, e cada um mora num campo:
#   1. `porte` ...... ANCORA DE ESCALA COM NUMERO E REFERENTE. Peso em libras
#                     por extenso + uma coisa do mundo que pesa aquilo.
#   2. `barriga` .... A BARRIGA COMO OBJETO GEOMETRICO COM POSICAO NO QUADRO.
#                     ⭐ E' o elemento que mais faltava, e o unico que obriga o
#                     gerador a alocar AREA DE PIXEL ao corpo: forma (uma bola
#                     macia so'), onde comeca e onde termina, quanto do quadro
#                     ela ocupa e contra o que ela e' comparada.
#   3. `sobre` ...... (no eixo `ROUPAS`) A PECA ESTICADA SOBRE ELA, COBRINDO
#                     TUDO. E' forma E guarda de moderacao no mesmo sintagma.
#   4. `membros` .... OS MEMBROS POR COMPARACAO — braco mais grosso que coxa.
#   5. `pescoco` / `nuca` .. O PESCOCO E O ROSTO, em duas variantes.
#   6. (na montagem) A CONSEQUENCIA NO QUE SUSTENTA O PESO.
#
# ⛔⛔ AS QUATRO TRAVAS, cada uma com o motivo medido:
#   T1. OS DESCRITORES DE OBESIDADE SAO DO TAKE 1 E SO' DELE. O take 2 e o
#       take 3 continuam magros — o motor existe para mostrar a MESMA pessoa
#       obesa e depois magra, e uma so' palavra de peso no reencontro mata o
#       angulo inteiro.
#   T2. QUEIXO, PAPADA, BOCHECHA e MAXILAR entram no CORPO do take 1 (campo
#       `pescoco`) e NUNCA na ancora de rosto (`ROSTOS`). A doutrina do bloco
#       `ROSTOS` proibe traco que o peso move na ANCORA, porque obriga o
#       gerador a escolher entre a ancora e a magreza do take 2, e ele escolhe
#       contra nos. A ancora fica INTOCADA.
#   T3. COM `rosto_ato1 = oculto` a camera esta' atras: queixo, papada e
#       bochecha SAEM da frase (contradicao direta) e entra a `nuca` — as
#       dobras do pescoco e as costas, que se veem de costas.
#   T4. NO CASAL o segundo corpo vem em FORMA COMPRIMIDA (`segundo`), nunca
#       cento e quarenta palavras vezes dois: e' ORCAMENTO. O teto de bloco da
#       AdBatch e' 3.900 caracteres.
#
# ⛔ E O PESO TEM DE SER CRIVEL PARA EMAGRECER: a rota e' de EMAGRECIMENTO e a
# mesma pessoa aparece magra oito segundos depois. A faixa e' 350-550 lb, e o
# autoteste a cobra entrada por entrada. Oitocentos e oitenta libras seria uma
# pessoa que o take 2 nao consegue desmentir.
#
# ⛔⛔ O CONTRATO DOS CAMPOS DE CORPO, e as clausulas nasceram de defeito
# MEDIDO no bloco montado (2026-08-21), nao de gosto:
#   1. ⛔ NAO REPETEM O PESO com sintagma de pessoa novo. A primeira sintagma
#      do IMAGE 01 ja' diz *"a very heavy 46-year-old woman"*; qualquer outro
#      *"the very heavy customer"* e' licenca para desenhar mais um corpo.
#      Medido antes: 100% dos blocos com DUAS ou mais ocorrencias, 32% com
#      QUATRO. Lente `RU14`.
#   2. ⛔ NAO CITAM ROSTO fora do campo `pescoco` — nem `face`, nem `mouth`,
#      nem `eyes`, nem `cheeks`, nem `jaw`. Com `rosto_oculto` a camera esta'
#      ATRAS da pessoa e a frase seguinte dizia *"flushed deep red across the
#      face"*: 108 dos 593 ocultos, 9% de TODOS os videos. Lente `RU4`.
#   3. ⛔ NAO NOMEIAM PECA DE ROUPA. A peca e' do eixo `ROUPAS` e de mais
#      ninguem: `the dress` sobre quem veste camiseta, `the shirt` sobre quem
#      veste vestido. Medido em 400 sorteios: 27 videos com `the dress`
#      fantasma e 63 com `the shirt`. Lente `RU3`.
# ⚠️ As tres sao cobradas TAMBEM no contrato de pool do autoteste, entrada por
# entrada, porque um pool novo entra sem passar por sorteio nenhum.
PESSOAS = [
    # -- MULHER SOZINHA ---------------------------------------------------
    {"id": "janet", "curto": "Janet · 50 · sozinha", "v": "v24",
     "nome": "Janet", "sexo": "mulher", "idade": 50,
     "ref": "Janet", "suj": "Janet", "obj": "Janet", "poss": "her",
     "poss_nome": "Janet's", "vida": "life",
     "porte": "She weighs four hundred and twenty pounds, as heavy as three "
              "ordinary grown women standing together.",
     "barriga": "One single enormous soft round ball of a belly starts high "
                "under her chest and hangs all the way down past her knees, "
                "the largest thing in the picture: it fills the whole lower "
                "half of the frame from the left edge to the right edge, far "
                "wider than her own shoulders.",
     "membros": "Her upper arms are thicker than her thighs, loose flesh "
                "folding over the elbows, her forearms round and swollen and "
                "her fingers thick.",
     "pescoco": "Her neck is buried in deep rolls of soft flesh, a triple "
                "chin spilling onto her chest, heavy jowls and round puffed "
                "cheeks.",
     "nuca": "The back of her neck is buried in three deep rolls of soft "
             "flesh over her collar, her shoulders and upper back one "
             "rounded mass."},
    {"id": "helen", "curto": "Helen · 57 · sozinha", "v": "v39",
     "nome": "Helen", "sexo": "mulher", "idade": 57,
     "ref": "Helen", "suj": "Helen", "obj": "Helen", "poss": "her",
     "poss_nome": "Helen's", "vida": "life",
     "porte": "She weighs three hundred and ninety pounds, as heavy as an "
              "upright piano.",
     "barriga": "Her belly is one huge soft round ball that begins at her "
                "chest and drops all the way to her thighs, the biggest "
                "single shape in the picture: it takes up the entire bottom "
                "half of the frame edge to edge and reaches well past the "
                "line of her hips on both sides.",
     "membros": "Her upper arms are thicker than her thighs, soft flesh "
                "gathering at the elbows, her forearms swollen tight and her "
                "fingers short and puffed.",
     "pescoco": "Her neck has all but disappeared into folds of soft flesh, a "
                "double chin flat on her chest, hanging jowls and cheeks "
                "pushed out round.",
     "nuca": "The back of her neck is lost in folds of soft flesh above her "
             "collar, her shoulders and back one smooth rounded mass."},
    {"id": "betsy", "curto": "Betsy · 48 · sozinha", "v": "v46",
     "nome": "Betsy", "sexo": "mulher", "idade": 48,
     "ref": "Betsy", "suj": "Betsy", "obj": "Betsy", "poss": "her",
     "poss_nome": "Betsy's", "vida": "life",
     "porte": "She weighs four hundred and thirty pounds, as heavy as a "
              "full-size chest freezer.",
     "barriga": "One gigantic soft round ball of a belly runs from just under "
                "her chest down past her knees and rests low, the largest "
                "thing in the picture: it covers the whole lower half of the "
                "frame from one edge to the other, a good deal wider than "
                "her shoulders.",
     "membros": "Her upper arms are thicker than her own thighs, the flesh "
                "folding over the elbows, her forearms tight and her hands "
                "puffed at the knuckles.",
     "pescoco": "Her neck is sunk into deep rolls of soft flesh, a triple "
                "chin spread onto her chest, low jowls and round full "
                "cheeks.",
     "nuca": "The back of her neck is sunk into deep rolls of soft flesh over "
             "her collar, her shoulders and back one wide rounded mass."},
    {"id": "margaret", "curto": "Margaret · 41 · sozinha", "v": "v47",
     "nome": "Margaret", "sexo": "mulher", "idade": 41,
     "ref": "Margaret", "suj": "Margaret", "obj": "Margaret", "poss": "her",
     "poss_nome": "Margaret's", "vida": "life",
     "porte": "She weighs four hundred and sixty pounds, as heavy as a stacked "
              "washer and dryer together.",
     "barriga": "Her belly is one vast soft round ball starting at her chest "
                "and hanging down to mid-shin, plainly the largest object in "
                "the picture: it fills the bottom half of the frame from "
                "edge to edge and is nearly twice the width of her "
                "shoulders.",
     "membros": "Her upper arms are far thicker than her thighs, the flesh "
                "folding over the elbows, her forearms swelling out round "
                "and her hands thick and soft.",
     "pescoco": "Her neck is buried under heavy rolls of soft flesh, a deep "
                "triple chin lying on her chest, sagging jowls and full "
                "round cheeks.",
     "nuca": "The back of her neck is buried under heavy rolls of soft flesh "
             "over her collar, her shoulders and upper back one unbroken "
             "rounded mass."},
    {"id": "betty", "curto": "Betty · 45 · sozinha", "v": "v50",
     "nome": "Betty", "sexo": "mulher", "idade": 45,
     "ref": "Betty", "suj": "Betty", "obj": "Betty", "poss": "her",
     "poss_nome": "Betty's", "vida": "life",
     "porte": "She weighs three hundred and seventy-five pounds, as heavy as a "
              "cast-iron claw-foot bathtub.",
     "barriga": "One enormous soft round ball of a belly hangs from her chest "
                "down over her thighs, the biggest single thing in the "
                "frame: it takes the whole lower half of the picture from "
                "the left edge to the right edge and carries well past her "
                "hips on either side.",
     "membros": "Her upper arms are thicker than her thighs, the flesh "
                "folding at the elbows, her forearms round and heavy and her "
                "fingers broad and soft.",
     "pescoco": "Her neck is packed into rolls of soft flesh, a double chin "
                "resting on her chest, heavy jowls at the sides and round "
                "puffed cheeks.",
     "nuca": "The back of her neck is packed into rolls of soft flesh above "
             "her collar, her shoulders and back one broad rounded mass."},
    {"id": "linda", "curto": "Linda · 53 · sozinha", "v": "v59",
     "nome": "Linda", "sexo": "mulher", "idade": 53,
     "ref": "Linda", "suj": "Linda", "obj": "Linda", "poss": "her",
     "poss_nome": "Linda's", "vida": "life",
     "porte": "She weighs five hundred and five pounds, as heavy as a full "
              "vending machine.",
     "barriga": "Her belly is one immense soft round ball that starts at her "
                "chest and hangs all the way down past her knees to rest on "
                "what is below her, the largest thing by far in the picture: "
                "it fills the bottom half of the frame corner to corner, "
                "more than twice as wide as her shoulders.",
     "membros": "Her upper arms are much thicker than her thighs, loose flesh "
                "folding over the elbows, her forearms round and swollen and "
                "her hands puffed.",
     "pescoco": "Her neck is gone into deep folds of soft flesh, a triple "
                "chin spilling wide onto her chest, heavy jowls and full "
                "round cheeks.",
     "nuca": "The back of her neck is gone into deep folds of soft flesh over "
             "her collar, her shoulders and back one continuous rounded "
             "mass."},
    {"id": "marjorie_sala", "curto": "Marjorie · 38 · sozinha", "v": "v27",
     "nome": "Marjorie", "sexo": "mulher", "idade": 38,
     "ref": "Marjorie", "suj": "Marjorie", "obj": "Marjorie", "poss": "her",
     "poss_nome": "Marjorie's", "vida": "life",
     "porte": "She weighs four hundred and forty-five pounds, as heavy as a "
              "full-grown black bear.",
     "barriga": "One huge soft round ball of a belly comes down from her "
                "chest and hangs past her knees, dwarfing everything else in "
                "the picture: it occupies the entire lower half of the frame "
                "from edge to edge and spreads far wider than her shoulders.",
     "membros": "Her upper arms are thicker than her thighs, soft flesh "
                "folding over the elbows, her forearms round and tight and "
                "her fingers short and swollen.",
     "pescoco": "Her neck sits in thick rolls of soft flesh, a triple chin "
                "down on her chest, loose jowls and cheeks round and pushed "
                "out.",
     "nuca": "The back of her neck sits in thick rolls of soft flesh over her "
             "collar, her shoulders and upper back one rounded mass."},
    # ⭐ A VARIANTE ANONIMA E' DA FONTE, nao economia minha: o v28 diz `This
    # was her before` do primeiro ao ultimo segundo e nunca da' um nome. Ela
    # existe no pool porque muda o registro do video — sem nome, o espectador
    # se enfia no lugar dela mais rapido.
    {"id": "anon_mulher", "curto": "sem nome · 40 · sozinha", "v": "v28",
     "nome": None, "sexo": "mulher", "idade": 40,
     "ref": "her", "suj": "she", "obj": "her", "poss": "her",
     "poss_nome": "her", "vida": "life",
     "porte": "She weighs three hundred and fifty-five pounds, as heavy as two "
              "large men put together.",
     "barriga": "Her belly is one big soft round ball that runs from her "
                "chest down onto her thighs, the largest shape in the "
                "picture: it fills the lower half of the frame from side to "
                "side and stands out wider than her shoulders by a hand's "
                "width on each side.",
     "membros": "Her upper arms are as thick as her thighs and fold at the "
                "elbows, her forearms round and full and her hands puffed "
                "with thick fingers.",
     "pescoco": "Her neck is thick with rolls of soft flesh, a double chin "
                "lying on her chest, soft jowls and round cheeks.",
     "nuca": "The back of her neck is thick with rolls of soft flesh above "
             "her collar, her shoulders and back one rounded mass."},
    # -- HOMEM (⏳ os dois anonimos — ver a divida declarada acima) --------
    {"id": "anon_homem_v40", "curto": "sem nome · 35 · sozinho", "v": "v40",
     "nome": None, "sexo": "homem", "idade": 35,
     "ref": "him", "suj": "he", "obj": "him", "poss": "his",
     "poss_nome": "his", "vida": "life",
     "porte": "He weighs five hundred and forty pounds, as heavy as a loaded "
              "pallet of cement bags.",
     "barriga": "One gigantic soft round ball of a belly hangs from his chest "
                "all the way down past his knees, far and away the largest "
                "thing in the picture: it fills the whole bottom half of the "
                "frame from the left edge to the right edge, well over twice "
                "the width of his shoulders.",
     "membros": "His upper arms are thicker than his thighs, loose flesh "
                "folding over the elbows, his forearms round and swollen and "
                "his hands broad and puffed.",
     "pescoco": "His neck is buried in deep rolls of soft flesh, a triple "
                "chin spilling onto his chest, sagging jowls and round full "
                "cheeks.",
     "nuca": "The back of his neck is buried in deep rolls of soft flesh over "
             "his collar, his shoulders and upper back one continuous "
             "rounded mass."},
    {"id": "anon_homem_v45", "curto": "sem nome · 37 · sozinho", "v": "v45",
     "nome": None, "sexo": "homem", "idade": 37,
     "ref": "him", "suj": "he", "obj": "him", "poss": "his",
     "poss_nome": "his", "vida": "life",
     "porte": "He weighs four hundred and seventy pounds, as heavy as a "
              "commercial deep freezer standing full.",
     "barriga": "His belly is one vast soft round ball starting high at his "
                "chest and hanging low past his knees, the biggest single "
                "object in the picture: it takes the entire lower half of "
                "the frame from edge to edge and carries a foot past his "
                "shoulders on either side.",
     "membros": "His upper arms are thicker than his thighs, soft flesh "
                "folding at the elbows, his forearms round and heavy and his "
                "fingers thick and swollen.",
     "pescoco": "His neck is lost in rolls of soft flesh, a double chin down "
                "on his chest, heavy jowls and cheeks pushed out round.",
     "nuca": "The back of his neck is lost in rolls of soft flesh above his "
             "collar, his shoulders and back one broad rounded mass."},
    # -- CASAL (o nome e' o DELA; o marido nunca e' nomeado na fonte) -----
    # ⛔ O `segundo` e' o corpo do marido em FORMA COMPRIMIDA — uma sentenca
    # que aponta para a arquitetura ja' descrita (`built exactly the same
    # way`) em vez de repeti-la. Cento e quarenta palavras vezes dois estoura
    # o teto de 3.900 caracteres da AdBatch, e bloco cortado em silencio e' o
    # pior modo de falha que existe.
    {"id": "marjorie", "curto": "Marjorie · 44 · casal", "v": "v09/v15",
     "nome": "Marjorie", "sexo": "casal", "idade": 44,
     "ref": "Marjorie", "suj": "Marjorie and her husband", "obj": "them",
     "poss": "their", "poss_nome": "Marjorie's", "vida": "lives",
     "porte": "She weighs four hundred and ten pounds, as heavy as three "
              "ordinary grown women together.",
     "barriga": "One enormous soft round ball of a belly hangs from her chest "
                "down past her knees, the largest thing in the picture: it "
                "fills the lower half of the frame from the left edge to the "
                "right edge and reaches far wider than her shoulders.",
     "membros": "Her upper arms are thicker than her thighs, loose flesh "
                "folding over the elbows, her forearms round and swollen and "
                "her hands soft and puffed.",
     "pescoco": "Her neck is buried in rolls of soft flesh, a triple chin "
                "onto her chest, heavy jowls and round full cheeks.",
     "nuca": "The back of her neck is buried in rolls of soft flesh over her "
             "collar, her shoulders and back one rounded mass.",
     "segundo": "The husband is built exactly the same way, the same round "
                "ball of a belly hanging from his chest onto his own thighs "
                "and the same thickness through the arms."},
    {"id": "marilyn", "curto": "Marilyn · 46 · casal", "v": "v51",
     "nome": "Marilyn", "sexo": "casal", "idade": 46,
     "ref": "Marilyn", "suj": "Marilyn and her husband", "obj": "them",
     "poss": "their", "poss_nome": "Marilyn's", "vida": "lives",
     "porte": "She weighs three hundred and eighty-five pounds, as heavy as a "
              "cast-iron wood stove.",
     "barriga": "Her belly is one huge soft round ball running from her chest "
                "down over her thighs, and nothing in the picture is bigger: "
                "it covers the bottom half of the frame edge to edge and "
                "stands out wider than her shoulders on both sides.",
     "membros": "Her upper arms are as thick as her thighs and fold heavily "
                "at the elbows, her forearms round and tight and her hands "
                "wide and puffed.",
     "pescoco": "Her neck sits in deep rolls of soft flesh, a double chin "
                "resting on her chest, sagging jowls and round cheeks.",
     "nuca": "The back of her neck sits in deep rolls of soft flesh above her "
             "collar, her shoulders and upper back one rounded mass.",
     "segundo": "The husband is built exactly the same way, with the same ball "
                "of a belly resting down on his thighs and the same swollen "
                "arms."},
    {"id": "mary", "curto": "Mary · 52 · casal", "v": "v49",
     "nome": "Mary", "sexo": "casal", "idade": 52,
     "ref": "Mary", "suj": "Mary and her husband", "obj": "them",
     "poss": "their", "poss_nome": "Mary's", "vida": "lives",
     "porte": "She weighs four hundred and thirty-five pounds, as heavy as a "
              "motorcycle with a rider on it.",
     "barriga": "One immense soft round ball of a belly starts at her chest "
                "and hangs all the way down past her knees, the biggest "
                "single shape in the picture: it fills the whole lower half "
                "of the frame from one edge to the other, nearly twice as "
                "wide as her shoulders.",
     "membros": "Her upper arms are thicker than her thighs, the flesh "
                "folding over the elbows, her forearms round and swollen and "
                "her fingers short and thick.",
     "pescoco": "Her neck is packed into deep rolls of soft flesh, a triple "
                "chin spread on her chest, heavy jowls and full round "
                "cheeks.",
     "nuca": "The back of her neck is packed into deep rolls of soft flesh "
             "over her collar, her shoulders and back one broad rounded "
             "mass.",
     "segundo": "The husband is built exactly the same way, the same round "
                "ball of a belly hanging past his knees and the same soft "
                "thickness through the arms."},
    {"id": "anon_casal", "curto": "sem nome · 39 · casal", "v": "v38",
     "nome": None, "sexo": "casal", "idade": 39,
     "ref": "them", "suj": "they", "obj": "them", "poss": "their",
     "poss_nome": "their", "vida": "lives",
     "porte": "She weighs four hundred and ninety pounds, as heavy as a full "
              "commercial ice machine.",
     "barriga": "Her belly is one vast soft round ball that begins under her "
                "chest and hangs down past her knees, by far the largest "
                "thing in the picture: it fills the entire lower half of the "
                "frame from the left edge to the right edge, well beyond the "
                "width of her shoulders.",
     "membros": "Her upper arms are much thicker than her thighs, loose flesh "
                "folding over the elbows, her forearms round and heavy and "
                "her fingers thick.",
     "pescoco": "Her neck is buried in heavy rolls of soft flesh, a triple "
                "chin down onto her chest, sagging jowls and round cheeks.",
     "nuca": "The back of her neck is buried in heavy rolls of soft flesh "
             "over her collar, her shoulders and upper back one rounded "
             "mass.",
     "segundo": "The husband is built exactly the same way, the same ball of a "
                "belly hanging from his chest onto his thighs and the same "
                "swollen forearms."},
]

# ⚠️ `corpo` e' DERIVADO e nao escrito entrada por entrada: e' pura
# gramatica (`bodies` no casal, `body` no resto) e nao ha' decisao editorial
# nenhuma a tomar em catorze linhas iguais.
# ⚠️ `obj_pron` e' o objeto SEMPRE em pronome, ao lado do `obj` que pode ser
# o nome. Existe porque duas frases precisam do pronome mesmo quando ha' nome:
# a do remedio (a virada ao lado ja' nomeou) e a das roupas folgadas (o
# possessivo ja' esta' em pronome).
# ⚠️ `e_sao` e' a COPULA em numero, e ela existe por defeito MEDIDO: a `vi3`
# dizia `And here is %(obj)s now,` e devolvia *"And here is THEM now"* e
# *"And here is HIM now"* — ingles quebrado em 34 de 400 videos (8,5%). O
# guarda `_RX_ANTES_REF` do autoteste nao pegava porque ele so' varre `%(ref)s`
# em posicao de sujeito, e `here is` + `%(obj)s` cai fora dele. Com a copula em
# slot a mesma entrada serve *"And here Janet is now"*, *"And here he is now"*
# e *"And here they are now"*.
for _p_ in PESSOAS:
    _p_["corpo"] = "bodies" if _p_["sexo"] == "casal" else "body"
    _p_["obj_pron"] = {"mulher": "her", "homem": "him",
                       "casal": "them"}[_p_["sexo"]]
    _p_["e_sao"] = "are" if _p_["sexo"] == "casal" else "is"

SEXOS = ("mulher", "homem", "casal")


# ===========================================================================
# O MARIDO — so' existe quando o desastre e' de casal
# ===========================================================================
# ⛔ Quatro entradas porque foram quatro os reels de casal lidos, e cada uma
# carrega o ANTES e o DEPOIS juntos: o take 2 mostra os dois magros, e um
# marido que troca de camisa entre os quadros e' a mesma quebra de continuidade
# que a peca ancora existe para impedir.
# ⚠️ Ele nao tem nome, nao tem fala e nao tem rosto proprio no BLOCO 0: a REF
# ancora o rosto DELA, que e' quem o video nomeia.
PARCEIROS = [
    {"id": "vermelha", "curto": "camisa vermelha", "v": "v09/v15",
     "antes": "a very heavy husband in a red t-shirt and black gym shorts "
              "with black sneakers",
     "depois": "the same husband, now slim, in the same red t-shirt hanging "
               "loose on him and white chino shorts"},
    {"id": "marinho", "curto": "camisa marinho", "v": "v51",
     "antes": "a very heavy husband in a navy blue t-shirt, black athletic "
              "shorts and black sneakers",
     "depois": "the same husband, now slim, in the same navy blue t-shirt "
                "hanging loose on him and khaki cargo shorts"},
    {"id": "grisalho", "curto": "grisalho de regata vermelha", "v": "v49",
     "antes": "a very heavy grey-haired husband in a red athletic t-shirt and "
              "black shorts with red side stripes",
     "depois": "the same grey-haired husband, now slim, in the same red "
               "athletic t-shirt hanging loose on him and khaki shorts"},
    {"id": "preta", "curto": "camisa preta", "v": "v38",
     "antes": "a very heavy husband in a black t-shirt and black athletic "
              "shorts with a white side stripe",
     "depois": "the same husband, now slim, in the same black t-shirt hanging "
               "loose on him and khaki chinos"},
]


# ===========================================================================
# ⭐⭐ O ROSTO — a ancora do BLOCO 0 (REF)
# ===========================================================================
# ⛔⛔ A ANCORA SO' CITA TRACO QUE O PESO NAO MOVE. Olhos (formato, distancia,
# implantacao), sobrancelha, ponte do nariz, orelha, sinal permanente e corte
# de cabelo atravessam trinta quilos; MAXILAR, BOCHECHA, PAPADA e QUEIXO nao.
# ⚠️ Uma ancora que cita bochecha cheia obriga o gerador a escolher entre a
# ancora e a magreza do take 2, e ele escolhe contra nos — e' exatamente o que
# se ve' na fonte: no v27 a loira de 35 do ato 1 volta grisalha de 55 no ato 2,
# e no v45 o homem branco de barba curta volta hispanico.
#
# ⛔ NENHUMA COR — nem de olho, nem de cabelo, nem de pele. A etnia vem da
# PAGINA e ja' entra na frase montada; duas vozes decidindo o mesmo sintagma o
# Veo resolve inventando (defeito FT14 do FIGHT 16). O que fica e' GEOMETRIA.
# ⭐ OCULOS EM 4 DAS 14 (29%), e eles entraram porque o
# `medir_personagens --gate` acusou o eixo ZERADO — eixo zerado num pool de
# gente e' o mesmo rosto repetido, e aqui o rosto e' a ancora inteira do
# angulo. ⚠️ Sao grounded: a Janet do v24 usa oculos de aro preto retangular
# nos dois atos, e a leitura otica registrou que eles PISCAM entre quadros —
# que e' justamente o defeito que a ancora repetida por extenso impede. E
# oculos sobrevivem a trinta quilos, que e' o criterio deste pool.
# ⛔ E NENHUMA PALAVRA DE APROVACAO nem de deterioracao: elogio puxa o rosto
# para a media do banco de imagem (mesmo mecanismo do `not a celebrity`), e
# avaria transforma a pessoa em caricatura antes de o video comecar.
# ⚠️ A FORMA E' CONTRATO: cada entrada e' uma lista de tracos separada por
# virgulas, sem verbo, porque tres frases diferentes a consomem (o REF, a
# IMAGE 01 e as IMAGE 02/03).
ROSTOS = [
    {"id": "amendoados_altos", "curto": "olhos amendoados + testa alta",
     "sexo": "mulher",
     "desc": "wide-set almond eyes under straight low brows, a high forehead, "
             "a narrow straight nose bridge, small close-set ears, a small "
             "mole below the outer corner of the left eye, black-framed "
             "rectangular glasses, and hair worn in a high loose bun with "
             "strands escaping at the temples"},
    {"id": "fundos_arco", "curto": "olhos fundos + sobrancelha em arco",
     "sexo": "mulher",
     "desc": "deep-set round eyes under a high arched brow, a short nose "
             "bridge with a slight dip, detached earlobes, a scatter of "
             "freckles straight across the nose bridge, and shoulder-length "
             "hair with a blunt fringe cut level with the brow"},
    {"id": "juntos_reta", "curto": "olhos proximos + sobrancelha reta",
     "sexo": "mulher",
     "desc": "close-set eyes with a slight downward tilt at the outer corner, "
             "a flat straight brow, a wide nose bridge, a pierced ear with a "
             "single small stud, a raised beauty spot high on the right cheek "
             "ridge, and hair pinned back off the face in a low twist"},
    {"id": "abertos_curto", "curto": "olhos abertos + cabelo curto",
     "sexo": "mulher",
     "desc": "large round wide-open eyes set far apart, thin brows that stop "
             "short of the outer corner, a short straight nose bridge, "
             "attached earlobes, a fine vertical scar line through the left "
             "brow, thin gold wire-rimmed glasses, and a short layered cut "
             "kept above the collar"},
    {"id": "encapuzados_ondas", "curto": "palpebra caida + ondas",
     "sexo": "mulher",
     "desc": "hooded eyelids over narrow eyes, a low flat brow line, a nose "
             "bridge with a visible bump at the top, large earlobes, three "
             "small freckles in a line under the right eye, and long waves "
             "parted deep on one side"},
    {"id": "rasgados_rabo", "curto": "olhos rasgados + rabo de cavalo",
     "sexo": "mulher",
     "desc": "long narrow eyes with a slight upward tilt, brows that sit close "
             "over them, a fine nose bridge that widens at the base, small "
             "flat ears, a permanent crease between the brows, and hair pulled "
             "back tight into a high ponytail"},
    {"id": "redondos_franja", "curto": "olhos redondos + franja lateral",
     "sexo": "mulher",
     "desc": "round eyes set at an even distance apart, thick brows with a "
             "gap in the tail of the left one, a straight even nose bridge, "
             "ears that sit low against the head, a small mole at the outer "
             "corner of the right eye, and a long side-swept fringe",
     },
    {"id": "assimetricos_coque", "curto": "olho esquerdo menor + coque baixo",
     "sexo": "mulher",
     "desc": "eyes of visibly different size, the left a little smaller, brows "
             "that sit at different heights, a narrow nose bridge, a pierced "
             "and slightly stretched left lobe, a freckle at the centre of the "
             "forehead, and hair gathered into a low bun at the nape"},
    {"id": "profundos_grisalho", "curto": "olhos profundos + mecha branca",
     "sexo": "mulher",
     "desc": "deep-set eyes under a heavy straight brow, a broad nose bridge, "
             "a small notch in the top of the right ear, a birthmark on the "
             "left temple, and a white streak running back from the hairline "
             "above one temple"},
    {"id": "h_juntos_barba", "curto": "olhos proximos + barba curta",
     "sexo": "homem",
     "desc": "close-set eyes under a heavy straight brow, a wide flat nose "
             "bridge, large detached earlobes, a mole on the left temple, "
             "short cropped hair and three days of stubble kept even"},
    {"id": "h_fundos_raspado", "curto": "olhos fundos + cabeca raspada",
     "sexo": "homem",
     "desc": "deep-set eyes set far apart, brows that meet in a low line, a "
             "nose bridge with a healed break at the top, ears that stand out "
             "from the head, a scar line above the right brow, thick "
             "black-framed glasses, and a shaved scalp"},
    {"id": "h_redondos_bigode", "curto": "olhos redondos + bigode",
     "sexo": "homem",
     "desc": "round eyes with a slight downward tilt, thin brows, a short "
             "straight nose bridge, attached earlobes, a beauty spot beside "
             "the left nostril, a full moustache and short hair parted low"},
    {"id": "h_encapuzados_ondas", "curto": "palpebra caida + cabelo ondulado",
     "sexo": "homem",
     "desc": "hooded eyelids over narrow eyes, one brow noticeably higher than "
             "the other, a narrow nose bridge, a pierced left ear with a small "
             "hoop, a permanent crease between the brows, and wavy hair pushed "
             "back off the forehead"},
    {"id": "h_amendoados_entradas", "curto": "olhos amendoados + entradas",
     "sexo": "homem",
     "desc": "almond eyes set close under a flat brow, a fine nose bridge, "
             "small close-set ears, a scatter of freckles across the nose "
             "bridge, rimless glasses, a high hairline with thick hair behind "
             "it and a close-trimmed chin beard"},
]


# ===========================================================================
# ⭐⭐ A PECA ANCORA — o achado do v46
# ===========================================================================
# ⛔⛔ E' A UNICA COISA NA FONTE QUE RESOLVE O PROBLEMA CENTRAL DESTE ANGULO.
# No v46 a MESMA blusa floral atravessa os dois atos: esticada sobre o corpo
# obeso no primeiro, **caindo solta** sobre o corpo magro no segundo. Ela e'
# ancora de continuidade E prova de emagrecimento no mesmo objeto — o
# espectador le' "e' a mesma pessoa" e "ela emagreceu" sem uma palavra.
# ⚠️ E onde a fonte NAO tem ancora de roupa ela troca de pessoa
# escancaradamente: v27, v28, v38 e v45. O v45 e' o caso limite — a roupa muda
# TRES vezes dentro do proprio ato 1 (camiseta cinza no arreio, regata preta na
# grama, polo azul na varanda) e o homem do reencontro nao passa pelo mesmo.
# ⛔ Por isso a peca vem SEM COR DE PELE e sem estampa que dependa de etnia, e
# a lente RU3 a cobra nos TRES quadros.
# ⚠️ `sexos` existe porque vestido e tunica nao servem ao pool masculino, e
# entrada que nao cabe com os minimos dos outros eixos esta' MORTA enquanto o
# autoteste a conta como viva (§35).
#
# ⭐⭐ O CAMPO `sobre` E' O ELEMENTO 3 DA ARQUITETURA DO CORPO (2026-08-21), e
# ele e' FORMA e GUARDA DE MODERACAO no mesmo sintagma. A peca esticada SOBRE a
# barriga e COBRINDO tudo e' o que da' ao gerador a superficie da bola — sem
# ela a barriga descrita fica sem casca e o corpo volta para a media do treino.
# ⛔⛔ E O VAO SAIU DO `antes`, EM TODAS AS DEZ. As formas antigas eram
# *"pulling open between the buttons"*, *"the zip pulling apart at the
# bottom"*, *"riding up at the waist"*, *"the hem rucked up"* e *"short at the
# waist"*: as cinco implicam ABERTURA e PELE EXPOSTA, que e' pedir recusa de
# moderacao numa cena que ja' e' de corpo em queda. ⭐ O que fica e' o tecido
# TENSIONADO — em cada botao, em cada costura, no ziper fechado — e a bainha
# PUXADA PARA BAIXO passando da cintura, com a barriga inteira dentro da peca.
# ⚠️ E o `sobre` nomeia a peca com modificador na frente (`The cream blouse`,
# nunca `the blouse`): o `_RX_PECA_FANTASMA` da RU3 recorta pelo artigo
# definido COLADO no substantivo, e a forma nua acusaria a propria ancora.
ROUPAS = [
    {"id": "blusa_floral", "curto": "blusa floral grande", "v": "v46/v50",
     "sexos": ("mulher", "casal"),
     "antes": "a cream blouse printed with large flowers, stretched tight "
              "across the front and back with the fabric standing tense at "
              "every button",
     "sobre": "The cream blouse is stretched taut over the whole of that "
              "belly and covers all of it, tense at every button, the hem "
              "pulled low past the waistband so the belly stays inside it.",
     "depois": "the same cream blouse printed with large flowers, now hanging "
               "loose and empty on the frame with the shoulders falling wide"},
    {"id": "regata_mostarda", "curto": "regata mostarda", "v": "v09/v15",
     "sexos": ("mulher", "casal"),
     "antes": "a mustard-yellow ribbed tank top stretched thin across the "
              "front and back with the ribbing pulled flat",
     "sobre": "The mustard-yellow ribbed tank top is stretched thin and taut "
              "over the whole of that belly and covers all of it, the hem "
              "drawn well past the waistband so the belly stays inside it.",
     "depois": "the same mustard-yellow ribbed tank top, now loose at the "
               "shoulders and hanging straight down from them"},
    {"id": "camiseta_cinza", "curto": "camiseta cinza mescla", "v": "v40",
     "sexos": ("mulher", "homem", "casal"),
     "antes": "a heather grey short-sleeve t-shirt pulled tight over the "
              "shoulders and the front with the seams standing out",
     "sobre": "The heather grey t-shirt is pulled taut over the whole of that "
              "belly and covers all of it, the cotton thin across the front, "
              "the hem hanging below the waistband so the belly stays inside "
              "it.",
     "depois": "the same heather grey short-sleeve t-shirt, now loose on the "
               "frame with the sleeves hanging well clear of the arms"},
    {"id": "zip_marinho", "curto": "blusao marinho de ziper", "v": "v59",
     "sexos": ("mulher", "homem", "casal"),
     "antes": "a navy blue zip-front top pulled closed across the middle with "
              "the zip fastened all the way to the top",
     "sobre": "The navy blue zip-front top is stretched taut over the whole "
              "of that belly and covers all of it, the zip closed its full "
              "length, the hem pulled past the waistband so the belly stays "
              "inside it.",
     "depois": "the same navy blue zip-front top, now hanging open and loose "
               "with the panels falling straight"},
    {"id": "camiseta_roxa", "curto": "camiseta roxa mescla", "v": "v47",
     "sexos": ("mulher", "homem", "casal"),
     "antes": "a purple heather short-sleeve t-shirt stretched tight across "
              "the front with the sleeves cutting into the upper arms",
     "sobre": "The purple heather t-shirt is stretched taut over the whole of "
              "that belly and covers all of it, the cotton thin across the "
              "front, the hem drawn low past the waistband so the belly stays "
              "inside it.",
     "depois": "the same purple heather short-sleeve t-shirt, now loose "
               "everywhere it touches and long past the waist"},
    {"id": "camiseta_vermelha", "curto": "camiseta vermelha", "v": "v24",
     "sexos": ("mulher", "homem", "casal"),
     "antes": "a bright red short-sleeve t-shirt pulled taut over the front "
              "with the seams standing out at the shoulders",
     "sobre": "The bright red t-shirt is pulled taut over the whole of that "
              "belly and covers all of it, the seams standing out along the "
              "front, the hem low past the waistband so the belly stays "
              "inside it.",
     "depois": "the same bright red short-sleeve t-shirt, now hanging loose "
               "from the shoulders with the seams sitting low on the arms"},
    {"id": "tunica_floral", "curto": "tunica floral clara", "v": "v39",
     "sexos": ("mulher",),
     "antes": "a pastel floral short-sleeve tunic stretched across the front "
              "and pulled tight under the arms",
     "sobre": "The pastel floral tunic is stretched taut over the whole of "
              "that belly and covers all of it, the fabric tense across the "
              "front, and it hangs well past the waistband so the belly stays "
              "inside it.",
     "depois": "the same pastel floral short-sleeve tunic, now hanging loose "
               "and straight with room to spare at the sides"},
    {"id": "vestido_lilas", "curto": "vestido lilas florido", "v": "v28",
     "sexos": ("mulher",),
     "antes": "a sleeveless lavender floral cotton dress stretched across the "
              "front and back with the armholes cutting in",
     "sobre": "The lavender floral cotton dress is stretched taut over the "
              "whole of that belly and covers all of it, tense from the "
              "shoulders down, and it falls past the waist so the belly stays "
              "inside it.",
     "depois": "the same sleeveless lavender floral cotton dress, now loose "
               "on the frame and hanging straight from the shoulders"},
    {"id": "camiseta_verde", "curto": "camiseta verde mescla", "v": "v09",
     "sexos": ("mulher", "homem", "casal"),
     "antes": "a heather green crew-neck t-shirt pulled tight across the "
              "chest and back with the collar strained",
     "sobre": "The heather green t-shirt is pulled taut over the whole of "
              "that belly and covers all of it, the knit thin across the "
              "front, the hem hanging past the waistband so the belly stays "
              "inside it.",
     "depois": "the same heather green crew-neck t-shirt, now loose at the "
               "collar and falling straight down the body"},
    {"id": "polo_marinho", "curto": "polo marinho", "v": "v45",
     "sexos": ("mulher", "homem", "casal"),
     "antes": "a navy blue polo shirt pulled tight down the front with the "
              "sleeves cutting into the upper arms",
     "sobre": "The navy blue polo shirt is pulled taut over the whole of that "
              "belly and covers all of it, the placket fastened and tense at "
              "each button, the hem low past the waistband so the belly stays "
              "inside it.",
     "depois": "the same navy blue polo shirt, now loose at the buttons with "
               "the sleeves hanging clear of the arms"},
]


# ===========================================================================
# O REENCONTRO — o lugar do ato 2 e do ato 3
# ===========================================================================
# ⛔ Os dois ultimos takes acontecem NO MESMO lugar e no MESMO enquadramento:
# na fonte isso e' um plano continuo em 12 dos 15 reels, e o que muda entre os
# dois beats e' so' a funcao da fala. Mudar de lugar no take 3 poria a Ruth em
# duas casas dentro de vinte segundos.
# ⚠️ Cinco sao varanda de suburbio com bandeira americana (o padrao da pagina),
# duas sao a BOTICA de ervas — e a leitura otica marcou a botica como *"o
# quadro mais rico e o mais congruente com a personagem Ruth, e o unico em que
# ela nao precisa se deslocar ate' a casa da cliente"*.
REENCONTROS = [
    {"id": "varanda_bandeira", "curto": "varanda com bandeira", "v": "v09/v15",
     "amb": "the front porch of a two-storey suburban American house on a "
            "summer afternoon, sage-green lap siding, cream painted columns "
            "and trim, a black wall lantern beside the door, a United States "
            "flag on an angled pole at the corner of the porch, painted grey "
            "deck boards underfoot, and behind them a tree-lined residential "
            "street with parked cars and mown lawns",
     "luz": "Warm late-afternoon sun raking in from one side, bright open "
            "shade on the porch against a sunlit lawn.",
     "audio": "quiet suburban room tone, birdsong, a light breeze and a "
              "distant car"},
    {"id": "varanda_coberta", "curto": "varanda coberta de colunas", "v": "v45",
     "amb": "the covered wooden porch of an American suburban house on a "
            "bright summer day, a white painted porch ceiling and beam, a "
            "squared natural wood post, a natural wood railing with square "
            "balusters, weathered deck boards, a clipped boxwood hedge just "
            "beyond the rail, and a residential street behind with parked cars "
            "and two United States flags on the neighbouring porches",
     "luz": "Bright summer daylight filtered through the porch roof and the "
            "maples, cooler and softer than the street beyond.",
     "audio": "birdsong, leaves moving in a light breeze and a car passing far "
              "off"},
    {"id": "deck_cinza", "curto": "deck de madeira cinza", "v": "v28/v40",
     "amb": "a weathered grey wooden deck at the front of a suburban Midwestern "
            "house on a bright summer day, a natural wood railing and a white "
            "porch post, a mown green lawn, a concrete driveway and sidewalk "
            "running behind, a row of single-storey ranch houses with pale "
            "siding across the street, tall leafy maples and clear blue sky",
     "luz": "High summer sun filtered through the maple canopy, warm dappled "
            "highlights on the deck boards, open blue-sky fill on both faces.",
     "audio": "outdoor summer room tone, cicadas, faint birdsong and a distant "
              "car"},
    {"id": "varanda_creme", "curto": "varanda creme com vasos", "v": "v46/v49",
     "amb": "the front porch of a clean suburban American house, cream vinyl "
            "siding, a painted wooden deck floor and rail, a white-framed "
            "window at one side, terracotta pots of pink and white flowers "
            "along the rail, a folding chair with a striped cushion, a wide "
            "mown lawn and two-storey neighbouring houses with parked cars "
            "across the street",
     "luz": "Warm late-afternoon sun raking across the porch from one side, "
            "soft shadows on the deck boards, blue sky behind.",
     "audio": "suburban outdoor room tone, birds, a car passing and light wind"},
    {"id": "varanda_maple", "curto": "varanda sob os bordos", "v": "v39/v59",
     "amb": "the wooden deck porch of an American suburban house on a bright "
            "summer day, weathered grey-brown deck boards, a natural wood "
            "railing with square balusters, a mowed green front lawn, a "
            "neighbouring white clapboard house with maroon shutters and a "
            "United States flag angled out from its porch, a paved sidewalk "
            "and tall leafy maples overhead",
     "luz": "Bright midday summer sun from the front, warm, with dappled leaf "
            "shadows falling across the deck boards.",
     "audio": "cicadas, birdsong and a light breeze moving through the trees"},
    {"id": "botica_pinho", "curto": "a botica de prateleiras de pinho",
     "v": "v27/v47",
     "amb": "an Amish home apothecary in warm honey-toned pine, open shelving "
            "floor to ceiling stacked with glass jars of dried herbs under "
            "handwritten paper labels, a rack of black cast-iron skillets hung "
            "on an iron rail, braided garlic and bundles of dried lavender "
            "hanging from the beam, framed botanical prints on the cream wall, "
            "stoneware crocks and woven splint baskets, and a wide plank pine "
            "floor with sun stripes across it",
     "luz": "Low winter sun raking in from a small window and laying bright "
            "stripes across the plank floor, warm bounce off the timber.",
     "audio": "quiet interior room tone and faint wind at the window"},
    {"id": "cozinha_botica", "curto": "a cozinha-botica da fazenda", "v": "v24",
     "amb": "a warm farmhouse apothecary kitchen in honey-toned pine, open "
            "shelves lined with glass storage jars of dried herbs, seeds and "
            "grains, black cast-iron skillets hanging from a wall rail, "
            "braided garlic beside them, framed botanical prints on the wall, "
            "wicker baskets and lidded crocks stacked under a thick "
            "butcher-block island, and a bright window looking onto green "
            "field",
     "luz": "Warm interior daylight pouring in from the window at one side, "
            "soft golden fill on the pine shelving and the glass jars.",
     "audio": "quiet indoor room tone with a clock somewhere out of frame"},
    {"id": "gramado_fazenda", "curto": "o gramado da fazenda branca", "v": "v50",
     "amb": "the mown front lawn of a white clapboard farmhouse, white porch "
            "columns with hanging baskets of pink and purple petunias, dark "
            "wooden rocking chairs on the porch deck behind, a black "
            "split-rail fence and an open green pasture beyond, and a large "
            "leafy shade tree at one edge of the frame",
     "luz": "Warm low golden-hour sunlight coming from behind the lens, soft, "
            "with no hard shadows on the faces.",
     "audio": "open country room tone, birdsong and wind moving over grass"},
]


# ⭐⭐ O CABELO SAI SEPARADO DO ROSTO, e isso e' exigencia do eixo
# `rosto_ato1`. Com o rosto OCULTO no take 1 a camera fica atras da pessoa: nao
# ha' olho, nao ha' sobrancelha, nao ha' ponte de nariz — a unica coisa da
# ancora que ainda existe em quadro e' o CABELO (mais a peca de roupa).
# ⛔ Repetir a `desc` inteira num quadro filmado de costas seria pedir ao
# gerador dois olhos que ele nao pode mostrar, e contradicao ele resolve
# mexendo no que estava certo: vira o rosto para a lente e o modo morre.
# ⚠️ Cada entrada aqui e' a MESMA clausula de cabelo que vive dentro da `desc`
# correspondente — escrita duas vezes de proposito, porque uma fatia por
# `split()` degradaria em silencio no dia em que alguem escrevesse uma `desc`
# com outra pontuacao (o fallback devolveria o rosto inteiro e ninguem veria).
# O autoteste cobra que as quatorze tenham cabelo declarado.
CABELOS = {
    "amendoados_altos": "hair worn in a high loose bun with strands escaping "
                        "at the temples",
    "fundos_arco": "shoulder-length hair with a blunt fringe cut level with "
                   "the brow",
    "juntos_reta": "hair pinned back off the face in a low twist",
    "abertos_curto": "a short layered cut kept above the collar",
    "encapuzados_ondas": "long waves parted deep on one side",
    "rasgados_rabo": "hair pulled back tight into a high ponytail",
    "redondos_franja": "a long side-swept fringe",
    "assimetricos_coque": "hair gathered into a low bun at the nape",
    "profundos_grisalho": "a white streak running back from the hairline above "
                          "one temple",
    "h_juntos_barba": "short cropped hair and three days of stubble kept even",
    "h_fundos_raspado": "a shaved scalp",
    "h_redondos_bigode": "a full moustache and short hair parted low",
    "h_encapuzados_ondas": "wavy hair pushed back off the forehead",
    "h_amendoados_entradas": "a high hairline with thick hair behind it and a "
                             "close-trimmed chin beard",
}
for _r_ in ROSTOS:
    _r_["cabelo"] = CABELOS[_r_["id"]]


# ###########################################################################
# A COPY
# ###########################################################################
# ⛔⛔ A COPY MORA TODA NESTA SECAO, INCLUSIVE O BEAT DO DESASTRE. Ele e'
# injetado nas entradas de `DESASTRES` logo abaixo em vez de ser escrito dentro
# delas, e isso e' escolha: cena e fala sao dois registros, e misturar os dois
# num dicionario so' foi como o BANHO 16 acabou com direcao de cena dentro de
# pool de fala. O autoteste cobra que os SESSENTA E DOIS tenham beat.
#
# ⚠️ TODA a copy esta' no PASSADO ou em modal. Nao e' estilo: e' o que permite
# o MESMO pool servir `she`, `he` e `they` sem uma unica variante de numero. O
# defeito `they looks` deixa de ser possivel em vez de ser proibido.

# ⭐ O ARCO, e ele e' o da fonte, medido:
#     TAKE 1  <abertura> <o desastre> <a testemunha> Pure shame.
#     TAKE 2  <a virada> <o remedio> <a prova>
#     TAKE 3  (<selo>) <o CTA>
# ⭐ `pure shame` fecha o ato 1 em 11 dos 15 reels. E' o unico literal travado
# da fala alem da keyword, e a lente RU11 o cobra.
FECHO_ATO1 = "Pure shame."


# ---------------------------------------------------------------------------
# O BEAT DO DESASTRE — um por entrada de DESASTRES
# ---------------------------------------------------------------------------
# ⚠️ TETO DE 15 PALAVRAS por beat, e o numero e' orcamento, nao gosto: a menor
# abertura tem 4, a menor testemunha tem 3 e o fecho tem 2, entao um beat de 16
# ja' mataria a combinacao mais curta que existe. O autoteste cobra o teto.
DESASTRES_FALA = {
    "guindaste_parede":
        "lifted out through the wall by a crane, until the strap gave way",
    "guindaste_sala":
        "hanging in a lifting sling in the middle of the living room",
    "cadeira_salao":
        "the chair at the nail salon cracked under %(poss)s weight",
    "rampa_medico":
        "the ramp to the doctor, and %(poss)s legs gave under the weight",
    "escada_varanda":
        "the porch steps broke apart under %(poss)s weight",
    "carro_cafe":
        "down on the driveway getting out of the car, hot coffee everywhere",
    "cctv_calcada":
        "face down on %(poss)s own driveway, unable to reach %(poss)s child",
    "reabilitacao":
        "learning to climb a staircase again, because of %(poss)s weight",
    "sofa_bombeiros":
        "unable to get off %(poss)s own couch without a fire crew",

    # -- CLUSTER A -----------------------------------------------------------
    "banco_igreja":
        "the church pew snapped under %(poss)s weight",
    "banqueta_lanchonete":
        "the stool at the diner counter gave way",
    "cadeira_churrasco":
        "the plastic chair buckled at the block cookout",
    "arquibancada_escola":
        "the bleacher plank broke through at the game",
    "cadeira_dobravel_festa":
        "the folding chair gave out at the party",
    "cadeira_guiche":
        "the chair at the service window blew apart",
    "rede_quintal":
        "the hammock post tore out of the deck",
    "tabua_pier":
        "the plank on the dock gave way under %(poss)s weight",
    "degrau_trailer":
        "the camper step tore off at the campground",
    "balanco_varanda":
        "the porch swing ripped out of the ceiling",
    "corrimao_biblioteca":
        "the handrail tore off the library stairs",
    "banco_restaurante":
        "the restaurant booth tore loose from the wall",
    # -- CLUSTER B -----------------------------------------------------------
    "mercado_faixa":
        "down in the supermarket lot, groceries rolling everywhere",
    "onibus_degrau":
        "off the bus step, laundry everywhere",
    "gelo_correios":
        "down at the post office, parcels everywhere",
    "praca_bandeja":
        "the tray went flying across the food court",
    "posto_latas":
        "down at the gas pump, cans rolling everywhere",
    "escada_rolante":
        "off the escalator, shopping spilled everywhere",
    "porta_giratoria":
        "stuck in the revolving door, coffee everywhere",
    "corredor_lixo":
        "down the outside steps, %(poss)s trash everywhere",
    "rampa_tinta":
        "down on the garage ramp, paint everywhere",
    "festa_rua":
        "down at the block party, food everywhere",
    "feira_caixote":
        "%(poss)s knee folded at the market kerb",
    "bingo_salao":
        "%(poss)s legs gave out at bingo night",
    # -- CLUSTER C -----------------------------------------------------------
    "empilhadeira_galpao":
        "sitting on a pallet on a forklift",
    "porta_arrancada":
        "the front door came off to get %(obj_pron)s out",
    "elevador_mudanca":
        "hoisted to a third-floor balcony on a ladder lift",
    "balanca_carga":
        "weighed on a freight scale like a load",
    "guincho_piscina":
        "hoisted out of the pool in a sling",
    "guincho_reboque":
        "pulled from a ditch by a tow winch",
    "carregadeira_feira":
        "carried across the fairground in a loader bucket",
    "talha_garagem":
        "raised off the garage floor by a hoist",
    "bolsa_ar_calcada":
        "lifted off the sidewalk on air bags",
    # -- CLUSTER D -----------------------------------------------------------
    "balanca_recepcao":
        "the clinic scale gave up on %(obj_pron)s",
    "manguito_pressao":
        "the cuff at the clinic would not close",
    "cadeira_rodas_estreita":
        "the wheelchair was too narrow for %(obj)s",
    "maca_transferencia":
        "it took four people to move %(obj_pron)s",
    "avental_costas":
        "the paper gown would not go on",
    "mesa_exame_papel":
        "the exam table dropped and the paper tore",
    "tomografo_estreito":
        "the hospital scanner would not take %(obj_pron)s",
    "andador_farmacia":
        "%(poss)s walker folded up in the pharmacy line",
    "cama_ala":
        "a wider hospital bed was wheeled in",
    "cadeira_dentista":
        "the dental chair stopped halfway down",
    # -- CLUSTER E -----------------------------------------------------------
    "catraca_metro":
        "the subway lane was too narrow",
    "trava_brinquedo":
        "the ride harness never closed over %(poss)s lap",
    "cinto_aviao":
        "the airplane seat belt would not reach around",
    "poltrona_cinema":
        "the cinema seat would not take %(obj)s",
    "provador_loja":
        "the fitting room curtain would not close",
    "bicicleta_academia":
        "%(poss)s knees would not clear the gym bike",
    "elevador_lobby":
        "the elevator would not close with %(obj_pron)s inside",
    "carro_concessionaria":
        "neither of them could get behind the wheel",
    "cavalo_trilha":
        "the trail horse was led away instead",
    "escada_farol":
        "the lighthouse stair was too narrow",
}
for _d in DESASTRES:
    _d["fala"] = DESASTRES_FALA[_d["id"]]


# ---------------------------------------------------------------------------
# ⭐⭐ A ABERTURA — CINCO FORMAS, e nenhuma delas e' invencao
# ---------------------------------------------------------------------------
# ⛔⛔ POOL DE UMA FORMA SO' NAO E' POOL. No RARO 16 eu escrevi oito hooks e os
# oito eram pergunta; quem viu foi o operador, na tela. Aqui o risco e' MAIOR,
# porque a assinatura da fonte E' uma forma so' (`This was X before` em 11 de
# 15) e copiar a fonte seria reincidir com desculpa.
# ⭐ As outras quatro formas saem de sentencas que os MESMOS videos dizem, so'
# que mais adiante, promovidas a' posicao de abertura:
#     rotina  <- v24  *"This was Janet's everyday reality."*
#     causa   <- v59  *"unable to move because of her size"*
#     dia     <- v09  *"This is what she faced every single day"*
#     tarefa  <- v24  *"Getting out of the car was already a struggle."*
#             + v39  *"A simple trip to Walmart started with a 10 minute fight"*
# Reposicionar sentenca da fonte nao e' escrever copy nova: e' usar o que ja'
# converteu num lugar em que ela ainda nao foi usada.
#
# ⛔⛔ TODA ENTRADA CARREGA O NOME, por um dos slots `ref`, `suj` ou
# `poss_nome`. Uma abertura que so' usa `obj` deixaria o casal sem nome no take
# 1 (`obj` e' `them` la'), e o nome e' o eixo mais barato do motor — perde-lo
# no unico take em que ele apresenta a pessoa esvazia o eixo inteiro. O
# autoteste varre o pool e cobra isso entrada por entrada.
ABERTURAS = [
    # -- APRESENTACAO — a assinatura literal da pagina (11 de 15) ---------
    {"id": "ap1", "forma": "apresentacao", "curto": "This was X before",
     "txt": "This was %(ref)s before,"},
    {"id": "ap2", "forma": "apresentacao", "curto": "This was X before all",
     "txt": "This was %(ref)s before all of this,"},
    {"id": "ap3", "forma": "apresentacao", "curto": "Look at X before",
     "txt": "Look at %(ref)s before,"},
    {"id": "ap4", "forma": "apresentacao", "curto": "X, a year ago",
     "txt": "This was %(ref)s a year ago,"},
    # -- ROTINA — v24 verbatim, promovida --------------------------------
    {"id": "ro1", "forma": "rotina", "curto": "everyday reality de X",
     "txt": "This was %(poss_nome)s everyday reality,"},
    {"id": "ro2", "forma": "rotina", "curto": "a semana inteira de X",
     "txt": "This was %(poss_nome)s whole week, every week,"},
    {"id": "ro3", "forma": "rotina", "curto": "a vida de X assim",
     "txt": "This was %(poss_nome)s %(vida)s, all of it,"},
    # -- CAUSA — v59 verbatim, promovida ---------------------------------
    {"id": "ca1", "forma": "causa", "curto": "X mal se movia",
     "txt": "%(Suj)s could barely move any more,"},
    {"id": "ca2", "forma": "causa", "curto": "o peso fez isso com X",
     "txt": "The weight did this to %(ref)s,"},
    # ⚠️ ESTA ENTRADA FOI ENCURTADA POR MEDICAO, nao por gosto: na forma
    # original (`%(Suj)s could not carry the weight any more,`) ela NUNCA saiu
    # em 400 sorteios. O `suj` do casal tem quatro palavras (`Marjorie and her
    # husband`), e com um beat de desastre de 13 ela nao cabia em orcamento
    # nenhum. Entrada que nao sai esta' morta e o autoteste a conta como viva.
    {"id": "ca3", "forma": "causa", "curto": "o peso mandava na vida de X",
     "txt": "The weight was running %(poss_nome)s %(vida)s,"},
    # -- DIA — v09 verbatim, promovida -----------------------------------
    {"id": "di1", "forma": "dia", "curto": "X passava por isso todo dia",
     "txt": "%(Suj)s faced this every single day,"},
    {"id": "di2", "forma": "dia", "curto": "todo dia era assim para X",
     "txt": "Every day looked like this for %(ref)s,"},
    {"id": "di3", "forma": "dia", "curto": "X acordava para isso",
     "txt": "%(Suj)s woke up to this every morning,"},
    # ⭐ AS DUAS CURTAS EXISTEM PARA A FORMA SOBREVIVER AO ORCAMENTO, e o
    # numero e' medido: com as tres primeiras entradas de cada forma, `tarefa`
    # caiu para 3% e `dia` para 9% dos videos — nao porque o sorteio as
    # despreze, mas porque nenhuma delas cabia ao lado dos beats de desastre
    # mais longos. Forma que so' tem entrada longa morre em silencio, e e' o
    # mesmo mecanismo que o RARO 16 pagou com as pontes curtas.
    {"id": "di4", "forma": "dia", "curto": "acontecia com X todo dia",
     "txt": "This happened to %(ref)s every day,"},
    # -- TAREFA — v24 e v39, promovidas ----------------------------------
    {"id": "ta1", "forma": "tarefa", "curto": "sair de casa ja' era luta",
     "txt": "For %(ref)s, leaving the house was a fight,"},
    {"id": "ta2", "forma": "tarefa", "curto": "uma ida simples virava isso",
     "txt": "One errand turned into this for %(ref)s,"},
    # ⚠️ Era *"Everything took %(ref)s ten minutes,"*, e o teste WTF a
    # derrubou colada num desastre que nao e' de demora (*"Everything took
    # Marilyn ten minutes, face down on their own driveway"*). A forma
    # `tarefa` tem de valer para os nove desastres.
    {"id": "ta3", "forma": "tarefa", "curto": "toda coisa pequena era luta",
     "txt": "Every small thing was a fight for %(ref)s,"},
    {"id": "ta4", "forma": "tarefa", "curto": "nada era simples para X",
     "txt": "Nothing was simple for %(ref)s,"},
]

FORMAS_ABERTURA = ("apresentacao", "rotina", "causa", "dia", "tarefa")

# ⛔⛔ E AS ENTRADAS FORAM COMPRIMIDAS ATE' A FAIXA FICAR ESTREITA (4 a 8
# palavras), o que e' o conserto ESTRUTURAL do vies de orcamento. Medido em
# 2.000 sorteios antes da compressao: a entrada mais sorteada saia 391 vezes e
# a menos sorteada 5 — as duas VIVAS pelo criterio do autoteste, e uma delas
# invisivel num lote de trinta videos.
# ⭐ Nenhum truque de sorteio conserta faixa larga: quando uma entrada custa o
# dobro da vizinha, o orcamento decide por ela. O sorteio nivela; o pool tem de
# caber.
#
# ⏳⏳ E ISSO CONTINUA VERDADE DEPOIS DO CONSERTO DE 2026-08-21, com o numero
# na mao. O `_sortear_plano` tirou o orcamento do papel de PESO e o deixou so'
# no papel de VIABILIDADE, e onde havia folga isso resolveu (a `vi7`, de dez
# palavras, foi de 6 sorteios em 400 para 31). Onde nao ha' folga nada resolve:
#     beat de desastre 13 + fecho 2 = 15  ->  sobram 10 para abertura+testemunha
#     menor abertura 4 + menor testemunha 5 = 9  ->  sobra UMA palavra
# A entrada de 7 palavras nao entra nessa conta em desastre nenhum desses, e
# por isso `ap1`+`ap3` (as duas de 4) ainda levam mais de um terco do lote.
# ⛔ O conserto que falta e' de COPY e e' alcada do operador: ou as entradas
# longas encurtam, ou os beats de desastre longos encurtam. O autoteste imprime
# a razao max/min por entrada para a divida ter numero em vez de impressao.


# ---------------------------------------------------------------------------
# ⭐⭐ A TESTEMUNHA — o beat que faz a humilhacao ser PUBLICA
# ---------------------------------------------------------------------------
# ⛔ Sem terceiro, isto e' acidente privado. A leitura otica achou SETE dos
# quinze reels sem um unico terceiro em quadro, e SEIS deles prometendo
# `getting filmed and laughed at by the people around her` na fala. Aqui o beat
# e' obrigatorio (lente RU1) e o pool e' de FORMA, nao de sinonimo.
#
# ⛔⛔ E A PALAVRA `filmed` SAIU. Ninguem filma em nenhum dos quinze videos —
# nao ha' um aparelho em quadro em lote nenhum — e escrever aparelho no prompt
# faz o gerador DESENHAR o aparelho (licao paga com um lote inteiro no VICK
# 16). Fala que promete o que a imagem nao paga e' o defeito que este motor
# existe para nao ter: o que ficou foi o que as testemunhas fazem de verdade —
# olham, viram a cabeca, apontam, riem e se calam.
#
# ⚠️ `forma` decide o par com o desastre (campo `formas` de cada entrada de
# DESASTRES): `plateia` so' existe onde ha' sala cheia, `dedo` so' onde ha'
# vizinho. Par que nao existe no mundo nao e' variedade, e' ruido — mesma
# mecanica do `certo`/`falso` do RARO 16, e a lente RU6 o cobra.
#
# ⛔⛔ E A FORMA TEM DE CASAR COM O QUE AS BEATS_TESTEMUNHA FAZEM NA IMAGEM, que e'
# FIXA por desastre. Isto foi achado LENDO a fala montada, nao por lente: o
# `silencio` (*"and the people there watched in total silence"*) saia sobre
# uma imagem cujas testemunhas estao explicitamente RINDO, em quatro dos nove
# desastres. Fala que desmente o proprio quadro e' o defeito que a leitura
# otica achou em seis dos quinze reels da fonte, invertido.
# ⚠️ Consequencia declarada: `silencio` e `plateia` sobrevivem em DOIS
# desastres cada (os dois de plateia sentada e quieta), e por isso saem em ~6%
# dos videos. E' estrutura, nao defeito — e e' por isso que o piso de forma do
# autoteste e' 4% e nao 10%.
# ⛔⛔ O NOME DO POOL E' `BEATS_TESTEMUNHA` E NAO `TESTEMUNHAS`, e isso e'
# conserto de um FALSO POSITIVO medido: o `medir_personagens --gate` classifica
# pool por NOME (o regex `NOMES_DE_POOL` inclui `TESTEMUNHAS?`) e reprovou este
# motor com SEIS eixos fisicos zerados — cabelo, pelo facial, oculos, porte,
# pele e ancora — em cima de um pool que nao tem gente nenhuma: sao BEATS DE
# FALA. ⭐ E a saida certa nao era declarar excecao no medidor: excecao diria
# *"este pool de gente legitimamente nao tem corpo"*, que e' mentira. As
# testemunhas de verdade, com corpo e com gesto, moram no campo `test` de cada
# entrada de `DESASTRES` — que e' onde o `medir_personagens` nao olha porque
# nao e' pool.
#
# ⛔⛔ E NENHUMA ENTRADA USA PRONOME SEM DONO. Quatro delas diziam `they`,
# `them` e `one of them` sem antecedente na propria fala (*"the chair cracked
# under her weight, and THEY laughed out loud"* — quem?), e pronome generico e'
# drifting: se o espectador pode perguntar de quem se trata, a copy esta'
# descartada. Cada uma passou a nomear o grupo: `the whole room`, `the people
# there`, `not one person`, `one of the neighbours`.
BEATS_TESTEMUNHA = [
    # -- RISO — a forma mais repetida da fonte (6 de 15), sem o `filmed` --
    {"id": "ri1", "forma": "riso", "curto": "riram dela",
     "txt": "and the people around %(obj)s laughed."},
    {"id": "ri2", "forma": "riso", "curto": "riram alto",
     "txt": "and the whole room laughed out loud."},
    {"id": "ri3", "forma": "riso", "curto": "riram e nao ajudaram",
     "txt": "and the people watching laughed instead."},
    {"id": "ri4", "forma": "riso", "curto": "riam enquanto acontecia",
     "txt": "and strangers stood there laughing."},
    # -- PLATEIA — v46/v50 verbatim --------------------------------------
    {"id": "pl1", "forma": "plateia", "curto": "todo mundo virou a cabeca",
     "txt": "and every head in the room turned."},
    {"id": "pl2", "forma": "plateia", "curto": "todo cliente olhou",
     "txt": "and every customer in that room looked."},
    {"id": "pl3", "forma": "plateia", "curto": "a sala inteira parou",
     "txt": "and the whole room stopped to watch."},
    # -- SILENCIO — v46/v50 verbatim -------------------------------------
    {"id": "si1", "forma": "silencio", "curto": "ninguem disse nada",
     "txt": "and nobody said a word."},
    {"id": "si2", "forma": "silencio", "curto": "olharam e se calaram",
     "txt": "and the people there watched in total silence."},
    {"id": "si3", "forma": "silencio", "curto": "ninguem desviou o olhar",
     "txt": "and not one person looked away."},
    # -- IMPOTENCIA — v09/v15/v51 verbatim -------------------------------
    {"id": "im1", "forma": "impotencia", "curto": "ninguem conseguiu erguer",
     "txt": "and nobody there could lift %(obj)s."},
    # ⚠️ ENCURTADA PELA MESMA MEDICAO: a forma longa (`wanted to help and
    # could not`) so' cabia com o beat de desastre mais curto do pool e saiu
    # ZERO vezes em 400 sorteios.
    {"id": "im2", "forma": "impotencia", "curto": "queriam ajudar e nao deu",
     "txt": "and the people around %(obj)s could not help."},
    {"id": "im3", "forma": "impotencia", "curto": "ficaram parados olhando",
     "txt": "and everyone just stood there watching."},
    # -- DEDO — v38 -------------------------------------------------------
    # ⚠️ AS DUAS PERDERAM O `it` EM 2026-08-21, e isso e' o cabecalho deste
    # pool sendo cumprido pela primeira vez. Ele ja' declarava *"NENHUMA
    # ENTRADA USA PRONOME SEM DONO"* e dizia que cada uma passou a nomear o
    # grupo — o GRUPO foi nomeado e o OBJETO do verbo ficou pendurado:
    # *"a neighbour shouted IT at him"* (gritou o QUE?), *"the neighbours
    # pointed and said IT"*. Medido: 43 de 400 videos (10,8%). Pronome sem
    # dono e' drifting, e o teste WTF descarta a sentenca.
    {"id": "de1", "forma": "dedo", "curto": "vizinho apontando e gritando",
     # ⚠️ E AS DUAS MANTIVERAM O COMPRIMENTO ORIGINAL (7 e 6 palavras) de
     # proposito: `de1` na forma longa (`shouted at her from the kerb`, 9
     # palavras) caiu de 17 para 2 sorteios em 400 — conserto de copy que
     # mata a propria entrada nao e' conserto.
     "txt": "and a neighbour was shouting at %(obj_pron)s."},
    {"id": "de2", "forma": "dedo", "curto": "apontaram o dedo",
     "txt": "and the neighbours pointed at %(obj_pron)s."},
    # ⚠️ ENCURTADA POR MEDICAO DE ALCANCE: com o `it` ela nunca saiu em 400
    # sorteios. Entrada que nao cabe com os minimos dos outros eixos esta'
    # morta, e o autoteste a contava como viva (§35).
    {"id": "de3", "forma": "dedo", "curto": "um deles gritou",
     "txt": "and one of the neighbours shouted across the street."},
    # -- JUIZO — v09/v15 verbatim ----------------------------------------
    {"id": "ju1", "forma": "juizo", "curto": "nao era o peso, era o julgamento",
     # ⚠️ O `just` NAO e' enfeite e e' verbatim da fonte (*"not just the
     # physical weight, but the judgment"*, v09/v15). Sem ele a frase NEGA o
     # peso — e o beat do desastio imediatamente antes acabou de dizer que a
     # escada cedeu SOB o peso. Achado LENDO o take montado, nao por lente:
     # *"the porch steps broke apart under their weight and it was never the
     # weight"* e' o teste WTF reprovando na primeira sentenca.
     "txt": "and the judgment was worse than the weight."},
    {"id": "ju2", "forma": "juizo", "curto": "o pior nao era o peso",
     "txt": "and the weight was never the worst part."},
    {"id": "ju3", "forma": "juizo", "curto": "julgada ali mesmo",
     "txt": "and %(suj)s got judged for it right there."},
]

FORMAS_TESTEMUNHA = ("riso", "plateia", "silencio", "impotencia", "dedo",
                     "juizo")


# ---------------------------------------------------------------------------
# TAKE 2 — a virada, o remedio e a prova
# ---------------------------------------------------------------------------
# ⚠️ `And this is her now` e' verbatim do v27; `And this is Betsy now` e'
# verbatim do v46. As duas formas convivem porque o eixo PESSOA decide qual
# sai: com nome, o nome; sem nome, o pronome.
VIRADAS = [
    {"id": "vi1", "curto": "e esta e' X agora", "txt": "And this is %(obj)s now,"},
    {"id": "vi2", "curto": "esta e' X hoje", "txt": "This is %(obj)s today,"},
    # ⚠️ REESCRITA POR MEDICAO (2026-08-21): era `And here is %(obj)s now,` e
    # devolvia *"And here is THEM now"* e *"And here is HIM now"* — ingles
    # quebrado em 34 de 400 videos. O slot `%(obj)s` e' OBJETO, e `here is X`
    # e' posicao de SUJEITO invertido. Com a copula em slot (`e_sao`) a mesma
    # entrada serve os tres numeros e continua carregando o nome.
    {"id": "vi3", "curto": "e aqui esta' X agora",
     "txt": "And here %(suj)s %(e_sao)s now,"},
    {"id": "vi4", "curto": "e esta e' X depois da mudanca",
     "txt": "And this is %(obj)s after the change,"},
    {"id": "vi5", "curto": "olhe para X agora", "txt": "Now look at %(obj)s,"},
    # ⚠️ AS DUAS FORAM REESCRITAS POR LEITURA DA FALA MONTADA, nao por
    # lente. A `vi6` era *"And this has been Betsy ever since"*, que e' ingles
    # torto; a `vi7` usava `%(ref)s` como SUJEITO e devolvia *"And this is what
    # THEM looked like after"* no casal. `ref` e' slot de OBJETO — quem serve
    # de sujeito e' `suj`, e por isso as duas passaram a usa'-lo no PASSADO,
    # que e' agnostico de numero.
    {"id": "vi6", "curto": "X saiu disso com esta cara",
     "txt": "%(Suj)s came out of it looking like this,"},
    {"id": "vi7", "curto": "e este e' o resultado",
     # ⚠️ Terminava em `after,` e a REMEDIO seguinte comeca em `after` — a
     # fala saia *"what he looked like after, after I gave him"*. Achado
     # lendo o take montado.
     "txt": "And this is what %(suj)s looked like a year on,"},
    {"id": "vi8", "curto": "e esta e' X desde entao",
     "txt": "And this is %(obj)s since then,"},
    {"id": "vi9", "curto": "veja X agora", "txt": "Look at %(obj)s now,"},
]

# ⛔ CT5 — NENHUM INGREDIENTE NOMEADO. O remedio e' `one simple remedy`, que e'
# o que a fonte diz nos quinze. A receita e' a UNICA moeda que o comentario
# compra; entregue uma vez, ela esta' gasta para os outros videos da pagina.
# ⛔ O REMEDIO USA O PRONOME, NUNCA O NOME — e e' o que a fonte faz: *"And
# this is Betsy now, after I gave HER one simple remedy"* (v46). A virada, que
# vem imediatamente antes, ja' disse o nome; repeti-lo devolvia *"And this is
# Janet one year later, after I gave JANET a simple remedy"*.
# ⛔⛔ E NENHUMA DURACAO AQUI. Duas duas entradas traziam `eight weeks` e
# `three months`, e as viradas traziam `eight months later` e `one year later`:
# o sorteio cruzava as duas listas e a fala saia *"this is her eight months
# later, after eight weeks of one simple remedy"* — dois relogios diferentes
# na mesma respiracao. ⭐ A duracao ficou num beat SO' (a prova `vd2`), e a
# lente RU13 cobra isso por video. A fonte, alias, nunca da' prazo nenhum.
REMEDIOS = [
    {"id": "re1", "curto": "um remedio simples toda manha",
     "txt": "after I gave %(obj_pron)s one simple remedy every single morning."},
    {"id": "re2", "curto": "um remedio simples, so' isso",
     "txt": "after one simple remedy, every single morning."},
    {"id": "re3", "curto": "o remedio que eu dei",
     "txt": "after I gave %(obj_pron)s one simple remedy to take every morning."},
    {"id": "re4", "curto": "o remedio que eu indiquei",
     "txt": "after the one simple remedy I told %(obj_pron)s about."},
    {"id": "re5", "curto": "o mesmo que eu tomo",
     "txt": "after I gave %(obj_pron)s the same simple remedy I take myself."},
    {"id": "re6", "curto": "um remedio e mais nada",
     "txt": "after one simple remedy every morning and nothing else."},
    {"id": "re7", "curto": "sem dieta, so' o remedio",
     "txt": "after one simple remedy every morning, with no diet at all."},
    {"id": "re8", "curto": "o remedio da minha mae",
     "txt": "after I gave %(obj_pron)s the simple remedy my mother gave me."},
    {"id": "re9", "curto": "o mesmo remedio, sem falhar",
     "txt": "after the same simple remedy, every morning without fail."},
]

# ⭐⭐ A PROVA — CINCO FORMAS, e a distribuicao e' MEDIDA no autoteste.
# ⚠️ `swelling`, `energy` e `drained itself` sao verbatim da fonte. Nenhuma
# delas promete numero de quilo nem prazo: a prova aqui e' o CORPO em quadro, e
# a fala so' nomeia o que o espectador ja' esta' vendo.
PROVAS = [
    {"id": "pe1", "forma": "peso", "curto": "o peso saiu, o inchaco baixou",
     "txt": "The weight came off, the swelling went down, and %(poss)s energy "
            "came back."},
    {"id": "pe2", "forma": "peso", "curto": "o peso saiu e nao voltou",
     "txt": "The weight came off and it never came back."},
    # ⚠️ `%(corpo)s` e nao `body`: no casal a fala dizia *"their body"* para
    # duas pessoas. E o `itself` saiu junto — com `bodies` ele quebra a
    # concordancia, e o verbo sozinho ja' diz tudo.
    {"id": "in1", "forma": "inchaco", "curto": "o inchaco sumiu",
     "txt": "%(Poss)s swelling disappeared and %(poss)s %(corpo)s finally "
            "drained."},
    {"id": "in2", "forma": "inchaco", "curto": "o corpo drenou sozinho",
     "txt": "The swelling is gone, and %(poss)s %(corpo)s finally drained."},
    {"id": "co1", "forma": "corpo", "curto": "o corpo voltou a ser dela",
     "txt": "A body that finally feels like %(poss)s own again."},
    {"id": "co2", "forma": "corpo", "curto": "cabe nas proprias roupas",
     # ⚠️ `%(obj_pron)s` e nao `%(obj)s`: com o nome saia *"Her own clothes
     # hang loose on Helen now"* — possessivo em pronome e objeto em nome na
     # mesma frase. Achado lendo a fala montada.
     "txt": "%(Poss)s own clothes hang loose on %(obj_pron)s now."},
    {"id": "en1", "forma": "energia", "curto": "a energia voltou",
     "txt": "%(Poss)s energy came back and it has not left since."},
    {"id": "en2", "forma": "energia", "curto": "sobe a escada sem parar",
     # ⚠️ Era `climbs`, e o casal devolvia *"they climbs"*. Todo verbo depois
     # de `%(suj)s` neste motor e' PASSADO ou MODAL, e o autoteste cobra isso.
     "txt": "%(Suj)s can climb the stairs now without stopping once."},
    {"id": "vd1", "forma": "vida", "curto": "mudou a vida por inteiro",
     "txt": "It completely transformed %(poss)s %(vida)s."},
    {"id": "vd2", "forma": "vida", "curto": "outra vida em oito meses",
     "txt": "Eight months, and %(poss)s whole %(vida)s changed."},
]

FORMAS_PROVA = ("peso", "inchaco", "corpo", "energia", "vida")


# ---------------------------------------------------------------------------
# TAKE 3 — o selo e o CTA
# ---------------------------------------------------------------------------
# ⛔⛔ O FOLLOW SAIU, E A RAZAO E' DE FATO. Os quinze reels fecham em *"follow
# me first or I can't reach you"* — e isso e' MENTIRA sobre a nossa automacao:
# *"a mensagem e' enviada independente de seguirem ou nao"* (operador,
# 2026-08-10). E' o CT8 do contrato, e aqui ele NAO precisa de excecao: o beat
# inteiro sai e as palavras vao para a isca. Copiar a fonte aqui seria copiar
# um portao que nao existe.
# ⛔ CT1 — a sentenca do CTA e' a ULTIMA. O selo vem ANTES, sempre.
SELOS = [
    {"id": "se0", "curto": "(sem selo)", "txt": ""},
    {"id": "se1", "curto": "sem remedio e sem cirurgia",
     "txt": "No pills and no surgery."},
    {"id": "se2", "curto": "custa quase nada", "txt": "It costs almost nothing."},
    {"id": "se3", "curto": "ja' esta' na sua cozinha",
     "txt": "You already have most of it at home."},
    {"id": "se4", "curto": "dois minutos por manha",
     "txt": "It takes two minutes a morning."},
    {"id": "se5", "curto": "sem medico e sem receita",
     "txt": "No doctor and no prescription."},
    {"id": "se6", "curto": "a mesma coisa toda manha",
     "txt": "The same thing every morning, nothing else."},
    {"id": "se7", "curto": "ninguem precisa saber",
     "txt": "Nobody around you has to know."},
    {"id": "se8", "curto": "eu tomo ha' quarenta anos",
     "txt": "I have taken it myself for forty years."},
]

# ⛔ A VIRGULA DEPOIS DA KEYWORD nao e' estilo: sem a micro-pausa o Veo emenda
# a palavra na frase. E o comando e' um LITERAL — comando variavel faz o modelo
# parafrasear a keyword, e a legenda do video nasce do Whisper rodando sobre o
# audio gerado.
# ⛔ CT6 — todo CTA diz ONDE a receita chega. O comentario leva nome e foto num
# feed publico; sem a cobertura, o custo social de comentar fica maior que a
# curiosidade.
CTAS = [
    {"id": "ct1", "curto": "quer saber o que eu dei?",
     "txt": "Want to know what I gave %(obj)s? %(cta)s and I will send it to "
            "your messages."},
    {"id": "ct2", "curto": "quer o mesmo?",
     "txt": "You want the same thing I gave %(obj)s? %(cta)s and it goes "
            "straight to your messages."},
    {"id": "ct3", "curto": "cabe numa linha",
     "txt": "What I gave %(obj)s fits in one line. %(cta)s and it lands in "
            "your messages."},
    {"id": "ct4", "curto": "peca e eu mando",
     "txt": "If you want what I gave %(obj)s, just say so. %(cta)s and I will "
            "send it to your messages."},
    {"id": "ct5", "curto": "quer o mesmo resultado?",
     # ⚠️ `%(suj)s` e nao `%(ref)s`: com `ref` este CTA devolvia *"Want the
     # same result THEM got?"* no casal. Mesmo defeito da `vi7`.
     "txt": "Want the same result %(suj)s got? %(cta)s and the whole thing "
            "goes to your messages."},
    {"id": "ct6", "curto": "me peca",
     "txt": "Ask me for what I gave %(obj)s. %(cta)s and it arrives in your "
            "messages."},
    {"id": "ct7", "curto": "quer saber o que mudou?",
     "txt": "Want to know what changed for %(obj)s? %(cta)s and I will send it "
            "to your inbox."},
    {"id": "ct8", "curto": "eu mando a mesma coisa",
     "txt": "I will send you exactly what I gave %(obj)s. %(cta)s and check "
            "your messages."},
    {"id": "ct9", "curto": "e' uma coisa so'",
     "txt": "It is one thing, and it is the same thing I gave %(obj)s. "
            "%(cta)s and it goes to your messages."},
]


# ===========================================================================
# CLAUSULAS DE QUADRO
# ===========================================================================
# ⛔⛔ A ORIENTACAO NAO CITA APARELHO. O `banho16_3t` descreve *"a person
# standing at the shelf filming with their phone in portrait mode"* — la' isso
# resolveu uma vista aerea, mas aqui e' proibido por ordem: a camera descreve
# ANGULO e ALTURA, nunca o aparelho, e nunca por negacao. Cada entrada de
# `DESASTRES` traz a sua geometria em graus e altura, que e' o que a ordem
# pede — e a lente RU5 varre os seis blocos atras de qualquer aparelho.
ORIENTACAO = "Vertical 9:16 portrait orientation."

CAUDA = ("Everyday amateur snapshot look, soft sensor grain. No on-screen "
         "text, no subtitles, no captions, no watermark.")

# ⭐ A camera dos dois quadros do reencontro e' a MESMA, e travada: na fonte os
# dois beats sao um plano continuo em 12 dos 15 reels. Mudar de angulo entre o
# take 2 e o take 3 leria como corte para outra casa.
# ⛔⛔ E A CLAUSULA NAO CONTA GENTE. Ela dizia `holding both figures full
# length` e o quadro do CASAL tem TRES pessoas (ela, o marido e a Ruth) —
# medido em 126 de 400 videos (32%). Instrucao de enquadramento que conta
# menos gente do que o bloco descreve e' convite para o gerador cortar alguem,
# e quem sai e' o marido ou a Ruth. ⚠️ Derivar o numero (`both`/`all three`)
# resolveria o casal e quebraria no dia em que o elenco mudasse outra vez: a
# forma NEUTRA nao tem esse prazo de validade. O autoteste cobra que nenhuma
# palavra de contagem volte para ca'.
CAM_REENCONTRO = ("The shot is taken from a few paces back at chest height, "
                  "level and straight on, holding everyone in frame full "
                  "length from the ground up")

# ⛔ A TRAVA ANTI-ARTEFATO. Cena de queda com varias pessoas e' onde o gerador
# mais inventa membro: um braco a mais, uma perna sem dono, dedos fundidos. A
# leitura otica achou os tres em SETE dos quinze reels (v24, v27, v28, v38,
# v46, v49, v51), e a clausula custa quinze palavras.
ANATOMIA = ("Every person in frame has two arms, two legs and five fingers on "
            "each hand, all limbs attached to a body that is visible in the "
            "shot.")

# ===========================================================================
# ⭐⭐ AS DUAS MARCAS DO BLOCO DE CORPO — a fronteira que a lente RU20 le'
# ===========================================================================
# ⛔ A RU20 cobra os tres sinais de obesidade (numero de peso, posicao no
# quadro, comparacao) NA SAIDA MONTADA, e nao no pool. Para isso ela precisa
# saber ONDE o corpo comeca e ONDE termina dentro da IMAGE 01 — varrer o bloco
# inteiro faria a lente passar pelo motivo errado, porque `cen`, `acao` e
# `test` tambem falam em `frame` e em `wider than`.
# ⭐ O corpo abre sempre em `MARCA_CORPO` e fecha sempre no literal do
# elemento 6 (`SUPORTE_FIM`), que e' a ultima sentenca que a montagem escreve
# antes de o `acao` do desastre entrar. Duas ancoras literais, nenhuma
# heuristica.
MARCA_CORPO = "At the centre of the frame"
SUPORTE_FIM = "with none of it showing on either side."

# ⭐ ELEMENTO 6 — A CONSEQUENCIA NO QUE SUSTENTA O PESO, e ela e' GENERICA de
# proposito. O concorrente escreve *"The small wooden chair has completely
# vanished under the seated man"*, que so' funciona porque o video dele tem uma
# cadeira. Aqui sao SESSENTA E DOIS desastres — poltrona, degrau, rampa, maca,
# lona de guindaste, chao de garagem — e uma frase por desastre morreria no dia
# seguinte, porque o campo `acao` e' reescrito toda semana por outra mao.
# ⛔ A forma sem substantivo (`whatever is under her taking her weight`) e'
# verdadeira nos sessenta e dois e diz exatamente o que o gerador precisa
# desenhar: o movel sumiu debaixo do corpo e nao aparece dos lados.
SUPORTE_SINGULAR = ("Whatever is under %s has vanished from sight beneath "
                    "%s, " + SUPORTE_FIM)
SUPORTE_CASAL = ("Whatever is under the two of them has vanished from sight "
                 "beneath them, " + SUPORTE_FIM)

# ⭐ A DERIVA DE CAMERA, uma por take. Camera identica em cortes seguidos e' o
# que denuncia geracao, e a fonte varia a imperfeicao em cada plano.
DERIVAS = [
    "The camera has a constant subtle handheld sway with a tiny drift to one "
    "side.",
    "The camera drifts slightly forward with a subtle wobble.",
    "The camera has a faint wobble and a tiny involuntary zoom-in that settles "
    "back.",
    "The camera sways gently and settles.",
    "The camera holds almost still with a slow shallow breath of movement.",
]


# ===========================================================================
# HELPERS
# ===========================================================================

def _palavras(t):
    return len(re.findall(r"[A-Za-z0-9'%()\-]+", t or ""))


_UNI = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
        "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
        "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
        "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19,
        "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
        "seventy": 70, "eighty": 80, "ninety": 90}


def _libras(txt):
    """⭐ O PESO EM LIBRAS, lido do numero POR EXTENSO que o corpo escreve.

    ⛔ Existe porque a faixa e' contrato e nao gosto: 350-550 lb num angulo de
    EMAGRECIMENTO, onde a MESMA pessoa aparece magra oito segundos depois. O
    concorrente escreve 880 lb e pode — o video dele nao emagrece ninguem.
    ⚠️ Comparar strings nao serve: o autoteste tem de ler o NUMERO, senao a
    trava passa a ser *"tem a palavra pounds"*, que e' forma sem funcao (§41).
    """
    m_ = _RX_PESO_LIBRAS.search(txt or "")
    if not m_:
        return None
    partes = m_.group(0).lower().replace("-", " ").split()
    total = 0
    for w in partes:
        if w == "hundred":
            total *= 100
        elif w in _UNI:
            total += _UNI[w]
    return total


def _cap(s):
    return s[0].upper() + s[1:] if s else s


def _chave(x):
    return x["id"] if isinstance(x, dict) else str(x)


def _fresco(pool, usados, rng):
    """Sorteia evitando o que saiu nos ultimos lotes.

    ⛔ Pool grande com sorteio sem memoria repete igual — licao paga no PEE 16,
    onde duas ampliacoes de pool nao consertaram a repeticao porque o problema
    nunca foi o tamanho.
    """
    livres = [x for x in pool if _chave(x) not in usados]
    return rng.choice(livres or list(pool))


def _por_id(pool, valor):
    if isinstance(valor, dict):
        return valor
    for x in pool:
        if x.get("id") == valor:
            return x
    return None


def _cta_literal():
    """`Comment recipe,` — com a palavra vinda do painel quando ele a troca."""
    return "Comment %s," % sc.keyword_do_motor(sys.modules[__name__])


def _dic(spec):
    """O dicionario gramatical que TODA entrada de copy consome.

    ⛔ E' o que permite um pool so' servir mulher, homem e casal. Ver o bloco
    de campos em `PESSOAS`.
    """
    p = spec["pessoa"]
    return {"ref": p["ref"], "Ref": _cap(p["ref"]),
            "suj": p["suj"], "Suj": _cap(p["suj"]),
            "obj": p["obj"], "Obj": _cap(p["obj"]),
            "poss": p["poss"], "Poss": _cap(p["poss"]),
            "poss_nome": p["poss_nome"], "Poss_nome": _cap(p["poss_nome"]),
            "obj_pron": p["obj_pron"], "e_sao": p["e_sao"],
            "vida": p["vida"], "corpo": p["corpo"],
            "cta": _cta_literal()}


def _r(txt, d):
    return txt % d


# ===========================================================================
# LEDGER
# ===========================================================================
EIXOS_LEDGER = ("desastre", "pessoa", "reencontro", "roupa", "rosto",
                "parceiro", "abertura", "testemunha", "prova", "cta")


def _carregar_ledger():
    if not os.path.isfile(LEDGER):
        return {}
    try:
        with io.open(LEDGER, encoding="utf-8") as f:
            return json.load(f)
    except (ValueError, IOError):
        return {}


def _gravar_ledger(ledger, spec=None):
    if spec is not None:
        for eixo in EIXOS_LEDGER:
            v = spec.get(eixo)
            if isinstance(v, dict):
                ledger.setdefault(eixo, []).append(v["id"])
                ledger[eixo] = ledger[eixo][-24:]
    try:
        with io.open(LEDGER, "w", encoding="utf-8") as f:
            f.write(json.dumps(ledger, ensure_ascii=False, indent=1))
    except IOError:
        pass


# ===========================================================================
# SORTEIO DA COPY
# ===========================================================================

def _tem_relogio(txt):
    """A frase carrega uma EXPRESSAO DE PRAZO? (`a year on`, `eight months`)

    ⚠️ Frequencia (`every morning`, `every single day`) NAO conta — sao coisas
    diferentes e convivem na mesma respiracao sem contradicao. Mesmo criterio
    da lente `RU13`, e de proposito: o filtro do sorteio e a lente que o cobra
    tem de ler a MESMA coisa, senao um dos dois mente.
    """
    return bool(_RX_DURACAO.search(txt or ""))


def _uniforme_por_forma(itens, rng):
    """FORMA uniforme, e so' entao ENTRADA uniforme dentro dela.

    `itens` sao tuplas `(entrada, n_palavras, tem_relogio)`.
    """
    grupos = {}
    for it in itens:
        grupos.setdefault(it[0].get("forma", "-"), []).append(it)
    return rng.choice(grupos[rng.choice(sorted(grupos))])


def _sortear_plano(pools, teto, rng):
    """Sorteia uma combinacao com o ORCAMENTO entrando como VIABILIDADE, nunca
    como peso.

    `pools` e' uma lista de listas de `(entrada, n_palavras, tem_relogio)`.

    ⛔⛔ ESTA FUNCAO SUBSTITUI O `_sortear_por_forma`, E O MOTIVO E' MEDIDO
    (2026-08-21). Ele nivelava forma e entrada — mas nivelava **dentro do
    conjunto que ja' tinha sobrevivido ao filtro de orcamento**, e a entrada
    longa nao esta' nesse conjunto na maioria dos desastres. O resultado, em
    400 sorteios:

        apresentacao   ap1=78 (4 palavras) · ap3=74 (4) | ap2=5 (7) · ap4=9 (6)
        tarefa         ta4=65 (5)                       | ta1=3 (8) · ta3=3 (8)
        impotencia     im1=56 (6) · im3=60 (6)          | im2=4 (8)
        silencio       si1=11 (5)                       | si2=2 (8)

    Com a pre-selecao `sexo=homem` — que e' o modo real de lote — `ap1`+`ap3`
    levavam **180 de 400 videos (45%)** e `de3` saia **zero** vezes. O proprio
    docstring do antecessor dizia ter consertado isso ("`im2` nunca sorteou uma
    unica vez"); medido depois, `im2` tinha saido de 0 para 4 em 400. De morta
    para quase-morta.

    ⭐ A REGRA NOVA E' UMA SO': **sorteia-se a entrada ANTES de olhar o
    orcamento, e o orcamento so' decide QUEM AINDA CABE DEPOIS DELA.** Os eixos
    sao percorridos em ordem ALEATORIA por video, cada um plano por forma e
    depois por entrada, restrito ao que ainda deixa completacao viavel (a soma
    do que ja' foi gasto mais o MINIMO de cada eixo que falta). Assim a entrada
    de 8 palavras nao compete com a irma de 4: ela e' escolhida primeiro e o
    orcamento passa a valer para as OUTRAS.
    ⚠️ A ordem e' sorteada, e nao fixa, porque quem vai primeiro e' quem fica
    perfeitamente plano — fixar a ordem seria escolher qual eixo tem o
    privilegio, e os dois eixos deste motor tem entradas de tamanho desigual.

    ⛔ E O PRAZO E' EXCLUSIVO POR FALA. Escolhida uma entrada que carrega
    duracao, os eixos que faltam perdem as suas — e' a lente `RU13` movida para
    DENTRO do sorteio. Medida antes: `vi7` x `vd2` produzia *"looked like a
    year on [...] Eight months, and her whole life changed"* em 11 dos 810
    trios, e o autoteste de 400 seeds FIXAS nunca via (1 em 3.000 sorteios
    livres, 6 em 1.440 sob as travas do painel). Defeito que so' aparece na
    tela do operador e' defeito que o gate nao pega.
    """
    n = len(pools)
    restante = {k: list(pools[k]) for k in range(n)}
    ordem = list(range(n))
    rng.shuffle(ordem)
    escolha, gasto = {}, 0
    for k in ordem:
        resto = sum(min(it[1] for it in restante[j])
                    for j in range(n) if j != k and j not in escolha)
        cand = restante[k]
        cabem = [it for it in cand if gasto + it[1] + resto <= teto]
        # ⚠️ Fallback: a entrada mais CURTA do eixo. Ele existe para o dia em
        # que um beat de desastre novo estourar o orcamento sozinho — e o
        # autoteste ja' cobra esse teto entrada por entrada, entao aqui ele
        # nunca deveria disparar.
        cabem = cabem or sorted(cand, key=lambda it: it[1])[:1]
        it = _uniforme_por_forma(cabem, rng)
        escolha[k], gasto = it[0], gasto + it[1]
        if it[2]:
            for j in range(n):
                if j not in escolha:
                    restante[j] = ([x for x in restante[j] if not x[2]]
                                   or restante[j])
    return tuple(escolha[i] for i in range(n))


def _medir(pool, d):
    """O pool com o comprimento e o relogio de cada entrada JA' RENDERIZADOS.

    ⛔ Medir a entrada com os slots preenchidos e nao com `%(suj)s` cru nao e'
    detalhe: `suj` vale `Marjorie and her husband` no casal e `she` no
    singular, e a mesma entrada custa quatro palavras a mais num video e nao no
    outro. Orcamento medido no molde e' orcamento medido errado.
    """
    saida = []
    for x in pool:
        t = _r(x["txt"], d)
        saida.append((x, _palavras(t), _tem_relogio(t)))
    return saida


# ---------------------------------------------------------------------------
# ⛔⛔ O GUARDA DE `room` — ACHADO LENDO A FALA MONTADA (2026-08-21)
# ---------------------------------------------------------------------------
# O acoplamento `formas` cobre a forma da testemunha e nao cobre a PALAVRA
# dentro dela. Quatro beats dizem `room`: os tres de `plateia` (que ja' saem
# so' onde ha' sala cheia, e por isso estavam certos) e o `ri2`, que e' de
# `riso` e nao tinha porteiro nenhum. Medido: `and the whole room laughed out
# loud` saia sobre um ponto de onibus, um patio de posto, uma rua fechada e um
# gramado de casa — **7 de 400 videos ANTES da expansao e 19 de 400 DEPOIS**,
# porque o pool novo trouxe muito lugar aberto.
# ⚠️ Este e' o MESMO defeito que o cabecalho do `rampa_medico` ja' registrava
# (*"as tres entradas dessa forma dizem `room`, e isto e' uma rampa ao ar
# livre"*) — a doutrina existia e cobria uma forma so'. Aqui ela vira campo.
# ⛔ E o porteiro NAO e' `plateia`: piscina coberta, academia, recepcao de
# clinica e vestiario sao INTERIORES sem plateia sentada, e gatear por
# `plateia` mataria `riso` em quatro cenas fechadas corretas. O campo
# `interior` responde a pergunta que a palavra faz, que e' *"ha' quatro
# paredes?"* — nada mais.
# ⭐ Nenhuma palavra de copy foi tocada: o beat `ri2` continua identico e
# continua saindo. O que mudou foi ONDE ele pode sair.
_RX_SALA = re.compile(r"\broom\b", re.I)


def _beat_cabe(t, des):
    """O beat de testemunha cabe naquele desastre? Forma + quatro paredes."""
    if t["forma"] not in des["formas"]:
        return False
    if _RX_SALA.search(t["txt"]) and not des.get("interior", True):
        return False
    return True


def _falas(spec, rng, quais=(0, 1, 2)):
    """As tres falas, cada uma sorteada entre as combinacoes que CABEM.

    ⛔⛔ NUNCA EM CASCATA (escolher o primeiro beat e depois procurar um que
    caiba): isso colapsa a variancia — medido no VICK 16, onde o take 2 saiu
    com UMA fala em 400 videos.

    ⛔⛔ E SORTEIA-SE A **ENTRADA** ANTES DO ORCAMENTO, nao depois. Ver o
    docstring de `_sortear_plano`: num sorteio filtrado por orcamento a entrada
    CURTA nao ganha peso, ela ganha o LOTE, porque a longa simplesmente nao
    esta' no conjunto que sobrou.
    """
    d = _dic(spec)
    des = spec["desastre"]
    f = dict(enumerate(spec.get("falas", ["", "", ""])))

    if 0 in quais:
        beat = _r(des["fala"], d)
        # ⛔ A testemunha e' filtrada pelo campo `formas` do desastre: plateia
        # so' onde ha' sala cheia, dedo so' onde ha' vizinho.
        # ⛔⛔ E PELO CADEADO DO PAINEL, que ate' 2026-08-21 nao existia aqui.
        # `travas["testemunha"]` era declarada em `EIXOS_TRAVAVEIS` e NUNCA
        # lida: o cadeado era honrado em 23 de 200 sorteios — 11%, que e' o
        # acaso de 1 em 13 formas cabiveis — e o botao `trocar` do painel via
        # a escolha do operador sobreviver 4 vezes em 120. Botao que promete e
        # nao entrega e' pior que botao ausente (GO21), e a unica lente que
        # pegaria isso estava desligada de proposito em `IGNORA_PAINEL`.
        pool_t = [t for t in BEATS_TESTEMUNHA if _beat_cabe(t, des)]
        fixo = _palavras(beat) + _palavras(FECHO_ATO1)
        travada = spec.get("trava_testemunha")
        if travada:
            so_ela = [t for t in pool_t if t["id"] == _chave(travada)]
            # ⚠️ E O CADEADO CEDE QUANDO A ENTRADA NAO CABE, em vez de estourar
            # o teto: medido, `de3` (9 palavras) travada sobre um beat de
            # desastre de 13 devolvia uma cena 1 de 28 palavras — tres
            # segundos de fala cortados, que e' o CTA inteiro no take 3 e o
            # `Pure shame.` aqui. Cadeado que entrega fala cortada e' pior que
            # cadeado que cede: o primeiro mente sobre o VIDEO, o segundo so'
            # sobre o botao, e a lente RU12 nao perdoa nenhum dos dois.
            menor_ab = min(_palavras(_r(a["txt"], d)) for a in ABERTURAS)
            if so_ela and (fixo + menor_ab
                           + _palavras(_r(so_ela[0]["txt"], d))
                           <= TETO_FALA[1]):
                pool_t = so_ela
        a, t = _sortear_plano([_medir(ABERTURAS, d), _medir(pool_t, d)],
                              TETO_FALA[1] - fixo, rng)
        spec["abertura"], spec["testemunha"] = a, t
        # ⚠️ A VIRGULA ANTES DA TESTEMUNHA nao e' estilo: todas as entradas
        # de `BEATS_TESTEMUNHA` abrem em `and`, e sem ela o take saia *"because of
        # her weight and every head in the room turned"* — duas oracoes coladas
        # sem respiro, que o TTS le' numa tirada so'. Achado lendo a fala
        # montada, nao por lente.
        f[0] = "%s %s, %s %s" % (_r(a["txt"], d), beat, _r(t["txt"], d),
                                 FECHO_ATO1)

    if 1 in quais:
        v, m, p = _sortear_plano([_medir(VIRADAS, d), _medir(REMEDIOS, d),
                                  _medir(PROVAS, d)], TETO_FALA[2], rng)
        spec["virada"], spec["remedio"], spec["prova"] = v, m, p
        f[1] = "%s %s %s" % (_r(v["txt"], d), _r(m["txt"], d), _r(p["txt"], d))

    if 2 in quais:
        # ⭐ O SELO E' OPCIONAL E O POOL VAZIO COMPETE DE IGUAL, como a PROVA
        # do RARO 16: forcar o selo estouraria os 25 nos CTAs longos, e o que
        # corta no fim de um take de 8s e' justamente o pedido.
        s, c = _sortear_plano([_medir(SELOS, d), _medir(CTAS, d)],
                              TETO_FALA[3], rng)
        spec["selo"], spec["cta"] = s, c
        f[2] = " ".join(x for x in (_r(s["txt"], d), _r(c["txt"], d)) if x)

    return f


# ===========================================================================
# SORTEIO
# ===========================================================================

def sortear(pagina, rng, led, travas=None):
    travas = travas or {}
    hist = led if isinstance(led, dict) else {}
    etnia = ETNIA.get(pagina, "white American")

    # ⛔ O DESASTRE E' O EIXO PRINCIPAL e por isso e' sorteado primeiro: e' ele
    # que decide quais pessoas cabem (o salao pede mulher, a rampa pede casal)
    # e quais formas de testemunha existem naquele quadro.
    desastre = (_por_id(DESASTRES, travas["desastre"])
                if travas.get("desastre")
                else _fresco(DESASTRES, hist.get("desastre", [])[-4:], rng))

    # ⚠️ A PRE-SELECAO DE SEXO VENCE O DESASTRE, e o desastre cede. Botao que
    # promete `homem` e devolve a cadeira do salao e' pior que botao ausente —
    # e o filtro que cede em silencio foi medido no GOOD 16, onde travar
    # `praia` numa pagina branca devolvia 0 de 120.
    sexo = travas.get("sexo")
    if sexo and sexo != "livre" and sexo not in desastre["sexos"]:
        cabem = [x for x in DESASTRES if sexo in x["sexos"]]
        if cabem:
            desastre = _fresco(cabem, hist.get("desastre", [])[-4:], rng)

    # ⛔ O CADEADO DA TESTEMUNHA FAZ O DESASTRE CEDER, como o da pessoa — e
    # ele nao existia: `travas["testemunha"]` era declarada em
    # `EIXOS_TRAVAVEIS`, desenhada no painel e NUNCA lida. Medido em 200
    # sorteios por eixo, o cadeado era honrado 23 vezes (11%, o acaso de 1 em
    # 13 formas cabiveis) contra 200 de 200 nos eixos que o codigo lia.
    # ⚠️ O `desastre` travado vence: e' ele que arrasta o mundo inteiro.
    t_trav = travas.get("testemunha")
    if t_trav and not travas.get("desastre"):
        alvo_t = _por_id(BEATS_TESTEMUNHA, t_trav)
        if alvo_t and alvo_t["forma"] not in desastre["formas"]:
            cabem = [x for x in DESASTRES
                     if _beat_cabe(alvo_t, x)
                     and (not sexo or sexo == "livre" or sexo in x["sexos"])]
            if cabem:
                desastre = _fresco(cabem, hist.get("desastre", [])[-4:], rng)

    pool_p = [p for p in PESSOAS if p["sexo"] in desastre["sexos"]]
    if sexo and sexo != "livre":
        pool_p = [p for p in pool_p if p["sexo"] == sexo] or pool_p
    pessoa = (_por_id(PESSOAS, travas["pessoa"]) if travas.get("pessoa")
              else _fresco(pool_p or PESSOAS, hist.get("pessoa", [])[-6:], rng))
    # ⛔ Cadeado do painel na PESSOA vence: o desastre cede, nunca a pessoa.
    if pessoa["sexo"] not in desastre["sexos"]:
        cabem = [x for x in DESASTRES if pessoa["sexo"] in x["sexos"]]
        desastre = rng.choice(cabem) if cabem else desastre

    # ⛔⛔ O CADEADO DE `rosto` E DE `roupa` VENCE A PESSOA, e isto e' conserto
    # de defeito MEDIDO (2026-08-21): o cadeado do painel era honrado em 152 de
    # 200 sorteios no rosto e em 188 de 200 na roupa, porque a pessoa era
    # sorteada ANTES e o acoplamento fazia o valor travado ceder EM SILENCIO.
    # ⭐ A ordem certa e' a mesma do `desastre`: quem cede e' o eixo LIVRE.
    # Cadeado que cede em silencio e' pior que cadeado ausente (GO21).
    # ⚠️ Quando `pessoa` TAMBEM esta' travada, ela vence — e' ela que carrega
    # nome, pronomes e idade, e trocar a pessoa trocaria a fala inteira.
    if travas.get("rosto") and not travas.get("pessoa"):
        alvo = _por_id(ROSTOS, travas["rosto"])
        preciso = "homem" if alvo and alvo["sexo"] == "homem" else "mulher"
        if (pessoa["sexo"] == "homem") != (preciso == "homem"):
            cabem = [x for x in pool_p
                     if (x["sexo"] == "homem") == (preciso == "homem")]
            if cabem:
                pessoa = _fresco(cabem, hist.get("pessoa", [])[-6:], rng)
    if travas.get("roupa") and not travas.get("pessoa"):
        alvo = _por_id(ROUPAS, travas["roupa"])
        if alvo and pessoa["sexo"] not in alvo["sexos"]:
            cabem = [x for x in pool_p if x["sexo"] in alvo["sexos"]]
            if cabem:
                pessoa = _fresco(cabem, hist.get("pessoa", [])[-6:], rng)
                if pessoa["sexo"] not in desastre["sexos"]:
                    outros = [x for x in DESASTRES
                              if pessoa["sexo"] in x["sexos"]]
                    desastre = rng.choice(outros) if outros else desastre

    # ⛔ O rosto casa com o SEXO da pessoa. No casal, o rosto e' o DELA — e' ela
    # que o video nomeia e e' ela que a REF ancora; o marido nunca e' nomeado
    # em nenhum dos quinze reels.
    sexo_rosto = "homem" if pessoa["sexo"] == "homem" else "mulher"
    pool_r = [x for x in ROSTOS if x["sexo"] == sexo_rosto]
    rosto = (_por_id(ROSTOS, travas["rosto"]) if travas.get("rosto")
             else _fresco(pool_r, hist.get("rosto", [])[-5:], rng))
    if rosto["sexo"] != sexo_rosto:
        rosto = _fresco(pool_r, hist.get("rosto", [])[-5:], rng)

    pool_roupa = [x for x in ROUPAS if pessoa["sexo"] in x["sexos"]]
    roupa = (_por_id(ROUPAS, travas["roupa"]) if travas.get("roupa")
             else _fresco(pool_roupa or ROUPAS, hist.get("roupa", [])[-5:], rng))
    if pessoa["sexo"] not in roupa["sexos"]:
        roupa = _fresco(pool_roupa or ROUPAS, hist.get("roupa", [])[-5:], rng)

    reencontro = (_por_id(REENCONTROS, travas["reencontro"])
                  if travas.get("reencontro")
                  else _fresco(REENCONTROS, hist.get("reencontro", [])[-4:],
                               rng))

    # ⭐⭐ O ROSTO NO ATO 1 E' EIXO, NAO PALPITE. A fonte esconde o rosto em 6
    # de 15 e mostra nos outros 9 — e o v46, que mostra, e' justamente o unico
    # com testemunha de verdade em foco. Nao da' para decidir com quinze
    # pontos: variavel confundida vira eixo e o campo responde. Mesma mecanica
    # do `mecanismo` do BANHO 16 3T.
    quer = travas.get("rosto_ato1")
    if quer in ("oculto", "visivel"):
        oculto = (quer == "oculto")
    else:
        oculto = bool(rng.getrandbits(1))

    spec = {
        "pagina": pagina, "etnia": etnia,
        "desastre": desastre, "pessoa": pessoa, "rosto": rosto,
        "roupa": roupa, "reencontro": reencontro,
        "idade": pessoa["idade"],
        "rosto_oculto": oculto,
        "parceiro": _fresco(PARCEIROS, hist.get("parceiro", [])[-2:], rng),
        # ⛔ TRES DERIVAS DISTINTAS no mesmo video: `rng.sample` garante que os
        # tres takes nunca repitam o movimento de camera, que e' o que denuncia
        # geracao em cortes seguidos.
        "derivas": rng.sample(DERIVAS, 3),
        # ⛔⛔ O CADEADO DA TESTEMUNHA VIVE NO SPEC, e nao numa assinatura nova
        # de `_falas`. Razao: quem re-sorteia a copy sao TRES caminhos
        # diferentes — `sortear`, `nova_fala` (o botao `trocar` de cena) e
        # `_coerir_cena` (a troca de eixo no painel) —, e um parametro extra
        # so' seria passado pelo primeiro. Foi assim que o cadeado morreu na
        # primeira versao: o eixo estava em `EIXOS_TRAVAVEIS`, o painel o
        # desenhava, e `travas["testemunha"]` nunca era lida em lugar nenhum.
        "trava_testemunha": travas.get("testemunha"),
    }
    spec["falas"] = [v for _, v in sorted(_falas(spec, rng).items())]
    return spec


def nova_fala(spec, i, rng):
    """O botao `trocar` de cena, que a UI chama por este nome.

    ⚠️ Ele existe e e' cobrado pelo autoteste porque no BANHO 16 3T o mesmo
    botao ficou MORTO por heranca: a UI procurava `nova_fala(spec, i, rng)` e o
    que havia era `trocar_fala(spec, rng, i)` — outro nome, outra ordem.
    """
    return _falas(spec, rng, quais=(i,))[i]


def trocar_fala(spec, rng, i):
    return nova_fala(spec, i, rng)


# ===========================================================================
# MONTAGEM
# ===========================================================================

def _genero(pessoa):
    return {"mulher": "woman", "homem": "man", "casal": "couple"}[pessoa["sexo"]]


def _cena_testemunha(spec):
    """`test`, `mov` e `audio` do desastre — na variante MUDA quando o beat
    sorteado e' `silencio`.

    ⛔⛔ Ver o bloco `A CENA MUDA` em `DESASTRES`: os dois unicos desastres que
    comportam a forma `silencio` tem riso escrito no quadro, e a fala saia
    dizendo *"and nobody said a word"* sobre gente rindo em 21 de 21 sorteios
    dessa forma. ⚠️ O `audio_q` e' opcional porque um dos dois ja' nasceu com
    audio sem riso — campo escrito sem necessidade e' campo que apodrece.
    """
    d = spec["desastre"]
    if spec.get("testemunha", {}).get("forma") == "silencio":
        return (d.get("test_q", d["test"]), d.get("mov_q", d["mov"]),
                d.get("audio_q", d["audio"]))
    return d["test"], d["mov"], d["audio"]


def montar(spec):
    des, p, rc = spec["desastre"], spec["pessoa"], spec["reencontro"]
    roupa, rosto, par = spec["roupa"], spec["rosto"], spec["parceiro"]
    et, idade = spec["etnia"], spec["idade"]

    # ⛔⛔ A VOZ E' UM BLOCO TRAVADO E REPETIDO PALAVRA POR PALAVRA NOS TRES
    # TAKES. Cada take e' uma chamada de video SEPARADA — o modelo ve' UM take
    # por vez e nao tem o anterior — entao pedir *"a mesma voz dos outros"* e'
    # anafora sem antecedente. O que faz tres geracoes independentes
    # convergirem e' a descricao ser especifica o bastante para caber uma voz
    # so': altura, corpo, textura, sotaque e volume.
    # ⭐ E quem narra os TRES takes e' a RUTH, inclusive o da humilhacao, onde
    # ela nao aparece. E' o que a fonte faz nos quinze reels — a voz da senhora
    # sobre a queda e' o que transforma o acidente em testemunho.
    # ⛔ `slow deliberate cadence` NAO entra: medido em 2026-08-20, pedir
    # lentidao derruba a fala de 3,49 para 2,62 palavras por segundo, que num
    # take de 8s e' a diferenca entre 25 e 20 palavras faladas.
    voz = ("Voice: one calm American woman in her eighties with a plain rural "
           "accent, pitched low and unhurried, close to the microphone at "
           "ordinary conversational volume, never raised and never whispered, "
           "speaking at the ordinary pace of everyday American speech, never "
           "stretching or slowing the words to fill the take. The pitch, the "
           "texture, the accent and the speed are identical in all three "
           "takes.")

    # ⭐⭐ A ANCORA DE IDENTIDADE, e ela e' repetida POR EXTENSO nos tres
    # quadros. Sem isso o take 2 devolve outra pessoa — e' literalmente o que a
    # fonte faz no v27 (loira de 35 vira grisalha de 55) e no v45 (o homem
    # branco de barba curta vira hispanico).
    # ⛔ Ela SO' cita traco que o peso nao move: olhos, sobrancelha, ponte do
    # nariz, orelha, sinal permanente, cabelo. Maxilar, bochecha e queixo
    # ficariam em contradicao com a magreza do take 2, e contradicao o gerador
    # resolve mexendo no que estava certo.
    # ⛔⛔ A ETNIA NAO ENTRA NA ANCORA, e isso e' o defeito FT14 do FIGHT 16
    # cometido por mim e pego lendo o bloco: as tres frases que consomem a
    # ancora JA' dizem a etnia (*"a very heavy 48-year-old Black American
    # woman"*), entao repeti-la aqui punha o gentilico duas vezes no mesmo
    # sintagma — e duas vozes decidindo a mesma coisa o Veo resolve inventando.
    # ⚠️ A primeira versao ainda o punha como aposto solto (*"the same face as
    # the reference photo, white American, deep-set eyes"*), com o gentilico
    # pendurado sem substantivo.
    ancora = rosto["desc"]

    # -- BLOCO 0 (REF) — o ROSTO -------------------------------------------
    # ⛔ Este motor TEM BLOCO 0 e ele e' obrigatorio, ao contrario do
    # `banho16_3t`, que o dispensou por ordem do operador. La' a ancora era a
    # MAO e ela ja' estava na IMAGE 01, na mesma luz; aqui o corpo MUDA de
    # proposito entre os quadros e a unica coisa que atravessa e' o rosto —
    # que precisa de foto propria, neutra, sem o peso de nenhum dos dois atos.
    ref = ("REF 01: Photo of a real person: a head and shoulders portrait of a "
           "%d-year-old %s, %s. Plain neutral grey background, soft even "
           "frontal light, the head upright and facing the lens. Slight sensor "
           "grain, raw amateur photo look. No on-screen text, no subtitles, no "
           "captions, no watermark."
           % (idade, "%s %s" % (et, "man" if p["sexo"] == "homem"
                                else "woman"), rosto["desc"]))

    # -- IMAGE 01/03 — A HUMILHACAO ----------------------------------------
    if spec["rosto_oculto"]:
        # ⛔ POSITIVO, NUNCA POR NEGACAO: `the face is not shown` injeta o
        # token que se quer evitar (mesma licao do `not a celebrity`). O que
        # esconde o rosto e' descrever de onde a camera olha.
        # ⛔⛔ A OCULTACAO DESCREVE O CORPO, NUNCA A CAMERA. A primeira
        # versao dizia *"shot from behind and slightly above"* — e o bloco JA'
        # traz a geometria da camera no campo `cam` do desastre. Duas posicoes
        # de camera no mesmo bloco e' contradicao, e o gerador escolhe uma, que
        # nao e' a nossa: e' a licao que o BANHO 16 3T pagou com `shot straight
        # on` brigando com `thirty degrees`.
        quem = ("turned away from the lens so that only the back of the head "
                "and the shoulders are visible, %s, wearing %s"
                % (rosto["cabelo"], roupa["antes"]))
    else:
        quem = ("the head turned toward the lens with the features fully "
                "readable, the same face as the reference photo, %s, wearing %s"
                % (ancora, roupa["antes"]))

    # -- ⭐⭐ A ARQUITETURA DO CORPO — os seis elementos, nesta ordem --------
    # ⛔⛔ ELA EXISTE PORQUE O OPERADOR REPROVOU UM LOTE COM O VIDEO NA MAO
    # (2026-08-21): *"nao esta' gerando personagens obesos, inclusive alguns
    # parecem ate' magros"*. O bloco antigo gastava CATORZE PALAVRAS de
    # adjetivo (*"They are both wide through the middle."*) e o gerador nao
    # desenha adjetivo — ele desenha FORMA, AREA DE QUADRO e COMPARACAO. Sem as
    # tres ele volta para a media do treino, que e' uma pessoa comum.
    # ⭐ A ordem e' a do concorrente cujo corpo SAI obeso, e cada elemento tem
    # uma funcao distinta: 1 escala, 2 area de pixel, 3 superficie, 4 membros,
    # 5 pescoco, 6 o movel que sumiu.
    # ⛔ E ELA E' DO TAKE 1 E SO' DELE. As IMAGE 02/03 continuam magras — o
    # motor existe para mostrar a MESMA pessoa obesa e depois magra.
    pf = "his" if p["sexo"] == "homem" else "her"
    of = "him" if p["sexo"] == "homem" else "her"

    # ⛔⛔ O ELEMENTO 2 GANHA UMA CLAUSULA DE ORIENTACAO, E ELA E' CONDICIONAL.
    # Com o rosto VISIVEL a barriga e' o objeto mais perto da lente, que e' o
    # que a poe na frente de tudo. Com `rosto_oculto` a camera esta' ATRAS da
    # pessoa: dizer que a barriga aponta para a lente contradiz o proprio
    # quadro, e contradicao o gerador resolve virando o corpo — que e' matar o
    # modo inteiro (mesma classe do defeito que a RU4 mede).
    if spec["rosto_oculto"]:
        eixo_barriga = ("It stands out well past both sides of %s back, so its "
                        "full width still reads from behind." % pf)
    else:
        eixo_barriga = "It is the nearest thing in the frame to the lens."

    # ⛔ ELEMENTO 5 EM DUAS VARIANTES: `pescoco` traz queixo, papada e bochecha
    # — os tracos que o PESO MOVE e que por isso estao BANIDOS da ancora de
    # rosto (`ROSTOS`). Com o rosto oculto eles saem por contradicao direta e
    # entra a `nuca`, que e' o que se ve' de costas.
    elem5 = p["nuca"] if spec["rosto_oculto"] else p["pescoco"]

    if p["sexo"] == "casal":
        suporte = SUPORTE_CASAL
    else:
        suporte = SUPORTE_SINGULAR % (of, of)

    corpo_p = " ".join(x for x in (p["porte"], p["barriga"], eixo_barriga,
                                   roupa["sobre"], p["membros"], elem5,
                                   p.get("segundo", ""), suporte) if x)

    if p["sexo"] == "casal":
        # ⛔⛔ `and beside her` SAIU, e e' conserto de defeito MEDIDO em 253 de
        # 1.200 videos (21,1%): a frase punha os dois COLADOS e tres palavras
        # depois o `acao` os punha em lugares diferentes (*"one sitting back on
        # the broken step [...] and the other flat on the driveway below"*,
        # *"tangled together and pointing in opposite directions"*). Duas
        # geometrias incompativeis no mesmo bloco, e o gerador escolhe uma.
        # ⭐ Quem coloca os dois no espaco tem de ser o `acao`, que e' o unico
        # que sabe onde eles cairam — `with her` os declara juntos na CENA sem
        # fixar posicao relativa. Lente `RU15`.
        # ⛔ O SEGUNDO CORPO VEM COMPRIMIDO (`segundo`, dentro de `corpo_p`):
        # cento e quarenta palavras vezes dois estouram os 3.900 caracteres da
        # AdBatch, e bloco cortado em silencio e' o pior modo de falha que ha'.
        corpo1 = ("%s are a very heavy %d-year-old %s woman, %s, and with her "
                  "%s. %s" % (MARCA_CORPO, idade, et, quem, par["antes"],
                              corpo_p))
    else:
        # ⚠️ PRONOME, NUNCA O NOME, na direcao de cena: o gerador nao sabe
        # quem e' Betty e um nome proprio no prompt e' token sem referente. O
        # nome vive na FALA, que e' onde ele compra alguma coisa.
        corpo1 = ("%s is a very heavy %d-year-old %s %s, %s. %s"
                  % (MARCA_CORPO, idade, et,
                     "man" if p["sexo"] == "homem" else "woman", quem, corpo_p))

    # ⛔ A CENA MUDA quando o beat da fala e' `silencio` — ver o bloco de
    # doutrina em `DESASTRES`. O quadro e' o mesmo; o que muda e' o gesto das
    # testemunhas e o audio.
    test_d, mov_d, audio_d = _cena_testemunha(spec)

    b1 = ("%s %s. %s %s. %s. %s %s %s %s"
          % (ORIENTACAO, _cap(des["cen"]), corpo1, _cap(des["acao"]),
             _cap(test_d), des["cam"] + ".", ANATOMIA, des["luz"], CAUDA))

    t1 = ("TAKE 01/03: Animate the provided image exactly. Handheld shot, very "
          "slight natural sway, no cuts. %s. Everyone stays where the image "
          "puts them and nobody new walks into the shot. %s %s\n"
          'Dialogue: "%s"\n%s\nAudio: %s. No music.'
          % (mov_d, ANATOMIA, spec["derivas"][0],
             sonorizar(spec["falas"][0]), voz, audio_d))

    # -- IMAGE 02/03 — O REENCONTRO ----------------------------------------
    # ⭐ O ANTES E O DEPOIS NA MESMA PECA. A roupa que estava esticada no
    # quadro anterior aparece aqui CAINDO SOLTA: o espectador le' "e' a mesma
    # pessoa" e "ela emagreceu" sem uma palavra. E' o achado do v46, e e' a
    # unica coisa na fonte que resolve o problema central deste angulo.
    if p["sexo"] == "casal":
        depois = ("a slim %d-year-old %s woman, the same face as the reference "
                  "photo, %s, wearing %s, and beside her %s"
                  % (idade, et, ancora, roupa["depois"], par["depois"]))
    else:
        depois = ("a slim %d-year-old %s %s, the same face as the reference "
                  "photo, %s, wearing %s"
                  % (idade, et, "man" if p["sexo"] == "homem" else "woman",
                     ancora, roupa["depois"]))

    # ⛔⛔ QUEM ESTA' AO LADO DA RUTH TEM DE CONCORDAR COM O ELENCO, e este e' o
    # defeito mais silencioso que a varredura de 2026-08-21 achou: as tres
    # frases de direcao de cena diziam `the person beside her` e `has turned
    # HER head` — literais cravados no FEMININO SINGULAR — em 400 de 400
    # blocos. Nos 57 videos de HOMEM o mesmo bloco dizia `man` e `her head`;
    # nos 126 de CASAL havia DUAS pessoas ao lado da Ruth e a direcao dirigia
    # UMA, sem dizer qual, deixando o marido sem instrucao nenhuma. 183 de 400
    # videos (46%) com o bloco contradizendo a si mesmo, e nenhuma das treze
    # lentes olhava para isso.
    # ⭐ O motor JA' tinha `poss`/`obj_pron`/`suj` em `PESSOAS` exatamente para
    # isto; a direcao de cena e' que nao os consumia. Lente `RU17`.
    if p["sexo"] == "casal":
        vizinho_img = ("the two beside her have turned their heads toward the "
                       "Amish woman and are laughing")
        vizinho_t2 = "the two beside her keep the smile"
        vizinho_t3 = "the two beside her turn back to the lens and hold the smile"
    else:
        vizinho_img = ("the person beside her has turned %s head toward the "
                       "Amish woman and is laughing" % p["poss"])
        vizinho_t2 = "the person beside her keeps the smile"
        vizinho_t3 = ("the person beside her turns back to the lens and holds "
                      "the smile")

    # ⚠️ `on one side of %s` com o PRONOME e nao com `them` cravado: no
    # singular a frase saia *"a slim 37-year-old man [...] and on one side of
    # THEM an Amish woman"* — plural para uma pessoa so'. No casal o pronome
    # ja' e' `them`, entao a mesma frase serve os dois.
    b2 = ("%s %s. Standing shoulder to shoulder and facing the lens are %s, "
          "and on one side of %s %s. Everyone is still and smiling except "
          "the Amish woman, who is talking straight to the lens with one open "
          "hand lifted from her waist. %s. %s %s %s"
          % (ORIENTACAO, _cap(rc["amb"]), depois, p["obj_pron"], RUTH,
             CAM_REENCONTRO, ANATOMIA, rc["luz"], CAUDA))

    t2 = ("TAKE 02/03: Animate the provided image exactly. Handheld shot, very "
          "slight natural sway, no cuts. As the line begins the Amish woman "
          "turns her face to the lens and starts talking. Halfway through the "
          "line she lifts her open hand a little higher from her waist. As the "
          "line ends the hand settles back and %s. Everyone holds the same "
          "position and nobody new walks into the shot. %s %s\n"
          'Dialogue: "%s"\n%s\nAudio: %s. No music.'
          % (vizinho_t2, ANATOMIA, spec["derivas"][1],
             sonorizar(spec["falas"][1]), voz, rc["audio"]))

    # -- IMAGE 03/03 — A RECEITA + CTA -------------------------------------
    # ⛔ MESMO LUGAR E MESMO ENQUADRAMENTO do quadro anterior: na fonte os dois
    # beats sao um plano continuo em 12 dos 15 reels, e trocar de angulo aqui
    # leria como corte para outra casa.
    # ⚠️ O QUE MUDA E' O GESTO, e isso e' conserto de um defeito da fonte: la'
    # o segundo beat e' um RE-TAKE da mesma foto posada (o aceno reinicia do
    # zero, a boca muda de forma no meio do mesmo retrato). Dois quadros
    # identicos com a fala trocada leem como falha de edicao.
    # ⛔⛔ SEM `the same` NA FRENTE DO ARTIGO. A primeira versao montava
    # *"the same a slim 52-year-old woman"* e *"the same an Amish woman"* —
    # artigo duplicado, que e' a mesma classe do `held upright, held upright`
    # do TRIO 16: o artigo e' da FRASE, nunca do dado. Quem diz que e' a mesma
    # gente e' a primeira sentenca do bloco, e ela basta.
    # ⚠️ E saiu o `facing the lens` daqui: o proprio bloco diz logo abaixo que
    # a pessoa ao lado VIROU a cabeca para a Ruth. Duas direcoes de olhar na
    # mesma pessoa e' contradicao, e contradicao o gerador resolve contra nos.
    b3 = ("%s The same place and the same framing as the previous scene: %s. "
          "Standing shoulder to shoulder are %s, and on one side of %s %s. "
          "The Amish woman now has her right palm raised open toward the lens "
          "at chest height, and %s. %s. %s %s %s"
          % (ORIENTACAO, rc["amb"], depois, p["obj_pron"], RUTH, vizinho_img,
             CAM_REENCONTRO, ANATOMIA, rc["luz"], CAUDA))

    t3 = ("TAKE 03/03: Animate the provided image exactly. Handheld shot, very "
          "slight natural sway, no cuts. As the line begins the Amish woman "
          "holds the raised palm toward the lens. Halfway through the line the "
          "palm drops slowly back to her waist. As the line ends %s. Everyone "
          "holds the same position and nobody new walks into the shot. %s %s\n"
          'Dialogue: "%s"\n%s\nAudio: %s. No music.'
          % (vizinho_t3, ANATOMIA, spec["derivas"][2],
             sonorizar(spec["falas"][2]), voz, rc["audio"]))

    return sc.selar_takes(sc.selar_tags({
        "BLOCO 0 (REF)": ref,
        IMAGENS[0]: b1, TAKES[0]: t1,
        IMAGENS[1]: b2, TAKES[1]: t2,
        IMAGENS[2]: b3, TAKES[2]: t3,
    }))


# ===========================================================================
# AS LENTES
# ===========================================================================
# ⛔ Regex escrito por EDICAO LITERAL, nunca por heredoc: `\b` dentro de
# heredoc nao-citado chega ao arquivo como BACKSPACE (0x08), o Python compila,
# o editor nao mostra nada e o padrao simplesmente NUNCA casa.

# ⛔⛔ O APARELHO. `camera` e `lens` NAO entram: eles descrevem o PONTO DE
# VISTA, que e' o idioma do parque inteiro (*"facing the lens"*, *"the camera
# has a subtle sway"*). O que se proibe e' o aparelho NA MAO de alguem em
# quadro — foi assim que o `vick16` disse `with the phone in his free hand` e o
# gerador desenhou o telefone num lote inteiro.
# ⚠️ E aqui isso pesa mais que em qualquer outro motor: a fala da FONTE promete
# `getting filmed` em seis dos quinze reels e nao ha' um aparelho em quadro em
# nenhum deles. A tentacao de "consertar" a fonte pondo celulares na mao das
# testemunhas esta' escrita aqui para nao ser cometida.
_RX_APARELHO = re.compile(
    r"\b(phones?|iphones?|smartphones?|camcorder|filming|filmed|recording|"
    r"selfie|tripod|gimbal|livestream(ing)?)\b", re.I)

_RX_GELATINA = re.compile(r"\bgelatin[ea]?\b", re.I)

# ⛔ A PALAVRA IMEDIATAMENTE ANTES DE `%(ref)s`, para a lente de posicao do
# slot no autoteste. ⚠️ Slot no INICIO da frase nao casa e por isso passa: la'
# ele so' aparece depois de preposicao (`For %(ref)s, leaving the house...`),
# que e' posicao de objeto e e' legitima.
_RX_ANTES_REF = re.compile(r"([A-Za-z']+)\s+%\(ref\)s")

# ⛔ A EXPRESSAO DE PRAZO, para a lente RU13. ⚠️ `every morning` e `every single
# day` NAO entram: sao FREQUENCIA, nao duracao, e as duas convivem com um prazo
# na mesma frase sem contradicao alguma (*"eight months of it, every single
# morning"*). Lente que confunde as duas reprovaria o pool inteiro.
_RX_DURACAO = re.compile(
    r"\b(?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|"
    r"a few|several|forty|a)\s+(?:days?|weeks?|months?|years?)\b", re.I)

# ⛔⛔ A PECA FANTASMA (lente RU3). ⚠️ O ARTIGO DEFINIDO E' O RECORTE INTEIRO:
# `a heavy man in a polo` e `two nail technicians in black work polos` sao
# roupa de OUTRA pessoa e sao legitimos; `the dress` e `the shirt` co-referem
# com quem o bloco ja' vestiu, e e' ai' que a contradicao mora. Sem essa
# restricao a lente acusaria as testemunhas de todos os nove desastres.
# ⚠️ E `the clothing` fica de FORA de proposito: e' generico e serve qualquer
# peca do eixo `ROUPAS` — o que se proibe e' nomear OUTRA peca, nao falar de
# roupa.
_RX_PECA_FANTASMA = re.compile(
    r"\bthe (shirt|t-shirt|dress|blouse|tunic|polo|tank top|sweater|"
    r"cardigan|skirt)\b", re.I)

# ⛔ O ROSTO NUM QUADRO FILMADO DE COSTAS (lente RU4).
_RX_ROSTO_NO_PORTE = re.compile(
    r"\b(face|faces|mouth|eyes|eyelids?|expression|cheeks?|jaw)\b", re.I)

# ⛔⛔ O TRACO QUE O PESO MOVE, para a variante `nuca` (contrato de pool). Com o
# rosto OCULTO a camera esta' atras: queixo, papada e bochecha nao existem em
# quadro, e escreve-los e' a contradicao que faz o gerador virar o corpo.
# ⚠️ Eles sao OBRIGATORIOS na variante `pescoco`, que e' o elemento 5 do corpo
# com o rosto visivel — a mesma palavra e' contrato num campo e defeito no
# vizinho, e por isso os dois sao cobrados separadamente.
_RX_TRACO_DE_PESO = re.compile(r"\b(chins?|jowls?|cheeks?|jaws?|jawline)\b",
                               re.I)

# ⛔⛔ O SINTAGMA DE PESSOA NOVO (lente RU14), e ele NAO e' o adjetivo. O
# defeito e' `heavy` + modificadores + um SUBSTANTIVO DE GENTE (*"the very
# heavy customer"*), que e' o que da' licenca ao gerador para desenhar mais um
# corpo. Descricao longa de UMA barriga nao casa com isto nenhuma vez.
_RX_CORPO_NOMEADO = re.compile(
    r"\b(?:very|extremely) heavy\b(?:\s+[a-z0-9-]+){0,4}?\s+"
    r"\b(?:woman|women|man|men|husband|wife|person|people|customer|customers|"
    r"shopper|shoppers|patient|patients|passenger|passengers|guest|guests|"
    r"occupant|occupants|body|bodies|figure|figures|male|female)\b", re.I)

# ⛔⛔ OS TRES SINAIS QUE A LENTE RU20 COBRA NO BLOCO DE CORPO MONTADO. Foi a
# ausencia dos tres que produziu o lote reprovado de 2026-08-21, e nenhuma das
# dezenove lentes olhava para eles.
#   (i) O NUMERO DE PESO. Por extenso, que e' como o corpo o escreve, e na
#       faixa 350-550 lb — creditar oitocentas libras num angulo de
#       EMAGRECIMENTO e' escrever um corpo que o take 2 nao consegue desmentir.
_RX_PESO_LIBRAS = re.compile(
    r"\b(?:three|four|five)\s+hundred(?:\s+and\s+[a-z-]+)?\s+pounds\b", re.I)
#  (ii) A POSICAO NO QUADRO — quanto do frame o corpo ocupa. E' o elemento que
#       mais faltava: sem area de pixel declarada o gerador aloca a area da
#       media do treino, que e' uma pessoa comum.
_RX_POSICAO_QUADRO = re.compile(
    r"\b(?:fills?|filling|covers?|covering|takes?|taking|occupies|occupying|"
    r"spans?|spanning)\b[^.:;]{0,80}?\b(?:frame|picture)\b"
    r"|\b(?:edge to edge|from the left edge to the right edge|"
    r"from one edge to the other|from side to side|corner to corner)\b"
    r"|\bnearest thing in the frame\b", re.I)
# (iii) A COMPARACAO — contra o proprio corpo (braco mais grosso que coxa,
#       barriga mais larga que ombro) ou contra uma coisa do mundo que pesa
#       aquilo. Adjetivo o gerador ignora; comparacao ele resolve desenhando.
_RX_COMPARACAO = re.compile(
    r"\b(?:wider|thicker|bigger|larger|heavier|broader|wide|thick)\s+than\b"
    r"|\bas\s+(?:heavy|thick|wide|big)\s+as\b"
    r"|\btwice\s+(?:as|the)\b"
    r"|\blargest thing\b|\bbiggest (?:single )?(?:thing|shape|object)\b"
    r"|\blargest (?:single )?(?:object|shape)\b", re.I)

# ⛔ A CONTAGEM NA CLAUSULA DE CAMERA (contrato de `CAM_REENCONTRO`).
_RX_CONTAGEM = re.compile(
    r"\b(both|two|three|all three|the pair|the couple)\b", re.I)

# ⛔ A CAMERA PARADA DENTRO DE UM BLOCO CUJO TAKE E' HANDHELD (contrato de
# `cam`). ⚠️ `level`, `straight on` e `at chest height` NAO entram: sao ANGULO
# e ALTURA, que e' exatamente o que o campo deve dizer.
_RX_CAM_PARADA = re.compile(r"\b(still|locked[- ]off|static|tripod)\b", re.I)

# ⛔⛔ A SEGUNDA PECA NO CORPO DE QUEM O VIDEO APRESENTA (lente RU19).
# ⭐ O NOME DA PECA, sem artigo nenhum — ao contrario do `_RX_PECA_FANTASMA`,
# que so' pega o artigo DEFINIDO. Aqui quem faz o recorte nao e' o artigo, e'
# a CONSTRUCAO: o que se proibe e' vestir, nao e' mencionar.
# ⚠️ `clothes`, `clothing` e `garment` ficam de FORA de proposito: sao
# genericos e apontam de volta para a propria peca do eixo `ROUPAS` — dizer
# *"still in its own street clothes"* e' o jeito certo de nao despir alguem
# sem declarar conformidade (`fully clothed` e' municao, licao de 2026-07-31).
_PECAS = (r"gowns?|robes?|smocks?|coats?|jackets?|blazers?|windbreakers?|"
          r"hoodies?|shirts?|t-shirts?|blouses?|tunics?|polos?|tank tops?|"
          r"sweaters?|sweatshirts?|cardigans?|vests?|waistcoats?|aprons?|"
          r"overalls?|scrubs|uniforms?|suits?|dress|dresses|skirts?|jeans|"
          r"trousers|slacks|shorts|leggings|pyjamas|pajamas|bunker gear")
_RX_PECA_NO_CORPO = re.compile(r"\b(%s)\b" % _PECAS, re.I)

# ⭐ AS DESIGNACOES DA PROTAGONISTA no bloco montado. Sao FECHADAS porque quem
# as escreve e' o motor: o `acao` de todo desastre chama quem cai de `the
# body`, `one of them`, `the other` ou `both`, e o `corpo1` do `montar` abre em
# `a very heavy NN-year-old`. Testemunha nenhuma usa nenhuma delas.
_ALVO = (r"the bod(?:y|ies)|one of them|the other|both of them|both are|"
         r"very heavy")

# ⛔⛔ A PASSAGEM DE DONO. Estes tokens dizem que a frase trocou de sujeito e
# que a roupa dali em diante e' de OUTRO: `, while a warehouse worker in a
# hi-vis vest`, `with two orderlies in navy scrubs`, `holding a folded coat`,
# `hung with dresses and jeans`. Sem eles a lente reprovaria a empilhadeira, a
# maca e o provador — que estao CERTOS. ⚠️ Ser generoso aqui so' pode DEIXAR
# PASSAR defeito, nunca criar falso positivo; e' a direcao certa de errar numa
# lente cujo custo de falso positivo e' reescrever cena que ja' funciona.
_PASSAGEM = (r"while|with|and|beside|behind|as|holding|held|hold|hung|"
             r"hanging|hangs|carried|carrying|carries|spread|standing|"
             r"stands|sits|sitting|steady|steadies|wheels|works|worn by")

# ⛔⛔ E OS DOIS PONTOS SAO FRONTEIRA DURA, junto com o ponto final — conserto
# de um FALSO POSITIVO MEDIDO (1 em 1.200 sorteios, `porta_arrancada`). Todo
# campo `test` deste pool abre a lista de testemunhas com dois pontos, e a
# frase antes deles termina em `and not ONE OF THEM is leaving:` — que casa a
# designacao da protagonista e emenda em `two men in work jackets`. Sem essa
# fronteira a lente reprovava um bloco CERTO, que e' o unico jeito de uma
# lente destas nascer morta.
_LIMITE = r"[^.:;]"

# ⛔⛔ A CONSTRUCAO INTEIRA — ALVO + verbo de vestir + peca, sem troca de dono
# no meio e sem sair da frase. E' isto que a `avental_costas` fazia:
# *"the body has come out of the cubicle IN A PALE BLUE PAPER GOWN"*, e o
# mesmo paragrafo ja' dizia *"wearing a cream blouse [...] stretched tight
# across the back"*. O gerador escolhe UMA das duas, e se escolher o avental o
# take 2 (`the same cream blouse, now hanging loose`) fica sem referente: a
# ancora de continuidade do angulo morre naquele video.
_RX_VESTIR_NO_ALVO = re.compile(
    r"\b(?:%s)\b"
    r"(?:(?!\b(?:%s)\b)%s)*?"
    r"\b(?:wearing|dressed in|changed into|into|in)\s+"
    r"(?:[a-z][a-z-]*\s+){0,5}"
    r"\b(?P<peca>%s)\b" % (_ALVO, _PASSAGEM, _LIMITE, _PECAS), re.I)

# ⛔ E A FORMA SEM PREPOSICAO, que o `bote_passeio` usava antes de sair
# (*"an orange life vest IS ON OVER THE SHOULDERS"*): a peca e' o sujeito e o
# corpo e' o complemento. Nenhum ALVO aparece na frase, entao a lente de cima
# nunca a veria.
_RX_VESTIDO_SOBRE = re.compile(
    r"\b(?P<peca>%s)\b[^.]{0,60}?"
    r"\b(?:is on over|are on over|pulled on over|worn over|put on over|"
    r"is on the shoulders|goes on over)\b" % _PECAS, re.I)


# ⛔⛔ LAPIDE — `_sem_dialogo(txt)` MORREU EM 2026-08-21 E FICA ESCRITO AQUI.
# Ela era `re.sub(r"Dialogue:.*", "", txt, flags=re.S)` e servia a RU5. O
# `re.S` faz o `.` casar `\n`, entao ela nao tirava a LINHA do dialogo: tirava
# tudo do primeiro `Dialogue:` ate' o fim do bloco — a fala, o `Voice:` e o
# `Audio:`. A lente lia dois tercos do TAKE e o controle negativo plantava o
# defeito justamente no terco que ela lia. ⭐ A licao generaliza: *corte por
# regex com `re.S` nao remove uma linha, remove uma cauda* — e cauda removida
# em silencio e' lente que passa por estar cega.


def _corpo_montado(img1):
    """⭐ O BLOCO DE CORPO RECORTADO DA IMAGE 01 MONTADA.

    ⛔ Da abertura (`MARCA_CORPO`) ao fim do elemento 6 (`SUPORTE_FIM`), que e'
    a ultima sentenca que a montagem escreve antes de o `acao` do desastre
    entrar. Devolve `""` quando qualquer uma das duas ancoras falta — e quem
    reprova a ausencia e' a lente, nunca este recorte em silencio (a lapide do
    `_sem_dialogo` logo acima e' exatamente esta licao).
    """
    i = img1.find(MARCA_CORPO)
    j = img1.find(SUPORTE_FIM)
    if i < 0 or j < 0 or j < i:
        return ""
    return img1[i:j + len(SUPORTE_FIM)]


def _ru1_testemunha(spec, blocos, ach):
    """⛔⛔ RU1 — A TESTEMUNHA EXISTE EM QUADRO E NA FALA.

    ⭐ E' a lente mais importante deste motor, e ela nasce de uma medicao: em
    SETE dos quinze reels lidos nao ha' um unico terceiro em quadro, e SEIS
    deles prometem `getting filmed and laughed at by the people around her` na
    fala. Sem terceiro olhando isto e' acidente privado, nao vergonha publica —
    o beat mais caro da formula existe so' no audio.
    ⚠️ Corolario que a leitura entregou e que vale para o parque: bombeiro e
    socorrista sao testemunha de AUTORIDADE (o desastre e' grave o bastante
    para chamar o 911), nunca testemunha de VERGONHA. Sao dois papeis, e a
    fonte confunde os dois.
    """
    img = blocos.get(IMAGENS[0], "")
    # ⚠️ A lente le' a cena EFETIVA, nao o campo `test` cru: com o beat
    # `silencio` o quadro sai na variante MUDA (`test_q`), e uma lente colada
    # no campo cru reprovaria 100% dos videos certos dessa forma.
    if _cena_testemunha(spec)[0].lower() not in img.lower():
        ach.append(("ERRO", "RU1: %s sem as testemunhas em quadro — sem "
                            "terceiro olhando a humilhacao vira acidente "
                            "privado" % IMAGENS[0]))
    esperado = spec["testemunha"]["txt"] % _dic(spec)
    if esperado.lower() not in (spec["falas"][0] or "").lower():
        ach.append(("ERRO", "RU1: a fala do take 1 nao traz o beat da "
                            "testemunha — e' ele que faz a vergonha ser "
                            "PUBLICA"))


def _ru2_ruth(spec, blocos, ach):
    """⛔ RU2 — A RUTH, INTEIRA, NOS DOIS QUADROS DO REENCONTRO.

    Ela e' a assinatura da pagina e nao e' eixo. ⚠️ E os OCULOS estao aqui por
    medicao: o v49 a mostra SEM oculos nos dois quadros de fechamento enquanto
    o v46 e o v47 a mostram com aro dourado — mesma personagem fixa com
    acessorio inconstante. A leitura otica pediu literalmente que, se o angulo
    virasse motor, os oculos entrassem na string travada.
    ⛔ A lente cobra TRES PECAS e nao a string inteira: lente colada na forma
    da string acusa a si mesma na primeira reescrita — foi o que a BA1 do
    BANHO 3T pagou, reprovando 800 blocos corretos.
    """
    for nome in IMAGENS[1:]:
        baixo = blocos.get(nome, "").lower()
        for peca in RUTH_PROVAS:
            if peca not in baixo:
                ach.append(("ERRO", "RU2: %s sem %r — a Ruth e' a assinatura "
                                    "da pagina e nao e' eixo" % (nome, peca)))
    if RUTH_PROVAS[0] in blocos.get(IMAGENS[0], "").lower():
        ach.append(("ERRO", "RU2: a Ruth aparece no %s — ela so' entra no "
                            "reencontro, e po-la na humilhacao entregaria o "
                            "final no primeiro segundo" % IMAGENS[0]))


def _ru3_peca_ancora(spec, blocos, ach):
    """⭐⭐ RU3 — A MESMA PECA NOS TRES QUADROS, APERTADA E DEPOIS SOLTA.

    E' o achado do v46 e a unica coisa na fonte que resolve o problema central
    deste angulo: a mesma blusa floral esticada sobre o corpo obeso e caindo
    solta sobre o corpo magro e' ancora de continuidade E prova de
    emagrecimento no MESMO objeto.
    ⚠️ Onde a fonte nao tem ancora de roupa ela troca de pessoa
    escancaradamente (v27, v28, v38, v45) — e no v45 a roupa muda tres vezes
    dentro do proprio ato 1.
    """
    if spec["roupa"]["antes"].lower() not in blocos.get(IMAGENS[0], "").lower():
        ach.append(("ERRO", "RU3: %s sem a peca ancora esticada no corpo"
                    % IMAGENS[0]))
    for nome in IMAGENS[1:]:
        if spec["roupa"]["depois"].lower() not in blocos.get(nome, "").lower():
            ach.append(("ERRO", "RU3: %s sem a MESMA peca caindo solta — sem "
                                "ela o video promete a mesma pessoa e mostra "
                                "outra" % nome))
    # ⛔⛔ E A PECA FANTASMA, que e' o mecanismo central do angulo quebrando
    # por dentro. Defeito MEDIDO em 2026-08-21: o `porte` da pessoa e o `acao`
    # do desastre nomeavam OUTRA peca com artigo definido — *"wearing a heather
    # grey t-shirt [...] the DRESS stretched tight across her"*, *"soaked the
    # whole front of the SHIRT"* — e em alguns sorteios havia TRES pecas na
    # mesma pessoa dentro do mesmo bloco. 27 videos em 400 com `the dress`
    # fantasma e 63 com `the shirt`; LINT vazio em todos.
    # ⭐ A ancora e' de UMA peca so': duas pecas na mesma pessoa e' a mesma
    # classe de defeito que a fonte comete no v45 (a roupa muda tres vezes
    # dentro do ato 1), e e' justamente o que este eixo existe para impedir.
    resto = blocos.get(IMAGENS[0], "").replace(spec["roupa"]["antes"], "")
    if spec["pessoa"]["sexo"] == "casal":
        resto = resto.replace(spec["parceiro"]["antes"], "")
    m_ = _RX_PECA_FANTASMA.search(resto)
    if m_:
        ach.append(("ERRO", "RU3: %s nomeia %r fora do eixo ROUPAS — a peca "
                            "ancora e' UMA, e a segunda contradiz a primeira"
                    % (IMAGENS[0], m_.group(0))))


def _ru4_ancora_rosto(spec, blocos, ach):
    """⛔⛔ RU4 — O BLOCO 0 E' O ROSTO, E OS QUADROS O REPETEM POR EXTENSO.

    ⛔ A ancora so' cita traco que o PESO NAO MOVE. Maxilar, bochecha, papada e
    queixo mudam com trinta quilos: uma ancora que os cita obriga o gerador a
    escolher entre a ancora e a magreza do take 2, e ele escolhe contra nos.
    ⚠️ Com o rosto OCULTO no take 1 o que atravessa e' o CABELO e a PECA —
    exigir a ancora facial num quadro filmado de costas seria pedir olhos que
    nao existem em quadro, e contradicao o gerador resolve virando o rosto para
    a lente, o que mata o modo.
    """
    if not blocos.get("BLOCO 0 (REF)", "").lstrip().upper().startswith("REF"):
        ach.append(("ERRO", "RU4: BLOCO 0 sem o cabecalho REF — o AdBatch "
                            "descarta a referencia em silencio"))
    if spec["rosto"]["desc"] not in blocos.get("BLOCO 0 (REF)", ""):
        ach.append(("ERRO", "RU4: o BLOCO 0 nao descreve o rosto sorteado"))
    for nome in IMAGENS[1:]:
        if spec["rosto"]["desc"] not in blocos.get(nome, ""):
            ach.append(("ERRO", "RU4: %s sem a ancora de rosto por extenso — "
                                "e' o unico traco que atravessa a mudanca de "
                                "corpo" % nome))
    img1 = blocos.get(IMAGENS[0], "")
    if spec["rosto_oculto"]:
        if spec["rosto"]["cabelo"] not in img1:
            ach.append(("ERRO", "RU4: rosto OCULTO e a %s nao traz nem o "
                                "cabelo — sem ele nao sobra ancora nenhuma "
                                "no take 1" % IMAGENS[0]))
        if spec["rosto"]["desc"] in img1:
            ach.append(("ERRO", "RU4: rosto OCULTO e a %s descreve os olhos — "
                                "quadro filmado de costas com ancora facial e' "
                                "contradicao, e o gerador vira o rosto"
                        % IMAGENS[0]))
        # ⛔⛔ E A ANCORA NAO ERA O UNICO LUGAR ONDE O ROSTO APARECIA. Defeito
        # MEDIDO em 2026-08-21: a lente varria SO' `spec['rosto']['desc']` e o
        # `porte` da pessoa passava por baixo — *"turned away from the lens so
        # that only the back of the head is visible [...] She is flushed deep
        # red across the FACE and neck"*, *"breathing hard with the MOUTH
        # open"*, *"young in the FACE"*. 108 dos 593 videos de rosto oculto,
        # 9% de TODOS. O proprio docstring desta lente ja' dizia que a
        # contradicao mata o modo; ela e' que nao olhava para ela.
        # ⚠️ A varredura e' na SENTENCA DO PORTE e nao no bloco inteiro, e isso
        # e' desenho: as testemunhas dos nove desastres tem rosto em quadro de
        # proposito (*"a flat hand over her mouth"*, *"his mouth open"*), e
        # varrer o bloco reprovaria os nove.
        # ⛔⛔ E DESDE 2026-08-21 ELA VARRE O BLOCO DE CORPO MONTADO, nao o
        # campo `porte` sozinho. A arquitetura nova tem SEIS campos de corpo
        # (`porte`, `barriga`, `membros`, `pescoco`/`nuca`, `segundo` e a
        # clausula de orientacao), e varrer um deles seria a mesma cegueira que
        # a versao anterior tinha com o `porte` — cinco entradas novas por onde
        # o rosto voltaria sem ninguem ver.
        # ⚠️ O recorte continua sendo o CORPO e nao o bloco: as testemunhas dos
        # sessenta e dois desastres tem rosto em quadro de proposito (*"a flat
        # hand over her mouth"*), e varrer o bloco reprovaria os sessenta e
        # dois.
        # ⚠️ E O RECORTE COMECA NO `porte`, NAO NA ABERTURA DO BLOCO — falso
        # positivo MEDIDO na primeira versao desta ampliacao: a clausula de
        # cabelo `juntos_reta` diz *"hair pinned back off the face in a low
        # twist"*, e ela e' a ANCORA do rosto oculto, que o motor injeta de
        # proposito. A lente acusava 22 de 400 videos CERTOS. O que ela mede e'
        # a DESCRICAO DO CORPO (do elemento 1 ao 6); a ancora tem regra propria
        # tres linhas acima.
        _seg = _corpo_montado(img1)
        _i = _seg.find(spec["pessoa"]["porte"])
        m_ = _RX_ROSTO_NO_PORTE.search(_seg[_i:] if _i >= 0 else _seg)
        if m_:
            ach.append(("ERRO", "RU4: rosto OCULTO e o bloco de corpo cita "
                                "%r — a frase descreve o rosto que a camera "
                                "esta' de costas para" % m_.group(0)))
    elif spec["rosto"]["desc"] not in img1:
        ach.append(("ERRO", "RU4: rosto VISIVEL e a %s sem a ancora facial"
                    % IMAGENS[0]))


def _ru5_sem_aparelho(spec, blocos, ach):
    """⛔ RU5 — NENHUM APARELHO NA DIRECAO DE CENA.

    Aparelho escrito vira aparelho DESENHADO: o `vick16` dizia `with the phone
    in his free hand` e o gerador desenhou o telefone num lote inteiro.
    ⚠️ Aqui a tentacao e' especifica: a fala da fonte promete `getting filmed`
    em seis dos quinze reels. A saida NAO e' por celular em quadro — e' pelas
    testemunhas fazendo o que a imagem paga (olhar, virar a cabeca, apontar,
    rir), e a palavra `filmed` ficou fora do pool.

    ⛔⛔ ELA VARRE O BLOCO INTEIRO DESDE 2026-08-21, E ANTES NAO VARRIA. O corte
    era `re.sub(r"Dialogue:.*", "", txt, flags=re.S)`, e o `re.S` apagava do
    primeiro `Dialogue:` ATE' O FIM DO BLOCO — a FALA, a linha `Voice:` e a
    linha `Audio:` ficavam todas fora da lente. Medido plantando o mesmo
    aparelho em tres lugares do mesmo TAKE: antes do `Dialogue:` ACUSOU, na
    linha `Audio:` PASSOU, dentro da fala PASSOU. ⭐ E a fala e' justamente
    onde a palavra `filmed` da FONTE tentaria voltar — o cabecalho deste motor
    diz que ela *"SAI da copy"*, e a unica parte do bloco que a lente nunca
    lia era a copy. ⚠️ O controle negativo do autoteste tambem so' plantava
    antes do `Dialogue:`: ele provava metade da lente e imprimia OK.
    ⚠️ Medido antes de ligar: ZERO ocorrencia em 400 videos na cauda que estava
    cega — era buraco LATENTE, nao defeito vivo. Lente que ninguem sabe se
    funciona e' o mesmo risco.
    """
    for k, v in blocos.items():
        m = _RX_APARELHO.search(v or "")
        if m:
            ach.append(("ERRO", "RU5: %s nomeia %r — aparelho escrito vira "
                                "aparelho desenhado" % (k, m.group(0))))


def _ru6_coerencia(spec, blocos, ach):
    """⛔⛔ RU6 — OS PARES QUE EXISTEM NO MUNDO.

    Quatro acoplamentos, e nenhum deles e' gosto:
      · o desastre aceita aquele SEXO — homem em cadeira de pedicure nao e'
        variedade, e' ruido; casal sozinho na clinica idem;
      · a forma da TESTEMUNHA existe naquele quadro — `plateia` so' onde ha'
        sala cheia, `dedo` so' onde ha' vizinho;
      · a PECA serve aquele sexo — vestido no pool masculino e' entrada morta
        que o autoteste conta como viva (§35);
      · o ROSTO casa com o sexo.
    ⭐ Mesma mecanica do `certo`/`falso` do RARO 16: combinacao que nao existe
    no mundo nao e' variedade.
    """
    d, p = spec["desastre"], spec["pessoa"]
    if p["sexo"] not in d["sexos"]:
        ach.append(("ERRO", "RU6: pessoa %r (%s) num desastre que so' aceita "
                            "%s" % (p["id"], p["sexo"], list(d["sexos"]))))
    if spec["testemunha"]["forma"] not in d["formas"]:
        ach.append(("ERRO", "RU6: testemunha na forma %r num desastre que so' "
                            "comporta %s — o quadro nao paga a fala"
                    % (spec["testemunha"]["forma"], list(d["formas"]))))
    if p["sexo"] not in spec["roupa"]["sexos"]:
        ach.append(("ERRO", "RU6: peca %r nao serve %r"
                    % (spec["roupa"]["id"], p["sexo"])))
    esperado = "homem" if p["sexo"] == "homem" else "mulher"
    if spec["rosto"]["sexo"] != esperado:
        ach.append(("ERRO", "RU6: rosto %r num video de %r"
                    % (spec["rosto"]["sexo"], p["sexo"])))


def _ru7_nome(spec, blocos, ach):
    """⭐ RU7 — O NOME ATRAVESSA O VIDEO.

    E' o eixo mais barato do motor e o unico que a fonte realmente troca entre
    dois videos do mesmo roteiro (Betsy/Betty na mesma cadeira, Marjorie/
    Marilyn na mesma rampa). Se ele nao chega ao take 1, o eixo esta' morto e
    o painel promete uma troca que o video nao faz.
    ⚠️ No CASAL o nome e' o DELA e o alvo do remedio e' `them` — e' o que a
    fonte faz nos quatro reels de casal. Por isso o take 3 so' e' cobrado no
    singular nomeado.
    """
    nome = spec["pessoa"]["nome"]
    if not nome:
        return
    if nome not in spec["falas"][0]:
        ach.append(("ERRO", "RU7: o take 1 nao diz o nome %r — e' o unico take "
                            "que apresenta a pessoa" % nome))
    if spec["pessoa"]["sexo"] != "casal":
        if not any(nome in f for f in spec["falas"][1:]):
            ach.append(("ERRO", "RU7: o nome %r some depois do take 1 — no "
                                "singular ele e' o fio entre o antes e o "
                                "depois" % nome))


def _ru8_cta(spec, blocos, ach):
    """⛔ RU8 — O CTA, E O QUE ELE NAO PODE TER.

    ⛔ `yes` e' a palavra que a FONTE pede em praticamente todos os 60 posts, e
    ela quebra a nossa automacao de DM. `book` idem. ⛔ E `gelatin` nao existe
    nesta rota: e' emagrecimento, nao o mecanismo dos outros 32 motores.
    ⛔ E o follow ficou de fora da fala inteira, por FATO: *"a mensagem e'
    enviada independente de seguirem ou nao"* (operador, 2026-08-10). Os quinze
    reels fecham em `follow me first or I can't reach you`, que promete um
    portao que a nossa automacao nao tem.
    """
    f3 = spec["falas"][2] or ""
    lit = _cta_literal()
    if lit not in f3:
        ach.append(("ERRO", "RU8: a cena 3 sem o literal %r — a legenda do "
                            "video nasce do Whisper sobre o audio, e comando "
                            "variavel faz o modelo parafrasear a keyword"
                    % lit))
    corpo = " ".join(spec["falas"])
    for tok, motivo in BANIDOS_CTA.items():
        if re.search(r"\b%s\b" % tok, corpo, re.I):
            ach.append(("ERRO", "RU8: a fala usa %r — %s" % (tok, motivo)))
    if sc.FOLLOW_16.search(corpo):
        ach.append(("ERRO", "RU8: a fala pede FOLLOW — a DM sai para seguidor "
                            "e nao-seguidor igual, e prometer o contrario e' "
                            "mentira para o espectador"))


def _ru9_fala_no_take(spec, blocos, ach):
    """⛔ RU9 — A FALA CHEGA AO `Dialogue:` PALAVRA POR PALAVRA.

    ⭐ Ela e' tambem a substituta honesta da lente de painel para os eixos de
    COPY: em vez de perguntar se o rotulo em portugues aparece no prompt (nunca
    aparece — `%(ref)s` nao e' texto renderizado), pergunta se o EFEITO do eixo
    aparece, que e' a pergunta que a lente de painel queria fazer.
    """
    for i, (take, fala) in enumerate(zip(TAKES, spec["falas"]), 1):
        alvo = 'Dialogue: "%s"' % sonorizar(fala)
        if alvo not in blocos.get(take, ""):
            ach.append(("ERRO", "RU9: a fala %d nao chega intacta ao %s"
                        % (i, take)))


def _ru10_sem_gelatina(spec, blocos, ach):
    """⛔ RU10 — ESTA ROTA NAO USA GELATINA.

    A lente existe porque o parque inteiro fala em gelatina e a proxima copy
    colada de outro motor traria a palavra junto sem ninguem notar. Mesma
    guarda do RARO 16.
    """
    for k, v in blocos.items():
        if _RX_GELATINA.search(v):
            ach.append(("ERRO", "RU10: %s fala em gelatina — esta rota e' de "
                                "emagrecimento e fecha em `recipe`" % k))


def _ru11_pure_shame(spec, blocos, ach):
    """⭐ RU11 — `Pure shame.` FECHA O TAKE 1.

    Medido na fonte: fecha o ato 1 em 11 dos 15 reels, e e' o unico literal
    travado da fala alem da keyword. E' ele que nomeia o que o espectador
    acabou de sentir vendo a queda — sem ele o take 1 e' so' um acidente.
    """
    f1 = (spec["falas"][0] or "").strip()
    if not f1.endswith(FECHO_ATO1):
        ach.append(("ERRO", "RU11: o take 1 nao fecha em %r" % FECHO_ATO1))


def _ru12_orcamento(spec, blocos, ach):
    for i, fala in enumerate(spec["falas"], 1):
        n = _palavras(fala)
        if n > TETO_FALA[i]:
            ach.append(("ERRO", "RU12: cena %d com %d palavras (teto %d) — "
                                "fala cortada mata o CTA"
                        % (i, n, TETO_FALA[i])))
        elif n < PISO_FALA[i]:
            ach.append(("AVISO", "RU12: cena %d com %d palavras (piso %d)"
                        % (i, n, PISO_FALA[i])))


def _ru13_um_relogio(spec, blocos, ach):
    """⛔⛔ RU13 — UM RELOGIO SO' POR FALA.

    ⚠️ DEFEITO REAL, achado LENDO o take montado e nao por lente nenhuma: a
    virada trazia `eight months later` e o remedio trazia `after eight weeks
    of one simple remedy`, sorteados de pools independentes. A fala saia com
    DOIS prazos diferentes na mesma respiracao, e o espectador que ouve os dois
    para de acreditar em ambos.
    ⭐ E' o modo de falha do pool combinatorio: cada beat lido sozinho estava
    certo, e o PAR estava errado — o mesmo que o FIGHT 16 pagou com a falsa
    causa sem negacao. O conserto ficou no POOL (a duracao vive num beat so'),
    e a lente existe para o dia em que alguem devolver um prazo a outro pool.
    ⚠️ A fonte, alias, nunca da' prazo nenhum nos quinze reels.
    """
    for i, fala in enumerate(spec["falas"], 1):
        achados = {m.group(0).lower() for m in _RX_DURACAO.finditer(fala or "")}
        if len(achados) > 1:
            ach.append(("ERRO", "RU13: a cena %d traz dois prazos diferentes "
                                "(%s) — dois relogios na mesma respiracao e o "
                                "espectador para de acreditar nos dois"
                        % (i, ", ".join(sorted(achados)))))


def _ru14_um_corpo_so(spec, blocos, ach):
    """⛔⛔ RU14 — UMA PESSOA, UM SINTAGMA. O sujeito nao se reintroduz.

    ⚠️ DEFEITO MEDIDO em 1.200 sorteios (2026-08-21), e ele estava em 100% dos
    videos: o IMAGE 01 nomeava o corpo obeso DUAS a QUATRO vezes, cada vez com
    um sintagma definido novo — *"a very heavy 46-year-old woman [...] a very
    heavy grey-haired husband [...] they are both very heavy [...] the very
    heavy person who was pushing it"*. Quatro corpos nomeados para duas
    pessoas, e o campo `acao` ainda punha um QUINTO papel (`its occupant`, `the
    very heavy customer`) que e' gente diferente na leitura de quem gera.
    ⭐ Um bloco que nomeia N corpos e' licenca para desenhar N corpos, e isto
    e' uma cena de queda com plateia — o pior lugar do parque para dar essa
    licenca (a propria clausula `ANATOMIA` existe porque o gerador inventa
    membro aqui).
    ⚠️ O teto e' 1 no singular e 2 no casal (ela + o marido), e nao um numero
    escrito a mao: e' quantas PESSOAS o video declara. O `porte` e o `acao`
    passaram a falar por PRONOME.

    ⛔⛔ ELA FOI REESCRITA EM 2026-08-21 PARA SABER A DIFERENCA ENTRE
    REINTRODUZIR UM CORPO E DESCREVER O CORPO QUE JA' EXISTE. A primeira
    versao contava o LITERAL `very heavy` e por isso mediu *"1200 -> 0"*
    quando eu enxuguei os catorze `porte` — e foi esse conserto que produziu o
    lote que o operador reprovou olhando (*"nao esta' gerando personagens
    obesos"*). Contar adjetivo empurra a solucao para o lado errado: para
    passar na lente antiga bastava tirar peso da descricao.
    ⭐ O defeito real nunca foi o adjetivo, foi o SINTAGMA DE PESSOA NOVO —
    `a very heavy woman [...] the very heavy CUSTOMER` sao dois substantivos
    de gente e o gerador desenha dois corpos. A lente conta agora
    `heavy` + ate' quatro modificadores + um SUBSTANTIVO DE PESSOA, que e'
    exatamente essa construcao. Cento e quarenta palavras descrevendo UMA
    barriga nao casam com ela nem uma vez, e a reintroducao de verdade casa
    sempre — os dois controles negativos provam os dois lados.
    """
    n = len(_RX_CORPO_NOMEADO.findall(blocos.get(IMAGENS[0], "")))
    teto = 2 if spec["pessoa"]["sexo"] == "casal" else 1
    if n > teto:
        ach.append(("ERRO", "RU14: %s nomeia o corpo %d vezes (teto %d) — "
                            "sujeito reintroduzido com sintagma novo e' "
                            "licenca para desenhar mais um"
                    % (IMAGENS[0], n, teto)))


def _ru15_geometria_casal(spec, blocos, ach):
    """⛔⛔ RU15 — NO CASAL, QUEM COLOCA OS DOIS NO ESPACO E' O `acao`.

    ⚠️ DEFEITO MEDIDO em 253 de 1.200 videos (21,1%): a frase de elenco dizia
    `and beside her a very heavy husband` e tres palavras depois o `acao` os
    punha em lugares diferentes — *"one sitting back on the broken step [...]
    and the other flat on the driveway below"*, *"tangled together and pointing
    in opposite directions"*. Duas geometrias incompativeis no mesmo bloco, e
    contradicao o gerador resolve escolhendo uma, que nao e' a nossa.
    ⭐ `with her` declara que estao JUNTOS na cena sem fixar posicao relativa;
    quem sabe onde eles cairam e' o unico campo que descreve a queda.
    """
    if spec["pessoa"]["sexo"] != "casal":
        return
    if "and beside her" in blocos.get(IMAGENS[0], ""):
        ach.append(("ERRO", "RU15: %s fixa a posicao do casal antes de o "
                            "`acao` os colocar — duas geometrias no mesmo "
                            "bloco" % IMAGENS[0]))


def _ru16_silencio_no_quadro(spec, blocos, ach):
    """⛔⛔ RU16 — `silencio` NA FALA EXIGE SILENCIO NO QUADRO.

    ⚠️ DEFEITO MEDIDO: a forma `silencio` so' existe em dois desastres e os
    DOIS tinham riso escrito no `test`, no `mov` e num deles no `audio`. Em 400
    sorteios, **21 de 21** videos dessa forma saiam com a fala dizendo *"and
    nobody said a word"* sobre gente rindo em quadro e sobre um audio de
    risada. Fala que desmente o proprio quadro e' o defeito que a leitura otica
    achou em seis dos quinze reels da fonte, invertido — e este motor nasceu
    para nao te-lo.
    ⭐ O conserto e' a variante MUDA do quadro (`test_q`/`mov_q`/`audio_q`), e
    esta lente e' quem cobra que ela exista e chegue ao bloco.
    """
    if spec.get("testemunha", {}).get("forma") != "silencio":
        return
    for nome in (IMAGENS[0], TAKES[0]):
        if re.search(r"\blaugh(s|ing|ed)?\b", blocos.get(nome, ""), re.I):
            ach.append(("ERRO", "RU16: a fala diz SILENCIO e o %s tem gente "
                                "rindo — o quadro desmente a fala" % nome))


def _ru17_pronome_do_vizinho(spec, blocos, ach):
    """⛔⛔ RU17 — A DIRECAO DE CENA CONCORDA COM O ELENCO.

    ⚠️ DEFEITO MEDIDO em 400 sorteios (2026-08-21): `the person beside her has
    turned HER head` estava CRAVADO no feminino singular e saia em 400 de 400
    blocos — nos 57 videos de HOMEM o mesmo bloco dizia `man` e `her head`, e
    nos 126 de CASAL havia DUAS pessoas ao lado da Ruth e a frase dirigia UMA,
    deixando o marido sem instrucao nenhuma. 183 de 400 (46%) com o bloco
    contradizendo a si mesmo, LINT vazio em todos.
    ⭐ O motor ja' tinha `poss`/`obj_pron`/`suj` em `PESSOAS` para isso; a
    direcao de cena e' que nao os consumia. A lente cobra o EFEITO: nenhum
    pronome que o ramo de sexo desminta sobrevive ao bloco.
    """
    p = spec["pessoa"]
    for nome in (IMAGENS[2], TAKES[1], TAKES[2]):
        txt = blocos.get(nome, "")
        if p["sexo"] == "casal":
            if "the person beside her" in txt:
                ach.append(("ERRO", "RU17: %s fala de UMA pessoa ao lado da "
                                    "Ruth e o quadro tem duas" % nome))
        else:
            if "the two beside her" in txt:
                ach.append(("ERRO", "RU17: %s fala de DUAS pessoas ao lado da "
                                    "Ruth num video de uma so'" % nome))
            errado = "his" if p["poss"] == "her" else "her"
            if "has turned %s head" % errado in txt:
                ach.append(("ERRO", "RU17: %s diz `turned %s head` num video "
                                    "de %r" % (nome, errado, p["sexo"])))


def _ru18_ingrediente_nas_tres(spec, blocos, ach):
    """⛔⛔ RU18 — O CT5 VALE PARA AS TRES FALAS, E O CONTRATO SO' LE' DUAS.

    ⚠️ DEFEITO DE ARQUITETURA, medido em 2026-08-21: `short_comum.lint_copy16`
    faz `f1, f2 = falas[0], falas[-1]`. Com TRES falas, `falas[1]` NUNCA e'
    lida por CT1/CT3/CT5/CT6/CT7 — e a cena 2 e' exatamente onde mora o beat do
    REMEDIO, que e' o unico lugar do motor onde alguem escreveria um
    ingrediente. Prova: a MESMA sentenca (*"after one spoon of apple cider
    vinegar and lemon every morning"*) plantada na cena 3 acusa CT5 e plantada
    na cena 2 passa.
    ⭐ Os pools estao limpos e o autoteste ja' os varre entrada por entrada; o
    buraco e' na lente POR VIDEO — que e' a que o operador ve' quando edita a
    copy a' mao no painel ou aperta `trocar`. Pool limpo nao protege copy
    editada na tela.
    ⛔ E a receita e' a UNICA moeda que o comentario compra: entregue uma vez,
    esta' gasta para todos os videos da pagina.
    """
    for i, fala in enumerate(spec["falas"], 1):
        alvo = sc.ingrediente_na_fala(fala)
        if alvo:
            ach.append(("ERRO", "RU18: a fala %d entrega o ingrediente %r — a "
                                "receita e' a moeda, e ela so' se paga uma vez"
                        % (i, alvo)))


def _ru19_so_a_ancora_no_corpo(spec, blocos, ach):
    """⭐⭐ RU19 — NENHUMA SEGUNDA PECA NO CORPO DE QUEM O VIDEO APRESENTA.

    ⛔⛔ DEFEITO MEDIDO NO BLOCO MONTADO (2026-08-21), e ele matava o mecanismo
    central do angulo. A IMAGE 01 da `avental_costas` dizia, no MESMO
    paragrafo:
        *"... wearing a cream blouse printed with large flowers, stretched
          tight across the back ..."*   <- a peca-ancora, injetada pelo motor
        *"The body has come out of the cubicle in a pale blue paper gown ..."*
                                        <- o `acao` da entrada
    O gerador escolhe UMA. Se escolher o avental, o take 2 (*"the same cream
    blouse, now hanging loose"*) fica sem referente e a continuidade do angulo
    morre naquele video — e a continuidade AQUI e' a peca de roupa, nao o
    rosto (achado do v46). ⚠️ A `RU3` nao pegava: ela cobra a peca-ancora
    PRESENTE e a peca fantasma com artigo DEFINIDO (`the dress`); um avental
    com artigo indefinido passava pelas duas.

    ⛔⛔ E ELA DISTINGUE TRES DONOS, porque lente que reprova o certo e' lente
    quebrada. A varredura mediu 55 pares (desastre x peca) no IMAGE 01 montado
    e SO' UM era defeito:
      · NO CORPO DELA .. `the body ... in a pale blue paper gown`  -> ERRO
      · EM TERCEIRO ... `six patients in paper gowns` (tomografo_estreito),
        `a warehouse worker in a hi-vis vest`, `two orderlies in navy scrubs`
        -> passa, porque a passagem de dono (`while`, `with`, o proprio
        substantivo de pessoa antes do `in`) corta a frase antes da peca
      · EM MOVEL ..... `a chrome return rack hung with dresses and jeans`
        (provador_loja), `a dress on its hanger held up against the front`,
        `folded shirts spread around them` -> passa, pelo mesmo corte
    ⚠️ `tomografo_estreito` e `provador_loja` sao os dois controles POSITIVOS
    desta lente: os dois foram acusados por um revisor humano e os dois estao
    CERTOS. Se algum dia ela reprovar um deles, o defeito e' dela.
    ⛔ E `clothes`/`clothing` nao entram na lista: *"still in its own street
    clothes"* e' justamente o jeito de nao despir alguem sem escrever a
    declaracao de conformidade que o repo baniu em 2026-07-31.
    """
    txt = blocos.get(IMAGENS[0], "").replace(spec["roupa"]["antes"], " ")
    if spec["pessoa"]["sexo"] == "casal":
        # ⚠️ O PARCEIRO E' UM SEGUNDO CORPO LEGITIMO e tem peca propria do
        # mesmo eixo `ROUPAS` — sem tira-la daqui a lente acusaria todo casal.
        txt = txt.replace(spec["parceiro"]["antes"], " ")
    for frase in txt.split(". "):
        for m_ in _RX_VESTIR_NO_ALVO.finditer(frase):
            ach.append(("ERRO", "RU19: %s veste %r em quem o video apresenta — "
                                "a peca-ancora e' a UNICA no corpo dela, e com "
                                "duas o gerador escolhe uma e o take 2 fica "
                                "sem referente"
                        % (IMAGENS[0], m_.group("peca"))))
        for m_ in _RX_VESTIDO_SOBRE.finditer(frase):
            ach.append(("ERRO", "RU19: %s poe %r SOBRE o corpo (a peca e' o "
                                "sujeito da frase) — a peca-ancora e' a UNICA"
                        % (IMAGENS[0], m_.group("peca"))))


def _ru20_corpo_obeso(spec, blocos, ach):
    """⭐⭐ RU20 — O CORPO DO TAKE 1 TRAZ NUMERO, AREA DE QUADRO E COMPARACAO.

    ⛔⛔ ESTA E' A LENTE QUE IMPEDE A REGRESSAO DE VOLTAR, e ela nasce do unico
    tipo de evidencia que vale: o operador gerou um lote, olhou o mp4 e
    reprovou — *"nao esta' gerando personagens obesos, inclusive alguns parecem
    ate' magros"*. O bloco que produziu aquilo dizia, inteiro:
        *"a very heavy 39-year-old white American woman [...] and with her a
          very heavy husband in a black t-shirt. They are both wide through the
          middle."*
    Catorze palavras, todas ADJETIVO, e o LINT saiu VAZIO em 400 de 400 videos:
    nenhuma das dezenove lentes olhava para o tamanho do corpo.

    ⭐ O gerador nao desenha adjetivo. Ele desenha:
      (i)   um NUMERO de peso com um referente de escala;
      (ii)  uma POSICAO NO QUADRO — quanto do frame o corpo ocupa;
      (iii) uma COMPARACAO — contra o proprio corpo ou contra uma coisa do
            mundo.
    Sem os tres ele volta para a media do treino, que e' uma pessoa comum. Foi
    exatamente o que voltou.

    ⛔ ELA MEDE A SAIDA MONTADA, NAO O POOL. Pool novo entra sem passar por
    sorteio, e o defeito de 2026-08-21 nasceu justamente de um campo de pool
    que passava em todas as lentes de campo. ⚠️ E o recorte e' o BLOCO DE
    CORPO, nao a IMAGE 01 inteira: `cen`, `acao` e `test` tambem falam em
    `frame` e em `wider than`, e uma lente que passasse por causa da legenda da
    camera estaria passando pelo motivo errado — que e' a definicao de lente
    cega (§ a lapide do `_sem_dialogo`).
    """
    img1 = blocos.get(IMAGENS[0], "")
    seg = _corpo_montado(img1)
    if not seg:
        ach.append(("ERRO", "RU20: %s sem o bloco de corpo delimitado (falta "
                            "%r ou %r) — sem ele nao ha' o que medir, e o "
                            "corpo sai na media do treino"
                    % (IMAGENS[0], MARCA_CORPO, SUPORTE_FIM)))
        return
    if not _RX_PESO_LIBRAS.search(seg):
        ach.append(("ERRO", "RU20: o corpo do %s nao traz NUMERO DE PESO — "
                            "adjetivo de porte o gerador ignora, e o lote de "
                            "2026-08-21 voltou com gente comum" % IMAGENS[0]))
    if not _RX_POSICAO_QUADRO.search(seg):
        ach.append(("ERRO", "RU20: o corpo do %s nao diz QUANTO DO QUADRO ele "
                            "ocupa — area de pixel nao declarada e' area de "
                            "pixel da media do treino" % IMAGENS[0]))
    if not _RX_COMPARACAO.search(seg):
        ach.append(("ERRO", "RU20: o corpo do %s nao traz COMPARACAO — sem um "
                            "`thicker than` ou um `as heavy as` sobra so' "
                            "adjetivo, que nao desenha nada" % IMAGENS[0]))


# ⛔⛔ UMA TRAVA DO CONTRATO DE 16s DESLIGADA, COM A ORDEM E O MOTIVO ESCRITOS.
# Regra que nasce desligada sem razao escrita e' regra que alguem religa amanha
# sem saber o que quebra.
# ---------------------------------------------------------------------------
# CT2 — *"o take 1 enuncia a FALHA dele, com dano concreto"*. ⛔ Este angulo
#   NAO e' de disfuncao eretil: e' EMAGRECIMENTO, e a falha nao e' um verbo, e'
#   um CORPO — a cadeira que racha, a rampa que vence o marido, o guindaste na
#   sala. O regex do CT2 procura `soft`, `stopped`, `quit`, `never works`, que
#   sao verbos de disfuncao masculina, e ele acusaria a maioria dos sorteios em
#   cima de copy que enuncia a falha melhor do que qualquer entrada da lista.
#   ⭐ O que o CT2 protege (o espectador se reconhecer) e' cobrado aqui pela
#   RU1 e pela RU11: o dano esta' em quadro, tem testemunha e tem nome.
# ⚠️ As outras seis travas valem INTEIRAS: CT1 (nada depois do CTA), CT3 (nao
#   ha' `gelatin trick` nesta rota), CT5 (nenhum ingrediente na fala), CT6 (o
#   CTA diz onde a receita chega), CT7 (nao ha' orgao nomeado) e CT8 (nenhum
#   follow na fala — e a fonte pede follow em 15 de 15).
# ⚠️ CT4 e CT4b nao se aplicam por CONSTRUCAO, nao por excecao: `NUCLEO` e'
#   vazio porque este angulo nao nomeia orgao nenhum. Excecao que nao suprime
#   nada e' ruido, e ruido ensina a desconfiar das que suprimem de verdade.
_CT_DESLIGADOS = ("CT2:",)


def lint(spec, blocos):
    ach = []
    falas = spec["falas"]
    sc.lint_tags(blocos, ach)
    sc.lint_sem_texto(blocos, ach)
    sc.lint_anticeleb(blocos, ach)
    sc.lint_take_vs_image(blocos, ach)
    sc.lint_painel_honesto(sys.modules[__name__], spec, blocos, ach)
    sc.lint_isca_cta(falas[2], ach, "a cena 3 (CTA)")
    # ⛔ `isca_absurda=False`: este angulo nao tem substancia absurda nenhuma —
    # o take 1 e' a queda de verdade, nao uma promessa que o video desmente.
    _ct = []
    sc.lint_copy16(sys.modules[__name__], spec, _ct, isca_absurda=False)
    ach.extend(x for x in _ct if not x[1].startswith(_CT_DESLIGADOS))
    for f in (_ru1_testemunha, _ru2_ruth, _ru3_peca_ancora, _ru4_ancora_rosto,
              _ru5_sem_aparelho, _ru6_coerencia, _ru7_nome, _ru8_cta,
              _ru9_fala_no_take, _ru10_sem_gelatina, _ru11_pure_shame,
              _ru12_orcamento, _ru13_um_relogio, _ru14_um_corpo_so,
              _ru15_geometria_casal, _ru16_silencio_no_quadro,
              _ru17_pronome_do_vizinho, _ru18_ingrediente_nas_tres,
              _ru19_so_a_ancora_no_corpo, _ru20_corpo_obeso):
        f(spec, blocos, ach)
    return ach


# ===========================================================================
# PAINEL
# ===========================================================================
EIXOS_UI = [
    ("desastre", "O DESASTRE", "DESASTRES", "curto"),
    ("pessoa", "A PESSOA", "PESSOAS", "curto"),
    ("reencontro", "O REENCONTRO", "REENCONTROS", "curto"),
    ("roupa", "A PECA ANCORA", "ROUPAS", "curto"),
    ("rosto", "O ROSTO (REF)", "ROSTOS", "curto"),
    ("testemunha", "A TESTEMUNHA", "BEATS_TESTEMUNHA", "curto"),
]
EIXOS_TRAVAVEIS = ["desastre", "pessoa", "reencontro", "roupa", "rosto",
                   "testemunha"]

# ⭐⭐ AS DUAS PRE-SELECOES. `sexo` e' operacional (o operador roda um lote de
# casal, outro de mulher sozinha); `rosto_ato1` E' O EXPERIMENTO — a fonte
# esconde o rosto em 6 de 15 e mostra nos outros 9, e o unico reel com
# testemunha de verdade em foco e' justamente um dos que MOSTRAM. Quinze pontos
# nao separam; quinze videos de cada lado separam.
TRAVAS_UI = [("sexo", "o alvo", ["livre"] + list(SEXOS)),
             ("rosto_ato1", "rosto no ato 1", ["livre", "oculto", "visivel"])]

DROPDOWNS_UI = [("rosto", "O ROSTO (REF)", "ROSTOS", "curto"),
                ("desastre", "O DESASTRE", "DESASTRES", "curto")]

# ⚠️ `testemunha` fica FORA da lente de honestidade e NAO fica sem guarda: o
# valor dela e' um molde com slot (`%(obj)s`), que nunca aparece literal em
# bloco nenhum — a lente acusaria 400 de 400 videos certos. Quem a cobra e' a
# RU1, e ela cobra MAIS: o beat renderizado dentro da fala E as testemunhas
# dentro da IMAGE.
#
# ⛔⛔ E ESTA EXCECAO CERTA ESCONDEU UM EIXO MORTO POR UM DIA INTEIRO, o que e'
# a licao mais cara da varredura de 2026-08-21. A razao acima esta' certa — a
# lente de painel HONESTAMENTE nao serve para um eixo cujo valor e' molde. Mas
# desligar a unica lente que olhava para o eixo deixou passar que
# `travas["testemunha"]` NUNCA era lida em `sortear`: o cadeado era honrado em
# 23 de 200 sorteios (11%, o acaso de 1 em 13 formas cabiveis) e a escolha do
# operador no botao `trocar` sobrevivia em 4 de 120 cliques (3%).
# ⭐ A REGRA QUE FICA: **excecao certa que deixa um buraco pede lente NOVA, nao
# lente removida.** Aqui a lente nova e' a medicao de cadeado e de `trocar` no
# autoteste, eixo por eixo, contra um piso — ela nao pergunta se o rotulo
# aparece no prompt, pergunta se o VALOR ESCOLHIDO sobrevive.
IGNORA_PAINEL = ("testemunha",)


def _refazer_falas(spec, rng):
    """⛔⛔ Os eixos que MEXEM NA COPY avisam a UI, senao o painel mente.

    ⚠️ DEFEITO REAL, filmado pelo operador no BANHO 16 3T: ele clicava em
    `trocar` na linha da copy e o painel trocava o ROTULO sem trocar as falas.
    A lente acusava a cada clique legitimo — e lente que acusa a cada clique
    treina o operador a ignorar a barra. O conserto e' aqui, nao na lente.
    ⛔ Aqui sao QUATRO os eixos que mexem na fala, e tres deles nao sao de
    copy: a PESSOA carrega os pronomes e o nome, o DESASTRE carrega o beat do
    take 1 e decide quais testemunhas cabem, e a TESTEMUNHA e' o beat.
    """
    spec["falas"] = [v for _, v in sorted(_falas(spec, rng).items())]


def _coerir_cena(spec, rng, tocado=None):
    """⛔⛔ REPARA OS ACOPLAMENTOS depois de uma troca de eixo no painel.

    ⚠️ DEFEITO MEDIDO no BANHO 16 3T, simulando o painel: clicar em `trocar` no
    eixo do banheiro deixava 34 de 40 videos invalidos, porque os dois eixos
    eram acoplados e a UI compartilhada nao tem como saber do acoplamento.
    ⭐ O autoteste passava em 400 sorteios e nunca via: SORTEAR e' so' metade
    do que o operador faz. O que ele faz depois — trocar eixo, travar,
    re-sortear cena — nao era exercitado por lente nenhuma.
    """
    # ⛔⛔ QUEM CEDE E' O MUNDO EM VOLTA, NUNCA O EIXO QUE O OPERADOR ACABOU DE
    # TROCAR — e ate' 2026-08-21 nao era assim: `_coerir_cena` reparava sempre
    # na MESMA ordem e o eixo clicado era justamente o primeiro a ceder.
    # Medido em 120 cliques por eixo: a escolha do operador sobrevivia em 3%
    # na testemunha e em 56% na pessoa. Botao que devolve outra coisa e' pior
    # que botao ausente.
    # ⭐ `tocado` chega por CLOSURE em `EIXOS_QUE_MEXEM_NA_COPY`, sem mexer na
    # assinatura que a UI compartilhada chama (`fn(spec, rng)`) — mudar o
    # contrato da UI por causa de um motor e' o caminho para quebrar os outros
    # quarenta e tres.
    p = spec["pessoa"]
    if tocado == "rosto":
        alvo_r = "homem" if spec["rosto"]["sexo"] == "homem" else "mulher"
        if (p["sexo"] == "homem") != (alvo_r == "homem"):
            cabem = [x for x in PESSOAS
                     if (x["sexo"] == "homem") == (alvo_r == "homem")]
            if cabem:
                spec["pessoa"] = p = rng.choice(cabem)
                spec["idade"] = p["idade"]
    if tocado == "roupa" and p["sexo"] not in spec["roupa"]["sexos"]:
        cabem = [x for x in PESSOAS if x["sexo"] in spec["roupa"]["sexos"]]
        if cabem:
            spec["pessoa"] = p = rng.choice(cabem)
            spec["idade"] = p["idade"]

    d = spec["desastre"]
    if tocado != "desastre":
        if p["sexo"] not in d["sexos"]:
            cabem = [x for x in DESASTRES if p["sexo"] in x["sexos"]]
            if cabem:
                spec["desastre"] = d = rng.choice(cabem)
        t_ = spec.get("testemunha")
        # ⚠️ Aqui o desastre cede por DUAS razoes, e a segunda e' orcamento:
        # uma testemunha de 9 palavras nao cabe ao lado de um beat de desastre
        # de 13 nem com a menor abertura do pool, e insistir devolvia uma cena
        # 1 de 28 palavras — fala cortada, que e' o defeito que o teto existe
        # para impedir.
        if tocado == "testemunha" and t_:
            d0 = _dic(spec)
            n_t = _palavras(_r(t_["txt"], d0))
            menor_ab = min(_palavras(_r(a["txt"], d0)) for a in ABERTURAS)

            def _serve(x, sexo_):
                return (t_["forma"] in x["formas"]
                        and sexo_ in x["sexos"]
                        and (_palavras(_r(x["fala"], d0)) + n_t + menor_ab
                             + _palavras(FECHO_ATO1)) <= TETO_FALA[1])

            if not _serve(d, p["sexo"]):
                cabem = [x for x in DESASTRES if _serve(x, p["sexo"])]
                if cabem:
                    spec["desastre"] = d = rng.choice(cabem)
                else:
                    # ⚠️ E A PESSOA CEDE JUNTO. Medido: em 28 de 120 cliques a
                    # forma escolhida nao existia em desastre NENHUM que
                    # comportasse o sexo da pessoa atual (a `plateia` so' mora
                    # em ambiente fechado, e nenhum dos tres aceita casal).
                    # Manter a pessoa ali era devolver ao operador uma
                    # testemunha que ele nao escolheu — e o eixo tocado e' o
                    # que manda.
                    outros = [(x, s_) for x in DESASTRES for s_ in x["sexos"]
                              if _serve(x, s_)
                              and [y for y in PESSOAS if y["sexo"] == s_]]
                    if outros:
                        x, s_ = rng.choice(outros)
                        spec["desastre"] = d = x
                        spec["pessoa"] = p = rng.choice(
                            [y for y in PESSOAS if y["sexo"] == s_])
                        spec["idade"] = p["idade"]

    if p["sexo"] not in d["sexos"]:
        cabem = [x for x in PESSOAS if x["sexo"] in d["sexos"]]
        if cabem:
            spec["pessoa"] = p = rng.choice(cabem)
            spec["idade"] = p["idade"]
    if p["sexo"] not in spec["roupa"]["sexos"]:
        cabem = [x for x in ROUPAS if p["sexo"] in x["sexos"]]
        if cabem:
            spec["roupa"] = rng.choice(cabem)
    alvo = "homem" if p["sexo"] == "homem" else "mulher"
    if spec["rosto"]["sexo"] != alvo:
        spec["rosto"] = rng.choice([x for x in ROSTOS if x["sexo"] == alvo])
    # ⛔⛔ A TESTEMUNHA ESCOLHIDA NO PAINEL SOBREVIVE AO RE-SORTEIO DA COPY, e
    # ate' 2026-08-21 nao sobrevivia: `_refazer_falas` chama `_falas`, que
    # re-sorteava a testemunha do zero e jogava fora a que o operador tinha
    # acabado de escolher. Medido simulando `ui_agente.trocar_eixo`: o valor
    # escolhido sobrevivia em 4 de 120 cliques (3%, que e' o acaso). ⭐ O
    # conserto e' o CADEADO, nao a lente: `trava_testemunha` entra no spec e o
    # sorteio da copy a respeita.
    # ⚠️ Quando a forma dela nao cabe no desastre novo, ela CEDE e o cadeado
    # cede junto — acoplamento e' fato do mundo, e a lente RU6 o cobra.
    if not _beat_cabe(spec.get("testemunha", {"forma": None, "txt": ""}), d):
        cabem = [x for x in BEATS_TESTEMUNHA if _beat_cabe(x, d)]
        if cabem:
            spec["testemunha"] = rng.choice(cabem)
    # ⚠️ O cadeado e' RESTAURADO depois: pinar para sempre transformaria uma
    # troca de `desastre` num cadeado permanente que o operador nunca pediu, e
    # o botao `trocar` da CENA 1 passaria a devolver sempre a mesma testemunha.
    antes = spec.get("trava_testemunha")
    spec["trava_testemunha"] = spec.get("testemunha")
    _refazer_falas(spec, rng)
    spec["trava_testemunha"] = antes


def _coerir(eixo):
    """Fecha o nome do eixo tocado dentro da assinatura que a UI chama."""
    return lambda spec, rng: _coerir_cena(spec, rng, eixo)


EIXOS_QUE_MEXEM_NA_COPY = {"desastre": _coerir("desastre"),
                           "pessoa": _coerir("pessoa"),
                           "roupa": _coerir("roupa"),
                           "rosto": _coerir("rosto"),
                           "testemunha": _coerir("testemunha")}


def resumo_pt(spec):
    p = spec["pessoa"]
    return ("24s, TRES takes de 8s. Take 1 — A HUMILHACAO: %s (%s), com %s em "
            "quadro e o rosto %s. Take 2 — O REENCONTRO: %s, ela magra na "
            "MESMA %s caindo solta, ao lado da Ruth. Take 3 — A RECEITA: "
            "fecha em `%s`. Pessoa: %s, %d anos. Rosto (REF): %s. Copy: "
            "abertura %s (%s) · testemunha %s (%s) · prova %s (%s). "
            "Rota de EMAGRECIMENTO, sem gelatina."
            % (spec["desastre"]["curto"], spec["desastre"]["v"],
               "TESTEMUNHA", "OCULTO" if spec["rosto_oculto"] else "VISIVEL",
               spec["reencontro"]["curto"], spec["roupa"]["curto"],
               _cta_literal(), p["curto"], p["idade"], spec["rosto"]["curto"],
               spec["abertura"]["curto"], spec["abertura"]["forma"],
               spec["testemunha"]["curto"], spec["testemunha"]["forma"],
               spec["prova"]["curto"], spec["prova"]["forma"]))


# ===========================================================================
# AUTOTESTE
# ===========================================================================

def autoteste(n=400):
    pags = sorted(ETNIA)
    erros = collections.Counter()
    eixos = collections.defaultdict(set)
    dist = collections.defaultdict(set)
    tam = collections.defaultdict(list)
    specs, falhas, avisos = [], [], 0

    for i in range(n):
        s = sortear(pags[i % len(pags)], random.Random(i), {})
        b = montar(s)
        specs.append(s)
        for e in ("desastre", "pessoa", "reencontro", "roupa", "rosto",
                  "parceiro", "abertura", "testemunha", "virada", "remedio",
                  "prova", "selo", "cta"):
            eixos[e].add(s[e]["id"])
        eixos["rosto_oculto"].add(s["rosto_oculto"])
        for c, f in enumerate(s["falas"], 1):
            dist[c].add(f)
            tam[c].append(_palavras(f))
        for nivel, msg in lint(s, b):
            if nivel == "ERRO":
                erros[msg[:72]] += 1
            else:
                avisos += 1

    print("RUTH 16 — %d sorteios, 5 paginas" % n)
    for c in sorted(dist):
        v = sorted(tam[c])
        pior = v[-1]
        print("  cena %d: %3d falas distintas · palavras min/med/max "
              "%d/%d/%d (teto %d) · no pior caso %.1fs num take de %.0fs"
              % (c, len(dist[c]), v[0], v[len(v) // 2], v[-1], TETO_FALA[c],
                 pior / TAXA_MEDIA, SEGUNDOS_TAKE))
    # ⛔⛔ O EIXO `desastre` E' MEDIDO EM 2.000 SORTEIOS, NAO NAS 400 SEEDS —
    # e isto e' conserto de um FALSO POSITIVO MEDIDO em 2026-08-21, no dia em
    # que o pool passou de 52 para 62 entradas. Com 400 seeds a media por
    # entrada e' 6,5, e a chance de UMA das 62 nao aparecer por puro acaso e'
    # ~9%: o autoteste acusava `balanco_varanda` de estar MORTA (§35) sobre uma
    # entrada que sai 22 vezes em 2.000 sorteios. ⚠️ Lente que reprova o que
    # esta' certo treina o operador a ignorar a barra inteira (§16), e o preco
    # de aumentar a amostra e' zero: os mesmos 2.000 sorteios ja' eram feitos
    # mais abaixo, para o ALCANCE POR DESASTRE. ⭐ As 400 seeds continuam sendo
    # a REGRESSAO de todo o resto — o que mudou de amostra foi so' a pergunta
    # *"esta entrada existe no sorteio?"*, que e' a unica cujo poder
    # estatistico depende do TAMANHO do pool.
    N_ALC = 2000
    cont_d = collections.Counter()
    cont_cl = collections.Counter()
    for i in range(N_ALC):
        sp_alc = sortear(pags[i % len(pags)], random.Random(80000 + i), {})
        cont_d[sp_alc["desastre"]["id"]] += 1
        cont_cl[sp_alc["desastre"].get("cluster", "LIDO (leitura otica)")] += 1
        eixos["desastre"].add(sp_alc["desastre"]["id"])

    for e, pool in (("desastre", DESASTRES), ("pessoa", PESSOAS),
                    ("reencontro", REENCONTROS), ("roupa", ROUPAS),
                    ("rosto", ROSTOS), ("parceiro", PARCEIROS),
                    ("abertura", ABERTURAS), ("testemunha", BEATS_TESTEMUNHA),
                    ("virada", VIRADAS), ("remedio", REMEDIOS),
                    ("prova", PROVAS), ("selo", SELOS), ("cta", CTAS)):
        print("  %-11s %2d de %2d alcancados" % (e, len(eixos[e]), len(pool)))
        # ⚠️ O piso e' o TAMANHO DO POOL, lido do proprio pool — numero cravado
        # a mao vira falso alarme no dia em que uma entrada sai.
        if len(eixos[e]) < len(pool):
            mortas = sorted({x["id"] for x in pool} - eixos[e])
            falhas.append("EIXO %s: %d de %d em %d sorteios — entrada que nao "
                          "sai esta' MORTA e o autoteste a conta como viva "
                          "(§35): %s" % (e, len(eixos[e]), len(pool), n,
                                         mortas[:6]))
    if len(eixos["rosto_oculto"]) < 2:
        falhas.append("EIXO rosto_ato1: so' um lado sai em %d sorteios — o "
                      "experimento inteiro depende dos dois" % n)

    # =======================================================================
    # ⭐⭐ A MEDICAO QUE TERIA PEGO O DEFEITO DO RARO 16
    # =======================================================================
    # O pool de la' nasceu com oito falhas e as OITO eram pergunta: contar
    # entradas dizia "8 opcoes", e o operador viu na tela que era uma frase
    # repintada. Contar FORMA e' o que mede variacao percebida — e a
    # DISTRIBUICAO importa mais que a existencia, porque uma forma em 60% dos
    # videos e' quase o pool antigo com enfeite.
    for eixo, campo, formas in (("abertura", "forma", FORMAS_ABERTURA),
                                ("testemunha", "forma", FORMAS_TESTEMUNHA),
                                ("prova", "forma", FORMAS_PROVA)):
        cont = collections.Counter(sp[eixo][campo] for sp in specs)
        print("  FORMA de %s (o que o espectador percebe, nao o numero de "
              "entradas):" % eixo)
        for k, v in cont.most_common():
            print("     %-14s %3d  %2d%%" % (k, v, 100 * v // len(specs)))
        faltando = [f for f in formas if f not in cont]
        if faltando:
            falhas.append("[FORMA] %s: as formas %s nunca saem — pool de forma "
                          "unica com enfeite" % (eixo, faltando))
        # ⛔ E O PISO TAMBEM E' LENTE. Dominancia e' metade do defeito; a
        # outra metade e' a forma que existe no pool e nao sai do sorteio
        # porque so' tem entrada LONGA. Medido: `tarefa` ficou em 3% e `dia`
        # em 9% ate' cada uma ganhar uma entrada curta.
        # ⚠️ O piso e' 4% e nao 10% por causa da `plateia`, que e' estrutural:
        # ela so' existe em DOIS dos nove desastres (os dois de ambiente
        # fechado com plateia sentada), e isso e' desenho, nao defeito.
        raro = [(k, v) for k, v in cont.items()
                if 100 * v // len(specs) < 4]
        if raro:
            falhas.append("[FORMA] %s: %s abaixo de 4%% — forma que so' tem "
                          "entrada LONGA nao cabe ao lado dos beats maiores e "
                          "morre em silencio" % (eixo, sorted(raro)))
        dom = cont.most_common(1)[0]
        if 100 * dom[1] // len(specs) > 45:
            falhas.append("[FORMA] %s: `%s` domina %d%% — num sorteio filtrado "
                          "por orcamento a entrada CURTA vira peso sem "
                          "ninguem pedir (RARO 16)"
                          % (eixo, dom[0], 100 * dom[1] // len(specs)))

    print("  linter: %d ERRO, %d AVISO" % (sum(erros.values()), avisos))
    for k, v in erros.most_common(6):
        print("     %4dx %s" % (v, k))

    # =======================================================================
    # O CONTRATO DOS POOLS
    # =======================================================================
    for pool, nome in ((DESASTRES, "DESASTRES"), (PESSOAS, "PESSOAS"),
                       (REENCONTROS, "REENCONTROS"), (ROUPAS, "ROUPAS"),
                       (ROSTOS, "ROSTOS"), (ABERTURAS, "ABERTURAS"),
                       (BEATS_TESTEMUNHA, "BEATS_TESTEMUNHA"), (PROVAS, "PROVAS"),
                       (CTAS, "CTAS"), (SELOS, "SELOS"), (VIRADAS, "VIRADAS"),
                       (REMEDIOS, "REMEDIOS"), (PARCEIROS, "PARCEIROS")):
        ids = [x["id"] for x in pool]
        if len(set(ids)) != len(ids):
            falhas.append("%s: id repetido — o ledger e o cadeado casam por id"
                          % nome)

    # ⛔ O beat do desastre cabe no orcamento mais apertado que existe: a menor
    # abertura + a menor testemunha + o fecho. Beat de 16 palavras mataria a
    # combinacao mais curta e nao apareceria em sorteio nenhum.
    d0 = _dic({"pessoa": PESSOAS[0]})
    min_ab = min(_palavras(a["txt"] % d0) for a in ABERTURAS)
    min_te = min(_palavras(t["txt"] % d0) for t in BEATS_TESTEMUNHA)
    for des in DESASTRES:
        if des["id"] not in DESASTRES_FALA:
            falhas.append("DESASTRE %s sem beat de fala" % des["id"])
            continue
        n_ = _palavras(des["fala"] % d0)
        if n_ + min_ab + min_te + _palavras(FECHO_ATO1) > TETO_FALA[1]:
            falhas.append("[TETO] o beat do desastre %s tem %d palavras e nao "
                          "cabe nem com a menor abertura (%d) e a menor "
                          "testemunha (%d)" % (des["id"], n_, min_ab, min_te))
        for f in des["formas"]:
            if f not in FORMAS_TESTEMUNHA:
                falhas.append("DESASTRE %s cita a forma %r, que nao existe em "
                              "BEATS_TESTEMUNHA" % (des["id"], f))
        if not [p for p in PESSOAS if p["sexo"] in des["sexos"]]:
            falhas.append("DESASTRE %s: nenhuma pessoa cabe nele" % des["id"])

    # ⛔⛔ TODA ABERTURA CARREGA O NOME. Uma que so' use `obj` deixaria o casal
    # sem nome no take 1 (`obj` e' `them` la'), e o nome e' o eixo mais barato
    # do motor — perde-lo no unico take que apresenta a pessoa mata o eixo.
    for a in ABERTURAS:
        if not any(s in a["txt"] for s in ("%(ref)s", "%(Suj)s", "%(suj)s",
                                           "%(poss_nome)s", "%(Poss_nome)s")):
            falhas.append("ABERTURA %s nao carrega o nome em slot nenhum"
                          % a["id"])
        if a["forma"] not in FORMAS_ABERTURA:
            falhas.append("ABERTURA %s com forma desconhecida %r"
                          % (a["id"], a["forma"]))

    # ⛔⛔ `%(ref)s` E' SLOT DE OBJETO, E A LENTE COBRA A POSICAO.
    # ⚠️ DEFEITO REAL, achado LENDO a fala montada e nao por lente nenhuma:
    # duas entradas usavam `ref` como SUJEITO e devolviam *"Want the same
    # result THEM got?"* e *"this is what THEM looked like"* — ingles quebrado
    # em todo video de casal, e' dizer, em 4 das 14 pessoas do pool.
    # ⭐ E' o §4 das licoes na forma mais literal: o slot passava no linter
    # (existe, e' interpolado, nao estoura o teto) e NAO cumpria a funcao pela
    # qual existe. Regra que da' para checar por regex vira linter — esta da'.
    _ANTES_DE_REF = ("was", "to", "for", "took", "gave", "about", "at", "with",
                     "of", "by", "toward", "from")
    for pool, nome in ((ABERTURAS, "ABERTURAS"), (BEATS_TESTEMUNHA, "BEATS_TESTEMUNHA"),
                       (VIRADAS, "VIRADAS"), (REMEDIOS, "REMEDIOS"),
                       (PROVAS, "PROVAS"), (SELOS, "SELOS"), (CTAS, "CTAS")):
        for x in pool:
            for m_ in _RX_ANTES_REF.finditer(x["txt"]):
                if m_.group(1).lower() not in _ANTES_DE_REF:
                    falhas.append("[SLOT] %s %s usa `%%(ref)s` depois de %r — "
                                  "`ref` e' OBJETO (no casal ele vale `them`), "
                                  "e em posicao de sujeito a frase sai "
                                  "quebrada: use `%%(suj)s`"
                                  % (nome, x["id"], m_.group(1)))

    for r in ROSTOS:
        if not r.get("cabelo"):
            falhas.append("ROSTO %s sem cabelo declarado — com o rosto oculto "
                          "no take 1 ele e' a unica ancora que sobra" % r["id"])
        for proibido in ("jaw", "cheekbone", "cheeks", "chin line", "jowl",
                         "double chin", "round face"):
            if proibido in r["desc"].lower():
                falhas.append("ROSTO %s cita %r — o peso MOVE esse traco, e "
                              "ancora que o cita briga com a magreza do take 2"
                              % (r["id"], proibido))
    for roupa in ROUPAS:
        for s_ in roupa["sexos"]:
            if s_ not in SEXOS:
                falhas.append("ROUPA %s: sexo %r desconhecido"
                              % (roupa["id"], s_))
    for p in PESSOAS:
        if p["sexo"] not in SEXOS:
            falhas.append("PESSOA %s: sexo %r desconhecido" % (p["id"], p["sexo"]))
        if p["nome"] and p["nome"] not in p["ref"]:
            falhas.append("PESSOA %s: `ref` nao carrega o nome, e a abertura "
                          "sai sem ele" % p["id"])
    # ⛔ CT8 na origem: nenhum pool de fala pede follow. A fonte pede em 15 de
    # 15, e a copia distraida traria o beat junto.
    for pool, nome in ((ABERTURAS, "ABERTURAS"), (BEATS_TESTEMUNHA, "BEATS_TESTEMUNHA"),
                       (VIRADAS, "VIRADAS"), (REMEDIOS, "REMEDIOS"),
                       (PROVAS, "PROVAS"), (SELOS, "SELOS"), (CTAS, "CTAS")):
        for x in pool:
            if sc.FOLLOW_16.search(x["txt"]):
                falhas.append("[CT8] %s %s pede follow — a DM sai igual"
                              % (nome, x["id"]))
            if sc.INGREDIENTES_16.search(x["txt"]):
                falhas.append("[CT5] %s %s nomeia ingrediente — a receita e' a "
                              "moeda" % (nome, x["id"]))
    # ⛔ CT6 e o literal do CTA, em TODAS as entradas.
    for c in CTAS:
        if "%(cta)s" not in c["txt"]:
            falhas.append("[CT6] CTA %s sem o slot da keyword" % c["id"])
        if not sc.ENTREGA_16.search(c["txt"]):
            falhas.append("[CT6] CTA %s nao diz ONDE a receita chega" % c["id"])
        if not c["txt"].rstrip().endswith("."):
            falhas.append("[CT1] CTA %s nao termina no pedido" % c["id"])

    # ⛔⛔ O CONTRATO DO `porte`, ENTRADA POR ENTRADA. As tres clausulas vivem
    # aqui e nao so' na lente por video, porque pool novo entra no arquivo sem
    # passar por sorteio nenhum e o defeito so' apareceria no lote do operador.
    # ⛔ OS SEIS CAMPOS DE CORPO, e nao mais so' o `porte`: a arquitetura de
    # 2026-08-21 espalhou o corpo por `porte`, `barriga`, `membros`, `pescoco`,
    # `nuca` e `segundo`, e cobrar um deles seria deixar cinco portas abertas.
    _CAMPOS_CORPO = ("porte", "barriga", "membros", "pescoco", "nuca",
                     "segundo")
    for p_ in PESSOAS:
        for campo in _CAMPOS_CORPO:
            txt = p_.get(campo)
            if not txt:
                continue
            if _RX_CORPO_NOMEADO.search(txt):
                falhas.append("[CORPO] %s.%s reintroduz o corpo com sintagma "
                              "de pessoa novo — a primeira sintagma do IMAGE "
                              "01 ja' o nomeia, e sujeito reintroduzido vira "
                              "corpo a mais (RU14)" % (p_["id"], campo))
            # ⭐ A LISTA LARGA, NAO A DO ARTIGO DEFINIDO (2026-08-21). Os
            # campos de corpo descrevem o CORPO e nunca a roupa, entao aqui
            # nao ha' forma legitima de nomear peca nenhuma — nem `the dress`
            # nem `a paper gown`. E' o unico lugar do motor onde a lista larga
            # pode ser cobrada crua, e ela fecha o buraco que a `RU19` nao
            # alcanca: a construcao de vestir do `corpo1` traz `and`/`with` no
            # meio e corta o casamento.
            m_ = _RX_PECA_NO_CORPO.search(txt)
            if m_:
                falhas.append("[CORPO] %s.%s nomeia %r — a peca e' do eixo "
                              "ROUPAS e de mais ninguem (RU3/RU19)"
                              % (p_["id"], campo, m_.group(0)))
            if not txt.rstrip().endswith("."):
                falhas.append("[CORPO] %s.%s nao fecha em ponto — a montagem "
                              "junta os seis elementos com espaco e a frase "
                              "seguinte emendaria na anterior"
                              % (p_["id"], campo))
        # ⛔ O ROSTO SO' PODE VIVER NO `pescoco`, que e' o elemento 5 do corpo
        # com o rosto VISIVEL. Nos outros cinco ele e' o defeito que a RU4 mede
        # (9% de TODOS os videos antes do conserto).
        for campo in ("porte", "barriga", "membros", "nuca", "segundo"):
            txt = p_.get(campo)
            if not txt:
                continue
            m_ = _RX_ROSTO_NO_PORTE.search(txt)
            if m_:
                falhas.append("[CORPO] %s.%s cita %r — com o rosto OCULTO a "
                              "camera esta' de costas e a frase descreve o que "
                              "nao esta' em quadro (RU4)"
                              % (p_["id"], campo, m_.group(0)))
        # ⛔⛔ E A `nuca` E' A VARIANTE DE COSTAS: queixo, papada e bochecha
        # SAEM por contradicao direta com o proprio quadro. Ja' o `pescoco` os
        # EXIGE — e' onde os tracos que o peso move moram, longe da ancora de
        # rosto que os proibe.
        m_ = _RX_TRACO_DE_PESO.search(p_.get("nuca", ""))
        if m_:
            falhas.append("[CORPO] %s.nuca cita %r — de costas nao ha' queixo "
                          "nem bochecha em quadro, e contradicao o gerador "
                          "resolve virando o corpo" % (p_["id"], m_.group(0)))
        if not _RX_TRACO_DE_PESO.search(p_.get("pescoco", "")):
            falhas.append("[CORPO] %s.pescoco nao traz queixo, papada nem "
                          "bochecha — e' o elemento 5, e os tracos que o peso "
                          "move so' podem morar nele" % p_["id"])
        # ⛔ ELEMENTO 1: NUMERO DE PESO, e na faixa CRIVEL PARA EMAGRECER.
        # 350-550 lb, nunca 880: a mesma pessoa aparece magra oito segundos
        # depois, e um corpo que o take 2 nao consegue desmentir mata o angulo.
        lb = _libras(p_["porte"])
        if lb is None:
            falhas.append("[CORPO] %s.porte sem numero de peso por extenso — "
                          "adjetivo de porte o gerador ignora (RU20)"
                          % p_["id"])
        elif not 350 <= lb <= 550:
            falhas.append("[CORPO] %s.porte diz %d lb, fora da faixa 350-550 "
                          "— peso que o take 2 nao consegue desmentir"
                          % (p_["id"], lb))
        if not _RX_COMPARACAO.search(p_["porte"]):
            falhas.append("[CORPO] %s.porte sem referente de escala — numero "
                          "sozinho nao e' ancora (RU20)" % p_["id"])
        # ⛔⛔ ELEMENTO 2: a barriga tem de trazer AREA DE QUADRO e COMPARACAO
        # na propria entrada. E' o elemento que faltava inteiro no lote
        # reprovado, e o unico que obriga o gerador a alocar pixel ao corpo.
        if not _RX_POSICAO_QUADRO.search(p_["barriga"]):
            falhas.append("[CORPO] %s.barriga nao diz quanto do QUADRO ela "
                          "ocupa — area nao declarada e' area da media do "
                          "treino (RU20)" % p_["id"])
        if not _RX_COMPARACAO.search(p_["barriga"]):
            falhas.append("[CORPO] %s.barriga sem comparacao — adjetivo o "
                          "gerador ignora (RU20)" % p_["id"])
        if not _RX_COMPARACAO.search(p_["membros"]):
            falhas.append("[CORPO] %s.membros sem comparacao — o elemento 4 e' "
                          "`braco mais grosso que coxa`, nao `bracos grossos`"
                          % p_["id"])
        # ⛔ O SEGUNDO CORPO SO' EXISTE NO CASAL, e comprimido: o teto de bloco
        # da AdBatch e' 3.900 caracteres e cento e quarenta palavras vezes dois
        # o estouram.
        if p_["sexo"] == "casal":
            if not p_.get("segundo"):
                falhas.append("[CORPO] %s e' casal e nao tem `segundo` — o "
                              "marido ficaria sem corpo nenhum" % p_["id"])
            elif _palavras(p_["segundo"]) > 30:
                falhas.append("[CORPO] %s.segundo com %d palavras (teto 30) — "
                              "o segundo corpo e' COMPRIMIDO, por orcamento de "
                              "bloco" % (p_["id"], _palavras(p_["segundo"])))
        elif p_.get("segundo"):
            falhas.append("[CORPO] %s nao e' casal e tem `segundo` — segundo "
                          "corpo num video de uma pessoa so'" % p_["id"])

    # ⛔ E O CONTRATO DO `sobre` (elemento 3), no eixo ROUPAS: a peca esticada
    # SOBRE a barriga, COBRINDO tudo, e a bainha PUXADA PARA BAIXO. As tres
    # clausulas sao forma e guarda de moderacao ao mesmo tempo.
    for roupa in ROUPAS:
        s_ = roupa.get("sobre", "")
        if not s_:
            falhas.append("[ROUPA] %s sem `sobre` — sem a peca esticada sobre "
                          "a barriga o corpo fica sem casca (RU20)"
                          % roupa["id"])
            continue
        if "belly" not in s_:
            falhas.append("[ROUPA] %s.sobre nao fala da barriga — a peca tem "
                          "de estar esticada SOBRE ela" % roupa["id"])
        if not re.search(r"\bcovers?\b", s_):
            falhas.append("[ROUPA] %s.sobre nao diz que a peca COBRE tudo — e' "
                          "forma e guarda de moderacao no mesmo sintagma"
                          % roupa["id"])
        if "stays inside it" not in s_ and "inside it" not in s_:
            falhas.append("[ROUPA] %s.sobre nao poe a barriga inteira DENTRO "
                          "da peca" % roupa["id"])
        # ⛔ O VAO. As formas antigas implicavam abertura e pele exposta, que e'
        # pedir recusa de moderacao numa cena que ja' e' de corpo em queda.
        for vao in ("pulling open", "pulling apart", "riding up", "rucked up",
                    "gaping", "gapes", "gap between the buttons"):
            for campo in ("antes", "sobre"):
                if vao in roupa[campo]:
                    falhas.append("[ROUPA] %s.%s diz %r — vao implica pele "
                                  "exposta; o que fica e' o tecido TENSIONADO"
                                  % (roupa["id"], campo, vao))
        # ⛔ E o `sobre` nomeia a peca com modificador na frente: a forma nua
        # (`the blouse`) faria a RU3 acusar a propria peca-ancora.
        m_ = _RX_PECA_FANTASMA.search(s_)
        if m_:
            falhas.append("[ROUPA] %s.sobre nomeia %r na forma nua — a RU3 "
                          "acusaria a propria ancora" % (roupa["id"],
                                                         m_.group(0)))

    # ⛔ E O MESMO PARA `acao` e `test` DOS DESASTRES: peca fantasma e camera
    # parada num bloco cujo TAKE e' handheld.
    for d_ in DESASTRES:
        for campo in ("acao", "test"):
            m_ = _RX_PECA_FANTASMA.search(d_[campo])
            if m_:
                falhas.append("[DESASTRE] %s.%s nomeia %r — a peca ancora e' "
                              "UMA (RU3)" % (d_["id"], campo, m_.group(0)))
        m_ = _RX_CAM_PARADA.search(d_["cam"])
        if m_:
            falhas.append("[DESASTRE] %s.cam diz %r e os TAKES sao TODOS "
                          "handheld com deriva sorteada — duas cameras no "
                          "mesmo bloco e o gerador escolhe uma"
                          % (d_["id"], m_.group(0)))
        # ⛔⛔ E QUEM DECLARA `silencio` TEM DE TER A CENA MUDA. Sem isso a
        # fala diz *"nobody said a word"* sobre gente rindo em quadro — 21 de
        # 21 sorteios dessa forma, medido em 2026-08-21.
        if "silencio" in d_["formas"]:
            for campo, alt in (("test", "test_q"), ("mov", "mov_q"),
                               ("audio", "audio_q")):
                base = d_.get(alt, d_[campo])
                if re.search(r"\blaugh(s|ing|ed)?\b", base, re.I):
                    falhas.append("[SILENCIO] %s comporta a forma `silencio` e "
                                  "o %s ainda ri — falta a variante muda `%s`"
                                  % (d_["id"], campo, alt))

    # ⛔ A CLAUSULA DE CAMERA DO REENCONTRO NAO CONTA GENTE (32% dos videos
    # tinham TRES pessoas sob um `both figures`).
    m_ = _RX_CONTAGEM.search(CAM_REENCONTRO)
    if m_:
        falhas.append("[CAM] CAM_REENCONTRO diz %r — o elenco do reencontro "
                      "muda com o sexo (2 ou 3 pessoas) e a clausula nao "
                      "pode contar" % m_.group(0))

    # =======================================================================
    # ⭐⭐ CONTROLES NEGATIVOS — cada lente prova que ACUSA o defeito plantado
    # =======================================================================
    # ⛔ Lente que nunca acusou e' lente que ninguem sabe se funciona; lente que
    # reprova 100% e' lente quebrada. Cada par abaixo tem o defeito E o limpo.
    s0 = sortear("joe", random.Random(7), {})
    b0 = montar(s0)

    def _prova(fn, spec_t, blocos_t):
        p_ = []
        fn(spec_t, blocos_t, p_)
        return bool(p_)

    s_casal = sortear("joe", random.Random(11), {}, {"sexo": "casal"})
    b_casal = montar(s_casal)
    s_nome = next((sortear("joe", random.Random(700 + k), {})
                   for k in range(60)
                   if sortear("joe", random.Random(700 + k), {})["pessoa"]["nome"]
                   and sortear("joe", random.Random(700 + k),
                               {})["pessoa"]["sexo"] != "casal"), s0)
    b_nome = montar(s_nome)

    controles = [
        ("RU1 sem testemunha na IMAGE", _ru1_testemunha, s0,
         dict(b0, **{IMAGENS[0]: "A ramp and a fallen body."}), True),
        ("RU1 limpo", _ru1_testemunha, s0, b0, False),
        ("RU2 sem a Ruth no reencontro", _ru2_ruth, s0,
         dict(b0, **{IMAGENS[1]: "A porch with two women smiling."}), True),
        ("RU2 com a Ruth na humilhacao", _ru2_ruth, s0,
         dict(b0, **{IMAGENS[0]: b0[IMAGENS[0]]
                     + " An old woman in a white prayer cap watches."}), True),
        ("RU2 limpo", _ru2_ruth, s0, b0, False),
        ("RU3 sem a peca no take 2", _ru3_peca_ancora, s0,
         dict(b0, **{IMAGENS[1]: "A slim woman in a denim jacket."}), True),
        ("RU3 limpo", _ru3_peca_ancora, s0, b0, False),
        # ⭐ A PECA FANTASMA — o defeito exato que a varredura mediu: o `porte`
        # dizia `the dress` sobre quem veste camiseta.
        ("RU3 com peca fantasma no IMAGE 01", _ru3_peca_ancora, s0,
         dict(b0, **{IMAGENS[0]: b0[IMAGENS[0]]
                     + " The dress is stretched tight across her."}), True),
        # ⚠️ CONTROLE NEGATIVO: a roupa das TESTEMUNHAS e' legitima e sai com
        # artigo indefinido — a lente nao pode acusar `a heavy man in a polo`.
        ("RU3 nao acusa roupa de figurante", _ru3_peca_ancora, s0,
         dict(b0, **{IMAGENS[0]: b0[IMAGENS[0]]
                     + " Two of them wear a polo and a plain shirt."}), False),
        ("RU16 silencio sobre gente rindo", _ru16_silencio_no_quadro,
         dict(s0, testemunha=_por_id(BEATS_TESTEMUNHA, "si1")),
         dict(b0, **{IMAGENS[0]: b0[IMAGENS[0]]
                     + " Two of them are laughing."}), True),
        ("RU16 limpo com silencio", _ru16_silencio_no_quadro,
         dict(s0, testemunha=_por_id(BEATS_TESTEMUNHA, "si1")),
         dict(b0, **{IMAGENS[0]: "A quiet room. Nobody moves.",
                     TAKES[0]: "Nobody speaks."}), False),
        # ⚠️ E ela SO' vale para a forma `silencio`: rir em quadro e' o padrao
        # dos outros cinco beats, e uma lente que acusasse `laughing` sempre
        # reprovaria 400 de 400 videos certos.
        ("RU16 nao acusa fora do silencio", _ru16_silencio_no_quadro, s0,
         dict(b0, **{IMAGENS[0]: b0[IMAGENS[0]] + " Two of them are laughing."}),
         False),
        ("RU4 sem a ancora de rosto", _ru4_ancora_rosto, s0,
         dict(b0, **{IMAGENS[1]: "A slim woman on a porch."}), True),
        ("RU4 limpo", _ru4_ancora_rosto, s0, b0, False),
        ("RU5 com celular na mao da testemunha", _ru5_sem_aparelho, s0,
         dict(b0, **{IMAGENS[0]: b0[IMAGENS[0]]
                     + " Two of them hold phones up."}), True),
        ("RU5 com `filming` na direcao", _ru5_sem_aparelho, s0,
         dict(b0, **{TAKES[0]: b0[TAKES[0]].replace(
             "Handheld shot", "Handheld shot of a bystander filming")}), True),
        ("RU5 limpo", _ru5_sem_aparelho, s0, b0, False),
        ("RU6 homem na cadeira do salao", _ru6_coerencia,
         dict(s0, desastre=_por_id(DESASTRES, "cadeira_salao"),
              pessoa=_por_id(PESSOAS, "anon_homem_v40")), b0, True),
        ("RU6 testemunha de forma impossivel", _ru6_coerencia,
         dict(s0, desastre=_por_id(DESASTRES, "reabilitacao"),
              testemunha=_por_id(BEATS_TESTEMUNHA, "de1")), b0, True),
        ("RU6 limpo", _ru6_coerencia, s0, b0, False),
        ("RU7 nome fora do take 1", _ru7_nome,
         dict(s_nome, falas=["This was her before. Pure shame.",
                             s_nome["falas"][1], s_nome["falas"][2]]),
         b_nome, True),
        ("RU7 limpo", _ru7_nome, s_nome, b_nome, False),
        ("RU7 limpo no casal", _ru7_nome, s_casal, b_casal, False),
        ("RU8 com `yes` no CTA", _ru8_cta,
         dict(s0, falas=[s0["falas"][0], s0["falas"][1],
                         "Comment yes, and I will send it to your messages."]),
         b0, True),
        ("RU8 com follow na fala", _ru8_cta,
         dict(s0, falas=[s0["falas"][0], s0["falas"][1],
                         s0["falas"][2] + " Follow me first."]), b0, True),
        ("RU8 limpo", _ru8_cta, s0, b0, False),
        ("RU9 com a fala reescrita no caminho", _ru9_fala_no_take, s0,
         dict(b0, **{TAKES[0]: b0[TAKES[0]].replace(
             'Dialogue: "%s"' % sonorizar(s0["falas"][0]),
             'Dialogue: "This was somebody before."')}), True),
        ("RU9 limpo", _ru9_fala_no_take, s0, b0, False),
        ("RU10 com gelatina no quadro", _ru10_sem_gelatina, s0,
         dict(b0, **{IMAGENS[1]: b0[IMAGENS[1]]
                     + " A box of gelatin sits on the rail."}), True),
        ("RU10 limpo", _ru10_sem_gelatina, s0, b0, False),
        ("RU11 sem `Pure shame.`", _ru11_pure_shame,
         dict(s0, falas=["This was Betty before, and they laughed.",
                         s0["falas"][1], s0["falas"][2]]), b0, True),
        ("RU11 limpo", _ru11_pure_shame, s0, b0, False),
        ("RU12 com a cena 1 estourada", _ru12_orcamento,
         dict(s0, falas=[" ".join(["word"] * 40), s0["falas"][1],
                         s0["falas"][2]]), b0, True),
        ("RU12 limpo", _ru12_orcamento, s0, b0, False),
        # ⭐ O CONTROLE DA RU13 PLANTA O DEFEITO QUE ELA ACHOU DE VERDADE: a
        # virada com `eight months later` ao lado do remedio com `eight weeks`,
        # que e' o par que o sorteio produzia antes de a duracao ir para um
        # beat so'.
        ("RU13 com dois prazos na mesma fala", _ru13_um_relogio,
         dict(s0, falas=[s0["falas"][0],
                         "And this is her eight months later, after eight "
                         "weeks of one simple remedy every morning.",
                         s0["falas"][2]]), b0, True),
        ("RU13 com prazo e FREQUENCIA (nao e' defeito)", _ru13_um_relogio,
         dict(s0, falas=[s0["falas"][0],
                         "And this is her now, after eight months of one "
                         "simple remedy every single morning.",
                         s0["falas"][2]]), b0, False),
        ("RU13 limpo", _ru13_um_relogio, s0, b0, False),
        # ⭐⭐ OS CONTROLES DAS CINCO LENTES NOVAS (2026-08-21). Cada um planta
        # o defeito EXATO que a varredura mediu no motor, e nao um parente.
        ("RU14 corpo reintroduzido", _ru14_um_corpo_so, s0,
         dict(b0, **{IMAGENS[0]: b0[IMAGENS[0]]
                     + " The very heavy customer is down on the tile."}), True),
        ("RU14 limpo", _ru14_um_corpo_so, s0, b0, False),
        ("RU14 limpo no casal (ela + o marido)", _ru14_um_corpo_so,
         s_casal, b_casal, False),
        # ⭐⭐ E O CONTROLE QUE A REESCRITA DE 2026-08-21 EXIGE: a lente tem de
        # saber a diferenca entre REINTRODUZIR um corpo e DESCREVER o corpo que
        # ja' existe. Cento e quarenta palavras de barriga, membros e pescoco
        # nao sao um segundo corpo — e foi por confundir os dois que a versao
        # anterior mediu *"1200 -> 0"* e entregou o lote reprovado.
        ("RU14 nao acusa a descricao longa do MESMO corpo", _ru14_um_corpo_so,
         s0, dict(b0, **{IMAGENS[0]: b0[IMAGENS[0]] + " " + s0["pessoa"]
                         ["barriga"] + " " + s0["pessoa"]["membros"]}), False),
        # ⚠️ E o outro lado do mesmo par: `heavy` + substantivo de gente segue
        # acusando mesmo quando o sintagma nao e' literalmente `very heavy`.
        ("RU14 acusa a reintroducao com outro modificador", _ru14_um_corpo_so,
         s0, dict(b0, **{IMAGENS[0]: b0[IMAGENS[0]] + " An extremely heavy "
                         "grey-haired shopper stands at the till."}), True),
        # ⭐⭐ OS CONTROLES DA RU20, PAREADOS COM O TEXTO QUE PRODUZIU O LOTE
        # REPROVADO. O plantio nao e' um parente do defeito: e' o bloco de
        # corpo antigo, palavra por palavra.
        ("RU20 o corpo VELHO (`wide through the middle`)", _ru20_corpo_obeso,
         s0, dict(b0, **{IMAGENS[0]: (
             "IMAGE 01/03: Vertical 9:16 portrait orientation. A driveway. "
             + MARCA_CORPO + " is a very heavy 39-year-old white American "
             "woman, wearing a cream blouse. She is wide through the middle. "
             "Whatever is under her taking her weight has vanished from sight "
             "beneath her, " + SUPORTE_FIM)}), True),
        ("RU20 sem as duas ancoras de recorte", _ru20_corpo_obeso, s0,
         dict(b0, **{IMAGENS[0]: "A driveway and a fallen body."}), True),
        ("RU20 limpo", _ru20_corpo_obeso, s0, b0, False),
        ("RU20 limpo no casal", _ru20_corpo_obeso, s_casal, b_casal, False),
        # ⚠️ CONTROLE NEGATIVO DE VERDADE: a lente le' o BLOCO DE CORPO e nao a
        # IMAGE 01 inteira. Um `cen` que fale em `frame` e um `test` que fale
        # em `wider than` nao podem fazer um corpo vazio PASSAR — lente que
        # passa pelo motivo errado e' lente cega.
        ("RU20 nao passa por causa do cenario", _ru20_corpo_obeso, s0,
         dict(b0, **{IMAGENS[0]: (
             "IMAGE 01/03: A hallway that fills the frame from edge to edge, "
             "wider than the doors, with a bench heavier than a car. "
             + MARCA_CORPO + " is a very heavy 39-year-old white American "
             "woman. She is wide through the middle. Whatever is under her "
             "taking her weight has vanished from sight beneath her, "
             + SUPORTE_FIM)}), True),
        ("RU15 casal colado e depois separado", _ru15_geometria_casal, s_casal,
         dict(b_casal, **{IMAGENS[0]: b_casal[IMAGENS[0]].replace(
             "and with her", "and beside her")}), True),
        ("RU15 limpo", _ru15_geometria_casal, s_casal, b_casal, False),
        # ⚠️ CONTROLE NEGATIVO DE VERDADE: no singular a lente nao pode
        # acusar, porque `beside her` la' se refere a' RUTH.
        ("RU15 nao acusa fora do casal", _ru15_geometria_casal, s0, b0, False),
        ("RU17 `her head` num video de homem", _ru17_pronome_do_vizinho,
         dict(s0, pessoa=_por_id(PESSOAS, "anon_homem_v40")),
         dict(b0, **{IMAGENS[2]: b0[IMAGENS[2]]
                     + " and the person beside her has turned her head."}),
         True),
        ("RU17 uma pessoa ao lado num casal", _ru17_pronome_do_vizinho,
         s_casal, dict(b_casal, **{IMAGENS[2]: b_casal[IMAGENS[2]]
                                   + " the person beside her smiles."}), True),
        ("RU17 duas pessoas ao lado num singular", _ru17_pronome_do_vizinho,
         s0, dict(b0, **{TAKES[2]: b0[TAKES[2]]
                         + " the two beside her smile."}), True),
        ("RU17 limpo", _ru17_pronome_do_vizinho, s0, b0, False),
        ("RU17 limpo no casal", _ru17_pronome_do_vizinho, s_casal, b_casal,
         False),
        ("RU18 ingrediente na CENA 2 (o buraco do CT5)",
         _ru18_ingrediente_nas_tres,
         dict(s0, falas=[s0["falas"][0],
                         "Look at her now, after one spoon of apple cider "
                         "vinegar and lemon every morning.", s0["falas"][2]]),
         b0, True),
        ("RU18 ingrediente na CENA 3", _ru18_ingrediente_nas_tres,
         dict(s0, falas=[s0["falas"][0], s0["falas"][1],
                         "Comment recipe, and I will send the apple cider "
                         "vinegar to your messages."]), b0, True),
        ("RU18 limpo", _ru18_ingrediente_nas_tres, s0, b0, False),
        # ⛔ RU5: o controle antigo plantava SO' antes do `Dialogue:` — que era
        # o unico pedaco que a lente lia. Os dois de baixo sao a metade que ela
        # nunca provou.
        ("RU5 com aparelho na linha Audio:", _ru5_sem_aparelho, s0,
         dict(b0, **{TAKES[0]: b0[TAKES[0]].replace(
             "Audio: ", "Audio: a phone ringing, ")}), True),
        ("RU5 com `filmed` dentro da FALA", _ru5_sem_aparelho, s0,
         dict(b0, **{TAKES[0]: b0[TAKES[0]].replace(
             "Pure shame.", "getting filmed by everyone. Pure shame.")}), True),
        # ⭐⭐ OS CONTROLES DA RU19, E ELES SAO PAREADOS DE PROPOSITO: o
        # plantio e' o defeito EXATO que a `avental_costas` tinha, e os tres
        # limpos sao os tres DONOS que a lente precisa saber separar. Os dois
        # ultimos (terceiro e movel) sao copia literal de campos que um revisor
        # humano acusou e que estao CERTOS — `tomografo_estreito` e
        # `provador_loja`. Lente que reprova o certo e' lente quebrada.
        ("RU19 avental VESTIDO no corpo dela", _ru19_so_a_ancora_no_corpo, s0,
         dict(b0, **{IMAGENS[0]: b0[IMAGENS[0]] + " The body has come out of "
                     "the cubicle in a pale blue paper gown with the two back "
                     "ties hanging loose."}), True),
        ("RU19 limpo", _ru19_so_a_ancora_no_corpo, s0, b0, False),
        ("RU19 limpo no casal (ela + a peca do marido)",
         _ru19_so_a_ancora_no_corpo, s_casal, b_casal, False),
        ("RU19 nao acusa avental em TERCEIRO", _ru19_so_a_ancora_no_corpo, s0,
         dict(b0, **{IMAGENS[0]: b0[IMAGENS[0]] + " Six patients in paper "
                     "gowns are waiting on the corridor chairs."}), False),
        ("RU19 nao acusa vestido em MOVEL", _ru19_so_a_ancora_no_corpo, s0,
         dict(b0, **{IMAGENS[0]: b0[IMAGENS[0]] + " A chrome return rack hung "
                     "with dresses and jeans stands down the middle."}),
         False),
        # ⚠️ E O CONTROLE QUE PROTEGE A SAIDA CERTA: *"still in its own street
        # clothes"* e' como se diz que ninguem esta' se despindo sem escrever
        # a declaracao de conformidade que o repo baniu. Se a lente acusar
        # isso, ela empurra a copy de volta para `fully clothed`.
        ("RU19 nao acusa `street clothes`", _ru19_so_a_ancora_no_corpo, s0,
         dict(b0, **{IMAGENS[0]: b0[IMAGENS[0]] + " The body is inside the "
                     "cubicle still in its own street clothes."}), False),
        ("RU19 peca SOBRE os ombros (a peca como sujeito)",
         _ru19_so_a_ancora_no_corpo, s0,
         dict(b0, **{IMAGENS[0]: b0[IMAGENS[0]] + " An orange life vest is on "
                     "over the shoulders with both front straps hanging."}),
         True),
    ]
    for rotulo, fn, spec_t, blocos_t, deve in controles:
        obtido = _prova(fn, spec_t, blocos_t)
        if obtido != deve:
            falhas.append("CONTROLE %s: a lente %s (esperado: %s)"
                          % (rotulo, "acusou" if obtido else "passou",
                             "acusar" if deve else "passar"))

    # =======================================================================
    # ⭐⭐ RU19 SOBRE OS DESASTRES, UM A UM — nao sobre uma amostra
    # =======================================================================
    # ⛔ Controle negativo prova que a lente ACUSA; so' a varredura prova que
    # ela nao acusa NINGUEM que esta' certo, e e' esse o lado caro: um falso
    # positivo aqui manda reescrever cena que ja' funciona, e cena e' alcada do
    # operador. A varredura sorteia ate' ver TODOS eles no bloco MONTADO —
    # campo passa em lente e quadro inteiro nao passa e' o defeito do VICK 16.
    ru19_vistos, ru19_maus = set(), {}
    for k in range(6000):
        if len(ru19_vistos) == len(DESASTRES):
            break
        sp_ = sortear(pags[k % len(pags)], random.Random(90000 + k), {})
        ru19_vistos.add(sp_["desastre"]["id"])
        a_ = []
        _ru19_so_a_ancora_no_corpo(sp_, montar(sp_), a_)
        if a_:
            ru19_maus.setdefault(sp_["desastre"]["id"], a_[0][1])
    print("  RU19 (a peca-ancora e' a UNICA no corpo dela): %d de %d "
          "desastres vistos no bloco montado · %d acusados"
          % (len(ru19_vistos), len(DESASTRES), len(ru19_maus)))
    if len(ru19_vistos) != len(DESASTRES):
        falhas.append("[RU19] so' %d dos %d desastres apareceram na varredura "
                      "— lente medida sobre amostra nao e' lente medida"
                      % (len(ru19_vistos), len(DESASTRES)))
    for id_, msg in sorted(ru19_maus.items()):
        falhas.append("[RU19] %s: %s" % (id_, msg))

    # ⛔ O EIXO `rosto_ato1` TEM DE MOVER O QUADRO. Botao que promete e nao
    # entrega e' pior que botao ausente — e o repo ja' pagou isso tres vezes.
    oc = montar(sortear("joe", random.Random(3), {}, {"rosto_ato1": "oculto"}))
    vi = montar(sortear("joe", random.Random(3), {}, {"rosto_ato1": "visivel"}))
    if oc[IMAGENS[0]] == vi[IMAGENS[0]]:
        falhas.append("EIXO rosto_ato1: oculto e visivel produzem a MESMA "
                      "IMAGE 01")
    for quer in ("mulher", "homem", "casal"):
        vistos = set()
        for k in range(20):
            sp = sortear(pags[k % len(pags)], random.Random(900 + k), {},
                         {"sexo": quer})
            vistos.add(sp["pessoa"]["sexo"])
        if vistos != {quer}:
            falhas.append("[PRE-SELECAO] `sexo=%s` devolveu %s — filtro que "
                          "cede em silencio e' pior que filtro ausente"
                          % (quer, sorted(vistos)))

    # ⛔ AS TRES DERIVAS SAO DISTINTAS NO MESMO VIDEO: camera que repete
    # movimento em cortes seguidos e' o que denuncia geracao.
    for i in range(40):
        d_ = sortear(pags[i % len(pags)], random.Random(1000 + i), {})["derivas"]
        if len(set(d_)) != 3:
            falhas.append("DERIVAS: o video %d repete movimento de camera" % i)
            break

    # ⭐⭐ O PAINEL SIMULADO — cada eixo trocado como a UI troca, e o linter
    # cobrado depois. ⛔ Sortear e' so' METADE do que o operador faz.
    for chave in [e[0] for e in EIXOS_UI]:
        pool_nome = dict((e[0], e[2]) for e in EIXOS_UI)[chave]
        for k in range(12):
            sp = sortear(pags[k % len(pags)], random.Random(500 + k), {})
            opcoes = [x for x in globals()[pool_nome] if x != sp[chave]]
            if not opcoes:
                continue
            sp[chave] = random.Random(k).choice(opcoes)
            if chave == "pessoa":
                sp["idade"] = sp["pessoa"]["idade"]
            reescreve = EIXOS_QUE_MEXEM_NA_COPY.get(chave)
            if reescreve:
                reescreve(sp, random.Random(k))
            ruins = [m for nv, m in lint(sp, montar(sp)) if nv == "ERRO"]
            if ruins:
                falhas.append("[PAINEL] trocar o eixo %r deixa o video "
                              "invalido: %s" % (chave, ruins[0][:80]))
                break

    # ⭐ E o botao `trocar` de CENA, que a UI chama por `nova_fala`.
    if not callable(globals().get("nova_fala")):
        falhas.append("[PAINEL] sem `nova_fala`: o botao `trocar` de cena fica "
                      "MORTO e a tela diz que o agente nao tem banco de copy")
    else:
        for k in range(12):
            sp = sortear(pags[k % len(pags)], random.Random(700 + k), {})
            sp["falas"][k % 3] = nova_fala(sp, k % 3, random.Random(k))
            ruins = [m for nv, m in lint(sp, montar(sp)) if nv == "ERRO"]
            if ruins:
                falhas.append("[PAINEL] `nova_fala` na cena %d deixa o video "
                              "invalido: %s" % (k % 3 + 1, ruins[0][:80]))
                break
        # ⛔⛔ E A PROVA DE QUE O BOTAO MUDA ALGUMA COISA E' POR CONTAGEM, NAO
        # POR UM CLIQUE. ⚠️ FALSO POSITIVO MEDIDO em 2026-08-21: a versao
        # anterior reprovava o motor quando UM clique devolvia a mesma copy —
        # e devolver a mesma e' o que o acaso faz de vez em quando (a cena 3
        # tem 9 selos x 9 CTAs filtrados pelo orcamento, e uma colisao em doze
        # cliques e' esperada). Lente que reprova o que esta' certo treina o
        # operador a ignorar a barra inteira (§16). O que prova a FUNCAO do
        # botao e' ele devolver copy DIFERENTE ao longo de varios cliques.
        for cena in (0, 1, 2):
            sp = sortear("joe", random.Random(777), {})
            vistas = {nova_fala(sp, cena, random.Random(900 + j))
                      for j in range(20)}
            if len(vistas) < 3:
                falhas.append("[PAINEL] `nova_fala` na cena %d devolveu %d "
                              "copy(s) distinta(s) em 20 cliques — botao que "
                              "nao muda nada e' botao quebrado"
                              % (cena + 1, len(vistas)))

    # =======================================================================
    # ⭐⭐ O ALCANCE POR ENTRADA — e ele nao e' o mesmo que "18 de 18"
    # =======================================================================
    # ⛔⛔ MEDICAO QUE FALTAVA, e ela desmentia a linha de cima. O autoteste
    # imprimia `abertura 18 de 18 alcancados` e a tabela de FORMA, e as duas
    # passavam enquanto DUAS entradas de quatro palavras levavam 45% do lote:
    #     ap1=78 ap3=74 (4 palavras) contra ap2=5 ap4=9 (7 e 6)
    #     ta4=65 (5) contra ta1=3 e ta3=3 (8)
    #     im1=56 im3=60 (6) contra im2=4 (8)
    # ⭐ "Alcancada" e' um teto baixissimo: uma entrada que sai TRES vezes em
    # 400 aparece em 14% dos lotes de vinte videos, e o operador que roda dois
    # lotes nunca a ve'. Contar existencia diz `18 de 18`; contar DISTRIBUICAO
    # diz que o pool tem seis entradas vivas.
    # ⏳ DIVIDA DECLARADA E MEDIDA (alcada do operador, e' copy): o que sobra
    # depois do conserto do sorteio e' de COMPRIMENTO. Com um beat de desastre
    # de 13 palavras o orcamento da abertura+testemunha e' de 10, e a menor
    # abertura (4) com a menor testemunha (5) ja' gasta 9 — a entrada de 7
    # palavras NAO CABE em desastre nenhum desses, e nenhum sorteio conserta
    # isso. Ou as entradas longas encurtam, ou os beats longos encurtam.
    print("  ALCANCE POR ENTRADA (existir nao e' sair):")
    for eixo, pool in (("abertura", ABERTURAS),
                       ("testemunha", BEATS_TESTEMUNHA),
                       ("virada", VIRADAS), ("prova", PROVAS)):
        cont = collections.Counter(sp[eixo]["id"] for sp in specs)
        v = sorted((cont.get(x["id"], 0), x["id"]) for x in pool)
        print("     %-11s min %s=%d · max %s=%d · razao %.0fx"
              % (eixo, v[0][1], v[0][0], v[-1][1], v[-1][0],
                 float(v[-1][0]) / max(v[0][0], 1)))
        mortas = [i for n_, i in v if n_ == 0]
        if mortas:
            falhas.append("[ALCANCE] %s: %s nao sai NENHUMA vez em %d "
                          "sorteios — entrada morta que o contador de "
                          "existencia conta como viva (§35)"
                          % (eixo, mortas, len(specs)))

    # =======================================================================
    # ⭐⭐ O ALCANCE POR DESASTRE, E A DISTRIBUICAO POR CLUSTER (2026-08-21)
    # =======================================================================
    # ⛔⛔ MEDICAO NOVA, e ela existe porque o pool MULTIPLICOU POR SETE (9 ->
    # 59 -> 52 -> 62) num dia so'. Com nove entradas, "9 de 9 alcancados" era
    # quase o mesmo que distribuicao; com sessenta e dois, a media por entrada
    # cai a um setimo e uma entrada rara passa a caber inteira dentro do ruido. O
    # contador de EXISTENCIA continua acima e continua certo — ele so' nao
    # responde a pergunta que importa agora, que e' *"o operador ve' esta cena
    # num lote de trinta?"*.
    # ⚠️ O piso e' 0,4x da MEDIA e nao um numero cravado, porque o acoplamento
    # e' real: um desastre de `casal` so' cabe em 4 das 14 pessoas, e um de
    # `mulher` so' em 8 — a entrada de casal sai naturalmente menos e isso e'
    # desenho. O que 0,4x separa e' "sai menos por acoplamento" de "esta'
    # morta e o autoteste a conta como viva" (§35).
    # ⚠️ `cont_d`, `cont_cl` e `N_ALC` sao computados LA' EM CIMA, junto do
    # contador de existencia por eixo — os mesmos 2.000 sorteios servem as duas
    # medicoes e rodar o laco duas vezes so' custaria tempo.
    media = float(N_ALC) / len(DESASTRES)
    v_d = sorted((cont_d.get(d["id"], 0), d["id"]) for d in DESASTRES)
    print("  ALCANCE POR DESASTRE em %d sorteios (media %.1f · piso 0,4x = "
          "%.1f):" % (N_ALC, media, 0.4 * media))
    print("     min %s=%d (%.2fx) · max %s=%d (%.2fx)"
          % (v_d[0][1], v_d[0][0], v_d[0][0] / media,
             v_d[-1][1], v_d[-1][0], v_d[-1][0] / media))
    abaixo = [(i, n_) for n_, i in v_d if n_ < 0.4 * media]
    if abaixo:
        falhas.append("[ALCANCE] desastre: %s abaixo de 0,4x da media (%.1f) "
                      "em %d sorteios — entrada rara demais e' entrada morta "
                      "com numero de pool" % (abaixo, media, N_ALC))
    print("  DISTRIBUICAO POR CLUSTER (a proveniencia, contada no sorteio):")
    for k in sorted(cont_cl):
        n_pool = len([d for d in DESASTRES
                      if d.get("cluster", "LIDO (leitura otica)") == k])
        print("     %-22s %4d  %2d%%  (%d entradas no pool)"
              % (k, cont_cl[k], 100 * cont_cl[k] // N_ALC, n_pool))

    # =======================================================================
    # ⭐⭐ O QUE ESTA EXPANSAO EXISTE PARA CONSERTAR — ANTES e DEPOIS
    # =======================================================================
    # ⛔⛔ O pool de desastres nao cresceu por gosto de variedade: ele cresceu
    # porque as entradas LONGAS de abertura e de testemunha estavam MORTAS, e
    # a causa era aritmetica de ORCAMENTO. Com nove desastres, seis deles
    # traziam beats de 11 a 15 palavras; sobrando 10 para abertura+testemunha,
    # a entrada de 7 ou 8 palavras nao cabia em quase nada.
    # ⭐ MEDIDO NAS MESMAS 400 SEEDS, antes da expansao (commit 52a1b36):
    #     ABERTURAS         min di3=2  · max ap1=66 · razao 33x
    #     BEATS_TESTEMUNHA  min de3=4  · max ri4=91 · razao 23x
    # Os dois numeros sao impressos lado a lado abaixo. ⛔ Se o minimo nao
    # subir, a expansao entregou variedade de CENA e falhou no que ela existe
    # para consertar, e a lente tem de dizer isso em vez de aplaudir o
    # `59 de 59 alcancados`.
    ANTES = {"abertura": ("di3", 2, "ap1", 66), "testemunha": ("de3", 4,
                                                               "ri4", 91)}
    print("  ⭐ O QUE A EXPANSAO EXISTE PARA CONSERTAR (mesmas 400 seeds):")
    for eixo, pool in (("abertura", ABERTURAS),
                       ("testemunha", BEATS_TESTEMUNHA)):
        cont = collections.Counter(sp[eixo]["id"] for sp in specs)
        v = sorted((cont.get(x["id"], 0), x["id"]) for x in pool)
        a_id, a_n, a_mx, a_nx = ANTES[eixo]
        print("     %-11s ANTES min %s=%d (razao %dx)  ->  DEPOIS min %s=%d "
              "(razao %.0fx)"
              % (eixo, a_id, a_n, a_nx // max(a_n, 1), v[0][1], v[0][0],
                 float(v[-1][0]) / max(v[0][0], 1)))
        print("                 a entrada que estava morta, `%s`: %d -> %d"
              % (a_id, a_n, cont.get(a_id, 0)))
        if v[0][0] <= a_n:
            falhas.append("[EXPANSAO] %s: o alcance MINIMO nao subiu "
                          "(%d antes, %d depois) — o pool de desastres "
                          "cresceu sete vezes e a entrada longa continua sem "
                          "caber; a expansao falhou no que existe para "
                          "consertar" % (eixo, a_n, v[0][0]))

    # =======================================================================
    # ⭐⭐ A TRAVA DE FORMAS — o par desastre x testemunha, entrada por entrada
    # =======================================================================
    # ⛔ Com 59 desastres declarando `formas` a mao, um rotulo errado nao
    # aparece no sorteio: ele aparece na FALA, sobre uma imagem que o
    # desmente. Duas coisas sao cobradas aqui e as duas por varredura de POOL,
    # nao por amostra:
    #   1. toda forma declarada TEM entrada em `BEATS_TESTEMUNHA` — forma sem
    #      beat e' desastre com um rotulo que nunca vira fala;
    #   2. nenhuma entrada declara `silencio` com riso escrito no `test` (nem
    #      no `mov`, nem no `audio`) sem a variante muda — a RU16 pega isso por
    #      video, esta pega no pool, antes de o video existir.
    # ⚠️ O `\blaugh(...)\b` com FRONTEIRA DE PALAVRA e' obrigatorio: sem ela
    # `grinding` (uma porta giratoria travando, um coturno no degrau de
    # madeira) casa com `grin` e a lente reprova duas cenas mudas corretas.
    _POR_FORMA = collections.Counter(t["forma"] for t in BEATS_TESTEMUNHA)

    def _forma_sem_beat(d_):
        return [f for f in d_["formas"] if not _POR_FORMA.get(f)]

    def _silencio_com_riso(d_):
        if "silencio" not in d_["formas"]:
            return []
        sujos = []
        for campo, alt in (("test", "test_q"), ("mov", "mov_q"),
                           ("audio", "audio_q")):
            base_ = d_.get(alt, d_[campo])
            if re.search(r"\blaugh(s|ing|ed)?\b", base_, re.I):
                sujos.append(campo)
        return sujos

    n_sil = 0
    for d_ in DESASTRES:
        vazias = _forma_sem_beat(d_)
        if vazias:
            falhas.append("[FORMAS] DESASTRE %s declara %s e BEATS_TESTEMUNHA "
                          "nao tem uma entrada dessa forma — rotulo que nunca "
                          "vira fala" % (d_["id"], vazias))
        sujos = _silencio_com_riso(d_)
        if sujos:
            falhas.append("[FORMAS] DESASTRE %s declara `silencio` e o %s "
                          "ainda ri — a fala diria *nobody said a word* "
                          "sobre gente rindo em quadro" % (d_["id"], sujos))
        n_sil += ("silencio" in d_["formas"])
    print("  TRAVA DE FORMAS: %d desastres varridos · %d comportam `silencio` "
          "e nenhum ri em quadro" % (len(DESASTRES), n_sil))
    # ⚠ E A DIAGNOSE DE POR QUE UMA FORMA E' RARA MORA AQUI, nao no palpite:
    # depois da expansao a forma mais escassa e' `dedo`, e a causa e' que ela
    # exige VIZINHO em quadro (os tres beats dizem `neighbour(s)`) e a
    # verificacao de coerencia a tirou de quatro cenas do cluster A onde o
    # publico e' cliente de balcao, convidado de festa ou PARENTE. Decisao
    # certa, e ela custa alcance: o numero abaixo e' o que o operador olha
    # antes de mandar escrever cena nova.
    # ⛔⛔ O GUARDA DE `room`, COBRADO NO POOL E NA SAIDA. Ver o bloco
    # `_beat_cabe`: quatro beats dizem `room` e so' tres deles (os de
    # `plateia`) tinham porteiro. ⚠️ Medido nas MESMAS 400 seeds: 7 videos
    # ANTES da expansao e 19 DEPOIS diziam `and the whole room laughed out
    # loud` sobre ponto de onibus, patio de posto e rua fechada.
    sem_flag = [d["id"] for d in DESASTRES if "interior" not in d]
    if sem_flag:
        falhas.append("[SALA] %s sem o campo `interior` — o guarda de "
                      "`room` cede em silencio para quem nao o declara"
                      % sem_flag[:6])
    fora = [d["id"] for d in DESASTRES
            if "plateia" in d["formas"] and not d.get("interior")]
    if fora:
        falhas.append("[SALA] %s declara `plateia` e nao e' interior — "
                      "os tres beats da forma dizem `room`" % fora)
    n_sala = 0
    for sp in specs:
        if (_RX_SALA.search(sp["testemunha"]["txt"])
                and not sp["desastre"].get("interior")):
            n_sala += 1
            falhas.append("[SALA] o beat %s diz `room` sobre %s, que e' ao ar "
                          "livre — teste WTF na primeira sentenca"
                          % (sp["testemunha"]["id"], sp["desastre"]["id"]))
    print("  GUARDA DE `room`: %d de %d desastres sao interior · %d de %d "
          "videos dizem `room` ao ar livre (era 7 de 400 antes da expansao)"
          % (len([d for d in DESASTRES if d.get("interior")]), len(DESASTRES),
             n_sala, len(specs)))
    # ⛔ CONTROLE NEGATIVO: o guarda tem de RECUSAR `ri2` num quadro aberto e
    # ACEITAR o mesmo `ri2` num fechado, e nunca tocar num beat sem `room`.
    _ri2 = _por_id(BEATS_TESTEMUNHA, "ri2")
    _ri1 = _por_id(BEATS_TESTEMUNHA, "ri1")
    _aberto = next(d for d in DESASTRES
                   if not d["interior"] and "riso" in d["formas"])
    _fechado = next(d for d in DESASTRES
                    if d["interior"] and "riso" in d["formas"])
    for rot, t_, d_, deve in (("SALA ri2 ao ar livre", _ri2, _aberto, False),
                              ("SALA ri2 em interior", _ri2, _fechado, True),
                              ("SALA ri1 ao ar livre (sem `room`)", _ri1,
                               _aberto, True),
                              ("SALA forma que nao cabe", _ri1,
                               next(d for d in DESASTRES
                                    if "riso" not in d["formas"]), False)):
        if _beat_cabe(t_, d_) != deve:
            falhas.append("CONTROLE %s: o guarda %s (esperado: %s)"
                          % (rot, "recusou" if deve else "aceitou",
                             "aceitar" if deve else "recusar"))
    print("     desastres por forma de testemunha (o teto de cada forma):")
    for f_ in FORMAS_TESTEMUNHA:
        n_ = len([d for d in DESASTRES if f_ in d["formas"]])
        print("        %-11s %2d de %2d desastres  (%2d%% do pool)"
              % (f_, n_, len(DESASTRES), 100 * n_ // len(DESASTRES)))

    # ⛔ CONTROLES NEGATIVOS DA TRAVA — lente que nunca acusou e' lente que
    # ninguem sabe se funciona. Os tres plantios sao os defeitos EXATOS que ela
    # existe para pegar, mais o falso positivo que ja' custou uma varredura.
    _d_sil = next(d for d in DESASTRES if "silencio" in d["formas"])
    _d_sem = next(d for d in DESASTRES if "silencio" not in d["formas"])
    for rotulo, fn_, alvo, deve in (
            ("FORMAS forma inexistente", _forma_sem_beat,
             dict(_d_sem, formas=tuple(_d_sem["formas"]) + ("gargalhada",)),
             True),
            ("FORMAS limpo", _forma_sem_beat, _d_sem, False),
            ("FORMAS silencio com riso no test", _silencio_com_riso,
             dict(_d_sil, formas=("silencio",),
                  test=_d_sil["test"] + " Two of them are laughing.",
                  test_q=_d_sil.get("test_q", _d_sil["test"])
                  + " Two of them are laughing."), True),
            ("FORMAS silencio com riso no audio", _silencio_com_riso,
             dict(_d_sil, formas=("silencio",),
                  audio_q=_d_sil.get("audio_q", _d_sil["audio"])
                  + ", and two people laughing"), True),
            ("FORMAS silencio limpo", _silencio_com_riso, _d_sil, False),
            # ⚠️ O FALSO POSITIVO QUE JA' FOI PAGO: `grinding` casa com `grin`
            # sem a fronteira de palavra, e duas cenas mudas corretas
            # (`a revolving door mechanism grinding to a stop`, `boots grinding
            # on wooden steps`) seriam reprovadas por um audio que nao ri.
            ("FORMAS nao acusa `grinding`", _silencio_com_riso,
             dict(_d_sil, formas=("silencio",),
                  audio_q="a door mechanism grinding to a stop"), False)):
        if bool(fn_(alvo)) != deve:
            falhas.append("CONTROLE %s: a trava %s (esperado: %s)"
                          % (rotulo, "acusou" if not deve else "passou",
                             "acusar" if deve else "passar"))

    # =======================================================================
    # ⭐⭐ O AUTOTESTE SOB AS TRAVAS DO PAINEL — e ele so' rodava LIVRE
    # =======================================================================
    # ⛔ `sortear` livre nao e' o modo em que o operador roda lote: ele
    # pre-seleciona `sexo` e `rosto_ato1` no painel. Medido, a pre-selecao MUDA
    # a distribuicao (com `sexo=homem` a forma `apresentacao` ia a 48% e `de3`
    # saia ZERO vezes), e nenhuma das lentes tinha visto um unico video desse
    # modo.
    for sexo_ in ("livre", "mulher", "homem", "casal"):
        for rosto_ in ("livre", "oculto", "visivel"):
            ruins = 0
            for k in range(30):
                sp = sortear(pags[k % len(pags)], random.Random(3000 + k), {},
                             {"sexo": sexo_, "rosto_ato1": rosto_})
                ruins += len([1 for nv, _ in lint(sp, montar(sp))
                              if nv == "ERRO"])
            if ruins:
                falhas.append("[TRAVAS] sexo=%s rosto=%s: %d ERRO em 30 "
                              "videos — o painel roda travado e o autoteste "
                              "so' rodava livre" % (sexo_, rosto_, ruins))

    # =======================================================================
    # ⭐⭐ RU13 POR FORCA BRUTA — a classe inteira, nao o par que ja' apareceu
    # =======================================================================
    # ⛔⛔ O autoteste usa 400 seeds FIXAS, o que faz dele REGRESSAO e nao
    # amostra: o par `vi7` x `vd2` (`a year on` + `Eight months`) saia 1 vez em
    # 3.000 sorteios livres e 6 vezes em 1.440 videos sob as travas do painel,
    # e nas seeds 0..399 ele NUNCA aparece — o autoteste imprimia `0 ERRO`
    # para sempre sobre um defeito vivo. A varredura abaixo custa
    # milissegundos e fecha a CLASSE: nenhum trio de VIRADA x REMEDIO x PROVA,
    # para nenhuma das catorze pessoas, pode trazer dois prazos.
    dois = []
    for p_ in PESSOAS:
        d_ = _dic({"pessoa": p_})
        for v_ in VIRADAS:
            for r_ in REMEDIOS:
                for x_ in PROVAS:
                    fala = "%s %s %s" % (_r(v_["txt"], d_), _r(r_["txt"], d_),
                                         _r(x_["txt"], d_))
                    if len({z.group(0).lower()
                            for z in _RX_DURACAO.finditer(fala)}) > 1:
                        dois.append((p_["id"], v_["id"], r_["id"], x_["id"]))
    print("  RU13 forca bruta: %d trios de %d com DOIS prazos · o sorteio "
          "bloqueia %s" % (len(dois), len(PESSOAS) * len(VIRADAS)
                           * len(REMEDIOS) * len(PROVAS),
                           "todos" if dois else "-"))
    # ⚠️ A varredura acusa o POOL (os pares existem no papel); quem os impede
    # e' `_sortear_plano`. A prova de que ele impede e' a contagem abaixo, e e'
    # ela que reprova o motor.
    vivos = 0
    for i in range(600):
        sp = sortear(pags[i % len(pags)], random.Random(70000 + i), {})
        vivos += len([1 for nv, msg in lint(sp, montar(sp))
                      if nv == "ERRO" and "RU13" in msg])
    if vivos:
        falhas.append("[RU13] %d de 600 sorteios em seeds NOVAS trazem dois "
                      "prazos — o filtro do sorteio nao esta' pegando" % vivos)

    # =======================================================================
    # ⭐⭐ O CADEADO E O BOTAO `trocar`, MEDIDOS EIXO POR EIXO
    # =======================================================================
    # ⛔⛔ A MEDICAO QUE FALTAVA E QUE ACHOU O EIXO MORTO. `testemunha` estava
    # em `EIXOS_UI` e em `EIXOS_TRAVAVEIS`, o painel desenhava o cadeado e o
    # botao — e `travas["testemunha"]` nunca era lida em `sortear`. Medido: o
    # cadeado era honrado em 23 de 200 sorteios (11%, o acaso de 1 em 13
    # formas cabiveis) e a escolha do operador no botao `trocar` sobrevivia em
    # 4 de 120 cliques (3%). ⚠️ E a unica lente que pegaria isso — a de painel
    # honesto — estava desligada de proposito para este eixo em
    # `IGNORA_PAINEL`, por uma razao CERTA (o valor e' um molde com slot, e a
    # lente acusaria 400 de 400 videos corretos). Excecao certa que deixa um
    # buraco pede lente NOVA, nao lente removida.
    # ⚠️ O piso e' 85% e nao 100% porque os acoplamentos sao reais: uma
    # testemunha travada cede quando a forma nao cabe no desastre travado, e
    # uma peca cede quando o sexo da pessoa travada nao a comporta. O que o
    # piso separa e' "cede as vezes, por acoplamento" de "nunca foi lido".
    print("  CADEADO e BOTAO `trocar` (o painel, simulado):")
    for chave, nome_pool in ((e[0], e[2]) for e in EIXOS_UI):
        pool = globals()[nome_pool]
        honra = 0
        for i in range(120):
            base = sortear(pags[i % len(pags)], random.Random(4000 + i), {})
            s2 = sortear(pags[i % len(pags)], random.Random(5000 + i), {},
                         {chave: base[chave]["id"]})
            honra += (s2[chave]["id"] == base[chave]["id"])
        sobrevive = 0
        for k in range(120):
            sp = sortear(pags[k % len(pags)], random.Random(6000 + k), {})
            opcoes = [x for x in pool if x != sp[chave]]
            escolhido = random.Random(k).choice(opcoes)
            sp[chave] = escolhido
            if chave == "pessoa":
                sp["idade"] = sp["pessoa"]["idade"]
            fn_ = EIXOS_QUE_MEXEM_NA_COPY.get(chave)
            if fn_:
                fn_(sp, random.Random(k))
            sobrevive += (sp[chave]["id"] == escolhido["id"])
        print("     %-11s cadeado %3d/120 · `trocar` sobrevive %3d/120"
              % (chave, honra, sobrevive))
        for rot, n_ in (("cadeado", honra), ("`trocar`", sobrevive)):
            if n_ < 102:
                falhas.append("[PAINEL] eixo %r: %s honrado em %d de 120 — "
                              "botao que promete e entrega outra coisa e' pior "
                              "que botao ausente (GO21)" % (chave, rot, n_))

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
    # ⚠️ MESMO REMENDO DO `medir_copy16.py`, e pela mesma razao medida: o
    # console do Windows e' cp1252 e os marcadores da doutrina nao cabem nele.
    # Sem isto o motor morre com UnicodeEncodeError ANTES de imprimir o
    # primeiro bloco — e morre so' no caminho em que ha' algo a dizer.
    for _f in (sys.stdout, sys.stderr):
        try:
            _f.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass
    ap = argparse.ArgumentParser(description=TITULO)
    ap.add_argument("--pagina", choices=sorted(ETNIA), default="joe")
    ap.add_argument("--n", type=int, default=1)
    ap.add_argument("--seed", type=int)
    ap.add_argument("--sexo", choices=list(SEXOS))
    ap.add_argument("--rosto", choices=["oculto", "visivel"],
                    help="o rosto da pessoa no ato 1 — o EIXO da hipotese; o "
                         "padrao e' 50/50")
    ap.add_argument("--desastre", choices=[d["id"] for d in DESASTRES])
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--autoteste", action="store_true")
    a = ap.parse_args()

    if a.autoteste:
        return autoteste()

    led = _carregar_ledger()
    rng = random.Random(a.seed)
    travas = {}
    if a.sexo:
        travas["sexo"] = a.sexo
    if a.rosto:
        travas["rosto_ato1"] = a.rosto
    if a.desastre:
        travas["desastre"] = a.desastre
    # ⛔⛔ VIDEO COM ERRO NAO CHEGA A SER IMPRESSO, e ate' 2026-08-21 chegava.
    # A ordem era: imprimir os sete blocos, DEPOIS rodar o linter, DEPOIS
    # imprimir os ERROS. Quando um disparava, o operador ja' tinha o roteiro
    # inteiro na tela para copiar — e o unico sinal era uma linha depois do
    # ultimo bloco, abaixo da rolagem. E' o padrao *"agente reprovado
    # rodavel"* dentro do proprio motor: quem gera o lote nao le' o rodape.
    # ⭐ O conserto e' re-sortear com teto de tentativas e imprimir so' o que
    # passou. ⚠️ O teto existe porque um pool novo pode nascer com um defeito
    # em 100% dos sorteios, e ai' o motor tem de DIZER isso em vez de girar
    # para sempre — nesse caso ele imprime o video E o diagnostico, com o
    # aviso na frente, que e' o unico caso em que ver o bloco defeituoso
    # ajuda.
    TENTATIVAS = 12
    for _ in range(a.n):
        for tentativa in range(TENTATIVAS):
            s = sortear(a.pagina, rng, led, travas)
            b = montar(s)
            ach = lint(s, b)
            ruins = [x for x in ach if x[0] == "ERRO"]
            if not ruins:
                break
        if ruins:
            print("=" * 70)
            print("[ABORTADO] %d sorteios seguidos com ERRO de lente — o "
                  "defeito nao e' de sorteio, e' de POOL. O video abaixo e' o "
                  "ultimo, impresso so' para diagnostico:" % TENTATIVAS)
            for nivel, msg in ruins:
                print("   [%s] %s" % (nivel, msg))
            print("=" * 70)
        print("=" * 70)
        print(resumo_pt(s))
        if tentativa:
            print("(%d re-sorteio(s) ate' um video passar nas lentes)"
                  % tentativa)
        print("=" * 70)
        for k in ("BLOCO 0 (REF)",) + IMAGENS + TAKES:
            print("\n%s\n" % b[k])
        for nivel, msg in ach:
            print("[%s] %s" % (nivel, msg))
        if not a.dry_run:
            _gravar_ledger(led, s)
    return 0


if __name__ == "__main__":
    sys.exit(main())
