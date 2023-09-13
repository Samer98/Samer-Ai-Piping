from python:3.8.10-slim
WORKDIR /app
COPY . .
RUN pip install -r ./requirements.txt
EXPOSE 3000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
