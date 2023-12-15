import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv
import os
from app.routes import router

load_dotenv()

app = FastAPI()
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host=os.environ['APP_URL'], port=int(os.environ['APP_PORT']))
