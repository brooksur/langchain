import os
import argparse
import warnings
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Suppress LangChain deprecation warnings
warnings.filterwarnings("ignore", category=DeprecationWarning, module="langchain")

parser = argparse.ArgumentParser()

parser.add_argument('--language', default='python')
parser.add_argument('--task', default='generate a random number between 0 and 10')

args = parser.parse_args()

llm = OpenAI(
  openai_api_key=os.getenv('OPENAI_API_KEY')
)

prompt = PromptTemplate(
  template="Write a very short {language} function that will {task}",
  input_variables=['language', 'task']
)

chain = LLMChain(llm=llm, prompt=prompt)

result = chain({'language': args.language, 'task': args.task})
result_text = result['text']

print(result_text)