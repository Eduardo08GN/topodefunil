"""Randomizador V6 — hook-first, com ledger anti-repeticao.

MUDANCA DE FILOSOFIA EM RELACAO AO V5
-------------------------------------
O v5 sorteava ELENCO (persona, etnia, setting, dispositivo). Isso e invisivel pro
espectador: dois videos com personas diferentes e a mesma historia parecem o mesmo
video. A engenharia reversa do Kofi&Simba (11 reels, 2026-07-27) mostrou que o
concorrente que performa faz o oposto — congela a historia e gira o HOOK.

O v6 inverte a verba de variacao:
- HOOK  = combinatorio e sempre novo (molde x substancia x prop x modificador x promessa)
- CORPO = espinha fixa validada (A/B/C), sorteada mas nao reescrita
- ELENCO = FIXO por pagina (um REF so, reaproveitado) — nao e mais eixo de sorteio

LEDGER
------
Para sustentar ~50 videos/dia sem repeticao, o sorteio nao pode ser sem memoria.
Cada spec emitida grava sua assinatura em `.ledger-v6.json`. Sorteios seguintes
rejeitam assinaturas ja usadas e preferem os valores menos usados de cada eixo
(least-recently-used), garantindo cobertura ampla antes de qualquer repeticao.

Uso:
  python randomizador-v6.py --pagina joe --n 10
  python randomizador-v6.py --pagina ray --n 50 --espinha A
  python randomizador-v6.py --stats            # o que o ledger ja gastou
  python randomizador-v6.py --listar           # eixos e valores
  python randomizador-v6.py --pagina joe --n 5 --dry-run   # nao grava no ledger
"""
import argparse
import hashlib
import json
import os
import random
import sys
from collections import Counter

LEDGER = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".ledger-v6.json")

# ---------------- pools (ver banco-hooks.md) ----------------

MOLDES = {
    "M1_substancia_absurda":   "Pour/Put [SUBST] on your [PROXY] and it will [PROMESSA]",
    "M2_consequencia_urgencia": "This is what happens when men ignore [X] too long. Do this before it's too late",
    "M3_diagnostico_triade":   "This is [cond]. This is [cond]. And this is [cond] too",
    "M4_reacao_demonstrada":   "Watch what happens when I add [A] to [B]",
    "M5_comando_social":       "[Comando]. If you're married, watch out brother, your wife won't keep up",
    "M6_antes_depois":         "You want your [proxy] to go from this to this in one month",
    "M7_isca_e_troca":         "[Promessa absurda]. You really think that's going to work?",
    "M8_combo_absurdo":        "Put [A] on [B] and reveal those hidden inches",
    "M9_confissao":            "Confissao em primeira pessoa (banco secao K)",
    "M10_pergunta_paradoxal":  "Pergunta que abre loop logico (banco secao L)",
    "M11_aviso_falso":         "Voz dela: 'Ladies, hide this from your husband'",
    "M12_prova_manha":         "A prova da manha (banco secao D)",
    "M13_medo_rival":          "O treinador de 28 anos (banco secao B)",
    "M14_ataque_industria":    "Acusacao abre o video (banco secao I)",
}

POOLS = {
    "molde": list(MOLDES),
    "substancia": ["toothpaste", "coca_cola", "baking_soda", "lime", "lemon",
                   "raw_garlic", "vaseline", "coconut_oil", "cinnamon", "turmeric",
                   "olive_oil", "raw_honey", "aloe", "apple_cider_vinegar",
                   "crushed_ice", "coffee"],
    "prop": ["banana", "cucumber", "watermelon", "geoduck", "daikon", "carrot",
             "zucchini", "corn", "eggplant", "sausage", "peach", "melon"],
    "modificador": ["pharma", "doctor", "ceticismo", "escassez", "insider", "nenhum"],
    "promessa": ["3_to_8_inches", "six_inches_two_weeks", "hidden_inches",
                 "this_to_this_one_month", "ten_times_bigger",
                 "different_man_by_morning", "wife_wont_keep_up", "five_inches_a_week"],
    "espinha": ["A", "B", "C"],
    "receita_isca": ["vaseline_honey_bakingsoda_coconut_gelatin",
                     "peach_milk_honey_gelatin_cinnamon",
                     "garlic_acv_cloves_tea",
                     "lime_water_bakingsoda_salt_acv",
                     "watermelon_beets_turmeric_honey",
                     "banana_cinnamon_ginger_lemon_honey"],
    "dor": ["momento_constrangedor", "desculpas_toda_noite", "gastos_farmacia",
            "medo_do_quarto", "fogo_apagando", "evitar_intimidade",
            "perda_confianca", "parceira_percebe", "efeitos_colaterais",
            "vergonha_medico"],
    "setting": ["kitchen", "guerrilha", "ranch"],
}

# Elenco fixo por pagina — NAO e sorteado (um REF por pagina, reaproveitado).
# Ver espinha-fixa.md e ARQUITETURA-OPERACAO.md.
PAGINAS = {
    "joe":    {"etnia": "branco", "espinha_default": "A", "dominio": "manresethub.pro"},
    "marcus": {"etnia": "negro",  "espinha_default": "A", "dominio": "vitalresetlab.site"},
    "ray":    {"etnia": "branco", "espinha_default": "B", "dominio": "primalvitalityhub.site"},
    "chuck":  {"etnia": "negro",  "espinha_default": "A", "dominio": "allmensnatural.site"},
    "matt":   {"etnia": "branco", "espinha_default": "C", "dominio": "steadystrengthhub.site"},
}

# CTA travado: a automacao Comentario->DM so dispara em variantes de gelatin.
# BOOK/YES nao existem como opcao. Ver espinha-fixa.md.
CTA_KEYWORD = "GELATIN"

# Selo de risco de bloqueio, aprendido em producao (ver banco-hooks.md).
# molde -> dispositivo visual seguro para a cena 1.
DISPOSITIVO_POR_MOLDE = {
    "M1_substancia_absurda":    "H1",   # proxy vertical no peito
    "M2_consequencia_urgencia": "H1",
    "M3_diagnostico_triade":    "H2",   # dois/tres estados etiquetados
    "M4_reacao_demonstrada":    "H7",   # pouring + crescimento
    "M5_comando_social":        "H1",
    "M6_antes_depois":          "H2",
    "M7_isca_e_troca":          "H8",
    "M8_combo_absurdo":         "H4",   # escala absurda, sem "oversized"
    "M9_confissao":             "H1",
    "M10_pergunta_paradoxal":   "H1",
    "M11_aviso_falso":          "H1",
    "M12_prova_manha":          "H1",
    "M13_medo_rival":           "H1",
    "M14_ataque_industria":     "H1",
}

# H9 nunca entra: bloqueia na politica do Veo (proxy na virilha). Ver banco-hooks.md.
DISPOSITIVOS_BANIDOS = {"H9"}

EIXOS_HOOK = ["molde", "substancia", "prop", "modificador", "promessa"]


def carregar_ledger():
    if not os.path.exists(LEDGER):
        return {"assinaturas": [], "uso": {}}
    try:
        with open(LEDGER, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        print(f"[aviso] ledger ilegivel, comecando limpo: {LEDGER}", file=sys.stderr)
        return {"assinaturas": [], "uso": {}}


def salvar_ledger(led):
    with open(LEDGER, "w", encoding="utf-8") as f:
        json.dump(led, f, indent=1)


def assinatura(row):
    """Identidade do hook. Duas specs com a mesma assinatura sao o mesmo video."""
    crua = "|".join(str(row[e]) for e in EIXOS_HOOK)
    return hashlib.sha1(crua.encode()).hexdigest()[:12]


def escolher_lru(eixo, uso, rng):
    """Sorteia preferindo os valores menos usados do pool (cobertura antes de repeticao)."""
    pool = POOLS[eixo]
    contagem = uso.get(eixo, {})
    minimo = min(contagem.get(v, 0) for v in pool)
    candidatos = [v for v in pool if contagem.get(v, 0) == minimo]
    return rng.choice(candidatos)


def montar(n, pagina, fixos, seed, led):
    rng = random.Random(seed)
    usados = set(led["assinaturas"])
    uso = {e: dict(led["uso"].get(e, {})) for e in POOLS}
    rows, tentativas_perdidas = [], 0

    while len(rows) < n:
        row = {}
        for eixo in POOLS:
            row[eixo] = fixos[eixo] if eixo in fixos else escolher_lru(eixo, uso, rng)

        sig = assinatura(row)
        if sig in usados:
            tentativas_perdidas += 1
            if tentativas_perdidas > 500:
                print(f"[aviso] espaco de hooks saturado apos {len(rows)} specs. "
                      f"Rode --reset-ledger ou amplie os pools em banco-hooks.md",
                      file=sys.stderr)
                break
            continue

        usados.add(sig)
        for eixo in EIXOS_HOOK + ["espinha", "receita_isca", "dor", "setting"]:
            uso.setdefault(eixo, {})
            uso[eixo][row[eixo]] = uso[eixo].get(row[eixo], 0) + 1

        row = reparar(row, pagina)
        row["_sig"] = sig
        rows.append(row)

    return rows, usados, uso


def reparar(row, pagina):
    """Restricoes duras: casting, setting, dispositivo seguro, CTA travado."""
    notas = []
    meta = PAGINAS[pagina]
    row["pagina"] = pagina
    row["etnia"] = meta["etnia"]
    row["dominio"] = meta["dominio"]
    row["cta_keyword"] = CTA_KEYWORD

    # dispositivo derivado do molde, nunca sorteado (selo de risco)
    disp = DISPOSITIVO_POR_MOLDE[row["molde"]]
    if disp in DISPOSITIVOS_BANIDOS:
        disp = "H1"
        notas.append("dispositivo banido=>H1")
    row["dispositivo"] = disp

    # etnia negra nunca em rancho (regra do V4)
    if row["setting"] == "ranch" and row["etnia"] == "negro":
        row["setting"] = "kitchen"
        notas.append("negro nao em ranch=>kitchen")

    # H7 (pouring+crescimento) exige prop que "cresce"
    if disp == "H7" and row["prop"] not in ("geoduck", "cucumber"):
        row["prop"] = "cucumber"
        notas.append("H7=>cucumber")

    # H8 (isca-e-troca) usa prop revestivel
    if disp == "H8" and row["prop"] in ("geoduck", "watermelon", "melon"):
        row["prop"] = "carrot"
        notas.append("H8=>carrot")

    # a isca NUNCA pode ser o mecanismo real (gelatin)
    if row["substancia"] == "gelatin":
        row["substancia"] = "coconut_oil"
        notas.append("isca==mecanismo=>troca")

    # receita_isca so importa na espinha A
    if row["espinha"] != "A":
        row["receita_isca"] = "-"

    row["_notas"] = ";".join(notas) if notas else "-"
    return row


def imprimir(rows, pagina, seed):
    meta = PAGINAS[pagina]
    print(f"# Specs V6 — pagina={pagina} ({meta['dominio']}) — etnia={meta['etnia']} "
          f"— seed={seed} — CTA travado={CTA_KEYWORD}")
    print(f"# {len(rows)} specs. Hook combinatorio + espinha fixa. Elenco NAO varia.\n")
    for i, r in enumerate(rows, 1):
        print(f"V{i:02d} [{r['_sig']}] espinha={r['espinha']} | {r['molde']}")
        print(f"     hook: subst={r['substancia']} prop={r['prop']} "
              f"mod={r['modificador']} promessa={r['promessa']} disp={r['dispositivo']}")
        print(f"     corpo: dor={r['dor']} setting={r['setting']} "
              f"isca={r['receita_isca']} cta={r['cta_keyword']}")
        if r["_notas"] != "-":
            print(f"     ajustes: {r['_notas']}")
        print()


def stats(led):
    total = len(led["assinaturas"])
    espaco = 1
    for e in EIXOS_HOOK:
        espaco *= len(POOLS[e])
    print(f"Ledger: {LEDGER}")
    print(f"Specs ja emitidas: {total}")
    print(f"Espaco combinatorio de hooks: {espaco:,} "
          f"({espaco/50:.0f} dias a 50 videos/dia)")
    print(f"Consumido: {100*total/espaco:.3f}%\n")
    for eixo in EIXOS_HOOK + ["espinha"]:
        c = Counter(led["uso"].get(eixo, {}))
        if not c:
            continue
        top = ", ".join(f"{k}={v}" for k, v in c.most_common(5))
        print(f"  {eixo}: {top}")


def main():
    ap = argparse.ArgumentParser(description="Randomizador V6 (hook-first + ledger)")
    ap.add_argument("--pagina", choices=list(PAGINAS), help="pagina alvo do lote")
    ap.add_argument("--n", type=int, default=10, help="quantas specs")
    ap.add_argument("--seed", type=int, default=None)
    ap.add_argument("--espinha", choices=POOLS["espinha"], help="travar a espinha")
    ap.add_argument("--molde", choices=list(MOLDES), help="travar o molde de hook")
    ap.add_argument("--dry-run", action="store_true", help="nao grava no ledger")
    ap.add_argument("--stats", action="store_true", help="uso acumulado do ledger")
    ap.add_argument("--listar", action="store_true")
    ap.add_argument("--reset-ledger", action="store_true", help="zera a memoria")
    a = ap.parse_args()

    if a.listar:
        print("Eixos e valores:\n")
        for eixo, vals in POOLS.items():
            print(f"  {eixo} ({len(vals)}): {', '.join(vals)}")
        print("\nMoldes de hook:")
        for k, v in MOLDES.items():
            print(f"  {k}: {v}")
        print(f"\nPaginas: {', '.join(PAGINAS)}")
        return 0

    led = carregar_ledger()

    if a.reset_ledger:
        salvar_ledger({"assinaturas": [], "uso": {}})
        print("Ledger zerado.")
        return 0

    if a.stats:
        stats(led)
        return 0

    if not a.pagina:
        print("--pagina e obrigatorio (ou use --stats / --listar)", file=sys.stderr)
        return 2

    fixos = {}
    if a.espinha:
        fixos["espinha"] = a.espinha
    else:
        fixos["espinha"] = PAGINAS[a.pagina]["espinha_default"]
    if a.molde:
        fixos["molde"] = a.molde

    seed = a.seed if a.seed is not None else random.randint(1, 10_000)
    rows, usados, uso = montar(a.n, a.pagina, fixos, seed, led)
    imprimir(rows, a.pagina, seed)

    if not a.dry_run:
        salvar_ledger({"assinaturas": sorted(usados), "uso": uso})
        print(f"# ledger atualizado: {len(usados)} specs ja emitidas no total")
    else:
        print("# dry-run: ledger NAO atualizado")
    return 0


if __name__ == "__main__":
    sys.exit(main())
