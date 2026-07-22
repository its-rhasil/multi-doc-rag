import hashlib

class ChunkIdGenerator:

    @staticmethod
    def generate_id(documenthash: str, page_num: int, chunk_index: int):

        text = f"{documenthash}:{page_num}:{chunk_index}"
        return hashlib.sha256(text.encode()).hexdigest()