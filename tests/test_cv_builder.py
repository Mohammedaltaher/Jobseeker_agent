import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.agents.job_matcher_agent.agent import create_job_matcher_agent
from app.pdf_template.vivid_vision import generate_cv
from app.agents.agent_manager.agent import JobSeekerAgentManager
from app.models.models import PersonalInfo, ProfessionalExperience, Education

client = TestClient(app)

# Test for FastAPI endpoints
def test_build_cv():
    response = client.post(
        "/build-cv/",
        json={
            "cv": "Sample CV data",
            "job_description": "Sample job description",
            "template": "vivid_vision"
        }
    )
    assert response.status_code == 422
    # Add more assertions based on the expected response

def test_download_cv():
    response = client.get("/download-cv/", params={"pdf_path": "static/John Doe_vivid_vision_cv.pdf"})
    assert response.status_code == 200
    # Add more assertions based on the expected response

# Test for create_job_matcher_agent
def test_create_job_matcher_agent():
    agent = create_job_matcher_agent()
    assert agent.name == "Job_Matcher_Agent"
    assert agent.model == "gemini-2.0-flash"

# Test for generate_cv
def test_generate_cv():
    sample_data = {
        "personal_info": {"name": "John Doe", "email": "john.doe@example.com"},
        "professional_experience": [
            {"role": "Developer", "company": "Tech Co", "duration": "2 years"}
        ]
    }
    pdf_path = generate_cv(sample_data)
    assert isinstance(pdf_path, str)

# Test for JobSeekerAgentManager
def test_job_seeker_agent_manager():
    manager = JobSeekerAgentManager()
    assert manager.agent_name == "jobseeker_manager_agent"
    assert manager.model == "gemini-2.0-flash"

# Test for Pydantic models
def test_personal_info_model():
    personal_info = PersonalInfo(name="John Doe", email="john.doe@example.com")
    assert personal_info.name == "John Doe"
    assert personal_info.email == "john.doe@example.com"

def test_professional_experience_model():
    experience = ProfessionalExperience(role="Developer", company="Tech Co")
    assert experience.role == "Developer"
    assert experience.company == "Tech Co"

def test_education_model():
    education = Education(degree="BSc Computer Science", institution="University X")
    assert education.degree == "BSc Computer Science"
    assert education.institution == "University X"