import os
import argparse
import warnings
from langchain.chat_models import ChatOpenAI
from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate
from langchain.chains import LLMChain, SequentialChain

# Suppress LangChain deprecation warnings
warnings.filterwarnings("ignore", category=DeprecationWarning, module="langchain")

# Create a chat
chat_llm = ChatOpenAI(
  openai_api_key=os.getenv('OPENAI_API_KEY'),
  model='gpt-3.5-turbo'
)

# Create a chat prompt template
chat_prompt = ChatPromptTemplate(
  input_variables=['content'],
  messages=[
    HumanMessagePromptTemplate.from_template('{content}')
  ]
)

# Create a chain
chain = LLMChain(
  llm=chat_llm,
  prompt=chat_prompt
)

while True:
  # Get user input
  content = input('>> ')
  
  # Check if the user wants to exit
  if content == 'exit':
    break
  
  # Get the response from the chain
  response = chain.invoke({'content': content})
  
  # Print the response
  print(response['text'])