from src.llm import BaseLLM, LLMRequest
from src.planner import Planner
from src.planner import Plan
from src.prompts import PromptManager
from src.core import get_logger

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
        self.logger = get_logger(__name__)

    def run(
        self,
        request: AgentRequest,
    ) -> AgentResponse:

        self.logger.info("Planning...")

        plan = self.create_plan(request)
        self.logger.info("Generated %s tasks", len(plan.tasks))

        results = self.execute_plan(plan)

        answer = self.combine_results(results)

        self.logger.info("Finished.")

        return AgentResponse(
            answer=answer
        )

    def create_plan(
        self,
        request: AgentRequest,
    ) -> Plan:

        return self.planner.create_plan(
            request.query
        )

    def execute_plan(
        self,
        plan: Plan,
    ) -> list[TaskResult]:

        results = []

        for task in plan.tasks:

            self.logger.info("Executing Task %s...", len(results) + 1)

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