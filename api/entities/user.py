from sqlalchemy.sql.sqltypes import DateTime, SmallInteger, Boolean
from sqlalchemy import Column, Integer, String
from models.database import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    usertypeid = Column(Integer)
    username = Column(String)
    status = Column(Boolean, default=True)
    user_code = Column(String)
