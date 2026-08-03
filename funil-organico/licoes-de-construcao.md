# 🧱 LIÇÕES DE CONSTRUÇÃO — os erros do assistente, e o que os impede

> Irmão do [`licoes-producao-veo.md`](licoes-producao-veo.md). Lá moram as
> lições pagas **com render recusado**; aqui as pagas **com trabalho errado
> entregue como certo**.
>
> ⚠️ **Este arquivo existe por ordem do operador (2026-08-02):** *"documente
> todos os seus erros em um md pertinente… erros viciosos hão de ser
> documentados a fim de evitá-los no futuro."*
>
> Ele é escrito na primeira pessoa de propósito. Não é lista de bugs do repo —
> é a lista dos **modos de falha do assistente**, e ela deve ser lida antes de
> construir ou alterar agente.

---

## A CAUSA RAIZ, e ela é uma só

Quase tudo aqui é o mesmo erro em roupas diferentes:

> **Eu verifico a FORMA e declaro pronto sem verificar a FUNÇÃO.**

O linter conferia placeholder presente, token banido ausente, teto de palavras,
cota do órgão — e passava. O que ele nunca conferia é se **o slot cumpre o
trabalho pelo qual existe**. Copy que passa no linter e não faz o trabalho é
**pior** que copy que quebra: quebra eu vejo; essa some no lote.

O corolário operacional, e ele vale para tudo abaixo:

> **Aceite é MEDIÇÃO, nunca RELATO.** Nem meu, nem de subagente.

---

## 1. ⛔ ENTREGAR COMO PRONTO O QUE NUNCA FOI EXECUTADO

**O caso (TROCA, 2026-08-01).** O motor chegou com relatório dizendo *"0 ERRO,
comandos passaram"* e **quebrava em 100% dos sorteios**. Quatro defeitos:

| Defeito | Como aparecia |
|---|---|
| `%` com argumento faltando | `TypeError: not enough arguments for format string` |
| dois nomes indefinidos (`TR8_NUMERO`, `_bolso`) | `NameError`, só na linha que executa |
| dois linters comparando com o **template cru** | 400 de 400 reprovados, com mensagem plausível |

**O que impede:**

1. `python -m pyflakes <motor>.py` — acha **todos** os nomes indefinidos de uma
   vez. Caçar de rodada em rodada custa uma execução por bug.
2. **400 sorteios pelas 5 páginas**, `sortear → montar → lint`, ledger em
   memória, **0 ERRO medido**. `--n 2 --dry-run` **não serve**: os defeitos
   deste motor só apareciam em parte dos sorteios.
3. Relatório de subagente é **hipótese**, não evidência. Reconferir sempre.

---

## 2. ⛔ LINTER QUE COMPARA COM CONSTANTE QUE TEM SLOT

`TR_X not in bloco` dá **100% de falso positivo** quando `TR_X` chega
formatada. Compara-se com o **miolo invariante** — o trecho entre os `%s`, que
sobrevive a qualquer preenchimento.

> ⚠️ **Se um linter reprova 100%, a suspeita é DELE, não da cena.** Regra que
> reprova tudo nunca foi testada.

**O caso irmão, e é pior:** o TR7 do TROCA exigia a bancada-recibo no
`IMAGE 03/03` enquanto o comentário do `montar()`, **três funções acima**,
dizia que ela é omitida ali de propósito por F12c. O código contradizia a si
mesmo e ninguém tinha rodado.

---

## 3. ⛔ REGRA CITADA EM CÓDIGO QUE NÃO EXISTE NA DOUTRINA

O motor do TROCA citava `TR15`-`TR21`. A doutrina ia até `TR14`. Toda mensagem
de erro mandava o operador **ler a regra errada**, e não havia como auditar
cobertura.

**O que impede** — conferência barata, roda em um segundo:

```bash
for n in $(seq 1 30); do
  m=$(grep -c "TR$n\b" motor.py); d=$(grep -c "TR$n\b" doutrina.md)
  [ "$m" -gt 0 ] && [ "$d" -eq 0 ] && echo "TR$n ÓRFÃ"
done
```

Regra que o motor descobre ao virar código **volta para o `.md`** (P9).

---

## 4. ⛔ O SLOT QUE NÃO CUMPRE A FUNÇÃO — o vício mais caro

Quatro ocorrências em dois dias, todas passando no linter:

| Slot | Existia para | Entregava | Peso medido |
|---|---|---|---|
| cena 3 do TROCA | dar **prova** | preço e prateleira de mercado | 100% dos vídeos |
| fundidas do FLAGRANTE | dar o **mecanismo** | `blood flow` **sem destino** | 23,8% |
| CTAs (7 motores) | fazer **comentar** | pedia sem dizer o que chega | **18%** |
| TAKEs (6 motores) | gerar vídeo **limpo** | nada sobre texto queimado | 0 de 18 tinham |

**O método que impede:** ao criar ou revisar pool, **escrever antes o que aquele
slot tem de entregar** e checar entrada por entrada contra isso. *"É a prova"* →
diz **o quê** mudou? *"É o CTA"* → diz **o que a pessoa recebe**? *"É o
mecanismo"* → diz **para onde**?

⭐ **Quando a função for verificável por regex, ela vira LINTER, não
comentário.** Já viraram:

| Guarda | Onde | Cobre |
|---|---|---|
| `lint_isca_cta` | `short_comum.py` | CTA que pede sem oferecer |
| `lint_sem_texto` / `SEM_TEXTO_TAKE` | `short_comum.py` | texto queimado no TAKE |

Ambos rodam dentro do `lint_curto`, então valem para **todo agente SHORT,
inclusive os que ainda vão nascer** — que foi a ordem explícita do operador.

---

## 5. ⛔ TETO CONSERVADOR VIRA ESPAÇO MORTO, E ESPAÇO MORTO VIRA ENCHIMENTO

**O caso (ESCANDALO, 2026-08-02).** Teto da cena 1 = 22 palavras. Capacidade
real de 8 segundos na nossa taxa de fala (3,4-4,0 p/s) = **27-32**. As falas
mediam **18,4**. O slot que sobrava virou enchimento — *"Give me eight
seconds"*, *"Stay with me here"*, *"Eight seconds. That's all."*

**O que impede:** medir `palavras_medidas / capacidade_real`, não só *"cabe no
teto"*. Teto folgado não é segurança: é frase morta esperando para nascer.

---

## 6. ⛔ ANUNCIAR PROBLEMA QUE NÃO EXISTE — o erro que custa confiança

**O caso.** Meu medidor de entropia chaveava os personagens por `idade` +
`marca`. Os pools de mulheres do VAZAMENTO e do PEE descrevem a pessoa em
`desc`/`payoff` — então **8 mulheres distintas colapsavam em 5 idades** e eu
reportei ao operador um vício que não existia.

**O que impede:** a chave de contagem tem de ser **o objeto inteiro**, nunca um
subconjunto de campos escolhido a olho. E antes de reportar um problema,
confirmar que o instrumento não é o problema.

---

## 7. ⛔ GREP INCOMPLETO E DECLARAÇÃO DE SUCESSO EM CIMA DELE

Testei as 5 páginas filtrando `TypeError|AttributeError|KeyError|IndexError|
ValueError` — e **esqueci `NameError`**. Declarei *"rodou"* para as cinco
enquanto todas falhavam.

**O que impede:** testar por **código de saída**, não por lista de exceções que
eu me lembrei de escrever. Lista de padrões é sempre incompleta.

---

## 8. ⛔ CONCLUIR DA ASSINATURA EM VEZ DE MEDIR

Li `sortear(pagina, rng, ledger, degrau=None, ...)` e anunciei ao operador que
o default **não** respeitava a decisão dele. Respeitava — o `None` resolvia
para `1` lá dentro, e **100% dos sorteios** caíam no degrau escolhido.

**O que impede:** rodar antes de concluir. Uma linha de medição custa segundos e
evita uma correção pública errada.

---

## 9. ⛔ CHUTAR CREDENCIAL LIDA DE PRINT

Li `jm7UGric` de um screenshot. Era `jm7UGrlc` — `I` maiúsculo e `l` minúsculo
são indistinguíveis na fonte do print, assim como `O` e `0`.

**O que impede:** **pedir em texto**, sempre. E ⛔ **nunca** tentar variações:
isso é chutar senha contra um serviço, e um bloqueio por tentativa queima o
proxy do operador.

---

## 10. ⛔ DIAGNÓSTICO QUE PARECE OUTRA COISA — a tabela de sintomas do garimpo

Três desvios que custaram tempo por parecerem o que não eram:

| Sintoma | Parecia | Era |
|---|---|---|
| `Cannot parse data` no yt-dlp | extractor defasado | **cookie de FB é atado ao IP** — faltava o `--proxy` da sessão |
| `502` no proxy, `200` no Facebook | proxy quebrado | proxy **IPv6-only**; o alvo de teste não tinha AAAA |
| `403` do Whisper | chave inválida | WAF barrando o `User-Agent` do `urllib`; via `curl` passa |

Detalhe completo em [`../PIPELINE-NOVO-AGENTE.md`](../PIPELINE-NOVO-AGENTE.md)
§[2], rota 2c.

---

## 11. ⛔ QUEBRAR REGRA VALIDADA AO CONSERTAR OUTRA COISA

Ao pôr a isca nos CTAs, escrevi `Comment gelatin and I'll send` — **sem a
vírgula** depois da keyword. Existe regra validada de que, sem essa micro-pausa,
o Veo narra *"gelatine"* e a automação de DM não casa.

**O que impede:** rodar o linter **depois de cada correção**, não só no fim.
Aqui ele pegou — e é exatamente para isso que ele existe.

---

## 12. ⛔ REPASSAR RELATÓRIO DE SUBAGENTE SEM CONFERIR O ESTADO ATUAL

O relatório final do build do TROCA descrevia o motor com **1.086 linhas**;
o arquivo em disco tinha **2.026**, porque agentes posteriores o reescreveram.
Ele também afirmava decisões (mão direita, âncora de bolso, a nora no pool) que
outros agentes **já haviam revertido**.

**O que impede:** relatório de workflow é foto de um instante, não do estado
final. **Conferir o disco** antes de repassar qualquer afirmação ao operador.

---

## 13. ⛔ NÃO VERIFICAR SE A ETAPA FINAL RODOU

Dei o registro do TROCA como feito. `WORKFLOW.md`, `CLAUDE.md` e o
`PIPELINE-NOVO-AGENTE.md` estavam **intocados** — a fase nunca completou.

**O que impede:** `git status` e `git diff --stat` nos arquivos que a etapa
deveria ter tocado. Mtime antigo = não rodou.

---

## 14. ⛔ SINTAXE DE SCRIPT DE WORKFLOW (duas vezes)

Quebrei o script duas vezes por caractere dentro de string:

- **apóstrofe** em `e' justamente` dentro de string de aspas simples;
- **backtick** de `\`comment book\`` dentro de template literal.

**O que impede:** em prompt de workflow, escrever sem apóstrofe e sem backtick —
usar aspas duplas para citar termo técnico.

---

## 15. ⛔ MEDIR A DIMENSÃO ERRADA — pool cheio, repertório vazio

O operador: *"seu repertório de personagens está fraquíssimo em boa parte dos
agentes"*. Eu já tinha medido esses pools e passado: 8, 9, 14 entradas, todas
distintas, nenhuma concentração acima do teto. **O número estava certo e a
conclusão errada** — eu contei *quantas entradas existem* quando o que importa
é *quantos eixos físicos as entradas acionam*.

Medido depois: os REFS do VAZAMENTO tinham **cabelo em 100%** das entradas e
**óculos em 0%, pelo facial em 0%, pele em 22%**. Nove homens descritos só pelo
cabelo são o mesmo homem nove vezes — e o gerador devolve o mesmo rosto, que
foi exatamente a queixa. No repo inteiro: **19 eixos zerados e 24 magros**.

**A forma do erro é a de sempre**, só que na métrica: contar é verificar a
FORMA do pool; perguntar se as pessoas parecem diferentes é verificar a FUNÇÃO.

**O que impede:** [`medir_personagens.py`](medir_personagens.py) — lê os motores
como árvore (`ast`, sem importar) e reporta cobertura por eixo: cabelo, pelo
facial, óculos, porte, pele, âncora facial. `--gate` sai 1 se algum eixo estiver
zerado. Entrada nova de personagem difere das outras em **≥ 3 eixos**.

## 16. ⛔ E O MEDIDOR TAMBÉM MENTE — 22 dos 41 achados eram falso positivo

A primeira versão do `medir_personagens.py` acusou **41 eixos zerados**. Vinte e
dois não existiam:

- `FIGURANTES` do ESCANDALO é `(1, 2)` — a **contagem** de figurantes. Meu regex
  casou o nome e nunca olhou o conteúdo;
- cobrei **pelo facial em pool de mulher** — barba de mulher;
- o PRISMA **decompõe** o REF em `REF_IDADES × REF_FISICOS × REF_MARCAS`, que se
  combinam no sorteio: cada parte é magra por construção, o **produto** é que
  precisa cobrir.

Se eu tivesse relatado os 41, teria mandado o operador consertar o que estava
certo — a §6 de novo, agora vestida de ferramenta.

**O que impede:** a §2 vale para o medidor igual vale para o motor. Antes de
reportar achado de linter novo, **abrir os 3 primeiros e conferir na mão**. E o
próprio medidor carrega no cabeçalho a lista do que já o fez mentir.

### As três formas do erro, todas cometidas no mesmo dia (2026-08-02)

No aceite do RESSURREICAO o instrumento errou **três vezes**, e as três quase
viraram defeito relatado ao operador:

| Forma | O que aconteceu | Como se detecta |
|---|---|---|
| **Sonda velha** | a sonda da R7 procurava `silent\|pause` e marcou **0/400** depois que a correção trocou a formulação (o apagão virou 0,8s ancorado no morph, com literal novo). Zero súbito em regra que estava em 400/400 **não é regra sumida** | um zero que apareceu **de repente** é suspeita contra a sonda, não contra o motor |
| **Regra larga demais** | a lente cobrava `your {o}` **sozinho** e acusou 175/400 — mas a doutrina **permite** condicional e pergunta; só a soma com prazo é proibida. Cobrar isso é cobrar o hook inteiro do agente | reler a regra **na doutrina** antes de codificar a lente, e codificar a **composição**, não o token |
| **Escopo errado** | a mesma lente varria os 3 takes **juntos**, e a regra é "no mesmo take de 8s": hook da cena 1 + prazo da cena 2 são 16 segundos de distância | a unidade da regra (vídeo? take? bloco? fala?) entra na lente **explicitamente** |
| **Escopo largo demais** (2026-08-03) | ao medir a frase órfã, contei `his {o}` como vício e acusei **400 em 200 vídeos** no FLAGRANTE. Falso: naquele ângulo a narradora conta a história de **um terceiro** e o espectador se identifica — `his old boy went soft` é o *formato*, não o defeito | antes de codificar, perguntar **de que ângulo é a regra**: o que vale no RESSURREICAO pode ser a espinha do FLAGRANTE |
| **Escopo estreito demais** (2026-08-03) | corrigi para medir por **cena** ("o órgão aparece em algum lugar?") — e o medidor **aprovou exatamente a cena que o operador tinha reprovado**, porque `his old boy` estava na última frase. A queixa era de **frase** | quando um medidor aprova o caso que motivou sua existência, ele está medindo outra coisa. **O caso reprovado vira controle** |

E o mesmo dia deu o caso simétrico, que é pior: o **`_rs10_prazo` existia desde
o primeiro dia do motor e nunca acusou uma vez** — o regex listava
`days|weeks|months` e não `seconds`. **Regra escrita não é regra que pega.**

**O que impede:** toda lente nova nasce com **controle positivo e negativo** —
frases que *têm* de casar e frases que *não podem* — e eles rodam **antes** de
qualquer número ser olhado. É o que o `medir_personagens.py --autoteste` faz.
E `0 ERRO` num lote grande é **suspeita**, não aprovação: sabotar de propósito é
a única forma de distinguir motor limpo de linter morto.

---

## 17. ⛔ TROCAR UMA ABSTRAÇÃO POR OUTRA E CHAMAR DE CONSERTO

O operador reprovou a cena 1 do RESSURREICAO três vezes seguidas, no mesmo slot,
em dois dias. Meus dois primeiros "consertos" **não eram consertos**:

| | o que a cena dizia | meu diagnóstico | por que ainda estava errado |
|---|---|---|---|
| original | `You just watched the mechanism work.` | meta-fala: declara que houve um mecanismo em vez de dizer qual | — |
| conserto 1 | `Outside it's visible. Inside it's the same blood.` | "agora tem substantivo concreto" | **fisiologia ainda é conversa.** O espectador não quer saber de sangue, quer saber do pinto dele |
| conserto 2 *(dele)* | `That's baking soda, and that's your Johnson on it. Her hand lands on it and she freezes.` | — | funciona porque nomeia **o que ele reconhece em si** e **o que ela sente** |

E a mesma coisa na cena 2: `It isn't age.` — idade causando **o quê**? Eu tinha
medido aquele pool e aprovado, porque `blood flow` e `vasodilators` **contam
como concretos** num detector de substantivo.

**A lição:** *concretude não é vocabulário técnico.* `nitric oxide` é mais
técnico e menos concreto que `she freezes`. O teste não é "tem substantivo?" —
é **"o espectador reconhece isso em si mesmo?"**. Fisiologia é o mecanismo do
produto; o espectador compra o **resultado no corpo dele e a reação de alguém**.

**Como se detecta antes de o operador ver:** ler a fala inteira renderizada em
voz alta e perguntar *"do que ela está falando?"*. Se a resposta precisa de
contexto que o vídeo não deu, é órfã. Vale como item de checklist e virou
medidor: [`medir_contexto_copy.py`](medir_contexto_copy.py), que cobra o alvo
**na mesma frase** da causa.

⚠️ **E o corolário caro:** eu "consertei" duas vezes e nas duas declarei
resolvido com número (`400/400 nomeiam a substância`). O número estava certo e
não media o que o operador estava reclamando — §15 de novo, agora em copy.

---

## O CHECKLIST, para colar antes de entregar agente ou alteração de motor

- [ ] `python -m pyflakes <motor>.py` — saída **vazia**
- [ ] **400 sorteios** pelas 5 páginas, `sortear → montar → lint`, **0 ERRO medido**
- [ ] Nenhum eixo acima de **~17%** de concentração; mínimo **9 opções** por eixo
- [ ] `python funil-organico/medir_personagens.py --gate` — **exit 0**, nenhum eixo
      físico zerado. Contar entradas não basta: dez homens descritos só por cabelo
      são o mesmo homem dez vezes, e o gerador devolve o mesmo rosto (§15)
- [ ] Numeração de regra **bate caractere por caractere** entre motor e doutrina
- [ ] Cada slot de copy **cumpre a função** pela qual existe (§4) — e se dá para
      checar por regex, **virou linter**
- [ ] **Sabotei o linter e ele acusou** — `0 ERRO` num lote grande é suspeita, não
      aprovação: pode ser motor limpo ou regra morta (§16). Uma sabotagem por
      regra travada, e a sabotagem tem que **chegar** onde a regra olha
- [ ] Toda lente/medição nova tem **controle positivo e negativo**, rodados
      antes de eu olhar o número (§16) — e **o caso que o operador reprovou
      entra como controle**, senão o medidor aprova justamente ele
- [ ] `python funil-organico/medir_contexto_copy.py --gate` — **exit 0**. Toda
      frase que nomeia uma causa diz, **na mesma frase**, o que ela quebra (§17)
- [ ] **Li a fala inteira em voz alta e perguntei "do que ela está falando?"**
      Se precisa de contexto que o vídeo não deu, é órfã (§17)
- [ ] Uso do orçamento medido contra a **capacidade real**, não contra o teto (§5)
- [ ] **Li algumas falas inteiras renderizadas**, não só os pools
- [ ] `git diff` conferido: nenhuma string validada redigitada sem ordem
- [ ] `.exe` **recompilado** — sem isso a correção não chega no operador
- [ ] Se houve subagente: **estado do disco conferido**, não o relatório dele

---

## Conexões

- [`licoes-producao-veo.md`](licoes-producao-veo.md) — as lições pagas com render recusado
- [`../PIPELINE-NOVO-AGENTE.md`](../PIPELINE-NOVO-AGENTE.md) — o pipeline, com o §[9] "aceite é medição"
- [`RUNBOOK-app-offline.md`](RUNBOOK-app-offline.md) — motor → app → `.exe`, e por que recompilar
- [`../CLAUDE.md`](../CLAUDE.md) — a alçada: copy e cena são do operador
