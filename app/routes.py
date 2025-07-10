# app/routes.py
from typing import Union
from fastapi import APIRouter
from pydantic import BaseModel
router = APIRouter()

class Application(BaseModel):
    company_name: str
    position_name:str
    application_status: bool
    followed_up_status:bool
    interviewed:bool

    def wordify(self) -> dict:
     return{
        "company_name":self.company_name,
        "position_name":self.position_name,
        "application_status": "Applied" if self.application_status else "Rejected",
        "followed_up_status": "Yes" if self.followed_up_status else "No",
        "interviewed": "Yes" if self.interviewed else "No"
     }




@router.get("/")
async def root():
    return{"message":"Hello, World!"}

@router.post("/applications/{application_num}")
def read_application(application_num:int, q:Union[str,None]=None):
    return {"application_num":application_num, "q":q}

@router.put("/applications/{application_num}")
def update_application(application_num:int, application:Application):
    return{"application_num":application_num, "application":application.wordify()}