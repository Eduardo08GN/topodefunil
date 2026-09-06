# -*- coding: utf-8 -*-
"""LANDINGS — DER ATEMANKER (de) / L'ANCRE DU SOUFFLE (fr).

    python build_landing.py de
    python build_landing.py fr
    python build_landing.py            -> os dois

Gera `de/index.html` e `fr/index.html`, cada um autossuficiente (CSS e SVG
inline), com as imagens ao lado ja' redimensionadas para a web.

⛔ O CSS E OS ICONES NAO SAO COPIADOS A MAO. Saem do `landing-150/index-de.html`,
que e' onde o sistema de design mora. Copiar 19 KB de CSS para ca' criaria uma
segunda fonte da verdade que diverge no primeiro ajuste — foi assim que o
conserto do texto-branco-sobre-card-branco chegou de graca nesta pagina.

⛔ UM BUILDER, DADOS POR IDIOMA (`copy_landing.TEXTOS`). Um
`build_landing_fr.py` seria a copia que diverge no primeiro conserto.

⏳ PENDENCIA DO OPERADOR: pagina comercial alema precisa de IMPRESSUM e
DATENSCHUTZERKLÄRUNG (TMG/DSGVO); a francesa precisa de MENTIONS LEGALES e
POLITIQUE DE CONFIDENTIALITE. Faltam os dados da empresa do Ed.
"""

import io
import os
import re
import shutil
import sys

from copy_landing import TEXTOS

AQUI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(AQUI)
REF = os.path.join(REPO, "landing-150", "index-de.html")
FOTOS = os.path.join(REPO, "ebook", "producao", "atem")

# ⏳ Trocado pelo link real assim que a Hotmart aprovar cada produto. Ate' la'
# aponta para a propria oferta na pagina — nunca para um `#` morto, que foi
# defeito medido nas tres landings do ebook 150.
CHECKOUT = {
    "de": "https://pay.hotmart.com/W107488023J?off=jnscv85r",  # produto 8464658
    "fr": "https://pay.hotmart.com/C107488941D?off=k45vfzlu",  # produto 8465131
}


def _ref_css_e_icones():
    s = io.open(REF, encoding="utf-8").read()
    css = re.search(r"<style>(.*?)</style>", s, re.S).group(1)
    defs = re.search(r"(<svg[^>]*>\s*<defs>.*?</defs>\s*</svg>)", s, re.S).group(1)
    return css, defs


EXTRA = """
/* ⛔ O CSS de referencia so' clareia `.lede` e `.eyebrow` dentro de
   `.sec-green` — dentro de `.problem` (fundo --ink, quase preto) eles ficam
   com a cor clara padrao --ink-soft, que e' cinza ESCURO. Medido:
   rgb(84,82,78) sobre rgb(26,26,26), ou seja, texto invisivel. */
.problem .lede{color:rgba(255,255,255,.88)}
.problem .eyebrow{color:#fff;background:rgba(255,255,255,.16)}
.problem .lede b{color:#fff}

h1 i{font-style:normal;color:var(--green);font-weight:900}
.sec-green h2 i,.problem h2 i{font-style:normal;color:var(--gold)}
.sec-white h2 i{font-style:normal;color:var(--green)}
.was{list-style:none;margin:0;padding:0;display:grid;gap:13px;max-width:760px}
.was li{position:relative;padding-left:30px;font-size:16.5px;line-height:1.6;
color:rgba(255,255,255,.9)}
.was li::before{content:"";position:absolute;left:0;top:9px;width:11px;height:11px;
border-radius:3px;background:var(--gold)}
.rcard p b{color:var(--ink);font-weight:800}
details.faq{border-top:1px solid var(--line);padding:16px 0}
details.faq summary{font-size:17.5px;font-weight:800;color:var(--ink);cursor:pointer;
list-style:none;position:relative;padding-right:28px}
details.faq summary::-webkit-details-marker{display:none}
details.faq summary::after{content:"+";position:absolute;right:4px;top:-2px;
font-size:24px;color:var(--green);font-weight:700}
details.faq[open] summary::after{content:"\\2013"}
details.faq p{margin-top:10px;color:var(--ink-soft);font-size:16.5px;line-height:1.65}
.card b{display:block;font-size:18px;line-height:1.3}
"""


def precorow(T):
    return ('<div class="pricehead"><span>%s <s>%s €</s></span>'
            '<span class="save">%s %s</span></div>'
            '<div class="price-row"><span class="now"><span class="cur">%s</span>%s'
            '<span class="cents">%s</span></span></div>'
            % (T["pb_statt"], T["preco_de"], T["desconto"], T["pb_sparen"],
               T["moeda_sinal"], T["preco"], T["centavos"]))


def pricebox(T, href):
    pay = "".join('<span><svg class="i"><use href="#%s"/></svg>%s</span>'
                  % (ic, tx) for ic, tx in zip(("ic-lock", "ic-mail", "ic-return"),
                                               T["pb_pay"]))
    return ('<div class="pricebox">' + precorow(T) +
            '<p class="once">%s</p>'
            '<a href="%s" class="btn">%s <svg class="i"><use href="#ic-arrow"/>'
            '</svg></a><div class="pay">%s</div></div>'
            % (T["pb_once"], href, T["pb_btn"], pay))


def corpo(T, checkout):
    b = []
    A = b.append

    # ⛔ TODO CTA VAI PARA O CHECKOUT, nao para `#offer`. Foi a decisao do Ed
    # nas tres landings do ebook 150, onde 4 botoes por pagina apontavam para
    # ancora interna e nenhum vendia. Botao que rola a pagina nao e' botao de
    # compra.
    A('<header class="topbar"><div class="wrap topbar-in">'
      '<div class="brand"><span class="brand-mark">%s</span> %s</div>'
      '<a href="%s" class="btn btn-sm">%s</a></div></header>'
      % (T["marca_mark"], T["marca"], checkout, T["btn_topo"]))

    badges = "".join('<span class="badge"><svg class="i"><use href="#%s"/></svg>'
                     '<b>%s</b> %s</span>' % bd for bd in T["hero_badges"])
    A('<section class="hero"><div class="wrap hero-grid"><div class="hero-copy">'
      '<span class="eyebrow">%s</span><h1>%s</h1><p class="lede">%s</p>'
      '<div class="badges">%s</div></div>'
      '<div class="hero-art"><img class="book" src="%s" alt="%s"></div>'
      '<div class="hero-price">%s</div></div></section>'
      % (T["hero_eyebrow"], T["hero_h1"], T["hero_lede"], badges,
         T["capa"], T["capa_alt"], pricebox(T, checkout)))

    A('<section class="sec problem"><div class="wrap">'
      '<div class="center kicker"><span class="eyebrow">%s</span><h2>%s</h2></div>'
      '<ul class="was" style="margin-top:30px">%s</ul>'
      '<p class="lede" style="margin-top:26px">%s</p></div></section>'
      % (T["prob_eyebrow"], T["prob_h2"],
         "".join("<li>%s</li>" % p for p in T["prob_itens"]), T["prob_punch"]))

    A('<section class="sec"><div class="wrap">'
      '<div class="center kicker"><span class="eyebrow">%s</span><h2>%s</h2>'
      '<p class="lede">%s</p></div>'
      '<div class="grid grid-3" style="margin-top:34px">%s</div></div></section>'
      % (T["feat_eyebrow"], T["feat_h2"], T["feat_lede"],
         "".join('<div class="card"><div class="ico"><svg class="i"><use href="#%s"/>'
                 '</svg></div><b>%s</b><p>%s</p></div>' % c for c in T["feat_cards"])))

    A('<section class="sec sec-white"><div class="wrap">'
      '<div class="center kicker"><span class="eyebrow">%s</span><h2>%s</h2>'
      '<p class="lede">%s</p></div>'
      '<div class="rail" style="margin-top:32px">%s</div>'
      '<p class="rail-hint"><svg class="i"><use href="#ic-swipe"/></svg>%s</p>'
      '</div></section>'
      % (T["rail_eyebrow"], T["rail_h2"], T["rail_lede"],
         "".join('<div class="rcard"><img src="%s.jpg" alt="%s">'
                 '<p><b>%s</b><br>%s</p></div>' % (f, t, t, d)
                 for f, t, d in T["rail_itens"]), T["rail_hint"]))

    A('<section class="sec"><div class="wrap"><div class="contentcard">'
      '<div class="head"><div class="ico"><svg class="i"><use href="#ic-book"/></svg>'
      '</div><h2 style="font-size:clamp(21px,3.2vw,28px)">%s</h2></div>'
      '<ul class="ticks">%s</ul></div></div></section>'
      % (T["cont_h2"], "".join("<li>%s</li>" % t for t in T["cont_ticks"])))

    A('<section class="sec sec-white"><div class="wrap">'
      '<div class="center kicker"><span class="eyebrow">%s</span><h2>%s</h2></div>'
      '<div class="grid grid-2" style="margin-top:34px">%s</div>'
      '<p class="center lede" style="margin-top:24px">%s</p></div></section>'
      % (T["bonus_eyebrow"], T["bonus_h2"],
         "".join('<div class="card bonus"><span class="bonus-tag">%s %s</span>'
                 '<div class="ico"><svg class="i"><use href="#%s"/></svg></div>'
                 '<b>%s</b><p>%s</p><div class="val"><s>%s €</s> %s</div></div>'
                 % (T["bonus_tag"], n, ic, tit, d, val, T["bonus_gratis"])
                 for n, ic, tit, d, val in T["bonus_itens"]), T["bonus_soma"]))

    A('<section class="sec"><div class="wrap">'
      '<div class="center kicker"><span class="eyebrow">%s</span><h2>%s</h2></div>'
      '<div class="grid grid-3" style="margin-top:34px">%s</div></div></section>'
      % (T["pass_eyebrow"], T["pass_h2"],
         "".join('<div class="step"><div class="n">%d</div><b>%s</b><p>%s</p></div>'
                 % (i + 1, t, d) for i, (t, d) in enumerate(T["pass_itens"]))))

    A('<section class="sec sec-green" id="offer"><div class="wrap">'
      '<div class="center kicker" style="margin-bottom:32px">'
      '<span class="eyebrow">%s</span><h2>%s</h2><p class="lede">%s</p></div>'
      '<div class="offer"><h3>%s</h3><ul class="ticks">%s</ul>'
      '<div class="rule"></div>%s<p class="once">%s</p>'
      '<a href="%s" class="btn btn-gold" style="margin-top:12px">%s '
      '<svg class="i"><use href="#ic-arrow"/></svg></a>'
      '<p class="btn-note">%s</p></div></div></section>'
      % (T["off_eyebrow"], T["off_h2"], T["off_lede"], T["off_h3"],
         "".join("<li>%s</li>" % t for t in T["off_ticks"]),
         precorow(T), T["off_once"], checkout, T["off_btn"], T["off_note"]))

    A('<section class="sec"><div class="wrap"><div class="guarantee">'
      '<div class="seal"><div><b>%s</b><span>%s</span></div></div><div>'
      '<h2 style="font-size:clamp(22px,3.4vw,30px)">%s</h2>'
      '<p style="color:var(--ink-soft);margin-top:12px">%s</p>'
      '<p style="color:var(--ink-soft);margin-top:12px;font-weight:700">%s</p>'
      '</div></div></div></section>'
      % (T["gar_dias"], T["gar_dias_lab"], T["gar_h2"], T["gar_p1"], T["gar_p2"]))

    A('<section class="sec sec-white"><div class="wrap">'
      '<div class="center kicker"><span class="eyebrow">%s</span><h2>%s</h2>'
      '<p class="lede">%s</p></div>'
      '<div class="grid grid-2" style="margin-top:34px">%s</div></div></section>'
      % (T["nicht_eyebrow"], T["nicht_h2"], T["nicht_lede"],
         "".join('<div class="card"><b>%s</b><p>%s</p></div>' % n
                 for n in T["nicht_itens"])))

    A('<section class="sec"><div class="wrap">'
      '<div class="center kicker" style="margin-bottom:32px">'
      '<span class="eyebrow">%s</span><h2>%s</h2></div>%s</div></section>'
      % (T["faq_eyebrow"], T["faq_h2"],
         "".join('<details class="faq"><summary>%s</summary><p>%s</p></details>'
                 % (q, a) for q, a in T["faq_itens"])))

    A('<section class="sec-tight sec-green center"><div class="wrap"><h2>%s</h2>'
      '<p class="lede" style="margin:12px auto 0;max-width:560px">%s</p>'
      '<a href="%s" class="btn btn-gold" style="margin-top:22px;max-width:420px">'
      '%s <svg class="i"><use href="#ic-arrow"/></svg></a></div></section>'
      % (T["cta_h2"], T["cta_lede"], checkout, T["cta_btn"]))

    A('<footer><div class="wrap">'
      '<div class="brand"><span class="brand-mark">%s</span> %s</div>'
      '<p>%s</p><p class="fine" style="margin-top:16px">%s</p></div></footer>'
      % (T["marca_mark"], T["marca"], T["rodape_direitos"], T["rodape_fine"]))

    return "\n".join(b)


def build(lang):
    T = TEXTOS[lang]
    css, defs = _ref_css_e_icones()
    doc = ("""<!doctype html><html lang="%s"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%s</title>
<meta name="description" content="%s">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<style>%s
%s</style></head><body>
%s
%s
</body></html>""" % (T["lang"], T["titulo_doc"], T["meta"], css, EXTRA, defs,
                     corpo(T, CHECKOUT[lang])))

    destino = os.path.join(AQUI, lang)
    if not os.path.isdir(destino):
        os.makedirs(destino)
    saida = os.path.join(destino, "index.html")
    io.open(saida, "w", encoding="utf-8").write(doc)

    # ⛔ Foto de ebook tem 1024px e ~650 KB. Numa landing isso e' 4,6 MB para
    # cards que aparecem com 3:4 — peso que o comprador paga em espera e o
    # anuncio paga em abandono. Entram reduzidas; a capa fica como esta'.
    from PIL import Image
    precisa = [T["capa"]] + ["%s.jpg" % f for f, _, _ in T["rail_itens"]]
    faltam = []
    for n in precisa:
        capa = n.startswith("capa")
        orig = os.path.join(FOTOS, n) if capa else os.path.join(FOTOS, "fotos", n)
        dst = os.path.join(destino, n)
        if not os.path.exists(orig):
            faltam.append(n)
            continue
        if capa:
            shutil.copy2(orig, dst)
        else:
            im = Image.open(orig).convert("RGB")
            im.thumbnail((620, 620), Image.LANCZOS)
            im.save(dst, quality=82, optimize=True)
    peso = sum(os.path.getsize(os.path.join(destino, f))
               for f in os.listdir(destino) if not f.startswith("_"))
    print("LANDING %s: %s  (html %.0f KB, pasta %.0f KB, %d/%d imagens)%s"
          % (lang.upper(), saida, os.path.getsize(saida) / 1024, peso / 1024,
             len(precisa) - len(faltam), len(precisa),
             "  FALTAM: " + " ".join(faltam) if faltam else ""))
    return saida


if __name__ == "__main__":
    alvos = [a for a in sys.argv[1:] if a in TEXTOS] or list(TEXTOS)
    for l in alvos:
        build(l)
