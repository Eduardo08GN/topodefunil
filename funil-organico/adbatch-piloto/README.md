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

### F3 — os dois monitores (2026-08-11)

Encomenda do operador com a bancada montada na frente dele: *"a janela 2 fica
full screen no meu segundo monitor vertical, a janela 1 full screen no monitor 1
horizontal"*.

⛔ **Monitor nao e' escolhido por NUMERO.** A numeracao do Windows muda quando se
troca um cabo de porta, e um numero trocado joga as dez abas do AdBatch no
monitor de retrato — onde a calibracao do F10 nao vale. A escolha e' por
propriedade:

| janela | criterio | fallback |
|---|---|---|
| 1 (AdBatch) | o monitor cuja **area util casa com `calib_w` x `calib_h`** — e' literalmente a tela onde os 6 pontos foram apontados | o monitor em **paisagem**, depois o 1 |
| 2 (dash + montador) | o monitor em **retrato** (altura > largura) | qualquer outro que nao o da janela 1 |

Medido nesta maquina: monitor 1 = 1920x1080 paisagem (util 1920x1032, primario),
monitor 2 = 1080x1920 retrato em (1920,-401). O `.ini` confirma a calibracao no
horizontal: o ponto mais distante e' (1171, 772), que so' cabe no monitor 1.

⚠️ Override, se a heuristica errar um dia: `[config] monitor_adbatch=1` e
`monitor_dash=2` (0 = automatico).

⛔ **Restaurar -> mover -> maximizar** e' a unica ordem que funciona: janela
maximizada IGNORA o `WinMove` — ela pertence ao monitor em que foi maximizada.

⭐ O popup ja' mostra em que monitor cada janela vai cair, e o aviso final
compara a janela 1 com a calibracao — descobrir a divergencia agora custa um
clique, descobrir no F10 custa a rodada.

### ⛔⛔ O defeito do AUTOCOMPLETE (medido em campo, 2026-08-11)

Primeiro teste real (sessao CTA-03 Neusa): a janela 2 abriu **5 abas do AdBatch**
onde devia abrir o dashboard. A causa nao era a url — era o **autocomplete inline
do Chrome**, e a forma das urls diz qual delas era vulneravel:

```
dash    = .../project/<pid>
adbatch = .../project/<pid>/tool/d882542c-...
```

A do dashboard e' **prefixo estrito** da do AdBatch, e e' a **unica das tres** com
essa propriedade — exatamente a unica que falhou. Digitado o prefixo, o Chrome
pendura o resto como texto SELECIONADO (aquela url tinha acabado de ser visitada
DEZ vezes) e o `Enter` navega para o completado.

⭐ Conserto: `{Delete}` entre o texto e o `Enter`, em **todas** as navegacoes.
Quando nao ha' nada pendurado o cursor esta' no fim e a tecla nao faz nada.

⚠️ **E o preview nao mostrava a linha do dashboard** — a unica das tres que deu
errado era a que a defesa nao exibia. Defesa que nao cobre todos os itens que ela
defende da' a sensacao de conferencia sem a conferencia. Corrigido: as quatro
linhas aparecem.

⭐ A url do dashboard deixou de ser deducao: o operador colou as tres de sessoes
diferentes e as tres sao `.../project/<pid>` puro, com "Todas as midias"
selecionado.

### ⭐⭐ O F3 FOI EXECUTADO DE VERDADE (2026-08-11)

AutoHotkey **v2.0.19 esta' instalado** (`C:\Program Files\AutoHotkey\v2\`) — o
relatorio anterior dizia que nao, sem ter checado. Isso muda o que da' para
provar, e o que se provou:

| teste | como | resultado |
|---|---|---|
| sintaxe das 1083 linhas | o v2 parseia o script INTEIRO antes de executar a 1a linha, entao carregar e' validar | carregou residente, stdout/stderr vazios |
| monitores | `MonitorGetWorkArea` real | m1 1920x1032 paisagem · m2 1080x1920 RETRATO em (1920,-401) |
| `monitoresDaBancada()` | funcao REAL via `#Include`, com o .ini dele | janela1 -> m1 · janela2 -> m2 |
| `idDoProjeto()` | as 3 urls de dashboard + tool sem `/pt/` + lixo | 5 de 5 |
| **`mandarPara()`** | Notepad descartavel, comecando MAXIMIZADO no m1 | 1936x1048 em (-8,-8) -> **1096x1936 em (1912,-409)**; centro dentro do m2, retrato, saltou de tela, notepad fechado |

⛔ O teste usa `#Include` do script real, **nao copias das funcoes**: uma copia
poderia passar aqui e o original falhar la'.

#### O defeito que so' a execucao mostrou: tolerancia de 12 contra borda de 16

`calib_w`/`calib_h` vem do `WinGetPos` (ver `calibrar()`), e janela **maximizada**
reporta a area util **mais a moldura invisivel**:

```
MonitorGetWorkArea .... 1920 x 1032
WinGetPos maximizada .. 1936 x 1048     <- 16px em cada eixo
```

Com a tolerancia de **12** que estava no `monitorPorTamanho`, o criterio
**principal** da janela 1 nunca casaria: cairia calado no fallback de paisagem.
Nesta maquina o resultado seria o mesmo monitor, e o defeito so' apareceria em
outra. Tolerancia agora e' **24**, com os numeros medidos no comentario, e o
teste checa `monitorPorTamanho(1936,1048)` — o valor que a calibracao de fato
grava, nao o que a area util reporta.

⚠️ **O que ainda nao foi executado:** o F3 de ponta a ponta numa sessao real
(Gui, `Ctrl+N`, o `{Delete}` na barra, as 16 abas). O que se provou foi cada peca
isolada e o posicionamento de verdade.

## ⭐⭐ F1 ajuda · F4 e o clique no icone (2026-08-11)

### O mapa dos atalhos

| tecla | o que faz |
|---|---|
| **F1** | ajuda: os atalhos **e o estado atual** do script |
| **F3** | monta a bancada (2 janelas, 16 abas, uma em cada monitor) |
| **F4** | levanta a bancada: traz as duas de volta, cada uma no seu monitor |
| **F8** | ensaio seco — roda sem colar e sem gastar credito |
| **F9** | calibrar os 6 pontos |
| **F10** | RODAR — o gatilho da geracao |
| **F12** | log |
| **Esc** | abortar (so' enquanto roda) |

Os mesmos comandos estao no **menu da bandeja**. Atalho serve a quem ja' sabe;
menu serve a quem esta' descobrindo — e um dos dois some depois de duas semanas
longe do script.

⛔ A tela do F1 tem **duas metades**, e a segunda e' a que faltava em todo lugar:
os atalhos, e **como o script esta' agora** (monitores, para onde vai cada
janela, abas, calibracao, bancadas montadas, clique ligado ou nao). Saber que o
F9 calibra nao ajuda quem nao sabe se *esta* calibrado.

### O clique no icone da sessao

Ordem do operador: *"de uma acao de um clique unico no icone do navegador de
determinada sessao logada, fazer abrir simultaneamente a janela 1 e 2 daquela
sessao nos seus respectivos monitores"* — e *"pode colocar as duas rotas, por
clique no icone e por apertar o F4"*.

⛔ **Nao da' para ouvir o botao da barra de tarefas** — ele e' do Explorer, nao do
navegador. O que da', e produz o mesmo efeito, e' ouvir a **consequencia**: o
clique ATIVA a janela, e o Windows avisa quem estiver registrado como shell hook
(`HSHELL_WINDOWACTIVATED` e `HSHELL_RUDEAPPACTIVATED` — o segundo e' o que chega
quando a janela vem de minimizada, que e' justamente o caso do clique).

⛔⛔ **A regra que impede isso de virar praga: so' age se a irma estiver
MINIMIZADA ou FORA DE LUGAR.** Sem ela, alternar entre as duas janelas com
alt-tab traria a outra para a frente toda vez. Com tudo ja' no lugar, o certo e'
nao fazer nada. Desligavel: `[config] clique_no_icone=0`.

⚠️ Tres guardas, cada uma por um motivo diferente: `rodando` (nunca durante o
F10/F3 — ele pediu "em standby"), `gArrumando` (reentrancia: arrumar ATIVA
janela, ativar dispara o hook de novo) e uma carencia de 1,5s (o Windows manda
mais de um evento por clique).

### Uma bancada por sessao, sem lista no codigo

*"funcione para as quatro sessoes, ou quantas vierem no futuro"*. Cada F3 grava o
par de janelas na secao `[bancadas]` do INI, com o **titulo da sessao como
chave**. Conta nova no Dolphin = chave nova no dia em que ela rodar o F3; nada no
codigo precisa ser editado.

⛔ O Windows **recicla handle**, entao toda leitura confere que as duas janelas
ainda existem — sem isso, uma janela qualquer herdaria a bancada de outra sessao
e o F4 arrastaria a janela errada.

### Medido em execucao (nao em leitura)

14 de 14, com **duas janelas criadas e destruidas pelo proprio teste**:
ajuda abre e lista os 8 atalhos + as 7 linhas de estado · gravar/achar/validar
bancada · levantar poe cada uma no seu monitor maximizada · **o foco volta para a
janela clicada** · **com tudo no lugar nao age** · **com a irma minimizada volta
a agir** · bancada morta some sozinha da lista.

⛔⛔ **Cobaia se mata pelo HANDLE, nunca pelo nome do processo.** No dia desta
entrega um `Stop-Process` por nome, escrito para limpar o Notepad de um teste
meu, fechou **dez Blocos de Notas do operador**, sete com alteracao nao salva — e
o do teste ja' tinha fechado sozinho. Nao havia nada meu para limpar.

### ⭐⭐ As quatro telas no mesmo dialeto (2026-08-11)

Segunda ordem do operador sobre a MESMA janela: *"eu te pedi pra melhorar a ui ux
de TODAS as janelas interfaces do script, vc ainda deixou essa daqui crua,
confusa"*. Ele estava certo — eu tinha refeito o seletor e a ajuda e deixado
justamente a **primeira tela que ele ve'**.

⛔ O que fazia parecer confuso nao era cada tela isolada, era serem **tres
dialetos**: uma pedia numero digitado, outra era paragrafo cinza, o log era um
MsgBox despejando texto. Fonte, margem, largura e o lugar dos botoes mudavam de
uma para outra — e isso obriga a reaprender a tela a cada vez.

Toda janela agora nasce de `janelaUI()` + `secaoUI()`. Nao e' economia de linha:
e' o que garante que o **proximo** dialogo tambem saia igual, em vez de depender
de eu lembrar as medidas.

**A tela do F3, item por item:**

| estava | ficou |
|---|---|
| campo de url sem rotulo | secao `1 · a url do projeto desta sessao` |
| paragrafo cinza corrido | secao `2 · o que vai ser montado`, em tabela |
| preview VAZIO ate' colar | tabela ja' nasce com janela/monitor/abas/ferramenta; so' a coluna da url completa ao colar |
| nada dizia o que faltava | linha de estado: vermelha sem url, verde com o id do projeto |
| botao sempre clicavel | **nasce travado**, libera so' com url valida |

⚠️ E o log deixou de ser MsgBox: agora tem rolagem, ordem **mais novo em cima**,
o caminho selecionavel e um botao que abre a pasta. Numa ferramenta em que o log
e' a unica prova do que aconteceu, ele nao pode ser a tela mais pobre do script.

#### Medido abrindo as quatro e conferindo cada controle

`0 controles fora da janela` nas quatro, e todas em **752px** — antes o log saia
com 826. ⛔ A causa da unica divergencia vale a nota: **caminho de arquivo nao vai
em `AddText`**. O caminho e' um token sem espacos, um Static nao consegue
quebra-lo, e o AHK **alarga o controle e a janela junto** — a tela do log ficou
74px mais larga que as outras tres, que era exatamente a inconsistencia que se
estava consertando. Um `Edit` respeita a largura pedida.

⭐ O teste tambem prova o comportamento, nao so' o desenho: o botao **Montar**
comeca travado, libera com url valida, e as tres urls derivadas aparecem na
tabela antes de qualquer clique.

### ⭐ Tela de abertura (2026-08-11)

O script subia mudo. Agora abre a **mesma tela do F1** com cabecalho e uma caixa
de *nao mostrar ao iniciar* — nao uma segunda tela parecida. ⛔ Duas telas quase
iguais divergem no primeiro conserto que so' uma delas receber, e a que fica para
tras e' sempre a que o operador ve'. Desligavel na propria tela; `[config]
tela_inicial=0`.

### ⛔⛔ O .EXE NAO SAIU, e o motivo importa

Pedido: *"consegue criar um executavel pro script e uma tela inicial bonitinha
pra ele?"*. A tela saiu. O executavel **nao**, e a tentativa merece registro para
ninguem repetir:

O **Ahk2Exe nao esta' instalado** nesta maquina — so' o interpretador v2.0.19,
sem compilador e sem base files. A saida tentada foi fazer o que ele faz num
build sem compressao: copiar o `AutoHotkey64.exe` e embutir o script como recurso
RCDATA `>AUTOHOTKEY SCRIPT<` via `BeginUpdateResource`/`UpdateResource`.

⚠️ **O recurso entrou** (conferido com `FindResource`: 73086 bytes, nome e tipo
certos) **e o interpretador ignorou.** O `AutoHotkey64.exe` avulso do v2.0 nao
procura script embutido; quem faz isso e' o **base file** que vem com o Ahk2Exe.

⛔⛔ **E o teste quase mentiu que funcionava.** O `mini.exe` de prova rodou o
script — mas por coincidencia: um exe do AutoHotkey sem argumentos procura um
`.ahk` com o **nome dele** na mesma pasta, e o `mini.ahk` estava do lado. O que
denunciou foi `A_IsCompiled = 0` e o `A_ScriptFullPath` apontando para o `.ahk`,
nao para o exe. A prova definitiva foi copiar o exe para uma pasta **sozinho**:
la' nao rodou nada.

⛔ Pelo mesmo motivo o `piloto-adbatch.exe` gerado foi **apagado**: naquela pasta
ele "funcionava" so' porque o `.ahk` estava ao lado — e, pior, ao subir com
`#SingleInstance Force` ele **matou a instancia que o operador tinha rodando**.
Executavel que depende do arquivo que ele deveria substituir e' uma mentira com
efeito colateral.

⭐ Para ter `.exe` de verdade falta **instalar o Ahk2Exe** (componente opcional
do proprio instalador do AutoHotkey). Decisao do operador — envolve baixar.

## ⭐⭐ VIDEO TERMINATOR BY EDDIE — o .exe e o tema escuro (2026-08-11)

Batismo do operador: *"nomeie o programa como Video Terminator by Eddie"*.
⚠️ **So' o nome VISIVEL mudou.** Os arquivos seguem `piloto-adbatch.ini`, `.log` e
a pasta `roteiros\` — renomear o `.ini` apagaria a calibracao dos 6 pontos e
renomear a pasta esconderia os roteiros gravados. Nome de produto e nome de
arquivo sao coisas diferentes, e so' o primeiro foi pedido.

### O executavel saiu

O **Ahk2Exe foi instalado** pelo instalador oficial que ja' vinha com o
AutoHotkey (`UX\install-ahk2exe.ahk`, que baixa do repositorio oficial
`AutoHotkey/Ahk2Exe`) — autorizado pelo operador. Compilado com o proprio
`AutoHotkey64.exe` como base.

⛔⛔ **E desta vez o exe foi provado SOZINHO NUMA PASTA VAZIA**, porque a
armadilha ja' cobrou uma vez: um exe do AutoHotkey sem argumentos procura um
`.ahk` **com o nome dele** na mesma pasta, entao um teste feito ao lado do fonte
passa sem provar nada. Medido na pasta isolada: a tela de abertura abriu dentro
do PID do exe, com os **8 atalhos** listados, e o processo ficou residente depois
de fechar a tela.

`Video Terminator.exe` · 1.310.208 bytes · ProductName `Video Terminator` ·
FileDescription `Video Terminator by Eddie` · versao 1.0.0.0.

⚠️ O exe le' o `piloto-adbatch.ini` e grava o `.log` **na pasta dele** — por isso
ele mora na PILOTO-ADBATCH, junto do resto. E' o mesmo programa: rodar o `.exe` e
o `.ahk` ao mesmo tempo poe **dois donos nos mesmos atalhos**. Um ou outro.

### Tema escuro, lido do Windows

⛔ Nao e' gosto: **todas** as telas do operador sao escuras — Windows, Chrome,
Flow, Dolphin. Uma janela branca no meio disso e' a unica coisa que pisca, e ele
passa o dia olhando para elas. Conferido na maquina: `AppsUseLightTheme = 0`.

⚠️ O tema e' **lido do Windows**, nunca cravado — quem voltar para o claro nao
herda um dialogo preto. Campos (`Edit`, `ListView`) **nao herdam** o `BackColor`
da janela e sao pintados um a um: janela escura com buracos brancos e' pior que
tudo claro. A barra de rolagem e as bordas vem do `uxtheme` por ordinais **nao
documentados** (135/136), e por isso dentro de `try`: numa build do Windows em
que sumirem, a janela sai clara em vez de o script morrer na partida.

⭐ E `Esc` fecha qualquer dialogo. E' o reflexo de todo mundo, e sem isso o
operador caça o botao Cancelar com o mouse.

### Medido depois de tudo isso

`0 controles fora da janela` nas quatro telas · abertura em 752x600 com o titulo
`Video Terminator by Eddie` · botao Montar **travado** sem url e **liberado** com
url valida · 16 de 16 nas bancadas/F4 · o exe rodando sozinho numa pasta vazia.

### ⛔⛔ O F4 nao funcionava, e a culpada era a minha propria guarda (2026-08-11)

Relato do operador: *"infelizmente o mecanismo de abrir as duas janelas da sessao
de uma vez so' nao funciona"*.

**Todos os elos da corrente estavam bons** — medidos um a um contra o INI real:
o par gravado (`CTA - 03 Neusa=4070014,3866962`), as duas janelas vivas, o
`RegisterShellHookWindow` retornando OK, a mensagem `SHELLHOOK` registrada
(49193), **10 ativacoes recebidas** e o `lParam` batendo com as janelas.

⛔ O unico elo que reprovava era esta regra, escrita por mim como protecao:

> so' age se a irma estiver MINIMIZADA ou FORA DE LUGAR

**As janelas dele nao estao minimizadas.** Estao maximizadas, cada uma no seu
monitor, apenas **ATRAS** de outras. A guarda concluia "esta' tudo no lugar" e
saia calada. Eu otimizei contra um incomodo de alt-tab e matei o caso principal.

⭐ **E o incomodo que ela evitava nao existe neste layout**: as duas janelas ficam
em **monitores diferentes**, entao erguer a irma nunca cobre a que ele clicou. A
geometria ja' resolvia o que a guarda tentava resolver.

⚠️ Do original ficou so' a **economia**: janela ja' maximizada e no monitor certo
e' apenas **erguida na ordem Z** (`WinMoveTop`), sem restaurar, sem mover e sem
roubar o foco. O caminho caro (restaurar -> mover -> maximizar) ficou para quem
esta' minimizada ou fora de lugar.

⛔⛔ **E o teste afirmava que o defeito era o certo.** Havia uma linha
`ok("com tudo no lugar, NAO age de novo", ... = false)` passando feliz. Teste que
codifica a suposicao errada nao protege de nada — passa exatamente quando o
produto falha. Agora o teste **reproduz o cenario dele**: uma janela intrusa
cobrindo a irma, e a conferencia e' a ORDEM Z medida antes e depois (irma 3 -> 2,
intrusa 1 -> 3), mais o foco continuar na janela clicada e a irma nao sair do
lugar. 20 de 20.

### ⛔⛔ O CARIMBO DA BUILD — o conserto que nao estava rodando (2026-08-11)

Tres vezes no mesmo dia o operador reportou que um conserto *"nao funciona"*, e
nas tres a correcao **simplesmente nao estava em execucao** — ele tinha uma
instancia antiga de pe'. O ultimo caso, medido: o `.ahk` rodando desde **17:20**,
a correcao gravada **17:40**, o clique dele **17:43**.

⭐ Um programa residente, reiniciado varias vezes ao dia, tem de responder
sozinho **"qual versao sou eu"**. A tela do F1 abre com:

```
esta build .......... 11/08/2026 17:48  ·  executavel
```

⚠️ A data vem do **arquivo em execucao** (`A_ScriptFullPath`), nao de uma
constante que eu teria de lembrar de atualizar — constante esquecida mente com
mais confianca do que nao ter carimbo nenhum.

### ⭐ Sempre no system tray

Ordem: *"deixe sempre o terminator exe rodando de background no system tray"*.

⛔ **Atalho na pasta Inicializar, nao chave de registro em `Run`.** Sao
equivalentes para o Windows e nao para o operador: a pasta ele abre, ve' e apaga
sozinho. Automacao que so' o autor sabe desligar e' automacao que assusta.

O atalho aponta para o **.exe** mesmo quando quem roda e' o `.ahk` — o que ele
pediu para ficar residente foi o executavel, e o atalho descreve o futuro, nao o
processo atual. Ligavel/desligavel na propria tela de abertura e no menu da
bandeja (com marca de check).

⚠️ **Um dono por vez.** O `.exe` e o `.ahk` sao o mesmo programa e disputam os
mesmos atalhos. A instancia antiga do `.ahk` foi encerrada nesta entrega, e o
atalho de inicializacao aponta so' para o exe.

## ⭐⭐ F2 — a tecla de cada sessao, escolhida por ele (2026-08-11)

Duas ordens em sequencia: *"atribua uma tecla para cada sessao logada
identificada"* e, logo depois, *"coloca um ui ux pertinente para eu setar qual
tecla quero que seja trigger de cada par de janela"*.

⛔ A primeira versao cravava `Ctrl+Alt+1..9` no codigo. Funcionava — e a escolha
nao era minha. Quem decora atalho e' quem opera, e ele ja' tem atalhos na cabeca
de outros programas. Tecla cravada por mim vira conflito que so' ele descobre e
so' eu posso consertar.

⭐ **F2** abre uma linha por sessao com um **controle Hotkey nativo**: ele clica e
aperta a combinacao, e o proprio Windows escreve. Digitar o nome da tecla a mao
seria erro que so' apareceria na hora de usar.

**Isto conserta a fraqueza do F4**, que so' funcionava com a janela certa ja' em
foco — ou seja, exigia achar a sessao antes de pedir para acha-la. Com tecla por
sessao ele chama a bancada de onde estiver, inclusive de dentro de outra sessao.

### Cinco decisoes que sao protecao, nao enfeite

| | |
|---|---|
| chave do INI e' o **nome da sessao**, nao um numero de ordem | numero de ordem faria uma sessao nova **renumerar** as outras, e tecla que muda de dono sozinha e' pior que nao ter tecla |
| **registro dinamico** (`Hotkey()`), nao `^!1::` no fonte | trocar a tecla desliga a antiga **antes** de ligar a nova; duas teclas para a mesma coisa e' o comeco de uma nao responder |
| `chamadorDaSessao()` e' funcao **separada** | closure criada dentro do laco captura a variavel do laco, e **todas** as teclas acabariam chamando a ultima sessao |
| duas sessoes na mesma tecla e' **recusado antes de gravar** | a segunda venceria em silencio e a primeira pareceria quebrada |
| `migrarTeclasAntigas()` na partida | quem ja' tinha tecla no formato de slot a perderia em silencio na atualizacao, e acharia que o recurso quebrou |

⚠️ Sugestao inicial continua sendo `Ctrl+Alt+<n>` livre — e **nao** `Ctrl+<n>`,
porque o proprio piloto **envia** `^1`..`^8` para trocar de aba (`irParaAba`):
registrar Ctrl+1 poria o script para disparar a si mesmo no meio de uma rodada.

### Medido

19 de 19 no F2 (migracao, nome legivel da tecla, atribuicao, **troca sem deixar a
antiga viva**, levantar a sessao certa com o foco em outra, chamadores
distintos) · 21 de 21 nas bancadas/F4 · `0 controles fora da janela` nas cinco
telas.

⛔ **E a tela do F2 nasceu com 1252px de largura contra os 752 das outras.** Com
`y+10` sozinho o AHK mantem o X do controle ANTERIOR — que era o campo de tecla,
la' na direita. A segunda linha nascia depois dele, a terceira depois dessa:
escada, nao formulario. `x18` explicito em cada linha. So' apareceu porque a
medicao compara a largura das telas entre si.


### F2 lista TODAS as sessoes, nao so' as montadas (2026-08-11)

O operador abriu o F2 e viu uma linha so': *"achei que haveria identificacao
automatica de todas as sessoes logadas e seriam ja' elencadas ali"*. Depois ele
mesmo dispensou o reparo — mas ele estava certo, e o erro era de ORDEM: a tela de
ATRIBUIR tecla so' mostrava quem ja' tinha bancada, ou seja, exigia montar antes
de poder escolher a tecla, quando escolher a tecla e' o passo anterior.

Quatro fontes, sem repetir ninguem:

| ordem | fonte | por que |
|---|---|---|
| 1 | perfis do Dolphin **abertos agora** | e' o que ele ve' na tela |
| 2 | sessoes **esperadas**, mesmo fechadas | da' para atribuir a tecla antes de abrir o perfil |
| 3 | quem tem **bancada** gravada | inclui alvo que nao e' Dolphin |
| 4 | quem tem **tecla** gravada | nunca perder uma atribuicao |

⛔ Janela do **Chrome nao entra pelo titulo**: o titulo muda a cada aba, e uma
lista cujos nomes mudam sozinhos nao serve para amarrar tecla. Bancada montada no
Chrome entra pela fonte 3, com o nome que tinha na hora.

⭐ **O estado vai junto do nome** (`bancada montada` · `aberta — rode o F3` ·
`fechada`), e nao numa coluna: e' o que responde *"por que essa tecla nao fez
nada?"* no lugar onde a pergunta nasce.

⚠️ E as janelas sao enumeradas **uma vez**. A primeira versao chamava
`listarSessoes()` dentro do laco, varrendo todas as janelas do sistema por
sessao — barato com seis, e a lista dele vai crescer por decisao dele mesmo.

⛔ Nota de metodo: este proprio paragrafo foi escrito primeiro por um `python -c`
dentro do bash, e as **crases viraram substituicao de comando** — o texto entrou
no arquivo com tres buracos no lugar dos nomes de funcao. Texto com marcacao vai
por ferramenta de arquivo, nunca por linha de comando.

Medido: F2 lista as 4 sessoes do Dolphin + as bancadas, com estado em cada uma ·
752px como as outras telas · 0 controles fora · 19 de 19 no F2 · 21 de 21 no F4.

### A sessao principal do Chrome tambem e' uma sessao (2026-08-11)

*"Achei que o script fosse pegar a minha sessao logada padrao do Chrome fora do
Dolphin tambem..."*

Ele estava certo, e a razao de eu ter excluido era um problema **meu**: o titulo
da janela do Chrome muda a cada aba, e eu tinha usado o titulo como chave da
sessao. Chave instavel nao serve para amarrar tecla — mas a resposta e' dar ao
Chrome uma chave **estavel**, e nao deixar a sessao de fora.

⭐ `chaveDaSessao(hwnd)` e' o **unico** lugar que decide o nome de uma sessao:
Dolphin pelo nome do perfil (estavel), Chrome por um nome fixo. O F3 grava por
ela e a tela de teclas lista por ela — as duas nao tem como divergir.

⛔ E o **F3 passou a gravar por essa chave**, nao pelo titulo cru. Uma bancada
montada no Chrome ficaria gravada sob o titulo da aba ativa, que muda no minuto
seguinte: a tecla dela nunca mais acharia a sessao.

⚠️ **E o Chrome aparecia como `fechada` com cinco janelas na tela.** O
`listarSessoes()` so' aceita janela de Chrome com o Flow no titulo — regra certa
para o seletor do F10, errada nesta tela, que responde *"esta sessao existe?"* e
nao *"esta sessao esta' com o Flow aberto?"*. Duas perguntas parecidas, um filtro
so', e a resposta errada.

Medido: 5 janelas de Chrome com titulos diferentes -> **1 chave so'** · os
perfis do Dolphin mantiveram o nome · o Chrome aparece como `aberta — rode o F3`
· 752px, 0 controles fora · 19/19 nas teclas, 8/8 no worker, 0 fora nas telas.

## ⭐⭐ MODO SEQUENCIAL (2026-08-11) — o F10 roda em varias bancadas

Proposta do operador: *"um toggle que quando ativado, a automacao de geracao das
imagens acontece com todas as bancadas montadas em sequencia e, quando
desativado, percorre para cada uma bancada selecionada"*.

⭐ **O F3 e' o que tornou isto possivel**, e vale dizer por que: como ele poe a
janela 1 de **toda** bancada maximizada no mesmo monitor, a calibracao dos 6
pontos vale para todas. Sem isso, a partir da segunda bancada o piloto estaria
clicando no escuro — e a trava de geometria abortaria, no melhor caso.

**Como usar:** liga o toggle na tela do F1. O F10 (e o F8) passam a abrir uma
tela com as bancadas montadas, **todas marcadas**; voce desmarca as que quiser
pular e o total de videos aparece **antes** do botao.

### Quatro decisoes, cada uma com o motivo

⛔⛔ **Duas fases: as ABAS de todas primeiro, depois as RONDAS de todas.** Fazendo
bancada a bancada (abas→ronda, abas→ronda), a ronda da primeira aconteceria logo
apos ela. Do jeito que ficou, as imagens da bancada 1 ganham **de graca** todo o
tempo que as bancadas 2, 3 e 4 levaram para preencher — e a ronda existe
justamente para pegar o slot que ainda nao chegou. O ganho e' de **qualidade**,
nao de relogio.

⚠️ **Uma bancada que falha nao derruba as outras.** Cada uma roda no seu `try`;
o que der errado entra no relatorio do fim, com o nome e o motivo. Sem isso, uma
janela fechada na bancada 2 custaria as bancadas 3 e 4.

⚠️ **Esc aborta tudo**, nao so' a bancada da vez. Quem aperta Esc no meio de uma
automacao quer que ela pare, nao que pule para a proxima.

⛔ **O total de videos fica na tela ANTES do botao.** A diferenca entre 10 e 40
geracoes e' credito, e o numero tem de estar visivel antes do clique.

### ⛔ O laco das abas foi EXTRAIDO, nao copiado

`percorrerAbas()` serve aos dois modos. Uma copia divergiria no primeiro conserto
que so' uma delas recebesse — e a que ficaria para tras seria justamente a que
gasta credito. O teste cobra isso contando a ocorrencia de uma linha do laco no
fonte: **tem de ser 1**.

⚠️ E o `catch` do laco passou a **lancar** em vez de `return`: no modo sequencial
quem chama precisa saber que **esta** bancada falhou para seguir para a proxima.
Um `return` mudo abortaria as outras tres em silencio.

### Medido

Toggle liga/desliga · a tela lista as 3 bancadas de teste, **todas marcadas**, com
`3 bancada(s) · 30 video(s) no total` · 752px, **0 controles fora** · fechar sem
confirmar devolve zero · o laco existe **1 vez** no fonte · regressao: 0 fora nas
telas, 6/6 no Chrome, 19/19 nas teclas, 8/8 no worker.

⚠️ **O ciclo real nao foi executado** — isso gastaria credito do Flow e mexeria
nas janelas dele. O caminho de verdade e' o **F8 (ensaio seco) com o toggle
ligado**: percorre as bancadas de verdade, copia do agente, mas nao cola e nao
gera. E' o primeiro teste, e e' gratuito.

## ⭐ O DOOMGUY (2026-08-11)

*"Coloque o gif do doomguy na interface do Video Terminator by Eddie."*

⛔ **O AHK v2 mostra apenas o primeiro frame de um GIF** num controle Picture —
nao anima. O gif foi quebrado em **6 PNGs** na hora de empacotar
(`scratchpad/extrair_doomguy.py`) e a troca e' feita por timer, na cadencia
medida no original (480ms). O custo fica na ferramenta de build, nao no script
que roda o dia inteiro.

⚠️ **Recorte por BRILHO, nao por `getbbox()`.** O `getbbox` corta o que for
exatamente preto, e a tarja deste gif tem ruido de compressao: o resultado foi a
caixa cheia, 640x480, com a cara minuscula no meio de uma moldura. Com limiar de
brilho, a caixa util e' `(146, 9, 466, 468)` — 44x64 no fim.

⚠️⚠️ **Enfeite nunca derruba a ferramenta.** Se a pasta `doomguy\` nao estiver ao
lado do executavel, a funcao nao desenha nada e a tela abre igual. Uma cara
faltando nao pode custar o acesso ao F10.

⭐ E o **cabecalho passou a aparecer no F1 tambem** — antes so' a tela de abertura
tinha nome e subtitulo, e o F1 abria direto na tabela: duas telas com a mesma
funcao e caras diferentes.

### ⛔⛔ E o defeito que ele viu: 1408px em vez de 752

*"Ta sobrando muito espaco de um lado na interface, esta desequilibrado e feio."*

O doomguy e' posicionado com **X absoluto** (canto direito). No AHK, o controle
seguinte que use so' `y+N` **herda o X do anterior** — entao o titulo da secao
nascia la' na direita, com 700px de largura, e a janela crescia para caber. Todo
o conteudo espremido de um lado, o resto vazio.

⚠️ **E' a terceira vez que este mesmo mecanismo morde neste arquivo** (a tela do
F2, o caminho do log, agora o cabecalho). Por isso o conserto foi dentro do
`secaoUI()`, que **toda** tela usa, e nao no ponto onde apareceu.

### ⛔ Um teste meu destruiu o que veio testar

A primeira versao do teste usava `FileMove` para "esconder" a pasta e provar o
caminho sem frames. **`FileMove` nao move diretorio**: apagou os seis PNGs e
deixou um arquivo solto chamado `doomguy_off`. Os frames foram regerados do gif
original, e o teste passou a provar a guarda sem tocar na pasta de verdade.

Medido depois: **752x823**, imagem em (674,18) 44x64, **0 controles fora**,
sobreviveu a 2,5s de animacao (5 trocas) · regressao nas outras telas: 752 em
todas, 0 fora · chrome 6/6 · teclas 19/19 · worker 8/8 · sequencial 8/8.

### A faixa preta do topo (2026-08-11)

*"Consegue deixar uma tira preta (tipo cabecalho de fundo preto) no topo da
interface pra harmonizar com o recorte do background do gif do doom? Pode deixar
o background cinza da interface, achei bonito e confortavel visualmente pros meus
olhos."*

⭐ E' a solucao certa para um problema que eu tinha deixado passar: o doomguy tem
fundo **preto** e a janela e' **cinza**, entao a cara aparecia num retangulo
escuro colado num fundo claro. Em vez de tentar recortar a tarja do gif — que e'
o proprio HUD do Doom, nao um defeito — o fundo da **faixa** virou preto e o
recorte deixou de existir aos olhos. ⛔ O cinza do resto fica: ele disse por que.

⚠️ O AHK nao pinta regiao, pinta **controle**. A faixa e' um `Text` vazio com
`Background000000`, desenhado antes dos outros para ficar por baixo, e os textos
do cabecalho levam o mesmo fundo — sem isso cada um carregaria seu retangulo
cinza por cima da faixa.

⛔⛔ **A faixa nasce estreita e cresce depois do `Show`.** O AHK dimensiona a
janela pelo controle mais a' direita **mais a margem**: uma faixa ja' larga o
bastante para encostar na borda empurraria a janela +18px, e sobraria exatamente
a tira cinza que ela veio eliminar. Foi o que a **captura de tela** mostrou —
janela 770 com a faixa parando em 736.

### ⭐⭐ E o metodo que achou isso: capturar a tela, nao so' medir coordenadas

Todas as telas anteriores foram conferidas contando controles fora da janela.
Isso prova que nada caiu fora — **e nao prova** que a faixa ficou por baixo dos
textos, nem que a cara casou com o preto, nem que sobrou tira cinza na borda.

O `scratchpad/ver_tela.ahk` abre a tela, captura a janela por GDI+ e grava um
PNG. Medido nele, depois do conserto: faixa de **x=8 a x=743** (os 736 de area
util, borda a borda), preto `(0,0,0)` dentro e cinza `(32,32,32)` fora, doomguy
centrado (20px em cima, 18 embaixo).

## ⛔⛔ A BANCADA TROCADA DE MONITOR (2026-08-11) — a calibracao mentia

*"Deu um bug no script que ele trocou a janela 2 pro monitor 1 e a janela 1 pro
monitor 2 vertical."*

O `.ini` dele estava assim:

```
cr_slot2_x=1054                 <- os pontos no monitor 1 (0..1920)
calib_w=1096   calib_h=1936     <- a geometria da janela VERTICAL
```

**Os pontos e o tamanho gravado apontavam para monitores diferentes**, e quem
decidia o destino da janela 1 era o **tamanho**: `1096x1936` casa com o monitor
2, entao o AdBatch ia para o vertical e o dashboard para o horizontal.

### A causa: uma suposicao minha, escrita no comentario e falsa

A `calibrar()` gravava a geometria com `WinGetPos("A")` — a janela **ativa** no
fim do F9 — sob este comentario: *"grava a da janela que estiver ATIVA no fim da
calibracao, que e' onde o operador acabou de apontar os seis pontos"*. Basta ele
clicar noutra janela ao terminar e a frase deixa de valer.

### Tres consertos, e o primeiro e' o que importa

⭐⭐ **O monitor passa a vir dos PONTOS.** Eles sao coordenadas de TELA: o monitor
que os contem **e'** o monitor onde ele calibrou. Nao e' proxy nem heuristica —
e' o dado. Virou o primeiro criterio, antes do tamanho da janela. ⚠️ Por
**maioria** dos seis pontos: um ponto isolado fora da janela nao decide sozinho.

⭐ **A calibracao grava a janela SOB os pontos** (`WindowFromPoint` + `GA_ROOT`),
nao a que estiver ativa.

⭐ **O `.ini` errado e' consertado na partida.** Corrigir so' o codigo nao
bastaria: o dado errado continuaria no disco e a trava de geometria do F10
abortaria comparando a janela certa com o tamanho da errada. Quando os pontos e o
tamanho discordam, o tamanho e' recalculado da area util do monitor dos pontos
mais a moldura — e **fica no log**:

```
21:41:55  calibracao corrigida: os pontos estao no monitor 1
          mas o tamanho gravado era 1096x1936 — passou a 1936x1048
```

### E o efeito colateral: *"clico na janela vertical e ela se move sozinha"*

Nao era bug novo — era a correcao agindo sobre uma bancada montada **antes** dela,
com a janela 1 no monitor errado. Comportamento certo, e assustador: ele so'
descobria clicando.

⭐ O F1 passou a **avisar**, em vermelho, quais bancadas estao no monitor errado,
e a dizer o que resolve (a tecla da sessao, ou o F4). ⚠️ **Minimizada nao conta**
— janela minimizada reporta (-32000,-32000) e cairia no aviso todo dia, ate' o
aviso virar ruido.

⚠️ E o relato de *"a janela 2 esta num projeto diferente da janela 1"* nao se
confirmou: medido, ele havia comparado a janela 2 da bancada **Neusa** (projeto
cta03, no vertical) com a janela 1 da bancada **Chrome** (projeto main, no
horizontal) — duas bancadas, nao uma furada. O que confundia era justamente a
janela 1 da Neusa estar empilhada no vertical com a irma.

Medido: 10/10 no teste do monitor (com o INI quebrado dele reproduzido, o
conserto, a idempotencia e o caso "os pontos no retrato") · 5/5 no aviso ·
regressao: 0 controles fora, chrome 6/6, teclas 19/19, worker 8/8, sequencial 8/8.

### ⛔⛔ Tamanho igual nao e' tela igual (2026-08-11)

*"Investigar o porque que tem janela que ele esta errando o alvo e janela que
esta acertando."*

Medido nas capturas das janelas dele, pelo logo do AdBatch:

| janela | logo em |
|---|---|
| Dolphin (as tres) | y = **151** |
| Chrome principal | y = **117** |

**34 pixels.** A causa: as janelas do Dolphin mostravam a **barra de favoritos** e
a do Chrome principal nao. A barra empurra a pagina inteira para baixo. Como a
calibracao foi feita numa janela do Dolphin, no Chrome o botao `Gerar` estava em
769 e o piloto clicava em 803.

⛔ **E a trava de geometria nao pegava**: as duas janelas tinham exatamente
`1936x1048`. Tamanho igual, conteudo deslocado — o pior tipo de erro, porque
passa por todas as conferencias e falha em silencio gastando credito.

⭐ O ponto do botao `Gerar` separa os dois casos sozinho: medido, `(255,255,255)`
— branco, o botao — na tela certa, e `(14,14,14)` — fundo de pagina — na errada.
O F9 passou a gravar essa cor (`cor_gerar`) e o `prepararJanela` confere o pixel
antes de rodar, abortando com o motivo provavel escrito na tela.

⚠️ Tolerancia larga (80 por canal): o que se separa sao dois extremos, e apertar
isso transformaria um realce de foco em falso alarme.

⚠️ O operador resolveu a causa na raiz tirando a barra do Dolphin — todas as
janelas ficaram iguais. A trava fica para o dia em que uma delas divergir de novo.

### ⛔⛔ O modal que matava a rota sequencial (2026-08-11)

*"Quando uso F10 para percorrer todas as bancadas montadas, quando o script salta
de uma bancada pra outra, ele ta me pedindo o clique manual no OK; esse step esta
quebrando a finalidade da rota, que e' ser automatica."*

A `ronda()` terminava com um `MsgBox` de sucesso. Numa bancada so' isso e' um
aviso util; em **quatro em sequencia sao quatro paradas esperando um clique** — e
uma automacao que precisa de babá no meio nao e' automacao.

⭐ A `ronda()` ganhou `silencioso`, ligado so' pelo modo sequencial. O resultado
de cada bancada vai para o **log** e para o **relatorio unico do fim**, que ja'
existia. Aviso por bancada so' faz sentido quando a bancada e' o trabalho inteiro.

⚠️ **Eram TRES modais, nao dois.** Na primeira leitura eu achei o de sucesso e o
de "ainda ha' slot vazio". O terceiro — *"Lotes disparados. Ronda pulada (falta
calibrar a cor)"* — so' apareceu quando a conferencia percorreu a funcao inteira
por regex, em vez de eu listar os que lembrava. **Auditoria que conta o que o
autor lembra nao e' auditoria.** Os tres estao guardados.

⚠️ E o aviso de FALHA tambem e' calado no sequencial, de proposito: uma caixa de
erro no meio da fila para a fila inteira. Ele entra no log e no relatorio final.
