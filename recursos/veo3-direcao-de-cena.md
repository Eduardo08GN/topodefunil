# 🎬 Direção de Cena Veo 3 — o padrão de GUERRA (anti-amador)

O [doc base](veo3-criativos.md) ensina a **operar** o Veo. Este ensina a **dirigir cena que converte** — a diferença entre prompt de turista ("mulher bonita segura produto e sorri") e prompt de diretor de guerra. **Todo prompt de criativo do funil passa por este padrão.** Prompt que descreve cena morna gera cena morna com qualidade de cinema — continua morno, só que caro.

- **Status:** ✅ LEI de produção (executa o ângulo escolhido na [matriz geradora](../funil-organico/guerra-reptiliana-angulos.md) sob a [Doutrina](../funil-organico/doutrina-criativa-agressiva.md))
- **Guardrails que continuam valendo:** [anti-irrealidade](generated-ai-video-anti-irrealidade-checklist.md) (com exceção fálica) · zero texto gerado · linguagem indireta no áudio.

## 1. Engenharia do 1º FRAME (o frame é o outdoor)

O Facebook decide a impressão no **frame 1 congelado** — antes do play, antes do som. O frame 1 não é "o começo do vídeo": é um **outdoor** que precisa vender o play sozinho.

- **Comece IN MEDIA RES:** a cena JÁ em movimento/conflito no frame 1. O espectador chega "atrasado" (FOMO instantâneo).
  - ❌ `she walks into the kitchen and picks up a banana` (3s de nada)
  - ✅ `opens mid-action: her jaw is ALREADY dropping, hand flying to her mouth, mid-gasp`
- **PROIBIDO no frame 1:** fade-in · establishing shot (fachada, paisagem) · pessoa parada olhando pra câmera esperando pra falar · logo/vinheta · qualquer "preparação".
- **No prompt, descreva o frame 1 explicitamente:** comece a `action` com `opens mid-action:` e descreva o instante congelado como se fosse um pôster.

## 2. Arquétipos de SHOT 1 (escolha um — nunca "talking head")

| Arquétipo | O que é | Quando usar |
|---|---|---|
| **Reaction-shot** | rosto humano em emoção EXTREMA (gasp, choque, inveja, fome) — nunca mostrar a causa | curiosity gap máximo; o mais compliant e barato |
| **Prop-choque macro** | o prop fálico/demo em estado absurdo, em close, JÁ acontecendo (banana desabando/levantando) | quando o mecanismo é o hook |
| **Micro-drama com elenco** | 2-3 personagens, UMA ação, UMA emoção (a ex congelando; o garfo parado no ar) | cenas-evento do [banco](../funil-organico/empilhamento-reptiliano.md) |
| **Flagrante** | estética de câmera que "não devia estar filmando" (security-cam, janela, celular escondido) | família I; autenticidade máxima |
| **POV** | as mãos/olhos do espectador dentro da cena | família G; imersão |
| **Contraste split** | dois estados lado a lado no MESMO quadro (murcho×firme, 53×53) | diagnóstico/antes-depois |

## 3. Direção EMOCIONAL (o que o Veo faz bem e ninguém pede)

Amador pede emoção genérica; diretor nomeia **micro-expressão + ação física**:
- ❌ `she looks surprised` / `he is sad`
- ✅ `her eyes go wide, she freezes mid-step, shopping bag slipping from her fingers, jaw slack — shock curdling into envy`
- ✅ `he lies staring at the ceiling in the dark, jaw tight, while her back is turned — the silence is louder than a fight`
- ✅ `slow smirk spreading, one eyebrow up — the look of a man who knows something the whole gym doesn't`
- **Blocking = história:** quem se aproxima domina; quem congela perdeu; quem vira as costas fere. Escreva o movimento dos corpos, não só "estão na cozinha".
- **Tensão em detalhe físico:** `knuckles white on the steering wheel` · `her fingers gripping the sheets` · `the fork stops halfway to his mouth`.

## 4. SOM como gancho (o segundo hook)

O primeiro SOM é um segundo pattern interrupt (metade assiste com som):
- **Abrir com som-choque:** gasp audível · porta batendo · vidro/talher caindo · risada estourada · sussurro colado no ouvido · **silêncio súbito** (corte de ambiente = para o dedo também).
- **Direção de entrega da fala** (o Veo obedece): `voice cracking with emotion` · `teasing whisper` · `mock disappointment` · `deadpan, then bursts out laughing` · `low conspiratorial tone, leaning in`.
- Fala SEMPRE atribuída por personagem + linguagem indireta ([regra de ouro](../funil-organico/signature-verbal.md)).

## 5. CÂMERA de guerra (um movimento por shot, com intenção)

- **Push-in rápido** no rosto = "isso importa AGORA" · **whip-pan** = revelação · **low-angle** no herói (poder) / **high-angle** no derrotado · **handheld tremido** = flagrante/urgência · **macro** = o prop é a estrela · **slow motion** = o corpo dela / o momento de glória.
- ❌ câmera parada em talking-head. ❌ dois movimentos no mesmo shot (confunde o modelo).

## 6. Templates JSON por arquétipo (preencher e disparar)

**Reaction-shot (o canivete suíço):**
```json
{
  "style": "cinematic UGC, 9:16 vertical, shallow DOF, intimate handheld",
  "scene": "[cenário doméstico específico + hora do dia]",
  "subject": "[Character Bible da personagem — IDÊNTICA entre shots]",
  "action": "opens mid-action: her eyes go wide mid-gasp, hand flying to her mouth, frozen in place — shock melting into a slow delighted smile. NEVER show what she sees.",
  "camera": "tight close-up on her face, fast push-in on the gasp",
  "lighting": "[luz motivada: janela/manhã/abajur]",
  "audio": "her audible gasp: 'oh my god—', then stunned silence, room tone",
  "negative": "on-screen text, labels, showing the cause, extra people, warped face, deformed hands, plastic skin"
}
```

**Micro-drama com elenco (cenas-evento):**
```json
{
  "style": "cinematic, 9:16 vertical, documentary handheld",
  "scene": "[local público específico: calçada de restaurante, churrasco no quintal]",
  "subject": "[personagem A + B + testemunha — 1 linha de Bible cada]",
  "action": "opens mid-action: [o casal em prova de posse — arm in arm, laughing]; [a testemunha] freezes mid-step, jaw slack, eyes locked on them — envy hardening on her face. [O herói] glances at her, smirks, and keeps walking.",
  "camera": "medium tracking shot, then whip-pan to the witness's face",
  "audio": "street ambience; his low chuckle; her sharp inhale",
  "negative": "on-screen text, labels, gibberish, deformed hands/faces, extra background people morphing"
}
```

**Prop-choque macro (demo/fálico):**
```json
{
  "style": "macro product cinematography, 9:16 vertical, crisp",
  "scene": "[bancada/mesa, luz forte e limpa]",
  "subject": "[o prop em estado inicial absurdo — limp banana flopped over the edge]",
  "action": "opens mid-action: two drops fall onto it; the banana stiffens and rises upright in one smooth motion. Clean, deliberate, comic timing.",
  "camera": "locked-off macro, slight slow push-in",
  "audio": "two audible drips, then a subtle 'pop'; kitchen room tone",
  "negative": "on-screen text, labels, morphing artifacts, melting shapes — EXCEPTION: the exaggerated banana behavior is intentional, keep it clean and well-lit"
}
```

**POV (família G):**
```json
{
  "style": "first-person POV, 9:16 vertical, natural handheld sway",
  "scene": "[da porta de casa ao corredor — o trajeto DELE]",
  "subject": "viewer's own hands/body visible at frame edges; [ela] ahead",
  "action": "opens mid-action: your hand pushes the front door open — she's already looking at you from the kitchen doorway, biting her lip, robe slipping off one shoulder, and she starts walking toward you",
  "camera": "POV, slow steady approach, her eyes locked on lens",
  "audio": "door click, her voice, teasing: 'you're late.', heels on the floor",
  "negative": "on-screen text, showing the viewer's face, warped hands, extra people"
}
```

## 7. Protocolo de iteração (generate & escolher o mais brutal)

1. **2–4 takes por shot** (fast pra explorar, quality pro aprovado).
2. **Critério de escolha:** o take mais EXTREMO que continua crível — não o "mais bonito". Emoção tímida = repromptar com micro-expressão mais forte, não aceitar.
3. **QA:** [checklist anti-irrealidade](generated-ai-video-anti-irrealidade-checklist.md) + Teste do Dedo no frame 1 congelado (screenshot do frame 1 → pergunta: é um outdoor?).
4. Falhou → **refazer só o shot**, ajustando UMA variável (emoção, câmera OU luz).

## 8. Os 8 erros de amador (proibidos)

1. Abrir em talking-head com produto na mão.
2. `a beautiful woman smiling` — genérico gera genérico. Bible detalhada + emoção nomeada, sempre.
3. Estabelecer contexto antes do choque ("ela entra, pega, olha, e então…").
4. Emoção vaga (`happy`, `surprised`) em vez de micro-expressão + ação física.
5. Dois momentos num prompt só (o Veo é construtor de UM momento).
6. Cena sem conflito/tensão — se nada está errado ou em jogo no shot 1, não há hook.
7. Ignorar o som (o gasp/porta/silêncio é metade do pattern interrupt).
8. Aceitar o take "bonitinho" — bonitinho não trava dedo; escolha o brutal.

## Conexões
- [⚔️ Guerra Reptiliana (matriz de ângulos)](../funil-organico/guerra-reptiliana-angulos.md) — o QUE filmar; este doc é o COMO
- [⚡ Doutrina](../funil-organico/doutrina-criativa-agressiva.md) · [Empilhamento](../funil-organico/empilhamento-reptiliano.md) · [Template Criativo](../funil-organico/template-criativo.md)
- [Veo 3 base](veo3-criativos.md) · [Veo 3 avançado (consistência)](veo3-avancado.md) · [Anti-Irrealidade](generated-ai-video-anti-irrealidade-checklist.md)
- [SOP de Produção](../funil-organico/producao-criativo-sop.md) — onde este padrão entra (passos 5–6)
