import os
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from assemble_and_build import assemble_html, compile_pdf

if __name__ == "__main__":
    print("Compiling full monograph treatise text...")
    assemble_html()
    compile_pdf()
