from pydantic import BaseModel
from datetime import date
from pydantic import Optional

class Application(BaseModel):
    company_name: str
    position_name:str
    application_status: str
    application_date: date
    application_deadline:Optional[date] = None
    followed_up_status:bool
    interviewed:bool
    resume_link:str
    notes: Optional[str] = None

    def wordify(self) -> dict:
     return{
        "company_name":self.company_name,
        "position_name":self.position_name,
        "application_status": self.application_status,
        "application_date": self.application_date,
        "application_deadline": self.application_deadline,
        "followed_up_status": "Yes" if self.followed_up_status else "No",
        "interviewed": "Yes" if self.interviewed else "No",
        "resume_link": self.resume_link,
        "Notes":self.notes
     }

