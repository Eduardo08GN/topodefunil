# -*- coding: utf-8 -*-
"""Baseline: hash do HTML PT de cada categoria. Roda ANTES e DEPOIS do i18n.
Se um hash mudar, o i18n regrediu o produto que ja' esta' vendendo."""
import hashlib, importlib, os, sys
import motor_receitas as motor

CFG = {"cafe": ("receitas_cafe", "cafe", 1, "Cafes da Manha Fit"),
       "almoco": ("receitas_almoco", "almoco", 31, "Almocos Fit"),
       "jantar": ("receitas_jantar", "jantar", 66, "Jantares Fit"),
       "sobremesa": ("receitas_sobremesa", "sobremesa", 101, "Sobremesas Fit"),
       "suco": ("receitas_suco", "suco", 121, "Vitaminas e Sucos Detox")}
AQUI = os.path.dirname(os.path.abspath(__file__))
img = os.path.join(AQUI, "fotos")

def _tag_suco(nome):
    n = nome.lower()
    if "cha" in n or "chá" in n or "chá" in n or "infus" in n: return "Cha detox"
    if "água" in n: return "Agua detox"
    if "vitamina" in n or "smoothie" in n: return "Vitamina"
    return "Suco detox"

for cat, (mod_nome, tipo, num0, titulo) in CFG.items():
    mod = importlib.import_module(mod_nome)
    if cat == "suco":
        for r in mod.RECEITAS:
            r.setdefault("tag", _tag_suco(r["nome"]))
    h = motor.montar_html(mod.RECEITAS, tipo, titulo, num0=num0, img_dir=img)
    print("%-10s %s  %7d chars" % (cat, hashlib.sha256(h.encode("utf-8")).hexdigest()[:16], len(h)))
