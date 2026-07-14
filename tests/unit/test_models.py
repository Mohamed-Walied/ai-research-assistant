from src.llm.models import LLMRequest, LLMResponse


def test_create_request():
    request = LLMRequest(
        prompt="Hello"
    )

    assert request.prompt == "Hello"


def test_create_response():
    response = LLMResponse(
        content="Hi!",
        model="gemini-2.5-flash"
    )

    assert response.content == "Hi!"
    assert response.model == "gemini-2.5-flash"