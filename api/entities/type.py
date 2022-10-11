from sqlalchemy.sql.sqltypes import DateTime, SmallInteger, Boolean
from sqlalchemy import Column, Integer, String
from models.database import Base

class Type(Base):
    __tablename__ = 'type'
    id  = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    m_type = Column(String)