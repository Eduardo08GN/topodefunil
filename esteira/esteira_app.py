# -*- coding: utf-8 -*-
"""ESTEIRA — o app offline. Video-fonte entra, prompts do Veo saem.

⛔ A UNICA etapa que precisa de modelo e' a 2, e ela acontece NO SEU CHAT: o
app te da' o pedido pronto e a folha de contato, voce cola la', e traz o JSON
de volta. O app nao fala com nenhuma API — nao ha' chave, nao ha' rede, nao ha'
token gasto aqui dentro.

⚠️ Isto NAO substitui os agentes. Motor gera LOTE de um angulo validado; esta
esteira gera UM video parecido com UM video. Escala repertorio, nao volume.
"""
import io
import json
import os

# ⛔ ANTES DE QUALQUER SUBPROCESSO: num build --windowed cada filho
# abre a propria janela de console no Windows. Inclusive os que o
# yt-dlp dispara, que ele nao esconde.
try:
    import sem_janela
    sem_janela.aplicar()
except Exception:  # noqa: BLE001
    pass
import subprocess
import sys
import threading
import tkinter as tk
from tkinter import filedialog, ttk

if getattr(sys, "frozen", False):
    AQUI = os.path.dirname(sys.executable)
else:
    AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

import gerar as G   # noqa: E402
import ler as L     # noqa: E402

BG, PANEL, LINE = "#15171a", "#1c1f24", "#2b3038"
# ⛔ A FAIXA DO CABECALHO E' A COR EXATA DO CANTO DO PNG DO DOOMGUY.
# Medido no proprio arquivo (`f0.png`, pixel 0,0): #0C0C0A. Sobre o `BG`
# do app (#15171A) aquele preto virava um RECORTE visivel em volta da
# carinha — foi o que o operador apontou. ⚠️ Recolorir o PNG nao servia:
# o desenho tem preto proprio no contorno e na sombra, entao trocar preto
# por BG comeria o traco. Mais barato e mais honesto e' o fundo ir ate'
# a imagem, e nao a imagem ate' o fundo.
CABEC = "#0c0c0a"
FG, MUTED, ACC = "#e6e8eb", "#8b929c", "#ff6a2b"
OK, ERRO = "#4ec86f", "#ff5c5c"
F_TIT = ("Segoe UI", 17, "bold")
F_UI = ("Segoe UI", 10)
F_MONO = ("Consolas", 9)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ESTEIRA by Eddie  ·  video-fonte -> prompts do Veo")
        self.configure(bg=BG)
        self.geometry("1180x820")
        self.video = None
        self.slug = None
        self._ui()

    # ------------------------------------------------------------------
    def _sec(self, pai, n, txt):
        f = tk.Frame(pai, bg=BG)
        f.pack(fill="x", pady=(14, 6))
        tk.Label(f, text=" %s " % n, bg=ACC, fg="#fff",
                 font=("Segoe UI", 10, "bold")).pack(side="left")
        tk.Label(f, text="  " + txt, bg=BG, fg=FG,
                 font=("Segoe UI", 11, "bold")).pack(side="left")
        return f

    def _bt(self, pai, txt, cmd, destaque=False, w=22):
        b = tk.Button(pai, text=txt, command=cmd, width=w, relief="flat",
                      bg=ACC if destaque else PANEL,
                      fg="#fff" if destaque else FG, font=F_UI,
                      activebackground=ACC, activeforeground="#fff",
                      cursor="hand2", pady=6, bd=0)
        return b

    def _doomguy(self, pai):
        """⚠️ ENFEITE NUNCA DERRUBA A FERRAMENTA — a regra e' copiada do AHK do
        Video Terminator, onde ela ja' esta' escrita. Se o Tk desta maquina nao
        souber ler PNG, `carregar()` devolve lista vazia, o `if` abaixo nao faz
        nada e o app abre igual. Nenhum caminho de erro passa por aqui.
        """
        try:
            import doomguy
            qs = doomguy.carregar(tk)
            if not qs:
                return
            lb = tk.Label(pai, bg=CABEC, bd=0)
            lb.pack(side="right", padx=(0, 22), pady=6)
            self._dg = qs                       # segura a referencia
            self._dg_i = 0

            def passo():
                self._dg_i = (self._dg_i + 1) % len(self._dg)
                lb.config(image=self._dg[self._dg_i])
                lb.after(doomguy.MS, passo)
            lb.config(image=qs[0])
            lb.after(doomguy.MS, passo)
        except Exception:  # noqa: BLE001
            pass

    def _ui(self):
        # ⭐ A faixa atravessa a janela inteira: meio-preto so' atras da
        # figura leria como remendo. Banda inteira le' como cabecalho.
        topo = tk.Frame(self, bg=CABEC)
        topo.pack(fill="x")
        self._doomguy(topo)
        esq_t = tk.Frame(topo, bg=CABEC)
        esq_t.pack(side="left", anchor="w", padx=18, pady=10)
        tk.Label(esq_t, text="ESTEIRA", bg=CABEC, fg=ACC,
                 font=F_TIT).pack(anchor="w")
        tk.Label(esq_t, text="um video-fonte entra · os prompts do Veo saem · "
                             "a unica etapa com modelo acontece no seu chat",
                 bg=CABEC, fg=MUTED, font=F_UI).pack(anchor="w")

        corpo = tk.Frame(self, bg=BG)
        corpo.pack(fill="both", expand=True, padx=18, pady=8)
        esq = tk.Frame(corpo, bg=BG, width=430)
        esq.pack(side="left", fill="y")
        esq.pack_propagate(False)
        dir_ = tk.Frame(corpo, bg=BG)
        dir_.pack(side="left", fill="both", expand=True, padx=(14, 0))

        # ---- 1 -------------------------------------------------------
        self._sec(esq, "1", "O VIDEO-FONTE")
        # ⭐ A URL vem PRIMEIRO porque e' o caminho que o operador mais usa:
        # ele acha o reel no navegador, copia o link e quer o pipeline andando.
        # Escolher arquivo continua ali para o que ja' esta' em disco.
        self.ent_url = tk.Entry(esq, bg=PANEL, fg=FG, font=F_UI, relief="flat",
                                insertbackground=FG)
        self.ent_url.pack(fill="x", ipady=6)
        self.ent_url.insert(0, "cole a URL do video aqui…")
        self.ent_url.bind("<FocusIn>", self._limpar_url)
        self.ent_url.bind("<Return>", lambda e: self.baixar())

        # ⛔⛔ COOKIE NUNCA E' COLADO. Ou o yt-dlp le' a sessao do navegador no
        # disco do operador, ou ele aponta um cookies.txt que ele mesmo
        # exportou. O valor nao passa por aqui, nao vai para log e nao entra em
        # commit. Em 2026-08-16 ele colou cookie de sessao numa conversa — este
        # campo existe para que o caminho FACIL seja tambem o seguro.
        lc = tk.Frame(esq, bg=BG)
        lc.pack(fill="x", pady=(6, 0))
        tk.Label(lc, text="cookies:", bg=BG, fg=MUTED, font=F_UI).pack(
            side="left")
        self.cb_cook = ttk.Combobox(
            lc, width=16, state="readonly",
            values=["não precisa", "do Chrome", "do Edge", "do Firefox",
                    "arquivo cookies.txt…"])
        self.cb_cook.set("não precisa")
        self.cb_cook.pack(side="left", padx=6)
        self.cb_cook.bind("<<ComboboxSelected>>", self._cookie_escolhido)
        self.lb_cook = tk.Label(lc, text="", bg=BG, fg=MUTED, font=F_UI)
        self.lb_cook.pack(side="left")
        self.cookie_arq = ""

        self._bt(esq, "BAIXAR E LER", self.baixar, True, 28).pack(
            anchor="w", pady=6)

        # ⭐ A BARRA E O PASSO. As etapas locais levam dezenas de segundos
        # (a transcricao e' a longa) e ate' agora o operador so' via uma
        # linha de texto mudando — sem nocao de quanto falta nem de qual
        # das quatro sub-etapas esta' rodando. A barra e' DETERMINADA em
        # todas: nenhuma delas finge andar.
        self.pb = ttk.Progressbar(esq, mode="determinate", maximum=100)
        self.pb.pack(fill="x")
        self.lb_passo = tk.Label(esq, text="", bg=BG, fg=MUTED, font=F_UI,
                                 anchor="w")
        self.lb_passo.pack(fill="x")

        self.lb_video = tk.Label(esq, text="nenhum video escolhido", bg=PANEL,
                                 fg=MUTED, font=F_UI, anchor="w", padx=10,
                                 pady=8, wraplength=400, justify="left")
        self.lb_video.pack(fill="x")
        lin = tk.Frame(esq, bg=BG)
        lin.pack(fill="x", pady=6)
        self._bt(lin, "escolher arquivo…", self.escolher, w=18).pack(
            side="left")
        self._bt(lin, "LER  (local, sem token)", self.ler, True, 22).pack(
            side="left", padx=6)

        self.lb_takes = tk.Label(esq, text="", bg=BG, fg=FG, font=F_MONO,
                                 anchor="w", justify="left")
        self.lb_takes.pack(fill="x")

        # ---- 2 -------------------------------------------------------
        self._sec(esq, "2", "A LEITURA — no seu chat")
        tk.Label(esq, text="Cole o pedido + a folha no chat. Traga o JSON de "
                           "volta e cole abaixo.",
                 bg=BG, fg=MUTED, font=F_UI, anchor="w",
                 wraplength=410, justify="left").pack(fill="x")
        lin2 = tk.Frame(esq, bg=BG)
        lin2.pack(fill="x", pady=6)
        self._bt(lin2, "copiar PEDIDO", self.copiar_pedido).pack(side="left")
        self._bt(lin2, "abrir a folha", self.abrir_folha).pack(
            side="left", padx=6)

        self.tx_mapa = tk.Text(esq, height=9, bg=PANEL, fg=FG, font=F_MONO,
                               insertbackground=FG, relief="flat", padx=8,
                               pady=6, wrap="word")
        self.tx_mapa.pack(fill="x")
        self._bt(esq, "salvar o mapa e conferir", self.salvar_mapa).pack(
            anchor="w", pady=6)

        # ---- 3 -------------------------------------------------------
        self._sec(esq, "3", "OS PROMPTS")
        lin3 = tk.Frame(esq, bg=BG)
        lin3.pack(fill="x")
        tk.Label(lin3, text="takes:", bg=BG, fg=MUTED, font=F_UI).pack(
            side="left")
        self.cb_takes = ttk.Combobox(lin3, values=["3", "2", "fonte"],
                                     width=7, state="readonly")
        # ⭐ O PADRAO E' 3, NAO `fonte`, e isso saiu da primeira rodada
        # real (2026-08-20): um reel de 38s da fonte devolveu DOZE takes,
        # o que com `fonte` viraria 12 IMAGE + 12 TAKE — vinte e quatro
        # prompts para UM video. O nosso funil so' tem dois formatos (2 e
        # 3 takes), entao `fonte` e' a opcao de ESTUDO e nao a de uso.
        self.cb_takes.set("3")
        self.cb_takes.pack(side="left", padx=6)
        self.v_modo = tk.StringVar(value="nosso")
        for t, v in (("nosso CTA", "nosso"), ("fiel a fonte", "fiel")):
            tk.Radiobutton(lin3, text=t, value=v, variable=self.v_modo, bg=BG,
                           fg=FG, selectcolor=PANEL, font=F_UI,
                           activebackground=BG, activeforeground=ACC).pack(
                side="left")
        self._bt(esq, "GERAR OS PROMPTS", self.gerar, True).pack(
            anchor="w", pady=8)

        self.lb_status = tk.Label(esq, text="", bg=BG, fg=MUTED, font=F_UI,
                                  anchor="w", wraplength=410, justify="left")
        self.lb_status.pack(fill="x")

        # ---- saida ---------------------------------------------------
        tk.Label(dir_, text="BLOCOS PARA A ADBATCH / VEO", bg=BG, fg=FG,
                 font=("Segoe UI", 11, "bold")).pack(anchor="w", pady=(14, 6))
        self.lst = tk.Listbox(dir_, bg=PANEL, fg=FG, font=F_MONO, height=8,
                              relief="flat", selectbackground=ACC,
                              highlightthickness=0)
        self.lst.pack(fill="x")
        self.lst.bind("<<ListboxSelect>>", self.mostrar)
        b = tk.Frame(dir_, bg=BG)
        b.pack(fill="x", pady=6)
        self._bt(b, "COPIAR ESTE BLOCO", self.copiar_bloco, True).pack(
            side="left")
        self._bt(b, "copiar TUDO", self.copiar_tudo).pack(side="left", padx=6)
        self.tx_out = tk.Text(dir_, bg=PANEL, fg=FG, font=F_MONO, relief="flat",
                              padx=10, pady=8, wrap="word",
                              insertbackground=FG)
        self.tx_out.pack(fill="both", expand=True)
        self.blocos = {}

    # ------------------------------------------------------------------
    def _passo(self, txt, pct=None):
        """Um lugar so' para mexer barra e rotulo — chamado das threads.

        ⚠️ `pct=None` deixa a barra como esta': serve para trocar so' o
        texto do passo sem a barra dar um pulo para tras.
        """
        try:
            if pct is not None:
                self.pb["value"] = max(0, min(100, pct))
            self.lb_passo.config(text=txt)
            self.update_idletasks()
        except Exception:  # noqa: BLE001
            pass

    def _st(self, txt, cor=MUTED):
        self.lb_status.config(text=txt, fg=cor)
        self.update_idletasks()

    def _limpar_url(self, *_):
        if self.ent_url.get().startswith("cole a URL"):
            self.ent_url.delete(0, "end")

    def _cookie_escolhido(self, *_):
        if self.cb_cook.get().startswith("arquivo"):
            p = filedialog.askopenfilename(
                title="o cookies.txt que VOCE exportou",
                filetypes=[("cookies", "*.txt"), ("todos", "*.*")])
            self.cookie_arq = p or ""
            self.lb_cook.config(
                text=("  " + os.path.basename(p)) if p else "  (nenhum)")
        else:
            self.cookie_arq = ""
            self.lb_cook.config(text="")

    def _modo_cookie(self):
        v = self.cb_cook.get()
        if v.startswith("arquivo"):
            return "arquivo", self.cookie_arq
        if v.startswith("do "):
            return "navegador", v.split()[-1]
        return "nao", ""

    def baixar(self):
        url = self.ent_url.get().strip()
        if not url or url.startswith("cole a URL"):
            return self._st("cole uma URL primeiro", ERRO)
        self._st("baixando…")
        threading.Thread(target=self._baixar_worker, args=(url,),
                         daemon=True).start()

    def _baixar_worker(self, url):
        try:
            import baixar as B
            modo, val = self._modo_cookie()
            dest = os.path.join(L.SAIDA, B.PASTA)
            def _prog(m):
                self._st(m)
                # ⭐ o texto do yt-dlp ja' traz a porcentagem: aproveita
                # em vez de inventar uma barra paralela.
                import re as _re
                g = _re.search(r"(\d+)%", m)
                self._passo("0/4 · baixando…",
                            int(g.group(1)) if g else None)
            p = B.baixar(url, dest, modo, val, progresso=_prog)
            self.video = p
            self.lb_video.config(text=p, fg=FG)
            self._st("baixado. Lendo…", OK)
            # ⭐ emenda direta na etapa 1: o operador pediu UM clique, nao dois.
            self._ler_worker()
        except Exception as e:  # noqa: BLE001
            self._st("nao baixou: %s" % e, ERRO)

    def escolher(self):
        p = filedialog.askopenfilename(
            title="o video-fonte",
            filetypes=[("video", "*.mp4 *.mov *.webm *.mkv"), ("todos", "*.*")])
        if p:
            self.video = p
            self.lb_video.config(text=p, fg=FG)

    def ler(self):
        if not self.video:
            return self._st("escolha um video primeiro", ERRO)
        self._st("lendo… (corte de cena, folha e transcricao — pode levar "
                 "um minuto)")
        threading.Thread(target=self._ler_worker, daemon=True).start()

    def _ler_worker(self):
        try:
            r = subprocess.run(
                [sys.executable, os.path.join(AQUI, "ler.py"), self.video]
                if not getattr(sys, "frozen", False) else None,
                capture_output=True, text=True) if False else None
            # ⛔ chamada DIRETA, sem subprocesso: congelado no `.exe` nao ha'
            # `python.exe` para chamar, e um subprocesso invisivel seria um
            # modo de falha que so' aparece na maquina do operador.
            slug = L._slug(self.video)
            dest = os.path.join(L.SAIDA, slug)
            os.makedirs(dest, exist_ok=True)
            self._passo("1/4 · medindo o video…", 4)
            dur = L.duracao(self.video)
            self._passo("2/4 · procurando os cortes de cena…", 12)
            cs = L.cortes(self.video)
            tks = L.takes(dur, cs)
            self._passo("3/4 · montando a folha (%d take(s))…" % len(tks), 25)
            L.folha(self.video, tks, dest)
            self._passo("4/4 · transcrevendo a fala…", 40)
            segs = L.transcrever(
                self.video, dur=dur,
                # ⭐ a transcricao ocupa a faixa de 40 a 98 da barra: e' a
                # etapa mais longa, entao e' a que merece mais regua.
                progresso=lambda p: self._passo(
                    "4/4 · transcrevendo a fala… %d%%" % p, 40 + p * 58 // 100))
            falas = L.alinhar(tks, segs)
            self._passo("pronto", 100)
            io.open(os.path.join(dest, "dossie.json"), "w",
                    encoding="utf-8").write(json.dumps(
                        {"slug": slug, "arquivo": self.video,
                         "duracao": round(dur, 2), "cortes": cs,
                         "takes": [{"i": i + 1, "t0": round(x, 2),
                                    "t1": round(y, 2), "fala": falas[i]}
                                   for i, (x, y) in enumerate(tks)],
                         "transcricao": segs}, indent=1, ensure_ascii=False))
            tabela = ("| take | de/ate | duracao |\n|---|---|---|\n"
                      + "\n".join("| take %d | %.1fs a %.1fs | %.1fs |"
                                  % (i + 1, x, y, y - x)
                                  for i, (x, y) in enumerate(tks)))
            blocos = "\n".join("**take %d** (%.1fs a %.1fs): %s"
                               % (i + 1, tks[i][0], tks[i][1],
                                  falas[i] or "_(sem fala)_")
                               for i in range(len(tks)))
            io.open(os.path.join(dest, "PEDIDO.md"), "w",
                    encoding="utf-8").write(L.PEDIDO.format(
                        slug=slug, n=len(tks), tabela=tabela,
                        q=len(tks) * 4, por=4, falas=blocos))
            self.slug = slug
            self.lb_takes.config(text="\n".join(
                "take %d   %5.1fs -> %5.1fs   %s"
                % (i + 1, x, y, (falas[i][:44] + "…") if len(falas[i]) > 44
                   else falas[i]) for i, (x, y) in enumerate(tks)))
            self._st("lido: %d take(s). Agora a etapa 2." % len(tks), OK)
        except Exception as e:  # noqa: BLE001
            self._st("falhou: %s" % e, ERRO)

    def _pasta(self):
        return os.path.join(L.SAIDA, self.slug) if self.slug else None

    def copiar_pedido(self):
        d = self._pasta()
        if not d:
            return self._st("leia um video antes", ERRO)
        self.clipboard_clear()
        self.clipboard_append(io.open(os.path.join(d, "PEDIDO.md"),
                                      encoding="utf-8").read())
        self._st("pedido copiado — cole no chat JUNTO com a folha.jpg", OK)

    def abrir_folha(self):
        """⛔ Botao que nao faz nada E nao diz nada e' o pior dos dois.
        Antes: sem video lido, `_pasta()` devolvia None e o clique morria
        em silencio; e se o `startfile` falhasse, o erro ia para um stderr
        que num build --windowed nao existe.
        """
        d = self._pasta()
        if not d:
            return self._st("leia um video antes — etapa 1", ERRO)
        f = os.path.join(d, "folha.jpg")
        if not os.path.exists(f):
            return self._st("a folha nao esta' em %s" % d, ERRO)
        try:
            os.startfile(f)  # noqa: S606
            self._st("folha aberta no visualizador de imagens", OK)
        except Exception as e:  # noqa: BLE001
            self._st("nao consegui abrir: %s" % e, ERRO)

    def salvar_mapa(self):
        d = self._pasta()
        if not d:
            return self._st("leia um video antes", ERRO)
        bruto = self.tx_mapa.get("1.0", "end").strip()
        # ⭐ o chat costuma devolver o JSON dentro de uma cerca ```json
        bruto = bruto.replace("```json", "").replace("```", "").strip()
        try:
            m = json.loads(bruto)
        except Exception as e:  # noqa: BLE001
            return self._st("nao e' JSON valido: %s" % e, ERRO)
        n = len(json.load(io.open(os.path.join(d, "dossie.json"),
                                  encoding="utf-8"))["takes"])
        if len(m.get("takes", [])) != n:
            return self._st("o mapa tem %d take(s) e o video tem %d"
                            % (len(m.get("takes", [])), n), ERRO)
        io.open(os.path.join(d, "mapa.json"), "w", encoding="utf-8").write(
            json.dumps(m, indent=1, ensure_ascii=False))
        self._st("mapa salvo, %d take(s) conferidos" % n, OK)

    def gerar(self):
        d = self._pasta()
        if not d or not os.path.exists(os.path.join(d, "mapa.json")):
            return self._st("falta o mapa.json — etapa 2", ERRO)
        mapa = json.load(io.open(os.path.join(d, "mapa.json"), encoding="utf-8"))
        dossie = json.load(io.open(os.path.join(d, "dossie.json"),
                                   encoding="utf-8"))
        self.blocos, avisos = G.montar(mapa, dossie, self.v_modo.get(),
                                       self.cb_takes.get())
        io.open(os.path.join(d, "prompts.txt"), "w", encoding="utf-8").write(
            "\n\n".join(self.blocos.values()))
        self.lst.delete(0, "end")
        for k, v in self.blocos.items():
            self.lst.insert("end", "%-16s %5d chars%s"
                            % (k, len(v), "  ESTOURA" if len(v) > G.TETO_BLOCO
                               else ""))
        self.lst.selection_set(0)
        self.mostrar()
        self._passo("prompts gerados", 100)
        self._st(("%d bloco(s) gerados" % len(self.blocos)) +
                 ((" · %d aviso(s): %s" % (len(avisos), " | ".join(avisos)))
                  if avisos else " · sem avisos"),
                 ERRO if avisos else OK)

    def mostrar(self, *_):
        s = self.lst.curselection()
        if not s:
            return
        k = list(self.blocos)[s[0]]
        self.tx_out.delete("1.0", "end")
        self.tx_out.insert("1.0", self.blocos[k])

    def copiar_bloco(self):
        s = self.lst.curselection()
        if not s:
            return
        self.clipboard_clear()
        self.clipboard_append(list(self.blocos.values())[s[0]])
        self._st("bloco copiado", OK)

    def copiar_tudo(self):
        if not self.blocos:
            return
        self.clipboard_clear()
        self.clipboard_append("\n\n".join(self.blocos.values()))
        self._st("todos os blocos copiados", OK)


if __name__ == "__main__":
    App().mainloop()
