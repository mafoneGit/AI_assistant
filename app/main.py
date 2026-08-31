from fastapi import FastAPI

from app.models import AskRequest, AskResponse

app = FastAPI(
    title="AI Assistant",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/ask", response_model=AskResponse)
def ask_question(request: AskRequest):
    return AskResponse(
        answer=f"You asked: {request.question}"
    )