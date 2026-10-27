# Master CSS styles for the university thesis monograph

CSS_STYLES = """
  @page {
    size: A4;
    margin: 2.2cm 2cm 2.2cm 2cm;
  }
  
  *, *:before, *:after {
    box-sizing: border-box;
  }
  
  body {
    font-family: 'Times New Roman', Times, 'Nimbus Roman No9 L', serif;
    font-size: 10pt;
    line-height: 1.55;
    color: #111827;
    margin: 0;
    padding: 0;
    text-align: justify;
    text-justify: inter-word;
    background-color: #ffffff;
  }

  /* Page break utilities */
  .page-break {
    page-break-before: always;
    break-before: page;
  }
  
  .no-break {
    page-break-inside: avoid;
    break-inside: avoid;
  }

  /* Title and University Front Matter */
  .univ-header {
    text-align: center;
    margin-top: 35pt;
    margin-bottom: 25pt;
  }
  .univ-logo-text {
    font-size: 13pt;
    font-weight: bold;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: #1e3a8a;
    margin-bottom: 5pt;
  }
  .univ-sublogo {
    font-size: 10pt;
    font-style: italic;
    color: #4b5563;
    margin-bottom: 30pt;
  }
  h1.thesis-title {
    font-size: 19pt;
    font-weight: 800;
    line-height: 1.35;
    color: #0f172a;
    margin-top: 20pt;
    margin-bottom: 12pt;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }
  .thesis-subtitle {
    font-size: 12pt;
    color: #2563eb;
    font-style: italic;
    margin-bottom: 35pt;
    line-height: 1.4;
  }
  .thesis-author {
    font-size: 13pt;
    font-weight: bold;
    color: #111827;
    margin-bottom: 4pt;
  }
  .thesis-degree-text {
    font-size: 10pt;
    color: #374151;
    margin-top: 25pt;
    margin-bottom: 25pt;
    line-height: 1.6;
    max-width: 80%;
    margin-left: auto;
    margin-right: auto;
  }
  .thesis-meta-box {
    margin-top: 30pt;
    font-size: 9.5pt;
    color: #4b5563;
    line-height: 1.6;
  }

  /* Standard Headings */
  h1.chapter-num {
    font-size: 13pt;
    font-weight: 800;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #2563eb;
    margin-top: 30pt;
    margin-bottom: 4pt;
    page-break-after: avoid;
  }
  h2.chapter-title {
    font-size: 16pt;
    font-weight: bold;
    color: #0f172a;
    border-bottom: 2pt solid #2563eb;
    padding-bottom: 6pt;
    margin-top: 0;
    margin-bottom: 18pt;
    page-break-after: avoid;
    line-height: 1.3;
  }
  h3.section-title {
    font-size: 12pt;
    font-weight: bold;
    color: #1e293b;
    margin-top: 20pt;
    margin-bottom: 8pt;
    page-break-after: avoid;
    border-left: 3pt solid #3b82f6;
    padding-left: 8pt;
  }
  h4.subsection-title {
    font-size: 10.5pt;
    font-weight: bold;
    color: #334155;
    margin-top: 14pt;
    margin-bottom: 6pt;
    page-break-after: avoid;
    font-style: italic;
  }

  /* Academic Environments */
  .theorem-box, .lemma-box, .prop-box, .def-box, .remark-box, .alert-box {
    margin: 12pt 0;
    padding: 10pt 14pt;
    border-radius: 2pt;
    page-break-inside: avoid;
    font-size: 9.8pt;
    line-height: 1.5;
  }
  .theorem-box {
    background-color: #f8fafc;
    border: 1px solid #cbd5e1;
    border-left: 4pt solid #1d4ed8;
  }
  .lemma-box {
    background-color: #f0fdf4;
    border: 1px solid #bbf7d0;
    border-left: 4pt solid #16a34a;
  }
  .prop-box {
    background-color: #fdf4ff;
    border: 1px solid #f5d0fe;
    border-left: 4pt solid #9333ea;
  }
  .def-box {
    background-color: #eff6ff;
    border: 1px solid #bfdbfe;
    border-left: 4pt solid #2563eb;
  }
  .remark-box {
    background-color: #f8fafc;
    border: 1px solid #e2e8f0;
    border-left: 4pt solid #64748b;
    font-style: normal;
  }
  .alert-box {
    background-color: #fef2f2;
    border: 1px solid #fecaca;
    border-left: 4pt solid #dc2626;
  }
  .proof-box {
    margin: 8pt 0 14pt 0;
    padding-left: 12pt;
    border-left: 1.5pt solid #cbd5e1;
    font-size: 9.8pt;
  }
  .proof-title {
    font-weight: bold;
    font-style: italic;
    color: #334155;
  }
  .qed {
    float: right;
    font-weight: bold;
    color: #1e293b;
  }

  /* Math Equations */
  .equation {
    margin: 10pt 0;
    text-align: center;
    overflow-x: auto;
    page-break-inside: avoid;
  }

  /* Tables */
  table.academic-table {
    width: 100%;
    border-collapse: collapse;
    margin: 14pt 0;
    font-size: 9pt;
    page-break-inside: avoid;
  }
  table.academic-table th, table.academic-table td {
    border-top: 1px solid #cbd5e1;
    border-bottom: 1px solid #cbd5e1;
    padding: 6pt 8pt;
    text-align: left;
    vertical-align: top;
  }
  table.academic-table th {
    border-top: 2px solid #0f172a;
    border-bottom: 1.5px solid #0f172a;
    background-color: #f8fafc;
    font-weight: bold;
    color: #0f172a;
  }
  table.academic-table tfoot td {
    border-bottom: 2px solid #0f172a;
  }
  .table-caption {
    font-size: 8.8pt;
    font-weight: bold;
    color: #475569;
    margin-bottom: 5pt;
    text-align: left;
  }

  /* Code Blocks */
  pre.code-block {
    background-color: #f8fafc;
    border: 1px solid #cbd5e1;
    border-radius: 3pt;
    padding: 9pt 12pt;
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 8.5pt;
    line-height: 1.45;
    color: #0f172a;
    overflow-x: auto;
    page-break-inside: avoid;
  }

  /* Front Matter Boxes */
  .declaration-box {
    margin: 20pt 0;
    padding: 18pt 22pt;
    border: 1px solid #cbd5e1;
    background-color: #f8fafc;
    line-height: 1.7;
    font-size: 9.8pt;
  }
  .sig-grid {
    margin-top: 40pt;
    display: flex;
    justify-content: space-between;
  }
  .sig-item {
    width: 45%;
    border-top: 1px solid #475569;
    padding-top: 6pt;
    font-size: 9pt;
    text-align: center;
  }

  .toc-container {
    margin-top: 15pt;
    line-height: 1.6;
    font-size: 9.3pt;
  }
  .toc-row {
    display: flex;
    justify-content: space-between;
    margin-bottom: 3.5pt;
    border-bottom: 1px dotted #cbd5e1;
    padding-bottom: 1pt;
  }
  .toc-row.chapter {
    font-weight: bold;
    margin-top: 7pt;
    border-bottom: 1px solid #94a3b8;
    color: #0f172a;
  }
  .toc-row.section {
    padding-left: 18pt;
    color: #334155;
  }

  /* Footnotes and Citations */
  .bib-entry {
    margin-bottom: 8pt;
    padding-left: 24pt;
    text-indent: -24pt;
    font-size: 9pt;
    line-height: 1.5;
  }
"""
