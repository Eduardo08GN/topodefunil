# -*- coding: utf-8 -*-
"""Gera a `Lista de postagem.txt` das paginas de WEIGHT LOSS que sobraram.

Uso:  python funil-organico/gerar_listas_postagem.py [AAAA-MM-DD] [dias]
      (sem argumento: 2026-09-05 por 30 dias — o lote que esta' no ar)

Saida: <BASE>/<pagina>/Lista de postagem/Lista de postagem.txt — 2 posts por dia
(manha e tarde), no formato que o operador ja' lia: cabecalho de data, gancho
terminando em 👉, linha de CTA, cinco pontos e 3 hashtags.

⛔ `BASE` e' pasta LOCAL do operador e fica fora do GitHub, como as outras pastas
dele. O que se versiona aqui e' o GERADOR — as decisoes moram nele, nao na saida.

⭐ As seis paginas que sobraram sao TODAS de mulher e TODAS de weight loss:
   US Loretta e Sarah · FR Catherine e Nathalie · DE Anja e Renate.
⭐ A legenda e' LEVE e em 1a pessoa de mulher (curiosidade: *"descobri esse truque
   e mudou tudo"*), nunca a dor. Ordem do operador em 2026-09-04.

⛔⛔ A PALAVRA DO CTA MUDA POR IDIOMA: EN `Book` · DE `Buch` · FR `Livre`. As tres
ja' estao cadastradas na automacao de DM — palavra nova exige cadastro ANTES do
primeiro lote, senao o comentario entra e a mensagem nao sai.

⛔⛔ HASHTAG NUNCA COLIDE ENTRE PAGINAS DO MESMO IDIOMA. Ordem do operador:
*"a sequencia das hashtags entre as paginas nao deve ser repetida nunca para nao
disputar publico no mesmo post"*. O guarda e' o `tag_off` de cada pagina: as duas
paginas de um idioma nascem META-POOL afastadas, entao a janela de 3 nunca se
sobrepoe. Medido: 60 slots por par, 0 sequencia igual e 0 hashtag em comum.
⚠️ Por isso o pool de cada idioma tem que continuar com TAMANHO PAR e os dois
`tag_off` do idioma separados por metade dele. Mexer num sem o outro reabre a
colisao — e ela e' silenciosa, nao quebra nada, so' faz as paginas brigarem.

⚠️ Os pools de hashtag foram varridos em 2026-09-08 por ALINHAMENTO COM O NICHO
(o porque de cada troca esta' comentado dentro de cada pool). A avaliacao foi
SEMANTICA — volume real no Facebook/Instagram nao foi medido.
"""
import os, sys, datetime

BASE = r"C:/Users/lucas/Desktop/Páginas"
DIAS_PT = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]  # Mon..Sun
INICIO = datetime.date(2026, 9, 5)
N_DIAS = 30

POOLS = {
 "en": {
  "hooks": [
   "I found this little trick and it changed everything for me 👉",
   "One spoon every morning and the weight started melting off 👉",
   "I still can't believe how fast this helped me lose weight 👉",
   "This little recipe made all the difference for me 👉",
   "I wish someone had told me about this trick sooner 👉",
   "Since I started this, my clothes finally fit again 👉",
   "I tried this at home and the pounds just came off 👉",
   "This is the little morning habit that changed my body 👉",
   "I lost the weight without the gym and without dieting 👉",
   "My friends keep asking what I did differently 👉",
   "This simple trick did what every diet failed to do 👉",
   "A few weeks in and I feel like a whole new woman 👉",
  ],
  "ctas": [
   "Comment Book and I'll send it to you 👇",
   "Comment Book and I'll send you the recipe 👇",
   "Just comment Book and it's yours 👇",
  ],
  "tags": ["#weightloss", "#fatloss", "#bellyfat", "#loseweight", "#transformation",
           "#beforeandafter", "#over40", "#over50", "#metabolism", "#metabolismboost",
           "#morningdrink", "#healthyhabits", "#healthyrecipes", "#naturalremedy",
           "#homeremedies", "#fatlosstips", "#weightlossjourney", "#weightlosstransformation"],
 },
 "fr": {
  "hooks": [
   "J'ai découvert cette petite astuce et ça a tout changé pour moi 👉",
   "Une cuillère chaque matin et les kilos ont commencé à partir 👉",
   "Je n'arrive toujours pas à croire à quelle vitesse j'ai maigri 👉",
   "Cette petite recette a fait toute la différence pour moi 👉",
   "J'aurais aimé connaître cette astuce bien plus tôt 👉",
   "Depuis que j'ai commencé, mes vêtements me vont enfin 👉",
   "J'ai essayé ça à la maison et les kilos sont partis tout seuls 👉",
   "C'est la petite habitude du matin qui a transformé mon corps 👉",
   "J'ai perdu du poids sans sport et sans régime 👉",
   "Mes amies me demandent ce que j'ai fait de différent 👉",
   "Cette astuce toute simple a réussi là où les régimes ont échoué 👉",
   "Quelques semaines et je me sens comme une nouvelle femme 👉",
  ],
  "ctas": [
   "Commente Livre et je te l'envoie 👇",
   "Commente Livre et je t'envoie la recette 👇",
   "Écris Livre en commentaire et c'est à toi 👇",
  ],
  # ⛔ Fora: #transformation (cross-nicho em FR: reforma, cabelo, móveis),
  # #santé e #bienêtre (wellness genérico + flerta com claim de saúde),
  # #métabolisme (tag técnica, pouco usada em FR), #mangersain (genérico).
  # ⭐ Entra: #rééquilibragealimentaire (a maior do emagrecimento em francês),
  # a variante SEM acento (é outra hashtag no IG/FB e muita gente digita assim),
  # e as de RECEITA, que é o que o produto é.
  "tags": ["#perdredupoids", "#minceur", "#maigrir", "#pertedepoids", "#régime",
           "#rééquilibragealimentaire", "#astuceminceur", "#recetteminceur", "#mincir",
           "#ventreplat", "#objectifminceur", "#motivationminceur", "#recettesminceur",
           "#reequilibragealimentaire", "#pertedepoidsnaturelle", "#maigrirsansrégime"],
 },
 "de": {
  "hooks": [
   "Ich habe diesen kleinen Trick entdeckt und er hat alles verändert 👉",
   "Ein Löffel jeden Morgen und die Kilos purzelten 👉",
   "Ich kann immer noch nicht glauben, wie schnell ich abgenommen habe 👉",
   "Dieses kleine Rezept hat für mich den Unterschied gemacht 👉",
   "Ich wünschte, ich hätte diesen Trick viel früher gekannt 👉",
   "Seit ich das mache, passen meine Klamotten endlich wieder 👉",
   "Ich habe es zu Hause probiert und die Kilos sind einfach verschwunden 👉",
   "Das ist die kleine Morgenroutine, die meinen Körper verändert hat 👉",
   "Ich habe abgenommen, ohne Sport und ohne Diät 👉",
   "Meine Freundinnen fragen, was ich anders gemacht habe 👉",
   "Dieser einfache Trick hat geschafft, woran jede Diät scheiterte 👉",
   "Ein paar Wochen und ich fühle mich wie eine neue Frau 👉",
  ],
  "ctas": [
   "Kommentiere Buch und ich schicke es dir 👇",
   "Kommentiere Buch und ich schicke dir das Rezept 👇",
   "Schreib Buch in die Kommentare und es gehört dir 👇",
  ],
  # ⛔ Fora: #figur (sozinho = personagem/estátua, ambíguo), #gesundleben
  # (wellness genérico), #abnehmreise (traducao literal de "weight loss journey"
  # que alemao nao usa), #motivationabnehmen (ordem invertida — a real e'
  # #abnehmmotivation), #stoffwechselanregen (frase verbal, fraca como tag),
  # #ernährung (nutricao em geral, dilui o nicho).
  # ⭐ Entra: #traumfigur, #abnehmmotivation e #kaloriendefizit (termos reais do
  # nicho em alemao) + as de RECEITA, que e' o que o produto e'.
  "tags": ["#abnehmen", "#abnehmtipps", "#stoffwechsel", "#gesundabnehmen",
           "#abnehmenmitgenuss", "#rezeptezumabnehmen", "#gesundeernährung", "#kaloriendefizit",
           "#traumfigur", "#fettverbrennung", "#bauchfett", "#abnehmrezepte",
           "#abnehmenohnesport", "#schlankwerden", "#wohlfühlgewicht", "#abnehmmotivation"],
 },
}

# ⛔ Cada pagina tem deslocamentos PROPRIOS (hook, cta, hashtag). As duas paginas
# do MESMO idioma ficam meio-pool afastadas na hashtag -> no mesmo slot elas nunca
# compartilham NENHUMA hashtag (janela de 3, distancia = metade do pool). Idiomas
# diferentes ja' tem pools distintos. Assim a sequencia nunca colide entre paginas.
# (rel, lang, nome, hook_off, cta_off, tag_off)
PAGINAS = [
 ("EUA/Brancos/Loretta Mayfield - Mulher Branca - Comprada", "en", "Loretta Mayfield", 0, 0, 0),
 ("EUA/Brancos/Sarah Brown - M Branca - Antiga Minha",       "en", "Sarah Brown",      6, 1, 9),
 ("FRENCH/Catherine Martin",        "fr", "Catherine Martin", 0, 0, 0),
 ("FRENCH/Nathalie Bernard",        "fr", "Nathalie Bernard", 6, 1, 8),
 ("German/Anja Hoffmann",           "de", "Anja Hoffmann",    0, 0, 0),
 ("German/Renate Vogel - Criada",   "de", "Renate Vogel",     6, 2, 8),
]


def gera(lang, ho=0, co=0, to=0):
    P = POOLS[lang]
    h, c, t = P["hooks"], P["ctas"], P["tags"]
    nt = len(t)
    out = []
    contador = 0
    for d in range(N_DIAS):
        dia = INICIO + datetime.timedelta(days=d)
        cab = "============== %02d.%02d (%s) ==============" % (dia.day, dia.month, DIAS_PT[dia.weekday()])
        out.append(cab)
        out.append("")
        for post in (1, 2):
            hook = h[(contador + ho) % len(h)]
            cta = c[(contador + co) % len(c)]
            base = contador * 3 + to
            tri = "%s %s %s" % (t[base % nt], t[(base+1) % nt], t[(base+2) % nt])
            out.append("%d. %s" % (post, hook))
            out.append(cta)
            out.append(".\n.\n.\n.\n.")
            out.append(tri)
            out.append("")
            contador += 1
        out.append("")  # segunda linha em branco entre blocos de data
    return "\n".join(out).rstrip() + "\n"


# argumentos opcionais: data de inicio (AAAA-MM-DD) e quantidade de dias.
# Sem eles, reproduz exatamente o lote que esta' no ar.
if len(sys.argv) > 1:
    INICIO = datetime.date(*[int(x) for x in sys.argv[1].split("-")])
if len(sys.argv) > 2:
    N_DIAS = int(sys.argv[2])
if not os.path.isdir(BASE):
    sys.exit("BASE nao encontrada: %s\n(pasta local do operador — ajuste a "
             "constante BASE no topo)" % BASE)

tot = 0
for rel, lang, nome, ho, co, to in PAGINAS:
    pasta = os.path.join(BASE, rel, "Lista de postagem")
    os.makedirs(pasta, exist_ok=True)
    caminho = os.path.join(pasta, "Lista de postagem.txt")
    with open(caminho, "w", encoding="utf-8-sig") as f:
        f.write(gera(lang, ho, co, to))
    posts = N_DIAS * 2
    tot += posts
    print("OK  %-18s [%s]  %d posts  ->  %s" % (nome, lang, posts, caminho))
print("Total: %d posts em %d paginas" % (tot, len(PAGINAS)))
