from html import entities
from sqlalchemy.orm import Session
from entities.chapter import Chapter
from models.database import db
from schemas import chapter

class ChapterModel():
    _entity = Chapter

    def create_chapter(chapter: chapter.ChapterCreate):
        db_chapter = Chapter(**chapter.dict())
        db.add(db_chapter)
        db.commit()
        db.refresh(db_chapter)
        return db_chapter