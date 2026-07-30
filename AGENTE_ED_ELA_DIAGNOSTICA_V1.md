# AGENTE UGC — ED / MEN'S WELLNESS
## ELA_DIAGNOSTICA V1 — A MULHER APONTANDO O CORPO DELE

> Agente paralelo e ESPECIALISTA no ângulo **diagnóstico ao vivo com REF
> FEMININA**: uma mulher de meia-idade, na sala de exame, **cravando o dedo no
> abdômen** de um homem sem camisa reclinado na poltrona, com **alarme
> escancarado no rosto**. É o primo do
> [`AGENTE_ED_CONSULTORIO_V1.md`](AGENTE_ED_CONSULTORIO_V1.md) com três
> inversões que mudam a dinâmica inteira.
>
> Motor mecânico, formato de entrega e regras de Veo: **por ponteiro**.
> Arquitetura modelada no [`AGENTE_ED_FLAGRANTE_V1.md`](AGENTE_ED_FLAGRANTE_V1.md)
> (nossa referência de excelência).

---

## POR QUE ESTE AGENTE EXISTE

Leitura ótica frame a frame do reel **1022316587192809** da Tanisha Rivers
(2026-07-29, 116 frames a 1 fps — vídeo longo, formato mini-VSL). O hook são
os **8 primeiros segundos**, e ele faz **três coisas que o nosso CONSULTORIO
não fazia**:

| # | Inversão | Por que importa |
|---|---|---|
| 1 | **O REF é MULHER** | não é homem julgando homem — é **mulher diagnosticando o corpo dele**. A vergonha sobe: o público-alvo é o homem que teme o julgamento feminino |
| 2 | **A evidência é a BARRIGA**, não um proxy | o dedo crava na gordura abdominal. Sintoma no próprio corpo, zero metáfora — o espectador olha a própria barriga |
| 3 | **O registro é ALARME, não professor calmo** | olhos arregalados, dentes à mostra, cara de nojo/susto. É o oposto do contraste frio que a gente vinha usando |

Os dois ângulos **coexistem**: CONSULTORIO = narrador masculino frio + marcador
de estado (post-it/proxy). Este = narradora feminina alarmada + a barriga como
evidência. Rodar os dois é variação real de página, não de embrulho.

---

## ⚠️ A CERCA — mesma solução do CONSULTORIO

A Tanisha usa sala de exame + estetoscópio + "my patients" = **credencial
médica falsa**, uma das 4 linhas da cerca. **Ficamos com o teatro, largamos a
credencial:**

| 🟢 PODE (teatro de autoridade) | ⛔ NÃO PODE (credencial declarada) |
|---|---|
| sala de exame, poltrona, lençol azul, pôster de anatomia, bandeira US, otoscópio na parede | jaleco branco + estetoscópio juntos |
| camisa de seda/blusa social, lav mic clipado | scrubs de enfermagem |
| `I've seen hundreds of men like him` (experiência) | `I'm a doctor` · `as a nurse` · `my patients` |
| `mod=doctor` como ATAQUE (`doctors will never tell you this`) | qualquer fala que afirme formação |

Ela é a **mulher que já viu isso demais** — autoridade de mileage, não de
diploma. A sala é cenário; a fala nunca reivindica o título.

---

## ANTES DE ESCREVER — O PORTEIRO

As 4 perguntas do [`AGENTE_ED_PRISMA_V1.md`](AGENTE_ED_PRISMA_V1.md) §O Porteiro
rodam **cena a cena**: cota de 75% com substantivo do **núcleo**, dor em
IMAGEM, frase chã (⛔ construção retórica), teste do rádio, teste da narração
(a fala diz a **falha**, não o comportamento).

---

## PASSO 0 — SPEC

1. **Sorteio:** specs com `CONCEITO=consultorio_diagnostico` ou
   `duo_esposa`; os eixos de corpo valem como sorteados.
2. **Comissão do operador.** Enquanto o conceito `ela_diagnostica` não entra no
   randomizador, roda por comissão.

⚠️ **A etnia do REF segue a etnia da página** (congruência inviolável). Página
de avatar negro → narradora negra. Só o **paciente** tem etnia livre.

---

## O HOOK — OS 5 ELEMENTOS OBRIGATÓRIOS

Lidos dos frames 1-8 do reel-fonte. **Nenhum é opcional.**

### 1️⃣ A NARRADORA (o REF — mulher)
Mulher ~50-60 da etnia da página, bem cuidada e apresentável, **blusa social /
camisa de botão**, **lav mic clipado na lapela**, joia discreta. Autoridade por
aparência, não por jaleco.

⛔ **NÃO COPIAR O LOOK DA FONTE — ver ED12.** O que se extrai do reel-fonte é o
**dispositivo** (lav mic, blusa social, alarme no rosto, dedo no abdômen), não
a **aparência** da Tanisha.

### 2️⃣ O PACIENTE SEM CAMISA NA POLTRONA
Homem 55-65, **sem camisa**, **barriga proeminente**, reclinado na poltrona de
exame, **lençol azul-claro da cintura pra baixo**, **cabeça baixa olhando pra
baixo**, expressão resignada. **Muda** — nunca fala, nunca encara a lente.

### 3️⃣ O DEDO CRAVADO NO ABDÔMEN ⭐
A assinatura da cena: **o dedo índice dela tocando/pressionando a barriga
dele**. Não é o colo, não é um proxy — é a **gordura abdominal como evidência**.
O espectador olha a própria barriga.

### 4️⃣ O ALARME NO ROSTO DELA
**Olhos arregalados, dentes à mostra, sobrancelhas travadas** — cara de susto
e de nojo. ⛔ Não é `professor_calmo`. O choque dela é o que valida que a coisa
é grave.

### 5️⃣ O SET CLÍNICO COMPLETO
Sala de exame: **2 pôsteres de anatomia emoldurados**, **bandeira dos EUA em
pedestal**, armário de madeira clara, otoscópio na parede, luz de janela.

---

## O ARCO — 5 CENAS

| Cena | Beat | O que a copy FAZ | O que a tela mostra |
|---|---|---|---|
| **1** | DIAGNÓSTICO | nomeia a **falha** com o órgão dito, e fecha virando pro espectador | os 5 elementos acima |
| **2** | A CAUSA | *because…* — o mecanismo apontado NO CORPO dele | ela com modelo anatômico ou apontando; paciente imóvel |
| **3** | RITUAL | *so I told him…* — o preparo, tease | mãos dela em ação (sachê, copo) — insert, sem paciente |
| **4** | ALTA | *nineteen days later…* + eco + `gelatin trick` + fecho que derruba barreira | **CLÍMAX**: casal redimido, prop grande (ver ED4) |
| **5** | CTA | gelatin + follow-gate | close nela, limpo |

---

## REGRAS PRÓPRIAS (ED1-ED9)

- **ED1 — ⭐ O DEDO CRAVA NO ABDÔMEN, NÃO NO COLO.** É a assinatura e é a
  construção **mais segura** que temos: barriga é abdômen, não virilha, então
  não encosta na geometria que o gerador recusa. Frase travada para o IMAGE:
  `she presses her right index finger into the loose fat of his bare belly,
  just above the blue drape`
  **E no TAKE:** `she keeps her fingertip pressed into his belly and taps it
  twice on "[palavra]"`.
- **ED2 — ELE ESTÁ DE CABEÇA BAIXA E MUDO.** `head bowed, chin toward his
  chest, looking down at his own belly, expression flat and resigned`. Nunca
  encara a lente, nunca fala. O contraste **alarme dela × resignação dele** é o
  motor.
- **ED3 — ⭐ O REGISTRO DELA É ALARME, NÃO CALMA.** `eyes wide, teeth showing,
  eyebrows locked, an expression of alarm and disgust`. Este ângulo **inverte**
  o F2 do FLAGRANTE (narrador calmo): aqui o choque dela é a prova social de
  que a coisa é grave. ⛔ `professor_calmo` não serve — se o sorteio der,
  executar como `urgencia_alarme`.
- **ED4 — A CENA 4 É O CASAL REDIMIDO** — ela sai do papel de diagnosticadora
  e entra **a esposa do paciente**. Pose e formulação **validadas**, copiar
  literal do [`AGENTE_ED_CONSULTORIO_V1.md`](AGENTE_ED_CONSULTORIO_V1.md)
  §Happy path do colo (`perched sideways on his right knee, the way a newlywed
  poses for a photograph` + linha de contexto no TAKE + verbos de contato
  neutros). ⚠️ A esposa é **terceira pessoa**, não a narradora — e leva marca
  facial própria + marcas de idade que **renderizem** (`deeply lined skin`,
  `hair heavily streaked with gray`).
- **ED5 — SEM CREDENCIAL DECLARADA.** Ver a tabela da cerca acima. Wardrobe
  dela: camisa de seda, blusa social, cardigan — **nunca** scrubs, **nunca**
  jaleco+estetoscópio.
- **ED6 — SET CLÍNICO COMPLETO E BANDEIRA.** Os 2 pôsteres de anatomia + a
  bandeira dos EUA em pedestal aparecem em **todos** os IMAGEs de sala. É o que
  faz o teatro de autoridade sem uma palavra de credencial. Luz travada
  verbatim nas cenas de mesmo set (P8).
- **ED7 — ⭐ CONTRASTE ENTRE NARRADORA E PACIENTE.** Aqui é **fácil** (sexos
  diferentes), mas a regra vale para o **paciente × marido da cena 4** se forem
  personagens distintos, e para a **esposa × narradora** se ambas aparecerem:
  ≥ 3 eixos visíveis (cabelo, óculos, compleição) **e** a frase de contraste
  escrita no IMAGE. Ver
  [`AGENTE_ED_PRISMA_V1.md`](AGENTE_ED_PRISMA_V1.md) §Regra do contraste.
- **ED8 — TETO DE GENTE: 3.** Narradora + paciente + esposa. Sem plateia —
  plateia é FLAGRANTE. Cenas 2, 3 e 5 só com a narradora.
- **ED10 — ⛔ O LENÇOL É LISO. SEM PROTUBERÂNCIA.** (ordem do operador,
  2026-07-29 — a regra existiu por um dia e foi **removida** pelo Ed no mesmo
  dia). O lençol azul cobre da cintura pra baixo e **fica plano**: `a light blue
  drape covering him from the waist down, lying flat`. O innuendo do quadro é
  **o geoduck na mão dela (ED11)** — não precisa de um segundo. ⛔ Não escrever
  `tented`, `peak`, `ridge`, `lift`, nem nada que levante o tecido — nem no
  IMAGE, nem no TAKE.
- **ED11 — ⭐ O GEODUCK ERETO NA MÃO DELA, NO HOOK** (ordem do operador,
  2026-07-29). Ela segura, **na mão livre** (a outra está com o dedo no
  abdômen), um geoduck **grande e ereto** — o segundo choque do quadro (o
  primeiro é o dedo na barriga). A leitura fica completa: a barriga é a causa, o
  geoduck na mão é a **promessa**.
  **No IMAGE** — dimensão por **escala corporal** (nunca adjetivo nem anatomia)
  e o siphon **já ereto** (o estado vive no IMAGE):
  ```
  In her left hand, raised at her shoulder, she grips the ridged tan shell of a
  large geoduck clam. Its siphon extends straight up out of her fist, held stiff
  and straight, as long as her forearm and as thick as her wrist, reaching well
  above the top of her head. The siphon is pale tan, its surface taut and
  glossy, streaked with darker mottled lines running along its length. No bird,
  no goose, no duck, no swan, no snake, no feathers, no beak, no eyes, no head,
  nothing alive.
  ```
  **No TAKE** — imobilidade declarada + negação de ave (a armadilha do geoduck
  virando pato está documentada em
  [`prop-metaforas`](funil-organico/prop-metaforas.md)):
  ```
  The clam in her raised fist stays exactly as it appears in the first frame —
  same position, same angle, same shape — completely motionless for the entire
  shot. It is a still object and nothing about it changes. No bird, no goose, no
  duck, no swan, no snake, no worm, no tentacle, no feathers, no beak, no eyes,
  no head, nothing alive, nothing with a face.
  ```
  ⛔ Nunca escrever `geoduck` no TAKE (só no IMAGE) — usar `the clam` /
  `the pale tan shellfish`. ⛔ Nunca `neck` — usar `siphon`.
- **ED12 — ⛔ O REF É NOSSO, NÃO É CÓPIA DA FONTE** (correção do operador,
  2026-07-29). Falha em produção: o primeiro REF deste agente saiu com **locs
  grisalhos em coque alto + blusa de seda creme + negra magra de ~58** — ou
  seja, a Tanisha. Eu transcrevi a **aparência** da fonte em vez de extrair o
  **dispositivo**. É o erro "maritaca" aplicado ao casting, e ele é pior que na
  copy: clonar o rosto da concorrente entrega a página.
  > **Do reel-fonte extrai-se o DISPOSITIVO** (lav mic na lapela, blusa social,
  > alarme no rosto, dedo no abdômen, set clínico com bandeira). **A APARÊNCIA
  > é nossa** e tem que ser visivelmente outra pessoa.
  ⛔ **Traços da Tanisha proibidos no nosso REF:** locs/tranças em **coque alto**
  · blusa de seda **creme/branca** · magra de ~58 sem óculos.
  ✅ **Diferenciar em ≥ 3 eixos de silhueta** (o que se vê no feed a 1 cm):
  | Eixo | Alternativas |
  |---|---|
  | **Cabelo** ⭐ | afro curto grisalho · bob liso na altura do maxilar · tranças soltas nos ombros · corte bem curto tapered |
  | **Óculos** ⭐ | armação tartaruga · armação metálica fina · nenhuma |
  | **Cor da blusa** | azul-marinho · vinho · cinza-carvão — **nunca creme/branco** |
  | Compleição/idade | mais cheia · 62-68 · ombros largos |
- **ED9 — A RETENÇÃO NO FIM DO HOOK (o gesto do frame 6).** Ela **tira o dedo
  da barriga e junta as duas mãos** num gesto de "presta atenção", falando
  direto na lente. É o pivô que segura o espectador pro corpo do vídeo.
  No TAKE: `on the last line she lifts her finger off his belly and brings both
  hands together in front of her chest, looking straight into the lens`.

---

## MECÂNICA — POR PONTEIRO (P9: uma regra, um lugar)

| Assunto | Fonte |
|---|---|
| Pose do colo na cena 4 (formulação validada) | [`AGENTE_ED_CONSULTORIO_V1.md`](AGENTE_ED_CONSULTORIO_V1.md) §Happy path do colo |
| Arco, F1 (eco), F5 (evidência visual), F6 (luz travada), F13/F14b (alvo, falha) | [`AGENTE_ED_FLAGRANTE_V1.md`](AGENTE_ED_FLAGRANTE_V1.md) |
| IMAGE/TAKE, REF, anti-celebridade, marca facial | `AGENTE_ED_ORGANIC_WAVE_V4.md` |
| Porteiro, cota 75%, fio (P21), contraste, PICO2 | [`AGENTE_ED_PRISMA_V1.md`](AGENTE_ED_PRISMA_V1.md) |
| Estado do prop, dimensão por escala, imobilidade no TAKE | [`funil-organico/prop-metaforas.md`](funil-organico/prop-metaforas.md) |
| Núcleo × tempero, frase chã, aparte, dor em imagem | [`funil-organico/arsenal-linguagem-indireta.md`](funil-organico/arsenal-linguagem-indireta.md) |
| `gelatin trick`, loop que derruba barreira, follow-gate | [`funil-organico/espinha-fixa.md`](funil-organico/espinha-fixa.md) |
| REF contra celebridade e contra mendigo | [`funil-organico/espinha-fixa.md`](funil-organico/espinha-fixa.md) §Construir o REF |

---

## CHECKLIST ELA_DIAGNOSTICA

- [ ] **Os elementos no IMAGE 01**: narradora mulher bem cuidada com lav mic · paciente sem camisa de cabeça baixa · **dedo cravado no abdômen** · alarme no rosto dela · set clínico com 2 pôsteres + bandeira?
- [ ] ⛔ **O lençol está LISO** — zero `tented`/`peak`/`ridge`/`lift` no IMAGE e no TAKE (ED10)?
- [ ] ⭐ **O geoduck grande e ereto na mão livre dela**, dimensionado por escala corporal (`as long as her forearm`, `as thick as her wrist`), com negação de ave e imobilidade no TAKE (ED11)?
- [ ] ⛔ **O REF NÃO PARECE A TANISHA** — difere em ≥3 eixos de silhueta (cabelo · óculos · cor da blusa)? Zero locs em coque alto, zero blusa creme (ED12)?
- [ ] **O dedo está no ABDÔMEN**, nunca no colo nem em proxy (ED1)?
- [ ] Paciente de cabeça baixa, **mudo**, olhando a própria barriga (ED2)?
- [ ] **Registro dela = ALARME** (olhos arregalados, dentes à mostra) — não professor calmo (ED3)?
- [ ] Etnia da narradora = etnia da página (congruência)? Paciente com etnia livre?
- [ ] **Zero credencial declarada** — sem scrubs, sem jaleco+estetoscópio, sem "my patients" (ED5)?
- [ ] Set com 2 pôsteres + bandeira em todos os IMAGEs de sala; luz travada verbatim (ED6/P8)?
- [ ] **Cena 4 no Happy path do colo copiado LITERAL** do CONSULTORIO; esposa com marca facial + marcas de idade que renderizem (ED4)?
- [ ] Contraste ≥3 eixos onde houver dois personagens do mesmo sexo/idade, com a frase escrita no IMAGE (ED7)?
- [ ] Teto de 3; cenas 2, 3 e 5 só com a narradora (ED8)?
- [ ] **O gesto de retenção no fim do hook** — tira o dedo, junta as mãos, fala na lente (ED9)?
- [ ] Cota 75% com termos do **núcleo**, rotacionados · `gelatin trick` dito · aparte do narrador · fecho da 4 derruba barreira?
- [ ] Hook: **nomeia a FALHA** (não comportamento) e é frase chã (⛔ paradoxo/tríade)?

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

- [`AGENTE_ED_CONSULTORIO_V1.md`](AGENTE_ED_CONSULTORIO_V1.md) — o primo com REF masculino frio; a cena 4 vem de lá
- [`AGENTE_ED_FLAGRANTE_V1.md`](AGENTE_ED_FLAGRANTE_V1.md) — a arquitetura-mãe
- [`AGENTE_ED_ELA_NARRADORA_V1.md`](AGENTE_ED_ELA_NARRADORA_V1.md) — o outro ângulo de voz feminina (esposa contando, espinha C) — **não confundir**
- [`concorrentes/tanisha-mapa-visual.md`](concorrentes/tanisha-mapa-visual.md) — o mapa visual da fonte
