import numpy as np
from antlr4 import *
from gParser import gParser
from gVisitor import gVisitor
from utils import *


class EvalVisitor(gVisitor):

    def __init__(self):
        self.stack = []

    def visitRoot(self, ctx):
        # print(f"[D]: Visiting root")
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
        # print(f"[D]: Visiting binary operation")
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if left is None:
            raise ValueError(f"Left operand is None for operation '{op}'")
        if right is None:
            raise ValueError(f"Right operand is None for operation '{op}'")

        op = ctx.getChild(1).getText().strip('~')
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
