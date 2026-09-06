# -*- coding: utf-8 -*-
"""HELPERS DO HARNESS PARA A HOTMART.

Carregue dentro de um script do browser-harness:

    import io
    exec(io.open("landing-atem/hotmart_helpers.py", encoding="utf-8").read())

⭐ Nasceu do cadastro dos produtos `Der Atemanker` (8464658) e `L'Ancre du
Souffle` (8465131). Cada funcao aqui existe por causa de um defeito medido, e
os comentarios sao o registro deles.
"""

# ⛔ Ha VARIAS abas de app.hotmart.com abertas. Pegar "a primeira que casa" leva
# para o produto errado sem avisar — aconteceu: eu li o conteudo do produto de
# receitas frances achando que era o Atemanker. Ancorar e' NAVEGAR e CONFERIR.

def hm(url=None, espera=9):
    import time
    tabs = [x for x in list_tabs() if "app.hotmart.com" in x.get("url", "")]
    if not tabs:
        raise RuntimeError("nenhuma aba da Hotmart aberta")
    switch_tab(tabs[0]["target_id"])
    if url:
        goto_url(url)
        time.sleep(espera)
        atual = page_info()["url"]
        alvo = url.split("?")[0].rstrip("/")
        if not atual.startswith(alvo):
            raise RuntimeError("nao chegou em %s (esta em %s)" % (alvo, atual))
        return atual
    return page_info()["url"]


def escolher(cid, val, espera=1.4):
    """Seleciona uma opcao num <hot-select>. Clique REAL para abrir, depois
    scrollIntoView e clique REAL na opcao — o componente ignora .click() no
    <hot-select-option> fechado e ignora tambem value setado por JS.
    ⚠️ A lista pode abrir PARA CIMA: a posicao vem do rect vivo."""
    import json, time
    r = json.loads(js("""
    (() => {const s=document.querySelector('hot-select#%s'); const b=s.getBoundingClientRect();
     return JSON.stringify([Math.round(b.x+b.width/2), Math.round(b.y+b.height/2)]);})()
    """ % cid))
    click_at_xy(r[0], r[1]); time.sleep(espera)
    o = json.loads(js("""
    (() => {const e=[...document.querySelectorAll('hot-select#%s hot-select-option')]
      .find(x=>x.getAttribute('value')===%r);
     if(!e) return 'null';
     e.scrollIntoView({block:'center'});
     const b=e.getBoundingClientRect();
     return JSON.stringify([Math.round(b.x+b.width/2), Math.round(b.y+b.height/2)]);})()
    """ % (cid, val)))
    if o is None:
        raise RuntimeError("opcao %s nao existe em %s" % (val, cid))
    time.sleep(0.5); click_at_xy(o[0], o[1]); time.sleep(espera)
    got = js("document.querySelector('hot-select#%s').getAttribute('value')" % cid)
    print("  %-14s -> %-18s %s" % (cid, got, "OK" if got == val else "FALHOU"))
    return got == val


def marcar(cid, alvo):
    """Liga/desliga um checkbox e PROVA o estado depois.

    ⛔ O input tem tamanho zero; quem responde e' o <label for=...>.
    ⛔⛔ E o clique por COORDENADA nao funciona na tela de checkout: o ponto
    resolve para o elemento certo no `elementFromPoint` e mesmo assim o foco
    fica no BODY. Clique de DOM no label resolve — e o mesmo vale para os
    campos de texto de la', que so' aceitaram `focus()` por JS.
    """
    import time
    est = js("(()=>{const e=document.querySelector('#%s'); return e? e.checked : null;})()" % cid)
    if est is None:
        print("  %-38s AUSENTE" % cid)
        return False
    if est == alvo:
        print("  %-38s ja estava %s" % (cid, "ON" if alvo else "OFF"))
        return True
    js("""
    (() => {let l=document.querySelector('label[for="%s"]');
     if(!l){const e=document.querySelector('#%s'); l=e.closest('label')||e.parentElement;}
     l.click(); return 1;})()
    """ % (cid, cid))
    time.sleep(1.0)
    novo_est = js("document.querySelector('#%s').checked" % cid)
    ok = (novo_est == alvo)
    print("  %-38s %s -> %s  %s" % (cid, "ON" if est else "OFF",
          "ON" if novo_est else "OFF", "OK" if ok else "FALHOU"))
    return ok
