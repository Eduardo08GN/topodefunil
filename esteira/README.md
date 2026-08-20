# ESTEIRA — video-fonte entra, prompts do Veo saem

> ⛔ **Não substitui os agentes.** Motor (`<angulo>_short.py`) gera **lote**
> variado de um ângulo validado; a esteira gera **um vídeo parecido com um
> vídeo**. Ela escala repertório, não volume. As duas convivem.

Desenhada em volta do **custo de token**, para o plano básico:

| etapa | onde roda | token |
|---|---|---|
| 1 · `ler.py` | seu PC | **zero** |
| 2 · a leitura | **no seu chat** | ~4-5k por vídeo |
| 3 · `gerar.py` | seu PC | **zero** |

## Como usar

Abra o `ESTEIRA.exe` (`Desktop\agentes_py\ESTEIRA\`) e siga as três caixas:

1. **Escolher vídeo → LER.** Detecta os cortes de cena, monta a folha de
   contato e transcreve com `faster-whisper`, tudo offline.
2. **Copiar PEDIDO → colar no chat junto com a `folha.jpg`.** Traga o JSON de
   volta, cole na caixa e clique em salvar. O app confere se o número de takes
   bate com o detectado.
3. **GERAR.** Sai `BLOCO 0 (REF)`, `IMAGE 01/0N` e `TAKE 01/0N`, com botão de
   copiar bloco a bloco.

Pela linha de comando é o mesmo caminho:
`python esteira/ler.py video.mp4` → cola no chat → `python esteira/gerar.py <slug>`.

## As duas decisões que o painel expõe

**`takes`:** `fonte` respeita os cortes detectados; `2` ou `3` colapsam para o
nosso formato. ⛔ O colapso **funde** os takes extras no último, nunca
descarta — na fonte o payoff quase sempre mora no fim.

**`nosso CTA` × `fiel à fonte`:** o modo `nosso` troca a palavra do CTA para
`gelatin`. ⛔ `book` e `yes` são as duas que a fonte mais pede e as duas que
**quebram a automação de DM** — o comentário entra e a mensagem não sai.
⚠️ O modo `fiel` é para clonar concorrente: se a fonte vender outra coisa, o
criativo deixa de casar com a VSL, que foi o que travou o MARCUS.

## O que o código impede sozinho, sem ninguém lembrar

- **aparelho SEGURADO** no prompt de imagem — `with the phone in his free hand`
  fez o gerador desenhar o telefone e o operador gerou um lote inteiro assim.
  ⚠️ `iPhone` na cauda estética continua passando: ele vive em 46 motores e
  está certo lá. O que quebra é o aparelho na **mão do personagem**.
- **negação** (`not a celebrity`, `no phone in frame`) — negação injeta o token.
- **bloco acima de 3.900 caracteres** — a AdBatch corta em 4.000 **em silêncio**,
  e o que ela corta é o fim, onde moram câmera, luz e cauda.
- **fala acima de 24 palavras** — 8,0s × 3,1 palavras/s, os dois medidos.

## O limiar de corte é medido, não escolhido

Gabarito: os 14 cortes que a leitura ótica quadro a quadro de 2026-08-16 achou
nos 7 vídeos-fonte.

| limiar | cortes reais achados | falsos |
|---|---|---|
| 0.30 | 8 de 14 | 0 |
| 0.20 | 12 de 14 | 0 |
| **0.12** | **14 de 14** | **2** |
| 0.05 | 14 de 14 | 30 |

⚠️ **Perder corte é pior que inventar um:** o take vira dois planos colados num
prompt só, e a imagem gerada não consegue ser os dois. Falso positivo o
operador vê na folha e ignora; corte perdido some.
