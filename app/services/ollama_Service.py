import requests

from app.config.settings import OLLAMA_BASE_URL, OLLAMA_MODEL


class OllamaService:

    def generate(self, prompt: str) -> str:

        response = requests.post(
            f"{OLLAMA_BASE_URL}/api/generate",
            json={
                "model": OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False
            }
        )

        response.raise_for_status()

        data = response.json()

        return data["response"]