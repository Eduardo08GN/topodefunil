"""Veo Editor By EDDIE — app desktop (tkinter, sem navegador).

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

VERSAO = "1.2-CTA"
GIF_TRABALHANDO = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               "trabalhando.gif")

# ⭐⭐ QUANTOS SLOTS DE TAKE MANUAL — 2026-08-21, ordem do operador: *"ajuste o
# editor para que ele seja capaz de editar 4 takes"*. O AMISH 16S nasceu com
# TAKE 01/04..04/04 (o take 1 nao cabia em 8s e virou dois), e o painel travava
# em tres: o quarto video nao tinha onde entrar.
# ⛔ Este numero e' o UNICO teto do editor. Todo o resto da cadeia ja' e'
# generico em quantidade de take — `preparar_takes` percorre a lista inteira,
# `concat` junta N, `_fim_takes_mudos` acha o ultimo mudo por DETECCAO de audio
# e `_inicio_take2` trabalha em proporcao. Medido em 21/08 com um lote sintetico
# de 4 takes (2 mudos + 2 com som): os quatro chegam ao arquivo final.
# ⚠️ Subir de novo (5, 6...) e' trocar este numero e mais nada NO PIPELINE.
# ⛔⛔ MAS O LAYOUT NAO E' GENERICO, e essa distincao custou um bug em 21/08:
# cada slot e' uma LINHA na coluna da esquerda, e as linhas empurram o que
# esta' embaixo. O rodape do painel ja' sumiu uma vez assim (as travas do DAY
# ficaram com altura 1 e invisiveis). Quem absorve a diferenca e' a lista da
# fila, que tem `expand=True` — por isso 8 cabe em 1080x790. Medido, nao
# suposto: com 8 slots o rodape continua na tela e a lista encolhe.
# ⭐ 2026-08-25: 4 -> 8, ordem do operador (*"ajuste o editor para caber ate 8
# takes"*).
N_MANUAL = 8

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
            messagebox.showerror("Veo Editor", "Pasta de entrada nao existe.", parent=self)
            return
        if not saida:
            messagebox.showerror("Veo Editor", "Informe a pasta de saida.", parent=self)
            return
        self._rodando = True
        self.bt.configure(state="disabled", text="Processando...")

        def rodar():
            try:
                processar_pasta(entrada, saida, model=esteira.CFG["model"],
                                margem=esteira.CFG["margem"],
                                musica=esteira.musica_atual(),
                                dias=esteira.dias_atual(),
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
        self.title(f"Veo Editor By EDDIE  v{VERSAO}")
        self.configure(bg=BG)
        # ⛔⛔ 680 NAO CABIA A SEGUNDA LINHA DO RODAPE (medido em 21/08).
        # A linha da `legenda DAY` foi empacotada ontem depois do rodape; com
        # a janela em 680 o `pack` nao sobrou altura nenhuma para ela e ela
        # saiu com ALTURA 1 — os quatro controles existiam, respondiam, eram
        # salvos no config e NUNCA apareceram na tela. Construir o botao e
        # nao olhar a janela e' a mesma falha de sempre: forma pronta, funcao
        # invisivel.
        # ⚠️ O numero e' verificado por medicao (`winfo_rooty` + altura da
        # linha), nao a olho — ver o teste no fim desta sessao.
        # ⭐⭐ 900, era 790 — 2026-08-26, quando o seletor 9:16 da legenda
        # entrou na coluna da direita. MEDIDO antes de escolher o numero:
        # com 790 o rodape inteiro (`legenda DAY`, `Pasta vigiada`,
        # `Pasta avulsa`) era empurrado para fora com altura 1, e o proprio
        # canvas saia espremido — 176px onde pedia 185, proporcao 0,60 no
        # lugar de 9:16. Mesmo defeito de 21/08 com as travas do DAY, e a
        # mesma licao: LAYOUT NAO E GENERICO, cada linha empurra o que esta
        # embaixo.
        # ⚠️ A tela dele mede 1920x1080; 900 deixa folga para a barra de
        # tarefas e para a barra de titulo.
        self.geometry("1080x900")
        self.minsize(900, 700)
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
        tk.Label(linha_titulo, text="Editor CTA FIXO", bg=BG, fg=AQUA, font=FH1).pack(side="left")
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
        self.lst_fila.pack(fill="both", expand=True, padx=12, pady=(0, 8))

        # ⭐ TAKES MANUAIS (2026-08-03) — subir os videos na mao, sem zip.
        # Mora aqui embaixo da fila de proposito: e' a mesma esteira, so' que
        # alimentada pela mao em vez do watcher.
        # ⭐ 2026-08-21: sao N_MANUAL slots (4), nao mais tres fixos.
        tk.Frame(sec_fila, bg=LINE, height=1).pack(fill="x", padx=12)
        cab_m = tk.Frame(sec_fila, bg=SURFACE)
        cab_m.pack(fill="x", padx=12, pady=(8, 4))
        tk.Label(cab_m, text="TAKES MANUAIS", bg=SURFACE, fg=MUT,
                 font=("Segoe UI", 8, "bold"), anchor="w").pack(side="left")
        tk.Label(cab_m, text="CORTAR", bg=SURFACE, fg=MUT,
                 font=("Segoe UI", 8, "bold"), anchor="e").pack(side="right")
        self.manual = [None] * N_MANUAL
        # ⭐⭐ CHAVINHA POR TAKE (2026-08-26) — ordem do operador: *"1 pequena
        # chavinha liga e desliga ao lado de cada take, para quando ela estiver
        # desligada o take em questao nao seja cortado"*.
        # ⛔ NASCE LIGADA: ligada = o comportamento de sempre. Chavinha que muda
        # o padrao faria todo lote antigo sair diferente sem ninguem pedir.
        self.corta = [True] * N_MANUAL
        self.lb_manual = []
        self.sw_manual = []
        for i in range(N_MANUAL):
            lin = tk.Frame(sec_fila, bg=SURFACE)
            lin.pack(fill="x", padx=12, pady=1)
            tk.Label(lin, text="%d" % (i + 1), bg=SURFACE2, fg=GOLD, font=FT,
                     width=2).pack(side="left", ipady=2)
            # ⚠️ a chavinha e' empacotada ANTES do botao de escolher, com
            # side="right": o botao vem depois com expand=True e ocupa o meio.
            # Invertendo a ordem o botao come a largura toda e a chavinha some.
            sw = tk.Button(lin, text="ON", command=lambda k=i: self._toggle_corte(k),
                           font=("Segoe UI", 8, "bold"), relief="flat", bd=0,
                           cursor="hand2", width=4, padx=0, pady=0,
                           bg=AQUA, fg="#04231f",
                           activebackground="#2adcc7", activeforeground="#04231f")
            sw.pack(side="right", padx=(6, 0), ipady=1)
            self.sw_manual.append(sw)
            b = tk.Button(lin, text="escolher...", command=lambda k=i: self._pick(k),
                          font=FT, bg=SURFACE, fg=DIM, relief="flat", bd=0,
                          cursor="hand2", anchor="w", padx=8,
                          activebackground=SURFACE2, activeforeground=INK)
            b.pack(side="left", fill="x", expand=True)
            self.lb_manual.append(b)
        acao_m = tk.Frame(sec_fila, bg=SURFACE)
        acao_m.pack(fill="x", padx=12, pady=(6, 12))
        self.bt_manual = botao(acao_m, "Editar agora", self._editar_manual,
                               primario=True)
        self.bt_manual.pack(side="left")
        self.bt_manual.configure(state="disabled")
        botao(acao_m, "Limpar", self._limpar_manual).pack(side="left", padx=(8, 0))

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

        # ===================================================================
        # ⭐⭐ O SELETOR 9:16 DA ALTURA DA LEGENDA — 2026-08-26
        # ===================================================================
        # Ordem do operador: *"crie um seletor com o tamanho 9:16 com uma regua
        # para mim selecionar a altura em que a legenda ira ficar (...) pois
        # cada video a legenda tem que ficar em uma altura diferente, e eu
        # preciso ajustar isso manualmente"*.
        #
        # ⛔ POR QUE UM RETANGULO 9:16 E NAO UM CAMPO DE NUMERO. O que ele
        # decide e' ESPACIAL — onde a legenda cai em relacao a cabeca e a
        # prova. Digitar `55` exige traduzir de cabeca porcentagem em posicao,
        # e e' onde o erro nasce. Arrastando uma linha dentro do quadro na
        # proporcao real, o que ele ve' e' o que sai.
        # ⭐ As DUAS marcas de referencia sao desenhadas junto e existem por
        # medicao, nao por enfeite: a faixa que a fonte usa (58%-63%, medida no
        # 2.mp4) e a linha do PIN do CTA (47%, medida nos frames do v001).
        # Sem elas ele arrastaria a legenda para cima do proprio CTA.
        sec_leg = tk.Frame(sec_pr, bg=SURFACE)
        sec_leg.pack(fill="x", padx=12, pady=(0, 12))
        tk.Frame(sec_leg, bg=LINE, height=1).pack(fill="x", pady=(0, 8))
        tk.Label(sec_leg, text="ALTURAS — ARRASTE AS LINHAS", bg=SURFACE, fg=MUT,
                 font=("Segoe UI", 8, "bold"), anchor="w").pack(fill="x")

        cx = tk.Frame(sec_leg, bg=SURFACE)
        cx.pack(fill="x", pady=(6, 0))
        # ⚠️ 104x185 e' 9:16 EXATO (185 * 9/16 = 104,06). Proporcao errada
        # aqui mentiria sobre onde a legenda cai no video de verdade.
        self.LEG_W, self.LEG_H = 104, 185
        self.cv_leg = tk.Canvas(cx, width=self.LEG_W, height=self.LEG_H,
                                bg="#05080c", highlightthickness=1,
                                highlightbackground=LINE, cursor="sb_v_double_arrow")
        self.cv_leg.pack(side="left")
        self.cv_leg.bind("<Button-1>", self._leg_pegar)
        self.cv_leg.bind("<B1-Motion>", self._leg_arrastar)
        self.cv_leg.bind("<ButtonRelease-1>", self._leg_soltar)

        lado = tk.Frame(cx, bg=SURFACE)
        lado.pack(side="left", fill="both", expand=True, padx=(10, 0))
        # \u2b50 DOIS numeros, um por linha, cada um na cor da sua linha no
        # quadro. Sem a cor, dois numeros empilhados nao dizem qual e' qual.
        self.lb_leg_pct = tk.Label(lado, text="legenda 60%", bg=SURFACE,
                                   fg=AQUA, font=("Segoe UI", 11, "bold"),
                                   anchor="w")
        self.lb_leg_pct.pack(fill="x")
        self.lb_cta_pct = tk.Label(lado, text="CTA 47%", bg=SURFACE,
                                   fg=GOLD, font=("Segoe UI", 11, "bold"),
                                   anchor="w")
        self.lb_cta_pct.pack(fill="x")
        self.bt_leg = botao(lado, "legenda", self._leg_alternar)
        self.bt_leg.pack(fill="x", pady=(8, 0))


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
                                     values=["base.en (rapido)", "small.en (equilibrado)",
                                             "medium.en (preciso, lento)"])
        self.cb_model.current(0)
        self.cb_model.pack(side="left", padx=(8, 20))
        self.cb_model.bind("<<ComboboxSelected>>", self._cfg)
        tk.Label(rodape, text="Silencio", bg=BG, fg=DIM, font=FT).pack(side="left")
        self.cb_margem = ttk.Combobox(rodape, style="Eddie.TCombobox", width=16,
                                      state="readonly", font=FT,
                                      values=["0.15s (seco)", "0.2s (padrao)", "0.35s (respiro)"])
        self.cb_margem.current(1)
        self.cb_margem.pack(side="left", padx=(8, 20))
        self.cb_margem.bind("<<ComboboxSelected>>", self._cfg)
        # ⭐ MUSICA dos takes mudos (2026-08-21, pedido para o AMISH 16S):
        # toca do inicio ate' o fim do penultimo take, cortada no tamanho do
        # trecho ja' editado. `travar` mantem a escolha entre sessoes.
        tk.Label(rodape, text="Musica", bg=BG, fg=DIM, font=FT).pack(side="left")
        self.cb_musica = ttk.Combobox(rodape, style="Eddie.TCombobox", width=22,
                                      state="readonly", font=FT,
                                      postcommand=self._musicas_refresh)
        self._musicas_refresh()
        self.cb_musica.pack(side="left", padx=(8, 6))
        self.cb_musica.bind("<<ComboboxSelected>>", self._cfg_musica)
        self.bt_travar = tk.Button(rodape, text="travar", font=FT, relief="flat",
                                   bd=0, cursor="hand2", padx=10, pady=4,
                                   command=self._alternar_trava_musica)
        self.bt_travar.pack(side="left", padx=(0, 20))
        self._pintar_trava_musica()

        botao(rodape, "Pasta avulsa...", lambda: ManualDialog(self)).pack(side="right")
        botao(rodape, "Pasta vigiada...", self._pasta_vigiada).pack(side="right", padx=(0, 8))

        # ⭐⭐ LEGENDA DE DIA nos takes MUDOS — 2026-08-21. O Veo nao consegue
        # fixar a legenda (some no meio em 8 de 8 takes medidos pelo
        # operador); aqui ela e' desenhada no mesmo pixel de todo frame.
        # ⛔ E' um botao GERAL: *"vai ser utilizado pra mais agentes tambem"*.
        linha2 = tk.Frame(self, bg=BG)
        linha2.pack(fill="x", padx=20, pady=(0, 12))
        self.bt_dia = tk.Button(linha2, text="legenda DAY", font=FT,
                                relief="flat", bd=0, cursor="hand2",
                                padx=12, pady=4, command=self._alternar_dia)
        self.bt_dia.pack(side="left", padx=(0, 10))
        tk.Label(linha2, text="dia do take 2", bg=BG, fg=DIM,
                 font=FT).pack(side="left")
        self.cb_dia = ttk.Combobox(
            linha2, style="Eddie.TCombobox", width=10, state="readonly",
            font=FT,
            values=["sorteio"] + [str(d) for d in
                                  range(esteira.DIA_MIN, esteira.DIA_MAX + 1)])
        self.cb_dia.pack(side="left", padx=(8, 16))
        self.cb_dia.bind("<<ComboboxSelected>>", self._cfg_dia)
        tk.Label(linha2, text="estilo", bg=BG, fg=DIM,
                 font=FT).pack(side="left")
        self.cb_dia_estilo = ttk.Combobox(
            linha2, style="Eddie.TCombobox", width=12, state="readonly",
            font=FT, values=["vermelho", "amarelo", "branco", "rosa", "roxo"])
        self.cb_dia_estilo.pack(side="left", padx=(8, 16))
        self.cb_dia_estilo.bind("<<ComboboxSelected>>", self._cfg_dia)
        tk.Label(linha2, text="cortar take mudo a", bg=BG, fg=DIM,
                 font=FT).pack(side="left")
        self.cb_dia_corte = ttk.Combobox(
            linha2, style="Eddie.TCombobox", width=12, state="readonly",
            font=FT, values=["nao cortar", "3s", "3.5s", "4s"])
        self.cb_dia_corte.pack(side="left", padx=(8, 16))
        self.cb_dia_corte.bind("<<ComboboxSelected>>", self._cfg_dia)
        # ⭐⭐ QUANTOS TAKES SAO MUDOS — 2026-08-21. `auto` mede pelo volume;
        # um numero DECLARA, e a declaracao ganha. Existe porque a medicao
        # ja' errou o lote inteiro: ver LIMIAR_MUDO no pipeline.
        tk.Label(linha2, text="takes mudos", bg=BG, fg=DIM,
                 font=FT).pack(side="left")
        self.cb_mudos = ttk.Combobox(
            linha2, style="Eddie.TCombobox", width=10, state="readonly",
            font=FT,
            values=["auto"] + [str(n) for n in range(0, N_MANUAL + 1)])
        self.cb_mudos.pack(side="left", padx=(8, 0))
        self.cb_mudos.bind("<<ComboboxSelected>>", self._cfg_dia)
        # ⭐⭐ CTA FIXO NO TOPO — religado em 2026-08-26. Ordem do operador:
        # *"fixe a palavra Comment Yes no topo do video no ultimo take de todo
        # video. Deixe um campo para mim conseguir escrever a palavra que quero
        # ficar no ultimo take para nao ter que ficar pedindo alteracao toda
        # hora"*.
        # ⛔ O pin existia desde sempre e foi DESLIGADO em 13/08 (`pin_cta`), nao
        # apagado — por isso religar foi um botao, e nao um recurso novo.
        # ⭐ A ENTRADA prefere o CTA FALADO: `captions.gerar_ass` procura
        # `comment <palavra>` no audio e so' cai para o comeco do ultimo take
        # quando nao acha. Foi a segunda metade do pedido dele (*"ou ao inves de
        # fixar no ultimo take inteiro, faca reconhecer o momento do CTA"*).
        # ⚠️ Campo VAZIO nao desliga nada: significa "usa a keyword que o audio
        # falou". Quem desliga e' o botao.
        self.bt_cta = tk.Button(linha2, text="CTA fixo", font=FT, relief="flat",
                                bd=0, cursor="hand2", padx=10, pady=4,
                                command=self._alternar_cta)
        self.bt_cta.pack(side="left", padx=(24, 6))
        tk.Label(linha2, text="palavra", bg=BG, fg=DIM, font=FT).pack(side="left")
        self.ent_cta = tk.Entry(linha2, width=10, font=FT, bg=SURFACE2, fg=INK,
                                relief="flat", bd=0, insertbackground=INK,
                                justify="center", disabledbackground=SURFACE,
                                disabledforeground=MUT)
        self.ent_cta.pack(side="left", padx=(8, 0), ipady=3)
        self.ent_cta.bind("<KeyRelease>", self._cfg_cta)
        self.ent_cta.bind("<FocusOut>", self._cfg_cta)
        # [LOCAL LUCAS] a roda do mouse TROCA o valor de um combobox readonly
        # e o operador ja' perdeu uma trava assim no painel do agente
        # (21/08). Roda inerte em todos os seletores deste rodape.
        for _cb in (self.cb_model, self.cb_margem, self.cb_musica,
                    self.cb_dia, self.cb_dia_estilo, self.cb_dia_corte,
                    self.cb_mudos):
            for _ev in ("<MouseWheel>", "<Button-4>", "<Button-5>"):
                _cb.bind(_ev, lambda _e: "break")
        self._sync_dia()

        self.opt = self.tk.call("tk", "windowingsystem")  # noqa: F841

    # ---------------- acoes ----------------

    def _cfg(self, _=None):
        esteira.CFG["model"] = self.cb_model.get().split(" ")[0]
        esteira.CFG["margem"] = self.cb_margem.get().split(" ")[0]
        esteira.salvar_cfg()

    SEM_MUSICA = "(sem musica)"

    def _musicas_refresh(self):
        """Rele a pasta a cada abertura do dropdown — musica nova entra sem
        reiniciar o app."""
        atual = getattr(self, "cb_musica", None) and self.cb_musica.get()
        vals = [self.SEM_MUSICA] + esteira.listar_musicas()
        self.cb_musica["values"] = vals
        alvo = esteira.CFG.get("musica") or self.SEM_MUSICA
        if atual != alvo and alvo in vals:
            self.cb_musica.set(alvo)
        elif not self.cb_musica.get():
            self.cb_musica.set(self.SEM_MUSICA)

    def _cfg_musica(self, _=None):
        v = self.cb_musica.get()
        esteira.CFG["musica"] = "" if v == self.SEM_MUSICA else v
        esteira.salvar_cfg()

    def _alternar_trava_musica(self):
        ligado = esteira.CFG.get("musica_travada") == "1"
        esteira.CFG["musica_travada"] = "" if ligado else "1"
        esteira.salvar_cfg()
        self._pintar_trava_musica()

    def _pintar_trava_musica(self):
        ligado = esteira.CFG.get("musica_travada") == "1"
        self.bt_travar.configure(
            bg=AQUA if ligado else SURFACE2,
            fg="#04231f" if ligado else DIM,
            activebackground=AQUA if ligado else SURFACE2,
            activeforeground="#04231f" if ligado else INK,
            text="travada" if ligado else "travar")

    _CORTES = {"nao cortar": "", "3s": "3", "3.5s": "3.5", "4s": "4"}

    # ===================================================================
    # ⭐⭐ O SELETOR DA ALTURA DA LEGENDA — 2026-08-26
    # ===================================================================
    _LEG_MIN, _LEG_MAX = 0.05, 0.90

    def _leg_pos(self):
        """A altura guardada, como fracao. Mesmo clamp do `esteira`."""
        t = (esteira.CFG.get("legenda_pos") or "60").strip().replace("%", "")
        try:
            v = float(t) / 100.0
        except ValueError:
            v = 0.60
        return max(self._LEG_MIN, min(self._LEG_MAX, v))

    def _cta_pos(self):
        """A altura do CTA, como fracao. Mesmo clamp da legenda."""
        t = (esteira.CFG.get("cta_pos") or "47").strip().replace("%", "")
        try:
            v = float(t) / 100.0
        except ValueError:
            v = 0.47
        return max(self._LEG_MIN, min(self._LEG_MAX, v))

    def _leg_pegar(self, e):
        """Qual das duas linhas o clique agarrou: a mais PROXIMA.

        \u26d4 Escolhe no BUTTON-1 e guarda ate' soltar. Decidir a cada
        `<B1-Motion>` faria a alca pular para a outra linha no instante em
        que as duas se cruzassem \u2014 e cruzar e' exatamente o que ele faz
        quando quer inverter a ordem delas.
        """
        v = e.y / float(self.LEG_H)
        self._leg_alvo = ("legenda_pos"
                          if abs(v - self._leg_pos()) <= abs(v - self._cta_pos())
                          else "cta_pos")
        self._leg_arrastar(e)

    def _leg_arrastar(self, e):
        """Arrasta a linha agarrada dentro do quadro 9:16."""
        v = e.y / float(self.LEG_H)
        v = max(self._LEG_MIN, min(self._LEG_MAX, v))
        esteira.CFG[getattr(self, "_leg_alvo", "legenda_pos")] = "%d" % round(v * 100)
        self._leg_pintar()

    def _leg_soltar(self, _e=None):
        # \u26a0\ufe0f grava no SOLTAR, nao a cada pixel do arrasto: salvar no
        # `<B1-Motion>` escreveria o config.json dezenas de vezes por segundo.
        esteira.salvar_cfg()

    def _leg_alternar(self):
        lig = esteira.CFG.get("legenda_ligada") == "1"
        esteira.CFG["legenda_ligada"] = "" if lig else "1"
        esteira.salvar_cfg()
        self._leg_pintar()

    def _leg_pintar(self):
        """Redesenha o quadro 9:16, as marcas de referencia e a linha."""
        c = self.cv_leg
        c.delete("all")
        W, H = self.LEG_W, self.LEG_H
        lig = esteira.CFG.get("legenda_ligada") == "1"
        v = self._leg_pos()

        # \u2b50 a faixa que a FONTE usa (58%-63%), medida no 2.mp4
        c.create_rectangle(1, H * 0.58, W - 1, H * 0.63,
                           fill="#0d1b16", outline="")
        # \u2b50\u2b50 A LINHA DO CTA VIROU ARRASTAVEL \u2014 2026-08-26, segunda ordem
        # dele: *"tambem quero poder controlar a altura do CTA"*. Ela ja'
        # estava desenhada como referencia; agora e' um controle.
        # \u26d4 AS DUAS NO MESMO QUADRO, e isso e' o ponto: a razao de existir a
        # marca do CTA era ele nao arrastar a legenda para cima dela. Num
        # segundo quadro, separado, a colisao voltaria a ser invisivel.
        vc = self._cta_pos()
        yc = H * vc
        cta_lig = esteira.CFG.get("cta_ligado") == "1"
        cor_cta = GOLD if cta_lig else "#5a4a2a"
        c.create_line(0, yc, W, yc, fill=cor_cta, width=2)
        alt_cta = max(5, int(H * 0.045))
        c.create_rectangle(6, yc, W - 6, yc + alt_cta, outline=cor_cta,
                           fill="#2b2412" if cta_lig else "")
        c.create_text(W - 4, yc - 6, text="CTA", anchor="e",
                      fill=cor_cta, font=("Segoe UI", 6, "bold"))

        y = H * v
        cor = AQUA if lig else "#3d4a52"
        c.create_line(0, y, W, y, fill=cor, width=2)
        # o bloco da legenda: uma linha a 0.045 da altura, como no `gerar_ass`
        alt = max(6, int(H * 0.055))
        c.create_rectangle(6, y, W - 6, y + alt, outline=cor,
                           fill="" if not lig else "#0b2b28")
        if not lig:
            c.create_text(W / 2, H / 2, text="DESLIGADA", fill="#5a6b73",
                          font=("Segoe UI", 8, "bold"))
        # \u26a0\ufe0f AVISA QUANDO AS DUAS SE ENCOSTAM. O bloco da legenda ocupa
        # ~5,5%% da altura e o do CTA ~4,5%%; abaixo de 8 pontos de distancia
        # eles se sobrepoem no video, e no quadro pequeno isso passa
        # despercebido.
        perto = abs(v - vc) < 0.08 and lig and cta_lig
        if perto:
            c.create_text(W / 2, H - 10, text="SOBREPOSTAS", fill=RED,
                          font=("Segoe UI", 7, "bold"))
        self.lb_leg_pct.configure(text="legenda %d%%" % round(v * 100),
                                  fg=RED if perto else (AQUA if lig else MUT))
        self.lb_cta_pct.configure(text="CTA %d%%" % round(vc * 100),
                                  fg=RED if perto else
                                  (GOLD if cta_lig else MUT))
        self.bt_leg.configure(
            bg=AQUA if lig else SURFACE2,
            fg="#04231f" if lig else DIM,
            activebackground=AQUA if lig else SURFACE2,
            activeforeground="#04231f" if lig else INK,
            text="legenda ligada" if lig else "legenda desligada")

    def _alternar_dia(self):
        lig = esteira.CFG.get("dia_ligado") == "1"
        esteira.CFG["dia_ligado"] = "" if lig else "1"
        esteira.salvar_cfg()
        self._pintar_dia()

    def _alternar_cta(self):
        lig = esteira.CFG.get("cta_ligado") == "1"
        esteira.CFG["cta_ligado"] = "" if lig else "1"
        esteira.salvar_cfg()
        self._pintar_cta()

    def _cfg_cta(self, _=None):
        # ⚠️ so' letras e numeros: a palavra vira texto QUEIMADO no video e
        # tambem e' procurada no audio. Espaco ou pontuacao nunca casaria com o
        # token do whisper, e o pin cairia calado no fallback.
        bruto = self.ent_cta.get().strip()
        limpo = "".join(c for c in bruto if c.isalnum())
        if limpo != bruto:
            self.ent_cta.delete(0, "end")
            self.ent_cta.insert(0, limpo)
        esteira.CFG["cta_palavra"] = limpo
        esteira.salvar_cfg()

    def _pintar_cta(self):
        lig = esteira.CFG.get("cta_ligado") == "1"
        self.bt_cta.configure(
            bg=AQUA if lig else SURFACE2,
            fg="#04231f" if lig else DIM,
            activebackground=AQUA if lig else SURFACE2,
            activeforeground="#04231f" if lig else INK,
            text="CTA fixo ligado" if lig else "CTA fixo")
        self.ent_cta.configure(state="normal" if lig else "disabled")

    def _cfg_dia(self, _=None):
        v = self.cb_dia.get()
        esteira.CFG["dia_num"] = "" if v == "sorteio" else v
        esteira.CFG["dia_estilo"] = self.cb_dia_estilo.get() or "vermelho"
        esteira.CFG["dia_corte"] = self._CORTES.get(self.cb_dia_corte.get(), "3")
        esteira.CFG["mudos"] = self.cb_mudos.get() or "auto"
        esteira.salvar_cfg()

    def _pintar_dia(self):
        lig = esteira.CFG.get("dia_ligado") == "1"
        self.bt_dia.configure(
            bg=AQUA if lig else SURFACE2,
            fg="#04231f" if lig else DIM,
            activebackground=AQUA if lig else SURFACE2,
            activeforeground="#04231f" if lig else INK,
            text="legenda DAY ligada" if lig else "legenda DAY")
        # ⛔ So' o DIA e o ESTILO seguem o botao. O corte do take mudo e o
        # seletor `takes mudos` NAO: eles governam a musica e o desvio do
        # auto-editor, que valem com a legenda desligada. Amarrados ao botao,
        # desligar a legenda apagava a musica junto, sem dizer nada.
        est = "readonly" if lig else "disabled"
        for cb in (self.cb_dia, self.cb_dia_estilo):
            cb.configure(state=est)

    def _sync_dia(self):
        self.cb_dia.set(esteira.CFG.get("dia_num") or "sorteio")
        self.cb_dia_estilo.set(esteira.CFG.get("dia_estilo") or "vermelho")
        atual = esteira.CFG.get("dia_corte") or ""
        rev = dict((v, k) for k, v in self._CORTES.items())
        self.cb_dia_corte.set(rev.get(atual, "3s"))
        self.cb_mudos.set(esteira.CFG.get("mudos") or "auto")
        self.ent_cta.delete(0, "end")
        self.ent_cta.insert(0, esteira.CFG.get("cta_palavra") or "")
        self._pintar_dia()
        self._pintar_cta()
        # ⭐ sem esta chamada o quadro 9:16 nasce VAZIO: o canvas so' e'
        # desenhado no `_leg_pintar`, e ate' o primeiro arrasto nao havia
        # nada na tela para arrastar.
        self._leg_pintar()

    def _sync_cfg(self):
        """Reflete o config.json carregado pela esteira nos combos."""
        for i, v in enumerate(self.cb_model["values"]):
            if v.split(" ")[0] == esteira.CFG["model"]:
                self.cb_model.current(i)
        for i, v in enumerate(self.cb_margem["values"]):
            if v.split(" ")[0] == esteira.CFG["margem"]:
                self.cb_margem.current(i)
        self._musicas_refresh()
        self._pintar_trava_musica()
        # ⛔ A LINHA DO `DAY` SO' PODE SER PREENCHIDA AQUI (2026-08-21).
        # `_montar()` roda ANTES de `esteira.iniciar()`, que e' quem le o
        # config.json — o `_sync_dia()` de la' pintava os defaults de memoria
        # e nao o que estava salvo. Efeito medido: `dia_ligado=1, dia=47,
        # estilo=amarelo` voltavam como DESLIGADO/sorteio/vermelho, e bastava
        # o operador encostar num combo para o `_cfg_dia` gravar por cima e
        # apagar a escolha dele de vez.
        self._sync_dia()

    def _pasta_vigiada(self):
        p = filedialog.askdirectory(
            parent=self, initialdir=esteira.pasta_vigiada(),
            title="Pasta vigiada — onde os zips adbatch*.zip sao capturados")
        if not p:
            return
        if not esteira.definir_pasta_vigiada(os.path.normpath(p)):
            messagebox.showerror("Veo Editor", "Pasta invalida.", parent=self)

    # ---------------- takes manuais ----------------

    def _pick(self, i):
        """Escolhe o video do slot i. Aceita multipla selecao: quem marca
        todos de uma vez preenche os slots dali pra baixo, em ordem.

        ⚠️ A ordem da selecao multipla e' a ORDEM DE NOME do dialogo, e os
        takes do Veo saem `..._1`, `..._2`: escolher os quatro de uma vez cai
        na ordem certa. O que passar do ultimo slot e' descartado em silencio
        de proposito — o alternativo seria empurrar take fora de ordem."""
        paths = filedialog.askopenfilenames(
            parent=self, title="Take %d" % (i + 1),
            filetypes=[("Videos", "*.mp4 *.mov *.mkv *.webm *.m4v *.avi"),
                       ("Todos", "*.*")])
        if not paths:
            return
        for k, p in enumerate(paths):
            if i + k < N_MANUAL:
                self.manual[i + k] = os.path.normpath(p)
        self._pintar_manual()

    def _toggle_corte(self, i):
        """Liga/desliga o corte do slot i. DESLIGADA = o take passa inteiro."""
        self.corta[i] = not self.corta[i]
        self._pintar_manual()

    def _limpar_manual(self):
        self.manual = [None] * N_MANUAL
        self.corta = [True] * N_MANUAL
        self._pintar_manual()

    def _pintar_manual(self):
        for i, b in enumerate(self.lb_manual):
            p = self.manual[i]
            nome = os.path.basename(p) if p else "escolher..."
            if len(nome) > 26:
                nome = nome[:12] + "..." + nome[-11:]
            b.configure(text=nome, fg=INK if p else DIM)
            liga = self.corta[i]
            sw = self.sw_manual[i]
            # slot vazio: chavinha apagada visualmente, mas ainda clicavel — da'
            # para pre-ajustar antes de escolher o video.
            if liga:
                sw.configure(text="ON", bg=AQUA if p else LINE,
                             fg="#04231f" if p else MUT,
                             activebackground="#2adcc7", activeforeground="#04231f")
            else:
                sw.configure(text="OFF", bg=SURFACE2, fg=RED if p else MUT,
                             activebackground=LINE, activeforeground=RED)
        # ⚠️ habilita com UM take, nao com tres: lote de 2 cenas existe, e
        # travar o botao obrigaria o operador a inventar um terceiro video.
        n = sum(1 for p in self.manual if p)
        self.bt_manual.configure(state="normal" if n else "disabled",
                                 text="Editar agora" if n <= 1
                                 else "Editar agora (%d takes)" % n)

    def _editar_manual(self):
        # ⛔ O INDICE DA CHAVINHA E' O DA LISTA COMPACTA, nao o do slot: se o
        # slot 1 esta' vazio e o 2 tem video com a chavinha desligada, o take e'
        # o de indice 0 para o pipeline. Mandar o numero do slot desligaria o
        # corte do take errado — em silencio.
        escolhidos, sem_corte = [], []
        for i, p in enumerate(self.manual):
            if not p:
                continue
            if not self.corta[i]:
                sem_corte.append(len(escolhidos))
            escolhidos.append(p)
        if not escolhidos:
            return
        try:
            nome = esteira.enfileirar_manual(escolhidos, sem_corte=sem_corte)
        except Exception as e:  # noqa: BLE001
            messagebox.showerror("Veo Editor", str(e), parent=self)
            return
        self._limpar_manual()
        messagebox.showinfo(
            "Veo Editor",
            "%d take(s) enviados como %s.\n\nA esteira pega em segundos e o "
            "resultado aparece em Prontos hoje." % (len(escolhidos), nome),
            parent=self)

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
            # um resumo dele. A versao antiga dizia 'nome nao comeca com
            # "adbatch"' — e o arquivo do operador se chamava
            # `adbatch_vertical_output.zip`, que COMECA com adbatch. Ele foi
            # conferir o nome no WinRAR, e o nome estava certo o tempo todo.
            # ⚠️ A v2.0 ja' tinha corrigido esta mesma mensagem em 2026-08-01,
            # depois de dois lotes parados. Chegou aqui com dois dias de atraso:
            # mensagem espelhada tambem envelhece em separado.
            vazio_fila = [f'{s["ignorados"]} zip(s) no Downloads IGNORADO(s):',
                          'esta esteira pega a familia AdBatch',
                          '(vertical 5, 4 e 3). Qualquer OUTRO .zip',
                          'e do Veo Editor 2.0 — abra ele, ou defina',
                          'uma Pasta vigiada dedicada (la qualquer',
                          '.zip e capturado).']
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


# PORTA PROPRIA (2026-08-08). Era 50573, a MESMA do editor original - e como
# a trava e um bind nessa porta, com o editor de sempre aberto esta versao
# achava que ela mesma ja estava rodando, tentava focar uma janela que nao
# existia e SAIA CALADA. O operador via so o CMD piscar. As duas versoes
# precisam coexistir: uma fila roda o editor de sempre, a outra a do CTA fixo.
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
        if not _focar_existente(f"Veo Editor By EDDIE  v{VERSAO}"):
            _r = tk.Tk()
            _r.withdraw()
            _r.attributes("-topmost", True)
            _r.lift()
            messagebox.showwarning(
                "Veo Editor",
                "O Veo Editor ja' esta' aberto, mas nao consegui trazer a\n"
                "janela para a frente. Procure na barra de tarefas.")
            _r.destroy()
        sys.exit(0)
    App().mainloop()

