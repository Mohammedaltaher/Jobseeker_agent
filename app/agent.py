import uuid
import os
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.memory import InMemoryMemoryService
from google.genai import types

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
            name="CV_Structured_Formatter",
            model=self.model,
            description="Specialized agent that transforms CV analysis into perfectly structured JSON format",
            instruction=self._agent_instruction()
        )

    def _agent_instruction(self) -> str:
        return """
        You are an expert data formatter with one specific task:

        1. Input Processing:
        - Receive analyzed/optimized CV data from cv_job_matcher_agent
        - Extract all relevant information with 100% accuracy

        2. Structured Transformation:
        - Format the data EXACTLY according to the required JSON schema
        - Maintain consistent field names and nesting structure
        - Preserve all original information while adapting to the format

        3. Quality Assurance:
        - Validate all dates follow "MM/YYYY – MM/YYYY" or "MM/YYYY – Present" format
        - Ensure skills are categorized correctly that is matched with the skills in the CV
        - Verify all URLs/emails/phones are properly formatted
        - Check for empty/null values

        4. Enhancement Suggestions:
        - Recommend specific skills to acquire if gaps are found
        - Suggest alternative experiences that could demonstrate required competencies
        - Provide phrasing improvements for stronger impact

        5. Output:
        - Return ONLY the structured JSON
        - No additional commentary or analysis
        - Perfect syntax with proper escaping for special characters
        - If there is any missing data, return "N/A" for that field
        - Fill the section "suggestions" with the following fields:
            - missing_skills: [string]
            - under_emphasized_experiences: [string]
            - phrasing_improvements: [string]
            - additional_suggestions: [string]

        Required JSON Structure:
        {
          "personal_info": {
            "name": string,
            "title": string,
            "location": string,
            "email": string,
            "phone": string,
            "nationality": string
          },
          "profile": string,
          "skills": {
            "category1": [string],
            "category2": [string],
            "category3": [string]
          },
          "professional_experience": [
            {
              "role": string,
              "company": string,
              "duration": string,
              "location": string,
              "tools": string,
              "description": string,
              "achievements": [string],
              "projects": [
                {
                  "name": string,
                  "description": string
                }
              ]
            }
          ],
          "education": [
            {
              "degree": string,
              "institution": string,
              "location": string,
              "year": string
            }
          ],
          "languages": [string],
          "suggestions": {
            "missing_skills": [string],
            "under_emphasized_experiences": [string],
            "phrasing_improvements": [string],
            "additional_suggestions": [string]
          }
        }
        """

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
