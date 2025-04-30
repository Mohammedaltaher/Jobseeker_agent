# Jobseeker Agent

Jobseeker Agent is a Python-based application designed to assist job seekers in creating professional resumes and CVs. The application leverages templates, tools, and utilities to generate customized PDF documents based on user input.

## Features

- **Resume Builder**: Generate professional resumes using predefined templates.
- **PDF Generation**: Convert user data into a well-formatted PDF document.
- **Customizable Templates**: Use HTML templates to define the structure and style of resumes.
- **Font Support**: Includes a variety of fonts for enhanced document styling.
- **Utilities and Tools**: Additional tools to streamline the resume creation process.

## Project Structure

- `app/`: Contains the core application logic, including agents, models, and utilities.
  - `main.py`: The entry point of the application, defining FastAPI endpoints.
  - `agents/`: Contains agent-related logic.
    - `agent_manager/`: Manages the main job seeker agent.
      - `agent.py`: Defines the `JobSeekerAgentManager` class.
      - `tools.py`: Utility functions for the agent manager.
    - `cv_structure_agent/`: Handles CV structure and formatting.
      - `agent.py`: Logic for CV structure agent.
      - `format.json`: JSON schema for CV structure.
      - `tools.py`: Utility functions for CV structure agent.
    - `job_matcher_agent/`: Matches CVs with job descriptions.
      - `agent.py`: Logic for job matcher agent.
      - `format.json`: JSON schema for job matching.
      - `tools.py`: Utility functions for job matcher agent.
  - `models/`: Defines data models using Pydantic.
    - `models.py`: Contains models like `PersonalInfo`, `ProfessionalExperience`, and `Education`.
  - `pdf_template/`: Handles PDF generation for CVs.
    - `classic.py`, `mono_slate.py`, `slate_lite.py`, `vivid_vision.py`: Different CV templates.

- `data/`: Stores fonts, templates, and other resources.
  - `font/`: Contains font files for PDF generation.
  - `template/`: Includes HTML templates for CVs.

- `static/`: Contains static files such as sample PDFs.

- `tests/`: Includes test cases to ensure the application works as expected.
  - `test_cv_builder.py`: Tests for the main application components.

## Agent Description

The `JobSeekerAgentManager` is a specialized agent designed to transform CV data into a structured JSON format. It ensures:

1. **Input Processing**: Extracts and validates CV data with 100% accuracy.
2. **Structured Transformation**: Formats data according to a predefined JSON schema.
3. **Quality Assurance**: Validates dates, categorizes skills, and ensures proper formatting of URLs, emails, and phone numbers.
4. **Enhancement Suggestions**: Recommends skills to acquire, alternative experiences, and phrasing improvements.

The agent is built using the `google.adk` library and operates asynchronously to process user queries efficiently.

## Getting Started

1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the application using the `main.py` script.

## Requirements

- Python 3.10 or higher
- Dependencies listed in `requirements.txt`

## License

This project is licensed under the MIT License.

## Testing

The project includes a comprehensive test suite to ensure the functionality of its components. The tests are located in the `tests/` directory and can be run using `pytest`.

### Running Tests

1. Install `pytest` if not already installed:
   ```bash
   pip install pytest
   ```

2. Navigate to the project directory:
   ```bash
   cd c:\Users\DMA\source\repos\PythonPtojects\Jobseeker_agent
   ```

3. Run the tests:
   ```bash
   pytest
   ```

4. View the results in the terminal to identify any issues or confirm that all tests pass successfully.