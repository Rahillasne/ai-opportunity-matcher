import openai
import numpy as np

openai.api_key = "YOUR_API_KEY"

def get_embedding(text, model="text-embedding-ada-002"):
    result = openai.Embedding.create(input=[text], model=model)
    return result["data"][0]["embedding"]

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def rank_jobs(user_input, jobs):
    user_embedding = get_embedding(user_input)
    ranked = []
    for job in jobs:
        job_embedding = get_embedding(job["description"])
        similarity = cosine_similarity(user_embedding, job_embedding)
        ranked.append((job, similarity))
    ranked.sort(key=lambda x: x[1], reverse=True)
    return [job for job, _ in ranked]
