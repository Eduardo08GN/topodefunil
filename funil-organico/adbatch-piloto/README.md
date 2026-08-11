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
