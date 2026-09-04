from app.services.chunking import split_text
from app.services.document_loader import load_text_file
from app.services.indexing import build_index


class KnowledgeBase:
    def __init__(self):
        self.index: list[dict] = []

    def load(self, file_path: str) -> None:
        text = load_text_file(file_path)

        chunks = split_text(text)        
        

        self.index = build_index(chunks)


knowledge_base = KnowledgeBase()