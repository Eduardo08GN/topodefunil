# ESTUDO — os raros em trios, e o preparo que faz sentido

Encomenda do operador (2026-08-19): *"pretendo criar um agente que irá utilizar
esses ingredientes nos vídeos que serão sobre receitas. De que forma esses
ingredientes podem ser preparados em pares de 3 em 3 [...] Quais os melhores
insumos para consumi-los?"*

O pool é o `RAROS` do [`botica16_short.py`](botica16_short.py), onde cada vídeo
usa **um**. Este estudo é para o agente novo, onde cada vídeo usa **três**.

⚠️ **Escrito sobre 9 e revisado sobre 14 no mesmo dia.** O commit `3a67be2` do
Eduardo levou o pool canônico de 9 para 14 entradas (`horny goat weed`, `panax
ginseng`, `saffron`, `catuaba`, `ashwagandha`) enquanto este arquivo estava em
pé. São **14 entradas e 13 plantas** — `epimedium` e `horny goat weed` são a
mesma planta com duas palavras faladas diferentes, de propósito.

---

## ⭐⭐ A pergunta que decide tudo: o que dissolve o quê

Antes de escolher veículo, uma regra de física que o roteiro não pode furar:

> **Raiz lenhosa não solta nada em água fria.** Semente mucilaginosa solta em
> água fria e não precisa de fogo. Princípio lipofílico não sai em água nenhuma
> — precisa de gordura. Folha e estigma entregam em calor **brando** e
> **estragam** em fervura.

São quatro comportamentos, não um. Um agente que sorteia "veículo" como eixo
livre vai produzir, na maioria dos vídeos, uma cena que mostra o oposto do que o
ingrediente faz — e é justamente o defeito que reprovou o `vick16`:
**distinção medida não é nexo medido.**

---

## 1. Os treze, um por um

| ingrediente | o que é, em quadro | o que extrai | ⭐ veículo certo | ⛔ veículo falso |
|---|---|---|---|---|
| **maca root** | pó amarelo-claro | amido (cerca de 70% do peso é carboidrato); o pó comercial já vem **pré-cozido** — é isso que "gelatinized maca" quer dizer, e não tem relação com gelatina | leite quente, batida cremosa, mingau | água fria pura (a tradição andina **sempre** cozinha) |
| **tongkat ali** | lascas de raiz marrom-clara | quassinoides e eurycomanona, **hidrossolúveis** — e o amargo vem deles | **decocção** de 20 a 30 min; o mesmo pedaço rende até 3 fervuras | água fria, batida crua |
| **tribulus** | vagens secas espinhosas | saponinas (protodioscina) | decocção | infusão rápida |
| **epimedium** / **horny goat weed** ⭐ | folhas secas em coração | icariina, flavonoide glicosídeo | decocção **curta** (10 a 15 min) ou maceração em vinho — as duas são tradição | fervura longa |
| **fenugreek** | sementes duras douradas | ⭐ **galactomanana** — mucilagem que sai em água **fria** e vira gel | **molho de 8 a 10h em água fria** (o clássico *methi water*); ou torrado e moído | — (é o mais flexível de todos) |
| **muira puama** | casca e raiz lascadas | ⛔ **lipofílico** — lupeol, ácidos graxos, terpenos; a literatura de campo diz que muitos ativos não são hidrossolúveis | **gordura**: leite integral; ou decocção longa | chá rápido, água gelada |
| **ginkgo** | folhas em leque | flavonoides + lactonas terpênicas | **infusão** — é folha, entra por último | decocção longa, gelatina fria |
| **mucuna** | grãos escuros brilhantes | L-DOPA (2 a 7% da semente) | ⭐ **molho longo → torra → moagem**: no México e na Guatemala isso é o *"Nescafé"* de mucuna | grão cru em água fria |
| **sarsaparilla** | pedaços de raiz torcida | saponinas de sarsapogenina — ⭐ **espumam** (é por isso que ela está na root beer, mais pela espuma que pelo sabor) | decocção | infusão rápida |
| **panax ginseng** ⭐ | raiz clara e torcida | ginsenosídeos, hidrossolúveis; o vermelho industrial sai de água a 90 °C por 14 a 16h | **decocção longa** (*insam cha*); e é raiz de **sopa** de verdade (*samgyetang*) | infusão de 3 minutos |
| **saffron** ⭐ | fios vermelho-escuros | crocina (cor, hidrossolúvel) + safranal (aroma, lipossolúvel) | ⛔⛔ **nunca na panela** — ver a regra abaixo | água fervente, gordura pura |
| **catuaba** ⭐ | lascas de casca avermelhada | decocção ou *garrafada* (infusão alcoólica) | decocção de 10 a 15 min | água fria |
| **ashwagandha** ⭐ | raiz bege e pó marrom-claro | withanolídeos — **lipossolúveis**, e a withaferina A é **termolábil** | ⭐ **fervida no LEITE** (*ksheerapaka*, 15 a 30 min) | fervura longa em água |

### ⛔⛔ A regra própria do saffron

Ele é o único do pool que **não pode entrar na panela**, e por dois motivos que
se somam:

1. **Água fervente destrói crocina e safranal em segundos.** O correto é
   60–70 °C por 15 a 20 minutos — água que queima a mão mas não fumega.
2. **Ele não libera cor em gordura pura.** Vai para o leite só *depois* de
   florescer numa colherada de água morna.

⭐ E isso, que parece um estorvo, é **o melhor beat visual do pool inteiro**: os
fios caem numa tigelinha de água morna e o líquido vira **ouro sozinho**, sem
ninguém mexer. Fervido, dá amarelo sujo. É a diferença entre o quadro que segura
e o quadro que não.

---

## 2. Os veículos, ranqueados

Ele perguntou por seis. Quatro se sustentam, dois não.

### ⭐⭐ 1º — A DECOCÇÃO (a panela) — serve 7 dos 13

A raiz lenhosa fervendo. É o preparo verdadeiro de **tongkat, tribulus,
epimedium, sarsaparilla, muira puama, ginseng e catuaba** — sete dos treze numa
panela só.

E é o mais fotogênico do estudo: vapor, a água mudando de cor, a espuma da
sarsaparilla subindo sozinha, o coador. **Movimento sem ator** — a mesma bala de
retenção que o `botica` compra com o utensílio em movimento.

### ⭐⭐ 2º — A GELATINA — e ela resolve a congruência de graça

Aqui está a jogada, e é a razão de este estudo existir:

> **A gelatina não compete com a decocção — ela é feita COM a decocção.**
> Ferve as raízes, coa, dissolve a gelatina no líquido ainda quente, leva para
> gelar. O cubo sai com a cor da raiz.

Isso mantém a **congruência inviolável** do funil (o mecanismo do criativo tem
de ser o que a VSL vende) sem que a receita vire propaganda: as ervas são o
conteúdo, e a gelatina é o formato. ⭐ E dá o payoff que o repo inteiro já sabe
filmar — o cubo, a tigela, a colher.

### ⭐ 3º — O LEITE / A BATIDA GORDA — o único que carrega o lipossolúvel

Não é escolha estética. **Muira puama, ashwagandha e maca só entregam com
gordura ou calor**, e o leite dá os dois. O `ksheerapaka` — raiz fervida no
leite — é preparo clássico documentado, não invenção nossa.

⚠️ O custo de cena: líquido opaco esconde o ingrediente. Quem escolher batida
precisa mostrar o pó **antes** de entrar, senão o quadro fica sem prova.

### ⭐ 4º — O MOLHO FRIO — só para o fenugreek, e ele é o coringa

O único do pool que vira **gel sozinho, em água fria, sem gelatina**. Oito a dez
horas de molho e a galactomanana engrossa a água.

⭐ Vale como beat: é a única textura do parque que o espectador não sabe
explicar. E rima com o cubo sem repeti-lo.

### ⛔ ÁGUA GELADA PURA — falsa para 12 dos 13

Raiz lenhosa em água fria não solta nada. Fora o fenugreek (que funciona) e a
diluição de um concentrado já pronto, o copo de água gelada com pó boiando é
**tecnicamente falso e visualmente morto** — nada acontece em quadro. É o pior
dos seis.

### ⛔ SOPA — funciona na química, quebra o enquadramento

Sopa é decocção com comida dentro, então quimicamente passa — e o ginseng tem
até um prato canônico (o *samgyetang*). Mas:

- sopa é **refeição**, não ritual — e o que converte aqui é o ritual secreto;
- 16 segundos não comportam uma refeição;
- e o público de 60+ nos EUA não liga sopa a performance. Liga a doente.

### ⚠️ CHÁ — honesto só para as folhas e para o estigma

Infusão é o preparo certo de **ginkgo, epimedium e saffron**. Para as nove
raízes, cascas e sementes, chamar de "tea" é impreciso, e quem conhece percebe.
Se a fala disser chá, que seja com folha ou fio em quadro.

---

## 3. ⭐⭐ A regra do trio: PAPEL, não ingrediente

Três de catorze dá **364 combinações**. A maioria não presta — três raízes
lenhosas juntas são o mesmo gesto três vezes, o mesmo marrom três vezes, e o
vídeo não tem o que mostrar.

O corte é por **papel na receita**:

| papel | o que faz | quem | gesto em quadro |
|---|---|---|---|
| **BASE** | ferve e dá cor e amargor | tongkat · muira puama · sarsaparilla · tribulus · ginseng · catuaba · ashwagandha | a panela, o vapor, o coador |
| **CORPO** | dá textura e substância | maca (pó) · fenugreek (gel) · mucuna (torrado) | bater, peneirar, torrar |
| **ACABAMENTO** | entra no fim, dá cor e aroma | epimedium · horny goat weed · ginkgo · saffron | mergulhar e tirar; ou florescer na água morna |

**Um de cada = 7 × 3 × 4 = 84 trios**, todos coerentes, cada um com **três
gestos diferentes e três cores diferentes** no mesmo vídeo.

⭐ Oitenta e quatro trios coerentes valem mais que trezentos e sessenta e quatro
sorteados: o que o espectador percebe é o contraste dentro do quadro, não o
tamanho do pool. É a lição do `banho16_3t` — *combinação nominal nunca foi a
métrica*.

⛔ **Uma trava obrigatória:** `epimedium` e `horny goat weed` são a **mesma
planta**. Como só se sorteia um ACABAMENTO por vídeo, eles nunca caem juntos —
mas a lente tem de existir, porque o dia em que alguém abrir o pool para dois
acabamentos, o vídeo vai nomear a mesma erva duas vezes com nomes diferentes.

### ⭐ O par que a própria tradição já fez

A literatura de campo da catuaba registra que os povos amazônicos que a usam
**a combinam com muira puama**, deixando a mistura em água morna de um dia para
o outro. É o único par do pool com combinação tradicional documentada — vale
como entrada privilegiada, não como regra.

⚠️ Mas os dois são BASE, então esse par só existe se o motor aceitar **duas
bases e nenhum acabamento** numa entrada de exceção. É decisão do operador, e o
preço é perder o terceiro gesto.

---

## 4. ⛔ O veículo é DERIVADO do corpo, nunca sorteado à parte

O erro que mata este agente antes de nascer é ter "veículo" como eixo livre.
Ele não é livre — o CORPO já o determina:

| corpo sorteado | veículo que vem junto |
|---|---|
| **maca** | leite / batida cremosa → e vira gelatina se quiser o cubo |
| **fenugreek** | molho frio (o gel) → ou entra na gelatina |
| **mucuna** | torrado e moído, bebida escura tipo café |

⭐ E há um segundo acoplamento, mais fino: quando a BASE é **ashwagandha**, a
decocção é **no leite**, não na água. Isso põe ashwagandha + maca na mesma
faixa e dá ao leite a entrada mais tradicional que ele tem.

A BASE está sempre na panela, o ACABAMENTO sempre no fim, e o **saffron nunca
na panela**. Sobra **um** eixo de escolha real: **fecha em copo ou fecha em
cubo**. Dois estados, e os dois congruentes com a VSL.

Sem esse acoplamento o motor produz mucuna torrada dentro de água gelada e fio
de açafrão fervendo por 20 minutos — exatamente o *"elemento visual sem nexo"*
que reprovou o `vick16` com 7.153 linhas e 0 ERRO em 600 sorteios.

---

## 5. As três decisões que são do operador

Nenhuma é minha, e nenhuma dá para deduzir do código:

1. **CT5 — a fala nomeia os três?** A trava de 16s diz que ingrediente não se
   nomeia na fala, porque *a receita é a moeda*. Um agente de receita com três
   ervas ou fura o CT5 (precedente declarado: `prato16`, `mel16`, `gelahorse16`)
   ou põe os três **no quadro** e a fala promete só *"the three roots"*.
   ⭐ Sugestão: a fala nomeia **um** — o mais estranho, que é a isca — e os
   outros dois ficam em quadro. Curiosidade sem entregar a receita.
2. **A gelatina fica em quadro?** Sugestão: sim, como finalizador — é o que
   segura a congruência com o que a VSL vende sem custar um beat.
3. **O par catuaba + muira puama vira exceção?** Duas bases, sem acabamento, em
   troca do terceiro gesto.

⚠️ **O gargalo do pool é o CORPO, com três entradas.** BASE tem sete e
ACABAMENTO tem quatro; cada corpo novo vale **28 trios**. Se um dia o pool
crescer de novo, é aí que ele deve crescer.

---

## 6. ⚠️ Segurança — cinco linhas, porque o público é 60+

Sem sermão, mas o dado é real e muda a redação:

- **mucuna** carrega L-DOPA de verdade (2 a 7% da semente) — é farmacologia, não
  tempero, e conversa com remédio de Parkinson e com MAOI;
- **ginkgo** aumenta risco de sangramento com varfarina, aspirina e clopidogrel
  — e homem de 60+ é exatamente a população anticoagulada;
- **panax ginseng** também mexe com varfarina e com remédio de diabetes;
- **epimedium** mexe com pressão e coração;
- **fenugreek** derruba glicemia e é da família do amendoim e do grão-de-bico.

⭐ A mitigação já é doutrina da casa e custa nada: o rodapé
`Not medical advice. Talk to your doctor.` na página, e a cena enquadrada como
**demonstração**, nunca como prescrição — ninguém diz quanto, nem por quantos
dias.

---

## 7. Como pedir o agente

O caminho é o [`PIPELINE-NOVO-AGENTE.md`](../PIPELINE-NOVO-AGENTE.md). O que
este estudo já entrega pronto:

- **eixo 1 — o TRIO**: 84 entradas (base × corpo × acabamento), cada uma com os
  três `img` que já existem no `RAROS` do botica;
- **eixo 2 — o FECHAMENTO**: copo ou cubo, 2 entradas;
- **derivados** (não sorteáveis): o veículo sai do corpo, o gesto sai do papel,
  e a decocção do ashwagandha é no leite;
- **lentes obrigatórias**: (a) os três em quadro nos dois takes; (b) o aposto do
  raro nomeado; (c) gesto distinto por papel — se dois papéis mandarem o mesmo
  verbo, o trio é reprovado; (d) **saffron nunca na panela**; (e) `epimedium` e
  `horny goat weed` nunca no mesmo vídeo; (f) zero nome científico na fala.

⛔ O que **não** sai daqui: a copy. Fala é alçada do operador, e este documento
para na cena.

---

## Fontes

- [Boiling maca root — the traditional way](https://nutri.it.com/can-i-boil-maca-root-and-drink-the-safe-and-traditional-preparation-method) · [Raw vs gelatinized maca](https://www.themacateam.com/gelatinized-maca-powder-how-it-s-different) · [Maca traditionally and today](https://riohealth.co.uk/blogs/news/maca-the-easy-superfood-traditionally-and-today)
- [Tongkat ali — evidence of human use](https://akarali.com/tongkat-ali-eurycoma-longifolia-evidence-of-human-use/) · [How to brew tongkat ali root tea](https://redtongkatalimy.com/blog/how-to-brew-tongkat-ali/)
- [Mucuna pruriens — Top Tropicals](https://toptropicals.com/catalog/uid/mucuna_pruriens.htm) · [How to make Nescafe from mucuna beans](https://toptropicals.com/gardenblog/1727960529.htm) · [Velvet bean — Tropical Plant Database](https://www.rain-tree.com/velvetbean.htm)
- [How to drink fenugreek seeds](https://biologyinsights.com/how-to-drink-fenugreek-seeds-water-tea-and-powder/) · [Methi water benefits](https://instacuppastore.com/blogs/main-page/methi-water-benefits-fenugreek-water-for-blood-sugar-hair)
- [Sarsaparilla — Tropical Plant Database](https://www.rain-tree.com/sarsaparilla.htm) · [Why saponins foam in root beer](https://sensemap.blog/why-quillaia-extract-in-root-beer)
- [Muira puama — Tropical Plant Database](https://rain-tree.com/muirapuama.htm) · [Muira puama uses and dosage](https://www.drugs.com/npp/muira-puama.html)
- [Horny goat weed — PeaceHealth](https://www.peacehealth.org/medical-topics/id/hn-4391000) · [Icariin and its derivatives](https://pmc.ncbi.nlm.nih.gov/articles/PMC4925704/)
- [Ginkgo biloba drug interactions and bleeding risk](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0321804) · [Ginkgo and warfarin in a VA population](https://pubmed.ncbi.nlm.nih.gov/26958257/)
- [Ashwagandha golden milk / ksheerapaka](https://openspicebox.com/recipes/ashwagandha-moon-milk) · [Withanolides — phytochemical profile](https://www.ayurvedhealing.com/ashwagandha-phytochemical-withanolides-alkaloids/)
- [Catuaba — shredded bark from Brazil](https://mayaherbs.com/ethnobotanicals/well-being/catuaba-trichilia-catigua-shredded-bark-from-brazil/) · [Catuaba](https://grokipedia.com/page/Catuaba)
- [Cold bloom vs hot bloom saffron](https://kashmiril.com/blogs/journal/cold-bloom-vs-hot-bloom-saffron) · [Why saffron threads are red but turn food golden](https://kashmiril.com/blogs/journal/why-saffron-threads-are-red-but-turn-food-golden) · [Saffron tea vs milk vs water](https://kashmiril.com/blogs/journal/saffron-tea-vs-milk-vs-water)
- [Korean red ginseng — history, preparation, composition](https://www.sciencedirect.com/science/article/pii/S1226845315000421) · [Ginseng tea (insam cha)](https://mykoreankitchen.com/ginseng-tea-insam-cha-in-korean/)
