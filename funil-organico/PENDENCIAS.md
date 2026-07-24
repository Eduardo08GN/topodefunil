# Pendências da Operação

Backlog do que está em aberto. Atualizado em **2026-07-24**.
Cada item tem: por que importa, o que fazer e onde mexer.

Visão geral da operação: [`ARQUITETURA-OPERACAO.md`](ARQUITETURA-OPERACAO.md)

---

## 🔴 Alta — risco real se ficar parado

### 1. Rotacionar tokens expostos
Três credenciais apareceram em texto puro no chat/prints durante o setup:

| Token | Onde rotacionar | Impacto de não fazer |
|---|---|---|
| **Coolify API** | Coolify → Keys & Tokens | Acesso total ao VPS/apps |
| **Hostinger API** (`topodefunil`) | hPanel → API | Controle de DNS/domínios |
| **Telegram bot** (`MerchAffiliate_bot`) | @BotFather → `/revoke` | Terceiro manda mensagem no seu canal |

**Fazer:** revogar, gerar novo, atualizar onde é usado. O do Coolify é usado nos
scripts de deploy; o do Telegram está nas env vars do app `vendas-telegram`
(rotacionar lá também). Como a Ratoeira foi desativada, revogar o bot agora **não
quebra mais nada**.

### 2. `vendas.jsonl` não é persistente
O histórico de vendas do notificador vive em `/data/vendas.jsonl` **dentro do
container** — some a cada redeploy. Além de perder o histórico, **a dedup zera**
(risco de notificar venda antiga duas vezes).

**Fazer:** criar um volume persistente no Coolify pro app `vendas-telegram`
(UUID `q6kqz7uoi21hx09y52wteh9i`) montado em `/data`.
Ver [`notificacao-vendas-telegram.md`](notificacao-vendas-telegram.md).

---

## 🟡 Média — melhora robustez / cobertura

### 3. Postback de reembolso não registrado
O postback de **venda** (`event=sale_approved`) já está ativo no BuyGoods desde
2026-07-24. Falta o de **reembolso** — sem ele, estornos não aparecem e o número
de comissão fica otimista.

**Fazer:** BuyGoods → Postback pixels → Add new, mesma URL do notificador
trocando `event=sale_approved` por `event=sale_refunded`. O serviço **já trata**
(mostra "❌ REEMBOLSO").

### 4. Endpoint do notificador em HTTP/sslip.io
`http://q6kqz7uoi21hx09y52wteh9i.159.195.12.135.sslip.io` funciona, mas é HTTP e
depende do sslip.io.

**Fazer:** apontar um subdomínio (ex.: `hooks.<um-dos-dominios>`) pro VPS, setar
como FQDN do app no Coolify (Traefik emite o cert), e atualizar a URL nos
postbacks do BuyGoods. **Lembrar do gotcha:** depois de apontar DNS, é preciso
**redeploy** pro cert sair ([`bridge-pages-deploy.md`](bridge-pages-deploy.md)).

### 5. `wholelifenutri.shop` ainda no parking
6º domínio, comprado e com app no Coolify (`cwanszytythvm4myf8yye46k`), mas o DNS
nunca foi apontado — segue no parking da Hostinger.

**Fazer:** quando entrar a 6ª página, apontar A `@` e `www` → `159.195.12.135`
(TTL 300) no hPanel, criar a bridge e redeployar.

### 6. Dashboard "Tracking Funnel" no automaweb
Foi desenhado (tenant `topodefunil` com aba única) mas **não implementado**. O
`vendas.jsonl` do notificador é a fonte de dados natural pra ele.

**Fazer:** decidir se ainda faz sentido agora que o Telegram já notifica. Se sim:
model `FunilPagina` + flag `trackingFunilHabilitado` no tenant + a página do
dashboard (padrão do `organicwaveHabilitado`). Código em `projetosweb/automaweb`.

---

## 🟢 Baixa — limpeza

*(nada em aberto no momento)*

---

## ✔️ Concluídas (registro)

- **Utmify removida por completo (2026-07-24).** Script `cdn.utmify` tirado das 5
  bridges (redeployadas) e o postback `api4.utmify` **desativado** (Inactive) no
  BuyGoods. Notificação de venda agora é 100% nossa (BuyGoods → Telegram). O
  postback ficou como Inactive (não Deleted) — dá pra reativar se algum dia quiser.
- **`bridge-pages/bp-vick` removido (2026-07-24).** Variante Vigortrix órfã desde a
  migração pra Ragnaroak; `git rm` feito no `projetosweb`.

---

## ✅ Próximo passo operacional (não é pendência técnica)

Gerar os criativos das 5 páginas. Agora é simples: **`--fix mecanismo=gelatin`**
pra qualquer lote, porque Horsewood e Ragnaroak vendem o mesmo mecanismo.
Fluxo: [`AGENTE_ED_ORGANIC_WAVE_V5.md`](../AGENTE_ED_ORGANIC_WAVE_V5.md) +
[`randomizador-v5.py`](randomizador-v5.py) → AdBatch Vertical 5 → Veo Editor.
