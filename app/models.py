from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy import Column, Integer, String


class PersonalInfo(BaseModel):
    name: Optional[str] = None
    title: Optional[str] = None
    location: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    nationality: Optional[str] = None


class Project(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


class ProfessionalExperience(BaseModel):
    role: Optional[str] = None
    company: Optional[str] = None
    duration: Optional[str] = None
    location: Optional[str] = None
    tools: Optional[str] = None
    description: Optional[str] = None
    achievements: Optional[List[str]] = None
    projects: Optional[List[Project]] = None


class Education(BaseModel):
    degree: Optional[str] = None
    institution: Optional[str] = None
    location: Optional[str] = None
    year: Optional[str] = 'N/A'


class Skills(BaseModel):
    frontend: Optional[List[str]] = None
    backend: Optional[List[str]] = None
    database: Optional[List[str]] = None
    teaching: Optional[List[str]] = None
    others: Optional[List[str]] = None


class CVInput(BaseModel):
    personal_info: Optional[PersonalInfo] = None
    profile: Optional[str] = None
    skills: Optional[Skills] = None
    professional_experience: Optional[List[ProfessionalExperience]] = None
    education: Optional[List[Education]] = None
    languages: Optional[List[str]] = None


class GetCV(BaseModel):
    cv: Optional[str] = None
    job_description: Optional[str] = None


# Example usage with Mohamed Eltaher's data
# mohamed_cv = CVInput(
#     personal_info=PersonalInfo(
#         name="Mohamed Eltaher",
#         title="Full Stack Developer",
#         location="Sharjah, UAE",
#         email="dev.eltaher@gmail.com",
#         phone="+971585199391",
#         nationality="Sudanese"
#     ),
#     profile="Skilled in designing robust backends using Microservices Architecture...",
#     skills=Skills(
#         frontend=["HTML", "CSS", "Blazor", "JQuery", "JSON", "Angular", "React", "XML", "AJAX", "Bootstrap", "Javascript"],
#         backend=["C#", "ASP.NET Core", "AspNet MVC", "OOP", ".NET", ".NET Core", ".NET Framework", "Swagger", "AspNet Core", "WebForms", "RESTful API"],
#         database=["MSSQL", "MongoDB", "Dapper", "MySQL", "Entity Framework", "ADO.NET", "Cosmos DB", "Oracle"],
#         others=["Unit Testing", "NUnit", "Moq", "IIS", "Git", "TFS", "GitHub", "Azure", "Docker", "Agile", "Microservices", "MediatR", "RabbitMQ", "CQRS"]
#     ),
#     professional_experience=[
#         ProfessionalExperience(
#             role="Full Stack Developer",
#             company="Department of Municipal Affairs - Sharjah",
#             duration="11/2022 – Present",
#             location="Sharjah, UAE",
#             tools="C#, .NET, MediatR, RabbitMQ, Microservices, CQRS",
#             description="Develop and manage a comprehensive system for building and construction NOC management across Sharjah municipalities.",
#             achievements=[
#                 "Built a dynamic NOC management system that enables administrators to define customizable services, fields, and workflows for construction and building approvals.",
#                 "Used microservices architecture with MediatR for command and query separation (CQRS) and RabbitMQ for asynchronous message processing.",
#                 "Enabled efficient process control through an admin interface, simplifying service management across multiple municipalities."
#             ]
#         ),
#         # Other experiences would follow the same pattern
#     ],
#     education=[
#         Education(
#             degree="Bachelor in Computer Science",
#             institution="Alneelain University",
#             location="Khartoum, Sudan",
#             year="N/A"
#         )
#     ],
#     languages=["Arabic", "English"]
# )

# Convert to JSON
# print(mohamed_cv.json(indent=2))