from typing import List
from fastapi import FastAPI
from odmantic import Model, AIOEngine
from motor.motor_asyncio import AsyncIOMotorClient
import datetime
import logging


class Employer(Model):
    name: str
    email: str
    age: int
    company: str
    join_date: datetime.date
    job_title: str
    gender: str
    salary: str


client = AsyncIOMotorClient("mongodb://localhost:27017/")
app = FastAPI(title="Employees API")
# engine = AIOEngine(motor_client=client, database="employees_db")
db_employees = client.employees
collection_employees = db_employees.get_collection("employee")
logging.info("Connecting to MongoDB")


@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()


@app.get('/employees', response_model=List[Employer])
async def get_employees():
    employees = []
    async for employee in collection_employees.find(Employer):
        print(employee)
        employees.append(employee)
    return employees
