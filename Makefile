all: generate run

generate:
	antlr4 -Dlanguage=Python3 -no-listener -visitor g.g4

run:
    python3 g.py ./test/programa.j > sortida.txt

clean:
    rm -rf g.tokens gLexer.py gLexer.tokens gParser.py g.interp gLexer.interp __pycache__ g.py gVisitor.py gListener.py
    