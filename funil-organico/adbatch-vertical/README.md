# 📦 Código-fonte das duas ferramentas do Flow

Transcrito do editor do Google Flow em **2026-08-07**, a pedido do operador.

| pasta | ferramenta | o que faz |
|---|---|---|
| `adbatch-vertical/` | **AdBatch Vertical 3 · v2.5** | roteiro → 3 imagens → 4 variantes de vídeo por slot |
| `montador-vertical-3/` | **Montador Vertical 3** | 3 vídeos prontos → ordena → `adbatch_vertical_3.zip` |

⚠️ **Isto é transcrição, não export.** O painel do Flow perde recuo ao copiar,
então a **indentação foi reconstruída**. Identificadores, tipos, literais e
constantes de configuração estão fiéis. O JSX puramente cosmético (layout,
classes Tailwind repetidas, o `<style>` injetado) foi omitido e está marcado
onde falta. Se a fonte da verdade for necessária, ela continua sendo o editor
do Flow — este arquivo existe para **doutrina**, não para recompilar.

A doutrina de uso (etapas, contrato de entrada, família 5/4/3) vive em
[`RUNBOOK-adbatch-vertical.md`](../RUNBOOK-adbatch-vertical.md). Este README
documenta o que só o **código** revela.

---

## ⭐⭐ O QUE O CÓDIGO REVELA, e nenhum dos nossos documentos dizia

### 1. O vídeo é pedido com `durationSeconds: 10`, não 8

```ts
await Flow.generate.video({
  prompt: slot.videoPrompt.prompt,
  modelDisplayName: VIDEO_MODEL,
  aspectRatio: '9:16',
  durationSeconds: 10,          // <──
  firstFrameImageMediaId: slot.imageMediaId,
});
```

Toda a nossa doutrina de teto de fala está calibrada em **8 segundos a
3,1 palavras/s = 25 palavras** (`medir_teto_fala.py`, `TETO_FALA` nos 19
motores). O código pede **10 segundos**.

⚠️ **Não conclua daí que o teto pode subir.** Há duas leituras e o código não
decide entre elas: ou o modelo entrega 10s e temos 6 palavras de folga por
cena, ou ele trunca em 8s e o parâmetro é aspiracional. **É medição de campo,
não de código** — cronometrar um take renderizado resolve em um minuto. Até
lá, o teto de 25 fica, porque errar para menos custa silêncio e errar para
mais custa fala cortada, que mata o CTA.

### 2. O modelo de vídeo é `Omni Flash`, não Veo 3.1

```ts
const IMAGE_MODEL = '🍌 Nano Banana 2';
const VIDEO_MODEL = 'Omni Flash';
const VALID_VIDEO_MODELS = ['Omni Flash', 'Veo 3.1 - Lite', 'Veo 3.1 - Fast', 'Veo 3.1 - Quality'];
```

Nossa doutrina de prompt é [`DOUTRINA-VEO-3.1.md`](../../recursos/DOUTRINA-VEO-3.1.md)
e a ferramenta está configurada em **Omni Flash**. Os quatro modelos estão na
lista válida — trocar é uma constante —, mas hoje **o que roda não é o modelo
para o qual a doutrina foi escrita**. Vale saber antes de culpar o prompt por
um comportamento estranho.

⭐ E há uma trava boa: se a constante não estiver na lista válida, o app
**bloqueia a geração inteira** em vez de cair num default. Um rename do lado do
Google vira erro visível, não lote gerado no modelo errado.

### 3. O prompt é truncado em 4.000 caracteres, em silêncio

```ts
const content = block.content.slice(0, 4000);
```

Vale para IMAGE **e** para TAKE. Não há aviso na tela: o texto simplesmente
chega cortado no meio da frase.

**Medido em 2026-08-07 nos 19 motores, 60 sorteios cada — maior bloco emitido:**

| motor | maior bloco | folga |
|---|---|---|
| `necrose` | 3.385 | 15% |
| `ressurreicao` | 3.206 | 20% |
| `exterior` | 2.429 | 39% |
| `colo` | 2.423 | 39% |
| os outros 15 | ≤ 1.959 | ≥ 51% |

**Zero estouros hoje.** Mas `necrose` está a 615 caracteres do corte — uma
ampliação de pool descuidada chega lá. Quem mexer nesses dois mede antes.

### 4. O REF é gerado a partir do bloco `REF` e amarra as três cenas

Se há bloco `REF` no roteiro e nenhuma imagem carregada à mão, o app gera a
referência **primeiro** e passa o `mediaId` dela como `referenceImageMediaIds`
nas três imagens. É a máquina que segura o mesmo rosto nas três cenas — e é por
isso que o `BLOCO 0 (REF)` dos motores existe.

⚠️ Se o REF falhar, o app **aborta o lote** (`return` dentro do `catch`). Não
gera as três imagens sem referência.

### 5. Rodar o lote de novo não queima crédito no que já deu certo

```ts
const slotsToGenerate = slots.filter(s => s.imageStatus !== 'success' && ...);
```

Só slots que ainda **não** tiveram sucesso entram. Para forçar, use o
`Regerar Imagem` do card.

### 6. A sequência de vídeo é serial por slot, paralela por variante

`triggerVideoSequence` faz `await` slot a slot (1 → 2 → 3) e dispara as **4
variantes** de cada slot em paralelo. O ZIP leva **só as variantes marcadas**
(`chosenIndex`); slot sem escolha fica de fora, e o rodapé lista quais faltam.

---

## O CONTRATO DO PARSER, linha a linha

O `parseBlocks` é o que separa nosso `.txt` em blocos. Três funções antes dele:

**`normalizeText`** — mata CRLF, zero-width (U+200B a U+200D, U+FEFF, U+2060),
soft hyphen (U+00AD) e converte NBSP (U+00A0) em espaço.
⭐ Isso nos protege de um erro que já cometi cinco vezes nesta base: caractere
invisível entrando no fonte por heredoc. O parser limpa — mas o `medir_contexto_copy --gate`
continua sendo a rede de verdade, porque ele acusa **antes** de virar prompt.

**`cleanContent`** — descarta linha decorativa (`-----`, `--- x ---`) e, **só
no TAKE**, linhas que começam com `Copy falada:` ou `Contagem:`.
⚠️ Repare no que **não** está nessa lista: `Dialogue:` e `Audio:` **passam** e
chegam ao modelo. É exatamente por isso que a fala precisa sair como
`Dialogue: "..."` — foi o defeito que deixou o FALTA gerando vídeo mudo.

**`removeLabels`** — remove do **início** do bloco os rótulos
`HOOK|CTA|REFORÇO|MECANISMO|INTRO|BODY|OUTRO|OFERTA` seguidos de `+ : — – -`.
⛔ Ou seja: um bloco que começasse com `HOOK — Medium shot...` perderia o
`HOOK —`. Nossos motores não usam esses rótulos no início do bloco; se algum
passar a usar, some.

**O cabeçalho:**

```js
/^(?:[*#> ]+)?(REF|IMAGE|TAKE)(?![A-Z])(?:\s*(\d+))?(?:[A-Z])?(?:\/\d+)?(?:\s*[:—–-])?\s*(.*)$/i
```

- aceita `*`, `#`, `>` e espaço antes (markdown colado)
- `(?![A-Z])` impede `IMAGES` de virar cabeçalho
- o índice é o **primeiro número**: em `IMAGE 01/03` ele lê `01` → `1`, e o
  `/03` é descartado
- tudo o que vem depois do cabeçalho **na mesma linha** já entra no conteúdo

---

## MONTADOR VERTICAL 3 — o que ele impõe

- **HOOK / MECANISMO / CTA são travados por índice**, na marra
  (`slot.index === 0 ? 'HOOK' : ...`). A ferramenta assume a família de 3
  takes; não há configuração.
- **O nome do arquivo é o número do slot**: `video_01.mp4`, `video_02.mp4`,
  `video_03.mp4`. ⛔ E o `forEach` percorre os três em ordem escrevendo só os
  preenchidos — então **pacote incompleto sai com buraco**, `video_01` +
  `video_03`, sem renumerar.
- **Só um vídeo toca por vez**, via listener de `play` na fase de captura.
- ⚠️ `handleSwap` faz cópia **rasa** (`[...prev]`) e escreve dentro dos objetos
  originais. Funciona hoje porque o array novo força re-render; quebra no dia
  em que alguém memoizar o slot.

---

## Conexões

- [`RUNBOOK-adbatch-vertical.md`](../RUNBOOK-adbatch-vertical.md) — a doutrina
  de uso, o contrato de entrada e a família 5/4/3
- [`adbatch-prompts-editor.md`](../adbatch-prompts-editor.md) — os prompts
  prontos para o Criador de Ferramentas. ⚠️ **Um assunto por prompt** — o
  editor regride
- [`licoes-producao-veo.md`](../licoes-producao-veo.md) — as lições pagas em
  campo, do lado do modelo
