import os
from dotenv import load_dotenv

load_dotenv()
OLLAMA_BASE_URL=os.getenv("OLLAMA_BASE_URL")
OLLAMA_MODEL=os.getenv("OLLAMA_MODEL")
OLLAMA_EMBEDDING_MODEL=os.getenv("OLLAMA_EMBEDDING_MODEL")
OLLAMA_EMBEDDING_API=os.getenv("OLLAMA_EMBEDDING_API")