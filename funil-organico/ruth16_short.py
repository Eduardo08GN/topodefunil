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
  DESASTRES   9 · o lugar + as testemunhas + o enquadramento JUNTOS numa
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
  · **`RU3`, `RU4` e `RU5` cresceram**: peca fantasma, rosto no `porte` com a
    camera de costas, e o bloco INTEIRO em vez de dois tercos dele.
  · **O sorteio mudou de regra** (`_sortear_plano`): a entrada e' sorteada
    ANTES do orcamento, e o prazo virou exclusivo por fala.
  · **O painel virou medicao**: cadeado e botao `trocar` contados eixo por eixo
    no autoteste, mais uma varredura sob as travas de `sexo` e `rosto_ato1`.
  · **O motor entrou nos medidores** de que estava fora (quatro dos sete).
  · **`main()` nao imprime mais video reprovado**: re-sorteia ate' 12 vezes.

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
  C. ⏳ **AS ENTRADAS LONGAS DE COPY CABEM EM POUCOS DESASTRES.** O conserto do
     sorteio nivelou o que dava para nivelar (a `vi7` foi de 6 para 31 em 400,
     a `im2` de 4 para 10), e o que sobra e' aritmetica: com um beat de
     desastre de 13 palavras, o orcamento de abertura+testemunha e' **10**, e a
     menor abertura (4) com a menor testemunha (5) ja' gasta 9. A entrada de 7
     ou 8 palavras **nao cabe em desastre nenhum desses**, e nenhum sorteio
     conserta isso. ⭐ Saidas, as duas de copy: encurtar as entradas longas, ou
     encurtar os beats de desastre longos. O autoteste agora IMPRIME a razao
     max/min por entrada, para a divida ter numero.
  D. ⏳ **4 DAS 14 PESSOAS SAO ANONIMAS E ABREM EM PRONOME** (122 de 400
     videos): *"This was her before"*, *"Nothing was simple for them"*. E'
     desenho declarado e verbatim do v28 — e e' tambem o unico lugar do motor
     onde o take 1 nao tem referente proprio. Vale a pena o operador olhar um
     desses videos na tela antes de o lote sair.

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
# ⭐⭐ OS NOVE DESASTRES — o eixo principal
# ===========================================================================
# ⛔ CADA ENTRADA ARRASTA O LUGAR + AS BEATS_TESTEMUNHA + O ENQUADRAMENTO JUNTOS.
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
     "cen": "the side wall of a two-storey American house on a bright summer "
            "day, cream lap siding with a rough rectangular hole torn open "
            "through the upper floor, splintered raw framing and loose boards "
            "hanging down over the siding, a black articulated hydraulic crane "
            "arm crossing the top of the frame with a red hook block on a "
            "chain, a red fire engine at the kerb, a wooden privacy fence and "
            "a mowed lawn below",
     "acao": "wide yellow nylon lifting slings have swung out of the torn "
             "opening and the strap has given way at the top of the swing, so "
             "the body in the sling is down on the grass below, tangled in the "
             "webbing, with wood splinters scattered around it",
     "test": "on the lawn, four neighbours have come across from the next "
             "house and stand in a loose ring a few paces back, close enough "
             "to read: two of them openly laughing with their heads tipped "
             "together, one older woman with a flat hand over her mouth, and a "
             "man in a ball cap with his arm out pointing straight down at the "
             "fallen body",
     "mov": "As the line begins the neighbours in the ring rock back and two "
            "of them start laughing out loud. Halfway through the line the man "
            "in the ball cap pushes his pointing arm further out and says "
            "something to the woman beside him. As the line ends the loose "
            "webbing settles on the grass and the ring closes half a step",
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
     "cen": "the cluttered living room of an old single-wide farmhouse in "
            "winter, a cream popcorn ceiling, a brass ceiling fan with dusty "
            "blades, tan wood-panel walls, a brown leather sofa, a floral area "
            "rug over speckled linoleum, a lace-curtained window with flat "
            "grey daylight, and a polished steel shop hoist with an orange "
            "hydraulic ram standing in the middle of the floor",
     "acao": "black nylon lifting straps run under the arms and hips of the "
             "body hanging upright in the sling a few inches above "
             "the rug, both hands gripping the straps, while two firefighters "
             "in tan bunker gear steady the mast",
     "test": "crowded into the doorway behind the hoist stand four neighbours "
             "who came in off the street and never left: two of them laughing "
             "with their shoulders shaking, one teenager grinning wide, and an "
             "older man with both hands on the door frame staring straight at "
             "the sling",
     "mov": "As the line begins the sling turns a few degrees and the "
            "neighbours in the doorway crane forward. Halfway through the line "
            "two of them break into open laughter and the teenager covers his "
            "grin. As the line ends the straps creak and the ceiling fan turns "
            "once overhead",
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
     "cen": "the inside of a small American nail salon, sage-green walls, a "
            "carved wooden sign high on the wall, racks of nail polish bottles "
            "in tight rainbow rows, a white drop ceiling with long fluorescent "
            "panels, three glass pendant lamps, beige tile floor and a long "
            "receding row of tan leather pedicure thrones with glass foot "
            "basins and rolled white towels",
     "acao": "the carved wooden armrest of the front pedicure throne has split "
             "and torn loose and the leather seat has dropped off its "
             "pedestal, so she is down on the tile beside it with both bare "
             "feet still wet and the foot basin tipped over",
     "test": "the six women seated along the pedicure row have all twisted "
             "round in their chairs to look, two of them laughing behind their "
             "hands, and two nail technicians in black work polos and white "
             "latex gloves stand over her without moving",
     "mov": "As the line begins the last two heads in the row turn round. "
            "Halfway through the line two of the seated women laugh behind "
            "their hands and one leans over to say something. As the line ends "
            "the whole room has gone quiet again and nobody moves",
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
     "cen": "an outdoor concrete wheelchair ramp climbing to the glass main "
            "entrance of a large city hospital on a bright morning, a pale "
            "limestone facade with dark tinted window bands, a dark canopy "
            "over the automatic sliding doors, grey steel pipe handrails down "
            "both sides of the ramp, a black planter with a clipped shrub and "
            "a parked SUV at street level behind the railing",
     "acao": "halfway up the ramp the wheelchair has tipped onto its side and "
             "dumped one of them onto the concrete, and the other is down "
             "flat on the slope beside it with the legs folded under the "
             "weight, one slip-on shoe thrown clear a few feet away",
     "test": "six people who were waiting outside the entrance have stopped on "
             "the steps to watch: two of them laughing with their heads "
             "together, a young man in a delivery uniform standing still with "
             "his mouth open, and an older couple who reach a hand halfway out "
             "and then pull it back",
     "mov": "As the line begins the two on the steps start laughing and the "
            "older couple half-reach toward the ramp. Halfway through the line "
            "the wheelchair rocks once on its side and nobody comes down the "
            "steps. As the line ends the group on the steps closes together "
            "and keeps watching",
     "cam": "The shot is taken from a few feet behind the group at hip height, "
            "tilted up along the slope of the ramp so the fallen bodies sit low "
            "in the frame and the entrance sits high in it",
     "luz": "Flat overcast midday daylight, soft shadowless light on pale "
            "concrete, cool neutral white balance.",
     "audio": "shoes scuffing concrete, laboured breathing, the metallic "
              "clatter of the wheelchair frame on the ground and two people "
              "laughing near the doors"},

    {"id": "escada_varanda", "curto": "a escada da varanda cede",
     "v": "v49", "sexos": ("casal",),
     "formas": ("impotencia", "riso", "dedo", "juizo"),
     "cen": "the front of a modest American house with pale grey clapboard "
            "siding, a weathered wooden porch with a square post and a slatted "
            "rail, a white-framed window and a black wall lantern beside the "
            "door, a run of thick weathered wooden steps down to a gravel "
            "driveway, green shrubs and an empty folding wheelchair parked at "
            "the foot of the steps",
     "acao": "one wooden tread has split clean through halfway up the flight "
             "and both of them are down, one sitting back on the "
             "broken step with both hands still on the rail and the other flat "
             "on the driveway below, pale wood splinters scattered across the "
             "gravel",
     "test": "three neighbours have come out onto the sidewalk at the end of "
             "the driveway and stand there watching: a man with his arms folded "
             "laughing openly, a woman beside him standing still and simply "
             "staring, and a third with one arm out pointing at the broken "
             "steps",
     "mov": "As the line begins the man on the sidewalk laughs and says "
            "something to the woman next to him. Halfway through the line the "
            "third neighbour pushes the pointing arm further out toward the "
            "broken tread. As the line ends the two on the ground are still "
            "down and the group on the sidewalk has not moved",
     "cam": "The shot is taken from driveway height a few paces back, angled "
            "up the flight so both fallen bodies and the neighbours on the "
            "sidewalk sit in the same vertical frame",
     "luz": "Hard midday summer sun from the left, bleached wood, deep shadow "
            "under the porch roof, bright sky.",
     "audio": "a loud splintering crack, wood shards skittering on gravel, two "
              "people groaning and laughter carrying from the sidewalk"},

    {"id": "carro_cafe", "curto": "a queda do carro com o cafe' derramado",
     "v": "v24", "sexos": ("mulher", "homem"),
     "formas": ("riso", "dedo", "juizo", "impotencia"),
     "cen": "a residential driveway paved in stamped brick-pattern concrete in "
            "warm terracotta and sand tones in the late afternoon, a white "
            "minivan filling one side of the frame with its side sliding door "
            "rolled fully open onto dark grey captain's chairs, a red painted "
            "kerb line along the far edge and a mowed lawn beyond",
     "acao": "a foot has slipped coming down out of the open sliding door, the "
             "takeaway coffee has flown out of the hand and soaked the whole "
             "front of the clothing, and the body is down on the brick pavers "
             "with both arms braced and a brown puddle spreading across "
             "the stones",
     "test": "three neighbours are on the sidewalk right at the end of the "
             "driveway, close enough to read: two teenagers openly laughing "
             "with their heads tipped back and a woman with a dog lead in one "
             "hand and the other flat over her mouth, all three stopped and "
             "watching",
     "mov": "As the line begins the two teenagers on the sidewalk break out "
            "laughing. Halfway through the line the woman with the dog lead "
            "takes half a step forward and stops. As the line ends the coffee "
            "puddle spreads another inch and nobody comes up the driveway",
     "cam": "The shot is taken from beside the open sliding door at chest "
            "height, angled down about thirty degrees onto the pavers, wide "
            "enough to hold the fallen body, the spilled coffee and the group "
            "on the sidewalk",
     "luz": "Hard low late-afternoon sun from the right, strong warm key, long "
            "dark shadows raked across the brick pavers, high contrast.",
     "audio": "a plastic lid clattering on brick, strained breathing, a dog "
              "barking once and two young voices laughing"},

    {"id": "cctv_calcada", "curto": "a queda na propria garagem",
     "v": "v38", "sexos": ("casal",),
     # ⚠️ SEM `plateia` pela mesma razao (garagem ao ar livre), e sem
     # `silencio` porque a imagem tem um vizinho GRITANDO — a fala nao pode
     # dizer que ninguem falou nada.
     "formas": ("dedo", "riso", "juizo", "impotencia"),
     "cen": "the wide concrete driveway of a new-build suburban development at "
            "midday, grey vinyl-sided two-storey houses with stone-front "
            "gables and dark garage doors across the street, mowed green "
            "lawns, a young maple in a mulch bed, a clean asphalt street, a "
            "dark navy SUV parked at one side and a black coach lantern on the "
            "garage wall",
     "acao": "both of them are face down on their own driveway, tangled "
             "together and pointing in opposite directions, arms out and "
             "unable to push themselves up, while a black three-wheel "
             "stroller with a small child strapped into it rolls away from "
             "them down the slope toward the street",
     "test": "four neighbours have closed into a ring around them on the "
             "concrete: a bearded man in a ball cap with his arms crossed "
             "laughing, a blonde woman beside him laughing too, a heavy man in "
             "a polo jabbing a pointed finger down at them and shouting, and an "
             "elderly woman against the garage with one hand over her mouth",
     "mov": "As the line begins the man in the polo jabs his finger down and "
            "starts shouting. Halfway through the line the bearded man and the "
            "blonde woman laugh out loud and the stroller rolls another few "
            "feet. As the line ends nobody in the ring has bent down to help",
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
     "cen": "the physical-therapy room of a small American medical clinic, "
            "beige painted walls, black-framed anatomical charts of the "
            "muscular and skeletal systems, a wall-mounted ultrasound cart "
            "with a white monitor, a white drop ceiling with recessed "
            "fluorescent panels, wide plank wood-look vinyl flooring and a "
            "pale oak practice staircase with a varnished handrail",
     "acao": "the practice staircase is being hauled one tread at a time on "
             "two grey forearm crutches with the whole weight hanging off the "
             "grips, the neck and forearms flushed deep red and the breath "
             "coming hard, an empty black folding wheelchair waiting at the "
             "foot of the stairs",
     "test": "six other patients waiting on the bench along the far wall have "
             "all stopped to watch: two of them leaning together laughing "
             "quietly, one young man openly staring, and an older woman who "
             "looks away and then back again",
     "mov": "As the line begins one crutch tip skids on the tread and the "
            "whole bench of patients looks up. Halfway through the line two of "
            "them lean together and laugh quietly. As the line ends the climb "
            "stalls one step from the top and the room stays quiet",
     "cam": "The shot is taken from the top of the practice staircase at chest "
            "height, angled slightly down along the treads so the climb fills "
            "the lower frame and the waiting bench sits behind it",
     "luz": "Flat cool overhead fluorescent light, no shadow direction, a "
            "faint greenish institutional cast.",
     "audio": "rubber crutch tips knocking on wood, laboured breathing, a low "
              "clinic hum and two people laughing quietly",
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
     "cen": "the living room of an ordinary suburban house, plain white-grey "
            "walls, a tall window with white venetian blinds letting in flat "
            "daylight, a beige fabric sectional sofa with loose cushions, a "
            "rectangular glass-top coffee table on a thin dark metal frame in "
            "the foreground and a grey geometric-pattern area rug beneath it",
     "acao": "two firefighters in tan bunker gear with yellow reflective "
             "stripes have taken a forearm each and are hauling the body up "
             "out of the sagging sofa cushions, the head tipped back "
             "and the shoulders sagging under the grip",
     "test": "the front door stands open behind the sofa and five neighbours "
             "have crowded into the doorway to watch: three of them laughing "
             "with their heads together, one leaning in over the others to "
             "stare, and a woman with both hands at her mouth",
     "mov": "As the line begins the two firefighters take the weight and the "
            "neighbours in the doorway press forward. Halfway through the line "
            "three of them laugh out loud and one says something to the others. "
            "As the line ends the body is half off the cushions and nobody in "
            "the doorway looks away",
     "cam": "The shot is taken from across the coffee table at seated chest "
            "height, level and straight on, wide enough to hold the sofa, both "
            "firefighters and the crowded doorway behind them",
     "luz": "Cool flat daylight from the window at one side, grey and "
            "shadowless, a faint blue cast on the room.",
     "audio": "gear rustling, boots scuffing the rug, a strained breath and "
              "several people laughing in the doorway"},
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
# ⛔⛔ O CONTRATO DO `porte`, e as TRES clausulas nasceram de defeito MEDIDO no
# bloco montado (2026-08-21), nao de gosto:
#   1. ⛔ NAO REPETE O PESO. A primeira sintagma do IMAGE 01 ja' diz *"a very
#      heavy 46-year-old woman"*; o `porte` dizia `very heavy,` outra vez na
#      frase seguinte. Medido: 100% dos blocos tinham DUAS ou mais ocorrencias
#      de `very heavy`, 76% tinham tres e 32% tinham QUATRO — quatro corpos
#      nomeados para duas pessoas. Sujeito reintroduzido com sintagma novo e'
#      licenca para o gerador desenhar mais um. Lente `RU14`.
#   2. ⛔ NAO CITA ROSTO — nem `face`, nem `mouth`, nem `eyes`, nem expressao.
#      Com `rosto_oculto` a camera esta' ATRAS da pessoa, e a frase seguinte
#      dizia *"flushed deep red across the face"*. Medido: 108 dos 593
#      ocultos, 9% de TODOS os videos. Contradicao o gerador resolve virando o
#      rosto para a lente — que e' matar o modo inteiro. Lente `RU4`.
#   3. ⛔ NAO NOMEIA PECA DE ROUPA. A peca e' do eixo `ROUPAS` e de mais
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
     "porte": "well past three hundred pounds, moving slowly and carrying "
              "the weight low"},
    {"id": "helen", "curto": "Helen · 57 · sozinha", "v": "v39",
     "nome": "Helen", "sexo": "mulher", "idade": 57,
     "ref": "Helen", "suj": "Helen", "obj": "Helen", "poss": "her",
     "poss_nome": "Helen's", "vida": "life",
     "porte": "around three hundred pounds, short of breath and flushed "
              "deep red across the neck and forearms"},
    {"id": "betsy", "curto": "Betsy · 48 · sozinha", "v": "v46",
     "nome": "Betsy", "sexo": "mulher", "idade": 48,
     "ref": "Betsy", "suj": "Betsy", "obj": "Betsy", "poss": "her",
     "poss_nome": "Betsy's", "vida": "life",
     "porte": "wide through the shoulders and hips, filling the whole width "
              "of the seat"},
    {"id": "margaret", "curto": "Margaret · 41 · sozinha", "v": "v47",
     "nome": "Margaret", "sexo": "mulher", "idade": 41,
     "ref": "Margaret", "suj": "Margaret", "obj": "Margaret", "poss": "her",
     "poss_nome": "Margaret's", "vida": "life",
     "porte": "close to four hundred pounds, barefoot and unable to take "
              "her own weight"},
    {"id": "betty", "curto": "Betty · 45 · sozinha", "v": "v50",
     "nome": "Betty", "sexo": "mulher", "idade": 45,
     "ref": "Betty", "suj": "Betty", "obj": "Betty", "poss": "her",
     "poss_nome": "Betty's", "vida": "life",
     "porte": "thick through the arms and middle, and heaviest low across "
              "the hips"},
    {"id": "linda", "curto": "Linda · 53 · sozinha", "v": "v59",
     "nome": "Linda", "sexo": "mulher", "idade": 53,
     "ref": "Linda", "suj": "Linda", "obj": "Linda", "poss": "her",
     "poss_nome": "Linda's", "vida": "life",
     "porte": "sunk deep into whatever she sits on and unable to rise out "
              "of it alone"},
    {"id": "marjorie_sala", "curto": "Marjorie · 38 · sozinha", "v": "v27",
     "nome": "Marjorie", "sexo": "mulher", "idade": 38,
     "ref": "Marjorie", "suj": "Marjorie", "obj": "Marjorie", "poss": "her",
     "poss_nome": "Marjorie's", "vida": "life",
     "porte": "roughly four hundred pounds, and already unable to stand "
              "unaided at that age"},
    # ⭐ A VARIANTE ANONIMA E' DA FONTE, nao economia minha: o v28 diz `This
    # was her before` do primeiro ao ultimo segundo e nunca da' um nome. Ela
    # existe no pool porque muda o registro do video — sem nome, o espectador
    # se enfia no lugar dela mais rapido.
    {"id": "anon_mulher", "curto": "sem nome · 40 · sozinha", "v": "v28",
     "nome": None, "sexo": "mulher", "idade": 40,
     "ref": "her", "suj": "she", "obj": "her", "poss": "her",
     "poss_nome": "her", "vida": "life",
     "porte": "broad through the back and upper arms, and wide across the "
              "shoulder blades"},
    # -- HOMEM (⏳ os dois anonimos — ver a divida declarada acima) --------
    {"id": "anon_homem_v40", "curto": "sem nome · 35 · sozinho", "v": "v40",
     "nome": None, "sexo": "homem", "idade": 35,
     "ref": "him", "suj": "he", "obj": "him", "poss": "his",
     "poss_nome": "his", "vida": "life",
     "porte": "well over six hundred pounds, barefoot and unable to carry "
              "his own weight a single step"},
    {"id": "anon_homem_v45", "curto": "sem nome · 37 · sozinho", "v": "v45",
     "nome": None, "sexo": "homem", "idade": 37,
     "ref": "him", "suj": "he", "obj": "him", "poss": "his",
     "poss_nome": "his", "vida": "life",
     "porte": "carrying it all low and forward at the middle, breathing hard "
              "and audibly"},
    # -- CASAL (o nome e' o DELA; o marido nunca e' nomeado na fonte) -----
    {"id": "marjorie", "curto": "Marjorie · 44 · casal", "v": "v09/v15",
     "nome": "Marjorie", "sexo": "casal", "idade": 44,
     "ref": "Marjorie", "suj": "Marjorie and her husband", "obj": "them",
     "poss": "their", "poss_nome": "Marjorie's", "vida": "lives",
     "porte": "both past three hundred pounds, both moving at the same slow "
              "pace"},
    {"id": "marilyn", "curto": "Marilyn · 46 · casal", "v": "v51",
     "nome": "Marilyn", "sexo": "casal", "idade": 46,
     "ref": "Marilyn", "suj": "Marilyn and her husband", "obj": "them",
     "poss": "their", "poss_nome": "Marilyn's", "vida": "lives",
     "porte": "both wide through the shoulders and hips, leaning on each "
              "other to move"},
    {"id": "mary", "curto": "Mary · 52 · casal", "v": "v49",
     "nome": "Mary", "sexo": "casal", "idade": 52,
     "ref": "Mary", "suj": "Mary and her husband", "obj": "them",
     "poss": "their", "poss_nome": "Mary's", "vida": "lives",
     "porte": "both grey at the temples and slow on their feet"},
    {"id": "anon_casal", "curto": "sem nome · 39 · casal", "v": "v38",
     "nome": None, "sexo": "casal", "idade": 39,
     "ref": "them", "suj": "they", "obj": "them", "poss": "their",
     "poss_nome": "their", "vida": "lives",
     "porte": "both wide through the middle, neither able to push up off "
              "the ground"},
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
ROUPAS = [
    {"id": "blusa_floral", "curto": "blusa floral grande", "v": "v46/v50",
     "sexos": ("mulher", "casal"),
     "antes": "a cream blouse printed with large flowers, stretched tight "
              "across the back and pulling open between the buttons",
     "depois": "the same cream blouse printed with large flowers, now hanging "
               "loose and empty on the frame with the shoulders falling wide"},
    {"id": "regata_mostarda", "curto": "regata mostarda", "v": "v09/v15",
     "sexos": ("mulher", "casal"),
     "antes": "a mustard-yellow ribbed tank top stretched thin over the back "
              "and riding up at the waist",
     "depois": "the same mustard-yellow ribbed tank top, now loose at the "
               "shoulders and hanging straight down from them"},
    {"id": "camiseta_cinza", "curto": "camiseta cinza mescla", "v": "v40",
     "sexos": ("mulher", "homem", "casal"),
     "antes": "a heather grey short-sleeve t-shirt pulled tight over the "
              "shoulders with the hem rucked up",
     "depois": "the same heather grey short-sleeve t-shirt, now loose on the "
               "frame with the sleeves hanging well clear of the arms"},
    {"id": "zip_marinho", "curto": "blusao marinho de ziper", "v": "v59",
     "sexos": ("mulher", "homem", "casal"),
     "antes": "a navy blue zip-front top strained closed across the middle "
              "with the zip pulling apart at the bottom",
     "depois": "the same navy blue zip-front top, now hanging open and loose "
               "with the panels falling straight"},
    {"id": "camiseta_roxa", "curto": "camiseta roxa mescla", "v": "v47",
     "sexos": ("mulher", "homem", "casal"),
     "antes": "a purple heather short-sleeve t-shirt stretched tight across "
              "the front and short at the waist",
     "depois": "the same purple heather short-sleeve t-shirt, now loose "
               "everywhere it touches and long past the waist"},
    {"id": "camiseta_vermelha", "curto": "camiseta vermelha", "v": "v24",
     "sexos": ("mulher", "homem", "casal"),
     "antes": "a bright red short-sleeve t-shirt pulled taut over the front "
              "with the seams standing out at the shoulders",
     "depois": "the same bright red short-sleeve t-shirt, now hanging loose "
               "from the shoulders with the seams sitting low on the arms"},
    {"id": "tunica_floral", "curto": "tunica floral clara", "v": "v39",
     "sexos": ("mulher",),
     "antes": "a pastel floral short-sleeve tunic stretched across the front "
              "and pulled tight under the arms",
     "depois": "the same pastel floral short-sleeve tunic, now hanging loose "
               "and straight with room to spare at the sides"},
    {"id": "vestido_lilas", "curto": "vestido lilas florido", "v": "v28",
     "sexos": ("mulher",),
     "antes": "a sleeveless lavender floral cotton dress strained across the "
              "back with the armholes cutting in",
     "depois": "the same sleeveless lavender floral cotton dress, now loose "
               "on the frame and hanging straight from the shoulders"},
    {"id": "camiseta_verde", "curto": "camiseta verde mescla", "v": "v09",
     "sexos": ("mulher", "homem", "casal"),
     "antes": "a heather green crew-neck t-shirt pulled tight across the "
              "chest and back with the collar strained",
     "depois": "the same heather green crew-neck t-shirt, now loose at the "
               "collar and falling straight down the body"},
    {"id": "polo_marinho", "curto": "polo marinho", "v": "v45",
     "sexos": ("mulher", "homem", "casal"),
     "antes": "a navy blue polo shirt straining at the buttons with the "
              "sleeves cutting into the upper arms",
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
# pool de fala. O autoteste cobra que os NOVE tenham beat.
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
        pool_t = [t for t in BEATS_TESTEMUNHA if t["forma"] in des["formas"]]
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
                     if alvo_t["forma"] in x["formas"]
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
        corpo1 = ("At the centre of the frame are a very heavy %d-year-old %s "
                  "woman, %s, and with her %s. They are %s."
                  % (idade, et, quem, par["antes"], p["porte"]))
    else:
        # ⚠️ PRONOME, NUNCA O NOME, na direcao de cena: o gerador nao sabe
        # quem e' Betty e um nome proprio no prompt e' token sem referente. O
        # nome vive na FALA, que e' onde ele compra alguma coisa.
        corpo1 = ("At the centre of the frame is a very heavy %d-year-old %s "
                  "%s, %s. %s is %s."
                  % (idade, et, "man" if p["sexo"] == "homem" else "woman",
                     quem, "He" if p["sexo"] == "homem" else "She",
                     p["porte"]))

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

# ⛔ A CONTAGEM NA CLAUSULA DE CAMERA (contrato de `CAM_REENCONTRO`).
_RX_CONTAGEM = re.compile(
    r"\b(both|two|three|all three|the pair|the couple)\b", re.I)

# ⛔ A CAMERA PARADA DENTRO DE UM BLOCO CUJO TAKE E' HANDHELD (contrato de
# `cam`). ⚠️ `level`, `straight on` e `at chest height` NAO entram: sao ANGULO
# e ALTURA, que e' exatamente o que o campo deve dizer.
_RX_CAM_PARADA = re.compile(r"\b(still|locked[- ]off|static|tripod)\b", re.I)


# ⛔⛔ LAPIDE — `_sem_dialogo(txt)` MORREU EM 2026-08-21 E FICA ESCRITO AQUI.
# Ela era `re.sub(r"Dialogue:.*", "", txt, flags=re.S)` e servia a RU5. O
# `re.S` faz o `.` casar `\n`, entao ela nao tirava a LINHA do dialogo: tirava
# tudo do primeiro `Dialogue:` ate' o fim do bloco — a fala, o `Voice:` e o
# `Audio:`. A lente lia dois tercos do TAKE e o controle negativo plantava o
# defeito justamente no terco que ela lia. ⭐ A licao generaliza: *corte por
# regex com `re.S` nao remove uma linha, remove uma cauda* — e cauda removida
# em silencio e' lente que passa por estar cega.


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
        m_ = _RX_ROSTO_NO_PORTE.search(spec["pessoa"]["porte"])
        if m_:
            ach.append(("ERRO", "RU4: rosto OCULTO e o porte da pessoa cita "
                                "%r — a frase seguinte descreve o rosto que a "
                                "camera esta' de costas para" % m_.group(0)))
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
    """
    n = len(re.findall(r"(?:very|extremely) heavy",
                       blocos.get(IMAGENS[0], ""), re.I))
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
              _ru17_pronome_do_vizinho, _ru18_ingrediente_nas_tres):
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
    if spec.get("testemunha", {}).get("forma") not in d["formas"]:
        cabem = [x for x in BEATS_TESTEMUNHA if x["forma"] in d["formas"]]
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
    for p_ in PESSOAS:
        n_ = len(re.findall(r"(?:very|extremely) heavy", p_["porte"], re.I))
        if n_:
            falhas.append("[PORTE] %s repete o peso (%d x) — a primeira "
                          "sintagma do IMAGE 01 ja' o diz, e sujeito "
                          "reintroduzido vira corpo a mais (RU14)"
                          % (p_["id"], n_))
        m_ = _RX_ROSTO_NO_PORTE.search(p_["porte"])
        if m_:
            falhas.append("[PORTE] %s cita %r — com o rosto OCULTO a camera "
                          "esta' de costas e a frase descreve o que nao esta' "
                          "em quadro (RU4)" % (p_["id"], m_.group(0)))
        m_ = _RX_PECA_FANTASMA.search("the " + p_["porte"]) or \
            _RX_PECA_FANTASMA.search(p_["porte"])
        if m_:
            falhas.append("[PORTE] %s nomeia %r — a peca e' do eixo ROUPAS e "
                          "de mais ninguem (RU3)" % (p_["id"], m_.group(0)))

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
    ]
    for rotulo, fn, spec_t, blocos_t, deve in controles:
        obtido = _prova(fn, spec_t, blocos_t)
        if obtido != deve:
            falhas.append("CONTROLE %s: a lente %s (esperado: %s)"
                          % (rotulo, "acusou" if obtido else "passou",
                             "acusar" if deve else "passar"))

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
