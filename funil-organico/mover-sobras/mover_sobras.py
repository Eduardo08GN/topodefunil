# -*- coding: utf-8 -*-
"""
MOVER SOBRAS — leva os videos nao postados para o HD externo
=============================================================

O QUE E': um worker que roda sozinho no Windows e, virado o dia, move os videos
que SOBRARAM (os que nunca foram postados) das pastas de dia do Veo Editor 2.0
para uma pasta unica no HD externo.

    C:\\...\\VEO-EDITOR-2.0\\03_prontos\\AAAA-MM-DD\\vNNN_final.mp4
        ->  D:\\estoque\\AAAA-MM-DD__vNNN_final.mp4

Encomenda do operador (2026-08-11): meta de 3 videos por pagina em 15 paginas
ativas; ele produz a mais, e o excedente fica parado na pasta do dia ocupando o
SSD.

-----------------------------------------------------------------------------
⛔⛔ A REGRA E' POSITIVA, E ISSO E' A DECISAO MAIS IMPORTANTE DESTE ARQUIVO
-----------------------------------------------------------------------------
Move-se APENAS o que casa com `vNNN_final.mp4` — o molde que o proprio
`esteira.py` gera (`^v(\\d+)_final\\.mp4$`, linha 292 de la'). Depois de postar,
o operador RENOMEIA o arquivo para `postado...`.

A regra tentadora seria "move tudo que nao se chama postado". Ela esta' ERRADA,
e a prova estava na pasta de 2026-08-09 antes mesmo de escrever este script:

    posado.mp4        <- sem o "t"
    posado (2).mp4    <- sem o "t"

Sao videos JA POSTADOS, com erro de digitacao no rename. A regra negativa os
levaria para o HD como se fossem sobra, e o registro do dia mentiria. A regra
positiva ignora qualquer nome fora do molde — inclusive os erros de digitacao
que ainda vao acontecer.

-----------------------------------------------------------------------------
DECISOES DO OPERADOR (2026-08-11)
-----------------------------------------------------------------------------
destino ......... D:\\estoque  (pasta unica, sem subpasta por dia)
colisao ......... prefixo com a data: `2026-08-10__v003_final.mp4`. Dois dias
                  podem ter um `v003_final.mp4`; sem o prefixo, um sobrescreveria
                  o outro em silencio — e o prefixo ainda ordena por data sozinho.
03_prontos\\estoque  NAO E' TOCADA. Ele transfere aquela pasta a mao.
pasta do dia .... fica como esta', com os `postado*` dentro: e' o registro do
                  que foi ao ar.

-----------------------------------------------------------------------------
COMO RODA
-----------------------------------------------------------------------------
Agendador de Tarefas do Windows: no logon E de hora em hora, com "executar assim
que possivel apos uma inicializacao perdida".

⚠️ E' por isso que NAO se usa a pasta Inicializar: ela roda no logon e mais nada.
Se a maquina estiver desligada na virada do dia — que e' o caso normal dele — a
pasta Inicializar so' agiria no proximo login, e um dia inteiro de sobras ficaria
no SSD ate' la'. O Agendador RECUPERA agendamento perdido.

    python mover_sobras.py --dry-run   # mostra o que faria, sem mover nada
    python mover_sobras.py             # move de verdade
    python mover_sobras.py --hoje      # inclui a pasta de HOJE (nao use no
                                       # agendamento: ele ainda esta' postando)
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import date, datetime

# ── caminhos ────────────────────────────────────────────────────────────────
ORIGEM = r"C:\Users\edlut\Desktop\agentes_py\VEO-EDITOR-2.0\03_prontos"
DESTINO = r"D:\estoque"
LOG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mover_sobras.log")
TRAVA = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".mover_sobras.lock")

TAREFA = "MoverSobrasVeo"

# ⭐⭐ O BATIMENTO. Encomenda do operador: *"quero um feedback visual em ambas as
# interfaces, do editor e do Video Terminator, do status do worker ativo 'live'"*
# — e, na mensagem seguinte: *"live e funcional"*.
#
# ⛔ "Live" nao pode ser "o arquivo do worker existe": isso e' verificar a FORMA.
# O que prova que ele esta' vivo E FUNCIONAL sao tres fatos diferentes, e o
# arquivo carrega os tres:
#   agendado ....... a tarefa existe no Agendador e esta' HABILITADA
#   batendo ........ a ultima execucao foi ha' pouco (ele roda de hora em hora)
#   com destino .... o HD estava conectado na ultima passada
# Agendado sem bater = tarefa quebrada. Batendo sem HD = vivo, mas sem para onde
# levar. Sao estados diferentes e a tela mostra cada um pelo nome.
#
# ⚠️ Fica em LOCALAPPDATA, e nao ao lado do script: as duas interfaces moram em
# pastas diferentes (VEO-EDITOR-2.0 e PILOTO-ADBATCH) e nenhuma delas deve
# precisar saber onde a outra parte foi instalada.
ESTADO_DIR = os.path.join(os.environ.get("LOCALAPPDATA", os.path.expanduser("~")),
                          "MoverSobras")
ESTADO = os.path.join(ESTADO_DIR, "estado.json")

# ⛔ o molde do `esteira.py`, copiado dali e nao reinventado
SOBRA = re.compile(r"^v\d+_final\.mp4$", re.I)
DIA = re.compile(r"^\d{4}-\d{2}-\d{2}$")

# ⚠️ preenchido so' pelo `--dias`. Vazio = comportamento normal (todo dia
# anterior a hoje), que e' o que o agendamento usa.
SO_ESTES_DIAS = None


def log(msg, eco=True):
    linha = "%s  %s" % (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), msg)
    try:
        with open(LOG, "a", encoding="utf-8") as f:
            f.write(linha + "\n")
    except OSError:
        pass
    if eco:
        print(linha)


def pastas_de_dia(incluir_hoje):
    """As pastas AAAA-MM-DD anteriores a hoje, da mais antiga para a mais nova.

    ⚠️ A pasta de HOJE fica de fora por padrao: ele ainda esta' postando dela, e
    levar um video que ele ia postar em seguida seria o unico dano real que este
    script pode causar. Nomes que nao sejam data (`estoque`, `videos terca
    feira`) nao entram — nem por engano, nem por ordenacao alfabetica.
    """
    hoje = date.today()
    achadas = []
    for nome in sorted(os.listdir(ORIGEM)):
        caminho = os.path.join(ORIGEM, nome)
        if not os.path.isdir(caminho) or not DIA.match(nome):
            continue
        if SO_ESTES_DIAS is not None and nome not in SO_ESTES_DIAS:
            continue
        try:
            d = datetime.strptime(nome, "%Y-%m-%d").date()
        except ValueError:
            continue
        if d > hoje:
            continue                      # data no futuro: defensivo
        if d == hoje and not incluir_hoje:
            continue
        achadas.append((nome, caminho))
    return achadas


def mover_um(origem, destino):
    """copia -> confere -> apaga a origem.

    ⛔ NUNCA apaga antes de confirmar. E copia para um `.parcial` primeiro: se o
    HD for desconectado no meio, o que fica no destino e' um arquivo com nome
    obviamente incompleto, e nao um mp4 truncado que passaria por bom.
    """
    tam = os.path.getsize(origem)
    parcial = destino + ".parcial"
    shutil.copy2(origem, parcial)
    if os.path.getsize(parcial) != tam:
        os.remove(parcial)
        raise IOError("copia saiu com tamanho diferente")
    os.replace(parcial, destino)
    os.remove(origem)
    return tam


def nome_no_destino(dia, arquivo):
    return "%s__%s" % (dia, arquivo)


def tarefa_agendada():
    """A tarefa existe no Agendador E esta' habilitada?

    ⛔ Existir nao basta: uma tarefa DESABILITADA continua aparecendo na consulta
    e nunca dispara. Sem checar o estado, a tela diria "agendado" para um worker
    que nao vai rodar nunca mais — que e' exatamente o defeito que ele quer
    enxergar.
    """
    try:
        r = subprocess.run(["schtasks", "/query", "/tn", TAREFA, "/fo", "list"],
                           capture_output=True, text=True, timeout=15)
        if r.returncode != 0:
            return False
        for linha in r.stdout.splitlines():
            if ":" not in linha:
                continue
            valor = linha.split(":", 1)[1].strip().lower()
            if linha.lower().startswith(("status", "estado")):
                return valor not in ("disabled", "desativado", "desabilitado")
        return True
    except Exception:                                  # noqa: BLE001
        return False


def medir_backlog(incluir_hoje):
    """Quanto esta' represado esperando o HD, por dia.

    ⚠️ MEDIDO EM TODA EXECUCAO, inclusive quando o HD esta' desconectado — e'
    justamente ai' que o numero interessa. Um painel de backlog que so' sabe
    contar quando tudo esta' bem nao serve para o dia em que nao esta'.
    """
    # ⛔⛔ O BACKLOG IGNORA O `--dias`. Medido em 2026-08-11: a primeira versao
    # reusava `pastas_de_dia()`, que respeita o filtro — entao uma passada
    # limitada a tres dias publicava `backlog: 0` com 32 sobras paradas nos dias
    # antigos. O painel existe justamente para mostrar o que NAO foi levado;
    # herdar o filtro de quem levou o transformava num espelho do proprio
    # sucesso.
    global SO_ESTES_DIAS
    guardado, SO_ESTES_DIAS = SO_ESTES_DIAS, None
    por_dia, total, tam = [], 0, 0
    for dia, caminho in pastas_de_dia(incluir_hoje):
        n = b = 0
        for a in os.listdir(caminho):
            if not SOBRA.match(a):
                continue
            n += 1
            try:
                b += os.path.getsize(os.path.join(caminho, a))
            except OSError:
                pass
        if n:
            por_dia.append({"dia": dia, "n": n, "gb": round(b / (1024 ** 3), 2)})
            total += n
            tam += b
    SO_ESTES_DIAS = guardado
    return por_dia, total, tam


def ler_estado():
    try:
        with open(ESTADO, encoding="utf-8") as f:
            return json.load(f)
    except Exception:                                  # noqa: BLE001
        return {}


def contar_destino():
    """Quantos videos ja' estao no HD.

    ⚠️ Conta o DESTINO de verdade, em vez de confiar no acumulado: o operador
    pode apagar, mover ou levar arquivos de la' por fora, e um contador que so'
    soma viraria mentira crescente.
    """
    try:
        return len([a for a in os.listdir(DESTINO) if a.lower().endswith(".mp4")])
    except OSError:
        return None


def gravar_estado(**campos):
    # ⭐ Contadores pedidos pelo operador: *"um contador de quantos videos foram
    # movidos e a quantidade atual de videos da pasta estoque"*. Sao numeros
    # DIFERENTES e os dois importam: o acumulado conta o trabalho do worker; o do
    # destino conta o que existe agora.
    antes = ler_estado()
    campos["movidos_total"] = (antes.get("movidos_total", 0)
                               + campos.get("movidos_ultima", 0))
    campos["gb_total"] = round(antes.get("gb_total", 0.0)
                               + campos.get("gb_ultima", 0.0), 2)
    campos["no_destino"] = contar_destino()
    campos["atualizado"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    campos["destino"] = DESTINO
    campos["log"] = LOG
    try:
        os.makedirs(ESTADO_DIR, exist_ok=True)
        tmp = ESTADO + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(campos, f, ensure_ascii=False, indent=1)
        os.replace(tmp, ESTADO)          # ⚠️ troca atomica: as interfaces leem
    except OSError as e:                 #    este arquivo a qualquer momento
        log("nao consegui gravar o estado: %s" % e, eco=False)


def rodar(dry, incluir_hoje):
    try:                       # mantem a trava fresca no modo servico
        os.utime(TRAVA, None)
    except OSError:
        pass
    if not os.path.isdir(ORIGEM):
        log("origem nao existe: %s" % ORIGEM)
        return 1

    # ⚠️ HD desconectado nao e' erro, e' o estado normal quando ele leva o HD.
    # O worker roda de hora em hora; reclamar seria ruido, entao apenas registra
    # e sai limpo — e as sobras continuam la', esperando.
    hd = os.path.isdir(os.path.splitdrive(DESTINO)[0] + "\\")
    if not hd:
        # ⚠️ HD desconectado nao e' erro, e' o estado normal quando ele leva o
        # HD. O worker roda de hora em hora; reclamar seria ruido. Mas o estado
        # E' GRAVADO com o backlog medido — e' o unico jeito de a tela dele
        # mostrar quanto esta' esperando enquanto o HD nao volta.
        por_dia, total, tam = medir_backlog(incluir_hoje)
        log("HD %s nao esta' conectado — %d sobra(s) esperando (%.2f GB)"
            % (os.path.splitdrive(DESTINO)[0], total, tam / (1024 ** 3)))
        gravar_estado(resultado="hd_desconectado", hd_conectado=False,
                      agendado=tarefa_agendada(), movidos_ultima=0,
                      gb_ultima=0.0, falhas_ultima=0,
                      backlog_arquivos=total,
                      backlog_gb=round(tam / (1024 ** 3), 2),
                      backlog_por_dia=por_dia)
        return 0
    if not dry:
        os.makedirs(DESTINO, exist_ok=True)

    movidos = pulados = falhas = 0
    bytes_movidos = 0
    for dia, caminho in pastas_de_dia(incluir_hoje):
        sobras = sorted(a for a in os.listdir(caminho) if SOBRA.match(a))
        if not sobras:
            continue
        log("%s: %d sobra(s)" % (dia, len(sobras)))
        for arquivo in sobras:
            org = os.path.join(caminho, arquivo)
            dst = os.path.join(DESTINO, nome_no_destino(dia, arquivo))

            # ⚠️ idempotente: rodando de hora em hora, o mesmo arquivo pode ser
            # visto de novo se a remocao falhou. Mesmo nome e mesmo tamanho no
            # destino = ja' foi; so' limpa a origem.
            if os.path.exists(dst):
                try:
                    if os.path.getsize(dst) == os.path.getsize(org):
                        if not dry:
                            os.remove(org)
                        log("   ja' estava no destino, origem limpa: %s" % arquivo)
                        pulados += 1
                        continue
                except OSError:
                    pass
                # mesmo nome, tamanho diferente: nao sobrescreve NUNCA
                base, ext = os.path.splitext(dst)
                n = 2
                while os.path.exists("%s (%d)%s" % (base, n, ext)):
                    n += 1
                dst = "%s (%d)%s" % (base, n, ext)
                log("   nome ocupado com tamanho diferente, virou: %s"
                    % os.path.basename(dst))

            if dry:
                log("   [ensaio] %s  ->  %s" % (arquivo, os.path.basename(dst)))
                movidos += 1
                continue
            try:
                bytes_movidos += mover_um(org, dst)
                movidos += 1
            except Exception as e:                     # noqa: BLE001
                log("   FALHOU %s: %s" % (arquivo, e))
                falhas += 1

    log("%s: %d movido(s), %d ja' estavam la', %d falha(s), %.2f GB"
        % ("ENSAIO" if dry else "fim", movidos, pulados, falhas,
           bytes_movidos / (1024 ** 3)))

    # ⭐ o backlog e' medido DEPOIS de mover: numa passada boa ele fica zero, e
    # e' esse zero que a tela usa para dizer "em dia".
    if not dry:
        por_dia, total, tam = medir_backlog(incluir_hoje)
        gravar_estado(resultado="falhas" if falhas else "ok", hd_conectado=True,
                      agendado=tarefa_agendada(), movidos_ultima=movidos,
                      gb_ultima=round(bytes_movidos / (1024 ** 3), 2),
                      falhas_ultima=falhas,
                      backlog_arquivos=total,
                      backlog_gb=round(tam / (1024 ** 3), 2),
                      backlog_por_dia=por_dia)
    return 0 if falhas == 0 else 2


def servico(intervalo_min=60, pulso_s=45):
    """Fica residente: bate pulso sempre, e faz a passada de hora em hora.

    ⛔⛔ POR QUE RESIDENTE E NAO AGENDADOR: registrar tarefa no Agendador exige
    ELEVACAO nesta maquina (`schtasks` e a API COM devolveram Access Denied sem
    admin). O `tarefa.xml` ao lado continua valendo para quem puder elevar — mas
    exigir um UAC toda vez que o worker for reinstalado nao serve para uma coisa
    que ele quer esquecer que existe.
    ⭐ E residente casa melhor com o que ele pediu ver: *"live e funcional"*. Um
    processo vivo tem pulso; uma tarefa agendada so' tem "ultima execucao", e uma
    tarefa quebrada fica indistinguivel de uma ociosa por ate' uma hora.

    ⚠️ O PULSO E' MAIS RAPIDO QUE A PASSADA — 45s contra 60min — de proposito. Se
    o unico sinal fosse a passada, um worker MORTO pareceria vivo por quase uma
    hora, que e' justamente o intervalo em que ele nao pode confiar na tela.
    """
    import time
    log("servico no ar (pulso %ds, passada a cada %dmin, pid %d)"
        % (pulso_s, intervalo_min, os.getpid()))
    proxima = 0.0
    while True:
        agora = time.time()
        try:
            if agora >= proxima:
                rodar(False, False)
                proxima = agora + intervalo_min * 60
            else:
                # ⚠️ pulso barato: nao varre disco, so' diz "estou aqui". Medir o
                # backlog a cada 45s seria ler a pasta inteira 80 vezes por hora
                # para um numero que muda uma vez por dia.
                # ⚠️ a trava e' renovada no PULSO, nao so' na passada: com 45s
                # entre pulsos e 10min de tolerancia, uma trava velha significa
                # de fato que o dono morreu.
                try:
                    os.utime(TRAVA, None)
                except OSError:
                    pass
                e = ler_estado()
                e["batimento"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                e["pid"] = os.getpid()
                e["modo"] = "servico"
                e["proxima_passada"] = datetime.fromtimestamp(proxima).strftime(
                    "%Y-%m-%d %H:%M:%S")
                try:
                    os.makedirs(ESTADO_DIR, exist_ok=True)
                    tmp = ESTADO + ".tmp"
                    with open(tmp, "w", encoding="utf-8") as f:
                        json.dump(e, f, ensure_ascii=False, indent=1)
                    os.replace(tmp, ESTADO)
                except OSError:
                    pass
        except Exception as ex:                        # noqa: BLE001
            # ⛔ o laco NUNCA morre por causa de uma passada ruim: um HD removido
            # no meio de uma copia nao pode derrubar o worker do dia inteiro.
            log("erro na passada: %s" % ex)
            proxima = time.time() + 5 * 60
        time.sleep(pulso_s)


def main():
    p = argparse.ArgumentParser(description="move as sobras do Veo Editor para o HD")
    p.add_argument("--servico", action="store_true",
                   help="fica residente: pulso a cada 45s, passada de hora em hora")
    p.add_argument("--dry-run", action="store_true",
                   help="mostra o que faria, sem mover nada")
    p.add_argument("--hoje", action="store_true",
                   help="inclui a pasta de HOJE (nao use no agendamento)")
    p.add_argument("--dias", nargs="+", metavar="AAAA-MM-DD",
                   help="roda SO' nestes dias — usado na primeira limpeza, que o "
                        "operador autorizou dia a dia")
    a = p.parse_args()
    global SO_ESTES_DIAS
    SO_ESTES_DIAS = set(a.dias) if a.dias else None

    # ⚠️ trava de instancia unica: duas execucoes ao mesmo tempo poderiam
    # disputar o mesmo arquivo no meio de uma copia.
    # ⛔ No modo servico a trava e' TOCADA a cada volta do laco (dentro do
    # `rodar`), senao a propria trava envelheceria e um segundo servico subiria.
    # ⛔⛔ SO' APAGA A TRAVA QUEM A CRIOU. Defeito medido em 2026-08-11, minutos
    # depois de escrever isto: duas instancias subiram quase juntas; a segunda
    # viu a trava e saiu — mas o `finally` dela APAGOU a trava da primeira, que
    # continuava viva. A porta ficou destrancada com o dono ainda dentro, e uma
    # terceira instancia entraria. Trava que qualquer um remove nao e' trava.
    minha = False
    if os.path.exists(TRAVA):
        try:
            idade = datetime.now().timestamp() - os.path.getmtime(TRAVA)
            if idade < 600:                 # o servico renova a cada passada
                log("outra execucao em andamento (trava de %d min) — saindo"
                    % (idade / 60))
                return 0
            log("trava velha (%.1f min), assumindo" % (idade / 60))
        except OSError:
            pass
    try:
        with open(TRAVA, "w") as f:
            f.write(str(os.getpid()))
        minha = True
    except OSError:
        pass
    try:
        if a.servico:
            return servico()
        return rodar(a.dry_run, a.hoje)
    except KeyboardInterrupt:
        log("encerrado a mao")
        return 0
    finally:
        if minha:
            try:
                os.remove(TRAVA)
            except OSError:
                pass


if __name__ == "__main__":
    sys.exit(main())
