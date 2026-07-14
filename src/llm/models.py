from dataclasses import dataclass
from typing import Optional


@dataclass(slots=True)
class LLMRequest:
    """
    Standard request sent to any LLM provider.
    """

    prompt: str
    temperature: Optional[float] = None
    max_output_tokens: Optional[int] = None


@dataclass(slots=True)
class LLMResponse:
    """
    Standard response returned by every LLM provider.
    """

    content: str
    model: str
    finish_reason: Optional[str] = None
    input_tokens: Optional[int] = None
    output_tokens: Optional[int] = None