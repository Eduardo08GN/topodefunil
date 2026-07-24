# Topodefunil — instruções do projeto

Repositório de operação do funil orgânico de nutra (nicho ED, mercado US).

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
