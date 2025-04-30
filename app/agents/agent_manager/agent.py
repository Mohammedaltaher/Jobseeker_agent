import uuid
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.memory import InMemoryMemoryService
from google.genai import types

from app.agents.cv_structure_agent.agent import create_cv_structured_formatter_agent
from app.agents.job_matcher_agent.agent import create_job_matcher_agent
from .tools import get_agent_instruction
from app.agents.job_matcher_agent.tools import get_agent_instruction as get_job_matcher_instruction
# Load environment variables
load_dotenv('.env')


class JobSeekerAgentManager:
    def __init__(
        self,
        user_id: str = "user_1234",
        app_name: str = "jobseeker_agent",
        agent_name: str = "jobseeker_manager_agent",
        model: str = "gemini-2.0-flash"
    ):
        self.user_id = user_id
        self.app_name = app_name
        self.agent_name = agent_name
        self.session_id = f"session_{uuid.uuid4()}"
        self.model = model

        # Session & Memory services
        self.session_service = InMemorySessionService()
        self.memory_service = InMemoryMemoryService()
        self.session = self._create_session()

        # Agent setup
        self.agent = self._create_agent()

        # Runner setup
        self.runner = Runner(
            agent=self.agent,
            app_name=self.app_name,
            session_service=self.session_service,
            memory_service=self.memory_service
        )

    def _create_session(self):
        return self.session_service.create_session(
            app_name=self.app_name,
            user_id=self.user_id,
            session_id=self.session_id,
            state={"initial_key": "initial_value"}
        )

    def _create_agent(self):
        return Agent(
            name="agent_manager",
            model=self.model,
            description="An intelligent agent manager that orchestrates interactions between the CV formatter and job matcher agents, ensuring seamless processing and actionable insights.",
            instruction= get_agent_instruction(),
            sub_agents=[create_cv_structured_formatter_agent(),  create_job_matcher_agent()]
        )

    async def call_agent(self, query: str) -> str:
        content = types.Content(role='user', parts=[types.Part(text=query)])
        print(f"\n--- Running Query: {query} ---")
        final_response_text = "No final text response captured."

        try:
            async for event in self.runner.run_async(
                user_id=self.user_id,
                session_id=self.session_id,
                new_message=content
            ):
                if event.content and event.content.parts:
                    for part in event.content.parts:
                        if part.text and not part.text.isspace():
                            print(f"***Text: '{part.text.strip()}'")

                if event.is_final_response():
                    final_response_text = event.content.parts[0].text
                    return final_response_text

        except Exception as e:
            print(f"Error during agent interaction: {e}")
            return f"Error during agent interaction: {e}"
