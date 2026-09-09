# -*- coding: utf-8 -*-
"""BONUS 2 — PILATES PER LA PANCIA PIATTA. ITALIANO.

Traducao literal de `exercicios_pilates_en.py`. Convencoes em GLOSSARIO-TRADUCAO.md.
⛔ METRICO: `a few inches` -> `alcuni centimetri` (o pt/de/fr/es dizem todos
   centimetro) e `a hand's width above the floor` -> `un palmo da terra`
   (DE: `eine Handbreit`, ES: `un palmo`). ⚠️ Nenhum dos dois tem numero, entao
   a lente `IMPERIAL_VAZADO` NAO os pegaria — foram convertidos na leitura.
⛔ O campo `prompt` NAO e' replicado: a foto e' a mesma (fotos/NNN, sem texto).
"""

EXERCICIOS = [
{
 "nome": "Respirazione Pilates (accendere gli addominali)",
 "foco": "Imparare a contrarre il muscolo addominale profondo — la base di ogni esercizio.",
 "nivel": "Principiante", "series": "5 respiri", "tempo": "2 min",
 "hook": "Prima di ogni altra cosa, impara ad accendere gli addominali dall'interno — è questo che fa funzionare il Pilates e rende la tua pancia più soda.",
 "passos": [
   "Sdraiati sulla schiena, con le ginocchia piegate e i piedi appoggiati a terra, alla larghezza dei fianchi. Lascia le braccia lungo il corpo.",
   "Metti le mani sulla pancia. Inspira dal naso, riempiendo la pancia come un palloncino.",
   "Espira lentamente dalla bocca e, allo stesso tempo, tira l'ombelico verso la colonna, come se stessi chiudendo la cerniera di un pantalone stretto.",
   "Mantieni quella contrazione per 3 secondi, sentendo la pancia soda, e rilassa.",
   "Ripeti 5 volte, espirando sempre e tirando dentro l'ombelico."],
 "respiracao": "Inspira dal naso riempiendo la pancia; espira dalla bocca svuotandola e contraendo gli addominali. Non trattenere mai il respiro.",
 "dica": "Questo «tirare dentro l'ombelico» è il segreto del Pilates. Userai la stessa contrazione in tutti gli altri esercizi — è ciò che lavora il muscolo più profondo della pancia, quello che tiene tutto al suo posto e assottiglia la vita.",
},
{
 "nome": "Basculamento del bacino",
 "foco": "Scaldare la colonna e accendere la parte bassa della pancia.",
 "nivel": "Principiante", "series": "2 serie da 10", "tempo": "3 min",
 "hook": "Un movimento piccolo e delicato che scioglie la zona lombare e sveglia la parte bassa della pancia.",
 "passos": [
   "Resta sdraiata sulla schiena, ginocchia piegate e piedi a terra.",
   "Espira e tira dentro l'ombelico, ruotando delicatamente il bacino all'indietro, così che la zona lombare si appoggi completamente a terra.",
   "Inspira e torna lentamente, lasciando un piccolo spazio tra la zona lombare e il pavimento.",
   "Fai il movimento molto lentamente, come se stessi disegnando con i fianchi, senza forzare.",
   "Ripeti 10 volte, riposa e fai un'altra serie da 10."],
 "respiracao": "Espira mentre la zona lombare si appoggia a terra; inspira mentre torni indietro. Il movimento segue il respiro.",
 "dica": "È un riscaldamento perfetto per chi ha la zona lombare sensibile. Il movimento è corto di proposito — a comandare è la contrazione della pancia, non la forza della schiena.",
},
{
 "nome": "The Hundred",
 "foco": "L'esercizio di Pilates più famoso per tutto l'addome.",
 "nivel": "Intermedio", "series": "1 serie (conta fino a 100)", "tempo": "3 min",
 "hook": "Il classico che scalda tutto il corpo e fa bruciare gli addominali — con delicatezza, ma brucia.",
 "passos": [
   "Sdraiati sulla schiena, piega le ginocchia e solleva le gambe finché non sono piegate a 90 gradi (stinchi paralleli al pavimento), come se fossi seduta su una sedia rovesciata.",
   "Espira, tira dentro l'ombelico e solleva leggermente la testa e le spalle da terra, guardando la pancia. Distendi le braccia dritte lungo il corpo, a un palmo da terra.",
   "Inizia a battere le braccia su e giù, con movimenti corti e decisi, come se stessi schiaffeggiando l'acqua.",
   "Conta cinque battute mentre inspiri e cinque mentre espiri.",
   "Continua finché non arrivi a 100 battute (o fermati prima se ti stanchi). Poi abbassa la testa e le gambe e riposa."],
 "respiracao": "Inspira per 5 battute ed espira per 5 battute, senza fermare il movimento delle braccia.",
 "dica": "Versione più facile: tieni i piedi a terra e solleva solo la testa e le spalle. Inizia con 30 o 50 battute e arriva a 100 col tempo.",
},
{
 "nome": "Sollevamento alternato delle gambe",
 "foco": "La parte bassa della pancia e il controllo del movimento.",
 "nivel": "Principiante", "series": "2 serie da 12", "tempo": "3 min",
 "hook": "Un movimento controllato che lavora esattamente quella parte bassa della pancia, la più ostinata.",
 "passos": [
   "Sdraiati sulla schiena, ginocchia piegate e piedi appoggiati a terra. Tieni la zona lombare aderente al pavimento per tutto il tempo.",
   "Espira, tira dentro l'ombelico e stacca un piede da terra, portando il ginocchio verso la pancia, finché la coscia non è verticale (90 gradi).",
   "Inspira e abbassa lentamente il piede finché non tocca di nuovo terra, con controllo.",
   "Alterna: adesso solleva l'altra gamba allo stesso modo.",
   "Fai 12 ripetizioni per gamba, tenendo la pancia contratta per tutto il tempo. Riposa e ripeti la serie."],
 "respiracao": "Espira mentre la gamba sale; inspira mentre scende. Gli addominali restano sodi per tutto il tempo.",
 "dica": "Quello che conta non è la velocità, è il controllo: più lentamente abbassi la gamba, più lavora la pancia. Se senti la zona lombare inarcarsi e staccarsi da terra, solleva meno la gamba.",
},
{
 "nome": "Crunch corto (sollevamento del busto)",
 "foco": "La parte alta e centrale della pancia.",
 "nivel": "Principiante", "series": "3 serie da 12", "tempo": "4 min",
 "hook": "Il solito crunch, ma fatto con il controllo del Pilates — sale poco e lavora tanto.",
 "passos": [
   "Sdraiati sulla schiena, ginocchia piegate e piedi a terra. Incrocia le braccia sul petto oppure appoggia le mani dietro la testa, senza tirare il collo.",
   "Espira, tira dentro l'ombelico e arrotola il busto verso l'alto, sollevando la testa e le spalle da terra, come se avvicinassi le costole ai fianchi.",
   "Sali solo finché le punte delle scapole non lasciano il pavimento (non serve tirarti su a sedere). Mantieni 1 secondo in alto.",
   "Inspira e scendi lentamente, srotolando la colonna a terra, una vertebra alla volta.",
   "Ripeti 12 volte, riposa e fai 3 serie in tutto."],
 "respiracao": "Espira mentre sali (è lì che la pancia si contrae di più); inspira mentre scendi.",
 "dica": "Non tirarti il collo con le mani — gli occhi guardano la pancia e il mento resta staccato dal petto, con lo spazio di un'arancia. A sollevare il corpo sono gli addominali, non il collo.",
},
{
 "nome": "Plank frontale",
 "foco": "Tutto l'addome, la zona lombare e la postura — l'esercizio più completo per il core.",
 "nivel": "Intermedio", "series": "3 volte tenendo 20-40 s", "tempo": "4 min",
 "hook": "Fermo, ma potente: tenere il plank rafforza tutta la pancia e la schiena allo stesso tempo.",
 "passos": [
   "Sdraiati a pancia in giù e appoggia gli avambracci a terra, con i gomiti sotto le spalle. Le mani restano davanti.",
   "Distendi le gambe all'indietro e appoggia le punte dei piedi a terra.",
   "Espira, tira dentro l'ombelico e solleva il corpo, tenendolo dritto come una tavola, dai talloni alla testa.",
   "Tieni i fianchi in linea con il corpo — non sollevati come una collina, e non ciondolanti verso il pavimento. Guarda a terra per non forzare il collo.",
   "Mantieni per 20-40 secondi, respirando normalmente. Scendi, riposa e ripeti 3 volte."],
 "respiracao": "Continua a respirare normalmente e lentamente per tutta la durata del plank. Non trattenere il respiro.",
 "dica": "Versione più facile: appoggia le ginocchia a terra (plank sulle ginocchia). Inizia tenendo 15 secondi e aumenta poco a poco. Se ti fa male la zona lombare, è il segno che i fianchi sono scesi — sollevali un po'.",
},
{
 "nome": "Plank laterale",
 "foco": "I muscoli laterali della pancia (obliqui) — assottiglia la vita.",
 "nivel": "Intermedio", "series": "2 volte per lato, 15-30 s", "tempo": "4 min",
 "hook": "È l'esercizio che disegna il lato degli addominali e definisce la vita.",
 "passos": [
   "Sdraiati su un fianco, con il corpo dritto. Appoggia a terra l'avambraccio sotto, con il gomito sotto la spalla.",
   "Sovrapponi una gamba all'altra (un piede sopra l'altro).",
   "Espira, tira dentro l'ombelico e solleva i fianchi da terra, tenendo il corpo dritto e in appoggio solo sull'avambraccio e sul lato del piede.",
   "Distendi il braccio di sopra verso il soffitto oppure appoggia la mano sulla vita. Mantieni per 15-30 secondi.",
   "Scendi con controllo, girati sull'altro lato e ripeti. Fallo 2 volte per lato."],
 "respiracao": "Respira normalmente e lentamente mentre mantieni la posizione.",
 "dica": "Versione più facile: piega le ginocchia e appoggia a terra la parte bassa delle gambe, sollevando solo i fianchi. Qui è la vita che lavora di più — tienila soda.",
},
{
 "nome": "Ponte per i glutei",
 "foco": "Glutei, parte posteriore delle cosce e addominali — e allevia la zona lombare.",
 "nivel": "Principiante", "series": "3 serie da 12", "tempo": "3 min",
 "hook": "Solleva il sedere, rafforza gli addominali da dietro e migliora anche la tua postura.",
 "passos": [
   "Sdraiati sulla schiena, ginocchia piegate e piedi appoggiati a terra, alla larghezza dei fianchi. Braccia lungo il corpo.",
   "Espira, tira dentro l'ombelico e solleva i fianchi da terra, contraendo i glutei, finché il corpo non forma una linea dritta dalle ginocchia alle spalle.",
   "Mantieni per 2 secondi in alto, tenendo i glutei e la pancia sodi.",
   "Inspira e abbassa lentamente i fianchi, srotolando la colonna a terra, una vertebra alla volta.",
   "Ripeti 12 volte, fai 3 serie."],
 "respiracao": "Espira mentre i fianchi salgono; inspira mentre scendono.",
 "dica": "Sali contraendo forte i glutei, non spingendo con la zona lombare. È uno dei pochi esercizi che rafforza la pancia e allo stesso tempo allevia il mal di schiena — ottimo per chi sta seduta tutto il giorno.",
},
{
 "nome": "Roll Up",
 "foco": "Tutto l'addome e la flessibilità della colonna.",
 "nivel": "Intermedio", "series": "2 serie da 8", "tempo": "4 min",
 "hook": "Tirarsi su e sdraiarsi srotolando lentamente la colonna — sembra semplice, ma sono gli addominali a fare tutto il lavoro.",
 "passos": [
   "Sdraiati sulla schiena con le gambe distese e le braccia distese all'indietro, sopra la testa.",
   "Inspira e porta le braccia in avanti, puntando verso il soffitto.",
   "Espira, tira dentro l'ombelico e inizia a tirarti su molto lentamente, srotolando la colonna: prima la testa, poi le spalle, poi la schiena, finché non sei seduta e arrivi ai piedi con le mani.",
   "Inspira in alto e, mentre espiri, scendi allo stesso modo lentamente, srotolando la colonna a terra, una vertebra alla volta.",
   "Ripeti 8 volte, con tutto il controllo che riesci. Fai 2 serie."],
 "respiracao": "Espira mentre sali e mentre scendi (è lì che la pancia lavora); inspira nelle pause.",
 "dica": "Versione più facile: piega un po' le ginocchia e, se ti serve, datti una piccola spinta con le braccia. Quello che conta è salire e scendere lentamente — il lavoro lo fa la pancia, non il collo o le braccia.",
},
{
 "nome": "Bicicletta a terra",
 "foco": "Gli obliqui (i lati della pancia) e tutto l'addome.",
 "nivel": "Intermedio", "series": "3 serie da 20 (10 per lato)", "tempo": "4 min",
 "hook": "Il movimento della pedalata che disegna i fianchi della pancia e alza un po' il battito.",
 "passos": [
   "Sdraiati sulla schiena, mani dietro la testa (senza tirare il collo). Solleva le gambe con le ginocchia piegate a 90 gradi.",
   "Espira, tira dentro l'ombelico e solleva la testa e le spalle da terra.",
   "Ruota il busto portando il gomito destro verso il ginocchio sinistro, mentre distendi la gamba destra in avanti.",
   "Torna al centro e fai l'altro lato: gomito sinistro verso il ginocchio destro, distendendo la gamba sinistra.",
   "Continua ad alternare, come se stessi pedalando lentamente in bicicletta. Fai 20 ripetizioni in tutto (10 per lato), 3 serie."],
 "respiracao": "Espira a ogni rotazione del busto; inspira mentre passi dal centro.",
 "dica": "Fallo lentamente e con controllo, senza fretta — è la rotazione del busto a lavorare il lato della pancia. Più lontano distendi la gamba, più diventa difficile ed efficace.",
},
{
 "nome": "Superman (estensione della schiena)",
 "foco": "Schiena e postura — riequilibra il corpo e fa sembrare la pancia più piatta in piedi.",
 "nivel": "Principiante", "series": "3 serie da 10", "tempo": "3 min",
 "hook": "Dopo tutti quei crunch, questo rafforza la schiena e migliora la postura — il che fa già sembrare la pancia più piatta.",
 "passos": [
   "Sdraiati a pancia in giù, con le braccia distese in avanti e le gambe distese all'indietro.",
   "Espira, tira leggermente dentro l'ombelico e solleva insieme le braccia, il petto e le gambe da terra, di alcuni centimetri, come Superman in volo.",
   "Mantieni per 2 secondi in alto, guardando a terra per non forzare il collo.",
   "Inspira e scendi lentamente, rilassandoti.",
   "Ripeti 10 volte, fai 3 serie."],
 "respiracao": "Espira mentre sollevi; inspira mentre scendi. Un movimento fluido, senza strappi.",
 "dica": "Non serve sollevarti tanto — pochi centimetri lavorano già la schiena. Rafforzare la schiena è essenziale: una schiena forte ti tiene dritta, e una buona postura da sola fa già sembrare la pancia più piccola.",
},
{
 "nome": "Allungamento finale",
 "foco": "Rilassare la colonna e gli addominali dopo l'allenamento.",
 "nivel": "Tutti i livelli", "series": "Tieni 30 s ciascuno", "tempo": "3 min",
 "hook": "Per finire, un bell'allungamento che rilassa la pancia e la schiena che hai appena lavorato.",
 "passos": [
   "Mettiti a quattro zampe (mani e ginocchia a terra). Siediti indietro sui talloni e distendi le braccia in avanti, appoggiando il busto sulle cosce (posizione del riposo). Appoggia la fronte a terra e respira profondamente per 30 secondi.",
   "Torna sdraiata sulla schiena. Abbraccia un ginocchio alla volta, tirandolo verso il petto, e mantieni per 30 secondi per lato — questo rilassa la zona lombare.",
   "Infine, sdraiata sulla schiena con le braccia aperte, lascia cadere lentamente entrambe le ginocchia da un lato e poi dall'altro, ruotando dolcemente la colonna, 30 secondi per lato.",
   "Respira profondamente per tutta la durata dell'allungamento, senza fretta.",
   "Alzati lentamente quando hai finito."],
 "respiracao": "Respira profondamente e lentamente, espirando a ogni allungamento e lasciando che il corpo si rilassi ancora un po'.",
 "dica": "Non saltare mai l'allungamento: rilassa i muscoli che hanno lavorato, previene i dolori del giorno dopo e migliora la flessibilità. È il momento per sentire il tuo corpo e chiudere l'allenamento in pace.",
},
]
