# Generated from g.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .gParser import gParser
else:
    from gParser import gParser

# This class defines a complete generic visitor for a parse tree produced by gParser.

class gVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by gParser#root.
    def visitRoot(self, ctx:gParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#numlist.
    def visitNumlist(self, ctx:gParser.NumlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#parentesis.
    def visitParentesis(self, ctx:gParser.ParentesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#opunariExpr.
    def visitOpunariExpr(self, ctx:gParser.OpunariExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#opbinariExpr.
    def visitOpbinariExpr(self, ctx:gParser.OpbinariExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#binari.
    def visitBinari(self, ctx:gParser.BinariContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#funcioAplicada.
    def visitFuncioAplicada(self, ctx:gParser.FuncioAplicadaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#llista.
    def visitLlista(self, ctx:gParser.LlistaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#unari.
    def visitUnari(self, ctx:gParser.UnariContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#id.
    def visitId(self, ctx:gParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#assignacio.
    def visitAssignacio(self, ctx:gParser.AssignacioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#expressio.
    def visitExpressio(self, ctx:gParser.ExpressioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#funcio.
    def visitFuncio(self, ctx:gParser.FuncioContext):
        return self.visitChildren(ctx)



del gParser