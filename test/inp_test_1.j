NB. BINARY ARITHMETIC OPERATORS
5 + 7            NB. Resultat: 12
10 - 3           NB. Resultat: 7
3 - 54           NB. Resultat: _51
6 * 4            NB. Resultat: 24
20 % 4           NB. Resultat: 5
27 ^ 3           NB. Resultat: 19683
2 | 5            NB. Resultat: 1

NB. UNARY OPERATORS
_10              NB. Resultat: -10
]5               NB. Resultat: 5
i.5              NB. Resultat: 0 1 2 3 4
# 1 2 3 4    NB. Resultat: 4

NB. RELATIONAL OPERATORS
2 > 1            NB. Resultat: 1
2 < 1            NB. Resultat: 0
2 >= 2           NB. Resultat: 1
3 <= 1           NB. Resultat: 0
5 = 5            NB. Resultat: 1
4 <> 4           NB. Resultat: 0

NB. ARRAY OPERATIONS
10 20 30 + 1 2 3        NB. Resultat: 11 22 33
10 20 30 * 2                NB. Resultat: 20 40 60
5 + 1 2 3                   NB. Resultat: 6 7 8

NB. DOUBLE OPERATORS
+: 1 2 3 4                  NB. Resultat: 2 4 6 8
*: 1 2 3 4                  NB. Resultat: 1 4 9 16
-: 10 3 2                    NB. Resultat: 0 0 0
%: 24 2 3                    NB. Resultat: 1 1 1
|: 10 3                       NB. Resultat: 0 0
^: 2 3 2                     NB. Resultat: 4 27 4

NB. FOLD OPERATORS
+/ 1 2 3 4                  NB. Resultat: 10
*/ 1 2 3 4                  NB. Resultat: 24
-/ 10 3 2                    NB. Resultat: 5
%/ 24 2 3                    NB. Resultat: 4

NB. SPECIAL OPERATORS
1 2 3 , 4 5              NB. Resultat: 1 2 3 4 5
1 0 1 # 10 20 30        NB. Resultat: 10 30
1 3 { 10 20 30 40       NB. Resultat: 20 40

NB. FLIP OPERATORS
2 ^~ 10 20 30               NB. Resultat: 100 400 900
1 2 3 *~ 3                  NB. Resultat: 3 6 9
2 %~ 10                         NB. Resultat: 5