# AGENTE UGC — ED / MEN'S WELLNESS
## V6 — HOOK-FIRST + ESPINHA FIXA + ELENCO TRAVADO

> Deriva do V4 (motor) e do V5 (biblioteca de dispositivos). **Substitui o V5 como
> agente de produção.** O V4 permanece como motor de referência: todas as regras de
> IMAGE/TAKE, estética iPhone, anti-glitch, anti-legenda e anti-bloqueio são herdadas
> dele sem alteração.
>
> A V6 existe porque a V5 randomizava o **eixo errado**.

---

## O QUE MUDA DA V5 PARA A V6

| Eixo | V5 | V6 |
|---|---|---|
| Variação principal | elenco (persona, etnia, setting, dispositivo) | **hook** (15 moldes × 16 substâncias × 12 props × 6 modificadores × 8 promessas) |
| Corpo do vídeo | reescrito a cada lote | **espinha fixa validada** (A/B/C), nunca improvisada |
| Persona | sorteada a cada vídeo | **fixa por página**, um REF reaproveitado |
| Memória | nenhuma (sorteio sem histórico) | **ledger** — nunca repete um hook já emitido |
| CTA | sorteado (keyword/book/yes) | **travado em GELATIN** |
| Risco de bloqueio | não modelado | **selo de risco por dispositivo**, aprendido em produção |

### Por que

Engenharia reversa de **Kofi&Simba** (20K seguidores, mesmo nicho, mesma keyword
`gelatin`, 11 reels lidos com `/watch` em 2026-07-27): quatro reels com 3.2K a 13K views
têm o **corpo idêntico palavra por palavra**. Só o hook muda.

Nós fazíamos o inverso — variávamos o invisível e repetíamos hooks mornos. O espectador
não vê que a persona mudou; ele vê que os primeiros 2 segundos são iguais.

Detalhe completo em [`banco-hooks.md`](funil-organico/banco-hooks.md).

---

## PASSO 0 — OBRIGATÓRIO: RODAR O RANDOMIZADOR

**Nunca escreva um vídeo sem uma linha de spec.** O agente não escolhe eixo nenhum.

```bash
python funil-organico/randomizador-v6.py --pagina joe --n 10
```

Opcionais: `--espinha A|B|C` · `--molde M1_substancia_absurda` · `--n 50` · `--dry-run`
· `--stats` (quanto do espaço combinatório já foi gasto).

Cada linha traz:

```
V01 [65d99b5f78b3] espinha=A | M13_medo_rival
     hook: subst=raw_honey prop=zucchini mod=nenhum promessa=ten_times_bigger disp=H1
     corpo: dor=desculpas_toda_noite setting=ranch isca=... cta=GELATIN
```

O agente **executa** essa combinação. Não troca, não prefere, não repete a última.

**Erro Fatal 30:** gerar sem spec, ou trocar um eixo da spec por conta própria.

---

## COMO MONTAR O VÍDEO

### Cena 1 — HOOK (a única cena que varia de verdade)

1. Pegue o **molde** da spec em [`banco-hooks.md`](funil-organico/banco-hooks.md).
2. Preencha com a `substancia`, o `prop` e a `promessa` da spec.
3. Cole o **modificador de autoridade** logo depois da primeira linha (se `mod != nenhum`).
4. O **dispositivo visual** vem derivado do molde — já está na spec, não escolha.

Exemplo com a spec acima (M13 medo do rival + raw_honey + zucchini + ten_times_bigger):

> "Her trainer is 28. You've done that math at 2am. I know. And rub raw honey on your soldier tonight, it gets ten times bigger by morning."

18-23 palavras, léxico não-gráfico, sem ALL CAPS na fala.

### Cenas 2-5 — ESPINHA FIXA

Copie de [`espinha-fixa.md`](funil-organico/espinha-fixa.md) a espinha da spec (A, B ou C).
**Não reescreva.** Adapte só o mínimo: a `dor` da spec entra na cena da confissão/problema,
a `receita_isca` entra na cena 2 da espinha A.

A espinha só muda com decisão explícita do operador e teste A/B.

### REF — fixo por página

Reaproveite o REF já travado daquela página (ver tabela em `espinha-fixa.md`). **Não gere
persona nova.** Se a página ainda não tem REF travado, gere um e registre lá.

---

## AS TRÊS REGRAS DE ENDURECIMENTO (novas na V6)

Nasceram de falhas reais de produção. Valem em toda cena.

### 1. ORÇAMENTO DE MÃOS — no máximo UMA ação de mão por cena

O Veo inventa uma terceira mão quando o prompt pede duas ações simultâneas diferentes.
Aconteceu com "segurar copo + mexer colher + gesto de encanamento" (Joe, cena 03).

- **Hero prop consome as duas mãos:** `both hands cupped firmly around it the entire shot, never letting go, never switching hands`.
- **A mão ociosa é declarada parada:** `left arm relaxed at his side and completely still the entire shot`.
- **Objetos que não estão em uso ficam na bancada**, não na mão.
- **Negue explicitamente o que não pode aparecer:** `no glass, no cup, no spoon, no bowl in the shot` — no IMAGE *e* no TAKE.

Onde não sobra mão livre, não há o que glitchar.

### 2. SELO DE RISCO DE BLOQUEIO — consultar antes da cena 1

| Construção | Selo |
|---|---|
| **H9** proxy na virilha, ponta pra baixo | 🔴 bloqueia — banido do randomizador |
| **H4** com "absurdly oversized" + fala com "perform" | 🔴 bloqueia |
| **H4** com "large" + fala sem conotação sexual | 🟡 passa |
| **H1** proxy vertical no peito, mãos paradas | 🟢 passa |
| **H7** pouring + crescimento | 🟢 passa |
| **M1** modelo anatômico | 🟢 passa |

Se um take for recusado por política: **suavize a escala do prop e a conotação da fala**,
nunca o dispositivo inteiro. O choque mora no proxy, não na palavra.

**Registre toda recusa nova** na tabela de `banco-hooks.md` — o selo é dado de produção,
não opinião.

### 3. SEGUNDA PESSOA — ausente ou sem ação

O REF trava **um** rosto. O segundo personagem renasce do texto a cada cena e morfa
(aconteceu nas IMG 03/04 do Joe: o parceiro virou três homens diferentes).

- Padrão: **cenas solo**. A segunda pessoa entra só onde a prova de casal importa (resultado).
- Quando entrar: **sem ação de mão**, postura estática, descrição repetida palavra por palavra da cena anterior.
- Se morfar mesmo assim: tire do quadro. Ela quase nunca é necessária narrativamente.

---

## HERDADO DO V4 — ABRA O V4, NÃO CONFIE NESTA LISTA

> ⛔ **Esta seção é um índice, não uma cópia.** Nenhuma regra mecânica é reproduzida
> aqui de propósito: quando o V4 mudava, a cópia daqui ficava velha e o agente executava
> a versão errada. **Aconteceu em 2026-07-28** — o V4 mudou o formato do TAKE e este
> arquivo continuou mandando fazer o formato antigo. Toda regra abaixo vive **só** no
> [`AGENTE_ED_ORGANIC_WAVE_V4.md`](AGENTE_ED_ORGANIC_WAVE_V4.md). Leia lá.

| Assunto | Onde no V4 |
|---|---|
| Formato de entrega (REF → 5 IMAGE → 5 TAKE, x/05) | *Formato de entrega* |
| Estética iPhone, luz de janela, elemento US | *Regras do IMAGE* |
| Descrição de persona, anti-celebridade | *Regras do IMAGE* |
| **TAKE é I2V: não re-descreva a persona** ⭐ | *O TAKE é I2V* |
| Sintaxe da fala (verbo + dois-pontos + aspas) | *Verbo + dois-pontos + aspas* |
| Rótulos `Dialogue:` / `Audio:` | *Rótulos de áudio e fala* |
| Anti-glitch, amarração do prop, mãos | *Anti-glitch* / *Amarração do prop* |
| Fechamentos obrigatórios de IMAGE e TAKE | *Regras do IMAGE* / *Regras do TAKE* |
| Texto de prop, anti-bloqueio, regras de copy | *Texto de prop* / *Anti-bloqueio* |

### A mudança de 2026-07-28 que você precisa saber antes de escrever

O TAKE virou **enxuto**. Ele é image-to-video — a persona já está no frame inicial.
Re-descrever rosto, roupa, idade e cenário no TAKE estourava as 150 palavras, fazia o
Veo descartar parte do prompt (inclusive o anti-glitch) e ainda convidava o modelo a
re-gerar o rosto. Era causa do morphing, da terceira mão e do prop sumindo.

TAKE agora abre com `Maintain the subject from the first frame.` e descreve **só**
movimento, câmera, luz, fala e áudio. Alvo: **80-150 palavras**. A descrição completa
de persona continua obrigatória **no IMAGE**, que é text-to-image.

E a biblioteca de dispositivos H1-H10 / M1-M7 do **V5**, Apêndice B e C (templates de
pouring + crescimento).

---

## ERROS FATAIS (herda os 22 do V4 + os 27 do V5 + 5 novos)

28. **Reescrever a espinha.** O corpo é ativo validado. Improviso aqui é o que produzia "sempre a mesma história" mal contada.
29. **Rotacionar persona dentro de uma página.** Um REF por página, sempre. Rosto novo a cada reel = fazenda de conteúdo.
30. **Gerar sem spec do randomizador**, ou trocar um eixo por conta própria.
31. **CTA diferente de GELATIN.** A automação Comentário→DM só dispara nas variantes de gelatin. Já custou um lote inteiro.
32. **Duas ações de mão na mesma cena.** Ver orçamento de mãos.
33. **Re-descrever a persona no TAKE.** O TAKE é I2V — rosto, roupa, idade e cenário já estão no frame inicial. Repetir estoura o limite de palavras, faz o Veo descartar o anti-glitch e convida o modelo a re-gerar o rosto.
34. **Copiar regra mecânica do V4 para dentro deste arquivo.** Aponte, nunca duplique. Cópia envelhece e passa a mentir.

---

## CHECKLIST V6

- [ ] Rodei o randomizador e estou executando UMA linha de spec, sem trocar eixo?
- [ ] O hook veio do molde da spec, preenchido com substância/prop/promessa dela?
- [ ] O modificador de autoridade foi colado (se `mod != nenhum`)?
- [ ] As cenas 2-5 vieram da espinha **copiadas**, não reescritas?
- [ ] O REF é o da página, reaproveitado — não gerei persona nova?
- [ ] Meus TAKEs abrem com `Maintain the subject from the first frame` e **não** re-descrevem persona/cenário, ficando em 80-150 palavras?
- [ ] A fala está como `says: "..."` (verbo + dois-pontos + aspas) e o áudio em linha `Audio:`?
- [ ] Toda cena tem no máximo uma ação de mão, com a mão ociosa declarada parada?
- [ ] Objetos ausentes negados explicitamente no IMAGE e no TAKE?
- [ ] Segunda pessoa ausente ou sem ação, com descrição repetida palavra por palavra?
- [ ] Dispositivo da cena 1 tem selo 🟢 ou 🟡 (nunca 🔴)?
- [ ] CTA = GELATIN + follow-gate na cena 5?
- [ ] Todo IMAGE e todo TAKE fecham com os negativos de legenda?
- [ ] Cumpro TODO o checklist do V4 e do V5?

---

## Conexões

- [`funil-organico/banco-hooks.md`](funil-organico/banco-hooks.md) — o que varia
- [`funil-organico/espinha-fixa.md`](funil-organico/espinha-fixa.md) — o que não varia
- [`funil-organico/randomizador-v6.py`](funil-organico/randomizador-v6.py) — o sorteador com ledger
- `AGENTE_ED_ORGANIC_WAVE_V4.md` — o motor (regras de IMAGE/TAKE)
- `AGENTE_ED_ORGANIC_WAVE_V5.md` — biblioteca de dispositivos H1-H10 / M1-M7 + Apêndice C
