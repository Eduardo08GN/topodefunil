#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
traducao_dados.py — a tabela EN->PT da copy dos agentes.

TERMOS: preenchedores de slot ({o}, {ing}, {s}, {eco}...) — pedaços de frase.
PT:     templates de fala inteiros. A chave é o template EN literal do motor,
        com os slots preservados; o valor é o mesmo template em português.

⛔ COPY NOVA ENTRA AQUI NO MESMO COMMIT. Ver traducao_pt.py --checar.
"""

# ======================================================================
# de dados_pt.py
# ======================================================================
# -*- coding: utf-8 -*-
"""
dados_pt.py — a tabela de tradução. LOCAL DO LUCAS, nunca versionado.

TERMOS: preenchedores de slot ({o}, {ing}, {eco}, {evento}...) — pedaços de
        frase, sem ponto final.
PT:     templates de fala inteiros. A chave é o template EN literal do motor,
        com os slots preservados; o valor é o mesmo template em português.

⚠️ O travessão dos motores às vezes chega como "—" e às vezes corrompido pelo
console. O casamento roda sobre texto normalizado (ver traducao._limpo), então
a forma do traço na chave não importa.

Cobertura por motor no fim do arquivo (COBERTURA), conferida pelo build.
"""

# ---------------------------------------------------------------------------
# TERMOS — preenchedores de slot
# ---------------------------------------------------------------------------
TERMOS = {
    # o núcleo do órgão ({o}). O app mostra a copy limpa; o TAKE leva a grafia
    # fonética (soljer, weiner...), então as duas formas entram.
    # ⚠️ TODOS masculinos de propósito: os templates dizem "o seu {o}" / "o meu
    # {o}", e um termo feminino aqui produziria "o seu pistola". Gênero se
    # resolve na escolha do termo, não com lógica de concordância no motor.
    "johnson": "Johnson", "john-son": "Johnson",
    "soldier": "soldado", "soljer": "soldado",
    "pecker": "pinto", "peck-er": "pinto",
    "manhood": "membro", "man-hood": "membro",
    "wiener": "salsichão", "weiner": "salsichão",
    "tool": "equipamento", "toole": "equipamento",
    "old boy": "velho companheiro",
    "willy": "pipi", "winner": "campeão",

    # {ing} — o preparo do ritual (NECROSE)
    "a spoonful of gelatin into a glass of cold water":
        "uma colher de gelatina num copo de água gelada",
    "a spoonful of gelatin into a jar of baking soda":
        "uma colher de gelatina num pote de bicarbonato",
    "a spoonful of gelatin and a spoon of honey into warm water":
        "uma colher de gelatina e uma colher de mel na água morna",
    "a spoonful of gelatin into cold water with fresh lemon":
        "uma colher de gelatina na água gelada com limão fresco",
}

# ---------------------------------------------------------------------------
# PT — templates de fala
# ---------------------------------------------------------------------------
PT = {}

# --------------------------------------------------------------- NECROSE
PT.update({
    # HOOKS
    "If you want your {o} to go from this to this in one month, watch close.":
        "Se você quer que o seu {o} saia disto aqui pra isto aqui em um mês, presta atenção.",
    "If your {o} looks more like this one than that one, watch close, brother.":
        "Se o seu {o} está mais parecido com este aqui do que com aquele ali, presta atenção, irmão.",
    "Nobody wants this one. If you want your {o} to look like that one, watch close.":
        "Ninguém quer este aqui. Se você quer que o seu {o} fique parecido com aquele ali, presta atenção.",
    "If you had to pick tonight, is your {o} this one or that one?":
        "Se você tivesse que escolher hoje à noite, o seu {o} é este aqui ou aquele ali?",

    # CAUSAS
    "Doctors call this getting older. It isn't. The blood flow to your {o} got strangled, and that is fixable.":
        "Os médicos chamam isso de envelhecer. Não é. O fluxo de sangue até o seu {o} foi estrangulado, e isso tem conserto.",
    "It's not age and it's not you. Something squeezed the blood flow to your {o} shut, and nobody told you.":
        "Não é idade e não é você. Alguma coisa fechou o fluxo de sangue até o seu {o}, e ninguém te contou.",
    "Nobody is born with this. Your {o} got here because the blood flow to it got shut down, year after year.":
        "Ninguém nasce assim. O seu {o} chegou nesse estado porque o fluxo de sangue até ele foi sendo fechado, ano após ano.",
    "This is not what age does to a man, brother. This is what happens when the blood flow to your {o} gets choked off.":
        "Isso não é o que a idade faz com um homem, irmão. Isso é o que acontece quando o fluxo de sangue até o seu {o} é sufocado.",

    # RECEITAS_FALA
    "Stir {ing}. One minute. That's the gelatin trick — do it before your {o} quits for good.":
        "Mexe {ing}. Um minuto. Esse é o truque da gelatina — faz isso antes que o seu {o} desista de vez.",
    "Stir {ing}. That is the whole gelatin trick, and it is what walked my {o} back.":
        "Mexe {ing}. Esse é o truque da gelatina inteiro, e foi o que trouxe o meu {o} de volta.",
    "Stir {ing}. That's the gelatin trick, and your {o} feels it inside a week.":
        "Mexe {ing}. Esse é o truque da gelatina, e o seu {o} sente em menos de uma semana.",
    "Tonight, stir {ing}. They call it the gelatin trick. Your {o} took years to get this bad.":
        "Hoje à noite, mexe {ing}. Chamam isso de truque da gelatina. O seu {o} levou anos pra ficar assim de ruim.",

    # PROVAS
    "Nineteen days of the gelatin trick and my {o} came back like this. {barreira}":
        "Dezenove dias do truque da gelatina e o meu {o} voltou assim. {barreira}",
    "One month of the gelatin trick, and this is what I carry now. My {o} has not quit since. {barreira}":
        "Um mês do truque da gelatina, e é isto que eu carrego agora. O meu {o} não falhou mais desde então. {barreira}",
    "That rotten one on the stand was me last year. This is my {o} today. {barreira}":
        "Aquele podre no suporte era eu no ano passado. Este é o meu {o} hoje. {barreira}",
    "This is my {o} after one month of that trick. {barreira}":
        "Este é o meu {o} depois de um mês desse truque. {barreira}",

    # BARREIRAS
    "A trick you can do from the comfort of your own home.":
        "Um truque que você pode fazer no conforto da sua casa.",
    "Costs less than a cup of coffee and nobody sees you buy it.":
        "Custa menos que um café e ninguém te vê comprando.",
    "No doctor, no pharmacy counter, nobody has to know.":
        "Sem médico, sem balcão de farmácia, ninguém precisa saber.",
    "Nothing to fill, nothing to explain to anybody.":
        "Nada pra aviar, nada pra explicar pra ninguém.",
    "You do it in your own kitchen, in about a minute.":
        "Você faz na sua própria cozinha, em mais ou menos um minuto.",

    # PACING
    "A month from tonight you won't recognise yourself.":
        "Daqui a um mês você não vai se reconhecer.",
    "Next Friday night she'll ask what changed.":
        "Sexta que vem, à noite, ela vai perguntar o que mudou.",
    "Next Friday night, when she asks what changed, you'll remember this.":
        "Sexta que vem, à noite, quando ela perguntar o que mudou, você vai lembrar disso.",

    # CTAS
    "{pacing} Comment gelatin, and I'll send you the exact one I use. {gate}":
        "{pacing} Comenta GELATIN que eu te mando exatamente o que eu uso. {gate}",
    "{pacing} Comment gelatin, and I'll send you the only one I trust. {gate}":
        "{pacing} Comenta GELATIN que eu te mando o único em que eu confio. {gate}",
    "{pacing} Comment gelatin, and I'll send you the recipe. {gate}":
        "{pacing} Comenta GELATIN que eu te mando a receita. {gate}",
    "{pacing} Comment gelatin, and I'll send you where I get mine. {gate}":
        "{pacing} Comenta GELATIN que eu te mando onde eu compro o meu. {gate}",

    # GATES
    "Follow me first, or I won't have any way to find your comment, brother.":
        "Me segue primeiro, senão eu não vou ter como achar o seu comentário, irmão.",
    "Follow me first, or my message never lands.":
        "Me segue primeiro, senão minha mensagem não chega.",
    "Hit follow right now, or Facebook can't deliver it.":
        "Aperta seguir agora, senão o Facebook não consegue entregar.",

    # NECROSE SHORT — as fundidas
    "It's not age — the blood flow got strangled. Stir {ing}. That's the gelatin trick, and my {o} hasn't quit since.":
        "Não é idade — o fluxo de sangue foi estrangulado. Mexe {ing}. Esse é o truque da gelatina, e o meu {o} não falhou mais desde então.",
    "Stir {ing}. That's the gelatin trick — it opens the blood flow your {o} lost. Mine came back like this.":
        "Mexe {ing}. Esse é o truque da gelatina — ele abre o fluxo de sangue que o seu {o} perdeu. O meu voltou assim.",
    "Stir {ing}. That's the gelatin trick, and the blood flow came back. So did my {o}.":
        "Mexe {ing}. Esse é o truque da gelatina, e o fluxo de sangue voltou. O meu {o} também.",
    "That's blood flow, choked off. Stir {ing} — the whole gelatin trick, and it walked my {o} back.":
        "Isso é fluxo de sangue sufocado. Mexe {ing} — o truque da gelatina inteiro, e foi o que trouxe o meu {o} de volta.",
    "The blood flow to your {o} got choked off. Stir {ing}. That's the gelatin trick, and this is me now.":
        "O fluxo de sangue até o seu {o} foi sufocado. Mexe {ing}. Esse é o truque da gelatina, e este sou eu agora.",
})

# --------------------------------------------------------------- FLAGRANTE
TERMOS.update({
    # {evento} — a ocasião pública onde a humilhação acontece
    "that christmas party": "aquela festa de Natal",
    "that anniversary party": "aquela festa de aniversário de casamento",
    "that company meeting": "aquela reunião da empresa",
    "that dinner table": "aquela mesa de jantar",
    # {eco} — o mesmo lugar do hook, na cena da redenção
    "same backyard, same crowd": "no mesmo quintal, com a mesma turma",
    "same clubhouse table": "na mesma mesa do clube",
    "same conference room": "na mesma sala de reunião",
    "same dinner table": "na mesma mesa de jantar",
    "same dock, same crew": "no mesmo píer, com a mesma turma",
    "same hall, same song": "no mesmo salão, com a mesma música",
    "same reception hall": "no mesmo salão de festas",
    "the next company party": "na festa seguinte da empresa",
    # {quem} — quem passou o truque
    "a guy from the shop": "um cara da oficina",
    "an old army friend": "um velho amigo do exército",
    # {brag}
    "spreading the gossip herself": "espalhando a fofoca ela mesma",
})

PT.update({
    # HOOKS
    "The whole {evento} had heard the gossip that his {o} quit on him. His hangs just like this.":
        "{evento} inteira já tinha ouvido a fofoca de que o {o} dele desistiu. O dele pende assim ó.",
    "Everyone at {evento} had already heard the gossip that his {o} doesn't work anymore. His hangs just like this.":
        "Todo mundo em {evento} já tinha ouvido a fofoca de que o {o} dele não funciona mais. O dele pende assim ó.",
    "Word got around {evento} that his {o} doesn't work anymore. His hangs just like this.":
        "Correu em {evento} que o {o} dele não funciona mais. O dele pende assim ó.",
    "Every man at {evento} had heard the gossip that his {o} can't stand up anymore. His hangs like this.":
        "Todo homem em {evento} tinha ouvido a fofoca de que o {o} dele não levanta mais. O dele pende assim.",
    "Every guy at {evento} had heard the gossip that his {o} can't finish anymore. She knows it. His hangs down like this.":
        "Todo cara em {evento} tinha ouvido a fofoca de que o {o} dele não termina mais. Ela sabe. O dele pende pra baixo assim.",
    "Half the people at {evento} had heard the gossip that his {o} can't get hard anymore. His hangs over his own fingers.":
        "Metade do pessoal em {evento} tinha ouvido a fofoca de que o {o} dele não fica duro mais. O dele pende por cima dos próprios dedos.",
    "Every husband at {evento} had heard the gossip that his {o} quit and his wife stopped asking. His stays folded like this.":
        "Todo marido em {evento} tinha ouvido a fofoca de que o {o} dele desistiu e a mulher parou de pedir. O dele fica dobrado assim.",
    "The women at {evento} had already heard the gossip that his {o} stopped working. His wife told them. His droops like this.":
        "As mulheres em {evento} já tinham ouvido a fofoca de que o {o} dele parou de funcionar. A esposa contou. O dele murcha assim.",
    "Nobody at {evento} was surprised. They'd heard the gossip that his {o} hasn't worked in two years. His stays down like this.":
        "Ninguém em {evento} se surpreendeu. Tinham ouvido a fofoca de que o {o} dele não funciona há dois anos. O dele fica caído assim.",
    "Neighbors at {evento} heard the gossip that his {o} went soft. I stopped reaching for my wife. His sags off his fingers.":
        "Os vizinhos em {evento} ouviram a fofoca de que o {o} dele amoleceu. Eu parei de procurar minha esposa. O dele escorre dos dedos.",
    "Everybody at {evento} heard the gossip that his {o} went dead on him. I was that man. His curls over his thumb.":
        "Todo mundo em {evento} ouviu a fofoca de que o {o} dele morreu. Eu fui esse homem. O dele enrola por cima do polegar.",
    "His crew at {evento} heard the gossip that his {o} gave out on him. Mine did too. His sinks into his lap.":
        "A turma dele em {evento} ouviu a fofoca de que o {o} dele falhou. O meu também falhou. O dele afunda no colo.",
    "Cousins at {evento} heard the gossip that his {o} shut down. That was me at sixty. His hides in his own fist.":
        "Os primos em {evento} ouviram a fofoca de que o {o} dele desligou. Esse era eu aos sessenta. O dele se esconde no próprio punho.",

    # DESCOBERTAS
    "That's when {quem} gave him the gelatin trick. It's not age. Right here, the blood flow to your {o} got choked off.":
        "Foi aí que {quem} passou pra ele o truque da gelatina. Não é idade. Bem aqui, o fluxo de sangue até o seu {o} foi sufocado.",
    "That's when {quem} pulled him aside and gave him the gelatin trick. It's not age, brother, the blood flow to your {o} got choked off.":
        "Foi aí que {quem} puxou ele de lado e passou o truque da gelatina. Não é idade, irmão, o fluxo de sangue até o seu {o} foi sufocado.",
    "That's when {quem} handed him the gelatin trick. It's not age, brother, your {o} got its blood flow choked off.":
        "Foi aí que {quem} entregou pra ele o truque da gelatina. Não é idade, irmão, o seu {o} teve o fluxo de sangue sufocado.",
    "That's when {quem} leaned over and whispered the gelatin trick. It's not your age, brother, and it's not you. The blood stopped reaching your {o}.":
        "Foi aí que {quem} se inclinou e sussurrou o truque da gelatina. Não é a sua idade, irmão, e não é você. O sangue parou de chegar no seu {o}.",
    "That's when {quem} finally told him about the gelatin trick. Your wife isn't bored, brother, and you're not done. The blood stopped filling your {o}.":
        "Foi aí que {quem} finalmente contou pra ele do truque da gelatina. Sua esposa não está entediada, irmão, e você não acabou. O sangue parou de encher o seu {o}.",
    "I laughed at the gelatin trick the first time. {quem} wouldn't let him laugh. Give it two days, brother, and the blood finds your {o} again.":
        "Eu ri do truque da gelatina na primeira vez. {quem} não deixou ele rir. Dá dois dias, irmão, e o sangue acha o seu {o} de novo.",
    "{quem} passed him the gelatin trick in a parking lot. Every man I know over sixty is on it now. The blood has to reach your {o}.":
        "{quem} passou pra ele o truque da gelatina num estacionamento. Todo homem que eu conheço acima de sessenta está tomando. O sangue tem que chegar no seu {o}.",

    # RITUAIS
    "That same night he stirred it into a glass and drank it. Do it tonight, before your {o} quits for good.":
        "Naquela mesma noite ele mexeu num copo e bebeu. Faz isso hoje à noite, antes que o seu {o} desista de vez.",
    "That same night he stirred it into a glass and drank it. Do it tonight and stop apologizing for your {o}.":
        "Naquela mesma noite ele mexeu num copo e bebeu. Faz isso hoje à noite e para de pedir desculpa pelo seu {o}.",
    "That same night he stirred it into a glass and drank it. She never saw. Do it tonight for your {o}.":
        "Naquela mesma noite ele mexeu num copo e bebeu. Ela nunca viu. Faz isso hoje à noite pelo seu {o}.",
    "That same night he stirred it into a glass and drank it. Stir it, drink it, give your {o} one week.":
        "Naquela mesma noite ele mexeu num copo e bebeu. Mexe, bebe, e dá uma semana pro seu {o}.",
    "That same night he mixed it into a glass and drank it. Stir it, drink it, and watch your {o} wake up.":
        "Naquela mesma noite ele misturou num copo e bebeu. Mexe, bebe, e vê o seu {o} acordar.",
    "He mixed his glass alone. Us guys do it after the house goes quiet. Stir yours tonight, before your {o} forgets how.":
        "Ele misturou o copo dele sozinho. Nós fazemos depois que a casa silencia. Mexe o seu hoje à noite, antes que o seu {o} esqueça como se faz.",
    "First night I drank mine, I sat on the bed waiting. Stir yours tonight and give your {o} the same chance.":
        "Na primeira noite que eu bebi o meu, sentei na cama esperando. Mexe o seu hoje à noite e dá a mesma chance pro seu {o}.",
    "I drank mine standing at the sink so nobody would ask. He did the same. Stir it tonight, your {o} is waiting.":
        "Eu bebi o meu em pé na pia pra ninguém perguntar. Ele fez igual. Mexe hoje à noite, o seu {o} está esperando.",
    "Nobody in my house buys those pills anymore. He stirred his that night. Stir yours tonight and stop guessing about your {o}.":
        "Ninguém na minha casa compra mais aqueles comprimidos. Ele mexeu o dele naquela noite. Mexe o seu hoje à noite e para de chutar sobre o seu {o}.",
    "This is what we do at my house. One glass, one spoon, before bed. Stir it tonight and let your {o} answer.":
        "É isso que a gente faz lá em casa. Um copo, uma colher, antes de dormir. Mexe hoje à noite e deixa o seu {o} responder.",

    # REDENCOES
    "Nineteen days later, {eco}. His wife is now the one talking. {barreira}":
        "Dezenove dias depois, {eco}. Agora quem fala é a esposa dele. {barreira}",
    "Nineteen days later, {eco}. Mine came back the same way at sixty-five. She hasn't stopped {brag} about his {o} since. {barreira}":
        "Dezenove dias depois, {eco}. O meu voltou do mesmo jeito aos sessenta e cinco. Ela não parou mais de {brag} sobre o {o} dele. {barreira}",
    "Nineteen days later, {eco}. My wife locked our bedroom door at seven in the morning once. Now his wife is {brag} about his {o} to her sisters. {barreira}":
        "Dezenove dias depois, {eco}. Minha esposa trancou a porta do quarto às sete da manhã uma vez. Agora a esposa dele está {brag} sobre o {o} dele pras irmãs. {barreira}",
    "Nineteen days later, {eco}. She stayed on his knee all night, and now she's the one {brag} about his {o}. {barreira}":
        "Dezenove dias depois, {eco}. Ela ficou no joelho dele a noite inteira, e agora é ela quem está {brag} sobre o {o} dele. {barreira}",
    "Nineteen days later, {eco}. She wouldn't get off his knee, and now she's the one {brag} about his {o}. {barreira}":
        "Dezenove dias depois, {eco}. Ela não saía do joelho dele, e agora é ela quem está {brag} sobre o {o} dele. {barreira}",
    "Nineteen days later, {eco}. She's the one reaching for him at six in the morning now, and the one {brag} about his {o}. {barreira}":
        "Dezenove dias depois, {eco}. Agora é ela quem procura ele às seis da manhã, e é ela quem está {brag} sobre o {o} dele. {barreira}",
    "Nineteen days later, {eco}. The same men who laughed asked him what he was taking. She just kept {brag} about his {o}. {barreira}":
        "Dezenove dias depois, {eco}. Os mesmos homens que riram perguntaram o que ele estava tomando. Ela só continuou {brag} sobre o {o} dele. {barreira}",
    "Nineteen days later, {eco}. The same women who whispered about him now hear her {brag} about his {o} instead. {barreira}":
        "Dezenove dias depois, {eco}. As mesmas mulheres que cochichavam dele agora ouvem ela {brag} sobre o {o} dele. {barreira}",
    "Nineteen days later, {eco}. They showed up an hour late because she wouldn't let him out of the bedroom. Now she's the one {brag} about his {o}. {barreira}":
        "Dezenove dias depois, {eco}. Chegaram uma hora atrasados porque ela não deixava ele sair do quarto. Agora é ela quem está {brag} sobre o {o} dele. {barreira}",
    "Nineteen days later, {eco}. This time his {o} stood up before she was even ready, and she's still {brag} about it. {barreira}":
        "Dezenove dias depois, {eco}. Dessa vez o {o} dele levantou antes mesmo de ela estar pronta, e ela continua {brag} sobre isso. {barreira}",

    # BARREIRAS
    "Costs less than a cup of coffee.": "Custa menos que um café.",
    "No doctor, no pharmacy counter.": "Sem médico, sem balcão de farmácia.",
    "Nobody has to know but her.": "Ninguém precisa saber além dela.",
    "Nothing to fill, nothing to explain.": "Nada pra aviar, nada pra explicar.",
    "You never say the words out loud to anybody.":
        "Você nunca diz essas palavras em voz alta pra ninguém.",

    # CTAS
    "Comment gelatin, and I'll send you the only one I trust tonight. {gate}":
        "Comenta GELATIN que hoje à noite eu te mando o único em que eu confio. {gate}",
    "Comment gelatin, and I'll send you that exact one today. {gate}":
        "Comenta GELATIN que hoje eu te mando exatamente esse. {gate}",
    "Comment gelatin, and I'll send you the recipe tonight. {gate}":
        "Comenta GELATIN que hoje à noite eu te mando a receita. {gate}",
    "Comment gelatin, and I'll send you the real source. The stuff on store shelves is watered-down powder. {gate}":
        "Comenta GELATIN que eu te mando a fonte de verdade. O que está na prateleira da loja é pó aguado. {gate}",
    "Comment gelatin, and I'll send it over tonight, so you never have to apologize in the dark again. {gate}":
        "Comenta GELATIN que eu mando hoje à noite, pra você nunca mais ter que pedir desculpa no escuro. {gate}",
    "Comment gelatin, and I'll send you the exact one he used. It shows up in a plain box. {gate}":
        "Comenta GELATIN que eu te mando exatamente o que ele usou. Chega numa caixa sem nada escrito. {gate}",
    "Comment gelatin, and I'll send you the one he got. Nineteen days from tonight, brother. {gate}":
        "Comenta GELATIN que eu te mando o que ele pegou. Dezenove dias a partir de hoje, irmão. {gate}",
    "Comment gelatin, and I'll send you what we pass around here, brother. Nobody outside this comment section finds out. {gate}":
        "Comenta GELATIN que eu te mando o que a gente passa por aqui, irmão. Ninguém fora dessa seção de comentários fica sabendo. {gate}",
    "Comment gelatin, and I'll send you the same one a man sent me at sixty-four. I didn't ask twice. {gate}":
        "Comenta GELATIN que eu te mando o mesmo que um homem me mandou aos sessenta e quatro. Eu não perguntei duas vezes. {gate}",
    "Comment gelatin, and I'll send you the exact one. I typed it myself once, brother, and nobody in my house ever knew. {gate}":
        "Comenta GELATIN que eu te mando exatamente esse. Eu mesmo digitei uma vez, irmão, e ninguém lá em casa soube. {gate}",

    # GATES
    "Follow me first or I can't find your comment.":
        "Me segue primeiro, senão eu não acho o seu comentário.",
    "Follow me first, brother.": "Me segue primeiro, irmão.",
    "Hit follow first, or Facebook won't deliver it.":
        "Aperta seguir primeiro, senão o Facebook não entrega.",

    # FLAGRANTE SHORT — as fundidas
    "That's when {quem} gave him the gelatin trick. It's not age — the blood flow to your {o} got choked off. Nineteen days later she's {brag} about his.":
        "Foi aí que {quem} passou pra ele o truque da gelatina. Não é idade — o fluxo de sangue até o seu {o} foi sufocado. Dezenove dias depois ela está {brag} sobre o dele.",
    "That's when {quem} told him about the gelatin trick. It's blood flow, not you. Nineteen days later the same men who laughed asked about his {o}.":
        "Foi aí que {quem} contou pra ele do truque da gelatina. É fluxo de sangue, não é você. Dezenove dias depois os mesmos homens que riram perguntaram do {o} dele.",
    "{quem} gave him the gelatin trick that night. The blood flow to your {o} got choked off, and it is fixable. Nineteen days later she reaches for him first.":
        "{quem} passou pra ele o truque da gelatina naquela noite. O fluxo de sangue até o seu {o} foi sufocado, e isso tem conserto. Dezenove dias depois é ela quem procura ele primeiro.",
    "{quem} handed him the gelatin trick. Blood flow, brother, not your age. Nineteen days later she wouldn't get off his knee, and his {o} was ready.":
        "{quem} entregou pra ele o truque da gelatina. Fluxo de sangue, irmão, não é a sua idade. Dezenove dias depois ela não saía do joelho dele, e o {o} dele estava pronto.",
    "{quem} pulled him aside with the gelatin trick — the blood flow stopped reaching your {o}. Nineteen days later she's the one {brag} about his.":
        "{quem} puxou ele de lado com o truque da gelatina — o sangue parou de chegar no seu {o}. Dezenove dias depois é ela quem está {brag} sobre o dele.",
})

# --------------------------------------------------------------- PEE
TERMOS.update({
    "that checkout line": "aquela fila do caixa",
    "that gas station": "aquele posto de gasolina",
    "that hardware store": "aquela loja de ferragens",
    "that produce aisle": "aquele corredor de hortifrúti",
    "the same aisle": "no mesmo corredor",
    "the same checkout line": "na mesma fila do caixa",
    "the same pharmacy counter": "no mesmo balcão da farmácia",
    "the same produce aisle": "no mesmo corredor de hortifrúti",
    "the same store counter": "no mesmo balcão da loja",
    "the same tool aisle": "no mesmo corredor de ferramentas",
    # {peca} — a roupa que mancha
    "cream linen trousers": "a calça de linho creme",
    "light gray sweatpants": "o moletom cinza-claro",
    "light khaki cargo shorts": "a bermuda cargo cáqui clara",
    "pale tan work pants": "a calça de trabalho bege",
})

PT.update({
    # HOOKS
    "He wet his pants in {evento} and everybody saw. Poor guy... same reason his {o} quit on him.":
        "Ele mijou nas calças em {evento} e todo mundo viu. Coitado... o mesmo motivo pelo qual o {o} dele desistiu.",
    "He peed himself in {evento} because he couldn't hold it in. Poor guy... same thing killed his {o} two years ago.":
        "Ele se mijou em {evento} porque não conseguiu segurar. Coitado... a mesma coisa matou o {o} dele dois anos atrás.",
    "He lost it right there in {evento}. Poor guy... and that's why his {o} hasn't worked in two years.":
        "Ele perdeu o controle bem ali em {evento}. Coitado... e é por isso que o {o} dele não funciona há dois anos.",
    "He soaked right through in {evento}. Poor guy... same thing that made him leak is why his {o} doesn't work.":
        "Ele encharcou tudo em {evento}. Coitado... a mesma coisa que fez ele vazar é o motivo do {o} dele não funcionar.",
    "He peed his pants in {evento}. His brother in law still tells that story. Same thing shut his {o} down.":
        "Ele mijou nas calças em {evento}. O cunhado dele ainda conta essa história. A mesma coisa desligou o {o} dele.",
    "He wet his pants in {evento}. His wife wasn't even surprised. Same reason his {o} stopped working two years back.":
        "Ele mijou nas calças em {evento}. A esposa dele nem se surpreendeu. O mesmo motivo pelo qual o {o} dele parou de funcionar dois anos atrás.",
    "He soaked his pants in {evento}. His wife stopped reaching for him two years ago. Same reason his {o} plays dead.":
        "Ele encharcou as calças em {evento}. A esposa parou de procurar ele dois anos atrás. O mesmo motivo pelo qual o {o} dele se faz de morto.",
    "He started leaking in {evento}. His wife already told her friends about it. Same reason his {o} does nothing.":
        "Ele começou a vazar em {evento}. A esposa já contou pras amigas. O mesmo motivo pelo qual o {o} dele não faz nada.",
    "He leaked down his leg in {evento}. Hasn't asked a woman out since the divorce. Same reason his {o} stays down.":
        "Escorreu pela perna dele em {evento}. Não chamou nenhuma mulher pra sair desde o divórcio. O mesmo motivo pelo qual o {o} dele fica caído.",
    "He peed right there in {evento}. That was me in 2019. Same reason my {o} went out that year.":
        "Ele mijou bem ali em {evento}. Esse era eu em 2019. O mesmo motivo pelo qual o meu {o} apagou naquele ano.",
    "He peed in {evento} today. I did the same in 2019. Every man I know has. Same thing took our {o}.":
        "Ele mijou em {evento} hoje. Eu fiz igual em 2019. Todo homem que eu conheço já fez. A mesma coisa levou o nosso {o}.",
    "She said it was fine when he peed in {evento}. She says that in bed too. Same reason his {o} quit.":
        "Ela disse que tudo bem quando ele mijou em {evento}. Ela diz isso na cama também. O mesmo motivo pelo qual o {o} dele desistiu.",

    # MANCHA (descrição usada na fala)
    "a large dark patch of wet fabric across the front of his {peca}":
        "uma mancha escura e grande de tecido molhado na frente d{peca}",
    "a large dark wet stain spreading across the front of his {peca}":
        "uma mancha escura e molhada se espalhando na frente d{peca}",
    "his {peca} are soaked dark down the front":
        "{peca} dele está encharcada e escura na frente",

    # MECANISMOS
    "It's his prostate squeezing the pipe shut. Same pressure keeps the blood out of your {o}.":
        "É a próstata dele apertando o cano até fechar. A mesma pressão mantém o sangue fora do seu {o}.",
    "It's the prostate choking the line. The same squeeze is why your {o} can't fill anymore.":
        "É a próstata sufocando a linha. O mesmo aperto é o motivo do seu {o} não encher mais.",
    "His prostate is clamping down on the pipe. That same pressure is what starves your {o}.":
        "A próstata dele está prensando o cano. Essa mesma pressão é o que mata o seu {o} de fome.",
    "It's not his age. His prostate swelled up and pinched the pipe. Same pinch is why no blood gets to your {o}.":
        "Não é a idade dele. A próstata inchou e beliscou o cano. O mesmo beliscão é o motivo de nenhum sangue chegar no seu {o}.",
    "Picture a boot standing on a garden hose. That's his prostate on the line, and it's why your {o} won't fill.":
        "Imagina uma bota pisando numa mangueira de jardim. É a próstata dele em cima da linha, e é por isso que o seu {o} não enche.",
    "Pills don't touch this. It's his prostate pressing the line flat, and that same press is why your {o} can't fill.":
        "Comprimido não resolve isso. É a próstata dele achatando a linha, e essa mesma pressão é o motivo do seu {o} não encher.",
    "Blood doesn't reach your {o} anymore. It's the same prostate pinching the same line that sends him to the bathroom all night.":
        "O sangue não chega mais no seu {o}. É a mesma próstata beliscando a mesma linha que manda ele pro banheiro a noite inteira.",
    "The dripping came first. That's his prostate closing the pipe, and it closes on your {o} a year or two later.":
        "O gotejamento veio primeiro. É a próstata dele fechando o cano, e ela fecha no seu {o} um ou dois anos depois.",
    "His doctor treated the bladder and never mentioned the rest. Same prostate pressing the same pipe is what took your {o} down.":
        "O médico dele tratou a bexiga e nunca mencionou o resto. A mesma próstata prensando o mesmo cano é o que derrubou o seu {o}.",
    "They never told him why, because a fixed man buys nothing. His prostate is sitting on that pipe and shutting your {o} down.":
        "Nunca contaram o porquê pra ele, porque homem resolvido não compra nada. A próstata dele está sentada nesse cano e desligando o seu {o}.",
    "They'll call it two different problems. It's one. His prostate is on the pipe, and that's why your {o} stays down.":
        "Vão chamar de dois problemas diferentes. É um só. A próstata dele está em cima do cano, e é por isso que o seu {o} fica caído.",
    "Us guys all have the same prostate leaning on the same line. That's why we drip, and that's why our {o} sleeps through it.":
        "Nós todos temos a mesma próstata apoiada na mesma linha. É por isso que a gente pinga, e é por isso que o nosso {o} dorme durante tudo.",
    "I know this one. My prostate grew over the line and closed it. I leaked. Then my {o} went half. Then nothing.":
        "Eu conheço essa. Minha próstata cresceu por cima da linha e fechou. Eu vazei. Depois o meu {o} foi pela metade. Depois nada.",

    # RITUAIS
    "That's when a buddy handed him the gelatin trick. He drank it that same night. Stir it, drink it, and watch your {o} wake up.":
        "Foi aí que um amigo entregou pra ele o truque da gelatina. Ele bebeu naquela mesma noite. Mexe, bebe, e vê o seu {o} acordar.",
    "That's when his brother gave him the gelatin trick. He stirred it into a glass that same night. Give your {o} one week.":
        "Foi aí que o irmão dele passou o truque da gelatina. Ele mexeu num copo naquela mesma noite. Dá uma semana pro seu {o}.",
    "That's when his son-in-law gave him the gelatin trick. He mixed it into a glass that night. Do it before your {o} quits for good.":
        "Foi aí que o genro passou pra ele o truque da gelatina. Ele misturou num copo naquela noite. Faz isso antes que o seu {o} desista de vez.",
    "A guy at the barbershop gave him the gelatin trick. He stirred a spoonful into cold water before bed. Do it tonight and your {o} answers by Friday.":
        "Um cara da barbearia passou pra ele o truque da gelatina. Ele mexeu uma colher na água gelada antes de dormir. Faz isso hoje à noite e o seu {o} responde até sexta.",
    "An old army buddy called him that night with the gelatin trick. One spoon, warm water, stirred slow. Do the same tonight and give your {o} nine days.":
        "Um velho amigo do exército ligou pra ele naquela noite com o truque da gelatina. Uma colher, água morna, mexida devagar. Faz igual hoje à noite e dá nove dias pro seu {o}.",
    "His fishing partner gave him the gelatin trick. He mixed it in the kitchen that same night. Give your {o} two weeks and stop saying sorry in the dark.":
        "O parceiro de pescaria passou pra ele o truque da gelatina. Ele misturou na cozinha naquela mesma noite. Dá duas semanas pro seu {o} e para de pedir desculpa no escuro.",
    "His nephew texted him the gelatin trick. He mixed a spoonful into his morning drink. Do the same and your {o} wakes up before you do.":
        "O sobrinho mandou pra ele o truque da gelatina por mensagem. Ele misturou uma colher na bebida da manhã. Faz igual e o seu {o} acorda antes de você.",
    "I found the gelatin trick in 2019, brother. I stirred one spoon into cold water that night. Nine days later my {o} answered.":
        "Eu achei o truque da gelatina em 2019, irmão. Mexi uma colher na água gelada naquela noite. Nove dias depois o meu {o} respondeu.",
    "The gelatin trick is what we do at home now. A spoonful in half a glass of cold water. Your {o} shows up before the weekend.":
        "O truque da gelatina é o que a gente faz em casa agora. Uma colher em meio copo de água gelada. O seu {o} aparece antes do fim de semana.",

    # REDENCOES
    "Nineteen days later he walked back into {eco} dry, head up. Now she's the one bragging about his {o}. {barreira}":
        "Dezenove dias depois ele voltou {eco} seco, de cabeça erguida. Agora é ela quem se gaba do {o} dele. {barreira}",
    "Nineteen days later he was back in {eco}, dry and standing tall. Now she won't stop talking about his {o}. {barreira}":
        "Dezenove dias depois ele estava de volta {eco}, seco e de cabeça erguida. Agora ela não para de falar do {o} dele. {barreira}",
    "Eighteen days later he was back in {eco} dry, chin up. She reaches for him first now. His {o} never quits. {barreira}":
        "Dezoito dias depois ele estava de volta {eco} seco, queixo erguido. Agora é ela quem procura ele primeiro. O {o} dele nunca falha. {barreira}",
    "Sixteen days later he walked into {eco} dry, head up. His {o} left her needing a minute to catch her breath. {barreira}":
        "Dezesseis dias depois ele entrou {eco} seco, de cabeça erguida. O {o} dele deixou ela precisando de um minuto pra recuperar o fôlego. {barreira}",
    "Twenty four days later he walked into {eco} dry, head up. Now she asks for a night off from his {o}. {barreira}":
        "Vinte e quatro dias depois ele entrou {eco} seco, de cabeça erguida. Agora ela pede uma noite de folga do {o} dele. {barreira}",
    "Twenty six days later he was back in {eco} dry, head high. She says his {o} wakes up before the alarm. {barreira}":
        "Vinte e seis dias depois ele estava de volta {eco} seco, cabeça erguida. Ela diz que o {o} dele acorda antes do despertador. {barreira}",

    # CTAS
    "Comment gelatin, and I'll send the same one he used. {gate}":
        "Comenta GELATIN que eu mando o mesmo que ele usou. {gate}",
    "Comment gelatin, and I'll send you the one we use at home. {gate}":
        "Comenta GELATIN que eu te mando o que a gente usa em casa. {gate}",
    "Comment gelatin, and I'll send you where to get the right one. {gate}":
        "Comenta GELATIN que eu te mando onde comprar o certo. {gate}",
    "Comment gelatin, and I'll send you the source. I can't name it here. {gate}":
        "Comenta GELATIN que eu te mando a fonte. Eu não posso citar aqui. {gate}",
    "Comment gelatin, and thank me Friday night. I'll send it over today. {gate}":
        "Comenta GELATIN, e me agradece sexta à noite. Eu mando hoje. {gate}",
    "Comment gelatin, tonight. Somebody always reports this and the video goes down by morning. {gate}":
        "Comenta GELATIN, hoje à noite. Sempre tem alguém que denuncia e o vídeo cai até de manhã. {gate}",
    "Comment gelatin. The store stuff did nothing for you. I'll send the real one. {gate}":
        "Comenta GELATIN. O de loja não fez nada por você. Eu mando o de verdade. {gate}",
    "One word. Comment gelatin, and it's in your inbox tonight. {gate}":
        "Uma palavra. Comenta GELATIN, e hoje à noite está na sua caixa de entrada. {gate}",

    # PEE SHORT — as fundidas
    "His prostate clamped the pipe shut, and that same pressure shut his {o} down. The gelatin trick opened both. Nineteen days later she reaches for him first.":
        "A próstata dele prensou o cano até fechar, e essa mesma pressão desligou o {o} dele. O truque da gelatina abriu os dois. Dezenove dias depois é ela quem procura ele primeiro.",
    "It's his prostate choking the line — the same squeeze is why your {o} can't fill. One spoon of the gelatin trick, and nineteen days later he was dry.":
        "É a próstata dele sufocando a linha — o mesmo aperto é o motivo do seu {o} não encher. Uma colher do truque da gelatina, e dezenove dias depois ele estava seco.",
    "It's the prostate pressing the line flat — the same squeeze that starves your {o}. His brother gave him the gelatin trick. Nineteen days later he was dry, head up.":
        "É a próstata achatando a linha — o mesmo aperto que mata o seu {o} de fome. O irmão dele passou o truque da gelatina. Dezenove dias depois ele estava seco, de cabeça erguida.",
    "Pills don't touch this — it's the prostate pressing the line flat. The gelatin trick opened it, and nineteen days later his {o} hasn't quit since.":
        "Comprimido não resolve isso — é a próstata achatando a linha. O truque da gelatina abriu, e dezenove dias depois o {o} dele não falhou mais.",
    "The prostate sits on that pipe and shuts your {o} down. His brother handed him the gelatin trick. Nineteen days later he walked in dry, head high.":
        "A próstata senta nesse cano e desliga o seu {o}. O irmão dele entregou o truque da gelatina. Dezenove dias depois ele entrou seco, cabeça erguida.",
})

# --------------------------------------------------------------- VAZAMENTO
TERMOS.update({
    # {n_ext} = idade dela por extenso · {n} = so' a unidade ("Thirty-{n}")
    "thirty": "trinta", "thirty-one": "trinta e um", "thirty-two": "trinta e dois",
    "thirty-three": "trinta e três", "thirty-four": "trinta e quatro",
    "thirty-five": "trinta e cinco",
    "one": "um", "two": "dois", "three": "três", "four": "quatro", "five": "cinco",
    # {N} do organicwave (idade do narrador, digito)
    "a small puddle of clear brine already pooled on the table beneath it":
        "uma poça pequena de salmoura transparente já formada na mesa embaixo",
    "the shell and siphon glisten, wet with brine":
        "a concha e o sifão brilham, molhados de salmoura",
    # {ing} do organicwave
    "a spoonful of gelatin into half a glass of warm water":
        "uma colher de gelatina em meio copo de água morna",
    # {isca}
    "a golden honey jar with a wooden dipper beside it":
        "um pote de mel dourado com uma colher de madeira ao lado",
    "a knob of fresh ginger root and a paring knife":
        "um pedaço de gengibre fresco e uma faca pequena",
    "a small jar of raw honey, lid off": "um potinho de mel puro, sem tampa",
    "a small tin of maca powder, lid beside it":
        "uma latinha de maca em pó, com a tampa ao lado",
    "three cinnamon sticks tied with twine":
        "três paus de canela amarrados com barbante",
})

PT.update({
    # HOOKS
    "Your {o} stopped showing up years ago. That's blood flow choked off. Do this before it's too late.":
        "O seu {o} parou de aparecer anos atrás. Isso é fluxo de sangue sufocado. Faz isso antes que seja tarde demais.",
    "She already knows your {o} won't work tonight. That's blood flow choked off. Fix it before Friday.":
        "Ela já sabe que o seu {o} não vai funcionar hoje à noite. Isso é fluxo de sangue sufocado. Resolve antes de sexta.",
    "She said it's okay, honey, and rolled over. It's blood flow, not you. Fix your {o} tonight.":
        "Ela disse tudo bem, amor, e virou pro outro lado. É fluxo de sangue, não é você. Resolve o seu {o} hoje à noite.",
    "Your wife stopped reaching for you. Nobody told you your {o} lost blood flow. Fix it tonight.":
        "Sua esposa parou de te procurar. Ninguém te contou que o seu {o} perdeu o fluxo de sangue. Resolve hoje à noite.",
    "You apologized in the dark again last night. Blood flow quit reaching your {o}. Do this tonight.":
        "Você pediu desculpa no escuro de novo ontem à noite. O fluxo de sangue parou de chegar no seu {o}. Faz isso hoje à noite.",
    "For four years I told my wife I was just tired. Blood flow quit my {o}. Don't lie to her.":
        "Por quatro anos eu disse pra minha esposa que era só cansaço. O fluxo de sangue abandonou o meu {o}. Não minta pra ela.",
    "I went four years without finishing once, brother. Blood flow quit my {o}. Give me sixty seconds.":
        "Passei quatro anos sem terminar uma vez sequer, irmão. O fluxo de sangue abandonou o meu {o}. Me dá sessenta segundos.",
    "I lost my confidence. I stopped touching my wife. Blood flow quit my {o}. Your turn's coming.":
        "Eu perdi minha confiança. Parei de tocar na minha esposa. O fluxo de sangue abandonou o meu {o}. A sua vez está chegando.",
    "Doctors billed you for twenty years and never once checked the blood flow to your {o}. Do this tonight.":
        "Os médicos te cobraram por vinte anos e nunca checaram o fluxo de sangue até o seu {o}. Faz isso hoje à noite.",
    "Nobody in my house buys those pills anymore. Blood flow quit your {o}, brother. Stop paying them.":
        "Ninguém na minha casa compra mais aqueles comprimidos. O fluxo de sangue abandonou o seu {o}, irmão. Para de pagar eles.",
    "You plan your nights around a pill that never opened the blood flow to your {o}. Do this tonight instead.":
        "Você planeja suas noites em volta de um comprimido que nunca abriu o fluxo de sangue até o seu {o}. Faz isso hoje à noite no lugar.",
    "American men let this happen to their {o} every day. Blood flow. Do this before it's too late.":
        "Homens americanos deixam isso acontecer com o {o} deles todo dia. Fluxo de sangue. Faz isso antes que seja tarde demais.",
    "This is what happens to your {o} when American men ignore blood flow too long. Do this tonight.":
        "É isso que acontece com o seu {o} quando o homem americano ignora o fluxo de sangue por tempo demais. Faz isso hoje à noite.",
    "This is what ignoring blood flow does to your {o}. Fix yours tonight, brother.":
        "É isso que ignorar o fluxo de sangue faz com o seu {o}. Resolve o seu hoje à noite, irmão.",

    # RECEITAS
    "Men, mix a spoonful of gelatin with baking soda in a jar. Stir it. Your {o} is about to wake back up.":
        "Homens, misturem uma colher de gelatina com bicarbonato num pote. Mexe. O seu {o} está prestes a acordar de novo.",
    "Men, mix gelatin into baking soda and stir until it's smooth. Do it tonight and check your {o} in the morning.":
        "Homens, misturem gelatina no bicarbonato e mexam até ficar liso. Faz hoje à noite e confere o seu {o} de manhã.",
    "Men, mix gelatin with baking soda and stir. Costs a dollar. The pill people charged you thirty a month for your {o}.":
        "Homens, misturem gelatina com bicarbonato e mexam. Custa um dólar. O pessoal do comprimido te cobrava trinta por mês pelo seu {o}.",
    "Men, mix gelatin with baking soda in a glass and stir. Do it before Saturday, before she finds out your {o} doesn't work.":
        "Homens, misturem gelatina com bicarbonato num copo e mexam. Faz antes de sábado, antes que ela descubra que o seu {o} não funciona.",
    "Men, one spoon of gelatin, one spoon of baking soda, stir. Takes a minute. Your {o} took twenty years to quit.":
        "Homens, uma colher de gelatina, uma colher de bicarbonato, mexe. Leva um minuto. O seu {o} levou vinte anos pra desistir.",
    "Men, pour the baking soda over the gelatin and stir it one full minute. She's still asking. Your {o} still isn't answering.":
        "Homens, joguem o bicarbonato por cima da gelatina e mexam um minuto inteiro. Ela continua pedindo. O seu {o} continua sem responder.",
    "Men, stir a spoonful of gelatin into baking soda for one minute. Do it before your {o} quits for good.":
        "Homens, mexam uma colher de gelatina no bicarbonato por um minuto. Faz antes que o seu {o} desista de vez.",
    "Men, stir gelatin and baking soda in a coffee mug while she's asleep. She doesn't need to know why your {o} came back.":
        "Homens, mexam gelatina e bicarbonato numa caneca enquanto ela dorme. Ela não precisa saber por que o seu {o} voltou.",
    "Men, stir gelatin into baking soda right on the counter. Your {o} worked fine at thirty. Get it back.":
        "Homens, mexam gelatina no bicarbonato ali na bancada mesmo. O seu {o} funcionava bem aos trinta. Traz ele de volta.",
    "Men, stir gelatin into baking soda, one full minute. That's the first half of getting your {o} back.":
        "Homens, mexam gelatina no bicarbonato, um minuto inteiro. Essa é a primeira metade de trazer o seu {o} de volta.",
    "Every man in my family keeps gelatin and baking soda on the counter. Mix them, stir a minute. Your {o} needs both.":
        "Todo homem da minha família tem gelatina e bicarbonato na bancada. Mistura os dois, mexe um minuto. O seu {o} precisa dos dois.",
    "Us guys don't order anything. Gelatin, baking soda, a spoon. Stir one minute. Nobody has to know your {o} needs it.":
        "Nós não encomendamos nada. Gelatina, bicarbonato, uma colher. Mexe um minuto. Ninguém precisa saber que o seu {o} precisa disso.",
    "We keep gelatin next to the coffee in this house. Stir a spoonful into baking soda. Your {o} gets one minute of your day.":
        "Nesta casa a gente guarda gelatina do lado do café. Mexe uma colher no bicarbonato. O seu {o} ganha um minuto do seu dia.",

    # VIRADAS
    "But here's the thing most guys never realize. Without the gelatin trick, baking soda on its own does nothing for your {o}. It's not age. Your blood flow got choked off.":
        "Mas tem uma coisa que a maioria dos caras nunca percebe. Sem o truque da gelatina, o bicarbonato sozinho não faz nada pelo seu {o}. Não é idade. O seu fluxo de sangue foi sufocado.",
    "But here's what most guys never find out. Without the gelatin trick, baking soda alone does nothing for your {o}. It's not age, brother — your blood flow got choked off.":
        "Mas tem uma coisa que a maioria dos caras nunca descobre. Sem o truque da gelatina, o bicarbonato sozinho não faz nada pelo seu {o}. Não é idade, irmão — o seu fluxo de sangue foi sufocado.",
    "Every man I gave this to called me back angry. Without the gelatin trick, baking soda does nothing for your {o}. It's not age — your blood flow got sealed off years back.":
        "Todo homem pra quem eu dei isso me ligou de volta bravo. Sem o truque da gelatina, o bicarbonato não faz nada pelo seu {o}. Não é idade — o seu fluxo de sangue foi lacrado anos atrás.",
    "I did this wrong first. I quit for a month. I told my wife it was over. Without the gelatin trick, baking soda does nothing for your {o} — your blood flow stays shut.":
        "Eu fiz errado primeiro. Desisti por um mês. Disse pra minha esposa que tinha acabado. Sem o truque da gelatina, o bicarbonato não faz nada pelo seu {o} — o seu fluxo de sangue continua fechado.",
    "I gave you half on purpose. Without the gelatin trick, that recipe does nothing for your {o}. It's not age, brother — your blood flow got pinched off decades ago.":
        "Eu te dei metade de propósito. Sem o truque da gelatina, essa receita não faz nada pelo seu {o}. Não é idade, irmão — o seu fluxo de sangue foi beliscado décadas atrás.",
    "I mixed that same spoon for a year and nothing moved. Without the gelatin trick, baking soda does nothing for your {o}. It's not age, brother — your blood flow got clamped shut.":
        "Eu mexi essa mesma colher por um ano e nada se mexeu. Sem o truque da gelatina, o bicarbonato não faz nada pelo seu {o}. Não é idade, irmão — o seu fluxo de sangue foi prensado até fechar.",
    "Now don't go telling the guys yet. Without the gelatin trick, baking soda by itself does nothing for your {o}. It's not age, brother. Your blood flow got shut down.":
        "Agora não sai contando pros caras ainda. Sem o truque da gelatina, o bicarbonato sozinho não faz nada pelo seu {o}. Não é idade, irmão. O seu fluxo de sangue foi desligado.",
    "She's waited two years already. Without the gelatin trick, baking soda does nothing for your {o}, and she waits two more. It's not age — your blood flow got choked off.":
        "Ela já esperou dois anos. Sem o truque da gelatina, o bicarbonato não faz nada pelo seu {o}, e ela espera mais dois. Não é idade — o seu fluxo de sangue foi sufocado.",
    "Stop right there. Without the gelatin trick, that baking soda is half a recipe and your {o} stays down. It's not age. Your blood flow got squeezed shut.":
        "Para aí. Sem o truque da gelatina, esse bicarbonato é meia receita e o seu {o} continua caído. Não é idade. O seu fluxo de sangue foi espremido até fechar.",
    "You didn't fail, brother. Nobody gave you the other half. Without the gelatin trick, baking soda does nothing for your {o}. It's not age — your blood flow got choked off.":
        "Você não fracassou, irmão. Ninguém te deu a outra metade. Sem o truque da gelatina, o bicarbonato não faz nada pelo seu {o}. Não é idade — o seu fluxo de sangue foi sufocado.",
    "You're one ingredient short, brother. Without the gelatin trick, baking soda does nothing for your {o}. It's not age. Your blood flow got choked off while you waited.":
        "Está faltando um ingrediente, irmão. Sem o truque da gelatina, o bicarbonato não faz nada pelo seu {o}. Não é idade. O seu fluxo de sangue foi sufocado enquanto você esperava.",

    # PROVAS
    "She's {n_ext} and she can't keep her hands off my {o}. Half my age, and she's the one who won't wait. {barreira}":
        "Ela tem {n_ext} e não tira as mãos do meu {o}. Metade da minha idade, e é ela quem não quer esperar. {barreira}",
    "She's {n_ext}. Half my age, and she asked me for a break. My {o} doesn't tap out first anymore. {barreira}":
        "Ela tem {n_ext}. Metade da minha idade, e ela me pediu uma pausa. O meu {o} não desiste primeiro mais. {barreira}",
    "She's {n_ext} and she drives an hour over on a Tuesday night. Half my age, and my {o} is why. {barreira}":
        "Ela tem {n_ext} e dirige uma hora numa terça à noite. Metade da minha idade, e o meu {o} é o motivo. {barreira}",
    "She's {n_ext}, half my age, and she needed a minute to catch her breath. My {o} did that. {barreira}":
        "Ela tem {n_ext}, metade da minha idade, e precisou de um minuto pra recuperar o fôlego. O meu {o} fez isso. {barreira}",
    "She's half my age and she can't keep her hands off my {o}. Thirty-{n} years old and she calls me every night. {barreira}":
        "Ela tem metade da minha idade e não tira as mãos do meu {o}. Trinta e {n} anos e me liga toda noite. {barreira}",
    "Thirty-{n} years old and she reaches for me first now. Half my age, and my {o} is why she stays. {barreira}":
        "Trinta e {n} anos e agora é ela quem me procura primeiro. Metade da minha idade, e o meu {o} é o motivo dela ficar. {barreira}",
    "Thirty-{n} years old and she told her girlfriends about my {o}. Half my age, and I'm what she brags about. {barreira}":
        "Trinta e {n} anos e ela contou pras amigas sobre o meu {o}. Metade da minha idade, e eu sou do que ela se gaba. {barreira}",
    "Us guys pass this around now. My {o} works and she's {n_ext}. She couldn't sit still the next day. Thirty-{n} years old. {barreira}":
        "Nós passamos isso entre a gente agora. O meu {o} funciona e ela tem {n_ext}. Ela não conseguiu ficar parada no dia seguinte. Trinta e {n} anos. {barreira}",

    # PACING
    "Next Friday night she'll ask what changed. You'll remember this.":
        "Sexta que vem, à noite, ela vai perguntar o que mudou. Você vai lembrar disso.",
    "Next Friday night, when she asks what changed, you'll remember this video.":
        "Sexta que vem, à noite, quando ela perguntar o que mudou, você vai lembrar deste vídeo.",

    # CTAS
    "{pacing} Comment gelatin, and I'll send you the only one I trust today. {gate}":
        "{pacing} Comenta GELATIN que hoje eu te mando o único em que eu confio. {gate}",
    "{pacing} Comment gelatin, and I'll send you the exact one I use, tonight. {gate}":
        "{pacing} Comenta GELATIN que hoje à noite eu te mando exatamente o que eu uso. {gate}",
    "{pacing} Comment gelatin, and I'll send you the full video today. {gate}":
        "{pacing} Comenta GELATIN que hoje eu te mando o vídeo completo. {gate}",
    "{pacing} Comment gelatin, and I'll send you what to buy and where. {gate}":
        "{pacing} Comenta GELATIN que eu te mando o que comprar e onde. {gate}",
    "{pacing} Comment gelatin, and I'll send the whole thing over before this comes down. {gate}":
        "{pacing} Comenta GELATIN que eu mando tudo antes que isso saia do ar. {gate}",
    "{pacing} Comment gelatin, and I'll send you the gelatin trick tonight. {gate}":
        "{pacing} Comenta GELATIN que hoje à noite eu te mando o truque da gelatina. {gate}",
    "{pacing} Comment gelatin, and I'll send you the other half of that recipe. {gate}":
        "{pacing} Comenta GELATIN que eu te mando a outra metade dessa receita. {gate}",
    "{pacing} Comment gelatin, and I'll send you the recipe today. {gate}":
        "{pacing} Comenta GELATIN que hoje eu te mando a receita. {gate}",
    "{pacing} Comment gelatin, and I'll send you the same one I sent my brother. {gate}":
        "{pacing} Comenta GELATIN que eu te mando o mesmo que eu mandei pro meu irmão. {gate}",
    "{pacing} Comment gelatin, and I'll send you the one we use at my house. I can't name it here. {gate}":
        "{pacing} Comenta GELATIN que eu te mando o que a gente usa lá em casa. Eu não posso citar aqui. {gate}",
    "{pacing} Comment gelatin, and I'll send you where I get mine. {gate}":
        "{pacing} Comenta GELATIN que eu te mando onde eu compro o meu. {gate}",
    "{pacing} Comment gelatin, and I'll send you what my own wife went looking for. She found it before I did. {gate}":
        "{pacing} Comenta GELATIN que eu te mando o que a minha própria esposa foi procurar. Ela achou antes de mim. {gate}",
    "{pacing} I waited four years to find this, brother. Comment gelatin, and you won't wait four days. {gate}":
        "{pacing} Eu esperei quatro anos pra achar isso, irmão. Comenta GELATIN, e você não vai esperar quatro dias. {gate}",

    # GATES
    "Follow me first, or Facebook can't deliver it, brother.":
        "Me segue primeiro, senão o Facebook não consegue entregar, irmão.",
    "Hit follow right now, or my message never lands.":
        "Aperta seguir agora, senão minha mensagem não chega.",
    "Make sure you're following me first, or I won't have any way to find your comment, brother.":
        "Garante que está me seguindo primeiro, senão eu não vou ter como achar o seu comentário, irmão.",

    # VAZAMENTO SHORT — as fundidas
    "Baking soda is half a recipe: without the gelatin trick your {o} stays down, because the blood flow is choked off. She's {n_ext} and she reaches for me first now.":
        "Bicarbonato é meia receita: sem o truque da gelatina o seu {o} continua caído, porque o fluxo de sangue está sufocado. Ela tem {n_ext} e agora é ela quem me procura primeiro.",
    "Nobody gave you the other half, brother. Without the gelatin trick the baking soda leaves your {o} down and the blood flow shut. She's {n_ext} and she needed a minute.":
        "Ninguém te deu a outra metade, irmão. Sem o truque da gelatina o bicarbonato deixa o seu {o} caído e o fluxo de sangue fechado. Ela tem {n_ext} e precisou de um minuto.",
    "Without the gelatin trick that baking soda does nothing for your {o} — your blood flow got squeezed shut, not your age. Thirty-{n} years old, and she won't wait.":
        "Sem o truque da gelatina esse bicarbonato não faz nada pelo seu {o} — o seu fluxo de sangue foi espremido até fechar, não é a sua idade. Trinta e {n} anos, e ela não quer esperar.",
    "Without the gelatin trick, baking soda alone does nothing for your {o} — that's blood flow, choked off. She's {n_ext}, half my age, and she can't keep her hands off mine.":
        "Sem o truque da gelatina, o bicarbonato sozinho não faz nada pelo seu {o} — isso é fluxo de sangue sufocado. Ela tem {n_ext}, metade da minha idade, e não tira as mãos do meu.",
    "Without the gelatin trick, baking soda is half a recipe and the blood flow never reaches your {o}. She's {n_ext}, half my age, and she calls me every night.":
        "Sem o truque da gelatina, o bicarbonato é meia receita e o fluxo de sangue nunca chega no seu {o}. Ela tem {n_ext}, metade da minha idade, e me liga toda noite.",
})

# --------------------------------------------------------------- ORGANIC WAVE SHORT
PT.update({
    # HOOKS — persona masculina
    "{N} years old, and this is what my {o} looked like every night. My wife stopped reaching for me.":
        "{N} anos, e era assim que o meu {o} ficava toda noite. Minha esposa parou de me procurar.",
    "This is my {o} before. I used to fall asleep on the couch on purpose so she wouldn't try.":
        "Este é o meu {o} antes. Eu dormia no sofá de propósito pra ela não tentar.",
    "Look at this one. That was my {o} at {n} — and I made excuses every single night.":
        "Olha esse aqui. Era o meu {o} aos {n} — e eu dava desculpa toda santa noite.",
    "I couldn't look my wife in the eye at {n}. My {o} hung like this and I knew why she stopped.":
        "Eu não conseguia olhar minha esposa nos olhos aos {n}. O meu {o} pendia assim e eu sabia por que ela parou.",
    "We slept like roommates for eight months. This was my {o}, and I thought that was just {n}.":
        "A gente dormia como colegas de quarto por oito meses. Este era o meu {o}, e eu achava que era só ter {n}.",
    "Four hundred dollars a month on pills, and my {o} still looked like this. She stopped asking, brother.":
        "Quatrocentos dólares por mês em comprimido, e o meu {o} continuava assim. Ela parou de pedir, irmão.",
    "My wife blamed herself. She thought it was her. It was my {o}, and it looked exactly like this.":
        "Minha esposa se culpava. Ela achava que era ela. Era o meu {o}, e ele estava exatamente assim.",
    "Too embarrassed to tell my own doctor. So I sat with this — my {o}, every night, for two years.":
        "Com vergonha demais de contar pro meu próprio médico. Então convivi com isso — o meu {o}, toda noite, por dois anos.",

    # HOOKS_F — persona feminina
    "My man is {n} and this is what his {o} looked like. He stopped coming to bed and I let him.":
        "Meu homem tem {n} e era assim que o {o} dele ficava. Ele parou de vir pra cama e eu deixei.",
    "My man is {n}. This was his {o} in March. I'm the one who found what fixed it.":
        "Meu homem tem {n}. Este era o {o} dele em março. Fui eu quem achou o que resolveu.",
    "Look at this one. That was my husband's {o} for two years, and I started thinking it was me.":
        "Olha esse aqui. Foi o {o} do meu marido por dois anos, e eu comecei a achar que era eu.",
    "We hadn't touched in eight months. This was his {o}, and he wouldn't talk about it.":
        "A gente não se tocava havia oito meses. Este era o {o} dele, e ele não falava sobre isso.",
    "I was about to leave. The bedroom was dead, and his {o} looked exactly like this.":
        "Eu estava quase indo embora. O quarto estava morto, e o {o} dele estava exatamente assim.",
    "He blamed his age. I blamed myself. It was neither of us — his {o} looked like this every night.":
        "Ele culpava a idade. Eu me culpava. Não era nenhum de nós dois — o {o} dele ficava assim toda noite.",
    "I stopped undressing in front of him. Not because of me — because of this. Because of his {o}.":
        "Eu parei de me despir na frente dele. Não por minha causa — por causa disso. Por causa do {o} dele.",
    "Four hundred a month on pills, and his {o} still looked like this. I stopped asking.":
        "Quatrocentos por mês em comprimido, e o {o} dele continuava assim. Eu parei de pedir.",

    # FUNDIDAS — masculina
    "It was never age — it's blood flow, choked off. Stir {ing}. That's the gelatin trick, and nineteen days later my {o} came back.":
        "Nunca foi idade — é fluxo de sangue, sufocado. Mexe {ing}. Esse é o truque da gelatina, e dezenove dias depois o meu {o} voltou.",
    "My neighbor gave me this. Stir {ing} — the gelatin trick. The blood flow came back, and so did my {o}.":
        "Meu vizinho me passou isso. Mexe {ing} — o truque da gelatina. O fluxo de sangue voltou, e o meu {o} também.",
    "Nobody told me it was blood flow. Stir {ing}, that's the whole gelatin trick, and my {o} hasn't quit since.":
        "Ninguém me disse que era fluxo de sangue. Mexe {ing}, esse é o truque da gelatina inteiro, e o meu {o} não falhou mais desde então.",
    "Stir {ing}. They call it the gelatin trick, and it opens the blood flow your {o} lost. This is me now.":
        "Mexe {ing}. Chamam isso de truque da gelatina, e ele abre o fluxo de sangue que o seu {o} perdeu. Este sou eu agora.",
    "Two dollars, brother. Stir {ing} — the gelatin trick — and the blood flow that left my {o} came right back.":
        "Dois dólares, irmão. Mexe {ing} — o truque da gelatina — e o fluxo de sangue que abandonou o meu {o} voltou na hora.",

    # FUNDIDAS_F — feminina
    "I stir {ing} for him. They call it the gelatin trick, and it opens the blood flow his {o} lost. Look at us now.":
        "Eu mexo {ing} pra ele. Chamam isso de truque da gelatina, e ele abre o fluxo de sangue que o {o} dele perdeu. Olha a gente agora.",
    "It was never his age — it's blood flow, choked off. I stir {ing}. That's the gelatin trick, and nineteen days later his {o} came back.":
        "Nunca foi a idade dele — é fluxo de sangue, sufocado. Eu mexo {ing}. Esse é o truque da gelatina, e dezenove dias depois o {o} dele voltou.",
    "My aunt gave me this. I stir {ing} — the gelatin trick. The blood flow came back, and so did his {o}.":
        "Minha tia me passou isso. Eu mexo {ing} — o truque da gelatina. O fluxo de sangue voltou, e o {o} dele também.",
    "Nobody told us it was blood flow. I stir {ing}, that's the whole gelatin trick, and his {o} hasn't quit since.":
        "Ninguém contou pra gente que era fluxo de sangue. Eu mexo {ing}, esse é o truque da gelatina inteiro, e o {o} dele não falhou mais desde então.",
    "Two dollars, girls. I stir {ing} — the gelatin trick — and the blood flow that left his {o} came right back.":
        "Dois dólares, meninas. Eu mexo {ing} — o truque da gelatina — e o fluxo de sangue que abandonou o {o} dele voltou na hora.",

    # CTAS — masculina
    "Next Friday night she'll ask what changed. Comment gelatin, and I'll send you the exact one I use. {gate}":
        "Sexta que vem, à noite, ela vai perguntar o que mudou. Comenta GELATIN que eu te mando exatamente o que eu uso. {gate}",
    "A month from tonight you won't recognise yourself. Comment gelatin, and I'll send you where I get mine. {gate}":
        "Daqui a um mês você não vai se reconhecer. Comenta GELATIN que eu te mando onde eu compro o meu. {gate}",
    "Comment gelatin, and I'll send it tonight. There's one more ingredient on that counter I can't name here. {gate}":
        "Comenta GELATIN que eu mando hoje à noite. Tem mais um ingrediente naquela bancada que eu não posso citar aqui. {gate}",
    "Comment gelatin, and I'll send you the one my neighbor sent me. Nobody in my house ever knew. {gate}":
        "Comenta GELATIN que eu te mando o que o meu vizinho me mandou. Ninguém lá em casa soube. {gate}",
    "Comment gelatin, and I'll send you the recipe tonight. {gate}":
        "Comenta GELATIN que hoje à noite eu te mando a receita. {gate}",
    "I waited two years to find this. Comment gelatin, and you won't wait two days. {gate}":
        "Eu esperei dois anos pra achar isso. Comenta GELATIN, e você não vai esperar dois dias. {gate}",

    # CTAS_F — feminina
    "Next Friday night he'll be the one reaching for you. Comment gelatin, and I'll send you the exact one I use. {gate}":
        "Sexta que vem, à noite, é ele quem vai te procurar. Comenta GELATIN que eu te mando exatamente o que eu uso. {gate}",
    "A month from now you won't recognise him. Comment gelatin, and I'll send you where I get mine. {gate}":
        "Daqui a um mês você não vai reconhecer ele. Comenta GELATIN que eu te mando onde eu compro o meu. {gate}",
    "Comment gelatin, and I'll send it tonight. There's one more thing on that counter I can't name here. {gate}":
        "Comenta GELATIN que eu mando hoje à noite. Tem mais uma coisa naquela bancada que eu não posso citar aqui. {gate}",
    "Comment gelatin, and I'll send you the one my aunt sent me. He never even knew I did it. {gate}":
        "Comenta GELATIN que eu te mando o que a minha tia me mandou. Ele nem soube que eu fiz. {gate}",
    "Comment gelatin, and I'll send you the recipe I use on him. {gate}":
        "Comenta GELATIN que eu te mando a receita que eu uso nele. {gate}",
})

COBERTURA = {"necrose": 36, "flagrante": 78, "pee": 81,
             "vazamento": 76, "organicwave": 49}


# ======================================================================
# de dados_troca.py
# ======================================================================
# -*- coding: utf-8 -*-
"""
dados_troca.py — o agente TROCA (novo em 2026-08-01). LOCAL DO LUCAS.

Fundido em dados_pt por traducao.py. Módulo separado de propósito: agente novo
não deve inchar o arquivo base, e assim dá pra medir a cobertura por agente.
"""

TERMOS.update({
    "the woman who cooks for him": "a mulher que cozinha pra ele",
    "the woman from the house next door": "a mulher da casa do lado",
    "the woman who does his shopping": "a mulher que faz as compras dele",
    "her hand on his": "a mão dela sobre a dele",
    "slides her hand up and down": "desliza a mão pra cima e pra baixo",
    "pressed against her face": "encostado no rosto dela",
    "sliding up and down": "deslizando pra cima e pra baixo",
})

PT.update({
    # DESMENTIDOS — o descrédito que abre a virada
    "You don't believe that works, right?": "Você não acredita que isso funciona, né?",
    "Yeah. Nobody actually believes that one.": "Pois é. Ninguém acredita nessa mesmo.",
    "Course it doesn't work. Never did.": "Claro que não funciona. Nunca funcionou.",
    "You know that's nonsense, right?": "Você sabe que isso é bobagem, né?",
    "Look at your face. Exactly that.": "Olha a sua cara. Exatamente isso.",
    "It doesn't. Not one bit.": "Não funciona. Nem um pouco.",
    "You're not buying that. Good.": "Você não está comprando essa. Ótimo.",
    "Nope. Never worked for anybody, ever.": "Não. Nunca funcionou pra ninguém, nunca.",
    "And you already know better.": "E você já sabe que não é bem assim.",
    "Sounds insane, because it is.": "Parece loucura, porque é.",
    "Right? Total garbage, every word.": "Né? Lixo total, cada palavra.",
    "Doesn't work. You know it.": "Não funciona. Você sabe disso.",

    # TESTEMUNHOS — a voz dela, depois
    "Now his {o} won't let me sleep.": "Agora o {o} dele não me deixa dormir.",
    "Nineteen days later his {o} doesn't quit.": "Dezenove dias depois o {o} dele não para.",
    "I'm the one asking his {o} for mercy now.": "Agora sou eu quem pede misericórdia pro {o} dele.",
    "His {o} hasn't given me a quiet night since.": "O {o} dele não me deu uma noite tranquila desde então.",
    "He was done by ten. Now his {o} isn't.": "Ele acabava às dez. Agora o {o} dele não acaba.",
    "His {o} wakes up before he does.": "O {o} dele acorda antes dele.",
    "I stopped asking. His {o} started answering.": "Eu parei de pedir. O {o} dele começou a responder.",
    "Now I'm the one who needs a night off from his {o}.": "Agora sou eu quem precisa de uma noite de folga do {o} dele.",
    "His {o} doesn't take no for an answer anymore.": "O {o} dele não aceita mais um não.",
    "I hid the box. His {o} gave it away.": "Eu escondi a caixa. O {o} dele entregou.",
    "Three weeks in, his {o} still outlasts me.": "Três semanas depois, o {o} dele ainda dura mais que eu.",
    "My sister asked what changed. His {o} did.": "Minha irmã perguntou o que mudou. Foi o {o} dele.",
    "He reaches first now, and his {o} doesn't wait.": "Agora é ele quem procura primeiro, e o {o} dele não espera.",
    "His {o} quit apologizing. So did he.": "O {o} dele parou de pedir desculpa. Ele também.",

    # PROVAS
    "Nineteen days, start to finish.": "Dezenove dias, do começo ao fim.",
    "Nineteen days on a man I know.": "Dezenove dias num homem que eu conheço.",
    "He'll tell you if you ask him.": "Ele te conta, se você perguntar.",
    "Two dollars a box, that's all.": "Dois dólares a caixa, só isso.",
    "He'll tell you the same thing.": "Ele vai te dizer a mesma coisa.",
    "Three weeks, every single night.": "Três semanas, toda santa noite.",
    "I watched the whole thing happen.": "Eu vi a coisa toda acontecer.",
    "No photo, no filter, no story.": "Sem foto, sem filtro, sem história.",
    "No pills, nothing else, just that.": "Sem comprimido, sem mais nada, só isso.",
    "Same man, nineteen days later.": "O mesmo homem, dezenove dias depois.",
    "He didn't believe it either. You won't.": "Ele também não acreditou. Você não vai.",
    "Not a story. You can check it.": "Não é história. Você pode conferir.",

    # BARREIRAS
    "Two dollars at any store.": "Dois dólares em qualquer loja.",
    "Nobody in your house knows.": "Ninguém lá na sua casa fica sabendo.",
    "No prescription, no doctor, no waiting.": "Sem receita, sem médico, sem espera.",
    "It's in the baking aisle.": "Está no corredor de confeitaria.",
    "Takes thirty seconds a night.": "Leva trinta segundos por noite.",
    "You already have the glass.": "Você já tem o copo.",
    "No pills, no appointment, no questions.": "Sem comprimido, sem consulta, sem perguntas.",
    "Cheaper than a single refill.": "Mais barato que uma única recarga.",
    "He never knew I did it.": "Ele nunca soube que eu fiz.",
    "Grocery store, bottom shelf, about four dollars.": "Mercado, prateleira de baixo, uns quatro dólares.",
    "Nothing to swallow but water.": "Nada pra engolir além de água.",
    "No one has to know.": "Ninguém precisa saber.",

    # CTAS
    "Comment gelatin, and I'll send you the whole recipe tonight.":
        "Comenta GELATIN que hoje à noite eu te mando a receita inteira.",
    "Comment gelatin, and the recipe's in your inbox in ten minutes.":
        "Comenta GELATIN que em dez minutos a receita está na sua caixa de entrada.",
    "Comment gelatin, and I'll send you exactly what to buy.":
        "Comenta GELATIN que eu te mando exatamente o que comprar.",
    "The recipe's yours — comment gelatin, and it goes out tonight.":
        "A receita é sua — comenta GELATIN, e ela sai hoje à noite.",
    "Comment gelatin, and I'll tell you how much and when.":
        "Comenta GELATIN que eu te digo quanto e quando.",
    "Comment gelatin, and I'll send you the full recipe.":
        "Comenta GELATIN que eu te mando a receita completa.",
    "One word in the comments: gelatin, and it's yours tonight.":
        "Uma palavra nos comentários: GELATIN, e hoje à noite ela é sua.",
    "Comment gelatin, and the recipe's on your phone tonight.":
        "Comenta GELATIN que hoje à noite a receita está no seu celular.",
    "Type gelatin, in the comments and I'll send the measurements.":
        "Digita GELATIN nos comentários que eu mando as medidas.",
    "Comment gelatin, and I'll send the whole thing, free.":
        "Comenta GELATIN que eu mando tudo, de graça.",
    "Say the word — gelatin, in the comments — and it's sent.":
        "Diz a palavra — GELATIN, nos comentários — e está enviada.",
    "Comment gelatin, and I'll send the recipe my aunt sent me.":
        "Comenta GELATIN que eu mando a receita que a minha tia me mandou.",
    "Comment gelatin, and I'll send you all four ingredients.":
        "Comenta GELATIN que eu te mando os quatro ingredientes.",
    "Want it? Comment gelatin, and I'll message you tonight.":
        "Quer? Comenta GELATIN que hoje à noite eu te mando mensagem.",
    "Comment gelatin, and I'll send it before you scroll away.":
        "Comenta GELATIN que eu mando antes de você rolar a tela.",
    "It's four lines long. Comment gelatin, and I'll send it.":
        "São quatro linhas. Comenta GELATIN que eu mando.",
    "Comment gelatin, and I'll send you where to get it.":
        "Comenta GELATIN que eu te mando onde conseguir.",
    "Just the word gelatin, in the comments. That's the whole ask.":
        "Só a palavra GELATIN, nos comentários. É só isso que eu peço.",

    # GATES
    "Follow first, or my message never lands.":
        "Segue primeiro, senão minha mensagem não chega.",
    "Hit follow, or the app blocks me.":
        "Aperta seguir, senão o app me bloqueia.",
    "I can only message people who follow.":
        "Eu só consigo mandar mensagem pra quem segue.",
    "Followers get answered first. Everyone else waits.":
        "Quem segue é respondido primeiro. O resto espera.",
    "One tap on follow. That's the whole gate.":
        "Um toque em seguir. É só essa a exigência.",
    "Follow me, brother, or this never arrives.":
        "Me segue, irmão, senão isso nunca chega.",
    "Without the follow my inbox stays shut.":
        "Sem o seguir, minha caixa de entrada fica fechada.",
    "Three hundred comments tonight. Followers go first.":
        "Trezentos comentários hoje à noite. Quem segue passa na frente.",
    "Follow tonight — tomorrow this leaves your feed.":
        "Segue hoje à noite — amanhã isso some do seu feed.",
    "Follow me, my friend. Then I can answer.":
        "Me segue, meu amigo. Aí eu consigo responder.",
    "The algorithm hides me from non-followers.":
        "O algoritmo me esconde de quem não segue.",
    "Follow first. That's how my inbox opens.":
        "Segue primeiro. É assim que minha caixa de entrada abre.",
    "I answer followers. Everyone else has to wait.":
        "Eu respondo quem segue. O resto tem que esperar.",
    "Tap follow, or the app eats the message.":
        "Toca em seguir, senão o app come a mensagem.",
})


# ======================================================================
# de dados_troca2.py
# ======================================================================
# -*- coding: utf-8 -*-
"""
dados_troca2.py — CRENDICES e FUNDIDAS do TROCA. LOCAL DO LUCAS.

Separado do dados_troca porque estes dois pools moram em **dicts com chave
`txt`**, e não em listas de string — foi por isso que a primeira extração não
os viu. O slot {s} é a substância da crendice (azeite, Vick, pasta de dente...).
"""

TERMOS.update({
    # {s} — a substância da crendice (SUBSTANCIAS no motor)
    "aloe": "babosa",
    "bacon grease": "gordura de bacon",
    "baking soda": "bicarbonato",
    "cider vinegar": "vinagre de maçã",
    "coconut oil": "óleo de coco",
    "egg white": "clara de ovo",
    "ginger": "gengibre",
    "honey": "mel",
    "menthol rub": "pomada de mentol",
    "mustard": "mostarda",
    "olive oil": "azeite",
    "peanut butter": "pasta de amendoim",
    "turmeric": "açafrão",
    "yogurt": "iogurte",
})

PT.update({
    # CRENDICES — a crença popular que a cena 1 apresenta para depois derrubar
    "Rub {s} on your {o} and it's gonna get ten times bigger.":
        "Passa {s} no seu {o} e ele vai ficar dez vezes maior.",
    "If you want your {o} ten times bigger, rub {s} on it tonight.":
        "Se você quer o seu {o} dez vezes maior, passa {s} nele hoje à noite.",
    "They all say {s} on your {o} makes it twice the size.":
        "Todo mundo diz que {s} no seu {o} deixa ele com o dobro do tamanho.",
    "Every man on this app swears {s} on your {o} is worth three inches.":
        "Todo homem neste app jura que {s} no seu {o} vale três polegadas.",
    "Put {s} on your {o} tonight and it doubles. The internet swears by it.":
        "Põe {s} no seu {o} hoje à noite e ele dobra. A internet jura que é verdade.",
    "One spoon of {s} on your {o} and you grow a full inch.":
        "Uma colher de {s} no seu {o} e você cresce uma polegada inteira.",
    "My cousin swears {s} on your {o} takes you from four to eight.":
        "Meu primo jura que {s} no seu {o} te leva de quatro pra oito.",
    "Rub {s} into your {o} every night and it never quits on you.":
        "Esfrega {s} no seu {o} toda noite e ele nunca mais te abandona.",
    "The whole internet says {s} on your {o} makes it ten times bigger.":
        "A internet inteira diz que {s} no seu {o} deixa ele dez vezes maior.",
    "Coat your {o} in {s} and it comes out a different animal.":
        "Cobre o seu {o} de {s} e ele vira outro animal.",
    "Two fingers of {s}, straight onto your {o}, and it grows ten times.":
        "Dois dedos de {s}, direto no seu {o}, e ele cresce dez vezes.",
    "Guys everywhere swear {s} on your {o} adds a couple of inches.":
        "Os caras em todo lugar juram que {s} no seu {o} acrescenta umas polegadas.",
    "Want your {o} ten times bigger? Then rub {s} straight on it tonight.":
        "Quer o seu {o} dez vezes maior? Então passa {s} direto nele hoje à noite.",
    "A spoonful of {s} on your {o} beats every pill on the shelf.":
        "Uma colher de {s} no seu {o} ganha de todo comprimido da prateleira.",
    "A little {s} on your {o}. That's the whole thing. Ten times bigger.":
        "Um pouco de {s} no seu {o}. É só isso. Dez vezes maior.",
    "Everybody says the same thing: {s} on your {o}, double the size.":
        "Todo mundo diz a mesma coisa: {s} no seu {o}, o dobro do tamanho.",
    "Rub {s} on your {o} — ten times bigger, that's the claim they make.":
        "Passa {s} no seu {o} — dez vezes maior, é o que eles afirmam.",
    "Half this country swears {s} on your {o} is worth two whole inches.":
        "Metade deste país jura que {s} no seu {o} vale duas polegadas inteiras.",

    # FUNDIDAS — a troca: larga a crendice, pega a gelatina
    "Forget that. This is what actually works — gelatin. That's the gelatin trick, and if you want the blood back in your {o}, that's the one.":
        "Esquece isso. Isto aqui é o que funciona de verdade — gelatina. Esse é o truque da gelatina, e se você quer o sangue de volta no seu {o}, é esse.",
    "Drop that. Pick this up. Gelatin in cold water, every single night — they call it the gelatin trick, and your {o} remembers.":
        "Larga isso. Pega isto. Gelatina na água gelada, toda santa noite — chamam de truque da gelatina, e o seu {o} lembra.",
    "That never worked on anybody. This did. A spoon of gelatin, stirred cold — the gelatin trick — and the blood flow came back to his {o}.":
        "Aquilo nunca funcionou em ninguém. Isto funcionou. Uma colher de gelatina, mexida gelada — o truque da gelatina — e o fluxo de sangue voltou pro {o} dele.",
    "It was never {s}. It's blood flow, choked off, and gelatin opens it. That's the gelatin trick, and my husband's {o} came back.":
        "Nunca foi {s}. É fluxo de sangue, sufocado, e a gelatina abre. Esse é o truque da gelatina, e o {o} do meu marido voltou.",
    "Set that down. This one's real: gelatin, stirred into cold water. The gelatin trick. Nineteen days and his {o} was back for good.":
        "Larga isso aí. Este é de verdade: gelatina, mexida na água gelada. O truque da gelatina. Dezenove dias e o {o} dele voltou pra ficar.",
    "Nobody's {o} ever got bigger from {s}. They got bigger from gelatin. That's the gelatin trick, and it costs two dollars a box.":
        "O {o} de ninguém nunca ficou maior por causa de {s}. Ficaram maiores por causa da gelatina. Esse é o truque da gelatina, e custa dois dólares a caixa.",
    "Put that down. Gelatin. Cold water, one spoon, before bed — the gelatin trick — and if blood flow is what your {o} lost, that's the one.":
        "Larga isso. Gelatina. Água gelada, uma colher, antes de dormir — o truque da gelatina — e se foi fluxo de sangue que o seu {o} perdeu, é esse.",
    "My aunt handed me this instead. Gelatin, stirred cold. The gelatin trick. Three weeks later his {o} had not quit once.":
        "Minha tia me entregou isto no lugar. Gelatina, mexida gelada. O truque da gelatina. Três semanas depois o {o} dele não tinha falhado uma vez.",
    "Wrong jar. This one. Gelatin in warm water, stirred until it's gone. They call it the gelatin trick, and his {o} answers now.":
        "Pote errado. Este aqui. Gelatina na água morna, mexida até sumir. Chamam de truque da gelatina, e o {o} dele responde agora.",
    "That jar goes down. This one comes up. Gelatin — the gelatin trick — and the blood flow his {o} lost is running again.":
        "Esse pote desce. Este sobe. Gelatina — o truque da gelatina — e o fluxo de sangue que o {o} dele perdeu está correndo de novo.",
    "Doctors never say blood flow. Gelatin does the job {s} never could. That's the gelatin trick, and his {o} proved it in weeks.":
        "Os médicos nunca falam fluxo de sangue. A gelatina faz o serviço que {s} nunca fez. Esse é o truque da gelatina, e o {o} dele provou em semanas.",
    "Trade it. One spoon of gelatin, cold water, nightly. The gelatin trick, and his {o} stopped quitting on us months ago.":
        "Troca. Uma colher de gelatina, água gelada, toda noite. O truque da gelatina, e o {o} dele parou de falhar com a gente meses atrás.",
    "Off the counter, into the trash. Gelatin is the one — the gelatin trick — and if blood flow is what your {o} is missing, start there.":
        "Sai da bancada, vai pro lixo. A gelatina é a certa — o truque da gelatina — e se é fluxo de sangue que está faltando no seu {o}, começa por aí.",
    "Same hand, different jar. Gelatin, stirred into cold water before bed. The gelatin trick. His {o} has not quit since March.":
        "Mesma mão, outro pote. Gelatina, mexida na água gelada antes de dormir. O truque da gelatina. O {o} dele não falha desde março.",
    "This goes down, this comes up. Gelatin. Cold water, one spoon — the gelatin trick — and if your {o} needs the blood flow, that's it.":
        "Este desce, este sobe. Gelatina. Água gelada, uma colher — o truque da gelatina — e se o seu {o} precisa do fluxo de sangue, é esse.",
})
