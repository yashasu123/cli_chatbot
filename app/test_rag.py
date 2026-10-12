
from app.services.rag_service import RAGService

rag_service = RAGService()

while True:
    question = input("\nYou: ").strip()

    if question.lower() in {"exit", "quit"}:
        break

    if not question:
        continue

    answer = rag_service.generate_answer(question)

    print("\nAssistant:", answer)