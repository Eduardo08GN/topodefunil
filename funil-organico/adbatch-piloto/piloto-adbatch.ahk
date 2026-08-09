#Requires AutoHotkey v2.0
#SingleInstance Force
SendMode "Event"          ; ⚠️ Event, nao Input: apps tkinter e o Chrome perdem
SetKeyDelay 30, 30        ;    cliques sinteticos rapidos demais.
SetMouseDelay 40
CoordMode "Mouse", "Screen"
CoordMode "Pixel", "Screen"

/*
===============================================================================
 PILOTO ADBATCH — o ciclo agente -> AdBatch Vertical 2, em N abas
===============================================================================

 O QUE ELE FAZ, por aba do Chrome:
   1. no AGENTE (monitor vertical): seleciona BLOCO 0 (REF) e copia
   2. copia os 2 IMAGE
   3. copia os 2 TAKE
   4. no CHROME (monitor horizontal): cola os tres no "Roteiro Master"
   5. clica em "Gerar Lote com Referencia"
   6. volta ao agente, marca como usado e sorteia o proximo (Ctrl+R)
   7. proxima aba

 Depois de preencher todas, entra em RONDA: revisita cada aba e, se um slot
 ainda estiver vazio, clica REGERAR nele. Repete ate' todos cheios ou ate' o
 limite de rondas.

 ⛔⛔ NADA DE COORDENADA CHUTADA. Rode a CALIBRACAO uma vez (F9): o script
 pergunta alvo por alvo, voce poe o mouse em cima e aperta F9 de novo. Fica
 tudo gravado no .ini ao lado — nao se perde ao fechar.

 ⚠️⚠️ A ARMADILHA DESTE TIPO DE SCRIPT E' O CLIPBOARD MUDO: se um clique de
 copiar falha, a area de transferencia continua com o conteudo ANTERIOR e o
 script cola o video da aba passada sem reclamar. Por isso, a cada copia:
 limpa o clipboard, clica, espera, e CONFERE A ASSINATURA do conteudo
 (`REF 01:`, `IMAGE 01/02`, `TAKE 01/02`). Assinatura errada = para e avisa.

 TECLAS
   F9   calibrar (ou recalibrar) os pontos de clique
   F10  rodar o ciclo completo
   F8   ensaio seco: percorre tudo SEM colar e SEM clicar em Gerar
   Esc  aborta na hora, em qualquer momento
   F12  mostra o log da ultima execucao

===============================================================================
*/

INI := A_ScriptDir "\piloto-adbatch.ini"
ARQ_LOG := A_ScriptDir "\piloto-adbatch.log"

; --- os alvos de clique, na ordem em que a calibracao pergunta ---------------
; chave | onde | o que e'
ALVOS := [
    ["ag_bloco_ref", "AGENTE",  "o item BLOCO 0 (REF) na lista da secao 3"],
    ["ag_copiar",    "AGENTE",  "o botao laranja COPIAR BLOCO"],
    ["ag_imgs",      "AGENTE",  "o botao 'copiar os 2 IMAGE'"],
    ["ag_takes",     "AGENTE",  "o botao 'copiar os 2 TAKE'"],
    ["ag_usado",     "AGENTE",  "o botao 'marcar como usado'"],
    ["cr_roteiro",   "CHROME",  "a caixa 'Cole o roteiro inteiro...' (Roteiro Master)"],
    ["cr_gerar",     "CHROME",  "o botao 'Gerar Lote com Referencia'"],
    ["cr_slot1",     "CHROME",  "o MEIO do quadro cinza do SLOT 01 (onde a imagem aparece)"],
    ["cr_slot2",     "CHROME",  "o MEIO do quadro cinza do SLOT 02"],
    ["cr_reger1",    "CHROME",  "o botao REGERAR do SLOT 01"],
    ["cr_reger2",    "CHROME",  "o botao REGERAR do SLOT 02"],
]

global abortar := false
global linhas := []
; ⚠️ `rodando` existe so' para escopar o Esc. Sem isso o script sequestra a
; tecla Esc do Windows inteiro enquanto estiver carregado, e o operador perde
; o Esc em toda janela — automacao que atrapalha fora da propria tarefa e' pior
; que automacao nenhuma.
global rodando := false

; =============================================================================
;  TECLAS
; =============================================================================
F9::  calibrar()
F10:: rodar(false)
F8::  rodar(true)
F12:: mostrarLog()
#HotIf rodando          ; ⛔ o Esc so' existe ENQUANTO o ciclo roda
Esc:: {
    global abortar
    abortar := true
    ToolTip "ABORTANDO..."
    SetTimer () => ToolTip(), -1200
}
#HotIf

; =============================================================================
;  CALIBRACAO
; =============================================================================
calibrar() {
    global INI, ALVOS, rodando
    rodando := true          ; o Esc precisa funcionar durante a calibracao
    try
        calibrarMiolo()
    finally
        rodando := false
}

calibrarMiolo() {
    global INI, ALVOS
    MsgBox(
        "CALIBRACAO — " ALVOS.Length " pontos.`n`n"
        "Para cada um: leve o mouse ate' o alvo e aperte F9.`n"
        "O script NAO clica em nada agora, so' anota onde e'.`n`n"
        "⚠️ Deixe as duas janelas ja' abertas e do jeito que vao ficar:`n"
        "   · o AGENTE no monitor vertical`n"
        "   · o Chrome com a AdBatch Vertical 2 no horizontal`n`n"
        "Mover ou redimensionar uma janela depois disso obriga a recalibrar.",
        "Piloto AdBatch — calibrar")

    for alvo in ALVOS {
        chave := alvo[1], onde := alvo[2], desc := alvo[3]
        ToolTip "[" onde "]  aponte para:`n" desc "`n`n(F9 confirma · Esc cancela)"
        if !esperarF9()
            return ToolTip()
        MouseGetPos(&x, &y)
        IniWrite x, INI, "pontos", chave "_x"
        IniWrite y, INI, "pontos", chave "_y"
        ToolTip "gravado: " chave " = " x "," y
        Sleep 350
    }
    ToolTip()

    ; ⭐ a COR DO SLOT VAZIO — e' com ela que a ronda sabe se a imagem chegou.
    p := lerPonto("cr_slot1")
    cor := PixelGetColor(p.x, p.y)
    IniWrite cor, INI, "pontos", "cor_vazio"

    n := InputBox("Quantas abas do Chrome estao abertas com a AdBatch?",
                  "Piloto AdBatch", "w320 h130", "10")
    if (n.Result = "OK" && IsInteger(n.Value))
        IniWrite n.Value, INI, "config", "abas"

    MsgBox("Calibrado.`n`nCor do slot vazio: " cor "`n"
           "Abas: " IniRead(INI, "config", "abas", "?") "`n`n"
           "F8 = ensaio seco (recomendado da primeira vez)`n"
           "F10 = rodar de verdade", "Piloto AdBatch")
}

esperarF9() {
    global abortar
    abortar := false
    KeyWait "F9", "U"
    loop {
        if abortar
            return false
        if GetKeyState("F9", "P") {
            KeyWait "F9", "U"
            return true
        }
        if GetKeyState("Escape", "P")
            return false
        Sleep 40
    }
}

lerPonto(chave) {
    global INI
    x := IniRead(INI, "pontos", chave "_x", "")
    y := IniRead(INI, "pontos", chave "_y", "")
    if (x = "" || y = "")
        throw Error("ponto nao calibrado: " chave " — rode F9")
    return {x: Integer(x), y: Integer(y)}
}

clicar(chave, seco := false) {
    p := lerPonto(chave)
    if seco {
        MouseMove p.x, p.y, 2
        ToolTip "[seco] clicaria em " chave " (" p.x "," p.y ")"
        Sleep 260
        return
    }
    Click p.x, p.y
    Sleep 160
}

; =============================================================================
;  COPIA COM CONFERENCIA DE ASSINATURA
; =============================================================================
; ⛔⛔ ISTO E' O CORACAO DA SEGURANCA DO SCRIPT. Sem a conferencia, um clique
; que nao pegou deixa o clipboard com o conteudo do video ANTERIOR, e o lote
; sai com a REF de um video e as cenas de outro — erro que so' aparece no
; render, quando ja' se gastou credito.
copiar(chaves, assinatura, rotulo) {
    A_Clipboard := ""
    for c in chaves
        clicar(c)
    if !ClipWait(3, 0)
        throw Error(rotulo ": nada foi copiado em 3s — o clique nao pegou o botao")
    txt := A_Clipboard
    if !InStr(txt, assinatura)
        throw Error(rotulo ": o texto copiado nao contem " assinatura "`n`n"
                    "primeiros 120 caracteres:`n" SubStr(txt, 1, 120))
    return txt
}

; =============================================================================
;  O CICLO
; =============================================================================
rodar(seco) {
    global rodando
    rodando := true
    try
        rodarMiolo(seco)
    finally {
        rodando := false      ; ⛔ SEMPRE, inclusive se algo estourar no meio —
        ToolTip()             ;    senao o Esc fica sequestrado para sempre
    }
}

rodarMiolo(seco) {
    global abortar, linhas, INI, ARQ_LOG
    abortar := false
    linhas := []

    try {
        abas := Integer(IniRead(INI, "config", "abas", "0"))
        if (abas < 1)
            throw Error("numero de abas nao configurado — rode F9")
        tAgente := IniRead(INI, "config", "titulo_agente", "AGENTE")
        tChrome := IniRead(INI, "config", "titulo_chrome", "Google Flow")
    } catch as e {
        return MsgBox("Falta calibrar: " e.Message, "Piloto AdBatch", 16)
    }

    anotar((seco ? "ENSAIO SECO" : "EXECUCAO") " — " abas " aba(s)")

    loop abas {
        i := A_Index
        if abortar
            break
        ToolTip "aba " i "/" abas " — copiando do agente..."

        try {
            ; ---- 1. o agente entrega as tres partes -------------------------
            if !WinExist(tAgente)
                throw Error("nao achei a janela do agente (" tAgente ")")
            WinActivate tAgente
            WinWaitActive tAgente, , 3
            Sleep 250

            ref   := copiar(["ag_bloco_ref", "ag_copiar"], "REF 01:",     "BLOCO 0 (REF)")
            imgs  := copiar(["ag_imgs"],                   "IMAGE 01/02", "os 2 IMAGE")
            takes := copiar(["ag_takes"],                  "TAKE 01/02",  "os 2 TAKE")

            ; ⚠️ conferencia extra: os DOIS de cada par tem de estar la'. O
            ; botao diz "os 2", mas se o motor tiver gerado so' um, o lote sai
            ; pela metade e o slot 2 fica vazio para sempre.
            if !InStr(imgs, "IMAGE 02/02")
                throw Error("so' veio UM bloco IMAGE — falta o 02/02")
            if !InStr(takes, "TAKE 02/02")
                throw Error("so' veio UM bloco TAKE — falta o 02/02")

            roteiro := ref "`n`n" imgs "`n`n" takes
            anotar("aba " i ": roteiro montado, " StrLen(roteiro) " caracteres")

            ; ---- 2. o Chrome recebe -----------------------------------------
            if !WinExist(tChrome)
                throw Error("nao achei a janela do Chrome (" tChrome ")")
            WinActivate tChrome
            WinWaitActive tChrome, , 3
            Sleep 250
            irParaAba(i)

            if seco {
                clicar("cr_roteiro", true)
                clicar("cr_gerar", true)
                anotar("aba " i ": [seco] colaria e clicaria em Gerar")
            } else {
                clicar("cr_roteiro")
                Send "^a"                    ; limpa o que estiver la'
                Sleep 80
                A_Clipboard := roteiro
                ClipWait(2, 0)
                Send "^v"
                Sleep 700                    ; o app precisa reparsear o texto
                clicar("cr_gerar")
                Sleep 900
                anotar("aba " i ": colado e Gerar clicado")
            }

            ; ---- 3. o agente sorteia o proximo -------------------------------
            if !seco {
                WinActivate tAgente
                WinWaitActive tAgente, , 3
                Sleep 200
                clicar("ag_usado")
                Sleep 250
                Send "^r"                    ; SORTEAR VIDEO
                Sleep 900
            }

        } catch as e {
            anotar("aba " i ": PAROU — " e.Message)
            ToolTip()
            MsgBox("Parei na aba " i ".`n`n" e.Message
                   "`n`nNada foi colado nesta aba. Corrija e rode de novo.",
                   "Piloto AdBatch", 16)
            return
        }
    }
    ToolTip()

    if (seco) {
        anotar("ensaio seco terminou sem erro")
        return MsgBox("Ensaio seco OK — os " abas " ciclos rodariam.`n`n"
                      "F12 ve' o log. F10 roda de verdade.", "Piloto AdBatch")
    }

    ronda()
}

irParaAba(n) {
    ; ⚠️ Ctrl+1..8 vai direto; Ctrl+9 e' SEMPRE a ultima aba no Chrome, entao
    ; da nona em diante o jeito honesto e' contar a partir da primeira.
    if (n <= 8) {
        Send "^" n
    } else {
        Send "^1"
        Sleep 120
        loop n - 1 {
            Send "^{Tab}"
            Sleep 90
        }
    }
    Sleep 400
}

; =============================================================================
;  RONDA — volta em cada aba e regera o slot que ficou vazio
; =============================================================================
ronda() {
    global abortar, INI
    abas   := Integer(IniRead(INI, "config", "abas", "0"))
    corVaz := IniRead(INI, "pontos", "cor_vazio", "")
    maxR   := Integer(IniRead(INI, "config", "rondas", "6"))
    espera := Integer(IniRead(INI, "config", "espera_s", "45"))
    tChrome := IniRead(INI, "config", "titulo_chrome", "Google Flow")

    if (corVaz = "") {
        anotar("ronda pulada: cor do slot vazio nao calibrada")
        return MsgBox("Lotes disparados.`n`nA ronda foi pulada — a cor do slot "
                      "vazio nao esta' calibrada (F9).", "Piloto AdBatch")
    }

    loop maxR {
        r := A_Index
        if abortar
            break
        ToolTip "ronda " r "/" maxR " — esperando " espera "s antes de conferir"
        if !dormir(espera * 1000)
            break

        pendentes := 0
        WinActivate tChrome
        WinWaitActive tChrome, , 3
        loop abas {
            i := A_Index
            if abortar
                break
            irParaAba(i)
            vazios := 0
            for par in [["cr_slot1", "cr_reger1"], ["cr_slot2", "cr_reger2"]] {
                p := lerPonto(par[1])
                if (PixelGetColor(p.x, p.y) = corVaz) {
                    vazios++
                    ; ⚠️ so' regera a partir da SEGUNDA ronda: na primeira o
                    ; slot vazio provavelmente ainda esta' gerando, e clicar
                    ; REGERAR ali joga fora o trabalho em andamento e gasta
                    ; credito de novo.
                    if (r >= 2)
                        clicar(par[2])
                }
            }
            if vazios
                pendentes++
            anotar("ronda " r ", aba " i ": " vazios " slot(s) vazio(s)")
        }
        ToolTip()
        if (pendentes = 0) {
            anotar("ronda " r ": todas as abas com as duas imagens")
            return MsgBox("Pronto — as " abas " abas estao com as duas imagens.",
                          "Piloto AdBatch")
        }
    }
    MsgBox("Fim das rondas. Ainda ha' aba com slot vazio.`n`n"
           "F12 ve' o log — pode ser fila do Flow, credito, ou a cor do slot "
           "vazio calibrada em cima de um pixel que muda.", "Piloto AdBatch", 48)
}

dormir(ms) {
    global abortar
    fim := A_TickCount + ms
    while (A_TickCount < fim) {
        if abortar
            return false
        Sleep 100
    }
    return true
}

; =============================================================================
;  ARQ_LOG
; =============================================================================
anotar(txt) {
    global linhas, ARQ_LOG
    linha := FormatTime(, "HH:mm:ss") "  " txt
    linhas.Push(linha)
    try FileAppend linha "`n", ARQ_LOG, "UTF-8"
}

mostrarLog() {
    global linhas
    if !linhas.Length
        return MsgBox("Nada rodou ainda.", "Piloto AdBatch")
    txt := ""
    for l in linhas
        txt .= l "`n"
    MsgBox(txt, "Piloto AdBatch — log")
}
