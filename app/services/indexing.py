from app.services.embeddings import create_embedding


def build_index(chunks: list[str]) -> list[dict]:
    index = []

    for chunk in chunks:
        embedding = create_embedding(chunk)

        index.append(
            {
                "text": chunk,
                "embedding": embedding,
            }
        )

    return index