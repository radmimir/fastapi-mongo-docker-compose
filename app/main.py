from fastapi import FastAPI
from starlette.responses import RedirectResponse
from model.employee import Employee
from pymongo import MongoClient
from typing import List
from model.database import retrieve_employees, retrieve_employee, employees_age_less
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


@app.get("/age_less", response_description="Employees with age less retrieved", tags=['Age less'],
         response_model=List[Employee])
async def get_age_less(age: int):
    global client
    employees = employees_age_less(client, age)  # , "{age: { $lt: 25}}")
    if employees:
        return employees
    return []


@app.get("/employee/{id}", response_description="Employees with id retrieved", tags=['Id'],
         response_model=List[Employee])
async def get_employee_by_id(id: str):
    global client
    employees = retrieve_employee(client, id)
    if employees:
        return employees
    return []