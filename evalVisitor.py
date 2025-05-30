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
        return self.visitChildren(ctx)

    def visitParentesis(self, ctx):
        return self.visitChildren(ctx)

    def visitBinari(self, ctx):
        return self.visitChildren(ctx)

    def visitFuncioAplicada(self, ctx):
        return self.visitChildren(ctx)

    def visitLlista(self, ctx):
        return self.visitChildren(ctx)

    def visitUnari(self, ctx):
        return self.visitChildren(ctx)

    def visitId(self, ctx):
        return self.visitChildren(ctx)

    def visitAssignacio(self, ctx):
        return self.visitChildren(ctx)

    def visitExpressio(self, ctx):
        return self.visitChildren(ctx)

    def visitFuncio(self, ctx):
        name = ctx.VAR().getText()
        # Skip VAR and '=:'
        ops = [child.getText() for child in ctx.children[2:]]
        print(f"[DEBUG] visitFuncio: name={name}")
        print(f"[DEBUG] visitFuncio: ops={ops}")
        self.functions[name] = ops
        print(f"[DEBUG] self.functions={self.functions}")
        return None
