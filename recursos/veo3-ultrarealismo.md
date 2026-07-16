# 🩸 Ultrarrealismo Veo 3 — fabricar REALIDADE, não evitar defeito

O [anti-irrealidade](generated-ai-video-anti-irrealidade-checklist.md) é o **piso** (não denunciar IA por erro). Este doc é o **teto**: fazer o vídeo passar por **filmagem real** no olho de um homem de 52 anos scrollando. A tese central que o padrão fraco ignorava:

> **O que denuncia IA não é o erro — é a PERFEIÇÃO.** Pele lisa demais, luz perfeita demais, simetria demais, cenário limpo demais, movimento flutuante demais. Realidade é feita de IMPERFEIÇÃO CONTROLADA. Quem não prompta imperfeição recebe plástico.

- **Status:** ✅ LEI de produção (par do [padrão de direção de cena](veo3-direcao-de-cena.md): aquele = o drama; este = a textura)
- **Teste-mãe:** congele 3 frames do take e pergunte: *"minha mãe scrollando acharia que é filmagem de celular de alguém?"* Na dúvida, é plástico — refaz.

## A KILL-LIST do "cheiro de IA" (o que grita 'gerado' — caçar e destruir)

| Denúncia | Antídoto no prompt |
|---|---|
| Pele de cera/porcelana | `natural skin texture, visible pores, slight skin imperfections, subtle sheen on forehead` |
| Simetria facial perfeita | `slightly asymmetrical natural face, lived-in features` |
| Dentes de outdoor | `natural teeth (not veneer-white)` |
| Luz "de estúdio" em cozinha | luz **motivada**: `single window light from the left, uneven exposure, soft shadow falloff` |
| Cores saturadas de videogame | `muted colors, cinematic film look, slightly faded` |
| Movimento flutuante/slow-motion involuntário | `natural weight in movement, real-time speed, grounded footsteps` |
| Olhar fixo sem piscar | `natural blinking, eyes drift and refocus on lens` |
| Cenário showroom (limpo/vazio/simétrico) | `lived-in space: everyday clutter, a coffee mug, mail on the counter, worn edges` |
| Roupa engomada sem física | `natural fabric wrinkles, clothes shift with movement` |
| Fundo desfocado "uniforme demais" | `natural depth of field falloff, recognizable but soft background objects` |
| Todo mundo bonito demais | figurantes/testemunhas = `ordinary-looking`, só os papéis-arma são calibrados ([casting](../funil-organico/ataque-5-casting-bibles.md)) |

## As 8 camadas do realismo (promptar TODAS as aplicáveis)

**1. PELE E CORPO** — `visible pores, fine facial hair, flyaway hairs catching light, faint under-eye texture, natural blush unevenness`; homem 55: `sun-weathered skin, crow's feet, gray stubble`. Suor/vida: `subtle sweat sheen` (praia/academia).

**2. LUZ MOTIVADA E SUJA** — toda luz vem de uma FONTE da cena (janela, abajur, sol). Misturar temperaturas (`warm lamp + cool window light mixing`). Aceitar imperfeição de exposição: `slightly blown-out window highlights, shadows with detail`. ❌ three-point lighting perfeito em cena doméstica.

**3. LENTE E CÂMERA COM CORPO** — a câmera é um OBJETO segurado por um HUMANO: `shot on iPhone, handheld with natural micro-shake, brief autofocus hunt, slight lens flare, sensor noise in the shadows, vertical 9:16`. Pra cinema: `35mm lens, f/1.8, shallow DOF with natural falloff, subtle film grain`. O micro-tremor de mão é o selo de autenticidade mais barato que existe.

**4. FÍSICA E PESO** — `cloth wrinkles and shifts as she moves, hair sways with the turn, her weight settles onto the counter, the bottle lands with a small thud`. Respiração visível em close: `subtle chest rise, a breath before speaking`.

**5. AMBIENTE VIVO** — o mundo continua existindo fora da ação: `dust motes in the sunbeam, steam rising from the mug, curtain moving slightly, a car passing outside the window, fridge hum`. Desgaste: `worn cutting board, water stains, chipped mug`.

**6. COMPORTAMENTO HUMANO IMPERFEITO** — `she glances away mid-sentence then back to the lens, small hesitation before the key word, adjusts her hair unconsciously, half-laugh between phrases`. Fala com respiração: `audible inhale before speaking, natural pauses, slightly uneven pacing` — NUNCA dicção de locutor.

**7. ÁUDIO DIEGÉTICO** — o som TEM que bater com a câmera: celular = `slightly compressed phone-mic audio, room echo`; cozinha = `room tone, distant dishes, fridge hum`; rua = `traffic bed, wind buffets on mic`. Voz sem ambiente = dublagem = IA.

**8. FORMATO NATIVO DA PLATAFORMA** — o realismo final é parecer POSTADO POR UMA PESSOA: enquadramento levemente torto, corte seco no início (sem fade), e na pós: legenda karaokê + **grão de filme sutil (Dehancer/overlay ~30%)** + leve crush nos pretos. Estéticas prontas: `smartphone vertical video` (UGC) · `security camera footage, timestamp overlay, slight fisheye, muted contrast` (flagrante) · `dashcam / GoPro chest mount` (POV).

## Bloco REALISM-SPEC (colar em TODO prompt de criativo, adaptando)
```
"realism": "shot on iPhone handheld, natural micro-shake, motivated window light with uneven exposure, natural skin texture with visible pores and slight imperfections, muted cinematic colors, real-time motion with natural weight, lived-in environment with everyday clutter, natural blinking and imperfect delivery, ambient room tone matching the space",
"negative": "studio lighting, plastic waxy skin, perfect symmetry, oversaturated colors, floaty slow motion, sterile empty background, ironed wrinkle-free clothes, static unblinking stare, voiceover-quality audio in casual setting"
```
*(Empilha com o bloco de negativos do [anti-irrealidade](generated-ai-video-anti-irrealidade-checklist.md) — um mata o defeito, o outro mata o plástico.)*

## Pipeline de realismo máximo (quando o shot é crítico)
1. **Imagem-base primeiro** ([veo3-avancado](veo3-avancado.md)): Midjourney/Nano Banana → **Enhancor** (pele) → **Magnific** (detail 30-50, grain 20-30) → image-to-video no Veo. Imagem hiper-real anima hiper-real.
2. **Take selection é 50% do realismo:** 2-4 takes, congelar frames, zoom em pele/mãos/fundo — escolher o take mais SUJO/crível, não o mais bonito.
3. **Pós obrigatória:** grão + color grade dessaturado + crush leve + (se UGC) 1-2% de zoom digital pra "quebrar" a perfeição do render.
4. **Upscale** Topaz (Proteus, recover detail 0) SÓ depois do grade.

## QA de ultrarrealismo (gate antes de publicar)
[ ] Congelou 3 frames e passou no teste-mãe? · [ ] Pele tem textura em zoom? · [ ] Luz tem FONTE visível/lógica? · [ ] Câmera tem tremor humano? · [ ] Fundo tem vida/desgaste? · [ ] Fala tem respiração/hesitação? · [ ] Áudio tem ambiente coerente? · [ ] Grão aplicado na pós? — **2+ "não" = take reprovado.**

## Conexões
- [Anti-Irrealidade (o piso)](generated-ai-video-anti-irrealidade-checklist.md) · [Direção de Cena (o drama)](veo3-direcao-de-cena.md) · [Veo3 Avançado (pipeline)](veo3-avancado.md)
- [Casting/Bibles](../funil-organico/ataque-5-casting-bibles.md) · [SOP](../funil-organico/producao-criativo-sop.md) · [Doutrina](../funil-organico/doutrina-criativa-agressiva.md)
