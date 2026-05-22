from dotenv import load_dotenv
load_dotenv()

from langchain_community.vectorstores import Chroma
from langchain_mistralai import MistralAIEmbeddings
from langchain_mistralai import ChatMistralAI

from langchain_core.documents import Document

docs = [
    Document(page_content="The company's revenue increased by 20% in the last quarter.", metadata={"source": "reports", "date": "2023-01-01"}),
    Document(page_content="The new product launch was a success, with 10,000 units sold in the first week.", metadata={"source": "product_launch", "date": "2023-02-01"}),
    Document(page_content="The company's stock price reached an all-time high of $100 per share.", metadata={"source": "stocks", "date": "2023-03-01"})
]

embedding_model = MistralAIEmbeddings(model="mistral-embed")

vector_store = Chroma.from_documents(
    documents = docs,
    embedding = embedding_model,
    persist_directory = r'g:\Gen AI\Gen-AI-\vector store\chroma-db'
)

result = vector_store.similarity_search("How much revenue the company made?", k=1)

# for doc in result:
    # print(doc)
    # print("Document ID: ", doc.id)
    # print("Document Content: ", doc.page_content)
    # print("-" * 20)
    # print("Document Metadata: ", doc.metadata)
    # print("-" * 20)

retriever = vector_store.as_retriever(search_kwargs={"k": 1})
results = retriever.invoke("How much revenue the company made?")

for doc in results:
    print(doc.page_content) 