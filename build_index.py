import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# โหลดโมเดล embedding ฟรี
model = SentenceTransformer("all-MiniLM-L6-v2")

# โหลดเอกสาร
with open("data/knowledge.txt", "r", encoding="utf-8") as f:
    texts = f.read().split("\n")

# สร้าง embedding
embeddings = model.encode(texts)

# สร้าง FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

# เซฟ index
faiss.write_index(index, "index.faiss")
np.save("texts.npy", texts)

print("Index built successfully.")