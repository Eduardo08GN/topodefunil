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

**Token da API:** fica como `COOLIFY_API_TOKEN` em `MazyOS/.env`,
`MazyOS/automaweb/.env` e `projetosweb/automaweb/.env` (os tres tem o mesmo
valor). Nao existe `.env` na raiz do `projetosweb` — so `.env.example`.
Nunca cole o token em chat/commit. Se aparecer em texto, rotacione no Coolify
(Keys & Tokens) e atualize os tres arquivos.

> ⛔⛔ **O token comeca com `4|` e PRECISA de aspas no `.env`.** Sem elas,
> `set -a; . .env` faz o shell ler `4` e tratar o resto como **pipe**, chamando
> o hash como comando. A variavel chega **vazia**, o `curl` manda
> `Authorization: Bearer ` e a API responde `{"message":"Unauthenticated."}`.
> ⚠️ **Isso imita perfeitamente um token expirado** e ja custou uma sessao
> inteira: foram tres arquivos testados, todos "invalidos", todos corretos.
> Pior: com `2>/dev/null` o `command not found` some e nao sobra pista nenhuma.
> Forma certa no arquivo:
> ```
> COOLIFY_API_TOKEN="4|<hash>"
> ```
> Antes de concluir que um token morreu, teste se ele chega inteiro:
> `( set -a; . .env; set +a; [ -n "$COOLIFY_API_TOKEN" ] && echo chegou )`
> — **sem** redirecionar stderr.

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

## ⛔ `fit-fr-bp` NAO AUTO-DEPLOYA (2026-09-21)

Os tres apps das landings do ebook 150 olham o mesmo repo e a mesma branch:

| App | UUID | Dominio | `base_directory` |
|---|---|---|---|
| `fit-en-bp` | `r2cgw8c5j25cq0e89i7lrj7n` | `book.dailyfactreport.site` | `/bridge-pages/bp-fit-en` |
| `fit-de-bp` | `qg2mxau3et2gp85kv6mrwdqo` | `book.plainfactsdaily.site` | `/bridge-pages/bp-fit-de` |
| `fit-fr-bp` | `v2524bw7z6ho7v22d6xadyz2` | `book.thedailyfinding.site` | `/bridge-pages/bp-fit-fr` |

Num push que tocou os tres, **EN e DE deployaram sozinhos e o FR nao**. Um
commit vazio de re-disparo tambem nao acordou o FR. So saiu com deploy manual
pela API. A API nao expoe o toggle de auto-deploy, entao a causa exata ficou
por confirmar no painel.

➡️ **Depois de mexer no `bp-fit-fr`, NAO confie no push.** Dispare o deploy e
espere o `status` virar `finished`:

```bash
( set -a; . MazyOS/.env; set +a
  curl -s -H "Authorization: Bearer $COOLIFY_API_TOKEN"     "http://159.195.12.135:8000/api/v1/deploy?uuid=v2524bw7z6ho7v22d6xadyz2&force=true" )
# → {"deployments":[{"deployment_uuid":"<DEP_UUID>", ...}]}
```

⭐ **A prova final nao e o `finished`, e o `Last-Modified` do dominio.** Foi o
header que denunciou o problema: EN e DE com build do dia, FR ainda com o de
cinco dias antes, servindo o checkout velho com HTTP 200 e pagina intacta.

```bash
curl -sI https://book.thedailyfinding.site/ | grep -i last-modified
```

## ⭐ LOTE INTEIRO? LEIA ISTO ANTES

Para subir VARIAS paginas de uma vez — dominio, build, cofre, Coolify,
tracking e notificacao — a sequencia completa e as armadilhas estao em
[`RUNBOOK-lote-de-bridges.md`](RUNBOOK-lote-de-bridges.md). Ele tem o caminho
feliz e o **caminho ruim**, escrito a partir dos desvios reais do lote 4.
⛔ A licao que vale por todas: **200 OK nao significa "deu certo" em lugar
nenhum deste sistema** — tres componentes respondem 200 enquanto descartam.

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
