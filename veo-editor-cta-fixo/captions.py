"""Transcricao (faster-whisper, offline) + geracao de legenda ASS estilo CapCut
word-by-word (karaoke fill: a palavra falada acende, o resto da linha fica em
espera). Timestamps por palavra vem do Whisper."""

import re

from faster_whisper import WhisperModel

_MODELO = {}  # cache por tamanho, pra nao recarregar a cada video


def transcrever(audio_path, model_size="base.en", language="en"):
    """Retorna lista de {text, start, end} por palavra."""
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


def _limpa(texto, maiuscula):
    # tira pontuacao/virgula solta no comeco (whisper as vezes destaca ela);
    # mantem a do fim. Neutraliza chaves que quebrariam o ASS.
    texto = re.sub(r"^[\s,.;:!?\-]+", "", texto.strip())
    texto = texto.replace("{", "(").replace("}", ")").replace("\\", "")
    return texto.upper() if maiuscula else texto


# palavras-gatilho do CTA ("comment GELATIN"): ganham cor propria e fonte maior
# para o espectador assimilar de cara o que digitar nos comentarios
KEYWORDS_PADRAO = ("HONEY", "GELATIN", "VICK", "VICKS", "RECIPE")


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
    por_linha=5,
    max_chars=22,
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
    duracao_video=None,        # fim do pin (segundos). None = fim da ultima palavra
    pin_em=None,               # ⭐ CTA FIXO: segundo em que o pin ENTRA
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
    margin_lr = int(largura * 0.11)
    margin_topo = int(altura * 0.11)   # karaoke: onde o exemplo poe o bloco
    margin_pin = int(altura * 0.29)    # pin: a faixa limpa medida nos frames

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
        toks = [(_limpa(w["text"], True).strip(".,!?;:").upper(), w)
                for w in palavras]
        # 1) o caso certo: a keyword vem logo depois de "comment"
        for i, (tok, _w) in enumerate(toks):
            if tok == "COMMENT" and i + 1 < len(toks) and toks[i + 1][0] in kw:
                kw_falada = toks[i + 1][0]
                t_pin = toks[i + 1][1]["end"]
                break
        # 2) sem "comment <keyword>" no audio: cai para a ULTIMA keyword falada.
        #    ⚠️ ULTIMA, nao primeira — o CTA mora no fim do video, e ingrediente
        #    citado no meio da receita nunca e' o que o espectador deve comentar.
        if kw_falada is None:
            for tok, w in reversed(toks):
                if tok in kw:
                    kw_falada = tok
                    t_pin = w["end"]
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
        if pin_em is not None:
            t_pin = pin_em
            for w in palavras:
                if w["start"] >= pin_em:
                    t_pin = w["start"]
                    break
            # ⛔ o pin fixo NAO depende de a keyword ter sido falada ainda —
            # ele entra antes do CTA de proposito. Sem keyword detectada, usa
            # a da automacao.
            if kw_falada is None:
                kw_falada = "GELATIN"
        if kw_falada is not None:
            fim_video = duracao_video if duracao_video else palavras[-1]["end"] + 0.5
            if fim_video > t_pin:
                txt_pin = (
                    f"COMMENT {{\\1c{cor_keyword}}}{kw_falada}{{\\1c&H00FFFFFF&}}"
                )
                eventos.append(
                    f"Dialogue: 1,{_ass_time(t_pin)},{_ass_time(fim_video)},"
                    f"PIN,,0,0,0,,{txt_pin}"
                )

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(header + "\n".join(eventos) + "\n")
    return out_path
