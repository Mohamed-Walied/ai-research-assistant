from src.llm import BaseLLM, LLMRequest
from src.prompts import PromptManager

from .base import BaseAgent
from .models import AgentRequest, AgentResponse


class ResearchAgent(BaseAgent):
    """
    AI Research Assistant.
    """

    def __init__(
        self,
        llm: BaseLLM,
        prompt_manager: PromptManager,
    ):
        self.llm = llm
        self.prompt_manager = prompt_manager

    def run(
        self,
        request: AgentRequest,
    ) -> AgentResponse:

        prompt = self.prompt_manager.render(
            "answer",
            context="",
            question=request.query,
        )

        llm_response = self.llm.generate(
            LLMRequest(prompt=prompt)
        )

        return AgentResponse(
            answer=llm_response.content
        )