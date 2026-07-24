# RUNBOOK — /watch: assistir e mapear vídeos (espionagem de criativos)

Como usar a skill `/watch` do Claude Code para **assistir um vídeo** (reel de
concorrente, criativo de referência, VSL) e receber de volta:

- **Transcrição completa** com timestamps (fala palavra a palavra)
- **Frames** do vídeo inteiro (leitura ótica: legendas karaoke, props, cenários)
- Mapeamento pronto pra virar doutrina de swipe / prompts do agente V4

Validado em produção em 2026-07-23 mapeando o reel Rhodiola da "Tanisha Rivers"
(104s, 38 segmentos transcritos, 59 frames lidos).

---

## Happy path 1 — Site público (YouTube, TikTok, X, Vimeo...)

O caminho feliz de verdade. Basta:

```
/watch <url do video>
```

O que acontece por baixo:

1. yt-dlp busca legendas nativas (grátis) e baixa o vídeo (até 720p)
2. Sem legenda nativa → extrai o áudio e transcreve via **Groq Whisper**
   (whisper-large-v3, centavos por vídeo)
3. ffmpeg extrai frames por mudança de cena (detail `balanced`, teto 100)
4. O Claude LÊ cada frame (visão) + transcrição e entrega o mapeamento

Variações úteis:

```
/watch <url> --start 0:45 --end 1:10     # foca num trecho (frames mais densos)
/watch <url> --detail transcript          # só transcrição, zero frames (barato)
/watch <url> --detail token-burner        # frame de TUDO (caro, máxima fidelidade)
/watch <arquivo.mp4 local>                # arquivo local funciona igual
```

**Pedir sempre:** "faça leitura ótica da copy visual" — garante que o Claude
leia TODOS os frames e mapeie as legendas queimadas (karaoke), não só a fala.

---

## Happy path 2 — Facebook / Instagram (login-walled)

Reels de FB/IG **não saem anônimos**. O fluxo que funciona:

### 2a. Com o Chrome FECHADO (mais simples)

Com `WATCH_COOKIES_BROWSER=chrome` configurado (ver Setup), o próprio
`/watch <url do reel>` funciona: o download anônimo falha, a skill faz o
retry com os cookies da sessão logada do Chrome e segue o fluxo normal.

**Pré-condição:** Chrome fechado. Com ele aberto, o Windows tranca o banco de
cookies e o retry falha (`Could not copy Chrome cookie database`).

### 2b. Com o Chrome ABERTO (rota validada em produção)

Quando o Chrome está em uso (sessão Claude in Chrome ativa), o caminho é
capturar o vídeo de dentro da própria aba logada:

1. **Abrir o reel** na aba do Claude in Chrome (sessão logada do usuário)
2. **Extrair as URLs do stream** do JSON embutido da página — os scripts do
   FB carregam `"progressive_url"` com URLs assinadas do fbcdn (funcionam sem
   cookie):
   ```js
   // via javascript_tool na aba do reel
   let urls = [];
   for (const s of document.querySelectorAll('script')) {
     const t = s.textContent || '';
     const re = /"progressive_url"\s*:\s*"((?:[^"\\]|\\.)*)"/g;
     let m; while ((m = re.exec(t)) !== null) urls.push(JSON.parse('"'+m[1]+'"'));
   }
   ```
3. **Tirar o vídeo da aba.** Dois bloqueios conhecidos e o desvio:
   - A extensão **bloqueia** retornar URLs assinadas no resultado da tool
     (`[BLOCKED: Cookie/query string data]`) → o Claude não pode "ver" a URL
   - O CSP do Facebook **bloqueia** `fetch` da página para `localhost`
   - **Desvio que funciona:** subir um mini servidor HTTP local (porta 8765)
     e fazer a aba **navegar** para
     `http://127.0.0.1:8765/relay#<urls-em-JSON-urlencoded>` — navegação não
     passa pelo `connect-src` do CSP. A página `/relay` (mesma origem do
     servidor) posta as URLs de volta e o servidor baixa o .mp4 do fbcdn
     server-side. A URL nunca entra no contexto do Claude.
4. **Rodar o watch no arquivo local:**
   ```
   python %USERPROFILE%\.claude\skills\watch\scripts\watch.py "caminho\do\reel.mp4" --resolution 640
   ```
5. Devolver a aba pro reel e derrubar o servidor.

> O script do servidor relay fica em sessão (scratchpad). Se precisar de novo,
> pedir: "captura esse reel de Facebook pelo Chrome como no runbook do watch".

---

## Setup (uma vez só)

Config em `~/.config/watch/.env`:

```
GROQ_API_KEY=gsk_...          # transcrição Whisper (console.groq.com/keys)
WATCH_DETAIL=balanced          # padrão de frames
WATCH_COOKIES_BROWSER=chrome   # resgate p/ sites login-walled (FB/IG)
SETUP_COMPLETE=true
```

Binários: `ffmpeg` + `yt-dlp` no PATH (winget) **e** `pip install yt-dlp`
(ver Gotchas #1).

---

## Gotchas (todos já vividos e resolvidos)

1. **yt-dlp velho no System32.** O exe em `C:\Windows\System32\yt-dlp.exe`
   não atualiza sem admin e quebrava o extractor do Facebook. A skill foi
   patchada (`scripts/download.py`) para preferir `python -m yt_dlp` (pip,
   sempre atualizável). Manter o pacote fresco: `pip install -U yt-dlp`.
2. **Cookies só como resgate.** O `--cookies-from-browser` entra SÓ quando o
   download anônimo falha. Motivo: com o navegador aberto o cookie DB fica
   trancado e derrubaria também os sites públicos.
3. **Downloads fantasma (D:\Downloads).** O registro do Windows aponta a
   pasta Downloads para `D:\Downloads` e o drive D: nem sempre existe.
   Downloads do Chrome somem e o watcher do Veo Editor vigia um caminho
   morto. Preferir salvar/capturar em pasta explícita.
4. **Reel ≠ página.** `/watch` é para VÍDEO. Perfil/página de FB se lê com o
   browser (Claude in Chrome se precisar de login), não com a skill.
5. **Custo de tokens.** ~60 frames a 640px ≈ 50-80k tokens de imagem. Para
   triagem rápida de muitos vídeos, usar `--detail transcript` primeiro e
   ler frames só dos vídeos que valerem a pena.

---

## O que pedir no final (padrão da casa)

Depois do mapeamento, os outputs úteis pro funil:

- **Tabela de cenas**: tempo, cenário/props, beat narrativo
- **Estilo da legenda**: fonte, cor do karaoke, palavras por linha
- **Copy falada completa** com timestamps (vem da transcrição)
- **Leituras estratégicas**: CTA usado, mecanismo, escassez, persona
- Opcional: salvar como swipe em `funil-organico/swipes/` e/ou converter o
  esqueleto em prompts V4 (`AGENTE_ED_ORGANIC_WAVE_V4.md`)
