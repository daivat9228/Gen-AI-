from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1.  Prompt Template
prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple words"
)

# 2. Models
model = ChatMistralAI(model = "mistral-small-latest")

# 3. Output parser
parser = StrOutputParser()

# step-by-step manual flow

# # Formate the prompt
# formatted_prompt = prompt.format_messages(topic = "Machine learning") 

# # Call the model manually
# response = model.invoke(formatted_prompt)

# # Parse the output manually
# final_output = parser.parse(response.content)

# print(final_output)

chain = prompt | model | parser

result = chain.invoke("Machine learning")
print(result)