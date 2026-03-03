# 🧠 Mini RAG (Fully Local & Free)

A simple Retrieval-Augmented Generation (RAG) system built entirely with open-source tools.

No API key. No cloud. Runs locally.

---

## 🚀 Tech Stack

- **Embedding**: sentence-transformers (all-MiniLM-L6-v2)
- **Vector Search**: FAISS
- **LLM**: Ollama (Llama3)
- **Language**: Python

---

## 🏗 How It Works

1. Convert documents into embeddings
2. Store embeddings in FAISS
3. Embed user question
4. Retrieve top-k relevant chunks
5. Send context to Llama3
6. Generate grounded answer

---

## ⚙️ Setup

### 1️⃣ Install Ollama

```bash
ollama pull llama3
```

### 2️⃣ Create Environment

```bash
python -m venv venv
venv\Scripts\activate
pip install sentence-transformers faiss-cpu numpy
```

## ▶️ Usage

Build index:
```bash
python build_index.py
```

Ask questions:
```bash
python ask.py
```
---

## 📁 Structure

```
try-RAG/
├── data/
│   ├── knowledge.txt
|
├── build_index.py
├── ask.py

```

---
## 📝 Commit Message Guideline

ใช้มาตรฐาน **Conventional Commits**

### Format
`type: description`

### Types

| Type | Description | Example |
|------|------------|----------|
| feat | เพิ่ม feature | `feat: add cosine similarity` |
| fix | แก้ bug | `fix: correct retrieval logic` |
| docs | แก้เอกสาร | `docs: update README` |
| refactor | ปรับโครงสร้าง | `refactor: improve chunking` |
| style | ปรับ format | `style: fix indentation` |
| chore | งานจิปาถะ | `chore: update dependency` |

---