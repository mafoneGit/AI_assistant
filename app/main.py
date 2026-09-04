from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.models import AskRequest, AskResponse
from app.services.knowledge_base import knowledge_base
from app.services.rag import ask_rag


@asynccontextmanager
async def lifespan(app: FastAPI):
    knowledge_base.load("data/company_faq.txt")

    yield


app = FastAPI(
    title="AI Assistant",
    version="0.1.0",
    lifespan=lifespan,
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