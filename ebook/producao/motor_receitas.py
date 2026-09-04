# -*- coding: utf-8 -*-
"""MOTOR do ebook — dados estruturados de receita -> HTML no template travado.

Template = a receita-modelo aprovada (fonte legivel, opcao B em 2 paginas,
margem na @page). Cada receita e' um dict; este arquivo so' RENDERIZA. Os dados
das receitas moram nos arquivos por categoria (ex.: receitas_cafe.py).

⛔ Metas de caloria por perfil sao FIXAS por tipo de refeicao (definido no
briefing). A coluna 'porcoes' de cada receita tem 8 strings, na ordem:
  Mulher 55-70 · 71-85 · 86-100 · 100+ · Homem 70-85 · 86-100 · 101-120 · 120+
"""
import html
import io
import os
import subprocess

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# metas (kcal) por tipo de refeicao -> [W1,W2,W3,W4, M1,M2,M3,M4]
METAS = {
    "cafe":      [300, 370, 420, 470, 450, 510, 560, 620],
    "almoco":    [360, 440, 500, 560, 540, 610, 680, 750],
    "jantar":    [340, 420, 480, 540, 520, 590, 650, 720],
    "sobremesa": [120, 150, 170, 190, 180, 200, 230, 260],
    "suco":      [90, 110, 130, 150, 130, 150, 170, 190],
}
FAIXAS_M = ["55–70 kg", "71–85 kg", "86–100 kg", "100 kg +"]
FAIXAS_H = ["70–85 kg", "86–100 kg", "101–120 kg", "120 kg +"]
ROTULO_CAT = {"cafe": "Café da manhã", "almoco": "Almoço", "jantar": "Jantar",
              "sobremesa": "Sobremesa", "suco": "Suco detox"}

# ── i18n ──────────────────────────────────────────────────────────────────
# Toda string fixa do template mora aqui. 'pt' e' o produto ja' validado e
# NAO se mexe; idioma novo entra como chave nova. As faixas de peso (kg) e as
# metas (kcal) sao METRICAS e valem igual em todos os idiomas.
# ⛔ DE trata o leitor por "du" (decisao do operador, 2026-09-04): o alemao e'
# o unico idioma do produto onde essa escolha muda TODA frase.
I18N = {
    "pt": {
        "html_lang": "pt-BR",
        # ⛔ VAZIO de proposito: qualquer regra aqui muda o PT, e o PT e' o
        # produto ja' entregue. A prova de que ele nao mudou e' `snapshot_pt.py`
        # (hash do HTML das 5 categorias, identico antes e depois do i18n).
        "css": "",
        "cat": ROTULO_CAT,
        "receita": "Receita ",
        "foto_ph": ("<b>FOTO %s</b><small>espaço quadrado reservado<br>"
                    "(gerar pelo prompt e nomear \"%s\")</small>"),
        "st_tempo": "Preparo", "st_rende": "Rende", "st_kcal": "Kcal base",
        "h_ings": "Ingredientes (porção base)",
        "h_passos": "Modo de preparo",
        "h_dica": "Por que ajuda a emagrecer",
        "adj_head": "Ajuste a sua porção",
        "adj_sub": "escolha a sua linha e siga essas quantidades",
        "th_perfil": "Perfil", "th_meta": "Meta desta refeição", "th_porcao": "Sua porção",
        "mulheres": "Mulheres", "homens": "Homens",
        "adj_note": ("Encontre a sua linha por <b>sexo e peso</b> e siga essas quantidades. "
                     "<b>Vegetais, verduras, café e chá sem açúcar são livres, à vontade — "
                     "não precisa contar.</b>"),
        "livre": ("<b>Bebida livre.</b> Sem açúcar, é pertinho de zero caloria — pode tomar "
                  "à vontade ao longo do dia, sem precisar medir a porção. É ótima para "
                  "substituir refrigerante e suco de caixinha, ajudando na hidratação e no "
                  "emagrecimento."),
        # ⚠️ As quebras de linha e a indentacao SAO PARTE DA STRING: o template
        # original trazia este paragrafo quebrado dentro do HTML. Mantidas
        # verbatim para o PT sair byte a byte igual ao produto ja' entregue.
        "foot": ("Valores aproximados, calculados por tabela nutricional padrão — servem como guia,\n"
                 "    não como prescrição médica. As metas por perfil consideram atividade leve; quem se exercita mais\n"
                 "    gasta mais e pode ajustar para cima."),
    },
    "de": {
        "html_lang": "de",
        # ⛔⛔ O alemao e' mais longo que o portugues e empurra o rodape para a
        # pagina seguinte: nos SUCOS isso produziu 4 paginas com DUAS PALAVRAS
        # ("oben anpassen."), medidas contra 0 no PT. A ordem do operador e'
        # "nao espremer nada para caber" — entao o conserto NAO encolhe fonte:
        # ele mantem o rodape colado ao bloco anterior e inteiro.
        "css": ("\n.foot{break-inside:avoid;page-break-inside:avoid;"
                "break-before:avoid;page-break-before:avoid}"
                "\n.tip{break-after:avoid;page-break-after:avoid}"),
        "cat": {"cafe": "Frühstück", "almoco": "Mittagessen", "jantar": "Abendessen",
                "sobremesa": "Dessert", "suco": "Detox-Saft"},
        "receita": "Rezept ",
        "foto_ph": ("<b>FOTO %s</b><small>quadratischer Platz reserviert<br>"
                    "(mit dem Prompt erzeugen und \"%s\" nennen)</small>"),
        "st_tempo": "Zeit", "st_rende": "Ergibt", "st_kcal": "Kcal Basis",
        "h_ings": "Zutaten (Grundportion)",
        "h_passos": "So geht's",
        "h_dica": "Warum das beim Abnehmen hilft",
        "adj_head": "Passe deine Portion an",
        "adj_sub": "suche deine Zeile und halte dich an diese Mengen",
        "th_perfil": "Profil", "th_meta": "Ziel dieser Mahlzeit", "th_porcao": "Deine Portion",
        "mulheres": "Frauen", "homens": "Männer",
        "adj_note": ("Suche deine Zeile nach <b>Geschlecht und Gewicht</b> und halte dich an diese "
                     "Mengen. <b>Gemüse, Blattsalat, Kaffee und Tee ohne Zucker sind frei, so viel "
                     "du magst — das musst du nicht mitzählen.</b>"),
        "livre": ("<b>Freies Getränk.</b> Ohne Zucker hat es fast keine Kalorien — du kannst es "
                  "über den ganzen Tag trinken, so viel du magst, ohne die Menge abzumessen. Es "
                  "ist super, um Limonade und Saft aus der Packung zu ersetzen, und hilft beim "
                  "Trinken und beim Abnehmen."),
        "foot": ("Ungefähre Werte, berechnet nach einer Standard-Nährwerttabelle — sie sind ein "
                 "Anhaltspunkt, keine ärztliche Vorgabe. Die Ziele pro Profil gehen von leichter "
                 "Bewegung aus; wer sich mehr bewegt, verbraucht mehr und darf nach oben anpassen."),
    },
    "fr": {
        "html_lang": "fr",
        # ⛔ Mesma razao do alemao: o frances tambem e' mais longo que o
        # portugues e empurra o rodape para a pagina seguinte. A ordem e' "nao
        # espremer" — entao o rodape fica inteiro e colado ao bloco anterior,
        # e a regra vive AQUI, nunca no ESTILO compartilhado com o PT.
        "css": ("\n.foot{break-inside:avoid;page-break-inside:avoid;"
                "break-before:avoid;page-break-before:avoid}"
                "\n.tip{break-after:avoid;page-break-after:avoid}"),
        "cat": {"cafe": "Petit-déjeuner", "almoco": "Déjeuner", "jantar": "Dîner",
                "sobremesa": "Dessert", "suco": "Jus détox"},
        "receita": "Recette ",
        "foto_ph": ("<b>PHOTO %s</b><small>emplacement carré réservé<br>"
                    "(à générer avec le prompt et à nommer \"%s\")</small>"),
        "st_tempo": "Temps", "st_rende": "Donne", "st_kcal": "Kcal de base",
        "h_ings": "Ingrédients (portion de base)",
        "h_passos": "Préparation",
        "h_dica": "Pourquoi ça aide à maigrir",
        "adj_head": "Ajuste ta portion",
        "adj_sub": "trouve ta ligne et suis ces quantités",
        "th_perfil": "Profil", "th_meta": "Objectif de ce repas", "th_porcao": "Ta portion",
        "mulheres": "Femmes", "homens": "Hommes",
        "adj_note": ("Trouve ta ligne selon le <b>sexe et le poids</b> et suis ces quantités. "
                     "<b>Les légumes, la salade, le café et le thé sans sucre sont libres, "
                     "à volonté — tu n'as pas besoin de les compter.</b>"),
        "livre": ("<b>Boisson libre.</b> Sans sucre, elle n'a presque aucune calorie — tu peux "
                  "en boire tout au long de la journée, autant que tu veux, sans mesurer la "
                  "quantité. Elle est parfaite pour remplacer les sodas et les jus en brique, "
                  "et elle aide à bien t'hydrater et à maigrir."),
        "foot": ("Valeurs approximatives, calculées d'après une table nutritionnelle standard — "
                 "elles servent de repère, pas de prescription médicale. Les objectifs par profil "
                 "supposent une activité légère ; qui bouge plus dépense plus et peut ajuster "
                 "vers le haut."),
    },
}

ESTILO = """
:root{--green:#196B45;--green-tint:#E8F7EB;--gold:#D9A441;--gold-tint:#FBF3E2;
--ink:#1A1A1A;--soft:#54524E;--line:#E2DED6;--cream:#F7F5F0;}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:"DM Sans",system-ui,sans-serif;color:var(--ink);-webkit-font-smoothing:antialiased}
.recipe{padding:0 0 6px;page-break-before:always}
.recipe:first-child{page-break-before:avoid}
.top{display:flex;align-items:center;justify-content:space-between;margin-bottom:14px}
.tag{background:var(--green-tint);color:var(--green);font-size:12px;font-weight:800;
letter-spacing:.12em;text-transform:uppercase;padding:6px 13px;border-radius:999px}
.num{font-size:12.5px;font-weight:700;color:var(--soft);letter-spacing:.05em}
h1{font-size:32px;font-weight:900;letter-spacing:-.02em;line-height:1.08}
.hook{font-size:16.5px;color:var(--soft);margin-top:9px;line-height:1.5;max-width:94%}
.grid{display:grid;grid-template-columns:290px 1fr;gap:26px;margin-top:22px}
.photo{width:290px;height:290px;border-radius:14px;background:var(--cream);
border:2px dashed #cfc8ba;display:flex;flex-direction:column;align-items:center;
justify-content:center;text-align:center;color:#9a927f;padding:16px}
.photo b{font-size:15px;color:var(--green);font-weight:800}
.photo small{font-size:11.5px;margin-top:6px;line-height:1.5}
.photo img{width:100%;height:100%;object-fit:cover;border-radius:12px}
.stats{display:flex;gap:10px;margin-bottom:16px}
.stat{flex:1;background:var(--cream);border-radius:10px;padding:10px 8px;text-align:center}
.stat .v{font-size:17px;font-weight:900;color:var(--green)}
.stat .l{font-size:10.5px;color:var(--soft);text-transform:uppercase;letter-spacing:.06em;margin-top:2px}
h2{font-size:14px;font-weight:800;color:var(--green);text-transform:uppercase;letter-spacing:.08em;margin:0 0 8px}
.ings{list-style:none}
.ings li{font-size:15.5px;padding:5px 0 5px 19px;position:relative;line-height:1.5}
.ings li::before{content:"";position:absolute;left:0;top:9px;width:7px;height:7px;border-radius:50%;background:var(--gold)}
.steps{margin-top:26px}
.steps ol{list-style:none;counter-reset:s}
.steps li{counter-increment:s;position:relative;padding:0 0 14px 42px;font-size:15.5px;line-height:1.55}
.steps li::before{content:counter(s);position:absolute;left:0;top:-1px;width:26px;height:26px;
background:var(--green);color:#fff;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:800}
.adj{margin-top:24px;border:1px solid var(--line);border-radius:14px;overflow:hidden;break-inside:avoid;page-break-inside:avoid}
.adj-head{background:var(--green);color:#fff;padding:12px 16px;font-size:14px;font-weight:800;
display:flex;align-items:center;justify-content:space-between}
.adj-head span{font-size:11.5px;font-weight:600;opacity:.85}
table{width:100%;border-collapse:collapse}
th,td{text-align:left;padding:10px 16px;font-size:14px;border-top:1px solid var(--line)}
th{background:var(--cream);font-size:11.5px;text-transform:uppercase;letter-spacing:.06em;color:var(--soft)}
.sex td{background:var(--gold-tint);font-weight:800;font-size:13px;text-transform:uppercase;letter-spacing:.05em}
td .kcal{font-weight:800;color:var(--green)}
.adj-note{padding:12px 16px;font-size:13.5px;color:var(--soft);background:var(--cream);line-height:1.6}
.tip{margin-top:22px;background:var(--gold-tint);border-left:4px solid var(--gold);
border-radius:0 10px 10px 0;padding:14px 18px;break-inside:avoid}
.tip b{color:#8a6a1a;font-size:12.5px;text-transform:uppercase;letter-spacing:.06em;display:block;margin-bottom:5px}
.tip p{font-size:15px;line-height:1.55}
.foot{margin-top:18px;padding-top:12px;border-top:1px solid var(--line);font-size:12.5px;color:#8f887a;line-height:1.55}
.livre{margin-top:24px;background:var(--green-tint);border-radius:14px;padding:16px 20px;
font-size:15px;color:var(--green);line-height:1.6;break-inside:avoid}
.livre b{font-weight:800}
@page{size:A4;margin:16mm 15mm}
"""


def _linha(faixa, meta, porcao):
    return ('<tr><td>%s</td><td><span class="kcal">~%d kcal</span></td>'
            '<td>%s</td></tr>' % (html.escape(faixa),
                                  meta, html.escape(porcao)))


def render_receita(r, tipo, num, img_dir=None, lang="pt"):
    """r: dict com nome, hook, tempo, porcoes(base kcal), rende, ings[], passos[],
    porcoes8[8], dica. num: 1..N. tipo: cafe/almoco/..."""
    T = I18N[lang]
    metas = METAS[tipo]
    n3 = "%03d" % num
    # foto: se existir o arquivo, embute; senao placeholder com o numero
    foto_html = T["foto_ph"] % (n3, n3)
    if img_dir:
        for ext in (".jpg", ".jpeg", ".png", ".webp"):
            cam = os.path.join(img_dir, n3 + ext)
            if os.path.isfile(cam):
                foto_html = '<img src="fotos/%s" alt="">' % (n3 + ext)
                break

    ings = "".join("<li>%s</li>" % html.escape(x) for x in r["ings"])
    passos = "".join("<li>%s</li>" % html.escape(x) for x in r["passos"])

    # bloco de ajuste: bebida livre (chá/água ~0 kcal) OU tabela por perfil
    if r.get("livre"):
        ajuste = '<div class="livre">%s</div>' % T["livre"]
    else:
        p = r["porcoes8"]
        linhas = (
            '<tr class="sex"><td colspan="3">%s</td></tr>' % T["mulheres"]
            + "".join(_linha(FAIXAS_M[i], metas[i], p[i]) for i in range(4))
            + '<tr class="sex"><td colspan="3">%s</td></tr>' % T["homens"]
            + "".join(_linha(FAIXAS_H[i], metas[4 + i], p[4 + i]) for i in range(4)))
        ajuste = (
            '<div class="adj">'
            '<div class="adj-head">%s <span>%s</span></div>'
            '<table><tr><th style="width:150px">%s</th><th style="width:120px">%s</th><th>%s</th></tr>'
            % (T["adj_head"], T["adj_sub"], T["th_perfil"], T["th_meta"], T["th_porcao"])
            + linhas + '</table>'
            '<div class="adj-note">%s</div>' % T["adj_note"]
            + '</div>')

    rotulo = r.get("tag", T["cat"][tipo])
    num_label = r.get("num_label", T["receita"] + n3)

    return """<div class="recipe">
  <div class="top"><span class="tag">%s</span><span class="num">%s</span></div>
  <h1>%s</h1>
  <p class="hook">%s</p>
  <div class="grid">
    <div class="photo">%s</div>
    <div>
      <div class="stats">
        <div class="stat"><div class="v">%s</div><div class="l">%s</div></div>
        <div class="stat"><div class="v">%s</div><div class="l">%s</div></div>
        <div class="stat"><div class="v">~%d</div><div class="l">%s</div></div>
      </div>
      <h2>%s</h2>
      <ul class="ings">%s</ul>
    </div>
  </div>
  <div class="steps"><h2>%s</h2><ol>%s</ol></div>
  %s
  <div class="tip"><b>%s</b><p>%s</p></div>
  <div class="foot">%s</div>
</div>""" % (html.escape(rotulo), html.escape(num_label), html.escape(r["nome"]),
            html.escape(r["hook"]), foto_html,
            html.escape(r["tempo"]), T["st_tempo"],
            html.escape(r["rende"]), T["st_rende"],
            r["kcal_base"], T["st_kcal"],
            T["h_ings"], ings, T["h_passos"], passos, ajuste,
            T["h_dica"], html.escape(r["dica"]), T["foot"])


def montar_html(receitas, tipo, titulo, num0=1, img_dir=None, lang="pt"):
    corpo = "\n".join(render_receita(r, tipo, num0 + i, img_dir, lang=lang)
                      for i, r in enumerate(receitas))
    return """<!DOCTYPE html><html lang="%s"><head><meta charset="utf-8">
<title>%s</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700;800;900&display=swap" rel="stylesheet">
<style>%s%s</style></head><body>%s</body></html>""" % (
        I18N[lang]["html_lang"], html.escape(titulo),
        ESTILO, I18N[lang]["css"], corpo)


def gerar_pdf(html_path, pdf_path, porta=8132):
    """Chrome headless: HTML servido em localhost -> PDF (mesmo motor do navegador)."""
    nome = os.path.basename(html_path)
    url = "http://127.0.0.1:%d/%s" % (porta, nome)
    subprocess.run([CHROME, "--headless=new", "--disable-gpu",
                    "--no-pdf-header-footer", "--print-to-pdf=" + pdf_path, url],
                   capture_output=True)
    return os.path.exists(pdf_path)
