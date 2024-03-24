FROM python:3.11-slim

COPY requirements.txt .
COPY server.py .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD [ "python", "./server.py" ]
