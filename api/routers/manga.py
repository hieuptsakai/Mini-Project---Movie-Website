from fastapi import APIRouter
from pydantic import BaseModel
from models.manga import MangaModel
from schemas import manga   

router = APIRouter()

@router.post('/manga')
def post_manga(manga: manga.MangaCreate):
    return MangaModel.create_manga(manga = manga)