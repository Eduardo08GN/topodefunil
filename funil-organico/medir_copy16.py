# -*- coding: utf-8 -*-
"""medir_copy16.py — o CONTRATO DE COPY 16s, cobrado de fora, motor por motor.

⛔ POR QUE EXISTE, E POR QUE E' SEPARADO DO `lint` DE CADA MOTOR.

Em 2026-08-10 o operador mandou reformular a copy de sete agentes da familia
16s. A revisao adversarial que motivou a ordem (6 lentes independentes, 127
achados, 79 derrubados na refutacao) nao encontrou defeitos de ESTILO: encontrou
sete defeitos ESTRUTURAIS, cada um presente em quase todos os motores ao mesmo
tempo. Medido ANTES da reforma, 200 sorteios por motor:

    motor            p/CTA rotulo ingred erecao 2nomes
    troca16           100%    73%     0%     0%   100%
    ressurreicao16    100%   100%    62%    22%   100%
    exterior16        100%   100%     0%   100%   100%
    flagrante16       100%   100%     0%     0%   100%
    pee16              26%    60%     0%    54%    98%
    escandalo16       100%   100%    56%     0%   100%
    colo16            100%    64%     0%    12%   100%

Defeito que aparece em sete motores nao e' erro de quem escreveu o pool — e'
ausencia de contrato. O contrato mora em `short_comum.lint_copy16`; este arquivo
o cobra DE FORA, pelo sorteio real, para que:

  1. de' para medir um motor ANTES de ele ligar a lente (senao nao ha' "antes");
  2. o numero seja do VIDEO gerado, nao do pool lido — os sete defeitos acima
     vivem na COMBINACAO, e nenhum deles aparece relendo a lista de strings.

⚠️ A LISTA DE MOTORES E' MANTIDA A MAO. Motor 16s novo entra AQUI no mesmo
commit em que nasce, junto com as listas do `medir_teto_fala`, `medir_deiticos`,
`medir_contexto_copy`, `medir_abertura` e `medir_alcance`.

    python funil-organico/medir_copy16.py
    python funil-organico/medir_copy16.py --motor colo16 --exemplos 5
    python funil-organico/medir_copy16.py --gate
"""
import argparse
import collections
import importlib
import os
import random
import sys

# ⛔ MESMO REMENDO DO `medir_personagens.py` (linha 51), e pela mesma razao
# medida em 2026-08-13: este gate MORREU no proprio rodape, com
# UnicodeEncodeError, ao imprimir a lista de travas DESLIGADAS — o console
# do Windows e' cp1252 e os marcadores nao cabem nele.
# ⚠️ E o padrao caro se repetiu inteiro: o rodape so' roda QUANDO HA' ALGO
# A REPORTAR, entao o gate quebrava exatamente na hora em que tinha algo a
# dizer, e nunca no caminho feliz. Gate que morre calado na hora do recado
# treina o operador a ignorar o gate.
for _f in (sys.stdout, sys.stderr):
    try:
        _f.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

AQUI = os.path.dirname(os.path.abspath(__file__))
if AQUI not in sys.path:
    sys.path.insert(0, AQUI)

import short_comum as sc                                        # noqa: E402

MOTORES = ["banho16", "troca16", "ressurreicao16", "exterior16", "flagrante16",
           "pee16", "escandalo16", "colo16",
           # os demais 16s: entram na medicao desde ja', mesmo antes da
           # reforma — numero que ninguem olha e' numero que envelhece
           "trio16", "dupla16", "falta16", "placa16", "botica16", "good16",
           # + 2026-08-10: o BED 16 entra AQUI no commit em que nasce — ele
           # ja' nasce sob o contrato, e motor fora da lista nao e' medido.
           "bed16", "necrose16", "wife16",
           # + 2026-08-15: o VICK 16, no commit em que nasce. Ele e' o
           # primeiro motor cuja `KEYWORD_NATIVA` NAO e' `gelatin` e que
           # ainda assim mede limpo — foi ele que expos o buraco do
           # `keyword_do_motor`, que os tres BANHO carregavam calado.
           "vick16",
           # + 2026-08-10: o FIGHT 16, no commit em que nasce
           "fight16",
           # + 2026-08-14: o BANHO 16 3TAKES, no commit em que nasce.
           # ⭐ E' o primeiro motor de TRES cenas a entrar aqui, e nao foi
           # preciso mexer em nada: o `sc.lint_copy16` le' `falas[-1]`, nao
           # `falas[1]`, entao a cena do CTA e' achada por POSICAO RELATIVA e
           # o contrato atravessou a mudanca de formato inteiro. Verificado,
           # nao suposto — o CT6 deu 0% (achou o endereco de entrega), que e'
           # impossivel se ele estivesse medindo a cena do PREPARO.
           "banho16_3t",
           # + 2026-08-10: o ALFA 16 entra aqui no commit em que nasce.
           # ⚠️ Ele DESLIGA o CT2 e o CT6 localmente (o angulo nao enuncia
           # falha, e o operador tirou a clausula de entrega do CTA) —
           # este relatorio continua MEDINDO os dois, e e' de proposito:
           # o motor nao cobra, mas o numero fica visivel aqui.
           "alfa16",
           # + 2026-08-12: o PRATO 16, no commit em que nasce. ⚠️ Ele DESLIGA
           # o CT2 e o CT5 localmente, os dois por decisao declarada do
           # operador (ver `DESLIGADAS`) — e este relatorio continua MEDINDO os
           # dois. E' o unico motor do parque que nomeia ingrediente na fala, e
           # e' justamente por isso que o numero dele tem de ficar visivel.
           "prato16", "mel16", "banho16_v2",
           # + 2026-08-14: o ORGANIC WAVE 16 entra AQUI no commit em que nasce.
           # ⚠️ Ele NAO desliga trava nenhuma. O CT2 dele acusa ~52% dos
           # sorteios e o numero fica visivel de proposito: metade dos hooks
           # aprovados pelo operador em 2026-07-31 enuncia a falha pelo
           # DEITICO mais o prop na mao (`this is what my {o} looked like`) em
           # vez de por verbo de disfuncao, e o regex do CT2 le' verbo. Nao e'
           # excecao declarada — e' pergunta aberta para o operador.
           "organicwave16",
           # + 2026-08-14: o HORSE 16 entra AQUI no commit em que nasce.
           # ⚠️⚠️ Ele NOMEIA a receita na fala (`horse gelatin, lemon and
           # cinnamon`), por ordem do operador — e mesmo assim mede 0% no
           # CT5. A razao vale para o parque inteiro: o CT5 le' a fala do
           # CTA (`falas[-1]`), e aqui os ingredientes estao no TAKE 1.
           # ⛔ Por isso ele NAO entra em `DESLIGADAS`: excecao que nao
           # suprime nada e' ruido, e ruido ensina a desconfiar das que
           # suprimem de verdade.
           "horse16"]

# ⛔ Angulos cuja cena 1 E' uma promessa falsa que o proprio video desmente.
# So' muda o CT7: la' o verbo de ereccao e' a isca, nao o claim.
ISCA_ABSURDA = {"troca16", "exterior16", "colo16"}

N = 200


def medir(nome, n=N, exemplos=0):
    M = importlib.import_module("%s_short" % nome)
    pags = sorted(getattr(M, "ETNIA", {"joe": None}))
    contas = collections.Counter()
    amostras = collections.defaultdict(list)
    apelidos = collections.Counter()
    for i in range(n):
        spec = M.sortear(pags[i % len(pags)], random.Random(i), {})
        corpo = " ".join(spec["falas"]).lower()
        for ap in sc.APELIDOS_16:
            if ap.lower() in corpo:
                apelidos[ap] += 1
        achados = []
        sc.lint_copy16(M, spec, achados,
                       isca_absurda=(nome in ISCA_ABSURDA))
        vistos = set()
        for nivel, msg in achados:
            ct = msg.split(":", 1)[0]
            if ct in vistos:
                continue
            vistos.add(ct)
            contas[ct] += 1
            if exemplos and len(amostras[ct]) < exemplos:
                amostras[ct].append((nivel, msg, spec["falas"]))
    return contas, amostras, apelidos


CTS = ["CT1", "CT2", "CT3", "CT4", "CT4b", "CT5", "CT6", "CT7", "CT8"]
ROTULO = {
    "CT1": "sentenca depois do CTA",
    "CT2": "take 1 sem falha enunciada",
    "CT3": "`gelatin trick` sem razao",
    "CT4": "apelido muda no corte",
    "CT5": "ingrediente na fala",
    "CT6": "CTA sem endereco de entrega",
    "CT7": "verbo de ereccao no take do CTA",
    "CT4b": "apelido fora de pecker/wiener/Johnson",
    "CT8": "pede follow na fala (a DM sai igual)",
}

# ⚠️ O CT4 sozinho garante UM apelido por video — e um apelido por video pode
# ser o MESMO apelido em todo o lote, que e' mode-collapse com cara de
# consistencia. Esta coluna mostra a reparticao real entre os tres.


# ⭐⭐ TRAVAS DESLIGADAS POR DOUTRINA — declaradas, nunca escondidas
# ---------------------------------------------------------------------------
# ⛔ Nem toda trava vale para todo angulo, e um relatorio que acusa uma DECISAO
# como se fosse defeito treina o operador a ignorar o relatorio inteiro
# (licoes §16). Mesma mecanica das `EXCECOES` do `medir_personagens.py`: o
# numero CONTINUA sendo medido e impresso — o que muda e' que o motor nao entra
# na lista de "violam", e a decisao aparece rotulada no rodape.
# ⛔ So' entra aqui trava desligada TAMBEM NO MOTOR, com o motivo escrito la'.
# Desligar so' aqui seria maquiar o relatorio.
DESLIGADAS = {
    # ------------------------------------------------------------------
    # VICK 16 — as tres, declaradas no commit em que o motor nasce
    # ------------------------------------------------------------------
    ("vick16", "CT5"):
        "o `gelatin` que o CT5 acusa NAO e' a receita entregue — e' o NOME DO "
        "RITUAL. O operador mandou aumentar o pool de nomes (*\"gelatin hack, "
        "rub hack, gelatin trick, rub trick, etc etc\"*), e a fonte faz igual "
        "no v11 (*\"a buddy told me about the horse gelatin trick\"*). "
        "⭐ E o CT5 so' passou a ver isso porque a keyword deste motor e' "
        "`recipe`: com `gelatin` fora do posto de keyword, ela volta a contar "
        "como ingrediente — regra que eu mesmo escrevi hoje e que aqui acusa "
        "certo o objeto errado. A lente VI1 do motor cobra o que importa: "
        "nenhuma fala nomeia Vicks, Knox, mel ou bicarbonato (0% medido).",
    ("vick16", "CT2"):
        "mesma pendencia do ORGANICWAVE 16 (49%) e do HORSE 16 (52%), e aqui "
        "ela e' maior porque METADE dos hooks e' a familia HISTORIA, que "
        "enuncia a falha pela PERDA (*\"she said I wasn't enough for her "
        "anymore\"*) e nao por verbo de disfuncao — e o regex do CT2 le' verbo. "
        "⛔ Nao reformulo os hooks para satisfazer o regex: a familia HISTORIA "
        "e' eixo pedido pelo operador, e dobrar a copy ao gate e' o defeito "
        "que a §16 das licoes descreve. Ou a lente cresce, ou fica assim.",
    ("vick16", "CT7"):
        "os 15 videos da fonte dizem `makes you hard`, `rock hard results`, "
        "`stay hard` — e o apelido do orgao esta' na sentenca VIZINHA, nao "
        "colada. ⚠️ O regex do CT7 mede por sentenca e as duas caem na mesma "
        "quando o hook e' curto. A lente VI7 do motor cobra o que tem preco "
        "medido de verdade: o GESTO no orgao, que rendeu ~95% de recusa no "
        "COLO 16 (0% aqui).",
    ("banho16_3t", "CT1"):
        "os SETE videos da fonte terminam no follow, depois do CTA, e o "
        "operador aprovou as doze copies uma a uma lendo essa ordem. "
        "⭐ E aqui o CT1 perde ainda mais forca: com TRES cenas o CTA tem "
        "cena PROPRIA, entao o follow nao divide espaco com o mecanismo — que "
        "era o risco real que o CT1 protegia.",
    ("banho16_3t", "CT2"):
        "duas das doze familias (a forma de melhor comentario da fonte, 20,5 "
        "por mil views) NAO enunciam falha nenhuma: avisam e prometem. "
        "⚠️ E' o mesmo desenho do ALFA 16, e neste motor e' EIXO "
        "declarado (`mecanismo`), nao descuido — o lote existe justamente para "
        "medir se explicar menos rende mais comentario.",
    ("banho16_3t", "CT4b"):
        "decisao E3, tomada pelo operador ao APROVAR a copy: as familias 4 "
        "(`bat`) e 7.2 (`pipe`, que ele mesmo escreveu) usam o vocabulario da "
        "FONTE, nao o pool compartilhado `pecker/wiener/Johnson`. "
        "⛔ Isso NAO vale para o `banho16` V1/V2, onde a ordem D7 (*so' "
        "Johnson e manhood*) continua de pe'. Quem cobra aqui e' a lente BA5.",
    ("banho16_3t", "CT8"):
        "follow liberado (mesma razao do `banho16`: os 7 reels da fonte pedem "
        "follow). ⚠️ O que NAO caiu foi a razao do CT8 — a DM sai "
        "igual — e por isso a lente BA7 deste motor ficou MAIS dura que a do "
        "irmao: alem de `follow or`, ela pega `follow first`/`follow before`, "
        "que foi como o portao voltou a aparecer em 14/08.",
    ("good16", "CT4b"):
        "ordem do operador (2026-08-13), lendo o lote: *\"nunca citar nada alem "
        "de johnson ou manhood, independente se esta' setado copy leve ou nao, "
        "esse agente deve citar somente esses 2\"*. Medido antes da ordem, 400 "
        "sorteios: `wiener` 155, `Johnson` 125, `pecker` 120 — dois em cada "
        "tres videos saiam com um apelido que ele nao quer neste angulo. "
        "⭐ O que o CT4b protege (variar o apelido ENTRE videos) segue vivo: o "
        "`NUCLEO` tem dois e o sorteio alterna. Quem cobra e' a lente GO19.",
    ("banho16_v2", "CT7"):
        "ordem direta do operador (2026-08-13), depois de eu mostrar que o CT7 e "
        "a BA6 reprovavam: *\"volte com o hard colado\"*. E' a frase da fonte, "
        "verbatim menos o apelido. ⚠️ COLIDE com o D8 dele (registro leve), que e' "
        "a razao de existir da BA6 — a ordem nova venceu por ser mais recente. O "
        "preco esta' medido: ~95% de recusa no COLO 16. ⭐ A excecao e' de UMA "
        "acao (`rasga_sache`), nao do motor: as outras doze seguem cobradas.",
    ("banho16_v2", "CT1"):
        "os SETE videos da fonte terminam no follow, depois do CTA, e o "
        "operador aprovou a ordem mecanismo -> CTA -> follow lendo a copy.",
    ("banho16", "CT1"):
        "os SETE videos da fonte terminam no follow, depois do CTA, e o "
        "operador aprovou a ordem mecanismo -> CTA -> follow lendo a copy.",
    ("banho16_v2", "CT2"):
        "o angulo nao abre em falha: abre num AVISO ou numa IDADE. Mesmo "
        "desenho do ALFA 16.",
    ("banho16", "CT2"):
        "o angulo nao abre em falha: abre num AVISO ou numa IDADE. Mesmo "
        "desenho do ALFA 16.",
    ("banho16_v2", "CT4b"):
        "ordem do operador: so' `Johnson` e `manhood`, nunca `pecker` nem "
        "`wiener` — que sao justamente dois dos tres do pool compartilhado.",
    ("banho16", "CT4b"):
        "ordem do operador: so' `Johnson` e `manhood`, nunca `pecker` nem "
        "`wiener` — que sao justamente dois dos tres do pool compartilhado.",
    ("banho16_v2", "CT8"):
        "follow liberado por ele. O que NAO caiu foi a razao do CT8: a DM sai "
        "igual, entao o follow e' PEDIDO e nunca CONDICAO (lente BA7).",
    ("banho16", "CT8"):
        "follow liberado por ele. O que NAO caiu foi a razao do CT8: a DM sai "
        "igual, entao o follow e' PEDIDO e nunca CONDICAO (lente BA7).",
    ("alfa16", "CT2"):
        "o angulo nao enuncia falha — ele AVISA e PROMETE, e o espectador se "
        "reconhece pela ESPOSA. Desenho do operador.",
    ("alfa16", "CT6"):
        "ordem do operador: o CTA sai sem clausula de entrega. As palavras "
        "liberadas foram para a objecao da cozinha.",
    ("prato16", "CT2"):
        "o take 1 e' TESTEMUNHO DE DESCOBERTA, nao enunciado de falha — mesma "
        "familia do GOOD 16 e do ALFA 16. Desenho do operador.",
    # ⛔ O MEL 16 herda a decisao do irmao: a fala nomeia os tres
    # ingredientes, como a fonte. ⚠️ O CT2 dele NAO entra aqui — a PERGUNTA de
    # abertura enuncia a falha em toda entrada do pool, entao ele cumpre a
    # regra em vez de pedir excecao.
    ("mel16", "CT5"):
        "ordem do operador (2026-08-12), a mesma do PRATO 16: a fala NOMEIA "
        "gelatina, limao e bicarbonato, como a fonte. Os dois motores testam a "
        "mesma hipotese de proposito — e' o par que o campo vai comparar "
        "contra os outros dezessete.",
    ("prato16", "CT5"):
        "ordem do operador (2026-08-12), com as tres opcoes na mesa e o preco "
        "escrito: a fala NOMEIA gelatina, limao e bicarbonato, como a fonte "
        "que fez 1.6K comentarios. E' HIPOTESE testada em campo — a receita "
        "dita torna o pedido crivel e o que a DM vende passa a ser o COMO. Se "
        "o comentario cair neste angulo contra os outros, a causa candidata "
        "numero um e' esta. O motor cobra o CONTRARIO na lente PR8.",
}


def main():
    ap = argparse.ArgumentParser(
        description="cobra o CONTRATO DE COPY 16s pelo sorteio real")
    ap.add_argument("--motor", choices=MOTORES)
    ap.add_argument("--n", type=int, default=N)
    ap.add_argument("--exemplos", type=int, default=0)
    ap.add_argument("--gate", action="store_true",
                    help="sai 1 se qualquer motor violar qualquer CT")
    a = ap.parse_args()
    alvos = [a.motor] if a.motor else MOTORES

    print("\nCONTRATO DE COPY 16s — %d sorteios por motor, %% de videos que "
          "violam" % a.n)
    print("-" * 88)
    print("%-16s %s   %s" % ("motor", "  ".join("%-5s" % c for c in CTS),
                            "/".join(sc.APELIDOS_16)))
    print("-" * 88)
    sujos = []
    for nome in alvos:
        try:
            contas, amostras, apelidos = medir(nome, a.n, a.exemplos)
        except Exception as e:                              # noqa: BLE001
            print("%-16s ERRO: %s" % (nome, str(e)[:60]))
            sujos.append(nome)
            continue
        # ⛔ trava desligada POR DOUTRINA nao conta como violacao (ver
        # DESLIGADAS) — mas o numero continua impresso, na coluna de sempre.
        if any(contas[c] for c in CTS if (nome, c) not in DESLIGADAS):
            sujos.append(nome)
        rep = "/".join("%d" % (100 * apelidos[x] // a.n)
                       for x in sc.APELIDOS_16)
        print("%-16s %s   %s"
              % (nome, "  ".join("%4d%%" % (100 * contas[c] // a.n)
                                 for c in CTS), rep))
        if a.exemplos:
            for c in CTS:
                for nivel, msg, falas in amostras.get(c, []):
                    print("    [%s] %s" % (nivel, msg[:120]))
                    for j, f in enumerate(falas, 1):
                        print("        %d| %s" % (j, f))
    print("-" * 88)
    for c in CTS:
        print("  %-4s %s" % (c, ROTULO[c]))
    decl = sorted((m, c) for (m, c) in DESLIGADAS if m in alvos)
    if decl:
        print("")
        print("DESLIGADAS POR DOUTRINA (o numero acima e' real, a "
              "decisao tambem):")
        for m, c in decl:
            print("  %-10s %-5s %s" % (m, c, DESLIGADAS[(m, c)]))
    print("\nmotores que violam o contrato: %d de %d — %s"
          % (len(sujos), len(alvos), ", ".join(sujos) or "nenhum"))
    return 1 if (a.gate and sujos) else 0


if __name__ == "__main__":
    sys.exit(main())
