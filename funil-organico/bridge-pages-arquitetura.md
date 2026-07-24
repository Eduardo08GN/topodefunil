# Arquitetura das Bridge Pages

Como cada bridge é feita, por que **cada domínio tem um design próprio**
(anti-fingerprint), e como editar/adicionar/trocar. Complementa a visão macro em
[`ARQUITETURA-OPERACAO.md`](ARQUITETURA-OPERACAO.md) e o status em
[`bridge-pages-deploy.md`](bridge-pages-deploy.md).

---

## Princípio: 5 bridges DISTINTAS, não 1 template clonado

Cada domínio serve uma bridge com **design, layout, estrutura HTML e ângulo de copy
próprios** — nenhuma igual à outra. Motivos:

1. **Anti-fingerprint.** Rodar o mesmo template (mesmo CSS/estrutura) ou a mesma
   imagem (mesmo hash) em vários domínios é uma pegada que Facebook/redes detectam
   e derrubam em bloco. Bridges distintas = 5 pegadas diferentes.
2. **Teste de ângulo.** Genres diferentes convertem diferente — dá pra ver qual
   formato de bridge puxa mais clique pra VSL.

O que TODAS compartilham (contrato funcional, não visual):
- CTA principal com `id="offer"` e `href="#"`; um `<script>` monta o link da VSL
  com `aff_id` + `sub_id` (atribuição por `?p=<slug>` → default `direct`).
- `noindex,nofollow`, `<title>` discreto, disclaimer de wellness, HTML autocontido
  (CSS inline), mobile-first.
- **Hero com hash próprio:** a imagem-oferta é re-encodada por bridge (crop/brilho
  levemente diferentes) → arquivos com MD5 distinto, mesmo sendo a "mesma" criativa.

---

## As 5 bridges (uma por domínio)

| Domínio | Pasta (projetosweb) | Genre / design | VSL | Mecanismo | App UUID |
|---|---|---|---|---|---|
| `manresethub.pro` | `bridge-pages/bp1` | **Private video** (dark cinematográfico) | Horsewood | gelatin | `v5t2rojizir3dc37al4zkb4p` |
| `vitalresetlab.site` | `bridge-pages/bp-vitalresetlab` | **DM / thread de mensagem** ("here's the private video I promised you") | Horsewood | gelatin | `bv4uhh6hpq6tkotyn42nagg3` |
| `primalvitalityhub.site` | `bridge-pages/bp-primalvitalityhub` | **Bilhete manuscrito / receita** (papel, handwritten, polaroid) | Horsewood | gelatin | `srd3jdzrvc0n7ri3yetjjmuq` |
| `allmensnatural.site` | `bridge-pages/bp-allmensnatural` | **Aviso de remoção / sistema** (alert, contador) | Vigortrix | vick | `iuge7sircaf0myor1jdl77jv` |
| `steadystrengthhub.site` | `bridge-pages/bp-steadystrengthhub` | **Card de depoimento / review** (5 estrelas, quote) | Vigortrix | vick | `xkma961zrq3jxraw5z4vpg47` |
| `wholelifenutri.shop` | — (reserva, DNS parking) | — | — | — | `cwanszytythvm4myf8yye46k` |

Todas servem no caminho `/bp1/` (o Dockerfile copia pra `/usr/share/nginx/html/bp1/`),
então a URL pública é sempre `<domínio>/bp1/` — o que muda é o CONTEÚDO, definido
pelo `base_directory` do app no Coolify.

> `bridge-pages/bp-vick` está **DEPRECADO/órfão** (era o clone do bp1; nenhum app
> aponta mais pra ele). Foi substituído por bp-allmensnatural e bp-steadystrengthhub.

### Anatomia de uma pasta de bridge
```
bridge-pages/<bp-dominio>/
├── Dockerfile      # FROM nginx:alpine; COPY index.html + hero.* -> /html/bp1/
├── index.html      # design próprio + CTA #offer + script do link VSL + disclaimer
└── hero.png|.jpg   # criativa-oferta, re-encodada (hash único por bridge)
```

**Fonte da verdade = `projetosweb`** (o Coolify puxa do GitHub). O `topodefunil`
guarda a doc e o bp1 de referência em [`bridge-page/`](bridge-page/).

---

## Contrato do link (o que não pode faltar em nenhuma)

```html
<a id="offer" href="#">…CTA clicável…</a>
<script>(function(){
  var OFFER="<VSL_URL>", AFF="<AFF>";
  var q=new URLSearchParams(location.search);
  var p=(q.get("p")||q.get("sub_id")||"direct").toLowerCase().replace(/[^a-z0-9_]/g,"")||"direct";
  document.getElementById("offer").href=OFFER+"?aff_id="+encodeURIComponent(AFF)+"&sub_id="+encodeURIComponent(p);
})();</script>
```
- Horsewood: `OFFER="https://horsewood.us/vsl3/"`, `AFF="45158"`.
- Vigortrix: `OFFER="https://vigortrix.com/vesp-l2/"`, `AFF="75486"`.
- **Nunca cruzar:** bridge de página Horsewood só aponta Horsewood; Vigortrix só Vigortrix.

---

## Como o Coolify decide qual bridge

Cada app tem `base_directory = /bridge-pages/<bp-dominio>`. Trocar/atualizar =
mudar o conteúdo da pasta (ou o base_directory) + redeployar.

## Receitas

### Editar uma bridge (copy/design/hero)
1. Edite `projetosweb/bridge-pages/<bp-dominio>/` → `git push`.
2. Redeploy do app: `GET http://159.195.12.135:8000/api/v1/deploy?uuid=<UUID>` (Bearer token).
3. Valide: `<domínio>/bp1/` (200) + `/bp1/hero.*` (200) + marcador do genre presente.

### Adicionar uma bridge nova (novo domínio/página)
1. `projetosweb/bridge-pages/bp-<dominio>/` com Dockerfile + index.html (design
   NOVO, distinto dos existentes) + hero re-encodado (hash próprio).
2. `git push` no projetosweb.
3. Repontar o app pro novo `base_directory` (PATCH) + redeploy.
4. Atualize a tabela acima.

### Trocar a VSL de um domínio
Edite o `OFFER`/`AFF` no `<script>` do index.html daquela bridge → push → redeploy.
(Se a nova VSL for outro mecanismo, alinhe os criativos daquela página.)

### Repontar base_directory (PATCH)
```bash
curl -s -X PATCH -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
  "http://159.195.12.135:8000/api/v1/applications/<UUID>" \
  -d '{"base_directory":"/bridge-pages/<bp-dominio>"}'
```

---

## Anti-fingerprint — checklist ao criar/editar
- [ ] HTML/CSS/estrutura **diferente** das outras 4 (não reaproveitar o mesmo arquivo)?
- [ ] Genre/ângulo de copy próprio?
- [ ] Hero re-encodado (MD5 diferente das outras)?
- [ ] Roteamento certo (VSL+aff do mecanismo da página, sem contaminação)?
- [ ] `#offer` + script de atribuição + noindex + disclaimer presentes?

## Gotchas herdados
- **Cert não emite sozinho** após apontar DNS: precisa redeploy (ver [`bridge-pages-deploy.md`](bridge-pages-deploy.md)).
- **Repo privado:** apps via `/applications/private-github-app` + GitHub App ([`RUNBOOK-deploy-coolify.md`](RUNBOOK-deploy-coolify.md)).
- **Token da API:** nunca commitar; se vazar em texto, rotacionar no Coolify.
