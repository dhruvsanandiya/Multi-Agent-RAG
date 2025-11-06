# AI Legal Assistant with CrewAI + RAG

Ever wished you had a super-smart paralegal that reads *all* the PDFs and answers your legal questions? **Agentic Paralegal** does just that — powered by AI agents, vector search, and OpenAI's GPT-4o.

---

## 🚀 What It Does

- 🧠 **Reads PDFs** — Ingests and chunks legal documents
- 🔍 **Finds info fast** — Uses Chroma vector store to fetch relevant sections
- 📄 **Writes smart answers** — GPT-4o generates responses from the docs
- ✅ **Checks its work** — Evaluation agent reviews the answer
- ✨ **Cleans it up** — Editor makes it human-friendly

If it can’t find the answer in your docs? It Googles it for you (kinda — via Tavily Search)!

---

## 🛠️ Stack Attack

- [CrewAI](https://docs.crewai.com/) for multi-agent orchestration  
- [LangChain](https://python.langchain.com) for RAG  
- [Chroma](https://www.trychroma.com/) for vector storage  
- [OpenAI GPT-4o](https://openai.com/) to do the thinking  
- Tavily API for web search (optional fallback)

---

## 🧪 How to Run

1. Clone this repo  
2. Install the goodies  
3.	Add your OPENAI_API_KEY in config.py
4.	Drop a legal PDF into ./data
5.	Fire it up

⸻

🗂️ Agents on the Crew
	•	🕵️‍♂️ Retriever Agent — finds the facts
	•	📚 Legal Assistant — writes the answer
	•	👩‍⚖️ Evaluation Agent — quality control
	•	✍️ Editor Agent — final polish

⸻

👩‍💻 Built With Love by Dhruv Sanandiya

Feel free to fork, play, or send a pull request 🛠️
MIT Licensed.
