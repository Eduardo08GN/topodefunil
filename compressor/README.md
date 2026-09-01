# Comprimir — vídeo e imagem menores, sem perda visível

Encolhe vídeos e imagens via ffmpeg. Motor + app tkinter, no estilo do Veo Editor.

## O que é cada arquivo

| | |
|---|---|
| `comprimir.py` | o **motor** (CLI). Também é o que o app chama por dentro |
| `app_compressor.py` | o **app** de janela (escolhe pasta/arquivos, botão, barra, log) |

O atalho `Comprimir.lnk` fica na **área de trabalho**, fora do repo (aponta para o
`pythonw` + `app_compressor.py`). Se sumir, recriar com um `.lnk` nativo apontando
para `pythonw.exe` com o `app_compressor.py` como argumento — **não** usar `.bat`
(a pegadinha do `start` com espaços no caminho, e CRLF).

## Uso pelo terminal

```
python comprimir.py <arquivo-ou-pasta>
python comprimir.py "C:\Users\lucas\Desktop\videos"
python comprimir.py video.mp4 --crf 23
python comprimir.py pasta --x265        (HEVC: ~40% menor, NÃO para AdBatch/FB)
python comprimir.py foto.png --para-jpg (PNG-foto vira JPG)
```

## Decisões que valem lembrar

- **CRF, não bitrate.** Mira QUALIDADE e deixa o tamanho cair. É o certo para "sem
  perder qualidade". Padrão CRF 23 = sem diferença visível (medido: PSNR 46,5 dB
  num vídeo real; acima de 40 dB o olho não vê).
- ⛔ **Padrão é H.264, não H.265.** O AdBatch e alguns fluxos do Facebook engasgam
  com HEVC. H.264 sobe em qualquer lugar. `--x265` só para arquivo de guardar.
- ⛔ **Nunca sobrescreve o original.** Saída em `comprimidos/` ao lado dos arquivos.
  Se o comprimido sairia maior (já estava ótimo), copia o original e avisa.
- ⛔ **PNG com transparência fica PNG** mesmo com `--para-jpg` (JPG perderia o alpha).
- ⛔ **Sob pythonw, `sys.stdout` é None** — o `reconfigure` é guardado, senão o app
  "não abre" (morre na importação, sem console para mostrar o erro).
- ⛔ **`CREATE_NO_WINDOW` em todo ffmpeg/ffprobe** — sem isso cada chamada abre um
  cmd preto próprio, porque o app roda sem console. Medido: 0 janelas.

Medido num vídeo real: 115 MB → 15 MB (-87%), PSNR 46,5 dB. Capa PNG: 1,8 → 1,0 MB.
