from fastapi import FastAPI
from model.employee import responseModel
from model.database import client, retrieve_employees, connect_to_db
import logging

app = FastAPI(title="Employees API")

@app.on_event("startup")
async def startup_db_client():
    await connect_to_db()

@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()


@app.get("/", response_description="Employees retrieved")
async def get_employees():
    logging.info("Get employees request")
    employees = await retrieve_employees()
    if employees:
        return responseModel(employees, "Employees data retrieved successfully")
    return responseModel(employees, "Empty list returned")


