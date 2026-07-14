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

        response = self.client.models.generate_content(
            model=self.model,
            contents=request.prompt,
            config=types.GenerateContentConfig(
                temperature=request.temperature
                or settings.TEMPERATURE,
                max_output_tokens=request.max_output_tokens
                or settings.MAX_OUTPUT_TOKENS,
            ),
        )

        return LLMResponse(
            content=response.text,
            model=self.model,
        )