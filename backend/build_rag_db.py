
import os
import sys

# Ensure we can import from rag.src
sys.path.append(os.getcwd())

from rag.src.data_loader import load_fisheries_data
from rag.src.vectorstore import create_vector_store
from langchain_text_splitters import RecursiveCharacterTextSplitter

def build_db():
    print("🚀 Starting Vector DB Generation...")
    
    # 1. Load Documents
    # We need to temporarily patch data_loader to look in the right place relative to backend/
    # Or we can just ensure the path in data_loader is correct. 
    # data_loader.py uses './data/fisheries/'
    # If we run from backend/, it should be './rag/data/fisheries/'
    
    # Let's verify paths
    data_path = "./rag/data/fisheries/"
    if not os.path.exists(data_path):
        print(f"❌ Error: Data path {data_path} not found.")
        return

    print(f"📂 Loading PDFs from {data_path}...")
    
    # Use PyPDFLoader directly here to avoid modifying data_loader.py if it's brittle
    from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
    loader = DirectoryLoader(data_path, glob="./*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()
    
    if not documents:
        print("⚠️ No documents found! Check if PDFs exist.")
        return
        
    print(f"✅ Loaded {len(documents)} documents.")
    
    # 2. Split Text
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(documents)
    print(f"🧩 Split into {len(chunks)} chunks.")
    
    # 3. Create Vector Store
    # This will save to ./chroma_db_fisheries (relative to backend/)
    # which matches what search.py expects when running main.py
    create_vector_store(chunks, persist_directory="./chroma_db_fisheries")
    print("🎉 Vector Store ready!")

if __name__ == "__main__":
    build_db()
