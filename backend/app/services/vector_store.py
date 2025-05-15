import os

from langchain.docstore.document import Document
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()


def create_vector_store(text_dir, faiss_index_path):
    docs = []
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

    for file in os.listdir(text_dir):
        if file.endswith(".txt"):
            with open(os.path.join(text_dir, file), "r", encoding="utf-8") as f:
                content = f.read()
                if not content.strip():
                    continue
                chunks = splitter.split_text(content)
                for chunk in chunks:
                    if len(chunk) < 10000:  # skip any absurdly long chunks
                        docs.append(
                            Document(page_content=chunk, metadata={"source": file})
                        )

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local(faiss_index_path)
    print(f"✅ Vector store created at {faiss_index_path}")


def load_vector_store(faiss_index_path):
    embeddings = OpenAIEmbeddings()
    return FAISS.load_local(
        faiss_index_path, embeddings, allow_dangerous_deserialization=True
    )


if __name__ == "__main__":
    create_vector_store("data/arxiv_texts", "data/faiss_index")
