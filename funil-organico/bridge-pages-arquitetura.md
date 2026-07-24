# Arquitetura das Bridge Pages

Como cada bridge é feita e como editar/adicionar/trocar. Complementa a visão macro
em [`ARQUITETURA-OPERACAO.md`](ARQUITETURA-OPERACAO.md) e o status em
[`bridge-pages-deploy.md`](bridge-pages-deploy.md).

---

## Regra de ouro: bridge é MÍNIMA (máx 3 linhas de copy)

**A bridge page NÃO converte a venda — quem converte é a VSL.** A bridge só vende a
*continuação do clique*: leva o visitante do reel/DM pra VSL. Portanto:

- **No máximo 3 linhas de copy.** Nada de parágrafo, storytelling ou parede de texto.
  Na prática: **1 headline curto + 1 linha de CTA** + o hero clicável. O disclaimer
  legal fininho não conta.
- **O estilo/CSS é o mesmo em todas** — não precisa variar design. O que varia entre
  domínios é só a **COPY** (e o hero da oferta).
- Hero com **hash próprio** por bridge (imagem re-encodada) só pra não compartilhar
  fingerprint de arquivo idêntico entre domínios — barato e automático.

Contrato funcional (igual em todas): CTA com `id="offer"` + `href="#"`; um `<script>`
monta o link da VSL com `aff_id` + `sub_id` (atribuição por `?p=<slug>` → default
`direct`); `noindex,nofollow`; HTML autocontido; mobile-first.

---

## As 5 bridges (uma por domínio)

Mesmo template minimal; muda só a copy + hero + VSL.

| Domínio | Pasta (projetosweb) | Headline (copy) | VSL | Mec. | App UUID |
|---|---|---|---|---|---|
| `manresethub.pro` | `bp1` | "He's 67. And she's the one chasing now." | Horsewood | gelatin | `v5t2rojizir3dc37al4zkb4p` |
| `vitalresetlab.site` | `bp-vitalresetlab` | "One red bowl. Thirty seconds before bed." | Horsewood | gelatin | `bv4uhh6hpq6tkotyn42nagg3` |
| `primalvitalityhub.site` | `bp-primalvitalityhub` | "No pills. Just the red bowl." | Horsewood | gelatin | `srd3jdzrvc0n7ri3yetjjmuq` |
| `allmensnatural.site` | `bp-allmensnatural` | "The pharmacy-aisle jar men use before bed." | Vigortrix | vick | `iuge7sircaf0myor1jdl77jv` |
| `steadystrengthhub.site` | `bp-steadystrengthhub` | "He tried it before bed. She noticed by morning." | Vigortrix | vick | `xkma961zrq3jxraw5z4vpg47` |
| `wholelifenutri.shop` | — (reserva, DNS parking) | — | — | — | `cwanszytythvm4myf8yye46k` |

Cada uma tem também 1 linha de CTA curta ("Tap play now", "Watch before it's taken
down", etc.). Todas servem em `<domínio>/bp1/`. `bp-vick` está **deprecado/órfão**.

### Anatomia de uma pasta
```
bridge-pages/<bp-dominio>/
├── Dockerfile   # FROM nginx:alpine; COPY index.html + hero.* -> /html/bp1/
├── index.html   # ~1.8KB: headline + hero clicavel + 1 linha CTA + script + disclaimer
└── hero.png|.jpg
```
Fonte da verdade = `projetosweb` (Coolify puxa do GitHub). O bp1 de referência
também está em [`bridge-page/`](bridge-page/) no topodefunil.

---

## Contrato do link (não pode faltar)

```html
<a id="offer" href="#"><img src="hero.png|jpg"></a>
<script>(function(){
  var OFFER="<VSL_URL>", AFF="<AFF>";
  var q=new URLSearchParams(location.search);
  var p=(q.get("p")||q.get("sub_id")||"direct").toLowerCase().replace(/[^a-z0-9_]/g,"")||"direct";
  document.getElementById("offer").href=OFFER+"?aff_id="+encodeURIComponent(AFF)+"&sub_id="+encodeURIComponent(p);
})();</script>
```
- Horsewood: `OFFER="https://horsewood.us/vsl3/"`, `AFF="45158"`, hero `hero.png`.
- Vigortrix: `OFFER="https://vigortrix.com/vesp-l2/"`, `AFF="75486"`, hero `hero.jpg`.
- **Nunca cruzar** VSL/mecanismo entre páginas.

---

## Receitas

### Editar a copy de uma bridge
1. Edite o `<h1>` / `<p class="c">` do `projetosweb/bridge-pages/<bp>/index.html`
   (mantendo **≤3 linhas**) → `git push`.
2. Redeploy: `GET http://159.195.12.135:8000/api/v1/deploy?uuid=<UUID>` (Bearer token).
3. Valide: `<domínio>/bp1/` = 200 + VSL certa no HTML.

### Adicionar bridge nova
`projetosweb/bridge-pages/bp-<dominio>/` com Dockerfile + index.html (copie de um
existente, troque só copy/hero/OFFER/AFF) + hero re-encodado → push → repontar app
(`PATCH base_directory`) → redeploy → atualizar a tabela.

### Repontar base_directory
```bash
curl -s -X PATCH -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
  "http://159.195.12.135:8000/api/v1/applications/<UUID>" \
  -d '{"base_directory":"/bridge-pages/<bp-dominio>"}'
```

---

## Checklist ao criar/editar
- [ ] **≤3 linhas de copy** (headline + 1 CTA)? Sem parede de texto?
- [ ] VSL + aff certos do mecanismo da página (sem contaminação)?
- [ ] `#offer` + script de atribuição + `noindex` + disclaimer?
- [ ] Hero certo (gelatin=hero.png / vick=hero.jpg)?

## Gotchas
- **Cert não emite sozinho** após apontar DNS: precisa redeploy ([`bridge-pages-deploy.md`](bridge-pages-deploy.md)).
- **Repo privado:** apps via `/applications/private-github-app` + GitHub App ([`RUNBOOK-deploy-coolify.md`](RUNBOOK-deploy-coolify.md)).
- **Token da API:** nunca commitar; se vazar, rotacionar no Coolify.
