"""Transcricao (faster-whisper, offline) + geracao de legenda ASS estilo CapCut
word-by-word (karaoke fill: a palavra falada acende, o resto da linha fica em
espera). Timestamps por palavra vem do Whisper."""

import re

from faster_whisper import WhisperModel

_MODELO = {}  # cache por tamanho, pra nao recarregar a cada video


# ⭐⭐ IDIOMA (2026-08-30). Ordem: *"O Veo editor esta' preparado para
# reconhecer audios e gerar legendas em alemao e frances?"*. Nao estava: os
# tres modelos do menu eram `.en` e o `lang` nunca saia de "en".
IDIOMAS = {"en": "Ingles", "de": "Alemao", "fr": "Frances"}


def modelo_para(model_size, language):
    """O modelo TEM de casar com o idioma, e por isso a escolha e' derivada.

    ⛔⛔ `small.en` com audio alemao NAO DA ERRO. O modelo so'-ingles
    transcreve o alemao foneticamente como se fosse ingles, e a legenda sai
    lixo com aparencia de legenda: o operador nao ve' falha nenhuma, ve' um
    video pronto com palavra errada. Silencio identico ao do acerto.

    ⭐ Por isso o app nao deixa escolher modelo e idioma separados: o idioma
    manda, e o sufixo `.en` e' colocado ou tirado aqui. Combinacao quebrada
    deixa de ser possivel por construcao.

    ⚠️ E o `.en` fica no ingles de proposito: para audio ingles o modelo
    so'-ingles e' mais preciso e mais rapido que o multilingue do mesmo porte.
    """
    base = (model_size or "base").replace(".en", "")
    return base + ".en" if (language or "en") == "en" else base


def transcrever(audio_path, model_size="base.en", language="en"):
    """Retorna lista de {text, start, end} por palavra."""
    model_size = modelo_para(model_size, language)
    if model_size not in _MODELO:
        _MODELO[model_size] = WhisperModel(model_size, device="cpu", compute_type="int8")
    model = _MODELO[model_size]
    segments, _info = model.transcribe(
        audio_path, language=language, word_timestamps=True, vad_filter=True
    )
    palavras = []
    for seg in segments:
        for w in (seg.words or []):
            t = w.word.strip()
            if t:
                palavras.append({"text": t, "start": float(w.start), "end": float(w.end)})
    return palavras


def _cs(seg):
    """segundos -> centesimos de segundo (unidade do \\k do ASS)."""
    return max(1, int(round(seg * 100)))


def _ass_time(t):
    h = int(t // 3600)
    m = int((t % 3600) // 60)
    s = t % 60
    return f"{h:d}:{m:02d}:{s:05.2f}"


def _ass_cor(hexa, padrao="&H00000000"):
    """#RRGGBB -> &H00BBGGRR (o ASS guarda a cor em BGR, ao contrario).

    ⛔ A INVERSAO E' O PONTO. Passar o hex direto nao da erro: da a cor
    errada, com o vermelho e o azul trocados. Amarelo #F0D000 vira
    &H0000D0F0 — e um azul #0000FF viraria &H00FF0000, que e' vermelho.
    """
    t = (hexa or "").strip().lstrip("#")
    if len(t) != 6:
        return padrao
    try:
        r, g, b = int(t[0:2], 16), int(t[2:4], 16), int(t[4:6], 16)
    except ValueError:
        return padrao
    return "&H00%02X%02X%02X" % (b, g, r)


def _ass_cor_alfa(hexa, alfa_pct, padrao="&H00000000"):
    """Como `_ass_cor`, mas com TRANSPARENCIA. alfa_pct: 0 opaco, 100 invisivel.

    ⛔ O `_ass_cor` crava `&H00` no comeco, e aquele `00` e' o canal ALFA do
    ASS — por isso a caixa da legenda fixa sempre saiu solida, sem que
    existisse opcao nenhuma de mudar isso.

    ⚠️ No ASS o alfa e' INVERTIDO em relacao ao que a pessoa espera: 00 e'
    totalmente OPACO e FF e' totalmente INVISIVEL. Medido em render, com
    caixa sobre fundo verde: 00 solida, 80 metade, FF sumiu e sobrou so' o
    texto.
    """
    base = _ass_cor(hexa, padrao)
    try:
        a = int(round(max(0.0, min(100.0, float(alfa_pct))) * 255.0 / 100.0))
    except (TypeError, ValueError):
        a = 0
    return "&H%02X%s" % (a, base[4:]) if len(base) == 10 else base


def _limpa(texto, maiuscula):
    # tira pontuacao/virgula solta no comeco (whisper as vezes destaca ela);
    # mantem a do fim. Neutraliza chaves que quebrariam o ASS.
    texto = re.sub(r"^[\s,.;:!?\-]+", "", texto.strip())
    texto = texto.replace("{", "(").replace("}", ")").replace("\\", "")
    return texto.upper() if maiuscula else texto


# palavras-gatilho do CTA ("comment GELATIN"): ganham cor propria e fonte maior
# para o espectador assimilar de cara o que digitar nos comentarios
KEYWORDS_PADRAO = ("HONEY", "GELATIN", "VICK", "VICKS", "RECIPE")


# =========================================================================
# ⭐⭐ O EFEITO "CIRCULADO + HERE" — 2026-08-28
# =========================================================================
# Ordem do operador, com um reel na mao: *"Quero que voce ajuste o Veo editor
# para ter uma chave para ligar esse efeito de circulado vermelho escrito Here
# nesse local do video em anexo"*, e logo depois: *"A chave deve ativar em
# todos os takes, e o local que aparece o circulado e o here deve ser
# selecionavel ali no seletor das legendas"*.
#
# ⛔ NAO E' UM PNG SOBREPOSTO, e a escolha tem consequencia: como e' desenho
# vetorial do proprio ASS (`\p1`), ele entra na MESMA queimada da legenda —
# nenhum passo novo de ffmpeg, nenhum arquivo de imagem para sumir, e escala
# sozinho de 720x1280 para 1080x1920 sem serrilhar.
#
# ⛔⛔ E O ASS NAO TEM "STROKE": `\p1` so' PREENCHE. Entao cada traco e'
# construido como CONTORNO — a curva deslocada de +w/2 na normal e a volta com
# -w/2. E' o que permite a espessura variar ao longo do traco, que e' o que faz
# parecer caneta. Uma elipse de `m ... b ...` sairia com espessura constante e
# denunciaria a ferramenta.
#
# ⭐ AS MEDIDAS SAIRAM DO VIDEO, componente conexa por componente conexa, em
# tres frames (t=3s, 10s, 18s) do reel que ele mandou — 720x1280:
#     elipse   x 454..706 (252)  y 794..951 (157)   traco ~9px, #F01010
#     "here"   x 572..689 (117)  y 724..767  (43)   vermelho com contorno branco
#     seta     x 448..533  (85)  y 682..783 (101)
# ⭐ Os tres sao IDENTICOS nos tres frames: o efeito e' ESTATICO no video
# inteiro — que e' exatamente o "em todos os takes" que ele pediu.
#
# ⚠️ TUDO ESCALA PELA LARGURA, inclusive as distancias verticais. O quadro e'
# 9:16 em todo o parque, entao largura e altura escalam juntas; usar as duas
# escalas separadas distorceria o desenho num video fora dessa proporcao, e
# distorcer e' pior que ficar pequeno.
# ⭐ A palavra do circulado muda com o idioma (2026-08-30). Um "here" num
# video alemao denuncia que o criativo foi feito em outra lingua.
AQUI_POR_IDIOMA = {"en": "here", "de": "hier", "fr": "ici"}
AQUI_TEXTO = AQUI_POR_IDIOMA["en"]


def aqui_texto_para(language):
    return AQUI_POR_IDIOMA.get((language or "en"), AQUI_POR_IDIOMA["en"])
_AQ_REF_W = 720.0                    # a largura em que tudo foi medido
# ⚠️ 118/72,5 e' o ESTADO PEQUENO da fonte (caixa 243x151), nao o
# tamanho medio: o pulso so' sobe, entao o repouso tem de ser o menor dos
# dois estados. Com 122/75 a caixa dava 251 e o pico passaria de 276.
_AQ_EL_RX, _AQ_EL_RY = 118.0, 72.5   # raios da elipse (centro = a ancora)
_AQ_EL_TRACO = 9.0
_AQ_TX_DX, _AQ_TX_DY = 50.5, -134.0  # centro do "here", relativo a ancora
_AQ_TX_FONTE = 72.0
_AQ_TX_GIRO = 7                      # graus: sobe para a direita, como a fonte
# ⚠️ O 112 saiu de MEDIR o render, nao de gosto: com Arial Black a 72 o bloco
# vermelho sai 121x37 e o da fonte e' 117x43. A largura ja' casa; o que falta e'
# altura, porque a fonte do reel e' mais estreita e mais alta que a Arial Black.
# Esticar so' o eixo Y encaixa os dois sem trocar de tipografia.
_AQ_TX_FSCY = 112
_AQ_SETA = {                         # pontos relativos a ancora
    "ini": (-131.0, -187.5),         # onde a caneta encosta
    "ctrl": (-72.0, -170.0),         # controle da curva
    "ponta": (-62.5, -95.0),         # vertice do V
    "farpa_esq": (-99.0, -124.0),
    "farpa_dir": (-55.0, -150.0),
}
_AQ_SETA_TRACO = 11.0
# ⭐ o pulso, medido no reel: 0,40 s de periodo e 110% de pico
_AQ_PULSO_T = 0.40
_AQ_PULSO_AMP = 110
# ⭐⭐ A SETA NAO PULSA: ela ESTICA PARA DENTRO DO CIRCULO e volta.
# Ordem do operador: *"quero que a seta pulse tambem (...) ou fique com
# efeito de esticar e voltar que seria melhor ainda, apontando para
# dentro do circulo"*.
# ⛔ O truque e' ONDE fica a origem do desenho. Ancorada na CAUDA (onde a
# caneta encosta), escalar o desenho empurra a PONTA para longe da cauda —
# e a ponta aponta para o circulo. O mesmo `\fscx` que no circulo e' um
# pulso concentrico, aqui vira uma estocada na direcao do alvo.
# ⚠️ 115 e nao 110: a seta mede ~85x101, entao 115%% avanca a ponta ~10 px
# na diagonal. Com 110%% o movimento fica em 7 px e some no video.
_AQ_SETA_AMP = 115


def _aq_poligono(centro, larguras):
    """Uma linha de espessura variavel vira POLIGONO FECHADO (ver acima)."""
    import math
    n = len(centro)
    esq, dir_ = [], []
    for i, (x, y) in enumerate(centro):
        px, py = centro[max(0, i - 1)]
        nx, ny = centro[min(n - 1, i + 1)]
        dx, dy = nx - px, ny - py
        m = math.hypot(dx, dy) or 1.0
        ox, oy = -dy / m, dx / m                     # normal unitaria
        w = larguras[i] / 2.0
        esq.append((x + ox * w, y + oy * w))
        dir_.append((x - ox * w, y - oy * w))
    return esq + list(reversed(dir_))


def _aq_afina(t):
    """Perfil de espessura da caneta ao longo do traco.

    ⚠️ NAO e' simetrico, e isso saiu do render lado a lado com a fonte: la' o
    traco JA' COMECA GROSSO (a caneta encosta com forca) e so' o fim, o excesso
    que passa do ponto, afina. Com perfil simetrico a cauda ficava fina demais e
    o circulo lia como desenhado por software.
    """
    ini = 0.62 + 0.38 * min(1.0, t / 0.12)
    fim = 1.0 if t < 0.88 else 1.0 - 0.55 * (t - 0.88) / 0.12
    return min(ini, fim)


def _aq_elipse(rx, ry, traco, passos=150):
    """A volta de caneta: comeca dentro, da' a volta e PASSA DO PONTO.

    ⭐ Sao tres coisas que separam "circulado a mao" de "elipse de programa", e
    as tres estao aqui porque as tres aparecem na fonte: o excesso (392 graus,
    nao 360), o bamboleio do raio, e a CAUDA que entra para dentro no comeco.
    """
    import math
    a0, sweep = math.radians(175), math.radians(392)
    pts, ws = [], []
    for i in range(passos + 1):
        t = i / float(passos)
        a = a0 + sweep * t
        k = 1.0 + 0.030 * math.sin(3.0 * a + 0.7)    # bamboleio
        if t < 0.09:                                  # a cauda, para dentro
            k *= 0.62 + 0.38 * (t / 0.09)
        pts.append((rx * k * math.cos(a), ry * k * math.sin(a)))
        ws.append(traco * _aq_afina(t))
    return _aq_poligono(pts, ws)


def _aq_bezier(p0, p1, p2, passos=40):
    out = []
    for i in range(passos + 1):
        t = i / float(passos)
        u = 1 - t
        out.append((u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0],
                    u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]))
    return out


def _aq_seta(traco):
    """A seta curva: haste + duas farpas, tres contornos."""
    s = _AQ_SETA
    haste = _aq_bezier(s["ini"], s["ctrl"], s["ponta"])
    n = len(haste) - 1
    w = [traco * (0.45 + 0.55 * min(1.0, 3.0 * (i / float(n))))
         for i in range(len(haste))]
    polis = [_aq_poligono(haste, w)]
    for chave in ("farpa_esq", "farpa_dir"):
        meio = ((s["ponta"][0] + s[chave][0]) / 2.0,
                (s["ponta"][1] + s[chave][1]) / 2.0)
        polis.append(_aq_poligono([s["ponta"], meio, s[chave]],
                                  [traco, traco * 0.85, traco * 0.5]))
    return polis


def _aq_pulso(fim, b, amp=None):
    """Os `\\t` que fazem o circulo RESPIRAR — 2026-08-28.

    ⛔⛔ EU TINHA ESCRITO QUE O EFEITO ERA ESTATICO, e estava errado. A prova
    do erro: amostrei o reel em 3s, 10s e 18s e os tres frames deram a mesma
    caixa, no mesmo pixel. Amostra rala mede POSICAO, nunca MOVIMENTO. A 30 fps
    o circulo respira.

    ⭐ MEDIDO no reel, 60 quadros a 30 fps, componente conexa por componente:
        elipse   243x151  ->  267x167   (x1,099 na largura, x1,106 na altura)
        seta      79x94   ->   83x95    (x1,05 — ruido de antisserrilhado)
        "here"   117x42   ->  117x42    (x1,000 — NAO mexe)
        centro   varia 2 px em 60 quadros
    ⛔ Por isso SO' A ELIPSE pulsa aqui. O "here" cravado em 117x42 nos 60
    quadros e' medicao, nao aproximacao: se o grupo inteiro escalasse, ele iria
    a 129. Animar a seta e o texto junto seria inventar o que a fonte nao faz.

    ⭐ O PERIODO SAIU DE AUTOCORRELACAO, nao de contar picos a olho: r=+0,74 no
    lag 12-13 e r=-0,85 no lag 6 (o meio-periodo). Os dois dizem 12 quadros a
    30 fps = **0,40 s**. Picos medidos em 0,20 · 0,60 · 1,00 · 1,40 confirmam.

    ⚠️ E o repouso e' o ESTADO PEQUENO: dentro do ciclo o circulo fica ~0,15 s
    parado no 243 e so' ~0,05 s no 267. Por isso o raio base do desenho e' o do
    estado pequeno e a animacao so' sobe — nunca desce abaixo de 100%.
    """
    partes, t = [], 0.0
    # ⚠️ teto de seguranca: 400 tags cobrem 80 s de video. Alem disso o pulso
    # simplesmente para, em vez de gerar um `.ass` gigante.
    while t < fim and len(partes) < 400:
        ms = int(round(t * 1000))
        partes.append("%st(%d,%d,%sfscx%d%sfscy%d)"
                      % (b, ms, ms + 150, b, amp or _AQ_PULSO_AMP,
                         b, amp or _AQ_PULSO_AMP))
        partes.append("%st(%d,%d,%sfscx100%sfscy100)"
                      % (b, ms + 200, ms + 320, b, b))
        t += _AQ_PULSO_T
    return "".join(partes)


def _aq_desenho(largura, altura, fx, fy):
    """As pecas do efeito, prontas para virar linhas de `Dialogue`.

    `fx`/`fy` sao fracao da largura/altura — o ponto que o operador arrasta no
    seletor 9:16. Ele e' o CENTRO DA ELIPSE, porque a elipse e' o que circula a
    prova; a seta e o "here" penduram nela com deslocamento fixo, medido na
    fonte. Assim ele posiciona UMA coisa e as tres andam juntas.

    ⛔⛔ A ELIPSE SAI EM COORDENADAS RELATIVAS AO PROPRIO CENTRO, e a seta em
    coordenadas absolutas. Nao e' capricho — e' o que faz o pulso funcionar:
    com `\\an7\\pos(cx,cy)` o libass poe a ORIGEM do desenho em `pos`, e o
    `\\fscx` escala em volta dessa origem. Coordenada relativa ao centro =
    escala em volta do centro.
    ⚠️ MEDIDO, porque a primeira tentativa errou: com `\\an5` o libass ancorou a
    escala no canto inferior direito e o circulo ANDAVA 12 px a cada pulso.
    Com `\\an7` + coordenada relativa o centro fica cravado (582,870) do estado
    pequeno ao grande.
    """
    u = largura / _AQ_REF_W
    cx, cy = fx * largura, fy * altura

    def _tira(contorno, ox, oy):
        p = ["%d %d" % (round(ox + x), round(oy + y)) for x, y in contorno]
        return "m " + p[0] + " l " + " ".join(p[1:])

    elipse = _tira(_aq_elipse(_AQ_EL_RX * u, _AQ_EL_RY * u, _AQ_EL_TRACO * u),
                   0, 0)
    # ⛔ A SETA SAI RELATIVA A CAUDA, nao ao centro nem ao quadro: e' o que faz
    # o `\fscx` estica-la NA DIRECAO DA PONTA em vez de incha-la no lugar.
    # Origem no ponto onde a caneta encosta -> a ponta e' que anda.
    tx0, ty0 = _AQ_SETA["ini"][0] * u, _AQ_SETA["ini"][1] * u
    seta = "".join(_tira(c, -tx0, -ty0) for c in _aq_seta(_AQ_SETA_TRACO * u))
    return {"elipse": elipse,
            "centro": (cx, cy),
            "seta": seta,
            "cauda": (cx + tx0, cy + ty0),
            "texto": (cx + _AQ_TX_DX * u, cy + _AQ_TX_DY * u),
            "fonte": max(10, int(round(_AQ_TX_FONTE * u))),
            "bord": max(2, int(round(5.0 * u)))}



def gerar_ass(
    palavras,
    largura,
    altura,
    out_path,
    # ⭐⭐ UMA PALAVRA POR VEZ — 2026-08-14, ordem do operador: *"o problema e'
    # que eu uso o editor para varios videos, e nao da' pra controlar toda hora
    # onde a legenda nao ira' cobrir, entao diminua o tamanho e deixe uma
    # palavra por vez"*.
    #
    # ⭐ O ARGUMENTO DELE E' DE ESCALA, e vence o meu: eu media UM video e
    # ajustava a cena; ele processa dezenas, de agentes diferentes, e nao tem
    # como saber onde a cabeca vai cair em cada um. Legenda que ocupa a menor
    # area possivel e a unica que serve a todos sem inspecao.
    #
    # ⛔⛔ E O MODO DE UMA PALAVRA DUROU UM LOTE. Ele rodou o v003 e voltou:
    # *"uma por uma realmente ficou muito rapido, deixe como estava porem
    # mantenha o mesmo tamanho de legenda que esta' atualmente"*.
    # ⚠️ E o numero ja' dizia: 45 palavras em 15s = 3,0 palavras/s, 332 ms por
    # palavra. Eu MEDI isso antes de implementar e escrevi que era piscada — e
    # implementei mesmo assim, porque o argumento dele (o editor serve dezenas
    # de videos, nao da' pra inspecionar cena a cena) valia o teste. Valia: hoje
    # a decisao esta' tomada com os dois na tela, nao com dois palpites.
    #
    # ⭐ O QUE SOBREVIVEU DO EXPERIMENTO, e e' o que resolve o problema dele:
    #   · a FONTE MENOR (0.045, era 0.052) — duas linhas a 57 ocupam ~82px
    #     contra ~95px a 66, e o bloco passa a terminar em 17,3% da altura, com
    #     a cabeca dele comecando em 19,9% no pior frame medido. Antes encostava;
    #   · o ESTICA-ATE-A-PROXIMA logo abaixo, que nasceu para o modo de uma
    #     palavra e serve igual aqui — buraco entre blocos e' buraco.
    # ⭐⭐ TRES PALAVRAS POR CARTAO — 2026-08-26, ordem do operador com o 2.mp4
    # na mao: *"ajusta a legenda do editor para ficar na mesma posicao que a dele,
    # e aparecer a mesma quantidade de palavras de forma que nao esta cobrindo
    # muito a tela"*.
    # ⭐ A FONTE FOI MEDIDA, nao olhada: frames a 720x1280, legenda em UMA linha,
    # sempre 3 palavras (`BEST DISCOVERY I`, `HORSE GELATIN HALF`, `HMM COMMENT
    # GELATIN`), 16 a 19 caracteres. O nosso saia com 4-5 palavras em DUAS linhas.
    # ⚠️ `max_chars=20` saiu de MEDICAO no render, nao de conta no papel: queimei
    # a legenda num frame 720x1280 e `BEST DISCOVERY I` (16 chars) ocupou 418px,
    # ou seja 26px por caixa alta. A caixa util com margin_lr 0.06 e' 634px -> 24
    # caracteres por linha. 20 deixa folga de 4 e cobre a faixa que a fonte usa
    # (16 a 19). Trinca mais longa que 20 vira cartao de 2 palavras, que e' o que
    # a fonte tambem faz (`MY MARRIAGE`).
    # ⛔ Nao subir de 22 sem re-medir: acima disso a linha quebra em duas e o
    # bloco dobra de altura, que e' exatamente o que este ajuste veio resolver.
    por_linha=3,
    max_chars=20,
    gap_quebra=0.6,
    maiuscula=True,
    cor_ativa="&H0000FFFF",    # amarelo (ABGR) — palavra ja falada/acesa
    cor_espera="&H00FFFFFF",   # branco — palavra por vir
    keywords=None,             # None = KEYWORDS_PADRAO
    cor_keyword="&H000049FF",  # vermelho-laranja vivo (ABGR de #FF4900)
    escala_keyword=1.4,        # fonte da keyword vs fonte normal
    # ⛔⛔ DESLIGADO EM 2026-08-13, ordem do operador: *"remova o comentario
    # fixado do veo editor cta fixo de comment gelatin"*. O video passa a sair
    # SO' com o karaoke da fala.
    # ⭐ E fica DESLIGADO, nao apagado: a maquinaria inteira do pin continua
    # aqui embaixo (estilo PIN, a busca da palavra depois de `Comment`, o
    # `pin_em`), porque ela custou uma licao cara — a versao antiga travava na
    # PRIMEIRA keyword falada, e as keywords tambem sao ingredientes da copy,
    # entao metade dos videos do CLEAN mandava comentar `honey` em vez de
    # `gelatin` e quebrava a automacao Comentario->DM. Apagar o codigo seria
    # jogar fora esse conserto junto.
    # ⚠️ Voltar e' UMA palavra: `pin_cta=True`.
    pin_cta=False,             # fixa "COMMENT <KEYWORD>" no topo apos o CTA falado
    # ⭐⭐ PALAVRA DO CTA ESCOLHIDA NO PAINEL (2026-08-26) — ordem do
    # operador: *"deixe um campo para mim conseguir escrever a palavra que
    # quero ficar no ultimo take para nao ter que ficar pedindo alteracao
    # toda hora"*. Vazio = usa a keyword detectada no audio (comportamento
    # antigo). Preenchido = e' ELA que aparece queimada, sempre.
    # ⛔ A palavra digitada TAMBEM entra na deteccao: o pin procura
    # `COMMENT <ela>` no audio, senao um `COMMENT yes` nunca seria achado
    # por quem so' conhece a lista fixa de keywords.
    cta_palavra=None,
    duracao_video=None,        # fim do pin (segundos). None = fim da ultima palavra
    pin_em=None,               # ⭐ CTA FIXO: segundo em que o pin ENTRA
    # ⭐⭐ A ALTURA DA LEGENDA VIRA PARAMETRO — 2026-08-26, ordem do
    # operador: *"crie um seletor com o tamanho 9:16 com uma regua para mim
    # selecionar a altura em que a legenda ira ficar (...) pois cada video a
    # legenda tem que ficar em uma altura diferente"*.
    # ⛔ Ate' aqui era a constante `0.60`, e o argumento dele desmonta a
    # ideia de constante: o numero certo depende de ONDE a cabeca e a prova
    # caem em CADA video, e isso muda de agente para agente. Valor fixo so'
    # pode estar certo para um lote.
    # ⚠️ Fracao da ALTURA, medida do TOPO (o alignment do karaoke e' 8).
    # 0.60 continua o padrao — e' a faixa medida na fonte do 2.mp4 (58%-63%).
    pos_legenda=0.60,
    # ⭐⭐ A CHAVE DA LEGENDA — mesma ordem: *"quero que haja uma chave para
    # quando eu quiser que seja possivel desligar a legenda, e fique somente
    # o CTA"*.
    # ⛔ NAO E' `palavras=[]`: a transcricao CONTINUA rodando, porque e' ela
    # que descobre QUANDO o CTA e' falado (`pin_em`). Desligar a transcricao
    # junto tiraria o pin de lugar — parecem a mesma coisa e nao sao.
    so_pin=False,
    # ⭐⭐ A ALTURA DO CTA, pelo mesmo motivo da legenda — 2026-08-26,
    # ordem do operador logo depois de aprovar o seletor: *"tambem quero
    # poder controlar a altura do CTA"*.
    # ⛔ Era a constante `0.47`, escolhida MEDINDO os frames do v001 do
    # Lamont — aos 40%% o pin caia em cima do rosto, e a faixa limpa era
    # 22%%-30%% naquele video. O numero estava certo PARA AQUELE lote, que
    # e' exatamente o argumento que derrubou a constante da legenda.
    # ⚠️ Fracao da ALTURA medida do TOPO, como a `pos_legenda`: o
    # alignment do PIN tambem e' 8.
    pos_cta=0.47,
    # ⭐⭐ O EFEITO "CIRCULADO + HERE" — 2026-08-28, ordem do operador com o
    # reel na mao: *"uma chave para ligar esse efeito de circulado vermelho
    # escrito Here"*, e *"a chave deve ativar em TODOS OS TAKES, e o local (...)
    # deve ser selecionavel ali no seletor das legendas"*.
    # ⭐ Por isso ele nasce em DOIS eixos (x e y) e nao em altura como a legenda
    # e o CTA: aqueles sao faixas de texto que ocupam a largura inteira, este e'
    # um ALVO — circula um objeto que pode estar em qualquer canto do quadro.
    # ⚠️ Fracao da largura / da altura. O padrao (0.806, 0.682) e' onde ele cai
    # no reel de referencia, medido em pixel.
    aqui_ligado=False,
    aqui_x=0.806,
    aqui_y=0.682,
    aqui_texto=AQUI_TEXTO,
    # ⭐ o pulso nasce LIGADO porque e' o que a fonte faz — ordem do
    # operador: *"a seta e o circulo devem ter o efeito de animacao igual
    # ao original"*. Fica como parametro para poder ser medido desligado.
    aqui_pulso=True,
    # ⭐⭐ ATE' QUE SEGUNDO O EFEITO VAI — 2026-08-28, ordem do operador:
    # *"tambem quero poder escolher por quantos takes o efeito ira durar"*.
    # ⛔ Chega em SEGUNDOS, nao em numero de takes, e de proposito: quem
    # sabe onde cada take caiu no video PRONTO e' o pipeline — ele cortou
    # o silencio e mudou a velocidade depois de juntar, entao somar as
    # duracoes cruas dos takes da' um instante que nao existe mais no
    # arquivo. Mesma razao do `pin_em`.
    # ⚠️ None = o video inteiro, que e' o padrao pedido antes
    # (*"a chave deve ativar em todos os takes"*).
    aqui_fim=None,
    # ⭐⭐ A LEGENDA FIXA (a caixa amarela) — 2026-08-29, ordem do operador com
    # o reel `1 (1).mp4` na mao: *"existe uma legenda fixa no take 1 (...) quero
    # escrever algo e posicionar onde ira ficar (...) e selecionar se sera
    # aplicada no take 1, 2, 3, 4... ou em todos"*.
    #
    # ⛔ NAO E' O KARAOKE COM OUTRO TEXTO. O karaoke nasce da transcricao e
    # acende palavra por palavra; esta e' uma placa que o operador escreve e que
    # fica PARADA durante um take inteiro. Sao mecanicas diferentes e por isso
    # sao estilos diferentes no `.ass`.
    #
    # ⭐ MEDIDO no reel, quadro a 1s (480x854):
    #     caixa amarela  x 20..459 (91% da largura)  y 68..195
    #     centro (0.499, 0.154)   cor #F0D000   texto PRETO, 3 linhas
    # ⚠️ O texto vem em UMA linha do painel e e' quebrado aqui em linhas de ate'
    # 24 caracteres — a linha mais larga da fonte ("THIS RECIPE CIRCULATING",
    # 23 chars) ocupa 91% da largura, entao 24 e' o limite que nao estoura.
    fixo_texto="",
    fixo_x=0.50,
    fixo_y=0.15,
    # ⚠️ Chegam em SEGUNDOS, pela mesma razao do `aqui_fim`: quem sabe onde cada
    # take caiu no video PRONTO e' o pipeline, que cortou silencio e mudou a
    # velocidade depois de juntar. None/None = o video inteiro.
    fixo_ini=None,
    fixo_fim=None,
    # ⭐⭐ AS DUAS CORES — 2026-08-29, ordem do operador logo depois de
    # pedir a legenda fixa: *"tambem quero poder controlar a cor da
    # legenda e do fundo dela"*.
    # ⚠️ Chegam em #RRGGBB (o formato do seletor de cor do tkinter) e sao
    # convertidas aqui. O ASS usa BGR invertido, entao passar o hex direto
    # sairia com vermelho e azul TROCADOS — e sem erro nenhum.
    # O padrao e' o do reel: texto preto sobre caixa amarela #F0D000.
    fixo_cor="#000000",
    fixo_fundo="#F0D000",
    # ⭐ TRANSPARENCIA DA CAIXA — 0 opaco (como sempre foi), 100 invisivel.
    # Nasce em 0 para nenhum video existente mudar de aparencia.
    fixo_alfa=0,
):
    """Gera um .ass karaoke. Agrupa palavras em linhas curtas (por_linha OU
    max_chars) e quebra tambem quando ha silencio > gap_quebra entre palavras.
    WrapStyle 0 garante que nada estoure a borda (quebra em 2 linhas se preciso)."""
    # ⭐⭐ AS DUAS LEGENDAS TROCARAM DE LUGAR EM 2026-08-13. Ordem do operador,
    # com o v001 do dia na mao: *"a legenda onde esta' fica tampando o item
    # principal, isso acontece com frequencia. Iremos resolver isso trocando de
    # lugar a legenda que fica no posicionamento de Comment gelatin no topo com
    # a legenda falada"*.
    #
    # ⛔ A RAZAO E' DE COMPOSICAO, e vale escrever: o objeto que prova o video
    # (a tigela, o copo, o prop) vive no TERCO INFERIOR do quadro em quase todo
    # agente do parque — e' onde as maos trabalham. O karaoke morava justamente
    # ali, a 20% do rodape, e tampava a prova em cima da hora. O pin do CTA e'
    # UMA linha curta e fixa; o karaoke sao duas linhas que mudam o tempo todo.
    # Quem tem de ceder o terco inferior e' o karaoke.
    #
    # ⭐ AGORA:  karaoke em CIMA (alignment 8, a 10% do topo)
    #            pin do CTA EMBAIXO (alignment 2, a 20% do rodape)
    # ⚠️ As margens trocaram JUNTO com os alignments — no ASS o MarginV e'
    # medido a partir da borda que o alignment escolhe. Trocar so' o alignment
    # poria o karaoke a 20% do TOPO, no meio do rosto.
    #
    # ⭐⭐ SEGUNDA PASSADA, no mesmo dia: o operador mandou um video de
    # referencia (`exemplo.mp4`) e disse *"quero que deixe como o do exemplo"*,
    # mais *"na hora de fixar o CTA comment gelatin a legenda fique mais no
    # centro da tela, em torno de 40% de altura (...) ou em algum lugar que
    # voce ache que ficara' um padrao bom para todos os videos"*.
    #
    # ⭐ O EXEMPLO FOI MEDIDO EM PIXEL, nao olhado: frame extraido a 720x1280,
    # bloco de texto de y=148 a y=265 (11,6% a 20,7%), DUAS linhas, altura de
    # caixa alta de 48px. Arial Black tem caixa alta ~0,716 em -> fonte 67px,
    # que da' 0.052 da altura. Dai' saem os tres numeros abaixo.
    #
    # ⛔⛔ E O PIN NAO FOI PARA OS 40%: os 40% foram TESTADOS, queimando o
    # texto nos frames reais do v002 em 23%, 29% e 40%. Aos 40% o pin cai em
    # cima do ROSTO nos dois frames — aos 3s e aos 12s. A faixa limpa nos dois
    # e' 22%-30%, porque a cabeca comeca por volta de 30% e a prova (a tigela)
    # vive no terco inferior.
    # ⭐ 29% e' o melhor ponto medido: livre do rosto, livre da tigela, e com
    # folga do karaoke (que termina por volta de 21%). O operador delegou a
    # escolha; esta e' a escolha, com a medicao junto.
    # ⭐ 14/08 — *"diminua o tamanho"*. Era 0.052 (o corpo do exemplo que ele
    # aprovou, medido em pixel no frame). Com UMA palavra por vez o bloco ja'
    # encolheu pela metade na altura; a fonte menor termina o servico.
    fonte_sz = max(24, int(altura * 0.045))
    fonte_pin = max(22, int(altura * 0.048))
    outline = max(3, int(round(altura * 0.007)))
    sombra = max(1, int(round(altura * 0.002)))
    # ⭐⭐ O KARAOKE DESCEU PARA 60% — 2026-08-26. Ordem do operador: a legenda
    # deve ficar *"na mesma posicao que a dele (...) na verdade a legenda pode
    # ficar ate um pouco mais pra baixo"*.
    # ⭐ MEDIDO na fonte (2.mp4, frames a 720x1280 com grade percentual queimada):
    # o bloco de legenda ocupa de 58% a 63% da altura. 0.60 poe o topo do nosso
    # bloco logo abaixo disso — o "um pouco mais pra baixo" que ele pediu.
    # ⚠️⚠️ ISTO REVERTE A TROCA DE 2026-08-13, e a razao daquela troca continua
    # de pe': a prova do video (tigela, copo, prop) vive no terco inferior, e foi
    # por tampar a prova que o karaoke subiu para o topo. O que mudou e' o
    # TAMANHO do bloco: com 3 palavras em UMA linha a 0.045 ele ocupa ~5,5% da
    # altura (60%-65,5%), contra ~10% das duas linhas de antes. Cabe na faixa que
    # a fonte usa sem cobrir a prova.
    # ⚠️ Se voltar a tampar, o numero a mexer e' este e so' este.
    # ⚠️ margin_lr caiu de 0.11 para 0.06 para a trinca caber em UMA linha — ver
    # a conta em max_chars.
    margin_lr = int(largura * 0.06)
    # ⭐ o 0.60 virou o PADRAO do parametro, nao mais um numero cravado aqui
    margin_topo = int(altura * pos_legenda)
    # ⭐⭐ O PIN DESCEU PARA 47% — 2026-08-26. Ordem do operador com o v001 do
    # Lamont na mao e um circulo vermelho desenhado no frame: *"ajuste a
    # legenda fixa do editor para ficar mais na parte central do video, para
    # nao tampar o rosto dos personagens"*.
    # ⭐ MEDIDO no frame que ele mandou, usando as duas legendas ja' na tela
    # como regua: o pin estava com o centro em 32% e o karaoke em 63%; o
    # circulo dele fica de 46% a 55%, centro em 50%. Com o bloco do pin
    # medindo 6,2% da altura (fonte 0.048 + contorno), o topo em 0.47 poe o
    # centro exatamente em 50%.
    # ⚠️ E a folga para o karaoke foi conferida, nao suposta: pin termina em
    # 53,1% e o karaoke comeca em 60% — 88px de respiro a 1280. Se algum dos
    # dois mudar de altura, e' esta conta que precisa ser refeita.
    # ⛔ Os 29% antigos vieram de outra medicao valida (a faixa limpa entre o
    # rosto e a tigela, testada em 23%, 29% e 40% em 13/08) — mas era com o
    # karaoke NO TOPO. Com o karaoke a 60%, a faixa livre mudou de lugar.
    # ⭐ o 0.47 virou o PADRAO do parametro, nao mais um numero cravado
    margin_pin = int(altura * pos_cta)
    # ⭐ o corpo e o contorno do "here" saem da MESMA regra do desenho
    # (escala pela largura), para o texto e o circulo nunca desandarem um
    # do outro quando o video for 1080x1920 em vez de 720x1280.
    # ⭐ o corpo da legenda fixa: 0.048 saiu de VARRER e medir o render
    # contra o reel, nao de conta no papel. A caixa amarela da fonte ocupa
    # 91% da largura com 3 linhas; medido a 480x854:
    #     0.040 -> 73%   0.046 -> 84%   0.048 -> 88%   0.050 -> 92%
    # ⚠️ 0.048 e nao 0.050 de proposito: 0.050 casa a largura exata do reel
    # NAQUELE texto, mas a quebra permite linhas de ate' 24 caracteres — uma
    # linha cheia a 0.050 encostaria na borda. 88% deixa a folga.
    fonte_fixo = max(20, int(round(altura * 0.048)))
    # o Outline no BorderStyle 3 e' o PADDING da caixa, nao um contorno
    pad_fixo = max(3, int(round(altura * 0.006)))
    cor_fixo_txt = _ass_cor(fixo_cor, "&H00000000")
    cor_fixo_box = _ass_cor_alfa(fixo_fundo, fixo_alfa, "&H0000D0F0")

    # ⭐⭐ SEM CAIXA VIRA CONTORNO, NAO "CAIXA INVISIVEL" — 2026-08-31.
    # ⛔ O defeito: BorderStyle 3 so' sabe desenhar CAIXA. Zerando so' o alfa,
    # o texto ficava sem caixa E SEM CONTORNO — ilegivel sobre video claro,
    # que foi exatamente o que o operador viu no primeiro render.
    # A fonte que ele quer copiar nao tem caixa nenhuma: e' texto com
    # contorno, o BorderStyle 1. Entao a opcao extrema troca de modo em vez
    # de so' apagar a caixa.
    # ⚠️ O contorno e' SEMPRE preto e opaco: e' ele que faz o texto sobreviver
    # a qualquer fundo. Herdar a cor da caixa aqui daria contorno amarelo.
    try:
        _alfa_n = float(fixo_alfa)
    except (TypeError, ValueError):
        _alfa_n = 0.0
    if _alfa_n >= 100:
        borda_fixo = 1                       # contorno + sombra
        esp_fixo = max(3, int(round(altura * 0.004)))
        cor_fixo_box = "&H00000000"          # preto opaco
    else:
        borda_fixo = 3                       # caixa opaca (o de sempre)
        esp_fixo = pad_fixo
    _aq_u = largura / _AQ_REF_W
    fonte_aqui = max(10, int(round(_AQ_TX_FONTE * _aq_u)))
    bord_aqui = max(2, int(round(5.0 * _aq_u)))

    # tira tokens que sao SO pontuacao (o whisper emite "," sozinho as vezes) —
    # eram eles que apareciam como virgula solta no comeco da linha.
    palavras = [w for w in palavras if _limpa(w["text"], maiuscula)]

    # --- agrupa em linhas ---
    linhas, grupo, chars = [], [], 0
    for w in palavras:
        limpo = _limpa(w["text"], maiuscula)
        if grupo:
            gap = w["start"] - grupo[-1]["end"]
            if (len(grupo) >= por_linha or gap > gap_quebra
                    or chars + 1 + len(limpo) > max_chars):
                linhas.append(grupo)
                grupo, chars = [], 0
        grupo.append(w)
        chars += (1 if chars else 0) + len(limpo)
    if grupo:
        linhas.append(grupo)

    header = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {largura}
PlayResY: {altura}
WrapStyle: 0
ScaledBorderAndShadow: yes
YCbCr Matrix: TV.709

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: CC,Arial Black,{fonte_sz},{cor_ativa},{cor_espera},&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,{outline},{sombra},8,{margin_lr},{margin_lr},{margin_topo},1
Style: PIN,Arial Black,{fonte_pin},&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,{outline},{sombra},8,{margin_lr},{margin_lr},{margin_pin},1
Style: AQUI,Arial Black,{fonte_aqui},&H001414FF,&H001414FF,&H00FFFFFF,&H00000000,-1,0,0,0,100,100,0,0,1,{bord_aqui},0,5,0,0,0,1
Style: FIXO,Arial Black,{fonte_fixo},{cor_fixo_txt},{cor_fixo_txt},{cor_fixo_box},{cor_fixo_box},-1,0,0,0,100,100,0,0,{borda_fixo},{esp_fixo},0,5,0,0,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

    kw = {k.strip().upper() for k in (keywords or KEYWORDS_PADRAO) if k.strip()}
    fs_kw = int(fonte_sz * escala_keyword)

    # ⭐⭐ ESTICA ATE' A PROXIMA — 2026-08-14, junto com o modo de UMA PALAVRA.
    # ⛔ Sem isto a tela PISCA: a palavra some no fim do audio dela e a proxima
    # so' entra quando comeca a ser falada. Com blocos de 4-5 palavras o buraco
    # era imperceptivel (um por frase); com uma palavra por vez sao 45 buracos
    # em 15 segundos. Medido no v002 de 14/08: mediana de 259 ms entre inicios
    # de palavra, e a palavra em si dura menos que isso.
    # ⚠️ E' ESTICAR, nao adiantar: o inicio continua no audio. O que muda e' o
    # FIM, que vai ate' a proxima palavra entrar — a legenda deixa de ter
    # buraco sem nunca aparecer antes do som.
    # ⛔ E o `gap_quebra` continua mandando: silencio longo (fim de frase, corte
    # entre takes) NAO e' esticado — la' a tela limpa de proposito.
    eventos = []
    # ⭐⭐ O CIRCULADO + "HERE" ENTRA PRIMEIRO, e a ordem e' a decisao.
    # ⛔ Ele fica na LAYER 0, a mesma do karaoke, e ANTES dele na lista: no ASS,
    # dentro da mesma layer quem vem depois desenha por cima. Assim, se o
    # operador arrastar o alvo para cima da faixa da legenda, quem fica legivel
    # e' a LEGENDA — texto tapado por um circulo vermelho e' defeito, circulo
    # cruzado por texto e' so' sobreposicao. (Medido: com os dois no mesmo
    # lugar, a palavra sai inteira por cima do circulo.)
    # ⚠️ E vai de 0 ate' o fim: *"a chave deve ativar em todos os takes"*. Nao
    # ha' deteccao de take nenhuma aqui — e' o video inteiro, de proposito.
    if aqui_ligado:
        _fim_aq = (aqui_fim or duracao_video
                   or (palavras[-1]["end"] + 0.5 if palavras else 0))
        # ⚠️ o pulso acompanha: os `\t` sao gerados so' ate' `_fim_aq`, entao
        # limitar o efeito a 2 takes tambem para de gerar tag depois disso.
        if _fim_aq > 0:
            _b = chr(92)          # ⛔ a barra vem daqui, nunca de literal
            _aq = _aq_desenho(largura, altura, aqui_x, aqui_y)
            _t0, _t1 = _ass_time(0), _ass_time(_fim_aq)
            # 1) a ELIPSE, com o pulso. Coordenada relativa ao centro + an7:
            #    e' isso que faz o `\fscx` escalar em volta do centro.
            eventos.append(
                "Dialogue: 0,%s,%s,AQUI,,0,0,0,,"
                "{%san7%spos(%d,%d)%sbord0%sshad0%s%sp1}%s{%sp0}"
                % (_t0, _t1, _b, _b, round(_aq["centro"][0]),
                   round(_aq["centro"][1]), _b, _b,
                   _aq_pulso(_fim_aq, _b) if aqui_pulso else "", _b,
                   _aq["elipse"], _b)
            )
            # 2) a SETA, esticando para dentro do circulo. A origem do
            #    desenho e' a CAUDA, entao a escala empurra a PONTA para o alvo.
            eventos.append(
                "Dialogue: 0,%s,%s,AQUI,,0,0,0,,"
                "{%san7%spos(%d,%d)%sbord0%sshad0%s%sp1}%s{%sp0}"
                % (_t0, _t1, _b, _b, round(_aq["cauda"][0]),
                   round(_aq["cauda"][1]), _b, _b,
                   _aq_pulso(_fim_aq, _b, _AQ_SETA_AMP) if aqui_pulso else "",
                   _b, _aq["seta"], _b)
            )
            # 3) o "here", parado — medido em 117x42 nos 60 quadros da fonte.
            eventos.append(
                "Dialogue: 0,%s,%s,AQUI,,0,0,0,,"
                "{%san5%spos(%d,%d)%sfrz%d%sfscy%d}%s"
                % (_t0, _t1, _b, _b, round(_aq["texto"][0]),
                   round(_aq["texto"][1]), _b, _AQ_TX_GIRO, _b, _AQ_TX_FSCY,
                   aqui_texto)
            )

    for _i, grupo in enumerate(linhas):
        ini = grupo[0]["start"]
        fim = grupo[-1]["end"]
        if _i + 1 < len(linhas):
            _prox = linhas[_i + 1][0]["start"]
            if _prox - fim <= gap_quebra:
                fim = _prox
        partes = []
        for j, w in enumerate(grupo):
            texto = _limpa(w["text"], maiuscula)
            # duracao do \k = ate a proxima palavra comecar (inclui o gap curto);
            # a ultima usa a propria duracao.
            if j < len(grupo) - 1:
                dur = _cs(grupo[j + 1]["start"] - w["start"])
            else:
                dur = _cs(w["end"] - w["start"])
            eh_keyword = texto.strip(".,!?;:").upper() in kw
            if eh_keyword:
                # keyword em cor propria (antes E depois do sweep) + fonte maior;
                # na sequencia restaura fonte e as cores do karaoke normal
                partes.append(
                    f"{{\\kf{dur}\\fs{fs_kw}\\1c{cor_keyword}\\2c{cor_keyword}}}"
                    f"{texto}"
                    f"{{\\fs{fonte_sz}\\1c{cor_ativa}\\2c{cor_espera}}} "
                )
            else:
                partes.append(f"{{\\kf{dur}}}{texto} ")
        txt = "".join(partes).strip()
        # \u26d4 COM A CHAVE DESLIGADA O KARAOKE NAO E' EMITIDO, e so' ele: o pin
        # do CTA la' embaixo continua saindo normalmente. E' o que ele pediu \u2014
        # *"fique somente o CTA mesmo no 3 take"*.
        if not so_pin:
            eventos.append(
                f"Dialogue: 0,{_ass_time(ini)},{_ass_time(fim)},CC,,0,0,0,,{txt}"
            )

    # --- pin do CTA: "COMMENT <KEYWORD>" fixo no topo ate o fim do video ---
    # o texto fica queimado na porcao superior dali em diante, com a keyword
    # na cor de destaque. Layer 1 = desenha por cima do karaoke sem colidir
    # (alignments diferentes: karaoke NO TOPO, pin NO RODAPE — trocados em
    # 2026-08-13, ver o bloco das margens la' em cima).
    #
    # ⛔⛔ O PIN SEGUE A PALAVRA DEPOIS DE "COMMENT", NAO A PRIMEIRA KEYWORD DO
    # VIDEO (2026-08-03). A versao antiga parava na primeira palavra-gatilho
    # falada, e as keywords tambem sao INGREDIENTES da copy: o CLEAN diz
    # `Kale and honey make your milk sweet` na cena 2, muito antes do
    # `Comment gelatin` da cena 3. O pin travava em "COMMENT HONEY" e ficava
    # queimado ate o fim.
    # Medido: 49% dos sorteios do CLEAN falam `honey` antes de `gelatin` — ou
    # seja, metade dos videos saia mandando comentar a palavra errada, o que
    # quebra a automacao Comentario->DM inteira (a keyword cadastrada e'
    # GELATIN). O operador viu 2 errados em 3 videos.
    if pin_cta and palavras:
        kw_falada = None
        t_pin = None
        escolhida = (cta_palavra or "").strip().upper()
        alvos = set(kw) | ({escolhida} if escolhida else set())
        toks = [(_limpa(w["text"], True).strip(".,!?;:").upper(), w)
                for w in palavras]
        # 1) o caso certo: a keyword vem logo depois de "comment"
        for i, (tok, _w) in enumerate(toks):
            if tok == "COMMENT" and i + 1 < len(toks) and toks[i + 1][0] in alvos:
                kw_falada = toks[i + 1][0]
                t_pin = toks[i + 1][1]["end"]
                break
        # 2) sem "comment <keyword>" no audio: cai para a ULTIMA keyword falada.
        #    ⚠️ ULTIMA, nao primeira — o CTA mora no fim do video, e ingrediente
        #    citado no meio da receita nunca e' o que o espectador deve comentar.
        #
        # ⛔⛔ ESTE FALLBACK SO' ESCOLHE A PALAVRA, NUNCA O TEMPO (2026-08-26).
        # Ele cravava `t_pin` tambem, e isso quebrou os tres casos medidos no dia
        # em que o pin foi religado: com o campo em `recipe` e o audio dizendo
        # `comment yes`, a busca do passo 1 falha, este passo acha o `gelatin`
        # da CENA 2 e o pin entrava aos 3,7s — no meio da receita, seis segundos
        # antes do CTA. Pior: com `t_pin` preenchido, a queda para o comeco do
        # ultimo take nunca acontecia.
        # ⭐ Palavra e tempo sao decisoes SEPARADAS: o tempo so' pode vir do
        # `comment` falado ou do `pin_em`; um ingrediente no meio da receita nao
        # tem opiniao sobre quando o CTA comeca.
        if kw_falada is None:
            for tok, w in reversed(toks):
                if tok in kw:
                    kw_falada = tok
                    break
        # ⭐⭐ CTA FIXO (2026-08-08) — o pin ENTRA NO COMECO DO TAKE 2 e fica
        # ate' o fim, em vez de esperar o CTA ser falado.
        # Ordem do operador: *"a legenda Comment Gelatin apareca fixa ... no
        # inicio do segundo take e fique ate' o final"*.
        #
        # ⛔ POR QUE NAO E' SO' `t_pin = 8.0`: o pipeline CORTA O SILENCIO e
        # muda a VELOCIDADE depois de juntar os takes, entao o segundo take nao
        # cai mais nos 8s originais — nos videos dele, takes de 24s viraram 16s
        # de video final. Quem sabe a proporcao e' o pipeline, e e' ele que
        # passa `pin_em` ja' na escala do video PRONTO.
        #
        # ⚠️ E o alvo e' ENCAIXADO na primeira palavra que comeca dali em
        # diante: entrar no meio de uma palavra do take 1 poria o CTA na tela
        # antes de a cena virar. Sem palavra depois do alvo, usa-se o alvo.
        # ⭐⭐ 2026-08-26 — A ENTRADA INVERTEU DE PRIORIDADE. Ordem do operador:
        # *"ou ao inves de fixar no ultimo take inteiro, faca reconhecer o
        # momento do CTA se for possivel"*.
        # ⭐ Agora: se o audio TEM `comment <palavra>`, o pin entra ali — e' o
        # frame exato, medido na fala. So' quando nao ha' `comment` no audio e'
        # que ele cai para `pin_em`, o comeco do ULTIMO take, que e' a
        # aproximacao proporcional que o pipeline calcula.
        # ⚠️ Antes era o contrario (o `pin_em` mandava sempre), porque o modo
        # existia para o pin entrar ANTES do CTA. Hoje o pedido e' o oposto.
        if t_pin is None and pin_em is not None:
            t_pin = pin_em
            for w in palavras:
                if w["start"] >= pin_em:
                    t_pin = w["start"]
                    break
        # ⛔ A palavra QUEIMADA e' sempre a escolhida no painel quando existe.
        # A deteccao acima serve para o TEMPO; ela nao decide o texto, senao um
        # ingrediente falado no meio da receita voltaria a mandar comentar a
        # palavra errada e quebrar a automacao Comentario->DM.
        palavra_pin = escolhida or kw_falada or "GELATIN"
        if t_pin is not None:
            kw_falada = palavra_pin
            fim_video = duracao_video if duracao_video else palavras[-1]["end"] + 0.5
            if fim_video > t_pin:
                txt_pin = (
                    f"COMMENT {{\\1c{cor_keyword}}}{kw_falada}{{\\1c&H00FFFFFF&}}"
                )
                eventos.append(
                    f"Dialogue: 1,{_ass_time(t_pin)},{_ass_time(fim_video)},"
                    f"PIN,,0,0,0,,{txt_pin}"
                )

    # ⭐⭐ A LEGENDA FIXA (caixa amarela) — 2026-08-29.
    # ⛔ LAYER 3, acima de tudo: e' a placa que o operador escreveu de proposito.
    # Karaoke tapando a fala do sistema e' aceitavel; karaoke tapando a frase que
    # ele digitou nao e'.
    # ⚠️ Sai antes do `return` para poder usar `duracao_video` ja' resolvido.
    _fx = (fixo_texto or "").strip()
    if _fx:
        _b3 = chr(92)
        _ini = 0.0 if fixo_ini is None else float(fixo_ini)
        _fim = (duracao_video or (palavras[-1]["end"] + 0.5 if palavras else 0)
                ) if fixo_fim is None else float(fixo_fim)
        if _fim > _ini:
            # quebra em linhas de ate' 24 caracteres, sem cortar palavra
            _lin, _cur = [], ""
            for _p in _fx.split():
                if _cur and len(_cur) + 1 + len(_p) > 24:
                    _lin.append(_cur); _cur = _p
                else:
                    _cur = (_cur + " " + _p).strip()
            if _cur:
                _lin.append(_cur)
            _txt3 = (_b3 + "N").join(_lin)
            # ⛔ chaves e barras viram texto inofensivo: o operador digita livre
            # e uma chave solta comeria o resto da linha como tag do ASS.
            _txt3 = _txt3.replace("{", "(").replace("}", ")")
            eventos.append(
                "Dialogue: 3,%s,%s,FIXO,,0,0,0,,{%san5%spos(%d,%d)}%s"
                % (_ass_time(_ini), _ass_time(_fim), _b3, _b3,
                   round(fixo_x * largura), round(fixo_y * altura), _txt3)
            )

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(header + "\n".join(eventos) + "\n")
    return out_path
