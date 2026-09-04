from app.services.knowledge_base import knowledge_base
from app.services.llm import generate_answer
from app.services.retrieval import find_relevant_chunks


def ask_rag(question: str) -> tuple[str, str, float]:
    results = find_relevant_chunks(
        question,
        knowledge_base.index,
        top_k=3,
    )

    context = "\n\n".join(
        text for text, score in results
    )

    answer = generate_answer(
        question=question,
        context=context,
    )

    best_score = results[0][1]

    return answer, context, best_score