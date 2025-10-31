# agents.py

from crewai import Agent
from tools.search_tool import web_search_tool

def create_agents(chroma_tool, llm):
    retriever_agent = Agent(
        role='Retriever Agent',
        goal='Retrieve relevant content about "{query}" from the vector store.',
        backstory=("You are skilled at searching the vector store for user queries and fetching relevant documents. "
                   "Your ability to find and retrieve relevant content ensures accurate reports."),
        verbose=True,
        memory=True,
        tools=[chroma_tool],
        llm=llm
    )

    legal_assistant_agent = Agent(
        role="Legal Assistant Agent",
        goal="Generate responses for the {query} based on retrieved documents only",
        backstory="You are a lawyer assistant. You create informative responses using the retriever's results. "
                  "If those aren't enough, you may consult the web search tool.",
        verbose=True,
        memory=True,
        allow_delegation=False,
        tools=[web_search_tool],
        llm=llm
    )

    evaluation_agent = Agent(
        role="Evaluation Expert Agent",
        goal="Verify and evaluate the accuracy and authenticity of responses created by retriever and generator agents.",
        backstory="You are a legal evaluation expert ensuring high-quality, factual output.",
        verbose=True,
        memory=False,
        allow_delegation=False,
        tools=[web_search_tool],
        llm=llm
    )

    editor_agent = Agent(
        role="Editor Agent",
        goal="Create a concise and edited output for '{query}' based on the generated response.",
        backstory="You are an editor responsible for polishing the final output, ensuring clarity and format correctness.",
        verbose=True,
        memory=False,
        llm=llm
    )

    return retriever_agent, legal_assistant_agent, evaluation_agent, editor_agent