# Bridge Pages — Deploy & Domínios

Registro de todas as bridge pages do funil orgânico ED, hospedadas no VPS via Coolify.

## Infra

- **VPS:** `159.195.12.135` (Netcup)
- **Orquestrador:** Coolify v4.1.2 — instância em `http://159.195.12.135:8000`
- **Reverse proxy:** Traefik (SSL automático via Let's Encrypt)
- **Source dos apps:** repo privado `Eduardo08GN/projetosweb`, branch `main`, GitHub App `coolify-projetosweb`
- **Build:** Dockerfile em `/bridge-pages/bp1` (nginx:alpine servindo `index.html` + `hero.png` em `/bp1/`)
- **Página servida em:** `<dominio>/bp1/`

## Link de destino (oferta) — ⚠️ NÃO É ÚNICO, TEM SPLIT

⛔ **Não existe um destino global.** Cada bridge aponta para a VSL da **sua** página. Uma
versão anterior deste documento declarava Horsewood para todas — isso manda a comissão
do Chuck e do Matt para o afiliado errado. Foi esse erro que motivou deletar o
redirector central (ver [ARQUITETURA-OPERACAO](ARQUITETURA-OPERACAO.md)).

| Página | Domínio da bridge | VSL de destino | `aff_id` |
|---|---|---|---|
| Joe | `manresethub.pro` | `horsewood.us/VHG2-L1ML3/` | **45158** |
| Marcus | `vitalresetlab.site` | `horsewood.us/VHG2-L1ML3/` | **45158** |
| Ray | `primalvitalityhub.site` | `horsewood.us/VHG2-L1ML3/` | **45158** |
| Chuck | `allmensnatural.site` | `ragnaroak.us/VHGML5-3/` | **2470** |
| Matt | `steadystrengthhub.site` | `ragnaroak.us/VHGML5-3/` | **2470** |
| Hank | `secondwindformen.site` | `horsewood.us/VHG2-L1ML3/` | **45158** |
| _(a definir)_ | `morningritualmen.site` | `horsewood.us/VHG2-L1ML3/` | **45158** |
| _(a definir)_ | `stridebackmen.site` | `horsewood.us/VHG2-L1ML3/` | **45158** |
| _(a definir)_ | `menritualhub.site` | `horsewood.us/VHG2-L1ML3/` | **45158** |
| _(a definir)_ | `thefitmenhub.site` | `horsewood.us/VHG2-L1ML3/` | **45158** |
| _(a definir)_ | `menvitalityhub.site` | `horsewood.us/VHG2-L1ML3/` | **45158** |
| Wade | `strengthandflow.site` | `horsewood.us/VHG2-L1ML3/` | **45158** |
| Isaiah | `dailyvitalitymethod.site` | `horsewood.us/VHG2-L1ML3/` | **45158** |
| Curtis | `menresethub.site` | `horsewood.us/VHG2-L1ML3/` | **45158** |
| Otis | `mensresetclub.online` | `horsewood.us/VHG2-L1ML3/` | **45158** |

```
https://<vsl-da-pagina>/?aff_id=<aff-da-pagina>&subid=<pagina>
```

- `aff_id` → comissão. **45158 = Horsewood · 2470 = Ragnaroak.** Conferir na tabela.
- `subid` → atribuição por página (lido de `?p=<slug>` na URL da bridge; default `direct`)

> ⚠️ **Na saída é `subid`, nunca `sub_id`.** O BuyGoods documenta `&subid=`; com
> `sub_id` a venda entra **sem atribuição** e o notificador não sabe qual página vendeu.
> Na *entrada* a bridge aceita `?p=` (padrão) e tolera `subid`/`sub_id` como legado.
>
> ✅ **Verificado em produção em 2026-07-28** (`curl` nos 3 domínios): o split e o
> `&subid=` estão corretos no ar. O erro era **deste documento**, não do deploy.

## Domínios & Apps

| # | Domínio | App Coolify (UUID) | URL de teste (sslip.io) | Status |
|---|---------|--------------------|-----------------------|------------|
| 1 | `manresethub.pro` | `v5t2rojizir3dc37al4zkb4p` | `http://v5t2rojizir3dc37al4zkb4p.159.195.12.135.sslip.io/bp1/` | ✅ **no ar** (HTTPS) |
| 2 | `wholelifenutri.shop` | `cwanszytythvm4myf8yye46k` | `http://cwanszytythvm4myf8yye46k.159.195.12.135.sslip.io/bp1/` | ⚠️ pendente (parking) |
| 3 | `vitalresetlab.site` | `bv4uhh6hpq6tkotyn42nagg3` | `http://bv4uhh6hpq6tkotyn42nagg3.159.195.12.135.sslip.io/bp1/` | ✅ **no ar** (HTTPS) |
| 4 | `primalvitalityhub.site` | `srd3jdzrvc0n7ri3yetjjmuq` | `http://srd3jdzrvc0n7ri3yetjjmuq.159.195.12.135.sslip.io/bp1/` | ✅ **no ar** (HTTPS) |
| 5 | `allmensnatural.site` | `iuge7sircaf0myor1jdl77jv` | `http://iuge7sircaf0myor1jdl77jv.159.195.12.135.sslip.io/bp1/` | ✅ **no ar** (HTTPS) |
| 6 | `steadystrengthhub.site` | `xkma961zrq3jxraw5z4vpg47` | `http://xkma961zrq3jxraw5z4vpg47.159.195.12.135.sslip.io/bp1/` | ✅ **no ar** (HTTPS) |
| 7 | `secondwindformen.site` | `p6b0bb2bsbychxyzs8m0axzp` | — | ✅ **no ar** (HTTPS) |
| 8 | `strengthandflow.site` | `t8koxrte3s7530p5b6mazkjv` | — | ✅ **no ar** (HTTPS) |
| 9 | `dailyvitalitymethod.site` | `tqwepmv042n3y13xiy68ve0v` | — | ✅ **no ar** (HTTPS) |
| 10 | `menresethub.site` | `u3szzoq1y9vcgoapsi2jnq0e` | — | ✅ **no ar** (HTTPS) |
| 11 | `mensresetclub.online` | `t9wzm0j2pctbql7tsu3nbbor` | — | ✅ **no ar** (HTTPS) |
| 13 | `morningritualmen.site` | `tlx57qzzdzscgypkkkw61505` | — | ✅ **no ar** (HTTPS, 2026-08-04) |
| 14 | `stridebackmen.site` | `idx2ek34etgj5dmpspc59iuu` | — | ✅ **no ar** (HTTPS, 2026-08-04) |
| 15 | `menritualhub.site` | `k1476zn3nxztce9yi07rf75p` | — | ✅ **no ar** (HTTPS, 2026-08-04) |
| 16 | `thefitmenhub.site` | `oi771du8quctmppyogchvo7l` | — | ✅ **no ar** (HTTPS, 2026-08-04) |
| 17 | `menvitalityhub.site` | `x1369zh3c0wjkfp3m0m3rffa` | — | ✅ **no ar** (HTTPS, 2026-08-04) |

> ⚠️ **As cinco de 2026-08-04 servem de `/bridge-pages/bp-<slug>`, não de `bp1`.**
> Cada uma tem pasta própria com Dockerfile, `hero.png` e `index.html` — o
> `bp1` é só a do Joe. E o `pagina` das cinco está `(a definir)` no `_build.py`
> e `[definir]` no dict do `webhooks/vendas-telegram`, **de propósito**: o
> notificador precisa do nome REAL da página do Facebook, e nome plausível e
> errado já custou uma venda sem origem (o fantasma `Dale`). Trocar assim que
> as páginas existirem.
>
> ✅ **Postback testado nos cinco em 2026-08-04**, no endpoint `/venda` (não em
> `/`, que é o health check e responde `OK` sem notificar nada). Controle
> negativo com segredo errado registrou `[auth] segredo invalido`; os cinco
> reais não geraram nenhuma linha `[telegram] ... falhou`, e as cinco
> mensagens chegaram no Telegram com o domínio certo.
| 12 | `dailyvitalreport.store` ⛔ **do LUCAS** | `kw5fu21f7rad8fnklgf1iiqn` | `http://kw5fu21f7rad8fnklgf1iiqn.159.195.12.135.sslip.io/` | ✅ **no ar** (HTTPS) |

### ⛔⛔ O #12 NÃO É DESTA OPERAÇÃO — não misturar

`dailyvitalreport.store` é do **Lucas**, subiu em 2026-08-03 e divide só o VPS.
Tudo o mais é separado, e a confusão aqui custa comissão indo para a pessoa
errada:

| | os 11 acima | o #12 |
|---|---|---|
| pasta no `projetosweb` | `bridge-pages/bp-<dominio>` | `bridge-pages/bp-dailyvitalreport` |
| oferta | Horsewood `VHG2-L1ML3` · Ragnaroak `VHGML5-3` | `horsewood.us/VHGTH-L3/` |
| `aff_id` | **45158** · **2470** | **44878** |
| gerado por | `bridge-pages/_build.py` | ⛔ **fora do `_build.py`, de propósito** |

⛔ **Não acrescentar `bp-dailyvitalreport` à tabela `PAGINAS` do `_build.py`.**
O gerador reescreveria o `aff_id` do Lucas com um dos desta operação no
próximo build — que é exatamente o erro que motivou deletar o redirector
central.

**As 5 URLs dele**, uma por página de Facebook, cada uma com o `subid` fixo no
HTML (sem JS):

| Página | URL | `subid` |
|---|---|---|
| Reggie Harris | `dailyvitalreport.store/reggie` | `reggie` |
| Otis & Gloria Living | `dailyvitalreport.store/otisgloria` | `otisgloria` |
| Denise Walker | `dailyvitalreport.store/denise` | `denise` |
| Wayne Miller | `dailyvitalreport.store/wayne` | `wayne` |
| Jennifer Moore | `dailyvitalreport.store/jennifer` | `jennifer` |

**⭐ Lote 2 — 2026-08-05** (5 páginas novas do Lucas, mesmas regras):

| Página | URL | `subid` | Perfil |
|---|---|---|---|
| Yvonne Bradley | `dailyvitalreport.store/yvonne` | `yvonne` | mulher negra |
| Curtis Grant | `dailyvitalreport.store/curtis` | `curtis` | homem negro |
| Carol Whitfield | `dailyvitalreport.store/carol` | `carol` | mulher branca |
| Hank & Marlene Daily | `dailyvitalreport.store/hankmarlene` | `hankmarlene` | casal branco |
| Dale Pruitt | `dailyvitalreport.store/dale` | `dale` | homem branco |

A raiz `dailyvitalreport.store/` serve a mesma matéria **sem** `subid`.

⭐ **O app tem auto-deploy pelo webhook do GitHub App.** O lote 2 subiu sozinho
depois do `git push` no `projetosweb` — não foi preciso chamar
`POST /api/v1/deploy`. Levou menos de 2 minutos entre o push e as 5 URLs
respondendo 200.

✅ **Verificado no ar em 2026-08-05** (`curl` nas 10 URLs): cada uma com 4 links,
`aff_id=44878` em todas e o `subid` próprio de cada página, `hero.jpg` em 200.
⚠️ **200 não prova conteúdo** — a conferência é do `subid` renderizado, não do
código de status: uma pasta copiada sem trocar o `subid` responderia 200 e
mandaria a atribuição para a página errada.

### ⭐ Lote 2 — 2026-08-03: qual página do Facebook usa qual bridge

⛔ **O pareamento é 1:1 e a fonte da verdade é este quadro** (repetido no
[`automacao-comentario-dm.md`](automacao-comentario-dm.md), que é onde o link vai
para dentro da DM).

| Página no Facebook | Bridge | `subid` | UUID Coolify |
|---|---|---|---|
| Hank Male Tips Hub | `secondwindformen.site` | `secondwindformen` | `p6b0bb2bsbychxyzs8m0axzp` |
| Wade All Natural Hub | `strengthandflow.site` | `strengthandflow` | `t8koxrte3s7530p5b6mazkjv` |
| Isaiah Vitality Men Tips | `dailyvitalitymethod.site` | `dailyvitalitymethod` | `tqwepmv042n3y13xiy68ve0v` |
| Curtis Reset Hub | `menresethub.site` | `menresethub` | `u3szzoq1y9vcgoapsi2jnq0e` |
| Otis Men Reset Hub | `mensresetclub.online` | `mensresetclub` | `t9wzm0j2pctbql7tsu3nbbor` |

> ⚠️ **`menresethub.site` (Curtis) NÃO é `manresethub.pro` (Joe).** Uma letra —
> **men** contra **man** — separa duas páginas diferentes, e as duas estão no ar.
> Trocar o link manda a venda do Curtis para a atribuição do Joe, e a notificação
> do Telegram mostra a página errada sem acusar erro nenhum.
>
> ⚠️ **"Wade All Natural Hub" (página) NÃO é `allmensnatural.site` (bridge do
> Chuck).** O nome da página ecoa o domínio de outra; o Wade vai para
> `strengthandflow.site`.

⭐ **Tracking conferido em produção em 2026-08-03**: as 5 servem o próprio `subid`
por padrão (sem depender do `?p=`), `aff_id=45158`, e o circuito
bridge → BuyGoods → Telegram foi testado de ponta a ponta com controles (segredo
inválido barrado, dedup funcionando, subid fora do mapa caindo como slug cru).

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
