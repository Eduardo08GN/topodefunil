"""Veo Editor By EDDIE — esteira de producao offline.

Abre o painel em http://127.0.0.1:7861. O watcher liga junto com o app: todo
.zip adbatch*.zip que cair na pasta Downloads (ou qualquer .zip arrastado para
01_entrada) e capturado, editado (juntar takes em ordem + tirar silencio +
variar velocidade + legenda CapCut) e organizado em 03_prontos/<data>/.
Modo manual (pasta avulsa) continua disponivel no fim do painel."""

import os
import threading
import webbrowser
import subprocess

from flask import Flask, render_template, request, jsonify, send_file

import esteira
from pipeline import processar_pasta, coletar_takes, contar_zips, VIDEO_EXT

app = Flask(__name__)

# ---------------- esteira (modo principal) ----------------


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/status")
def status():
    return jsonify(esteira.status())


@app.route("/config", methods=["POST"])
def config():
    d = request.get_json(silent=True) or {}
    if d.get("model") in ("base.en", "small.en", "medium.en"):
        esteira.CFG["model"] = d["model"]
    if d.get("margem") in ("0.15s", "0.2s", "0.35s"):
        esteira.CFG["margem"] = d["margem"]
    return jsonify(ok=True, cfg=dict(esteira.CFG))


@app.route("/retry", methods=["POST"])
def retry():
    nome = (request.get_json(silent=True) or {}).get("zip", "")
    return jsonify(ok=esteira.tentar_de_novo(nome))


@app.route("/video/<data>/<arquivo>")
def video(data, arquivo):
    p = esteira.caminho_video(data, arquivo)
    if not p:
        return "nao encontrado", 404
    return send_file(p, mimetype="video/mp4", conditional=True)


@app.route("/abrir-pasta", methods=["POST"])
def abrir_pasta():
    # abre o Explorer na pasta de prontos (app e local, sem risco)
    try:
        subprocess.Popen(["explorer", esteira.D_PRONTOS])
        return jsonify(ok=True)
    except OSError as e:
        return jsonify(ok=False, msg=str(e))


# ---------------- modo manual (legado, pasta avulsa) ----------------

JOB = {"running": False, "log": [], "gerados": [], "erro": None}


def _log(msg):
    JOB["log"].append(str(msg))


def _rodar(entrada, saida, model, margem):
    JOB.update(running=True, log=[], gerados=[], erro=None)
    try:
        _log(f"entrada: {entrada}")
        _log(f"saida:   {saida}")
        _log(f"modelo whisper: {model} | margem silencio: {margem}")
        _log("-" * 40)
        gerados = processar_pasta(entrada, saida, model=model, margem=margem, log=_log)
        JOB["gerados"] = gerados
        _log("-" * 40)
        _log(f"CONCLUIDO: {len(gerados)} video(s) gerado(s).")
    except Exception as e:  # noqa: BLE001
        JOB["erro"] = str(e)
        _log(f"ERRO: {e}")
    finally:
        JOB["running"] = False


@app.route("/inspecionar", methods=["POST"])
def inspecionar():
    entrada = (request.get_json(silent=True) or {}).get("entrada", "").strip('"').strip()
    if not entrada or not os.path.isdir(entrada):
        return jsonify(ok=False, msg="Pasta de entrada nao encontrada.")
    subs = [d for d in os.listdir(entrada) if os.path.isdir(os.path.join(entrada, d))]
    soltos = [a for a in os.listdir(entrada)
              if a.lower().endswith(VIDEO_EXT) and os.path.isfile(os.path.join(entrada, a))]
    zips = contar_zips(entrada)
    if zips:
        return jsonify(ok=True, videos=len(zips),
                       modo=f"{len(zips)} zip(s) — extracao automatica, 1 video por zip")
    if soltos:
        return jsonify(ok=True, modo="1 video (arquivos soltos)", videos=1, takes=len(soltos))
    validos = [d for d in subs if coletar_takes(os.path.join(entrada, d))]
    if validos:
        return jsonify(ok=True, modo=f"{len(validos)} video(s) (1 por subpasta)", videos=len(validos))
    return jsonify(ok=False, msg="Nenhum video (nem em subpastas) encontrado.")


@app.route("/processar", methods=["POST"])
def processar():
    if JOB["running"]:
        return jsonify(ok=False, msg="Ja tem um processamento rodando.")
    d = request.get_json(silent=True) or {}
    entrada = d.get("entrada", "").strip('"').strip()
    saida = d.get("saida", "").strip('"').strip()
    model = d.get("model", "base.en")
    margem = d.get("margem", "0.2s")
    if not os.path.isdir(entrada):
        return jsonify(ok=False, msg="Pasta de entrada nao existe.")
    if not saida:
        return jsonify(ok=False, msg="Informe a pasta de saida.")
    threading.Thread(target=_rodar, args=(entrada, saida, model, margem), daemon=True).start()
    return jsonify(ok=True)


@app.route("/manual/status")
def manual_status():
    return jsonify(running=JOB["running"], log=JOB["log"],
                   gerados=JOB["gerados"], erro=JOB["erro"])


if __name__ == "__main__":
    esteira.iniciar()
    url = "http://127.0.0.1:7861"
    print(f"\n  Veo Editor By EDDIE rodando em {url}")
    print(f"  Esteira vigiando: {esteira.DOWNLOADS} (adbatch*.zip)")
    print(f"                    {esteira.D_ENTRADA} (*.zip)")
    print("  Feche esta janela para encerrar o app.\n")
    try:
        threading.Timer(1.2, lambda: webbrowser.open(url)).start()
    except Exception:  # noqa: BLE001
        pass
    app.run(host="127.0.0.1", port=7861, debug=False)
