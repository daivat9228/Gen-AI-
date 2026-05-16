#init chat model
from dotenv import load_dotenv

load_dotenv()

from langchain.chat_models import init_chat_model
model = init_chat_model("google_genai:gemini-2.5-flash-lite")

response = model.invoke("Hello, how are you?")
print(response.content)




#model  class
# another way to invoke the model using Langchain Google Generative AI
"""
from dotenv import load_dotenv

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash-lite",temperature=0.9)

response = model.invoke("write a poem on AI")
print(response.content)
"""



"""
from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(model = "mistral-small-2506",temperature=0.9)

response = model.invoke("write a poem on AI")

print(response.content)
"""

"""
from dotenv import load_dotenv

load_dotenv()

from langchain_anthropic import ChatAnthropic

model = ChatAnthropic(model = "claude-haiku-4-5",temperature=0.9)

response = model.invoke("write a poem on AI")

print(response.content)
"""

"""
from dotenv import load_dotenv

load_dotenv()
from langchain_openai import ChatOpenAI
model = ChatOpenAI(model = "gpt-3.5-turbo",temperature=0.9)

response = model.invoke("write a poem on AI")

print(response.content)
"""

