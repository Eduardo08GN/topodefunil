#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""AGENTE AMISH 16S — a vovo Amish, o antes/depois com DAY em quadro, e o CTA YES.

⭐⭐ FONTE: pagina "Martha.Knows" (Old Nanny Pure Wisdom, 39k seguidores),
78 reels enumerados em 2026-08-21 e os **18 com 50k+ views lidos quadro a
quadro** (legenda karaoke queimada = a copy, palavra por palavra). Nicho:
EMAGRECIMENTO — nao ED. E' o primeiro motor do parque fora do nicho.

O FORMATO, ordem do operador (2026-08-21):
  take 1 — 3s — DAY 1  (o sujeito obeso recebe a colherada)
  take 2 — 3s — DAY 47-57 sorteado (o MESMO sujeito, magro, mesma roupa larga)
  take 3 — 8s — a apresentacao selfie + CTA
⚠️ Os takes saem do gerador com ~8s; os takes 1-2 sao CORTADOS a 3s na edicao.
Por isso a acao deles mora nos TRES PRIMEIROS segundos ("within the first
second...") — o que acontece depois do corte e' custo, nao cena.

⛔⛔ O TETO DE FALA E' CALCULADO, nao chutado. A regra do operador: 14 palavras
em 6s (2,33 p/s) e 24 em 8s (3,0 p/s). Para 3s, pela taxa mais dura:
14/6 x 3 = **7 palavras** (o palpite dele era 6; a conta da' 7). ⭐ Mas os
takes 1-2 nascem **MUDOS por fidelidade**: nos 18 reels lidos, ninguem fala
sobre o antes/depois — a fala inteira mora no selfie. O teto de 7 fica
registrado para o dia em que alguem quiser fala ali.
⚠️ TAKE 3: teto nominal 24 (24/8s). A COPY 1 tem **34 palavras** — verbatim da
fonte (8 dos 18 videos, campea com 331k views) e a ordem foi *"o resto deve
permanecer igual"*. A 3,1 p/s medidos da voz gerada, 34 palavras pedem ~11s:
risco DECLARADO de a cauda cortar. O que corta e' o pedido de share/follow —
o `comment YES` vem no meio e sobrevive. Encurtar e' alcada do operador.

⛔⛔ O DAY E' ESCRITO PELO VEO, NAO NA EDICAO — ordem literal: *"e' o proprio
veo que deve escrever essa legenda no mesmo padrao dos videos originais"*.
Consequencia unica no parque: a trava `SEM_TEXTO_TAKE` do contrato
compartilhado **NAO entra nos takes 1-2** (ela mataria a unica coisa que o
take existe para mostrar) e entra normalmente no take 3, onde texto nenhum e'
bem-vindo. A lente AM4 cobra os dois lados dessa excecao.

⛔ KEYWORD NATIVA = "YES", e isso CONFLITA de proposito com a lista
`BANIDAS_KEYWORD` do short_comum ("yes" quebra a automacao de DM do funil ED).
Este motor e' de OUTRO funil: a pagina nova nasce com a automacao cadastrada
em YES, como a fonte (18 de 18 pedem YES/DRINK/BOOK — e o operador travou:
*"O cta sempre deve ser comentar YES"*). A banida vale para TROCAR no painel;
a nativa deste motor e' decisao dele, registrada aqui.

⛔⛔ SEM BLOCO 0 (REF), desde 2026-08-21 — ordem: *"a referencia deve ser
baseada direto na imagem 1 [...] gere a imagem 2 e 3 a partir da imagem 1 que
irei anexar como base. Dessa forma eu economizo tempo."* A IMAGE 01 e' a unica
descricao completa; as IMAGEs 02/03 sao instrucoes de EDICAO sobre ela, e a
lente AM8 cobra as ancoras (`Using the provided image`, `Change ONLY`...).

⭐ AS 4 COPIES SAO AS VALIDADAS NA FONTE, renumeradas por uso e views:
  1 — resultados (8/18 usos · 331k+184k+110k+109k+88k+61k+56k+54k)
  2 — colher + receita (2/18 · 88k+76k)
  3 — Johnny secreto (1/18 · 70k)
  4 — colher + comprar (1/18 · 67k)
⛔ A unica variacao permitida: nome do personagem e ele/ela conforme o sexo
do sujeito. O resto e' constante e a lente AM2 cobra verbatim.

    python funil-organico/amish16_short.py --pagina clara --n 3
    python funil-organico/amish16_short.py --autoteste
    python funil-organico/amish16_short.py --stats
"""
import argparse
import io
import json
import os
import random
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
if AQUI not in sys.path:
    sys.path.insert(0, AQUI)

import short_comum as sc                                        # noqa: E402
from nucleo_sonoro import sonorizar                             # noqa: E402

TITULO = "AGENTE AMISH 16S"
SLUG = "amish-16s"
SUBTITULO = ("4 takes (4s + 4s + 8s + 6s) · o antes/depois · a vovo Amish e "
             "mais oito narradores · CTA YES · a legenda DAY sai no editor")

LEDGER = os.path.join(AQUI, ".amish-16s-ledger.json")

# ⚠️ A quarta caixa nasce VAZIA nas copies 2/3/4, que saem em tres takes —
# o rotulo diz isso para a caixa vazia nao parecer copy perdida.
CENAS_UI = ["1 · DAY 1 (mudo)", "2 · o depois (mudo)",
            "3 · o CTA", "4 · CTA parte 2 (so' na copy 1)"]

# ⛔⛔ QUATRO TAKES, TRES IMAGENS — o TAKE 04 anima a MESMA IMAGE 03 (a
# selfie). Ordem do operador (2026-08-21, gravacao de 21 min): *"caso nao
# seja possivel falar tudo dentro de 8 segundos, ai' voce ira' ajustar o
# agente para que gere 4 takes ao inves de 3"*.
# ⭐ E ele nao foi possivel — MEDIDO por ele em campo, nao estimado: das 4
# geracoes do TAKE 3 com a COPY 1 (34 palavras), TRES cortaram na MESMA
# palavra (`video`, a 28a) e so' uma falou inteira. 28 palavras em 8s.
IMAGENS = ("IMAGE 01/03", "IMAGE 02/03", "IMAGE 03/03")
# ⚠️ `TAKES` e' o caso de QUATRO e continua existindo porque metade do
# arquivo o referencia; o numero real de um video sai de `takes_do(spec)`.
TAKES = ("TAKE 01/04", "TAKE 02/04", "TAKE 03/04", "TAKE 04/04")


def n_takes(spec):
    """3 ou 4, decidido pela COPY sorteada (2026-08-21).

    ⭐ Quatro so' quando a fala NAO cabe nos 8s do take 3. Ordem dele:
    *"quando eu travar ou sortear as copys 2, 3, 4 sejam geradas somente em
    3 takes"* — e a razao que ele deu e' aritmetica, nao gosto: elas tem 24
    palavras ou menos.
    ⛔ Quem responde e' a fala montada, nao o id da copy: `spec["falas"][3]`
    so' e' preenchida quando a divisao foi necessaria.
    """
    return 4 if (spec.get("falas") or ["", "", "", ""])[3] else 3


def takes_do(spec):
    """Os rotulos de take DESTE video, ja' numerados /03 ou /04.

    ⛔ Existe porque o rotulo mente se ficar fixo: um video de tres takes
    com `TAKE 03/04` manda o operador procurar um quarto que nao existe —
    e foi exatamente essa a duvida dele quando o motor passou a 4 takes
    (*"so' esta' gerando 3 imagens"*). Rotulo e' contrato.
    """
    n = n_takes(spec)
    return tuple("TAKE 0%d/0%d" % (i + 1, n) for i in range(n))

# ⛔ O RELOGIO, medido por ele no proprio Veo: *"o Veo so' da' o limite
# minimo aqui, o mais curto e' quatro"* — os takes 1-2 nascem com 4s e sao
# cortados a ~3s na edicao. E *"todos os videos precisam ter no maximo 20
# segundos"*: 3 + 3 + 8 + 6 = 20 no arquivo final.
SEGUNDOS_TAKE = {1: 4, 2: 4, 3: 8, 4: 6}
TAXA = 3.0                        # palavras/s — a regra dele (24 em 8s)
# ⛔ takes 1-2 sao MUDOS (a musica entra no editor), entao teto 0.
TETO_FALA = {1: 0, 2: 0,
             3: int(SEGUNDOS_TAKE[3] * TAXA),      # 24
             4: int(SEGUNDOS_TAKE[4] * TAXA)}      # 18

# ⛔ As paginas aqui sao o CONTRATO DE UI (botao de pele), nao paginas reais
# do Facebook: o motor nasce antes da pagina. `clara`/`escura` definem o
# DEFAULT de pele de narrador e sujeito; as travas do painel vencem.
ETNIA = {"clara": "white American", "escura": "Black American"}
PELES = {"branca": "white American", "negra": "Black American"}

# ⛔⛔ O CTA E' SEMPRE YES — ordem do operador (2026-08-21): *"o cta desse
# agente deve ser sempre a palavra yes"*. O campo de keyword da UI NAO
# aparece (KEYWORD_UI=False) e nao ha' substituicao em lugar nenhum: a
# palavra vive escrita dentro das quatro copies verbatim e a AM2 cobra o
# literal `comment YES`.
# ⚠️ A automacao de DM da pagina nova tem de nascer cadastrada em YES.
KEYWORD_UI = False
KEYWORD_NATIVA = "YES"

# ⭐ [LOCAL LUCAS] o seletor pele/pagina do topo NAO aparece neste motor —
# as paginas aqui sao sinteticas (contrato de UI) e a pele ja' tem DUAS
# travas proprias no painel (narrador e sujeito). Dois controles para a
# mesma trava e' a copia espelhada que diverge na semana seguinte.
SEM_SELETOR_PAGINA = True

DIA_MIN, DIA_MAX = 47, 57
# ⛔⛔ 380-420 kg DESDE 21/08 — e' a faixa do prompt que ele carimbou como
# *"absurdamente perfeito"*, que sai em **880 lb** (≈ 399 kg). Isso SUPERA a
# ordem de mais cedo no mesmo dia (*"aumente esse numero de peso para 240-280
# kg"*), e a superacao e' o proprio teste de campo dele: registrar o prompt
# aprovado mantendo a faixa antiga entregaria 570 lb, ou seja, outra coisa.
# ⚠️ A faixa e' larga de proposito — 838 a 926 lb — para o eixo continuar
# sorteando; 880 e' o centro, nao um valor fixo.
PESO_MIN, PESO_MAX = 380, 420      # kg — no prompt vai em lb

# ⛔⛔ O SUJEITO QUE MUDA TEM 50 OU MAIS — ordem de 2026-08-23: *"a idade
# das pessoas que sofrem a mudanca seja sempre acima de 50 anos, entao remova
# as pessoas e caracteristicas que nao combinarem, que representarem mais
# pessoas americanas jovens"*.
# ⚠️ Apagar nao servia: 25 dos 46 estavam abaixo, e 18 das 24 mulheres —
# deletar levaria o pool feminino a SEIS e destruiria a paridade 16/16/16/16
# fechada no dia anterior. O que saiu foi a CARACTERISTICA jovem, nao a
# pessoa: cada penteado ganhou marca de idade (grisalho, prateado, branco nas
# temporas) e a idade subiu. Um punk de 57 de moicano grisalho e' personagem
# melhor que um punk de 38 apagado.
# ⭐ O publico do nicho tem a idade do sujeito: mulher e homem de 45 a 65
# querendo emagrecer. Corpo-prova de 31 anos nao e' espelho de ninguem la'.
IDADE_MIN_SUJEITO = 50

# ⛔ Contrato do `lint_copy16`/`medir_copy16`: NUCLEO e' o pool de apelidos do
# orgao. Este motor e' de EMAGRECIMENTO — nao ha' orgao, nao ha' apelido.
# Lista vazia e' declaracao, nao esquecimento.
NUCLEO = []


# ===========================================================================
# NARRADORES — os nove que o operador ditou, um a um
# ===========================================================================
# ⛔ Cada rosto tem ARQUITETURA (formato, nariz, marca) — rosto generico
# deriva para a media do treino, e a media tem nome. Doutrina de 2026-08-10;
# zero negacao de celebridade em lugar nenhum.
# ⚠️ `pele_fixa`: indigenas e curandeiros africanos tem identidade que a trava
# de pele NAO pode trocar. A trava e' IGNORADA COM AVISO — botao que cede em
# silencio e' o defeito que o GO21 ja' pagou; aqui ele avisa.
NARRADORES = [
    # ⭐⭐ `receita` / `receita_pt` — 2026-08-22, ordem dele com o painel
    # aberto no indio anciao: *"quando eu selecionar quem narra, esse
    # trecho da copy 2 deve ser correspondente a vocacao do narrador,
    # no caso aqui muda de bebida Amish para bebida indigena"*.
    # ⛔ A palavra `Amish` estava CRAVADA na copy 2, entao a anciã
    # indigena, a freira e a root doctor mandavam o espectador pedir
    # uma receita amish — a fala desmentindo a imagem no mesmo video.
    # ⚠️ E \'e um EIXO, nao um `if`: narrador novo declara a
    # bebida dele na propria entrada, e quem esquecer e \'acusado pela
    # AM15. Ver tambem `dados_amish16.py`, que precisa do termo no
    # glossario, senao a traducao cai para "≈ aproximada".
    # ⛔ TRES SAIRAM EM 2026-08-22, por ordem: *"quero que exclua os
    # personagens doutores de 40, moca de 25 anos"*. Eram `doutora`,
    # `doutor` e `moca_verao`.
    # ⚠️ A lapide fica porque a razao e' estrutural e vale para quem
    # vier: os tres eram os UNICOS do pool sem as cinco propriedades
    # que fazem a vovo Amish funcionar — medico tem autoridade
    # MODERNA (compete com o sistema em vez de passar por fora) e a
    # moca de 25 nao tem saber antigo nem corpo-prova de idade.
    # Repor um deles e' repor o furo.
    {"id": "vovo_amish", "receita": "Amish", "receita_pt": "Amish", "mundo": "amish", "rotulo": "vovo Amish (a ancora)", "sexo": "f",
     "pele_fixa": None,
     "voz": "a warm, cracked elderly woman's voice",
     "desc": ("an elderly Amish %(pele)s woman in her late seventies, a long "
              "deeply lined face with high cheekbones, a narrow straight nose "
              "and pale gray eyes, small pearl-drop earrings, wearing a plain "
              "%(cor)s dress with a white lace-trimmed bonnet and a white bow "
              "tied at her collar")},
    {"id": "vovo_amish_h", "receita": "Amish", "receita_pt": "Amish", "mundo": "amish", "rotulo": "vovo Amish homem (75)", "sexo": "m",
     "pele_fixa": None,
     "voz": "a deep, unhurried elderly man's voice",
     "desc": ("a 75-year-old Amish %(pele)s man with a long white beard and "
              "no mustache, a square weathered face with deep-set eyes under "
              "heavy white brows, wearing a straw hat, a plain collarless "
              "white shirt and dark suspenders")},
    {"id": "india_anciana", "receita": "Native American", "receita_pt": "indígena", "mundo": "amish", "rotulo": "india anciana de 80", "sexo": "f",
     "pele_fixa": "Native American",
     "voz": "a low, steady elderly woman's voice",
     "desc": ("an 80-year-old Native American elder woman with long silver "
              "braids, a broad deeply lined face with high flat cheekbones "
              "and dark hooded eyes, wearing traditional beaded regalia with "
              "a woven shawl over her shoulders")},
    {"id": "indio_anciao", "receita": "Native American", "receita_pt": "indígena", "mundo": "amish", "rotulo": "indio anciao de 80", "sexo": "m",
     "pele_fixa": "Native American",
     "voz": "a deep, gravelly elderly man's voice",
     "desc": ("an 80-year-old Native American elder man with long silver "
              "hair, a broad lined face with a strong straight nose and "
              "hooded eyes, wearing traditional regalia with beadwork and a "
              "bone-bead breastplate")},
    {"id": "curandeira_africana", "receita": "African", "receita_pt": "africana", "mundo": "amish", "rotulo": "curandeira africana de 80",
     "sexo": "f", "pele_fixa": "Black African",
     "voz": "a warm, resonant elderly woman's voice",
     "desc": ("an 80-year-old African healer woman, a round deeply lined "
              "face with wide-set eyes, her white hair wrapped in a printed "
              "headwrap, wearing traditional printed robes with layered "
              "beaded necklaces")},
    {"id": "curandeiro_africano", "receita": "African", "receita_pt": "africana", "mundo": "amish", "rotulo": "curandeiro africano de 80",
     "sexo": "m", "pele_fixa": "Black African",
     "voz": "a deep, warm elderly man's voice",
     "desc": ("an 80-year-old African healer man with a short white beard, a "
              "lean deeply lined face with a broad nose, wearing traditional "
              "healer robes with cowrie-shell necklaces")},
    # ⭐⭐ AS TRES IDENTIDADES NOVAS — 2026-08-21, escolhidas contra o
    # MECANISMO da vovo Amish, nao por serem folcloricas. As cinco
    # propriedades que ela tem e que estas repetem: reconhecimento em 200ms
    # pela silhueta, saber PRE-MODERNO (velho, nao inventado), mensageiro
    # que NAO VENDE, comunidade FECHADA (que responde sozinha ao *"por que
    # eu nunca ouvi falar disso?"*) e — a que mais elimina candidato — a
    # comunidade EXISTE HOJE, entao a receita esta' disponivel agora.
    # ⛔ Por isso `pioneira da pradaria` e `velho oeste` ficaram de fora: sao
    # museu, e museu nao entrega receita que o espectador use amanha.
    # ⛔⛔ E CADA UMA ARRASTA O PROPRIO MUNDO. Freira num celeiro com bandeira
    # americana le' como FANTASIA, nao como vocacao — e vocacao legivel foi
    # o pedido dele (*"com suas roupas tipicas para deixar nitido sua
    # classe/vocacao"*). Ver o campo `mundo` e a lente AM14.
    {"id": "granny_apalache", "receita": "Appalachian", "receita_pt": "apalache", "mundo": "apalache",
     "rotulo": "granny woman apalache — MULHER (74)", "sexo": "f",
     # ⛔ pele TRAVADA: as `granny women` das hollows sao uma tradicao branca
     # escocesa-irlandesa. Travar e' honesto; sortear seria fantasia.
     # ⚠️ 74 anos: velha o bastante para uma vida de pratica, nova o
     # bastante para ainda estar atendendo — o pico de credibilidade do
     # arquetipo. Mais que isso vira personagem de museu.
     "pele_fixa": "white American",
     "voz": "a thin, reedy elderly woman's voice with a soft mountain drawl",
     "desc": ("a 74-year-old white American mountain granny woman from the "
              "Appalachian hollows, a narrow deeply lined face with sharp "
              "cheekbones, thin lips and steady watchful eyes, her white "
              "hair pinned up in a loose bun with wisps escaping, wearing a "
              "faded %(cor)s calico dress under a worn white cotton apron, "
              "wire-rimmed spectacles and a hand-knitted shawl around her "
              "shoulders")},
    {"id": "freira", "receita": "convent", "receita_pt": "do convento", "mundo": "convento", "rotulo": "freira — MULHER (80)",
     "sexo": "f",
     # ⚠️ 80 anos por ORDEM dele (*"a freira eu quero idosa, 80 anos"*).
     # ⚠️ pele LIVRE: habito nao tem etnia, e freira idosa existe em toda
     # cor — travar aqui fecharia a identidade a uma pagina so'.
     # ⛔ E o `%(cor)s` do vestido NAO entra: o habito e' preto e branco, e
     # um `habito roxo` seria a cor sorteada mentindo sobre a vocacao.
     "pele_fixa": None,
     "voz": "a gentle, papery elderly woman's voice",
     "desc": ("an 80-year-old %(pele)s Catholic nun, a small deeply lined "
              "face with soft round cheeks and calm eyes behind thin "
              "wire-rimmed glasses, wearing a full black habit with a long "
              "black veil over a stiff white coif and a starched white "
              "wimple framing her face, a simple wooden crucifix on a cord "
              "at her chest")},
    {"id": "root_doctor", "receita": "Gullah", "receita_pt": "Gullah", "mundo": "gullah",
     "rotulo": "root doctor Gullah — MULHER (78)", "sexo": "f",
     # ⭐ E' a unica das tres que resolve o lado NEGRO do funil sem parecer
     # copia da amish: Gullah Geechee sao AMERICANOS, nao africanos — o pool
     # ja' tinha curandeira AFRICANA e nao tinha uma ancia negra AMERICANA.
     # ⚠️ 78 anos: root doctor ganha autoridade com idade, e a cesta de
     # sweetgrass na dobra do braco e' o marcador de oficio.
     "pele_fixa": "Black American",
     "voz": ("a deep, unhurried elderly woman's voice with a low Sea Island "
             "lilt"),
     "desc": ("a 78-year-old Black American root doctor from the Gullah Sea "
              "Islands, a broad deeply lined face with high cheekbones and "
              "steady dark eyes, her white hair wrapped in a bright %(cor)s "
              "headwrap tied at the front, wearing a loose long-sleeve work "
              "dress under a burlap apron, small brass hoop earrings, and a "
              "woven sweetgrass basket of dried roots hooked over one arm")},
]

# ⭐ A ANCORA VARIA SO' NA COR DO VESTIDO — ordem: *"mude somente as cores da
# roupa dela"*. O roxo e' o original; o vinho apareceu na propria fonte.
CORES_VESTIDO = ["deep purple", "dark burgundy red", "navy blue",
                 "forest green", "chocolate brown", "slate blue"]


# ===========================================================================
# SUJEITOS — quem passa pelo antes/depois (looks lidos dos 18 reels)
# ===========================================================================
# ⛔ O look NAO diz pele nem sexo: pele vem da trava/pagina, sexo da trava.
# Cada entrada e' cabelo+roupa+idade — o que sobrevive ao emagrecimento e
# ancora a continuidade entre os dois quadros gerados separadamente.
SUJEITOS_H = [
    {"id": "grisalho_macacao", "pele": ("branca",), "rotulo": "grisalho de macacao", "idade": 62,
     "rosto": "a broad square face with a heavy jaw, deep-set blue eyes under bushy brows, a wide flat nose and weather-worn skin",
     "visual": "shoulder-length gray hair and a thick gray mustache",
     "roupa": "a thin red plaid short-sleeve shirt"},
    {"id": "cabeludo_oculos", "pele": ("branca", "negra"), "rotulo": "cabeludo de oculos laranja",
     "idade": 55,
     "rosto": "a long oval face with a high forehead, close-set brown eyes, a narrow hooked nose and smooth skin",
     "visual": "long dark curly hair, a dark mustache and orange-tinted "
               "glasses",
     "roupa": "a thin white short-sleeve shirt"},
    {"id": "calvo_oculos", "pele": ("branca", "negra"), "rotulo": "calvo de oculos", "idade": 60,
     "rosto": "a round face with full cheeks, small hazel eyes, a short blunt nose and a cleft chin",
     "visual": "a balding head with neat side hair and rectangular glasses",
     "roupa": "a thin plain white short-sleeve button shirt"},
    {"id": "careca", "pele": ("branca", "negra"), "rotulo": "careca", "idade": 52,
     "rosto": "a wide moon face with a low brow, small dark eyes, a bulbous nose and heavy flushed cheeks",
     "visual": "a completely bald head and a clean-shaven round face",
     "roupa": "a thin white short-sleeve shirt with a gray stripe"},
    {"id": "ruivo_estampada", "pele": ("branca",), "rotulo": "ruivo de camisa estampada",
     "idade": 50,
     "rosto": "a square freckled face with a strong chin, pale green eyes, a broad straight nose and reddened cheeks",
     "visual": "curly red hair and a bushy red mustache",
     "roupa": "a thin loud pink-and-blue patterned short-sleeve shirt"},
    {"id": "franjinha", "pele": ("branca",), "rotulo": "franjinha de polo", "idade": 58,
     "rosto": "a narrow face with a pointed chin, gray-blue eyes, a thin straight nose and hollow cheeks",
     "visual": "thin combed-back brown hair and small round glasses",
     "roupa": "a thin plain white polo shirt"},
    {"id": "coroa_social", "pele": ("branca", "negra"), "rotulo": "coroa de camisa social", "idade": 65,
     "rosto": "a heavy rectangular face with jowls, brown eyes under drooping lids, a wide nose and a weathered complexion",
     "visual": "short gray hair and bushy gray eyebrows",
     "roupa": "a thin light blue short-sleeve button shirt"},
    {"id": "barbudo", "pele": ("branca", "negra"), "rotulo": "barbudo de flanela", "idade": 53,
     "rosto": "a broad face with high cheekbones, dark brown eyes, a straight nose and sun-weathered skin",
     "visual": "a full brown beard going gray and shaggy brown hair",
     "roupa": "a thin green-and-black checked short-sleeve shirt"},
    # ⭐⭐ OS TRES HOMENS NEGROS — 2026-08-21, ordem dele depois de a trava
    # de pele passar a funcionar: *"quero a mesma quantidade de variacoes
    # para homens negros e brancos e mulheres negras e brancas"*.
    # ⛔ Sao `("negra",)` de proposito: locs, afro e trancas nao sao
    # penteado neutro, e fingir que sao repete em outro endereco o erro que
    # este bloco existe para consertar.
    # ⚠️ Cada rosto e' ARQUITETURA (mandibula, arcada, ossos, nariz), nunca
    # rosto generico — rosto generico deriva para a media do treino, e a
    # media tem nome. Zero token de coloracao: a cor vem do eixo de pele.
    {"id": "careca_barba", "pele": ("negra",), "rotulo": "careca de barba grisalha",
     "idade": 66,
     "rosto": "a long face with a heavy square jaw, deep-set dark eyes under a strong brow ridge, a wide flat nose and a deeply lined forehead",
     "visual": "a shaved head and a full close-cropped gray beard",
     "roupa": "a thin cream short-sleeve button shirt"},
    {"id": "dread_grisalho", "pele": ("negra",), "rotulo": "locs grisalhos",
     "idade": 54,
     "rosto": "a broad face with prominent cheekbones, wide-set dark eyes, a rounded nose with flared nostrils and a full mouth",
     "visual": "shoulder-length locs going gray at the temples and a clean-shaven face",
     "roupa": "a thin navy short-sleeve shirt with a chest pocket"},
    {"id": "bigode_boina", "pele": ("negra",), "rotulo": "bigode e boina",
     "idade": 59,
     "rosto": "an angular face with a narrow chin, small dark eyes, a straight bridged nose and deep smile lines",
     "visual": "a thick salt-and-pepper mustache and a flat cap",
     "roupa": "a thin brown-and-tan striped short-sleeve shirt"},
    # ⭐⭐ ONZE HOMENS NOVOS — 2026-08-22, ordem dele: *"estao gerando muito
    # parecidos, mude as caracteristicas fisicas, roqueiros, punks, countrys,
    # loiras, ruivas e ruivos, olhos azuis"*. O pool masculino sai de 11 para
    # 22 e a paridade continua 16 brancos / 16 negros.
    # ⛔ Quem carrega coloracao europeia (ruivo, loiro, olho azul) e
    # `("branca",)` — e a AM12 acusa quem marcar o contrario, porque cinco
    # tokens de coloracao vencem uma trava de pele, medido em 21/08.
    # ⚠️ Cada rosto e ARQUITETURA e nenhuma se repete: mandibula, arcada,
    # ossos, nariz, queixo. Rosto generico deriva para a media do treino.
    {"id": "roqueiro_cabeludo", "pele": ("branca", "negra"),
     "rotulo": "roqueiro cabeludo", "idade": 58,
     "rosto": "a long face with a heavy brow ridge, deep-set dark eyes, a strong hooked nose and a wide thin-lipped mouth",
     "visual": "long gray-streaked hair past the shoulders and thick sideburns",
     "roupa": "a faded black band t-shirt"},
    {"id": "punk_moicano", "pele": ("branca", "negra"),
     "rotulo": "punk de moicano", "idade": 57,
     "rosto": "a narrow angular face with a pointed chin, close-set dark eyes, a thin straight nose and hollow temples",
     "visual": "a tall graying mohawk and stretched earlobe plugs, clean-shaven",
     "roupa": "a black sleeveless t-shirt with a torn collar"},
    {"id": "country_chapeu", "pele": ("branca", "negra"),
     "rotulo": "country de chapeu", "idade": 57,
     "rosto": "a square face with a heavy jaw, dark eyes under low brows, a broad nose and deep creases running to the mouth",
     "visual": "a straw cowboy hat over short dark hair and a thick dark mustache",
     "roupa": "a checked western shirt with pearl snap buttons"},
    {"id": "motoqueiro_bandana", "pele": ("branca", "negra"),
     "rotulo": "motoqueiro de bandana", "idade": 61,
     "rosto": "a broad blunt face with a wide jaw, small dark eyes, a flattened nose and heavy folded eyelids",
     "visual": "a dark bandana tied over the head and a long gray goatee",
     "roupa": "a black t-shirt with a faded eagle print"},
    {"id": "pescador_bone", "pele": ("branca", "negra"),
     "rotulo": "pescador de bone", "idade": 63,
     "rosto": "a wide face with fleshy cheeks, hooded dark eyes, a bulbous nose and a dimpled chin",
     "visual": "a worn mesh trucker cap over gray hair and short gray stubble",
     "roupa": "a washed-out olive fishing shirt"},
    {"id": "ruivo_barba_cheia", "pele": ("branca",),
     "rotulo": "ruivo de barba cheia", "idade": 52,
     "rosto": "an oval freckled face with a soft jaw, pale green eyes, a short upturned nose and ruddy cheeks",
     "visual": "buzzed red hair going gray at the temples and a full red beard shot through with white",
     "roupa": "a green flannel short-sleeve shirt"},
    {"id": "loiro_rabicho", "pele": ("branca",),
     "rotulo": "loiro de rabicho", "idade": 51,
     "rosto": "a long face with a square chin, pale blue eyes, a straight narrow nose and fair weathered skin",
     "visual": "long blond hair tied in a low ponytail and a blond goatee",
     "roupa": "a gray sleeveless t-shirt"},
    {"id": "punk_espetado", "pele": ("branca",),
     "rotulo": "punk de cabelo espetado", "idade": 54,
     "rosto": "a lean triangular face with sharp cheekbones, pale blue eyes, a thin nose and a small pointed chin",
     "visual": "short spiked steel-gray hair and a safety-pin earring",
     "roupa": "a black t-shirt covered in band patches"},
    {"id": "locs_barbudo", "pele": ("negra",),
     "rotulo": "locs com barba", "idade": 60,
     "rosto": "a broad face with a strong square jaw, wide dark eyes, a rounded nose with flared nostrils and full lips",
     "visual": "long locs gathered back and a thick black beard streaked with gray",
     "roupa": "a burgundy short-sleeve henley shirt"},
    {"id": "careca_cavanhaque", "pele": ("negra",),
     "rotulo": "careca de cavanhaque", "idade": 55,
     "rosto": "a round face with heavy cheeks, deep-set dark eyes, a wide flat nose and a broad chin",
     "visual": "a shaved head, a neat black goatee and a small gold stud earring",
     "roupa": "a charcoal short-sleeve polo shirt"},
    {"id": "trancinhas_h", "pele": ("negra",),
     "rotulo": "trancinhas coladas", "idade": 55,
     "rosto": "an angular face with high sharp cheekbones, narrow dark eyes, a straight bridged nose and a firm chin",
     "visual": "salt-and-pepper cornrows braided straight back and a thin gray mustache",
     "roupa": "a white short-sleeve baseball jersey"},
]
SUJEITOS_M = [
    {"id": "ruiva_regata", "pele": ("branca",), "rotulo": "ruiva de regata azul", "idade": 50,
     "rosto": "a round freckled face with soft cheeks, green eyes, a small upturned nose and fair skin",
     "visual": "long curly red hair with white at the temples",
     "roupa": "a light blue tank top"},
    {"id": "ruiva_amarelo", "pele": ("branca",), "rotulo": "ruiva de top amarelo", "idade": 53,
     "rosto": "an oval face with a rounded chin, hazel eyes, a straight narrow nose and freckled fair skin",
     "visual": "long curly red hair faded and threaded with white",
     "roupa": "a yellow tank top"},
    {"id": "loira_rabo", "pele": ("branca",), "rotulo": "loira de rabo baixo", "idade": 54,
     "rosto": "a square face with a firm jaw, pale blue eyes, a small straight nose and light skin",
     "visual": "faded blond hair going white, in a low ponytail",
     "roupa": "a white blouse"},
    {"id": "morena_solta", "pele": ("branca", "negra"), "rotulo": "morena de cabelo solto", "idade": 61,
     "rosto": "a long face with a narrow chin, dark brown eyes, a slim straight nose and smooth even skin",
     "visual": "long straight dark hair heavily streaked with silver",
     "roupa": "a lavender t-shirt"},
    {"id": "cacheada_curta", "pele": ("branca", "negra"), "rotulo": "cacheada curta", "idade": 63,
     "rosto": "a round face with full cheeks, dark eyes, a short broad nose and warm skin",
     "visual": "short tight curls gone silver",
     "roupa": "a thin chambray short-sleeve shirt"},
    {"id": "grisalha_floral", "pele": ("branca",), "rotulo": "grisalha de blusa floral",
     "idade": 58,
     "rosto": "a heart-shaped face with a pointed chin, gray-green eyes, a fine straight nose and pale skin",
     "visual": "shoulder-length gray-streaked hair",
     "roupa": "a floral print blouse"},
    {"id": "ruiva_gola", "pele": ("branca",), "rotulo": "ruiva de gola alta", "idade": 51,
     "rosto": "an oval face with high cheekbones, amber eyes, a small nose and freckled skin",
     "visual": "curly auburn hair going gray at the temples",
     "roupa": "a high-collar white button blouse"},
    {"id": "coque_verde", "pele": ("branca", "negra"), "rotulo": "coque de blusa verde", "idade": 62,
     "rosto": "a broad face with a soft jaw, brown eyes, a rounded nose and soft full cheeks",
     "visual": "gray-streaked dark hair in a loose bun",
     "roupa": "a green summer top"},
    # ⭐⭐ AS CINCO MULHERES NEGRAS — mesma ordem de 21/08. Cinco aqui e tres
    # homens la' porque a paridade e' POR SEXO: o pool feminino nascera' com
    # quatro ruivas e uma loira, e so' tres das oito serviam em negra.
    {"id": "trancas_longas", "pele": ("negra",), "rotulo": "trancas longas",
     "idade": 59,
     "rosto": "an oval face with a defined jawline, large dark eyes, a small rounded nose and full lips",
     "visual": "long gray box braids worn loose",
     "roupa": "a coral tank top"},
    {"id": "black_power", "pele": ("negra",), "rotulo": "black power",
     "idade": 60,
     "rosto": "a round face with soft cheeks, wide dark brown eyes, a broad nose and a small pointed chin",
     "visual": "a large round afro gone mostly silver",
     "roupa": "a mustard t-shirt"},
    {"id": "bob_liso", "pele": ("negra",), "rotulo": "bob liso", "idade": 52,
     "rosto": "a square face with a firm jaw, dark almond eyes, a straight narrow nose and pronounced laugh lines",
     "visual": "a chin-length straight bob with a side part",
     "roupa": "a thin white short-sleeve blouse"},
    {"id": "grisalha_curta", "pele": ("negra",), "rotulo": "grisalha de cabelo curto",
     "idade": 60,
     "rosto": "a heart-shaped face with a narrow chin, dark deep-set eyes, a fine straight nose and a high forehead",
     "visual": "very short natural gray hair",
     "roupa": "a soft teal short-sleeve blouse"},
    {"id": "twists_rabo", "pele": ("negra",), "rotulo": "twists em rabo baixo",
     "idade": 57,
     "rosto": "a long face with high angular cheekbones, dark eyes, a slim nose with a rounded tip and a wide mouth",
     "visual": "shoulder-length gray twists gathered in a low ponytail",
     "roupa": "a striped short-sleeve top"},
    # ⭐⭐ ONZE MULHERES NOVAS — mesma ordem de 22/08. O pool feminino sai de
    # 13 para 24, e a paridade continua 16 brancas / 16 negras.
    {"id": "roqueira_franja", "pele": ("branca", "negra"),
     "rotulo": "roqueira de franja", "idade": 55,
     "rosto": "a heart-shaped face with a narrow chin, dark eyes ringed with heavy liner, a small straight nose and sharp cheekbones",
     "visual": "long gray-streaked hair with a heavy blunt fringe",
     "roupa": "a black band t-shirt with a cracked print"},
    {"id": "punk_raspada", "pele": ("branca", "negra"),
     "rotulo": "punk de lateral raspada", "idade": 54,
     "rosto": "a square face with a strong jaw, wide dark eyes, a small nose with a nose ring and a short forehead",
     "visual": "one side of the head shaved and the rest long and gray-streaked",
     "roupa": "a sleeveless black t-shirt with a hand-cut neckline"},
    {"id": "country_trancas", "pele": ("branca", "negra"),
     "rotulo": "country de trancas", "idade": 51,
     "rosto": "a round face with full cheeks, dark eyes, a short straight nose and a dimpled chin",
     "visual": "two long gray-streaked braids under a straw cowboy hat",
     "roupa": "a red checked western shirt"},
    {"id": "motoqueira_couro", "pele": ("branca", "negra"),
     "rotulo": "motoqueira de couro", "idade": 52,
     "rosto": "a long face with a firm jaw, deep-set dark eyes, a straight nose and lines at the corners of the mouth",
     "visual": "dark hair pulled into a high ponytail",
     "roupa": "a black t-shirt under an open leather vest"},
    {"id": "caminhoneira_bone", "pele": ("branca", "negra"),
     "rotulo": "caminhoneira de bone", "idade": 58,
     "rosto": "a broad face with heavy cheekbones, small dark eyes, a wide nose and a set mouth",
     "visual": "dark gray hair tucked under a mesh cap, no makeup",
     "roupa": "a loose gray work t-shirt"},
    {"id": "loira_bob", "pele": ("branca",),
     "rotulo": "loira de bob platinado", "idade": 57,
     "rosto": "an oval face with a soft chin, pale blue eyes, a small upturned nose and fair skin",
     "visual": "a short platinum-and-silver bob",
     "roupa": "a pale pink short-sleeve blouse"},
    {"id": "ruiva_ondulada", "pele": ("branca",),
     "rotulo": "ruiva de cabelo ondulado", "idade": 52,
     "rosto": "a round freckled face with soft cheeks, green eyes, a small straight nose and fair reddened skin",
     "visual": "long wavy red hair dulled with gray at the roots",
     "roupa": "a cream short-sleeve blouse"},
    {"id": "punk_rosa", "pele": ("branca",),
     "rotulo": "punk de pontas rosa", "idade": 56,
     "rosto": "a triangular face with a pointed chin, pale blue eyes, a thin nose and a small mouth",
     "visual": "short choppy silver hair with the ends dyed deep violet",
     "roupa": "a faded black t-shirt with a torn hem"},
    {"id": "bantu_knots", "pele": ("negra",),
     "rotulo": "bantu knots", "idade": 58,
     "rosto": "a round face with high full cheeks, large dark eyes, a broad nose and a small rounded chin",
     "visual": "silver-streaked hair in neat bantu knots and large gold hoop earrings",
     "roupa": "a bright teal short-sleeve top"},
    {"id": "crespo_volumoso", "pele": ("negra",),
     "rotulo": "crespo volumoso", "idade": 50,
     "rosto": "a long face with sharp angular cheekbones, deep-set dark eyes, a narrow nose and a strong jaw",
     "visual": "big natural curls piled high off the face",
     "roupa": "a rust orange short-sleeve blouse"},
    {"id": "tranca_lateral", "pele": ("negra",),
     "rotulo": "tranca lateral grossa", "idade": 56,
     "rosto": "a square face with a wide jaw, steady dark eyes, a rounded nose and full lips",
     "visual": "one thick gray braid pulled over the shoulder",
     "roupa": "a navy short-sleeve work shirt"},
]


def sujeitos_do_sexo(spec):
    """Pool de QUEM MUDA conforme o sexo travado/sorteado — contrato da UI."""
    return SUJEITOS_H if spec.get("sexo_sujeito") == "homem" else SUJEITOS_M


sujeitos_do_sexo.recebe_spec = True

# ⚠️ Pool combinado so' para inventario (--stats e paineis que listam tudo).
SUJEITOS = SUJEITOS_H + SUJEITOS_M


# ===========================================================================
# CENARIOS — 12 rotacoes do mundo-fonte (fazenda Amish, bandeira, cavalos)
# ===========================================================================
# ⛔ Ordem: *"os cenarios devem sempre mudar, mas ser parecidos com o original
# que funcionou, sempre rotacionando e inovando"*. Todos sao o MESMO mundo —
# fazenda Amish de verao — trocando o fundo. A bandeira americana e' quase
# constante na fonte e fica em 10 dos 12.
#
# ⛔⛔ NADA ATRAVESSA O QUADRO — 2026-08-21, gravacao de tela do operador.
# ===========================================================================
# Ele filmou os quatro takes de um mesmo video e mostrou a carroca de feno
# passando atras do casal no take 1 — e passando DE NOVO no take 2, que
# acontece 47 dias depois, e outra vez nos takes 3 e 4, sendo o take 4 a
# continuacao direta do 3, com a MESMA imagem de base:
#   *"a carroca fica dando looping. Isso esta' errado, isso e' confuso. A
#   carroca ja' deveria ter passado."*
# ⛔ A causa nao e' o cenario: e' o campo `vida`, que entra nos QUATRO takes
# e e' literalmente a ordem de mover a coisa. Um `vida` de travessia vira
# quatro travessias, uma por take, e o espectador le' loop.
# ⭐ A regra que ele ditou: *"deve ser objetos estaticos que nao mudam. No
# maximo, pequenos animais ali no chao, como galinhas pastando [...] ou entao
# pessoas se mexendo, mas num cenario muito ao fundo mesmo, la' onde estao
# essas arvores, que mal da' para ver, como agricultores trabalhando"*.
# ⛔ Logo: `vida` so' pode ser movimento NO LUGAR (balancar, fumegar,
# ciscar, girar no eixo) ou figura minuscula na linha das arvores. Verbo de
# travessia — `past`, `along the lane`, `rolls`, `plods`, `hauling`,
# `pulled by` — esta' banido, e quem cobra e' a lente `AM11`.
# ⚠️ Quatro entradas foram reescritas por isso: `carroca_feno` (virou os
# fardos), `construcao_celeiro` (a obra parada), `colheita_milho` (saiu a
# carroca de mula) e `pomar_florido` (saiu o cavaleiro).
CENARIOS = [
    {"id": "celeiro_bandeira", "mundo": "amish", "rotulo": "celeiro vermelho + bandeira",
     "desc": ("in front of a weathered red barn with a large American flag "
              "hung on its wall, a black Amish buggy parked with its shafts "
              "resting on the ground and two draft horses standing still at "
              "a hitching rail"),
     "vida": "the horses shift their weight and swish their tails",
     "curto": "the red barn with the American flag"},
    {"id": "fardos_feno", "mundo": "amish", "rotulo": "fardos de feno empilhados",
     "desc": ("beside a tall stack of square hay bales in a freshly mown "
              "field, a red barn and an American flag on a pole in the "
              "distance"),
     "vida": "",
     "curto": "the stack of hay bales"},
    {"id": "celeiro_novo", "mundo": "amish", "rotulo": "celeiro novo, obra parada",
     "desc": ("in a quiet farmyard beside the bare wooden frame of a "
              "half-built barn, stacks of fresh lumber and two sawhorses "
              "resting on the ground, an American flag on a post"),
     "vida": "",
     "curto": "the half-built barn frame"},
    {"id": "varal_caldeiroes", "mundo": "amish", "rotulo": "varal + caldeiroes fumegando",
     "desc": ("in a dry packed-dirt work yard with laundry lines and big "
              "black cauldrons sitting over open fires, a gray barn and an "
              "American flag behind"),
     "vida": "",
     "curto": "the steaming cauldrons"},
    {"id": "curral", "mundo": "amish", "rotulo": "curral de vacas e ovelhas",
     "desc": ("by a wooden fence with dairy cows and sheep crowding the "
              "barnyard behind, chickens pecking near the fence posts, a "
              "small American flag on the barn"),
     "vida": "the chickens peck at the ground near the fence posts",
     "curto": "the crowded barnyard"},
    {"id": "milharal", "mundo": "amish", "rotulo": "milharal na colheita",
     "desc": ("at the edge of a tall cornfield at harvest time, wooden "
              "crates of picked corn stacked on the ground beside them, an "
              "American flag on a pole"),
     "vida": "",
     "curto": "the edge of the cornfield"},
    {"id": "pomar_florido", "mundo": "amish", "rotulo": "pomar florido",
     "desc": ("in a blooming spring orchard with pink flowering trees, a "
              "white farmhouse and a red barn far in the distance"),
     # ⛔ as petalas caindo SAIRAM em 22/08: *"remova as petalas caindo
     # pois esta atrapalhando a cena"*. Ficou o movimento no galho,
     # que da vida ao fundo sem cruzar o quadro do casal.
     "vida": "",
     "curto": "the blooming orchard"},
    {"id": "celeiro_cinza", "mundo": "amish", "rotulo": "celeiro cinza + foice",
     "desc": ("against a weathered gray barn wall with an American flag "
              "nailed to it and a long-handled scythe leaning beside, open "
              "green pasture behind"),
     "vida": "",
     "curto": "the gray barn wall with the flag"},
    {"id": "pasto_moinho", "mundo": "amish", "rotulo": "pasto + moinho de vento",
     "desc": ("in an open summer pasture with grazing cows and a tall metal "
              "windmill standing still in the distance, a dirt lane and a "
              "fence line running through the field"),
     "vida": "",
     "curto": "the pasture with the windmill"},
    {"id": "despensa_ervas", "mundo": "amish", "rotulo": "despensa de ervas",
     "desc": ("inside a rustic herb pantry, wooden shelves packed with "
              "glass jars of dried herbs and roots behind, warm window "
              "light from the side"),
     "vida": "",
     "curto": "the herb pantry shelves"},
    {"id": "lago_gansos", "mundo": "amish", "rotulo": "lago com gansos",
     "desc": ("by a farm pond with white geese on the bank, a covered "
              "wooden bridge and a red barn beyond, an American flag on the "
              "bridge post"),
     "vida": "the geese preen and dip their beaks at the water's edge",
     "curto": "the farm pond"},
    {"id": "horta_abobora", "mundo": "amish", "rotulo": "horta + carroca de abobora",
     "desc": ("beside a fenced vegetable garden with a wooden cart of "
              "pumpkins parked at the fence, a farmhouse porch with an "
              "American flag, and the tiny far-off figure of an Amish woman "
              "hoeing a row up at the tree line"),
     # ⭐ a unica pessoa que ainda se mexe no fundo do parque, e minuscula:
     # e' a excecao que ele autorizou — *"pessoas se mexendo, mas [...] la'
     # onde estao essas arvores, que mal da' para ver"*.
     "vida": "the tiny distant figure keeps hoeing at the tree line",
     "curto": "the pumpkin cart by the garden"},
    # ⭐⭐ OS TRES MUNDOS NOVOS (2026-08-21) — um por identidade. Cada um
    # existe para que a VOCACAO se leia sem legenda: a hollow diz granny
    # woman, o claustro diz freira, a marisma diz Gullah.
    # ⛔ Todos obedecem a regra de 21/08: nada atravessa o quadro. O `vida`
    # e' movimento NO LUGAR — tecido, vapor, poeira, folha, agua.
    {"id": "apalache_varanda", "mundo": "apalache",
     "rotulo": "varanda da cabana",
     "desc": ("on the sagging wooden porch of a weathered mountain cabin, a "
              "rocking chair and a patchwork quilt over the rail, blue "
              "ridges fading into the distance behind"),
     "vida": "",
     "curto": "the cabin porch"},
    {"id": "apalache_despensa", "mundo": "apalache",
     "rotulo": "despensa de raizes",
     "desc": ("inside a dim cabin pantry lined with shelves of glass jars "
              "holding dried roots and herbs, bunches of plants hung to dry "
              "from the beams, warm light from one small window"),
     "vida": "",
     "curto": "the root pantry"},
    {"id": "apalache_horta", "mundo": "apalache",
     "rotulo": "horta na encosta",
     "desc": ("beside a small hillside garden fenced with split rails, tin "
              "buckets and a hoe leaning against the fence, forested ridges "
              "climbing behind"),
     "vida": "",
     "curto": "the hillside garden"},
    {"id": "convento_jardim", "mundo": "convento",
     "rotulo": "jardim de ervas murado",
     "desc": ("in a walled monastery herb garden with low clipped hedges "
              "and labelled beds of herbs, a stone well at the centre, the "
              "arches of a cloister behind"),
     "vida": "",
     "curto": "the walled herb garden"},
    {"id": "convento_cozinha", "mundo": "convento",
     "rotulo": "cozinha do convento",
     "desc": ("in an old stone convent kitchen with a long scrubbed wooden "
              "table, copper pots hung on the wall and shelves of amber "
              "glass jars, light falling from one tall narrow window"),
     "vida": "",
     "curto": "the convent kitchen"},
    {"id": "convento_claustro", "mundo": "convento",
     "rotulo": "claustro de pedra",
     "desc": ("under the stone arches of a quiet cloister, a courtyard of "
              "clipped grass and a small fountain framed between the "
              "columns"),
     "vida": "",
     "curto": "the stone cloister"},
    {"id": "gullah_alpendre", "mundo": "gullah",
     "rotulo": "alpendre da ilha",
     "desc": ("on the porch of a small tin-roofed island house raised on "
              "brick piers, woven sweetgrass baskets stacked by the door, "
              "live oaks draped with hanging moss beyond"),
     "vida": "",
     "curto": "the island porch"},
    {"id": "gullah_marisma", "mundo": "gullah",
     "rotulo": "marisma de mare",
     "desc": ("at the edge of a tidal salt marsh with a weathered wooden "
              "dock, a flat-bottomed boat tied up at the post, tall marsh "
              "grass running to the water"),
     "vida": "",
     "curto": "the salt marsh"},
    {"id": "gullah_cozinha", "mundo": "gullah",
     "rotulo": "cozinha da ilha",
     "desc": ("in a small island kitchen with a cast-iron pot on the stove, "
              "bunches of dried roots hanging from a nail and rows of jars "
              "on a painted shelf, the screen door open to the yard"),
     "vida": "",
     "curto": "the island kitchen"},
]


# ===========================================================================
# ⭐⭐ AS TRIBOS — o eixo que quebra o "todos parecidos" (2026-08-23)
# ===========================================================================
# Queixa dele, com o lote na mao: *"esse agente esta gerando sempre as mesmas
# pessoas [...] os sorteios estao gerando sempre pessoas extremamente
# parecidas"*, e depois *"mude as roupas tambem, esta gerando sempre roupas
# iguais, por isso eu falei dos emos, goticos, roqueiros, countrys, cowboys,
# fazendeiros, pois eles tem estilo de roupas diferentes um dos outros"*.
#
# ⛔ A CAUSA NAO ERA FALTA DE ENTRADA — o pool ja tinha 46 sujeitos. Medido no
# bloco gerado: a IDENTIDADE era 45 palavras, 9% do prompt, contra 203
# palavras de uma formula de corpo IDENTICA nos 46. O corpo dominava por
# 4,5:1 e o gerador desenhava o mesmo obeso com outro cabelo. E as roupas
# eram todas a mesma silhueta: 23 das 46 continham `short-sleeve`, 19
# continham `shirt`, e nao havia UMA jaqueta, colete, macacao ou moletom.
#
# ⭐ Por isso escrever mais entradas de 45 palavras nao resolveria: soma nao
# vence proporcao. A TRIBO e um eixo INDEPENDENTE que multiplica — 46 rostos
# x 15 tribos = 690 combinacoes — e traz MASSA: roupa + marcas sobem a
# identidade de 45 para ~85 palavras.
#
# ⛔ A tribo NAO fala de cabelo nem de barba: quem fala e o campo `visual` do
# sujeito, e duas fontes descrevendo cabelo se contradizem dentro do mesmo
# prompt — a familia de defeito que este motor ja pagou quatro vezes.
# ⛔ E nenhuma tribo usa token de coloracao europeia (`red`, `blond`, `pale`,
# `freckled`, olhos azuis/verdes): a MESMA tribo tem de servir a pessoa negra
# e a branca sem trocar uma palavra, senao ela vira um segundo eixo de etnia
# brigando com a trava de pele. Quem cobra as tres coisas e a `AM16`.
#
# ⚠️ Escritas por cinco autores em paralelo e auditadas por um revisor cada,
# que consertou de verdade: a jaqueta fechada que nao pode ser esticada sobre
# a barriga virou camiseta sob colete aberto; um raio sobre bigorna com letra
# gotica virou martelo, por risco de leitura de simbolo de odio; e a pulseira
# que estava debaixo de manga fechada ganhou `below a shoved-up sleeve`.
# ⚰️ APOSENTADAS EM 2026-08-23, no mesmo dia em que nasceram. Ele viu o
# lote e reprovou: *"ficou muito esquisito punks, roqueiros de 50 anos ou
# mais"*. A licao que fica e' a que custou o dia: SUBCULTURA COLIDE COM
# IDADE. Um punk de 57 nao le como pessoa comum obesa — le como
# personagem, e o espectador do nicho nao se reconhece nele.
# ⚠️ E elas nao tinham campo de SEXO, zero de quinze: mecanico e veterano
# de guerra caiam em mulher de 60. O eixo novo tem.
# ⛔ Ficam aqui como memoria; NADA le esta lista.
TRIBOS_APOSENTADAS = [
    {"id": 'punk_cravejado', "rotulo": 'punk de colete cravejado',
     "roupa": ("a washed-out charcoal t-shirt with a cracked screen-print of a"
              " snarling bulldog, worn under an open sleeveless denim vest"
              " crusted with metal studs and safety pins"),
     "marcas": ("three small steel rings through one eyebrow, a safety pin worn"
              " as an earring in the upper curve of one ear, a black bandana"
              " knotted at the side of the neck with the ends hanging loose,"
              " and chipped black polish on the thick fingers")},
    {"id": 'gotico_veludo', "rotulo": 'gotico de veludo e prata',
     "roupa": ("a high-collared black velvet shirt with wide bishop sleeves"
              " and a long column of tiny jet buttons down the front, worn"
              " under an open black brocade waistcoat patterned with silver"
              " thorns"),
     "marcas": ("smudged black liner ringed all the way around both eyes, a"
              " narrow black velvet choker with a single silver teardrop at"
              " the hollow of the throat, heavy silver rings set with dark"
              " polished stones on three thick fingers, and a small ankh inked"
              " behind one ear")},
    {"id": 'emo_listrado', "rotulo": 'emo de moletom e listras',
     "roupa": ("a black zip-up hoodie closed all the way to the chin over a"
              " horizontally striped black-and-white long-sleeve shirt, with a"
              " small enamel pin of a cracked cassette tape on the chest"),
     "marcas": ("thick rectangular black plastic-framed glasses slid halfway"
              " down the nose, a dense stack of woven black and deep purple"
              " friendship bracelets crowding one thick wrist below a shoved-"
              " up sleeve, three small black plugs through the lobe of each"
              " ear, and a heart drawn in ballpoint ink on the back of one"
              " hand, half rubbed away")},
    {"id": 'metaleiro_bigorna', "rotulo": 'metaleiro de camisa de turnê e tarraxas',
     "roupa": ("a washed-out charcoal long-sleeve tour shirt with a cracked"
              " white screen-print of a hammer striking an anvil across the"
              " chest and columns of gothic tour lettering running down both"
              " sleeves"),
     "marcas": ("a wide black leather cuff covered in blunt pyramid studs on"
              " one wrist, a heavy pewter ring shaped like a coiled serpent on"
              " the index finger, matte black plugs filling both earlobes, and"
              " chipped black polish on the thick thumbnails")},
    {"id": 'roqueiro_veludo70', "rotulo": 'roqueiro setentista de veludo e colar de contas',
     "roupa": ("a deep plum crushed-velvet button-down shirt with an enormous"
              " pointed collar, pearl snap buttons, and thin gold piping"
              " stitched along both shoulder yokes"),
     "marcas": ("round wire-rim glasses with amber tinted lenses sitting low on"
              " the nose, three thin gold hoops stacked in one ear, a chunky"
              " turquoise-and-silver ring on the middle finger of each hand,"
              " and a long strand of dark wooden love beads resting across the"
              " collarbones")},
    {"id": 'motoqueiro_roda_alada', "rotulo": 'motoqueiro de colete de couro e bandana',
     "roupa": ("a heavy black cotton t-shirt with a faded screen-print of a"
              " two-lane highway vanishing into mountains across the chest,"
              " worn under a scuffed black leather riding vest that hangs wide"
              " open at the sides, dulled brass zipper pulls and loose buckle"
              " straps swinging from the vest's front edges"),
     "marcas": ("a dark paisley bandana knotted low across the forehead, a"
              " small steel hoop through the septum, a weathered tattoo of a"
              " winged wheel on the side of the neck, and fingerless leather"
              " gloves on the thick hands with a heavy steel signet ring worn"
              " over the leather")},
    {"id": 'cowboy_rodeio', "rotulo": 'cowboy de rodeio com numero preso no peito',
     "roupa": ("a faded indigo pearl-snap western shirt with white piping"
              " arrows across the chest yoke and a creased paper contestant"
              " number safety-pinned to the front"),
     "marcas": ("a sweat-darkened straw cowboy hat with a sharply curled brim,"
              " a braided leather bolo tie with a turquoise-and-silver slide"
              " sitting at the throat, white athletic tape wound around two"
              " thick fingers, and a heavy oval silver ring on one little"
              " finger")},
    {"id": 'fazendeiro_trator', "rotulo": 'fazendeiro de trator com bone de tela e oculos empoeirados',
     "roupa": ("a buttoned olive-drab canvas chore coat with a wide corduroy"
              " collar and one grease-darkened chest patch pocket, worn closed"
              " over a washed-out grey t-shirt"),
     "marcas": ("a mesh-back trucker cap with a cracked embroidered patch of a"
              " wheat sheaf above the brim, thick plastic-framed glasses"
              " filmed over with field dust, a shiny old scar line running"
              " across the back of one hand, and dark grease packed under"
              " short square fingernails")},
    {"id": 'criador_gado', "rotulo": 'criador de gado de flanela e bandana no pescoco',
     "roupa": ("a heavy dark-olive wool flannel work shirt with a double-thick"
              " shoulder yoke and worn horn buttons, the sleeves shoved up"
              " over the forearms"),
     "marcas": ("a squashed dark canvas flat cap with a short stiff brim, a"
              " knotted navy paisley bandana riding high at the throat, a"
              " small dark ink tattoo of a horseshoe on the back of one hand,"
              " and a plain brass livestock ear-tag hanging from a leather"
              " cord at the neck")},
    {"id": 'caminhoneiro_estrada', "rotulo": 'caminhoneiro de bone de tela',
     "roupa": ("an oatmeal-colored heavy flannel work shirt worn over a"
              " washed-out charcoal t-shirt with a cracked screen-print of a"
              " long-nose semi truck across the chest"),
     "marcas": ("wraparound amber-tinted driving glasses pushed up onto the"
              " brim of a foam-front mesh-back cap, a thin steel chain with a"
              " small flat pewter medallion resting at the base of the throat,"
              " and a wide worn wedding band sunk deep into the thick finger"
              " of one hand")},
    {"id": 'mecanico_oficina', "rotulo": 'mecanico de macacao engraxado',
     "roupa": ("a navy short-sleeve mechanic's coverall unzipped to mid-chest,"
              " a blank oval name patch stitched above the breast pocket and"
              " dark grease smears streaking the front"),
     "marcas": ("clear plastic safety glasses pushed up onto the forehead, a"
              " hand-poked blue-black gear tattoo on the side of the neck, a"
              " shiny raised scar across one knuckle, and black grease packed"
              " under every fingernail")},
    {"id": 'pescador_barco', "rotulo": 'pescador de capa de oleado',
     "roupa": ("a heavy mustard-yellow oilskin slicker jacket worn over a"
              " salt-stained charcoal waffle-knit thermal shirt"),
     "marcas": ("a snug ribbed knit watch cap pulled down over the ears, a"
              " small gold hoop through one earlobe, a faded blue-black anchor"
              " tattoo across the back of one hand, and cracked salt-dried"
              " skin over swollen knuckles")},
    {"id": 'hiphop_anos90', "rotulo": 'hip-hop dos anos 90, jersey e corrente de ouro',
     "roupa": ("a cream basketball jersey with bold navy block numbers"
              " stitched across the chest, layered over a thick black long-"
              " sleeve thermal shirt"),
     "marcas": ("a thick gold rope chain lying deep in the folds of the neck, a"
              " black canvas bucket hat pulled low over the brow, a small gold"
              " hoop in one earlobe, and three chunky gold rings crowded onto"
              " the thick fingers")},
    {"id": 'boliche_liga', "rotulo": 'jogador de boliche de liga, camisa de time',
     "roupa": ("a short-sleeve league bowling shirt in charcoal and cream"
              " panels with piped edges, a curved team name chain-stitched"
              " across the chest and a small oval name patch embroidered over"
              " the breast pocket"),
     "marcas": ("thick square-framed glasses slid halfway down the nose, a"
              " black elastic wrist support strapped tight from the knuckles"
              " to the middle of one forearm, a heavy embossed tournament ring"
              " cutting into the ring finger, and a tiny enamel bowling-pin"
              " pin fastened to the collar")},
    {"id": 'veterano_reformado', "rotulo": 'veterano de guerra aposentado, bone com pins',
     "roupa": ("a washed-out olive-drab sweatshirt with a cracked screen-"
              " printed eagle crest and faded stencil lettering across the"
              " chest, the ribbed hem long since given up"),
     "marcas": ("a dark green veteran's ball cap with gold embroidered"
              " lettering and four small enamel service pins clipped along the"
              " brim, a ball chain with two dented metal tags resting in the"
              " neck folds, heavy tinted aviator-style glasses, and a blurred"
              " dark-green anchor tattoo sunk into the back of one swollen"
              " hand")},
]

# ===========================================================================
# ⭐⭐ OS EIXOS DA PESSOA — o sujeito deixa de ser LISTA e vira COMPOSICAO
# ===========================================================================
# 2026-08-23. Ordem dele, depois de reprovar as tribos de subcultura:
# *"ficou muito esquisito punks, roqueiros de 50 anos ou mais. Ajuste
# novamente para pessoas comuns, com roupas comuns, porem quero uma variedade
# enorme nos sorteios para quase nunca repetir as roupas, cores e detalhes"*
# — e o mesmo para os rostos: *"capriche nesses detalhes como cor do olhos,
# cabelo, bigode, barba, se e homem careca ou nao, cabelo liso, cacheado,
# trancas"*.
#
# ⛔⛔ LISTA NUNCA DA "QUASE NUNCA REPETIR". Quinze tribos sao quinze; 46
# rostos sao 46. Foi por isso que ele continuou vendo gente parecida mesmo
# depois de o pool triplicar. A unica arquitetura que entrega variedade
# praticamente inesgotavel e a COMPOSICAO — a conta vira PRODUTO em vez de
# soma. Ver `combinacoes_possiveis()`, que MEDE o numero em vez de prometer.
#
# ⛔ TODA ENTRADA DECLARA `pele` E `sexo`, e as duas travas existem por
# defeito medido:
#   · `pele`: olho azul e cabelo ruivo nao servem pessoa negra; tranca, dread
#     e crespo nao servem pessoa branca. Sem isso o prompt se contradiz e o
#     gerador segue a DESCRICAO, nao a trava — 5 tokens contra 1, medido em
#     21/08.
#   · `sexo`: reclamacao dele em 23/08 — *"muita coisa que era pra ser so
#     homem esta caindo como mulher quando eu mudo a trava de sexo: mecanico,
#     cowboy, militar aposentado. Nao faz sentido para mulheres americanas de
#     60 anos essas profissoes"*. As tribos NAO tinham campo de sexo: zero de
#     quinze. Aqui todo eixo tem.
#
# ⭐ E NAO HA PROFISSAO NENHUMA nestes pools — so' roupa. `mechanic-style work
# shirt` e uma peca; `mecanico de macacao engraxado` era um personagem. A
# diferenca e' exatamente a queixa dele.


# A peca de CIMA — ela e' esticada sobre a barriga, entao
# nao ha calca, saia nem sapato aqui.
PECAS = [
    {"id": 'polo_mc', "en": 'short-sleeve polo shirt with a three-button placket', "tipo": 'polo', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'polo_ml', "en": 'long-sleeve polo shirt with a ribbed knit collar', "tipo": 'polo', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'polo_bolso', "en": 'short-sleeve polo shirt with a small chest pocket', "tipo": 'polo', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'polo_zip', "en": 'short-sleeve knit polo with a quarter-zip collar', "tipo": 'polo', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'camisa_oxford', "en": 'long-sleeve oxford shirt with a button-down collar', "tipo": 'camisa', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'camisa_social', "en": 'long-sleeve dress shirt with a spread collar and stiff cuffs', "tipo": 'camisa', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'camisa_mc_bolso', "en": 'short-sleeve button-up shirt with a single chest pocket', "tipo": 'camisa', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'camisa_aberta', "en": 'button-up shirt worn open over a plain crew-neck t-shirt', "tipo": 'sobreposicao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'flanela', "en": 'heavy brushed flannel shirt with a wide collar', "tipo": 'camisa', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'flanela_aberta', "en": 'flannel shirt hanging open over a pocket t-shirt', "tipo": 'sobreposicao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'camisa_western', "en": 'snap-front western shirt with pointed shoulder yokes', "tipo": 'camisa', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'camisa_jeans', "en": 'denim shirt with two flapped chest pockets', "tipo": 'camisa', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'camisa_gola_padre', "en": 'band-collar shirt with the top button left undone', "tipo": 'camisa', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'camisa_camp', "en": 'camp-collar short-sleeve shirt with a straight hem worn untucked', "tipo": 'camisa', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'guayabera', "en": 'short-sleeve guayabera shirt with vertical pleats and four pockets', "tipo": 'camisa', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'camisa_pesca', "en": 'vented short-sleeve fishing shirt with two zip pockets', "tipo": 'camisa', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'camisa_boliche', "en": 'bowling-style shirt with a loop collar and boxy short sleeves', "tipo": 'camisa', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'camisa_cotele', "en": 'wide-wale corduroy shirt with two flap pockets', "tipo": 'camisa', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'camisa_chamois', "en": 'soft napped chamois cloth shirt with a heavy collar', "tipo": 'camisa', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'camisa_linho', "en": 'rumpled linen button-up shirt with an open collar', "tipo": 'camisa', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'camisa_popover', "en": 'popover shirt with a half placket and a soft collar', "tipo": 'camisa', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'camisa_seersucker', "en": 'puckered seersucker short-sleeve shirt with one chest pocket', "tipo": 'camisa', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'camisa_trabalho', "en": 'sturdy two-pocket work shirt buttoned all the way to the collar', "tipo": 'trabalho', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'camisa_mecanico', "en": 'short-sleeve mechanic-style work shirt with a stiff turndown collar', "tipo": 'trabalho', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'camiseta_crew', "en": 'plain crew-neck t-shirt', "tipo": 'malha', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'camiseta_v', "en": 'v-neck t-shirt with a soft stretched-out collar', "tipo": 'malha', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'camiseta_bolso', "en": 'short-sleeve pocket t-shirt with a curved hem', "tipo": 'malha', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'camiseta_ml', "en": 'long-sleeve t-shirt with the cuffs shoved up the forearms', "tipo": 'malha', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'camiseta_raglan', "en": 'raglan t-shirt with three-quarter sleeves', "tipo": 'malha', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'termica', "en": 'waffle-knit thermal shirt worn on its own', "tipo": 'malha', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'regata_costela', "en": 'ribbed sleeveless undershirt with wide shoulder straps', "tipo": 'malha', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'henley_curto', "en": 'short-sleeve henley with the placket buttons left undone', "tipo": 'malha', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'henley_longo', "en": 'long-sleeve henley with a three-button placket', "tipo": 'malha', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'rugby', "en": 'rugby-style knit shirt with a heavy fabric collar', "tipo": 'malha', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'cotoveleira', "en": 'long-sleeve knit shirt with suede elbow patches', "tipo": 'malha', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'moletom_careca', "en": 'crew-neck sweatshirt with ribbed cuffs and hem', "tipo": 'moletom', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'moletom_capuz', "en": 'pullover hooded sweatshirt with a kangaroo pocket', "tipo": 'moletom', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'moletom_capuz_ziper', "en": 'zip-front hooded sweatshirt with the hood pushed back', "tipo": 'moletom', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'moletom_ziper', "en": 'full-zip fleece sweatshirt left hanging open over a t-shirt', "tipo": 'sobreposicao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'fleece_quarto_zip', "en": 'soft fleece pullover with a quarter zip at the throat', "tipo": 'moletom', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'jaqueta_track', "en": 'zip-front track jacket with a stand collar', "tipo": 'sobreposicao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'anoraque', "en": 'half-zip anorak pullover with one chest pocket', "tipo": 'sobreposicao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'jaqueta_jeans', "en": 'button-front denim jacket worn over a t-shirt', "tipo": 'sobreposicao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'jaqueta_chore', "en": 'heavy canvas chore jacket with three square front pockets', "tipo": 'sobreposicao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'corta_vento', "en": 'lightweight zip-front windbreaker with an elastic hem', "tipo": 'sobreposicao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'colete_acolchoado', "en": 'quilted vest worn open over a long-sleeve shirt', "tipo": 'sobreposicao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'colete_fleece', "en": 'zip-front fleece vest over a long-sleeve shirt', "tipo": 'sobreposicao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'colete_utilitario', "en": 'utility vest with rows of small pockets over a long-sleeve shirt', "tipo": 'sobreposicao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'colete_trico', "en": 'sleeveless knit sweater vest over a collared shirt', "tipo": 'sobreposicao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'gola_alta_sob_camisa', "en": 'thin turtleneck worn under an open button-up shirt', "tipo": 'sobreposicao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'shacket', "en": 'flannel-lined shirt jacket worn buttoned over a t-shirt', "tipo": 'sobreposicao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'sueter_careca', "en": 'crew-neck wool sweater with a thick ribbed hem', "tipo": 'trico', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'sueter_v', "en": 'v-neck knit sweater worn over a collared shirt', "tipo": 'trico', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'sueter_cable', "en": 'chunky cable-knit sweater with a rolled collar', "tipo": 'trico', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'gola_alta', "en": 'turtleneck sweater bunched into folds at the throat', "tipo": 'trico', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'mock_neck', "en": 'mock-neck knit pullover with raglan sleeves', "tipo": 'trico', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'meio_zip_trico', "en": 'half-zip knit pullover with the zipper open at the chest', "tipo": 'trico', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'cardigan_aberto', "en": 'button-front knit cardigan worn open', "tipo": 'trico', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'cardigan_fechado', "en": 'buttoned knit cardigan with two low patch pockets', "tipo": 'trico', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'cardigan_xale', "en": 'shawl-collar cardigan with a thick folded knit collar', "tipo": 'trico', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'cardigan_ziper', "en": 'zip-front knit cardigan with a stand collar', "tipo": 'trico', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'cardigan_ombros', "en": 'knit cardigan draped over the shoulders with the sleeves hanging empty', "tipo": 'trico', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'cardigan_longo', "en": 'long open-front knit duster cardigan', "tipo": 'trico', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'blusa_drapeada', "en": 'soft draped blouse with a rounded neckline', "tipo": 'feminina', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'blusa_botao', "en": 'button-front blouse with a small collar and gathered shoulders', "tipo": 'feminina', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'blusa_babado', "en": 'button-front blouse with a ruffled front placket', "tipo": 'feminina', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'blusa_sem_manga', "en": 'sleeveless button-front blouse with a pointed collar', "tipo": 'feminina', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'blusa_camponesa', "en": 'peasant-style blouse with an elastic gathered neckline', "tipo": 'feminina', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'tunica', "en": 'long tunic top with a v-neckline and short side slits', "tipo": 'feminina', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'twinset', "en": 'sleeveless knit shell top under a matching open cardigan', "tipo": 'feminina', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'cowl', "en": 'cowl-neck knit top with three-quarter sleeves', "tipo": 'feminina', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'boat_neck', "en": 'boat-neck knit top with elbow-length sleeves', "tipo": 'feminina', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'blusa_keyhole', "en": 'short-sleeve knit top with a small keyhole neckline', "tipo": 'feminina', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'top_envelope', "en": 'wrap-front knit top gathered at one side', "tipo": 'feminina', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'blusa_zip', "en": 'zip-front velour top with a stand collar', "tipo": 'feminina', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'xale_trico', "en": 'knit shawl draped over the shoulders and pinned at the chest', "tipo": 'feminina', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'housecoat', "en": 'snap-front housecoat with two deep front pockets', "tipo": 'caseira', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'vestido_casa', "en": 'short-sleeve knit house dress with a round neckline', "tipo": 'caseira', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'muumuu', "en": 'muumuu-style house dress falling straight from the shoulders', "tipo": 'caseira', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'robe_acolchoado', "en": 'quilted robe closed over a pajama top and tied at the waist', "tipo": 'caseira', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'pijama_top', "en": 'buttoned pajama top with contrast piping along the collar', "tipo": 'caseira', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'camisola', "en": 'long nightgown with a lace-trimmed yoke', "tipo": 'caseira', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'jaleco_jardim', "en": 'canvas gardening smock with one wide front pocket', "tipo": 'trabalho', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'avental', "en": 'bib apron worn over a long-sleeve shirt', "tipo": 'trabalho', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'scrub', "en": 'v-neck scrub-style top with a single patch pocket', "tipo": 'trabalho', "pele": 'ambas', "sexo": 'ambos'},
]

# `tipo`: `cor` ou `padrao`. O `plain` nao entra
# na frase montada — ver o compositor.
CORES_E_PADROES = [
    {"id": 'navy_blue', "en": 'navy blue', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'midnight_blue', "en": 'deep midnight blue', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'slate_blue', "en": 'slate blue', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'faded_denim_blue', "en": 'faded denim blue', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'powder_blue', "en": 'soft powder blue', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'steel_blue', "en": 'steel blue', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'petrol_blue', "en": 'dark petrol blue', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'cadet_blue', "en": 'dull cadet blue', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'indigo_washed', "en": 'washed indigo', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'cornflower_soft', "en": 'soft cornflower blue', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'periwinkle_dusty', "en": 'dusty periwinkle blue', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'smoke_blue_gray', "en": 'smoky blue-gray', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'teal', "en": 'muted teal', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'turquoise_muted', "en": 'muted turquoise', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'seafoam', "en": 'pale seafoam green', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'mint_pale', "en": 'pale mint green', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'sage_green', "en": 'sage green', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'celery_green', "en": 'pale celery green', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'olive_green', "en": 'olive green', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'olive_drab', "en": 'washed olive drab', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'moss_green', "en": 'moss green', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'avocado_green', "en": 'dull avocado green', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'forest_green', "en": 'dark forest green', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'hunter_green', "en": 'hunter green', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'pine_green', "en": 'deep pine green', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'bottle_green', "en": 'deep bottle green', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'mustard_yellow', "en": 'mustard yellow', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'golden_wheat', "en": 'golden wheat yellow', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'butter_yellow', "en": 'pale butter yellow', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'straw_pale', "en": 'pale straw yellow', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'buttercream', "en": 'soft buttercream', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'honey_gold', "en": 'muted honey gold', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'ochre', "en": 'dusty ochre', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'brass_dull', "en": 'dull brass gold', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'copper_muted', "en": 'muted copper', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'rust_orange', "en": 'rust orange', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'burnt_sienna', "en": 'burnt sienna', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'terracotta', "en": 'terracotta', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'pumpkin_muted', "en": 'muted pumpkin orange', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'apricot_soft', "en": 'soft apricot', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'peach_pale', "en": 'pale peach', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'coral_muted', "en": 'muted coral', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'brick_red', "en": 'brick red', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'barn_red', "en": 'weathered barn red', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'cranberry', "en": 'cranberry red', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'burgundy', "en": 'burgundy', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'maroon', "en": 'deep maroon', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'wine_red', "en": 'dark wine red', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'dusty_rose', "en": 'dusty rose', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'salmon_muted', "en": 'muted salmon pink', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'blush_pink', "en": 'soft blush pink', "tipo": 'cor', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'mauve', "en": 'mauve', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'plum', "en": 'plum', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'eggplant', "en": 'deep eggplant purple', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'lilac_soft', "en": 'soft lilac', "tipo": 'cor', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'lavender_gray', "en": 'grayish lavender', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'charcoal_gray', "en": 'charcoal gray', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'graphite_gray', "en": 'dark graphite gray', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'slate_gray', "en": 'dark slate gray', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'heather_gray', "en": 'heather gray', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'pewter', "en": 'pewter gray', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'ash_gray', "en": 'ash gray', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'stone_gray', "en": 'stone gray', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'dove_gray', "en": 'pale dove gray', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'silver_gray', "en": 'soft silver gray', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'mushroom_gray', "en": 'pale mushroom gray', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'greige', "en": 'greige', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'black_worn', "en": 'worn black', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'cream', "en": 'cream', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'ivory', "en": 'ivory', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'bone_white', "en": 'bone white', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'ecru', "en": 'ecru', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'oatmeal', "en": 'oatmeal beige', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'warm_beige', "en": 'warm beige', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'sand', "en": 'pale sand', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'tan', "en": 'tan', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'khaki', "en": 'khaki', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'camel', "en": 'camel', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'taupe', "en": 'taupe', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'caramel', "en": 'caramel brown', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'clay_brown', "en": 'dusty clay brown', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'russet', "en": 'warm russet brown', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'cedar_brown', "en": 'warm cedar brown', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'chestnut_brown', "en": 'chestnut brown', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'walnut_brown', "en": 'dark walnut brown', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'cocoa_muted', "en": 'muted cocoa brown', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'chocolate_brown', "en": 'chocolate brown', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'coffee_brown', "en": 'dark coffee brown', "tipo": 'cor', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'plain', "en": 'plain solid', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'tonal_stripe', "en": 'tone-on-tone striped', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'small_checked', "en": 'small checked', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'microcheck', "en": 'tiny microchecked', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'gingham', "en": 'gingham-checked', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'windowpane_check', "en": 'windowpane-checked', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'buffalo_check', "en": 'large buffalo-checked', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'madras_check', "en": 'washed madras-checked', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'wide_plaid', "en": 'wide plaid', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'muted_tartan', "en": 'muted tartan plaid', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'shadow_plaid', "en": 'faint shadow plaid', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'thin_vertical_stripes', "en": 'narrow vertically striped', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'wide_vertical_stripes', "en": 'wide vertically striped', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'pinstriped', "en": 'pinstriped', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'chalk_striped', "en": 'chalk-striped', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'bengal_striped', "en": 'bold bengal-striped', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'ticking_stripes', "en": 'narrow ticking-striped', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'horizontal_bands', "en": 'wide horizontally striped', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'heathered', "en": 'heathered', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'marled_knit', "en": 'marled two-tone', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'speckled_fleck', "en": 'finely flecked', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'tweed_flecked', "en": 'flecked tweed', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'herringbone', "en": 'herringbone', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'houndstooth', "en": 'small houndstooth', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'argyle', "en": 'muted argyle', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'twill_woven', "en": 'diagonal twill-woven', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'birdseye', "en": 'fine birdseye-woven', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'crosshatch', "en": 'fine crosshatch-woven', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'basketweave', "en": 'open basketweave', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'slub_woven', "en": 'coarse slub-woven', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'seersucker', "en": 'puckered seersucker', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'chambray', "en": 'chambray', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'denim_textured', "en": 'denim-textured', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'corduroy_ribbed', "en": 'wide-wale corduroy', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'cable_knit', "en": 'chunky cable-knit', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'waffle_knit', "en": 'waffle-knit', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'ribbed_knit', "en": 'fine ribbed-knit', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'double_knit', "en": 'smooth double-knit', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'pique_knit', "en": 'pique-textured', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'terry_looped', "en": 'soft terry-looped', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'velour_napped', "en": 'soft velour-napped', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'flannel_napped', "en": 'brushed flannel-napped', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'fleece_brushed', "en": 'brushed fleece', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'quilted_diamond', "en": 'diamond-quilted', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'jacquard_tonal', "en": 'tonal jacquard-textured', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'two_tone_yoke', "en": 'color-blocked two-tone', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'contrast_collar', "en": 'contrast-collared', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'faded', "en": 'faded and sun-bleached', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'stonewashed', "en": 'stonewashed and softened', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'pilled_worn', "en": 'pilled and worn thin', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'geometric_repeat', "en": 'small repeating geometric print', "tipo": 'padrao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'small_polka_dots', "en": 'scattered small polka-dot', "tipo": 'padrao', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'small_floral', "en": 'small floral-print', "tipo": 'padrao', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'scattered_leaf', "en": 'scattered leaf-print', "tipo": 'padrao', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'paisley_soft', "en": 'soft muted paisley', "tipo": 'padrao', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'boucle', "en": 'nubby boucle-textured', "tipo": 'padrao', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'eyelet', "en": 'fine eyelet-textured', "tipo": 'padrao', "pele": 'ambas', "sexo": 'mulher'},
]

# O que torna a peca especifica sem trocar a peca.
DETALHES_ROUPA = [
    {"id": 'bolso_peito', "en": 'with a chest pocket', "tipo": 'bolso', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'bolso_duplo_aba', "en": 'with two flap pockets across the chest', "tipo": 'bolso', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'bolso_caneta', "en": 'with a pen clipped inside the chest pocket', "tipo": 'bolso', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'bolso_lenco', "en": 'with a folded handkerchief showing in the chest pocket', "tipo": 'bolso', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'bolso_deformado', "en": 'with the chest pocket sagging out of shape', "tipo": 'bolso', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'bolso_mancha_tinta', "en": 'with a faded ink stain on the pocket', "tipo": 'bolso', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'bolso_ziper', "en": 'with a small zippered pocket on the chest', "tipo": 'bolso', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'bolso_fundo_frente', "en": 'with two deep patch pockets low on the front', "tipo": 'bolso', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'bolso_aba_solta', "en": 'with the pocket flap left unfastened', "tipo": 'bolso', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'bolso_aba_fechada', "en": 'with the pocket flap buttoned shut', "tipo": 'bolso', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'bolso_torto', "en": 'with the chest pocket sewn on slightly crooked', "tipo": 'bolso', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'bolso_bloco', "en": 'with a small notepad squared off in the chest pocket', "tipo": 'bolso', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'bolso_remendado', "en": 'with the chest pocket patched in a slightly different fabric', "tipo": 'bolso', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'bolso_fantasma', "en": 'with a sun-faded rectangle where a pocket used to be', "tipo": 'bolso', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'bolso_lenco_papel', "en": 'with a crumpled tissue pushed into the chest pocket', "tipo": 'bolso', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'bolso_costura_aberta', "en": 'with the pocket seam split open at one corner', "tipo": 'bolso', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'bolso_embutido', "en": 'with a narrow slit pocket set into the front seam', "tipo": 'bolso', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'bolso_dois_niveis', "en": 'with a small pocket set above a larger one on the chest', "tipo": 'bolso', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'botoes_pressao', "en": 'with pearl snap buttons', "tipo": 'fechamento', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'botoes_trocados', "en": 'with mismatched buttons', "tipo": 'fechamento', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'botao_faltando', "en": 'with one button missing near the waist', "tipo": 'fechamento', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'abotoado_pescoco', "en": 'buttoned all the way to the throat', "tipo": 'fechamento', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'dois_botoes_abertos', "en": 'with the top two buttons undone', "tipo": 'fechamento', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'meio_ziper', "en": 'with a half-zip pulled down at the neck', "tipo": 'fechamento', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'ziper_inteiro', "en": 'with a full-length zipper instead of buttons', "tipo": 'fechamento', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'botoes_grandes', "en": 'with oversized plain plastic buttons', "tipo": 'fechamento', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'botoes_madeira', "en": 'with dull wooden buttons', "tipo": 'fechamento', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'botoes_repuxando', "en": 'with the front buttons pulling into small gaps', "tipo": 'fechamento', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'cordao_barra', "en": 'with a drawstring gathered at the hem', "tipo": 'fechamento', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'carcela_reforcada', "en": 'with heavy double stitching down the front placket', "tipo": 'fechamento', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'botoes_desalinhados', "en": 'with the placket buttoned one hole off', "tipo": 'fechamento', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'ziper_cordao', "en": 'with a loop of string tied where the zipper pull broke off', "tipo": 'fechamento', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'botoes_linha_diferente', "en": 'with the buttons sewn back on in a different thread', "tipo": 'fechamento', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'velcro_adaptado', "en": 'with hook-and-loop tabs in place of buttons', "tipo": 'fechamento', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'ziper_travado', "en": 'with the zipper stopped halfway and stuck', "tipo": 'fechamento', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'pressao_gola_aberta', "en": 'with one snap left open at the collar', "tipo": 'fechamento', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'carcela_larga', "en": 'with a wide button band down the front', "tipo": 'fechamento', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'toggle_peito', "en": 'with a toggle fastening across the chest', "tipo": 'fechamento', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'colchete_gola', "en": 'with small hook and eye closures at the throat', "tipo": 'fechamento', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'botoes_forrados', "en": 'with a row of small fabric-covered buttons', "tipo": 'fechamento', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'mangas_cotovelo', "en": 'with the sleeves rolled to the elbow', "tipo": 'manga', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'mangas_antebraco', "en": 'with the sleeves pushed up on the forearms', "tipo": 'manga', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'punhos_soltos', "en": 'with the cuffs unbuttoned and hanging loose', "tipo": 'manga', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'punho_puido', "en": 'with a frayed cuff on one wrist', "tipo": 'manga', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'mangas_curtas_pulso', "en": 'with the sleeves ending short of the wrists', "tipo": 'manga', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'punhos_canelados', "en": 'with ribbed cuffs at the wrists', "tipo": 'manga', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'vinco_manga', "en": 'with a pressed crease running down each sleeve', "tipo": 'manga', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'cotovelo_reforco', "en": 'with reinforced patches at the elbows', "tipo": 'manga', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'cotovelo_gasto', "en": 'worn thin and shiny at the elbows', "tipo": 'manga', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'mangas_desiguais', "en": 'with one sleeve pushed higher than the other', "tipo": 'manga', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'punho_elastico', "en": 'with elastic gathering at the sleeve ends', "tipo": 'manga', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'punho_apertado', "en": 'with the cuffs buttoned tight against the wrists', "tipo": 'manga', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'costura_axila_aberta', "en": 'with the sleeve seam split open under one arm', "tipo": 'manga', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'manga_acima_cotovelo', "en": 'with short sleeves ending just above the elbow', "tipo": 'manga', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'punho_virado', "en": 'with the cuffs turned back to show a lighter underside', "tipo": 'manga', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'tira_manga', "en": 'with a buttoned tab holding each rolled sleeve in place', "tipo": 'manga', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'manga_larga_reta', "en": 'with wide straight sleeves hanging away from the arms', "tipo": 'manga', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'manga_tres_quartos', "en": 'with three-quarter sleeves ending mid-forearm', "tipo": 'manga', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'manga_curta_franzida', "en": 'with slightly gathered short sleeves at the shoulders', "tipo": 'manga', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'manga_cava', "en": 'with plain cap sleeves at the shoulders', "tipo": 'manga', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'gola_puida', "en": 'with a frayed collar', "tipo": 'gola', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'gola_mole', "en": 'with a soft worn-out collar', "tipo": 'gola', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'gola_levantada', "en": 'with the collar turned up at the back', "tipo": 'gola', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'gola_torta', "en": 'with the collar sitting crooked on one side', "tipo": 'gola', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'gola_larga_antiga', "en": 'with a wide dated collar', "tipo": 'gola', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'gola_v', "en": 'with a plain V neckline', "tipo": 'gola', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'gola_careca_frouxa', "en": 'with a plain crew neck stretched loose', "tipo": 'gola', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'gola_xale', "en": 'with a shawl collar', "tipo": 'gola', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'capuz_vazio', "en": 'with an empty hood bunched behind the neck', "tipo": 'gola', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'gola_role', "en": 'with a folded-over turtleneck collar', "tipo": 'gola', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'gola_entalhe', "en": 'with a plain notched collar', "tipo": 'gola', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'gola_engomada', "en": 'with a collar pressed flat and starched', "tipo": 'gola', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'gola_meio_role', "en": 'with a mock turtleneck at the throat', "tipo": 'gola', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'gola_carcela_curta', "en": 'with a short buttoned placket at the neck', "tipo": 'gola', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'gola_ponta_curvada', "en": 'with one collar point curling up', "tipo": 'gola', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'gola_padre', "en": 'with a plain stand collar closed at the throat', "tipo": 'gola', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'gola_debruada', "en": 'with the neckline trimmed in a contrasting band', "tipo": 'gola', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'gola_abotoada', "en": 'with the collar points buttoned down', "tipo": 'gola', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'gola_dupla_camada', "en": 'with a doubled collar band at the neck', "tipo": 'gola', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'gola_babado', "en": 'with a narrow ruffle along the neckline', "tipo": 'gola', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'gola_redonda', "en": 'with a small rounded collar', "tipo": 'gola', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'gola_bordada', "en": 'with plain embroidered trim around the neckline', "tipo": 'gola', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'laco_gola', "en": 'with a small fabric bow at the neckline', "tipo": 'gola', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'gola_drapeada', "en": 'with a soft cowl gathered at the neck', "tipo": 'gola', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'gola_canoa', "en": 'with a plain wide scoop neckline', "tipo": 'gola', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'bolinhas_pilling', "en": 'pilled all over the chest and shoulders', "tipo": 'desgaste', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'remendo_ombro', "en": 'with a small hand-stitched mend at the shoulder', "tipo": 'desgaste', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'marcas_dobra', "en": 'with fold creases still showing from the drawer', "tipo": 'desgaste', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'mancha_clara', "en": 'with a washed-out bleach spot near the hem', "tipo": 'desgaste', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'barra_solta', "en": 'with the hem coming loose in one place', "tipo": 'desgaste', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'ombros_desbotados', "en": 'sun-faded across the shoulders', "tipo": 'desgaste', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'linha_solta', "en": 'with a loose thread trailing from a seam', "tipo": 'desgaste', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'amassada_costas', "en": 'creased and slept-in across the back', "tipo": 'desgaste', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'gola_amarelada', "en": 'with the collar edge gone yellow with age', "tipo": 'desgaste', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'costura_refeita', "en": 'with a seam re-sewn in slightly different thread', "tipo": 'desgaste', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'forro_aparecendo', "en": 'with a soft lining showing at the cuffs', "tipo": 'desgaste', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'furo_queimadura', "en": 'with a small burn hole near the hem', "tipo": 'desgaste', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'mancha_cafe', "en": 'with a dried coffee stain on the chest', "tipo": 'desgaste', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'tecido_fino', "en": 'with the fabric gone soft and thin across the front', "tipo": 'desgaste', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'brilho_ferro', "en": 'with a faint pressed shine left by an iron', "tipo": 'desgaste', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'casa_botao_gasta', "en": 'with one buttonhole stretched open and fraying', "tipo": 'desgaste', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'mancha_fantasma', "en": 'with an old stain washed down to a faint shadow', "tipo": 'desgaste', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'fiapos_frente', "en": 'with lint clinging across the front', "tipo": 'desgaste', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'costura_franzida', "en": 'with the shoulder seam puckered from many washes', "tipo": 'desgaste', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'cor_desigual', "en": 'with the colour gone uneven from line drying', "tipo": 'desgaste', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'fio_puxado', "en": 'with a snag pulled into a small loop on the chest', "tipo": 'desgaste', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'felpa_achatada', "en": 'with a brushed fleece surface matted flat in patches', "tipo": 'desgaste', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'pala_ombros', "en": 'with a yoke seam across the shoulders', "tipo": 'construcao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'pesponto_contrastante', "en": 'with contrast stitching along the seams', "tipo": 'construcao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'debrum_ombro', "en": 'with piping along the shoulder seams', "tipo": 'construcao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'barra_canelada', "en": 'with a ribbed band at the hem', "tipo": 'construcao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'raglan', "en": 'with raglan sleeve seams running from the neck', "tipo": 'construcao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'costura_lateral', "en": 'with flat-felled seams down each side', "tipo": 'construcao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'painel_peito', "en": 'with a chest panel cut in a slightly different weave', "tipo": 'construcao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'trico_trancado', "en": 'with a cable-knit pattern down the front', "tipo": 'construcao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'malha_waffle', "en": 'with a waffle-textured knit surface', "tipo": 'construcao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'matelasse', "en": 'with quilted stitching across the chest', "tipo": 'construcao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'gorgurao_ombro', "en": 'with a strip of grosgrain tape along the shoulder seams', "tipo": 'construcao', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'elastico_costas', "en": 'with a shirred elastic panel at the back of the waist', "tipo": 'construcao', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'prega_frente', "en": 'with a pleated panel down the front', "tipo": 'construcao', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'pences_frente', "en": 'with shaping darts at the front', "tipo": 'construcao', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'recorte_abaixo_peito', "en": 'with a seam running below the chest', "tipo": 'construcao', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'ombro_caido', "en": 'with the shoulder seams sitting low on the arms', "tipo": 'caimento', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'gola_deslocada', "en": 'with the neckline pulled off-centre to one side', "tipo": 'caimento', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'vincos_radiais', "en": 'with the fabric pulled into radiating creases at the front', "tipo": 'caimento', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'torcido', "en": 'sitting twisted so the side seams have rotated forward', "tipo": 'caimento', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'camada_dupla', "en": 'with a second layer showing at the collar and cuffs', "tipo": 'caimento', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'mangas_frouxas', "en": 'with the sleeves hanging loose while the front pulls tight', "tipo": 'caimento', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'costura_lateral_tensa', "en": 'with the side seams strained and standing out', "tipo": 'caimento', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'gola_afastada_nuca', "en": 'with the collar standing away from the back of the neck', "tipo": 'caimento', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'ombro_quadrado', "en": 'with a stiff square shoulder line', "tipo": 'caimento', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'camiseta_por_baixo', "en": 'with a plain undershirt showing at the open collar', "tipo": 'caimento', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'oculos_gola', "en": 'with a pair of reading glasses hooked in the neckline', "tipo": 'acessorio', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'cordao_oculos', "en": 'with an eyeglass cord looped behind the collar', "tipo": 'acessorio', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'guardanapo_gola', "en": 'with a cloth napkin tucked into the collar', "tipo": 'acessorio', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'papel_toalha_gola', "en": 'with a folded paper towel tucked at the neckline', "tipo": 'acessorio', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'relogio_punho', "en": 'with a plain metal watch band showing under the cuff', "tipo": 'acessorio', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'corrente_fina', "en": 'with a thin plain chain resting at the throat', "tipo": 'acessorio', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'cachecol_tricot', "en": 'with a plain knit scarf folded at the neck', "tipo": 'acessorio', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'gravata_clipe', "en": 'with a plain clip-on tie loosened at the collar', "tipo": 'acessorio', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'suspensorio', "en": 'with plain suspender straps over the shoulders', "tipo": 'acessorio', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'xale_ombros', "en": 'with a light shawl draped over the shoulders', "tipo": 'acessorio', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'flor_gola', "en": 'with a small plain fabric flower pinned at the collar', "tipo": 'acessorio', "pele": 'ambas', "sexo": 'mulher'},
]

# `tipo`: `formato` (osso e mandibula), `nariz`, `boca`.
# Arquitetura, nunca cor de pele.
ROSTOS = [
    {"id": 'quadrado_mandibula_pesada', "en": 'a square face with a heavy jaw', "tipo": 'formato', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'longo_queixo_estreito', "en": 'a long face with a narrow chin', "tipo": 'formato', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'redondo_bochechas_cheias', "en": 'a round face with full cheeks', "tipo": 'formato', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'largo_macas_altas', "en": 'a broad face with high flat cheekbones', "tipo": 'formato', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'coracao_queixo_pontudo', "en": 'a heart-shaped face with a pointed chin', "tipo": 'formato', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'oval_mandibula_macia', "en": 'an oval face with a softly rounded jawline', "tipo": 'formato', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'retangular_mandibula_reta', "en": 'a rectangular face with a long flat jaw', "tipo": 'formato', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'diamante_queixo_pequeno', "en": 'a diamond-shaped face with wide cheekbones and a small chin', "tipo": 'formato', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'triangular_base_larga', "en": 'a triangular face that widens toward the jaw', "tipo": 'formato', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'testa_alta_abaulada', "en": 'a tall face with a high domed forehead', "tipo": 'formato', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'papada_lateral', "en": 'a wide face with heavy jowls along the jaw', "tipo": 'formato', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'macas_baixas', "en": 'a flat face with low set cheekbones', "tipo": 'formato', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'testa_estreita_mandibula_larga', "en": 'a narrow forehead over a wide heavy jaw', "tipo": 'formato', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'arcada_marcada', "en": 'a blunt face with a strong brow ridge', "tipo": 'formato', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'queixo_recuado', "en": 'a soft face with a receding chin', "tipo": 'formato', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'mandibula_quadrada_testa_curta', "en": 'a wide square jaw and a short forehead', "tipo": 'formato', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'bochechas_baixas_pesadas', "en": 'a rounded face with heavy lower cheeks', "tipo": 'formato', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'rosto_curto_compacto', "en": 'a short compact face with a small tight jaw', "tipo": 'formato', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'assimetrico', "en": 'a slightly uneven face with one cheek fuller than the other', "tipo": 'formato', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'macas_largas_arredondadas', "en": 'a broad face with soft wide cheekbones and no sharp jaw corners', "tipo": 'formato', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'testa_larga_queixo_largo', "en": 'a wide forehead and a broad flat chin', "tipo": 'formato', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'pera_pesado_embaixo', "en": 'a pear-shaped face heaviest at the jawline', "tipo": 'formato', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'ossudo_linha_capilar_quadrada', "en": 'a big-boned face with a deep set brow and a square hairline', "tipo": 'formato', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'lua_tracos_pequenos', "en": 'a full moon-shaped face with small close-set features', "tipo": 'formato', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'rosto_marcado_intemperie', "en": 'a weathered face with deep creases across both cheeks', "tipo": 'formato', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'rosto_corado_vasos', "en": 'a ruddy face with broken capillaries across the cheeks', "tipo": 'formato', "pele": 'branca', "sexo": 'ambos'},
    {"id": 'rosto_sardas_desbotadas', "en": 'a pale face with faded freckles over the nose and cheeks', "tipo": 'formato', "pele": 'branca', "sexo": 'ambos'},
    {"id": 'testa_recuada_alta', "en": 'a tall face with the hairline set far back', "tipo": 'formato', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'testa_baixa_sobrancelha_curta', "en": 'a heavy face with a low hairline over a short brow', "tipo": 'formato', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'rosto_liso_sem_linhas', "en": 'a smooth full face with almost no lines', "tipo": 'formato', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'rosto_cicatriz_sobrancelha', "en": 'a broad face with a faint old scar above one eyebrow', "tipo": 'formato', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'rosto_cansado_sombras', "en": 'a tired face with deep shadows under the eyes', "tipo": 'formato', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'rosto_tom_profundo_uniforme', "en": 'a full face with rich even dark skin and high round cheeks', "tipo": 'formato', "pele": 'negra', "sexo": 'ambos'},
    {"id": 'nariz_largo_achatado', "en": 'a broad flat nose', "tipo": 'nariz', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'nariz_adunco_estreito', "en": 'a narrow hooked nose', "tipo": 'nariz', "pele": 'branca', "sexo": 'ambos'},
    {"id": 'nariz_arrebitado_curto', "en": 'a short upturned nose', "tipo": 'nariz', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'nariz_reto_com_calo', "en": 'a straight bridged nose with a slight bump', "tipo": 'nariz', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'nariz_narinas_abertas', "en": 'a wide nose with rounded flaring nostrils', "tipo": 'nariz', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'nariz_bulboso', "en": 'a bulbous nose with a thick rounded tip', "tipo": 'nariz', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'nariz_longo_ponta_fina', "en": 'a long straight nose with a narrow tip', "tipo": 'nariz', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'nariz_pequeno_alto', "en": 'a small button nose set high between the eyes', "tipo": 'nariz', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'nariz_carnudo_base_larga', "en": 'a fleshy nose that spreads at the base', "tipo": 'nariz', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'nariz_aquilino', "en": 'a sharp aquiline nose with a high thin bridge', "tipo": 'nariz', "pele": 'branca', "sexo": 'ambos'},
    {"id": 'nariz_torto', "en": 'a slightly crooked nose that leans to one side', "tipo": 'nariz', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'nariz_ponte_baixa', "en": 'a wide nose with a low flat bridge', "tipo": 'nariz', "pele": 'negra', "sexo": 'ambos'},
    {"id": 'nariz_pequeno_colado', "en": 'a small neat nose set close to the face', "tipo": 'nariz', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'nariz_pesado_sulco_fundo', "en": 'a heavy nose with a deep groove above the lip', "tipo": 'nariz', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'nariz_fino_apertado', "en": 'a thin pinched nose with tight nostrils', "tipo": 'nariz', "pele": 'branca', "sexo": 'ambos'},
    {"id": 'nariz_largo_ponte_arredondada', "en": 'a broad nose with a wide rounded bridge and full nostrils', "tipo": 'nariz', "pele": 'negra', "sexo": 'ambos'},
    {"id": 'nariz_ponta_caida', "en": 'a downturned nose with a drooping tip', "tipo": 'nariz', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'nariz_ponta_quadrada', "en": 'a straight nose with a squared-off tip', "tipo": 'nariz', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'nariz_ponte_amassada', "en": 'a bridge flattened across the middle as if broken long ago', "tipo": 'nariz', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'nariz_estreito_ponta_larga', "en": 'a narrow bridge that widens into a heavy tip', "tipo": 'nariz', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'nariz_ponta_bifida', "en": 'a broad nose with a slight split at the tip', "tipo": 'nariz', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'nariz_asas_finas', "en": 'a straight nose with thin flat nostril wings', "tipo": 'nariz', "pele": 'branca', "sexo": 'ambos'},
    {"id": 'nariz_curto_largo_baixo', "en": 'a short wide nose that sits low on the face', "tipo": 'nariz', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'nariz_ponte_alta_estreita', "en": 'a high narrow bridge running in a slim straight line', "tipo": 'nariz', "pele": 'branca', "sexo": 'ambos'},
    {"id": 'nariz_poros_grossos', "en": 'a heavy nose with coarse open pores at the tip', "tipo": 'nariz', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'nariz_inclinado_narinas_visiveis', "en": 'a tilted nose that shows the nostrils from the front', "tipo": 'nariz', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'nariz_dorso_ondulado', "en": 'a nose with a wavy line running down the bridge', "tipo": 'nariz', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'nariz_grande_dominante', "en": 'an oversized nose that dominates the middle of the face', "tipo": 'nariz', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'nariz_discreto_pequeno', "en": 'a small unremarkable nose that barely rises from the face', "tipo": 'nariz', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'nariz_ponta_carnuda_vinco', "en": 'a thick nose with a soft crease across the tip', "tipo": 'nariz', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'nariz_narinas_estreitas_inclinadas', "en": 'a long nose with narrow slanted nostrils', "tipo": 'nariz', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'nariz_reto_curto_acima_labio', "en": 'a wide straight nose that stops short above the lip', "tipo": 'nariz', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'boca_labios_finos_linhas', "en": 'thin lips with deep lines at the corners', "tipo": 'boca', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'boca_larga_queixo_covinha', "en": 'a wide mouth and a dimpled chin', "tipo": 'boca', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'boca_cheia_queixo_duplo', "en": 'full lips and a soft double chin', "tipo": 'boca', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'boca_pequena_labio_fino', "en": 'a small mouth with a very thin upper lip', "tipo": 'boca', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'boca_caida_linhas_marionete', "en": 'a downturned mouth with heavy lines running to the jaw', "tipo": 'boca', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'boca_larga_queixo_amplo', "en": 'wide full lips over a broad flat chin', "tipo": 'boca', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'boca_estreita_queixo_curto', "en": 'a narrow mouth and a short blunt chin', "tipo": 'boca', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'boca_dentes_separados', "en": 'a gap between the front teeth showing when the mouth opens', "tipo": 'boca', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'boca_covinha_uma_bochecha', "en": 'an even mouth with a deep dimple in one cheek', "tipo": 'boca', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'boca_linha_reta_queixo_projetado', "en": 'lips that press into a flat line and a jutting chin', "tipo": 'boca', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'boca_labio_inferior_cheio', "en": 'a full lower lip and a weak chin folded into the neck', "tipo": 'boca', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'boca_linhas_riso_fundas', "en": 'a broad mouth with laugh lines carved deep', "tipo": 'boca', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'boca_canto_mais_alto', "en": 'a mouth that sits a little higher on one side', "tipo": 'boca', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'boca_fina_queixo_longo', "en": 'thin drawn lips over a long chin', "tipo": 'boca', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'boca_macia_queixo_com_vinco', "en": 'full soft lips and a rounded chin with a crease beneath it', "tipo": 'boca', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'boca_franzida_linhas_verticais', "en": 'a small pursed mouth with vertical lines above the upper lip', "tipo": 'boca', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'boca_labios_entreabertos', "en": 'heavy lips that rest slightly parted', "tipo": 'boca', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'boca_vincos_nasolabiais', "en": 'a wide mouth with strong creases running up to the nostrils', "tipo": 'boca', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'boca_labio_inferior_avancado', "en": 'a lower lip that pushes forward past the upper one', "tipo": 'boca', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'boca_queixo_fendido', "en": 'a cleft in the chin and a straight even mouth', "tipo": 'boca', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'boca_cantos_baixos_labios_medios', "en": 'medium lips with the corners settled low and a square chin', "tipo": 'boca', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'boca_labios_rachados', "en": 'dry chapped lips with flaking corners', "tipo": 'boca', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'boca_filtro_longo', "en": 'a long space between the nose and a thin upper lip', "tipo": 'boca', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'boca_arco_cupido', "en": "a clear cupid's bow over a soft lower lip", "tipo": 'boca', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'boca_contorno_escuro', "en": 'well-defined lips with a darker outline', "tipo": 'boca', "pele": 'negra', "sexo": 'ambos'},
    {"id": 'boca_dentes_amarelados', "en": 'front teeth stained yellow with age', "tipo": 'boca', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'boca_dentadura', "en": 'even too-white denture teeth that show when the mouth opens', "tipo": 'boca', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'boca_muito_larga_labios_finos', "en": 'a very wide mouth with thin flat lips', "tipo": 'boca', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'boca_pequena_redonda', "en": 'a small round mouth set high above the chin', "tipo": 'boca', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'boca_labios_iguais_cheios', "en": 'evenly full lips of about the same thickness', "tipo": 'boca', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'boca_superior_fino_inferior_cheio', "en": 'a thin upper lip over a much fuller lower one', "tipo": 'boca', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'boca_vinco_mento', "en": 'a deep horizontal crease between the lower lip and the chin', "tipo": 'boca', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'boca_dente_faltando', "en": 'a missing tooth showing to one side when the mouth opens', "tipo": 'boca', "pele": 'ambas', "sexo": 'ambos'},
]

# Cor + palpebra + sobrancelha. E' aqui que a tag de pele
# mais importa: olho azul/verde nunca e' `ambas`.
OLHOS = [
    {"id": 'castanho_fundo_pesado', "en": 'deep-set dark brown eyes under heavy lids', "tipo": 'olhos', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'castanho_afastado_pes', "en": "wide-set warm brown eyes with deep crow's feet at the corners", "tipo": 'olhos', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'castanho_pequeno_junto', "en": 'small dark brown eyes set close together under a low brow', "tipo": 'olhos', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'castanho_redondo_bolsa', "en": 'round brown eyes with puffy lower lids', "tipo": 'olhos', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'castanho_amendoado_caido', "en": 'almond-shaped brown eyes with softly downturned outer corners', "tipo": 'olhos', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'castanho_lid_caida_brow_cinza', "en": 'dark brown eyes half covered by drooping upper lids, under thick gray brows', "tipo": 'olhos', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'castanho_brow_rala', "en": 'brown eyes under thin sparse brows that fade out before the temple', "tipo": 'olhos', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'castanho_lacrimejante', "en": 'watery brown eyes with sore-looking lower lids', "tipo": 'olhos', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'castanho_quase_preto', "en": 'near-black eyes with very dark lashes and no visible line between iris and pupil', "tipo": 'olhos', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'castanho_bolsas_fundas', "en": 'brown eyes sitting above heavy under-eye pouches', "tipo": 'olhos', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'castanho_estreito_sorriso', "en": 'narrow brown eyes that nearly disappear when the cheeks lift', "tipo": 'olhos', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'castanho_brilhante_rugas', "en": 'bright brown eyes with a wet shine, ringed by fine wrinkles', "tipo": 'olhos', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'mel_capuz_dobra', "en": 'hooded honey-brown eyes under a heavy fold of skin', "tipo": 'olhos', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'avela_fundo_flecks', "en": 'deep-set hazel eyes flecked with green and gold', "tipo": 'olhos', "pele": 'branca', "sexo": 'ambos'},
    {"id": 'avela_brow_arqueada', "en": 'hazel eyes under high arched brows, wide open and alert', "tipo": 'olhos', "pele": 'branca', "sexo": 'ambos'},
    {"id": 'ambar_lid_pesada', "en": 'amber eyes under heavy lids and short thin lashes', "tipo": 'olhos', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'mel_afastado_aberto', "en": 'wide-set honey-colored eyes with a warm open stare', "tipo": 'olhos', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'ambar_pequeno_tenso', "en": 'small amber-brown eyes set deep behind tight lids', "tipo": 'olhos', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'azul_pequeno_crinkles', "en": 'small pale blue eyes buried in fine crinkles', "tipo": 'olhos', "pele": 'branca', "sexo": 'ambos'},
    {"id": 'azul_gelo_anel', "en": 'washed-out ice blue eyes with a faint pale ring around each iris', "tipo": 'olhos', "pele": 'branca', "sexo": 'ambos'},
    {"id": 'azul_aco_brow_branca', "en": 'wide-set steel blue eyes under bushy white brows', "tipo": 'olhos', "pele": 'branca', "sexo": 'ambos'},
    {"id": 'azul_capuz_solto', "en": 'hooded cornflower blue eyes with loose lids hanging at the outer corners', "tipo": 'olhos', "pele": 'branca', "sexo": 'ambos'},
    {"id": 'azul_lid_rosada', "en": 'watery blue eyes with pink-rimmed lids', "tipo": 'olhos', "pele": 'branca', "sexo": 'ambos'},
    {"id": 'azul_marinho_fundo', "en": 'deep-set dark blue eyes shadowed under a strong brow ridge', "tipo": 'olhos', "pele": 'branca', "sexo": 'ambos'},
    {"id": 'azul_desbotado_bolsas', "en": 'faded blue eyes over pronounced under-eye bags', "tipo": 'olhos', "pele": 'branca', "sexo": 'ambos'},
    {"id": 'azul_cilios_palidos', "en": 'pale blue eyes with almost invisible light lashes', "tipo": 'olhos', "pele": 'branca', "sexo": 'ambos'},
    {"id": 'azul_brow_fina_alerta', "en": 'sharp light blue eyes wide open under thin arched brows', "tipo": 'olhos', "pele": 'branca', "sexo": 'ambos'},
    {"id": 'azul_brow_arame_branco', "en": 'blue eyes under brows gone completely white and wiry', "tipo": 'olhos', "pele": 'branca', "sexo": 'ambos'},
    {"id": 'azul_brow_loira_grisalha', "en": 'blue eyes under reddish-blond brows going half gray', "tipo": 'olhos', "pele": 'branca', "sexo": 'ambos'},
    {"id": 'verde_musgo_brow_clara', "en": 'small mossy green eyes under sparse sandy brows', "tipo": 'olhos', "pele": 'branca', "sexo": 'ambos'},
    {"id": 'verde_anel_escuro', "en": 'clear green eyes with a dark outer ring and short pale lashes', "tipo": 'olhos', "pele": 'branca', "sexo": 'ambos'},
    {"id": 'verde_cinza_junto', "en": 'gray-green eyes set close together over a narrow bridge', "tipo": 'olhos', "pele": 'branca', "sexo": 'ambos'},
    {"id": 'verde_oliva_capuz', "en": 'hooded olive-green eyes with heavy skin folding over the outer half', "tipo": 'olhos', "pele": 'branca', "sexo": 'ambos'},
    {"id": 'verde_sardas_palpebra', "en": 'green eyes ringed by faded freckles across the lids', "tipo": 'olhos', "pele": 'branca', "sexo": 'ambos'},
    {"id": 'verde_manchas_sol', "en": 'green eyes with sandy lashes and sun spots scattered across the lids', "tipo": 'olhos', "pele": 'branca', "sexo": 'ambos'},
    {"id": 'cinza_azul_sem_cilio', "en": 'flat gray-blue eyes with almost no visible lash line', "tipo": 'olhos', "pele": 'branca', "sexo": 'ambos'},
    {"id": 'cinza_palido_brow_reta', "en": 'pale gray eyes under straight heavy brows', "tipo": 'olhos', "pele": 'branca', "sexo": 'ambos'},
    {"id": 'cinza_verde_osso_frontal', "en": 'deep-set gray-green eyes shadowed by a heavy brow bone', "tipo": 'olhos', "pele": 'branca', "sexo": 'ambos'},
    {"id": 'castanho_brow_quase_junta', "en": 'dark brown eyes under brows that nearly meet above the nose', "tipo": 'olhos', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'castanho_assimetrico', "en": 'slightly uneven brown eyes, the left sitting lower than the right', "tipo": 'olhos', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'castanho_grande_calmo', "en": 'large soft brown eyes with a patient unhurried look', "tipo": 'olhos', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'castanho_brow_lapis', "en": 'brown eyes under thin brows drawn in with a pencil line', "tipo": 'olhos', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'castanho_rimel_borrado', "en": 'dark brown eyes with a trace of smudged mascara on the lower lashes', "tipo": 'olhos', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'castanho_liner_desbotado', "en": 'brown eyes with a faded line of liner left on the lower lid', "tipo": 'olhos', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'azul_sombra_suave', "en": 'pale blue eyes with soft blue-gray shadow worn into the crease', "tipo": 'olhos', "pele": 'branca', "sexo": 'mulher'},
    {"id": 'azul_cilios_curvados', "en": 'small blue eyes under short curled lashes', "tipo": 'olhos', "pele": 'branca', "sexo": 'mulher'},
    {"id": 'castanho_brow_selvagem', "en": 'brown eyes half hidden by wild untrimmed brows', "tipo": 'olhos', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'castanho_brow_cheia_grisalha', "en": 'brown eyes under full brows gone salt-and-pepper', "tipo": 'olhos', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'castanho_olheira_funda', "en": 'brown eyes with dark circles pressed deep beneath them', "tipo": 'olhos', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'castanho_semicerrado', "en": 'brown eyes squeezed into a permanent squint', "tipo": 'olhos', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'castanho_linhas_de_riso', "en": 'brown eyes with fans of laugh lines cut deep at the corners', "tipo": 'olhos', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'castanho_pele_crepe', "en": 'brown eyes with a loose crepey fold of skin resting on the lashes', "tipo": 'olhos', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'avela_sacos_vincados', "en": 'hazel eyes over soft creased bags', "tipo": 'olhos', "pele": 'branca', "sexo": 'ambos'},
    {"id": 'castanho_cilios_baixos_grossos', "en": 'large dark brown eyes with thick lower lashes', "tipo": 'olhos', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'castanho_brow_torta', "en": 'brown eyes under one brow permanently raised higher than the other', "tipo": 'olhos', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'castanho_canto_erguido', "en": 'brown eyes with slightly upturned outer corners', "tipo": 'olhos', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'castanho_lid_seca', "en": 'dry-looking brown eyes with finely creased lids', "tipo": 'olhos', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'castanho_anel_azulado', "en": 'brown eyes with a thin bluish-white ring at the outer edge of each iris', "tipo": 'olhos', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'castanho_lid_inchada', "en": 'brown eyes with sparse lashes and slightly swollen lids', "tipo": 'olhos', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'castanho_brow_baixa_sombra', "en": 'brown eyes under a low straight brow that keeps them in shadow', "tipo": 'olhos', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'castanho_brow_quase_sumida', "en": 'brown eyes under brows thinned to a few gray hairs', "tipo": 'olhos', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'castanho_encara_fixo', "en": 'steady dark brown eyes that hold the camera without blinking', "tipo": 'olhos', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'castanho_um_canto_caido', "en": 'brown eyes with the outer corner of one lid sagging lower', "tipo": 'olhos', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'castanho_vinco_entre_brow', "en": 'brown eyes under a deep vertical crease pressed between the brows', "tipo": 'olhos', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'castanho_saliente', "en": 'slightly protruding brown eyes with a wide unblinking look', "tipo": 'olhos', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'castanho_sinal_canto', "en": 'brown eyes with a small dark mole just below one outer corner', "tipo": 'olhos', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'castanho_cicatriz_brow', "en": 'brown eyes under a brow broken by a faint old scar at the tail', "tipo": 'olhos', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'castanho_catarata_leve', "en": 'brown eyes with a faint milky haze clouding one of them', "tipo": 'olhos', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'castanho_olhar_de_lado', "en": 'brown eyes that slide to the side instead of meeting the lens', "tipo": 'olhos', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'castanho_cilios_curtos_ralos', "en": 'brown eyes with lashes so short and sparse the bare lid line shows', "tipo": 'olhos', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'castanho_lid_frouxa', "en": 'brown eyes with slack lower lids hanging a little away from the eye', "tipo": 'olhos', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'castanho_piscar_lento', "en": 'tired brown eyes with a slow heavy blink', "tipo": 'olhos', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'castanho_iris_cobre', "en": 'warm reddish-brown eyes that turn coppery in direct light', "tipo": 'olhos', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'castanho_lid_pigmentada', "en": 'deep brown eyes with naturally dark lids and thick black lashes', "tipo": 'olhos', "pele": 'negra', "sexo": 'ambos'},
]

# `tipo`: `cabelo` ou `barba`. Quase tudo com marca de
# idade, porque o sujeito tem 50+.
CABELOS = [
    {"id": 'careca_total', "en": 'a completely bald head', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'calvo_ferradura', "en": 'a bald crown with a close-cropped gray horseshoe of hair around the sides', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'careca_lateral_longa', "en": 'a bald top with the side hair left long enough to touch the ears', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'entradas_fundas', "en": 'a deeply receding hairline with thin gray hair combed straight back', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'raspado_stubble', "en": 'a closely shaved head showing a shadow of gray stubble', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'careca_cicatriz', "en": 'a shaved head with a smooth shine and an old scar above one ear', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'tufo_frontal_isolado', "en": 'a bald scalp with one stubborn tuft of white hair left at the front', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'flat_top', "en": 'a short military flat top of steel-gray hair', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'penteado_lado', "en": 'short salt-and-pepper hair combed neatly to one side', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'ondulado_prateado', "en": 'thick wavy silver hair swept back over the ears', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'rabo_baixo', "en": 'long gray hair gathered into a low ponytail at the nape', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'ombro_atras_orelhas', "en": 'shoulder-length white hair tucked behind the ears', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'tufos_bagunca', "en": 'unruly gray hair sticking up in tufts above the ears', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'comb_over', "en": 'a few thin gray strands combed across a bare scalp', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'crew_cut', "en": 'a neat gray crew cut', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'buzz_branco', "en": 'a uniform buzz cut of white stubble', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'widow_peak', "en": "a sharp widow's peak of dark hair heavily streaked with gray", "tipo": 'cabelo', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'pomada_temporas', "en": 'short dark hair going gray at the temples, slicked down flat', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'coroa_rala', "en": 'thinning gray hair with a bare patch showing at the crown', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'iron_gray_parted', "en": 'coarse iron-gray hair parted low on one side', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'repartido_meio', "en": 'gray hair parted down the middle and tucked behind both ears', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'molhado_penteado', "en": 'gray hair pressed flat and damp, as if just combed with water', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'anel_de_bone', "en": 'gray hair flattened into a ring all the way around the head', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'branco_grosso_quadrado', "en": 'a full head of thick white hair cut short and squared off at the neck', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'ivy_league', "en": 'a short gray cut neatly tapered at the neck', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'taper_alto_homem', "en": 'a high taper with an inch of gray left on top', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'franja_reta', "en": 'thick gray hair cut short with a straight fringe across the forehead', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'frente_penteada_baixa', "en": 'thin gray hair brushed forward into a short fringe', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'topete_baixo', "en": 'short gray hair brushed up into a low pompadour at the front', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'cacheado_curto_denso', "en": 'curly gray hair cropped short and dense on top', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'crescido_sobre_orelhas', "en": 'thick gray hair grown out past its last cut, curling over the ears', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'nuca_comprida', "en": 'gray hair cut short at the front and left long over the collar', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'preto_tingido_homem', "en": 'hair dyed a flat uniform black too dark for his age', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'amarelado_frente', "en": 'coarse silver hair with a yellowed tint at the front', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'ruivo_desbotado', "en": 'faded red hair now mostly sandy gray, cut short', "tipo": 'cabelo', "pele": 'branca', "sexo": 'homem'},
    {"id": 'loiro_esbranquicado_ralo', "en": 'wispy white-blond hair thin enough to show the scalp', "tipo": 'cabelo', "pele": 'branca', "sexo": 'homem'},
    {"id": 'loiro_escuro_apagado', "en": 'dark blond hair dulled to gray-brown, cut short', "tipo": 'cabelo', "pele": 'branca', "sexo": 'homem'},
    {"id": 'careca_manchas_sol', "en": 'a bald scalp mottled with brown sun spots', "tipo": 'cabelo', "pele": 'branca', "sexo": 'homem'},
    {"id": 'careca_marca_chapeu', "en": 'a bald head tanned dark with a pale band across the forehead', "tipo": 'cabelo', "pele": 'branca', "sexo": 'homem'},
    {"id": 'grisalho_rosado_homem', "en": 'thin white hair over a scalp that shows pink at the crown', "tipo": 'cabelo', "pele": 'branca', "sexo": 'homem'},
    {"id": 'locs_curtos_homem', "en": 'short gray locs pulled back off the forehead', "tipo": 'cabelo', "pele": 'negra', "sexo": 'homem'},
    {"id": 'afro_baixo_fade', "en": 'a low gray afro faded close at the sides', "tipo": 'cabelo', "pele": 'negra', "sexo": 'homem'},
    {"id": 'afro_grisalho_medio', "en": 'a rounded gray afro grown a few inches out', "tipo": 'cabelo', "pele": 'negra', "sexo": 'homem'},
    {"id": 'coils_lineup', "en": 'tight gray coils cut short with a sharp lined-up hairline', "tipo": 'cabelo', "pele": 'negra', "sexo": 'homem'},
    {"id": 'ferradura_coils', "en": 'a bald crown ringed by tight white coils above the ears', "tipo": 'cabelo', "pele": 'negra', "sexo": 'homem'},
    {"id": 'cornrows_homem', "en": 'short cornrows running straight back, gray at the temples', "tipo": 'cabelo', "pele": 'negra', "sexo": 'homem'},
    {"id": 'waves_curtos', "en": 'short gray hair brushed flat into tight waves', "tipo": 'cabelo', "pele": 'negra', "sexo": 'homem'},
    {"id": 'careca_lineup', "en": 'a shaved head with a sharply lined-up hairline and gray at the edges', "tipo": 'cabelo', "pele": 'negra', "sexo": 'homem'},
    {"id": 'twists_curtos_homem', "en": 'short gray twists standing up all over the head', "tipo": 'cabelo', "pele": 'negra', "sexo": 'homem'},
    {"id": 'coque_baixo', "en": 'gray hair pulled into a tight low bun', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'coque_solto', "en": 'silver hair gathered in a loose bun with strands falling around the face', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'coque_alto_pin', "en": 'a high round bun of white hair held with a plain pin', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'french_twist', "en": 'a loose twist of silver hair pinned at the back of the head', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'rabo_cavalo', "en": 'a shoulder-length gray ponytail pulled back tight from the face', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'rabo_curto_toco', "en": 'gray hair yanked back into a short stub of a ponytail with a plain elastic', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'meio_preso', "en": 'shoulder-length gray hair with the top half pinned back', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'curto_liso', "en": 'short straight gray hair cut just below the ears', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'bob_franja', "en": 'a chin-length silver bob with a blunt fringe', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'camadas_orelha', "en": 'layered gray hair falling just past the ears', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'franja_lateral', "en": 'gray hair with a long side-swept fringe over one eyebrow', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'ondulado_ombro', "en": 'shoulder-length wavy salt-and-pepper hair', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'permanente_curta', "en": 'a short tightly permed cap of gray curls', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'permanente_crescida', "en": 'a grown-out perm, straight at the roots and still curled at the ends', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'comprido_solto', "en": 'long white hair worn loose over the shoulders', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'presilha', "en": 'gray hair clipped back from the temples with a plain barrette', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'pixie', "en": 'a cropped gray pixie cut', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'curto_sem_estilo', "en": 'very short gray hair cut close with no styling at all', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'lenco_algodao', "en": 'a faded cotton kerchief knotted over short gray hair', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'rede_cabelo', "en": 'a fine hairnet over set gray curls', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'rolinhos_espuma', "en": 'gray hair with a few pink foam curlers still in at the crown', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'ondas_salao', "en": 'gray hair set in stiff waves, freshly done at a salon', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'tintura_raizes', "en": 'hair dyed a flat brassy brown with gray roots showing at the part', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'mecha_branca_frente', "en": 'dark hair with a single white streak sweeping back from the forehead', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'volume_topo', "en": 'thinning gray hair teased for volume at the crown', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'atras_orelhas_achatado', "en": 'short gray hair pushed behind the ears and flattened on one side', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'mulher'},
    {"id": 'trancas_finas_topo', "en": 'two thin gray braids pinned across the top of the head', "tipo": 'cabelo', "pele": 'branca', "sexo": 'mulher'},
    {"id": 'tranca_lateral_branca', "en": 'a thin gray braid hanging forward over one shoulder', "tipo": 'cabelo', "pele": 'branca', "sexo": 'mulher'},
    {"id": 'auburn_risca', "en": 'shoulder-length hair dyed dark auburn with silver showing along the part', "tipo": 'cabelo', "pele": 'branca', "sexo": 'mulher'},
    {"id": 'morango_desbotado', "en": 'faded strawberry-blond hair, more white than red, cut to the jaw', "tipo": 'cabelo', "pele": 'branca', "sexo": 'mulher'},
    {"id": 'loiro_oxigenado_raiz', "en": 'brittle bleached-blond hair with an inch of white regrowth at the roots', "tipo": 'cabelo', "pele": 'branca', "sexo": 'mulher'},
    {"id": 'platinado_salao', "en": 'hair dyed a soft platinum blond and set in loose curls', "tipo": 'cabelo', "pele": 'branca', "sexo": 'mulher'},
    {"id": 'cobre_tingido', "en": 'hair dyed a flat copper red with white showing at the temples', "tipo": 'cabelo', "pele": 'branca', "sexo": 'mulher'},
    {"id": 'fino_couro_rosado', "en": 'fine white hair so thin the pink scalp shows through', "tipo": 'cabelo', "pele": 'branca', "sexo": 'mulher'},
    {"id": 'box_braids', "en": 'shoulder-length box braids streaked with gray', "tipo": 'cabelo', "pele": 'negra', "sexo": 'mulher'},
    {"id": 'twists_gray', "en": 'thick gray twists gathered at the back of the head', "tipo": 'cabelo', "pele": 'negra', "sexo": 'mulher'},
    {"id": 'coils_naturais_curtos', "en": 'short natural coils of tight gray hair', "tipo": 'cabelo', "pele": 'negra', "sexo": 'mulher'},
    {"id": 'afro_redondo', "en": 'a gray afro cut close and round', "tipo": 'cabelo', "pele": 'negra', "sexo": 'mulher'},
    {"id": 'trancas_longas_coque', "en": 'long thin braids, half of them silver, pulled up into a bun', "tipo": 'cabelo', "pele": 'negra', "sexo": 'mulher'},
    {"id": 'cornrows_mulher', "en": 'neat cornrows running straight back, gray along the hairline', "tipo": 'cabelo', "pele": 'negra', "sexo": 'mulher'},
    {"id": 'locs_ombro', "en": 'shoulder-length locs gone gray from the roots', "tipo": 'cabelo', "pele": 'negra', "sexo": 'mulher'},
    {"id": 'raspada_mulher', "en": 'a smoothly shaved scalp with the faintest white shadow', "tipo": 'cabelo', "pele": 'negra', "sexo": 'mulher'},
    {"id": 'bob_alisado', "en": 'a straightened gray bob pressed flat and turned under at the ends', "tipo": 'cabelo', "pele": 'negra', "sexo": 'mulher'},
    {"id": 'relaxado_curto', "en": 'short relaxed hair swept back, gray at the front', "tipo": 'cabelo', "pele": 'negra', "sexo": 'mulher'},
    {"id": 'finger_waves', "en": 'short gray hair pressed into flat finger waves', "tipo": 'cabelo', "pele": 'negra', "sexo": 'mulher'},
    {"id": 'peruca_lisa', "en": 'a straight dark wig cut to the shoulders, sitting slightly off at the hairline', "tipo": 'cabelo', "pele": 'negra', "sexo": 'mulher'},
    {"id": 'turbante_algodao', "en": 'a printed cotton head wrap tied high off the forehead', "tipo": 'cabelo', "pele": 'negra', "sexo": 'mulher'},
    {"id": 'touca_cetim', "en": 'a plain satin sleep bonnet pulled over her hair', "tipo": 'cabelo', "pele": 'negra', "sexo": 'mulher'},
    {"id": 'ralo_curto', "en": 'short thinning gray hair', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'branco_cropped', "en": 'closely cropped white hair', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'dormido_de_lado', "en": 'gray hair flattened on one side as if slept on', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'grisalho_sem_forma', "en": 'medium-length gray hair with no particular shape to it', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'raizes_brancas', "en": 'dark hair with two inches of white grown out at the roots', "tipo": 'cabelo', "pele": 'ambas', "sexo": 'ambos'},
    {"id": 'barba_limpo', "en": 'a clean-shaven face', "tipo": 'barba', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'barba_limpo_sombra', "en": 'a clean-shaven face with a faint gray shadow along the jaw', "tipo": 'barba', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'barba_pescoco', "en": 'a shaved jaw with gray stubble left growing down the neck', "tipo": 'barba', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'bigode_branco_grosso', "en": 'a thick white mustache', "tipo": 'barba', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'bigode_farto', "en": 'a bushy gray mustache that hides the upper lip', "tipo": 'barba', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'bigode_fino', "en": 'a thin pencil mustache, mostly white', "tipo": 'barba', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'bigode_ferradura', "en": 'a drooping horseshoe mustache, gray at the ends', "tipo": 'barba', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'bigode_amarelado', "en": 'a white mustache yellowed at the center', "tipo": 'barba', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'barba_curta_cinza', "en": 'a short gray beard trimmed close to the jaw', "tipo": 'barba', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'barba_maquina_uniforme', "en": 'a beard clipped to one even short length all over', "tipo": 'barba', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'barba_cheia_branca', "en": 'a full white beard reaching the collar', "tipo": 'barba', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'barba_longa_sem_forma', "en": 'a long gray beard grown out and never shaped', "tipo": 'barba', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'barba_penteada', "en": 'a full silver beard combed smooth and shaped at the edges', "tipo": 'barba', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'barba_quadrada', "en": 'a soft white beard cut square at the chin', "tipo": 'barba', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'barba_falhada', "en": 'a patchy salt-and-pepper beard', "tipo": 'barba', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'barba_arame', "en": 'a wiry gray beard growing unevenly on the cheeks', "tipo": 'barba', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'barba_bochecha_raspada', "en": 'a gray beard shaved clean off the cheeks and left thick along the jaw', "tipo": 'barba', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'queixo_cortina', "en": 'a beard along the jaw and chin with the upper lip shaved clean', "tipo": 'barba', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'cavanhaque', "en": 'a neat gray goatee', "tipo": 'barba', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'cavanhaque_fechado', "en": 'a boxed goatee joined to a mustache, white at the chin', "tipo": 'barba', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'cavanhaque_longo', "en": 'a long gray goatee reaching below the chin', "tipo": 'barba', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'van_dyke', "en": 'a pointed white beard kept separate from the mustache', "tipo": 'barba', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'barba_por_fazer', "en": 'several days of gray stubble', "tipo": 'barba', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'sombra_pesada', "en": "a heavy five o'clock shadow, gray along the jaw", "tipo": 'barba', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'costeletas_longas', "en": 'long gray sideburns and no beard', "tipo": 'barba', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'costeletas_unidas', "en": 'wide sideburns joined to a gray mustache', "tipo": 'barba', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'chin_strap', "en": 'a thin beard trimmed in a strap along the jawline', "tipo": 'barba', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'soul_patch', "en": 'a small white patch of hair under the lower lip', "tipo": 'barba', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'barba_bicolor', "en": 'a close-trimmed beard, dark at the chin and white at the sideburns', "tipo": 'barba', "pele": 'ambas', "sexo": 'homem'},
    {"id": 'barba_ruiva_grisalha', "en": 'a short beard still red at the chin and white at the sides', "tipo": 'barba', "pele": 'branca', "sexo": 'homem'},
    {"id": 'barba_crespa_curta', "en": 'a short beard of tight gray coils along the jaw', "tipo": 'barba', "pele": 'negra', "sexo": 'homem'},
]

# ===========================================================================
# ⭐⭐ O COMPOSITOR DO SUJEITO — 2026-08-23
# ===========================================================================
# Ver o cabecalho dos eixos acima. Aqui a pessoa e' MONTADA, e o resultado
# tem exatamente a forma que o pool antigo tinha, para o resto do motor nao
# precisar saber de nada.
def _sorteia(pool, pele, sexo, rng, tipo=None, hist=(), janela=0):
    """Uma entrada compativel com a pele e o sexo pedidos.

    ⛔ O filtro de PELE e' o mesmo principio da AM12: olho azul e cabelo
    ruivo nao servem a pessoa negra, e tranca e dread nao servem a branca.
    Cada entrada declara onde vale, e aqui so' entram as que valem.
    ⚠️ `janela` liga a memoria curta: as ultimas N escolhas daquele eixo sao
    evitadas, que e' o que impede a mesma cor sair duas vezes seguidas num
    lote — pool grande com sorteio sem memoria repete igual.
    """
    cand = [x for x in pool
            if (tipo is None or x.get("tipo") == tipo)
            and x.get("pele", "ambas") in ("ambas", pele)
            and x.get("sexo", "ambos") in ("ambos", sexo)]
    if not cand:
        return None
    if janela:
        frescos = [x for x in cand if x["id"] not in tuple(hist)[-janela:]]
        cand = frescos or cand
    return rng.choice(cand)


# ⛔⛔ COMPATIBILIDADE ENTRE EIXOS — 2026-08-23, medido na primeira saida.
# Composicao livre produz CONTRADICAO: saiu `half-zip pulled down` numa
# CAMISETA, e `brushed flannel-napped soft napped chamois cloth shirt`, onde
# o padrao e a peca dizem a mesma textura duas vezes. O gerador resolve
# contradicao inventando — a familia de defeito que este motor ja pagou
# cinco vezes esta semana.
# ⭐ A regra e barata e pega quase tudo: se a PECA ja fala daquele assunto,
# o detalhe/padrao daquele assunto nao entra. Peca que ja diz `collar` nao
# recebe detalhe de gola; peca que ja diz `zip` nao recebe fechamento; peca
# que ja nomeia um TECIDO nao recebe padrao de textura.
_ASSUNTO_DETALHE = {
    "gola": ("collar", "neck", "placket", "turtleneck"),
    "manga": ("sleeve", "cuff", "sleeveless"),
    "fechamento": ("zip", "button", "snap", "placket"),
    "bolso": ("pocket",),
}
_TECIDOS = ("flannel", "chamois", "corduroy", "seersucker", "denim",
            "waffle", "fleece", "linen", "canvas", "knit", "cable",
            "madras", "oxford", "chambray", "quilted", "suede")


def _cabe(peca_en, x, familia):
    """A entrada `x` nao repete assunto que a peca ja trouxe."""
    if not x:
        return False
    p = peca_en.lower()
    if familia == "padrao":
        # padrao de TEXTURA nao entra em peca que ja nomeia o tecido
        if any(t in x["en"].lower() for t in _TECIDOS) and                 any(t in p for t in _TECIDOS):
            return False
        return True
    # ⚠️ O `tipo` DECLARADO nao basta — medido: 30 em 300 passavam, porque
    # "with a small notepad in the chest POCKET" vem marcado como
    # `acessorio` e nao como `bolso`. Quem decide e o TEXTO dos dois lados:
    # assunto que aparece nos dois e assunto repetido.
    d = x["en"].lower()
    for palavras in _ASSUNTO_DETALHE.values():
        if any(a in p for a in palavras) and any(a in d for a in palavras):
            return False
    return True


def compor_sujeito(pele, sexo, rng, hist=None):
    """Monta a pessoa sentada a partir dos eixos. Devolve o mesmo dicionario
    que o pool antigo entregava."""
    hist = hist or {}
    _p = "negra" if pele == PELES["negra"] else "branca"
    _s = "homem" if sexo == "homem" else "mulher"

    def pega(pool, tipo=None, chave=None, janela=6):
        x = _sorteia(pool, _p, _s, rng, tipo,
                     hist.get(chave or tipo or "x", []), janela)
        return x or {"id": "-", "en": ""}

    formato = pega(ROSTOS, "formato")
    olhos = pega(OLHOS, None, "olhos")
    nariz = pega(ROSTOS, "nariz")
    boca = pega(ROSTOS, "boca")
    cabelo = pega(CABELOS, "cabelo")
    barba = pega(CABELOS, "barba") if _s == "homem" else {"id": "", "en": ""}
    peca = pega(PECAS, None, "peca")
    cor = pega(CORES_E_PADROES, "cor")

    def compativel(pool, tipo, chave, familia, tentativas=8):
        """Sorteia ate achar um que nao brigue com a peca; desiste vazio.
        ⚠️ Desistir VAZIO e' de proposito: peca sem detalhe le bem, peca com
        detalhe contraditorio nao."""
        for _ in range(tentativas):
            x = pega(pool, tipo, chave)
            if _cabe(peca["en"], x, familia):
                return x
        return {"id": "-", "en": ""}

    padrao = compativel(CORES_E_PADROES, "padrao", "padrao", "padrao")
    detalhe = compativel(DETALHES_ROUPA, None, "detalhe", "detalhe")

    # ⚠️ o `visual` e' cabelo (+ pelo facial): e' o campo que a IMAGE 02 usa
    # para manter a MESMA pessoa depois de emagrecer.
    visual = cabelo["en"]
    if barba.get("en"):
        visual += " and " + barba["en"]

    rosto = ", ".join(x for x in (formato["en"], olhos["en"], nariz["en"],
                                  boca["en"]) if x)
    # ⚠️ `plain` nao entra na frase: "a plain navy blue polo shirt" e' o certo,
    # "a plain plain navy" nao.
    _pad = "" if padrao["id"] in ("plain", "liso", "-") else padrao["en"] + " "
    # ⚠️ DUAS clausulas `with` empilhadas ficam truncadas: a peca ja pode
    # trazer a sua ("shirt WITH a chest pocket") e o detalhe traz outra
    # ("WITH a soft lining at the cuffs"). Emendadas por `and`, viram uma
    # frase que se le; grudadas, viram lista.
    _det = detalhe["en"]
    # ⚠️ O ARTIGO CONCORDA COM O SOM. Medido em 400 sorteios: 19 saiam com
    # `a oatmeal`, `a ecru`, `a ivory`, `a ash`, `a olive` — 5% dos videos com
    # erro de gramatica na primeira linha do prompt. Nasce do compositor, que
    # colava `"a " + cor` sem olhar a cor.
    # ⚠️ Sem excecao de `u`: medido, nenhuma das 88 cores comeca com essa
    # letra, entao a armadilha do `a European` nao existe aqui. Se alguem
    # acrescentar uma, o autoteste acusa.
    _art = "an" if cor["en"][:1].lower() in "aeio" else "a"
    _base = "%s %s %s%s" % (_art, cor["en"], _pad, peca["en"])
    if _det:
        # ⚠️ "with X and with Y" fica truncado; vira "with X and Y".
        if " with " in _base and _det.startswith("with "):
            roupa = _base + " and " + _det[5:]
        else:
            roupa = _base + " " + _det
    else:
        roupa = _base
    roupa = " ".join(roupa.split())

    idade = rng.randint(IDADE_MIN_SUJEITO, 70)
    rot = "%da · %s · %s" % (idade, cabelo["en"][:34],
                                  peca["en"][:30])
    return {"id": "comp_%s_%s_%s_%s" % (cabelo["id"], olhos["id"],
                                        peca["id"], cor["id"]),
            "rotulo": rot, "idade": idade,
            "pele": ("branca", "negra"),
            "rosto": rosto, "visual": visual, "roupa": roupa,
            "_eixos": {"formato": formato["id"], "olhos": olhos["id"],
                       "nariz": nariz["id"], "boca": boca["id"],
                       "cabelo": cabelo["id"], "barba": barba.get("id", ""),
                       "peca": peca["id"], "cor": cor["id"],
                       "padrao": padrao["id"], "detalhe": detalhe["id"]}}


def combinacoes_possiveis(pele="branca", sexo="homem"):
    """Quantas pessoas distintas o compositor consegue montar. E' o numero
    que responde ao *"quase nunca repetir"* — e ele e' MEDIDO, nao prometido.
    """
    def n(pool, tipo=None):
        return len([x for x in pool
                    if (tipo is None or x.get("tipo") == tipo)
                    and x.get("pele", "ambas") in ("ambas", pele)
                    and x.get("sexo", "ambos") in ("ambos", sexo)])
    total = (n(ROSTOS, "formato") * n(OLHOS) * n(ROSTOS, "nariz")
             * n(ROSTOS, "boca") * n(CABELOS, "cabelo")
             * max(1, n(CABELOS, "barba") if sexo == "homem" else 1)
             * n(PECAS) * n(CORES_E_PADROES, "cor")
             * n(CORES_E_PADROES, "padrao") * n(DETALHES_ROUPA))
    return total


# ===========================================================================
# O DAY — escrito pelo Veo, no estilo da fonte
# ===========================================================================
# ⭐ Um estilo por video, IGUAL nos dois takes (comportamento da fonte: o
# estilo nunca muda dentro do mesmo reel — mudar leria como outro video).
ESTILOS_DAY = [
    {"id": "vermelho", "rotulo": "vermelho com contorno branco",
     "desc": "thick bold red block letters with a white outline"},
    {"id": "amarelo", "rotulo": "amarelo com contorno preto",
     "desc": "bold bright yellow block letters with a thin black outline"},
    {"id": "branco", "rotulo": "branco com contorno preto",
     "desc": "bold white block letters with a heavy black outline"},
    {"id": "chip_rosa", "rotulo": "branco em etiqueta rosa",
     "desc": "bold white block letters on a small hot-pink rectangular tag"},
    {"id": "roxo", "rotulo": "branco com brilho roxo",
     "desc": "bold white block letters with a purple outline glow"},
]

# ⛔⛔ O DAY SAIU DO PROMPT EM 2026-08-21 — ordem do operador depois de
# filmar quatro geracoes de cada take: *"remova completamente esse dia 1 e
# dia 50 e poucos do prompt [...] e coloque pro editor conseguir fazer essa
# legenda queimada [...] porque ele tem dificuldade em fixar essa legenda"*.
# ⭐ MEDIDO por ele: em 8 de 8 geracoes de take a legenda DESAPARECIA no
# meio, e em 2 lotes de imagem veio uma TARJA PRETA atras do texto. Nenhuma
# das duas coisas o prompt consegue impedir de forma confiavel.
# ⚠️ Agora TODO quadro nasce LIMPO e a legenda e' queimada pelo Veo Editor,
# fixa e identica do primeiro ao ultimo frame. O `dia2` continua sorteado no
# spec — ele vai para o resumo em PT, para o operador saber o que pedir ao
# editor —, mas nao entra em prompt nenhum.
# ⭐⭐ PROMPT NEGATIVO — pedido literal do operador (2026-08-21): *"coloque
# tambem no mesmo prompt um prompt negativo, o que a imagem NAO deve ter"*.
# ⛔ Nasce de defeito medido, nao de precaucao: ele gerou quatro imagens
# seguidas SEM bigode e SEM o cabelo pedido, com a base anexada.
# ⚠️ E' negacao de DEFEITO (careca, barbeado, texto), nunca de pessoa: dizer
# `not a celebrity` injeta o token, e a ordem de 10/08 baniu isso no parque
# inteiro. Negar `bald` nao tem esse efeito — `bald` nao e' identidade.
# ⛔⛔ O NEGATIVO NAO PODE PROIBIR O QUE O PROMPT PEDE — conserto de 21/08,
# achado ao escrever os sujeitos novos. A linha nascera' com `a bald or
# shaved head` INCONDICIONAL, e dois sujeitos pedem careca com todas as
# letras (`careca` = *a completely bald head*, `calvo_oculos` = *a balding
# head*). Em 25% dos sorteios masculinos o prompt mandava e desmandava na
# mesma frase — a contradicao que o gerador resolve inventando, que e' a
# familia de defeito que este motor ja' pagou tres vezes hoje (a colher
# fantasma, o joinha, a mao subindo).
# ⚠️ Nao da' para simplesmente apagar o item: ele existe porque o gerador
# carecava homens de cabelo descrito. Ele fica — mas SO' quando o sujeito
# nao pediu careca. Quem cobra e' a `AM13`.
def _negativo_img(visual):
    """A lista negativa da IMAGE, ajustada ao sujeito sorteado."""
    itens = []
    if not re.search(r"\b(?:bald|balding|shaved head)\b", visual, re.I):
        itens.append("a bald or shaved head")
    itens += ["a clean-shaven face when facial hair is described",
              "hair or facial hair of a different colour or length than "
              "described", "a different face from the one described",
              "glasses that were not described",
              "any text, caption, number or watermark",
              "a black bar or coloured box behind anything",
              "extra hands, arms or fingers"]
    return "Do NOT include: " + "; ".join(itens) + "."


# ⚠️ Lapide: a versao incondicional fica registrada aqui porque e' ela que
# aparece nos lotes gerados ate' 21/08 — quem for investigar um render
# antigo precisa reconhecer o texto.
NEGATIVO_IMG_ANTIGO = (
    "Do NOT include: a bald or shaved head; a clean-shaven face "
    "when facial hair is described; hair or facial hair of a "
    "different colour or length than described; a different face "
    "from the one described; glasses that were not described; "
    "any text, caption, number or watermark; a black bar or "
    "coloured box behind anything; extra hands, arms or fingers.")

# ===========================================================================
# ⛔⛔ O AR LIMPO — ordem absoluta do operador, 2026-08-23
# ===========================================================================
# *"NUNCA em hipotese alguma faca ter poeira, chuva ou qualquer coisa que
# atrapalhe a filmagem no ambiente. Deve ser um ambiente sem esse tipo de
# coisa voando, caindo, passando, subindo, balancando, etc."*
#
# ⛔⛔ E A POEIRA NAO ERA ACASO: ESTAVA ESCRITA NO MOTOR. Cada cenario tem um
# campo `vida`, criado quando ele mandou parar a carroça de feno — o unico
# movimento autorizado no fundo. Auditado no dia da ordem, 15 dos 21 `vida`
# eram exatamente o que ele acabou de proibir:
#     voando   4  sawdust drifts / dust motes drift (x2) / loose straw stirs
#     subindo  3  steam keeps rising (x3)
#     balanca  7  milho, capim, flor, colcha, vagem, musgo, capim de marisma
#     girando  1  the windmill blades turn slowly
# O vídeo que ele filmou era o `celeiro_novo`, cujo `vida` dizia literalmente
# `sawdust drifts in the sunlight above the lumber stacks`. A serragem nao
# apareceu sozinha: o motor pediu.
#
# ⭐ OS QUATRO QUE FICAM sao animal de solo e gente longe — exatamente o que
# ele liberou por escrito na ordem anterior (*"no maximo pequenos animais de
# solo, plantacoes, ou pessoas bem longe na linha das arvores"*): cavalos,
# galinhas, gansos e a figura distante capinando.
# ⚠️ Os cavalos do `celeiro_bandeira` `swish their tails`, que e' rabo
# balancando. Ficam por pertencerem a familia liberada; a decisao esta'
# declarada aqui para ele reverter numa linha se quiser.
#
# ⛔ A FRASE E' POSITIVA, e isso e' o contrato do arquivo: ela diz que o ar
# esta' LIMPO e nunca lista `no dust, no rain` — negacao injeta o token, que
# e' a familia de defeito que este motor pagou na colher fantasma, no joinha,
# na pessoa sentada da IMAGE 03 e na roupa folgada da IMAGE 02.
AR_LIMPO_IMG = ("THE AIR AND THE GROUND: the air is completely clear and "
                "empty, and the ground is dry and firm. Nothing at all is "
                "in the air anywhere in the picture, and every object in "
                "the background sits perfectly still exactly where it is.")
AR_LIMPO_TK = ("The air stays completely clear and empty for the whole "
               "shot: nothing at all moves through the air at any moment, "
               "and the ground stays dry and firm.")

# ⚰️ APOSENTADO EM 2026-08-23. Era a lista `Do NOT include:` da IMAGE 02, e
# ela era o DEFEITO, nao a defesa: medido em 200 sorteios, punha `loose` 415
# vezes, `hanging` 409 e `oversized` 201 nos prompts — 100% deles — num
# quadro cujo trabalho e' desenhar roupa justa. Fica como lapide; NADA le esta
# constante.
# ⛔⛔ O QUE O OPERADOR BANIU DO AMBIENTE EM 2026-08-23 — ver AR_LIMPO_IMG.
# ⚠️ `\bwind\b` com fronteira de propósito: `windmill` e' um objeto parado e
# nao pode ser acusado por conter as quatro letras.
_RX_ATMOSFERA = re.compile(
    r"\b(dust|sawdust|steam|steaming|smoke|mist|fog|rain|raining|drizzle|"
    r"snow|pollen|drift\w*|sway\w*|stir|stirs|blow\w*|breeze|wind|windy|"
    r"flutter\w*|rustl\w*|rippl\w*|billow\w*|swirl\w*|spin|spins|"
    r"spinning|rotat\w*|turning|splash\w*|spray|muddy)\b", re.I)
# ⛔ e a NEGACAO da atmosfera e' tao proibida quanto a atmosfera
_RX_NEGA_ATMOSFERA = re.compile(
    r"\b(no|without|never|not)\s+(any\s+)?(dust|rain|smoke|steam|mist|fog|"
    r"snow|wind)\b", re.I)
_RX_FOLGA = re.compile(
    r"\b(loose|loosely|roomy|baggy|oversized|billow\w*|slouch\w*|"
    r"untucked|drap\w*|hanging|hangs)\b", re.I)
_RX_NEGA_CORPO = re.compile(
    r"\b(no|without|never|not)\s+(any\s+)?(remaining\s+)?(belly|"
    r"double chin|thick thighs|hanging flesh|fat)\b", re.I)

NEGATIVO_MAGRO_APOSENTADO = ("Do NOT include: a different person; a ""Do NOT include: a different person; a different face; a "
                  "changed hairstyle or facial hair; any remaining belly, "
                  "double chin or thick thighs; oversized clothes hanging "
                  "loose on the body; any text, caption, number or "
                  "watermark; extra hands, arms or fingers.")

_SEM_TEXTO_IMG = ("There is no text, no caption, no lettering, no numbers "
                  "and no watermark anywhere in this image.")
_SEM_TEXTO_TK = ("No text, no caption, no lettering, no numbers and no "
                 "watermark appear at any moment.")


# ===========================================================================
# AS 4 COPIES — verbatim da fonte, renumeradas por uso e views
# ===========================================================================
# ⛔ ALCADA: copy e' do operador. As quatro chegaram prontas na ordem de
# 2026-08-21; a unica variacao permitida e' nome/pronome do sujeito.
# ⚠️ O literal YES e' substituido pela keyword do painel quando o operador
# trocar (substituicao verificada, molde `tirar_bandeira`) — nunca redigitado.
# ⛔⛔ CADA COPY VEM PARTIDA EM DUAS — a divisao e' o unico jeito de a fala
# caber no relogio, e o corte foi escolhido no PONTO NATURAL de respiro de
# cada uma (fim de sentenca), nunca no meio de uma oracao. A soma das duas
# partes e' a copy validada, palavra por palavra: nada foi reescrito.
# ⚠️ Parte 1 vai no TAKE 03 (8s, teto 24) e parte 2 no TAKE 04 (6s, teto 18).
COPIES = [
    {"id": "c1", "rotulo": "1 · resultados (a campea — 8/18, 331k)",
     "usos": 8, "views_max": 331000,
     "pt1": ("Se voce quer saber o que eu dei pra %(pt_obj)s conseguir esses "
             "resultados, comente YES e eu te mando."),
     "pt2": ("Mas me siga e compartilhe este video para que minha mensagem "
             "chegue ate voce."),
     "en1": ("If you wanna know what I gave %(obj)s to get those results, "
             "comment YES and I will send it to you."),
     "en2": ("But follow me and share this video so that my message "
             "reaches you.")},
    {"id": "c2", "rotulo": "2 · colher + receita (2/18, 88k)",
     "usos": 2, "views_max": 88000,
     "pt1": "Uma colher de sopa toda manha antes do cafe. So isso.",
     "pt2": "Comente YES que eu te mando a receita dessa bebida %(pt_receita)s.",
     "en1": "One tablespoon every morning before breakfast. That's it.",
     "en2": ("Comment YES and I will send you this %(receita)s drink recipe.")},
    {"id": "c3", "rotulo": "3 · o segredo do Johnny (1/18, 70k)",
     "usos": 1, "views_max": 70000,
     "pt1": ("Quer saber a bebida secreta que eu acabei de dar pro "
             "%(pt_nome)s pra %(pt_obj)s emagrecer?"),
     "pt2": "E' so' comentar YES que eu te mando.",
     "en1": ("Wanna know the secret drink I just gave %(nome)s to help "
             "%(obj)s lose weight?"),
     "en2": "Just comment YES and I will send it to you."},
    {"id": "c4", "rotulo": "4 · colher + comprar (1/18, 67k)",
     "usos": 1, "views_max": 67000,
     "pt1": "Beba uma colher de sopa toda manha antes do cafe. So isso.",
     "pt2": ("Para comprar, comente YES que eu mando direto pra voce na sua "
             "caixa de entrada."),
     "en1": "Drink one tablespoon every morning before breakfast. That's it.",
     "en2": ("To buy it, comment YES and I will send it straight to your "
             "inbox.")},
]

# ⭐ Copy 3 nomeia o personagem — Johnny e' o da fonte; os outros sao nomes
# rurais US da mesma familia sonora. Nome segue o SEXO do sujeito.
NOMES = {"homem": ["Johnny", "Billy", "Tommy", "Eddie", "Walter", "Harold"],
         "mulher": ["Sally", "Betty", "Peggy", "Mary", "Dorothy", "Hazel"]}


# ===========================================================================
# geometria travada (as tres cenas da fonte, em constantes)
# ===========================================================================
ORIENTACAO = ("Vertical 9:16 portrait orientation, photorealistic smartphone "
              "footage in bright summer daylight, handheld realism.")

_GARRAFA = "a dark amber glass bottle"


def _palavras(t):
    return len(re.findall(r"[A-Za-z0-9'%()\-]+", t or ""))


def _por_id(pool, ident):
    for x in pool:
        if x["id"] == ident:
            return x
    return pool[0]


def _fresco(pool, usados, rng, chave="id"):
    """Sorteia evitando os ids recentes — pool grande sem memoria repete."""
    livres = [x for x in pool if x[chave] not in usados]
    return rng.choice(livres or pool)


# ===========================================================================
# LEDGER
# ===========================================================================
def _carregar_ledger():
    if not os.path.isfile(LEDGER):
        return {}
    try:
        with io.open(LEDGER, encoding="utf-8") as f:
            return json.load(f)
    except Exception:                                    # noqa: BLE001
        return {}


def _gravar_ledger(led, spec):
    for k, v in [("narrador", spec["narrador"]["id"]),
                 ("cenario", spec["cenario"]["id"]),
                 ("sujeito", spec["sujeito"]["id"]),
                 ("copy", spec["copy"]["id"]),
                 ("estilo", spec["estilo"]["id"]),
                 ("cor", spec["cor_vestido"]),
                 ("peso", spec["peso_kg"]),
                 ("dia2", spec["dia2"]),
                 ("sexo", spec["sexo_sujeito"])]:
        led.setdefault(k, []).append(v)
        led[k] = led[k][-40:]
    try:
        with io.open(LEDGER, "w", encoding="utf-8") as f:
            json.dump(led, f, ensure_ascii=False, indent=0)
    except Exception:                                    # noqa: BLE001
        pass


# ===========================================================================
# SORTEIO
# ===========================================================================
def _modulo():
    return sys.modules[__name__]


def _kw():
    """⛔ SEMPRE YES, por ordem (2026-08-21) — nao le' painel nem processo."""
    return "YES"


def _virgular_cta(fala):
    """⭐⭐ A PALAVRA DO CTA ENTRE VIRGULAS — 2026-08-21, ordem dele:
    *"sempre deve conter uma virgula antes e depois da palavra para melhor
    diccao na narracao"*.

    `comment YES and` vira `comment, yes, and`. A virgula e' pausa para o
    TTS do Veo: sem ela a keyword sai colada na frase e o espectador nao
    ouve QUAL palavra digitar — e a palavra e' a automacao inteira.

    ⛔ Roda em CIMA DA FALA, nao no bloco montado, e por isso vale nos dois
    modos: com quatro takes o CTA cai no take 4, com tres cai no take 3.
    Foi essa a condicao dele — *"depende de onde estara' a palavra"*.
    ⚠️ E a caixa vira minuscula, como no exemplo que ele mandou. Nao muda
    o que o espectador digita (a automacao nao diferencia caixa) e nao muda
    a legenda queimada (o editor sobe tudo para maiuscula), mas muda a
    prosodia: `YES` em caixa alta puxa entonacao de grito no TTS.
    """
    kw = _kw()
    novo = re.sub(r"\s*\b%s\b\s*" % re.escape(kw),
                  ", %s, " % kw.lower(), fala, flags=re.I)
    # limpa os encontros que a insercao cria: `, .` -> `.` e `, ,` -> `,`
    novo = re.sub(r",\s*([.,!?;:])", r"\1", novo)
    novo = re.sub(r"\s{2,}", " ", novo).strip()
    return re.sub(r"^,\s*", "", novo)


def _falas(spec):
    c = spec["copy"]
    obj = "him" if spec["sexo_sujeito"] == "homem" else "her"
    pt_obj = "ele" if spec["sexo_sujeito"] == "homem" else "ela"
    # ⭐ a bebida vem do NARRADOR, nao da copy — ver `receita` no pool
    nar = spec["narrador"]
    val = {"obj": obj, "nome": spec["nome"],
           "receita": nar.get("receita", "Amish")}
    val_pt = {"pt_obj": pt_obj, "pt_nome": spec["nome"],
              "pt_receita": nar.get("receita_pt", "Amish")}
    # ⛔ SEM substituicao de keyword: o YES e' cravado por ordem (2026-08-21)
    p1 = c["en1"] % val if "%" in c["en1"] else c["en1"]
    p2 = c["en2"] % val if "%" in c["en2"] else c["en2"]
    spec["fala_pt"] = ((c["pt1"] % val_pt if "%" in c["pt1"] else c["pt1"])
                       + " " + (c["pt2"] % val_pt if "%" in c["pt2"]
                                else c["pt2"]))
    # ⛔ takes 1-2 MUDOS por fidelidade a fonte e por ordem (a musica entra
    # no editor); a fala mora inteira nos takes finais.
    #
    # ⭐⭐ TRES OU QUATRO TAKES, DECIDIDO PELA COPY — 2026-08-21, ordem dele:
    # *"quando eu travar ou sortear as copys 2, 3, 4 sejam geradas somente em
    # 3 takes, pois todas possuem 24 palavras ou menos, e 24 palavras cabem
    # dentro de 8 segundos"*.
    # ⛔ A regra NAO e' `se a copy for a c1`: e' a CONTAGEM contra o teto do
    # take 3. Cravar o id fixaria hoje e mentiria amanha — bastaria ele
    # encurtar a copy 1 no painel para o motor continuar gerando quatro takes
    # sem motivo, ou alongar a copy 3 para cortar a fala em silencio.
    # ⚠️ Medido nas quatro: c1 tem 34 palavras (nao cabe em 8s — TRES das
    # quatro geracoes cortaram na mesma palavra), c2/c3/c4 tem 19/24/23.
    # ⭐ a virgula do CTA entra AQUI, antes da divisao em takes: assim ela
    # acompanha a palavra para onde quer que ela caia
    p1, p2 = _virgular_cta(p1), _virgular_cta(p2)
    inteira = (p1 + " " + p2).strip()
    # ⭐ guarda a copy RESOLVIDA: e' contra ela que a AM2 confere a
    # divisao em takes. Comparar com o TEMPLATE nao serve desde que a
    # bebida virou eixo — `%(receita)s` e' um token e `Native
    # American` sao dois, e a lente acusava 400 videos certos.
    spec["copy_inteira"] = inteira
    if _palavras(inteira) <= TETO_FALA[3]:
        return ["", "", inteira, ""]
    return ["", "", p1, p2]


def sortear(pagina, rng, led, travas=None):
    travas = travas or {}
    hist = led if isinstance(led, dict) else {}
    pele_pag = ETNIA.get(pagina, "white American")
    avisos = []

    nar = (_por_id(NARRADORES, travas["narrador"]) if travas.get("narrador")
           else _fresco(NARRADORES, hist.get("narrador", [])[-4:], rng))

    # pele do narrador: trava > identidade fixa > pagina
    pele_nar = PELES.get(travas.get("pele_narrador", ""), pele_pag)
    if nar["pele_fixa"]:
        if travas.get("pele_narrador"):
            avisos.append("a trava de pele do narrador foi IGNORADA: %r tem "
                          "identidade fixa (%s)"
                          % (nar["id"], nar["pele_fixa"]))
        pele_nar = nar["pele_fixa"]

    sexo = travas.get("sexo_sujeito") or rng.choice(["homem", "mulher"])
    pele_suj = PELES.get(travas.get("pele_sujeito", ""), pele_pag)

    # ⛔⛔ A PELE FILTRA O SUJEITO — 2026-08-21. Ele travou a pele em NEGRA,
    # gerou varios sorteios e o Veo devolveu homem branco: *"a trava de pele
    # negra do sujeito nao esta' funcionando"*.
    # ⛔ A trava CHEGAVA ao prompt — a `AM7` cobrava isso e passava. O que
    # nao chegava era COERENCIA: o pool trazia a coloracao europeia dentro
    # da descricao do rosto, e o prompt saia se contradizendo. No pior caso
    # o placar era 5 a 1 contra a trava (`curly red hair` + `bushy red
    # mustache` + `freckled` + `pale green eyes` + `reddened cheeks` contra
    # um unico `Black American`). O gerador nao ignorou a trava: ele
    # resolveu a contradicao por peso de evidencia, como sempre faz.
    # ⭐ Eixo que ARRASTA outro nao pode ser sorteado como independente —
    # mesma familia da `GO21` do GOOD 16 (cenario que so' existe numa etnia)
    # e do COLO, onde a etnia arrasta o mundo inteiro.
    # ⚠️ Oito sujeitos ficam SO' em branca porque a coloracao E' a
    # identidade deles (os quatro ruivos, a loira, e tres com olhos
    # azuis/verdes). Os outros oito valem nas duas — as frases de compleicao
    # que nomeavam tom europeu (`ruddy`, `pale`, `florid`, `sallow`,
    # `olive`) sairam e viraram arquitetura (`weather-worn skin`, `hollow
    # cheeks`), preservando o rosto e soltando a cor.
    pool_s = SUJEITOS_H if sexo == "homem" else SUJEITOS_M
    _chave = ("negra" if pele_suj == PELES["negra"] else "branca")
    _compat = [x for x in pool_s if _chave in x.get("pele", ("branca",))]
    if travas.get("sujeito"):
        suj = _por_id(pool_s, travas["sujeito"])
        # ⛔ TRAVA DE SUJEITO GANHA DA TRAVA DE PELE, e avisa — mesma regra
        # do narrador de identidade fixa logo acima. O contrario emitiria um
        # prompt que se contradiz, que e' o defeito que estamos consertando.
        if _chave not in suj.get("pele", ("branca",)):
            avisos.append("a trava de pele do sujeito foi IGNORADA: %r so' "
                          "existe em branca (a coloracao e' a identidade "
                          "dele)" % suj["id"])
            pele_suj = PELES["branca"]
    else:
        # ⭐⭐ SORTEIO LIVRE = PESSOA COMPOSTA (23/08). O pool fixo de 46
        # continua existindo so' para a trava de `sujeito` do painel; quem
        # nao trava recebe uma pessoa MONTADA dos eixos, e ai' a variedade
        # deixa de ser 46 e passa a ser o produto dos eixos.
        suj = compor_sujeito(pele_suj, sexo, rng, hist)

    # ⛔⛔ O NARRADOR ARRASTA O CENARIO — 2026-08-21, com as tres
    # identidades novas. A freira num celeiro com bandeira americana le
    # como FANTASIA, nao como vocacao, e vocacao legivel foi o pedido
    # dele. Mesma familia da trava de pele consertada de manha: eixo que
    # ARRASTA outro nao pode ser sorteado como independente.
    # ⚠️ Os nove narradores antigos ficam todos no mundo `amish`, entao
    # o comportamento deles nao muda em nada — medido bit a bit.
    _mundo = nar.get("mundo", "amish")
    _cens = [c for c in CENARIOS if c.get("mundo", "amish") == _mundo]
    if travas.get("cenario"):
        cen = _por_id(CENARIOS, travas["cenario"])
        # ⛔ TRAVA DE NARRADOR GANHA DA TRAVA DE CENARIO, e avisa —
        # mesma regra da pele. O contrario poria a freira na hollow.
        if cen.get("mundo", "amish") != _mundo:
            avisos.append("a trava de cenario foi IGNORADA: %r e do "
                          "mundo %r e o narrador %r vive em %r"
                          % (cen["id"], cen.get("mundo", "amish"),
                             nar["id"], _mundo))
            cen = _fresco(_cens, hist.get("cenario", [])[-5:], rng)
    else:
        cen = _fresco(_cens or CENARIOS,
                      hist.get("cenario", [])[-5:], rng)
    # ⭐ A TRIBO do sujeito sentado — eixo independente do rosto, ver TRIBOS.
    # ⚠️ Janela de frescor de SEIS: com 15 tribos, seis e' o maior valor que
    # ainda deixa qualquer uma cair no proximo sorteio.
    estilo = (_por_id(ESTILOS_DAY, travas["estilo_day"])
              if travas.get("estilo_day")
              else _fresco(ESTILOS_DAY, hist.get("estilo", [])[-2:], rng))
    cor = travas.get("cor_vestido") or rng.choice(
        [c for c in CORES_VESTIDO
         if c not in hist.get("cor", [])[-2:]] or CORES_VESTIDO)

    quer = str(travas.get("copy") or "").strip()
    if quer and quer != "livre":
        copy = COPIES[max(0, min(3, int(quer) - 1))]
    else:
        copy = _fresco(COPIES, hist.get("copy", [])[-2:], rng)

    # ⭐⭐ O PESO DO SUJEITO — ordem do operador (2026-08-21, com dois lotes
    # de imagem na mao): *"a pessoa sentada nao estava com o peso que eu
    # desejo. Sempre deve gerar a pessoa com 200-240 kg em sorteio."*
    # ⛔ `obese` + `enormous belly` rendeu gente so' acima do peso — adjetivo
    # nao pesa. O prompt passa a dizer o NUMERO, e em LIBRAS, que e' a
    # unidade que a fonte queima na tela (`DAY 1 : 350 pounds`) e a que o
    # gerador associa a corpos americanos.
    pesos_livres = [k for k in range(PESO_MIN, PESO_MAX + 1)
                    if k not in hist.get("peso", [])[-6:]]
    peso_kg = rng.choice(pesos_livres or list(range(PESO_MIN, PESO_MAX + 1)))

    # ⛔ DAY 1 fixo; DAY do take 2 sorteado em 47-57 (ordem), com memoria
    dias_livres = [d for d in range(DIA_MIN, DIA_MAX + 1)
                   if d not in hist.get("dia2", [])[-4:]]
    dia2 = rng.choice(dias_livres or list(range(DIA_MIN, DIA_MAX + 1)))

    spec = {
        "pagina": pagina,
        "narrador": nar, "pele_narrador": pele_nar, "cor_vestido": cor,
        "sexo_sujeito": sexo, "pele_sujeito": pele_suj, "sujeito": suj,
        "cenario": cen, "estilo": estilo, "copy": copy,
        "nome": rng.choice(NOMES[sexo]),
        "peso_kg": peso_kg, "peso_lb": int(round(peso_kg * 2.20462 / 10) * 10),
        "dia2": dia2, "avisos": avisos,
    }
    spec["falas"] = _falas(spec)
    return spec


def _refazer_falas(spec, rng):
    spec["falas"] = _falas(spec)


EIXOS_QUE_MEXEM_NA_COPY = {"copy": _refazer_falas}


def nova_fala(spec, i, rng):
    """O botao `trocar` da cena 3 re-sorteia a COPY inteira (sao atomicas)."""
    atual = spec["copy"]["id"]
    spec["copy"] = _fresco([c for c in COPIES if c["id"] != atual], [], rng)
    spec["falas"] = _falas(spec)
    return spec["falas"][i]


# ===========================================================================
# MONTAGEM
# ===========================================================================
def _nar_desc(spec):
    d = spec["narrador"]["desc"] % {"pele": spec["pele_narrador"],
                                    "cor": spec["cor_vestido"]}
    return d


def _suj_desc(spec, magro=False):
    s = spec["sujeito"]
    sexo_en = "man" if spec["sexo_sujeito"] == "homem" else "woman"
    # ⭐ A ROUPA VEM DA TRIBO desde 23/08 — ver o bloco TRIBOS. O campo
    # `roupa` do sujeito fica como reserva para o dia em que alguem sortear
    # sem tribo (ou escrever um sujeito novo antes de a tribo existir).
    # ⚠️ SEM ARTIGO no "the same X": a roupa do pool ja' traz `a `/`an `.
    roupa = re.sub(r"^(a|an)\s+", "", s["roupa"])
    if magro:
        # ⛔⛔ NAO E' UM HOMEM NOVO — E' O MESMO, DEPOIS. Diagnostico do
        # operador em 21/08, e ele estava certo: *"nao e' pra pedir pra
        # transformar completamente o homem sentado SUBSTITUINDO por um homem
        # americano branco de 62 anos [...] porque aqui ele entende que e' pra
        # criar um novo homem. Se trata do MESMO homem"*. O verbo `replace` e
        # a redescricao da pessoa liberavam o gerador a inventar outro rosto —
        # foi o que ele filmou: base com bigode, saida sem bigode.
        # ⭐ Agora a frase e' de CONTINUIDADE, e o unico redescrito e' o CORPO.
        # ⛔⛔ A ROUPA E' A MESMA, EM OUTRO TAMANHO — correcao dele no mesmo
        # dia: *"e' importante manter a consistencia visual da roupa sim [...]
        # porem deve sair de uma roupa XXXG para uma roupa P de acordo com o
        # novo tamanho do corpo, e nao usar a roupa antiga extremamente larga
        # e desproporcional"*. E' o que a fonte faz: nos dois frames do reel
        # de 110k a camisa xadrez e o macacao sao os MESMOS, servindo.
        # ⚠️ A PERNA tem clausula propria porque foi o defeito que ele
        # apontou com o dedo: *"a perna dele nao mudou nada, o grosso dessa
        # perna pra essa daqui esta exatamente igual"*.
        # ⭐⭐ TEXTO APROVADO EM CAMPO — 2026-08-23, palavra por palavra:
        # *"Aprovada:"* seguido do bloco inteiro. Ele nasceu de tres rodadas
        # de variacao (A/B/C) e de tres defeitos que ele filmou, nesta ordem:
        #   1. o corpo continuava gordo e a roupa folgada;
        #   2. a roupa trocava de CORTE (manga curta virava longa, calca
        #      virava short) e so' a cor sobrevivia;
        #   3. a IMAGE 02 herdava a PERNA ABERTA da IMAGE 01.
        #
        # ⛔⛔ A CAUSA DE (1) ESTAVA MEDIDA E ERA NEGACAO. O bloco antigo
        # dizia `no hanging flesh`, `never the huge loose clothes` e a lista
        # `Do NOT include: [...] oversized clothes hanging loose`. Contado em
        # 200 sorteios: `loose` saia 415 vezes, `hanging` 409 e `oversized`
        # 201 — ou seja, 100% dos prompts pediam roupa larga em texto, num
        # quadro cuja base e' um corpo de 840 libras. E' a mesma familia da
        # colher fantasma, do joinha e da pessoa sentada na IMAGE 03.
        # ⭐ Aqui NAO HA UMA NEGACAO sobre o corpo. A magreza e' provada por
        # GEOMETRIA POSITIVA — a cadeira aparecendo inteira em volta dele.
        #
        # ⛔⛔ (2) NAO ERA O PROMPT ESQUECENDO, ERA SILENCIO: medido, a peca
        # de baixo aparecia em 0 de 200 prompts (nem na IMAGE 01 nem na 02) e
        # so' 29 das 85 pecas do compositor declaram comprimento de manga.
        # Nao havia o que manter. Entram `SAME SLEEVE LENGTH` e `SAME LEG
        # LENGTH`, ancoradas ao PONTO DO CORPO (`ending at the same point on
        # his arm as it does in the base image`) — funcionam para manga curta
        # e longa sem nomear nenhuma das duas.
        # ⭐ E a moldura e' o ALFAIATE: `taken in by a tailor to his new
        # size`. Ajuste de alfaiate preserva todo detalhe de desenho e muda
        # so' a quantidade de tecido — e' uma ordem so', em vez de duas
        # brigando. A versao anterior dizia `a DIFFERENT, SMALLER shirt`, e a
        # palavra `DIFFERENT` era a licenca que o gerador usava para
        # redesenhar a peca.
        #
        # ⛔⛔ (3) ERA DEFEITO MEU. A variacao anterior dizia `thighs narrow
        # and separated, with an open gap between them` — eu escrevi isso
        # como PROVA de magreza e o gerador leu como ORDEM DE POSTURA,
        # somada a uma base que ja' vinha de pernas abertas. A prova mudou de
        # endereco para a cadeira; a postura ganhou bloco proprio, com a
        # permissao literal dele: *"nao precisa ser exatamente a mesma
        # postura da imagem 1"*.
        #
        # ⚠️ DUAS GENERALIZACOES MINHAS sobre o texto aprovado, ambas
        # mecanicas e declaradas:
        #   · `the same summer light` -> `the same light`. Quatro dos 21
        #     cenarios sao INTERNOS (despensa, cozinha do convento, cozinha
        #     gullah, despensa apalache) e neles `summer light` e' falso.
        #   · `the same hair` -> a descricao especifica do cabelo/pelo facial
        #     (`s["visual"]`). O generico apagaria a trava de 21/08, que ele
        #     pagou filmando QUATRO geracoes seguidas sem o bigode pedido.
        #     Reverter e' uma linha, se ele preferir o literal.
        lb = 154 if spec["sexo_sujeito"] == "homem" else 121
        _h = sexo_en == "man"
        v = {"e": "he" if _h else "she", "E": "He" if _h else "She",
             "d": "his" if _h else "her", "D": "His" if _h else "Her",
             "o": "him" if _h else "her", "lb": lb, "vis": s["visual"]}
        return ("the same person photographed months later: the same face, "
                "the same %(vis)s, the same skin tone, the same age.\n\n"
                "%(D)s BODY: %(d)s whole body is now lean and athletic at "
                "exactly %(lb)d pounds, slim from head to feet. %(D)s face "
                "is narrow, with a hollow under each cheekbone and a "
                "jawline that reads as one clean line from ear to chin. "
                "%(D)s neck is thin, and the tendons show at the sides of "
                "it. %(D)s shoulders are the widest part of %(o)s; %(d)s "
                "chest is flat and %(d)s waist is clearly narrower than "
                "%(d)s shoulders. %(D)s stomach is flat, so the front of "
                "%(d)s top falls in one straight vertical line from %(d)s "
                "chest down to %(d)s waistband. %(D)s hips are narrow, "
                "%(d)s thighs are narrow, %(d)s knees are bony and clearly "
                "drawn, %(d)s calves are thin and %(d)s ankles are narrow. "
                "%(D)s arms are slim, and the sleeve follows the line of "
                "the arm. %(D)s hands are narrow, with long thin fingers, "
                "the knuckles and the tendons showing on the back of each "
                "hand. The whole wooden chair is in plain view around "
                "%(o)s: the seat shows on both sides of %(d)s hips, and "
                "both back posts show on either side of %(d)s ribs.\n\n"
                "%(D)s POSTURE: %(e)s sits properly and comfortably now, "
                "the way a slim person sits. %(E)s is upright, %(d)s back "
                "straight and resting against the back of the chair, %(d)s "
                "shoulders level and relaxed, %(d)s two knees together and "
                "pointing forward, and both feet flat on the ground side by "
                "side, directly under %(d)s knees. %(D)s posture is neat "
                "and composed, and it does not have to match the posture in "
                "the base image.\n\n"
                "%(D)s CLOTHES: %(e)s is wearing the very same outfit as in "
                "the base image, taken in by a tailor to %(d)s new size. "
                "The only thing that changed about the clothes is how much "
                "fabric there is; every design detail is copied from the "
                "base image exactly. On top, the same garment in the same "
                "colour, the same pattern and the same fabric, with the "
                "same collar or neckline, the same pockets, the same hem, "
                "and the SAME SLEEVE LENGTH, each sleeve ending at the same "
                "point on %(d)s arm as it does in the base image. On the "
                "bottom, the same garment in the same colour and the same "
                "fabric, with the SAME LEG LENGTH, each leg ending at the "
                "same point on %(d)s leg as it does in the base image. "
                "Sleeve length, neckline, pockets, hem and leg length are "
                "identical to the base image. What changed is only the fit: "
                "the shoulder seam sits exactly on the point of %(d)s "
                "shoulder, the top follows the shape of %(d)s chest and "
                "waist, and the lower garment follows the line of %(d)s "
                "thighs." % v)

    # ⭐⭐ A FORMULA SUMO — calibrada em SETE rodadas de teste com o operador.
    # ⛔ A IDENTIDADE VEM ANTES DO CORPO desde 21/08: ele filmou quatro
    # geracoes seguidas SEM bigode e SEM o cabelo pedido, e diagnosticou
    # *"talvez seja muito detalhe aqui"* — o cabelo e o bigode moravam no FIM
    # de uma descricao longa de gordura e perdiam peso. Agora abrem a frase.
    # ⛔ PESO EXATO, sem `around`: *"nao quero que tenha a aproximacao [...]
    # o peso exato no prompt, isso facilita ele ter precisao"*.
    _dele = "his" if sexo_en == "man" else "her"
    # ⭐⭐ A BARRIGA EM DOBRO — carimbada em campo em 21/08: *"esse prompt
    # ficou absurdamente perfeito, registre ele na memoria imediatamente"*.
    # ⛔ A alavanca nova, e a que explica o salto, e' a ANCORA DE QUADRO. Ate'
    # aqui o prompt media a barriga contra o CORPO dele (*passa dos
    # joelhos*), e isso um homem so' grande ja' satisfaz. Medir contra o
    # QUADRO — metade inferior, de borda a borda — nao tem meio-termo,
    # porque e' o mesmo espaco em que o gerador compoe a imagem.
    # ⭐ E a OCLUSAO junto (esconde colo, joelhos e a cadeira): esconder
    # objeto de tamanho conhecido forca volume como adjetivo nenhum forca.
    # ⚠️ As sete rodadas anteriores morreram tentando adjetivo mais forte,
    # camera mais longe e geometria relativa ao proprio corpo. Nenhuma das
    # tres esta' aqui — se alguem for encurtar este bloco um dia, corte a
    # oclusao, nunca a ancora de quadro.
    return ("A %d-year-old %s %s with %s, and %s. This hair and facial hair "
            "must appear exactly as described.%s %s body is that of the very "
            "largest super-heavyweight sumo wrestler in the world, weighing "
            "exactly %d pounds, "
            "sitting upright in a relaxed, normal posture on a small wooden "
            "chair: one gigantic soft round ball of a belly starts at the "
            "chest and hangs all the way down past the knees until it rests "
            "on the ground, and it is by far the largest thing in the "
            "picture — it fills the entire lower half of the frame from the "
            "left edge to the right edge, far wider than %s shoulders and "
            "wider than the whole chair, completely hiding %s lap, %s knees "
            "and almost all of the chair behind it, pointed toward the lens "
            "as the closest "
            "object in the frame; %s %s is stretched drum-tight over the "
            "entire ball and covers all of it, "
            "the hem hanging low below the waistband so the whole belly "
            "stays inside the shirt; upper arms thicker than thighs hanging "
            "with loose soft flesh folding over the elbows, forearms round "
            "and swollen, puffy hands with thick soft fingers, the neck "
            "buried in deep rolls of soft flesh with a triple chin spilling "
            "onto the chest, heavy sagging jowls and round puffed cheeks"
            % (s["idade"], spec["pele_sujeito"], sexo_en, s["visual"],
               s["rosto"],
               # ⭐ o slot vazio que ja existia aqui vira a MASSA de
               # identidade: as marcas da tribo (tatuagem, piercing, oculos,
               # chapeu). Sobe a identidade de 45 para ~85 palavras.
               "",
               "His" if sexo_en == "man" else "Her", spec["peso_lb"],
               _dele, _dele, _dele, _dele, roupa))


def montar(spec):
    cen = spec["cenario"]
    nar = _nar_desc(spec)
    nar_ela = "she" if spec["narrador"]["sexo"] == "f" else "he"
    nar_dela = "her" if spec["narrador"]["sexo"] == "f" else "his"
    suj_en = "man" if spec["sexo_sujeito"] == "homem" else "woman"
    suj_ele = "he" if spec["sexo_sujeito"] == "homem" else "she"
    suj_dele = "his" if spec["sexo_sujeito"] == "homem" else "her"
    # ⛔ PRONOME OBJETO, que faltava: a `MOVIMENTO_T1` dizia
    # *"everything else about HE is frozen"* — ele leu o prompt colado
    # e o erro estava em todo take 1 gerado desde 21/08. `he`/`she` e
    # sujeito; depois de preposicao vai `him`/`her`.
    suj_obj = "him" if spec["sexo_sujeito"] == "homem" else "her"

    # ⛔⛔ AS MAOS DO SENTADO — conserto do defeito mais visivel da gravacao
    # de 21/08: *"do nada aparece uma colher na mao dele"*, em 8 de 8
    # geracoes dos takes 1 e 2. O gerador inventa o objeto porque a cena tem
    # UMA colher e DUAS pessoas, e nada diz de quem ela e'.
    # ⛔ NA IMAGEM: maos vazias, parado. E' descricao de ESTADO.
    # ⚠️ JOELHOS, NAO COXAS — 2026-08-21. O take 2 comecou a ser recusado
    # pela politica e a hipotese do operador foi a coxa: *"acredito que e'
    # referente a citacao de mao na coxa ou algo do tipo"*. A palavra dele e'
    # `joelhos` (*"apenas deixar as maos sobre os joelhos imoveis"*), e a
    # troca custa nada: o gesto e' o mesmo e o token sai.
    # ⛔ Nao e' diagnostico fechado — o take 1 carrega a MESMA clausula de
    # coxa e passou. Ver a nota no `t2` sobre o que mais mudou junto.
    MAOS_SENTADO = ("Both of the seated %s's hands rest empty on %s own "
                    "knees — %s holds nothing, and there is no spoon, cup "
                    "or object of any kind in %s hands. The only spoon in "
                    "the scene is the one held by the narrator."
                    % (suj_en, suj_dele, suj_ele, suj_dele))
    # ⛔⛔ NO TAKE: e' o MOVIMENTO que precisa ser proibido, nao o estado.
    # Defeito filmado pelo operador em 21/08 e conferido quadro a quadro por
    # mim: nos tres primeiros frames as maos estao nas coxas, e no quarto ele
    # JA' ergueu o braco com uma colher amarela — dai em diante come sozinho
    # e a colher da narradora some. A clausula de imagem nao pegava isso: ela
    # descreve um ESTADO, e o gerador leu *"a colher vai a' boca dele"* como
    # *"ele leva a colher a' boca"*. Quem responde a isso e' um verbo negado.
    # ⛔⛔⛔ A NEGACAO ERA O DEFEITO — 2026-08-21, o conserto mais caro do dia.
    # =======================================================================
    # A versao anterior tinha DEZ clausulas negando a colher na mao dele, e a
    # colher continuou nascendo. O operador filmou de novo e eu conferi o
    # frame: aos 0,75s a colher MATERIALIZA na mao PARADA, no colo, com o
    # braco ainda embaixo — a trava de movimento estava sendo OBEDECIDA e o
    # bug acontecia assim mesmo. Logo o alvo estava errado: nao era o
    # movimento, era o OBJETO.
    # ⛔ Medido no prompt reprovado: `spoon` aparecia OITO vezes, e TRES
    # clausulas colavam `colher` em `mao do homem sentado` — todas em
    # negacao. A atencao cruzada encoda o sintagma, nao o `never`. E' o
    # `not a celebrity` aplicado a um objeto: descrever o quadro proibido
    # sete vezes e' pinta'-lo sete vezes.
    # ⭐⭐ O conserto e' POSITIVO e foi escolhido POR TESTE DE CAMPO, nao por
    # gosto: mandei tres variacoes e o operador rodou as seis (21/08).
    #   take 1 -> variacao B: enumerar o UNICO movimento que ele tem;
    #   take 2 -> variacao C: B + as maos com TAREFA + a trava de CONTAGEM.
    # ⛔ A lista `Do NOT show:` inteira SAIU dos dois. Ela era a maior fonte
    # de injecao — e quem cobra que ela nao volte e' a `AM10`.
    #
    # ⭐ VARIACAO B — o take 1. Nada e' negado: diz-se o que ele FAZ, e a
    # enumeracao fecha o resto por exclusao.
    MOVIMENTO_T1 = ("The seated %s's only movement in the entire shot is %s "
                    "mouth opening to receive the spoonful, closing, and %s "
                    "eyes widening; everything else about %s is frozen "
                    "exactly as in the photograph — %s arms, %s hands and %s "
                    "shoulders hold the identical position from the first "
                    "frame to the last. The narrator is the only person in "
                    "the frame whose arms move."
                    % (suj_en, suj_dele, suj_dele, suj_obj, suj_dele,
                       suj_dele, suj_dele))
    # ⭐ VARIACAO C — o take 2. As maos GANHAM TAREFA (agarrar as rotulas):
    # mao ocupada e' incompativel com mao segurando colher, e a frase nao
    # precisa dizer `colher` para isso. Fecha com a trava de CONTAGEM, que
    # e' a unica mencao a colher que sobra do lado dele — e ela e'
    # afirmativa: existe UMA, e ela esta' com o narrador.
    MOVIMENTO_T2 = ("The seated %s keeps both hands closed around %s own "
                    "kneecaps, fingers curled over the front of each knee, "
                    "gripping them steadily, and %s arms stay locked in that "
                    "exact position from the first frame to the last. %s "
                    "only movement in the entire shot is %s mouth opening to "
                    "receive the spoonful, closing, and %s eyes widening. "
                    "The narrator is the only person in the frame who moves: "
                    "%s arm reaches in from the side and does all of the "
                    "feeding, and %s is the only hand that ever comes near "
                    "%s face. Exactly one spoon exists in this scene from "
                    "beginning to end, and it stays in the narrator's "
                    "fingers the whole time."
                    % (suj_en, suj_dele, suj_dele, suj_dele.capitalize(),
                       suj_dele, suj_dele, nar_dela,
                       "hers" if spec["narrador"]["sexo"] == "f" else "his",
                       suj_dele))
    # ⛔⛔ A GARRAFA NA MAO — *"ela soltou a garrafa [...] do nada a garrafa
    # vai aparecer de novo, esse bug visual nao pode acontecer"*.
    _GARRAFA_DEF = _GARRAFA.replace("a dark", "the dark", 1)
    # ⛔ SUJEITO EXPLICITO, nunca pronome. A versao anterior abria com
    # `He keeps...` logo depois de duas frases sobre o homem SENTADO — e o
    # `He` mais proximo e' ele, nao o narrador. Pronome ambiguo num prompt
    # nao e' estilo: e' o gerador escolhendo por conta, que e' a familia de
    # defeito que esta cena ja' pagou com a colher fantasma.
    GARRAFA_TRAVADA = ("The narrator keeps %s gripped in the same hand for "
                       "the entire shot: it never leaves the narrator's "
                       "hand, never disappears and never reappears, and it "
                       "stays visible in frame from the first frame to the "
                       "last." % _GARRAFA_DEF)
    # ⚠️ Nos takes 1-2 o narrador tem DUAS maos ocupadas — uma alimenta, a
    # outra segura a garrafa — e a frase precisa dizer QUAL, senao o gerador
    # e' quem escolhe. Nos takes 3-4 nao existe mao que alimenta, e dizer
    # `the other hand` la' inventaria uma segunda tarefa que a cena nao tem.
    GARRAFA_ALIMENTA = GARRAFA_TRAVADA.replace(
        "in the same hand", "in %s other hand" % nar_dela, 1)
    # ⛔⛔ SO' ENGOLE, NAO MASTIGA — 2026-08-22, filmado por ele: *"a
    # pessoa do antes e depois esta mastigando apos receber a colherada.
    # Nao e' solido para mastigar"*. Conferido quadro a quadro: nos oito
    # primeiros frames a colher entra certo, e nos oito seguintes a
    # mandibula trabalha por dois segundos inteiros.
    # ⛔ A trava e' POSITIVA e nao diz `chew` uma vez. Escrever *"does not
    # chew"* poria a mastigacao no prompt — e' a licao que este motor pagou
    # tres vezes ontem (a colher fantasma nasceu de dez clausulas negando
    # colher). Aqui se descreve o LIQUIDO e o gesto UNICO que ele permite:
    # o que e' liquido nao tem como ser mastigado.
    ENGOLIR = ("The dark syrup is a thin liquid, like cough syrup: the "
               "seated %s closes %s lips around the spoon once, takes it "
               "down in a SINGLE swallow with one movement of %s throat, "
               "and %s jaw and lips stay still and closed from that moment "
               "on. The spoon comes straight back out of frame in the "
               "narrator's hand."
               % (suj_en, suj_dele, suj_dele, suj_dele))
    # ⛔ MAO FANTASMA — *"com uma mao que nao existe, mao fantasma"*.
    DUAS_MAOS = ("Exactly two hands are visible in the whole frame and both "
                 "belong to the narrator; no extra hand, arm or finger "
                 "appears at any moment.")

    # ⛔⛔ O FUNDO PARADO — 2026-08-21, a carroca em looping.
    # =======================================================================
    # O `vida` do cenario entra nos QUATRO takes. Enquanto ele era um verbo
    # de travessia, o mesmo objeto atravessava o quadro quatro vezes: no
    # take 1, de novo no take 2 (47 dias depois) e mais duas no 3 e no 4,
    # que saem da MESMA imagem. *"A carroca ja' deveria ter passado."*
    # ⭐ A trava e' POSITIVA e nao nomeia nenhum veiculo: dizer *"no wagon
    # crossing"* injetaria a carroca no prompt — a licao do `not a
    # celebrity`, paga em 30 motores. Aqui o `vida` sorteado e' declarado o
    # UNICO movimento permitido, e tudo o mais fica onde esta'. O que nao e'
    # nomeado nao e' desenhado.
    def _fundo_parado(vida):
        # ⚠️ E a clausula nao lista substantivos (`wagon`, `cart`, `buggy`)
        # nem para mandar parar: o que se escreve, o gerador desenha.
        # ⚠️ E sem pronome: a versao anterior dizia *"anywhere behind THEM"*,
        # e nos takes 3 e 4 so' a narradora esta' em quadro — `them` sem
        # referente e' a mesma familia de defeito da garrafa (`He keeps...`
        # lido como o homem sentado).
        # ⛔⛔ SEM `vida` O FUNDO E' PEDRA — ver o bloco AR_LIMPO. Quinze dos
        # 21 cenarios perderam o campo na ordem de 23/08, e sem este ramo a
        # frase sairia como *"the only movement is this — ."*, que e' um
        # predicado vazio: o gerador preenche o que falta.
        v = (vida or "").strip().rstrip(".")
        if not v:
            return ("The background holds perfectly still: nothing in the "
                    "background moves at all, everything stays exactly "
                    "where it is from the first frame to the last, and "
                    "nothing travels across the frame. " + AR_LIMPO_TK)
        return ("The background holds perfectly still: the only movement "
                "anywhere in the background is this, and nothing else moves "
                "at all — %s. Everything else in the background stays "
                "exactly where it is from the first frame to the last, and "
                "nothing travels across the frame. %s" % (v, AR_LIMPO_TK))

    # ⛔⛔ SEM BLOCO 0 (REF) — ordem de 21/08: a IMAGE 01 e' a unica descricao
    # completa e as IMAGEs 02/03 sao instrucoes de EDICAO sobre ela.
    # ⭐ O SUJEITO ABRE O PROMPT — foi parte do que destravou a massa nas
    # sete rodadas de teste; o cenario desceu para o fim.
    _suj = _suj_desc(spec)
    _suj = _suj[0].upper() + _suj[1:]
    b1 = ("%s %s. The small wooden chair has completely vanished under the "
          "seated %s. Standing at the side, small next to the seated %s, "
          "%s holds %s in one hand and lifts a spoonful of dark syrup "
          "toward the seated %s's wide-open mouth with the other. %s They "
          "are %s %s"
          % (ORIENTACAO, _suj, suj_en, suj_en, nar, _GARRAFA, suj_en,
             MAOS_SENTADO, cen["desc"] + ". " + AR_LIMPO_IMG,
             _SEM_TEXTO_IMG + " "
             + _negativo_img(spec["sujeito"]["visual"])))

    # ⭐ VARIACAO B, escolhida em campo pelo operador (21/08): *"a variacao B
    # foi a que melhor funcionou no take 1"*. Ver o bloco do `MOVIMENTO_T1`.
    # ⚠️ `the narrator's HAND slides` — a mao e' nomeada como sujeito da
    # acao. Faz parte da variacao testada; nao trocar por `the narrator`.
    t1 = ("Animate the provided image exactly as it is. Within the first "
          "second the narrator's hand slides the spoonful into the seated "
          "%s's mouth; %s swallows, %s eyes going wide at the taste, and the "
          "narrator nods once, pleased. %s %s %s %s Camera: static "
          "handheld with a barely visible sway. Audio: completely silent — "
          "no sound at all, no ambience, no music, no wind, no voice."
          % (suj_en, suj_ele, suj_dele, MOVIMENTO_T1 + " " + ENGOLIR,
             GARRAFA_ALIMENTA,
             _fundo_parado(cen["vida"]), _SEM_TEXTO_TK))

    b2 = ("Using the provided image as the base. Same location, the same "
          "light, same framing, same wooden chair, and the same narrator "
          "standing at the side in the same clothes, holding the same dark "
          "amber glass bottle and lifting another spoonful of dark syrup. "
          "The person on the chair is %s\n\n%s\n\n%s %s"
          % (_suj_desc(spec, magro=True), AR_LIMPO_IMG, MAOS_SENTADO,
             _SEM_TEXTO_IMG))

    # ⛔⛔ O JOINHA CAIU — 2026-08-21, recusa de politica no take 2.
    # =======================================================================
    # Ordem do operador, com a recusa na mao: *"o homem nunca deve fazer
    # sinal de joinha ou positivo, apenas deixar as maos sobre os joelhos
    # imoveis"*.
    # ⚠️ TRES COISAS MUDARAM DE UMA VEZ, e isso e' declarado de proposito
    # porque o RUNBOOK-bisseccao-moderacao manda isolar UMA variavel:
    #   1. o joinha saiu           — ordem direta, nao e' teste;
    #   2. `thighs` -> `knees`     — hipotese DELE, e a palavra que ele usou;
    #   3. `lips`   -> `mouth`     — hipotese MINHA.
    # ⛔ A (2) sozinha explica mal a recusa: o take 1 carrega a MESMA
    # clausula de coxa e passa. O que o take 2 tinha de exclusivo era
    # `lips` + `thumbs-up` + `grinning` + uma mao subindo — e o take 1, que
    # passa, diz `mouth`. Por isso a (3) entrou junto.
    # ⚠️ Se voltar a ser recusado, o proximo suspeito nao e' mais a mao: e'
    # a colherada na boca de um adulto por outro adulto, que e' a unica
    # coisa que sobra em comum entre os dois takes.
    # ⭐ VARIACAO C, escolhida em campo pelo operador (21/08): *"a variacao C
    # foi a que melhor funcionou no take 2"*. Ver o bloco do `MOVIMENTO_T2`.
    # ⚠️ E' a variacao MAIS PESADA das tres, e ela ganhou justamente no take
    # que tambem apanhava da moderacao — as maos com tarefa fecham as duas
    # frentes de uma vez: mao ocupada nao segura colher e nao fica pousada
    # sobre a propria perna.
    t2 = ("Animate the provided image exactly as it is. Within the first "
          "second the narrator's hand brings the spoonful to the seated "
          "%s's mouth and %s swallows, %s eyes going wide at the taste, "
          "while the narrator smiles, pleased. %s %s %s %s Camera: "
          "static handheld with a barely visible sway. Audio: completely "
          "silent — no sound at all, no ambience, no music, no wind, no "
          "voice."
          % (suj_en, suj_ele, suj_dele, MOVIMENTO_T2 + " " + ENGOLIR,
             GARRAFA_ALIMENTA, _fundo_parado(cen["vida"]),
             _SEM_TEXTO_TK))

    # ⛔⛔ QUEM E O NARRADOR, DITO COM TODAS AS LETRAS — 2026-08-23.
    # Ele copiou a IMAGE 03 e o gerador devolveu, em 3 de 4, o SUJEITO
    # SENTADO no lugar da narradora (a mulher de chapeu de palha e camisa
    # xadrez vermelha com duas trancas e o `country_trancas`, nao a vovo
    # Amish): *"muitas vezes o Veo esta gerando a pessoa que esta sentada
    # como referencia na imagem 3, quando deve ser sempre a pessoa em pe"*.
    # ⛔ A causa: a IMAGE 03 dizia `Keep the same narrator` e NUNCA DEFINIA
    # quem era o narrador. A base tem DUAS pessoas, e o unico desempate era
    # uma NEGACAO (`the seated person is no longer in frame`) — que e
    # justamente a construcao que nao segura, como este motor ja pagou tres
    # vezes esta semana.
    # ⭐ O conserto e POSITIVO e tem tres camadas, da mais forte para a mais
    # fraca: (1) a POSICAO na base (`the one who was STANDING`), que e a
    # unica coisa que separa as duas sem ambiguidade; (2) a DESCRICAO
    # INTEIRA dela repetida aqui — idade, roupa, rosto —, que e o mesmo
    # texto da IMAGE 01 e nao deixa margem; (3) a contagem (`the only
    # person in this image`).
    # ⚠️ E a negacao antiga SAIU: dizer `the seated person` reinjetava a
    # pessoa sentada no prompt em que ela nao pode aparecer.
    b3 = ("Using the provided image as the base. This image keeps ONLY the "
          "person who was STANDING at the side in the base image — %s — and "
          "she is the only person in this image. Keep her exact face, her "
          "exact clothes and the same light, and the same "
          "location, but reframe as a selfie: she now fills the "
          "lower half of the frame, face close to the lens, looking "
          "straight into it, %s visible behind %s. %s holds %s raised in "
          "front of %s chest, the label clearly visible, the bottle fully "
          "inside the frame. %s"
          % (nar, cen["curto"], nar_dela, nar_ela.capitalize(), _GARRAFA,
             nar_dela, AR_LIMPO_IMG + " " + _SEM_TEXTO_IMG + " "
             + _negativo_img(spec["sujeito"]["visual"])))
    # ⚠️ `she`/`her` viram `he`/`his` quando o narrador e homem — cinco dos
    # nove sao. Sem isto a vovo Amish HOMEM sairia descrita no feminino.
    if spec["narrador"]["sexo"] == "m":
        b3 = (b3.replace(" and she is the only", " and he is the only")
                .replace("Keep her exact face, her exact clothes",
                         "Keep his exact face, his exact clothes")
                .replace("but reframe as a selfie: she now fills",
                         "but reframe as a selfie: he now fills"))

    _voz = spec["narrador"]["voz"]
    # ⭐⭐ O TAKE 3 SABE SE E' O ULTIMO — 2026-08-21. Com as copies 2/3/4 nao
    # existe take 4, e o gesto de erguer a garrafa (que fecha o video) tem de
    # voltar para ca'. Sem isso, o lote de tres takes terminaria sem o beat
    # final e ninguem veria — o prompt do take 3 nao mudaria de aparencia.
    _ultimo = not spec["falas"][3]
    _fecho = ("In the final two seconds %s raises the bottle closer to the "
              "lens until it fills part of the frame. " % nar_ela
              if _ultimo else "")
    t3 = ("Animate the provided image exactly as it is. The narrator speaks "
          "straight into the lens at a brisk, natural conversational pace, "
          "with small head movements, warm and direct like a video call. "
          "%s%s %s %s %s Camera: selfie held at arm's length, slight handheld "
          "sway. Audio: only the narrator's voice — %s — with no music and "
          "no background sound.\n"
          'Dialogue: "%s"'
          % (_fecho, GARRAFA_TRAVADA, DUAS_MAOS, _fundo_parado(cen["vida"]),
             _SEM_TEXTO_TK, _voz, sonorizar(spec["falas"][2])))

    # ⭐⭐ TAKE 04 — anima a MESMA IMAGE 03, continuando a fala do take 3.
    # ⛔ O gesto de erguer a garrafa mudou de casa: ele era o fecho do take 3
    # e agora fecha o take 4, que e' o ultimo frame do video.
    # ⚠️ O OPERADOR CONTOU AS IMAGENS E ACHOU QUE FALTAVA UMA (21/08):
    # *"so' esta' gerando 3 imagens [...] imagino que e' pra gerar o take do
    # CTA parte 1 e parte 2 tudo com a imagem 3"*. Era, sim — mas o bloco
    # nao dizia, e contrato que so' existe na minha cabeca e' contrato que o
    # operador descobre errando. Agora ele diz na primeira linha.
    t4 = ("(Use the SAME IMAGE 03/03 as the base for this take — there is no "
          "separate image 04.) Animate the provided image exactly as it is. "
          "This is the direct "
          "continuation of the previous shot: the same narrator, same "
          "selfie framing, same light, still speaking straight into the "
          "lens at a brisk, natural conversational pace. In the final two "
          "seconds %s raises the bottle closer to the lens until it fills "
          "part of the frame. %s %s %s %s Camera: selfie held at arm's "
          "length, slight handheld sway. Audio: only the narrator's voice "
          "— %s — with no music and no background sound.\n"
          'Dialogue: "%s"'
          % (nar_ela, GARRAFA_TRAVADA, DUAS_MAOS,
             _fundo_parado(cen["vida"]), _SEM_TEXTO_TK, _voz,
             sonorizar(spec["falas"][3])))

    # ⭐ Os rotulos vem de `takes_do(spec)`: com tres takes eles saem
    # `TAKE 01/03`..`TAKE 03/03`, e o take 4 nem e' montado.
    _tk = takes_do(spec)
    blocos = {
        IMAGENS[0]: b1, _tk[0]: t1,
        IMAGENS[1]: b2, _tk[1]: t2,
        IMAGENS[2]: b3, _tk[2]: t3,
    }
    if len(_tk) == 4:
        blocos[_tk[3]] = t4
    blocos = sc.selar_tags(blocos)
    # ⛔ SEM `sc.selar_takes` — de proposito, e e' o unico motor do parque
    # assim. A clausula propria `_SEM_TEXTO_TK` ja' esta' em TODOS os quatro
    # takes e cobre mais que a compartilhada (numeros e lettering, que sao
    # justamente o que o DAY deixou de ser). Somar as duas poria duas travas
    # dizendo a mesma coisa em palavras diferentes: dilui o prompt e as duas
    # envelhecem separadas.
    return blocos


# ===========================================================================
# LENTES
# ===========================================================================
def _am1_limpo(spec, blocos, ach):
    """⭐⭐ AM1 — NENHUM texto em quadro nenhum. O DAY e' do EDITOR.

    ⛔ Ordem de 2026-08-21, depois de o operador filmar oito geracoes: a
    legenda DESAPARECIA no meio do take em 8 de 8, e dois lotes de imagem
    vieram com TARJA PRETA atras do texto. *"Remova completamente esse dia 1
    e dia 50 e poucos do prompt [...] coloque pro editor conseguir fazer essa
    legenda queimada"*. Prompt nao consegue fixar texto; o ffmpeg consegue.
    ⚠️ A lente inverteu de sinal: antes EXIGIA o caption, agora o PROIBE."""
    for nome in list(IMAGENS) + list(TAKES):
        txt = blocos.get(nome, "")
        if '"DAY' in txt or "caption reading" in txt:
            ach.append(("ERRO", "AM1: %s pede legenda ao gerador — o DAY sai "
                                "no editor desde 21/08" % nome))
    for nome in IMAGENS:
        if "no text, no caption" not in blocos.get(nome, "").lower():
            ach.append(("ERRO", "AM1: %s sem a trava de quadro limpo — sem "
                                "ela vem texto inventado e tarja preta"
                        % nome))
    for nome in takes_do(spec):
        if "no text, no caption" not in blocos.get(nome, "").lower():
            ach.append(("ERRO", "AM1: %s sem a trava de quadro limpo" % nome))
    if not (DIA_MIN <= spec["dia2"] <= DIA_MAX):
        ach.append(("ERRO", "AM1: dia2=%r fora de %d-%d — o numero vai para o "
                            "editor, mas continua sendo sorteado aqui"
                    % (spec["dia2"], DIA_MIN, DIA_MAX)))


def _am2_copy(spec, blocos, ach):
    """⛔⛔ AM2 — as DUAS partes da copy chegam VERBATIM, uma por take.

    ⭐ E a soma delas tem de ser a copy validada inteira: partir a fala em
    dois takes nao pode virar desculpa para reescrever meia frase.
    ⚠️ Com TRES takes (copies 2/3/4, desde 21/08) nao ha' parte 2: a copy
    inteira mora no take 3 e a lente cobra so' ele. O que NAO muda e' a
    soma — em qualquer dos dois modos ela tem de bater com a copy validada.
    """
    _tk = takes_do(spec)
    pares = [(2, _tk[2])] + ([(3, _tk[3])] if len(_tk) == 4 else [])
    for i, take in pares:
        alvo = 'Dialogue: "%s"' % sonorizar(spec["falas"][i])
        if alvo not in blocos.get(take, ""):
            ach.append(("ERRO", "AM2: a parte %d da copy %r nao chegou "
                                "intacta ao %s — copy validada nao se "
                                "reescreve no caminho"
                        % (i - 1, spec["copy"]["id"], take)))
    if spec["falas"][0] or spec["falas"][1]:
        ach.append(("ERRO", "AM2: fala nos takes 1-2 — eles sao MUDOS"))
    inteira = (spec["falas"][2] + " " + spec["falas"][3]).strip()
    # ⛔ a soma das partes tem de ser a copy inteira, CARACTERE por
    # caractere — e' o que impede a divisao em takes de perder ou reescrever
    # um pedaco. A referencia e' a copy ja' RESOLVIDA (`copy_inteira`), nao
    # o template: desde 22/08 a bebida e' um eixo, e contar palavra do
    # template acusava 400 videos certos.
    c = spec["copy"]
    ref = spec.get("copy_inteira")
    if ref is not None and inteira != ref:
        ach.append(("ERRO", "AM2: a copy %r montada nao bate com a copy "
                            "inteira — a divisao em takes mexeu no texto"
                    % c["id"]))
    kw = _kw()
    # ⚠️ `,?\s*` no meio: desde 21/08 a palavra do CTA sai entre virgulas
    # (*"sempre deve conter uma virgula antes e depois [...] para melhor
    # diccao"*), e a versao antiga do regex passou a acusar 400 de 400
    # videos CERTOS. Lente colada na pontuacao envelhece na primeira vez
    # que a pontuacao muda — e aqui ela mudou por ordem.
    if len(re.findall(r"\bcomment,?\s*%s\b" % re.escape(kw), inteira,
                      re.IGNORECASE)) != 1:
        ach.append(("ERRO", "AM2: a copy inteira nao tem exatamente um "
                            "`comment %s`" % kw))
    # ⛔⛔ E A VIRGULA E' COBRADA: antes E depois da palavra, onde quer que
    # ela caia. Sem lente, a proxima edicao de copy tira a pausa e ninguem
    # ve' — o defeito so' aparece no audio do render.
    for m in re.finditer(r"\b%s\b" % re.escape(kw), inteira, re.IGNORECASE):
        antes = inteira[:m.start()].rstrip()
        depois = inteira[m.end():].lstrip()
        if not antes.endswith(",") or not depois.startswith(","):
            ach.append(("ERRO", "AM2: a palavra do CTA (%s) sem virgula dos "
                                "dois lados em %r — a virgula e' a pausa que "
                                "faz o espectador ouvir QUAL palavra digitar"
                        % (kw, inteira[max(0, m.start() - 18):m.end() + 8])))
    # ⛔ o teto e' POR TAKE, e o relogio de cada um e' diferente
    for i, n in ((2, 3), (3, 4)):
        if i >= len(_tk):
            continue
        p = _palavras(spec["falas"][i])
        if p > TETO_FALA[n]:
            ach.append(("ERRO", "AM2: a parte %d tem %d palavras e o TAKE 0%d "
                                "e' de %ds (teto %d) — foi assim que a COPY 1 "
                                "cortou em 3 de 4 geracoes"
                        % (i - 1, p, n, SEGUNDOS_TAKE[n], TETO_FALA[n])))


def _am4_mudez(spec, blocos, ach):
    """⛔ AM4 — os dois lados da excecao de texto deste motor."""
    _tk = takes_do(spec)
    for nome in _tk[:2]:
        t = blocos.get(nome, "")
        if "Dialogue:" in t:
            ach.append(("ERRO", "AM4: %s com Dialogue — os takes 1-2 sao "
                                "mudos" % nome))
        if sc.SEM_TEXTO_TAKE in t:
            ach.append(("ERRO", "AM4: %s com a trava de sem-texto — ela "
                                "mataria o DAY que o Veo tem de escrever"
                        % nome))
        if "completely silent — no sound at all" not in t:
            ach.append(("ERRO", "AM4: %s sem a clausula de SILENCIO TOTAL — "
                                "ordem de 21/08: a musica entra no editor, o "
                                "take nasce mudo" % nome))
    # ⚠️ A trava de texto dos takes de FALA e' a propria (`_SEM_TEXTO_TK`),
    # cobrada pela AM1 em todos os quatro. A compartilhada saiu para nao
    # haver duas dizendo o mesmo.
    # ⚠️ `_tk[2:]` e nao `(TAKES[2], TAKES[3])`: com tres takes o video
    # tem UM take de fala, e cobrar um quarto acusaria o certo.
    for nome in _tk[2:]:
        if "Dialogue:" not in blocos.get(nome, ""):
            ach.append(("ERRO", "AM4: %s sem linha Dialogue — os takes "
                                "de selfie sao os que falam" % nome))


def _am5_pronome(spec, blocos, ach):
    """⛔ AM5 — pronome e nome seguem o SEXO do sujeito (a unica variacao)."""
    fala = spec["falas"][2]
    cid = spec["copy"]["id"]
    if cid in ("c1", "c3"):
        errado = r"\bher\b" if spec["sexo_sujeito"] == "homem" else \
                 r"\b(him|his)\b"
        if re.search(errado, fala):
            ach.append(("ERRO", "AM5: pronome do sexo errado na copy %s "
                                "(sujeito=%s)" % (cid, spec["sexo_sujeito"])))
    if cid == "c3" and spec["nome"] not in NOMES[spec["sexo_sujeito"]]:
        ach.append(("ERRO", "AM5: nome %r fora do pool do sexo %s"
                    % (spec["nome"], spec["sexo_sujeito"])))


def _am6_garrafa(spec, blocos, ach):
    """⭐ AM6 — a garrafa ambar atravessa os tres takes (e' a assinatura)."""
    for nome in tuple(IMAGENS) + takes_do(spec):
        if "amber" not in blocos.get(nome, "").lower():
            ach.append(("ERRO", "AM6: %s sem a garrafa ambar" % nome))


def _am9_peso(spec, blocos, ach):
    """⭐⭐ AM9 — a FORMULA SUMO chega inteira a IMAGE 01.

    Calibrada em sete rodadas de geracao real com o operador (21/08). As
    ancoras cobradas sao as que MOVERAM o corpo nos testes; perder qualquer
    uma e' voltar ao fazendeiro rechonchudo que ele reprovou seis vezes."""
    b1 = blocos.get(IMAGENS[0], "")
    for alvo, motivo in [
            ("the very largest super-heavyweight sumo wrestler in the world",
             "o token de silhueta, no grau que ele carimbou em 21/08"),
            # ⭐⭐ AS DUAS ANCORAS DA BARRIGA EM DOBRO (21/08). A de QUADRO e'
            # a que explica o salto: medir contra a moldura em vez de contra
            # o proprio corpo. Sem lente, ela e' a primeira coisa que um
            # refactor de encurtamento apaga.
            ("fills the entire lower half of the frame",
             "a ancora de QUADRO — sete rodadas mediram contra o corpo dele "
             "e nenhuma funcionou"),
            ("until it rests on the ground",
             "ate' onde a barriga desce; `past the knees` um homem so' "
             "grande ja' satisfaz"),
            ("completely hiding",
             "a OCLUSAO: esconder objeto de tamanho conhecido forca volume"),
            ("exactly %d pounds" % spec["peso_lb"],
             "peso EXATO — `around` foi vetado em 21/08 (*\"nao quero a "
             "aproximacao\"*)"),
            ("must appear exactly as described",
             "a identidade abre a frase; no fim de uma lista de gordura ela "
             "perdia peso e saiam 4 geracoes sem bigode"),
            # ⛔⛔ REVERTIDO EM 21/08: era `small strip of bare belly`, e o
            # operador viu o resultado e mandou o oposto — *"para a imagem 1
            # a barriga nunca estar para fora da camisa"*. A faixa de pele
            # que a versao anterior PEDIA saiu; a camisa cobre a bola
            # inteira. A lente vira ao contrario junto: cobra a cobertura e
            # proibe a faixa nua, senao a ordem antiga volta num refactor.
            ("the whole belly stays inside the shirt",
             "a camisa cobre a barriga INTEIRA (ordem de 21/08, revertendo "
             "a faixa de pele que a versao anterior pedia)"),
            ("sitting upright in a relaxed, normal posture",
             "sem a pose de quem passa mal (ordem final)"),
            ("closest object in the frame",
             "a barriga apontada para a lente e' o truque de perspectiva")]:
        if alvo not in b1:
            ach.append(("ERRO", "AM9: IMAGE 01 sem %r — %s" % (alvo, motivo)))
    # ⛔ e a faixa de pele nao pode VOLTAR: e' a ordem de 21/08 ao contrario
    if re.search(r"bare belly|belly shows|strip of bare", b1, re.I):
        ach.append(("ERRO", "AM9: IMAGE 01 pedindo pele nua na barriga — o "
                            "operador mandou a camisa cobrir tudo em 21/08"))
    # ⛔ a palavra explicita e' o token de politica — nunca em bloco nenhum
    for nome, txt in blocos.items():
        if re.search(r"\bobese\b|\bobesity\b|\bfat\b", txt, re.I):
            ach.append(("ERRO", "AM9: %s com palavra explicita de condicao "
                                "— o numero informa, a palavra viola" % nome))
    if not (PESO_MIN <= spec["peso_kg"] <= PESO_MAX):
        ach.append(("ERRO", "AM9: peso %r fora de %d-%d kg"
                    % (spec["peso_kg"], PESO_MIN, PESO_MAX)))


def _am10_bugs(spec, blocos, ach):
    """⭐⭐ AM10 — as tres travas de BUG filmadas pelo operador em 21/08.

    Cada uma nasceu de um defeito visto em geracao real, nao de suposicao:
      · a COLHER FANTASMA na mao do sentado — 8 de 8 takes;
      · a GARRAFA que a narradora SOLTA e que reaparece do nada;
      · a MAO FANTASMA no take do CTA.
    ⛔ Clausula sem lente e' forma sem funcao: some no proximo refactor e
    ninguem percebe ate' o lote sair errado."""
    for nome in (IMAGENS[0], IMAGENS[1]):
        if "hands rest empty" not in blocos.get(nome, ""):
            ach.append(("ERRO", "AM10: %s sem a trava de ESTADO das maos "
                                "— maos vazias na imagem parada" % nome))
    # ⛔⛔⛔ NOS TAKEs A LENTE VIROU AO CONTRARIO — 2026-08-21.
    # Ela cobrava TRES literais de negacao (`never takes, holds, reaches
    # for or touches the spoon`, `The ONLY hand that moves toward`, `Do NOT
    # show:`) — e a medicao do frame provou que essas tres eram a CAUSA, nao
    # o conserto: com as dez negacoes no lugar, a colher continuava nascendo
    # na mao parada aos 0,75s. O que passou em campo foram as variacoes
    # POSITIVAS (B no take 1, C no take 2), e e' isso que a lente cobra
    # agora — mais a proibicao de a lista `Do NOT show:` voltar.
    # ⛔ A memoria do defeito NAO cai: os literais antigos viram o CONTROLE,
    # nao o alvo. Quem os replantar e' acusado.
    ancoras = {takes_do(spec)[0]: ["only movement in the entire shot",
                          "frozen exactly as in the photograph",
                          "the only person in the frame"],
               takes_do(spec)[1]: ["closed around", "kneecaps",
                          "only movement in the entire shot",
                          "the only person in the frame",
                          "Exactly one spoon exists"]}
    for nome, lits in ancoras.items():
        txt = blocos.get(nome, "")
        for lit in lits:
            if lit not in txt:
                ach.append(("ERRO", "AM10: %s sem %r — e' a variacao que "
                                    "passou em campo em 21/08 (B no take 1, "
                                    "C no take 2)" % (nome, lit)))
    # ⛔ a trava de SO' ENGOLIR (22/08) vive nos dois takes de colherada
    for nome in takes_do(spec)[:2]:
        txt = blocos.get(nome, "")
        for lit in ("SINGLE swallow", "jaw and lips stay still",
                    "thin liquid"):
            if lit not in txt:
                ach.append(("ERRO", "AM10: %s sem %r — sem ela o gerador faz "
                                    "o sentado MASTIGAR o xarope, filmado em "
                                    "22/08" % (nome, lit)))
        # ⛔ e a palavra proibida nao pode entrar nem negada: negar `chew`
        # e' pintar a mastigacao no prompt
        if re.search(r"\bchew", txt, re.I):
            ach.append(("ERRO", "AM10: %s escreve `chew` — mesmo negando, o "
                                "token entra e o gerador mastiga" % nome))
        if "Do NOT show:" in txt:
            ach.append(("ERRO", "AM10: %s com a lista `Do NOT show:` de "
                                "volta — ela era a maior fonte de injecao "
                                "da colher na mao dele" % nome))
        # ⛔ e nenhuma clausula pode colar COLHER em MAO DELE, nem negando
        for m in re.finditer(r"[^.;:]+", txt):
            fr = m.group(0)
            if re.search(r"spoon", fr, re.I) and \
               re.search(r"\b(?:his|her) hand|seated %s's hand"
                         % ("man" if spec.get("sexo_sujeito") == "homem"
                            else "woman"), fr, re.I) and \
               "narrator" not in fr:
                ach.append(("ERRO", "AM10: %s cola `spoon` na mao do sentado "
                                    "(%r) — foi assim que ela nasceu la'"
                            % (nome, fr.strip()[:60])))
    for nome in takes_do(spec):
        if "never leaves" not in blocos.get(nome, ""):
            ach.append(("ERRO", "AM10: %s sem a trava da GARRAFA — ela some "
                                "da mao e volta do nada" % nome))
    for nome in takes_do(spec)[2:]:
        if "Exactly two hands" not in blocos.get(nome, ""):
            ach.append(("ERRO", "AM10: %s sem a trava das DUAS MAOS — mao "
                                "fantasma no take do CTA" % nome))


# ⚠️⚠️ DUAS PALAVRAS SOZINHAS NAO SERVEM, e as duas foram achadas MEDINDO O
# PROMPT GERADO — nenhuma aparecia na pool:
#   · `past`   — a IMAGE 01 diz que a barriga *"hangs past the knees"*, que
#                e' posicao; acusou 200 de 200 videos CERTOS;
#   · `riding` — a mesma imagem diz *"the hem riding up"*, que e' a camisa
#                subindo, pedido dele; acusou os mesmos 200.
# ⛔ Lente colada no literal cru acusa a si mesma (§16). Aqui os dois so'
# contam em construcao de MOVIMENTO — `creaks slowly past`, `riding along`
# — e o substantivo `rider`, que era o defeito real do pomar, fica.
# ⚠️ E `across the` exclui `frame`: e' a propria trava que diz *"nothing
# travels across the frame"*.
_RX_TRAVESSIA = re.compile(
    r"\b(?:(?:creaks?|rolls?|rumbles?|trundles?|rattles?|clatters?|moves?|"
    r"drives?|walks?|goes|passes|plods?|rides?|riding)\s+(?:\w+\s+)?"
    r"(?:past|along|across|by)|"
    r"passing|crossing|crosses|plods|plodding|"
    r"hauling|hauls|pulled by|pulling|driving|rider|"
    r"approaching|approaches|travels|traveling|travelling|"
    r"along the|across the (?:field|yard|lane|road|track|pasture|barnyard)|"
    r"down the (?:lane|track|road|path))\b", re.I)


def _am11_fundo(spec, blocos, ach):
    """⛔⛔ AM11 — NADA ATRAVESSA O QUADRO (2026-08-21).

    O operador filmou os quatro takes de um video e mostrou a carroca de
    feno passando atras do casal no take 1, passando OUTRA VEZ no take 2 —
    que acontece 47 dias depois — e mais duas no 3 e no 4, que nascem da
    mesma imagem: *"a carroca fica dando looping [...] ela ja' deveria ter
    passado"*.

    ⭐ A lente tem DUAS metades, e a primeira e' a que importa:
      1. audita a POOL INTEIRA, nao so' o cenario sorteado. Cenario ruim
         que hoje nao caiu no sorteio cai amanha, e o defeito volta pela
         porta dos fundos. Mesmo precedente da `GO21` do GOOD 16.
      2. exige a trava de fundo parado nos QUATRO takes, que e' onde o
         `vida` entra e onde o movimento e' de fato pedido.
    """
    for c in CENARIOS:
        for campo in ("desc", "vida", "curto"):
            m = _RX_TRAVESSIA.search(c.get(campo, ""))
            if m:
                ach.append(("ERRO", "AM11: cenario %r tem %r no campo %s — "
                                    "verbo de travessia vira objeto cruzando "
                                    "o quadro nos quatro takes, e o operador "
                                    "filmou esse loop"
                            % (c["id"], m.group(0), campo)))
    for nome in takes_do(spec):
        if "The background holds perfectly still" not in blocos.get(nome, ""):
            ach.append(("ERRO", "AM11: %s sem a trava de FUNDO PARADO — o "
                                "`vida` entra cru e o fundo volta a se mexer"
                        % nome))


# ⛔ os tokens que CODIFICAM coloracao europeia. Nao e' lista de palavras
# feias: e' a lista do que, num rosto declarado negro, faz o gerador escolher
# entre a trava e a descricao — e escolher a descricao.
_RX_COR_EUROPEIA = re.compile(
    r"\b(?:red|ginger|blond|blonde|freckled|freckles|fair|ruddy|florid|"
    r"sallow|pale|strawberry)\b|\b(?:blue|green|gray-blue|grey-blue)\s+eyes",
    re.I)


def _am12_coerencia_pele(spec, blocos, ach):
    """⛔⛔ AM12 — a pele declarada e a coloracao descrita nao podem brigar.

    Nasceu do lote de 21/08: ele travou o sujeito em NEGRA, gerou varios
    sorteios e veio homem branco. A `AM7` passava, porque ela so' pergunta
    se `Black American` CHEGOU ao bloco — e chegava. O que faltava era
    perguntar se, na mesma frase, havia outra coisa dizendo o contrario.

    ⭐ A lente audita a POOL INTEIRA alem do sorteio: sujeito marcado como
    compativel com negra mas descrito com cabelo ruivo cai aqui mesmo que
    hoje o sorteio nao o pegue. Mesmo desenho da `AM11` — defeito que dorme
    na pool acorda no lote seguinte.
    """
    for pool, rot in ((SUJEITOS_H, "H"), (SUJEITOS_M, "M")):
        for s in pool:
            if "negra" not in s.get("pele", ("branca",)):
                continue
            for campo in ("rosto", "visual"):
                m = _RX_COR_EUROPEIA.search(s.get(campo, ""))
                if m:
                    ach.append(("ERRO", "AM12: sujeito %s/%s vale em negra e "
                                        "tem %r no campo %s — o prompt sai "
                                        "se contradizendo e o gerador segue "
                                        "a descricao, nao a trava"
                                % (rot, s["id"], m.group(0), campo)))
    # e o sujeito SORTEADO: pele nao-branca nao convive com coloracao europeia
    # ⛔⛔ SO' `rosto` E `visual`, NUNCA A ROUPA — conserto de 22/08. A versao
    # anterior varria o trecho inteiro do sujeito no bloco gerado, e a roupa
    # vai junto: `a red checked western shirt` acusou 7 de 400 videos CERTOS,
    # porque `red` esta no regex por causa de CABELO ruivo. Camisa vermelha
    # nao diz nada sobre a pele de ninguem.
    # ⚠️ Oitava vez esta semana que uma lente colada numa palavra crua acusa
    # o estado correto. O recorte certo e o CAMPO, nao o texto todo.
    if spec.get("pele_sujeito") and spec["pele_sujeito"] != PELES["branca"]:
        suj = spec.get("sujeito") or {}
        for campo in ("rosto", "visual"):
            m = _RX_COR_EUROPEIA.search(suj.get(campo, ""))
            if m:
                ach.append(("ERRO", "AM12: sujeito declarado %s e descrito "
                                    "com %r no campo %s — 1 token de trava "
                                    "contra a coloracao inteira, e a trava "
                                    "perde"
                            % (spec["pele_sujeito"], m.group(0), campo)))


def _am13_negativo_coerente(spec, blocos, ach):
    """⛔⛔ AM13 — o negativo nao pode proibir o que o prompt PEDE.

    Achada em 21/08 ao escrever os sujeitos novos: `NEGATIVO_IMG` proibia
    *a bald or shaved head* incondicionalmente, e dois sujeitos pedem
    careca com todas as letras. Em 25% dos sorteios masculinos o mesmo
    prompt mandava e desmandava.
    ⛔ E' a QUARTA vez que este motor paga a mesma familia num dia so' — a
    colher fantasma, o joinha contra a trava de bracos, a negacao que
    desenhava a colher, e agora esta. Por isso a lente e' GENERICA: ela nao
    cobra um literal, ela compara o que o sujeito PEDE com o que a lista
    NEGA, e vale para qualquer item que alguem acrescentar depois.
    """
    # ⚠️ SO' ITENS INCONDICIONAIS ENTRAM AQUI. A primeira versao tambem
    # cobrava `glasses that were not described` contra o sujeito de oculos e
    # acusou 52 de 400 videos CERTOS — porque essa frase JA' se qualifica
    # sozinha (*that were not described*), como `a clean-shaven face WHEN
    # facial hair is described`. Negativo auto-qualificado nao contradiz
    # nada; quem contradiz e' o item que nega sem condicao.
    vis = (spec.get("sujeito") or {}).get("visual", "")
    pares = [(r"\b(?:bald|balding|shaved head)\b", "a bald or shaved head")]
    for rx, item in pares:
        if not re.search(rx, vis, re.I):
            continue
        for nome in (IMAGENS[0], IMAGENS[1]):
            txt = blocos.get(nome, "")
            neg = txt.split("Do NOT include:")[-1] if "Do NOT include:" in txt \
                else ""
            if item in neg:
                ach.append(("ERRO", "AM13: %s pede %r no sujeito e o negativo "
                                    "proibe %r — prompt que se contradiz e' o "
                                    "que o gerador resolve inventando"
                            % (nome, vis[:34], item)))


# ⛔ o token que a lente procura no bloco, por identidade fixa. O da
# curandeira africana e `African` porque a descricao dela diz `African
# healer`, nunca `Black African` — foi o falso positivo de 89 em 400
# que a AM7 deu no primeiro autoteste.
_TOKEN_PELE_FIXA = {"Native American": "Native American",
                    "Black African": "African",
                    "Black American": "Black American",
                    "white American": "white American"}


# ⛔ peca de BAIXO: a roupa da tribo e' esticada sobre a barriga, entao
# calca, bermuda e sapato nao servem — e a frase montada sairia sem sentido
# ("his jeans is stretched drum-tight over the entire ball").
_RX_PECA_DE_BAIXO = re.compile(
    r"\b(jeans|trousers|pants|shorts|slacks|leggings|skirt|boots?|shoes|"
    r"sneakers|sandals)\b", re.I)


def _am17_idade(spec, blocos, ach):
    """⛔⛔ AM17 — ninguem abaixo de 50 no pool do sujeito (23/08).

    ⭐ Audita a POOL INTEIRA, nao so' o sorteado: entrada nova escrita com
    38 anos so' apareceria no dia em que caisse no sorteio, e ai' num lote
    inteiro. Mesmo desenho da AM11, AM12 e AM16.
    ⚠️ E cobra a idade NO QUADRO, nao so' no dado: e' a IMAGE 01 que o
    gerador le', e ja' houve caso neste motor de campo certo que nao chegava
    ao bloco.
    """
    for pool, rot in ((SUJEITOS_H, "H"), (SUJEITOS_M, "M")):
        for x in pool:
            if x.get("idade", 0) < IDADE_MIN_SUJEITO:
                ach.append(("ERRO", "AM17: sujeito %s/%s tem %d anos e o piso "
                                    "e' %d — corpo-prova jovem nao e' espelho "
                                    "do publico do nicho"
                            % (rot, x["id"], x["idade"], IDADE_MIN_SUJEITO)))
    idade = (spec.get("sujeito") or {}).get("idade")
    if idade and "%d-year-old" % idade not in blocos.get(IMAGENS[0], ""):
        ach.append(("ERRO", "AM17: a idade do sujeito (%d) nao chegou a "
                            "IMAGE 01" % idade))


def _am18_composicao(spec, blocos, ach):
    """⛔⛔ AM18 — a pessoa COMPOSTA nao contradiz a trava de sexo nem a
    de pele, e chega inteira ao quadro.

    ⭐ Substitui a AM16 (das tribos), aposentada no mesmo dia. A licao que
    sobrevive dela e a razao desta existir: as tribos NAO tinham campo de
    sexo — zero de quinze —, e mecanico, cowboy e veterano de guerra caiam
    em mulher de 60. Ele viu no painel: *"nao faz sentido para mulheres
    americanas de 60 anos essas profissoes"*.

    ⚠️ Audita a POOL INTEIRA alem do sorteio: entrada nova sem tag de sexo
    ou de pele so apareceria no dia em que caisse, e ai num lote inteiro.
    """
    for nome, pool in (("PECAS", PECAS), ("CORES_E_PADROES", CORES_E_PADROES),
                       ("DETALHES_ROUPA", DETALHES_ROUPA),
                       ("ROSTOS", ROSTOS), ("OLHOS", OLHOS),
                       ("CABELOS", CABELOS)):
        for x in pool:
            if x.get("pele") not in ("ambas", "branca", "negra"):
                ach.append(("ERRO", "AM18: %s/%r sem tag de PELE valida"
                            % (nome, x.get("id"))))
            if x.get("sexo") not in ("ambos", "homem", "mulher"):
                ach.append(("ERRO", "AM18: %s/%r sem tag de SEXO valida"
                            % (nome, x.get("id"))))
    eixos = (spec.get("sujeito") or {}).get("_eixos")
    if not eixos:
        return                      # sujeito travado do pool fixo: nao se aplica
    _p = "negra" if spec["pele_sujeito"] == PELES["negra"] else "branca"
    _s = "homem" if spec["sexo_sujeito"] == "homem" else "mulher"
    todos = {x["id"]: x for pool in (PECAS, CORES_E_PADROES, DETALHES_ROUPA,
                                     ROSTOS, OLHOS, CABELOS) for x in pool}
    for eixo, eid in eixos.items():
        x = todos.get(eid)
        if not x:
            continue
        if x.get("sexo", "ambos") not in ("ambos", _s):
            ach.append(("ERRO", "AM18: o eixo %s sorteou %r, que e' de %s, "
                                "num sujeito %s" % (eixo, eid,
                                                    x.get("sexo"), _s)))
        if x.get("pele", "ambas") not in ("ambas", _p):
            ach.append(("ERRO", "AM18: o eixo %s sorteou %r, que e' de pele "
                                "%s, num sujeito de pele %s"
                        % (eixo, eid, x.get("pele"), _p)))


def _am19_ar(spec, blocos, ach):
    """⛔⛔ AM19 — o ar limpo e o fundo de pedra (ordem de 2026-08-23).

    *"NUNCA em hipotese alguma faca ter poeira, chuva ou qualquer coisa que
    atrapalhe a filmagem no ambiente. Deve ser um ambiente sem esse tipo de
    coisa voando, caindo, passando, subindo, balancando, etc."*

    ⭐ Ela audita a POOL INTEIRA de cenarios, nao so' o sorteado — um `vida`
    com poeira so' apareceria no dia em que aquele cenario caisse, e ai' num
    lote inteiro. Foi exatamente assim que a serragem do `celeiro_novo`
    chegou ao vídeo dele.
    ⛔ E cobra a frase POSITIVA nos tres quadros e nos takes: o contrato do
    arquivo e' que negacao injeta o token, entao `no dust` esta' proibido tanto
    quanto a poeira.
    """
    for c in CENARIOS:
        for campo in ("vida", "desc"):
            m = _RX_ATMOSFERA.search(c.get(campo, "") or "")
            if m:
                ach.append(("ERRO", "AM19: cenario %r tem %r em `%s` — o "
                                    "operador baniu coisa voando, caindo, "
                                    "passando, subindo ou balancando"
                            % (c["id"], m.group(0), campo)))
    for nome in IMAGENS:
        if AR_LIMPO_IMG not in blocos.get(nome, ""):
            ach.append(("ERRO", "AM19: %s sem a clausula de ar limpo" % nome))
    for nome in takes_do(spec):
        if AR_LIMPO_TK not in blocos.get(nome, ""):
            ach.append(("ERRO", "AM19: %s sem a clausula de ar limpo" % nome))
    # ⛔⛔ E NENHUM DOS TRES QUADROS PEDE POEIRA PELA NEGACAO. `no dust in the
    # air` desenha poeira — e' a mesma familia da colher fantasma.
    # ⚠️ SO' A PARTE VISUAL. O bloco de audio dos takes diz `no sound at
    # all, no ambience, no music, no wind, no voice` — ali `no wind` e' som
    # de vento, nao vento em quadro, e a primeira versao desta lente acusou
    # 400 de 400 videos CERTOS por causa dele. E' a decima vez que este
    # arquivo paga lente colada em literal cru; a correcao e' sempre a
    # mesma: restringir o ESCOPO, nunca afrouxar o padrao.
    for nome in list(IMAGENS) + list(takes_do(spec)):
        m = _RX_NEGA_ATMOSFERA.search(blocos.get(nome, "").split("Audio:")[0])
        if m:
            ach.append(("ERRO", "AM19: %s NEGA atmosfera (%r) — negacao "
                                "injeta o token; a frase tem de ser positiva"
                        % (nome, m.group(0))))


def _am20_magro(spec, blocos, ach):
    """⛔⛔ AM20 — a IMAGE 02 nao pode conter palavra de FOLGA.

    Medido em 200 sorteios no dia em que ele reprovou o lote: o bloco antigo
    escrevia `loose` 415 vezes, `hanging` 409 e `oversized` 201 — 100% dos
    videos —, todas vindas de NEGACOES (`no hanging flesh`, `never the huge
    loose clothes`, `Do NOT include: oversized clothes hanging loose`). O
    prompt cuja tarefa e' desenhar roupa justa pedia roupa larga cinco vezes.
    ⚠️ A palavra pode chegar por dois caminhos, e a lente cobra os dois: a
    negacao (que saiu) e a ROUPA COMPOSTA — 15 entradas dos pools descrevem a
    peca como folgada (`with the cuffs unbuttoned and hanging loose`). Hoje a
    IMAGE 02 nao restata a peca, entao elas nao chegam la'; se alguem voltar a
    restatar, esta lente pega.
    """
    # ⚠⚠ SO' DO BLOCO `BODY:` PARA BAIXO. A frase de abertura carrega a
    # descricao do CABELO, e `loose curls` / `loose bun` sao penteados, nao
    # roupa folgada: a primeira versao desta lente acusou 22 de 400 videos
    # CERTOS por causa deles. E' a decima primeira vez que este arquivo paga
    # lente colada em literal cru, e a correcao e' sempre restringir o
    # ESCOPO — afrouxar o padrao mataria a lente.
    b2 = blocos.get(IMAGENS[1], "").split(" BODY:", 1)[-1]
    m = _RX_FOLGA.search(b2)
    if m:
        ach.append(("ERRO", "AM20: IMAGE 02 diz %r — o quadro que tem de "
                            "desenhar roupa justa esta' pedindo roupa larga"
                    % m.group(0)))
    # ⛔ e nenhuma negacao sobre o CORPO: `no belly`, `no double chin`,
    # `Do NOT include: any remaining belly` desenham a barriga de volta.
    m = _RX_NEGA_CORPO.search(b2)
    if m:
        ach.append(("ERRO", "AM20: IMAGE 02 NEGA o corpo gordo (%r) — "
                            "negacao injeta o token" % m.group(0)))


def _am15_receita(spec, blocos, ach):
    """⛔⛔ AM15 — a bebida da copy nomeia a VOCACAO de quem narra.

    Nasceu do painel dele em 22/08: com o indio anciao selecionado, a copy
    2 seguia mandando comentar por uma *"Amish drink recipe"*. Fala
    desmentindo a imagem no mesmo video e' o defeito mais barato de evitar
    e o mais caro de deixar passar — o espectador nao sabe o que esta
    pedindo.

    ⭐ Audita a POOL INTEIRA: narrador sem `receita` declarada cai aqui no
    dia em que for escrito, nao no dia em que for sorteado.
    """
    for n in NARRADORES:
        if not n.get("receita") or not n.get("receita_pt"):
            ach.append(("ERRO", "AM15: narrador %r sem `receita`/`receita_pt` "
                                "— a copy 2 nomearia a bebida errada"
                        % n["id"]))
    r = spec["narrador"].get("receita")
    if r and spec["copy"]["id"] == "c2":
        fala = " ".join(x for x in spec["falas"] if x)
        if r not in fala:
            ach.append(("ERRO", "AM15: o narrador %r e de bebida %r e a copy "
                                "nao diz isso — a fala desmente a imagem"
                        % (spec["narrador"]["id"], r)))
        if r != "Amish" and "Amish" in fala:
            ach.append(("ERRO", "AM15: sobrou `Amish` na fala de um narrador "
                                "%r" % r))


def _am14_mundo(spec, blocos, ach):
    """⛔⛔ AM14 — o narrador e o cenario vivem no MESMO mundo.

    Nasceu com as tres identidades de 21/08. Sem ela, a freira cai na
    varanda da cabana e a granny woman no claustro: roupa tipica em
    cenario errado nao le como vocacao, le como fantasia — e vocacao
    legivel foi exatamente o que ele pediu.

    ⭐ Audita a POOL INTEIRA alem do sorteio: mundo de narrador sem
    cenario nenhum e uma armadilha que so aparece no dia em que ele
    for sorteado. Mesmo desenho da AM11 e da AM12.
    """
    mundos_cen = {c.get("mundo", "amish") for c in CENARIOS}
    for n in NARRADORES:
        m = n.get("mundo", "amish")
        if m not in mundos_cen:
            ach.append(("ERRO", "AM14: narrador %r vive no mundo %r e "
                                "nao existe cenario nenhum la" 
                        % (n["id"], m)))
    mn = spec["narrador"].get("mundo", "amish")
    mc = spec["cenario"].get("mundo", "amish")
    if mn != mc:
        ach.append(("ERRO", "AM14: narrador %r e do mundo %r e o cenario "
                            "%r e do mundo %r — vocacao em cenario errado "
                            "le como fantasia"
                    % (spec["narrador"]["id"], mn,
                       spec["cenario"]["id"], mc)))


def _am7_pele(spec, blocos, ach):
    """⛔ AM7 — a pele sorteada/travada aparece ESCRITA nos blocos.

    ⚠️ A primeira versao cobrava o LITERAL `Black African` num narrador cuja
    identidade ja' esta' escrita como `African healer` — 89 acusacoes em 400
    videos CERTOS no primeiro autoteste. Lente colada na forma acusa a si
    mesma; o que ela tem de garantir e' que a IDENTIDADE chegue ao quadro:
    nos fixos, o token da identidade; nos livres, a pele sorteada."""
    # ⚠️ O MAPA E EXPLICITO desde 21/08. A versao anterior era um
    # `if/else` que mandava toda pele fixa que nao fosse indigena para
    # o token `African` — com a root doctor Gullah (`Black American`)
    # isso acusaria 100% dos videos dela, porque `African` nao aparece
    # em lugar nenhum da descricao. Mapa que adivinha envelhece na
    # primeira identidade nova.
    fixa = spec["narrador"]["pele_fixa"]
    alvo = _TOKEN_PELE_FIXA.get(fixa, fixa) if fixa \
        else spec["pele_narrador"]
    if alvo not in blocos.get(IMAGENS[0], ""):
        ach.append(("ERRO", "AM7: a identidade do narrador (%s) nao chegou a "
                            "IMAGE 01" % alvo))
    if spec["pele_sujeito"] not in blocos.get(IMAGENS[0], ""):
        ach.append(("ERRO", "AM7: pele do sujeito (%s) nao chegou a IMAGE 01"
                    % spec["pele_sujeito"]))


def _am8_mesmo(spec, blocos, ach):
    """⭐⭐ AM8 — as IMAGEs 2-3 DERIVAM da IMAGE 01 anexada (ordem 21/08).

    ⛔ Sem a ancora `Using the provided image` o prompt vira descricao solta
    e o gerador inventa outra cena — o tempo que a ordem existe para poupar
    volta em dobro como incoerencia entre quadros."""
    b2 = blocos.get(IMAGENS[1], "")
    # ⛔ ancoras do MAGRO ABSOLUTO (21/08): TRANSFORM (verbo forte), a
    # barriga CHATA com numero, a identidade do rosto restatada e a roupa
    # larga. "Change ONLY" + "slimmer" relativo rendeu gordo em 3 de 4.
    # ⛔ ANCORAS REESCRITAS EM 21/08 — o operador diagnosticou que `TRANSFORM
    # [...] replace the enormous body` fazia o gerador criar uma PESSOA NOVA.
    # As ancoras de hoje sao de CONTINUIDADE, e cada uma responde a um
    # defeito que ele apontou com o dedo na gravacao.
    # ⚠️ ANCORAS REESCRITAS EM 23/08, junto com o texto aprovado. As
    # antigas (`SAME TWO PEOPLE`, `face is IDENTICAL`, `THIN LEGS`, `flat
    # stomach`, `in a small size that fits`) apontavam para literais que
    # sairam do bloco — lente presa a literal morto acusa 100% e treina o
    # operador a ignorar o gate.
    for lit, motivo in (
            ("Using the provided image", "a base anexada e' a referencia"),
            ("the same person photographed months later",
             "continuidade, nunca substituicao"),
            ("lean and athletic at exactly",
             "o peso EXATO, sem aproximacao (ordem de 21/08)"),
            ("slim from head to feet",
             "*\"deve emagrecer por completo, nao so a barriga\"*"),
            ("stomach is flat", "barriga CHATA, nao 'menor'"),
            ("knees are bony", "*\"a perna dele nao mudou nada\"*"),
            ("the very same outfit",
             "a MESMA peca, nunca uma peca nova — e' o literal que o "
             "controle negativo planta como `a new`"),
            ("taken in by a tailor",
             "a MESMA peca ajustada — nao uma peca nova"),
            ("SAME SLEEVE LENGTH",
             "*\"o que era camisa curta virou camisa de manga longa\"*"),
            ("SAME LEG LENGTH",
             "*\"o que era calca virou shorts, e vice-versa\"*"),
            ("knees together and pointing forward",
             "*\"a imagem 2 o personagem sempre deve estar com a postura "
             "correta\"*")):
        if lit not in b2:
            ach.append(("ERRO", "AM8: IMAGE 02 sem %r — %s" % (lit, motivo)))
    b3 = blocos.get(IMAGENS[2], "")
    # ⚠️ `no longer in frame` SAIU em 23/08 — era a negacao que reinjetava
    # a pessoa sentada. No lugar entram as tres ancoras positivas.
    for lit in ("Using the provided image", "reframe as a selfie",
                "person who was STANDING", "the only person in this image"):
        if lit not in b3:
            ach.append(("ERRO", "AM8: IMAGE 03 sem %r — sem isso o gerador "
                                "escolhe sozinho entre as duas pessoas da "
                                "base, e escolheu a SENTADA em 3 de 4" % lit))
    # ⛔ e a descricao do narrador tem de estar AQUI, nao so na IMAGE 01
    _idade = re.search(r"\b(\d\d)-year-old|in (?:her|his) late seventies",
                       spec["narrador"]["desc"])
    if _idade and _idade.group(0) not in b3:
        ach.append(("ERRO", "AM8: IMAGE 03 sem a idade do narrador (%r) — a "
                            "idade e o que separa a narradora do sujeito "
                            "sentado" % _idade.group(0)))
    # ⛔ a pessoa sentada NAO pode ser mencionada num quadro onde ela nao esta
    if re.search(r"seated (?:person|man|woman)", b3, re.I):
        ach.append(("ERRO", "AM8: IMAGE 03 menciona a pessoa SENTADA — "
                            "nomear quem nao pode aparecer e' desenha-la"))


def lint(spec, blocos):
    ach = []
    for aviso in spec.get("avisos", []):
        ach.append(("AVISO", aviso))
    sc.lint_tags(blocos, ach)
    _am1_limpo(spec, blocos, ach)
    _am2_copy(spec, blocos, ach)
    _am4_mudez(spec, blocos, ach)
    _am5_pronome(spec, blocos, ach)
    _am6_garrafa(spec, blocos, ach)
    _am7_pele(spec, blocos, ach)
    _am9_peso(spec, blocos, ach)
    _am10_bugs(spec, blocos, ach)
    _am11_fundo(spec, blocos, ach)
    _am12_coerencia_pele(spec, blocos, ach)
    _am13_negativo_coerente(spec, blocos, ach)
    _am14_mundo(spec, blocos, ach)
    _am15_receita(spec, blocos, ach)
    _am19_ar(spec, blocos, ach)
    _am20_magro(spec, blocos, ach)
    _am18_composicao(spec, blocos, ach)
    _am17_idade(spec, blocos, ach)
    _am8_mesmo(spec, blocos, ach)
    sc.lint_anticeleb(blocos, ach)
    # ⛔ O TETO ANTIGO MORREU COM A EXCECAO QUE ELE CARREGAVA: ate' 21/08 a
    # COPY 1 era excecao declarada (34 palavras num take de 8s) e o campo
    # media' o take 3 inteiro. A divisao em QUATRO takes tornou a excecao
    # desnecessaria — cada parte cabe no proprio relogio, e quem cobra isso
    # agora e' a AM2, por take, com o `SEGUNDOS_TAKE` de cada um.
    return ach


# ===========================================================================
# RESUMO
# ===========================================================================
def resumo_pt(spec):
    c = spec["copy"]
    return ("20s, 4 takes (4s+4s+8s+6s no Veo · takes 1-2 cortados a ~3s na "
            "edicao). NARRA: %s, pele %s%s. MUDA: %s de %d anos (%s, pele "
            "%s) — antes ~%d kg, depois LEAN/FIT ~70 kg. CENARIO: %s. "
            "** LEGENDA: os quadros saem LIMPOS — no editor, queime DAY 1 no "
            "take 1 e DAY %d no take 2, estilo %s. ** TAKES 1-2 MUDOS (a "
            "musica entra no editor). COPY %s — PT: %s"
            % (spec["narrador"]["rotulo"], spec["pele_narrador"],
               (" · vestido %s" % spec["cor_vestido"])
               if spec["narrador"]["id"] == "vovo_amish" else "",
               "homem" if spec["sexo_sujeito"] == "homem" else "mulher",
               spec["sujeito"]["idade"], spec["sujeito"]["rotulo"],
               spec["pele_sujeito"], spec["peso_kg"],
               spec["cenario"]["rotulo"], spec["dia2"],
               spec["estilo"]["rotulo"], c["rotulo"],
               spec.get("fala_pt", "")))


# ===========================================================================
# CONTRATO DA UI COMPARTILHADA
# ===========================================================================
EIXOS_UI = [
    ("copy", "A COPY", "COPIES", "rotulo"),
    ("cenario", "O CENARIO", "CENARIOS", "rotulo"),
    ("sujeito", "QUEM MUDA", "sujeitos_do_sexo", "rotulo"),
    ("estilo", "A LEGENDA DAY", "ESTILOS_DAY", "rotulo"),
]
EIXOS_TRAVAVEIS = ["copy", "cenario", "sujeito", "estilo"]
DROPDOWNS_UI = [("narrador", "QUEM NARRA", "NARRADORES", "rotulo")]
TRAVAS_UI = [
    ("copy", "copy", ["livre", "1", "2", "3", "4"]),
    ("sexo_sujeito", "quem muda", ["livre", "homem", "mulher"]),
    ("pele_narrador", "pele narrador", ["livre", "branca", "negra"]),
    ("pele_sujeito", "pele sujeito", ["livre", "branca", "negra"]),
]
IGNORA_PAINEL = ("copy", "sujeito", "estilo")


# ===========================================================================
# AUTOTESTE — aceite e' MEDICAO, nunca relato
# ===========================================================================
def autoteste(n=400):
    print("%s — autoteste, %d sorteios" % (TITULO, n))
    erros = 0
    vistos = {"narrador": set(), "copy": set(), "cenario": set(),
              "sujeito": set(), "estilo": set(), "dia2": set(),
              "sexo": set()}
    for i in range(n):
        rng = random.Random(i)
        s = sortear(["clara", "escura"][i % 2], rng, {})
        b = montar(s)
        for nivel, msg in lint(s, b):
            if nivel == "ERRO":
                erros += 1
                if erros <= 5:
                    print("  [ERRO] seed %d: %s" % (i, msg))
        for k, v in [("narrador", s["narrador"]["id"]),
                     ("copy", s["copy"]["id"]),
                     ("cenario", s["cenario"]["id"]),
                     ("sujeito", s["sujeito"]["id"]),
                     ("estilo", s["estilo"]["id"]),
                     ("dia2", s["dia2"]), ("sexo", s["sexo_sujeito"])]:
            vistos[k].add(v)
    print("  ERRO em %d sorteios ... %d" % (n, erros))
    alvo = {"narrador": len(NARRADORES), "copy": len(COPIES),
            "cenario": len(CENARIOS),
            # ⚠️ o sujeito e' COMPOSTO: o alvo nao e' o tamanho de um pool,
            # e sim quantas pessoas DISTINTAS sairam. Com 400 sorteios,
            # exigimos 400 — a composicao nao pode repetir ninguem.
            "sujeito": n,
            "estilo": len(ESTILOS_DAY),
            "dia2": DIA_MAX - DIA_MIN + 1, "sexo": 2}
    falha_alcance = 0
    for k, a in alvo.items():
        ok = len(vistos[k]) == a
        falha_alcance += 0 if ok else 1
        print("  alcance %-9s %2d/%2d %s"
              % (k, len(vistos[k]), a, "ok" if ok else "<-- INALCANCAVEL"))

    # --- travas honradas ---------------------------------------------------
    rng = random.Random(99)
    falha_trava = 0
    for nid in [x["id"] for x in NARRADORES]:
        s = sortear("clara", rng, {}, {"narrador": nid})
        if s["narrador"]["id"] != nid:
            falha_trava += 1
    for i in "1234":
        s = sortear("clara", rng, {}, {"copy": i})
        if s["copy"]["id"] != "c%s" % i:
            falha_trava += 1
    # ⚠️ A trava de SEXO exigia o sujeito dentro do pool FIXO. Desde 23/08 ele
    # e' COMPOSTO, entao o que se cobra mudou: o sexo pedido e' honrado e
    # NENHUM eixo sorteado pertence ao outro sexo — que e' a queixa que deu
    # origem a isto (*"mecanico, cowboy, militar aposentado [...] nao faz
    # sentido para mulheres americanas de 60 anos essas profissoes"*).
    _todos_eixos = {x["id"]: x for _p in (PECAS, CORES_E_PADROES,
                                          DETALHES_ROUPA, ROSTOS, OLHOS,
                                          CABELOS) for x in _p}
    for sx in ("homem", "mulher"):
        for _t in range(40):
            s = sortear("clara", rng, {}, {"sexo_sujeito": sx})
            _ex = (s["sujeito"].get("_eixos") or {}).values()
            if s["sexo_sujeito"] != sx or any(
                    _todos_eixos.get(e, {}).get("sexo", "ambos")
                    not in ("ambos", sx) for e in _ex):
                falha_trava += 1
                break
    s = sortear("clara", rng, {}, {"pele_narrador": "negra",
                                   "narrador": "vovo_amish"})
    if s["pele_narrador"] != "Black American":
        falha_trava += 1
    s = sortear("clara", rng, {}, {"pele_narrador": "negra",
                                   "narrador": "india_anciana"})
    if s["pele_narrador"] != "Native American" or not s["avisos"]:
        falha_trava += 1
    s = sortear("escura", rng, {}, {"pele_sujeito": "branca"})
    if s["pele_sujeito"] != "white American":
        falha_trava += 1
    print("  travas honradas ......... %s"
          % ("ok" if not falha_trava else "%d FALHA(S)" % falha_trava))

    # --- controles NEGATIVOS: plantar o defeito e exigir a acusacao --------
    rng = random.Random(7)
    # ⛔⛔ A BASE DOS CONTROLES E' TRAVADA NA COPY 1, e isso passou a
    # importar em 21/08: desde que as copies 2/3/4 saem em TRES takes, um
    # sorteio livre aqui podia nao ter `TAKE 04` nenhum — e metade dos
    # controles abaixo indexa `TAKES[3]`. Eles vinham passando por SORTE do
    # seed, que e' medidor cego com outro nome.
    s = sortear("clara", rng, {}, {"copy": "1"})
    b = montar(s)
    cegas = 0
    if len(takes_do(s)) != 4:
        cegas += 1   # a base dos controles deixou de ter 4 takes

    def _acusa(blocos, trecho, spec=None):
        return any(trecho in m for nv, m in lint(spec or s, blocos)
                   if nv == "ERRO")

    # ⛔ o DAY nao pode VOLTAR ao prompt em silencio (ordem de 21/08)
    p = dict(b)
    p[IMAGENS[0]] += ' A large caption reading "DAY 1" on top.'
    cegas += 0 if _acusa(p, "AM1") else 1
    p = dict(b)
    p[IMAGENS[0]] = p[IMAGENS[0]].replace(_SEM_TEXTO_IMG, "")
    cegas += 0 if _acusa(p, "AM1") else 1
    # ⛔ as tres travas de bug filmadas
    p = dict(b)
    p[IMAGENS[0]] = p[IMAGENS[0]].replace("hands rest empty", "hands rest")
    cegas += 0 if _acusa(p, "AM10") else 1
    # ⛔⛔ OS CONTROLES VIRARAM JUNTO COM A LENTE (21/08): o que se planta
    # agora e' o retorno da NEGACAO, que era a causa medida no frame.
    p = dict(b)
    p[TAKES[0]] = p[TAKES[0]].replace("only movement in the entire shot",
                                      "movement in the shot")
    cegas += 0 if _acusa(p, "AM10") else 1
    p = dict(b)
    p[TAKES[1]] = p[TAKES[1]].replace("Exactly one spoon exists",
                                      "There is one spoon")
    cegas += 0 if _acusa(p, "AM10") else 1
    p = dict(b)
    p[TAKES[1]] = p[TAKES[1]].replace("kneecaps", "knees")
    cegas += 0 if _acusa(p, "AM10") else 1
    # a lista de negacao nao pode VOLTAR a nenhum dos dois
    for _k in (TAKES[0], TAKES[1]):
        p = dict(b)
        p[_k] += (" Do NOT show: the seated man holding a spoon; a spoon "
                  "appearing in the seated man's hand.")
        cegas += 0 if _acusa(p, "AM10") else 1
    # nem uma clausula solta colando colher na mao dele
    p = dict(b)
    p[TAKES[0]] += " No spoon ever appears in his hands at any moment."
    cegas += 0 if _acusa(p, "AM10") else 1
    # ⛔⛔ ESTE CONTROLE JA' FOI INVERTIDO DUAS VEZES EM UM DIA, e o registro
    # das duas fica porque cada volta custou um lote:
    #   1a — exigia que `raising a hand or an arm` NAO estivesse no take 2,
    #        porque o take 2 pedia um joinha e o negativo o contradizia;
    #   2a — com o joinha fora, passou a exigir que ESTIVESSE nos dois;
    #   3a (agora) — exige que NAO esteja em nenhum, porque o frame provou
    #        que a familia inteira de negacao era a causa da colher.
    # ⚠️ A licao sobrevivente e' a terceira e ela e' mais geral que as duas:
    # negar o objeto na mao e' pinta'-lo la'. O que funciona e' ocupar a mao.
    cegas += 0 if not any("raising a hand or an arm" in v
                          for v in b.values()) else 1
    # ⛔ e o joinha nao pode VOLTAR em silencio a nenhum bloco
    cegas += 0 if not any("thumbs-up" in v for v in b.values()) else 1
    # ⛔⛔ O MODO DE TRES TAKES (21/08) — cada copy curta tem de sair com
    # TRES blocos de take, rotulados /03, com a copy INTEIRA no take 3 e o
    # beat de fecho (erguer a garrafa) de volta nele.
    for _cid in ("2", "3", "4"):
        _s3 = sortear("clara", random.Random(13), {}, {"copy": _cid})
        _b3 = montar(_s3)
        _t3 = [k for k in _b3 if k.startswith("TAKE")]
        cegas += 0 if len(_t3) == 3 else 1
        cegas += 0 if all(k.endswith("/03") for k in _t3) else 1
        cegas += 0 if "TAKE 04/04" not in _b3 else 1
        # a copy inteira, verbatim, num take so'
        _alvo = 'Dialogue: "%s"' % sonorizar(_s3["falas"][2])
        cegas += 0 if _alvo in _b3["TAKE 03/03"] else 1
        cegas += 0 if not _s3["falas"][3] else 1
        # o fecho voltou para o take 3, senao o video acaba sem o beat final
        cegas += 0 if "raises the bottle closer to the lens" in \
            _b3["TAKE 03/03"] else 1
        cegas += 0 if not any(nv == "ERRO" for nv, _m in lint(_s3, _b3)) else 1
    # ⛔⛔ A VIRGULA DO CTA (21/08) — tira a pausa e exige a acusacao, nas
    # QUATRO copies, porque a palavra cai em take diferente conforme o modo
    for _cid in "1234":
        _sv = sortear("clara", random.Random(21), {}, {"copy": _cid})
        _bv = montar(_sv)
        _tk = takes_do(_sv)
        # ⛔ ONDE CAIU O CTA E' PERGUNTA, NAO PALPITE. A primeira versao
        # deste controle assumiu *o ultimo take* e acusou a copy 1: la' o
        # CTA esta' no take 3 e o take 4 e' o pedido de follow. Foi
        # literalmente a condicao que ele levantou — *"depende de onde
        # estara' a palavra"*.
        _i = next((k for k in (2, 3)
                   if re.search(r"\byes\b", _sv["falas"][k] or "", re.I)), 2)
        _sv2 = dict(_sv)
        _sv2["falas"] = list(_sv["falas"])
        _sv2["falas"][_i] = _sv["falas"][_i].replace(", yes,", " yes")
        cegas += 0 if _acusa(_bv, "sem virgula dos", _sv2) else 1
        # e o estado certo NAO acusa
        cegas += 0 if not _acusa(_bv, "sem virgula dos", _sv) else 1
        # a palavra sai minuscula e entre virgulas no bloco entregue
        cegas += 0 if ", yes," in _bv[_tk[_i]] else 1
    # ⛔ e a copy 1 (34 palavras) NAO pode cair no modo de tres
    _s4 = sortear("clara", random.Random(13), {}, {"copy": "1"})
    cegas += 0 if len(takes_do(_s4)) == 4 else 1
    # ⛔ o fecho nao pode aparecer DUAS vezes quando ha' quatro takes
    _b4 = montar(_s4)
    cegas += 0 if "raises the bottle closer to the lens" not in \
        _b4["TAKE 03/04"] else 1
    # ⛔⛔ O NEGATIVO QUE SE CONTRADIZ: planta a lista incondicional de volta
    # num sorteio de sujeito CARECA e exige a acusacao
    _sc = sortear("clara", random.Random(2), {}, {"sujeito": "careca",
                                                 "sexo_sujeito": "homem"})
    _bc = montar(_sc)
    p = dict(_bc)
    p[IMAGENS[0]] = p[IMAGENS[0]].replace(
        "Do NOT include: a clean-shaven face",
        "Do NOT include: a bald or shaved head; a clean-shaven face")
    cegas += 0 if _acusa(p, "AM13", _sc) else 1
    cegas += 0 if not _acusa(_bc, "AM13", _sc) else 1
    # e o sujeito de OCULOS nao pode levar `glasses that were not described`
    _sg = sortear("clara", random.Random(2), {}, {"sujeito": "calvo_oculos",
                                                 "sexo_sujeito": "homem"})
    cegas += 0 if not _acusa(montar(_sg), "AM13", _sg) else 1
    # ⛔⛔ O PISO DE 50 ANOS (23/08) — plantar um jovem tem de acusar
    _gi = SUJEITOS_H[0]["idade"]
    SUJEITOS_H[0]["idade"] = 34
    cegas += 0 if _acusa(b, "AM17") else 1
    SUJEITOS_H[0]["idade"] = _gi
    cegas += 0 if not _acusa(b, "AM17") else 1
    cegas += 0 if min(x["idade"] for x in SUJEITOS) >= IDADE_MIN_SUJEITO else 1
    # ⛔⛔ A PESSOA COMPOSTA (23/08) — o eixo que substituiu as tribos
    for _sx in ("homem", "mulher"):
        for _pl in ("branca", "negra"):
            _sc2 = sortear("clara", random.Random(41), {},
                           {"sexo_sujeito": _sx, "pele_sujeito": _pl})
            _bc2 = montar(_sc2)
            _su = _sc2["sujeito"]
            # os tres campos compostos chegam ao quadro
            for _c in ("rosto", "visual"):
                cegas += 0 if _su[_c] in _bc2[IMAGENS[0]] else 1
            _rr = re.sub(r"^(a|an)\s+", "", _su["roupa"])
            cegas += 0 if _rr in _bc2[IMAGENS[0]] else 1
            # ⚠⚠ A IMAGE 02 NAO RESTATA MAIS A PECA (23/08), e isso e'
            # PROPOSITO, nao esquecimento: o texto aprovado diz `the same
            # garment in the same colour [...] SAME SLEEVE LENGTH`, sem
            # nomear a peca. Foi o que consertou *"o que era camisa curta
            # virou camisa de manga longa"* — repetir a descricao dava ao
            # gerador uma segunda chance de redesenhar.
            # ⭐ E tem um ganho medido de brinde: as 15 entradas dos pools
            # que descrevem a peca como folgada (`with the cuffs unbuttoned
            # and hanging loose`) deixaram de chegar ao quadro que precisa
            # desenhar roupa justa.
            cegas += 0 if _rr not in _bc2[IMAGENS[1]] else 1
            for _lit in ("taken in by a tailor", "SAME SLEEVE LENGTH",
                         "SAME LEG LENGTH"):
                cegas += 0 if _lit in _bc2[IMAGENS[1]] else 1
            # e nenhuma lente reclama da pessoa composta
            cegas += 0 if not any(nv == "ERRO"
                                  for nv, _m in lint(_sc2, _bc2)) else 1
    # ⛔ e a variedade e MEDIDA: 200 sorteios, quantas pessoas repetidas?
    _rng2 = random.Random(77)
    _vistos2 = set()
    for _i in range(200):
        _sx2 = sortear("clara", _rng2, {})
        _vistos2.add(_sx2["sujeito"]["id"])
    cegas += 0 if len(_vistos2) >= 198 else 1
    # ⛔ e a PROSA da roupa: `a oatmeal` saia em 5% dos sorteios
    _art_ruim = 0
    _rng3 = random.Random(78)
    for _i in range(300):
        _sx3 = sortear("clara", _rng3, {})
        if re.search(r"a [aeiou]", _sx3["sujeito"]["roupa"], re.I):
            _art_ruim += 1
    cegas += 0 if _art_ruim == 0 else 1
    # controle negativo: uma cor de vogal tem de sair com `an`
    _cv = [x for x in CORES_E_PADROES
           if x.get("tipo") == "cor" and x["en"][:1].lower() in "aeio"]
    cegas += 0 if _cv else 1
    # ⛔⛔ QUEM NARRA NA IMAGE 03 (23/08) — o gerador devolvia o SUJEITO
    # SENTADO em 3 de 4. As tres ancoras positivas tem de estar la, e a
    # negacao antiga NAO pode voltar.
    for _nid in ("vovo_amish", "vovo_amish_h", "root_doctor",
                 "granny_apalache", "freira"):
        _sq = sortear("clara", random.Random(29), {}, {"narrador": _nid})
        _bq = montar(_sq)
        _b3q = _bq[IMAGENS[2]]
        # a posicao na base, a contagem e a descricao inteira
        cegas += 0 if "person who was STANDING" in _b3q else 1
        cegas += 0 if "the only person in this image" in _b3q else 1
        cegas += 0 if _nar_desc(_sq)[:60] in _b3q else 1
        # o pronome acompanha o sexo do narrador
        _esp = "he is the only" if _sq["narrador"]["sexo"] == "m"             else "she is the only"
        cegas += 0 if _esp in _b3q else 1
        # e a pessoa sentada nao e' nomeada num quadro em que ela nao esta
        cegas += 0 if not re.search(r"seated (?:person|man|woman)",
                                    _b3q, re.I) else 1
        cegas += 0 if not _acusa(_bq, "AM8", _sq) else 1
        # plantando a volta da negacao antiga, a AM8 tem de acusar
        p = dict(_bq)
        p[IMAGENS[2]] = p[IMAGENS[2]].replace(
            "the only person in this image",
            "there. The seated person from the base image is no longer in "
            "frame")
        cegas += 0 if _acusa(p, "AM8", _sq) else 1
    # ⭐⭐ A BEBIDA SEGUE A VOCACAO (22/08) — cada narrador, a sua
    for _n in NARRADORES:
        _sr = sortear("clara", random.Random(23), {}, {"narrador": _n["id"],
                                                       "copy": "2"})
        _fala = " ".join(x for x in _sr["falas"] if x)
        cegas += 0 if _n["receita"] in _fala else 1
        if _n["receita"] != "Amish":
            cegas += 0 if "Amish" not in _fala else 1
        cegas += 0 if not _acusa(montar(_sr), "AM15", _sr) else 1
        # e a copy curta continua cabendo em TRES takes
        cegas += 0 if len(takes_do(_sr)) == 3 else 1
    # narrador sem `receita` declarada tem de ser acusado
    _g = NARRADORES[0].pop("receita")
    cegas += 0 if _acusa(b, "AM15") else 1
    NARRADORES[0]["receita"] = _g
    # ⛔⛔ SO' ENGOLE, NAO MASTIGA (22/08) — enfraquecer a trava acusa, e
    # escrever `chew` acusa mesmo negado
    for _k in takes_do(s)[:2]:
        p = dict(b)
        p[_k] = p[_k].replace("SINGLE swallow", "swallow")
        cegas += 0 if _acusa(p, "AM10") else 1
        p = dict(b)
        p[_k] = p[_k].replace("jaw and lips stay still", "jaw relaxes")
        cegas += 0 if _acusa(p, "AM10") else 1
        p = dict(b)
        p[_k] += " Do NOT show: the seated man chewing."
        cegas += 0 if _acusa(p, "AM10") else 1
    # e o estado certo nao acusa
    cegas += 0 if not _acusa(b, "SINGLE swallow") else 1
    # ⛔ os tres narradores removidos nao podem VOLTAR em silencio
    _ids = {n["id"] for n in NARRADORES}
    cegas += 0 if not (_ids & {"doutora", "doutor", "moca_verao"}) else 1
    # ⛔ e as tres identidades novas dizem o SEXO no rotulo (ordem de 22/08)
    for _nid in ("granny_apalache", "freira", "root_doctor"):
        _r = _por_id(NARRADORES, _nid)["rotulo"]
        cegas += 0 if ("MULHER" in _r or "HOMEM" in _r) else 1
    # ⛔⛔ AS TRES IDENTIDADES NOVAS (21/08) — o mundo tem de acompanhar
    for _nid, _mundo, _traco in (("granny_apalache", "apalache", "granny woman"),
                                 ("freira", "convento", "black habit"),
                                 ("root_doctor", "gullah", "sweetgrass")):
        _sn2 = sortear("clara", random.Random(17), {}, {"narrador": _nid})
        _bn2 = montar(_sn2)
        # o cenario sorteado e' do mundo dela
        cegas += 0 if _sn2["cenario"]["mundo"] == _mundo else 1
        # a roupa tipica chega ao quadro — e' o que torna a vocacao legivel
        cegas += 0 if _traco in _bn2[IMAGENS[0]] else 1
        # e o estado certo nao acusa
        cegas += 0 if not _acusa(_bn2, "AM14", _sn2) else 1
        # planto um cenario de OUTRO mundo: a AM14 tem de acusar
        _sx = dict(_sn2)
        _sx["cenario"] = [c for c in CENARIOS
                          if c.get("mundo", "amish") != _mundo][0]
        cegas += 0 if _acusa(_bn2, "AM14", _sx) else 1
        # travar cenario de outro mundo => a trava do NARRADOR ganha e avisa
        _st = sortear("clara", random.Random(17), {},
                      {"narrador": _nid, "cenario": "celeiro_bandeira"}) \
            if _mundo != "amish" else _sn2
        cegas += 0 if _st["cenario"]["mundo"] == _mundo else 1
        cegas += 0 if _st["avisos"] else 1
    # ⛔ a pele fixa nova (Black American) tem de CHEGAR ao quadro — com o
    # mapa antigo a AM7 procurava `African` e acusaria 100% dos videos dela
    _sg2 = sortear("clara", random.Random(17), {}, {"narrador": "root_doctor"})
    cegas += 0 if "Black American" in montar(_sg2)[IMAGENS[0]] else 1
    cegas += 0 if not _acusa(montar(_sg2), "AM7", _sg2) else 1
    # ⛔ e a freira NAO leva cor de vestido sorteada (o habito e preto)
    _sf2 = sortear("clara", random.Random(17), {}, {"narrador": "freira"})
    cegas += 0 if _sf2["cor_vestido"] not in _nar_desc(_sf2) else 1
    # ⛔⛔ A COERENCIA DE PELE (lote de 21/08 — a trava negra que nao pegava)
    # planta o ruivo como se ele valesse em negra: a lente tem de acusar
    _guardado = SUJEITOS_H[4]["pele"]
    SUJEITOS_H[4]["pele"] = ("branca", "negra")
    cegas += 0 if _acusa(b, "AM12") else 1
    SUJEITOS_H[4]["pele"] = _guardado
    # e planta a coloracao europeia direto no bloco de um sujeito negro
    _sn = sortear("clara", random.Random(3), {}, {"pele_sujeito": "negra",
                                                 "sexo_sujeito": "homem"})
    _bn = montar(_sn)
    if _sn["pele_sujeito"] == PELES["negra"]:
        # ⛔ o plantio mudou de lugar em 22/08 junto com a lente: ela le o
        # CAMPO do sujeito, nao o texto do bloco, entao sujar o bloco nao
        # acusa mais — e um controle que planta onde a lente nao olha e
        # controle cego.
        _sujo = dict(_sn)
        _sujo["sujeito"] = dict(_sn["sujeito"])
        _sujo["sujeito"]["visual"] = (_sn["sujeito"]["visual"]
                                      + " and pale freckled skin")
        cegas += 0 if _acusa(_bn, "AM12", _sujo) else 1
        cegas += 0 if not _acusa(_bn, "AM12", _sn) else 1
    else:
        cegas += 2   # a trava nem foi honrada: falha dupla
    # ⛔⛔ AS ANCORAS DA BARRIGA EM DOBRO (prompt carimbado em 21/08)
    for _lit, _fraco in (
            ("fills the entire lower half of the frame", "is very large"),
            ("until it rests on the ground", "past the knees"),
            ("the very largest super-heavyweight sumo wrestler in the world",
             "a super-heavyweight sumo wrestler"),
            ("completely hiding", "partly hiding")):
        p = dict(b)
        p[IMAGENS[0]] = p[IMAGENS[0]].replace(_lit, _fraco)
        cegas += 0 if _acusa(p, "AM9") else 1
    # ⛔ e o peso nao pode cair de volta para a faixa antiga
    _s = dict(s)
    _s["peso_kg"] = 260
    cegas += 0 if _acusa(b, "AM9", _s) else 1
    # ⛔ a faixa de barriga nua nao pode voltar (ordem de 21/08)
    p = dict(b)
    p[IMAGENS[0]] = p[IMAGENS[0]].replace(
        "the whole belly stays inside the shirt",
        "only a small strip of bare belly shows above the waistband")
    cegas += 0 if _acusa(p, "AM9") else 1
    # ⛔ maos nos JOELHOS, nunca nas coxas (recusa de politica de 21/08)
    # ⚠️ A palavra `thigh` SOZINHA nao serve — quarta vez hoje que colo um
    # controle num literal cru e ele acusa o certo. Ela e' legitima em duas
    # descricoes de corpo que o operador aprovou em sete rodadas de teste:
    # `upper arms as thick as thighs` (o obeso) e `the thighs and calves are
    # now slim` (o magro). O que saiu foi a MAO na coxa, e e' so' isso que
    # este controle pode cobrar.
    cegas += 0 if not any(re.search(r"(?:on|over) (?:his|her|the) thigh", v)
                          for v in b.values()) else 1
    # ⛔ e a garrafa e' do NARRADOR, dito com todas as letras
    cegas += 0 if all("The narrator keeps" in b[k] for k in TAKES) else 1
    p = dict(b)
    p[TAKES[2]] = p[TAKES[2]].replace("never leaves", "sometimes leaves")
    cegas += 0 if _acusa(p, "AM10") else 1
    p = dict(b)
    p[TAKES[3]] = p[TAKES[3]].replace("Exactly two hands", "Some hands")
    cegas += 0 if _acusa(p, "AM10") else 1
    p = dict(b)
    p[TAKES[2]] = p[TAKES[2]].replace("comment", "type")
    cegas += 0 if _acusa(p, "AM2") else 1
    # ⛔⛔ A CARROCA EM LOOPING — o defeito que ele filmou em 21/08. Planto o
    # `vida` antigo de volta na pool e exijo que a AM11 acuse; depois tiro a
    # trava de fundo parado de cada take, um por um.
    _guardado = CENARIOS[1]["vida"]
    CENARIOS[1]["vida"] = "the loaded hay wagon creaks slowly past behind them"
    cegas += 0 if _acusa(b, "AM11") else 1
    CENARIOS[1]["vida"] = _guardado
    _guardado = CENARIOS[5]["desc"]
    CENARIOS[5]["desc"] = "a mule cart passing on the dirt lane"
    cegas += 0 if _acusa(b, "AM11") else 1
    CENARIOS[5]["desc"] = _guardado
    # ⚠️ e a pool limpa NAO pode acusar: lente que grita no estado certo
    # ensina o operador a ignorar a lente
    cegas += 0 if not _acusa(b, "AM11") else 1
    for _k in TAKES:
        p = dict(b)
        p[_k] = p[_k].replace("The background holds perfectly still",
                              "The background is alive")
        cegas += 0 if _acusa(p, "AM11") else 1
    p = dict(b)
    p[IMAGENS[0]] += " Ordinary face, not a celebrity."
    cegas += 0 if _acusa(p, "anticeleb") else 1
    p = dict(b)
    p[TAKES[0]] += '\nDialogue: "hello there"'
    cegas += 0 if _acusa(p, "AM4") else 1
    p = dict(b)
    p[TAKES[0]] += " " + sc.SEM_TEXTO_TAKE
    cegas += 0 if _acusa(p, "AM4") else 1
    p = dict(b)
    p[TAKES[3]] = p[TAKES[3]].replace("Dialogue:", "Fala:")
    cegas += 0 if _acusa(p, "AM4") else 1
    s2 = dict(s, sexo_sujeito=("mulher" if s["sexo_sujeito"] == "homem"
                               else "homem"))
    if s["copy"]["id"] in ("c1", "c3"):
        cegas += 0 if _acusa(b, "AM5", spec=s2) else 1
    p = dict(b)
    p[IMAGENS[1]] = p[IMAGENS[1]].replace("the very same", "a new")
    cegas += 0 if _acusa(p, "AM8") else 1
    # ⛔⛔ OS CINCO DEFEITOS QUE ELE FILMOU, PLANTADOS UM A UM (23/08)
    for _de, _para, _lente in (
            ("stomach is flat", "stomach is smaller", "AM8"),
            ("knees are bony", "knees are slimmer", "AM8"),
            ("taken in by a tailor", "in a smaller size", "AM8"),
            ("SAME SLEEVE LENGTH", "a comfortable sleeve length", "AM8"),
            ("SAME LEG LENGTH", "a comfortable leg length", "AM8"),
            ("knees together and pointing forward",
             "knees apart and pointing outward", "AM8"),
            ("slim from head to feet", "slimmer around the middle", "AM8")):
        p = dict(b)
        p[IMAGENS[1]] = p[IMAGENS[1]].replace(_de, _para)
        cegas += 0 if _acusa(p, _lente) else 1
    # ⛔⛔ A ROUPA LARGA E A NEGACAO DE CORPO — os dois caminhos da AM20
    for _veneno in ("the shirt stays loose on the body",
                    "the sleeves are left hanging",
                    "there is no belly and no double chin"):
        p = dict(b)
        p[IMAGENS[1]] = p[IMAGENS[1]] + " " + _veneno
        cegas += 0 if _acusa(p, "AM20") else 1
    # ⛔⛔ A ATMOSFERA — planta poeira no `vida` de um cenario e a negacao
    # de poeira num quadro. Os dois tem de acusar.
    _g = CENARIOS[0]["vida"]
    CENARIOS[0]["vida"] = "fine dust drifts across the yard"
    cegas += 0 if _acusa(b, "AM19") else 1
    CENARIOS[0]["vida"] = _g
    p = dict(b)
    p[IMAGENS[0]] = p[IMAGENS[0]] + " There is no dust in the air."
    cegas += 0 if _acusa(p, "AM19") else 1
    for _n in (IMAGENS[0], IMAGENS[1], IMAGENS[2]):
        p = dict(b)
        p[_n] = p[_n].replace(AR_LIMPO_IMG, "")
        cegas += 0 if _acusa(p, "AM19") else 1
    p = dict(b)
    p[IMAGENS[2]] = p[IMAGENS[2]].replace("Using the provided image",
                                          "A fresh new scene")
    cegas += 0 if _acusa(p, "AM8") else 1
    # ⛔ o REF nao pode voltar em silencio — a ordem foi tira'-lo
    cegas += 0 if "BLOCO 0 (REF)" not in b else 1
    # ⛔ o prompt negativo e' pedido explicito de 21/08 — e vale para as
    # IMAGEs 01 e 03, que descrevem rosto e cabelo.
    # ⛔⛔ A IMAGE 02 FICOU DE FORA EM 23/08, e o motivo esta' medido: a lista
    # dela (`Do NOT include: [...] any remaining belly [...] oversized clothes
    # hanging loose`) punha `loose` 415 vezes, `hanging` 409 e `oversized` 201
    # em 200 sorteios — 100% dos prompts — no unico quadro cuja tarefa e'
    # desenhar roupa JUSTA num corpo MAGRO. Era o defeito, nao a defesa.
    for _i in (0, 2):
        cegas += 0 if "Do NOT include" in b[IMAGENS[_i]] else 1
    cegas += 0 if "Do NOT include" not in b[IMAGENS[1]] else 1
    p = dict(b)
    p[IMAGENS[0]] = p[IMAGENS[0]].replace(
        "exactly %d pounds" % s["peso_lb"], "quite heavy")
    cegas += 0 if _acusa(p, "AM9") else 1
    p = dict(b)
    p[IMAGENS[0]] = p[IMAGENS[0]].replace(
        "super-heavyweight sumo wrestler", "large man")
    cegas += 0 if _acusa(p, "AM9") else 1
    p = dict(b)
    p[IMAGENS[0]] = p[IMAGENS[0]].replace(
        "sitting upright in a relaxed, normal posture", "leaning far back")
    cegas += 0 if _acusa(p, "AM9") else 1
    p = dict(b)
    p[IMAGENS[0]] += " He is an obese man."
    cegas += 0 if _acusa(p, "AM9") else 1
    print("  controles negativos ..... %s"
          % ("todos acusam" if not cegas else "%d CEGO(S)" % cegas))

    ok = not erros and not falha_alcance and not falha_trava and not cegas
    print("\n%s" % ("AUTOTESTE OK" if ok else "AUTOTESTE REPROVADO"))
    return 0 if ok else 1


def stats(n=400):
    print("%s — %d narradores · %d sujeitos (%dH/%dM) · %d cenarios · "
          "%d estilos DAY · %d copies · dias %d-%d"
          % (TITULO, len(NARRADORES), len(SUJEITOS), len(SUJEITOS_H),
             len(SUJEITOS_M), len(CENARIOS), len(ESTILOS_DAY), len(COPIES),
             DIA_MIN, DIA_MAX))
    for c in COPIES:
        print("  %-40s %2d palavras%s"
              % (c["rotulo"],
                 _palavras(c["en"] % {"obj": "him", "nome": "Johnny"}),
                 "  <-- excecao declarada (34, fonte 331k)"
                 if c["id"] == "c1" else ""))
    return autoteste(n)


# ===========================================================================
def main():
    ap = argparse.ArgumentParser(description=TITULO)
    ap.add_argument("--pagina", choices=sorted(ETNIA), default="clara")
    ap.add_argument("--n", type=int, default=1)
    ap.add_argument("--seed", type=int)
    ap.add_argument("--narrador", choices=[x["id"] for x in NARRADORES])
    ap.add_argument("--copy", choices=["1", "2", "3", "4"])
    ap.add_argument("--sexo", choices=["homem", "mulher"])
    ap.add_argument("--pele-narrador", choices=sorted(PELES))
    ap.add_argument("--pele-sujeito", choices=sorted(PELES))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--autoteste", action="store_true")
    ap.add_argument("--stats", action="store_true")
    a = ap.parse_args()

    if a.autoteste:
        return autoteste()
    if a.stats:
        return stats()

    led = _carregar_ledger()
    rng = random.Random(a.seed)
    travas = {}
    if a.narrador:
        travas["narrador"] = a.narrador
    if a.copy:
        travas["copy"] = a.copy
    if a.sexo:
        travas["sexo_sujeito"] = a.sexo
    if a.pele_narrador:
        travas["pele_narrador"] = a.pele_narrador
    if a.pele_sujeito:
        travas["pele_sujeito"] = a.pele_sujeito

    for _ in range(a.n):
        s = sortear(a.pagina, rng, led, travas)
        b = montar(s)
        print("=" * 70)
        print(resumo_pt(s))
        print("=" * 70)
        for k in [x for par in zip(IMAGENS, TAKES) for x in par]:
            print("\n%s\n" % b[k])
        for nivel, msg in lint(s, b):
            print("[%s] %s" % (nivel, msg))
        if not a.dry_run:
            _gravar_ledger(led, s)
    return 0


if __name__ == "__main__":
    sys.exit(main())
