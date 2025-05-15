import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from backend.app.services.qa_chain import build_qa_chain, ask_question
from backend.app.services.theme_identifier import identify_themes

st.set_page_config(page_title="Research Theme Chatbot", layout="wide")
st.title("📚 ArXiv Research Theme Identifier Chatbot")

query = st.text_input("🔍 Ask a question related to the research papers:")

if query:
    st.info("Processing your query...")
    qa_chain = build_qa_chain()
    answer, citations = ask_question(qa_chain, query)

    st.subheader("📌 Synthesized Answer")
    st.markdown(answer)

    st.subheader("📄 Document-wise Responses")
    citation_rows = []
    for row in citations:
        doc_id = row['source'].replace(".txt", "").upper().replace("-", "").replace("_", "")
        citation_rows.append([doc_id, row["excerpt"]])

    st.table(citation_rows)

    st.subheader("🧠 Identified Themes Across Documents")
    theme_summary = identify_themes(citations)
    st.markdown(theme_summary)
