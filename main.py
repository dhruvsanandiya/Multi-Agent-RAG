from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyMuPDFLoader
from tools.chroma_tool import ChromaRetrieverTool
from agents import create_agents
from tasks import get_tasks
from langchain_openai import ChatOpenAI
from config import OPENAI_API_KEY
from openai import OpenAI
from crewai import Crew

client = OpenAI(api_key=OPENAI_API_KEY)


def ingest_documents(pdf_path, persist_dir="./vectorstore/chroma_db"):
    loader = PyMuPDFLoader(pdf_path)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = splitter.split_documents(docs)

    embedding = OpenAIEmbeddings()
    vectorstore = Chroma(persist_directory=persist_dir, embedding_function=embedding)
    vectorstore.add_documents(chunks)
    vectorstore.persist()

    return vectorstore


def main():
    pdf_path = "./data/sample.pdf"
    print("[INFO] Ingesting documents...")
    vectorstore = ingest_documents(pdf_path)

    retriever = vectorstore.as_retriever()

    # Create the tool using retriever
    chroma_tool = ChromaRetrieverTool(retriever=retriever)
    llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.2,
    openai_api_key=OPENAI_API_KEY
    )

    retriever_agent, legal_assistant_agent, evaluation_agent, editor_agent = create_agents(chroma_tool, llm)

    tasks = get_tasks()

    # Dynamically assign agents
    tasks[0].agent = retriever_agent
    tasks[1].agent = legal_assistant_agent
    tasks[2].agent = evaluation_agent
    tasks[3].agent = editor_agent

    # Define the user query
    query = "what are the welfare benefits according to federal law?"
    
    crew = Crew(
        agents=[
            retriever_agent,
            legal_assistant_agent,
            evaluation_agent,
            editor_agent
        ],
        tasks=tasks,
        verbose=True
    )

    print("[INFO] Running CrewAI agents...")
    result = crew.kickoff(inputs={"query": query})
    print("[CrewAI] Final Answer:")
    print(result)

if __name__ == "__main__":
    main()