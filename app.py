import os

from dotenv import load_dotenv
from langchain.agents import AgentType, initialize_agent
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_google_genai import ChatGoogleGenerativeAI

if __name__ == "__main__":
    load_dotenv()

    if "GEMINI_API_KEY" not in os.environ:
        raise ValueError(
            "A chave API do Google não foi encontrada. Verifique o arquivo .env."
        )

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0,
        google_api_key=os.environ["GEMINI_API_KEY"],
    )

    tools = load_tools(["llm-math", "wikipedia"], llm=llm)

    agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    question = input("\n📝 Sua pergunta: ")
    answer = agent.run(question)

    print(f"\n🤖 Resposta: {answer}")
