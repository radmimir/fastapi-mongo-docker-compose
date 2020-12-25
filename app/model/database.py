from pymongo import MongoClient

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
