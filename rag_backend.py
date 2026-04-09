#Steps in Building HR Q&A Solution with RAG – Backend Code

#Import OS, Document Loader, Text Splitter, Bedrock Embeddings, Vector DB, VectorStoreIndex, Bedrock-LLM
#Define the data source and load data with PDFLoader (https://…/Leave-Policy-India.pdf)
#Split the text based on Character, Tokens etc. Recursively split by character – ["\n\n", "\n", " "]
#Create Embeddings – client connection

#5a. Create Vector DB, Store Embeddings and Index for Search – VectorStoreIndexCreator

#5b. Create index for HR Report

#5c. Wrap within a function

#6a. Write a function to connect to Bedrock Foundation Model

#6b. Write a function which searches the user prompt, searches the best match from Vector DB and sends both to LLM

#Index creation → https://api.python.langchain.com/en/latest/indexes/langchain.indexes.vectorstore.VectorStoreIndexCreator.


# rag_backend.py

# rag_backend.py

import json
import boto3
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_aws import BedrockEmbeddings

# ---------------- LOAD DOCUMENT ----------------
data_load = PyPDFLoader(
    "https://www.upl-ltd.com/images/people/downloads/Leave-Policy-India.pdf"
)
documents = data_load.load()

# ---------------- TEXT SPLITTING ----------------
splitter = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n", " ", ""],
    chunk_size=100,
    chunk_overlap=20
)
texts = splitter.split_documents(documents)

# ---------------- BEDROCK CLIENT ----------------
bedrock_client = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"
)

# ---------------- EMBEDDINGS ----------------
data_embeddings = BedrockEmbeddings(
    client=bedrock_client,
    model_id="amazon.titan-embed-text-v1"
)

print("PDF loaded successfully")
print(f"Number of chunks: {len(texts)}")
print("Embeddings object created successfully")

# ---------------- VECTOR STORE ----------------
vectorstore = FAISS.from_documents(texts, data_embeddings)
print("Vector DB created successfully")

# ---------------- DIRECT MISTRAL INVOCATION ----------------
def hr_llm(prompt: str) -> str:
    model_id = "mistral.mistral-large-2402-v1:0"
    # If this still fails, change only this line to:
    # model_id = "mistral.mixtral-8x7b-instruct-v0:1"

    formatted_prompt = f"<s>[INST] {prompt} [/INST]"

    request_body = {
        "prompt": formatted_prompt,
        "max_tokens": 200,
        "temperature": 0.1
    }

    response = bedrock_client.invoke_model(
        modelId=model_id,
        body=json.dumps(request_body),
        contentType="application/json",
        accept="application/json",
    )

    model_response = json.loads(response["body"].read())
    return model_response["outputs"][0]["text"]

# ---------------- RAG FUNCTION ----------------
def hr_rag_response(question: str) -> str:
    print("Question received:", question)

    docs = vectorstore.similarity_search(question, k=2)
    print(f"Retrieved {len(docs)} documents")

    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = f"""
You are an HR assistant.
Answer only from the given context.
If the answer is not in the context, say: "I could not find that in the document."

Context:
{context}

Question:
{question}
"""

    print("Sending to LLM...")
    response = hr_llm(prompt)
    print("LLM responded!")

    return response

if __name__ == "__main__":
    answer = hr_rag_response("What is leave policy?")
    print("\nFinal Answer:\n")
    print(answer)