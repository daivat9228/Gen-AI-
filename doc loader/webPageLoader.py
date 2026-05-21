from dotenv import load_dotenv

load_dotenv()

from langchain_community.document_loaders import WebBaseLoader
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

model = ChatMistralAI(model = "mistral-small-2506")

url = "https://en.wikipedia.org/wiki/Prompt_engineering"
data = WebBaseLoader(url)
docs = data.load()

prompt = ChatPromptTemplate.from_messages([
    ("system", "you're AI that sums the text from web page"),
    ("human", "{data}")
])

prompt = prompt.format_messages(data = docs)
result = model.invoke(prompt)

print(result.content)