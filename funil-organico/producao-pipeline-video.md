# 🎬 Pipeline de Produção de Vídeo — garimpagem ao post, do jeito que escala

O fluxo completo de produção de quem já roda volume: da mineração ao vídeo publicado. Insights de campo. O mantra que atravessa tudo: **volume sem perfeccionismo, porque o vídeo não converte, quem converte é a VSL.**

- **Status:** ✅ campo

## 1. Garimpagem (a mineração automatizada)

- Skill de decupagem instalada no Claude Code (repositório do GitHub): cola o link do Facebook ou TikTok, ela **baixa o vídeo, transcreve e devolve a copy mais o prompt decupado.** A transcrição roda via API de Whisper (Groq).
- O prompt de decupagem precisa ser bem feito, senão sai porco.
- **Fonte de ideias número 1: Amazon Ultra.** Afiliados de Amazon vendem produtos comuns (limpeza, peróxido, pet) com vídeos que escalam a milhões de views. **Amazon converte MAIS que Nutra por causa da credibilidade da marca** (mas paga comissão menor). Modelar o FORMATO que escalou e adaptar pra nossa copy e produto.
- Facebook é a fonte mais validada de ideia. TikTok por palavra chave serve de ideia também, com mais risco. **Não copiar da biblioteca de anúncios** (não funciona). Modelar é pegar a IDEIA e o formato, nunca o vídeo nem a copy literal (pra Amazon, criar a sua própria copy).

## 2. O agente cloud (o cérebro da produção)

- Um agente do Claude Code configurado a dedo, através de muito teste, pra devolver **prompt realista** já pronto.
- Ele pega a copy, **decupa em cenas de 8 segundos** (conta as palavras, separa certinho, porque a copy inteira não cabe num take), e devolve **imagem 1, 2, 3 mais take 1, 2, 3** com os elementos visuais de cada cena.
- A base de prompt foi clonada de um nicho hot (estrutura em JSON) e adaptada pro nicho, pedindo nível de realismo alto em todos os vídeos. Esse agente bem calibrado é o ativo mais valioso do processo.
- **Modelo:** pra conteúdo mais black (ED), usar Claude 4.6, porque 4.8 dá guardrail. Esforço médio (economia de token, o volume é grande).
- Rodar sempre na mesma conversa pra o agente manter memória boa do que tem que fazer.

## 3. Geração de imagem (Flow, Nano Banana Pro)

- No Flow, com Nano Banana Pro, formato 9:16, **gerar 4 imagens por prompt** e escolher a melhor. No lower priority isso não gasta crédito.
- Critério de escolha é visual e ganha no feeling: a mais real, sem bug (sem 6 dedos, sem mão dentro do pote, sem membro cortado gritante). Bug pequeno passa, o negócio é volume.
- **Consistência: usar a primeira imagem escolhida como BASE de todas as outras.** Incluir ela no comando das próximas e readicionar o personagem a cada nova imagem, pra manter a cara igual. Numerar imagem 1, 2, 3 no próprio prompt pra não se perder no meio do volume.

## 4. Geração de vídeo (Veo 3, lower priority)

- Cada take casa com uma imagem. Fazer uma imagem só com o take inteiro perde dinâmica e qualidade, não viraliza igual.
- **Usar FRAMES, nunca "elementos".** Elemento só pega a característica do personagem e erra a cena inteira. Frames 9:16.
- Lower priority permite gerar x4; se não tiver lower priority, usar light (gasta menos) e gerar uma vez só.
- Cada cena é 8 segundos, por isso a copy tem que ser decupada em cenas antes.

## 5. Custo (o segredo da escala barata)

- **Veo 3 no lower priority é infinito e não cobra crédito.** Acesso via rateio do Google Ultra no modo "família" (o email entra como membro, 6 ou 7 pessoas dividem o plano, custo por cabeça na casa de pouco mais de cem reais no plano maior).
- **O lower priority só funciona MANUAL, não via API.** É o que trava a automação total da geração.
- Veo 3 fora do rateio custa caro. Vertex AI e qualquer rota de API saem caro demais pro volume. É por isso que a produção em massa ainda depende de trabalho manual.

## 6. Edição (CapCut, sem perfeccionismo)

- Jogar os takes numerados no CapCut, cortar o silêncio manualmente entre eles, gerar legenda (atalho Alt mais G), escolher um estilo de legenda, exportar. Simples e rápido.
- Cloud Code faz corte de silêncio via FFmpeg, mas a legenda tem que ser gerada em Python (não dá pra copiar a do CapCut). Editor automático que junta takes numerados, tira silêncio e legenda existe, mas é ferramenta paga à parte.
- **Formato talking head alternativo:** vídeo real (ou do avatar Veo) ao lado, remover o fundo no CapCut (mascarar, remoção automática) e colocar um vídeo de fundo. Modelo de página estilo Amazon.

## 7. Duração e a regra do volume

- Vídeos entre 10 e 40 segundos. **Nutra de ED tipicamente 10 a 13 segundos:** hook mais fala mais o CTA de comentar. O CTA principal é sempre comentar a palavra chave.
- **Volume vence perfeccionismo.** O vídeo não converte, a VSL converte. Descartar take só se o bug for gritante.
- **Repetir copy que funcionou:** uma copy que performou vira 4 vídeos daquela copy, misturada com outras 2. Pegou muita view, repete junto, posta de novo depois. Modelar funciona e repetir também.

## Conexões
- [Contas e Páginas](operacao-contas-paginas.md) · [Automação e CTA](operacao-automacao-cta.md) · [Estratégia de Mercado](estrategia-mercado-oferta.md)
- [Diretrizes do Script de 32s](diretrizes-script-32s.md) · [Direção de Cena Veo 3](../recursos/veo3-direcao-de-cena.md) · [Veo 3 Avançado](../recursos/veo3-avancado.md)
