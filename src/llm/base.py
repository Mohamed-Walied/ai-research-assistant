from abc import ABC, abstractmethod

from .models import LLMResponse


class BaseLLM(ABC):
    """
    Abstract interface for all LLM providers.
    """

    @abstractmethod
    def generate(self, prompt: str) -> LLMResponse:
        """
        Generate a response from the model.
        """
        pass