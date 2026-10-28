import os
import subprocess
from playwright.sync_api import sync_playwright

BASE_DIR = r"C:\Users\praja\.gemini\antigravity\scratch\navier_stokes_research"
CHAPTERS_DIR = os.path.join(BASE_DIR, "chapters")
OUTPUT_HTML = os.path.join(BASE_DIR, "monograph_full_treatise.html")
OUTPUT_PDF = os.path.join(BASE_DIR, "monograph.pdf")
DESKTOP_DIR = r"C:\Users\praja\Desktop\research paper 2"

HTML_HEADER = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>On the Directional Drift-Diffusion of Vorticity, Scale-Invariant Strain Bounds, and Ancient Rigidity for the 3D Incompressible Navier–Stokes Equations</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]});"></script>
<style>
  @page {
    size: A4;
    margin: 2.2cm 2cm 2.2cm 2cm;
  }
  body {
    font-family: 'Times New Roman', Times, serif;
    font-size: 10.5pt;
    line-height: 1.5;
    color: #111;
    margin: 0;
    padding: 0;
    text-align: justify;
  }
  .header-section {
    text-align: center;
    margin-bottom: 25pt;
  }
  h1.title {
    font-size: 16pt;
    font-weight: bold;
    margin-top: 10pt;
    margin-bottom: 8pt;
    line-height: 1.3;
  }
  .subtitle {
    font-size: 11.5pt;
    color: #2b6cb0;
    margin-bottom: 15pt;
    font-style: italic;
  }
  .author-block {
    font-size: 12pt;
    font-weight: bold;
    margin-bottom: 4pt;
  }
  .affiliation {
    font-size: 9.5pt;
    font-style: italic;
    color: #444;
    margin-bottom: 4pt;
  }
  .date {
    font-size: 9.5pt;
    color: #666;
    margin-bottom: 20pt;
  }
  .abstract-box {
    margin: 0 15pt 20pt 15pt;
    padding: 12pt 15pt;
    background-color: #f7fafc;
    border-left: 3.5pt solid #2b6cb0;
    font-size: 9pt;
    line-height: 1.45;
  }
  .abstract-title {
    text-align: center;
    font-weight: bold;
    font-size: 10pt;
    margin-bottom: 6pt;
    letter-spacing: 1.5px;
    color: #2b6cb0;
  }
  .toc-box {
    margin: 0 15pt 25pt 15pt;
    padding: 12pt 15pt;
    background-color: #edf2f7;
    border: 1px solid #cbd5e0;
    font-size: 9pt;
  }
  .toc-title {
    font-weight: bold;
    text-align: center;
    margin-bottom: 8pt;
    letter-spacing: 1px;
  }
  .toc-list {
    list-style: none;
    padding-left: 0;
    margin: 0;
    line-height: 1.6;
  }
  h2.chapter-title {
    font-size: 13pt;
    font-weight: bold;
    color: #1a202c;
    border-bottom: 1.5pt solid #2b6cb0;
    padding-bottom: 4pt;
    margin-top: 25pt;
    margin-bottom: 12pt;
    page-break-after: avoid;
  }
  h3 {
    font-size: 11pt;
    font-weight: bold;
    color: #2d3748;
    margin-top: 15pt;
    margin-bottom: 6pt;
    page-break-after: avoid;
  }
  .theorem-box {
    margin: 12pt 0;
    padding: 10pt 14pt;
    background-color: #f8fafc;
    border: 1px solid #cbd5e1;
    border-left: 3.5pt solid #0284c7;
    page-break-inside: avoid;
  }
  .alert-box {
    border-left-color: #dc2626;
    background-color: #fef2f2;
  }
  .equation {
    margin: 10pt 0;
    text-align: center;
  }
  table.data-table {
    width: 100%;
    border-collapse: collapse;
    margin: 12pt 0;
    font-size: 9pt;
  }
  table.data-table th, table.data-table td {
    border: 1px solid #cbd5e1;
    padding: 6pt 8pt;
    text-align: left;
  }
  table.data-table th {
    background-color: #f1f5f9;
    font-weight: bold;
  }
  pre {
    background-color: #f1f5f9;
    border: 1px solid #e2e8f0;
    padding: 8pt;
    font-size: 8pt;
    font-family: Consolas, monospace;
    overflow-x: auto;
  }
  ol.bib-list {
    font-size: 8.5pt;
    line-height: 1.5;
    padding-left: 18pt;
  }
  ol.bib-list li {
    margin-bottom: 5pt;
  }
</style>
</head>
<body>
"""

HTML_FOOTER = """
</body>
</html>
"""

def assemble_html():
    chapter_files = [
        "ch00_front_matter.html",
        "ch01.html",
        "ch02_ch03.html",
        "ch04_ch05.html",
        "ch06_ch07.html",
        "ch08_ch09.html",
        "ch10_ch11_app.html"
    ]
    
    content = [HTML_HEADER]
    for fname in chapter_files:
        fpath = os.path.join(CHAPTERS_DIR, fname)
        if os.path.exists(fpath):
            with open(fpath, "r", encoding="utf-8") as f:
                content.append(f.read())
        else:
            print(f"Warning: {fpath} not found!")
            
    content.append(HTML_FOOTER)
    full_html = "\n".join(content)
    
    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"Assembled master HTML: {OUTPUT_HTML} ({len(full_html)} bytes)")

def compile_pdf():
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    if not os.path.exists(chrome_path):
        chrome_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
        
    print(f"Compiling PDF via Playwright with {chrome_path}...")
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=chrome_path, headless=True)
        page = browser.new_page()
        page.goto(f"file:///{OUTPUT_HTML.replace(os.sep, '/')}", wait_until="networkidle")
        print("Waiting for KaTeX rendering...")
        page.wait_for_timeout(4000)
        
        page.pdf(
            path=OUTPUT_PDF,
            format="A4",
            margin={"top": "2cm", "bottom": "2cm", "left": "1.8cm", "right": "1.8cm"},
            print_background=True,
            display_header_footer=True,
            header_template="<div style='font-size:7.5pt; width:100%; text-align:center; color:#666;'>Rohit Ramakant Prajapati &bull; 3D Navier–Stokes Geometric Regularity Treatise</div>",
            footer_template="<div style='font-size:7.5pt; width:100%; text-align:center; color:#666;'><span class='pageNumber'></span> / <span class='totalPages'></span></div>"
        )
        browser.close()
        
    size_kb = os.path.getsize(OUTPUT_PDF) / 1024
    print(f"Successfully compiled PDF: {OUTPUT_PDF} ({size_kb:.2f} KB)")

def copy_to_desktop():
    print(f"Copying monograph assets to Desktop: {DESKTOP_DIR}...")
    os.makedirs(DESKTOP_DIR, exist_ok=True)
    subprocess.run([
        "robocopy", BASE_DIR, DESKTOP_DIR, "monograph.pdf", "monograph_full_treatise.html",
        "/IS", "/IT"
    ], check=False)
    print("Desktop assets synchronized.")

if __name__ == "__main__":
    assemble_html()
    compile_pdf()
    copy_to_desktop()
