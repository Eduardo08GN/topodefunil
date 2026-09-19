# Organic Wave Studio — v3

**Versão de referência:** `37182cc` · 2026-09-19
**Repositório da ferramenta:** `Eduardo08GN/ogtoolsv2`, branch `v3`
*(este arquivo é só o registro da versão; o código vive lá)*

---

## O que a v3 é

Uma esteira contínua que transforma vídeos de origem em vídeos finais legendados, sem que
ninguém precise ficar na frente do computador. A promessa é literal: **a pessoa põe 50, 100
ou 200 vídeos na fila, vai dormir, e volta com os vídeos prontos.**

Um comando faz tudo:

```
python v3/rodar.py --raiz <pasta da leva> --fontes <pasta dos vídeos> --cta <palavra>
```

## A arquitetura, em uma página

**O livro.** Cada leva tem um `_livro.json` que é a única verdade sobre o estado de cada vídeo
e de cada take. Toda mudança de estado passa por uma porta só (`marcar`), e cada mudança grava
em disco na hora — por isso a esteira pode morrer a qualquer instante sem perder trabalho.

**Sete tarefas vivas, um livro só.** Preparo, descrição, produção, colheita, montagem, painel e
player rodam ao mesmo tempo sobre a mesma leva. Nenhuma espera a outra terminar: enquanto um
vídeo está sendo gerado, outro está sendo montado e um terceiro está subindo âncoras.

**Transporte não é veredito.** Falha de rede, daemon mudo, upload que não completou — nada disso
gasta a chance do take. Só a recusa real do gerador conta como tentativa. Um take que esgota as
chances volta para uma segunda volta quando a fila esvazia.

**O vigia (novidade desta versão).** O comando acima sobe um **supervisor**, que por sua vez sobe
a esteira como processo filho e a mede pelo livro — por **produção**, não por sinal de vida:
takes prontos, operações enviadas ao gerador e vídeos finais, três contadores que só sobem.

| situação | o que o vigia faz |
|---|---|
| 20 min sem nenhum contador subir, com trabalho na fila | aposenta os daemons do navegador |
| mais 10 min sem avanço | mata a esteira e sobe outra |
| livro 6 min sem ser escrito, esteira viva | reinicia na hora |
| esteira morreu com leva inacabada | sobe outra |
| vigia reiniciado com esteira viva | **adota** a esteira — produção não para |
| só o operador (`--parar` / Ctrl-C) | encerra |

**Por que o supervisor é um processo separado:** a falha que motivou tudo isto foi uma esteira
que ficou viva e não conseguia mais criar processos filhos. Ela não teria como se reiniciar.
Quem cura precisa estar de fora.

## Por que o vigia existe — a noite de 19/09/2026

Uma leva de 71 vídeos rodava enquanto o operador dormia. Das 02:36 às 05:32 a esteira ficou
**viva e improdutiva**: respondia, escrevia o livro a cada ciclo, e todo pedido ao navegador
falhava na criação do processo. Três horas, 67 takes perdidos, zero vídeos entregues.

A lição virou regra de arquitetura: **estar viva não é estar produzindo.** Nada que meça pid,
uso de CPU ou data de modificação teria visto aquilo — só contadores de produção veem.

Depois que o vigia assumiu, a mesma leva rodou **3 h 34 sem travar uma única vez** (zero curas,
zero reinícios) e saiu de 14 para 66 vídeos entregues.

## Resultado medido — leva de 71 vídeos

| | |
|---|---|
| entregues | **66 de 71** (422 MB) |
| takes gerados | 223 |
| operações enviadas ao gerador | 227 |
| melhor ritmo sustentado | 0,87 take/min com 2 contas |
| curas / reinícios do vigia após a correção | 0 / 0 |
| não entregues | 4 por recusa de conteúdo do gerador nas duas voltas · 1 barrado no portão |

## O que entrou nesta versão

| commit | o quê |
|---|---|
| `37182cc` | vídeo barrado no portão não conta como trabalho pendente (vigia e esteira com um critério só) |
| `243ed50` | o vigia adota a esteira viva em vez de matá-la |
| `ba57d5a` | a diretriz-mor no `CLAUDE.md`: viva ≠ produzindo |
| `9e41fb8` | **o vigia**: supervisor que mede produção, e o sensor rápido de daemon mudo |
| `28567c7` | take preso a uma conta doente troca de faixa depois de 3 falhas de transporte |
| `002ed39` | o painel de status sai do disco (`v3/quadro.py`), não da memória de quem operou |
| `9c22561` | matar daemon confere se morreu, e a porta é a segunda testemunha |

## Princípios que o código defende

- **A produção não para.** Nenhum erro, conta caída ou credencial faltando interrompe a fila —
  só uma ordem expressa do operador.
- **Uma porta para cada mudança de estado.** Nada escreve no livro por fora.
- **Falha fala mais alto que sucesso.** Todo take que cai diz no log qual conta, qual motivo e
  qual contador pagou.
- **O que mede produção são contadores que só sobem.** Tentativa em círculo não é avanço.
- **Nunca dois produtores na mesma conta.** Dois relógios de rajada na mesma conta derrubam a
  conta; o vigia recusa um segundo supervisor na mesma leva.
