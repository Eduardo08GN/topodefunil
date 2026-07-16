# Veo 3 — pipeline avançado (hiperrealismo, consistência, multi-câmera)

- **Fonte:** síntese de 2 tutoriais avançados (documentário macro com IA + pipeline de hiperrealismo indistinguível de real)
- **Serve para:** subir de "vídeo IA bonito" pra **produção hiperrealista com personagem/produto consistente** — o que permite uma **série de ads** da mesma "atriz"/produto
- **Status:** ✅ consolidado
- **Base:** [Veo 3 — produzir os criativos](veo3-criativos.md) (leia primeiro)

> **A regra do realismo:** não use **um** tool só. Cada etapa (imagem → consistência → upscale → animar → lip-sync → edição) tem a ferramenta que faz melhor. E **90% do sucesso é preparação** (juntar referências antes de "filmar").

## Caso de uso: documentário / macro (transformações)
Padrão de 4 passos: **definir → prompt → gerar imagem → gerar vídeo da imagem.**
- Fórmula de prompt de imagem: **"extreme macro photograph" + inseto/sujeito + ação + detalhes** ("nitidez, luz suave filtrada, foco no olho, bokeh, realismo cinematográfico").
- Gere **4 imagens** por prompt (mais opções). Depois use a melhor **como referência** pra dar zoom sem perder qualidade (olho, perna...) → vários ângulos do **mesmo** sujeito → permite **cortes rápidos** no editor.
- **Transições com start/end frame:** decaimento (libélula viva → exoesqueleto), metamorfose (larva → lagarta → casulo → borboleta). Dica: prompt com **"câmera fixa"** ou **"hyperlapse"** conforme o efeito. Gere 2–3× e escolha a melhor.

## Consistência (o pilar do realismo)
### Nano Banana (Google AI Studio)
- **Adicionar elementos mantendo o rosto** (envie foto + óculos → "add sunglasses"); gerar **novos ângulos** ("extreme close-up", "medium close-up over the shoulder") sem perder consistência.
- Dica: a **última imagem enviada define o aspect ratio** do resultado. E **abra um chat novo por tarefa** — quando começa a dar resultado estranho, o contexto acumulado é a causa.

### Midjourney (mood board + omni reference)
- **Mood board** = estética consistente (arraste imagens de referência → "use in prompt"). **Omni reference** (força 100–250) = **seu rosto/personagem** repetível. Dá pra **animar** direto no Midjourney (feel "handheld/iPhone").

### Face-swap profissional (o nível "high-end")
Melhor que apps de face-swap: **treinar um "subject"/LoRA**.
1. No Midjourney, gere **variações do rosto** (corrija pintas/imperfeições no Photoshop com generative fill; remova fundo → fundo branco).
2. Treine o subject no **Krea.ai** (3–50 imagens, só rosto/fundo branco).
3. **Inpaint** com modelo **Flux**: marque a área do rosto → aplique o subject treinado.
4. **Por que > face-swap tools:** (a) menos **restrições/filtros**, (b) **consistência** real, (c) **sem downgrade** de qualidade (mantém a resolução original). Entre apps, **RP face swap > Remaker**.

### ChatGPT = melhor pra rosto/pose fotorrealista
- Gera **retratos** que "parecem reais" (o "molho" que Nano Banana/Midjourney não têm — estes ainda pedem limpeza). Truque: gerar **close do rosto a partir de um full body** sai mais fotorrealista.
- Excelente em **replicar poses**.
- **Hack pra driblar filtro:** transforme a imagem em **desenho estilo infantil** → faça a modificação (pose/roupa) → converta **de volta pra foto realista** (em chat novo, sem contexto).

## Upscale / realismo de imagem
**Enhancor.ai** (conserta pele/textura, tira cara "cerosa") → **Magnific** (precision; detail 30–50%, grain 20–30, sharpen 5–10) pro acabamento hiperrealista. Baixe em PNG 100%.

## Animar (imagem → vídeo)
- **Cling 2.1 frames** — start + end frame; **"flip"** (end vira start) + nova imagem = **shot contínuo/infinito sem cortes**. Boa aderência ao prompt.
- **Seedance** (Fal.ai) — **melhor coerência de prompt**, **12s**, e o recurso-chave: **multi-câmera via "shot switch"** — escreva `shot switch` onde quiser mudar de plano; ele entrega vários ângulos num clipe (na prática ~**6 shots** com **transições suaves**, não cortes duros). Só image-to-video por ora.

## Lip-sync em vídeo existente + voz
- **Runway** — adicione fala a um vídeo sem lip-sync usando uma **"driving performance"**: seu rosto falando (gerado no Veo) **ou** uma gravação sua no **celular** (pra emoção custom).
- **ElevenLabs voice changer** — troque a voz pela **sua voz treinada** ou uma da comunidade.

## Prompt de vídeo: JSON generator
Custom GPT **"V3 JSON prompt generator"**: envie a imagem → "turn a prompt from image" → responda as perguntas (ex.: "a mulher faz rap, muitos cortes de câmera") → ele monta o JSON com **camera switches**. Cole no Veo (fast mode serve). ~5 gerações já dão material pra editar.

## Pré-produção = 90% (blocos de referência)
Junte **antes** de gerar: **atores** · **figurino** (óculos, sapatos, acessórios) · **poses** (quanto mais inusitada, mais autêntica — casa com Cling frames) · **maquiagem/rosto** · **cabelo** · **ambiente** · **iluminação** (mood boards) · **props**. Tudo aplicável com Nano Banana.

## Edição final
**DaVinci Resolve** (grátis; ou Premiere/After Effects) — só **combinar clipes**, já que os cortes de câmera vieram do Veo/Seedance. Adicione **color correction** + **film grain** (sempre dá aquela textura de câmera real).

## Conexões
- [Veo 3 — produzir os criativos](veo3-criativos.md) — o básico do prompt e da produção
- [Anatomia do Hook](../hooks/anatomia-do-hook.md) — personagem consistente = a "atriz" do seu hook recorrente
- [Anatomia da VSL](../swipes/vsl-suplemento-masculino.md) — cenas dramáticas (casal, humilhação) viram criativos com atores consistentes
