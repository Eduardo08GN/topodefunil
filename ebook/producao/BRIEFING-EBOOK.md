# BRIEFING DO EBOOK — 150 Fitness Recipes / A Lighter Life

> Arquivo de inteligência da produção do entregável (PDF).
> O Lucas vai enviando as instruções por partes; eu anoto TUDO aqui e só avanço
> quando ele mandar continuar. Este arquivo é a fonte da verdade da montagem.

⭐⭐ **MOTORES REUSÁVEIS (base para futuros ebooks/landings, qualquer nicho):**
[`PLAYBOOK-EBOOK.md`](PLAYBOOK-EBOOK.md) (arquitetura dados→motor→PDF, template
travado, design, fotos, entrega "Passo N", frente do livro, regras) e
[`PLAYBOOK-LANDING.md`](../../landing-150/PLAYBOOK-LANDING.md) (estrutura de seções,
tokens, responsivo mobile-first, copy/conversão). Este BRIEFING é a memória do
PROJETO atual; os PLAYBOOKS são a doutrina REUTILIZÁVEL.

- **Produto:** ebook de 150 receitas/métodos de emagrecimento
- **Entregável:** PDF, entregue após a compra (Hotmart)
- **Idiomas:** EN (base) · DE · FR (o Lucas começa pelo inglês)
- **Landing:** `landing-150/` (EN e PT-de-revisão) — a promessa que o PDF tem de cumprir
- **Capa aprovada:** `ebook/capa-150-EN-hotmart.png` (150 FITNESS RECIPES · A Lighter Life)

---

## STATUS DA COLETA
- [x] Parte 1 recebida (distribuição das 150 + regras de produção).
- [x] Parte 1 COMPLEMENTADA (fotos por prompt, calorias, tabela de ajuste por perfil).
- [x] RESOLVIDO: o Claude escreve as 150 receitas SOZINHO. Arquivos de
      referência do Lucas são OPCIONAIS (só se ele tiver pratos que EXIGE
      incluir). Sem eles, receitas 100% originais.
- [x] Parte 2 recebida (páginas iniciais, estrutura, bônus, regra de ingredientes).
- [x] Parte 3 recebida (índice de ingredientes, notas/impressão, A4, páginas de prévia).
- [ ] LEMBRAR: definir as receitas da seção 'Por Dentro do Livro' (prévia) — quando o ebook estiver pronto.
- [x] Parte 3 era a última instrução. Próximo passo: RECEITA-MODELO (café da manhã).
- [x] Lucas liberou a receita-modelo. Detalhe extra: receitas PEQUENAS/simples
      (ex.: sucos) podem ter MAIS DE UMA por página para economizar páginas,
      quando couber.
- [ ] Depois de tudo: escrever a RECEITA-MODELO (café da manhã) para aprovação.

## PROGRESSO DA ESCRITA (categorias)
- [x] **CAFÉS DA MANHÃ (30)** — `receitas_cafe.py` · `cafe.pdf` (60 pág, 30 fotos). PRONTO.
- [x] **ALMOÇOS (35)** — `receitas_almoco.py` · `almoco.pdf` (70 pág, fotos 031-065
      pendentes). PRONTO, aguardando fotos. Prompts em `PROMPTS-FOTOS-ALMOCO.txt`.
      ⛔ ZERO receitas vegetarianas (regra nova: vegetariano é o Bônus 1). Proteínas:
      13 frango · 9 carne · 6 peixe · 2 camarão · 2 peru · 3 ovo/atum.
- [x] **JANTARES (35)** — `receitas_jantar.py` · `jantar.pdf` (70 pág, fotos 066-100
      pendentes). PRONTO, aguardando fotos. Prompts em `PROMPTS-FOTOS-JANTAR.txt`.
      Mais leve que o almoço (peixe/sopas/assados). Proteínas: 11 frango · 9 peixe ·
      6 carne · 4 peru · 3 camarão · 2 ovo. Zero repetição de prato do almoço.
      ✅ 35 fotos distribuídas (fotos/066-100). PDF final 6,9 MB.
- [x] **SOBREMESAS (20)** — `receitas_sobremesa.py` · `sobremesa.pdf` (40 pág, fotos
      101-120 pendentes). PRONTO, aguardando fotos. Prompts em `PROMPTS-FOTOS-SOBREMESA.txt`.
      Todas FIT e SEM AÇÚCAR (fruta/mel opcional/adoçante culinário). Bolo de chocolate = 101.
      Variedade: bolos, mousses, cremes, gelados (nice cream/picolé/bark), cookies, gelatina,
      trufa, cheesecake sem forno, frutas assadas.
      ✅ 20 fotos distribuídas (fotos/101-120). PDF final 3,7 MB.
- [x] **VITAMINAS, SUCOS E CHÁS DETOX (30)** — `receitas_suco.py` · `suco.pdf`
      (53 pág, **1 por página, template GRANDE das outras categorias**, fotos 121-150 pendentes).
      Prompts em `PROMPTS-FOTOS-SUCOS.txt`. ⛔ O motor compacto de 2 por página foi
      DESCARTADO (`motor_sucos.py` apagado): o Lucas reprovou — "fonte pequena, espremido,
      fotos pequenas". Legibilidade > economia de página. ⭐ Chás/águas (10, ≈0 kcal) usam
      faixa "Bebida livre" no lugar da tabela (flag `livre:True` no `motor_receitas`);
      sucos/vitaminas (20) mantêm a tabela. Rótulo varia por receita (`_tag_suco` no build).
      Sem açúcar. Sem superalimento importado (nada de açaí/matcha/spirulina/chia).

      ✅ 30 fotos distribuídas (fotos/121-150). PDF final 4,2 MB.

⭐⭐ **AS 150 RECEITAS ESTÃO PRONTAS, TODAS COM FOTO** (fotos/001-150).
Faltam: FRENTE DO LIVRO (checklist abaixo), os 3 BÔNUS, montar tudo num PDF único,
compactar, e depois a TRADUÇÃO EN/DE/FR.
- Motor genérico: `build_ebook.py <cat>` gera html+pdf de qualquer categoria.

### ⛔ REGRAS NOVAS (2026-09-01, no meio dos almoços)
- ⛔ **Nada de vegetariano nas 150** — é o Bônus 1. Sempre proteína animal.
- ⛔ **Tradução converte UNIDADES** — peso/volume/distância/temperatura por idioma
      (US = oz/lb/cups/°F; DE e FR seguem métrico). Não é só traduzir a palavra.
- ⭐ **Compactar cada PDF no final** — comprimir p/ ficar leve sem perder qualidade;
      lembrar o Lucas ao fechar cada entrega.

## O QUE JÁ SEI (da landing, a cumprir no PDF)
- 150 receitas: 40 sucos/vitaminas · 30 chás/infusões · 30 sopas/caldos ·
  50 refeições do dia a dia · (+ sobremesas fit dentro do total)
- 3 bônus: Dieta Vegetariana · Pilates Seca Barriga em Casa · 50 Hábitos e Exercícios
  (o "Doces Fitness" foi REMOVIDO como bônus — mas sobremesas seguem nas 150)
- Composição pedida antes: 100 de comida/suco/dieta + 50 de exercício/sono/rotina/água

---

## INSTRUÇÕES RECEBIDAS (log — vou preenchendo)

### Parte 1 — DISTRIBUIÇÃO E REGRAS (recebida)

**As 150, distribuídas (fechado, soma 150):**
| Categoria | Qtd |
|---|---|
| Cafés da manhã fit | 30 |
| Almoços fit | 35 |
| Jantares fit | 35 |
| Sobremesas fit | 20 |
| Vitaminas e sucos detox | 30 |
| **TOTAL** | **150** |

**Regras invioláveis da produção:**
1. ⛔ **Pesquisa aprofundada obrigatória** — além dos arquivos de referência
   que o Lucas deixou. Receitas REAIS, que qualquer pessoa consiga preparar e
   que FUNCIONEM de verdade (emagrecimento).
2. ⛔ **1 receita = 1 página**, e TODA receita tem uma FOTO.
3. ⛔ **Foto:** eu tento gerar por IA; se não conseguir, entrego o PROMPT
   (formato QUADRADO) para o Lucas gerar, ele anexa e eu ajusto uma por uma.
4. ⛔ **Modo de preparo extremamente detalhado** — passo a passo à prova de
   erro, qualquer pessoa consegue seguir.
5. ⛔ **Ingredientes fáceis e baratos** de achar nos EUA, Alemanha E França.
6. ⛔ **Escrever primeiro em PORTUGUÊS.** A tradução (EN/DE/FR) só quando o
   Lucas aprovar o conteúdo.
7. Formato final: **PDF** (usar a skill `pdf`).

⚠️ **PENDÊNCIA A — arquivos de referência:** o Lucas disse "arquivos em anexo
que estou deixando", mas não sei ONDE estão (pasta/caminho). Preciso do local
antes da pesquisa, para não ignorar a referência dele.

⚠️ **PENDÊNCIA B — geração de foto:** neste ambiente eu NÃO tenho ferramenta de
gerar foto realista (só HTML/SVG). Então o caminho real é: eu entrego o PROMPT
quadrado de cada receita, o Lucas gera e anexa. Confirmar com ele.

⚠️ **DECISÃO C — campos de cada receita:** propor template e travar ANTES de
escrever as 150 (senão retrabalho em massa). Sugestão de campos:
nome · foto · tempo de preparo · porções · [calorias/macros?] · ingredientes
(com substituição por mercado quando divergir) · modo de preparo passo a passo
· dica fit (por que ajuda a emagrecer).

---

### Parte 1 — COMPLEMENTOS (respostas do Lucas às minhas dúvidas)

**1. Arquivos de referência:** virão DEPOIS de todas as partes. ⚠️ TENHO QUE
LEMBRAR ele.

**2. Fotos — fechado o método:**
- Eu entrego PROMPT DETALHADO por receita, da REFEIÇÃO PRONTA, foto realista,
  formato QUADRADO. **1 foto por página.**
- ⛔ Em cada página deixo o ESPAÇO da imagem já reservado (quadrado).
- ⛔ Cada prompt vem com o NÚMERO correspondente da imagem/página. O Lucas gera,
  nomeia a imagem com o número, joga tudo numa pasta, e eu distribuo.
- ⭐ ID estável = número da receita (001-150). Imagem `001` → receita 001, etc.
  (número da receita alinhado à página; front-matter à parte). Confirmar no modelo.

**3. Receita-modelo:** SIM, faço a primeira para o Lucas analisar antes de escalar.

**4. Calorias:** SIM, cada receita traz as calorias.

**5. Ordem:** começar pelos CAFÉS DA MANHÃ.

**6. ⭐⭐ OBRIGATÓRIO — TABELA DE AJUSTE POR PERFIL (o mais complexo):**
Dentro de CADA receita, uma tabela que diz, por SEXO + PESO + ALTURA, para
quantas calorias a pessoa deve ajustar aquela refeição e QUANTO de cada
ingrediente isso significa (porções concretas).
Exemplo do Lucas: *"Mulheres de 1,50-1,60 pesando 83kg → ajustar para X kcal =
3 colheres de sopa de arroz, 2 de feijão, 150g de carne vermelha, vegetais à
vontade."* Repetir para outros pesos/alturas, e o mesmo para HOMENS.
⛔ Tem que ser um PADRÃO ÚNICO que serve para as 150 receitas — os perfis e as
metas de caloria são FIXOS; só as porções mudam por receita.

**MINHA ABORDAGEM PROPOSTA (validar no modelo):**
- Perfis fixos, iguais em todas as receitas. Mulheres e Homens separados.
- Faixas por PESO (o que mais move a caloria) com ALTURA anotada na faixa.
  Rascunho de faixas (a confirmar):
    Mulheres: 55-70kg · 71-85kg · 86-100kg · 100kg+   (× altura baixa/média/alta)
    Homens:   70-85kg · 86-100kg · 101-120kg · 120kg+
- Base científica p/ credibilidade: BMR Mifflin-St Jeor + fator de atividade
  leve, déficit de ~500 kcal/dia para emagrecer. (Sem idade/atividade exatas,
  é GUIA — declarar isso.)
- A caloria por refeição = fração da meta diária conforme o TIPO:
  café ~25% · almoço ~30% · jantar ~30% · sobremesa ~10% · suco/vitamina ~5-10%.
- Cada receita nasce numa PORÇÃO-BASE; a tabela escala para cada perfil com
  porções concretas (colheres, gramas, unidades), não só um multiplicador.
⚠️ Desafio de layout: isso + foto + ingredientes + passo a passo + calorias
numa PÁGINA SÓ. A tabela precisa ser COMPACTA. Resolver no modelo.

---

### Parte 2 — PÁGINAS INICIAIS, ESTRUTURA E REGRA DE INGREDIENTES (recebida)

**Layout — flexibilizado:** se uma receita não couber em 1 página, pode usar
2. ⭐ Prioridade é ENTREGAR VALOR e QUALIDADE MÁXIMA, não caber em 1 página.

**PÁGINAS INICIAIS (antes das 150 receitas) — avisos honestos:**
1. ⛔ A dieta NÃO faz milagre. Seguir a dieta e no fim de semana comer doces/
   guloseimas diferentes = SEM resultado. Consistência é tudo.
2. ⛔ Resultado NÃO é do dia para a noite. Precisa manter o plano por ALGUNS
   MESES.
3. ⭐ Importância de atividade física e exercícios — deixar claro. Os exercícios
   vêm LOGO APÓS as 150 receitas (nos bônus).
4. ⛔ SEM promessas falsas. Entregamos um PROTOCOLO COMPLETO que PODE trazer
   resultados sólidos (linguagem honesta, condicional).

**ESTRUTURA GERAL DO EBOOK (ordem):**
1. Capa
2. Páginas iniciais: instruções + avisos honestos (os 4 acima)
3. As 150 receitas (30 café · 35 almoço · 35 jantar · 20 sobremesa · 30 suco/vitamina)
4. SESSÕES DOS 3 BÔNUS, cada uma sua seção:
   - Bônus 1: Dieta Vegetariana [x] FEITO — `receitas_bonus_veg.py` +
     `build_bonus_veg.py` → `bonus_vegetariano.pdf` (19 pág). 20 opções, 4/categoria:
     café/sobremesa/sucos = referência às receitas já existentes (lista na abertura);
     almoço/jantar = 8 receitas NOVAS (fotos 151-158 pendentes, prompts em
     `PROMPTS-FOTOS-BONUS-VEGETARIANO.txt`). Ovo-lacto; proteína de leguminosas/tofu/
     ovos/queijos. ⭐ motor ganhou `num_label` (rótulo "Bônus · Vegetariano").
     ✅ 8 fotos distribuídas (151-158). Título da abertura em DESTAQUE (selo verde
     "BÔNUS 1" + h1 66px verde + régua dourada). PDF 2,1 MB.
   - Bônus 2: Pilates Seca Barriga em Casa [x] FEITO — `exercicios_pilates.py` +
     `build_bonus_pilates.py` → `Bônus 2 - Pilates Seca Barriga em Casa.pdf` (20 pág).
     12 exercícios de core, feitos em casa sem aparelho, com variação fácil. Fotos
     159-170 pendentes (prompts em `Prompts Fotos - Bônus 2 - Pilates.txt`). Card
     próprio (nível/séries/tempo/foco/como fazer/respiração/dica). Abertura com aviso
     honesto (não se queima gordura só na barriga) + plano da semana + índice dos 12.
   - Bônus 3: [x] REESCRITO (2026-09-02) — `exercicios_habitos.py` + `build_bonus3.py`
     → `Bônus 3 - Exercícios e Hábitos para Emagrecer.pdf` (10 pág). ⛔ A 1ª versão
     (`habitos_50.py`, 50 hábitos em texto) foi REPROVADA e APAGADA: o Lucas achou
     "muitos hábitos e poucos exercícios, muito texto, hábitos óbvios e inúteis
     (tenha paciência, comemore vitórias)". Nova versão = EXERCÍCIOS REAIS com
     PROGRESSÃO (caminhada 2→5 km, corrida, bike, natação, HIIT, máquinas, musculação,
     força em casa) — onde fazer, gasto ~kcal/30min, plano semana a semana, dica —
     + só hábitos úteis (alimentação, água/sono) no fim. ⭐ "Tópico" = TEMA (categoria):
     9 temas, 1 IMAGEM POR TEMA (fotos 171-179, prompts em
     `Prompts Fotos - Bônus 3 - Exercicios.txt`). 21 exercícios + 10 hábitos.
     ⭐ CORRIGIDO 2026-09-02: nome VOLTOU para "50 Hábitos e Exercícios" (o produto tem
     que ter 50 itens). Total = 50: **30 exercícios + 20 hábitos**, numerados 1-50.
     ⛔ CADA EXERCÍCIO tem a SUA foto (card individual, fotos 171-200); os 20 hábitos vêm
     em 3 seções com 1 foto de tema cada (201-203). 33 fotos no total, prompts em
     `Prompts Fotos - Bônus 3.txt`. Card espaçoso e legível (3 exercícios por página).
     Arquivo: `Bônus 3 - 50 Hábitos e Exercícios.pdf` (16 pág).
     ✅ 33 fotos distribuídas (171-203), posturas conferidas OK. PDF 5,0 MB.

⛔⛔ NOMES DOS PDFs (2026-09-02, Hotmart em ARQUIVOS SEPARADOS): prefixo **"Passo N -"**
para ordenar alfabeticamente na ordem de leitura (a frente sempre em 1º). Ordem:
`Passo 1 - Comece Por Aqui` · `Passo 2 - Cafés da Manhã` · `Passo 3 - Almoços` ·
`Passo 4 - Jantares` · `Passo 5 - Sobremesas` · `Passo 6 - Vitaminas, Sucos e Chás Detox` ·
`Passo 7 - Bônus 1 - Dieta Vegetariana` · `Passo 8 - Bônus 2 - Pilates Seca Barriga em Casa` ·
`Passo 9 - Bônus 3 - 50 Hábitos e Exercícios`. Builds já geram com esses nomes.
(Só 9 arquivos → dígito único ordena certo, sem precisar de "Passo 01".)

⭐ FRENTE DO LIVRO [x] FEITA — `build_frente.py` → `Passo 1 - Comece Por Aqui.pdf`
(6 pág): boas-vindas · como o material funciona (os 9 passos) · 4 avisos honestos ·
dicas (YouTube, anotar/imprimir, calorias/porções) · PLANO ALIMENTAR DE 30 DIAS
(tabela dia a dia: café+almoço+jantar+sobremesa+suco por número de receita; sobremesa
reinicia no dia 21 porque só há 20). ⏳ FALTAM (opcionais, decidir com o Lucas):
índice de ingredientes e índice visual — com arquivos separados o conceito de "página"
mudou; talvez não sejam mais necessários.
   ⭐ Destacar a importância de SEGUIR o Pilates e os Hábitos para ACELERAR os
   resultados.

**O QUE PROMETEMOS NA PÁGINA E TEM DE ESTAR NAS RECEITAS:**
⛔ No meio das 150 têm de existir: sucos, chás, sopas e BOLO DE CHOCOLATE —
todos fit e SEM AÇÚCAR. (O bolo de chocolate sai como uma das 20 sobremesas.)

**REGRA DE INGREDIENTES (dura):**
⛔ SEM superalimento importado. SEM suplementos. SEM alimento caríssimo
(caviar e afins). Eu defino o que entra com base no PREÇO real dos alimentos
nos 3 países (EUA, Alemanha, França) — comum de supermercado, barato nos três.

---

### Parte 3 — ÍNDICE, NOTAS, A4 E PÁGINAS DE PRÉVIA (recebida)

**PÁGINAS INICIAIS — acrescentar:**
1. ⭐ **ÍNDICE DE INGREDIENTES / receitas:** uma lista onde a pessoa lê o NOME
   da receita + os INGREDIENTES e sabe QUAL PÁGINA olhar. (índice navegável)
2. ⭐ Destacar a importância de **fazer ANOTAÇÕES** para lembrar o que fazer e
   comer — OU, se preferir, **IMPRIMIR** as páginas de comidas/hábitos/
   exercícios de interesse.

**INGREDIENTES — reforço:** todas as receitas bem aceitas e COMUNS nos 3 países
(EUA, Alemanha, França). ⛔ Mas NUNCA mencionar os países no texto.

**FORMATO:** ⛔ criar o conteúdo para poder IMPRIMIR em **A4** (as páginas
precisam funcionar em A4 — margem, proporção, legibilidade impressa).

**PÁGINAS DE PRÉVIA (a seção 'Por Dentro do Livro' / 'Real pages from the book'
da LANDING):** o Lucas quer capricho máximo nessas páginas-amostra. Ideias
iniciais dele: **1 sobremesa · 1 suco detox · 1 sopa**. ⭐ Eu ajudo a definir o
RESTO das amostras QUANDO O EBOOK ESTIVER PRONTO. ⚠️ LEMBRAR ELE.
(Essas páginas viram as imagens dos slots 'Recipe page' da landing.)

---

### Parte 4 — PLANO DE ALIMENTAÇÃO (nas páginas iniciais) (recebida)

⭐ Nas primeiras páginas, além do índice e avisos, criar um **PLANO DE
ALIMENTAÇÃO de 1 mês**: quais receitas intercalar por 30 dias SEM repetir.
- Cada dia inclui: **1 sobremesa + 1 suco + 1 prato diferente**.
- ⛔ Só pode REPETIR uma opção depois de ESGOTAR as anteriores (30 dias sem
  repetir prato/suco/sobremesa).
- ⛔ Montar o plano **DEPOIS de todas as 150 receitas prontas** (preciso das
  receitas existirem para referenciar). ⚠️ LEMBRAR.

### FOTOS — regra reforçada (Parte 4):
⛔ NENHUMA imagem com escrita/texto. Só a FOTO ultrarealista, QUADRADA, da
comida pronta. Prompt sempre termina com "no text, no writing, 1:1 square".

### MOTOR DE PRODUÇÃO:
As receitas saem de um motor (`montar_cafe.py` etc.): dados estruturados +
template travado (receita-modelo) -> HTML -> PDF via Chrome headless. Metas de
café da manhã (fixas): Mulheres 300/370/420/470 · Homens 450/510/560/620 kcal.

---

### Parte 5 — YOUTUBE, VOCABULÁRIO SIMPLES, MENOS REPETIÇÃO (recebida)

**PÁGINAS INICIAIS — acrescentar:**
⭐ Aviso: se a pessoa tiver dificuldade em alguma receita, é só pesquisar o
NOME da receita + "modo de preparo" no YOUTUBE que encontra um vídeo ensinando.

**⛔⛔ VOCABULÁRIO EXTREMAMENTE SIMPLES (regra dura de escrita):**
Escrever para quem NÃO é cozinheiro e NÃO tem prática — qualquer pessoa, de
qualquer país/língua, tem de entender. Nada de termo técnico de cozinha.
Exemplo que pegou o Lucas: "unte" (ele não sabia o que era). Trocas já feitas
nos cafés: unte→"passe um pouco de óleo"; antiaderente→"que não gruda";
refogue→"frite em um pouco de óleo, mexendo"; homogêneo→"bem misturado";
escumadeira→"colher com furos"; potência alta→"velocidade máxima";
murchar→"folhas ficarem moles"; caramelizar→"ficar dourado".
⛔ Toda categoria nova passa por essa varredura ANTES de fechar.

**MENOS REPETIÇÃO:** evitar repetir demais receitas e ingredientes quando
possível. (Café da manhã tem repertório universal limitado — ovos/aveia/
iogurte; nos ALMOÇOS e JANTARES dá para variar muito mais. Diversificar lá.)

**FOTOS:** o Lucas vai GERAR as imagens agora e mandar; eu ajusto o arquivo
distribuindo cada foto na página certa (001-030).

---

### Parte 6 — ÍNDICE VISUAL DE FOTOS (páginas iniciais) (recebida)

⭐ Nas páginas iniciais, um ÍNDICE VISUAL: as FOTOS dos pratos (miniaturas
pequenas) com o NOME e o NÚMERO DA PÁGINA onde a pessoa encontra cada um.
- ⛔ Fotos PEQUENAS (grade/mosaico), para não ocupar muitas páginas.
- ⭐ Ótimo para o público idoso, que navega por imagem melhor que por texto.
- Organizar por categoria (café · almoço · jantar · sobremesa · suco).
- Estimativa: grade de ~4 col × 6 linhas = 24 por página -> ~6-7 páginas p/ 150.
- ⛔ Montar no FIM (precisa de todas as fotos + números de página finais).
- Complementa o índice de INGREDIENTES em texto (Parte 3): um por imagem,
  outro por nome+ingrediente. Os dois convivem.

### FRENTE DO LIVRO (páginas iniciais) — checklist consolidado p/ montar no fim:
1. Boas-vindas + como usar
2. Avisos honestos (não faz milagre · leva meses · exercício importa · sem promessa falsa)
3. Aviso do YouTube (nome da receita + "modo de preparo")
4. Anotar / imprimir as páginas de interesse
5. Nota de valores aproximados (calorias = guia)
6. ÍNDICE DE INGREDIENTES (texto: nome + ingredientes -> página)
7. ÍNDICE VISUAL (fotos pequenas + nome + página)
8. PLANO DE 1 MÊS (sobremesa + suco + prato/dia, sem repetir 30 dias)

---

### Parte 7 — REGRA DE TRADUÇÃO (recebida)

⛔⛔ Estamos escrevendo em PORTUGUÊS só para o Lucas entender e validar agora.
DEPOIS de o livro PT estar 100% pronto, TRADUZIR TUDO para **EN, DE e FR**.
- ⛔ Tradução com CALMA, **1 por 1** (receita a receita / seção a seção), e EU
  vou PERGUNTANDO ao Lucas a cada passo — não traduzir em massa sem validar.
- ⛔ LINGUAGEM SIMPLES em TODAS as línguas — a mesma régua da varredura de
  vocabulário do PT (sem jargão de cozinheiro), adaptada a cada idioma.
- São 4 versões finais do PDF: PT (base de trabalho), EN, DE, FR.
⚠️ LEMBRAR o Lucas disso quando o PT terminar.

---

## DECISÕES DE MONTAGEM (a definir com o Lucas)
- Estrutura: capa → avisos honestos → 150 receitas (5 categorias) → 3 seções de bônus. 1-2 páginas por receita.
- Tipografia e identidade visual (paleta da landing? creme/verde/DM Sans):
- Formato de cada receita: APROVADO (receita-modelo 001). Campos: tag categoria,
  nº receita, título, gancho, foto quadrada (por prompt), stats (tempo/porção/
  kcal), ingredientes base, passo a passo numerado, TABELA DE AJUSTE por perfil
  (4 mulheres + 4 homens por faixa de peso, com porções concretas), dica fit,
  rodapé de valores aproximados.
- ⛔ FONTE LEGÍVEL, NÃO PEQUENA — público tem muitos IDOSOS. Nada apertado.
- ⛔ Opção B: deixar respirar em 2 páginas QUANDO necessário. Receitas simples
  (sucos) cabem em 1 ou várias por página.
- Índice de ingredientes/receitas navegável (Parte 3). Formato A4 imprimível.
- Ferramenta de geração do PDF: skill `pdf` (reportlab/latex).

## NOTA SOBRE AS CALORIAS (declarar no ebook)
As calorias que eu calculo são ESTIMATIVAS com base em tabelas nutricionais
padrão (não são medidas de laboratório). O ebook deve dizer "valores
aproximados" — é honesto e é o padrão de qualquer livro de receitas.
As metas por perfil (Mifflin-St Jeor + déficit) também são GUIA, não
prescrição médica. Declarar isso nas páginas iniciais.

## PENDÊNCIAS / DÚVIDAS
-
