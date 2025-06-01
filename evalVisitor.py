import numpy as np
from antlr4 import *
from gParser import gParser
from gVisitor import gVisitor
from utils import *


class EvalVisitor(gVisitor):

    def __init__(self):
        # Diccionari pels símbols i variables
        self.symbols = {}
        # print("Inicialitzat el visitor... a veure si funciona")

    def visitRoot(self, ctx):
        try:
            resultats = []
            for i in range(ctx.getChildCount()):
                fill = ctx.getChild(i)
                if not isinstance(fill, TerminalNode):
                    try:
                        resultat = self.visit(fill)
                        if resultat is not None:
                            resultats.append(resultat)
                            # Imprimim el resultat segons si és llista o no
                            if isinstance(resultat, list) or isinstance(resultat, np.ndarray):
                                valors_enters = [int(x) for x in resultat]
                                format_text = " ".join('_' + str(abs(x)) if x < 0 else str(x)
                                                    for x in valors_enters)
                                print(format_text)
                            else:
                                print(int(round(resultat)))
                    except Exception as e:
                        # Un error en un fill no hauria d'aturar tota l'execució
                        print(f"Error sintàctic al node {i}: {str(e)}")
            return resultats
        except Exception as e:
            print(f"Error greu al visitRoot: {str(e)}")
            return []

    def visitParentesis(self, ctx):
        try:
            # Simplement retornem el valor de l'expressió dins els parèntesis
            return self.visit(ctx.expr())
        except Exception as e:
            print(f"Error als parèntesis: {str(e)}")
            raise ValueError("Estructura de parèntesis incorrecta")

    def visitExpressio(self, ctx):
        try:
            # Avaluem una expressió normal
            return self.visit(ctx.expr())
        except Exception as e:
            print(f"Error en expressió: {str(e)}")
            raise ValueError("Expressió mal formada")

    def visitLlista(self, ctx):
        try:
            # Creem una llista buida i l'omplim amb els valors
            nums = []
            for n in ctx.numlist().NUM():
                text = n.getText()
                try:
                    if text.startswith('_'):
                        nums.append(-int(text[1:]))  # Números negatius
                    else:
                        nums.append(int(text))  # Números positius
                except ValueError:
                    print(f"'{text}' no és un número vàlid")
            return nums
        except Exception as e:
            print(f"Error a la llista: {str(e)}")
            raise ValueError("Format de llista incorrecte")

    def visitBinari(self, ctx):
        try:
            # Obtenim operands i operador
            esq = self.visit(ctx.expr(0))
            dre = self.visit(ctx.expr(1))
            op = ctx.getChild(1).getText().strip('~')
            
            # Comprovacions de seguretat
            if esq is None:
                print(f"Problema: operand esquerre és None a '{op}'")
                raise ValueError(f"Error a l'operació {op}: l'operand esquerre no és vàlid")
            if dre is None:
                print(f"Problema: operand dret és None a '{op}'")
                raise ValueError(f"Error a l'operació {op}: l'operand dret no és vàlid")

            # Intercanviem operands si l'operador té '~'
            if '~' in ctx.getChild(1).getText():
                esq, dre = dre, esq

            # Fem l'operació
            return apply_binary_operation(op, esq, dre)
        except Exception as e:
            if "Error a l'operació" in str(e):
                raise e  # Re-llançar errors específics
            print(f"Error en operació binària: {str(e)}")
            raise ValueError("Problema amb l'operador binari o els seus operands")

    def visitUnari(self, ctx):
        try:
            # Obtenim l'operador unari
            if ctx.OPUNARI():
                op = ctx.OPUNARI().getText()
            else:
                op = ctx.getChild(0).getText()

            # Obtenim l'expressió
            expr = self.visit(ctx.expr())
            if expr is None:
                print(f"Error: expressió nul·la per operador unari '{op}'")
                raise ValueError(f"L'expressió per l'operador {op} no és vàlida")
                
            # Apliquem l'operació
            return apply_unary_operation(op, expr)
        except Exception as e:
            print(f"Error amb operador unari: {str(e)}")
            raise ValueError("Problema amb l'operador unari o el seu operand")

    def visitAssignacio(self, ctx):
        try:
            # Obtenim nom i valor
            nom = ctx.ID().getText()
            valor = self.visit(ctx.expr())
            
            # Comprovacions bàsiques
            if valor is None:
                print(f"No es pot assignar None a '{nom}'")
                raise ValueError(f"Error: valor nul per assignar a {nom}")
                
            # Si és una llista o array, la convertim a numpy.array
            if isinstance(valor, list) or isinstance(valor, np.ndarray):
                valor = np.array(valor)

            # Guardem el valor al diccionari
            self.symbols[nom] = valor
        except Exception as e:
            print(f"Error en assignació: {str(e)}")
            raise ValueError(f"Problema amb l'assignació a {nom}")

    def visitId(self, ctx):
        try:
            # Obtenim el nom de la variable
            nom = ctx.ID().getText()
            
            # Comprovem si existeix
            if nom in self.symbols:
                return self.symbols[nom]
            else:
                print(f"Variable '{nom}' no definida")
                raise ValueError(f"Error: la variable {nom} no existeix")
        except Exception as e:
            print(f"Error accedint a variable: {str(e)}")
            raise ValueError(f"Problema accedint a la variable {nom}")

    def visitFuncDef(self, ctx):
        try:
            # Obtenim el nom de la funció
            nom = ctx.ID().getText()
            funcDef = ctx.funcDefinition()

            # Llista per guardar els operadors
            ops = []
            
            # Processem cada element de la definició
            for i in range(funcDef.getChildCount()):
                try:
                    text_fill = funcDef.getChild(i).getText()
                    # Només processem elements que no són el delimitador
                    if text_fill != '@:':
                        if text_fill in self.symbols and isinstance(self.symbols[text_fill], list):
                            # Si és una referència a una funció ja definida
                            ops_func = self.symbols[text_fill]
                            # print(f"[D]: Resolved function '{text_fill}' to its definition: {ops_func}")
                            
                            # Afegim els operadors de la subfunció
                            if len(ops) == 1:
                                ops.append(ops_func[0])
                            else:
                                ops.extend(ops_func)
                        else:
                            ops.append(text_fill)
                except Exception as e:
                    print(f"Error processant element de la funció: {str(e)}")
                    # Continuem amb el següent element
            
            # Guardem la funció al diccionari
            self.symbols[nom] = np.array(ops)
            # print(f"[D]: Stored function '{nom}' with operators: {self.symbols}")
        except Exception as e:
            print(f"Error definint funció: {str(e)}")
            raise ValueError(f"Problema amb la definició de la funció {nom}")

    def visitFunction(self, ctx):
        try:
            # Nom de la funció i comprovació existència
            nom_funcio = ctx.ID().getText()
            if nom_funcio not in self.symbols:
                print(f"La funció '{nom_funcio}' no existeix!")
                raise ValueError(f"Error: funció {nom_funcio} no definida")

            # Obtenim la definició
            definicio = self.symbols[nom_funcio]
            # print(f"[DEBUG]: Definició trobada per '{nom_funcio}': {definicio}")

            # Inicialitzem piles
            pila_ops = []
            pila_vals = []

            # Expandim la funció amb control d'errors
            for operador in definicio:
                try:
                    # Si és una altra funció
                    if operador in self.symbols and isinstance(self.symbols[operador], (np.ndarray, list)):
                        # Cas de funció dins funció
                        funcio_interna = self.symbols[operador]
                        # print(f"[DEBUG]: Expandint subfunció '{operador}': {funcio_interna}")

                        # Processem cada element de la subfunció
                        for op_intern in funcio_interna:
                            try:
                                # Intentem veure si és un número
                                if isinstance(op_intern, str) and op_intern.startswith('_'):
                                    valor = -int(op_intern[1:])
                                    pila_vals.append(valor)
                                elif isinstance(op_intern, str) and op_intern.isdigit():
                                    valor = int(op_intern)
                                    pila_vals.append(valor)
                                elif op_intern != '@:':
                                    pila_ops.append(op_intern)
                            except ValueError:
                                # Si no és un número, afegim com a operador
                                if op_intern != '@:':
                                    pila_ops.append(op_intern)
                    else:
                        # Cas element normal
                        try:
                            # Mirem si és un número
                            if isinstance(operador, str) and operador.startswith('_'):
                                valor = -int(operador[1:])
                                pila_vals.append(valor)
                            elif isinstance(operador, str) and operador.isdigit():
                                valor = int(operador)
                                pila_vals.append(valor)
                            elif operador == '@:':
                                # Ignorem el delimitador
                                pass
                            elif operador in UNARY_OPERATORS or operador in BINARY_OPERATORS:
                                pila_ops.append(operador)
                            else:
                                # Podria ser variable o funció
                                # print(f"[DEBUG]: Element desconegut '{operador}', afegit a pila_ops")
                                pila_ops.append(operador)
                        except ValueError:
                            # Si falla la conversió a número
                            if operador != '@:':
                                pila_ops.append(operador)
                except Exception as e:
                    print(f"Error expandint operador '{operador}': {str(e)}")
                    # Seguim amb el següent operador

            # Recollim els arguments
            llista_args = []
            for i in range(1, ctx.getChildCount()):
                try:
                    fill = ctx.getChild(i)
                    if not isinstance(fill, TerminalNode):
                        arg = self.visit(fill)
                        if arg is not None:
                            llista_args.append(arg)
                except Exception as e:
                    print(f"Error processant argument: {str(e)}")
                    # Seguim amb el següent argument

            # Afegim arguments a la pila de valors
            for arg in llista_args:
                pila_vals.append(arg)

            # print(f"[DEBUG]: Piles inicials - Operadors: {pila_ops}, Valors: {pila_vals}")

            # Avaluem l'expressió
            return self.avalua_piles(pila_ops, pila_vals)
        
        except Exception as e:
            print(f"Error executant funció '{nom_funcio}': {str(e)}")
            raise ValueError(f"Problema en l'execució de la funció {nom_funcio}")

    def avalua_piles(self, pila_ops, pila_vals):
        try:
            # Fem còpies per evitar modificar les originals
            ops = pila_ops.copy() if pila_ops else []
            vals = pila_vals.copy() if pila_vals else []
            
            # Processem els operadors
            while ops:
                try:
                    operador_actual = ops.pop()

                    # Cas 1: operador unari
                    if operador_actual in UNARY_OPERATORS:
                        if not vals:
                            print(f"No hi ha prou valors per l'operació '{operador_actual}'")
                            raise ValueError(f"Error: falten operands per {operador_actual}")

                        valor = vals.pop()
                        try:
                            resultat = apply_unary_operation(operador_actual, valor)
                            vals.append(resultat)
                        except Exception as e:
                            print(f"Error aplicant operador '{operador_actual}': {str(e)}")
                            raise ValueError(f"Error en operació unària {operador_actual}")

                    # Cas 2: operador binari
                    elif operador_actual in BINARY_OPERATORS:
                        if len(vals) < 2:
                            print(f"Falten operands per '{operador_actual}'")
                            raise ValueError(f"Error: falten operands per {operador_actual}")

                        dreta = vals.pop()
                        esquerra = vals.pop()

                        try:
                            resultat = apply_binary_operation(operador_actual, esquerra, dreta)
                            vals.append(resultat)
                        except Exception as e:
                            print(f"Error en operació binària '{operador_actual}': {str(e)}")
                            raise ValueError(f"Error en operació binària {operador_actual}")

                    # Cas 3: valor literal o variable
                    else:
                        try:
                            # Provem si és un número
                            if isinstance(operador_actual, str) and operador_actual.startswith('_'):
                                val_num = -int(operador_actual[1:])
                                vals.insert(0, val_num)
                            elif isinstance(operador_actual, str) and operador_actual.isdigit():
                                val_num = int(operador_actual)
                                vals.insert(0, val_num)
                            elif operador_actual in self.symbols:
                                # És una variable
                                valor_var = self.symbols[operador_actual]
                                vals.insert(0, valor_var)
                            else:
                                print(f"No entenc què és '{operador_actual}'")
                                raise ValueError(f"Operador o valor desconegut: {operador_actual}")
                        except ValueError as ve:
                            if "Operador o valor desconegut" in str(ve):
                                raise ve  # Re-llançar errors d'operadors desconeguts
                            # Si és un altre tipus d'error de valor
                            print(f"Error interpretant '{operador_actual}': {str(ve)}")
                            raise ValueError(f"Error processant {operador_actual}")
                
                except Exception as e:
                    if "Error:" in str(e) or "Error en operació" in str(e) or "Operador o valor desconegut" in str(e):
                        raise e  # Re-llançar errors específics
                    print(f"Error processant operador: {str(e)}")
                    # Si és un error general, intentem seguir amb el següent operador
                    continue

            # Comprovem que quedi algun resultat
            if not vals:
                print("La pila de valors està buida al final!")
                raise ValueError("Error: no hi ha resultat disponible")

            # Retornem el resultat
            resultat_final = vals.pop(0)
            return resultat_final
            
        except Exception as e:
            if "Error:" in str(e) or "Error en operació" in str(e):
                raise e  # Re-llançar errors específics
            print(f"Error general avaluant les piles: {str(e)}")
            raise ValueError("Error en l'avaluació de l'expressió")
