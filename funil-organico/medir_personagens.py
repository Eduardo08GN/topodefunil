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
import copy
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
    # ⭐ 2026-08-16: o eixo passou a falar tambem a lingua da MAO. Seis pools
    # do parque nao tem rosto (os tres BANHO, o HORSE, o PAR 16 e o DESCARTE
    # 16) e a ancora migrou para calo, queimadura, dedo torto, unha lascada e
    # junta deformada. O medidor acusava `ancora 0/N` e o que faltava era
    # vocabulario dele, nao marca no pool.
    # ⛔ O teste continua o mesmo: DISTINTIVA E PERMANENTE, nunca deterioracao
    # generica. `wrinkled`, `rough`, `dry` e `weathered` ficam de FORA — sao
    # textura, e textura mora no eixo `pele`. Os controles negativos cobram.
    "ancora":  r"\b(scars?|birthmark\w*|moles?|streak\w*|notched|dimple\w*|"
               r"cleft|gap between|beauty mark|crown|stud|hoop|"
               r"patch of white|white streak|silver streak|"
               r"call?us(es)?|calloused|burn marks?|chipped nails?|"
               r"cracked nails?|split nails?|missing nails?|"
               r"crooked (left |right )?(index|middle|ring|little|"
               r"fore)?fingers?|bent (index|middle|ring|little)?fingers?|"
               r"old break|knuckles? (that )?sits? (high|low)|"
               r"swollen (arthritic )?knuckles?|arthritic knuckles?|"
               r"knobbed knuckles?|cracked dry creases|nicks?|"
               r"ink stains?|tattoo\w*)\b",
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
                u"a wide gap between her front teeth",
                # ⭐ as cinco de MAO, uma por forma de ancora
                u"a hard yellow callus along the right palm edge",
                u"a shiny burn mark on the right thumb pad",
                u"a crooked left little finger set from an old break",
                u"one chipped nail on the left ring finger",
                u"swollen arthritic knuckles on both middle fingers"],
               [u"a printed housedress",
                # ⛔ OS FALSOS POSITIVOS QUE ESTA AMPLIACAO PODIA CRIAR:
                # textura de pele NAO e' ancora, e ja' tem eixo proprio.
                u"deeply wrinkled weathered skin across the backs",
                u"rough dry hands with high ropey veins",
                u"short blunt nails and thick square knuckles"]),
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
    falhas += _autoteste_leitura()
    print("autoteste do medidor: %s" % ("%d falha(s)" % falhas if falhas else "ok"))
    return falhas


# ⛔⛔ O CONTROLE DA LEITURA, e nao so' dos regexes (2026-08-11). Os controles
# acima provam que cada EIXO reconhece o que deve; nenhum provava que o pool
# CHEGA ate' eles. E foi ai' que o medidor cegou: um `"idade": IDADE_MULHER`
# dentro do `REFS` do trio16 derrubava o `literal_eval`, o `except: continue`
# engolia o pool inteiro, e trinta mulheres sumiram do gate sem uma linha de
# aviso. Eixo que nao e' lido nao reprova — e ausencia parece aprovacao.
_FONTE_CONTROLE = u'''
IDADE_X = 41
REFS_X = [
    {"idade": IDADE_X,
     "cabeca": "long silver waves worn loose over her shoulders",
     "marca": "a thin scar through her right eyebrow"},
    {"idade": 38,
     "cabeca": "a cropped platinum pixie cut",
     "marca": "a wide gap between her front teeth"},
]
'''


def _autoteste_leitura():
    """Pool com CONSTANTE NOMEADA dentro tem de ser lido, nao descartado."""
    import tempfile
    falhas = 0
    d = tempfile.mkdtemp()
    cam = os.path.join(d, "_controle_leitura.py")
    with io.open(cam, "w", encoding="utf-8") as f:
        f.write(_FONTE_CONTROLE)
    try:
        achados = pools_do_arquivo(cam)
        if "REFS_X" not in achados:
            print("  AUTOTESTE FALHOU  leitura: pool com constante nomeada "
                  "(`IDADE_X`) foi DESCARTADO — o gate para de ver o pool "
                  "inteiro e isso nao aparece como reprovacao")
            falhas += 1
        elif len(achados["REFS_X"]) != 2 or \
                achados["REFS_X"][0].get("idade") != 41:
            print("  AUTOTESTE FALHOU  leitura: constante nomeada nao foi "
                  "resolvida no valor certo (%r)" % (achados.get("REFS_X"),))
            falhas += 1
    finally:
        try:
            os.remove(cam)
            os.rmdir(d)
        except OSError:
            pass
    return falhas

# ⚠️ o sufixo opcional NAO e' enfeite. A v2 deste regex terminava em ")$" e por
# isso era CEGA para HOMENS_CLARA, CORPOS_PROVA_ESCURA e REFS_H_CLARA — ou seja,
# o elenco masculino do ESCANDALO, do TROCA e do ORGANICWAVE inteiro nunca foi
# medido, e o organicwave_short.py nao aparecia UMA VEZ no relatorio. Gate que
# nao ve o pool nao reprova o pool: ele so' produz um "passou" mentiroso.
# ⛔⛔ `MAOS` ENTROU EM 2026-08-16, e o buraco era grande: os QUATRO motores sem
# rosto do parque (`descarte16` e os tres BANHO) descrevem a pessoa inteira num
# pool chamado MAOS, e este regex nao o conhecia. O `descarte16` nao aparecia em
# UMA linha do relatorio — 93 blocos de motor, nenhum deles ele. ⚠️ Nos tres
# BANHO o buraco era menor porque eles tambem tem `HOMENS`, que era medido; a
# mao deles nunca foi.
# ⛔ E o preco de ligar: quatro dos seis eixos (cabelo, pelo_facial, oculos,
# pele) nao existem em mao nenhuma. Eles entram em EXCECOES abaixo, senao o gate
# passa a berrar para sempre — e gate que berra para sempre e' gate que ninguem
# le'. Os eixos que SOBRAM (porte e ancora) sao os que a mao de fato tem.
NOMES_DE_POOL = re.compile(
    r"^(REFS?|REF|HOMENS|MULHERES|NARRADORAS?|NARRADORES?|VITIMAS?|"
    r"ARQUETIPOS?|PACIENTES?|FIGURANTES?|PLATEIA|TESTEMUNHAS?|CORPOS?_PROVA|"
    r"MONTANHESES?|ESPECIALISTAS?|MAOS)(_[A-Z_]+)?$")

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
    # ⭐⭐ PAR 16 (2026-08-16) — O CORTE MAIS ALTO DO PARQUE: nao ha' cabeca,
    # nao ha' tronco, nao ha' braco acima do cotovelo. O `BLOCO 0 (REF)` E' UMA
    # FOTO DAS MAOS, e a linha `Nothing above the elbows enters the shot.` esta'
    # travada nos dois IMAGE. Cobrar barba ou oculos aqui e' pedir para desenhar
    # exatamente o que a decisao de projeto tirou do enquadramento.
    # ⚠️⚠️ E ATE' 2026-08-16 ESTE MOTOR NAO EXISTIA PARA O GATE. O pool chamava
    # `MAOS`, que o `NOMES_DE_POOL` nao casava — o arquivo inteiro evaporava do
    # relatorio e o gate saia 0 por nao ver nada, nao por estar limpo. E' o
    # mesmo modo de falha ja' escrito neste arquivo (o `REFS` do trio16, o
    # `pee16` que nunca estivera na lista): *ausencia nao e' zero*. O `MAOS`
    # entrou no `NOMES_DE_POOL` — e com ele apareceram tambem os `MAOS` do
    # `banho16` e do `banho16_3t`, que estavam invisiveis pelo mesmo motivo.
    # ⛔ `cabelo` NAO entra aqui de proposito: ele mede 1/8, e o unico acerto e'
    # `coarse grey-white hair over the forearms` — pelo de ANTEBRACO, que esta'
    # em quadro de verdade. Excecao sobre eixo nao-zerado vira orfa e reprova o
    # gate; e mais util ele ficar visivel como `magro`, que e' o que ele e'.
    ("par16_short.py", "MAOS", "pelo_facial"):
        "PAR16 — sem rosto em quadro: o BLOCO 0 e' uma FOTO DAS MAOS e os dois "
        "IMAGE travam `Nothing above the elbows enters the shot.`",
    ("par16_short.py", "MAOS", "oculos"):
        "idem PAR16 — sem cabeca em quadro, nao ha' onde por oculos",
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
    # ⛔⛔ OS QUATRO MOTORES SEM ROSTO — a familia POV do parque. A pessoa
    # inteira entra pelas MAOS: nao ha' cabeca em quadro, entao cabelo, pelo
    # facial e oculos nao sao pobreza de pool, sao a geometria do angulo. E
    # `pele` sai porque o regex dele e' de pele de ROSTO (`deeply lined`,
    # `laugh lines`, `sun-spotted`): a pele da mao mora no eixo `ancora`, que
    # continua cobrado e continua cheio (veia, no', calo, greta, cicatriz).
    # ⚠️ Isto NAO e' anistia: o `descarte16_short.py` cobra os cinco eixos de
    # mao (veia · no' · marca · unha · dedo) por conta propria, no `--autoteste`.
    ("descarte16_short.py", "MAOS", "cabelo"):
        "DE — angulo POV: nao ha' rosto em quadro, so' as maos e os antebracos. "
        "O `BLOCO 0 (REF)` e' uma FOTO DAS MAOS pela mesma razao.",
    ("descarte16_short.py", "MAOS", "pelo_facial"): "idem DE — sem rosto",
    ("descarte16_short.py", "MAOS", "oculos"): "idem DE — sem rosto",
    ("descarte16_short.py", "MAOS", "pele"):
        "idem DE — o regex de `pele` e' de pele de ROSTO; a pele da mao mora "
        "no eixo `ancora`, que e' cobrado e esta' cheio.",
    ("banho16_short.py", "MAOS", "cabelo"):
        "BA — mesmo desenho POV do descarte16: camera sem rosto, o narrador "
        "existe so' pelas maos.",
    ("banho16_short.py", "MAOS", "pelo_facial"): "idem BA — sem rosto",
    ("banho16_short.py", "MAOS", "oculos"): "idem BA — sem rosto",
    ("banho16_short.py", "MAOS", "pele"): "idem BA — pele de mao e' `ancora`",
    ("banho16_v2_short.py", "MAOS", "cabelo"): "idem BA — herdado por copia",
    ("banho16_v2_short.py", "MAOS", "pelo_facial"): "idem BA — sem rosto",
    ("banho16_v2_short.py", "MAOS", "oculos"): "idem BA — sem rosto",
    ("banho16_v2_short.py", "MAOS", "pele"): "idem BA — pele de mao e' `ancora`",
    ("banho16_3t_short.py", "MAOS", "cabelo"): "idem BA — herdado por copia",
    ("banho16_3t_short.py", "MAOS", "pelo_facial"): "idem BA — sem rosto",
    ("banho16_3t_short.py", "MAOS", "oculos"): "idem BA — sem rosto",
    ("banho16_3t_short.py", "MAOS", "pele"): "idem BA — pele de mao e' `ancora`",
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
    # ⚠️ o CLEAN V1 16SEG e' COPIA LITERAL do clean_short e herda o MESMO
    # REFS_M — conferido com `a.REFS_M == b.REFS_M`, nao de olho. A isencao
    # acompanha o pool: ela e' da REGRA, nao do arquivo.
    ("clean_v1_16s_short.py", "REFS_M", "oculos"): "idem clean_short",
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
    # ⭐ RESSURREICAO 16 (2026-08-08) — mesma NARRADORAS, mesma lei. Motor
    # nascido por copia literal; a chave da excecao inclui o nome do arquivo,
    # entao a do original nao alcanca o novo. ⚠️ Conferido: pool identico.
    ("ressurreicao16_short.py", "NARRADORAS", "oculos"):
        "idem ressurreicao_short — LEI DO REF, oculos de leitura brigam com "
        "'super fit e linda'. Pool identico, copia literal.",
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
    # ⭐ ESCANDALO 16 (2026-08-08) — mesma NARRADORAS, mesma lei. O motor
    # nasceu por copia literal do de 24s e o pool nao mudou; a excecao do
    # arquivo original nao alcanca o arquivo novo porque a chave inclui o nome
    # do arquivo. ⚠️ Conferido: o pool e' o mesmo objeto, entrada por entrada.
    ("escandalo16_short.py", "NARRADORAS", "oculos"):
        "idem escandalo_short — LEI DO REF, oculos de leitura brigam com "
        "'super fit e linda'. Pool identico, copia literal.",
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

    # ---------------------------------------------------------------------
    # ⭐ 2026-08-10 — os 16s que entraram sem isencao e deixavam o gate vermelho
    # ---------------------------------------------------------------------
    # ⛔ Herança NAO se presume: cada uma das cinco abaixo foi provada com
    # `a.POOL == b.POOL` no interpretador, nao de olho no diff. Onde o pool NAO
    # era identico, nao entrou isencao nenhuma — foi para o relatorio do
    # operador. E' a mesma disciplina do `clean_v1_16s_short` acima.
    ("clean_v2_16s_short.py", "REFS_M", "oculos"):
        "idem clean_short_v2 — pool identico, conferido (n=17).",
    ("flagrante16_short.py", "REFS", "pelo_facial"):
        "idem flagrante_short (F4b) — pool identico, conferido (n=18).",
    ("flagrante16_short.py", "REFS", "oculos"):
        "idem flagrante_short (F4b) — pool identico, conferido (n=18).",
    ("necrose16_short.py", "ARQUETIPOS", "pelo_facial"):
        "idem necrose_short (NE5) — pool identico, conferido (n=18).",
    ("necrose16_short.py", "ARQUETIPOS", "oculos"):
        "idem necrose_short (NE5) — pool identico, conferido (n=18).",
    # ⚠️⚠️ AS DUAS LINHAS ABAIXO FORAM REESCRITAS EM 2026-08-10, e a reescrita
    # e' o ponto: elas diziam *"pool identico ao pee_short, conferido (n=13)"*,
    # e isso DEIXOU DE SER VERDADE no commit em que o pool REFS do pee16 foi
    # reescrito e dobrado (n=24) para matar o atrator de celebridade. A razao
    # da isencao nao mudou uma virgula — mas a JUSTIFICATIVA mudou de "e' o
    # mesmo pool do vizinho" para "e' o contrato deste angulo". Isencao que
    # aponta para um pool que nao existe mais e' permissao esquecida ligada.
    ("pee16_short.py", "REFS", "pelo_facial"):
        "PE9/F4b — o narrador e' BARBEADO e SEM OCULOS de proposito: careca + "
        "bigode + oculos e' o que marca a VITIMA, e os dois dividem o IMAGE 01 "
        "num plano medio. Encher qualquer um dos dois aqui apaga o contraste "
        "de 3 eixos que separa os dois a' distancia. ⭐ O pool proprio do "
        "pee16 (n=24, reescrito em 2026-08-10) cobra os dois em autoteste "
        "(`python funil-organico/pee16_short.py --autoteste`), e os outros "
        "quatro eixos estao cheios: cabelo 92%, porte 63%, pele 42%, "
        "ancora 79%.",
    ("pee16_short.py", "REFS", "oculos"): "idem PE9/F4b — ver a linha acima",

    # ⛔⛔ ALFA 16 (2026-08-10) — DUAS isencoes, e as duas sao CONTRATO DE CENA.
    # ⚠️ Conferidas lendo os blocos montados, nao supostas por analogia. E o
    # terceiro eixo que nasceu zerado — `pelo_facial` nos HOMENS — NAO entrou
    # aqui: aquele era buraco de verdade (dezesseis homens de 50+ todos
    # barbeados sao um homem so' repetido) e foi PREENCHIDO, nao isentado.
    # E' a diferenca que este arquivo existe para manter.
    ("alfa16_short.py", "HOMENS", "oculos"):
        "CONTRATO DA CENA — ele passa os DOIS takes de tronco nu e toalha na "
        "cintura, e sete dos dez ambientes do take 2 sao agua ou vapor "
        "(piscina, jacuzzi, spa, praia, deck de borda infinita). Oculos ali "
        "nao sobrevivem ao quadro; e como ele e' uma das TRES pessoas que "
        "atravessam o corte, acessorio que aparece num take e some no outro "
        "troca a pessoa — que e' o defeito que a lente FA3 existe para impedir.",
    ("alfa16_short.py", "MULHERES", "oculos"):
        "LEI DO REF + CENA — as duas estao enroladas em toalha (ou de biquini) "
        "em piscina, jacuzzi e spa, e METADE dos sorteios as traz do pool BELA, "
        "onde a lei do operador proibe oculos desde 2026-08-03. Um pool com "
        "oculos entregaria a REF bela de oculos de leitura em 50% do lote.",

    # ⛔ CONTRATO DO MOTOR, o mesmo do falta_short: NENHUMA entrada do pool
    # masculino carrega adjetivo de etnia — conferido chave a chave, as seis
    # entradas de cada um so' tem `idade`, `cabeca`/`marca` e `sinal`. Quem
    # injeta a etnia e' a pagina (trava ETNIA), e pool com etnia dentro
    # quebraria a congruencia de mundo.
    # ⚠️ O pool FEMININO destes dois motores TEM `etnia` dentro, e por isso
    # `pele` la' nao aparece zerado. A assimetria e' de proposito.

    # ⛔⛔ TRES EXCECOES DE `pele` SAIRAM EM 2026-08-13 (good16, bed16, fight16).
    # Elas isentavam pools que NAO tinham marcador de pele nenhum; quando os
    # pools foram ampliados e saneados, a pele saudavel entrou e a isencao virou
    # LETRA MORTA. ⭐ E quem avisou foi o proprio gate, na secao "EXCECAO
    # DECLARADA QUE NAO ESTA' MAIS ZERADA" — excecao que sobrevive ao motivo
    # dela e' pior que excecao nenhuma: ela autoriza em silencio o defeito
    # voltar.

    # ⛔ LEI DO REF nos pools femininos que NASCERAM em MODO BELA. A prova nao
    # e' o nome do pool, e' o conteudo dele: idades 24-34 e descritores de
    # beleza (`slim toned`, `flat stomach`, `beauty spot`, `freckles`). Oculos
    # de leitura brigam frontalmente com isso, e a lei e' ordem permanente do
    # operador desde 2026-08-03.
    # ⚠️ O `bed16_short` NAO entra aqui de proposito: o pool dele e' a esposa de
    # 46-50 anos, escrita COM marcas de desgaste (`going dry at the ends`,
    # `heavy through the middle`, `a deep line between her brows`). MODO BELA
    # nao se aplica, entao o zero de la' e' buraco de verdade e fica vermelho.
    ("necrose16_short.py", "MULHERES_BELA", "oculos"):
        "LEI DO REF — pool em MODO BELA (24-31 anos, corpo tonificado).",
    ("good16_short.py", "MULHERES", "oculos"):
        "LEI DO REF — pool em MODO BELA (27-31 anos, porte atletico).",
    ("wife16_short.py", "MULHERES", "oculos"):
        "LEI DO REF — pool em MODO BELA (29-34 anos).",

    # ⛔⛔ FIGHT 16 — TRES ISENCOES, E AS TRES SAO CONTRATO DA CENA, nao buraco.
    # ⚠️ Conferidas UMA A UMA lendo os blocos montados, nao supostas por analogia
    # com o motor irmao. A analogia so' vale onde o contrato e' literalmente o
    # mesmo, e esta' dito em cada linha qual e'.
    # ⛔ A CENA NAO COMPORTA OCULOS, e isso e' verificavel nos dois blocos: no
    # take 1 ele acabou de sair do banho (tronco nu, TOALHA na cintura) e num
    # dos dez ambientes do take 2 ele esta' DENTRO da agua, com a agua no peito.
    # ⚠️ E ha' um motivo estrutural em cima do de cena: ele e' a UNICA coisa que
    # atravessa o corte neste angulo (os dois eixos de cena sao independentes),
    # entao a descricao dele E' a ancora de continuidade. Oculos que aparecem
    # num take e somem no outro trocam a pessoa — que e' exatamente o defeito
    # que a lente FT3 existe para impedir.
    ("fight16_short.py", "HOMENS", "oculos"):
        "CONTRATO DA CENA — ele sai do banho de toalha no take 1 e um dos dez "
        "ambientes do take 2 e' dentro d'agua; e a descricao dele e' a ancora "
        "de continuidade entre dois lugares independentes.",
    # ⛔ Nela o motivo se soma: METADE dos sorteios deste motor a poe em MODO
    # BELA (`sc.ref_bela`), onde a LEI DO REF proibe oculos por ordem permanente
    # do operador. Um pool com oculos entregaria a REF bela de oculos em 50% do
    # lote, que e' o oposto do que a lei manda.
    ("fight16_short.py", "MULHERES", "oculos"):
        "LEI DO REF + CENA — metade dos sorteios a traz do pool bela, e ela "
        "reaparece no take 2 dentro d'agua em um dos dez ambientes.",
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


def _constantes(arvore):
    """{NOME: valor} das constantes de modulo que sao literal pura.

    ⛔⛔ POR QUE ISTO EXISTE (2026-08-11). O `literal_eval` explode em QUALQUER
    nome dentro do pool, e o `except: continue` fazia o pool INTEIRO sumir da
    medicao — sem aviso, sem contagem, sem linha no relatorio. Ausencia nao e'
    zero: o gate nao reprova o que ele nao ve'.
    ⚠️ Achado no dia em que o `trio16_short.py` trocou os 30 `"idade": 22` por
    `"idade": IDADE_MULHER` (a regra dos 22, ordem do operador). O pool `REFS`
    dele — trinta mulheres, o eixo que a LEI DO REF vigia — evaporou do gate, e
    o unico sintoma foi um aviso obliquo de "excecao declarada que nao esta'
    mais zerada". Sem esse aviso, ninguem teria percebido.
    """
    consts = {}
    for no in arvore.body:
        if not isinstance(no, ast.Assign):
            continue
        for alvo in no.targets:
            if isinstance(alvo, ast.Name):
                try:
                    consts[alvo.id] = ast.literal_eval(no.value)
                except (ValueError, SyntaxError):
                    pass
    return consts


def _com_constantes(no, consts):
    """Avalia o no' trocando NOME por valor. Devolve None se sobrar coisa viva.

    ⚠️ Substitui SO' nome de constante de modulo ja' resolvida — nao executa
    chamada, nao concatena f-string, nao resolve atributo. O medidor le o
    arquivo como ARVORE de proposito: importar o motor dispararia efeito.
    """
    class _Troca(ast.NodeTransformer):
        def visit_Name(self, n):
            if n.id in consts:
                return ast.copy_location(ast.Constant(consts[n.id]), n)
            return n
    try:
        novo = _Troca().visit(copy.deepcopy(no))
        ast.fix_missing_locations(novo)
        return ast.literal_eval(novo)
    except (ValueError, SyntaxError, TypeError, RecursionError):
        return None


def pools_do_arquivo(caminho):
    """Le o .py como ARVORE, nao importa o modulo — nao dispara efeito nenhum."""
    with io.open(caminho, encoding="utf-8") as f:
        arvore = ast.parse(f.read())
    consts = _constantes(arvore)
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
                valor = _com_constantes(no.value, consts)
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
