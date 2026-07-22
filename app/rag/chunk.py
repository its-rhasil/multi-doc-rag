from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

def chunk(pages: list, chunk_size: int = 1000, chunk_overlap: int = 200):
    textsplitter = RecursiveCharacterTextSplitter(
        chunk_size = chunk_size,
        chunk_overlap = chunk_overlap,
        length_function = len
    )
    documents = []
    for page in pages:
        document = Document(
            page_content=page["text"],
            metadata = page["metadata"]
        )
        documents.append(document)

    chunks = textsplitter.split_documents(documents)

    return chunks