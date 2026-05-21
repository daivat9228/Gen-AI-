from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate

model = ChatMistralAI(model = "mistral-small-2506")

data = PyPDFLoader("doc loader/GRU.pdf")
docs = data.load()

template = ChatPromptTemplate.from_messages([
    ("system", "you're an AI that summerizes text"),
    ("human", "{data}")
])

prompt = template.format_messages(data = docs)
# prompt = template.format_messages(data = docs[1].page_content)

result = model.invoke(prompt)

print(result.content)

# print(docs)
# print(len(docs))
# print(docs[0].page_content)
# print(docs[14].page_content)

 