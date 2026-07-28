# 🤖 Automação e Mecânica de CTA — comment to DM sem tomar ban

Como o comentário vira venda, e o erro que derruba página. Insights de campo de operadores que já escalaram. A automação nativa do Meta é o "ManyChat de graça".

- **Status:** ✅ campo

## A mecânica em uma frase

Vídeo com copy → a pessoa comenta a palavra chave (`GELATIN`) pra receber o conteúdo → a automação dispara uma DM com o link da **bridge page** no privado.

> ⚠️ **Corrigido em 2026-07-28.** Esta linha dizia "link da VSL" e mandava repetir o link
> "na descrição do post e na bio" — as duas coisas estão erradas e a segunda contradizia
> a regra de "só DM" logo abaixo, no próprio documento.
> - A DM entrega a **bridge**, nunca a VSL direta: sem a bridge o `?p=` se perde e a
>   venda entra sem atribuição de página.
> - **Nada de link público** (bio, descrição, comentário fixado): expõe o mecanismo do
>   funil e ajuda a Meta a fingerprintar a operação.

## Só DM, NUNCA resposta de comentário (a regra que salva a página)

- **A automação SÓ pode mandar DM. Nunca responder o comentário.** Resposta de comentário é o que dispara spam e bloqueio quando a página cresce.
- Na configuração da automação, **remover o campo de resposta ao comentário.** O link vai pra pessoa via DM, mas não aparece resposta pública embaixo do comentário.
- **DM aguenta volume:** mil disparos de DM no dia não dá B.O. O que dá B.O. é resposta de comentário.
- Quando a página crescer muito, **desativar os comentários** de vez, pra não acumular sinal de spam.

## Configuração (Meta Business Suite)

- Caminho: Meta Business Suite → Caixa de entrada → Automações → "Comente para enviar mensagem".
- Colocar a palavra chave (maiúscula e minúscula), o link curto na DM (mensagem enxuta, sem encher linguiça), e um nome interno na automação (como nome de campanha, só pra você achar).
- ⚠️ **"Precisa do Instagram conectado" — NÃO se confirmou na nossa operação.** Este era
  um insight de campo de terceiros. As duas automações que já rodam aqui (Joe e Matt)
  foram configuradas com **canal Messenger e Instagram desmarcado**, e funcionam.
  Siga o passo a passo validado em
  [`automacao-comentario-dm.md`](automacao-comentario-dm.md) — e veja abaixo por que
  conectar o Instagram é risco alto pro nosso nicho.

## Por que NÃO automatizar via API (a armadilha do checkpoint)

- **A API/MCP do Facebook não serve pra automação de operação.** A API muda o tempo todo. Qualquer comando que a API não reconhecer no momento do disparo gera checkpoint, porque o sistema entende que algo mudou e você não acompanhou.
- Operadores de tráfego pago que rodam milhões já perderam dezenas de páginas e BMs por isso. Não é problema de comando ruim, é a instabilidade da própria API.
- Diferente do Google/YouTube, onde dá pra automatizar subida e análise de criativo via API. No Facebook, não.
- **Postagem automática, se um dia rolar, tem que ser click by click** (macro movendo o mouse, um SaaS que simula o clique humano), sem vínculo de API com o Facebook. Ideia em discussão, não validada: SaaS numa droplet que fica ligado e posta sozinho movendo o mouse na hora certa, página por página. Risco conhecido: se qualquer botão ou zoom mudar de lugar, o macro quebra.

## Instagram: risco alto, evitar pra Nutra de velho

- **Perder um Instagram derruba todos os Instagram conectados e até o perfil pessoal.** Diferente do Facebook, que derruba uma página isolada. Já teve operador que quase perdeu tudo por postar num Insta que tomou violação.
- **Velho americano não usa Instagram.** Pra Nutra de público 50 mais US, o canal é só Facebook. Instagram serve pra outros produtos/públicos.
- Cross posting automático entre redes é arriscado e pode gerar violação.

## Conexões
- [Contas e Páginas](operacao-contas-paginas.md) · [Pipeline de Produção](producao-pipeline-video.md) · [Estratégia de Mercado](estrategia-mercado-oferta.md)
- [Arquitetura do Funil](arquitetura-do-funil.md)
