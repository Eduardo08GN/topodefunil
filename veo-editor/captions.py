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


def gerar_ass(
    palavras,
    largura,
    altura,
    out_path,
    por_linha=4,
    max_chars=15,
    gap_quebra=0.6,
    maiuscula=True,
    cor_ativa="&H0000FFFF",   # amarelo (ABGR) — palavra ja falada/acesa
    cor_espera="&H00FFFFFF",  # branco — palavra por vir
):
    """Gera um .ass karaoke. Agrupa palavras em linhas curtas (por_linha OU
    max_chars) e quebra tambem quando ha silencio > gap_quebra entre palavras.
    WrapStyle 0 garante que nada estoure a borda (quebra em 2 linhas se preciso)."""
    fonte_sz = max(24, int(altura * 0.058))
    outline = max(3, int(round(altura * 0.007)))
    sombra = max(1, int(round(altura * 0.002)))
    margin_v = int(altura * 0.20)  # sobe a legenda pro terco inferior/centro-baixo
    margin_lr = int(largura * 0.11)

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

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

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
            partes.append(f"{{\\kf{dur}}}{texto} ")
        txt = "".join(partes).strip()
        eventos.append(
            f"Dialogue: 0,{_ass_time(ini)},{_ass_time(fim)},CC,,0,0,0,,{txt}"
        )

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(header + "\n".join(eventos) + "\n")
    return out_path
