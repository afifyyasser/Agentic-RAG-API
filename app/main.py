from fastapi import FastAPI, HTTPException
from .schemas import QueryRequest, QueryResponse, StatusResponse
from .rag_service import RAGService

app = FastAPI(
    title="Agentic RAG API",
    description="PDF + Web RAG System using LangChain, Chroma, and OpenAI",
    version="1.0"
)

rag_service = RAGService()

@app.get("/status", response_model=StatusResponse)
def status():
    return {"status": "ok"}

@app.post("/index", response_model=StatusResponse)
def build_index():
    try:
        rag_service.build_index()
        return {"status": "index_built"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/ask", response_model=QueryResponse)
def ask_question(req: QueryRequest):
    try:
        answer = rag_service.ask(req.query)
        return {"answer": answer}
    except RuntimeError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
