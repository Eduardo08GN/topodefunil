# -*- coding: utf-8 -*-
"""30 receitas de VITAMINAS, SUCOS E CHÁS DETOX (121-150). FRANCÊS. Sem açúcar.

Tradução literal de `receitas_suco.py`. Convenções em GLOSSARIO-TRADUCAO.md.
⛔ O campo `prompt` não é replicado: a foto é a mesma do PT (fotos/121-150).
- Sucos e vitaminas (têm caloria): porcoes8 (8 entradas).
  Metas (kcal): 90/110/130/150 · 130/150/170/190.
- Chás e águas detox (≈ zero caloria): `livre: True` -> a faixa "Boisson libre"
  entra no lugar da tabela e a receita NÃO tem porcoes8, como no PT.
"""

# porção padrão para sucos (metas 90/110/130/150 · 130/150/170/190)
P = ["1 verre (200 ml)", "1 verre (250 ml)", "1 grand verre (300 ml)", "1 grand verre · ½ fruit",
     "1 grand verre (300 ml)", "1 grand verre (350 ml)", "1 grand verre · ½ fruit", "2 verres ou 1 fruit en plus"]
# porção padrão para vitaminas (mais encorpadas, dá para somar aveia)
V = ["1 verre (200 ml)", "1 verre (250 ml)", "1 grand verre (300 ml)", "1 verre · 1 c. à s. d'avoine",
     "1 grand verre (300 ml)", "1 grand verre (350 ml)", "1 grand verre · 1 c. à s. d'avoine", "1 grand verre · 2 c. à s. d'avoine"]

RECEITAS = [
# ---------------- SUCOS DETOX (121-130) ----------------
{
 "nome": "Jus vert détox",
 "hook": "Le classique détox du matin : léger, rafraîchissant et plein de chlorophylle pour donner un coup de pouce à l'organisme.",
 "tempo": "5 min", "rende": "1 grand verre", "kcal_base": 90,
 "ings": ["1 feuille de chou kale (ou 1 poignée d'épinards)", "1 pomme verte en morceaux", "le jus de ½ citron",
          "1 petit morceau de gingembre", "200 ml d'eau glacée", "glaçons au goût"],
 "passos": [
   "Lave bien le chou kale et la pomme. Retire la grosse tige du chou.",
   "Mets le tout dans le mixeur avec l'eau glacée et mixe à pleine puissance pendant 1 minute, jusqu'à ce que ce soit bien liquide.",
   "Si tu le préfères sans morceaux, filtre avec une passoire fine. Sers tout de suite, avec des glaçons."],
 "porcoes8": P,
 "dica": "Les feuilles vertes contiennent beaucoup de fibres et d'eau pour très peu de calories, elles aident à dégonfler et à se sentir rassasié. Le boire avant le petit-déjeuner hydrate et prépare le corps pour la journée. Sans sucre, c'est l'une des boissons les plus légères qui soient.",
},
{
 "nome": "Jus de concombre, citron et menthe",
 "hook": "De la fraîcheur pure dans un verre — le concombre rafraîchit, le citron réveille et la menthe parfume. Une hydratation qui aide à dégonfler.",
 "tempo": "5 min", "rende": "1 grand verre", "kcal_base": 70,
 "ings": ["½ concombre en morceaux", "le jus de 1 citron", "5 feuilles de menthe", "250 ml d'eau glacée", "glaçons au goût"],
 "passos": [
   "Lave le concombre et coupe-le en morceaux (tu peux garder la peau si elle est fine).",
   "Mixe le concombre, le jus de citron, la menthe et l'eau au mixeur pendant 1 minute.",
   "Filtre si tu le veux plus limpide et sers bien frais, avec des glaçons."],
 "porcoes8": P,
 "dica": "Le concombre est presque entièrement composé d'eau et aide à s'hydrater et à réduire la rétention d'eau (cette sensation de gonflement). Avec du citron et de la menthe, ça devient une boisson super rafraîchissante et pratiquement sans calories — excellente à boire tout au long de la journée à la place d'un soda.",
},
{
 "nome": "Jus d'ananas à la menthe et au gingembre",
 "hook": "Sucré, tropical et digestif — l'ananas au gingembre est le jus qui rafraîchit et aide en plus à calmer les inflammations.",
 "tempo": "5 min", "rende": "1 grand verre", "kcal_base": 110,
 "ings": ["2 tranches d'ananas en morceaux", "5 feuilles de menthe", "1 petit morceau de gingembre",
          "200 ml d'eau glacée", "glaçons au goût"],
 "passos": [
   "Coupe l'ananas en morceaux, en retirant l'écorce et le cœur dur du centre.",
   "Mixe l'ananas, la menthe, le gingembre et l'eau au mixeur pendant 1 minute, jusqu'à ce que ce soit homogène.",
   "Filtre si tu veux et sers bien frais, avec des glaçons et une petite feuille de menthe."],
 "porcoes8": P,
 "dica": "L'ananas contient des enzymes qui aident à la digestion et il est riche en eau et en vitamine C. Le gingembre accélère légèrement le métabolisme et calme les inflammations. C'est un jus naturellement sucré, il n'a donc pas besoin de sucre — le fruit fait déjà ce travail.",
},
{
 "nome": "Jus de betterave, carotte et orange",
 "hook": "Rouge éclatant et plein d'énergie — la betterave avec l'orange est un jus qui donne de l'entrain et colore la journée.",
 "tempo": "5 min", "rende": "1 grand verre", "kcal_base": 120,
 "ings": ["½ petite betterave crue en morceaux", "1 carotte en morceaux", "le jus de 2 oranges",
          "100 ml d'eau", "glaçons au goût"],
 "passos": [
   "Épluche la betterave et la carotte et coupe-les en petits morceaux.",
   "Presse les oranges. Mixe la betterave, la carotte, le jus d'orange et l'eau au mixeur pendant 2 minutes, jusqu'à ce que ce soit bien liquide.",
   "Filtre avec une passoire fine (la betterave et la carotte laissent des fibres) et sers frais."],
 "porcoes8": P,
 "dica": "La betterave améliore la circulation et donne de l'énergie, la carotte apporte de la vitamine A et l'orange de la vitamine C. Ensemble, elles forment un jus naturellement sucré et nourrissant. Comme il contient le sucre naturel des fruits et de la betterave, il vaut la peine de respecter la taille du verre.",
},
{
 "nome": "Jus de pastèque au citron",
 "hook": "L'hydratation sous forme de jus : la pastèque est presque entièrement de l'eau, sucrée juste comme il faut et rafraîchissante comme peu d'autres.",
 "tempo": "5 min", "rende": "1 grand verre", "kcal_base": 80,
 "ings": ["2 grandes tranches de pastèque sans écorce", "le jus de ½ citron", "5 feuilles de menthe (facultatif)", "glaçons au goût"],
 "passos": [
   "Coupe la pastèque en dés et retire les plus grosses graines.",
   "Mixe la pastèque avec le jus de citron (et la menthe, si tu veux) au mixeur pendant 30 secondes — la pastèque rend beaucoup d'eau, tu n'as presque pas besoin d'ajouter de liquide.",
   "Sers immédiatement, bien frais, avec des glaçons."],
 "porcoes8": P,
 "dica": "La pastèque contient plus de 90 % d'eau, elle hydrate donc beaucoup et remplit l'estomac pour peu de calories. Elle est naturellement sucrée et rafraîchissante, parfaite pour calmer l'envie de quelque chose de sucré et de glacé quand il fait chaud, sans sortir du régime.",
},
{
 "nome": "Jus de carotte, pomme et gingembre",
 "hook": "Sucré, orangé et avec une touche piquante de gingembre — un jus qui renforce les défenses et réveille le corps.",
 "tempo": "5 min", "rende": "1 grand verre", "kcal_base": 110,
 "ings": ["1 carotte en morceaux", "1 pomme en morceaux", "1 petit morceau de gingembre", "200 ml d'eau", "glaçons au goût"],
 "passos": [
   "Épluche la carotte et coupe la pomme en morceaux, en retirant les pépins.",
   "Mixe la carotte, la pomme, le gingembre et l'eau au mixeur pendant 2 minutes, jusqu'à ce que ce soit bien liquide.",
   "Filtre avec une passoire fine et sers frais."],
 "porcoes8": P,
 "dica": "La carotte et la pomme apportent une douceur naturelle et beaucoup de fibres, tandis que le gingembre donne cette touche stimulante qui aide le métabolisme. C'est un jus renforcé en vitamines, idéal pour commencer la journée avec de l'énergie sans avoir besoin de sucre.",
},
{
 "nome": "Jus vert aux épinards, ananas et concombre",
 "hook": "Vert et sucré à la fois — l'ananas masque les épinards et tu ne remarques même pas que tu bois quelque chose d'aussi sain.",
 "tempo": "5 min", "rende": "1 grand verre", "kcal_base": 100,
 "ings": ["1 poignée d'épinards", "1 tranche d'ananas en morceaux", "½ concombre en morceaux",
          "le jus de ½ citron", "200 ml d'eau glacée", "glaçons au goût"],
 "passos": [
   "Lave bien les épinards et le concombre.",
   "Mixe les épinards, l'ananas, le concombre, le citron et l'eau au mixeur pendant 1 minute, jusqu'à ce que ce soit bien vert et liquide.",
   "Filtre si tu veux et sers frais."],
 "porcoes8": P,
 "dica": "Les épinards sont très riches en fer et en nutriments pour presque aucune calorie, et l'ananas rend le jus sucré et agréable sans sucre. Le concombre hydrate et aide à dégonfler. C'est une façon simple et savoureuse de manger plus de vert.",
},
{
 "nome": "Jus d'orange, carotte et gingembre",
 "hook": "La dose quotidienne de vitamine C dans un verre orangé et lumineux — il renforce les défenses et donne de l'énergie pour la journée.",
 "tempo": "5 min", "rende": "1 grand verre", "kcal_base": 110,
 "ings": ["le jus de 3 oranges", "1 carotte en morceaux", "1 petit morceau de gingembre", "glaçons au goût"],
 "passos": [
   "Presse les oranges pour en extraire le jus.",
   "Épluche la carotte et coupe-la en petits morceaux. Mixe la carotte, le jus d'orange et le gingembre au mixeur pendant 2 minutes.",
   "Filtre avec une passoire fine et sers bien frais, avec des glaçons."],
 "porcoes8": P,
 "dica": "L'orange et la carotte sont pleines de vitamines C et A, et le gingembre donne une touche qui aide la circulation et le métabolisme. C'est un jus énergisant et naturellement sucré — souviens-toi seulement de respecter la portion, puisque le sucre des fruits compte dans les calories.",
},
{
 "nome": "Jus de raisin naturel au citron",
 "hook": "Violet intense et plein d'antioxydants — le raisin devient un jus naturellement sucré qui fait du bien au cœur.",
 "tempo": "5 min", "rende": "1 grand verre", "kcal_base": 120,
 "ings": ["1 petite grappe de raisin noir sans pépins (environ 225 g)", "le jus de ½ citron",
          "150 ml d'eau glacée", "glaçons au goût"],
 "passos": [
   "Lave bien les raisins et détache-les de la grappe.",
   "Mixe les raisins avec le citron et l'eau au mixeur pendant 1 minute, jusqu'à ce qu'ils se défassent.",
   "Filtre avec une passoire fine, en pressant bien pour extraire tout le jus, et sers frais."],
 "porcoes8": P,
 "dica": "Le raisin noir est riche en antioxydants qui protègent le cœur et la peau. Fait sur le moment, sans sucre, le jus de raisin naturel n'a rien à voir avec celui en brique — souviens-toi seulement que le raisin est un fruit très sucré, donc la taille du verre compte.",
},
{
 "nome": "Jus détox pomme, chou kale et céleri",
 "hook": "Ultra-léger et dégonflant — la combinaison verte qui nettoie l'organisme et passe très bien avant les repas.",
 "tempo": "5 min", "rende": "1 grand verre", "kcal_base": 90,
 "ings": ["1 pomme verte en morceaux", "1 feuille de chou kale", "1 branche de céleri", "le jus de ½ citron",
          "200 ml d'eau glacée", "glaçons au goût"],
 "passos": [
   "Lave le chou kale, la pomme et le céleri. Retire la grosse tige du chou.",
   "Mixe la pomme, le chou kale, le céleri, le citron et l'eau au mixeur pendant 1 minute.",
   "Filtre et sers bien frais."],
 "porcoes8": P,
 "dica": "Le céleri est diurétique et aide à éliminer l'excès de liquide, le chou kale apporte des fibres et des nutriments et la pomme sucre naturellement. C'est un jus vert léger et dégonflant, excellent pour accompagner une démarche d'amincissement.",
},
# ---------------- VITAMINAS / SMOOTHIES (131-140) ----------------
{
 "nome": "Smoothie à la banane, avoine et cannelle",
 "hook": "Crémeux et réconfortant, ce smoothie tient toute la matinée — le petit-déjeuner liquide des journées chargées.",
 "tempo": "5 min", "rende": "1 grand verre", "kcal_base": 190,
 "ings": ["1 banane", "2 c. à s. de flocons d'avoine", "200 ml de lait (ou boisson végétale)",
          "1 pincée de cannelle", "glaçons au goût"],
 "passos": [
   "Épluche la banane (plus elle est mûre, plus elle sucre).",
   "Mixe la banane, l'avoine, le lait et la cannelle au mixeur pendant 1 minute, jusqu'à ce que ce soit crémeux.",
   "Sers tout de suite, avec une pincée de cannelle par-dessus. Si tu le veux plus frais, ajoute des glaçons et mixe à nouveau."],
 "porcoes8": V,
 "dica": "La banane avec l'avoine forme un duo qui rassasie des heures grâce aux fibres, et le lait apporte les protéines. C'est un smoothie qui fonctionne comme un repas liquide complet — parfait pour le petit-déjeuner ou le goûter de ceux qui sont pressés, sans avoir besoin de sucre.",
},
{
 "nome": "Smoothie à la fraise et au yaourt",
 "hook": "Rosé et crémeux, avec la douceur naturelle de la fraise — un smoothie qui ressemble à un milk-shake, mais léger et protéiné.",
 "tempo": "5 min", "rende": "1 grand verre", "kcal_base": 150,
 "ings": ["150 g de fraises (fraîches ou surgelées)", "1 pot de yaourt nature sans sucre (environ 170 g)",
          "100 ml de lait (ou d'eau)", "édulcorant au goût (facultatif)", "glaçons au goût"],
 "passos": [
   "Lave les fraises et retire les petites feuilles vertes.",
   "Mixe les fraises, le yaourt et le lait au mixeur pendant 1 minute, jusqu'à obtenir une crème rosée et lisse.",
   "Goûte et, si tu veux, sucre un peu. Sers frais."],
 "porcoes8": V,
 "dica": "Le yaourt nature apporte des protéines et du crémeux sans sucre, et la fraise sucre naturellement pour très peu de calories. C'est un smoothie rassasiant et rafraîchissant qui calme l'envie de milk-shake de façon légère et nourrissante.",
},
{
 "nome": "Smoothie aux fruits rouges",
 "hook": "Violet, antioxydant et plein de goût — un mélange de petits fruits rouges mixé bien crémeux, excellent pour la peau et la satiété.",
 "tempo": "5 min", "rende": "1 grand verre", "kcal_base": 140,
 "ings": ["140 g de fruits rouges mélangés (fraises, myrtilles, framboises)", "1 pot de yaourt nature sans sucre",
          "100 ml de lait (ou d'eau)", "édulcorant au goût (facultatif)", "glaçons au goût"],
 "passos": [
   "Si les fruits sont surgelés, utilise-les directement (le smoothie sera plus froid et plus crémeux).",
   "Mixe les fruits rouges, le yaourt et le lait au mixeur pendant 1 minute, jusqu'à obtenir une crème lisse.",
   "Goûte, sucre si tu veux et sers tout de suite."],
 "porcoes8": V,
 "dica": "Les fruits rouges sont champions en antioxydants, qui luttent contre le vieillissement, et ils contiennent peu de sucre. Avec du yaourt, ils deviennent un smoothie protéiné et crémeux qui rassasie et compte parmi les goûters les plus sains.",
},
{
 "nome": "Smoothie vert à la banane et aux épinards",
 "hook": "Vert dehors, sucré dedans — la banane cache les épinards et livre une boisson crémeuse pleine de nutriments.",
 "tempo": "5 min", "rende": "1 grand verre", "kcal_base": 160,
 "ings": ["1 banane", "1 poignée d'épinards", "½ pomme en morceaux", "200 ml de lait (ou d'eau de coco)",
          "glaçons au goût"],
 "passos": [
   "Lave bien les épinards.",
   "Mixe la banane, les épinards, la pomme et le lait au mixeur pendant 1 minute, jusqu'à ce que ce soit vert et crémeux.",
   "Sers tout de suite, bien frais."],
 "porcoes8": V,
 "dica": "C'est une façon délicieuse de manger plus de feuilles vertes : la banane et la pomme sucrent naturellement et masquent les épinards, qui arrivent pleins de fer et de fibres. Crémeux et rassasiant, il fonctionne comme un petit-déjeuner liquide et nourrissant.",
},
{
 "nome": "Smoothie à l'avocat",
 "hook": "Ultra-crémeux et réconfortant, avec la bonne graisse de l'avocat — un smoothie qui rassasie vraiment et nourrit la peau.",
 "tempo": "5 min", "rende": "1 grand verre", "kcal_base": 190,
 "ings": ["½ avocat mûr", "200 ml de lait (ou boisson végétale)", "édulcorant au goût — ou 1 c. à c. de miel",
          "1 pincée de cannelle ou quelques gouttes de citron", "glaçons au goût"],
 "passos": [
   "Prélève la chair de l'avocat à la cuillère, en n'utilisant que la partie bien tendre.",
   "Mixe l'avocat, le lait et l'édulcorant (ou le miel) au mixeur pendant 1 minute, jusqu'à obtenir une crème lisse et soyeuse.",
   "Sers frais, avec une pincée de cannelle ou quelques gouttes de citron."],
 "porcoes8": V,
 "dica": "L'avocat contient de la bonne graisse qui rassasie beaucoup et fait du bien au cœur et à la peau. Mixé avec du lait, il devient un smoothie crémeux et nourrissant qui tient la faim pendant des heures. Comme il est plus calorique, c'est une excellente option de goûter dans la portion d'un verre.",
},
{
 "nome": "Smoothie à la mangue et au yaourt",
 "hook": "Tropical, doré et crémeux — la mangue devient un smoothie sucré qui ressemble à un dessert et rafraîchit sur-le-champ.",
 "tempo": "5 min", "rende": "1 grand verre", "kcal_base": 150,
 "ings": ["1 mangue mûre en dés (ou 165 g surgelée)", "1 pot de yaourt nature sans sucre",
          "100 ml de lait (ou d'eau)", "glaçons au goût"],
 "passos": [
   "Épluche la mangue et coupe la chair en dés.",
   "Mixe la mangue, le yaourt et le lait au mixeur pendant 1 minute, jusqu'à obtenir une crème dorée et lisse.",
   "Sers bien frais."],
 "porcoes8": V,
 "dica": "La mangue est naturellement sucrée et pleine de vitamines A et C, ce qui rend le sucre inutile. Avec du yaourt, le smoothie gagne des protéines et du crémeux et devient un goûter rafraîchissant et rassasiant — respecte seulement la portion, puisque la mangue est un fruit sucré.",
},
{
 "nome": "Smoothie à la poire et à l'avoine",
 "hook": "Doux et délicat, la poire apporte une légère douceur à l'avoine crémeuse — un smoothie calme et réconfortant.",
 "tempo": "5 min", "rende": "1 grand verre", "kcal_base": 170,
 "ings": ["1 poire mûre en morceaux", "2 c. à s. de flocons d'avoine", "200 ml de lait (ou boisson végétale)",
          "1 pincée de cannelle", "glaçons au goût"],
 "passos": [
   "Lave la poire et coupe-la en morceaux, en retirant le cœur avec les pépins.",
   "Mixe la poire, l'avoine, le lait et la cannelle au mixeur pendant 1 minute, jusqu'à ce que ce soit crémeux.",
   "Sers tout de suite, avec une pincée de cannelle par-dessus."],
 "porcoes8": V,
 "dica": "La poire est un fruit doux et plein de fibres, et avec l'avoine elle forme un smoothie qui rassasie longtemps. Le lait ajoute les protéines. C'est une boisson légère et réconfortante, excellente pour le petit-déjeuner ou pour un goûter qui tient la faim.",
},
{
 "nome": "Smoothie à la banane et au cacao",
 "hook": "Le goût du chocolat dans un smoothie crémeux et sans sucre — la solution parfaite pour l'envie de sucré de l'après-midi.",
 "tempo": "5 min", "rende": "1 grand verre", "kcal_base": 180,
 "ings": ["1 banane", "1 c. à s. de cacao en poudre 100 %", "200 ml de lait (ou boisson végétale)",
          "1 c. à c. de beurre de cacahuète (facultatif)", "glaçons au goût"],
 "passos": [
   "Épluche la banane (plus elle est mûre, plus elle sucre).",
   "Mixe la banane, le cacao, le lait et le beurre de cacahuète au mixeur pendant 1 minute, jusqu'à obtenir une crème chocolatée et lisse.",
   "Sers bien frais, avec des glaçons."],
 "porcoes8": V,
 "dica": "Le cacao pur donne le goût du chocolat sans sucre, et la banane sucre et rend le smoothie crémeux. C'est la façon la plus agréable de calmer l'envie de chocolat de l'après-midi de manière nourrissante, avec les fibres du fruit et les protéines du lait.",
},
{
 "nome": "Smoothie à la pomme, cannelle et avoine",
 "hook": "Le goût d'une tarte aux pommes dans un verre crémeux — de l'avoine, de la pomme et de la cannelle mixées en un goûter qui réconforte.",
 "tempo": "5 min", "rende": "1 grand verre", "kcal_base": 170,
 "ings": ["1 pomme en morceaux", "2 c. à s. de flocons d'avoine", "200 ml de lait (ou boisson végétale)",
          "1 c. à c. de cannelle", "glaçons au goût"],
 "passos": [
   "Coupe la pomme en morceaux, en retirant les pépins (tu peux garder la peau).",
   "Mixe la pomme, l'avoine, le lait et la cannelle au mixeur pendant 1 minute et demie, jusqu'à ce que ce soit crémeux et que la pomme soit bien défaite.",
   "Sers tout de suite, avec encore un peu de cannelle par-dessus."],
 "porcoes8": V,
 "dica": "Pomme, cannelle et avoine rappellent un dessert, mais ensemble elles donnent un smoothie plein de fibres qui rassasie des heures. La cannelle aide à contrôler l'envie de sucré. C'est un goûter crémeux, savoureux et léger, sans aucun sucre ajouté.",
},
{
 "nome": "Smoothie au melon et à la menthe",
 "hook": "Vert clair, sucré et ultra-rafraîchissant — le melon à la menthe, c'est de l'hydratation pure dans un smoothie léger.",
 "tempo": "5 min", "rende": "1 grand verre", "kcal_base": 110,
 "ings": ["3 tranches de melon sans écorce, en dés", "5 feuilles de menthe", "½ pot de yaourt nature (ou 100 ml d'eau)",
          "glaçons au goût"],
 "passos": [
   "Coupe le melon en dés, en retirant les graines.",
   "Mixe le melon, la menthe et le yaourt (ou l'eau) au mixeur pendant 1 minute, jusqu'à ce que ce soit lisse.",
   "Sers bien frais, avec une petite feuille de menthe."],
 "porcoes8": V,
 "dica": "Le melon est riche en eau et aide à s'hydrater et à dégonfler, pour très peu de calories. Mixé avec de la menthe, il est rafraîchissant et léger ; avec un peu de yaourt, il gagne du crémeux et des protéines. Un smoothie parfait pour les jours chauds.",
},
# ---------------- ÁGUAS DETOX (141-144) — LIVRES ----------------
{
 "nome": "Eau détox au concombre, citron et menthe",
 "hook": "L'eau qui donne envie d'être bue : légère, parfumée et rafraîchissante, pour s'hydrater toute la journée sans s'en lasser.",
 "tempo": "5 min + réfrigérateur", "rende": "1 carafe", "kcal_base": 10, "livre": True,
 "ings": ["1 litre d'eau", "½ concombre en fines rondelles", "½ citron en rondelles", "6 feuilles de menthe", "glaçons au goût"],
 "passos": [
   "Lave le concombre, le citron et la menthe.",
   "Dans une carafe, mets l'eau, les rondelles de concombre et de citron et les feuilles de menthe.",
   "Mets au réfrigérateur au moins 1 heure, pour que l'eau prenne le goût. Sers frais tout au long de la journée ; tu peux rajouter de l'eau au fur et à mesure que tu bois."],
 "dica": "Remplacer les sodas et les jus sucrés par de l'eau aromatisée est l'une des habitudes qui aident le plus à maigrir. Le concombre, le citron et la menthe donnent du goût sans calories, rendent l'eau plus agréable et t'aident à rester bien hydraté toute la journée.",
},
{
 "nome": "Eau détox au gingembre et au citron",
 "hook": "Une eau tiède ou glacée avec une touche piquante qui réveille le métabolisme dès le matin.",
 "tempo": "5 min", "rende": "1 verre", "kcal_base": 8, "livre": True,
 "ings": ["1 verre d'eau (tiède ou glacée)", "le jus de ½ citron", "quelques fines lamelles de gingembre", "glaçons au goût (si glacée)"],
 "passos": [
   "Coupe le gingembre en lamelles très fines.",
   "Mélange l'eau, le jus de citron et le gingembre dans un verre.",
   "Laisse reposer 5 minutes pour que le gingembre libère son goût. Bois le matin, à jeun, tiède ou glacée."],
 "dica": "Boire de l'eau au citron et au gingembre à jeun aide à réveiller l'organisme et la digestion. Le gingembre a un léger effet stimulant (il accélère un peu le métabolisme). Sans sucre, c'est un rituel matinal simple qui soutient l'amincissement.",
},
{
 "nome": "Eau détox aux fruits rouges",
 "hook": "Rosée et jolie dans la carafe, avec des petits fruits qui flottent — une eau aromatisée qui a des airs de boisson de spa.",
 "tempo": "5 min + réfrigérateur", "rende": "1 carafe", "kcal_base": 15, "livre": True,
 "ings": ["1 litre d'eau", "1 poignée de fruits rouges (fraises, myrtilles, framboises)", "½ citron en rondelles",
          "feuilles de menthe", "glaçons au goût"],
 "passos": [
   "Lave les fruits rouges et coupe les fraises en deux.",
   "Dans une carafe, mets l'eau, les fruits, les rondelles de citron et la menthe. Écrase légèrement les fruits avec une cuillère pour qu'ils libèrent leur couleur et leur goût.",
   "Mets au réfrigérateur 1 à 2 heures et sers bien frais."],
 "dica": "Les fruits rouges donnent de la couleur, du goût et des antioxydants à l'eau pour presque aucune calorie. C'est une façon jolie et agréable de boire plus d'eau au fil de la journée, en remplaçant les boissons sucrées et en aidant à l'hydratation et à l'amincissement.",
},
{
 "nome": "Eau de coco au citron et à la menthe",
 "hook": "L'hydratation naturelle de l'eau de coco, relevée au citron et à la menthe — rafraîchissante et pleine de minéraux.",
 "tempo": "3 min", "rende": "1 grand verre", "kcal_base": 45, "livre": True,
 "ings": ["1 grand verre d'eau de coco", "le jus de ½ citron", "5 feuilles de menthe", "glaçons au goût"],
 "passos": [
   "Mélange l'eau de coco avec le jus de citron dans un verre.",
   "Ajoute les feuilles de menthe et les glaçons et remue.",
   "Sers bien frais, de préférence avec de l'eau de coco naturelle (celle en brique contient souvent du sucre ajouté — préfère la naturelle)."],
 "dica": "L'eau de coco reconstitue les minéraux et hydrate très bien, avec peu de calories quand elle est naturelle. Avec du citron et de la menthe, elle devient encore plus rafraîchissante. Elle est excellente après une activité physique ou les jours chauds, à la place des boissons sportives sucrées.",
},
# ---------------- CHÁS / INFUSÕES (145-150) — LIVRES ----------------
{
 "nome": "Thé vert au citron et au gingembre",
 "hook": "L'allié numéro 1 de qui veut maigrir : le thé vert accélère le métabolisme, et le citron et le gingembre donnent un coup de pouce supplémentaire.",
 "tempo": "8 min", "rende": "1 tasse", "kcal_base": 5, "livre": True,
 "ings": ["240 ml d'eau", "1 c. à c. de thé vert (ou 1 sachet)", "quelques lamelles de gingembre", "le jus de ½ citron"],
 "passos": [
   "Fais bouillir l'eau et retire du feu. Attends 1 minute (une eau trop chaude rend le thé vert amer).",
   "Ajoute le thé vert et les lamelles de gingembre, couvre et laisse infuser à couvert 3 minutes.",
   "Filtre, ajoute le jus de citron et bois tiède. Tu peux aussi le boire glacé, tout au long de la journée."],
 "dica": "Le thé vert est l'un des aliments les plus étudiés pour l'amincissement : il contient des substances qui aident à accélérer le métabolisme et à brûler les graisses. Avec du gingembre et du citron, l'effet est renforcé. Sans sucre, c'est une boisson libre que tu peux boire tous les jours.",
},
{
 "nome": "Thé d'hibiscus glacé",
 "hook": "Rouge rubis et légèrement acidulé, l'hibiscus est réputé pour aider à dégonfler — délicieux glacé quand il fait chaud.",
 "tempo": "10 min + réfrigérateur", "rende": "1 carafe", "kcal_base": 5, "livre": True,
 "ings": ["1 litre d'eau", "2 c. à s. de fleurs d'hibiscus séchées (ou 2 sachets)",
          "rondelles de citron", "feuilles de menthe", "glaçons au goût"],
 "passos": [
   "Fais bouillir l'eau et retire du feu. Ajoute l'hibiscus, couvre et laisse infuser à couvert 5 à 7 minutes.",
   "Filtre et laisse refroidir. Mets au réfrigérateur.",
   "Sers bien frais, avec des rondelles de citron, de la menthe et des glaçons."],
 "dica": "Le thé d'hibiscus est connu pour aider à réduire la rétention d'eau (le gonflement) et il est riche en antioxydants. Glacé et sans sucre, c'est une boisson rafraîchissante et libre, excellente pour remplacer les sodas et les jus industriels au fil de la journée.",
},
{
 "nome": "Tisane de camomille à la cannelle",
 "hook": "Chaude et réconfortante, la tisane qui apaise avant de dormir — et une bonne nuit de sommeil aide aussi à maigrir.",
 "tempo": "8 min", "rende": "1 tasse", "kcal_base": 5, "livre": True,
 "ings": ["240 ml d'eau", "1 c. à s. de fleurs de camomille (ou 1 sachet)", "1 bâton de cannelle (ou 1 pincée en poudre)"],
 "passos": [
   "Fais bouillir l'eau et retire du feu.",
   "Ajoute la camomille et la cannelle, couvre et laisse infuser à couvert 5 minutes.",
   "Filtre et bois tiède, de préférence le soir, avant d'aller dormir."],
 "dica": "La camomille apaise et aide à se détendre, ce qui améliore le sommeil. Bien dormir est un facteur que beaucoup oublient dans l'amincissement : des nuits mal dormies augmentent la faim et l'envie de sucré le lendemain. Cette tisane est un rituel du soir qui soutient le régime.",
},
{
 "nome": "Infusion de gingembre, citron et cannelle",
 "hook": "Une infusion stimulante et parfumée qui réchauffe le corps et donne ce coup de pouce au métabolisme.",
 "tempo": "10 min", "rende": "1 grande tasse", "kcal_base": 8, "livre": True,
 "ings": ["300 ml d'eau", "plusieurs lamelles de gingembre", "1 bâton de cannelle", "le jus de ½ citron"],
 "passos": [
   "Dans une petite casserole, fais bouillir l'eau avec les lamelles de gingembre et le bâton de cannelle 5 minutes, à feu doux.",
   "Retire du feu, couvre et laisse infuser encore 3 minutes.",
   "Filtre, ajoute le jus de citron et bois tiède."],
 "dica": "Le gingembre et la cannelle ont un léger effet stimulant, c'est-à-dire qu'ils aident le corps à dépenser un peu plus d'énergie. C'est une infusion chaude et réconfortante, sans sucre, qui fait du bien les jours froids et donne ce soutien supplémentaire au métabolisme.",
},
{
 "nome": "Tisane de menthe au citron",
 "hook": "Fraîche et digestive, la tisane de menthe apaise l'estomac après les repas — légère et parfumée.",
 "tempo": "8 min", "rende": "1 tasse", "kcal_base": 4, "livre": True,
 "ings": ["240 ml d'eau", "1 poignée de feuilles de menthe fraîche (ou 1 sachet)", "le jus de ½ citron"],
 "passos": [
   "Fais bouillir l'eau et retire du feu.",
   "Ajoute les feuilles de menthe, couvre et laisse infuser à couvert 5 minutes.",
   "Filtre, ajoute le jus de citron et bois tiède ou glacé, de préférence après les repas."],
 "dica": "La menthe aide à la digestion et réduit cette sensation d'estomac lourd après avoir mangé. Une tisane digestive et sans sucre après les repas est une habitude simple qui aide à éviter de grignoter du sucré juste après.",
},
{
 "nome": "Tisane de fenouil",
 "hook": "Douce et naturellement sucrée, le fenouil apaise l'estomac et réduit les ballonnements — une tisane réconfortante après le repas.",
 "tempo": "8 min", "rende": "1 tasse", "kcal_base": 4, "livre": True,
 "ings": ["240 ml d'eau", "1 c. à c. de graines de fenouil — ou 1 sachet"],
 "passos": [
   "Écrase légèrement les graines de fenouil (elles libèrent ainsi plus d'arôme).",
   "Fais bouillir l'eau et retire du feu. Ajoute le fenouil, couvre et laisse infuser à couvert 5 minutes.",
   "Filtre et bois tiède, de préférence après les repas ou le soir."],
 "dica": "Le fenouil est connu pour apaiser l'estomac et réduire les gaz et le ventre gonflé. Naturellement sucré, il se passe de sucre. C'est une tisane digestive et réconfortante, excellente pour clore un repas en douceur.",
},
]
