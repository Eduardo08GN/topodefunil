---
name: page-facebook
version: "1.0.0"
description: Gera o kit completo de preenchimento de uma pagina de Facebook para o funil organico de nutra US (nicho ED ou weight loss). Entrega nomes, bio, categoria, setup de mercado US, prompts de imagem para banner e avatar, primeiros posts e guardrails de claim. Pergunta o nicho antes de cuspir os dados.
argument-hint: "[ed|weightloss] [tema opcional]"
allowed-tools: AskUserQuestion, Read, Write
user-invocable: true
---

# /page-facebook — Kit de preenchimento de pagina

Gera tudo que preenche uma pagina virgem do Facebook para rodar video-criativo
no funil organico de nutra US. Uma invocacao = uma pagina pronta pra preencher.

Contexto da operacao vive em [operacao-contas-paginas.md](../../../funil-organico/operacao-contas-paginas.md)
e o swipe de concorrentes em [paginas-referencia.md](../../../funil-organico/paginas-referencia.md).

---

## REGRA DE ENTRADA — perguntar o nicho ANTES

Nunca cuspir dados sem saber o nicho. Primeira acao da skill:

> **AskUserQuestion:** "Qual o nicho desta pagina?"
> - **ED / vitalidade masculina** — homens 45+, circulacao, energia, performance
> - **Weight loss / metabolismo** — 40+, metabolismo, habitos, saciedade
>
> Segunda pergunta (mesma chamada, multiSelect false): **"Quantas paginas gerar agora?"** (1 / 3 / 5)

Se o usuario ja passou o nicho no argumento (`/page-facebook ed`), pular a pergunta
e ir direto. Se passou tema (`/page-facebook ed cozinha`), usar como eixo criativo.

Gerar **5 paginas de uma vez** e o default operacional (o ciclo de viralizacao exige
volume: uma pega, outra fica pra tras). Cada pagina sai com identidade DIFERENTE —
nunca 5 variacoes do mesmo nome.

---

## O QUE A SKILL ENTREGA (por pagina)

### 1. Identidade

- **Nome da pagina** — marca tematica em ingles US natural. 1 escolhido + 3 alternativas.
- **Username** (`facebook.com/nome`) — minusculo, sem numero aleatorio.
- **Eixo criativo** — a angulacao que separa esta pagina das outras 4 do lote.

**Nome tem que ter IMAGEM, nao descricao.** `Men's Circulation Daily` descreve e
esquece. `The Quiet Engine` cria imagem e gruda. O nome descritivo e o default
preguicoso: usar so como alternativa, nunca como primario.

Fontes de nome que geram imagem:
- **Metafora do corpo/maquina:** The Quiet Engine · Full Circuit · The Furnace Room
- **Americana / oficio:** The Root Cellar · The Morning Forge · Copper Kettle Notes
- **Idiom coloquial:** Second Wind Society · The Long Way Back · Still Running
- **Recorte de tempo:** The Slow Hour · First Light Habits · The 5AM Table
- **Ingrediente como marca:** The Beet Report · Ginger & Iron

| Nicho | Primarios com imagem | Descritivos (so alternativa) |
|---|---|---|
| ED / vitalidade | `The Quiet Engine` · `The Root Cellar` · `Second Wind Society` · `The Morning Forge` · `The Slow Hour` | `Men's Circulation Daily` · `After 40 Vitality Notes` |
| Weight loss | `The Lean Hour` · `Slow Burn Kitchen` · `The Empty Plate` · `Back to Fighting Weight` | `Simple Metabolism Tips` · `Metabolism After 40` |

Regras duras de nome:
- Sem `Dr.` / `Dra.` / `MD` / `Clinic` / `Rx` — sinal medico que o Meta cata.
- Sem nome proprio de pessoa (nao e persona-centered).
- Sem promessa no nome (`CureED`, `FatBurn Fast`) — nome e tema, promessa e conteudo.
- Ingles US natural, 2 a 4 palavras. Le em voz alta: se soa a traducao, refaz.
- **Teste do bar:** se voce nao consegue dizer o nome pra um amigo e ele repetir de
  memoria 10 minutos depois, o nome e fraco. Refaz.

> **Tradeoff a declarar sempre:** nome com imagem gruda mas nao diz o tema. Quem
> carrega o tema e a bio e a descricao. Entregar sempre 1 descritivo entre as
> alternativas, pra o operador escolher se prefere memorabilidade ou clareza.

### 2. Bio / descricao

Estrutura de 3 linhas (o que as paginas de referencia fazem e converte):

```
<linha 1: para quem e + tema>
<linha 2: o que a pagina entrega>
<linha 3: CTA + link>
```

Exemplo (ED):
```
Natural vitality tips for men over 45.
Simple food, movement and daily habit ideas you can try at home.
More tips below
<link>
```

Regras de bio:
- Sem claim de doenca, cura ou substituicao de tratamento (ver guardrails).
- Sem `#erectiledysfunction` / `#cured` na bio — crava o nicho pro classificador.
  Hashtag de nicho, se usar, vai no post, nao na bio.
- Link: encurtador proprio. Um por pagina, nunca o mesmo em 5 paginas.

### 2b. Descricao (campo About) — NAO confundir com a bio

Bio e a linha curta sob o nome. **Descricao e o campo About**, texto longo que
aparece na aba Sobre. Toda pagina precisa dos DOIS. Entregar sempre os dois.

Estrutura da descricao (4 blocos, 400 a 600 caracteres):

```
<1: o que a pagina e, em 1 frase>
<2: pra quem e, com o recorte de idade/momento>
<3: o que a pessoa encontra aqui, concreto (3 tipos de conteudo)>
<4: disclaimer>
```

Exemplo (ED):
```
The Quiet Engine is a place for men who want to understand how their body
actually works after 45.

Everything here starts with circulation: what supports it, what gets in the way,
and the small daily choices that add up over time.

You will find short kitchen videos, simple movement you can do in two minutes,
and plain explanations of the things most men were never told.

Not medical advice. Talk to your doctor before changing anything.
```

Regras de descricao:
- Escrita em 3a pessoa pro nome da marca, nunca "I" (nao ha pessoa por tras).
- Zero credencial, zero anos de experiencia, zero "as seen on".
- O disclaimer fecha SEMPRE. E o que muda o enquadramento da pagina inteira.

### 3. Categoria e setup

- **Categoria sugerida:** `Blogger` ou `Health & Wellness Website` — pagina de dicas
  e literalmente um blog, entao `Blogger` e verdadeiro, nao disfarce.
- **Nao sugerir** categoria de culinaria/receita para pagina que linka suplemento:
  o descasamento entre o que a pagina diz ser e o que ela vende e o que puxa revisao.
- **Mercado/localidade:** Estados Unidos. Cidade sugerida por pagina (variar entre as 5:
  Austin TX · Tampa FL · Charlotte NC · Phoenix AZ · Nashville TN). Cidade e sinal de
  mercado da marca, nao alegacao de residencia de uma pessoa.
- **Idioma:** English (US).
- **Botao de CTA:** `Learn more` apontando pro link.

### 4. Prompts de imagem

Dois prompts prontos por pagina, em ingles, para o gerador de imagem.

**Avatar (quadrado, 1:1)** — marca/simbolo/lifestyle, NAO retrato de pessoa
inventada com identidade. Padroes que funcionam:
- Bodegon de ingrediente central (raiz de beterraba, gengibre, melancia) em fundo limpo
- Simbolo grafico simples (folha + circulo, seta ascendente organica)
- Cena de cozinha/bancada em close, sem rosto

Template de prompt de avatar:
```
Square brand avatar for a natural wellness tips page. <objeto central>,
top-down on a <superficie> surface, soft natural window light, shallow depth of field,
warm earthy palette (<cores>), clean minimal composition, no text, no faces,
photorealistic, high detail.
```

**Banner (capa, 1640x624)** — cena ampla, respiro no centro-esquerda pro texto.

Template de prompt de banner:
```
Facebook cover photo, 1640x624, for a natural wellness tips page about <tema>.
Wide horizontal composition: <cena> on the right third, generous clean negative space
on the left for text overlay. Soft morning light, warm earthy palette (<cores>),
photorealistic lifestyle photography, shallow depth of field, no text, no logos, no faces.
```

Regras de imagem:
- **Sem rosto de pessoa fabricada** como identidade da pagina (avatar/banner).
  Mao, silhueta, corpo parcial e cena sao livres — o que nao entra e um individuo
  nomeado com biografia inventada posando de autor real.
- Sem jaleco, estetoscopio, cruz medica, consultorio — sinal de credencial clinica falsa.
- Sem antes/depois de corpo, sem circulo vermelho em parte do corpo.
- Sem bandeira US forcada no avatar (padrao batido do nicho, ja queimado).

### 5. Primeiros posts (semeadura)

5 angulos de conteudo pra pagina nao nascer vazia. Formato de cada:
`<gancho de 6 palavras> | <ideia do video> | <CTA de comentario>`

Cadencia (de [operacao-contas-paginas.md](../../../funil-organico/operacao-contas-paginas.md)):
- Aquecimento: 1 post/dia por 3 dias
- Depois: ate 3/dia, **maximo 3**
- Consistencia diaria pesa mais que volume

### 5b. Prompts Veo 3 (o video de estreia de cada pagina)

Estrutura vem de [diretrizes-script-32s.md](../../../funil-organico/diretrizes-script-32s.md)
e vale aqui inteira: **4 clipes de 8s = 32s**, teto do Veo por clipe, e o mapa
neurologico. O que muda nestas paginas e o CONTEUDO, nao a estrutura.

| Clipe | Cerebro | Funcao |
|---|---|---|
| 1 (0–8s) | Reptiliano | cold open visual + hook que pressupoe conversa |
| 2 (8–16s) | Limbico | ele se ve + negacao da causa falsa |
| 3 (16–24s) | Cortex | UM tease de mecanismo + prova concreta |
| 4 (24–32s) | Reptiliano | projecao curta + CTA de comentario |

**Orcamento de fala: 10 a 16 palavras por clipe.** Contar antes de aprovar.
**Orcamento de mecanismo: UM tease, ZERO explicacao.** Se entregar completo,
o cara vai no Google e nao na DM.

**Divergencia deliberada da doutrina de persona:** a doutrina agressiva (biquini
em quadro, frame 1 com corpo/casal, tom de porno soft) foi escrita pra pagina de
persona-expert. Estas paginas sao marca tematica de dicas. Bio dizendo "simple
kitchen recipes" com video de pitch sexual e o descasamento que puxa revisao de
conteudo. Aqui o scroll-stop vem de **prop e movimento** (corte, fervura, vapor,
mao trabalhando), nao de corpo. Mantem a estrutura e o loop, troca a alavanca.

**Template de prompt Veo 3 por clipe:**

```
[8s, vertical 9:16] <tipo de plano> of <sujeito/objeto> <acao concreta> in <cenario US>.
<luz e atmosfera>. <movimento de camera>. Handheld realism, natural imperfection.
Audio: ambient <som do ambiente>.
Dialogue (male voice, <idade>, <sotaque US>, conversational, unpolished):
"<fala de 10 a 16 palavras>"
Style: photorealistic UGC, shot on phone, no captions, no text overlay.
```

Regras duras do prompt Veo (herdadas do repo):
- **Sem hifen nem travessao** em nenhuma fala. Marcador nº1 de IA.
- **UMA figura por linha.** Empilhar figura vira bingo de copy.
- Fala imperfeita: contracao, recomeco, "honestly", frase que desaba no casual.
- Cenario sempre casa americana real (cozinha, garagem, varanda), nunca estudio.
- `no text overlay` no prompt: legenda entra na edicao, nao no Veo (o Veo erra texto).
- Clipes 3 e 4 sao corpo reciclavel: 1 corpo × N hooks. So 1 e 2 mudam na leva.

### 6. Guardrails de claim (INVIOLAVEL)

O que a skill **nunca** escreve em nome/bio/post — vale pros dois nichos:

| Proibido | Por que | Troca por |
|---|---|---|
| `cures`, `treats`, `reverses`, `fixes ED` | claim de doenca = FTC + strike de saude no Meta | `supports`, `may help`, `part of a routine` |
| `nature's viagra`, `no more blue pills` | comparacao com farmaco de prescricao | `natural daily habits` |
| `replaces your medication` | induz parar tratamento real | `talk to your doctor before changing anything` |
| `guaranteed`, `in 7 days`, `works for everyone` | promessa de resultado | `some people notice`, `results vary` |
| depoimento inventado em 1a pessoa | testemunho falso | conteudo de dica, sem testemunho |
| `Dr.` / credencial nao possuida | credencial falsa | sem credencial |

**Nota de ED especificamente:** disfuncao eretil e com frequencia o primeiro sinal
visivel de problema cardiovascular ou diabetes. Copy que promete resolver com receita
caseira faz o cara adiar o cardiologista. Alem do risco pra ele, e o perfil exato de
claim que a FTC processa e que o Meta derruba. Toda pagina do nicho sai com uma linha
de rodape do tipo `Not medical advice. Talk to your doctor.` — custa nada e muda o
enquadramento da pagina inteira aos olhos do classificador.

---

## LIMITES DA SKILL

Duas coisas que esta skill nao gera, de proposito:

1. **Identidade humana fabricada** — nome americano inventado + rosto de IA + cidade de
   residencia + historia pessoal, apresentado como o autor real da pagina. Alem de ser
   mentira sobre quem fala, e o unico elemento que mata a pagina inteira quando cai
   (e o argumento que os proprios operadores da call usam pra nao fixar persona).
   A skill entrega marca tematica, que e o que o operador pediu e o que sobrevive.

2. **Disfarce de categoria** — escolher categoria falsa (culinaria/receita) pra escapar
   da revisao de conteudo de saude. A skill sugere categoria verdadeira. Se o operador
   quiser mudar depois, e decisao dele, mas nao sai automatizado daqui.

---

## FORMATO DA SAIDA

Para cada pagina, entregar em bloco copiavel:

```
━━━ PAGINA <n> — <NOME> ━━━
Nome:        <nome com imagem>
Alternativas: <2 com imagem + 1 descritivo>
Username:    facebook.com/<username>
Eixo:        <angulacao criativa desta pagina>
Categoria:   <categoria>
Mercado:     <cidade>, <estado>, United States · English (US)
Botao CTA:   Learn more → <link>

BIO (linha curta sob o nome)
<3 linhas>

DESCRICAO (campo About)
<4 blocos, 400 a 600 caracteres>

PROMPT AVATAR (1:1)
<prompt>

PROMPT BANNER (1640x624)
<prompt>

PRIMEIROS 5 POSTS
1. <gancho> | <ideia> | <CTA>
...

VEO 3 — VIDEO DE ESTREIA (4 clipes de 8s)
CLIPE 1 <prompt completo>
CLIPE 2 <prompt completo>
CLIPE 3 <prompt completo>
CLIPE 4 <prompt completo>

RODAPE PADRAO
Not medical advice. Talk to your doctor.
```

Ao fim do lote, lembrar o operador:
- Maximo 5 paginas por perfil (concentrar = concentrar risco)
- Link diferente por pagina
- 15 a 20 dias ate a pagina achar publico; nao matar antes disso
