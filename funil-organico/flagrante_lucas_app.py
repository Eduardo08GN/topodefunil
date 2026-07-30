#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
FLAGRANTE LUCAS — app desktop offline do agente FLAGRANTE.

Interface para o motor em flagrante_lucas.py: sorteia os eixos, deixa
retrocar eixo por eixo, permite editar a copy, roda o linter e entrega os
11 blocos com um clique de copia cada.

Roda offline, sem dependencia externa (tkinter vem com o Python).

    python funil-organico/flagrante_lucas_app.py
"""

import os
import random
import sys
import tkinter as tk
from tkinter import filedialog, ttk

if getattr(sys, "frozen", False):          # rodando como .exe do PyInstaller
    BASE = os.path.dirname(sys.executable)
    sys.path.insert(0, sys._MEIPASS)
else:
    BASE = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, BASE)

import flagrante_lucas as motor  # noqa: E402

# o ledger acompanha o executavel, nao a pasta temporaria do PyInstaller
motor.LEDGER = os.path.join(BASE, ".flagrante-ledger.json")

# --------------------------------------------------------------------------
# PALETA — fill solido, contraste alto, zero cinza-sobre-cinza
# --------------------------------------------------------------------------
BG = "#0f1116"
PANEL = "#171a22"
PANEL2 = "#1e222c"
LINE = "#2b3140"
TXT = "#e8eaf0"
MUTED = "#98a0b3"
ACCENT = "#ff6a3d"
ACCENT_D = "#e0522a"
OK = "#35d07f"
ERRO = "#ff5f56"
AVISO = "#ffb02e"

F_UI = ("Segoe UI", 10)
F_UI_B = ("Segoe UI Semibold", 10)
F_TIT = ("Segoe UI Semibold", 17)
F_PASSO = ("Segoe UI Semibold", 9)
F_MONO = ("Consolas", 10)
F_SMALL = ("Segoe UI", 9)

EIXOS = [
    ("ocasiao", "OCASIÃO", "OCASIOES", "id"),
    ("prop", "PROP", "PROPS", "id"),
    ("ambiente", "AMBIENTE", "AMBIENTES", "id"),
    ("ref", "NARRADOR", "REFS", "marca"),
    ("vitima", "VÍTIMA", "VITIMAS", "marca"),
    ("mulher", "MULHER", "MULHERES", "hook"),
]

CENAS = ["1 · RUÍNA", "2 · DESCOBERTA", "3 · RITUAL", "4 · REDENÇÃO", "5 · CTA"]

# nomes legiveis para o resumo em portugues
# ja' com a preposicao contraida — abrem a frase do resumo
PT_OCASIAO = {
    "casamento": "Num casamento", "confraternizacao": "Na confraternização da firma",
    "pescaria_firma": "Na pescaria da firma", "reuniao_firma": "Na reunião da firma",
    "churrasco": "Num churrasco de família", "jantar_amigos": "Num jantar de amigos",
    "aniversario": "Nas bodas de casamento", "clube_golfe": "No almoço do clube de golfe",
}
PT_PROP = {
    "geoduck": "um geoduck", "banana": "uma banana", "okra": "um quiabo",
    "pepino": "um pepino", "aspargo": "um aspargo", "daikon": "um nabo daikon",
    "linguica": "uma linguiça",
}
PT_AMBIENTE = {
    "cozinha": "na cozinha", "cozinha_aberta": "na cozinha com ilha",
    "churrasqueira": "na área de churrasco", "varanda": "na varanda coberta",
    "garagem": "na garagem oficina", "copa": "na copa",
}


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("FLAGRANTE LUCAS  v1.1")
        self.configure(bg=BG)
        self.geometry("1360x900")
        self.minsize(1180, 760)

        self.spec = None
        self.blocos = {}
        self.achados = []
        self.rng = random.Random()

        self._estilos()
        self._topo()
        corpo = tk.Frame(self, bg=BG)
        corpo.pack(fill="both", expand=True, padx=16, pady=(0, 8))
        self._coluna_esq(corpo)
        self._coluna_dir(corpo)
        self._rodape()

        self.bind("<Control-r>", lambda _e: self.sortear())
        self.bind("<Control-s>", lambda _e: self.salvar())

        self.sortear()

    # ---------------------------------------------------------------- estilo
    def _estilos(self):
        s = ttk.Style(self)
        s.theme_use("clam")
        s.configure("TCombobox", fieldbackground=PANEL2, background=PANEL2,
                    foreground=TXT, arrowcolor=TXT, bordercolor=LINE,
                    lightcolor=LINE, darkcolor=LINE, insertcolor=TXT)
        self.option_add("*TCombobox*Listbox.background", PANEL2)
        self.option_add("*TCombobox*Listbox.foreground", TXT)
        self.option_add("*TCombobox*Listbox.selectBackground", ACCENT)

    def _btn(self, pai, texto, cmd, primario=False, pady=6):
        c = ACCENT if primario else PANEL2
        ca = ACCENT_D if primario else LINE
        return tk.Button(pai, text=texto, command=cmd,
                         font=F_UI_B if primario else F_UI,
                         bg=c, fg="#ffffff" if primario else TXT,
                         activebackground=ca, activeforeground="#ffffff",
                         relief="flat", bd=0, cursor="hand2", padx=15, pady=pady)

    def _passo(self, pai, num, titulo, dica):
        """Cabecalho numerado — diz o que fazer naquela area."""
        c = tk.Frame(pai, bg=BG)
        c.pack(fill="x", pady=(14, 6))
        badge = tk.Label(c, text=" %s " % num, font=F_PASSO, bg=ACCENT,
                         fg="#ffffff", padx=4)
        badge.pack(side="left", ipady=1)
        tk.Label(c, text=titulo, font=F_UI_B, bg=BG, fg=TXT).pack(side="left", padx=(8, 0))
        tk.Label(c, text=dica, font=F_SMALL, bg=BG, fg=MUTED).pack(side="left", padx=(10, 0))
        return c

    # ------------------------------------------------------------------ topo
    def _topo(self):
        t = tk.Frame(self, bg=BG)
        t.pack(fill="x", padx=16, pady=(12, 4))

        tk.Label(t, text="FLAGRANTE", font=F_TIT, bg=BG, fg=TXT).pack(side="left")
        tk.Label(t, text="LUCAS", font=F_TIT, bg=BG, fg=ACCENT).pack(side="left", padx=(7, 0))
        tk.Label(t, text="humilhação pública · gerador offline de prompts Veo",
                 font=F_SMALL, bg=BG, fg=MUTED).pack(side="left", padx=(14, 0), pady=(7, 0))

        cx = tk.Frame(t, bg=BG)
        cx.pack(side="right")

        self._btn(cx, "SORTEAR VÍDEO   Ctrl+R", self.sortear,
                  primario=True, pady=8).pack(side="right")

        tk.Label(cx, text="seed", font=F_SMALL, bg=BG, fg=MUTED).pack(side="right", padx=(16, 5))
        self.var_seed = tk.StringVar()
        tk.Entry(cx, textvariable=self.var_seed, width=7, font=F_UI, bg=PANEL2,
                 fg=TXT, insertbackground=TXT, relief="flat",
                 justify="center").pack(side="right", ipady=6)

        self.var_pag = tk.StringVar(value="ray")
        cb = ttk.Combobox(cx, textvariable=self.var_pag, values=sorted(motor.ETNIA),
                          state="readonly", width=9, font=F_UI)
        cb.pack(side="right", padx=(0, 12), ipady=4)
        cb.bind("<<ComboboxSelected>>", lambda _e: self.sortear())
        tk.Label(cx, text="página", font=F_SMALL, bg=BG,
                 fg=MUTED).pack(side="right", padx=(0, 5))

        tk.Frame(self, bg=LINE, height=1).pack(fill="x", padx=16, pady=(10, 0))

    # -------------------------------------------------------------- esquerda
    def _coluna_esq(self, pai):
        col = tk.Frame(pai, bg=BG, width=490)
        col.pack(side="left", fill="y")
        col.pack_propagate(False)

        self._passo(col, 1, "O vídeo sorteado", "não gostou de um eixo? troque só ele")

        # resumo em portugues — o que o video E', sem ler ingles
        res = tk.Frame(col, bg=PANEL2)
        res.pack(fill="x")
        self.lbl_resumo = tk.Label(res, text="", font=F_UI, bg=PANEL2, fg=TXT,
                                   wraplength=450, justify="left", anchor="w",
                                   padx=14, pady=11)
        self.lbl_resumo.pack(fill="x")

        cx = tk.Frame(col, bg=PANEL)
        cx.pack(fill="x", pady=(2, 0))
        self.lbl_eixo = {}
        for i, (chave, rotulo, _p, _c) in enumerate(EIXOS):
            lin = tk.Frame(cx, bg=PANEL)
            lin.pack(fill="x", padx=13, pady=(9 if i == 0 else 4, 4))
            tk.Label(lin, text=rotulo, font=F_SMALL, bg=PANEL, fg=MUTED,
                     width=10, anchor="w").pack(side="left")
            tk.Button(lin, text="trocar", font=F_SMALL, bg=PANEL2, fg=ACCENT,
                      activebackground=LINE, activeforeground=ACCENT,
                      relief="flat", bd=0, cursor="hand2", padx=10, pady=2,
                      command=lambda c=chave: self.trocar_eixo(c)).pack(side="right")
            v = tk.Label(lin, text="—", font=F_UI_B, bg=PANEL, fg=TXT,
                         anchor="w", wraplength=300, justify="left")
            v.pack(side="left", fill="x", expand=True)
            self.lbl_eixo[chave] = v
        tk.Frame(cx, bg=PANEL, height=8).pack()

        self._passo(col, 2, "A copy", "edite à vontade — copy é sua, o app só confere")

        cc = tk.Frame(col, bg=PANEL)
        cc.pack(fill="both", expand=True)
        self.txt_fala = []
        for i, nome in enumerate(CENAS):
            cab = tk.Frame(cc, bg=PANEL)
            cab.pack(fill="x", padx=13, pady=(9 if i == 0 else 6, 2))
            tk.Label(cab, text=nome, font=F_SMALL, bg=PANEL,
                     fg=ACCENT, anchor="w").pack(side="left")
            cont = tk.Label(cab, text="", font=F_SMALL, bg=PANEL, fg=MUTED)
            cont.pack(side="right")
            t = tk.Text(cc, height=3, font=F_SMALL, bg=PANEL2, fg=TXT, wrap="word",
                        relief="flat", bd=0, insertbackground=TXT, padx=10, pady=6,
                        highlightthickness=1, highlightbackground=LINE,
                        highlightcolor=ACCENT)
            t.pack(fill="x", padx=13)
            t.contador = cont
            t.bind("<KeyRelease>", lambda _e: self._marcar_sujo())
            self.txt_fala.append(t)

        acao = tk.Frame(cc, bg=PANEL)
        acao.pack(fill="x", padx=13, pady=12)
        self._btn(acao, "aplicar copy e revalidar", self.aplicar_copy).pack(side="left")
        self.lbl_sujo = tk.Label(acao, text="", font=F_SMALL, bg=PANEL, fg=AVISO)
        self.lbl_sujo.pack(side="left", padx=10)

    # ---------------------------------------------------------------- direita
    def _coluna_dir(self, pai):
        col = tk.Frame(pai, bg=BG)
        col.pack(side="left", fill="both", expand=True, padx=(16, 0))

        self._passo(col, 3, "Copie para o AdBatch",
                    "clique no bloco, depois em COPIAR — ou copie os 5 de uma vez")

        barra = tk.Frame(col, bg=BG)
        barra.pack(fill="x", pady=(0, 8))
        self.b_img = self._btn(barra, "copiar os 5 IMAGE",
                               lambda: self.copiar_grupo("IMAGE"))
        self.b_img.pack(side="left")
        self.b_tak = self._btn(barra, "copiar os 5 TAKE",
                               lambda: self.copiar_grupo("TAKE"))
        self.b_tak.pack(side="left", padx=8)
        self._btn(barra, "salvar .txt", self.salvar).pack(side="left")
        self._btn(barra, "marcar como usado", self.marcar_usado).pack(side="right")

        cx = tk.Frame(col, bg=BG)
        cx.pack(fill="both", expand=True)

        lcx = tk.Frame(cx, bg=PANEL, width=168)
        lcx.pack(side="left", fill="y")
        lcx.pack_propagate(False)
        self.lista = tk.Listbox(lcx, font=F_UI, bg=PANEL, fg=TXT,
                                selectbackground=ACCENT, selectforeground="#ffffff",
                                relief="flat", bd=0, highlightthickness=0,
                                activestyle="none")
        self.lista.pack(fill="both", expand=True, padx=7, pady=7)
        self.lista.bind("<<ListboxSelect>>", lambda _e: self.mostrar_bloco())
        self.lista.bind("<Double-Button-1>", lambda _e: self.copiar_bloco())

        dcx = tk.Frame(cx, bg=PANEL)
        dcx.pack(side="left", fill="both", expand=True, padx=(10, 0))

        cab = tk.Frame(dcx, bg=PANEL)
        cab.pack(fill="x", padx=11, pady=(11, 7))
        self.lbl_bloco = tk.Label(cab, text="", font=F_UI_B, bg=PANEL, fg=ACCENT)
        self.lbl_bloco.pack(side="left")
        self.lbl_chars = tk.Label(cab, text="", font=F_SMALL, bg=PANEL, fg=MUTED)
        self.lbl_chars.pack(side="left", padx=11)
        self.b_copiar = self._btn(cab, "COPIAR BLOCO", self.copiar_bloco,
                                  primario=True, pady=7)
        self.b_copiar.pack(side="right")

        env = tk.Frame(dcx, bg=PANEL)
        env.pack(fill="both", expand=True, padx=11, pady=(0, 11))
        sb = tk.Scrollbar(env, relief="flat", bd=0, bg=PANEL2,
                          troughcolor=PANEL, activebackground=LINE)
        sb.pack(side="right", fill="y")
        self.txt_bloco = tk.Text(env, font=F_MONO, bg=PANEL2, fg=TXT, wrap="word",
                                 relief="flat", bd=0, padx=13, pady=11,
                                 insertbackground=TXT, yscrollcommand=sb.set)
        self.txt_bloco.pack(fill="both", expand=True)
        sb.configure(command=self.txt_bloco.yview)

    # ---------------------------------------------------------------- rodape
    def _rodape(self):
        tk.Frame(self, bg=LINE, height=1).pack(fill="x", padx=16)
        r = tk.Frame(self, bg=BG)
        r.pack(fill="x", padx=16, pady=(8, 12))
        self.pino = tk.Frame(r, bg=OK, width=10, height=10)
        self.pino.pack(side="left", pady=5)
        self.lbl_lint = tk.Label(r, text="", font=F_SMALL, bg=BG, fg=TXT, anchor="w")
        self.lbl_lint.pack(side="left", padx=9)
        self.lbl_toast = tk.Label(r, text="", font=F_UI_B, bg=BG, fg=OK)
        self.lbl_toast.pack(side="right")

    # ------------------------------------------------------------------ acao
    def sortear(self):
        seed = self.var_seed.get().strip()
        self.rng = random.Random(int(seed)) if seed.isdigit() else random.Random()
        self.spec = motor.sortear(self.var_pag.get(), self.rng,
                                  motor._carregar_ledger())
        self._preencher_copy()
        self._marcar_limpo()
        self._render()

    def _preencher_copy(self):
        for i, t in enumerate(self.txt_fala):
            t.delete("1.0", "end")
            t.insert("1.0", self.spec["falas"][i])

    def trocar_eixo(self, chave):
        if not self.spec:
            return
        pool = getattr(motor, dict((e[0], e[2]) for e in EIXOS)[chave])
        opcoes = [x for x in pool if x is not self.spec[chave]] or pool
        self.spec[chave] = self.rng.choice(opcoes)
        if chave == "ocasiao":   # ocasiao alimenta o hook e o eco da cena 4
            self._recopiar_ocasiao()
        self._render()
        self._toast("%s re-sorteado" % chave)

    def _recopiar_ocasiao(self):
        oc = self.spec["ocasiao"]
        self.spec["falas"][0] = self.rng.choice(motor.HOOKS).format(
            evento=oc["plateia_evento"], o=self._orgao(0) or "Johnson")
        self.spec["falas"][3] = self.rng.choice(motor.REDENCOES).format(
            eco=oc["eco"], brag=self.rng.choice(motor.BRAGGING),
            o=self._orgao(3) or "manhood",
            barreira=self.rng.choice(motor.BARREIRAS))
        self._preencher_copy()

    def _orgao(self, i):
        baixo = self.spec["falas"][i].lower()
        return next((n for n in motor.NUCLEO if n.lower() in baixo), None)

    def aplicar_copy(self):
        for i, t in enumerate(self.txt_fala):
            self.spec["falas"][i] = " ".join(t.get("1.0", "end").split())
        self._marcar_limpo()
        self._render()
        self._toast("copy aplicada")

    def marcar_usado(self):
        motor._gravar_ledger(motor._carregar_ledger(), self.spec)
        self._toast("registrado no ledger — não repete tão cedo")

    def _marcar_sujo(self):
        self.lbl_sujo.configure(text="copy editada — clique em aplicar")

    def _marcar_limpo(self):
        self.lbl_sujo.configure(text="")

    # --------------------------------------------------------------- render
    def _render(self):
        for chave, _r, _p, campo in EIXOS:
            v = self.spec[chave]
            if chave == "ocasiao":
                txt = "%s   [%s]" % (v["id"], v["selo"])
            elif chave in ("ref", "vitima", "mulher"):
                txt = "%dy · %s" % (v["idade"], v.get(campo, "?"))
            else:
                txt = v.get(campo, "?")
            self.lbl_eixo[chave].configure(text=txt)

        et = "branca" if "white" in motor.ETNIA[self.spec["pagina"]] else "negra"
        self.lbl_resumo.configure(text=(
            "%s, o colega segura %s murcho no próprio colo enquanto o "
            "narrador aponta e a mesa ri. As cenas 2 a 5 rodam %s. "
            "Elenco de pele %s."
            % (PT_OCASIAO.get(self.spec["ocasiao"]["id"], "Num evento"),
               PT_PROP.get(self.spec["prop"]["id"], "o prop"),
               PT_AMBIENTE.get(self.spec["ambiente"]["id"], "no set interno"), et)))

        self.blocos = motor.montar(self.spec)
        self.achados = motor.lint(self.spec, self.blocos)

        for i, t in enumerate(self.txt_fala):
            n = motor._palavras(self.spec["falas"][i])
            teto = motor.TETO_FALA[i + 1]
            t.contador.configure(text="%d/%d palavras" % (n, teto),
                                 fg=AVISO if n > teto else MUTED)

        sel = self.lista.curselection()
        idx = sel[0] if sel else 0
        self.lista.delete(0, "end")
        for nome in self._ordem():
            self.lista.insert("end", "  " + nome.replace("/05", ""))
        self.lista.selection_set(min(idx, self.lista.size() - 1))
        self.mostrar_bloco()

        erros = [a for a in self.achados if a[0] == "ERRO"]
        if not self.achados:
            self.pino.configure(bg=OK)
            self.lbl_lint.configure(text="LINTER OK — nenhuma violação mecânica.", fg=OK)
        else:
            self.pino.configure(bg=ERRO if erros else AVISO)
            self.lbl_lint.configure(
                text="   ·   ".join("%s" % a[1] for a in self.achados[:2]),
                fg=ERRO if erros else AVISO)

    def _ordem(self):
        return (["BLOCO 0 (REF)"]
                + sorted(k for k in self.blocos if k.startswith("IMAGE"))
                + sorted(k for k in self.blocos if k.startswith("TAKE")))

    def _nome_sel(self):
        sel = self.lista.curselection()
        return self._ordem()[sel[0]] if sel else self._ordem()[0]

    def mostrar_bloco(self):
        nome = self._nome_sel()
        txt = self.blocos[nome]
        self.lbl_bloco.configure(text=nome)
        self.lbl_chars.configure(text="%d caracteres" % len(txt))
        self.txt_bloco.delete("1.0", "end")
        self.txt_bloco.insert("1.0", txt)

    # ---------------------------------------------------------------- copiar
    def _clip(self, texto):
        self.clipboard_clear()
        self.clipboard_append(texto)
        self.update()

    def _piscar(self, btn, cor_final=None):
        orig = btn.cget("bg")
        btn.configure(bg=OK, fg="#0f1116")
        self.after(430, lambda: btn.configure(bg=cor_final or orig,
                                              fg="#ffffff" if orig == ACCENT else TXT))

    def copiar_bloco(self):
        self._clip(self.txt_bloco.get("1.0", "end").rstrip())
        self._piscar(self.b_copiar, ACCENT)
        self._toast("%s copiado" % self._nome_sel())

    def copiar_grupo(self, prefixo):
        nomes = sorted(k for k in self.blocos if k.startswith(prefixo))
        self._clip("\n\n".join(self.blocos[n] for n in nomes))
        self._piscar(self.b_img if prefixo == "IMAGE" else self.b_tak)
        self._toast("%d blocos %s copiados" % (len(nomes), prefixo))

    def salvar(self):
        cam = filedialog.asksaveasfilename(
            defaultextension=".txt", filetypes=[("Texto", "*.txt")],
            initialfile="flagrante_%s_%s.txt" % (self.spec["pagina"],
                                                 self.spec["ocasiao"]["id"]))
        if not cam:
            return
        with open(cam, "w", encoding="utf-8") as f:
            for nome in self._ordem():
                f.write(nome + "\n" + self.blocos[nome] + "\n\n")
        self._toast("salvo em %s" % os.path.basename(cam))

    def _toast(self, msg):
        self.lbl_toast.configure(text=msg)
        self.after(2600, lambda: self.lbl_toast.configure(text=""))


if __name__ == "__main__":
    App().mainloop()
