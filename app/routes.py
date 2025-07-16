# app/routes.py
from typing import Union, List
from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Application as ApplicationModel
from app.utils import Wordify_application
from app.schemas import (
    ApplicationCreate,
    ApplicationUpdate,
    ApplicationResponse,
)
from app.extensions import limiter


router = APIRouter()

@router.post("/applications/", response_model=ApplicationResponse)
@limiter.limit("5/minute")
def create_application(application: ApplicationCreate, request:Request, db: Session = Depends(get_db)):
    new_app = ApplicationModel(**application.model_dump())
    db.add(new_app)
    db.commit()
    db.refresh(new_app)
    return new_app


@router.put("/applications/{application_id}", response_model=ApplicationResponse)
@limiter.limit("10/minute")
def update_application(application_id:int, updated_app:ApplicationUpdate, request: Request, db:Session = Depends(get_db)):
    db_app = db.query(ApplicationModel).filter(ApplicationModel.application_id == application_id).first()
    if not db_app:
        raise HTTPException(status_code = 404, detail="Application not found")
    
    for field, value in updated_app.dict(exclude_unset=True).items():
        setattr(db_app,field,value)

    db.commit()
    db.refresh(db_app)
    return Wordify_application(db_app) 

@router.get("/applications/{application_id}", response_model=ApplicationResponse)
@limiter.limit("5/minute")
def get_application(application_id: int,request:Request,db: Session = Depends(get_db)):
    db_app = db.query(ApplicationModel).filter(ApplicationModel.application_id == application_id).first()
    if not db_app:
        raise HTTPException(status_code=404, detail="Application not found")
    return Wordify_application(db_app)

@router.get("/applications/")
@limiter.limit("3/minute")
def get_all_applications(request: Request, db: Session = Depends(get_db)):
    db_apps = db.query(ApplicationModel).all()
    return [Wordify_application(app) for app in db_apps]

@router.delete("/applications/{application_id}")
@limiter.limit("3/minute")
def delete_applications(application_id: int,request:Request,db: Session = Depends(get_db)):
    db_app = db.query(ApplicationModel).filter(ApplicationModel.application_id == application_id).first()
    if not db_app:
        raise HTTPException(status_code=404, detail="Application not found")
    db.delete(db_app)
    db.commit()

