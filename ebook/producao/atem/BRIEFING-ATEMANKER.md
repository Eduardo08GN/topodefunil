# BRIEFING — DER ATEMANKER (2026-09-05)

> Segundo produto do parque de ebooks. Mercado alemão, nicho de ansiedade /
> regulação do sistema nervoso. Nasce para ser o destino do funil `gelo16`.

---

## 1. O QUE É

| | |
|---|---|
| Nome | **Der Atemanker — Ruhe in 2 Minuten** |
| Mecanismo único | **Der Atemanker** (escolha do Ed entre 3 propostas) |
| Promessa | Sair do alarme permanente em 2 minutos, sentado, em casa |
| Idioma | Alemão, tratamento **`du`** |
| Preço | **10 €**, pagamento único, garantia 7 dias |
| Entrega | 7 PDFs (`Schritt 1..7`) num zip, **58 páginas**, 3,8 MB |
| Landing | `book.morningritualmen.site` |

## 2. ⭐⭐ A DECISÃO DE CONTEÚDO QUE CONTRARIA A FONTE

O Ed mandou o PDF do **Wim Hof Method Explained** como referência de conteúdo.
A técnica de lá é **hiperventilação (30 respiros) + retenção longa + frio**.

**Não foi isso que entrou no produto, e a razão não é estética:**

- Hiperventilar derruba o CO₂ e produz **formigamento, tontura, aperto no peito
  e coração acelerado** — que é, item por item, a lista de sintomas do ataque de
  pânico que a compradora está tentando evitar. Vender "respire assim para a
  ansiedade" e entregar hiperventilação é entregar o gatilho embrulhado como
  solução.
- O que regula é o **oposto**: respiração lenta com **expiração mais longa que a
  inspiração** (4 in / 6 out, ~6 por minuto). Seguro, cabe nos 2 minutos que os
  criativos já prometem, e não pede equipamento.
- **Bônus colateral:** afasta o produto tanto do Wim Hof (direito autoral — o PDF
  fonte é `ALL RIGHTS RESERVED`) quanto do `Freemor Breathing®` do concorrente.
  Nenhuma frase foi traduzida da fonte; o que atravessa é fisiologia, que é fato
  e não se protege.

⛔ Nenhum exercício do produto pede hiperventilar nem segurar o ar com o pulmão
vazio.

## 3. AS TRÊS TRAVAS QUE ATRAVESSAM TUDO

1. **Sem hiperventilação** — ver §2.
2. **Água nunca** (`GE4` do `gelo16_short.py`). Respiração + imersão é o
   mecanismo do desmaio de águas rasas, que mata quem sabe nadar. A trava está
   em toda página de exercício, na página de segurança e nas regras do Bônus 1.
   Existe em **duas versões**: a longa (didática, onde há espaço) e a curta
   (ordem, no rodapé do card) — o parágrafo inteiro no card empurrava a caixa
   vermelha sozinha para a página seguinte.
3. **Sem diagnóstico e sem cura** (HWG alemão). Moldura: `Nervensystem im
   Daueralarm` → `Regulation in Minuten`. Quem está em crise aguda é mandado ao
   médico **por escrito**, com os telefones de DE/AT/CH. É a mesma lição já paga
   no cabeçalho do `atem16_short.py`.

## 4. CONGRUÊNCIA COM O FUNIL (o que o produto DEVE dizer)

O `gelo16` mostra uma alemã **sentada sobre o gelo** e a lente `GE5` obriga o
take 3 a dispensar o gelo por escrito (`kein Eis`, `zu Hause`, `im Warmen`).
Então o produto **tem** de entregar:

- método que funciona **no quente, em casa, sentado** — e entrega;
- **2 minutos** (`Nur zwei Minuten` está no pool de CTA) — e entrega, 12 respiros;
- o frio como **bônus opcional**, nunca como o método — é o `Bonus 1`, e a
  primeira frase dele diz que o Ed pode pular inteiro sem perder nada.
- A capa carrega `Ohne Eis. Ohne Ausrüstung. Zu Hause.` — quem vem do vídeo lê
  isso antes de qualquer outra coisa.

⚠️ A keyword do funil é `ATEM`, já cadastrada na automação de DM. O mecanismo se
chama **Atemanker** de propósito: comentário do vídeo e nome do produto falam a
mesma palavra.

## 5. ESTRUTURA

```
Schritt 1 - Fang hier an              8 pag   fisiologia + segurança
Schritt 2 - Der Atemanker            10 pag   a grundübung + 5 variantes
Schritt 3 - Der Notfall-Anker         7 pag   90 s no agudo + 3h da manhã
Schritt 4 - Dein 21-Tage-Plan         7 pag   1 tarefa/dia + tabela
Schritt 5 - Die Abendroutine          7 pag   noite e sono
Schritt 6 - Bonus 1 - Kaelte ohne Eis 7 pag   frio de pia, opcional
Schritt 7 - Bonus 2 - Ruhe-Tagebuch   9 pag   vorlagen para imprimir
```

## 6. MEDIÇÃO DO ACEITE (não relato)

| lente | resultado |
|---|---|
| páginas totais | **58** |
| páginas órfãs | **0** (a única sinalizada é seção curta real, 32%) |
| português vazado | **0** |
| mojibake | **0** |
| umlauts/eszett renderizados | **531** |
| texto extraído | 42.929 caracteres |
| compressão | 15,8 → 3,8 MB, **texto e paginação idênticos byte a byte** |
| zip | 2,9 MB, CRC OK, 7 arquivos |

⛔ **A caça à órfã levou 5 rodadas e o primeiro medidor estava errado.** Ele
contava pixel escuro e por isso acusava toda página com foto grande e diagrama
claro — 21 falsos positivos. O medidor certo pergunta **até onde o conteúdo
desce na página**. *Medidor de tinta não mede órfã.*

## 7. FERRAMENTAS NOVAS

- `motor_atem.py` — template do exercício. **Não é cópia** do `motor_receitas`:
  importa dele os TOKENS e o caminho do Chrome, e tem template próprio, porque
  receita e exercício de respiração não têm a mesma anatomia.
- `conteudo_atem.py` + `conteudo_atem2.py` — dados (partidos por tamanho).
- `build_atem.py` — dados → HTML → Chrome → 7 PDFs.
- `build_capa.py` — capa composta em HTML e rasterizada. ⛔ O texto da capa não
  sai do gerador de imagem: ele erra trema, e capa com trema errado parece
  produto falsificado.
- `../gerar_fotos_flow.py` — **muda o playbook**: ver §8.

## 8. ⭐⭐ O PASSO MANUAL DA FOTO ACABOU

O `PLAYBOOK-EBOOK` dizia: *"Eu escrevo o PROMPT, o operador GERA, eu distribuo"*
— porque o agente não tinha gerador. Com o browser-harness no Chrome logado, ele
tem: `gerar_fotos_flow.py` dirige o **Google Flow** por CDP, gera 1024×1024 e
baixa para `fotos/<slug>.jpg`. 20 fotos deste produto saíram assim.

- ⛔ **Modelo:** `Nano Banana 2`, que custa **0 crédito**. O `Pro` cobra: 12
  créditos foram gastos nas 13 primeiras fotos antes do Ed mandar trocar. A
  qualidade das 6 geradas no grátis não se distingue das do Pro no mosaico.
- ⛔ **Idempotente:** slug com arquivo na pasta é pulado. Crédito é finito.
- ⚠️ **Conferir com mosaico rotulado é obrigatório quando a POSTURA é o
  conteúdo.** A foto `haltung` saiu de pernas cruzadas enquanto a aula manda
  "os dois pés chapados no chão" — a imagem contradizia a instrução ao lado
  dela. Refeita com a restrição explícita no prompt.
- ⚠️ O `stdin` do harness não garante UTF-8: script com `⛔`/`⭐` no docstring
  quebra em `UnicodeEncodeError`. Rodar por um loader ascii que faz
  `io.open(..., encoding="utf-8")`.

## 9. PENDÊNCIA DECLARADA

⏳ **Impressum e Datenschutzerklärung.** Página comercial alemã precisa dos dois
(TMG/DSGVO). Não tenho os dados da empresa do Ed; o rodapé está preparado e
vazio. **Preencher antes de escalar tráfego** — é multa por notificação
(`Abmahnung`), não é detalhe.
