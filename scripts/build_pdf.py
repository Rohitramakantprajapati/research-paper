import os
from playwright.sync_api import sync_playwright

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD_DIR = os.path.join(REPO_ROOT, "paper", "build")

def generate_pdf():
    os.makedirs(BUILD_DIR, exist_ok=True)
    html_file = os.path.join(BUILD_DIR, "monograph_print.html")
    if not os.path.exists(html_file):
        # Fall back to repo root if present
        root_html = os.path.join(REPO_ROOT, "monograph_print.html")
        if os.path.exists(root_html):
            html_file = root_html
    pdf_file = os.path.join(BUILD_DIR, "monograph.pdf")
    
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    if not os.path.exists(chrome_path):
        chrome_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
        
    print(f"Loading {html_file}")
    print(f"Using Chrome binary: {chrome_path}")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=chrome_path, headless=True)
        page = browser.new_page()
        page.goto(f"file:///{html_file.replace(os.sep, '/')}", wait_until="networkidle")
        print("Waiting for KaTeX equation rendering...")
        page.wait_for_timeout(4000)
        
        print("Printing to PDF...")
        page.pdf(
            path=pdf_file,
            format="A4",
            margin={"top": "2.2cm", "bottom": "2.2cm", "left": "2cm", "right": "2cm"},
            print_background=True,
            display_header_footer=True,
            header_template="<div style='font-size:8pt; width:100%; text-align:center; color:#666;'>Rohit Ramakant Prajapati &bull; 3D Navier–Stokes Geometric Regularity</div>",
            footer_template="<div style='font-size:8pt; width:100%; text-align:center; color:#666;'><span class='pageNumber'></span> / <span class='totalPages'></span></div>"
        )
        browser.close()
        
    if os.path.exists(pdf_file):
        size_kb = os.path.getsize(pdf_file) / 1024
        print(f"SUCCESS: Generated {pdf_file} ({size_kb:.2f} KB)")
    else:
        print("ERROR: PDF was not generated.")

if __name__ == "__main__":
    generate_pdf()
