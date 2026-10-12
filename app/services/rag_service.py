
from app.services.retrieval_service import RetrievalService
from app.services.ollama_Service import OllamaService


class RAGService:

    def __init__(self):
        self.retrieval_service = RetrievalService()
        self.ollama_service = OllamaService()

    def generate_answer(self, question: str) -> str:
        results = self.retrieval_service.search(
            query=question,
            top_k=3
        )

        context="\n".join(result["text"] for result in results)

        prompt = f"""
You are a helpful assistant.

Answer the user's question using the context below.
If the context does not contain enough information, say so.
Do not invent facts that are not supported by the context.

Context:
{context}

User question:
{question}

Answer:
"""

        return self.ollama_service.generate(prompt)