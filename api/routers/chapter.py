from fastapi import APIRouter
from pydantic import BaseModel
from models.chapter import ChapterModel
from schemas import chapter

router = APIRouter()

@router.post('/chapter')
def post_chapter(chapter: chapter.ChapterCreate):
    return ChapterModel.create_chapter(chapter=chapter)
