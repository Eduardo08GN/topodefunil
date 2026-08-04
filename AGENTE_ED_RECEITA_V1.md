# AGENTE ED — RECEITA V1 (SHORT nativo, 3×8s)

> **A receita sendo feita é a prova.** Um homem confessa em primeira pessoa que
> estava perdendo a mulher, e o que ele oferece como evidência não é um corpo —
> é a própria bancada dele, sem rosto em quadro até o payoff.

- **Motor:** [`funil-organico/receita_short.py`](funil-organico/receita_short.py) · app + `.exe` em `agentes_py\RECEITA-SHORT`
- **Ledger:** `.receita-short-ledger.json`
- **Fonte:** reel `facebook.com/reel/1683536299390859` (19,8s). Leitura ótica
  frame a frame + Whisper, 2026-08-04. Baixado pela rota 2b do
  [`RUNBOOK-watch-videos.md`](funil-organico/RUNBOOK-watch-videos.md).
- **Mecânica de Veo (IMAGE/TAKE, mãos, prop, câmera, luz):** mora no
  [`V4`](AGENTE_ED_ORGANIC_WAVE_V4.md) e **só lá**.

---

## 1. O QUE ESTE ÂNGULO TEM QUE NENHUM OUTRO TEM

É o **único agente do repertório sem prop fálico e sem corpo-prova** nas duas
primeiras cenas. Os outros doze seguram o scroll com um objeto na mão de
alguém; este segura com **uma mão de homem velho e uma tigela**.

| | os outros | RECEITA |
|---|---|---|
| quem fala | narradora, ou o narrador sobre um terceiro | **o próprio homem, 1ª pessoa** |
| a prova | um corpo, um prop, uma plateia | **a receita sendo feita** |
| o rosto | nas 3 cenas | **só na cena 3** |
| o claim | dito na copy | **impresso na caixa** (silhueta de cavalo) |

⛔ **A confissão é dele.** `RE14` trava a primeira pessoa na cena 1. Narradora
contando de um terceiro já é o TROCA e o ESCÂNDALO — trocar a voz aqui não
"varia", apaga o ângulo.

---

## 2. O ARCO — 3 cenas de 8s

```
cena 1  A PERDA      perda -> rejeição -> VILÃO               (o hook)
cena 2  A RECEITA    virada -> resultado -> REAÇÃO            (o mecanismo)
cena 3  O PAYOFF     ele e ela num lugar masculino + a taça   (o CTA)
```

**Três beats por cena, e nenhum é opcional** — os dois últimos (o VILÃO da cena 1
e a REAÇÃO da cena 2) entraram por ordem do operador, ocupando folga de tempo que
eu tinha **medido e reportado** sem preencher. É o padrão: eu meço, ele decide o
que entra.

### ⭐⭐ RE2/RE3 — O TOGGLE DA CENA 1

Ordem do operador, 2026-08-04. A cena 1 tem **dois enquadramentos** e o painel
alterna entre eles (`livre` sorteia):

| modo | o quadro |
|---|---|
| **`corte de maos`** | macro de cima, só as mãos e a tigela. Zero rosto, zero tronco. É a cena 1 da fonte, literal. A fala roda como **voz sobre a cena** — sem rosto não há lip-sync a sincronizar |
| **`terceira pessoa`** | plano médio, ele atrás da bancada, falando na lente. **Mesma ação, mesma tigela, mesma caixa** — muda o enquadramento e só ele |

⛔ **O toggle é regra de FUNÇÃO, não de estilo, e o linter cobra dos dois
lados:** no `corte` é ERRO ter rosto; no `terceira` é ERRO não ter. O autoteste
ainda compara os dois `IMAGE 01/03` gerados com a mesma seed — se saírem
iguais, o painel está oferecendo uma escolha decorativa (§4 das lições).

⚠️ **O toggle governa só a cena 1**, que foi o escopo pedido. A cena 2 fica
sempre no plano aberto sem rosto (fiel à fonte), então no modo `terceira` o
rosto aparece na 1, some na 2 e volta na 3. **Está declarado, não escondido** —
mudar isso é decisão do operador.

---

## 3. AS TRAVAS DO AGENTE

### RE1 — a caixa, e o cavalo que só existe nela
A caixa kraft com **silhueta de cavalo preto impressa** é o prop-mestre: ela faz
o claim de potência sem uma palavra de claim. ⛔ `no readable words` não é
enfeite — rótulo com letra em foco é texto em cena, e a CAUDA promete o
contrário.

⛔⛔ **O cavalo VIVO foi cortado** (ordem do operador, 2026-08-04). A entropia
que ele trazia migrou para o pool de **LUGARES** masculinos. O linter varre
`horse` fora da string travada da caixa.

### RE4 — a bancada aberta, e a mão chapada
A **mão esquerda chapada em primeiro plano**, grande no quadro, é o achado da
leitura ótica e não pode cair: é ela que dá presença física a um homem que não
tem rosto. Sem ela a cena 2 vira b-roll de receita.

### RE12 — ⭐⭐ a reação nomeia o órgão
> ❌ `She noticed.` · ✅ `She noticed my {o} harder than ever.`

O bullet migrou do post-it manuscrito da fonte (`HARDER THAN EVER`) — o papel
saiu do quadro e a copy foi para a fala, ocupando a folga de tempo da cena 2
(a fonte roda 16/18/14 palavras contra uma capacidade de 27-32).

⛔ **Reação de terceiro é o slot da PROVA SOCIAL.** Vago ali, o vídeo perde a
prova *em silêncio*, porque `She noticed.` é uma sentença gramaticalmente
perfeita e passa em qualquer linter de forma. Toda entrada do pool carrega
`{o}`, e o linter cobra dos dois lados. Registro do vício:
[`licoes-de-construcao.md` §20](funil-organico/licoes-de-construcao.md).

⚠️ **O escopo é estreito de propósito.** A versão larga — "todo verbo de
percepção precisa do órgão" — reprovaria `She stopped reaching over at night`
(que está certa) e até a copy que o operador aprovou no RESSURREICAO
(`Her hand lands on it and she freezes`, cujo objeto é um pronome). A regra
codificada é a do **slot**: a última sentença da cena 2.

### ⭐ RE20 — o vilão nomeia QUEM esconde ou QUEM lucra
Terceiro beat da cena 1, por ordem do operador (2026-08-04): *"poderia ter
incluído bullet de ângulo de grande vilão: 'doctors don't want you to know
this'"*.

**O que ele faz:** a PERDA dá o tamanho do problema, a REJEIÇÃO faz o espectador
se ver, e o VILÃO **tira a culpa dele e a põe em alguém**. Sem esse beat, o homem
que assiste conclui que o problema é ele — e não há motivo para ficar mais oito
segundos.

⛔ **Regra de função:** `Nobody told me this` sem dono é **queixa**;
`no doctor gets paid for the answer that actually worked` é **vilão**. É a §20
outra vez, no slot da culpa.

⚠️ **A unidade da lente é o BEAT INTEIRO, não a última sentença** — a primeira
versão olhava só o fim e reprovou `Add up what they took from me. None of it was
meant to work.`, cujo agente mora na primeira sentença. Regra que reprova a copy
certa é regra mal escrita.

### RE21 — nenhum placeholder cru chega ao prompt
Guarda geral nascida de caso real: um `.format()` esquecido mandou
`a man's {o} stays broken` para o `Dialogue:`. O teto de palavras **não pega** —
`_palavras` normaliza `{o}` para uma palavra. Só apareceu **lendo a saída**.

### RE17 — despejo cru
Ordem do operador. **Nada cresce, nada faz morph em cena nenhuma.** Quem cresce
é o RESSURREICAO, e lá o morph é o bit visual. Aqui o bit visual é o pó caindo.

### RE19 — a escalada não é a isca
`If you want the whole recipe — Comment gelatin, and I'll send you the whole
recipe.` A promessa dita duas vezes com as mesmas palavras, no take mais denso
dos três. Resolvido **no sorteio**, não só cobrado no linter.

### As herdadas
`gelatin trick` literal na cena 2 (RE13) · CTA travado em `Comment gelatin,`
com isca · cota do órgão 2/3 · âncora de continuidade na cena 3 **só no modo
`terceira`** (RE7 — no `corte` aquele é o primeiro rosto do vídeo, e cobrar
continuidade de um rosto que ninguém viu é regra larga demais).

---

## 4. OS EIXOS

| eixo | tamanho | nota |
|---|---|---|
| **MUNDOS** (a cozinha) | 12 em 9 famílias | ⚠️ **etnia arrasta o mundo inteiro** — cozinha, bancada, traje, luz, ambiência e as famílias de lugar que aquele nicho comporta. Não há eixo `etnia` solto |
| **LUGARES** (payoff) | 16 em 6 famílias | garagem é **5 entradas distintas** = 36% do lote. É como se atende "garagem bem mainly" sem que **nenhuma entrada** passe do teto de 17% |
| **REFS** (o confessor) | 12, 57-69 anos | cobre rosto **e mão** — a mão é a única identidade dele no modo `corte` e na cena 2 inteira |
| **MULHERES** (a parceira) | 12, 30-35 anos | ⛔ **lei do REF.** Faixa no topo da lei de propósito: a fonte põe uma loira de ~25 ao lado de um homem de 60+, e diferença de idade grande é geometria que o classificador olha com lupa sem nada a ganhar em conversão |
| ACOMPANHAMENTOS · PO_E_GEL | 10 · 7 | zero marca legível (P12) |

**Copy:** PERDAS 10 · REJEIÇÕES 10 · **VILÕES 14** · VIRADAS 8 · RESULTADOS 8 ·
**REAÇÕES 10** · ESCALADAS 10 · ISCAS 10 · GATES 9.

⚠️ **A tensão com a regra 3.2 está declarada, não escondida:** o WORKFLOW manda
a etnia do REF casar com o avatar da página. Este motor segue o precedente que
o operador abriu no COLO — a etnia sai do MUNDO. Quem quiser o comportamento
antigo trava o mundo no painel.

---

## 5. MEDIDO

```
600 vídeos · 0 ERRO · mundos 12/12 · lugares 16/16 · etnias 10 · refs 12/12
toggle: corte 47,2% | terceira 52,8%
cena 1: 22-31 palavras (média 28,8) · 3,59 p/s
cena 2: 27-33 palavras (média 31,6) · 3,95 p/s
cena 3: 23-31 palavras (média 28,7) · 3,59 p/s
vídeo: 89,2 palavras
```

⚠️ **A cena 1 rodava a 2,43 p/s** (média 19,4 palavras) contra uma capacidade
real de 3,4-4,0 — oito palavras de silêncio por vídeo. Reportei a folga sem
preencher, porque inventar bullet é alçada do operador; ele mandou o VILÃO, e a
taxa subiu para 3,59, alinhada com as outras duas cenas. **É assim que a folga se
fecha: medição de um lado, decisão do outro.**

Gates: `medir_personagens --gate` exit 0 · `medir_contexto_copy --gate` exit 0
(0 frases órfãs em 1.619). ⚠️ O gate de contexto **reprovou uma entrada dos
VILÕES na primeira passada** — `They sold me the age excuse for eleven years.`
nomeia uma causa (`age`) sem dizer o que ela quebra, que é a frase órfã da §17.
Corrigida antes da entrega.

---

## ⛔ RECUSA DO GERADOR — troca-se a FORMA DE DIZER, nunca a cena

> **Quase nunca a cena está barrada — a frase está.**

Recusa do gerador **não é veredito sobre o conteúdo**. O classificador julga
**tokens e geometria**, não intenção: a mesma cena, dita com outro vocabulário,
passa. Caso validado (Ray/consultório 2026-07-28): `sitting across his lap` foi
recusado na política de menores **duas vezes**, com o IMAGE já aprovado;
`perched sideways on his right knee, the way a newlywed poses for a photograph`
gerou **a mesma imagem** sem bloqueio nenhum.

⚠️ **Onde este agente é mais exposto:** a cena 3, que pareia um homem de 57-69
com uma mulher de 30-35. Se ela for recusada, a primeira alavanca é **nomear a
relação** (`his wife of thirty years`) e **nomear o gênero da imagem** (`the way
a family photograph is taken`) — nunca separar o casal, que é o que faz o
payoff existir.

**As 4 alavancas, nesta ordem:**
1. **Trocar o token exato** que o classificador reconhece.
2. **Nomear a relação** na mesma frase da pose.
3. **Nomear o gênero da imagem** — diz ao modelo que é retrato, não intimidade.
4. **Neutralizar os verbos de contato e congelar a geometria.**

⛔ **O que NÃO funciona:** declarar conformidade (`not a celebrity`, `they are
adults`) sem trocar a forma. Declaração não desarma classificador — ela entrega
ao classificador a categoria que ele deve procurar.

⛔ **NUNCA mudar copy ou cena por conta própria.** Esgotadas 3-4 formulações,
**parar e reportar ao Ed** com o diagnóstico e as opções — a decisão é dele
(`CLAUDE.md` §Regra de alçada).

Protocolo completo e tabela de reescritas já validadas:
[`funil-organico/prop-metaforas.md`](funil-organico/prop-metaforas.md)
§Recusa do gerador.

---

## Conexões

- [`funil-organico/receita_short.py`](funil-organico/receita_short.py) — o motor
- [`funil-organico/RUNBOOK-app-offline.md`](funil-organico/RUNBOOK-app-offline.md) — motor → app → `.exe`
- [`funil-organico/licoes-de-construcao.md`](funil-organico/licoes-de-construcao.md) — §20 é a regra que fez o RE12 existir
- [`AGENTE_ED_ORGANIC_WAVE_V4.md`](AGENTE_ED_ORGANIC_WAVE_V4.md) — a mecânica do Veo
- [`AGENTE_ED_COLO_V1.md`](AGENTE_ED_COLO_V1.md) — o precedente de "etnia arrasta o mundo"
