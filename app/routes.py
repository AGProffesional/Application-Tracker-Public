# app/routes.py
from fastapi import APIRouter, Depends, HTTPException, Request, Query
from sqlalchemy.orm import Session
from typing import Optional
from datetime import date as datetimedate

from app.database import get_db
from app.extensions import limiter
from app.models import Application as ApplicationModel
from app.schemas import ApplicationCreate, ApplicationResponse, ApplicationUpdate
from app.utils import Wordify_application

router = APIRouter()


@router.post("/applications/", response_model=ApplicationResponse)
@limiter.limit("5/minute")
def create_application(
    application: ApplicationCreate, request: Request, db: Session = Depends(get_db)
):
    new_app = ApplicationModel(**application.model_dump())
    db.add(new_app)
    db.commit()
    db.refresh(new_app)
    return new_app


@router.put("/applications/{application_id}", response_model=ApplicationResponse)
@limiter.limit("10/minute")
def update_application(
    application_id: int,
    updated_app: ApplicationUpdate,
    request: Request,
    db: Session = Depends(get_db),
):
    db_app = (
        db.query(ApplicationModel)
        .filter(ApplicationModel.application_id == application_id)
        .first()
    )
    if not db_app:
        raise HTTPException(status_code=404, detail="Application not found")

    for field, value in updated_app.dict(exclude_unset=True).items():
        setattr(db_app, field, value)

    db.commit()
    db.refresh(db_app)
    return Wordify_application(db_app)

@router.get("/applications/search", response_model=list[ApplicationResponse])
@limiter.limit("3/minute")
def search_applications(
    request: Request,
    company_name: Optional[str] = Query(None),
    position_name: Optional[str] = Query(None),
    application_status: Optional[str] = Query(None),
    start_date: Optional[datetimedate] = Query(None),
    end_date: Optional[datetimedate] = Query(None),
    application_deadline:Optional[datetimedate] = Query(None),
    followed_up_status: Optional[bool] = Query(None),
    interviewed_status: Optional[bool] = Query(None),
    db: Session = Depends(get_db),
):
    query = db.query(ApplicationModel)

    if company_name:
        query = query.filter(ApplicationModel.company_name.ilike(f"%{company_name}%"))
    if position_name:
        query = query.filter(ApplicationModel.position_name.ilike(f"%{position_name}%"))
    if application_status:
        query = query.filter(ApplicationModel.application_status.ilike(f"%{application_status}%"))
    if start_date and end_date:
        query = query.filter(ApplicationModel.application_date.between(start_date, end_date))
    elif start_date:
        query = query.filter(ApplicationModel.application_date >= start_date)
    elif end_date:
        query = query.filter(ApplicationModel.application_date <= end_date)
    if application_deadline:
        query = query.filter(ApplicationModel.application_deadline == application_deadline)
    if followed_up_status is not None:
        query= query.filter(ApplicationModel.followed_up_status)
    if interviewed_status is not None:
        query = query.filter(ApplicationModel.interviewed_status)

    results = query.all()
    return [Wordify_application(app) for app in results]


@router.get("/applications/")
@limiter.limit("3/minute")
def get_all_applications(request: Request, db: Session = Depends(get_db)):
    db_apps = db.query(ApplicationModel).all()
    return [Wordify_application(app) for app in db_apps]


@router.delete("/applications/{application_id}")
@limiter.limit("3/minute")
def delete_applications(
    application_id: int, request: Request, db: Session = Depends(get_db)
):
    db_app = (
        db.query(ApplicationModel)
        .filter(ApplicationModel.application_id == application_id)
        .first()
    )
    if not db_app:
        raise HTTPException(status_code=404, detail="Application not found")
    db.delete(db_app)
    db.commit()
