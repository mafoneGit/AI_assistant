from pydantic import BaseModel


class AskRequest(BaseModel):
    question: str


class Source(BaseModel):
    section: str
    text: str


class AskResponse(BaseModel):
    answer: str
    sources: list[Source]
    score: float