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


def create_job_matcher_agent():
    model = "gemini-2.0-flash"
    job_matcher_agent = Agent(
        name="Job_Matcher_Agent",
        model=model,
        description="Agent that matches CVs with job descriptions and provides actionable feedback",
        instruction=get_agent_instruction()
    )
    return job_matcher_agent