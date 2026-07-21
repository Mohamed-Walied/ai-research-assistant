from google import genai
from google.genai import types

from src.config import settings
from src.llm.base import BaseLLM
from src.llm.models import LLMRequest, LLMResponse


class GeminiClient(BaseLLM):
    """
    Gemini implementation of BaseLLM.
    """

    def __init__(self):
        self.client = genai.Client(api_key=settings.GEMINI_API_KEY)
        self.model = settings.GEMINI_MODEL

    def generate(self, request: LLMRequest) -> LLMResponse:

        temperature = (
            request.temperature
            if request.temperature is not None
            else settings.TEMPERATURE
        )
        max_output_tokens = (
            request.max_output_tokens
            if request.max_output_tokens is not None
            else settings.MAX_OUTPUT_TOKENS
        )

        response = self.client.models.generate_content(
            model=self.model,
            contents=request.prompt,
            config=types.GenerateContentConfig(
                temperature=temperature,
                max_output_tokens=max_output_tokens,
            ),
        )

        return LLMResponse(
            content=response.text or "",
            model=self.model,
        )