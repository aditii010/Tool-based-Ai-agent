AI Research Agent (LangChain + Groq)

This project demonstrates how to build a modern AI agent using LangChain that can reason, use tools, and return structured outputs instead of unstructured text.
Unlike basic chatbots, this agent:
Decides when to use tools
Produces validated, structured responses
Avoids hallucinations using schema enforcement

✨ Features

Tool-aware reasoning (web search support)
Structured outputs using Pydantic
Modern LangChain architecture (LCEL)
Clean, extensible design
Production-friendly setup

🧱 Tech Stack

Python 3.10+
LangChain (v1.x)
Groq (LLM backend)
Pydantic
DuckDuckGo Search Tool

📁 Project Structure
AI_agent01/
│
├── main.py        # Main agent logic
├── tools.py       # Tool definitions
├── .env           # API keys (not committed)
└── README.md

⚙️ Setup Instructions
Install dependencies
pip install langchain langchain-groq langchain-community python-dotenv

Create .env file
GROQ_API_KEY=your_api_key_here

How It Works
1. Define a schema for output
class ResearchResponse(BaseModel):
    topic: str
    response: str
    sources: list[str]
    tools_used: list[str]


This guarantees clean, predictable outputs.

2. Define tools
@tool
def search(query: str) -> str:
    ...


The model can now decide when to search the web.

3. Build the agent pipeline
prompt → model → tools → structured output


This replaces older agent APIs and ensures reliability.

Run the Agent
python main.py


Example output:

{
  "topic": "Miss World 2005",
  "response": "Unnur Birna Vilhjálmsdóttir won Miss World 2005.",
  "sources": ["Wikipedia"],
  "tools_used": ["search"]
}

Key Takeaways

Agents are more than prompts — they are structured systems

Tools + schemas = reliable AI

LangChain’s new architecture is composable and clean
