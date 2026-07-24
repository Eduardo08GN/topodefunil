# Bridge Pages — Deploy & Domínios

Registro de todas as bridge pages do funil orgânico ED, hospedadas no VPS via Coolify.

## Infra

- **VPS:** `159.195.12.135` (Netcup)
- **Orquestrador:** Coolify v4.1.2 — instância em `http://159.195.12.135:8000`
- **Reverse proxy:** Traefik (SSL automático via Let's Encrypt)
- **Source dos apps:** repo privado `Eduardo08GN/projetosweb`, branch `main`, GitHub App `coolify-projetosweb`
- **Build:** Dockerfile em `/bridge-pages/bp1` (nginx:alpine servindo `index.html` + `hero.png` em `/bp1/`)
- **Página servida em:** `<dominio>/bp1/`

## Link de destino (oferta)

O clique na imagem da bridge leva para:

```
https://horsewood.us/vsl3/?aff_id=45158&sub_id=<pagina>
```

- `aff_id=45158` → comissão
- `sub_id` → atribuição por página (lido de `?p=<slug>` na URL da bridge; default `direct`)

## Domínios & Apps

| # | Domínio | App Coolify (UUID) | URL de teste (sslip.io) | Status |
|---|---------|--------------------|-----------------------|------------|
| 1 | `manresethub.pro` | `v5t2rojizir3dc37al4zkb4p` | `http://v5t2rojizir3dc37al4zkb4p.159.195.12.135.sslip.io/bp1/` | ✅ **no ar** (HTTPS) |
| 2 | `wholelifenutri.shop` | `cwanszytythvm4myf8yye46k` | `http://cwanszytythvm4myf8yye46k.159.195.12.135.sslip.io/bp1/` | ⚠️ pendente (parking) |
| 3 | `vitalresetlab.site` | `bv4uhh6hpq6tkotyn42nagg3` | `http://bv4uhh6hpq6tkotyn42nagg3.159.195.12.135.sslip.io/bp1/` | ✅ **no ar** (HTTPS) |
| 4 | `primalvitalityhub.site` | `srd3jdzrvc0n7ri3yetjjmuq` | `http://srd3jdzrvc0n7ri3yetjjmuq.159.195.12.135.sslip.io/bp1/` | ✅ **no ar** (HTTPS) |
| 5 | `allmensnatural.site` | `iuge7sircaf0myor1jdl77jv` | `http://iuge7sircaf0myor1jdl77jv.159.195.12.135.sslip.io/bp1/` | ✅ **no ar** (HTTPS) |
| 6 | `steadystrengthhub.site` | `xkma961zrq3jxraw5z4vpg47` | `http://xkma961zrq3jxraw5z4vpg47.159.195.12.135.sslip.io/bp1/` | ✅ **no ar** (HTTPS) |

Todos os 6 apps: deploy **finished**, servindo HTTP 200 (`index.html` 5.1 KB + `hero.png` 1.6 MB).

### Status em 2026-07-24 — 5 de 6 no ar

`https://<domínio>/bp1/` responde **200 com cert Let's Encrypt válido** e redirect
HTTP→HTTPS nos 5 domínios apontados (manresethub.pro, vitalresetlab.site,
primalvitalityhub.site, allmensnatural.site, steadystrengthhub.site). Falta só o
`wholelifenutri.shop`, ainda no parking (`2.57.91.91`) — apontar o A record.

**Gotcha do cert (resolvido):** os apps foram criados ANTES do DNS apontar, então
o Traefik tentou o ACME, falhou (domínio não resolvia pra VPS) e entrou em
backoff. Depois de apontar o DNS, o cert **não sai sozinho** — foi preciso um
**redeploy** de cada app (`GET /api/v1/deploy?uuid=<uuid>`) pra reaplicar os
labels do Traefik e reemitir o cert na hora. Regra: apontou o DNS → redeploya o
app do Coolify → valida HTTPS.

## Pendência: apontar DNS

Cada domínio ainda está nos nameservers de **parking** (`*.dns-parking.com`). Para ir ao ar no domínio final com SSL, em cada painel de DNS:

- Registro **A** `@` → `159.195.12.135`
- (opcional) Registro **A** `www` → `159.195.12.135`

Após propagação, o Traefik emite o certificado e `https://<dominio>/bp1/` responde.

## Como adicionar uma nova bridge page

1. Criar app via API (`POST /api/v1/applications/private-github-app`) com `base_directory: /bridge-pages/bp1`, `ports_exposes: 80`.
2. Setar FQDN (`PATCH /api/v1/applications/<uuid>` com `domains`).
3. Disparar deploy (`GET /api/v1/deploy?uuid=<uuid>`).
4. Apontar DNS (registro A → VPS).
