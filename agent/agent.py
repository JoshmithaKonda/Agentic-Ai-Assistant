from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from langchain_ollama import ChatOllama

from agent.tools import search_web, get_wikipedia, get_arxiv


def create_agent():
    llm = ChatOllama(
        model="llama3",
        temperature=0
    )

    tools = [
        Tool(
            name="Search",
            func=search_web,
            description="Use this for latest information, news, or general queries from the web."
        ),
        Tool(
            name="Wikipedia",
            func=get_wikipedia,
            description="Use this ONLY for definitions, explanations, or general knowledge about a topic."
        ),
        Tool(
            name="Arxiv",
            func=get_arxiv,
            description="Use this STRICTLY for research papers, academic topics, or when the user asks for papers, studies, or research work."
        ),
    ]

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        max_iterations=5,
        early_stopping_method="generate",
        agent_kwargs={
            "system_message": """
You are a research assistant.

IMPORTANT RULES:
- Do NOT explain which tools you used.
- Do NOT describe your process.
- Always give a clean, direct answer.

If the user asks for research papers:
- Return ONLY a list of paper titles with links.
- Do NOT include definitions.

Be concise and finish quickly.
"""
        }
    )

    return agent