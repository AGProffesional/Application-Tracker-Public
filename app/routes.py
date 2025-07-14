# app/routes.py
from typing import Union, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Application as ApplicationModel
from app.utils import Wordify_application
from app.schemas import (
    ApplicationCreate,
    ApplicationUpdate,
    ApplicationResponse,
)
router = APIRouter()

@router.post("/applications/", response_model=ApplicationResponse)
def create_application(application: ApplicationCreate, db: Session = Depends(get_db)):
    new_app = ApplicationModel(**application.dict())
    db.add(new_app)
    db.commit()
    db.refresh(new_app)
    return new_app


@router.put("/applications/{application_id}", response_model=ApplicationResponse)
def update_application(application_id:int, updated_app:ApplicationUpdate, db:Session = Depends(get_db)):
    db_app = db.query(ApplicationModel).filter(ApplicationModel.application_id == application_id).first()
    if not db_app:
        raise HTTPException(status_code = 404, detail="Application not found")
    
    for field, value in updated_app.dict(exclude_unset=True).items():
        setattr(db_app,field,value)

    db.commit()
    db.refresh(db_app)
    return Wordify_application(db_app) 

@router.get("/applications/{application_id}", response_model=ApplicationResponse)
def get_application(application_id: int, db: Session = Depends(get_db)):
    db_app = db.query(ApplicationModel).filter(ApplicationModel.application_id == application_id).first()
    if not db_app:
        raise HTTPException(status_code=404, detail="Application not found")
    return Wordify_application(db_app)

@router.get("/applications/")
def get_all_applications(db: Session = Depends(get_db)):
    db_apps = db.query(ApplicationModel).all()
    return [Wordify_application(app) for app in db_apps]

