# -*- coding: utf-8 -*-
"""BUILD — ATEMANKER / L'ANCRE DU SOUFFLE. Gera as 7 PDFs de um idioma.

    python build_atem.py de          -> os 7 alemaes
    python build_atem.py fr          -> os 7 franceses
    python build_atem.py fr 3 5      -> so' as etapas 3 e 5 do frances

⛔⛔ UM BUILDER, NAO UM POR IDIOMA. O que muda entre alemao e frances sao os
DADOS (`conteudo_atem*`), incluindo os rotulos fixos de interface (`ROT`) e os
nomes dos arquivos (`ARQUIVOS`). O motor e este builder sao os mesmos — a
doutrina do repo e' uma ferramenta por funcao, nunca uma copia por idioma, e um
`build_atem_fr.py` seria a copia que diverge no primeiro conserto.

⛔ O HTML e' intermediario e descartavel (o `motor_atem.gerar_pdf` o apaga).
"""

import importlib
import sys

import motor_atem as M

# ⭐ Mapa de idioma -> par de modulos de dados. O alemao nasceu sem sufixo
# porque foi o primeiro; renomear custaria mexer no que ja' esta' aprovado.
IDIOMAS = {
    "de": ("conteudo_atem", "conteudo_atem2"),
    "fr": ("conteudo_atem_fr", "conteudo_atem2_fr"),
}


def _ps(lista):
    return "".join("<p>%s</p>" % p for p in lista)


def _pares(lista):
    return "".join("<p><b>%s</b> %s</p>" % (t, d) for t, d in lista)


class Livro(object):
    """Renderiza os 7 PDFs a partir de um par de modulos de dados."""

    def __init__(self, lang):
        m1, m2 = IDIOMAS[lang]
        self.lang = lang
        self.C1 = importlib.import_module(m1)
        self.C2 = importlib.import_module(m2)
        self.R = self.C1.ROT
        self.ARQ = self.C1.ARQUIVOS
        self.TIT = self.C1.TITULOS_DOC

    # -- helpers ---------------------------------------------------------
    def _card(self, u):
        return M.uebung(u["tag"], u["nome"], u["hook"], u["foto"], u["stats"],
                        u["ritmo"], u["schritte"], u["worauf"], u["sicher"],
                        rot_merk=self.R["merk"], rot_stop=self.R["stop"],
                        rot_svg=self.R["svg"])

    def _tabela_vazia(self, colunas, linhas, primeira=None):
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

    # -- as sete pecas ---------------------------------------------------
    def p1(self):
        S, R = self.C1.S1, self.R
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
                         + '<div style="margin:16px 0">%s</div>' % M.svg_barra(4, 6, rot=R["svg"])
                         + '<div style="margin:8px 0 4px">%s</div>' % M.svg_onda(4, 6, 0, 3, rot=R["svg"])
                         + M.merk(R["s1_satz"], S["ausatmen_merk"])))
        c.append(M.secao(S["ehrlich_titel"], S["ehrlich_sub"], _pares(S["ehrlich"])))
        c.append(M.secao(S["sicher_titel"], S["sicher_sub"],
                         M.lista(S["sicher_regeln"])
                         + M.stop(R["s1_arzt"], S["sicher_arzt"])
                         + M.stop(R["s1_krise"], S["sicher_krise"])))
        c.append(M.secao(S["los_titel"], S["los_sub"],
                         M.passos(S["los"]) + M.merk(R["s1_druck"], S["los_drucken"])))
        return M.montar(self.TIT[0], "".join(c))

    def p2(self):
        S, R = self.C1.S2, self.R
        c = [M.capa(S["badge"], S["titel"], S["lead"], S["foto"])]
        drei = "".join(
            '<div class="tagcard"><div class="tnum"><s>%s</s><b>%d</b></div>'
            '<div><h4>%s</h4><p>%s</p></div></div>' % (R["anker"], i + 1, t, d)
            for i, (t, d) in enumerate(S["drei"]))
        c.append(M.secao(S["drei_titel"], S["drei_sub"], drei))
        for u in S["uebungen"]:
            c.append(self._card(u))
        c.append(M.secao(S["fehler_titel"], S["fehler_sub"], _pares(S["fehler"])))
        c.append(M.secao(R["faq"], "", M.faq(S["faq"])))
        return M.montar(self.TIT[1], "".join(c))

    def p3(self):
        S, R = self.C2.S3, self.R
        c = [M.capa(S["badge"], S["titel"], S["lead"], S["foto"])]
        c.append(M.secao(S["was_titel"], S["was_sub"],
                         _ps(S["was"]) + M.merk(R["s3_real"], S["was_merk"])))
        for u in S["uebungen"]:
            c.append(self._card(u))
        c.append(M.secao(S["wenn_titel"], S["wenn_sub"], M.lista(S["wenn"])))
        linhas = "".join(
            '<tr><th style="width:44%%">%s</th><td class="leer">'
            '<span style="color:#9b978f;font-size:13.5px">%s</span></td></tr>'
            % (a, b) for a, b in S["plan_zeilen"])
        c.append(M.secao(S["plan_titel"], S["plan_sub"],
                         '<table class="log">%s</table>' % linhas
                         + M.stop(R["s3_notruf"], S["plan_hinweis"])))
        return M.montar(self.TIT[2], "".join(c))

    def p4(self):
        S, R = self.C2.S4, self.R
        c = [M.capa(S["badge"], S["titel"], S["lead"], S["foto"])]
        c.append(M.secao(S["wie_titel"], S["wie_sub"],
                         M.lista(S["wie"]) + M.merk(R["s4_warum"], S["wie_merk"])))
        for w in S["wochen"]:
            corpo = [M.wochekopf(w["rot"], w["titel"]), "<p>%s</p>" % w["text"]]
            for n, t, d in w["tage"]:
                corpo.append(M.tagcard(n, t, d, rotulo=R["tag"]))
            c.append(M.secao("", "", "".join(corpo)))
        c.append(M.secao(S["danach_titel"], S["danach_sub"], _ps(S["danach"])))
        cab = "<tr>" + "".join("<th>%s</th><th>%s</th>" % (R["tag"].title(), S["tabela_col"])
                               for _ in range(3)) + "</tr>"
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
        return M.montar(self.TIT[3], "".join(c))

    def p5(self):
        S, R = self.C2.S5, self.R
        c = [M.capa(S["badge"], S["titel"], S["lead"], S["foto"])]
        c.append(M.secao(S["warum_titel"], S["warum_sub"], _ps(S["warum"])))
        for u in S["uebungen"]:
            c.append(self._card(u))
        c.append(M.secao(S["stunde_titel"], S["stunde_sub"], _pares(S["stunde"])))
        c.append(M.secao(R["faq"], "", M.faq(S["faq"])))
        return M.montar(self.TIT[4], "".join(c))

    def p6(self):
        S, R = self.C2.S6, self.R
        c = [M.capa(S["badge"], S["titel"], S["lead"], S["foto"], dourado=True)]
        c.append(M.secao(S["warum_titel"], S["warum_sub"], _ps(S["warum"])))
        c.append(M.secao(S["regeln_titel"], S["regeln_sub"],
                         M.lista(S["regeln"]) + M.stop(R["s6_wer"], S["regeln_wer"])))
        for u in S["uebungen"]:
            c.append(self._card(u))
        tage = "".join(M.tagcard(n, t, d, rotulo=R["tag"]) for n, t, d in S["woche_tage"])
        c.append(M.secao(S["woche_titel"], S["woche_sub"], tage))
        return M.montar(self.TIT[5], "".join(c))

    def p7(self):
        S, R = self.C2.S7, self.R
        c = [M.capa(S["badge"], S["titel"], S["lead"], S["foto"], dourado=True)]
        c.append(M.secao(S["warum_titel"], S["warum_sub"], _ps(S["warum"])))
        c.append(M.secao(S["wie_titel"], S["wie_sub"],
                         M.lista(S["wie"]) + M.merk(R["s7_skala"], S["wie_merk"])))
        for w in (1, 2, 3):
            c.append(M.secao("%s — %s %d" % (S["wochen_titel"], R["woche"], w),
                             S["wochen_sub"] if w == 1 else "",
                             self._tabela_vazia(S["wochen_spalten"], 7, R["dias"])))
        c.append(M.secao(S["ausloeser_titel"], S["ausloeser_sub"],
                         self._tabela_vazia(S["ausloeser_spalten"], 9)))
        fragen = "".join(
            '<div class="faq"><h4>%d. %s</h4><p>%s</p></div>'
            '<table class="log"><tr><td class="leer"></td></tr>'
            '<tr><td class="leer"></td></tr></table>' % (i + 1, q, d)
            for i, (q, d) in enumerate(S["abend_fragen"]))
        c.append(M.secao(S["abend_titel"], S["abend_sub"], fragen))
        c.append(M.secao(S["ende_titel"], S["ende_sub"],
                         _ps(S["ende"]) + M.merk(R["s7_ende"], S["ende_schluss"])))
        return M.montar(self.TIT[6], "".join(c))

    def build(self, quais=None):
        ok = True
        pecas = [self.p1, self.p2, self.p3, self.p4, self.p5, self.p6, self.p7]
        for i, fn in enumerate(pecas, start=1):
            if quais and i not in quais:
                continue
            ok = M.gerar_pdf(fn(), self.ARQ[i - 1],
                             tmp="_tmp_%s%d.html" % (self.lang, i)) and ok
        return ok


if __name__ == "__main__":
    args = sys.argv[1:]
    lang = args[0].lower() if args and args[0].lower() in IDIOMAS else "de"
    quais = set(int(a) for a in args if a.isdigit())
    sys.exit(0 if Livro(lang).build(quais or None) else 1)
