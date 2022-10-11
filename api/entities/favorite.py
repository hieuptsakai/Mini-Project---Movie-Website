from sqlalchemy.sql.sqltypes import DateTime, SmallInteger, Boolean
from sqlalchemy import Column, Integer, String
from models.database import Base

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    userid = Column(Integer)
    mangaid = Column(Integer)