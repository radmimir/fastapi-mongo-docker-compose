import datetime
from pydantic import BaseModel, EmailStr, Field


class Employee(BaseModel):
    name: str = Field(...)
    email: EmailStr = Field(...)
    age: int = Field(...)
    company: str = Field(...)
    join_date: datetime.date = Field(...)
    job_title: str = Field(...)
    gender: str = Field(...)
    salary: int = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Steve Jobs",
                "email": "jobs@mail.ru",
                "age": "25",
                "company": "Apple",
                "join_date": "25.12.2020",
                "job_title": "Developer",
                "gender": "male",
                "salary": 10000
            }
        }


def responseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def errorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
