from pydantic import BaseModel
from pydantic import ConfigDict
from datetime import date
from typing import Optional


class ApplicationCreate(BaseModel):
    user_id:int
    company_name: str
    position_name:str
    application_status: str
    application_date: date
    application_deadline:Optional[date] = None
    followed_up_status:bool
    interviewed_status:bool
    resume_link:str
    notes: Optional[str] = None


class ApplicationUpdate(BaseModel):
    user_id: Optional[int] = None
    company_name: Optional[str] = None
    position_name: Optional[str] = None
    application_status: Optional[str] = None
    application_date: Optional[date] = None
    application_deadline: Optional[date] = None
    followed_up_status: Optional[bool] = None
    interviewed_status: Optional[bool] = None
    resume_link: Optional[str] = None
    notes: Optional[str] = None

class ApplicationResponse(BaseModel):
    application_id:int
    user_id:int
    company_name: str
    position_name:str
    application_status: str
    application_date: date
    application_deadline:Optional[date] = None
    followed_up_status:bool
    interviewed_status:bool
    resume_link:str
    notes: Optional[str] = None
        
    model_config = ConfigDict(from_attributes=True)