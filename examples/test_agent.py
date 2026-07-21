from src.agent import AgentRequest, ResearchAgent
from src.llm import GeminiClient
from src.planner import Planner
from src.prompts import PromptManager

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

response = agent.run(
    AgentRequest(
        query="Explain CNN and Vision Transformer then compare them."
    )
)

print(response.answer)