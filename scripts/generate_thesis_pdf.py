"""
Master Build Script for University Research Thesis Monograph
Author: Rohit Ramakant Prajapati
Generates the complete 140+ page doctoral research thesis in PDF and HTML format.
"""
import os
import sys

# Ensure thesis_generator is in path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
GEN_DIR = os.path.join(CURRENT_DIR, "thesis_generator")
if GEN_DIR not in sys.path:
    sys.path.insert(0, GEN_DIR)

from builder import assemble_thesis, compile_pdf

if __name__ == "__main__":
    print("=" * 70)
    print("STARTING 3D NAVIER-STOKES UNIVERSITY THESIS BUILD PIPELINE")
    print("=" * 70)
    html_file = assemble_thesis()
    page_count = compile_pdf(html_file)
    print("=" * 70)
    print(f"BUILD FINISHED: Generated complete university thesis ({page_count} pages)")
    print("=" * 70)
