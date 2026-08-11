#Requires AutoHotkey v2.0
#SingleInstance Force
SendMode "Event"          ; ⚠️ Event, nao Input: tkinter e Chrome perdem
                          ;    entrada sintetica rapida demais.
; ⛔⛔ 2026-08-10, 4a rodada de aceleracao. O operador pediu mais velocidade
; SEM encurtar a ronda de 15s — e o RITMO ja' estava no limite (ver a nota
; dele abaixo). O que sobrou de gordura sao ESTES DOIS, que sao FIXOS por
; tecla e por clique e ficam FORA do fator: num ciclo com ~8 teclas e 2
; cliques eles somavam mais que as 13 pausas inteiras.
;     SetKeyDelay    40 -> 22 ms   (por tecla, antes E depois)
;     SetMouseDelay  50 -> 28 ms   (por acao de mouse)
; ⚠⚠⚠ E ESTE E' O UNICO AJUSTE DE VELOCIDADE COM RISCO DE FALHA SILENCIOSA.
; Abaixo de um certo limiar o tkinter e o Chrome DESCARTAM a entrada
; sintetica: a tecla nao chega, o clipboard fica com o roteiro ANTERIOR, e o
; lote sai com a REF de um video e as cenas de outro — sem aviso, aparecendo
; so' no render com o credito gasto. A conferencia das cinco partes (ver a
; nota do CLIPBOARD MUDO) e' a rede que pega isso, e o F8 existe para
; exercita-la de graca.
; ⛔ ORDEM PARA QUEM MEXER AQUI DE NOVO: rode o F8 (ensaio seco) UMA vez
; depois de baixar estes numeros. Ele copia e confere sem colar e sem gastar
; credito. Se o F8 acusar parte faltando, SUBA os dois de volta.
SetKeyDelay 22, 22
SetMouseDelay 28
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
; ⭐ o HANDLE da janela do AdBatch que o F3 montou. Depois da montagem a
; sessao passa a ter TRES janelas com o MESMO titulo (o nome do perfil no
; Dolphin); sem guardar isto, o operador teria de adivinhar qual escolher.
global gBancada := 0
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
; ⛔⛔ E AQUI ACABA O QUE O RITMO CONSEGUE FAZER. Os delays de ENTRADA (topo do
; arquivo) sao FIXOS por tecla e por clique, fora do fator — num ciclo com ~8
; teclas e 2 cliques eles ja' somam mais que as 13 pausas inteiras. Cortar o
; RITMO de novo rende cada vez menos tempo real.
; ⚠️ Na 4a rodada de aceleracao (2026-08-10) foi exatamente ali que se foi
; buscar o tempo: SetKeyDelay 40 -> 22 e SetMouseDelay 50 -> 28, mais a
; velocidade do MouseMove de 8-22 para 4-11. ⛔ Esse e' o unico ajuste de
; velocidade deste script COM RISCO DE FALHA SILENCIOSA — leia a nota do topo
; antes de baixar de novo, e rode o F8.
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

; =============================================================================
;  ⭐⭐ AS SESSOES — 2026-08-11
; =============================================================================
; ⛔ O PROBLEMA QUE ISTO RESOLVE, e a causa nao era o que parecia. O operador:
; *"quando aperto F10 ele sempre abre minha sessao do Google Flow logada no meu
; login principal; preciso que abra tb a janela dessas outras sessoes"*.
;
; ⚠️ NAO ERA PREFERENCIA DO AHK. O script procurava a janela pelo titulo
; `Google Flow` (INI `config/titulo_chrome`), e as janelas do Dolphin NAO TEM
; esse texto no titulo — elas se chamam pelo NOME DO PERFIL. Medido na maquina
; do operador:
;     chrome.exe .... "Google Flow - bladerunner2049v2 - Google Chrome"
;     anty.exe ...... "CTA - O2 Ricardo"
;     anty.exe ...... "CTA - 03 Neusa"
; A busca so' casava com a primeira. Ele nunca "preferia" o principal: as
; outras eram invisiveis para ele.
;
; ⭐ O DISCRIMINANTE E' O EXECUTAVEL, nao o titulo: o Dolphin roda `anty.exe`
; (um processo por perfil aberto) e o Chrome roda `chrome.exe`. Titulo muda
; quando se troca de aba; executavel nao.
;
; ⛔⛔ E POR ISSO O ALVO PASSOU A SER O HWND, e nao mais uma string. O
; `irParaAba()` troca a aba, a aba MUDA O TITULO DA JANELA — um `WinActivate`
; por titulo no meio do laco podia deixar de achar a mesma janela que ativou no
; comeco. Com o handle isso nao tem como acontecer.
;
; ⚠️ SO' JANELAS JA' ABERTAS — decisao do operador. A API local do Dolphin
; existe (localhost:3001 responde) e daria para dar START num perfil parado,
; mas exigiria o token dele gravado em arquivo. Perfil fechado aparece na lista
; como FECHADA, para ele saber que precisa abrir — some da lista e' pior, porque
; parece que o script deixou de enxergar.

SESSOES_ESPERADAS := "CTA - 01,CTA - O2 Ricardo,CTA - 03 Neusa,CTA - 04 Isis"

; ⛔ Devolve [{hwnd, titulo, tipo}] de tudo que serve como alvo AGORA.
listarSessoes() {
    global INI
    achadas := []
    ; as do Dolphin: um processo `anty.exe` por perfil aberto
    for hwnd in WinGetList("ahk_exe anty.exe") {
        t := WinGetTitle(hwnd)
        if (t != "")
            achadas.Push({hwnd: hwnd, titulo: t, tipo: "Dolphin"})
    }
    ; a principal: Chrome com a AdBatch aberta
    tC := IniRead(INI, "config", "titulo_chrome", "Google Flow")
    for hwnd in WinGetList("ahk_exe chrome.exe") {
        t := WinGetTitle(hwnd)
        if (t != "" && InStr(t, tC))
            achadas.Push({hwnd: hwnd, titulo: t, tipo: "Chrome"})
    }
    return achadas
}

; ⛔ O seletor. Devolve o HWND escolhido, ou 0 se o operador desistir.
escolherSessao() {
    global INI, SESSOES_ESPERADAS, gBancada
    lista := listarSessoes()
    if (lista.Length = 0) {
        MsgBox("Nenhuma sessao aberta.`n`nAbra o perfil no Dolphin (ou a aba "
               "da AdBatch no Chrome) e rode de novo.", "Piloto AdBatch", 48)
        return 0
    }

    txt := "Em qual sessao rodar?`n`n"
    padrao := "1"
    for i, s in lista {
        marca := (s.hwnd = gBancada) ? "   <-- montada pelo F3" : ""
        if (s.hwnd = gBancada)
            padrao := String(i)
        txt .= i ". [" s.tipo "] " s.titulo marca "`n"
    }

    ; ⚠️ o que esta' FECHADO tambem aparece — sumir da lista parece defeito do
    ; script, e o operador ficaria procurando por que a sessao "desapareceu".
    esperadas := StrSplit(IniRead(INI, "sessoes", "esperadas",
                                  SESSOES_ESPERADAS), ",")
    fechadas := []
    for nome in esperadas {
        nome := Trim(nome)
        if (nome = "")
            continue
        aberta := false
        for s in lista
            if InStr(s.titulo, nome)
                aberta := true
        if !aberta
            fechadas.Push(nome)
    }
    if (fechadas.Length > 0) {
        txt .= "`nfechadas (abra no Dolphin para usar):`n"
        for nome in fechadas
            txt .= "   - " nome "`n"
    }

    ; ⚠️ o campo ja' vem preenchido com a janela que o F3 montou:
    ; ela e' a que o operador quer em quase todo caso, e digitar o numero
    ; errado aqui roda o piloto na BANCADA ERRADA — que e' o unico jeito de
    ; este seletor causar dano.
    r := InputBox(txt, "Piloto AdBatch — sessao", "w460 h" (190 + 18 * (lista.Length + fechadas.Length)), padrao)
    if (r.Result != "OK")
        return 0
    if !IsInteger(r.Value) || Integer(r.Value) < 1 || Integer(r.Value) > lista.Length {
        MsgBox("Numero fora da lista.", "Piloto AdBatch", 48)
        return 0
    }
    return lista[Integer(r.Value)].hwnd
}

; ⛔⛔ A GEOMETRIA — a trava que impede o pior desfecho deste script.
; Os pontos calibrados sao coordenadas de TELA (`CoordMode "Mouse", "Screen"`).
; Se a janela escolhida nao estiver do mesmo tamanho e no mesmo lugar da janela
; em que o F9 calibrou, TODO clique cai fora do alvo — e o script segue rodando,
; clicando em lugar nenhum e gastando credito, sem erro nenhum na tela.
; ⭐ Duas defesas, nesta ordem: MAXIMIZA a janela (e' o que torna as geometrias
; iguais na pratica) e depois COMPARA com a geometria gravada na calibracao. Se
; diferir, ABORTA — clicar no escuro e' pior que nao rodar.
prepararJanela(hwnd) {
    global INI
    if !WinExist("ahk_id " hwnd)
        throw Error("a janela escolhida foi fechada")
    if (WinGetMinMax("ahk_id " hwnd) != 1)
        WinMaximize "ahk_id " hwnd
    WinActivate "ahk_id " hwnd
    if !WinWaitActive("ahk_id " hwnd, , 4)
        throw Error("nao consegui ativar a janela escolhida")
    Sleep 250

    WinGetPos(&x, &y, &w, &h, "ahk_id " hwnd)
    cw := IniRead(INI, "pontos", "calib_w", "")
    ch := IniRead(INI, "pontos", "calib_h", "")
    ; ⚠️ INI ANTERIOR A ESTA TRAVA nao tem a geometria gravada. Obrigar uma
    ; recalibracao inteira dos seis pontos por causa disso seria punir o
    ; operador por uma mudanca minha — e ele PODE ja' ter calibrado numa
    ; janela do mesmo tamanho desta. Entao a decisao passa a ser dele, com a
    ; informacao na tela: adotar esta geometria, ou recalibrar.
    ; ⛔ O que NAO se faz e' adotar em silencio: se os pontos vieram de uma
    ; janela de outro tamanho, todo clique cai fora e o credito vai embora
    ; sem uma linha de erro.
    if (cw = "" || ch = "") {
        r := MsgBox("Esta calibracao e' anterior a trava de geometria e nao "
                    "sabe em que tamanho de janela foi feita.`n`n"
                    "A janela escolhida esta' " w "x" h ".`n`n"
                    "SIM  = adotar este tamanho como o da calibracao`n"
                    "       (so' clique SIM se os 6 pontos foram apontados "
                    "numa janela deste mesmo tamanho)`n`n"
                    "NAO  = cancelar e rodar o F9 aqui",
                    "Piloto AdBatch — geometria", 4 + 48)
        if (r != "Yes")
            throw Error("cancelado — rode o F9 nesta janela")
        IniWrite w, INI, "pontos", "calib_w"
        IniWrite h, INI, "pontos", "calib_h"
        IniWrite WinGetTitle("ahk_id " hwnd), INI, "pontos", "calib_janela"
        return
    }
    if (Abs(w - Integer(cw)) > 8 || Abs(h - Integer(ch)) > 8)
        throw Error("a janela esta' " w "x" h " e a calibracao foi feita em "
                    cw "x" ch ". Os cliques cairiam fora do alvo. "
                    "Maximize a janela nesta mesma tela, ou rode o F9 aqui.")
}

; =============================================================================
;  ⭐⭐ F3 — MONTAR A BANCADA DA SESSAO (2026-08-11)
; =============================================================================
; ⛔ Encomenda do operador: *"pra poupar o trabalho de eu ficar montando essa
; estrutura de telas e janelas pra cada sessao manualmente, via ctrl+c ctrl+v,
; ctrl+t, haveria como implementar um trigger tipo F3 que abrisse um popup para
; input de URL e montasse a estrutura automaticamente?"*
;
; A ESTRUTURA, ditada por ele:
;   janela 1 ... N abas na ferramenta ADBATCH VERTICAL 2 do projeto X (N e' o
;                mesmo `config/abas` que o F10 percorre — os dois numeros TEM de
;                ser o mesmo, senao o F10 varre aba que nao existe)
;   janela 2 ... M abas no DASHBOARD do projeto X  +  1 aba no MONTADOR
;
; ⭐⭐ O QUE FOI MEDIDO NAS URLS DELE, e e' isto que torna a automacao possivel:
;   AdBatch  .... tool/d882542c-72bd-4f73-81e1-472aa705775f   CONSTANTE
;   Montador .... tool/0a949867-f37f-4808-b178-4478edc7b5ad   CONSTANTE
;   project  .... 91c8bb90-... / c82f5efd-...                 VARIA por sessao
; O operador confirmou que o projeto e' diferente DE PROPOSITO em cada sessao:
; *"pra nao sobrecarregar um projeto com muitas midias e atrapalhar o refresh"*.
;
; ⛔ E POR ISSO NAO SE CONCATENA O QUE FOI COLADO. As urls dele vieram com o
; segmento de idioma INCONSISTENTE — o Montador da CTA-03 veio `/fx/tools/` e
; todo o resto `/fx/pt/tools/`. O script EXTRAI o id do projeto e reconstroi as
; tres urls de um molde unico; emendar texto colado propagaria a inconsistencia.
;
; ⚠️ AS DUAS JANELAS NASCEM NOVAS (Ctrl+N), e isso nao e' detalhe: o F10 faz
; `Ctrl+1` para ir a' primeira aba e conta a partir dela. Se as abas fossem
; abertas na janela que ja' estava aberta, a aba 1 seria uma antiga e o piloto
; varreria a bancada errada. Janela nova nasce com UMA aba em branco, que vira a
; primeira do lote.

FLOW_BASE     := "https://labs.google/fx/pt/tools/flow/project/"
TOOL_ADBATCH  := "d882542c-72bd-4f73-81e1-472aa705775f"
TOOL_MONTADOR := "0a949867-f37f-4808-b178-4478edc7b5ad"

; ⛔ Aceita QUALQUER url do Flow que carregue um id de projeto — dashboard,
; AdBatch ou Montador. O operador nao deveria ter de saber qual delas colar.
idDoProjeto(url) {
    if RegExMatch(url, "i)project/([0-9a-fA-F\-]{30,40})", &m)
        return m[1]
    return ""
}

urlsDaBancada(pid) {
    global FLOW_BASE, TOOL_ADBATCH, TOOL_MONTADOR
    return {adbatch:  FLOW_BASE pid "/tool/" TOOL_ADBATCH,
            dash:     FLOW_BASE pid,
            montador: FLOW_BASE pid "/tool/" TOOL_MONTADOR}
}

; ⛔ Abre uma aba e navega. `Ctrl+L` antes de digitar: a aba nova ja' nasce com
; a barra de endereco focada, mas isso e' COMPORTAMENTO e nao contrato — e uma
; aba que receba o texto no lugar errado vira uma BUSCA, nao uma navegacao.
abrirAba(url, nova := true) {
    if nova {
        Send "^t"
        pausa(700, 180)
    }
    Send "^l"
    pausa(260, 90)
    SendText url
    pausa(220, 80)
    Send "{Enter}"
    pausa(1400, 350)
}

montarBancada() {
    global rodando, abortar
    if rodando
        return
    rodando := true
    abortar := false
    try
        montarBancadaMiolo()
    finally {
        rodando := false
        ToolTip()
    }
}

montarBancadaMiolo() {
    global INI, abortar, gBancada

    nAd   := Integer(IniRead(INI, "config", "abas", "10"))
    nDash := Integer(IniRead(INI, "config", "abas_dashboard", "5"))

    g := Gui("+AlwaysOnTop -MinimizeBox", "Montar bancada da sessao")
    g.SetFont("s10", "Segoe UI")
    g.AddText("w540", "Cole QUALQUER url do Flow do projeto desta sessao (dashboard, AdBatch ou Montador).")
    g.SetFont("s9", "Consolas")
    eUrl := g.AddEdit("w540 r1")
    g.SetFont("s9", "Segoe UI")
    g.AddText("w540 r4 cGray", "Vai montar DUAS janelas novas nesta sessao:`n   janela 1 — " nAd " abas no AdBatch Vertical 2`n   janela 2 — " nDash " abas no dashboard + 1 aba no Montador Vertical 2`nO F10 continua sendo o gatilho da geracao.")
    prev := g.AddText("w540 r3 cSilver", "")
    bOk := g.AddButton("w130 Default", "Montar")
    g.AddButton("x+10 w130", "Cancelar").OnEvent("Click", (*) => g.Destroy())

    ; ⭐ O PREVIEW E' A DEFESA CONTRA ABRIR 16 ABAS ERRADAS: ele mostra as urls
    ; DERIVADAS antes de qualquer clique. Url errada se ve' aqui, e nao depois
    ; de dezesseis abas abertas na sessao errada.
    atualizar(*) {
        pid := idDoProjeto(eUrl.Value)
        if (pid = "") {
            prev.Value := (Trim(eUrl.Value) = "") ? "" : "url sem id de projeto — nao vou abrir nada"
            return
        }
        u := urlsDaBancada(pid)
        prev.Value := "projeto: " pid "`nAdBatch:  " u.adbatch "`nMontador: " u.montador
    }
    eUrl.OnEvent("Change", atualizar)

    escolhido := ""
    bOk.OnEvent("Click", (*) => (escolhido := eUrl.Value, g.Destroy()))
    g.OnEvent("Close", (*) => g.Destroy())
    g.Show()
    WinWaitClose "ahk_id " g.Hwnd

    if (Trim(escolhido) = "")
        return
    pid := idDoProjeto(escolhido)
    if (pid = "")
        return MsgBox("Nao achei um id de projeto nessa url.", "Piloto AdBatch", 48)
    u := urlsDaBancada(pid)

    hBase := escolherSessao()
    if (hBase = 0)
        return
    if !WinExist("ahk_id " hBase)
        return MsgBox("a janela escolhida sumiu", "Piloto AdBatch", 16)
    WinActivate "ahk_id " hBase
    if !WinWaitActive("ahk_id " hBase, , 4)
        return MsgBox("nao consegui ativar a sessao", "Piloto AdBatch", 16)

    anotar("montando bancada — projeto " pid " em " WinGetTitle("ahk_id " hBase))

    hJan1 := novaJanela(hBase)
    if (hJan1 = 0)
        return MsgBox("nao consegui abrir a janela 1", "Piloto AdBatch", 16)
    abrirAba(u.adbatch, false)
    loop nAd - 1 {
        if abortar
            break
        ToolTip "janela 1 — aba " (A_Index + 1) "/" nAd
        abrirAba(u.adbatch)
    }

    hJan2 := 0
    if !abortar {
        hJan2 := novaJanela(hJan1)
        if (hJan2 = 0)
            return MsgBox("nao consegui abrir a janela 2", "Piloto AdBatch", 16)
        abrirAba(u.dash, false)
        loop nDash - 1 {
            if abortar
                break
            ToolTip "janela 2 — dashboard " (A_Index + 1) "/" nDash
            abrirAba(u.dash)
        }
        if !abortar {
            ToolTip "janela 2 — montador"
            abrirAba(u.montador)
        }
        WinMaximize "ahk_id " hJan2
    }

    ; ⛔ MAXIMIZA AS DUAS. A trava de geometria do F10 compara o tamanho da
    ; janela com o da calibracao; uma janela nova que nascesse restaurada faria
    ; o F10 seguinte ABORTAR, e o operador acharia que a montagem quebrou algo.
    WinMaximize "ahk_id " hJan1
    WinActivate "ahk_id " hJan1
    ToolTip()

    ; ⭐ GUARDA QUAL JANELA E' A DO ADBATCH. Depois do F3 a sessao passa a ter
    ; TRES janelas com o MESMO titulo (o nome do perfil no Dolphin), e sem isto
    ; o operador teria de adivinhar qual escolher no F10.
    gBancada := hJan1
    anotar("bancada montada: janela1=" hJan1 " (" nAd " abas AdBatch), janela2=" hJan2)
    MsgBox("Bancada montada.`n`nJanela 1: " nAd " abas do AdBatch`nJanela 2: " nDash " abas do dashboard + 1 Montador`n`nNo F10 ela aparece marcada como montada pelo F3.", "Piloto AdBatch")
}

; ⛔ Abre uma janela nova a partir de uma existente e devolve o HANDLE dela.
; ⚠️ Compara a LISTA de janelas antes e depois em vez de confiar em `WinExist("A")`:
; a janela nova pode demorar a receber o foco, e pegar a ativa cedo demais
; devolveria a janela de ORIGEM — as dezesseis abas iriam para o lugar errado.
novaJanela(hOrigem) {
    antes := Map()
    for h in WinGetList("ahk_exe anty.exe")
        antes[h] := true
    for h in WinGetList("ahk_exe chrome.exe")
        antes[h] := true

    WinActivate "ahk_id " hOrigem
    WinWaitActive "ahk_id " hOrigem, , 4
    Send "^n"

    fim := A_TickCount + 8000
    while (A_TickCount < fim) {
        Sleep 200
        for exe in ["ahk_exe anty.exe", "ahk_exe chrome.exe"] {
            for h in WinGetList(exe) {
                if !antes.Has(h) {
                    WinActivate "ahk_id " h
                    WinWaitActive "ahk_id " h, , 3
                    Sleep 400
                    return h
                }
            }
        }
    }
    return 0
}

F3::  montarBancada()
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

    ; ⛔⛔ GRAVA A GEOMETRIA DA JANELA CALIBRADA. Sem isto o `prepararJanela`
    ; nao tem com o que comparar, e o script poderia rodar numa janela de
    ; outro tamanho clicando fora de todos os alvos — em silencio, gastando
    ; credito. E' o unico dado que faltava para a trava existir.
    ; ⚠️ Grava a da janela que estiver ATIVA no fim da calibracao, que e'
    ; onde o operador acabou de apontar os seis pontos.
    try {
        WinGetPos(&cx, &cy, &cw, &ch, "A")
        IniWrite cw, INI, "pontos", "calib_w"
        IniWrite ch, INI, "pontos", "calib_h"
        IniWrite WinGetTitle("A"), INI, "pontos", "calib_janela"
    }

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
        MouseMove x, y, Random(4, 11)
        ToolTip "[seco] clicaria em " chave
        pausa(280)
        return
    }
    ; ⚠️ o mouse ANDA (velocidade 8-22; quanto maior, mais devagar) e so'
    ; depois clica — com um respiro curto no meio, como quem mira.
    MouseMove x, y, Random(4, 11)
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
    } catch as e {
        return MsgBox("Falta calibrar: " e.Message, "Piloto AdBatch", 16)
    }

    ; ⭐⭐ A SESSAO E' ESCOLHIDA AQUI, a cada F10/F8 — decisao do operador.
    ; Ele ve' onde vai rodar ANTES de gastar credito, e o ensaio seco (F8)
    ; passa pelo mesmo caminho de propria: um F8 que testasse outra janela
    ; que nao a do F10 nao testaria nada.
    hJanela := escolherSessao()
    if (hJanela = 0)
        return
    try
        prepararJanela(hJanela)
    catch as e
        return MsgBox(e.Message, "Piloto AdBatch", 16)
    anotar("sessao: " WinGetTitle("ahk_id " hJanela))

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

            ; ⚠️ pelo HANDLE, nunca pelo titulo: o `irParaAba()` troca de aba
            ; e a aba MUDA o titulo da janela.
            if !WinExist("ahk_id " hJanela)
                throw Error("a janela da sessao foi fechada no meio do ciclo")
            WinActivate "ahk_id " hJanela
            WinWaitActive "ahk_id " hJanela, , 4
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
    ; ⛔ A RONDA RECEBE A MESMA JANELA. Ela le' pixel e clica REGERAR nos
    ; slots vazios — feita noutra sessao, ela leria a cor errada e clicaria
    ; em REGERAR de um lote que nao e' este, jogando fora trabalho pronto e
    ; gastando credito. Era o risco de deixar a busca por titulo aqui.
    ronda(hJanela)
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
ronda(hJanela) {
    global abortar, INI
    abas    := Integer(IniRead(INI, "config", "abas", "0"))
    corVaz  := IniRead(INI, "pontos", "cor_vazio", "")
    maxR    := Integer(IniRead(INI, "config", "rondas", "6"))
    espera  := Integer(IniRead(INI, "config", "espera_s", "15"))

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
        if !WinExist("ahk_id " hJanela) {
            anotar("ronda parada: a janela da sessao foi fechada")
            break
        }
        WinActivate "ahk_id " hJanela
        WinWaitActive "ahk_id " hJanela, , 4
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
