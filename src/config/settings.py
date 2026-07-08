from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    """

    GEMINI_API_KEY: str

    GEMINI_MODEL: str = "gemini-2.5-pro"

    TEMPERATURE: float = 0.2

    MAX_OUTPUT_TOKENS: int = 2048

    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()