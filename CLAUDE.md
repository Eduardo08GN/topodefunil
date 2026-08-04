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

Os **quatorze agentes** deste funil são os `<angulo>_short.py` em `funil-organico/`:
`clean` · `clean_v2` · `escandalo` · `troca` · `organicwave` · `ressurreicao` ·
`flagrante` · `pee` · `vazamento` · `necrose` · `exterior` · `colo` · `receita` ·
`botica`.
Três cenas de 8s, destino AdBatch Vertical 3.
**Cada um é autossuficiente e é a FONTE DA VERDADE do seu ângulo** — correção de
regra entra no `_short`.

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
entregue em `C:\Users\edlut\Desktop\agentes_py`. Receita e gotchas:
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
nosso. O morph mora no apagão de fala e acontece oculto dentro do jato).
Tabela completa com evidências no WORKFLOW.md. Todos enxutos: regras
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
- **AdBatch Vertical (a ferramenta do Flow que vira o roteiro em vídeo):** [`funil-organico/RUNBOOK-adbatch-vertical.md`](funil-organico/RUNBOOK-adbatch-vertical.md) — arquitetura, contrato do parser e a família 5/4/3. Prompts prontos pro Criador de Ferramentas: [`funil-organico/adbatch-prompts-editor.md`](funil-organico/adbatch-prompts-editor.md). ⚠️ **Um assunto por prompt** — o editor regride.
- **Investigar uma recusa do Veo (método):** [`funil-organico/RUNBOOK-bisseccao-moderacao.md`](funil-organico/RUNBOOK-bisseccao-moderacao.md) — bissecção com variável única. ⚠️ **Regerar 2× antes de investigar**: a política de conteúdo nocivo tem variância.
- **Lições de produção Veo (moderação + copy):** [`funil-organico/licoes-producao-veo.md`](funil-organico/licoes-producao-veo.md) — playbook das lições pagas em campo; ler antes de gerar lote.
- ⛔ **Lições de construção — os erros do assistente:** [`funil-organico/licoes-de-construcao.md`](funil-organico/licoes-de-construcao.md) — **ler antes de construir ou alterar agente.** 22 modos de falha já cometidos, com o que impede cada um, e o checklist de entrega. A causa raiz é uma só: *verificar a FORMA e declarar pronto sem verificar a FUNÇÃO*. Corolário: **aceite é MEDIÇÃO, nunca RELATO** — nem meu, nem de subagente. Dois gates: `python funil-organico/medir_personagens.py --gate` (eixo físico zerado = reprovação) e `python funil-organico/medir_contexto_copy.py --gate` (frase que nomeia causa sem dizer o que ela quebra = reprovação — §17, *"tá deixando o viewer sem entender do que se trata"*).
- **Mapa visual da Tanisha (base do CONSULTORIO):** [`concorrentes/tanisha-mapa-visual.md`](concorrentes/tanisha-mapa-visual.md).
- `funil-organico/` — doutrina de copy, criativos, arquitetura do funil, runbooks.
- Bridge pages (código): repo `Eduardo08GN/projetosweb`, pasta `/bridge-pages/bp1`.
- Deploy: Coolify na VPS `159.195.12.135` via API (ver runbook).
