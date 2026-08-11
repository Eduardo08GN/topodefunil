#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ui_agente.py — a interface tkinter COMPARTILHADA dos apps de agente.

Uma so' interface serve todos os agentes portados. Cada motor
(<agente>_lucas.py) declara o que e' proprio dele:

    TITULO, SUBTITULO   — o cabecalho
    EIXOS_UI            — [(chave, rotulo, nome_do_pool, campo_exibido), ...]
    CENAS_UI            — os 5 rotulos das falas
    resumo_pt(spec)     — a frase em portugues que descreve o video sorteado
    EIXOS_QUE_MEXEM_NA_COPY — {chave: funcao(app)} para reescrever falas
                              dependentes quando aquele eixo e' re-sorteado

...mais a API que o gerador ja' expoe: ETNIA, sortear, montar, lint,
_carregar_ledger, _gravar_ledger, NUCLEO, TETO_FALA, _palavras, LEDGER.

⭐ TRES CONTRATOS OPCIONAIS DE TRAVA (2026-08-03; o 3o em 2026-08-05) — todos
lidos com `getattr(motor, ...)`, entao motor que nao declara nada nao ve' nada e
nao muda de comportamento. E' obrigatorio: esta interface e' compartilhada por
todos os agentes SHORT.

    PELE_TRAVAVEL    True = a etnia deste motor e' LIVRE (nao vem da pagina) e
                     o seletor clara/escura do painel vira TRAVA de verdade:
                     entra em `sortear(..., travas)` como travas["pele"].

    TRAVAS_UI        [(chave, rotulo, [opcoes])] — PRE-SELECAO. O painel desenha
                     `livre | opcao | opcao` no topo; o que nao estiver em
                     `livre` entra em `sortear(..., travas)`.
    EIXOS_TRAVAVEIS  [chave, ...] — CADEADO por eixo, ao lado do `trocar`.
                     Cadeado fechado = aquele eixo NAO e' re-sorteado no SORTEAR
                     VIDEO: o valor que esta' na tela e' devolvido ao motor
                     dentro de `travas`, e o motor remonta o video em volta
                     dele. ⚠️ E' o motor que reconstroi, nao a UI que congela a
                     chave: eixo travado costuma mandar em coisas derivadas (no
                     CLEAN o item da copy manda na bancada e no despejo), e
                     congelar por fora deixa o video incoerente consigo mesmo.

⚠️ Declarar qualquer um dos dois implica que `sortear()` daquele motor aceita o
quarto argumento `travas`.

Duplicar esta interface por agente seria o mesmo erro que a regra P9 proibe
na doutrina: copia envelhece e mente.
"""

import os
import random
import sys
import tkinter as tk
from tkinter import filedialog, ttk

from nucleo_sonoro import termos_reescritos, ATIVA


def paginas_por_pele(motor):
    """{'clara': [...], 'escura': [...]} a partir do mapa ETNIA do motor.

    A pele NAO e' um eixo independente: a congruencia de etnia (REF = avatar da
    pagina) e' inviolavel. Entao o seletor de pele escolhe uma PAGINA daquela
    pele — nunca troca a etnia deixando a pagina para tras.
    """
    g = {"clara": [], "escura": []}
    for pag, et in sorted(motor.ETNIA.items()):
        g["clara" if "white" in et else "escura"].append(pag)
    return g


def base_dir():
    """Pasta ao lado do .exe (congelado) ou do .py (solto)."""
    if getattr(sys, "frozen", False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))


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

ASSINATURA = "by Eddie"

# o rotulo do "sem pre-selecao" do TRAVAS_UI. Constante porque ele e' comparado,
# nao so' exibido: `sortear` so' manda a trava quando o valor NAO e' este.
LIVRE = "livre"

F_UI = ("Segoe UI", 10)
F_UI_B = ("Segoe UI Semibold", 10)
F_TIT = ("Segoe UI Semibold", 17)
# a assinatura da familia — mesma do Veo Editor. Mora AQUI e so' aqui: vale
# para os quatro agentes portados e para os que vierem, sem tocar em motor.
F_ASSIN = ("Segoe UI", 12)
F_PASSO = ("Segoe UI Semibold", 9)
F_MONO = ("Consolas", 10)
F_SMALL = ("Segoe UI", 9)


class App(tk.Tk):
    def __init__(self, motor):
        super().__init__()
        self.m = motor
        self.title("%s %s  v1.2" % (motor.TITULO, ASSINATURA))
        self.configure(bg=BG)
        self.geometry("1360x900")
        self.minsize(1180, 760)

        self.spec = None
        self.blocos = {}
        self.achados = []
        self.rng = random.Random()

        # os dois contratos de trava, resolvidos UMA vez (ver o cabecalho).
        # ⚠️ `getattr` com default: os outros nove motores nao declaram nenhum
        # dos dois e nao podem quebrar por causa disso.
        self.travas_ui = list(getattr(motor, "TRAVAS_UI", []) or [])
        self.eixos_travaveis = list(getattr(motor, "EIXOS_TRAVAVEIS", []) or [])
        # ⭐ 3o contrato aditivo (2026-08-05): PELE_TRAVAVEL. Nos motores de
        # etnia POR PAGINA o seletor de pele funciona trocando a pagina; no
        # CLEAN V2 a etnia e' livre (sai do MUNDO) e a troca de pagina nao
        # muda nada — o botao acendia e o sorteio seguia aleatorio. Motor que
        # declara a flag recebe travas["pele"] e remonta o video em volta.
        self.pele_travavel = bool(getattr(motor, "PELE_TRAVAVEL", False))
        # ⭐ 4o contrato aditivo (2026-08-05): MODO_BELA. Ordem do operador,
        # lendo os lotes do DUPLA e do PLACA: *"gostei muito da ideia de ref
        # feminina lindas super models com corpao e pouca roupa. Estou pensando
        # em colocar um toggle de trava pra modo ref mulher bela em todos os ui
        # ux pertinentes dos agentes shorts"*. Motor que declara recebe
        # travas["bela"] e remonta a REF, a roupa e a clausula do rosto.
        # ⭐ Dois modos, mesmo contrato: `MODO_BELA` (mulher super model) e
        # `MODO_FORTE` (homem musculoso). Ordem do operador, 2026-08-05.
        # ⛔ Guardados num dicionario e nao em dois atributos: um terceiro modo
        # amanha nao pode custar mais um par de `if` espalhado pela classe.
        # ⭐ 2026-08-10: o TERCEIRO modo, e ele NAO e' de REF — e' de CENA.
        # `MODO_RECEITA` (WIFE 16) poe a tigela de cubos e a caixa de
        # bicarbonato na borda da agua e o homem MEXENDO. O comentario acima
        # ja' previa isto: "um terceiro modo amanha nao pode custar mais um
        # par de `if` espalhado pela classe" — e nao custou, so' entrou na
        # tupla. ⚠️ ADITIVO: motor que nao declara a flag nao ganha botao, e
        # por isso os outros 33 nao mudam de comportamento.
        self.modos = [m for m in ("bela", "forte", "receita")
                      if getattr(motor, "MODO_%s" % m.upper(), False)]
        # ⭐ 5o contrato aditivo (2026-08-10): MODOS_DEFAULT — quais modos
        # nascem LIGADOS. Ordem do operador para o GOOD 16: *"toggle marcado
        # como default"* no modo FORTE.
        # ⛔ Ate' aqui TODO modo nascia desligado, e um motor que quisesse o
        # contrario so' poderia consegui-lo mentindo no `sortear` (ligando o
        # modo sem trava) — o botao apagado e o video ligado, que e' a
        # forma-sem-funcao ao contrario e pior: o operador desliga e nada muda.
        # ⚠️ ADITIVO e lido com `getattr`: motor que nao declara `MODOS_DEFAULT`
        # continua nascendo com TUDO desligado, e por isso nenhum dos outros
        # motores muda de comportamento (medido nos 33, nao prometido).
        _padrao = tuple(getattr(motor, "MODOS_DEFAULT", ()) or ())
        self.modo_on = {m: (m in _padrao) for m in self.modos}
        self.pele_travada = None
        # ⚠️ defaults ANTES de montar a tela: `travas()` consulta os dois, e
        # quem monta os botoes e' o `_topo()`, que roda depois daqui.
        self.sexos, self.b_sexo, self.sexo_travado = [], {}, None
        self.var_trava = {}
        self.var_cadeado = {}
        self.b_cadeado = {}

        self._estilos()
        self._topo()
        corpo = tk.Frame(self, bg=BG)
        corpo.pack(fill="both", expand=True, padx=16, pady=(0, 8))
        self._coluna_esq(corpo)
        self._coluna_dir(corpo)
        self._rodape()

        self.bind("<Control-r>", lambda _e: self.sortear())
        self.bind("<Control-s>", lambda _e: self.salvar())

        # ⭐⭐ ATALHOS DE COPIA — 2026-08-08, para o Piloto AdBatch.
        # ⛔ POR QUE ELES EXISTEM. O piloto (AutoHotkey) precisava CLICAR nos
        # botoes da secao 3, e clique depende de coordenada de tela. Medido no
        # dia: o layout desta janela e' mais LARGO que o monitor vertical de
        # 1080px, entao `COPIAR BLOCO` e `marcar como usado` ficam CORTADOS na
        # borda — nao ha' coordenada valida para eles ali. E a janela nao
        # reflui: ela so' clipa.
        # ⭐ Com atalho, o piloto nao precisa de coordenada NENHUMA deste lado:
        # ativa a janela e manda a tecla. Sai a fragilidade inteira.
        # ⚠️ `Control-0` e' o que o AdBatch de fato quer — ele tem UMA caixa
        # ("Cole o roteiro inteiro") e parseia REF/IMAGE/TAKE de dentro dela.
        # Copiar em tres pedacos e remontar do lado de fora era trabalho a toa.
        self.bind("<Control-Key-0>", lambda _e: self.copiar_tudo())
        self.bind("<Control-Key-1>", lambda _e: self.copiar_ref())
        self.bind("<Control-Key-2>", lambda _e: self.copiar_grupo("IMAGE"))
        self.bind("<Control-Key-3>", lambda _e: self.copiar_grupo("TAKE"))
        self.bind("<Control-Key-4>", lambda _e: self.marcar_usado())

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
        return tk.Button(pai, text=texto, command=cmd,
                         font=F_UI_B if primario else F_UI,
                         bg=ACCENT if primario else PANEL2,
                         fg="#ffffff" if primario else TXT,
                         activebackground=ACCENT_D if primario else LINE,
                         activeforeground="#ffffff",
                         relief="flat", bd=0, cursor="hand2", padx=15, pady=pady)

    def _passo(self, pai, num, titulo, dica):
        c = tk.Frame(pai, bg=BG)
        c.pack(fill="x", pady=(14, 6))
        tk.Label(c, text=" %s " % num, font=F_PASSO, bg=ACCENT,
                 fg="#ffffff", padx=4).pack(side="left", ipady=1)
        tk.Label(c, text=titulo, font=F_UI_B, bg=BG, fg=TXT).pack(side="left", padx=(8, 0))
        tk.Label(c, text=dica, font=F_SMALL, bg=BG, fg=MUTED).pack(side="left", padx=(10, 0))

    # ------------------------------------------------------------------ topo
    def _topo(self):
        t = tk.Frame(self, bg=BG)
        t.pack(fill="x", padx=16, pady=(12, 4))

        a, b = self.m.TITULO.split(" ", 1) if " " in self.m.TITULO else (self.m.TITULO, "")
        tk.Label(t, text=a, font=F_TIT, bg=BG, fg=TXT).pack(side="left")
        if b:
            tk.Label(t, text=b, font=F_TIT, bg=BG, fg=ACCENT).pack(side="left", padx=(7, 0))
        # a assinatura acompanha o nome, mas em peso menor: nao disputa com o
        # agente, so' fecha a marca. Mesma logica do "Veo Editor by Eddie".
        tk.Label(t, text=ASSINATURA, font=F_ASSIN, bg=BG,
                 fg=MUTED).pack(side="left", padx=(8, 0), pady=(4, 0))
        tk.Label(t, text=self.m.SUBTITULO, font=F_SMALL, bg=BG,
                 fg=MUTED).pack(side="left", padx=(14, 0), pady=(7, 0))

        cx = tk.Frame(t, bg=BG)
        cx.pack(side="right")
        self._btn(cx, "SORTEAR VÍDEO   Ctrl+R", self.sortear,
                  primario=True, pady=8).pack(side="right")
        tk.Label(cx, text="seed", font=F_SMALL, bg=BG,
                 fg=MUTED).pack(side="right", padx=(16, 5))
        self.var_seed = tk.StringVar()
        tk.Entry(cx, textvariable=self.var_seed, width=7, font=F_UI, bg=PANEL2,
                 fg=TXT, insertbackground=TXT, relief="flat",
                 justify="center").pack(side="right", ipady=6)
        self.var_pag = tk.StringVar(value=sorted(self.m.ETNIA)[0])
        cb = ttk.Combobox(cx, textvariable=self.var_pag, values=sorted(self.m.ETNIA),
                          state="readonly", width=9, font=F_UI)
        cb.pack(side="right", padx=(0, 14), ipady=4)
        cb.bind("<<ComboboxSelected>>", lambda _e: self._escolher_pagina())
        tk.Label(cx, text="página", font=F_SMALL, bg=BG,
                 fg=MUTED).pack(side="right", padx=(0, 5))

        # seletor de PELE — troca para uma pagina congruente com a pele escolhida
        self.grupos = paginas_por_pele(self.m)
        self.b_pele = {}
        for pele in ("escura", "clara"):
            b = tk.Button(cx, text=pele, font=F_SMALL, relief="flat", bd=0,
                          cursor="hand2", padx=12, pady=5,
                          command=lambda k=pele: self.trocar_pele(k))
            b.pack(side="right", padx=(0, 2))
            self.b_pele[pele] = b
        tk.Label(cx, text="pele", font=F_SMALL, bg=BG,
                 fg=MUTED).pack(side="right", padx=(0, 6))

        # ⭐⭐ SELETOR DE SEXO DE QUEM NARRA (2026-08-06). Ordem do operador:
        # *"assim como existe o botao de pele clara e escura, tambem haja o
        # botao de selecionar homem ou mulher para deixar travado"*.
        # ⛔ So' aparece nos motores que DECLARAM os dois sexos em `SEXOS` —
        # e' a marcacao que ele pediu na mesma mensagem. Nos treze que so'
        # produzem um sexo o botao nao existe: botao que nao muda nada e' a
        # forma-sem-funcao que o botao de pele ja' custou caro.
        # ⚠️ E nao aparece onde o sexo JA' e' eixo de pre-selecao (`sexo` em
        # TRAVAS_UI, como no CLEAN): dois controles para a mesma trava e' a
        # cópia espelhada que diverge na semana seguinte.
        self.b_sexo = {}
        self.sexo_travado = None
        # ⛔ `self.m`, nunca `motor`: `_topo` nao recebe o motor por parametro,
        # e o NameError so' estourava ao ABRIR o painel — 16 dos 19 apps
        # entregues quebrados na cara do operador, enquanto o verificador
        # media o motor e dizia tudo verde. UI tambem e' funcao: verificar
        # entrega passa a abrir a janela (sonda_ui), nao so' importar o motor.
        _ja_e_eixo = any(t[0] == "sexo" for t in self.travas_ui)
        self.sexos = ([] if _ja_e_eixo
                      else list(getattr(self.m, "SEXOS", []) or []))
        if len(self.sexos) > 1:
            for _s in reversed(self.sexos):
                b = tk.Button(cx, text=_s, font=F_SMALL, relief="flat", bd=0,
                              cursor="hand2", padx=12, pady=5,
                              command=lambda k=_s: self.trocar_sexo(k))
                b.pack(side="right", padx=(0, 2))
                self.b_sexo[_s] = b
            tk.Label(cx, text="narra", font=F_SMALL, bg=BG,
                     fg=MUTED).pack(side="right", padx=(0, 6))

        # ⭐⭐ OS TOGGLES — so' os que o motor declara.
        # ⚠️ O texto NAO e' mais `ref <modo>` para todos: `bela` e `forte`
        # trocam a PESSOA (sao modos de REF), mas `receita` troca a CENA. Um
        # botao escrito "ref receita" prometeria trocar alguem.
        self.b_modo = {}
        for _m in reversed(self.modos):
            _txt = _m if _m in self.MODOS_DE_CENA else "ref %s" % _m
            b = tk.Button(cx, text=_txt, font=F_SMALL, relief="flat",
                          bd=0, cursor="hand2", padx=12, pady=5,
                          command=lambda k=_m: self.alternar_modo(k))
            b.pack(side="right", padx=(0, 4))
            self.b_modo[_m] = b
        if self.modos:
            tk.Label(cx, text="modo", font=F_SMALL, bg=BG,
                     fg=MUTED).pack(side="right", padx=(14, 6))
            self._pintar_modos()

        self._barra_travas()
        tk.Frame(self, bg=LINE, height=1).pack(fill="x", padx=16, pady=(10, 0))

    def _barra_travas(self):
        """A pre-selecao do TRAVAS_UI — `livre | opcao | opcao` por eixo.

        ⛔ Nao desenha NADA quando o motor nao declara TRAVAS_UI: nove dos dez
        agentes nao declaram, e o painel deles tem de continuar igual ao pixel.
        ⚠️ O default e' `livre` em todos, entao abrir o app e clicar em SORTEAR
        VÍDEO devolve exatamente o mesmo comportamento de antes desta barra.
        """
        if not self.travas_ui:
            return
        f = tk.Frame(self, bg=BG)
        f.pack(fill="x", padx=16, pady=(9, 0))
        tk.Label(f, text="pré-seleção", font=F_SMALL, bg=BG,
                 fg=MUTED).pack(side="left", padx=(0, 10))
        for chave, rotulo, opcoes in self.travas_ui:
            self.var_trava[chave] = tk.StringVar(value=LIVRE)
            tk.Label(f, text=rotulo, font=F_SMALL, bg=BG,
                     fg=TXT).pack(side="left", padx=(6, 5))
            grupo = []
            # ⛔ DEDUPE, e ele conserta um defeito VISIVEL: esta barra ja'
            # prepende o `livre`, e os motores declaram `["livre"] + POOL` —
            # entao o botao saia DUPLICADO, dois `livre` laranja lado a lado.
            # ⚠️ Achado em 2026-08-04 LENDO O PRINT do .exe do RECEITA, nao por
            # teste: nenhum smoke test olha para pixel, e o COLO carregava o
            # mesmo defeito desde que a barra nasceu.
            # ⚠️ Corrigido AQUI e nao nos motores de proposito (P9): assim vale
            # para o COLO sem toca-lo e para todo agente que nascer copiando o
            # `TRAVAS_UI` dele — que e' exatamente como este nasceu.
            vistos = set()
            ordenadas = [o for o in [LIVRE] + list(opcoes)
                         if not (o in vistos or vistos.add(o))]
            for op in ordenadas:
                b = tk.Button(f, text=op, font=F_SMALL, relief="flat", bd=0,
                              cursor="hand2", padx=11, pady=4)
                b.configure(command=lambda c=chave, o=op, g=grupo:
                            self._escolher_trava(c, o, g))
                b.pack(side="left", padx=(0, 2))
                grupo.append((op, b))
            self._pintar_trava(chave, grupo)

    def _escolher_trava(self, chave, opcao, grupo):
        self.var_trava[chave].set(opcao)
        self._pintar_trava(chave, grupo)
        self.sortear()

    def _pintar_trava(self, chave, grupo):
        atual = self.var_trava[chave].get()
        for op, b in grupo:
            on = (op == atual)
            b.configure(bg=ACCENT if on else PANEL2,
                        fg="#ffffff" if on else MUTED,
                        activebackground=ACCENT_D if on else LINE,
                        activeforeground="#ffffff")

    # -------------------------------------------------------------- esquerda
    def _rolagem(self, pai, largura):
        """Devolve um Frame que ROLA dentro de uma coluna de largura fixa.

        ⚠️ Sem isto a coluna e' um Frame de altura fixa e o que nao coubesse na
        janela ficava simplesmente inalcancavel — nos agentes de 5 cenas o
        botao `aplicar copy e revalidar` some abaixo da borda, e nao ha' como
        chegar nele (relatado em producao, 2026-08-02).
        """
        ext = tk.Frame(pai, bg=BG, width=largura)
        ext.pack(side="left", fill="y")
        ext.pack_propagate(False)

        cv = tk.Canvas(ext, bg=BG, highlightthickness=0, bd=0)
        sb = tk.Scrollbar(ext, orient="vertical", command=cv.yview,
                          relief="flat", bd=0, bg=PANEL2,
                          troughcolor=PANEL, activebackground=LINE)
        cv.configure(yscrollcommand=sb.set)
        sb.pack(side="right", fill="y")
        cv.pack(side="left", fill="both", expand=True)

        col = tk.Frame(cv, bg=BG)
        jan = cv.create_window((0, 0), window=col, anchor="nw")
        # ⚠️ O frame interno TEM de acompanhar a largura do canvas: dentro de um
        # canvas ele nao herda largura nenhuma, e todo `fill="x"` colapsaria
        # para o tamanho do texto.
        cv.bind("<Configure>", lambda e: cv.itemconfigure(jan, width=e.width))
        col.bind("<Configure>",
                 lambda _e: cv.configure(scrollregion=cv.bbox("all")))

        def roda(e):
            caixa = cv.bbox("all")
            if caixa and caixa[3] > cv.winfo_height():   # so' rola se precisar
                cv.yview_scroll(int(-e.delta / 120), "units")
            return "break"

        # ⚠️ `bind_all` so' enquanto o ponteiro esta' sobre a coluna. Um bind
        # global permanente roubaria a roda do Text da direita.
        ext.bind("<Enter>", lambda _e: ext.bind_all("<MouseWheel>", roda))
        ext.bind("<Leave>", lambda _e: ext.unbind_all("<MouseWheel>"))
        return col

    def _coluna_esq(self, pai):
        # a barra come' ~15px: as wraplength daqui pra baixo contam com isso
        col = self._rolagem(pai, 490)

        self._passo(col, 1, "O vídeo sorteado", "não gostou de um eixo? troque só ele")

        res = tk.Frame(col, bg=PANEL2)
        res.pack(fill="x")
        self.lbl_resumo = tk.Label(res, text="", font=F_UI, bg=PANEL2, fg=TXT,
                                   wraplength=435, justify="left", anchor="w",
                                   padx=14, pady=11)
        self.lbl_resumo.pack(fill="x")

        cx = tk.Frame(col, bg=PANEL)
        cx.pack(fill="x", pady=(2, 0))
        self.lbl_eixo = {}
        for i, (chave, rotulo, _p, _c) in enumerate(self.m.EIXOS_UI):
            lin = tk.Frame(cx, bg=PANEL)
            lin.pack(fill="x", padx=13, pady=(9 if i == 0 else 4, 4))
            tk.Label(lin, text=rotulo, font=F_SMALL, bg=PANEL, fg=MUTED,
                     width=10, anchor="w").pack(side="left")
            tk.Button(lin, text="trocar", font=F_SMALL, bg=PANEL2, fg=ACCENT,
                      activebackground=LINE, activeforeground=ACCENT,
                      relief="flat", bd=0, cursor="hand2", padx=10, pady=2,
                      command=lambda c=chave: self.trocar_eixo(c)).pack(side="right")
            # ⭐ o CADEADO, a' esquerda do `trocar` — so' nos eixos que o motor
            # declarou travaveis. Motor sem EIXOS_TRAVAVEIS nao ganha botao.
            if chave in self.eixos_travaveis:
                self.var_cadeado[chave] = tk.BooleanVar(value=False)
                bc = tk.Button(lin, text="trava", font=F_SMALL, relief="flat",
                               bd=0, cursor="hand2", padx=9, pady=2)
                bc.configure(command=lambda c=chave: self.alternar_cadeado(c))
                bc.pack(side="right", padx=(0, 7))
                self.b_cadeado[chave] = bc
                self._pintar_cadeado(chave)
            v = tk.Label(lin, text="—", font=F_UI_B, bg=PANEL, fg=TXT,
                         anchor="w", wraplength=300, justify="left")
            v.pack(side="left", fill="x", expand=True)
            self.lbl_eixo[chave] = v
        tk.Frame(cx, bg=PANEL, height=8).pack()

        self._passo(col, 2, "A copy", "edite à vontade — copy é sua, o app só confere")

        cc = tk.Frame(col, bg=PANEL)
        cc.pack(fill="both", expand=True)
        self.txt_fala = []
        for i, nome in enumerate(self.m.CENAS_UI):
            cab = tk.Frame(cc, bg=PANEL)
            cab.pack(fill="x", padx=13, pady=(9 if i == 0 else 6, 2))
            tk.Label(cab, text=nome, font=F_SMALL, bg=PANEL,
                     fg=ACCENT, anchor="w").pack(side="left")
            cont = tk.Label(cab, text="", font=F_SMALL, bg=PANEL, fg=MUTED)
            cont.pack(side="right")
            # troca so' a fala desta cena, mantendo o resto do video
            tk.Button(cab, text="trocar", font=F_SMALL, bg=PANEL2, fg=ACCENT,
                      activebackground=LINE, activeforeground=ACCENT,
                      relief="flat", bd=0, cursor="hand2", padx=8, pady=0,
                      command=lambda k=i: self.trocar_fala(k)).pack(side="right", padx=(0, 9))
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

        # avisa que o TAKE sai com o termo hifenizado (o painel mostra a copy
        # limpa; o bloco entregue leva a reescrita fonetica)
        self.lbl_sonoro = tk.Label(cc, text="", font=F_SMALL, bg=PANEL, fg=MUTED,
                                   anchor="w", justify="left", wraplength=425)
        self.lbl_sonoro.pack(fill="x", padx=13, pady=(0, 12))

    # ---------------------------------------------------------------- direita
    def _coluna_dir(self, pai):
        col = tk.Frame(pai, bg=BG)
        col.pack(side="left", fill="both", expand=True, padx=(16, 0))

        self._passo(col, 3, "Copie para o AdBatch",
                    "clique no bloco, depois em COPIAR — ou copie os 5 de uma vez")

        barra = tk.Frame(col, bg=BG)
        barra.pack(fill="x", pady=(0, 8))
        # a contagem vem do motor, nao do texto: os agentes SHORT entregam 3
        # cenas e o rotulo fixo "os 5" mandaria o operador colar no AdBatch
        # errado — o de 5 slots descartaria nada, mas o inverso silencia dois
        n = len(self.m.CENAS_UI)
        self.b_img = self._btn(barra, "copiar os %d IMAGE" % n,
                               lambda: self.copiar_grupo("IMAGE"))
        self.b_img.pack(side="left")
        self.b_tak = self._btn(barra, "copiar os %d TAKE" % n,
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

    # ----------------------------------------------------------------- trava
    def alternar_cadeado(self, chave):
        var = self.var_cadeado[chave]
        var.set(not var.get())
        self._pintar_cadeado(chave)
        self._toast("%s %s" % (chave, "TRAVADO — não sai no sorteio"
                               if var.get() else "destravado"))

    def _pintar_cadeado(self, chave):
        on = self.var_cadeado[chave].get()
        self.b_cadeado[chave].configure(
            text="TRAVADO" if on else "trava",
            bg=ACCENT if on else PANEL2, fg="#ffffff" if on else MUTED,
            activebackground=ACCENT_D if on else LINE,
            activeforeground="#ffffff")

    def travas(self):
        """O que o sorteio NAO pode mexer, no formato que o motor espera.

        `None` quando o motor nao declara contrato nenhum — e' o sinal para
        chamar `sortear()` com tres argumentos, como os nove outros esperam.
        ⚠️ O cadeado devolve o VALOR QUE ESTA' NA TELA (`self.spec[chave]`), nao
        um id: quem remonta o video em volta dele e' o motor.
        """
        # ⚠️ `self.sexos` entra nesta conta desde 2026-08-06: sem ele o
        # ORGANICWAVE caía no ramo de tres argumentos e a trava de quem narra
        # nunca chegava ao motor — botao aceso, sorteio livre.
        if not (self.travas_ui or self.eixos_travaveis or self.pele_travavel
                or self.modos or self.sexos):
            return None
        t = {}
        for chave, var in self.var_trava.items():
            if var.get() != LIVRE:
                t[chave] = var.get()
        for chave, var in self.var_cadeado.items():
            if var.get() and self.spec and chave in self.spec:
                t[chave] = self.spec[chave]
        # ⚠️ a pele entra POR ULTIMO e nunca sobrescreve o cadeado de etnia:
        # etnia travada na tela e' mais especifica que clara/escura.
        if self.pele_travada and "etnia" not in t:
            t["pele"] = self.pele_travada
        # ⚠️ O sexo entra pela mesma porta da pele e pelo mesmo motivo: e' uma
        # trava GROSSA, e qualquer cadeado de tela e' mais especifico que ela.
        if self.sexo_travado and "sexo" not in t:
            t["sexo"] = self.sexo_travado
        # ⚠️ Os modos entram por ULTIMO e NAO sobrescrevem o cadeado de `ref`:
        # REF travada na tela e' mais especifica que "uma bela qualquer".
        # ⛔⛔ O CADEADO DE `ref` SO' DESLIGA OS MODOS DE PESSOA. `bela` e
        # `forte` trocam quem aparece, entao uma REF travada na tela e' mais
        # especifica que "uma bela qualquer" e vence. Um modo de CENA nao
        # disputa com o cadeado: travar o homem e perder a tigela na borda
        # seria o botao aceso com o video sem a receita — forma sem funcao,
        # e silenciosa.
        for _m, _on in self.modo_on.items():
            if _on and ("ref" not in t or _m in self.MODOS_DE_CENA):
                t[_m] = True
        return t

    # ------------------------------------------------------------------ acao
    def sortear(self):
        seed = self.var_seed.get().strip()
        self.rng = random.Random(int(seed)) if seed.isdigit() else random.Random()
        # ⭐ PELE TRAVADA NUM MOTOR DE ETNIA-POR-PAGINA: a trava e' aplicada
        # AQUI, sorteando dentro do grupo. Sem isto o botao segurava so' o
        # primeiro video e o SORTEAR seguinte trazia a outra pele de volta —
        # era o "botao que nao trava" de novo, so' que uma tela adiante.
        if self.pele_travada and not self.pele_travavel:
            grupo = self.grupos.get(self.pele_travada) or []
            if grupo and self.var_pag.get() not in grupo:
                self.var_pag.set(self.rng.choice(grupo))
        travas = self.travas()
        args = (self.var_pag.get(), self.rng, self.m._carregar_ledger())
        self.spec = (self.m.sortear(*args) if travas is None
                     else self.m.sortear(*args, travas))
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
        try:
            pool = self._pool(dict((e[0], e[2]) for e in self.m.EIXOS_UI)[chave])
        except AttributeError as e:
            # ⛔ Nunca falhar calado. Sob pythonw nao ha' stderr: a excecao
            # morria no callback do tkinter e o botao simplesmente nao fazia
            # nada. Foi assim que os seis eixos dos agentes SHORT ficaram
            # quebrados sem ninguem perceber (2026-07-31).
            self._toast("eixo %s: %s" % (chave, e))
            return
        # ⚠️ `!=` e nao `is not`: os pools novos do CLEAN V2 devolvem STRING
        # (etnia) e LISTA (o par do truque), montadas na hora — identidade nao
        # exclui o valor que ja' esta' na tela, e o botao `trocar` devolvia o
        # mesmo. Para os pools de DICT o resultado e' o mesmo de antes: as
        # entradas sao unicas, entao so' a atual sai da lista.
        # ⛔ POOL DE UM SO' VALOR: o `or pool` devolvia o MESMO valor e o botao
        # ficava mudo — "cliquei e nao acontece nada", que e' indistinguivel de
        # botao quebrado. Acontece de verdade: 4 dos 20 mundos do CLEAN V2 tem
        # uma etnia unica (`apalache` so' comporta `white American`), e ai' o
        # eixo nao TEM alternativa. Dizer isso e' honesto; ficar mudo nao e'.
        # ⚠️ So' a mensagem muda; o comportamento e' o mesmo de antes.
        opcoes = [x for x in pool if x != self.spec[chave]]
        if not opcoes:
            self._toast("%s: só existe esta opção aqui — troque outro eixo"
                        % chave)
            return
        self.spec[chave] = self.rng.choice(opcoes)
        reescreve = getattr(self.m, "EIXOS_QUE_MEXEM_NA_COPY", {}).get(chave)
        if reescreve:
            reescreve(self.spec, self.rng)
            self._preencher_copy()
        self._render()
        self._toast("%s re-sorteado" % chave)

    def _pool(self, nome):
        """Resolve o pool de um eixo pelo nome, no motor OU no base dele.

        ⚠️ Os agentes SHORT **derivam**: o EIXOS_UI deles vem do motor longo e
        cita pools que vivem la' ("OCASIOES", "PROPS", "REFS"), nao no modulo
        derivado. Sem este fallback TODO botao `trocar` de agente derivado
        estourava AttributeError — os seis eixos dos quatro SHORT, quebrados de
        uma vez. Relatado em producao, 2026-07-31.

        ⚠️ E o pool pode ser uma FUNCAO da pagina em vez de lista: quando a
        congruencia de etnia trava o elenco, o agente expoe `mulheres_de(pag)`.

        ⭐ 2026-08-03 — e ha' pool que depende do SPEC, nao da pagina: o `QUEM
        FALA` do CLEAN sai de `REFS_H` ou `REFS_M` conforme o sexo em cena, e
        nome de pool nenhum resolve isso (era o bug: o painel oferecia as
        MULHERES com um homem no video). A convencao e' ADITIVA — o callable
        marcado com `.recebe_spec = True` recebe o spec inteiro; sem a marca,
        continua recebendo a pagina, que e' o caso dos outros nove motores.
        """
        pool = getattr(self.m, nome, None)
        if pool is None:
            pool = getattr(getattr(self.m, "base", None), nome, None)
        if pool is None:
            raise AttributeError("pool '%s' nao existe nem no motor nem no base"
                                 % nome)
        if not callable(pool):
            return pool
        return pool(self.spec if getattr(pool, "recebe_spec", False)
                    else self.spec["pagina"])

    def pele_atual(self):
        return "clara" if "white" in self.m.ETNIA[self.var_pag.get()] else "escura"

    def _escolher_pagina(self):
        """⚠️ ESCOLHA EXPLICITA VENCE A TRAVA. Se a pele esta' travada em
        `escura` e o operador seleciona no combo uma pagina de pele clara, ele
        esta' dizendo o que quer — e o painel obedecendo a trava por cima disso
        seria o botao decidindo contra o clique. A trava cai e o botao apaga.
        ⛔ So' vale para motor de etnia-por-pagina: onde a etnia e' livre
        (PELE_TRAVAVEL) a pagina nao manda na etnia e nao ha' conflito."""
        if (self.pele_travada and not self.pele_travavel
                and self.var_pag.get() not in (self.grupos.get(self.pele_travada) or [])):
            self.pele_travada = None
            self._toast("pele destravada — você escolheu a página na mão")
        self.sortear()

    def trocar_pele(self, pele):
        """⭐⭐ O BOTAO DE PELE E' UMA TRAVA — EM TODOS OS AGENTES (2026-08-06).

        Antes ele fazia DUAS coisas diferentes conforme o motor, e o operador
        batia de frente com isso: nos que declaram `PELE_TRAVAVEL` era trava
        (clicou, fica), e nos outros era um pulo — trocava para uma pagina
        daquela pele UMA vez, e o proximo SORTEAR podia devolver a outra. Mesmo
        botao, duas promessas: o tipo de coisa que faz o operador parar de
        confiar no painel inteiro.

        Agora clicar SEMPRE trava, e clicar de novo na mesma pele destrava. O
        que muda por baixo e' so' QUEM filtra:

          · motor com PELE_TRAVAVEL  -> a trava vai em `travas["pele"]` e o
            motor remonta o video em volta dela (a etnia dele e' livre, nao
            vem da pagina);
          · motor sem a flag         -> a etnia vem de `ETNIA[pagina]`, entao
            quem filtra e' a PAGINA, a cada sorteio (ver `sortear`).
        """
        if self.pele_travada == pele:
            self.pele_travada = None
            self.sortear()
            self._toast("pele livre")
            return
        self.pele_travada = pele
        # motor de etnia-por-pagina: ja' pula para uma pagina da pele pedida,
        # senao o primeiro sorteio sairia com a pagina errada em cena.
        if not self.pele_travavel:
            grupo = self.grupos.get(pele) or []
            if not grupo:
                self.pele_travada = None
                self._toast("este agente nao tem pagina de pele %s" % pele)
                return
            if self.var_pag.get() not in grupo:
                self.var_pag.set(self.rng.choice(grupo))
        self.sortear()
        self._toast("pele travada: %s" % pele)
        self._toast("pele %s — página %s" % (pele, self.var_pag.get()))

    def trocar_sexo(self, sexo):
        """Trava QUEM NARRA em homem ou mulher. Clicar de novo destrava.

        ⛔ Mesmo contrato do botao de pele, de proposito: aceso = travado, e o
        segundo clique solta. Foi a licao de 2026-08-06 — o botao de pele fazia
        duas coisas diferentes em motores diferentes e o operador nunca sabia
        se estava travado ou so' sorteado.
        """
        if self.sexo_travado == sexo:
            self.sexo_travado = None
            self.sortear()
            self._toast("quem narra: livre")
            return
        self.sexo_travado = sexo
        self.sortear()
        self._toast("quem narra travado: %s" % sexo)

    def _pintar_sexo(self):
        for sexo, b in self.b_sexo.items():
            ativo = (sexo == self.sexo_travado)
            b.configure(bg=ACCENT if ativo else PANEL2,
                        fg="#ffffff" if ativo else MUTED,
                        activebackground=ACCENT_D if ativo else LINE,
                        activeforeground="#ffffff")

    # ⛔ Modos que mexem na CENA, nao na pessoa. Dois efeitos: o botao nao
    # diz `ref`, e o cadeado de REF NAO os desliga (ver `travas()`).
    MODOS_DE_CENA = ("receita",)

    ROTULO_MODO = {
        "bela": "super model, corpo escultural, pouca roupa",
        "forte": "homem forte e musculoso",
        # ⚠️ este descreve CENA, nao pessoa — e o rotulo diz isso, para o
        # operador nao esperar que ele troque alguem.
        "receita": "a receita na borda: tigela, caixa e ele mexendo",
    }

    def alternar_modo(self, chave):
        """Liga/desliga um modo de REF e refaz o video inteiro.

        ⛔ E' TRAVA, nao pre-selecao: enquanto ligado, TODO sorteio respeita.
        Um botao que so' valesse para o proximo sorteio seria o mesmo cadeado
        que nao trava — e o operador confia no que esta' aceso.
        """
        self.modo_on[chave] = not self.modo_on[chave]
        self._pintar_modos()
        self.sortear()
        self._toast("modo REF %s %s" % (
            chave.upper(),
            "LIGADO — " + self.ROTULO_MODO.get(chave, "")
            if self.modo_on[chave] else "desligado"))

    def _pintar_modos(self):
        for chave, b in self.b_modo.items():
            on = self.modo_on[chave]
            b.configure(bg=ACCENT if on else PANEL2,
                        fg="#ffffff" if on else MUTED,
                        activebackground=ACCENT_D if on else LINE,
                        activeforeground="#ffffff")

    def _pintar_pele(self):
        # ⚠️ Motor com PELE_TRAVAVEL: aceso = TRAVADO, apagado = livre. Acender
        # a pele da pagina aqui seria mentir — a pagina nao manda na etnia.
        atual = self.pele_travada if self.pele_travavel else self.pele_atual()
        for pele, b in self.b_pele.items():
            ativo = (pele == atual)
            b.configure(bg=ACCENT if ativo else PANEL2,
                        fg="#ffffff" if ativo else MUTED,
                        activebackground=ACCENT_D if ativo else LINE,
                        activeforeground="#ffffff")

    def trocar_fala(self, i):
        """Re-sorteia a copy de UMA cena. O motor devolve a linha nova ja'
        formatada com os slots daquele video (evento, eco, idade dela...)."""
        nova = getattr(self.m, "nova_fala", None)
        if not nova:
            self._toast("este agente ainda nao tem banco de copy por cena")
            return
        for _ in range(8):                      # evita devolver a mesma linha
            candidata = nova(self.spec, i, self.rng)
            if candidata != self.spec["falas"][i]:
                break
        self.spec["falas"][i] = candidata
        self.txt_fala[i].delete("1.0", "end")
        self.txt_fala[i].insert("1.0", candidata)
        self._marcar_limpo()
        self._render()
        self._toast("copy da cena %d re-sorteada" % (i + 1))

    def aplicar_copy(self):
        for i, t in enumerate(self.txt_fala):
            self.spec["falas"][i] = " ".join(t.get("1.0", "end").split())
        self._marcar_limpo()
        self._render()
        self._toast("copy aplicada")

    def marcar_usado(self):
        self.m._gravar_ledger(self.m._carregar_ledger(), self.spec)
        self._toast("registrado no ledger — não repete tão cedo")

    def _marcar_sujo(self):
        self.lbl_sujo.configure(text="copy editada — clique em aplicar")

    def _marcar_limpo(self):
        self.lbl_sujo.configure(text="")

    # --------------------------------------------------------------- render
    @staticmethod
    def _texto_eixo(v, campo):
        """O que o painel mostra na linha de um eixo.

        ⚠️ Ate' 2026-08-03 isto assumia DICT: `"selo" in v` num valor de texto
        e' teste de SUBSTRING, e `v.get(...)` numa string estoura
        AttributeError dentro do callback do tkinter — ou seja, o painel morria
        calado. O CLEAN V2 poe' no painel um eixo de STRING (a etnia) e um de
        LISTA (o par do truque), entao os tres casos ficam explicitos.
        Para DICT o comportamento e' o mesmo de sempre, caractere por caractere.
        """
        if isinstance(v, str):
            return v
        if isinstance(v, (list, tuple)):
            return " + ".join(str(x) for x in v)
        if isinstance(v, dict):
            if "selo" in v:
                return "%s   [%s]" % (v.get(campo, "?"), v["selo"])
            if "idade" in v:
                return "%dy · %s" % (v["idade"], v.get(campo, "?"))
            return v.get(campo, "?")
        return str(v)

    def _render(self):
        for chave, _r, _p, campo in self.m.EIXOS_UI:
            txt = self._texto_eixo(self.spec[chave], campo)
            # ⚠️ pool com placeholder: o ITEM_B do CLEAN carrega `{o}` e o
            # painel mostrava o template cru (`your {o} going` — print do
            # operador, 2026-08-05). Mostra-se o texto como o video FALA,
            # formatado com o orgao deste sorteio.
            # ⛔ OPT-IN por motor (ROTULO_FORMATA_O): ordem do operador de
            # 2026-08-05 — mexer SO' no V2. Motor sem a flag mostra o rotulo
            # exatamente como sempre mostrou, placeholder e tudo.
            if "{" in txt and getattr(self.m, "ROTULO_FORMATA_O", False):
                try:
                    txt = txt.format(o=self.spec["orgaos"][1])
                except (KeyError, IndexError):
                    pass
            self.lbl_eixo[chave].configure(text=txt)

        self.lbl_resumo.configure(text=self.m.resumo_pt(self.spec))
        self._pintar_pele()
        self._pintar_sexo()

        usados = sorted({t for f in self.spec["falas"] for t in termos_reescritos(f)})
        self.lbl_sonoro.configure(
            text=("no TAKE sai como:  " + " · ".join("%s → %s" % (t, ATIVA[t])
                                                     for t in usados)) if usados else "")

        self.blocos = self.m.montar(self.spec)
        self.achados = self.m.lint(self.spec, self.blocos)

        for i, t in enumerate(self.txt_fala):
            n = self.m._palavras(self.spec["falas"][i])
            teto = self.m.TETO_FALA[i + 1]
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
            self.lbl_lint.configure(text="   ·   ".join(a[1] for a in self.achados[:2]),
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

    def copiar_ref(self):
        """O BLOCO 0 (REF) — sem depender de qual item esta' selecionado.

        ⚠️ O `copiar_bloco` copia o bloco SELECIONADO na lista. Chamado por
        atalho, ele copiaria o que estivesse marcado — que no meio de um lote
        automatizado pode ser qualquer um. Aqui o alvo e' nomeado.
        """
        nome = next((k for k in self.blocos if k.startswith("BLOCO 0")), None)
        if nome is None:
            return self._toast("nao ha' BLOCO 0 (REF) neste roteiro")
        self._clip(self.blocos[nome])
        self._toast("%s copiado" % nome)

    def copiar_tudo(self):
        """⭐ O ROTEIRO INTEIRO — REF + IMAGEs + TAKEs, na ordem, de uma vez.

        E' o formato que a AdBatch Vertical espera na caixa "Cole o roteiro
        inteiro": ela le' o texto todo e conta os REF/IMAGE/TAKE de dentro.
        ⛔ A ORDEM E' FIXA e nao e' a alfabetica: o REF vem primeiro porque a
        ferramenta usa a referencia para as imagens seguintes.
        """
        ref = [k for k in self.blocos if k.startswith("BLOCO 0")]
        img = sorted(k for k in self.blocos if k.startswith("IMAGE"))
        tak = sorted(k for k in self.blocos if k.startswith("TAKE"))
        ordem = ref + img + tak
        if not ordem:
            return self._toast("nao ha' blocos para copiar")
        self._clip("\n\n".join(self.blocos[n] for n in ordem))
        self._toast("roteiro inteiro copiado — %d blocos (%d REF, %d IMAGE, "
                    "%d TAKE)" % (len(ordem), len(ref), len(img), len(tak)))

    def copiar_grupo(self, prefixo):
        nomes = sorted(k for k in self.blocos if k.startswith(prefixo))
        self._clip("\n\n".join(self.blocos[n] for n in nomes))
        self._piscar(self.b_img if prefixo == "IMAGE" else self.b_tak)
        self._toast("%d blocos %s copiados" % (len(nomes), prefixo))

    def salvar(self):
        cam = filedialog.asksaveasfilename(
            defaultextension=".txt", filetypes=[("Texto", "*.txt")],
            initialfile="%s_%s.txt" % (getattr(self.m, "SLUG", "agente"),
                                       self.spec["pagina"]))
        if not cam:
            return
        with open(cam, "w", encoding="utf-8") as f:
            for nome in self._ordem():
                f.write(nome + "\n" + self.blocos[nome] + "\n\n")
        self._toast("salvo em %s" % os.path.basename(cam))

    def _toast(self, msg):
        self.lbl_toast.configure(text=msg)
        self.after(2600, lambda: self.lbl_toast.configure(text=""))
