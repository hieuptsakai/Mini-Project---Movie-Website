from sqlalchemy.sql.sqltypes import DateTime, SmallInteger, Boolean, ARRAY
from sqlalchemy import Column, Integer, String
from models.database import Base

class Chapter(Base):
    __tablename__ = 'chapter'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    chapter_num = Column(Integer)
    mangaid = Column(Integer)
    images = Column(ARRAY(Integer),nullable=False)