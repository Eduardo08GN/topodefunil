# Veo 3 — produzir os vídeos-criativos com IA

- **Fonte:** síntese de 8 tutoriais sobre Google Veo 3 / 3.1 (produção de anúncios em vídeo com IA)
- **Serve para:** gerar os criativos (ads/aberturas de VSL) que carregam nossos [hooks](../hooks/README.md) — vídeos com cara de produção de $100k a partir de **um prompt**
- **Status:** ✅ consolidado
- **Nível avançado (hiperrealismo, consistência, face-swap, multi-câmera):** [Veo 3 — pipeline avançado](veo3-avancado.md)

> **Onde isso se encaixa na base:** o Veo é a **ferramenta de produção**. A copy/estratégia (hook, mecanismo, oferta) vem da nossa base; o Veo entrega o **hook visual** ([key visual + scroll-stop](../hooks/anatomia-do-hook.md)) e as **cenas dramáticas de abertura** das VSLs ([anatomia da VSL](../swipes/vsl-suplemento-masculino.md)).

## A regra de ouro
**Escreva como um DIRETOR, não pergunte como no ChatGPT.** Veo é sofisticado: prompt raso = resultado medíocre. Você está **dando direção de cena** a quem nunca a viu mas pode criá-la na hora. **Quanto mais claro você descreve, mais controle você tem** — esse é o jogo inteiro. Por que Veo (e não outros): é o único que junta **áudio + fala com lip-sync + controle cinematográfico real** num só prompt.

## Anatomia do prompt (os componentes)
Inclua quase sempre, nesta lógica (funde os "10 componentes" + a fórmula de 7 pontos):
1. **Cena** (o setup: "um capitão entrega uma fala no convés ao pôr do sol"; ou "man on the street", "POV shot")
2. **Sujeito** (quem é, aparência detalhada)
3. **Fundo/background** (o que acontece atrás)
4. **Ação** (o que o sujeito faz)
5. **Estilo** (ex.: "horror cinematic" vs "comedy cinematic" — define o humor) → **coloque o estilo no INÍCIO: Veo pesa mais as palavras do começo**
6. **Câmera** (tipo de plano, ângulo, movimento, lente)
7. **Composição**
8. **Iluminação + mood** (ex.: "golden hour, tons quentes" / "azul frio, sombras pesadas")
9. **Áudio** (diálogo, som ambiente, música)
10. **Paleta de cores** (opcional, pra ir mais fundo)
11. **Instruções negativas** (o que NÃO gerar — muita gente esquece)

**JSON prompting > texto corrido:** estruturar o prompt em JSON (papéis/instruções em tokens legíveis, sem "fluff") dá resultado bem mais cinematográfico. Não escreva na mão.

## O meta-workflow (o pulo do gato)
> **A arte é a sua IDEIA, não o prompt.** O prompt é só o "tradutor" entre sua ideia e a linguagem do modelo. Deixe uma IA traduzir pra outra IA.

Como montar:
1. **Treine um GPT/Gem** na **documentação oficial do modelo** (Veo: DeepMind → Build with Gemini → docs → "prompt writing basics") **ou** numa coleção de **exemplos JSON**.
2. Dê sua **ideia simples** entre colchetes (ex.: "entrevista de rua com um chimpanzé") → ele **expande** no prompt otimizado.
3. Cole no gerador. **Generate & iterate:** resultado ruim? Diga o que errou (ou anexe print) e peça o ajuste — não reescreva na mão.

## Técnicas essenciais
- **Diálogo:** atribua a fala **por personagem** explicitamente ("o repórter diz X; o vilão diz Y"). Controle de **tom** funciona melhor descrevendo a ideia geral do que com script fixo. **Sotaque** só cola se for **plausível no ambiente** (um brasileiro na praia do Rio ganha sotaque; numa loja em NY, não).
- **Áudio:** peça **som ambiente** ("ondas", "vento + buzinas") e **música com instrumentos específicos** — deixa o vídeo imersivo.
- **Câmera = storytelling:** varie **plano** (close / corpo inteiro / long shot), **ângulo** (low angle = poderoso; high angle = fraco; bird's eye = visão do ambiente), **movimento** (dolly, pan, tilt, crane, orbit, zoom) e **lente** (fisheye, macro, infravermelho). Combine os três pros vídeos mais dinâmicos.
- **Gênero e estilo:** trocar o **gênero de filme** (horror/comédia/sci-fi) muda cor e mood. Pra **estilo de animação** (anime, Pixar 3D), ponha o keyword **no começo**. "muted colors, cinematic film" ajuda a fugir do visual "video game 3D".
- **Iluminação/paleta:** dessaturado (Saving Private Ryan = gritty), tons frios (frieza), quentes (aconchego), monocromático.

## Personagem / produto CONSISTENTE (para série de ads)
Melhor método: **gere imagens consistentes primeiro, depois anime (image-to-video).**
- Crie o personagem/produto e replique-o com **omni-reference** (Midjourney) ou **Flux Context** — mesma aparência em cenas novas.
- Anime cada imagem no Veo (frames-to-video).
- **Limitação:** com imagem de referência, o Veo **não gera diálogo** → use lip-sync externo (ex.: Higgsfield/apps de lip sync) se precisar falar.
- Alternativas: descrição textual hiperdetalhada do personagem repetida; "green screen hack"; mas image-to-video é o mais consistente. (Recursos "ingredients"/"extend"/"frame interpolation" caem no **Veo 2 antigo** — sem áudio.)

## Quebrar o limite de 8 segundos (vídeos longos)
1. **Pense em SHOTS, não em vídeo.** Não tente um filme de 30s num prompt — Veo é *construtor de cena*, não editor. Cramming (3 personagens, 4 ações, 2 locais) confunde a IA.
2. Quebre em: intro → ação → reação → fecho. **Um momento visual por prompt.**
3. **Continuidade:** repita **mesmo personagem, ambiente e estilo** entre os clipes.
4. **Veo 3.1 — start/end frame:** defina 1º e último frame; o modelo preenche a transição (ótimo pra narrativa). **Chaining:** troque o *end frame* pra virar o *start* do próximo clipe → comprimento **~ilimitado** com transições **seamless**. Recurso **"elements"**: até 3 imagens de referência guiando look/pacing.
5. **Monte no editor** (CapCut/Premiere): som, transições, ritmo, texto. **Escreva o roteiro ANTES dos prompts** — trate o Veo como sua equipe de filmagem virtual (ou use o **Google Flow** pra storyboard/pipeline).

## 3 frameworks de prompt "de diretor"
- **Hero shot** (TikTok/trailer/reveal): personagem + ação ousada + movimento lento de câmera + luz emocional + fala-assinatura.
- **Scene sandwich** (história em 3 prompts): setup → momento-chave → beat emocional.
- **Style-first** (identidade visual forte): comece pela direção de estilo/câmera/mood, depois sujeito + ação.

## Fluxo de produção realista (qualidade de VSL/ad)
Para máximo realismo, **não use um tool só**:
1. **Imagem:** Midjourney com **mood board** (consistência de estética) + **omni-reference** (personagem consistente).
2. **Upscale da imagem:** Enhancer.ai (pele/textura realista, evita cara "cerosa") ou Gigapixel/Topaz (objetos).
3. **Animar:** **Veo 3** (melhor física + **lip-sync**; use quando o personagem precisa falar) **ou Seed Dance** (mais realista, **1080p nativo, até 12s, ~$0,60/geração** vs ~$2,50 do Veo). Cling é ok mas distorce rostos; Runway/Luma/Minimax perdem realismo.
4. **Upscale do vídeo:** Topaz Video AI (modelo Proteus, 4K; `recover detail` em 0 pra não criar artefato).
5. **Grão de filme** no editor (overlay ~30%) pra dar textura de câmera real.

## Acesso, custo e armadilhas
- **flow.google** dá acesso ao Veo. **Gemini AI Pro** costuma ter **1 mês grátis** + créditos. **OpenArt** = acesso rápido aos modelos novos, tudo num lugar (imagem+áudio+vídeo).
- **V3 Fast** (~20 créditos, 720p): barato, mas movimentos piores **e o fast text-to-video NÃO gera diálogo**. **V3 Quality** ("beta audio") pros shots importantes.
- **Upscale 720→1080p é grátis** com assinatura; pra 4K, upscaler externo.
- **Legendas queimadas:** bug comum do Veo; "no subtitles" nem sempre funciona → **cortar/dar zoom** no editor ou usar removedor de legenda por IA.
- **Vertical (shorts):** não há opção nativa; **truque** = rotacionar a imagem de referência 90°, gerar, e rotacionar o vídeo de volta.

## Conexões
- [Anatomia do Hook](../hooks/anatomia-do-hook.md) — o criativo entrega o **key visual** e o scroll-stop
- [Como Escrever o Hook](../hooks/como-escrever-o-hook.md) — o hook falado/visual/texto que vai no vídeo
- [Anatomia da VSL de Suplemento Masculino](../swipes/vsl-suplemento-masculino.md) — o cold-open dramático é candidato nº1 a virar criativo Veo
- [Baixar qualquer VSL](baixar-qualquer-vsl.md) — minerar criativos de concorrentes pra modelar
