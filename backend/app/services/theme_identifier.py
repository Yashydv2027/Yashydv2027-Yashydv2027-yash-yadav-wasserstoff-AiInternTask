
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

def identify_themes(citation_table):
    prompt_template = ChatPromptTemplate.from_template("""
You are an AI assistant. Given excerpts from various documents with IDs, identify and summarize key themes across them. Group documents under themes with short descriptions.

Output Format:
Theme 1 – [Short Title]:
 Description...
 Documents: DOC001, DOC002

Theme 2 – [Short Title]:
 Description...
 Documents: DOC003, DOC005, DOC007

Excerpts:
{citation_text}
""")
    citation_text = ""
    for i, row in enumerate(citation_table):
        doc_id = row['source'].replace(".txt", "").upper().replace("-", "").replace("_", "")
        citation_text += f"{doc_id}: {row['excerpt'][:500].replace('\n', ' ')}\n"

    messages = prompt_template.format_messages(citation_text=citation_text)
    response = llm(messages)
    return response.content

if __name__ == "__main__":
    sample_table = [
        {"source": "DOC001.txt", "excerpt": "This paper discusses the impact of optimization algorithms on training stability..."},
        {"source": "DOC002.txt", "excerpt": "Reinforcement learning models often suffer from reward sparsity issues..."},
    ]
    print(identify_themes(sample_table))
