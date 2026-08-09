# Piloto AdBatch — o ciclo agente → AdBatch Vertical 2, em N abas

Script AutoHotkey **v2** que faz o vaivém entre o app do agente (monitor
vertical) e a ferramenta AdBatch Vertical 2 no Chrome (monitor horizontal).

```bash
"C:\Users\edlut\Topodefunil\funil-organico\adbatch-piloto\Piloto AdBatch.bat"
```

## O ciclo, por aba

1. **agente** — seleciona `BLOCO 0 (REF)` e clica `COPIAR BLOCO`
2. **agente** — clica `copiar os 2 IMAGE`
3. **agente** — clica `copiar os 2 TAKE`
4. **Chrome** — cola os três juntos no **Roteiro Master**
5. **Chrome** — clica `Gerar Lote com Referência`
6. **agente** — `marcar como usado` + `Ctrl+R` (sorteia o próximo vídeo)
7. próxima aba

Depois de preencher todas, entra em **ronda**: revisita cada aba e, se um slot
continuar vazio, clica `REGERAR` nele. Repete até todos cheios ou até o limite
de rondas.

## Teclas

| tecla | o que faz |
|---|---|
| **F9** | calibrar (ou recalibrar) os pontos de clique |
| **F8** | ⭐ **ensaio seco** — percorre tudo sem colar e sem clicar em Gerar |
| **F10** | rodar de verdade |
| **F12** | mostra o log da última execução |
| **Esc** | aborta na hora ⚠️ *só funciona enquanto o ciclo está rodando* |

## ⛔ Antes da primeira vez

**Rode a calibração (F9).** O script não tem nenhuma coordenada chutada: ele
pergunta alvo por alvo, você põe o mouse em cima e aperta F9. Fica gravado em
`piloto-adbatch.ini`, ao lado do script.

Deixe as duas janelas **já posicionadas** como vão ficar. Mover ou
redimensionar qualquer uma delas depois obriga a recalibrar — as coordenadas
são de tela absoluta.

Depois de calibrar, **rode o F8 primeiro**. Ele percorre o ciclo inteiro
movendo o mouse pelos alvos, mas não cola nada e não clica em Gerar. É como se
confere que a calibração pegou os botões certos sem gastar crédito do Flow.

## ⚠️⚠️ A armadilha que o script existe para evitar

**O clipboard mudo.** Se um clique de copiar não pega o botão, a área de
transferência continua com o conteúdo do vídeo **anterior** — e o script
colaria a REF de um vídeo com as cenas de outro, sem reclamar. O erro só
apareceria no render, com o crédito já gasto.

Por isso, a cada cópia o script **limpa o clipboard, clica, espera e confere a
assinatura** do que veio (`REF 01:`, `IMAGE 01/02`, `TAKE 01/02`). Assinatura
errada = para na hora e diz em qual aba parou. E confere também que vieram os
**dois** de cada par (`IMAGE 02/02`, `TAKE 02/02`) — se o motor tiver entregue
só um, o lote sairia pela metade e o slot 2 ficaria vazio para sempre.

## Configuração fina — `piloto-adbatch.ini`

A calibração grava o essencial. Estes você pode editar à mão:

```ini
[config]
abas=10                        ; quantas abas do Chrome
rondas=6                       ; quantas voltas de conferência
espera_s=45                    ; segundos antes de cada volta
titulo_agente=AGENTE           ; casa com "AGENTE COLO 16 by Eddie"
titulo_chrome=Google Flow
```

⚠️ `titulo_agente=AGENTE` casa com qualquer um dos agentes. Se quiser travar em
um só, ponha o título inteiro (`AGENTE COLO 16 by Eddie  v1.2`).

## ⭐ Velocidade — o botão `RITMO`

No topo do `.ahk`, uma linha só governa **todas** as esperas ajustáveis:

```ahk
global RITMO := 0.55
```

`1.00` é o ritmo original. **`0.55` é o atual** — pedido do operador em
2026-08-09 (*"pode acelerar, tá lento, reduzir 2 segundos"*). As esperas
ajustáveis somavam **4.710 ms por aba**; a 0.55 caem para ~2.360 ms, medidos —
**2,35 s a menos por aba**, ou ~23 s num lote de 10.

Quer mais rápido? Baixe o número. Voltou a errar clique ou colar no lugar
errado? Suba. **Não mexa nas esperas uma a uma** — é o número que existe para
isso.

⛔ **Três coisas o fator NÃO acelera, e não é esquecimento:**

| o quê | por quê |
|---|---|
| `Sleep 900 + Random(0,700)` depois do `Ctrl+V` | o app precisa **reparsear** o roteiro colado antes de o Gerar valer. Isso é função, não cadência. |
| `respirar()` — a pausa longa e rara | é ela que quebra o padrão de máquina. Encolher desfaria a proteção de atividade suspeita. |
| o espalhamento (`±35%`) de cada pausa | o tremor continua o mesmo **em porcentagem** — acelerar não deixa o ritmo mais regular. |

## O que é frágil aqui, dito na cara

- **Coordenada de tela.** Qualquer mudança de layout, zoom do Chrome ou posição
  de janela quebra tudo. É o preço de automatizar uma UI que não expõe API.
- **A cor do slot vazio.** A ronda decide se a imagem chegou comparando o pixel
  do meio do slot com a cor gravada na calibração. Se o Flow mudar o
  placeholder, ou se o pixel calibrado cair em cima de algo que anima, a ronda
  passa a mentir. Ela só **regera a partir da segunda volta**, justamente para
  não jogar fora imagem que ainda estava sendo gerada.
- **`Ctrl+9` no Chrome vai para a ÚLTIMA aba, não para a nona.** Da nona em
  diante o script conta a partir da primeira com `Ctrl+Tab`.

## Estado

⚠️ **Sintaxe validada; o ciclo nunca rodou contra as janelas de verdade.** Não
dá para medir isso sem as duas telas abertas. O `F8` existe exatamente por
isso: é o primeiro teste, e ele é gratuito.
