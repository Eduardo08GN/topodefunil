# Bridge Pages — Deploy & Domínios

Registro de todas as bridge pages do funil orgânico ED, hospedadas no VPS via Coolify.

## ⛔⛔ TRÊS DONOS DIVIDEM ESTE VPS — e só o VPS

| dono | pasta no `projetosweb` | apps | `aff_id` |
|---|---|---|---|
| **Ed** (esta operação) | `/bridge-pages` | um por domínio (`*-bp`, `*-bp1`) | **45158** · **2470** |
| **a PARCEIRA** (amiga do Ed) | `/parceira-bridges` | `parceira-bridges-4dom` — **um só, 10 domínios** | **52138** |
| **o LUCAS** | `/bridge-pages/bp-dailyvitalreport` e irmãos | `dailyvitalreport-bp` e irmãos | **44878** |

⚠️ **A parceira usa a MESMA oferta que o Ed** (`horsewood.us/VHG2-L1ML3/`). Ver
`horsewood` numa página dela **não é erro** — o que separa o dinheiro é o
**número** do `aff_id`. A conferência é sempre do número, nunca da oferta.

⛔ **O documento que garante o isolamento é
`projetosweb/parceira-bridges/PROPRIEDADE-E-ISOLAMENTO.md`** — mapa dos 10
domínios dela, as quatro camadas que impedem a mistura (guarda de afiliado que
aborta o build, pasta irmã, app próprio, `root` por domínio) e a receita para
acrescentar mais um. **Ler antes de tocar em `/parceira-bridges`.**

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
| Philippe Laurent | `morningritualmen.site` | `horsewood.us/VHG2-L1ML3/` | **45158** |
| Jason H. | `stridebackmen.site` | `horsewood.us/VHG2-L1ML3/` | **45158** |
| Earl Hodge | `menritualhub.site` | `horsewood.us/VHG2-L1ML3/` | **45158** |
| Dean Whitaker | `thefitmenhub.site` | `horsewood.us/VHG2-L1ML3/` | **45158** |
| Roy Tanner | `menvitalityhub.site` | `horsewood.us/VHG2-L1ML3/` | **45158** |
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

### ⭐⭐ 2026-08-06 — AS 10 PÁGINAS SE ESPALHARAM POR 5 DOMÍNIOS, 2 EM CADA

⛔ **`dailyvitalreport.store` não hospeda mais as 10.** O operador comprou 4
domínios e pediu a divisão: *"dessa forma as páginas ficarão mais seguras caso
um link seja marcado"*. Antes, um domínio marcado derrubava **as 10 URLs de uma
vez**; agora derruba **2**.

| Domínio | App Coolify (UUID) | Página | `subid` | Avatar |
|---|---|---|---|---|
| `dailyvitalreport.store` | `kw5fu21f7rad8fnklgf1iiqn` | Reggie Harris | `reggie` | homem negro |
| " | " | Jennifer Miller | `jennifer` | mulher branca |
| `dailyfactreport.site` | `uurhd13s9x1rei59f5gqm3jc` | Denise Walker | `denise` | mulher negra |
| " | " | Wayne Miller | `wayne` | homem branco |
| `plainfactsdaily.site` | `vx3q4f59noi9u5cr7fx6jzj3` | Otis & Gloria | `otisgloria` | casal negro |
| " | " | Dale Pruitt | `dale` | homem branco |
| `thedailyfinding.site` | `b5e8211hjaxecijcgybsvgde` | Curtis Grant | `curtis` | homem negro |
| " | " | Carol Whitfield | `carol` | mulher branca |
| `everydaydigest.site` | `goc65jdh6xw2po2ja3mk99sa` | Yvonne Bradley | `yvonne` | mulher negra |
| " | " | Hank & Marlene | `hankmarlene` | casal branco |

⚠️ **O pareamento não é aleatório:** cada domínio leva **uma página de avatar
negro e uma de avatar branco**. Um domínio marcado não apaga um demográfico
inteiro do funil.

⚠️ **Cada bridge tem marca própria** no `<title>` e nas páginas legais — Daily
Fact Report, Plain Facts Daily, The Daily Finding, Everyday Digest. São cinco
sites que se parecem, não cinco cópias com o nome trocado.

⛔ **As 8 pastas que migraram foram REMOVIDAS do `bp-dailyvitalreport`**, por
ordem do operador. Corte limpo: manter as URLs velhas vivas seria manter o alvo
grande, que é justamente o que a divisão desfaz.
⚠️ **Consequência:** `dailyvitalreport.store/{denise,wayne,otisgloria}` passou a
dar 404, e as bios dessas 3 páginas no Facebook precisaram ser trocadas.

A raiz de cada domínio serve a mesma matéria **sem** `subid`.

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

---

## O SPLIT ETNICO DAS 5 PAGINAS NOVAS (2026-08-05)

**3 avatares brancos · 2 avatares negros.** A decisao e' de VOLUME, e vale
separar duas coisas que se confundem:

- **Prevalencia** de disfuncao eretil e' MAIOR entre homens negros nos EUA —
  puxada pelas comorbidades (diabetes, hipertensao, obesidade).
- **Volume absoluto de compra** e' dos brancos: ~60% da populacao masculina
  adulta contra ~13% de negros. Mesmo com prevalencia menor, o numero de
  compradores e' varias vezes maior.

Para resposta direta o que paga escala e' volume absoluto -> a MAIORIA (branco)
leva 3 paginas, a minoria leva 2. Mesma proporcao das 5 paginas antigas
(Joe/Ray/Matt brancos, Marcus/Chuck negros).

⚠️ RESSALVA HONESTA: prevalencia e populacao sao dados que eu tenho com
confianca; **participacao de mercado por etnia em nutra de ED especificamente
nao e' dado publico que eu conheca** — a divisao acima e' inferencia de volume
populacional. Dado de plataforma (Meta Ads, Buy Goods) ganha desta inferencia.

| Pagina | Avatar | Dominio |
|---|---|---|
| Jason H. | negro, 50s, musculoso | `stridebackmen.site` |
| Philippe Laurent | negro, 50s, musculoso | `morningritualmen.site` |
| Roy Tanner | branco, 55, comum | `menvitalityhub.site` |
| Dean Whitaker | branco, 48, comum | `thefitmenhub.site` |
| Earl Hodge | branco, 60, comum | `menritualhub.site` |

⭐ A ETNIA DA PAGINA TRAVA A ETNIA DO REF DO CRIATIVO (congruencia inviolavel).
Ao acrescentar estas paginas ao `ETNIA` dos motores: Roy/Dean/Earl como
`white American`, Jason/Philippe como `Black American`.
