from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(
    model = 'text-embedding-3-large',
    dimensions=64
)

texts = [
    "Hello this is Akarsh Vyas",
    "Hello your name is YouTube",
    "And you all are very beautiful"
]

vector = embeddings.embed_documents(texts) 
# embed_documents for document embedding (documents size can be large)

# vector = embeddings.embed_query("Hello this is Daivat Dhimmar")
# embed_query for query embedding

print(vector)