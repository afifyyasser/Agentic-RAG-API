# Agentic RAG API

An **Agentic Retrieval-Augmented Generation (RAG) API** built with **FastAPI** that enables querying knowledge from multiple data sources, including **PDF documents** and **web pages**.

The system uses **LangChain**, **Chroma Vector Database**, and **OpenAI (GPT-4o)** to create a searchable knowledge base and generate accurate, context-aware answers.

---

## 🧠 Architecture Overview

User Query
↓
FastAPI (/ask)
↓
RAG Service
↓
Retriever (Chroma Vector Store)
↓
Relevant Chunks
↓
LLM (OpenAI GPT-4o)
↓
Final Answer


---

## ✨ Features

- Load and process documents from:
  - Local PDF files
  - Web URLs
- Recursive text chunking with overlap
- Vector embeddings using OpenAI
- Chroma-based semantic retrieval
- Retrieval-Augmented Generation (RAG) pipeline
- RESTful API interface
- Agent-like workflow (Index → Query)

---

## 📁 Project Structure

project/
│
├── main.py # FastAPI application entry point
├── rag_service.py # RAG pipeline logic
├── loaders.py # PDF & Web document loaders
├── splitter.py # Text splitting logic
├── tools.py # Vector store and retriever
├── schemas.py # API request/response schemas
│
├── data/
│ └── pdfs/ # Local PDF documents
│
├── .env # Environment variables
├── README.md


---

## ⚙️ How It Works

### 1. Load Documents
- Reads all PDF files from the `data/pdfs` directory
- Loads content from predefined web URLs

### 2. Split Documents
- Chunk size: `600`
- Chunk overlap: `150`

### 3. Create Vector Store
- Generates embeddings using OpenAI
- Stores vectors in Chroma

### 4. Build RAG Chain
- Uses `RetrievalQA` from LangChain
- LLM: `ChatOpenAI (gpt-4o)`
- Retrieves relevant chunks and generates answers

---

## 🚀 API Endpoints

### ✅ Health Check
GET /status


**Response**
```json
{
  "status": "ok"
}
🧱 Build Index
Builds the vector index.
Must be called before querying.

POST /index
Response

{
  "status": "index_built"
}
❓ Ask a Question
POST /ask
Request

{
  "query": "What programs does Machinfy offer?"
}
Response

{
  "answer": "Machinfy offers programs in AI, Data Science, UI/UX, and more."
}
🔐 Environment Variables
Create a .env file in the project root:

OPENAI_API_KEY=your_openai_api_key
📦 Installation
pip install fastapi uvicorn python-dotenv \
langchain langchain-community langchain-openai \
langchain-text-splitters langchain-chroma chromadb
▶️ Run the Application
uvicorn main:app --reload
API documentation (Swagger UI):

http://127.0.0.1:8000/docs
🌐 Data Sources
Local PDF documents

Web pages from machinfy.com

🔮 Future Improvements
Persistent vector store

Metadata-based filtering

Multi-agent orchestration

Streaming responses

Authentication and rate limiting

Caching and monitoring

📝 License
This project is intended for educational and experimental purposes.
