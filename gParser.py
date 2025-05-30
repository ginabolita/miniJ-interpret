# Generated from g.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r")
        buf.write("F\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\7\2")
        buf.write("\17\n\2\f\2\16\2\22\13\2\3\3\6\3\25\n\3\r\3\16\3\26\3")
        buf.write("\4\3\4\3\4\6\4\34\n\4\r\4\16\4\35\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\5\4*\n\4\3\4\3\4\3\4\3\4\3\4\5\4")
        buf.write("\61\n\4\3\4\7\4\64\n\4\f\4\16\4\67\13\4\3\5\3\5\3\5\3")
        buf.write("\5\5\5=\n\5\3\6\3\6\3\6\6\6B\n\6\r\6\16\6C\3\6\2\3\6\7")
        buf.write("\2\4\6\b\n\2\3\4\2\3\3\b\b\2O\2\20\3\2\2\2\4\24\3\2\2")
        buf.write("\2\6)\3\2\2\2\b<\3\2\2\2\n>\3\2\2\2\f\17\5\b\5\2\r\17")
        buf.write("\5\n\6\2\16\f\3\2\2\2\16\r\3\2\2\2\17\22\3\2\2\2\20\16")
        buf.write("\3\2\2\2\20\21\3\2\2\2\21\3\3\2\2\2\22\20\3\2\2\2\23\25")
        buf.write("\7\n\2\2\24\23\3\2\2\2\25\26\3\2\2\2\26\24\3\2\2\2\26")
        buf.write("\27\3\2\2\2\27\5\3\2\2\2\30\31\b\4\1\2\31\33\7\13\2\2")
        buf.write("\32\34\5\6\4\2\33\32\3\2\2\2\34\35\3\2\2\2\35\33\3\2\2")
        buf.write("\2\35\36\3\2\2\2\36*\3\2\2\2\37 \t\2\2\2 *\5\6\4\t!*\5")
        buf.write("\4\3\2\"#\7\5\2\2#$\5\6\4\2$%\7\6\2\2%*\3\2\2\2&*\7\13")
        buf.write("\2\2\'*\7\b\2\2(*\7\t\2\2)\30\3\2\2\2)\37\3\2\2\2)!\3")
        buf.write("\2\2\2)\"\3\2\2\2)&\3\2\2\2)\'\3\2\2\2)(\3\2\2\2*\65\3")
        buf.write("\2\2\2+\60\f\b\2\2,\61\7\t\2\2-.\7\t\2\2.\61\7\4\2\2/")
        buf.write("\61\7\3\2\2\60,\3\2\2\2\60-\3\2\2\2\60/\3\2\2\2\61\62")
        buf.write("\3\2\2\2\62\64\5\6\4\t\63+\3\2\2\2\64\67\3\2\2\2\65\63")
        buf.write("\3\2\2\2\65\66\3\2\2\2\66\7\3\2\2\2\67\65\3\2\2\289\7")
        buf.write("\13\2\29:\7\7\2\2:=\5\6\4\2;=\5\6\4\2<8\3\2\2\2<;\3\2")
        buf.write("\2\2=\t\3\2\2\2>?\7\13\2\2?A\7\7\2\2@B\5\6\4\2A@\3\2\2")
        buf.write("\2BC\3\2\2\2CA\3\2\2\2CD\3\2\2\2D\13\3\2\2\2\13\16\20")
        buf.write("\26\35)\60\65<C")
        return buf.getvalue()


class gParser ( Parser ):

    grammarFileName = "g.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'#'", "'~'", "'('", "')'", "'=:'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "OPUNARI", "OPBINARI", "NUM", 
                      "VAR", "WS", "COMMENT" ]

    RULE_root = 0
    RULE_numlist = 1
    RULE_expr = 2
    RULE_stat = 3
    RULE_function = 4

    ruleNames =  [ "root", "numlist", "expr", "stat", "function" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    OPUNARI=6
    OPBINARI=7
    NUM=8
    VAR=9
    WS=10
    COMMENT=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gParser.StatContext)
            else:
                return self.getTypedRuleContext(gParser.StatContext,i)


        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gParser.FunctionContext)
            else:
                return self.getTypedRuleContext(gParser.FunctionContext,i)


        def getRuleIndex(self):
            return gParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = gParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << gParser.T__0) | (1 << gParser.T__2) | (1 << gParser.OPUNARI) | (1 << gParser.OPBINARI) | (1 << gParser.NUM) | (1 << gParser.VAR))) != 0):
                self.state = 12
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 10
                    self.stat()
                    pass

                elif la_ == 2:
                    self.state = 11
                    self.function()
                    pass


                self.state = 16
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(gParser.NUM)
            else:
                return self.getToken(gParser.NUM, i)

        def getRuleIndex(self):
            return gParser.RULE_numlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumlist" ):
                return visitor.visitNumlist(self)
            else:
                return visitor.visitChildren(self)




    def numlist(self):

        localctx = gParser.NumlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_numlist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 17
                    self.match(gParser.NUM)

                else:
                    raise NoViableAltException(self)
                self.state = 20 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParentesisContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(gParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParentesis" ):
                return visitor.visitParentesis(self)
            else:
                return visitor.visitChildren(self)


    class OpunariExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OPUNARI(self):
            return self.getToken(gParser.OPUNARI, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpunariExpr" ):
                return visitor.visitOpunariExpr(self)
            else:
                return visitor.visitChildren(self)


    class OpbinariExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OPBINARI(self):
            return self.getToken(gParser.OPBINARI, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpbinariExpr" ):
                return visitor.visitOpbinariExpr(self)
            else:
                return visitor.visitChildren(self)


    class BinariContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gParser.ExprContext)
            else:
                return self.getTypedRuleContext(gParser.ExprContext,i)

        def OPBINARI(self):
            return self.getToken(gParser.OPBINARI, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinari" ):
                return visitor.visitBinari(self)
            else:
                return visitor.visitChildren(self)


    class FuncioAplicadaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(gParser.VAR, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gParser.ExprContext)
            else:
                return self.getTypedRuleContext(gParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncioAplicada" ):
                return visitor.visitFuncioAplicada(self)
            else:
                return visitor.visitChildren(self)


    class LlistaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def numlist(self):
            return self.getTypedRuleContext(gParser.NumlistContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlista" ):
                return visitor.visitLlista(self)
            else:
                return visitor.visitChildren(self)


    class UnariContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(gParser.ExprContext,0)

        def OPUNARI(self):
            return self.getToken(gParser.OPUNARI, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnari" ):
                return visitor.visitUnari(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(gParser.VAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = gParser.FuncioAplicadaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 23
                self.match(gParser.VAR)
                self.state = 25 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 24
                        self.expr(0)

                    else:
                        raise NoViableAltException(self)
                    self.state = 27 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

                pass

            elif la_ == 2:
                localctx = gParser.UnariContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 29
                _la = self._input.LA(1)
                if not(_la==gParser.T__0 or _la==gParser.OPUNARI):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 30
                self.expr(7)
                pass

            elif la_ == 3:
                localctx = gParser.LlistaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 31
                self.numlist()
                pass

            elif la_ == 4:
                localctx = gParser.ParentesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 32
                self.match(gParser.T__2)
                self.state = 33
                self.expr(0)
                self.state = 34
                self.match(gParser.T__3)
                pass

            elif la_ == 5:
                localctx = gParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 36
                self.match(gParser.VAR)
                pass

            elif la_ == 6:
                localctx = gParser.OpunariExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 37
                self.match(gParser.OPUNARI)
                pass

            elif la_ == 7:
                localctx = gParser.OpbinariExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 38
                self.match(gParser.OPBINARI)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 51
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = gParser.BinariContext(self, gParser.ExprContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 41
                    if not self.precpred(self._ctx, 6):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                    self.state = 46
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        self.state = 42
                        self.match(gParser.OPBINARI)
                        pass

                    elif la_ == 2:
                        self.state = 43
                        self.match(gParser.OPBINARI)
                        self.state = 44
                        self.match(gParser.T__1)
                        pass

                    elif la_ == 3:
                        self.state = 45
                        self.match(gParser.T__0)
                        pass


                    self.state = 48
                    self.expr(7) 
                self.state = 53
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AssignacioContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(gParser.VAR, 0)
        def expr(self):
            return self.getTypedRuleContext(gParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignacio" ):
                return visitor.visitAssignacio(self)
            else:
                return visitor.visitChildren(self)


    class ExpressioContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(gParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressio" ):
                return visitor.visitExpressio(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = gParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stat)
        try:
            self.state = 58
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = gParser.AssignacioContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.match(gParser.VAR)
                self.state = 55
                self.match(gParser.T__4)
                self.state = 56
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = gParser.ExpressioContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gParser.RULE_function

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FuncioContext(FunctionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.FunctionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(gParser.VAR, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gParser.ExprContext)
            else:
                return self.getTypedRuleContext(gParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncio" ):
                return visitor.visitFuncio(self)
            else:
                return visitor.visitChildren(self)



    def function(self):

        localctx = gParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_function)
        try:
            localctx = gParser.FuncioContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(gParser.VAR)
            self.state = 61
            self.match(gParser.T__4)
            self.state = 63 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 62
                    self.expr(0)

                else:
                    raise NoViableAltException(self)
                self.state = 65 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         




