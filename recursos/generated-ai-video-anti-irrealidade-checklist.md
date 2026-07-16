# Checklist Anti-Irrealidade — guardrail de prompt Veo 3

Regras **obrigatórias** ao gerar os prompts Veo 3 dos nossos criativos, derivadas da [auditoria dos 42 reels](generated-ai-video-anti-irrealidade.md). Objetivo: não repetir os 5 pontos fracos da IA — e fazer o exagero fálico parecer **intencional**, não glitch.

- **Status:** ✅ consolidado (guardrail de produção)

## As 5 regras de ouro (por ponto fraco)

### 1. TEXTO — nunca deixar o Veo escrever
- **Zero texto crítico na cena gerada:** rótulos de produto, pôsteres, placas, capas de livro, diplomas, telas → tudo entra **no editor (CapCut/Premiere)** como overlay, ou o produto é adicionado em pós.
- No prompt: descrever embalagens como **lisas/genéricas** ("frasco sem rótulo", "pôster desfocado ao fundo") e listar em **negativo**: `no on-screen text, no product labels, no readable signage, no gibberish text, blank labels`.
- Frascos/produtos com nosso rótulo real → **compositar em pós**, nunca pedir pro Veo desenhar.

### 2. MÃOS + objeto pequeno — evitar o close arriscado
- Evitar **close extremo de dedos segurando objeto pequeno** (onde a IA funde/alonga dedos).
- Preferir: objeto **apoiado na bancada**, mão em **plano mais aberto**, ou segurar com a **mão inteira** (não pinça de dedos).
- No prompt: `natural five-fingered hands, hands relaxed`; negativo: `deformed hands, extra fingers, fused fingers, elongated thumb`.
- Se precisar do close → **gerar 2–4 takes e escolher**, ou refazer só o shot.

### 3. CONSISTÊNCIA — sem troca de prop no corte
- O **prop-herói** (a fruta/produto) deve ser o **mesmo tamanho e forma** ao longo do clipe. Não fazer **corte duro** que troca a escala do prop (o "salto" expõe a IA).
- Antes/depois de tamanho → usar **dois objetos distintos no mesmo quadro** (não o mesmo objeto "crescendo" num corte).
- Character/Style Bible travadas ([veo3-avancado](veo3-avancado.md)) pra o avatar não morphar entre shots.

### 4. FÍSICA de líquido — cuidado com fio fino
- Líquido fino (suco pingando, filete) tende a virar "contas". Preferir **líquido em volume** (despejar de jarra, líquido já no copo, vapor de panela — que a IA faz bem) a **fio fino escorrendo**.
- No prompt: `smooth continuous pour`; negativo: `floating droplets, beaded liquid, unnatural fluid`.

### 5. FUNDO/asset — cena limpa e sem inset frágil
- Fundo **simples e reconhecível** (cozinha/varanda), sem objetos ambíguos. Negativo: `melting objects, deformed background people, blobby shapes`.
- Insets/telas de "reação" e gráficos → **no editor**, não pedir pro Veo compor.

## Prompt-base: bloco de NEGATIVOS padrão
Colar em todo prompt Veo 3 nosso:
```
Negativos: on-screen text, product labels, readable signage, gibberish text,
deformed/extra/fused fingers, elongated limbs, warped face, morphing between cuts,
floating/beaded liquid, melting or amorphous objects, deformed background people,
plastic/waxy skin, impossible shadows.
```

## As EXCEÇÕES propositais (manter — mas fazer parecer deliberado)
O exagero fálico/choque é **feature**, não bug. Pra ler como intencional e não glitch:
- **Ancorar no texto/piada** (a legenda nomeia a comparação: "antes × depois", "big like…").
- **Escala consistente** entre quadros (o objeto grande continua grande; nada "cresce" num corte).
- **Enquadramento claro** do prop (bem iluminado, nítido) — exagero proposital é **limpo**; glitch é borrado/ambíguo.
- Props aprovados: banana/pepino/berinjela grande, modelo anatômico antes/depois, vulcão de bicarbonato, geoduck/raiz de choque. → [catálogo](../funil-organico/prop-metaforas.md).

## Checklist de QA (rodar em cada criativo)
**Pré-geração (no prompt):** [ ] sem pedido de texto na cena · [ ] mãos em plano seguro · [ ] prop-herói com escala fixa · [ ] líquido em volume, não fio · [ ] bloco de negativos colado · [ ] Character/Style Bible travada.
**Pós-geração (revisar o take):** [ ] dedos ok (5, sem fusão) · [ ] rosto/roupa/cenário estáveis nos cortes · [ ] nenhum rótulo/placa gerado (só overlays de pós) · [ ] prop-herói não trocou de tamanho · [ ] sem objeto amorfo/derretido · [ ] líquido natural. **Qualquer falha → refazer só o shot** (barato) antes de montar.

## Compliance (lembrete)
Este doc é sobre **realismo técnico**. As regras de **conteúdo** (sem persona médica fake, sem claim de cura) estão em [Signature por Arquétipo](../funil-organico/signature-por-arquetipo.md) e [Persuasão × Manipulação](../principios/persuasao-vs-manipulacao.md).

## Conexões
- [Auditoria & Taxonomia](generated-ai-video-anti-irrealidade.md) — a evidência por trás destas regras
- [Veo 3 — criativos](veo3-criativos.md) · [Veo 3 avançado](veo3-avancado.md) · [Template Criativo](../funil-organico/template-criativo.md)
