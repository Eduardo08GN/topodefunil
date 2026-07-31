# WORKFLOW — Operação Funil Orgânico ED (US)

**Ponto de entrada do repositório.** Se você é um agente chegando nesta conversa do
zero, leia este arquivo inteiro antes de tocar em qualquer coisa. Ele diz o que a
operação é, como se produz, o que é inviolável e o que está pendente.

- **Última atualização:** 2026-07-27
- **Repo de operação (este):** `Eduardo08GN/topodefunil` — doutrina, agentes, runbooks
- **Repo de código:** `Eduardo08GN/projetosweb` — bridge pages + ferramentas Flow

---

## 1. O QUE É A OPERAÇÃO (30 segundos)

Funil orgânico de nutra, nicho ED / men's wellness, mercado US, **tráfego 100% orgânico**
(reels no Facebook, sem anúncio pago).

```
1 perfil (Eduardo Nogueira)
  → 5 páginas de fãs
    → reel com "Comment GELATIN"
      → automação Comentário→DM entrega o link
        → bridge page (domínio próprio)
          → VSL de afiliado (Horsewood ou Ragnaroak)
            → comissão BuyGoods
```

Mapa completo em [`funil-organico/ARQUITETURA-OPERACAO.md`](funil-organico/ARQUITETURA-OPERACAO.md).

### As 5 páginas

| Página | Domínio | VSL | Etnia do avatar |
|---|---|---|---|
| Joe's Wellness Hub | `manresethub.pro` | Horsewood | branco |
| Marcus' Men Reset Hub | `vitalresetlab.site` | Horsewood | **negro** |
| Ray's Natural Vitality Hub | `primalvitalityhub.site` | Horsewood | branco |
| Chuck's Men Welness Hub | `allmensnatural.site` | Ragnaroak | **negro** |
| Matt's Natural Reset Tips | `steadystrengthhub.site` | Ragnaroak | branco |

Split 3 Horsewood (aff 45158) / 2 Ragnaroak (aff 2470). **As duas VSLs vendem o mesmo
mecanismo: gelatin trick.** Por isso todas as 5 páginas postam criativo de gelatin.

---

## 2. PIPELINE DE PRODUÇÃO DE CRIATIVO

Meta operacional: **~50 vídeos/dia sem repetição de conteúdo.**

### Passo 1 — Sortear a spec (OBRIGATÓRIO)

```bash
python funil-organico/randomizador-v6.py --pagina joe --n 50
```

Nunca escreva um vídeo sem uma linha de spec. O agente **executa** a combinação
sorteada — não escolhe, não prefere, não repete a última. Isso existe porque modelo de
linguagem tem mode-collapse: solto, ele gravita pro mesmo protótipo.

Flags: `--espinha A|B|C` · `--molde M1_substancia_absurda` · `--dry-run` · `--stats`
· `--listar` · `--reset-ledger`.

O randomizador tem **ledger persistente** (`.ledger-v6.json`, fora do git): nunca repete
uma assinatura de hook já emitida e prefere os valores menos usados de cada eixo.
Espaço combinatório: **129.024 hooks** = 2.580 dias a 50 vídeos/dia.

### Passo 2 — Gerar o roteiro com o Agente V6

> 🎬 **Nunca escreveu prompt de Veo antes? Leia primeiro a
> [`DOUTRINA-VEO-3.1.md`](recursos/DOUTRINA-VEO-3.1.md)** — como o modelo se comporta,
> por que ele alucina mão extra / prop flutuando / legenda embaralhada, e a tabela de
> sintoma → causa → fix. É o documento mãe do Veo.

[`AGENTE_ED_ORGANIC_WAVE_V6.md`](AGENTE_ED_ORGANIC_WAVE_V6.md) — o agente de produção atual.

- **Cena 1 (hook):** monta do molde da spec + substância + prop + promessa, com o
  modificador de autoridade colado. Vem do [`banco-hooks.md`](funil-organico/banco-hooks.md).
- **Cenas 2-5 (corpo):** **copiadas** da [`espinha-fixa.md`](funil-organico/espinha-fixa.md),
  nunca reescritas.
- **REF:** solto, sorteado por vídeo (`REF solto` na spec do randomizador) —
  só a etnia é travada pela página (regra 3.4).

Saída: `REF 01` + 5 blocos `IMAGE 01/05..05/05` + 5 blocos `TAKE 01/05..05/05`.

### Passo 3 — AdBatch Vertical 5 (Google Flow)

Cola o roteiro, gera as 5 imagens (com o REF em Consistência Visual), depois os 5 vídeos
(Veo 3.1 Lite, 8s, I2V com a imagem como frame inicial), baixa o ZIP.

Código: `projetosweb/ferramentas/adbatch-vertical-5/`. Prompt de cada cena é **editável
direto no card** nas duas etapas — corrigir uma palavra numa cena e usar "Regerar" só
naquele slot, sem re-colar o roteiro de 25k na sidebar.

### Passo 4 — Veo Editor

Junta, desilencia, varia velocidade, legenda karaokê com a keyword destacada.

### Passo 5 — Postar

Reel na página → keyword no comentário → DM automática entrega o link da bridge.

---

## 3. REGRAS INVIOLÁVEIS

Quebrar qualquer uma destas já custou lote refeito ou conta em risco.

### 3.1 Congruência de mecanismo
O mecanismo do criativo casa com o que a VSL daquela página vende. Hoje: **gelatin em
todas as 5**. Criativo de um mecanismo levando pra VSL de outro mata a conversão.

### 3.2 Congruência de casting/etnia
A etnia do REF casa com a etnia do avatar da página. Avatar negro recebe **só** REF
afro-americano US (homem e parceira). Cruzar denuncia a operação como fabricada.

### 3.3 CTA travado em GELATIN
A automação Comentário→DM das 5 páginas só dispara nas variantes de gelatin (`gelatin,
gelatine, jelatin, gelatn, gelati, gellatin, gelatim, gelantin, geltin, gelaton`).
⛔ **`BOOK` e `YES` são proibidos** — o randomizador v6 nem oferece. Já custou um lote.

### 3.4 REF solto por vídeo (política revertida em 2026-07-28)
**Cada vídeo sorteia um REF novo e aleatório** — o randomizador PRISMA emite
`REF solto: idade/marca/físico` na spec. A regra anterior (um REF fixo por página)
foi revogada por decisão do operador. O que fica inegociável é a **congruência de
etnia** (regra 3.2): página de avatar negro → só REF afro-americano US.

### 3.5 As regras mecânicas do Veo moram no V4 — e só lá

⛔ **Este documento não reproduz regra mecânica.** Elas viviam duplicadas aqui, no V6 e
no V4; o V4 mudou em 2026-07-28 e as cópias passaram a mandar fazer o formato antigo.
**Uma regra, um lugar:** [`AGENTE_ED_ORGANIC_WAVE_V4.md`](AGENTE_ED_ORGANIC_WAVE_V4.md).

O que vive lá, em uma linha cada:

| Regra | Ataca |
|---|---|
| **TAKE é I2V — não re-descreva a persona**, 80-150 palavras | morphing, 3ª mão, prop sumindo |
| Fala = `says: "..."` (verbo + dois-pontos + aspas) | lip-sync |
| Rótulos `Dialogue:` / `Audio:` em linha própria | áudio ausente |
| Orçamento de mãos — uma ação por cena, mão ociosa parada | 3ª mão |
| Amarração do prop + `no floating objects` | prop flutuando/sumindo |
| Câmera no início do prompt, luz travada verbatim | câmera ignorada, luz derivando |
| Fechamentos anti-legenda no IMAGE **e** no TAKE | legenda queimada |

**Exceção — o selo de risco de bloqueio** não é regra mecânica, é dado de produção, e
vive no [`banco-hooks.md`](funil-organico/banco-hooks.md): H9 (proxy na virilha) está
**banido**, H4 só sem "absurdly oversized" e sem "perform". **Toda recusa nova se
registra lá.**

### 3.6 A correção das aspas (2026-07-28)

Uma leva de doutrina mandou **tirar as aspas** da fala, culpando-as pela legenda
embaralhada. **Estava errado e foi revertido.** A referência do Veo confirma que o verbo
de fala + aspas é o que alimenta o lip-sync — tirar as aspas conserta a legenda e
arrebenta a sincronia labial. A forma correta é `He says: "..."`. Detalhe no V4.

---

## 4. COMO EXPANDIR O REPERTÓRIO ⭐

**Este é o loop de crescimento da operação.** Sempre que o Ed garimpar uma página nova
de concorrente, ele invoca a skill e solta o link:

```
/watch https://www.facebook.com/profile.php?id=<ID_DA_PAGINA>
```

### O que o agente faz com isso

1. **Enumerar os reels.** Facebook exige login para listar — use o Chrome do usuário
   (`mcp__claude-in-chrome__`), navegue até `?sk=reels_tab`, role e extraia os hrefs:
   ```js
   [...new Set([...document.querySelectorAll('a[href*="/reel/"]')].map(a=>a.href.split('?')[0]))]
   ```
   `yt-dlp` sozinho não passa do login na página de perfil.

2. **Puxar os transcripts em modo barato.** Frames custam caro e o que interessa é a
   copy:
   ```bash
   python <SKILL_DIR>/scripts/watch.py "<url_do_reel>" --detail transcript
   ```
   No Windows use `python`, não `python3`.

3. **Separar o que varia do que não varia.** Compare os reels entre si. A pergunta certa
   não é "quais ângulos eles têm" — é **"o que é idêntico entre os vídeos e o que muda"**.
   Foi assim que descobrimos que o Kofi&Simba tem 1 história e 11 hooks.

4. **Destilar na fórmula** e escrever em [`banco-hooks.md`](funil-organico/banco-hooks.md):
   ```
   HOOK = [MOLDE] + [SUBSTÂNCIA] + [PROP] + [MODIFICADOR] + [PROMESSA]
   ```
   Molde novo vira seção nova (M15, M16…) com **linhas literais**, não só template.
   Anotar views/reactions quando visíveis — é o que ordena os moldes por performance.

5. **Ampliar os pools** no [`randomizador-v6.py`](funil-organico/randomizador-v6.py):
   `MOLDES`, `POOLS["substancia"]`, `POOLS["prop"]`, `POOLS["modificador"]`,
   `POOLS["promessa"]`. Todo molde novo precisa de entrada em `DISPOSITIVO_POR_MOLDE`.

6. **Limpar os temporários:** `rm -rf /c/Users/edlut/AppData/Local/Temp/watch-*`

### Páginas já digeridas

| Página | Quando | O que rendeu |
|---|---|---|
| **Kofi&Simba** (20K, Houston) | 2026-07-27 | 11 reels → moldes M1-M8 + os 2 modificadores de autoridade + a espinha isca-e-troca. Mesma keyword `gelatin` que a nossa. |
| Corpus de 13 (8 baseline + 5 seeds) | anterior | Biblioteca de dispositivos H1-H10 / M1-M7 (Apêndice A do V5) |
| 42 análises de signature | anterior | [`prop-metaforas.md`](funil-organico/prop-metaforas.md), [`signature-matriz.md`](funil-organico/signature-matriz.md) |

---

## 5. MAPA DE ARQUIVOS

### Agentes (raiz)
| Arquivo | Papel |
|---|---|
| `AGENTE_ED_ORGANIC_WAVE_V6.md` | ⭐ **agente de produção atual** — hook-first |
| `AGENTE_ED_PRISMA_V1.md` | lote heterogêneo por construção — 10 eixos + solver de distância |

### Agentes especialistas por ângulo (desmembramento 2026-07-28)

Um agente por ângulo, todos enxutos (regras próprias + mecânica por ponteiro).
O PRISMA sorteia; o especialista do ângulo sorteado executa.

| Agente | Ângulo | Evidência |
|---|---|---|
| `AGENTE_ED_FLAGRANTE_V1.md` | humilhação pública (M15) | 20-50x a média (Tanisha) |
| `AGENTE_ED_GEMEO_V1.md` | antes/depois gêmeo (M6) | ⭐ **345K — o recorde** (Zariah) |
| `AGENTE_ED_RESSURREICAO_V1.md` | despejo → prop ressuscita (H6/H7/P17) | Tanisha 1.6K, IA aprovada na moderação |
| `AGENTE_ED_DEMO_QUIMICA_V1.md` | a reação química é a prova (M4/E5) | 7.1K/5K/4.3K |
| `AGENTE_ED_SUBSTANCIA_ABSURDA_V1.md` | comando impossível (M1/M8) | 18K — top Kofi&Simba |
| `AGENTE_ED_DIAGNOSTICO_V1.md` | "this is you" — tríade/contrastes (M3/E8) | 10K |
| `AGENTE_ED_CONSEQUENCIA_V1.md` | ruína anunciada + exposé (M2/M14/E6) | 13K |
| `AGENTE_ED_ELA_NARRADORA_V1.md` | voz feminina (M11/E3) | 🟡 piloto |
| `AGENTE_ED_CONFISSAO_V1.md` | confissão crua 1ª pessoa (M9/M13/E4) | 🟡 piloto |
| `AGENTE_ED_DIARIO_V1.md` | Day 0 → Day 7 (M12/E7/H2) | 🟡 piloto |
| `AGENTE_ED_GUERRILHA_V1.md` | set público — loja/POV (H5) | 🟡 piloto |
| `AGENTE_ED_CONSULTORIO_V1.md` | diagnóstico ao vivo — paciente-evidência + marcador de estado (Tanisha, mapeamento frame a frame 2026-07-28) | 🟡 piloto — top da fonte: 2.3K comments |
| `AGENTE_ED_PEE_V1.md` | **a mancha pública** — incontinência flagrada no corredor da loja; sub-ângulo do FLAGRANTE, cenas 2-5 herdadas dele | ⭐ **fonte: 1.5K/583/311, 20-50× a média** (reel fundador do M15) |
| `AGENTE_ED_ELA_DIAGNOSTICA_V1.md` | **REF feminina** cravando o dedo no abdômen do paciente, com alarme no rosto — as 3 inversões do CONSULTORIO (mulher / barriga como evidência / alarme em vez de calma) | 🟡 piloto — reel 1022316587192809 |
| `AGENTE_ED_VAZAMENTO_V1.md` | **o corpo-prova e a receita incompleta** — REF musculoso segurando o geoduck gigante e mole que **vaza**, receita de supermercado (`gelatin + baking soda`) que ele mesmo declara incompleta sem o `gelatin trick`. Solo, dois settings | 🟡 piloto — fonte Kofi&Simba reel 1555163349606149: **703/254/36** (254 comentários = KPI do funil) |
| `AGENTE_ED_UNCAO_V1.md` | **a mão dela, o cubo e a ressurreição na tela** — REF feminina 30+ esfregando cubos de gelatina pronta no sifão do geoduck, que endireita dentro do take; payoff é o homem dela exibindo num evento social com mulheres boquiabertas. Único ângulo em que o mecanismo TOCA o proxy | 🟡 piloto — **comissão do operador 2026-07-30, sem leitura ótica**. Selo de risco mais alto do repertório (fila de reformulação no agente) |
| `AGENTE_ED_NECROSE_V1.md` | **os dois órgãos lado a lado** — dois modelos anatômicos 3D em pedestal de aço, um **apodrecido** e um **são**, nas mãos de um montanhês de tronco nu com um **lobo** atrás, no topo de uma montanha nevada. O contraste é em **cinco eixos** (cor, superfície, volume, contorno, eixo), nunca em tamanho. Antes/depois do ÓRGÃO, sem corpo, sem vítima, sem plateia — o ângulo mais barato de produzir do repertório | 🟡 piloto — fonte Alaskan Mountain Men Tips reel 1740829770294515: **1.9K/307/103**. Leitura ótica do hook 2026-07-30 |

⛔ `fake_broadcast` foi **removido** do pool de conceitos (ordem do operador,
2026-07-28 — risco de ban). Micro-hooks do V5 renomeados **M1-M7 → D1-D7**
(colisão de namespace com os moldes). `dispositivo=nenhum` extinto (P18).
| `AGENTE_ED_ORGANIC_WAVE_V5.md` | biblioteca de dispositivos H1-H10 / M1-M7 + templates Veo (Apêndice C) |
| `AGENTE_ED_ORGANIC_WAVE_V4.md` | **o motor** — regras de IMAGE/TAKE, estética, anti-glitch, formato |
| `AGENTE_ED_ORGANIC_WAVE_V3/V2.md` | histórico, não usar |

O V6 herda o motor do V4 e a biblioteca do V5. Correção de regra mecânica entra **no V4**
e vale para todos.

### Criativo
| Arquivo | Papel |
|---|---|
| [`recursos/DOUTRINA-VEO-3.1.md`](recursos/DOUTRINA-VEO-3.1.md) | ⭐ **documento mãe do Veo** — comportamento do modelo, sintaxe, tabela de falhas |
| [`funil-organico/banco-hooks.md`](funil-organico/banco-hooks.md) | o que varia — 15 moldes, ~100 hooks literais, selo de risco |
| [`funil-organico/espinha-fixa.md`](funil-organico/espinha-fixa.md) | o que não varia — 3 espinhas validadas + CTA + persona por página |
| [`funil-organico/randomizador-v6.py`](funil-organico/randomizador-v6.py) | sorteador hook-first com ledger |
| [`funil-organico/banco-copy-agressiva.md`](funil-organico/banco-copy-agressiva.md) | munição bruta, 325+ linhas (seções A-X) |
| [`funil-organico/prop-metaforas.md`](funil-organico/prop-metaforas.md) | catálogo de props e o arsenal expandido |
| [`recursos/generated-ai-video-anti-irrealidade-checklist.md`](recursos/generated-ai-video-anti-irrealidade-checklist.md) | guardrail de prompt Veo |
| [`hooks/`](hooks/) | teoria — hooks viciosos, biblioteca de formatos, curiosity loops |

### Infra
| Arquivo | Papel |
|---|---|
| [`funil-organico/ARQUITETURA-OPERACAO.md`](funil-organico/ARQUITETURA-OPERACAO.md) | ⭐ **fonte da verdade operacional** — página → domínio → VSL → aff_id |
| [`funil-organico/PENDENCIAS.md`](funil-organico/PENDENCIAS.md) | backlog técnico detalhado |
| [`funil-organico/README.md`](funil-organico/README.md) | índice do pilar (⚠️ visão de negócio é de planejamento) |
| [`veo-editor/README.md`](veo-editor/README.md) | manual da esteira do Passo 4 |
| [`funil-organico/RUNBOOK-deploy-coolify.md`](funil-organico/RUNBOOK-deploy-coolify.md) | **ler antes de subir qualquer página** |
| [`funil-organico/bridge-pages-deploy.md`](funil-organico/bridge-pages-deploy.md) | inventário de domínios e apps |
| [`funil-organico/bridge-pages-arquitetura.md`](funil-organico/bridge-pages-arquitetura.md) | pastas, receitas, contrato do link |
| [`funil-organico/automacao-comentario-dm.md`](funil-organico/automacao-comentario-dm.md) | keywords + congruência da cadeia |
| [`funil-organico/RUNBOOK-watch-videos.md`](funil-organico/RUNBOOK-watch-videos.md) | mineração de vídeo |

VPS `159.195.12.135`, Coolify, Traefik+SSL. Cada bridge aponta **direto** pra sua VSL
(sem redirecionador central — um porteiro único mandaria Chuck e Matt pro aff errado).

---

## 6. PENDÊNCIAS

Ver também [`funil-organico/PENDENCIAS.md`](funil-organico/PENDENCIAS.md).

| # | Item | Prioridade |
|---|---|---|
| 1 | **Rotacionar o token da API do Coolify** — foi exposto em chat | 🔴 alta |
| 2 | ~~Travar os 5 REFs de persona~~ — **obsoleto**: política mudou para REF solto por vídeo (2026-07-28) | ✅ resolvido por mudança de política |
| 3 | Automação Comentário→DM em **Marcus, Ray e Chuck** (kit pronto) | 🟡 |
| 4 | Subir o AdBatch atualizado pro Flow (código pronto em `projetosweb`, falta colar no builder) | 🟡 |
| 5 | Persistência do `vendas.jsonl` (volume no Coolify) | 🟡 |
| 6 | Postback de reembolso BuyGoods | 🟢 |
| 7 | `wholelifenutri.shop` ainda em parking | 🟢 |

---

## 7. PARA O AGENTE QUE CHEGA AGORA

Ordem de leitura recomendada:

1. Este arquivo
2. [`funil-organico/ARQUITETURA-OPERACAO.md`](funil-organico/ARQUITETURA-OPERACAO.md) — o mapa
3. `AGENTE_ED_ORGANIC_WAVE_V6.md` + `V4` — se for gerar criativo
4. [`funil-organico/RUNBOOK-deploy-coolify.md`](funil-organico/RUNBOOK-deploy-coolify.md) — se for mexer em página

**O erro mais comum:** improvisar a copy do corpo do vídeo. A espinha é ativo validado —
copie, não reescreva. Toda a variação mora no hook, e o hook vem do randomizador.
