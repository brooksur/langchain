import os
import argparse
import warnings
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

# Suppress LangChain deprecation warnings
warnings.filterwarnings("ignore", category=DeprecationWarning, module="langchain")

# Initialize argument parser
parser = argparse.ArgumentParser()

# Add arguments for language and task with default values
parser.add_argument('--language', default='python')
parser.add_argument('--task', default='generate a random number between 0 and 10')

# Parse the command line arguments
args = parser.parse_args()

# Initialize the OpenAI LLM with the API key from environment variable
llm = OpenAI(
  openai_api_key=os.getenv('OPENAI_API_KEY')
)

# Create a prompt template for generating code snippets
code_prompt = PromptTemplate(
  template="Write a very short {language} function that will {task}",
  input_variables=['language', 'task']
)

# Create a chain to generate some code with the LLM
code_chain = LLMChain(
  llm=llm, 
  prompt=code_prompt,
  output_key='code'
)

# Create a prompt template for generating a test for the code
test_prompt = PromptTemplate(
  template="Write a very short {language} test for the code: {code}",
  input_variables=['language', 'code']
)

# Create a chain to generate a test for the code with the LLM
test_chain = LLMChain(
  llm=llm,
  prompt=test_prompt,
  output_key='test'
)

# Create a sequential chain that passes the result of the code chain to the test chain
sequential_chain = SequentialChain(
  chains=[code_chain, test_chain],
  input_variables=['language', 'task'],
  output_variables=['code', 'test']
)

# Generate the result using the chain with provided arguments
result = sequential_chain({'language': args.language, 'task': args.task})
print('>>>> GENERATED CODE <<<\n')
print(result['code'] + '\n')
print('>>>> GENERATED TEST <<<\n')
print(result['test'])

