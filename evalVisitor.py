import numpy as np
from antlr4 import *
from gParser import gParser
from gVisitor import gVisitor
from utils import *


class EvalVisitor(gVisitor):

    def __init__(self):
        self.symbols = {}

    def visitRoot(self, ctx):
        # print(f"[D]: Visiting root")
        results = []
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if not isinstance(child, TerminalNode):
                result = self.visit(child)
                if result is not None:
                    results.append(result)

        # Don't try to convert everything to int - handle different types appropriately
        formatted_results = []
        for result in results:
            if isinstance(result, (int, float, np.ndarray, list)):
                # Already a numeric type or array
                formatted_results.append(result)
            elif isinstance(result, str) and result.isdigit():
                # String representation of a number
                formatted_results.append(int(result))
            else:
                # Keep non-numeric values as is
                formatted_results.append(result)

        for r in formatted_results:
            print(r)
        return formatted_results

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

        print(f"[D]: Assigning '{name}' with expression: {expr.getText()}")

        value = self.visit(ctx.expr())
        if value is None:
            raise ValueError(f"Assignació per '{name}' és None")
        if isinstance(value, list) or isinstance(value, np.ndarray):
            value = np.array(value)

        self.symbols[name] = value
        print(f"[D]: Stored '{name}' with value: {value}")
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
            operators.append(child_text)

        self.symbols[name] = operators
        print(f"[D]: Stored function '{name}' with operators {operators}")
        return self.symbols[name]

    def visitFunction(self, ctx):
        print(f"[D]: Visiting function")
        name = ctx.ID().getText()
        if name not in self.symbols:
            raise ValueError(f"Function '{name}' no definida")
        func_def = self.symbols[name]
        print(f"[D]: Function definition for '{name}': {func_def}")

        op_stack = []
        val_stack = []

        for op in func_def:
            try:
                if op.startswith('_'):
                    val = -int(op[1:])
                    val_stack.append(val)
                    print(f"[D]: Added numeric value to val_stack from function definition: {val}")
                else:
                    val = int(op)
                    val_stack.append(val)
                    print(f"[D]: Added numeric value to val_stack from function definition: {val}")
            except ValueError:
                if op in UNARY_OPERATORS or op in BINARY_OPERATORS:
                    op_stack.append(op)
                    print(f"[D]: Added operator to op_stack: {op}")
                elif op in self.symbols:
                    val = self.symbols[op]
                    val_stack.append(val)
                    print(f"[D]: Added variable value to val_stack: {val}")
                else:
                    # Si no es reconocido, asumimos que es un operador personalizado
                    op_stack.append(op)
                    print(f"[D]: Added custom operator to op_stack: {op}")

        args = []
        for i in range(1, ctx.getChildCount()):
            child = ctx.getChild(i)
            if not isinstance(child, TerminalNode):
                arg = self.visit(child)
                if arg is not None:
                    args.insert(0, arg)
        print(f"[D]: Function '{name}' called with arguments: {args}")

        for arg in args:
            val_stack.insert(0, arg)
        print(f"[D]: Initial stacks - Operators: {op_stack}, Values: {val_stack}")

        return self.evalua_amb_pila(op_stack, val_stack)

    def evalua_amb_pila(self, op_stack, val_stack):
        print(
            f"[D]: Evaluating with stacks - Operators: {op_stack}, Values: {val_stack}"
        )
        while op_stack:
            print(f"[D]: Current operator stack: {op_stack}")
            print(f"[D]: Current value stack: {val_stack}")
            op = op_stack.pop()
            if op in UNARY_OPERATORS:
                if not val_stack:
                    raise ValueError(f"Operació unària '{op}' sense valors a la pila")

                val = val_stack.pop()
                print(f"[D]: Applying unary operation '{op}' on value: {val}")
                result = apply_unary_operation(op, val)
                print(f"[D]: Result after unary operation: {result}")
                val_stack.insert(0, result)
            elif op in BINARY_OPERATORS:
                right = val_stack.pop()
                left = val_stack.pop()

                print(f"[D]: Applying binary operation '{op}' on values: {left}, {right}")
                result = apply_binary_operation(op, left, right)
                print(f"[D]: Result after binary operation: {result}")
                val_stack.insert(0, result)
            else:
                try:
                    if op.startswith('_'):
                        val = -int(op[1:])
                    else:
                        val = int(op)

                    val_stack.insert(0, val)
                    print(f"[D]: Added numeric value to stack: {val}")

                except ValueError:
                    # Si no es un número, comprobar si es una variable
                    if op in self.symbols:
                        val = self.symbols[op]
                        val_stack.insert(0, val)
                        print(f"[D]: Added variable value to stack: {val}")
                    else:
                        raise ValueError(f"Unknown operator or value: '{op}'")
        if not val_stack:
            raise ValueError("La pila de valors està buida després de l'operació")
        if len(val_stack) > 1:
            print(f"[D]: Stack after evaluation: {val_stack}")
        result = val_stack.pop(0)
        print(f"[D]: Final result after evaluation: {result}")
        return result
