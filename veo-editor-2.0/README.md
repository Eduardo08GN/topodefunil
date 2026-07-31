# Veo Editor 2.0 By EDDIE — a esteira do pipeline SHORT

Cópia do [`veo-editor`](../veo-editor) v1.2 com **uma diferença de comportamento**:
ela acelera o vídeo. Os dois rodam ao mesmo tempo, cada um com sua fila.

> **Para que serve:** a AdBatch Vertical 3 entrega 3 takes de 8s = **24 segundos**.
> A v2.0 devolve esse vídeo com **~22 segundos**.

---

## A TAXA

```python
CENTRO_VEL = 24.0 / 22.0     # 1.0909... — 24s vira 22s
VARIACAO   = 0.05            # +-5%, sorteado por video
VEL_MIN, VEL_MAX = 1.0364, 1.1455
```

⚠️ **O v1.2 não acelera nada.** O fator dele (0.95 a 1.03, média ~0.99) é
**ruído anti-duplicata**, não velocidade — é por isso que a coluna VEL do painel
sempre orbitou o 1.0. A v2.0 mantém o mesmo sorteio por vídeo, só desloca o
centro. A variação continua existindo pelo motivo original: dois uploads com a
duração idêntica ao milissegundo são fáceis de casar.

Medido em 2000 sorteios: um vídeo de 24s sai entre **20,95s e 23,16s**, média
**22,01s**.

⚠️ **A taxa é FIXA, não calculada da duração.** Um zip de 5 takes (40s) sairia
com 36,7s, não 38s — a v2.0 é do pipeline SHORT. Quando o número de takes não é
3, o log avisa (mas não recusa).

---

## ⛔ AS TRÊS FRONTEIRAS COM O v1.2

Sem elas as duas esteiras se atropelam, e **em silêncio** — o vídeo sai com a
taxa errada e nada na tela acusa.

| O quê | v1.2 | v2.0 | Se fosse igual |
|---|---|---|---|
| **Porta do mutex** | 50573 | **50574** | a v2.0 se recusaria a abrir com o v1.2 aberto |
| **Pasta de trabalho** | `VEO_EDITOR_BASE` | **`VEO_EDITOR2_BASE`** | fila, histórico e prontos compartilhados |
| **Padrão de captura** | `^adbatch(?!...vertical.3).*` | **`^adbatch.?vertical.?3.*`** | as duas vigiam a MESMA pasta Downloads; quem fizesse poll primeiro levava o zip da outra |

A terceira exigiu **mexer no v1.2 também**: o padrão dele era `^adbatch.*\.zip$`
e pegava os zips da vertical 3. Ganhou o lookahead negativo complementar. A
divisão foi conferida arquivo por arquivo:

```
adbatch_vertical_3.zip        ->  só v2.0
adbatch_vertical_4.zip        ->  só v1.2
adbatch_vertical_5.zip        ->  só v1.2
adbatch_lote.zip              ->  só v1.2
AdBatch Vertical 3 (1).zip    ->  só v2.0
```

---

## INSTALAÇÃO

Instalado em `C:\Users\edlut\Desktop\agentes_py\VEO-EDITOR-2.0`, ao lado das
pastas dos agentes. Abre pelo `Veo Editor 2.0.bat`.

O `.venv` foi **copiado** do v1.2 em vez de reinstalado — 317 MB de dependências
que já estavam resolvidas. Funciona porque o `.bat` chama
`.venv\Scripts\python.exe` direto, e o `python.exe` de um venv resolve o próprio
prefixo pela localização dele, não por caminho embutido. (Os entry points como
`pip.exe` é que carregam caminho absoluto — se precisar de `pip`, rode
`instalar.bat`.)

---

## O QUE **NÃO** MUDOU

Tudo o mais é o v1.2: transcrição, legenda karaokê com as keywords destacadas,
corte de silêncio, junção dos takes, organização em `03_prontos/<data>`,
histórico em CSV, retry da pasta de erros, pasta avulsa.

⚠️ **Fix de bug entra nos dois.** Esta pasta é uma cópia, e cópia envelhece e
mente — a mesma razão pela qual os agentes SHORT foram **derivados** em vez de
copiados. Se as duas esteiras começarem a divergir de verdade, o movimento
certo é extrair o núcleo comum e deixar aqui só o perfil.

---

## Conexões

- [`../veo-editor/README.md`](../veo-editor/README.md) — o v1.2
- [`../funil-organico/RUNBOOK-adbatch-vertical.md`](../funil-organico/RUNBOOK-adbatch-vertical.md) — a ferramenta que produz o zip de 24s
- [`../funil-organico/RUNBOOK-app-offline.md`](../funil-organico/RUNBOOK-app-offline.md) §SHORT — os agentes que geram o roteiro de 3 cenas
