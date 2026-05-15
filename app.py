import streamlit as st
from dotenv import load_dotenv
from langchain_ollama import ChatOllama

from agent.agent import create_agent

load_dotenv()

st.set_page_config(page_title="Agentic AI Assistant", layout="wide")

# 🧠 Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

if "is_generating" not in st.session_state:
    st.session_state.is_generating = False

# 🧠 Sidebar
st.sidebar.title("🤖 Agentic AI Assistant")
st.sidebar.markdown("""
**Features:**
- 🔎 Web Search  
- 📘 Wikipedia  
- 📄 arXiv Papers  
- 🧠 Agent Reasoning  
""")

# 🔄 Clear Chat
if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.messages = []

# 🌙 DARK THEME (ONLY)
st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
        color: white;
    }

    .stChatMessage {
        background-color: #1E1E1E;
        padding: 12px;
        border-radius: 12px;
        margin-bottom: 10px;
    }

    section[data-testid="stChatInput"] {
        background-color: #0E1117 !important;
        border-top: 1px solid #333;
    }

    textarea {
        background-color: #1E1E1E !important;
        color: white !important;
    }

    textarea::placeholder {
        color: #888 !important;
    }

    button svg {
        fill: white !important;
    }

    button {
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# 🧠 Title
st.title("🤖 Agentic AI Research Assistant")
st.caption("AI agent using tools to answer intelligently")

# 📜 Chat History
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 📝 Input
query = st.chat_input("Ask something...")

if query:
    if query.strip() == "":
        st.warning("Please enter a valid query.")
    else:
        # User message
        st.session_state.messages.append({"role": "user", "content": query})
        with st.chat_message("user"):
            st.markdown(query)

        # Assistant response
        with st.chat_message("assistant"):
            st.session_state.is_generating = True

            try:
                with st.spinner("🔍 Thinking..."):
                    agent = create_agent()
                    raw_response = agent.run(query)

                    llm = ChatOllama(
                        model="llama3",
                        temperature=0
                    )

                    final_prompt = f"""
User query: {query}

Agent output: {raw_response}

Generate a clean structured answer:

RULES:
- Do NOT mention tools
- Do NOT explain process
- Use bullet points
- Keep it neat

If research papers:
→ return list with links
"""

                    final_answer = llm.invoke(final_prompt)
                    text = final_answer.content

                    # 🎯 Format output
                    lines = text.split("\n")
                    formatted = ""
                    for line in lines:
                        if line.strip():
                            formatted += f"- {line.strip()}\n"

                    st.markdown(formatted)

                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": formatted
                    })

            except Exception:
                st.error("⚠️ Error: Make sure Ollama is running (`ollama run llama3`)")

            finally:
                st.session_state.is_generating = False