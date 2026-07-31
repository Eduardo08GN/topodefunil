# 📋 Prompts para o Criador de Ferramentas — AdBatch V4 e V3

> Bateria pronta pra colar no editor do Google Flow. Duas frentes:
> **atualizar a V4** (7 prompts, na ordem) e **criar a V3** (1 prompt de spec).
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
9. Modelo de imagem continua "🍌 Nano Banana Pro", 9:16.
10. Teto de 4000 caracteres por prompt, cortado antes da chamada.

Ao terminar, NÃO responda "pronto". Responda o que você mudou, arquivo por
arquivo, e o resultado do teste de aceitação deste prompt.
```

---

# BATERIA V4 — seis prompts, nesta ordem

> **O escopo é o delta 5→4**: só o que a V5 tem e a V4 não. Ordenados do mais
> barato e isolado ao mais estrutural, porque o editor regride.
>
> ⛔ **Nomes de arquivo NÃO entram nesta bateria.** Ali a V4 já está certa — o
> `sanitizeFilename` dela padroniza com dois dígitos. Quem está torta é a V5,
> que baixa individual sem zero à esquerda (`img_1.jpg`) e só pada dentro do
> ZIP. O prompt está no fim do arquivo, marcado como **correção da V5**.

## PROMPT 1 — modelo de vídeo e duração

*Duas constantes. É o de maior impacto e menor risco — comece por ele.*

```text
[PREÂMBULO]

ESCOPO: apenas as constantes de geração de vídeo em App.tsx.

1. VIDEO_MODEL passa de 'Omni Flash' para 'Veo 3.1 - Lite'.
2. Em Flow.generate.video, durationSeconds passa de 4 para 8.

REGRA FAIL-CLOSED: se 'Veo 3.1 - Lite' não estiver disponível na lista de
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

Modelo de imagem: "🍌 Nano Banana Pro", 9:16.
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
Modelo: "Veo 3.1 - Lite", 9:16, durationSeconds 8.

REGRA FAIL-CLOSED DE MODELO: se "Veo 3.1 - Lite" não estiver disponível, NÃO
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

## Conexões

- [`RUNBOOK-adbatch-vertical.md`](RUNBOOK-adbatch-vertical.md) — a arquitetura, o contrato do parser e o levantamento do atraso da V4
- [`RUNBOOK-bisseccao-moderacao.md`](RUNBOOK-bisseccao-moderacao.md) — a mesma disciplina de variável única, aplicada à moderação do Veo
- [`../WORKFLOW.md`](../WORKFLOW.md) §Passo 3 — onde a ferramenta entra no funil
