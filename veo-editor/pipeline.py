"""Motor de edicao: junta os takes -> tira silencio -> transcreve -> queima
legenda CapCut. Roda 100% offline (FFmpeg + auto-editor + faster-whisper).

Modelo de pasta:
  - Se a pasta de ENTRADA tem subpastas, cada subpasta = 1 video (seus arquivos
    de video, em ordem de nome, sao os takes).
  - Se a pasta de ENTRADA tem arquivos de video soltos, eles sao os takes de UM
    unico video.
O resultado vai pra pasta de SAIDA como <nome>.mp4.
"""

import os
import re
import sys
import json
import shutil
import zipfile
import tempfile
import subprocess

from captions import transcrever, gerar_ass

FFMPEG = shutil.which("ffmpeg") or "ffmpeg"
FFPROBE = shutil.which("ffprobe") or "ffprobe"
VIDEO_EXT = (".mp4", ".mov", ".mkv", ".webm", ".m4v", ".avi")


def _auto_editor():
    """Prefere o auto-editor do proprio ambiente (venv) e so depois o do PATH.
    Sem isso, rodando pelo venv o subprocess acharia a versao global (ou nada)."""
    base = os.path.dirname(os.path.abspath(sys.executable))
    for pasta in (base, os.path.join(base, "Scripts"), os.path.join(base, "bin")):
        for nome in ("auto-editor.exe", "auto-editor"):
            caminho = os.path.join(pasta, nome)
            if os.path.isfile(caminho):
                return caminho
    return shutil.which("auto-editor") or "auto-editor"


AUTO_EDITOR = _auto_editor()


def _run(cmd, cwd=None):
    p = subprocess.run(cmd, capture_output=True, text=True, cwd=cwd,
                       encoding="utf-8", errors="replace")
    if p.returncode != 0:
        raise RuntimeError(
            f"comando falhou ({cmd[0]}):\n{(p.stderr or p.stdout)[-1800:]}"
        )
    return p


def _natural(nome):
    # ordena take2 antes de take10
    return [int(x) if x.isdigit() else x.lower() for x in re.split(r"(\d+)", nome)]


def dims(path):
    p = _run([FFPROBE, "-v", "error", "-select_streams", "v:0",
              "-show_entries", "stream=width,height", "-of", "json", path])
    st = json.loads(p.stdout)["streams"][0]
    return int(st["width"]), int(st["height"])


def coletar_takes(pasta):
    arqs = [a for a in os.listdir(pasta)
            if a.lower().endswith(VIDEO_EXT) and os.path.isfile(os.path.join(pasta, a))]
    arqs.sort(key=_natural)
    return [os.path.join(pasta, a) for a in arqs]


def contar_zips(pasta):
    return [a for a in sorted(os.listdir(pasta), key=_natural)
            if a.lower().endswith(".zip") and os.path.isfile(os.path.join(pasta, a))]


def extrair_zips(entrada, log=print):
    """Extrai os .zip soltos na pasta de entrada (o pacote que o Flow baixa).
    Cada zip vira uma subpasta com o nome do arquivo = 1 video.
    So extrai video, achatando a estrutura interna (o basename tambem elimina
    qualquer path traversal do zip). Retorna as pastas criadas."""
    criadas = []
    for z in contar_zips(entrada):
        zpath = os.path.join(entrada, z)
        destino = os.path.join(entrada, os.path.splitext(z)[0])
        if os.path.isdir(destino) and coletar_takes(destino):
            log(f"  zip ja extraido, reaproveitando: {z}")
            criadas.append(destino)
            continue
        os.makedirs(destino, exist_ok=True)
        log(f"  extraindo {z}...")
        with zipfile.ZipFile(zpath) as zf:
            for membro in zf.infolist():
                if membro.is_dir():
                    continue
                nome = os.path.basename(membro.filename)
                if not nome or not nome.lower().endswith(VIDEO_EXT):
                    continue
                with zf.open(membro) as src, open(os.path.join(destino, nome), "wb") as dst:
                    shutil.copyfileobj(src, dst)
        n = len(coletar_takes(destino))
        if not n:
            log(f"  AVISO: {z} nao tinha video dentro, ignorando")
            shutil.rmtree(destino, ignore_errors=True)
            continue
        log(f"  {n} take(s) -> {os.path.basename(destino)}/")
        criadas.append(destino)
    return criadas


def duracao(path):
    p = _run([FFPROBE, "-v", "error", "-show_entries", "format=duration",
              "-of", "json", path])
    try:
        return float(json.loads(p.stdout)["format"]["duration"])
    except (KeyError, ValueError, TypeError):
        return 0.0


def concat(takes, out, cortes=None):
    """Junta na ordem, re-encodando uniforme (aguenta params diferentes do Veo).

    cortes: {caminho_do_take: [inicio, fim]} em segundos. fim None ou 0 = ate o
    final. O corte entra como filtro trim (preciso no frame) em vez de -ss, que
    com seek rapido erraria o ponto."""
    cortes = cortes or {}
    if len(takes) == 1 and not cortes.get(takes[0]):
        shutil.copy(takes[0], out)
        return out

    inputs = []
    for t in takes:
        inputs += ["-i", t]

    partes, rotulos = [], ""
    for i, t in enumerate(takes):
        corte = cortes.get(t)
        if corte:
            ini = max(0.0, float(corte[0] or 0))
            fim = float(corte[1]) if len(corte) > 1 and corte[1] else None
            tv = f"trim=start={ini:.3f}" + (f":end={fim:.3f}" if fim else "")
            ta = f"atrim=start={ini:.3f}" + (f":end={fim:.3f}" if fim else "")
            partes.append(f"[{i}:v:0]{tv},setpts=PTS-STARTPTS[v{i}]")
            partes.append(f"[{i}:a:0]{ta},asetpts=PTS-STARTPTS[a{i}]")
        else:
            partes.append(f"[{i}:v:0]null[v{i}]")
            partes.append(f"[{i}:a:0]anull[a{i}]")
        rotulos += f"[v{i}][a{i}]"

    fc = ";".join(partes) + f";{rotulos}concat=n={len(takes)}:v=1:a=1[v][a]"
    _run([FFMPEG, "-y", *inputs, "-filter_complex", fc, "-map", "[v]", "-map", "[a]",
          "-c:v", "libx264", "-preset", "veryfast", "-crf", "18",
          "-c:a", "aac", "-b:a", "192k", "-r", "30", out])
    return out


def desilenciar(inp, out, margem="0.2s"):
    _run([AUTO_EDITOR, inp, "-o", out, "--no-open", "--margin", margem])
    return out


def aplicar_velocidade(inp, out, fator):
    """Muda a velocidade do video inteiro (video+audio). fator 1.03 = 3% mais
    rapido, 0.95 = 5% mais lento. atempo preserva o pitch da voz, entao a
    variacao fica inaudivel. Roda ANTES da transcricao para a legenda karaoke
    nascer ja sincronizada com o audio no ritmo final."""
    if fator is None or abs(fator - 1.0) < 0.001:
        shutil.copy(inp, out)
        return out
    _run([FFMPEG, "-y", "-i", inp,
          "-filter_complex",
          f"[0:v:0]setpts=PTS/{fator:.4f}[v];[0:a:0]atempo={fator:.4f}[a]",
          "-map", "[v]", "-map", "[a]",
          "-c:v", "libx264", "-preset", "veryfast", "-crf", "18",
          "-c:a", "aac", "-b:a", "192k", out])
    return out


def queimar_legenda(inp, ass_path, out):
    # roda com cwd = pasta do .ass e passa o nome relativo, pra fugir do inferno
    # de escape de path do filtro ass no Windows (dois-pontos do drive).
    work = os.path.dirname(ass_path)
    ass_nome = os.path.basename(ass_path)
    _run([FFMPEG, "-y", "-i", os.path.abspath(inp),
          "-vf", f"ass={ass_nome}",
          "-c:v", "libx264", "-preset", "veryfast", "-crf", "18",
          "-c:a", "copy", os.path.abspath(out)], cwd=work)
    return out


def processar_video(takes, out_final, model="base.en", lang="en",
                    margem="0.2s", fator=None, log=print):
    if not takes:
        raise RuntimeError("nenhum take encontrado")
    work = tempfile.mkdtemp(prefix="owedit_")
    try:
        juntado = os.path.join(work, "01_juntado.mp4")
        cortado = os.path.join(work, "02_cortado.mp4")
        ritmado = os.path.join(work, "03_ritmado.mp4")
        assf = os.path.join(work, "04_legenda.ass")

        log(f"  juntando {len(takes)} take(s)...")
        concat(takes, juntado)
        log("  tirando silencio (auto-editor)...")
        desilenciar(juntado, cortado, margem)
        if fator is not None and abs(fator - 1.0) >= 0.001:
            log(f"  variando velocidade: {fator:.3f}x...")
            aplicar_velocidade(cortado, ritmado, fator)
            base = ritmado
        else:
            base = cortado
        w, h = dims(base)
        log(f"  transcrevendo (whisper {model})... {w}x{h}")
        palavras = transcrever(base, model, lang)
        log(f"  {len(palavras)} palavras -> legenda")
        gerar_ass(palavras, w, h, assf)
        log("  queimando legenda...")
        os.makedirs(os.path.dirname(os.path.abspath(out_final)), exist_ok=True)
        queimar_legenda(base, assf, out_final)
        log(f"  OK -> {out_final}")
        return out_final
    finally:
        shutil.rmtree(work, ignore_errors=True)


def _tem_video_solto(pasta):
    return any(a.lower().endswith(VIDEO_EXT) for a in os.listdir(pasta)
              if os.path.isfile(os.path.join(pasta, a)))


def processar_pasta(entrada, saida, model="base.en", lang="en", margem="0.2s", log=print):
    """Processa a pasta de entrada (subpastas=1 video cada, ou arquivos soltos=1 video).
    Retorna lista de arquivos gerados."""
    os.makedirs(saida, exist_ok=True)
    gerados = []

    # o Flow entrega o lote como .zip; extrai antes de decidir o modo de pasta
    extraidas = extrair_zips(entrada, log)

    subpastas = [d for d in sorted(os.listdir(entrada), key=_natural)
                 if os.path.isdir(os.path.join(entrada, d))]

    # se veio de zip, o modo e sempre "1 video por subpasta", mesmo que haja
    # video solto na entrada (evita misturar lote antigo com o recem-extraido)
    if not extraidas and _tem_video_solto(entrada):
        # arquivos soltos = 1 video
        nome = os.path.basename(os.path.normpath(entrada)) or "video"
        out = os.path.join(saida, f"{nome}_final.mp4")
        log(f"[1 video] {nome}")
        gerados.append(processar_video(coletar_takes(entrada), out, model, lang, margem, log))
    elif subpastas:
        for i, d in enumerate(subpastas, 1):
            takes = coletar_takes(os.path.join(entrada, d))
            if not takes:
                log(f"[{i}/{len(subpastas)}] {d}: sem takes, pulando")
                continue
            out = os.path.join(saida, f"{d}_final.mp4")
            log(f"[{i}/{len(subpastas)}] {d}")
            gerados.append(processar_video(takes, out, model, lang, margem, log))
    else:
        raise RuntimeError("pasta de entrada nao tem videos nem subpastas com videos")
    return gerados


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(description="Editor CapCut offline (junta+desilencia+legenda)")
    ap.add_argument("--input", "-i", required=True, help="pasta de entrada (takes do Veo)")
    ap.add_argument("--output", "-o", required=True, help="pasta de saida")
    ap.add_argument("--model", default="base.en", help="modelo whisper (base.en, small.en, medium.en)")
    ap.add_argument("--lang", default="en")
    ap.add_argument("--margin", default="0.2s", help="margem de silencio a manter (ex: 0.2s)")
    a = ap.parse_args()
    feitos = processar_pasta(a.input, a.output, a.model, a.lang, a.margin)
    print(f"\nPronto. {len(feitos)} video(s) gerado(s):")
    for f in feitos:
        print("  -", f)
