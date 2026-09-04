# -*- coding: utf-8 -*-
"""30 receitas de VITAMINAS, SUCOS E CHÁS DETOX (121-150). INGLÊS (mercado US). Sem açúcar.

Tradução literal de `receitas_suco.py`. Convenções em GLOSSARIO-TRADUCAO.md:
tratamento por "you", volume de copo em OZ (o americano não mede bebida em ml),
1 litro = 4 cups.
⛔ A flag `livre` é PARIDADE COM O PT, nunca escolha: as 4 águas detox e os 6
chás não têm `porcoes8` lá e não podem ter aqui — a lente compara os dois.
⛔ O campo `prompt` NÃO é replicado aqui: a foto é a mesma do PT (fotos/121-150).
- Sucos e vitaminas (têm caloria): porcoes8 (8 entradas).
  Metas (kcal): 90/110/130/150 · 130/150/170/190.
porcoes8 na ordem: Mulher 120-155/156-185/186-220/220+ lb · Homem 155-185/186-220/221-265/265+ lb
"""

# porção padrão para sucos (metas 90/110/130/150 · 130/150/170/190)
P = ["1 glass (7 oz)", "1 glass (8 oz)", "1 large glass (10 oz)", "1 large glass · 1/2 fruit",
     "1 large glass (10 oz)", "1 large glass (12 oz)", "1 large glass · 1/2 fruit", "2 glasses or 1 extra fruit"]
# porção padrão para vitaminas (mais encorpadas, dá para somar aveia)
V = ["1 glass (7 oz)", "1 glass (8 oz)", "1 large glass (10 oz)", "1 glass · 1 tbsp oats",
     "1 large glass (10 oz)", "1 large glass (12 oz)", "1 large glass · 1 tbsp oats", "1 large glass · 2 tbsp oats"]

RECEITAS = [
# ---------------- SUCOS DETOX (121-130) ----------------
{
 "nome": "Green Detox Juice",
 "hook": "The classic morning detox: light, refreshing and full of chlorophyll to give your body that push.",
 "tempo": "5 min", "rende": "1 large glass", "kcal_base": 90,
 "ings": ["1 kale leaf (or 1 handful of spinach)", "1 green apple in pieces", "juice of 1/2 lemon",
          "1 small piece of ginger", "3/4 cup cold water", "ice to taste"],
 "passos": [
   "Wash the kale and the apple well. Take the thick stem off the kale.",
   "Put everything in the blender with the cold water and blend at top speed for 1 minute, until it is fully liquid.",
   "If you prefer it with no little bits, strain it through a sieve. Serve right away, with ice."],
 "porcoes8": P,
 "dica": "Green leaves have a lot of fiber and water with very few calories, helping to reduce bloating and bring fullness. Drinking it before breakfast hydrates you and gets your body ready for the day. With no sugar, it is one of the lightest drinks there is.",
},
{
 "nome": "Cucumber, Lemon and Mint Juice",
 "hook": "Pure freshness in a glass — the cucumber refreshes, the lemon wakes you up and the mint perfumes it. Hydration that helps reduce bloating.",
 "tempo": "5 min", "rende": "1 large glass", "kcal_base": 70,
 "ings": ["1/2 cucumber in pieces", "juice of 1 lemon", "5 mint leaves", "1 cup cold water", "ice to taste"],
 "passos": [
   "Wash the cucumber and cut it into pieces (you can leave the skin on if it is thin).",
   "Blend the cucumber, the lemon juice, the mint and the water in the blender for 1 minute.",
   "Strain it if you want it cleaner and serve very cold, with ice."],
 "porcoes8": P,
 "dica": "Cucumber is almost all water and helps to hydrate you and reduce water retention (that bloated feeling). With lemon and mint, it becomes a super refreshing drink with practically no calories — great to drink through the day instead of soda.",
},
{
 "nome": "Pineapple Juice with Mint and Ginger",
 "hook": "Sweet, tropical and good for digestion — pineapple with ginger is the juice that refreshes and also helps calm inflammation.",
 "tempo": "5 min", "rende": "1 large glass", "kcal_base": 110,
 "ings": ["2 slices of pineapple in pieces", "5 mint leaves", "1 small piece of ginger",
          "3/4 cup cold water", "ice to taste"],
 "passos": [
   "Cut the pineapple into pieces, taking off the skin and the hard core in the center.",
   "Blend the pineapple, the mint, the ginger and the water in the blender for 1 minute, until it is even.",
   "Strain it if you like and serve very cold, with ice and a mint leaf."],
 "porcoes8": P,
 "dica": "Pineapple has enzymes that help digestion and is rich in water and vitamin C. Ginger slightly speeds up your metabolism and calms inflammation. It is a naturally sweet juice, so it needs no sugar — the fruit already does that job.",
},
{
 "nome": "Beetroot, Carrot and Orange Juice",
 "hook": "Bright red and full of energy — beetroot with orange is a juice that gives you a lift and colors your day.",
 "tempo": "5 min", "rende": "1 large glass", "kcal_base": 120,
 "ings": ["1/2 small raw beetroot in pieces", "1 carrot in pieces", "juice of 2 oranges",
          "1/2 cup water", "ice to taste"],
 "passos": [
   "Peel the beetroot and the carrot and cut them into small pieces.",
   "Squeeze the oranges. Blend the beetroot, the carrot, the orange juice and the water in the blender for 2 minutes, until it is fully liquid.",
   "Strain it through a sieve (beetroot and carrot leave fibers) and serve cold."],
 "porcoes8": P,
 "dica": "Beetroot improves circulation and gives energy, carrot brings vitamin A and orange brings vitamin C. Together, they make a naturally sweet and nourishing juice. Since it has natural sugar from the fruit and the beetroot, it is worth respecting the glass portion.",
},
{
 "nome": "Watermelon Juice with Lemon",
 "hook": "Hydration in juice form: watermelon is almost all water, sweet in just the right measure and as refreshing as it gets.",
 "tempo": "5 min", "rende": "1 large glass", "kcal_base": 80,
 "ings": ["2 large slices of watermelon with no rind", "juice of 1/2 lemon", "5 mint leaves (optional)", "ice to taste"],
 "passos": [
   "Cut the watermelon into cubes and take out the bigger seeds.",
   "Blend the watermelon with the lemon juice (and the mint, if you like) in the blender for 30 seconds — watermelon releases a lot of water, so you barely need to add any liquid.",
   "Serve immediately, very cold, with ice."],
 "porcoes8": P,
 "dica": "Watermelon is more than 90% water, so it hydrates you a lot and fills your stomach with few calories. It is naturally sweet and refreshing, perfect for killing the craving for something sweet and cold in the heat without leaving your diet.",
},
{
 "nome": "Carrot, Apple and Ginger Juice",
 "hook": "Sweet, orange and with a spicy touch of ginger — a juice that strengthens your immune system and wakes your body up.",
 "tempo": "5 min", "rende": "1 large glass", "kcal_base": 110,
 "ings": ["1 carrot in pieces", "1 apple in pieces", "1 small piece of ginger", "3/4 cup water", "ice to taste"],
 "passos": [
   "Peel the carrot and cut the apple into pieces, taking out the seeds.",
   "Blend the carrot, the apple, the ginger and the water in the blender for 2 minutes, until it is fully liquid.",
   "Strain it through a sieve and serve cold."],
 "porcoes8": P,
 "dica": "Carrot and apple bring natural sweetness and plenty of fiber, while ginger gives that thermogenic touch that helps your metabolism. It is a juice loaded with vitamins, ideal for starting the day with energy and no need for sugar.",
},
{
 "nome": "Green Juice with Spinach, Pineapple and Cucumber",
 "hook": "Green and sweet at the same time — the pineapple hides the spinach and you do not even notice you are drinking something so healthy.",
 "tempo": "5 min", "rende": "1 large glass", "kcal_base": 100,
 "ings": ["1 handful of spinach", "1 slice of pineapple in pieces", "1/2 cucumber in pieces",
          "juice of 1/2 lemon", "3/4 cup cold water", "ice to taste"],
 "passos": [
   "Wash the spinach and the cucumber well.",
   "Blend the spinach, the pineapple, the cucumber, the lemon and the water in the blender for 1 minute, until it is nicely green and liquid.",
   "Strain it if you like and serve cold."],
 "porcoes8": P,
 "dica": "Spinach is extremely rich in iron and nutrients with almost no calories, and pineapple makes the juice sweet and tasty with no sugar. Cucumber hydrates and helps reduce bloating. It is an easy and tasty way to eat more greens.",
},
{
 "nome": "Orange Juice with Carrot and Ginger",
 "hook": "Your daily dose of vitamin C in a bright orange glass — it boosts your immune system and gives you energy for the day.",
 "tempo": "5 min", "rende": "1 large glass", "kcal_base": 110,
 "ings": ["juice of 3 oranges", "1 carrot in pieces", "1 small piece of ginger", "ice to taste"],
 "passos": [
   "Squeeze the oranges for the juice.",
   "Peel the carrot and cut it into small pieces. Blend the carrot, the orange juice and the ginger in the blender for 2 minutes.",
   "Strain it through a sieve and serve very cold, with ice."],
 "porcoes8": P,
 "dica": "Orange and carrot are full of vitamin C and A, and ginger adds a touch that helps circulation and metabolism. It is an energizing and naturally sweet juice — just remember to respect the portion, since the sugar in the fruit adds calories.",
},
{
 "nome": "Natural Grape Juice with Lemon",
 "hook": "Deep purple and full of antioxidants — grapes turn into a naturally sweet juice that is good for your heart.",
 "tempo": "5 min", "rende": "1 large glass", "kcal_base": 120,
 "ings": ["1 small bunch of seedless purple grapes (about 1 1/2 cups)", "juice of 1/2 lemon",
          "2/3 cup cold water", "ice to taste"],
 "passos": [
   "Wash the grapes well and take them off the stems.",
   "Blend the grapes with the lemon and the water in the blender for 1 minute, until they break down.",
   "Strain it through a sieve, pressing well to get all the juice out, and serve cold."],
 "porcoes8": P,
 "dica": "Purple grapes are rich in antioxidants that protect your heart and your skin. Made fresh, with no sugar, natural grape juice is very different from the boxed kind — just remember that grapes are a very sweet fruit, so the glass portion matters.",
},
{
 "nome": "Detox Juice with Apple, Kale and Celery",
 "hook": "Extremely light and de-bloating — the green combination that cleans out your system and works very well before meals.",
 "tempo": "5 min", "rende": "1 large glass", "kcal_base": 90,
 "ings": ["1 green apple in pieces", "1 kale leaf", "1 celery stalk", "juice of 1/2 lemon",
          "3/4 cup cold water", "ice to taste"],
 "passos": [
   "Wash the kale, the apple and the celery. Take the thick stem off the kale.",
   "Blend the apple, the kale, the celery, the lemon and the water in the blender for 1 minute.",
   "Strain it and serve very cold."],
 "porcoes8": P,
 "dica": "Celery is a diuretic and helps to get rid of extra fluid, kale brings fiber and nutrients and the apple sweetens naturally. It is a light, de-bloating green juice, great to go with a weight-loss routine.",
},
# ---------------- VITAMINAS / SMOOTHIES (131-140) ----------------
{
 "nome": "Banana Smoothie with Oats and Cinnamon",
 "hook": "Creamy and comforting, this smoothie carries you through the whole morning — the liquid breakfast for busy days.",
 "tempo": "5 min", "rende": "1 large glass", "kcal_base": 190,
 "ings": ["1 banana", "2 tbsp oats", "3/4 cup milk (or plant drink)",
          "1 pinch of cinnamon", "ice to taste"],
 "passos": [
   "Peel the banana (if it is very ripe, it sweetens more).",
   "Blend the banana, the oats, the milk and the cinnamon in the blender for 1 minute, until it is creamy.",
   "Serve right away, with a pinch of cinnamon on top. If you want it colder, add ice and blend again."],
 "porcoes8": V,
 "dica": "Banana with oats is a pair that keeps you full for hours thanks to the fiber, and the milk brings protein. It is a smoothie that works as a complete liquid meal — perfect for breakfast or a snack when you are in a hurry, with no need for sugar.",
},
{
 "nome": "Strawberry Smoothie with Yogurt",
 "hook": "Pink and creamy, with the natural sweetness of strawberries — a smoothie that looks like a milkshake, but is light and full of protein.",
 "tempo": "5 min", "rende": "1 large glass", "kcal_base": 150,
 "ings": ["1 cup of strawberries (fresh or frozen)", "1 cup of plain yogurt with no sugar (about 6 oz)",
          "1/2 cup milk (or water)", "sweetener to taste (optional)", "ice to taste"],
 "passos": [
   "Wash the strawberries and take off the green leaves.",
   "Blend the strawberries, the yogurt and the milk in the blender for 1 minute, until it turns into a smooth, pink cream.",
   "Taste it and, if you like, sweeten it a little. Serve cold."],
 "porcoes8": V,
 "dica": "Plain yogurt brings protein and creaminess with no sugar, and strawberries sweeten naturally with very few calories. It is a filling and refreshing smoothie that kills the craving for a milkshake in a light and nourishing way.",
},
{
 "nome": "Mixed Berry Smoothie",
 "hook": "Purple, full of antioxidants and packed with flavor — a mix of berries blended creamy, great for your skin and for fullness.",
 "tempo": "5 min", "rende": "1 large glass", "kcal_base": 140,
 "ings": ["1 cup of mixed berries (strawberry, blueberry, raspberry)", "1 cup of plain yogurt with no sugar",
          "1/2 cup milk (or water)", "sweetener to taste (optional)", "ice to taste"],
 "passos": [
   "If the berries are frozen, use them straight from the freezer (they make the smoothie colder and creamier).",
   "Blend the berries, the yogurt and the milk in the blender for 1 minute, until it turns into a smooth cream.",
   "Taste it, sweeten it if you like and serve right away."],
 "porcoes8": V,
 "dica": "Berries are champions in antioxidants, which fight ageing, and they are low in sugar. With yogurt, they become a protein-rich, creamy smoothie that fills you up and is one of the healthiest snacks there is.",
},
{
 "nome": "Green Smoothie with Banana and Spinach",
 "hook": "Green outside, sweet inside — the banana hides the spinach and delivers a creamy drink full of nutrients.",
 "tempo": "5 min", "rende": "1 large glass", "kcal_base": 160,
 "ings": ["1 banana", "1 handful of spinach", "1/2 apple in pieces", "3/4 cup milk (or coconut water)",
          "ice to taste"],
 "passos": [
   "Wash the spinach well.",
   "Blend the banana, the spinach, the apple and the milk in the blender for 1 minute, until it is green and creamy.",
   "Serve right away, very cold."],
 "porcoes8": V,
 "dica": "It is a delicious way to eat more green leaves: the banana and the apple sweeten naturally and hide the spinach, which comes in full of iron and fiber. Creamy and filling, it works as a nourishing liquid breakfast.",
},
{
 "nome": "Avocado Smoothie",
 "hook": "Extremely creamy and comforting, with the good fat of avocado — a smoothie that really fills you up and feeds your skin.",
 "tempo": "5 min", "rende": "1 large glass", "kcal_base": 190,
 "ings": ["1/2 ripe avocado", "3/4 cup milk (or plant drink)", "sweetener to taste — or 1 tsp honey",
          "1 pinch of cinnamon or a few drops of lemon", "ice to taste"],
 "passos": [
   "Scoop the avocado flesh out with a spoon, using only the very soft part.",
   "Blend the avocado, the milk and the sweetener (or honey) in the blender for 1 minute, until it turns into a smooth, silky cream.",
   "Serve cold, with a pinch of cinnamon or a few drops of lemon."],
 "porcoes8": V,
 "dica": "Avocado has good fat that fills you up a lot and is good for your heart and your skin. Blended with milk, it becomes a creamy and nourishing smoothie that holds hunger back for hours. Since it is higher in calories, it is a great snack option in a one-glass portion.",
},
{
 "nome": "Mango Smoothie with Yogurt",
 "hook": "Tropical, golden and creamy — mango turns into a sweet smoothie that tastes like dessert and refreshes right away.",
 "tempo": "5 min", "rende": "1 large glass", "kcal_base": 150,
 "ings": ["1 ripe mango in cubes (or 1 cup frozen)", "1 cup of plain yogurt with no sugar",
          "1/2 cup milk (or water)", "ice to taste"],
 "passos": [
   "Peel the mango and cut the flesh into cubes.",
   "Blend the mango, the yogurt and the milk in the blender for 1 minute, until it turns into a smooth, golden cream.",
   "Serve very cold."],
 "porcoes8": V,
 "dica": "Mango is naturally sweet and full of vitamin A and C, so it needs no sugar. With yogurt, the smoothie gains protein and creaminess, becoming a refreshing and filling snack — just respect the portion, since mango is a sweet fruit.",
},
{
 "nome": "Pear Smoothie with Oats",
 "hook": "Gentle and delicate, the pear brings a light sweetness to the creamy oats — a calm and comforting smoothie.",
 "tempo": "5 min", "rende": "1 large glass", "kcal_base": 170,
 "ings": ["1 ripe pear in pieces", "2 tbsp oats", "3/4 cup milk (or plant drink)",
          "1 pinch of cinnamon", "ice to taste"],
 "passos": [
   "Wash the pear and cut it into pieces, taking out the core with the seeds.",
   "Blend the pear, the oats, the milk and the cinnamon in the blender for 1 minute, until it is creamy.",
   "Serve right away, with a pinch of cinnamon on top."],
 "porcoes8": V,
 "dica": "The pear is a gentle fruit full of fiber, and with oats it makes a smoothie that keeps you full for a good while. The milk adds protein. It is a light and comforting drink, great for breakfast or a snack that holds hunger back.",
},
{
 "nome": "Banana and Cocoa Smoothie",
 "hook": "The taste of chocolate in a creamy, sugar-free smoothie — the perfect answer to the afternoon craving for sweets.",
 "tempo": "5 min", "rende": "1 large glass", "kcal_base": 180,
 "ings": ["1 banana", "1 tbsp 100% cocoa powder", "3/4 cup milk (or plant drink)",
          "1 tsp peanut butter (optional)", "ice to taste"],
 "passos": [
   "Peel the banana (if it is very ripe, it sweetens more).",
   "Blend the banana, the cocoa, the milk and the peanut butter in the blender for 1 minute, until it turns into a smooth, chocolatey cream.",
   "Serve very cold, with ice."],
 "porcoes8": V,
 "dica": "Pure cocoa gives the chocolate flavor with no sugar, and the banana sweetens it and makes the smoothie creamy. It is the tastiest way to kill the afternoon chocolate craving in a nourishing way, with the fiber of the fruit and the protein of the milk.",
},
{
 "nome": "Apple Smoothie with Cinnamon and Oats",
 "hook": "The flavor of an apple pie in a creamy glass — oats, apple and cinnamon blended into a snack that comforts.",
 "tempo": "5 min", "rende": "1 large glass", "kcal_base": 170,
 "ings": ["1 apple in pieces", "2 tbsp oats", "3/4 cup milk (or plant drink)",
          "1 tsp cinnamon", "ice to taste"],
 "passos": [
   "Cut the apple into pieces, taking out the seeds (you can leave the skin on).",
   "Blend the apple, the oats, the milk and the cinnamon in the blender for 1 1/2 minutes, until it is creamy and the apple is fully broken down.",
   "Serve right away, with a little more cinnamon on top."],
 "porcoes8": V,
 "dica": "Apple with cinnamon and oats tastes like a dessert, but together they make a smoothie full of fiber that keeps you full for hours. Cinnamon helps control the craving for sweets. It is a creamy, tasty and light snack, with no added sugar at all.",
},
{
 "nome": "Melon Smoothie with Mint",
 "hook": "Pale green, sweet and ultra-refreshing — melon with mint is pure hydration in a light smoothie.",
 "tempo": "5 min", "rende": "1 large glass", "kcal_base": 110,
 "ings": ["3 slices of melon with no rind, in cubes", "5 mint leaves", "1/2 cup of plain yogurt (or 1/2 cup water)",
          "ice to taste"],
 "passos": [
   "Cut the melon into cubes, taking out the seeds.",
   "Blend the melon, the mint and the yogurt (or the water) in the blender for 1 minute, until it is smooth.",
   "Serve very cold, with a mint leaf."],
 "porcoes8": V,
 "dica": "Melon is rich in water and helps to hydrate you and reduce bloating, with very few calories. Blended with mint, it is refreshing and light; with a little yogurt, it gains creaminess and protein. A perfect smoothie for hot days.",
},
# ---------------- ÁGUAS DETOX (141-144) — LIVRES ----------------
{
 "nome": "Detox Water with Cucumber, Lemon and Mint",
 "hook": "The water that makes you want to drink: light, fragrant and refreshing, to keep you hydrated all day without getting bored.",
 "tempo": "5 min + fridge", "rende": "1 pitcher", "kcal_base": 10, "livre": True,
 "ings": ["4 cups of water", "1/2 cucumber in thin rounds", "1/2 lemon in rounds", "6 mint leaves", "ice to taste"],
 "passos": [
   "Wash the cucumber, the lemon and the mint.",
   "In a pitcher, put the water, the cucumber and lemon rounds and the mint leaves.",
   "Put it in the fridge for at least 1 hour, so the water takes in the flavor. Serve cold through the day; you can top it up with more water as you drink it."],
 "dica": "Swapping soda and sugary juices for flavored water is one of the habits that helps most with losing weight. Cucumber, lemon and mint bring flavor with no calories, making water tastier and helping you stay hydrated all day.",
},
{
 "nome": "Detox Water with Ginger and Lemon",
 "hook": "A warm or cold water with a spicy touch that wakes your metabolism up first thing in the morning.",
 "tempo": "5 min", "rende": "1 glass", "kcal_base": 8, "livre": True,
 "ings": ["1 glass of water (warm or cold)", "juice of 1/2 lemon", "a few thin slices of ginger", "ice to taste (if cold)"],
 "passos": [
   "Cut the ginger into very thin slices.",
   "Mix the water, the lemon juice and the ginger in a glass.",
   "Let it rest for 5 minutes so the ginger releases its flavor. Drink it in the morning, on an empty stomach, warm or cold."],
 "dica": "Drinking water with lemon and ginger on an empty stomach helps to wake up your body and your digestion. Ginger has a slight thermogenic effect (it speeds up your metabolism a little). With no sugar, it is a simple morning ritual that supports weight loss.",
},
{
 "nome": "Detox Water with Berries",
 "hook": "Pink and pretty in the pitcher, with little fruits floating — a flavored water that looks like a spa drink.",
 "tempo": "5 min + fridge", "rende": "1 pitcher", "kcal_base": 15, "livre": True,
 "ings": ["4 cups of water", "1 handful of berries (strawberry, blueberry, raspberry)", "1/2 lemon in rounds",
          "mint leaves", "ice to taste"],
 "passos": [
   "Wash the berries and cut the strawberries in half.",
   "In a pitcher, put the water, the fruit, the lemon rounds and the mint. Lightly crush the fruit with a spoon so it releases its color and flavor.",
   "Put it in the fridge for 1 to 2 hours and serve cold."],
 "dica": "Berries bring color, flavor and antioxidants to the water with almost no calories. It is a beautiful and tasty way to drink more water through the day, replacing sugary drinks and helping with hydration and weight loss.",
},
{
 "nome": "Coconut Water with Lemon and Mint",
 "hook": "The natural hydration of coconut water, boosted with lemon and mint — refreshing and full of minerals.",
 "tempo": "3 min", "rende": "1 large glass", "kcal_base": 45, "livre": True,
 "ings": ["1 large glass of coconut water", "juice of 1/2 lemon", "5 mint leaves", "ice to taste"],
 "passos": [
   "Mix the coconut water with the lemon juice in a glass.",
   "Add the mint leaves and the ice and stir.",
   "Serve very cold, ideally the natural kind (boxed coconut water usually has added sugar — go for the natural one)."],
 "dica": "Coconut water replaces minerals and hydrates very well, with few calories when it is natural. With lemon and mint, it is even more refreshing. It is great after exercise or on hot days, instead of sugary sports drinks.",
},
# ---------------- CHÁS / INFUSÕES (145-150) — LIVRES ----------------
{
 "nome": "Green Tea with Lemon and Ginger",
 "hook": "The number 1 ally for anyone losing weight: green tea speeds up your metabolism, and lemon and ginger give it an extra push.",
 "tempo": "8 min", "rende": "1 cup", "kcal_base": 5, "livre": True,
 "ings": ["1 cup of water", "1 tsp green tea (or 1 tea bag)", "a few slices of ginger", "juice of 1/2 lemon"],
 "passos": [
   "Boil the water and turn off the heat. Wait 1 minute (water that is too hot makes green tea bitter).",
   "Add the green tea and the ginger slices, cover it and let it steep for 3 minutes.",
   "Strain it, add the lemon juice and drink it warm. You can also drink it cold, through the day."],
 "dica": "Green tea is one of the most studied foods for weight loss: it has substances that help speed up your metabolism and burn fat. With ginger and lemon, the effect is reinforced. With no sugar, it is a free drink you can have every day.",
},
{
 "nome": "Iced Hibiscus Tea",
 "hook": "Ruby red and slightly tart, hibiscus is famous for helping to reduce bloating — delicious cold in the heat.",
 "tempo": "10 min + fridge", "rende": "1 pitcher", "kcal_base": 5, "livre": True,
 "ings": ["4 cups of water", "2 tbsp dried hibiscus flowers (or 2 tea bags)",
          "lemon rounds", "mint leaves", "ice to taste"],
 "passos": [
   "Boil the water and turn it off. Add the hibiscus, cover it and let it steep for 5 to 7 minutes.",
   "Strain it and let it cool. Put it in the fridge.",
   "Serve very cold, with lemon rounds, mint and ice."],
 "dica": "Hibiscus tea is known for helping to reduce water retention (bloating) and is rich in antioxidants. Cold and with no sugar, it is a refreshing and free drink, great for replacing sodas and processed juices through the day.",
},
{
 "nome": "Chamomile Tea with Cinnamon",
 "hook": "Warm and comforting, the tea that calms you before bed — and a good night's sleep also helps you lose weight.",
 "tempo": "8 min", "rende": "1 cup", "kcal_base": 5, "livre": True,
 "ings": ["1 cup of water", "1 tbsp chamomile flowers (or 1 tea bag)", "1 cinnamon stick (or 1 pinch of ground)"],
 "passos": [
   "Boil the water and turn off the heat.",
   "Add the chamomile and the cinnamon, cover it and let it steep for 5 minutes.",
   "Strain it and drink it warm, ideally at night, before bed."],
 "dica": "Chamomile calms you and helps you relax, improving your sleep. Sleeping well is a factor many people forget in weight loss: bad nights increase hunger and the craving for sweets the next day. This tea is a nighttime ritual that supports your diet.",
},
{
 "nome": "Ginger, Lemon and Cinnamon Infusion",
 "hook": "A thermogenic and fragrant infusion that warms your body and gives your metabolism that boost.",
 "tempo": "10 min", "rende": "1 large cup", "kcal_base": 8, "livre": True,
 "ings": ["1 large cup of water", "several slices of ginger", "1 cinnamon stick", "juice of 1/2 lemon"],
 "passos": [
   "In a small pot, boil the water with the ginger slices and the cinnamon stick for 5 minutes, over low heat.",
   "Turn it off, cover it and let it rest for another 3 minutes.",
   "Strain it, add the lemon juice and drink it warm."],
 "dica": "Ginger and cinnamon have a slight thermogenic effect, meaning they help your body spend a little more energy. It is a warm and comforting infusion, with no sugar, that works well on cold days and gives your metabolism that extra support.",
},
{
 "nome": "Mint Tea with Lemon",
 "hook": "Fresh and good for digestion, mint tea calms your stomach after meals — light and fragrant.",
 "tempo": "8 min", "rende": "1 cup", "kcal_base": 4, "livre": True,
 "ings": ["1 cup of water", "1 handful of fresh mint leaves (or 1 tea bag)", "juice of 1/2 lemon"],
 "passos": [
   "Boil the water and turn off the heat.",
   "Add the mint leaves, cover it and let it steep for 5 minutes.",
   "Strain it, add the lemon juice and drink it warm or cold, ideally after meals."],
 "dica": "Mint helps digestion and reduces that heavy stomach feeling after eating. A digestive tea with no sugar after meals is a simple habit that helps you avoid nibbling on sweets right afterwards.",
},
{
 "nome": "Fennel Tea",
 "hook": "Gentle and naturally sweet, fennel calms your stomach and reduces gas — a comforting tea after eating.",
 "tempo": "8 min", "rende": "1 cup", "kcal_base": 4, "livre": True,
 "ings": ["1 cup of water", "1 tsp fennel seeds — or 1 tea bag"],
 "passos": [
   "Lightly crush the fennel seeds (this releases more aroma).",
   "Boil the water and turn it off. Add the fennel, cover it and let it steep for 5 minutes.",
   "Strain it and drink it warm, ideally after meals or at night."],
 "dica": "Fennel is known for calming your stomach and reducing gas and belly bloating. Naturally sweet, it needs no sugar. It is a comforting digestive tea, great for finishing a meal in a light way.",
},
]
