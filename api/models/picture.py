from html import entities
from sqlalchemy.orm import Session
from entities.picture import Picture
from models.database import db
from schemas import picture

class PictureModel():
    _entity = Picture