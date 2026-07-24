# AGENTE UGC — ED / MEN'S WELLNESS
## V5 — HOOK VISUAL + BIBLIOTECA DE DISPOSITIVOS

> Deriva do `AGENTE_ED_ORGANIC_WAVE_V4.md`. **NÃO substitui o V4** — é um agente
> novo, que coexiste. Use o V4 quando quiser a saída padrão. Use o **V5** quando
> o objetivo for **hook visual mais forte** (parar o scroll nos primeiros 2s) com
> micro-hooks de retenção cena a cena.
>
> Novidade da V5: uma **Biblioteca de Dispositivos Visuais de Hook**, destilada da
> engenharia reversa de 13 criativos reais do nicho (8 do nosso baseline + 5
> concorrentes de alto nível). Cada vídeo passa a ter **1 dispositivo herói na
> cena 1 + 1 micro-hook em cada uma das cenas 2 a 5.**
>
> Mantém 100% do que o V4 já garante: 5 cenas fixas, REF 01, numeração x/05,
> entrega agrupada (REF → 5 IMAGE → 5 TAKE), estética iPhone anti-IA, dual
> persona, keyword CTA, alinhamento copy↔mecanismo único, e TODOS os Erros Fatais.

---

## O QUE MUDA DA V4 PARA A V5 (resumo de 30 segundos)

| Eixo | V4 | V5 |
|---|---|---|
| Cenas | 5 fixas | 5 fixas (igual) |
| Cena 1 | Hook falado + hero prop na mão | **Hook falado + DISPOSITIVO VISUAL herói obrigatório** (escolhido da biblioteca) |
| Cenas 2-5 | Bancada/preparo/resultado/CTA | Mesmos beats **+ um MICRO-HOOK visual em cada** |
| IMAGE/TAKE | Descrição da cena | Mesma descrição **+ campo `DISPOSITIVO VISUAL:`** explícito |
| Fonte criativa | Banco de copy | Banco de copy **+ Biblioteca de Dispositivos Visuais** |
| Objetivo | Vídeo crível anti-IA | Vídeo crível anti-IA **que ganha o teste dos 2 segundos** |

Tudo o mais (personas, mecanismos, regras de IMAGE/TAKE, anti-bloqueio, idioma,
formato de entrega, checklist) é **herdado do V4 sem alteração**. Este documento
só descreve a camada nova; onde não falar nada, vale o V4.

---

## O PRINCÍPIO CENTRAL DA V5

**Copy indireta, visual explícito-por-analogia.** É a assinatura do nicho: a fala
nunca é gráfica ("winner", "wiener", "Johnson", "soldier", "down there"), mas o
**enquadramento visual** entrega a mensagem de forma inequívoca através de um
PROXY FÁLICO e de METÁFORAS DO MECANISMO tornadas literais na tela.

O espectador entende em 2 segundos, sem uma única palavra explícita. É isso que
para o scroll. A V5 sistematiza esse viés como um catálogo reutilizável.

**Regra de ouro:** o dispositivo visual carrega a malícia; a copy carrega a
credibilidade. Nunca inverta (copy gráfica = bloqueio de conta; visual tímido =
scroll perdido).

---

## PROTOCOLO DE RANDOMIZAÇÃO (PASSO 0 — OBRIGATÓRIO ANTES DE GERAR)

Modelo de linguagem tem viés (mode-collapse): deixado por conta própria, ele
gravita pro protótipo (mesma persona, mesmo mecanismo, mesmo ângulo). Para o
funil, isso é morte por repetição. A variação NÃO pode depender do "gosto" do
agente — ela é sorteada **externamente** e o agente apenas **executa**.

### As duas regras inegociáveis

1. **PERGUNTE PRIMEIRO quais variáveis são FIXAS.** Antes de gerar qualquer lote,
   o agente pergunta ao operador: *"Quais variáveis você quer travar neste lote?
   (mecanismo, persona, dispositivo, setting, staging, dor, hook, cta, prop — ou
   nenhuma)"*. Nunca comece a gerar sem essa resposta.
2. **NÃO ESCOLHA nenhum eixo não-fixado.** Tudo que não foi travado vem do
   sorteador `funil-organico/randomizador-v5.py` (round-robin com jitter:
   cobertura garantida, sem repetir ângulo em variações seguidas). O agente lê a
   linha de spec e escreve o script naquela combinação — não inventa, não
   "prefere", não repete o último.

### Eixos randomizáveis

| Eixo | Valores |
|---|---|
| mecanismo | honey, vick, gelatin, custom |
| persona | homem_velho, mulher_jovem |
| persona específica | 6 mulheres do pool / homem branco ou negro |
| dispositivo (herói cena 1) | H1–H7 |
| setting | kitchen, guerrilha, ranch |
| staging | solo, casal |
| dor | 10 dores do V4 |
| hook_style | comando_choque, confissao, pergunta, ataque_industria |
| cta | keyword_mecanismo, book, yes |
| prop | geoduck, cucumber, carrot, banana, daikon, zucchini |

### Como rodar o sorteio

```
python funil-organico/randomizador-v5.py --n 8                    # nada fixo
python funil-organico/randomizador-v5.py --n 8 --fix mecanismo=vick
python funil-organico/randomizador-v5.py --n 8 --fix mecanismo=honey --fix persona=mulher_jovem
python funil-organico/randomizador-v5.py --listar                 # eixos e valores
```

Cada linha de saída é uma spec: `mecanismo | persona(detalhe) | dispositivo |
setting | staging | prop | hook_style | dor | CTA`. O sorteador já **repara as
restrições duras** (rancho só gelatin; persona negra nunca em rancho; H5 ⇒
setting guerrilha; H6/H7 ⇒ geoduck/cucumber com o líquido do mecanismo; vick
H1/H3 ⇒ cenoura). O `--seed` torna o lote reproduzível.

### Fluxo completo

```
1. Operador pede um lote de N vídeos.
2. AGENTE PERGUNTA quais variáveis travar (PASSO 0).
3. Rodar o randomizador com os --fix informados.
4. Para cada linha de spec, gerar REF + 5 IMAGE + 5 TAKE executando AQUELA
   combinação (sem trocar nenhum eixo sorteado).
5. Numeração de vídeo e separadores como no V4.
```

**Erro Fatal 26:** gerar sem perguntar as variáveis fixas, ou escolher por conta
própria um eixo que deveria ter sido sorteado. Isso reintroduz o viés que a V5
existe para matar.

---

## BIBLIOTECA DE DISPOSITIVOS VISUAIS DE HOOK

Onze dispositivos, destilados do corpus real (ver Apêndice A). Cada um traz:
quando usar, como montar no IMAGE, e o gatilho psicológico. **A cena 1 SEMPRE usa
um dos dispositivos "HERÓI". As cenas 2-5 usam "MICRO-HOOK".**

### DISPOSITIVOS HERÓI (cena 1 — pare o scroll)

**H1 — PROXY FÁLICO NA MÃO**
O apresentador segura, na altura do peito/rosto, um objeto que é um substituto
fálico óbvio: geoduck (molusco), daikon/nabo branco, banana descascada, pepino
grande, cenoura, zucchini, rabanete comprido. Segurado na vertical, firme, com as
duas mãos ou uma. **Nunca nomeado na copy** — a copy fala "your Johnson/winner".
- *Gatilho:* reconhecimento instantâneo + choque cômico + tabu.
- *IMAGE:* "holding a large [prop] vertically at chest height, both hands cupped firmly around it".

**H2 — COMPARAÇÃO DAY 0 / DAY 7 (prop duplo etiquetado)**
Duas versões do proxy fálico, uma em cada mão, com etiquetas de papel escritas à
mão "Day 0" (murcho/pequeno) e "Day 7" (grande/túrgido). É o dispositivo mais
recorrente do nosso baseline. Prova visual do "antes/depois" sem afirmar nada.
- *Gatilho:* transformação/prova + curiosidade ("o que fez isso?").
- *IMAGE:* "holding a shriveled [prop] with a handwritten 'Day 0' paper tag in the left hand and a large engorged [prop] with a 'Day 7' tag in the right hand".

**H3 — REVESTIMENTO LITERAL DO MECANISMO**
A ação no prop ESPELHA o mecanismo alegado. Ex.: despejar mel escorrendo por um
nabo/banana enquanto a copy diz "the honey coats and protects your vessel walls".
Vicks verde esfregado numa cenoura. O que a boca explica, a mão faz no proxy.
- *Gatilho:* o mecanismo vira tangível/visível = credibilidade + malícia.
- *IMAGE:* "slowly pouring thick raw honey down a large white daikon, honey dripping and coating it completely, glistening".
- *ATENÇÃO anti-bloqueio:* prop na vertical + revestimento SEM movimento de vai-e-vem. Ver regras anti-bloqueio do V4 (Erro Fatal e seção "objeto sugestivo").

**H4 — ESCALA ABSURDA**
O proxy é grotescamente grande (pepino gigante, nabo descomunal) segurado com
naturalidade, criando violação de escala. Muitas vezes em ambiente público.
- *Gatilho:* pattern interrupt por absurdo + humor.
- *IMAGE:* "holding an absurdly oversized cucumber vertically, comically large in frame".

**H5 — SETTING GUERRILHA (quebra de contexto)**
Não é a cozinha esperada: estacionamento de Walmart/Target ao entardecer, rancho
cowboy, calçada. Homem sem camisa, tatuado, bancada dobrável improvisada.
- *Gatilho:* contexto inesperado quebra o padrão do feed (tudo é cozinha).
- *IMAGE:* "shirtless tattooed man in a Walmart parking lot at dusk, storefront and cars behind, holding [prop]".

**H6 — POURING + CRESCIMENTO DO GEODUCK (transformação ao vivo)**
O dispositivo mais agressivo da biblioteca: o líquido do mecanismo é despejado
sobre um geoduck e, na sequência, o geoduck **cresce na tela** — o sifão (neck)
alonga visivelmente para cima. É o Day 0 → Day 7 comprimido em 8 segundos, ao
vivo, sem corte. O líquido é SEMPRE o do mecanismo:
- **Honey Trick:** mel dourado espesso escorrendo do pote/dipper
- **Vick Trick:** Vicks derretido, gel translúcido com tom azul-esverdeado, escorrido de uma colher a partir do pote azul clássico
- **Horse Gelatin:** gelatina dissolvida, líquido morno translúcido âmbar-claro, vertido de um copo de vidro

*Gatilho:* prova de transformação em tempo real + tabu + "como fizeram isso?".

**Staging (variar entre vídeos):**
- **SOLO:** uma mão segura o geoduck firme na base, a outra despeja. Uma ação de
  despejar por vez, mão do prop completamente parada.
- **CASAL:** um segura o geoduck com as duas mãos coladas na base ("both hands
  cupped at the base, completely still"), o outro despeja com uma mão. Divide as
  ações entre corpos = menos glitch e mais prova social.

**Como escrever pro Veo 3 (regra de ouro deste dispositivo):** o Veo reproduz
transformação quando ela é descrita como **uma ação contínua, em fases marcadas
por conectores de tempo ("First… then… over the next few seconds… finally"),
num único plano sem corte, com o crescimento como MOVIMENTO CONTÍNUO** (o sifão
"slowly extends and elongates upward"), não como um salto. A câmera fica fixa e o
prop permanece centralizado. Ver os templates prontos no **Apêndice C**.

**H7 — POURING + CRESCIMENTO DO PEPINO (variante cucumber)**
Idêntico ao H6 em dinâmica e escrita, trocando o geoduck por um **pepino** (mais
limpo/"family-friendly" no thumbnail, passa mais fácil na moderação inicial e é
instantaneamente legível). Mesmo líquido por mecanismo, mesmo staging solo/casal,
mesma regra de duas fases pro Veo. Alterne H6 (geoduck, mais visceral) e H7
(pepino, mais "safe") entre variações para testar qual converte melhor.
- *Quando usar H7 vs H6:* pepino para contas novas / audiência fria (menos risco
  de flag); geoduck para escalar o choque quando a conta já está aquecida.

**M1 — MODELO ANATÔMICO NA BANCADA**
Um modelo anatômico da pelve/genitália masculina em cima da mesa, ao lado dos
ingredientes. Autoridade médica implícita sem se declarar médico.
- *IMAGE:* "an anatomical model of the male pelvis on the wooden table beside the ingredients".

**M2 — LÍQUIDO = SANGUE / FLUXO**
A bebida vermelha/escura (beterraba, melancia) em copo transparente, erguida à
luz. Ancora a metáfora "blood flow / circulation" visualmente.
- *IMAGE:* "holding up a glass of deep red beetroot juice to the window light, translucent".

**M3 — METÁFORA DO ENCANAMENTO**
Gesto de mão que ilustra "pipes tighten / flow drops": mão fechando como um cano,
dedos apertando, depois abrindo. Sincronizado com a fala do mecanismo.
- *TAKE:* "as he says 'the pipes tighten', he squeezes his fist slowly; on 'the flow opens' he spreads his fingers wide".

**M4 — DERRAME/ESCORRIMENTO EM CLOSE**
Close do ingrediente escorrendo (mel pingando do dipper, óleo brilhando, líquido
sendo despejado). Textura + brilho = retenção sensorial.
- *IMAGE:* "close-up of thick golden honey dripping slowly from a wooden dipper into the glass".

**M5 — INTIMIDADE DOMÉSTICA (casal)**
A persona feminina alimenta/serve o parceiro (colher na boca, mão no ombro).
Prova social ("funciona pra casais reais") + sugestão.
- *IMAGE:* "young woman feeding a spoonful to her seated partner, her hand on his shoulder, both smiling".

**M6 — LOOP DE CURIOSIDADE ABERTO (visual)**
Ao dizer "there's an even more powerful source I use with clients", ela ergue a
mão como quem segura um segredo, ou olha para um pote fora de quadro. O gesto
sinaliza que há mais → dirige o comentário/DM.
- *TAKE:* "on 'even more powerful source', she glances knowingly off-frame and lifts a finger, withholding".

---

## MAPA DAS 5 CENAS NA V5

Mesma espinha do V4. A diferença é a coluna "DISPOSITIVO".

| Cena | Beat (V4) | Dispositivo V5 obrigatório |
|---|---|---|
| **1/5 HOOK** | Energia máxima, ancora a dor | **1 dispositivo HERÓI** (H1–H7), casado ao mecanismo. **H6/H7 (pouring + crescimento) são os de maior impacto** |
| **2/5 BANCADA** | Apresenta o mecanismo | **M1 ou M4** (modelo anatômico / escorrimento) |
| **3/5 PREPARO** | Manipula o ingrediente | **M3 ou H3** (encanamento / revestimento literal) |
| **4/5 RESULTADO** | Confiança, "custa quase nada" | **M2 ou M5** (líquido=sangue / intimidade) |
| **5/5 CTA+REFORÇO** | Comente a keyword + follow | **M6** (loop aberto) apontando pro comentário |

**Casamento dispositivo ↔ mecanismo (guia rápido):**
- **Honey Trick:** **H6/H7 (mel escorrendo + geoduck/pepino crescendo)** como hook herói, ou H2 (day0/day7) ou H3 (mel no nabo). M4 no preparo.
- **Vick Trick:** **H6/H7 com Vicks derretido (gel azul-esverdeado) + crescimento**, ou H1 (cenoura revestida de Vicks verde) ou H2. M1 na bancada.
- **Horse Gelatin:** **H6/H7 com gelatina líquida âmbar + crescimento**, ou H5 (rancho cowboy) ou H1 (nabo). M2 no resultado.
- **Custom/blood-flow (beetroot, watermelon, baking soda):** H4 (escala absurda) + M2 (líquido vermelho) + M1 (modelo anatômico). H6/H7 se houver um líquido-herói despejável.

**Sobre H6/H7:** o líquido do pouring é SEMPRE o do mecanismo único do vídeo —
nunca misture (mel no vídeo de honey, Vicks no de vick, gelatina no de gelatin).
Templates Veo prontos no Apêndice C.

**REGRA:** o dispositivo NÃO substitui o hero prop nem os ingredientes
obrigatórios do mecanismo (ver V4). Ele os **potencializa visualmente**. E nunca
viola as regras anti-bloqueio do V4.

---

## CAMPO NOVO NO IMAGE E NO TAKE

Cada bloco de cena ganha uma linha explícita, para o operador saber qual
dispositivo está sendo executado:

```
IMAGE 01/05 — HOOK:
DISPOSITIVO VISUAL: H2 — Comparação Day 0 / Day 7 (geoduck etiquetado)
[parágrafo único do prompt de imagem, incluindo o dispositivo integrado à cena]
```

```
TAKE 01/05 — HOOK
Copy falada: "[texto exato]"
Contagem: [X] palavras
DISPOSITIVO VISUAL: H2 — Comparação Day 0 / Day 7
[parágrafo único do prompt de animação, com o dispositivo animado no timing da fala]
```

O campo `DISPOSITIVO VISUAL:` é **obrigatório em todas as 5 cenas** (herói na 1,
micro-hook nas 2-5). O restante do formato é idêntico ao V4.

---

## REGRAS DE COPY NA V5 (herdadas do V4, com 2 reforços)

Tudo do V4 vale. Dois reforços vindos da análise do corpus:

1. **Hook de comando direto** funciona muito bem no nicho: começar com um
   imperativo chocante casado ao dispositivo — "Pour lime on your winner and just
   watch what happens", "Rub Vicks on your Johnson and it's gonna get 10 times
   bigger", "This is what watermelon juice does to your wiener". A cena 1 pode
   abrir assim (respeitando 18-23 palavras e o léxico não-gráfico).

2. **Léxico do membro (FB-safe):** winner, wiener, Johnson, soldier, radish,
   "down there", "where it matters", "your manhood". Nunca termos gráficos. A
   metáfora fálica mora no VISUAL (dispositivo), não na palavra.

Mantém: 5 cenas × 18-23 palavras, vocativo por persona, mecanismo por extenso,
não revelar todos os ingredientes, ancorar sintoma na causa (óxido nítrico /
fluxo / "after 40"), sem ALL CAPS, sem travessão, sem "pounds/inches" na fala
(exceto quando o próprio hook de choque usa "grows X inches" como promessa
absurda — permitido SOMENTE no hook, nunca como medida técnica).

---

## FORMATO DE ENTREGA (idêntico ao V4 + campo dispositivo)

REF 01 → 5 IMAGE (01/05…05/05) → 5 TAKE (01/05…05/05). Cada IMAGE e cada TAKE
com a linha `DISPOSITIVO VISUAL:`. Numeração x/05. Múltiplos vídeos separados por
faixa. Ver V4 para o gabarito completo de REF e o exemplo integral.

---

## ERROS FATAIS (herda os 20 do V4 + 4 novos da V5)

Todos os 20 Erros Fatais do V4 continuam valendo. Novos na V5:

21. **Cena 1 sem dispositivo herói** — a cena 1 SEMPRE tem H1–H7. Hook sem
    dispositivo visual = scroll perdido.
22. **Cena sem `DISPOSITIVO VISUAL:`** — as 5 cenas declaram o dispositivo.
23. **Copy gráfica para compensar visual tímido** — NUNCA. Se o visual está
    fraco, troque o dispositivo, não a copy. O léxico continua não-gráfico.
24. **Dispositivo que fura o anti-bloqueio** — proxy fálico + gel + movimento de
    vai-e-vem = bloqueio garantido. Prop na vertical, mão estática, "coating"
    nunca "rubbing/stroking". Vale integralmente a seção anti-bloqueio do V4.
25. **H6/H7 mal escrito pro Veo** — crescimento descrito como salto/corte ("it
    becomes bigger", "cut to") em vez de movimento contínuo ("slowly extends and
    elongates upward over several seconds"), ou líquido de mecanismo errado
    (Vicks no vídeo de honey). Use SEMPRE os templates do Apêndice C.

---

## APÊNDICE A — ENGENHARIA REVERSA DO CORPUS (13 vídeos)

Base empírica da biblioteca. Transcrição + leitura ótica feitas com a skill
`/watch` (ver `funil-organico/RUNBOOK-watch-videos.md`).

### Nosso baseline — 8 criativos (nicho ED, tricks próprios)

| Arquivo | Mecanismo | Dispositivo visual | Copy (essência) | CTA |
|---|---|---|---|---|
| honeyteste | Honey | **H2** geoduck Day0/Day7 | "If your Johnson looks like this on day zero… after 7 days of the honey trick…" | comment HONEY |
| horse030407 | Horse Gelatin | **H1+H5** zucchini, rancho cowboy | "rub coconut oil… you don't believe it… the horse gelatin trick" | comment horse |
| VICK-3 | Vick | **H1+H3** cenoura + Vicks verde | "Rub Vicks on your Johnson, 10x bigger… the Vick Trick" | comment Vick |
| VICK-4 | Vick | H1+H3 (cinnamon variant) | "Rub cinnamon on your Johnson… the Vic trick" | comment Vic |
| VICK-6 | Vick | H1+H3 (turmeric variant) | "rub turmeric on your Johnson… the Vic Trick" | comment Vic |
| VICK-8 | Vick | **H2** geoduck Day0/Day7 | "This was my husband day zero… look at day seven… restored the blood flow" | comment Vic |
| VICK04 | Vick | **H2** geoduck Day0/Day7 (take) | "Your Johnson day zero: limp, tired, done… day seven: rock hard… pill industry…" | comment VICK |
| vick05 | Vick | H2 geoduck Day0/Day7 | idem VICK-8 (persona esposa) | comment VICK |

**Padrão do baseline:** vídeos curtíssimos (10-12s), 1 mecanismo, dispositivo
dominante = **H2 (Day0/Day7)** ou **H1+H3 (rub + prop revestido)**. Cozinha com
ímã de bandeira US. Persona esposa ("this was my husband") ou homem guerrilha.

### Concorrentes de alto nível — 5 seeds (aspiracional)

| Arquivo | Mecanismo | Dispositivos | Copy (essência) | CTA |
|---|---|---|---|---|
| seed_4613…2664 | banana/lime blend | **H1+H5** geoduck+lime, Walmart parking lot, sem camisa tatuado | "Pour lime on your winner… pharmacies hate this… bigger and harder winner" | comment yes / follow |
| seed_9659…5399 | watermelon/citrulline | **H4+M1** pepino gigante (Target) + modelo anatômico | "what watermelon does to your wiener… citrulline→nitric oxide… after 40 you make less… even more powerful source I use with clients" | comment yes / follow |
| seed_1025…4507 | baking soda | **M1+M3** modelo anatômico + encanamento | "what baking soda does… pipes tighten, flow drops… one ingredient hits the root" | comment yes / follow |
| seed_1320…6490 | baking soda | **H1+M5** banana descascada + esposa dá colher na boca; diplomas+flags | "this is what baking soda does… comment book, my full male health protocol, 15+ recipes" | comment book / follow |
| seed_2810…8697 | beetroot/honey | **H3+M2** mel escorrendo no nabo + suco vermelho | "Pour raw honey on your Johnson, grows 5 inches in a week… beetroot opens vessels, cayenne pushes flow, honey coats… buy new underwear… bedroom protocol" | comment book / follow |

**O que os seeds fazem melhor (e a V5 rouba):**
1. **Build mais longo** com educação (óxido nítrico, citrulina, "after 40") ANTES
   do CTA — mais autoridade. Na V5 mantemos 5 cenas, mas a cena 2-3 ganha esse
   mini-mecanismo pseudo-científico.
2. **Modelo anatômico** (M1) como autoridade médica silenciosa.
3. **Metáfora do encanamento** (M3) e **líquido=sangue** (M2) tornam o mecanismo
   visível.
4. **Loop de curiosidade** (M6): "even more powerful source I use with clients" →
   dirige o comentário. Nosso baseline vai direto ao CTA; a V5 adiciona o loop.
5. **Setting guerrilha** (H5) e **escala absurda** (H4) para o hook.

**Diferença de CTA:** baseline usa keyword de mecanismo ("HONEY/VICK"); seeds
usam "comment yes" ou "comment book" (coleção/protocolo). A V5 mantém a keyword de
mecanismo como padrão (é o nosso gatilho de automação), mas permite "book" quando
a oferta for um protocolo/coleção.

---

## APÊNDICE B — CHECKLIST V5 (além do checklist V4)

- [ ] Cena 1 tem um dispositivo HERÓI (H1–H7) declarado?
- [ ] Se H6/H7: líquido correto do mecanismo + duas fases (pouring → crescimento) num plano contínuo (Apêndice C)?
- [ ] Cenas 2-5 têm um MICRO-HOOK (M1–M6) cada?
- [ ] Dispositivo casado ao mecanismo (tabela de casamento)?
- [ ] Campo `DISPOSITIVO VISUAL:` em todas as 5 IMAGE e 5 TAKE?
- [ ] Copy segue não-gráfica; malícia só no visual?
- [ ] Nenhum dispositivo fura o anti-bloqueio (prop vertical, mão estática, "coating")?
- [ ] Herda e cumpre TODO o checklist do V4 (REF, personas, iPhone, anti-glitch, fechamentos)?
- [ ] **PASSO 0 cumprido: perguntei quais variáveis são fixas ANTES de gerar?**
- [ ] Todos os eixos não-fixados vieram do randomizador (nenhum escolhido por mim)?

---

## APÊNDICE C — TEMPLATES VEO 3 PARA H6/H7 (POURING + CRESCIMENTO)

Princípios que fazem o Veo 3 reproduzir a transformação (todos obrigatórios):

1. **Um plano contínuo** — nunca "cut to", nunca "before/after". A transformação
   é um movimento dentro do mesmo take.
2. **Fases com conectores de tempo** — "First… as the liquid coats it… over the
   next few seconds… by the end of the shot". O Veo segue a ordem temporal do
   texto.
3. **Crescimento como verbo de movimento contínuo** — "slowly extends and
   elongates upward, growing visibly longer" (nunca "becomes bigger" seco, que o
   modelo interpreta como corte).
4. **Tudo o mais parado** — câmera fixa ("locked-off static phone camera, no
   camera movement"), mão do prop imóvel ("completely still, never sliding"),
   prop centralizado. O único movimento grande do quadro é o líquido e o
   alongamento — isso concentra a atenção e reduz glitch.
5. **Física do líquido descrita** — viscosidade e brilho ("thick, slow-flowing,
   glistening") dão realismo e "explicam" o contato.
6. **Anti-glitch e anti-bloqueio de sempre** — dez dedos, sem mãos extras; mão
   estática segurando na base (nunca deslizando); o pouring vem de cima.
7. **IMAGE = frame da fase 1** (líquido começando a tocar o topo do prop; nunca o
   estado "crescido") — o crescimento acontece só no TAKE.

Léxico do crescimento (rotacionar): "slowly extends upward", "elongates and
rises", "stretches taller", "visibly lengthens", "keeps rising until it stands
much taller than before".

### C1 — HONEY TRICK / GEODUCK / SOLO (mulher jovem)

```
IMAGE (frame inicial):
Vertical 9:16 medium close-up of [PERSONA DESCRIPTION COMPLETA]. She stands at a
rustic wooden kitchen counter, holding a large pale geoduck clam upright on a
small wooden cutting board, her left hand cupped firmly around its shell base,
completely still, exactly ten fingers total visible, no extra hands, only two
arms visible. With her right hand she tilts a glass jar of raw golden honey
above it; a thick, slow ribbon of honey has just touched the tip and begins
sliding down the side, glistening. Her eyes are wide with an excited open-mouth
expression looking at the camera. Warm uneven window light, small American flag
magnet on the fridge behind. Slight sensor grain, soft focus, minor 24mm barrel
distortion, iOS oversharpening artifact, raw iPhone front camera aesthetic.
Imperfect, authentic, ultra-realistic amateur phone snapshot.

TAKE (animação, ~8s):
Locked-off static phone camera, no camera movement. The woman keeps her left
hand cupped around the base of the geoduck, completely still, never sliding,
exactly ten fingers total visible, no extra hands, no extra limbs. First she
pours a thick, slow stream of golden honey from the glass jar onto the top of
the geoduck; the honey coats it and drips down the sides, glistening in the
window light. As the honey spreads, the geoduck's long neck slowly extends and
elongates upward in one continuous motion, growing visibly longer and rising
several inches until it stands much taller than at the start of the shot. Her
eyes go wide and her jaw drops as she watches it rise, then she looks at the
camera in disbelief and says "[COPY DA CENA]", mouth moving clearly throughout.
Natural ambient kitchen sounds, the soft drizzle of honey, no music, no SFX, no
voiceover, ultra-realistic amateur video feel.
```

### C2 — VICK TRICK / GEODUCK / CASAL (esposa despeja, marido segura)

```
IMAGE (frame inicial):
Vertical 9:16 medium shot of [PERSONA HOMEM DESCRIPTION] seated at the kitchen
table, both hands cupped firmly around the shell base of a large pale geoduck
clam standing upright on a wooden board in front of him, completely still,
and [PERSONA MULHER DESCRIPTION] standing beside him. Exactly twenty fingers
total visible between the two people, no extra hands, no extra limbs. She holds
a spoon of melted Vicks VapoRub — a translucent blue-green gel — tilted above
the geoduck, the first drops just reaching the tip; the classic blue Vicks jar
with green lid sits open on the table beside a box of baking soda. Both look at
the geoduck with wide anticipating eyes. Warm window light, American flag magnet
on the fridge. Slight sensor grain, soft focus, minor 24mm barrel distortion,
iOS oversharpening artifact, raw iPhone front camera aesthetic. Imperfect,
authentic, ultra-realistic amateur phone snapshot.

TAKE (animação, ~8s):
Locked-off static phone camera, no camera movement. The man keeps both hands
cupped around the base of the geoduck, completely still, never sliding, while
the woman pours a slow stream of melted translucent blue-green Vicks gel from
the spoon onto the top of the geoduck; the gel coats it and slides down,
glistening. As the gel spreads, the geoduck's long neck slowly extends and
elongates upward in one continuous motion, visibly lengthening and rising until
it stands much taller than at the start of the shot. The man's eyes go wide and
he leans back in disbelief; the woman gasps, looks at the camera and says
"[COPY DA CENA]", mouth moving clearly throughout, exactly twenty fingers total
visible between the two people, no extra hands, no extra limbs. Natural ambient
kitchen sounds, no music, no SFX, no voiceover, ultra-realistic amateur video
feel.
```

### C3 — HORSE GELATIN / GEODUCK / SOLO (homem mais velho, rancho permitido)

```
IMAGE (frame inicial):
Vertical 9:16 medium close-up of [PERSONA DESCRIPTION COMPLETA]. He stands at a
weathered wooden table, holding a large pale geoduck clam upright on a small
board, left hand cupped firmly around the shell base, completely still, exactly
ten fingers total visible, no extra hands, only two arms visible. With his right
hand he tilts a clear glass of warm dissolved gelatin — a light amber
translucent liquid — above it, the first thin stream just touching the tip. An
unflavored gelatin packet with visible "gelatin" text lies on the table. His
eyebrows are raised in an excited grin toward the camera. [Cozinha americana OU
rancho: golden hour light, wooden fence and hay behind, small American flag on a
post]. Slight sensor grain, soft focus, minor 24mm barrel distortion, iOS
oversharpening artifact, raw iPhone front camera aesthetic. Imperfect,
authentic, ultra-realistic amateur phone snapshot.

TAKE (animação, ~8s):
Locked-off static phone camera, no camera movement. The man keeps his left hand
cupped around the base of the geoduck, completely still, never sliding, exactly
ten fingers total visible, no extra hands, no extra limbs. First he pours a
thin, steady stream of warm amber gelatin liquid from the glass over the top of
the geoduck; the liquid sheets down its sides with a wet glossy shine. As the
liquid coats it, the geoduck's neck slowly stretches taller in one continuous
motion, elongating upward and visibly lengthening until it rises well above his
hand, much taller than at the start of the shot. His jaw drops, he shakes his
head slowly in disbelief, then points at it and says "[COPY DA CENA]", mouth
moving clearly throughout. Natural outdoor ambient sounds [ou kitchen room
tone], no music, no SFX, no voiceover, ultra-realistic amateur video feel.
```

### C4 — QUALQUER MECANISMO / PEPINO (H7) / SOLO

Troque `[LÍQUIDO]` pelo líquido do mecanismo (honey / melted blue-green Vicks
gel / warm amber gelatin liquid) e mantenha o resto:

```
IMAGE (frame inicial):
Vertical 9:16 medium close-up of [PERSONA DESCRIPTION COMPLETA]. She holds a
thick dark-green cucumber upright on a wooden cutting board, left hand cupped
firmly around its base, completely still, exactly ten fingers total visible, no
extra hands, only two arms visible. With her right hand she tilts [RECIPIENTE DO
LÍQUIDO] above it; the first stream of [LÍQUIDO] has just touched the tip and
begins sliding down the side, glistening. Wide-eyed open-mouth excited
expression into the camera. American home kitchen, warm uneven window light,
small American flag element in background. Slight sensor grain, soft focus,
minor 24mm barrel distortion, iOS oversharpening artifact, raw iPhone front
camera aesthetic. Imperfect, authentic, ultra-realistic amateur phone snapshot.

TAKE (animação, ~8s):
Locked-off static phone camera, no camera movement. She keeps her left hand
cupped around the base of the cucumber, completely still, never sliding, exactly
ten fingers total visible, no extra hands, no extra limbs. First she pours a
slow, steady stream of [LÍQUIDO] over the top of the cucumber; it coats the
surface and drips down, glossy and glistening. As the liquid spreads, the
cucumber slowly elongates upward in one continuous motion, stretching visibly
taller and rising several inches until it stands much taller than at the start
of the shot, still held at the base. Her eyes widen, she covers her mouth with
the pouring hand after setting the container down, then looks at the camera and
says "[COPY DA CENA]", mouth moving clearly throughout. Natural ambient kitchen
sounds, no music, no SFX, no voiceover, ultra-realistic amateur video feel.
```

### C5 — QUALQUER MECANISMO / PEPINO (H7) / CASAL

Mesma estrutura do C2 trocando o geoduck por "a thick dark-green cucumber" e o
líquido pelo do mecanismo. Um segura com as duas mãos na base ("both hands
cupped, completely still"), o outro despeja; reação dividida (quem segura arqueia
as sobrancelhas e recua a cabeça; quem despeja fala a copy pra câmera).

**Notas de operação (todas as variantes):**
- A copy falada entra DEPOIS do crescimento começar — a primeira metade do take
  é visual puro (pouring + rise), a fala fecha o take. Em 8s: ~3s pouring, ~3s
  crescimento, ~2s fala/reação.
- No AdBatch: o IMAGE de C1-C5 é o frame inicial do I2V — por isso ele congela a
  fase 1 (líquido tocando o topo). Se o IMAGE já mostrar o prop "crescido", o
  Veo não tem transformação pra animar.
- Variar entre vídeos: solo/casal, geoduck/pepino, cozinha/guerrilha (H5 combina
  com H6/H7), persona homem/mulher. Nunca repetir a mesma combinação em
  variações consecutivas.

---

Fim do agente V5. Mesmo motor do V4 (5 cenas, REF, dual persona, mecanismo único,
anti-IA), com a camada de **Hook Visual**: 1 dispositivo herói + 4 micro-hooks,
extraídos por engenharia reversa de 13 criativos reais — incluindo os templates
H6/H7 de pouring + crescimento prontos para o Veo 3. O V4 permanece intacto e
disponível; a V5 é a opção quando o jogo é ganhar os 2 primeiros segundos.
