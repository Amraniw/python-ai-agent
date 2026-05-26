from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

load_dotenv()

# setting up the LLM

llm = ChatOpenAI(model = "gpt-4.1-mini")
response = llm.invoke("What is the mening of life?")
print(response.content)