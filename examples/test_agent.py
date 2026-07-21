from src.agent import AgentRequest, ResearchAgent
from src.llm import GeminiClient
from src.prompts import PromptManager


def main():
    llm = GeminiClient()

    prompts = PromptManager()

    agent = ResearchAgent(
        llm=llm,
        prompt_manager=prompts,
    )

    response = agent.run(
        AgentRequest(
            query="Explain Retrieval-Augmented Generation."
        )
    )

    print(response.answer)


if __name__ == "__main__":
    main()