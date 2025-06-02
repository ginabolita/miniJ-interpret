from antlr4 import *
from gLexer import gLexer
from gParser import gParser
from evalVisitor import evalVisitor
import sys

def main():
    file_name = sys.argv[1]
    visitor = evalVisitor()
    with open(file_name, 'r') as file:
        for line in file:
            input_stream = InputStream(line)
            lexer = gLexer(input_stream)
            token_stream = CommonTokenStream(lexer)
            parser = gParser(token_stream)
            tree = parser.root()
            # print(tree.toStringTree(recog=parser))
            result = visitor.visit(tree)

if __name__ == '__main__':
    main()
