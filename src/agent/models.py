from dataclasses import dataclass


@dataclass(slots=True)
class AgentRequest:
    """
    Input to the agent.
    """

    query: str


@dataclass(slots=True)
class AgentResponse:
    """
    Output from the agent.
    """

    answer: str