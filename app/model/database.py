import motor.motor_asyncio
from motor.motor_asyncio import AsyncIOMotorCollection
import logging

MONGO_DETAILS = "mongodb://localhost:27017/test"

collection_employees = AsyncIOMotorCollection()
client = motor.motor_asyncio.AsyncIOMotorClient()


def connect_to_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
    db_employees = client.test

    collection_employees = db_employees.get_collection("employee")
    logging.info("Connected to DB")


# helpers


def employee_helper(employee) -> dict:
    return {
        "id": str(employee["_id"]),
        "name": str(employee["name"]),
        "email": employee["email"],
        "age": employee["age"],
        "company": employee["company"],
        "join_date": employee["join_date"],
        "job_title": employee["job_title"],
        "gender": employee["gender"],
        "salary": employee["salary"]
    }


async def retrieve_employees():
    employees = []
    logging.info(collection_employees.employee)
    async for employee in collection_employees.find():
        employees.append(employee_helper(employee))
        logging.info("retrieved ", employee)
    return employees
