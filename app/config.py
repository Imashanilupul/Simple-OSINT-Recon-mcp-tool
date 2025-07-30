import os
from pydantic_settings import BaseSettings
from pydantic import ConfigDict
from dotenv import load_dotenv

# Load environment variables from a .env file (if present)
load_dotenv()


class Settings(BaseSettings):
    model_config = ConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

    # OpenAI or LLM settings
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY")
    MODEL_NAME: str = os.getenv("MODEL_NAME")

    # Optional: Vector store settings
    VECTOR_DB_PATH: str = "vector_store/"
    USE_VECTOR_DB: bool = True

    # Streamlit UI settings
    STREAMLIT_SERVER_PORT: int = 8501

    # Debug mode
    DEBUG: bool = True


settings = Settings()