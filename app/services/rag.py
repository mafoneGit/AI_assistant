from app.services.knowledge_base import knowledge_base
from app.services.llm import generate_answer
from app.services.retrieval import find_relevant_chunks


def ask_rag(question: str) -> tuple[str, list[dict], float]:
    results = find_relevant_chunks(
        question,
        top_k=3,
        threshold=0.45,
)

    if not results:
        return (
            "I don't know based on the available information.",
            [],
            0.0,
        )

    context = "\n\n".join(
        item["text"] for item in results
    )

    answer = generate_answer(
        question=question,
        context=context,
    )

    sources = [
        {
            "section": item["section"],
            "text": item["text"],
        }
        for item in results
    ]

    best_score = results[0]["score"]

    return answer, sources, best_score