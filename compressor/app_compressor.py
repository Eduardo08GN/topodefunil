# -*- coding: utf-8 -*-
"""COMPRIMIR - app de janela. Motor em `comprimir.py`, so' a interface aqui.

Mesma identidade do Veo Editor (paleta, fontes). Escolhe pasta ou arquivos,
clica, e ve' a economia em tempo real. A saida vai para `comprimidos/` ao lado
dos arquivos — nunca sobrescreve o original.
"""
import os
import queue
import sys
import threading
import tkinter as tk
from tkinter import filedialog

# o motor mora ao lado
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import comprimir as M  # noqa: E402

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
GREEN = "#4bd18a"
FT = ("Segoe UI", 9)
FB = ("Segoe UI", 10, "bold")
FTIT = ("Segoe UI", 15, "bold")


class Args:
    """espelha o argparse do motor, alimentado pela UI."""
    def __init__(self):
        self.crf = 23
        self.x265 = False
        self.preset = "medium"
        self.jpeg_q = 3
        self.para_jpg = False


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Comprimir  -  video e imagem, sem perder qualidade")
        self.configure(bg=BG)
        self.geometry("720x620")
        self.minsize(660, 560)
        self._alvos = []
        self._rodando = False
        self._fila = queue.Queue()
        self._montar()
        self.after(80, self._bombear)

    # ------------------------------------------------------------------
    def _montar(self):
        tk.Label(self, text="COMPRIMIR", bg=BG, fg=INK, font=FTIT).pack(
            anchor="w", padx=22, pady=(18, 0))
        tk.Label(self, text="video e imagem menores, sem diferenca visivel",
                 bg=BG, fg=MUT, font=FT).pack(anchor="w", padx=22, pady=(0, 14))

        # --- zona de soltar / escolher ---
        self.drop = tk.Frame(self, bg=SURFACE, highlightbackground=LINE,
                             highlightthickness=1)
        self.drop.pack(fill="x", padx=22)
        self.lb_drop = tk.Label(self.drop,
                                text="Nenhuma pasta escolhida.\nClique em "
                                     "“Escolher pasta” ou “Escolher "
                                     "arquivos”.",
                                bg=SURFACE, fg=DIM, font=FB, justify="center",
                                pady=26)
        self.lb_drop.pack(fill="x")

        linha_b = tk.Frame(self, bg=BG)
        linha_b.pack(fill="x", padx=22, pady=12)
        self._botao(linha_b, "Escolher pasta", self._pick_pasta, primario=True
                    ).pack(side="left")
        self._botao(linha_b, "Escolher arquivos", self._pick_arquivos
                    ).pack(side="left", padx=(8, 0))
        self._botao(linha_b, "Limpar", self._limpar).pack(side="left", padx=(8, 0))

        # --- opcoes ---
        opc = tk.Frame(self, bg=SURFACE, highlightbackground=LINE,
                       highlightthickness=1)
        opc.pack(fill="x", padx=22, pady=(0, 12))
        tk.Label(opc, text="QUALIDADE", bg=SURFACE, fg=MUT,
                 font=("Segoe UI", 8, "bold")).grid(row=0, column=0, columnspan=4,
                                                    sticky="w", padx=14, pady=(10, 6))

        # nivel de qualidade em 3 botoes (esconde o CRF cru do operador)
        self.nivel = tk.StringVar(value="equilibrado")
        niveis = [("Maxima", "maxima", "quase perfeito, arquivo maior"),
                  ("Equilibrado", "equilibrado", "sem diferenca visivel  (recomendado)"),
                  ("Compacto", "compacto", "menor, perda minima")]
        self._radios = []
        for i, (rot, val, _dsc) in enumerate(niveis):
            b = tk.Radiobutton(opc, text=rot, value=val, variable=self.nivel,
                               bg=SURFACE, fg=INK, selectcolor=SURFACE2,
                               activebackground=SURFACE, activeforeground=AQUA,
                               font=FT, bd=0, highlightthickness=0,
                               command=self._pintar_dsc)
            b.grid(row=1, column=i, sticky="w", padx=(14 if i == 0 else 8, 0))
            self._radios.append(b)
        self.lb_dsc = tk.Label(opc, text="", bg=SURFACE, fg=MUT, font=FT)
        self.lb_dsc.grid(row=2, column=0, columnspan=4, sticky="w", padx=14, pady=(2, 10))

        # dois toggles
        self.v_x265 = tk.BooleanVar(value=False)
        self.v_jpg = tk.BooleanVar(value=False)
        tk.Checkbutton(opc, text="HEVC (menor ainda, mais lento — NAO para "
                       "AdBatch/Facebook)", variable=self.v_x265,
                       bg=SURFACE, fg=DIM, selectcolor=SURFACE2, font=FT, bd=0,
                       activebackground=SURFACE, activeforeground=INK,
                       highlightthickness=0).grid(row=3, column=0, columnspan=4,
                                                  sticky="w", padx=12, pady=(0, 2))
        tk.Checkbutton(opc, text="Converter PNG de foto para JPG (encolhe muito; "
                       "PNG com transparencia fica PNG)", variable=self.v_jpg,
                       bg=SURFACE, fg=DIM, selectcolor=SURFACE2, font=FT, bd=0,
                       activebackground=SURFACE, activeforeground=INK,
                       highlightthickness=0).grid(row=4, column=0, columnspan=4,
                                                  sticky="w", padx=12, pady=(0, 12))
        self._pintar_dsc()

        # --- acao ---
        self.bt_go = self._botao(self, "Comprimir", self._rodar, primario=True,
                                 grande=True)
        self.bt_go.pack(fill="x", padx=22)
        self.bt_go.configure(state="disabled")

        # --- progresso ---
        self.barra_fundo = tk.Frame(self, bg=SURFACE2, height=6)
        self.barra_fundo.pack(fill="x", padx=22, pady=(12, 2))
        self.barra = tk.Frame(self.barra_fundo, bg=AQUA, height=6, width=0)
        self.barra.place(x=0, y=0, relheight=1)

        # --- log ---
        cx = tk.Frame(self, bg=SURFACE, highlightbackground=LINE, highlightthickness=1)
        cx.pack(fill="both", expand=True, padx=22, pady=(6, 8))
        self.log = tk.Text(cx, bg=SURFACE, fg=DIM, font=("Consolas", 9),
                           relief="flat", bd=0, padx=12, pady=10, wrap="none",
                           highlightthickness=0)
        self.log.pack(fill="both", expand=True)
        self.log.configure(state="disabled")

        self.lb_total = tk.Label(self, text="", bg=BG, fg=GREEN, font=FB)
        self.lb_total.pack(anchor="w", padx=22, pady=(0, 12))

    # ------------------------------------------------------------------
    def _botao(self, pai, texto, cmd, primario=False, grande=False):
        bg = AQUA if primario else SURFACE2
        fg = "#04231f" if primario else INK
        return tk.Button(pai, text=texto, command=cmd, font=FB if grande else FB,
                         bg=bg, fg=fg, relief="flat", bd=0, cursor="hand2",
                         activebackground=("#2adcc7" if primario else LINE),
                         activeforeground=fg, padx=18,
                         pady=(11 if grande else 8))

    def _pintar_dsc(self):
        d = {"maxima": "Qualidade quase perfeita. Arquivo maior. (CRF 18)",
             "equilibrado": "Sem diferenca visivel a olho. Recomendado. (CRF 23)",
             "compacto": "O menor, com perda minima. (CRF 26)"}
        self.lb_dsc.configure(text=d.get(self.nivel.get(), ""))

    # ------------------------------------------------------------------
    def _pick_pasta(self):
        d = filedialog.askdirectory(title="Escolha a pasta com os videos/imagens")
        if not d:
            return
        exts = M.VIDEO_EXT | M.IMAGEM_EXT
        self._alvos = [os.path.join(d, n) for n in sorted(os.listdir(d))
                       if os.path.isfile(os.path.join(d, n))
                       and os.path.splitext(n)[1].lower() in exts]
        self._refletir(os.path.basename(d) or d)

    def _pick_arquivos(self):
        fs = filedialog.askopenfilenames(
            title="Escolha os arquivos",
            filetypes=[("Video e imagem",
                        "*.mp4 *.mov *.mkv *.webm *.avi *.m4v "
                        "*.jpg *.jpeg *.png *.webp *.bmp *.tiff"),
                       ("Todos", "*.*")])
        if not fs:
            return
        self._alvos = list(fs)
        self._refletir("%d arquivo(s)" % len(fs))

    def _refletir(self, origem):
        n = len(self._alvos)
        if not n:
            self.lb_drop.configure(text="Nada de video ou imagem ali.", fg=RED)
            self.bt_go.configure(state="disabled")
            return
        v = sum(1 for p in self._alvos if os.path.splitext(p)[1].lower() in M.VIDEO_EXT)
        i = n - v
        tot = sum(os.path.getsize(p) for p in self._alvos)
        self.lb_drop.configure(
            text="%s\n%d video(s) + %d imagem(ns)  -  %.1f MB no total"
                 % (origem, v, i, M._mb(tot)), fg=INK)
        self.bt_go.configure(state="normal")

    def _limpar(self):
        self._alvos = []
        self.lb_drop.configure(text="Nenhuma pasta escolhida.", fg=DIM)
        self.bt_go.configure(state="disabled")
        self._log_limpar()
        self.lb_total.configure(text="")
        self.barra.configure(width=0)

    # ------------------------------------------------------------------
    def _log(self, msg):
        self.log.configure(state="normal")
        self.log.insert("end", msg + "\n")
        self.log.see("end")
        self.log.configure(state="disabled")

    def _log_limpar(self):
        self.log.configure(state="normal")
        self.log.delete("1.0", "end")
        self.log.configure(state="disabled")

    # ------------------------------------------------------------------
    def _rodar(self):
        if self._rodando or not self._alvos:
            return
        self._rodando = True
        self.bt_go.configure(state="disabled", text="Comprimindo...")
        self._log_limpar()
        self.lb_total.configure(text="")
        args = Args()
        args.crf = {"maxima": 18, "equilibrado": 23, "compacto": 26}[self.nivel.get()]
        args.x265 = self.v_x265.get()
        args.para_jpg = self.v_jpg.get()
        alvos = list(self._alvos)
        threading.Thread(target=self._worker, args=(alvos, args), daemon=True).start()

    def _worker(self, alvos, args):
        ta = td = feitos = 0
        for k, p in enumerate(alvos, 1):
            self._fila.put(("prog", k - 1, len(alvos)))
            self._fila.put(("log", "  processando %s ..." % os.path.basename(p)[:44]))
            try:
                r = self._proc_um(p, args)
            except Exception as e:  # noqa: BLE001
                self._fila.put(("log", "  >>> ERRO: %s" % e))
                r = None
            if r:
                ta += r[0]; td += r[1]; feitos += 1
                self._fila.put(("subst", r[2]))
        self._fila.put(("prog", len(alvos), len(alvos)))
        self._fila.put(("fim", (feitos, ta, td)))

    def _proc_um(self, entrada, args):
        """igual ao processar() do motor, mas devolve tambem a linha pronta."""
        e = os.path.splitext(entrada)[1].lower()
        if e not in M.VIDEO_EXT and e not in M.IMAGEM_EXT:
            return None
        saida = M._saida_para(entrada, args.para_jpg)
        antes = M._tamanho(entrada)
        if e in M.VIDEO_EXT:
            res = M.comprimir_video(entrada, saida, args.crf, args.x265, args.preset)
            tipo = "V"
        else:
            res = M.comprimir_imagem(entrada, saida, args.jpeg_q, args.para_jpg)
            tipo = "I"
        if res.returncode != 0 or not os.path.exists(saida):
            return None
        depois = M._tamanho(saida)
        if depois >= antes:
            import shutil
            shutil.copy2(entrada, saida)
            linha = "  = %-34s ja' estava otimo (%.1f MB)" % (
                os.path.basename(entrada)[:34], M._mb(antes))
            return (antes, antes, linha)
        linha = "  %s %-32s %6.1f MB -> %5.1f MB  (-%.0f%%)" % (
            tipo, os.path.basename(entrada)[:32], M._mb(antes), M._mb(depois),
            M._pct(antes, depois))
        return (antes, depois, linha)

    # ------------------------------------------------------------------
    def _bombear(self):
        try:
            while True:
                tipo, *dados = self._fila.get_nowait()
                if tipo == "log":
                    self._log(dados[0])
                elif tipo == "subst":
                    self._log(dados[0])
                elif tipo == "prog":
                    feito, total = dados
                    w = int(self.barra_fundo.winfo_width() * feito / max(1, total))
                    self.barra.configure(width=w)
                elif tipo == "fim":
                    feitos, ta, td = dados[0]
                    self._rodando = False
                    self.bt_go.configure(state="normal", text="Comprimir")
                    if feitos:
                        self.lb_total.configure(
                            text="Pronto: %d arquivo(s)  %.1f MB -> %.1f MB  "
                                 "(economia %.0f%%, %.1f MB a menos)"
                                 % (feitos, M._mb(ta), M._mb(td),
                                    M._pct(ta, td), M._mb(ta - td)))
                        self._log("")
                        self._log("Salvos na subpasta 'comprimidos'.")
                    else:
                        self.lb_total.configure(text="Nada processado.", fg=RED)
        except queue.Empty:
            pass
        self.after(80, self._bombear)


if __name__ == "__main__":
    # ⛔ pythonw NAO tem console: um erro de inicializacao morre em silencio e o
    # app "nao abre". Este guarda grava qualquer excecao num log ao lado do
    # arquivo, para nunca mais haver falha invisivel.
    try:
        App().mainloop()
    except Exception:  # noqa: BLE001
        import traceback
        _log = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "erro_ao_abrir.txt")
        with open(_log, "w", encoding="utf-8") as _f:
            _f.write(traceback.format_exc())
        raise
