# -*- coding: utf-8 -*-
"""30 receitas de VITAMINAS, SUCOS E CHÁS DETOX (121-150). ALEMÃO. Sem açúcar.

Tradução literal de `receitas_suco.py`. Convenções em GLOSSARIO-TRADUCAO.md.
⛔ O campo `prompt` não é replicado: a foto é a mesma do PT (fotos/121-150).
- Sucos e vitaminas (têm caloria): porcoes8 (8 entradas).
  Metas (kcal): 90/110/130/150 · 130/150/170/190.
- Chás e águas detox (≈ zero caloria): `livre: True` -> a faixa "Freies Getränk"
  entra no lugar da tabela e a receita NÃO tem porcoes8, como no PT.
"""

# porção padrão para sucos (metas 90/110/130/150 · 130/150/170/190)
P = ["1 Glas (200 ml)", "1 Glas (250 ml)", "1 großes Glas (300 ml)", "1 großes Glas · ½ Frucht",
     "1 großes Glas (300 ml)", "1 großes Glas (350 ml)", "1 großes Glas · ½ Frucht", "2 Gläser oder 1 Frucht mehr"]
# porção padrão para vitaminas (mais encorpadas, dá para somar aveia)
V = ["1 Glas (200 ml)", "1 Glas (250 ml)", "1 großes Glas (300 ml)", "1 Glas · 1 EL Haferflocken",
     "1 großes Glas (300 ml)", "1 großes Glas (350 ml)", "1 großes Glas · 1 EL Haferflocken", "1 großes Glas · 2 EL Haferflocken"]

RECEITAS = [
# ---------------- SUCOS DETOX (121-130) ----------------
{
 "nome": "Grüner Detox-Saft",
 "hook": "Der Klassiker am Morgen: leicht, erfrischend und voller Chlorophyll, das dem Körper einen Anstoß gibt.",
 "tempo": "5 Min.", "rende": "1 großes Glas", "kcal_base": 90,
 "ings": ["1 Blatt Grünkohl (oder 1 Handvoll Spinat)", "1 grüner Apfel in Stücken", "Saft von ½ Zitrone",
          "1 kleines Stück Ingwer", "200 ml kaltes Wasser", "Eiswürfel nach Geschmack"],
 "passos": [
   "Wasche den Grünkohl und den Apfel gründlich. Entferne den dicken Strunk vom Grünkohl.",
   "Gib alles mit dem kalten Wasser in den Mixer und mixe 1 Minute auf höchster Stufe, bis alles gut flüssig ist.",
   "Wenn du es ohne Stückchen magst, gieße alles durch ein Sieb. Serviere sofort, mit Eiswürfeln."],
 "porcoes8": P,
 "dica": "Grüne Blätter haben viele Ballaststoffe und viel Wasser bei sehr wenigen Kalorien, sie helfen beim Entwässern und geben ein Sättigungsgefühl. Vor dem Frühstück getrunken versorgt dieser Saft dich mit Flüssigkeit und bereitet den Körper auf den Tag vor. Ohne Zucker ist er eines der leichtesten Getränke überhaupt.",
},
{
 "nome": "Gurken-Zitronen-Minz-Saft",
 "hook": "Pure Frische in einem Glas — die Gurke erfrischt, die Zitrone weckt auf und die Minze duftet. Flüssigkeit, die beim Entwässern hilft.",
 "tempo": "5 Min.", "rende": "1 großes Glas", "kcal_base": 70,
 "ings": ["½ Gurke in Stücken", "Saft von 1 Zitrone", "5 Minzblätter", "250 ml kaltes Wasser", "Eiswürfel nach Geschmack"],
 "passos": [
   "Wasche die Gurke und schneide sie in Stücke (die Schale kannst du dranlassen, wenn sie dünn ist).",
   "Mixe die Gurke, den Zitronensaft, die Minze und das Wasser 1 Minute im Mixer.",
   "Gieße alles durch ein Sieb, wenn du es klarer magst, und serviere es schön kalt, mit Eiswürfeln."],
 "porcoes8": P,
 "dica": "Die Gurke besteht fast nur aus Wasser und hilft dabei, den Körper zu versorgen und Wassereinlagerungen (das Aufgeschwemmtsein) zu verringern. Mit Zitrone und Minze wird daraus ein super erfrischendes Getränk mit praktisch keinen Kalorien — hervorragend, um es über den Tag anstelle von Limonade zu trinken.",
},
{
 "nome": "Ananas-Minz-Ingwer-Saft",
 "hook": "Süß, tropisch und gut für die Verdauung — Ananas mit Ingwer ist der Saft, der erfrischt und dazu entzündungshemmend wirkt.",
 "tempo": "5 Min.", "rende": "1 großes Glas", "kcal_base": 110,
 "ings": ["2 Scheiben Ananas in Stücken", "5 Minzblätter", "1 kleines Stück Ingwer",
          "200 ml kaltes Wasser", "Eiswürfel nach Geschmack"],
 "passos": [
   "Schneide die Ananas in Stücke und entferne die Schale und den harten Strunk in der Mitte.",
   "Mixe die Ananas, die Minze, den Ingwer und das Wasser 1 Minute im Mixer, bis alles gleichmäßig ist.",
   "Gieße alles durch ein Sieb, wenn du magst, und serviere es schön kalt, mit Eiswürfeln und einem Minzblättchen."],
 "porcoes8": P,
 "dica": "Die Ananas enthält Enzyme, die bei der Verdauung helfen, und ist reich an Wasser und Vitamin C. Der Ingwer bringt den Stoffwechsel leicht in Schwung und wirkt entzündungshemmend. Der Saft ist von Natur aus süß, Zucker braucht er also nicht — das übernimmt die Frucht.",
},
{
 "nome": "Rote-Bete-Möhren-Orangen-Saft",
 "hook": "Leuchtend rot und voller Energie — Rote Bete mit Orange ist ein Saft, der wach macht und den Tag bunt beginnt.",
 "tempo": "5 Min.", "rende": "1 großes Glas", "kcal_base": 120,
 "ings": ["½ kleine rohe Rote Bete in Stücken", "1 Möhre in Stücken", "Saft von 2 Orangen",
          "100 ml Wasser", "Eiswürfel nach Geschmack"],
 "passos": [
   "Schäle die Rote Bete und die Möhre und schneide beides in kleine Stücke.",
   "Presse die Orangen aus. Mixe die Rote Bete, die Möhre, den Orangensaft und das Wasser 2 Minuten im Mixer, bis alles gut flüssig ist.",
   "Gieße alles durch ein Sieb (Rote Bete und Möhre hinterlassen Fasern) und serviere es kalt."],
 "porcoes8": P,
 "dica": "Die Rote Bete verbessert die Durchblutung und gibt Energie, die Möhre bringt Vitamin A und die Orange Vitamin C. Zusammen ergeben sie einen von Natur aus süßen und nahrhaften Saft. Weil er den natürlichen Zucker der Früchte und der Roten Bete enthält, lohnt es sich, die Glasgröße einzuhalten.",
},
{
 "nome": "Wassermelonensaft mit Zitrone",
 "hook": "Flüssigkeit in Saftform: Die Wassermelone besteht fast nur aus Wasser, ist genau richtig süß und erfrischt wie kaum etwas anderes.",
 "tempo": "5 Min.", "rende": "1 großes Glas", "kcal_base": 80,
 "ings": ["2 große Scheiben Wassermelone ohne Schale", "Saft von ½ Zitrone", "5 Minzblätter (nach Wunsch)", "Eiswürfel nach Geschmack"],
 "passos": [
   "Schneide die Wassermelone in Würfel und entferne die größeren Kerne.",
   "Mixe die Wassermelone mit dem Zitronensaft (und der Minze, wenn du magst) 30 Sekunden im Mixer — die Wassermelone gibt viel Wasser ab, du brauchst kaum Flüssigkeit dazuzugeben.",
   "Serviere sofort, schön kalt, mit Eiswürfeln."],
 "porcoes8": P,
 "dica": "Die Wassermelone besteht zu über 90 % aus Wasser, sie versorgt den Körper also gut und füllt den Magen mit wenigen Kalorien. Sie ist von Natur aus süß und erfrischend, perfekt, um bei Hitze die Lust auf etwas Süßes und Kaltes zu stillen, ohne die Diät zu verlassen.",
},
{
 "nome": "Möhren-Apfel-Ingwer-Saft",
 "hook": "Süß, orange und mit einer scharfen Note Ingwer — ein Saft, der die Abwehrkräfte stärkt und den Körper weckt.",
 "tempo": "5 Min.", "rende": "1 großes Glas", "kcal_base": 110,
 "ings": ["1 Möhre in Stücken", "1 Apfel in Stücken", "1 kleines Stück Ingwer", "200 ml Wasser", "Eiswürfel nach Geschmack"],
 "passos": [
   "Schäle die Möhre und schneide den Apfel in Stücke, dabei die Kerne entfernen.",
   "Mixe die Möhre, den Apfel, den Ingwer und das Wasser 2 Minuten im Mixer, bis alles gut flüssig ist.",
   "Gieße alles durch ein Sieb und serviere es kalt."],
 "porcoes8": P,
 "dica": "Möhre und Apfel bringen natürliche Süße und viele Ballaststoffe, während der Ingwer die wärmende Note gibt, die dem Stoffwechsel hilft. Es ist ein vitaminreicher Saft, ideal, um mit Energie in den Tag zu starten, ganz ohne Zucker.",
},
{
 "nome": "Grüner Saft mit Spinat, Ananas und Gurke",
 "hook": "Grün und süß zugleich — die Ananas überdeckt den Spinat, und du merkst gar nicht, wie gesund das ist, was du gerade trinkst.",
 "tempo": "5 Min.", "rende": "1 großes Glas", "kcal_base": 100,
 "ings": ["1 Handvoll Spinat", "1 Scheibe Ananas in Stücken", "½ Gurke in Stücken",
          "Saft von ½ Zitrone", "200 ml kaltes Wasser", "Eiswürfel nach Geschmack"],
 "passos": [
   "Wasche den Spinat und die Gurke gründlich.",
   "Mixe den Spinat, die Ananas, die Gurke, die Zitrone und das Wasser 1 Minute im Mixer, bis alles schön grün und flüssig ist.",
   "Gieße alles durch ein Sieb, wenn du magst, und serviere es kalt."],
 "porcoes8": P,
 "dica": "Spinat ist außerordentlich reich an Eisen und Nährstoffen bei fast keinen Kalorien, und die Ananas macht den Saft süß und lecker ganz ohne Zucker. Die Gurke versorgt den Körper mit Flüssigkeit und hilft beim Entwässern. Ein einfacher und schmackhafter Weg, mehr Grünes zu essen.",
},
{
 "nome": "Orangen-Möhren-Ingwer-Saft",
 "hook": "Die tägliche Portion Vitamin C in einem leuchtend orangefarbenen Glas — stärkt die Abwehrkräfte und gibt Energie für den Tag.",
 "tempo": "5 Min.", "rende": "1 großes Glas", "kcal_base": 110,
 "ings": ["Saft von 3 Orangen", "1 Möhre in Stücken", "1 kleines Stück Ingwer", "Eiswürfel nach Geschmack"],
 "passos": [
   "Presse die Orangen aus.",
   "Schäle die Möhre und schneide sie in kleine Stücke. Mixe die Möhre, den Orangensaft und den Ingwer 2 Minuten im Mixer.",
   "Gieße alles durch ein Sieb und serviere es schön kalt, mit Eiswürfeln."],
 "porcoes8": P,
 "dica": "Orange und Möhre stecken voller Vitamin C und A, und der Ingwer gibt die Note, die der Durchblutung und dem Stoffwechsel hilft. Es ist ein Energiesaft, der von Natur aus süß ist — denk nur daran, die Portion einzuhalten, denn der Zucker der Früchte zählt bei den Kalorien mit.",
},
{
 "nome": "Natürlicher Traubensaft mit Zitrone",
 "hook": "Kräftig violett und voller Antioxidantien — die Traube wird zu einem von Natur aus süßen Saft, der dem Herzen guttut.",
 "tempo": "5 Min.", "rende": "1 großes Glas", "kcal_base": 120,
 "ings": ["1 kleine Rispe blaue kernlose Weintrauben (ca. 225 g)", "Saft von ½ Zitrone",
          "150 ml kaltes Wasser", "Eiswürfel nach Geschmack"],
 "passos": [
   "Wasche die Trauben gründlich und zupfe sie von den Stielen.",
   "Mixe die Trauben mit der Zitrone und dem Wasser 1 Minute im Mixer, bis sie zerfallen.",
   "Gieße alles durch ein Sieb und drücke gut aus, um den ganzen Saft zu gewinnen, und serviere es kalt."],
 "porcoes8": P,
 "dica": "Die blaue Traube ist reich an Antioxidantien, die das Herz und die Haut schützen. Frisch gemacht und ohne Zucker ist natürlicher Traubensaft etwas ganz anderes als der aus der Packung — denk nur daran, dass die Traube eine sehr süße Frucht ist, die Glasgröße zählt also.",
},
{
 "nome": "Detox-Saft mit Apfel, Grünkohl und Staudensellerie",
 "hook": "Superleicht und entwässernd — die grüne Kombination, die den Körper reinigt und vor den Mahlzeiten sehr gut passt.",
 "tempo": "5 Min.", "rende": "1 großes Glas", "kcal_base": 90,
 "ings": ["1 grüner Apfel in Stücken", "1 Blatt Grünkohl", "1 Stange Staudensellerie", "Saft von ½ Zitrone",
          "200 ml kaltes Wasser", "Eiswürfel nach Geschmack"],
 "passos": [
   "Wasche den Grünkohl, den Apfel und den Sellerie. Entferne den dicken Strunk vom Grünkohl.",
   "Mixe den Apfel, den Grünkohl, den Sellerie, die Zitrone und das Wasser 1 Minute im Mixer.",
   "Gieße alles durch ein Sieb und serviere es schön kalt."],
 "porcoes8": P,
 "dica": "Staudensellerie wirkt harntreibend und hilft, überschüssige Flüssigkeit auszuscheiden, der Grünkohl bringt Ballaststoffe und Nährstoffe und der Apfel süßt von selbst. Ein leichter, entwässernder grüner Saft, hervorragend als Begleitung beim Abnehmen.",
},
# ---------------- VITAMINAS / SMOOTHIES (131-140) ----------------
{
 "nome": "Bananen-Smoothie mit Haferflocken und Zimt",
 "hook": "Cremig und wohltuend, dieser Smoothie trägt durch den ganzen Vormittag — das flüssige Frühstück für volle Tage.",
 "tempo": "5 Min.", "rende": "1 großes Glas", "kcal_base": 190,
 "ings": ["1 Banane", "2 EL Haferflocken", "200 ml Milch (oder Pflanzendrink)",
          "1 Prise Zimt", "Eiswürfel nach Geschmack"],
 "passos": [
   "Schäle die Banane (je reifer sie ist, desto süßer wird der Smoothie).",
   "Mixe die Banane, die Haferflocken, die Milch und den Zimt 1 Minute im Mixer, bis alles cremig ist.",
   "Serviere sofort, mit einer Prise Zimt obendrauf. Wenn du es kälter magst, gib Eiswürfel dazu und mixe noch einmal."],
 "porcoes8": V,
 "dica": "Banane mit Haferflocken ist ein Duo, das dank der Ballaststoffe stundenlang satt hält, und die Milch bringt Eiweiß dazu. Das ist ein Smoothie, der als vollständige flüssige Mahlzeit funktioniert — perfekt zum Frühstück oder als Snack für alle, die es eilig haben, ganz ohne Zucker.",
},
{
 "nome": "Erdbeer-Smoothie mit Joghurt",
 "hook": "Rosa und cremig, mit der natürlichen Süße der Erdbeere — ein Smoothie, der wie ein Milchshake wirkt, aber leicht und eiweißreich ist.",
 "tempo": "5 Min.", "rende": "1 großes Glas", "kcal_base": 150,
 "ings": ["150 g Erdbeeren (frisch oder gefroren)", "1 Becher Naturjoghurt ohne Zucker (ca. 170 g)",
          "100 ml Milch (oder Wasser)", "Süßstoff nach Geschmack (nach Wunsch)", "Eiswürfel nach Geschmack"],
 "passos": [
   "Wasche die Erdbeeren und entferne die grünen Blättchen.",
   "Mixe die Erdbeeren, den Joghurt und die Milch 1 Minute im Mixer, bis eine glatte, rosa Creme entsteht.",
   "Probiere und süße bei Bedarf etwas nach. Serviere kalt."],
 "porcoes8": V,
 "dica": "Der Naturjoghurt bringt Eiweiß und Cremigkeit ohne Zucker, und die Erdbeere süßt von selbst bei sehr wenigen Kalorien. Das ist ein sättigender und erfrischender Smoothie, der die Lust auf einen Milchshake auf leichte und nahrhafte Weise stillt.",
},
{
 "nome": "Beeren-Smoothie",
 "hook": "Violett, voller Antioxidantien und Geschmack — eine Mischung roter Beeren, cremig gemixt, gut für die Haut und die Sättigung.",
 "tempo": "5 Min.", "rende": "1 großes Glas", "kcal_base": 140,
 "ings": ["140 g gemischte Beeren (Erdbeeren, Heidelbeeren, Himbeeren)", "1 Becher Naturjoghurt ohne Zucker",
          "100 ml Milch (oder Wasser)", "Süßstoff nach Geschmack (nach Wunsch)", "Eiswürfel nach Geschmack"],
 "passos": [
   "Wenn die Beeren gefroren sind, nimm sie direkt so (dann wird der Smoothie kälter und cremiger).",
   "Mixe die Beeren, den Joghurt und die Milch 1 Minute im Mixer, bis eine glatte Creme entsteht.",
   "Probiere, süße bei Bedarf nach und serviere sofort."],
 "porcoes8": V,
 "dica": "Beeren sind Spitzenreiter bei den Antioxidantien, die dem Altern entgegenwirken, und enthalten wenig Zucker. Mit Joghurt werden sie zu einem eiweißreichen, cremigen Smoothie, der sättigt und zu den gesündesten Snacks überhaupt gehört.",
},
{
 "nome": "Grüner Smoothie mit Banane und Spinat",
 "hook": "Grün von außen, süß von innen — die Banane versteckt den Spinat und liefert ein cremiges Getränk voller Nährstoffe.",
 "tempo": "5 Min.", "rende": "1 großes Glas", "kcal_base": 160,
 "ings": ["1 Banane", "1 Handvoll Spinat", "½ Apfel in Stücken", "200 ml Milch (oder Kokoswasser)",
          "Eiswürfel nach Geschmack"],
 "passos": [
   "Wasche den Spinat gründlich.",
   "Mixe die Banane, den Spinat, den Apfel und die Milch 1 Minute im Mixer, bis alles grün und cremig ist.",
   "Serviere sofort, schön kalt."],
 "porcoes8": V,
 "dica": "Das ist ein köstlicher Weg, mehr grüne Blätter zu essen: Banane und Apfel süßen von selbst und überdecken den Spinat, der voller Eisen und Ballaststoffe steckt. Cremig und sättigend funktioniert er als nahrhaftes flüssiges Frühstück.",
},
{
 "nome": "Avocado-Smoothie",
 "hook": "Extrem cremig und wohltuend, mit dem guten Fett der Avocado — ein Smoothie, der wirklich sättigt und die Haut pflegt.",
 "tempo": "5 Min.", "rende": "1 großes Glas", "kcal_base": 190,
 "ings": ["½ reife Avocado", "200 ml Milch (oder Pflanzendrink)", "Süßstoff nach Geschmack — oder 1 TL Honig",
          "1 Prise Zimt oder ein paar Tropfen Zitrone", "Eiswürfel nach Geschmack"],
 "passos": [
   "Hole das Fruchtfleisch der Avocado mit einem Löffel heraus und nimm nur den ganz weichen Teil.",
   "Mixe die Avocado, die Milch und den Süßstoff (oder Honig) 1 Minute im Mixer, bis eine glatte, seidige Creme entsteht.",
   "Serviere kalt, mit einer Prise Zimt oder ein paar Tropfen Zitrone."],
 "porcoes8": V,
 "dica": "Die Avocado enthält gutes Fett, das stark sättigt und dem Herzen und der Haut guttut. Mit Milch gemixt wird daraus ein cremiger, nahrhafter Smoothie, der den Hunger stundenlang fernhält. Weil er kalorienreicher ist, eignet er sich sehr gut als Snack in der Größe eines Glases.",
},
{
 "nome": "Mango-Smoothie mit Joghurt",
 "hook": "Tropisch, golden und cremig — die Mango wird zu einem süßen Smoothie, der wie ein Nachtisch wirkt und sofort erfrischt.",
 "tempo": "5 Min.", "rende": "1 großes Glas", "kcal_base": 150,
 "ings": ["1 reife Mango in Würfeln (oder 165 g gefroren)", "1 Becher Naturjoghurt ohne Zucker",
          "100 ml Milch (oder Wasser)", "Eiswürfel nach Geschmack"],
 "passos": [
   "Schäle die Mango und schneide das Fruchtfleisch in Würfel.",
   "Mixe die Mango, den Joghurt und die Milch 1 Minute im Mixer, bis eine goldene, glatte Creme entsteht.",
   "Serviere schön kalt."],
 "porcoes8": V,
 "dica": "Die Mango ist von Natur aus süß und voller Vitamin A und C, Zucker ist überflüssig. Mit Joghurt gewinnt der Smoothie Eiweiß und Cremigkeit und wird zu einem erfrischenden, sättigenden Snack — halte nur die Portion ein, denn die Mango ist eine süße Frucht.",
},
{
 "nome": "Birnen-Smoothie mit Haferflocken",
 "hook": "Sanft und fein gibt die Birne den cremigen Haferflocken eine leichte Süße — ein ruhiger, wohltuender Smoothie.",
 "tempo": "5 Min.", "rende": "1 großes Glas", "kcal_base": 170,
 "ings": ["1 reife Birne in Stücken", "2 EL Haferflocken", "200 ml Milch (oder Pflanzendrink)",
          "1 Prise Zimt", "Eiswürfel nach Geschmack"],
 "passos": [
   "Wasche die Birne und schneide sie in Stücke, dabei das Kerngehäuse entfernen.",
   "Mixe die Birne, die Haferflocken, die Milch und den Zimt 1 Minute im Mixer, bis alles cremig ist.",
   "Serviere sofort, mit einer Prise Zimt obendrauf."],
 "porcoes8": V,
 "dica": "Die Birne ist eine milde Frucht voller Ballaststoffe, und mit den Haferflocken zusammen ergibt sie einen Smoothie, der lange satt hält. Die Milch bringt Eiweiß dazu. Ein leichtes, wohltuendes Getränk, hervorragend zum Frühstück oder als Snack, der den Hunger fernhält.",
},
{
 "nome": "Bananen-Kakao-Smoothie",
 "hook": "Schokoladengeschmack in einem cremigen Smoothie ohne Zucker — die perfekte Lösung für die Lust auf Süßes am Nachmittag.",
 "tempo": "5 Min.", "rende": "1 großes Glas", "kcal_base": 180,
 "ings": ["1 Banane", "1 EL 100 % Kakaopulver", "200 ml Milch (oder Pflanzendrink)",
          "1 TL Erdnussmus (nach Wunsch)", "Eiswürfel nach Geschmack"],
 "passos": [
   "Schäle die Banane (je reifer sie ist, desto süßer wird der Smoothie).",
   "Mixe die Banane, den Kakao, die Milch und das Erdnussmus 1 Minute im Mixer, bis eine glatte Schokoladencreme entsteht.",
   "Serviere schön kalt, mit Eiswürfeln."],
 "porcoes8": V,
 "dica": "Reiner Kakao gibt den Schokoladengeschmack ohne Zucker, und die Banane süßt und macht den Smoothie cremig. Das ist die leckerste Art, die Lust auf Schokolade am Nachmittag nahrhaft zu stillen, mit den Ballaststoffen der Frucht und dem Eiweiß der Milch.",
},
{
 "nome": "Apfel-Zimt-Hafer-Smoothie",
 "hook": "Der Geschmack eines Apfelkuchens in einem cremigen Glas — Haferflocken, Apfel und Zimt gemixt zu einem Snack, der wohltut.",
 "tempo": "5 Min.", "rende": "1 großes Glas", "kcal_base": 170,
 "ings": ["1 Apfel in Stücken", "2 EL Haferflocken", "200 ml Milch (oder Pflanzendrink)",
          "1 TL Zimt", "Eiswürfel nach Geschmack"],
 "passos": [
   "Schneide den Apfel in Stücke und entferne die Kerne (die Schale kannst du dranlassen).",
   "Mixe den Apfel, die Haferflocken, die Milch und den Zimt 1½ Minuten im Mixer, bis alles cremig und der Apfel gut zerkleinert ist.",
   "Serviere sofort, mit noch etwas Zimt obendrauf."],
 "porcoes8": V,
 "dica": "Apfel mit Zimt und Haferflocken erinnert an einen Nachtisch, ergibt zusammen aber einen Smoothie voller Ballaststoffe, der stundenlang satt hält. Der Zimt hilft, die Lust auf Süßes zu steuern. Ein cremiger, leckerer und leichter Snack, ganz ohne zugesetzten Zucker.",
},
{
 "nome": "Honigmelonen-Minz-Smoothie",
 "hook": "Hellgrün, süß und ultra-erfrischend — Honigmelone mit Minze ist pure Erfrischung in einem leichten Smoothie.",
 "tempo": "5 Min.", "rende": "1 großes Glas", "kcal_base": 110,
 "ings": ["3 Scheiben Honigmelone ohne Schale, in Würfeln", "5 Minzblätter", "½ Becher Naturjoghurt (oder 100 ml Wasser)",
          "Eiswürfel nach Geschmack"],
 "passos": [
   "Schneide die Honigmelone in Würfel und entferne die Kerne.",
   "Mixe die Melone, die Minze und den Joghurt (oder das Wasser) 1 Minute im Mixer, bis alles glatt ist.",
   "Serviere schön kalt, mit einem Minzblättchen."],
 "porcoes8": V,
 "dica": "Die Honigmelone ist reich an Wasser und hilft dabei, den Körper zu versorgen und zu entwässern, bei sehr wenigen Kalorien. Mit Minze gemixt wird sie erfrischend und leicht; mit etwas Joghurt gewinnt sie Cremigkeit und Eiweiß. Ein perfekter Smoothie für heiße Tage.",
},
# ---------------- ÁGUAS DETOX (141-144) — LIVRES ----------------
{
 "nome": "Detox-Wasser mit Gurke, Zitrone und Minze",
 "hook": "Das Wasser, das Lust aufs Trinken macht: leicht, duftend und erfrischend, um den ganzen Tag versorgt zu sein, ohne dass es langweilig wird.",
 "tempo": "5 Min. + Kühlschrank", "rende": "1 Krug", "kcal_base": 10, "livre": True,
 "ings": ["1 Liter Wasser", "½ Gurke in dünnen Scheiben", "½ Zitrone in Scheiben", "6 Minzblätter", "Eiswürfel nach Geschmack"],
 "passos": [
   "Wasche die Gurke, die Zitrone und die Minze.",
   "Gib das Wasser, die Gurken- und Zitronenscheiben und die Minzblätter in einen Krug.",
   "Stelle ihn mindestens 1 Stunde in den Kühlschrank, damit das Wasser den Geschmack annimmt. Trinke es über den Tag verteilt kalt; du kannst immer wieder Wasser nachfüllen."],
 "dica": "Limonade und gezuckerte Säfte durch aromatisiertes Wasser zu ersetzen ist eine der Gewohnheiten, die beim Abnehmen am meisten helfen. Gurke, Zitrone und Minze geben Geschmack ohne Kalorien, machen das Wasser leckerer und helfen dir, den ganzen Tag genug zu trinken.",
},
{
 "nome": "Detox-Wasser mit Ingwer und Zitrone",
 "hook": "Ein warmes oder kaltes Wasser mit einer scharfen Note, das den Stoffwechsel gleich am Morgen weckt.",
 "tempo": "5 Min.", "rende": "1 Glas", "kcal_base": 8, "livre": True,
 "ings": ["1 Glas Wasser (warm oder kalt)", "Saft von ½ Zitrone", "ein paar dünne Ingwerscheiben", "Eiswürfel nach Geschmack (wenn kalt)"],
 "passos": [
   "Schneide den Ingwer in sehr dünne Scheiben.",
   "Vermische das Wasser, den Zitronensaft und den Ingwer in einem Glas.",
   "Lass alles 5 Minuten stehen, damit der Ingwer seinen Geschmack abgibt. Trinke es morgens auf nüchternen Magen, warm oder kalt."],
 "dica": "Wasser mit Zitrone und Ingwer auf nüchternen Magen zu trinken hilft, den Körper und die Verdauung zu wecken. Der Ingwer wirkt leicht wärmend (er bringt den Stoffwechsel ein wenig in Schwung). Ohne Zucker ist das ein einfaches Morgenritual, das beim Abnehmen unterstützt.",
},
{
 "nome": "Detox-Wasser mit Beeren",
 "hook": "Rosa und schön im Krug, mit Beeren, die darin schwimmen — ein aromatisiertes Wasser, das wie ein Getränk aus dem Spa wirkt.",
 "tempo": "5 Min. + Kühlschrank", "rende": "1 Krug", "kcal_base": 15, "livre": True,
 "ings": ["1 Liter Wasser", "1 Handvoll Beeren (Erdbeeren, Heidelbeeren, Himbeeren)", "½ Zitrone in Scheiben",
          "Minzblätter", "Eiswürfel nach Geschmack"],
 "passos": [
   "Wasche die Beeren und halbiere die Erdbeeren.",
   "Gib das Wasser, die Beeren, die Zitronenscheiben und die Minze in einen Krug. Drücke die Beeren mit einem Löffel leicht an, damit sie Farbe und Geschmack abgeben.",
   "Stelle den Krug 1 bis 2 Stunden in den Kühlschrank und serviere das Wasser kalt."],
 "dica": "Die Beeren geben dem Wasser Farbe, Geschmack und Antioxidantien bei fast keinen Kalorien. Es ist eine schöne und leckere Art, über den Tag mehr zu trinken, gezuckerte Getränke zu ersetzen und so die Versorgung mit Flüssigkeit und das Abnehmen zu unterstützen.",
},
{
 "nome": "Kokoswasser mit Zitrone und Minze",
 "hook": "Die natürliche Erfrischung von Kokoswasser, aufgepeppt mit Zitrone und Minze — erfrischend und voller Mineralstoffe.",
 "tempo": "3 Min.", "rende": "1 großes Glas", "kcal_base": 45, "livre": True,
 "ings": ["1 großes Glas Kokoswasser", "Saft von ½ Zitrone", "5 Minzblätter", "Eiswürfel nach Geschmack"],
 "passos": [
   "Vermische das Kokoswasser mit dem Zitronensaft in einem Glas.",
   "Gib die Minzblätter und die Eiswürfel dazu und rühre um.",
   "Serviere schön kalt, am besten mit naturbelassenem Kokoswasser (das aus der Packung enthält oft zugesetzten Zucker — nimm lieber das natürliche)."],
 "dica": "Kokoswasser füllt die Mineralstoffe auf und versorgt den Körper sehr gut mit Flüssigkeit, bei wenigen Kalorien, wenn es naturbelassen ist. Mit Zitrone und Minze wird es noch erfrischender. Es ist hervorragend nach Bewegung oder an heißen Tagen, anstelle von gezuckerten Sportgetränken.",
},
# ---------------- CHÁS / INFUSÕES (145-150) — LIVRES ----------------
{
 "nome": "Grüner Tee mit Zitrone und Ingwer",
 "hook": "Der Verbündete Nummer 1 beim Abnehmen: Grüner Tee bringt den Stoffwechsel in Schwung, und Zitrone und Ingwer geben noch einen Schub dazu.",
 "tempo": "8 Min.", "rende": "1 Tasse", "kcal_base": 5, "livre": True,
 "ings": ["240 ml Wasser", "1 TL grüner Tee (oder 1 Teebeutel)", "ein paar Ingwerscheiben", "Saft von ½ Zitrone"],
 "passos": [
   "Koche das Wasser auf und nimm den Topf vom Herd. Warte 1 Minute (zu heißes Wasser macht grünen Tee bitter).",
   "Gib den grünen Tee und die Ingwerscheiben dazu, decke alles ab und lass es 3 Minuten zugedeckt ziehen.",
   "Gieße alles durch ein Sieb, gib den Zitronensaft dazu und trinke den Tee warm. Du kannst ihn auch kalt über den Tag trinken."],
 "dica": "Grüner Tee ist eines der am besten untersuchten Lebensmittel beim Abnehmen: Er enthält Stoffe, die helfen, den Stoffwechsel anzuregen und Fett zu verbrennen. Mit Ingwer und Zitrone wird die Wirkung verstärkt. Ohne Zucker ist er ein freies Getränk, das du jeden Tag trinken kannst.",
},
{
 "nome": "Eisgekühlter Hibiskustee",
 "hook": "Rubinrot und leicht säuerlich, ist der Hibiskus dafür bekannt, beim Entwässern zu helfen — köstlich eisgekühlt bei Hitze.",
 "tempo": "10 Min. + Kühlschrank", "rende": "1 Krug", "kcal_base": 5, "livre": True,
 "ings": ["1 Liter Wasser", "2 EL getrocknete Hibiskusblüten (oder 2 Teebeutel)",
          "Zitronenscheiben", "Minzblätter", "Eiswürfel nach Geschmack"],
 "passos": [
   "Koche das Wasser auf und nimm den Topf vom Herd. Gib den Hibiskus dazu, decke alles ab und lass es 5 bis 7 Minuten zugedeckt ziehen.",
   "Gieße alles durch ein Sieb und lass es abkühlen. Stelle es in den Kühlschrank.",
   "Serviere den Tee schön kalt, mit Zitronenscheiben, Minze und Eiswürfeln."],
 "dica": "Hibiskustee ist dafür bekannt, Wassereinlagerungen (das Aufgeschwemmtsein) zu verringern, und ist reich an Antioxidantien. Eisgekühlt und ohne Zucker ist er ein erfrischendes, freies Getränk, hervorragend als Ersatz für Limonade und Fertigsäfte über den Tag.",
},
{
 "nome": "Kamillentee mit Zimt",
 "hook": "Warm und wohltuend, der Tee, der vor dem Schlafengehen beruhigt — und eine gute Nacht hilft ebenfalls beim Abnehmen.",
 "tempo": "8 Min.", "rende": "1 Tasse", "kcal_base": 5, "livre": True,
 "ings": ["240 ml Wasser", "1 EL Kamillenblüten (oder 1 Teebeutel)", "1 Zimtstange (oder 1 Prise gemahlener Zimt)"],
 "passos": [
   "Koche das Wasser auf und nimm den Topf vom Herd.",
   "Gib die Kamille und den Zimt dazu, decke alles ab und lass es 5 Minuten zugedeckt ziehen.",
   "Gieße alles durch ein Sieb und trinke den Tee warm, am besten abends vor dem Schlafengehen."],
 "dica": "Kamille beruhigt und hilft beim Entspannen, das verbessert den Schlaf. Gut zu schlafen ist ein Faktor, den viele beim Abnehmen vergessen: Schlecht durchschlafene Nächte steigern am nächsten Tag den Hunger und die Lust auf Süßes. Dieser Tee ist ein Abendritual, das die Diät unterstützt.",
},
{
 "nome": "Aufguss mit Ingwer, Zitrone und Zimt",
 "hook": "Ein wärmender, duftender Aufguss, der den Körper aufwärmt und dem Stoffwechsel den bekannten Anstoß gibt.",
 "tempo": "10 Min.", "rende": "1 große Tasse", "kcal_base": 8, "livre": True,
 "ings": ["300 ml Wasser", "mehrere Ingwerscheiben", "1 Zimtstange", "Saft von ½ Zitrone"],
 "passos": [
   "Koche das Wasser mit den Ingwerscheiben und der Zimtstange in einem kleinen Topf 5 Minuten bei kleiner Hitze.",
   "Nimm den Topf vom Herd, decke ihn ab und lass alles noch 3 Minuten ziehen.",
   "Gieße alles durch ein Sieb, gib den Zitronensaft dazu und trinke den Aufguss warm."],
 "dica": "Ingwer und Zimt wirken leicht wärmend, das heißt, sie helfen dem Körper, etwas mehr Energie zu verbrauchen. Es ist ein warmer, wohltuender Aufguss ohne Zucker, der an kalten Tagen guttut und dem Stoffwechsel diese zusätzliche Unterstützung gibt.",
},
{
 "nome": "Minztee mit Zitrone",
 "hook": "Frisch und gut für die Verdauung, beruhigt Minztee den Magen nach dem Essen — leicht und duftend.",
 "tempo": "8 Min.", "rende": "1 Tasse", "kcal_base": 4, "livre": True,
 "ings": ["240 ml Wasser", "1 Handvoll frische Minzblätter (oder 1 Teebeutel)", "Saft von ½ Zitrone"],
 "passos": [
   "Koche das Wasser auf und nimm den Topf vom Herd.",
   "Gib die Minzblätter dazu, decke alles ab und lass es 5 Minuten zugedeckt ziehen.",
   "Gieße alles durch ein Sieb, gib den Zitronensaft dazu und trinke den Tee warm oder kalt, am besten nach den Mahlzeiten."],
 "dica": "Minze hilft bei der Verdauung und verringert das Gefühl eines schweren Magens nach dem Essen. Ein Verdauungstee ohne Zucker nach den Mahlzeiten ist eine einfache Gewohnheit, die verhindert, dass du gleich danach Süßes naschst.",
},
{
 "nome": "Fencheltee",
 "hook": "Mild und von Natur aus süß, beruhigt Fenchel den Magen und verringert Blähungen — ein wohltuender Tee nach dem Essen.",
 "tempo": "8 Min.", "rende": "1 Tasse", "kcal_base": 4, "livre": True,
 "ings": ["240 ml Wasser", "1 TL Fenchelsamen — oder 1 Teebeutel"],
 "passos": [
   "Zerdrücke die Fenchelsamen leicht (so geben sie mehr Aroma ab).",
   "Koche das Wasser auf und nimm den Topf vom Herd. Gib den Fenchel dazu, decke alles ab und lass es 5 Minuten zugedeckt ziehen.",
   "Gieße alles durch ein Sieb und trinke den Tee warm, am besten nach den Mahlzeiten oder abends."],
 "dica": "Fenchel ist dafür bekannt, den Magen zu beruhigen und Blähungen sowie einen aufgeblähten Bauch zu verringern. Er ist von Natur aus süß und braucht keinen Zucker. Ein Verdauungstee, der wohltut und eine Mahlzeit auf leichte Weise abschließt.",
},
]
