from app.services.embedding_service import EmbeddingService
from app.document_store import documents

class DocumentEmbeddingService:
    def __init__(self):
        self.embedding_service=EmbeddingService()
    
    def generate_document_embeddings(self):
        embedded_documents = []

        for document in documents.documents:
            vector= self.embedding_service.generate_embedding(document["text"])
            embedded_documents.append({
                "id": document["id"],
                "text": document["text"],
                "embedding": vector
            })
        return embedded_documents