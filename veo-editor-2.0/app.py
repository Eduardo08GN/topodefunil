"""Veo Editor 2.0 By EDDIE — app desktop (tkinter, sem navegador).

A v2.0 e o editor do pipeline SHORT: acelera o video para que os
24s da AdBatch Vertical 3 saiam com ~22s. Roda em paralelo ao v1.2,
com fila, historico e mutex proprios.

Janela unica com a esteira de producao: fila, editando agora (log ao vivo),
prontos hoje, erros com retry. O watcher liga junto com o app. Design system
da casa: fundo escuro, aqua, dourado, fill solido.
"""

import os
import queue
import socket
import sys
import threading
import subprocess

import tkinter as tk
from tkinter import ttk, filedialog, messagebox

import esteira
from pipeline import processar_pasta

VERSAO = "2.0"
GIF_TRABALHANDO = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               "trabalhando.gif")

# design system (mesmo do painel antigo)
BG = "#080b10"
SURFACE = "#101a22"
SURFACE2 = "#16222c"
LINE = "#22313c"
AQUA = "#18cbb6"
GOLD = "#ebc66a"
INK = "#ecf3f1"
DIM = "#a6b8b6"
MUT = "#657b7d"
RED = "#e0524a"
CONSOLE = "#05080c"

F = ("Segoe UI", 10)
FB = ("Segoe UI", 10, "bold")
FT = ("Segoe UI", 9)
FH1 = ("Segoe UI", 16, "bold")
FMONO = ("Consolas", 9)
FNUM = ("Segoe UI", 18, "bold")


class Gif(tk.Label):
    """GIF animado via PhotoImage frame a frame (nativo do tk, sem Pillow).
    Anima so quando ligado — o mascote trabalha quando a esteira trabalha."""

    def __init__(self, master, caminho, **kw):
        super().__init__(master, bg=SURFACE, bd=0, **kw)
        self.frames = []
        try:
            i = 0
            while True:
                self.frames.append(tk.PhotoImage(file=caminho, format=f"gif -index {i}"))
                i += 1
        except tk.TclError:
            pass  # acabaram os frames (ou arquivo ausente: fica sem mascote)
        if self.frames and self.frames[0].width() > 200:
            fator = max(1, round(self.frames[0].width() / 160))
            self.frames = [f.subsample(fator, fator) for f in self.frames]
        self._i = 0
        self._rodando = False

    def ligar(self):
        if not self.frames or self._rodando:
            return
        self._rodando = True
        self._anima()

    def desligar(self):
        self._rodando = False

    def _anima(self):
        if not self._rodando or not self.winfo_exists():
            return
        self.configure(image=self.frames[self._i])
        self._i = (self._i + 1) % len(self.frames)
        self.after(60, self._anima)


class Secao(tk.Frame):
    """Bloco com titulo em caps discreto, no padrao das colunas do painel."""

    def __init__(self, master, titulo, **kw):
        super().__init__(master, bg=SURFACE, highlightbackground=LINE,
                         highlightthickness=1, **kw)
        self.titulo = tk.Label(self, text=titulo.upper(), bg=SURFACE, fg=MUT,
                               font=("Segoe UI", 8, "bold"), anchor="w")
        self.titulo.pack(fill="x", padx=12, pady=(10, 6))


def botao(master, texto, cmd, primario=False, **kw):
    b = tk.Button(master, text=texto, command=cmd, relief="flat", cursor="hand2",
                  font=("Segoe UI", 9, "bold"), bd=0, padx=14, pady=6,
                  bg=AQUA if primario else SURFACE2,
                  fg="#04231f" if primario else INK,
                  activebackground="#2adcc7" if primario else LINE,
                  activeforeground="#04231f" if primario else INK, **kw)
    return b


class ManualDialog(tk.Toplevel):
    """Modo manual (pasta avulsa) — o legado, agora em janela propria."""

    def __init__(self, master):
        super().__init__(master)
        self.title("Processar pasta avulsa")
        self.configure(bg=BG)
        self.geometry("640x480")
        self.resizable(False, False)
        self._fila_log = queue.Queue()
        self._rodando = False

        tk.Label(self, text="Pasta de ENTRADA (takes ou .zip)", bg=BG, fg=DIM,
                 font=FT).pack(anchor="w", padx=20, pady=(18, 4))
        linha1 = tk.Frame(self, bg=BG)
        linha1.pack(fill="x", padx=20)
        self.entrada = tk.Entry(linha1, bg=SURFACE2, fg=INK, insertbackground=INK,
                                relief="flat", font=F)
        self.entrada.pack(side="left", fill="x", expand=True, ipady=6, padx=(0, 8))
        botao(linha1, "Procurar", lambda: self._procurar(self.entrada)).pack(side="right")

        tk.Label(self, text="Pasta de SAIDA", bg=BG, fg=DIM,
                 font=FT).pack(anchor="w", padx=20, pady=(12, 4))
        linha2 = tk.Frame(self, bg=BG)
        linha2.pack(fill="x", padx=20)
        self.saida = tk.Entry(linha2, bg=SURFACE2, fg=INK, insertbackground=INK,
                              relief="flat", font=F)
        self.saida.pack(side="left", fill="x", expand=True, ipady=6, padx=(0, 8))
        botao(linha2, "Procurar", lambda: self._procurar(self.saida)).pack(side="right")

        self.bt = botao(self, "Processar", self._processar, primario=True)
        self.bt.pack(fill="x", padx=20, pady=14)

        self.log = tk.Text(self, bg=CONSOLE, fg=DIM, relief="flat", font=FMONO,
                           state="disabled", wrap="word", padx=10, pady=8)
        self.log.pack(fill="both", expand=True, padx=20, pady=(0, 18))
        self.after(400, self._pump)

    def _procurar(self, entry):
        p = filedialog.askdirectory(parent=self)
        if p:
            entry.delete(0, "end")
            entry.insert(0, os.path.normpath(p))

    def _processar(self):
        if self._rodando:
            return
        entrada = self.entrada.get().strip().strip('"')
        saida = self.saida.get().strip().strip('"')
        if not os.path.isdir(entrada):
            messagebox.showerror("Veo Editor 2.0", "Pasta de entrada nao existe.", parent=self)
            return
        if not saida:
            messagebox.showerror("Veo Editor 2.0", "Informe a pasta de saida.", parent=self)
            return
        self._rodando = True
        self.bt.configure(state="disabled", text="Processando...")

        def rodar():
            try:
                processar_pasta(entrada, saida, model=esteira.CFG["model"],
                                lang=esteira.CFG.get("lang", "en"),
                                pin_cta=bool(esteira.CFG.get("pin_cta", True)),
                                palavra_cta=esteira.CFG.get("palavra_cta") or None,
                                margem=esteira.CFG["margem"],
                                log=self._fila_log.put)
                self._fila_log.put("CONCLUIDO.")
            except Exception as e:  # noqa: BLE001
                self._fila_log.put(f"ERRO: {e}")
            finally:
                self._fila_log.put(None)
        threading.Thread(target=rodar, daemon=True).start()

    def _pump(self):
        try:
            while True:
                msg = self._fila_log.get_nowait()
                if msg is None:
                    self._rodando = False
                    self.bt.configure(state="normal", text="Processar")
                    continue
                self.log.configure(state="normal")
                self.log.insert("end", str(msg) + "\n")
                self.log.see("end")
                self.log.configure(state="disabled")
        except queue.Empty:
            pass
        if self.winfo_exists():
            self.after(400, self._pump)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(f"Veo Editor 2.0 By EDDIE  v{VERSAO}")
        self.configure(bg=BG)
        self.geometry("1080x680")
        self.minsize(900, 560)
        self._cache = {}
        self._montar()
        esteira.iniciar()
        self._sync_cfg()
        self.after(300, self._refresh)

    # ---------------- layout ----------------

    def _montar(self):
        # header
        head = tk.Frame(self, bg=BG)
        head.pack(fill="x", padx=20, pady=(16, 2))
        t = tk.Frame(head, bg=BG)
        t.pack(side="left")
        linha_titulo = tk.Frame(t, bg=BG)
        linha_titulo.pack(anchor="w")
        tk.Label(linha_titulo, text="Veo ", bg=BG, fg=INK, font=FH1).pack(side="left")
        tk.Label(linha_titulo, text="Editor", bg=BG, fg=AQUA, font=FH1).pack(side="left")
        tk.Label(linha_titulo, text="  By EDDIE", bg=BG, fg=INK, font=FH1).pack(side="left")
        self.lb_watch = tk.Label(t, text="esteira iniciando...", bg=BG, fg=MUT,
                                 font=("Consolas", 8), anchor="w", justify="left")
        self.lb_watch.pack(anchor="w", pady=(2, 0))

        cont = tk.Frame(head, bg=BG)
        cont.pack(side="right")
        self.lb_n = tk.Label(cont, text="0", bg=BG, fg=GOLD, font=FNUM)
        self.lb_n.pack(side="left")
        tk.Label(cont, text=" pronto(s) hoje", bg=BG, fg=DIM, font=F).pack(side="left")

        # colunas
        corpo = tk.Frame(self, bg=BG)
        corpo.pack(fill="both", expand=True, padx=20, pady=(12, 0))
        corpo.columnconfigure(0, weight=2, uniform="c")
        corpo.columnconfigure(1, weight=4, uniform="c")
        corpo.columnconfigure(2, weight=3, uniform="c")
        corpo.rowconfigure(0, weight=3)
        corpo.rowconfigure(1, weight=1)

        # fila
        sec_fila = Secao(corpo, "Fila")
        sec_fila.grid(row=0, column=0, sticky="nsew", padx=(0, 12))
        self.lst_fila = tk.Listbox(sec_fila, bg=SURFACE, fg=INK, relief="flat",
                                   font=FT, highlightthickness=0, bd=0,
                                   selectbackground=SURFACE2, activestyle="none")
        self.lst_fila.pack(fill="both", expand=True, padx=12, pady=(0, 12))

        # editando agora
        sec_atual = Secao(corpo, "Editando agora")
        sec_atual.grid(row=0, column=1, sticky="nsew", padx=(0, 12))
        self.lb_etapa = tk.Label(sec_atual, text="Esteira ociosa.", bg=SURFACE,
                                 fg=GOLD, font=FB, anchor="w", wraplength=380,
                                 justify="left")
        self.lb_etapa.pack(fill="x", padx=12, pady=(0, 6))
        self.gif = Gif(sec_atual, GIF_TRABALHANDO)
        self._gif_visivel = False
        self.txt_log = tk.Text(sec_atual, bg=CONSOLE, fg=DIM, relief="flat",
                               font=FMONO, state="disabled", wrap="word",
                               padx=10, pady=8, highlightthickness=0)
        self.txt_log.pack(fill="both", expand=True, padx=12, pady=(0, 12))

        # prontos hoje
        sec_pr = Secao(corpo, "Prontos hoje")
        sec_pr.grid(row=0, column=2, sticky="nsew")
        st = ttk.Style(self)
        st.theme_use("clam")
        st.configure("Eddie.Treeview", background=SURFACE, fieldbackground=SURFACE,
                     foreground=INK, rowheight=26, font=FT, borderwidth=0,
                     bordercolor=LINE, lightcolor=SURFACE, darkcolor=SURFACE)
        st.configure("Eddie.Treeview.Heading", background=SURFACE2, foreground=DIM,
                     font=("Segoe UI", 8, "bold"), relief="flat")
        st.map("Eddie.Treeview", background=[("selected", SURFACE2)],
               foreground=[("selected", AQUA)])
        self.tree = ttk.Treeview(sec_pr, columns=("dur", "fator", "hora"),
                                 style="Eddie.Treeview", show="tree headings",
                                 selectmode="browse")
        self.tree.heading("#0", text="ARQUIVO", anchor="w")
        self.tree.heading("dur", text="DUR", anchor="e")
        self.tree.heading("fator", text="VEL", anchor="e")
        self.tree.heading("hora", text="HORA", anchor="e")
        self.tree.column("#0", width=150, stretch=True)
        self.tree.column("dur", width=48, anchor="e", stretch=False)
        self.tree.column("fator", width=58, anchor="e", stretch=False)
        self.tree.column("hora", width=48, anchor="e", stretch=False)
        self.tree.pack(fill="both", expand=True, padx=12, pady=(0, 8))
        self.tree.bind("<Double-1>", lambda e: self._ver())
        bts = tk.Frame(sec_pr, bg=SURFACE)
        bts.pack(fill="x", padx=12, pady=(0, 12))
        botao(bts, "Ver", self._ver, primario=True).pack(side="left", padx=(0, 8))
        botao(bts, "Abrir pasta", self._abrir_pasta).pack(side="left")

        # erros
        sec_err = Secao(corpo, "Erros")
        sec_err.titulo.configure(fg=RED)
        sec_err.grid(row=1, column=0, columnspan=3, sticky="nsew", pady=(12, 0))
        linha_err = tk.Frame(sec_err, bg=SURFACE)
        linha_err.pack(fill="both", expand=True, padx=12, pady=(0, 12))
        self.lst_err = tk.Listbox(linha_err, bg=SURFACE, fg=RED, relief="flat",
                                  font=FT, highlightthickness=0, bd=0, height=3,
                                  selectbackground=SURFACE2, activestyle="none")
        self.lst_err.pack(side="left", fill="both", expand=True, padx=(0, 10))
        botao(linha_err, "Tentar de novo", self._retry).pack(side="right", anchor="n")

        # rodape: opcoes + status
        # ⭐⭐ A LINHA DO CTA FIXO — reconstruida em 2026-09-01. O checkbox e o
        # campo `Palavra` decidem a palavra que fica queimada no topo do video
        # depois do CTA falado. ⛔ Ela e' FORCADA, nao detectada: as keywords
        # tambem sao ingredientes da copy, e o pin travava na primeira que o
        # Whisper ouvisse (medido: metade dos videos do CLEAN mandava comentar
        # `honey` em vez de `gelatin`). E fora do ingles a deteccao nao acha
        # nada, porque ela procura o literal `COMMENT`.
        linha_cta = tk.Frame(self, bg=BG)
        linha_cta.pack(fill="x", padx=20, pady=(10, 0))
        self.var_pin = tk.BooleanVar(value=True)
        self.chk_pin = tk.Checkbutton(
            linha_cta, variable=self.var_pin, command=self._cfg,
            bg=BG, fg=INK, selectcolor=SURFACE2, activebackground=BG,
            activeforeground=INK, font=FT, bd=0, highlightthickness=0,
            text='Escrever "COMMENT GELATIN" no topo do video')
        self.chk_pin.pack(side="left")
        tk.Label(linha_cta, text="Palavra", bg=BG, fg=DIM,
                 font=FT).pack(side="left", padx=(20, 6))
        self.ent_cta = tk.Entry(linha_cta, bg=SURFACE2, fg=INK, font=FT,
                                relief="flat", width=14,
                                insertbackground=INK)
        self.ent_cta.pack(side="left", ipady=3)
        self.ent_cta.bind("<KeyRelease>", self._cfg)
        self.ent_cta.bind("<FocusOut>", self._cfg)

        rodape = tk.Frame(self, bg=BG)
        rodape.pack(fill="x", padx=20, pady=(10, 14))
        tk.Label(rodape, text="Precisao", bg=BG, fg=DIM, font=FT).pack(side="left")
        st.configure("Eddie.TCombobox", fieldbackground=SURFACE2, background=SURFACE2,
                     foreground=INK, arrowcolor=DIM, borderwidth=0,
                     selectbackground=SURFACE2, selectforeground=INK)
        st.map("Eddie.TCombobox",
               fieldbackground=[("readonly", SURFACE2)],
               foreground=[("readonly", INK)],
               background=[("readonly", SURFACE2)],
               selectbackground=[("readonly", SURFACE2)],
               selectforeground=[("readonly", INK)])
        self.option_add("*TCombobox*Listbox.background", SURFACE2)
        self.option_add("*TCombobox*Listbox.foreground", INK)
        self.option_add("*TCombobox*Listbox.selectBackground", AQUA)
        self.option_add("*TCombobox*Listbox.selectForeground", "#04231f")
        self.option_add("*TCombobox*Listbox.font", FT)
        self.cb_model = ttk.Combobox(rodape, style="Eddie.TCombobox", width=22,
                                     state="readonly", font=FT,
                                     values=["base (rapido)", "small (equilibrado)",
                                             "medium (preciso, lento)"])
        self.cb_model.current(0)
        self.cb_model.pack(side="left", padx=(8, 20))
        self.cb_model.bind("<<ComboboxSelected>>", self._cfg)
        # ⭐⭐ IDIOMA DO AUDIO — porte do Veo Editor CTA FIXO, 2026-09-01.
        # Ate' hoje este editor so' entendia ingles: os tres modelos do menu
        # eram `.en` e o `lang` nunca saia de "en". Audio alemao ou frances nao
        # dava erro — saia transcrito foneticamente como ingles, com cara de
        # legenda pronta. Foi assim que um video alemao do operador saiu
        # legendado com "I was born in the middle of the school".
        # ⛔ O SUFIXO `.en` SUMIU DOS ROTULOS de proposito: quem o poe e tira e'
        # o `captions.modelo_para`, a partir DESTE combo. Escolher modelo e
        # idioma em separado permitia a combinacao quebrada.
        tk.Label(rodape, text="Idioma", bg=BG, fg=DIM, font=FT).pack(side="left")
        self._IDIOMAS = [("en", "Ingles"), ("de", "Alemao"), ("fr", "Frances")]
        self.cb_lang = ttk.Combobox(rodape, style="Eddie.TCombobox", width=10,
                                    state="readonly", font=FT,
                                    values=[r for _c, r in self._IDIOMAS])
        self.cb_lang.current(0)
        self.cb_lang.pack(side="left", padx=(8, 20))
        self.cb_lang.bind("<<ComboboxSelected>>", self._cfg)
        tk.Label(rodape, text="Silencio", bg=BG, fg=DIM, font=FT).pack(side="left")
        self.cb_margem = ttk.Combobox(rodape, style="Eddie.TCombobox", width=16,
                                      state="readonly", font=FT,
                                      values=["0.15s (seco)", "0.2s (padrao)", "0.35s (respiro)"])
        self.cb_margem.current(1)
        self.cb_margem.pack(side="left", padx=(8, 20))
        self.cb_margem.bind("<<ComboboxSelected>>", self._cfg)
        botao(rodape, "Pasta avulsa...", lambda: ManualDialog(self)).pack(side="right")
        botao(rodape, "Pasta vigiada...", self._pasta_vigiada).pack(side="right", padx=(0, 8))

        self.opt = self.tk.call("tk", "windowingsystem")  # noqa: F841

    # ---------------- acoes ----------------

    # ⛔⛔ MEDIDO no audio alemao do operador (2026-09-01): com `base`, o
    # Whisper devolve `Hohe SKORTISOL` no lugar de `Hohes Cortisol` e `Wenn EIN
    # Herz` no lugar de `dein Herz` — erra o NOME DO MECANISMO e mata o
    # vocativo. Com `small` sai correto. Em ingles `base` e' um rapido honesto;
    # fora do ingles ele e' um gerador de ruido com cara de legenda pronta, e
    # legenda queimada nao tem revisao depois.
    MODELO_MINIMO_FORA_DO_INGLES = "small"

    def _rotulo_pin(self):
        """O rotulo do checkbox mostra a palavra REAL — texto que mente sobre
        o proprio controle e' pior que rotulo generico."""
        p = (self.ent_cta.get() or "").strip().upper() or "..."
        self.chk_pin.configure(text='Escrever "COMMENT %s" no topo do video' % p)

    def _cfg(self, _=None):
        esteira.CFG["pin_cta"] = bool(self.var_pin.get())
        esteira.CFG["palavra_cta"] = (self.ent_cta.get() or "").strip().upper()
        self._rotulo_pin()
        esteira.CFG["model"] = self.cb_model.get().split(" ")[0]
        esteira.CFG["margem"] = self.cb_margem.get().split(" ")[0]
        rot = self.cb_lang.get()
        lang_antes = esteira.CFG.get("lang", "en")
        for cod, r in self._IDIOMAS:
            if r == rot:
                esteira.CFG["lang"] = cod
                break
        # ⚠️ So' quando o IDIOMA MUDA. Depois disso, escolher `base` com alemao
        # selecionado e' decisao do operador e fica valendo — botao que desfaz
        # a escolha do dono a cada clique e' pior que botao nenhum.
        if (esteira.CFG.get("lang") != lang_antes
                and esteira.CFG.get("lang") != "en"
                and esteira.CFG.get("model") == "base"):
            self._subir_modelo()
        esteira.salvar_cfg()

    def _subir_modelo(self):
        """Sobe `base` para `small` ao sair do ingles, e DIZ por que."""
        for i, v in enumerate(self.cb_model.cget("values")):
            if v.startswith(self.MODELO_MINIMO_FORA_DO_INGLES):
                self.cb_model.current(i)
                esteira.CFG["model"] = self.MODELO_MINIMO_FORA_DO_INGLES
                break
        try:
            self.lst_err.insert(
                0, "precisao subiu para `small`: fora do ingles o `base` "
                   "escreve o mecanismo errado (medido: Skortisol por "
                   "Cortisol). Pode voltar para base se quiser.")
        except Exception:                                   # noqa: BLE001
            pass

    def _sync_cfg(self):
        """Reflete o config.json carregado pela esteira nos combos."""
        # ⚠️ `.replace(".en","")`: o `config.json` que ja' esta' na maquina do
        # operador guarda `base.en`, do tempo em que o sufixo morava no rotulo.
        # Sem isto o combo nao casaria com nada, ficaria no indice 0 em
        # silencio, e a tela mentiria sobre o que esta' selecionado.
        salvo = (esteira.CFG.get("model") or "base").replace(".en", "")
        for i, v in enumerate(self.cb_model["values"]):
            if v.split(" ")[0] == salvo:
                self.cb_model.current(i)
        for i, (cod, _rot) in enumerate(self._IDIOMAS):
            if cod == esteira.CFG.get("lang", "en"):
                self.cb_lang.current(i)
        self.var_pin.set(bool(esteira.CFG.get("pin_cta", True)))
        self.ent_cta.delete(0, "end")
        self.ent_cta.insert(0, esteira.CFG.get("palavra_cta") or "GELATIN")
        self._rotulo_pin()
        for i, v in enumerate(self.cb_margem["values"]):
            if v.split(" ")[0] == esteira.CFG["margem"]:
                self.cb_margem.current(i)

    def _pasta_vigiada(self):
        p = filedialog.askdirectory(
            parent=self, initialdir=esteira.pasta_vigiada(),
            title="Pasta vigiada — onde os zips adbatch*.zip sao capturados")
        if not p:
            return
        if not esteira.definir_pasta_vigiada(os.path.normpath(p)):
            messagebox.showerror("Veo Editor 2.0", "Pasta invalida.", parent=self)

    def _ver(self):
        sel = self.tree.selection()
        if not sel:
            return
        _, data, arquivo = sel[0].split("|", 2)
        p = os.path.join(esteira.D_PRONTOS, data, arquivo)
        if os.path.isfile(p):
            os.startfile(p)  # noqa: S606 — player padrao do Windows

    def _abrir_pasta(self):
        try:
            subprocess.Popen(["explorer", esteira.D_PRONTOS])
        except OSError:
            pass

    def _retry(self):
        sel = self.lst_err.curselection()
        if not sel:
            return
        nome = self.lst_err.get(sel[0]).split("  —  ")[0]
        esteira.tentar_de_novo(nome)

    # ---------------- refresh ----------------

    def _set_lista(self, chave, lst, itens, vazio):
        if isinstance(vazio, str):
            vazio = [vazio]
        mostra = itens if itens else vazio
        if self._cache.get(chave) == mostra:
            return
        self._cache[chave] = mostra
        lst.delete(0, "end")
        for i in mostra:
            lst.insert("end", i)
        if not itens:
            for j in range(len(mostra)):
                lst.itemconfig(j, fg=MUT)

    def _refresh(self):
        s = esteira.status()

        self.lb_watch.configure(text="vigiando:  " + "\n           ".join(s["watch"]))
        self.lb_n.configure(text=str(len(s["prontos"])))

        vazio_fila = "Nenhum zip aguardando. Baixe um lote no Flow."
        if s.get("ignorados"):
            # ⚠️ O aviso enuncia o filtro REAL (esteira.PADRAO_DOWNLOADS), nao
            # um resumo dele: dizer 'nao comeca com "adbatch"' custou dois
            # lotes parados em 2026-08-01 — os arquivos comecavam com
            # "adbatch". Desde a inversao, o unico .zip que esta esteira
            # recusa e' o da Vertical 5/4, e o aviso diz para onde ele vai.
            vazio_fila = [f'{s["ignorados"]} zip(s) no Downloads IGNORADO(s):',
                          'sao da AdBatch Vertical 5/4',
                          '(adbatch_vertical_5*, _4, _output, adbatch_lote*).',
                          'Quem edita esses e o Veo Editor v1.2 —',
                          'abra ele. Qualquer OUTRO .zip que cair',
                          'no Downloads esta esteira pega sozinha.']
        self._set_lista("fila", self.lst_fila, s["pendentes"], vazio_fila)

        # ⭐ O mascote acende em TRES estados, nao so' no processamento: o zip
        # visto e estabilizando, o enfileirado e o em edicao. Sem os dois
        # primeiros o painel fica dizendo "ociosa" por ate' 5 segundos depois
        # do download terminar — a janela em que o operador olha e acha que
        # quebrou. Ordem do operador, 2026-07-31.
        chegando = s.get("chegando") or []
        if s["atual"]:
            self.lb_etapa.configure(text=f'{s["atual"]["zip"]}  —  {s["atual"]["etapa"]}')
            log = "\n".join(s["atual"]["log"])
        elif chegando:
            self.lb_etapa.configure(text=f"{chegando[0]}  —  chegando...")
            log = ""
        elif s["pendentes"]:
            self.lb_etapa.configure(text=f"{s['pendentes'][0]}  —  na fila, comecando...")
            log = ""
        else:
            self.lb_etapa.configure(text="Esteira ociosa.")
            log = ""

        ocupada = bool(s["atual"] or chegando or s["pendentes"])
        if ocupada and not self._gif_visivel:
            self.gif.pack(before=self.txt_log, pady=(0, 6))
            self.gif.ligar()
            self._gif_visivel = True
        elif not ocupada and self._gif_visivel:
            self.gif.desligar()
            self.gif.pack_forget()
            self._gif_visivel = False
        if self._cache.get("log") != log:
            self._cache["log"] = log
            self.txt_log.configure(state="normal")
            self.txt_log.delete("1.0", "end")
            self.txt_log.insert("1.0", log)
            self.txt_log.see("end")
            self.txt_log.configure(state="disabled")

        chave_pr = [(p["data"], p["arquivo"], p["duracao"], p["fator"], p["hora"])
                    for p in s["prontos"]]
        if self._cache.get("prontos") != chave_pr:
            self._cache["prontos"] = chave_pr
            self.tree.delete(*self.tree.get_children())
            # ⛔ o indice na frente torna o iid unico por construcao: nome
            # repetido no historico estourava "Item already exists" e a tabela
            # parava ali, mostrando menos linhas que o contador.
            for i, p in enumerate(reversed(s["prontos"])):
                iid = f'{i}|{p["data"]}|{p["arquivo"]}'
                self.tree.insert("", "end", iid=iid, text=p["arquivo"],
                                 values=(f'{p["duracao"]:.0f}s',
                                         f'{p["fator"]:.3f}x', p["hora"]))

        erros = [f'{e["zip"]}  —  {e["erro"]}' for e in s["erros"]]
        self._set_lista("erros", self.lst_err, erros, "Nenhum erro.")

        self.after(1200, self._refresh)


# ⚠️ Porta PROPRIA. Com a do v1.2 (50573) a v2.0 se recusaria a abrir
# enquanto o v1.2 estivesse rodando — e a ideia e' que os dois rodem juntos.
PORTA_TRAVA = 50574   # so' serve de mutex; nada trafega por ela


def _instancia_unica():
    """Impede duas esteiras rodando ao mesmo tempo.

    Duas instancias sobem DOIS watchers e DOIS workers na mesma pasta: elas
    disputam o zip no shutil.move, e a que perde a corrida nunca seta
    ESTADO["atual"] — entao nunca mostra o mascote nem conta o video no painel,
    parecendo travada. Aconteceu em producao 2026-07-30 (o app aberto pelo
    pythonw do .venv e pelo do sistema ao mesmo tempo).

    Devolve o socket quando conseguiu a trava (guardar a referencia viva
    enquanto o app roda) ou None quando ja' existe outra instancia.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind(("127.0.0.1", PORTA_TRAVA))
        s.listen(1)
    except OSError:
        s.close()
        return None
    return s


def _focar_existente(titulo):
    """Traz a janela ja' aberta para a frente. True se conseguiu.

    ctypes puro, sem dependencia: FindWindowW acha pelo titulo exato, o mesmo
    que a App() seta. SW_RESTORE (9) desminimiza antes de trazer para frente,
    senao a janela minimizada volta ao foco mas continua na barra de tarefas.
    """
    try:
        import ctypes
        u = ctypes.windll.user32
        h = u.FindWindowW(None, titulo)
        if not h:
            return False
        u.ShowWindow(h, 9)
        u.SetForegroundWindow(h)
        return True
    except Exception:                                        # noqa: BLE001
        return False


if __name__ == "__main__":
    _trava = _instancia_unica()
    if _trava is None:
        # ⭐ Foca a janela que ja' esta' aberta e sai calado. O aviso
        # abaixo e' ULTIMO recurso: se a janela nao for achada, o
        # operador precisa saber por que o clique nao fez nada —
        # sumico silencioso e' pior que um alerta.
        if not _focar_existente(f"Veo Editor 2.0 By EDDIE  v{VERSAO}"):
            _r = tk.Tk()
            _r.withdraw()
            _r.attributes("-topmost", True)
            _r.lift()
            messagebox.showwarning(
                "Veo Editor 2.0",
                "O Veo Editor 2.0 ja' esta' aberto, mas nao consegui trazer a\n"
                "janela para a frente. Procure na barra de tarefas.")
            _r.destroy()
        sys.exit(0)
    App().mainloop()
