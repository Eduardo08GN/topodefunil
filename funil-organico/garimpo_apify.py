# -*- coding: utf-8 -*-
"""GARIMPO VIA APIFY — a etapa 1 do PIPELINE-NOVO-AGENTE, sem sessao logada.

⛔⛔ O PROBLEMA QUE ISTO RESOLVE, e ele esta' escrito como divida no HORSE 16:
*"o pool de ACOES nasce com CINCO, nao generoso, e e' divida declarada: ele
deveria sair de 13 reels da WellnessMSimple, cuja listagem e' inalcancavel
(geo-bloqueio, depois checkpoint da Meta)"*. O garimpo manual depende do Chrome
logado do operador, e o Chrome logado do operador e' exatamente o que a Meta
bloqueia. O ator do Apify roda de datacenter, sem conta, sem cookie e sem
sessao — a pagina publica responde a ele.

⭐⭐ E ELE DEVOLVE A TRANSCRICAO (`captionText`). Isso colapsa os passos 1 e 2
da secao 4 do WORKFLOW (*"enumerar reels pelo Chrome logado -> transcripts em
--detail transcript"*) numa chamada so'.

⭐ O RANKING E' O DO REPO, nao o do Apify: **comentarios por mil views**. E' a
regua que separou os sete reels da fonte do BANHO 16 3T (exclusao 20,5 ·
idade+hack 11,8/7,5/5,6 · confissao 8,1 · rodeio 6,4 · pergunta 4,0), e foi ela
que revelou que o campeao era o unico SEM MECANISMO. Ordenar por views
devolveria a pagina inteira na ordem do algoritmo; ordenar por comentario/mil
devolve na ordem do que o NOSSO funil compra.
⚠️ Com um piso de views: 3 comentarios em 40 views dao 75/mil e nao significam
nada. `--piso-views` existe para o topo da lista nao virar ruido.

USO
    set APIFY_TOKEN=apify_api_xxx        (ou --token, ou .apify-token na raiz)
    python funil-organico/garimpo_apify.py --pagina WellnessMSimple --n 60
    python funil-organico/garimpo_apify.py --pagina a --pagina b --n 40 --so-video

SAIDA
    concorrentes/<slug>-garimpo.md      o relatorio ranqueado, para leitura
    concorrentes/<slug>-garimpo.json    o bruto, porque medicao se refaz

⚠️ CUSTO: US$ 2,00 por 1.000 posts, e a conta gratuita da US$ 5,00 de credito
por mes. Um garimpo de 60 posts custa ~US$ 0,12 — o volume deste repo cabe
folgado no credito gratuito. O script IMPRIME a estimativa antes de rodar.

⛔ SO' PAGINAS PUBLICAS, e so' o que a pagina publica ja' exibe: e' a mesma
leitura que o operador faz a olho, feita em lote. Nada de conta, login, cookie
ou conteudo restrito.
"""
import argparse
import io
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DESTINO = os.path.join(RAIZ, "concorrentes")
ATOR = "apify~facebook-posts-scraper"
BASE = "https://api.apify.com/v2"


# ---------------------------------------------------------------------------
# TOKEN — tres origens, e NENHUMA e' o codigo
# ---------------------------------------------------------------------------
# ⛔ Token nunca entra no fonte: este arquivo e' versionado e o repo tem outro
# autor empurrando na main.
def ler_token(arg):
    if arg:
        return arg.strip()
    env = os.environ.get("APIFY_TOKEN", "").strip()
    if env:
        return env
    caminho = os.path.join(RAIZ, ".apify-token")
    if os.path.exists(caminho):
        with io.open(caminho, encoding="utf-8") as f:
            return f.read().strip()
    return ""


def _http(url, dados=None, metodo="GET"):
    corpo = json.dumps(dados).encode("utf-8") if dados is not None else None
    req = urllib.request.Request(url, data=corpo, method=metodo)
    req.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(req, timeout=180) as r:
        txt = r.read().decode("utf-8")
    return json.loads(txt) if txt.strip() else {}


def rodar_ator(token, urls, n, transcricao=True):
    """Dispara o ator e espera. Devolve a lista de itens do dataset."""
    entrada = {
        "startUrls": [{"url": u} for u in urls],
        "resultsLimit": n,
        # ⭐ e' esta linha que traz o TRANSCRIPT — o passo que o `/watch` fazia
        # a parte e' o que mais custa tempo no garimpo manual.
        "captionText": bool(transcricao),
    }
    print("  disparando o ator (%d pagina(s), teto %d posts)..." % (len(urls), n))
    run = _http("%s/acts/%s/runs?token=%s" % (BASE, ATOR, token), entrada, "POST")
    rid = run["data"]["id"]
    print("  run %s — esperando" % rid, end="", flush=True)
    for _ in range(240):                      # ate' ~20 min
        time.sleep(5)
        st = _http("%s/actor-runs/%s?token=%s" % (BASE, rid, token))["data"]
        if st["status"] in ("SUCCEEDED", "FAILED", "ABORTED", "TIMED-OUT"):
            print(" -> " + st["status"])
            if st["status"] != "SUCCEEDED":
                raise SystemExit("o ator terminou em %s" % st["status"])
            ds = st["defaultDatasetId"]
            return _http("%s/datasets/%s/items?token=%s&clean=true"
                         % (BASE, ds, token))
        print(".", end="", flush=True)
    raise SystemExit("tempo esgotado esperando o ator")


# ---------------------------------------------------------------------------
# A REGUA DO REPO
# ---------------------------------------------------------------------------
def _int(v):
    try:
        return int(v or 0)
    except (TypeError, ValueError):
        return 0


# ⚠️ `isVideo` E' CAMPO DO ATOR, e eu tinha escrito uma heuristica antes de
# medir o retorno de verdade. A medicao (10 posts da DrEricBerg) mostrou o
# campo pronto no dataset — heuristica minha em cima de dado que ja' existe e'
# so' uma chance a mais de errar.
def e_video(p):
    if p.get("isVideo") is not None:
        return bool(p.get("isVideo"))
    return bool(p.get("viewsCount") or p.get("videoPostViewCount")
                or "/reel/" in str(p.get("url", "")))


def medir(p):
    views = _int(p.get("viewsCount"))
    com = _int(p.get("comments"))
    curt = _int(p.get("likes"))
    comp = _int(p.get("shares"))
    return {
        "url": p.get("url", ""),
        "data": (p.get("time") or "")[:10],
        "views": views, "comentarios": com, "curtidas": curt, "shares": comp,
        # ⭐ A METRICA. Comentario e' o que dispara a DM; view nao compra nada.
        "com_mil": round(com * 1000.0 / views, 1) if views else None,
        "curt_mil": round(curt * 1000.0 / views, 1) if views else None,
        "texto": " ".join((p.get("text") or "").split())[:400],
        "transcricao": " ".join((p.get("captionText") or "").split()),
        "video": e_video(p),
    }


def relatorio(slug, linhas, piso):
    fortes = [x for x in linhas if x["com_mil"] is not None
              and x["views"] >= piso]
    fortes.sort(key=lambda x: -x["com_mil"])
    sem = [x for x in linhas if x not in fortes]
    med = sorted(x["com_mil"] for x in fortes)
    mediana = med[len(med) // 2] if med else 0

    out = []
    w = out.append
    w("# GARIMPO — %s\n" % slug)
    w("> Ranqueado por **comentarios por mil views**, que e' o que o nosso funil")
    w("> compra: o comentario dispara a DM, a view nao compra nada. Piso de")
    w("> **%d views** para o topo da lista nao virar ruido de amostra pequena.\n" % piso)
    w("**%d posts** · %d com views acima do piso · mediana **%s** com/mil\n"
      % (len(linhas), len(fortes), mediana))
    w("| # | com/mil | views | com | curt | data | abertura da fala |")
    w("|---|---|---|---|---|---|---|")
    for i, x in enumerate(fortes[:40], 1):
        abre = (x["transcricao"] or x["texto"] or "")[:90]
        w("| %d | **%s** | %d | %d | %d | %s | %s |"
          % (i, x["com_mil"], x["views"], x["comentarios"], x["curtidas"],
             x["data"], abre.replace("|", "/")))
    if sem:
        w("\n⚠️ **%d posts fora do ranking** (sem views ou abaixo do piso) — "
          "eles continuam no `.json`." % len(sem))

    w("\n## As transcricoes dos %d melhores\n" % min(10, len(fortes)))
    w("⛔ E' daqui que sai o pool, e **nunca de invencao**: entrada nova de")
    w("pool sai de leitura de video. A regra e' do HORSE 16 e vale para todos.\n")
    for i, x in enumerate(fortes[:10], 1):
        w("### %d. %s com/mil · %d views" % (i, x["com_mil"], x["views"]))
        w("%s\n" % x["url"])
        if x["transcricao"]:
            w("> " + x["transcricao"][:1200] + "\n")
        else:
            w("> *(sem transcricao — o reel nao tem legenda automatica; "
              "cai para leitura otica manual)*\n")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description="Garimpo de paginas do Facebook via Apify")
    ap.add_argument("--pagina", action="append", required=True,
                    help="slug ou URL da pagina (pode repetir)")
    ap.add_argument("--n", type=int, default=50, help="teto de posts POR RODADA")
    ap.add_argument("--piso-views", type=int, default=300,
                    help="views minimas para entrar no ranking (padrao 300)")
    ap.add_argument("--so-video", action="store_true",
                    help="descarta post que nao e' video/reel")
    ap.add_argument("--sem-transcricao", action="store_true")
    ap.add_argument("--token", default="")
    ap.add_argument("--dry-run", action="store_true",
                    help="so' mostra o custo e a entrada, nao chama a API")
    a = ap.parse_args()

    token = ler_token(a.token)
    if not token and not a.dry_run:
        raise SystemExit(
            "sem token. Use uma das tres:\n"
            "  set APIFY_TOKEN=apify_api_xxx\n"
            "  --token apify_api_xxx\n"
            "  grave o token em %s" % os.path.join(RAIZ, ".apify-token"))

    urls = [p if p.startswith("http") else "https://www.facebook.com/" + p
            for p in a.pagina]
    custo = len(urls) * a.n * 2.0 / 1000.0
    print("paginas: %s" % ", ".join(urls))
    print("custo estimado: US$ %.2f  (US$ 2,00 / 1.000 posts · o plano gratuito "
          "da' US$ 5,00/mes)" % custo)
    if a.dry_run:
        return

    itens = rodar_ator(token, urls, a.n, not a.sem_transcricao)
    print("  %d item(ns) no dataset" % len(itens))

    linhas = [medir(p) for p in itens]
    if a.so_video:
        antes = len(linhas)
        linhas = [x for x in linhas if x["video"]]
        print("  --so-video: %d de %d" % (len(linhas), antes))

    if not os.path.isdir(DESTINO):
        os.makedirs(DESTINO)
    # ⚠️ Pagina nova do Facebook nao tem vanity URL — ela vem como
    # `profile.php?id=615917...`. Sem este ramo o arquivo saia
    # `profile-php-id-615917-sk-reels-tab`, ilegivel na pasta.
    m_id = re.search(r"[?&]id=(\d+)", urls[0])
    slug = ("fb-" + m_id.group(1)) if m_id else (
        re.sub(r"[^a-z0-9]+", "-",
               urls[0].rstrip("/").split("/")[-1].lower()).strip("-") or "garimpo")
    pj = os.path.join(DESTINO, "%s-garimpo.json" % slug)
    pm = os.path.join(DESTINO, "%s-garimpo.md" % slug)
    with io.open(pj, "w", encoding="utf-8") as f:
        json.dump(itens, f, ensure_ascii=False, indent=1)
    with io.open(pm, "w", encoding="utf-8") as f:
        f.write(relatorio(slug, linhas, a.piso_views))
    print("  -> %s" % pm)
    print("  -> %s  (bruto)" % pj)

    com = [x["com_mil"] for x in linhas
           if x["com_mil"] is not None and x["views"] >= a.piso_views]
    if com:
        com.sort(reverse=True)
        print("\n  melhores com/mil: %s" % ", ".join(str(c) for c in com[:8]))
        print("  a sua regua: BANHO 16 3T teve 20,5 no campeao e 4,0 no pior")


if __name__ == "__main__":
    main()
