class LLMError(Exception):
    """Base exception for all LLM-related errors."""


class AuthenticationError(LLMError):
    """Raised when authentication fails."""


class RateLimitError(LLMError):
    """Raised when the API rate limit is exceeded."""


class GenerationError(LLMError):
    """Raised when text generation fails."""