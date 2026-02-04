def build_prompt(context, question):
    return f"""
You are a helpful assistant.
Answer the question ONLY using the context below.
If the answer is not found, say "I don't know".

Context:
{context}

Question:
{question}

Answer:
"""
