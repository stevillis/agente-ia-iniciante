import os

from dotenv import load_dotenv
from langchain.agents import AgentType, initialize_agent
from langchain.memory import ConversationBufferMemory
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


class InicianteAgent:
    def __init__(self):
        if "GEMINI_API_KEY" not in os.environ:
            raise ValueError(
                "A chave API do Google não foi encontrada. Verifique o arquivo .env."
            )

        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0,
            google_api_key=os.environ["GEMINI_API_KEY"],
        )

        self.tools = load_tools(["llm-math", "wikipedia"], llm=self.llm)

        self.memory = ConversationBufferMemory(memory_key="chat_history")

        self.agent_executor = initialize_agent(
            self.tools,
            self.llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True,
            memory=self.memory,
            handle_parsing_errors=True,
        )

    def run(self, query: str):
        return self.agent_executor.invoke({"input": query})
