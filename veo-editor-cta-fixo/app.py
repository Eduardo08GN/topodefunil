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
import tempfile

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, colorchooser

import esteira
import pipeline
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
                                lang=esteira.CFG.get("lang", "en"),
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
        # 930, era 900 -- 2026-08-28, quando o combo de DURACAO EM TAKES
        # entrou na coluna do seletor. MEDIDO em A/B, com e sem o combo:
        # a ultima linha do rodape (legenda DAY, estilo, takes mudos, CTA
        # fixo, palavra) caiu de h=21 para h=8 -- esmagada, ilegivel, e sem
        # erro nenhum. Terceira vez que este layout cobra o mesmo pedagio
        # (21/08 nas travas do DAY, 26/08 no seletor, hoje aqui).
        # A LICAO QUE FALTAVA NO MEU TESTE: ele so' olhava o INICIO do
        # widget (y < 0 ou y > altura) e por isso deu 'zero problemas' com o
        # rodape a 8 px de altura. Widget esmagado comeca dentro da janela.
        # Quem acusa e' medir onde ele TERMINA, e a altura contra a de antes.
        # 946, era 930 -- 2026-08-29, quando a linha da LEGENDA FIXA entrou
        # embaixo do quadro 9:16. MEDIDO em A/B: com 930 os dois botoes do
        # rodape (legenda DAY e CTA fixo) caiam de h=28 para h=22 -- nao
        # sumiam, so' perdiam o respiro. Com 946 voltam aos 28.
        # TETO REAL DA TELA DELE: 1920x1080 com area util de 1017 px, menos
        # ~31 da barra de titulo = 986. Estamos a 40 px do limite; a proxima
        # linha que entrar aqui vai ter de PAGAR o espaco tirando outra.
        self.geometry("1080x946")
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
        tk.Label(sec_leg, text="ALTURAS E ALVO — ARRASTE NO QUADRO", bg=SURFACE, fg=MUT,
                 font=("Segoe UI", 8, "bold"), anchor="w").pack(fill="x")

        cx = tk.Frame(sec_leg, bg=SURFACE)
        cx.pack(fill="x", pady=(6, 0))
        # ⭐⭐ A LEGENDA FIXA — 2026-08-29. Tudo numa LINHA SO' (texto, as duas
        # cores e o take), e isso e' restricao medida, nao gosto: a tela dele
        # tem 1017 px uteis, a janela ja' esta' em 930 e as tres colunas do
        # corpo terminam 12 px acima da secao de ERROS. Duas linhas novas
        # empurrariam o rodape para fora — o defeito de 28/08.
        # ⚠️ Os tres numeros acima cairam de 11 para 9 para pagar esta linha.
        self._fixo_linha = tk.Frame(sec_leg, bg=SURFACE)
        self._fixo_linha.pack(fill="x", pady=(6, 0))
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
        # ⭐ DOIS numeros, um por linha, cada um na cor da sua linha no
        # quadro. Sem a cor, dois numeros empilhados nao dizem qual e' qual.
        self.lb_leg_pct = tk.Label(lado, text="legenda 60%", bg=SURFACE,
                                   fg=AQUA, font=("Segoe UI", 9, "bold"),
                                   anchor="w")
        self.lb_leg_pct.pack(fill="x")
        self.lb_cta_pct = tk.Label(lado, text="CTA 47%", bg=SURFACE,
                                   fg=GOLD, font=("Segoe UI", 9, "bold"),
                                   anchor="w")
        self.lb_cta_pct.pack(fill="x")
        # ⭐ o terceiro numero traz DOIS eixos (x/y), porque o circulado
        # e' um ALVO e nao uma faixa de texto.
        self.lb_aqui_pct = tk.Label(lado, text="here 81/68%", bg=SURFACE,
                                    fg=RED, font=("Segoe UI", 9, "bold"),
                                    anchor="w")
        self.lb_aqui_pct.pack(fill="x")
        # ⭐⭐ A PREVIA DO TAKE COMO FUNDO — 2026-08-28, ordem do
        # operador: *"onde esta preto na tela da alturas e alvo, deve ser
        # possivel eu selecionar um take para ficar como imagem de fundo
        # para mim saber a altura que devo medir certo"*.
        # ⛔ O combo mora AQUI, na coluna de numeros, e nao embaixo do
        # quadro. MEDIDO: as tres colunas do corpo tem 609 px e a secao de
        # ERROS comeca 12 px abaixo delas — qualquer widget novo em pe
        # sobre o quadro empurraria o rodape para fora, que e' o defeito
        # de 26/08. Aqui ele cabe na altura que o quadro ja' ocupa.
        self.cb_fundo = ttk.Combobox(lado, style="Eddie.TCombobox",
                                     width=16, state="readonly", font=FT,
                                     values=[self._FUNDO_NENHUM])
        self.cb_fundo.set(self._FUNDO_NENHUM)
        self.cb_fundo.pack(fill="x", pady=(6, 0))
        self.cb_fundo.bind("<<ComboboxSelected>>", self._fundo_escolhido)
        self.bt_leg = botao(lado, "legenda", self._leg_alternar)
        self.bt_leg.pack(fill="x", pady=(8, 0))
        self.bt_aqui = botao(lado, "circulado", self._aqui_alternar)
        self.bt_aqui.pack(fill="x", pady=(4, 0))
        # ⭐ POR QUANTOS TAKES o efeito dura — 2026-08-28. Fica colado no
        # botao que ele modifica, e nao no rodape das opcoes gerais: quem
        # liga o circulado decide na mesma passada por quanto tempo.
        self.cb_aqui_takes = ttk.Combobox(
            lado, style="Eddie.TCombobox", width=16, state="readonly",
            font=FT, values=self._AQUI_TAKES_VALS)
        # ARRANCA COM O QUE ESTA GRAVADO, nao com o primeiro da lista:
        # combo que mostra "todos" enquanto o CFG diz "2" e o pior tipo de
        # painel -- ele mente sobre o que o proximo video vai fazer.
        self.cb_aqui_takes.set(self._aqui_takes_rotulo())
        self.cb_aqui_takes.pack(fill="x", pady=(4, 0))
        self.cb_aqui_takes.bind("<<ComboboxSelected>>",
                                self._aqui_takes_escolhido)

        # ---- a linha da LEGENDA FIXA (a caixa colorida do take) ----
        # ⛔ NAO TEM CHAVE LIGA/DESLIGA, de proposito: texto em branco ja' quer
        # dizer "nao quero", e um botao a mais nao cabia na altura da tela.
        lf = self._fixo_linha
        self.ent_fixo = tk.Entry(lf, bg=SURFACE2, fg=INK, relief="flat", bd=0,
                                 font=FT, insertbackground=INK,
                                 highlightthickness=1, highlightbackground=LINE,
                                 highlightcolor=AQUA)
        self.ent_fixo.pack(side="left", fill="x", expand=True, ipady=3)
        self.ent_fixo.insert(0, esteira.CFG.get("fixo_texto") or "")
        # ⚠️ grava no SOLTAR DA TECLA e ao sair do campo, nunca a cada
        # caractere com salvar_cfg — seria escrever o config.json a cada letra.
        self.ent_fixo.bind("<KeyRelease>", self._fixo_digitou)
        self.ent_fixo.bind("<FocusOut>", self._fixo_soltou)
        self.ent_fixo.bind("<Return>", self._fixo_soltou)

        self.bt_cor_txt = tk.Button(
            lf, text="A", command=lambda: self._fixo_cor("fixo_cor"),
            font=("Segoe UI", 8, "bold"), relief="flat", bd=0, cursor="hand2",
            width=2, padx=0, pady=0)
        self.bt_cor_txt.pack(side="left", padx=(4, 0), ipady=2)
        self.bt_cor_fundo = tk.Button(
            lf, text="█", command=lambda: self._fixo_cor("fixo_fundo"),
            font=("Segoe UI", 8, "bold"), relief="flat", bd=0, cursor="hand2",
            width=2, padx=0, pady=0)
        self.bt_cor_fundo.pack(side="left", padx=(2, 0), ipady=2)

        # ⭐ TRANSPARENCIA DA CAIXA. O `_ass_cor` cravava &H00 no alfa,
        # entao a caixa era sempre solida e nao havia como mudar isso.
        # ⚠️ Os rotulos sao em "quanto se ve", nao em alfa cru: no ASS o
        # alfa e' invertido (00 opaco, FF invisivel) e expor isso na UI
        # so' geraria escolha errada.
        self.cb_fixo_alfa = ttk.Combobox(
            lf, style="Eddie.TCombobox", width=10, state="readonly",
            font=FT, values=list(self._ALFA_VALS))
        self.cb_fixo_alfa.set(self._alfa_rotulo())
        self.cb_fixo_alfa.pack(side="left", padx=(4, 0))
        self.cb_fixo_alfa.bind("<<ComboboxSelected>>", self._fixo_alfa_escolhido)
        for _ev in ("<MouseWheel>", "<Button-4>", "<Button-5>"):
            self.cb_fixo_alfa.bind(_ev, lambda _e: "break")

        self.bt_emoji = tk.Button(
            lf, text="emoji", command=self._abrir_emoji,
            font=FT, relief="flat", bd=0, cursor="hand2",
            bg=SURFACE2, fg=INK, activebackground=AQUA,
            padx=8, pady=0)
        self.bt_emoji.pack(side="left", padx=(4, 0), ipady=2)

        self.cb_fixo_take = ttk.Combobox(
            lf, style="Eddie.TCombobox", width=9, state="readonly", font=FT,
            values=self._FIXO_TAKES_VALS)
        self.cb_fixo_take.set(self._fixo_take_rotulo())
        self.cb_fixo_take.pack(side="left", padx=(4, 0))
        self.cb_fixo_take.bind("<<ComboboxSelected>>", self._fixo_take_escolhido)


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
        self.cb_model = ttk.Combobox(rodape, style="Eddie.TCombobox", width=20,
                                     state="readonly", font=FT,
                                     values=["base (rapido)", "small (equilibrado)",
                                             "medium (preciso, lento)"])
        self.cb_model.current(0)
        self.cb_model.pack(side="left", padx=(8, 16))
        self.cb_model.bind("<<ComboboxSelected>>", self._cfg)
        # ⭐⭐ IDIOMA DO AUDIO (2026-08-30). Ate' hoje o editor so' entendia
        # ingles: os tres modelos do menu eram `.en` e o `lang` nunca saia de
        # "en". Audio alemao ou frances nao dava erro — saia transcrito
        # foneticamente como ingles, com cara de legenda pronta.
        # ⛔ O SUFIXO `.en` SUMIU DOS ROTULOS de proposito: quem o poe e tira
        # e' o `captions.modelo_para`, a partir DESTE combo. Escolher modelo
        # e idioma em separado permitia a combinacao quebrada.
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
        # ⭐ MUSICA dos takes mudos (2026-08-21, pedido para o AMISH 16S):
        # toca do inicio ate' o fim do penultimo take, cortada no tamanho do
        # trecho ja' editado. `travar` mantem a escolha entre sessoes.
        tk.Label(rodape, text="Musica", bg=BG, fg=DIM, font=FT).pack(side="left")
        self.cb_musica = ttk.Combobox(rodape, style="Eddie.TCombobox", width=22,
                                      state="readonly", font=FT,
                                      postcommand=self._musicas_refresh)
        self._musicas_refresh()
        self.cb_musica.pack(side="left", padx=(8, 6))

        # ⭐ VELOCIDADE — 2026-08-31, pedido do operador.
        # ⛔ Ate' aqui o fator era SEMPRE sorteado entre 0.95 e 1.03 e nao
        # havia como travar. "sorteio" mantem o anti-lote (cada video sai com
        # duracao um pouco diferente, para 50 videos nao terem o mesmo
        # tamanho); qualquer outro valor trava o lote inteiro.
        # ⚠️ A MUSICA NAO ENTRA NA ACELERACAO, e isso ja' era verdade antes:
        # ela e' mixada DEPOIS da legenda queimada (pipeline, mixar_musica),
        # e a velocidade roda bem antes (aplicar_velocidade). Travar o fator
        # nao muda essa ordem.
        tk.Label(rodape, text="Velocidade", bg=BG, fg=DIM,
                 font=FT).pack(side="left", padx=(12, 0))
        self.cb_vel = ttk.Combobox(
            rodape, style="Eddie.TCombobox", width=9, state="readonly",
            font=FT, values=list(self._VEL_VALS))
        self.cb_vel.set(self._vel_rotulo())
        self.cb_vel.pack(side="left", padx=(8, 6))
        self.cb_vel.bind("<<ComboboxSelected>>", self._vel_escolhida)
        for _ev in ("<MouseWheel>", "<Button-4>", "<Button-5>"):
            self.cb_vel.bind(_ev, lambda _e: "break")
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
        rot = self.cb_lang.get()
        for cod, r in self._IDIOMAS:
            if r == rot:
                esteira.CFG["lang"] = cod
                break
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

    # ⭐⭐ OS LIMITES DO ALVO NAO SAO OS DA LEGENDA, e nao podem ser.
    # ⛔ A legenda e o CTA sao faixas de texto centradas: basta nao encostar na
    # borda. O circulado tem PENDURICALHOS — o "here" fica 50px a direita e
    # 134px acima do centro, e a seta 137px a esquerda (medido em 720x1280).
    # Deixar o centro chegar a 90% poria o "here" FORA DO QUADRO, e o ASS corta
    # em silencio: sairia meia palavra e nenhum erro.
    # ⚠️ As contas: cx + 50 + 60 <= 720 -> x <= 0.85; cx - 137 >= 0 -> x >= 0.19;
    # cy - 134 - 21 >= 0 -> y >= 0.13; cy + 78 <= 1280 -> y <= 0.93.
    _AQ_X_MIN, _AQ_X_MAX = 0.19, 0.85
    _AQ_Y_MIN, _AQ_Y_MAX = 0.13, 0.93

    def _aqui_pos(self):
        """O centro do circulado como (x, y) em fracao. Mesmo clamp do esteira."""
        def _f(chave, padrao, lo, hi):
            t = (esteira.CFG.get(chave) or str(padrao)).strip().replace("%", "")
            try:
                v = float(t) / 100.0
            except ValueError:
                v = padrao / 100.0
            return max(lo, min(hi, v))
        return (_f("aqui_x", 81, self._AQ_X_MIN, self._AQ_X_MAX),
                _f("aqui_y", 68, self._AQ_Y_MIN, self._AQ_Y_MAX))

    # ===================================================================
    # ⭐⭐ A PREVIA DO TAKE NO SELETOR — 2026-08-28
    # ===================================================================
    _FUNDO_NENHUM = "sem fundo"
    _FUNDO_ARQUIVO = "escolher arquivo..."

    def _fundo_valores(self):
        """A lista do combo: os slots que TEM video, mais as duas opcoes."""
        vals = [self._FUNDO_NENHUM]
        for i, p in enumerate(self.manual):
            if p:
                n = os.path.basename(p)
                if len(n) > 13:
                    n = n[:11] + ".."
                vals.append("%d · %s" % (i + 1, n))
        vals.append(self._FUNDO_ARQUIVO)
        return vals

    def _fundo_lista(self):
        """Refaz a lista quando os takes mudam.

        ⚠️ Se o item escolhido sumiu (ele limpou os slots), o fundo cai para
        `sem fundo` em vez de continuar mostrando um quadro de video que nao
        esta' mais na fila — previa de video errado e' pior que previa nenhuma.
        """
        vals = self._fundo_valores()
        self.cb_fundo.configure(values=vals)
        if self.cb_fundo.get() not in vals:
            self.cb_fundo.set(self._FUNDO_NENHUM)
            self._leg_fundo = None
            self._leg_img = None
            self._leg_pintar()

    def _fundo_escolhido(self, _e=None):
        v = self.cb_fundo.get()
        if v == self._FUNDO_NENHUM:
            self._leg_fundo = None
        elif v == self._FUNDO_ARQUIVO:
            # ⭐ existe para o fluxo do ZIP, onde os takes nao passam pelos
            # slots manuais: ele aponta o arquivo direto.
            p = filedialog.askopenfilename(
                parent=self, title="Video de fundo do seletor",
                filetypes=[("Videos", "*.mp4 *.mov *.mkv *.webm *.m4v *.avi"),
                           ("Todos", "*.*")])
            if not p:
                self.cb_fundo.set(self._FUNDO_NENHUM)
                self._leg_fundo = None
            else:
                self._leg_fundo = os.path.normpath(p)
                nome = os.path.basename(p)
                self.cb_fundo.configure(
                    values=self._fundo_valores() + [nome])
                self.cb_fundo.set(nome)
        else:
            try:
                i = int(v.split(" ")[0]) - 1
            except ValueError:
                i = -1
            self._leg_fundo = self.manual[i] if 0 <= i < N_MANUAL else None
        self._fundo_carregar()
        self._leg_pintar()

    def _fundo_carregar(self):
        """Puxa UM quadro do video escolhido e guarda como fundo do quadro.

        ⛔ PPM, nao PNG: o `tk.PhotoImage` do tkinter puro le' GIF/PGM/PPM e
        mais nada. PNG obrigaria a Pillow, que nao esta' no venv — instalar
        uma dependencia inteira para desenhar uma miniatura seria caro demais.
        ⚠️ A REFERENCIA FICA EM `self._leg_img`: PhotoImage sem referencia viva
        e' coletado pelo Python e o canvas mostra vazio, SEM ERRO NENHUM. E' o
        modo de falha classico do tkinter e o mais dificil de diagnosticar.
        ⭐ O quadro sai do MEIO do take: o comeco costuma ser transicao e o fim
        costuma ser a mao saindo. O meio e' onde a cena esta' montada.
        """
        self._leg_img = None
        p = getattr(self, "_leg_fundo", None)
        if not p or not os.path.isfile(p):
            return
        try:
            t = max(0.1, pipeline.duracao(p) / 2.0)
        except Exception:
            t = 1.0
        dest = os.path.join(tempfile.gettempdir(), "veoedit_fundo.ppm")
        try:
            r = subprocess.run(
                [pipeline.FFMPEG, "-y", "-v", "error", "-ss", "%.2f" % t,
                 "-i", p, "-frames:v", "1",
                 "-vf", "scale=%d:%d" % (self.LEG_W, self.LEG_H),
                 "-f", "image2", "-c:v", "ppm", dest],
                capture_output=True, creationflags=pipeline.SEM_JANELA)
            if r.returncode == 0 and os.path.isfile(dest):
                self._leg_img = tk.PhotoImage(file=dest)
        except Exception:
            # ⚠️ previa e' conforto, nao funcao: se o ffmpeg falhar o seletor
            # volta ao fundo preto e o editor segue trabalhando.
            self._leg_img = None

    # ⭐ "todos os takes" e' o PRIMEIRO da lista porque e' o padrao pedido
    # na primeira ordem (*"a chave deve ativar em todos os takes"*); os
    # numeros vieram depois, como recorte.
    _AQUI_TAKES_VALS = ["todos os takes"] + [
        "%d take%s" % (n, "" if n == 1 else "s")
        for n in range(1, N_MANUAL + 1)]

    def _aqui_takes_rotulo(self):
        t = (esteira.CFG.get("aqui_takes") or "").strip()
        if t.isdigit() and 1 <= int(t) <= N_MANUAL:
            n = int(t)
            return "%d take%s" % (n, "" if n == 1 else "s")
        return self._AQUI_TAKES_VALS[0]

    def _aqui_takes_escolhido(self, _e=None):
        v = self.cb_aqui_takes.get()
        # ⚠️ "" no CFG quer dizer TODOS, nao zero — ver `_inteiro` no
        # `esteira.py`. Gravar "0" apagaria o efeito do video inteiro.
        esteira.CFG["aqui_takes"] = ("" if v == self._AQUI_TAKES_VALS[0]
                                     else v.split(" ")[0])
        esteira.salvar_cfg()

    # ===================================================================
    # ⭐⭐ A LEGENDA FIXA — a caixa colorida do take (2026-08-29)
    # ===================================================================
    # Ordem do operador com o reel `1 (1).mp4` na mao: *"existe uma legenda
    # fixa no take 1 (...) quero escrever algo e posicionar onde ira ficar (...)
    # e selecionar se sera aplicada no take 1, 2, 3, 4... ou em todos"*, e logo
    # depois *"tambem quero poder controlar a cor da legenda e do fundo dela"*.
    _FIXO_TAKES_VALS = ["todos"] + ["take %d" % n for n in range(1, N_MANUAL + 1)]
    # ⚠️ a caixa e' larga: com 24 caracteres ela ocupa 88% da largura. Por
    # isso o X anda menos do que parece — o libass encaixa a caixa dentro do
    # quadro, e texto largo so' consegue ficar no meio. O Y anda inteiro.
    _FX_X_MIN, _FX_X_MAX = 0.10, 0.90
    _FX_Y_MIN, _FX_Y_MAX = 0.06, 0.94

    def _fixo_pos(self):
        def _f(chave, padrao, lo, hi):
            t = (esteira.CFG.get(chave) or str(padrao)).strip().replace("%", "")
            try:
                v = float(t) / 100.0
            except ValueError:
                v = padrao / 100.0
            return max(lo, min(hi, v))
        return (_f("fixo_x", 50, self._FX_X_MIN, self._FX_X_MAX),
                _f("fixo_y", 15, self._FX_Y_MIN, self._FX_Y_MAX))

    def _fixo_txt(self):
        return (esteira.CFG.get("fixo_texto") or "").strip()

    def _fixo_take_rotulo(self):
        t = (esteira.CFG.get("fixo_take") or "").strip()
        if t.isdigit() and 1 <= int(t) <= N_MANUAL:
            return "take %d" % int(t)
        return self._FIXO_TAKES_VALS[0]

    def _fixo_take_escolhido(self, _e=None):
        v = self.cb_fixo_take.get()
        esteira.CFG["fixo_take"] = ("" if v == self._FIXO_TAKES_VALS[0]
                                    else v.split(" ")[1])
        esteira.salvar_cfg()

    def _fixo_digitou(self, _e=None):
        """A cada tecla so' o DESENHO muda; gravar fica para o soltar."""
        esteira.CFG["fixo_texto"] = self.ent_fixo.get()
        self._leg_pintar()

    def _fixo_soltou(self, _e=None):
        esteira.CFG["fixo_texto"] = self.ent_fixo.get()
        esteira.salvar_cfg()
        self._leg_pintar()

    # ===================================================================
    # ⭐ TRANSPARENCIA DA CAIXA + EMOJI — 2026-08-31
    # ===================================================================
    # No ASS o alfa e' INVERTIDO: 00 opaco, FF invisivel. Medido em render
    # sobre fundo verde: 0 solida, 50 metade, 100 sumiu e sobrou so' o texto.
    _ALFA_VALS = ("caixa solida", "caixa 25%", "caixa 50%",
                  "caixa 75%", "so contorno")
    _ALFA_PCT = {"caixa solida": 0, "caixa 25%": 25, "caixa 50%": 50,
                 "caixa 75%": 75, "so contorno": 100}

    # ⚠️ O sorteio fica PRIMEIRO de proposito: e' o padrao e o que o
    # operador deve escolher na duvida. Uma lista que abre num numero
    # convida a travar o lote sem querer.
    _VEL_VALS = ("sorteio", "0.90x", "0.95x", "1.00x", "1.05x",
                 "1.10x", "1.15x", "1.20x")

    def _vel_rotulo(self):
        v = (esteira.CFG.get("velocidade") or "sorteio").strip().lower()
        if v in ("", "sorteio"):
            return "sorteio"
        try:
            return "%.2fx" % float(v.rstrip("x").replace(",", "."))
        except ValueError:
            return "sorteio"

    def _vel_escolhida(self, _=None):
        esteira.CFG["velocidade"] = self.cb_vel.get()
        esteira.salvar_cfg()

    def _alfa_rotulo(self):
        try:
            v = int(float(esteira.CFG.get("fixo_alfa") or 0))
        except (TypeError, ValueError):
            v = 0
        for rot, pct in self._ALFA_PCT.items():
            if pct == v:
                return rot
        return self._ALFA_VALS[0]

    def _fixo_alfa_escolhido(self, _=None):
        pct = self._ALFA_PCT.get(self.cb_fixo_alfa.get(), 0)
        esteira.CFG["fixo_alfa"] = str(pct)
        # ⛔ ACOPLAMENTO DELIBERADO, nao magica: em "so contorno" o
        # `captions` troca para BorderStyle 1 e o contorno e' SEMPRE preto.
        # O padrao do texto e' PRETO — preto sobre contorno preto e'
        # invisivel. Quem escolhe esse modo quer o visual da fonte (branco
        # com contorno preto), entao o texto vai para branco junto.
        # ⭐ Nao e' irreversivel: o botao "A" continua mandando depois.
        if pct >= 100 and (esteira.CFG.get("fixo_cor") or "#000000").lower()                 in ("#000000", "000000"):
            esteira.CFG["fixo_cor"] = "#FFFFFF"
        esteira.salvar_cfg()
        self._leg_pintar()

    # ⛔ EMOJI SAI SEMPRE MONOCROMATICO, e isso e' do libass, nao escolha
    # nossa: o ffmpeg queima legenda por ele, e ele le so' a camada de
    # CONTORNO das fontes de emoji coloridas (a Segoe UI Emoji tem as duas).
    # Medido em render: coracao, fogo, mao e bebe sairam como linha branca.
    # ⭐ Em compensacao NAO precisa de tag de fonte nenhuma: o libass troca
    # de fonte sozinho ao achar um caractere que a Arial Black nao tem.
    # Medido no mesmo render, com o emoji cru no meio do texto.
    _EMOJIS = [
        "🤷", "🤦", "🙄", "😭",
        "😂", "😍", "😱", "😳",
        "👶", "👉", "👇", "👏",
        "❤", "⭐", "🔥", "✨",
        "🛒", "🎁", "💸", "✅",
    ]

    def _abrir_emoji(self):
        """Paleta pequena. Insere no cursor do campo da legenda fixa."""
        top = tk.Toplevel(self)
        top.title("Emoji")
        top.configure(bg=BG)
        top.resizable(False, False)
        top.transient(self)
        tk.Label(top, bg=BG, fg=DIM, font=FT, justify="left",
                 text="Sai em contorno branco, sem cor.\n"
                      "E' o libass do ffmpeg, nao da' para mudar aqui.",
                 ).grid(row=0, column=0, columnspan=5, padx=10, pady=(10, 6))

        def por(e):
            try:
                self.ent_fixo.insert(self.ent_fixo.index("insert"), e)
            except tk.TclError:
                self.ent_fixo.insert("end", e)
            self._fixo_digitou()
            top.destroy()

        for i, e in enumerate(self._EMOJIS):
            tk.Button(top, text=e, command=lambda x=e: por(x),
                      font=("Segoe UI Emoji", 16), relief="flat", bd=0,
                      bg=SURFACE2, fg=INK, activebackground=AQUA,
                      width=2, cursor="hand2"
                      ).grid(row=1 + i // 5, column=i % 5, padx=3, pady=3)
        top.update_idletasks()
        top.geometry("+%d+%d" % (self.winfo_rootx() + 220,
                                 self.winfo_rooty() + 220))

    def _fixo_cor(self, chave):
        """Abre o seletor de cor do sistema e guarda em #RRGGBB.

        ⚠️ #RRGGBB e' o que o tkinter devolve; quem inverte para o BGR do ASS
        e' o `captions._ass_cor`. Guardar aqui ja' invertido faria o painel
        mostrar uma cor e o video sair com outra.
        """
        atual = esteira.CFG.get(chave) or ("#000000" if chave == "fixo_cor"
                                           else "#F0D000")
        _rgb, hexa = colorchooser.askcolor(color=atual, parent=self,
                                           title="Cor")
        if not hexa:
            return
        esteira.CFG[chave] = hexa.upper()
        esteira.salvar_cfg()
        self._leg_pintar()

    def _aqui_alternar(self):
        lig = esteira.CFG.get("aqui_ligado") == "1"
        esteira.CFG["aqui_ligado"] = "" if lig else "1"
        esteira.salvar_cfg()
        self._leg_pintar()

    def _leg_pegar(self, e):
        """O que o clique agarrou: o ALVO do "here", ou a linha mais PROXIMA.

        ⛔ O alvo so' e' agarravel com a CHAVE LIGADA. Desligada, o seletor se
        comporta exatamente como antes deste efeito existir — quem nunca usa o
        circulado nao pode perder o controle das duas alturas por causa dele.

        ⛔ E o teste do alvo e' de CAIXA, nao de proximidade: as linhas ocupam a
        largura inteira, entao "a mais proxima" venceria sempre e o alvo nunca
        seria pego. Caixa pequena tambem devolve as linhas assim que o clique
        sai de cima do circulo — e o circulo ocupa 36 dos 104 px de largura,
        entao sobra quadro de sobra para agarrar as linhas ao lado dele.

        ⛔ Escolhe no BUTTON-1 e guarda ate' soltar. Decidir a cada
        `<B1-Motion>` faria a alca pular para a outra linha no instante em
        que as duas se cruzassem — e cruzar e' exatamente o que ele faz
        quando quer inverter a ordem delas.
        """
        v = e.y / float(self.LEG_H)
        # ⛔ A CAIXA FIXA E' O PRIMEIRO ALVO quando ha' texto: ela e' a maior
        # coisa do quadro e o operador acabou de digitar nela. As linhas
        # continuam alcancaveis por fora dela.
        fx_txt = self._fixo_txt()
        if fx_txt:
            fx, fy = self._fixo_pos()
            larg = min(0.88, max(0.16, len(fx_txt) / 24.0 * 0.88))
            n_lin = max(1, (len(fx_txt) + 23) // 24)
            if (abs(e.x - fx * self.LEG_W) <= larg * self.LEG_W / 2
                    and abs(e.y - fy * self.LEG_H)
                    <= max(7, 0.048 * n_lin * self.LEG_H / 2)):
                self._leg_alvo = "fixo"
                self._leg_arrastar(e)
                return
        if esteira.CFG.get("aqui_ligado") == "1":
            ax, ay = self._aqui_pos()
            if (abs(e.x - ax * self.LEG_W) <= 22
                    and abs(e.y - ay * self.LEG_H) <= 16):
                self._leg_alvo = "aqui"
                self._leg_arrastar(e)
                return
        self._leg_alvo = ("legenda_pos"
                          if abs(v - self._leg_pos()) <= abs(v - self._cta_pos())
                          else "cta_pos")
        self._leg_arrastar(e)

    def _leg_arrastar(self, e):
        """Arrasta o que o `_leg_pegar` agarrou dentro do quadro 9:16."""
        alvo = getattr(self, "_leg_alvo", "legenda_pos")
        if alvo == "fixo":
            x = e.x / float(self.LEG_W)
            y = e.y / float(self.LEG_H)
            esteira.CFG["fixo_x"] = "%d" % round(
                max(self._FX_X_MIN, min(self._FX_X_MAX, x)) * 100)
            esteira.CFG["fixo_y"] = "%d" % round(
                max(self._FX_Y_MIN, min(self._FX_Y_MAX, y)) * 100)
            self._leg_pintar()
            return
        if alvo == "aqui":
            # ⭐ DOIS eixos de uma vez: o circulado e' um alvo, e alvo se move
            # nas duas direcoes. As duas linhas continuam so' na vertical.
            x = e.x / float(self.LEG_W)
            y = e.y / float(self.LEG_H)
            esteira.CFG["aqui_x"] = "%d" % round(
                max(self._AQ_X_MIN, min(self._AQ_X_MAX, x)) * 100)
            esteira.CFG["aqui_y"] = "%d" % round(
                max(self._AQ_Y_MIN, min(self._AQ_Y_MAX, y)) * 100)
        else:
            v = e.y / float(self.LEG_H)
            v = max(self._LEG_MIN, min(self._LEG_MAX, v))
            esteira.CFG[alvo] = "%d" % round(v * 100)
        self._leg_pintar()

    def _leg_soltar(self, _e=None):
        # ⚠️ grava no SOLTAR, nao a cada pixel do arrasto: salvar no
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

        # ⭐⭐ O QUADRO DO TAKE ENTRA PRIMEIRO, embaixo de tudo — e' o ponto
        # do pedido: sem ele as tres reguas flutuam sobre preto e a altura
        # "certa" e' chute. Com o quadro, ele ve' onde cai a cabeca.
        img = getattr(self, "_leg_img", None)
        if img is not None:
            c.create_image(0, 0, anchor="nw", image=img)

        # ⭐ a faixa que a FONTE usa (58%-63%), medida no 2.mp4
        # ⚠️ com o quadro atras ela vira CONTORNO: preenchida, tapava
        # justamente a parte do take que ele quer enxergar.
        if img is None:
            c.create_rectangle(1, H * 0.58, W - 1, H * 0.63,
                               fill="#0d1b16", outline="")
        else:
            c.create_rectangle(1, H * 0.58, W - 1, H * 0.63,
                               outline="#1d5c4e", dash=(2, 2))
        # ⭐⭐ A LINHA DO CTA VIROU ARRASTAVEL — 2026-08-26, segunda ordem
        # dele: *"tambem quero poder controlar a altura do CTA"*. Ela ja'
        # estava desenhada como referencia; agora e' um controle.
        # ⛔ AS DUAS NO MESMO QUADRO, e isso e' o ponto: a razao de existir a
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

        # ⭐⭐ O ALVO DO CIRCULADO + "HERE" — 2026-08-28, ordem do operador:
        # *"o local que aparece o circulado e o here deve ser selecionavel ali
        # no seletor das legendas"*. Mesmo quadro das duas alturas, e e' o
        # ponto: e' aqui que se ve' se o circulo vai cair em cima da legenda.
        # ⭐ As proporcoes sao as MEDIDAS do reel, nao aproximacao de desenho:
        # raio 0,169 da largura e 0,059 da altura; o "here" a +0,070 da largura
        # e -0,105 da altura do centro. O que ele arrasta aqui e' o que sai la'.
        # ⚠️ DESENHADO MESMO DESLIGADO, em cor apagada: sem isso ele teria de
        # ligar a chave as cegas para descobrir onde o efeito ia cair.
        aq_lig = esteira.CFG.get("aqui_ligado") == "1"
        ax, ay = self._aqui_pos()
        acx, acy = ax * W, ay * H
        # ⚠️ 118/720 e 72,5/1280 — os MESMOS raios do `captions.py`, no
        # estado de repouso (o pulso so' sobe). Numero solto aqui faria o
        # painel prometer um tamanho e o video entregar outro.
        arx, ary = W * 0.164, H * 0.0566
        cor_aq = RED if aq_lig else "#5a3330"
        c.create_line(acx - W * 0.182, acy - H * 0.146,
                      acx - W * 0.087, acy - H * 0.074,
                      fill=cor_aq, width=2, arrow="last",
                      arrowshape=(6, 7, 3))
        c.create_oval(acx - arx, acy - ary, acx + arx, acy + ary,
                      outline=cor_aq, width=2)
        c.create_text(acx + W * 0.070, acy - H * 0.105, text="here",
                      fill=cor_aq, font=("Segoe UI", 7, "bold"))
        # ⚠️ AVISA QUANDO AS DUAS SE ENCOSTAM. O bloco da legenda ocupa
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
        # ⭐⭐ A CAIXA DA LEGENDA FIXA, desenhada nas cores de verdade — e' o
        # unico jeito de ele ver ANTES de renderizar se o texto preto vai sumir
        # num fundo escuro. A largura acompanha o tamanho do texto: 24
        # caracteres ocupam 88% da largura, medido no render.
        fx_txt = self._fixo_txt()
        if fx_txt:
            fx, fy = self._fixo_pos()
            n_lin = max(1, (len(fx_txt) + 23) // 24)
            larg = min(0.88, max(0.16, len(fx_txt) / 24.0 * 0.88))
            fw, fh = W * larg, H * 0.048 * n_lin
            cor_fx = esteira.CFG.get("fixo_cor") or "#000000"
            cor_bg = esteira.CFG.get("fixo_fundo") or "#F0D000"
            # ⚠️ o Canvas do tkinter nao tem alfa: com "sem caixa" a
            # previa DESENHA a caixa e o video final nao teria nenhuma.
            # Previa que mente e' pior que previa pobre — entao ela some.
            try:
                _alf = int(float(esteira.CFG.get("fixo_alfa") or 0))
            except (TypeError, ValueError):
                _alf = 0
            if _alf < 100:
                c.create_rectangle(fx * W - fw / 2, fy * H - fh / 2,
                                   fx * W + fw / 2, fy * H + fh / 2,
                                   fill=cor_bg, outline=cor_bg)
            c.create_text(fx * W, fy * H, text=fx_txt[:10], fill=cor_fx,
                          font=("Segoe UI", 6, "bold"))
        for _b, _k, _p in ((self.bt_cor_txt, "fixo_cor", "#000000"),
                           (self.bt_cor_fundo, "fixo_fundo", "#F0D000")):
            _c = esteira.CFG.get(_k) or _p
            _b.configure(bg=_c, activebackground=_c,
                         fg="#FFFFFF" if _k == "fixo_fundo" else "#FFFFFF")
        self.lb_aqui_pct.configure(
            text="here %d/%d%%" % (round(ax * 100), round(ay * 100)),
            fg=RED if aq_lig else MUT)
        self.bt_aqui.configure(
            bg=RED if aq_lig else SURFACE2,
            fg="#2a0b08" if aq_lig else DIM,
            activebackground=RED if aq_lig else SURFACE2,
            activeforeground="#2a0b08" if aq_lig else INK,
            text="circulado ligado" if aq_lig else "circulado desligado")
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
        for i, (cod, rot) in enumerate(self._IDIOMAS):
            if cod == esteira.CFG.get("lang", "en"):
                self.cb_lang.current(i)
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
        # ⭐ a lista do fundo acompanha os slots: escolher ou limpar take
        # atualiza o combo na mesma acao, sem o operador ter de mexer nele.
        if hasattr(self, "cb_fundo"):
            self._fundo_lista()
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

