from langchain_community.document_loaders import TextLoader

data = TextLoader('doc loader/notes.txt')
docs = data.load()
print(docs)
print(docs[0].page_content)