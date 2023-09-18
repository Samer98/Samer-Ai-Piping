from python:3.8.10-slim
WORKDIR /app
COPY . .
RUN pip install -r ./requirements.txt
EXPOSE 3000
# ENV openai_key
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]
