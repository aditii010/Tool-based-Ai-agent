from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun

search_engine = DuckDuckGoSearchRun()

@tool
def search(query: str) -> str:
    """Search the web for information."""
    return search_engine.run(query)
