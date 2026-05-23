from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import MistralAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

embedding_model = MistralAIEmbeddings()

vector_store = Chroma(
    embedding_function=embedding_model,
    persist_directory=r"g:\Gen AI\Gen-AI-\vector store\chroma-db"
)

retriever = vector_store.as_retriever(
    search_kwargs={"k": 4, "fetch_k": 10, "lambda_mult":0.5},
    search_type="mmr"
)

llm = ChatMistralAI(model = "mistral-small-latest")

Prompt = ChatPromptTemplate.from_messages([
    (
            "system",
            """You are a helpful AI assistant.

Use ONLY the provided context to answer the question.

If the answer is not present in the context,
say: "I could not find the answer in the document."
"""
        ),
         (
            "human",
            """Context:
{context}

Question:
{question}
"""
        )
])

print("RAG system created")

print("press 0 to exit")

while True:
    query = input("Ask a question:")
    if query == "0" :
        break 
    docs = retriever.invoke(query)
    context = "\n".join([doc.page_content for doc in docs])
    
    response = llm.invoke(Prompt.format(context=context, question=query))
    print(f"\n AI: {response.content}")