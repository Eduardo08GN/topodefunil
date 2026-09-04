# Bridge Pages — Deploy & Domínios

Registro de todas as bridge pages do funil orgânico ED, hospedadas no VPS via Coolify.

## ⛔⛔ TRÊS DONOS DIVIDEM ESTE VPS — e só o VPS

| dono | pasta no `projetosweb` | apps | `aff_id` |
|---|---|---|---|
| **Ed** (esta operação) | `/bridge-pages` | um por domínio (`*-bp`, `*-bp1`) | **45158** · **2470** |
| **a PARCEIRA** (amiga do Ed) | `/parceira-bridges` | `parceira-bridges-4dom` — **um só, 10 domínios** | **52138** |
| **o LUCAS** | `/bridge-pages/bp-dailyvitalreport` e irmãos | `dailyvitalreport-bp` e irmãos | **44878** |

⚠️ **A parceira usa a MESMA oferta que o Ed** (`horsewood.us/VHG2-L1ML3/`). Ver
`horsewood` numa página dela **não é erro** — o que separa o dinheiro é o
**número** do `aff_id`. A conferência é sempre do número, nunca da oferta.

⛔ **O documento que garante o isolamento é
`projetosweb/parceira-bridges/PROPRIEDADE-E-ISOLAMENTO.md`** — mapa dos 10
domínios dela, as quatro camadas que impedem a mistura (guarda de afiliado que
aborta o build, pasta irmã, app próprio, `root` por domínio) e a receita para
acrescentar mais um. **Ler antes de tocar em `/parceira-bridges`.**

## Infra

- **VPS:** `159.195.12.135` (Netcup)
- **Orquestrador:** Coolify v4.1.2 — instância em `http://159.195.12.135:8000`
- **Reverse proxy:** Traefik (SSL automático via Let's Encrypt)
- **Source dos apps:** repo privado `Eduardo08GN/projetosweb`, branch `main`, GitHub App `coolify-projetosweb`
- **Build:** Dockerfile em `/bridge-pages/bp1` (nginx:alpine servindo `index.html` + `hero.png` em `/bp1/`)
- **Página servida em:** `<dominio>/bp1/`

## Link de destino (oferta) — ⚠️ NÃO É ÚNICO, TEM SPLIT

⛔ **Não existe um destino global.** Cada bridge aponta para a VSL da **sua** página. Uma
versão anterior deste documento declarava Horsewood para todas — isso manda a comissão
do Chuck e do Matt para o afiliado errado. Foi esse erro que motivou deletar o
redirector central (ver [ARQUITETURA-OPERACAO](ARQUITETURA-OPERACAO.md)).

| Página | Domínio da bridge | VSL de destino | `aff_id` |
|---|---|---|---|
| Joe | `manresethub.pro` | `horsewood.us/VHG2-L1ML3/` | **45158** |
| Marcus | `vitalresetlab.site` | `horsewood.us/VHG2-L1ML3/` | **45158** |
| Ray | `primalvitalityhub.site` | `horsewood.us/VHG2-L1ML3/` | **45158** |
| Chuck | `allmensnatural.site` | `ragnaroak.us/VHGML5-3/` | **2470** |
| Matt | `steadystrengthhub.site` | `ragnaroak.us/VHGML5-3/` | **2470** |
| Hank | `secondwindformen.site` | `horsewood.us/VHG2-L1ML3/` | **45158** |
| Philippe Laurent | `morningritualmen.site` | `horsewood.us/VHG2-L1ML3/` | **45158** |
| Jason H. | `stridebackmen.site` | `horsewood.us/VHG2-L1ML3/` | **45158** |
| Earl Hodge | `menritualhub.site` | `horsewood.us/VHG2-L1ML3/` | **45158** |
| Dean Whitaker | `thefitmenhub.site` | `horsewood.us/VHG2-L1ML3/` | **45158** |
| Roy Tanner | `menvitalityhub.site` | `horsewood.us/VHG2-L1ML3/` | **45158** |
| Wade | `strengthandflow.site` | `horsewood.us/VHG2-L1ML3/` | **45158** |
| Isaiah | `dailyvitalitymethod.site` | `horsewood.us/VHG2-L1ML3/` | **45158** |
| Curtis | `menresethub.site` | `horsewood.us/VHG2-L1ML3/` | **45158** |
| Otis | `mensresetclub.online` | `horsewood.us/VHG2-L1ML3/` | **45158** |

```
https://<vsl-da-pagina>/?aff_id=<aff-da-pagina>&subid=<pagina>
```

- `aff_id` → comissão. **45158 = Horsewood · 2470 = Ragnaroak.** Conferir na tabela.
- `subid` → atribuição por página (lido de `?p=<slug>` na URL da bridge; default `direct`)

> ⚠️ **Na saída é `subid`, nunca `sub_id`.** O BuyGoods documenta `&subid=`; com
> `sub_id` a venda entra **sem atribuição** e o notificador não sabe qual página vendeu.
> Na *entrada* a bridge aceita `?p=` (padrão) e tolera `subid`/`sub_id` como legado.
>
> ✅ **Verificado em produção em 2026-07-28** (`curl` nos 3 domínios): o split e o
> `&subid=` estão corretos no ar. O erro era **deste documento**, não do deploy.

## ⭐⭐ AS TRÊS LANDINGS DO EBOOK 150 — não são bridges de ED (2026-09-03)

⛔ **Estas três não pertencem ao funil de ED e não seguem a regra das bridges.**
Elas vendem o infoproduto *150 Receitas* (Hotmart) e vivem em **subdomínio
`book.`**, cada uma num app próprio do Coolify, servindo de
`/bridge-pages/bp-fit-<lang>` no `projetosweb` (commit `eb65b20`, do Lucas).

| Idioma | URL | App Coolify (UUID) | `base_directory` |
|---|---|---|---|
| **EN** | `https://book.dailyfactreport.site` | `r2cgw8c5j25cq0e89i7lrj7n` | `/bridge-pages/bp-fit-en` |
| **DE** | `https://book.plainfactsdaily.site` | `qg2mxau3et2gp85kv6mrwdqo` | `/bridge-pages/bp-fit-de` |
| **FR** | `https://book.thedailyfinding.site` | `v2524bw7z6ho7v22d6xadyz2` | `/bridge-pages/bp-fit-fr` |

⭐ **Os três domínios são os de nome mais genérico do inventário** (estilo
jornal, nada que remeta a ED), que é o critério do operador para este produto.

✅ **Medido no ar em 2026-09-04**, nas URLs reais e não no código de status:
HTTPS **200** nas três · `<html lang>` e `<title>` no idioma certo em cada uma ·
**capa própria por idioma** (`capa-150-{EN,DE,FR}-hotmart.jpg`) e pasta
`receitas/<lang>/` própria — não é a mesma página com o nome trocado ·
**13 de 13 assets em 200** em cada domínio (capa, 5 vídeos de review, 5 fotos de
receita, selo Hotmart), medidos um a um com HEAD.

⛔⛔ **AS TRÊS ESTÃO NO AR E NENHUMA VENDE.** Medido no HTML servido: os **4
botões** de cada página apontam para `#offer` (âncora interna) ou `#`, e **não
existe UMA URL externa** nas três — nenhum link de checkout da Hotmart. A página
tem a seção de pagamento inteira montada e diz *"Secure Hotmart checkout"*, mas
o botão não leva a lugar nenhum. **É o único elo que falta**, e é decisão do
operador: o link do produto na Hotmart (um por idioma) não se inventa.

⚠️ **Duas das três dividem o apex com uma bridge de ED viva** — medido:
`dailyfactreport.site/lamont` e `plainfactsdaily.site/sam` respondem **200**.
Subdomínio é app e contêiner separados, mas o **domínio registrável é o mesmo**:
um problema no apex (registrador, Cloudflare, marcação) leva o `book.` junto.
`thedailyfinding.site` é a única das três com o apex limpo. Se o operador quiser
separação total, `everydaydigest.site` e `dailyvitalreport.store` também estão
sem página de ED e de prontidão — **é escolha dele, não se move página no ar por
julgamento próprio.**

## Domínios & Apps

| # | Domínio | App Coolify (UUID) | URL de teste (sslip.io) | Status |
|---|---------|--------------------|-----------------------|------------|
| 1 | `manresethub.pro` | `v5t2rojizir3dc37al4zkb4p` | `http://v5t2rojizir3dc37al4zkb4p.159.195.12.135.sslip.io/bp1/` | ✅ **no ar** (HTTPS) |
| 2 | `wholelifenutri.shop` | `cwanszytythvm4myf8yye46k` | `http://cwanszytythvm4myf8yye46k.159.195.12.135.sslip.io/bp1/` | ⚠️ pendente (parking) |
| 3 | `vitalresetlab.site` | `bv4uhh6hpq6tkotyn42nagg3` | `http://bv4uhh6hpq6tkotyn42nagg3.159.195.12.135.sslip.io/bp1/` | ✅ **no ar** (HTTPS) |
| 4 | `primalvitalityhub.site` | `srd3jdzrvc0n7ri3yetjjmuq` | `http://srd3jdzrvc0n7ri3yetjjmuq.159.195.12.135.sslip.io/bp1/` | ✅ **no ar** (HTTPS) |
| 5 | `allmensnatural.site` | `iuge7sircaf0myor1jdl77jv` | `http://iuge7sircaf0myor1jdl77jv.159.195.12.135.sslip.io/bp1/` | ✅ **no ar** (HTTPS) |
| 6 | `steadystrengthhub.site` | `xkma961zrq3jxraw5z4vpg47` | `http://xkma961zrq3jxraw5z4vpg47.159.195.12.135.sslip.io/bp1/` | ✅ **no ar** (HTTPS) |
| 7 | `secondwindformen.site` | `p6b0bb2bsbychxyzs8m0axzp` | — | ✅ **no ar** (HTTPS) |
| 8 | `strengthandflow.site` | `t8koxrte3s7530p5b6mazkjv` | — | ✅ **no ar** (HTTPS) |
| 9 | `dailyvitalitymethod.site` | `tqwepmv042n3y13xiy68ve0v` | — | ✅ **no ar** (HTTPS) |
| 10 | `menresethub.site` | `u3szzoq1y9vcgoapsi2jnq0e` | — | ✅ **no ar** (HTTPS) |
| 11 | `mensresetclub.online` | `t9wzm0j2pctbql7tsu3nbbor` | — | ✅ **no ar** (HTTPS) |
| 13 | `morningritualmen.site` | `tlx57qzzdzscgypkkkw61505` | — | ✅ **no ar** (HTTPS, 2026-08-04) |
| 14 | `stridebackmen.site` | `idx2ek34etgj5dmpspc59iuu` | — | ✅ **no ar** (HTTPS, 2026-08-04) |
| 15 | `menritualhub.site` | `k1476zn3nxztce9yi07rf75p` | — | ✅ **no ar** (HTTPS, 2026-08-04) |
| 16 | `thefitmenhub.site` | `oi771du8quctmppyogchvo7l` | — | ✅ **no ar** (HTTPS, 2026-08-04) |
| 17 | `menvitalityhub.site` | `x1369zh3c0wjkfp3m0m3rffa` | — | ✅ **no ar** (HTTPS, 2026-08-04) |

> ⚠️ **As cinco de 2026-08-04 servem de `/bridge-pages/bp-<slug>`, não de `bp1`.**
> Cada uma tem pasta própria com Dockerfile, `hero.png` e `index.html` — o
> `bp1` é só a do Joe. E o `pagina` das cinco está `(a definir)` no `_build.py`
> e `[definir]` no dict do `webhooks/vendas-telegram`, **de propósito**: o
> notificador precisa do nome REAL da página do Facebook, e nome plausível e
> errado já custou uma venda sem origem (o fantasma `Dale`). Trocar assim que
> as páginas existirem.
>
> ✅ **Postback testado nos cinco em 2026-08-04**, no endpoint `/venda` (não em
> `/`, que é o health check e responde `OK` sem notificar nada). Controle
> negativo com segredo errado registrou `[auth] segredo invalido`; os cinco
> reais não geraram nenhuma linha `[telegram] ... falhou`, e as cinco
> mensagens chegaram no Telegram com o domínio certo.
| 12 | `dailyvitalreport.store` ⛔ **do LUCAS** | `kw5fu21f7rad8fnklgf1iiqn` | `http://kw5fu21f7rad8fnklgf1iiqn.159.195.12.135.sslip.io/` | ✅ **no ar** (HTTPS) |

### ⛔⛔ O #12 NÃO É DESTA OPERAÇÃO — não misturar

`dailyvitalreport.store` é do **Lucas**, subiu em 2026-08-03 e divide só o VPS.
Tudo o mais é separado, e a confusão aqui custa comissão indo para a pessoa
errada:

| | os 11 acima | o #12 |
|---|---|---|
| pasta no `projetosweb` | `bridge-pages/bp-<dominio>` | `bridge-pages/bp-dailyvitalreport` |
| oferta | Horsewood `VHG2-L1ML3` · Ragnaroak `VHGML5-3` | `horsewood.us/VHGTH-L3/` |
| `aff_id` | **45158** · **2470** | **44878** |
| gerado por | `bridge-pages/_build.py` | ⛔ **fora do `_build.py`, de propósito** |

⛔ **Não acrescentar `bp-dailyvitalreport` à tabela `PAGINAS` do `_build.py`.**
O gerador reescreveria o `aff_id` do Lucas com um dos desta operação no
próximo build — que é exatamente o erro que motivou deletar o redirector
central.

**As 5 URLs dele**, uma por página de Facebook, cada uma com o `subid` fixo no
HTML (sem JS):

### ⭐⭐ 2026-08-06 — AS 10 PÁGINAS SE ESPALHARAM POR 5 DOMÍNIOS, 2 EM CADA

⛔ **`dailyvitalreport.store` não hospeda mais as 10.** O operador comprou 4
domínios e pediu a divisão: *"dessa forma as páginas ficarão mais seguras caso
um link seja marcado"*. Antes, um domínio marcado derrubava **as 10 URLs de uma
vez**; agora derruba **2**.

⛔⛔ **2026-08-20 — DAS TREZE SOBRARAM TRÊS.** Dez páginas de Facebook caíram.
Ordem do operador: *"deixe só para as 3 páginas mesmo para não sujar os
domínios [...] é só o que está após a barra que será apagado, os domínios
continuarão do mesmo jeito de prontidão para serem usados de novo em novas
páginas futuras"*. As dez pastas saíram no commit `5214a71` do `projetosweb`.

| Domínio | App Coolify (UUID) | Página | `subid` | Avatar |
|---|---|---|---|---|
| `dailyfactreport.site` | `uurhd13s9x1rei59f5gqm3jc` | **Lamont Boyd** | `lamont` | homem negro |
| `plainfactsdaily.site` | `vx3q4f59noi9u5cr7fx6jzj3` | **Sam Pickett** | `sam` | homem negro |

#### ⭐⭐ 2026-08-28 — AS DUAS SAEM DO HORSEWOOD

Ordem do operador: *"Altere os links nas páginas do Sam e do Lammont, dos
botões e tudo para esse: https://bg.alphaforgeplus.com/2607-15ar/?aff_id=25518"*.

| | antes | agora |
|---|---|---|
| oferta | `horsewood.us/VHGTH-L3/` | **`bg.alphaforgeplus.com/2607-15ar/`** |
| `aff_id` | **44878** | **25518** |
| `subid` | `lamont` / `sam` | **inalterado** |

⛔ **SÓ as duas pastas de página.** As **cinco raízes** dos domínios dele
(`dailyfactreport`, `plainfactsdaily`, `dailyvitalreport`, `everydaydigest`,
`thedailyfinding`) seguem no `horsewood.us/VHGTH-L3/?aff_id=44878` — medido: 3
ocorrências em cada uma, intactas.

⭐ **O `&subid=` foi preservado de propósito.** O link que ele passou vem sem
ele; sem `subid` a venda entra **sem atribuição** e não dá para saber qual das
duas páginas vendeu. Como o parâmetro `aff_id` é o mesmo nome que a BuyGoods
usa nas outras duas ofertas, `subid` deve valer aqui também — mas isso é
**inferência**, não medição: quem confirma é a primeira venda com atribuição.

⚠️ **O cofre não cobre estas duas.** O `_cofre.py` sela o mapa
domínio → oferta + aff que sai da tabela `PAGINAS` do `_build.py`, e as páginas
do Lucas estão fora do `_build.py` de propósito. `--verificar` segue em
✅ 20 páginas, e **isso não é aval da troca** — é silêncio sobre ela.

⛔⛔ **A COPY DA BRIDGE NÃO FOI TOCADA, e ela promete outra coisa.** O
`<title>` e a manchete das duas dizem *Gelatin Horse Trick* e
*Add Up To 1.9 Inches Without Pills* — escritas para a VSL do horsewood. Se a
oferta nova vender outro mecanismo, a cadeia
reel → DM → bridge → VSL quebra no último elo. Copy é alçada do operador
([`CLAUDE.md`](../CLAUDE.md) §REGRA DE ALÇADA): fica registrado, não corrigido.

### ⛔⛔ De três sobraram DUAS — a bridge é só de ED (2026-08-21)

Ordem do operador: *"a página da Sara como é weight loss não terá uma landing,
a landing será somente para páginas ED [...] irei mandar o link de afiliado
direto"*.

A **Sarah Brown** virou página de **emagrecimento** (roda o `AMISH 16S`) e saiu
de `everydaydigest.site/sarah`. A pasta e a linha `COPY` saíram juntas —
commit `e1d876f` do `projetosweb` —, o deploy do app `goc65jdh6xw2po2ja3mk99sa`
foi disparado e **medido na URL real**: `/sarah` devolve **404**, a raiz e o
`privacy.html` seguem em **200**, e `dailyfactreport.site/lamont` continua
**200** (nada colateral).

⭐ **O domínio e o app ficam de prontidão**, como nas dez de 20/08: o
`everydaydigest.site` segue servindo a matéria da raiz, com DNS e SSL intactos.
Página nova volta a existir criando a pasta e a linha do `COPY`.

⚠️ **A regra que isto cria:** bridge page é dispositivo do funil de **ED**. Uma
página de emagrecimento manda o tráfego direto para o link de afiliado, sem
página intermediária — e por isso ela não consome domínio nenhum.

⏳ **Pendência declarada:** o link de afiliado de emagrecimento **ainda não
existe** (*"ainda não tenho o link mas irei passar quando conseguir"*). Até ele
chegar, a `bio.txt` da Sarah e os 25 slots da lista de postagem dela continuam
apontando para o `/sarah` que agora dá 404 — de propósito, porque trocar por um
placeholder poria um link morto **diferente** no lugar de um link morto
**conhecido**. Quando o link chegar, a troca é num lugar só: a `bio.txt` da
pasta dela, que é de onde o `legendas.py` lê a URL de todos os posts.

⛔ **NENHUM APP E NENHUM DOMÍNIO FOI TOCADO**, e é decisão explícita dele. Os
cinco continuam no ar servindo a matéria da raiz, com DNS e SSL intactos —
página nova volta a existir criando a pasta e commitando. Apagar app no Coolify
obrigaria a refazer app, domínio e certificado do zero.

⚠️ **`dailyvitalreport.store` e `thedailyfinding.site` ficaram sem pasta de
página nenhuma.** É o estado desejado, não esquecimento — os dois estão de
prontidão para a próxima página.

⚠️ As dez URLs (`jennifer`, `reggie`, `denise`, `wayne`, `dale`, `otisgloria`,
`carol`, `curtis`, `hankmarlene`, `yvonne`) passam a dar **404**, e isso é o
objetivo: manter URL viva de página morta é manter o alvo grande. As bios do
Facebook não precisaram de conserto porque as páginas já tinham caído.

<details><summary>O mapa das 13, antes do corte de 20/08 — histórico</summary>

| Domínio | App Coolify (UUID) | Página | `subid` | Avatar |
|---|---|---|---|---|
| `dailyvitalreport.store` | `kw5fu21f7rad8fnklgf1iiqn` | Reggie Harris | `reggie` | homem negro |
| " | " | Jennifer Miller | `jennifer` | mulher branca |
| `dailyfactreport.site` | `uurhd13s9x1rei59f5gqm3jc` | Denise Walker | `denise` | mulher negra |
| " | " | Wayne Miller | `wayne` | homem branco |
| `plainfactsdaily.site` | `vx3q4f59noi9u5cr7fx6jzj3` | Otis & Gloria | `otisgloria` | casal negro |
| " | " | Dale Pruitt | `dale` | homem branco |
| `thedailyfinding.site` | `b5e8211hjaxecijcgybsvgde` | Curtis Grant | `curtis` | homem negro |
| " | " | Carol Whitfield | `carol` | mulher branca |
| `everydaydigest.site` | `goc65jdh6xw2po2ja3mk99sa` | Yvonne Bradley | `yvonne` | mulher negra |
| " | " | Hank & Marlene | `hankmarlene` | casal branco |
| " | " | **Sarah Brown** | `sarah` | mulher branca |
| `dailyfactreport.site` | `uurhd13s9x1rei59f5gqm3jc` | **Lamont Boyd** | `lamont` | homem negro |

</details>

⚠️ **O pareamento não é aleatório:** cada domínio leva **uma página de avatar
negro e uma de avatar branco**. Um domínio marcado não apaga um demográfico
inteiro do funil.

⭐ **Lote 3 — 2026-08-11: +2 páginas, uma em cada domínio.** Ordem do operador:
*"escolha qualquer uma dos meus domínios, de forma que fique uma em cada
domínio"*. Sarah foi para `everydaydigest.site` e Lamont para
`dailyfactreport.site` — e a escolha **não foi sorteio**:

  · ⛔ nenhum dos dois entrou num domínio que já tinha **o mesmo tipo de
    avatar**. Mulher branca já existe em `dailyvitalreport` (Jennifer) e
    `thedailyfinding` (Carol); homem negro solo, nos mesmos dois (Reggie,
    Curtis). Os dois domínios ficaram de fora por isso;
  · o pareamento negro/branco de cada domínio continua de pé — `everydaydigest`
    fica 1 negro / 2 brancos e `dailyfactreport` 2 negros / 1 branco, em vez de
    empilhar o mesmo demográfico num só.

⚠️ As duas nasceram por **cópia literal** da irmã do próprio domínio (Yvonne e
Denise), com **só o `subid` trocado** — 2 linhas de diferença, medidas. É o
único jeito de não herdar `subid` alheio nem redesenhar o layout à mão. A
conferência é do **`subid` renderizado**, nunca do 200.

⚠️ **Cada bridge tem marca própria** no `<title>` e nas páginas legais — Daily
Fact Report, Plain Facts Daily, The Daily Finding, Everyday Digest. São cinco
sites que se parecem, não cinco cópias com o nome trocado.

⛔ **As 8 pastas que migraram foram REMOVIDAS do `bp-dailyvitalreport`**, por
ordem do operador. Corte limpo: manter as URLs velhas vivas seria manter o alvo
grande, que é justamente o que a divisão desfaz.
⚠️ **Consequência:** `dailyvitalreport.store/{denise,wayne,otisgloria}` passou a
dar 404, e as bios dessas 3 páginas no Facebook precisaram ser trocadas.

A raiz de cada domínio serve a mesma matéria **sem** `subid`.

⭐ **O app tem auto-deploy pelo webhook do GitHub App.** O lote 2 subiu sozinho
depois do `git push` no `projetosweb` — não foi preciso chamar
`POST /api/v1/deploy`. Levou menos de 2 minutos entre o push e as 5 URLs
respondendo 200.

✅ **Verificado no ar em 2026-08-05** (`curl` nas 10 URLs): cada uma com 4 links,
`aff_id=44878` em todas e o `subid` próprio de cada página, `hero.jpg` em 200.
⚠️ **200 não prova conteúdo** — a conferência é do `subid` renderizado, não do
código de status: uma pasta copiada sem trocar o `subid` responderia 200 e
mandaria a atribuição para a página errada.

### ⭐ Lote 2 — 2026-08-03: qual página do Facebook usa qual bridge

⛔ **O pareamento é 1:1 e a fonte da verdade é este quadro** (repetido no
[`automacao-comentario-dm.md`](automacao-comentario-dm.md), que é onde o link vai
para dentro da DM).

| Página no Facebook | Bridge | `subid` | UUID Coolify |
|---|---|---|---|
| Hank Male Tips Hub | `secondwindformen.site` | `secondwindformen` | `p6b0bb2bsbychxyzs8m0axzp` |
| Wade All Natural Hub | `strengthandflow.site` | `strengthandflow` | `t8koxrte3s7530p5b6mazkjv` |
| Isaiah Vitality Men Tips | `dailyvitalitymethod.site` | `dailyvitalitymethod` | `tqwepmv042n3y13xiy68ve0v` |
| Curtis Reset Hub | `menresethub.site` | `menresethub` | `u3szzoq1y9vcgoapsi2jnq0e` |
| Otis Men Reset Hub | `mensresetclub.online` | `mensresetclub` | `t9wzm0j2pctbql7tsu3nbbor` |

> ⚠️ **`menresethub.site` (Curtis) NÃO é `manresethub.pro` (Joe).** Uma letra —
> **men** contra **man** — separa duas páginas diferentes, e as duas estão no ar.
> Trocar o link manda a venda do Curtis para a atribuição do Joe, e a notificação
> do Telegram mostra a página errada sem acusar erro nenhum.
>
> ⚠️ **"Wade All Natural Hub" (página) NÃO é `allmensnatural.site` (bridge do
> Chuck).** O nome da página ecoa o domínio de outra; o Wade vai para
> `strengthandflow.site`.

⭐ **Tracking conferido em produção em 2026-08-03**: as 5 servem o próprio `subid`
por padrão (sem depender do `?p=`), `aff_id=45158`, e o circuito
bridge → BuyGoods → Telegram foi testado de ponta a ponta com controles (segredo
inválido barrado, dedup funcionando, subid fora do mapa caindo como slug cru).

Todos os 6 apps: deploy **finished**, servindo HTTP 200 (`index.html` 5.1 KB + `hero.png` 1.6 MB).

### Status em 2026-07-24 — 5 de 6 no ar

`https://<domínio>/bp1/` responde **200 com cert Let's Encrypt válido** e redirect
HTTP→HTTPS nos 5 domínios apontados (manresethub.pro, vitalresetlab.site,
primalvitalityhub.site, allmensnatural.site, steadystrengthhub.site). Falta só o
`wholelifenutri.shop`, ainda no parking (`2.57.91.91`) — apontar o A record.

**Gotcha do cert (resolvido):** os apps foram criados ANTES do DNS apontar, então
o Traefik tentou o ACME, falhou (domínio não resolvia pra VPS) e entrou em
backoff. Depois de apontar o DNS, o cert **não sai sozinho** — foi preciso um
**redeploy** de cada app (`GET /api/v1/deploy?uuid=<uuid>`) pra reaplicar os
labels do Traefik e reemitir o cert na hora. Regra: apontou o DNS → redeploya o
app do Coolify → valida HTTPS.

## Pendência: apontar DNS

Cada domínio ainda está nos nameservers de **parking** (`*.dns-parking.com`). Para ir ao ar no domínio final com SSL, em cada painel de DNS:

- Registro **A** `@` → `159.195.12.135`
- (opcional) Registro **A** `www` → `159.195.12.135`

Após propagação, o Traefik emite o certificado e `https://<dominio>/bp1/` responde.

## Como adicionar uma nova bridge page

1. Criar app via API (`POST /api/v1/applications/private-github-app`) com `base_directory: /bridge-pages/bp1`, `ports_exposes: 80`.
2. Setar FQDN (`PATCH /api/v1/applications/<uuid>` com `domains`).
3. Disparar deploy (`GET /api/v1/deploy?uuid=<uuid>`).
4. Apontar DNS (registro A → VPS).

---

## O SPLIT ETNICO DAS 5 PAGINAS NOVAS (2026-08-05)

**3 avatares brancos · 2 avatares negros.** A decisao e' de VOLUME, e vale
separar duas coisas que se confundem:

- **Prevalencia** de disfuncao eretil e' MAIOR entre homens negros nos EUA —
  puxada pelas comorbidades (diabetes, hipertensao, obesidade).
- **Volume absoluto de compra** e' dos brancos: ~60% da populacao masculina
  adulta contra ~13% de negros. Mesmo com prevalencia menor, o numero de
  compradores e' varias vezes maior.

Para resposta direta o que paga escala e' volume absoluto -> a MAIORIA (branco)
leva 3 paginas, a minoria leva 2. Mesma proporcao das 5 paginas antigas
(Joe/Ray/Matt brancos, Marcus/Chuck negros).

⚠️ RESSALVA HONESTA: prevalencia e populacao sao dados que eu tenho com
confianca; **participacao de mercado por etnia em nutra de ED especificamente
nao e' dado publico que eu conheca** — a divisao acima e' inferencia de volume
populacional. Dado de plataforma (Meta Ads, Buy Goods) ganha desta inferencia.

| Pagina | Avatar | Dominio |
|---|---|---|
| Jason H. | negro, 50s, musculoso | `stridebackmen.site` |
| Philippe Laurent | negro, 50s, musculoso | `morningritualmen.site` |
| Roy Tanner | branco, 55, comum | `menvitalityhub.site` |
| Dean Whitaker | branco, 48, comum | `thefitmenhub.site` |
| Earl Hodge | branco, 60, comum | `menritualhub.site` |

⭐ A ETNIA DA PAGINA TRAVA A ETNIA DO REF DO CRIATIVO (congruencia inviolavel).
Ao acrescentar estas paginas ao `ETNIA` dos motores: Roy/Dean/Earl como
`white American`, Jason/Philippe como `Black American`.
