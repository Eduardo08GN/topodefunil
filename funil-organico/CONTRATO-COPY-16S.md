# CONTRATO DE COPY 16s — v2 (2026-08-10)

> **Sete travas que toda copy de vídeo 16s tem de passar.** Elas moram em
> [`short_comum.lint_copy16`](short_comum.py) e são cobradas de fora por
> [`medir_copy16.py`](medir_copy16.py). Este arquivo diz **por quê** cada uma
> existe — o código diz **o quê**.

**Origem:** ordem do operador em 2026-08-10 — *"agentes troca16, ressurreicao16,
exterior16, flagrante16, pee16, escandalo16, colo16 precisam de reformulação
total de suas copys"* — depois de uma revisão adversarial de **6 lentes
independentes** (teste do polegar · Jon Benson · Stefan Georgi · ouvido nativo
americano · compreensão sentença a sentença · credibilidade/CTA/plataforma)
sobre três lotes renderizados. **127 achados, 79 derrubados na refutação, 48 de
pé.**

---

## ⛔ A descoberta que organiza tudo

A revisão não encontrou defeitos de estilo. Encontrou **sete defeitos
estruturais, cada um presente em quase todos os motores ao mesmo tempo.** Medido
antes da reforma, 200 sorteios por motor:

| | CT1 | CT2 | CT3 | CT4 | CT5 | CT6 | CT7 |
|---|---|---|---|---|---|---|---|
| troca16 | 100% | 78% | 55% | 100% | — | 95% | — |
| ressurreicao16 | 100% | 30% | 100% | 100% | 78% | 100% | — |
| exterior16 | 100% | 100% | 100% | 100% | — | 100% | — |
| flagrante16 | 100% | 17% | 95% | 100% | — | 100% | — |
| pee16 | 26% | 31% | 84% | 98% | — | 100% | 54% |
| escandalo16 | 100% | 94% | 100% | 100% | 100% | 100% | — |
| colo16 | 100% | 65% | 64% | 100% | — | 100% | 12% |

> **Defeito que aparece em sete motores não é erro de quem escreveu o pool — é
> ausência de contrato.**

E nenhum deles aparece relendo a lista de strings: todos vivem na
**combinação**. É por isso que o contrato é código, não parágrafo.

---

## A estrutura travada do vídeo

```
TAKE 1   gancho visual + A FALHA DELE, com dano concreto
TAKE 2   mecanismo COM RAZÃO → (prova curta) → follow → CTA        ← fim do vídeo
```

### ⭐⭐ A conta que faz caber

A cobertura social não cabe como batida própria em 25 palavras. Ela mora
**dentro da sentença do CTA**:

```
antes:  Comment gelatin, and I'll send the recipe.        (9 palavras)
depois: Comment gelatin, and the recipe goes to your messages.   (9 palavras)
```

Mesmo custo, e entrega de graça **(a)** o endereço da entrega, **(b)** a
privacidade e **(c)** o fato de que não é na tela pública.

Orçamento fechado, take 2, teto 25:

| batida | palavras |
|---|---|
| mecanismo com razão | 8 |
| prova curta | 5 |
| follow | 3 |
| CTA com cobertura | 9 |
| **total** | **25** |

---

## As sete travas

### CT1 — nada depois da sentença do CTA
O defeito mais caro do lote antigo: **100% dos sorteios em 6 de 7 motores.**

```
✗ ...Comment gelatin, and I'll send the recipe. The algorithm hides me from non-followers.
✗ ...Comment gelatin, and I'll send the recipe. Followers get answered first.
✗ ...Comment gelatin, and I'll send you the recipe. Follow me.
```

A última coisa no ouvido, colada no único pedido que gera receita, era uma
**expectativa negativa sobre a entrega**, uma **condicional na recompensa** ou
um **segundo CTA nu**. A posição final é a que fica; ela tem de ser o pedido.
⭐ **O follow continua existindo — ele vai ANTES.**

### CT2 — o take 1 enuncia a FALHA dele
Em dois dos três vídeos revisados não existia **uma sentença** dizendo o que o
corpo dele faz de errado. `never changes` não descreve nada — muda como, de quê
para quê?

Sem auto-reconhecimento não há comentário: ele não comenta porque a copy é boa,
comenta porque **se viu**. A melhor linha do lote inteiro é esta, e é a mais
simples:

```
He'd lose it ten minutes in.
```

Cinco palavras, um número, um dano concreto.

⚠️ **AVISO, não ERRO** — há ângulos cuja cena 1 é aviso de excesso, não falha
(o GOOD 16). Quem não enuncia falha tem de saber que não enuncia.

### CT3 — `gelatin trick` carrega razão na mesma sentença
Nome de mecanismo sem razão ao lado não vira crença: vira ruído de marca.

```
✗ The gelatin trick is the half that works.
✗ The gelatin trick: pomegranate and collagen.
✓ The gelatin trick puts back what holds the blood in.
```

A sentença precisa de **verbo de efeito** + **alvo** (o órgão, o sangue, o
corpo). A lista de verbos é generosa e para crescer — o que se proíbe é o
rótulo **nu**.

### CT4 — um apelido do órgão por vídeo
⛔⛔ **Isto reverte a regra anterior, e a reversão é declarada.** Vários motores
*exigiam* substantivos diferentes entre as cenas (*"duas menções iguais em 16
segundos são bordão"*), e o resultado medido foi o apelido mudando no corte em
**98-100% dos vídeos**.

Em 24s e cinco cenas o bordão é o risco. Em 16s e duas cenas o risco é o
oposto: **o corte zera a memória de trabalho**, e trocar `soldier` por `Johnson`
no segundo 9 obriga o espectador a remapear justamente quando ele já está com um
pé fora. A variação continua existindo **entre** vídeos, que é onde ela nunca
custou nada.

### CT5 — nenhum ingrediente nomeado na fala
```
✗ The gelatin trick: pomegranate and collagen.
```
A receita é a **única** moeda que o comentário compra. E o dano não é de um
vídeo: entregue uma vez na página, ela está gasta para os **outros 49** que
pedem a mesma palavra pela mesma receita.

### CT6 — o CTA diz onde a receita chega
O KPI é uma **confissão pública**: o comentário leva nome e foto e vai para o
feed da esposa dele. A keyword `gelatin` existe para dar negabilidade — mas
quanto melhor o diagnóstico em 2ª pessoa, **mais caro fica comentar**.

Em 48 segundos de copy dos três vídeos revisados não havia **uma palavra**
baixando esse custo. A cláusula é grátis (ver a conta acima) e não é opcional.

### CT4b — os três apelidos, e só eles
> Ordem do operador, 2026-08-10: *"quero que vc use weiner e john-son pra se
> referir ao órgão tb, não apenas pec-ker"*

```
pecker  ·  wiener  ·  Johnson
```

⛔ O **CT4 sozinho é uma armadilha**: ele trava um apelido por vídeo, e um
apelido por vídeo pode ser o **mesmo apelido no lote inteiro** — mode-collapse
com cara de consistência. O CT4b é onde a variação **entre** vídeos é cobrada, e
o `medir_copy16` tem uma coluna só para a repartição real.

⚠️ `soldier` saiu: soa **filme de guerra** para ouvido americano (lente de ouvido
nativo da revisão adversarial). `tool` saiu por ambiguidade em gíria dos EUA. Os
dois **continuam no `NUCLEO`** de cada motor porque as lentes os usam para
*detectar* o órgão — o que muda é que não são mais **sorteáveis**.

### CT8 — nenhum pedido de follow na fala
> Ordem do operador, 2026-08-10: *"eu tb não acho que deva ter que ter follow me
> no cta, **a mensagem é enviada independente de seguirem ou não**"*

⛔⛔ **Isto reverte doutrina antiga, e a reversão é de FATO, não de gosto.** O
gate de follow existia no repo inteiro porque se acreditava que a automação de
DM só alcançava seguidor. Quem opera a automação corrigiu a premissa.

Toda a família `GATES` / `FOLLOWS16` / `GATES16` nasceu dessa premissa errada —
são 6 a 14 entradas por motor, ocupando **2 a 5 palavras** num take de 25, de
copy que nunca deveria ter existido.

⭐ **E o CT1 nasceu justamente porque esse beat vivia depois do CTA.** Com o
follow fora, o defeito mais caro do lote (100% dos sorteios em 6 de 7 motores)
deixa de ter de onde vir. As palavras liberadas vão para o mecanismo e a prova.

⚠️ Os pools ficaram no arquivo, **marcados como aposentados**, porque os
autotestes ainda os validam e apagá-los exigiria duas cirurgias no mesmo commit
em que a copy inteira mudou. Cada um leva no cabeçalho o aviso de que **melhorar
suas entradas não muda um único vídeo**. Se o follow voltar, volta **antes** do
CTA e por decisão do operador.

⚠️ **Consequência medida:** o piso da cena 2 do TROCA 16 batia em 130 de 400
sorteios depois da remoção. Piso calibrado com um beat que não existe mais é
alarme que sempre dispara — e alarme que sempre dispara ensina a ignorar o
linter inteiro. Recalibrado de 20 para 18.

### CT7 — verbo de ereção colado no órgão
```
✗ The gelatin trick gets your pecker hard.       ← reprova no gerador
✓ This leaves your body harder than in decades.  ← passa
```

⚠️ **A lição paga no COLO 16 (~95% de recusa) não é sobre a palavra — é sobre a
palavra COLADA NO ÓRGÃO.** A primeira versão desta trava proibia o token em
qualquer lugar e acusou o GOOD 16 em 87% dos sorteios, em cima da copy da fonte
que converte. Sobre o **corpo** passa; sobre o **órgão** não.

⭐ No take 1 dos ângulos de **isca absurda** (TROCA, EXTERIOR, COLO) o verbo é
permitido: ali a promessa é justamente a que vai ser desmentida meio segundo
depois, e proibi-la mataria o ângulo.

---

## O que NÃO virou trava, e por quê

| achado | por que ficou de fora |
|---|---|
| **O loop planta concorrente da keyword** — o Reels repete e o áudio do take 1 (`baking soda`, `cucumber`) toca enquanto ele digita | Achado do crítico de completude, **não verificado em campo**. E a substância absurda é o hook de três ângulos: proibi-la no take 1 mataria o que faz o vídeo parar o polegar. Fica como **aviso de doutrina**. |
| **Teto real de 19-21 palavras** (140-155 wpm) | O teto de 25 vem de **render**, não de teoria — 32 cortou e 28 cortou, 25 não. Baixar para 21 custaria batidas que o contrato exige. ⚠️ Mas a tensão é real: **se a keyword é a última coisa e o take estoura, ela é a primeira a ser cortada.** |
| **Endereçar a esposa** (metade da audiência é feminina e comenta de graça) | É **cena e copy nova**, alçada do operador. Registrado aqui: 5 palavras (`If he won't ask, you ask.`) abrem a metade barata da audiência. |
| **A keyword só existe como fonema** — sem texto em tela, e `gelatin` volta escrito como *jello, jelly, gelatine* | Conserto de **infraestrutura** (overlay do AdBatch + cluster de variantes na automação), não de copy. |

---

## Como rodar

```bash
python funil-organico/medir_copy16.py
```

```bash
python funil-organico/medir_copy16.py --motor colo16 --exemplos 3
```

```bash
python funil-organico/medir_copy16.py --gate
```

⚠️ **Motor 16s novo entra na lista `MOTORES` no mesmo commit em que nasce** —
junto com as listas do `medir_teto_fala`, `medir_deiticos`,
`medir_contexto_copy`, `medir_abertura` e `medir_alcance`. Motor que não está na
lista não é medido, e "sem achado" nele significa *ninguém olhou*.

## Conexões

- [`licoes-de-construcao.md`](licoes-de-construcao.md) — os modos de falha do assistente
- [`RUNBOOK-app-offline.md`](RUNBOOK-app-offline.md) — motor → app → `.exe`
- [`licoes-producao-veo.md`](licoes-producao-veo.md) — as lições pagas em render

---

## ⚠️ A exceção declarada: o MODO BELA do NECROSE 16

Em **todo o resto do parque** o MODO BELA troca a **mulher que já existe na
cena** por uma do pool bela. No `necrose16` ele faz outra coisa, por ordem do
operador (2026-08-10):

> *"quando ativado, o REF passa a ser uma mulher linda no **primeiro take**; o
> segundo take continua do jeito que está. Apenas excepcionalmente o modo bela é
> levemente diferente para o caso do necrose16 — quando eu pedir pra implementar
> modo bela em outros agentes, continua conforme o sempre combinado."*

⛔ **Quem for implementar MODO BELA em outro agente não deve copiar isso.**

O ângulo comporta a troca porque as duas funções são separadas — **ela
apresenta, ele prova**:

| | |
|---|---|
| a copy do take 1 | toda **condicional em 2ª pessoa** e imperativa — zero primeira pessoa masculina, então cabe na boca dela sem reescrever uma linha |
| a copy do take 2 | é a que carrega `This is my {o} now`, e o take 2 **não muda** |
| o `BLOCO 0 (REF)` | continua sendo **ele** — a AdBatch Vertical 2 recebe **uma** foto de referência, e ela ancora quem precisa de consistência facial. Ela entra por descrição, como todo personagem secundário do repo |

A lente `NE-BELA` cobra os **dois** estados: com a trava ligada, a mulher chega
à `IMAGE 01/02` **e** o homem continua na `IMAGE 02/02`; com ela desligada,
nenhuma mulher aparece na primeira.
