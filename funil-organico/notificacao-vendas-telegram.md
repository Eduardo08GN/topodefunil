# Notificação de Vendas própria (BuyGoods + Hotmart → Telegram)

Sistema próprio de notificação de vendas, **sem depender de Utmify ou qualquer
terceiro**. O BuyGoods dispara o postback direto pro nosso serviço no VPS, que
manda a venda no Telegram e guarda o histórico.

```
BuyGoods (venda aprovada) ──postback GET──► nosso serviço (VPS/Coolify)
                                                 ├──► Telegram (notificação)
                                                 └──► vendas.jsonl (histórico nosso)
```

## Por que próprio

- **Sem mensalidade e sem terceiro** no meio do dado de faturamento. Substituiu a
  Utmify por completo (removida em 2026-07-24) — script e postback.
- **Traduz `subid` → nome da página** (você vê "Chuck's Men Welness Hub", não um slug).
- **O histórico é nosso** (`vendas.jsonl`) — é a matéria-prima do dashboard de
  tracking (guia "Tracking Funnel" do tenant no automaweb).
- Pega **os dois offers** (Horsewood e Ragnaroak): o postback do BuyGoods é global
  da conta de afiliado, não por oferta.
- **Convive com outros postbacks.** O BuyGoods aceita vários — dá pra rodar o
  nosso junto de qualquer outro sem conflito.

## Componentes

| Peça | Onde |
|---|---|
| Serviço | `projetosweb/webhooks/vendas-telegram/` (`app.py` + `Dockerfile`) |
| Runtime | Python 3.12 alpine, **stdlib pura** (sem dependência) |
| App Coolify | `vendas-telegram` — UUID `q6kqz7uoi21hx09y52wteh9i` |
| Endpoint | `http://q6kqz7uoi21hx09y52wteh9i.159.195.12.135.sslip.io/venda` |
| Histórico | `/data/vendas.jsonl` no container |

### Variáveis de ambiente (setadas no Coolify)
| Var | Papel |
|---|---|
| `TELEGRAM_BOT_TOKEN` | token do bot (@MerchAffiliate_bot) |
| `TELEGRAM_CHAT_ID` | `5676155351` (DM do Eduardo) |
| `WEBHOOK_SECRET` | segredo exigido no `?s=` da URL |

## Regras de projeto (aprendidas na marra)

1. **SEMPRE responder `OK` (200), mesmo em falha.** O painel do BuyGoods avisa:
   *"Make sure your script echoes something upon successful completion. If we
   receive no output from your script, we will assume it failed and keep calling
   it again and again."* Serviço que trava/erra = loop infinito de retry.
2. **Responder ANTES de falar com o Telegram.** O envio vai numa thread; travar
   na chamada do Telegram faria o BuyGoods achar que falhou.
3. **Dedup por `orderId:evento`.** O BuyGoods reenvia quando fica na dúvida —
   sem dedup você recebe a mesma venda várias vezes. Persistido no JSONL
   (sobrevive a restart).
4. **Segredo na URL (`?s=`).** O endpoint é público; sem segredo qualquer um
   forjaria "venda". Requisição sem segredo é ignorada mas responde `OK`
   (não revela nada a quem sonda).

## Formato da notificação

```
💰 VENDA APROVADA

💵 Comissao: US$ 52.30
📄 Oferta: Ragnaroak
📱 Pagina: Chuck's Men Welness Hub
🧾 Tipo: frontend
🛍 Produto: ragnaroak
🆔 Order: BG-8842119
```

O mapa `subid → página/oferta` fica em `PAGINAS` no `app.py` — atualizar lá ao
adicionar página nova.

## Registro no BuyGoods

BuyGoods → menu da conta (canto sup. direito) → **Postback pixels** → **Add new**:
- **URL:** `http://<endpoint>/venda?s=<SECRET>&orderId={ORDERID}&commission={COMMISSION_AMOUNT}&subId={SUBID}&type={CONV_TYPE}&product={PRODUCT_CODENAME}&event=sale_approved`
- **Status:** Active · **Event:** Purchase

Macros que o BuyGoods preenche: `{ORDERID}`, `{COMMISSION_AMOUNT}`, `{SUBID}`,
`{SUBID2..5}`, `{EMAILHASH}`, `{CONV_TYPE}`, `{PRODUCT_CODENAME}`.

> O `{SUBID}` só chega preenchido porque a bridge manda `&subid=<pagina>` pra VSL
> (ver [`bridge-pages-arquitetura.md`](bridge-pages-arquitetura.md)). É o que
> permite saber **qual página** vendeu.

## Manutenção

- **Ver histórico:** o `vendas.jsonl` fica no volume do container.
- **Adicionar página nova:** editar `PAGINAS` no `app.py` → push → redeploy.
- **Redeploy:** `GET http://159.195.12.135:8000/api/v1/deploy?uuid=q6kqz7uoi21hx09y52wteh9i`
- **Trocar bot/chat:** alterar as env vars no Coolify e redeployar.

## Segunda entrada: HOTMART (infoproduto 150 Receitas) — 2026-09-21

O mesmo serviço atende **dois gateways**. O BuyGoods (funil de ED) manda `GET`
com querystring em `/venda`; a Hotmart (ebook 150) manda **`POST` JSON** em
**`/hotmart`**. São rotas separadas de propósito — formatos e autenticação
diferentes, e juntar num handler só esconderia bug dos dois lados.

```
Hotmart (venda aprovada) ──POST JSON──► /hotmart ──► Telegram + vendas.jsonl
```

| Peça | Valor |
|---|---|
| Endpoint | `http://q6kqz7uoi21hx09y52wteh9i.159.195.12.135.sslip.io/hotmart?s=<HOTMART_URL_SECRET>` |
| Autenticação | `?s=` na URL **ou** `X-HOTMART-HOTTOK` no header (basta uma) |
| Env nova | `HOTMART_URL_SECRET` (separada do `WEBHOOK_SECRET` do BuyGoods) |
| Versão do webhook | 2.0.0 |

### Atribuição: de onde vem o nome da página

A landing põe `sck` e `src` no link de checkout, com **o mesmo slug** do
`data-subid` que ela já manda pro funil-tracker (domínio sem TLD — o
`slug_de()` do `_build.py`). Uma chave só para os dois sistemas:

```html
<a href="https://pay.hotmart.com/T107474501A?sck=bookdailyfactreport&amp;src=bookdailyfactreport">
```

| Idioma | Domínio | slug (`sck`) | Produto Hotmart |
|---|---|---|---|
| EN | `book.dailyfactreport.site` | `bookdailyfactreport` | 8458340 · `T107474501A` |
| DE | `book.plainfactsdaily.site` | `bookplainfactsdaily` | 8458435 · `K107474696C` |
| FR | `book.thedailyfinding.site` | `bookthedailyfinding` | 8458452 · `A107474735Q` |
| ES | `libro.dailyvitalreport.store` | `librodailyvitalreport` | ⏳ sem produto |
| IT | `libro.everydaydigest.site` | `libroeverydaydigest` | ⏳ sem produto |

ES e IT já estão no `PAGINAS_HOTMART` esperando: no dia que tiverem produto,
ninguém precisa lembrar deste arquivo.

### Decisões que custaram tempo

- ⛔⛔ **A doc da Hotmart responde 403 fora do painel** (CloudFront bloqueia
  `developers.hotmart.com`), e a aba *Histórico* estava vazia — conta sem venda
  não tem payload de exemplo. Por isso a extração de campos é **tolerante**:
  cada campo tenta vários caminhos, e o `sck` ainda tem busca profunda como
  último recurso. O payload cru vai inteiro pro JSONL, então **a primeira venda
  real é que permite apertar isso**. Conferir o JSONL depois da primeira venda.
- ⛔ **A aba *Autenticação* do painel não renderiza o hottok.** Foi por isso que
  a rota passou a aceitar `?s=` — depender só do hottok deixava o endpoint sem
  como ser protegido.
- ⚠️ **Responder 200 cedo vale aqui também, por motivo diferente:** a Hotmart
  reenvia o evento enquanto não receber 2xx. Mesma regra, outro gateway.
- ⚠️ **Venda sem `sck` grita na notificação** (`⚠️ veio sem sck — atribuição
  perdida`). Melhor um alerta feio na hora do que descobrir semanas depois,
  conferindo planilha, que não dá para saber qual idioma vendeu.
- ⚠️ **`&` no href tem de ser `&amp;`.** Dois parâmetros no link de checkout, e
  o HTML cru passa batido no navegador mas é erro de parse.

### Registro no painel da Hotmart

Ferramentas → **Webhook** → *Cadastrar Webhook*:
- **URL:** o endpoint acima, com o `?s=`
- **Versão:** 2.0.0
- **Produtos:** os três do 150 (não "todos" — a conta tem outros produtos com
  webhooks próprios: Appmestre, UTMify, Vturb)
- **Eventos:** `PURCHASE_APPROVED` no mínimo; o `app.py` também formata
  `PURCHASE_COMPLETE`, `PURCHASE_REFUNDED`, `PURCHASE_CHARGEBACK`,
  `PURCHASE_PROTEST`, `PURCHASE_BILLET_PRINTED` e carrinho abandonado.

> ⏳ **Pode esbarrar em HTTPS.** As quatro integrações já cadastradas na conta
> são todas `https://`, e o nosso endpoint é `http://` em sslip.io. Se o
> cadastro recusar, é o item "domínio próprio + HTTPS" das pendências abaixo
> que vira bloqueio — não é detalhe estético.

## Pendências / evolução

- [ ] Registrar também o postback de **reembolso** (`event=sale_refunded`).
- [ ] Domínio próprio + HTTPS no endpoint (hoje sslip.io/HTTP).
- [ ] Volume persistente pro `vendas.jsonl` (hoje vive no container; some no redeploy).
- [ ] Ligar o `vendas.jsonl` ao dashboard "Tracking Funnel" do automaweb.
