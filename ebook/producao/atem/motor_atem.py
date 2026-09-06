# -*- coding: utf-8 -*-
"""MOTOR ATEMANKER — template travado do entregavel de respiracao (alemao).

⛔ NAO e' uma copia do `motor_receitas`. E' outro PRODUTO, e o template de
receita (foto + ingredientes + tabela de porcao por perfil) nao descreve um
exercicio de respiracao. O que se REUSA do motor de receitas e' o que de fato
e' comum e por isso mora la': os TOKENS do design system (`base.ESTILO`) e o
caminho do Chrome (`base.CHROME`). Token duplicado e' token que diverge.

⭐⭐ O MECANISMO E' EXPIRACAO MAIS LONGA QUE A INSPIRACAO, e a escolha e'
deliberada contra a fonte de referencia. A fonte (metodo de respiracao em gelo)
e' hiperventilacao + retencao longa. Num publico ANSIOSO isso e' a ferramenta
errada: hiperventilar derruba o CO2 e produz formigamento, tontura e aperto no
peito — exatamente a lista de sintomas do ataque de panico que a compradora
esta' tentando evitar. Respiracao lenta com expiracao alongada faz o contrario.
⛔ Por isso NENHUM exercicio deste produto pede hiperventilar nem segurar o ar
com o pulmao vazio. As pausas sao curtas e sempre com o pulmao confortavel.

⛔ AGUA NUNCA. Ver `GE4` no `gelo16_short.py`: respiracao seguida de imersao e'
o mecanismo do desmaio de aguas rasas. Todo card carrega a trava, e o bonus do
frio e' explicitamente FORA da banheira.

⛔ SEM ALEGACAO DE CURA (HWG). A moldura e' `sistema nervoso em alarme` ->
`regulacao em minutos`, nunca diagnostico e nunca cura. Ver a licao ja' paga no
cabecalho do `atem16_short.py`.
"""

import os
import sys

_PAI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _PAI not in sys.path:
    sys.path.insert(0, _PAI)

import motor_receitas as base  # noqa: E402  (tokens e CHROME vem daqui)

AQUI = os.path.dirname(os.path.abspath(__file__))
CHROME = base.CHROME
PORTA = 8133

# ⛔ Corpo >= 16px, regra do PLAYBOOK-EBOOK: publico com idosos, nunca espremer.
ESTILO = base.ESTILO + """
.cover{page-break-after:always;padding-top:26px}
.cover .badge{display:inline-block;background:var(--green);color:#fff;font-size:15px;
font-weight:900;letter-spacing:.14em;text-transform:uppercase;padding:9px 20px;border-radius:999px}
.cover .badge.b{background:var(--gold);color:#3d2c05}
.cover h1{font-size:58px;font-weight:900;letter-spacing:-.03em;margin:20px 0 16px;
line-height:1.02;color:var(--green)}
.cover .rule{width:74px;height:5px;background:var(--gold);border-radius:3px;margin:0 0 22px}
.cover .lead{font-size:18.5px;color:var(--soft);line-height:1.7;max-width:97%}
.cover .capfoto{margin-top:26px;width:100%;height:330px;object-fit:cover;border-radius:18px}

.sec{page-break-before:always;padding-top:4px}
.sec.cont{page-break-before:auto}
.sec h2{font-size:31px;font-weight:900;letter-spacing:-.01em;color:var(--green);
margin-bottom:8px;line-height:1.12}
.sec h3{font-size:19px;font-weight:800;color:var(--ink);margin:22px 0 9px}
.sec .sub{font-size:17px;color:var(--soft);line-height:1.6;margin-bottom:18px;max-width:97%}
.sec p{font-size:17.5px;line-height:1.72;margin-bottom:13px}
.sec p b{color:var(--ink)}
.sec ul.plain{list-style:none;margin:0 0 14px}
.sec ul.plain li{position:relative;padding-left:22px;font-size:17.5px;line-height:1.62;
margin-bottom:9px}
.sec ul.plain li::before{content:"";position:absolute;left:0;top:10px;width:8px;height:8px;
border-radius:50%;background:var(--gold)}

.foto-larga{width:100%;height:300px;object-fit:cover;border-radius:16px;margin:6px 0 18px}
.foto-quad{width:100%;aspect-ratio:1/1;object-fit:cover;border-radius:15px}

.uebung{page-break-before:always;padding-top:4px}
.uebung .tag{background:var(--green-tint);color:var(--green);font-size:12px;font-weight:800;
letter-spacing:.09em;text-transform:uppercase;padding:6px 13px;border-radius:999px;display:inline-block}
.uebung h2{font-size:28px;font-weight:900;color:var(--green);letter-spacing:-.015em;
margin:9px 0 6px;line-height:1.08}
.uebung .hook{font-size:16.5px;color:var(--soft);line-height:1.5;margin-bottom:11px}
.grid2{display:grid;grid-template-columns:262px 1fr;gap:18px;align-items:start;margin-bottom:6px}
.stats{display:flex;gap:8px;margin-bottom:10px}
.stat{flex:1;background:var(--cream);border-radius:10px;padding:8px 6px;text-align:center}
.stat .v{font-size:17px;font-weight:900;color:var(--green);line-height:1.2}
.stat .l{font-size:11.5px;color:var(--soft);text-transform:uppercase;letter-spacing:.05em;margin-top:3px}

.steps{list-style:none;margin:4px 0 0}
.steps li{position:relative;padding-left:42px;margin-bottom:7px;font-size:16.5px;line-height:1.46;
break-inside:avoid}
.steps li .n{position:absolute;left:0;top:0;width:30px;height:30px;background:var(--green);
color:#fff;border-radius:50%;display:flex;align-items:center;justify-content:center;
font-size:14px;font-weight:800}

.merk{margin-top:10px;background:var(--gold-tint);border-left:4px solid var(--gold);
border-radius:0 12px 12px 0;padding:11px 15px;break-inside:avoid}
.merk b{display:block;color:#8a6a1a;font-size:13px;text-transform:uppercase;
letter-spacing:.06em;margin-bottom:5px}
.merk p{font-size:16px;line-height:1.45;margin:0}

.stop{margin-top:9px;background:#FCEDEC;border-left:4px solid #C0392B;border-radius:0 12px 12px 0;
padding:11px 15px;break-inside:avoid}
.stop b{display:block;color:#96271b;font-size:13px;text-transform:uppercase;
letter-spacing:.06em;margin-bottom:5px}
.stop p{font-size:16px;line-height:1.45;margin:0}

.ruhe{margin-top:18px;background:var(--green-tint);border-radius:14px;padding:18px 22px;
font-size:17px;color:var(--green);line-height:1.62;break-inside:avoid}

.tagcard{border:1px solid var(--line);border-radius:14px;padding:12px 15px;margin-bottom:9px;
break-inside:avoid;display:grid;grid-template-columns:52px 1fr;gap:13px;align-items:start}
.tagcard .tnum{width:46px;height:46px;border-radius:12px;background:var(--green);color:#fff;
display:flex;flex-direction:column;align-items:center;justify-content:center;line-height:1}
.tagcard .tnum s{text-decoration:none;font-size:9.5px;letter-spacing:.09em;opacity:.85}
.tagcard .tnum b{font-size:21px;font-weight:900}
.tagcard h4{font-size:17px;font-weight:800;color:var(--ink);margin-bottom:3px}
.tagcard p{font-size:15.5px;line-height:1.5;color:var(--soft);margin:0}
.wochekopf{background:var(--green);color:#fff;border-radius:13px;padding:11px 17px;
margin:0 0 11px;break-inside:avoid}
.wochekopf b{font-size:12px;letter-spacing:.12em;text-transform:uppercase;opacity:.9;display:block}
.wochekopf h3{font-size:21px;font-weight:900;margin:3px 0 0;color:#fff}

table.log{width:100%;border-collapse:collapse;margin-top:12px;break-inside:avoid}
table.log th,table.log td{border:1px solid var(--line);padding:11px 10px;font-size:15px;
text-align:left;vertical-align:top}
table.log th{background:var(--cream);font-size:11.5px;text-transform:uppercase;
letter-spacing:.06em;color:var(--soft)}
table.log td.leer{height:44px}

.faq{border-top:1px solid var(--line);padding:15px 0;break-inside:avoid}
.faq h4{font-size:18px;font-weight:800;color:var(--green);margin-bottom:6px}
.faq p{font-size:17px;line-height:1.62;margin:0;color:var(--soft)}
"""


def esc(t):
    return (t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


# ===========================================================================
# ⭐ OS DIAGRAMAS — a entropia visual que NAO depende do gerador de imagem.
# Ritmo respiratorio nao se fotografa; se desenha. Estes SVGs sao a peca de
# ensino mais importante do produto: mostram, sem uma palavra, que a expiracao
# e' mais longa que a inspiracao.
# ===========================================================================

SVG_DE = {"ein": "EIN", "aus": "AUS", "ein_longo": "EINATMEN",
          "aus_longo": "AUSATMEN", "cheio": "VOLL", "vazio": "LEER",
          "legenda": "Das Ausatmen ist l&#228;nger. Genau das ist der ganze Trick."}


def svg_onda(ein, aus, pausa=0, ciclos=3, w=980, h=190, rot=None):
    """Curva do folego: subida curta (inspira), descida longa (expira).

    A LARGURA de cada trecho e' proporcional aos SEGUNDOS reais, e e' isso que
    faz o desenho ensinar: o olho ve' a descida ocupar mais espaco que a subida
    antes de ler qualquer numero.
    """
    rot = rot or SVG_DE
    total = (ein + aus + pausa) * ciclos
    esq, dir_, topo, base_y = 54, 18, 26, h - 46
    largura = w - esq - dir_
    px = largura / float(total)

    d = []
    x = esq
    d.append("M %.1f %.1f" % (x, base_y))
    marcas = []
    for _ in range(ciclos):
        x1 = x + ein * px
        d.append("C %.1f %.1f %.1f %.1f %.1f %.1f" % (
            x + ein * px * .45, base_y, x + ein * px * .55, topo, x1, topo))
        marcas.append(("EIN", x, x1, True))
        x = x1
        if pausa:
            x1 = x + pausa * px
            d.append("L %.1f %.1f" % (x1, topo))
            x = x1
        x1 = x + aus * px
        d.append("C %.1f %.1f %.1f %.1f %.1f %.1f" % (
            x + aus * px * .45, topo, x + aus * px * .55, base_y, x1, base_y))
        marcas.append(("AUS", x, x1, False))
        x = x1

    s = ['<svg viewBox="0 0 %d %d" width="100%%" xmlns="http://www.w3.org/2000/svg" '
         'style="display:block">' % (w, h)]
    s.append('<rect x="0" y="0" width="%d" height="%d" rx="16" fill="#F7F5F0"/>' % (w, h))
    s.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="#E2DED6" stroke-width="2"/>'
             % (esq, base_y, w - dir_, base_y))
    # faixas: verde para inspirar, dourado para expirar
    for _lbl, xa, xb, e in marcas:
        s.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" opacity=".5"/>'
                 % (xa, topo, xb - xa, base_y - topo,
                    "#E8F7EB" if e else "#FBF3E2"))
    s.append('<path d="%s" fill="none" stroke="#196B45" stroke-width="4" '
             'stroke-linecap="round" stroke-linejoin="round"/>' % " ".join(d))
    # rotulos do primeiro ciclo
    for _lbl, xa, xb, e in marcas[:2]:
        s.append('<text x="%.1f" y="%.1f" text-anchor="middle" font-family="DM Sans,sans-serif" '
                 'font-size="15" font-weight="800" fill="%s">%s %d s</text>'
                 % ((xa + xb) / 2.0, base_y + 26, "#196B45" if e else "#8a6a1a",
                    (rot["ein"] if e else rot["aus"]), ein if e else aus))
    s.append('<text x="10" y="%.1f" font-family="DM Sans,sans-serif" font-size="12" '
             'font-weight="800" fill="#54524E">%s</text>' % (topo + 5, rot["cheio"]))
    s.append('<text x="10" y="%.1f" font-family="DM Sans,sans-serif" font-size="12" '
             'font-weight="800" fill="#54524E">%s</text>' % (base_y, rot["vazio"]))
    s.append("</svg>")
    return "".join(s)


def svg_barra(ein, aus, w=980, h=112, rot=None):
    """A barra do contraste: inspira x expira, lado a lado, na mesma escala."""
    rot = rot or SVG_DE
    esq, dir_ = 18, 18
    largura = w - esq - dir_
    tot = float(ein + aus)
    we = largura * (ein / tot)
    s = ['<svg viewBox="0 0 %d %d" width="100%%" xmlns="http://www.w3.org/2000/svg" '
         'style="display:block">' % (w, h)]
    s.append('<rect x="%d" y="26" width="%.1f" height="46" rx="12" fill="#196B45"/>'
             % (esq, we))
    s.append('<rect x="%.1f" y="26" width="%.1f" height="46" rx="12" fill="#D9A441"/>'
             % (esq + we + 6, largura - we - 6))
    s.append('<text x="%.1f" y="55" text-anchor="middle" font-family="DM Sans,sans-serif" '
             'font-size="17" font-weight="900" fill="#fff">%s %d</text>'
             % (esq + we / 2, rot["ein_longo"], ein))
    s.append('<text x="%.1f" y="55" text-anchor="middle" font-family="DM Sans,sans-serif" '
             'font-size="17" font-weight="900" fill="#3d2c05">%s %d</text>'
             % (esq + we + 6 + (largura - we - 6) / 2, rot["aus_longo"], aus))
    s.append('<text x="%d" y="96" font-family="DM Sans,sans-serif" font-size="14.5" '
             'fill="#54524E">%s</text>' % (esq, rot["legenda"]))
    s.append("</svg>")
    return "".join(s)


# ⛔ `svg_uhr` REMOVIDO. Era um relogio decorativo que nenhum builder chamava e
# que carregava `MINUTEN` e `Atemzuege` cravados — codigo morto com defeito de
# idioma dentro e' armadilha para quem vier depois: um dia alguem o usa e o
# alemao reaparece num PDF frances sem que ninguem entenda de onde veio.


# ===========================================================================
# BLOCOS DE PAGINA
# ===========================================================================

def capa(badge, titulo, lead, foto=None, dourado=False):
    p = ['<section class="cover">']
    p.append('<span class="badge%s">%s</span>' % (" b" if dourado else "", esc(badge)))
    p.append("<h1>%s</h1>" % titulo)
    p.append('<div class="rule"></div>')
    p.append('<p class="lead">%s</p>' % lead)
    if foto:
        p.append('<img class="capfoto" src="fotos/%s.jpg">' % foto)
    p.append("</section>")
    return "".join(p)


def secao(titulo, sub="", corpo="", nova_pagina=True):
    p = ['<section class="sec%s">' % ("" if nova_pagina else " cont")]
    if titulo:
        p.append("<h2>%s</h2>" % titulo)
    if sub:
        p.append('<p class="sub">%s</p>' % sub)
    p.append(corpo)
    p.append("</section>")
    return "".join(p)


def lista(itens):
    return ('<ul class="plain">%s</ul>'
            % "".join("<li>%s</li>" % i for i in itens))


def passos(itens):
    return ('<ul class="steps">%s</ul>'
            % "".join('<li><span class="n">%d</span>%s</li>' % (i + 1, t)
                      for i, t in enumerate(itens)))


def merk(titulo, texto):
    return '<div class="merk"><b>%s</b><p>%s</p></div>' % (titulo, texto)


def stop(titulo, texto):
    return '<div class="stop"><b>%s</b><p>%s</p></div>' % (titulo, texto)


def ruhe(texto):
    return '<div class="ruhe">%s</div>' % texto


def uebung(tag, nome, hook, foto, stats, ritmo, schritte, worauf, sicher,
           rot_merk="Woran du merkst, dass es wirkt", rot_stop="Sicherheit",
           rot_svg=None):
    """Card de UM exercicio. `ritmo` = (ein, aus, pausa, ciclos) ou None.

    ⛔ Os dois rotulos das caixas CHEGAM DE FORA. Eram alemao cravado aqui
    dentro, e a doutrina do repo e' uma ferramenta por funcao, nunca uma
    copia por idioma — o frances usa este mesmo motor."""
    p = ['<section class="uebung">']
    p.append('<span class="tag">%s</span>' % esc(tag))
    p.append("<h2>%s</h2>" % nome)
    p.append('<p class="hook">%s</p>' % hook)
    p.append('<div class="grid2">')
    p.append('<div><img class="foto-quad" src="fotos/%s.jpg"></div>' % foto)
    p.append("<div>")
    p.append('<div class="stats">%s</div>'
             % "".join('<div class="stat"><div class="v">%s</div>'
                       '<div class="l">%s</div></div>' % (v, l) for v, l in stats))
    # ⛔ UM diagrama por card, e ele mora na COLUNA, nao na largura toda.
    # A versao com barra + onda de largura total estourava a pagina e jogava
    # `merk`/`stop` sozinhos na seguinte: 15 paginas orfas medidas em 73.
    if ritmo:
        ein, aus, pausa, ciclos = ritmo
        p.append('<div style="margin-top:10px">%s</div>'
                 % svg_onda(ein, aus, pausa, 2, h=168, rot=rot_svg))
    # ⭐ A caixa dourada mora NA COLUNA, ao lado da foto. Ela e' o que sobrava:
    # a foto tem 262px de altura e a coluna da direita so' ~140, e essa faixa
    # vazia era exatamente do tamanho da caixa que ia sozinha para a pagina
    # seguinte. Espaco morto virou conteudo, e a orfa some sem apertar fonte.
    if worauf:
        p.append(merk(rot_merk, worauf))
    if sicher:
        p.append(stop(rot_stop, sicher))
    p.append("</div></div>")
    p.append(passos(schritte))
    p.append("</section>")
    return "".join(p)


def tagcard(n, titel, texto, rotulo="TAG"):
    return ('<div class="tagcard"><div class="tnum"><s>%s</s><b>%d</b></div>'
            '<div><h4>%s</h4><p>%s</p></div></div>' % (rotulo, n, titel, texto))


def wochekopf(rot, titulo):
    return '<div class="wochekopf"><b>%s</b><h3>%s</h3></div>' % (rot, titulo)


def faq(pares):
    return "".join('<div class="faq"><h4>%s</h4><p>%s</p></div>' % (q, a)
                   for q, a in pares)


def montar(titulo_doc, corpo):
    return ("""<!doctype html><html lang="de"><head><meta charset="utf-8">
<title>%s</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700;800;900&display=swap" rel="stylesheet">
<style>%s</style></head><body>%s</body></html>"""
            % (esc(titulo_doc), ESTILO, corpo))


def gerar_pdf(html, nome_pdf, tmp="_tmp_atem.html"):
    """HTML -> http.server local -> Chrome headless -> PDF. Mesmo caminho do
    motor de receitas; o HTML temporario tem nome ascii sem espaco de proposito."""
    import http.server
    import socketserver
    import subprocess
    import threading
    import time

    html_path = os.path.join(AQUI, tmp)
    pdf_path = os.path.join(AQUI, nome_pdf)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)

    if not getattr(gerar_pdf, "_srv", None):
        def _srv():
            os.chdir(AQUI)
            with socketserver.TCPServer(("127.0.0.1", PORTA),
                                        http.server.SimpleHTTPRequestHandler) as s:
                s.serve_forever()
        t = threading.Thread(target=_srv, daemon=True)
        t.start()
        gerar_pdf._srv = t
        time.sleep(1.2)

    subprocess.run([CHROME, "--headless=new", "--disable-gpu",
                    "--no-pdf-header-footer", "--virtual-time-budget=30000",
                    "--print-to-pdf=" + pdf_path,
                    "http://127.0.0.1:%d/%s" % (PORTA, tmp)],
                   capture_output=True)
    ok = os.path.exists(pdf_path)
    print("PDF: %-58s %s %s" % (nome_pdf, "OK" if ok else "FALHOU",
                                "(%.1f MB)" % (os.path.getsize(pdf_path) / 1e6) if ok else ""))
    if ok and os.path.exists(html_path):
        os.remove(html_path)
    return ok
