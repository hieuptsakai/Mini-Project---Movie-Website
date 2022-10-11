from pydantic import BaseModel

class MangaBase(BaseModel):
    name: str
    genre: set[str] = set()
    author: str
    summary: str | None = None
    images: list[int] = []

class MangaCreate(MangaBase):
    pass

class Manga(MangaBase):

    class Config:
        orm_mode = True