from pydantic import BaseModel, EmailStr, Field
from bson.objectid import ObjectId


class Employee(BaseModel):
    _id: hex = ObjectId()
    name: str = Field(...)
    email: EmailStr = Field(...)
    age: int = Field(...)
    company: str = Field(...)
    join_date: str = Field(...)
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

