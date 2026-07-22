from app.rag.chunk_id_generator import ChunkIdGenerator

def index_chunk(chunks):

    for index, chunk in enumerate(chunks):
        chunk.metadata["chunk_index"] = index
        chunk.metadata["chunk_id"] = ChunkIdGenerator.generate_id(
            chunk.metadata["document_hash"], chunk.metadata["page_number"], index
        )
    return chunks