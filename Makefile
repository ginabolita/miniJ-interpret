all: generate

generate:
	antlr4 -Dlanguage=Python3 -no-listener -visitor g.g4

clean:
	rm -rf g.interp g.tokens gLexer.interp gLexer.py gLexer.tokens gParser.py gVisitor.py output.out __pycache__    