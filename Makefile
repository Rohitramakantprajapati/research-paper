.PHONY: pdf clean lean

pdf:
	latexmk -pdf monograph.tex

clean:
	latexmk -c

lean:
	cd lean_package && lake build
