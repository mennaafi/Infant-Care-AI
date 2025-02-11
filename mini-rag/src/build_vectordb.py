from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from src.helpers.config import get_settings  

settings = get_settings()
EMBEDDING_MODEL_NAME = settings.EMBEDDING_MODEL_NAME

class VectorDBBuilder:
    def __init__(self, data_path="data", chunk_size=800, chunk_overlap=200, embedding_model_name=EMBEDDING_MODEL_NAME):
        self.data_path = data_path
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.embedding_model_name = embedding_model_name  
        self.documents = []
        self.text_chunks = []
        self.embedding_model = None

    def load_documents(self):
        loader = DirectoryLoader(self.data_path, glob="*.pdf", loader_cls=PyPDFLoader)
        self.documents = loader.load()
        return self.documents

    def split_text_into_chunks(self):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=self.chunk_size, chunk_overlap=self.chunk_overlap)
        self.text_chunks = text_splitter.split_documents(self.documents)
        return self.text_chunks

    def download_embedding_model(self):
        self.embedding_model = HuggingFaceEmbeddings(model_name=self.embedding_model_name)
        return self.embedding_model

    def process(self):
        self.load_documents()
        self.split_text_into_chunks()
        self.download_embedding_model()
        print(f" Processed {len(self.text_chunks)} text chunks.")

