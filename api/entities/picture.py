from enum import auto
from sqlalchemy.sql.sqltypes import DateTime, SmallInteger, Boolean, ARRAY
from sqlalchemy import Column, Integer, String
from models.database import Base

class Picture(Base):
    __tablename__ = 'type'
    id  = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    url = Column(String)
    array = Column(Integer)
