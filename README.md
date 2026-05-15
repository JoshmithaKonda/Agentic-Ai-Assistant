# 🤖 Agentic AI Research Assistant

An intelligent **Agentic AI system** that dynamically selects tools to answer user queries, combining LLM reasoning with real-time data sources.

🔗 Built for practical AI applications like research assistance, knowledge retrieval, and smart search systems.

---

## ✨ Key Features

- 🧠 **Agent-Based Reasoning** using LangChain  
- 🔀 **Dynamic Tool Routing** based on query intent  
- 🔎 **Web Search** (DuckDuckGo) for real-time data  
- 📘 **Wikipedia Integration** for factual knowledge  
- 📄 **arXiv Integration** for research papers  
- 💬 **Interactive Chat UI** built with Streamlit  
- ⚡ **Runs Locally with Ollama (Llama3)** — no API cost  

---

## 🧩 System Architecture

User Query
↓
LLM (Agent)
↓
Router
↙ ↓ ↘
Search Wiki arXiv
↓ ↓ ↓
→ Final Response →


---

## 🧠 How It Works

1. User enters a query in the chat interface  
2. The **LLM Agent** analyzes intent  
3. The **Router** selects the most relevant tool:
   - 🌐 General queries → Web Search  
   - 📘 Definitions → Wikipedia  
   - 📄 Research queries → arXiv  
4. Tool outputs are processed and returned as a clean response  

---

## 🛠️ Tech Stack

| Layer        | Technology |
|-------------|-----------|
| Frontend     | Streamlit |
| LLM          | Ollama (Llama3) |
| Framework    | LangChain |
| Tools/APIs   | DuckDuckGo, Wikipedia, arXiv |
| Language     | Python |

---

## ▶️ Run Locally

```bash
# Clone repo
git clone https://github.com/your-username/agentic-ai-assistant.git

cd agentic-ai-assistant

# Activate virtual environment
source venv/bin/activate

# Run Ollama model
ollama run llama3

# Start app
streamlit run app.py<img width="1470" height="956" alt="Screenshot 2026-05-15 at 20 52 54" src="https://github.com/user-attachments/assets/3b919ff8-f2ee-4152-b61c-df4450e5607c" />

⚡ Challenges Solved
Designing tool-based reasoning with LLMs
Handling API rate limits and fallbacks
Managing Streamlit UI state & reruns
Integrating multiple data sources into a single pipeline
🚀 Future Improvements
🌐 Deploy using OpenAI APIs
🧠 Add conversation memory
🎤 Voice-based queries
📊 Better UI/UX with advanced components
👩‍💻 Author
Joshmitha
