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

⭐ 5 A 8 HASHTAGS POR POST (era 3 fixas), pool de 28 por idioma. Veio da leitura
de concorrente que o operador trouxe em 2026-09-08: eles postam de 5 a 8, e a
composicao mistura NUCLEO do nicho + SINTOMA (#bloating, #flatbelly) + RITUAL
(#morningdrink) + CASEIRO (#homeremedy) + ALCANCE (#fbreels). A quantidade CICLA
em `QTD_TAGS` porque na fonte ela varia de post para post — bloco de tamanho fixo
e' assinatura de automacao.
⛔ INGREDIENTE NAO VIRA HASHTAG. A fonte poe #bakingsoda quando a receita leva
bicarbonato; decisao do operador e' nao acompanhar. A lista cobre 30 dias de
receitas diferentes, entao a tag so' seria verdadeira em algumas.
⭐ A ORDEM DENTRO DO POOL NAO E' DECORATIVA: o nucleo cai em 3 de cada 7
posicoes, entao QUALQUER janela sai equilibrada. Enfileirar as tags por familia
faria um post nascer so' de barriga e o seguinte so' de receita.

⛔⛔ HASHTAG NUNCA COLIDE ENTRE PAGINAS DO MESMO IDIOMA. Ordem do operador:
*"a sequencia das hashtags entre as paginas nao deve ser repetida nunca para nao
disputar publico no mesmo post"*. O guarda e' o `tag_off`: as duas paginas de um
idioma nascem META-POOL afastadas (14 de 28), entao as janelas caem em metades
opostas e nao se tocam. ⚠️ Por isso a janela MAXIMA (8) tem que caber em metade
do pool — foi essa conta que obrigou o pool a crescer de 16-18 para 28.
⭐ Quem cobra isso agora e' `_conferir()`, que roda ANTES de gravar e compara os
dois lados slot a slot. A colisao e' SILENCIOSA — nada quebra, as paginas so'
passam a brigar pelo mesmo publico —, entao comentario nao bastava.

⚠️ Os pools foram montados por ALINHAMENTO COM O NICHO (o porque de cada troca
esta' comentado dentro de cada pool). A avaliacao e' SEMANTICA — volume real no
Facebook/Instagram nao foi medido.
"""
import os, sys, random, datetime

BASE = r"C:/Users/lucas/Desktop/Páginas"
DIAS_PT = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]  # Mon..Sun
INICIO = datetime.date(2026, 9, 5)
N_DIAS = 30

# ⭐ Quantas hashtags por post. CICLA — a fonte varia de 5 a 8, e bloco de tamanho
# fixo e' assinatura de automacao. ⛔ O maximo TEM que caber em metade do pool,
# senao as duas paginas do idioma voltam a dividir hashtag (`_conferir()` barra).
QTD_TAGS = [8, 6, 7, 5]
# ⭐ De quanto a janela anda por post. 5 e' coprimo de 28, entao ela passa pelas 28
# posicoes antes de repetir; e como 5 e' MENOR que a janela, posts seguidos dividem
# 2 ou 3 tags — que e' o que a fonte faz com as ancoras dela (#over50, #bloating).
PASSO_TAG = 5

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
  # ⭐ As 18 antigas continuam todas aqui; entram 10 das familias que a fonte usa
  # e nos nao tinhamos: SINTOMA (#bloating, #flatbelly, #stubbornfat, #guthealth),
  # RITUAL (#morningritual), CASEIRO (#homeremedy — singular, e' outra tag),
  # #holistichealth, #weightlossrecipes e as de ALCANCE (#fbreels, #usareels).
  # ⚠️ As duas de alcance ficam a 13 posicoes uma da outra de proposito: assim no
  # maximo UMA cai por post. Elas trazem volume, nao publico qualificado.
  "tags": ["#weightloss", "#bellyfat", "#loseweight", "#bloating", "#fatloss",
           "#morningdrink", "#healthyrecipes", "#over50", "#flatbelly", "#weightlossjourney",
           "#homeremedy", "#metabolism", "#guthealth", "#usareels", "#fatlosstips",
           "#stubbornfat", "#over40", "#naturalremedy", "#weightlossrecipes", "#metabolismboost",
           "#morningritual", "#weightlosstransformation", "#holistichealth", "#beforeandafter",
           "#homeremedies", "#transformation", "#fbreels", "#healthyhabits"],
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
  # ⭐ 2a rodada (mesmo dia): as 16 varridas ficam todas, entram 12 das familias
  # novas — SINTOMA (#ballonnements, #ventregonflé, #graisseabdominale,
  # #perdreduventre, #kilosentrop, #digestion), RITUAL (#routinematinale,
  # #boissonminceur), NATURAL (#remedesnaturels, #minceurnaturelle),
  # #astucesminceur (plural, e' outra tag) e #fbreels.
  # ⚠️ #ballonnements e o par ventre gonflé/ventre plat sao o equivalente frances
  # de #bloating/#flatbelly, o eixo que mais aparece na fonte e que nos faltava.
  "tags": ["#perdredupoids", "#ventreplat", "#minceur", "#recetteminceur", "#maigrir",
           "#ballonnements", "#routinematinale", "#pertedepoids", "#graisseabdominale",
           "#rééquilibragealimentaire", "#astuceminceur", "#régime", "#perdreduventre",
           "#remedesnaturels", "#mincir", "#kilosentrop", "#objectifminceur", "#recettesminceur",
           "#motivationminceur", "#digestion", "#boissonminceur", "#pertedepoidsnaturelle",
           "#ventregonflé", "#maigrirsansrégime", "#astucesminceur",
           "#reequilibragealimentaire", "#minceurnaturelle", "#fbreels"],
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
  # ⭐ 2a rodada (mesmo dia): as 16 varridas ficam todas, entram 12 das familias
  # novas — SINTOMA (#blähbauch, #flacherbauch, #bauchfettverlieren, #verdauung,
  # #darmgesundheit), RITUAL (#morgenroutine, #morgenritual), CASEIRO (#hausmittel,
  # #natürlichabnehmen), RECEITA (#gesunderezepte), #abnehmenab40 e #fbreels.
  # ⚠️ #blähbauch e #flacherbauch sao o par #bloating/#flatbelly em alemao, e
  # #hausmittel e' o #homeremedy deles — as tres faltavam e sao centrais na fonte.
  "tags": ["#abnehmen", "#bauchfett", "#abnehmtipps", "#abnehmrezepte", "#gesundabnehmen",
           "#blähbauch", "#morgenroutine", "#schlankwerden", "#stoffwechsel", "#abnehmmotivation",
           "#hausmittel", "#kaloriendefizit", "#flacherbauch", "#rezeptezumabnehmen",
           "#traumfigur", "#verdauung", "#abnehmenmitgenuss", "#natürlichabnehmen",
           "#fettverbrennung", "#gesundeernährung", "#morgenritual", "#abnehmenohnesport",
           "#darmgesundheit", "#wohlfühlgewicht", "#gesunderezepte", "#abnehmenab40",
           "#bauchfettverlieren", "#fbreels"],
 },
}

# ⛔ Cada pagina tem deslocamentos PROPRIOS (hook, cta, hashtag). As duas paginas
# do MESMO idioma ficam meia-pool afastadas na hashtag (14 de 28) -> as janelas
# caem em metades opostas do pool e no mesmo slot elas nao dividem NENHUMA
# hashtag. Idiomas diferentes ja' tem pools distintos. `_conferir()` mede isso
# antes de gravar. ⭐ O tag_off desloca tambem a QUANTIDADE de tags (14 % 4 = 2),
# entao as duas paginas do idioma nem postam o mesmo numero de hashtags no dia.
# (rel, lang, nome, hook_off, cta_off, tag_off)
PAGINAS = [
 ("EUA/Brancos/Loretta Mayfield - Mulher Branca - Comprada", "en", "Loretta Mayfield", 0, 0, 0),
 ("EUA/Brancos/Sarah Brown - M Branca - Antiga Minha",       "en", "Sarah Brown",      6, 1, 14),
 ("FRENCH/Catherine Martin",        "fr", "Catherine Martin", 0, 0, 0),
 ("FRENCH/Nathalie Bernard",        "fr", "Nathalie Bernard", 6, 1, 14),
 ("German/Anja Hoffmann",           "de", "Anja Hoffmann",    0, 0, 0),
 ("German/Renate Vogel - Criada",   "de", "Renate Vogel",     6, 2, 14),
]


def linhas_de_tags(lang, to, n_slots, vistas=None):
    """As linhas de hashtag de UMA pagina inteira, na ordem dos posts.
    Fonte unica: `gera()` e `_conferir()` leem daqui — senao a prova de
    nao-colisao mediria uma coisa e o arquivo sairia com outra.

    ⭐ Duas coisas acontecem aqui, e as duas mexem so' na ORDEM, nunca no
    CONJUNTO — e' isso que preserva a prova de nao-colisao, que compara conjuntos:

    1. EMBARALHA dentro do post. Sem isso a janela deslizante ficava visivel na
       pagina: o post da tarde comecava com as mesmas 3 ultimas tags do post da
       manha, na mesma ordem. Costura de automacao que qualquer um enxerga.
    2. REJEITA linha ja' usada nesta pagina. A janela volta ao mesmo conjunto a
       cada 28 posts (o pool tem 28 e o passo e' coprimo dele), e em 60 posts o
       embaralho as vezes caia na mesma permutacao — medido: 3 linhas identicas
       nas 6 listas. Repetir o CONJUNTO e' desejado (a fonte tem ancoras que
       voltam); repetir a LINHA inteira, nao.

    ⛔ `vistas` e' COMPARTILHADO pelo lote inteiro (ver `todas_as_linhas`): a
    mesma sequencia em duas paginas, ainda que em dias diferentes, e' impressao
    digital que liga as contas uma a' outra.
    """
    t = POOLS[lang]["tags"]
    nt = len(t)
    linhas = []
    if vistas is None:
        vistas = set()
    for i in range(n_slots):
        n = QTD_TAGS[(i + to) % len(QTD_TAGS)]
        base = i * PASSO_TAG + to
        janela = [t[(base + k) % nt] for k in range(n)]
        linha = None
        for tentativa in range(200):
            random.Random("%s|%d|%d|%d" % (lang, i, to, tentativa)).shuffle(janela)
            linha = " ".join(janela)
            if linha not in vistas:
                break
        vistas.add(linha)
        linhas.append(linha)
    return linhas


def todas_as_linhas():
    """As linhas de hashtag das SEIS paginas de uma vez, com memoria unica.
    E' o que garante que nenhuma sequencia se repita em lugar nenhum do lote."""
    vistas = set()
    return dict((rel, linhas_de_tags(lang, to, N_DIAS * 2, vistas))
                for rel, lang, nome, ho, co, to in PAGINAS)


def gera(lang, tags, ho=0, co=0):
    P = POOLS[lang]
    h, c = P["hooks"], P["ctas"]
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
            out.append("%d. %s" % (post, hook))
            out.append(cta)
            out.append(".\n.\n.\n.\n.")
            out.append(tags[contador])
            out.append("")
            contador += 1
        out.append("")  # segunda linha em branco entre blocos de data
    return "\n".join(out).rstrip() + "\n"


def _conferir():
    """Prova, ANTES de gravar, que duas paginas do mesmo idioma nao dividem
    hashtag em slot nenhum. Fica em codigo e nao em comentario porque a colisao
    e' silenciosa: nada quebra, as paginas so' passam a brigar pelo mesmo post."""
    todas = [l for linhas in TODAS.values() for l in linhas]
    assert len(set(todas)) == len(todas), (
        "sequencia de hashtag repetida no lote (%d de %d unicas)"
        % (len(set(todas)), len(todas)))
    for lang, P in POOLS.items():
        tags, n = P["tags"], len(P["tags"])
        assert n % 2 == 0, "%s: o pool de hashtag tem que ser PAR (esta' %d)" % (lang, n)
        assert len(set(tags)) == n, "%s: hashtag repetida no pool" % lang
        assert max(QTD_TAGS) <= n // 2, (
            "%s: %d tags por post nao cabem em meia pool de %d — reabre a colisao"
            % (lang, max(QTD_TAGS), n))
        offs = sorted(p[5] for p in PAGINAS if p[1] == lang)
        assert offs == [0, n // 2], (
            "%s: os tag_off tem que ser 0 e %d, estao %s" % (lang, n // 2, offs))
    # a medicao de verdade, sobre as linhas que vao mesmo para o arquivo
    for lang in POOLS:
        pg = [p for p in PAGINAS if p[1] == lang]
        if len(pg) != 2:
            continue
        A, B = TODAS[pg[0][0]], TODAS[pg[1][0]]
        for i, (la, lb) in enumerate(zip(A, B)):
            comum = set(la.split()) & set(lb.split())
            assert not comum, "%s slot %d divide %s" % (lang, i, sorted(comum))


# argumentos opcionais: data de inicio (AAAA-MM-DD) e quantidade de dias.
# Sem eles, reproduz exatamente o lote que esta' no ar.
if len(sys.argv) > 1:
    INICIO = datetime.date(*[int(x) for x in sys.argv[1].split("-")])
if len(sys.argv) > 2:
    N_DIAS = int(sys.argv[2])
TODAS = todas_as_linhas()
_conferir()
if not os.path.isdir(BASE):
    sys.exit("BASE nao encontrada: %s\n(pasta local do operador — ajuste a "
             "constante BASE no topo)" % BASE)

tot = 0
for rel, lang, nome, ho, co, to in PAGINAS:
    pasta = os.path.join(BASE, rel, "Lista de postagem")
    os.makedirs(pasta, exist_ok=True)
    caminho = os.path.join(pasta, "Lista de postagem.txt")
    with open(caminho, "w", encoding="utf-8-sig") as f:
        f.write(gera(lang, TODAS[rel], ho, co))
    posts = N_DIAS * 2
    tot += posts
    print("OK  %-18s [%s]  %d posts  ->  %s" % (nome, lang, posts, caminho))
print("Total: %d posts em %d paginas" % (tot, len(PAGINAS)))
