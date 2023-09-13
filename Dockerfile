from asdkant/fastapi-hello-world:latest
EXPOSE 3000
ENTRYPOINT ["uvicorn", "main:app" ,"--reload"]
