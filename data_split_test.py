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


#Import OS, Document Loader, Text Splitter, Bedrock Embeddings, Vector DB, VectorStoreIndex, Bedrock-LLM
# 1. Import required libraries
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain.embeddings import BedrockEmbeddings
# from langchain.vectorstores import VectorStoreIndexCreator
# from langchain.llms import Bedrock
# from langchain_community.vectorstores import FAISS
# from langchain_aws import BedrockLLM

#2 LOAD DOC
data_load=PyPDFLoader('https://www.upl-ltd.com/images/people/downloads/Leave-Policy-India.pdf')

#3 text splitter
documents = data_load.load()

splitter = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n", " ", ""],
    chunk_size=100,
    chunk_overlap=20
)

texts = splitter.split_documents(documents)

print(texts[:2])