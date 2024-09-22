import warnings

from langchain.vectorstores.chroma import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from redundant_filter_retriever import RedundantFilterRetriever

print("Starting prompt...")

warnings.filterwarnings("ignore", category=DeprecationWarning, module="langchain")

chat = ChatOpenAI()

embeddings = OpenAIEmbeddings()

chroma = Chroma(
  persist_directory="emb",
  embedding_function=embeddings
)

retriever = RedundantFilterRetriever(
  embeddings=embeddings,
  chroma=chroma
)

chain = RetrievalQA.from_chain_type(
  llm=chat,
  retriever=retriever,
  chain_type="stuff"
)

result = chain.run('What is an interesting fact about the english language?')

print(result)
