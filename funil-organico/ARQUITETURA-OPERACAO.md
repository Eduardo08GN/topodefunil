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
VSL de afiliado (Horsewood OU Ragnaroak) + aff_id + subid
      ▼
💰 comissão
```

**Regra de congruência de MECANISMO (inegociável):** o mecanismo do CRIATIVO tem
que casar com o mecanismo que a VSL daquela página vende. Hoje as duas VSLs
(Horsewood e Ragnaroak) vendem o **mesmo mecanismo — gelatin trick** — então todas
as 5 páginas postam criativo de gelatin. Se um dia entrar uma VSL de outro
mecanismo, as páginas dela têm que trocar de criativo junto: criativo de um
mecanismo levando pra VSL de outro mata a conversão e a credibilidade.

**Regra de congruência de CASTING/ETNIA (inegociável):** a etnia do personagem REF
do criativo tem que casar com a etnia do AVATAR da página. **Página com avatar de
pele escura recebe SÓ criativos com REF de pele escura (afro-americano US).** Nunca
cruzar: avatar negro postando REF branco (ou vice-versa) quebra a verossimilhança
e denuncia a operação como fabricada. Na prática: travar `--fix etnia=negro` (que
governa homem E parceira) junto do `--fix mecanismo=gelatin` ao gerar o lote de uma
página de avatar escuro. Ver coluna "Etnia do avatar" no mapeamento abaixo.

---

## As 2 VSLs (ofertas de afiliado)

| VSL | Link direto | aff_id | Mecanismo | Nº de páginas |
|---|---|---|---|---|
| **Horsewood** | `https://horsewood.us/vsl3/?aff_id=45158&subid=<pagina>` | 45158 | **Gelatin trick** (red bowl) | **3** |
| **Ragnaroak** | `https://ragnaroak.us/VHGML5-3/?aff_id=2470&subid=<pagina>` | 2470 | **Gelatin trick** (mesmo do Horsewood) | **2** |

- `subid=<pagina>` → atribuição por página (lido do `?p=<slug>` na URL da bridge; default `direct`).
- **As DUAS VSLs vendem o mesmo mecanismo: gelatin trick.** Vigortrix (vick) foi
  desativado em 2026-07-24 e substituído pelo Ragnaroak.
- **Consequência prática:** TODAS as 5 páginas usam criativos de **gelatin** →
  fixar `mecanismo=gelatin` no randomizador (PASSO 0) para qualquer lote.
- **Vira um A/B de VSL:** mesmo mecanismo e mesmo tipo de criativo em todas; 3
  páginas mandam pro Horsewood e 2 pro Ragnaroak. Dá pra comparar qual VSL
  converte melhor com o tráfego equivalente.

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

Split: **3 Horsewood / 2 Ragnaroak** (ambos gelatin trick). Domínios = os 5 já no ar
(ver [`bridge-pages-deploy.md`](bridge-pages-deploy.md)); `wholelifenutri.shop`
fica de **reserva**. Mapeamento fechado e **consistente com o deploy atual**.

| Página | Domínio (bridge) | VSL | Etnia do avatar | `--fix` do lote (V5) |
|---|---|---|---|---|
| Joe's Wellness hub | `manresethub.pro` | **Horsewood** | branco | `mecanismo=gelatin etnia=branco` |
| Marcus' Men Reset Hub | `vitalresetlab.site` | **Horsewood** | **negro** | `mecanismo=gelatin etnia=negro` |
| Ray's Natural Vitality Hub | `primalvitalityhub.site` | **Horsewood** | branco | `mecanismo=gelatin etnia=branco` |
| Chuck's Men Welness Hub | `allmensnatural.site` | **Ragnaroak** | **negro** | `mecanismo=gelatin etnia=negro` |
| Matt's Natural Reset Tips | `steadystrengthhub.site` | **Ragnaroak** | branco | `mecanismo=gelatin etnia=branco` |

> **Casting travado por avatar:** Marcus' e Chuck's têm avatar de **casal negro** →
> criativos SÓ com REF afro-americano US (homem **e** parceira). As outras três têm
> avatar de homem branco → REF branco. O eixo `etnia` no randomizador governa o
> casting inteiro (homem + mulher do casal) de uma vez — basta o `--fix etnia=` da
> coluna acima. Ver [regra de congruência de casting](#) acima.

> Para trocar uma página de VSL: mude a linha aqui + repointe a variante da bridge
> no domínio (receita em [`bridge-pages-arquitetura.md`](bridge-pages-arquitetura.md)).

Reserva: `wholelifenutri.shop` (no ar como parking até apontar DNS; sobra pra 6ª
página futura).

---

## Bridge pages: MÍNIMAS (a VSL vende, a bridge só entrega o clique)

Regra de ouro: **bridge = no máx. 3 linhas de copy** (1 headline + 1 CTA + o hero
clicável). Ela não converte a venda — quem converte é a VSL. Mesmo estilo/CSS em
todas; o que **varia entre domínios é só a copy** (e o hero da oferta). Todas
roteiam pro clique na VSL com atribuição `?p=<slug>` → `subid`.

| Domínio | Headline (copy) | VSL |
|---|---|---|
| `manresethub.pro` | "He's 67. And she's the one chasing now." | Horsewood (gelatin) |
| `vitalresetlab.site` | "One red bowl. Thirty seconds before bed." | Horsewood (gelatin) |
| `primalvitalityhub.site` | "No pills. Just the red bowl." | Horsewood (gelatin) |
| `allmensnatural.site` | "The red bowl he keeps by the bed." | Ragnaroak (gelatin) |
| `steadystrengthhub.site` | "He ate it before bed. She noticed by morning." | Ragnaroak (gelatin) |

Detalhe técnico (pastas, deploy, receitas, contrato do link) em
[`bridge-pages-arquitetura.md`](bridge-pages-arquitetura.md).

---

## Pipeline de criativos (referência)

Os reels de cada página saem da esteira:
1. **Agente Organic Wave V5** (`AGENTE_ED_ORGANIC_WAVE_V5.md`) + `randomizador-v5.py`
   → roteiros REF+5 IMAGE+5 TAKE, com o **mecanismo travado** conforme a VSL da
   página — hoje **gelatin em todas** (as duas VSLs vendem gelatin trick).
2. **AdBatch Vertical 5** (Flow/Veo) → imagens + takes → `.zip`.
3. **Veo Editor** (esteira) → junta, desilencia, varia velocidade, legenda karaoke
   com keyword destacada.
4. Postagem orgânica na página → keyword no comentário → DM → bridge → VSL.

**Congruência na prática:** hoje é simples — fixar `mecanismo=gelatin` no
randomizador (PASSO 0) para QUALQUER página, porque Horsewood e Ragnaroak vendem
o mesmo mecanismo.

---

## Inventário rápido

- **Perfil:** Eduardo Nogueira → 5 páginas (IDs acima).
- **VSLs:** Horsewood (aff 45158) e Ragnaroak (aff 2470) — **ambas gelatin trick**, ambas no **BuyGoods** (mesma conta: HorseWood [12662], RAGNAROAK [12911]).
- **Domínios:** 5 no ar + `wholelifenutri.shop` reserva ([`bridge-pages-deploy.md`](bridge-pages-deploy.md)).
- **Bridges:** 5 no ar, mínimas, copy própria por domínio ([`bridge-pages-arquitetura.md`](bridge-pages-arquitetura.md)).
- **Notificação de venda:** sistema **próprio** BuyGoods → Telegram, sem terceiro ([`notificacao-vendas-telegram.md`](notificacao-vendas-telegram.md)).
- **Automação Comentário → DM:** só DM, sem resposta pública; keywords + congruência da cadeia ([`automacao-comentario-dm.md`](automacao-comentario-dm.md)).
- **Infra:** VPS `159.195.12.135`, Coolify, Traefik+SSL ([`RUNBOOK-deploy-coolify.md`](RUNBOOK-deploy-coolify.md)).
