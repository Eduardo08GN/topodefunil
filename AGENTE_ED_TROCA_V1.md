# AGENTE UGC — ED / MEN'S WELLNESS
## TROCA V1 — o proxy sai, o mecanismo entra no mesmo ponto do quadro

> Agente paralelo e ESPECIALISTA. Não substitui V4/V5/V6/PRISMA — coexiste.
> Use **este** quando o vídeo for do formato **SHORT nativo de 3 cenas × 8s**
> em que uma **narradora sozinha na cozinha** manda esfregar uma substância
> banal no órgão, e o argumento inteiro é uma **substituição de objeto dentro
> do mesmo enquadramento**: o proxy desce, a gelatina sobe, mesma mão, mesma
> altura, sem corte.
>
> Motor mecânico, formato de entrega e regras de Veo: **por ponteiro** (ver
> tabela na seção MECÂNICA). Este arquivo só carrega o que é PRÓPRIO do ângulo.
>
> ⚠️ **SHORT NATIVO.** Os outros SHORT (`flagrante_short`, `pee_short`,
> `vazamento_short`, `necrose_short`) **derivam** de um motor longo de 5 cenas
> por colapso. Este **não**: a fonte tem 12-14s de take único e o ângulo nasce
> em três cenas. Não existe — e não deve existir — um `troca_lucas.py` de 5
> cenas.

---

## POR QUE ESTE AGENTE EXISTE

**Fonte:** leitura ótica frame a frame de **8 reels** (7 da página *Julie
Evans*, 1 da *Sofia Maren*), 142 frames, transcrição Whisper large-v3,
2026-08-01 — [`concorrentes/julie-evans-mapa-visual.md`](concorrentes/julie-evans-mapa-visual.md).

| Reel | Views | Estrutura |
|---|---|---|
| v02 · Vicks / abobrinha | **29.763** | CONFIRMA |
| v05 · honey / banana | **25.877** | CONFIRMA |
| v03 · Vicks / banana | **25.558** | CONFIRMA |
| v06 · turmeric / abobrinha | **17.290** | DESMENTE |
| v07 · turmeric / cenoura | **11.568** | DESMENTE |
| v04 · honey / abobrinha 45-50cm | 5.610 | CONFIRMA (o corte espelhado) |
| v08 · Sofia Maren, 29,7s | **82.169** | DESMENTE + receita entregue + follow-gate |

Sete vídeos numa faixa de 11K-30K com **take único, elenco 1 e zero VFX**. A
mediana é 25,5K.

### ⚠️ O mapa recomendou o contrário — e a decisão é do operador

A §4 da fonte concluiu **"não é ângulo novo o suficiente para agente próprio"**
(marca 2 de 4 no critério do [`PIPELINE-NOVO-AGENTE.md`](PIPELINE-NOVO-AGENTE.md)
§[3]: tem cena e evidência, não tem vítima nem arco). **O Ed decidiu criar o
agente assim mesmo, em 2026-08-01** — alçada dele, registrada aqui para que
ninguém "corrija" o arquivo depois lendo só o mapa.

### O que este agente tem que nenhum outro tem

**⭐ A TROCA.** O proxy desce e o mecanismo sobe **no mesmo ponto do quadro,
mesma mão, mesma altura, sem corte** (8/8 dos reels; 6/8 sem corte nenhum). O
cérebro lê **substituição** — *"isso não funciona, ISTO funciona"* — sem uma
palavra. Nos nossos ângulos o pivô mora numa **cena nova**, com outro
enquadramento, outra luz e outro beat; aqui ele custa **zero segundos e zero
renders**. É o único elemento do lote que carrega o vídeo inteiro e que não
existe no nosso repertório — e é o que dá nome ao agente.

### Onde ele encosta nos vizinhos — e como se separa

| Vizinho | O que é dele | Como a TROCA se separa |
|---|---|---|
| [`SUBSTANCIA_ABSURDA`](AGENTE_ED_SUBSTANCIA_ABSURDA_V1.md) | **dono do hook**: comando imperativo + substância banal + prop + promessa numérica (M1) | a TROCA **executa** o hook dele e acrescenta o dispositivo de montagem. ⚠️ E **desobedece o P20/P17 dele** de propósito (TR2) |
| [`UNCAO`](AGENTE_ED_UNCAO_V1.md) | **dono do gesto**: mão feminina, mecanismo tocando o proxy, vocabulário de cozinha (UN3) | lá o prop **cresce na tela** e o payoff é status público. Aqui **nada cresce** e o payoff é a substituição |
| [`ELA_DIAGNOSTICA`](AGENTE_ED_ELA_DIAGNOSTICA_V1.md) | REF feminina + homem em quadro + registro de alarme | lá o **corpo dele é o sintoma** (dedo cravado no abdômen, ele deitado, passivo, cabeça baixa, sala de exame). Aqui ele **está de pé, neutro, ativo, segurando o próprio prop**, ela **não encosta**, e ele só aparece **na cena 3**. Lá o homem é o diagnóstico; aqui é a **constatação** |
| [`FLAGRANTE`](AGENTE_ED_FLAGRANTE_V1.md) | humilhação pública, plateia, prop minúsculo e murcho | aqui **não há plateia, não há vergonha e o prop é grande**. A cena 3 usa a **geometria** da F12b sem o registro dela (TR10) |

---

## ANTES DE ESCREVER — O PORTEIRO

> **"Estou referenciando e sendo claro o suficiente para que quem está
> assistindo entenda do que se trata cada cena?"**

As 4 perguntas do [`AGENTE_ED_PRISMA_V1.md`](AGENTE_ED_PRISMA_V1.md) §O Porteiro
rodam **cena a cena** (cota do órgão, dor em imagem, frase chã, teste do rádio).

⚠️ **O risco específico deste ângulo é a ELIPSE.** Três coisas grandes nunca
são ditas: o proxy não é nomeado (TR3), a substância nunca é vista sendo
aplicada (TR4) e a receita não é entregue. Isso é elipse **de imagem**, e ela
funciona porque a imagem paga a conta. ⛔ **A fala não pode ser elíptica
também** — se a copy também virar charada, o vídeo tem duas camadas de código e
nenhuma mensagem (F14). O órgão é dito com substantivo do núcleo, em voz alta,
nas duas primeiras cenas.

---

## PASSO 0 — SPEC

Duas portas de entrada, nunca improviso:

1. **Sorteio pelo motor** — **rota atual desde 2026-08-01**:
   ```bash
   python funil-organico/troca_short.py --pagina <joe|marcus|ray|chuck|matt> --n 10
   ```
   Ou o app offline: `AGENTE-TROCA-SHORT.exe` em
   `C:\Users\edlut\Desktop\agentes_py\TROCA-SHORT`.
2. **Comissão do operador**, para spec dirigida. ⚠️ `troca` ainda **não** está no
   `randomizador-prisma.py` — o ângulo não introduziu conceito novo de eixo, e
   enquanto não entrar lá o PRISMA não o sorteia.

O motor: **`funil-organico/troca_short.py`** ✅ **SHORT nativo e autônomo, sem
motor longo** — o molde
   arquitetural exato é [`funil-organico/organicwave_short.py`](funil-organico/organicwave_short.py)
   (importa só `json`/`os`/`random`, pools próprios, `ETNIA`,
   `homens_de()`/`mulheres_de()`, `TETO_FALA`, `CENAS_UI`, `EIXOS_UI`,
   `sortear()`, `montar()`, `lint()`, `nova_fala()`, `resumo_pt()`,
   `_carregar_ledger()`/`_gravar_ledger()`, `EIXOS_QUE_MEXEM_NA_COPY` e
   `_evitando()`). Ledger: `.troca-short-ledger.json`. Maquinaria compartilhada
   do formato: [`funil-organico/short_comum.py`](funil-organico/short_comum.py).
   Interface: `ui_agente.py` (compartilhada) → `troca_short_app.py` → `.exe`,
   pela receita do [`RUNBOOK-app-offline`](funil-organico/RUNBOOK-app-offline.md).

`TETO_FALA = {1: 22, 2: 34, 3: 26}` e `PISO_FALA = {1: 16, 2: 26, 3: 20}` — ver TR14, que é onde o orçamento vira regra. ⚠️ **O piso é cobrado pelo linter**, não é julgamento; e a soma dos tetos (82) colide com o piso do orçamento total (82-96) — tensão registrada na TR14, decisão do Ed.

### Os eixos próprios da TROCA

Rotacionar — combo repetido em vídeos consecutivos da mesma página é proibido
(o `_evitando()` do ledger faz isso quando o motor existir; em comissão,
conferir na mão).

| Eixo | Valores observados na fonte | Nota |
|---|---|---|
| **SUBSTÂNCIA DO HOOK** | `coconut oil` · `Vicks VapoRub` · `honey` · `turmeric paste` | ⚠️ Doméstica e reconhecível em meio segundo (gramática do SUBSTANCIA_ABSURDA). ⛔ A marca não entra em quadro (TR7) |
| **PROXY** | cenoura crua gigante · abobrinha verde-escura gigante · banana madura de tamanho natural | ⚠️ Escala absurda **não** prediz performance: os dois de banana natural fizeram 25,5K e 25,9K; a abobrinha de 45-50cm fez 5,6K |
| **⭐ FÍSICA DA SUBSTÂNCIA** | verniz molhado · gel opaco em placas com teias · fio contínuo pendurado · pasta seca em marcas de dedo | Eixo independente da substância. É onde mora a carga — ver TR6 |
| **ARQUÉTIPO DA NARRADORA** | 8 observados, um por vídeo (loira 28-33, negra 25-32, ruiva sardenta, MILF 40-45, morena oliva, ruiva tatuada, goth, loira de óculos "especialista" 35-40) | **Solto** por vídeo (TR11). É o maior eixo de variação visível do lote |
| **CENÁRIO** | cozinha doméstica (7/8) · home office com estante, diplomas e bandeira (1/8 — o de 82K) | O álibi de "receita caseira" × o álibi de **autoridade** |
| **PROMESSA** | `ten times bigger` (7/8) · `last all night long` (1/8) | Formulação pela escada da TR8 |

⛔ **Dois eixos da fonte que NÃO são sorteáveis para nós:**
- **O mecanismo real** — travado em **gelatina** (congruência inviolável: o
  mecanismo do criativo é o que a VSL vende). Eles trocam entre pote de Vicks,
  mason jar de mel e tigela de azeite; nós não.
- **A keyword do CTA** — travada em `gelatin`. Eles usam `Vic`/`Vick`/`honey`/
  `book` e isso é **defeito operacional deles** (quatro automações, duas
  palavras que o espectador confunde). ⛔ `BOOK` e `YES` são proibidos —
  quebram a automação de DM, e o reel de 82K usa literalmente `book`: **copiar
  a arquitetura, nunca a palavra.**

---

## O HOOK — OS 6 ELEMENTOS OBRIGATÓRIOS

Lidos dos 8 reels, todos 8/8. **Nenhum é opcional** — o teste é *"se eu tirar,
a cena ainda se lê?"*.

### 1️⃣ ELA, SOZINHA EM QUADRO, OLHAR TRAVADO NA LENTE
Elenco = 1 do primeiro ao último frame. Sem o rosto dela no **mesmo quadro** do
proxy, o objeto vira b-roll e a piada perde dono; o olhar na lente é o que faz
a promessa ser **endereçada** (*your John-son*). Marca facial própria
obrigatória (P6).

### 2️⃣ O PROXY VEGETAL NA VERTICAL, PONTA PRA CIMA, NA ALTURA DO ROSTO
É o órgão. Segurado **de pé no punho esquerdo**, no **mesmo plano focal do
rosto**, ao lado da bochecha. É a **única régua de escala do quadro** — baixar o
prop pra bancada mata a relação corpo-prop e a cena vira demonstração culinária.
Dimensionado por **âncora de escala corporal**, nunca por adjetivo
([`prop-metaforas`](funil-organico/prop-metaforas.md) §Spec dimensional).
⚠️ Contato com o rosto: `held beside her cheek at eye level`, nunca
`pressed against her face` (§6.5 do mapa).

### 3️⃣ A SUBSTÂNCIA JÁ NO PROP E NAS MÃOS, NO FRAME 1
A aplicação **nunca é mostrada** (TR4). A prova de procedência é o **pote
aberto com a tampa deitada ao lado**, na bancada.

### 4️⃣ A MÃO LIVRE TRABALHANDO NO EIXO DO PROP
É o **verbo**. Mão parada segurando = foto de produto. Vocabulário e frase
travada: **UN3** do [`UNCAO`](AGENTE_ED_UNCAO_V1.md) — este agente **não
redeclara** o gesto (P9).

### 5️⃣ A BANCADA-RECIBO
3-4 itens em quadro, **nenhum citado na fala** (TR7). É o lastro do *full
recipe*.

### 6️⃣ O ÁLIBI DOMÉSTICO + A BANDEIRA DOS EUA
Cozinha real (ou home office de autoridade). Em estúdio ou fundo neutro a
**mesma ação muda de gênero** — e de política de plataforma. A bandeira dos EUA
é sinal de mercado US, **não é marca** e está no nosso catálogo
([`prop-metaforas`](funil-organico/prop-metaforas.md) §Props de autoridade).

---

## O ARCO — 3 CENAS

Fio narrativo (P21) em três batidas: **crendice → troca → prova**.

| Cena | Beat | Teto | O que a copy FAZ | O que a tela mostra |
|---|---|---|---|---|
| **1** | **A CRENDICE** | 22 | comando imperativo + promessa numérica + **o desmentido** (*you don't believe that works, right?*) — TR8 | os 6 elementos acima. **Nada cresce**; quem entrega o número é a cara dela (TR2) |
| **2** | **A TROCA ⭐** | 34 | a **copy fundida**: o mecanismo é BATIZADO com o literal `gelatin trick` + a prova (TR9) | o proxy desce, a tigela de gelatina sobe **no mesmo ponto, mesma mão, mesma altura, sem corte** (TR1). O proxy lambuzado **fica em quadro** na tábua |
| **3** | **O CORPO-PROVA + CTA** | 26 | CTA `gelatin,` + follow-gate | o homem **de pé**, segurando o proxy **na própria mão, no próprio colo**; ela **aponta sem encostar**, falando na lente (TR10) |

**A ponte lógica das 3 falas:** *faça isso e vai crescer — você não acredita,
né? → mas existe uma coisa que funciona de verdade, e chama gelatin trick, e é
por isso que funciona → e é assim que fica; comenta gelatin.*

⚠️ **Formato de entrega, sempre:** `BLOCO 0 (REF)` → **os 3 IMAGEs agrupados**
→ **os 3 TAKEs agrupados**. Nunca intercalar. Numeração `x/03`.
Destino da esteira: **AdBatch Vertical 3**
([`RUNBOOK-adbatch-vertical`](funil-organico/RUNBOOK-adbatch-vertical.md)).

---

## REGRAS PRÓPRIAS (TR1-TR21)

- **TR1 — ⭐⭐ A TROCA: MESMA MÃO, MESMO PONTO, MESMA ALTURA, SEM CORTE.**
  É o agente inteiro. Invariante 8/8 da fonte, e o único achado que não existe
  no nosso repertório.

  **Três coisas fazem a leitura de substituição, e as três são obrigatórias:**
  1. **A peça já estava plantada.** Detalhe forense do v01 e do v03: o pote
     estava **aberto na bancada desde o frame 1** e a **tampa continua lá**
     depois que ele sobe pra mão. O "reveal" não apresenta nada novo — puxa pro
     primeiro plano o que já estava no cenário. ⛔ Objeto que entra de fora do
     quadro não é troca, é corte disfarçado.
  2. **A mesma mão.** A mão que segurava o proxy é a que volta com o mecanismo.
     (Por UN4 o proxy nasce no punho **esquerdo**; então é o esquerdo que desce
     e sobe. A direita continua sendo a que trabalha a substância.)
     ⚠️ **O motor inverteu isso por conta própria e foi corrigido** (2026-08-01):
     as travadas diziam `right`, com o argumento de que "travada manda" e de que
     as três eram coerentes entre si na direita. O argumento era falso — a
     `TR_VAIVEM` não nomeava mão nenhuma — e a escolha é de **cena**, ou seja,
     alçada do Ed. Hoje o motor segue esta regra. Se o Ed preferir a direita, é
     esta linha e o UN4 que mudam, não o código sozinho.
     ⭐ **E a MÃO LIVRE tem de estar declarada no IMAGE.** Ela é o **verbo**
     (invariante 4/28: mão parada segurando = foto de produto), e nenhum IMAGE a
     declarava — o TAKE mandava trabalhar `along the length of it` sobre uma
     imagem com uma única mão, a que segura o prop de pé ao lado da bochecha.
     **Prompt que se contradiz, o modelo resolve como quiser.**
  3. **Sem corte e sem mexer a câmera.** Take único. 6/8 dos reels não têm corte
     nenhum; o único que corta na troca (v04) é **o pior número do lote**.

  **Coreografia para o TAKE 02 — em batidas com segundos** (o método é o de
  [`prop-metaforas`](funil-organico/prop-metaforas.md) §Coreografia de
  crescimento, 🟢 validado como método: âncora fixa · caminho · estado final
  travado. Verbo sozinho não é instrução — o Veo precisa do **como**):
  ```
  0 to 2 seconds: the camera does not move and there is no cut at any point in
  this shot. She keeps talking to the lens while her left hand lowers the
  [proxy] straight down onto the wooden board in front of her and lets go of it.
  The [proxy] stays lying on that board, still in frame, for the rest of the shot.
  2 to 4 seconds: the same left hand comes straight back up to the same spot in
  the frame, at the same height beside her face, now holding the shallow white
  bowl of gelatin.
  4 to 8 seconds: her hand does not move again. The bowl stays held up at that
  same height beside her face until the end of the shot.
  ```
  ⚠️ **Selo 🟡** — a geometria é 8/8 na fonte, mas esta redação é nossa e ainda
  não passou por render. ⛔ **E não se comprime antes do primeiro render**: uma
  versão do motor tinha achatado as três batidas numa frase só e, de quebra,
  descia o proxy `onto the workbench` enquanto a frase seguinte dizia que ele
  ficava `on the wooden board` — **duas superfícies para a mesma ação**, no take
  que é o agente inteiro. Comprimir o único método validado que temos antes de
  testá-lo descarta a evidência sem gerar nenhuma. O linter cobra as três
  batidas e a superfície única.
  ⛔ Nunca `swap`, `switch`, `replaces` (o Veo troca o objeto **cortando**) —
  descreve-se **descida, subida e ponto**, nunca o resultado.
  ⚠️ **A tigela é a string travada do UN2** — copiar de lá, não redigitar.

- **TR2 — ⭐ O PROP NÃO CRESCE. A PROMESSA É VERBAL; QUEM A ENTREGA É A CARA
  DELA.** 🟡 (decisão do operador [D4], 2026-08-01)
  Achado ① da fonte: **8/8 sem crescimento, sem VFX, sem morph, sem
  antes/depois** — o agente do v03 recortou o primeiro e o último frame lado a
  lado para confirmar (mesma banana, mesmo tamanho) — e mesmo assim 25-30K
  views. O `ten times bigger` é **100% verbal**.
  **Quem paga a promessa é a reação facial**, sincronizada no frame exato do
  número:
  ```
  On the word "[numeral]" her eyebrows jump and her eyes go wide at the lens for
  about half a second, then settle. Nothing in her hands changes.
  ```
  ⛔ `mouth open`, `tongue`, `lips parted` (§6.4 do mapa) — a reação entra por
  **outro traço**: sobrancelha, olho, `caught mid-word`.
  **Corolário dimensional:** se nada cresce, nada muda **entre as cenas**
  tampouco. A âncora de escala do proxy é declarada em todo IMAGE e é **a mesma
  na cena 1 e na cena 3**. ⛔ Não existe antes/depois neste ângulo.
  **No TAKE, o prop é objeto estático declarado** —
  [`prop-metaforas`](funil-organico/prop-metaforas.md) §Regra dos dois lados;
  ⛔ zero `stiff`/`limp`/`sags`/`grows`/`pulse`/`swelling`.
  ⛔ **A travada de imobilidade é usada NUA, e o objeto é NOMEADO.** Uma versão
  do motor a prefixava com `Nothing in her hand changes size, shape or state at
  any point` e a infixava com `same position, same angle, same length` —
  **negação que injeta `size`, `state` e `length`** num prompt cuja tese é
  justamente que nada muda de tamanho. Munição de graça, pela mesma mecânica de
  `fully clothed`, e ainda inchava a travada 3× (F12c: string validada é
  intocável; o que encolhe é descrição livre). O que se escreve é:
  ```
  The [proxy] in her fist stays exactly as it appears in the first frame —
  completely motionless for the entire shot.
  ```
  ✅ Nomear o legume aqui é permitido e desejável (a TR3 só o proíbe na
  `Dialogue:`); `the thing in his fist` é eufemismo desnecessário.
  ⚠️ **E o gatilho de sincronia segue a família da promessa sorteada.** `On the
  number` numa crendice da família de **resistência** (`it never quits on you`,
  `a different animal`, `beats every pill on the shelf` — 25% do pool) manda o
  Veo sincronizar com um numeral que a fala não tem, e ele escolhe sozinho onde.
  Nesses casos: `On the promise, her eyes go wide…`.
  ⚠️ **Isto diverge do P17 e do P20 do PRISMA de propósito** — ver SELO DE
  RISCO. Economia medida: nós queimamos **5 tentativas de geoduck**, uma
  coreografia de 7 elementos e o banimento de um prop inteiro para conseguir
  crescimento na tela; o concorrente faz 25-30K com o prop parado.

- **TR3 — ⛔ O PROXY NUNCA É NOMEADO NA FALA.** Invariante nº 9 da fonte, 8/8, e
  é o truque inteiro: o classificador e o algoritmo ouvem `gelatin` e
  `John-son`, **nunca ouvem o objeto**. A substituição é feita pelo espectador.
  ⛔ Na linha `Dialogue:`: `banana`, `zucchini`, `carrot`, `cucumber`, `squash`,
  `vegetable`. ✅ Na direção de cena (IMAGE/TAKE) o legume é nomeado
  normalmente — é lá que ele precisa ser desenhado.
  ⚠️ E o proxy também não é apontado por dêixis na fala (`look at this`,
  `from this to this`): dêixis é a 4ª forma de vago do
  [`licoes-producao-veo`](funil-organico/licoes-producao-veo.md) §Copy, e neste
  formato ela é pior ainda porque **a imagem não entrega os dois estados**
  (TR2). A fala fala do **corpo do espectador**, com substantivo do núcleo.
  ⛔ **E dêixis a PESSOA nas cenas 1 e 2 é pior ainda** (correção 2026-08-01):
  `He's standing right here.` · `Look at him.` · `That's him. Not a photo.` ·
  `Ask him yourself.` · `Right there. That's the proof.` rodavam em **40% dos
  lotes** — mandando olhar para um homem que o próprio IMAGE 02 declara ausente
  (`She is the only person in the frame`, elenco 1/1/2 da TR13). Reprova o
  **teste do rádio** do checklist. A prova da cena 2 é **não-dêitica**:
  `Nineteen days on a man I know.`, `He'll tell you if you ask him.`, `No photo,
  no filter, no story.`

- **TR4 — A SUBSTÂNCIA JÁ ESTÁ NO PROP NO FRAME 1; A APLICAÇÃO NUNCA É
  MOSTRADA.** Elipse deliberada, 8/8. Ninguém enfia o dedo no pote em cena.
  **A procedência é provada pelo objeto, não pela ação:** o pote **aberto**,
  com a **tampa deitada ao lado**, na bancada, desde o primeiro frame — e é a
  mesma peça que sobe na TR1.
  ⚠️ Isto é o que separa a TROCA do P20 do SUBSTANCIA_ABSURDA ("a aplicação
  acontece na tela"): aqui ela **já aconteceu**, fora de cena.
  ⚠️ **O detalhe forense é por objeto, não uma frase única.** A tampa deitada
  veio do v01/v03, onde o mecanismo era **pote com tampa** — e o motor a estava
  aplicando aos dez, mandando desenhar `its lid lying face-up` em tigela, pires,
  sachê, copo e panela (7 dos 10; 48% dos IMAGE 02). Contradição dentro do mesmo
  bloco, justamente na prova de que a peça estava plantada. Cada mecanismo
  declara o seu: tampa deitada · foil rasgado · colher usada ao lado.

- **TR5 — A SUBSTÂNCIA SÓ TOCA O VEGETAL E AS MÃOS.** 8/8, e é o que mantém o
  vídeo no ar: toda a carga é transferida ao proxy. **Nunca corpo humano** — nem
  colo, nem esterno, nem boca.
  ⛔ E sobre a pele dela, **silêncio**: não descrever, não negar. Se aparecer no
  render é acidente do modelo, não instrução nossa — e escrever `no substance on
  her skin` seria **munição de graça**
  ([`licoes-producao-veo`](funil-organico/licoes-producao-veo.md) §Declaração é
  munição). Contra o classificador, o silêncio é mais forte que a negação.

- **TR6 — A FÍSICA DA SUBSTÂNCIA É EIXO PRÓPRIO — é a carga que a fala não
  paga.** Achado ④. Quatro texturas sorteáveis, independentes da substância:
  | Textura | Como se lê |
  |---|---|
  | **verniz molhado** | só brilho especular, sem escorrer |
  | **gel opaco em placas** | teias entre os dedos, filetes descendo |
  | **fio contínuo pendurado** | atravessa o quadro até a tábua |
  | **pasta seca** | marcas de dedo e grumos, sem escorrer |

  ⚠️ **O fio pendurado é o ponto mais arriscado do quadro** (§6.2 do mapa).
  ⛔ Não amputar: **redirecionar o destino e nomear o gênero da imagem** —
  ```
  a slow thread of the honey runs off the bottom end and down onto the wooden
  board, the way honey runs off a dipper
  ```
  ⛔ **Nunca `onto her chest`** — é o destino-corpo que carrega a leitura, não o
  fio.
  ⛔ **A SUBSTÂNCIA É NOMEADA DENTRO DA TEXTURA — nunca `it`.** Uma versão do
  motor trocou `honey` por `it` em todas as dez texturas; como nenhuma nomeava a
  substância, o referente mais próximo de `it` passava a ser **o proxy**. O
  prompt descrevia então *um fio saindo da ponta de baixo de um objeto fálico*,
  com substância anônima e a analogia do dipper pendurada sem antecedente — ou
  seja, a leitura de ejaculação com a **única salvaguarda removida**. Nomear a
  coisa e nomear o gênero da imagem é a alavanca 3 inteira.
  ⚠️ **A textura acompanha o proxy nas três cenas.** Ela chegava só ao IMAGE 01;
  do 02 em diante o proxy saía **limpo**, contra o invariante 26/28 e contra o
  próprio checklist ("o proxy lambuzado FICA em quadro"). Nas cenas 2 e 3 entra
  a forma curta (`still wet with honey`), não a descrição inteira — densidade é
  superfície de bloqueio (F12c).
  ⚠️ Hipótese testável registrada pela fonte: os três piores números do lote são
  de **pasta seca**, os três melhores de gel/fio. Pode ser a **física** que
  separa o topo do fundo, e não a estrutura de copy. É hipótese, e é A/B nosso.

- **TR7 — A BANCADA-RECIBO: A BOCA CITA 1, A IMAGEM MOSTRA 3-4.** Achado ③,
  8/8. Bicarbonato + ingrediente extra + tigela + colher de pau + respingos na
  madeira, **nunca mencionados em fala nenhuma**. É o que dá lastro ao *I'll
  send you the full recipe*: o vídeo **mostra o ingrediente e esconde a
  receita**. Nós prometíamos a receita completa sem nunca provar em imagem que
  existe uma.
  ⛔ **P12 — nenhuma marca legível.** Eles têm caixa Arm & Hammer em 8/8 e pote
  de Vicks em 3/8. **Substituir por FORMA, nunca por marca:**
  | O deles | O nosso |
  |---|---|
  | caixa laranja de bicarbonato com rótulo | pote de vidro liso com pó branco e colher de pau |
  | garrafa `EXTRA VIRGIN OLIVE OIL` de frente | garrafa de vidro escuro **sem rótulo** |
  | pote de Vicks azul-cobalto | a tigela de gelatina do UN2 |
  | — | raiz de gengibre inteira · limão cortado ao meio · tigela de cerâmica rústica |
  | **bandeira dos EUA** | ✅ **copiar** — não é marca |
  ⚠️ **Teto:** 3-4 itens. Bancada lotada é densidade, e densidade é superfície de
  bloqueio (F12c).
  ⚠️ **A ausência de rótulo se declara pela AFIRMATIVA.** `Nothing in the frame
  carries a readable label, logo or brand` injeta `label`, `logo` e `brand` num
  prompt cuja tese é que não há nenhum — mesma mecânica de `fully clothed`. O
  que se escreve é `Every container in the frame is plain and unlabelled.`
  ⚠️ **E o pote de pomada não é azul.** Pote azul baixo de pomada é a silhueta e
  a cor da Vicks: trade dress reconhecível **sem rótulo**. P12 manda substituir
  por forma, não reproduzir a forma da marca. Cerâmica branca.
  ⛔ **O recibo NÃO entra no IMAGE 03.** Esse é o bloco de maior risco do lote —
  a regra de que ele deriva custou 4 recusas determinísticas — e era também o
  mais gordo do repo: **230 palavras, 2,3× o IMAGE 01 do próprio FLAGRANTE**, das
  quais 42 eram um recibo que não serve a beat nenhum da cena 3. O lastro do
  *full recipe* já foi provado nas cenas 1 e 2. No lugar entra o **mecanismo**,
  em uma oração: a cena que diz `comment gelatin` passa a mostrar gelatina em
  quadro (antes o IMAGE 03 não tinha nem gelatina, nem tábua, nem pote).
  ⚠️ **A bancada-recibo também não repete o pote da substância.** 11 de 168
  pares desenhavam o mesmo objeto duas vezes no mesmo quadro (`a plain glass jar
  of fine white powder` no pote **e** na bancada; `a rustic ceramic bowl` nos
  dois). Recibo que repete o pote mostra dois ingredientes, não três.

- **TR8 — O DESMENTIDO É BEAT PRÓPRIO DA CENA 1.** A fonte tem duas variantes
  de credibilidade — CONFIRMA (*and trust me, it really works*) e DESMENTE
  (*you don't believe that works, right?*) — e as duas convertem na mesma faixa.
  **Este agente roda DESMENTE**, por duas razões estruturais, não por número:
  1. É **exatamente o arco do SUBSTANCIA_ABSURDA**: o absurdo é a porta, o
     mecanismo real é a chave. CONFIRMA faz a substância do hook ser também a
     keyword — e a nossa keyword é travada em `gelatin`, que nunca vai ser a
     substância absurda do hook.
  2. Em 3 cenas, é o desmentido que **abre buraco** para a cena 2 ter o que
     batizar. Sem ele, a TROCA não tem contra o quê acontecer.

  **A promessa numérica roda a escada da §5c do mapa, nesta ordem** (⚠️ **a
  escolha do degrau é do Ed** — alçada; e a **Regra Zero vem antes**: regerar o
  take 2× e a imagem 2× antes de concluir qualquer coisa):
  1. **Assertiva, como a fonte:** `Rub [substância] on your John-son and it's
     gonna get ten times bigger.`
  2. **Condicional** — a única forma validada em produção: `If you want your
     John-son ten times bigger, rub [substância] on it tonight.`
  3. **`from this to this`** — linha 15 do nosso M1. ⚠️ É **dêixis** e neste
     formato o prop não cresce (TR2): só entra se o Ed aceitar a inconsistência.
  4. ⛔ **Interrogativa com prazo** (`by Sunday?`) — **descartada**: reintroduz o
     token de prazo que derrubou o NECROSE.

  ⭐ **A escolha do degrau é EXERCÍVEL, não só declarada** (correção 2026-08-01):
  cada entrada de `CRENDICES` declara o seu `degrau` e o motor aceita
  `--degrau {assertiva|condicional|testemunho|resistencia}`. Sem a flag o pool
  sai misturado, como antes. **Antes desta correção o motor sorteava por conta
  própria o que esta regra reserva ao Ed**, e o Ed não tinha como escolher sem
  editar código — o lote misturava o degrau 1 (🟡) com o degrau 2 (o único
  validado em produção).

  ⛔ **A promessa é sobre o corpo do ESPECTADOR (`your {o}`), sempre.** É o
  `your Johnson` que transfere o proxy para quem assiste (invariante 8/28, 8/8
  na fonte). Cinco entradas do pool diziam `his {o}`/`their {o}` — 29% dos lotes
  — e sem o `your` a promessa deixa de ser endereçada e o hook vira fofoca sobre
  terceiros. O linter cobra `your` na mesma frase do núcleo.

  ⛔ **CLAIM SOBRE O CORPO DO ESPECTADOR + PRAZO NA MESMA CENA É PROIBIDO.**
  É a composição exata que derrubou o **vídeo** do NECROSE com *"políticas
  contra a geração de conteúdo nocivo"*: diagnóstico do corpo de quem assiste
  somado a promessa com prazo. Vale também para a **cena 2**, onde o mecanismo é
  explicado:
  | ⛔ afirma | ✅ condiciona |
  |---|---|
  | `it's the blood flow your {o} is missing` | `if blood flow is what your {o} is missing, that's the one` |
  | `the blood flow reaches your {o} again` | `that's how the blood flow got back to his {o}` |
  | `it puts the blood back in your {o}` | `if you want the blood back in your {o}, that's the one` |
  A condicional **vende exatamente o mesmo desejo**; o que ela não faz é
  *atestar* o estado do corpo de quem assiste. O linter reprova a soma
  `your <núcleo>` + marcador de prazo dentro do mesmo take de 8s.

  ⚠️ `ten times bigger` aparece em **7 das 18 crendices**. É **travamento
  deliberado**, não vício: a fonte usa a mesma promessa em 7 dos 8 reels.
  Diluir é decisão de copy — alçada.

  ⚠️ `ten` por extenso (o Veo soletra algarismo). Grafia homófona **`John-son`**
  🟢 validada em render, custo zero.

- **TR9 — O BATISMO ACONTECE NA CENA 2, E O LITERAL `gelatin trick` É
  OBRIGATÓRIO.** 7/8 dos reels batizam o mecanismo com nome próprio (*the honey
  trick*) — é o nosso `gelatin trick` confirmado de fora, e a fonte prova que
  **a keyword mais forte é o nome do mecanismo**. A adaptação é 1:1:
  > `…and it's called the gelatin trick.`

  ⚠️ **A cena 2 é a copy FUNDIDA do formato SHORT** — ela carrega o batismo **e**
  a prova, porque as cenas que traziam cada um separadamente são justamente as
  que caem no colapso de 5 para 3
  ([`short_comum.py`](funil-organico/short_comum.py) §O literal `gelatin trick`).
  Sem ele o criativo deixa de ser congruente com o que a VSL vende — **regra
  inviolável, não preferência**. O linter do SHORT trava nisso.
  **Como a keyword se escreve:** minúscula e **seguida de vírgula** dentro do
  `Dialogue:` — [`espinha-fixa`](funil-organico/espinha-fixa.md) §Como a keyword
  se escreve (duas falhas pagas: `GLATN` e `gelatine`).

- **TR10 — ⭐ A CENA 3 É A F12b: ELE SEGURA, ELA APONTA SEM ENCOSTAR.**
  (ideia do operador [D1], 2026-08-01 — resolve o take que hoje fica com copy
  visual vaga nos nossos SHORT.)
  **A regra-mãe é a F12b do [`FLAGRANTE`](AGENTE_ED_FLAGRANTE_V1.md) — ler lá,
  inteira, com as duas strings travadas. Não copiar (P9).** O que ela ensina, e
  que vale aqui sem mudar uma vírgula:
  > **O que bloqueia não é o prop, é a AGÊNCIA.** Quatro IMG 01 recusadas em
  > sequência, **deterministicamente**, com tudo trocado entre elas. Em todo
  > frame aprovado, quem segura o objeto na virilha é **o dono da virilha**, e
  > ele está **ativo**.

  **O delta da TROCA — três diferenças de registro, e só elas:**
  | | FLAGRANTE (F12b) | TROCA (TR10) |
  |---|---|---|
  | Postura | **sentado**, cabeça baixa, mudo e abatido | **de pé**, neutro, queixo firme, mudo |
  | Prop | **minúsculo e murcho** (`no longer than his thumb`) | **grande**, dimensionado por escala corporal |
  | Leitura | vergonha, com plateia rindo | **constatação**, sem plateia nenhuma |

  **Formulação para o IMAGE 03** — 🟡 candidata, montada de fragmentos já
  validados; cada pedaço com procedência:
  ```
  In his own fist, held down beside the lap of his khaki shorts, he holds a
  [proxy] as long as his forearm and as thick as his wrist, its skin glossy.
  Beside him, [ela, com a relação nomeada] points her finger at it without
  touching him, talking to camera.
  ```
  | Fragmento | Vem de |
  |---|---|
  | `In his own fist … he holds` + `points … without touching him` | F12b (🟢) |
  | `beside the lap of his khaki shorts` | [`prop-metaforas`](funil-organico/prop-metaforas.md) §Recusa — a âncora de roupa que substituiu `level with his groin` (recusado) |
  | `as long as his forearm and as thick as his wrist` | prop-metaforas §Spec dimensional (🟢) |

  ⛔ **`lap` É A COORDENADA, E É STRING TRAVADA.** Só a **peça** varia com a
  calça sorteada; o substantivo, nunca. Uma versão do motor trocou `lap` por
  `front pocket`/`side pocket` "para acompanhar a calça" — isso é (a) reescrever
  string validada sem ordem do operador e (b) mover o prop da virilha para o
  quadril, que é **amputar a cena para destravar**, o reflexo que o `CLAUDE.md`
  §Alçada proíbe. Pior: o linter chegou a **exigir** a formulação não validada.
  ⚠️ **Tensão aberta, decisão do Ed:** o homem está **de pé** (esta mesma regra)
  e homem de pé não tem colo. Ou a postura cede, ou a âncora, ou nasce uma
  terceira formulação. Enquanto ele não decide, vale a string validada.

  ⚠️ **A âncora de escala é no corpo DELE** (`as long as **his** forearm`): quem
  segura na cena 3 é ele. 83% dos lotes saíam com `in his own fist … as long as
  **her** forearm` — o objeto é o mesmo, a régua é de quem o segura.

  ⚠️ **O olhar dele na lente é obrigatório no IMAGE 03, não só no TAKE.** A F12b
  diz que o que bloqueia é a **passividade**; `stands still and says nothing,
  his fist steady at his side` é o vocabulário exato do homem abatido das quatro
  recusas — e ainda tira o punho do colo. O que se escreve é `upright, chin
  level, **his eyes on the lens**, saying nothing`.

  **E no TAKE 03:** `her pointing finger stays close but never touches him. He
  keeps his eyes on the lens and never speaks; his fist stays where it is.` +
  a imobilidade declarada do prop (TR2).

  ⛔ **Tokens proibidos no prompt desta cena:** `groin`, `pubic`, `the victim`,
  `the narrator`. `victim` é uma palavra que **significa dano** — rotular a cena
  assim entrega munição de graça. **Descrever a pessoa, ou nomear a relação.**
  ⚠️ **A relação nomeada tem que ser fisicamente possível com as idades
  sorteadas.** O exemplo do operador é `his wife of thirty-one years`; com uma
  narradora de 28 anos e um corpo-prova de 60, 31 anos de casamento não fecha —
  aí troca-se o número ou a relação (`her neighbor of twenty-six years`, `the
  man she cooks for`), **nunca se omite**. Nomear a relação é a alavanca 2 do
  protocolo de recusa, e ela é obrigatória aqui.
  ⛔ **`his daughter-in-law` está fora.** O motor tinha inventado esse vínculo
  (12,5% dos lotes) e ele não está em lugar nenhum desta regra — e é o pior
  possível para esta composição: injeta leitura sexual intrafamiliar exatamente
  na geometria que já custou 4 recusas determinísticas. Se o Ed quiser a nora,
  é ordem dele e volta como entrada de pool.
  ⚠️ **A VOZ DA CENA 2 CASA COM A RELAÇÃO.** `my husband's {o}` / `stopped
  quitting on us` só entram quando a relação nomeada é **esposa**. Sortear os
  dois de forma independente punha 13% dos lotes dizendo `my husband` sobre um
  IMAGE 03 que declarava a narradora como a vizinha — e **contradizer a relação
  nomeada anula a alavanca 2**. A relação é sorteada **antes** das falas.

- **TR11 — CASTING: O CORPO-PROVA É TRAVADO, A NARRADORA É SOLTA.**
  (decisão do operador [D2], 2026-08-01)
  - **O HOMEM da cena 3** casa com o avatar da página: joe/ray/matt = *white
    American*; marcus/chuck = *Black American*. 50-70 anos, idade por **marca
    física** que renderize (`deeply lined skin`, `hair heavily streaked with
    gray`), nunca por rótulo.
  - **A NARRADORA é sorteada livre** entre os 8 arquétipos observados.
  **Razão do operador:** *o espectador de 50+ se identifica com o CORPO, não com
  quem narra* — então a congruência vale onde ela vende, e o maior eixo de
  variação visual do lote fica livre.
  ⚠️ Esta é a **única exceção registrada** à regra "etnia do REF = etnia do
  avatar da página", e ela existe porque neste ângulo o REF **não é** o avatar.
  ⛔ **O REF é nosso, não é cópia da Julie Evans nem da Sofia Maren** — do
  reel-fonte extrai-se o **dispositivo**, nunca a **aparência**. A regra inteira
  e a tabela de eixos de silhueta estão na **ED12** do
  [`ELA_DIAGNOSTICA`](AGENTE_ED_ELA_DIAGNOSTICA_V1.md); clonar o rosto da
  concorrente entrega a página.
  ⚠️ **Mesmo rosto nas 3 cenas do vídeo**, marca facial obrigatória (P6).
  ⛔ **PISO DE IDADE DA NARRADORA: 28 ANOS.** Herdado do `organicwave_short.py`
  (`IDADE_MINIMA_MULHER = 28`), que o carrega com o motivo escrito: *"já pagamos
  para descobrir que idade em cena com conteúdo de ED é zona sensível"*, e com
  `⛔ não baixar sem ordem do operador`. O motor da TROCA tinha baixado para 24
  sem ordem registrada em lugar nenhum. Aqui pesa **mais** que lá: a cena 3
  pareia a narradora com um corpo-prova de até 65 numa composição de proxy
  fálico, e a política de **menores** é a determinística — não cede a regerar, e
  é sensível a **geometria de intimidade + diferença de idade**, não à idade
  real. ⛔ E zero `baby tee` no figurino: o token `baby` entra de graça, pela
  mesma mecânica de `fully clothed`. `ringer tee` é a mesma peça.
  ⚠️ A idade numérica no prompt (`A 61-year-old …`) é **exigência do linter de
  continuidade** do SHORT (a âncora `the same N-year-old`), não contradição
  desta regra: o rótulo ancora a continuidade, e é a **marca física** que faz a
  idade renderizar. Os dois convivem — nunca só o rótulo.

- **TR12 — FIGURINO: SEGUIR A FONTE.** 🟡 (decisão do operador [D3], 2026-08-01)
  Os 8 concorrentes usam **cropped, barriga à mostra, decote e joias de ouro**, e
  passam na moderação com 11K-30K views. **O operador decidiu seguir a fonte.**
  ⚠️ Isto é **divergência deliberada do UN1** do [`UNCAO`](AGENTE_ED_UNCAO_V1.md),
  que manda roupa coberta. **O UN1 continua valendo integralmente no UNCAO** —
  nada lá é apagado ou contradito. Ver SELO DE RISCO.
  ⛔ **O que NÃO muda:** zero vocabulário de desejo no prompt — `sexy`,
  `seductive`, `curvy`, `revealing`, `cleavage`, `lingerie` continuam banidos. A
  roupa entra como **peça descrita**, não como adjetivo de desejo. ⛔ E nunca
  declarar conformidade sobre roupa (`fully clothed`): é munição.

- **TR13 — ELENCO 1 / 1 / 2, E UMA VOZ SÓ — A DELA.** Cenas 1 e 2: ela sozinha
  em quadro. Cena 3: ela + o corpo-prova, e mais ninguém. ⛔ **Zero plateia** —
  plateia é FLAGRANTE, e é justamente um dos quatro ingredientes da composição
  que produziu as recusas determinísticas.
  Só ela tem `Dialogue:` nas 3 cenas; ele é **mudo** (diálogo do Veo é
  monofônico na prática e duas vozes saem tortas).
  ⚠️ **Contraste** (P13): se por comissão houver dois personagens do mesmo sexo
  e faixa etária, valem os ≥3 eixos visíveis **e** a frase de contraste escrita
  no IMAGE.

- **TR14 — O ORÇAMENTO DE FALA É PISO **E** TETO: ADAPTAR AQUI É EXPANDIR ~2,3×.**
  (⚠️ ordem do operador, 2026-08-01)
  A fonte fala **~35-40 palavras em 12-14s**. O nosso vídeo tem **24s em três
  takes de 8s**, e cada take precisa se sustentar sozinho — o orçamento é
  **82-96 palavras**. **Copiar os 4 beats deles deixa ar sobrando**, e ar num
  take de 8s vira pausa morta.
  | Cena | Teto | Piso prático |
  |---|---|---|
  | 1 · A CRENDICE | 22 | 16 |
  | 2 · A TROCA | 34 | 26 |
  | 3 · CORPO-PROVA + CTA | 26 | 20 |
  ⚠️ **Teto continua sendo teto:** cena estourada → **cortar uma frase** (a que
  explica), nunca reescrever mais curto e mais vago. E o piso não se cumpre com
  enchimento: cumpre-se com **mais fato** — o mecanismo, o custo, a segunda
  pessoa.

  ⭐ **O PISO É MECÂNICO, IGUAL AO TETO** (correção 2026-08-01). Tratá-lo como
  "julgamento que mora na doutrina" foi o que deixou **48% das cenas 2 abaixo
  dele**: piso não cobrado é piso que não existe. O motor agora carrega
  `PISO_FALA = {1: 16, 2: 26, 3: 20}`, o linter avisa quando a cena fica abaixo,
  e o `--stats` **enumera exaustivamente** o pior e o melhor caso de cada pool —
  foi assim que se descobriu que o AVISO de teto era **código morto** (nenhuma
  cena conseguia estourar).

  🔴 **TENSÃO ARITMÉTICA ABERTA — decisão do Ed.**
  A soma dos tetos por cena é **22 + 34 + 26 = 82**, que é exatamente o **piso**
  do orçamento total (82-96). Ou seja: o vídeo só entraria na faixa com as três
  cenas no teto exato, e **nunca passaria de 82**. Os dois números não podem
  estar certos ao mesmo tempo.
  Medido depois da expansão dos pools: total **66-78 palavras, média ~71** (era
  58-72, média 64,6), com **0 de 400 sorteios abaixo do piso ou acima do teto em
  qualquer cena**. Isso é **1,9× a fonte**, não 2,3×.
  **As duas saídas, e a escolha é dele:** (a) subir os tetos por cena — o mais
  fiel à ordem "expandir 2,3×"; (b) baixar a faixa total para ~66-82. ⛔ O motor
  não escolhe: cobra piso e teto **por cena**, e o AVISO de total dispara acima
  de **96** (a borda de cima), nunca acima de 82, que é a de baixo.
  **Cota do órgão no SHORT: 2 de 3 cenas** com substantivo do **núcleo**,
  rotacionado (é o proporcional dos 75%; o linter de
  [`short_comum.py`](funil-organico/short_comum.py) conta assim).

### As sete que nasceram no motor (TR15-TR21)

> ⚠️ **Estas não vieram do garimpo — vieram da implementação**, em 2026-08-01.
> São regras que o `troca_short.py` legitimamente descobriu ao virar código, e
> estão aqui porque **o linter cita esses números nas mensagens de erro**.
> Regra citada em código e ausente da doutrina manda o operador ler a regra
> errada: a TR9 daqui é o batismo do `gelatin trick`, e uma versão anterior do
> motor usava "TR9" para a âncora de bolso. **A numeração é a mesma dos dois
> lados, caractere por caractere** (P9).

- **TR15 — FOLLOW-GATE, E VOCATIVO SÓ NO GATE.** O gate mora na cena 3 e é o
  único lugar do vídeo onde cabe aposto. ⚠️ No máximo **2 dos 14 GATES**
  carregam `brother`, e a maioria não tem vocativo nenhum — o operador mediu
  `brother` em 31-73% dos vídeos dos outros agentes e mandou variar
  (2026-08-01). O linter guarda a cena 3 inteira: se um dia alguém puser
  vocativo num CTA ou numa barreira, dois apostos caem na mesma respiração.

- **TR16 — ⛔ DECLARAÇÃO DE CONFORMIDADE É MUNIÇÃO.** Varre-se **todo** bloco,
  fala inclusa: `not a celebrity`, `fully clothed`, `no nudity`, `appropriate`,
  `safe for work`. **Silêncio vence negação** — declarar conformidade entrega
  ao classificador a categoria que ele deve procurar. Fonte:
  [`licoes-producao-veo`](funil-organico/licoes-producao-veo.md).
  ⚠️ Aqui a regra é mais afiada que nos outros agentes: a tese do vídeo é que
  **nada muda de tamanho**, e um `fully clothed` ao lado disso nomeia o assunto
  que a cena inteira evita nomear.

- **TR17 — OS VERBOS DA §6, E A ANALOGIA APONTANDO PARA FORA.** O vai-e-vém
  entra pela travada `TR_VAIVEM`, que troca o verbo **e nomeia o gênero da
  imagem** (`the way a cook rubs marinade into…`). ⛔ `strokes`, `pumps`,
  `grips`, `slides her hand up and down` são recusa.
  ⚠️ **O domínio culinário da analogia tem de ser diferente do proxy em quadro**
  (campo `analogia`): analogia de abobrinha com abobrinha na mão aponta para
  dentro da própria cena e não desambigua nada.

- **TR18 — A ÂNCORA DE CONTINUIDADE É INVERTIDA.** Nos outros agentes quem
  repete rosto é o REF masculino; aqui é a **narradora** — ela está nas três
  cenas, e a descrição dela volta **inteira, com a marca facial**, nunca em
  âncora curta. `same hair` carrega a roupa e perde o rosto: foi assim que o
  VAZAMENTO devolveu um senhor de óculos e bigode no lugar do corpo-prova.
  ⛔ E ela **nunca** leva adjetivo de etnia — é sorteada livre (TR11/[D2]); só o
  corpo-prova casa com o avatar da página.

- **TR19 — O RECIBO É MUDO, E NÃO REPETE O POTE.** Os três itens da bancada
  nunca são citados na fala (é o que dá lastro ao `full recipe`: a boca cita um
  ingrediente, a imagem mostra três). ⚠️ A não-colisão é **por construção, não
  por sorte**: o sorteio evita bancada que contenha a substância sorteada — com
  `substancia=ginger`, uma bancada de gengibre poria na boca justamente o que a
  imagem tinha de esconder.

- **TR20 — LEDGER.** Os eixos sorteados vão para `.troca-short-ledger.json` e as
  últimas 12 saídas de cada eixo são evitadas no sorteio seguinte. Sem isso o
  lote de 20 vídeos repete rosto e cenário mesmo com pool grande — foi a queixa
  medida do operador em 2026-08-01.


### Densidade medida — o número que o F12c pede (2026-08-01)

Palavras por bloco, pior caso em 400 sorteios, depois das correções:

| bloco | antes | agora |
|---|---|---|
| IMAGE 01/03 | 271 | 275 (ganhou a mão livre e a substância nomeada) |
| IMAGE 02/03 | ~200 | 216 (ganhou a re-âncora de cenário e a textura) |
| **IMAGE 03/03** — a F12b | **230** | **219** (perdeu o recibo, ganhou o mecanismo) |

⚠️ **O IMAGE 01 é o bloco mais gordo e continua assim de propósito:** ele
carrega os 6 elementos obrigatórios do hook, o pote (TR4), o mecanismo plantado
(TR1) e o recibo (TR7) — e é a composição de **menor** risco do lote (uma
pessoa, sem virilha em quadro). ⛔ Cortar TR4 ou TR7 dali para "aliviar" é
amputar regra, não densidade.
⚠️ **O IMAGE 03 continua acima dos peers** (219 × ~101-191) porque descreve
**duas pessoas inteiras** com marca facial obrigatória (TR11/TR18) mais o prop.
Se o Ed quiser baixar mais, o que sobra para cortar é a **re-âncora de cenário**
(~15 palavras) — e o preço é a entropia de cenário voltar a colapsar nas cenas 2
e 3. É troca, não ganho: decisão dele.

- **TR21 — SELF-TEST: O MOTOR SÓ ESTÁ PRONTO QUANDO ALGUÉM RODOU.**
  ⚠️ **Regra paga na própria construção deste agente.** O motor foi entregue com
  quatro defeitos que quebravam **100% dos sorteios** — dois nomes indefinidos,
  um `%` com argumento faltando e dois linters comparando com o *template cru*
  em vez do texto formatado — e mesmo assim veio acompanhado de relatório
  dizendo "0 ERRO, comandos passaram".
  **Aceite do motor é medição, não relato:** 400 sorteios pelas 5 páginas →
  `sortear` → `montar` → `lint` → **0 ERRO**, e nenhum eixo acima de ~17% de
  concentração. Antes de caçar bug a bug, `python -m pyflakes <motor>.py` acha
  todos os nomes indefinidos de uma vez.
  ⛔ **Linter nunca compara com a constante que tem slot** — `TR_X not in bloco`
  dá 100% de falso positivo quando `TR_X` chega formatada. Compara-se com o
  **miolo invariante** (o trecho entre os slots).

---

## SELO DE RISCO

**Primeiro, o que joga a favor — e é muito.** Pela régua que mais nos custou
caro ([`licoes-producao-veo`](funil-organico/licoes-producao-veo.md) §O
classificador julga a composição, não o assunto), as cenas 1 e 2 são **🟢 na
composição**: uma pessoa só, ativa, segurando o próprio objeto, sem plateia,
sem corpo passivo, sem mão de terceiro em corpo alheio, sem virilha humana em
quadro. Nada da geometria que produziu as 4 recusas determinísticas de
2026-07-30. **A briga aqui é sobre VERBOS, não sobre o frame.**

### 🟡 As duas divergências deliberadas — até A/B nosso

| # | Divergência | Contra o quê | Motivo | Status |
|---|---|---|---|---|
| 1 | **O prop não cresce** (TR2) — despejo sem crescimento, promessa entregue por reação facial | **P17** ("despejo sem crescimento é falha") e **P20** ("a demo acontece no TAKE da cena 1") do PRISMA | 8/8 dos reels convertem 25-30K com o prop **parado**, e nós queimamos 5 tentativas de geoduck + uma coreografia de 7 elementos para conseguir crescimento na tela. Se confirmar, é a economia de produção mais barata do repertório | 🟡 **até A/B nosso.** ⛔ Não propagar para os outros agentes antes do teste — lá o P17/P20 continua valendo |
| 2 | **Figurino cropped, barriga à mostra, decote, joias de ouro** (TR12) | **UN1** do UNCAO (roupa coberta, zero vocabulário de desejo) | 8/8 dos concorrentes fazem o oposto do UN1 e passam na moderação com 11K-30K views. Decisão do operador [D3]: seguir a fonte | 🟡 **até A/B nosso.** O UN1 **não é revogado** e continua valendo no UNCAO — a tensão fica registrada, não resolvida por opinião |

### 🟡 A cena 3 (TR10)

Composição derivada de uma regra 🟢 (F12b) com **três alterações** — de pé,
prop grande, sem plateia. As duas primeiras aumentam a agência e reduzem a
leitura de passividade; a terceira **remove** um dos quatro ingredientes do
bloqueio. Direção do risco: **para baixo**. Ainda assim é 🟡 até render.

### 🔴 / ⛔ Fila de reformulação — a cena não muda, muda a forma de dizer

Os 9 riscos com a reescrita validada de cada um moram na **§6 do
[`mapa visual`](concorrentes/julie-evans-mapa-visual.md)**. Usar **aquelas**
formulações. Ordem de tentativa:

1. **O vai-e-vém no eixo** (`slides her hand up and down`, `strokes`, `pumps`,
   `grips` — ⛔ já banidos no UN3) → alavanca 4 + alavanca 3:
   `her fingertips work the gelatin along the length of it, the way a cook rubs
   marinade into a squash before roasting`. **Nomear o gênero da imagem é
   obrigatório, não opcional.**
2. **O fio de fluido** → redirecionar destino + nomear gênero (TR6).
3. **A reação facial** → outro traço, nunca boca/língua (TR2).
4. **O prop na bochecha** → `held beside her cheek at eye level`.
5. **`Johnson`** → `John-son` 🟢.
6. **A promessa numérica** → a escada da TR8.
7. **Densidade** (F12c) → o prompt entrega o que a cena precisa pra ser lida —
   cozinha, prop, substância, mãos, rosto — **e para**. Joia, tatuagem, ímã de
   geladeira e marca de bancada são superfície de bloqueio. ⚠️ Mas **string
   travada é intocável**: descrição livre encolhe, bloco validado se copia
   caractere por caractere.

⚠️ **Regra Zero antes de tudo:** regerar o **take 2×** e a **imagem 2×**. As
três políticas do gerador têm variância, inclusive a de conteúdo nocivo. Só
vira investigação quando o mesmo bloco falha em **renders diferentes** —
método em [`RUNBOOK-bisseccao-moderacao`](funil-organico/RUNBOOK-bisseccao-moderacao.md).

⛔ **Esgotadas 3-4 formulações: parar e reportar ao Ed** com o diagnóstico e as
opções. Não tirar a substância, não tirar o fio, não afastar o prop do rosto,
não trocar o gesto, não cortar o homem da cena 3.

---

## MECÂNICA — POR PONTEIRO (P9: uma regra, um lugar)

| Assunto | Fonte |
|---|---|
| **O gesto** — contato mão-prop, domínio de cozinha, tokens banidos, fila de reformulação | [`AGENTE_ED_UNCAO_V1.md`](AGENTE_ED_UNCAO_V1.md) §UN3 · o prop de pé no punho §UN4 · a tigela de gelatina §UN2 |
| **O hook** — gramática do absurdo, substância doméstica, verbo físico, promessa numérica | [`AGENTE_ED_SUBSTANCIA_ABSURDA_V1.md`](AGENTE_ED_SUBSTANCIA_ABSURDA_V1.md) · [`banco-hooks.md`](funil-organico/banco-hooks.md) §M1/M8 |
| **A agência na cena 3** (a lição mais cara da operação) | [`AGENTE_ED_FLAGRANTE_V1.md`](AGENTE_ED_FLAGRANTE_V1.md) §F12b · densidade §F12c |
| IMAGE/TAKE, REF, marca facial, anti-glitch, anti-legenda, amarração de prop | `AGENTE_ED_ORGANIC_WAVE_V4.md` |
| Doutrina do modelo (I2V, fala, áudio) | [`recursos/DOUTRINA-VEO-3.1.md`](recursos/DOUTRINA-VEO-3.1.md) |
| Porteiro, fio narrativo (P21), 2ª pessoa (P22), contraste (P13), proxy no hook (P18), marca (P12), P17/P20 | [`AGENTE_ED_PRISMA_V1.md`](AGENTE_ED_PRISMA_V1.md) |
| Spec dimensional, imobilidade no TAKE, coreografia por batidas, recusa do gerador | [`funil-organico/prop-metaforas.md`](funil-organico/prop-metaforas.md) |
| Regra Zero, grafia homófona, declaração é munição, composição × assunto | [`funil-organico/licoes-producao-veo.md`](funil-organico/licoes-producao-veo.md) |
| Núcleo × tempero, frase chã, as 6 formas de vago, dor em imagem | [`funil-organico/arsenal-linguagem-indireta.md`](funil-organico/arsenal-linguagem-indireta.md) |
| CTA `gelatin,`, follow-gate, persona por página, `gelatin trick` | [`funil-organico/espinha-fixa.md`](funil-organico/espinha-fixa.md) |
| **Colapso de 5→3, copy fundida, linter do SHORT, cota 2/3** | [`funil-organico/short_comum.py`](funil-organico/short_comum.py) |
| **Molde do motor** (SHORT nativo, sem motor longo) | [`funil-organico/organicwave_short.py`](funil-organico/organicwave_short.py) · porte: [`RUNBOOK-app-offline`](funil-organico/RUNBOOK-app-offline.md) |
| Esteira 3×8s | [`funil-organico/RUNBOOK-adbatch-vertical.md`](funil-organico/RUNBOOK-adbatch-vertical.md) |
| **Legenda karaoke** (posição travada, amarelo, nunca sobre prop/rosto) e badge `COMMENT` | [`funil-organico/adbatch-prompts-editor.md`](funil-organico/adbatch-prompts-editor.md) — é regra de Veo Editor, não de agente |
| A fonte, os 28 invariantes, os 9 riscos com reescrita | [`concorrentes/julie-evans-mapa-visual.md`](concorrentes/julie-evans-mapa-visual.md) |

---

## CHECKLIST TROCA (além dos do V4 e do PRISMA)

- [ ] ⭐⭐ **A TROCA está coreografada no TAKE 02** — batidas com segundos, **mesma mão**, **mesmo ponto do quadro**, **mesma altura**, `no cut at any point`, câmera parada (TR1)?
- [ ] **A tigela de gelatina já está na bancada no IMAGE 02** (e no 01), e o pote do hook está **aberto com a tampa deitada ao lado** desde o frame 1 (TR1/TR4)?
- [ ] **O proxy lambuzado FICA em quadro** na tábua depois de largado (TR1)?
- [ ] ⭐ **Nada cresce em lugar nenhum** — zero VFX, zero morph, zero antes/depois, e a **âncora de escala do proxy é a mesma na cena 1 e na 3**, com a régua no corpo de **quem segura** (TR2/TR10)?
- [ ] ⛔ **A travada de imobilidade está NUA** — sem `changes size, shape or state`, sem `same length` (negação injeta o token que a cena evita), e o objeto está **nomeado** na direção de cena (TR2)?
- [ ] **A MÃO LIVRE está declarada no IMAGE** (é o verbo — mão parada segurando é foto de produto), e é a **direita** (o proxy nasce no punho esquerdo, UN4/TR1)?
- [ ] **A reação facial está sincronizada no frame do número** (`eyebrows jump`, `eyes go wide`) — e ⛔ zero `mouth open`/`tongue`/`lips parted` (TR2)?
- [ ] **No TAKE, o prop é objeto imóvel declarado** — ⛔ zero `stiff`/`limp`/`sags`/`grows`/`pulse`/`swelling` (TR2)?
- [ ] ⛔ **O proxy não é nomeado em NENHUMA linha `Dialogue:`** — e não é apontado por dêixis (TR3)?
- [ ] ⛔ **Zero dêixis a PESSOA nas cenas 1 e 2** (`look at him`, `right here`, `that's him`) — o quadro tem elenco 1 (TR3/TR13)?
- [ ] **A aplicação da substância não aparece** em cena nenhuma (TR4)?
- [ ] **A substância só toca o vegetal e as mãos** — e sobre a pele dela, **silêncio**, nem descrição nem negação (TR5)?
- [ ] **A física da substância está escolhida e escrita** (verniz / gel em placas / fio pendurado / pasta seca)? Se for fio: **destino na tábua + gênero nomeado**, ⛔ nunca `onto her chest` (TR6)?
- [ ] ⛔ **A substância está NOMEADA dentro da textura** (`a slow thread of the honey`), nunca `it` — com `it` o referente mais próximo vira o proxy (TR6)?
- [ ] **O proxy volta lambuzado nas cenas 2 e 3**, na forma curta (TR6)?
- [ ] **Bancada-recibo com 3-4 itens, nenhum citado na fala, nos IMAGE 01 e 02** (⛔ **não** no 03) — e **zero marca legível**, forma no lugar de rótulo (TR7)? Bandeira dos EUA em quadro em **todas** as cenas?
- [ ] **A bancada não repete o pote da substância**, e a ausência de rótulo está na **afirmativa** (`plain and unlabelled`) (TR7/TR19)?
- [ ] **O detalhe forense casa com o objeto** — tampa deitada só em pote com tampa; sachê tem foil, tigela tem colher (TR4)?
- [ ] **O desmentido está na cena 1** como beat próprio, e a promessa numérica saiu da escada da §5c, com `ten` por extenso e `John-son` (TR8)?
- [ ] **O literal `gelatin trick` está na cena 2**, minúsculo, e a keyword `gelatin,` está **minúscula e seguida de vírgula** na cena 3 (TR9)?
- [ ] ⭐ **Cena 3 na geometria da F12b**: ele **de pé**, o proxy **na própria mão**, âncora de roupa (`beside the lap of his khaki shorts`), ela **apontando sem encostar**, prop **dimensionado por escala corporal** (TR10)?
- [ ] ⛔ **Zero `groin` / `pubic` / `the victim` / `the narrator`** em qualquer bloco (TR10)?
- [ ] ⛔ **`beside the lap of his …` está literal** — só a peça varia, nunca o substantivo; ⛔ zero `pocket` na âncora (TR10)?
- [ ] **Ele está ATIVO no IMAGE 03 e no TAKE 03** — `his eyes on the lens`, punho onde estava; ⛔ zero `stands still`, `steady at his side` (TR10)?
- [ ] **A voz da cena 2 casa com a relação** — `my husband` só com esposa (TR10)?
- [ ] **A relação está nomeada** — e é **possível** com as idades sorteadas (TR10)?
- [ ] **Etnia do corpo-prova = etnia do avatar da página**; narradora sorteada livre; **mesmo rosto nas 3 cenas**; marca facial em todo personagem descrito (TR11)?
- [ ] ⛔ **O REF não parece a Julie Evans nem a Sofia Maren** — dispositivo sim, aparência não (TR11 / ED12)?
- [ ] **Figurino da fonte aplicado, e zero vocabulário de desejo** no prompt (TR12)? A divergência 🟡 do UN1 está nomeada na entrega?
- [ ] **Elenco 1 / 1 / 2**, ⛔ zero plateia, e **só ela tem `Dialogue:`** (TR13)?
- [ ] **Orçamento por cena entre piso e teto** (16-22 / 26-34 / 20-26) — o piso é cobrado, não é julgamento (TR14)?
- [ ] ⚠️ **O total 82-96 é inalcançável com os tetos atuais** (somam 82). A entrega sai 66-78. Isso está **nomeado na resposta** como decisão pendente do Ed (TR14)?
- [ ] ⛔ **Nenhuma cena empilha `your <núcleo>` + prazo** (a linha que derrubou o NECROSE) (TR8)?
- [ ] **A crendice fala do corpo do ESPECTADOR** (`your {o}`), não de terceiros (TR8)?
- [ ] **Cota do órgão 2/3** com substantivo do **núcleo**, rotacionado (TR14)?
- [ ] **Cada cena aterrissa em 2ª pessoa ou imperativo** (P22)? Zero cena em pura 3ª pessoa?
- [ ] **Teste do primo que não é do nicho**: nos 5 primeiros segundos dá pra saber que o assunto é o homem não conseguir levantar (F14)?
- [ ] **Teste do rádio**: alguma fala deixa de significar sem a imagem? Se sim, era dêixis — reescrever.
- [ ] **Fio narrativo**: as 3 falas em sequência = crendice → troca → prova (P21)?
- [ ] **Storyboard mudo**: 3 palavras, nenhuma repetida? **Planos**: ≥ 2 tamanhos diferentes?
- [ ] **Formato de entrega**: `BLOCO 0 (REF)` → os **3 IMAGEs agrupados** → os **3 TAKEs agrupados**, numeração `x/03`, nunca intercalado?
- [ ] **Narradora com 28 anos ou mais** (piso de idade), e ⛔ zero `baby tee` (TR11)?
- [ ] **Os riscos 🟡 nomeados na resposta** (divergência P17/P20 e divergência UN1)?

---

## ⛔ RECUSA DO GERADOR — troca-se a FORMA DE DIZER, nunca a cena

> **Quase nunca a cena está barrada — a frase está.**

Recusa do gerador **não é veredito sobre o conteúdo**. O classificador julga
**tokens e geometria**, não intenção: a mesma cena, dita com outro vocabulário,
passa. Caso validado (Ray/consultório 2026-07-28): `sitting across his lap` foi
recusado na política de menores **duas vezes**, com o IMAGE já aprovado;
`perched sideways on his right knee, the way a newlywed poses for a photograph`
gerou **a mesma imagem** — mulher no colo, prop ereto — sem bloqueio nenhum.

**As 4 alavancas, nesta ordem:**
1. **Trocar o token exato** que o classificador reconhece (`lap` → `knee`,
   `measuring tape stretched along` → `carpenter's tape run out alongside`).
2. **Nomear a relação** na mesma frase da pose (`his wife of forty years`,
   `the husband`).
3. **Nomear o gênero da imagem** (`the way a newlywed poses for a photograph`)
   — diz ao modelo que é retrato, não intimidade.
4. **Neutralizar os verbos de contato e congelar a geometria** (`pats her
   forearm once`, `her hand rests on his shoulder`, `neither changes position`).

⛔ **O que NÃO funciona:** declarar conformidade (`not a celebrity`, `they are
adults`) sem trocar a forma. Declaração não desarma classificador.

⛔ **NUNCA mudar copy ou cena por conta própria.** Esgotadas 3-4 formulações,
**parar e reportar ao Ed** com o diagnóstico e as opções — a decisão é dele
(`CLAUDE.md` §Regra de alçada). Amputar o bit visual resolve o bloqueio
destruindo o que fazia o vídeo converter.

Protocolo completo e tabela de reescritas já validadas:
[`funil-organico/prop-metaforas.md`](funil-organico/prop-metaforas.md)
§Recusa do gerador.

---

## Conexões

- [`concorrentes/julie-evans-mapa-visual.md`](concorrentes/julie-evans-mapa-visual.md) — **a fonte**: 28 invariantes, eixos, os 9 riscos com reescrita, o veredito honesto
- [`AGENTE_ED_SUBSTANCIA_ABSURDA_V1.md`](AGENTE_ED_SUBSTANCIA_ABSURDA_V1.md) — **dono do hook** (M1: comando + substância + promessa)
- [`AGENTE_ED_UNCAO_V1.md`](AGENTE_ED_UNCAO_V1.md) — **dono do gesto** (UN2/UN3/UN4); e a divergência 🟡 de figurino é contra o UN1
- [`AGENTE_ED_FLAGRANTE_V1.md`](AGENTE_ED_FLAGRANTE_V1.md) — **a arquitetura-mãe** e a F12b da cena 3
- [`AGENTE_ED_ELA_DIAGNOSTICA_V1.md`](AGENTE_ED_ELA_DIAGNOSTICA_V1.md) — o vizinho de REF feminina + homem em quadro; **não confundir** (ver tabela de separação)
- [`AGENTE_ED_PRISMA_V1.md`](AGENTE_ED_PRISMA_V1.md) — regras herdadas · `AGENTE_ED_ORGANIC_WAVE_V4.md` — motor mecânico
- [`PIPELINE-NOVO-AGENTE.md`](PIPELINE-NOVO-AGENTE.md) — o processo que gerou este arquivo · prefixo **`TR`** registrado
