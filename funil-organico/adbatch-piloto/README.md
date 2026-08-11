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

## ⭐⭐ AS SESSOES (2026-08-11) — o F10 pergunta ONDE rodar

⛔ **O sintoma:** *"quando aperto F10 ele sempre abre a sessao do meu login
principal"*. ⚠️ **A causa nao era preferencia do AHK** — o script procurava a
janela pelo TITULO `Google Flow`, e as janelas do Dolphin **nao tem esse texto
no titulo**: elas se chamam pelo NOME DO PERFIL. Medido:

```
chrome.exe .... "Google Flow - bladerunner2049v2 - Google Chrome"
anty.exe ...... "CTA - O2 Ricardo"
anty.exe ...... "CTA - 03 Neusa"
```

A busca so' casava com a primeira. As outras eram **invisiveis** para o script.

⭐ **O discriminante e' o EXECUTAVEL:** o Dolphin roda `anty.exe` (um processo
por perfil aberto), o Chrome roda `chrome.exe`. Titulo muda quando se troca de
aba; executavel nao.

**Como usar agora:** o F10 (e o F8) abrem uma lista das sessoes **abertas** e
voce escolhe pelo numero. Os perfis que estao **fechados** aparecem marcados,
para voce saber que precisa abri-los no Dolphin — sumir da lista pareceria
defeito do script.

⛔ **So' janelas ja' abertas.** A API local do Dolphin existe (`localhost:3001`
responde) e daria para dar START num perfil parado, mas exigiria o token
gravado em arquivo. Decisao do operador: abrir no Dolphin, como ja' faz.

⛔⛔ **A TRAVA DE GEOMETRIA — leia antes do primeiro F10.** Os pontos
calibrados sao coordenadas de **TELA**. Se a janela escolhida nao tiver o mesmo
tamanho da janela em que o F9 calibrou, **todo clique cai fora do alvo e o
script segue rodando**, gastando credito sem erro nenhum. Por isso o script
agora MAXIMIZA a janela escolhida e COMPARA com a geometria gravada na
calibracao; se diferir, ele ABORTA.

⚠️ **INI antigo:** calibracoes anteriores a esta versao nao gravaram a
geometria. No primeiro F10 o script pergunta se pode adotar o tamanho da janela
atual — **so' responda SIM se os seis pontos foram apontados numa janela deste
mesmo tamanho.** Na duvida, rode o F9 na janela em que voce vai trabalhar.

⚠️ **A ronda usa a MESMA janela** que o ciclo usou. Ela le' pixel e clica
REGERAR em slot vazio: feita noutra sessao, leria a cor errada e jogaria fora
lote pronto.

## ⭐⭐ F3 (2026-08-11) — monta a bancada da sessao

**O problema:** montar a mao, por sessao, 16 abas em 2 janelas com Ctrl+T /
Ctrl+C / Ctrl+V.

**Como usar:** F3 abre um popup, voce cola **qualquer** url do Flow daquele
projeto (dashboard, AdBatch ou Montador), confere o preview e clica **Montar**.
Depois escolhe a sessao, e o script monta:

- **janela 1** — N abas no AdBatch Vertical 2 (N = o mesmo `config/abas` do F10)
- **janela 2** — M abas no dashboard + 1 aba no Montador (`config/abas_dashboard`, default 5)

O **F10 continua sendo o gatilho da geracao**, sem mudanca.

### O que tornou a automacao possivel (medido nas urls do operador)

| | valor | |
|---|---|---|
| tool AdBatch Vertical 2 | `d882542c-72bd-4f73-81e1-472aa705775f` | **constante** |
| tool Montador Vertical 2 | `0a949867-f37f-4808-b178-4478edc7b5ad` | **constante** |
| project | varia | **um por sessao**, de proposito |

O projeto e' diferente por sessao por ordem do operador: *"pra nao sobrecarregar
um projeto com muitas midias e atrapalhar o refresh"*.

⛔ **O script NAO concatena o que foi colado.** As urls dele vinham com o
segmento de idioma inconsistente (uma sem `/pt/`, o resto com). Ele **extrai o
id do projeto** e reconstroi as tres urls de um molde unico. Testado contra as
quatro urls reais + dashboard com query + lixo colado por engano: 7 de 7.

⚠️ **As duas janelas nascem NOVAS** (`Ctrl+N`). O F10 faz `Ctrl+1` e conta a
partir da primeira aba: abrir as abas numa janela que ja' existia deixaria a
aba 1 sendo uma antiga, e o piloto varreria a bancada errada.

⭐ **Depois do F3 a sessao tem tres janelas com o MESMO titulo** (o nome do
perfil no Dolphin). Por isso o F3 guarda o handle da janela do AdBatch, e o
seletor do F10 a marca com `<-- montada pelo F3` e ja' vem com o numero dela
preenchido.

⚠️ **O preview do popup e' a defesa contra abrir 16 abas erradas**: ele mostra as
urls DERIVADAS antes de qualquer clique.
