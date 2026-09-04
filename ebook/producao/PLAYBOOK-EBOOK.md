# PLAYBOOK — MOTOR DE EBOOK (reutilizável, qualquer nicho)

> Fonte da verdade para criar **novos ebooks** (mesmo nicho ou outro).
> O motor é agnóstico de nicho: o que muda é o CONTEÚDO (receitas/itens e copy),
> não a arquitetura. Primeiro ebook feito: "150 Receitas da Boa Forma" (emagrecimento).

---

## 1. ARQUITETURA (dados → motor → PDF)

```
receitas_<categoria>.py   (DADOS: lista de dicts, 1 por item)
        │
        ▼
motor_receitas.py         (TEMPLATE TRAVADO: dict -> HTML de 1 página)
        │
build_<x>.py  ──►  HTML  ──►  http.server local (porta 8132)  ──►  Chrome headless  ──►  PDF
        │                                                                (--print-to-pdf)
        ▼
fotos/NNN.jpg             (1 foto por item, quadrada 1000x1000, nomeada pelo número)
```

- **Dados e apresentação separados.** O `.py` de dados só descreve o item; o motor RENDERIZA.
- **String validada é CONSTANTE, nunca redigitada.** Copy aprovada não se reescreve no caminho.
- **O HTML é intermediário e descartável** — o build o apaga após gerar o PDF
  (o PDF já sai com as imagens embutidas). A pasta guarda só os PDFs.

### Pipeline de geração (o que todo build faz)
1. Monta o HTML (`motor_receitas.montar_html` ou builder próprio).
2. Sobe `python -m http.server 8132` na pasta (thread daemon).
3. Chama o Chrome: `--headless=new --disable-gpu --no-pdf-header-footer
   --virtual-time-budget=20000 --print-to-pdf="<abs>" http://127.0.0.1:8132/<tmp>.html`.
4. Apaga o HTML temporário.
- ⚠️ HTML temporário tem nome **ascii sem espaço** (`_tmp_x.html`); o PDF recebe o
  nome final "bonito" (com espaços/acentos). Isso evita ter que URL-encodar.

### Verificação (SEMPRE)
- `pip install pypdfium2 pillow`; renderiza páginas para PNG e **olha** (Read).
- Não existe poppler/weasyprint/wkhtmltopdf no ambiente — usar pypdfium2.
- ⛔ **Aceite é MEDIÇÃO, não relato.** Renderizar e conferir com o olho.

---

## 2. O TEMPLATE TRAVADO DA RECEITA (`motor_receitas.py`)

Cada item (dict) tem: `nome, hook, tempo, rende, kcal_base, ings[], passos[],
porcoes8[8], dica, prompt`. Campos opcionais: `tag` (rótulo da categoria),
`num_label` (troca "Receita NNN"), `livre:True` (bebida livre → troca a tabela por
uma faixa "à vontade").

Layout de 1 página: tag + número · H1 título · hook · GRID[foto quadrada | stats
(tempo/rende/kcal) + ingredientes] · passo a passo numerado · **TABELA DE AJUSTE
por perfil** · dica ("por que ajuda") · rodapé de valores aproximados.

### Tabela de ajuste por perfil (o mais valioso e reusável)
- 8 perfis FIXOS: Mulheres 55-70/71-85/86-100/100+ · Homens 70-85/86-100/101-120/120+.
- `METAS` (kcal) por tipo de refeição no motor. Base científica: Mifflin-St Jeor +
  atividade leve + déficit ~500 kcal. É GUIA, declarar isso.
- `porcoes8` = 8 strings com a porção CONCRETA (colher/grama/unidade) por perfil.
- Altura foi REMOVIDA (só sexo+peso movem o essencial). 

---

## 3. SISTEMA DE DESIGN (travado)

- Paleta: `--green #196B45` · `--gold #D9A441` · `--green-tint #E8F7EB` ·
  `--gold-tint #FBF3E2` · `--cream #F7F5F0` · `--ink #1A1A1A` · `--soft #54524E`.
- Fonte: **DM Sans** (Google Fonts).
- `@page{size:A4;margin:16mm 15mm}` — margem na @PAGE (senão a página 2 cola no topo).
- **1 receita por página** (`page-break-before`). Opção B: pode usar 2 páginas.
- ⛔⛔ **FONTE GRANDE — público idoso.** Corpo ≥16px em QUALQUER PDF. Nunca espremer.
  Legibilidade > economia de página. (Motor compacto de 2/página já foi REPROVADO.)
- `.adj`, `.tip`, faixa "livre" usam `break-inside:avoid`.

---

## 4. FOTOS (workflow travado)

- **Eu escrevo o PROMPT, o operador GERA, eu distribuo.** Não tenho gerador de foto.
- Prompt de comida: quadrado, ultrarrealista, comida pronta, termina em
  **`no text, no writing, 1:1 square`**.
- O operador joga as imagens numa pasta (nomes descritivos do gerador). Eu **mapeio
  por palavra-chave** do nome → número da receita, e **recorto** com ffmpeg:
  `-vf "scale=1000:1000:force_original_aspect_ratio=increase,crop=1000:1000"`.
- **Conferir SEMPRE** com um mosaico rotulado (montage PIL) quando a POSTURA/prato
  importa (ex.: exercícios) — 2 imagens com nome igual se separam pelo timestamp/olho.
- `render_receita` acha `fotos/NNN.<ext>` sozinho; sem foto, mostra placeholder.

---

## 5. ESTRUTURA DO PRODUTO (entrega)

⛔ **Arquivos SEPARADOS** (não um PDF único), numerados como PASSOS para ficarem em
ordem no download e a frente ser sempre a primeira:

```
Passo 1 - Comece Por Aqui           (frente do livro — build_frente.py)
Passo 2..6 - <categorias no PLURAL>  (build_ebook.py, PDF_NAME)
Passo 7..9 - Bônus N - <Nome>        (build_bonus_*.py)
```
- Pasta de entrega: **`Entregavel em <LANG>`** (ex.: "Entregavel em PT"). Copiar
  (não mover) os `Passo *.pdf` para lá.
- Bônus: capa = selo verde "Bônus N" + H1 grande verde (~56-66px) + régua dourada.
  Card de exercício = foto PRÓPRIA por item; card de hábito = 1 foto por TEMA + lista.

### Frente do livro ("Comece Por Aqui" / `build_frente.py`)
Boas-vindas · Como funciona (lista dos passos) · Avisos honestos (não faz milagre ·
leva meses · exercício importa · sem promessa falsa) · dica do YouTube (nome +
"modo de preparo") · anotar/imprimir · nota de calorias (valores aproximados) ·
**PLANO DE 30 DIAS** (gerado dos módulos de receita: café/almoço/jantar/sobremesa/
suco por dia, sem repetir; sobremesas repetem após esgotar as 20).

---

## 6. REGRAS DE CONTEÚDO (do nicho emagrecimento — adaptar por nicho)

- ⛔ Escrever em **PT primeiro** → validar → **traduzir 1 por 1** (EN/DE/FR),
  perguntando a cada passo. ⛔ **Converter TODAS as unidades** na tradução
  (g→oz/lb, ml→cups, °C→°F em US; DE/FR métrico).
- ⛔ **Vocabulário extremamente simples** — sem jargão de cozinha. Termo técnico vai
  no formato "termo (explicação simples)". Varrer antes de fechar cada categoria.
- ⛔ Ingredientes **comuns e baratos** nos mercados-alvo, **sem citar os países**,
  sem superalimento importado/suplemento/item caro.
- ⛔ **Sem vegetariano nas 150** (é o Bônus 1). Almoço/jantar sempre com proteína animal.
- ⛔ Copy e cena são do OPERADOR — sugerir sim, trocar não. Responder em PT
  (a copy dos vídeos é EN; aqui o produto é PT-base).
- Toda receita traz "por que ajuda a emagrecer" (o mecanismo, honesto).

---

## 7. PARA CRIAR UM EBOOK NOVO (checklist)

1. Definir categorias e quantidades; travar o formato de item (reusar o template).
2. Escrever `receitas_<cat>.py` (dados) — vocabulário simples, medido.
3. `METAS` do tipo no motor (se refeição) ou variante `livre` (se bebida/zero-cal).
4. Gerar prompts de foto → operador gera → mapear+recortar em `fotos/`.
5. `build_<cat>` / builders de bônus / `build_frente` → PDFs "Passo N - Nome".
6. Verificar renderizando (pypdfium2) — layout, fonte, tabela, fotos, posturas.
7. Copiar para `Entregavel em <LANG>`; **compactar** no fim (lembrar o operador).
8. Landing correspondente: ver [PLAYBOOK-LANDING](../../landing-150/PLAYBOOK-LANDING.md).

---

## 8. LIÇÕES PAGAS (não repetir)

- **Legibilidade > densidade.** 2 itens/página espremido foi reprovado.
- **Medir a FUNÇÃO, não só a peça nova.** Gerar a saída e olhar; suíte passando não
  garante que o vídeo/página saiu certo.
- **Sem abreviação que confunde** (ex.: "Sem" de semana virou "Semana"; min→minutos).
  Público idoso não decodifica abreviação.
- **Nome de arquivo claro** (plural, "Passo N -") para o comprador se achar.
- **String validada é constante** — comprimir/reescrever copy na mão introduz erro.
