"""Esteira de producao do Veo Editor: vigia a pasta Downloads (e 01_entrada),
captura o .zip que as ferramentas do Flow baixam, edita sozinha e organiza o
resultado em pastas de fila/prontos/arquivo/erros. Desenhada para dezenas de
videos por dia sem intervencao manual.

Pastas (criadas ao lado do app):
  01_entrada/          zips arrastados manualmente (qualquer *.zip)
  02_processando/      zip + takes extraidos do video em edicao
  03_prontos/AAAA-MM-DD/vNNN_final.mp4
  04_zips_arquivados/  zip original preservado (limpeza automatica > 14 dias)
  05_erros/            zip que falhou + .log do erro (com retry pelo painel)
  historico.csv        registro de tudo que passou pela esteira
"""

import os
import re
import csv
import json
import time
import queue
import random
import shutil
import zipfile
import traceback
import threading
from datetime import datetime, date, timedelta

from pipeline import processar_video, coletar_takes, duracao, VIDEO_EXT, _natural

BASE = os.environ.get("VEO_EDITOR_BASE") or os.path.dirname(os.path.abspath(__file__))
D_ENTRADA = os.path.join(BASE, "01_entrada")
D_PROC = os.path.join(BASE, "02_processando")
D_PRONTOS = os.path.join(BASE, "03_prontos")
D_ARQUIVO = os.path.join(BASE, "04_zips_arquivados")
D_ERROS = os.path.join(BASE, "05_erros")
HISTORICO = os.path.join(BASE, "historico.csv")
CONFIG = os.path.join(BASE, "config.json")

# so zips das nossas ferramentas sao capturados na pasta vigiada; na 01_entrada
# qualquer zip vale (caminho manual)
PADRAO_DOWNLOADS = re.compile(r"^adbatch.*\.zip$", re.I)
DIAS_ARQUIVO = 14
VEL_MIN, VEL_MAX = 0.95, 1.03  # -5% a +3%, sorteado por video

# watch_dir vazio = usa o Downloads do Windows
CFG = {"model": "base.en", "margem": "0.2s", "watch_dir": ""}

_lock = threading.RLock()
_fila = queue.Queue()
_iniciada = False

ESTADO = {
    "pendentes": [],   # [nome do zip aguardando]
    "atual": None,     # {"zip", "etapa", "log": [...]}
    "prontos": [],     # [{"arquivo","data","zip","duracao","fator","hora"}]
    "erros": [],       # [{"zip","erro","hora"}]
    "watch": [],       # pastas vigiadas (informativo pro painel)
}


def pasta_downloads():
    """Downloads verdadeiro do Windows (nao um palpite em ~/Downloads)."""
    if os.name == "nt":
        try:
            import winreg
            with winreg.OpenKey(
                winreg.HKEY_CURRENT_USER,
                r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders",
            ) as k:
                val, _ = winreg.QueryValueEx(k, "{374DE290-123F-4565-9164-39C4925E467B}")
            p = os.path.expandvars(val)
            if os.path.isdir(p):
                return p
        except OSError:
            pass
    return os.path.join(os.path.expanduser("~"), "Downloads")


def _carregar_cfg():
    try:
        with open(CONFIG, encoding="utf-8") as f:
            dados = json.load(f)
        for k in CFG:
            if isinstance(dados.get(k), str):
                CFG[k] = dados[k]
    except (OSError, ValueError):
        pass


def salvar_cfg():
    try:
        with open(CONFIG, "w", encoding="utf-8") as f:
            json.dump(CFG, f, ensure_ascii=False, indent=2)
    except OSError:
        pass


def pasta_vigiada():
    """Pasta onde os zips sao capturados. Prioridade:
    env (testes) > escolhida pelo usuario (config.json) > Downloads real."""
    env = os.environ.get("VEO_EDITOR_DOWNLOADS")
    if env:
        return env
    if CFG["watch_dir"] and os.path.isdir(CFG["watch_dir"]):
        return CFG["watch_dir"]
    return pasta_downloads()


def _modo_downloads(vigiada):
    """True quando a pasta vigiada e o Downloads real: ai vale o filtro
    adbatch*.zip (senao a esteira engoliria qualquer download). Numa pasta
    dedicada escolhida pelo usuario, QUALQUER .zip e capturado."""
    try:
        return os.path.normcase(os.path.abspath(vigiada)) == \
            os.path.normcase(os.path.abspath(pasta_downloads()))
    except OSError:
        return True


def _captura(nome, modo_downloads):
    if not nome.lower().endswith(".zip"):
        return False
    return PADRAO_DOWNLOADS.match(nome) is not None if modo_downloads else True


def definir_pasta_vigiada(p):
    """Troca a pasta vigiada em tempo real (o watcher le a cada ciclo)."""
    if not p or not os.path.isdir(p):
        return False
    CFG["watch_dir"] = os.path.normpath(p)
    salvar_cfg()
    return True


def _preparar_pastas():
    for d in (D_ENTRADA, D_PROC, D_PRONTOS, D_ARQUIVO, D_ERROS):
        os.makedirs(d, exist_ok=True)


def _nome_unico(pasta, nome):
    """a.zip -> a.zip, a (2).zip, a (3).zip... ate nao colidir."""
    destino = os.path.join(pasta, nome)
    if not os.path.exists(destino):
        return destino
    raiz, ext = os.path.splitext(nome)
    n = 2
    while True:
        destino = os.path.join(pasta, f"{raiz} ({n}){ext}")
        if not os.path.exists(destino):
            return destino
        n += 1


def _registrar(arquivo, data_str, zip_origem, dur, fator, status):
    novo = not os.path.exists(HISTORICO)
    with open(HISTORICO, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if novo:
            w.writerow(["datahora", "arquivo", "data", "zip_origem",
                        "duracao_s", "fator", "status"])
        w.writerow([datetime.now().isoformat(timespec="seconds"), arquivo,
                    data_str, zip_origem, f"{dur:.1f}", f"{fator:.4f}", status])


def _carregar_prontos_de_hoje():
    """Repovoa o painel apos reiniciar o app no meio do dia."""
    if not os.path.exists(HISTORICO):
        return
    hoje = date.today().isoformat()
    try:
        with open(HISTORICO, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                if row.get("data") == hoje and row.get("status") == "ok":
                    ESTADO["prontos"].append({
                        "arquivo": row["arquivo"], "data": row["data"],
                        "zip": row["zip_origem"],
                        "duracao": float(row["duracao_s"] or 0),
                        "fator": float(row["fator"] or 1),
                        "hora": row["datahora"][11:16],
                    })
    except (OSError, ValueError, KeyError):
        pass


def _limpar_arquivo_antigo():
    limite = time.time() - DIAS_ARQUIVO * 86400
    try:
        for a in os.listdir(D_ARQUIVO):
            p = os.path.join(D_ARQUIVO, a)
            if os.path.isfile(p) and os.path.getmtime(p) < limite:
                os.remove(p)
    except OSError:
        pass


def _proximo_nome(pasta_dia):
    """v001_final.mp4, v002_final.mp4... sequencial dentro da pasta do dia."""
    os.makedirs(pasta_dia, exist_ok=True)
    maior = 0
    for a in os.listdir(pasta_dia):
        m = re.match(r"^v(\d+)_final\.mp4$", a, re.I)
        if m:
            maior = max(maior, int(m.group(1)))
    return f"v{maior + 1:03d}_final.mp4"


def _extrair_zip(zpath, destino):
    """Extrai so os videos, achatando a estrutura interna do zip."""
    os.makedirs(destino, exist_ok=True)
    with zipfile.ZipFile(zpath) as zf:
        for membro in zf.infolist():
            if membro.is_dir():
                continue
            nome = os.path.basename(membro.filename)
            if not nome or not nome.lower().endswith(VIDEO_EXT):
                continue
            with zf.open(membro) as src, open(os.path.join(destino, nome), "wb") as dst:
                shutil.copyfileobj(src, dst)


def _enfileirar(origem_path):
    """Move o zip para 02_processando e poe na fila."""
    destino = _nome_unico(D_PROC, os.path.basename(origem_path))
    shutil.move(origem_path, destino)
    nome = os.path.basename(destino)
    with _lock:
        ESTADO["pendentes"].append(nome)
    _fila.put(nome)
    return nome


# ---------------- watcher ----------------

def _watcher():
    """Poll a cada 2.5s. Um zip so e capturado quando o tamanho ficou estavel
    entre duas leituras (download concluido) e nao ha .crdownload do navegador."""
    tamanhos = {}
    while True:
        try:
            candidatos = []
            vigiada = pasta_vigiada()  # relido a cada ciclo: troca vale na hora
            modo_dl = _modo_downloads(vigiada)
            for a in os.listdir(vigiada):
                if _captura(a, modo_dl):
                    candidatos.append(os.path.join(vigiada, a))
            for a in os.listdir(D_ENTRADA):
                if a.lower().endswith(".zip"):
                    candidatos.append(os.path.join(D_ENTRADA, a))

            for p in candidatos:
                if not os.path.isfile(p):
                    continue
                if os.path.exists(p + ".crdownload") or os.path.exists(p + ".part"):
                    continue
                try:
                    tam = os.path.getsize(p)
                except OSError:
                    continue
                if tamanhos.get(p) == tam and tam > 0:
                    tamanhos.pop(p, None)
                    try:
                        _enfileirar(p)
                    except OSError:
                        pass  # arquivo em uso; tenta no proximo ciclo
                else:
                    tamanhos[p] = tam
            # esquece caminhos que sumiram
            for p in list(tamanhos):
                if not os.path.exists(p):
                    tamanhos.pop(p, None)
        except OSError:
            pass
        time.sleep(2.5)


# ---------------- worker ----------------

def _log_atual(msg):
    with _lock:
        if ESTADO["atual"] is not None:
            ESTADO["atual"]["log"].append(str(msg))
            # a "etapa" e a ultima linha de log resumida
            ESTADO["atual"]["etapa"] = str(msg).strip()


def _processar_zip(nome):
    zpath = os.path.join(D_PROC, nome)
    extra = os.path.join(D_PROC, os.path.splitext(nome)[0] + "_takes")
    with _lock:
        if nome in ESTADO["pendentes"]:
            ESTADO["pendentes"].remove(nome)
        ESTADO["atual"] = {"zip": nome, "etapa": "extraindo...", "log": []}
    try:
        _log_atual(f"extraindo {nome}...")
        _extrair_zip(zpath, extra)
        takes = coletar_takes(extra)
        if not takes:
            raise RuntimeError("o zip nao tinha nenhum video dentro")
        _log_atual(f"{len(takes)} take(s) em ordem: "
                   + ", ".join(os.path.basename(t) for t in takes))

        fator = round(random.uniform(VEL_MIN, VEL_MAX), 4)
        data_str = date.today().isoformat()
        pasta_dia = os.path.join(D_PRONTOS, data_str)
        arquivo = _proximo_nome(pasta_dia)
        out = os.path.join(pasta_dia, arquivo)

        processar_video(takes, out, model=CFG["model"], margem=CFG["margem"],
                        fator=fator, log=_log_atual)

        dur = duracao(out)
        shutil.move(zpath, _nome_unico(D_ARQUIVO, nome))
        _registrar(arquivo, data_str, nome, dur, fator, "ok")
        with _lock:
            ESTADO["prontos"].append({
                "arquivo": arquivo, "data": data_str, "zip": nome,
                "duracao": dur, "fator": fator,
                "hora": datetime.now().strftime("%H:%M"),
            })
    except Exception as e:  # noqa: BLE001
        erro = str(e)
        try:
            destino_err = _nome_unico(D_ERROS, nome)
            if os.path.exists(zpath):
                shutil.move(zpath, destino_err)
            with open(destino_err + ".log", "w", encoding="utf-8") as f:
                f.write(traceback.format_exc())
            nome = os.path.basename(destino_err)
        except OSError:
            pass
        _registrar("", date.today().isoformat(), nome, 0.0, 1.0, "erro")
        with _lock:
            ESTADO["erros"].append({
                "zip": nome, "erro": erro[:300],
                "hora": datetime.now().strftime("%H:%M"),
            })
    finally:
        shutil.rmtree(extra, ignore_errors=True)
        with _lock:
            ESTADO["atual"] = None


def _worker():
    while True:
        nome = _fila.get()
        try:
            _processar_zip(nome)
        finally:
            _fila.task_done()


# ---------------- API usada pelo app ----------------

def iniciar():
    """Sobe watcher + worker (idempotente). Chamar no boot do app."""
    global _iniciada
    with _lock:
        if _iniciada:
            return
        _iniciada = True
    _preparar_pastas()
    _carregar_cfg()
    _carregar_prontos_de_hoje()
    _limpar_arquivo_antigo()
    threading.Thread(target=_watcher, daemon=True).start()
    threading.Thread(target=_worker, daemon=True).start()


def status():
    with _lock:
        hoje = date.today().isoformat()
        atual = None
        if ESTADO["atual"] is not None:
            atual = {"zip": ESTADO["atual"]["zip"],
                     "etapa": ESTADO["atual"]["etapa"],
                     "log": list(ESTADO["atual"]["log"])}
        vigiada = pasta_vigiada()
        modo_dl = _modo_downloads(vigiada)
        padrao = "adbatch*.zip" if modo_dl else "*.zip"
        ignorados = 0
        if modo_dl:
            # zips no Downloads fora do padrao: avisa em vez de ignorar mudo
            try:
                ignorados = sum(1 for a in os.listdir(vigiada)
                                if a.lower().endswith(".zip")
                                and not PADRAO_DOWNLOADS.match(a))
            except OSError:
                pass
        return {
            "watch": [f"{vigiada} ({padrao})", D_ENTRADA + r" (*.zip)"],
            "ignorados": ignorados,
            "pendentes": list(ESTADO["pendentes"]),
            "atual": atual,
            "prontos": [p for p in ESTADO["prontos"] if p["data"] == hoje],
            "erros": list(ESTADO["erros"]),
            "pasta_prontos": D_PRONTOS,
            "cfg": dict(CFG),
        }


def tentar_de_novo(nome):
    """Retry de um zip que caiu em 05_erros."""
    p = os.path.join(D_ERROS, nome)
    if not os.path.isfile(p):
        return False
    for sufixo in (".log",):
        try:
            os.remove(p + sufixo)
        except OSError:
            pass
    with _lock:
        ESTADO["erros"] = [e for e in ESTADO["erros"] if e["zip"] != nome]
    _enfileirar(p)
    return True


def caminho_video(data_str, arquivo):
    """Resolve com validacao o caminho de um video pronto (pro player)."""
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", data_str):
        return None
    if not re.match(r"^v\d+_final\.mp4$", arquivo, re.I):
        return None
    p = os.path.join(D_PRONTOS, data_str, arquivo)
    return p if os.path.isfile(p) else None
