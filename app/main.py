import logging

# Configure logging to filter logs and show only errors
logging.basicConfig(
    level=logging.ERROR,  # Set the logging level to ERROR
    format="%(asctime)s - %(levelname)s - %(message)s",  # Customize the log format
    datefmt="%Y-%m-%d %H:%M:%S",  # Set the date format
)

logging.getLogger("fastapi").setLevel(logging.CRITICAL)
logging.getLogger("starlette").setLevel(logging.CRITICAL)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
from app.agents.agent_manager import agent
from app.pdf_template  import classic , vivid_vision , mono_slate , slate_lite 
from fastapi.responses import FileResponse
from datetime import datetime


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Replace with your Angular app's URL
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)
@app.post("/build-cv/")
async def build_cv(cv: str, job_description: str, template: str):
    """
    Endpoint to build a CV based on user-provided details and a selected template.

    Args:
        cv (str): The user's CV content in plain text format.
        job_description (str): The job description to tailor the CV towards.
        template (str): The name of the template to use for generating the CV.
        
        'vivid_vision', 'mono_slate', 'slate_lite', 'classic'

    Returns:
        dict: A JSON response containing the result and the path to the generated PDF.
    """
    agent_manager = agent.JobSeekerAgentManager()
    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = await agent_manager.call_agent(f"cv : {cv} , job_description : {job_description}")
            break
        except Exception as e:
            error_message = str(e)
            if "503" in error_message and attempt < max_retries - 1:
                print(f"Attempt {attempt + 1} failed: {error_message}. Retrying...")
                continue
            else:
                return {"error": "Failed to process the request. Please try again later."}
            
    cleaned_str = json.loads(response.strip('```json').strip('```').strip())
    
    # Select the appropriate template based on user input
    if template == "vivid_vision":
        pdf_path = vivid_vision.generate_cv(cleaned_str)
    elif template == "mono_slate":
        pdf_path = mono_slate.generate_cv(cleaned_str)
    elif template == "slate_lite":
        pdf_path = slate_lite.generate_cv(cleaned_str)
    elif template == "classic":
        pdf_path = classic.generate_cv(cleaned_str)
    else:
        return {"error": "Invalid template name provided."}
    
    return {"result": "success", "pdf_path": pdf_path, "textResult": cleaned_str}


@app.get("/download-cv/")
async def download_cv(pdf_path: str):
    """
    Endpoint to download the generated CV PDF.

    Args:
        pdf_path (str): The path to the generated PDF file.

    Returns:
        FileResponse: The generated PDF file for download.
    """
    # File name should be the applicant name and the current date
    
    #take the filename from path 
    filename = pdf_path.split('/')[-1]
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    fullname = f"{filename}_{current_time}_cv.pdf"
    
    return FileResponse(pdf_path, media_type="application/pdf", filename=fullname)
