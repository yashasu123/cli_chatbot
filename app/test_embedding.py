
from app.services.embedding_service import EmbeddingService
from app.util.similarity import cosine_similarity
embedding_service = EmbeddingService()

sentence_a = "I love learning Python."
sentence_b = "Python programming is fun."
sentence_c = "I like eating pizza."

vector_a = embedding_service.generate_embedding(sentence_a)
vector_b = embedding_service.generate_embedding(sentence_b)
vector_c = embedding_service.generate_embedding(sentence_c)

print("Sentence A dimensions:", len(vector_a))
print("Sentence A :", vector_a[:5])
print("Sentence B dimensions:", len(vector_b))
print("Sentence B :", vector_b[:5])
print("Sentence C dimensions:", len(vector_c))
print("Sentence C :", vector_c[:5])

score_ab = cosine_similarity(vector_a, vector_b)
score_ac = cosine_similarity(vector_a, vector_c)

print(f"A vs B: {score_ab:.10f}")
print(f"A vs C: {score_ac:.10f}")