from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from pprint import pprint
import json

from tools import search

# Load environment variables
load_dotenv()

class ResearchResponse(BaseModel):
    topic: str = Field(description="Main topic of the question")
    response: str = Field(description="Clear factual answer")
    sources: list[str] = Field(description="Sources used to answer")
    tools_used: list[str] = Field(description="Tools used during reasoning")

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.3
)

# Bind tools to model
llm_with_tools = llm.bind_tools([search])

# Enforce structured output
structured_llm = llm_with_tools.with_structured_output(ResearchResponse)

prompt = ChatPromptTemplate.from_messages([
    ("system",
     """
You are a research assistant.

Rules:
- Always return valid JSON.
- Do NOT wrap lists as strings.
- Fill all fields: topic, response, sources, tools_used.
- Use tools when helpful.
     """
    ),
    ("human", "{query}")
])

chain = prompt | structured_llm

result = chain.invoke({"query": "Who was Miss World 2005?"})

print("\n--- Structured Output ---")
pprint(result.model_dump())
print("\n--- JSON Output ---")
print(json.dumps(result.model_dump(), indent=2))
