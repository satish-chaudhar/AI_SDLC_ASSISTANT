from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from config import EMBED_MODEL, VECTOR_STORE_DIR

def load_and_embed(file_path):
    loader = PyPDFLoader(file_path)
    pages = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
    chunks = splitter.split_documents(pages)

    embeddings = OpenAIEmbeddings(model=EMBED_MODEL)
    vectordb = Chroma.from_documents(chunks, embedding=embeddings, persist_directory=VECTOR_STORE_DIR)
    vectordb.persist()

    return vectordb
