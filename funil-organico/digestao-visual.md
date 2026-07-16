# Digestão Visual — pipeline de mineração de criativos concorrentes

- **Status:** consolidado (metodologia) — a execução roda por leva de criativos coletados, alimentando a matriz-mestre continuamente
- **Serve para:** converter um vídeo-criativo de concorrente (Nitric Health, Tanisha Rivers, Kofi&Simba, Alexis Burgundy...) num **brief estruturado e comparável**, achar o padrão visual que se repete entre páginas que performam, e alimentar prompts Veo 3 próprios — **sem nunca copiar claim, testemunho ou credencial**.
- **Ferramentas:** ffmpeg, yt-dlp, Python, visão do Claude, browser — tudo já disponível no ambiente, nada a instalar.

> **Onde isso se encaixa:** este doc é o motor operacional por trás da [gramática visual comum](gramatica-visual.md) — é o processo que **produziu** aquele padrão (a partir das [páginas de referência mineradas](paginas-referencia.md)) e que se repete a cada nova leva de concorrentes. Sem digestão sistemática, a gramática visual vira opinião; com ela, vira **evidência agregada**.

## A) Schema de Signature Visual (as 10 dimensões do brief)

Preencher estas 10 colunas para **cada criativo** minerado. É a unidade atômica da matriz-mestre (passo 4 do pipeline).

| # | Dimensão | Perguntas-guia (o que capturar) | Exemplo já observado (páginas mineradas) |
|---|----------|----------------------------------|-------------------------------------------|
| 1 | **Persona/avatar** | Qual arquétipo (autoridade médica, curandeiro tribal, wellness/lifestyle, marca institucional)? Demografia (gênero/raça/idade)? Figurino? Sinal de autoridade (jaleco, óculos, diploma, cartaz anatômico)? Apelo (sexual, relatável, exótico)? | Nitric Health: mulher branca atraente, jaleco/óculos, decote acentuado (apelo sexual). Kofi&Simba: homem negro idoso musculoso, colar de contas, roupa étnica africana (mecanismo único exótico). |
| 2 | **Cenário** | Local? Sinais de tribo (bandeira dos EUA, cidade citada na bio)? Luz/paleta? | Consultório/cozinha/varanda; **bandeira dos EUA** presente na maioria. Kofi&Simba soma leão nas fotos e cenário "apothecary" (Houston, TX). |
| 3 | **Prop-metáfora** | Objeto usado + qual função ele cumpre (inuendo fálico / demonstração de mecanismo / experimento caseiro)? | Banana com fita métrica, suco de beterraba ("nature's viagra"), vulcão de bicarbonato, liquidificador com 4 ingredientes, "horse gelatin" + pasta de dente. |
| 4 | **Hook visual** | O que aparece nos primeiros 1-2s? Que interrupção de padrão o frame de abertura cria? | "YOUR NATURE'S VIAGRA", "WATCH WHAT HAPPENS", "SUPPRESSES TESTOSTERONE", "THIS IS LOW TESTOSTERONE". |
| 5 | **Texto na tela** | Estilo da legenda (cor, caixa)? Ritmo karaokê palavra-a-palavra? Copy do gancho? | Amarelo destacado (Tanisha Rivers) ou branco/azul em caixa; keyword em destaque dentro da frase. |
| 6 | **Edição/tempo** | Duração total? Nº de cortes? Demonstração ao vivo vs. talking-head? Cenas dramatizadas? | Demonstração ao vivo (vulcão de bicarbonato, smoothie no liquidificador); dramatização (casal, fisioterapia, homens de toalha). |
| 7 | **Áudio** | Voz/sotaque? Música? Som ambiente? | **Ainda não coletado nas páginas mineradas** — essa linha só se preenche com o vídeo bruto (ver seção D); screenshot não carrega áudio. |
| 8 | **CTA/mecânica** | Palavra-gatilho? Pede follow? Onde está o link (bio/comentários/DM)? Copy do post? | Tanisha Rivers: "Comment Book for the link to my complete male health protocol". Kofi&Simba: "Comment YES/Gelatin". Alexis Burgundy: comenta + recebe "sent you the full remedy... go rock your partner's world!". |
| 9 | **Sinal de performance** | Seguidores da página? Comentários (proxy de conversão)? Likes/shares (proxy de alcance)? | Nitric Health ~95K seguidores; Kofi&Simba ~19K seguidores — os únicos números confirmados até aqui. Comentários por post = quantos pediram o link (métrica a acompanhar por criativo, ver [arquitetura do funil](arquitetura-do-funil.md)). |
| 10 | **Flag de compliance** | Tem claim de cura? Testemunho/credencial fabricada apresentada como real? Innuendo sexual no limite da política da plataforma? | Todas as páginas com criativo minerado usam **persona de IA apresentada como especialista real** — flag alta por padrão de arquétipo, não exceção. Ver seção de compliance abaixo. |

## B) Pipeline de 5 passos

### 1. Coletar o criativo
- Priorize o **arquivo de vídeo bruto** ou a **URL direta** do post — não o screenshot. Screenshot é fallback (ver seção D).
- `yt-dlp` baixa de URLs públicas de FB/IG/YouTube/TikTok; para vídeo protegido ou embutido, aplicar a técnica geral de captura descrita em [Baixar qualquer VSL](../recursos/baixar-qualquer-vsl.md).
- Organize por página-fonte (ex.: pasta por página + data do post) para rastrear a origem de cada linha na matriz-mestre.

### 2. Extrair keyframes com ffmpeg
- Regra: **1 frame a cada 1-2s** (cobre o ritmo de corte do vídeo inteiro) **+ isolar o 1º frame à parte** — é o frame do HOOK, o que decide o scroll-stop.
- Comandos-base:
  - Grade de frames: `ffmpeg -i video.mp4 -vf fps=1/1.5 frame_%03d.png`
  - Hook isolado (1º frame): `ffmpeg -i video.mp4 -vf "select=eq(n\,0)" -vframes 1 hook_frame.png`
- Monte uma **grade de stills** (contact sheet) com os frames extraídos — Python (PIL) ou `montage` (ImageMagick) — para visualizar a sequência inteira de uma vez, sem precisar reassistir o vídeo repetidamente.

### 3. Ler os frames (visão do Claude)
- Passe a grade de stills (ou os frames em sequência) para leitura visual e preencha as 10 linhas do schema por criativo.
- **Edição/tempo** se lê contando planos distintos e a duração aproximada de cada um na sequência de frames — isso substitui "assistir o vídeo" para fins de mapeamento estrutural.
- **Persona/cenário/prop/hook/texto** saem direto da imagem. **Áudio** e **CTA/mecânica** completos (copy do post, palavra-gatilho) exigem o vídeo + a legenda do post, não só os frames.

### 4. Agregar em matriz-mestre
- Uma **linha por criativo**; colunas = as 10 dimensões do schema + página-fonte + arquétipo (ver [Avatares/Experts](avatares-experts.md)) + data de coleta.
- Formato duplo: **CSV** (filtrar/pivotar por arquétipo, prop, hook) espelhado em **MD** (ler direto na base).
- Cruze por **arquétipo**: comparar hooks, props e CTAs de páginas diferentes dentro do mesmo arquétipo. O que se repete **entre páginas que não se copiam** é o candidato mais forte a padrão que realmente performa — não coincidência.

### 5. Destilar em template modelável
- **Brief de criativo:** preencha as 10 dimensões do schema como especificação de um vídeo **novo** — trocando prop/hook/cenário por variação própria, mas mantendo a estrutura recorrente do arquétipo escolhido.
- **Prompt-base Veo 3 por arquétipo:** monte usando a anatomia de prompt de [Veo 3 — produzir os criativos](../recursos/veo3-criativos.md) (cena, sujeito, fundo, ação, estilo, câmera, composição, iluminação, áudio, paleta, instruções negativas), preenchida com o que a matriz revelou daquele arquétipo — **nunca com o claim específico do concorrente**.

## C) Ferramentas (já disponíveis, nada a instalar)

| Ferramenta | Papel no pipeline |
|---|---|
| **yt-dlp** | Passo 1 — baixar o vídeo bruto a partir da URL do post |
| **ffmpeg** | Passo 2 — extrair keyframes (grade + hook isolado) |
| **Python** | Passos 2 e 4 — montar a grade de stills; consolidar a matriz-mestre em CSV |
| **Visão do Claude** (ler imagem) | Passo 3 — preencher o schema a partir dos frames |
| **Browser** | Passo 1 e apoio — localizar/abrir o post original, ler bio/copy da página |

## D) O que é preciso para rodar (vídeo vs. screenshot)

- **Cobertura completa do schema exige o vídeo** (arquivo ou URL baixável). É o único jeito de preencher **edição/tempo** (cortes, ritmo, demonstração ao vivo) e **áudio** (voz, música, som ambiente).
- **Screenshot é fallback PARCIAL:** captura só **persona, prop e texto na tela** de um único frame — as linhas de edição/tempo e áudio da matriz ficam em branco ou inferidas, e o registro deve ser marcado como parcial na matriz-mestre para não distorcer o cruzamento por arquétipo.
- Ordem de prioridade na coleta: **vídeo completo > vídeo parcial (alguns clipes do post) > screenshot** (usar só quando o vídeo foi removido ou o post está inacessível).

## E) Output do sistema

1. **Matriz-mestre** (CSV + espelho em MD) — uma linha por criativo com as 10 dimensões do schema, arquétipo, página-fonte e sinal de performance.
2. **Cruzamento por arquétipo** — o que se repete entre páginas diferentes do mesmo arquétipo = padrão validado a modelar (não a copiar).
3. **Template de brief de criativo** — as 10 dimensões preenchidas como especificação de produção própria.
4. **Prompt-base Veo 3 por arquétipo** — usando a anatomia de prompt de [Veo 3 — produzir os criativos](../recursos/veo3-criativos.md). Esqueletos estruturais (sem claim, sem produto nomeado):
   - **Autoridade médica/científica:** cena em consultório doméstico com cartaz anatômico e bandeira dos EUA ao fundo; sujeito de jaleco, tom confiante-professoral; ação = demonstra o prop-metáfora sem enunciar claim médico; estilo documentário-consultório, luz clean; câmera em plano médio fixo com zoom lento no prop; legenda karaokê destacada; negativo: sem jargão de cura, sem nome de produto.
   - **Curandeiro ancestral/tribal:** cena em varanda/cozinha rústica com elementos étnicos e bandeira dos EUA; sujeito robusto, colar/figurino tradicional, narrando um "segredo antigo"; estilo caseiro-quente, luz dourada; câmera handheld leve com closes no prop; voz grave em cadência de contação de história; negativo: sem citar cura milagrosa nem atacar entidade real por nome.
   - **Wellness/lifestyle:** cena em cozinha clara, preparo de suco/smoothie em tempo real; estilo aspiracional, luz natural; câmera em close nas mãos cortando para o rosto; tom de "amiga confidente"; negativo: sem prometer resultado sexual explícito na fala.
   - Para se aprofundar em consistência de personagem/produto entre vídeos de uma mesma persona, ver [Veo 3 — pipeline avançado](../recursos/veo3-avancado.md).

## Compliance

A digestão visual modela **estrutura, estética, formato e mecânica de CTA** — nunca os **claims médicos**, **testemunhos** ou **credenciais** dos concorrentes. As páginas com criativo minerado convergem no mesmo risco: **persona fabricada por IA apresentada como especialista real**, o que é padrão de arquétipo nesse nicho, não exceção — e ainda assim carrega risco alto de ban de página (Facebook) e exposição legal (FTC: fake testimonial, health claim não-substanciado, disclosure de afiliado, automação de DM). Toda linha da matriz marcada com **flag de compliance alta** deve ser tratada como "modelar a forma, descartar o conteúdo". Ver [Persuasão × Manipulação](../principios/persuasao-vs-manipulacao.md).

## Conexões
- [Gramática Visual](gramatica-visual.md) — o padrão consolidado que este pipeline produz e atualiza
- [Avatares/Experts](avatares-experts.md) — a taxonomia de arquétipos usada para cruzar a matriz-mestre (passo 4)
- [Páginas de Referência](paginas-referencia.md) — as páginas mineradas que alimentam os exemplos do schema
- [Arquitetura do Funil](arquitetura-do-funil.md) — onde o sinal de performance (comentários = proxy de conversão) se conecta ao restante do funil
- [Veo 3 — produzir os criativos](../recursos/veo3-criativos.md) — anatomia de prompt usada no output (passo 5)
- [Veo 3 — pipeline avançado](../recursos/veo3-avancado.md) — consistência de personagem entre criativos de uma mesma persona
- [Baixar qualquer VSL](../recursos/baixar-qualquer-vsl.md) — técnica de captura de vídeo aplicada ao passo 1
- [Persuasão × Manipulação](../principios/persuasao-vs-manipulacao.md) — o limite entre modelar estrutura e copiar claim
- [Segredo Imoral dos Anúncios](../principios/segredo-imoral-anuncios.md) — o disfarce de anúncio como conteúdo, presente em todo criativo orgânico minerado
- [Anatomia do Hook](../hooks/anatomia-do-hook.md) — a dimensão "hook visual" do schema se conecta direto ao pattern interrupt do hook
