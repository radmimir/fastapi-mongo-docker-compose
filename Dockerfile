FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY app /app
WORKDIR /app
RUN "/usr/local/bin/python -m pip install --upgrade pip"
