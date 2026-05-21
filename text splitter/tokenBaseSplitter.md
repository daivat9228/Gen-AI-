# Token-Based Text Splitter Explanation

This document explains the Python script in [tokenBaseSplitter.py](file:///g:/Gen%20AI/Gen-AI-/text%20splitter/tokenBaseSplitter.py) step-by-step. This script demonstrates how to split a PDF document into smaller chunks based on LLM tokens (using tiktoken) rather than characters.

---

## What is a Token?
Before diving into the code, it's important to understand what a **token** is. Language models (like GPT or Mistral) don't see words as letters or even full words. They process text in chunks of characters called tokens. 
* A rough rule of thumb is that **1 token ≈ 4 characters** or **0.75 words** in English.
* Splitting by tokens instead of characters ensures your chunks stay within the strict token context limits of LLMs.

---

## Code Breakdown

### 1. Importing Libraries
```python
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import TokenTextSplitter
```
* **`PyPDFLoader`**: A document loader designed to read PDF files and partition them page-by-page into LangChain `Document` objects.
* **`TokenTextSplitter`**: A text splitter that measures chunk sizes using **tokens** (using the `gpt2` encoding by default via `tiktoken`).

---

### 2. Loading the PDF Document
```python
data = PyPDFLoader("text splitter/GRU.pdf")
docs = data.load()
```
* **What it does**: Initializes the PDF loader for the file `GRU.pdf` located inside the `text splitter` directory and loads the text content.
* **Result**: `docs` is a list where each element represents a page from the PDF containing page content and metadata.

---

### 3. Configuring the Token Text Splitter
```python
splitter = TokenTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 100
)
```
* **`chunk_size = 1000`**: Specifies that each chunk should contain a maximum of **1000 tokens**.
* **`chunk_overlap = 100`**: Configures an overlap of **100 tokens** between adjacent chunks. This helps prevent context loss by repeating 100 tokens at the start of each new chunk.

---

### 4. Splitting and Printing Output
```python
chunks = splitter.split_documents(docs)
print(chunks[0].page_content)   
```
* **`split_documents(docs)`**: Splits the loaded PDF documents into the defined token chunks.
* **`print(chunks[0].page_content)`**: Prints the text content of the very first chunk (`chunks[0]`) to the console.
