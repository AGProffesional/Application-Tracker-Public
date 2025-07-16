from sqlalchemy import Boolean, Column, Date, Integer, String, Text

from app.database import Base


class Application(Base):
    __tablename__ = "applications"

    application_id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    company_name = Column(String)
    position_name = Column(String)
    application_status = Column(String)
    application_date = Column(Date)
    application_deadline = Column(Date)
    followed_up_status = Column(Boolean)
    interviewed_status = Column(Boolean)
    resume_link = Column(String)
    notes = Column(Text)
