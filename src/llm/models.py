from dataclasses import dataclass
from typing import Optional


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