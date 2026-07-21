"""Veo Editor By EDDIE — app offline (roda so na sua maquina): informa a pasta
de ENTRADA (os takes do Veo ou o .zip baixado do Flow) e a pasta de SAIDA,
clica Processar. Junta + tira silencio + legenda CapCut, tudo local.
Abra http://127.0.0.1:7861 no navegador."""

import os
import threading
import webbrowser

from flask import Flask, render_template, request, jsonify

from pipeline import processar_pasta, coletar_takes, contar_zips, VIDEO_EXT

app = Flask(__name__)

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


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/inspecionar", methods=["POST"])
def inspecionar():
    """Conta o que ha na pasta de entrada, pra dar feedback antes de rodar."""
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


@app.route("/status")
def status():
    return jsonify(running=JOB["running"], log=JOB["log"],
                   gerados=JOB["gerados"], erro=JOB["erro"])


if __name__ == "__main__":
    url = "http://127.0.0.1:7861"
    print(f"\n  Veo Editor By EDDIE rodando em {url}")
    print("  Feche esta janela para encerrar o app.\n")
    try:
        threading.Timer(1.2, lambda: webbrowser.open(url)).start()
    except Exception:  # noqa: BLE001
        pass
    app.run(host="127.0.0.1", port=7861, debug=False)
