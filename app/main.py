from fastapi import FastAPI

from app.models import AskRequest, AskResponse
from app.services.rag import ask_rag

app = FastAPI(
    title="AI Assistant",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/ask", response_model=AskResponse)
def ask_question(request: AskRequest):
    answer, source, score = ask_rag(request.question)

    return AskResponse(
        answer=answer,
        source=source,
        score=score,
    )