from html import entities
from sqlalchemy.orm import Session
from entities.favorite import Favorite
from models.database import db
from schemas import favorite

class FavoriteModel():
    _entity = Favorite