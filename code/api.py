from typing import List
from fastapi import FastAPI
from pymongo import MongoClient
from odmantic import Model, ObjectId, AIOEngine
from motor.motor_asyncio import AsyncIOMotorClient
import datetime
import json


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
# client = MongoClient('localhost', 27017)
app = FastAPI(title='SimpleAPI')
engine = AIOEngine(motor_client=client, database="employees_db")


@app.on_event("startup")
async def create_db_client():
    db = client['employees']
    collection_employees = db['employer']
    with open('./code/employees.json') as f:
        employees = json.load(f)

    collection_employees.insert_many(employees)
    print('completed')


@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/employees', response_model=List[Employer])
async def get_employees():
    employees = await engine.find(Employer)
    return employees
