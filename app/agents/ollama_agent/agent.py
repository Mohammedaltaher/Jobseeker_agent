from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLLM
from app.agents.ollama_agent.tools import get_agent_instruction 

ollama_model = LiteLLM(model="ollama_chat/tinyllama") 

root_agent = Agent(
            name="agent_manager",
            model=ollama_model,
            description="The CV Tailoring Agent is an intelligent assistant designed to optimize a candidate’s CV for a specific job description. It automatically analyzes the provided job listing, compares it with the applicant’s current CV (in JSON format), and generates a customized version of the CV that aligns closely with the job requirements.",
            instruction= get_agent_instruction(),
            # sub_agents=[create_cv_structured_formatter_agent(),  create_job_matcher_agent()]
        )