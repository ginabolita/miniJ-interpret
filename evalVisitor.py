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

    def visitBinari(self, ctx):
        return self.visitChildren(ctx)

    def visitFuncioAplicada(self, ctx):
        name = ctx.VAR().getText()
        args = [self.visit(child) for child in ctx.expr()]
        print(f"[DEBUG] visitFuncioAplicada: args={args}")
        symbol = self.symbols.get(name)
        if hasattr(symbol, 'OPUNARI'):
            op = symbol.OPUNARI().getText()
            print(f"[DEBUG] visitFuncioAplicada: opunari={op}")
            return apply_unary_op(op, args[0])

    def visitLlista(self, ctx):
        numlist_ctx = ctx.getChild(0)
        numbers = [int(child.getText()) for child in numlist_ctx.getChildren()]
        return np.array(numbers)

    def visitUnari(self, ctx):
        op = ctx.OPUNARI().getText()
        expr_ctx = ctx.expr()
        expr_val = self.visit(expr_ctx)
        print(
            f"[DEBUG] visitUnari: op={op}, expr_ctx={expr_ctx.getText()}, expr_val={expr_val}"
        )
        # You can implement the actual operation here if needed
        # return expr_val  # or apply the operator to expr_val

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
