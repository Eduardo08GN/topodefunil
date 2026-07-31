# 🔬 RUNBOOK — Bissecção de moderação do Veo

> **Como descobrir, na prática, o que faz o Veo bloquear um prompt.**
>
> Não é sobre "reescrever até passar". É um método de **teste empírico com
> variável única**, feito a quatro mãos: o agente propõe a hipótese, o operador
> roda no Flow e traz `passou` / `caiu`, e a hipótese seguinte nasce do
> resultado.
>
> Nasceu da investigação do NECROSE em 2026-07-31, que em cinco rodadas
> derrubou três hipóteses minhas seguidas — inclusive a de que existia um
> gatilho.

---

## POR QUE ESTE ARQUIVO EXISTE

Antes dele, o reflexo diante de uma recusa era **reescrever no escuro**: trocar
uma palavra que parecia suspeita, mandar de novo, e se passasse declarar
vitória. Isso tem três defeitos que custaram lotes inteiros:

| Defeito | O que acontece |
|---|---|
| **Mudar duas coisas de uma vez** | passa, e você não sabe qual das duas resolveu — então não vira regra |
| **Mirar na categoria errada** | eu gastei duas rodadas atacando "parece carne apodrecida" quando a taxonomia pública do Veo **não tem categoria de gore** |
| **Tratar 1 passe como prova** | a política de conteúdo nocivo tem **variância**: o mesmo prompt caiu e depois passou, sem mudar um caractere |

O método abaixo fecha os três. E o subproduto é mais valioso que o vídeo:
**cada rodada mapeia um pedaço do classificador**, e esse mapa se acumula.

---

## O PROTOCOLO

### Os papéis

| Quem | Faz |
|---|---|
| **O agente (Claude)** | formula a hipótese, escreve o prompt-teste, **declara antes o que cada resultado vai significar**, e propõe a rodada seguinte a partir do resultado |
| **O operador (Ed)** | roda no Flow e responde **`passou`** ou **`caiu`**. Nada mais é necessário |

### O ciclo

```
recusa  →  isolar a variável  →  hipótese  →  prompt-teste  →  operador roda
                                     ↑                              ↓
                                     └────── resultado ─────────────┘
                                                  ↓
                               3 baterias com sorteios DIFERENTES
                                                  ↓
                               pedir permissão  →  gravar no agente
```

### As regras duras

**1. Uma variável por rodada.** Se duas mudam e passa, a rodada não ensinou
nada. Isso vale inclusive para "melhorias" que parecem óbvias no caminho.

**2. Declarar o significado ANTES de rodar.** Toda rodada sai com uma tabela:
*se passar, quer dizer X e a próxima é Y; se cair, quer dizer W e a próxima é
Z.* **Teste que só é informativo quando passa é teste ruim** — a falha também
tem que apontar para o próximo passo.

**3. Todo prompt-teste carrega uma linha `Dialogue:` — e ela SAI DO AGENTE.**
Sem a linha, o Veo **improvisa a fala** e o vídeo sai fora do escopo. Com uma
linha inventada, sai igualmente fora do escopo — só que por culpa de quem
escreveu o teste. *(Regra descoberta na rodada C do caso NECROSE, quando a copy
driftou.)*

> ⛔ **Ao formular hipótese, não se faz drift do alinhamento de propósito da
> copy estrutural da operação.** Ordem do operador, 2026-07-31, depois de eu
> propor uma "fala neutra" inventada (*"It has been a long week out here…"*)
> para isolar variável. Foi a **segunda vez no mesmo dia**.

Por que a fala neutra é uma armadilha seedutora e errada:

| | |
|---|---|
| **Se o teste passa** | você tem um vídeo com copy que não vende nada — geração paga, output no lixo |
| **Se o teste cai** | você aprendeu sobre uma frase que nunca vai ao ar |
| **Nos dois casos** | mediu-se o classificador contra um texto que não existe na operação |

**O que fazer no lugar:** para isolar a fala, troque por **outra fala do próprio
agente** — de preferência uma que já passou em render. Ela é copy em escopo
*e* é um controle melhor, porque o resultado dela já é conhecido. No caso
NECROSE, a fala da cena 2 servia: estava aprovada minutos antes e ainda por
cima falava do ingrediente que estava na mesa da cena testada.

**4. Bissecção roda 1×. Produção roda 3×, com SORTEIOS DIFERENTES.**
Repetir o mesmo prompt três vezes só mede variância. Rodar três sorteios
distintos — arquétipo, página, copy e props diferentes — mede se a correção
**generaliza no pool**, que é o que importa antes de virar constante.

**5. Só se escreve no agente depois das 3 aprovações — e ainda assim pedindo
permissão.** Ordem do operador, 2026-07-31. Copy e cena são dele.

### Como escolher a PRIMEIRA hipótese

Sempre a mesma pergunta, antes de qualquer reescrita:

> **O que este bloco tem que os blocos que PASSARAM não têm?**

Compare com o resto do lote, elemento por elemento, e monte a tabela. No caso
NECROSE, isso mostrou de cara que o IMAGE 01 passava e só o vídeo caía — o que
já eliminava metade do espaço de busca antes da primeira geração de teste.

⚠️ **E o passo que eu mais pulei: ISOLAR A VARIÁVEL.** Antes de reescrever
qualquer coisa, rode o **prompt mínimo** na mesma imagem:

```
Animate the provided image exactly. Handheld iPhone shot, very slight natural
sway, no cuts. The man speaks to the camera. Nothing else in the frame moves.
Dialogue: "<uma linha qualquer do agente>"
Audio: <ambiente>. No music.
```

- **Caiu** → a causa está na **imagem**. Nenhuma reescrita de texto resolve.
- **Passou** → a imagem está exonerada; o gatilho está no **prompt**, e a
  bissecção começa devolvendo um pedaço por rodada.

Esse teste custa uma geração e corta o problema ao meio. **Fazer isso primeiro
teria economizado quatro rodadas no caso fundador.**

---

## O QUE JÁ SABEMOS DA MODERAÇÃO DO VEO 3.1

Pesquisa 2026-07-31 (documentação oficial + fórum de desenvolvedores).

### As categorias são `violence · sexual · derogatory · toxic`

São as nomeadas publicamente para os filtros de prompt e de imagem de entrada.
⚠️ **Não existe categoria pública de "gore" nem de "conteúdo médico".** A
cláusula de saúde da Prohibited Use Policy é estreita — fala de *"claims
enganosos de expertise"*, não de imagética anatômica.

> **Consequência prática:** ao formular hipótese, mire numa categoria que
> **existe**. Eu queimei duas rodadas atacando "parece tecido necrosado"
> quando gore não é uma categoria dele.

### O classificador é MULTIMODAL

A documentação é explícita: **artefatos benignos combinados podem produzir um
resultado nocivo.** Imagem e texto são julgados **juntos**, nunca em separado.
Por isso a mesma frase passa numa imagem e cai em outra.

### Imagem aprovada pode ser bloqueada no vídeo

É comportamento **documentado**, não bug nosso: há relato no fórum oficial de
imagem gerada pelo próprio Gemini, aprovada no filtro de imagem, e recusada na
etapa de vídeo. **O filtro de vídeo é mais estrito que o de imagem.**

> É por isso que `IMAGE aprovado + VÍDEO recusado` é um padrão, não um acidente
> — e é o cenário mais comum das nossas recusas.

### Os filtros são over-tuned

Descritos como desenhados para sinalizar **qualquer coisa que remotamente se
pareça** com violação. Falso positivo é o modo normal de operação, não a
exceção.

### ⚠️ CORREÇÃO IMPORTANTE — "conteúdo nocivo" NÃO é determinística

O [`licoes-producao-veo`](licoes-producao-veo.md) classificava as três políticas
assim:

| Política | Comportamento que a gente supunha |
|---|---|
| pessoa famosa | variância alta → regerar 1-2× antes de investigar |
| menores | consistente → mudar geometria |
| conteúdo nocivo | **consistente → reescrever a string** |

**A terceira linha está errada.** No caso NECROSE, o **mesmo prompt, na mesma
imagem, caiu e depois passou** sem mudar um caractere.

> **Antes de investigar qualquer recusa, regere 2×.** Vale para as três
> políticas. Investigar variância é a forma mais cara de não aprender nada.

---

## O CASO FUNDADOR — NECROSE, 2026-07-31

Cena 1: dois modelos anatômicos 3D em pedestal, um apodrecido e um são, com o
REF de tronco nu e um lobo. `IMAGE 01` aprovado; **vídeo recusado** com
*"políticas contra a geração de conteúdo nocivo"*. A cena 2, com a placa D1 em
corte sagital, passava.

| # | Direção de cena | Fala | Resultado |
|---|---|---|---|
| **A** | completa | assertiva (`Your {o} looks like this right now`) | ❌ |
| **B** | completa | condicional (`If you want your {o} to go from this to this`) | ❌ |
| **C** | mínima | **nenhuma** | ✅ |
| **D** | mínima | condicional | ✅ |
| **E** | mínima + **gesto de apontar os dois modelos** | condicional | ✅ |
| **F** | E + **declaração longa de imobilidade** | condicional | ✅ |
| **G** | **completa** (reconstrução total) | condicional | ✅ |

### O que cada rodada matou

- **C** exonerou a **imagem**: o par de modelos genitais em volume *pode* ser
  animado. Quase joguei o bit visual fora antes disso.
- **D** exonerou a **fala**, inclusive a condicional.
- **E** exonerou o **gesto de apontar para os modelos** — o suspeito nº 1, por
  analogia com o F12b do FLAGRANTE (mão de terceiro no corpo).
- **F** exonerou a **imobilidade longa**, que eu suspeitava por precedente
  (`pulse`/`swelling` derrubou vídeo com IMAGE aprovado: *nomear o eixo já
  basta, negar não protege*).

### As três hipóteses minhas que morreram

1. **"É a necrose lida como carne."** Morreu na pesquisa: gore não é categoria.
2. **"É o claim de cura na fala."** Morreu na rodada B — a forma condicional,
   que é a linha literal da fonte, caiu igual.
3. **"É a morfologia fálica em 3D."** Morreu na rodada C — a mesma imagem
   animou sem problema.

> **A hipótese que sobreviveu foi a que eu não tinha considerado: variância.**
> Cinco passes seguidos em prompts cada vez mais completos, num caso onde três
> tentativas anteriores tinham falhado.

### O veredito (rodada G)

A rodada G devolveu a **direção de cena inteira** — nada omitido, nada suavizado
— na mesma imagem que tinha derrubado o vídeo duas vezes. **Passou.**

> **Não havia gatilho.** O prompt que caiu nas rodadas A e B é, na parte de
> direção de cena, o mesmo que passou na G. A única diferença que sobreviveu ao
> escrutínio foi **a tentativa**, não o texto.

Duas consequências, e a segunda é a que dói:

1. **O agente NECROSE está certo como está.** Nenhuma linha de cena precisou
   mudar. A única correção que valeu foi a do **hook condicional** (NE7) — e
   essa nasceu de escopo de copy, não de moderação.
2. **Quatro rodadas de reescrita foram gastas caçando um fantasma.** Um
   `regerar` na primeira recusa teria fechado o caso. É exatamente por isso que
   "regere 2× antes de investigar" virou a primeira regra deste runbook.

---

## O QUE SOBROU DE APRENDIZADO PERMANENTE

**1. Recusa não é veredito sobre o conteúdo.** Continua valendo — mas agora com
um degrau antes: **recusa também não é necessariamente sinal.** Regere 2× antes
de formular hipótese.

**2. Compare com o que passou, não com o que você imagina.** A tabela
"o que este bloco tem que os outros não têm" é mais barata e mais informativa
que qualquer intuição sobre o classificador.

**3. Prompt mal parseado piora o julgamento.** Um aposto pendurado
(`...with a gland at its base, lifted to shoulder height`) prende o verbo no
substantivo errado. Antes de suspeitar de política, leia a frase como um
parser leria.

**4. Mire numa categoria que existe.** `violence · sexual · derogatory · toxic`.
Se a sua hipótese não cai em nenhuma delas, provavelmente está errada.

**5. ⛔ Mudança de cena feita sob hipótese não provada volta atrás — e custa duas
vezes.** Caso registrado em 2026-07-31: a cena 3 do SHORT caiu várias vezes, eu
apontei a **embalagem de marca** (caixa de bicarbonato com logotipo e painel
nutricional legíveis) como suspeita, e o prop saiu de cena nos quatro agentes —
com string travada, receita fixada e regra de linter. O operador tinha dito na
hora: *"não creio que seja o problema, pois já vi vários vídeos com a marca
aprovados"*. Ele estava certo: o take **com** o bicarbonato passou, e tudo foi
revertido.

> **O prop não estava barrado; a rodada é que não tinha sido feita.** Antes de
> tirar qualquer coisa da cena, a pergunta é: *isto foi testado ou é palpite?*
> Se for palpite, não sai de cena — vira rodada.

O custo real não é o retrabalho: é que a mudança **destrói o que faz o vídeo
converter** enquanto persegue um fantasma. É a mesma armadilha do §Recusa do
gerador, agora com o carimbo de um caso concreto.

**6. Deriva de copy não se corrige com boa intenção.** No mesmo caso, três de
quatro hooks tinham escorregado da forma condicional da fonte para a forma
assertiva sem que ninguém notasse. A correção só é durável quando vira
**regra de linter** no motor do agente.

---

## TEMPLATE DE RODADA (copiar e preencher)

```markdown
# RODADA <n>

**O que já sabemos:**
| # | variável | resultado |
|---|---|---|
| ... | ... | ✅ / ❌ |

**Hipótese:** <o gatilho é X, porque Y>

**Mudo uma coisa só:** <a variável desta rodada>

<o prompt completo, pronto para colar>

## O que cada resultado me diz
| | significado | próxima rodada |
|---|---|---|
| **passou** | ... | ... |
| **caiu** | ... | ... |
```

---

## Conexões

- [`licoes-producao-veo.md`](licoes-producao-veo.md) — o playbook das lições pagas; **as três políticas e a correção sobre variância moram lá também**
- [`prop-metaforas.md`](prop-metaforas.md) §Recusa do gerador — as 4 alavancas de reescrita (token, relação, gênero da imagem, geometria congelada). Este runbook é o que se faz **antes** de escolher a alavanca
- [`RUNBOOK-app-offline.md`](RUNBOOK-app-offline.md) — como a regra descoberta vira linter no motor do agente
- [`../CLAUDE.md`](../CLAUDE.md) §Regra de alçada — por que a gravação no agente sempre passa por permissão
- Fontes da pesquisa: [Responsible AI for Veo (Vertex AI)](https://cloud.google.com/vertex-ai/generative-ai/docs/video/responsible-ai-and-usage-guidelines) · [Generative AI Prohibited Use Policy](https://policies.google.com/terms/generative-ai/use-policy) · [Veo 3.1 image-to-video false positive (fórum oficial)](https://discuss.ai.google.dev/t/veo-3-1-image-to-video-blocks-wholesome-commercial-storyboard-child-safety-false-positive/131917)
