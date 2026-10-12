
from app.services.retrieval_service import RetrievalService

retrieval_service = RetrievalService()

query = input("Ask a question: ")

results = retrieval_service.search(query, top_k=3)

print("\nMost relevant documents:\n")

for result in results:
    print(f"ID: {result['id']}")
    print(f"Text: {result['text']}")
    print(f"Similarity: {result['score']:.4f}")
    print("-" * 40)