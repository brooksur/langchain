import warnings
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.chroma import Chroma

# Suppress LangChain deprecation warnings
warnings.filterwarnings("ignore", category=DeprecationWarning, module="langchain")

# Create embeddings
embeddings = OpenAIEmbeddings()

# Create loader for the facts text file
loader = TextLoader("facts.txt")

# Create text splitter
splitter = CharacterTextSplitter(
  separator="\n", 
  chunk_size=200, 
  chunk_overlap=0
)

# Split the text data into chunks
docs = loader.load_and_split(
  text_splitter=splitter
)

# Create chroma vector store
vector_store = Chroma.from_documents(
  docs,
  embedding=embeddings,
  persist_directory="emb"
)

results = vector_store.similarity_search_with_score('What is an interesting fact about the english language?')

for result in results:
  print("---")
  print(result[1])
  print(result[0].page_content)
  print("---")
