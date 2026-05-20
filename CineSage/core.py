from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

model = ChatMistralAI(model = "mistral-small-2506",temperature=0.9)

prompt = ChatPromptTemplate.from_messages()

response = model.invoke("hello")

print(response.content)















# from langchain_core.messages import AIMessage , SystemMessage , HumanMessage


# model = ChatMistralAI(model = "mistral-small-2506",temperature=0.9)

# messages = [
#     SystemMessage(content="You are a movie recommendation agent.")
# ]

# while True:
#     prompt = input("You : ")
#     messages.append(HumanMessage(content=prompt))
#     response = model.invoke(messages)
#     messages.append(AIMessage(content=response.content))
#     print("Bot :",response.content)

    






























# from langchain_core.messages import AIMessage , SystemMessage , HumanMessage


# model = ChatMistralAI(model = "mistral-small-2506",temperature=0.9)

# messages = [
#     SystemMessage(content="You are a movie recommendation agent.")
# ]

# while True:
#     prompt = input("You : ")
#     messages.append(HumanMessage(content=prompt))
#     response = model.invoke(messages)
#     messages.append(AIMessage(content=response.content))
#     print("Bot :",response.content)

    