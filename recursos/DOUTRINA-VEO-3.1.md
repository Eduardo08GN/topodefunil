# 🎬 Doutrina Veo 3.1 — documento mãe

**Para o agente que chegou agora.** Leia isto inteiro antes de escrever um único prompt
de vídeo. Ao terminar, você sabe como o Veo 3.1 se comporta, por que ele falha, e como
não induzir as falhas.

- **Status:** ✅ operacional · **Compilado em:** 2026-07-28
- **Escopo:** o modelo. Como o Veo pensa, o que ele premia, o que ele quebra.

> ⛔ **Este documento não contém as nossas regras de produção.** Formato de entrega,
> descrição de persona, estética iPhone, anti-bloqueio do nicho e checklist operacional
> vivem **só** no [`AGENTE_ED_ORGANIC_WAVE_V4.md`](../AGENTE_ED_ORGANIC_WAVE_V4.md).
> Aqui é o *porquê*; lá é o *como fazemos*. Regra mecânica duplicada envelhece e passa
> a mentir — já aconteceu neste repo em 2026-07-28.

---

## 1. O MODELO EM 60 SEGUNDOS

Veo 3.1 (Google DeepMind) é o único gerador grande com **áudio nativo sincronizado**:
diálogo, efeitos e trilha nascem junto com a imagem, e o **lip-sync é nativo**. Isso é o
diferencial dele e também a origem de metade dos problemas — porque a sintaxe da fala
importa de um jeito que não importa em nenhum outro modelo.

| Capacidade | Veo 3 | Veo 3.1 |
|---|---|---|
| Text-to-video | ✅ | ✅ |
| **Image-to-video (first frame)** | ❌ | ✅ |
| **Reference ingredients** (múltiplas refs) | ❌ | ✅ |
| Alinhamento de áudio | bom | preciso ao frame |
| Diálogo multi-pessoa | monofônico na prática | direcionado |

**Duração.** A referência de sintaxe fala em clipes de 4/6/8s; material mais recente
cita até 60s no 3.1 com decupagem inteligente. ⚠️ **Fontes divergem.** Na nossa esteira
(Google Flow, Veo 3.1 Lite) o clipe é de **8 segundos** — trate 8s como o teto real e
ignore a promessa de 60s até medir.

**Teto de fala: ~8 segundos de áudio falado por clipe**, independente da duração do
vídeo. Passar disso faz a locução acelerar de forma não-natural.

---

## 2. A LEI FUNDAMENTAL — ORÇAMENTO DE ATENÇÃO

**Faixa ótima: 100-150 palavras.** Abaixo de ~50 o modelo improvisa; acima de ~200 ele
faz *cherry-picking* — **descarta silenciosamente parte do seu prompt**.

Esta é a lei mais violada e a que explica mais bugs. Quando um prompt de 250 palavras
"ignora" a sua instrução anti-glitch, o modelo não desobedeceu: **ele nunca leu**. Você
gastou o orçamento em adjetivo.

**Peso no começo.** O gerador dá mais atenção aos primeiros 30-40% dos tokens. Ordem:

```
[Câmera / enquadramento]  ← primeiro, sempre
[Sujeito / ação]
[Ambiente]
[Luz / atmosfera]
[Estilo / paleta]         ← modificadores de qualidade por último
[Áudio]
[Duração]
```

Instrução de câmera declarada **depois** da ação é ignorada. Não é bug, é orçamento.

- ⛔ `A man opens the fridge. The camera is a slow push-in.`
- ✅ `Slow 50mm push-in. A man opens the fridge.`

**Corolário:** cada palavra que você gasta re-descrevendo algo que o modelo já sabe é
uma palavra roubada da instrução que você precisa que ele obedeça.

---

## 3. SINTAXE DA FALA (a parte única do Veo)

A forma canônica tem **três partes, nenhuma opcional**:

```
He says: "raw garlic on corn and your wife won't keep up"
└verbo┘  └:┘ └──────────────── aspas ────────────────┘
```

| Forma | Resultado |
|---|---|
| `He says: "..."` | ✅ canônica — dois-pontos é mais confiável que vírgula |
| `He says, "..."` | 🟡 funciona |
| `He says: ...` sem aspas | ⛔ **quebra o lip-sync** |
| `"..."` solto, sem verbo | ⛔ pior de todos |

**Modificadores de voz vão antes do verbo:** `He says in a weary voice: "..."` ·
`She whispers nervously: "..."` · `He shouts excitedly: "..."`

> ⚠️ **Mito derrubado.** Circula na internet que as aspas causam a legenda queimada e
> que a solução é removê-las. **É falso e custa caro.** As aspas são o que marca a fala
> para o lip-sync; tirá-las conserta a legenda e arrebenta a sincronia labial. A legenda
> se combate com negativo (§7), não mutilando a sintaxe.

---

## 4. ÁUDIO — PRECISA DE RÓTULO

O Veo **não infere** que deve gerar áudio a partir da descrição visual. Sem rótulo
explícito, o modo de falha é "áudio ausente na saída". Rótulos em **linha própria**:

```
Dialogue: He says: "just hear me out"
Audio: quiet kitchen room tone, faint refrigerator hum
SFX: (spoon tapping ceramic at 2 seconds)
```

As quatro camadas, da mais simples à mais rica:

1. **Ambiente:** `Audio: wind through grass, distant crickets.`
2. **Efeito direcionado:** `Audio: crunchy snap with each keystroke.`
3. **Diálogo + ambiente:** as duas linhas juntas.
4. **Paisagem completa:** múltiplas falas nomeadas + SFX + trilha.

---

## 5. IMAGE-TO-VIDEO — A REGRA DE OURO

**No I2V a imagem é o first frame. Não re-descreva o que já está nela.**

> *"Do not re-describe static elements. Describe only motion, camera, light change,
> and audio."*

Abra sempre com a âncora de identidade:

```
Maintain the subject from the first frame.
```

Re-descrever rosto, roupa, idade e cenário no prompt de animação faz **três** estragos
de uma vez:

1. Estoura o orçamento de palavras → o modelo descarta o resto (inclusive o anti-glitch)
2. **Convida o modelo a re-gerar** o rosto em vez de preservá-lo → morphing
3. Rouba espaço da descrição de movimento, que é a única coisa que o I2V precisa

**Isto inverte a intuição do text-to-video**, onde repetir o bloco de identidade em todo
clipe é obrigatório (o gerador não tem memória entre gerações). No I2V a memória é a
imagem. Saber em qual dos dois você está é metade do trabalho.

---

## 6. CONSISTÊNCIA DE PERSONAGEM

Ordenado do mais fraco ao mais forte.

| Técnica | Como | Força |
|---|---|---|
| Bloco de identidade repetido | mesma descrição literal em todo prompt T2V | 🟡 fraca — texto não trava rosto |
| First frame (I2V) | `maintain the subject from the first frame` | 🟢 boa, dentro do clipe |
| **Reference ingredients (3.1)** | subir várias refs e citá-las no prompt | 🟢 forte |
| **Character sheet multi-ângulo** | uma imagem-carta com vários ângulos do rosto | 🟢 forte |
| **Grade 3×3** | 9 ângulos numa imagem só, usada como referência | ⭐ mais estável hoje |
| Modelo de rosto treinado | ex. Soul ID — 5-20 fotos, identidade persistente | ⭐ estrutural, outra plataforma |

**Reference ingredients** — a sintaxe é por citação:

```
The character from reference_1 walks into the location from reference_2
holding the object from reference_3.
```

**Character sheet** — prompt para gerar a carta de ângulos no gerador de imagem:

```
Create multiple different angles of this character: front-facing, left profile,
right profile, back of the head, side of the head. Clean white background.
```

A **grade 3×3** (nove ângulos numa imagem) é hoje mais estável que a 2×2 e cobre mais
ângulos. Usada como referência única, ela ancora melhor que uma frontal solta.

---

## 7. MODOS DE FALHA → CAUSA REAL → FIX

A tabela mais importante do documento. **O sintoma quase nunca é a causa.**

| Sintoma | Causa real | Fix |
|---|---|---|
| **Legenda queimada e embaralhada** | o Veo transcreve toda fala por padrão | negativo `no subtitles, no captions, no burned-in text, no on-screen text` — e no I2V também na **imagem**, senão o vídeo herda |
| **Mão extra / terceira mão** | duas ações de mão simultâneas no mesmo prompt | **uma** ação de mão por cena; mão ociosa declarada parada; prop herói consome as duas; mais o negativo `exactly ten fingers total visible, no extra hands, no extra limbs, only two arms visible` |
| **Prop flutuando** | objeto sem contato declarado, ou nascendo só no vídeo | amarração explícita + `no floating objects`; no I2V a **mão já tem que estar segurando no frame inicial** |
| **Prop some no meio** | estado do objeto não declarado por beat | declarar a trajetória: `counter -> both hands -> still in both hands` |
| **Anti-glitch ignorado** | prompt acima de ~200 palavras → cherry-picking | cortar para 100-150 |
| **Rosto muda entre cenas** | re-descrição no I2V convidando re-geração | `maintain the subject from the first frame` + parar de re-descrever |
| **Locução acelerada** | mais de ~8s de fala no clipe | cortar a linha; ler em voz alta para medir |
| **Áudio ausente** | falta rótulo `Audio:` / `Says:` / `SFX:` | rotular em linha própria |
| **Câmera ignorada** | instrução de câmera no meio ou no fim | mover para o começo |
| **Cor do objeto muda ao mexer no clima** | *concept bleed* — palavra de humor vazando para o objeto | migrar para JSON, travar o objeto no bloco de continuidade |
| **Luz derivando entre clipes** | fonte de luz não nomeada | nomear fonte + direção e repetir **palavra por palavra** em todos os clipes |
| **Rosto com cara de IA** | *tag spam* de qualidade | trocar por linguagem de produção |

### Negativo no Veo: cuidado

**O Veo não tem campo de negative prompt separado** — o negativo vai no corpo e consome
orçamento. Consequências:

- Negativo **curto e essencial** apenas. Lista gigante come as palavras que importam.
- Para **anatomia**, existe a hipótese de que **frase positiva** funcione melhor que a
  negação — `anatomically correct hands, clean finger separation, realistic proportions` —
  porque repetir "hands" na negativa pesaria o token e aumentaria a alucinação.
  ⚠️ **É hipótese em aberto (A/B nº 2), não regra.** O **padrão vigente continua sendo o
  negativo dos dez dedos**, que é obrigatório em toda cena — ver
  [V4](../AGENTE_ED_ORGANIC_WAVE_V4.md), *Anti-glitch*. Não troque em lote antes de medir.
- O negativo de **legenda** é exceção: é curto, é necessário, e vai nas duas pontas.

---

## 8. JSON — QUANDO A PROSA NÃO SEGURA

O Veo parseia JSON estruturado. Isso separa fisicamente humor de objeto e **impede o
concept bleed**.

**Use JSON quando:** várias cenas numa geração · continuidade estrita de personagem ·
props que não podem mudar de cor/tamanho · a prosa começou a mudar o objeto quando você
acrescentou palavra de clima.

**Não use** para clipe simples — prosa é mais rápida e costuma sair melhor.

```json
{
  "version": "veo-3.1",
  "output": { "duration_sec": 8, "fps": 24, "resolution": "1080p", "aspect_ratio": "9:16" },
  "global_style": { "look": "...", "color": "...", "mood": "..." },
  "continuity": {
    "characters": [{ "id": "man", "description": "60s, silver buzz cut, navy henley" }],
    "props": ["unflavored gelatin packet"],
    "lighting_constant": "warm window light as key from frame-left"
  },
  "scenes": [{
    "id": "01", "start": "0.0", "end": "8.0",
    "shot": { "type": "medium close-up", "framing": "eye-level", "camera": "slow push-in, 50mm" },
    "action": "...", "environment": "...", "lighting": "...", "audio": "..."
  }]
}
```

O truque é onde as coisas moram: **humor em `global_style`**, **objeto em `continuity`**.
Assim o humor não pode vazar para a cor do objeto.

---

## 9. VOCABULÁRIO QUE RENDERIZA

**Lentes** — declare sempre, funciona em todos os modelos:

| Lente | Efeito |
|---|---|
| 24mm | amplo, imersivo, espaço exagerado |
| 35mm | documentário natural |
| 50mm | íntimo, perspectiva humana |
| 85mm | retrato, fundo comprimido |
| 100mm macro | textura, detalhe |

**Um movimento de câmera dominante por clipe.** Empilhar três em 8 segundos produz caos.
Um movimento principal + no máximo um micro-ajuste (leve tremor, rack focus sutil).

**Mostre, não conte.** O modelo não renderiza sentimento — renderiza corpo.

- ⛔ `He is scared.`
- ✅ `His jaw locks. He stops breathing for one beat. His fingers curl against the doorframe.`

**Palavras que não renderizam** e denunciam preguiça: *cinematic, professional, high
quality, masterpiece, stunning, epic, beautiful lighting, dynamic camera, 8k*. Elas
empurram o modelo para território de arte-de-IA. Troque por linguagem de produção:
`shot on 50mm, natural skin texture, motivated lighting, documentary feel`.

**Cada plano merece três detalhes físicos concretos:** uma pressão do ambiente (luz fria
da geladeira, vidro embaçado), uma micro-ação física (o maxilar trava, o nó do dedo
embranquece), e uma âncora sonora. Plano sem nenhum dos três é enchimento.

---

## 10. AUDITORIA ANTES DE GERAR

- [ ] Está entre 100-150 palavras? (I2V pode ficar em 80-150)
- [ ] A câmera está no **começo** do prompt?
- [ ] Se é I2V: abre com `maintain the subject from the first frame` e **não** re-descreve persona/cenário?
- [ ] A fala está como `verbo + dois-pontos + "aspas"`?
- [ ] A fala cabe em 8 segundos lidos em voz alta?
- [ ] Tem linha `Audio:` rotulada?
- [ ] **Uma** ação de mão por cena, mão ociosa declarada parada?
- [ ] Todo objeto na mão tem contato declarado e trajetória de estado?
- [ ] Negativo de legenda presente — e na imagem também, se for I2V?
- [ ] Um movimento de câmera dominante, não três?
- [ ] Zero *tag spam* de qualidade?
- [ ] Luz nomeada por fonte + direção, idêntica à das outras cenas do lote?

---

## 11. COMO EXPANDIR ESTE DOCUMENTO

Toda recusa, glitch ou descoberta nova entra **aqui** se for sobre o comportamento do
modelo, e no **V4** se for sobre a nossa forma de produzir. Na dúvida: *"isso valeria
para qualquer um usando Veo?"* → sim, entra aqui.

Registre **evidência de produção**, não opinião: o que foi pedido, o que voltou, o que
consertou. O selo de risco de bloqueio dos nossos dispositivos vive no
[`banco-hooks.md`](../funil-organico/banco-hooks.md) e segue essa mesma regra.

---

## Fontes

- **[smixs/visual-skills](https://github.com/smixs/visual-skills)** — `video/references/veo.md`,
  `universal-rules.md`, `fixes-and-skeletons.md`. Autor: Serge Shima. Licença CC BY 4.0.
  Origem da sintaxe de fala, do esquema JSON, da regra de I2V e da maioria da tabela de falhas.
- **[cclank/lanshu-awesome-ai-video-kit](https://github.com/cclank/lanshu-awesome-ai-video-kit)** —
  `methodology/12-veo-公式.md`, `06-约束词清单.md`, `20-realistic-character-consistency.md`.
  Origem das camadas de áudio, da faixa de 100-150 palavras e das técnicas de character sheet / grade 3×3.
- **Produção própria** — falhas reais registradas em 2026-07-27/28 (H9 bloqueado, H4 com
  "absurdly oversized", tripla mão do copo+colher, morphing do segundo personagem).

## Conexões

- [`AGENTE_ED_ORGANIC_WAVE_V4.md`](../AGENTE_ED_ORGANIC_WAVE_V4.md) — as nossas regras de IMAGE/TAKE
- [`AGENTE_ED_ORGANIC_WAVE_V6.md`](../AGENTE_ED_ORGANIC_WAVE_V6.md) — o agente de produção
- [`checklist anti-irrealidade`](generated-ai-video-anti-irrealidade-checklist.md) — guardrail de realismo
- [`WORKFLOW.md`](../WORKFLOW.md) — a operação inteira
