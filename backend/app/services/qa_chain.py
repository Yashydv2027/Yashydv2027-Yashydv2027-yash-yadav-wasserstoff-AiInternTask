
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from .vector_store import load_vector_store

def build_qa_chain():
    vectorstore = load_vector_store("backend/data/faiss_index")
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5})
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=True)
    return qa

def ask_question(qa_chain, query):
    result = qa_chain(query)
    answer = result['result']
    sources = result['source_documents']

    citation_table = []
    for doc in sources:
        citation_table.append({
            "source": doc.metadata.get("source", "Unknown"),
            "excerpt": doc.page_content[:300].strip() + "...",
        })

    return answer, citation_table

if __name__ == "__main__":
    qa = build_qa_chain()
    ans, citations = ask_question(qa, "What are the key challenges in reinforcement learning?")
    print(ans)
    for c in citations:
        print(f"{c['source']}: {c['excerpt'][:200]}")