from os import getenv
import uuid
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.memory import InMemoryMemoryService
from google.genai import types
from .tools import get_agent_instruction

# Load environment variables
load_dotenv('.env')


def create_cv_structured_formatter_agent():
    cv_structured_formatter_agent = Agent(
            name="CV_Structured_Formatter_Agent",
            model=getenv("MODEL_GEMINI_2_0_FLASH"),
            description="Agent that formats CVs into structured JSON",
            instruction=get_agent_instruction()
        )
    return cv_structured_formatter_agent