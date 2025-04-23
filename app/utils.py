from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import json

# SQL Server connection string

username = ""
password = "" # Escapes special characters
server = "DESKTOP-LIB7CJS"
database = "JobSeekerDB"



SQLALCHEMY_DATABASE_URL = f"mssql+pyodbc://@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"
# Create the SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for our models
Base = declarative_base()

class Jobseeker(Base):
    __tablename__ = "jobseekers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    resume = Column(String)


def insert_or_update_jobseeker(db: Session, name: str, email: str, resume: dict):
    serialized_resume = json.dumps(resume)  # Serialize the resume dictionary to a JSON string
    existing_jobseeker = db.query(Jobseeker).filter(Jobseeker.email == email).first()
    if existing_jobseeker:
        existing_jobseeker.resume = serialized_resume
        db.commit()
        db.refresh(existing_jobseeker)
        return existing_jobseeker
    else:
        new_jobseeker = Jobseeker(name=name, email=email, resume=serialized_resume)
        db.add(new_jobseeker)
        db.commit()
        db.refresh(new_jobseeker)
        return new_jobseeker
