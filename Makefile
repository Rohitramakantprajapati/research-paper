.PHONY: all pdf lean audit clean

all: lean audit pdf

# Compile LaTeX paper into PDF (uses pdflatex if available, otherwise playwright generator)
pdf:
	@mkdir -p paper/build 2>/dev/null || if not exist paper\build mkdir paper\build
	@if command -v pdflatex >/dev/null 2>&1; then \
		echo "Compiling LaTeX monograph with pdflatex..."; \
		cd paper && pdflatex -interaction=nonstopmode -output-directory=build monograph.tex && \
		pdflatex -interaction=nonstopmode -output-directory=build monograph.tex; \
	else \
		echo "pdflatex not found in PATH; building via Python rendering pipeline..."; \
		python scripts/build_pdf.py; \
	fi

# Build Lean 4 formalization package
lean:
	cd lean && lake build

# Run foundational axiom dependency check
audit:
	cd lean && lake env lean AxiomCheck.lean

# Remove build artifacts and temporary files
clean:
	rm -rf paper/build/*.aux paper/build/*.log paper/build/*.out paper/build/*.toc paper/build/*.synctex.gz paper/build/*.fls paper/build/*.fdb_latexmk 2>/dev/null || true
	rm -rf lean/.lake 2>/dev/null || true
