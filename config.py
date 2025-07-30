import os
from dotenv import load_dotenv

# Load environment variables from a .env file (if present)
load_dotenv()

# OpenAI or LLM settings
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4")

# MCP server settings
MCP_SERVER_HOST = "localhost"
MCP_SERVER_PORT = 8000
MODEL_ID = "ai_tutor"

# Optional: Vector store settings
VECTOR_DB_PATH = "vector_store/"
USE_VECTOR_DB = True

# Streamlit UI settings
UI_TITLE = "AI Tutor MCP"
STREAMLIT_SERVER_PORT = 8501

# Debug mode
DEBUG = True
