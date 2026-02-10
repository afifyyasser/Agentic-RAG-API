import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_classic.chains import RetrievalQA

from .loaders import load_all_documents
from .splitter import split_documents
from .tools import create_retriever

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class RAGService:
    def __init__(self):
        self.qa = None

    def build_index(self):
        # Load documents
        docs = load_all_documents()

        #chunking
        chunks = split_documents(docs)

        # Retriever
        retriever = create_retriever(chunks)

        # LLM
        llm = ChatOpenAI(
            openai_api_key=OPENAI_API_KEY,
            model_name="gpt-4o",
            temperature=0
        )

        # RAG Chain
        self.qa = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=retriever,
            return_source_documents=False
        )

    def ask(self, query: str) -> str:
        if not self.qa:
            raise RuntimeError("RAG index not built. Call /index first.")
        output = self.qa.invoke({"query": query})
        return output["result"]
