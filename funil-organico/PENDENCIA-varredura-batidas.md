# ⏳ PENDÊNCIA — varrer a família 16s com as duas lentes novas

> Aberta em **2026-08-10**, por ordem do operador: *"documente essa pendência
> num md e commite no repo. Faremos num momento oportuno."*
>
> ⛔ **Isto não é uma lista de defeitos. É uma lista de CANDIDATOS**, com a
> medição preliminar já feita e com o que ela tem de falso positivo escrito
> junto. Ler a seção 4 antes de sair corrigindo.

---

## 1. De onde ela vem

Em 2026-08-10 o operador achou **cinco defeitos** lendo renders e copy no app,
e nenhuma das lentes do repo pegava nenhum deles. Os cinco são a **mesma
família**:

| o que ele achou | onde | por que nenhuma lente via |
|---|---|---|
| caixa de papelão dentro da jacuzzi | `fight16` | nenhuma lente cruza **objeto** com **lugar** |
| falsa causa sem `NOT` | `fight16` | cada batida certa sozinha; o **par** errado |
| etnia declarada × tom de pele | `fight16` | duas autoridades para o mesmo atributo |
| `got hold of me` — agarrou **como?** | `alfa16` | linter cobrava **forma**, não **função** |
| `Your wife` em vez de `My wife` | `alfa16` | a pessoa gramatical **entre** batidas |

> **A causa raiz é uma só: as lentes olham a batida, e o defeito mora na
> RELAÇÃO entre batidas.** Frase por frase, tudo passa.

Dois controles nasceram disso, hoje, **e vivem só no `alfa16_short.py`**:

- **PREDICADO VAZIO** (o teste WTF em código) — lista curta de predicados que
  não dizem nada: `did something`, `got hold of`, `it worked`, `did the trick`,
  `made a difference`, `took care of it`, `blew my mind`…
- **PESSOA POR TAKE** — o take 1 é **depoimento** (`my wife`), o take 2 é
  **oferta** (`your {o}`, `Comment gelatin`). O paradoxo não fala com o
  espectador; o mecanismo e a cozinha não falam em 1ª pessoa.

**A pendência é levar as duas ao resto da família.**

---

## 2. ⚠️ O que a medição preliminar já disse — e ela encolheu a pendência

Rodei as duas varreduras nos **18 motores de 16s**, 120 sorteios cada, antes de
escrever este arquivo. **O resultado é bem menor do que eu tinha estimado ao
propor a varredura**, e fica registrado assim de propósito.

### 2a. Predicado vazio — **nenhum caso real**

A varredura crua acusou `botica16` (6/240) e `fight16` (21/240). **Os dois são
falso positivo**, e pelo mesmo motivo: o padrão `things changed` casa com

```
But things changed when I discovered the gelatin trick.
```

que é a **copy verbatim do operador** no `fight16` — e ali ela não é vaga
coisa nenhuma, porque a sentença **anterior** já disse o que não funcionava.
Vagueza é propriedade da **sentença dentro do seu contexto**, não do token.

⛔ Corolário para quem for executar: **tirar `things changed` da lista, ou
aceitar que ele exige leitura humana.** Lente que reprova a copy aprovada pelo
operador é a §16 das lições, e treina ele a ignorar o relatório.

### 2b. Zigue-zague de pessoa — **um motor, e é o `ressurreicao16`**

| motor | take 1 com padrão `2→1→2` |
|---|---|
| **`ressurreicao16`** | **12%** |
| os outros 17 | **0%** |

O caso, com a sequência de pessoas de cada sentença entre colchetes:

```
[1 2 1 -]  Sixty-one, and my man quit on me in bed.  Sound like your Johnson?
           Then my aunt handed over her recipe.  My husband needed something else.
```

⚠️ **E aqui é onde o julgamento entra, não o regex.** `Sound like your Johnson?`
é uma **pergunta de identificação** cravada no meio do depoimento — pode ser
exatamente o beat que faz o vídeo funcionar, e não um defeito. É a mesma
natureza do `AVISO` do `alfa16`, que também é 2ª pessoa no meio de um take em
1ª — só que lá ele está na **abertura**, onde o gancho tem de estar.

**A pergunta a levar ao operador é essa, e é dele:** a pergunta de
identificação fica onde está, ou vai para a abertura como no `alfa16`?

### 2c. A forma de referência

O `alfa16` fecha em `2 1 1` — gancho em 2ª pessoa, depoimento em 1ª, e o take 2
inteiro em 2ª. É o desenho que o operador aprovou ouvindo, e serve de régua
para comparar os outros.

---

## 3. Como executar, quando for a hora

1. **Portar os dois controles** do `alfa16_short.py` para `short_comum.py`,
   como funções que cada motor chama do seu `autoteste` — hoje eles são código
   local, e código local não se propaga.
   ⛔ Portar **sem** a lista de tokens fixa: cada ângulo declara a sua, porque
   `things changed` é vazio num motor e é a copy do operador em outro.
2. **Rodar motor a motor**, não em lote — o veredito de cada frase é humano.
3. **Levar ao operador** só o que sobreviver à leitura. Copy é alçada dele
   (`CLAUDE.md` §REGRA DE ALÇADA): sugerir sim, trocar não.
4. Onde ele aprovar a troca, **o guarda entra na lista**, nunca no sorteio —
   foi assim que o `NOT` do `fight16` e a pessoa do `alfa16` ficaram seguros
   por construção.

---

## 4. ⛔ O que NÃO fazer

- **Não** rodar uma varredura em lote e "consertar" o que ela acusar. As duas
  varreduras desta pendência já produziram **mais falso positivo do que
  achado**, e isso está medido acima.
- **Não** copiar a lista de predicados vazios do `alfa16` como se fosse
  universal. Ela é do ângulo.
- **Não** mexer em copy aprovada pelo operador para satisfazer uma lente. O
  repo já cometeu o inverso disso quatro vezes com o `medir_personagens.py` —
  otimizar a métrica **contra** o objetivo.

---

## Conexões

- [`funil-organico/alfa16_short.py`](alfa16_short.py) — os dois controles, no
  `autoteste`, com o motivo de cada um escrito
- [`funil-organico/CONTRATO-COPY-16S.md`](CONTRATO-COPY-16S.md) — as travas que
  já são cobradas de fora
- [`funil-organico/licoes-de-construcao.md`](licoes-de-construcao.md) — §16
  (lente que reprova o que está certo) e §17 (trocar uma abstração por outra)
- `CLAUDE.md` §REGRA DE ALÇADA — copy e cena são do operador
