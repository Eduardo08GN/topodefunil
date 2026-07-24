# RUNBOOK — Como subir um site (Coolify + VPS)

> Leia isto **antes** de tentar deployar qualquer página. Este runbook existe pra
> não ficar perdido reaprendendo a infra a cada conversa nova.

## 1. O que temos (fatos da infra — não mude sem confirmar)

| Coisa | Valor |
|-------|-------|
| VPS (Netcup) | `159.195.12.135` |
| Coolify (painel + API) | `http://159.195.12.135:8000` |
| API base | `http://159.195.12.135:8000/api/v1` |
| Reverse proxy | Traefik (SSL automático via Let's Encrypt) |
| Server UUID | `nakr4xp0tipmct1hn0343kjt` |
| Project UUID ("My first project") | `pvdb5sd41fc3zh0a75a1ra8u` |
| Environment | `production` |
| Repo source (privado) | `Eduardo08GN/projetosweb` branch `main` |
| GitHub App UUID (autentica o repo privado) | `yhriwaecxwznwiino9848rg1` |

**Token da API:** fica no `.env` do repo `projetosweb` como `COOLIFY_API_TOKEN`.
Nunca cole o token em chat/commit. Se aparecer em texto, rotacione no Coolify
(Keys & Tokens) e atualize o `.env`.

## 2. Duas ferramentas — saiba qual usar

### `scripts/coolify.js` (no repo projetosweb)
- Serve pra operar **UM app já existente**, o `automaweb` (preso ao
  `COOLIFY_APP_UUID` do `.env`).
- Comandos: `status`, `deploy`, `restart`, `env list`, `env set CHAVE valor`.
- **NÃO cria apps novos.** Pra site novo, use a API direto (seção 4).

### API REST direta (curl)
- Pra **criar app novo**, setar domínio e deployar. É o caminho das bridge pages.

## 3. GOTCHA que já queimou tempo (leia!)

O repo `projetosweb` é **PRIVADO**. Se criar o app pelo endpoint público
(`/applications/public`), o deploy falha com:

```
fatal: could not read Username for 'https://github.com': No such device or address
```

➡️ **Sempre use** `/applications/private-github-app` passando
`github_app_uuid: yhriwaecxwznwiino9848rg1`. Esse é o GitHub App já instalado
que dá acesso ao repo privado.

## 4. Receita: subir uma bridge page nova

Pré-requisito: os arquivos do site já commitados no repo `projetosweb`, numa
pasta com um `Dockerfile`. As bridge pages ficam em `/bridge-pages/bp1`
(nginx:alpine servindo `index.html` + `hero.png` em `/bp1/`).

### Passo 1 — criar o app
```bash
curl -s -X POST \
  -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
  "http://159.195.12.135:8000/api/v1/applications/private-github-app" \
  -d '{
    "github_app_uuid": "yhriwaecxwznwiino9848rg1",
    "project_uuid": "pvdb5sd41fc3zh0a75a1ra8u",
    "server_uuid": "nakr4xp0tipmct1hn0343kjt",
    "environment_name": "production",
    "git_repository": "Eduardo08GN/projetosweb",
    "git_branch": "main",
    "build_pack": "dockerfile",
    "base_directory": "/bridge-pages/bp1",
    "ports_exposes": "80",
    "name": "MEUAPP-bp1",
    "description": "..."
  }'
# → retorna {"uuid":"<APP_UUID>", ...}
```

### Passo 2 — setar o domínio (FQDN)
```bash
curl -s -X PATCH \
  -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
  "http://159.195.12.135:8000/api/v1/applications/<APP_UUID>" \
  -d '{"domains": "https://MEUDOMINIO.site,http://<APP_UUID>.159.195.12.135.sslip.io"}'
```
O segundo host (`<uuid>.159.195.12.135.sslip.io`) é o **fallback de teste** que
funciona ANTES do DNS apontar — use pra validar sem esperar propagação.

### Passo 3 — deployar
```bash
curl -s -H "Authorization: Bearer $TOKEN" \
  "http://159.195.12.135:8000/api/v1/deploy?uuid=<APP_UUID>"
# → retorna {"deployments":[{"deployment_uuid":"<DEP_UUID>", ...}]}
```

### Passo 4 — acompanhar até terminar
```bash
curl -s -H "Authorization: Bearer $TOKEN" \
  "http://159.195.12.135:8000/api/v1/deployments/<DEP_UUID>" \
  | python -c "import sys,json;print(json.load(sys.stdin).get('status'))"
# estados: queued -> in_progress -> finished | failed
```
Se `failed`, leia o campo `logs` do mesmo endpoint (é um JSON array de linhas).

### Passo 5 — validar
```bash
curl -sL -o /dev/null -w "%{http_code}/%{size_download}\n" \
  "http://<APP_UUID>.159.195.12.135.sslip.io/bp1/"
# espere 200/5114 pro html e 200/1685509 pro /bp1/hero.png
```

### Passo 6 — DNS (feito pelo dono no painel do registrador)
Cada domínio nasce nos nameservers de **parking** (`*.dns-parking.com`).
Pra ir ao ar no domínio final com SSL:
- Registro **A** `@` → `159.195.12.135`
- (opcional) **A** `www` → `159.195.12.135`

Como saber se já apontou: `nslookup DOMINIO 8.8.8.8`. Se ainda mostra o IP de
parking (`2.57.91.91`) em TODOS os nós, o registro **não foi trocado** ainda —
não é "propagação", é que ninguém mexeu no A record.

## 5. Endpoints úteis de descoberta (read-only)

```
GET /api/v1/applications          # lista todos os apps (uuid, name, fqdn)
GET /api/v1/applications/<uuid>   # detalhe de 1 app (source_id, base_directory…)
GET /api/v1/github-apps           # lista GitHub Apps (achar o uuid do repo privado)
GET /api/v1/servers               # servers
GET /api/v1/projects              # projects (project_uuid)
```

## 6. Registro vivo

O inventário atual de domínios/apps fica em
[`bridge-pages-deploy.md`](bridge-pages-deploy.md). Atualize-o sempre que
criar/remover um app.
