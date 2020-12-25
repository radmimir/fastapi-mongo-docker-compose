# FastAPI example app
FastAPI + MongoDB web application

Quickstart 
----------
1. Create environment variables::
```
   export MONGO_USERNAME=<your_username>
   expore MONGO_PASSWORD=<your_password>
```
2. Clone project::
```
    git clone https://github.com/radmimir/fastapi-mongo-docker-compose
    cd PlarinNet
```
3. Edit ``.env`` file in project root and set environment variables for application::
```
    touch .env
    echo MONGO_USERNAME=$MONGO_USERNAME >> .env
    echo $MONGO_PASSWORD=$MONGO_PASSWORD >> .env
```
4. Run application in testing mode::
```
    python test.py
```
Deployment with Docker-compose
----------------------

You must have ``docker`` and ``docker-compose`` tools installed to work with material in this section.
First, create or modify ``.env`` file like in `Quickstart` section.
Then just run in ``/`` section of project::
```
    docker-compose up -d 
```
Application will be available on ``localhost:8080`` in your browser.

Web routes
----------

Routes are available on ``/docs`` or ``/redoc`` paths with Swagger or ReDoc.

Manual testing responces
----------

1. Get all employees in database::
```
   curl -X GET "http://0.0.0.0:8080/age_less?age=25" -H  "accept: application/json"
```
2. Get employee by id (replace {ID} with ID you're looking for)::
```
    curl -X GET "http://0.0.0.0:8080/employee/{ID}" -H  "accept: application/json"
```
3. Get employee with age less than {age}: ::
```
   curl -X GET "http://0.0.0.0:8080/employee/{age}" -H  "accept: application/json"
```

TODO
----------

1. Add more unittests
2. Full authentification on mongo
3. AsyncIOMotor usage in FastAPI
