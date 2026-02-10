from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
def create_retriever(chunks):
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma.from_documents(chunks, embeddings)
    return vectorstore.as_retriever(search_kwargs={"k": 5})
