# PDF Parser Implementation
# Strategy:
#   1. PyMuPDF extracts text page-by-page with layout preservation
#   2. pdfplumber extracts tables with row/column structure intact
#   3. Combine: replace raw table text with structured table dicts
#   (Future) Tesseract OCR for scanned pages (image-only PDFs)

import fitz
import pdfplumber
from pathlib import Path
import re


def structure_table(raw_table, page_num, table_idx):
    if not raw_table or len(raw_table) < 2:
        return None
    
    # First raw is header
    headers = [str(cell or "").strip() for cell in raw_table[0]]
    rows = []
    for raw_row in raw_table[1:]:
        row = {
            headers[i]: str(cell or "").strip()
            for i, cell in enumerate(raw_row)
            if i < len(headers)
        }
        if any(row.values()):  # skip empty rows
            rows.append(row)

    if not rows:
        return None
    
    # Create a markdown representation for embedding
    md_lines = ["| " + " | ".join(headers) + " |"]
    md_lines.append("| " + " | ".join(["---"] * len(headers)) + " |")
    for row in rows:
        md_lines.append("| " + " | ".join(row.get(h, "") for h in headers) + " |")

    return {
        "page": page_num,
        "table_index": table_idx,
        "headers": headers,
        "rows": rows,
        "row_count": len(rows),
        "col_count": len(headers),
        "markdown": "\n".join(md_lines),
    }



def parse_pdf(pdf_path):
    pages_text = [] # raw text of each page in order, with layout preserved
    tables = []
    pages = [] # pages with everything structured
    total_pages = 0

    # Extract text with PyMuPDF for better layout preservation
    with fitz.open(pdf_path) as doc:
        total_pages = len(doc)
        for page_num, page in enumerate(doc):
            text = page.get_text("text", sort=True)
            pages_text.append(text)
            pages.append({
                "page_num": page_num + 1,
                "text": text,
                "tables": []
            })

    # Extract tables with pdfplumber for structured data
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages):
            raw_tables = page.extract_tables()
            for table_idx, raw_table in enumerate(raw_tables):
                structured_table = structure_table(raw_table, page_num, table_idx)
                if structured_table:
                    page_text = pages[page_num]["text"]
                    table_title = None
                    for line in page_text.split("\n"):
                        if re.match(r"^\s*table\s*\d*", line.lower()):
                            table_title = line.strip()
                    
                    structured_table["table_title"] = table_title
                    tables.append(structured_table)
                    pages[page_num]["tables"].append(structured_table)

    full_text = "\n\n".join(pages_text)

    return {
        "doc_type": "pdf",
        "doc_id": pdf_path.stem,
        "source_path": pdf_path,
        "content": full_text, # full raw text of the entire document unstructured
        # "raw_pages": pages_text, # list of raw text for each page in order
        "page_count": total_pages,
        "pages": pages, # list of dicts with page_num, text, and tables for each page
        "tables": tables, # list of all tables with structure and metadata
        "metadata": {
            "file_name": pdf_path.name,
            "file_size_bytes": pdf_path.stat().st_size,
            "has_tables": len(tables) > 0,
            "has_scanned_pages": False,  # Placeholder for future OCR detection
        }
    }

if __name__ == "__main__":
    PDF_PATH = r"D:\Ubaid\github\RAGLens\data\thesis.pdf"
    PDF_PATH = Path(PDF_PATH)
    result = parse_pdf(PDF_PATH)
    print(f"Document ID: {result['doc_id']}")
    print(f"Parsed PDF: {result['source_path']}")
    print(f"Page Count: {result['page_count']}")
    print(f"Tables Found: {len(result['tables'])}")
    print(f"File Name: {result['metadata']['file_name']}")
    print(f"File Size: {result['metadata']['file_size_bytes']} bytes")
    print(f"Has Tables: {result['metadata']['has_tables']}")
    print(f"Has Scanned Pages: {result['metadata']['has_scanned_pages']}")
    # print a certain page
    n = 15
    # print(f"\n--- Page {n} Text ---")
    # print(result["pages"][n - 1])
    # See any tables found
    from pprint import pprint
    # pprint(result[0], depth=3)
    pprint(result["pages"][14])