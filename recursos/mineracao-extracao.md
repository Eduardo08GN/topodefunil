# Mineração & Extração — o pipeline validado

Nosso **kit comprovado** de coletar e processar fontes (PDF, YouTube, reels do Facebook, áudio, frames). É o método que **de fato funcionou** na prática — distinto do método "de aula" em [baixar-qualquer-vsl.md](baixar-qualquer-vsl.md). Ferramentas já instaladas: **pypdf, yt-dlp, ffmpeg/ffprobe, Python, o navegador integrado, e a visão do Claude**.

- **Status:** ✅ consolidado (validado em uso)

## A) PDF → texto (destilar livros/relatórios)
- **Ferramenta:** `pypdf` (Python). Extrai texto corrido de PDFs baseados em texto.
- ⚠️ **Armadilha real:** um `.bat` com `pdf-to-markdown` gerou arquivos **0 KB** — o comando não estava instalado, e o `>` cria o arquivo vazio *antes* do comando rodar. Sempre **conferir o tamanho** do output.
- Snippet: `PdfReader(path)` → iterar `page.extract_text()` → salvar `.txt`/`.md`.

## B) YouTube (canal ou vídeo) → transcrição
- **Listar vídeos do canal:** `yt-dlp --flat-playlist --print "%(id)s | %(title)s" "<url do canal>/videos"`.
- **Baixar legendas** (sem baixar o vídeo): `yt-dlp --write-auto-subs --write-subs --sub-langs "pt,en" --sub-format vtt --skip-download -o "subs/%(id)s.%(ext)s" "<canal/vídeo>"`.
- **Limpar o VTT:** tirar timestamps/tags e **deduplicar a repetição rolante** das legendas automáticas (a mesma frase reaparece linha após linha). Um limpador em Python que colapsa linhas repetidas/prefixas resolve. Preferir PT; cair pra EN se não houver.

## C) Facebook reels → download (a descoberta-chave)
1. **As páginas são PÚBLICAS no navegador deslogado** — dá pra ver o grid de Reels sem login.
2. **Colher os IDs dos reels do DOM** (JS no navegador): pegar `a[href]` que casem com `/reel/\d+`. Rola a página se precisar de mais.
3. **Baixar por URL — SEM cookie:** `yt-dlp -f "best[height<=720]/best" "https://www.facebook.com/reel/<ID>/"`. Reel público baixa direto.
- ⚠️ **Armadilha:** `--cookies-from-browser chrome` está **morto** aqui — o Chrome trava o banco de cookies enquanto aberto **e** usa app-bound encryption. Não perca tempo com cookies; o caminho é o download público por URL.
- ⚠️ URLs de **página com nome** (`/nome/reels_tab`) às vezes caem em login-wall; use o formato `profile.php?id=...&sk=reels_tab`.

## D) Vídeo → contact-sheet (digestão visual)
- **Grade de frames (1 imagem/vídeo):** `ffmpeg -i in.mp4 -vf "fps=1/3,scale=320:-1,tile=4x4" -frames:v 1 sheet.jpg` (16 quadros da linha do tempo num JPG só — barato pra ler/analisar).
- **Hook isolado (frame 0):** `ffmpeg -i in.mp4 -vf "select=eq(n\,0)" -vframes 1 hook.png`.
- ⚠️ **Armadilha Windows:** o arquivo de lista do `concat` do ffmpeg precisa de path **estilo Windows** (`C:/...`), não `/c/...` — o ffmpeg é binário Windows e não entende o path do git-bash **dentro** do arquivo de concat (nos argumentos ele é traduzido; no arquivo, não).

## E) Vídeo → mp3 (para transcrição de áudio)
- **Extrair:** `ffmpeg -i in.mp4 -vn -c:a libmp3lame -q:a 5 -ar 44100 -ac 1 out.mp3` (mono, uniforme).
- **Compilar por grupo:** extrair todos para mp3 uniforme, depois `ffmpeg -f concat -safe 0 -i lista.txt -c copy grupo.mp3` (paths Windows na lista — ver armadilha em D).

## F) Análise em escala
- **Workflow com subagentes** lendo os contact-sheets/transcrições em paralelo (1 por página/lote) → matriz de signature → síntese. Ver [digestao-visual.md](../funil-organico/digestao-visual.md).

## Onde guardar
- **Brutos de terceiros** (transcrições, frames): `_fontes/` no repo (privado) ou **fora do Git** se for pesado (áudio/vídeo em `C:\vsl\...`). **Não commitar mp3/mp4** no Git.
- **Destilado/análise:** nos pilares (`frameworks/`, `principios/`, `funil-organico/`, `swipes/`).

## Conexões
- [Baixar qualquer VSL (método de aula)](baixar-qualquer-vsl.md) — a versão "teórica" (Facebook Ads Library, FetV, AssemblyAI)
- [Digestão Visual (pipeline no funil)](../funil-organico/digestao-visual.md) · [Signature — Matriz](../funil-organico/signature-matriz.md)
- [Insights: Empirismo Acumulado](../00-mapa/insights-empiricos.md)
