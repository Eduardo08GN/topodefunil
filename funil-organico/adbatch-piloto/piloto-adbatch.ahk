#Requires AutoHotkey v2.0
#SingleInstance Force
SendMode "Event"          ; ⚠️ Event, nao Input: tkinter e Chrome perdem
SetKeyDelay 40, 40        ;    entrada sintetica rapida demais.
SetMouseDelay 50
CoordMode "Mouse", "Screen"
CoordMode "Pixel", "Screen"

/*
===============================================================================
 PILOTO ADBATCH — agente -> AdBatch Vertical 2, em N abas
===============================================================================

 POR CICLO:
   1. AGENTE  — Ctrl+0 copia o ROTEIRO INTEIRO (REF + 2 IMAGE + 2 TAKE)
   2. CHROME  — cola na caixa "Cole o roteiro inteiro" e clica em Gerar
   3. AGENTE  — Ctrl+4 marca como usado, Ctrl+R sorteia o proximo
   4. proxima aba

 ⭐⭐ SO' EXISTEM **DUAS** COORDENADAS OBRIGATORIAS, e as duas sao do Chrome.
 A primeira versao clicava nos botoes do agente e pedia ONZE pontos. Ao MEDIR,
 descobriu-se que o layout da janela do agente e' mais LARGO que o monitor
 vertical de 1080px: `COPIAR BLOCO` e `marcar como usado` ficam CORTADOS na
 borda, e a janela nao reflui — so' clipa. Nao havia coordenada valida ali.
 ⭐ A saida foi consertar a CAUSA: o `ui_agente.py` ganhou atalhos de teclado
 (Ctrl+0/1/2/3/4). Tecla nao tem coordenada, nao depende de onde a janela
 esta', e nao quebra quando o operador arrasta a janela.

 ⚠️⚠️ A ARMADILHA QUE SOBRA E' O CLIPBOARD MUDO: se o Ctrl+0 nao chegar na
 janela certa, a area de transferencia fica com o roteiro ANTERIOR e o lote
 sai com a REF de um video e as cenas de outro — sem aviso, aparecendo so' no
 render com o credito gasto. Por isso, a cada ciclo: limpa o clipboard, manda
 a tecla, espera, e CONFERE as CINCO partes, uma a uma.

 TECLAS
   F9   calibrar (6 pontos, todos no Chrome — 2 obrigatorios, 4 para a ronda)
   F8   ensaio seco — copia e confere, mas nao cola e nao clica em Gerar
   F10  rodar
   F12  log
   Esc  aborta (so' ativo enquanto roda)
===============================================================================
*/

INI := A_ScriptDir "\piloto-adbatch.ini"
ARQ_LOG := A_ScriptDir "\piloto-adbatch.log"
; ⭐⭐ ONDE A FASE 1 DEIXA O RECADO PARA A FASE 2.
; ⛔ Sem isto a Fase 2 nao existe: quando as imagens ficam prontas, o
; agente ja' sorteou outros dez videos e o roteiro daquela aba SUMIU.
; O take tem de ser guardado no momento em que passa pela mao do piloto.
DIR_ROT := A_ScriptDir "\roteiros"

ALVOS := [
    ["cr_roteiro", "a caixa 'Cole o roteiro inteiro...' (Roteiro Master)"],
    ["cr_gerar",   "o botao 'Gerar Lote com Referencia'"],
    ["cr_slot1",   "o MEIO do quadro cinza do SLOT 01"],
    ["cr_slot2",   "o MEIO do quadro cinza do SLOT 02"],
    ["cr_reger1",  "o botao REGERAR do SLOT 01"],
    ["cr_reger2",  "o botao REGERAR do SLOT 02"],
]

global abortar := false
global rodando := false
global linhas := []

; =============================================================================
;  CADENCIA HUMANA — ordem do operador, 2026-08-08
; =============================================================================
; ⛔⛔ O QUE MAIS DENUNCIA NAO E' O RITMO, E' A PRECISAO. Um humano nunca clica
; duas vezes no MESMO PIXEL, e o piloto clicava exatamente no ponto calibrado
; em 100% das vezes, dez abas seguidas. Ritmo constante e' suspeito; coordenada
; identica repetida e' impossivel. Por isso ha' DUAS aleatorizacoes aqui, e a
; do pixel importa mais que a do relogio.
; ⚠️ E o mouse passa a ANDAR ate' o alvo (`MouseMove` com velocidade sorteada)
; em vez de teleportar. Teleporte nao existe em maozinha nenhuma.

; ⭐⭐ RITMO — UM NUMERO SO' GOVERNA TODAS AS ESPERAS AJUSTAVEIS.
; Ordem do operador, 2026-08-09: *"pode acelerar o script? ele ta' lento. Pode
; reduzir 2 segundos no tempo entre as interacoes."*
; ⚠️ Espalhar a aceleracao em quinze numeros magicos seria impossivel de afinar
; depois. Aqui e' um fator: 1.00 e' o ritmo original, 0.05 e' o atual.
; ⭐ MEDIDO, rodando as 13 esperas de uma aba isoladas:
;     RITMO 0.55  ->  ~2.480 ms   (o ajuste de 2026-08-09)
;     RITMO 0.20  ->   1.063 ms   (medido)
;     RITMO 0.10  ->     515 ms   (medido)
;     RITMO 0.05  ->     281 ms   (3a rodada, mesmo dia)
; A base sem fator soma 4.710 ms. O segundo corte tirou ~1,4 s por aba, que
; e' o que o operador pediu: *"o tempo entre as interacoes diminua 1 segundo
; e meio"*.
; ⚠⚠ E O PISO DESCE JUNTO A CADA CORTE, senao o ganho se paga com o TREMOR:
; quando base*RITMO cai abaixo do piso, a pausa vira CONSTANTE e a
; aleatoriedade daquela espera morre. 40 -> 25 -> 15 -> 8 ms, acompanhando
; 0.55 -> 0.20 -> 0.10 -> 0.05. A 0.05 restam 3 das 13 no piso.
; ⛔⛔ E AQUI ACABA O QUE O RITMO CONSEGUE FAZER. O SetKeyDelay 40 e o
; SetMouseDelay 50 (topo do arquivo) sao FIXOS por tecla e por clique, fora
; do fator — num ciclo com ~8 teclas e 2 cliques eles ja' somam mais que as 13
; pausas inteiras. Cortar o RITMO de novo vai render cada vez menos tempo
; real, e mexer nos delays de entrada e' outro problema: abaixo deles o
; tkinter e o Chrome DESCARTAM a entrada sintetica, e a tecla se perde em
; silencio — que e' o pior modo de falha deste script.
; ⛔ O QUE O FATOR **NAO** TOCA, e nao e' esquecimento:
;   · o `Sleep 900 + Random(0,700)` depois do Ctrl+V — o app precisa reparsear
;     o roteiro antes de o Gerar valer, e essa espera e' funcao, nao cadencia;
;   · o `respirar()` — a pausa longa e rara e' justamente o que quebra o padrao
;     de maquina, e encolhe-la desfaria o pedido anterior do operador;
;   · o espalhamento `esp` de cada pausa — o tremor continua o mesmo em %.
global RITMO := 0.05

pausa(base, esp := 35) {
    global RITMO
    ; base em ms, `esp` = espalhamento em % para cada lado.
    ; ⚠️ piso de 8ms: sorteio que devolve valor perto de zero volta a ser
    ; ritmo de maquina, so' que rapido. Era 40 ate' o RITMO cair para 0.20 —
    ; ver a nota do RITMO acima.
    d := Round(base * RITMO) * (100 + Random(-esp, esp)) // 100
    Sleep (d < 8 ? 8 : d)
}

respirar() {
    ; ⭐ A pausa longa e RARA — a pessoa que para para olhar a tela. Um ritmo
    ; uniforme, mesmo com ruido, ainda e' uniforme: o que quebra o padrao e' a
    ; excecao ocasional, nao o tremor constante.
    if (Random(1, 100) <= 22)
        Sleep Random(1200, 3400)
}

F9::  calibrar()
F10:: rodar(false)
F8::  rodar(true)
F12:: mostrarLog()

#HotIf rodando          ; ⛔ o Esc so' existe ENQUANTO o ciclo roda, senao o
Esc:: {                 ;    script sequestra o Esc do Windows inteiro
    global abortar
    abortar := true
    ToolTip "ABORTANDO..."
    SetTimer () => ToolTip(), -1200
}
#HotIf

; =============================================================================
calibrar() {
    global rodando
    rodando := true
    try
        calibrarMiolo()
    finally
        rodando := false
}

calibrarMiolo() {
    global INI, ALVOS
    MsgBox("CALIBRACAO — " ALVOS.Length " pontos, todos no CHROME.`n`n"
           "Para cada um: leve o mouse ate' o alvo e aperte F9.`n"
           "O script nao clica em nada agora.`n`n"
           "⭐ Os botoes do AGENTE nao precisam de calibracao: o piloto usa os "
           "atalhos de teclado (Ctrl+0, Ctrl+4, Ctrl+R).", "Piloto AdBatch")

    for alvo in ALVOS {
        ToolTip "[CHROME] aponte para:`n" alvo[2] "`n`n(F9 confirma · Esc cancela)"
        if !esperarF9()
            return ToolTip()
        MouseGetPos(&x, &y)
        IniWrite x, INI, "pontos", alvo[1] "_x"
        IniWrite y, INI, "pontos", alvo[1] "_y"
        ToolTip "gravado: " alvo[1] " = " x "," y
        Sleep 350
    }
    ToolTip()

    p := lerPonto("cr_slot1")
    cor := PixelGetColor(p.x, p.y)
    IniWrite cor, INI, "pontos", "cor_vazio"

    n := InputBox("Quantas abas do Chrome estao abertas com a AdBatch?",
                  "Piloto AdBatch", "w320 h130", "10")
    if (n.Result = "OK" && IsInteger(n.Value))
        IniWrite n.Value, INI, "config", "abas"

    MsgBox("Calibrado.`n`nCor do slot vazio: " cor
           "`nAbas: " IniRead(INI, "config", "abas", "?")
           "`n`nF8 = ensaio seco · F10 = rodar", "Piloto AdBatch")
}

esperarF9() {
    KeyWait "F9", "U"
    loop {
        if GetKeyState("Escape", "P")
            return false
        if GetKeyState("F9", "P") {
            KeyWait "F9", "U"
            return true
        }
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
    ; ⛔ NUNCA no mesmo pixel: ±6px em volta do ponto calibrado. Os alvos sao
    ; botoes e caixas de texto — 6px cabe folgado em qualquer um deles, e e'
    ; suficiente para a sequencia de cliques nao ser identica.
    x := p.x + Random(-6, 6)
    y := p.y + Random(-6, 6)
    if seco {
        MouseMove x, y, Random(8, 22)
        ToolTip "[seco] clicaria em " chave
        pausa(280)
        return
    }
    ; ⚠️ o mouse ANDA (velocidade 8-22; quanto maior, mais devagar) e so'
    ; depois clica — com um respiro curto no meio, como quem mira.
    MouseMove x, y, Random(8, 22)
    pausa(120, 50)
    Click
    pausa(180)
}

; =============================================================================
;  O ROTEIRO, PELO ATALHO — com conferencia das cinco partes
; =============================================================================
; =============================================================================
;  RECORTE DOS TAKES — o que a Fase 2 vai colar em cada imagem
; =============================================================================
; ⚠️ O corte e' pelo ROTULO, nao por contagem de linhas: o TAKE tem numero
; variavel de linhas (a fala muda de tamanho) e cortar por posicao entregaria
; meio bloco. Cada take vai do proprio rotulo ate' o rotulo seguinte.
recortarTake(roteiro, rotulo) {
    i := InStr(roteiro, rotulo)
    if !i
        return ""
    resto := SubStr(roteiro, i)
    ; o proximo rotulo TAKE, se houver, fecha o bloco
    j := InStr(resto, "TAKE ", , 2)
    return Trim(j ? SubStr(resto, 1, j - 1) : resto, " `t`r`n")
}

gravarRoteiro(aba, roteiro) {
    global DIR_ROT
    if !DirExist(DIR_ROT)
        DirCreate DIR_ROT
    t1 := recortarTake(roteiro, "TAKE 01/02")
    t2 := recortarTake(roteiro, "TAKE 02/02")
    if (t1 = "" || t2 = "")
        throw Error("nao consegui recortar os dois TAKE do roteiro da aba " aba)
    ; ⚠️ um arquivo por take, com o numero da aba no nome: e' assim que a Fase 2
    ; sabe qual take pertence a qual imagem sem depender de ordem de nada.
    for par in [[1, t1], [2, t2]] {
        arq := Format("{1}\\aba{2:02}-take{3}.txt", DIR_ROT, aba, par[1])
        if FileExist(arq)
            FileDelete arq
        FileAppend par[2], arq, "UTF-8"
    }
}

pegarRoteiro(tAgente) {
    if !WinExist(tAgente)
        throw Error("nao achei a janela do agente (titulo comeca com '" tAgente "')")
    WinActivate tAgente
    if !WinWaitActive(tAgente, , 4)
        throw Error("a janela do agente nao veio para a frente")
    pausa(350)

    A_Clipboard := ""
    Send "^0"                       ; copiar_tudo() do ui_agente
    if !ClipWait(4, 0)
        throw Error("Ctrl+0 nao copiou nada.`n`nO .exe deste agente foi "
                    "recompilado depois de 2026-08-08? Os atalhos so' existem "
                    "nas versoes novas.")
    txt := A_Clipboard

    ; ⛔ AS CINCO PARTES, uma a uma. Procurar so' por `IMAGE` nao basta: se
    ; vier apenas o 01/02, o lote sai pela metade e o slot 2 fica vazio para
    ; sempre — e o video so' seria descoberto quebrado depois do render.
    for parte in ["REF 01:", "IMAGE 01/02", "IMAGE 02/02", "TAKE 01/02", "TAKE 02/02"] {
        if !InStr(txt, parte)
            throw Error("o roteiro copiado nao tem " parte "`n`n"
                        "primeiros 150 caracteres:`n" SubStr(txt, 1, 150))
    }
    return txt
}

; =============================================================================
rodar(seco) {
    global rodando
    rodando := true
    try
        rodarMiolo(seco)
    finally {
        rodando := false     ; ⛔ SEMPRE — senao o Esc fica sequestrado
        ToolTip()
    }
}

rodarMiolo(seco) {
    global abortar, linhas, INI
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
        ToolTip "aba " i "/" abas " — pegando o roteiro no agente..."
        try {
            roteiro := pegarRoteiro(tAgente)
            ; ⭐ GRAVA ANTES DE COLAR. Se gravasse depois, uma falha no meio do
            ; caminho deixaria a aba com lote disparado e sem take guardado — e
            ; a Fase 2 nao teria o que animar naquela imagem.
            if !seco
                gravarRoteiro(i, roteiro)
            anotar("aba " i ": roteiro OK, " StrLen(roteiro) " caracteres"
                   (seco ? " [seco: nao gravei]" : ", takes gravados"))

            if !WinExist(tChrome)
                throw Error("nao achei a janela do Chrome (" tChrome ")")
            WinActivate tChrome
            WinWaitActive tChrome, , 4
            pausa(300)
            irParaAba(i)

            if seco {
                clicar("cr_roteiro", true)
                clicar("cr_gerar", true)
                anotar("aba " i ": [seco] colaria e clicaria em Gerar")
            } else {
                clicar("cr_roteiro")
                pausa(220, 60)
                Send "^a"
                pausa(140, 60)
                A_Clipboard := roteiro
                ClipWait(2, 0)
                Send "^v"
                ; ⚠️ ESTA e' a unica espera que NAO deve encolher: o app
                ; precisa reparsear o roteiro colado antes de o Gerar valer.
                ; Aqui o sorteio so' ADICIONA tempo, nunca tira.
                Sleep 900 + Random(0, 700)
                respirar()
                clicar("cr_gerar")
                pausa(1000)
                anotar("aba " i ": colado e Gerar clicado")

                WinActivate tAgente
                WinWaitActive tAgente, , 4
                pausa(250)
                Send "^4"                 ; marcar como usado
                pausa(300)
                Send "^r"                 ; sortear o proximo
                pausa(1100)
                respirar()                ; entre uma aba e outra
            }
        } catch as e {
            anotar("aba " i ": PAROU — " e.Message)
            ToolTip()
            MsgBox("Parei na aba " i ".`n`n" e.Message
                   "`n`nNada foi colado nesta aba.", "Piloto AdBatch", 16)
            return
        }
    }
    ToolTip()

    if seco {
        anotar("ensaio seco terminou sem erro")
        return MsgBox("Ensaio seco OK — os " abas " ciclos rodariam.`n`n"
                      "⚠️ Ele COPIOU de verdade do agente (inofensivo) e "
                      "conferiu as cinco partes. So' nao colou nem gerou."
                      "`n`nF12 ve' o log. F10 roda de verdade.", "Piloto AdBatch")
    }
    ronda()
}

irParaAba(n) {
    ; ⚠️ Ctrl+9 no Chrome vai para a ULTIMA aba, nao para a nona.
    if (n <= 8) {
        Send "^" n
    } else {
        Send "^1"
        pausa(150, 50)
        loop n - 1 {
            Send "^{Tab}"
            pausa(110, 60)
        }
    }
    pausa(450)
}

; =============================================================================
ronda() {
    global abortar, INI
    abas    := Integer(IniRead(INI, "config", "abas", "0"))
    corVaz  := IniRead(INI, "pontos", "cor_vazio", "")
    maxR    := Integer(IniRead(INI, "config", "rondas", "6"))
    espera  := Integer(IniRead(INI, "config", "espera_s", "15"))
    tChrome := IniRead(INI, "config", "titulo_chrome", "Google Flow")

    if (corVaz = "") {
        anotar("ronda pulada: cor do slot vazio nao calibrada")
        return MsgBox("Lotes disparados. Ronda pulada (falta calibrar a cor).",
                      "Piloto AdBatch")
    }

    loop maxR {
        r := A_Index
        if abortar
            break
        ToolTip "ronda " r "/" maxR " — esperando " espera "s"
        ; ⚠️ ±18% na espera da ronda: um alarme que dispara a cada 45s
        ; cravados por seis rondas e' relogio, nao gente.
        if !dormir(espera * 1000 * (100 + Random(-18, 18)) // 100)
            break

        pendentes := 0
        WinActivate tChrome
        WinWaitActive tChrome, , 4
        loop abas {
            i := A_Index
            if abortar
                break
            irParaAba(i)
            pausa(400, 45)
            vazios := 0
            for par in [["cr_slot1", "cr_reger1"], ["cr_slot2", "cr_reger2"]] {
                p := lerPonto(par[1])
                if (PixelGetColor(p.x, p.y) = corVaz) {
                    vazios++
                    ; ⚠️ so' regera da SEGUNDA ronda em diante: na primeira o
                    ; slot vazio provavelmente ainda esta' gerando, e clicar
                    ; REGERAR ali joga fora o trabalho e gasta credito de novo.
                    if (r >= 2)
                        clicar(par[2])
                }
            }
            if vazios
                pendentes++
            anotar("ronda " r ", aba " i ": " vazios " vazio(s)")
        }
        ToolTip()
        if (pendentes = 0) {
            anotar("ronda " r ": tudo cheio")
            return MsgBox("Pronto — as " abas " abas com as duas imagens.",
                          "Piloto AdBatch")
        }
    }
    MsgBox("Fim das rondas, ainda ha' slot vazio. F12 ve' o log.",
           "Piloto AdBatch", 48)
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
