# PROPOSTA — RUTH 16, a humilhação pública no nicho de emagrecimento

> Fonte: `facebook.com/profile.php?id=61589307140516` ("Ruth Yoder").
> 60 posts garimpados, 59 baixados, 58 transcritos, folhas de contato de todos.
> Bruto em [`concorrentes/fb-61589307140516-garimpo.md`](../concorrentes/fb-61589307140516-garimpo.md).

## Por que esta página vale um agente

**A mediana da página inteira é 48,5 comentários por mil views.** O melhor
reel-fonte que este repo já modelou — o campeão dos sete do BANHO 16 3T — fez
**20,5**, e era o topo, não a mediana. O topo daqui faz **95,7**.

⚠️ E o CTA dela é `yes` em praticamente todos os 60, que quebra a nossa
automação de DM. Vira `recipe` ou a palavra que a oferta de emagrecimento
cadastrar.

## O corte: 15 de 59

⛔ Ordem do operador: *"os vídeos que não são de humilhação pública serão
descartados como vídeo-fonte"*. A assinatura é **literal** e dá para separar
por texto, sem olhar: os vídeos de humilhação abrem em

> `This was <NOME> before, <o desastre público>, <as testemunhas>. Pure shame.`

Os outros 44 são receita (`One teaspoon of baking soda…`), barriga em close
(`If your belly looks like this…`) ou pergunta-resposta (`People are asking me
the same question…`). ⚠️ Um regex largo de humilhação pegava 15 desses por
falar em `gym`, `doctor` ou `chair` — a assinatura é a **abertura**, não a
presença da palavra.

## A fórmula, e ela é UM template com um eixo trocado

```
TAKE 1  This was <NOME> before, <DESASTRE PÚBLICO>, <TESTEMUNHAS>. Pure shame.
TAKE 2  And this is <ela/ele> now, after I gave <ela/ele> one simple remedy
        every single morning… <CTA>
```

O corte cai sozinho em **~7,7s** no reel de 150 mil views — dois takes, que é
exatamente o nosso formato de 8s. ⭐ `pure shame` fecha o ato 1 em **11 dos 15**.

## Os oito desastres lidos (o eixo principal)

| desastre | reels | o que está em quadro |
|---|---|---|
| **o guindaste** | v27 · v28 · v40 · v45 · v47 | içada pela janela do 2º andar, bombeiros, EMS, ambulância; **o cabo arrebenta e ela cai** |
| **a cadeira do salão** | v46 · v50 | a cadeira racha durante a pedicure, e **todo cliente do salão vira a cabeça** |
| **a rampa do médico** | v09 · v15 · v51 | as pernas do marido tremendo sob o peso, os amigos parados sem conseguir ajudar |
| **a escada** | v49 | a escada cede e **leva o marido junto** |
| **o carro e o café** | v24 | ela perde o apoio ao sair do carro, cai e derrama café quente em si mesma |
| **a câmera de segurança** | v38 | o CCTV registra o casal **sem conseguir proteger o próprio filho** |
| **a reabilitação** | v39 | reaprendendo a andar numa clínica; dez minutos de luta para sair do carro no Walmart |
| **a imobilidade** | v59 | sem conseguir se mover, filmada e ridicularizada |

⭐⭐ **O beat da TESTEMUNHA é o que faz a humilhação ser pública**, e ele é
quase constante: `getting filmed and laughed at by the people around her`.
Sem terceiro em quadro isso vira acidente, não vergonha.

## A arquitetura proposta

**Constante — a personagem.** Ruth: senhora amish de touca branca, blusa
branca de mangas dobradas e avental cinza, na botica de prateleiras de vidros
e ervas penduradas. Ela é a assinatura da página e **não é eixo**.

**Eixo 1 — O DESASTRE (8 entradas lidas).** Cada entrada carrega o desastre +
o lugar + as testemunhas + o enquadramento **juntos**. ⛔ Separar em quatro
eixos daria mais combinação e menos nexo — é a lição do VICK 16.

**Eixo 2 — A PESSOA (nome, sexo, idade).** ⭐ A fonte troca **só o nome** e
republica o mesmo script: Betsy/Betty na mesma cadeira de salão,
Marjorie/Marilyn na mesma rampa. Isso não é descuido deles, é o eixo mais
barato que existe — e o nome atravessa os dois takes.

**Eixo 3 — O REENCONTRO (o lugar do depois).** Varanda de subúrbio com
bandeiras americanas, a botica, a calçada, a foto de família. É onde Ruth
aparece ao lado da pessoa transformada.

**Eixo 4 — O REMÉDIO.** O que ela deu. ⚠️ Depende da oferta de emagrecimento
que a VSL vender; hoje a fonte diz `one simple remedy` sem nomear, e nomeia
ingrediente só nos vídeos de receita (que estão fora do corte).

**Eixo 5 — O CTA.** Em `recipe` ou o que a automação escutar. Nunca `yes`.

## ⛔ O custo que precisa estar declarado antes de começar

**A MESMA PESSOA, obesa no take 1 e magra no take 2, em dois quadros gerados
separadamente.** É a continuidade mais cara que este parque já pediu — mais
cara que as três pessoas do ALFA 16, porque aqui o corpo **muda de propósito**
e só o rosto tem de permanecer. As saídas conhecidas:

- **BLOCO 0 (REF) com o rosto**, e os dois IMAGE ancorando nele por extenso.
- **O rosto parcialmente oculto no take 1** (de costas, de lado, cortado pelo
  batente) — que é o que a própria fonte faz em vários: no v45 o homem içado
  aparece de perfil e longe.
- ⛔ E a alternativa que eu **não** recomendo: pessoas diferentes. O vídeo
  inteiro é a promessa de que é a mesma pessoa.

## ⚠️ Três riscos, ditos uma vez

**Moderação.** Isto é humilhação explícita de pessoa obesa, com terceiros rindo
em quadro. O operador autorizou *"igual à fonte"*, e a fonte roda — mas ela
também declara `#syntheticperformer` e carimba `genaicontent` no vídeo, o que
é declaração de conteúdo sintético e provavelmente parte de por que sobrevive.

**Congruência.** O agente aponta para uma **VSL de emagrecimento**, decidida
pelo operador. Ele não é irmão dos 32 de gelatina — é rota própria, como o
RARO 16.

**A fonte é gerada por IA.** As pessoas, a Ruth e os desastres são todos
sintéticos. Isso ajuda (a marca sai embaralhada, não há pessoa real
humilhada) e cobra (o gerador tem de aceitar a cena, e cena de resgate com
bombeiro é onde a moderação costuma travar).

## O que eu faria primeiro

Ler oticamente os **15**, quadro a quadro, e só então escrever os pools — é o
que separou o `gelahorse16` do `vick16`. Os 44 descartados continuam em disco
e viram repertório para um segundo agente de **receita**, se a oferta pedir.
