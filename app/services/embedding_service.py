import requests

from app.config.settings import OLLAMA_BASE_URL, OLLAMA_EMBEDDING_MODEL, OLLAMA_EMBEDDING_API 


class EmbeddingService:

    def generate_embedding(self, text: str) -> list[float]:
        response = requests.post(f"{OLLAMA_BASE_URL}{OLLAMA_EMBEDDING_API}", 
        json={
        "model": OLLAMA_EMBEDDING_MODEL,
        "prompt": text
        })

        response.raise_for_status()

        data = response.json()

        return data["embedding"]