# 🎬 RUNBOOK — AdBatch Vertical (Google Flow)

> **A ferramenta que transforma o roteiro do agente em vídeo pronto.**
>
> Ela mora dentro do Google Flow (Criador de Ferramentas), é escrita em
> React/TypeScript e roda contra o `flow-sdk`. Recebe o texto que o agente
> Python cospe, gera as imagens, e usa cada imagem como **frame inicial** do
> vídeo correspondente. Saída: um ZIP numerado, pronto pra postagem.
>
> A **V5 (5 takes) é a referência** — é a versão redonda. A V4 está atrasada e a
> V3 ainda não existe. O que muda entre elas é **uma constante**.

---

## O LUGAR DELA NO PIPELINE

```
agente .exe  →  [copiar os 5 IMAGE]  →  AdBatch etapa 1  →  revisão  →
                [copiar os 5 TAKE]   →  AdBatch etapa 2  →  ZIP  →  Veo Editor
```

A ferramenta é o **meio de campo**: não decide nada de criativo, não reescreve
prompt, não traduz. Ela **executa o índice**. Toda a inteligência mora antes
(no motor do agente) e depois (na esteira do Veo Editor).

---

## AS DUAS ETAPAS

| | Etapa 1 — IMAGENS | Etapa 2 — VÍDEOS |
|---|---|---|
| Entrada | bloco `REF` + N blocos `IMAGE` | N blocos `TAKE` |
| Modelo | `🍌 Nano Banana 2` (prioridade baixa) | `Veo 3.1 - Lite [Lower Priority]` |
| Formato | 9:16 | 9:16, **8 segundos** |
| Referência | o media do `REF` entra em `referenceImageMediaIds` de **cada** slot | a imagem do slot entra em `firstFrameImageMediaId` |
| Portão | a etapa 2 só abre com **≥1 imagem em success** | — |

**O REF é bloqueante.** Ele gera primeiro, sozinho; só depois o lote dispara,
já com o `mediaId` dele em mãos. Nunca em paralelo — senão os slots saem sem
referência e você tem cinco pessoas diferentes no mesmo vídeo.

---

## ⭐ O CONTRATO DE ENTRADA — o que o parser aceita

Esta é a parte que mais custou pra ficar de pé (seis rodadas de correção no
histórico da V4). O parser quebra o texto colado em blocos por **cabeçalho**,
não por separador.

### O cabeçalho

```
^\s*(?:\*{1,2}|#{1,4}|>)?\s*(REF|IMAGE)(?![a-zA-ZÀ-ÿ])
\s*(\d+[ABab]?)?\s*(?:/\s*\d+)?\s*(?:[—–\-:]+\s*)?(.*)$
```

Traduzindo cláusula por cláusula — cada uma existe por causa de uma falha real:

| Cláusula | Aceita | Por que existe |
|---|---|---|
| `(?:\*{1,2}\|#{1,4}\|>)?` | `**IMAGE 01**`, `## IMAGE 01`, `> IMAGE 01` | texto colado de markdown |
| `(?![a-zA-ZÀ-ÿ])` | bloqueia `IMAGENS`, `IMAGEM` | o separador decorativo `--- IMAGENS ---` virava bloco |
| `(\d+[ABab]?)?` | `01`, `3`, `03A` | takes desdobrados (`03A`, `03B`) |
| `(?:/\s*\d+)?` | `01/05` | é a grafia que os motores emitem |
| `[—–\-:]+` | `—`, `–`, `-`, `:` | travessão, hífen e dois-pontos, em qualquer combinação |
| `(.*)$` | resto da linha | **o conteúdo pode começar na mesma linha do cabeçalho** |

Três limpezas rodam junto:

- **`normalizeText`** — mata zero-width (`​`), BOM, soft-hyphen e nbsp, e
  normaliza CRLF. ⚠️ **Foi o bug mais caro do histórico**: o parser caía no
  fallback de "1 bloco" porque o copy/paste trazia caractere invisível colado no
  `I` de `IMAGE`. Nada na tela denunciava.
- **`isSeparator`** — descarta `---`, `=====`, `--- IMAGENS (VIDEO 1) ---`.
- **`stripBeatLabel`** — corta o rótulo do beat do começo do conteúdo (`HOOK:`,
  `CTA + REFORÇO —`), pra não virar prompt.

### Só no TAKE: `stripMetadata`

Linhas que começam com `Copy falada:` ou `Contagem:` são removidas do prompt de
animação. São anotação de produção, não direção de cena.

> ⚠️ **`Dialogue:` e `Audio:` NÃO são removidos — e é assim que tem que ser.**
> Eles são o prompt. Se algum dia um agente emitir uma linha de metadado nova,
> ela entra no `stripMetadata` — nunca no `stripBeatLabel`.

### O que acontece com bloco sem número

Vai pra fila e ocupa o **primeiro slot livre**, na ordem de chegada. Se sobrar
bloco sem slot, a flag `ignored` acende e a barra lateral avisa.

---

## O CABEÇALHO `REF` FAZ PARTE DO BLOCO — corrigido em 2026-07-31

Descasamento achado ao conferir a integração motor → ferramenta, **já
corrigido nos quatro motores**.

Os motores emitiam o bloco de referência com a chave de exibição
`BLOCO 0 (REF)`, mas o **conteúdo começava direto** em `Photo of a real
person, ...` — sem a palavra `REF` na frente. Os blocos `IMAGE`/`TAKE`, esses
sim, sempre carregaram o cabeçalho inline (`IMAGE 01/05: ...`).

Colado no mesmo textarea dos IMAGE, o parser lia a referência como **bloco
anônimo**, tentava encaixar num slot livre, não achava (os cinco já numerados)
e **descartava** acendendo `ignored`. O painel ficava em "Sem referência" — e o
lote saía com cinco pessoas diferentes, que é exatamente a falha que o REF
existe para impedir.

**A correção:** `montar()` agora emite `REF 01: Photo of a real person, ...`.
Uma linha em cada motor, e uma regra de linter em cada um para que não se perca:

```python
if not blocos.get("BLOCO 0 (REF)", "").lstrip().upper().startswith("REF"):
    achados.append(("ERRO", "BLOCO 0 sem o cabecalho REF: o AdBatch "
                            "descarta a referencia em silencio"))
```

> ⚠️ **A falha era silenciosa dos dois lados** — o motor não sabia que o
> cabeçalho fazia falta, e a ferramenta descartava sem erro. Por isso virou
> `ERRO` de linter e não comentário: falha silenciosa só se paga com trava
> mecânica.

O upload manual (`Flow.media.select`) continua existindo como fallback.

---

## ⭐ O ÍNDICE MANDA EM TUDO

A regra que amarra a cadeia inteira:

```
bloco N  →  imagem N  →  take N  →  vídeo N  →  video_0N.mp4
```

**Numera-se pelo índice de origem, nunca pela ordem em que a geração termina.**
Se o slot 02 falhar, o ZIP sai com `video_01.mp4`, `video_03.mp4`,
`video_04.mp4` — com o buraco, sem renumerar. Renumerar seria pior que a falha:
você perderia a correspondência com o roteiro.

---

## ARQUITETURA DA V5 (a referência)

```
types.ts            <- Status, Block, AdSlot, AppState
utils/parser.ts     <- parseBlocks(text, type) + mapBlocksToSlots(blocks, maxSlots)
components/UI.tsx   <- SectionLabel, StatusBadge, Shimmer, IconButton, SlotActionButton
App.tsx             <- o estado, o ciclo, a grade
```

### O estado é UM objeto

`AppState` carrega `stage`, `refBlock`, `slots[]`, `imageInput`, `videoInput`,
`isBatchProcessing`. Cada `AdSlot` carrega **os dois prompts e os dois medias**:

```ts
imagePrompt / imagePromptFromScript / imagePromptDirty
videoPrompt / videoPromptFromScript / videoPromptDirty
imageMediaId / imageBase64 / imageStatus
videoMediaId / videoBase64 / videoStatus
```

### ⭐ O par `FromScript` + `Dirty` — a peça mais importante da V5

É o que separa a V5 da V4. Um `useEffect` reparsa o texto colado **a cada
tecla** e sincroniza os slots. Mas:

```ts
imagePrompt: slot.imagePromptDirty ? slot.imagePrompt : scriptContent
```

> **Se você editou aquele card na mão, a sincronização não te atropela.**

Editar o prompt de um card acende `Dirty` e o rótulo vira **"Selo: Editado"**;
um botão **Restaurar** (ícone `undo`, âmbar) devolve o `FromScript`. Sem esse
par, ou o texto colado manda em tudo (e você não pode ajustar um card), ou os
cards congelam (e recolar o roteiro não faz nada).

### O ciclo de geração

| Função | Faz |
|---|---|
| `generateImage(slotId \| 'REF', prompt, refMediaId?)` | uma imagem; `'REF'` escreve em `refBlock` |
| `generateVideo(slotId, prompt, firstFrameMediaId)` | um vídeo I2V |
| `runImageBatch()` | REF bloqueante → `Promise.allSettled` nos slots |
| `runVideoBatch()` | `Promise.allSettled` nos slots que têm imagem |

Os dois lotes filtram `status !== 'success'`: **rodar o lote de novo preenche só
os buracos**, não refaz o que já deu certo. Regerar um slot bom é botão
individual, decisão sua.

### Detalhes de UX que a V5 acertou

- **Modal de preview** — clique no vídeo abre em `90vh` com `controls`; fecha
  no clique fora ou no `X`.
- **Um vídeo por vez** — listener global de `play` (fase de captura) pausa todos
  os outros. Sem isso, cinco áudios tocam juntos na hora da revisão.
- **Quadro Base ao lado do vídeo** — na etapa 2 cada cena mostra a imagem de
  origem (a 40% de opacidade, rotulada) **ao lado** do resultado. É o que
  permite julgar se o vídeo respeitou o frame.
- **Contador `{length}/4000`** por card, com corte em 4000 no `onChange` e de
  novo no `slice()` antes da chamada — o SDK rejeita acima disso.

---

## A FAMÍLIA — 5, 4 e 3 takes

| | V5 | V4 | V3 |
|---|---|---|---|
| Slots | 5 | 4 | 3 |
| Status | ⭐ **referência, redonda** | atrasada | a construir |
| ZIP | `adbatch_vertical_5.zip` | `adbatch_lote.zip` | `adbatch_vertical_3.zip` |

**O que muda de verdade é `maxSlots`.** Na V5 ele é o default de
`mapBlocksToSlots(blocks, maxSlots = 5)` e o `length: 5` do `Array.from` que
cria os slots. Todo o resto — parser, ciclo, UI, ZIP — é idêntico.

> É por isso que a V5 é a fonte: **portar é trocar uma constante**, não
> reimplementar. Quem reimplementa reintroduz os seis bugs do histórico.

### O atraso da V4 — o que falta

Levantado por leitura cruzada dos dois fontes, 2026-07-31:

| # | Falta na V4 | Gravidade |
|---|---|---|
| 1 | **Prompt editável por card** (`FromScript`/`Dirty`, selo, Restaurar) | 🔴 |
| 2 | **Modelo de vídeo errado** — `Omni Flash` em vez de `Veo 3.1 - Lite` | 🔴 |
| 3 | **Duração 4s** em vez de 8s | 🔴 |
| 4 | **Lote não é aguardado** — `forEach` sem `await`, `isGeneratingBatch` cai na hora; o botão nunca mostra progresso real | 🟡 |
| 5 | **Sem modal de preview** | 🟡 |
| 6 | **Sem "um vídeo por vez"** | 🟡 |
| 7 | **Sem Quadro Base ao lado** — o vídeo cobre a imagem no mesmo tile | 🟡 |
| 8 | **Sem teto de slots** — a grade cresce com o que for colado | 🟡 |
| 9 | **Sem contador por card** | 🟢 |

### ⚠️ E o inverso: duas coisas que a V4 tem e a V5 não

Não se atualiza a V4 apagando isto — e a V5 devia herdar:

| O que | Onde | Por quê importa |
|---|---|---|
| **Tag `REF:[id]` no card** | `refMediaIdUsed` gravado no item e exibido no rodapé | é a **prova visual** de que a referência entrou na requisição daquele slot. Foi criada justamente porque a ferramenta uma vez *disse* que anexava e não anexava |
| **Estado `waiting`** | slots ficam "aguardando referência" enquanto o REF gera | a V5 tem `'waiting'` no tipo e no `StatusBadge`, mas **nunca atribui** — o estado existe e está morto |

Some-se a isso um detalhe de arquivo: o download individual da V5 sai
**sem zero à esquerda** (`img_1.jpg`, `video_1.mp4`), enquanto o ZIP sai
`video_01.mp4`. A V4 padroniza os dois pelo `sanitizeFilename`. **A grafia certa
é a da V4.**

---

## REGRAS TRAVADAS (valem nas três)

1. **Não traduzir.** Prompt e roteiro vão pro modelo exatamente como colados.
   Eles nascem em inglês no motor do agente e é assim que o Veo os quer.
2. ⭐ **Os dois modelos são de PRIORIDADE BAIXA, sempre** (ordem do operador,
   2026-07-31):

   | | modelo | por quê |
   |---|---|---|
   | imagem | **`🍌 Nano Banana 2`** | prioridade baixa, **0 créditos** |
   | vídeo | **`Veo 3.1 - Lite [Lower Priority]`** | idem |

   **Fail-closed:** se o modelo pedido não estiver na lista, **não gera** e
   avisa em vermelho. Nunca cai em outro modelo, nunca num pago.

   ⚠️ **O nome tem que bater CARACTERE POR CARACTERE com o seletor do Flow —
   emoji e colchetes inclusos.** Nome inexistente faz o SDK cair no modelo
   padrão, que é pago, e **falha em silêncio**.

   > **O caso que produziu a regra.** A spec original da ferramenta já pedia
   > prioridade baixa nos dois. O construtor implementou os nomes **sem o
   > sufixo** — `"Veo 3.1 - Lite"` em vez de `"Veo 3.1 - Lite [Lower
   > Priority]"`, e `"🍌 Nano Banana Pro"` no lugar de um gratuito. As três
   > ferramentas queimaram cota paga por semanas sem ninguém ver, até o limite
   > diário do Nano Banana Pro estourar em produção.
   >
   > **A regra existia e não foi verificada** — que é o mesmo defeito do
   > `two fully clothed adults`: escrever a regra não a implementa.

   ⚙️ **Por isso o painel mostra `IMG MODEL` e `VID MODEL` no rodapé.** Sem
   isso não havia como saber qual modelo estava rodando sem abrir o `App.tsx`
   — e foi o rodapé que diagnosticou o problema em dez segundos. **Não
   remover.**

   **Como conferir se um modelo é gratuito:** selecione-o no compositor
   principal do Flow e leia a linha *"A geração vai usar X créditos"*. É a
   fonte autoritativa; não deduza pelo nome.
3. **Uma imagem = um enquadramento.** Jamais colagem, grade, mosaico ou
   storyboard dentro de um frame. Um bloco, uma chamada.
4. **9:16 sempre.** Vídeo de 8 segundos.
5. **Teto de 4000 caracteres por prompt**, cortado antes da chamada.
6. **O índice manda** (ver acima).

---

## GOTCHAS

| Sintoma | Causa provável | Saída |
|---|---|---|
| "1 bloco detectado" com texto cheio de cabeçalhos | caractere invisível colado no cabeçalho | é o que o `normalizeText` resolve — confira que ele existe no parser |
| Painel "Sem referência" com REF colado | o bloco REF está sem o cabeçalho | os motores já emitem `REF 01:` desde 2026-07-31 — se sumiu, o linter acusa |
| Cinco pessoas diferentes no mesmo lote | o `mediaId` do REF não entrou em `referenceImageMediaIds` | guardar o ID em estado **não basta** — ele tem que entrar na requisição de cada slot |
| Botão "Gerar Vídeos" desabilitado com takes colados | nenhum slot correspondente tem imagem em `success` | a etapa 2 depende da 1: `TAKE 0N` anima a **imagem do slot N** |
| Prompt some ao recolar o roteiro | falta o par `FromScript`/`Dirty` | é o item 1 do atraso da V4 |
| Blocos somem acima do teto | comportamento correto | o aviso de excedente tem que estar visível, nunca silencioso |

---

## COMO SE MEXE NISSO

A ferramenta não tem repositório: ela vive no **Criador de Ferramentas do
Flow**, e se edita **por prompt em linguagem natural**. Isso muda o método.

> **O editor regride.** No histórico da V4 está registrado: ao implementar o
> parser da etapa 2, ele **quebrou o parser da etapa 1** que já estava aprovado.
> E declarou "corrigido" duas vezes sem ter rodado teste nenhum.

Daí as três regras de edição — as mesmas do
[`RUNBOOK-bisseccao-moderacao`](RUNBOOK-bisseccao-moderacao.md), por motivo
idêntico:

1. **Um assunto por prompt.** Nunca dois.
2. **Lista explícita do que NÃO pode mudar**, no topo de cada prompt.
3. **Teste de aceitação com input literal**, e exigir que ele **mostre o
   resultado**, não que declare pronto.

A bateria pronta pra colar — atualização da V4 e criação da V3 — está em
[`adbatch-prompts-editor.md`](adbatch-prompts-editor.md).

---

## Conexões

- [`adbatch-prompts-editor.md`](adbatch-prompts-editor.md) — os prompts prontos para o Criador de Ferramentas
- [`../WORKFLOW.md`](../WORKFLOW.md) §Passo 3 — o lugar da ferramenta no funil
- [`RUNBOOK-app-offline.md`](RUNBOOK-app-offline.md) — os agentes `.exe` que produzem o texto de entrada
- [`RUNBOOK-bisseccao-moderacao.md`](RUNBOOK-bisseccao-moderacao.md) — mesma disciplina de variável única, aplicada à moderação
- [`../veo-editor/README.md`](../veo-editor/README.md) — o que recebe o ZIP na saída
