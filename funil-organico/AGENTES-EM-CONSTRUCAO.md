# Agentes SHORT em construção — retomada

> Estado em 2026-08-05. Este arquivo existe para que a construção continue
> **sem depender da memória de uma sessão**. Tudo que já foi decidido está aqui;
> nada precisa ser reperguntado ao operador.

## ⛔ A regra que mandou refazer tudo

Ordem do operador: *"comece do zero todos os agentes onde vc não respeitou o
pipeline de build e pulou a etapa de leitura ótica do vídeo fonte"*.

⚠️ **A flag `--detail transcript` do `/watch` PULA OS FRAMES.** Usá-la para
economizar contexto transforma a etapa [2] do
[`PIPELINE-NOVO-AGENTE.md`](../PIPELINE-NOVO-AGENTE.md) — *"LEITURA ÓTICA: ver,
não resumir"* — em leitura de legenda. O preço foi medido: descrevi o bit visual
do reel 893 como "efervescência" quando o bit real é **o corpo cavernoso da peça
anatômica indo de murcho para ereto** (o mecanismo do RESSURREICAO). O agente
inteiro teria nascido sobre o bit errado.

**O comando certo**, que força a progressão real:

```bash
python C:/Users/edlut/.claude/skills/watch/scripts/watch.py "<url>" \
  --detail token-burner --no-dedup --fps 1 --out-dir "<dir>"
```

E depois **abrir todos os frames**, não uma amostra.

---

## 1. Agente da PLACA (reel 1325916592470208) — sem código

**Leitura ótica: INCOMPLETA.** 40 frames capturados, 4 lidos. Refazer.

**Transcrição da fonte** (33s):

```
[00:00] Having a small and disgusting banana, and that's exactly why men over 50
        need this trick before it's too late.
[00:05] Mix a tablespoon of beef bone broth powder with a teaspoon of raw honey
        and the juice of half a lemon into a cup of warm water.
[00:13] Drink it first thing in the morning before food.
[00:16] The collagen in the broth rebuilds what your body stopped producing,
        and the blood flow comes back with it.
[00:22] If you want my complete protocol... comment book...
```

**Visual lido nos 4 frames que abri:** REF loira de óculos, top verde, luva de
látex na mão, apontando para uma **banana podre** na virilha de um homem de
camisa levantada, com uma **placa escrita à mão** "SMALL BANANA ☹". Cena 2 é a
receita na bancada com potes rotulados. Cena 3 ela segura um livro.

**Decisões do operador (entrevista fechada):**

| eixo | decisão |
|---|---|
| take 1 | fiel à fonte, terminando em `before it's too late`, com `gelatin trick` no lugar de `this trick` |
| placa escrita à mão | **entra como eixo sorteável** — pool de placas |
| prop | **par vergonha/payoff**: murcho no take 1, geoduck grande e ereto no take 3 |
| take 3 | a narradora **é** a mulher do casal, sentada com o marido; um homem a mais atrás, mudo e espantado |
| cenário | doméstico regional — **sem** jaleco, luva, diplomas ou consultório |
| etnia | por **região dos EUA** (redneck apalache, Texas, Louisiana/cajun...) |

⛔ **Conflito técnico a resolver antes de escrever:** todo take carrega o literal
travado `No on-screen text, no subtitles, no captions, no watermark`, cobrado
pelo `lint_sem_texto` do `short_comum.py`. Uma placa física em cena contradiz
isso — e contradição entre IMAGE e TAKE é pior que omissão, porque o Veo resolve
mexendo no que estava certo. **A saída acordada:** neste motor a cauda vira
`No burned-in text, no subtitles, no captions, no watermark` — preserva a
intenção (impedir legenda queimada) sem proibir um prop que tem letra.

---

## 2. Agente do MODELO ANATÔMICO (reel 893070330083605) — sem código

**Leitura ótica: PARCIAL.** Só o hook (0-12s), 3 frames lidos de 23.
Falta todo o resto, e sobretudo confirmar o morph quadro a quadro.

**Transcrição da fonte** (44s):

```
[00:00] Watch what happens when I add baking soda to this Johnson.
[00:03] Squeeze the juice of one full lime, add one teaspoon of baking soda
        and watch it fizz.
[00:09] Add a pinch of salt and two tablespoons of apple cider vinegar.
[00:13] Drink this every morning for four days.
[00:15] Your prostate swelling goes down, your urine flow gets stronger,
        those late night bathroom trips stop...
[00:34] ...comment book and I will send you my bedroom protocol.
```

⭐⭐ **O BIT VISUAL, confirmado nos frames t=02 e t=04:** ela segura um **modelo
anatômico em corte** do assoalho pélvico masculino numa mão e a caixa de
bicarbonato na outra, e **a haste do modelo passa de pendida para angulada para
cima** — o corpo cavernoso vai de murcho a ereto enquanto ela despeja. É o
mecanismo do RESSURREICAO numa peça anatômica.

**Decisões do operador (entrevista fechada):**

| eixo | decisão |
|---|---|
| take 1 | fiel até `to this Johnson` |
| o bit | o **morph do corpo cavernoso** durante o despejo — não efervescência |
| ângulo | **próstata como porta, ED como destino** — adaptar minimamente para ereção |
| modelo | ela **SEGURA na mão** e derrama nele (o NECROSE tem modelos parados em pedestal — é o que separa os dois) |
| take 3 | duas mulheres jovens, uma segurando o geoduck ereto |
| etnia | por região dos EUA |
| payoff repetido | operador ciente e **aceita o custo** de motores separados |

---

## 3. As 8 cenas que ainda cortam fala

Piso do pool acima de 25 palavras — **nenhum sorteio resolve**, é cirurgia de
copy. Ordem permanente: *"não pode haver cortes de fala"*.

| motor | cena | piso |
|---|---|---|
| `exterior` | 3 | 32 |
| `vazamento` | 2 | 29 |
| `receita` | 1 | 28 |
| `vazamento` | 3 | 28 |
| `receita` | 2 | 27 |
| `colo` | 2 | 27 |
| `escandalo` | 2 | 26 |
| `ressurreicao` | 2 | 26 |

⚠️ **Antes de tocar em qualquer uma:** rodar
`python funil-organico/medir_teto_fala.py --curva --motor <nome>` e **imprimir a
fala mínima decomposta em beats**, com o custo em palavras de cada um. O corte
sai de enchimento e do que a imagem já mostra — **nunca do referente**.

⛔ **Três armadilhas já pagas:**
1. `exterior` c2 a 25 levanta `IndexError` em 600 de 600 sorteios.
2. `colo` c3 e `botica` c3 **pioraram** quando baixei o teto — o `or pool` do
   `_cabem` devolve o pool inteiro quando nada cabe.
3. Baixar o teto sem consertar a cadeia de sorteio **arma a bomba** em vez de
   desarmá-la.

---

## O que já está pronto

15 motores no ar, 15 `.exe` atualizados e verificados abrindo. Gates de
drifting, personagens e contexto de copy limpos. Corte de fala: de 28 cenas
para 11.

O **DUPLA** (reel 1138675695123216) foi o único construído com leitura ótica
completa e serve de referência para os dois que faltam — sobretudo pelas **seis
lentes herdadas que tiveram de ser reescritas** porque codificavam a doutrina do
BOTICA e reprovavam 100% da produção do ângulo novo. Copiar um motor traz o
linter do motor copiado junto: conferir lente por lente é parte do trabalho, não
um extra.

## Conexões

- [`../PIPELINE-NOVO-AGENTE.md`](../PIPELINE-NOVO-AGENTE.md) — as 8 etapas
- [`licoes-de-construcao.md`](licoes-de-construcao.md) — §28 (o teto vem de
  render, não de conta), §24 (contar as partes do molde), §16 (aceite é medição)
- [`RUNBOOK-app-offline.md`](RUNBOOK-app-offline.md) — motor → app → `.exe`
