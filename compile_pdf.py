import subprocess
import os
import sys

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
if not os.path.exists(chrome):
    chrome = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

base_dir = r"C:\Users\praja\.gemini\antigravity\scratch\navier_stokes_research"
html = os.path.join(base_dir, "university_thesis_monograph.html")
pdf = os.path.join(base_dir, "university_thesis_monograph.pdf")
user_data = r"C:\Users\praja\.gemini\antigravity\scratch\chrome_temp"

html_url = "file:///" + html.replace("\\", "/")

cmd = [
    chrome,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--no-pdf-header-footer",
    f"--user-data-dir={user_data}",
    f"--print-to-pdf={pdf}",
    html_url
]

print("Executing Chrome CLI:")
print(" ".join(cmd))
res = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
print("Exit code:", res.returncode)
if res.stdout:
    print("STDOUT:", res.stdout)
if res.stderr:
    print("STDERR:", res.stderr)

if os.path.exists(pdf):
    size = os.path.getsize(pdf)
    mtime = os.path.getmtime(pdf)
    print(f"SUCCESS: {pdf} generated! Size: {size} bytes, mtime: {mtime}")
else:
    print("FAILED to generate PDF.")
