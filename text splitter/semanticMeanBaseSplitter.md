# Recursive Character-Based (Approximated Semantic) Text Splitter Explanation

This document explains the Python script in [semanticMeanBaseSplitter.py](file:///g:/Gen%20AI/Gen-AI-/text%20splitter/semanticMeanBaseSplitter.py) step-by-step. This script demonstrates how to split a PDF document into smaller segments using LangChain's `RecursiveCharacterTextSplitter`.

---

## What is Recursive Character Splitting?
The `RecursiveCharacterTextSplitter` is the recommended splitter for generic text. 
* It takes a list of separators (by default: `["\n\n", "\n", " ", ""]`) and attempts to split the text by them in order.
* First, it tries to split by double newlines (`\n\n`) to keep paragraphs together. If a chunk is still too large, it tries single newlines (`\n`), then spaces (` `), and finally individual characters (`""`).
* This approach keeps semantically related parts of the text (like paragraphs and sentences) together as much as possible, which is why it is often used as a standard baseline for "semantic" grouping.

> [!NOTE]
> *Note on Naming:* While this script is named `semanticMeanBaseSplitter.py`, it uses a recursive character splitter rather than an embedding-based semantic splitter (like LangChain's `SemanticChunker`, which uses machine learning embeddings to calculate semantic similarity thresholds).

---

## Code Breakdown

### 1. Importing Libraries
```python
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
```
* **`PyPDFLoader`**: Loads the PDF pages and parses the text into LangChain `Document` objects.
* **`RecursiveCharacterTextSplitter`**: The splitter that recursively breaks down the text keeping paragraphs/sentences intact.

---

### 2. Loading the PDF Document
```python
data = PyPDFLoader("GRU.pdf")
docs = data.load()
```
* **What it does**: Initializes the PDF loader for `GRU.pdf` and extracts the text content into the `docs` list.

---

### 3. Configuring the Splitter
```python
splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 200
)
```
* **`chunk_size = 1000`**: Sets the maximum character limit for each chunk to **1000 characters**.
* **`chunk_overlap = 200`**: Sets a **200-character** overlap between consecutive chunks. This ensures that context at the boundary is not lost between chunks.

---

### 4. Splitting and Printing Count
```python
chunks = splitter.split_documents(docs)
print(len(chunks))
```
* **`split_documents(docs)`**: Splits the loaded documents into character-based chunks.
* **`print(len(chunks))`**: Prints the total number of chunks generated from the PDF.
