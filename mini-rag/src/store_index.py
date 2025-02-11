import os
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from src.build_vectordb import VectorDBBuilder
from src.helpers.config import get_settings

settings = get_settings()
PINECONE_API_KEY = settings.PINECONE_API_KEY
index_name = settings.PINECONE_INDEX_NAME

vector_db = VectorDBBuilder()
vector_db.process()

pc = Pinecone(api_key=PINECONE_API_KEY)

existing_indexes = [index["name"] for index in pc.list_indexes()]

if index_name in existing_indexes:
    print(f"Pinecone index '{index_name}' already exists. Skipping creation.")
else:
    print(f"Creating Pinecone index '{index_name}'...")
    pc.create_index(
        name=index_name,
        dimension=384,  # d: Based on embedding model 
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )
    print(f"Index '{index_name}' created successfully.")

docsearch = PineconeVectorStore.from_documents(
    documents=vector_db.text_chunks,
    index_name=index_name,
    embedding=vector_db.embedding_model
)

retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})
print("Pinecone index is ready, and retriever is set up.")
