# -*- coding: utf-8 -*-
"""FRENTE DO LIVRO — "Comece Por Aqui" (Passo 1).
Boas-vindas, como o material funciona, avisos honestos, dica do YouTube,
anotar/imprimir, nota de calorias/porções e o PLANO ALIMENTAR DE 30 DIAS.
Gera: "Passo 1 - Comece Por Aqui.pdf".
"""
import os
import time
import http.server
import socketserver
import threading
import importlib
import html as _html
import subprocess

import motor_receitas as motor
import receitas_cafe as R_cafe
import receitas_almoco as R_almoco
import receitas_jantar as R_jantar
import receitas_sobremesa as R_sobremesa
import receitas_suco as R_suco

PORTA = 8132
AQUI = os.path.dirname(os.path.abspath(__file__))


def _nome(mod, i):
    return mod.RECEITAS[i]["nome"]


def _curto(nome, n=26):
    if len(nome) <= n:
        return nome
    corte = nome[:n].rsplit(" ", 1)[0]
    return corte + "…"


EXTRA_CSS = """
.cover{page-break-after:always;padding-top:30px}
.badge{display:inline-block;background:var(--green);color:#fff;font-size:16px;font-weight:900;
letter-spacing:.14em;text-transform:uppercase;padding:9px 20px;border-radius:999px}
.cover h1{font-size:62px;font-weight:900;letter-spacing:-.03em;margin:18px 0 18px;line-height:1.0;color:var(--green)}
.cover .rule{width:70px;height:5px;background:var(--gold);border-radius:3px;margin:0 0 22px}
.cover .lead{font-size:18.5px;color:var(--soft);line-height:1.7;max-width:97%}
.sec{page-break-before:always;padding-top:6px}
.sec h2{font-size:32px;font-weight:900;letter-spacing:-.01em;color:var(--green);margin-bottom:8px;line-height:1.1}
.sec .sub{font-size:17px;color:var(--soft);line-height:1.6;margin-bottom:18px;max-width:97%}
.sec p{font-size:17.5px;line-height:1.7;margin-bottom:13px}
.sec p b{color:var(--ink)}
.stepbox{display:grid;grid-template-columns:44px 1fr;gap:12px;padding:13px 0;border-bottom:1px solid var(--line);break-inside:avoid;align-items:start}
.stepbox .sn{width:36px;height:36px;background:var(--green);color:#fff;border-radius:50%;
display:flex;align-items:center;justify-content:center;font-size:16px;font-weight:800}
.stepbox p{font-size:17px;line-height:1.55;margin:0}
.stepbox p b{color:var(--ink);font-weight:800}
.warn{background:var(--gold-tint);border-left:4px solid var(--gold);border-radius:0 12px 12px 0;
padding:18px 22px;margin-bottom:16px;break-inside:avoid}
.warn b{color:#8a6a1a;font-size:14px;text-transform:uppercase;letter-spacing:.05em;display:block;margin-bottom:6px}
.warn p{font-size:17px;line-height:1.6;margin:0}
.tipbox{background:var(--green-tint);border-radius:14px;padding:20px 24px;margin-bottom:16px;break-inside:avoid}
.tipbox h3{font-size:16.5px;color:var(--green);text-transform:uppercase;letter-spacing:.05em;margin-bottom:9px}
.tipbox p{font-size:17px;line-height:1.6;margin:0}
.plan-note{font-size:16px;color:var(--soft);line-height:1.6;margin-bottom:20px}
.dcard{padding:15px 0 13px;border-top:1.5px solid var(--line);break-inside:avoid;page-break-inside:avoid}
.dcard h3{font-size:21px;font-weight:900;color:var(--green);margin-bottom:11px}
.drow{display:grid;grid-template-columns:160px 1fr;gap:10px;padding:5px 0;align-items:baseline}
.drow .lbl{color:var(--soft);font-weight:800;font-size:13.5px;text-transform:uppercase;letter-spacing:.04em}
.drow .val{font-size:16.5px;line-height:1.45;color:var(--ink)}
.drow .val .n{color:var(--green);font-weight:800;margin-right:6px}
"""


def cover():
    return """
<div class="cover">
  <span class="badge">Comece Por Aqui</span>
  <h1>Boas-vindas!</h1>
  <div class="rule"></div>
  <p class="lead">Que bom ter você aqui. Você acaba de dar o primeiro passo para
    emagrecer comendo bem, sem passar fome e sem dietas malucas. Este material é um
    <b>protocolo completo</b>: 150 receitas fit, um plano de 30 dias e três bônus de
    exercícios e hábitos. Antes de começar a cozinhar, leia estas primeiras páginas
    com carinho — elas vão te poupar tempo e evitar frustração. Vamos juntos!</p>
</div>
"""


def como_funciona():
    passos = [
     ("Comece Por Aqui", "Este arquivo. As instruções, os avisos e o plano de 30 dias."),
     ("Cafés da Manhã", "30 receitas para começar o dia com energia e saciedade."),
     ("Almoços", "35 pratos completos e leves para o meio do dia."),
     ("Jantares", "35 opções mais leves para a noite."),
     ("Sobremesas", "20 doces fit e sem açúcar para matar a vontade sem culpa."),
     ("Vitaminas, Sucos e Chás Detox", "30 bebidas para hidratar, desinchar e acelerar."),
     ("Bônus 1 — Dieta Vegetariana", "20 opções sem carne, bem distribuídas."),
     ("Bônus 2 — Pilates Seca Barriga em Casa", "12 exercícios de abdômen, sem aparelho."),
     ("Bônus 3 — 50 Hábitos e Exercícios", "Os exercícios e hábitos que aceleram o resultado."),
    ]
    linhas = ""
    for i, (t, d) in enumerate(passos, 1):
        linhas += ('<div class="stepbox"><div class="sn">%d</div>'
                   '<p><b>Passo %d — %s.</b> %s</p></div>' % (i, i, _html.escape(t), _html.escape(d)))
    return """<div class="sec">
  <h2>Como este material funciona</h2>
  <p class="sub">Para ficar organizado, o material vem em arquivos separados, numerados
    como <b>passos</b>. Siga a ordem — cada passo é uma parte do seu dia.</p>
  %s
  <p style="margin-top:16px">Dentro de cada arquivo, as receitas têm um <b>número</b>
    (por exemplo, <b>Receita 003</b>). É por esse número que o plano de 30 dias, mais
    à frente, indica o que comer em cada dia.</p>
</div>""" % linhas


def avisos():
    itens = [
     ("A dieta não faz milagre", "Não existe fórmula mágica. O que existe é consistência. Seguir o cardápio durante a semana e exagerar em doces e frituras no fim de semana anula todo o esforço. O resultado vem de quem mantém o hábito na maior parte do tempo."),
     ("O resultado leva alguns meses", "Você não vai mudar da noite para o dia — e ainda bem, porque o que vem rápido também vai embora rápido. Dê ao seu corpo alguns meses de constância e a mudança será sólida e duradoura."),
     ("Exercício faz parte", "A alimentação é a maior parte, mas o corpo se transforma de verdade quando você também se movimenta. Os Bônus 2 e 3 trazem exercícios para todos os níveis, de dentro e de fora de casa. Use-os."),
     ("Sem promessas falsas", "A gente não promete que você vai perder 10 quilos em uma semana, porque isso seria mentira. A gente entrega um protocolo completo e honesto que, seguido com constância, pode trazer resultados reais e duradouros."),
    ]
    blocos = ""
    for t, d in itens:
        blocos += ('<div class="warn"><b>%s</b><p>%s</p></div>'
                   % (_html.escape(t), _html.escape(d)))
    return """<div class="sec">
  <h2>A verdade, com honestidade</h2>
  <p class="sub">Antes de qualquer receita, quatro verdades que ninguém costuma te contar —
    e que fazem toda a diferença para você ter sucesso.</p>
  %s
</div>""" % blocos


def dicas():
    return """<div class="sec">
  <h2>Dicas para aproveitar melhor</h2>
  <p class="sub">Pequenos truques que deixam a sua jornada mais fácil.</p>

  <div class="tipbox">
    <h3>Ficou em dúvida numa receita? Use o YouTube</h3>
    <p>Se você não souber como fazer algum passo, é só pesquisar no YouTube o
      <b>nome da receita + "modo de preparo"</b> que vão aparecer vídeos ensinando
      passo a passo. É uma mão na roda, principalmente no começo.</p>
  </div>

  <div class="tipbox">
    <h3>Anote e imprima o que for usar</h3>
    <p>Marque as receitas que você mais gostou e faça <b>anotações</b> do que vai
      comprar e preparar na semana. Se preferir, <b>imprima</b> as páginas das
      comidas, dos hábitos e dos exercícios de interesse e deixe à vista, na cozinha
      ou na geladeira. O que está à mão a gente cumpre.</p>
  </div>

  <div class="tipbox">
    <h3>Sobre as calorias e as porções</h3>
    <p>As calorias de cada receita são <b>valores aproximados</b>, calculados por
      tabelas nutricionais padrão — servem como guia, não como medida exata de
      laboratório. Cada receita traz uma <b>tabela de ajuste por sexo e peso</b>:
      encontre a sua linha e siga aquelas quantidades. Vegetais, verduras, café e chá
      sem açúcar são livres, à vontade — não precisa contar.</p>
  </div>
</div>"""


ROT = {"cafe": ("Café", R_cafe, 0), "almoco": ("Almoço", R_almoco, 30),
       "jantar": ("Jantar", R_jantar, 65), "sobremesa": ("Sobremesa", R_sobremesa, 100),
       "suco": ("Suco", R_suco, 120)}


def _row(lbl, num, mod, idx):
    return ('<div class="drow"><span class="lbl">%s</span>'
            '<span class="val"><span class="n">%03d</span>%s</span></div>'
            % (lbl, num, _html.escape(_nome(mod, idx))))


def plano_30():
    dias = ""
    for dia in range(1, 31):
        s = ((dia - 1) % 20) + 1   # sobremesa 101..120, repete após 20
        dias += ("""<div class="dcard"><h3>Dia %d</h3>
  %s%s%s%s%s</div>""" % (
            dia,
            _row("Café da manhã", dia, R_cafe, dia - 1),
            _row("Almoço", 30 + dia, R_almoco, dia - 1),
            _row("Jantar", 65 + dia, R_jantar, dia - 1),
            _row("Sobremesa", 100 + s, R_sobremesa, s - 1),
            _row("Suco", 120 + dia, R_suco, dia - 1)))
    return """<div class="sec">
  <h2>Plano Alimentar de 30 Dias</h2>
  <p class="sub">Um mês inteiro montado para você — é só seguir. Cada dia traz um café,
    um almoço, um jantar, uma sobremesa e um suco diferentes, sem repetir os pratos ao
    longo do mês.</p>
  <p class="plan-note">O número antes de cada receita indica onde encontrá-la no arquivo
    da categoria (por exemplo, a <b>Receita 031</b> está no arquivo <b>Almoços</b>). As
    sobremesas, por serem 20, recomeçam a partir do dia 21. Sinta-se livre para trocar
    qualquer prato por outro da mesma categoria que você prefira.</p>
  %s
</div>""" % dias


def build():
    for m in (R_cafe, R_almoco, R_jantar, R_sobremesa, R_suco):
        importlib.reload(m)
    corpo = cover() + como_funciona() + avisos() + dicas() + plano_30()
    doc = ("""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">
<title>Comece Por Aqui</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700;800;900&display=swap" rel="stylesheet">
<style>%s
%s</style></head><body>%s</body></html>""" % (motor.ESTILO, EXTRA_CSS, corpo))

    html_path = os.path.join(AQUI, "_tmp_frente.html")
    pdf_path = os.path.join(AQUI, "Passo 1 - Comece Por Aqui.pdf")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(doc)

    def _srv():
        os.chdir(AQUI)
        with socketserver.TCPServer(("127.0.0.1", PORTA),
                                    http.server.SimpleHTTPRequestHandler) as s:
            s.serve_forever()
    threading.Thread(target=_srv, daemon=True).start()
    time.sleep(1.2)
    subprocess.run([motor.CHROME, "--headless=new", "--disable-gpu",
                    "--no-pdf-header-footer", "--virtual-time-budget=20000",
                    "--print-to-pdf=" + pdf_path,
                    "http://127.0.0.1:%d/%s" % (PORTA, "_tmp_frente.html")],
                   capture_output=True)
    ok = os.path.exists(pdf_path)
    print("PDF:", pdf_path, "OK" if ok else "FALHOU",
          "(%.1f MB)" % (os.path.getsize(pdf_path) / 1e6) if ok else "")
    if ok and os.path.exists(html_path):
        os.remove(html_path)
    return ok


if __name__ == "__main__":
    build()
