from app.services.chunking import split_text
from app.services.document_loader import load_text_file
from app.services.indexing import build_index
from app.services.vector_store import create_collection, upsert_chunks


def main():
    text = load_text_file("data/company_faq.txt")

    chunks = split_text(text)

    index = build_index(chunks)

    vector_size = len(index[0]["embedding"])

    create_collection(vector_size=vector_size)

    upsert_chunks(index)

    print(f"Indexed {len(index)} chunks into Qdrant.")


if __name__ == "__main__":
    main()