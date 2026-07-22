import fitz
from pathlib import Path
from app.rag.document_hasher import DocumentHasher

def load(pdf_path: str) -> list[dict]:
    document_hash = DocumentHasher.hash_document(pdf_path)
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
                    "page_number": page_num + 1,
                    "document_hash": document_hash
                }
            })
    return pages
