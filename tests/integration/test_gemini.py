from src.llm import GeminiClient, LLMRequest


def test_generate():
    llm = GeminiClient()

    response = llm.generate(
        LLMRequest(
            prompt="Say hello in one sentence."
        )
    )

    assert isinstance(response.content, str)
    assert len(response.content) > 0