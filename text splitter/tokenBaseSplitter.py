from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import TokenTextSplitter


data = PyPDFLoader("text splitter/GRU.pdf")
docs = data.load()
# print(docs)

splitter = TokenTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 100
)

chunks = splitter.split_documents(docs)
# print(len(chunks))
print(chunks[0].page_content)   