from app.services.embeddings import create_embedding


def build_index(chunks: list[dict]) -> list[dict]:
    index = []

    for chunk in chunks:
        embedding = create_embedding(chunk["text"])

        index.append(
            {
                "section": chunk["section"],
                "text": chunk["text"],
                "embedding": embedding,
            }
        )

    return index