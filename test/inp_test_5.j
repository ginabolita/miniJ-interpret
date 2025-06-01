NB. Llistes buides i casos límit
buit =: i.0
#buit        NB. Longitud d'una llista buida
un =: 5
dos =: 10
tres =: _15

NB. Funcions més complexes
abs =: ] * ((>:0) - 2 * (<:0))  NB. Valor absolut
abs 5        NB. 5
abs _7       NB. |-7| = 7

NB. Manipulació d'arrays
matriu =: 1 2 3 , 4 5 6 , 7 8 9
reshape =: [: (] $ [)  NB. Reshape matriu
3 3 reshape matriu    NB. Matriu 3x3

NB. Generació de sèries
suma_serie =: +/ @: i.
suma_serie 100   NB. Suma dels primers 100 enters

NB. Càlculs complexos
potencia =: ^
log =: ]
fibonacci =: [: (+/) [: (,&1) 1:  NB. Seqüència de Fibonacci
fib =: fibonacci ^ 10   NB. 10 primeres iteracions
fib