from fastapi import FastAPI
from app.routes import router
from pydantic import BaseModel
from app.models import Base
from app.database import engine 

app= FastAPI()
app.include_router(router)

Base.metadata.create_all(bind=engine)

