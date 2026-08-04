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
    por_linha=4,
    max_chars=15,
    gap_quebra=0.6,
    maiuscula=True,
    cor_ativa="&H0000FFFF",    # amarelo (ABGR) — palavra ja falada/acesa
    cor_espera="&H00FFFFFF",   # branco — palavra por vir
    keywords=None,             # None = KEYWORDS_PADRAO
    cor_keyword="&H000049FF",  # vermelho-laranja vivo (ABGR de #FF4900)
    escala_keyword=1.4,        # fonte da keyword vs fonte normal
    pin_cta=True,              # fixa "COMMENT <KEYWORD>" no topo apos o CTA falado
    duracao_video=None,        # fim do pin (segundos). None = fim da ultima palavra
):
    """Gera um .ass karaoke. Agrupa palavras em linhas curtas (por_linha OU
    max_chars) e quebra tambem quando ha silencio > gap_quebra entre palavras.
    WrapStyle 0 garante que nada estoure a borda (quebra em 2 linhas se preciso)."""
    fonte_sz = max(24, int(altura * 0.058))
    outline = max(3, int(round(altura * 0.007)))
    sombra = max(1, int(round(altura * 0.002)))
    margin_v = int(altura * 0.20)  # sobe a legenda pro terco inferior/centro-baixo
    margin_lr = int(largura * 0.11)
    fonte_pin = max(22, int(altura * 0.048))   # pin do topo: um pouco menor que o karaoke
    margin_pin = int(altura * 0.10)            # distancia do topo (fora da zona de UI do FB)

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
Style: CC,Arial Black,{fonte_sz},{cor_ativa},{cor_espera},&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,{outline},{sombra},2,{margin_lr},{margin_lr},{margin_v},1
Style: PIN,Arial Black,{fonte_pin},&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,{outline},{sombra},8,{margin_lr},{margin_lr},{margin_pin},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

    kw = {k.strip().upper() for k in (keywords or KEYWORDS_PADRAO) if k.strip()}
    fs_kw = int(fonte_sz * escala_keyword)

    eventos = []
    for grupo in linhas:
        ini = grupo[0]["start"]
        fim = grupo[-1]["end"]
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
    # (alignments diferentes: karaoke embaixo, pin no topo).
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
