#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""AGENTE OCTOPUS 5 — app desktop offline.

⛔⛔ NAO USA O `ui_agente.py`, E ISSO E' DECISAO, NAO PREGUICA.
   A interface compartilhada monta o combobox de pagina direto de
   `motor.ETNIA` no construtor, sem guarda, e desenha em volta disso os
   botoes de REF, sexo, MODO BELA e MODO FORTE. Este agente nao tem NENHUM
   desses eixos: nao ha' pagina, nem etnia, nem pessoa sorteavel — o elenco e'
   um bebe generico e o produto e' uma string travada.
   Para passar por la' eu teria de inventar um `ETNIA` falso, e o painel
   abriria com meia duzia de controles MORTOS. A doutrina da casa e' explicita:
   botao que nao troca nada e' pior que botao nenhum.

⭐ O QUE ESTE PAINEL DESENHA, e so' isto porque so' isto existe:
   · quantos videos e a seed
   · CINCO pre-selecoes, uma por slot de take: deixe em `sorteio` ou trave uma
     cena especifica. E' o mesmo mecanismo de eixo pre-selecionavel do
     `sem_mecanismo` do BANHO 16 3T — variavel confundida vira eixo, nunca
     palpite.
   · a legenda: sorteada ou escolhida da lista
   · o texto pronto, com botao de copiar

⚠️ O ledger acompanha o EXECUTAVEL, nao a pasta temporaria do PyInstaller.
   Sem esta linha o `.exe` esqueceria o repertorio a cada abertura e o
   anti-repeticao viraria enfeite.

    python funil-organico/octopus5_app.py
"""

import os
import random
import sys
import tkinter as tk
from tkinter import ttk

if getattr(sys, "frozen", False):          # rodando como .exe do PyInstaller
    sys.path.insert(0, sys._MEIPASS)
    BASE = os.path.dirname(os.path.abspath(sys.executable))
else:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    BASE = os.path.dirname(os.path.abspath(__file__))

import octopus5 as motor                   # noqa: E402

motor.LEDGER = os.path.join(BASE, ".octopus-5-ledger.json")

BG, SURFACE, SURFACE2 = "#0e1a18", "#12211f", "#193029"
INK, DIM, MUT = "#e8fffb", "#9fc7bf", "#6f918a"
AQUA, GOLD = "#2fe0c8", "#e8b04b"
FT = ("Segoe UI", 9)
SORTEIO = "sorteio"


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("%s  v1.0" % motor.TITULO)
        self.configure(bg=BG)
        self.geometry("1080x760")
        self.minsize(920, 640)

        st = ttk.Style(self)
        try:
            st.theme_use("clam")
        except tk.TclError:
            pass
        st.configure("O.TCombobox", fieldbackground=SURFACE2,
                     background=SURFACE2, foreground=INK,
                     arrowcolor=AQUA, bordercolor=SURFACE2, relief="flat")

        cab = tk.Frame(self, bg=SURFACE)
        cab.pack(fill="x")
        tk.Label(cab, text="OCTOPUS", bg=SURFACE, fg=INK,
                 font=("Segoe UI", 17, "bold")).pack(side="left", padx=(14, 4),
                                                     pady=10)
        tk.Label(cab, text="5", bg=SURFACE, fg=AQUA,
                 font=("Segoe UI", 17, "bold")).pack(side="left")
        tk.Label(cab, text="  5 takes de 4s  ·  AdBatch Vertical 5  ·  sem fala",
                 bg=SURFACE, fg=MUT, font=FT).pack(side="left", padx=8)

        ctl = tk.Frame(self, bg=BG)
        ctl.pack(fill="x", padx=14, pady=(12, 6))

        tk.Label(ctl, text="videos", bg=BG, fg=DIM, font=FT).pack(side="left")
        self.sp_n = tk.Spinbox(ctl, from_=1, to=50, width=4, font=FT,
                               bg=SURFACE2, fg=INK, relief="flat",
                               buttonbackground=SURFACE2, justify="center",
                               insertbackground=INK)
        self.sp_n.delete(0, "end")
        self.sp_n.insert(0, "5")
        self.sp_n.pack(side="left", padx=(6, 16), ipady=2)

        tk.Label(ctl, text="seed", bg=BG, fg=DIM, font=FT).pack(side="left")
        self.ent_seed = tk.Entry(ctl, width=8, font=FT, bg=SURFACE2, fg=INK,
                                 relief="flat", justify="center",
                                 insertbackground=INK)
        self.ent_seed.pack(side="left", padx=(6, 16), ipady=2)
        tk.Label(ctl, text="(vazio = aleatorio)", bg=BG, fg=MUT,
                 font=("Segoe UI", 8)).pack(side="left")

        self.bt = tk.Button(ctl, text="Gerar", command=self._gerar, font=FT,
                            relief="flat", bd=0, cursor="hand2", padx=22,
                            pady=5, bg=AQUA, fg="#04231f",
                            activebackground="#4df0da")
        self.bt.pack(side="right")
        tk.Button(ctl, text="Copiar", command=self._copiar, font=FT,
                  relief="flat", bd=0, cursor="hand2", padx=16, pady=5,
                  bg=SURFACE2, fg=INK, activebackground=SURFACE
                  ).pack(side="right", padx=(0, 8))

        # ---- as cinco pre-selecoes ----
        eix = tk.Frame(self, bg=SURFACE)
        eix.pack(fill="x", padx=14, pady=(0, 8))
        tk.Label(eix, text="PRE-SELECAO POR TAKE", bg=SURFACE, fg=MUT,
                 font=("Segoe UI", 8, "bold")).pack(anchor="w", padx=10,
                                                    pady=(8, 2))
        linha = tk.Frame(eix, bg=SURFACE)
        linha.pack(fill="x", padx=10, pady=(0, 10))
        self.cbs = []
        for i in range(motor.N_TAKES):
            col = tk.Frame(linha, bg=SURFACE)
            col.pack(side="left", fill="x", expand=True, padx=(0, 8))
            tk.Label(col, text="%d · %s" % (i + 1, motor.NOMES_TAKE[i]),
                     bg=SURFACE, fg=GOLD, font=("Segoe UI", 8, "bold"),
                     anchor="w").pack(fill="x")
            vals = [SORTEIO] + [c["id"] for c in motor.POOLS[i]]
            cb = ttk.Combobox(col, style="O.TCombobox", values=vals,
                              state="readonly", font=FT)
            cb.set(SORTEIO)
            cb.pack(fill="x", pady=(2, 0))
            # ⚠️ a roda do mouse TROCA o valor de um combobox readonly, e o
            # operador ja' perdeu uma trava assim no painel do editor (21/08).
            for ev in ("<MouseWheel>", "<Button-4>", "<Button-5>"):
                cb.bind(ev, lambda _e: "break")
            self.cbs.append(cb)

        leg = tk.Frame(self, bg=BG)
        leg.pack(fill="x", padx=14, pady=(0, 8))
        tk.Label(leg, text="legenda", bg=BG, fg=DIM, font=FT).pack(side="left")
        self.cb_leg = ttk.Combobox(
            leg, style="O.TCombobox", state="readonly", font=FT,
            values=[SORTEIO] + [l.split("\n")[0] for l in motor.LEGENDAS])
        self.cb_leg.set(SORTEIO)
        self.cb_leg.pack(side="left", fill="x", expand=True, padx=(6, 0))
        for ev in ("<MouseWheel>", "<Button-4>", "<Button-5>"):
            self.cb_leg.bind(ev, lambda _e: "break")

        cx = tk.Frame(self, bg=BG)
        cx.pack(fill="both", expand=True, padx=14, pady=(0, 12))
        self.txt = tk.Text(cx, bg=SURFACE, fg=INK, relief="flat", bd=0,
                           font=("Consolas", 9), wrap="word",
                           insertbackground=INK, padx=12, pady=10)
        sb = tk.Scrollbar(cx, command=self.txt.yview, relief="flat", bd=0,
                          bg=SURFACE2, troughcolor=BG,
                          activebackground=AQUA)
        self.txt.configure(yscrollcommand=sb.set)
        sb.pack(side="right", fill="y")
        self.txt.pack(side="left", fill="both", expand=True)

        self.lb = tk.Label(self, text="pronto", bg=SURFACE, fg=MUT, font=FT,
                           anchor="w", padx=12)
        self.lb.pack(fill="x")

    # -----------------------------------------------------------------
    def _travar(self, v):
        """⭐ Aplica a pre-selecao DEPOIS do sorteio, nao antes.

        ⛔ Trocar a cena ja' sorteada mantem o ledger consistente: ele registra
        o que o motor escolheu, e a trava e' decisao do operador por cima. Se
        eu filtrasse a pool antes, uma trava fixa por muitos videos envenenaria
        a memoria anti-repeticao dos outros slots.
        """
        for i, cb in enumerate(self.cbs):
            alvo = cb.get()
            if alvo and alvo != SORTEIO:
                for c in motor.POOLS[i]:
                    if c["id"] == alvo:
                        v["cenas"][i] = c
                        break
        alvo_leg = self.cb_leg.get()
        if alvo_leg and alvo_leg != SORTEIO:
            for l in motor.LEGENDAS:
                if l.split("\n")[0] == alvo_leg:
                    # o emoji continua sorteado: e' o unico eixo de cor
                    v["legenda"] = l + v["legenda"][-1]
                    break
        return v

    def _gerar(self):
        try:
            n = max(1, min(50, int(self.sp_n.get())))
        except ValueError:
            n = 5
        s = self.ent_seed.get().strip()
        try:
            seed = int(s) if s else None
        except ValueError:
            seed = None
        rng = random.Random(seed)
        led = motor._carregar_ledger()

        partes, reprovados = [], 0
        for k in range(n):
            v = self._travar(motor.montar(rng, led))
            p = motor.lint(v)
            if p:
                reprovados += 1
                partes.append("REPROVADO pela lente: %s\n" % "; ".join(p))
                continue
            partes.append(motor.render(v, k + 1))
        motor._salvar_ledger(led)

        self.txt.delete("1.0", "end")
        self.txt.insert("1.0", "\n".join(partes))
        self.lb.configure(
            text="%d video(s) gerado(s)%s" % (n - reprovados,
                                              "" if not reprovados else
                                              "  ·  %d reprovado(s) pela lente"
                                              % reprovados),
            fg=GOLD if reprovados else MUT)

    def _copiar(self):
        t = self.txt.get("1.0", "end-1c")
        if not t.strip():
            return
        self.clipboard_clear()
        self.clipboard_append(t)
        self.lb.configure(text="copiado (%d caracteres)" % len(t), fg=AQUA)


if __name__ == "__main__":
    App().mainloop()
