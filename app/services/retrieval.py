import math

from app.services.embeddings import create_embedding


def cosine_similarity(
    vector_a: list[float],
    vector_b: list[float],
) -> float:
    dot_product = sum(
        a * b
        for a, b in zip(vector_a, vector_b)
    )

    magnitude_a = math.sqrt(
        sum(a * a for a in vector_a)
    )

    magnitude_b = math.sqrt(
        sum(b * b for b in vector_b)
    )

    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0

    return dot_product / (magnitude_a * magnitude_b)


def find_relevant_chunks(
    question: str,
    index: list[dict],
    top_k: int = 3,
    threshold: float = 0.45,
) -> list[dict]:
    question_embedding = create_embedding(question)

    results = []

    for item in index:
        score = cosine_similarity(
            question_embedding,
            item["embedding"],
        )

        if score >= threshold:
            results.append(
                {
                    "section": item["section"],
                    "text": item["text"],
                    "score": score,
                }
            )

    results.sort(
        key=lambda item: item["score"],
        reverse=True,
    )

    return results[:top_k]