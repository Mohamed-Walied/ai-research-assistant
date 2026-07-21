from src.llm import BaseLLM, LLMRequest
from src.planner import Planner
from src.prompts import PromptManager

from .base import BaseAgent
from .models import (
    AgentRequest,
    AgentResponse,
    TaskResult,
)


class ResearchAgent(BaseAgent):
    """
    AI Research Agent.

    Workflow:

    User
        ↓
    Planner
        ↓
    Execute Tasks
        ↓
    Combine Results
        ↓
    Final Answer
    """

    def __init__(
        self,
        llm: BaseLLM,
        prompt_manager: PromptManager,
        planner: Planner,
    ):
        self.llm = llm
        self.prompt_manager = prompt_manager
        self.planner = planner

    def run(
        self,
        request: AgentRequest,
    ) -> AgentResponse:

        plan = self.create_plan(request)

        results = self.execute_plan(plan)

        answer = self.combine_results(results)

        return AgentResponse(
            answer=answer
        )

    def create_plan(
        self,
        request: AgentRequest,
    ):

        return self.planner.create_plan(
            request.query
        )

    def execute_plan(
        self,
        plan,
    ) -> list[TaskResult]:

        results = []

        for task in plan.tasks:

            prompt = self.prompt_manager.render(
                "answer",
                context="",
                question=task.description,
            )

            response = self.llm.generate(
                LLMRequest(
                    prompt=prompt
                )
            )

            results.append(
                TaskResult(
                    task=task.description,
                    answer=response.content,
                )
            )

        return results

    def combine_results(
        self,
        results: list[TaskResult],
    ) -> str:

        sections = []

        for result in results:

            sections.append(
                f"## {result.task}\n\n{result.answer}"
            )

        return "\n\n".join(sections)