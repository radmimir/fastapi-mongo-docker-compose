from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.son import SON


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


def retrieve_employees(client: MongoClient):
    db_employees = client.get_database("employees")
    collection_employees = db_employees.get_collection("employee")
    results = list(map(employee_helper, [r for r in collection_employees.find()]))
    return results


def retrieve_employee(client: MongoClient, id: str):
    db_employees = client.get_database("employees")
    collection_employees = db_employees.get_collection("employee")
    employee = collection_employees.find_one({"_id": ObjectId(id)})
    if employee:
        return employee_helper(employee)


def employees_age_less(client: MongoClient, age: int):
    db_employees = client.get_database("employees")
    collection_employees = db_employees.get_collection("employee")
    query = {"age": {"$lt": age}}
    results = list(map(employee_helper, [r for r in collection_employees.find(query)]))
    return results
