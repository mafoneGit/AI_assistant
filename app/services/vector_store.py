from qdrant_client import QdrantClient
from qdrant_client.models import Distance, PointStruct, VectorParams

COLLECTION_NAME = "salon_knowledge"

client = QdrantClient(url="http://localhost:6333")


def create_collection(vector_size: int) -> None:
    collections = client.get_collections().collections
    collection_names = [collection.name for collection in collections]

    if COLLECTION_NAME not in collection_names:
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=vector_size,
                distance=Distance.COSINE,
            ),
        )


def upsert_chunks(chunks: list[dict]) -> None:
    points = []

    for index, chunk in enumerate(chunks):
        points.append(
            PointStruct(
                id=index,
                vector=chunk["embedding"],
                payload={
                    "section": chunk["section"],
                    "text": chunk["text"],
                },
            )
        )

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points,
    )