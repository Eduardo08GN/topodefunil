#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Randomizador PRISMA — sorteio multi-eixo com GARANTIA MEDIDA de distancia entre videos.

Diferenca para o randomizador-v6: o v6 varia so o hook (cena 1) e trava o resto.
O PRISMA sorteia 10 eixos VISIVEIS (CONCEITO da cena, esqueleto narrativo, setting,
gramatica visual, luz, molde de hook, dispositivo, dor, registro emocional, wardrobe)
e usa um solver greedy max-min para escolher o lote que maximiza a distancia par-a-par.

O eixo CONCEITO e o mais pesado: e o bit visual que carrega o video no mudo
(demo quimica, prop gigante, duo com esposa/amigo, loja big-box, telejornal falso,
podcast, etiquetas Day 0->7) — engenharia reversa de Alisha/Marcus Hayes/Angela
Brooks em 2026-07-28. Talking head solo virou UMA opcao entre dez, nao o padrao.

Contrato: dois videos sao "distintos" se diferem em >= 6 dos 10 eixos.
O relatorio final IMPRIME a % de pares distintos — a meta e >= 70%, o solver
normalmente entrega > 95%. Se um lote sair abaixo de 70%, o script avisa e o
agente NAO deve escrever o lote (rode de novo com outra seed ou n menor).

Uso:
  python funil-organico/randomizador-prisma.py --pagina joe --n 50
  python funil-organico/randomizador-prisma.py --pagina matt --n 10 --seed 42 --dry-run
  python funil-organico/randomizador-prisma.py --stats
"""
import argparse
import hashlib
import json
import random
import sys
from itertools import combinations
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

LEDGER = Path(__file__).parent / ".prisma-ledger.json"

# ---------------------------------------------------------------- paginas
PAGINAS = {
    "joe":    {"dominio": "manresethub.pro",        "etnia": "branco"},
    "marcus": {"dominio": "vitalresetlab.site",     "etnia": "negro"},
    "ray":    {"dominio": "primalvitalityhub.site", "etnia": "branco"},
    "chuck":  {"dominio": "allmensnatural.site",    "etnia": "negro"},
    "matt":   {"dominio": "steadystrengthhub.site", "etnia": "branco"},
}

# ---------------------------------------------------------------- eixos
ESQUELETOS = [
    "E1_isca_e_troca", "E2_direta", "E3_esposa", "E4_confissao",
    "E5_experimento", "E6_expose", "E7_diario", "E8_mito_verdade",
]
# CONCEITO = o bit visual que carrega o video no mudo (o eixo que faltava)
CONCEITOS = [
    "solo_classico",    # talking head puro — agora UMA opcao, nao o padrao
    "demo_quimica",     # reacao visivel no prop (baking soda + melancia etc.)
    "prop_gigante",     # prop comicamente grande em cena (selo amarelo — ver banco-hooks H4)
    "duo_esposa",       # esposa + marido no mesmo quadro (antes/depois, ela conduz)
    "duo_amigo",        # segundo personagem homem (o amigo cetico/barrigudo)
    "local_publico",    # loja big-box generica / estacionamento / corredor farmacia
    "pov_mercado",      # selfie andando no corredor, produto na mao
    # "fake_broadcast" REMOVIDO (2026-07-28, ordem do operador): risco de ban ja
    # documentado em empilhamento-reptiliano.md ("eles usam, nos NAO") e o Ed
    # rejeitou o ancora de jornal em producao. Nao re-adicionar sem decisao dele.
    "podcast",          # mesa com microfone e fone, estetica de clipe de podcast
    "day_labels",       # progressao Day 0 -> Day 7 com etiqueta manuscrita (regra V4: max 2 palavras)
    "flagrante_publico",# humilhacao publica testemunhada (Tanisha Rivers, 20-50x a media dela)
                        # acoplado ao molde M15 — cena 1 publica com vitima + testemunhas,
                        # cenas 2-5 em set interno (a troca de set faz parte do padrao)
    "prop_ressurreicao",# prop GIGANTE murcho -> vertical apos despejo da substancia
                        # (Tanisha reel 856954520543734, 1.6K/673/211, IA gerada e passou):
                        # lab branco, bandeja inox, narrador pequeno em frente do prop monumental
    "antes_depois_gemeo",# ⭐ MAIOR TRACAO MEDIDA: 345K views / 7.7K (Zariah 1487684136039129)
                        # MESMO homem, MESMA roupa, MESMO enquadramento, cut seco em ~2s:
                        # corpo barrigudo -> rasgado E o prop na mao ~4x MAIOR (tamanho, nao
                        # so firmeza). A promessa numerica do hook fica literal na tela.
                        # Acoplado a M6.
    "pip_broll",        # narrador pequeno recortado num canto + B-roll dominante (corrente
                        # sanguinea 3D, anatomia). B-roll entra NO EDITOR, nao no Veo.
]
# conceitos "ambulantes": a pessoa esta de pe em espaco publico, sem bancada.
# demo clinica (modelo anatomico / demo quimica) nao cabe neles.
AMBULANTES = ["local_publico", "pov_mercado", "flagrante_publico"]

# PICO 2 = o segundo bit visual, nas cenas 2 ou 4. O conceito carrega o HOOK e
# so ele; sem um segundo pico o video vira 1 choque + 4 cenas de cobertura e
# morre no segundo 9 (falha em producao, lote Joe 2026-07-28 — ver P16).
PICOS2 = [
    "colo_crescimento",       # mulher (etnia da pagina) sentada no colo dele, prop alongando na mao dela, rosto de surpresa
    "reacao_testemunha",      # segunda pessoa entra no quadro, ve o resultado e reage com choque
    "demo_quimica_prop",      # despeja a substancia no prop e a reacao acontece na tela
    "antes_depois_prop",      # cut seco entre dois estados do prop na bancada (murcho -> maior e firme)
    "prop_gigante_revelacao", # ele puxa de fora de quadro um prop comicamente grande
    "esposa_reagindo",        # ela surge atras dele, olha pra camera, reacao muda (boca aberta / revira os olhos)
    "pilha_pilulas",          # ele varre uma pilha de frascos de pilula pra lixeira num gesto so
    "fita_metrica",           # dois props lado a lado, a promessa do hook fica literal na tela
]
# picos que exigem prop na mao — nao cabem com dispositivo=nenhum (senao viola P5)
PICOS2_COM_PROP = [
    "colo_crescimento", "demo_quimica_prop", "antes_depois_prop",
    "prop_gigante_revelacao", "fita_metrica",
]
# o pico 2 nunca repete o bit do hook — se o conceito ja e aquilo, o pico e outro
PICO2_COLIDE = {
    "demo_quimica":       ["demo_quimica_prop"],
    "antes_depois_gemeo": ["antes_depois_prop", "colo_crescimento", "fita_metrica"],
    "prop_gigante":       ["prop_gigante_revelacao"],
    "prop_ressurreicao":  ["antes_depois_prop", "prop_gigante_revelacao"],
    "duo_esposa":         ["esposa_reagindo", "colo_crescimento"],
    "duo_amigo":          ["reacao_testemunha"],
    # esposa_reagindo fora do flagrante: ela ja esta no hook, e a reacao muda
    # dela na cena 4 nao e bit — e figurante (falha Chuck/fila 2026-07-28, F15)
    "flagrante_publico":  ["reacao_testemunha", "esposa_reagindo"],
}
# familia "crescimento": desde a regra do despejo (P17), TODO pouring termina em
# prop alongando. Entao se o hook ja cresce, um pico2 que tambem cresce e o mesmo
# truque duas vezes — e dois choques do mesmo tipo somam a um.
PICOS2_CRESCIMENTO = ["colo_crescimento", "demo_quimica_prop", "antes_depois_prop"]
CONCEITOS_QUE_CRESCEM = ["demo_quimica", "prop_ressurreicao"]
SETTINGS = [
    "kitchen", "garage_bancada", "backyard_deck", "truck_cabine",
    "ranch", "varanda_manha", "quintal_grill", "escritorio_caseiro",
    "penthouse_urbano",
    "loja_bigbox", "estacionamento_loja", "corredor_farmacia",
    "estudio_news", "estudio_podcast", "laboratorio",
]
SETTINGS_DOMESTICOS = [
    "kitchen", "garage_bancada", "backyard_deck", "truck_cabine",
    "ranch", "varanda_manha", "quintal_grill", "escritorio_caseiro",
    "penthouse_urbano",
]
GRAMATICAS = [
    "talking_head_classico", "sentado_mesa", "demo_maos_e_rosto",
    "close_confessional", "sentado_carro", "low_angle_deck",
]
LUZES = ["morning_window", "golden_hour", "night_lamp", "overcast_soft", "noon_harsh"]
LUZES_ESPECIAIS = ["fluorescente_loja", "luz_estudio"]
REGISTROS = [
    "raiva_contida", "humor_seco", "vergonha_crua",
    "professor_calmo", "conspiratorio", "urgencia_alarme",
]
DISPOSITIVOS = [
    "H1_proxy_peito", "H4_soft", "H7_pouring",
    "D1_modelo_anatomico", "D4_demo_quimica",  # "nenhum" removido: P18 — todo hook tem proxy
]
WARDROBES = [
    "flannel", "henley", "polo", "plain_tee", "jaqueta_leve", "camisa_trabalho",
    "scrub_medico",  # uniforme clinico colorido — autoridade sem jaleco (Zariah, 345K)
]
DORES = [
    "momento_constrangedor", "desculpas_toda_noite", "gastos_farmacia",
    "medo_do_quarto", "fogo_apagando", "evitar_intimidade",
    "perda_confianca", "parceira_percebe", "efeitos_colaterais", "vergonha_medico",
]

# hook (mesmos pools do banco-hooks.md — fonte: banco-hooks.md)
MOLDES = [
    "M1_substancia_absurda", "M2_consequencia", "M3_triade", "M4_reacao",
    "M5_comando_social", "M6_antes_depois", "M7_isca_troca", "M8_combo_absurdo",
    "M9_confissao", "M10_pergunta", "M11_aviso_falso", "M12_prova_manha",
    "M13_medo_rival", "M14_ataque_industria", "M15_flagrante_publico",
]
SUBSTANCIAS = [
    "toothpaste", "coca_cola", "baking_soda", "lime", "lemon", "raw_garlic",
    "vaseline", "coconut_oil", "cinnamon", "turmeric", "olive_oil", "raw_honey",
    "aloe", "apple_cider_vinegar", "crushed_ice", "coffee",
]
PROPS = [
    "banana", "cucumber", "watermelon", "geoduck", "daikon", "carrot",
    "zucchini", "corn", "eggplant", "sausage", "peach", "melon",
]
PROMESSAS = [
    "3_to_8_inches", "six_inches_two_weeks", "hidden_inches", "this_to_this_one_month",
    "ten_times_bigger", "different_man_by_morning", "wife_wont_keep_up", "five_inches_a_week",
]
MODIFICADORES = ["pharma", "doctor", "ceticismo", "escassez", "insider", "nenhum"]

# ---------------------------------------------------------------- REF solto (politica 2026-07-28)
# REF NAO e mais travado por pagina: cada video sorteia um rosto novo.
# Unica trava: etnia congruente com o avatar da pagina (negro -> so afro-americano US).
# Fora do contrato de distancia (nao conta nos 10 eixos) — e identidade, nao bit visual.
REF_IDADES = ["52", "55", "58", "61", "64", "67", "70", "73"]
REF_MARCAS = [
    "extensive vitiligo patches on face and neck", "a bold white streak in the hair",
    "a thin scar through one eyebrow", "a small notch missing from the top of one ear",
    "heterochromia, one blue eye one brown", "a large dark birthmark on one cheek",
    "a long distinctive beard reaching mid-chest", "a shaved head with a gray goatee",
    "deep smile lines and a gold front tooth glint", "thick black-rimmed glasses and heavy brows",
]
REF_FISICOS = [
    "lean wiry build", "stocky barrel-chested build", "fit athletic build",
    "heavyset soft build", "tall broad-shouldered build",
]

# ---------------------------------------------------------------- compatibilidades
ESQ_MOLDES = {
    "E1_isca_e_troca": ["M1_substancia_absurda", "M7_isca_troca", "M8_combo_absurdo", "M5_comando_social", "M15_flagrante_publico"],
    "E2_direta":       ["M1_substancia_absurda", "M2_consequencia", "M3_triade", "M5_comando_social", "M12_prova_manha", "M8_combo_absurdo", "M15_flagrante_publico"],
    "E3_esposa":       ["M11_aviso_falso", "M6_antes_depois"],
    "E4_confissao":    ["M9_confissao", "M13_medo_rival", "M12_prova_manha"],
    "E5_experimento":  ["M4_reacao"],
    "E6_expose":       ["M14_ataque_industria", "M10_pergunta", "M2_consequencia", "M15_flagrante_publico"],
    "E7_diario":       ["M6_antes_depois", "M12_prova_manha"],
    "E8_mito_verdade": ["M10_pergunta", "M3_triade", "M7_isca_troca"],
}
DISP_POR_MOLDE = {
    "M1_substancia_absurda": ["H1_proxy_peito", "H7_pouring"],
    "M2_consequencia":       ["D1_modelo_anatomico", "H1_proxy_peito"],
    "M3_triade":             ["D1_modelo_anatomico", "H1_proxy_peito"],
    "M4_reacao":             ["D4_demo_quimica"],
    "M5_comando_social":     ["H1_proxy_peito", "H7_pouring"],
    "M6_antes_depois":       ["H4_soft", "H1_proxy_peito"],
    "M7_isca_troca":         ["H1_proxy_peito", "H7_pouring"],
    "M8_combo_absurdo":      ["H1_proxy_peito", "H7_pouring"],
    # M9/M11/M13 emitiam "nenhum" e violavam o P18 ("todo hook tem proxy, sem
    # excecao"). Resolvido 2026-07-28: proxy neles tambem — na confissao o proxy
    # MURCHO na mao e a propria confissao visual; no aviso falso ela segura o
    # proxy firme como "prova do perigo".
    "M9_confissao":          ["H1_proxy_peito", "H4_soft"],
    "M10_pergunta":          ["D1_modelo_anatomico"],
    "M11_aviso_falso":       ["H1_proxy_peito"],
    "M12_prova_manha":       ["H1_proxy_peito"],
    "M13_medo_rival":        ["H4_soft", "H1_proxy_peito"],
    "M14_ataque_industria":  ["D1_modelo_anatomico"],
    # M15: o REF segura o proxy AO LADO da vitima (proxy murcho = a evidencia).
    # ⚠️ ANTES daqui saia inferido de UM reel da Tanisha. Errado: o hook
    # sem proxy perde o scroll-stopper (falha em producao, lote Matt 2026-07-28 — P18).
    "M15_flagrante_publico": ["H4_soft", "H1_proxy_peito"],
}
SETTINGS_POR_ESQ = {
    "E5_experimento": ["kitchen", "garage_bancada"],
    "E7_diario":      ["kitchen", "varanda_manha", "backyard_deck", "escritorio_caseiro"],
    "E3_esposa":      ["kitchen", "varanda_manha", "escritorio_caseiro", "backyard_deck", "quintal_grill"],
}
# conceito por esqueleto: a historia dita quais bits visuais fazem sentido
CONC_POR_ESQ = {
    "E1_isca_e_troca": ["solo_classico", "demo_quimica", "duo_amigo", "pov_mercado", "prop_gigante", "prop_ressurreicao", "pip_broll"],
    "E2_direta":       ["solo_classico", "prop_gigante", "local_publico", "pov_mercado", "podcast", "duo_amigo", "prop_ressurreicao", "pip_broll", "antes_depois_gemeo"],
    "E3_esposa":       ["duo_esposa", "solo_classico", "local_publico", "antes_depois_gemeo"],
    "E4_confissao":    ["solo_classico", "podcast", "pip_broll"],
    "E5_experimento":  ["demo_quimica", "prop_ressurreicao"],
    "E6_expose":       ["podcast", "solo_classico", "local_publico", "pip_broll"],
    "E7_diario":       ["day_labels", "solo_classico", "antes_depois_gemeo"],
    "E8_mito_verdade": ["solo_classico", "podcast", "prop_gigante", "pip_broll"],
}
# settings validos por conceito (None = usa SETTINGS_POR_ESQ / domesticos)
SETTINGS_POR_CONC = {
    "antes_depois_gemeo": ["penthouse_urbano", "escritorio_caseiro", "kitchen", "quintal_grill"],
    "prop_ressurreicao": ["laboratorio", "kitchen", "garage_bancada"],
    "flagrante_publico": ["loja_bigbox", "corredor_farmacia", "estacionamento_loja"],
    "local_publico":  ["loja_bigbox", "estacionamento_loja", "corredor_farmacia"],
    "pov_mercado":    ["loja_bigbox", "corredor_farmacia"],
    "podcast":        ["estudio_podcast"],
    "demo_quimica":   ["kitchen", "garage_bancada", "quintal_grill"],
    "prop_gigante":   ["kitchen", "backyard_deck", "quintal_grill", "estacionamento_loja"],
}
GRAM_POR_SETTING = {
    "kitchen":             ["talking_head_classico", "demo_maos_e_rosto", "sentado_mesa", "close_confessional"],
    "garage_bancada":      ["talking_head_classico", "demo_maos_e_rosto", "close_confessional"],
    "backyard_deck":       ["talking_head_classico", "low_angle_deck", "close_confessional"],
    "truck_cabine":        ["sentado_carro", "close_confessional"],
    "ranch":               ["talking_head_classico", "close_confessional"],
    "varanda_manha":       ["talking_head_classico", "sentado_mesa", "low_angle_deck", "close_confessional"],
    "quintal_grill":       ["talking_head_classico", "close_confessional"],
    "escritorio_caseiro":  ["sentado_mesa", "close_confessional", "talking_head_classico"],
    "penthouse_urbano":    ["talking_head_classico", "sentado_mesa", "close_confessional"],
    "laboratorio":         ["talking_head_classico", "demo_maos_e_rosto"],
    "loja_bigbox":         ["talking_head_classico", "demo_maos_e_rosto"],
    "estacionamento_loja": ["talking_head_classico"],
    "corredor_farmacia":   ["talking_head_classico", "close_confessional"],
    "estudio_news":        ["sentado_mesa"],
    "estudio_podcast":     ["sentado_mesa", "close_confessional"],
}
LUZ_POR_SETTING = {
    "laboratorio":         ["fluorescente_loja"],
    "loja_bigbox":         ["fluorescente_loja"],
    "corredor_farmacia":   ["fluorescente_loja"],
    "estacionamento_loja": ["noon_harsh", "overcast_soft", "golden_hour"],
    "estudio_news":        ["luz_estudio"],
    "estudio_podcast":     ["luz_estudio", "night_lamp"],
}
# segundo personagem por conceito (esposa herda etnia da pagina; amigo e livre)
SEGUNDO_POR_CONC = {
    "duo_esposa":         "esposa_etnia_da_pagina",
    "duo_amigo":          "amigo_etnia_livre",
    "flagrante_publico":  "vitima_flagrante",   # + testemunhas desfocadas ao fundo (cena 1)
    "antes_depois_gemeo": "sujeito_transformado",  # o MESMO homem em 2 estados, cut seco
}
REG_POR_ESQ = {
    "E1_isca_e_troca": ["conspiratorio", "humor_seco", "urgencia_alarme", "professor_calmo"],
    "E2_direta":       ["professor_calmo", "urgencia_alarme", "raiva_contida", "humor_seco"],
    "E3_esposa":       ["humor_seco", "urgencia_alarme", "conspiratorio", "vergonha_crua"],
    "E4_confissao":    ["vergonha_crua", "raiva_contida"],
    "E5_experimento":  ["professor_calmo", "humor_seco", "urgencia_alarme"],
    "E6_expose":       ["raiva_contida", "conspiratorio", "professor_calmo"],
    "E7_diario":       ["professor_calmo", "humor_seco", "vergonha_crua"],
    "E8_mito_verdade": ["professor_calmo", "conspiratorio", "raiva_contida"],
}

# eixos usados na metrica de distancia
EIXOS_DIST = ["conceito", "pico2", "esqueleto", "setting", "gramatica", "luz", "molde", "dispositivo", "dor", "registro", "wardrobe"]
LIMIAR_DISTINTO = 7  # >= 7 eixos diferentes de 11 = par distinto (mesma proporcao do 6/10 anterior)


# ---------------------------------------------------------------- geracao
def gerar_candidato(etnia, rng, conceitos_recentes=()):
    esq = rng.choice(ESQUELETOS)
    molde = rng.choice(ESQ_MOLDES[esq])
    disp = rng.choice(DISP_POR_MOLDE[molde])

    # conceito: filtrado pelo dispositivo/molde sorteado
    if molde == "M15_flagrante_publico":
        conceito = "flagrante_publico"  # o flagrante E o hook — acoplamento 1:1
    else:
        concs = list(CONC_POR_ESQ[esq])
        if disp == "D4_demo_quimica":
            concs = ["demo_quimica", "prop_ressurreicao"]
        else:
            concs = [c for c in concs if c != "demo_quimica"]
            if disp != "H7_pouring":
                concs = [c for c in concs if c != "prop_ressurreicao"]
        if disp not in ("H1_proxy_peito", "H4_soft", "H7_pouring"):
            concs = [c for c in concs if c != "prop_gigante"]
        # antes_depois_gemeo exige o molde M6 (o hook E o cut seco) e prop na mao
        if molde != "M6_antes_depois":
            concs = [c for c in concs if c != "antes_depois_gemeo"]
        # pip_broll: narrador pequeno no canto — mao ociosa, sem prop
        if disp != "nenhum":
            concs = [c for c in concs if c != "pip_broll"]
        # demo clinica NUNCA em conceito ambulante: modelo anatomico em pe numa loja
        # vira aula de anatomia, nao video de ED (falha em producao 2026-07-28)
        if disp in ("D1_modelo_anatomico", "D4_demo_quimica"):
            concs = [c for c in concs if c not in AMBULANTES]
        # memoria de conceito: em lote pequeno nao ha par pra o solver medir, entao
        # o ledger e a unica protecao. Sem isso, gerando 1 video por vez, o eixo mais
        # pesado do sistema repete (falha 2026-07-28: solo_classico duas vezes seguidas).
        frescos = [c for c in concs if c not in conceitos_recentes]
        if frescos:
            concs = frescos
        conceito = rng.choice(concs) if concs else "solo_classico"

    settings = SETTINGS_POR_CONC.get(conceito) or SETTINGS_POR_ESQ.get(esq, SETTINGS_DOMESTICOS)
    if etnia == "negro":
        settings = [s for s in settings if s != "ranch"]
    setting = rng.choice(settings)
    grams = GRAM_POR_SETTING[setting]
    if disp == "D4_demo_quimica":
        gram = "demo_maos_e_rosto" if "demo_maos_e_rosto" in grams else rng.choice(grams)
    else:
        gram = rng.choice(grams)

    # pico 2: o segundo bit visual (cena 2 ou 4). Nunca repete o bit do hook.
    picos = [p for p in PICOS2 if p not in PICO2_COLIDE.get(conceito, [])]
    if disp == "nenhum":
        picos = [p for p in picos if p not in PICOS2_COM_PROP]
    # hook que ja cresce nao ganha pico2 que tambem cresce (P17 + regra do 2o pico)
    if disp == "H7_pouring" or conceito in CONCEITOS_QUE_CRESCEM:
        picos = [p for p in picos if p not in PICOS2_CRESCIMENTO]
    if conceito in AMBULANTES or setting in ("estacionamento_loja", "corredor_farmacia", "loja_bigbox"):
        # exige estar sentado — MAS no flagrante o pico2 mora nas cenas internas
        # 2-5 (F6), onde sentar cabe. Excluir o flagrante deste filtro (bug
        # corrigido 2026-07-28: o filtro bloqueava o climax do angulo inteiro).
        if conceito != "flagrante_publico":
            picos = [p for p in picos if p != "colo_crescimento"]
    if conceito == "flagrante_publico":
        # a REDENCAO pede CLIMAX visual (falha em producao Chuck/fila 2026-07-28:
        # esposa_reagindo degradou em figurante muda atras do narrador — cara de
        # reacao nao e bit). Default: colo_crescimento do CASAL REDIMIDO (a mulher
        # no colo da vitima, o prop do hook agora ereto na mao dela) — 3x o peso.
        pesos = [3 if p == "colo_crescimento" else 1 for p in picos]
        pico2 = rng.choices(picos, weights=pesos)[0] if picos else "colo_crescimento"
        pico2_cena = 4  # a redencao E a cena 4 — arco fixo do flagrante
    else:
        pico2 = rng.choice(picos) if picos else "reacao_testemunha"
        # cena 4 (RESULTADO) e o lugar natural: a copy ja e o payoff, a imagem paga junto.
        # cena 2 quando o choque pertence a causa. Nunca 3 (maos em acao) nem 5 (CTA limpo).
        pico2_cena = rng.choices([4, 2], weights=[3, 1])[0] if picos else 4

    return {
        "conceito": conceito,
        "esqueleto": esq,
        "setting": setting,
        "gramatica": gram,
        "luz": rng.choice(LUZ_POR_SETTING.get(setting, LUZES)),
        "molde": molde,
        "dispositivo": disp,
        "dor": rng.choice(DORES),
        "registro": rng.choice(REG_POR_ESQ[esq]),
        "wardrobe": rng.choice(WARDROBES),
        "pico2": pico2,
        "pico2_cena": pico2_cena,
        "segundo": SEGUNDO_POR_CONC.get(conceito, "nenhum"),
        "substancia": rng.choice(SUBSTANCIAS),
        "prop": rng.choice(PROPS),
        "promessa": rng.choice(PROMESSAS),
        "modificador": rng.choice(MODIFICADORES),
        "cta": "GELATIN",
        # REF solto por video (fora do contrato de distancia)
        "ref_idade": rng.choice(REF_IDADES),
        "ref_marca": rng.choice(REF_MARCAS),
        "ref_fisico": rng.choice(REF_FISICOS),
    }


def dist(a, b):
    return sum(1 for e in EIXOS_DIST if a[e] != b[e])


def spec_id(spec):
    base = json.dumps({k: spec[k] for k in sorted(spec)}, sort_keys=True)
    return hashlib.sha1(base.encode()).hexdigest()[:12]


def hook_triplo(spec):
    return (spec["molde"], spec["substancia"], spec["prop"])


JANELA_CONCEITO = 3  # quantos conceitos recentes ficam bloqueados


def carregar_ledger():
    if LEDGER.exists():
        led = json.loads(LEDGER.read_text(encoding="utf-8"))
        led.setdefault("conceitos", [])  # compat: ledgers antigos nao tinham o campo
        return led
    return {"hooks": [], "specs": [], "conceitos": []}


def salvar_ledger(ledger):
    LEDGER.write_text(json.dumps(ledger, indent=1), encoding="utf-8")


def selecionar_lote(n, etnia, rng, hooks_usados, conceitos_recentes=()):
    # em lote grande o solver max-min ja garante variedade de conceito; a memoria
    # do ledger serve pro caso critico do lote pequeno (1-3 videos por vez)
    if n > len(CONCEITOS) // 2:
        conceitos_recentes = ()
    # pool grande de candidatos validos, sem hook repetido vs ledger
    pool, vistos = [], set()
    for _ in range(max(4000, n * 80)):
        c = gerar_candidato(etnia, rng, conceitos_recentes)
        chave = tuple(c[e] for e in EIXOS_DIST) + hook_triplo(c)
        if chave in vistos or list(hook_triplo(c)) in hooks_usados:
            continue
        vistos.add(chave)
        pool.append(c)
    if len(pool) < n:
        raise SystemExit(f"pool insuficiente ({len(pool)} < {n}) — espaco quase esgotado, rode --stats")

    # greedy max-min: comeca aleatorio, adiciona sempre o candidato mais distante do lote
    sel = [pool.pop(rng.randrange(len(pool)))]
    hooks_lote = {hook_triplo(sel[0])}
    while len(sel) < n:
        rng.shuffle(pool)
        melhor, melhor_d = None, -1
        for c in pool:
            if hook_triplo(c) in hooks_lote:
                continue
            d = min(dist(c, s) for s in sel)
            if d > melhor_d:
                melhor, melhor_d = c, d
        if melhor is None:
            raise SystemExit("sem candidatos com hook inedito suficientes — diminua --n")
        sel.append(melhor)
        hooks_lote.add(hook_triplo(melhor))
        pool.remove(melhor)
    return sel


def relatorio(sel):
    if len(sel) < 2:
        print("\n# lote de 1 spec — sem pares para medir; distincao garantida vs ledger (hook inedito)")
        return 100.0
    pares = list(combinations(sel, 2))
    ds = [dist(a, b) for a, b in pares]
    ne = len(EIXOS_DIST)
    pct = 100.0 * sum(1 for d in ds if d >= LIMIAR_DISTINTO) / len(ds)
    print(f"\n# RELATORIO DE DISTINCAO ({len(sel)} specs, {len(pares)} pares)")
    print(f"#   distancia minima: {min(ds)}/{ne} | media: {sum(ds)/len(ds):.1f}/{ne}")
    print(f"#   pares distintos (>= {LIMIAR_DISTINTO}/{ne} eixos): {pct:.1f}%   [meta >= 70%]")
    if pct < 70:
        print("#   *** LOTE REPROVADO — nao escreva. Rode de novo (outra seed ou n menor). ***")
    for eixo in EIXOS_DIST:
        usados = len({s[eixo] for s in sel})
        print(f"#   cobertura {eixo}: {usados} valores usados")
    return pct


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pagina", choices=sorted(PAGINAS))
    ap.add_argument("--n", type=int, default=10)
    ap.add_argument("--seed", type=int)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--stats", action="store_true")
    args = ap.parse_args()

    ledger = carregar_ledger()
    if args.stats:
        print(f"ledger: {len(ledger['specs'])} specs emitidas, {len(ledger['hooks'])} hooks queimados")
        return
    if not args.pagina:
        ap.error("--pagina obrigatorio (ou --stats)")

    pag = PAGINAS[args.pagina]
    seed = args.seed if args.seed is not None else random.randrange(10**6)
    rng = random.Random(seed)

    recentes = ledger["conceitos"][-JANELA_CONCEITO:]
    sel = selecionar_lote(args.n, pag["etnia"], rng, ledger["hooks"], recentes)
    if recentes:
        print(f"# conceitos bloqueados (ultimos {JANELA_CONCEITO} do ledger): {', '.join(recentes)}")

    print(f"# Specs PRISMA - pagina={args.pagina} ({pag['dominio']}) - etnia={pag['etnia']} - seed={seed} - CTA travado=GELATIN")
    print(f"# {args.n} specs. 10 eixos sorteados (conceito = bit visual), solver max-min, hook inedito vs ledger.\n")
    for i, s in enumerate(sel, 1):
        sid = spec_id(s)
        seg = f" segundo={s['segundo']}" if s["segundo"] != "nenhum" else ""
        print(f"P{i:02d} [{sid}] CONCEITO={s['conceito']} | {s['esqueleto']} | setting={s['setting']} gram={s['gramatica']} luz={s['luz']} registro={s['registro']}{seg}")
        print(f"     hook: molde={s['molde']} subst={s['substancia']} prop={s['prop']} mod={s['modificador']} promessa={s['promessa']} disp={s['dispositivo']}")
        print(f"     DEMO OBRIGATORIA (P20): {s['substancia']} APLICADA no {s['prop']} na tela, no TAKE do hook -> crescimento rapido + reacao. Prop so na mao = P20.")
        print(f"     PICO2={s['pico2']} na cena {s['pico2_cena']}")
        print(f"     corpo: dor={s['dor']} wardrobe={s['wardrobe']} cta={s['cta']}")
        print(f"     REF solto: idade={s['ref_idade']} etnia={pag['etnia']} marca=\"{s['ref_marca']}\" fisico=\"{s['ref_fisico']}\"")

    pct = relatorio(sel)

    if not args.dry_run and pct >= 70:
        for s in sel:
            ledger["hooks"].append(list(hook_triplo(s)))
            ledger["specs"].append(spec_id(s))
            ledger["conceitos"].append(s["conceito"])
        salvar_ledger(ledger)
        print(f"\n# ledger atualizado: {len(ledger['specs'])} specs emitidas no total")
    elif args.dry_run:
        print("\n# dry-run: ledger NAO atualizado")


if __name__ == "__main__":
    main()
