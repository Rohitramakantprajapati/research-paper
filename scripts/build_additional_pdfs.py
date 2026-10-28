import os
import markdown
from playwright.sync_api import sync_playwright

def convert_md_to_pdf(md_filename, pdf_filename, title):
    with open(md_filename, "r", encoding="utf-8") as f:
        md_text = f.read()
        
    html_body = markdown.markdown(md_text, extensions=['extra', 'codehilite', 'tables'])
    
    html_doc = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>{title}</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {{delimiters: [{{left: '$$', right: '$$', display: true}}, {{left: '$', right: '$', display: false}}]}});"></script>
<style>
  @page {{
    size: A4;
    margin: 2cm;
  }}
  body {{
    font-family: 'Segoe UI', Helvetica, Arial, sans-serif;
    font-size: 10.5pt;
    line-height: 1.6;
    color: #24292f;
    margin: 0;
    padding: 0;
  }}
  h1 {{ font-size: 16pt; border-bottom: 2px solid #0969da; padding-bottom: 6px; margin-top: 10px; color: #1f2328; }}
  h2 {{ font-size: 13pt; border-bottom: 1px solid #d0d7de; padding-bottom: 4px; margin-top: 20px; color: #1f2328; }}
  h3 {{ font-size: 11.5pt; margin-top: 15px; color: #1f2328; }}
  pre {{ background: #f6f8fa; padding: 10px; border-radius: 6px; font-size: 9pt; overflow-x: auto; border: 1px solid #d0d7de; }}
  code {{ font-family: Consolas, monospace; background: #f6f8fa; padding: 2px 4px; border-radius: 4px; font-size: 9pt; }}
  table {{ border-collapse: collapse; width: 100%; margin: 15px 0; font-size: 9.5pt; }}
  th, td {{ border: 1px solid #d0d7de; padding: 6px 10px; text-align: left; }}
  th {{ background: #f6f8fa; }}
  blockquote {{ border-left: 4px solid #0969da; padding-left: 12px; color: #57606a; margin: 10px 0; }}
  hr {{ border: 0; height: 1px; background: #d0d7de; margin: 20px 0; }}
</style>
</head>
<body>
{html_body}
</body>
</html>"""

    temp_html = md_filename.replace(".md", "_temp.html")
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(html_doc)
        
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=chrome_path, headless=True)
        page = browser.new_page()
        page.goto(f"file:///{os.path.abspath(temp_html).replace(os.sep, '/')}", wait_until="networkidle")
        page.wait_for_timeout(2000)
        page.pdf(
            path=pdf_filename,
            format="A4",
            margin={"top": "2cm", "bottom": "2cm", "left": "2cm", "right": "2cm"},
            print_background=True,
            display_header_footer=True,
            header_template=f"<div style='font-size:8pt; width:100%; text-align:center; color:#666;'>{title}</div>",
            footer_template="<div style='font-size:8pt; width:100%; text-align:center; color:#666;'><span class='pageNumber'></span> / <span class='totalPages'></span></div>"
        )
        browser.close()
        
    if os.path.exists(temp_html):
        os.remove(temp_html)
        
    if os.path.exists(pdf_filename):
        print(f"SUCCESS: Generated {pdf_filename} ({os.path.getsize(pdf_filename)/1024:.2f} KB)")

if __name__ == "__main__":
    REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    letters_md = os.path.join(REPO_ROOT, "docs", "private-notes", "peer_review_cover_letters.md")
    letters_pdf = os.path.join(REPO_ROOT, "docs", "private-notes", "peer_review_cover_letters.pdf")
    arxiv_md = os.path.join(REPO_ROOT, "docs", "arxiv_submission_guide.md")
    arxiv_pdf = os.path.join(REPO_ROOT, "docs", "arxiv_submission_guide.pdf")

    if os.path.exists(letters_md):
        convert_md_to_pdf(letters_md, letters_pdf, "Peer-Review Cover Letters & Evaluation Package")
    if os.path.exists(arxiv_md):
        convert_md_to_pdf(arxiv_md, arxiv_pdf, "arXiv Submission Guide & Instructions")
