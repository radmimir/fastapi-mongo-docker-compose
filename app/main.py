from fastapi import FastAPI
from starlette.responses import RedirectResponse
from model.employee import Employee
from pymongo import MongoClient
from typing import List
from model.database import retrieve_employees
import logging
from os import environ

app = FastAPI(title="Employees API")

global client


@app.on_event("startup")
async def on_startup():
    global client
    client = MongoClient(environ.get("MONGO_URI"))
    logging.info("Created MongoDB connection")


@app.on_event("shutdown")
async def on_shutdown():
    global client
    client.close()
    logging.info("Closed MongoDB connection")


@app.get("/employees", response_description="Employees retrieved", tags=["All"], response_model=List[Employee])
async def get_employees():
    global client
    employees = retrieve_employees(client)
    if employees:
        return employees
    return


@app.get("/age_less_25", response_description="Employees with age less 25 retrieved", tags=['Age < 25'],
         response_model=List[Employee])
async def get_age_less_25():
    global client
    employees = retrieve_employees(client)  # , "{age: { $lt: 25}}")
    if employees:
        return employees
    return []
