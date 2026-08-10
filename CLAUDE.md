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
com **catorze agentes**, não mais um. **2 takes de 8s**, destino **AdBatch
Vertical 2**, ledger próprio cada um:

`trio16` · `dupla16` · `falta16` · `placa16` · `troca16` · `botica16` ·
`colo16` · `exterior16` · `escandalo16` · `ressurreicao16` · `flagrante16` ·
`pee16` · `good16` · (+ `clean_v1_16s`/`clean_v2_16s`, do outro autor)

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

## Onde as coisas ficam

- **App offline dos agentes (motor + tkinter + .exe):** [`funil-organico/RUNBOOK-app-offline.md`](funil-organico/RUNBOOK-app-offline.md).
- **AdBatch Vertical (a ferramenta do Flow que vira o roteiro em vídeo):** [`funil-organico/RUNBOOK-adbatch-vertical.md`](funil-organico/RUNBOOK-adbatch-vertical.md) — arquitetura, contrato do parser e a família 5/4/3. ⭐ **Código-fonte das duas ferramentas, versionado e comentado:** [`funil-organico/adbatch-vertical/README.md`](funil-organico/adbatch-vertical/README.md) — o que só o código revela (`durationSeconds: 10`, modelo `Omni Flash`, corte silencioso em 4.000 chars). Prompts prontos pro Criador de Ferramentas: [`funil-organico/adbatch-prompts-editor.md`](funil-organico/adbatch-prompts-editor.md). ⚠️ **Um assunto por prompt** — o editor regride.
- **Investigar uma recusa do Veo (método):** [`funil-organico/RUNBOOK-bisseccao-moderacao.md`](funil-organico/RUNBOOK-bisseccao-moderacao.md) — bissecção com variável única. ⚠️ **Regerar 2× antes de investigar**: a política de conteúdo nocivo tem variância.
- **Lições de produção Veo (moderação + copy):** [`funil-organico/licoes-producao-veo.md`](funil-organico/licoes-producao-veo.md) — playbook das lições pagas em campo; ler antes de gerar lote.
- ⛔⛔ **Contrato de copy da família 16s:** [`funil-organico/CONTRATO-COPY-16S.md`](funil-organico/CONTRATO-COPY-16S.md) — **ler antes de escrever ou alterar copy de qualquer `*16_short.py`.** Sete travas em `short_comum.lint_copy16`, cobradas por `python funil-organico/medir_copy16.py --gate`. Tem também os quatro achados da revisão adversarial que **não** viraram trava, com o motivo de cada um.
- ⛔ **Lições de construção — os erros do assistente:** [`funil-organico/licoes-de-construcao.md`](funil-organico/licoes-de-construcao.md) — **ler antes de construir ou alterar agente.** 23 modos de falha já cometidos, com o que impede cada um, e o checklist de entrega. A causa raiz é uma só: *verificar a FORMA e declarar pronto sem verificar a FUNÇÃO*. Corolário: **aceite é MEDIÇÃO, nunca RELATO** — nem meu, nem de subagente. Dois gates: `python funil-organico/medir_personagens.py --gate` (eixo físico zerado = reprovação) e `python funil-organico/medir_contexto_copy.py --gate` (frase que nomeia causa sem dizer o que ela quebra = reprovação — §17, *"tá deixando o viewer sem entender do que se trata"*).
- **Mapa visual da Tanisha (base do CONSULTORIO):** [`concorrentes/tanisha-mapa-visual.md`](concorrentes/tanisha-mapa-visual.md).
- `funil-organico/` — doutrina de copy, criativos, arquitetura do funil, runbooks.
- Bridge pages (código): repo `Eduardo08GN/projetosweb`, pasta `/bridge-pages/bp1`.
- Deploy: Coolify na VPS `159.195.12.135` via API (ver runbook).
