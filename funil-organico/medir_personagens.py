# -*- coding: utf-8 -*-
"""Mede a DIVERSIDADE DESCRITIVA dos pools de personagem dos motores.

    python funil-organico/medir_personagens.py            # relatorio
    python funil-organico/medir_personagens.py --gate      # sai 1 se houver ZERO
    python funil-organico/medir_personagens.py --arquivo troca_short.py

POR QUE ESTE ARQUIVO EXISTE (2026-08-02). O operador reclamou que os agentes
geravam sempre a mesma cara: "seu repertorio de personagens esta fraquissimo".
A contagem de entradas nao mostrava nada de errado — os pools tinham 8, 9, 14
opcoes. O defeito estava em OUTRA dimensao: as entradas descreviam a pessoa
so' por CABELO. Dez homens descritos so' por cabelo sao o mesmo homem dez
vezes, e o gerador devolve o mesmo rosto.

Entao a metrica nao e' "quantas entradas o pool tem" (isso o medir_vicio.py
mede) e sim "quantos EIXOS FISICOS as entradas realmente acionam".

⛔ EIXO COM ZERO MENCOES E' REPROVACAO. Todo motor novo passa por aqui antes
de virar .exe — e' o gate de personagem do checklist de licoes-de-construcao.

⚠️ ESTE MEDIDOR JA' MENTIU UMA VEZ. A v1 acusou 41 eixos zerados e 22 eram
FALSO POSITIVO:
  · FIGURANTES do ESCANDALO e' (1, 2) — a CONTAGEM de figurantes, nao gente.
    Por isso o e_pool_de_gente(): pool sem texto descritivo nao e' pool de
    personagem so' porque o NOME parece.
  · pool de mulher nao tem pelo facial. Cobrar isso e' cobrar barba de mulher.
  · o PRISMA decompoe o REF em REF_IDADES x REF_FISICOS x REF_MARCAS, que se
    COMBINAM no sorteio: cada pool sozinho e' magro por construcao, o PRODUTO
    e' que precisa cobrir os eixos.
Linter que reprova o que esta' certo nunca foi testado — vale para o medidor
igual vale para o motor (licoes-de-construcao §linter contra template).
"""
import argparse
import ast
import io
import os
import re
import sys

FO = os.path.dirname(os.path.abspath(__file__))

# ⛔⛔ SAIDA EM UTF-8, SEMPRE. O console do Windows e' cp1252 e nao imprime os
# marcadores deste arquivo. Isto ja' foi remendado emoji a emoji e VOLTOU no
# primeiro merge — por isso agora e' no topo, uma linha que cobre todo print
# presente e futuro.
# ⚠️ O padrao que faz o bug ser caro: os prints com marcador so' rodam QUANDO HA'
# ALGO A REPORTAR. O crash acontece exatamente na hora em que a mensagem
# importa, e nunca no caminho feliz — foi assim que o aviso de "excecao
# declarada que nao esta' mais zerada" ficou invisivel duas vezes.
for _f in (sys.stdout, sys.stderr):
    try:
        _f.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

# os eixos que fazem duas pessoas parecerem diferentes num plano medio.
# ⛔ nao existe eixo de ETNIA aqui de proposito: etnia e' injetada por pagina
# pelo dict ETNIA do motor (congruencia com o avatar), nunca pela descricao.
# ⚠️ prefixo termina em \w* de proposito. A v3 escrevia "freckl" dentro de
# \b(...)\b e por isso NUNCA casava com "freckles" nem "freckled" — o eixo pele
# do organicwave aparecia zerado com as tres entradas preenchidas.
EIXOS = {
    "cabelo":  r"\b(hair|bald\w*|buzz|crew.?cut|ponytail|braid\w*|dreadlock\w*|"
               r"afro|topknot|bun|shaved head|receding|comb-?over|curls?|locs|"
               r"perm\w*|pixie|bob|fringe|mane|shag|flat-?top|taper|hairline)\b",
    "pelo_facial": r"\b(beard\w*|mustache\w*|moustache\w*|goatee|stubble|"
               r"sideburns|muttonchop\w*|clean-?shaven|whiskers|chin.?strap|"
               r"chevron|walrus)\b",
    "oculos":  r"\b(glasses|spectacles|bifocal\w*|readers|shades|lenses|"
               r"rimless|half-?rim|half-?moon|wire-?rimmed|wire-?frame\w*|"
               r"sunglasses|clip-?on)\b",
    "porte":   r"\b(heavy-?set|stocky|thin|lean|bony|barrel-?chested|burly|"
               r"wiry|slight|paunch\w*|round-?faced|tall|short|stout|gaunt|"
               r"husky|compact|rangy|solid|thickset|petite|small-?framed|"
               r"long-?limbed|full-?figured|slim|trim|broad-?shouldered|"
               r"heavy through|broad shoulders|sloping shoulders|wide hips|"
               r"narrow waist|swimmer's shoulders|narrow build|square frame|"
               r"\w+ frame|\w+ build)\b",
    # ⛔ "olive" e "fair" sairam: casavam com COR DE ROUPA ("olive summer
    # dress") e davam eixo de pele preenchido onde nao havia pele nenhuma.
    # ⛔ "dark-skinned" saiu porque etnia nao entra por descricao (vem do
    # dict ETNIA por pagina) — cobrar isso seria cobrar a regra ao contrario.
    "pele":    r"\b(freckl\w*|weathered|sun-?weathered|leathery|lined|ruddy|"
               r"sallow|pockmarked|smooth-?skinned|deeply lined|creased|"
               r"sun-?spotted|age spots?|liver-?spotted|laugh lines|"
               r"lines fanning|tan\w* from|tanned)\b",
    # ancora facial permanente (P6) — e' o que faz o rosto VOLTAR igual na
    # cena seguinte. ⛔ so' do lado distintivo: cicatriz limpa, mecha, pinta.
    # dente lascado / palpebra caida viram mendigo e matam a credibilidade
    # (licoes-producao-veo §REF — DISTINTIVO, NUNCA DETERIORADO).
    "ancora":  r"\b(scars?|birthmark\w*|moles?|streak\w*|notched|dimple\w*|"
               r"cleft|gap between|beauty mark|crown|stud|hoop|"
               r"patch of white|white streak|silver streak)\b",
}

# ⭐ CONTROLES DO PROPRIO MEDIDOR. Este arquivo ja' mentiu TRES vezes (ver
# cabecalho). Cada eixo carrega frases que TEM de casar e frases que NAO podem
# casar — as negativas sao os falsos positivos reais que ja' aconteceram.
# `--autoteste` roda isso; o --gate roda antes de medir qualquer coisa.
CONTROLES = {
    "pele":   ([u"a dense spray of dark freckles",
                u"skin tanned and freckled from the sun",
                u"dark age spots across his right temple",
                u"deep laugh lines around her mouth"],
               [u"a fitted olive summer dress", u"a rose-pink cardigan"]),
    "porte":  ([u"petite and small-framed",
                u"broad shoulders and clear definition in her arms",
                u"wide hips and a narrow waist",
                u"broad-shouldered with strong arms",
                u"a tall rangy frame"],
               [u"a wide brush mustache", u"a broad square jaw"]),
    "cabelo": ([u"thin white hair set in tight permed curls",
                u"a high messy topknot", u"a cropped platinum pixie cut"],
               [u"thick black-framed glasses"]),
    "oculos": ([u"half-moon reading glasses low on her nose",
                u"thin gold wire-rimmed glasses",
                u"sunglasses pushed up on her head"],
               [u"a fitted denim shirtdress"]),
    "pelo_facial": ([u"a full snow-white walrus mustache", u"close grey stubble",
                     u"thick rust-red sideburns"],
                    [u"a heavy gray-brown mop combed forward"]),
    "ancora": ([u"a thin scar through her right eyebrow",
                u"a coin-sized dark birthmark on his crown",
                u"a wide gap between her front teeth"],
               [u"a printed housedress"]),
}


def autoteste():
    """Falha ANTES de medir se algum eixo voltou a mentir. Devolve nº de falhas."""
    falhas = 0
    for eixo, (devem, nao_devem) in sorted(CONTROLES.items()):
        for frase in devem:
            if not re.search(EIXOS[eixo], frase, re.I):
                print("  AUTOTESTE FALHOU  %-12s deveria casar: %r" % (eixo, frase))
                falhas += 1
        for frase in nao_devem:
            achado = re.search(EIXOS[eixo], frase, re.I)
            if achado:
                print("  AUTOTESTE FALHOU  %-12s nao podia casar %r (casou %r)"
                      % (eixo, frase, achado.group(0)))
                falhas += 1
    print("autoteste do medidor: %s" % ("%d falha(s)" % falhas if falhas else "ok"))
    return falhas

# ⚠️ o sufixo opcional NAO e' enfeite. A v2 deste regex terminava em ")$" e por
# isso era CEGA para HOMENS_CLARA, CORPOS_PROVA_ESCURA e REFS_H_CLARA — ou seja,
# o elenco masculino do ESCANDALO, do TROCA e do ORGANICWAVE inteiro nunca foi
# medido, e o organicwave_short.py nao aparecia UMA VEZ no relatorio. Gate que
# nao ve o pool nao reprova o pool: ele so' produz um "passou" mentiroso.
NOMES_DE_POOL = re.compile(
    r"^(REFS?|REF|HOMENS|MULHERES|NARRADORAS?|NARRADORES?|VITIMAS?|"
    r"ARQUETIPOS?|PACIENTES?|FIGURANTES?|PLATEIA|TESTEMUNHAS?|CORPOS?_PROVA|"
    r"MONTANHESES?|ESPECIALISTAS?)(_[A-Z_]+)?$")

# pools que se COMBINAM no sorteio — medir o produto, nao as partes
COMBINAM = {"randomizador-prisma.py": ["REF_IDADES", "REF_FISICOS", "REF_MARCAS"]}

# ⭐ ZEROS QUE SUSTENTAM REGRA. Nem todo eixo vazio e' pobreza: em alguns pools
# o vazio E' a regra, e preencher DESTROI o contraste que faz o video funcionar.
# Gate que berra pra sempre e' gate que ninguem le' — entao esses saem da
# reprovacao e aparecem rotulados. Cada linha citou o codigo que a sustenta.
# ⛔ so' entra aqui zero VERIFICADO no arquivo, nunca zero que deu trabalho.
# ⚠️ AS CHAVES MUDARAM DE ARQUIVO EM 2026-08-03. Os pools moraram nos `*_lucas`
# ate' o desacoplamento; agora vivem nos `_short`, que sao a fonte da verdade.
# A regra que cada excecao sustenta nao mudou uma virgula — so' o endereco.
EXCECOES = {
    ("flagrante_short.py", "REFS", "pelo_facial"):
        "F4b — o REF e' barbeado e sem oculos DE PROPOSITO: careca+bigode+"
        "oculos e' o que marca a VITIMA. Encher aqui apaga o contraste que "
        "separa os dois no plano medio.",
    ("flagrante_short.py", "REFS", "oculos"): "idem F4b",
    ("pee_short.py", "REFS", "pelo_facial"): "idem F4b/PE9 — o PEE herda o contraste",
    ("pee_short.py", "REFS", "oculos"): "idem F4b/PE9",
    ("vazamento_short.py", "REFS", "pelo_facial"):
        "o BLOCO 0 ja' renderiza `clean-shaven` em string TRAVADA — barba no "
        "pool contradiria o proprio prompt.",
    ("necrose_short.py", "ARQUETIPOS", "pelo_facial"):
        "NE5 — ARQUETIPOS e' cenario+chapeu+animal. O rosto mora em REFS.",
    ("necrose_short.py", "ARQUETIPOS", "oculos"): "idem NE5",
    ("exterior_short.py", "HOMENS_SEM_ROSTO", "cabelo"):
        "EX5 — geometria travada do IMAGE 01: ele entra CORTADO NO PEITO, sem "
        "rosto em quadro. E' a economia que justifica o agente — um rosto a "
        "menos para manter identico entre tres blocos de 8s gerados "
        "separadamente. Encher este eixo e' desenhar o que a decisao de projeto "
        "tirou do enquadramento. Os tres eixos que sobram (porte 12/12, pele "
        "12/12, ancora 12/12) sao os unicos que o espectador ve'.",
    ("exterior_short.py", "HOMENS_SEM_ROSTO", "pelo_facial"): "idem EX5",
    ("exterior_short.py", "HOMENS_SEM_ROSTO", "oculos"): "idem EX5",
    # ⭐ EXTERIOR 16 (2026-08-08) — mesmo corte no peito, mesma razao. O
    # motor nasceu por copia literal do de 24s: a cena fundida herdou o
    # quadro da cena 3, onde ele entra cortado no peito segurando o geoduck
    # limpo. Cobrar cabelo, barba ou oculos de um personagem que NAO TEM
    # CABECA em quadro e' cobrar o que a cena proibe.
    ("exterior16_short.py", "HOMENS_SEM_ROSTO", "cabelo"):
        "idem EX5 do exterior_short — corte no peito, sem rosto em quadro",
    ("exterior16_short.py", "HOMENS_SEM_ROSTO", "pelo_facial"): "idem EX5",
    ("exterior16_short.py", "HOMENS_SEM_ROSTO", "oculos"): "idem EX5",
    # ⛔ COLO — o corte e' MAIS ALTO que o do EXTERIOR: la' e' no peito, aqui e'
    # na CINTURA. Nao ha' cabeca, nao ha' tronco, nao ha' rosto — so' pernas e
    # maos. Cobrar cabelo, barba, oculos ou pele DE ROSTO de um personagem que
    # nao tem cabeca em quadro e' o medidor pedindo para desenhar o que a
    # decisao de projeto tirou do enquadramento.
    # ⚠️ E ele NAO fica sem identidade: como nao ha' rosto, a ancora migrou para
    # a MAO e a CALCA (aliança, cicatriz no dorso, relogio, unha marcada,
    # tatuagem no pulso), que sao a unica pele dele em quadro. O eixo `porte`
    # continua sendo cobrado e continua cheio.
    # ⛔ COLO 16 herda os pools por copia literal.
    ("colo16_short.py", "HOMENS", "cabelo"):
        "herdado do colo_short.py por copia literal.",
    ("colo16_short.py", "HOMENS", "pelo_facial"):
        "herdado do colo_short.py por copia literal.",
    ("colo16_short.py", "HOMENS", "oculos"):
        "herdado do colo_short.py por copia literal.",
    ("colo16_short.py", "NARRADORAS", "oculos"):
        "herdado do colo_short.py por copia literal.",
    ("colo_short.py", "HOMENS", "cabelo"):
        "CO1/CO13 — o homem entra CORTADO NA CINTURA, sem cabeca e sem tronco "
        "em quadro. A identidade dele mora na mao e na calca, nao no rosto.",
    ("colo_short.py", "HOMENS", "pelo_facial"): "idem CO1/CO13 — sem rosto",
    ("colo_short.py", "HOMENS", "oculos"): "idem CO1/CO13 — sem rosto",
    # ⛔ COLO — LEI DO REF (2026-08-03): *"ref mulheres sempre muito lindas"*.
    # ⚠️ E ESTE EIXO ZERADO E' O REGISTRO DE UM ERRO MEU, o MESMO do
    # RESSURREICAO e cometido de novo dez dias depois: escrevi o pool otimizando
    # para ESTE medidor, que premia oculos e pele marcada, e ele me devolveu
    # narradoras de 40, 42 e 44 anos, grisalhas, de oculos de leitura e "deeply
    # lined skin" — num agente em que ela e' quem vende para homem. O operador
    # viu no lote e mandou reescrever.
    # ⚠️ A ancora facial NAO sumiu: ela migrou para sinal de BELEZA — marca de
    # nascenca, covinha, olho de cor incomum, sarda, falha entre os dentes,
    # malar alto. Distintivo, nunca deteriorado.
    # ⛔ CLEAN e CLEAN V2 — LEI DO REF (2026-08-03): *"quero todos os refs
    # homens musculosos e todas as refs mulheres lindas no agente clean short"*.
    # ⚠️ TERCEIRA VEZ que este medidor PRODUZIU o defeito que deveria pegar: as
    # tres ultimas entradas do REFS_M foram escritas para preencher os eixos
    # `oculos` e `pele` que ele premia, e trouxeram `half-moon reading glasses`,
    # `silver-streaked hair`, `sun-weathered skin` e idade 52 — num agente cuja
    # REF vende para homem. Nota boa, personagem errada.
    # ⚠️ So' o pool FEMININO tem excecao. No REFS_H oculos e grisalho FICAM, e de
    # proposito: no homem eles leem como CREDIBILIDADE, o oposto do efeito nela.
    ("clean_short.py", "REFS_M", "oculos"):
        "LEI DO REF — oculos de leitura brigam frontalmente com 'linda'. Cabelo "
        "e ancora seguem cheios, e o PORTE mora no eixo proprio CORPOS_M "
        "(CL26 desde 2026-08-04: sensual, nunca musculoso).",
    ("clean_short_v2.py", "REFS_M", "oculos"): "idem clean_short",
    # ⛔ FALTA 16 herda o pool HOMENS por copia literal — mesmo contrato.
    ("falta16_short.py", "HOMENS", "pele"):
        "CONTRATO DO MOTOR — identico ao falta_short.py: as entradas do "
        "pool nao carregam adjetivo de etnia, quem injeta e a montagem "
        "a partir do MUNDO sorteado.",
    ("falta_short.py", "HOMENS", "pele"):
        "CONTRATO DO MOTOR — as entradas do pool carregam ZERO adjetivo de "
        "etnia, e quem injeta e' a montagem, a partir do MUNDO sorteado (o "
        "homem sai como '%s man' com a etnia do mundo). E' o mesmo contrato "
        "do pool das mulheres deste agente e do NECROSE/EXTERIOR. Pool com "
        "etnia dentro quebraria a congruencia de mundo, que e' inviolavel "
        "neste funil.",
    # ⛔ FALTA 16 herda o pool REFS do FALTA por copia literal.
    ("falta16_short.py", "REFS", "oculos"):
        "LEI DO REF — mesmo pool e mesma razao do falta_short.py.",
    ("falta_short.py", "REFS", "oculos"):
        "LEI DO REF — este agente nasce em MODO BELA por ordem do operador "
        "(*mulheres extremamente lindas, roupa curta*), e oculos de leitura "
        "brigam frontalmente com isso. Os outros eixos seguem cheios: cabelo, "
        "marca facial, porte e idade. ⚠️ Sao DUAS mulheres em quadro, entao o "
        "eixo que carrega a variacao aqui e' o CABELO — e' o que separa uma da "
        "outra no mesmo frame.",
    ("colo_short.py", "NARRADORAS", "oculos"):
        "LEI DO REF — oculos de leitura brigam frontalmente com 'linda e jovem'. "
        "Os outros eixos continuam cheios (cabelo, porte, pele, ancora).",
    ("ressurreicao_short.py", "NARRADORAS", "oculos"):
        "LEI DO REF (2026-08-03) — neste agente a narradora e' sempre linda, "
        "jovem e de sex appeal alto, por ordem do operador. Oculos de leitura "
        "brigam com isso frontalmente. ⚠️ E este eixo zerado e' o REGISTRO de "
        "um erro meu: a passada de variedade de 02/08 otimizava para ESTE "
        "medidor, que premia oculos e pele marcada — e ele me devolveu "
        "narradoras de 47 e 52 anos, grisalhas e de oculos de leitura, num "
        "agente de nutra sexual. Otimizei a metrica contra o objetivo.",
    # ⛔⛔ ESCANDALO — LEI DO REF (2026-08-04): *"mulheres sempre super fit e
    # lindas nos videos gerados pelo agente short escandalo"*.
    # ⚠️⚠️ QUARTA VEZ que este medidor PRODUZIU o defeito que deveria pegar, e
    # esta foi a pior: o ESCANDALO era o UNICO dos quatro agentes de narradora
    # feminina SEM excecao declarada aqui. Sem ela, o gate reprovava o pool
    # certo — entao em 2026-08-02 eu enchi o pool para passar no gate e ele
    # devolveu narradoras de 44, 47, 50 e 52 anos, grisalhas, de oculos de
    # leitura, com `sun-weathered skin`, `deep laugh lines` e `a notched scar in
    # her upper lip`. O operador viu no lote e mandou reescrever.
    # ⛔ A licao que fica: quando tres agentes irmaos tem excecao e um nao tem,
    # o que falta e' a EXCECAO, nao o conteudo do pool. Consertar so' o pool
    # deixaria o defeito voltar no proximo aceite (licoes-de-construcao §18).
    ("escandalo_short.py", "NARRADORAS", "oculos"):
        "LEI DO REF — oculos de leitura brigam frontalmente com 'super fit e "
        "linda'. Os outros eixos continuam cheios: PORTE atletico em 20/20 "
        "(era 5/20), cabelo e ancora facial de beleza em 100%.",
    # ⛔ RECEITA — LEI DO REF. O pool MULHERES e' a parceira do payoff (cena 3),
    # e a lei vale igual: 30-35 anos, sempre bonita. ⚠️ `pele` NAO entra na
    # excecao — ela esta' em 12/12, so' que sempre como SINAL DE BELEZA
    # (`smooth`, `clear`, `glowing`, `sun-kissed`), nunca como deterioracao.
    # E' a diferenca que os outros tres agentes aprenderam do jeito caro.
    ("receita_short.py", "MULHERES", "oculos"):
        "LEI DO REF — oculos de leitura brigam frontalmente com 'linda'. "
        "Cabelo, porte, pele e ancora facial seguem em 100% do pool.",
    # ⛔ BOTICA — a boticaria e' REF feminina: vale a lei do REF inteira.
    # ⚠️ DECISAO DECLARADA: a FONTE deste agente e' uma mulher de ~40 de oculos,
    # e a autoridade dela vem de PARECER curandeira. Escolhi a lei do operador
    # sobre a fonte — a tradicao entra pelo TRAJE do mundo, nao pelo desgaste do
    # rosto. Se ele preferir o contrario, e' uma linha no pool.
    # ⛔⛔ DUPLA — a lei do REF e' o ANGULO, nao regra herdada. Ordem do
    # operador: "duas mulheres novinhas lindas com vestido mais curto". Um eixo
    # de oculos cheio aqui seria o motor contrariando a propria razao de existir.
    # ⛔ PLACA — mesma razao: a REF e' a bullet de retencao, e o angulo e' a
    # humilhacao publica do corpo dele. Oculos de leitura brigam com "linda".
    # ⛔ PLACA 16 herda o pool REFS por copia literal — mesma razao.
    ("placa16_short.py", "REFS", "oculos"):
        "LEI DO REF — mesmo pool e mesma razao do placa_short.py.",
    ("placa_short.py", "REFS", "oculos"):
        "LEI DO REF — a REF deste angulo e' a bullet de retencao.",
    # ⛔ CHA — a ordem do operador para este agente e' a mais explicita do repo:
    # *"a ref mulher tem que ser extremamente linda e com um corpo muito
    # atrativo, e' imperativo que ela use roupas com muito decote"*. O eixo
    # `oculos` e' o oposto exato do que foi encomendado — zera-lo aqui e' cumprir
    # a regra, nao furar a lente.
    # ⚠️ `pele` esteve declarado aqui e SAIU: os REFS top model variam pele, e a
    # propria lente avisou que a excecao virou letra morta. Excecao que nao e'
    # mais necessaria e' permissao esquecida ligada.
    # ⛔ TRIO — mesma razao: a REF e as duas sentadas sao a bullet de
    # retencao, e o operador pediu "extremamente lindas". Oculos brigam.
    ("trio_short.py", "REFS", "oculos"):
        "LEI DO REF — as tres mulheres sao a bullet de retencao do angulo.",
    # ⛔ TRIO 16 herda o pool REFS do TRIO por copia literal, entao herda a
    # razao inteira. Excecao declarada no dia em que o motor nasceu — deixar o
    # gate vermelho "porque eu sei que e' de proposito" e' como o operador
    # aprende a ignorar o gate.
    ("trio16_short.py", "REFS", "oculos"):
        "LEI DO REF — mesmo pool e mesma razao do trio_short.py.",
    ("cha_short.py", "REFS", "oculos"):
        "LEI DO REF — a REF deste angulo E' a bullet de retencao do hook.",
    ("dupla_short.py", "REFS", "oculos"):
        "LEI DO REF — as duas mulheres sao a bullet de retencao deste angulo, "
        "por encomenda do operador.",
    # ⛔ DUPLA 16 herda o pool REFS do DUPLA por copia literal, entao herda a
    # razao inteira. Excecao declarada no dia em que o motor nasceu — deixar o
    # gate vermelho "porque eu sei que e' de proposito" e' como o operador
    # aprende a ignorar o gate.
    ("dupla16_short.py", "REFS", "oculos"):
        "LEI DO REF — mesmo pool e mesma razao do dupla_short.py.",
    # ⛔ BOTICA 16 herda o pool REFS por copia literal — mesma razao.
    ("botica16_short.py", "REFS", "oculos"):
        "LEI DO REF — mesmo pool e mesma razao do botica_short.py.",
    ("botica_short.py", "REFS", "oculos"):
        "LEI DO REF — oculos brigam frontalmente com 'linda'. Cabelo 12/12, "
        "porte 10/12, pele 6/12 e ancora 6/12 seguem cheios.",
}

FEMININO = re.compile(r"\b(she|her|woman|women|hers)\b", re.I)
# ⛔ SO' OS `_short` — ordem do operador 2026-08-03. Os `*_lucas` sao de
# terceiro, sairam para `agentes-de-terceiros/` e nao entram nem em leitura.
# O PRISMA e' a outra engine e tambem esta' fora do escopo de iteracao.
IGNORAR = ("short_comum.py", "ui_agente.py", "medir_personagens.py",
           "medir_contexto_copy.py", "distribuir.py", "nucleo_sonoro.py",
           "randomizador-prisma.py", "randomizador-v6.py")

PISO_MAGRO = 30.0   # abaixo disso o eixo existe mas quase nao e' sorteado


def texto_da_entrada(v):
    """Concatena tudo que e' string na entrada, seja dict, str ou tupla."""
    if isinstance(v, str):
        return v
    if isinstance(v, dict):
        return " ".join(str(x) for x in v.values() if isinstance(x, str))
    if isinstance(v, (list, tuple)):
        return " ".join(texto_da_entrada(x) for x in v)
    return ""


def e_pool_de_gente(entradas):
    """(1, 2) nao e' gente. Exige texto com cara de descricao fisica."""
    textos = [texto_da_entrada(v) for v in entradas]
    if not any(textos):
        return False
    return sum(len(t) for t in textos) / float(len(textos)) >= 15


def pools_do_arquivo(caminho):
    """Le o .py como ARVORE, nao importa o modulo — nao dispara efeito nenhum."""
    with io.open(caminho, encoding="utf-8") as f:
        arvore = ast.parse(f.read())
    achados = {}
    for no in arvore.body:
        if not isinstance(no, ast.Assign):
            continue
        for alvo in no.targets:
            if not isinstance(alvo, ast.Name) or not NOMES_DE_POOL.match(alvo.id):
                continue
            try:
                valor = ast.literal_eval(no.value)
            except (ValueError, SyntaxError):
                continue
            if isinstance(valor, (list, tuple)) and valor and e_pool_de_gente(valor):
                achados[alvo.id] = list(valor)
    return achados


def relatar(rotulo, textos, zerados, magros, declarados, arq, feminino):
    print("  %-16s n=%-3d distintas=%-3d" % (rotulo, len(textos), len(set(textos))))
    for eixo, padrao in EIXOS.items():
        if eixo == "pelo_facial" and feminino:
            print("      %-12s    —     pool feminino, eixo nao se aplica" % eixo)
            continue
        bate = sum(1 for t in textos if re.search(padrao, t, re.I))
        pct = 100.0 * bate / len(textos)
        motivo = EXCECOES.get((arq, rotulo, eixo))
        if bate == 0 and motivo:
            sinal, alvo = "zero por doutrina", declarados
        elif bate == 0:
            sinal, alvo = "ZERO  <<<", zerados
        elif pct < PISO_MAGRO:
            sinal, alvo = "magro", magros
        else:
            sinal, alvo = "ok", None
        if alvo is not None:
            alvo.append((arq, rotulo, eixo))
        print("      %-12s %3d/%-3d  %5.1f%%  %s" % (eixo, bate, len(textos), pct, sinal))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gate", action="store_true",
                    help="sai com codigo 1 se algum eixo estiver zerado")
    ap.add_argument("--arquivo", help="medir so' um motor")
    ap.add_argument("--autoteste", action="store_true",
                    help="so' roda os controles do medidor e sai")
    args = ap.parse_args()

    # ⛔ medidor mente. Roda os controles ANTES de reportar qualquer numero.
    falhas = autoteste()
    if args.autoteste:
        return 1 if falhas else 0
    if falhas:
        print("⛔ o medidor esta' quebrado — conserte o regex antes de confiar "
              "no relatorio abaixo")

    if args.arquivo:
        arquivos = [args.arquivo]
    else:
        arquivos = sorted(a for a in os.listdir(FO)
                          if a.endswith(".py") and not a.endswith("_app.py")
                          and a not in IGNORAR)
    zerados, magros, declarados = [], [], []
    for arq in arquivos:
        try:
            pools = pools_do_arquivo(os.path.join(FO, arq))
        except (SyntaxError, IOError) as e:
            print("%s: NAO LE (%s)" % (arq, e))
            continue
        if not pools:
            continue
        print("\n" + "=" * 74 + "\n" + arq + "\n" + "=" * 74)
        combinam = COMBINAM.get(arq, [])
        partes = []
        for nome, entradas in sorted(pools.items()):
            textos = [texto_da_entrada(v).lower() for v in entradas]
            if nome in combinam:
                partes.append(textos)
                print("  %-16s n=%-3d  (parte do produto, medido junto abaixo)"
                      % (nome, len(entradas)))
                continue
            feminino = (re.match(r"(MULHERES|NARRADORAS)", nome) is not None
                        or any(FEMININO.search(t) for t in textos))
            relatar(nome, textos, zerados, magros, declarados, arq, feminino)
        if len(partes) > 1:
            juntos = [" ".join(p[i % len(p)] for p in partes)
                      for i in range(max(len(p) for p in partes))]
            relatar("+".join(combinam), juntos, zerados, magros, declarados,
                    arq, False)

    print("\n" + "=" * 74)
    print("EIXOS ZERADOS: %d   (reprovacao)" % len(zerados))
    for a, n, e in zerados:
        print("  %-26s %-16s %s" % (a, n, e))
    print("EIXOS MAGROS (<%.0f%%): %d   (aviso)" % (PISO_MAGRO, len(magros)))
    for a, n, e in magros:
        print("  %-26s %-16s %s" % (a, n, e))
    print("ZERO POR DOUTRINA: %d   (nao e' pobreza, e' a regra)" % len(declarados))
    for a, n, e in declarados:
        print("  %-26s %-16s %-12s %s" % (a, n, e, EXCECOES[(a, n, e)].split(" — ")[0]))
    # excecao declarada que deixou de estar zerada = alguem encheu um eixo que
    # sustentava contraste. Nao e' erro de gate, e' regra quebrada em silencio.
    orfas = [k for k in EXCECOES if k[0] in arquivos and k not in declarados]
    if orfas:
        print("\n⚠️  EXCECAO DECLARADA QUE NAO ESTA' MAIS ZERADA — confira se a "
              "regra foi quebrada, ou remova a excecao:")
        for a, n, e in orfas:
            print("  %-26s %-16s %s" % (a, n, e))
    if args.gate and (zerados or orfas):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
