# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# Topodefunil — instruções do projeto

Repositório de operação do funil orgânico de nutra (nicho ED, mercado US). É um repo
de **doutrina (Markdown) + scripts Python de sorteio** — não tem build, lint nem testes.
Os únicos "comandos" são os randomizadores (ver abaixo). No Windows use `python`,
nunca `python3`.

## ⭐ LEIA PRIMEIRO: [`WORKFLOW.md`](WORKFLOW.md)

Ponto de entrada do repo. Tem a operação inteira: as 5 páginas, o pipeline de
produção de criativo (randomizador → agente → AdBatch → Veo Editor → postagem), as
regras invioláveis, como expandir o repertório com `/watch`, o mapa de arquivos e as
pendências. **Nenhum trabalho começa antes de ler esse arquivo.**

## Duas engines de produção — escolha antes de escrever

São **paralelas e coexistem**; a PRISMA não substitui a V6. Cada uma tem seu agente,
seu randomizador e seu ledger:

| Engine | Quando usar | Randomizador | Agente | Ledger |
|---|---|---|---|---|
| **V6** (Kofi) | corpo comprovado, 1 história × N hooks — a variação inteira mora na cena 1 | `randomizador-v6.py` | `AGENTE_ED_ORGANIC_WAVE_V6.md` | `.ledger-v6.json` (gitignored) |
| **PRISMA V1** ⭐ | lote heterogêneo (10-50+) onde os vídeos são **distintos por construção** — 10 eixos visíveis + solver de distância | `randomizador-prisma.py` | `AGENTE_ED_PRISMA_V1.md` | `.prisma-ledger.json` (versionado) |

PRISMA é a frente de desenvolvimento atual (todo commit recente é dela). O agente
**executa** a linha sorteada — não escolhe, não prefere, não repete. Se o relatório do
PRISMA disser **REPROVADO (< 70% de pares distintos), o lote não é escrito** — rode de
novo com outra seed.

**Como nasce um agente novo** (garimpo -> leitura ótica -> mapa visual -> destilação
-> arquivo -> registro -> primeiro vídeo -> loop de campo -> **motor -> app -> .exe**):
[`PIPELINE-NOVO-AGENTE.md`](PIPELINE-NOVO-AGENTE.md). Ler antes de construir
qualquer agente novo.

## ⛔⛔ ESCOPO — SÓ EXISTEM OS `*_short.py` (2026-08-03)

> **Quando o Ed disser "os agentes" — melhorar, ajustar, medir, ler — ele está
> sempre falando dos SHORT.** Não pergunte qual.

Os **dezenove agentes** deste funil são os `<angulo>_short.py` em `funil-organico/`:
`clean` · `clean_v2` · `escandalo` · `troca` · `organicwave` · `ressurreicao` ·
`flagrante` · `pee` · `vazamento` · `necrose` · `exterior` · `colo` · `receita` ·
`botica` · `dupla` · `placa` · `cha` · `trio` · `falta`.
Três cenas de 8s, destino AdBatch Vertical 3.
**Cada um é autossuficiente e é a FONTE DA VERDADE do seu ângulo** — correção de
regra entra no `_short`.

⭐⭐ **E existe uma segunda família temporal desde 2026-08-08: o 16s** — hoje
com **trinta e um agentes nossos**, não mais um. **2 takes de 8s**, destino
**AdBatch Vertical 2**, ledger próprio cada um:

`trio16` · `dupla16` · `falta16` · `placa16` · `troca16` · `botica16` ·
`colo16` · `exterior16` · `escandalo16` · `ressurreicao16` · `flagrante16` ·
`pee16` · `necrose16` · `good16` · `bed16` · `wife16` · `fight16` · `alfa16` ·
`prato16` · `banho16` · `banho16_v2` · `mel16` · `organicwave16` ·
**`banho16_3t`** · `horse16` · `vick16` · **`vick2_16`** · **`gelahorse16`** ·
**`par16`** · **`descarte16`** · **`atem16`** ·
(+ `clean_v1_16s`/`clean_v2_16s`, do outro autor — 33 no total)

⭐ **`par16` e `descarte16` (2026-08-16) — DOIS agentes tirados de sete
vídeos, não sete.** Os 7 reels do lote de 16/08 são uma página rodando **um
script só**: o mesmo homem, a mesma embalagem, o mesmo líquido azul, o mesmo
`old blood blocking my flow`, o mesmo `comment gelatin`. ⛔ Quando mecanismo e
CTA não variam, o que separa um agente do outro é o **hook e o beat que ele
exige em quadro** — e por esse teste os sete colapsam em dois. O `par16` fica
com cinco (as duas peças anatômicas em pedestal cromado, o pó caindo **entre**
elas, e do narrador só as mãos); o `descarte16` sai inteiro do **v07** (o
frasco âmbar virado de boca para baixo sobre a lata de lixo, com a tigela da
receita esperando no mesmo quadro) e ⛔ **não tem prop fálico em quadro
nenhum**, o que é propriedade do ângulo e zera o custo de moderação dele.
⭐⭐ **A lente mais cara desse par não mede variedade, mede CONSTÂNCIA:** o
defeito dominante da fonte não é copy nem cena — a embalagem trocou de design
entre cenas em **5 de 7**, o copo mudou de silhueta em **4 de 7** e o par
evaporou ou mutou em **4 de 7**. Leitura ótica e decisão em
[`PROPOSTA-lote-16ago.md`](funil-organico/PROPOSTA-lote-16ago.md).

⭐⭐ **`gelahorse16` (2026-08-16) — os treze reels da Healthy Men's Guide, e a
CENA e o GESTO como dois eixos separados.** ⛔ **Não substitui o `horse16`**:
aquele saiu de **um** reel da mesma página (a bancada do bar de garagem), este
lê os treze. ⭐ **O take 1 sorteia a CENA** — 6 entradas, uma por reel lido
quadro a quadro — e **o take 2 sorteia o GESTO**, 4 entradas em pool própria:
24 combinações, todas medidas. ⛔ **Mas o ambiente vem sempre do take 1.** Se o
gesto arrastasse a cozinha dele junto, o segundo quadro mudaria de lugar no
meio do vídeo — o defeito que a âncora do IMAGE 02 existe para impedir.
⭐ **Toda fala é verbatim**, cada beat com o `v` do reel de origem.
⛔ **Menos a palavra do CTA, e isso é conserto**: dos 13 CTAs da fonte, **sete
pedem `yes` e três pedem `horse`** — as duas quebram a automação de DM. Nasce
em `gelatin`, trocável no campo de keyword da UI. ⛔ **Sem cavalo**, por ordem
— quem sustenta o nome é o rótulo da caixa, e a exceção ao P12 pesa por isso.
⚠️ **Três exceções em `DESLIGADAS`, todas por FIDELIDADE:** CT5 (a fonte nomeia
a receita em 13 de 13 — mesma hipótese do PRATO/MEL), **CT2 91%** (7 dos 10
hooks são a família **social**, `my wife was about to leave me`, e o regex lê
verbo de disfunção) e **CT6 75%** (1 dos 3 CTAs diz onde a receita chega).
⏳ **Dívida declarada: 7 dos 13 reels ainda sem leitura ótica** — pool cresce de
vídeo lido, nunca de invenção. **Medido: 0 ERRO em 400 sorteios, 24/24
combinações alcançáveis, 34 falas distintas no take 1 e 19 no take 2.**

⭐ **`vick16` / `vick2_16` (2026-08-15) — a pomada azul, e a lição mais cara da
semana.** O `vick16` nasceu com 7.153 linhas, pools de 100 entradas por eixo e
**0 ERRO em 600 sorteios** — e foi **reprovado olhando o vídeo**: *"as cenas
ficaram com muito elemento visual sem nexo e as copys completamente em drifting
copy"*. ⛔⛔ **Distinção medida não é nexo medido**: sete eixos empilhados, cada
PAR passando numa lente e o QUADRO INTEIRO nunca verificado — cem elementos
distintos viraram cem elementos **soltos**, enquanto a fonte varia praticamente
**um** (a superfície). Reconstruído pequeno e fiel no mesmo dia. ⛔ O `vick2_16`
é a segunda tentativa, com **cada cena dos 15 vídeos-fonte como pool do take 1**
e a **massagem** (região do corpo como eixo) que a fonte tem e a v1 ignorou.
⚠️ **E o `vick16` seguiu rodável e o operador gerou um lote inteiro com ele**:
os prompts diziam `with the phone in his free hand` e o gerador **desenhou o
telefone**. Consertado em 2026-08-16 — a câmera descreve o **ângulo**, nunca o
aparelho, e **sem** `no phone in frame`, porque negação injeta o token.
⛔ **Agente reprovado que continua executável é armadilha.**

⭐⭐ **`horse16` (2026-08-14) — a bancada do bar de garagem, e a primeira fonte
que já nasce em dois takes.** Nasceu por cópia literal do `banho16_v2`, que é o
parente **estrutural**: câmera sem rosto (só as mãos), `BLOCO 0 (REF)` que é uma
**foto das mãos**, marca em quadro por exceção ao P12, e o **gesto como eixo**.
O mundo é outro: sai o banheiro, entra o balcão — e entra **ela**, de toalha,
sentada atrás, sorrindo enquanto ele prepara (ordem do operador: *"sempre uma
personagem mulher sorrindo olhando pro cara preparando"*).
⭐ **O corte de take cai sozinho em ~8,5s** na fonte (reel 1038123865853645,
"Healthy Men's Guide", 69K views), entre o fim do beat da receita e o começo da
prova. Não houve colapso de cenas — houve tradução. Leitura ótica a **16 fps**,
275 quadros; mapa em [`concorrentes/horse-mapa-visual.md`](concorrentes/horse-mapa-visual.md).
⛔ **O CTA pede `gelatin`, não `horse`.** A fonte diz *"Comment horse"*, e a
palavra cadastrada na automação de DM é `gelatin`: pedir outra faz o comentário
entrar e a mensagem não sair. Mesmo motivo de `book` e `yes`.
⛔ **Sem cavalo, por ordem — e o preço está medido:** na fonte, um cavalo
pastando atrás do casal é o que fecha o sentido da palavra sem dizer nada. Sem
ele, quem sustenta o nome é o **rótulo da caixa** em quadro, e por isso a exceção
ao P12 aqui pesa **mais** que no `banho16`, onde o texto da marca sai embaralhado
de propósito. Lente `HO1` cobra a caixa nos dois quadros.
⭐ **A fala nomeia a receita** (`horse gelatin, lemon and cinnamon`) — e mesmo
assim mede **0% no CT5**. A razão vale para o parque: o `lint_copy16` cobra o CT5
na fala do **CTA**, e aqui os ingredientes estão no **take 1**. ⛔ Por isso ele
**não** entra em `DESLIGADAS`: exceção que não suprime nada é ruído.
⚠️ `half a lemon` da fonte virou `lemon` — a fala não paga o que o quadro mostra.
⏳ **O pool de AÇÕES nasce com CINCO, não generoso**, e é dívida declarada: ele
deveria sair de 13 reels da WellnessMSimple, cuja listagem é inalcançável
(geo-bloqueio, depois checkpoint da Meta). Cada entrada carrega **gesto nos dois
takes + os vasilhames + copy própria** (ordem: *"o pool de ações puxa copy tb e
universo"*), e o campo de copy está vazio nas cinco porque a fonte tem um script
para o vídeo inteiro. ⛔ Entrada nova sai de **leitura de vídeo**, nunca de
invenção.
⏳ **CT2 acusa 52%** — metade dos hooks é a falha **social** da fonte (*"my wife
was about to leave me"*) e o regex lê **verbo** de disfunção. O pool tem as duas
famílias de propósito, para a medição significar algo em vez de a copy se dobrar
ao regex. Mesma pendência do `organicwave16`. **Medido: zero ERRO em 400
sorteios, os 8 pools 100% alcançáveis, 0% em CT1/CT3/CT4/CT4b/CT5/CT6/CT7/CT8,
zero frase órfã em 800, zero drifting em 1.000 falas.**

⭐⭐ **`atem16` (2026-09-01) — a mancha pública em ALEMÃO, e o primeiro agente
que vende INFOPRODUTO.** ⛔ **Não é gelatina e não é ED**: a oferta é
`Begin To Breathe`, curso de breathwork de Corrina Holzner (Beamdream
Breathworks), 147 EUR, e o mecanismo único é **`Freemor Breathing®`** —
respiração consciente somada a **tremor neurogênico**, que a própria página
crava ser *"die einzige Atemtechnik dieser Art im deutschsprachigen Raum"*.
⭐ É o `gelatin trick` deste funil: nome próprio, proprietário, que a FAQ da
fonte diz não existir no YouTube. Lente `AT5` cobra o literal no take 3.
⭐ **A gramática de cena é a do PEE 16**, por ordem do operador — a mancha em
roupa clara, a plateia rindo E apontando, a vítima chorando e muda, e o dedo da
narradora na **mancha do tecido**, sem encostar (a construção que passou na
moderação depois das 4 recusas por agência). ⛔ **Elenco inteiro feminino**:
`SEXOS = ("mulher",)`, e o REF é uma coach **original** no arquétipo da
produtora — ordem dele: *"não é pra vc usar ela, mas sim alguém parecida"*.

⛔⛔ **A CAUSA DA MANCHA NÃO É ATAQUE DE PÂNICO, E ISSO É DECISÃO DECLARADA.**
O briefing pedia ataque de ansiedade; a página de vendas do produto **exclui
essa pessoa por escrito** em dois lugares (*"akuten psychischen Krise"* e
`Panikattacken` na lista de "fale com seu médico antes"). Vender contra a
contraindicação do produtor custa refund, o afiliado, e a Alemanha é o mercado
mais duro do mundo em alegação de saúde. ⭐ **A cena não perdeu uma vírgula** —
mudou a moldura para **sistema nervoso preso em alarme** e a promessa para
**regulação em minutos**, as duas copy da própria página. Lente `AT9` bane
diagnóstico e cura. ⚠️ Reversível em um pool, e a decisão é do operador.

⭐⭐ **O TETO DE FALA É EM SÍLABAS, E ESTE É O PRIMEIRO MOTOR DO PARQUE ASSIM.**
Os outros contam PALAVRAS porque em inglês as duas medidas andam juntas (~1,4
sílabas por palavra). Alemão tem ~1,7, e composto é pior — `Nervensystem` é
UMA palavra e QUATRO sílabas. ⛔ Um teto de 25 palavras em alemão autoriza fala
que não cabe em 8s, e fala que não cabe **sai cortada no render sem ninguém
ver** (§27). A unidade física é a sílaba: **35 em 8s**; palavra fica como rede
secundária (24). ⚠️ **E ele pegou o defeito na primeira rodada**: o take 3
saía com **59 sílabas** porque eu havia empilhado método + CTA + barreira num
take só. A barreira mudou para o fim do take 2, onde há folga.

⛔ **Três takes de 8s (24s), destino AdBatch Vertical 3** — mesmo formato do
`ruth16` e pela razão registrada por ele (*"2 takes fica muito suprimido as
copys"*), que aqui pesa mais: alemão gasta mais sílaba por ideia e esta copy
ainda precisa **apresentar um mecanismo com nome próprio**.
⛔ **A direção de cena continua em INGLÊS; só a linha `Dialogue:` é alemã**, e
o bloco `Voice:` declara alemã NATIVA — sem isso o TTS lê alemão com fonemas
ingleses. ⚠️ No Veo Editor, selecionar **`Idioma: Alemão`** no rodapé: a
legenda queimada nasce do Whisper sobre o áudio.
⛔ **Keyword `ATEM`**, editável no painel. ⏳ **Ela precisa ser cadastrada na
automação de DM antes do primeiro lote** — é o preço já pago com `book`, `yes`
e `horse`. ⏳ **E as cinco páginas do `ETNIA` são provisórias**: o operador
ainda não passou as páginas deste funil.

⚠️ **O que só apareceu LENDO O VÍDEO GERADO, com o autoteste já cravando
"0 ERRO em 400 sorteios":** quatro frases quebradas (`She is head bowed` sem
verbo, `crouched on one knee` duplicado, dois pontos faltando) e uma **frase
órfã em 100% dos vídeos** — a garantia de 14 dias caindo no take 2, antes de
existir oferta. **Medidor de pool não mede função.** Viraram as lentes `AT14`
(barreira de compra fora do take 2) e `AT15` (o hook carrega o elo com o
alarme, e nenhuma fala menciona filmagem). ⭐ A `AT15` existia só como
comentário acima do pool, e **uma das doze entradas já a violava** — molde que
não vira código é onde o vício mora.
**Medido: 0 ERRO em 400 sorteios, 12/12 pools alcançáveis, 31/30/30 sílabas de
teto 35, 9 controles negativos acusando 40/40, e a janela gerando as três falas
em alemão.**

⛔⛔ **E ELE ACHOU UM DEFEITO VIVO NOS AGENTES DO OPERADOR.**
`short_comum.aplicar_keyword` **contradizia a própria docstring**: ela diz
*"assumir `gelatin` para todos reescreveria uma exceção declarada em
silêncio"*, e o código nunca consultava a flag `_KEYWORD_EXPLICITA` que existe
exatamente para isso. Resultado medido, com o app recém-aberto e ninguém
tocando no campo: **os três BANHO tinham `Comment recipe` reescrito para
`Comment gelatin` a cada abertura**, revertendo em silêncio a ordem de
2026-08-13. ⚠️ Nos BANHO o sintoma é discreto (`Comment gelatin` é frase
plausível) e por isso durou; no ATEM era grosseiro (`Kommentiere gelatin`) e
apareceu na primeira sonda de janela. **Sete motores afetados**
(`banho16`, `banho16_v2`, `banho16_3t`, `raro16`, `ruth16`, `vick16`,
`vick2_16`) — consertados e **os sete `.exe` reconstruídos**, porque o exe leva
o `short_comum` assado dentro e conserto na fonte não chega a quem roda o exe.
⭐ E `trocar_keyword` passou a aceitar os comandos alemães (`Kommentiere`,
`Schreib`): sem isso o campo de keyword ficaria **mudo** neste motor.
**Medido bit a bit: 53 de 54 motores idênticos em 1.092 linhas de CTA — o único
que muda é o próprio ATEM, e muda de "não trocava" para "troca".**

⭐⭐ **`ruth16` (2026-08-21) — a humilhação pública no EMAGRECIMENTO, e a
TERCEIRA família temporal: 3 takes de 8s (24s).** ⛔ **Não é 16s e não é o
formato do `banho16_3t`** — lá são 3 takes de ~5s com teto de 14 palavras;
aqui são **3 takes de 8s com teto de 25**, o mesmo teto do 16s três vezes.
Destino **AdBatch Vertical 3**. O formato é ordem do operador com o motivo
escrito: *"2 takes fica muito suprimido as copys"* — o terceiro take existe
para **caber copy**, não para variar imagem.
⛔⛔ **É a primeira rota fora da gelatina depois do `raro16`**, e a única de
**emagrecimento**: CTA `recipe`, keyword editável no painel, e uma lente
própria bane a palavra `gelatin` do motor inteiro — o parque fala gelatina em
32 motores e a próxima copy colada traria a palavra junto.
⭐ Fonte: **"Ruth Yoder"** (`61589307140516`), 59 reels baixados e 58
transcritos. ⛔ **Só 15 entraram**, por ordem do operador (*"os vídeos que não
são de humilhação pública serão descartados como vídeo-fonte"*); a assinatura é
a **abertura** (`This was <NOME> before…`), não a presença da palavra —
⚠️ um regex largo pegava 15 vídeos de receita por falarem em `gym`/`doctor`/
`chair`. **A mediana da página é 48,5 comentários por mil views**; o melhor
reel que este repo já modelou fez 20,5, e era o topo.
⭐⭐ **A ÂNCORA DE CONTINUIDADE É A PEÇA DE ROUPA, não o rosto** — e é o achado
do v46. A mesma blusa **esticada e abrindo entre os botões** no corpo obeso e
**caindo solta e vazia** no corpo magro é âncora *e* prova de emagrecimento no
mesmo objeto, sem uma palavra de fala. Onde a fonte não tem essa âncora, ela
troca de pessoa escancaradamente (v27, v28, v38, v45).
⛔⛔ **E a âncora de ROSTO só cita traço que o peso não move**: olhos,
sobrancelha, ponte do nariz, orelha, sinal, cabelo, óculos. Maxilar, bochecha,
papada e queixo ficam **de fora** — citados, obrigam o gerador a escolher entre
a âncora e a magreza do take 2, e ele escolhe contra nós. O autoteste varre o
pool atrás dos termos proibidos.
⭐ **`rosto_ato1` é eixo 50/50 pré-selecionável, não palpite**: a fonte esconde
o rosto em 6 de 15 e mostra nos outros 9, e o único reel com testemunha em foco
é um dos que **mostram**. Quinze pontos não separam continuidade de
identificação; quinze vídeos de cada lado separam. Mesma mecânica do
`sem_mecanismo` do BANHO 16 3T.
⛔⛔ **A TESTEMUNHA é obrigatória em quadro**, e em 7 dos 9 desastres isso é
**correção** da fonte, não cópia dela: a leitura ótica achou **7 dos 15 reels
sem um terceiro em quadro**, seis deles prometendo `laughed at by the people
around her` na fala. Sem terceiro olhando, humilhação vira acidente. Bombeiro e
socorrista são testemunha de **autoridade**, nunca de **vergonha**.
⛔ **A palavra `filmed` saiu da copy**: ninguém filma em nenhum dos quinze e não
há aparelho em quadro em lote nenhum — escrever o aparelho faz o gerador
**desenhar** o aparelho, lição paga com um lote inteiro no VICK 16.
⚠️ **CT2 desligado, declarado**: este ângulo é de **peso**, não de disfunção —
a falha não é um verbo, é um **corpo** (a cadeira que racha, a rampa que vence
o marido), e o regex do CT2 lê verbo de disfunção masculina. CT4/CT4b não se
aplicam por **construção** (`NUCLEO` vazio), não por exceção.
⏳ **Duas dívidas declaradas, as duas de CENA e portanto do operador:** (a) o
**ato 3 é o ato 2 com outro gesto de mão** — mesmo lugar, mesmo enquadramento,
16s de varanda parada; um objeto só (o copo pronto, o papel dobrado) separaria
os dois, e é o único beat que o CT5 permite mostrar. (b) a **Ruth não tem
arquitetura facial** — 1 traço contra 5 de cada rosto sorteável, então a marca
da página vai derivar de vídeo para vídeo; inventá-la é trocar a marca.
**Medido: 0 ERRO em 400 sorteios, 13 pools 100% alcançáveis, 367/361/264 falas
distintas por cena, 25/25/25 palavras no teto, 0 déitico sujo em 1.718
sentenças, 0 frase órfã em 1.365, e os treze defeitos da varredura adversarial
zerados na saída montada.** Proposta e leitura em
[`PROPOSTA-ruth16.md`](funil-organico/PROPOSTA-ruth16.md) — ⚠️ escrita para
**2** takes, antes de o operador mudar o formato; o motor é a fonte da verdade.

⛔ **O `banho16_3t` está nessa lista por parentesco, não por formato.** Ele é o
único que **não** tem 2 takes de 8s: são **3 takes de ~5s**, destino **AdBatch
Vertical 3**, teto de **14 palavras por cena** contra 25. Bloco próprio abaixo.

⚠️ A lista dizia **dezoito** contando dezesseis nomes, e faltavam `necrose16` e
`wife16`. O `wife16` some da conta por engano fácil: o `bed16` nasceu como cópia
dele e o cabeçalho registra o *"renomeado"* — mas **os dois arquivos existem, os
dois têm `.exe` e eles divergiram em 1.622 linhas**. São dois motores, não um
renomeado. Contagem conferida por varredura de `funil-organico/*_short.py`
(2026-08-11), não a olho.

⭐ **`bed16` (2026-08-10) — a cama fria e a tigela.** (Nasceu como `wife16` e
foi renomeado no mesmo dia, por ordem do operador: o que nomeia o ângulo é a
cama, não a esposa.) Segundo motor do parque com **narrador homem** (o outro é
o `good16`) e o único cuja prova não é um corpo nem um prop. ⭐⭐ **A tigela é o
fio do vídeo**: no take 1 ela está **no colo dele**, sozinho, mexendo a mistura
âmbar com a colher, enquanto ela, vários pés atrás e de **braços cruzados**,
**encara** ele; no take 2 a **mesma tigela** está **nas mãos dela**, com os
cubos de gelatina, os dois colados dentro d'água. O mesmo objeto conta o antes
e o depois sem uma palavra. ⛔ A **profundidade de campo é a copy visual** do
take 1 — ele grande e nítido na frente, ela menor e suave atrás — e é pedida
explicitamente. ⛔ **Não tem prop fálico, e isso é propriedade do ângulo, não
esquecimento.** Um eixo só (a região) arrasta etnia + quarto + água + luz +
áudio + traje dela — 15 regiões dos EUA, mecânica do `falta16` fundida com a do
`good16`. ⭐ **MODO BELA** pelo contrato compartilhado: desligado entrega a
esposa realista do print (44-52 anos), ligado traz a REF do pool bela — e o
modo move idade, porte e traje dela **dentro da região sorteada**. ⚠️ A
doutrina mora no cabeçalho do motor: a **leitura ótica da fonte está pendente**
(reel 1752010159557238, que também não baixa sem login), então os pools de fala
são construção nossa sob o contrato, não verbatim.

⭐⭐ **`banho16` (2026-08-12) — o banheiro, e o primeiro agente SEM PESSOA.**
Modelado em **7 reels da página "Be yourself"**, lidos a 1 fps + transcrição,
mais a grade de 21 miniaturas. ⭐ É o primeiro ângulo do parque que acontece num
**banheiro** e o primeiro cuja câmera é **POV**: não há rosto, não há corpo, não
há prop fálico — o narrador existe **só pelas mãos**, e é nelas que a idade e a
etnia vivem. ⛔ Por isso o `BLOCO 0 (REF)` **é uma foto das mãos**: sem rosto,
elas são a única âncora de continuidade entre os dois takes.
⭐⭐ **A peça central é o INSTRUMENTO DE MEDIDA** — régua ou fita métrica —
parado em quadro do primeiro ao último segundo e **nunca tocado**. É a promessa
(`bigger`) virada objeto: a fala nunca diz **onde**, e quem fecha o sentido é a
régua. Régua não é palavra, então o classificador não tem o que pegar. Presente
em 6 dos 7 reels; lente `BA1`.
⭐ **O rótulo `growth hack`** (placa de papelão, post-it, papel colado) é
obrigatório e foi a única variável que separou os dois grupos da fonte: **média
de 108,5k views com ele contra 67k sem**, mediana de comentários 2.300 contra
374. Sete pontos é indício, não prova — mas custa nada e os dois melhores o têm.
⛔ **Quatro travas do contrato de 16s nascem DESLIGADAS**, cada uma com a ordem
do operador escrita no motor e declarada no `medir_copy16`: **CT1** (a fonte
termina no follow em 7 de 7), **CT2** (o ângulo não abre em falha — abre num
aviso ou numa idade, como o `alfa16`), **CT4b** (*"somente jonhson e manhood, e
não pecker, wiener e outras"*) e **CT8** (follow liberado). ⚠️ O que **não**
caiu do CT8 foi a razão: a DM sai igual, então o follow é **pedido e nunca
condição** — quem cobra isso é a lente `BA7`.
⭐ **`MODO PESSOA`, o quinto toggle da UI compartilhada, nasce DESLIGADO**: 1
reel em 7 tem gente, e o padrão é a ausência. Ligado, o take 1 vira o homem de
costas no espelho passando o creme na própria nuca — o único reel da fonte com
alguém em quadro (101k views).
⚠️ **A congruência com a VSL foi dispensada por escrito** (a receita alterna
bebida e pomada 50/50): *"não importa a congruência com a VSL, é apenas para
despertar o desejo de comentar e ir assistir a VSL"*. Registrado para ninguém
"corrigir" isso depois. ⛔ E a marca **pode** aparecer aqui, exceção declarada
ao P12 — a leitura ótica mostrou que os reels da fonte são **gerados por IA** e
o texto dos rótulos sai embaralhado, então a forma é reconhecível e o texto não
é legível: não se pede a marca ao gerador, ela vem sozinha.

⭐⭐ **`banho16_v2` (2026-08-13, do Ed) — o mesmo banheiro, com o GESTO como
eixo.** ⛔ **Não substitui o `banho16`** — os dois convivem, como o CLEAN v1/v2.
A diferença é arquitetural: onde o v1 sorteia peças de fala, este lê **13 pares
de gesto** nos mesmos 7 reels (rasga o sachê, abre a caixa, toca a caixa sob o
chuveiro, segura o pote, ergue o dedo com o creme, entra com a colher…) e faz
do **gesto** o que muda entre um vídeo e outro. ⭐ Os banheiros viraram **eixo
de região** (15, classe média para alta) e a receita ganhou **bicarbonato e
babosa**. ⭐⭐ **Três gestos carregam copy PRÓPRIA, verbatim da fonte** — o do
rodeio (*"falling like a lame horse in the middle of a rodeo"*), o do
`struggling`, e o do `hard` colado no órgão. ⛔⛔ **Esse último é uma exceção ao
CT7 de UMA AÇÃO, não do motor**, e por ordem direta do operador
(*"volte com o hard colado"*) contra o parecer da própria lente `BA6`: **o preço
está medido — verbo de ereção colado no órgão rendeu ~95% de recusa no COLO
16**. Se os renders desse gesto caírem, a causa candidata número um está escrita
lá. As outras doze ações seguem no registro leve.

⭐⭐ **`banho16_3t` (2026-08-14) — o mesmo banheiro em TRÊS takes de ~5s, e a
primeira família temporal nova desde o 16s.** ⛔ **Não substitui o `banho16`
nem o `banho16_v2`** — os três convivem. Ordem do operador: *"Resolvi criar a
partir de agora vídeos mais dinâmicos, com 3 takes de 5 segundos"*. O relógio
arrasta tudo: **teto de 14 palavras por cena** (número **medido por ele em
campo**, não estimado — *"posso gerar cada take com o limite de 6 segundos"*),
**3 imagens**, destino **AdBatch Vertical 3**.

⛔⛔ **Nasceu de uma hipótese do operador que a medição DESMENTIU.** Ele
diagnosticou *"a variação das combinações é sempre muito parecida uma com a
outra"*. Medido: os 9 hooks do `banho16` têm **12%** de sobreposição de
vocabulário e 4 aberturas distintas em 9; os 7 da fonte que ele preferiu têm
**14%** e 5 em 7 — e **duas das copies dele são idênticas palavra por palavra**.
⭐⭐ **O que separa não é a variedade, é a FORMA do hook.** Comentários por mil
views nos sete originais: **exclusão 20,5** · idade+hack 11,8/7,5/5,6 ·
confissão 8,1 · rodeio 6,4 · pergunta 4,0. ⭐⭐ **E o campeão é o único SEM
MECANISMO** — não explica nada, só avisa e promete. É o **CT5** (*a receita é a
moeda*) confirmado por quem nunca leu o contrato.
⚠️ **Mas n=7 e o campeão é único em três coisas ao mesmo tempo** (exclusão, sem
mecanismo, o mais curto): não dá para separar. **Por isso `sem_mecanismo` virou
EIXO PRÉ-SELECIONÁVEL no painel, não decisão** — 15 vídeos de cada lado e o
campo responde o que a fonte não responde. *Variável confundida vira eixo,
nunca palpite.*

⭐ **A copy é organizada em 12 FAMÍLIAS ATÔMICAS**, não em pools de beat. As três
cenas vêm juntas porque foram aprovadas juntas — o operador carimbou as doze uma
a uma e reescreveu seis na mão. ⚠️ **12 combinações nominais contra as 81 do
`banho16`, e mais diferença percebida**: lá 5 dos 9 hooks abriam com as mesmas
três palavras (**55% dos sorteios**). *Combinação nominal nunca foi a métrica.*
A lente **`BA9`** cobra que as três falas cheguem **verbatim** à linha
`Dialogue:` — copy aprovada não se reescreve no caminho.

⛔ **Decisões do operador que valem só aqui:** keyword **`RECIPE`** (a fonte
inteira pede Recipe — reverte o D2 do `banho16`); **`bat` e `pipe` liberados**
como apelido do órgão (decisão E3, tomada **ao aprovar a copy** — no `banho16`
V1/V2 a ordem D7 *"só Johnson e manhood"* continua de pé); e o **follow é o beat
compressível** do CTA (*"não é tão importante quanto o CTA, deve ser feita de
modo que não atrapalhe a quantidade de palavras"*).
⛔ O **`Segue primeiro`** que ele escreveu na família 6.2 **saiu por fato, não
por gosto**: *"a mensagem é enviada independente de seguirem ou não"* (10/08).
A lente `BA7` daqui é mais dura que a do irmão — pega `follow first`/`follow
before`, não só `follow or`.

⭐ **Sete melhorias de construção lidas na conversa que o operador teve com
outro agente**, e que o `banho16` não tinha: (1) a **reação borbulhante** como
payoff — mesmo prop, mesmo plano, muda o **verbo** (`afunda em fitas lentas` →
`ERUPCIONA`), contida abaixo da borda por ordem dele; (2) **três gestos
cronometrados** por take em vez de um; (3) **mãos ricas** com âncora fixa
(veias, nós, manchas); (4) a trava dos **dez dedos**; (5) o **banheiro
habitado** (barbeador, escovas, toalha amassada); (6) o **bloco de orientação em
graus** — lição paga por ele: `looking straight down` devolveu **vista aérea**,
e o que funcionou foi descrever a pessoa segurando o telefone; (7) **som e
deriva de câmera** variando por take.
⚠️ **E nem tudo dele veio junto**: os prompts do outro agente carregam
`not a celebrity`, que a ordem de 10/08 baniu; ele vazou template de outro
ângulo (um homem branco numa cozinha com mel no lugar do banheiro POV); vazou
copy de uma cena que não existia; e só respeitou o teto de palavras nos dois
últimos vídeos.

⚠️ **Dívida declarada:** a IMAGE 01 sai com **mediana de 370 palavras** contra
**239 da fonte**, e 12% das imagens passam do maior prompt dela (376). Cada
palavra acima veio de uma cláusula que o próprio operador pediu — o bloco de
orientação, os dez dedos, a âncora de mão, o banheiro habitado. Encurtar é
decisão dele, não minha.

⭐ **`good16` (2026-08-12, ajustado) — o casal na água.** Primeiro motor com
**narrador homem** e o único com **três** toggles. ⭐⭐ O `modo copy leve` é o
**primeiro toggle do parque que troca a FALA**, não quem aparece: ligado, a
fala 2 sai de `MISTURAS` para `MISTURAS_LEVE` e **não nomeia o órgão**. Nasce
desligado — é compra consciente de leveza, e o preço (a leitura "anabolizante"
que o operador reprovou) está declarado no código.
⛔⛔ **O MODO FORTE tem POOL PRÓPRIO, `HOMENS_FORTES`, 61-72 anos.** Ordem do
operador: *"sempre que travar a referência de forte mantenha o homem acima de
60 anos"*. ⚠️ E não dava para usar o `sc.ref_forte` compartilhado: ele tem 16
homens de **26 a 38**, nenhum acima de 60, e **cede quando a faixa não casa**
(`[...] or _pool`) — medido, `idade_min=61` devolvia 26-38 com o botão FORTE
aceso. Botão que promete 60+ e entrega 26 é pior que botão que não existe.
Mesmo precedente do `alfa16`. Lente `GO13`, com controle negativo que planta
exatamente esse homem de 34.
⛔⛔ **A mulher é sempre BRANCA, sempre 25** (era 24 até 2026-08-13), **sempre
no registro de beleza do TRIO/DUPLA** — 12 entradas, 4 ruivas · 4 loiras · 4
morenas, cabelo **molhado** porque a cena é dentro d'água. A idade é a constante
`IDADE_MULHER`, que a lente `GO14` lê — lente e pool não podem discordar. A
`GO14` cobra o **pool inteiro**, não só a entrada sorteada.
⛔⛔ **E a água é sempre PISCINA CHIQUE, de obra** (ordem de 2026-08-13:
*"nunca de plástico, ofuros, hidromassagem ou qualquer coisa do tipo"*). ⚠️ Isso
**reverte** a ordem de 2026-08-09 (*"sempre voltado pra piscina, jacuzzi"*) —
registrado para ninguém "consertar" de volta. Medido antes: **11 dos 15 mundos
violavam** (seis banheiras de hidromassagem, uma piscina **inflável** de
telhado, quatro armáveis — uma com `blue liner`). Lente `GO16`, que bane também
`steam` e `jets`: são a jacuzzi desenhada sem a palavra.
⛔ **E o CTA nunca marca horário** — `tonight` saiu, entrou `right now`. Ordem
de 2026-08-13: *"nunca deve especificar horário, deve dizer que vai receber
agora"*. Lente `GO17`. ⚠️ **A dívida é do parque**: a varredura achou `tonight`
ou `today` em CTAs de **20 motores**, ~70 linhas — copy, alçada do operador,
não varrida.

⭐⭐ **E a tarde de 2026-08-13 reescreveu metade do motor**, tudo por lote do
operador. ⛔ **A POSTURA virou eixo**: a posição dele estava cravada na frase
(`Sitting in <água>, submerged to his chest`), o que travava o agente em
piscina — numa espreguiçadeira ou numa sauna a frase é falsa. São **6 posturas**
(`dentro_agua` · `borda_sentado` · `espreguicadeira` · `sauna` · `praia` ·
`roupao`), cada uma com as quatro cláusulas de corpo, e o mundo diz qual usar.
⭐ **28 mundos** (eram 15) — jacuzzi de teca, hidromassagem de pedra, banheira
de mármore, sauna de cedro, praia privada, espreguiçadeira, cabana, cobertura,
spa coberto, chalé, solário, píer. ⚠️ Isso **reverte** o veto a água quente da
manhã do mesmo dia; o que sobrevive das duas ordens é **nada de plástico**.
⭐ **Pré-seleção de CENÁRIO no painel** — e a lente `GO21` cobra que todo
cenário exista nas **duas etnias**, porque travar `praia` numa página branca
devolvia 0/120 e o filtro cedia em silêncio: *botão que promete e entrega outra
coisa é pior que botão ausente*.
⛔ **Ela sorri sempre** (`GO22` implícita na string travada), com a cláusula
**positiva** do `alfa16` — nunca `not laughing`, porque negação injeta o token.
⛔ **O quarto de cima do quadro fica livre**, para o rosto não cair sob a
legenda queimada (medido no v006: as cabeças começavam em 20,7% e a legenda vai
até 21% — passava raspando).
⚠️ **E a recusa por conteúdo sexual foi resolvida por ACÚMULO, não por palavra**:
`bikini` aparece em 64/200 blocos do DUPLA e 56/200 do TRIO, e os dois passam.
O que saiu foi o composto `bare-chested`, a geometria de corpos colados
(`pressed against his side` → `shoulder to shoulder`), o busto nomeado e o
**vocabulário de formato de torso** dela (`hourglass`, `curvy`, `narrow hips`) —
a beleza mudou de endereço para altura, porte e rosto. ⭐ Isso **não** quebra a congruência do funil: aqui quem
fala é o HOMEM, e a etnia que a página governa é a dele.
⛔ **E por isso o `MODO_BELA` foi DESLIGADO neste motor** — não por gosto: o
`sc.ref_bela` entrega idades **21-33** (medido em 80 sorteios), então o botão
violaria os 24 anos em 11 de 12 vídeos. Reversível numa linha se a regra cair.

⭐ **`fight16` (2026-08-10) — a briga no quarto.** Terceiro motor do parque com
**narrador homem** (os outros são `good16` e `bed16`). No take 1 ele está **de
pé**, tronco nu, **toalha branca na cintura**, uma mão aberta se explicando
**para a lente**, enquanto ela, atrás, de **braços cruzados**, o encara — muda.
No take 2 os dois estão **colados**, e ⭐⭐ **ele carrega a prova nas duas
mãos**: a tigela de cubos de gelatina numa, a **caixa de bicarbonato** na outra
(o CT5 em quadro aberto — o lugar do ingrediente é a imagem, nunca a fala).
⭐ A copy é a da **fonte lida a 1 fps** (reel 1337455585246706), com a virada
que o operador escreveu à mão: `Struggling to stay hard? I thought it was just
age. But things changed when I discovered the gelatin trick.`
⛔⛔ **Foi o primeiro 16s com DOIS EIXOS DE CENA INDEPENDENTES** (o `alfa16`
herdou a arquitetura no mesmo dia), e é isso que o
separa do irmão estrutural `bed16`: lá os dois ambientes são da **mesma casa** e
vêm do mesmo eixo (a região arrasta quarto + água), aqui o operador ditou **duas
listas separadas** — 8 quartos da briga e os **10 ambientes do casal**, palavra
por palavra dele. Consequência em código: a continuidade **não pode exigir a
mesma casa**; o que atravessa o corte é **o mesmo HOMEM** (lente `FT3`), e a
`FT13` proíbe dizer `the same room/house` no take 2. ⛔ **Sem prop fálico** — a
prova é o casal. ⭐ **MODO BELA**: desligado entrega a mulher realista do print
(34-43), ligado traz a REF do pool bela. ⚠️ Nenhum pool de fala diz idade, e
isso é a pendência B do `bed16` impedida na origem. ⭐⭐ **A falsa causa do take
1 nomeia o órgão desde 2026-08-10** — ordem do operador lendo o app: *"«Struggling
to stay firm every night?» — firm WHAT?? my butt?? / «I thought age did that to
every man» — did that to WHO or to WHAT???"*. O nome entra na **falsa causa**,
nunca no hook: o CT7 vale por **sentença**, então o verbo de ereção fica numa e o
órgão na vizinha — o ouvido junta, o classificador não.
⛔⛔ **E essa sentença carrega `not`/`never` obrigatoriamente** — segunda
correção do operador no mesmo dia (*"tem que ter o NOT, senão não faz
sentido"*). A forma afirmativa (`I figured age was what killed my pecker`) só
funcionava se a virada a desmentisse, e **só 1 das 6 viradas desmente** (a que
abre com `But`). Como o sorteio cruza qualquer falsa com qualquer virada, em
**5 de 6 vídeos** o take 1 fechava *afirmando* que a idade matou o órgão — o
contrário do que a VSL vende. É o modo de falha do pool combinatório: cada beat
lido sozinho estava certo, e o **par** estava errado. O guarda ficou na lista
(negação em toda entrada), não no sorteio. Spec completa em
[`SPEC-FIGHT-16.md`](funil-organico/SPEC-FIGHT-16.md).

⭐ **`alfa16` (2026-08-10) — o aviso e as duas do lado.** Quarto motor com
**narrador homem**, e o **único do parque que não abre numa falha**. Os outros
dezoito abrem na mancha, no murcho, no *"struggling to stay hard"*; este abre
num **alerta brincalhão** (`If you have a wife, watch out.`) e fecha numa
**hipérbole paradoxal** — o truque funciona tão bem que **quem pede trégua é
ela**. O espectador se reconhece pela **esposa**, não pelo órgão.
⛔⛔ E isso tem consequência em código: **o `CT2` e o `CT6` são desligados neste
motor**, cada um com o motivo escrito. O CT2 exige que o take 1 enuncie a falha
— este ângulo, por desenho do operador, não enuncia nenhuma. O CT6 exige que o
CTA diga onde a receita chega, e a ordem foi literal: *"vc não usará complemento
tal como by message"*; as palavras liberadas foram para a **objeção da cozinha**
(`All ingredients you have in your kitchen`), que derruba o "vou ter de comprar
alguma coisa" — objeção que vem **antes** do custo social.
⚠️ O `medir_copy16.py` ganhou um mecanismo de **`DESLIGADAS`**: os dois números
continuam medidos e impressos, o motor sai da lista de "violam" e a decisão
aparece rotulada no rodapé. Gate que acusa uma decisão declarada treina o
operador a ignorar o gate.
⭐ **Dois eixos de cena independentes** (10 quartos × 10 ambientes, os dez do
take 2 ditados pelo operador), **as MESMAS duas mulheres** atravessando o corte
— três pessoas para manter idênticas entre dois quadros gerados separadamente, o
mais caro do parque — e ele com **a tigela numa mão e a caixa de bicarbonato na
outra**, sempre. ⭐ **MODO FORTE com pool próprio 50+**: o compartilhado do repo
tem 26-38 anos e não serve num ângulo cujo REF o operador travou em 50+; aqui o
toggle não troca a pessoa, troca **o corpo dela**. ⛔ Elas **sorriem**, nunca
gargalham — e a cláusula é **positiva**, sem `not laughing`, porque negação
injeta o token.

⭐ **`prato16` (2026-08-12) — o prato erguido e a cozinha de fora.** Quinto
motor com **narrador homem** e o primeiro cujo hook é um homem **sozinho** —
os outros quatro têm a esposa colada desde o primeiro frame. ⭐⭐ **A prova
não é um corpo, nem um prop fálico: é a RECEITA ACONTECENDO.** Take 1, ele
atrás da bancada erguendo um prato de cubos de gelatina com a colher e um cubo
ao lado do rosto, olhos arregalados; take 2, o **copo estendido na lente**,
braço esticado, e a **esposa aparecendo colada nele**, muda. ⛔ **O gole da
fonte foi cortado** por ordem do operador — o último frame fica na prova, não
na boca dele, e o TAKE proíbe o gole em texto (sem a cláusula o gerador o traz
de volta). ⛔⛔ **É o ÚNICO motor do parque que fura o `CT5`**: a fala nomeia
gelatina, limão e bicarbonato, como a fonte (reel 1709350110183701, 868
reações / **1,6K comentários**). Isso é **hipótese declarada**, não descuido —
a receita dita torna o pedido crível e o que a DM vende passa a ser o *como*.
Se o comentário cair neste ângulo contra os outros, a causa candidata número um
está escrita no motor e no `medir_copy16` (mecanismo `DESLIGADAS`). ⭐ A cor da
gelatina é **eixo sorteável** e atravessa três objetos (cubo, líquido, caixa) —
cubo verde virando bebida roxa é a incoerência que o espectador perdoa menos.

⭐ **`mel16` (2026-08-12) — o fio de mel sobre os cubos.** Irmão estrutural do
`prato16`: mesma cozinha de fora, mesmo casal, mesma arquitetura — e a
diferença é **um beat visual só**, de propósito. Dois motores irmãos existem
para isolar UMA variável; se tudo mudasse, o campo não saberia a que atribuir a
diferença. ⭐⭐ **O hook é o MEL CAINDO**: prato de cerâmica decorada numa mão,
squeeze de mel na outra, e um fio contínuo escorrendo sobre os cubos (a lente
`ME-MEL` cobra o FIO, não o frasco — frasco parado é embalagem na mão). ⭐ **A
regata preta** substitui a polo, e não é figurino: é o que põe braço e ombro em
quadro e dá ao **MODO FORTE** onde aparecer — aqui o toggle troca o **corpo**
(`CORPOS_FORTES`, super musculoso), nunca a pessoa, e o narrador é 61-72 nos
dois estados. ⭐⭐ **A pergunta de qualificação** abrindo a fala (`Struggling
with ED?`) é beat que nenhum 16s tinha, e ela **resolve o CT2 de graça**: o
`prato16` precisa declarar a exceção, este cumpre a regra (0% no gate). ⭐ **O
eixo TAMANHO, 50/50** — metade do lote promete tamanho como a fonte, metade
fica só na função; o preço (incongruência com o que a VSL vende + peso na
moderação) está declarado no motor. ⛔ Fura o **CT5** como o irmão, por ordem do
operador — os dois testam a mesma hipótese, e é o par que o campo vai comparar
contra os outros dezessete. Fonte: reel 1527794201990448, 21,1s, take único.

⭐ **Dois consertos no `good16` no mesmo dia:** (a) **MODO COPY LEVE**, o
primeiro toggle de **copy** do parque — ligado, a fala do take 2 deixa de
nomear o órgão e sai de um pool próprio; nasce desligado, e o preço (a leitura
"anabolizante" que o próprio operador reprovou em 10/08) está declarado no
código. (b) **O TIOZÃO FORTE**: `sc.REFS_FORTES` inteiro ia de 26 a 38 anos, e
por isso ligar "ref forte" num motor de narrador de 58 **trocava o homem por um
de 32** em vez de trocar o corpo dele. Entrou `sc.REFS_FORTES_MADUROS` (48-68),
**opt-in** por `ref_forte(..., maduros=True)` — nenhum dos outros 16 motores que
usam o helper muda (medido bit a bit em 20.000 chamadas).

⭐⭐ **`organicwave16` (2026-08-14) — o primeiro agente da operação em 16s.**
Nasceu por **cópia literal** do [`organicwave_short.py`](funil-organico/organicwave_short.py)
(`Copy-Item`, não redigitação), com cirurgia só no eixo temporal — os dois
convivem, formatos diferentes. ⭐ É o único 16s de **primeira pessoa** com
**elenco de aspiração** (o oposto dos especialistas: aqui o rosto vende) e com
**dois narradores possíveis** — no masculino o dono do problema fala de si, no
feminino a esposa conta e resolve escondido. ⭐⭐ **O quadro fundido** junta as
cenas 2 e 3 num só: a bancada com o copo, o sachê e a **isca** (o curiosity gap
que a copy nunca nomeia), e **o parceiro colado no ombro**, mudo, com o prop
ereto na mão livre. Sem isso o colapso comeria ou o mecanismo ou o payoff.
⛔ **A copy da cena 2 é NOVA, e por medição**: as `FUNDIDAS`/`CTAS`/`GATES` do
`_short` violam **cinco** das sete travas ao mesmo tempo (CT1 pelo `{gate}`
depois do CTA, CT5 pelo `fresh lemon` da receita na fala, CT6 por nenhum CTA
dizer onde a receita chega, CT7 pelo `gets your {o} hard again`, CT8 pelo pool
de follow inteiro). Os cinco pools ficaram no arquivo **com lápide**, e
melhorar qualquer entrada deles não muda um único vídeo. Os beats novos saem
das sentenças que o operador já aprovou em 2026-07-31, cortando só o proibido.
⚠️ **A receita saiu da fala e ficou no quadro** — e por isso `_recopiar_receita`
morreu: trocar o ritual no painel muda a imagem e mais nada.
⏳ **Pendência declarada, alçada do operador:** o **CT2 acusa 49%** dos
sorteios. Não é excepção declarada — é que **13 dos 26 hooks aprovados**
enunciam a falha pelo **dêictico + o prop na mão** (`this is what my {o} looked
like`) em vez de por verbo de disfunção, e o regex do CT2 lê verbo. Três saídas:
crescer a lente (precedente: ela já cresceu 5 vezes por reprovar copy certa),
declarar exceção em `DESLIGADAS`, ou reformular os 13 hooks. **Medido: zero
ERRO em 400 sorteios, todos os 8 pools 100% alcançáveis, 0% em CT1/CT3/CT4/
CT4b/CT5/CT6/CT7/CT8, zero frase órfã.**

⏳ **Pendência aberta:**
[`PENDENCIA-varredura-batidas.md`](funil-organico/PENDENCIA-varredura-batidas.md)
— levar as duas lentes novas do `alfa16` (predicado vazio e coerência de
pessoa) ao resto da família 16s. ⚠️ **A medição preliminar já está lá e
encolheu a pendência**: predicado vazio deu zero caso real (os dois
acusados eram copy verbatim do operador) e o zigue-zague de pessoa só
aparece no `ressurreicao16`, em 12%. Ler antes de executar — a varredura
produziu mais falso positivo que achado.

### ⛔⛔ CONTRA A CELEBRIDADE, SILÊNCIO — NUNCA `not a celebrity` (2026-08-10)

Ordem do operador, com o lote na mão: *"não falar de celebridade nem usar a
palavra famoso, celebridade no prompt, muito menos dizer burramente no prompt
'not morgan freeman', 'not celebrity', 'not famous people'"*. A doutrina do repo
já dizia isso desde 2026-07-31
([`licoes-producao-veo.md`](funil-organico/licoes-producao-veo.md) §*Declaração é
munição*) e **nunca tinha sido aplicada aos motores** — `not a celebrity` seguia
em 43 arquivos, injetando justamente o token que se temia.

> **A defesa não é negar celebridade; é descrever um rosto que nenhuma
> celebridade tem.** Rosto genérico deriva para a média do treino, e a média tem
> nome.

⭐ Consertado em **`pee16`** (cláusula deletada; pool `REFS` reescrito e dobrado
para 24 entradas com **arquitetura facial** — formato do rosto, testa/arcada,
nariz, maxilar, malar — e 5 das 24 não grisalhas, porque um pool 100% prateado é
um homem só) e em **`fight16`** (as três negações removidas, a metade positiva
fica).

#### ⭐⭐ DÍVIDA PAGA EM 2026-08-14 — *"tire not a celebrity do prompt"*

Os outros motores foram varridos. ⛔ **Não por edição à mão:** a cláusula é um
recorte **regular**, e as 54 entradas do `APELO_EUA` são copy validada —
redigitar copy validada é o erro que o repo já pagou. O molde é o
`tirar_bandeira`/`_BANDEIRA`: **substituição verificada, com a lente junto.**

| | |
|---|---|
| Ferramenta | [`tirar_anticeleb.py`](funil-organico/tirar_anticeleb.py) — `--dry-run` (padrão) · `--aplicar` · `--lapide` |
| Recorte + lente | `short_comum.tirar_anticeleb` / `lint_anticeleb` (+ `autoteste_anticeleb`) |
| Cobrança | `lint_anticeleb` roda em **44 de 44** motores — pelo `lint_curto` e, nos que têm `lint()` próprio, por chamada explícita |
| Aplicado | **30 arquivos, 112 strings** (111 na primeira passada + a do plural) |
| Medido (seed `20260814`, N=60) | `celebrity` **100% → 0%** nos 30 motores sujos; **0%** nos 5 padrões em 44 de 44 |
| Controle negativo | 264 plantios da cláusula, **264 acusados** — nenhum motor "limpo por ninguém estar olhando" |
| Prosa | 0 acusação de vírgula dupla / espaço duplo em **5.280 sorteios** |

⭐ **A metade positiva fica.** `"Ordinary relatable face, not a celebrity."` virou
`"Ordinary relatable face."` — 18 das 20 formas tinham descrição sobrevivente. As
duas do **FALTA** eram negação **pura**: viraram vazio, e por isso o slot passou
a levar a própria pontuação (`sc.frase_anti`), senão sobrava ponto órfão.

⛔ **As lápides ficam, todas as 105** — comentário, docstring, e os regex
`_CELEB_POOL`/`ES17`/`RS12`/`TR16`, que são o **detector**, não o defeito.
Apagá-los removeria a memória que impede a reincidência.

⚠️ **Duas coisas que só a medição achou** — nenhuma estava no inventário:
- O **VAZAMENTO** tinha a forma **plural sem artigo** (`not celebrities, not
  models, not actors`), que o primeiro regex não pegava. Saía em **100%** dos
  vídeos. Quem a achou foi a medição do **prompt gerado**, não o grep no fonte.
- O **ESCANDALO** tem fala aprovada — *"The gelatin trick is not famous"* — onde
  `not famous` significa "o truque não é famoso". Por isso a lente lê a
  **direção de cena** e nunca a fala, e `not famous` cru ficou fora do recorte.

⛔ E a âncora do controle negativo do **DUPLA** deixou de ser `ANTICELEB`: com a
constante vazia, `str.replace("", X)` insere `X` entre cada caractere (91 chars
viravam 5.059) e o controle seguia "passando" pelo motivo errado.

⛔ E o eixo de rosto do `pee16` ganhou o que faltava do outro lado: **narrador e
vítima entraram no ledger**. Eram os dois únicos eixos do motor **sem memória
nenhuma** (`rng.choice` cru), e era isso que trazia a mesma dupla em lotes
seguidos mesmo depois de duas ampliações de pool — *pool grande com sorteio sem
memória repete igual*. O `LOCAIS` foi de 9 para 21 (as 9 antigas eram seis vezes
o mesmo corredor de varejo) e o motor ganhou `--autoteste`, que ele nunca teve.

Cada um **não substitui** o SHORT do mesmo ângulo: são formatos diferentes e os
dois coexistem. Nasceram por cópia literal com cirurgia só no eixo temporal — as
duas cenas finais fundem num quadro só.

### ⛔⛔ [`CONTRATO-COPY-16S.md`](funil-organico/CONTRATO-COPY-16S.md) — leia antes de escrever copy de 16s

Sete travas em código (`short_comum.lint_copy16`), cobradas de fora por
`python funil-organico/medir_copy16.py --gate`. Nasceram de uma revisão
adversarial de 6 lentes sobre lotes renderizados (2026-08-10), e do fato de que
os **sete defeitos apareciam em quase todos os motores ao mesmo tempo** — o que
não é erro de quem escreveu o pool, é ausência de contrato.

| | |
|---|---|
| **CT1** | nada depois da sentença do CTA — o `follow` vai **antes** |
| **CT2** | o take 1 enuncia a **falha dele**, com dano concreto |
| **CT3** | `gelatin trick` carrega **verbo de efeito + alvo** na mesma sentença |
| **CT4** | **um** apelido do órgão por vídeo, repetido nos dois takes |
| **CT4b** | os apelidos sorteáveis são **`pecker` · `wiener` · `Johnson`** |
| **CT5** | nenhum **ingrediente** nomeado na fala — a receita é a moeda |
| **CT6** | o CTA diz **onde** a receita chega (`goes to your messages`) |
| **CT7** | verbo de ereção **colado no órgão** é proibido |
| **CT8** | **nenhum pedido de follow na fala** |

⛔ **O CT4 reverte a regra antiga** de "substantivos distintos por cena". Em 24s
e cinco cenas o bordão é o risco; em 16s e duas cenas o corte zera a memória de
trabalho, e trocar `soldier` por `Johnson` no segundo 9 obriga a remapear. A
variação continua **entre** vídeos, e é o **CT4b** que a cobra — sem ele, "um
apelido por vídeo" vira o mesmo apelido no lote inteiro.

⛔⛔ **O CT8 reverte outra**, e por correção de FATO: *"a mensagem é enviada
independente de seguirem ou não"* (operador, 2026-08-10). O gate de follow
existia no repo inteiro por uma premissa errada sobre a automação de DM. Os
pools `GATES`/`FOLLOWS16` ficaram no código **marcados como aposentados** —
mexer neles não muda vídeo nenhum. A lente `T16-2` (o follow nunca encosta na
keyword) fica como rede para o dia em que o beat voltar.
⚠️ A ferramenta do Flow ainda não existe — o prompt de criação da **AdBatch
Vertical 2** está em
[`adbatch-prompts-editor.md`](funil-organico/adbatch-prompts-editor.md)
§*CRIAÇÃO DA V2*. O Montador Vertical 3 já serve para 2 vídeos (medido no
fonte); só o rótulo do slot 2 mente.

⛔ **Tudo com label `lucas` mudou-se para
[`agentes-de-terceiros/`](agentes-de-terceiros/) e não existe para nós.** São de
um amigo do Ed, que arquitetou de outra forma. **Não ler, não medir, não
consertar, não citar.** Os `.exe` deles seguem na área de trabalho e continuam
funcionando — ordem dele de manter como estão.

⚠️ Até 2026-08-03 quatro SHORT faziam `import <agente>_lucas as base`. Foram
desacoplados por **cópia literal**, com duas provas antes do commit: importação
dos `*_lucas` bloqueada (os 9 rodam) e **equivalência bit a bit** em 5 seeds e
4.000 vídeos — o refactor não mudou um caractere do vídeo gerado.

**Agente maduro vira ferramenta.** Quando as regras param de mudar, o agente é
portado para código: motor (`<agente>_short.py` — pools sorteáveis, strings
travadas como constantes, linter em regex), app tkinter offline e `.exe`
entregue em `C:\Users\edlut\Desktop\agentes_py`, dentro de **uma das três
famílias** (`AGENTES-NORMAIS` · `AGENTES-SHORT` · `AGENTES-16`, reorganização de
2026-08-09 — o `distribuir.py` classifica pelo sufixo do nome). Receita e gotchas:
[`funil-organico/RUNBOOK-app-offline.md`](funil-organico/RUNBOOK-app-offline.md).
A interface é compartilhada (`ui_agente.py`), só o motor muda; a maquinaria do
colapso de 5 para 3 cenas mora em `short_comum.py`.
⚠️ A copy fundida da cena 2 carrega obrigatoriamente o literal `gelatin trick` e
o mecanismo do agente, porque as cenas que os traziam são justamente as que caem.
⚠️ **Vai pro código o mecânico e verificável; fica no Markdown o julgamento.**
String validada é **constante**, nunca redigitada — comprimir o D1 na mão já
entregou esqueleto 3D no lugar da placa em corte.

**Agentes especialistas por ângulo** (desmembramento 2026-07-28): **19 agentes**
`AGENTE_ED_<ANGULO>_V1.md` na raiz — FLAGRANTE (humilhação pública), GEMEO
(antes/depois, o recorde 345K), RESSURREICAO (despejo→crescimento), DEMO_QUIMICA,
SUBSTANCIA_ABSURDA, DIAGNOSTICO, CONSEQUENCIA, ELA_NARRADORA, CONFISSAO, DIARIO,
GUERRILHA, CONSULTORIO (diagnóstico ao vivo com paciente-evidência — Tanisha),
PEE (a mancha pública — o hook fundador do M15, 1.5K/583/311),
ELA_DIAGNOSTICA (REF feminina + dedo no abdômen + alarme),
VAZAMENTO (corpo-prova musculoso + geoduck gigante que vaza + a receita que ele
declara incompleta — Kofi 703/254/36),
UNCAO (REF feminina esfregando cubos de gelatina no sifão que endireita na tela +
payoff de status em evento social — comissão do operador, sem leitura ótica),
**NECROSE** (dois modelos anatômicos 3D em pedestal lado a lado, um apodrecido
e um são, nas mãos de um montanhês de tronco nu com um lobo — Alaskan Mountain
Men Tips, 1.9K/307/103),
**TROCA** (a narradora manda esfregar a substância absurda, desmente a
própria isca e troca o proxy pela gelatina no mesmo ponto do quadro; corpo-prova
masculino na cena 3 — Julie Evans, mediana 25,5K em 7 reels),
**ESCANDALO** (a plateia congelada que a fala nunca menciona: 1-2 figurantes mudos,
em foco ao lado da cabeça dela, congelados de olhos arregalados enquanto ela ergue o
par eixo+orifício; o homem do hook volta como corpo-prova na cena 3 — Sofia Maren,
32.930 no reel fundador),
**BOTICA** (a botica de casa contra a farmácia da esquina: uma mulher de traje
tradicional, numa cozinha forrada de potes de ervas, prepara a receita em cena
— e o vilão é a **farmácia**, nomeado já na fonte. ⭐ Único ângulo com
**utensílio em movimento** (12 métodos, e o operador proibiu fixar o
liquidificador) e com **pool de ingredientes raros**, que entram sempre como
`nome popular + aposto` (`maca root, that Andean root from Peru`), nunca com
nome científico. Na cena 3 um homem **mudo** olha o copo com espanto — True
Health, reel 3973945436069257, 1K/1K/53),
**RECEITA** (a receita é a prova: um homem confessa em 1ª pessoa que estava
perdendo a mulher, e a evidência não é um corpo — é a bancada dele, sem rosto
até o payoff. Único ângulo sem prop fálico e sem corpo-prova nas duas primeiras
cenas. ⭐ **Toggle de enquadramento na cena 1**: `corte de maos` (macro só nas
mãos, como a fonte) ou `terceira pessoa` (ele em quadro preparando). O cavalo
vivo foi cortado e a entropia dele virou pool de **lugares masculinos**, garagem
como carro-chefe — reel 1683536299390859),
**COLO** (a isca no colo: prop fálico em pé no punho dela, acima do colo e entre
os joelhos, com substância absurda despejada por cima; ela desmente a própria
promessa na mesma respiração e corta para a bancada, de pé, com a receita — a
etnia arrasta o mundo inteiro, 12 mundos em 9 famílias — Sofia Maren, reel
1580259273673843),
**RESSURREICAO** (o despejo faz o prop murcho **alongar na tela** — e a escala é
**diferencial**: altura 2,31× contra largura 1,44×, medido em pixels na fonte, então
ele alonga em vez de inchar; escala uniforme lê como tumescência e já derrubou vídeo
nosso. O morph mora no apagão de fala e acontece oculto dentro do jato),
**CHA** (a caneca estendida na lente: ela sentada na varanda de casa, braço
esticado, a caneca de vidro com chá verde grande em primeiro plano e ela menor
atrás — corta para a cozinha da **mesma casa**, com a mesma roupa, e a receita é
limões + gengibre + alho + o raro fervendo numa panela sobre fogareiro. ⭐ Único
ângulo com **corte de ambiente dentro do vídeo**, e por isso varanda e cozinha
são **um eixo só**. ⛔ Sem homem, sem prop fálico, sem substância absurda, sem
vilão — a fonte não tem nenhum dos quatro. ⭐⭐ **O traje é a bullet de retenção**
por ordem do operador (decote, saia curta, pernas em quadro), e é o eixo que o
painel põe logo abaixo da REF — Alani bussy, reel 1669063827687365, 31K views /
1.4K reações / **2.4K comentários**, o melhor CTA de comentário do repertório).
**TRIO** (a especialista que apresenta dois casos: duas mulheres **sentadas**
num sofá, cada uma com um geoduck no colo — uma o murcho, outra o grande — e a
REF **em pé atrás**, inclinada entre os ombros delas, o dedo descendo sobre um
deles. ⭐ É a geometria que separa do DUPLA: lá as duas estão em pé e a
comparação é horizontal; aqui quem fala está **acima e atrás**, e a leitura muda
de "duas amigas comparando" para "alguém apresentando dois casos". Corta para a
cozinha da mesma casa (a REF + uma delas) e fecha na cena do EXTERIOR — ela com
o copo, ele **cortado no peito, sem rosto**, com o prop grande na cintura.
⛔ O CTA da fonte é `book`, proibido aqui: virou `gelatin` — Alexis Lin
Wellness, reel 1255806096524989),
**FALTA** (a receita entregue **inteira menos um pedaço**, e o vídeo diz isso
na cara: a isca deixa de ser *"te mando a receita"* e vira **te mando o pedaço
que falta** — que É o gelatin trick. ⭐ É o único ângulo em que a promessa do
CTA nasce nomeada dentro da cena 2 (`the missing part`) e reaparece literal no
CTA; o guarda de eco do motor bloqueia repetição entre cenas **menos** essa,
que é a costura. ⭐ Duas mulheres nas três cenas e ⛔ **nenhum homem** — a
fonte tem um cozinhando ao fundo e ele saiu por ordem do operador. O prop do
hook é **eixo sorteado**: geoduck OU peça anatômica peniana, e ele **muda na
tela** durante o despejo — ⚠️ com escala **diferencial**, nunca uniforme, que é
a lição paga do RESSURREICAO. MODO BELA de nascença, 15 arquétipos por região
dos EUA — reel 1753888712524981).
Tabela completa com evidências no WORKFLOW.md.
⚠️ **Essa tabela está atrasada**: DUPLA, PLACA, CHA, TRIO e FALTA ainda não têm
linha lá — os cinco são motor-only (sem `AGENTE_ED_*.md`), e a descrição acima
é hoje a fonte da verdade deles. Todos enxutos: regras
próprias + mecânica por ponteiro (V4/PRISMA/arsenal). O PRISMA sorteia a spec;
o especialista do ângulo sorteado executa. ⛔ `fake_broadcast` está banido.

## ⛔ REGRA DE ALÇADA — copy e cena são do operador (2026-07-28)

> **Nunca alterar COPY ou CENA por conta própria. Consultar o Ed antes,
> sempre.**

Vale principalmente quando um prompt é recusado pelo gerador. O reflexo errado
— cometido várias vezes em produção — é **mudar a cena** para destravar: tirar
a fita métrica, trocar a pose do colo, afastar o proxy do corpo, cortar
personagem. Isso resolve o bloqueio destruindo justamente o que fazia o vídeo
converter, e a decisão não é minha.

**O que fazer diante de recusa:**
1. Isolar a variável (que cena falhou, quais passaram, o que as diferencia).
2. **Reescrever a forma de dizer**, mantendo cena e copy intactas — protocolo
   completo em [`prop-metaforas`](funil-organico/prop-metaforas.md) §Recusa do
   gerador.
3. Esgotar 3-4 formulações.
4. Se nada passar: **reportar ao Ed com o diagnóstico e as opções**, e esperar
   a decisão dele. Não escolher por ele.

O mesmo vale para "melhorar" copy: sugerir sim, trocar não.

**Lição que generaliza (validada em produção 2026-07-28):** *quase nunca a
cena está barrada — a frase está.* `sitting across his lap` foi recusado duas
vezes na política de menores; `perched sideways on his right knee, the way a
newlywed poses for a photograph` gerou **a mesma imagem** sem bloqueio. O
classificador julga **tokens e geometria**, não intenção.

⚙️ **Todo agente `AGENTE_ED_*.md` — os existentes e os que vierem — carrega a
seção `## ⛔ RECUSA DO GERADOR — troca-se a FORMA DE DIZER, nunca a cena`,
logo antes de `## Conexões`.** Ao criar um agente novo, copiar o bloco de
qualquer agente existente. Fonte da verdade:
[`funil-organico/prop-metaforas.md`](funil-organico/prop-metaforas.md)
§Recusa do gerador (protocolo + tabela de reescritas validadas).

## Produção de criativo — o essencial

- **Doutrina do modelo:** [`recursos/DOUTRINA-VEO-3.1.md`](recursos/DOUTRINA-VEO-3.1.md) —
  ler antes de escrever qualquer prompt de vídeo.
- **Sempre rodar o randomizador antes de escrever** (obrigatório — o modelo tem
  mode-collapse; solto, gravita pro mesmo protótipo):
  - PRISMA: `python funil-organico/randomizador-prisma.py --pagina <joe|marcus|ray|chuck|matt> --n 10`
  - V6:     `python funil-organico/randomizador-v6.py --pagina <...> --n 10`
  - Flags úteis: `--seed 42` (reproduzível) · `--dry-run` (não grava ledger) · `--stats`.
- **As regras mecânicas do Veo (IMAGE/TAKE, mãos, prop, câmera, luz) moram no V4 e só
  lá.** Uma regra, um lugar. Correção de regra mecânica entra no V4 e vale para as duas
  engines. O V6 herda motor do V4 + biblioteca do V5.
- Na V6: o hook varia (vem do [`banco-hooks.md`](funil-organico/banco-hooks.md)); o corpo
  é **copiado** da [`espinha-fixa.md`](funil-organico/espinha-fixa.md), nunca reescrito.
- CTA travado em **GELATIN**. `BOOK`/`YES` são proibidos (quebram a automação DM).
- Congruência inviolável: mecanismo do criativo = o que a VSL vende (gelatin nas 5);
  etnia do REF = etnia do avatar da página. REF é **solto por vídeo** (sorteado na
  spec, política 2026-07-28) — só a etnia é travada; mesmo rosto nas 5 cenas do vídeo.

## Expandir repertório

Quando o Ed mandar `/watch <link de página garimpada>`, siga a receita da seção 4 do
[`WORKFLOW.md`](WORKFLOW.md): enumerar reels pelo Chrome logado → transcripts em
`--detail transcript` → separar o que varia do que não varia → destilar na fórmula
do `banco-hooks.md` → ampliar os pools do randomizador.

## Deploy de sites / bridge pages

**Antes de tentar subir qualquer página, leia o runbook:**
[`funil-organico/RUNBOOK-deploy-coolify.md`](funil-organico/RUNBOOK-deploy-coolify.md)

Ele tem a infra completa (VPS, Coolify, UUIDs), o gotcha do repo privado
(`/applications/private-github-app` + `github_app_uuid`), e a receita passo a
passo (criar app → domínio → deploy → validar → DNS). Não reinvente — o
`coolify.js` só opera o app `automaweb` existente e **não cria apps novos**.

Inventário atual de domínios e apps:
[`funil-organico/bridge-pages-deploy.md`](funil-organico/bridge-pages-deploy.md)

## ⭐⭐ A ESTEIRA — o segundo pipeline (2026-08-20)

[`esteira/`](esteira/README.md) — **um vídeo-fonte entra, os prompts do Veo
saem.** ⛔ **Não substitui os agentes e não é uma versão pobre deles:** motor
gera **lote** variado de um ângulo validado (pool, ledger, lente, autoteste);
a esteira gera **um vídeo parecido com um vídeo**. Escala repertório, não
volume. As duas convivem.

⭐ **A arquitetura é desenhada em volta do CUSTO DE TOKEN**, por ordem do
operador (*"mês que vem vou pegar o plano básico"*):

| etapa | onde roda | token |
|---|---|---|
| 1 · `ler.py` | o PC dele | **zero** |
| 2 · a leitura | **no chat do navegador** | ~4-5k por vídeo |
| 3 · `gerar.py` | o PC dele | **zero** |

⛔⛔ **E o prompt final não é escrito por modelo nenhum.** Se fosse, cada vídeo
custaria 4-5× mais e traria de volta, um por um, os defeitos já pagos em campo:
aparelho na mão do personagem, `not a celebrity`, bloco estourando os 4.000 da
AdBatch, fala maior que o take. Cada um virou uma linha do `gerar.py` — **o
modelo descreve o que vê; a montagem é código**, e código não regride.

⭐ **O limiar de corte é MEDIDO**, contra os 14 cortes que a leitura ótica de
16/08 achou nos 7 vídeos: `0.30` acha 8 de 14, `0.12` acha **14 de 14** com 2
falsos, `0.05` acha tudo com 30 falsos. ⚠️ **Perder corte é pior que inventar
um** — o take vira dois planos colados num prompt só. Medido em **67 vídeos:
zero falha, mediana de 4 takes, 0,5s de detecção por vídeo**.

App tkinter + `.exe` em `Desktop\agentes_py\ESTEIRA\` (517 MB porque leva o
`faster-whisper` dentro, que é o preço de transcrever offline).

## Onde as coisas ficam

- **App offline dos agentes (motor + tkinter + .exe):** [`funil-organico/RUNBOOK-app-offline.md`](funil-organico/RUNBOOK-app-offline.md).
- **AdBatch Vertical (a ferramenta do Flow que vira o roteiro em vídeo):** [`funil-organico/RUNBOOK-adbatch-vertical.md`](funil-organico/RUNBOOK-adbatch-vertical.md) — arquitetura, contrato do parser e a família 5/4/3. ⭐ **Código-fonte das duas ferramentas, versionado e comentado:** [`funil-organico/adbatch-vertical/README.md`](funil-organico/adbatch-vertical/README.md) — o que só o código revela (`durationSeconds: 10`, modelo `Omni Flash`, corte silencioso em 4.000 chars). Prompts prontos pro Criador de Ferramentas: [`funil-organico/adbatch-prompts-editor.md`](funil-organico/adbatch-prompts-editor.md). ⚠️ **Um assunto por prompt** — o editor regride.
- **Investigar uma recusa do Veo (método):** [`funil-organico/RUNBOOK-bisseccao-moderacao.md`](funil-organico/RUNBOOK-bisseccao-moderacao.md) — bissecção com variável única. ⚠️ **Regerar 2× antes de investigar**: a política de conteúdo nocivo tem variância.
- **Lições de produção Veo (moderação + copy):** [`funil-organico/licoes-producao-veo.md`](funil-organico/licoes-producao-veo.md) — playbook das lições pagas em campo; ler antes de gerar lote.
- ⛔⛔ **Contrato de copy da família 16s:** [`funil-organico/CONTRATO-COPY-16S.md`](funil-organico/CONTRATO-COPY-16S.md) — **ler antes de escrever ou alterar copy de qualquer `*16_short.py`.** Sete travas em `short_comum.lint_copy16`, cobradas por `python funil-organico/medir_copy16.py --gate`. Tem também os quatro achados da revisão adversarial que **não** viraram trava, com o motivo de cada um.
- ⛔ **Lições de construção — os erros do assistente:** [`funil-organico/licoes-de-construcao.md`](funil-organico/licoes-de-construcao.md) — **ler antes de construir ou alterar agente.** 43 modos de falha já cometidos, com o que impede cada um, e o checklist de entrega. ⭐⭐ §43 é a mais recente: *o medidor só conhecia UMA sintaxe de slot* — o verificador de tradução cravou **0 faltando** nos seis motores novos enquanto 12 falas saíam inteiras em inglês, porque ele só compila slot `{nome}` e a família **printf** (`%s`, `%(receita)s`) nunca casa a fala renderizada: ela passa como *"não é copy"*, e esse silêncio é idêntico ao do aprovado. **Medidor de pool não mede função — gere a saída e olhe.** Corolário achado na mesma varredura: *termo de 3+ palavras sem tradução aciona o guarda de slot e derruba a FALA INTEIRA* — 6 locais faltando no glossário do PEE viraram 37 pedaços em inglês. ⭐ §41 continua a mais cara de ver: *o toggle entregava MENOS do que o estado desligado* — o `MODO FORTE` do GOOD 16 tinha idade certa, lente própria e controle negativo, e mesmo assim 232 de 400 corpos saíam sem uma palavra de músculo (contra 0 de 400 com o botão desligado). **Quando um botão não entrega, meça o estado DESLIGADO também.** A causa raiz é uma só: *verificar a FORMA e declarar pronto sem verificar a FUNÇÃO*. Corolário: **aceite é MEDIÇÃO, nunca RELATO** — nem meu, nem de subagente. Dois gates: `python funil-organico/medir_personagens.py --gate` (eixo físico zerado = reprovação) e `python funil-organico/medir_contexto_copy.py --gate` (frase que nomeia causa sem dizer o que ela quebra = reprovação — §17, *"tá deixando o viewer sem entender do que se trata"*).
- **Mapa visual da Tanisha (base do CONSULTORIO):** [`concorrentes/tanisha-mapa-visual.md`](concorrentes/tanisha-mapa-visual.md).
- `funil-organico/` — doutrina de copy, criativos, arquitetura do funil, runbooks.
- Bridge pages (código): repo `Eduardo08GN/projetosweb`, pasta `/bridge-pages/bp1`.
- Deploy: Coolify na VPS `159.195.12.135` via API (ver runbook).
