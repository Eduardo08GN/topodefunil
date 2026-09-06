# -*- coding: utf-8 -*-
"""CONTEUDO — L'ANCRE DU SOUFFLE (frances). DADOS, nao apresentacao.

Versao francesa do `Der Atemanker`. Mesmo motor, mesmo builder, mesmas fotos —
o que muda e' este arquivo. Ver `conteudo_atem.py` para as tres travas, que
valem aqui inteiras e sem excecao:
  1. SEM HIPERVENTILACAO (o mecanismo e' expiracao mais longa);
  2. AGUA NUNCA (`GE4` — desmaio de aguas rasas);
  3. SEM DIAGNOSTICO E SEM CURA.

⭐ TRATAMENTO: `vous`. Nao e' escolha de gosto — e' a voz que o repo ja' usa em
frances (`landing-150/index-fr.html`: 47 `vous`, zero `tu`). O alemao usa `du`
porque o pool do `gelo16` fala `du`; o frances nao tem funil com essa trava, e
trocar de registro dentro do mesmo idioma e' o que confunde o comprador.

⚠️ OS TELEFONES DE CRISE SAO OUTROS. Copiar os alemaes seria dar a uma francesa
em crise um numero que nao atende. Franca `3114` (national, gratuito, 24h),
Belgica `0800 32 123`, Suica `143`. Urgencia vital: `112` (ou `15` na Franca).
"""

MARCA = "L'Ancre du Souffle"
SUB_MARCA = "Deux minutes pour dire à votre corps que le danger est passé."

# ⛔ A regra da agua saiu DAQUI porque `EAU_COURTE` ja' a diz, e as duas juntas
# repetiam a mesma ordem no mesmo quadrinho — duas linhas a mais que faziam o
# ultimo passo do card cair sozinho na pagina seguinte. Nenhuma regra se
# perdeu: todo card que usa esta constante usa `EAU_COURTE` logo em seguida.
SECURITE_COURTE = (
    "Asseyez-vous ou allongez-vous. Jamais debout, jamais au volant. Si la "
    "tête tourne, vous arrêtez et vous respirez normalement."
)

EAU_LONGUE = (
    "Jamais dans l'eau. Ni baignoire, ni piscine, ni lac — même en eau peu "
    "profonde et même accompagnée. Exercices de respiration et eau ne vont pas "
    "ensemble, et cette phrase revient dans chaque fichier parce qu'elle est la "
    "plus importante du lot."
)

EAU_COURTE = "Jamais dans l'eau ni au bord — ni baignoire, ni piscine, ni lac."

# ===========================================================================
# ETAPE 1
# ===========================================================================

S1 = {
    "badge": "Étape 1",
    "titel": "Commencez ici",
    "lead": ("Dix minutes de lecture, et vous saurez ce que vous allez faire "
             "pendant trois semaines — et pourquoi ça marche. Ensuite, vous "
             "n'aurez plus jamais besoin de plus de deux minutes d'affilée."),
    "foto": "persona",

    "willkommen_titel": "Contente de vous voir ici",
    "willkommen_sub": ("Avant tout exercice, quelques phrases sur ce que vous "
                       "avez acheté — et sur ce que vous n'avez pas acheté."),
    "willkommen": [
        "Vous n'avez pas acheté une vidéo de cours que vous ne finirez jamais. Vous "
        "avez acheté <b>quelques fichiers</b> que vous pouvez imprimer, lire sur votre "
        "téléphone et poser à côté du lit.",
        "Tout le contenu tourne autour d'<b>une seule chose</b> : expirer plus "
        "longtemps que vous n'inspirez. Cela paraît trop petit pour changer quoi que "
        "ce soit. C'est pourtant ce qui dit le plus vite à votre corps qu'il a le "
        "droit de redescendre.",
        "Tout le reste — la posture, le plan, le soir, l'eau froide — tient à cette "
        "seule phrase.",
        "<b>Et cela prend vraiment deux minutes.</b> Pas vingt. Deux. Celle qui n'a "
        "pas vingt minutes est exactement la personne pour qui ce livret a été fait.",
    ],

    "paket_titel": "Ce que contient ce lot",
    "paket_sub": "Sept fichiers, numérotés dans cet ordre exact.",
    "paket": [
        ("Étape 1", "Commencez ici", "Le fichier que vous lisez. Comment votre "
         "corps déclenche l'alarme, pourquoi l'expiration la coupe, et les "
         "règles de sécurité."),
        ("Étape 2", "L'Ancre du Souffle", "L'exercice de base. La posture, la "
         "main sur les côtes, le rythme 4–6 — et cinq variantes pour le bureau, "
         "le trajet et la file d'attente."),
        ("Étape 3", "L'Ancre d'urgence", "Ce que vous faites quand ça vous tombe "
         "dessus. Quatre-vingt-dix secondes, assise, sans que personne ne "
         "remarque quoi que ce soit."),
        ("Étape 4", "Votre plan de 21 jours", "Jour après jour, une seule tâche "
         "par jour. C'est la partie qui transforme un exercice en habitude."),
        ("Étape 5", "La routine du soir", "Pour la tête qui devient plus bruyante "
         "le soir que la journée, et pour les nuits où vous êtes réveillée à "
         "trois heures."),
        ("Bonus 1", "Le froid sans glace", "Le petit amplificateur : de l'eau "
         "froide sur les poignets, sur le visage, à la fin de la douche. "
         "Facultatif, et jamais en même temps que la respiration."),
        ("Bonus 2", "Votre carnet de calme", "Des fiches à imprimer. Au bout de "
         "trois semaines, vous voyez noir sur blanc ce qui a changé — et ce qui "
         "vous fait monter à chaque fois."),
    ],

    "alarm_titel": "Pourquoi votre corps sonne l'alarme alors qu'il ne se passe rien",
    "alarm_sub": "La partie biologie, courte et honnête. Après, on ne fait que pratiquer.",
    "alarm": [
        "Dans votre corps tourne une partie du système nerveux dont vous n'avez "
        "jamais à vous occuper. Elle règle les battements du cœur, la digestion, le "
        "diamètre des vaisseaux. Vous ne décidez rien : cela se fait tout seul.",
        "Cette partie a deux modes. Le premier vous prépare à agir : cœur plus "
        "rapide, muscles tendus, souffle court et haut dans la poitrine. Le second "
        "fait l'inverse : pouls qui descend, digestion qui repart, souffle lent et "
        "profond dans le ventre.",
        "Chez beaucoup de gens, le premier mode reste <b>allumé</b> alors qu'il n'y a "
        "aucun danger. Pas de bête, pas d'incendie, pas d'attaque — juste un mail, "
        "une facture, une pensée à 23 heures. Le corps déroule quand même tout le "
        "programme.",
        "<b>Et voilà l'endroit où vous pouvez intervenir.</b> De tout ce que ce "
        "système commande, il existe exactement une chose que vous pouvez aussi "
        "prendre en main consciemment : <b>le souffle</b>. Vous ne pouvez pas "
        "ordonner à votre pouls de ralentir. Ni à votre digestion. À votre souffle, "
        "si.",
        "Le souffle est la porte. C'est pour cela que tout ce lot ne parle que de lui.",
    ],

    "ausatmen_titel": "Pourquoi l'expiration, précisément",
    "ausatmen_sub": "L'idée unique sur laquelle tout le reste repose.",
    "ausatmen": [
        "Quand vous <b>inspirez</b>, votre cœur accélère légèrement. Quand vous "
        "<b>expirez</b>, il ralentit. Ce n'est pas une impression, cela se mesure, et "
        "cela arrive à chaque personne à chaque respiration.",
        "Il en découle quelque chose de très simple : <b>plus vous passez de temps à "
        "expirer, plus votre cœur passe de temps dans le mode lent.</b>",
        "C'est exactement ce que nous faisons. Nous ne respirons pas plus "
        "profondément, ni plus vite, ni davantage. Nous déplaçons seulement le "
        "rapport : <b>court à l'entrée, long à la sortie.</b>",
        "Dans l'exercice de base, c'est quatre secondes à l'inspiration et six à "
        "l'expiration. Dix secondes par cycle, six respirations par minute. La "
        "plupart des gens respirent douze à seize fois par minute au repos — vous "
        "descendez donc à peu près de moitié.",
    ],
    "ausatmen_merk": ("Tout ce que vous devez retenir tient dans cette phrase : "
                      "<b>l'expiration est plus longue que l'inspiration.</b> Si "
                      "vous oubliez le reste du lot et gardez celle-là, vous avez "
                      "déjà l'essentiel."),

    "ehrlich_titel": "Remarques honnêtes",
    "ehrlich_sub": "Ce que ce lot peut faire — et ce qu'il ne peut expressément pas.",
    "ehrlich": [
        ("Ce n'est pas un traitement.", "L'Ancre du Souffle est un exercice, pas "
         "une thérapie et pas un médicament. Elle ne remplace ni médecin ni "
         "psychothérapie, et ne pose aucun diagnostic."),
        ("N'arrêtez rien.", "Si vous prenez un traitement, vous continuez. Toute "
         "modification se décide avec la personne qui vous l'a prescrit — pas "
         "avec un PDF."),
        ("Une fois ne suffit pas.", "La première fois, il ne se passe souvent "
         "rien. C'est normal. L'effet vient de la répétition, pas de l'essai "
         "isolé. C'est précisément pour cela qu'il y a un plan de 21 jours."),
        ("Tout ne va pas devenir silencieux.", "Nous ne vous promettons ni une "
         "tête vide ni une vie sans tension. L'objectif est plus petit et plus "
         "honnête : redescendre plus vite qu'avant."),
        ("Vous le sentez d'abord dans le corps.", "La plupart remarquent d'abord "
         "des mains qui se réchauffent, des épaules qui se relâchent ou un "
         "bâillement profond — pas une tête plus calme. La tête vient après."),
    ],

    "sicher_titel": "Sécurité — à lire entièrement, une fois",
    "sicher_sub": "Une page. Elle compte plus que n'importe quel exercice du lot.",
    "sicher_regeln": [
        "<b>Toujours assise ou allongée.</b> Jamais debout. Si la tête tourne, vous "
        "êtes déjà assise.",
        "<b>Jamais au volant.</b> Ni en voiture, ni à vélo, ni sur un escabeau, ni "
        "devant une machine.",
        "<b>Jamais dans l'eau ni au bord de l'eau.</b> Ni baignoire, ni piscine, ni "
        "lac. Même peu profond, même accompagnée.",
        "<b>Arrêtez si ça bascule.</b> Vertiges, fourmillements dans les mains ou "
        "les lèvres, cœur qui s'emballe, pression dans la poitrine : vous arrêtez "
        "l'exercice et vous respirez normalement. Ce n'est pas un échec, c'est de "
        "l'attention.",
        "<b>Ne forcez rien.</b> Si six secondes d'expiration serrent, prenez-en "
        "cinq. Ou quatre. Un exercice qui vous demande un effort fait l'inverse de "
        "ce pour quoi il existe.",
    ],
    "sicher_arzt": (
        "<b>Parlez-en d'abord à votre médecin</b> si vous êtes enceinte, si vous "
        "avez une maladie cardiaque ou pulmonaire, si vous souffrez d'épilepsie, "
        "si vous avez une tension très basse, ou si vous êtes suivie pour une "
        "maladie psychique."
    ),
    "sicher_krise": (
        "<b>Si vous allez très mal en ce moment</b> — si vous traversez une crise "
        "psychique ou si vous avez des pensées de vous faire du mal — alors ce lot "
        "n'est pas la bonne étape suivante. Cherchez de l'aide auprès d'un être "
        "humain. En France, le <b>3114</b> répond gratuitement, jour et nuit. En "
        "Belgique : <b>0800 32 123</b>. En Suisse : <b>143</b>. En cas d'urgence "
        "vitale, appelez le <b>112</b> (ou le <b>15</b> en France)."
    ),

    "los_titel": "Comment procéder maintenant",
    "los_sub": "Quatre phrases, et vous en avez fini avec ce fichier.",
    "los": [
        "Lisez ensuite l'<b>Étape 2</b> et faites l'exercice de base une fois. Cela "
        "prend moins de cinq minutes.",
        "Regardez l'<b>Étape 3</b> aujourd'hui, même si vous n'en avez pas besoin "
        "maintenant. On ne lit pas une notice pendant que ça brûle.",
        "Commencez demain matin avec l'<b>Étape 4</b>, jour 1. Pas ce soir en "
        "vitesse — demain, avec le jour 1.",
        "L'<b>Étape 5</b> et les deux bonus arrivent quand le plan vous le dira. "
        "Vous n'avez pas besoin de les lire avant.",
    ],
    "los_drucken": (
        "<b>Un conseil qui change vraiment quelque chose :</b> imprimez la page de "
        "l'Ancre d'urgence (Étape 3) et posez-la quelque part où vous la trouverez "
        "sans chercher — table de nuit, sac, tiroir du bureau. Dans le moment "
        "même, personne ne tape un nom de fichier."
    ),
}

# ===========================================================================
# ETAPE 2
# ===========================================================================

S2 = {
    "badge": "Étape 2",
    "titel": "L'Ancre du Souffle",
    "lead": ("L'exercice de base et cinq variantes pour le quotidien. Si vous "
             "ne deviez garder qu'un seul fichier de ce lot, ce serait "
             "celui-ci."),
    "foto": "rippen",

    "drei_titel": "Les trois ancres",
    "drei_sub": ("Une ancre tient un bateau au même endroit pendant que tout "
                 "bouge autour. C'est exactement ce que font ces trois-là."),
    "drei": [
        ("L'ancre du corps", "Votre façon de vous asseoir. Un corps affaissé ne "
         "laisse tout simplement pas l'air descendre. On commence donc par la "
         "posture, pas par le souffle."),
        ("L'ancre du souffle", "Le rythme : quatre secondes à l'inspiration, six "
         "à l'expiration. C'est le cœur de la méthode, et tout le reste du lot "
         "n'en est qu'une variante."),
        ("L'ancre du regard", "Où va l'attention pendant que vous respirez. Sans "
         "cette troisième ancre, vous comptez tout en pensant à demain — et là, "
         "ça ne marche qu'à moitié."),
    ],

    "uebungen": [
        {
            "tag": "Base",
            "nome": "La posture",
            "hook": ("Avant de changer une seule respiration : voici comment vous "
                     "asseoir pour que l'air puisse descendre."),
            "foto": "haltung",
            "stats": [("1 min", "Durée"), ("Chaise", "Lieu"), ("Chaque jour", "Fréquence")],
            "ritmo": None,
            "schritte": [
                "Asseyez-vous sur la <b>moitié avant</b> d'une chaise. Sans vous "
                "adosser, mais sans raideur non plus — vous devez être à l'aise, pas "
                "au garde-à-vous.",
                "Les deux <b>pieds à plat au sol</b>, écartés d'environ la largeur des "
                "hanches. Si vos pieds ne touchent pas, glissez un livre dessous.",
                "<b>Basculez légèrement le bassin vers l'avant</b>, de façon à vous "
                "asseoir sur les ischions et non sur le coccyx. Le bas du dos "
                "retrouve ainsi sa courbe naturelle.",
                "<b>Montez les épaules, tenez un instant, laissez-les tomber.</b> Deux "
                "fois. Là où elles atterrissent est le bon endroit.",
                "<b>Menton très légèrement vers la poitrine</b>, comme si vous teniez "
                "une noix sous le menton. La nuque s'allonge.",
                "<b>Mains posées sans effort sur les cuisses.</b> Voilà. C'est ainsi "
                "que vous vous asseyez pour chaque exercice de ce lot.",
            ],
            "worauf": ("Quand la posture est juste, votre ventre avance un peu de "
                       "lui-même à l'inspiration, sans que vous poussiez quoi que "
                       "ce soit. Si cela n'arrive pas, le bas du dos est encore "
                       "probablement affaissé."),
            "sicher": None,
        },
        {
            "tag": "Base",
            "nome": "La main sur les côtes",
            "hook": ("La plupart des gens respirent en haut, dans la poitrine. Cet "
                     "exercice vous dit en deux minutes si vous en faites partie."),
            "foto": "rippen",
            "stats": [("2 min", "Durée"), ("Assise", "Posture"), ("Une fois", "Pour tester")],
            "ritmo": None,
            "schritte": [
                "Asseyez-vous comme dans l'exercice précédent.",
                "Posez une <b>main à plat sur les côtes basses</b>, sur le côté, là où "
                "la cage thoracique se rétrécit. L'autre main sur le ventre.",
                "Respirez <b>tout à fait normalement</b>. Pas plus profondément, pas "
                "plus consciemment. Juste normalement, et observez cinq ou six "
                "respirations.",
                "<b>Quelle main bouge le plus ?</b> Si c'est celle du haut, vous "
                "respirez dans la poitrine — c'est le cas de la plupart des gens, et "
                "c'est précisément la respiration que le corps utilise en état "
                "d'alarme.",
                "Dirigez maintenant l'air <b>vers le bas</b> : imaginez que vous "
                "respirez dans votre main posée sur les côtes et que vous la poussez "
                "doucement vers l'extérieur.",
                "Cinq respirations ainsi. Les épaules restent basses — si elles "
                "montent, vous êtes remontée en haut.",
            ],
            "worauf": ("C'est juste quand les côtes s'ouvrent <b>sur les côtés</b>, "
                       "comme un soufflet, et que les épaules restent immobiles. "
                       "C'est cette respiration que vous utiliserez dans tous les "
                       "exercices suivants."),
            "sicher": None,
        },
        {
            "tag": "L'exercice principal",
            "nome": "L'Ancre du Souffle 4–6",
            # ⛔ O antigo passo 1 ("sente-se como no exercicio 1") virou parte do
            # chapeu. Nao e' uma acao do ritmo, e' o ponto de partida — e como
            # passo custava um bloco inteiro que empurrava o ultimo passo para
            # uma pagina so' dele. Seis passos viraram cinco sem perder nada.
            "hook": ("La voici. Deux minutes, douze respirations, et vous n'avez "
                     "besoin de rien d'autre qu'une chaise. Asseyez-vous comme dans "
                     "l'exercice 1 — une main peut rester sur les côtes, cela aide "
                     "au début."),
            "foto": "anker",
            "stats": [("2 min", "Durée"), ("12", "Respirations"), ("6 / min", "Fréquence")],
            "ritmo": (4, 6, 0, 3),
            "schritte": [
                "<b>Inspirez par le nez en comptant jusqu'à quatre.</b> Pas au maximum — "
                "environ aux trois quarts. À bloc, c'est désagréable et cela fait "
                "l'inverse.",
                "<b>Expirez par le nez en comptant jusqu'à six.</b> Laissez l'air sortir "
                "plutôt que de le pousser. À la fin il en reste, et c'est voulu.",
                "<b>Aucune pause.</b> Les six passées, l'inspiration suivante commence "
                "directement. On ne bloque jamais, ni plein ni vide.",
                "<b>L'ancre du regard :</b> choisissez <b>une</b> chose à laquelle vous "
                "restez — les chiffres, l'air aux narines, ou la main. Une, pas trois.",
                "<b>Douze respirations</b>, soit deux minutes. Ensuite vous arrêtez, "
                "même si c'est agréable.",
            ],
            "worauf": ("Des mains qui se réchauffent. Un bâillement profond. Des "
                       "épaules qui descendent. Ce sont les signes que le mode calme "
                       "s'est enclenché — et ils arrivent presque toujours avant la "
                       "sensation d'être calme."),
            "sicher": SECURITE_COURTE + " " + EAU_COURTE,
        },
        {
            "tag": "Variante",
            "nome": "Si six, c'est trop long",
            "hook": ("Pour toutes celles chez qui l'expiration longue serre au "
                     "début. C'est fréquent et ce n'est pas mauvais signe."),
            "foto": "nase",
            "stats": [("2 min", "Durée"), ("3→4", "Départ"), ("1 semaine", "Montée")],
            "ritmo": (3, 4, 0, 3),
            "schritte": [
                "Commencez à <b>trois à l'inspiration, quatre à l'expiration</b>. Le "
                "rapport est déjà bon — la sortie est plus longue que l'entrée — et "
                "c'est cela qui compte.",
                "Restez-y deux ou trois jours, jusqu'à ce que ce soit sans effort.",
                "Passez ensuite à <b>trois / cinq</b>. Encore quelques jours.",
                "Puis <b>quatre / six</b>. C'est la forme cible.",
                "Si une journée se passe moins bien, revenez d'un cran en arrière. "
                "C'est permis et cela arrive à tout le monde.",
            ],
            "worauf": ("Cette montée progressive n'est pas un lot de consolation. "
                       "Un rythme que vous tenez trois semaines fait plus qu'un "
                       "rythme impressionnant abandonné au bout de quatre jours."),
            "sicher": ("Ne forcez jamais le chiffre. Si vous devez happer l'air à la "
                       "fin de l'expiration, l'intervalle est trop long — enlevez une "
                       "seconde."),
        },
        {
            "tag": "Quotidien",
            "nome": "L'ancre au bureau",
            "hook": ("La version que personne ne remarque dans la pièce. Pas d'yeux "
                     "fermés, pas de geste, pas de bruit."),
            "foto": "schreibtisch",
            "stats": [("90 s", "Durée"), ("Invisible", "Pour les autres"), ("2–3x", "Par jour")],
            "ritmo": (4, 6, 0, 3),
            "schritte": [
                "<b>Les yeux restent ouverts</b>, sur l'écran ou sur un point de la "
                "table. Personne ne voit rien.",
                "<b>Les deux pieds à plat au sol</b>, en appuyant très légèrement dans "
                "le sol. C'est votre ancre du corps en position assise — discrète et "
                "efficace.",
                "Retirez les <b>mains du clavier</b> et posez-les sur vos cuisses. Cela "
                "seul fait déjà descendre les épaules.",
                "Neuf respirations au rythme <b>4–6</b>, par le nez, sans un bruit.",
                "<b>Ici, l'ancre du regard, ce sont les pieds</b>, pas les chiffres — "
                "sentez le sol sous vos semelles pendant que vous comptez.",
            ],
            "worauf": ("Le meilleur moment est <b>avant</b> le rendez-vous difficile, "
                       "pas après. Deux minutes en amont ne vous coûtent rien et "
                       "changent la voix avec laquelle vous entrez."),
            "sicher": None,
        },
        {
            "tag": "Quotidien",
            "nome": "L'ancre en marchant",
            "hook": ("Pour celles que l'immobilité rend nerveuses. Le corps bouge, "
                     "le rythme reste."),
            "foto": "gehen",
            "stats": [("5 min", "Durée"), ("Dehors", "Lieu"), ("Les pas", "La mesure")],
            "ritmo": (4, 6, 0, 3),
            "schritte": [
                "Marchez à un <b>rythme calme et régulier</b>. Pas de sport, pas "
                "d'objectif, pas de montre.",
                "Au lieu des secondes, comptez les <b>pas</b> : inspirez sur quatre "
                "pas, expirez sur six pas.",
                "Si cela ne tombe pas juste, marchez plus lentement. <b>C'est le "
                "souffle qui donne la mesure, pas les jambes.</b>",
                "Par le nez, même en marchant. Si vous n'y arrivez pas, vous allez "
                "trop vite.",
                "Cinq minutes suffisent. Ensuite vous reprenez votre marche normale.",
            ],
            "worauf": ("Cette variante est la meilleure pour les journées agitées. "
                       "Si rester assise revient à tenir en place sous tension, "
                       "marcher n'est pas un recul : c'est le chemin qui convient."),
            "sicher": ("Uniquement là où vous n'avez à faire attention à rien. Pas au "
                       "bord d'une route, pas avec des écouteurs dans la circulation, "
                       "et pas au bord de l'eau — ni berge, ni ponton, ni bassin."),
        },
    ],

    "fehler_titel": "Les cinq erreurs les plus fréquentes",
    "fehler_sub": ("Quand l'exercice devient désagréable, la raison est presque "
                   "toujours dans cette liste."),
    "fehler": [
        ("Inspirer trop plein.", "L'erreur la plus fréquente de toutes. « Respirer "
         "profondément » ne veut pas dire « respirer beaucoup ». Aux trois quarts "
         "suffit — à ras bord, cela crée exactement la pression dans la poitrine "
         "dont vous voulez vous débarrasser."),
        ("Bloquer la respiration.", "Ni en haut ni en bas. Dès que l'inspiration "
         "est finie, l'expiration commence, et inversement. Bloquer rend beaucoup "
         "de gens plus agités, pas plus calmes."),
        ("Respirer par la bouche.", "Le nez réchauffe et freine l'air. Par la "
         "bouche, il en entre trop, trop vite. L'exception est l'ancre d'urgence "
         "de l'Étape 3, et la raison y est expliquée."),
        ("Respirer avec les épaules.", "Si vos épaules montent à chaque "
         "inspiration, vous respirez en haut. Revenez à la main sur les côtes "
         "jusqu'à ce que le mouvement se refasse en bas."),
        ("Le faire trop longtemps.", "Douze respirations, puis stop. Vingt minutes "
         "d'affilée ne valent pas mieux — c'est simplement ce que vous ne referez "
         "plus la semaine prochaine."),
    ],

    "faq": [
        ("Je bâille sans arrêt. Je fais quelque chose de travers ?",
         "Au contraire. Bâillements, soupirs et déglutitions apparaissent "
         "justement quand le corps passe du mode alarme au mode calme. Laissez "
         "faire."),
        ("Je perds le compte en permanence.",
         "C'est normal et ce n'est pas un problème. Quand vous remarquez que vous "
         "étiez partie, vous reprenez à un à la respiration suivante. C'est le "
         "fait de remarquer qui est l'exercice, pas le fait de tenir."),
        ("Faut-il fermer les yeux ?",
         "Non. Certaines personnes deviennent plus agitées les yeux fermés, parce "
         "que les pensées sont alors plus fortes. Un regard doux posé sur un point "
         "fixe fonctionne tout aussi bien."),
        ("Quel est le meilleur moment de la journée ?",
         "Le matin, parce qu'à ce moment-là vous ne pouvez pas encore négocier "
         "avec vous-même. Le plan de l'Étape 4 l'accroche pour cela à quelque "
         "chose que vous faites déjà chaque matin."),
        ("Puis-je le faire plus de deux fois par jour ?",
         "Oui, aussi souvent que vous voulez — tant que cela reste court. Six fois "
         "deux minutes réparties dans la journée valent mieux qu'une fois douze "
         "minutes."),
    ],
}

# ===========================================================================
# ROTULOS / ARQUIVOS
# ===========================================================================

ROT = {
    "merk": "Comment vous savez que ça agit",
    "stop": "Sécurité",
    "faq": "Questions fréquentes",
    "tag": "JOUR",
    "anker": "ANCRE",
    "s1_satz": "La phrase unique",
    "s1_arzt": "À demander avant",
    "s1_krise": "Crise aiguë",
    "s1_druck": "À imprimer",
    "s3_real": "Rester réaliste",
    "s3_notruf": "Quand ce n'est pas une affaire d'exercice respiratoire",
    "s4_warum": "Pourquoi 21 jours",
    "s6_wer": "Qui doit sauter ce bonus",
    "s7_skala": "À propos de l'échelle",
    "s7_ende": "Pour finir",
    "dias": ["Lun", "Mar", "Mer", "Jeu", "Ven", "Sam", "Dim"],
    "woche": "Semaine",
    "svg": {"ein": "INSP", "aus": "EXP", "ein_longo": "INSPIREZ",
            "aus_longo": "EXPIREZ", "cheio": "PLEIN", "vazio": "VIDE",
            "legenda": "L&#39;expiration est plus longue. C&#39;est tout le principe."},
}

ARQUIVOS = [
    "Etape 1 - Commencez ici.pdf",
    "Etape 2 - L'Ancre du Souffle.pdf",
    "Etape 3 - L'Ancre d'urgence.pdf",
    "Etape 4 - Votre plan de 21 jours.pdf",
    "Etape 5 - La routine du soir.pdf",
    "Etape 6 - Bonus 1 - Le froid sans glace.pdf",
    "Etape 7 - Bonus 2 - Votre carnet de calme.pdf",
]

TITULOS_DOC = [
    "Commencez ici — L'Ancre du Souffle", "L'Ancre du Souffle",
    "L'Ancre d'urgence", "Votre plan de 21 jours", "La routine du soir",
    "Le froid sans glace", "Votre carnet de calme",
]
