import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
 
load_dotenv()
 
PDF_PATH = "data/clinic_faq.pdf"
CHROMA_DIR = "chroma_db"
 
def ingest():
    print("Loading PDF...")
    loader = PyPDFLoader(PDF_PATH)
    documents = loader.load()
 
    print(f"Loaded {len(documents)} page(s). Splitting into chunks...")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=60,
        separators=["\n\n", "\n", ".", " "]
    )
    chunks = splitter.split_documents(documents)
    print(f"Created {len(chunks)} chunks.")
 
    print("Loading embedding model (first time may take 2-3 mins to download)...")
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"}
    )
 
    print("Building ChromaDB vector store...")
    if os.path.exists(CHROMA_DIR):
        import shutil
        shutil.rmtree(CHROMA_DIR)
 
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DIR
    )
    vectorstore.persist()
    print(f"Vector store saved to '{CHROMA_DIR}' folder.")
    print("Ingestion complete! You can now run website_bot.py or whatsapp_bot.py")
 
if __name__ == "__main__":
    ingest()