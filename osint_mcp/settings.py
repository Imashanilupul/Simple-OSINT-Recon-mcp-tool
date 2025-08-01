import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    WIGLE_API_NAME: str = os.getenv("WIGLE_API_NAME")
    WIGLE_API_TOKEN: str = os.getenv("WIGLE_API_TOKEN")
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY")
    
settings = Settings()
