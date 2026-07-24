# Automação Comentário → DM (Meta) + congruência da cadeia

Como configurar a automação "Comentar para enviar mensagem" do Meta Business Suite
em cada página, e por que a copy da DM tem que casar com o reel e com a VSL.

Fluxo: **reel → comentário com a keyword → DM automática (com o link da bridge) →
bridge → VSL**. A automação é o elo que transforma comentário em DM.

Visão macro da operação: [`ARQUITETURA-OPERACAO.md`](ARQUITETURA-OPERACAO.md) ·
Bridges: [`bridge-pages-arquitetura.md`](bridge-pages-arquitetura.md)

---

## Regra de ouro (alinhada na call com Fran e Giovanni)

**Só DM. NUNCA responder na seção de comentários dos posts.**

No formulário do Meta, o que gera a resposta pública é o campo
**"Resposta ao comentário (recomendado)"** (vem pré-preenchido com *"Enviei uma
mensagem para você!"*). Esse campo é **opcional** — deixar **vazio (0/500)** faz o
robô só mandar DM, sem tocar nos comentários. **Sempre limpar esse campo.**

Motivo: responder no comentário expõe o mecanismo do funil publicamente (qualquer
um vê a automação disparando), suja o post e ajuda a Meta a fingerprintar a
operação. A entrega é 1:1, no privado.

---

## Keywords (gatilho)

**Sempre `gelatin`** (todas as páginas rodam gelatin trick). O Meta aceita **até
10 keywords** e o match é **"o comentário CONTÉM a palavra", case-insensitive** —
então `gelatin` já pega `GELATIN`, `Gelatin`, `gelatin please`, `gelatins`. Os
outros 9 slots cobrem **erros de digitação que quebram o miolo** da palavra (que o
`gelatin` puro não pegaria), com grafias de um **americano** (nada de `gelatina`,
que é PT/ES):

```
gelatin
gelatine
jelatin
gelatn
gelati
gellatin
gelatim
gelantin
geltin
gelaton
```

> A keyword tem que ser **idêntica** à que a legenda/CTA do reel manda comentar.
> O randomizador V5 emite `CTA:GELATIN` quando `cta=keyword_mecanismo` — é essa.

---

## DM (mensagem privada)

O link da DM é **a bridge daquela página** com atribuição `?p=<slug>` (ver tabela
por página abaixo). Modelo (exemplo Matt's / steadystrengthhub):

```
Hey! Here's the gelatin recipe I mentioned in my reel 👇
https://steadystrengthhub.site/?p=steadystrengthhub
That's the full trick — grab it before they make me take it down.
```

**Por que "recipe" e não "video":** gelatina é algo que se **prepara e ingere** →
"recipe" é o substantivo congruente com o gelatin trick. "video" é genérico e, pior,
"**short** video" **mente sobre a duração** (a VSL do Ragnaroak é longa) — o lead
entra esperando 30 s, vê VSL longa e faz bounce bem na hora da venda. Nunca prometa
duração que a VSL não cumpre.

---

## Congruência da cadeia (a regra que não pode quebrar)

Se o reel promete uma coisa e a DM entrega outra, o clique morre. **Tudo tem que
apontar pra mesma coisa: a receita do gelatin trick.**

| Elo | Promessa (tem que ser a MESMA) |
|---|---|
| **Reel — CTA (cena 5)** | "comment **GELATIN** → I'll send you the **recipe**" |
| **DM** | "here's the gelatin **recipe** I mentioned in my reel" |
| **Bridge** | *"He ate it before bed…"* → clique no vídeo privado |
| **VSL (Ragnaroak/Horsewood)** | apresenta o gelatin trick / a receita |

**Checklist de congruência ao escrever/editar:**
- [ ] A keyword da DM == a keyword que o reel manda comentar (`GELATIN`)?
- [ ] O substantivo entregue é **recipe** no reel E na DM (não "video", não "short")?
- [ ] A DM cita "**in my reel**" (amarra ao vídeo que a pessoa acabou de ver)?
- [ ] O mecanismo é o mesmo nos 4 elos (**gelatin**)?
- [ ] A voz/persona é a mesma (o mesmo "eu" do reel fala na DM)?
- [ ] A escassez do reel ("before it's gone") ecoa na DM ("before they make me take it down")?

> A copy da DM NÃO segue a regra das 3 linhas da bridge — isso é regra de bridge
> page. A DM é 1:1 no inbox; mantê-la curta (3 linhas) é boa prática, mas o limite
> real é 1000 caracteres.

---

## Link da DM por página (atribuição `?p=`)

Todas gelatin; muda só o slug/domínio (e a VSL de destino, mas o link da DM é
sempre a **bridge**, não a VSL direta).

| Página | Link na DM |
|---|---|
| Joe's Wellness hub | `https://manresethub.pro/?p=manresethub` |
| Marcus' Men Reset Hub | `https://vitalresetlab.site/?p=vitalresetlab` |
| Ray's Natural Vitality Hub | `https://primalvitalityhub.site/?p=primalvitalityhub` |
| Chuck's Men Welness Hub | `https://allmensnatural.site/?p=allmensnatural` |
| Matt's Natural Reset Tips | `https://steadystrengthhub.site/?p=steadystrengthhub` |

---

## Passo a passo no Meta Business Suite

Caixa de Entrada → Automações → "Comentar para enviar mensagem" → Editar:

1. **Nome:** `<Página> - Comment to DM (gelatin)`.
2. **Canal:** Messenger ✅. Instagram só se a página tiver IG vinculado (as páginas
   são FB → normalmente **desmarcar Instagram**).
3. **Palavras-chave:** as 10 acima (uma por vez + Enter).
4. **Mensagem privada:** a DM da página (modelo acima, com o link `?p=` certo).
5. **Resposta ao comentário:** **LIMPAR → deixar vazio (0/500).** ⚠️ passo crítico.
6. **Salvar alterações.**

> Repetir por página, trocando só nome, link da DM e (se precisar) a persona da voz.

---

## Status

- [x] Matt's Natural Reset Tips — copy/keywords/DM definidos (este doc).
- [ ] Matt's — automação salva no Meta (DM only, comentário em branco).
- [ ] Joe's, Marcus', Ray's, Chuck's — replicar com o link `?p=` de cada uma.
