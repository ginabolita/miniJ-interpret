import numpy as np
from antlr4 import *
from gParser import gParser
from gVisitor import gVisitor
from utils import *


class EvalVisitor(gVisitor):

    def __init__(self):
        self.symbols = {}

    def visitRoot(self, ctx):
        results = []
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if not isinstance(child, TerminalNode):
                result = self.visit(child)
                if result is not None:
                    results.append(result)
                    if isinstance(result, list) or isinstance(
                            result, np.ndarray):
                        int_results = [int(x) for x in result]
                        formatted = " ".join('_' +
                                             str(abs(x)) if x < 0 else str(x)
                                             for x in int_results)
                        print(formatted)
                    else:
                        print(int(round(result)))


        return results

    def visitParentesis(self, ctx):
        return self.visit(ctx.expr())

    def visitExpressio(self, ctx):
        # print(f"[D]: Visiting expression")
        return self.visit(ctx.expr())

    def visitLlista(self, ctx):
        # print(f"[D]: Visiting list")
        numbers = []
        for n in ctx.numlist().NUM():
            text = n.getText()
            if text.startswith('_'):
                numbers.append(-int(text[1:]))
            else:
                numbers.append(int(text))
        return numbers

    def visitBinari(self, ctx):
        # print(f"[D]:Binary operation")
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText().strip('~')
        if left is None:
            raise ValueError(f"Esquerra és null '{op}'")
        if right is None:
            raise ValueError(f"Dreta és null '{op}'")

        if '~' in ctx.getChild(1).getText():
            left, right = right, left

        return apply_binary_operation(op, left, right)

    def visitUnari(self, ctx):
        # print(f"[D]: Unary operation '{ctx.getText()}'")
        if ctx.OPUNARI():
            op = ctx.OPUNARI().getText()
        else:
            op = ctx.getChild(0).getText()

        expr = self.visit(ctx.expr())
        return apply_unary_operation(op, expr)

    def visitAssignacio(self, ctx):
        # print(f"[D]: Visiting assignment")
        name = ctx.ID().getText()
        expr = ctx.expr()

        # print(f"[D]: Assigning '{name}' with expression: {expr.getText()}")

        value = self.visit(ctx.expr())
        if value is None:
            raise ValueError(f"Assignació per '{name}' és None")
        if isinstance(value, list) or isinstance(value, np.ndarray):
            value = np.array(value)

        self.symbols[name] = value
        # print(f"[D]: Stored '{name}' with value: {value}")
        # return value

    def visitId(self, ctx):
        # print(f"[D]: Visiting identifier")
        name = ctx.ID().getText()
        if name in self.symbols:
            return self.symbols[name]
        else:
            raise ValueError(f"Variable '{name}' no trobada al diccionari symbols")

    def visitFuncDef(self, ctx):
        # print(f"[D]: Visiting function definition")

        name = ctx.ID().getText()
        funcDef = ctx.funcDefinition()

        operators = []
        for i in range(funcDef.getChildCount()):
            child_text = funcDef.getChild(i).getText()
            # print(f"[D]: Processing child '{child_text}' in function definition")
            if child_text != '@:': 
                if child_text in self.symbols and isinstance(
                        self.symbols[child_text], list):
                    func_ops = self.symbols[child_text]
                    print(
                        f"[D]: Resolved function '{child_text}' to its definition: {func_ops}"
                    )
                    if len(operators) == 1:
                        operators.append(func_ops[0])  
                    else:
                        operators.extend(func_ops)
                else:
                    operators.append(child_text)


        self.symbols[name] = np.array(operators)
        print(f"[D]: Stored function '{name}' with operators: {self.symbols}")
        # return operators

    def visitFunction(self, ctx):
        name = ctx.ID().getText()
        if name not in self.symbols:
            raise ValueError(f"Function '{name}' no definida")
        
        func_def = self.symbols[name]
        print(f"[D]: Function definition for '{name}': {func_def}")

        op_stack = []
        val_stack = []

        # Expandir función completamente antes de procesar
        for op in func_def:
            if op in self.symbols and isinstance(self.symbols[op], (np.ndarray, list)):
                # Si es una referencia a otra función, expandir sus operadores
                inner_func = self.symbols[op]
                print(f"[D]: Expanding function '{op}': {inner_func}")
                
                # Procesar cada operador de la función interna
                for inner_op in inner_func:
                    try:
                        # Intentar interpretar como número
                        if inner_op.startswith('_'):
                            val = -int(inner_op[1:])
                            val_stack.append(val)
                        else:
                            val = int(inner_op)
                            val_stack.append(val)
                    except ValueError:
                        # No es un número, añadir a la pila de operadores
                        if inner_op != '@:':  # Ignorar el operador de composición
                            op_stack.append(inner_op)
            else:
                try:
                    # Intentar interpretar como número
                    if op.startswith('_'):
                        val = -int(op[1:])
                        val_stack.append(val)
                    else:
                        val = int(op)
                        val_stack.append(val)
                except ValueError:
                    # No es un número, añadir a la pila de operadores
                    if op == '@:':
                        # Ignorar el operador de composición
                        continue
                    elif op in UNARY_OPERATORS or op in BINARY_OPERATORS:
                        op_stack.append(op)
                    else:
                        # Si no se reconoce, podría ser otra función o variable
                        # Para este caso específico, lo añadimos a la pila de operadores
                        print(f"[D]: Unrecognized operator '{op}', adding to op_stack")
                        op_stack.append(op)

        # Recopilar argumentos
        args = []
        for i in range(1, ctx.getChildCount()):
            child = ctx.getChild(i)
            if not isinstance(child, TerminalNode):
                arg = self.visit(child)
                if arg is not None:
                    args.append(arg)

        # Añadir argumentos a la pila de valores
        for arg in args:
            val_stack.append(arg)

        print(f"[D]: Initial stacks - Operators: {op_stack}, Values: {val_stack}")
        
        return self.evalua_amb_pila(op_stack, val_stack)

    def evalua_amb_pila(self, op_stack, val_stack):
        # print(
        #     f"[D]: Evaluating with stacks - Operators: {op_stack}, Values: {val_stack}"
        # )
        while op_stack:
            # print(f"[D]: Current operator stack: {op_stack}")
            # print(f"[D]: Current value stack: {val_stack}")
            op = op_stack.pop()
            if op in UNARY_OPERATORS:
                if not val_stack:
                    raise ValueError(f"Operació unària '{op}' sense valors a la pila")

                val = val_stack.pop()
                # print(f"[D]: Applying unary operation '{op}' on value: {val}")
                result = apply_unary_operation(op, val)
                # print(f"[D]: Result after unary operation: {result}")
                val_stack.append(result)
            elif op in BINARY_OPERATORS:
                right = val_stack.pop()
                left = val_stack.pop()

                # print(f"[D]: Applying binary operation '{op}' on values: {left}, {right}")
                result = apply_binary_operation(op, left, right)
                # print(f"[D]: Result after binary operation: {result}")
                val_stack.append(result)
            else:
                try:
                    if op.startswith('_'):
                        val = -int(op[1:])
                    else:
                        val = int(op)

                    val_stack.insert(0, val)
                    # print(f"[D]: Added numeric value to stack: {val}")

                except ValueError:
                    # Si no es un número, comprobar si es una variable
                    if op in self.symbols:
                        val = self.symbols[op]
                        val_stack.insert(0, val)
                        # print(f"[D]: Added variable value to stack: {val}")
                    else:
                        raise ValueError(f"Unknown operator or value: '{op}'")
        if not val_stack:
            raise ValueError("La pila de valors està buida després de l'operació")
        # if len(val_stack) > 1:
        #     print(f"[D]: Stack after evaluation: {val_stack}")
        result = val_stack.pop(0)
        # print(f"[D]: Final result after evaluation: {result}")
        return result
