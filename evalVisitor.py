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
        self.symbols = {}
        self.stack = []

    def visitRoot(self, ctx):
        for child in ctx.getChildren():
            result = self.visit(child)
            if result is not None:
                arr = np.array(result)
                arr = arr.flatten()
                formatted = " ".join(str(x).replace("-", "_") for x in arr)
                print(formatted)

    def visitParentesis(self, ctx):
        return self.visit(ctx.getChild(1))

    def visitFuncioAplicada(self, ctx):
        name = ctx.VAR().getText()
        args = [self.visit(child) for child in ctx.expr()]
        print(f"[DEBUG] visitFuncioAplicada: args={args}")
        symbol = self.symbols.get(name)
        if hasattr(symbol, 'OPUNARI'):
            op = symbol.OPUNARI().getText()
            print(f"[DEBUG] visitFuncioAplicada: opunari={op}")
            return apply_unary_op(op, args[0])
        elif hasattr(symbol, 'OPBINARI'):
            op = symbol.OPBINARI().getText()
            print(f"[DEBUG] visitFuncioAplicada: opbinari={op}")
            return apply_binary_op(op, args[0], args[1])

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
        print(f"[DEBUG] visitBinari: left={left}, op={op}, right={right}")

        if op == '#':
            return mask_op(left, right)
        elif op == '{':
            return index_op(left, right)
        elif op == ',':
            return concatenate_op(left, right)
        elif op == '|':
            return aritmetic_op(op, right, left)
        elif op in aritmetics:
            return aritmetic_op(op, expr1, expr2)
        elif op in relacionals:
            return relacional_op(op, expr1, expr2)
        else:
            raise Exception(f"Unknown binary operator: {op}")

    def visitUnari(self, ctx):
        op = ctx.OPUNARI().getText() if ctx.OPUNARI() else ctx.getChild(0).getText()
        expr_ctx = ctx.expr()
        expr_val = self.visit(expr_ctx)
        print(
            f"[DEBUG] visitUnari: op={op}, expr_ctx={expr_ctx.getText()}, expr_val={expr_val}"
        )
        if op == '#':
            return size_op(expr_val)

        if op == 'i.':
            return n_primers(expr_val)
        elif op == ']':
            return identity_op(expr_val)
        elif op == '_':
            return negate_op(expr_val)
        elif op[1:] == ':':
            return double_op(op[0], expr_val)
        elif op[1:] == '/':
            return fold_op(op[0], expr_val)

    def visitId(self, ctx):
        return self.visitChildren(ctx)

    def visitAssignacio(self, ctx):
        name = ctx.VAR().getText()
        expr_ctx = ctx.expr()
        self.symbols[name] = expr_ctx
        print(f"[DEBUG] Assigned symbol: {name} = {expr_ctx.getText()}")
        return None

    def visitExpressio(self, ctx):
        return self.visitChildren(ctx)

    # def visitFuncio(self, ctx):
    #     name = ctx.VAR().getText()
    #     ops = [child.getText() for child in ctx.children[2:]]
    #     self.functions[name] = ops
    #     print(f"[DEBUG] self.functions={self.functions}")
    #     return None
