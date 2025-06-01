# Intèrpret miniJ - LP Pràctica
---
## Universitat Politècnica de Catalunya
### Llenguatges de Programació


Autora: Gina Escofet González : [gina.escofet@estudiantat.upc.edu](gina.escofet@estudiantat.upc.edu)


---
**Ús**
```
make
python3 g.py ./test/inp_test_[1-5].j > output.out
cmp out_test_[1-5].out
```

**Estructura de l'intèrpret**
L'intèrpret es basa en el patró visitor generat per ANTLR4, però amb les següents modificacions:

- Classe EvalVisitor: Implementa tots els mètodes necessaris per avaluar els diferents nodes de l'AST
- Classe utils.py: Classe auxiliar per guardar la lògica de les operacions.
- Diccionari self.symbols: Emmagatzema variables i funcions definides durant l'execució
- Sistema de piles: Per avaluar expressions i funcions utilitzo dues piles:
		- pila_ops: Per guardar operadors
		- pila_vals: Per guardar valors o llistes
---
**Decisions d'implementació**
1. **Gestió de variables i funcions**
He decidit utilitzar un únic diccionari self.symbols per emmagatzemar tant variables com funcions. Això simplifica el codi però requereix comprovar el tipus quan es processa un símbol:
```
if nom in self.symbols:
    if isinstance(self.symbols[nom], (list, np.ndarray)):
        # És una funció
    else:
        # És una variable
```

2. **Avaluació d'expressions i funcions**
Per avaluar expressions i funcions, he implementat un sistema basat en piles inspirat en l'exercici de Haskell fet al laboratori de la calculadora postfixa.
- Permet treballar amb operadors unaris i binaris fàcilment
- Simplifica la gestió d'operadors amb prioritat
- Facilita l'avaluació recursiva de subfuncions

Permet treballar amb operadors unaris i binaris fàcilment
Simplifica la gestió d'operadors amb prioritat
Facilita l'avaluació recursiva de subfuncions

La funció avalua_piles és el cor d'aquest mecanisme, processant operadors i valors segons un ordre determinat.

3. **Gestió d'errors**
He implementat un sistema de gestió d'errors que:

- Detecta i informa d'errors sintàctics
- Ignora (amb comportament indefinit) errors semàntics, de tipus i d'execució
- Utilitza blocs try-except per evitar que el programa peti completament
- Mostra missatges d'error descriptius

```
try:
    # Codi que pot fallar
except Exception as e:
    print(f"Error en operació: {str(e)}")
    raise ValueError("Missatge d'error específic")
```

4. **Expansió de funcions**
La implementació de la composició de funcions (\@\:) m'ha costat implementarla. Finalment he decidit:

- Expandir les funcions recursivament en temps d'execució
- Processar operadors especials com ] específicament
- Mantenir l'ordre correcte d'avaluació per a operacions compostes
---
**Principals dificultats i solucions**
**Problema amb la composició**
Un dels principals problemes ha estat la correcta expansió de funcions composades com:
```
inc =: 1 + ]
test =: +/ @: inc @: i.
```
**Solució:** Implementar una expansió recursiva més completa, detectant específicament subfuncions i operadors especials com ].

**Gestió d'errors**
Un altre repte ha estat gestionar els errors sense que el programa peti, però informant adequadament quan hi ha problemes sintàctics.

**Solució:** Utilitzar blocs try-except a cada mètode visitor i distingir entre errors sintàctics (reportats) i errors d'execució (amb comportament indefinit).
