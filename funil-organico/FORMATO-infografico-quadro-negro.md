# FORMATO — o infográfico de quadro-negro

> **O Mecanismo Único do Problema desenhado em vez de escrito.**
> Um quadro-negro de sala de aula, um desenho anatômico tosco a giz, uma lista
> que desmonta o que a pessoa já tentou, e um X vermelho em cima da solução
> errada.

- **Status:** ⚠️ **doutrina de observação, ainda NÃO testada contra o gerador.**
  Tudo aqui saiu da leitura de quatro anúncios de concorrente; nada foi
  renderizado ainda. Ver §*O que falta medir*.
- **Fonte:** quatro criativos garimpados em 2026-09-02 (biblioteca de anúncios),
  nichos de olheiras, ciática, Hashimoto e blefaroplastia masculina.
- **Serve para:** post de imagem estática e criativo de anúncio. **Não** é
  formato de reel.

## ⭐ A EVIDÊNCIA É O TEMPO NO AR, não o like

Os quatro rodam há **30, 30, 32 e 32 dias** (`Aug 2 - Present · 32d`). Anúncio
que sobrevive um mês está pagando o próprio tráfego — é o único sinal público
que não dá para comprar. Curtida e comentário nesse contexto são ruído; o
relógio não é.

⚠️ Os números nos selos verdes e azuis (`99`, `215`, `34%`, `85%`) são da
ferramenta de espionagem e **não sei o que medem**. Não construa hipótese em
cima deles.

## A anatomia — sete elementos, e cada um tem função

| # | elemento | função |
|---|---|---|
| 1 | quadro-negro com moldura de madeira | professor, não anunciante |
| 2 | traço de giz à mão | não parece anúncio, e por isso é olhado |
| 3 | manchete em caixa alta | a negação da solução óbvia |
| 4 | desenho anatômico tosco | mostra **onde** o problema mora |
| 5 | lista de 4 a 6 bullets | desmonta o que ela já tentou |
| 6 | **um** X vermelho | a única cor da peça, e o olho vai nele |
| 7 | seta de CTA no canto | `HERE'S HOW →` |

⛔ **O X vermelho é a única cor.** Nos quatro anúncios o resto é giz branco
sobre verde ou preto. Colocar uma segunda cor divide a atenção e mata o
elemento 6 — que é o que diz, sem palavra nenhuma, *o que você faz hoje está
errado*.

## ⭐⭐ A MANCHETE — a fórmula é uma só

    WHY <o problema> WON'T <resolver>
    WHY <a solução que ela usa> DOESN'T <funcionar>

Os quatro, literais:

    WHY YOUR EYE BAGS WON'T LEAVE
    WHY STRETCHING YOUR BACK DOESN'T FIX IT
    WHY HASHIMOTO'S WON'T LEAVE
    WHY MEN 50+ ARE CHOOSING THIS OVER BLEPHAROPLASTY

⛔ **Três das quatro abrem em `WHY` e negam.** Isso não é estilo, é o
**Mecanismo Único do Problema** do Georgi na forma mais curta que existe: *você
falhou até agora, e não foi culpa sua — foi porque ninguém te contou X*. A
manchete promete a explicação, nunca o resultado.
⚠️ A quarta (`CHOOSING THIS OVER`) é de outra família — comparação, não
mecanismo. É a única que carrega nome de procedimento e a única com preço
implícito.

⭐ **A sub-manchete, quando existe, é uma EQUAÇÃO:** `WRONG AREA = SHORT
RELIEF`. Três palavras, um sinal de igual, e ela entrega o mecanismo inteiro.

## A LISTA — o padrão bullet a bullet

Do anúncio de olheiras, verbatim:

    - not lack of sleep
    - creams don't reach it
    - 0.3mm below surface
    - barrier blocks everything
    - fluid — stuck here

⭐ Leia a ordem, ela é deliberada:

1. **nega a causa que ela acredita** (`not lack of sleep`)
2. **nega a solução que ela comprou** (`creams don't reach it`)
3. ⭐⭐ **um NÚMERO** (`0.3mm below surface`)
4. **nomeia o obstáculo** (`barrier blocks everything`)
5. **aponta o lugar** (`fluid — stuck here`), amarrado ao desenho por uma seta

⛔ **O número é o eixo da peça.** `0.3mm` não ajuda ninguém a fazer nada — ele
existe para dar **cheiro de verdade**. É a mesma função do `neurogenes Zittern`
no ATEM 16 e do `gelatin trick` no resto do parque: um detalhe específico
demais para ter sido inventado. Sem ele a lista vira opinião.

⛔ **Bullet tem no máximo 5 palavras.** Nos quatro anúncios nenhum passa disso.
O leitor está no scroll: ele lê a manchete, varre a lista em dois segundos e
decide. Bullet de linha inteira não é lido.

## ⛔⛔ O PROBLEMA QUE DECIDE A RECEITA: GERADOR ESCREVE TEXTO MAL

Este formato é **quase inteiramente texto**, e é justamente o que gerador de
imagem faz pior. Letra trocada, palavra inventada, linha que vira rabisco.

⚠️ E o repo já sabe disso por medição própria: a doutrina do `banho16` registra
que os reels da fonte são gerados por IA e que **o texto dos rótulos sai
embaralhado** — por isso aquele agente pede a FORMA da embalagem e nunca o
texto dela.

⭐ **Daí a regra deste formato, e ela é a peça central do documento:**

> **O gerador faz o QUADRO e o DESENHO. O texto entra por cima, depois.**

Duas camadas:

| camada | quem faz | o que entra |
|---|---|---|
| **fundo** | o gerador de imagem | quadro-negro, moldura, giz do desenho anatômico, o X vermelho, textura |
| **texto** | composição posterior | manchete, sub-manchete, bullets, seta de CTA |

⛔ **Não peça o texto ao gerador nem para "ver como fica".** Um quadro com texto
embaralhado tem de ser descartado inteiro, e você não consegue apagar giz
gerado sem destruir o fundo. Peça o quadro **com áreas vazias** onde o texto vai.

⚠️ Isto tem precedente direto na casa: o Veo Editor já queima texto por cima de
vídeo (legenda e o pin do CTA) exatamente porque texto pedido ao gerador não é
confiável. É a mesma decisão, em outra mídia.

## Molde de prompt — a camada de fundo

⚠️ **Não testado.** Use como ponto de partida e corrija contra o render.

```
A dark green classroom chalkboard in a scratched wooden frame, filling the
frame straight on. Drawn on it in rough white chalk, by hand, is a simple
side-profile anatomical diagram of <a região do corpo>, crude and
diagrammatic like a teacher sketched it quickly during a lesson, with two
thin chalk arrows pointing at <o ponto exato do mecanismo>. Over <a solução
errada> there is a single large X drawn in red chalk — it is the only colour
on the board. The upper third of the board is EMPTY chalkboard, and the right
half beside the diagram is EMPTY chalkboard. Chalk dust smudges, an eraser
streak across one corner, uneven chalk pressure. Flat even classroom light.
Photographed straight on, no perspective distortion. Vertical 4:5.
No lettering, no words, no numbers, no writing of any kind on the board.
```

⛔ A última linha é a mais importante do molde. `No lettering, no words, no
numbers` é o que preserva as áreas vazias para o texto real.
⚠️ E ela é uma **negação**, que este repo normalmente proíbe porque negação
injeta o token. Aqui é exceção consciente: o token que ela injeta (`words`) é
justamente o que se quer ausente, e o custo de o gerador escrever é maior que o
custo de ele desenhar um rabisco a mais. **Se o render vier com letra mesmo
assim, o caminho não é reforçar a negação — é descrever positivamente o que
ocupa aquele espaço** (`the upper third is clean bare slate`).

## A camada de texto — o que compor por cima

- **Fonte:** giz de verdade (`Chalkduster`, `Caveat`, `Gochi Hand`) ou uma
  sans condensada em caixa alta. ⛔ Nunca a fonte padrão do editor.
- **Manchete:** caixa alta, ocupa o terço superior inteiro, duas linhas no
  máximo.
- **Bullets:** alinhados à esquerda, um travessão antes de cada, na metade
  direita.
- **O CTA:** canto inferior direito, dentro de uma caixa de giz, com uma seta.

## O que este formato NÃO é

⛔ **Não é reel.** É imagem estática. Todo o parque de agentes é vídeo; este
documento descreve outra mídia e não deve ser misturado com os `*_short.py`.
⛔ **Não substitui o infográfico "de produção"** que o operador já publicou na
`The Wellness Hub` (o de técnica de respiração, colorido, com fotos). Aquele é
material de autoridade e ensina; este **nega e abre curiosidade**. Os dois
convivem e fazem trabalhos opostos.

## ⏳ O que falta medir — nada aqui foi renderizado

1. **O molde de fundo aguenta a instrução de não escrever?** É a pergunta que
   decide se o formato é viável. Testar em 10 renders e contar quantos vêm com
   letra.
2. **O desenho anatômico sai legível a giz?** Anatomia tosca é fácil; anatomia
   tosca *e correta* é outra coisa.
3. **O X vermelho fica no lugar pedido**, ou o gerador o espalha pelo quadro.
4. **Compor o texto em quê?** O Veo Editor queima texto em vídeo via `.ass`;
   para imagem estática não há ferramenta na casa ainda. Decidir antes de
   escalar.

## Conexões

- [`CONTRATO-COPY-16S.md`](CONTRATO-COPY-16S.md) — o CT5 (a receita é a moeda)
  vale aqui inteiro: a lista **nega e localiza**, nunca ensina.
- [`licoes-producao-veo.md`](licoes-producao-veo.md) — §*Declaração é munição*,
  que é a razão de a negação do molde ser exceção declarada.
- `principios/mecanismo-unico.md` — de onde a manchete sai.
- [`licoes-de-construcao.md`](licoes-de-construcao.md) — §*aceite é MEDIÇÃO,
  nunca RELATO*, que é por que este documento nasce marcado como não testado.
