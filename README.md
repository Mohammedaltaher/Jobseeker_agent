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
- `data/`: Stores fonts, templates, and other resources.
- `static/`: Contains static files such as sample PDFs.
- `tests/`: Includes test cases to ensure the application works as expected.

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