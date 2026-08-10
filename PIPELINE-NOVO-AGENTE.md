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
--- daqui pra baixo o agente vira FERRAMENTA (só quando maduro) ---
[9]  motor        → <agente>_lucas.py: pools + strings travadas + linter
[10] app          → <agente>_lucas_app.py: interface tkinter offline
[11] executável   → .exe entregue em C:\Users\edlut\Desktop\agentes_py\AGENTES-<FAMILIA>
```

⚠️ **As etapas 9-11 são opcionais e só entram depois do [8].** Portar um agente
que ainda está mudando de forma é congelar hipótese em código. O gatilho para
portar é: **as regras pararam de mudar e o que sobrou é repetição mecânica.**

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
| **TROCA** | Julie Evans, 7 reels + Sofia Maren | mediana **25,5K**, topo 29,7K — ⚠️ o mapa recomendou **não** criar o agente (2/4 no critério); o operador decidiu o contrário e a cena que ele acrescentou supriu a vítima que faltava |

---

## [2] LEITURA ÓTICA — ver, não resumir

Receita completa: [`funil-organico/RUNBOOK-watch-videos.md`](funil-organico/RUNBOOK-watch-videos.md).
Reels de Facebook são login-walled — o happy path 2b (captura pela aba logada
do Chrome) é a rota validada.

> ⭐ **Rota 2c — cookies + o MESMO proxy da sessão** (validada 2026-08-01, TROCA:
> 8 reels baixados em minutos). Quando o Ed roda a conta de garimpagem no
> **Dolphin Anty atrás de proxy**, ele pode passar o JSON de cookies e a linha do
> proxy; aí o `yt-dlp` baixa direto, sem o relay HTTP da 2b.
>
> ⚠️ **O detalhe que custou meia hora: cookie de Facebook é atado ao IP.** Com os
> cookies certos mas saindo por outro IP, o FB devolve uma página diferente e o
> yt-dlp morre com `Cannot parse data` — que *parece* extractor defasado e não é.
> **Os cookies e o `--proxy` andam juntos, sempre.** Sintomas e o que significam:
>
> | Sintoma | Causa real |
> |---|---|
> | `Cannot parse data` | cookies válidos, IP errado — falta o `--proxy` |
> | `407` no proxy | credencial errada. ⛔ Se veio de print, **peça em texto** — `l`/`I` e `O`/`0` são indistinguíveis, e chutar senha queima o proxy |
> | `502` no proxy, mas `200` no Facebook | proxy **IPv6-only**: o alvo de teste não tem AAAA. Testar contra o alvo real, não contra `ip-api.com` |
> | Whisper devolvendo `403` | WAF barrando o `User-Agent` do `urllib`. Subir pelo `curl` resolve |
>
> ⛔ O arquivo de cookies vive **no scratchpad da sessão** — nunca no repo, nunca
> em commit.

**A densidade de frame que funcionou:** `fps=2` nos **primeiros 4 segundos** e
`fps=1` no resto. O hook carrega o agente inteiro e é onde o olho precisa de
resolução temporal; no corpo, 1 fps basta. Nos 8 reels do TROCA isso deu 142
frames — 8 de hook e 8-26 de corpo por vídeo.

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

### ⚠️ O critério é um diagnóstico, não um veto — e o operador pode suprir

Validado no TROCA (2026-08-01). A leitura ótica dos 8 reels concluiu, com
argumento: **"não é ângulo novo o suficiente para agente próprio"** — marcava
**2 de 4** (tinha cena e evidência; não tinha **vítima** nem **arco**). O hook
inteiro já era nosso (M1 do SUBSTANCIA_ABSURDA) e o gesto já era do UNCAO.

O que aconteceu em seguida é o breadcrumb: **o Ed propôs uma cena que supriu
exatamente o elemento que faltava** — um corpo-prova masculino segurando o
próprio prop no colo, na cena 3, com a narradora apontando sem encostar. Isso é
a **vítima**, e com ela o arco fecha.

Três consequências para quem rodar o pipeline:

1. **Rodar o critério antes de construir, e dizer o número em voz alta.**
   "2 de 4, faltam vítima e arco" é acionável; "acho que é parecido com o
   SUBSTANCIA_ABSURDA" não é.
2. **Um veredito negativo é uma lista de compras.** Nomear o que falta permite
   ao operador decidir se quer supri-lo — e essa decisão é **alçada dele**,
   nunca do agente.
3. **Registrar a divergência dentro do arquivo do agente.** Quando o operador
   decide contra a recomendação, isso vai na seção 1 do `AGENTE_ED_*.md`, com
   data, para que ninguém "corrija" o agente depois lendo só o mapa visual.

⚠️ **E os achados que não viram agente não se perdem:** o mapa do TROCA
produziu 4 achados transversais (o prop que **não cresce** e converte, a troca
na mesma geometria, a bancada-recibo, a física do fluido). Cada um tem um
arquivo-dono — PRISMA, V5, `prop-metaforas` — e a tabela de destino fica escrita
no próprio mapa visual.

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
| `UN` | UNCAO | `NE` | NECROSE |
| `TR` | TROCA | `ES` | ESCANDALO |

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

## [9] [10] [11] O AGENTE VIRA FERRAMENTA — motor, app e `.exe`

Receita completa, com os gotchas do PyInstaller e o checklist de porte:
**[`funil-organico/RUNBOOK-app-offline.md`](funil-organico/RUNBOOK-app-offline.md)**.

O primeiro caso completo foi o **FLAGRANTE LUCAS** (2026-07-30): agente Markdown
-> `flagrante_lucas.py` -> `flagrante_lucas_app.py` -> `FLAGRANTE-LUCAS.exe` de
~10 MB rodando offline na área de trabalho.

**A regra de corte entre Markdown e código:**

> Vai para o código o que é **mecânico e verificável** — strings travadas,
> contagem de cota, teto de fala, token proibido, sorteio de eixo. Fica no
> Markdown o que é **julgamento** — o porquê da regra, a evidência que a gerou,
> o arco narrativo. **Código não substitui doutrina; impede que ela seja
> violada por descuido.**

Os três custos que justificaram a migração, todos medidos em produção:

| Custo | O caso real | O que o código resolveu |
|---|---|---|
| String travada corrompida | ao enxugar um prompt, reescrevi o D1 "com minhas palavras" e o render virou esqueleto 3D | as strings viraram **constantes** — não passam mais pela digitação |
| Auditoria por julgamento | contei a cota do órgão no olho e declarei 4/5 o que era 3/5 | **linter em regex** — conta, soma e varre token banido |
| Mode-collapse | eu e o modelo gravitando pro mesmo protótipo | **sorteio de eixos** com ledger anti-repetição |

⚠️ **Uma fonte de verdade.** O app **importa** o motor; o motor **cita** a
doutrina. Regra nova entra no `.md`, desce para o motor, e aparece no app e no
`.exe` sem tocar em interface. Duplicar string entre camadas é o mesmo erro que
a regra P9 já proíbe entre arquivos de doutrina.

### ⛔ ACEITE DO MOTOR É MEDIÇÃO, NUNCA RELATO (validado no TROCA, 2026-08-01)

O motor do TROCA foi entregue **com relatório dizendo "0 ERRO, comandos
passaram"** — e quebrava em **100% dos sorteios**. Quatro defeitos:

| Defeito | Sintoma |
|---|---|
| `%` com argumento faltando | `TypeError: not enough arguments for format string` |
| dois nomes indefinidos (`TR8_NUMERO`, `_bolso`) | `NameError` só na linha que executa |
| dois linters comparando com o **template cru** | 400 de 400 reprovados, com mensagem plausível |

**O checklist que fecha o portão** — nesta ordem, porque cada passo poupa o
seguinte:

1. **`python -m pyflakes <motor>.py`.** Acha **todos** os nomes indefinidos de
   uma vez. Caçar de rodada em rodada custa uma execução por bug — o `pyflakes`
   custa uma só. Ele também acusa `redefinition of unused`, que é o sinal de
   duas versões da mesma função no arquivo.
2. **400 sorteios pelas 5 páginas**, `sortear → montar → lint`, com o ledger em
   memória. **0 ERRO medido.** O `--n 2 --dry-run` de smoke test não serve: os
   defeitos deste motor só apareciam em parte dos sorteios.
3. **Entropia medida, não estimada** (ver a barra abaixo).
4. **⚠️ Quando o linter falha em 100%, a suspeita é do LINTER, não da cena.**
   Regra que reprova tudo nunca foi testada.

⛔ **Linter não compara com constante que tem slot.** `TR_X not in bloco` dá
100% de falso positivo quando `TR_X` chega formatada. Compara-se com o **miolo
invariante** — o trecho entre os `%s`, que sobrevive a qualquer preenchimento.

⛔ **A numeração de regra é a mesma nos dois lados, caractere por caractere.**
O motor do TROCA passou a citar `TR15`-`TR21` que **não existiam** na doutrina:
toda mensagem de erro mandava o operador ler a regra errada, e não havia como
auditar cobertura. Regra que o motor descobre ao virar código **volta para o
`.md`** — é lá que ela existe (P9). Conferência barata:
`for n in $(seq 1 N); do grep -c "TR$n\b" motor.py doutrina.md; done`.

**A barra de entropia** (medida nos SHORT em 2026-08-01, com 400 sorteios cada):

| O quê | Piso |
|---|---|
| opções por eixo visual | **≥ 9**, alvo 12-14 |
| concentração no item mais sorteado | **≤ ~17%** |
| `FUNDIDAS` (a copy fundida) | ≥ 13 |
| `CTAS` | ≥ 14 |
| `GATES` | ≥ 11, **no máximo 2 com `brother`**, maioria sem vocativo |
| erros de linter em 400 sorteios | **0** |

> Pool grande não basta: sem ledger anti-repetição o lote de 20 vídeos repete
> rosto e cenário mesmo com 14 opções por eixo.

---

## Conexões

- [`funil-organico/RUNBOOK-app-offline.md`](funil-organico/RUNBOOK-app-offline.md) — as etapas [9]-[11] em detalhe
- [`WORKFLOW.md`](WORKFLOW.md) — a operação inteira · [`CLAUDE.md`](CLAUDE.md) — regras invioláveis e alçada
- [`AGENTE_ED_PRISMA_V1.md`](AGENTE_ED_PRISMA_V1.md) — engine + regras transversais · [`AGENTE_ED_FLAGRANTE_V1.md`](AGENTE_ED_FLAGRANTE_V1.md) — **o esqueleto a copiar**
- [`AGENTE_ED_ORGANIC_WAVE_V4.md`](AGENTE_ED_ORGANIC_WAVE_V4.md) — motor mecânico · [`recursos/DOUTRINA-VEO-3.1.md`](recursos/DOUTRINA-VEO-3.1.md) — doutrina do modelo
- [`funil-organico/RUNBOOK-watch-videos.md`](funil-organico/RUNBOOK-watch-videos.md) — a etapa [2] em detalhe
- [`funil-organico/prop-metaforas.md`](funil-organico/prop-metaforas.md) — props, dimensão, recusa do gerador
- [`funil-organico/arsenal-linguagem-indireta.md`](funil-organico/arsenal-linguagem-indireta.md) — vocabulário · [`funil-organico/espinha-fixa.md`](funil-organico/espinha-fixa.md) — personas, CTA, gates
- [`funil-organico/licoes-producao-veo.md`](funil-organico/licoes-producao-veo.md) — o playbook das lições pagas em campo
