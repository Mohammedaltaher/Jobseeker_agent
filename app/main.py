from fastapi import FastAPI
from app.pdf_generator import generate_pdf
from .models import CVInput, GetCV
from app.utils import Base, Jobseeker, SessionLocal, engine, insert_or_update_jobseeker
from fastapi.encoders import jsonable_encoder
from app import agent
import json
import debugpy


# Create all tables in the database
Base.metadata.create_all(bind=engine)

app = FastAPI()


# Allow debugger to attach on port 5678
# debugpy.listen(("127.0.0.1", 5678))
# print("Waiting for debugger to attach...")
# debugpy.wait_for_client()  # Optional: Pause execution until debugger is attached



@app.post("/generate-cv/")
async def generate_cv(cv_input: CVInput):

    structured_data = cv_input.dict()
    pdf_path = generate_pdf(structured_data)

    db = SessionLocal()
    insert_or_update_jobseeker(
        db,
        cv_input.personal_info.name,
        cv_input.personal_info.email,
        jsonable_encoder(cv_input),
    )
    db.close()

    return {"message": "CV generated", "pdf": pdf_path}

@app.post("/build-cv/")
async def build_cv(cv:str , job_description :str):
    agent_manager = agent.JobSeekerAgentManager()
    response = await agent_manager.call_agent(f"cv : {cv} , job_description : {job_description}")
    cleaned_str = json.loads(response.strip('```json').strip('```').strip())
    pdf_path = generate_pdf( cleaned_str)
    return cleaned_str
