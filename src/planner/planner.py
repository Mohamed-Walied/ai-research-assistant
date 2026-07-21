from src.llm import BaseLLM, LLMRequest
from src.prompts import PromptManager

from .models import Plan, Task
from .prompts import PLANNER_TEMPLATE


class Planner:
    """
    Uses the LLM to decompose a user request into smaller tasks.
    """

    def __init__(
        self,
        llm: BaseLLM,
        prompt_manager: PromptManager,
    ):
        self.llm = llm
        self.prompt_manager = prompt_manager

    def create_plan(
        self,
        query: str,
    ) -> Plan:

        prompt = self.prompt_manager.render(
            PLANNER_TEMPLATE,
            query=query,
        )

        response = self.llm.generate(
            LLMRequest(
                prompt=prompt
            )
        )

        tasks = self._parse_response(
            response.content
        )

        return Plan(tasks=tasks)

    def _parse_response(
        self,
        text: str,
    ) -> list[Task]:
        """
        Convert the LLM response into Task objects.
        """

        tasks = []

        for line in text.splitlines():

            line = line.strip()

            if not line:
                continue

            line = line.lstrip(
                "-•1234567890. "
            )

            tasks.append(
                Task(description=line)
            )

        return tasks