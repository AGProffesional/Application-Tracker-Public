# app/routes.py
from typing import Union
from app.models import Application
from sqlalchemy.orm import Session
from app.database import SessionLocal
from fastapi import APIRouter,Depends
from pydantic import BaseModel 
router = APIRouter()

@router.get("/")
async def root():
    return{"message":"If you're seeing this, you should be in /Docs/"}

@router.post("/applications/{application_num}")
def read_application(application_num:int, q:Union[str,None]=None):
    return {"application_num":application_num, "q":q}

@router.put("/applications/{application_num}")
def update_application(application_num:int, application:Application):
    return{"application_num":application_num, "application":application.wordify()}

@router.get("/applications/")
def read_apps(db: Session = Depends(get_db)):
    return db.query(Application).all()