import sqlite3
from sentence_transformers import SentenceTransformer
from pathlib import Path
import textwrap
import numpy as np

DB_PATH = "rag/db.sqlite"
DOCS_PATH = "rag/docs"
CHUNK_SIZE = 300

model = SentenceTransformer("all-MiniLM-L6-v2")

def chunk_text(text):
    return textwrap.wrap(text, CHUNK_SIZE)

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS chunks (
    id INTEGER PRIMARY KEY,
    content TEXT,
    embedding BLOB
)
""")

for file in Path(DOCS_PATH).glob("*.md"):
    text = file.read_text()
    for chunk in chunk_text(text):
        embedding = model.encode(chunk).astype(np.float32).tobytes()
        cur.execute(
            "INSERT INTO chunks (content, embedding) VALUES (?, ?)",
            (chunk, embedding)
        )

conn.commit()
conn.close()

print("✅ Documents ingested successfully")
