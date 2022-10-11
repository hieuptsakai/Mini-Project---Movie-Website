from html import entities
from sqlalchemy.orm import Session
from entities.manga import Manga
from models.database import db
from schemas import manga

class MangaModel():
    _entity = Manga

    def create_manga(manga: manga.MangaCreate):
        db_manga = Manga(**manga.dict())
        db.add(db_manga)
        db.commit()
        db.refresh(db_manga)
        return db_manga
