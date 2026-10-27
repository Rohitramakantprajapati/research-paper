import os
import sys
import shutil
import re
from playwright.sync_api import sync_playwright

from styles import CSS_STYLES
from front_matter import generate_front_matter
from chapter01 import generate_chapter_01
from chapter02 import generate_chapter_02
from chapter03 import generate_chapter_03
from chapter04 import generate_chapter_04
from chapter05 import generate_chapter_05
from chapter06 import generate_chapter_06
from chapter07 import generate_chapter_07
from chapter08 import generate_chapter_08
from chapter09 import generate_chapter_09
from chapter10 import generate_chapter_10
from chapter11 import generate_chapter_11
from chapter12 import generate_chapter_12
from appendices import generate_appendices
from bibliography import generate_bibliography

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>On the Directional Drift-Diffusion of Vorticity, Scale-Invariant Strain Bounds, and Ancient Rigidity for the 3D Incompressible Navier–Stokes Equations</title>
<!-- KaTeX Styles and Scripts -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}], throwOnError: false, strict: false});"></script>
<style>
{css_styles}
</style>
</head>
<body>

{body_content}

</body>
</html>
"""

def clean_latex(text):
    """
    Normalizes LaTeX backslashes so that math equations render in standard horizontal format
    instead of stacking vertically due to extraneous '\\' newline tokens.
    """
    # Protect cases and matrix row breaks
    text = re.sub(r'\\\\(?=\s*(?:[0-9]|\\text|\\end))', '__KATEX_ROWBREAK__', text)
    text = re.sub(r'\\\\(?=\s*\\\\\s*(?:[0-9]|\\text|\\end))', '__KATEX_ROWBREAK__', text)
    
    # Replace all extraneous double backslashes with single backslash
    text = text.replace('\\\\', '\\')
    
    # Restore genuine matrix/cases row breaks
    text = text.replace('__KATEX_ROWBREAK__', '\\\\')
    
    return text

def assemble_thesis():
    print("Assembling dissertation chapters and front matter...")
    body_parts = [
        generate_front_matter(),
        generate_chapter_01(),
        generate_chapter_02(),
        generate_chapter_03(),
        generate_chapter_04(),
        generate_chapter_05(),
        generate_chapter_06(),
        generate_chapter_07(),
        generate_chapter_08(),
        generate_chapter_09(),
        generate_chapter_10(),
        generate_chapter_11(),
        generate_chapter_12(),
        generate_appendices(),
        generate_bibliography()
    ]
    
    raw_body = "\n".join(body_parts)
    print("Normalizing equation backslashes for horizontal math formatting...")
    full_body = clean_latex(raw_body)
    
    full_html = HTML_TEMPLATE.replace("{css_styles}", CSS_STYLES).replace("{body_content}", full_body)
    
    output_html_path = os.path.abspath("university_thesis_monograph.html")
    with open(output_html_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"Generated clean HTML treatise: {output_html_path} ({len(full_html)} bytes)")
    return output_html_path

def compile_pdf(html_path):
    output_pdf_path = os.path.abspath("university_thesis_monograph.pdf")
    monograph_pdf_path = os.path.abspath("monograph.pdf")
    
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    if not os.path.exists(chrome_path):
        chrome_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
        
    print(f"Launching browser engine from: {chrome_path}")
    print(f"Loading document: {html_path}")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=chrome_path, headless=True)
        page = browser.new_page()
        page.goto(f"file:///{html_path.replace(os.sep, '/')}", wait_until="networkidle")
        
        print("Ensuring KaTeX renders all equations horizontally...")
        page.evaluate("""() => {
            if (typeof renderMathInElement !== 'undefined') {
                renderMathInElement(document.body, {
                    delimiters: [
                        {left: '$$', right: '$$', display: true},
                        {left: '$', right: '$', display: false}
                    ],
                    throwOnError: false,
                    strict: false
                });
            }
        }""")
        
        # Wait for fonts to be ready
        page.evaluate("() => document.fonts.ready")
        page.wait_for_timeout(5000)
        
        # Check rendered math count
        math_count = page.evaluate("() => document.querySelectorAll('.katex').length")
        print(f"Successfully rendered {math_count} KaTeX mathematical formulas.")
        
        print("Rendering publication-grade PDF via Chromium printing pipeline...")
        page.pdf(
            path=output_pdf_path,
            format="A4",
            margin={"top": "2.2cm", "bottom": "2.2cm", "left": "2cm", "right": "2cm"},
            print_background=True,
            display_header_footer=True,
            header_template="<div style='font-size:7.5pt; font-family:Times New Roman, serif; width:100%; text-align:center; color:#64748b; padding-bottom:4pt;'>Rohit Ramakant Prajapati &bull; Doctoral Dissertation &bull; 3D Navier–Stokes Geometric Regularity</div>",
            footer_template="<div style='font-size:7.5pt; font-family:Times New Roman, serif; width:100%; text-align:center; color:#64748b; padding-top:4pt;'><span class='pageNumber'></span> / <span class='totalPages'></span></div>"
        )
        browser.close()
        
    if os.path.exists(output_pdf_path):
        # Update monograph.pdf in thesis_generator
        shutil.copyfile(output_pdf_path, monograph_pdf_path)
        
        # Update root repo PDFs and HTML
        repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        root_monograph = os.path.join(repo_root, "monograph.pdf")
        root_thesis = os.path.join(repo_root, "university_thesis_monograph.pdf")
        root_html = os.path.join(repo_root, "university_thesis_monograph.html")
        try:
            shutil.copyfile(output_pdf_path, root_monograph)
            shutil.copyfile(output_pdf_path, root_thesis)
            shutil.copyfile(html_path, root_html)
            print("Updated root repository monograph.pdf and university_thesis_monograph.pdf")
        except Exception as e:
            print(f"Warning updating root repo files: {e}")
            
        # Copy to Desktop directories
        desktop_folders = [
            r"C:\Users\praja\Desktop\research paper 3",
            r"C:\Users\praja\Desktop\research paper 2"
        ]
        for df in desktop_folders:
            if os.path.exists(df):
                try:
                    shutil.copyfile(output_pdf_path, os.path.join(df, "university_thesis_monograph.pdf"))
                    shutil.copyfile(output_pdf_path, os.path.join(df, "monograph.pdf"))
                    shutil.copyfile(html_path, os.path.join(df, "university_thesis_monograph.html"))
                    print(f"Updated Desktop directory: {df}")
                except Exception as e:
                    print(f"Warning updating {df}: {e}")
                    
        # Count pages
        try:
            with open(output_pdf_path, "rb") as f:
                data = f.read()
                page_matches = re.findall(rb'/Type\s*/Page\b', data)
                page_count = len(page_matches)
                print("=" * 60)
                print(f"SUCCESS: Generated {output_pdf_path}")
                print(f"File Size: {os.path.getsize(output_pdf_path) / (1024*1024):.2f} MB")
                print(f"Total Page Count: {page_count} pages")
                print("=" * 60)
                return page_count
        except Exception as e:
            print(f"Error checking page count: {e}")
            return -1
    else:
        print("ERROR: Output PDF was not generated.")
        return 0

if __name__ == "__main__":
    html_file = assemble_thesis()
    compile_pdf(html_file)
