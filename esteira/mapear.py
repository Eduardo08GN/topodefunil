# -*- coding: utf-8 -*-
"""ESTEIRA · ETAPA 2 — MAPEAR: o video-fonte vira um MAPA DE FIDELIDADE, sem ninguem olhar quadro.

    python esteira/mapear.py <slug>          (slug = pasta em esteira/saida/, criada pelo ler.py)

Sai `mapa_fidelidade.json` na pasta do slug, com tudo que a montagem precisa MEDIDO:
  - takes (do ler.py) e a DIVISAO dos takes acima do teto do Veo (8s), na maior pausa da fala
  - palavras com tempo (faster-whisper) e a fala verbatim por take/sub-take
  - LEGENDA KARAOKE: presenca, centro (x,y), altura da caixa alta — pela PALAVRA AMARELA
  - LABELS estaticas com glow (tipo "DAY 1"): segmentos t0/t1 + bbox — por brilho laranja
  - PILULA (retangulo branco arredondado): t0/t1 + bbox
  - MUSICA: presenca e t0/t1 por energia de graves; trecho sem voz extraido como cama
  - CAMERA: fator de push-in por take, pela altura do rosto (Haar) inicio -> fim

⛔ O que o codigo NAO le': o TEXTO das labels e da pilula (nao ha OCR local) e a DESCRICAO
visual de cada take. Isso e' a etapa 3 (o chat do operador, com a folha): este script
escreve `PEDIDO-CLONE.md` dizendo exatamente o que o chat deve devolver.

Licoes pagas que estao aqui em codigo (2026-09-03/04):
  - detector de "texto branco" e' CONTAMINADO por gola, balcao, casa branca. A legenda
    karaoke se acha pela PALAVRA AMARELA; a label estatica, pelo HALO laranja; a pilula,
    pela FORMA (retangulo largo, solido, arredondado). Nunca por "branco".
  - objeto amarelo fixo (limao) engana o detector de karaoke: descarta-se o que e'
    amarelo em > 90% dos quadros no mesmo lugar.
  - a musica NAO e' "presente ate' o fim" por padrao: na Martha ela para no corte do
    take 3. Mede-se a energia de graves nas pausas da fala.
"""
import argparse, json, os, subprocess, sys
import numpy as np

AQUI = os.path.dirname(os.path.abspath(__file__))
SAIDA = os.path.join(AQUI, "saida")
TETO_VEO = 8.0
FPS_AMOSTRA = 5          # quadros por segundo analisados (bastam para texto e forma)


def ffprobe_dur(p):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p],
                       capture_output=True, text=True)
    return float(r.stdout.strip() or 0)


def palavras(video):
    from faster_whisper import WhisperModel
    m = WhisperModel("small", device="cpu", compute_type="int8")
    segs, _ = m.transcribe(video, word_timestamps=True, language="en")
    return [{"w": w.word.strip(), "t0": round(w.start, 2), "t1": round(w.end, 2)}
            for s in segs for w in (s.words or []) if w.word.strip()]


def quadros(video, fps_amostra=FPS_AMOSTRA):
    """Gerador (t, frame) a fps_amostra."""
    import cv2
    cap = cv2.VideoCapture(video); fps = cap.get(cv2.CAP_PROP_FPS) or 30
    n = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)); passo = max(1, int(round(fps / fps_amostra)))
    i = 0
    while True:
        ok, fr = cap.read()
        if not ok: break
        if i % passo == 0: yield i / fps, fr
        i += 1
    cap.release()


# ── LEGENDA KARAOKE (palavra amarela) ────────────────────────────────────────
def mapear_karaoke(video):
    import cv2
    amostras = []; W = H = None
    mapa_fixo = None; n = 0
    for t, fr in quadros(video):
        H, W = fr.shape[:2]
        hsv = cv2.cvtColor(fr, cv2.COLOR_BGR2HSV)
        am = cv2.inRange(hsv, (22, 160, 190), (34, 255, 255))
        mapa_fixo = am.astype(np.uint16) if mapa_fixo is None else mapa_fixo + (am > 0)
        n += 1; amostras.append((t, am))
    if not amostras: return None
    fixo = (mapa_fixo / max(1, n)) > 0.90          # amarelo em >90% dos quadros = objeto (limao)
    pts = []
    for t, am in amostras:
        am = am.copy(); am[fixo] = 0
        am[:int(H * 0.10)] = 0; am[int(H * 0.78):] = 0
        nl, lab, st, ce = cv2.connectedComponentsWithStats(am)
        blobs = [s for s in st[1:] if s[4] > 40 and H * 0.012 < s[3] < H * 0.09 and s[2] > s[3] * 0.6]
        if blobs:
            # a palavra amarela: junta os blobs (letras) numa caixa
            x0 = min(b[0] for b in blobs); x1 = max(b[0] + b[2] for b in blobs)
            y0 = min(b[1] for b in blobs); y1 = max(b[1] + b[3] for b in blobs)
            pts.append((t, (x0 + x1) / 2 / W, (y0 + y1) / 2 / H, (y1 - y0) / H))
    if len(pts) < 0.05 * len(amostras): return None
    ts = [p[0] for p in pts]
    return {"presente": True, "t0": round(min(ts), 2), "t1": round(max(ts), 2),
            "cobertura": round(len(pts) / len(amostras), 3),
            "centro_pct": [round(float(np.median([p[1] for p in pts])), 3), round(float(np.median([p[2] for p in pts])), 3)],
            "altura_caixa_alta_pct": round(float(np.median([p[3] for p in pts])), 4),
            "estilo": "caixa alta, branca, contorno preto, palavra atual em amarelo"}


# ── LABELS ESTATICAS COM GLOW (tipo "DAY 1") ─────────────────────────────────
def mapear_labels(video):
    import cv2
    obs = []; H = W = None
    for t, fr in quadros(video):
        H, W = fr.shape[:2]
        band = fr[:int(H * 0.5)]
        hsv = cv2.cvtColor(band, cv2.COLOR_BGR2HSV)
        white = cv2.inRange(hsv, (0, 0, 235), (180, 35, 255))
        glow = cv2.inRange(hsv, (3, 150, 150), (22, 255, 255)) | cv2.inRange(hsv, (170, 150, 150), (180, 255, 255))
        white = cv2.morphologyEx(white, cv2.MORPH_CLOSE, np.ones((7, 21), np.uint8))
        nl, lab, st, ce = cv2.connectedComponentsWithStats(white)
        for s in st[1:]:
            x, y, w, h, a = s
            if w < W * 0.08 or not (H * 0.025 < h < H * 0.10): continue
            pad = int(h * 0.6)
            ring = glow[max(0, y - pad):y + h + pad, max(0, x - pad):x + w + pad]
            halo = float(ring.sum() / 255) / max(1.0, float(a))
            if halo < 0.8: continue            # sem halo laranja = casa branca, nuvem, gola
            obs.append((t, x / W, y / H, (x + w) / W, (y + h) / H))
    # 1) no MESMO quadro, juntar componentes na mesma linha (palavras da mesma label: "DAY" + "64")
    por_t = {}
    for t, x0, y0, x1, y1 in obs: por_t.setdefault(t, []).append([x0, y0, x1, y1])
    obs = []
    for t, caixas in por_t.items():
        caixas.sort(); fund = []
        for c in caixas:
            if fund and abs((fund[-1][1] + fund[-1][3]) / 2 - (c[1] + c[3]) / 2) < 0.03 and c[0] - fund[-1][2] < 0.10:
                fund[-1] = [fund[-1][0], min(fund[-1][1], c[1]), c[2], max(fund[-1][3], c[3])]
            else: fund.append(c)
        obs += [(t, *c) for c in fund]
    # 2) agrupar por caixa parecida e tempo continuo
    segs = []
    for t, x0, y0, x1, y1 in sorted(obs):
        for sg in segs:
            if abs(sg["cy"] - (y0 + y1) / 2) < 0.04 and abs(sg["cx"] - (x0 + x1) / 2) < 0.12 and t - sg["t1"] <= 0.6:
                sg["t1"] = t; sg["n"] += 1
                sg["bbs"].append((x0, y0, x1, y1)); break
        else:
            segs.append({"t0": t, "t1": t, "n": 1, "cx": (x0 + x1) / 2, "cy": (y0 + y1) / 2, "bbs": [(x0, y0, x1, y1)]})
    out = []
    for sg in segs:
        if sg["t1"] - sg["t0"] < 0.8: continue
        if sg["n"] < 0.6 * (sg["t1"] - sg["t0"]) * FPS_AMOSTRA: continue   # label de verdade fica parada; brilho de flor pisca
        b = np.median(np.array(sg["bbs"]), axis=0)
        out.append({"t0": round(sg["t0"], 2), "t1": round(sg["t1"], 2),
                    "bbox_pct": [round(float(v), 3) for v in b],
                    "centro_pct": [round(float((b[0] + b[2]) / 2), 3), round(float((b[1] + b[3]) / 2), 3)],
                    "altura_caixa_alta_pct": round(float(b[3] - b[1]), 4),
                    "texto": None,   # <- vem do chat (PEDIDO-CLONE.md)
                    "estilo": "caixa alta branca, contorno preto fino, glow laranja->vermelho"})
    return out


# ── PILULA (retangulo branco arredondado) ────────────────────────────────────
def mapear_pilula(video):
    import cv2
    obs = []
    for t, fr in quadros(video):
        H, W = fr.shape[:2]
        hsv = cv2.cvtColor(fr, cv2.COLOR_BGR2HSV)
        wm = cv2.inRange(hsv, (0, 0, 225), (180, 25, 255)); wm[:int(H * 0.35)] = 0; wm[int(H * 0.80):] = 0
        nl, lab, st, ce = cv2.connectedComponentsWithStats(wm)
        for s in st[1:]:
            x, y, w, h, a = s
            if w < W * 0.30 or not (H * 0.03 < h < H * 0.09) or w / h < 4: continue
            if a / float(w * h) < 0.80: continue           # solido = e' uma caixa, nao texto
            obs.append((t, x / W, y / H, (x + w) / W, (y + h) / H))
    if not obs: return None
    ts = [o[0] for o in obs]
    if max(ts) - min(ts) < 0.8: return None
    b = np.median(np.array([o[1:] for o in obs]), axis=0)
    return {"t0": round(min(ts), 2), "t1": round(max(ts), 2), "bbox_pct": [round(float(v), 4) for v in b],
            "texto": None,   # <- vem do chat
            "estilo": "retangulo branco arredondado, texto escuro regular, emoji reais"}


# ── MUSICA (graves nas pausas da fala) ──────────────────────────────────────
def mapear_musica(video, pals, dur, dest_wav):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", video, "-ac", "1", "-ar", "16000", "-f", "s16le", "-"],
                         capture_output=True).stdout
    a = np.frombuffer(raw, np.int16).astype(np.float32) / 32768; hop = 3200
    graves = []
    for i in range(0, len(a) - hop, hop):
        seg = a[i:i + hop] * np.hanning(hop); sp = np.abs(np.fft.rfft(seg)); f = np.fft.rfftfreq(hop, 1 / 16000)
        graves.append((i / 16000, 20 * np.log10(sp[(f > 40) & (f < 110)].mean() + 1e-6)))
    # janelas SEM fala
    def falando(t): return any(w["t0"] - 0.1 <= t <= w["t1"] + 0.1 for w in pals)
    silenc = [(t, g) for t, g in graves if not falando(t)]
    if not silenc:
        return {"presente": None, "obs": "sem pausa de fala para medir; assumido SEM musica"}, None
    nivel = float(np.median([g for _, g in silenc]))
    presente = nivel > 5.0                                # medido: cama musical ~25 dB; silencio ~-40
    if not presente:
        return {"presente": False, "nivel_graves_pausas_db": round(nivel, 1)}, None
    on = [t for t, g in graves if g > nivel - 12]
    t0, t1 = min(on), max(on) + 0.2
    # cama: o maior trecho sem fala dentro da musica
    melhor = (0, 0, 0)
    ini = None
    for t, g in graves:
        if t0 <= t <= t1 and not falando(t):
            ini = t if ini is None else ini
        else:
            if ini is not None and t - ini > melhor[2]: melhor = (ini, t, t - ini)
            ini = None
    if melhor[2] >= 2.0:
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", video, "-vn", "-ss", str(melhor[0]), "-t", str(melhor[2]),
                        "-ac", "2", "-ar", "44100", dest_wav])
    return {"presente": True, "t0": round(t0, 2), "t1": round(min(t1, dur), 2), "nivel_graves_db": round(nivel, 1),
            "cama": {"arquivo": dest_wav if melhor[2] >= 2.0 else None, "trecho_sem_voz": [round(melhor[0], 2), round(melhor[1], 2)]}}, None


# ── CAMERA (push-in pela altura do rosto) ────────────────────────────────────
def mapear_camera(video, takes):
    import cv2
    casc = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    cap = cv2.VideoCapture(video); out = []
    def rosto(t):
        cap.set(cv2.CAP_PROP_POS_MSEC, t * 1000); ok, fr = cap.read()
        if not ok: return None
        fs = casc.detectMultiScale(cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY), 1.1, 4, minSize=(60, 60))
        if not len(fs): return None
        x, y, w, h = max(fs, key=lambda r: r[2] * r[3]); return h / fr.shape[0], (x + w / 2) / fr.shape[1], (y + h / 2) / fr.shape[0]
    for tk in takes:
        def med(ts):
            rs = [r for r in (rosto(t) for t in ts) if r]
            return (float(np.median([r[0] for r in rs])), float(np.median([r[1] for r in rs])), float(np.median([r[2] for r in rs]))) if rs else None
        a = med([tk["t0"] + 0.2, tk["t0"] + 0.5, tk["t0"] + 0.8]); b = med([tk["t1"] - 0.8, tk["t1"] - 0.5, tk["t1"] - 0.2])
        push = round(b[0] / a[0], 2) if (a and b and a[0] > 0) else 1.0
        push = max(1.0, min(1.6, push))            # teto 1,6: acima disso e' ruido do Haar (Martha take 1 media 2,0 e a fonte e' ~1,1)
        if push < 1.12: push = 1.0                        # ruido do Haar; a fonte "fixa" mede 1,03-1,11
        out.append({"take": tk["i"], "pushin": push, "_obs": "estimativa por altura do rosto (Haar) — a lente mais fraca do mapa", "foco": [round(b[1], 2), round(b[2], 2)] if b else [0.5, 0.5],
                    "rosto_inicio": [round(v, 3) for v in a] if a else None, "rosto_fim": [round(v, 3) for v in b] if b else None})
    cap.release(); return out


# ── DIVISAO dos takes acima do teto ─────────────────────────────────────────
def dividir(takes, pals):
    out = []
    for tk in takes:
        ws = [w for w in pals if tk["t0"] <= w["t0"] < tk["t1"]]
        dur = tk["t1"] - tk["t0"]
        if dur <= TETO_VEO or len(ws) < 4:
            out.append({"take": tk["i"], "parte": 1, "t0": tk["t0"], "t1": tk["t1"], "dur": round(dur, 2),
                        "fala": " ".join(w["w"] for w in ws)})
            continue
        # cortar na MAIOR pausa entre palavras dentro do miolo do take (30%-70%)
        melhor = None
        for a, b in zip(ws, ws[1:]):
            pos = (b["t0"] - tk["t0"]) / dur
            if 0.3 <= pos <= 0.7:
                gap = b["t0"] - a["t1"]
                if melhor is None or gap > melhor[0]: melhor = (gap, a["t1"], b["t0"])
        corte = (melhor[1] + melhor[2]) / 2 if melhor else tk["t0"] + dur / 2
        for k, (t0, t1) in enumerate(((tk["t0"], corte), (corte, tk["t1"])), 1):
            sub = [w for w in ws if t0 <= w["t0"] < t1]
            out.append({"take": tk["i"], "parte": k, "t0": round(t0, 2), "t1": round(t1, 2), "dur": round(t1 - t0, 2),
                        "fala": " ".join(w["w"] for w in sub), "dividido_em": round(corte, 2)})
    return out


def main():
    ap = argparse.ArgumentParser(description="Etapa 2 da esteira — mapa de fidelidade")
    ap.add_argument("slug"); a = ap.parse_args()
    pasta = os.path.join(SAIDA, a.slug)
    dos = json.load(open(os.path.join(pasta, "dossie.json"), encoding="utf-8"))
    video = dos["arquivo"]; dur = float(dos["duracao"])
    print("mapeando", os.path.basename(video), f"{dur:.1f}s")

    pals = palavras(video); print("  palavras:", len(pals))
    partes = dividir(dos["takes"], pals); print("  takes:", len(dos["takes"]), "-> clipes:", len(partes))
    kar = mapear_karaoke(video); print("  karaoke:", "sim" if kar else "nao", kar and kar["centro_pct"])
    labs = mapear_labels(video); print("  labels com glow:", len(labs))
    pil = mapear_pilula(video); print("  pilula:", "sim" if pil else "nao")
    mus, _ = mapear_musica(video, pals, dur, os.path.join(pasta, "musica_fonte.wav")); print("  musica:", mus.get("presente"))
    cam = mapear_camera(video, dos["takes"]); print("  camera:", [c["pushin"] for c in cam])

    mapa = {"fonte": {"arquivo": video, "duracao_s": dur, "slug": a.slug},
            "takes": dos["takes"], "cortes": dos["cortes"], "clipes": partes, "palavras": pals,
            "legenda_karaoke": kar, "labels": labs, "pilula": pil, "trilha": mus, "camera": cam,
            "teto_veo_s": TETO_VEO}
    json.dump(mapa, open(os.path.join(pasta, "mapa_fidelidade.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)

    # o que o CHAT precisa devolver (etapa 3)
    ped = ["# PEDIDO-CLONE — cole no chat junto com `folha.jpg`", "",
           "Devolva **so' JSON**, neste formato, e salve como `descricoes.json` nesta pasta:", "", "```json", "{",
           '  "persona": {"prompt_img": "<retrato do narrador: idade, etnia, cabelo, barba, roupa, cenario fixo, luz — em ingles, 9:16>"},',
           '  "takes": {']
    for tk in dos["takes"]:
        ped.append(f'    "{tk["i"]}": {{"cena": "<o que esta em quadro, em ingles>", "acao": "<o que a pessoa FAZ neste take, em ingles>"}},')
    ped[-1] = ped[-1].rstrip(",")
    ped.append("  },")
    ped.append('  "labels_texto": [' + ", ".join(f'"<texto da label em {l["t0"]}-{l["t1"]}s>"' for l in labs) + "],")
    ped.append('  "pilula_texto": ' + ('"<texto da pilula, com os emojis>"' if pil else 'null'))
    ped += ["}", "```", "", "Regras: descreva o que VE, nao invente; roupa e cenario iguais em todos os takes se forem iguais na folha;",
            "nao cite marca nem pessoa famosa; nada de aparelho na mao do personagem."]
    open(os.path.join(pasta, "PEDIDO-CLONE.md"), "w", encoding="utf-8").write("\n".join(ped))
    print("pronto:", os.path.join(pasta, "mapa_fidelidade.json"))
    print("  -> etapa 3: cole PEDIDO-CLONE.md + folha.jpg no chat; salve a resposta como descricoes.json")


if __name__ == "__main__":
    main()
