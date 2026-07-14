from src.config import settings


def test_gemini_model_exists():
    assert settings.GEMINI_MODEL is not None


def test_temperature_range():
    assert 0.0 <= settings.TEMPERATURE <= 2.0


def test_max_tokens_positive():
    assert settings.MAX_OUTPUT_TOKENS > 0


def test_log_level_exists():
    assert settings.LOG_LEVEL in [
        "DEBUG",
        "INFO",
        "WARNING",
        "ERROR",
        "CRITICAL",
    ]