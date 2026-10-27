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
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]});"></script>
<style>
{css_styles}
</style>
</head>
<body>

{body_content}

</body>
</html>
"""

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
    
    full_body = "\n".join(body_parts)
    full_html = HTML_TEMPLATE.replace("{css_styles}", CSS_STYLES).replace("{body_content}", full_body)
    
    output_html_path = os.path.abspath("university_thesis_monograph.html")
    with open(output_html_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"Generated HTML treatise: {output_html_path} ({len(full_html)} bytes)")
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
        
        print("Waiting for KaTeX mathematical typesetting engine to render...")
        page.wait_for_timeout(6000)
        
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
        shutil.copyfile(output_pdf_path, monograph_pdf_path)
        print(f"Updated primary repository PDF: {monograph_pdf_path}")
        
        # Check desktop path if available
        desktop_dir = r"C:\Users\praja\Desktop\research paper 2"
        if os.path.exists(desktop_dir):
            desktop_pdf = os.path.join(desktop_dir, "university_thesis_monograph.pdf")
            desktop_monograph = os.path.join(desktop_dir, "monograph.pdf")
            try:
                shutil.copyfile(output_pdf_path, desktop_pdf)
                shutil.copyfile(output_pdf_path, desktop_monograph)
                print(f"Copied PDF to user desktop directory: {desktop_pdf}")
            except Exception as e:
                print(f"Could not copy to desktop directory: {e}")
                
        # Count pages
        try:
            with open(output_pdf_path, "rb") as f:
                data = f.read()
                page_matches = re.findall(rb'/Type\s*/Page\b', data)
                page_count = len(page_matches)
                print(f"==================================================")
                print(f"SUCCESS: Generated {output_pdf_path}")
                print(f"File Size: {os.path.getsize(output_pdf_path) / (1024*1024):.2f} MB")
                print(f"Total Page Count: {page_count} pages")
                print(f"==================================================")
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
