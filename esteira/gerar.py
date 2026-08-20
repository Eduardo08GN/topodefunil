# -*- coding: utf-8 -*-
"""ESTEIRA · ETAPA 3 — o mapa vira PROMPT. ZERO TOKEN.

    python esteira/gerar.py <slug> [--takes 2|3|fonte] [--fiel|--nosso]

⛔⛔ O PROMPT NAO E' ESCRITO POR MODELO NENHUM, e essa e' a decisao central da
esteira. O modelo (etapa 2) devolve o que VE'; a montagem e' codigo. Se o
prompt final viesse do chat, cada video custaria 4-5x mais tokens e traria de
volta, um por um, os defeitos que este repo pagou em campo:

  · `with the phone in his free hand` -> o gerador DESENHA o telefone
  · `not a celebrity` -> negacao INJETA o token que se queria evitar
  · bloco de 4.500 caracteres -> a AdBatch corta em 4.000 EM SILENCIO, e o
    que ela corta e' o FIM, onde moram camera, luz e cauda
  · fala de 30 palavras num take de 8s -> corta, e o que corta e' o CTA

Cada um desses vira uma linha de codigo aqui, e codigo nao regride.

⚠️ O QUE ESTA ETAPA NAO FAZ: julgar. Ela nao decide se a copy da fonte serve ao
nosso funil — isso e' alcada do operador e esta' no par `--fiel` / `--nosso`.
"""
import argparse
import io
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
SAIDA = os.path.join(AQUI, "saida")

# ⛔ O teto de caractere e' o da ferramenta, nao gosto meu: o codigo da AdBatch
# faz `block.content.slice(0, 4000)` sem avisar. 3.900 deixa margem.
TETO_BLOCO = 3900
# ⛔ O teto de fala e' RELOGIO x RITMO, os dois medidos: o player marca 8s por
# take e a fala normal corre a 3,1 palavras/s.
SEG_TAKE, TAXA = 8.0, 3.1
TETO_FALA = int(SEG_TAKE * TAXA)

CAUDA = ("Everyday amateur snapshot look, slight natural sway, soft sensor "
         "grain. No on-screen text, no subtitles, no captions, no watermark.")

# ⛔ APARELHO SEGURADO e NEGACAO — os dois recortes que o repo ja' pagou.
# ⚠️ `iPhone` solto NAO entra aqui: ele vive na cauda estetica de 46 motores e
# esta' certo la'. O que quebra e' o aparelho na MAO do personagem.
RX_APARELHO = re.compile(
    r"\b(phone|iphone|camera|camcorder|tripod|gimbal)\b[^.]{0,60}?"
    r"\b(in (his|her|their) (free )?hand|held|holding|hand-held)\b|"
    r"\b(holding|held|with) (a |the )?(phone|iphone|camera)\b", re.I)
RX_NEGACAO = re.compile(
    r"\bnot a (celebrity|model|actor|famous)\b|\bno phone in frame\b|"
    r"\bnot famous\b|\bnot celebrities\b", re.I)

BANIDOS_CTA = {"book", "yes"}
KEYWORD = "gelatin"


def _palavras(s):
    return len([p for p in re.split(r"\s+", s.strip()) if p])


def limpar(txt):
    """Tira do texto do modelo o que o gerador de imagem nao pode receber."""
    achados = []
    if RX_APARELHO.search(txt):
        achados.append("aparelho SEGURADO")
        txt = RX_APARELHO.sub("", txt)
    if RX_NEGACAO.search(txt):
        achados.append("negacao")
        txt = RX_NEGACAO.sub("", txt)
    txt = re.sub(r"\s{2,}", " ", txt)
    txt = re.sub(r"\s+([.,])", r"\1", txt)
    txt = re.sub(r"([.,])\1+", r"\1", txt)
    return txt.strip(), achados


def trocar_keyword(fala):
    """O CTA da fonte vira o NOSSO CTA.

    ⛔ `book` e `yes` sao as duas palavras que a fonte mais pede e as duas que
    quebram a automacao de DM: o comentario entra e a mensagem nao sai. A troca
    e' obrigatoria e e' aqui, nao no olho do operador.
    """
    def _sub(m):
        return "%s %s" % (m.group(1), KEYWORD)
    return re.sub(r"\b(comment|write|type)\s+[\"“]?(%s)\b[\"”]?"
                  % "|".join(BANIDOS_CTA), _sub, fala, flags=re.I)


def montar(mapa, dossie, modo, alvo_takes):
    tks = mapa["takes"]
    falas = [t.get("fala", "") for t in dossie["takes"]]

    # ⛔ Colapso: a fonte pode ter 5 planos e o nosso formato aceita 2 ou 3. Os
    # takes extras sao FUNDIDOS no ultimo, nunca descartados — descartar
    # perderia o payoff, que na fonte mora quase sempre no fim.
    if alvo_takes != "fonte":
        n = int(alvo_takes)
        if len(tks) > n:
            # ⛔⛔ ISTO AQUI FUNDIA NO PAPEL E DESCARTAVA NA PRATICA.
            # Era `tks[:n-1] + [tks[n-1]]`, que e' IDENTICO a `tks[:n]`:
            # o ultimo take da FONTE — onde mora o payoff — simplesmente
            # sumia, enquanto a FALA dele era empilhada num quadro que nao
            # mostra nada do que ela promete. Medido no v01 com --takes 2:
            # sete props do take 3 perdidos e a fala indo de 25 para 43
            # palavras. O comentario dizia o contrario do codigo.
            # ⭐ Agora funde de verdade: o quadro final e' o ULTIMO da
            # fonte (o payoff), e os props do meio sao herdados sem
            # repetir.
            cauda = tks[n - 1:]
            ult = dict(cauda[-1])
            props = []
            for t in cauda:
                for p in (t.get("props") or []):
                    if p not in props:
                        props.append(p)
            ult["props"] = props
            tks = tks[:n - 1] + [ult]
            falas = falas[:n - 1] + [
                " ".join(x for x in falas[n - 1:] if x).strip()]

    blocos, avisos = {}, []
    n = len(tks)

    p0 = tks[0].get("pessoa", "") or ""
    if p0 and p0.lower() != "none":
        ref, ach = limpar(p0)
        avisos += ["BLOCO 0: " + a for a in ach]
        blocos["BLOCO 0 (REF)"] = (
            "REF 01: Photo of a real person, %s, chest up, facing forward, "
            "calm steady expression. Plain neutral gray background, soft even "
            "frontal light. Slight sensor grain, raw amateur photo look. "
            "No subtitles, no captions, no burned-in text, no watermark." % ref)

    for i, t in enumerate(tks, 1):
        props = ", ".join(t.get("props") or [])
        partes = [t.get("ambiente", "")]
        if t.get("superficie") and t["superficie"].lower() != "none":
            partes.append("On %s" % t["superficie"])
        if props:
            partes.append("In frame: %s" % props)
        if t.get("pessoa") and t["pessoa"].lower() != "none":
            partes.append("In frame is %s" % t["pessoa"])
        if t.get("traje") and t["traje"].lower() not in ("none", "none visible"):
            partes.append("Wearing %s" % t["traje"])
        if t.get("gesto"):
            partes.append(t["gesto"])
        # ⛔⛔ A CAMERA E O AUDIO SAO LIMPOS ANTES, e nao so' dentro do
        # bloco IMAGE. O `limpar()` rodava so' na IMAGE e no REF, entao
        # `phone in his free hand` vindo no campo `camera` chegava INTACTO
        # ao bloco TAKE — que e' justamente o prompt que ANIMA a imagem —
        # e o aviso dizia "IMAGE 01: aparelho SEGURADO", passando ao
        # operador a impressao de que estava resolvido. E' o defeito que
        # este modulo existe para impedir, escapando pela porta de tras.
        cam, ach_c = limpar(t.get("camera", "") or "")
        aud, ach_a = limpar(t.get("audio", "") or "")
        avisos += ["TAKE %02d (camera): %s" % (i, a) for a in ach_c]
        avisos += ["TAKE %02d (audio): %s" % (i, a) for a in ach_a]
        partes += [cam, t.get("luz", ""), CAUDA]
        txt, ach = limpar(". ".join(x.strip(" .") for x in partes if x) + ".")
        avisos += ["IMAGE %02d: %s" % (i, a) for a in ach]

        chave = "IMAGE %02d/%02d" % (i, n)
        if len(txt) > TETO_BLOCO:
            avisos.append("IMAGE %02d com %d chars — a AdBatch corta em 4000"
                          % (i, len(txt)))
        blocos[chave] = "%s: %s" % (chave, txt)

        fala = (falas[i - 1] or "").strip()
        if modo == "nosso":
            fala = trocar_keyword(fala)
        if fala and _palavras(fala) > TETO_FALA:
            avisos.append("TAKE %02d com %d palavras (teto %d em %.0fs) — "
                          "a fala CORTA" % (i, _palavras(fala), TETO_FALA,
                                            SEG_TAKE))
        ktake = "TAKE %02d/%02d" % (i, n)
        corpo = ("TAKE %02d/%02d: Animate the provided image exactly. %s and "
                 "there are no cuts. Audio: %s."
                 % (i, n, cam or "The camera holds still",
                    aud or "quiet room tone, no music"))
        if fala:
            corpo += '\nDialogue: "%s"' % fala
        blocos[ktake] = corpo

    return blocos, avisos


def main():
    ap = argparse.ArgumentParser(description="Etapa 3 — o mapa vira prompt")
    ap.add_argument("slug")
    ap.add_argument("--takes", default="fonte",
                    help="2, 3 ou 'fonte' (respeita os cortes detectados)")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--fiel", action="store_const", dest="modo", const="fiel")
    g.add_argument("--nosso", action="store_const", dest="modo", const="nosso")
    ap.set_defaults(modo="nosso")
    a = ap.parse_args()

    d = os.path.join(SAIDA, a.slug)
    fm, fd = os.path.join(d, "mapa.json"), os.path.join(d, "dossie.json")
    if not os.path.exists(fm):
        raise SystemExit("falta o mapa.json em %s\n"
                         "Cole o PEDIDO.md + folha.jpg no chat e salve a "
                         "resposta ali." % d)
    # ⛔ Mapa mais VELHO que o dossie e' mapa de outra leitura. Com o slug
    # antigo isso virava prompt Frankenstein; com o slug novo so' acontece
    # se o operador reler o mesmo video com outro limiar — e ai' o numero
    # de takes pode ate' bater por acaso. A data nao mente.
    if os.path.getmtime(fm) < os.path.getmtime(fd):
        raise SystemExit("o mapa.json e' de uma leitura ANTERIOR a este "
                         "dossie. Refaca a etapa 2 com a folha nova.")
    mapa = json.load(io.open(fm, encoding="utf-8"))
    dossie = json.load(io.open(fd, encoding="utf-8"))
    if len(mapa.get("takes", [])) != len(dossie["takes"]):
        raise SystemExit("o mapa tem %d take(s) e o dossie tem %d — o modelo "
                         "leu um numero de cenas diferente do detectado."
                         % (len(mapa.get("takes", [])), len(dossie["takes"])))

    blocos, avisos = montar(mapa, dossie, a.modo, a.takes)
    saida = "\n\n".join("%s\n%s" % (("=" * 70), v) if False else v
                        for v in blocos.values())
    io.open(os.path.join(d, "prompts.txt"), "w", encoding="utf-8").write(saida)

    print("%s · %d bloco(s) · modo %s" % (a.slug, len(blocos), a.modo))
    for k, v in blocos.items():
        print("   %-16s %5d chars%s" % (k, len(v),
                                        "  ⛔" if len(v) > TETO_BLOCO else ""))
    if avisos:
        print("\nAVISOS (%d):" % len(avisos))
        for x in avisos:
            print("   %s" % x)
    print("\n-> %s" % os.path.join(d, "prompts.txt"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
