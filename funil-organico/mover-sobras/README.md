# Mover Sobras — as sobras do Veo Editor vao para o HD

Worker que leva os videos **nao postados** das pastas de dia do Veo Editor 2.0
para uma pasta unica no HD externo.

```
C:\...\VEO-EDITOR-2.0\03_prontos\AAAA-MM-DD\vNNN_final.mp4
    ->  D:\estoque\AAAA-MM-DD__vNNN_final.mp4
```

Encomenda do operador (2026-08-11): meta de **3 videos por pagina em 15 paginas**;
ele produz a mais, e o excedente fica parado ocupando o SSD.

## ⛔⛔ A regra e' POSITIVA, e essa e' a decisao mais importante

Move-se **apenas** o que casa com `vNNN_final.mp4` — o molde que o proprio
`esteira.py` gera (`^v(\d+)_final\.mp4$`, linha 292 de la'). Depois de postar, o
operador **renomeia** para `postado...`.

A regra tentadora seria *"move tudo que nao se chama postado"*. Ela esta' errada,
e a prova estava na pasta de 2026-08-09 **antes** de o script existir:

```
posado.mp4        <- sem o "t"
posado (2).mp4    <- sem o "t"
```

Videos **ja postados**, com erro de digitacao no rename. A regra negativa os
levaria para o HD como se fossem sobra, e o registro do dia mentiria. A positiva
ignora qualquer nome fora do molde — inclusive os erros que ainda vao acontecer.

## Decisoes do operador

| | |
|---|---|
| destino | `D:\estoque`, pasta unica |
| colisao de nome | prefixo com a data: `2026-08-10__v003_final.mp4`. Dois dias podem ter um `v003_final.mp4`; sem prefixo um sobrescreveria o outro em silencio, e o prefixo ainda ordena por data sozinho |
| `03_prontos\estoque` | **nao e' tocada** — ele transfere aquela pasta a mao |
| pasta do dia | fica como esta', com os `postado*` dentro: e' o registro do que foi ao ar |

## Como fica sempre ativo

⛔ **Nao deu para usar o Agendador de Tarefas**: registrar tarefa exige
**elevacao** nesta maquina (`schtasks` e a API COM devolveram `Access denied`). O
`tarefa.xml` fica versionado aqui para quem puder elevar, mas exigir um UAC toda
vez nao serve para uma coisa que ele quer esquecer que existe.

⭐ O worker e' **residente** (`--servico`), com atalho na pasta Inicializar. Liga
o PC, ele sobe; faz uma passada na hora e depois de hora em hora.

⚠️ **O pulso e' mais rapido que a passada** — 45s contra 60min, de proposito. Se
o unico sinal fosse a passada, um worker **morto** pareceria vivo por quase uma
hora, que e' justamente o intervalo em que a tela nao poderia ser confiada.

## O estado publicado

`%LOCALAPPDATA%\MoverSobras\estado.json`, trocado de forma atomica (`os.replace`)
porque as duas interfaces leem a qualquer momento.

```json
{ "batimento": "...", "resultado": "ok|hd_desconectado|falhas",
  "no_destino": 137, "movidos_total": 137, "gb_total": 0.74,
  "backlog_arquivos": 0, "backlog_por_dia": [{"dia":"...","n":4,"gb":0.5}] }
```

⛔ **"Live" nunca e' "o arquivo existe"** — e' o pulso ter menos de 3 minutos.
E sao **tres estados diferentes**, cada um com nome proprio: `live` · `live,
esperando o HD` (ele levou o HD — nao e' falha) · `PARADO`.

⚠️ **O contador do destino conta a pasta de verdade**, em vez de confiar no
acumulado: ele pode apagar ou levar arquivos de la' por fora, e um contador que
so' soma viraria mentira crescente. Por isso sao dois numeros — `movidos_total`
(o trabalho do worker) e `no_destino` (o que existe agora).

## Onde aparece

| interface | o que mostra |
|---|---|
| **Video Terminator** | linha colorida na tela de abertura e no F1; **F7** abre o painel com contadores e o backlog **por dia** |
| **Veo Editor 2.0** | rotulo no cabecalho, abaixo do contador de prontos: aqua em dia, dourado esperando o HD, vermelho parado |

⛔ O backlog e' **por dia**, e nao um total: um total nao diz se o problema
comecou hoje ou ha' uma semana.

## Tres defeitos que a execucao pegou

**O backlog herdava o filtro `--dias`.** Uma passada limitada a tres dias
publicava `backlog: 0` com **32 sobras** paradas nos dias antigos. O painel existe
para mostrar o que **nao** foi levado; herdar o filtro de quem levou o
transformava num espelho do proprio sucesso.

**A trava era removivel por quem nao a criou.** Duas instancias subiram quase
juntas; a segunda viu a trava e saiu — mas o `finally` dela **apagou a trava da
primeira**, que continuava viva. Porta destrancada com o dono dentro. Agora so'
apaga quem criou, e o pulso renova a trava.

**E a minha propria checagem de "esta rodando?" mentiu tres vezes.** O filtro
casava a linha de comando, e casou com **o proprio PowerShell que fazia a
pergunta**. Reportei "worker vivo: 1" com zero workers no ar — eu tinha matado o
real com a minha limpeza. O filtro agora exige `pythonw.exe` **e** o nome do
script.

## Medido

| | |
|---|---|
| primeira limpeza | **105** videos dos 3 dias autorizados + **32** dos dias antigos = **137**, 0,74 GB, 0 falha |
| pastas do dia | ficaram so' com os postados (39, 40, 18) — os dois `posado` intactos |
| arquivos `.parcial` | nenhum |
| trava | intrusa sobe, sai sozinha, e a trava do dono sobrevive |
| pulso | avanca sozinho a cada 45s (medido em duas leituras separadas) |
| Video Terminator | 4 blocos de teste, painel F7 em 752px, **0 controles fora** |
| Veo Editor | **7 de 7**: os tres estados forjados + sem arquivo + json incompleto |
