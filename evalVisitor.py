import numpy as np
from antlr4 import *
from gParser import gParser
from gVisitor import gVisitor
from utils import *

class evalVisitor(gVisitor):
    def __init__(self):
        """Inicialitza el diccionari d'estat per emmagatzemar variables i funcions."""
        self.diccionari = {} # Diccionari per funcions i variables

    def visitRoot(self, ctx):
        """Visita el node arrel i processa les expressions."""
        try:
            resultats = []
            for i in range(ctx.getChildCount()):
                fill = ctx.getChild(i)
                if not isinstance(fill, TerminalNode):
                    try:
                        resultat = self.visit(fill)
                        if resultat is not None:
                            resultats.append(resultat)
                            self.imprimeix(resultat)
                    except Exception as e:
                        print(f"Error sintàctic al node {i}: {str(e)}")
            return resultats
        except Exception as e:
            print(f"Error al visitRoot: {str(e)}")
            return []

    def imprimeix(self, resultat):
        """Imprimeix el resultat de l'expressió amb el format adequat."""
        if isinstance(resultat, (list, np.ndarray)):
            valors_enters = [int(x) for x in resultat]
            format_text = " ".join('_' + str(abs(x)) if x < 0 else str(x)
                                   for x in valors_enters)
            print(format_text)
        else:
            print(int(resultat))

    def visitParentesis(self, ctx):
        """Visita les expressions entre parèntesis."""
        try:
            return self.visit(ctx.expr())
        except Exception as e:
            print(f"Error als parèntesis: {str(e)}")
            raise ValueError("Estructura de parèntesis incorrecta")

    def visitExpressio(self, ctx):
        """Visita una expressió i retorna el seu valor."""
        return self.visit(ctx.expr())

    def visitLlista(self, ctx):
        """Visita una llista de números i retorna un array de numpy."""
        try:
            nums = []
            for n in ctx.numlist().NUM():
                text = n.getText()
                try:
                    if text.startswith('_'):
                        nums.append(-int(text[1:]))  # negatius
                    else:
                        nums.append(int(text))  # positius
                except ValueError:
                    print(f"'{text}' no és número vàlid")
            return np.array(nums)
        except Exception as e:
            print(f"Error a la llista: {str(e)}")
            raise ValueError("Format de llista incorrecte")

    def visitBinari(self, ctx):
        """Visita una operació binària i retorna el resultat."""
        try:
            esq = self.visit(ctx.expr(0))
            dre = self.visit(ctx.expr(1))
            op = ctx.getChild(1).getText().strip('~')

            if esq is None or dre is None:
                raise ValueError(f"Error a l'operació {op}: un operand no vàlid")

            if '~' in ctx.getChild(1).getText():  # cas flip
                esq, dre = dre, esq
            return apply_binary_operation(op, esq, dre)
        except Exception as e:
            raise ValueError("Problema amb l'operador binari o els seus operands")

    def visitUnari(self, ctx):
        """Visita una operació unària i retorna el resultat."""
        try:
            op = self.obtenir_operador_unari(ctx)
            expr = self.visit(ctx.expr())
            if expr is None:
                print(f"Error: expressió nul·la per '{op}'")
                raise ValueError(f"Eexpressió per {op} no vàlida")
            return apply_unary_operation(op, expr)
        except Exception as e:
            print(f"Error amb operador unari: {str(e)}")
            raise ValueError("Problema amb l'operador unari o el seu operand")

    def obtenir_operador_unari(self, ctx):
        """Obté l'operador unari del context."""
        if ctx.OPUNARI():
            return ctx.OPUNARI().getText()
        else:
            return ctx.getChild(0).getText()

    def visitAssignacio(self, ctx):
        """Visita una assignació i actualitza el diccionari d'estat."""
        try:
            nom = ctx.ID().getText()
            valor = self.visit(ctx.expr())
            if valor is None:
                print(f"No es pot assignar None a '{nom}'")
                raise ValueError(f"Error: valor nul per assignar a {nom}")
            if isinstance(valor, list) or isinstance(valor, np.ndarray):
                valor = np.array(valor)
            self.diccionari[nom] = valor
        except Exception as e:
            print(f"Error en assignació: {str(e)}")
            raise ValueError(f"Problema amb l'assignació a {nom}")

    def visitId(self, ctx):
        """Visita un identificador i retorna el seu valor del diccionari."""
        try:
            nom = ctx.ID().getText()
            if nom in self.diccionari:
                return self.diccionari[nom]
            else:
                print(f"Variable '{nom}' no definida")
                raise ValueError(f"Error: la variable {nom} no existeix")
        except Exception as e:
            print(f"Error accedint a variable: {str(e)}")
            raise ValueError(f"Problema accedint a la variable {nom}")

    def visitFuncDef(self, ctx):
        """Visita una definició de funció i la registra al diccionari."""
        name = ctx.ID().getText()
        funcDef = ctx.funcDefinition()

        operators = self.processaFunction(funcDef)
        self.diccionari[name] = np.array(operators)

    def processaFunction(self, funcDef):
        """Processa la definició de funció i retorna els operadors."""
        operadors = []
        for i in range(funcDef.getChildCount()):
            text = funcDef.getChild(i).getText()
            if text != '@:':
                if text in self.diccionari and isinstance(self.diccionari[text], list):
                    self.resol_funcio(text, operadors)
                else:
                    operadors.append(text)
                    
        return operadors

    def resol_funcio(self, func_name, operadors):
        """Expandeix la referència a una funció i afegeix els seus operadors."""
        func_ops = self.diccionari[func_name]

        if len(operadors) == 1:
            operadors.append(func_ops[0])
        else:
            operadors.extend(func_ops)

    def visitFunction(self, ctx):
        """Visita una funció i avalua la seva definició."""
        name = ctx.ID().getText()
        if name not in self.diccionari:
            raise ValueError(f"Function '{name}' no definida")

        func_def = self.diccionari[name]

        op_stack = []
        val_stack = []
        self.processa_tokens(func_def, op_stack, val_stack)
        args = self.retorna_arguments(ctx)
        val_stack.extend(args)
        return self.evalua_amb_pila(op_stack, val_stack)

    def processa_tokens(self, func_def, op_stack, val_stack):
        """Processa els tokens de la definició de funció i omple les piles d'operadors i valors."""
        for token in func_def:
            if token in self.diccionari and isinstance(self.diccionari[token],
                                                       (np.ndarray, list)):
                inner_func = self.diccionari[token]
                for inner_op in inner_func:
                    self.processa_un_token(inner_op, op_stack, val_stack)
            else:
                self.processa_un_token(token, op_stack, val_stack)

    def processa_un_token(self, token, op_stack, val_stack):
        """Processa un token individual i l'afegeix a la pila corresponent."""
        try:
            if isinstance(token, str):
                if token.startswith('_'):
                    val_stack.append(-int(token[1:]))
                    return
                elif token.isdigit():
                    val_stack.append(int(token))
                    return

            if token in BINARY_OPERATORS or token in UNARY_OPERATORS:
                if token != '@:':  # Ignorar operador de composició
                    op_stack.append(token)
            elif token in self.diccionari:
                val = self.diccionari[token]
                val_stack.append(val)
            else:
                op_stack.append(token)
        except ValueError:
            if token != '@:':
                op_stack.append(token)

    def retorna_arguments(self, ctx):
        """Visita els arguments d'una funció i retorna els seus valors."""
        args = []
        for i in range(1, ctx.getChildCount()):
            child = ctx.getChild(i)
            if not isinstance(child, TerminalNode):
                arg = self.visit(child)
                if arg is not None:
                    args.append(arg)
        return args

    def evalua_amb_pila(self, op_stack, val_stack):
        """Evalua les operacions utilitzant les piles d'operadors i valors."""
        try:
            while op_stack:
                op = op_stack.pop()
                if op in UNARY_OPERATORS:
                    self.tractat_unari(op, val_stack)
                elif op in BINARY_OPERATORS:
                    self.tractat_binari(op, val_stack)
                else:
                    self.tractat_altres(op, val_stack)

            if not val_stack:
                raise ValueError("La pila de valors està buida després de l'operació")

            result = val_stack.pop(0)
            return result
        except Exception as e:
            raise ValueError("Error en l'avaluació de l'expressió")

    def tractat_unari(self, op, val_stack):
        """ Aplica una operació unària sobre la pila de valors. """
        if not val_stack:
            raise ValueError(f"Operació unària '{op}' sense valors a la pila")

        val = val_stack.pop()
        result = apply_unary_operation(op, val)
        val_stack.append(result)

    def tractat_binari(self, op, val_stack):
        """ Aplica una operació binària sobre la pila de valors. """
        if len(val_stack) < 2:
            raise ValueError(f"Operació binària '{op}' sense suficients valors a la pila")

        right = val_stack.pop()
        left = val_stack.pop()
        result = apply_binary_operation(op, left, right)
        val_stack.append(result)

    def tractat_altres(self, token, val_stack):
        """ Processa altres tokens que no són operadors ni valors numèrics. """
        try:
            if isinstance(token, str):
                if token.startswith('_'):
                    val = -int(token[1:])
                    val_stack.insert(0, val)
                    return
                elif token.isdigit():
                    val = int(token)
                    val_stack.insert(0, val)
                    return

            if token in self.diccionari:
                val = self.diccionari[token]
                val_stack.insert(0, val)
                return

            raise ValueError(f"Operador o valor desconegut: {token}")
        except ValueError as e:
            raise ValueError(f"No es pot processar el token '{token}': {str(e)}")
