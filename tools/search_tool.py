from langchain_community.tools.tavily_search import TavilySearchResults
from crewai.tools import BaseTool
from pydantic import Field

search = TavilySearchResults()

class SearchTool(BaseTool):
    name: str = "Search"
    description: str = "Useful for search-based queries. Use this to find current information about latest legal trends and news."
    search: TavilySearchResults = Field(default_factory=TavilySearchResults)

    def _run(self, query: str) -> str:
        """Execute the search query and return results"""
        try:
            return self.search.run(query)
        except Exception as e:
            return f"Error performing search: {str(e)}"
        
        
web_search_tool = SearchTool()