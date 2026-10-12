
from app.services.document_embedding_service import (DocumentEmbeddingService)


service = DocumentEmbeddingService()

embedded_documents = service.generate_document_embeddings()

for document in embedded_documents:
    print("\nDocument ID:", document["id"])
    print("Text:", document["text"])
    print("Vector dimensions:", len(document["embedding"]))
    