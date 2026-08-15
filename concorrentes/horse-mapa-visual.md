# HORSE — mapa visual da fonte

> Base do agente `horse16`. Leitura ótica a **16 fps** (275 quadros) + transcrição
> por Whisper do reel [1038123865853645](https://www.facebook.com/reel/1038123865853645).
> 17,3 segundos · 480×854 · 30 fps nativos.
>
> ⚠️ **Esta é UMA fonte.** O pool de ações do agente sai de **13 reels** da página
> [WellnessMSimple](https://www.facebook.com/WellnessMSimple), ainda **não lidos** —
> a listagem da página é geo-bloqueada e as URLs individuais são necessárias.
> Precedente do método: `banho16_v2`, que tirou 13 pares de gesto de 7 reels.

---

## A fala, verbatim, com os tempos medidos

```
0,00 → 2,38   My wife was about to leave me because of my performance.
3,18 → 5,56   Everything changed when I discovered a simple mixture,
6,08 → 8,28   horse gelatin, half a lemon and cinnamon.
8,94 → 12,52  The result was so strong that I got three times bigger and hard as iron.
12,98 → 16,44 Want the full explanation? Comment horse and I'll send it to your inbox.
```

⭐ **O corte de take cai sozinho em ~8,5s** — entre o fim do terceiro beat (8,28) e
o começo do quarto (8,94). A fonte já é um 16s de dois takes, sem precisar de
colapso: é a primeira do parque em que o formato não precisou ser forçado.

### Os cinco beats

| # | função | palavras |
|---|---|---|
| 1 | a falha, com dano social concreto (**a mulher ia embora**) | 10 |
| 2 | a descoberta, sem dizer o quê ainda | 8 |
| 3 | **a receita nomeada**: horse gelatin, meio limão, canela | 7 |
| 4 | a prova, em duas dimensões: **tamanho** e **dureza** | 14 |
| 5 | pergunta + CTA + onde chega (`inbox`) | 14 |

---

## O que a imagem faz, quadro a quadro

### TAKE 1 — a bancada, só mãos

Bancada de madeira clara, luz de janela, vaso de planta ao fundo desfocado.
**Nenhum rosto em quadro nenhum momento.** As mãos são de homem idoso — pele
manchada, veias marcadas, unhas curtas — e é nelas que a idade vive.

Objetos em quadro, do primeiro segundo:
- a **caixa rosa `HORSE GELATIN`**, com um cavalo desenhado, de pé atrás da tigela;
- um **post-it amarelo** colado na tigela: **`HARD AS IRON`**;
- limões inteiros e cortados, tigela de vidro transparente, copo medidor.

A sequência de ações, na ordem:
1. despeja **água fervendo** (vapor visível) da jarra medidora na tigela;
2. **rasga a caixa** e derrama o pó rosa por cima;
3. **mexe com a colher** até virar líquido vermelho translúcido;
4. **espreme meio limão** com a mão sobre a tigela;
5. **polvilha canela** de um potinho.

### TAKE 2 — o resultado e o casal

6. despeja o líquido vermelho num **refratário de vidro** sobre bancada de mármore;
7. corte para os **cubos firmes**, e a colher **corta um cubo** e o ergue;
8. ⭐ **o payoff**: um homem de barba branca (~65) e uma mulher loira jovem, num
   **campo aberto ao entardecer, com um cavalo pastando atrás deles**, os dois
   sorrindo um para o outro, comendo os cubos de uma tigela sobre mesa de madeira.

Legenda queimada em caixa alta e vermelho, palavra a palavra, o vídeo inteiro.
No fim, fixo no topo: **`Comment HORSE`**.

---

## ⛔ As decisões do operador que se afastam da fonte (2026-08-14)

| a fonte faz | o `horse16` faz | motivo |
|---|---|---|
| CTA pede **`horse`** | CTA pede **`gelatin`** | é a palavra cadastrada na automação de DM. Pedir `horse` faria o comentário entrar e a DM não sair |
| paga o **cavalo** no fundo do payoff | **sem cavalo** | ordem do operador |
| payoff no **campo, com o casal** | a mulher fica **no fundo da própria cena**, de toalha, sorrindo para ele preparar | é a identidade visual da página dele (bar de garagem), não a da fonte |
| a caixa da marca aparece | **a marca aparece** | exceção declarada ao P12, como o `banho16` |
| nomeia os ingredientes | **nomeia também**, com `horse gelatin` na fala | CT5 furado por decisão, entra no trio com `prato16` e `mel16` |

⚠️ **`half a lemon` não sobrevive.** A fala da fonte diz a fração, e a lei do repo
é *a fala não paga o que o quadro mostra*: sem medida, vasilhame nem fração na copy
falada. Vira `lemon`, e a metade fica na imagem, onde ela já estava.

⚠️ **Sem o cavalo, o nome do ângulo se apoia só na caixa.** Na fonte, o cavalo
pastando atrás do casal é o que fecha o sentido da palavra sem dizer nada. Tirando
ele, quem sustenta `horse` é o rótulo da caixa em quadro — e é por isso que a
exceção ao P12 aqui pesa mais que no `banho16`.

---

## O que ainda falta ler

⏳ **Os 13 reels da WellnessMSimple**, de onde sai o **pool generoso de ações** —
o eixo que o operador pediu. A fonte acima entrega **cinco ações** (despejar,
derramar o pó, mexer, espremer, polvilhar); um pool generoso precisa de muito mais,
e cada uma tem de ser lida no vídeo, não inventada.

⚠️ E a lição que o `banho16_v2` já pagou: **alguns gestos carregam copy própria,
verbatim da fonte**, e outros entram no registro leve. Colar a fala errada num
gesto é defeito que só aparece no vídeo renderizado.

⏳ **A beterraba**, que o operador quer no pool de ingredientes. Ela tinge de
vermelho igual à gelatina — então a **cor do líquido** precisa continuar coerente
entre os beats. O `prato16` já paga essa conta tratando a cor como eixo sorteável,
e é o precedente a seguir.

## Conexões

- [`CONTRATO-COPY-16S.md`](../funil-organico/CONTRATO-COPY-16S.md) — as sete travas
- [`PIPELINE-NOVO-AGENTE.md`](../PIPELINE-NOVO-AGENTE.md) — garimpo → mapa → motor
- `banho16_v2` — o precedente do gesto como eixo, e o de agente sem rosto
