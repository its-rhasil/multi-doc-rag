import fitz
from pathlib import Path

def load(pdf_path: str) -> list[dict]:
    
    pdf_path = Path(pdf_path)

    if not pdf_path.exists():
        raise FileNotFoundError(f"File Not found at path: {pdf_path}")
    
    with fitz.open(pdf_path) as document:
        pages = []
        for page_num, page in enumerate(document):
            text = page.get_text("text").strip()
            pages.append({
                "text": text,
                "metadata": {
                    "source": pdf_path.name,
                    "page_number": page_num + 1
                }
            })
    return pages
