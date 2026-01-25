import os
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

def create_vector_store(chunks, persist_directory="./chroma_db_fisheries"):
    """
    Initializes embeddings and creates a persistent ChromaDB vector store.
    """
    # Using a fast, local HuggingFace model for embeddings
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # Creating the vector database from document chunks
    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=persist_directory
    )
    
    print(f"Vector store created and saved at: {persist_directory}")
    return vector_db

def load_vector_store(persist_directory="./chroma_db_fisheries"):
    """
    Loads an existing vector store for querying.
    """
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    if os.path.exists(persist_directory):
        return Chroma(
            persist_directory=persist_directory,
            embedding_function=embeddings
        )
    else:
        print("Error: Vector store directory not found.")
        return None