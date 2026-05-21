from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter

model = ChatMistralAI(model = "mistral-small-latest")

loader = PyPDFLoader("GRU.pdf")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 200
)

chunks = splitter.split_documents(docs)
# print(len(chunks))
# print(chunks[0].page_content)

prompt  = template.formate_message(data = chunks)

result = model.invoke(prompt)
print(result.content)



