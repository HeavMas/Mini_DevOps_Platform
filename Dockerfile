FROM python:3.12-slim
WORKDIR /app/Mini_DevOps_Platform
COPY . .
RUN pip3 install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]