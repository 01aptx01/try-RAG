import faiss
import numpy as np
import subprocess
from sentence_transformers import SentenceTransformer

# โหลด embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# โหลด index
index = faiss.read_index("index.faiss")
texts = np.load("texts.npy", allow_pickle=True)

question = input("Ask something: ")

# embed คำถาม
query_vector = model.encode([question])

# ค้น top 2
D, I = index.search(np.array(query_vector), k=2)

context = "\n".join([texts[i] for i in I[0]])

prompt = f"""
Answer based only on this context:

{context}

Question: {question}
"""

# เรียก Ollama
result = subprocess.run(
    ["ollama", "run", "llama3"],
    input=prompt,
    text=True,
    capture_output=True
)

print("\nAnswer:")
print(result.stdout)