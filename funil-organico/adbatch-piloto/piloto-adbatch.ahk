#Requires AutoHotkey v2.0
#SingleInstance Force

; ⭐ Metadados do executavel, lidos pelo Ahk2Exe na compilacao. Sem eles o .exe
; sai com o nome e a versao do proprio AutoHotkey nas Propriedades do arquivo —
; e um executavel que se apresenta como outro programa e' o tipo de coisa que
; antivirus e operador estranham, cada um a seu modo.
;@Ahk2Exe-SetName        Video Terminator
;@Ahk2Exe-SetDescription Video Terminator by Eddie
;@Ahk2Exe-SetProductName Video Terminator
;@Ahk2Exe-SetCopyright   Eddie
;@Ahk2Exe-SetVersion     1.0.0.0
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

;  ⭐⭐ O FORMATO DA BANCADA — Vertical 2 ou Vertical 3 (2026-08-20)
; =============================================================================
; Ordem do operador: *"selecionar se a montagem da bancada sera para abrir no
; adbatch vertical 3, pra adaptar para a nova rota de 3 takes de 6 segundos"*.
;
; ⛔ NAO ERA SO' TROCAR A URL. Sete coisas dependiam do numero de takes, e a
; que bloqueava de verdade era a CONFERENCIA DAS PARTES: ela procurava
; `IMAGE 01/02` com o sufixo cravado, entao um roteiro do `banho16_3t` (que
; emite `IMAGE 01/03`) era recusado antes de o piloto colar qualquer coisa.
;
; ⛔⛔ E A CALIBRACAO E' POR FORMATO, nunca compartilhada. O Vertical 3 tem
; TRES colunas de slot onde o 2 tem duas: os pontos do `slot1` e do `reger1`
; caem em lugares diferentes nos dois layouts. Uma secao so' no .ini faria
; calibrar o V3 APAGAR a calibracao do V2 — e o operador so' descobriria com o
; ponteiro clicando no vazio, com o credito ja' gasto.
;   2 takes -> secao [pontos]   (a que ja' existe; a calibracao dele sobrevive)
;   3 takes -> secao [pontos3]
;
; ⚠️ O id do Vertical 2 foi MEDIDO constante entre sessoes. O do Vertical 3 tem
; UMA observacao. Os dois moram no .ini com estes valores como padrao: se o id
; do V3 variar por projeto, o conserto e' uma linha no arquivo.

TOOL_ADBATCH_V2 := "d882542c-72bd-4f73-81e1-472aa705775f"
TOOL_ADBATCH_V3 := "89820f1d-1ec5-4fea-a1b1-1e5709a7634b"

nTakes() {
    global INI
    n := IniRead(INI, "config", "takes", "2")
    return (n = "3") ? 3 : 2
}

; ⛔ O sufixo dos blocos: `01/02` ou `01/03`. E' o que o agente escreve e o que
; a conferencia procura — os dois TEM de sair da mesma funcao.
sufTake() {
    return (nTakes() = 3) ? "/03" : "/02"
}

; ⛔ A secao do .ini onde os pontos daquele formato moram.
secPontos() {
    return (nTakes() = 3) ? "pontos3" : "pontos"
}

nomeFormato() {
    return (nTakes() = 3) ? "AdBatch Vertical 3" : "AdBatch Vertical 2"
}

toolAdbatch() {
    global INI, TOOL_ADBATCH_V2, TOOL_ADBATCH_V3
    if (nTakes() = 3)
        return IniRead(INI, "ferramentas", "adbatch3", TOOL_ADBATCH_V3)
    return IniRead(INI, "ferramentas", "adbatch2", TOOL_ADBATCH_V2)
}

; ⭐ `ALVOS` continua GLOBAL e continua sendo uma lista — todos os `for a in
; ALVOS` do arquivo seguem funcionando sem tocar em nenhum deles. O que muda e'
; que ela e' RECONSTRUIDA quando o formato troca.
ALVOS := []

montarAlvos() {
    global ALVOS
    ALVOS := [
        ["cr_roteiro", "a caixa 'Cole o roteiro inteiro...' (Roteiro Master)"],
        ["cr_gerar",   "o botao 'Gerar Lote com Referencia'"],
    ]
    loop nTakes() {
        i := A_Index
        ALVOS.Push(["cr_slot" i,  "o MEIO do quadro cinza do SLOT 0" i])
    }
    loop nTakes() {
        i := A_Index
        ALVOS.Push(["cr_reger" i, "o botao REGERAR do SLOT 0" i])
    }
}
montarAlvos()

; ⛔⛔ TROCAR DE FORMATO NAO APAGA A CALIBRACAO DO OUTRO — mas o formato
; novo pode nunca ter sido calibrado, e rodar sem calibrar clica no vazio
; GASTANDO CREDITO em silencio. Melhor dizer na hora da troca do que o
; operador descobrir no render.
trocarFormato(n) {
    global INI, ALVOS
    IniWrite((n = 3) ? "3" : "2", INI, "config", "takes")
    montarAlvos()
    if (IniRead(INI, secPontos(), "cr_gerar_x", "") != "")
        return
    msg := "Formato trocado para " nomeFormato() "."
        . "`n`nEste formato AINDA NAO FOI CALIBRADO."
        . "`nAperte F9 com o " nomeFormato() " aberto no Chrome antes de"
        . " rodar — sao " ALVOS.Length " pontos."
        . "`n`nA calibracao do outro formato continua guardada."
    MsgBox(msg, "Video Terminator", "Icon!")
}

; ⭐ Os pares (slot, regerar) que a ronda percorre. Mesma fonte da verdade.
paresDaRonda() {
    pares := []
    loop nTakes() {
        i := A_Index
        pares.Push(["cr_slot" i, "cr_reger" i])
    }
    return pares
}

; ⭐ As partes que o roteiro copiado TEM de ter. Cinco no V2, sete no V3.
partesDoRoteiro() {
    ; ⛔⛔ O `REF 01:` SO' E' COBRADO NO VERTICAL 2, e isso nao e' folga:
    ; o `banho16_3t` e' o UNICO dos 44 motores sem `BLOCO 0 (REF)`, por
    ; ordem do operador em 2026-08-14 testando o app: *"A imagem do bloco 0
    ; desse agente e' completamente irrelevante, posso anexar direto a
    ; imagem 1 como referencia"*. E ele esta' certo pela estrutura: a ancora
    ; daquele angulo e' a MAO, que ja' aparece na IMAGE 01, na mesma luz.
    ; Exigir REF aqui recusaria TODO roteiro de tres takes.
    ; ⚠️ A guarda contra copia truncada continua inteira: sao as TRES IMAGE
    ; e os TRES TAKE, conferidos um a um logo abaixo.
    p := (nTakes() = 3) ? [] : ["REF 01:"]
    loop nTakes() {
        p.Push(Format("IMAGE 0{1}{2}", A_Index, sufTake()))
    }
    loop nTakes() {
        p.Push(Format("TAKE 0{1}{2}", A_Index, sufTake()))
    }
    return p
}

; =============================================================================
;  ⭐⭐ UMA CARA SO' PARA TODAS AS TELAS (2026-08-11)
; =============================================================================
; Ordem do operador: *"melhore o ui do script, esta confuso atualmente"* e, sobre
; a janela do F3 especificamente: *"vc ainda deixou essa daqui crua, confusa"*.
;
; ⛔ O que fazia parecer confuso nao era cada tela isolada — era serem TRES
; DIALETOS. Uma pedia numero digitado, outra era paragrafo cinza, outra um
; MsgBox. Fonte, margem, largura e o lugar dos botoes mudavam de uma para outra,
; e isso obriga a reaprender a tela a cada vez.
;
; ⭐ Daqui em diante toda janela nasce destas duas funcoes. Nao e' economia de
; linha: e' o que garante que o proximo dialogo tambem saia igual, em vez de
; depender de eu lembrar as medidas.
; ⭐ O NOME DO PROGRAMA, batizado pelo operador em 2026-08-11:
; *"nomeie o programa como Video Terminator by Eddie"*.
; ⚠️ So' o nome VISIVEL mudou. Os arquivos seguem `piloto-adbatch.ini`,
; `.log` e a pasta `roteiros\` — renomear o .ini apagaria a calibracao dos 6
; pontos, e renomear a pasta esconderia os roteiros ja' gravados. Nome de
; produto e nome de arquivo sao coisas diferentes, e so' o primeiro foi pedido.
APP := "Video Terminator by Eddie"

LARG_UI := 700

; ⭐⭐ TEMA ESCURO, e nao por gosto: TODAS as telas do operador sao escuras — o
; Windows, o Chrome, o Flow, o Dolphin. Uma janela branca no meio disso e' a
; unica coisa que pisca na tela, e ele passa o dia olhando para elas. O tema e'
; LIDO DO WINDOWS, nunca cravado: quem volta para o claro nao herda um dialogo
; preto.
temaEscuro() {
    try return !RegRead("HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes"
                        "\Personalize", "AppsUseLightTheme")
    return false
}

ESCURO   := temaEscuro()
COR_FUNDO := ESCURO ? "202020" : ""
COR_TEXTO := ESCURO ? "E8E8E8" : ""
COR_CAMPO := ESCURO ? "2B2B2B" : ""
COR_FRACA := ESCURO ? "9A9A9A" : "Gray"
COR_BOA   := ESCURO ? "6FD08C" : "Green"
COR_MA    := ESCURO ? "FF7B72" : "Red"

; ⚠️ Ordinais NAO DOCUMENTADOS do uxtheme (135 = SetPreferredAppMode, 136 =
; FlushMenuThemes). Sao o unico jeito de a barra de rolagem e a moldura dos
; controles comuns virem escuras — mas justamente por nao serem documentados vao
; dentro de `try`: numa build do Windows em que sumirem, a janela sai clara em
; vez de o script morrer na partida.
if ESCURO {
    try {
        DllCall("uxtheme\#135", "Int", 2)
        DllCall("uxtheme\#136")
    }
}

; ⭐ pinta o controle com o tema escuro dos controles comuns (rolagem, borda,
; cabecalho de ListView). Sem isto o fundo fica escuro e a rolagem fica branca.
escurecerUI(ctl) {
    global ESCURO
    if !ESCURO
        return ctl
    try DllCall("uxtheme\SetWindowTheme", "Ptr", ctl.Hwnd,
                "Str", "DarkMode_Explorer", "Ptr", 0)
    return ctl
}

fonteUI(g, opc := "s9", familia := "Segoe UI") {
    global COR_TEXTO
    g.SetFont(opc (COR_TEXTO = "" ? "" : " c" COR_TEXTO), familia)
}

; ⚠️ campo (Edit/ListView) nao herda o BackColor da janela — tem de ser dito um
; a um, senao a janela fica escura com buracos brancos, que e' pior que tudo
; claro.
fundoUI() {
    global COR_CAMPO
    return (COR_CAMPO = "" ? "" : " Background" COR_CAMPO)
}

; ⚠️ titulo vazio nao vira "Piloto AdBatch — " com o travessao solto: a tela de
; abertura nao e' "o Piloto AdBatch de alguma coisa", e' o Piloto AdBatch.
janelaUI(titulo := "") {
    global COR_FUNDO
    g := Gui("+AlwaysOnTop -MinimizeBox",
             APP (titulo = "" ? "" : " — " titulo))
    g.MarginX := 18, g.MarginY := 16
    if (COR_FUNDO != "")
        g.BackColor := COR_FUNDO
    fonteUI(g)
    ; ⭐ Esc fecha. E' o reflexo de todo mundo diante de uma caixa de dialogo, e
    ; sem isto o operador fica caçando o botao Cancelar com o mouse.
    g.OnEvent("Escape", (*) => g.Destroy())
    return g
}

; =============================================================================
;  ⭐ O DOOMGUY (2026-08-11)
; =============================================================================
; Pedido do operador: *"coloque o gif do doomguy na interface do Video Terminator
; by Eddie"*.
;
; ⛔ O AHK v2 mostra apenas o PRIMEIRO frame de um GIF num controle Picture — nao
; anima. Por isso o gif foi quebrado em 6 PNGs na hora de empacotar
; (`scratchpad/extrair_doomguy.py`) e a troca e' feita com um timer. O custo fica
; na ferramenta de build, e nao no script que roda o dia inteiro.
;
; ⚠️⚠️ ENFEITE NUNCA DERRUBA A FERRAMENTA. Se a pasta `doomguy\` nao estiver ao
; lado do executavel, esta funcao simplesmente nao desenha nada e a tela abre
; igual. Uma cara faltando nao pode custar o acesso ao F10.
;
; ⚠️ O timer e' amarrado ao FECHAMENTO da janela. Sem isso ele continuaria
; disparando contra um controle destruido — e o erro apareceria minutos depois,
; longe da causa.
DOOM_FRAMES := 6
DOOM_MS := 480          ; a cadencia do gif original, medida nele

; ⚠️ `altFaixa` centra a cara verticalmente na faixa preta. Passar a altura em
; vez de cravar um `y` deixa a faixa e a imagem amarradas: mudar uma sem a outra
; deixaria a cara flutuando fora do preto, que e' justamente o que a faixa veio
; consertar.
doomguy(g, altFaixa := 100) {
    global DOOM_FRAMES, DOOM_MS, LARG_UI
    pasta := A_ScriptDir "\doomguy"
    if !FileExist(pasta "\f0.png")
        return
    pic := g.AddPicture("x" (18 + LARG_UI - 44) " y" ((altFaixa - 64) // 2)
                        " w44 h64", pasta "\f0.png")
    quadro := 0
    virar() {
        if !WinExist("ahk_id " g.Hwnd) {
            SetTimer , 0
            return
        }
        quadro := Mod(quadro + 1, DOOM_FRAMES)
        try pic.Value := pasta "\f" quadro ".png"
    }
    SetTimer virar, DOOM_MS
    g.OnEvent("Close", (*) => SetTimer(virar, 0))
}

; ⚠️ `primeira` existe porque a primeira secao nao leva o respiro de cima — sem
; isso a janela abre com um buraco antes do primeiro titulo.
; ⛔⛔ O `x18` AQUI E' O CONSERTO DE UM DEFEITO QUE O OPERADOR VIU NA TELA:
; *"ta sobrando muito espaco de um lado na interface, esta desequilibrado e
; feio"*. A janela tinha saido com 1408px em vez de 752.
;
; A causa: o doomguy e' posicionado com X ABSOLUTO (canto direito). No AHK, o
; controle seguinte que use so' `y+N` HERDA O X DO ANTERIOR — entao o titulo da
; secao nascia la' na direita, com 700px de largura, e a janela crescia para
; caber. Todo o conteudo ficava espremido de um lado e o resto era vazio.
;
; ⚠️ E' a TERCEIRA vez que este mesmo mecanismo morde neste arquivo (a tela do
; F2, a linha do log, agora aqui). Por isso o conserto foi no `secaoUI`, que
; TODA tela usa, e nao no ponto onde apareceu.
secaoUI(g, texto, primeira := false) {
    global LARG_UI
    fonteUI(g, "s10 Bold")
    g.AddText("x18 w" LARG_UI (primeira ? "" : " y+18"), texto)
    fonteUI(g, "s9 Norm")
}

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
; ⭐⭐ E DESDE 2026-08-15 NENHUM DESTES NUMEROS E' CRAVADO. Ordem do operador:
; *"quero um ui ux pertinente onde consigo setar quais valores quero pro script
; que copia e cola os prompts no adbatch vertical — tempo entre as bancadas,
; tempo de interacao entre os eventos etc"*.
;
; ⛔ OS VALORES ABAIXO SAO O PADRAO, nao a verdade: o `aplicarTempos()` le' a
; secao `[tempos]` do INI por cima deles na partida E no comeco de cada F10.
; Quem edita e' a tela do atalho `Tempos` — e os padroes daqui sao exatamente
; os numeros que o script tinha antes de a tela existir, entao INI vazio =
; comportamento identico ao de sempre.
global RITMO := 0.05
global PISO_PAUSA := 8
global VEL_MOUSE_MIN := 4
global VEL_MOUSE_MAX := 11
global PARSE_MS := 900
global PARSE_EXTRA := 700
global RESPIRO_PCT := 22
global RESPIRO_MIN := 1200
global RESPIRO_MAX := 3400
global ENTRE_BANCADAS_S := 0

; ⚠️ Numero do INI e' entrada HOSTIL como qualquer outra: campo vazio, texto,
; virgula decimal ou 500 no `ritmo` chegariam ao ffmpeg do dia a dia como uma
; espera de dez minutos por clique. Fora da faixa e' GRAMPEADO, nunca recusado
; — erro de digitacao numa caixa nao pode impedir o operador de rodar o lote.
tempoNum(chave, padrao, lo, hi) {
    global INI
    v := Trim(IniRead(INI, "tempos", chave, ""))
    v := StrReplace(v, ",", ".")
    if !IsNumber(v)
        return padrao
    n := Number(v)
    return (n < lo) ? lo : (n > hi) ? hi : n
}

; ⛔⛔ CHAMADO NA PARTIDA **E** NO COMECO DE CADA F10/F8/F9, e isso nao e'
; redundancia: `SetKeyDelay`/`SetMouseDelay` sao POR THREAD no AHK v2. Chamados
; so' na partida eles viram o padrao das threads novas — mas um valor salvo na
; tela DEPOIS da partida nunca alcancaria a thread que ja' esta' rodando. Sem
; esta segunda chamada, a tela salvaria e o operador juraria que nao mudou nada.
aplicarTempos() {
    global RITMO, PISO_PAUSA, VEL_MOUSE_MIN, VEL_MOUSE_MAX, PARSE_MS
    global PARSE_EXTRA, RESPIRO_PCT, RESPIRO_MIN, RESPIRO_MAX, ENTRE_BANCADAS_S
    RITMO            := tempoNum("ritmo",            0.05, 0.01, 2)
    PISO_PAUSA       := tempoNum("piso_ms",          8,    1,    2000)
    VEL_MOUSE_MIN    := tempoNum("mouse_vel_min",    4,    0,    50)
    VEL_MOUSE_MAX    := tempoNum("mouse_vel_max",    11,   0,    50)
    PARSE_MS         := tempoNum("parse_ms",         900,  0,    20000)
    PARSE_EXTRA      := tempoNum("parse_extra_ms",   700,  0,    20000)
    RESPIRO_PCT      := tempoNum("respiro_pct",      22,   0,    100)
    RESPIRO_MIN      := tempoNum("respiro_min_ms",   1200, 0,    30000)
    RESPIRO_MAX      := tempoNum("respiro_max_ms",   3400, 0,    30000)
    ENTRE_BANCADAS_S := tempoNum("entre_bancadas_s", 0,    0,    900)
    ; ⚠️ par invertido nao e' erro de quem digitou, e' ordem de digitacao: quem
    ; poe 20 no minimo antes de subir o maximo passa por um instante invalido.
    ; `Random(20, 11)` levantaria excecao no meio do ciclo — colapsa em vez.
    if (VEL_MOUSE_MAX < VEL_MOUSE_MIN)
        VEL_MOUSE_MAX := VEL_MOUSE_MIN
    if (RESPIRO_MAX < RESPIRO_MIN)
        RESPIRO_MAX := RESPIRO_MIN
    kd := Round(tempoNum("key_delay_ms", 22, 1, 400))
    SetKeyDelay kd, kd
    SetMouseDelay Round(tempoNum("mouse_delay_ms", 28, 1, 400))
}

pausa(base, esp := 35) {
    global RITMO, PISO_PAUSA
    ; base em ms, `esp` = espalhamento em % para cada lado.
    ; ⚠️ piso: sorteio que devolve valor perto de zero volta a ser ritmo de
    ; maquina, so' que rapido. Era 40 ate' o RITMO cair para 0.20 — ver a nota
    ; do RITMO acima. Hoje ele DESCE JUNTO pela tela, e e' por isso que a tela
    ; mostra os dois lado a lado.
    d := Round(base * RITMO) * (100 + Random(-esp, esp)) // 100
    Sleep (d < PISO_PAUSA ? PISO_PAUSA : d)
}

respirar() {
    global RESPIRO_PCT, RESPIRO_MIN, RESPIRO_MAX
    ; ⭐ A pausa longa e RARA — a pessoa que para para olhar a tela. Um ritmo
    ; uniforme, mesmo com ruido, ainda e' uniforme: o que quebra o padrao e' a
    ; excecao ocasional, nao o tremor constante.
    if (RESPIRO_PCT > 0 && Random(1, 100) <= RESPIRO_PCT)
        Sleep Random(RESPIRO_MIN, RESPIRO_MAX)
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
; ⛔⛔ O PISO DE TAMANHO NAO E' CAPRICHO. Com o seletor novo mostrando a
; geometria, apareceu na lista uma "sessao" chamada `Translate this page?` de
; 355x61 — o popup de traducao do Chrome, que e' uma janela com titulo do mesmo
; processo. Ela estava na lista ANTES tambem; so' era invisivel porque a versao
; antiga mostrava apenas o titulo. Uma janela de navegador nao tem 355x61, e
; escolher o popup por engano rodaria o piloto contra nada.
JANELA_MIN_W := 600
JANELA_MIN_H := 400

; ⛔ Devolve [{hwnd, titulo, tipo}] de tudo que serve como alvo AGORA.
listarSessoes() {
    global INI, JANELA_MIN_W, JANELA_MIN_H
    achadas := []
    grande(hwnd) {
        global JANELA_MIN_W, JANELA_MIN_H
        try {
            WinGetPos , , &w, &h, "ahk_id " hwnd
            return (w >= JANELA_MIN_W && h >= JANELA_MIN_H)
        }
        return false
    }
    ; as do Dolphin: um processo `anty.exe` por perfil aberto
    for hwnd in WinGetList("ahk_exe anty.exe") {
        t := WinGetTitle(hwnd)
        if (t != "" && grande(hwnd))
            achadas.Push({hwnd: hwnd, titulo: t, tipo: "Dolphin"})
    }
    ; a principal: Chrome com a AdBatch aberta
    tC := IniRead(INI, "config", "titulo_chrome", "Google Flow")
    for hwnd in WinGetList("ahk_exe chrome.exe") {
        t := WinGetTitle(hwnd)
        if (t != "" && InStr(t, tC) && grande(hwnd))
            achadas.Push({hwnd: hwnd, titulo: t, tipo: "Chrome"})
    }
    return achadas
}

; ⛔ Em que monitor a janela esta' — pelo CENTRO dela, nao pelo canto: janela a
; cavalo entre duas telas tem canto numa e corpo na outra, e o canto mentiria.
monitorDaJanela(hwnd) {
    if !WinExist("ahk_id " hwnd)
        return 0
    WinGetPos &x, &y, &w, &h, "ahk_id " hwnd
    cx := x + w / 2, cy := y + h / 2
    loop MonitorGetCount() {
        MonitorGetWorkArea(A_Index, &l, &t, &r, &b)
        if (cx >= l && cx <= r && cy >= t && cy <= b)
            return A_Index
    }
    return 0
}

; ⭐⭐ QUANTO UMA JANELA MAXIMIZADA TRANSBORDA A AREA UTIL. Medido em 2026-08-11:
; area util 1920x1032, WinGetPos da mesma janela maximizada 1936x1048 — 16px. E'
; a moldura invisivel de redimensionamento. Vem do sistema em vez de constante
; cravada porque muda com o tema e a escala do Windows.
molduraMaximizada() {
    return 2 * (SysGet(32) + SysGet(92))    ; SM_CXSIZEFRAME + SM_CXPADDEDBORDER
}

; ⭐⭐ PREVE O VEREDITO DA prepararJanela() SEM TER DE RODAR NADA.
; A trava de geometria do F10 maximiza a janela e compara com a calibracao. Como
; maximizada = area util do monitor + moldura, da' para dizer AQUI, na lista, se
; aquela janela vai servir — e o operador escolhe sabendo, em vez de descobrir la'
; na frente com o roteiro ja' colado.
serveParaOF10(hwnd) {
    global INI, ALVOS
    m := monitorDaJanela(hwnd)
    if (m = 0)
        return "?"
    cw := IniRead(INI, secPontos(), "calib_w", "")
    ch := IniRead(INI, secPontos(), "calib_h", "")
    if (cw != "" && ch != "") {
        MonitorGetWorkArea(m, &l, &t, &r, &b)
        mo := molduraMaximizada()
        if (Abs((r - l) + mo - Integer(cw)) <= 12 && Abs((b - t) + mo - Integer(ch)) <= 12)
            return "SIM"
        return "NAO — o F10 aborta"
    }

    ; ⭐⭐ SEM `calib_w`/`calib_h` (calibracao anterior a trava) AINDA DA' PARA
    ; RESPONDER, e a resposta e' ate' mais direta: os SEIS PONTOS CALIBRADOS sao
    ; coordenadas de TELA. Se um deles cai fora do retangulo da janela, aquele
    ; clique vai bater em outro lugar — nao ha' o que discutir.
    ; ⚠️ Sem isto a coluna mais util da tela vinha "calibracao antiga" em TODAS as
    ; linhas, que e' o mesmo que nao existir. Medido no .ini dele: os pontos vao
    ; ate' (1171, 772), entao a janela de retrato em x>=1920 e' reprovada de cara
    ; e a de paisagem passa — exatamente o que ele precisa ver.
    WinGetPos &wx, &wy, &ww, &wh, "ahk_id " hwnd
    algum := false
    for a in ALVOS {
        px := IniRead(INI, secPontos(), a[1] "_x", "")
        py := IniRead(INI, secPontos(), a[1] "_y", "")
        if (px = "" || py = "")
            continue
        algum := true
        if (Integer(px) < wx || Integer(px) > wx + ww
            || Integer(py) < wy || Integer(py) > wy + wh)
            return "NAO — pontos fora"
    }
    return algum ? "provavel" : "sem calibracao"
}

; =============================================================================
;  ⭐⭐ AS BANCADAS GRAVADAS — UM PAR POR SESSAO, QUANTAS SESSOES EXISTIREM
; =============================================================================
; Ordem do operador (2026-08-11): *"funcione para as quatro sessoes, ou quantas
; vierem no futuro, pois pretendo expandir a operacao e ter outras contas no
; Dolphin"*.
;
; ⛔ E' POR ISSO QUE NAO HA' LISTA DE SESSOES NESTE CODIGO. Cada F3 grava o par
; de janelas daquela sessao numa chave propria do INI, com o titulo dela como
; nome da chave. Conta nova no Dolphin = chave nova no dia em que ela rodar o F3;
; nada aqui precisa ser editado. A `SESSOES_ESPERADAS` continua existindo so'
; para dizer o que esta' FECHADO, que e' outro assunto.
;
; ⚠️ O handle morre quando o script e' reiniciado — e reiniciar e' exatamente o
; que ele faz depois de cada versao nova. Foi assim que a marca do F3 sumiu no
; primeiro uso real. No disco, sobrevive.

; ⛔ `=` e `;` quebrariam o arquivo INI, e o titulo vem do Windows: nao da' para
; confiar que nao tem nenhum dos dois.
chaveDeBancada(titulo) {
    t := StrReplace(StrReplace(Trim(titulo), "=", "-"), ";", "-")
    return SubStr(t, 1, 80)
}

; ⭐⭐ O NOME DA SESSAO PRINCIPAL DO CHROME (2026-08-11)
; Reparo pedido pelo operador: *"achei que o script fosse pegar a minha sessao
; logada padrao do Chrome fora do Dolphin tambem"*.
;
; ⛔ Ele estava certo, e a minha razao para excluir era um problema MEU: o titulo
; da janela do Chrome muda a cada aba, e eu tinha usado o titulo como chave da
; sessao. Chave instavel nao serve para amarrar tecla — mas a resposta e' dar ao
; Chrome uma chave ESTAVEL, e nao deixar a sessao de fora da lista.
;
; ⚠️ E' um nome FIXO, nao o titulo: fora do Dolphin ha' uma sessao logada so' — a
; principal dele. Se um dia houver mais de uma, ela precisara' de um nome proprio,
; e nao de um titulo que muda quando ele troca de aba.
CHAVE_CHROME := "Chrome — sessao principal"

; ⛔ A chave de QUALQUER janela: Dolphin pelo nome do perfil (que e' estavel),
; Chrome pelo nome fixo. Esta funcao e' o unico lugar que decide isso — o F3
; grava por ela e a tela de teclas lista por ela, entao as duas nao tem como
; divergir.
chaveDaSessao(hwnd) {
    global CHAVE_CHROME
    try {
        exe := WinGetProcessName("ahk_id " hwnd)
        if (exe = "chrome.exe")
            return CHAVE_CHROME
    }
    return chaveDeBancada(WinGetTitle("ahk_id " hwnd))
}

gravarBancada(titulo, h1, h2) {
    global INI
    try IniWrite h1 "," h2, INI, "bancadas", chaveDeBancada(titulo)
}

; devolve [{chave, h1, h2}] apenas das bancadas cujas DUAS janelas ainda vivem
bancadasVivas() {
    global INI
    vivas := []
    bruto := ""
    try bruto := IniRead(INI, "bancadas")      ; secao inteira, "chave=valor"
    if (bruto = "")
        return vivas
    for linha in StrSplit(bruto, "`n") {
        p := InStr(linha, "=")
        if (!p)
            continue
        chave := SubStr(linha, 1, p - 1)
        par := StrSplit(SubStr(linha, p + 1), ",")
        if (par.Length < 2 || !IsInteger(Trim(par[1])) || !IsInteger(Trim(par[2])))
            continue
        h1 := Integer(Trim(par[1])), h2 := Integer(Trim(par[2]))
        ; ⛔ O WINDOWS RECICLA HANDLE. Sem conferir que as duas ainda existem,
        ; uma janela qualquer poderia herdar a bancada de outra sessao e o F4
        ; arrastaria a janela errada para o monitor errado.
        if (WinExist("ahk_id " h1) && WinExist("ahk_id " h2))
            vivas.Push({chave: chave, h1: h1, h2: h2})
    }
    return vivas
}

; a bancada a que uma janela pertence, ou 0
parDaJanela(hwnd) {
    for b in bancadasVivas()
        if (b.h1 = hwnd || b.h2 = hwnd)
            return b
    return 0
}

bancadaPorChave(chave) {
    for b in bancadasVivas()
        if (b.chave = chave)
            return b
    return 0
}

; =============================================================================
;  ⭐⭐ UMA TECLA POR SESSAO, ESCOLHIDA POR ELE (2026-08-11)
; =============================================================================
; Duas ordens do operador, na sequencia:
;   *"atribua uma tecla para cada sessao logada identificada"*
;   *"coloca um ui ux pertinente para eu setar qual tecla quero que seja trigger
;    de cada par de janela"*
;
; ⛔ A primeira versao cravava `Ctrl+Alt+1..9` no codigo. Funcionava, mas a
; escolha da tecla e' DELE: quem decora atalho e' quem opera, e ele ja' tem
; atalhos na cabeca de outros programas. Tecla cravada por mim vira conflito que
; so' ele descobre — e so' eu posso consertar.
;
; ⭐ Agora a tecla e' CAPTURADA num controle Hotkey nativo (ele aperta a combinacao
; e o Windows a escreve) e registrada em tempo de execucao com `Hotkey()`. Nada
; de atalho fixo no fonte.
;
; ⚠️ FORMATO NO INI: `[teclas] <nome da sessao> = <tecla em sintaxe AHK>`, por
; exemplo `CTA - 03 Neusa=^!1`. A chave e' o NOME DA SESSAO e nao um numero de
; ordem: numero de ordem faria uma sessao nova RENUMERAR as outras, e tecla que
; muda de dono sozinha e' pior que nao ter tecla.

TECLAS_MAX := 9

; ⛔ Converte a sintaxe do AHK para o que se le' numa tela. `^!1` nao e' nome de
; tecla para ninguem fora do AutoHotkey.
nomeDaTecla(t) {
    if (t = "")
        return "(nenhuma)"
    n := ""
    resto := t
    for par in [["^", "Ctrl+"], ["!", "Alt+"], ["+", "Shift+"], ["#", "Win+"]] {
        if InStr(SubStr(resto, 1, 4), par[1]) {
            n .= par[2]
            resto := StrReplace(resto, par[1], , , , 1)
        }
    }
    return n StrUpper(SubStr(resto, 1, 1)) SubStr(resto, 2)
}

; [{chave, tecla}] de tudo que tem bancada gravada OU tecla gravada — as duas
; fontes, porque uma sessao pode ter tecla e estar fechada, e vice-versa.
teclasGravadas() {
    global INI
    vistos := Map()
    r := []
    bruto := ""
    try bruto := IniRead(INI, "teclas")
    for linha in StrSplit(bruto, "`n") {
        p := InStr(linha, "=")
        if (!p)
            continue
        c := Trim(SubStr(linha, 1, p - 1))
        if (c = "" || vistos.Has(c))
            continue
        vistos[c] := true
        r.Push({chave: c, tecla: Trim(SubStr(linha, p + 1))})
    }
    ; ⚠️ sessao com bancada e sem tecla TEM de aparecer na tela de configuracao,
    ; senao ele nao tem por onde atribuir a primeira tecla dela.
    bb := ""
    try bb := IniRead(INI, "bancadas")
    for linha in StrSplit(bb, "`n") {
        p := InStr(linha, "=")
        if (!p)
            continue
        c := Trim(SubStr(linha, 1, p - 1))
        if (c = "" || vistos.Has(c))
            continue
        vistos[c] := true
        r.Push({chave: c, tecla: ""})
    }
    return r
}

; ⭐⭐ TODAS AS SESSOES QUE EXISTEM, e nao so' as que ja' rodaram o F3
; (2026-08-11). Reparo pedido pelo operador: *"a tela de setup dos pares esta'
; elencando so' a CTA 03, achei que haveria identificacao automatica de todas as
; sessoes logadas e seriam ja' elencadas ali"*.
;
; ⛔ Ele estava certo, e o erro era de ordem: a tela de ATRIBUIR tecla so'
; mostrava quem ja' tinha bancada — ou seja, exigia montar antes de poder
; escolher a tecla, quando escolher a tecla e' justamente o passo anterior.
;
; ⚠️ QUATRO FONTES, nesta ordem de utilidade, sem repetir ninguem:
;   1. perfis do Dolphin ABERTOS agora ...... o que ele ve' na tela
;   2. sessoes esperadas, mesmo FECHADAS .... da' para atribuir a tecla antes de
;                                             abrir o perfil
;   3. quem tem bancada gravada ............. inclui alvo que nao e' Dolphin
;   4. quem tem tecla gravada ............... nunca perder uma atribuicao
;
; ⛔ Janela do Chrome NAO entra pelo titulo: o titulo dela muda a cada aba, e uma
; lista cujos nomes mudam sozinhos nao serve para amarrar tecla. Se ele montar
; uma bancada no Chrome, ela entra pela fonte 3, com o nome que tinha na hora.
sessoesConhecidas() {
    global INI, SESSOES_ESPERADAS, CHAVE_CHROME, JANELA_MIN_W, JANELA_MIN_H
    ; ⚠️ enumera as janelas UMA vez. A primeira versao chamava `listarSessoes()`
    ; dentro do laco, varrendo todas as janelas do sistema por sessao — barato
    ; com seis, e a lista dele vai crescer por decisao dele mesmo.
    abertas := Map()
    for s in listarSessoes()
        abertas[chaveDaSessao(s.hwnd)] := s.tipo
    ; ⚠️ O `listarSessoes()` so' aceita janela de Chrome que tenha o Flow no
    ; titulo — regra certa para o seletor do F10, e errada AQUI: esta tela
    ; responde "esta sessao existe?", nao "esta sessao esta' com o Flow aberto".
    ; Sem isto, o Chrome aparecia como FECHADA com cinco janelas na tela.
    if !abertas.Has(CHAVE_CHROME) {
        for h in WinGetList("ahk_exe chrome.exe") {
            if (WinGetTitle(h) = "")
                continue
            try {
                WinGetPos , , &w, &hh, "ahk_id " h
                if (w >= JANELA_MIN_W && hh >= JANELA_MIN_H) {
                    abertas[CHAVE_CHROME] := "Chrome"
                    break
                }
            }
        }
    }
    vistos := Map()
    r := []
    juntar(chave) {
        chave := Trim(chave)
        if (chave = "" || vistos.Has(chave))
            return
        vistos[chave] := true
        r.Push({chave: chave,
                tecla: IniRead(INI, "teclas", chave, ""),
                estado: (bancadaPorChave(chave) != 0) ? "bancada montada"
                        : abertas.Has(chave) ? "aberta — rode o F3"
                        : "fechada"})
    }
    ; ⚠️ Dolphin e Chrome entram os DOIS. A versao anterior filtrava
    ; `tipo = "Dolphin"` e deixava a sessao principal dele de fora da lista.
    for chave, tipo in abertas
        juntar(chave)
    for nome in StrSplit(IniRead(INI, "sessoes", "esperadas", SESSOES_ESPERADAS), ",")
        juntar(chaveDeBancada(nome))
    ; ⭐ a sessao principal do Chrome aparece SEMPRE, aberta ou nao: e' onde ele
    ; tambem trabalha, e ele precisa poder escolher a tecla dela antes de montar
    ; a bancada — que e' a ordem certa das duas coisas.
    juntar(CHAVE_CHROME)
    for e in teclasGravadas()
        juntar(e.chave)
    return r
}

teclaDaSessao(chave) {
    global INI
    return IniRead(INI, "teclas", chave, "")
}

gravarTecla(chave, tecla) {
    global INI
    try {
        if (tecla = "")
            IniDelete INI, "teclas", chave
        else
            IniWrite tecla, INI, "teclas", chave
    }
    registrarTeclasDeSessao()
}

; ⚠️ Migra o formato antigo (`1=CTA - 03 Neusa`, numero de ordem) para o novo
; (`CTA - 03 Neusa=^!1`). Sem isto, quem ja' tinha tecla atribuida a perderia em
; silencio na primeira atualizacao — e ficaria achando que o recurso quebrou.
migrarTeclasAntigas() {
    global INI, TECLAS_MAX
    loop TECLAS_MAX {
        n := String(A_Index)
        v := IniRead(INI, "teclas", n, "")
        if (v = "")
            continue
        try IniDelete INI, "teclas", n
        if (IniRead(INI, "teclas", v, "") = "")
            try IniWrite "^!" n, INI, "teclas", v
    }
}

; primeira tecla livre da familia Ctrl+Alt+1..9, so' como SUGESTAO inicial
teclaLivre() {
    global TECLAS_MAX
    usadas := Map()
    for e in teclasGravadas()
        if (e.tecla != "")
            usadas[e.tecla] := true
    loop TECLAS_MAX {
        t := "^!" A_Index
        if !usadas.Has(t)
            return t
    }
    return ""
}

garantirTecla(chave) {
    t := teclaDaSessao(chave)
    if (t != "")
        return t
    t := teclaLivre()
    if (t != "")
        gravarTecla(chave, t)
    return t
}

; ⛔⛔ REGISTRO DINAMICO. Toda tecla ativa e' desligada antes de religar a lista
; nova — sem isto, trocar a tecla de uma sessao deixaria a ANTIGA respondendo
; tambem, e duas teclas para a mesma coisa e' o comeco de uma nao responder.
global gTeclasAtivas := Map()

registrarTeclasDeSessao() {
    global gTeclasAtivas
    for t, _ in gTeclasAtivas {
        try Hotkey(t, "Off")
    }
    gTeclasAtivas := Map()
    for e in teclasGravadas() {
        if (e.tecla = "")
            continue
        try {
            Hotkey(e.tecla, chamadorDaSessao(e.chave), "On")
            gTeclasAtivas[e.tecla] := e.chave
        } catch as err {
            anotar("tecla ignorada (" e.tecla "): " err.Message)
        }
    }
}

; ⚠️ funcao separada de proposito: uma closure criada DENTRO do laco captura a
; variavel do laco, e todas as teclas acabariam chamando a ultima sessao.
chamadorDaSessao(chave) {
    return (*) => levantarSessao(chave)
}

avisoRapido(txt) {
    ToolTip txt
    SetTimer () => ToolTip(), -2400
}

levantarSessao(chave) {
    global rodando
    if rodando
        return
    b := bancadaPorChave(chave)
    if (b = 0)
        return avisoRapido("a bancada de '" chave "' nao esta' aberta.`n"
                           "Abra o perfil no Dolphin e rode o F3.")
    ; ⭐ o foco vai para a janela do AdBatch: ele chamou a SESSAO, e e' nela que
    ; o trabalho acontece. No F4 o foco fica na que ele clicou, que e' outro caso.
    arrumarBancada(b, b.h1)
}

; =============================================================================
;  ⭐ A TELA DE CONFIGURAR AS TECLAS (F2)
; =============================================================================
; ⛔ Um controle Hotkey por sessao, todos visiveis de uma vez: sao no maximo
; nove linhas, e uma tela que exige SELECIONAR antes de EDITAR cobra dois passos
; para o que cabe em um.
; ⚠️ O controle e' o nativo do Windows — ele aperta a combinacao e o proprio
; sistema escreve. Digitar o nome da tecla a mao seria fonte de erro que so'
; apareceria na hora de usar.
configurarTeclas(*) {
    global LARG_UI, INI
    lista := sessoesConhecidas()
    g := janelaUI("teclas das sessoes")
    secaoUI(g, "Qual tecla levanta cada sessao", true)
    if (lista.Length = 0) {
        g.AddText("w" LARG_UI " c" COR_FRACA,
                  "Nenhuma sessao encontrada. Abra um perfil no Dolphin — "
                  "ele aparece aqui sozinho, mesmo antes de rodar o F3.")
        g.AddButton("w110 h30 x" (18 + LARG_UI - 110) " y+16 Default", "Fechar")
         .OnEvent("Click", (*) => g.Destroy())
        g.Show()
        return
    }
    g.AddText("w" LARG_UI " c" COR_FRACA,
              "Clique no campo e aperte a combinacao. Use Ctrl, Alt ou Shift "
              "junto — tecla solta atrapalharia a digitacao.`n"
              "`"None`" quer dizer sem tecla. A tecla so' levanta as janelas "
              "depois que aquela sessao rodar o F3.")
    ; ⛔ O `x18` EXPLICITO EM CADA LINHA nao e' redundancia. Medido em
    ; 2026-08-11: com `y+10` sozinho, o AHK mantem o X do controle ANTERIOR — que
    ; e' o campo de tecla, la' na direita. A segunda linha nascia depois dele, a
    ; terceira depois dessa, e a janela saiu com 1252px de largura contra os 752
    ; das outras telas. Escada, nao formulario.
    ; ⛔ O `x18` EXPLICITO EM CADA LINHA nao e' redundancia. Medido em
    ; 2026-08-11: com `y+10` sozinho, o AHK mantem o X do controle ANTERIOR — que
    ; e' o campo de tecla, la' na direita. A segunda linha nascia depois dele, a
    ; terceira depois dessa, e a janela saiu com 1252px contra os 752 das outras
    ; telas. Escada, nao formulario.
    ; ⭐ O ESTADO VAI JUNTO DO NOME, e nao numa coluna: e' o que responde "por que
    ; essa tecla nao fez nada?" no lugar onde a pergunta nasce.
    campos := []
    for e in lista {
        fonteUI(g, "s9")
        g.AddText("x18 y+10 w" (LARG_UI - 210), e.chave "   (" e.estado ")")
        hk := g.AddHotkey("x+10 yp-3 w200", e.tecla)
        campos.Push({chave: e.chave, ctl: hk})
    }

    ; ⚠️ o aviso fica ACIMA dos botoes e sempre visivel: mensagem de erro que
    ; aparece depois do clique chega tarde.
    aviso := g.AddText("x18 y+14 w" LARG_UI " c" COR_FRACA,
                       "as teclas passam a valer assim que voce salvar")

    salvar(*) {
        global TECLA_NENHUMA
        usadas := Map()
        for c in campos {
            t := c.ctl.Value
            if (t = "")
                continue
            ; ⛔ duas sessoes na mesma tecla: a segunda venceria em silencio e a
            ; primeira pareceria quebrada. Recusa antes de gravar qualquer coisa.
            if usadas.Has(t) {
                aviso.Opt("c" COR_MA)
                aviso.Value := "a tecla " nomeDaTecla(t) " esta' em DUAS sessoes — "
                             . "cada uma precisa da sua"
                return
            }
            usadas[t] := c.chave
        }
        for c in campos
            gravarTecla(c.chave, c.ctl.Value)
        g.Destroy()
        avisoRapido("teclas salvas")
    }

    g.AddButton("w150 h30 x" (18 + LARG_UI - 150) " y+12 Default", "Salvar")
     .OnEvent("Click", salvar)
    g.AddButton("w110 h30 x" (18 + LARG_UI - 270) " yp", "Cancelar")
     .OnEvent("Click", (*) => g.Destroy())
    g.Show()
}

; ⚠️ usado so' para MARCAR no seletor qual linha e' bancada
bancadaGravada(lista) {
    for b in bancadasVivas()
        for s in lista
            if (s.hwnd = b.h1)
                return b.h1
    return 0
}

; =============================================================================
;  ⭐⭐ O SELETOR (reescrito em 2026-08-11)
; =============================================================================
; ⛔ A versao anterior era uma caixa de texto pedindo um NUMERO, e o operador
; disse na cara: *"nao to entendendo esse ui ux, esta confuso"*. Ele tinha razao,
; e o print mostra por que: depois do F3 a sessao tem TRES janelas com o MESMO
; TITULO, entao a lista trazia "CTA - 03 Neusa" tres vezes, identicas, e nada no
; texto dizia qual era qual. Pedir um numero sobre linhas indistinguiveis nao e'
; escolha, e' sorteio — e o premio de errar e' rodar o piloto na bancada errada.
;
; ⭐ O CONSERTO NAO E' "DEIXAR MAIS BONITO", E' DAR AS COLUNAS QUE SEPARAM:
;   Onde ....... em que monitor a janela esta' (o F3 poe a bancada e o dashboard
;                em telas diferentes, entao esta coluna sozinha ja' desempata)
;   Tamanho .... a geometria de verdade
;   Serve? ..... o VEREDITO ANTECIPADO da trava do F10. E' a coluna mais util da
;                tela: diz quais janelas o piloto aceita ANTES de tentar.
;   F3 ......... qual foi montada pelo F3, agora sobrevivendo a reinicio
;
; ⭐ E clicar substitui digitar. O botao MOSTRAR JANELA pisca a selecionada — com
; tres titulos iguais, ver e' a unica prova.
escolherSessao() {
    global INI, SESSOES_ESPERADAS, gBancada
    lista := listarSessoes()
    if (lista.Length = 0) {
        MsgBox("Nenhuma sessao aberta.`n`nAbra o perfil no Dolphin (ou a aba "
               "da AdBatch no Chrome) e rode de novo.", APP, 48)
        return 0
    }
    if (gBancada = 0)
        gBancada := bancadaGravada(lista)

    ; ⛔ ORDEM DA LISTA = ORDEM DE UTILIDADE, nao ordem de descoberta: a bancada
    ; do F3 primeiro, depois as que servem, e por ultimo as que o F10 recusaria.
    ordem := []
    for s in lista {
        s.onde   := monitorDaJanela(s.hwnd)
        s.serve  := serveParaOF10(s.hwnd)
        s.eF3    := (s.hwnd = gBancada)
        ; ⚠️ ordena por VEREDITO, nao pela string exata: os rotulos ja' mudaram
        ; uma vez, e uma comparacao literal viraria ordenacao morta em silencio.
        s.peso   := s.eF3 ? 0
                    : (SubStr(s.serve, 1, 3) = "NAO") ? 3
                    : (s.serve = "SIM" || s.serve = "provavel") ? 1
                    : 2
        WinGetPos , , &sw, &sh, "ahk_id " s.hwnd
        s.tam := sw "x" sh
        ordem.Push(s)
    }
    loop ordem.Length - 1 {          ; ordenacao simples: a lista tem ~6 itens
        i := A_Index
        loop ordem.Length - i {
            j := A_Index
            if (ordem[j].peso > ordem[j + 1].peso) {
                tmp := ordem[j], ordem[j] := ordem[j + 1], ordem[j + 1] := tmp
            }
        }
    }

    g := janelaUI("em qual janela rodar")
    secaoUI(g, "Escolha a janela do AdBatch", true)
    g.AddText("w" LARG_UI " c" COR_FRACA,
              "Depois do F3 a sessao tem varias janelas com o MESMO nome. "
              "As colunas abaixo sao o que as separa — em duvida, use MOSTRAR JANELA.")
    lv := escurecerUI(g.AddListView("w" LARG_UI " r8 -Multi +Grid y+8" fundoUI(),
                        ["Sessao", "Tipo", "Onde", "Tamanho", "Serve para o F10?", "F3"]))
    for s in ordem {
        lv.Add("", s.titulo, s.tipo,
               (s.onde ? "monitor " s.onde : "?"),
               s.tam, s.serve, (s.eF3 ? "bancada" : ""))
    }
    lv.ModifyCol(1, LARG_UI - 452), lv.ModifyCol(2, 62), lv.ModifyCol(3, 78)
    lv.ModifyCol(4, 88),  lv.ModifyCol(5, 148), lv.ModifyCol(6, 62)
    lv.Modify(1, "Select Focus Vis")     ; ⭐ a primeira ja' e' a mais provavel

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
        txtF := ""
        for nome in fechadas
            txtF .= (txtF = "" ? "" : "   ·   ") nome
        g.AddText("w" LARG_UI " y+10 c" COR_FRACA,
                  "fechadas (abra no Dolphin para usar):   " txtF)
    }

    escolhido := 0
    ; ⭐ mesma gramatica da tela do F3: acoes a' direita, a principal por ultimo
    bRodar   := g.AddButton("w150 h30 x" (18 + LARG_UI - 150) " y+14 Default", "Rodar aqui")
    g.AddButton("w110 h30 x" (18 + LARG_UI - 270) " yp", "Cancelar").OnEvent("Click", (*) => g.Destroy())
    bMostrar := g.AddButton("w150 h30 x18 yp", "Mostrar janela")

    ; ⭐ PISCA A JANELA SELECIONADA. Com tres titulos iguais na tela, nenhuma
    ; descricao textual convence — ver a janela vir para a frente convence.
    mostrar(*) {
        r := lv.GetNext()
        if (r = 0)
            return
        h := ordem[r].hwnd
        if !WinExist("ahk_id " h)
            return MsgBox("essa janela ja' foi fechada", APP, 48)
        WinActivate "ahk_id " h
        Sleep 1100
        WinActivate "ahk_id " g.Hwnd
    }
    rodar(*) {
        r := lv.GetNext()
        if (r = 0)
            return MsgBox("Clique numa linha primeiro.", APP, 48)
        if !WinExist("ahk_id " ordem[r].hwnd)
            return MsgBox("essa janela ja' foi fechada", APP, 48)
        escolhido := ordem[r].hwnd
        g.Destroy()
    }
    bMostrar.OnEvent("Click", mostrar)
    bRodar.OnEvent("Click", rodar)
    lv.OnEvent("DoubleClick", rodar)
    g.OnEvent("Close", (*) => g.Destroy())
    g.Show()
    WinWaitClose "ahk_id " g.Hwnd
    return escolhido
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
    cw := IniRead(INI, secPontos(), "calib_w", "")
    ch := IniRead(INI, secPontos(), "calib_h", "")
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
                    APP " — geometria", 4 + 48)
        if (r != "Yes")
            throw Error("cancelado — rode o F9 nesta janela")
        IniWrite w, INI, secPontos(), "calib_w"
        IniWrite h, INI, secPontos(), "calib_h"
        IniWrite WinGetTitle("ahk_id " hwnd), INI, secPontos(), "calib_janela"
        return
    }
    if (Abs(w - Integer(cw)) > 8 || Abs(h - Integer(ch)) > 8)
        throw Error("a janela esta' " w "x" h " e a calibracao foi feita em "
                    cw "x" ch ". Os cliques cairiam fora do alvo. "
                    "Maximize a janela nesta mesma tela, ou rode o F9 aqui.")

    ; ⛔⛔ TAMANHO IGUAL NAO E' TELA IGUAL. Medido em 2026-08-11, depois de
    ; o operador ver o ponteiro errar numa janela e acertar noutra: as janelas do
    ; Dolphin mostravam a BARRA DE FAVORITOS e a do Chrome principal nao, e isso
    ; empurra a pagina inteira 34px para baixo. As duas janelas tinham EXATAMENTE
    ; 1936x1048 — a trava de geometria passava, e todo clique caia 34px fora, em
    ; silencio, gastando credito.
    ;
    ; ⭐ O ponto do `Gerar` distingue sozinho: e' um botao BRANCO na tela certa
    ; e fundo de pagina na errada. Medido: (255,255,255) contra (14,14,14).
    ; ⚠️ Tolerancia larga (80 por canal): o que se quer separar sao dois
    ; extremos, e apertar isso transformaria um realce de foco em falso alarme.
    cg := IniRead(INI, secPontos(), "cor_gerar", "")
    if (cg != "") {
        try {
            pg := lerPonto("cr_gerar")
            atual := PixelGetColor(pg.x, pg.y)
            d := 0
            loop 3 {
                i := (A_Index - 1) * 8
                d := Max(d, Abs(((atual >> i) & 0xFF) - ((Integer(cg) >> i) & 0xFF)))
            }
            if (d > 80)
                throw Error("a tela nao esta' igual a' da calibracao: no ponto do "
                            "botao Gerar eu esperava a cor " Format("0x{:06X}", Integer(cg))
                            " e encontrei " Format("0x{:06X}", atual) ".`n`n"
                            "A causa mais comum e' a BARRA DE FAVORITOS: com ela "
                            "a pagina desce ~34px, e a janela continua do mesmo "
                            "tamanho — os cliques cairiam todos fora.`n`n"
                            "Deixe as janelas iguais (barra em todas ou em "
                            "nenhuma) e rode o F9.")
        }
    }
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
; ⛔ O id do AdBatch saiu daqui e virou `toolAdbatch()`, que escolhe pelo
; formato. O do Montador continua unico ate' medicao em contrario.
TOOL_MONTADOR := "0a949867-f37f-4808-b178-4478edc7b5ad"

; ⛔ Aceita QUALQUER url do Flow que carregue um id de projeto — dashboard,
; AdBatch ou Montador. O operador nao deveria ter de saber qual delas colar.
idDoProjeto(url) {
    if RegExMatch(url, "i)project/([0-9a-fA-F\-]{30,40})", &m)
        return m[1]
    return ""
}

urlsDaBancada(pid) {
    global FLOW_BASE, TOOL_MONTADOR
    return {adbatch:  FLOW_BASE pid "/tool/" toolAdbatch(),
            dash:     FLOW_BASE pid,
            montador: FLOW_BASE pid "/tool/" TOOL_MONTADOR}
}

; ⛔ Abre uma aba e navega. `Ctrl+L` antes de digitar: a aba nova ja' nasce com
; a barra de endereco focada, mas isso e' COMPORTAMENTO e nao contrato — e uma
; aba que receba o texto no lugar errado vira uma BUSCA, nao uma navegacao.
;
; ⛔⛔ O `{Delete}` ANTES DO `{Enter}` NAO E' PARANOIA — e' o conserto de um
; defeito medido em campo (2026-08-11, sessao CTA-03 Neusa): a janela 2 abriu 5
; abas do ADBATCH onde devia abrir o dashboard.
;
; A causa e' o AUTOCOMPLETE INLINE do Chrome, e a prova esta' na forma das urls:
;   dash    = .../project/<pid>
;   adbatch = .../project/<pid>/tool/d882542c-...
; a url do dashboard e' PREFIXO ESTRITA da do AdBatch, e e' a UNICA das tres com
; essa propriedade — exatamente a unica que falhou. Digitado o prefixo, o Chrome
; pendura `/tool/d882542c-...` como texto SELECIONADO (aquela url tinha acabado
; de ser visitada DEZ vezes, entao era o match campeao) e o `Enter` navega para o
; COMPLETADO, nao para o digitado.
;
; `{Delete}` apaga a selecao pendurada. Se nao houver nada pendurado, o cursor
; esta' no fim e a tecla nao faz nada — e' seguro em toda url.
abrirAba(url, nova := true) {
    if nova {
        Send "^t"
        pausa(700, 180)
    }
    Send "^l"
    pausa(260, 90)
    SendText url
    pausa(320, 110)      ; ⚠️ tempo para o autocomplete APARECER — apagar antes
                         ; de ele existir deixaria a armadilha de pe'
    Send "{Delete}"
    pausa(180, 70)
    Send "{Enter}"
    pausa(1400, 350)
}

; =============================================================================
;  ⭐⭐ POSICIONAMENTO NOS DOIS MONITORES (2026-08-11)
; =============================================================================
; Encomenda do operador, com a bancada montada a mao na frente dele: *"a janela
; 2 fica full screen no meu segundo monitor vertical, a janela 1 full screen no
; monitor 1 horizontal"*.
;
; ⛔ NAO SE FIXA MONITOR POR NUMERO. A numeracao do Windows muda quando se troca
; um cabo de porta, e um numero trocado joga as dez abas do AdBatch no monitor de
; RETRATO — onde a calibracao do F10 nao vale e os cliques cairiam fora do alvo.
; A escolha e' por PROPRIEDADE:
;   janela 1 ... o monitor cuja area util casa com o TAMANHO DA CALIBRACAO
;                (`calib_w` x `calib_h`). E' a definicao mais forte que existe:
;                e' literalmente a tela onde os 6 pontos foram apontados. Sem
;                calibracao gravada, cai para o monitor em PAISAGEM.
;   janela 2 ... o monitor em RETRATO (altura > largura).
;
; Medido nesta maquina em 2026-08-11:
;   monitor 1 ... 1920x1080 paisagem, util 1920x1032, primario
;   monitor 2 ... 1080x1920 RETRATO em (1920,-401)
; e o .ini confirma que a calibracao foi feita no horizontal: o ponto mais
; distante e' (1171, 772), que so' cabe na area util do monitor 1.
;
; ⚠️ Da' para mandar na marra pelo INI, se um dia a heuristica errar:
;   [config] monitor_adbatch=1 · monitor_dash=2   (0 = automatico)

; ⛔⛔ A TOLERANCIA DE 24 NAO E' CHUTE — E' A BORDA DA JANELA MAXIMIZADA, MEDIDA.
; O `calib_w`/`calib_h` vem do `WinGetPos` (ver a calibrar()), e uma janela
; MAXIMIZADA reporta a area util MAIS a moldura invisivel de redimensionamento:
;     MonitorGetWorkArea .... 1920 x 1032
;     WinGetPos maximizada .. 1936 x 1048      (medido em 2026-08-11)
; sao 16px em cada eixo. Com a tolerancia de 12 que estava aqui, o criterio
; PRINCIPAL da janela 1 nunca casaria e cairia calado no fallback de paisagem —
; nesta maquina daria o mesmo monitor, e o defeito so' apareceria em outra.
; ⚠️ Comparacao larga nao confunde monitor: 1920x1032 e 1080x1920 estao a
; centenas de pixels de distancia.
monitorPorTamanho(w, h) {
    if (w = "" || h = "")
        return 0
    loop MonitorGetCount() {
        MonitorGetWorkArea(A_Index, &l, &t, &r, &b)
        if (Abs((r - l) - Integer(w)) <= 24 && Abs((b - t) - Integer(h)) <= 24)
            return A_Index
    }
    return 0
}

; ⛔⛔ O MONITOR DOS PONTOS — a evidencia mais forte que existe, e a que
; faltava (2026-08-11, depois de o operador reportar: *"deu um bug no script que
; ele trocou a janela 2 pro monitor 1 e a janela 1 pro monitor 2 vertical"*).
;
; O `.ini` dele estava assim:
;     cr_slot2_x=1054      <- os pontos no monitor 1 (0..1920)
;     calib_w=1096  calib_h=1936   <- a geometria da janela VERTICAL
; Os dois apontavam para monitores DIFERENTES, e quem decidia era o TAMANHO:
; 1096x1936 casa com o monitor 2, entao o AdBatch foi para o vertical e o
; dashboard para o horizontal. A troca exata que ele viu.
;
; ''' + E + ''' Os pontos calibrados sao coordenadas de TELA: o monitor que os contem E'
; o monitor onde ele calibrou. Nao e' proxy, nao e' heuristica — e' o dado.
; Por isso ele passa a ser o PRIMEIRO criterio, antes do tamanho da janela.
monitorDosPontos() {
    global INI, ALVOS
    votos := Map()
    for a in ALVOS {
        px := IniRead(INI, secPontos(), a[1] "_x", "")
        py := IniRead(INI, secPontos(), a[1] "_y", "")
        if (px = "" || py = "")
            continue
        loop MonitorGetCount() {
            MonitorGetWorkArea(A_Index, &l, &t, &r, &b)
            if (px >= l && px <= r && py >= t && py <= b) {
                votos[A_Index] := votos.Has(A_Index) ? votos[A_Index] + 1 : 1
                break
            }
        }
    }
    ; ''' + A + ''' por MAIORIA, nao pelo primeiro: um ponto isolado fora da janela
    ; (clique errado numa calibracao antiga) nao pode decidir sozinho.
    melhor := 0, maior := 0
    for m, n in votos {
        if (n > maior) {
            maior := n
            melhor := m
        }
    }
    return melhor
}

; ''' + X + ''' A janela que esta' SOB uma coordenada de tela. E' assim que a calibracao
; passa a saber de qual janela gravar o tamanho, em vez de perguntar qual esta'
; ativa — pergunta cuja resposta muda se o operador clicar em qualquer lugar
; antes de terminar.
janelaDoPonto(x, y) {
    h := DllCall("WindowFromPoint", "Int64", (y << 32) | (x & 0xFFFFFFFF), "Ptr")
    if !h
        return 0
    return DllCall("GetAncestor", "Ptr", h, "UInt", 2, "Ptr")   ; GA_ROOT
}

monitorPorForma(retrato) {
    loop MonitorGetCount() {
        MonitorGetWorkArea(A_Index, &l, &t, &r, &b)
        if (((b - t) > (r - l)) = retrato)
            return A_Index
    }
    return 0
}

; ⛔⛔ RESTAURA ANTES DE MOVER. Uma janela MAXIMIZADA ignora o WinMove: ela
; pertence ao monitor em que foi maximizada, e mover sem restaurar nao a tira de
; la'. Restaurar -> mover -> maximizar de novo e' a unica ordem que funciona.
mandarPara(hwnd, mon) {
    if (mon = 0 || !WinExist("ahk_id " hwnd))
        return false
    MonitorGetWorkArea(mon, &l, &t, &r, &b)
    WinRestore "ahk_id " hwnd
    Sleep 260
    ; ⚠️ a folga de 30px e' para a janela cair INTEIRA dentro do monitor alvo —
    ; o WinMaximize maximiza no monitor onde esta' a MAIOR PARTE dela, entao uma
    ; janela a cavalo entre as duas telas voltaria para a errada.
    WinMove l + 30, t + 30, (r - l) - 60, (b - t) - 60, "ahk_id " hwnd
    Sleep 260
    WinMaximize "ahk_id " hwnd
    Sleep 300
    return true
}

; ⛔ Resolve os dois indices de uma vez, porque a regra "nao deixar as duas no
; MESMO monitor" so' existe olhando o par — decidir uma de cada vez empilharia
; as duas na mesma tela numa maquina de monitor unico sem ninguem perceber.
monitoresDaBancada() {
    global INI
    m1 := Integer(IniRead(INI, "config", "monitor_adbatch", "0"))
    m2 := Integer(IniRead(INI, "config", "monitor_dash", "0"))
    if (m1 = 0) {
        ; ⛔⛔ OS PONTOS PRIMEIRO. O tamanho da janela e' proxy; os pontos
        ; sao o dado. Quando os dois discordam — e discordaram, no dia em que
        ; isto foi escrito — quem manda e' onde os cliques vao cair.
        m1 := monitorDosPontos()
        if (m1 = 0)
            m1 := monitorPorTamanho(IniRead(INI, secPontos(), "calib_w", ""),
                                    IniRead(INI, secPontos(), "calib_h", ""))
        if (m1 = 0)
            m1 := monitorPorForma(false)
        if (m1 = 0)
            m1 := 1
    }
    if (m2 = 0)
        m2 := monitorPorForma(true)
    ; ⚠️ Monitor unico, ou os dois caindo no mesmo: pega qualquer outro. Se nao
    ; houver outro, deixa as duas juntas — empilhado e' ruim, mas montar nao e'
    ; pior do que nao montar.
    if (m2 = 0 || m2 = m1) {
        m2 := 0
        loop MonitorGetCount() {
            if (A_Index != m1) {
                m2 := A_Index
                break
            }
        }
        if (m2 = 0)
            m2 := m1
    }
    return [m1, m2]
}

; =============================================================================
;  ⭐⭐ F4 + CLIQUE NO ICONE — LEVANTAR A BANCADA INTEIRA (2026-08-11)
; =============================================================================
; Ordem do operador: *"quando o script estiver de standby, de uma acao de um
; clique unico no icone do navegador de determinada sessao logada, fazer abrir
; simultaneamente a janela 1 e 2 daquela sessao nos seus respectivos monitores"*
; — e, na mesma mensagem: *"pode colocar as duas rotas, por clique no icone e por
; apertar o F4"*.
;
; ⛔ NAO DA' PARA OUVIR O CLIQUE NO BOTAO DA BARRA DE TAREFAS: aquele botao e' do
; Explorer, nao do navegador. O que da' — e produz o MESMO efeito — e' ouvir a
; consequencia dele: clicar no icone ATIVA a janela, e o Windows avisa quem
; estiver registrado como shell hook.
;
; ⛔⛔ E A REGRA QUE IMPEDE ISSO DE VIRAR PRAGA: so' age se a irma estiver
; MINIMIZADA ou FORA DE LUGAR. Sem esta condicao, alternar entre as duas janelas
; da bancada com alt-tab traria a outra para a frente toda vez, e o operador
; perderia o controle de qual janela esta' vendo. Levantar a bancada e' o caso em
; que as janelas estao guardadas; com tudo ja' no lugar, o certo e' nao fazer
; nada.
;
; ⚠️ Tres guardas, cada uma por um motivo diferente:
;   `rodando` ........ nunca durante um F10/F3. Ele pediu "em standby".
;   `gArrumando` ..... reentrancia: arrumar ATIVA janela, ativar dispara o hook
;                      de novo, e sem esta trava as duas ficariam se chamando.
;   carencia ......... o Windows manda mais de um evento por clique.

global gArrumando := false
global gUltimoArrumo := 0
global MSG_SHELL := 0

; ⛔ Uma janela so' esta' "em ordem" se estiver MAXIMIZADA no monitor dela. O
; minimizado (-1) e' o caso do clique no icone; o monitor errado e' o caso de
; quem arrastou a janela sem querer.
precisaArrumar(hwnd, mon) {
    if !WinExist("ahk_id " hwnd)
        return false
    if (WinGetMinMax("ahk_id " hwnd) != 1)
        return true
    return (monitorDaJanela(hwnd) != mon)
}

; ⛔⛔ QUAIS BANCADAS ESTAO NO MONITOR ERRADO (2026-08-11).
; Nasceu do relato dele: *"eu to clicando na parte superior da janela que ta na
; vertical e ela ta se movendo sozinha pro monitor horizontal"*. Nao era bug
; novo — era a correcao da calibracao agindo sobre uma bancada montada ANTES
; dela, com a janela 1 no monitor errado. Comportamento certo, e assustador: ele
; so' descobria clicando.
;
; ⚠️ MINIMIZADA NAO E' "FORA DO LUGAR". Janela minimizada reporta posicao
; (-32000,-32000) e cairia em todo aviso, todo dia, ate' o aviso virar ruido —
; e aviso que sempre acende nao avisa nada.
foraDoLugar(h, m) {
    if !WinExist("ahk_id " h)
        return false
    if (WinGetMinMax("ahk_id " h) = -1)
        return false
    md := monitorDaJanela(h)
    return (md != 0 && md != m)
}

bancadasForaDoLugar() {
    mons := monitoresDaBancada()
    fora := []
    for b in bancadasVivas()
        if (foraDoLugar(b.h1, mons[1]) || foraDoLugar(b.h2, mons[2]))
            fora.Push(b.chave)
    return fora
}

; ⛔⛔ REGRA CORRIGIDA EM CAMPO (2026-08-11): *"infelizmente o mecanismo de abrir
; as duas janelas da sessao de uma vez so' nao funciona"*.
;
; A versao anterior so' agia se a irma estivesse MINIMIZADA ou FORA DE LUGAR, e
; saia calada quando as duas estavam "no lugar". Medido no uso real: as janelas
; dele NAO estao minimizadas — estao maximizadas, cada uma no seu monitor, apenas
; ATRAS de outras. A regra concluia "esta' tudo certo" e nao fazia nada. Todos os
; outros elos estavam bons (o par gravado, o hook registrado, 10 ativacoes
; recebidas, o lParam batendo): o unico que reprovava era a minha guarda.
;
; ⭐ E o incomodo que aquela guarda evitava NAO EXISTE NESTE LAYOUT. As duas
; janelas ficam em MONITORES DIFERENTES — trazer a irma para a frente nunca cobre
; a que ele clicou. A guarda resolvia um problema que a geometria ja' resolvia.
;
; ⚠️ O que ficou da ideia original e' so' a ECONOMIA: janela ja' maximizada e no
; monitor certo e' apenas ERGUIDA na ordem Z (`WinMoveTop`), sem restaurar, sem
; mover e sem roubar o foco. O caminho caro (restaurar -> mover -> maximizar)
; ficou para quem esta' minimizada ou fora de lugar.
arrumarBancada(b, hFoco := 0) {
    global gArrumando, gUltimoArrumo
    if (b = 0)
        return false
    mons := monitoresDaBancada()
    gArrumando := true
    try {
        for par in [[b.h1, mons[1]], [b.h2, mons[2]]] {
            h := par[1], m := par[2]
            if !WinExist("ahk_id " h)
                continue
            if precisaArrumar(h, m)
                mandarPara(h, m)
            else
                try WinMoveTop "ahk_id " h      ; ergue sem tirar o foco de nada
        }
        ; ⭐ o foco termina na janela que ELE clicou, nunca na irma
        alvo := (hFoco && WinExist("ahk_id " hFoco)) ? hFoco : b.h1
        WinActivate "ahk_id " alvo
    } finally {
        gArrumando := false
        gUltimoArrumo := A_TickCount
    }
    return true
}

; ⚠️ HSHELL_WINDOWACTIVATED (4) e HSHELL_RUDEAPPACTIVATED (32772). O segundo e' o
; que chega quando a janela vem de MINIMIZADA — que e' justamente o clique no
; icone. Ouvir so' o primeiro deixaria o caso principal de fora.
aoAtivarJanela(wParam, lParam, *) {
    global rodando, gArrumando, gUltimoArrumo
    if (wParam != 4 && wParam != 32772)
        return
    if (rodando || gArrumando)
        return
    if (A_TickCount - gUltimoArrumo < 1500)
        return
    b := parDaJanela(lParam)
    if (b = 0)
        return
    arrumarBancada(b, lParam)
}

ligarCliqueNoIcone() {
    global INI, MSG_SHELL
    if (IniRead(INI, "config", "clique_no_icone", "1") = "0")
        return false
    ; ⚠️ registra a JANELA DO PROPRIO SCRIPT para receber os avisos do shell
    if !DllCall("RegisterShellHookWindow", "Ptr", A_ScriptHwnd)
        return false
    MSG_SHELL := DllCall("RegisterWindowMessage", "Str", "SHELLHOOK", "UInt")
    OnMessage(MSG_SHELL, aoAtivarJanela)
    return true
}

; ⭐ A rota do teclado. Arruma a bancada da janela ATIVA; se a ativa nao for de
; bancada nenhuma, oferece a lista em vez de errar calado.
levantarBancada() {
    global rodando
    if rodando
        return
    b := parDaJanela(WinExist("A"))
    if (b = 0) {
        vivas := bancadasVivas()
        if (vivas.Length = 0) {
            MsgBox("Nenhuma bancada montada ainda.`n`nRode o F3 numa sessao "
                   "para montar as duas janelas — dai o F4 passa a levanta-las.",
                   APP, 48)
            return
        }
        if (vivas.Length = 1) {
            b := vivas[1]
        } else {
            h := escolherSessao()
            if (h = 0)
                return
            b := parDaJanela(h)
            if (b = 0) {
                MsgBox("Essa janela nao faz parte de uma bancada do F3.",
                       APP, 48)
                return
            }
        }
    }
    arrumarBancada(b, WinExist("A"))
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

    ; ⛔⛔ TELA REFEITA EM 2026-08-11, segunda ordem do operador sobre a MESMA
    ; janela: *"eu te pedi pra melhorar a ui ux de TODAS as janelas interfaces do
    ; script, vc ainda deixou essa daqui crua, confusa"*. Ele estava certo — eu
    ; tinha refeito o seletor e a ajuda e deixado justamente a PRIMEIRA tela que
    ; ele ve'.
    ;
    ; O que estava errado, e nao era enfeite:
    ;   · o campo da url nao tinha rotulo nenhum, so' uma caixa fina
    ;   · a explicacao era um paragrafo cinza — texto corrido nao se le' na hora
    ;     de agir, se pula
    ;   · o preview ficava VAZIO ate' colar alguma coisa, entao metade da janela
    ;     era um retangulo branco sem funcao aparente
    ;   · nada dizia o que faltava para o botao servir
    ;
    ; ⭐ Agora o plano da montagem e' uma TABELA que ja' nasce preenchida com o
    ; que e' fixo (janela, monitor, quantas abas, qual ferramenta) e completa a
    ; coluna da URL conforme ele cola. A tela ensina o que vai acontecer mesmo
    ; com o campo vazio — e o preview deixou de ser um vazio a ser preenchido
    ; para ser uma linha a ser conferida.
    mPrev := monitoresDaBancada()
    g := janelaUI("montar bancada")
    secaoUI(g, "1 · a url do projeto desta sessao", true)
    g.AddText("w" LARG_UI " c" COR_FRACA,
              "Serve QUALQUER uma: o dashboard, a AdBatch ou o Montador. "
              "So' o projeto e' lido — as tres urls sao reconstruidas daqui.")
    fonteUI(g, "s10", "Consolas")
    eUrl := escurecerUI(g.AddEdit("w" LARG_UI " r1 y+6" fundoUI()))
    fonteUI(g)
    aviso := g.AddText("w" LARG_UI " y+6 c" COR_MA, "cole uma url para liberar o botao")

    secaoUI(g, "2 · o que vai ser montado")
    lv := escurecerUI(g.AddListView("w" LARG_UI " r3 -Multi +Grid NoSort" fundoUI(),
                        ["Janela", "Onde", "Abas", "Ferramenta", "Url que vai abrir"]))
    lv.Add("", "janela 1", "monitor " mPrev[1], nAd,    nomeFormato(),  "—")
    lv.Add("", "janela 2", "monitor " mPrev[2], nDash,  "dashboard das midias", "—")
    lv.Add("", "janela 2", "monitor " mPrev[2], 1,      "Montador Vertical 2", "—")
    lv.ModifyCol(1, 66), lv.ModifyCol(2, 68), lv.ModifyCol(3, 42)
    lv.ModifyCol(4, 138), lv.ModifyCol(5, LARG_UI - 336)

    g.AddText("w" LARG_UI " y+12 c" COR_FRACA,
              "As duas janelas nascem NOVAS e maximizadas. "
              "O F10 continua sendo o gatilho da geracao.")

    ; ⭐ botoes a' direita, com a acao principal por ultimo — e' onde a mao vai
    bOk := g.AddButton("w160 h30 x" (18 + LARG_UI - 160) " y+14 Default", "Montar bancada")
    g.AddButton("w110 h30 x" (18 + LARG_UI - 280) " yp", "Cancelar").OnEvent("Click", (*) => g.Destroy())

    ; ⭐ O PREVIEW E' A DEFESA CONTRA ABRIR 16 ABAS ERRADAS: mostra as urls
    ; DERIVADAS antes de qualquer clique. Url errada se ve' aqui, e nao depois
    ; de dezesseis abas abertas na sessao errada.
    ;
    ; ⛔ A LINHA DO DASHBOARD FALTAVA AQUI, e essa omissao teve custo: no teste
    ; de campo de 2026-08-11 a UNICA das tres urls que deu errado foi justamente
    ; a que o preview nao mostrava. Defesa que nao cobre todos os itens que ela
    ; defende da' a sensacao de conferencia sem a conferencia.
    atualizar(*) {
        pid := idDoProjeto(eUrl.Value)
        if (pid = "") {
            vazio := (Trim(eUrl.Value) = "")
            aviso.Opt("c" COR_MA)
            aviso.Value := vazio ? "cole uma url para liberar o botao"
                                 : "nao achei um id de projeto nessa url — nao vou abrir nada"
            loop 3
                lv.Modify(A_Index, "Col5", "—")
            bOk.Enabled := false
            return
        }
        u := urlsDaBancada(pid)
        aviso.Opt("c" COR_BOA)
        aviso.Value := "projeto " pid
        lv.Modify(1, "Col5", u.adbatch)
        lv.Modify(2, "Col5", u.dash)
        lv.Modify(3, "Col5", u.montador)
        bOk.Enabled := true
    }
    eUrl.OnEvent("Change", atualizar)
    bOk.Enabled := false        ; ⛔ nasce travado: sem url, montar nao faz sentido

    escolhido := ""
    bOk.OnEvent("Click", (*) => (escolhido := eUrl.Value, g.Destroy()))
    g.OnEvent("Close", (*) => g.Destroy())
    g.Show()
    WinWaitClose "ahk_id " g.Hwnd

    if (Trim(escolhido) = "")
        return
    pid := idDoProjeto(escolhido)
    if (pid = "")
        return MsgBox("Nao achei um id de projeto nessa url.", APP, 48)
    u := urlsDaBancada(pid)

    hBase := escolherSessao()
    if (hBase = 0)
        return
    if !WinExist("ahk_id " hBase)
        return MsgBox("a janela escolhida sumiu", APP, 16)
    WinActivate "ahk_id " hBase
    if !WinWaitActive("ahk_id " hBase, , 4)
        return MsgBox("nao consegui ativar a sessao", APP, 16)

    anotar("montando bancada — projeto " pid " em " WinGetTitle("ahk_id " hBase))

    mons := monitoresDaBancada()

    hJan1 := novaJanela(hBase)
    if (hJan1 = 0)
        return MsgBox("nao consegui abrir a janela 1", APP, 16)
    ; ⭐ POSICIONA ANTES DE ABRIR AS ABAS, nao depois: assim o operador ve' a
    ; bancada nascer no lugar certo, e nao dez abas surgirem na tela errada para
    ; so' entao pularem de monitor.
    mandarPara(hJan1, mons[1])
    WinActivate "ahk_id " hJan1
    WinWaitActive "ahk_id " hJan1, , 3
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
            return MsgBox("nao consegui abrir a janela 2", APP, 16)
        mandarPara(hJan2, mons[2])
        WinActivate "ahk_id " hJan2
        WinWaitActive "ahk_id " hJan2, , 3
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
        ; ⚠️ REAFIRMA o lugar da janela 2. Abrir seis abas pode ter tirado o
        ; foco dela; maximizar de novo custa nada e garante o full screen que o
        ; operador pediu no monitor de retrato.
        mandarPara(hJan2, mons[2])
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
    ; ⚠️ TAMBEM NO DISCO, E COMO PAR: o handle em memoria morre quando o script e'
    ; reiniciado — e reiniciar e' exatamente o que o operador faz depois de cada
    ; versao nova. Foi assim que a marca sumiu do seletor no primeiro uso real.
    ; ⭐ Gravado com o TITULO DA SESSAO como chave, uma chave por sessao: e' o que
    ; faz o F4 e o clique no icone servirem para quantas contas ele abrir.
    ; ⛔ Grava pela `chaveDaSessao`, NAO pelo titulo cru. Numa bancada montada no
    ; Chrome o titulo e' o da aba ativa e muda no minuto seguinte — a bancada
    ; ficaria gravada sob um nome que nunca mais bate, e a tecla dela nunca
    ; acharia a sessao.
    tituloSessao := chaveDaSessao(hBase)
    gravarBancada(tituloSessao, hJan1, hJan2)
    ; ⭐ a tecla da sessao nasce JUNTO com a bancada, e e' anunciada no fim:
    ; atalho que ninguem contou que existe nao existe.
    tSessao := garantirTecla(tituloSessao)

    ; ⚠️ CONFERE A JANELA 1 CONTRA A CALIBRACAO E AVISA AQUI. O F10 ja' tem a
    ; trava de geometria, mas ela dispara la' na frente, com o roteiro colado e a
    ; geracao prestes a comecar. Descobrir agora, com a bancada recem montada,
    ; custa um clique; descobrir depois custa a rodada.
    aviso := ""
    cw := IniRead(INI, secPontos(), "calib_w", "")
    ch := IniRead(INI, secPontos(), "calib_h", "")
    WinGetPos , , &w1, &h1, "ahk_id " hJan1
    ; ⛔⛔ AS CHAVES E O PONTO SAO O CONSERTO DE UM ERRO QUE QUEBROU EM CAMPO
    ; (2026-08-11, primeira montagem boa do F3). A versao anterior quebrava a
    ; string em duas linhas SEM o operador `.` e SEM chaves, e isso produziu
    ; DOIS defeitos de uma tacada so':
    ;   1. o AHK v2 leu a segunda linha como CHAMADA DE FUNCAO — `cw("x" ch ...)`
    ;      — e estourou "This value of type String has no method named Call";
    ;   2. sem chaves, o `if` governava so' a primeira linha, entao a segunda
    ;      rodava SEMPRE, houvesse calibracao ou nao.
    ; ⚠️ E O TESTE DE CARGA NAO PEGOU: aquilo era sintaticamente VALIDO (chamar
    ; funcao e' legitimo), so' quebrava na EXECUCAO. Carregar valida SINTAXE, nao
    ; SEMANTICA — declarar "as 1083 linhas parseiam" nao e' declarar que rodam.
    if (cw != "" && ch != "" && (Abs(w1 - Integer(cw)) > 8 || Abs(h1 - Integer(ch)) > 8)) {
        aviso := "`n`nATENCAO: a janela 1 esta' " w1 "x" h1 " e a calibracao foi feita em "
               . cw "x" ch ". O F10 vai abortar — rode o F9 nesta janela."
    }

    anotar("bancada montada: janela1=" hJan1 " (" nAd " abas AdBatch, monitor "
           mons[1] ", " w1 "x" h1 "), janela2=" hJan2 " (monitor " mons[2] ")")
    tecla := (tSessao != "")
             ? ("`n`nTecla desta sessao: " nomeDaTecla(tSessao)
                "  (levanta as duas janelas de onde voce estiver, e o F2 troca)")
             : ""
    MsgBox("Bancada montada.`n`nJanela 1 — monitor " mons[1] ": " nAd " abas do AdBatch"
           "`nJanela 2 — monitor " mons[2] ": " nDash " abas do dashboard + 1 Montador"
           "`n`nNo F10 ela aparece marcada como montada pelo F3." tecla aviso,
           APP)
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

; =============================================================================
;  ⭐⭐ O STATUS DO WORKER DAS SOBRAS (2026-08-11)
; =============================================================================
; Encomenda do operador: *"quero um feedback visual em ambas as interfaces, do
; editor e do Video Terminator, do status do worker ativo live"* e, na mensagem
; seguinte, o criterio: *"live e funcional"*. Depois: *"gerar ui ux pertinente
; para visualizar backlog em caso de erro do worker, dele nao estar live"* e *"um
; contador de quantos videos foram movidos e a quantidade atual de videos da
; pasta estoque"*.
;
; ⛔ "LIVE" NAO E' "O ARQUIVO EXISTE". O worker publica um estado em
; `%LOCALAPPDATA%\MoverSobras\estado.json` e bate PULSO a cada 45s, separado da
; passada horaria. Se o unico sinal fosse a passada, um worker MORTO pareceria
; vivo por quase uma hora — justamente o intervalo em que esta tela nao poderia
; ser confiada. O corte e' 3 minutos: quatro pulsos perdidos.
;
; ⚠️ Nada aqui sabe ONDE o worker foi instalado. As duas interfaces moram em
; pastas diferentes; o ponto de encontro e' o LOCALAPPDATA, e so'.

ARQ_WORKER := EnvGet("LOCALAPPDATA") "\MoverSobras\estado.json"

; ⚠️ leitura por regex em vez de um parser de JSON: sao seis campos planos e o
; arquivo e' escrito por nos. Trazer um parser inteiro para isto seria pagar
; caro por um problema que nao existe.
estadoWorker() {
    global ARQ_WORKER, COR_FRACA, COR_BOA, COR_MA
    e := {vivo: false, rotulo: "worker das sobras: NAO INSTALADO",
          cor: COR_FRACA, backlog: 0, backlogGb: 0.0, destino: 0,
          movidos: 0, quando: "", dias: []}
    if !FileExist(ARQ_WORKER)
        return e
    j := ""
    try j := FileRead(ARQ_WORKER, "UTF-8")
    if (j = "")
        return e

    num(c) {
        return RegExMatch(j, '"' c '":\s*([-0-9.]+)', &m) ? m[1] : 0
    }
    txt(c) {
        return RegExMatch(j, '"' c '":\s*"([^"]*)"', &m) ? m[1] : ""
    }

    e.backlog   := Integer(num("backlog_arquivos"))
    e.backlogGb := num("backlog_gb")
    e.destino   := Integer(num("no_destino"))
    e.movidos   := Integer(num("movidos_total"))
    bat         := txt("batimento")
    e.quando    := bat != "" ? bat : txt("atualizado")
    resultado   := txt("resultado")

    ; ⛔ o backlog por dia — e' o que a tela de erro mostra
    pos := 1
    while RegExMatch(j, '\{\s*"dia":\s*"([^"]+)",\s*"n":\s*(\d+),\s*"gb":\s*([0-9.]+)',
                     &m, pos) {
        e.dias.Push({dia: m[1], n: Integer(m[2]), gb: m[3]})
        pos := m.Pos + m.Len
    }

    ; ── idade do pulso
    idade := 999999
    if RegExMatch(e.quando, "^(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2})$", &d) {
        carimbo := d[1] d[2] d[3] d[4] d[5] d[6]
        idade := DateDiff(A_Now, carimbo, "Seconds")
    }
    e.vivo := (idade < 180)

    if !e.vivo {
        e.cor := COR_MA
        e.rotulo := "worker das sobras: PARADO"
                  . (e.quando != "" ? "  (ultimo sinal " e.quando ")" : "")
    } else if (resultado = "hd_desconectado") {
        ; ⚠️ vivo e sem HD e' um TERCEIRO estado, nao um erro: ele levou o HD.
        ; Chamar isso de falha treinaria o operador a ignorar o indicador.
        e.cor := "FFB454"
        e.rotulo := "worker das sobras: LIVE, esperando o HD"
    } else {
        e.cor := COR_BOA
        e.rotulo := "worker das sobras: LIVE"
    }
    return e
}

; ⭐ A linha que resume tudo numa frase, para caber na tela de abertura.
resumoWorker() {
    e := estadoWorker()
    return e.rotulo
         . "   ·   " e.destino " no estoque"
         . "   ·   " e.movidos " movidos ate' hoje"
         . (e.backlog ? ("   ·   " e.backlog " esperando") : "   ·   em dia")
}

; =============================================================================
;  ⭐ F7 — O PAINEL DAS SOBRAS
; =============================================================================
; ⛔ Existe para o dia em que o worker NAO estiver live: e' quando saber quanto
; esta' represado, e desde quando, e' a unica informacao que importa. Por isso a
; tela mostra o backlog POR DIA, e nao um total — um total nao diz se o problema
; comecou hoje ou ha' uma semana.
painelSobras(*) {
    global LARG_UI, ARQ_WORKER
    e := estadoWorker()
    g := janelaUI("sobras — worker")

    secaoUI(g, "Estado do worker", true)
    fonteUI(g, "s11 Bold")
    g.SetFont("s11 Bold c" e.cor, "Segoe UI")
    g.AddText("w" LARG_UI, e.rotulo)
    fonteUI(g)
    g.AddText("w" LARG_UI " y+4 c" COR_FRACA,
              "ultimo sinal: " (e.quando = "" ? "nunca" : e.quando)
              . "     ele bate pulso a cada 45s e faz a passada de hora em hora")

    secaoUI(g, "Contadores")
    fonteUI(g, "s9", "Consolas")
    escurecerUI(g.AddEdit("w" LARG_UI " r3 ReadOnly -E0x200 -Wrap" fundoUI(),
          "no estoque (D:\estoque) .. " e.destino " video(s)"
        . "`nmovidos ate' hoje ........ " e.movidos " video(s)"
        . "`nesperando para ir ........ " e.backlog " video(s)  ("
          . e.backlogGb " GB)"))
    fonteUI(g)

    secaoUI(g, e.backlog ? "O que esta' esperando, por dia" : "Backlog")
    if (e.dias.Length = 0) {
        g.AddText("w" LARG_UI " c" COR_BOA,
                  "Nada represado — todas as sobras dos dias anteriores ja' "
                  "estao no HD.")
    } else {
        lv := escurecerUI(g.AddListView("w" LARG_UI " r6 -Multi +Grid NoSort" fundoUI(),
                                        ["Dia", "Sobras", "GB"]))
        for d in e.dias
            lv.Add("", d.dia, d.n, d.gb)
        lv.ModifyCol(1, 160), lv.ModifyCol(2, 90), lv.ModifyCol(3, 90)
    }

    g.AddButton("w110 h30 x" (18 + LARG_UI - 110) " y+16 Default", "Fechar")
     .OnEvent("Click", (*) => g.Destroy())
    g.AddButton("w150 h30 x18 yp", "Abrir o estoque")
     .OnEvent("Click", (*) => Run("explorer.exe D:\estoque"))
    g.AddButton("w170 h30 x+8 yp", "Ver o log do worker")
     .OnEvent("Click", (*) => abrirLogWorker())
    g.Show()
}

abrirLogWorker() {
    global ARQ_WORKER
    j := ""
    try j := FileRead(ARQ_WORKER, "UTF-8")
    if RegExMatch(j, '"log":\s*"([^"]*)"', &m) {
        caminho := StrReplace(m[1], "\\", "\")
        if FileExist(caminho)
            return Run('notepad.exe "' caminho '"')
    }
    MsgBox("nao achei o log do worker", APP, 48)
}

; =============================================================================
;  ⭐⭐ A AJUDA (F1) — 2026-08-11
; =============================================================================
; Ordem do operador, duas mensagens seguidas: *"coloque um ui ux pertinente de
; guia ajuda: mostra um sumario dos atalhos e suas funcoes"* e *"melhore o ui do
; script, esta confuso atualmente"*.
;
; ⛔ O problema nao era falta de tela bonita, era o SCRIPT SER INVISIVEL: sete
; teclas de funcao, nenhuma delas escrita em lugar nenhum, e um comportamento
; novo (o clique no icone) que age sozinho. Ferramenta que so' responde a teclas
; que o operador tem de lembrar de cor obriga a decorar — e o que se decora,
; se esquece na semana seguinte.
;
; ⭐ Por isso a tela tem DUAS metades, e a segunda e' a que faltava em toda parte:
; os atalhos, e O ESTADO ATUAL. Saber que o F9 calibra nao ajuda quem nao sabe se
; ESTA calibrado; saber que o F3 monta nao ajuda quem nao sabe quais bancadas ja'
; existem. Estado visivel e' o que dispensa a pergunta.
;
; ⚠️ E os mesmos comandos foram para o MENU DA BANDEJA. Atalho e' para quem ja'
; sabe; menu e' para quem esta' descobrindo. Os dois apontam para as mesmas
; funcoes — nunca para copias.

; ⭐⭐ OS COMANDOS — E A TECLA DE CADA UM VIROU CONFIGURAVEL (2026-08-15)
; Ordem do operador: *"quero um ui ux pertinente que consiga setar as teclas de
; atalho pra outros valores se eu quiser, tipo se atualmente quiser mudar o F2
; para outra tecla, nao consigo"*.
;
; ⛔ ELE ESTAVA CERTO E O MOTIVO ERA ESTRUTURAL: as teclas de SESSAO ja' eram
; configuraveis desde 2026-08-11 (registro dinamico com `Hotkey()`), e as dos
; COMANDOS eram `F2::` cravado no fim do arquivo — sintaxe de LOAD TIME, que
; nao se remapeia sem editar codigo. Havia dois sistemas de tecla no mesmo
; script, um configuravel e outro nao, e nada anunciava a diferenca.
;
; ⛔⛔ E A TABELA DA AJUDA PASSA A SAIR DAQUI. Antes ela era uma SEGUNDA lista
; escrita a mao, e uma tela de ajuda que anuncia `F10` depois de o operador
; remapear para `Ctrl+F10` e' pior do que nao ter ajuda: ela mente com
; autoridade. Uma fonte, um lugar.
;
; ⚠️ `ctx: true` = so' vale ENQUANTO o ciclo roda (e' o caso do abortar). Sem
; isso o script sequestraria o Esc do Windows inteiro, que foi exatamente o
; motivo do `#HotIf` na versao anterior.
global COMANDOS := [
    {id: "ajuda",    padrao: "F1",  rotulo: "Ajuda",
     detalhe: "esta tela: os atalhos e como o script esta' agora",
     fn: (*) => ajuda()},
    {id: "teclas",   padrao: "F2",  rotulo: "Teclas das sessoes",
     detalhe: "escolhe qual tecla levanta cada par de janelas",
     fn: (*) => configurarTeclas()},
    {id: "montar",   padrao: "F3",  rotulo: "Montar bancada",
     detalhe: "cria as DUAS janelas da sessao e abre as abas nelas",
     fn: (*) => montarBancada()},
    {id: "levantar", padrao: "F4",  rotulo: "Levantar bancada",
     detalhe: "traz as duas janelas de volta, cada uma no seu monitor",
     fn: (*) => levantarBancada()},
    {id: "tempos",   padrao: "F6",  rotulo: "Tempos",
     detalhe: "ritmo das pausas, espera da ronda e pausa entre bancadas",
     fn: (*) => telaTempos()},
    {id: "sobras",   padrao: "F7",  rotulo: "Sobras",
     detalhe: "estado do worker das sobras e o que esta' represado",
     fn: (*) => painelSobras()},
    {id: "seco",     padrao: "F8",  rotulo: "Ensaio seco",
     detalhe: "roda o ciclo SEM colar e SEM gastar credito",
     fn: (*) => rodar(true)},
    {id: "calibrar", padrao: "F9",  rotulo: "Calibrar",
     detalhe: "aponta os 6 pontos da tela do AdBatch",
     fn: (*) => calibrar()},
    {id: "rodar",    padrao: "F10", rotulo: "RODAR",
     detalhe: "o gatilho da geracao. Com o modo sequencial ligado, roda em varias bancadas",
     fn: (*) => rodar(false)},
    {id: "atalhos",  padrao: "F11", rotulo: "Atalhos",
     detalhe: "troca a tecla de qualquer comando desta lista",
     fn: (*) => configurarAtalhos()},
    {id: "log",      padrao: "F12", rotulo: "Log",
     detalhe: "o que o script fez nesta sessao",
     fn: (*) => mostrarLog()},
    {id: "abortar",  padrao: "Esc", rotulo: "Abortar", ctx: true,
     detalhe: "so' funciona ENQUANTO o ciclo esta' rodando",
     fn: (*) => abortarAgora()},
]

teclaDoComando(id) {
    global INI, COMANDOS
    for c in COMANDOS
        if (c.id = id)
            return IniRead(INI, "teclas_comandos", id, c.padrao)
    return ""
}

; ⛔⛔ A GUARDA DA TECLA SOLTA. Um comando em `a` deixaria a maquina inutilizavel
; — toda letra digitada dispararia o F10 — e o operador nao teria como abrir a
; tela para desfazer, porque digitar tambem estaria sequestrado. Teclas de
; funcao e do bloco numerico passam soltas (ninguem digita texto com elas); o
; resto exige Ctrl, Alt ou Shift.
; ⭐ A saida de emergencia existe de qualquer jeito: o MENU DA BANDEJA abre as
; duas telas sem depender de tecla nenhuma.
teclaPerigosa(t) {
    if (t = "")
        return ""
    if RegExMatch(t, "[\^!+#]")
        return ""
    if RegExMatch(t, "i)^(F\d{1,2}|Numpad[A-Za-z0-9]+|Esc|Escape|Pause|Break"
                   . "|Insert|Home|End|PgUp|PgDn|ScrollLock|NumLock|AppsKey"
                   . "|Browser_[A-Za-z]+|Media_[A-Za-z]+|Volume_[A-Za-z]+"
                   . "|Launch_[A-Za-z]+)$")
        return ""
    return "a tecla " nomeDaTecla(t) " esta' solta — ela sequestraria a "
         . "digitacao no Windows inteiro. Use Ctrl, Alt ou Shift junto."
}

; ⛔⛔ REGISTRO DINAMICO, o mesmo molde de `registrarTeclasDeSessao()`: TUDO que
; esta' ligado e' desligado antes de religar a lista nova. Sem isso, trocar a
; tecla de um comando deixaria a ANTIGA respondendo tambem — e duas teclas para
; a mesma coisa e' o comeco de uma delas nao responder.
global gTeclasComando := Map()

; ⛔⛔ UM UNICO OBJETO DE CONTEXTO, guardado num global — e isto NAO e' estilo.
; O AHK casa a variante de uma hotkey pela IDENTIDADE do callback do `HotIf`.
; Criando `(*) => rodando` na hora de registrar e outro na hora de desligar,
; o `Hotkey t, "Off"` procuraria uma variante que nao existe: o Esc antigo
; continuaria ligado e o novo entraria por cima. Duas teclas para a mesma coisa
; e' o comeco de uma delas nao responder — e' a mesma nota do `gTeclasAtivas`.
global gCtxRodando := (*) => rodando

registrarTeclasDeComando() {
    global gTeclasComando, COMANDOS, gCtxRodando
    for t, ctx in gTeclasComando {
        try {
            HotIf(ctx ? gCtxRodando : "")
            Hotkey t, "Off"
        }
    }
    HotIf()
    gTeclasComando := Map()
    for c in COMANDOS {
        t := teclaDoComando(c.id)
        if (t = "" || t = "None")
            continue
        ctx := c.HasOwnProp("ctx")
        try {
            ; ⛔ com `ctx`, so' vale ENQUANTO o ciclo roda — senao o script
            ; sequestra o Esc do Windows inteiro, que foi o motivo do `#HotIf`
            ; da versao anterior.
            HotIf(ctx ? gCtxRodando : "")
            Hotkey t, c.fn, "On"
            gTeclasComando[t] := ctx
        } catch as err {
            anotar("tecla de comando ignorada (" c.id " = " t "): " err.Message)
        }
    }
    HotIf()
}

abortarAgora() {
    global abortar
    abortar := true
    ToolTip "ABORTANDO..."
    SetTimer () => ToolTip(), -1200
}

; ⭐ A tabela da ajuda, montada da fonte unica. `ATALHOS` continua existindo com
; o mesmo nome e o mesmo formato para o resto da tela nao precisar saber de
; nada disso.
atalhosAtuais() {
    global COMANDOS
    r := []
    for c in COMANDOS
        r.Push([nomeDaTecla(teclaDoComando(c.id)), c.rotulo, c.detalhe])
    return r
}

; ⚠️ `inicial` transforma a MESMA tela na tela de abertura, em vez de existir uma
; segunda parecida. Duas telas quase iguais divergem no primeiro conserto que so'
; uma delas receber — e a que ficar para tras e' sempre a que o operador ve'.
ajuda(inicial := false) {
    global INI, LARG_UI
    g := janelaUI(inicial ? "" : "ajuda")

    ; =========================================================================
    ;  ⭐⭐ A FAIXA PRETA DO TOPO (2026-08-11)
    ; =========================================================================
    ; Pedido do operador: *"consegue deixar uma tira preta (tipo cabecalho de
    ; fundo preto) no topo da interface pra harmonizar com o recorte do
    ; background do gif do doom? (pode deixar o background cinza da interface,
    ; achei bonito e confortavel visualmente pros meus olhos)"*.
    ;
    ; ⭐ E' a solucao certa para um problema que eu tinha deixado de lado: o
    ; doomguy tem fundo PRETO e a janela e' CINZA, entao a cara aparecia num
    ; retangulo escuro colado num fundo claro. Em vez de tentar recortar a tarja
    ; do gif — que e' o proprio HUD do Doom e nao um defeito —, o fundo da FAIXA
    ; passa a ser preto e o recorte deixa de existir aos olhos.
    ;
    ; ⛔ O CINZA DO RESTO FICA. Ele disse por que: e' confortavel para os olhos
    ; dele, e ele passa o dia nesta tela. A faixa e' so' o topo.
    ;
    ; ⚠️ O AHK nao pinta regiao — pinta CONTROLE. A faixa e' um `Text` vazio com
    ; `Background`, desenhado ANTES dos outros para ficar por baixo, e com a
    ; largura da area util inteira (`18 + LARG_UI + 18`) para encostar nas duas
    ; bordas. Meia faixa seria pior que faixa nenhuma.
    ; ⛔⛔ A FAIXA NASCE ESTREITA E CRESCE DEPOIS DO `Show`, e isso nao e' manha:
    ; o AHK dimensiona a janela pelo controle mais a' direita MAIS a margem. Uma
    ; faixa larga o bastante para encostar na borda direita EMPURRARIA a janela
    ; mais 18px, e sobraria justamente a tira cinza que ela veio eliminar.
    ; Medido na captura: janela 754 de area util com a faixa parando em 736.
    ; ⚠️ So' depois do `Show` existe largura final para copiar.
    ALT_FAIXA := 100
    faixa := g.AddText("x0 y0 w10 h" ALT_FAIXA " Background000000", "")

    ; ⭐ O CABECALHO APARECE NOS DOIS CASOS. Antes so' a tela de abertura tinha
    ; nome e subtitulo, e o F1 abria direto na tabela — duas telas com a mesma
    ; funcao e caras diferentes.
    ; ⚠️ os textos levam `Background000000` tambem: sem isso cada um carregaria
    ; seu proprio retangulo cinza por cima da faixa, e o remendo apareceria.
    g.SetFont("s16 Bold cFFFFFF", "Segoe UI")
    g.AddText("x18 y16 w" (LARG_UI - 60) " Background000000", APP)
    g.SetFont("s10 Norm cB9B9B9", "Segoe UI")
    g.AddText("x18 y+2 w" (LARG_UI - 60) " Background000000",
              "do agente ao AdBatch Vertical 2, em N abas — o script esta' no ar "
              "e ouvindo os atalhos abaixo.")
    fonteUI(g)
    doomguy(g, ALT_FAIXA)
    ; ⚠️ a primeira secao e' ancorada ABAIXO da faixa por Y absoluto: se herdasse
    ; o `y+18` do doomguy, uma mudanca na altura da imagem mexeria no layout
    ; inteiro sem ninguem perceber.
    fonteUI(g, "s10 Bold")
    g.AddText("x18 y" (ALT_FAIXA + 16) " w" LARG_UI, "Atalhos")
    fonteUI(g, "s9 Norm")
    lv := escurecerUI(g.AddListView("w" LARG_UI " r13 -Multi +Grid NoSort" fundoUI(),
                                    ["Tecla", "O que faz", "Detalhe"]))
    for a in atalhosAtuais()
        lv.Add("", a[1], a[2], a[3])
    ; ⭐⭐ AS TECLAS DE SESSAO ENTRAM NA MESMA TABELA, nao num quadro a
    ; parte: para quem opera, "Ctrl+Alt+1 levanta a CTA - 03 Neusa" e' um atalho
    ; como qualquer outro. Sao as unicas linhas que mudam de maquina para
    ; maquina, e por isso vem do INI em vez de escritas no codigo.
    for t in teclasGravadas()
        lv.Add("", nomeDaTecla(t.tecla), t.chave,
               (t.tecla = "") ? "sem tecla — o F2 atribui uma"
               : (bancadaPorChave(t.chave) != 0)
                 ? "levanta as duas janelas desta sessao"
                 : "as janelas nao estao abertas — rode o F3")
    ; ⚠️ a ultima coluna toma a sobra: na captura ficava uma coluna vazia
    ; de ~20px na direita, que e' o espaco reservado a uma barra de rolagem
    ; que esta tabela nao tem.
    lv.ModifyCol(1, 58), lv.ModifyCol(2, 150), lv.ModifyCol(3, LARG_UI - 212)

    ; ⭐⭐ O STATUS DO WORKER GANHA LINHA PROPRIA E COLORIDA, acima do bloco
    ; monoespacado: dentro daquele bloco cinza ele seria mais uma linha entre
    ; sete, e o unico item da tela que pode estar QUEBRADO agora precisa ser o
    ; primeiro que o olho encontra.
    ; ⛔ O AVISO DE BANCADA FORA DO LUGAR fica ACIMA do worker, logo abaixo dos
    ; atalhos: e' a unica linha da tela que pede uma acao AGORA. E ela so'
    ; aparece quando ha' algo errado — linha que esta sempre la' deixa de ser
    ; lida na segunda semana.
    _fora := bancadasForaDoLugar()
    if (_fora.Length) {
        secaoUI(g, "Atencao")
        _lista := ""
        for _b in _fora
            _lista .= (_lista = "" ? "" : "   ·   ") _b
        g.SetFont("s10 Bold c" COR_MA, "Segoe UI")
        g.AddText("x18 w" LARG_UI, "bancada no monitor errado:   " _lista)
        fonteUI(g)
        g.AddText("x18 w" LARG_UI " y+2 c" COR_FRACA,
                  "aperte a tecla da sessao (F2 mostra qual) ou o F4 com ela em "
                  "foco — as duas janelas voltam para o monitor certo.")
    }

    secaoUI(g, "Worker das sobras")
    _w := estadoWorker()
    g.SetFont("s10 Bold c" _w.cor, "Segoe UI")
    g.AddText("w" LARG_UI, resumoWorker())
    fonteUI(g)
    g.AddText("w" LARG_UI " y+2 c" COR_FRACA,
              "F7 abre o painel com o backlog por dia")

    secaoUI(g, "Como esta' agora")
    fonteUI(g, "s9", "Consolas")

    ; ── monitores
    mons := ""
    loop MonitorGetCount() {
        MonitorGetWorkArea(A_Index, &l, &t, &r, &b)
        mons .= (mons = "" ? "" : "   ") . "m" A_Index " " (r - l) "x" (b - t)
              . ((b - t) > (r - l) ? " retrato" : " paisagem")
    }
    md := monitoresDaBancada()
    nAd := IniRead(INI, "config", "abas", "10")
    nDa := IniRead(INI, "config", "abas_dashboard", "5")

    ; ── calibracao
    cw := IniRead(INI, secPontos(), "calib_w", "")
    ch := IniRead(INI, secPontos(), "calib_h", "")
    cal := (cw != "" && ch != "")
           ? ("6 pontos, janela " cw "x" ch)
           : "6 pontos, SEM tamanho gravado — o F10 vai perguntar uma vez"

    ; ── bancadas
    vv := bancadasVivas()
    bnc := (vv.Length = 0) ? "nenhuma ainda (rode o F3)" : ""
    for b in vv
        bnc .= (bnc = "" ? "" : "   ") . b.chave

    lig := (IniRead(INI, "config", "clique_no_icone", "1") = "0") ? "DESLIGADO" : "ligado"

    ; ⛔⛔ O CARIMBO DA BUILD, e ele nasceu de um custo real: em 2026-08-11 o
    ; operador reportou tres vezes que um conserto "nao funcionava", e nas tres a
    ; correcao SIMPLESMENTE NAO ESTAVA RODANDO — ele tinha uma instancia antiga
    ; de pe'. Um programa residente, que ele reinicia varias vezes ao dia, tem de
    ; conseguir responder sozinho "qual versao sou eu". Sem isto, cada relato de
    ; falha custa uma investigacao inteira antes de descobrir que o codigo novo
    ; nunca subiu.
    ; ⚠️ A data vem do ARQUIVO EM EXECUCAO (`A_ScriptFullPath`), nao de uma
    ; constante que eu teria de lembrar de atualizar — constante esquecida mente
    ; com mais confianca do que nao ter carimbo nenhum.
    carimbo := "?"
    try {
        cf := FileGetTime(A_ScriptFullPath, "M")
        carimbo := FormatTime(cf, "dd/MM/yyyy HH:mm")
    }
    est := escurecerUI(g.AddEdit("w" LARG_UI " r8 ReadOnly -E0x200 -Wrap +HScroll" fundoUI(),
          "esta build .......... " carimbo
        . "  ·  " (A_IsCompiled ? "executavel" : "script .ahk")
        . "`nmonitores .......... " mons
        . "`nbancada vai para ... AdBatch no monitor " md[1] " · dashboard no monitor " md[2]
        . "`nabas por bancada ... " nAd " no AdBatch + " nDa " no dashboard + 1 Montador"
        . "`nformato ............ " nomeFormato() " · " nTakes()
          . " takes · o roteiro tem de dizer 0N" sufTake()
        . "`ncalibracao ......... " cal
        . "`nbancadas montadas .. " bnc
        . "`nclique no icone .... " lig " (levanta a bancada ao clicar no icone da sessao)"
        . "`ninicia com Windows . " (iniciaComWindows() ? "sim" : "nao")
        . "`nmodo sequencial .... "
          . ((IniRead(INI, "config", "sequencial", "0") = "1")
             ? "LIGADO — o F10 pergunta em quais bancadas rodar"
             : "desligado — o F10 roda numa sessao so'")
        . "`narquivo ............ " INI))

    fonteUI(g)
    ; ⭐ na abertura, quem nao quiser a tela desliga aqui mesmo. Caixa de "nao
    ; mostrar de novo" que obriga a caçar a opcao noutro lugar nao e' escolha.
    ; ⭐ As duas caixas ficam JUNTAS e sempre visiveis, na abertura e no F1.
    ; Comportamento que age sozinho — subir com o Windows, levantar a bancada ao
    ; clicar — tem de poder ser desligado na mesma tela onde e' anunciado.
    ; ⭐⭐ O FORMATO DA BANCADA (2026-08-20). Fica JUNTO das outras caixas
    ; pelo mesmo motivo delas: comportamento que muda o que o F3 ABRE e o
    ; que o F10 CONFERE tem de poder ser trocado na tela onde e' anunciado.
    secaoUI(g, "Formato da bancada")
    ; ⛔ O `R3` NAO E' ESTETICA: sem numero de linhas o AHK abre a parte
    ; suspensa com altura ~zero e o clique nao mostra nada. Os dois itens
    ; sempre estiveram la' (provado por `dd.Value := 2` num Gui de teste);
    ; o que nao havia era ONDE eles aparecerem.
    ddFmt := g.AddDropDownList("w" LARG_UI " R3 y+6 Choose"
                               ((nTakes() = 3) ? 2 : 1),
                               ["AdBatch Vertical 2 — 2 takes de 8s"
                                " (o roteiro diz IMAGE 01/02)",
                                "AdBatch Vertical 3 — 3 takes de 6s"
                                " (o roteiro diz IMAGE 01/03)"])
    ddFmt.OnEvent("Change", (*) => trocarFormato((ddFmt.Value = 2) ? 3 : 2))

    cbSeq := g.AddCheckbox("w" LARG_UI " y+10",
                           "modo sequencial: o F10 roda em VARIAS bancadas numa "
                           "tacada (voce marca quais)")
    cbSeq.Value := (IniRead(INI, "config", "sequencial", "0") = "1")
    cbSeq.OnEvent("Click", (*) =>
        IniWrite(cbSeq.Value ? "1" : "0", INI, "config", "sequencial"))
    cbIni := g.AddCheckbox("w" LARG_UI " y+6",
                           "iniciar junto com o Windows (fica no system tray)")
    cbIni.Value := iniciaComWindows()
    cbIni.OnEvent("Click", (*) => ligarInicioComWindows(cbIni.Value))
    if inicial {
        cb := g.AddCheckbox("w" LARG_UI " y+6",
                            "nao mostrar esta tela quando o script iniciar "
                            "(o F1 continua abrindo)")
        cb.Value := (IniRead(INI, "config", "tela_inicial", "1") = "0")
        cb.OnEvent("Click", (*) =>
            IniWrite(cb.Value ? "0" : "1", INI, "config", "tela_inicial"))
    }
    ; ⭐ mesma gramatica das outras telas: a acao de sair a' direita, as acoes de
    ; fazer alguma coisa a' esquerda
    g.AddButton("w110 h30 x" (18 + LARG_UI - 110) " y+16 Default",
                inicial ? "Comecar" : "Fechar")
     .OnEvent("Click", (*) => g.Destroy())
    g.AddButton("w160 h30 x18 yp",
                "Montar bancada (" nomeDaTecla(teclaDoComando("montar")) ")")
     .OnEvent("Click", (*) => (g.Destroy(), montarBancada()))
    g.AddButton("w170 h30 x+8 yp",
                "Levantar bancada (" nomeDaTecla(teclaDoComando("levantar")) ")")
     .OnEvent("Click", (*) => (g.Destroy(), levantarBancada()))
    g.AddButton("w110 h30 x+8 yp", "Ver o log")
     .OnEvent("Click", (*) => mostrarLog())
    ; ⚠️ SEGUNDA LINHA. A primeira ja' tem 456px de botao mais o Fechar a'
    ; direita; os dois novos ali dentro alargariam a janela e desalinhariam
    ; tudo — e' o mesmo mecanismo do `x18` que a nota do `secaoUI` descreve.
    g.AddButton("w160 h30 x18 y+8", "Tempos e ritmo")
     .OnEvent("Click", (*) => (g.Destroy(), telaTempos()))
    g.AddButton("w170 h30 x+8 yp", "Atalhos do teclado")
     .OnEvent("Click", (*) => (g.Destroy(), configurarAtalhos()))
    g.OnEvent("Close", (*) => g.Destroy())
    g.Show()
    ; ⭐ agora que a janela existe, a faixa copia a largura util dela e encosta
    ; nas duas bordas. Antes do Show esse numero nao existe.
    cli := Buffer(16, 0)
    DllCall("GetClientRect", "Ptr", g.Hwnd, "Ptr", cli)
    faixa.Move(0, 0, NumGet(cli, 8, "Int"), ALT_FAIXA)
}


; =============================================================================
;  ⭐⭐ A TELA DOS TEMPOS (2026-08-15)
; =============================================================================
; ⛔ CADA CAMPO DIZ O QUE CUSTA, nao so' o que faz. O operador ja' pediu tres
; rodadas de aceleracao neste script, e a quarta foi a que ele mesmo marcou como
; "risco de falha silenciosa" — uma tela que so' listasse numeros o convidaria a
; baixar justamente os dois que quebram o clipboard em silencio.
; ⚠️ Por isso os dois de RISCO estao no fim, numa secao com o aviso junto, e nao
; misturados no meio dos inofensivos.
;
; ⭐ A ESTIMATIVA fica ACIMA do botao Salvar. E' o unico jeito de o operador ver
; a consequencia dos doze numeros sem rodar um lote de credito para descobrir.
TEMPOS_UI := [
    ["ritmo",            "Ritmo das pausas",        "x",  "1.00 e' o ritmo original; 0.05 e' o de hoje. Governa as 13 esperas ajustaveis de cada aba."],
    ["piso_ms",          "Piso de cada pausa",      "ms", "nenhuma pausa fica menor que isto. Se subir o piso acima do ritmo, o tremor morre e a cadencia vira de maquina."],
    ["parse_ms",         "Espera do Ctrl+V",        "ms", "o tempo que o AdBatch leva para reparsear o roteiro colado. ⛔ NAO e' cadencia: se encurtar demais, o Gerar clica num roteiro pela metade."],
    ["parse_extra_ms",   "Sorteio somado ao Ctrl+V","ms", "sorteado de 0 ate' este valor e SOMADO a espera acima — nunca tirado dela."],
    ["respiro_pct",      "Chance do respiro longo", "%",  "de vez em quando o piloto para de olhar a tela, como gente. 0 desliga."],
    ["respiro_min_ms",   "Respiro longo, minimo",   "ms", ""],
    ["respiro_max_ms",   "Respiro longo, maximo",   "ms", ""],
    ["mouse_vel_min",    "Mouse, mais rapido",      "",   "0 e' teleporte, e teleporte nao existe em maozinha nenhuma. Quanto MAIOR o numero, mais devagar o ponteiro anda."],
    ["mouse_vel_max",    "Mouse, mais devagar",     "",   ""],
    ["entre_bancadas_s", "Pausa ENTRE bancadas",    "s",  "so' vale no modo sequencial. 0 emenda uma bancada na outra, que e' como o script sempre rodou."],
]

; ⚠️ Estes dois moram em `[config]`, nao em `[tempos]`: ja' estavam la' antes
; desta tela existir, e mudar de secao apagaria em silencio o valor que o
; operador tem hoje. Secao errada e' preco de arrumacao; valor perdido e' preco
; de lote.
RONDA_UI := [
    ["espera_s", "Espera de cada ronda", "s", "quanto o piloto espera antes de conferir de novo se os slots ficaram prontos. ±18% sorteado."],
    ["rondas",   "Quantas rondas",       "",  "quantas vezes ele volta para conferir e regerar slot vazio. A partir da SEGUNDA e' que ele regera."],
]

RISCO_UI := [
    ["key_delay_ms",   "Atraso por tecla",  "ms", ""],
    ["mouse_delay_ms", "Atraso por clique", "ms", ""],
]

lerTempoUI(chave, padrao) {
    global INI
    v := Trim(IniRead(INI, "tempos", chave, ""))
    return (v = "") ? padrao : v
}

; ⭐ O padrao de cada campo sai do MESMO lugar que o motor usa (`aplicarTempos`
; le' estes numeros como fallback). Uma segunda lista de padroes divergiria no
; primeiro ajuste, e a tela passaria a mostrar um numero que o script nao usa.
PADROES_TEMPO := Map(
    "ritmo", "0.05", "piso_ms", "8", "parse_ms", "900", "parse_extra_ms", "700",
    "respiro_pct", "22", "respiro_min_ms", "1200", "respiro_max_ms", "3400",
    "mouse_vel_min", "4", "mouse_vel_max", "11", "entre_bancadas_s", "0",
    "key_delay_ms", "22", "mouse_delay_ms", "28",
    "espera_s", "15", "rondas", "6")
; ⚠️ `espera_s` e `rondas` vivem em `[config]`, mas o padrao mora no mapa acima
; junto com os outros: uma segunda tabela de padroes divergiria da primeira no
; primeiro ajuste, e a tela passaria a mostrar numero que o motor nao usa.

; ⭐ TRES PRESETS. Doze numeros e' mais do que cabe na cabeca de quem so' quer
; "mais devagar hoje"; o preset da' o passo inteiro e a tela continua aberta
; para ele afinar em cima.
PRESETS_TEMPO := Map(
    "Original (lento)", Map("ritmo", "1.00", "piso_ms", "40",
                            "key_delay_ms", "40", "mouse_delay_ms", "50"),
    "Rapido (o de hoje)", Map("ritmo", "0.05", "piso_ms", "8",
                              "key_delay_ms", "22", "mouse_delay_ms", "28"),
    "Cauteloso", Map("ritmo", "0.35", "piso_ms", "25",
                     "key_delay_ms", "35", "mouse_delay_ms", "45"))

telaTempos(*) {
    global LARG_UI, INI, COR_FRACA, COR_MA, TEMPOS_UI, RONDA_UI, RISCO_UI
    global PADROES_TEMPO, PRESETS_TEMPO
    g := janelaUI("tempos")
    campos := Map()

    linha(chave, rotulo, unidade, dica, secao) {
        fonteUI(g, "s9")
        g.AddText("x18 y+10 w" (LARG_UI - 250), rotulo)
        val := (secao = "config")
               ? IniRead(INI, "config", chave, PADROES_TEMPO.Has(chave) ? PADROES_TEMPO[chave] : "")
               : lerTempoUI(chave, PADROES_TEMPO.Has(chave) ? PADROES_TEMPO[chave] : "")
        e := escurecerUI(g.AddEdit("x+10 yp-3 w90 Right" fundoUI(), val))
        g.AddText("x+6 yp+3 w40 c" COR_FRACA, unidade)
        campos[chave] := {ctl: e, secao: secao}
        if (dica != "")
            g.AddText("x18 y+2 w" (LARG_UI - 60) " c" COR_FRACA, dica)
    }

    secaoUI(g, "O ritmo das interacoes", true)
    for t in TEMPOS_UI
        linha(t[1], t[2], t[3], t[4], "tempos")

    secaoUI(g, "As rondas (a conferencia dos slots)")
    for t in RONDA_UI
        linha(t[1], t[2], t[3], t[4], "config")

    ; ⛔⛔ A SECAO DE RISCO E' SEPARADA E VEM COM O AVISO EM CIMA. Estes dois sao
    ; os unicos numeros deste script cuja reducao falha EM SILENCIO: abaixo de um
    ; limiar o Chrome descarta a entrada sintetica, o clipboard fica com o
    ; roteiro ANTERIOR e o lote sai com a REF de um video e as cenas de outro —
    ; aparecendo so' no render, com o credito ja' gasto.
    secaoUI(g, "Entrada sintetica — mexa por ultimo")
    fonteUI(g, "s9")
    g.AddText("x18 w" (LARG_UI - 60) " c" COR_MA,
              "Baixar estes dois pode fazer a tecla NAO CHEGAR no Chrome, e a "
              "falha e' MUDA: o lote sai com a REF de um video e as cenas de "
              "outro. Depois de mexer, rode o Ensaio seco UMA vez — ele confere "
              "as cinco partes de graca.")
    for t in RISCO_UI
        linha(t[1], t[2], t[3], t[4], "tempos")

    ; --- a estimativa -----------------------------------------------------
    ; ⚠️ ESTIMATIVA GROSSEIRA, e a tela diz isso. A base de 4.710 ms das 13
    ; pausas de uma aba esta' medida no cabecalho do RITMO; o resto (ffmpeg do
    ; Chrome, o app respondendo) nao da' para prever daqui.
    est := g.AddText("x18 y+16 w" (LARG_UI - 60) " c" COR_FRACA, "")

    estimar(*) {
        n := (v, p) => IsNumber(StrReplace(Trim(v), ",", ".")) ? Number(StrReplace(Trim(v), ",", ".")) : p
        r  := n(campos["ritmo"].ctl.Value, 0.05)
        pv := n(campos["parse_ms"].ctl.Value, 900) + n(campos["parse_extra_ms"].ctl.Value, 700) / 2
        kd := n(campos["key_delay_ms"].ctl.Value, 22)
        md := n(campos["mouse_delay_ms"].ctl.Value, 28)
        rp := n(campos["respiro_pct"].ctl.Value, 22) / 100
        rm := (n(campos["respiro_min_ms"].ctl.Value, 1200)
               + n(campos["respiro_max_ms"].ctl.Value, 3400)) / 2
        abas := Integer(IniRead(INI, "config", "abas", "10"))
        eb := n(campos["entre_bancadas_s"].ctl.Value, 0)
        ; 4.710 ms de base nas 13 pausas + ~8 teclas + ~2 cliques + 2 respiros
        porAba := 4710 * r + kd * 8 * 2 + md * 2 + pv + rp * rm * 2
        est.Value := Format("estimativa grosseira: ~{1:.1f}s por aba  ·  "
                          . "~{2:.1f} min por bancada de {3} abas"
                          . (eb > 0 ? "  ·  +{4}s entre bancadas" : ""),
                            porAba / 1000, porAba * abas / 60000, abas, eb)
    }
    for _, c in campos
        c.ctl.OnEvent("Change", estimar)
    estimar()

    aviso := g.AddText("x18 y+8 w" (LARG_UI - 60) " c" COR_FRACA,
                       "vale no proximo ciclo — nao interrompe um que ja' esteja rodando")

    aplicar(*) {
        for chave, c in campos {
            v := Trim(c.ctl.Value)
            if (v = "")
                v := PADROES_TEMPO.Has(chave) ? PADROES_TEMPO[chave] : "0"
            IniWrite StrReplace(v, ",", "."), INI, c.secao, chave
        }
        aplicarTempos()
    }

    ; ⚠️ `nome` chega por `.Bind()`, nao por closure. Closure criada DENTRO do
    ; laco dos botoes captura a VARIAVEL do laco, e os tres botoes acabariam
    ; carregando o ultimo preset — a mesma armadilha que o `chamadorDaSessao`
    ; documenta la' em cima, e que ja' mordeu este arquivo uma vez.
    presetar(nome, *) {
        for chave, val in PRESETS_TEMPO[nome]
            if campos.Has(chave)
                campos[chave].ctl.Value := val
        estimar()
        aviso.Value := "preset '" nome "' carregado — clique em Salvar para valer"
    }

    padroes(*) {
        for chave, c in campos
            if PADROES_TEMPO.Has(chave)
                c.ctl.Value := PADROES_TEMPO[chave]
        estimar()
        aviso.Value := "padroes de fabrica carregados — clique em Salvar para valer"
    }

    ; ⭐ mesma gramatica das outras telas: sair a' direita, fazer a' esquerda
    g.AddButton("w150 h30 x" (18 + LARG_UI - 150) " y+14 Default", "Salvar")
     .OnEvent("Click", (*) => (aplicar(), g.Destroy(), avisoRapido("tempos salvos")))
    g.AddButton("w110 h30 x" (18 + LARG_UI - 270) " yp", "Cancelar")
     .OnEvent("Click", (*) => g.Destroy())
    ; ⚠️ Os presets vao numa SEGUNDA linha: quatro botoes de 130px mais os dois
    ; da direita nao cabem nos 700px da janela, e o AHK nao quebra linha — ele
    ; ALARGA a janela e o layout inteiro sai torto.
    x := 18
    for nome, _ in PRESETS_TEMPO {
        g.AddButton("w150 h30 " (x = 18 ? "x18 y+10" : "x+8 yp"), nome)
         .OnEvent("Click", presetar.Bind(nome))
        x += 158
    }
    g.AddButton("w110 h30 x+8 yp", "Padroes").OnEvent("Click", padroes)
    g.Show()
}


; =============================================================================
;  ⭐⭐ A TELA DOS ATALHOS (2026-08-15)
; =============================================================================
; ⛔ E' a IRMA da tela do F2, de proposito: mesmo controle nativo `Hotkey`, mesma
; deteccao de colisao, mesmo aviso acima dos botoes. Duas telas com a mesma
; funcao e caras diferentes divergem no primeiro conserto que so' uma receber.
; ⛔⛔ E A COLISAO E' CONFERIDA CONTRA AS DUAS FAMILIAS — comandos E sessoes.
; Elas vivem em secoes diferentes do INI e sao registradas por funcoes
; diferentes, entao nada impediria o operador de pedir `Ctrl+Alt+1` para o
; RODAR quando esse par ja' levanta a "CTA - 03 Neusa". A segunda venceria em
; silencio e a primeira pareceria quebrada.
configurarAtalhos(*) {
    global LARG_UI, INI, COMANDOS, COR_FRACA, COR_MA
    g := janelaUI("atalhos dos comandos")
    secaoUI(g, "Qual tecla dispara cada comando", true)
    g.AddText("x18 w" (LARG_UI - 60) " c" COR_FRACA,
              "Clique no campo e aperte a tecla. Teclas de funcao (F1..F12) e do "
              "bloco numerico valem sozinhas; qualquer outra precisa de Ctrl, "
              "Alt ou Shift junto.`n"
              "Campo vazio DESLIGA o comando — ele continua no menu da bandeja, "
              "que e' a saida quando nao sobra tecla nenhuma.")

    campos := []
    for c in COMANDOS {
        fonteUI(g, "s9")
        g.AddText("x18 y+10 w" (LARG_UI - 240), c.rotulo
                  . (c.HasOwnProp("ctx") ? "   (so' durante o ciclo)" : ""))
        hk := g.AddHotkey("x+10 yp-3 w200", teclaDoComando(c.id))
        campos.Push({id: c.id, rotulo: c.rotulo, ctl: hk})
    }

    aviso := g.AddText("x18 y+14 w" (LARG_UI - 60) " c" COR_FRACA,
                       "as teclas passam a valer assim que voce salvar")

    salvar(*) {
        usadas := Map()
        ; ⛔ as teclas de SESSAO entram na conta ANTES: elas ja' estao ligadas, e
        ; quem chega depois e' que tem de ceder.
        for e in teclasGravadas()
            if (e.tecla != "")
                usadas[e.tecla] := "a sessao '" e.chave "'"
        for c in campos {
            t := c.ctl.Value
            if (t = "")
                continue
            if (msg := teclaPerigosa(t)) {
                aviso.Opt("c" COR_MA)
                aviso.Value := msg
                return
            }
            if usadas.Has(t) {
                aviso.Opt("c" COR_MA)
                aviso.Value := nomeDaTecla(t) " ja' e' de " usadas[t]
                             . " — cada comando precisa da sua"
                return
            }
            usadas[t] := "o comando '" c.rotulo "'"
        }
        ; ⛔⛔ AS CHAVES SAO OBRIGATORIAS AQUI, e custaram uma partida quebrada
        ; na maquina do operador. Sem elas, `if (...) try X` seguido de `else`
        ; NAO COMPILA: no v2 o `Try` tem um `Else` proprio (Try/Catch/Else),
        ; entao o parser le' aquele `else` como o do `Try` — sem `Catch` no
        ; meio — e derruba o SCRIPT INTEIRO na partida com "Unexpected Else".
        for c in campos {
            if (c.ctl.Value = "") {
                try IniDelete INI, "teclas_comandos", c.id
            } else {
                IniWrite c.ctl.Value, INI, "teclas_comandos", c.id
            }
        }
        registrarTeclasDeComando()
        montarBandeja()
        g.Destroy()
        avisoRapido("atalhos salvos")
    }

    padroes(*) {
        for i, c in campos
            campos[i].ctl.Value := COMANDOS[i].padrao
        aviso.Opt("c" COR_FRACA)
        aviso.Value := "padroes carregados — clique em Salvar para valer"
    }

    g.AddButton("w150 h30 x" (18 + LARG_UI - 150) " y+12 Default", "Salvar")
     .OnEvent("Click", salvar)
    g.AddButton("w110 h30 x" (18 + LARG_UI - 270) " yp", "Cancelar")
     .OnEvent("Click", (*) => g.Destroy())
    g.AddButton("w110 h30 x18 yp", "Padroes").OnEvent("Click", padroes)
    g.Show()
}

; ⭐ O MENU DA BANDEJA repete os mesmos comandos. Atalho serve a quem ja' sabe;
; menu serve a quem esta' descobrindo — e um dos dois some quando o operador
; passa duas semanas longe do script.
; =============================================================================
;  ⭐⭐ INICIAR COM O WINDOWS (2026-08-11)
; =============================================================================
; Ordem do operador: *"deixe sempre o terminator exe rodando de background no
; system tray"*.
;
; ⛔ Atalho na pasta Inicializar, e NAO chave de registro em `Run`. Sao
; equivalentes para o Windows, mas nao para o operador: a pasta ele ABRE, VE' e
; APAGA sozinho quando quiser. Registro exige que ele me chame de volta — e
; automacao que so' o autor sabe desligar e' automacao que assusta.
;
; ⚠️ O atalho aponta para o .EXE quando ele existe ao lado, mesmo que quem esteja
; rodando agora seja o .ahk: o que ele pediu para ficar residente foi o
; executavel, e o atalho descreve o FUTURO, nao o processo atual.
atalhoDoInicio() {
    return A_Startup "\Video Terminator.lnk"
}

alvoDoInicio() {
    exe := A_ScriptDir "\Video Terminator.exe"
    return FileExist(exe) ? exe : A_ScriptFullPath
}

iniciaComWindows() {
    return FileExist(atalhoDoInicio()) ? true : false
}

ligarInicioComWindows(ligar) {
    lnk := atalhoDoInicio()
    if ligar {
        try FileCreateShortcut(alvoDoInicio(), lnk, A_ScriptDir, ,
                               "Video Terminator by Eddie")
        catch as e
            return MsgBox("nao consegui criar o atalho:`n" e.Message, APP, 16)
    } else {
        try FileDelete lnk
    }
}

; ⛔⛔ E O MENU E' A SAIDA DE EMERGENCIA desde que as teclas viraram
; configuraveis: se o operador desligar a tecla de TODOS os comandos, e' por
; aqui que ele reabre a tela de atalhos. Por isso o rotulo de cada item passa a
; sair de `teclaDoComando()` — menu que anuncia F10 depois do remapeamento
; mente igual a' tela de ajuda que mentia.
itemBandeja(id) {
    global COMANDOS
    for c in COMANDOS
        if (c.id = id) {
            t := teclaDoComando(c.id)
            A_TrayMenu.Add(c.rotulo (t = "" ? "  (sem tecla)"
                                            : "  (" nomeDaTecla(t) ")"), c.fn)
            return
        }
}

montarBandeja() {
    A_TrayMenu.Delete()
    itemBandeja("ajuda")
    A_TrayMenu.Add()
    itemBandeja("montar")
    itemBandeja("levantar")
    itemBandeja("teclas")
    itemBandeja("atalhos")
    itemBandeja("tempos")
    A_TrayMenu.Add()
    itemBandeja("rodar")
    itemBandeja("seco")
    itemBandeja("calibrar")
    A_TrayMenu.Add()
    itemBandeja("sobras")
    itemBandeja("log")
    A_TrayMenu.Add()
    A_TrayMenu.Add("Iniciar com o Windows",    (*) => (
        ligarInicioComWindows(!iniciaComWindows()), montarBandeja()))
    if iniciaComWindows()
        A_TrayMenu.Check("Iniciar com o Windows")
    A_TrayMenu.Add("Sair",                     (*) => ExitApp())
    ; ⚠️ o padrao do duplo-clique aponta para o rotulo MONTADO, nao para um
    ; literal: com a tecla remapeada o literal deixaria de casar e o AHK
    ; levantaria erro na partida.
    _t := teclaDoComando("ajuda")
    try A_TrayMenu.Default := "Ajuda" (_t = "" ? "  (sem tecla)"
                                              : "  (" nomeDaTecla(_t) ")")
    A_IconTip := APP (_t = "" ? "" : " — " nomeDaTecla(_t) " abre a ajuda")
}

; ⛔⛔ CONSERTA A CALIBRACAO CONTRADITORIA NA PARTIDA (2026-08-11).
; O `.ini` do operador ficou com os pontos num monitor e o `calib_w/h` de outro,
; e o resultado foi a bancada montada TROCADA. Corrigir so' o codigo nao bastava:
; o dado errado continuaria no disco, e a trava de geometria do F10 abortaria
; toda vez comparando a janela certa com o tamanho da errada.
;
; ⭐ Os PONTOS mandam. Se eles apontam para um monitor e o tamanho gravado casa
; com outro, o tamanho e' recalculado da area util do monitor dos pontos mais a
; moldura da janela maximizada — que e' exatamente o que o `WinGetPos` devolveria
; ali. E fica no log: conserto silencioso vira mistério na proxima duvida.
consertarCalibracao() {
    global INI
    cw := IniRead(INI, secPontos(), "calib_w", "")
    ch := IniRead(INI, secPontos(), "calib_h", "")
    mp := monitorDosPontos()
    if (cw = "" || ch = "" || mp = 0)
        return
    if (monitorPorTamanho(cw, ch) = mp)
        return                       ; concordam: nada a fazer
    MonitorGetWorkArea(mp, &l, &t, &r, &b)
    mo := molduraMaximizada()
    nw := (r - l) + mo, nh := (b - t) + mo
    IniWrite nw, INI, secPontos(), "calib_w"
    IniWrite nh, INI, secPontos(), "calib_h"
    anotar("calibracao corrigida: os pontos estao no monitor " mp
           " mas o tamanho gravado era " cw "x" ch " — passou a " nw "x" nh)
}

montarBandeja()
consertarCalibracao()
; ⚠️ a migracao vem ANTES do registro: as teclas do formato antigo tem de
; existir no formato novo para serem ligadas nesta mesma partida.
migrarTeclasAntigas()
registrarTeclasDeSessao()
registrarTeclasDeComando()
; ⚠️ na partida isto define o padrao das threads novas (SetKeyDelay/SetMouseDelay
; sao por thread); o `rodar()` e o `calibrar()` chamam de novo na thread deles.
aplicarTempos()
gCliqueLigado := ligarCliqueNoIcone()

; ⚠️ O SCRIPT SUBIA MUDO. Sem nada na partida, nao havia como saber que ele
; estava rodando, quais teclas existiam, nem que agora ha' um comportamento que
; age sozinho (o clique no icone). A tela de abertura e' a MESMA do F1, com
; cabecalho e a caixa de desligar — nao uma segunda tela parecida.
if (IniRead(INI, "config", "tela_inicial", "1") != "0")
    ajuda(true)
else
    TrayTip("F1 abre a ajuda com todos os atalhos."
            . "`nclique no icone da sessao: " (gCliqueLigado ? "ligado" : "desligado"),
            APP " no ar")

; ⛔⛔ AQUI HAVIA ONZE HOTKEYS CRAVADAS (`F1::`, `F2::`, ... `Esc::`). Elas
; sairam porque essa sintaxe e' de LOAD TIME e nao se remapeia — ver a nota do
; `COMANDOS`. Quem as liga agora e' `registrarTeclasDeComando()`, la' em cima.
;
; ⛔⛔ E O `Persistent` NAO E' ENFEITE: sem uma unica hotkey ESTATICA no arquivo,
; o AHK v2 encerra o script ao chegar no fim da secao de auto-execucao. As
; hotkeys dinamicas segurariam o processo de pe' — ate' o dia em que o operador
; desligar a tecla de todos os comandos na tela nova, e ai' o script morreria na
; partida sem dizer por que. O custo de declarar e' zero; o de descobrir isso em
; campo seria uma manha.
; ⚠️ COM PARENTESES: `Persistent` sozinho numa linha e' uma EXPRESSAO SEM EFEITO
; no v2, nao uma chamada — o script sairia igual e nada acusaria.
Persistent()

; =============================================================================
calibrar() {
    global rodando
    aplicarTempos()
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
           "atalhos de teclado (Ctrl+0, Ctrl+4, Ctrl+R).", APP)

    for alvo in ALVOS {
        ToolTip "[CHROME] aponte para:`n" alvo[2] "`n`n(F9 confirma · Esc cancela)"
        if !esperarF9()
            return ToolTip()
        MouseGetPos(&x, &y)
        IniWrite x, INI, secPontos(), alvo[1] "_x"
        IniWrite y, INI, secPontos(), alvo[1] "_y"
        ToolTip "gravado: " alvo[1] " = " x "," y
        Sleep 350
    }
    ToolTip()

    p := lerPonto("cr_slot1")
    cor := PixelGetColor(p.x, p.y)
    IniWrite cor, INI, secPontos(), "cor_vazio"

    ; ⛔⛔ A COR DO PONTO DO **GERAR** — a trava que faltava, e que so'
    ; existe porque o operador viu o ponteiro errar o alvo numa janela e acertar
    ; noutra (2026-08-11). Medido nas capturas das janelas dele:
    ;     Dolphin (onde ele calibrou) .... logo do AdBatch em y=151
    ;     Chrome principal ............... logo do AdBatch em y=117
    ; DIFERENCA DE 34px, porque as janelas do Dolphin mostram a BARRA DE
    ; FAVORITOS e a do Chrome principal nao. A barra empurra a pagina inteira
    ; para baixo.
    ;
    ; ⛔ E a trava de geometria NAO PEGA ISSO: as duas janelas tem exatamente
    ; o mesmo tamanho (1936x1048). Tamanho igual, conteudo deslocado — e todo
    ; clique cai 34px fora, em silencio, gastando credito.
    ;
    ; ⭐ O ponto do `Gerar` distingue os dois casos sozinho: e' um botao BRANCO
    ; na janela certa e fundo de pagina na errada. Medido: (255,255,255) contra
    ; (14,14,14).
    try {
        pg := lerPonto("cr_gerar")
        IniWrite PixelGetColor(pg.x, pg.y), INI, secPontos(), "cor_gerar"
    }

    ; ⛔⛔ GRAVA A GEOMETRIA DA JANELA CALIBRADA. Sem isto o `prepararJanela`
    ; nao tem com o que comparar, e o script poderia rodar numa janela de
    ; outro tamanho clicando fora de todos os alvos — em silencio, gastando
    ; credito. E' o unico dado que faltava para a trava existir.
    ; ⛔⛔ A GEOMETRIA VEM DA JANELA SOB OS PONTOS, nao da janela ATIVA.
    ; A versao anterior usava `WinGetPos("A")` com este comentario: *"grava a da
    ; janela que estiver ATIVA no fim da calibracao, que e' onde o operador
    ; acabou de apontar os seis pontos"*. A suposicao e' FALSA — basta ele
    ; clicar noutra janela ao terminar. Foi o que aconteceu: os pontos ficaram no
    ; monitor 1 e o tamanho gravado foi o da janela vertical, e o piloto passou a
    ; montar a bancada trocada.
    try {
        pg := lerPonto("cr_gerar")
        hCal := janelaDoPonto(pg.x, pg.y)
        if (hCal && WinExist("ahk_id " hCal)) {
            WinGetPos(, , &cw, &ch, "ahk_id " hCal)
            IniWrite cw, INI, secPontos(), "calib_w"
            IniWrite ch, INI, secPontos(), "calib_h"
            IniWrite WinGetTitle("ahk_id " hCal), INI, secPontos(), "calib_janela"
        }
    }

    n := InputBox("Quantas abas do Chrome estao abertas com a AdBatch?",
                  APP, "w320 h130", "10")
    if (n.Result = "OK" && IsInteger(n.Value))
        IniWrite n.Value, INI, "config", "abas"

    MsgBox("Calibrado.`n`nCor do slot vazio: " cor
           "`nAbas: " IniRead(INI, "config", "abas", "?")
           "`n`nF8 = ensaio seco · F10 = rodar", APP)
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
    x := IniRead(INI, secPontos(), chave "_x", "")
    y := IniRead(INI, secPontos(), chave "_y", "")
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
    global VEL_MOUSE_MIN, VEL_MOUSE_MAX
    if seco {
        MouseMove x, y, Random(VEL_MOUSE_MIN, VEL_MOUSE_MAX)
        ToolTip "[seco] clicaria em " chave
        pausa(280)
        return
    }
    ; ⚠️ o mouse ANDA (quanto MAIOR o numero, mais devagar; 0 e' teleporte) e
    ; so' depois clica — com um respiro curto no meio, como quem mira.
    MouseMove x, y, Random(VEL_MOUSE_MIN, VEL_MOUSE_MAX)
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
    ; ⭐ N takes, nunca dois cravados: o V3 grava tres arquivos.
    takes := []
    loop nTakes() {
        i := A_Index
        t := recortarTake(roteiro, Format("TAKE 0{1}{2}", i, sufTake()))
        if (t = "")
            throw Error("nao consegui recortar o TAKE 0" i sufTake()
                        " do roteiro da aba " aba)
        takes.Push([i, t])
    }
    ; ⚠️ um arquivo por take, com o numero da aba no nome: e' assim que a Fase 2
    ; sabe qual take pertence a qual imagem sem depender de ordem de nada.
    for par in takes {
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

    ; ⛔ AS PARTES, uma a uma — CINCO no Vertical 2 e SETE no Vertical 3.
    ; ⚠️ O sufixo (`/02` ou `/03`) vem de `sufTake()`, nunca escrito na mao:
    ; cravado, ele recusava todo roteiro de tres takes ANTES de colar nada.
    ; Procurar so' por `IMAGE` nao basta: se
    ; vier apenas o 01/02, o lote sai pela metade e o slot 2 fica vazio para
    ; sempre — e o video so' seria descoberto quebrado depois do render.
    for parte in partesDoRoteiro() {
        if !InStr(txt, parte)
            throw Error("o roteiro copiado nao tem " parte "`n`n"
                        "primeiros 150 caracteres:`n" SubStr(txt, 1, 150))
    }
    return txt
}

; =============================================================================
rodar(seco) {
    global rodando
    ; ⛔ NA THREAD DO CICLO, nao so' na partida: `SetKeyDelay`/`SetMouseDelay`
    ; sao por thread, e sem esta linha um valor salvo na tela depois de o script
    ; subir nunca chegaria ao lote que esta' rodando.
    aplicarTempos()
    rodando := true
    try
        rodarMiolo(seco)
    finally {
        rodando := false     ; ⛔ SEMPRE — senao o Esc fica sequestrado
        ToolTip()
    }
}

; ⛔ O LACO DAS ABAS, extraido do `rodarMiolo` para servir aos DOIS modos.
; Nao e' copia: e' o mesmo codigo, chamado de dois lugares. Uma copia divergiria
; no primeiro conserto que so' uma delas recebesse — e a que ficaria para tras
; seria justamente a que gasta credito.
percorrerAbas(hJanela, abas, seco, tAgente, prefixo := "") {
    ; ⚠️ `PARSE_MS`/`PARSE_EXTRA` DECLARADOS, mesmo so' sendo lidos: no v2 um
    ; nome nao declarado dentro de uma funcao e' LOCAL, e um local em branco
    ; viraria `Sleep 0` — o `Gerar` clicado contra um roteiro pela metade, em
    ; silencio. E' a mesma razao de `pausa()` declarar o RITMO que so' le'.
    global abortar, PARSE_MS, PARSE_EXTRA
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
                ; ⛔ FORA DO `RITMO` de proposito — e continua fora mesmo agora
                ; que virou campo. Ela e' FUNCAO (o app tem de terminar de
                ; reparsear), nao cadencia; quem a encurtar clica em `Gerar`
                ; contra um roteiro pela metade e gasta credito no lixo.
                Sleep PARSE_MS + Random(0, PARSE_EXTRA)
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
            ; ⛔ LANCA em vez de voltar: no modo sequencial quem chama precisa
            ; saber que ESTA bancada falhou para seguir para a proxima. Um
            ; `return` mudo aqui abortaria as outras tres em silencio.
            throw Error("aba " i ": " e.Message)
        }
    }
    ToolTip()
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
        return MsgBox("Falta calibrar: " e.Message, APP, 16)
    }

    ; ⭐⭐ MODO SEQUENCIAL (2026-08-11) — proposta do operador: *"um toggle que
    ; quando ativado, a automacao de geracao das imagens acontece com todas as
    ; bancadas montadas em sequencia e, quando desativado, percorre para cada
    ; uma bancada selecionada"*.
    ;
    ; ⭐ O F3 e' o que tornou isto possivel: como ele poe a janela 1 de TODA
    ; bancada maximizada no mesmo monitor, a calibracao vale para todas. Sem
    ; isso, a partir da segunda bancada o piloto estaria clicando no escuro.
    if (IniRead(INI, "config", "sequencial", "0") = "1")
        return rodarVarias(seco, abas, tAgente)

    hJanela := escolherSessao()
    if (hJanela = 0)
        return
    try
        prepararJanela(hJanela)
    catch as e
        return MsgBox(e.Message, APP, 16)
    anotar("sessao: " WinGetTitle("ahk_id " hJanela))
    anotar((seco ? "ENSAIO SECO" : "EXECUCAO") " — " abas " aba(s)")

    try
        percorrerAbas(hJanela, abas, seco, tAgente)
    catch as e {
        MsgBox("Parei: " e.Message "`n`nNada foi colado nesta aba.", APP, 16)
        return
    }

    if seco {
        anotar("ensaio seco terminou sem erro")
        return MsgBox("Ensaio seco OK — os " abas " ciclos rodariam.`n`n"
                      "⚠️ Ele COPIOU de verdade do agente (inofensivo) e "
                      "conferiu as cinco partes. So' nao colou nem gerou."
                      "`n`nF12 ve' o log. F10 roda de verdade.", APP)
    }
    ronda(hJanela)
}

; =============================================================================
;  ⭐⭐ RODAR EM VARIAS BANCADAS
; =============================================================================
; ⛔⛔ DUAS FASES, E A ORDEM E' A RAZAO DE SER: primeiro as ABAS de todas as
; bancadas, e so' depois as RONDAS de todas. Fazendo bancada a bancada
; (abas->ronda, abas->ronda) a ronda da primeira aconteceria logo apos ela. Do
; jeito que ficou, as imagens da bancada 1 ganham DE GRACA todo o tempo que as
; bancadas 2, 3 e 4 levaram para preencher — e a ronda existe justamente para
; pegar o slot que ainda nao chegou. O ganho e' de qualidade, nao de relogio.
;
; ⚠️ UMA BANCADA QUE FALHA NAO DERRUBA AS OUTRAS. Cada uma roda dentro do seu
; try; o que der errado entra no relatorio do fim. Sem isso, uma janela fechada
; na bancada 2 custaria as bancadas 3 e 4.
;
; ⚠️ O Esc aborta TUDO, nao so' a bancada da vez. Quem aperta Esc no meio de uma
; automacao quer que ela pare, nao que pule para a proxima.
; ⭐ A PAUSA ENTRE UMA BANCADA E A PROXIMA (2026-08-15) — pedido do operador:
; *"tempo entre as bandas"*. Ela NAO existia: a fase 1 emendava uma sessao na
; outra sem respiro nenhum, o que e' justamente o padrao de maquina que o resto
; deste arquivo passa o dia inteiro tentando quebrar.
; ⛔ PADRAO ZERO, e de proposito: com o INI vazio o script se comporta como
; antes desta funcao existir. Numero inventado por mim mudaria o lote dele sem
; ninguem ter pedido.
; ⚠️ NAO PAUSA DEPOIS DA ULTIMA — esperar dois minutos para nao fazer mais nada
; e' a versao mais barata de um script que parece travado.
; ⚠️ E usa `dormir()`, nao `Sleep`: durante a pausa o Esc tem de continuar
; abortando, senao a unica saida seria matar o processo.
pausaEntreBancadas(atual, lista) {
    global ENTRE_BANCADAS_S, abortar
    if (ENTRE_BANCADAS_S <= 0 || abortar)
        return
    if (lista.Length && lista[lista.Length].chave = atual.chave)
        return
    ; ±12% como toda espera longa deste script: alarme cravado e' relogio.
    ms := ENTRE_BANCADAS_S * 1000 * (100 + Random(-12, 12)) // 100
    anotar("pausa entre bancadas: " Round(ms / 1000) "s")
    ToolTip "pausa entre bancadas — " Round(ms / 1000) "s   (Esc aborta)"
    dormir(ms)
    ToolTip()
}

rodarVarias(seco, abas, tAgente) {
    global abortar
    escolhidas := escolherBancadas(seco, abas)
    if (escolhidas.Length = 0)
        return

    anotar((seco ? "ENSAIO SECO" : "EXECUCAO") " SEQUENCIAL — "
           escolhidas.Length " bancada(s), " abas " aba(s) cada")

    feitas := [], falhas := []
    ; ── FASE 1: as abas de todas
    for b in escolhidas {
        if abortar
            break
        try {
            if !WinExist("ahk_id " b.h1)
                throw Error("a janela nao esta' mais aberta")
            prepararJanela(b.h1)
            anotar("== " b.chave " ==")
            percorrerAbas(b.h1, abas, seco, tAgente, b.chave)
            feitas.Push(b)
            pausaEntreBancadas(b, escolhidas)
        } catch as e {
            anotar("== " b.chave ": FALHOU — " e.Message)
            falhas.Push({chave: b.chave, erro: e.Message})
        }
    }

    ; ── FASE 2: as rondas, na mesma ordem
    if (!seco && !abortar) {
        for b in feitas {
            if abortar
                break
            try {
                if !WinExist("ahk_id " b.h1)
                    throw Error("a janela sumiu antes da ronda")
                prepararJanela(b.h1)
                anotar("== ronda de " b.chave " ==")
                ronda(b.h1, true)
                pausaEntreBancadas(b, feitas)
            } catch as e {
                anotar("== ronda de " b.chave ": FALHOU — " e.Message)
                falhas.Push({chave: b.chave " (ronda)", erro: e.Message})
            }
        }
    }

    ToolTip()
    txt := (seco ? "Ensaio seco sequencial" : "Execucao sequencial")
         . (abortar ? " ABORTADA" : " terminada") ".`n`n"
         . feitas.Length " de " escolhidas.Length " bancada(s) percorrida(s)"
    if (falhas.Length) {
        txt .= "`n`nNAO rodaram:"
        for f in falhas
            txt .= "`n   " f.chave " — " f.erro
    }
    anotar("sequencial: " feitas.Length "/" escolhidas.Length
           " ok, " falhas.Length " falha(s)")
    MsgBox(txt "`n`nF12 ve' o log.", APP)
}

; ⭐ A tela de marcar. Ordem do operador: *"eu marco quais, na hora"*.
; ⛔ O TOTAL DE VIDEOS FICA NA TELA ANTES DO BOTAO. A diferenca entre 10 e 40
; geracoes e' credito, e o numero tem de estar visivel antes do clique, nao
; depois.
escolherBancadas(seco, abas) {
    global LARG_UI, COR_FRACA, COR_BOA
    vivas := bancadasVivas()
    if (vivas.Length = 0) {
        MsgBox("Nenhuma bancada montada.`n`nRode o F3 nas sessoes que voce quer "
               "percorrer — ou desligue o modo sequencial na tela do F1.",
               APP, 48)
        return []
    }
    g := janelaUI(seco ? "ensaio seco em varias bancadas"
                       : "rodar em varias bancadas")
    secaoUI(g, "Em quais bancadas rodar", true)
    g.AddText("w" LARG_UI " c" COR_FRACA,
              "Todas comecam marcadas. Desmarque a que voce quiser pular nesta "
              "rodada.")
    caixas := []
    for b in vivas {
        cb := g.AddCheckbox("x18 y+8 w" LARG_UI " Checked", b.chave)
        caixas.Push({cb: cb, b: b})
    }
    total := g.AddText("x18 y+14 w" LARG_UI " c" COR_BOA, "")
    atualizar(*) {
        n := 0
        for c in caixas
            if c.cb.Value
                n++
        total.Value := n " bancada(s)  ·  " (n * abas) " video(s) no total"
                     . (seco ? "   (ensaio seco: nao gasta credito)" : "")
    }
    for c in caixas
        c.cb.OnEvent("Click", atualizar)
    atualizar()

    escolhido := []
    ir(*) {
        for c in caixas
            if c.cb.Value
                escolhido.Push(c.b)
        if (escolhido.Length = 0)
            return MsgBox("Marque pelo menos uma.", APP, 48)
        g.Destroy()
    }
    g.AddButton("w170 h30 x" (18 + LARG_UI - 170) " y+14 Default",
                seco ? "Ensaiar" : "Rodar agora").OnEvent("Click", ir)
    g.AddButton("w110 h30 x" (18 + LARG_UI - 290) " yp", "Cancelar")
     .OnEvent("Click", (*) => g.Destroy())
    g.Show()
    WinWaitClose "ahk_id " g.Hwnd
    return escolhido
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
; ⛔⛔ O `silencioso` E' O CONSERTO DE UM DEFEITO QUE MATAVA A FINALIDADE DA
; ROTA (2026-08-11). Relato do operador: *"quando uso F10 para percorrer todas
; as bancadas montadas, quando o script salta de uma bancada pra outra, ele ta
; me pedindo o clique manual no OK; esse step esta quebrando a finalidade da
; rota, que e' ser automatica"*.
;
; A ronda terminava com um MsgBox de sucesso. Numa bancada so' isso e' um aviso
; util; em QUATRO em sequencia sao quatro paradas esperando um clique — e uma
; automacao que precisa de babá no meio nao e' automacao.
;
; ⭐ No modo sequencial o resultado de cada bancada vai para o LOG e para o
; relatorio unico do fim, que ja' existe. Aviso por bancada so' faz sentido
; quando a bancada e' o trabalho inteiro.
ronda(hJanela, silencioso := false) {
    global abortar, INI
    abas    := Integer(IniRead(INI, "config", "abas", "0"))
    corVaz  := IniRead(INI, secPontos(), "cor_vazio", "")
    maxR    := Integer(IniRead(INI, "config", "rondas", "6"))
    espera  := Integer(IniRead(INI, "config", "espera_s", "15"))

    if (corVaz = "") {
        anotar("ronda pulada: cor do slot vazio nao calibrada")
        ; ⚠️ TAMBEM CALADO no sequencial. Este era o terceiro MsgBox da ronda e
        ; passou despercebido na primeira leitura: eu tinha achado dois. Uma
        ; auditoria que conta "os MsgBox que eu lembro" nao e' auditoria — a que
        ; achou este percorreu a funcao inteira por regex.
        if silencioso
            return
        return MsgBox("Lotes disparados. Ronda pulada (falta calibrar a cor).",
                      APP)
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
            for par in paresDaRonda() {
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
            if silencioso
                return
            return MsgBox("Pronto — as " abas " abas com as duas imagens.",
                          APP)
        }
    }
    ; ⚠️ mesmo o aviso de FALHA e' calado no sequencial: ele entra no log e no
    ; relatorio do fim. Uma caixa de erro no meio da fila para a fila inteira.
    anotar("fim das rondas com slot vazio")
    if silencioso
        return
    MsgBox("Fim das rondas, ainda ha' slot vazio. F12 ve' o log.",
           APP, 48)
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

; ⛔ Era um MsgBox despejando o log inteiro: sem rolagem util, sem como copiar
; uma linha, e crescendo ate' estourar a tela num dia de muitas rodadas. Numa
; ferramenta em que o log e' a UNICA prova do que aconteceu, ele nao pode ser a
; tela mais pobre do script.
mostrarLog(*) {
    global linhas, ARQ_LOG, LARG_UI
    g := janelaUI("log")
    secaoUI(g, "O que o script fez nesta sessao", true)
    if !linhas.Length {
        g.AddText("w" LARG_UI " c" COR_FRACA, "Nada rodou ainda desde que o script subiu.")
    } else {
        txt := ""
        ; ⚠️ mais NOVO em cima: numa lista longa, o que importa e' o fim
        loop linhas.Length
            txt .= linhas[linhas.Length - A_Index + 1] "`r`n"
        fonteUI(g, "s9", "Consolas")
        escurecerUI(g.AddEdit("w" LARG_UI " r16 ReadOnly -Wrap +HScroll" fundoUI(), txt))
        fonteUI(g)
    }
    ; ⛔ CAMINHO NAO VAI EM `AddText`. Medido em 2026-08-11: o caminho do log e'
    ; um token SEM ESPACOS, um Static nao consegue quebra-lo, e o AHK ALARGA o
    ; controle — a janela do log saiu 74px mais larga que as outras tres, que e'
    ; exatamente a inconsistencia que se estava consertando. Um Edit respeita a
    ; largura pedida, e de quebra o caminho fica selecionavel.
    g.AddText("w" LARG_UI " y+10 c" COR_FRACA, "arquivo completo:")
    fonteUI(g, "s9", "Consolas")
    escurecerUI(g.AddEdit("w" LARG_UI " r1 y+2 ReadOnly -E0x200 -Wrap +HScroll" fundoUI(), ARQ_LOG))
    fonteUI(g)
    g.AddButton("w150 h30 x" (18 + LARG_UI - 150) " y+12 Default", "Fechar")
     .OnEvent("Click", (*) => g.Destroy())
    g.AddButton("w170 h30 x18 yp", "Abrir a pasta do log")
     .OnEvent("Click", (*) => Run('explorer.exe /select,"' ARQ_LOG '"'))
    g.OnEvent("Close", (*) => g.Destroy())
    g.Show()
}
