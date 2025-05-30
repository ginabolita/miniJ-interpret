# Generated from g.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\r")
        buf.write("Z\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\3")
        buf.write("\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\5\7,\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\5\b:\n\b\3\t\6\t=\n\t\r\t\16\t>\3\n\3\n\7\n")
        buf.write("C\n\n\f\n\16\nF\13\n\3\13\6\13I\n\13\r\13\16\13J\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\f\7\fT\n\f\f\f\16\fW\13\f\3\f")
        buf.write("\3\f\2\2\r\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\3\2\n\4\2__aa\b\2\'\',-//\61\61``~~\t\2\'\',-")
        buf.write("//>>@@``~~\3\2\62;\4\2C\\c|\6\2\62;C\\aac|\5\2\13\f\17")
        buf.write("\17\"\"\4\2\f\f\17\17\2g\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write("\3\31\3\2\2\2\5\33\3\2\2\2\7\35\3\2\2\2\t\37\3\2\2\2\13")
        buf.write("!\3\2\2\2\r+\3\2\2\2\179\3\2\2\2\21<\3\2\2\2\23@\3\2\2")
        buf.write("\2\25H\3\2\2\2\27N\3\2\2\2\31\32\7\u0080\2\2\32\4\3\2")
        buf.write("\2\2\33\34\7%\2\2\34\6\3\2\2\2\35\36\7*\2\2\36\b\3\2\2")
        buf.write("\2\37 \7+\2\2 \n\3\2\2\2!\"\7?\2\2\"#\7<\2\2#\f\3\2\2")
        buf.write("\2$,\t\2\2\2%&\7k\2\2&,\7\60\2\2\'(\t\3\2\2(,\7<\2\2)")
        buf.write("*\t\3\2\2*,\7\61\2\2+$\3\2\2\2+%\3\2\2\2+\'\3\2\2\2+)")
        buf.write("\3\2\2\2,\16\3\2\2\2-:\t\4\2\2./\7@\2\2/:\7?\2\2\60\61")
        buf.write("\7>\2\2\61:\7?\2\2\62:\7?\2\2\63\64\7>\2\2\64:\7@\2\2")
        buf.write("\65:\7.\2\2\66\67\7B\2\2\67:\7<\2\28:\7}\2\29-\3\2\2\2")
        buf.write("9.\3\2\2\29\60\3\2\2\29\62\3\2\2\29\63\3\2\2\29\65\3\2")
        buf.write("\2\29\66\3\2\2\298\3\2\2\2:\20\3\2\2\2;=\t\5\2\2<;\3\2")
        buf.write("\2\2=>\3\2\2\2><\3\2\2\2>?\3\2\2\2?\22\3\2\2\2@D\t\6\2")
        buf.write("\2AC\t\7\2\2BA\3\2\2\2CF\3\2\2\2DB\3\2\2\2DE\3\2\2\2E")
        buf.write("\24\3\2\2\2FD\3\2\2\2GI\t\b\2\2HG\3\2\2\2IJ\3\2\2\2JH")
        buf.write("\3\2\2\2JK\3\2\2\2KL\3\2\2\2LM\b\13\2\2M\26\3\2\2\2NO")
        buf.write("\7P\2\2OP\7D\2\2PQ\7\60\2\2QU\3\2\2\2RT\n\t\2\2SR\3\2")
        buf.write("\2\2TW\3\2\2\2US\3\2\2\2UV\3\2\2\2VX\3\2\2\2WU\3\2\2\2")
        buf.write("XY\b\f\2\2Y\30\3\2\2\2\t\2+9>DJU\3\b\2\2")
        return buf.getvalue()


class gLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    OPUNARI = 6
    OPBINARI = 7
    NUM = 8
    VAR = 9
    WS = 10
    COMMENT = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'~'", "'#'", "'('", "')'", "'=:'" ]

    symbolicNames = [ "<INVALID>",
            "OPUNARI", "OPBINARI", "NUM", "VAR", "WS", "COMMENT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "OPUNARI", "OPBINARI", 
                  "NUM", "VAR", "WS", "COMMENT" ]

    grammarFileName = "g.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


