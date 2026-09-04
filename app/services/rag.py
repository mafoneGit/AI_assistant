from app.services.knowledge_base import knowledge_base
from app.services.llm import generate_answer
from app.services.retrieval import find_most_relevant_chunk


def ask_rag(question: str) -> tuple[str, str, float]:
    best_chunk, score = find_most_relevant_chunk(
        question,
        knowledge_base.index,
    )

    answer = generate_answer(
        question=question,
        context=best_chunk,
    )

    return answer, best_chunk, score