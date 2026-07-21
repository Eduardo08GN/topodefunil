# Veo Editor By EDDIE

Automatiza a **última etapa manual** do pipeline de produção: pega os takes que o
Veo gerou, **junta na ordem, tira o silêncio e queima a legenda estilo CapCut
(word-by-word)**. Roda 100% offline na sua máquina (FFmpeg + auto-editor +
faster-whisper). Nenhuma ferramenta paga, nenhuma API.

## O que ele faz (por vídeo)
1. Extrai o `.zip` baixado do Flow, se houver.
2. Junta os takes (`take1..takeN`) na ordem.
3. Corta o silêncio entre/dentro dos takes (auto-editor).
4. Transcreve o áudio offline (Whisper) com timestamp por palavra.
5. Queima a legenda karaoke: a palavra falada acende (amarelo), o resto fica branco.

Saída: um `.mp4` 9:16 pronto pra postar.

## Instalação (Windows)

**Pré-requisitos** — instale antes, uma vez só:
```powershell
winget install Python.Python.3.12
winget install Gyan.FFmpeg
```
Feche e reabra o terminal depois (pro PATH atualizar).

**Instalar o app** — dê duplo clique em:
```
instalar.bat
```
Ele cria o ambiente virtual, instala as dependências e põe o atalho
**Veo Editor By EDDIE** na área de trabalho.

**Abrir** — duplo clique no atalho da área de trabalho. O navegador abre
sozinho em `http://127.0.0.1:7861`. Pra encerrar, feche a janela preta.

## Como usar

Informe a **pasta de entrada** e a **pasta de saída**, escolha a precisão e
clique **Processar**. Use **Inspecionar** antes pra conferir o que ele detectou.

### O que pode ir na pasta de entrada

| Conteúdo | Resultado |
|---|---|
| Um `.zip` baixado do Flow | Extraído automático = 1 vídeo |
| Vários `.zip` | 1 vídeo por zip, em lote |
| Arquivos de vídeo soltos | 1 vídeo (os takes, em ordem de nome) |
| Subpastas com vídeos | 1 vídeo por subpasta, em lote |

Os takes são ordenados por nome com ordenação natural, então `take2` vem antes
de `take10`. O `.zip` original é preservado após a extração, e rodar de novo
reaproveita o que já foi extraído em vez de refazer.

## Uso por linha de comando (opcional)
```powershell
.venv\Scripts\python.exe pipeline.py -i "C:\...\veo_takes" -o "C:\...\prontos" --model base.en --margin 0.2s
```

## Precisão da transcrição
- `base.en` — rápido, bom pra volume (padrão).
- `small.en` — equilíbrio.
- `medium.en` — mais preciso, mais lento.

O modelo é baixado uma vez no primeiro uso e fica em cache (offline depois disso).

## Arquivos
- `instalar.bat` — instalação e atalho na área de trabalho.
- `Veo Editor.bat` — abre o app.
- `app.py` — interface local (Flask).
- `pipeline.py` — motor (extrair zip → juntar → desilenciar → legendar) + CLI.
- `captions.py` — transcrição + geração do ASS karaoke CapCut.

## Notas de dependência
- `auto-editor` está em **29.3.1**; a 27.x foi removida do PyPI.
- `requests` é declarado explicitamente porque o `faster-whisper` 1.1.0 o importa
  sem declarar — antes vinha via `huggingface-hub`, que na 1.x migrou pra httpx.
- A fonte da legenda é **Arial Black** (nativa do Windows).
