from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()
class ResearchResponse(BaseModel):
    topic: str
    summary : str
    sources: list[str]
    tools_used: list[str]
# setting up the LLM

llm = ChatOpenAI(model = "gpt-4.1-mini")
paser = PydanticOutputParser(pydantic_object = ResearchResponse)
