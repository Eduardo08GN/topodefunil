# -*- coding: utf-8 -*-
"""GERADOR DE FOTOS VIA GOOGLE FLOW (Nano Banana Pro), por CDP.

⭐ O QUE ESTA FERRAMENTA MUDA. O PLAYBOOK-EBOOK dizia: *"Eu escrevo o PROMPT, o
operador GERA, eu distribuo"* — porque o agente nao tinha gerador. Com o
browser-harness attachado ao Chrome logado do operador, ele tem. O passo manual
sai do meio, e o prompt continua sendo escrito aqui.

⛔ UMA FERRAMENTA POR FUNCAO: esta gera foto para QUALQUER ebook, nao so' para o
alemao. Por isso ela nao sabe nada sobre respiracao — recebe um JSON
`{slug: prompt}` e uma pasta de saida, e so'.

USO (tem de rodar DENTRO do harness, que pre-importa os helpers):

    BH_PROMPTS=atem/prompts.json BH_OUT=atem/fotos browser-harness < gerar_fotos_flow.py

⭐ IDEMPOTENTE POR CONSTRUCAO: slug que ja' tem arquivo na pasta de saida e'
pulado. Credito do Flow e' finito e rodar de novo nao pode custar de novo.

⚠️ O compositor do Flow e' um ProseMirror. Valor setado por JS NAO persiste —
tem de ser digitacao real (`type_text`), a mesma licao ja' paga nos formularios
da Hotmart.
"""

import base64
import json
import os
import time

OUT = os.environ.get("BH_OUT", "fotos")
PROMPTS = os.environ.get("BH_PROMPTS", "prompts.json")
ESPERA_MAX = int(os.environ.get("BH_ESPERA", "240"))

# ⛔ Cauda travada em TODO prompt. `no text` porque texto gerado por modelo sai
# com erro de ortografia — e em alemao, com trema errado. Quem escreve texto na
# pagina e' o motor do PDF, nunca o gerador de imagem.
CAUDA = ", ultra realistic photo, natural light, muted colours, no text, no writing, no watermark, 1:1 square"


def _ids_na_pagina():
    """Ids das imagens ja' renderizadas. O id vem da URL assinada do CDN."""
    return set(json.loads(js("""
    (() => JSON.stringify([...document.querySelectorAll('img')]
      .filter(i=>i.naturalWidth>200)
      .map(i=>(i.src.match(/\\/image\\/([0-9a-f-]{36})/)||[])[1])
      .filter(Boolean)))()
    """)))


def _url_de(iid):
    return js("""
    (() => {const i=[...document.querySelectorAll('img')]
      .find(x=>x.src.indexOf(%r)>=0); return i?i.src:'';})()
    """ % iid)


def _baixar(url, destino):
    b64 = js("""
    (async () => {
      const r = await fetch(%r);
      if(!r.ok) return '';
      const b = await r.arrayBuffer(); const v = new Uint8Array(b);
      let s=''; const CH=0x8000;
      for(let i=0;i<v.length;i+=CH){ s+=String.fromCharCode.apply(null, v.subarray(i,i+CH)); }
      return btoa(s);
    })()
    """ % url)
    if not b64:
        return 0
    raw = base64.b64decode(b64)
    with open(destino, "wb") as f:
        f.write(raw)
    return len(raw)


def _limpar_compositor():
    el = js("""
    (() => {const p=document.querySelector('.ProseMirror');
      if(!p) return 'sem compositor';
      p.focus(); return 'ok';})()
    """)
    if el != "ok":
        raise RuntimeError(el)
    # ⚠️ Ctrl+A dentro do ProseMirror, nunca `textContent=''`.
    press_key("Control+a")
    press_key("Delete")


def _enviar():
    """Clique no DOM, nao por coordenada: o compositor cresce com o texto e
    empurra o botao para baixo — coordenada fixa clica no lugar errado."""
    return js("""
    (() => {
      const b=[...document.querySelectorAll('button')]
        .filter(x=>(x.innerText||'').trim()==='arrow_forward');
      if(!b.length) return 'sem botao';
      const alvo=b[b.length-1];
      if(alvo.disabled) return 'desabilitado';
      alvo.click(); return 'ok';
    })()
    """)


def gerar(slug, prompt):
    destino = os.path.join(OUT, slug + ".jpg")
    if os.path.exists(destino):
        print("  = %-16s ja existe, pulado" % slug)
        return True

    antes = _ids_na_pagina()
    _limpar_compositor()
    type_text(prompt + CAUDA)
    time.sleep(0.6)
    r = _enviar()
    if r != "ok":
        print("  ! %-16s nao enviou (%s)" % (slug, r))
        return False

    esperou = 0
    while esperou < ESPERA_MAX:
        time.sleep(6)
        esperou += 6
        novos = _ids_na_pagina() - antes
        if novos:
            iid = sorted(novos)[0]
            url = _url_de(iid)
            if not url:
                continue
            n = _baixar(url, destino)
            if n > 20000:
                print("  + %-16s %d KB  (%ds)" % (slug, n // 1024, esperou))
                return True
            print("  ! %-16s download vazio" % slug)
            return False
    print("  ! %-16s TIMEOUT apos %ds" % (slug, ESPERA_MAX))
    return False


def main():
    with open(PROMPTS, encoding="utf-8") as f:
        pedidos = json.load(f)
    os.makedirs(OUT, exist_ok=True)
    print("Flow -> %s  (%d prompts)" % (OUT, len(pedidos)))
    falhas = []
    for slug, prompt in pedidos.items():
        if not gerar(slug, prompt):
            falhas.append(slug)
    print("\nFEITO. %d/%d" % (len(pedidos) - len(falhas), len(pedidos)))
    if falhas:
        print("FALTAM:", " ".join(falhas))


main()
