import os
from langchain.llms import OpenAI

llm = OpenAI(
  openai_api_key=os.getenv('OPENAI_API_KEY')
)

result = llm('Where a very very short poem')
print(result)