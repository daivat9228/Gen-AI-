from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import ChatPromptTemplate

model = ChatMistralAI(model = "mistral-small-2506")

data = TextLoader("doc loader/notes.txt")
docs = data.load()

template = ChatPromptTemplate.from_messages([
    ("system", "you're an AI that summerize the text"),
    ("human", "{data}")
])

prompt = template.format_messages(data = docs[0].page_content)

result = model.invoke(prompt)


# result = model.invoke("what is your name?") 

print(result.content)



























# from langchain_core.prompts import PromptTemplate

# template = PromptTemplate(input_variables = ['name'], template = "Hello {name}, how are you?")

# prompt = template.format(name = "John")

# result = model.invoke(prompt)

# print(result.content)