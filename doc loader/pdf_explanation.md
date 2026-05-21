# LangChain PDF Summarizer Explanation

Here is a step-by-step breakdown of how the PDF loading and summarization code works:

---

### **1. Loading Environment Variables**
```python
from dotenv import load_dotenv

load_dotenv()
```
* **What it does:** Looks for a `.env` file in your project folder and loads your API keys (like `MISTRAL_API_KEY`) into the environment so they can be securely used by your code.

---

### **2. Importing the Libraries**
```python
from langchain_mistralai import ChatMistralAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate
```
* **`ChatMistralAI`**: The integration tool that allows us to connect and send messages to Mistral's AI models.
* **`PyPDFLoader`**: The specialized loader class that knows how to read and extract text from PDF files.
* **`ChatPromptTemplate`**: A template system that helps structure how we format system instructions and user input before sending them to the AI.

---

### **3. Setting Up the AI Model**
```python
model = ChatMistralAI(model = "mistral-small-2506")
```
* **What it does:** Configures the Mistral AI model we want to use (in this case, `mistral-small-2506`).

---

### **4. Loading the PDF File**
```python
data = PyPDFLoader("doc loader/GRU.pdf")
docs = data.load()
```
* **`PyPDFLoader(...)`**: Points to the PDF file on your computer.
* **`data.load()`**: Reads the PDF and converts it into a list of LangChain `Document` objects (where each page in the PDF becomes one `Document` in the list).

---

### **5. Designing the Prompt Template**
```python
template = ChatPromptTemplate.from_messages([
    ("system", "you're an AI that summerizes text"),
    ("human", "{data}")
])
```
* **`system`**: Tells the AI how to behave (e.g., *"you are an AI that summarizes text"*).
* **`human`**: Holds a placeholder `{data}` where we will insert our loaded PDF text.

---

### **6. Formatting the Prompt**
```python
prompt = template.format_messages(data = docs)
```
* **What it does:** Replaces the `{data}` placeholder inside the template with your loaded PDF documents (`docs`) and converts the template into structured messages that the AI model can understand.

---

### **7. Asking the AI and Printing the Result**
```python
result = model.invoke(prompt)

print(result.content)
```
* **`model.invoke(...)`**: Sends the prompt containing the system instruction and PDF pages to Mistral AI.
* **`result.content`**: Extracts and prints only the textual summary response returned by the AI.
