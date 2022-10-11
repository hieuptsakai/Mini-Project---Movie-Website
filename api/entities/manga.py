from enum import auto
from sqlalchemy.sql.sqltypes import DateTime, SmallInteger, Boolean, ARRAY
from sqlalchemy import Column, Integer, String
from models.database import Base

class Manga(Base):
    __tablename__ = 'manga'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String)
    genre = Column(ARRAY(String),nullable=False)
    author = Column(String)
    summary = Column(String)
    images = Column(ARRAY(Integer),nullable=False)