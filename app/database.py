#Creating the database structure
from sqlalchemy import Column,Integer,String,Date,Text,Foreign_key
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import sessionmaker

Base = declarative_base

class Application(Base):
    __tablename__ = "applications"

    application_id = Column(Integer, primary_key = True)
    user_id = Column(Integer, Foreign_key = True)
    company = Column(String)
    position = Column(String)
    status = Column(String)
    deadline = Column(Date)
    resume_link = Column(String)
    notes= Column(Text)

DATABASE_URL = "postgresql+psycopg2://username:password@localhost:5432/dbname"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()