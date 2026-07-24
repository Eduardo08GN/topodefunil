# Arquitetura das Bridge Pages

Como cada bridge page é feita, como o domínio decide qual VSL serve, e como
adicionar/trocar. Complementa a visão macro em [`ARQUITETURA-OPERACAO.md`](ARQUITETURA-OPERACAO.md)
e o inventário/status em [`bridge-pages-deploy.md`](bridge-pages-deploy.md).

---

## O que uma bridge page é

Uma landing **estática** "Private video" (dark, headline em Oswald, hero clicável,
disclaimer). Servida por `nginx:alpine` no caminho **`/bp1/`** de cada domínio.
O clique no hero monta, via JS, o link da VSL com `aff_id` + `sub_id`:

```js
OFFER + "?aff_id=" + AFF + "&sub_id=" + p     // p = ?p=<slug> da URL (default "direct")
```

- **Atribuição por página:** a URL da bridge recebe `?p=<slug-da-pagina>` (do link
  que a página posta/manda no DM). Esse `p` vira `sub_id` na VSL → dá pra ver no
  afiliado qual página converteu.
- `noindex,nofollow` + `title "Private video"` = discrição.

Código-fonte (referência) mora no `topodefunil`:
- Horsewood: [`funil-organico/bridge-page/`](bridge-page/) (= `bp1`)
- Vigortrix: [`funil-organico/bridge-page-vick/`](bridge-page-vick/) (= `bp-vick`)

O que **deploya** de verdade é o repo `projetosweb` (o Coolify puxa do GitHub):
`projetosweb/bridge-pages/bp1` e `projetosweb/bridge-pages/bp-vick`.

---

## As 2 variantes (uma por VSL)

Regra de congruência: o domínio serve a variante da VSL que aquela página roda.

| Variante | Pasta (projetosweb) | Hero | Headline | Clique → | aff_id |
|---|---|---|---|---|---|
| **Horsewood** | `bridge-pages/bp1` | `hero.png` (red bowl + banana) | "He's 67. She's 34. And she's the one chasing now." | `horsewood.us/vsl3/` | 45158 |
| **Vigortrix** | `bridge-pages/bp-vick` | `hero.jpg` (jar Vicks + banana + CLICK HERE) | "He's 67. One jar from the pharmacy aisle. And now she's the one asking." | `vigortrix.com/vesp-l2/` | 75486 |

As duas servem no mesmo caminho `/bp1/` (o Dockerfile copia pra
`/usr/share/nginx/html/bp1/`), então a URL pública é sempre `<domínio>/bp1/` —
o que muda é o CONTEÚDO conforme o `base_directory` do app no Coolify.

### Anatomia de uma pasta de variante
```
bridge-pages/<variante>/
├── Dockerfile      # FROM nginx:alpine; COPY index.html + hero.* -> /html/bp1/
├── index.html      # landing (headline, hero clicável, JS do link VSL)
└── hero.png|.jpg   # imagem do hero
```

---

## Mapa domínio → variante → página (fase inicial)

| Domínio (bridge) | Variante | VSL | Página | App Coolify (UUID) |
|---|---|---|---|---|
| `manresethub.pro` | bp1 (Horsewood) | Horsewood | Joe's Wellness hub | `v5t2rojizir3dc37al4zkb4p` |
| `vitalresetlab.site` | bp1 (Horsewood) | Horsewood | Marcus' Men Reset Hub | `bv4uhh6hpq6tkotyn42nagg3` |
| `primalvitalityhub.site` | bp1 (Horsewood) | Horsewood | Ray's Natural Vitality Hub | `srd3jdzrvc0n7ri3yetjjmuq` |
| `allmensnatural.site` | **bp-vick (Vigortrix)** | Vigortrix | Chuck's Men Welness Hub | `iuge7sircaf0myor1jdl77jv` |
| `steadystrengthhub.site` | **bp-vick (Vigortrix)** | Vigortrix | Matt's Natural Reset Tips | `xkma961zrq3jxraw5z4vpg47` |
| `wholelifenutri.shop` | — (reserva, DNS no parking) | — | — | `cwanszytythvm4myf8yye46k` |

> A designação página↔domínio é a proposta do doc de operação (fácil de trocar).
> O que está **cravado no deploy** é a variante por domínio (coluna "Variante").

---

## Como o Coolify decide a variante

Cada app do Coolify tem um `base_directory` apontando pra pasta da variante:
- 3 apps Horsewood → `base_directory = /bridge-pages/bp1`
- 2 apps Vigortrix → `base_directory = /bridge-pages/bp-vick`

Trocar a variante de um domínio = mudar o `base_directory` do app + redeployar.

---

## Receitas

### Trocar um domínio de Horsewood → Vigortrix (ou vice-versa)
```bash
TOKEN=<coolify_api_token>
# 1. repontar o base_directory
curl -s -X PATCH -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
  "http://159.195.12.135:8000/api/v1/applications/<APP_UUID>" \
  -d '{"base_directory":"/bridge-pages/bp-vick"}'
# 2. redeployar
curl -s -H "Authorization: Bearer $TOKEN" \
  "http://159.195.12.135:8000/api/v1/deploy?uuid=<APP_UUID>"
# 3. validar: <dominio>/bp1/ deve conter "vigortrix" e /bp1/hero.jpg = 200
```

### Criar uma variante nova (nova VSL)
1. `projetosweb/bridge-pages/bp-<nome>/` com `Dockerfile` + `index.html` + `hero.*`
   (copie de `bp1` ou `bp-vick`; troque headline, hero e o `OFFER`/`AFF` no script).
2. `git push` no `projetosweb`.
3. Repontar o app do domínio pro novo `base_directory` + redeploy (receita acima).
4. Espelhe a fonte em `topodefunil/funil-organico/bridge-page-<nome>/` e atualize
   esta tabela.

### Editar uma bridge existente (copy/hero)
1. Edite `projetosweb/bridge-pages/<variante>/` → `git push`.
2. Redeploy dos apps que usam essa variante (`GET /api/v1/deploy?uuid=`).
3. Espelhe a mudança em `topodefunil/funil-organico/bridge-page*/`.

---

## Gotchas herdados
- **Cert não emite sozinho** após apontar DNS: precisa redeploy do app (ver
  [`bridge-pages-deploy.md`](bridge-pages-deploy.md)).
- **Repo privado:** apps criados via `/applications/private-github-app` com o
  GitHub App (ver [`RUNBOOK-deploy-coolify.md`](RUNBOOK-deploy-coolify.md)).
- **Token da API:** nunca commitar; se vazar em texto, rotacionar no Coolify.
