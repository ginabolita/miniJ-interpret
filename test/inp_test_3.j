doble =: 2 * ]      NB. Funció que duplica
doble 7
doble 10 20 30      NB. Aplicació a llista

triple =: 3 * ]
triple 5

succ =: 1 + ]       NB. Successors
succ 9
succ 1 2 3 4 5

quadrat =: ] *: ]    NB. Quadrat d'un número
quadrat 8

suma =: +/          NB. Suma d'una llista
suma 1 2 3 4 5

prod =: */          NB. Producte d'una llista
prod 1 2 3 4 5

sumQuad =: +/ @: quadrat @: i.  NB. Suma dels quadrats dels primers n números
sumQuad 5           
