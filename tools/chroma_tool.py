from crewai.tools import BaseTool
from pydantic import Field
from typing import Any

class ChromaRetrieverTool(BaseTool):
    name: str = "ChromaRetriever"
    description: str = "Retrieves relevant documents from the Chroma vector store for a given query."
    
    retriever: Any = Field(...)

    def _run(self, query: str) -> str:
        
        try:
            docs = self.retriever.invoke(query)
            return "\n\n".join([doc.page_content for doc in docs])
        except Exception as e:
            return f"[Chroma Retrieval Error] {str(e)}"