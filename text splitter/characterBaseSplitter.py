from langchain_community.document_loaders import TextLoader

from langchain_text_splitters import CharacterTextSplitter

data = TextLoader("text splitter/notes.txt")
docs = data.load()
print(docs)

splitter = CharacterTextSplitter(
    separator="",
    chunk_size=10,
    chunk_overlap=1
)

chunks = splitter.split_documents(docs)
print(len(chunks))

# for i in chunks :
#     print(i.page_content)
#     print("\n")