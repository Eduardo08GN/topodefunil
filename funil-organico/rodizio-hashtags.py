# -*- coding: utf-8 -*-
"""
⚠️ CÓPIA VERSIONADA da ferramenta do LUCAS. O original roda em
`Desktop/Angulos/gerar-calendario-hashtags.py`, e e' la' que ele executa — os
caminhos apontam para a area de trabalho dele.

Esta' aqui por ordem dele, para o Ed ter acesso ao METODO. O que se aproveita
nao e' o caminho: e' o RODIZIO POR DESLOCAMENTO, que resolve com uma linha de
conta um problema que o Ed tambem tem com as paginas dele — 10 paginas
postando as mesmas hashtags no mesmo dia competem entre si.

⛔ NAO EDITAR ESTA COPIA esperando efeito. A fonte de verdade e' a do
Desktop; esta e' registro. Mudanca real entra la' e volta para ca' por copia.
"""
"""
⭐⭐ ESTE ARQUIVO E' O MESTRE. Os 30 combos moram AQUI DENTRO, na constante
COMBOS. Os `.txt` que ele gera sao DESCARTAVEIS: o operador apaga o combo
conforme usa, e quando acabar e' so' rodar isto de novo.

    python gerar-calendario-hashtags.py

⛔ NAO apagar nem editar este arquivo para "marcar o que ja' usei". Apague nos
   `Calendario-Hashtags.txt` das pastas das paginas, que sao a copia de
   trabalho. Se este arquivo se perder, perde-se a fonte de tudo.

O PROBLEMA QUE ISTO RESOLVE
---------------------------
Havia um `Hashtags.txt` IDENTICO na pasta de cada pagina. Como os combos estao
na mesma ordem em todos, toda pagina comeca pelo combo 1 — no mesmo dia as 10
paginas disputam as MESMAS hashtags, que e' o oposto do que se queria. E
marcar na mao nao coordena: um arquivo nao ve' o outro.

A REGRA, EM UMA LINHA
---------------------
    post k da pagina i  ->  combo (3*i + k) % 30

  [1] ZERO COLISAO ENTRE PAGINAS. No mesmo indice de post, duas paginas so'
      cairiam no mesmo combo se 3i ≡ 3j (mod 30), o que exige i = j. Como
      cada pagina posta 3x, um dia inteiro consome 10x3 = 30 combos: a grade
      fecha exata, cada combo usado uma vez por dia.

  [2] OS 30 ANTES DE REPETIR. A pagina anda de 1 em 1 pelos combos; ela so'
      volta ao primeiro depois de passar pelos 30 (= 10 dias a 3 posts/dia).

⛔ O TETO E' MATEMATICO: sao 30 combos e 10 paginas. A 3 posts/dia a grade
   fecha no limite. Para 4 posts/dia seriam precisos 40 combos — o script
   RECUSA a configuracao em vez de gerar um calendario que mente.

⚠️ SEM DATAS, DE PROPOSITO (ordem do operador): tem dia que ele nao posta. Se
   o calendario fosse por data, um dia pulado desalinharia tudo. A lista e'
   uma FILA: usou, apaga, o proximo sobe.
"""
import argparse
import io
import os
import re
import sys

for _f in (sys.stdout, sys.stderr):
    try:
        _f.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

AQUI = os.path.dirname(os.path.abspath(__file__))
PAGINAS_DIR = os.path.join(os.path.dirname(AQUI), "Páginas")

# ---------------------------------------------------------------------------
# ⭐ OS 30 COMBOS — A FONTE DA VERDADE
# ---------------------------------------------------------------------------
# 1-20: leva original.  21-30: leva de 2026-08-06, com 30 hashtags INEDITAS
# (conferido contra as 40 antigas; assert de carga abaixo).
# ⛔ Toda hashtag aparece no maximo 2x no conjunto — foi a regra do operador
# quando as 20 primeiras nasceram, e vale para as novas.
COMBOS = [
 ("Comment GELATIN and I'll send you the full recipe \U0001F4E9",
  "#menshealth #menswellness #lowtestosterone"),
 ("Comment GELATIN and I'll send you the recipe in full \U0001F4EC",
  "#menswellness #malevitality #menover50"),
 ("I can't post the recipe here. Comment GELATIN and I'll send it \U0001F92C",
  "#malevitality #testosterone #menover60"),
 ("Comment GELATIN for the whole recipe, measurements and all \U0001F4CB",
  "#testosterone #usareels #circulation"),
 ("Comment GELATIN and I'll send you the complete instructions \U0001F513",
  "#usareels #healthtips #staminaboost"),
 ("Comment GELATIN and I'll send you the rest of the recipe \U0001F517",
  "#healthtips #healthylifestyle #energyboost"),
 ("Comment GELATIN and I'll send exactly what to buy and how much \U0001F6D2",
  "#healthylifestyle #naturalremedies #kitchenremedy"),
 ("Comment GELATIN and follow me, so the recipe can reach you \U0001F514",
  "#naturalremedies #menover40 #grandpasremedy"),
 ("Comment GELATIN and I'll send what the video left out \U0001F9E9",
  "#menover40 #usa #oldremedies"),
 ("Comment GELATIN and I'll send the recipe written out step by step \U0001F4DD",
  "#usa #mensfitness #agingwell"),
 ("Comment GELATIN and I'll send the complete list of ingredients ✅",
  "#mensfitness #wellness #nutritiontips"),
 ("Comment GELATIN and I'll send the ingredient nobody mentions \U0001F4E9",
  "#wellness #homeremedies #superfoods"),
 ("Comment GELATIN and I'll send the step almost everyone skips ⚠️",
  "#homeremedies #malehealth #gelatinrecipe"),
 ("Comment GELATIN and the full recipe lands in your messages right now ⚡",
  "#malehealth #healthyaging #feelyounger"),
 ("Comment GELATIN and I'll send the whole thing, free \U0001F381",
  "#healthyaging #bloodflow #dailyhabits"),
 ("Comment GELATIN and I'll send it before you forget ⏳",
  "#bloodflow #strongerman #naturalhealing"),
 ("Comment GELATIN and I'll send the recipe I use myself \U0001F44C",
  "#strongerman #americanmen #vitality"),
 ("Comment GELATIN and I'll send the full method to your inbox \U0001F4E7",
  "#americanmen #wellnesstips #manpower"),
 ("Comment GELATIN and follow me for the full recipe in your DMs \U0001F4EC",
  "#mensdaily #healthyman #usamen"),
 ("Comment GELATIN and I'll send the complete recipe right now ⚡",
  "#healthyman #menshealth #manpower"),
 ("Comment GELATIN and I'll send the recipe straight to you \U0001F4E5",
  "#bloodcirculation #hearthealth #prostatehealth"),
 ("Comment GELATIN and the full method goes to your inbox \U0001F4E8",
  "#midlifehealth #menover70 #seniorhealth"),
 ("Comment GELATIN and I'll send the amounts and the order \U0001F4D0",
  "#naturalboost #herbalremedy #folkremedy"),
 ("Comment GELATIN and I'll send the written version of this \U0001F4C4",
  "#ancientremedy #grandmasrecipe #kitchencures"),
 ("Comment GELATIN and I'll send the details the video skipped \U0001F3AC",
  "#foodismedicine #simplerecipe #twoingredients"),
 ("Comment GELATIN and I'll send the one detail most people miss \U0001F50D",
  "#collagenboost #gelatintrick #beetroot"),
 ("Comment GELATIN and I'll send the recipe my grandfather used \U0001F474",
  "#morningroutine #dailyritual #healthyhabits"),
 ("Comment GELATIN and I'll send the whole thing, start to finish \U0001F9FE",
  "#selfcareformen #fitover50 #strengthafter50"),
 ("Comment GELATIN and I'll send how often to take it ⏱️",
  "#dadenergy #americanhealth #homekitchen"),
 ("Comment GELATIN and I'll send it, no strings attached \U0001F381",
  "#realfood #betterwithage #mensroutine"),
]

# ⛔ asserts de carga: o mestre nao pode degradar em silencio numa edicao futura
_tags = [h for _c, t in COMBOS for h in t.split()]
assert len(COMBOS) == 30, "sao 30 combos, achei %d" % len(COMBOS)
assert all(len(t.split()) == 3 for _c, t in COMBOS), "todo combo tem 3 hashtags"
assert max(_tags.count(h) for h in set(_tags)) <= 2, "hashtag usada 3x ou mais"
assert len({c for c, _t in COMBOS}) == 30, "legenda repetida"

# ⚠️ A ORDEM DAS PAGINAS E' O QUE DA' O DESLOCAMENTO DE CADA UMA. Reordenar
# reembaralha o calendario inteiro; pagina nova entra NO FIM.
PAGINAS = [
    ("Reggie Harris",        "Reggie"),
    ("Jennifer Miller",      "Jennifer"),
    ("Denise Walker",        "Denise"),
    ("Wayne Miller",         "Wayne"),
    ("Otis & Gloria",        "Otis"),
    ("Dale Pruitt",          "Dale"),
    ("Curtis Grant",         "Curtis"),
    ("Carol Whitfield",      "Carol"),
    ("Yvonne Bradley",       "Yvonne"),
    ("Hank & Marlene Daily", "Hank"),
]


def achar_pasta(marca):
    """Casa por trecho do nome — sobrevive a renomeacao (o operador ja'
    prefixou algumas pastas com `[IA]`)."""
    for grupo in ("Negros", "Brancos"):
        d = os.path.join(PAGINAS_DIR, grupo)
        if not os.path.isdir(d):
            continue
        for nome in os.listdir(d):
            if marca.lower() in nome.lower():
                return os.path.join(d, nome)
    return None


def combo_de(i, k, posts):
    """A regra inteira, num lugar so'."""
    return (posts * i + k) % len(COMBOS)


def main():
    ap = argparse.ArgumentParser(description="Fila de hashtags por pagina")
    ap.add_argument("--posts", type=int, default=3, help="posts/dia por pagina")
    ap.add_argument("--ciclos", type=int, default=3,
                    help="quantas voltas completas gerar (1 volta = 30 posts)")
    ap.add_argument("--limpar", action="store_true",
                    help="apaga os Hashtags.txt antigos das pastas")
    a = ap.parse_args()

    n, p = len(COMBOS), len(PAGINAS)
    print("%d combos | %d paginas | %d posts/dia" % (n, p, a.posts))
    if p * a.posts > n:
        print("\n⛔ IMPOSSIVEL: %d x %d = %d combos por dia, e so' existem %d."
              "\n   Reduza para %d post(s)/dia, ou acrescente %d combos."
              % (p, a.posts, p * a.posts, n, n // p, p * a.posts - n))
        return 1

    total = n * a.ciclos
    escritos, apagados, faltando = 0, 0, []
    for i, (nome, marca) in enumerate(PAGINAS):
        pasta = achar_pasta(marca)
        if not pasta:
            faltando.append(nome)
            continue
        if a.limpar:
            velho = os.path.join(pasta, "Hashtags.txt")
            if os.path.isfile(velho):
                os.remove(velho)
                apagados += 1
        # ⚠️ SEM INDENTACAO no corpo: o operador copia e cola direto, e espaco
        # a esquerda vira trabalho de apagar a mao em cada post.
        L = ["FILA DE HASHTAGS — %s" % nome,
             "=" * 60,
             "Use de cima para baixo. USOU, APAGUE o bloco.",
             "Nenhuma outra pagina usa estes combos na mesma rodada, e esta",
             "pagina so' repete um combo depois de passar pelos %d." % n,
             "Quando acabar: rode gerar-calendario-hashtags.py de novo.",
             ""]
        for k in range(total):
            c = combo_de(i, k, a.posts)
            cap, tags = COMBOS[c]
            L += ["-" * 60, "%s" % cap, "%s" % tags, ""]
        io.open(os.path.join(pasta, "Fila-Hashtags.txt"), "w",
                encoding="utf-8", newline="\r\n").write("\n".join(L))
        # o calendario antigo (com datas) sai de cena
        antigo = os.path.join(pasta, "Calendario-Hashtags.txt")
        if os.path.isfile(antigo):
            os.remove(antigo)
        escritos += 1

    # grade geral — quem usa o que, por rodada
    G = ["GRADE — os combos de cada pagina, rodada a rodada", "=" * 66,
         "1 rodada = 1 dia a %d posts. Zero colisao entre paginas." % a.posts,
         ""]
    for r in range(total // a.posts):
        G.append("── rodada %d" % (r + 1))
        for i, (nome, _m) in enumerate(PAGINAS):
            cs = [combo_de(i, r * a.posts + s, a.posts) + 1
                  for s in range(a.posts)]
            G.append("   %-22s %s" % (nome, ", ".join("%02d" % c for c in cs)))
        G.append("")
    io.open(os.path.join(AQUI, "GRADE-Hashtags.txt"), "w",
            encoding="utf-8", newline="\r\n").write("\n".join(G))

    # ---- PROVA das duas regras, medida ----
    colisoes = 0
    for r in range(total // a.posts):
        usados = [combo_de(i, r * a.posts + s, a.posts)
                  for i in range(p) for s in range(a.posts)]
        colisoes += len(usados) - len(set(usados))
    repet = 0
    for i in range(p):
        for ini in range(total - n + 1):
            j = [combo_de(i, k, a.posts) for k in range(ini, ini + n)]
            repet += len(j) - len(set(j))

    print("\nPROVA (medida, nao prometida)")
    print("  [1] mesma rodada, paginas diferentes: %d colisoes em %d rodadas"
          % (colisoes, total // a.posts))
    print("  [2] dentro da pagina, qualquer janela de %d posts: %d repeticoes"
          % (n, repet))
    print("\n%d filas escritas (%d posts cada)." % (escritos, total))
    if apagados:
        print("%d Hashtags.txt antigos apagados." % apagados)
    if faltando:
        print("⚠️ sem pasta: %s" % ", ".join(faltando))
    return 0 if not (colisoes or repet) else 1


if __name__ == "__main__":
    raise SystemExit(main())
