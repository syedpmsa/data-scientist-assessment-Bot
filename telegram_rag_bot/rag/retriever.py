import sqlite3
import numpy as np
from sentence_transformers import SentenceTransformer

DB_PATH = "rag/db.sqlite"
model = SentenceTransformer("all-MiniLM-L6-v2")

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def retrieve(query, k=3):
    query_emb = model.encode(query)

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT content, embedding FROM chunks")

    scored_chunks = []
    for content, emb_blob in cur.fetchall():
        emb = np.frombuffer(emb_blob, dtype=np.float32)
        score = cosine_similarity(query_emb, emb)
        scored_chunks.append((score, content))

    conn.close()

    scored_chunks.sort(reverse=True)
    return [chunk for _, chunk in scored_chunks[:k]]
