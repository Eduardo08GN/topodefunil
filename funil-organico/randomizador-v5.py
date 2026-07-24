"""Randomizador de specs para o Agente Organic Wave V5.

Tira a escolha criativa do modelo (que tem vies/mode-collapse) e transforma a
variacao em ESTATISTICA. Cada linha de saida e um conjunto de coordenadas
(mecanismo x persona x dispositivo x setting x staging x dor x hook x cta x prop)
que o agente V5 apenas EXECUTA — ele nao escolhe nenhum eixo nao-fixado.

Filosofia:
- Eixos FIXADOS pelo operador ficam constantes (o modelo pergunta antes).
- Eixos NAO fixados sao sorteados por round-robin com jitter: todos os valores do
  pool aparecem antes de qualquer repeticao (cobertura), com uma leve embaralhada
  pra nao virar sequencia obvia. Bem melhor que sorteio puro, que por azar repete
  o mesmo angulo em variacoes seguidas.
- Restricoes duras do nicho sao reparadas depois do sorteio (ex.: rancho so com
  gelatin; persona negra nunca em rancho; H5 implica setting guerrilha; H6/H7 usam
  prop geoduck/cucumber com liquido do mecanismo).

Uso:
  python randomizador-v5.py --n 8 --seed 42
  python randomizador-v5.py --n 8 --fix mecanismo=honey
  python randomizador-v5.py --n 10 --fix mecanismo=vick --fix persona=mulher_jovem
  python randomizador-v5.py --listar        # mostra os eixos e valores fixaveis
"""
import argparse
import random
import sys

# ---------------- pools (derivados do V4/V5) ----------------

POOLS = {
    "mecanismo":  ["honey", "vick", "gelatin", "custom"],
    "persona":    ["homem_velho", "mulher_jovem"],
    # personas especificas
    "mulher":     ["morena_tatuada", "loira_americana", "loira_russa",
                   "morena_cacheada", "ruiva", "morena_bronzeada"],
    "homem_etnia": ["branco", "negro"],
    "dispositivo": ["H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10"],
    "setting":    ["kitchen", "guerrilha", "ranch"],
    "staging":    ["solo", "casal"],
    "dor":        ["momento_constrangedor", "desculpas_toda_noite",
                   "gastos_farmacia", "medo_do_quarto", "fogo_apagando",
                   "evitar_intimidade", "perda_confianca", "parceira_percebe",
                   "efeitos_colaterais", "vergonha_medico"],
    "hook_style": ["comando_choque", "confissao", "pergunta", "ataque_industria", "rub_this_on"],
    # isca do H8 (rub-this-on): ingrediente banal esfregado, SEMPRE != mecanismo real
    "isca": ["vicks", "cinnamon", "turmeric", "coconut_oil", "olive_oil", "aloe"],
    "cta":        ["keyword_mecanismo", "book", "yes"],
    "prop":       ["geoduck", "cucumber", "carrot", "banana", "daikon", "zucchini"],
}

# eixos que o operador pode fixar (os demais sao derivados/reparados)
FIXAVEIS = ["mecanismo", "persona", "mulher", "homem_etnia", "dispositivo",
            "setting", "staging", "dor", "hook_style", "cta", "prop", "isca"]

# isca (H8) mapeada pro mecanismo que o "Trick" nomeia (a isca NUNCA e o mecanismo)
ISCA_PROIBIDA_POR_MEC = {"vick": "vicks", "honey": None, "gelatin": None, "custom": None}

LIQUIDO_POR_MEC = {
    "honey": "mel dourado espesso",
    "vick": "Vicks derretido (gel azul-esverdeado)",
    "gelatin": "gelatina liquida ambar-clara",
    "custom": "liquido do mecanismo custom",
}


def draw_balanced(pool, n, rng):
    """Round-robin com jitter: repete o pool ate cobrir n, embaralha cada ciclo
    (assim todos os valores saem antes de repetir, sem ordem obvia)."""
    out = []
    while len(out) < n:
        bloco = pool[:]
        rng.shuffle(bloco)
        out.extend(bloco)
    return out[:n]


def reparar(row):
    """Aplica as restricoes duras do nicho, ajustando o minimo necessario."""
    notas = []

    # H5 = dispositivo guerrilha -> setting guerrilha
    if row["dispositivo"] == "H5" and row["setting"] != "guerrilha":
        row["setting"] = "guerrilha"; notas.append("H5=>setting guerrilha")

    # rancho so existe pra gelatin
    if row["setting"] == "ranch" and row["mecanismo"] != "gelatin":
        row["setting"] = "kitchen"; notas.append("ranch so gelatin=>kitchen")

    # persona negra nunca em rancho
    if row["setting"] == "ranch" and row["persona"] == "homem_velho" \
            and row.get("homem_etnia") == "negro":
        row["homem_etnia"] = "branco"; notas.append("negro nao em ranch=>branco")

    # H6/H7 = pouring+crescimento: prop tem que ser geoduck ou cucumber
    if row["dispositivo"] in ("H6", "H7"):
        row["prop"] = "geoduck" if row["dispositivo"] == "H6" else "cucumber"
        row["liquido"] = LIQUIDO_POR_MEC[row["mecanismo"]]

    # vick + revestimento (H1/H3) casa melhor com cenoura
    if row["mecanismo"] == "vick" and row["dispositivo"] in ("H1", "H3") \
            and row["prop"] in ("geoduck", "cucumber"):
        row["prop"] = "carrot"; notas.append("vick H1/H3=>carrot")

    # H2 (day0/day7) usa geoduck por padrao
    if row["dispositivo"] == "H2":
        row["prop"] = "geoduck"

    # H9 (estado-problema ponta-pra-baixo) precisa de prop que "cai": banana/nabo
    if row["dispositivo"] == "H9" and row["prop"] not in ("banana", "daikon"):
        row["prop"] = "banana"; notas.append("H9=>banana")

    # H8 (rub-this-on) <-> hook_style rub_this_on andam juntos; usa prop revestivel
    if row["dispositivo"] == "H8" or row["hook_style"] == "rub_this_on":
        row["dispositivo"] = "H8"; row["hook_style"] = "rub_this_on"
        if row["prop"] in ("geoduck", "cucumber"):
            row["prop"] = "carrot"; notas.append("H8=>carrot")
        # a isca NUNCA pode ser o proprio mecanismo (ex.: vicks num video de vick)
        if row["isca"] == ISCA_PROIBIDA_POR_MEC.get(row["mecanismo"]):
            row["isca"] = "cinnamon" if row["isca"] != "cinnamon" else "coconut_oil"
            notas.append("isca==mecanismo=>troca")
    else:
        row["isca"] = "-"  # so relevante no H8

    # staging casal exige 2 corpos; ok em qualquer dispositivo
    # cta keyword casa com o mecanismo (book/yes = coleçao/oferta)
    if row["cta"] == "keyword_mecanismo":
        row["cta_keyword"] = {"honey": "HONEY", "vick": "VICK",
                              "gelatin": "GELATIN", "custom": "RECIPE"}[row["mecanismo"]]
    else:
        row["cta_keyword"] = row["cta"].upper()

    row["_notas"] = ";".join(notas) if notas else "-"
    return row


def montar(n, fixos, seed):
    rng = random.Random(seed)
    # eixos a sortear = todos os pools menos os fixados
    sorteados = {}
    for eixo in POOLS:
        if eixo in fixos:
            continue
        sorteados[eixo] = draw_balanced(POOLS[eixo], n, rng)

    rows = []
    for i in range(n):
        row = {}
        for eixo in POOLS:
            if eixo in fixos:
                row[eixo] = fixos[eixo]
            else:
                row[eixo] = sorteados[eixo][i]
        rows.append(reparar(row))
    return rows


def imprimir(rows, fixos, seed):
    print(f"# Specs V5 — seed={seed} — fixados: "
          + (", ".join(f"{k}={v}" for k, v in fixos.items()) if fixos else "(nenhum)"))
    print(f"# {len(rows)} variacoes. Colunas: persona detalhe so aparece conforme o tipo.\n")
    cols = ["mecanismo", "persona", "dispositivo", "setting", "staging",
            "prop", "hook_style", "dor", "cta_keyword"]
    for i, r in enumerate(rows, 1):
        pd = r["mulher"] if r["persona"] == "mulher_jovem" else f"homem_{r['homem_etnia']}"
        disp = r["dispositivo"] + (f"(isca:{r['isca']})" if r["dispositivo"] == "H8" else "")
        linha = " | ".join([
            f"V{i:02d}",
            r["mecanismo"], f"{r['persona']}({pd})", disp,
            r["setting"], r["staging"], r["prop"],
            r["hook_style"], r["dor"], f"CTA:{r['cta_keyword']}",
        ])
        print(linha)
        if r["_notas"] != "-":
            print(f"      ajustes: {r['_notas']}")


def main():
    ap = argparse.ArgumentParser(description="Randomizador de specs V5")
    ap.add_argument("--n", type=int, default=8, help="quantas variacoes")
    ap.add_argument("--seed", type=int, default=None, help="seed reproduzivel")
    ap.add_argument("--fix", action="append", default=[],
                    help="eixo=valor (repetivel). Ex: --fix mecanismo=honey")
    ap.add_argument("--listar", action="store_true", help="lista eixos fixaveis e valores")
    a = ap.parse_args()

    if a.listar:
        print("Eixos fixaveis e seus valores:\n")
        for eixo in FIXAVEIS:
            print(f"  {eixo}: {', '.join(POOLS[eixo])}")
        return 0

    fixos = {}
    for f in a.fix:
        if "=" not in f:
            print(f"--fix invalido: {f} (use eixo=valor)", file=sys.stderr); return 2
        k, v = f.split("=", 1)
        k, v = k.strip(), v.strip()
        if k not in FIXAVEIS:
            print(f"eixo nao fixavel: {k}. Veja --listar", file=sys.stderr); return 2
        if v not in POOLS[k]:
            print(f"valor invalido pra {k}: {v}. Opcoes: {POOLS[k]}", file=sys.stderr); return 2
        fixos[k] = v

    seed = a.seed if a.seed is not None else random.randint(1, 10_000)
    rows = montar(a.n, fixos, seed)
    imprimir(rows, fixos, seed)
    return 0


if __name__ == "__main__":
    sys.exit(main())
