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
        # print(f"[D]: Visiting binary operation")
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
        if ctx.OPUNARI():
            op = ctx.OPUNARI().getText()
        else:
            op = ctx.getChild(0).getText()
        expr = self.visit(ctx.expr())
        return apply_unary_operation(op, expr)

    def visitAssignacio(self, ctx):
        print(f"[D]: Visiting assignment")
        name = ctx.ID().getText()
        expr = ctx.expr()

        print(f"[D]: Assigning '{name}' with expression: {expr.getText()}")
        for i in range(expr.getChildCount()):
            child_text = expr.getChild(i).getText()
            print(f"[D]: Child {i}: {child_text}")


        value = self.visit(ctx.expr())
        if value is None:
            raise ValueError(f"Assignació per '{name}' és None")
        if isinstance(value, list) or isinstance(value, np.ndarray):
            value = np.array(value)

        self.symbols[name] = value

        return value

    def visitId(self, ctx):
        print(f"[D]: Visiting identifier")
        name = ctx.ID().getText()
        if name in self.symbols:
            return self.symbols[name]
        else:
            raise ValueError(f"Variable '{name}' no trobada al diccionari symbols")

    def visitFuncDef(self, ctx):
        print(f"[D]: Visiting function definition")
        name = ctx.ID().getText()
        funcDef = ctx.funcDefinition()
        print(f"[D]: Function name: {name}")

        operators = []

        for i in range(funcDef.getChildCount()):
            child_text = funcDef.getChild(i).getText()
            print(f"[D]: Child {i}: {funcDef.getChild(i).getText()}")
            operators.append(child_text)

        self.symbols[name] = operators
        print(f"[D]: Stored function '{name}' with operators {operators}")
        print(f"[D]: Current symbols: {self.symbols}")
        return self.symbols[name]

    def visitCall(self, ctx):
        print(f"[D]: Visiting function call")
        name = ctx.ID(0).getText()

        if name not in self.symbols:
            raise ValueError(f"Function '{name}' no definida al diccionari symbols")

        stored_operators = self.symbols[name]
        print(f"[D]: Function name: {name}")
        print(f"[D]: Stored operators: {stored_operators}")

        variables = []
        functions = []

        id_tokens = []
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if isinstance(child, TerminalNode) and child.getSymbol().type == gParser.ID:
                id_tokens.append(child)

        print(f"[D]: ID tokens: {[token.getText() for token in id_tokens]}")
        print(f"[D]: Number of ID tokens: {len(id_tokens)}")
        print(f"[D]: value {self.symbols[id_tokens[0].getText()]}")

        for i in range(0, len(id_tokens)):
            arg_name = ctx.ID(i).getText()
            print(f"[D]: Argument {i}: {arg_name}")

            if arg_name in self.symbols:
                variables.append(self.symbols[arg_name])
            else:
                try:
                    if arg_name.startswith('_'):
                        variables.append(-int(arg_name[1:]))
                    else:
                        variables.append(int(arg_name))
                except ValueError:
                    if arg_name in aritmetics or arg_name in relacionals:
                        functions.append(arg_name)
                    else:
                        raise ValueError(
                        f"Unknown identifier or operator: {arg_name}")

        print(f"[D]: Variables stack: {variables}")
        print(f"[D]: Functions stack: {functions}")
        result = self._evaluate_with_stacks(variables, functions)
        return result

    def _evaluate_with_stacks(self, variables, functions):
        vars = variables.copy()
        funcs = functions.copy()

        if not funcs and vars:
            return vars[0]

        while funcs:
            op = funcs.pop(0)
            if op in aritmetics or op in relacionals:
                if len(vars) < 2:
                    raise ValueError(f"Not enough variables for operation '{op}'")
                right = vars.pop()
                left = vars.pop()
                print(f"[D]: Operands for {op}: left={left}, right={right}")

                result = apply_binary_operation(op, left, right)
                print(f"[D]: Result of operation '{op}': {result}")
                vars.insert(0, result)
            elif op in unary_ops or (len(op) > 1 and op[1:] ==  ':' or op[1:] == '/'):
                if not vars:
                    raise ValueError(f"Not enough variables for unary operation '{op}'")
                expr = vars.pop(0)
                print(f"[D]: Operand for {op}: {expr}")

                result = apply_unary_operation(op, expr)
                print(f"[D]: Result of unary operation '{op}': {result}")
                vars.insert(0, result)
            else:
                raise ValueError(f"Unknown operation: {op}")
        if not vars:
            return None
        elif len(vars) == 1:
            return vars[0]
        else:
            print(f"[D]: Warning: Multiple values left on stack: {vars}")
            return vars[0]
