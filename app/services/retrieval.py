from app.services.embeddings import create_embedding
from app.services.vector_store import COLLECTION_NAME, client


def find_relevant_chunks(
    question: str,
    top_k: int = 3,
    threshold: float = 0.45,
) -> list[dict]:
    question_embedding = create_embedding(question)

    search_result = client.query_points(
        collection_name=COLLECTION_NAME,
        query=question_embedding,
        limit=top_k,
        score_threshold=threshold,
    )

    results = []

    for point in search_result.points:
        results.append(
            {
                "section": point.payload["section"],
                "text": point.payload["text"],
                "score": point.score,
            }
        )

    return results