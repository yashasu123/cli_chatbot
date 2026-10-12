
from app.services.embedding_service import EmbeddingService
from app.services.document_embedding_service import (
    DocumentEmbeddingService
)
from app.util.similarity import cosine_similarity


class RetrievalService:

    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.document_embedding_service = DocumentEmbeddingService()

    def search(self, query: str, top_k: int = 3) -> list[dict]:
        query_vector = self.embedding_service.generate_embedding(query)

        embedded_documents = (
            self.document_embedding_service
            .generate_document_embeddings()
        )

        results = []

        for document in embedded_documents:
            score = cosine_similarity(
                query_vector,
                document["embedding"]
            )

            results.append({
                "id": document["id"],
                "text": document["text"],
                "score": score
            })
        
    #    for r in results:
    #       print(f"text:{r["text"]}\n score:{r["score"]}")

        results.sort(
            key=lambda result: result["score"],
            reverse=True
        )

        return results[:top_k]