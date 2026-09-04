# PLAYBOOK — MOTOR DE LANDING (reutilizável, qualquer nicho)

> Fonte da verdade para criar **novas landing pages** de venda de infoproduto
> (mesmo nicho ou outro). A ESTRUTURA e o SISTEMA DE DESIGN são reusáveis; muda a
> copy e as imagens. Primeira landing: `landing-150/` (ebook de emagrecimento).

---

## 1. ARQUIVOS E BILINGUISMO

- Uma landing = **1 HTML por idioma**, autossuficiente (CSS e SVGs inline, sem build):
  `index.html` (EN) · `index-pt.html` (PT). Futuro: `index-de.html`, `index-fr.html`.
- ⛔⛔ **Toda alteração é varredura das DUAS (ou N) versões** — nunca só uma.
  Ao editar, checar o mesmo trecho em cada idioma (contadores, valores, copy, CSS).
- Imagens com texto queimado (ex.: nome da receita na foto) são **por idioma**:
  `receitas/pt/…`, `receitas/en/…`. Foto sem texto pode ser compartilhada.

---

## 2. ORDEM DAS SEÇÕES (estrutura que converte)

1. **Topbar** (logo + selo "150" + botão).
2. **Hero** — eyebrow ("150 Receitas · N Bônus Grátis · Acesso Imediato") · headline ·
   badges de categoria · preço · arte do livro. Mobile centralizado, desktop 2 colunas.
3. **Problema** (`.problem`, fundo escuro `--ink`) — a dor, com o "punch" em dourado.
4. **Features** — 3 `.card` (ícone-em-cima + título + texto). Por que funciona.
5. **Por Dentro do Livro** — `.rail` (carrossel horizontal) de `.rcard`: FOTO 3:4 +
   nome + descrição curta. Subtítulo diz **"N exemplos das 150"** (não parecer o todo).
6. **Conteúdo / o que vem** (`.contentcard` — ícone AO LADO do título, lista `.ticks`).
7. **Bônus** — `.grid.grid-4` de `.card.bonus` (fundo `--gold-tint`, borda dourada,
   selo "Bônus N" no canto, ícone, título, descrição, preço riscado). Valem $X somados.
8. **Como funciona** — 3 `.step` (numerados, já centrados).
9. **Oferta** (`#offer`, `.sec-green`) — caixa com a lista de tudo que chega + preço.
10. **Garantia** · **Depoimentos** (`.rail` de vídeos) · **FAQ** (`<details>`) · **CTA final**.

---

## 3. SISTEMA DE DESIGN (tokens)

- `--green #196B45` (marca) · `--gold` (destaque) · `--green-tint`/`--gold-tint`
  (fundos suaves) · `--cream` (fundo) · `--ink`/`--ink-soft` (texto) · `--line`
  (bordas) · `--surface` (cards) · `--r-lg` (raio) · `--shadow`. Fonte **DM Sans**.
- Ícones: `<svg><use href="#ic-…"/>` (defs inline). Existem: leaf, pulse, bolt,
  calendar, book, utensils, basket, gift, glass, cake, bowl, star, shield, lock,
  mail, card, play, swipe, arrow, return.

## 4. RESPONSIVO (mobile-first)

- **Base = mobile.** `@media(min-width:700px)` = tablet (grids ligam). 
  `@media(min-width:1000px)` = desktop (hero 2 col, grid-4 vira 4 col, body 18px).
- Grids: `.grid-2`/`.grid-3`/`.grid-4` (colunas só no ≥700; grid-4 = 2 col no tablet,
  4 col no desktop). Rail: `grid-auto-flow:column` + `scroll-snap` (carrossel).
- ⭐ **Centralizar no MOBILE** o que é bloco curto de ícone: 
  `@media(max-width:699px){ .card{text-align:center} .card .ico{margin:auto}
   .bonus-tag{left:50%;transform:translateX(-50%)} }`.
  ⛔ NÃO centralizar texto longo (FAQ, listas) — piora a leitura. Hero e garantia já
  centram no mobile e alinham à esquerda no desktop (padrão do arquivo).
- **Dica de swipe** (`.rail-hint`) = selo verde chamativo (fundo `--green-tint`, texto
  `--green` bold ~15px) com a setinha ANIMADA (translateX). Guardar a animação sob
  `@media(prefers-reduced-motion:reduce){ *{animation:none!important} }`.

---

## 5. COPY / CONVERSÃO (princípios)

- **Honesto, sem promessa falsa** (ex.: "não prometemos X kg em 1 semana"). É o que
  sustenta a página aos olhos do comprador e das plataformas.
- Contadores coerentes em TODA a página (N bônus, valor somado dos bônus, delivery).
- Entrega: a copy tem de bater com o formato real. Hoje: **arquivos separados passo a
  passo** por e-mail (não "um único PDF"). Se o formato mudar, varrer as menções.
- Preço-âncora: bônus com valor riscado somando um "valem $X"; oferta como custo único.
- "N exemplos das 150" para mostrar escala sem dar a impressão de que é tudo.

---

## 6. PARA CRIAR UMA LANDING NOVA (checklist)

1. Copiar `index.html`/`index-pt.html` como base (estrutura + CSS + SVGs prontos).
2. Trocar COPY por idioma (hero, problema, features, bônus, oferta, FAQ) — varrer as N.
3. Trocar imagens: arte do produto + as `.rcard` (fotos 3:4 de exemplos; nome no
   Canva ou queimado por idioma via PIL — ver §1). Ajustar contadores/valores.
4. Conferir no navegador em **mobile e desktop** (centralização, grids, swipe hint).
5. Deploy: ver `funil-organico/RUNBOOK-deploy-coolify.md` (não reinventar).

---

## 7. LIÇÕES PAGAS (não repetir)

- **Fonte pequena/apagada afasta** — hints e descrições precisam de tamanho e cor
  fortes (público idoso). "Swipe" cinza 13px foi reprovado → selo verde 15px animado.
- **Centralizar no mobile só o que é bloco curto** (ícone-cards, selo de bônus).
- **Selo de bônus:** centrado no mobile, no canto no desktop (decisão do operador).
- **Toda mudança nas duas línguas**, sempre. Screenshot pode vir de cache — recarregar.
- Ligado ao ebook: [PLAYBOOK-EBOOK](../ebook/producao/PLAYBOOK-EBOOK.md).
