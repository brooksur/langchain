import warnings
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

# Suppress LangChain deprecation warnings
warnings.filterwarnings("ignore", category=DeprecationWarning, module="langchain")

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


