all: generate run

generate:
	antlr4 -Dlanguage=Python3 -no-listener -visitor g.g4

run:
	python3 g.py test_enunciat.j > output.out

clean:
	rm -rf g.interp g.tokens gLexer.interp gLexer.py gLexer.tokens gParser.py gVisitor.py output.out
    