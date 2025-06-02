# Intèrpret miniJ - Pràctica de Llenguatges de Programació

---

## Universitat Politècnica de Catalunya
### Llenguatges de Programació

[Gina Escofet González](gina.escofet@estudiantat.upc.edu)

---

## **Ús**
Per compilar i executar l'intèrpret amb els fitxers de prova:
```
make
python3 g.py ./test/inp_test_[1-3].j > output.out
```
---

## **Estructura i Decisions**

**Components Principals**
- **g.py**: Classe que executa el main.
- **g.g4**: Gramàtica ANTLR4.
- **evalVisitor.py**: La classe central que hereta de gVisitor i implementa la lògica d'avaluació.
- **utils.py**: Funcions auxiliars que encapsulen la lògica de les operacions unàries i binàries.
- **./test**: Jocs de prova comprovant la lògica de l'intèrpret.

---

**Modularitat i Principi de Responsabilitat Única**

El disseny del projecte segueix el principi de **modularitat**, separant la lògica d’avaluació (evalVisitor) de la lògica d’operacions bàsiques (utils.py), a part de la definició de la gramàtica (g.g4). Cada funció té una única responsabilitat.

La classe `evalVisitor` aplica el **principi de responsabilitat única**: cada mètode s’encarrega d’una tasca concreta (avaluar una assignació, una expressió, una funció, etc.), i la gestió de l’estat es centralitza en el diccionari d’instància `diccionari`. Aquesta organització permet que el codi sigui més llegible, fàcil de depurar i de modificar sense risc d’efectes col·laterals.

---

**Justificació de les Decissions**

- **Diccionari unificat:** S’ha optat per un únic diccionari per gestionar variables i funcions, simplificant la resolució de noms i evitant duplicació de lògica. La principal distinció entre variables i funcions és el context en que s'utilitzen, per tant, es tracten en temps d'execució i no a la gramàtica.
- **Gestió d’errors:** L’ús de try-except a cada mètode garanteix que els errors es gestionen localment millorant la robustesa de l’intèrpret.
- **Extensibilitat:** L’estructura modular i la separació de responsabilitats permeten afegir fàcilment nous operadors o funcionalitats sense modificar la base del sistema.
- **Claredat i mantenibilitat:** L’ús de docstrings i noms descriptius facilita la comprensió del codi per tercers i per a la seva pròpia evolució futura.

--- 

**Avaluació d'Expressions i Funcions**

L'avaluació es realitza amb una lògica de stack, inspirat en la lògica de calculadores postfixes de l'exercici de Haskell. Aquesta aproximació permet:

- Gestionar eficientment operadors unaris i binaris.
- Simplificar la resolució de la precedència d'operadors.
- Facilitar l'avaluació recursiva i la composició de funcions.

He definit una funció `evalua_amb_pila` que fa ús de dos stacks `op_stack` i `val_stack` per anar operant segons el tipus d'operadors.

**Gestió d'Errors**
S'ha implementat una estratègia de gestió d'errors que utilitza try-except per a capturar i informar d'excepcions sense provocar la terminació abrupta de l'intèrpret. Proporciona missatges d'error descriptius per facilitar la depuració.

---
## Conclusions

**Composició de Funcions \@\:**

El principal repte per mi ha estat la correcta expansió i avaluació de funcions composades i anidades, les que utilitzen l'operador '\@\:'.

**Solució:** S'ha optat per una resolució recursiva de les funcions en temps d'execució dins de `visitFuncDef` i `visitFunction`, assegurant que cada component de la funció composada s'avalua en l'ordre correcte i que les subfuncions es resolen a les seves definicions d'operadors.
