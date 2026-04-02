# RAG-Q-A-BOT-AWS-Bedrock-FAISS-Streamlit-
# 💼 Q&A System using RAG (AWS Bedrock + FAISS + Streamlit)

## 📌 Overview

This project is a Retrieval-Augmented Generation (RAG) based assistant that answers user questions from a company leave policy document. It combines semantic search with a Large Language Model (LLM) to generate accurate, context-aware responses.

---

## 🚀 Features

* 📄 Load and process Company policy PDF
* ✂️ Intelligent text chunking
* 🔍 Semantic search using vector embeddings
* 🤖 Context-aware answer generation
* 🌐 Interactive UI using Streamlit
* ☁️ AWS Bedrock integration for embeddings and LLM

---

## 🧠 Architecture

```text
User → Streamlit UI → Backend (Python)
        ↓
Document Loader (LangChain)
        ↓
Text Splitter
        ↓
Embeddings (AWS Bedrock)
        ↓
FAISS Vector Database
        ↓
Similarity Search (Top-K)
        ↓
LLM (AWS Bedrock - Mistral)
        ↓
Final Answer
```

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **LLM Provider:** AWS Bedrock (Mistral)
* **Embeddings:** Amazon Titan Embeddings
* **Vector Database:** FAISS
* **Framework:** LangChain (for data processing)

---

## 📂 Project Structure

```text
├── rag_backend.py      # RAG pipeline (loading, embeddings, retrieval, LLM)
├── rag_frontend.py     # Streamlit UI
├── client.py           #boto3 client connection
└── README.md           # Project documentation
```

---

## ⚙️ Installation

### 1. Clone repository

```bash
git clone https://github.com/your-username/hr-rag-bedrock.git
cd hr-rag-bedrock
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 AWS Setup

* Configure AWS credentials:

```bash
aws configure
```

* Ensure access to:

  * AWS Bedrock
  * Embedding model (`amazon.titan-embed-text-v1`)
  * Text model (`mistral.mistral-large-2402-v1:0`)

---

## ▶️ Run the Application

### Run Backend (optional test)

```bash
python rag_backend.py
```

### Run Frontend

```bash
streamlit run rag_frontend.py
```

---

## 💡 How It Works

1. The PDF is loaded and split into smaller chunks
2. Each chunk is converted into embeddings using AWS Bedrock
3. Embeddings are stored in FAISS for fast similarity search
4. User query is converted into embedding
5. Top-K relevant chunks are retrieved
6. Context + query is sent to the LLM
7. Model generates a grounded answer

---

## 📊 Key Concepts

* **RAG (Retrieval-Augmented Generation):** Combines retrieval + generation
* **Embeddings:** Numerical representation of text
* **Vector Search:** Finds semantically similar content
* **FAISS:** Efficient similarity search library

---

## 🔥 Why LangChain?

LangChain is used to simplify:

* Document loading (`PyPDFLoader`)
* Text splitting (`RecursiveCharacterTextSplitter`)
* Embeddings integration
* Vector store creation (FAISS)

---

## 📈 Future Improvements

* 💬 Chat history (multi-turn conversations)
* ⚡ Streaming responses
* 🌐 Deployment (AWS / Render)
* 🔐 Authentication system

---

## 👩‍💻 Author

**K Sai Thanmayi**



This project demonstrates practical implementation of RAG systems using modern GenAI tools and cloud-based LLMs.
