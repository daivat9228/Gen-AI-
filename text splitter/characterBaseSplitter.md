# Character-Based Text Splitter Explanation

This document explains the Python script in [characterBaseSplitter.py](file:///g:/Gen%20AI/Gen-AI-/text%20splitter/characterBaseSplitter.py) step-by-step. This script demonstrates how to split simple text files into smaller chunks of a fixed character length using LangChain's `CharacterTextSplitter`.

---

## Code Breakdown

### 1. Importing Libraries
```python
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
```
* **`TextLoader`**: A loader that reads plain text files (`.txt`, `.md`, etc.) and returns them as a LangChain `Document`.
* **`CharacterTextSplitter`**: A basic text splitter that splits text based on a specific character separator (e.g., newline, space, or an empty string) and group sizes.

---

### 2. Loading the Text File
```python
data = TextLoader("text splitter/notes.txt")
docs = data.load()
print(docs)
```
* **What it does**: Initializes the loader with the path to the text file (`text splitter/notes.txt`) and loads the text content.
* **`print(docs)`**: Prints the loaded documents to the console, showing the list containing a single `Document` object with the text content and its source metadata.

---

### 3. Configuring the Character Text Splitter
```python
splitter = CharacterTextSplitter(
    separator="",
    chunk_size=10,
    chunk_overlap=1
)
```
* **`separator=""`**: The character or pattern on which to split the text. By setting it to an empty string `""`, it treats every single character as a potential boundary to satisfy the chunk size constraint.
* **`chunk_size=10`**: Specifies that each chunk should contain a maximum of **10 characters**.
* **`chunk_overlap=1`**: Configures an overlap of **1 character** between consecutive chunks (i.e., the last character of a chunk will be the first character of the next chunk).

---

### 4. Splitting the Document and Printing Results
```python
chunks = splitter.split_documents(docs)
print(len(chunks))
```
* **`split_documents(docs)`**: Processes the loaded document and returns a list of split `Document` chunks.
* **`print(len(chunks))`**: Prints the total count of chunks generated from the input file.

---

### 5. Displaying Content (Commented Out)
```python
# for i in chunks :
#     print(i.page_content)
#     print("\n")
```
* **What it does**: If uncommented, this loop iterates through every generated chunk and prints its exact textual content (`page_content`), followed by empty lines to visually separate the chunks.
