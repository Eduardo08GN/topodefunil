# 🌉 RUNBOOK — subir um LOTE de bridge pages, do domínio ao Telegram

> Escrito depois do **lote 4** (5 páginas, 2026-08-07), com o caminho que
> funcionou e **cada desvio que eu tomei no meio**. Não é teoria: toda linha do
> caminho ruim aconteceu neste build.
>
> A infra (UUIDs, endpoints, gotcha do repo privado) mora em
> [`RUNBOOK-deploy-coolify.md`](RUNBOOK-deploy-coolify.md). Aqui é a
> **sequência** e as armadilhas.

---

## ⛔⛔ A LIÇÃO QUE VALE POR TODAS AS OUTRAS

**`200 OK` neste sistema não significa "deu certo" em lugar nenhum.**

Três componentes diferentes respondem **200 enquanto descartam**, e cada um por
uma razão legítima:

| componente | responde 200 e descarta quando | por quê |
|---|---|---|
| `/api/funil/evento` | subid fora da allowlist | endpoint é público; não pode virar superfície de flood |
| `/api/funil/evento` | falta `sessaoId` ou `visitanteId` | payload inválido não derruba a bridge |
| webhook `/venda` | `?s=` errado ou ausente | *"não revela nada a quem sondar"* |

Neste build eu comemorei 200 **três vezes** e as três estavam vazias. Só o
banco e o log do contêiner dizem a verdade.

> **A regra:** depois de qualquer POST/GET de verificação, vá ao **banco** ou ao
> **log**. O código de status é o eco, não o resultado.

---

## ✅ O CAMINHO FELIZ, na ordem

### 0. Antes de escrever uma linha
```bash
for d in dominio1.site dominio2.site; do nslookup $d 8.8.8.8; done
```
O A record tem de apontar para `159.195.12.135`. Se ainda mostra `2.57.91.91`
(parking), **ninguém trocou** — não é propagação.

### 1. Decidir o que só o dono decide
- **VSL + `aff_id`** de cada página. Errar manda a comissão para outra conta.
- **Nome real da página do Facebook** — vai no alerta do Telegram.
- **Etnia do avatar** — congruência inviolável com o REF do criativo.

### 2. Pastas e assets
Copiar de uma bridge existente: `hero.png`, `peter.jpg` e os 4 logos. O build
**reprova** por asset faltando — e asset faltando só aparece como imagem
quebrada com a página já no ar.

### 3. As três pontas do `subid`
O `subid` é o **domínio sem o TLD** e tem de bater em **três** lugares:

```
bridge-pages/_build.py            → PAGINAS[].dominio
webhooks/vendas-telegram/app.py   → PAGINAS{} (chave)
automaweb/src/lib/funil-queries.ts → PAGINAS_FUNIL[].subid
```

Confira por **contagem**, não por leitura:
```
build 20 · notificador 20 · allowlist 20 · build−allowlist: nenhum
```

### 4. O cofre (só o dono)
```bash
python bridge-pages/_cofre.py --resselar
```
O build **aborta** até isso. A senha nunca passa pelo assistente.

### 5. Build → commit → push
```bash
python bridge-pages/_build.py      # espere "0 pagina(s) com problema"
```

### 6. Coolify: criar, apontar, deployar
Sempre `/applications/private-github-app` com o `github_app_uuid`. O endpoint
público falha no repo privado.
Domínio: `https://DOMINIO,http://<APP_UUID>.159.195.12.135.sslip.io` — o
segundo valida antes do DNS.

### 7. ⛔ DEPLOYAR TAMBÉM O QUE VOCÊ SÓ COMMITOU
Commit **não** é deploy. O `vendas-telegram` é uma app separada no Coolify
(`q6kqz7uoi21hx09y52wteh9i`); sem redeploy dela, o contêiner segue com o
`PAGINAS` velho e as páginas novas chegam sem nome.

### 8. Validar de verdade
```bash
curl -sL --max-time 30 "https://DOMINIO/" | wc -c     # ~12000, não 930
```
Depois: um evento com payload **completo** e conferência no banco; e um
`/venda?s=SEGREDO&subId=...&orderId=...` com leitura do **log do contêiner**.

---

## ⛔ O CAMINHO RUIM — o que eu fiz de errado neste build

### 1. Confiei no `200` do tracking
`POST /api/funil/evento` devolveu 200 nos 5 subids. **Zero gravou.** A rota
descarta payload sem `sessaoId`/`visitanteId` e responde `OK`.
**O tell:** nenhum. **A prova:** `SELECT ... WHERE visitanteId LIKE 'probe-%'`.

### 2. Confiei no `200` do webhook de vendas
Cinco `HTTP 200`, **zero mensagens**. O log do contêiner dizia
`[auth] segredo invalido` cinco vezes — falta o `?s=<WEBHOOK_SECRET>`, e o
endpoint responde 200 de propósito para não revelar nada a quem sonda.
**A prova:** `GET /api/v1/applications/<uuid>/logs`.

### 3. Nome de parâmetro chutado
`order_id` não existe: é **`orderId`**. E `event`, não `type`. Parâmetro errado
não dá erro — vira campo vazio na mensagem.

### 4. Substituição por string exata num arquivo que eu não tinha lido inteiro
O `assert VELHO in s` falhou porque uma edição anterior tinha quebrado a linha
em outro ponto. **Sempre** substitua por **faixa de linha** quando o alvo é um
bloco que já foi editado antes.

### 5. `%{size_download}` do curl conta o corpo COMPRIMIDO
Alarme falso: 930 bytes eram 12 KB em gzip. Para medir tamanho real, baixe e
conte caracteres.

### 6. `$?` depois de um pipe é do último comando do pipe
```bash
npx tsc --noEmit | head -5 ; echo $?     # ⛔ código do `head`, sempre 0
npx tsc --noEmit > log 2>&1 ; echo $?    # ✅
```
Isto me fez declarar "tsc limpo" com um erro `TS2304` na tela.

### 7. Variável de outro componente
Escrevi `linhas.length` no componente do **gráfico**, que só conhece `serie`. O
`tsc` pegou — mas só porque eu conferi o código de saída direito na segunda vez.

### 8. `grep | head -30` escondeu um motor
A varredura da cara de surpresa achou 3 agentes; o quarto (`trio`) vinha depois
no alfabeto e o `head` cortou. **Lente truncada não avisa que truncou** —
varredura de escopo tem de ser programática e contar o total.

### 9. Parser de `nslookup` lendo o IP errado
Procurei `address:` na saída e peguei o endereço do **servidor DNS**: um domínio
inventado deu "resolve". Use o resolvedor da linguagem, que levanta exceção.

### 10. Caracteres invisíveis no arquivo que avisa sobre caracteres invisíveis
Escrevi zero-width **literais** dentro do parágrafo que documenta o
`normalizeText`. Depois de qualquer heredoc ou colagem, varra o arquivo:
```python
[hex(ord(c)) for c in s if ord(c) < 32 and c not in "\n\t"]
```

---

## 🧾 O QUE FICA CONTAMINADO, e é honesto dizer

Testar de verdade deixa rastro. Neste lote:
- **2 eventos** com `visitanteId` começando em `probe-` (`mensrenewalhub`,
  `mensvitalhub`) — as outras 3 já tinham tráfego real.
- **5 vendas de teste** no Telegram e no JSONL do notificador, com
  `orderId` começando em `TESTE-`.

Prefira contaminar de forma **identificável** a declarar pronto sem prova.

---

## Conexões

- [`RUNBOOK-deploy-coolify.md`](RUNBOOK-deploy-coolify.md) — infra, UUIDs, o
  gotcha do repo privado
- [`bridge-pages-deploy.md`](bridge-pages-deploy.md) — inventário de domínios
- [`licoes-de-construcao.md`](licoes-de-construcao.md) — os mesmos modos de
  falha, do lado dos agentes. A causa raiz é uma só: **verificar a FORMA e
  declarar pronto sem verificar a FUNÇÃO**
