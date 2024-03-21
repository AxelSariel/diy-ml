FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
COPY server.py .

RUN pip install -r requirements.txt

EXPOSE 5000
