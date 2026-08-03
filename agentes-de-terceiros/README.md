# ⛔ AGENTES DE TERCEIROS — FORA DO NOSSO ESCOPO

> **Não leia, não meça, não conserte, não cite.** Para efeito de qualquer
> trabalho neste repo, os arquivos desta pasta **não existem**.

Ordem do operador em **2026-08-03**:

> *"Separe tudo que tem label `lucas` de nós. Quando eu sequer mencionar de
> melhorarmos ou fazer algum ajuste nos agentes, eu sempre estarei me referindo
> aos agentes do tipo SHORT (sem label lucas). Esses agentes com label `lucas`
> nunca sequer entrarão no escopo de leitura nossa: devem ser tratados como
> inexistentes para nós — eles são de um amigo meu que resolveu arquitetar os
> agentes de outra forma."*

## O que tem aqui

Quatro agentes de **arco longo (5 cenas)**, com a arquitetura do autor original:

| arquivo | ângulo |
|---|---|
| `flagrante_lucas.py` | humilhação pública |
| `pee_lucas.py` | a mancha pública |
| `vazamento_lucas.py` | o corpo-prova e a receita incompleta |
| `necrose_lucas.py` | os dois órgãos lado a lado |

Mais o `_app.py` de cada um. Os `.exe` correspondentes seguem na área de
trabalho do operador (`Desktop\agentes_py\FLAGRANTE`, `NECROSE`, `PEE`,
`VAZAMENTO`) e **continuam funcionando** — ele pediu para mantê-los como estão.

## ⭐ A nossa fonte da verdade é outra

Os agentes deste funil são os **`*_short.py`** em
[`../funil-organico/`](../funil-organico/) — 3 cenas de 8s, destino AdBatch
Vertical 3. São eles que entram em escopo de leitura, medição e melhoria.

**Nove, e nenhum depende desta pasta:** `clean_short` · `escandalo_short` ·
`troca_short` · `organicwave_short` · `ressurreicao_short` · `flagrante_short` ·
`pee_short` · `vazamento_short` · `necrose_short`.

## ⚠️ Como esta separação foi feita, e por que ela é segura

Até 2026-08-03 quatro SHORT faziam `import <agente>_lucas as base` e herdavam
daqui strings travadas, pools e tabelas de linter — mover a pasta os quebraria
na hora. Antes de mover, cada um recebeu **cópia literal** do que herdava e
ficou autossuficiente.

Duas provas rodadas antes do commit, e nenhuma delas é relato:

1. **Importação bloqueada** — um `meta_path` finder que levanta `ImportError`
   para todo `*_lucas`; os **9 SHORT importam e rodam 20 sorteios com 0 ERRO**.
2. **Equivalência bit a bit** — 200 vídeos por motor com o mesmo seed, antes e
   depois, comparando o SHA-256 do texto montado inteiro:

   | motor | hash |
   |---|---|
   | `flagrante_short` | `e8f10574984cf513…` **idêntico** |
   | `pee_short` | `14600a31770cbe96…` **idêntico** |
   | `vazamento_short` | `b3b3b9917f63902b…` **idêntico** |
   | `necrose_short` | `d561374598b0728a…` **idêntico** |

   O refactor não mudou um caractere do vídeo gerado.

⛔ **Não volte a importar daqui.** Correção de regra de um ângulo entra no
`<angulo>_short.py`, que é a fonte da verdade.
