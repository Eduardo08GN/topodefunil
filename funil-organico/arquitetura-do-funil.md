# Arquitetura do Funil Orgânico (Facebook + IA + MaxWeb)

- **Status:** 🟡 em construção
- **Serve para:** mapear o funil ponta-a-ponta — da página-persona até a comissão de afiliado — pra qualquer criativo/produto novo encaixar sem reinventar a engenharia
- **Contexto:** operação 100% orgânica (sem tráfego pago) no Facebook, com criativos gerados por IA (Veo 3), pra ofertas de afiliado da rede **MaxWeb** no nicho de saúde sexual masculina (disfunção erétil/performance)

> **A tese central:** como não há mídia paga empurrando o vídeo, o **algoritmo do Facebook é o único distribuidor** — e ele só empurra o que retém e engaja. Por isso o funil inteiro é desenhado pra colocar **hook e retenção no centro de tudo**: sem viralização não existe alcance, sem alcance não existe comentário, sem comentário não existe DM, sem DM não existe clique no link de afiliado. Cada elo depende do anterior.

## O funil em 8 elos

```
1. PÁGINA-PERSONA (arquétipo de expert)
        ↓
2. CRIATIVO ORGÂNICO (vídeo IA, Veo 3, 9:16)
        ↓
3. HOOK (1-2s, scroll-stop) → RETENÇÃO até o fim
        ↓
4. CTA DE COMENTÁRIO ("comente [palavra] e siga [página]")
        ↓
5. AUTOMAÇÃO COMMENT-TO-DM (dispara ao detectar a palavra-gatilho)
        ↓
6. REPLY NA DM (entrega o link de afiliado MaxWeb)
        ↓
7. CLIQUE → VSL / oferta (produto MaxWeb, ainda TBD)
        ↓
8. VENDA → comissão de afiliado
```

Cada elo é auditável por um sinal diferente (ver seção de métricas). Se a operação não vender, o primeiro lugar a olhar é **onde a cadeia quebrou**, não "o produto é ruim" — quebra pode estar no hook (sem retenção), no CTA (sem comentário) ou na automação (sem entrega do link).

## Elo 1 — Página-persona

Cada página de Facebook carrega **uma persona-expert consistente** (avatar gerado por IA, sempre o mesmo rosto/figurino/cenário), construída num dos arquétipos mapeados em [avatares-experts.md](avatares-experts.md). A persona é o "rosto" que dá contexto e autoridade/relatabilidade ao conteúdo — sem ela, o vídeo é só um clipe solto; com ela, vira "mais um post daquele perfil que eu já sigo e confio".

A página funciona como ativo de mídia própria: quanto mais seguidores e histórico de engajamento, mais o algoritmo testa o próximo post pra uma audiência maior (efeito composto). Por isso o CTA de "seguir" (elo 4) não é cosmético — é o que constrói esse ativo ao longo do tempo.

## Elo 2 — Criativo orgânico (Veo 3)

O vídeo é produzido com Google Veo 3 seguindo a [gramática visual comum](gramatica-visual.md) minerada das páginas de referência (formato 9:16, avatar consistente, cenário doméstico/autoridade + bandeira dos EUA, prop-metáfora, legenda estilo karaoke). O processo de produção (prompting, consistência de personagem, técnicas de câmera/áudio) está em [Veo 3 — vídeos-criativos](../recursos/veo3-criativos.md) e no [pipeline avançado](../recursos/veo3-avancado.md) (hiperrealismo, consistência entre cenas).

## Elo 3 — Hook e retenção (o motor do orgânico)

**Por que orgânico muda o jogo:** numa operação paga, um vídeo fraco ainda roda porque a verba compra a distribuição. Numa operação orgânica, a distribuição **é ganha** — o algoritmo do Facebook decide expandir o alcance de um post com base em sinais de retenção e engajamento nos primeiros espectadores. Isso inverte a prioridade de produção: o hook (primeiro 1-2s, interrupção de padrão) e a retenção até o fim do vídeo não são "um componente a mais" da copy — são a **condição de existência** do funil. Um criativo com oferta perfeita e hook fraco morre sem alcance; um hook forte com oferta mediana ainda gera volume de comentários pra testar.

Essa é a razão de a página priorizar, na produção, exatamente os elementos que a [gramática visual](gramatica-visual.md) documenta como recorrentes nos concorrentes que performam: hook de curiosidade no frame de abertura, prop-metáfora caseira, presenter que gera scroll-stop, legenda grande estilo karaoke.

## Elo 4 — CTA de comentário + follow

No fim do vídeo, a persona pede uma ação de baixo atrito: **comentar uma palavra-gatilho específica** e **seguir a página**. Duas funções em paralelo:

- **Follow** → constrói o ativo de audiência da página (algoritmo passa a testar posts futuros numa base maior — ver elo 1).
- **Comentário da palavra-gatilho** → (a) sinal de engajamento que o algoritmo do Facebook lê como "conteúdo relevante, seguir empurrando" e (b) **gatilho técnico** que aciona a automação do elo 5. O comentário faz dupla função: é métrica e é mecanismo.

Copy de post observada nas referências: *"100,000 men flushed blue pills after this simple trick"*; *"Comment YES if you want more remedies like this"*.

## Elo 5 — Automação comment-to-DM

Uma automação monitora os comentários do post e, ao detectar a palavra-gatilho configurada, dispara um **reply automático via Direct Message** para quem comentou. Esse é o ponto de transição do público (comentário público) para o privado (DM) — onde o link pode ser entregue sem ficar exposto no feed pra qualquer um copiar/reportar.

## Elo 6 — Reply na DM (entrega do link)

A DM automática entrega o **link de afiliado MaxWeb**. Esse é o primeiro ponto de fricção real do funil (a pessoa precisa abrir a DM e clicar) — por isso a operação **não depende de um único canal de link**, e sim de 3 camadas redundantes:

| Camada | Onde vive | Função |
|---|---|---|
| **Bio** | Link na bio da página, via encurtador **linktw.in** | Fallback permanente — quem visita o perfil por curiosidade (sem comentar) ainda encontra o caminho |
| **Comentários** | Link (ou instrução) postado nos comentários do vídeo | Reforço público visível a qualquer um rolando os comentários, mesmo sem esperar a DM |
| **DM** | Mensagem automática comment-to-DM | Canal primário — entrega direta, individualizada, após a ação de comentar |

A lógica é: se uma camada falhar (DM atrasa, link do comentário for removido em moderação), as outras seguem entregando. É engenharia de redundância pra não perder venda por falha de infraestrutura.

## Elo 7 — Clique → VSL / oferta

O link de afiliado leva à **oferta MaxWeb**, uma VSL. O produto específico ainda está **TBD** — candidato entre as VSLs já dissecadas em [Anatomia da VSL de Suplemento Masculino](../swipes/vsl-suplemento-masculino.md) (ex.: ErectPrime, EndoPeak, Boosterro). A escolha do produto é uma decisão separada da arquitetura do funil: o funil de tráfego (elos 1-6) é o mesmo independente de qual VSL for escolhida — só o link muda.

## Elo 8 — Venda → comissão

A MaxWeb é a **rede de afiliado**: rastreia o clique até a venda na VSL e paga comissão. Não há dado de ticket/comissão/EPC documentado ainda — isso é definido junto com a escolha do produto (elo 7).

## Por que "comentários" é a métrica-proxy central

Como o funil é orgânico e a DM é automática (sem visibilidade manual de quem recebeu o quê), **o comentário com a palavra-gatilho é o evento mensurável mais próximo da intenção de compra** disponível no próprio Facebook — é o único ponto da jornada em que o lead declara ativamente "eu quero o link". Por isso:

| Sinal | O que mede | Onde fica no funil |
|---|---|---|
| **Comentários (com a palavra-gatilho)** | Proxy de conversão — quantos pediram o link | Elo 4 → gatilho do elo 5 |
| **Likes / shares** | Alcance / viralização do criativo | Elo 3 (retenção que o algoritmo recompensa) |

Um vídeo com muitos likes/shares mas poucos comentários-com-palavra indica hook forte e CTA fraco (ou incongruente com o conteúdo). Um vídeo com poucos likes mas comentários concentrados indica alcance pequeno mas audiência qualificada. Comparar essas duas colunas por criativo é o diagnóstico mais rápido de onde ajustar.

## Tabela — palavras-gatilho observadas

Todas **confirmadas nas transcrições** (ver [signature-verbal.md](signature-verbal.md)):

| Palavra-gatilho | Página(s) | Ecoa… |
|---|---|---|
| **book** | Tanisha, Men's | "complete male health protocol" |
| **yes** | Kofi, Zuberi | afirmação simples ("more remedies") |
| **gelatin** | Kofi | o ingrediente ("only gelatin I trust") |
| **girth / would** | Nitric | o benefício ("male thickness protocol") |
| **link / secret / cortisol / help** | Olivia | o produto/mecanismo |
| **hard** | Zuberi | eufemismo/benefício |
| **boost / drive / apex / rocket** | Men's | o produto ("Apex Drive Pro") |

> **Padrão da palavra-gatilho:** ela **ecoa algo dito/mostrado no vídeo** (ingrediente, benefício, nome do produto) — reduz fricção cognitiva (a pessoa só repete o que acabou de ver) e confirma que assistiu até o CTA. Sempre acompanhada do **follow-gate reenquadrado** ("siga primeiro, senão o sistema não me deixa te enviar") — ver [signature-verbal.md](signature-verbal.md).

## Nota de compliance

Dois riscos jurídicos/operacionais específicos deste elo do funil (automação + entrega de link), além do risco de claim médico/persona fabricada já coberto em [avatares-experts.md](avatares-experts.md):

- **ToS de automação de DM:** ferramentas de comment-to-DM operam sobre a API/Políticas da Plataforma Meta — usar fora dos termos (spam, mensagem não solicitada em volume, contornar limites) é motivo de suspensão da automação e, em cascata, da própria página.
- **Disclosure de afiliado (FTC):** o link entregue é de afiliado — a ausência de divulgação clara ("eu ganho comissão se você comprar") é uma prática vedada pela FTC nos EUA (mercado-alvo desta operação). É um risco separado do risco de claim de saúde, e ambos precisam de tratamento — ver [Persuasão × Manipulação](../principios/persuasao-vs-manipulacao.md) sobre onde fica a linha ética, e a nota de compliance completa em [avatares-experts.md](avatares-experts.md).

**Regra prática:** modelar a **estrutura** do funil (arquitetura de 8 elos, camadas de link, mecânica de comentário→DM) é seguro e é o que este documento cobre. Modelar **claims de cura, credenciais falsas ou ausência de disclosure de afiliado** é o que muda o risco de "operação agressiva" para "operação que pode ser banida/multada". Página banida mata o funil inteiro — todos os elos dependem da página 1 estar no ar.

## Conexões
- [Avatares/Experts](avatares-experts.md) — os arquétipos de persona que ocupam o elo 1
- [Gramática Visual](gramatica-visual.md) — os elementos recorrentes que sustentam o elo 3 (hook/retenção)
- [Páginas de Referência](paginas-referencia.md) — as páginas mineradas de onde vêm os exemplos deste documento
- [Digestão Visual](digestao-visual.md) — o processo de minerar novos criativos de concorrentes
- [Veo 3 — vídeos-criativos](../recursos/veo3-criativos.md) / [Veo 3 — pipeline avançado](../recursos/veo3-avancado.md) — produção do elo 2
- [Anatomia da VSL de Suplemento Masculino](../swipes/vsl-suplemento-masculino.md) — a oferta que recebe o clique no elo 7
- [Segredo Imoral dos Anúncios](../principios/segredo-imoral-anuncios.md) — por que o criativo se disfarça de conteúdo, não de anúncio
- [Fear Sells](../principios/fear-sells.md) — a alavanca emocional por trás da oferta ED
- [Mecanismo Único](../principios/mecanismo-unico.md) — por trás do prop-metáfora/"segredo" de cada persona
- [Cialdini e Kawasaki](../principios/cialdini-kawasaki.md) — autoridade/prova social nos arquétipos de expert
- [Os Três Cérebros](../principios/tres-cerebros.md) — por que hook/prop visual precede qualquer argumento racional
- [Persuasão × Manipulação](../principios/persuasao-vs-manipulacao.md) — onde fica a linha ética nesta operação
