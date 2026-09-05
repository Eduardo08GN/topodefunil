# -*- coding: utf-8 -*-
"""BUILD — DER ATEMANKER. Gera as 7 PDFs do entregavel alemao.

    python build_atem.py            -> todos
    python build_atem.py 3 5        -> so' os Schritte 3 e 5

⛔ O HTML e' intermediario e descartavel (o `motor_atem.gerar_pdf` o apaga).
A pasta guarda so' os PDFs e a pasta `fotos/`.
"""

import sys

import motor_atem as M
import conteudo_atem as C1
import conteudo_atem2 as C2


def _ps(lista):
    return "".join("<p>%s</p>" % p for p in lista)


def _pares(lista):
    """(titulo, texto) -> paragrafo com o titulo em negrito na frente."""
    return "".join("<p><b>%s</b> %s</p>" % (t, d) for t, d in lista)


# ===========================================================================
# SCHRITT 1
# ===========================================================================

def schritt1():
    S = C1.S1
    c = [M.capa(S["badge"], S["titel"], S["lead"], S["foto"])]

    c.append(M.secao(S["willkommen_titel"], S["willkommen_sub"],
                     _ps(S["willkommen"])))

    paket = "".join(
        '<div class="tagcard"><div class="tnum"><s>%s</s><b>%s</b></div>'
        '<div><h4>%s</h4><p>%s</p></div></div>'
        % (a.split()[0].upper(), a.split()[-1], b, d)
        for a, b, d in S["paket"])
    c.append(M.secao(S["paket_titel"], S["paket_sub"], paket))

    c.append(M.secao(S["alarm_titel"], S["alarm_sub"],
                     '<img class="foto-larga" src="fotos/persona.jpg">'
                     + _ps(S["alarm"])))

    c.append(M.secao(S["ausatmen_titel"], S["ausatmen_sub"],
                     _ps(S["ausatmen"])
                     + '<div style="margin:16px 0">%s</div>' % M.svg_barra(4, 6)
                     + '<div style="margin:8px 0 4px">%s</div>' % M.svg_onda(4, 6, 0, 3)
                     + M.merk("Der eine Satz", S["ausatmen_merk"])))

    c.append(M.secao(S["ehrlich_titel"], S["ehrlich_sub"],
                     _pares(S["ehrlich"])))

    c.append(M.secao(S["sicher_titel"], S["sicher_sub"],
                     M.lista(S["sicher_regeln"])
                     + M.stop("Vorher fragen", S["sicher_arzt"])
                     + M.stop("Akute Krise", S["sicher_krise"])))

    c.append(M.secao(S["los_titel"], S["los_sub"],
                     M.passos(S["los"])
                     + M.merk("Ausdrucken", S["los_drucken"])))

    return M.montar("Fang hier an — Der Atemanker", "".join(c))


# ===========================================================================
# SCHRITT 2
# ===========================================================================

def schritt2():
    S = C1.S2
    c = [M.capa(S["badge"], S["titel"], S["lead"], S["foto"])]

    drei = "".join(
        '<div class="tagcard"><div class="tnum"><s>ANKER</s><b>%d</b></div>'
        '<div><h4>%s</h4><p>%s</p></div></div>' % (i + 1, t, d)
        for i, (t, d) in enumerate(S["drei"]))
    c.append(M.secao(S["drei_titel"], S["drei_sub"], drei))

    for u in S["uebungen"]:
        c.append(M.uebung(u["tag"], u["nome"], u["hook"], u["foto"], u["stats"],
                          u["ritmo"], u["schritte"], u["worauf"], u["sicher"]))

    c.append(M.secao(S["fehler_titel"], S["fehler_sub"], _pares(S["fehler"])))
    c.append(M.secao("Häufige Fragen", "", M.faq(S["faq"])))
    return M.montar("Der Atemanker", "".join(c))


# ===========================================================================
# SCHRITT 3
# ===========================================================================

def schritt3():
    S = C2.S3
    c = [M.capa(S["badge"], S["titel"], S["lead"], S["foto"])]

    c.append(M.secao(S["was_titel"], S["was_sub"],
                     _ps(S["was"]) + M.merk("Realistisch bleiben", S["was_merk"])))

    for u in S["uebungen"]:
        c.append(M.uebung(u["tag"], u["nome"], u["hook"], u["foto"], u["stats"],
                          u["ritmo"], u["schritte"], u["worauf"], u["sicher"]))

    c.append(M.secao(S["wenn_titel"], S["wenn_sub"], M.lista(S["wenn"])))

    linhas = "".join(
        '<tr><th style="width:44%%">%s</th><td class="leer">'
        '<span style="color:#9b978f;font-size:13.5px">%s</span></td></tr>'
        % (a, b) for a, b in S["plan_zeilen"])
    c.append(M.secao(S["plan_titel"], S["plan_sub"],
                     '<table class="log">%s</table>' % linhas
                     + M.stop("Wann es kein Fall für eine Atemübung ist",
                              S["plan_hinweis"])))
    return M.montar("Der Notfall-Anker", "".join(c))


# ===========================================================================
# SCHRITT 4
# ===========================================================================

def schritt4():
    S = C2.S4
    c = [M.capa(S["badge"], S["titel"], S["lead"], S["foto"])]

    c.append(M.secao(S["wie_titel"], S["wie_sub"],
                     M.lista(S["wie"]) + M.merk("Warum 21 Tage", S["wie_merk"])))

    for w in S["wochen"]:
        corpo = [M.wochekopf(w["rot"], w["titel"]), "<p>%s</p>" % w["text"]]
        for n, t, d in w["tage"]:
            corpo.append(M.tagcard(n, t, d))
        c.append(M.secao("", "", "".join(corpo)))

    c.append(M.secao(S["danach_titel"], S["danach_sub"], _ps(S["danach"])))

    # tabela de hakchen: 21 dias em 3 colunas de 7
    cab = "<tr>" + "".join(
        "<th>Tag</th><th>Geübt</th>" for _ in range(3)) + "</tr>"
    corpo = []
    for i in range(7):
        tds = []
        for col in range(3):
            d = i + 1 + col * 7
            tds.append('<td style="font-weight:800;color:#196B45">%d</td>'
                       '<td class="leer"></td>' % d)
        corpo.append("<tr>%s</tr>" % "".join(tds))
    c.append(M.secao(S["tabelle_titel"], S["tabelle_sub"],
                     '<table class="log">%s%s</table>' % (cab, "".join(corpo))))
    return M.montar("Dein 21-Tage-Plan", "".join(c))


# ===========================================================================
# SCHRITT 5
# ===========================================================================

def schritt5():
    S = C2.S5
    c = [M.capa(S["badge"], S["titel"], S["lead"], S["foto"])]
    c.append(M.secao(S["warum_titel"], S["warum_sub"], _ps(S["warum"])))
    for u in S["uebungen"]:
        c.append(M.uebung(u["tag"], u["nome"], u["hook"], u["foto"], u["stats"],
                          u["ritmo"], u["schritte"], u["worauf"], u["sicher"]))
    c.append(M.secao(S["stunde_titel"], S["stunde_sub"], _pares(S["stunde"])))
    c.append(M.secao("Häufige Fragen", "", M.faq(S["faq"])))
    return M.montar("Die Abendroutine", "".join(c))


# ===========================================================================
# SCHRITT 6
# ===========================================================================

def schritt6():
    S = C2.S6
    c = [M.capa(S["badge"], S["titel"], S["lead"], S["foto"], dourado=True)]
    c.append(M.secao(S["warum_titel"], S["warum_sub"], _ps(S["warum"])))
    c.append(M.secao(S["regeln_titel"], S["regeln_sub"],
                     M.lista(S["regeln"])
                     + M.stop("Wer diesen Bonus auslässt", S["regeln_wer"])))
    for u in S["uebungen"]:
        c.append(M.uebung(u["tag"], u["nome"], u["hook"], u["foto"], u["stats"],
                          u["ritmo"], u["schritte"], u["worauf"], u["sicher"]))
    tage = "".join(M.tagcard(n, t, d) for n, t, d in S["woche_tage"])
    c.append(M.secao(S["woche_titel"], S["woche_sub"], tage))
    return M.montar("Kälte ohne Eis", "".join(c))


# ===========================================================================
# SCHRITT 7
# ===========================================================================

def _tabela_vazia(colunas, linhas, primeira=None):
    cab = "<tr>%s</tr>" % "".join("<th>%s</th>" % c for c in colunas)
    corpo = []
    for i in range(linhas):
        tds = []
        for j in range(len(colunas)):
            if j == 0 and primeira:
                tds.append('<td style="font-weight:800;color:#196B45">%s</td>'
                           % primeira[i])
            else:
                tds.append('<td class="leer"></td>')
        corpo.append("<tr>%s</tr>" % "".join(tds))
    return '<table class="log">%s%s</table>' % (cab, "".join(corpo))


def schritt7():
    S = C2.S7
    DIAS = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
    c = [M.capa(S["badge"], S["titel"], S["lead"], S["foto"], dourado=True)]
    c.append(M.secao(S["warum_titel"], S["warum_sub"], _ps(S["warum"])))
    c.append(M.secao(S["wie_titel"], S["wie_sub"],
                     M.lista(S["wie"]) + M.merk("Zur Skala", S["wie_merk"])))

    for w in (1, 2, 3):
        c.append(M.secao("%s — Woche %d" % (S["wochen_titel"], w),
                         S["wochen_sub"] if w == 1 else "",
                         _tabela_vazia(S["wochen_spalten"], 7, DIAS)))

    c.append(M.secao(S["ausloeser_titel"], S["ausloeser_sub"],
                     _tabela_vazia(S["ausloeser_spalten"], 9)))

    fragen = "".join(
        '<div class="faq"><h4>%d. %s</h4><p>%s</p></div>'
        '<table class="log"><tr><td class="leer"></td></tr>'
        '<tr><td class="leer"></td></tr></table>' % (i + 1, q, d)
        for i, (q, d) in enumerate(S["abend_fragen"]))
    c.append(M.secao(S["abend_titel"], S["abend_sub"], fragen))

    c.append(M.secao(S["ende_titel"], S["ende_sub"],
                     _ps(S["ende"]) + M.merk("Zum Schluss", S["ende_schluss"])))
    return M.montar("Dein Ruhe-Tagebuch", "".join(c))


# ===========================================================================

PDFS = [
    (1, "Schritt 1 - Fang hier an.pdf", schritt1),
    (2, "Schritt 2 - Der Atemanker.pdf", schritt2),
    (3, "Schritt 3 - Der Notfall-Anker.pdf", schritt3),
    (4, "Schritt 4 - Dein 21-Tage-Plan.pdf", schritt4),
    (5, "Schritt 5 - Die Abendroutine.pdf", schritt5),
    (6, "Schritt 6 - Bonus 1 - Kaelte ohne Eis.pdf", schritt6),
    (7, "Schritt 7 - Bonus 2 - Dein Ruhe-Tagebuch.pdf", schritt7),
]


def main(quais=None):
    ok = True
    for n, nome, fn in PDFS:
        if quais and n not in quais:
            continue
        ok = M.gerar_pdf(fn(), nome, tmp="_tmp_s%d.html" % n) and ok
    return ok


if __name__ == "__main__":
    q = set(int(a) for a in sys.argv[1:] if a.isdigit())
    sys.exit(0 if main(q or None) else 1)
