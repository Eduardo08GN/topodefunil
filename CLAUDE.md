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

**Agentes especialistas por ângulo** (desmembramento 2026-07-28): 11 agentes
`AGENTE_ED_<ANGULO>_V1.md` na raiz — FLAGRANTE (humilhação pública), GEMEO
(antes/depois, o recorde 345K), RESSURREICAO (despejo→crescimento), DEMO_QUIMICA,
SUBSTANCIA_ABSURDA, DIAGNOSTICO, CONSEQUENCIA, ELA_NARRADORA, CONFISSAO, DIARIO,
GUERRILHA. Tabela completa com evidências no WORKFLOW.md. Todos enxutos: regras
próprias + mecânica por ponteiro (V4/PRISMA/arsenal). O PRISMA sorteia a spec;
o especialista do ângulo sorteado executa. ⛔ `fake_broadcast` está banido.

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

- `funil-organico/` — doutrina de copy, criativos, arquitetura do funil, runbooks.
- Bridge pages (código): repo `Eduardo08GN/projetosweb`, pasta `/bridge-pages/bp1`.
- Deploy: Coolify na VPS `159.195.12.135` via API (ver runbook).
