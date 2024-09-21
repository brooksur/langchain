import os
import argparse
import warnings
from langchain.chat_models import ChatOpenAI
from langchain.prompts import MessagesPlaceholder, HumanMessagePromptTemplate, ChatPromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationSummaryMemory, FileChatMessageHistory

# Suppress LangChain deprecation warnings
warnings.filterwarnings("ignore", category=DeprecationWarning, module="langchain")

# Create a chat
chat_llm = ChatOpenAI(
  openai_api_key=os.getenv('OPENAI_API_KEY'),
  model='gpt-3.5-turbo',
  verbose=True
)

# Create a memory
memory = ConversationSummaryMemory(
  # chat_memory=FileChatMessageHistory("messages.json"),
  memory_key='messages',
  return_messages=True,
  llm=chat_llm # This is the LLM that will be used to summarize the conversation
)

# Create a chat prompt template
chat_prompt = ChatPromptTemplate(
  input_variables=['content', 'messages'],
  messages=[
    MessagesPlaceholder(variable_name='messages'),
    HumanMessagePromptTemplate.from_template('{content}')
  ]
)

# Create a chain
chain = LLMChain(
  llm=chat_llm,
  prompt=chat_prompt,
  memory=memory,
  verbose=True
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
    

    
    
    