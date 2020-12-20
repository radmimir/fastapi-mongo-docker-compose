FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./code /app
WORKDIR /app
RUN "/usr/local/bin/python -m pip install --upgrade pip"
