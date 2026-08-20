# PEDIDO DE LEITURA — v01

> Cole este arquivo INTEIRO no chat, junto com a imagem `folha.jpg` desta
> mesma pasta. Salve a resposta como `mapa.json`, aqui do lado.

Voce vai ler UMA folha de contato de um video e devolver **so' JSON**, sem
texto antes nem depois.

O video tem **3 take(s)**, ja' detectados por corte de cena:

| take | de/ate | duracao |
|---|---|---|
| take 1 | 0.0s a 5.7s | 5.7s |
| take 2 | 5.7s a 11.5s | 5.8s |
| take 3 | 11.5s a 17.6s | 6.1s |

A folha tem 12 quadros, 4 por take, na ordem dos takes. O tempo de cada
quadro esta' queimado em amarelo no canto.

## O QUE DEVOLVER

Um objeto com a chave `takes`, uma entrada por take, NA ORDEM:

```json
{"takes": [
  {"ambiente": "", "superficie": "", "props": [""], "gesto": "",
   "pessoa": "", "traje": "", "camera": "", "luz": "", "audio": "",
   "texto_em_quadro": ""}
]}
```

## REGRAS DURAS

- Tudo **EM INGLES** e pronto para entrar num prompt de imagem: frase
  descritiva, concreta, com material e cor. Nada de julgamento
  ("beautiful kitchen"), nada de marca, nada de nome de pessoa famosa.
- ⛔ NUNCA escreva `phone`, `iPhone`, `camera`, `filming`, `selfie` ou
  `tripod` no campo `camera`. Descreva o **angulo** e a **altura**. Escrever o
  aparelho faz o gerador DESENHAR o aparelho.
- ⛔ NUNCA escreva negacao do tipo `not a celebrity` ou `no phone in frame`:
  negacao INJETA o token. Descreva o que EXISTE.
- `props` e uma lista, um item por objeto, com cor, material e **posicao no
  quadro**.
- `pessoa`: o que aparece do corpo (so' maos? torso? rosto?), idade aparente,
  etnia, marcas distintivas. Se nao houver ninguem, escreva `none`.
- `texto_em_quadro`: a legenda queimada nessa cena, como aparece. Se nao
  houver, string vazia.
- Se um take estiver ambiguo na folha, descreva o que da' para ver e diga o
  que ficou incerto dentro do proprio campo. **Nao invente.**

## A FALA DE CADA TAKE, ja' alinhada por tempo

**take 1** (0.0s a 5.7s): At 65, my wife asked what changed. These two show you exactly what.
**take 2** (5.7s a 11.5s): A spoonful of the gelatin trick in cold water opens the blood flow your soldier lost.
**take 3** (11.5s a 17.6s): Comment gelatin and follow me to receive the complete step by step.
