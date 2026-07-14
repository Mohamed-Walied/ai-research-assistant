from abc import ABC, abstractmethod

from .models import LLMRequest, LLMResponse


class BaseLLM(ABC):
    """
    Interface implemented by every LLM provider.
    """

    @abstractmethod
    def generate(self, request: LLMRequest) -> LLMResponse:
        """
        Generate text from an LLM.
        """
        raise NotImplementedError