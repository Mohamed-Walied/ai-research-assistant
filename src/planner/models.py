from dataclasses import dataclass


@dataclass(slots=True)
class Task:
    """
    Represents a single task in a research plan.
    """

    description: str


@dataclass(slots=True)
class Plan:
    """
    Represents the full execution plan.
    """

    tasks: list[Task]