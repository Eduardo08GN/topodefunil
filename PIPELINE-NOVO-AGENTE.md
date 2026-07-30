# PIPELINE — COMO NASCE UM AGENTE NOVO

> **Para quem chega de memória virgem:** este arquivo é o mapa completo do
> processo que transforma **um reel garimpado de concorrente** em **um agente
> especialista versionado no repo**, e daí em **vídeos em produção**.
>
> Ordem de leitura para se contextualizar do zero:
> 1. [`CLAUDE.md`](CLAUDE.md) — as regras invioláveis e a alçada
> 2. [`WORKFLOW.md`](WORKFLOW.md) — a operação inteira (páginas, funil, agentes)
> 3. **este arquivo** — o pipeline de construção de agente
>
> Este arquivo descreve **o processo**. As regras de criativo moram nos agentes
> e na doutrina — aqui só se aponta para elas (regra P9: uma regra, um lugar).

---

## O QUE É UM "AGENTE" NESTE REPO

Não é código. É um **arquivo Markdown de doutrina** que um Claude lê para
produzir prompts de Veo de um ângulo específico. Três camadas coexistem:

| Camada | Arquivos | Papel |
|---|---|---|
| **Motor mecânico** | `AGENTE_ED_ORGANIC_WAVE_V4.md` (regras Veo) · `V5` (biblioteca de props/dispositivos) | como se escreve um IMAGE/TAKE. **Uma regra mecânica só existe aqui.** |
| **Engines** | `V6` (Kofi, 1 história × N hooks) · `PRISMA V1` (lote heterogêneo, 10 eixos + solver) | quem **sorteia a spec** e carrega as regras transversais (Porteiro, fio narrativo, PICO2, contraste, cota do órgão) |
| **Especialistas por ângulo** | os 15 `AGENTE_ED_<ANGULO>_V1.md` | quem **executa** a spec sorteada num ângulo específico. Enxutos: só o que é próprio do ângulo, o resto por ponteiro |

**O agente novo que você vai construir é sempre da terceira camada.** Se a
descoberta for uma regra mecânica de Veo, ela **não vira agente** — vira uma
linha no V4. Se for uma regra de copy transversal, vira uma seção no PRISMA ou
no arsenal. Agente novo só quando existe um **ângulo narrativo inteiro** novo:
uma cena, uma vítima, uma evidência, um arco.

---

## O PIPELINE — 8 ETAPAS

```
[1] garimpo        → o Ed manda o link do reel
[2] leitura ótica  → /watch frame a frame + transcrição
[3] mapa visual    → o que varia × o que não varia, elemento a elemento
[4] destilação     → os elementos viram REGRAS numeradas
[5] o arquivo      → AGENTE_ED_<ANGULO>_V1.md na anatomia padrão
[6] registro       → WORKFLOW.md + CLAUDE.md + (se preciso) randomizador
[7] primeiro vídeo → produzir 1 vídeo pelo agente = o teste do agente
[8] loop de campo  → cada recusa/falha de render volta como regra
```

---

## [1] GARIMPO — a entrada

O Ed manda um link e o que ele quer daquilo:

```
/watch https://www.facebook.com/reel/<id>
faça leitura visual do hook inicial (1 frame a cada segundo), mapeie a copy
visual desse vídeo e vamos partir para o building de um novo agente
```

**Critério para virar agente** (se não bater, o achado vira hook no banco, não
agente): números muito acima da média da página · uma **cena** reconhecível e
repetível · uma evidência visual que o espectador lê no mudo em meio segundo.

Casos que passaram no critério:

| Agente | Fonte | Números |
|---|---|---|
| **PEE** | Tanisha Rivers, reel 1669109991889559 | 1.5K / 583 / 311 — 20-50× a média da página |
| **VAZAMENTO** | Kofi, reel 1555163349606149 | 703 / 254 / 36 |
| **GEMEO** | Zariah, reel 1487684136039129 | **345K views / 7.7K** — o recorde do repertório |
| **CONSULTORIO** | Tanisha (maca) | 909 reactions, padrão repetido |

---

## [2] LEITURA ÓTICA — ver, não resumir

Receita completa: [`funil-organico/RUNBOOK-watch-videos.md`](funil-organico/RUNBOOK-watch-videos.md).
Reels de Facebook são login-walled — o happy path 2b (captura pela aba logada
do Chrome) é a rota validada.

```bash
python %USERPROFILE%\.claude\skills\watch\scripts\watch.py "<arquivo.mp4>" --resolution 640
```

Duas coisas que **não** podem ser puladas:

1. **Frame a frame no hook.** Os primeiros 4 segundos carregam o agente
   inteiro. No PEE, 25 frames a 1 fps renderam os 5 elementos obrigatórios do
   quadro — nenhum deles aparecia na transcrição.
2. **Copy visual ≠ copy falada.** Legenda queimada, karaoke, etiqueta de prop,
   posição do texto. Pedir explicitamente *"leitura ótica da copy visual"*.

Saída desta etapa: um **mapa visual** salvo em `concorrentes/<nome>-mapa-visual.md`
(modelo: [`concorrentes/tanisha-mapa-visual.md`](concorrentes/tanisha-mapa-visual.md)).

---

## [3] MAPA VISUAL — o que varia × o que não varia

A pergunta que organiza tudo: **o que este vídeo tem que os nossos não têm?**

Enumerar o quadro do hook **elemento por elemento**, e para cada um responder
*"se eu tirar isto, a cena ainda se lê?"*. O que sobrevive à pergunta é
decorativo; o que derruba a leitura é **obrigatório** e vira regra.

Exemplo real (PEE, hook da Tanisha) — 5 elementos, nenhum opcional:

| # | Elemento | Por que é obrigatório |
|---|---|---|
| 1 | mancha escura na frente de bermuda **clara** | o contraste é o que faz a leitura em meio segundo |
| 2 | vítima **chorando muito**, olhando a própria mancha | sem choro é acidente engraçado; com choro é ruína |
| 3 | narrador **agachado num joelho** apontando a mancha | a assinatura da cena |
| 4 | plateia rindo **e apontando** | sem plateia não há flagrante |
| 5 | loja genérica, zero marca | P12 — marca legível derruba o vídeo |

Exemplo real (VAZAMENTO, Kofi) — as 4 novidades do ângulo: o REF **é** o
corpo-prova · o prop **vaza** · a receita de mercado como isca · a virada
*"sem X isso não basta"*.

---

## [4] DESTILAÇÃO — elemento vira REGRA numerada

Cada elemento obrigatório vira uma regra com **prefixo próprio do agente** e
número, para poder ser citada em qualquer lugar do repo sem ambiguidade.

**Registro de prefixos já ocupados** (⚠️ escolher um livre e registrar aqui):

| Prefixo | Agente | Prefixo | Agente |
|---|---|---|---|
| `P` | PRISMA (engine) | `F` | FLAGRANTE |
| `PE` | PEE | `V` | VAZAMENTO |
| `CN` | CONSULTORIO | `ED` | ELA_DIAGNOSTICA |
| `G` | GEMEO | `R` | RESSURREICAO |
| `Q` | DEMO_QUIMICA | `S` | SUBSTANCIA_ABSURDA |
| `DG` | DIAGNOSTICO | `C` | CONSEQUENCIA |
| `N` | ELA_NARRADORA | `K` | CONFISSAO |
| `Y` | DIARIO | `U` | GUERRILHA |
| `UN` | UNCAO | | |

**Anatomia de uma regra boa** (o padrão da casa, ver PE2, F12, F15):

- **enunciado curto em negrito** — o que é, em uma linha
- **por que existe** — a falha de produção ou a evidência que a gerou
- **frase travada** para o IMAGE, verbatim, pronta pra copiar
- **frase travada para o TAKE**, quando o comportamento no movimento difere
- **⛔ o que é proibido**, com o token exato que já bloqueou

> ⚠️ **Adjetivo não dimensiona, categoria não desenha.** As duas lições que
> mais geraram regra: `muscular`/`large`/`small` sozinhos não renderizam —
> exigem **âncora de escala** (`no longer than his thumb`, `as thick as her
> wrist`) ou **grupo nomeado** (`broad chest, thick arms`). E descrever prop
> por **sistema** (`the male reproductive system`) entrega o corte errado —
> descreve-se por **objeto + geometria**. Fonte:
> [`funil-organico/prop-metaforas.md`](funil-organico/prop-metaforas.md).

---

## [5] O ARQUIVO — anatomia padrão do agente

`AGENTE_ED_<ANGULO>_V1.md` na **raiz** do repo. Copiar o esqueleto do
[`AGENTE_ED_FLAGRANTE_V1.md`](AGENTE_ED_FLAGRANTE_V1.md) — é a **referência
arquitetural** declarada pelo operador.

Seções, nesta ordem:

| # | Seção | Conteúdo |
|---|---|---|
| 0 | **Banner** | agente paralelo, não substitui V4/V5/V6/PRISMA; mecânica por ponteiro |
| 1 | `## POR QUE ESTE AGENTE EXISTE` | a fonte + os **números** + o que difere dos ângulos vizinhos |
| 2 | `## ANTES DE ESCREVER — O PORTEIRO` | ponteiro pro PRISMA §Porteiro, com a nota do que é próprio daqui |
| 3 | `## PASSO 0 — SPEC` | como a spec entra: sorteio no randomizador ou **comissão do operador** |
| 4 | `## O HOOK — OS N ELEMENTOS OBRIGATÓRIOS` | o mapa visual da etapa [3], em prosa executável |
| 5 | `## O ARCO — 5 CENAS` | tabela cena / beat / o que a copy FAZ / o que a tela mostra |
| 6 | `## REGRAS PRÓPRIAS (<PREFIXO>1-N)` | as regras da etapa [4] |
| 7 | `## SELO DE RISCO` | 🟢 validado · 🟡 A/B não testado · 🔴 já bloqueou — **e a fila de reformulação** |
| 8 | `## MECÂNICA — POR PONTEIRO` | tabela assunto → arquivo-fonte. **Nunca copiar regra do V4/PRISMA pra cá (P9)** |
| 9 | `## CHECKLIST <ANGULO>` | um item por regra própria + os testes herdados |
| 10 | `## ⛔ RECUSA DO GERADOR` | **bloco obrigatório em todo agente** — copiar de qualquer agente existente |
| 11 | `## Conexões` | links para os agentes e docs irmãos |

⚙️ **A seção 10 é obrigatória por ordem do `CLAUDE.md`** — todo `AGENTE_ED_*.md`,
os existentes e os que vierem, carrega o bloco `## ⛔ RECUSA DO GERADOR` logo
antes de `## Conexões`. Fonte da verdade:
[`funil-organico/prop-metaforas.md`](funil-organico/prop-metaforas.md) §Recusa
do gerador.

**O agente é ENXUTO.** Se a informação já existe no V4, no PRISMA, no arsenal
ou no prop-metaforas, aponta-se. Cópia envelhece e mente — foi a conclusão da
auditoria que criou a regra P9.

---

## [6] REGISTRO — o agente tem que ser encontrável

Três lugares, sempre os três:

1. **[`WORKFLOW.md`](WORKFLOW.md)** — linha na tabela de agentes, com o ângulo
   em uma frase e as **evidências numéricas**.
2. **[`CLAUDE.md`](CLAUDE.md)** — atualizar a contagem ("15 agentes") e a
   descrição curta na lista de especialistas.
3. **[`funil-organico/randomizador-prisma.py`](funil-organico/randomizador-prisma.py)**
   — só se o ângulo introduzir um **conceito novo** ou valores novos de eixo.
   Enquanto não entrar no randomizador, o agente roda por **comissão do
   operador** (é o caso do PEE hoje) — e isso fica escrito no PASSO 0 dele.

---

## [7] PRIMEIRO VÍDEO — o agente só existe depois de rodar

Um agente que nunca produziu um vídeo é hipótese, não doutrina. O primeiro
vídeo é o teste do arquivo: onde ele for ambíguo, você vai travar.

Sequência de produção (vale para todo agente):

```bash
# quando o ângulo tem conceito no randomizador:
python funil-organico/randomizador-prisma.py --pagina <joe|marcus|ray|chuck|matt> --n 1
```

- A spec sorteada é **executada**, não escolhida (P1). Se o relatório do PRISMA
  disser **REPROVADO (< 70% de pares distintos), o lote não é escrito.**
- **Congruência de casting:** etnia do REF = etnia do avatar da página
  (Joe/Ray/Matt brancos · Marcus/Chuck negros). REF é **solto por vídeo**;
  só a etnia é travada, e a marca facial sorteada é obrigatória.
- **Formato de entrega, sempre:** `BLOCO 0 (REF)` → **os 5 IMAGEs agrupados**
  → **os 5 TAKEs agrupados**. Nunca intercalar.
- CTA travado em **GELATIN** + follow-gate na cena 5. `BOOK`/`YES` são
  proibidos (quebram a automação DM).
- Fechar com a **auditoria do checklist** na resposta — cota do órgão contada,
  orçamento de fala somado, storyboard mudo em uma palavra por cena, e os
  riscos 🟡 nomeados.

Daí segue o pipeline de mídia normal do [`WORKFLOW.md`](WORKFLOW.md):
AdBatch → Veo Editor → postagem.

---

## [8] LOOP DE CAMPO — a doutrina cresce por evidência, nunca por improviso

**Toda falha de produção volta como regra.** É de onde vem a maioria do que
está escrito nos agentes hoje: `F12` nasceu do proxy que saiu longe do quadril,
`F15` do still mole entregue como redenção, `PE2` do choro que faltava, a regra
do REF musculoso dos REFs raquíticos, o §D1 do modelo anatômico que veio corte
abdominal.

Ao registrar, sempre: **o que falhou · a causa diagnosticada · a frase travada
que resolve · o token proibido.** Data e caso ("falha em produção,
Chuck/churrasco 2026-07-28") — é isso que impede a regra de ser revogada por
palpite depois.

### ⛔ E o limite de alçada, que vale em todas as 8 etapas

> **Nunca alterar COPY ou CENA por conta própria. Consultar o Ed antes,
> sempre.**

Diante de recusa do gerador: isolar a variável → **reescrever a forma de
dizer** mantendo cena e copy intactas → esgotar 3-4 formulações → **reportar ao
Ed com o diagnóstico e as opções**. Amputar o bit visual destrói justamente o
que fazia o vídeo converter, e a decisão não é do agente.

---

## Conexões

- [`WORKFLOW.md`](WORKFLOW.md) — a operação inteira · [`CLAUDE.md`](CLAUDE.md) — regras invioláveis e alçada
- [`AGENTE_ED_PRISMA_V1.md`](AGENTE_ED_PRISMA_V1.md) — engine + regras transversais · [`AGENTE_ED_FLAGRANTE_V1.md`](AGENTE_ED_FLAGRANTE_V1.md) — **o esqueleto a copiar**
- [`AGENTE_ED_ORGANIC_WAVE_V4.md`](AGENTE_ED_ORGANIC_WAVE_V4.md) — motor mecânico · [`recursos/DOUTRINA-VEO-3.1.md`](recursos/DOUTRINA-VEO-3.1.md) — doutrina do modelo
- [`funil-organico/RUNBOOK-watch-videos.md`](funil-organico/RUNBOOK-watch-videos.md) — a etapa [2] em detalhe
- [`funil-organico/prop-metaforas.md`](funil-organico/prop-metaforas.md) — props, dimensão, recusa do gerador
- [`funil-organico/arsenal-linguagem-indireta.md`](funil-organico/arsenal-linguagem-indireta.md) — vocabulário · [`funil-organico/espinha-fixa.md`](funil-organico/espinha-fixa.md) — personas, CTA, gates
- [`funil-organico/licoes-producao-veo.md`](funil-organico/licoes-producao-veo.md) — o playbook das lições pagas em campo
