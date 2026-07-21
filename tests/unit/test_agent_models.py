from src.agent.models import AgentRequest, AgentResponse


def test_request():
    request = AgentRequest(
        query="Hello"
    )

    assert request.query == "Hello"


def test_response():
    response = AgentResponse(
        answer="Hi"
    )

    assert response.answer == "Hi"