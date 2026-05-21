# LangChain TextLoader Explanation

Here is a step-by-step breakdown of how the document loader code works:

* **Step 1: Import the Tool (`TextLoader`)**
  ```python
  from langchain_community.document_loaders import TextLoader
  ```
  * **What it does:** Imports LangChain's special tool designed to read text files.

* **Step 2: Point to the File**
  ```python
  data = TextLoader('doc loader/notes.txt')
  ```
  * **What it does:** Tells the tool which file (`notes.txt`) we want to load.

* **Step 3: Read the File (`.load()`)**
  ```python
  docs = data.load()
  ```
  * **What it does:** Reads the file off the disk and converts it into a LangChain "Document".

* **Step 4: Print Everything**
  ```python
  print(docs)
  ```
  * **What it does:** Prints the entire loaded object, which includes both the text and its details (metadata).

* **Step 5: Print Only the Text**
  ```python
  print(docs[0].page_content)
  ```
  * **What it does:** Prints *only* the actual written content of the file, clean and readable.

* **Step 6: Print Only the File Details (Metadata)**
  ```python
  print(docs[0].metadata)
  ```
  * **What it does:** Prints extra information (like the file's path/source: `{'source': 'doc loader/notes.txt'}`).
