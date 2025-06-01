1 2 3 4 5    NB. Llista de números
nums =: 10 20 30 40 50
nums
nums + 5      NB. Suma escalar a llista
nums * 2      NB. Multiplicació escalar
nums1 =: 1 2 3 4 5
nums + nums1   NB. Suma entre llistes
nums , nums1  NB. Concatenació
#nums         NB. Longitud
i.10          NB. Seqüència 0..9
1 0 1 0 1 # nums  NB. Filtratge
2 0 4 1 { nums  NB. Indexació
+/ nums        NB. Fold suma
*/ nums1        NB. Fold multiplicació
+: nums          NB. Duplicar suma
-: nums          NB. Duplicar resta