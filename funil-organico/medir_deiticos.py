# -*- coding: utf-8 -*-
"""Mede as TRES familias de drifting que o operador expos em 2026-08-04.

⛔ AS TRES NASCERAM DE RENDER REPROVADO, NAO DE TEORIA. Ele leu a saida do
RECEITA e corrigiu tres takes a mao, e as tres correcoes tem a mesma forma: a
frase apontava para alguma coisa e nao dizia qual.

    A) DEITICO TERMINAL — a frase termina apontando para o vazio
       gerado:  "...points you at the expensive pill and away from this."
       ele:     *"Drifting identificado 'away from this.' From what???"*
       ⚠️ Deitico resolve para TRAS. No take 1 o mecanismo ainda nao foi dito,
       entao nao ha' para onde resolver.

    B) PRONOME NO LUGAR DO ORGAO — o sujeito do resultado e' `It`
       gerado:  "It came back full and stayed hard for the better part..."
       ele:     *"My tool came back full and stayed hard..."*
       ⚠️ `It` depois de uma frase sobre `the gelatin trick` resolve para O
       TRUQUE. O espectador ouve que o truque voltou inteiro.

    C) ABSTRATO SEM DESTINO — a frase nomeia o que foi escondido e nao diz
       para que serve
       gerado:  "Nobody owns what my grandfather knew."
       ele:     *"Nobody owns what my grandfather knew to trully save my
                 john-son and my marriage"*
       ⚠️ Foi esta que revelou que o vicio e' SISTEMICO e nao pontual: no pool
       de VILOES do RECEITA, 12 das 14 entradas terminavam em substantivo
       abstrato sem destino, e TODAS passavam pela lente RE20 — porque RE20
       cobrava o agente no COMECO da frase e nunca olhava o fim.

⭐⭐ POR QUE ESTE MEDIDOR EXISTE, e nao so' as lentes dentro de cada motor:
lente de motor pega o motor dela. O que custou caro hoje foi descobrir que a
familia (C) morava em 12 de 14 entradas de um pool que eu tinha declarado
limpo. A pergunta certa nunca e' "esta linha esta' certa?" — e' "quantas linhas
do repertorio inteiro tem esta forma?".

⛔ OS CONTROLES RODAM ANTES DE QUALQUER NUMERO SER OLHADO (licoes §16). As tres
frases que ele reprovou tem de ser acusadas; as tres correcoes dele tem de
passar. Medidor que nao reprova o caso conhecido mede outra coisa.

    python funil-organico/medir_deiticos.py            # relatorio
    python funil-organico/medir_deiticos.py --gate     # exit 1 se houver
    python funil-organico/medir_deiticos.py --motor receita
"""
import argparse
import importlib

import os
import random
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
if AQUI not in sys.path:
    sys.path.insert(0, AQUI)

# ⛔ Escopo do repo: os quatorze SHORT. `*_lucas` nao existe para nos.
MOTORES = ["clean", "clean_short_v2", "escandalo", "troca", "organicwave",
           "ressurreicao", "flagrante", "pee", "vazamento", "necrose",
           "exterior", "colo", "receita", "botica",
           "dupla", "placa"]

# --------------------------------------------------------------------------
# OS REFERENTES QUE CONTAM COMO "a frase disse do que se trata"
# --------------------------------------------------------------------------
# ⚠️ DELIBERADAMENTE LARGO. Um medidor de drifting que acusa copy certa e' pior
# que nenhum: ele treina o operador a ignorar o relatorio (licoes §16). Prefiro
# deixar passar um caso duvidoso a acusar dez corretos.
# ⛔⛔ AS GRAFIAS SAEM DOS MOTORES, NAO DA MINHA MEMORIA.
# A primeira versao escreveu `wei?ner` a mao — que casa `weiner` e `wener`, e
# NAO casa `wiener`, que e' a grafia que os motores realmente usam. O efeito era
# silencioso e caro: frases que NOMEIAM o orgao eram acusadas de nao nomear, e o
# relatorio inflava com falso positivo. E' a §2 de novo — medidor que acusa a
# copy certa treina o operador a ignorar o relatorio.
# ⚠️ `nucleo_sonoro` e' a fonte da verdade das grafias foneticas; os pools dos
# motores saem dele. Ler de la' e' a unica forma de isto nao envelhecer mentindo.
def _grafias():
    vistas = set()
    for _m in MOTORES:
        try:
            _mod = importlib.import_module(
                _m if _m.endswith("_v2") else "%s_short" % _m)
        except Exception:                            # noqa: BLE001
            continue
        vistas.update(getattr(_mod, "NUCLEO", []) or [])
    vistas.update(["manhood", "erection"])           # sinonimos nao-foneticos
    return sorted(vistas, key=len, reverse=True)


ORGAO = "|".join(re.escape(g) for g in _grafias())
PESSOA = (r"my (?:husband|wife|man|woman|marriage)|his wife|her husband|"
          r"the woman I married|my grandfather|my father|my brother")
MECANISMO = (r"gelatin|recipe|trick|mix|mixture|ingredients?|jar|glass|"
             r"kitchen|counter|bowl|powder|honey|cinnamon|ginger|paste")
VILAO = (r"pharmac\w+|drug compan\w+|drug industry|pill compan\w+|doctors?|"
         r"clinic|chemists?|prescription|television ad")
REFERENTE = re.compile("|".join([ORGAO, PESSOA, MECANISMO, VILAO]), re.I)

# (A) a frase acaba num deitico nu, EM CONSTRUCAO DE CONTRASTE
# ⛔⛔ A PRIMEIRA VERSAO ERA SO' "termina em deitico" E ACUSAVA 302 FRASES DO
# RESSURRECAO, A ESMAGADORA MAIORIA CORRETA. Achado LENDO os flagrantes antes de
# reportar o numero (§16/§19) — se eu tivesse entregue a tabela, teria entregue
# um relatorio que manda consertar copy que esta' certa.
#
# ⚠️ TRES COISAS QUE A REGRA LARGA NAO SABIA, e que sao especificas de VIDEO:
#   1. `Hit follow first, or Facebook won't deliver it.` — `it` e' a receita,
#      nomeada na sentenca anterior do mesmo CTA. Isso e' anafora, nao drifting.
#      E como esta' no CTA de todos os motores, sozinho inflava a tabela.
#   2. `His hangs just like this.` / `Like this.` — o deitico aponta para o PROP
#      EM QUADRO. Num video isso resolve: e' o bit visual carregando o
#      referente. Texto puro nao tem essa opcao; video tem.
#   3. `Urologists won't tell you this.` — e' a FORMA QUE O OPERADOR DITOU
#      (`doctors don't want you to know this`). Acusar isso e' acusar o cliente.
#
# ⭐ O QUE REALMENTE DISTINGUE O CASO QUE ELE REPROVOU: o deitico e' o outro
# lado de um CONTRASTE — "points you at the expensive pill AND AWAY FROM this" —
# e o nosso lado do contraste nunca foi nomeado. A frase promete uma oposicao e
# entrega metade dela. Sem o marcador de contraste, `this` e' so' um ponteiro
# para a tela ou para a frase anterior, e ambos resolvem.
FIM_DEITICO = re.compile(r"\b(this|that|it|these|those|them)\s*[.!?]*\s*$", re.I)
CONTRASTE = re.compile(
    r"\b(and (?:never|not)|away from|instead of|rather than|and no one|"
    r"but not|never about)\b", re.I)

# (B) `It ...` descrevendo estado do corpo sem nomear o corpo
# ⛔⛔ O PRONOME TEM DE SER O SUJEITO DO VERBO — e a primeira versao so' exigia
# que a frase COMECASSE com pronome e que o verbo aparecesse em algum lugar.
# Com isso acusou 22 frases do NECROSE, todas a mesma:
#     "That's the gelatin trick, and the blood flow came back."
# O sujeito de `came back` ali e' `the blood flow`, que ESTA' nomeado; o `That's`
# do inicio e' outra oracao e aponta para a demonstracao em quadro. Achado
# lendo o flagrante (§19), como sempre — a contagem parecia perfeitamente
# plausivel.
# ⚠️ Agora o verbo tem de vir colado no pronome (no maximo um adverbio no meio).
ESTADO_CORPO = (r"came back|come back|stood up|stands up|went from|got hard|"
                r"stayed hard|stay hard|stayed up|held all night|"
                r"twice the size|three times harder|swollen|filled out|woke me")
PRONOME_SUJEITO = re.compile(
    r"^\s*(?:it|they|that)\s+(?:\w+\s+)?(?:%s)\b" % ESTADO_CORPO, re.I)

# (C) abstrato de "o que foi escondido" sem dizer para que serve
ABSTRATO = re.compile(
    r"\b(the (?:cheap |real |only |two-dollar )?(?:fix|answer|truth|secret)|"
    r"what (?:my \w+ knew|costs? [\w-]+)|nothing that worked|"
    r"asking questions|never one answer|stays broken)\b", re.I)
DESTINO = re.compile("|".join([ORGAO, r"\bmarriage\b", r"\bmy wife\b",
                               r"\bhis wife\b", MECANISMO]), re.I)


def sentencas(texto):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", texto or "") if s.strip()]


def classificar(s):
    """Devolve a familia (`A`/`B`/`C`) ou None. Uma frase, um veredito."""
    # ⛔ FAMILIA A NAO USA `REFERENTE`, E A PRIMEIRA VERSAO USAVA — ficou cega no
    # proprio controle do operador. `Every television ad points you at the
    # expensive pill and away from this.` casava em `television ad` e passava.
    # ⚠️ Mas o que importa nao e' se a frase nomeia ALGUMA coisa: e' se ela
    # nomeia a coisa PARA ONDE O DEITICO APONTA. `television ad` e `pill` sao os
    # objetos do VILAO; `away from this` significa longe do NOSSO, que e'
    # exatamente o que a frase nao diz. Entao aqui so' valem mecanismo e orgao.
    if (FIM_DEITICO.search(s) and CONTRASTE.search(s)
            and not re.search("%s|%s" % (MECANISMO, ORGAO), s, re.I)):
        return "A"
    if PRONOME_SUJEITO.search(s) and not re.search(ORGAO, s, re.I):
        return "B"
    if ABSTRATO.search(s) and not DESTINO.search(s):
        return "C"
    return None


# --------------------------------------------------------------------------
# CONTROLES — as frases do operador, literais
# --------------------------------------------------------------------------
# ⛔ A esquerda o que ele REPROVOU (tem de ser acusado, na familia dita); a
# direita o que ele ESCREVEU no lugar (tem de passar limpo).
CONTROLES = [
    ("A", "Every television ad points you at the expensive pill and away from this.",
          "Every television ad points you at the expensive pill, the secret is "
          "in this natural trick."),
    ("B", "It came back full and stayed hard for the better part of an hour.",
          "My tool came back full and stayed hard for the better part of an hour."),
    ("C", "Nobody owns what my grandfather knew.",
          "Nobody owns what my grandfather knew to truly save my john-son and "
          "my marriage."),
]
# ⚠️ Controles positivos extras: copy que ESTA' CERTA e ja' me fez escrever
# regra larga demais uma vez. Se qualquer um destes for acusado, o medidor esta'
# errado, nao a copy.
LIMPOS = [
    "Comment gelatin, and I'll send you the whole recipe.",     # termina em `recipe`
    "She stopped reaching over at night.",                       # concreta, sem orgao
    "Add up what the pharmacy took from me. None of it worked.",  # `it` no meio
    "It all changed the day my brother showed me the gelatin trick.",
    # ⛔ os quatro abaixo foram acusados pela versao LARGA da familia A e estao
    # CERTOS. Ficam aqui para sempre: se voltarem a ser acusados, quem regrediu
    # foi o medidor, nao a copy.
    "Hit follow first, or Facebook won't deliver it.",
    "His hangs just like this.",
    "Look at that.",
    "Urologists won't tell you this.",
    # ⛔ acusada pela versao larga da familia B: o sujeito de `came back` e'
    # `the blood flow`, que ESTA' nomeado — o `That's` do inicio e' outra
    # oracao e aponta para a demonstracao em quadro.
    "That's the gelatin trick, and the blood flow came back.",
]


def rodar_controles():
    falhas = []
    for fam, ruim, bom in CONTROLES:
        got = classificar(ruim)
        if got != fam:
            falhas.append("[%s] NAO acusa a frase que o operador reprovou "
                          "(veio %r): %r" % (fam, got, ruim))
        got = classificar(bom)
        if got is not None:
            falhas.append("[%s] acusa a CORRECAO do operador (%s) — regra larga "
                          "demais: %r" % (fam, got, bom))
    for s in LIMPOS:
        for frase in sentencas(s):
            got = classificar(frase)
            if got is not None:
                falhas.append("[%s] acusa copy limpa — regra larga demais: %r"
                              % (got, frase))
    return falhas


def varrer(nome, n=250, seed=11):
    # ⚠️ o v2 do CLEAN quebra a convencao: o arquivo e' `clean_short_v2.py`, e
    # nao `clean_v2_short.py`. Sem esta excecao ele saia da tabela com um
    # `ERRO: No module named`, que eu quase deixei passar como ruido — motor
    # que nao foi medido nao e' motor limpo (§16).
    mod = importlib.import_module(
        nome if nome.endswith("_v2") else "%s_short" % nome)
    paginas = sorted(getattr(mod, "ETNIA", {"joe": None}))
    achados = []
    total = 0
    rng = random.Random(seed)
    for i in range(n):
        pag = paginas[i % len(paginas)]
        # ⛔⛔ TRES ARGUMENTOS, SEMPRE. A versao anterior tentava
        # `sortear(p, rng, {}, {})` e caia para 3 no TypeError — e isso estava
        # ERRADO: o 4o posicional NAO e' `travas` em todo motor. No ESCANDALO e'
        # `degrau`, no RESSURREICAO e' `credibilidade`. Passar `{}` ali injetava
        # um degrau invalido e o motor gerava fala fora da escada, sem erro de
        # tipo — ou seja, o medidor media um motor em estado que o operador
        # nunca produz. Todos os eixos opcionais tem default, entao 3 basta.
        spec = mod.sortear(pag, random.Random(rng.randrange(1 << 30)), {})
        for cena, fala in enumerate(spec["falas"], 1):
            for s in sentencas(fala):
                total += 1
                fam = classificar(s)
                if fam:
                    achados.append((fam, cena, s))
    return total, achados


def main():
    ap = argparse.ArgumentParser(
        description="Mede deitico terminal, pronome no lugar do orgao e "
                    "abstrato sem destino nos 14 agentes SHORT")
    ap.add_argument("--motor", help="so' este (sem o sufixo _short)")
    ap.add_argument("--n", type=int, default=250, help="videos por motor")
    ap.add_argument("--gate", action="store_true",
                    help="exit 1 se qualquer motor tiver achado")
    a = ap.parse_args()

    # ⛔ CONTROLES PRIMEIRO. Numero de medidor cego e' pior que numero nenhum.
    falhas = rodar_controles()
    if falhas:
        print(">> O MEDIDOR ESTA' CEGO — nenhum numero abaixo vale:")
        for f in falhas:
            print("   " + f)
        return 1
    print("controles OK — as 3 frases reprovadas acusam, as 3 correcoes passam, "
          "e a copy limpa nao e' acusada.\n")

    alvos = [a.motor] if a.motor else MOTORES
    print("%-16s %7s %6s %5s %5s %5s" % ("motor", "sents", "sujos", "A", "B", "C"))
    print("-" * 50)
    sujos = {}
    for nome in alvos:
        try:
            total, ach = varrer(nome, a.n)
        except Exception as e:                       # noqa: BLE001
            print("%-16s  ERRO: %s" % (nome, str(e)[:60]))
            continue
        c = {"A": 0, "B": 0, "C": 0}
        for fam, _, _ in ach:
            c[fam] += 1
        print("%-16s %7d %6d %5d %5d %5d"
              % (nome, total, len(ach), c["A"], c["B"], c["C"]))
        if ach:
            sujos[nome] = ach

    if not sujos:
        print("\nNENHUM ACHADO nos %d motores." % len(alvos))
        return 0

    print("\n" + "=" * 70)
    print("FLAGRANTES — ate' 4 por motor, a frase como ela sai renderizada")
    print("=" * 70)
    for nome, ach in sujos.items():
        print("\n--- %s (%d) ---" % (nome, len(ach)))
        vistas = set()
        n = 0
        for fam, cena, s in ach:
            if s in vistas:
                continue
            vistas.add(s)
            print("  [%s] cena %d: %s" % (fam, cena, s))
            n += 1
            if n >= 4:
                break
    return 1 if a.gate else 0


if __name__ == "__main__":
    sys.exit(main())
