# Topodefunil — instruções do projeto

Repositório de operação do funil orgânico de nutra (nicho ED, mercado US).

## ⭐ LEIA PRIMEIRO: [`WORKFLOW.md`](WORKFLOW.md)

Ponto de entrada do repo. Tem a operação inteira: as 5 páginas, o pipeline de
produção de criativo (randomizador v6 → agente V6 → AdBatch → Veo Editor →
postagem), as regras invioláveis, como expandir o repertório com `/watch`, o mapa
de arquivos e as pendências. **Nenhum trabalho começa antes de ler esse arquivo.**

## Produção de criativo — o essencial

- **Doutrina do modelo:** [`recursos/DOUTRINA-VEO-3.1.md`](recursos/DOUTRINA-VEO-3.1.md) —
  ler antes de escrever qualquer prompt de vídeo.
- Agente de produção: `AGENTE_ED_ORGANIC_WAVE_V6.md` (motor no V4, dispositivos no V5).
- **Sempre rodar o randomizador antes de escrever:**
  `python funil-organico/randomizador-v6.py --pagina <joe|marcus|ray|chuck|matt> --n 10`
- O hook varia (vem do [`banco-hooks.md`](funil-organico/banco-hooks.md)); o corpo
  é **copiado** da [`espinha-fixa.md`](funil-organico/espinha-fixa.md), nunca reescrito.
- CTA travado em **GELATIN**. `BOOK`/`YES` são proibidos (quebram a automação DM).

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
