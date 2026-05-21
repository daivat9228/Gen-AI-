# LangChain & Mistral AI Text Processing Pipeline Explanation

This document explains the Python script in [main.py](file:///g:/Gen%20AI/Gen-AI-/text%20splitter/main.py) step-by-step. The script is designed to load a PDF file, split its text into manageable chunks, format a prompt, send it to a Mistral AI LLM, and print the response.

---

## Code Breakdown

### 1. Loading Environment Variables
```python
from dotenv import load_dotenv
load_dotenv()
```
* **What it does**: Reads a `.env` file in your project root directory and loads any environment variables defined inside it (like `MISTRAL_API_KEY`).
* **Why it's needed**: LangChain integrations (like Mistral AI) require authentication keys, which are safely retrieved from environment variables rather than hardcoded in the source code.

---

### 2. Importing Dependencies
```python
from langchain_mistralai import ChatMistralAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
```
* **`ChatMistralAI`**: The integration class to interact with Mistral AI chat models.
* **`PyPDFLoader`**: A document loader that reads PDF files and converts pages into LangChain `Document` objects.
* **`ChatPromptTemplate`**: A class used to create structured templates for messaging LLMs.
* **`RecursiveCharacterTextSplitter`**: A text splitter that splits documents into smaller segments using a list of default separators (like double newlines, single newlines, spaces) to keep semantic paragraphs together.

---

### 3. Initializing the Model
```python
model = ChatMistralAI(model = "mistral-small-latest")
```
* **What it does**: Instantiates the chat interface for Mistral AI, specifying the `"mistral-small-latest"` model.

---

### 4. Loading the PDF Document
```python
loader = PyPDFLoader("GRU.pdf")
docs = loader.load()
```
* **What it does**: Initializes the PDF loader for a file named `GRU.pdf` and calls `.load()` to extract the text content and metadata from all pages in the PDF.
* **Result**: `docs` becomes a list of `Document` objects, where each object represents a single page from the PDF.

---

### 5. Configuring and Splitting Text Chunks
```python
splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 200
)

chunks = splitter.split_documents(docs)
```
* **`chunk_size = 1000`**: Defines the target size of each text chunk (maximum of 1000 characters).
* **`chunk_overlap = 200`**: Sets a 200-character overlap between consecutive chunks. This ensures that context (like sentences cut in half) is preserved across chunk boundaries.
* **`split_documents(docs)`**: Executes the splitting logic on the loaded pages, returning a list of smaller `Document` chunks.

---

### 6. Formatting the Prompt and Invoking the Model
```python
prompt  = template.formate_message(data = chunks)

result = model.invoke(prompt)
print(result.content)
```
* **What it attempts to do**: Format a message with the split chunks, send it to the Mistral AI model, and print the generated response.

> [!WARNING]
> **Identified Issues in this Section:**
> 1. **Undefined Variable**: The variable `template` is not defined or initialized anywhere in the script. You need to create `template` using `ChatPromptTemplate`.
> 2. **Typo in Method Name**: `formate_message` is misspelled and does not exist. It should be `format_messages` or `format`.
>
> ### Suggested Fix
> To make the script run successfully, you can define a template and format it like this:
>
> ```python
> # 1. Define a template
> template = ChatPromptTemplate.from_template(
>     "Summarize the following document content:\n\n{data}"
> )
> 
> # 2. Format the template (passing text instead of the list of Document objects directly)
> doc_content = "\n\n".join([c.page_content for c in chunks])
> prompt = template.format(data=doc_content)
> ```
