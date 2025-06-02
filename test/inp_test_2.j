NB. VARIABLE ASSIGNMENTS
a =: 5            NB. Resultat: 5
a
b =: 7            NB. Resultat: 7
b
c =: 10           NB. Resultat: 10
c
d =: _10          NB. Resultat: _10
d
arr1 =: 1 2 3 4   NB. Resultat: 1 2 3 4
arr1
arr2 =: 10 20 30  NB. Resultat: 10 20 30
arr2

NB. BINARY ARITHMETIC OPERATORS WITH VARIABLES
a + b            NB. Resultat: 12
c - 3            NB. Resultat: 7
3 - c * 5 + a    NB. Resultat: _97
6 * 4            NB. Resultat: 24
c * 2 % 4        NB. Resultat: 5
3 ^ b            NB. Resultat: 2187
2 | c + a        NB. Resultat: 1

NB. UNARY OPERATORS WITH VARIABLES
_a              NB. Resultat: _5
]d              NB. Resultat: _10
i.a             NB. Resultat: 0 1 2 3 4
#arr1           NB. Resultat: 4

NB. RELATIONAL OPERATORS WITH VARIABLES
b > a           NB. Resultat: 1
a > b           NB. Resultat: 0
c >= c          NB. Resultat: 1
b <= a          NB. Resultat: 0
a = 5           NB. Resultat: 1
a <> c          NB. Resultat: 1

NB. ARRAY OPERATIONS WITH VARIABLES
arr2 + 1 0 2 { arr1    NB. Resultat: 12 21 33
arr2 * 2               NB. Resultat: 20 40 60
a + 1 2 3              NB. Resultat: 6 7 8

NB. DOUBLE OPERATORS WITH VARIABLES
+: arr1               NB. Resultat: 2 4 6 8
*: arr1               NB. Resultat: 1 4 9 16
-: 10 3 2             NB. Resultat: 0 0 0
%: c * 2 + 4 2 3      NB. Resultat: 1 1 1
|: c	                 NB. Resultat: 0 
^: 2 3 2              NB. Resultat: 4 27 4

NB. FOLD OPERATORS WITH VARIABLES
+/ arr1               NB. Resultat: 10
*/ arr1               NB. Resultat: 24
-/ c               NB. Resultat:0
%/ c * 2 + 4 2 3      NB. Resultat: 4

NB. SPECIAL OPERATORS WITH VARIABLES
(0 1 2 { arr1) , 4 5  NB. Resultat: 1 2 3 4 5
1 0 1 # arr2          NB. Resultat: 10 30
1 0 { arr2         NB. Resultat: 20 10

NB. FLIP OPERATORS WITH VARIABLES
2 ^~ arr2             NB. Resultat: 100 400 900
0 1 2 { arr1 *~ 3   NB. Resultat: 3 6 9
2 %~ c                NB. Resultat: 5

e =: a + b * 2         NB. Resultat: 19
e
f =: arr2 + 5          NB. Resultat: 15 25 35
f
g =: 2 * f - arr2      NB. Resultat: 10 10 10
g
h =: +/ arr1 * 2       NB. Resultat: 20
h
i =: (#arr1) ^ 2       NB. Resultat: 16
i
j =: (g + 5) , (f - 5) NB. Resultat: 15 15 15 10 20 30
j
