from html import entities
from sqlalchemy.orm import Session
from entities.type import Type
from models.database import db
from schemas import type

class TypeModel():
    _entity = Type