from app.services.chunking import split_text
from app.services.document_loader import load_text_file
from app.services.indexing import build_index
from app.services.llm import generate_answer
from app.services.retrieval import find_most_relevant_chunk


def ask_rag(question: str) -> tuple[str, str, float]:
    text = load_text_file("data/company_faq.txt")

    chunks = split_text(text, chunk_size=120)

    index = build_index(chunks)

    best_chunk, score = find_most_relevant_chunk(
        question,
        index,
    )

    answer = generate_answer(
        question=question,
        context=best_chunk,
    )

    return answer, best_chunk, score