# 📋 Prompts para o Criador de Ferramentas — AdBatch V4 e V3

> Bateria pronta pra colar no editor do Google Flow. Três frentes: o
> **PROMPT 0** (modelos em prioridade baixa, vale para as três ferramentas),
> **atualizar a V4** (6 prompts, na ordem) e **criar a V3** (1 prompt de spec).
>
> A arquitetura, o contrato do parser e o levantamento do atraso estão no
> [`RUNBOOK-adbatch-vertical.md`](RUNBOOK-adbatch-vertical.md). Este arquivo é
> só a munição.

---

## ⛔ LEIA ANTES DE COLAR

**O editor regride.** Está registrado no histórico da própria V4: ao mexer no
parser da etapa 2, ele quebrou o parser da etapa 1 que já estava aprovado — e
declarou "corrigido" duas vezes sem ter rodado teste nenhum.

Por isso a bateria é assim:

| Regra | Motivo |
|---|---|
| **Um assunto por prompt** | se dois mudam e algo quebra, você não sabe qual foi |
| **Ordem importa** | os prompts estão ordenados do mais barato/isolado ao mais estrutural |
| **Preâmbulo anti-regressão em todos** | é a lista do que ele não pode encostar |
| **Teste de aceitação com input literal** | e exija que ele **mostre o resultado**, não que declare pronto |
| **Rode o teste você mesmo antes do próximo** | não encadeie prompt em cima de correção não verificada |

Se um prompt regredir alguma coisa: **não mande o próximo**. Mande o
**PROMPT R** (no fim do arquivo) apontando o que quebrou.

---

## 🔒 PREÂMBULO — cole no TOPO de cada prompt da bateria V4

```text
Antes de qualquer alteração, leia esta lista. Nada dela pode mudar neste
prompt. Se a sua alteração exigir encostar em algum destes pontos, PARE e me
avise em vez de mexer:

1. O parser de blocos (normalizeText, isSeparator, buildHeaderRegex,
   stripBeatLabel, splitBlocks, parseImageBlocks, parseTakeBlocks) fica
   VERBATIM como está. Ele custou seis rodadas de correção. Não "melhore",
   não simplifique, não unifique com nada.
2. Etapa 1 e Etapa 2 têm parsers independentes. Mudança em um nunca altera o
   outro.
3. O bloco REF alimenta o painel Consistência Visual e NUNCA vira slot da
   grade nem desloca a numeração.
4. O mediaId do REF entra em referenceImageMediaIds de CADA chamada de imagem
   do lote. Guardar o ID em estado não basta.
5. A tag "REF:[id]" no rodapé de cada card continua existindo. Ela é a prova
   visual de que a referência entrou na requisição.
6. O estado "waiting" (aguardando referência) dos slots continua existindo.
7. O índice manda: bloco N -> imagem N -> take N -> vídeo N -> video_0N.mp4.
   Nunca renumerar por ordem de conclusão. Slot que falhou deixa buraco.
8. Nada de tradução. Prompt e roteiro vão para o modelo exatamente como
   colados, em inglês.
9. Modelo de imagem continua "🍌 Nano Banana 2" em prioridade baixa, 9:16.
10. Teto de 4000 caracteres por prompt, cortado antes da chamada.

Ao terminar, NÃO responda "pronto". Responda o que você mudou, arquivo por
arquivo, e o resultado do teste de aceitação deste prompt.
```

---

> ⭐ **Antes de tudo, o PROMPT 0** (logo abaixo): põe os dois modelos em
> prioridade baixa. Ele vale para as **três** ferramentas e é o único que se
> paga sozinho — enquanto não passar, cada geração de teste dos outros prompts
> queima cota paga.

---

# BATERIA V4 — seis prompts, nesta ordem

> **O escopo é o delta 5→4**: só o que a V5 tem e a V4 não. Ordenados do mais
> barato e isolado ao mais estrutural, porque o editor regride.
>
> ⛔ **Nomes de arquivo NÃO entram nesta bateria.** Ali a V4 já está certa — o
> `sanitizeFilename` dela padroniza com dois dígitos. Quem está torta é a V5,
> que baixa individual sem zero à esquerda (`img_1.jpg`) e só pada dentro do
> ZIP. O prompt está no fim do arquivo, marcado como **correção da V5**.

## PROMPT 0 — os dois modelos em prioridade baixa ⭐

*Vale para as TRÊS ferramentas — 3, 4 e 5 — porque as três herdaram o mesmo
defeito. Rode este antes de qualquer outro: enquanto ele não passar, cada
geração de teste dos outros prompts queima cota paga.*

```text
[PREÂMBULO]

ESCOPO: apenas as constantes de modelo em App.tsx. Nada mais muda.

A ferramenta nomeia os modelos SEM o sufixo de prioridade, entao consome cota
paga em vez do tier gratuito. A regra ja existia na especificacao original e
nunca foi implementada.

IMAGE_MODEL passa a ser exatamente:   🍌 Nano Banana 2
VIDEO_MODEL passa a ser exatamente:   Veo 3.1 - Lite [Lower Priority]

Os nomes tem que bater CARACTERE POR CARACTERE com o que aparece no seletor de
modelos do Flow, emoji e colchetes inclusos. Se o seletor mostrar qualquer um
deles com sufixo de prioridade, use o nome COM o sufixo — e a variante que nao
consome credito.

⚠️ Se algum desses nomes nao existir na lista de modelos disponiveis, NAO
invente um nome parecido e NAO caia no anterior: pare e me diga quais nomes
existem. Nome inexistente faz o SDK cair no modelo padrao, que e pago, e falha
em silencio — o pior caso possivel.

ADICIONE, se ainda nao existir: um rodape no painel lateral mostrando
IMG MODEL e VID MODEL em texto pequeno. Sem ele nao ha como saber qual modelo
esta rodando sem abrir o codigo, e foi assim que este defeito passou semanas
sem ser visto.

MANTENHA a regra fail-closed: se o modelo pedido nao estiver disponivel, NAO
gera e avisa em vermelho.

TESTE DE ACEITACAO: me mostre as duas constantes e o que o rodape exibe.
Depois gere UMA imagem e me confirme dois pontos — qual modelo foi
efetivamente chamado, e se algum credito foi consumido.
```

---

## PROMPT 1 — modelo de vídeo e duração

*Duas constantes. É o de maior impacto e menor risco — comece por ele.*

```text
[PREÂMBULO]

ESCOPO: apenas as constantes de geração de vídeo em App.tsx.

1. VIDEO_MODEL passa de 'Omni Flash' para 'Veo 3.1 - Lite [Lower Priority]'.
   ⚠️ COM o sufixo: sem ele o SDK usa a variante paga.
2. Em Flow.generate.video, durationSeconds passa de 4 para 8.

REGRA FAIL-CLOSED: se 'Veo 3.1 - Lite [Lower Priority]' não estiver na lista de
modelos, NÃO gere nada e mostre um aviso explícito na interface. Nunca caia
em outro modelo silenciosamente, e nunca em modelo pago.

Não mexa em mais nada. Não toque na etapa 1.

TESTE DE ACEITAÇÃO: me mostre as duas linhas alteradas e confirme que
nenhuma outra chamada de vídeo ficou com durationSeconds 4.
```

---

## PROMPT 2 — teto de 4 slots e aviso de excedente

*A ferramenta se chama "Vertical 4" mas a grade cresce com o que for colado.*

```text
[PREÂMBULO]

ESCOPO: quantidade de slots e aviso na barra lateral.

Esta ferramenta produz exatamente 4 cenas. Hoje a grade cresce conforme o
número de blocos colados, o que quebra a identidade dela.

1. Crie a constante MAX_SLOTS = 4 em App.tsx e use-a em todo lugar onde
   hoje a quantidade vem do resultado do parse.
2. A grade sempre mostra 4 slots (01 a 04), mesmo vazios.
3. Bloco IMAGE ou TAKE com índice acima de 4 é DESCARTADO — nunca cria slot
   extra, nunca desloca os outros.
4. Quando algo for descartado, mostre na barra lateral um aviso âmbar:
   "Blocos acima de 04 ignorados." O descarte nunca pode ser silencioso.
5. O bloco REF não conta para esse teto (ele não é slot).

Não mexa no parser: o teto é aplicado DEPOIS do parse, na hora de mapear
blocos para slots.

TESTE DE ACEITAÇÃO: cole este input literal e me diga quantos slots
apareceram na grade e se o aviso acendeu.

REF: Photo of a real person, test reference block.

IMAGE 01/05 — HOOK: Vertical 9:16 test scene one.

IMAGE 02/05 — BANCADA: Vertical 9:16 test scene two.

IMAGE 03/05 — PREPARO: Vertical 9:16 test scene three.

IMAGE 04/05 — RESULTADO: Vertical 9:16 test scene four.

IMAGE 05/05 — CTA: Vertical 9:16 test scene five.

RESULTADO EXIGIDO: painel Consistência Visual com o REF detectado, grade com
4 slots (01 a 04), aviso de blocos ignorados aceso por causa do IMAGE 05.
```

---

## PROMPT 3 — o lote passa a ser realmente aguardado

*Bug real: `setIsGeneratingBatch(false)` roda logo depois do `forEach`, sem
`await`. O botão volta ao normal antes da primeira imagem existir.*

```text
[PREÂMBULO]

ESCOPO: as duas funções de lote (handleGenerateImages e handleGenerateVideos).

Hoje as duas disparam as gerações com prompts.forEach(...) e chamam
setIsGeneratingBatch(false) / setIsGeneratingVideos(false) imediatamente
depois. Como o forEach não aguarda nada, o estado de "gerando" cai antes da
primeira mídia ficar pronta e o rótulo do botão mente.

Corrija nas duas:

1. Colete as promessas e aguarde com Promise.allSettled antes de baixar a
   flag de "gerando". Use try/finally para a flag descer mesmo se algo
   estourar.
2. allSettled, não all: uma falha isolada não pode cancelar as outras.
3. Cada slot continua atualizando o próprio estado por conta, como já faz —
   a barra de progresso é por card, não global.
4. O REF continua bloqueante: gera sozinho, aguarda o sucesso, e SÓ ENTÃO o
   lote dispara com o mediaId dele. Se o REF falhar, o lote NÃO dispara e o
   painel mostra o erro com botão de tentar de novo só do REF.
5. Rodar o lote de novo deve preencher apenas os buracos: filtre os slots
   que já estão em success. Nunca refaça o que deu certo.

TESTE DE ACEITAÇÃO: dispare um lote e me confirme que o botão fica em
"Gerando Lote..." até a última imagem concluir, e que um slot em erro não
impede os outros de terminarem.
```

---

## PROMPT 4 — prompt editável por card (o item mais importante)

*É a diferença real entre a V4 e a V5. Prompt grande, mas é uma coisa só.*

```text
[PREÂMBULO]

ESCOPO: estado dos slots e o card da grade, nas duas etapas.

PROBLEMA: hoje os prompts são recalculados do texto colado a cada render
(parseImageBlocks / parseTakeBlocks chamados direto no corpo do componente).
Isso significa que eu não consigo ajustar o prompt de um card específico: ou
eu reescrevo o roteiro inteiro na barra lateral, ou nada. Quero corrigir uma
frase de UM slot sem tocar nos outros.

IMPLEMENTE O PADRÃO ABAIXO — é o que já roda em produção na versão de 5
cenas, então copie o comportamento exatamente:

1. Cada slot passa a guardar TRÊS campos por prompt, em vez de um:
   - promptFromScript : o que veio do texto colado (a fonte)
   - prompt           : o que vai para o modelo
   - promptDirty      : booleano, true quando eu editei na mão
   Vale para imagem e para vídeo, separadamente:
   imagePromptFromScript / imagePrompt / imagePromptDirty
   videoPromptFromScript / videoPrompt / videoPromptDirty

2. Um useEffect observa o texto colado e sincroniza os slots a cada
   alteração. A regra de merge é esta, e ela é o coração da feature:

   prompt = promptDirty ? prompt : promptFromScript

   Ou seja: recolar o roteiro atualiza os cards que eu NÃO editei, e nunca
   atropela os que eu editei.

3. Cada card ganha um textarea com o prompt daquele slot, editável.
   Editar acende promptDirty.

4. Quando promptDirty estiver ligado, o rótulo do card muda de "Prompt" para
   "Selo: Editado" e aparece ao lado um botão "Restaurar" (ícone undo, cor
   âmbar) que devolve promptFromScript e desliga o promptDirty.

5. Contador de caracteres no canto do card, no formato "1234/4000". Corte a
   entrada em 4000 no onChange, além do corte que já existe antes da chamada.

6. Os botões Regerar e Baixar continuam como estão. Regerar passa a usar o
   prompt ATUAL do card (editado ou não), e continua reanexando a mesma
   referência ativa.

TESTE DE ACEITAÇÃO (rode os três antes de me responder):
A) Colar o roteiro, editar o prompt do slot 02, recolar o mesmo roteiro na
   barra lateral. O slot 02 mantém minha edição; 01, 03 e 04 acompanham.
B) Clicar em Restaurar no slot 02: o texto volta ao do roteiro e o selo some.
C) Regerar o slot 02 depois de editar: a imagem sai do texto editado, com a
   tag REF:[id] presente.
```

---

## PROMPT 5 — Quadro Base ao lado do vídeo, na Etapa 2

```text
[PREÂMBULO]

ESCOPO: apenas o layout do card da Etapa 2.

Hoje o vídeo pronto cobre a imagem no mesmo tile (a imagem some por
transição de opacidade). Isso me impede de julgar a coisa mais importante da
revisão: se o vídeo respeitou o frame inicial.

Mude o card da Etapa 2 para mostrar OS DOIS lado a lado, mesma altura:
- à esquerda, a imagem que serviu de frame inicial, com opacidade reduzida e
  o rótulo "QUADRO BASE" sobreposto;
- à direita, o vídeo gerado.
Ambos em 9:16.

O card fica mais largo: use uma grade de no máximo 2 colunas na Etapa 2, em
vez das 4-5 colunas da Etapa 1.

Não mexa na Etapa 1. Não mexa em nenhuma chamada de geração.

TESTE DE ACEITAÇÃO: me descreva o card da Etapa 2 depois da mudança e
confirme que a imagem base continua visível com o vídeo pronto ao lado.
```

---

## PROMPT 6 — modal de preview e um vídeo por vez

```text
[PREÂMBULO]

ESCOPO: reprodução dos vídeos na Etapa 2. Nenhuma lógica de geração muda.

1. MODAL DE PREVIEW: clicar no vídeo de um card abre ele em tela cheia, num
   overlay escuro com blur, altura 90vh, proporção 9:16, com os controles
   nativos e autoPlay. Fecha clicando fora ou no X do canto superior direito.
   O clique dentro do player não fecha o modal.

2. UM VÍDEO POR VEZ: registre um listener global do evento 'play' na fase de
   captura. Quando qualquer vídeo começar a tocar, pause todos os outros da
   página. Sem isso, cinco áudios tocam juntos na hora da revisão e não dá
   pra avaliar nada.

TESTE DE ACEITAÇÃO: com dois vídeos prontos, dar play no segundo tem que
pausar o primeiro. Clicar num vídeo abre o modal e ele toca sozinho.
```

---

## FORA DA BATERIA — nomes de arquivo, e é correção **da V5**

⛔ **Não mande este na V4.** Ela já está certa: o `sanitizeFilename` padroniza
com dois dígitos nos dois caminhos. É a **V5** que baixa individual sem zero à
esquerda (`img_1.jpg`, `video_1.mp4`) e só pada dentro do ZIP.

Guarde para quando for mexer na V5 — trocando o nome do ZIP para
`adbatch_vertical_5.zip`:

```text
[PREÂMBULO]

ESCOPO: nomes de arquivo no download individual e no ZIP.

Padronize TODOS os downloads com dois dígitos, usando o índice do slot:
- imagem individual: imagem_01.jpg, imagem_02.jpg, ...
- vídeo individual:  video_01.mp4, video_02.mp4, ...
- dentro do ZIP:     video_01.mp4, video_02.mp4, ...
- nome do ZIP:       adbatch_vertical_5.zip

O número é sempre o do SLOT, nunca a ordem de conclusão. Se o slot 02
falhou, o ZIP sai com video_01, video_03 e video_04 — com o buraco, sem
renumerar.

TESTE DE ACEITAÇÃO: me confirme o nome gerado para o slot 3 nos três
caminhos (imagem individual, vídeo individual, dentro do ZIP).
```

---

## PROMPT R — só se algo regredir

```text
REGRESSÃO. O prompt anterior quebrou uma coisa que já funcionava.

O QUE QUEBROU: <descreva o sintoma exato, com o que aparece na tela>
O QUE EU ESPERAVA: <o comportamento anterior>

Restaure o comportamento anterior desse ponto SEM desfazer a alteração que
eu tinha pedido. As duas coisas coexistem — o erro foi ter deixado a
alteração vazar para uma área que não era o escopo.

Antes de responder, rode os dois testes:
A) o teste de aceitação do prompt anterior (a feature nova)
B) o teste do comportamento que regrediu

Só me responda depois de rodar os dois, e me mostre o resultado de cada um.
Se qualquer um falhar, a implementação está incompleta.
```

---

# CRIAÇÃO DA V3 — ferramenta nova, 3 cenas

Prompt único de especificação. Cole numa ferramenta **nova**, em branco.
Depois de criada, rode a mesma bateria de teste de aceitação dos prompts 2 a 7
como verificação.

```text
Crie uma ferramenta de produção de anúncios verticais em lote, chamada
"AdBatch Vertical 3", com EXATAMENTE 3 cenas por lote. Ela funciona em duas
etapas: primeiro gera as imagens, depois gera os vídeos a partir dessas
mesmas imagens, sem download nem reupload no meio.

=== O QUE AMARRA TUDO: O ÍNDICE ===
bloco N -> imagem N -> take N -> vídeo N -> video_0N.mp4
Numere sempre pelo índice de origem, NUNCA pela ordem em que a geração
terminar. Slot que falhou deixa buraco na numeração; nunca renumere.
MAX_SLOTS = 3, como constante única usada em todo lugar.

=== PARSER DE BLOCOS (implemente EXATAMENTE assim) ===
O texto colado é dividido em blocos por CABEÇALHO, não por separador.

Cabeçalho = linha que começa com a palavra REF, IMAGE ou TAKE em maiúsculas,
com estas tolerâncias, todas obrigatórias:
- prefixo de markdown opcional antes: ** , ## , >
- lookahead negativo depois da palavra, para NÃO casar "IMAGENS"/"IMAGEM"
- número opcional, aceitando letra colada: 01, 3, 03A
- fração opcional que é descartada: /05
- travessão, hífen ou dois-pontos opcionais depois: — – - :
- o RESTO DA LINHA vira o início do conteúdo do bloco, nunca é descartado

Antes de parsear, normalize o texto: converta CRLF para LF, remova
zero-width space, zero-width non-joiner, zero-width joiner, word joiner, BOM
e soft hyphen, e troque nbsp por espaço comum. Isso não é opcional: o
copy/paste traz esses caracteres invisíveis e sem essa limpeza o parser cai
no fallback de "1 bloco" sem nenhum sinal na tela.

Descarte linhas decorativas: "---", "=====", "--- IMAGENS ---" e similares.
Nunca viram bloco.

Do começo do conteúdo, remova o rótulo do beat quando houver: "HOOK:",
"CTA + REFORÇO —", etc.

Só nos blocos TAKE: remova as linhas que começam com "Copy falada:" ou
"Contagem:" — são anotação de produção. ATENÇÃO: linhas que começam com
"Dialogue:" e "Audio:" NÃO são metadados, elas são parte do prompt e têm que
ir para o modelo.

Bloco sem número ocupa o primeiro slot livre, na ordem de chegada. Bloco com
índice acima de 3 é descartado, e o descarte acende um aviso âmbar na barra
lateral: "Blocos acima de 03 ignorados." Nunca em silêncio.

Etapa 1 e Etapa 2 têm parsers independentes: mudança em um nunca altera o
outro.

=== ETAPA 1 — IMAGENS ===
Barra lateral com:
- painel "Consistência Visual": mostra o estado da referência
  (Sem referência -> Gerando -> thumbnail com a tag "REF GERADO" e o id).
  Um link discreto "ou anexar manualmente" permite subir uma imagem como
  fallback; se eu anexar, esse mediaId substitui o gerado.
- textarea grande "Prompts de Imagem", onde eu colo REF + os 3 blocos IMAGE
  de uma vez.
- contador de blocos detectados.
- botão "Gerar Lote com Referência".

O botão faz a sequência inteira sozinha:
(a) gera a imagem do bloco REF via SDK e AGUARDA concluir;
(b) só então dispara os 3 slots IMAGE, passando o mediaId do REF em
    referenceImageMediaIds de CADA chamada;
(c) enquanto o REF gera, os slots ficam no estado "aguardando referência".
Se o REF falhar, o lote NÃO dispara: mostre o erro e um botão que regera só
o REF. Nunca gere as imagens sem referência em silêncio.

Guardar o id da referência em estado NÃO BASTA: ele tem que entrar na
requisição de cada slot. Cada card exibe no rodapé a tag "REF:[últimos 4
dígitos do id]" como prova visual de que a referência foi anexada. Se um
slot for gerado sem referência enquanto existe bloco REF no texto, marque o
card com alerta em vez de sucesso.

Modelo de imagem: "🍌 Nano Banana 2" (prioridade baixa, 0 creditos), 9:16.
⚠️ O nome tem que bater caractere por caractere com o seletor do Flow. Se ele
mostrar sufixo de prioridade, use o nome COM o sufixo.
Uma imagem = um enquadramento único. Jamais colagem, grade, mosaico,
múltiplos painéis ou storyboard dentro de uma mesma imagem.

=== PORTÃO DE REVISÃO ===
Depois das imagens eu reviso e regenero os slots ruins. A Etapa 2 só fica
disponível quando existir pelo menos uma imagem com sucesso, e só abre
quando eu clicar. Nenhum vídeo é gerado antes disso.

=== ETAPA 2 — VÍDEOS ===
Textarea "Roteiros (Takes)" onde eu colo os 3 blocos TAKE de uma vez. O take
N anima a imagem do slot N.

Cada chamada de vídeo passa a imagem do slot correspondente como frame
inicial (image-to-video). O texto do TAKE é a direção de movimento e fala.
Modelo: "Veo 3.1 - Lite [Lower Priority]", 9:16, durationSeconds 8.
⚠️ COM o sufixo de prioridade: e a variante que nao consome credito.

REGRA FAIL-CLOSED DE MODELO: se "Veo 3.1 - Lite [Lower Priority]" não estiver, NÃO
gere e avise. Nunca caia em outro modelo, nunca em modelo pago.

Se houver TAKE sem imagem correspondente, marque alerta naquele card em vez
de travar o lote inteiro.

=== PROMPT EDITÁVEL POR CARD (nas duas etapas) ===
Cada slot guarda três campos por prompt:
- promptFromScript : o que veio do texto colado
- prompt           : o que vai para o modelo
- promptDirty      : true quando eu editei na mão
Separados para imagem e para vídeo.

Um useEffect observa o texto colado e sincroniza os slots a cada alteração,
com esta regra de merge:
   prompt = promptDirty ? prompt : promptFromScript
Recolar o roteiro atualiza os cards que eu não editei e NUNCA atropela os que
eu editei.

Cada card tem um textarea editável com o prompt daquele slot, um contador
"1234/4000", e — quando promptDirty estiver ligado — o rótulo vira "Selo:
Editado" com um botão "Restaurar" (ícone undo, âmbar) que devolve o texto do
roteiro.

Teto de 4000 caracteres por prompt: corte no onChange e de novo antes da
chamada ao SDK. O SDK rejeita acima disso.

=== AÇÕES POR CARD ===
Abaixo de cada mídia, dois botões de 32px de altura, sempre visíveis (não
dependem de hover), fundo sólido, texto em caixa alta pequena:
- "Regerar": refaz APENAS aquele slot, com o prompt atual do card e a mesma
  referência ativa. Nunca regera o REF, nunca toca nos outros slots. Só
  aquele card volta para loading com shimmer.
- "Baixar": baixa o arquivo daquele card.
Em loading, os dois ficam desabilitados.

Rodar o lote de novo preenche apenas os buracos: filtre os slots que já estão
em sucesso. Nunca refaça o que deu certo.

=== REVISÃO DO VÍDEO ===
- Na Etapa 2, cada card mostra LADO A LADO, mesma altura: à esquerda a imagem
  que serviu de frame inicial, com opacidade reduzida e o rótulo "QUADRO
  BASE"; à direita o vídeo gerado. É o que permite julgar se o vídeo
  respeitou o frame.
- Clicar no vídeo abre um modal de preview em tela cheia: overlay escuro com
  blur, 90vh, 9:16, controles nativos, autoPlay. Fecha no clique fora ou no X.
- Um vídeo por vez: um listener global do evento 'play' na fase de captura
  pausa todos os outros vídeos da página quando um começa a tocar.

=== EXPORTAÇÃO ===
Botão "Baixar Pacote ZIP (N)" na barra lateral da Etapa 2, com o contador em
tempo real, desabilitado enquanto não houver nenhum vídeo pronto. Empacota
com JSZip todos os vídeos em sucesso.

Nomes com dois dígitos, sempre pelo índice do slot:
- imagem individual: imagem_01.jpg
- vídeo individual:  video_01.mp4
- dentro do ZIP:     video_01.mp4
- nome do ZIP:       adbatch_vertical_3.zip

=== REGRA FINAL ===
NÃO TRADUZA NADA. Prompts e roteiros vão para o modelo exatamente como
colados, em inglês. A interface é em português; o conteúdo, nunca.

=== TESTE DE ACEITAÇÃO (rode antes de responder) ===
Cole este input literal no campo de imagens e me diga o que o parser
devolveu: quantos blocos, de que tipo, e quantos caracteres cada um.

REF 01: Photo of a real person, test reference block.

IMAGE 01/03 — HOOK: Vertical 9:16 test scene one.

IMAGE 02/03 — MECANISMO: Vertical 9:16 test scene two.

IMAGE 03/03 — CTA: Vertical 9:16 test scene three.

RESULTADO EXIGIDO: 1 bloco REF (painel sai de "Sem referência" para "REF
detectado") e 3 blocos IMAGE nos slots 01, 02 e 03. Se der qualquer outro
resultado, a implementação está errada — me diga o que deu, não conserte por
conta própria.
```

---

# BATERIA V3 v2.4 — colar tudo de uma vez (2 prompts, nesta ordem)

> **O problema, medido em produção 2026-08-01.** Hoje o operador cola o REF e os
> IMAGE na aba "1. Imagens", **espera o lote inteiro terminar**, troca para a aba
> "2. Vídeos" e só ali cola os TAKE. São dois bloqueios somados no `App.tsx`:
>
> 1. **O textarea dos TAKE não existe enquanto se está na aba de imagens.** Não
>    está desabilitado — não está no DOM. A sidebar renderiza
>    `stage === 'images' ? (<textarea inputText/>) : (<textarea takeText/>)`.
> 2. **A aba "2. Vídeos" está travada:**
>    `disabled={!slots.some(s => s.imageStatus === 'success') || isBatchLoading}`
>    — só destrava com pelo menos uma imagem pronta **e** o lote parado.
>
> **O que muda:** um campo único onde se cola REF + IMAGE + TAKE de uma vez. Os
> takes ficam em estado desde a colagem, e o disparo dos vídeos fica **armado**
> (um clique) assim que as imagens ficam prontas.
>
> ⭐ **Semiautomático por decisão do operador (2026-08-01), não automático.** O
> encadeamento automático economizaria um clique e custaria a janela de revisar
> as imagens — e essa janela é usada: o botão "Regerar Imagem" existe por card e
> é acionado antes de animar. Auto-disparo em cima de imagem torta queima 4
> variantes de vídeo.
>
> ⚠️ **O parser não é tocado.** O `parseBlocks()` já reconhece `REF`, `IMAGE` e
> `TAKE` na mesma varredura, com o mesmo `headerRegex`, e cada `useEffect` já
> filtra por `b.type`. Apontar os dois para o mesmo texto resolve sem uma linha
> de `parser.ts`. É mudança de UI e de estado.

## 🔒 PREÂMBULO V3 — cole no TOPO dos dois prompts desta bateria

```text
Antes de qualquer alteracao, leia esta lista. Nada dela pode mudar neste
prompt. Se a sua alteracao exigir encostar em algum destes pontos, PARE e me
avise em vez de mexer:

1. utils/parser.ts fica VERBATIM: normalizeText, cleanContent, removeLabels,
   parseBlocks e o headerRegex. Nao "melhore", nao simplifique, nao unifique.
   Ele ja reconhece REF, IMAGE e TAKE na mesma varredura — e' de proposito.
2. O bloco REF alimenta o painel Consistencia Visual e NUNCA vira slot da
   grade nem desloca a numeracao. Continuam sendo 3 slots.
3. O mediaId do REF entra em referenceImageMediaIds de CADA chamada de imagem
   do lote (a variavel currentRefId em generateBatch).
4. O indice manda: bloco N -> slot N -> variantes A/B/C/D ->
   slot_0N_variant_X.mp4. Nunca renumerar por ordem de conclusao.
5. Nada de traducao. Prompt e roteiro vao para o modelo exatamente como
   colados, em ingles.
6. Teto de 4000 caracteres por prompt, cortado antes da chamada (.slice(0,4000)).
7. IMAGE_MODEL e VIDEO_MODEL nao mudam neste prompt, nem a regra fail-closed
   do modelError.
8. 4 variantes por slot. Os videos continuam saindo SLOT A SLOT (await
   Promise.allSettled por slot antes do proximo) — e' anti rate-limit, nao e'
   estilo.
9. durationSeconds: 10 e aspectRatio '9:16' ficam como estao.
10. promptDirty continua mandando: prompt editado a mao no card NAO e'
    sobrescrito quando o texto colado muda.
11. chosenIndex, o ZIP e o nome adbatch_vertical_output.zip ficam como estao.

Ao terminar, NAO responda "pronto". Responda o que voce mudou, arquivo por
arquivo, e o resultado do teste de aceitacao deste prompt.
```

## PROMPT V3-1 — campo único de roteiro ⭐

*O prompt que resolve o problema. Um assunto: fundir os dois textareas em um.*

```text
[PREAMBULO V3]

ESCOPO: apenas a sidebar e o estado de texto em App.tsx. parser.ts nao muda.

HOJE existem dois estados de texto e dois textareas mutuamente exclusivos:
inputText (renderizado so' quando stage === 'images') e takeText (renderizado
so' quando stage === 'videos'). Por isso e' impossivel colar os TAKE antes das
imagens terminarem: o campo nao existe na tela.

MUDE PARA UM CAMPO SO:

1. Substitua os dois estados por um unico: scriptText.
2. A sidebar passa a ter UM textarea, SEMPRE VISIVEL, nas duas abas — nao mais
   dentro do ternario de stage. Placeholder:
   "Cole o roteiro inteiro: REF + IMAGE 01/02/03 + TAKE 01/02/03"
   Altura maior que a atual (h-64 -> h-80), porque agora recebe o dobro.
3. Os DOIS useEffect de sincronizacao passam a ler scriptText. Continuam
   independentes e continuam filtrando por b.type: um pega os blocos IMAGE,
   o outro pega os blocos TAKE. NAO unifique os dois useEffect.
4. generateBatch() ja faz parseBlocks(inputText) para achar o REF — passa a
   ler scriptText.
5. O textarea NAO fica mais disabled durante isBatchLoading. O operador tem de
   poder colar ou corrigir o roteiro enquanto as imagens geram. (Os botoes de
   disparo continuam disabled — so' o textarea libera.)

⛔ NAO mexa nos textareas dos CARDS. Cada card continua com o seu campo
proprio, mostrando imagePrompt ou videoPrompt conforme a aba, com o selo
"Editado" e o promptDirty. Isso e' o item 10 do preambulo.

TESTE DE ACEITACAO — cole exatamente este texto no campo unico, com a
ferramenta recem-carregada e ainda na aba "1. Imagens":

REF 01: a 44-year-old woman, chest up, facing camera, plain gray background.
IMAGE 01/03: she stands in a kitchen holding a carrot.
IMAGE 02/03: she stands in the same kitchen holding a jar.
IMAGE 03/03: she stands beside a man in the same kitchen.
TAKE 01/03: she talks to the lens, no cuts.
TAKE 02/03: she lowers the carrot onto the board.
TAKE 03/03: she points at what he is holding.

Me mostre, SEM gerar nada e SEM sair da aba de imagens:
(a) o conteudo do campo de prompt de cada um dos 3 cards na aba "1. Imagens";
(b) o conteudo do campo de prompt de cada um dos 3 cards depois de clicar na
    aba "2. Videos".
O esperado e' que os TAKE ja estejam nos 3 cards em (b), sem ter gerado
imagem nenhuma. Se nao estiverem, a implementacao esta errada — me diga o que
deu, nao conserte por conta propria.
```

## PROMPT V3-2 — o disparo fica armado, e o operador vê que está

*Só depois do V3-1 passar. Um assunto: tornar visível que os takes já estão em
memória e que basta um clique.*

```text
[PREAMBULO V3]

ESCOPO: apenas indicadores de estado e o destravamento da aba 2 em App.tsx.
Nenhuma logica de geracao muda.

⛔ NAO implemente disparo automatico. O operador decidiu SEMIAUTOMATICO: as
imagens terminam, o botao fica armado, e ELE clica. A janela entre imagem
pronta e video disparado e' onde ele regera imagem torta — auto-disparo em
cima de imagem ruim queima 4 variantes de video.

1. CONTADOR DE ROTEIRO. Abaixo do textarea unico, uma linha pequena mostrando
   o que o parser encontrou no texto colado, ao vivo:
      "REF: sim/nao · IMAGE: N/3 · TAKE: N/3"
   Verde quando 3/3, ambar quando parcial, cinza quando zero. E' a prova de
   que os takes entraram — hoje nao ha como saber sem trocar de aba.

2. A ABA "2. Videos" destrava assim que houver PELO MENOS UMA imagem com
   sucesso, mesmo com isBatchLoading true. Hoje a condicao e'
   `!slots.some(s => s.imageStatus === 'success') || isBatchLoading` e o
   `|| isBatchLoading` tranca a aba durante o lote inteiro, sem motivo: olhar
   nao dispara nada. Tire APENAS o `|| isBatchLoading` desta condicao.
   ⛔ Os BOTOES de disparo continuam disabled durante isBatchLoading.

3. BOTAO ARMADO. O "Redisparar Sequencia (1→2→3)" ganha tres estados visiveis:
   · sem take em memoria  -> disabled, rotulo "Cole os TAKE no roteiro"
   · take ok, imagem nao  -> disabled, rotulo "Aguardando imagens"
   · take ok e >=1 imagem -> habilitado, rotulo "Disparar Videos (1→2→3)",
                             com anel branco pulsando (ring-2 ring-white/40
                             animate-pulse) para dizer que esta' armado.

4. Nada de encadeamento, nada de timer, nada de useEffect que dispare geracao.

TESTE DE ACEITACAO — com a ferramenta recem-carregada, cole o mesmo roteiro do
teste anterior e me mostre, em ordem:
(a) o que o contador exibe logo apos colar, ainda sem gerar nada;
(b) o rotulo e o estado do botao de video nesse momento;
(c) o rotulo e o estado do botao depois que as 3 imagens ficarem prontas;
(d) confirme explicitamente que NENHUM video comecou a gerar sozinho em
    momento nenhum.
```

---

# CRIAÇÃO DA V2 — ferramenta nova, 2 cenas (o formato 16s)

> Nasce para o **AGENTE TRIO 16**: 2 takes de 8s = 16 segundos. A V3 continua
> existindo e continua sendo a ferramenta dos 19 motores de 3 cenas — a V2 **não
> substitui nada**, é uma segunda ferramenta.
>
> ⭐ **Ela nasce em paridade com a V3 v2.5**, não com a V3 original. Tudo o que
> as baterias V3-1 e V3-2 acrescentaram depois (campo único de roteiro, contador
> ao vivo, botão armado) já entra na especificação. Criar em v1 e depois aplicar
> duas baterias seria pagar duas vezes pelo mesmo aprendizado.
>
> ⚠️ **A especificação abaixo descreve o CÓDIGO REAL da V3**, transcrito em
> `adbatch-vertical/`, não o prompt de criação da V3 que está mais acima neste
> arquivo. Os dois divergem em quatro pontos, e onde divergem **manda o código**:
>
> | ponto | prompt de criação da V3 (aspiração) | código real hoje |
> |---|---|---|
> | modelo de vídeo | `Veo 3.1 - Lite [Lower Priority]` | **`Omni Flash`** |
> | duração | `8` | **`10`** (aspiracional — sai 8s) |
> | nome do ZIP | `adbatch_vertical_3.zip` | **`adbatch_vertical_output.zip`** |
> | nome do arquivo | `video_01.mp4` | **`slot_01_variant_A.mp4`** |
>
> A V2 nasce **igual à V3 de hoje** nos três primeiros e com o ZIP renomeado. Se
> um dia o PROMPT 0 (prioridade baixa) for aplicado, ele vale para as duas.

## PROMPT V2 — criação, prompt único

*Cole numa ferramenta **nova**, em branco. Sem preâmbulo anti-regressão: não há
o que regredir.*

```text
Crie uma ferramenta de producao de anuncios verticais em lote, chamada
"AdBatch Vertical 2", com EXATAMENTE 2 cenas por lote. Ela funciona em duas
etapas: primeiro gera as imagens, depois gera os videos a partir dessas mesmas
imagens, sem download nem reupload no meio.

=== O QUE AMARRA TUDO: O INDICE ===
bloco N -> imagem N -> take N -> video N -> slot_0N_variant_X.mp4
Numere sempre pelo indice de origem, NUNCA pela ordem em que a geracao
terminar. Slot que falhou deixa buraco na numeracao; nunca renumere.
MAX_SLOTS = 2, como constante unica usada em todo lugar. A grade mostra
sempre 2 slots (01 e 02), mesmo vazios.

=== PARSER DE BLOCOS — copie EXATAMENTE, inclusive a regex ===
Este parser custou seis rodadas de correcao na ferramenta irma. Nao "melhore",
nao simplifique, nao unifique. Implemente em utils/parser.ts com estas quatro
pecas, nesta ordem:

1. normalizeText(text): troca CRLF por LF; depois DUAS substituicoes, ambas
   escritas no codigo-fonte com ESCAPE UNICODE, jamais com o caractere colado
   (colar o caractere invisivel dentro da regra que o remove ja aconteceu
   nesta base, e o arquivo fica sujo sem ninguem ver):
   (a) uma classe de caracteres que remove, POR PONTO DE CODIGO:
       U+200B zero width space, U+200C zero width non-joiner,
       U+200D zero width joiner, U+FEFF BOM, U+2060 word joiner,
       U+00AD soft hyphen.
   (b) uma segunda que troca U+00A0 (nbsp) por espaco comum U+0020.
   NAO E OPCIONAL: o copy/paste traz esses invisiveis e sem a limpeza o parser
   cai no fallback de "1 bloco" sem nenhum sinal na tela.

2. cleanContent(lines, type): descarta linha decorativa — /^([-=])\1+$/ e
   /^---.*---$/ — e, SO quando type === 'TAKE', descarta linhas que comecam com
   "Copy falada:" ou "Contagem:".
   ATENCAO: linhas que comecam com "Dialogue:" e "Audio:" NAO sao metadados.
   Elas sao o prompt de fala e de som, e TEM que chegar ao modelo. Filtrar
   essas duas gera video mudo.

3. removeLabels(text): remove do INICIO
   /^(HOOK|CTA|REFORCO|MECANISMO|INTRO|BODY|OUTRO|OFERTA)\s*([+:—–-])\s*/i

4. parseBlocks(text): divide por CABECALHO, nao por separador, com esta regex
   literal:

   /^(?:[*#> ]+)?(REF|IMAGE|TAKE)(?![A-Z])(?:\s*(\d+))?(?:[A-Z])?(?:\/\d+)?(?:\s*[:—–-])?\s*(.*)$/i

   - aceita *, #, > e espaco antes (markdown colado)
   - o lookahead (?![A-Z]) impede "IMAGENS" de virar cabecalho
   - o indice e o PRIMEIRO numero: em "IMAGE 01/02" le 01 e DESCARTA o /02
   - o resto da linha depois do cabecalho ja entra no conteudo, nunca some
   Devolve { type, index, content } por bloco.

Bloco IMAGE ou TAKE com indice acima de 2 e DESCARTADO — nunca cria slot
extra, nunca desloca os outros. Quando algo for descartado, acenda um aviso
ambar na barra lateral: "Blocos acima de 02 ignorados." O descarte nunca pode
ser silencioso.

O bloco REF nao conta para esse teto: ele nao e slot.

=== CAMPO UNICO DE ROTEIRO ===
UM textarea so na barra lateral, SEMPRE VISIVEL nas duas abas — nunca dentro
de um ternario de stage. Estado unico: scriptText. Placeholder:
"Cole o roteiro inteiro: REF + IMAGE 01/02 + TAKE 01/02"

DOIS useEffect independentes leem o mesmo scriptText: um filtra b.type ===
'IMAGE' e alimenta imagePrompt, o outro filtra b.type === 'TAKE' e alimenta
videoPrompt. NAO unifique os dois useEffect.

O textarea NAO fica disabled durante a geracao: eu tenho que poder corrigir o
roteiro enquanto as imagens saem. Só os BOTOES de disparo ficam disabled.

Abaixo do textarea, um contador ao vivo do que o parser encontrou:
   "REF: sim/nao · IMAGE: N/2 · TAKE: N/2"
verde quando 2/2, ambar quando parcial, cinza quando zero. E a prova de que os
takes entraram sem precisar trocar de aba.

=== ETAPA 1 — IMAGENS ===
Painel "Consistencia Visual" na barra lateral: Sem referencia -> Gerando ->
thumbnail com a tag "REF GERADO" e o id. Um link discreto "ou anexar
manualmente" permite subir uma imagem; se eu anexar, esse mediaId substitui o
gerado.

O botao "Gerar Lote com Referencia" faz a sequencia inteira sozinho:
(a) se ha bloco REF no roteiro e nenhuma referencia carregada, gera a imagem do
    REF e AGUARDA concluir;
(b) so entao dispara os 2 slots IMAGE, passando o mediaId do REF em
    referenceImageMediaIds de CADA chamada;
(c) enquanto o REF gera, os slots ficam em "aguardando referencia".

Se o REF falhar, o lote NAO dispara: mostre o erro e um botao que regera so o
REF. Nunca gere as imagens sem referencia em silencio.

Guardar o id da referencia em estado NAO BASTA: ele tem que entrar na
requisicao de cada slot. Cada card exibe no rodape a tag "REF:[ultimos 4
digitos do id]" como prova visual de que a referencia foi anexada.

Rodar o lote de novo preenche apenas os buracos: filtre os slots que ja estao
em sucesso. Nunca refaca o que deu certo.

Modelo de imagem: "🍌 Nano Banana 2", aspectRatio "9:16".
Uma imagem = um enquadramento unico. Jamais colagem, grade, mosaico, multiplos
paineis ou storyboard dentro de uma mesma imagem.

=== TRAVA DE MODELO, fail-closed ===
Declare as duas listas:
  VALID_IMAGE_MODELS = ['🍌 Nano Banana Pro', '🍌 Nano Banana 2', '🍌 Nano Banana 2 Lite']
  VALID_VIDEO_MODELS = ['Omni Flash', 'Veo 3.1 - Lite', 'Veo 3.1 - Fast', 'Veo 3.1 - Quality']
Num useEffect de montagem, se IMAGE_MODEL ou VIDEO_MODEL nao estiver na sua
lista, BLOQUEIE a geracao inteira e mostre em vermelho:
  'MODELO NAO ENCONTRADO: "<nome>". Geracao bloqueada por seguranca.'
Nunca caia num modelo padrao. Um rename do lado do Google tem que virar erro
visivel, nao lote gerado no modelo errado.

=== PORTAO DE REVISAO ===
A aba "2. Videos" destrava assim que houver PELO MENOS UMA imagem com sucesso.
Nao trave a aba durante o lote: olhar nao dispara nada. Os BOTOES de disparo
continuam disabled enquanto o lote roda.

⛔ NAO implemente disparo automatico de video. E semiautomatico de proposito:
as imagens terminam, o botao fica armado, e EU clico. A janela entre imagem
pronta e video disparado e onde eu regero imagem torta — auto-disparo em cima
de imagem ruim queima 4 variantes de video.

O botao de disparo tem tres estados visiveis:
  · sem take em memoria -> disabled, rotulo "Cole os TAKE no roteiro"
  · take ok, imagem nao -> disabled, rotulo "Aguardando imagens"
  · take ok e >=1 imagem -> habilitado, "Disparar Videos (1→2)", com anel
    branco pulsando (ring-2 ring-white/40 animate-pulse)

=== ETAPA 2 — VIDEOS ===
O take N anima a imagem do slot N: cada chamada passa a imagem daquele slot
como frame inicial (firstFrameImageMediaId). O texto do TAKE e a direcao de
movimento e de fala.

Modelo: "Omni Flash", aspectRatio "9:16", durationSeconds 10.

QUATRO VARIANTES POR SLOT (A, B, C, D). A sequencia e SERIAL POR SLOT e
PARALELA POR VARIANTE: aguarde as 4 variantes do slot 01 com
Promise.allSettled antes de comecar o slot 02. Isso e anti rate-limit, nao e
estilo — nao paralelize os slots entre si.

allSettled, nunca all: uma variante que falha nao pode cancelar as outras.

Eu escolho UMA variante por slot (chosenIndex). Slot sem escolha fica fora do
ZIP, e o rodape lista quais faltam.

Se houver TAKE sem imagem correspondente, marque alerta naquele card em vez de
travar o lote inteiro.

=== PROMPT EDITAVEL POR CARD (nas duas etapas) ===
Cada slot guarda TRES campos por prompt, separados para imagem e para video:
  promptFromScript : o que veio do texto colado
  prompt           : o que vai para o modelo
  promptDirty      : true quando eu editei na mao

A regra de merge e o coracao da feature:
  prompt = promptDirty ? prompt : promptFromScript
Recolar o roteiro atualiza os cards que eu NAO editei e nunca atropela os que
eu editei.

Cada card tem um textarea editavel, um contador "1234/4000" e — quando
promptDirty estiver ligado — o rotulo vira "Selo: Editado" com um botao
"Restaurar" (icone undo, ambar) que devolve promptFromScript e desliga o dirty.

TETO DE 4000 CARACTERES por prompt: .slice(0, 4000) no onChange E de novo
antes da chamada ao SDK. O corte hoje e silencioso na ferramenta irma; aqui eu
quero o contador ficando vermelho ao passar de 3800, para eu ver chegando.

=== ACOES POR CARD ===
Dois botoes de 32px, SEMPRE VISIVEIS (nao dependem de hover), fundo solido,
texto em caixa alta pequena:
- "Regerar": refaz APENAS aquele slot, com o prompt atual do card e a mesma
  referencia ativa. Nunca regera o REF, nunca toca no outro slot.
- "Baixar": baixa o arquivo daquele card.
Em loading, os dois ficam desabilitados.

=== REVISAO DO VIDEO ===
- Cada card da Etapa 2 mostra LADO A LADO, mesma altura: a esquerda a imagem
  que serviu de frame inicial, com opacidade reduzida e o rotulo "QUADRO BASE";
  a direita o video. E o que permite julgar se o video respeitou o frame.
- Clicar no video abre um modal em tela cheia: overlay escuro com blur, 90vh,
  9:16, controles nativos, autoPlay. Fecha no clique fora ou no X. Clique
  dentro do player nao fecha.
- UM VIDEO POR VEZ: listener global do evento 'play' na FASE DE CAPTURA. Quando
  qualquer video comeca, pause todos os outros da pagina.

=== EXPORTACAO ===
Botao "Baixar Pacote ZIP (N)" na barra lateral da Etapa 2, contador em tempo
real, desabilitado enquanto nao houver escolha nenhuma. Empacota com JSZip so
as variantes escolhidas.

Nomes sempre pelo indice do SLOT, com dois digitos:
- video individual:  slot_01_variant_A.mp4
- dentro do ZIP:     slot_01_variant_A.mp4
- nome do ZIP:       adbatch_vertical_2.zip

=== REGRA FINAL ===
NAO TRADUZA NADA. Prompts e roteiros vao para o modelo exatamente como
colados, em ingles. A interface e em portugues; o conteudo, nunca.

=== TESTE DE ACEITACAO — rode ANTES de responder ===
Com a ferramenta recem-carregada e ainda na aba "1. Imagens", cole este texto
literal no campo unico:

REF 01: Photo of a real person, a 24-year-old woman, chest up, facing the camera.
IMAGE 01/02: two women sit on a couch, a third stands behind them.
IMAGE 02/02: she holds a glass in a kitchen, a man stands at frame-right.
IMAGE 03/02: this block must be discarded.
TAKE 01/02: she speaks to the lens, no cuts.
Dialogue: "test line one"
TAKE 02/02: she holds the glass steady.
Copy falada: esta linha tem que sumir
Dialogue: "test line two"

Me responda, SEM gerar nada e SEM sair da aba de imagens:
(a) quantos blocos o parser devolveu, de que tipo e com que indice;
(b) o que o contador de roteiro exibe;
(c) se o aviso ambar de bloco ignorado acendeu, e com que texto;
(d) o conteudo exato do campo de prompt dos 2 cards na aba "2. Videos";
(e) confirme que a linha "Dialogue:" SOBREVIVEU nos dois takes e que a linha
    "Copy falada:" SUMIU do take 02.

RESULTADO EXIGIDO: 1 REF + 2 IMAGE (slots 01 e 02) + 2 TAKE (slots 01 e 02);
contador "REF: sim · IMAGE: 2/2 · TAKE: 2/2" em verde; aviso ambar aceso por
causa do IMAGE 03; as duas linhas Dialogue presentes; a linha "Copy falada:"
ausente.

Se der qualquer outro resultado, a implementacao esta errada — me diga o que
deu, NAO conserte por conta propria.
```

⚠️ Se ele regredir alguma coisa, use o **PROMPT R** acima.

### 🧾 O Montador Vertical 3 NÃO precisa de versão 2

Medido no fonte (`montador-vertical-3/App.tsx`), não suposto:

- os 3 slots nascem `media: null` e o `downloadZip` faz `slots.forEach` gravando
  **só os preenchidos** — com os slots 0 e 1 cheios, o ZIP sai `video_01.mp4` +
  `video_02.mp4`, numeração correta, sem buraco;
- o terceiro slot fica vazio na tela e não atrapalha o download.

A única esquisitice é cosmética: os rótulos são travados por índice
(`slot.index === 0 ? 'HOOK' : ...`), então o **slot 2 aparece como `MECANISMO`**
quando no 16s ele é o CTA. Um vídeo de 16s monta na ferramenta de hoje.

---

## Conexões

- [`adbatch-vertical/README.md`](adbatch-vertical/README.md) — o código-fonte transcrito das duas ferramentas e o que só ele revela
- [`RUNBOOK-adbatch-vertical.md`](RUNBOOK-adbatch-vertical.md) — a arquitetura, o contrato do parser e o levantamento do atraso da V4
- [`RUNBOOK-bisseccao-moderacao.md`](RUNBOOK-bisseccao-moderacao.md) — a mesma disciplina de variável única, aplicada à moderação do Veo
- [`../WORKFLOW.md`](../WORKFLOW.md) §Passo 3 — onde a ferramenta entra no funil
