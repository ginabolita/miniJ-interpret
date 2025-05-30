import numpy as np
from antlr4 import *
from utils import *

if "." in __name__:
    from .gParser import gParser
    from .gVisitor import gVisitor
    from .gLexer import gLexer
else:
    from gParser import gParser
    from gVisitor import gVisitor
    from gLexer import gLexer

class evalVisitor(gVisitor):
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.stack = []

    def visitRoot(self, ctx):
        for child in ctx.getChildren():
            result = self.visit(child)
            if result is not None:
                arr = np.array(result)
                arr = arr.flatten()
                arr = arr.astype(int)
                formatted = " ".join(str(x).replace("-", "_") for x in arr)
                print(formatted)

    def visitParentesis(self, ctx):
        return self.visit(ctx.getChild(1))

    def visitFuncioAplicada(self, ctx):
        name = ctx.VAR().getText()
        args = [self.visit(child) for child in ctx.expr()]
        print(f"[DEBUG] visitFuncioAplicada: args={args}")
        if name in self.functions:
            func_ctx = self.functions[name]
            for arg in reversed(args):
                self.stack.append(arg)
            result = self.visit(func_ctx)
            print(f"[DEBUG] visitFuncioAplicada: result={result}")
            return result
        else:
            raise Exception(f"Function '{name}' is not defined.")

    def visitLlista(self, ctx):
        numlist_ctx = ctx.getChild(0)
        numbers = [int(child.getText()) for child in numlist_ctx.getChildren()]
        return np.array(numbers)

    def visitBinari(self, ctx):
        children = list(ctx.getChildren())
        if len(children) == 4 and children[2].getText() == '~':
            left = self.visit(children[0])
            op = children[1].getText()
            right = self.visit(children[3])
            print(f"[DEBUG] visitBinari: left={left}, op={op}, right={right}")
            return flip_op(op, left, right)

        left = self.visit(ctx.getChild(0))
        op = ctx.getChild(1).getText()
        right = self.visit(ctx.getChild(2))

        if op == '@:':

            def composed(arg):
                if callable(right):
                    right_result = right(arg)
                else:
                    self.stack.append(arg)
                    right_result = self.visit(right)
                if callable(left):
                    return left(right_result)
                else:
                    self.stack.append(right_result)
                    return self.visit(left)

            if self.stack:
                arg = self.stack.pop()
                result = composed(arg)
                print(
                    f"[DEBUG] visitBinari: composed @{left} @{right}({arg}) = {result}"
                )
                return result
            else:
                return composed
        result = apply_binary_op(op, left, right)
        return result

    def visitUnari(self, ctx):
        op = ctx.OPUNARI().getText() if ctx.OPUNARI() else ctx.getChild(0).getText()
        expr_ctx = ctx.expr()
        if op == ']':
            if self.stack:
                arg = self.stack.pop()
                print(f"[DEBUG] visitUnari: op=], returning argument from stack: {arg}")
                return arg
            else:
                print("[DEBUG] visitUnari: op=], stack empty, returning None")
                return None
        expr_val = self.visit(expr_ctx)
        print(
            f"[DEBUG] visitUnari: op={op}, expr_ctx={expr_ctx.getText()}, expr_val={expr_val}"
        )
        if op == '#':
            return size_op(expr_val)
        if op == 'i.':
            return n_primers(expr_val)
        elif op == '_':
            return negate_op(expr_val)
        elif op[1:] == ':':
            return double_op(op[0], expr_val)
        elif op[1:] == '/':
            return fold_op(op[0], expr_val)

    def visitId(self, ctx):
        name = ctx.VAR().getText()
        if name in self.variables:
            value = self.variables[name]
            print(f"[DEBUG] visitId: {name} (variable) = {value}")
            return value
        elif name in self.functions:
            func_node = self.functions[name]
            print(f"[DEBUG] visitId: {name} (function node) = {func_node}")
            return func_node
        else:
            print(f"[DEBUG] visitId: {name} not found")
            return None

    def visitAssignacio(self, ctx):
        name = ctx.VAR().getText()
        expr_ctx = ctx.expr()
        self.functions[name] = expr_ctx
        print(f"[DEBUG] Assigned symbol: {name} = {expr_ctx.getText()}")
        return None

    def visitExpressio(self, ctx):
        return self.visitChildren(ctx)

    def visitOpunariExpr(self, ctx):
        op = ctx.getText()
        if self.stack:
            arg = self.stack.pop()
            print(f"[DEBUG] visitOpunariExpr: op={op}, applying apply_unary_op to {arg}")
            return apply_unary_op(op, arg)
        else:
            print(f"[DEBUG] visitOpunariExpr: op={op}, stack empty, returning None")
            return None

    def visitOpbinariExpr(self, ctx):
        op = ctx.getText()
        def binop(left, right):
            print(f"[DEBUG] visitOpbinariExpr: op={op}, left={left}, right={right}")
            return apply_binary_op(op, left, right)
        return binop
