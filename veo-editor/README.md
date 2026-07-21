# Veo Editor By EDDIE

Esteira de produção offline para a **última etapa** do pipeline: pega o `.zip`
que as ferramentas do Flow baixam, **junta os takes na ordem, tira o silêncio,
varia a velocidade e queima a legenda estilo CapCut (word-by-word)** — tudo
sozinho, organizado para dezenas de vídeos por dia. Roda 100% local
(FFmpeg + auto-editor + faster-whisper). Nenhuma ferramenta paga, nenhuma API.

## A esteira (modo principal)

Abra o app pelo atalho e pronto — o watcher liga junto. A partir daí:

1. Você clica **Baixar Pacote ZIP** na ferramenta do Flow.
2. O watcher detecta o `adbatch*.zip` na pasta **Downloads** (download concluído,
   tamanho estável) e captura sozinho. Zips avulsos podem ser arrastados para
   `01_entrada/` (qualquer nome).
3. Edição automática: extrai → junta os takes em ordem natural (`video_01..NN`)
   → corta silêncio → **varia a velocidade** → transcreve → queima legenda karaoke.
4. O vídeo pronto cai em `03_prontos/AAAA-MM-DD/vNNN_final.mp4` (sequencial por
   dia), o zip original é arquivado e o histórico registrado.

### Organização de pastas (criadas ao lado do app)

| Pasta | Papel |
|---|---|
| `01_entrada/` | zips arrastados manualmente |
| `02_processando/` | o vídeo em edição no momento (fila de 1 por vez) |
| `03_prontos/AAAA-MM-DD/` | finais do dia: `v001_final.mp4`, `v002_final.mp4`... |
| `04_zips_arquivados/` | zip original preservado (p/ reeditar); limpeza automática > 14 dias |
| `05_erros/` | zip que falhou + `.log` do erro, com botão de retry no painel |
| `historico.csv` | data, arquivo, zip de origem, duração, fator de velocidade, status |

### Variação de velocidade (anti-batch)

Cada vídeo recebe um fator sorteado entre **0.95x (−5%) e 1.03x (+3%)** — assim
um lote de 50 vídeos nunca sai com durações idênticas. Aplicada com
`setpts`+`atempo` (pitch da voz preservado, inaudível) **antes da transcrição**,
então a legenda karaoke nasce sincronizada com o ritmo final. O fator usado fica
registrado no `historico.csv` e no painel.

### Janela do app (desktop, sem navegador)

App tkinter nativo com a identidade da casa (fundo escuro, aqua, dourado):
três colunas — **Fila** / **Editando agora** (log ao vivo) / **Prontos hoje**
(contador + duplo clique ou "Ver" abre o vídeo no player padrão) —, seção de
erros com "Tentar de novo", ajustes de precisão/silêncio e **Pasta avulsa...**
(modo manual em janela própria).

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

**Abrir** — duplo clique no atalho. A janela do app abre direto (sem navegador,
sem console). Pra encerrar, feche a janela — o watcher para junto.

## Uso por linha de comando (opcional, modo manual)
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
- `app.py` — app desktop (tkinter): esteira + prontos + modo manual.
- `esteira.py` — orquestrador: watcher do Downloads, fila, pastas, histórico, retry.
- `pipeline.py` — motor (extrair → juntar → desilenciar → velocidade → legendar) + CLI.
- `captions.py` — transcrição + geração do ASS karaoke CapCut.

## Notas de dependência
- `auto-editor` está em **29.3.1**; a 27.x foi removida do PyPI.
- `requests` é declarado explicitamente porque o `faster-whisper` 1.1.0 o importa
  sem declarar — antes vinha via `huggingface-hub`, que na 1.x migrou pra httpx.
- A fonte da legenda é **Arial Black** (nativa do Windows).
- O watcher acha o Downloads verdadeiro pelo registro do Windows (funciona com
  OneDrive redirecionando pastas).
