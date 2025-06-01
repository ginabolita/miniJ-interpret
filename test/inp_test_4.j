NB. Operadors conmutats
3 +~ 5        NB. 5+3
10 -~ 3       NB. 3-10
a =: 2 4 6 8 10
b =: 10 8 6 4 2
a >~ b        NB. b>a
a =~ b        NB. b=a
NB. Casos amb indexació i filtrat
indices =: 3 1 0
valors =: 100 200 300 400 500
valors{indices}  NB. Indexació complexa
filtres =: 1 0 1 0 1
valors # filtres  NB. Filtrat complex
NB. Combinacions d'operadors
quants =: #i.10   NB. Longitud d'una seqüència
quants
dobleQuants =: doble quants  NB. Funció amb funció
dobleQuants
NB. Funció recursiva
fact =: */ @: i. @: succ  NB. Factorial (producte dels números de 1 a n)
fact 5       NB. 5! = 1*2*3*4*5 = 120
NB. Operador ternari
maxim =: ((>~ *: ]) + (<~ *: [))  NB. Retorna el màxim de dos valors
maxim 7 12   NB. 12