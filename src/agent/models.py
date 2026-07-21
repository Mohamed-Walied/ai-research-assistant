from dataclasses import dataclass


@dataclass(slots=True)
class AgentRequest:
    """
    User request.
    """

    query: str


@dataclass(slots=True)
class AgentResponse:
    """
    Final answer returned by the agent.
    """

    answer: str


@dataclass(slots=True)
class TaskResult:
    """
    Result of executing a single task.
    """

    task: str
    answer: str