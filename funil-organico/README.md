# Pilar: Operação — Funil Orgânico no Facebook

- **Status:** em construção (pilar novo, arquitetura mapeada + páginas de referência mineradas)
- **Contexto:** operação de afiliado 100% orgânica (sem tráfego pago) no nicho de saúde sexual masculina, rodando via páginas de Facebook com persona-expert gerada por IA.

## Visão geral do modelo de negócio

A operação monetiza como **afiliado da rede MaxWeb** (ofertas de saúde/ED — disfunção erétil e performance masculina). Não há compra de tráfego: o crescimento vem de **páginas de Facebook** construídas em torno de uma **persona-expert** (ver [avatares-experts.md](avatares-experts.md)), que posta **vídeos-criativos gerados por IA** (Google Veo 3 — ver [../recursos/veo3-criativos.md](../recursos/veo3-criativos.md) e [../recursos/veo3-avancado.md](../recursos/veo3-avancado.md)).

Cada vídeo termina com um **CTA de comentário** (ex.: "comente Book e siga a página"). O comentário dispara uma **automação comment-to-DM** que entrega o **link de afiliado da MaxWeb** direto na caixa de mensagem — com camadas redundantes de link também na bio (encurtador linktw.in) e nos comentários fixados. Quem clica cai numa **VSL** (o produto final da MaxWeb ainda será escolhido entre os já dissecados em [../swipes/vsl-suplemento-masculino.md](../swipes/vsl-suplemento-masculino.md)) e a venda gera comissão.

Como não há mídia paga, **viralização é o motor inteiro do negócio**: o jogo se resume a hook (retenção nos primeiros segundos) e formato replicável — ver [gramatica-visual.md](gramatica-visual.md). O proxy de conversão a acompanhar é **volume de comentários com a palavra-gatilho** (não likes/shares, que medem só alcance).

## O funil em uma linha

```
Página-persona (avatar-expert IA) → criativo orgânico (Veo 3, 9:16) → hook (0-3s) → CTA de comentário (palavra-gatilho) → comment-to-DM (automação) → link afiliado MaxWeb (bio + comentários + DM) → VSL/oferta → venda (comissão)
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
| **[prop-metaforas.md](prop-metaforas.md)** | Catálogo dos props (banana/pepino/modelo anatômico…) e suas funções |
| **[template-criativo.md](template-criativo.md)** | O **template modelável** + prompt-base Veo 3 + os slots da triangulação (o output acionável) |
| **[producao-criativo-sop.md](producao-criativo-sop.md)** | O **SOP em 12 passos** (oferta → prompt Veo 3 → publicar) — o fio que costura todo o workflow |

> Insight-mãe da operação: [../00-mapa/insights-empiricos.md](../00-mapa/insights-empiricos.md) (triangulação signature × copy × oferta).

## Como o pilar se conecta com o resto da base

Esta operação é a **ponte entre copy e produção**: a persuasão que sustenta o funil vem dos princípios e formatos já mapeados no cérebro de copy; a execução visual depende do recurso de geração em vídeo.

- **Copy (persuasão do criativo e do CTA):** [../hooks/anatomia-do-hook.md](../hooks/anatomia-do-hook.md) e [../hooks/como-escrever-o-hook.md](../hooks/como-escrever-o-hook.md) (o hook visual/falado dos 3 primeiros segundos) · [../hooks/biblioteca-de-formatos.md](../hooks/biblioteca-de-formatos.md) (arquétipos de hook aplicáveis ao roteiro Veo 3) · [../principios/fear-sells.md](../principios/fear-sells.md) (o medo que vende — status/relacionamento, não a doença) · [../principios/mecanismo-unico.md](../principios/mecanismo-unico.md) (a alavanca do arquétipo tribal/curandeiro) · [../principios/cialdini-kawasaki.md](../principios/cialdini-kawasaki.md) (autoridade/prova social dos arquétipos médicos) · [../principios/segredo-imoral-anuncios.md](../principios/segredo-imoral-anuncios.md) (disfarçar anúncio de conteúdo orgânico) · [../principios/tres-cerebros.md](../principios/tres-cerebros.md) e [../principios/persuasao-vs-manipulacao.md](../principios/persuasao-vs-manipulacao.md) (limite ético do funil)
- **A oferta final:** [../swipes/vsl-suplemento-masculino.md](../swipes/vsl-suplemento-masculino.md) — as 9 VSLs dissecadas de onde sairá o produto MaxWeb a promover; [../mentores/gary-bencivenga/segredo-fechamento.md](../mentores/gary-bencivenga/segredo-fechamento.md) (fechamento aplicado à VSL de destino)
- **Produção do criativo:** [../recursos/veo3-criativos.md](../recursos/veo3-criativos.md) (workflow base Veo 3) e [../recursos/veo3-avancado.md](../recursos/veo3-avancado.md) (pipeline avançado — hiper-realismo e consistência de persona entre vídeos)

## Nota de compliance

Persona-expert **fabricada por IA** apresentada como especialista real + claims de "cura" de ED + testemunhos/credenciais falsos + innuendo sexual = risco **alto** de ban de página (Facebook) e exposição legal (FTC: testemunho falso, health claim não substanciado, ausência de disclosure de afiliado, automação de DM). **Regra da operação:** modelar apenas o que é modelável — estrutura, estética, formato, CTA — e **nunca** os claims médicos nem credenciais falsas. Página banida mata o funil inteiro. Ver [../principios/persuasao-vs-manipulacao.md](../principios/persuasao-vs-manipulacao.md).

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
