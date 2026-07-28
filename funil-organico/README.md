# Pilar: Operação — Funil Orgânico no Facebook

- **Status:** em construção (pilar novo, arquitetura mapeada + páginas de referência mineradas)
- **Contexto:** operação de afiliado 100% orgânica (sem tráfego pago) no nicho de saúde sexual masculina, rodando via páginas de Facebook com persona-expert gerada por IA.

> ⚠️ **ESTE DOCUMENTO É DA FASE DE PLANEJAMENTO (rede e oferta mudaram).** A teoria de
> viralização, hook e gramática visual continua válida. **Os fatos operacionais abaixo
> não** — rede, oferta, keyword e camadas de link já foram decididos e são outros.
> **Fonte da verdade operacional:** [`ARQUITETURA-OPERACAO.md`](ARQUITETURA-OPERACAO.md).
>
> | Aqui dizia | A realidade hoje |
> |---|---|
> | rede MaxWeb, produto TBD | **BuyGoods** — Horsewood (aff 45158) e Ragnaroak (aff 2470) |
> | CTA "comente Book" | **`GELATIN`**, travado. `BOOK`/`YES` quebram a automação |
> | link na bio + comentário + DM | **só DM.** Link público expõe o funil à Meta |
> | DM entrega link de afiliado | DM entrega a **bridge page**, nunca a VSL direta |

## Visão geral do modelo de negócio

A operação monetiza como **afiliado no BuyGoods** (ofertas de saúde/ED — disfunção erétil e performance masculina). Não há compra de tráfego: o crescimento vem de **páginas de Facebook** construídas em torno de uma **persona-expert** (ver [avatares-experts.md](avatares-experts.md)), que posta **vídeos-criativos gerados por IA** (Google Veo 3.1 — ver [`DOUTRINA-VEO-3.1.md`](../recursos/DOUTRINA-VEO-3.1.md)).

Cada vídeo termina com um **CTA de comentário** (`comment GELATIN` + follow gate). O comentário dispara uma **automação comment-to-DM** que entrega o link da **bridge page** direto na caixa de mensagem — **só na DM**, nunca na bio nem em comentário público. Da bridge o clique vai para a **VSL** da página (Horsewood ou Ragnaroak) e a venda gera comissão.

Como não há mídia paga, **viralização é o motor inteiro do negócio**: o jogo se resume a hook (retenção nos primeiros segundos) e formato replicável — ver [gramatica-visual.md](gramatica-visual.md). O proxy de conversão a acompanhar é **volume de comentários com a palavra-gatilho** (não likes/shares, que medem só alcance).

## O funil em uma linha

```
Página-persona (avatar-expert IA) → criativo orgânico (Veo 3.1, 9:16) → hook (0-3s) → CTA "comment GELATIN" → comment-to-DM (automação, só DM) → bridge page (domínio próprio) → VSL (Horsewood ou Ragnaroak) → venda (comissão BuyGoods)
```

## Índice dos docs do pilar

| Doc | O que cobre |
|-----|-------------|
| [arquitetura-do-funil.md](arquitetura-do-funil.md) | A engrenagem completa: página, automação comment-to-DM, camadas de link, mecânica de palavra-gatilho e métricas-proxy |
| [avatares-experts.md](avatares-experts.md) | Taxonomia dos arquétipos de persona-expert (autoridade médica, curandeiro ancestral, wellness influencer, marca institucional) e a alavanca de persuasão de cada um |
| [gramatica-visual.md](gramatica-visual.md) | O padrão visual que se repete nos criativos que viralizam: formato, avatar, prop-metáfora, texto na tela, cenário, CTA |
| [digestao-visual.md](digestao-visual.md) | O pipeline de 5 passos para minerar um criativo concorrente (baixar → keyframes → ler → agregar em matriz → destilar em template/prompt Veo 3) |
| [paginas-referencia.md](paginas-referencia.md) | As páginas concorrentes mineradas com persona, props e CTA de cada uma |
| **[signature-matriz.md](signature-matriz.md)** | A digestão visual de **42 reels (6 páginas)** — matriz de signature por página |
| **[signature-por-arquetipo.md](signature-por-arquetipo.md)** | O **padrão universal** destilado (o esqueleto que todas repetem) + os 3 arquétipos |
| **[signature-verbal.md](signature-verbal.md)** | O **roteiro-padrão** do áudio (5 blocos, hooks, dispositivos, mecânica de CTA) + mapa de ofertas |
| **[prop-metaforas.md](prop-metaforas.md)** | Catálogo dos props (banana/pepino/modelo anatômico…) e suas funções |
| **[template-criativo.md](template-criativo.md)** | O **template modelável** + prompt-base Veo 3 + os slots da triangulação (o output acionável) |
| **[producao-criativo-sop.md](producao-criativo-sop.md)** | O **SOP em 12 passos** (oferta → prompt Veo 3 → publicar) — o fio que costura todo o workflow |
| **[cruzamento-copy-excelencia.md](cruzamento-copy-excelencia.md)** | O **mapa** signature → nosso lever de copy superior → onde superamos (a lente obrigatória) |
| **[doutrina-criativa-agressiva.md](doutrina-criativa-agressiva.md)** | ⚡ **A LEI**: anti-copy-morna, Teste do Dedo, ataque reptiliano, FOMO, future projection — ler ANTES de gerar qualquer cena/copy |
| **[desejos-ocultos-50plus.md](desejos-ocultos-50plus.md)** | O **mapa da mina**: 15 desejos ocultos + 7 feridas do homem US 50+, cada um com hook-cena candidato |
| **[pecados-capitais-50plus.md](pecados-capitais-50plus.md)** | 🔥 O **arsenal de instintos**: os 7 pecados capitais mapeados no avatar (luxúria/soberba abrem o hook, ≥2 empilhados por peça) + tabela pecado × desejo × ferida — par obrigatório do mapa de desejos |
| **[arsenal-linguagem-indireta.md](arsenal-linguagem-indireta.md)** | 🗣️ O **banco de eufemismo**: como referenciar o órgão, firme/murcho, tamanho, fôlego e a reação dela sem a palavra banida + linhas prontas por gatilho — a fonte fixa de toda copy |
| **[diretrizes-script-32s.md](diretrizes-script-32s.md)** | ⚙️🔥 **A LINHA DE MONTAGEM**: toda a base de copy comprimida no processo único do script de 32s (brief → 4 clipes → voz → gate → CTA → QA) + orçamento de mecanismo (1 tease, zero explicação) + os 9 erros de campo — LER ANTES de escrever qualquer script |
| **[operacao-contas-paginas.md](operacao-contas-paginas.md)** | 🏗️ **INFRA (campo)**: comprar páginas US antigas 2020-2023, perfil de família, 5 páginas por perfil, proxy, geo restrição, cadência, ciclo de viralização de 15-20 dias |
| **[operacao-automacao-cta.md](operacao-automacao-cta.md)** | 🤖 **AUTOMAÇÃO (campo)**: comment to DM só na DM (nunca resposta de comentário = ban), Meta Business Suite, por que a API do FB não serve, risco do Instagram |
| **[producao-pipeline-video.md](producao-pipeline-video.md)** | 🎬 **PIPELINE (campo)**: garimpagem → agente cloud → Flow/Nano Banana → Veo 3 lower priority → CapCut, custos, volume sem perfeccionismo |
| **[estrategia-mercado-oferta.md](estrategia-mercado-oferta.md)** | 🌊 **MERCADO (campo)**: a onda do Veo 3, nichos (ED, weight, Amazon Ultra), VSL black (com alerta de compliance), Stories, e as divergências da nossa estratégia (persona fixa, 32s) |
| **[empilhamento-reptiliano.md](empilhamento-reptiliano.md)** | ⚡ A **fórmula multiplicadora** do hook (desejo × posse × testemunha × dominância) + banco de cenas-evento + hipérbole situacional + **leque de 30 ângulos situacionais em 6 famílias** (rotação anti-afunilamento) |
| **[guerra-reptiliana-angulos.md](guerra-reptiliana-angulos.md)** | ⚔️ O **GERADOR de ângulos**: 9 botões reptilianos × 8 famílias de cena inexploradas (G–N: POV, flagrante, objeto-protagonista, confissão…) × matriz anti-vício de rota |

### 🗡️ O Plano de Ataque (7 docs — a máquina de hooking)
| Doc | O que cobre |
|-----|-------------|
| **[ataque-1-neuro-hooking.md](ataque-1-neuro-hooking.md)** | Neurocopy → vídeo: ordem de ataque aos 3 cérebros, neurônios-espelho, power words EN, Kenrick, dopamina/loops, Fitts/Hick |
| **[ataque-2-benson-video.md](ataque-2-benson-video.md)** | Benson comprimido: regra dos 60%, neuro-opening, 3 loops encadeados, 1 ideia/1 CTA, objeções-relâmpago, oratória |
| **[ataque-3-georgi-research.md](ataque-3-georgi-research.md)** | RMBC do criativo: research na voz do avatar (comentários/reviews/Reddit), MUP→MUS, brief de 10 linhas, ciclo vivo |
| **[ataque-4-roteiro-maquina.md](ataque-4-roteiro-maquina.md)** | ⏱️ **LEI dos 35s** + a régua segundo a segundo, 10 aberturas prontas, fórmulas de transição, CTA de guerra, variante curta 15-22s, QA |
| **[ataque-5-casting-bibles.md](ataque-5-casting-bibles.md)** | Casting reptiliano: 7 Bibles prontas (Sky, Lauren, Maya, Frank, Denise, rival, Solomon) + Style Bibles + escalação |
| **[ataque-6-fabrica-escala.md](ataque-6-fabrica-escala.md)** | A fábrica: 1 corpo × N hooks, cadência semanal, métricas (comment rate = north star), kill/iterate/scale, tracker |
| **[ataque-7-entrevista-decisoes.md](ataque-7-entrevista-decisoes.md)** | 🎙️ A entrevista: as 10 decisões do operador que ligam a máquina (com recomendações) |
| **[copy-humana.md](copy-humana.md)** | 🫀 **Verdade > Técnica**: o anti-bingo de copywriting — 8 leis + gate ("isso aconteceu" vs "que copy boa") — a pele humana sobre o esqueleto da régua |
| **[o-que-igualar-dos-exemplos.md](o-que-igualar-dos-exemplos.md)** | 🔥 A crueza que eu sanitizava: 5 elementos a IGUALAR do piso (crueza sensorial, receita tangível, reação dela vívida, escassez, tribo) — sanitizar a palavra ≠ sanitizar o tom |

> Insight-mãe da operação: [../00-mapa/insights-empiricos.md](../00-mapa/insights-empiricos.md) (triangulação signature × copy × oferta).

## Como o pilar se conecta com o resto da base

Esta operação é a **ponte entre copy e produção**: a persuasão que sustenta o funil vem dos princípios e formatos já mapeados no cérebro de copy; a execução visual depende do recurso de geração em vídeo.

- **Copy (persuasão do criativo e do CTA):** [../hooks/anatomia-do-hook.md](../hooks/anatomia-do-hook.md) e [../hooks/como-escrever-o-hook.md](../hooks/como-escrever-o-hook.md) (o hook visual/falado dos 3 primeiros segundos) · [../hooks/biblioteca-de-formatos.md](../hooks/biblioteca-de-formatos.md) (arquétipos de hook aplicáveis ao roteiro Veo 3) · [../principios/fear-sells.md](../principios/fear-sells.md) (o medo que vende — status/relacionamento, não a doença) · [../principios/mecanismo-unico.md](../principios/mecanismo-unico.md) (a alavanca do arquétipo tribal/curandeiro) · [../principios/cialdini-kawasaki.md](../principios/cialdini-kawasaki.md) (autoridade/prova social dos arquétipos médicos) · [../principios/segredo-imoral-anuncios.md](../principios/segredo-imoral-anuncios.md) (disfarçar anúncio de conteúdo orgânico) · [../principios/tres-cerebros.md](../principios/tres-cerebros.md) e [../principios/persuasao-vs-manipulacao.md](../principios/persuasao-vs-manipulacao.md) (limite ético do funil)
- **A oferta final:** [../swipes/vsl-suplemento-masculino.md](../swipes/vsl-suplemento-masculino.md) — as 9 VSLs dissecadas de onde sairá o produto MaxWeb a promover; [../mentores/gary-bencivenga/segredo-fechamento.md](../mentores/gary-bencivenga/segredo-fechamento.md) (fechamento aplicado à VSL de destino)
- **Produção do criativo:** [../recursos/veo3-criativos.md](../recursos/veo3-criativos.md) (workflow base Veo 3) e [../recursos/veo3-avancado.md](../recursos/veo3-avancado.md) (pipeline avançado — hiper-realismo e consistência de persona entre vídeos)

## Nota de compliance

Persona-expert **fabricada por IA** apresentada como especialista real + claims de "cura" de ED + testemunhos/credenciais falsos = risco **alto** de ban de página (Facebook) e exposição legal (FTC: testemunho falso, health claim não substanciado, ausência de disclosure de afiliado, automação de DM). **Regra da operação:** modelar apenas o que é modelável — estrutura, estética, formato, CTA — e **nunca** os claims médicos nem credenciais falsas. Página banida mata o funil inteiro. Ver [../principios/persuasao-vs-manipulacao.md](../principios/persuasao-vs-manipulacao.md).

**⚡ E a contraparte de mesmo peso:** compliance limita a PALAVRA e os CLAIMS — nunca a intensidade. Criativo morno "por segurança" é a outra forma de matar o funil (invisibilidade). A régua de agressividade obrigatória (Teste do Dedo, ataque reptiliano, desejos ocultos, cenas-evento empilhadas) está na [Doutrina Criativa Agressiva](doutrina-criativa-agressiva.md) — os dois guardrails andam juntos: **palavra limpa, cena impiedosa.**

## Conexões
- [../principios/segredo-imoral-anuncios.md](../principios/segredo-imoral-anuncios.md)
- [../principios/fear-sells.md](../principios/fear-sells.md)
- [../principios/mecanismo-unico.md](../principios/mecanismo-unico.md)
- [../principios/cialdini-kawasaki.md](../principios/cialdini-kawasaki.md)
- [../principios/tres-cerebros.md](../principios/tres-cerebros.md)
- [../principios/persuasao-vs-manipulacao.md](../principios/persuasao-vs-manipulacao.md)
- [../hooks/anatomia-do-hook.md](../hooks/anatomia-do-hook.md)
- [../hooks/como-escrever-o-hook.md](../hooks/como-escrever-o-hook.md)
- [../hooks/biblioteca-de-formatos.md](../hooks/biblioteca-de-formatos.md)
- [../mentores/gary-bencivenga/segredo-fechamento.md](../mentores/gary-bencivenga/segredo-fechamento.md)
- [../swipes/vsl-suplemento-masculino.md](../swipes/vsl-suplemento-masculino.md)
- [../recursos/veo3-criativos.md](../recursos/veo3-criativos.md)
- [../recursos/veo3-avancado.md](../recursos/veo3-avancado.md)
