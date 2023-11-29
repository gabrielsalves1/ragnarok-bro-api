import uvicorn
from fastapi import FastAPI
import app.models
from app.routes import router
from app.config import engine

app.models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000)