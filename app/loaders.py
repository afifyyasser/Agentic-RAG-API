import os
from langchain_community.document_loaders import PyPDFLoader, WebBaseLoader

PDF_DIR = "data/pdfs"
URLS = [
    "https://machinfy.com/",
    "https://machinfy.com/page/2/",
    "https://machinfy.com/program/ai-for-hr/",
    "https://machinfy.com/program/ai-for-education/",
    "https://machinfy.com/program/machinfy-ui-ux-design/",
    "https://machinfy.com/program/machinfy-professional-data-analysis-course/",
    "https://machinfy.com/program/machinfy-professional-data-science-and-ai/",
    "https://machinfy.com/program/software-testing-level-1/"
]

def load_all_documents():
    docs = []

    # PDF
    if os.path.exists(PDF_DIR):
        for file in os.listdir(PDF_DIR):
            if file.lower().endswith(".pdf"):
                path = os.path.join(PDF_DIR, file)
                loader = PyPDFLoader(path)
                docs.extend(loader.load())

    # web
    for url in URLS:
        docs.extend(WebBaseLoader(url).load())

    return docs
