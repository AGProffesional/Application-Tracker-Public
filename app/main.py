from fastapi import FastAPI
from app.routes import router
from pydantic import BaseModel
from app.models import Application
from app.database import engine, Base

print("Tables registered in metadata:", Base.metadata.tables.keys())
Base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(router)



