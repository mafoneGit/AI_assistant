from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(timeout=20.0)


def generate_answer(question: str, context: str) -> str:
    response = client.responses.create(
        model="gpt-5.5",
        input=[
            {
                "role": "system",
                "content": (
                    "Answer the user's question only using the provided context. "
                    "If the answer is not in the context, say that you don't know."
                ),
            },
            {
                "role": "user",
                "content": f"Context:\n{context}\n\nQuestion:\n{question}",
            },
        ],
    )

    return response.output_text