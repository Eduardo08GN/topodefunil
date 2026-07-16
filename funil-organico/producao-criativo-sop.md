# SOP — Produção do Criativo (da oferta ao prompt Veo 3)

O **passo-a-passo operacional** que costura toda a base: dada uma oferta MaxWeb, produzir o prompt Veo 3 e o criativo do funil. É o "manual de operação" — cada passo aponta pro doc que o embasa.

- **Status:** ✅ consolidado (fecha o workflow de geração de prompt)
- **Princípio-mãe:** [Triangulação](../00-mapa/insights-empiricos.md) — signature (piso/estilo) × nossa copy (superior) × oferta (âncora). A signature dá a **forma**; a copy e a oferta dão o **conteúdo**.

## Pré-requisitos (decisões, não docs)
- [ ] **Oferta MaxWeb escolhida** (qual VSL/produto — ver [dissecação](../swipes/vsl-suplemento-masculino.md)).
- [ ] **Arquétipo de avatar** decidido ([avatares-experts](avatares-experts.md)).
- [ ] **Character Bible + Style Bible** travadas ([veo3-avançado](../recursos/veo3-avancado.md)) — a "atriz"/guru recorrente + o look fixo.

## Os 12 passos

**1. Preencher os SLOTS a partir da oferta** ([template-criativo](template-criativo.md))
`[MECANISMO]`, `[PROMESSA]`, `[VILÃO]`, `[PROP]`, `[AVATAR]`, `[PALAVRA-GATILHO]`. Mecanismo/promessa/prova saem da [VSL da oferta](../swipes/vsl-suplemento-masculino.md).

**2. Escolher o avatar-expert** congruente ([avatares-experts](avatares-experts.md) + [signature-por-arquétipo](signature-por-arquetipo.md)). Travar as Bibles.

**3. Escolher a prop-metáfora** ([prop-metaforas](prop-metaforas.md)) que **demonstra o MECANISMO real** (não um innuendo aleatório). Definir função: innuendo / demonstração / antes-depois.

**4. Escrever o roteiro em blocos** ([template-criativo](template-criativo.md)):
hook → problema+vilão → mecanismo+demonstração → prova → CTA. Usar a [fórmula do hook](../hooks/como-escrever-o-hook.md) (context-lean→scroll-stop→snapback, 1 subject/1 question), [fear-sells](../principios/fear-sells.md), [mecanismo-único](../principios/mecanismo-unico.md), [prova Bencivenga](../mentores/gary-bencivenga/segredo-fechamento.md).

**5. Quebrar em SHOTS de ≤8s** ([veo3-criativos](../recursos/veo3-criativos.md)) — um momento por prompt; continuidade via mesma Bible.

**6. Montar cada prompt Veo 3** ([veo3-criativos](../recursos/veo3-criativos.md), anatomia: cena/sujeito/fundo/ação/estilo/câmera/luz/áudio/paleta/negativos; estilo no início; JSON). Diálogo atribuído por personagem. **Texto/legenda/rótulo: SEMPRE no editor, nunca no prompt.**

**7. Aplicar o guardrail anti-irrealidade** ([checklist](../recursos/generated-ai-video-anti-irrealidade-checklist.md)): colar o bloco de **negativos**; evitar close de mão+objeto pequeno; escala do prop-herói fixa; líquido em volume (não fio fino); nada de texto na cena.

**8. Gerar** ([veo3-criativos](../recursos/veo3-criativos.md)): *fast* pra testar, *quality* pros aprovados; **2–4 takes** e escolher; upscale. *Generate & iterate.*

**9. QA pós-geração** ([checklist](../recursos/generated-ai-video-anti-irrealidade-checklist.md)): dedos (5, sem fusão), rosto/roupa/cenário estáveis, sem texto gerado, prop com escala fixa, sem objeto amorfo, líquido natural. **Falhou → refazer só o shot.**

**10. Editar** (CapCut/Premiere): **legenda karaokê** + overlays de texto/rótulo/produto, **grão** ([Dehancer](../recursos/veo3-criativos.md)), som, cortes, montar a sequência.

**11. Publicar no funil** ([arquitetura-do-funil](arquitetura-do-funil.md)): CTA de comentário (`[PALAVRA-GATILHO]`) + seguir → comment-to-DM → link afiliado MaxWeb (bio + comentários + DM).

**12. Compliance final** ([persuasão × manipulação](../principios/persuasao-vs-manipulacao.md) + [o-que-modelar×risco](signature-por-arquetipo.md)): sem persona médica fake, sem claim de cura/erétil direto, sem texto burlando filtro, **prova real**. Página banida mata o funil.

## Fluxo em uma linha
```
Oferta → slots → avatar+Bibles → prop → roteiro (copy nossa) → shots ≤8s →
prompt Veo3 (JSON, sem texto na cena) → guardrail anti-irrealidade →
gerar+QA → editar (legenda/grão) → publicar (comment-to-DM) → compliance
```

## O que ainda depende de você (não é lacuna de doc)
- **Escolher a oferta MaxWeb** → destrava os slots.
- **Signature verbal** (transcrições `compilado_*.md` em `C:\vsl\videos-criativo`) → quando você liberar, extraio só o padrão de estilo do CTA/hook (a copy deles **não** é referência de qualidade — a nossa é superior).
- **Definir e travar a Character/Style Bible** do nosso avatar (feito uma vez, no início da produção).

## Conexões
- [Template Criativo](template-criativo.md) · [Signature por Arquétipo](signature-por-arquetipo.md) · [Prop-Metáforas](prop-metaforas.md)
- [Veo 3 criativos](../recursos/veo3-criativos.md) · [Anti-Irrealidade checklist](../recursos/generated-ai-video-anti-irrealidade-checklist.md)
- [Arquitetura do Funil](arquitetura-do-funil.md) · [Insights: Triangulação](../00-mapa/insights-empiricos.md)
