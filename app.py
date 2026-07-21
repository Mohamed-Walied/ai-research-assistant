from src.agent import AgentRequest, ResearchAgent
from src.llm import GeminiClient
from src.planner import Planner
from src.prompts import PromptManager


def main():

    llm = GeminiClient()

    prompt_manager = PromptManager()

    planner = Planner(
        llm=llm,
        prompt_manager=prompt_manager,
    )

    agent = ResearchAgent(
        llm=llm,
        prompt_manager=prompt_manager,
        planner=planner,
    )

    print("=" * 60)
    print("Research Agent")
    print("=" * 60)
    print("Query:")

    while True:

        query = input("> ")

        if query.lower() == "exit":
            break

        response = agent.run(
            AgentRequest(query=query)
        )

        print("\n")
        print("=" * 60)
        print("Final Answer")
        print("=" * 60)

        print(response.answer)


if __name__ == "__main__":
    main()