from fastapi import APIRouter
from pydantic import BaseModel
from models.favorite import FavoriteModel
from schemas import favorite

router = APIRouter()

