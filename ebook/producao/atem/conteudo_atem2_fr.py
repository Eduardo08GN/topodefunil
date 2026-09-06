# -*- coding: utf-8 -*-
"""CONTEUDO — L'ANCRE DU SOUFFLE, parte 2: Etapas 3 a 7.

Continuacao de `conteudo_atem_fr.py`. As tres travas do cabecalho de la' valem
aqui inteiras: sem hiperventilacao, agua nunca, sem diagnostico e sem cura.
"""

from conteudo_atem_fr import SECURITE_COURTE, EAU_COURTE

# ===========================================================================
# ETAPE 3
# ===========================================================================

S3 = {
    "badge": "Étape 3",
    "titel": "L'Ancre d'urgence",
    "lead": ("Pour le moment où ça vous tombe dessus. Quatre-vingt-dix "
             "secondes, assise, sans que personne dans la pièce ne s'en rende "
             "compte. Lisez ceci aujourd'hui — pas quand vous en aurez besoin."),
    "foto": "akut",

    "was_titel": "Ce qui se passe à cet instant précis",
    "was_sub": ("Savoir ce que fait le corps lui enlève déjà une partie de sa "
                "taille."),
    "was": [
        "Votre corps a décidé que quelque chose était dangereux et il bascule en "
        "mode action. Le cœur accélère pour envoyer du sang aux muscles. Le souffle "
        "monte dans la poitrine et se raccourcit. Les mains deviennent froides, "
        "parce que le sang est ramené de la périphérie vers le centre.",
        "Tout cela est <b>logique</b> — simplement inutile en ce moment. Le corps "
        "déroule un programme prévu pour un danger qui n'est pas là.",
        "Et voici la partie difficile à croire sur le moment : <b>c'est le souffle "
        "rapide qui maintient le programme en marche.</b> Quand vous respirez vite et "
        "haut dans la poitrine, votre corps se répond à lui-même : « on est encore "
        "en plein dedans ». C'est une boucle.",
        "L'Ancre d'urgence coupe exactement cette boucle au seul endroit que vous "
        "pouvez atteindre — <b>l'expiration</b>.",
    ],
    "was_merk": ("N'attendez pas de passer de cent à zéro. L'objectif est de "
                 "passer de <b>neuf à six</b>. À partir de six, vous avancez "
                 "seule ; à partir de neuf, non."),

    "uebungen": [
        {
            "tag": "Aigu",
            "nome": "Le frein aux lèvres",
            "hook": ("Le premier exercice dans le moment aigu, parce que c'est le "
                     "seul qui marche encore quand vous ne pensez plus clairement."),
            "foto": "lippen",
            "stats": [("90 s", "Durée"), ("6", "Respirations"), ("Immédiat", "Usage")],
            "ritmo": (4, 8, 0, 2),
            "schritte": [
                "<b>Asseyez-vous.</b> N'importe où — chaise, bord du lit, marche "
                "d'escalier, abattant des toilettes. L'essentiel est d'être assise.",
                "<b>Inspirez par le nez, comptez jusqu'à quatre.</b> Pas "
                "profondément. Une quantité tout à fait normale.",
                "<b>Pincez les lèvres</b>, comme pour souffler dans une paille ou "
                "pour presque éteindre une bougie — sans l'atteindre.",
                "<b>Expirez par cette fente étroite en comptant jusqu'à huit.</b> La "
                "résistance aux lèvres rend l'expiration longue facile ; sans elle, "
                "c'est presque impossible dans le moment aigu.",
                "<b>Six respirations.</b> Cela fait environ quatre-vingt-dix secondes.",
                "Ensuite, passez à la respiration nasale normale <b>4–6</b>, aussi "
                "longtemps que cela fait du bien.",
            ],
            "worauf": ("Le premier signe n'est presque jamais « je suis calme ». "
                       "C'est un soupir profond et involontaire, ou le fait de "
                       "remarquer à quel point vos mâchoires étaient serrées."),
            "sicher": SECURITE_COURTE + " " + EAU_COURTE,
        },
        {
            "tag": "Aigu",
            "nome": "L'ancre au sol 5–4–3",
            "hook": ("Quand la tête tourne en boucle et que compter ne suffit pas : "
                     "l'ancre passe alors par les sens."),
            "foto": "boden",
            "stats": [("2 min", "Durée"), ("Yeux ouverts", "Toujours"), ("Partout", "Lieu")],
            "ritmo": None,
            "schritte": [
                "Asseyez-vous et faites <b>une</b> longue expiration avant de "
                "commencer.",
                "<b>Cinq choses que vous voyez.</b> Nommez-les intérieurement — "
                "« encadrement », « tasse », « câble ». Après chaque chose, une "
                "longue expiration.",
                "<b>Quatre choses que vous entendez.</b> Y compris les discrètes : le "
                "réfrigérateur, une voiture, votre propre souffle.",
                "<b>Trois choses que vous sentez.</b> Les pieds dans les chaussures. "
                "Le tissu sur le bras. L'assise sous vous.",
                "Puis six respirations <b>4–6</b>, et c'est terminé.",
            ],
            "worauf": ("Cet exercice sort l'attention de la tête pour la ramener "
                       "dans la pièce. Il est particulièrement utile quand compter "
                       "est devenu lui-même une source de tension (« est-ce que je "
                       "le fais bien ? »)."),
            "sicher": None,
        },
        {
            "tag": "La nuit",
            "nome": "L'ancre de trois heures du matin",
            "hook": ("Pour le réveil au milieu de la nuit, quand la tête est "
                     "immédiatement à pleine puissance."),
            "foto": "nacht",
            "stats": [("Allongée", "Posture"), ("Sans lumière", "Règle"), ("4–8", "Rythme")],
            "ritmo": (4, 8, 0, 2),
            "schritte": [
                "<b>Restez allongée et n'allumez pas.</b> Pas de téléphone — un "
                "regard sur l'écran met fin à la nuit pour de bon.",
                "Tournez-vous sur le <b>côté droit</b> ou sur le dos, selon ce qui est "
                "plus confortable, et posez une main sur le ventre.",
                "<b>Quatre à l'inspiration par le nez, huit à l'expiration par le "
                "nez.</b> L'expiration longue est plus facile allongée qu'assise.",
                "<b>Comptez les expirations à rebours</b>, de dix à un. Si vous "
                "arrivez à un et que vous êtes encore éveillée, vous repartez de dix.",
                "Il est expressément <b>égal</b> que vous vous rendormiez ou non. Dès "
                "que se rendormir devient l'objectif, cela devient un examen — et les "
                "examens tiennent éveillée.",
            ],
            "worauf": ("Rester allongée calmement et respirer repose votre corps "
                       "bien plus que rester allongée éveillée à calculer combien "
                       "d'heures il reste. Ce n'est pas une consolation, c'est le "
                       "but réel."),
            "sicher": None,
        },
    ],

    "wenn_titel": "Si ça n'agit pas tout de suite",
    "wenn_sub": "Trois phrases qui vous aideront alors.",
    "wenn": [
        "<b>N'attendez pas un interrupteur.</b> C'est un variateur. De neuf à six, "
        "c'est tout le travail — et à partir de six, vous avancez seule.",
        "<b>Ne forcez pas les chiffres.</b> Si huit secondes d'expiration ne "
        "passent pas sur le moment, prenez-en six. C'est le rapport qui compte, pas "
        "la valeur.",
        "<b>L'Ancre d'urgence s'améliore avec la pratique.</b> Celle qui l'a "
        "travaillée trois semaines au calme retrouve quelque chose de connu le jour "
        "où ça arrive. Celle qui l'essaie pour la première fois en pleine tempête a "
        "bien plus de mal. C'est exactement pour cela qu'il y a l'Étape 4.",
    ],

    "plan_titel": "Votre plan d'urgence à imprimer",
    "plan_sub": ("Remplissez-le une fois au calme et posez-le là où vous le "
                 "trouverez sans chercher."),
    "plan_zeilen": [
        ("Je le remarque d'abord à …", "ex. poitrine serrée, mains froides, boule dans la gorge"),
        ("Ensuite je m'assois — ici :", "ex. chaise de cuisine, bord du lit, voiture à l'arrêt"),
        ("Je fais :", "frein aux lèvres 4–8, six respirations"),
        ("Ensuite :", "respiration nasale 4–6, tant que ça fait du bien"),
        ("Si ça ne va pas mieux, j'appelle :", "nom et numéro d'une personne"),
    ],
    "plan_hinweis": (
        "<b>À prendre au sérieux une bonne fois :</b> une forte douleur dans la "
        "poitrine, une difficulté à respirer, un malaise avec perte de "
        "connaissance ou un état vraiment différent de d'habitude ne relèvent pas "
        "d'un exercice de respiration mais du <b>112</b> (ou du <b>15</b> en "
        "France). Un exercice ne remplace pas un avis médical."
    ),
}

# ===========================================================================
# ETAPE 4
# ===========================================================================

S4 = {
    "badge": "Étape 4",
    "titel": "Votre plan de 21 jours",
    "lead": ("Une tâche par jour, jamais plus de cinq minutes. C'est la partie "
             "qui transforme un exercice en habitude — et la seule raison pour "
             "laquelle, dans trois semaines, ce sera différent d'aujourd'hui."),
    "foto": "plan21",

    "wie_titel": "Comment fonctionne ce plan",
    "wie_sub": "Quatre règles, et les quatre sont volontairement placées bas.",
    "wie": [
        "<b>Une tâche par jour.</b> Pas trois. Si vous voulez en faire plus, faites "
        "plus — mais la tâche reste toujours une seule.",
        "<b>Accrochez-la à quelque chose que vous faites déjà.</b> Après le brossage "
        "de dents. Après que le café a coulé. En vous asseyant dans la voiture, "
        "avant de démarrer. Une habitude a besoin d'un voisin fixe, pas d'une alarme.",
        "<b>Un jour manqué n'est pas un abandon.</b> Vous reprenez le lendemain là où "
        "vous en étiez. Deux jours manqués non plus. Ce plan n'a pas de date limite.",
        "<b>Cochez.</b> Chaque jour une croix dans le tableau à la fin de ce fichier "
        "ou dans le carnet de calme. Cela paraît puéril et c'est pourtant la raison "
        "pour laquelle les gens sont encore là en semaine trois.",
    ],
    "wie_merk": ("Pourquoi 21 jours ? Pas parce qu'une habitude serait prête au "
                 "bout de 21 jours exactement — c'est un mythe, et nous ne vous "
                 "le vendons pas. Trois semaines, c'est simplement assez long "
                 "pour que vous remarquiez la différence vous-même, et assez "
                 "court pour qu'on tienne."),

    "wochen": [
        {
            "rot": "Semaine 1",
            "titel": "Les fondations",
            "text": ("Cette semaine sert seulement à faire entrer le rythme dans "
                     "le corps — pas encore à l'utiliser quand c'est difficile."),
            "tage": [
                (1, "La posture", "Lisez l'Étape 2 et ne faites que l'exercice « La "
                    "posture ». Deux minutes. Pas encore de rythme aujourd'hui."),
                (2, "La main sur les côtes", "Découvrez si vous respirez en haut ou "
                    "en bas. Cinq respirations avec la main sur les côtes."),
                (3, "4–6 pour la première fois", "Douze respirations au rythme 4–6. "
                    "Si six est trop long, prenez 3–4. Les deux sont justes."),
                (4, "Encore 4–6", "La même chose qu'hier, même heure, même endroit. "
                    "Aujourd'hui, la répétition est la vraie tâche."),
                (5, "L'ancre du regard", "Aujourd'hui vous choisissez volontairement "
                    "<b>une</b> chose à laquelle vous restez : les chiffres, l'air "
                    "aux narines, ou la main. Une seule."),
                (6, "Deux minutes sans compter", "Faites l'exercice, mais sans "
                    "compter. Seulement « long à la sortie ». Ensuite : avez-vous "
                    "tenu le rythme ?"),
                (7, "Bilan", "L'exercice comme d'habitude, puis une minute : qu'est-ce "
                    "qui a été différent cette semaine ? Écrivez une phrase dans le "
                    "carnet de calme."),
            ],
        },
        {
            "rot": "Semaine 2",
            "titel": "Deux fois par jour",
            "text": ("Le deuxième rendez-vous s'ajoute, et vous travaillez pour la "
                     "première fois l'Ancre d'urgence — au calme, exprès, pendant "
                     "qu'il ne se passe rien."),
            "tage": [
                (8, "Matin et soir", "Deux fois deux minutes. Le rendez-vous du soir "
                    "s'accroche à quelque chose que vous faites déjà."),
                (9, "Travailler le frein aux lèvres", "Lisez l'Étape 3 et faites le "
                    "frein aux lèvres une fois, tranquillement. C'est maintenant, "
                    "quand vous n'en avez pas besoin, que vous l'apprenez."),
                (10, "L'ancre au bureau", "Glissez la variante invisible une fois "
                     "dans votre journée de travail — avant un rendez-vous, pas "
                     "après."),
                (11, "Avant le moment difficile", "Choisissez aujourd'hui une "
                     "situation dont vous savez qu'elle vous tend, et respirez deux "
                     "minutes <b>avant</b>."),
                (12, "L'ancre en marchant", "Cinq minutes de marche, quatre pas à "
                     "l'inspiration, six pas à l'expiration. Même si vous êtes du "
                     "genre assise : essayez une fois."),
                (13, "Expirer plus longtemps", "Aujourd'hui 4–7 au lieu de 4–6, si "
                     "cela passe sans effort. Sinon vous restez à 4–6. Aucun malus."),
                (14, "Bilan", "Deux fois deux minutes, puis : dans quelle situation "
                     "l'ancre vous aurait-elle bien servi cette semaine, alors que "
                     "vous l'avez oubliée ?"),
            ],
        },
        {
            "rot": "Semaine 3",
            "titel": "Dans la vraie vie",
            "text": ("L'exercice quitte le rendez-vous protégé. Cette semaine, "
                     "vous l'utilisez là où il a réellement sa place."),
            "tage": [
                (15, "L'ancre du soir", "Lisez l'Étape 5 et faites la routine du "
                     "soir pour la première fois, au lit, allongée."),
                (16, "Sans préparation", "Faites l'exercice aujourd'hui à un moment "
                     "spontané, quand vous remarquez que vous êtes tendue. Peu "
                     "importe où."),
                (17, "L'eau froide", "Lisez le Bonus 1 et ne faites que l'exercice "
                     "des poignets. Vingt secondes, pas plus."),
                (18, "L'ancre au sol", "Faites aujourd'hui le 5–4–3 de l'Étape 3 une "
                     "fois au calme, pour le connaître le jour venu."),
                (19, "Deux fois, plus une fois spontanée", "Les deux rendez-vous "
                     "fixes, et une fois quand la journée le demande."),
                (20, "Votre propre rythme", "Trouvez la variante qui vous apporte le "
                     "plus, et ne faites que celle-là aujourd'hui."),
                (21, "Le bilan", "L'exercice comme d'habitude. Ensuite vous prenez le "
                     "carnet de calme et vous relisez les trois semaines d'un trait. "
                     "C'est le moment le plus important de tout le plan."),
            ],
        },
    ],

    "danach_titel": "Et après le jour 21 ?",
    "danach_sub": "La partie honnête.",
    "danach": [
        "Cela ne s'arrête pas. L'Ancre du Souffle n'est pas une cure que l'on "
        "termine — c'est plutôt comme se brosser les dents : petit, sans éclat, et "
        "on le remarque surtout quand cela disparaît.",
        "<b>Ce qui reste dans la plupart des cas :</b> deux fois deux minutes par "
        "jour, matin et soir, plus l'Ancre d'urgence quand elle sert. Cela fait "
        "quatre minutes. Il n'en faut pas plus sur la durée.",
        "<b>Si vous sentez que ça vous échappe</b> — et cela arrive à presque tout "
        "le monde à un moment — vous recommencez simplement au jour 1. Le deuxième "
        "tour va nettement plus vite que le premier.",
    ],

    "tabela_col": "Fait",
    "tabelle_titel": "Votre tableau de croix",
    "tabelle_sub": ("Imprimez cette page. Une croix par jour, rien de plus — les "
                    "notes vont dans le carnet de calme."),
}

# ===========================================================================
# ETAPE 5
# ===========================================================================

S5 = {
    "badge": "Étape 5",
    "titel": "La routine du soir",
    "lead": ("Pour la tête qui devient plus bruyante le soir que la journée. "
             "Vingt minutes avant d'éteindre, et un exercice pour les nuits où "
             "vous vous réveillez à trois heures."),
    "foto": "abend",

    "warum_titel": "Pourquoi la tête devient plus bruyante le soir",
    "warum_sub": "Ce n'est pas parce que vous réfléchissez trop.",
    "warum": [
        "La journée, votre tête est occupée. Il y a des tâches, des gens, des "
        "bruits, des écrans. Tout cela consomme de l'attention, et l'attention est "
        "limitée.",
        "Le soir, tout cela disparaît. Pour la première fois depuis le lever, il y a "
        "de la <b>place</b> — et ce que vous entendez alors était là toute la "
        "journée. C'était simplement couvert.",
        "C'est pour cela que le conseil « n'y pense pas » échoue si régulièrement. "
        "On ne peut pas s'ordonner de ne pas penser à quelque chose.",
        "Ce que vous pouvez faire : <b>donner au corps un signal plus fort que la "
        "pensée.</b> Une expiration longue est un tel signal. Une pièce chaude, une "
        "lumière tamisée et un corps allongé en sont trois autres.",
    ],

    "uebungen": [
        {
            "tag": "Le soir",
            "nome": "L'ancre du soir 4–8",
            "hook": ("Le même exercice que la journée, avec une expiration deux "
                     "fois plus longue — allongée, cela devient soudain facile."),
            "foto": "liegen",
            "stats": [("3 min", "Durée"), ("10", "Respirations"), ("Au lit", "Lieu")],
            "ritmo": (4, 8, 0, 2),
            "schritte": [
                "<b>Allongez-vous sur le dos</b>, jambes longues, bras le long du "
                "corps. Si le bas du dos tire, glissez un coussin sous les genoux.",
                "Une <b>main sur le ventre</b>. Allongée, vous sentez le mouvement plus "
                "nettement qu'assise.",
                "<b>Quatre à l'inspiration par le nez.</b> Pas profondément — une "
                "quantité normale.",
                "<b>Huit à l'expiration par le nez.</b> Laissez l'air s'écouler hors "
                "de vous, sans pousser. Si huit est trop, prenez-en six.",
                "<b>Dix respirations.</b> Ensuite vous arrêtez de compter et vous "
                "laissez le souffle faire ce qu'il veut.",
            ],
            "worauf": ("Le ventre devient souple. Souvent, c'est seulement là que "
                       "vous remarquez que vous l'aviez tenu contracté toute la "
                       "journée."),
            "sicher": SECURITE_COURTE + " " + EAU_COURTE,
        },
        {
            "tag": "Le soir",
            "nome": "Le scan du corps, de bas en haut",
            "hook": ("Pour les soirs où le souffle seul ne rattrape pas la tête. "
                     "Dix minutes, et vous êtes rarement éveillée à la fin."),
            "foto": "scan",
            "stats": [("10 min", "Durée"), ("Allongée", "Posture"), ("Du bas", "Sens")],
            "ritmo": None,
            "schritte": [
                "Allongez-vous et faites <b>cinq respirations</b> au rythme 4–8, pour "
                "que le corps sache ce qui arrive.",
                "Puis remontez avec l'attention <b>depuis les pieds</b>. D'abord le "
                "pied gauche, puis le droit. Les mollets. Les genoux. Les cuisses. "
                "Le bassin.",
                "À chaque endroit, restez <b>deux respirations</b> et posez une seule "
                "question : <b>y a-t-il quelque chose de serré ici ?</b> Si oui, "
                "relâchez-le d'un cran à l'expiration.",
                "Continuez : ventre, bas du dos, cage thoracique, mains, bras, "
                "épaules.",
                "<b>Les quatre endroits où presque tout le monde trouve quelque "
                "chose :</b> la mâchoire, la langue, le front entre les sourcils, les "
                "épaules. Prenez plus de temps pour ces quatre-là.",
                "À la fin, la tête. Ensuite vous restez simplement allongée, sans "
                "rien faire.",
            ],
            "worauf": ("La mâchoire est la surprise pour la plupart des gens. Quand "
                       "vous desserrez les dents et décollez la langue du palais, "
                       "une partie de la tension de la nuque part souvent avec."),
            "sicher": None,
        },
        {
            "tag": "S'endormir",
            "nome": "À rebours depuis cent",
            "hook": ("Quand les pensées tournent, ce n'est pas le vide qui aide — "
                     "c'est une tâche assez ennuyeuse."),
            "foto": "einschlafen",
            "stats": [("Libre", "Durée"), ("Allongée", "Posture"), ("Chaque nuit", "Si besoin")],
            "ritmo": None,
            "schritte": [
                "Respirez au rythme <b>4–8</b>, sans compter les secondes.",
                "À <b>chaque expiration</b>, comptez intérieurement un nombre à "
                "rebours, en partant de cent. Expiration — cent. Expiration — "
                "quatre-vingt-dix-neuf.",
                "Si vous vous trompez ou perdez le nombre, c'est <b>bon signe</b> : "
                "cela veut dire que votre tête est en train de décrocher. Reprenez à "
                "un nombre rond quelconque.",
                "Si vous arrivez à quatre-vingts et que vous êtes bien réveillée, "
                "arrêtez, levez-vous un instant, buvez une gorgée d'eau et "
                "recouchez-vous. Rester des heures éveillée au lit n'apporte rien.",
            ],
            "worauf": ("L'astuce, c'est l'<b>ennui</b>. La tâche doit occuper juste "
                       "assez d'attention pour qu'il ne reste rien à la boucle des "
                       "soucis — et être assez fade pour ne pas vous tenir éveillée."),
            "sicher": None,
        },
    ],

    "stunde_titel": "La dernière heure avant de dormir",
    "stunde_sub": ("Cinq choses qui apportent plus que n'importe quel exercice — "
                   "et trois d'entre elles ne coûtent rien."),
    "stunde": [
        ("Baissez la lumière, une heure avant.", "Pas le plafonnier, une petite "
         "lampe. Votre corps lit la luminosité comme une heure."),
        ("L'écran hors du lit.", "Pas seulement à cause de la lumière bleue — "
         "surtout parce que ce qui se passe sur l'écran vous tient éveillée. Les "
         "informations à 23 heures sont une décision contre le sommeil."),
        ("Dormez au frais.", "Autour de 18 degrés. Pour s'endormir, le corps doit "
         "baisser sa température centrale, et dans une pièce chaude c'est plus "
         "difficile."),
        ("Le papier à côté du lit.", "Si quelque chose vous vient, notez-le au "
         "lieu de le retenir. Une pensée écrite cesse de se répéter."),
        ("Même heure de lever, week-end compris.", "L'heure du lever règle le "
         "rythme plus fortement que l'heure du coucher. Deux heures de grasse "
         "matinée le dimanche vous coûtent le dimanche soir."),
    ],

    "faq": [
        ("Je m'endors pendant l'exercice. C'est mauvais ?",
         "Non, le soir c'est exactement le but. Si vous vous endormez en journée, "
         "faites l'exercice assise plutôt qu'allongée."),
        ("Est-ce que cela aide en cas de trouble du sommeil ?",
         "Ce fichier est une routine du soir, pas un traitement. Si vous ne dormez "
         "presque plus depuis des semaines, cela relève d'un avis médical — il "
         "existe des approches efficaces, et un PDF n'en est pas une."),
        ("Combien de temps avant de sentir une différence ?",
         "Pour l'endormissement, beaucoup remarquent quelque chose dès la première "
         "semaine. Pour les réveils nocturnes, c'est en général plus long, parce "
         "qu'il n'y a pas que le souffle qui joue."),
    ],
}

# ===========================================================================
# ETAPE 6 — BONUS 1
# ===========================================================================

S6 = {
    "badge": "Bonus 1",
    "titel": "Le froid sans glace",
    "lead": ("Le petit amplificateur — de l'eau froide sur les poignets, sur le "
             "visage, à la fin de la douche. Facultatif, en trente secondes, et "
             "jamais en même temps que les exercices de respiration."),
    "foto": "handgelenk",
    "dourado": True,

    "warum_titel": "Pourquoi le froid — et pourquoi ce n'est pas l'essentiel",
    "warum_sub": "Ce fichier est un bonus, et c'est à prendre au pied de la lettre.",
    "warum": [
        "L'eau froide sur le visage et les poignets déclenche une réaction très "
        "ancienne et très rapide : le pouls descend, l'attention saute de la pensée "
        "vers le corps. Cela se produit en quelques secondes et sans que vous ayez "
        "quoi que ce soit à réussir.",
        "C'est précisément ce qui fait du froid un bon <b>ouvre-porte</b> les jours "
        "où vous êtes trop remontée pour vous asseoir et compter. D'abord l'eau "
        "froide, ensuite l'ancre du souffle — dans cet ordre.",
        "<b>Et maintenant la partie honnête :</b> le froid n'est pas la raison pour "
        "laquelle tout cela fonctionne. C'est le souffle. S'il fallait choisir entre "
        "les deux, vous prenez le souffle, tous les jours.",
        "Vous n'avez besoin <b>d'aucune glace</b>, d'aucun bac, d'aucune baignoire "
        "et d'aucun stage. Un robinet suffit.",
    ],

    "regeln_titel": "Les règles — à lire avant le premier exercice",
    "regeln_sub": "Cette page est la raison pour laquelle ce bonus est si court.",
    "regeln": [
        "<b>Jamais respiration et froid en même temps.</b> D'abord l'un, puis "
        "l'autre, avec quelques minutes entre les deux. Jamais combinés.",
        "<b>Ne bloquez jamais la respiration pendant que vous êtes dans l'eau "
        "froide.</b> Ni brièvement ni longuement, ni sous la douche ni au lavabo.",
        "<b>Jamais dans une baignoire, une piscine, un lac ou une rivière.</b> Même "
        "peu profond. Même accompagnée. Qui entre dans l'eau froide après des "
        "exercices de respiration peut perdre connaissance sans prévenir — et cela "
        "arrive aussi à des gens qui nagent bien.",
        "<b>Pas plus de trente secondes.</b> Au-delà, cela n'apporte rien et "
        "transforme un petit exercice en compétition.",
        "<b>Pas de départ brutal.</b> Ne commencez pas par la tête ni par la "
        "poitrine — toujours par les mains.",
    ],
    "regeln_wer": (
        "<b>Sautez ce bonus entièrement</b> si vous avez une maladie cardiaque ou "
        "de l'hypertension, si vous êtes enceinte, si vous souffrez d'un syndrome "
        "de Raynaud ou d'une allergie au froid, ou si vous avez le moindre doute. "
        "Ce bonus est la seule partie du lot que vous pouvez supprimer "
        "complètement sans rien perdre."
    ),

    "uebungen": [
        {
            "tag": "Niveau 1",
            "nome": "De l'eau froide sur les poignets",
            "hook": "La plus petite dose qui existe, et le bon départ pour tout le monde.",
            "foto": "handgelenk",
            "stats": [("20 s", "Durée"), ("Lavabo", "Lieu"), ("Froide", "Pas glacée")],
            "ritmo": None,
            "schritte": [
                "Ouvrez le robinet sur <b>froid</b>. Pas de glace, pas de glaçons — "
                "l'eau du robinet suffit largement.",
                "Tenez le <b>poignet gauche</b> sous le filet, face interne vers le "
                "haut, pendant dix secondes.",
                "Puis le <b>droit</b>, dix secondes également.",
                "<b>Continuez à respirer normalement.</b> Pas de blocage, pas de "
                "halètement, pas de comptage. Si vous bloquez malgré vous, l'eau est "
                "trop froide pour vous.",
                "Séchez. C'est fini. Ensuite vous pouvez vous asseoir et faire deux "
                "minutes d'ancre du souffle — elle passe mieux maintenant.",
            ],
            "worauf": ("Une inspiration brève et vive au premier contact est "
                       "normale. Ensuite, le souffle devrait se calmer de lui-même "
                       "en deux ou trois respirations. Si ce n'est pas le cas, "
                       "arrêtez."),
            "sicher": ("Uniquement au lavabo. Pas au-dessus d'une baignoire, pas "
                       "dans la baignoire, et jamais en bloquant la respiration."),
        },
        {
            "tag": "Niveau 2",
            "nome": "Le linge froid sur le visage",
            "hook": ("La variante la plus forte au lavabo — et celle qui agit le "
                     "plus vite dans un moment de tension."),
            "foto": "gesichtstuch",
            "stats": [("20 s", "Durée"), ("Assise", "Posture"), ("Gant", "Outil")],
            "ritmo": None,
            "schritte": [
                "Mouillez un <b>gant de toilette à l'eau froide</b> et essorez-le "
                "légèrement. <b>Asseyez-vous</b> avant de continuer.",
                "Posez le linge sur le <b>front, les yeux et les pommettes</b>. C'est "
                "cette zone qui compte — pas la bouche ni la gorge.",
                "<b>Continuez à respirer tout à fait normalement</b> et surtout ne "
                "bloquez pas. Vingt secondes, pas plus.",
                "Retirez le linge, séchez-vous le visage, restez assise un moment.",
                "Ensuite l'ancre du souffle <b>4–6</b>, douze respirations.",
            ],
            "worauf": ("Beaucoup remarquent que la tête devient « vide » pendant "
                       "quelques secondes. C'est exactement cette fenêtre que vous "
                       "utilisez pour l'exercice de respiration — c'est pour cela "
                       "qu'il vient juste après."),
            "sicher": ("Assise, jamais penchée au-dessus d'un lavabo plein, et jamais "
                       "en bloquant la respiration. À supprimer entièrement en cas de "
                       "maladie cardiaque."),
        },
        {
            "tag": "Niveau 3",
            "nome": "Les vingt dernières secondes de la douche",
            "hook": ("Pour celles qui ont fait les deux premiers niveaux sans "
                     "problème pendant une semaine."),
            "foto": "dusche",
            "stats": [("20 s", "Durée"), ("À la fin", "Quand"), ("Pieds d'abord", "Ordre")],
            "ritmo": None,
            "schritte": [
                "Douchez-vous chaud tout à fait normalement. Ceci se passe <b>à la "
                "fin</b>, pas au début.",
                "Passez au froid et commencez par les <b>pieds</b>. Puis les mollets, "
                "puis les mains et les avant-bras.",
                "Ensuite le <b>dos et la nuque</b>. La tête est facultative et n'est "
                "pas un objectif.",
                "<b>Continuez à respirer, à voix haute et calmement</b> — une "
                "expiration longue et audible aide ici plus que tout le reste. Pas de "
                "blocage.",
                "Vingt secondes. Sortez, séchez-vous bien, habillez-vous chaudement.",
            ],
            "worauf": ("Si vous tremblez après, c'était trop long ou trop froid. Le "
                       "but est d'être réveillée et bien irriguée, pas glacée."),
            "sicher": ("Tenez-vous bien, accrochez-vous si la baignoire glisse. Pas "
                       "en cas de problèmes circulatoires. Celle qui voit noir en se "
                       "levant régulièrement saute le niveau 3."),
        },
    ],

    "woche_titel": "Une semaine de montée",
    "woche_sub": "Si vous faites ce bonus, faites-le ainsi — et pas plus vite.",
    "woche_tage": [
        (1, "Poignets, 10 secondes", "Seulement les mains, seulement brièvement."),
        (2, "Poignets, 20 secondes", "Même exercice, un peu plus longtemps."),
        (3, "Poignets plus visage avec les mains", "De l'eau froide deux fois sur "
            "le visage, debout au lavabo."),
        (4, "Le linge froid, 10 secondes", "Assise, pour la première fois."),
        (5, "Le linge froid, 20 secondes", "Puis directement l'ancre du souffle."),
        (6, "Pause", "Exprès. Un jour sans froid fait partie du programme."),
        (7, "Votre choix", "Le niveau qui vous a fait le plus de bien. Le niveau 3 "
            "seulement la semaine suivante."),
    ],
}

# ===========================================================================
# ETAPE 7 — BONUS 2
# ===========================================================================

S7 = {
    "badge": "Bonus 2",
    "titel": "Votre carnet de calme",
    "lead": ("Des fiches à imprimer. Au bout de trois semaines, vous voyez noir "
             "sur blanc ce qui a changé — et ce qui vous fait monter à chaque "
             "fois."),
    "foto": "tagebuch",
    "dourado": True,

    "warum_titel": "Pourquoi écrire",
    "warum_sub": "Deux raisons, et la seconde est la plus importante.",
    "warum": [
        "<b>Premièrement : la mémoire ment.</b> Le jour où vous allez mal, votre tête "
        "vous affirme avec une conviction totale que c'est « toujours » comme ça et "
        "que ça n'ira « jamais » mieux. Une feuille avec quatorze croix et trois "
        "bonnes soirées notées dit le contraire.",
        "<b>Deuxièmement : on ne voit les schémas que de l'extérieur.</b> Presque "
        "tout le monde a deux ou trois déclencheurs fiables — une heure précise, une "
        "personne précise, un lieu précis, trop peu de sommeil, trop de café, un "
        "estomac vide. Tant que cela reste dans la tête, c'est du brouillard. Dès que "
        "c'est écrit cinq fois sur la même feuille, c'est une information.",
        "Et avec une information, on peut faire quelque chose : déplacer le "
        "rendez-vous, respirer avant, sauter le quatrième café.",
    ],

    "wie_titel": "Comment l'utiliser",
    "wie_sub": "Deux minutes le soir. Rien de plus n'est prévu.",
    "wie": [
        "<b>Imprimez les fiches</b> — trois feuilles de semaine et une feuille de "
        "déclencheurs. Une feuille par semaine suffit.",
        "<b>Le soir, juste après l'ancre du soir</b>, vous faites votre croix et "
        "remplissez les trois courtes colonnes. Si cela vous prend plus de deux "
        "minutes, vous écrivez trop.",
        "<b>Des chiffres plutôt que des mots, quand c'est possible.</b> « Tension "
        "aujourd'hui : 6 » est comparable. « C'était un peu fatigant » ne l'est pas.",
        "<b>Le déclencheur ne va sur la deuxième feuille que s'il s'est vraiment "
        "passé quelque chose.</b> Les jours calmes, elle reste vide, et c'est bon "
        "signe, pas un oubli.",
        "<b>À la fin de la semaine 3</b>, posez les trois feuilles côte à côte et "
        "lisez-les d'un trait. C'est le jour 21 du plan, et c'est le moment pour "
        "lequel tout ce carnet existe.",
    ],
    "wie_merk": ("Une échelle de 0 à 10 paraît arbitraire, et elle l'est. Elle doit "
                 "seulement rester la même <b>pour vous</b> — alors elle mesure une "
                 "évolution, et c'est tout ce qu'on lui demande."),

    "wochen_titel": "Feuille de semaine",
    "wochen_sub": ("Une ligne par jour. Tension de 0 à 10, où 0 est parfaitement "
                   "calme et 10 le pire état que vous connaissez."),
    "wochen_spalten": ["Jour", "Fait", "Tension 0–10", "Sommeil (h)",
                       "Une phrase sur la journée"],

    "ausloeser_titel": "La feuille des déclencheurs",
    "ausloeser_sub": ("À ne remplir que s'il s'est vraiment passé quelque chose. "
                      "Ici, les lignes vides sont une bonne nouvelle."),
    "ausloeser_spalten": ["Quand", "Où / avec qui", "Intensité 0–10",
                          "Ce que j'ai fait", "Est-ce que ça a aidé ?"],

    "abend_titel": "Les trois questions du soir",
    "abend_sub": ("Si la feuille de semaine vous paraît trop sèche, prenez "
                  "plutôt ces trois questions. Trois lignes, à la main."),
    "abend_fragen": [
        ("Quand ai-je été la plus tendue aujourd'hui ?",
         "L'heure et la situation suffisent. Pas d'explication, pas de jugement."),
        ("Qu'est-ce qui a aidé aujourd'hui — ne serait-ce que deux minutes ?",
         "Les petites choses comptent aussi : une fenêtre ouverte, une marche, un "
         "appel, l'ancre du souffle avant le rendez-vous."),
        ("Qu'est-ce que je me propose pour demain — une seule chose ?",
         "Une. La plus petite qui vous vienne. Les grandes résolutions du soir "
         "sont annulées le matin."),
    ],

    "ende_titel": "Ce que vous verrez au bout de 21 jours",
    "ende_sub": "Quatre choses que presque tout le monde retrouve dans ses feuilles.",
    "ende": [
        "<b>Que ça oscille.</b> Aucune courbe ne descend proprement. Il y a de bonnes "
        "semaines avec une mauvaise journée dedans, et c'est le cas normal — pas "
        "l'échec.",
        "<b>Que les pics raccourcissent avant de se raréfier.</b> En général, ce qui "
        "change d'abord, c'est la durée d'un état, et seulement plus tard sa "
        "fréquence.",
        "<b>Que le sommeil explique presque tout.</b> En posant vos valeurs de "
        "tension à côté des heures de sommeil, beaucoup de gens voient là leur lien "
        "le plus fort — plus net que n'importe quel autre déclencheur.",
        "<b>Que vous avez pratiqué plus de jours que vous ne l'auriez cru.</b> La "
        "tête se souvient des trous. La feuille se souvient des croix.",
    ],
    "ende_schluss": (
        "Si vous voulez arrêter après trois semaines, arrêtez. Si vous voulez "
        "continuer, vous n'avez besoin de rien de nouveau — deux fois deux minutes "
        "par jour et cette feuille une fois par semaine suffisent sur la durée. "
        "<b>Et si vos valeurs restent hautes pendant des semaines alors que vous "
        "pratiquez, ce n'est pas une raison de forcer davantage — c'est le moment "
        "où quelqu'un du métier devrait y jeter un œil.</b>"
    ),
}
