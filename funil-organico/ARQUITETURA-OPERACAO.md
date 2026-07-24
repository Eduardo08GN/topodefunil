# Arquitetura da Operação — Funil Orgânico ED (US)

Mapa-mestre da operação: perfil → páginas → bridge pages → VSLs → comissão.
Nicho: disfunção erétil / men's wellness, mercado US, tráfego **orgânico** (reels
no Facebook, sem anúncio pago).

> Fase inicial: **1 perfil → 5 páginas → 5 bridge pages (domínios distintos) → 2 VSLs.**

---

## Fluxo macro

```
Perfil pessoal (Eduardo Nogueira)
      │  vincula
      ▼
5 páginas de fãs (personas men's wellness)
      │  cada reel pede "Comment [KEYWORD]"
      ▼
DM automation entrega o link
      ▼
Bridge page (domínio próprio, /bp1/) — "Private video"
      │  clique no hero
      ▼
VSL de afiliado (Horsewood OU Vigortrix) + aff_id + sub_id
      ▼
💰 comissão
```

**Regra de congruência (inegociável):** o mecanismo do CRIATIVO tem que casar com
o mecanismo que a VSL daquela página vende. Página que roda **Vigortrix** só posta
criativo de **Vick VapoRub trick**. Página que roda **Horsewood** posta o mecanismo
do Horsewood (**gelatin trick**). Nunca cruze: criativo de vick
levando pra VSL de gelatin mata a conversão e a credibilidade.

---

## As 2 VSLs (ofertas de afiliado)

| VSL | Link direto | aff_id | Mecanismo | Nº de páginas |
|---|---|---|---|---|
| **Horsewood** | `https://horsewood.us/vsl3/?aff_id=45158&sub_id=<pagina>` | 45158 | **Gelatin trick** (red bowl) | **3** |
| **Vigortrix** | `https://vigortrix.com/vesp-l2/?aff_id=75486&sub_id=<pagina>` | 75486 | **Vick VapoRub trick** | **2** |

- `sub_id=<pagina>` → atribuição por página (lido do `?p=<slug>` na URL da bridge; default `direct`).
- **Horsewood = Gelatin trick** (confirmado). A bridge vende "the red bowl"
  (gelatina vermelha no hero); os criativos das 3 páginas Horsewood usam o
  mecanismo **gelatin** → fixar `mecanismo=gelatin` no randomizador (PASSO 0).
- **Vigortrix = Vick trick** → fixar `mecanismo=vick`.

---

## As 5 páginas (1 perfil)

Perfil dono: **Eduardo Nogueira**. Todas as páginas são "Página de fãs", mercado
US, 0 seguidores (recém-criadas), foto de perfil = homem 45+ + estética natural.

| # | Página | Page ID | Bio (essência) |
|---|---|---|---|
| 1 | **Joe's Wellness hub** | `61553002709366` | "for guys who are tired of vague advice and just want something concrete they can try today, at home, with what they already have." |
| 2 | **Chuck's Men Welness Hub** | `61553010659077` | fitness/praia, casal maduro (capa beach workout) |
| 3 | **Marcus' Men Reset Hub** | `61553077015815` | "simple daily habits for men who want to feel strong, energized and alive again, the natural way. For guys over 45 ready to reset their energy, movement and confidence." |
| 4 | **Matt's Natural Reset Tips** | `61553069396197` | "simple daily habits for building a stronger body and a clearer mind, the natural way. For men who want to reset their energy, movement." |
| 5 | **Ray's Natural Vitality Hub** | `61553015908598` | "for men over 45 who are tired of vague advice... Simple food, small daily habits and natural ways to bring back your energy, circulation and drive." |

---

## Mapeamento página → domínio → VSL (DEFINIDO)

Split: **3 Horsewood (gelatin) / 2 Vigortrix (vick)**. Domínios = os 5 já no ar
(ver [`bridge-pages-deploy.md`](bridge-pages-deploy.md)); `wholelifenutri.shop`
fica de **reserva**. Mapeamento fechado e **consistente com o deploy atual**.

| Página | Domínio (bridge) | VSL | Mecanismo dos criativos |
|---|---|---|---|
| Joe's Wellness hub | `manresethub.pro` | **Horsewood** | **gelatin trick** |
| Marcus' Men Reset Hub | `vitalresetlab.site` | **Horsewood** | **gelatin trick** |
| Ray's Natural Vitality Hub | `primalvitalityhub.site` | **Horsewood** | **gelatin trick** |
| Chuck's Men Welness Hub | `allmensnatural.site` | **Vigortrix** | **vick trick** |
| Matt's Natural Reset Tips | `steadystrengthhub.site` | **Vigortrix** | **vick trick** |

> Para trocar uma página de VSL: mude a linha aqui + repointe a variante da bridge
> no domínio (receita em [`bridge-pages-arquitetura.md`](bridge-pages-arquitetura.md)).

Reserva: `wholelifenutri.shop` (no ar como parking até apontar DNS; sobra pra 6ª
página futura).

---

## Bridge pages: 5 designs DISTINTOS (anti-fingerprint)

Cada domínio serve `/bp1/` com uma bridge de **design próprio** — nenhuma igual à
outra (evita pegada de template repetido entre domínios). Todas roteiam pro clique
na VSL da sua página, com atribuição `?p=<slug>` → `sub_id`.

| Domínio | Genre da bridge | VSL |
|---|---|---|
| `manresethub.pro` | Private video (dark) | Horsewood (gelatin) |
| `vitalresetlab.site` | DM / thread de mensagem | Horsewood (gelatin) |
| `primalvitalityhub.site` | Bilhete manuscrito / receita | Horsewood (gelatin) |
| `allmensnatural.site` | Aviso de remoção / sistema | Vigortrix (vick) |
| `steadystrengthhub.site` | Card de depoimento / review | Vigortrix (vick) |

Cada bridge também usa um hero com **hash próprio** (imagem re-encodada) pra não
compartilhar fingerprint de arquivo. Detalhe técnico (pastas, deploy, receitas) em
[`bridge-pages-arquitetura.md`](bridge-pages-arquitetura.md).

---

## Pipeline de criativos (referência)

Os reels de cada página saem da esteira:
1. **Agente Organic Wave V5** (`AGENTE_ED_ORGANIC_WAVE_V5.md`) + `randomizador-v5.py`
   → roteiros REF+5 IMAGE+5 TAKE, com o **mecanismo travado** conforme a VSL da
   página (vick para páginas Vigortrix; gelatin/honey para páginas Horsewood).
2. **AdBatch Vertical 5** (Flow/Veo) → imagens + takes → `.zip`.
3. **Veo Editor** (esteira) → junta, desilencia, varia velocidade, legenda karaoke
   com keyword destacada.
4. Postagem orgânica na página → keyword no comentário → DM → bridge → VSL.

**Congruência na prática:** ao gerar um lote para uma página Vigortrix, fixar
`mecanismo=vick` no randomizador (PASSO 0). Para páginas Horsewood, fixar
`mecanismo=gelatin`.

---

## Inventário rápido

- **Perfil:** Eduardo Nogueira → 5 páginas (IDs acima).
- **VSLs:** Horsewood (aff 45158), Vigortrix (aff 75486, vick).
- **Domínios:** 5 no ar + `wholelifenutri.shop` reserva ([`bridge-pages-deploy.md`](bridge-pages-deploy.md)).
- **Bridges:** variante Horsewood (feita) + variante Vigortrix (a criar).
- **Infra:** VPS `159.195.12.135`, Coolify, Traefik+SSL ([`RUNBOOK-deploy-coolify.md`](RUNBOOK-deploy-coolify.md)).
