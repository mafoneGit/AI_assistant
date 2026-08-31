import math

from app.services.embeddings import create_embedding


def cosine_similarity(vector_a: list[float], vector_b: list[float]) -> float:
    dot_product = sum(a * b for a, b in zip(vector_a, vector_b))

    magnitude_a = math.sqrt(sum(a * a for a in vector_a))
    magnitude_b = math.sqrt(sum(b * b for b in vector_b))

    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0

    return dot_product / (magnitude_a * magnitude_b)


def find_most_relevant_chunk(
    question: str,
    index: list[dict],
) -> tuple[str, float]:
    question_embedding = create_embedding(question)

    best_chunk = ""
    best_score = -1.0

    for item in index:
        score = cosine_similarity(
            question_embedding,
            item["embedding"],
        )

        if score > best_score:
            best_score = score
            best_chunk = item["text"]

    return best_chunk, best_score