from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class  Member(Base):
    __tablename__ = 'member'
    id = Column(Integer, primary_key=True)
    name = Column(String,nullable=False)
    type=Column(String,nullable=False)
