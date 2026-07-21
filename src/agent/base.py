from abc import ABC, abstractmethod

from .models import AgentRequest, AgentResponse


class BaseAgent(ABC):
    """
    Base class for all agents.
    """

    @abstractmethod
    def run(
        self,
        request: AgentRequest,
    ) -> AgentResponse:
        """
        Execute the agent.
        """
        raise NotImplementedError