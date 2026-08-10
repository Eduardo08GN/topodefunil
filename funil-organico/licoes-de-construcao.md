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

## 18. ⛔ ÂNCORA DE PONTUAÇÃO: o medidor dizia 0 com 48 falas meio em inglês

Terceira vez que o **medidor** é o culpado (§15, §16, agora esta). O verificador
de tradução casa o template contra os trechos da fala gerada — e a regex que ele
compila é **ancorada no fim**:

| onde | o texto |
|---|---|
| pool do motor | `Ginger and cinnamon wake your {o} up` — **sem ponto final** |
| trecho da fala | `Ginger and cinnamon wake your wiener up.` — **com ponto**, porque veio de um `split` por sentença |

A regex nunca casou. Resultado: **`templates sem PT: 0`** enquanto o app mostrava
frase pela metade em inglês. E o mesmo desencontro do outro lado — o dicionário
tinha a chave *com* ponto e o pool consulta *sem* — fazia o relatório acusar 18
templates que já estavam traduzidos.

> **Medidor que mente é pior que medidor nenhum:** com nenhum eu vou olhar; com
> um mentindo eu declaro pronto e vou embora.

**O que impede:** ao casar template contra texto renderizado, **normalizar a
pontuação terminal dos dois lados** antes de comparar. Vale para qualquer lente
que compare *string gravada no pool* com *string que passou por montagem de
frase* — a montagem sempre acrescenta pontuação que o pool não tem.

⚠️ **O que revelou o erro não foi o medidor: foi ler a saída.** Duas falas lidas
inteiras mostraram inglês no meio do português, e só então eu fui olhar por que
o número dizia zero. **Ler a saída continua sendo o único controle que nenhum
medidor substitui.**

📌 **E o gatilho que produziu tudo isso:** copy alterada a montante. Quando
alguém reescreve um pool, a camada PT fica órfã **em silêncio** — nenhum linter
de motor olha para tradução. Toda alteração de copy tem de sair com a tradução
na mesma entrega, medida.

### ⛔⛔ A emenda cara: consertei o MEDIDOR e não o MEDIDO

No dia seguinte, o mesmo bug apareceu de novo — e a causa foi o meu conserto.

Eu tinha corrigido a âncora de pontuação **no verificador**. O verificador
passou a dizer `0 templates sem PT`. Mas quem traduz para o usuário é outro
arquivo, e nele a âncora continuava errada: **151 falas saíam inteiras em
inglês no painel enquanto o relatório mostrava cobertura cheia.**

> **Consertar a lente não conserta o que ela olha.** E é pior que não consertar
> nada: agora o número me dava permissão para ir embora.

**O que impede:** achou um bug de casamento/parsing num verificador? Perguntar
**onde mais esse mesmo código roda**. Aqui eram dois: `checar.py` (mede) e
`traducao.py` (faz). Corrigir só o primeiro é maquiar o painel.

### ⛔ E o corolário: a correção seguinte quebrou um agente que estava zerado

Ao consertar o tradutor, quebrei a fala no travessão **antes** de tentar casar
o template. Passou de 95,4% para 92,8% e **derrubou o TROCA de 0 para 38 falas
quebradas** — porque metade dos templates tem travessão *dentro*
(`gelatin trick - days, not months`), e quebrar ali destrói o template.

O jeito certo foi o travessão como **último recurso**: tenta casar inteiro,
e só se falhar tenta partir. Regra geral: **separador que também aparece dentro
do conteúdo não pode ser aplicado antes da tentativa de casamento inteiro.**

⚠️ **E o que revelou a regressão foi medir os OUTROS agentes.** Se eu tivesse
olhado só o número do agente que estava consertando, teria comemorado 92,8%
sem ver que quebrei um vizinho. **Toda correção em código compartilhado se mede
no parque inteiro, não no caso que motivou a correção.**

---

## 19. ⛔ GREP NO CÓDIGO NÃO VÊ FRASE QUEBRADA ENTRE LINHAS

Três vezes no mesmo dia, e a terceira quase foi entregue.

Ao ancorar os dentes do CLEAN (CL25), procurei os pontos com
`grep "mouth open mid-word"`. Achou **4**. Existiam **7**: o Python quebra
string longa em várias literais adjacentes, e a frase mora partida —

```python
"...with %(Ss)s mouth "
"open mid-word as %(s)s speaks, ..."     # ← o grep nunca vê a frase inteira
```

Editei os 4, medi **o código**, declarei pronto. Metade dos blocos continuava
sem âncora, e só apareceu ao **renderizar e ler a saída**.

> **O código é o que eu escrevo; o prompt é o que o modelo recebe.** São coisas
> diferentes sempre que há concatenação, `%`-format ou `.join()` no meio — e
> num gerador de prompt há sempre.

**O que impede:** verificar no **texto montado**, nunca no fonte. Concretamente:
`montar(spec)` num laço, e conferir a presença da frase no bloco renderizado com
os espaços normalizados (`re.sub(r"\s+", " ", texto)`).

⚠️ **E remendar às cegas cria defeito novo.** No meio disso eu duplicei a
palavra `speaks` em dois blocos — `"...as she speaks, the front teeth even and
complete, speaks, her torso upright..."`. Não aparece no `git diff`, porque
cada linha isolada está correta; só aparece na frase montada.

📌 **Generaliza para todo medidor deste repo:** os que leem `.py` com `ast` ou
regex (`medir_personagens`, `checar.py`) medem *pools*, não *saída*. Servem para
achar buraco de repertório. **Não servem para provar que uma frase chegou ao
prompt** — para isso, montar e ler.

---

## 20. ⛔⛔ "SHE NOTICED." — o vício crônico de ser vago em copy

**Terceira vez que o operador me para pelo mesmo motivo** (§17 foi a primeira,
a frase órfã do RESSURREICAO; a segunda foi a prova sem `{o}` do TROCA). Em
2026-08-04, propondo o pool de bullets do agente novo, escrevi:

```
SHE NOTICED
```

O operador respondeu com a única coisa que importa — **o que o espectador pensa
ao ouvir aquilo**:

> *"Ela notou o quê? **WTF???**"*

E nomeou o defeito: **"vício crônico seu de drifting de copy"**. A forma certa,
ditada por ele:

| | |
|---|---|
| ❌ o que eu escrevi | `She noticed.` |
| ✅ o que converte | `she noticed his John-son harder than ever` |

**Por que eu reincido, e é sempre a mesma mecânica:** a frase me parece completa
**porque eu tenho o contexto da cena na cabeça**. Eu sei que ela notou o pau
dele — acabei de escrever a cena. O espectador chegou agora, no scroll, com o
som pela metade, e recebe um sujeito reagindo a coisa nenhuma.

⚠️ **E é pior num slot de REAÇÃO do que em qualquer outro.** Reação de terceiro
é o slot que carrega a **prova social** — é ele que diz que funcionou. Vago ali,
o vídeo perde justamente a prova, e perde em silêncio: passa em todo linter de
forma, porque `She noticed.` é uma sentença perfeita.

**A regra, e ela não tem exceção:**

> **Todo verbo de percepção ou reação nomeia o órgão NA MESMA SENTENÇA.**
> `noticed`, `saw`, `felt`, `froze`, `stopped`, `stared`, `couldn't believe` —
> nenhum deles sai sozinho. Sentença é a unidade; frase vizinha não paga (§16,
> escopo).

**O que impede** — vira linter, não comentário (§4). Sentença com verbo de
percepção/reação e **sem** substantivo do `NUCLEO` na mesma sentença = **ERRO**.
Nasce dentro do agente novo, com controle positivo (`She noticed.`,
`Her jaw dropped.`) e negativo (`she noticed his John-son harder than ever`)
rodados **antes** de qualquer número ser olhado (§16).

⚠️ **Promoção para o `short_comum.py` só depois de medir o parque inteiro** —
ligar lente nova para os doze de uma vez é como eu quebrei um vizinho ao
consertar o tradutor (§18).

📌 **O teste barato, e é o mesmo do §17, agora explícito para reação:** ler a
sentença **sozinha, fora do vídeo**, e perguntar *"o quê?"*. Se a pergunta tem
resposta só na cena, na frase anterior ou na minha cabeça, a sentença está vaga.

---

## 21. ⛔⛔⛔ POR QUE EU REINCIDO NA COPY VAGA — a investigação que o operador pediu

**Quarta ocorrência no mesmo dia** (2026-08-04). O operador leu o take 2
renderizado do ESCANDALO e parou tudo:

> *"«I read every forum there is and found nothing» — telespectador: «read what?
> WTF? What the hell is she talking about???»"*

E então fez a pergunta que este capítulo existe para responder:

> ***"Você precisa investigar o porquê você está cometendo de forma teimosa e
> recorrente isso. Seria cálculo cego de encaixe matemático de fala pra caber
> dentro do espaço curto de duração de vídeo? Se sim, você está sacrificando
> todo o nosso funil de vendas em prol disso."***

### O que a medição disse — e ela desmente a minha própria desculpa

Medido em 120 sorteios × 13 motores, olhando a **primeira sentença de cada
cena** (a que o espectador ouve antes de qualquer outra):

| motor | aberturas órfãs | folga média naquelas falas |
|---|---|---|
| clean | 81,1% | **+3,9 palavras** |
| pee | 75,0% | +4,7 |
| organicwave | 70,6% | **+7,2** |
| flagrante | 66,9% | +5,6 |
| necrose | 66,7% | +6,5 |
| **escandalo** | **64,2%** | **+3,1** |
| receita | 61,7% | +1,9 |
| troca | 36,4% | +2,6 |

> **A hipótese do encaixe matemático CAI.** Sobravam 2 a 7 palavras exatamente
> nas falas onde eu omiti o referente. O teto nunca me obrigou.

### A causa raiz, e são três camadas

**1. Eu construí todas as lentes na UNIDADE ERRADA.** A cota do órgão cobra a
CENA. A §20 cobra a última sentença. A RE20 cobra o beat do vilão. **Nenhuma
lente jamais olhou a PRIMEIRA sentença** — e é ela que decide se o espectador
fica. Toda vez que eu media, o órgão *estava lá*, na terceira frase, e eu ia
embora satisfeito. O instrumento dizia verde sobre o lugar errado.

**2. Eu escrevo com a cena inteira na memória de trabalho.** Ao escrever *"I
read every forum there is"* eu estou segurando *"...e aí veio o gelatin trick e
o pau dele voltou"* na cabeça. A sentença me parece completa porque o PARÁGRAFO
está completo. O espectador recebe **em série**, uma frase de cada vez, e a
primeira chega sozinha.

**3. O orçamento não é a causa, mas é uma PRESSÃO DE SELEÇÃO real.** O
`_cabem()` descarta em silêncio a linha que não cabe. Ao longo de dezenas de
entradas isso enviesa o pool para o curto — e **a forma mais barata de encurtar
uma frase é matar o objeto dela**, que é gramaticalmente opcional e
comunicativamente obrigatório. Não foi o teto que me obrigou; foi o teto que me
*educou* errado. É a parte da hipótese do operador que está certa.

### A regra, e ela é dele

> **"Sempre leia: se a sentença dá afirmativo para possibilidade do leitor
> dizer «wtf he/she talking about?», é drifting de copy vaga, é DESCARTE de
> copy."**

⛔ O veredito é **descarte**, não conserto: a linha sai do pool. E o teste roda
**sentença a sentença, lida isolada** — nunca sobre a fala inteira, porque lida
inteira ela sempre faz sentido para quem a escreveu.

### O que impede

| | |
|---|---|
| **ES22** (ESCANDALO) | a primeira sentença da cena 2 nomeia o órgão. Controle negativo = a frase exata que o operador reprovou |
| **§20 / RE12** | a reação nomeia o órgão na mesma sentença |
| **RE20** | o vilão nomeia quem esconde ou quem lucra |
| **`medir_contexto_copy --gate`** | frase que nomeia causa sem dizer o que ela quebra |

⚠️ **E o que ainda NÃO está travado:** as aberturas órfãs dos outros 12 motores
(36% a 81%). Estão **medidas e registradas** aqui, não corrigidas — reescrever
copy dos doze é decisão do operador, não minha (regra de alçada).

---

## 22. ⛔⛔⛔ A LENTE CARREGAVA O VÍCIO QUE EXISTIA PARA PEGAR

**Quinta e sexta ocorrências**, no mesmo dia (2026-08-04), horas depois de eu
escrever a §21 dizendo que tinha entendido.

| o que saiu no app | o operador |
|---|---|
| `I almost lost her because my pecker embarrassed me` | *"lost **who**? His mom? His sister? Wtf are he talking about?"* |
| `They will sell you a monthly plan before they sell you the truth` | *"**who** will sell **what** and with **what purpose**?"* |

E a frase dele: ***"Mais uma vez você cometeu seu vício mais crônico de todos!
Inacreditável!"***

### O que era novo, e é pior que a §21

A §21 diz que eu media a **unidade errada**. Isto é outra coisa:

> **Eu construí a lente RE20 para exigir "o vilão nomeia QUEM" — e aceitei
> `they`, `them`, `nobody` e `somebody` como resposta válida.**

Pronome não é nome. A regex que eu escrevi para pegar o vício **continha o
vício**. Ela rodou verde em 600 sorteios, com controle positivo e negativo
passando, e mandou para produção exatamente a frase que o operador reprovou.

**A forma que generaliza:** ao escrever a lista de tokens aceitos por uma lente,
eu incluo o que é **fácil de casar**, não o que **cumpre a função**. `they`
aparece em toda frase de vilão — por isso entrou. É a §4 mudada de lugar: agora
não é o slot que não cumpre a função, é a **lente**.

**O que impede:** toda lista de tokens aceitos passa pelo teste da função, item
por item. *"`they` diz QUEM esconde?"* Não → fora. E o controle positivo tem de
incluir **a forma quase-certa**, não só a obviamente errada: `They will sell
you…` parece um vilão e não é.

### ⭐ O modelo do vilão, ditado pelo operador

```
[QUEM] + [o que ele te VENDE] + [o que ele te ESCONDE]
```
> *"the pharmacy industry will sell you pills and not let you know the truth
> that works"*

⛔ E o mesmo vale para a PERDA: **quem** se perde, nomeado. `my wife`, nunca
`her`.

### ⛔ E o bug de escrita que custou três rodadas

Ao corrigir isso por script, escrevi a regex num heredoc:

```python
t = t.replace(..., 'r"\\b(my wife|...)"')     # vira \b na string...
```

`\b` numa string Python **não-raw** é o caractere **BACKSPACE (0x08)**. O arquivo
ficou com `r"<BS>(my wife|…)"` — um byte invisível dentro de uma string raw, e o
padrão passou a exigir um backspace no texto. **Reprovou 100% do pool** com uma
mensagem perfeitamente plausível, e eu caí nele **duas vezes seguidas**.

> **Regex se escreve no ARQUIVO, com edição literal — nunca por script com
> escape.** E `0x08` no fonte é invisível no `git diff` e no editor.

Sintoma de reconhecimento: linter novo que reprova **tudo** — §2 outra vez, e a
suspeita é sempre dele.
## 23. ⛔ 100% DE AMOSTRA NÃO É 100% — o medidor mentiu pela QUARTA vez

Eu declarei ao operador, com número na mão: **`2160/2160 = 100%`**, tradução
completa nos doze agentes. Ele pediu para ajustar mesmo assim. Fui medir fundo:

| sorteios por agente | templates sem PT que apareceram |
|---|---|
| 60 *(o default)* | **0** ← o número que eu reportei |
| 400 | **+10** |
| 1.200 | **+1** |
| 3.000 | 0 |
| 6.000 | 0 — convergiu |

**Onze templates sem tradução**, e o relatório dizia 100%. Eles vivem em
combinações raras de pool — um item A que só casa com dois item B, um gate que
só aparece com uma família — e 60 sorteios simplesmente nunca os tiravam.

> **Cobertura de amostra mede o que o sorteio calhou de gerar, não o que o
> agente é capaz de gerar.** Com pool combinatório, a cauda é longa e é
> exatamente onde mora o que ninguém revisou.

**O que impede:**
- ⛔ **Não basta aumentar o número.** Número maior sempre acha mais, até
  convergir. O que prova cobertura é **convergência**: dois patamares seguidos
  sem achado novo.
- O default do `checar.py` subiu de 60 para **400**, e ganhou `--fundo` (3.000).
  Quando o resultado é limpo mas a amostra é pequena, ele **avisa na tela** que
  aquilo é amostra.
- Antes de dizer "100%" para o operador: **rodar `--fundo` e ver convergir.**

⚠️ **E a linha do aviso não pode ter emoji.** A primeira versão tinha `⚠️`, e o
console do Windows é cp1252: `UnicodeEncodeError` derrubando o próprio
verificador na hora de avisar.

---

## 24. ⛔⛔⛔ O VÍCIO SE MUDOU PARA O FIM DA FRASE — e a lente olhava só o começo

**Data:** 2026-08-04. **Custo:** três renders reprovados no mesmo dia, e a
descoberta de que 12 das 14 entradas de um pool que eu tinha declarado limpo
carregavam o mesmo defeito.

O operador leu três takes do RECEITA e corrigiu os três à mão:

| gerado | reação dele | o que devia ser |
|---|---|---|
| `...points you at the expensive pill and away from this.` | *"Drifting identificado 'away from this.' From what???"* | `...at the expensive pill, the secret is in this natural trick.` |
| `Nobody owns what my grandfather knew.` | — | `Nobody owns what my grandfather knew to trully save my john-son and my marriage` |
| `It came back full and stayed hard...` | — | `My tool came back full and stayed hard...` |

⚠️ **A segunda foi a cara.** Ao reler o pool inteiro com o teste WTF, não eram
duas linhas ruins: eram **12 de 14**. Toda entrada terminava num substantivo
abstrato sem destino — `what costs two dollars`, `nothing that worked`, `the
cheap fix`, `asking questions`, `a man stays broken`.

⛔⛔ **E todas passavam pela minha lente RE20**, que existia exatamente para
cobrar isso. Porque **RE20 cobrava o agente no COMEÇO da frase e nunca olhava o
fim.** Eu tinha escrito a regra a partir do exemplo que o operador me deu
(`[QUEM] + [o que VENDE] + [o que ESCONDE]`) e não percebi que o molde dele
tinha uma quarta parte que eu não codifiquei:

> **[QUEM] + [o que ele te VENDE] + [o que ele te ESCONDE] + [PARA QUE SERVE]**

Sem a quarta parte o espectador ouve uma briga com a farmácia e **não sabe o que
ele ganha se a farmácia perder**.

⭐ **A causa raiz é a mesma da §22, num disfarce novo.** Lá o vício era *sujeito
sem objeto* (`She noticed.`). Aqui é *objeto sem substantivo*: a frase termina
apontando o dedo para o vazio. A lente pegava a forma que eu já conhecia e o
vício simplesmente **mudou de posição dentro da frase**.

⛔ **O que impede:** ao escrever lente de slot, cobrir a frase INTEIRA, não a
posição onde o defeito apareceu da última vez. E ao receber um molde do
operador, **contar as partes** — se ele deu quatro e a lente cobra três, a
quarta é exatamente onde o vício vai morar.

⭐ **E a escassez de repertório empurra para o pronome.** O motor sorteava DUAS
grafias do órgão por vídeo, com um comentário meu explicando que bastava
"porque repetir o substantivo vira bordão". Essa premissa falsa é o que
empurrou metade dos slots para `It` e `this`. O operador mostrou a saída usando
**quatro grafias** nos takes que corrigiu (`weiner`…`john-son`, `tool`…`soljer`).
`NUCLEO` sempre teve cinco. **Bordão é a mesma palavra duas vezes; grafia
diferente não é.**

---

## 25. ⛔⛔ O CONTROLE ACERTAVA POR COINCIDÊNCIA DA COPY VIZINHA

**Data:** 2026-08-04. Descoberto porque o autoteste roda os controles antes dos
números — ele acusou a si mesmo.

O controle negativo do `She noticed.` trocava a última sentença assim:

```python
re.sub(r"[^.]+\.$", "She noticed.", falas[1])     # ⛔ sem o \s*
```

Sem o `\s*`, a troca comia o espaço separador e produzia
`...twenty years.She noticed.`. E `_sentencas` divide em `. ` — então devolvia
**as duas grudadas como uma sentença só**. A sentença grudada carregava o órgão
da frase anterior, e RE12 passava.

⚠️ **Ele funcionou por dois meses.** Só quebrou no dia em que a copy VIZINHA
mudou: enquanto o resultado começava com `It came back...` a frase grudada não
tinha órgão e o controle acertava; quando o resultado passou a nomear o órgão, o
controle ficou cego.

⛔ **Controle que depende da copy ao redor não é controle.** É a §16 aplicada ao
próprio medidor: se ele só reprova o caso conhecido por acidente, ele mede outra
coisa. **Todo controle tem de construir a string inteira que ele afirma testar**,
nunca derivá-la por substituição parcial de uma fala sorteada.

⚠️ **Corolário que já cobrou duas vezes hoje:** ao estreitar uma lente, o teste
não é "o número caiu" — é **ler os flagrantes**. A primeira versão do
`medir_deiticos.py` acusou 302 frases do RESSURREICAO e 22 do NECROSE, todas
corretas, com uma tabela perfeitamente plausível. Vídeo tem duas saídas que
texto não tem: **anáfora do CTA** (`or Facebook won't deliver it` — `it` é a
receita, dita na frase anterior) e **dêitico que aponta para o prop em quadro**
(`His hangs just like this`). Regra que ignora isso manda consertar copy certa.

---

## 26. ⛔⛔⛔ O EXEMPLO DELE É REFERÊNCIA DE FORMA, NUNCA ESPECIFICAÇÃO DE MÉTRICA

**Data:** 2026-08-04. **O que eu fiz:** o operador reescreveu um take à mão para
me mostrar o molde do vilão. O take dele tinha 33 palavras. Eu **subi o teto de
fala de 31 para 33** para acomodá-lo.

Ele parou:

> *"Eu não testei o meu exemplo contra o teto. Pare de ser literal com meus
> exemplos, eles são apenas referência, não absolutismo. Você errou quando
> assumiu que eu verifiquei o meu exemplo contra o teto."*

E, na mesma conversa:

> *"Pare de reproduzir literalmente meus exemplos como uma maritaca repetindo o
> dono. Você tem que entender a IDEIA que quero passar."*

⭐ **A separação que eu não fiz:** o exemplo dele especifica a **FORMA** — as
quatro partes do molde, a ordem dos beats, o registro. A **MÉTRICA** (quantas
palavras cabem em 8 segundos) é física e continua sendo minha obrigação medir.
**Forma se copia; métrica se mede.** Assumir que ele validou a métrica é inventar
uma verificação que ninguém fez.

⚠️ **E o custo tem duas partes.** A primeira é óbvia: eu afrouxei uma trava
física. A segunda é sutil e pior — copiar o exemplo ao pé da letra faz o
repertório do agente ficar **do tamanho do exemplo**, que é exatamente o
mode-collapse que os randomizadores existem para evitar.

⛔ **O que impede:** quando ele der um exemplo, extrair a REGRA e depois testar a
regra contra as travas físicas do motor. Se o exemplo dele violar uma trava,
isso não é permissão para mover a trava: é a hora de dizer *"o seu exemplo tem
33 palavras e o teto físico é 32; a forma eu aplico, e ela cabe assim"*.

⭐ **Corolário do próprio dele, dito na sequência:** ao comprimir para caber, o
que sai é palavra que **não carrega nada**. Nunca sai o referente. Comprimir
matando o "do que se trata" troca um defeito por outro pior — ver §20, §24.

---

## 27. ⛔⛔⛔ A LENTE DO TETO CONFERIA COERÊNCIA INTERNA, NÃO CAPACIDADE FÍSICA

**Data:** 2026-08-04. Descoberto ao auditar os 14 motores depois do aviso dele.
**Cinco motores cortavam fala em produção e nenhum medidor sabia.**

| motor | cena | estouro | pior caso |
|---|---|---|---|
| `vazamento` | 3 | **53,5%** | **48 palavras = 6,0 p/s** |
| `exterior` | 3 | **95,7%** | 34 palavras |
| `vazamento` | 2 | 32,5% | 36 palavras |
| `organicwave` | 2 | 9,0% | 34 palavras |
| `flagrante` | 2 | 6,0% | 33 palavras |
| `necrose` | 3 | 3,2% | 36 palavras |

⛔⛔ **Cada motor já tinha a lente do próprio teto — e todas passavam.** Porque
comparavam a fala com o `TETO_FALA` **declarado naquele arquivo**. Se o teto
declarado é 40, uma fala de 40 palavras passa no lint e é cortada no render.

**A regra media coerência interna, não a coisa que precisava ser verdade.** É a
§16 na forma mais cara: o medidor conferia o que era fácil conferir. Um teto
declarado acima da capacidade física não é uma escolha de estilo — é uma trava
desligada, e o lint vira carimbo.

⚠️ **E o `_cabem()` tem um fallback `or pool`** que devolve o pool inteiro quando
nada cabe. Ele existe por bom motivo (lista vazia derrubaria o sorteio com
`IndexError` em vez de acusar pelo linter), mas é um caminho de estouro
**silencioso**: quando o orçamento aperta, ele entrega a fala longa sem reclamar.

⛔ **O que impede:** [`medir_teto_fala.py`](medir_teto_fala.py), que compara com
o número **físico** (32) e não com o declarado, e que também acusa **teto
declarado acima de 32 mesmo quando ainda não estourou** — bomba armada é a
entrada longa que alguém vai acrescentar amanhã.

---

## 28. ⛔⛔ O TOPO DA FAIXA NÃO É TETO — 32 PALAVRAS AINDA CORTA

**Data:** 2026-08-05. **Evidência:** um render, não uma conta.

Eu tinha acabado de estabelecer 32 palavras como teto físico (§27), tirado da
§5: *"capacidade real de 8s na nossa taxa de fala (3,4-4,0 p/s) = 27-32"*. O
operador mandou um TAKE 01 do BOTICA com a fala **cortada** — e ela tinha
**exatamente 32 palavras**.

⚠️ **O erro foi pegar o TOPO de uma faixa e chamar de teto.** A faixa 3,4-4,0
p/s descreve o que a narração *pode* fazer, não o que ela faz sempre. 32
palavras exige que a REF fale a 4,0 p/s — o limite superior — durante os 8
segundos inteiros, sem respirar. Qualquer narradora um pouco mais lenta, e a
frase não termina.

⭐ **A reescrita dele tinha 25 palavras = 3,1 p/s.** Ou seja, o operador
naturalmente escreve *abaixo* da faixa que a doutrina declara. Isso é dado, não
opinião: é a taxa que ele considera falável.

⛔ **O que impede:** teto por cena calibrado no que o motor **realmente entrega
sem cortar**, não no máximo aritmético. Quando houver render cortado, o número
que vale é o do render — o cálculo perde para a evidência. E ⚠️ **§5 continua
valendo na outra direção**: teto conservador demais vira espaço morto e o slot
vira enchimento. A faixa útil é estreita e se acha medindo, não deduzindo.

⛔⛔ **SEGUNDA EVIDÊNCIA, no mesmo dia — e ela mostra que eu não tinha aprendido
a lição, só ajustado o número.** Baixei o teto do BOTICA para 28 e o operador
mandou outro render **cortado em `secret`**, com a fala em **exatamente 28
palavras**. Duas vezes seguidas o teto que eu escolhi era o comprimento que
cortava.

⚠️ **O erro de método é o mesmo nas duas:** eu escolhi o número pelo que *cabia
na conta* e depois esperei o render reprovar. O caminho certo é o inverso —
**partir do que já se sabe que fala sem cortar** (os exemplos que o operador
escreve à mão vivem em 3,0-3,1 p/s, nunca em 4,0) e só subir se sobrar silêncio
medido.

⭐ **E havia uma aritmética que eu não tinha feito.** Na cena 1 do BOTICA o
ingrediente raro custa até **10 palavras** (o aposto é obrigatório por outra
regra), a virada mais curta 5 e o fecho mais curto 5: são **20 palavras
comprometidas antes de a abertura dizer qualquer coisa**. Com aberturas de 11
palavras, nenhum teto honesto fecharia. **Antes de calibrar teto, somar os
pisos dos beats obrigatórios** — se a soma já ocupa o orçamento, o problema não
é o teto, é o repertório.

⚠️ **Corolário sobre a §27:** o gate `medir_teto_fala.py` usava 32 como limite
absoluto — ele pegava o que era *certamente* impossível, e **não** garantia que
uma cena de 31 coubesse. Gate de teto é piso de qualidade, não certificado.

⛔⛔ **O NÚMERO FINAL É 25, e a ordem que o fixou é permanente.** Ed, 2026-08-05:
*"Sempre meça. Não pode haver cortes de fala."* Os exemplos que ele escreve à
mão vivem em **16-25 palavras (2,0-3,1 p/s)** — essa é a taxa real da narração,
não os 4,0 da §5.

⭐⭐ **E a coluna que decide não é o máximo, é o MÍNIMO** — `medir_teto_fala.py
--curva`. Se o piso do motor já passa do teto, **baixar o teto não resolve
nada**: o motor não sabe falar mais curto, e o único caminho é encurtar copy.
Sem essa coluna a gente troca o teto e o render continua cortando, que foi
exatamente o que aconteceu duas vezes. Medido nos 14 motores em 2026-08-05:
**28 das 42 cenas cortavam fala**, sendo 8 delas com o piso acima de 25.

---

## 29. ⛔⛔ COPIAR UM MOTOR TRAZ O LINTER **E AS CENAS** — e só um dos dois grita

**O que aconteceu.** Criei o PLACA copiando `dupla_short.py`. Troquei a
identidade, troquei os pools de copy, e parei ali. O operador pegou lendo o
prompt gerado: *"me parece que o agente placa está gerando os prompts image do
agente dupla"*. Estava mesmo — duas mulheres lado a lado com um par de props,
quando o PLACA é UMA mulher apontando o prop na virilha DELE com uma placa
escrita à mão. A fala era a certa; a imagem era de outro ângulo.

**Por que passou.** Motor copiado traz duas heranças, e elas falham de jeitos
opostos:

| Herança | Como falha | Ruído |
|---|---|---|
| **O LINTER** | reprova 100% da produção na hora | ALTO — impossível não ver |
| **AS CENAS** | geram um prompt **válido** do ângulo errado | **ZERO** |
| **AS SONDAS do autoteste** | passam sempre, vigiando regra morta | **ZERO** |

O barulhento me obrigou a olhar. O silencioso chegou ao render. E a terceira
linha é a pior: uma sonda que vigia regra desligada dá "AUTOTESTE OK" e o
autoteste inteiro perde o direito de ser acreditado.

**O que impede.** Ao copiar um motor, três listas, nesta ordem, antes de rodar
qualquer coisa:

1. **Toda constante `BO_*` de cena** — cada uma é uma decisão visual do OUTRO
   ângulo até que eu a reescreva ou a apague.
2. **Toda regra do `lint()`** — reescrever ou apagar, nunca `if False`. Regra
   desligada com `if False` deixa a sonda correspondente viva e cega.
3. **Toda sonda do `autoteste()`** — cada uma tem de apontar para uma regra que
   este ângulo TEM. Sonda de regra morta é decoração.

**O corolário que vale para tudo.** *A lente tem de acompanhar a regra.* Toda
vez que eu movo uma regra (o raro saiu da cena 1 e foi para a cena 2, o
aposto mudou de cena, o traje virou eixo próprio), a sonda que a vigiava fica
apontando para o lugar vazio e passa a devolver verde eterno. Aconteceu três
vezes no mesmo dia: BO8 no PLACA, BO8 no CHA, e o controle do aposto no BOTICA.

**Segunda ocorrência, mesmo dia, forma diferente — o botão que mente.** No CHA
declarei `EIXOS_TRAVAVEIS` copiando a lista do BOTICA: `homem`, `prop`,
`substancia`, `metodo` — quatro eixos que este motor não sorteia. O cadeado
apareceria no painel e não travaria nada. Pior que cadeado ausente: o operador
confia nele. E o cadeado do `traje`, que este ângulo TEM, também não segurava —
`_por_traje` só aceitava string e a UI passa a tupla.

Nenhum dos dois apareceu no lint, no autoteste ou no pyflakes. Apareceram porque
**passei a medir o cadeado**: travar o eixo, sortear 30 vezes, conferir que o
valor não mudou. Sete eixos, sete medições. É barato e é a única prova.

---

## 30. ⛔⛔ EU CONFERI OS `IMAGE` E DECLAREI PRONTO SEM ABRIR UM `TAKE`

**O caso (PLACA e DUPLA, 2026-08-05).** De manhã consertei o PLACA, que gerava
as cenas do DUPLA (§29). Reescrevi os três `IMAGE`, medi 600 sorteios sem ERRO,
recompilei, commitei. À tarde, ao rodar a **etapa [7]** e ler o vídeo produzido,
o `TAKE 01` dizia:

> *"Her right hand keeps the dish at the same height and the same tilt. Only the
> falling scatter moves."*

Numa cena sem prato e sem despejo. E o `TAKE 02` mandava tampar o liquidificador
enquanto a `IMAGE` mostrava uma colher num caneco. O DUPLA tinha os mesmos três,
mais um `TAKE 03` falando de *"the man behind her"* numa cena de duas mulheres.

**Por que passou em 600 sorteios.** Todo linter do repo olhava **um bloco por
vez**. Nenhum comparava o `TAKE` com a `IMAGE` do mesmo bloco — e a doutrina que
isso viola estava escrita em comentário em **seis motores** e vigiada em nenhum:

> *Contradição entre IMAGE e TAKE é pior que omissão: a omissão o gerador
> preenche com o frame; a contradição ele resolve mexendo no que estava certo.*

**O que impede:** `sc.lint_take_vs_image` — cobra que o objeto citado na
**direção** do TAKE exista na IMAGE do mesmo bloco, e que `only person in the
shot` não conviva com um segundo corpo na imagem.

**As três coisas que a lente me ensinou enquanto eu a escrevia**, e cada uma foi
um falso positivo antes de ser regra:

| Versão | Acusava | Por que estava errada |
|---|---|---|
| olhar o bloco inteiro | `You already own the glass` (RESSURREICAO) | isso está na **FALA**. Direção manda desenhar; fala é o que a boca diz. Erro de categoria |
| `behind her and` como pista de pessoa | *"documents behind her and the US flag"* | pista de **posição**, não de gente |
| `beside her at frame` | cenário | idem |

> **Falso positivo é pior que lente nenhuma:** o operador aprende a ignorar a
> lente, e ela para de proteger o caso real.

**E a armadilha final, que quase me fez declarar vitória de novo.** Rodei a lente
nos 17 motores e vi **"limpo"** em quatorze. Fui conferir: **sete deles não
chamam `lint_curto`** — têm `lint()` próprio, e a lente nunca rodou neles. O
"limpo" era ausência de medição, não ausência de defeito. Ao plugar nos sete, o
DUPLA saltou de "limpo" para **200 de 200**.

> ⭐ **Medir a lente é medir TAMBÉM se ela é chamada.** Cobertura silenciosa lê
> como aprovação.

**O que ela achou fora do meu escopo:** ESCANDALO e RESSURREICAO mandam animar
*"a wooden spoon"* que não está na IMAGE. É defeito real, e o conserto é CENA —
alçada do operador. Os `.exe` dos dois **não foram recompilados**, para não
travar a produção dele com um linter que reprova antes de a decisão existir.

---

## 31. ⛔⛔ EU FIZ O BEAT ERRADO CEDER — o mecanismo virou item de lista

**O caso (CHA, 2026-08-06).** O operador leu o `TAKE 02` gerado e apontou:

> *"O centro de gravitação nosso, que é o mecanismo único `gelatin trick`, está
> apenas coadjuvante na medida em que ele é elencado durante a fala do ref no
> take 2."*

A fala saía assim:

> *"Three lemons cut open, fresh ginger, garlic, and ginkgo, the leaf off that
> ancient Chinese tree. Then boil it ten minutes, **and one gelatin trick**."*

Sete itens numa enumeração, e o `gelatin trick` era o sétimo. O espectador ouve
uma lista de compras. Mas o `gelatin trick` **é o que a VSL vende e é a palavra
que o CTA pede** — ele não pode ter o peso do alho.

**A causa foi minha, e foi de PROJETO, não de redação.** No dia anterior eu
tinha medido a cena 2 estourando o teto de 25 (o `tongkat ali` com aposto custa
10 palavras) e encurtei o pool `SEGREDOS` de 8 para 4 palavras. Ao encurtar,
matei a hierarquia:

| antes | depois | efeito |
|---|---|---|
| `and one secret I add: the gelatin trick` | `and one gelatin trick` | virou item N |

> **Eu escolhi o beat que cede pela facilidade, não pela função.** O `SEGREDO`
> era o mais fácil de encurtar e o único que não podia encolher.

**A forma que o operador escreveu à mão**, e que virou a regra:

> *"...and ginkgo, the leaf off that ancient Chinese tree **and... THE SECRET:
> the gelatin trick.**"*

Três partes, nenhuma opcional: **conjunção** que separa da lista → **rótulo com
dois-pontos** que anuncia hierarquia → **o literal**. Sem o rótulo o trick volta
a ser alho; é o rótulo que diz que o que vem depois não é ingrediente.

**De onde sai o espaço:** da RECEITA, sempre. Ordem do operador quando eu
apresentei o conflito de teto — *"retire um ingrediente da elencação então,
melhor fazer assim e manter a hierarquia"*. E a razão é boa: **o quadro já
mostra os ingredientes.** O que o quadro não mostra, e por isso só a fala pode
carregar, é o segredo.

**Onde aplica:** toda cena 2 que tem **preparo em quadro** (bancada, panela,
copo, liquidificador). Onde não há preparo, a fala não está enumerando e não há
lista da qual se destacar.

**O que impede:** `sc.lint_hierarquia_mecanismo` — só dispara quando a IMAGE da
cena mostra preparo, e cobra o rótulo com dois-pontos antes do literal.

> ⭐ **A pergunta que generaliza:** quando o teto aperta e algum beat tem de
> ceder, o que cede é o que o QUADRO JÁ CONTA. O que só existe na fala é o
> último a encolher.

---

## 32. ⛔⛔ A INTEGRAÇÃO RESPONDIA 401 DESDE SEMPRE — e o erro estava escrito para ser engolido

**Onde:** `automaweb/src/lib/buygoods.ts`, na guia Tracking do funil.
**Não é lição de agente** — está aqui porque a causa raiz é a MESMA das §29-§31,
e é aqui que ela mora.

Escrevi a integração de receita, o `tsc` passou, o painel montou, as colunas
apareceram. Declarei a construção pronta. Só quando fui **medir** é que
apareceu: a API respondia **HTTP 401 em toda chamada, desde a primeira**. Três
defeitos empilhados, e nenhum dos três fazia barulho:

1. **O token estava percent-encoded.** Foi copiado de dentro de uma URL, onde
   já vinha com `%3D` no lugar do `=` final. Como `searchParams.set` codifica de
   novo, o servidor recebia `%253D` — token errado, 401 garantido.
2. **Os nomes dos campos eram chute.** A ClickCRM devolve `subid1` e
   `conversions_count`; eu lia `subid` e `conversions`. Com o token corrigido e
   isso não, a junção daria vazio e a venda daria zero — **sem erro nenhum**.
3. **`if (!r.ok) break` devolvia lista vazia.** Este é o pior. Um 401 ficava
   visualmente **idêntico** a "não vendeu nada". O operador olharia um zero de
   cara honesta por semanas.

Os três compõem o mesmo desenho: **eu construí um caminho em que a falha tem a
mesma aparência do sucesso magro.** Zero venda é um resultado plausível num
funil novo — foi justamente essa plausibilidade que me faria aceitar o número.

**O que impede:** `prisma/conferir-buygoods.ts`, versionado. Ele não pergunta
"a chamada respondeu?", pergunta **"os 15 subids nossos existem do lado deles?"**
— e imprime `[!]` para cada página ausente. Mais: a lib agora devolve
`{dados, erro}` e o erro **sobe até a tela**, num aviso que diz que a receita
está fora e que o resto continua valendo.

> ⭐ **A pergunta que generaliza:** diante de um resultado vazio, *provei que
> está vazio, ou só constatei que veio vazio?* Antes de acreditar no parser,
> olhe a resposta CRUA. Um `[]` que veio de 401 e um `[]` que veio de "não
> houve venda" são a mesma variável em memória e coisas opostas no mundo.

> ⚠️ **Corolário de infra:** integração de terceiro que pode falhar **precisa
> de um estado de erro visível**. "Degradar sem derrubar o painel" é certo;
> "degradar sem contar a ninguém" é mentira com cara de dado.

---

## 33. ⛔⛔⛔ SETE LENTES, ZERO ACHADO — e o PRIMEIRO LOTE tinha quatro defeitos

**Onde:** FALTA, 2026-08-06, na revisão adversarial que o operador exigiu como
condição de entrega (*"não aceito drifting de copy mais hein"*).

**O que eu fiz certo, e por isso a lição dói.** O espaço de copy do agente é
finito — 288 + 288 + 24 = **600 falas**. Não amostrei: enumerei as 600. Escrevi
**sete lentes novas**, de fora do agente, depois da copy, justamente para não
repetir o vício de linter que valida o que o autor já pensou. Elas acharam
cinco defeitos reais, inclusive dois graves: a receita que abria com sintagma
nominal sem verbo em **288 de 288** combinações, e 60 falas estourando o teto
que o sorteio só escondia. Corrigi, remedi, e o painel ficou todo verde:

```
600 falas, 7 lentes            -> 0 achado
linter próprio, 2.400 sorteios -> 0 ERRO, 0 aviso
gates, deíticos, teto de fala  -> exit 0
```

**Declarei a revisão concluída.** Aí gerei **um** lote de entrega — e o prompt
saiu com quatro defeitos:

| defeito | como saía |
|---|---|
| português cru no prompt em inglês | `pours a thin steady stream over the peça anatômica` |
| dois verbos finitos na mesma oração | `the moulded shaft lies folded down against the base changes on camera` |
| ponto duplo nos quatro blocos | `not resembling any famous person..` |
| plural de elenco com ela sozinha | `the wall behind them` + `She is the only person in the frame` |

**A causa:** as sete lentes mediam a **FALA**. Nenhuma media o **BLOCO**. E o
que vai para o Veo é o bloco. Eu tinha construído um aparato de medição
impecável em cima de **uma das duas metades do produto**, e o verde dele me
convenceu de que o produto inteiro estava medido.

> ⛔ **A regra:** *cobertura de lente não é qualidade — é cobertura.* Antes de
> chamar uma revisão de completa, **listar o que a revisão NÃO olhou**. Se essa
> lista não existir, a revisão não terminou; ela só terminou onde eu parei.

> ⭐ **E o teste que expõe isso em 30 segundos: GERE UM LOTE E LEIA.** Não o
> `resumo_pt`, não as falas — o bloco inteiro, como o operador vai colar no
> gerador. Os quatro defeitos eram visíveis a olho nu na primeira leitura. Isto
> é a §30 outra vez (*"conferi os IMAGE e declarei pronto sem abrir um TAKE"*),
> num disfarce mais convincente: agora eu tinha números.

### ⛔⛔ E a lente nova nasceu cega — na mesma hora em que a escrevi

Escrevi a **FA10** para pegar o defeito nº2. Ela checava se a string montada
continha `"%s, changes on camera" % antes`. Reinjetei o defeito original
(`antes = "the moulded shaft lies folded down"`) e **ela passou**: a vírgula
continuava no lugar. Ela media a **FORMA do encaixe**, nunca a **NATUREZA do
que encaixou** — que é literalmente o vício que ela existia para pegar. Agora
mede o campo, com regex de verbo finito que **ignora particípio de propósito**
(`hanging`, `lying` são as formas que *podem* estar ali).

> ⛔ **Corolário, e ele é o mais importante desta seção:** **zero achado num
> motor já corrigido não distingue lente boa de lente morta.** Uma lente nova
> só está provada quando o defeito que a motivou é **reinjetado** e ela grita.
> Fiz isso com os quatro, mais um quinto (o mesmo defeito no outro prop): as
> cinco acusaram, o motor corrigido passou limpo. **Sem esse passo, eu teria
> commitado duas lentes decorativas e o registro escrito de que elas funcionam.**

---

## 34. ⛔⛔⛔ 16 DOS 19 APPS QUEBRARAM NA ABERTURA — e o verificador dizia tudo verde

**Onde:** `ui_agente.py`, 2026-08-06, o seletor de QUEM NARRA. Relato do
operador com print: *"Estou tentando abrir os agentes python e a maioria está
dando esse erro"* — `NameError: name 'motor' is not defined`.

**A causa, em uma linha de código:** dentro do `_topo()` eu escrevi
`getattr(motor, "SEXOS", ...)` — mas `motor` só existe como parâmetro do
`__init__`; dentro dos métodos o nome é `self.m`. Erro de iniciante, num
arquivo que eu já tinha editado dezenas de vezes.

**Por que TRÊS camadas de verificação não pegaram:**

| camada | o que ela media | por que passou |
|---|---|---|
| `verificar_entrega` | importa o motor, `sortear`/`montar`/`lint`, tradução | nunca instancia a `App` |
| `medir_trava_sexo` | a trava, 120/120, com controle negativo | chama `m.sortear(travas=...)` direto — sem UI |
| gates + lint | copy e personagem | idem |

O aparato inteiro media o **motor**, e a linha quebrada morava na **janela**.
E o pior: o CLEAN e o V2 abriam normalmente — neles `_ja_e_eixo` é verdadeiro
e o Python **nem avalia** o ramo com o nome errado. Ou seja: se eu tivesse
aberto um app para "conferir", provavelmente teria aberto o CLEAN V2 (o que eu
estava mexendo) e declarado pronto do mesmo jeito.

> ⛔ **A regra: a UI também é FUNÇÃO, e função só conta verificada onde ela
> roda.** Entrega de app passa a incluir a `sonda_ui`: instanciar
> `ui_agente.App(motor)` em cada pasta entregue, rodar `update()` + um
> `sortear()` pelo caminho da UI, destruir. 19 janelas abertas de verdade,
> não 19 motores importados.

> ⚠️ **Corolário do ramo não-avaliado:** em código com `if` por agente, o
> teste de UM agente não prova o parque — o CLEAN abria porque o ramo quebrado
> nem rodava nele. É a §18 (*"alterei código compartilhado? medi o parque
> INTEIRO"*) com um agravante: aqui "medir o parque" tem de significar medir
> **pelo caminho que o operador usa**, não pelo atalho que o medidor prefere.

---

## 35. ⛔⛔ COMPRIMI A FRASE MATANDO O SUBSTANTIVO — e escrevi um pool que repetia a mesma forma em 62%

**O que aconteceu.** No TRIO 16 escrevi `she feels the difference first`. Não
coube no teto de 25 palavras. Cortei `the difference` e entreguei
**`she feels it first`**.

O operador leu: *"fills it o QUÊ??? O clima, formigão no pé???"*

E emendou a diretriz que generaliza:

> *"concretude, ser taxativo, é melhor candidato que pronomes genéricos
> (pool de 'sua namorada', 'sua esposa') para fugir do copy drifting"*

**As duas causas, e a segunda é pior que a primeira.**

**(a) Comprimir podando o núcleo.** Quando o teto aperta, o reflexo errado é
tirar palavras da frase que já está escrita. Sai primeiro o substantivo — que é
justamente o que carrega o sentido — e fica o pronome, que é gramática. O certo
é **trocar a frase inteira por uma mais curta que ainda diz do que se trata**.
É o mesmo erro do `every morning just ginkgo` (§*drifting*): o corte parecia
economia e era amputação.

**(b) Lista única de frases prontas repete a FORMA.** Dez das minhas dezesseis
entradas abriam a segunda oração com `she`. **62% do pool com a mesma
estrutura** — e nenhum linter acusa, porque todos medem *conteúdo* (token
banido, teto, referente) e nenhum mede *forma repetida*. Mode-collapse com o
relatório verde.

**O conserto que virou método:** decompor a frase em **eixos sorteáveis** em vez
de escrever frases inteiras.

```
antes:  USOS = [16 frases prontas]                  -> 276 falas distintas/600
depois: EFEITOS(12) x PARCEIRAS(6) x REACOES(18)    -> 587 falas distintas/600
```

Com três eixos é **impossível** repetir a forma: a parceira é sempre nomeada
(pool próprio, zero pronome) e a reação vem de um pool que só aceita
**comportamento observável** (`digs her nails in`), nunca estado interno
(`is satisfied`) — o espectador compra a cena, não o adjetivo.

**A regra virou lente** (`T16-5`), porque regra que depende de eu lembrar não é
regra: reprova fala sem parceira nomeada, sentença abrindo com `She` nu, e verbo
de percepção seguido de `it` sem antecedente.

### ⛔ E o mesmo dia entregou o irmão deste defeito: **entrada de pool que nunca sai**

Medindo cobertura em 600 sorteios, **seis das dez entradas de `FOLLOWS` nunca
apareceram**. Não eram raras — eram **impossíveis**: custavam 6-7 palavras e o
orçamento real do eixo era 5 (`TETO_FALA − CTA fixo − mínimos dos outros três
eixos`). O autoteste contava dez opções; a produção tinha quatro. E as seis
mortas eram justamente as que davam a **razão** de seguir.

Nenhuma lente pegava, e o motivo é instrutivo: todas verificam a frase
**montada**, que sempre cabe por causa do fallback do `_ok`. Nenhuma verificava
se cada **entrada** é alcançável.

> **Vira controle de autoteste, não comentário.** `[ALCANCE]`: para cada eixo,
> o teto real é `TETO − partes fixas − Σ mínimos dos outros`; qualquer entrada
> acima disso reprova o lote.

**O que fazer sempre:** depois de escrever um pool sob teto de palavras, medir
**cobertura** — quantas entradas realmente saem em N sorteios — e não só se o
linter passou. Passar no linter e ter metade do pool morto é o mesmo defeito de
sempre com outra roupa: **verificar a FORMA e não a FUNÇÃO**.

---

## 36. ⛔⛔ O BEAT ORÇAVA CONTRA O PIOR CASO DE UM BEAT QUE ERA SORTEADO SOLTO DEPOIS

**A cena 3 do `receita_short` entregava DOZE falas distintas em 400 vídeos — e as
400 começavam pela mesma frase.** Não havia bug: cada linha estava aprovada, o
linter passava, o autoteste dizia OK e o `medir_teto_fala` não reclamava. O que
havia era um **orçamento pessimista**:

```python
esc  = rng.choice(_cabem(ESCALADAS,
           lambda e: "...%s..." % max(ISCAS_ENTREGA, key=_palavras), TETO))
isca = rng.choice(livres)      # <- livre, DEPOIS, sem teto nenhum
```

A escalada reservava espaço para a isca **mais longa** — e a isca era escolhida
livremente na linha seguinte, sem orçamento nenhum. Pagava-se o preço da isca de
5 palavras em **todo** sorteio, inclusive nos que usavam a de 2. Sobrevivia
**1 escalada de 10 e 2 gates de 9**.

> **Reservar o pior caso de um beat que depois se escolhe livre é pessimismo
> puro.** A ordem certa é a mesma que tirou o TROCA do corte de fala: cada beat
> filtra contra o **mínimo** dos outros, e o beat sem restrição própria é
> escolhido **dentro** do orçamento, não antes dele.

`12 → 55` falas distintas, escaladas `1 → 4`, gates `2 → 6`, teto respeitado
(máx. 25 de 25), **sem mudar uma palavra**. As seis escaladas que continuam de
fora têm 26-27 palavras no melhor caso possível — essas são copy, e copy é
alçada do operador (§CL15: descarta-se a linha, nunca se encurta a linha).

**O sintoma, para achar o próximo:** uma cena com contagem de falas distintas
**uma ordem de grandeza abaixo das vizinhas** no mesmo motor. Foi assim que este
apareceu — `368/357/12`.

### ⛔⛔ E o contra-exemplo, medido no mesmo dia: **no COLO a correção PIORA**

O `colo_short` cena 3 tem a **forma** exata do defeito — `isca = rng.choice(...)`
livre antes de qualquer orçamento, e a rotina filtrada contra `min(GATES)` em vez
do gate real. Reimplementar a correção canônica e rodar **30 seeds × 400
sorteios** derrubou as falas distintas de **145,6 para 123,2**; a variante "gate
primeiro" derrubou para 103,7.

O motivo: quando o orçamento é tão apertado que quase nada cabe, escolher o beat
livre **dentro** do orçamento concentra o sorteio nas poucas entradas curtas —
enquanto o desenho antigo espalhava por caminhos diferentes conforme a isca
sorteada. Medido: das 14 ROTINAS, com isca de 3 palavras sobrevivem 4; com isca
de 5, sobrevive **1**.

E o número que fecha a discussão, verificado à mão fora do motor:

| | cena 3 do COLO |
|---|---|
| combinações brutas (rotina × isca × gate × órgão) | **6.300** |
| que **cabem** em 25 palavras | **167** |
| que realmente saem em 400 sorteios | **151** (90,4%) |
| falas geradas acima do teto | **0** |

⛔ **97% do espaço combinatório é morto pelo teto, não pela ordem de escolha.**
Com 90% do que cabe já saindo, não existe ganho mecânico — o teto de variedade é
o **comprimento da copy**, e isso é alçada do operador.

> **A lição sobre a lição:** §36 é um padrão a **investigar**, nunca a aplicar de
> reflexo. Antes de reordenar, medir os dois mundos — quantas entradas cabem
> hoje e quantas caberiam — e **rodar as duas versões**. Achar a forma do defeito
> não é achar o defeito.

### ⚠️ E a sonda que foi caçar isso errou primeiro, do jeito de sempre

A primeira versão do `medir_alcance.py` olhava só `spec["falas"]` e **acusou 18
dos 19 motores**. Pool que alimenta os **blocos** (traje, corpo, apelo) nunca
aparece na fala — eram falsos positivos em massa. A assinatura estava visível de
longe: **pools 100% mortos em série**.

> **Lente que acusa quase todo mundo está medindo a coisa errada, não
> encontrando uma epidemia.** Antes de reportar uma varredura, olhe a taxa de
> acusação: 95% dos alvos sujos é diagnóstico da lente, não do repo.

Com falas **+** blocos, e separando as três perguntas que a mistura confundia —
(1) o pool é referenciado? (2) quantas entradas saem? (3) quantas falas
distintas por cena? — sobraram 12 de 19. Duas defesas ficaram no arquivo:
prefixo abaixo de 20 caracteres não credita entrada nenhuma, e pool `0 de N` não
é acusado (é pool que a sonda não alcança, não pool morto).

---

## 37. ⛔⛔ COBERTURA DE 100% COM O PAINEL EM INGLÊS — o medidor media o INSUMO

O verificador da camada de tradução cravava **100% de cobertura** e o operador
via frase em inglês no painel. Os dois estavam certos, porque mediam coisas
diferentes:

| medida | pergunta | resposta |
|---|---|---|
| cobertura | *todo template literal em `.py` tem PT?* | 100% — e era verdade |
| entrega | *toda fala MONTADA sai em PT?* | 95,1%, com 271 fragmentos crus |

A diferença inteira é **concatenação**. O motor não guarda a fala pronta: ele
sorteia `hook` + `mecanismo` + `prova` e cola. Nenhuma das 99 frases que faltavam
existia como literal em arquivo nenhum — elas **nascem no `montar()`**. Um
medidor que varre o código-fonte procurando strings jamais as veria, por mais
fundo que fosse a varredura, porque não é questão de amostra: é questão de estar
olhando para o lugar errado.

> **Mede-se o ENTREGÁVEL, não o insumo.** Se o operador vê a fala montada, a
> medida roda em cima da fala montada — `sortear()` → `montar()` → traduzir →
> contar. Cobertura de pool, de template ou de pedaço é diagnóstico interno, e
> nenhum número dela autoriza dizer "está pronto".

⚠️ É a mesma família do §23 e do §34, e é a **quinta** vez que um medidor meu
aprova o que o operador reprova de olho. A assinatura já é reconhecível: sempre
que a saída final é **construída** a partir de partes, medir as partes é medir
outra coisa.

### ⚠️⚠️ E depois de fechar 100%, o painel AINDA tinha inglês

Com `74.400/74.400 = 100%` medido, um dos primeiros vídeos que abri na entrega
trazia `Married men, use this. com caution` e `Comment gelatin, e recipe hits
your messages inteira`. A medição de 100% estava certa e era **irrelevante**,
porque perguntava outra coisa:

| lente | pergunta | o que deixa passar |
|---|---|---|
| exatidão | *algum molde casou a fala inteira?* | molde **errado** que casa conta como acerto |
| sobra de pool | *sobrou valor de pool em inglês?* | inglês que veio do **molde**, não do pool |
| **inglês na saída** | *tem palavra inglesa na frase?* | — é esta que o operador faz de olho |

A terceira achou **7,2% de falas sujas** onde as outras duas viam 100%.

> **Toda lente de aprovação tem que ser a pergunta que o operador faz olhando o
> resultado.** Se ele olha a frase e vê inglês, a lente pergunta "tem inglês na
> frase" — não "casou molde", que é uma pergunta sobre o mecanismo, não sobre o
> produto.

⚠️ E a lente nova errou na primeira rodada do jeito clássico do §36: acusou
**37 de 37 motores**, 25,6%. A culpa eram três palavras na lista de "inglês" que
são português — `do` (de+o), `use` (imperativo de usar) e `come` (verbo comer).
Tiradas as três, o número real era 7,2%. *Lente que acusa todo mundo está errada
antes de o repo estar.*

### ⛔⛔⛔ TRÊS GUARDAS SEGUIDOS FURADOS PELA MESMA PERGUNTA ERRADA

Fechar esses 7,2% expôs um defeito de fundo no tradutor. O guarda que rejeita
"slot que engoliu oração" perguntava, nas suas três versões, **se a saída ficou
diferente da entrada** — e molde-passagem sempre muda alguma coisa:

1. `{o}` no **fim** do molde vira `(.+?)$` e come a frase inteira
2. molde-passagem `{p}, {f}.` tem PT **idêntico** ao inglês: devolveu a frase
   crua com um ponto a mais, e "ganhou um ponto" contava como tradução
3. `{a} and {b}` devolveu `gelatin e salt into warm water` — trocou uma
   palavra, logo "traduziu"

Os três produziam o mesmo sintoma no painel: meia frase em inglês com o placar
em 100%.

> **A condição de aceite do guarda tem que ser a MESMA da lente de aceite do
> produto.** O guarda agora pergunta *"depois de traduzido, o slot ainda tem
> palavra inglesa?"* — a mesma pergunta do operador, aplicada um nível abaixo.
> Enquanto o guarda mediu "mudou?" e a lente mediu "está em português?", as
> duas nunca iam concordar.

### ⚠️ O corolário que apareceu junto: gênero não cabe no template

Com a fala montada sob a lente apareceu `na sua pepino`. O template escreve o
determinante **antes de saber** que palavra cai no slot, e o mesmo molde do COLO
recebe `banana` (f) e `pepino` (m) — não existe escolha certa na hora de
escrever. Consertar entrada por entrada seria consertar o sintoma.

> Quando o erro depende de um **valor que só existe em tempo de montagem**, a
> correção mora numa **passada depois do preenchimento**, nunca no molde. Igual
> à contração de preposição (`em aquele` → `naquele`), que nasceu do mesmo
> raciocínio.

⛔ E **não se adivinha gênero por terminação**: `-a` acerta `banana` e erra
`problema`. A passada só toca palavra com gênero **declarado** — artigo colado
no glossário ou tabela escrita à mão. Palavra desconhecida sai intacta, e o
controle negativo (`a gente vai a pé`, `ele começou a falar`, `o problema é a
idade`) roda junto com o positivo.

---

## O CHECKLIST, para colar antes de entregar agente ou alteração de motor

- [ ] **Gerar UM lote e LER o bloco inteiro**, como o operador vai colar no
      gerador — não o `resumo_pt`, não só as falas (§33). Os defeitos de prompt
      não aparecem em nenhum medidor de copy porque nenhum medidor de copy olha
      para lá
- [ ] **Lente nova? Reinjete o defeito que a motivou e veja-a gritar** (§33).
- [ ] **Escreveu `.py` por heredoc? Varra bytes de controle** (§37). `\b` e `\1`
      dentro de heredoc não-citado chegam ao arquivo como `\x08` e `\x01`. O
      Python compila, o editor não mostra nada, e o regex simplesmente **nunca
      casa** — no caso real, um `^(naquele|aquela|…)\x08` deixava `this store`
      sair como *"aquela loja"* em vez de *"esta loja"*: português plausível,
      dêitico invertido, invisível para qualquer medidor de cobertura.
      `[i for i,c in enumerate(open(f,'rb').read()) if c<9 or 13<c<32]`
      Zero achado num motor já corrigido não distingue lente boa de lente morta
- [ ] `python -m pyflakes <motor>.py` — saída **vazia**
- [ ] **400 sorteios** pelas 5 páginas, `sortear → montar → lint`, **0 ERRO medido**
- [ ] `python funil-organico/medir_teto_fala.py --curva --motor <nome>` —
      **nenhuma cena acima de 25 palavras**, e o `min` de cada cena **≤ 25**.
      ⛔ Ordem permanente do operador: *"não pode haver cortes de fala"*. Uma
      fala cortada mata o CTA, e o vídeo inteiro deixa de converter
- [ ] `python funil-organico/medir_deiticos.py --motor <nome>` — **zero** achado
      nas três famílias de drifting (§24)
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
- [ ] **Nenhuma sentença de percepção/reação sem o órgão nela** — `She noticed.`
      faz o espectador perguntar *"notou o quê?"* e a prova social morre em
      silêncio. Verbo de reação e `NUCLEO` na MESMA sentença (§20)
- [ ] ⭐ **TESTE WTF, sentença a sentença, lida ISOLADA** (§21): se dá para o
      espectador perguntar *"do que ele/ela está falando?"*, é **descarte** de
      copy, não conserto. Vale principalmente para a **PRIMEIRA** sentença de
      cada cena — é ela que decide se ele fica, e era a única que nenhuma
      lente minha olhava
- [ ] ⭐ **Li a LISTA DE TOKENS que a minha lente aceita, item por item, e
      perguntei de cada um "isto cumpre a função?"** (§22). `they` como "agente
      nomeado" fez a lente carregar o vício que existia para pegar. O controle
      positivo inclui a forma **quase-certa**, não só a obviamente errada
- [ ] **Escrevi regex por EDIÇÃO LITERAL, nunca por script com escape** (§22):
      `\b` num heredoc vira BACKSPACE (0x08), invisível no diff, e o padrão
      passa a exigir um caractere que não existe
- [ ] Uso do orçamento medido contra a **capacidade real**, não contra o teto (§5)
- [ ] **Li algumas falas inteiras renderizadas**, não só os pools
- [ ] `git diff` conferido: nenhuma string validada redigitada sem ordem
- [ ] **Mexi em copy? A tradução PT saiu junto**, e eu **li duas falas
      renderizadas inteiras** — não confiei só no número (§18)
- [ ] **Consertei um verificador? Procurei o MESMO bug no código que ele
      verifica** — lente consertada não conserta o objeto (§18)
- [ ] **Alterei código compartilhado? Medi o parque INTEIRO**, não só o agente
      que motivou a mudança (§18)
- [ ] **Conferi a frase no PROMPT MONTADO, não no `.py`** — `grep` no fonte não
      vê string quebrada entre linhas adjacentes (§19)
- [ ] **Declarei 100%? Rodei em DOIS patamares de amostra e vi convergir** —
      100% de 60 sorteios escondeu 11 templates sem tradução (§23)
- [ ] **A cena 2 mostra preparo?** Então o `gelatin trick` vem com rótulo e
      dois-pontos, nunca como item da enumeração (§31)
- [ ] **Algum beat teve de ceder pelo teto?** Cedeu o que o QUADRO JÁ
      CONTA — não o que só existe na fala (§31)
- [ ] **Li os três `TAKE` inteiros**, não só os `IMAGE` — cada TAKE anima a
      SUA cena e nenhuma outra (§30)
- [ ] **A lente nova é CHAMADA pelo motor?** Sete motores têm `lint()`
      próprio e não passam pelo `lint_curto` — "limpo" neles pode ser
      ausência de medição (§30)
- [ ] **`resumo_pt` descreve ESTE vídeo?** É o texto que o operador lê para
      aprovar em dois segundos; herdado, faz ele aprovar o que não viu
- [ ] **Motor copiado?** As três listas do §29 percorridas: toda `BO_*` de
      cena, toda regra do `lint()`, toda sonda do `autoteste()`
- [ ] **Cada cadeado MEDIDO** — travar o eixo, sortear 30×, conferir que não
      mudou. Botão que mente é pior que botão ausente (§29)
- [ ] **Cada eixo de `EIXOS_TRAVAVEIS` existe no spec** — herdado da cópia,
      ele desenha cadeado para eixo que o motor não sorteia
- [ ] **Cobertura de pool MEDIDA**, não contada no código: sortear 600× e ver
      quantas entradas de cada eixo realmente saem. Entrada que não cabe com os
      mínimos dos outros eixos está morta e o autoteste conta como viva (§35)
- [ ] **Nenhum pronome genérico na copy falada** — `she`/`it` sem dono é
      drifting. A parceira é NOMEADA (pool próprio), e comprimir a frase nunca
      pode podar o substantivo que carrega o sentido (§35)
- [ ] **A forma do pool varia?** Contar quantas entradas abrem a segunda oração
      do mesmo jeito. Acima de ~30% é mode-collapse, e nenhum linter acusa (§35)
- [ ] ⭐ `python funil-organico/medir_alcance.py --motor <nome>` — e **comparar
      as falas distintas de cada cena entre si**. Cena uma ordem de grandeza
      abaixo das vizinhas (`368/357/12`) é orçamento pessimista, não copy
      pobre (§36)
- [ ] **Nenhum beat orça contra o MÁXIMO de outro beat** — se o outro é
      escolhido livre depois, paga-se o pior caso em todo sorteio. Cada beat
      filtra contra o **mínimo** dos outros, e o beat sem restrição própria é
      escolhido **dentro** do orçamento (§36)
- [ ] ⛔ **Achou a forma do §36? RODE AS DUAS VERSÕES antes de trocar.** No COLO
      a correção canônica derrubou as falas distintas de 145,6 para 123,2 em 30
      seeds. Compare também **combinações que cabem** × **combinações que saem**:
      acima de ~90% de cobertura não há ganho mecânico nenhum, o teto é a copy
- [ ] **Varredura acusou quase todos os alvos? A lente está errada** — 18 de 19
      motores sujos foi diagnóstico da sonda, não do repo. Olhar a taxa de
      acusação **antes** de reportar (§36)
- [ ] `.exe` **recompilado** — sem isso a correção não chega no operador
- [ ] **Mexi na `ui_agente`? A `sonda_ui` abriu as 19 JANELAS** — motor
      importado não prova painel construído, e ramo por agente esconde o
      NameError dos agentes que não o executam (§34)
- [ ] Se houve subagente: **estado do disco conferido**, não o relatório dele

---

## Conexões

- [`licoes-producao-veo.md`](licoes-producao-veo.md) — as lições pagas com render recusado
- [`../PIPELINE-NOVO-AGENTE.md`](../PIPELINE-NOVO-AGENTE.md) — o pipeline, com o §[9] "aceite é medição"
- [`RUNBOOK-app-offline.md`](RUNBOOK-app-offline.md) — motor → app → `.exe`, e por que recompilar
- [`../CLAUDE.md`](../CLAUDE.md) — a alçada: copy e cena são do operador
