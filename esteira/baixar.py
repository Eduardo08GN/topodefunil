# -*- coding: utf-8 -*-
"""ESTEIRA · ETAPA 0 — a URL vira arquivo local. ZERO TOKEN.

⛔⛔ SOBRE COOKIES, E ESTA REGRA NAO SE NEGOCIA: **o operador nunca cola cookie
em lugar nenhum.** Ele escolhe o NAVEGADOR (e o yt-dlp le' a sessao dele
direto, no disco dele) ou aponta um arquivo `cookies.txt` que ele mesmo
exportou. O valor do cookie nao passa por chat, nao vai para log, nao entra em
commit e nao e' visto por mim.
⚠️ Isso ja' quase aconteceu: em 2026-08-16 ele colou os cookies de sessao do
Facebook numa conversa. Cookie colado e' credencial vazada — a unica saida
depois e' trocar a senha, que e' o que foi recomendado na hora. Esta etapa
existe para que o caminho FACIL seja tambem o seguro.

⭐ E o `yt_dlp` entra como BIBLIOTECA, nao como `.exe` chamado por fora: assim
ele viaja dentro do nosso executavel e o operador nao precisa instalar nada.
"""
import os
import re

PASTA = "_baixados"


def _erro_legivel(msg):
    """Traduz o erro do yt-dlp para o que o operador tem de FAZER.

    ⛔ `ERROR: [facebook] Cannot parse data` nao diz nada a quem so' quer o
    video. Cada linha aqui e' um erro real que a familia Meta devolve, com a
    acao do lado.
    """
    m = (msg or "").lower()
    if "login" in m or "cookies" in m or "rate-limit" in m or "sign in" in m:
        return ("essa pagina exige sessao logada. Escolha o navegador em "
                "COOKIES (o yt-dlp le' a sua sessao no disco) ou aponte um "
                "cookies.txt exportado.")
    if "dpapi" in m or "could not copy" in m or "failed to decrypt" in m:
        return ("o Windows nao deixou ler os cookies do navegador com ele "
                "ABERTO. Feche o navegador e tente de novo, ou use um "
                "cookies.txt exportado.")
    if "unsupported url" in m or "no video" in m:
        return "essa URL nao tem video que o yt-dlp reconheca."
    if "private" in m or "not available" in m or "removed" in m:
        return "o video esta' privado, removido ou bloqueado na sua regiao."
    if "http error 429" in m or "too many" in m:
        return "a plataforma limitou o ritmo. Espere alguns minutos."
    return msg


def opcoes_cookie(modo, valor):
    """`modo` e' 'nao', 'navegador' ou 'arquivo'."""
    if modo == "navegador" and valor:
        # ⚠️ a tupla e' (navegador, perfil, keyring, container) — so' o
        # primeiro campo interessa, o resto fica no padrao do yt-dlp.
        return {"cookiesfrombrowser": (valor.lower(), None, None, None)}
    if modo == "arquivo" and valor:
        if not os.path.exists(valor):
            raise ValueError("nao achei o arquivo de cookies: %s" % valor)
        return {"cookiefile": valor}
    return {}


def baixar(url, destino, modo_cookie="nao", valor_cookie="", progresso=None):
    """Baixa e devolve o caminho do arquivo. Levanta `RuntimeError` legivel."""
    import yt_dlp

    if not re.match(r"^https?://", url.strip(), re.I):
        raise RuntimeError("isso nao parece uma URL")
    os.makedirs(destino, exist_ok=True)
    achado = {}

    def _hook(d):
        if d.get("status") == "downloading" and progresso:
            tot = d.get("total_bytes") or d.get("total_bytes_estimate") or 0
            got = d.get("downloaded_bytes") or 0
            progresso("baixando… %s" % (("%d%%" % (100 * got // tot))
                                        if tot else "%d KB" % (got // 1024)))
        elif d.get("status") == "finished":
            achado["arquivo"] = d.get("filename")
            if progresso:
                progresso("baixado, juntando faixas…")

    opts = {
        # ⛔ o nome do arquivo sai do ID da plataforma, nao do TITULO: titulo
        # traz emoji, barra e acento, e o slug da etapa 1 ja' sofreu com isso.
        "outtmpl": os.path.join(destino, "%(extractor)s-%(id)s.%(ext)s"),
        # ⭐ mp4 de preferencia: e' o que o ffmpeg e o Veo digerem sem conversa.
        "format": "bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]/bv*+ba/b",
        "merge_output_format": "mp4",
        "quiet": True, "no_warnings": True, "noprogress": True,
        "progress_hooks": [_hook], "retries": 3, "fragment_retries": 3,
        "concurrent_fragment_downloads": 4,
    }
    try:
        opts.update(opcoes_cookie(modo_cookie, valor_cookie))
    except ValueError as e:
        raise RuntimeError(str(e))

    try:
        with yt_dlp.YoutubeDL(opts) as y:
            info = y.extract_info(url, download=True)
    except Exception as e:  # noqa: BLE001
        raise RuntimeError(_erro_legivel(str(e)))

    p = achado.get("arquivo")
    if p and os.path.exists(p):
        # ⚠️ quando ha' merge, o hook devolve o arquivo da FAIXA e o final e'
        # o `.mp4`. Preferir o mp4 irmao quando ele existir.
        base = os.path.splitext(p)[0]
        if os.path.exists(base + ".mp4"):
            return base + ".mp4"
        return p
    try:
        cand = yt_dlp.YoutubeDL(opts).prepare_filename(info)
        base = os.path.splitext(cand)[0]
        for ext in (".mp4", ".mkv", ".webm"):
            if os.path.exists(base + ext):
                return base + ext
    except Exception:  # noqa: BLE001
        pass
    raise RuntimeError("o download terminou mas eu nao achei o arquivo")
