
# 📚 Chatbot Theme Identifier (Wasserstoff Internship Task)

This project builds a Generative AI-powered chatbot that performs document-level research, answers user queries, and synthesizes key themes across ArXiv research papers.

## ✅ Features

- Downloads 75 ArXiv papers using a query (e.g. Machine Learning)
- Extracts text using PyMuPDF and Tesseract
- Embeds data into FAISS vector DB using OpenAI embeddings
- Answers queries with citations (DOCID + excerpt)
- Synthesizes themes across documents using LangChain + OpenAI
- Streamlit interface for input/output

## 🗂 Folder Structure

```
chatbot_theme_identifier/
├── backend/app/services/    # Arxiv download, OCR, embeddings, QA
├── backend/data/            # PDFs, text, and FAISS index
├── demo/streamlit_app.py    # Streamlit frontend
└── README.md
```

## 🚀 How to Run

### 1. Clone the repo and install requirements

```bash
cd backend
pip install -r requirements.txt
```

### 2. Add your `.env` file

Create `.env` in `backend/` with:

```
OPENAI_API_KEY=your_key_here
```

### 3. Download ArXiv papers

```bash
python app/services/arxiv_downloader.py
```

### 4. Extract text using OCR

```bash
python app/services/text_processor.py
```

### 5. Create vector store

```bash
python app/services/vector_store.py
```

### 6. Run Streamlit UI

```bash
streamlit run demo/apk.py
```

## 📬 Contact

For any issues, contact: yadavyash337@gmail.com
